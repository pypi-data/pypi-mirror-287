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

from .autoencoder.codec import MyEncoder
from .magvit2.codec import Decoder
from .data import get_or_create_directory, get_dataset
from .vq.hyperball import HyperSphere


class VQAE(nn.Module):
    def __init__(self, encoder_conf, decoder_conf, quan_conf):
        super().__init__()
        self.encoder = MyEncoder(**encoder_conf)
        self.decoder = Decoder(**decoder_conf)
        self.quantizer = HyperSphere(**quan_conf)
        self.adaptor = nn.Linear(encoder_conf['compressed_seq_length'], encoder_conf['original_seq_length'])
        self.target_channels = encoder_conf['target_channels']
        self.patch_size = encoder_conf['patch_size']

    def forward(self, x, return_q=True):
        """x - images [NCHW]
        return_q - if True, return `r` (recons images [NCHW]), and optional `vqres` (quantized info)
        """
        z, _ = self.encoder(x)
        vqres = self.quantizer(z)
        t = self.adaptor(vqres.quantized)
        y = t.view(-1, self.target_channels, self.patch_size, self.patch_size)
        r = self.decoder(y)
        return r, vqres if return_q else r