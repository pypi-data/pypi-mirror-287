from .magvit2.codec import Encoder, Decoder
import torch.nn as nn
from .vq.hyperball import HyperSphere


class VQAE(nn.Module):
    def __init__(self, encoder_conf, decoder_conf, quan_conf):
        super().__init__()
        self.encoder = Encoder(**encoder_conf)
        self.decoder = Decoder(**decoder_conf)
        self.quantizer = HyperSphere(**quan_conf)

    def forward(self, x, return_q=True):
        """x - images [NCHW]
        return_q - if True, return `r` (recons images [NCHW]), and optional `vqres` (quantized info)
        """
        z = self.encoder(x)
        vqres = self.quantizer(z)
        r = self.decoder(vqres.quantized)
        return r, vqres if return_q else r
