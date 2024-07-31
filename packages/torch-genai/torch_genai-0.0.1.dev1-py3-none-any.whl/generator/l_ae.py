import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.utils as vutils
from torch.utils.data import DataLoader
import pytorch_lightning as pl
from hiq.cv_torch import get_cv_dataset, DS_PATH_OXFLOWER_7K, ensure_split
import wandb
from pytorch_lightning.loggers import WandbLogger
import os
from pytorch_lightning.callbacks import ModelCheckpoint
from autoencoder.codec import MyEncoder, MyDecoder
from data import get_or_create_directory, get_dataset


class AutoEncoder(pl.LightningModule):
    def __init__(self, encoder, decoder, args):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.learning_rate = args.learning_rate
        self.criterion = nn.MSELoss()
        self.num_epochs = args.epochs
        self.automatic_optimization = False  # Disable automatic optimization

    def forward(self, x):
        compressed_output, _ = self.encoder(x)
        recovered_output, _ = self.decoder(compressed_output)
        return recovered_output

    def training_step(self, batch, batch_idx):
        x, _ = batch
        recovered_output = self(x)
        loss = self.criterion(recovered_output, x)

        # Manual optimization
        encoder_optimizer, decoder_optimizer = self.optimizers()
        encoder_optimizer.zero_grad()
        decoder_optimizer.zero_grad()
        self.manual_backward(loss)
        encoder_optimizer.step()
        decoder_optimizer.step()

        # Log learning rate
        self.log("lr_encoder", encoder_optimizer.param_groups[0]["lr"])
        self.log("lr_decoder", decoder_optimizer.param_groups[0]["lr"])
        self.log("train_loss", loss)

        # Log images and loss to WandB
        if batch_idx == 0 and self.current_epoch % 10 == 0:
            comparison_grid = vutils.make_grid(
                torch.cat((x[:3], recovered_output[:3]), dim=0),
                nrow=3,
                normalize=True,
                scale_each=True,
            )
            self.logger.experiment.log(
                {
                    "comparison_images": [
                        wandb.Image(
                            comparison_grid, caption="Original and Reconstructed Images"
                        )
                    ],
                    "epoch": self.current_epoch,
                }
            )
        return loss

    def validation_step(self, batch, batch_idx):
        x, _ = batch
        recovered_output = self(x)
        loss = self.criterion(recovered_output, x)
        self.log("val_loss", loss)

        # Log images and loss to WandB
        if batch_idx == 0 and self.current_epoch % 10 == 0:
            comparison_grid = vutils.make_grid(
                torch.cat((x[:3], recovered_output[:3]), dim=0),
                nrow=3,
                normalize=True,
                scale_each=True,
            )
            self.logger.experiment.log(
                {
                    "val_comparison_images": [
                        wandb.Image(
                            comparison_grid,
                            caption="Validation Original and Reconstructed Images",
                        )
                    ],
                    "epoch": self.current_epoch,
                }
            )
        return loss

    def configure_optimizers(self):
        encoder_optimizer = optim.Adam(self.encoder.parameters(), lr=self.learning_rate)
        decoder_optimizer = optim.Adam(self.decoder.parameters(), lr=self.learning_rate)
        encoder_scheduler = optim.lr_scheduler.CosineAnnealingLR(
            encoder_optimizer, T_max=self.num_epochs, eta_min=5e-6
        )
        decoder_scheduler = optim.lr_scheduler.CosineAnnealingLR(
            decoder_optimizer, T_max=self.num_epochs, eta_min=5e-6
        )
        return [encoder_optimizer, decoder_optimizer], [
            encoder_scheduler,
            decoder_scheduler,
        ]

    def on_train_epoch_end(self):
        # Step schedulers
        enc_scheduler, dec_scheduler = self.lr_schedulers()
        enc_scheduler.step()
        dec_scheduler.step()


def create_ae(args):
    from hiq import print_model

    d_model = args.d_model
    qk_dim = args.qk_dim
    v_dim = args.v_dim
    n_head = args.n_head
    original_seq_length = args.original_seq_length
    compressed_seq_length = args.compressed_seq_length
    PATCHSIZE = args.patch_size

    # Initialize the models
    encoder = MyEncoder(
        d_model=d_model,
        qk_dim=qk_dim,
        v_dim=v_dim,
        n_head=n_head,
        original_seq_length=original_seq_length,
        patch_size=PATCHSIZE,
        compressed_seq_length=compressed_seq_length,
        tiny_latent=args.tiny_latent,
        num_layers=args.num_layers,
        target_channels=args.book_hidden_dim,
    )

    decoder = MyDecoder(
        d_model=d_model,
        qk_dim=qk_dim,
        v_dim=v_dim,
        n_head=n_head,
        compressed_seq_length=compressed_seq_length,
        original_seq_length=original_seq_length,
        patch_size=PATCHSIZE,
        image_size=args.image_size,
        tiny_latent=args.tiny_latent,
        num_layers=args.num_layers,
        target_channels=args.book_hidden_dim,
    )
    print_model(encoder)
    print_model(decoder)

    # Initialize PyTorch Lightning model
    model = AutoEncoder(encoder, decoder, args)
    return model


def train(args, proj="TransReprV3"):
    # Initialize WandB logger
    wandb_logger = WandbLogger(project=proj)

    # Initialize PyTorch Lightning model
    model = create_ae(args)

    checkpoint_callback = ModelCheckpoint(
        dirpath=get_or_create_directory(args.resume),
        filename="{epoch}-{val_loss:.2f}",
        save_top_k=1,
        mode="min",
        monitor="val_loss",
        save_last=False,
    )

    # Initialize PyTorch Lightning trainer
    trainer = pl.Trainer(
        max_epochs=args.epochs,
        logger=wandb_logger,
        accelerator="gpu" if torch.cuda.is_available() else "cpu",
        devices=args.world_size if torch.cuda.is_available() else 1,
        callbacks=[checkpoint_callback],
    )

    # Initialize DataLoader
    train_loader, test_loader = get_dataset(args)

    # Train the model
    if os.path.exists(args.resume) and os.path.isfile(args.resume):
        trainer.fit(model, train_loader, test_loader, ckpt_path=args.resume)
    else:
        trainer.fit(model, train_loader, test_loader)


if __name__ == "__main__":
    import argparse
    from hiq import ensure_folder

    torch.backends.cudnn.benchmark = True

    parser = argparse.ArgumentParser(description="Train Fuheng's Model")
    num_gpus = torch.cuda.device_count()
    BATCH_SIZE = 16
    parser.add_argument(
        "--batch_size", type=int, default=BATCH_SIZE, help="Batch size for training"
    )
    parser.add_argument(
        "--learning_rate", type=float, default=1e-4, help="Initial learning rate"
    )
    parser.add_argument(
        "--weight_decay", type=float, default=1e-4, help="Weight decay for optimizer"
    )
    parser.add_argument(
        "--epochs", type=int, default=100, help="Number of training epochs"
    )
    parser.add_argument(
        "--image_size", type=int, default=256, help="Size of the input images"
    )
    parser.add_argument(
        "--max_num", type=int, default=int(1e10), help="Maximum number of images"
    )
    parser.add_argument(
        "--dataset",
        type=str,
        default=DS_PATH_OXFLOWER_7K,
        help="Dataset to use for training",
    )
    parser.add_argument(
        "--world_size",
        type=int,
        default=torch.cuda.device_count(),
        help="Number of GPUs to use",
    )
    parser.add_argument(
        "--resume", type=str, default="./mbin", help="Path to the latest checkpoint"
    )
    parser.add_argument(
        "--d_model", type=int, default=1024, help="Dimension of the model"
    )
    parser.add_argument(
        "--qk_dim", type=int, default=64, help="Dimension of the query and key"
    )
    parser.add_argument("--v_dim", type=int, default=64, help="Dimension of the value")
    parser.add_argument(
        "--n_head", type=int, default=8, help="Number of attention heads"
    )
    parser.add_argument(
        "--original_seq_length",
        type=int,
        default=256,
        help="Length of the original sequence",
    )
    parser.add_argument(
        "--compressed_seq_length",
        type=int,
        default=64,
        help="Length of the compressed sequence",
    )
    parser.add_argument(
        "--patch_size", type=int, default=16, help="Size of each image patch"
    )
    parser.add_argument("--num_layers", type=int, default=3, help="layers")
    parser.add_argument(
        "--book_hidden_dim", type=int, default=12, help="dim of code book"
    )
    parser.add_argument("--tiny_latent", type=int, default=0, help="compress to 32x12")
    args = parser.parse_args()
    train(args)

"""
DS_PATH_OXFLOWER_7K = "nelorth/oxford-flowers"  # 8k
DS_PATH_FFHQ256_70K = "merkol/ffhq-256"
DS_PATH_FFHQ512_30K = "cld07/captioned_ffhq_512"
"""
