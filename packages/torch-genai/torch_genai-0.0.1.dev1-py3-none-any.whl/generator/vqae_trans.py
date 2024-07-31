import os

import pytorch_lightning as pl
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.utils as vutils
import wandb
from hiq.cv_torch import get_cv_dataset, DS_PATH_OXFLOWER_7K, ensure_split
from pytorch_lightning.callbacks import ModelCheckpoint
from pytorch_lightning.loggers import WandbLogger
from torch.utils.data import DataLoader

from .autoencoder.codec import MyEncoder, MyDecoder
from .data import get_or_create_directory, get_dataset
from .vq.hyperball import HyperSphere


class VQAE(nn.Module):
    def __init__(self, encoder_conf, decoder_conf, quan_conf):
        super().__init__()
        self.encoder = MyEncoder(**encoder_conf)
        self.decoder = MyDecoder(**decoder_conf)
        self.quantizer = HyperSphere(**quan_conf)

    def forward(self, x, return_q=True):
        """x - images [NCHW]
        return_q - if True, return `r` (recons images [NCHW]), and optional `vqres` (quantized info)
        """
        z, _ = self.encoder(x)
        vqres = self.quantizer(z)
        r, _ = self.decoder(vqres.quantized)
        return r, vqres if return_q else r
