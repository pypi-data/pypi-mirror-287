import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from .autoencoder.codec import MyEncoder, MyDecoder
from .vq.common import VQRes, T0
#from .magvit2.codec import Decoder


class vMF:
    def __init__(self, latent_dim=3, kappa = 20, epsilon=1e-7):
        self.pool_size = 10**6
        x = np.arange(-1 + epsilon, 1, epsilon)
        y = kappa * x + np.log(1 - x ** 2) * (latent_dim - 3) / 2
        y = np.cumsum(np.exp(y - y.max()))
        y = y / y[-1]
        self.W = torch.tensor(np.interp(np.random.random(self.pool_size), y, x), dtype=torch.float32)
        self.latent_dim = latent_dim

    def reparameterize(self, mu):
        original_shape = mu.shape
        assert self.latent_dim == mu.shape[-1]
        mu = mu.view(-1, self.latent_dim)
        idx = torch.randint(0, self.pool_size, (mu.size(0), 1), dtype=torch.long, device=mu.device)
        w = self.W.to(mu.device)[idx]
        eps = torch.randn_like(mu)
        nu = eps - (eps * mu).sum(dim=1, keepdim=True) * mu
        nu = F.normalize(nu, p=2, dim=-1)
        r = w * mu + torch.sqrt(1 - w ** 2) * nu
        r = r.view(*original_shape)
        return r

class sVAE(nn.Module):
    """sphere variational autoencoder(vMF)"""
    def __init__(self, encoder_conf, decoder_conf):
        super().__init__()
        self.encoder = MyEncoder(**encoder_conf)
        self.decoder = MyDecoder(**decoder_conf)
        self.vmf = vMF(encoder_conf['target_channels'])

    def forward(self, x, return_q=True):
        """x - images [NCHW]
        return_q - if True, return `r` (recons images [NCHW]), and optional `vqres` (quantized info)
        """
        z0, _ = self.encoder(x)
        t0 = z0.permute(0, 2, 1)
        mu = F.normalize(t0, p=2, dim=-1)
        t1 = self.vmf.reparameterize(mu)
        z1 = t1.permute(0, 2, 1)
        r, _ = self.decoder(z1)
        return r, VQRes(quantized=None,
                        indices=None,
                        entro_mean=T0,
                        mean_entro=T0,
                        entro_loss=T0,
                        commit_loss=T0,
                        cdbook_loss=T0)