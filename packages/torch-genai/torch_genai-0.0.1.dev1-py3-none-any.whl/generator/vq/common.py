from collections import namedtuple

import numpy as np
import torch

from einops import rearrange, reduce, pack, unpack

T0 = torch.tensor(0.)

VQRes = namedtuple('VQRes', [
    'quantized',
    'indices',
    'entro_mean',
    'mean_entro',
    'entro_loss',
    'commit_loss',
    'cdbook_loss'
])


def pack_one(t, pattern):
    return pack([t], pattern)


def unpack_one(t, ps, pattern):
    return unpack(t, ps, pattern)[0]


def generate_super_points(len_, dim_, radius=1.0):
    points = np.random.normal(size=(len_, dim_))
    points /= np.linalg.norm(points, axis=1, keepdims=True)
    if radius != 1.0:
        points *= radius
    return torch.tensor(points, dtype=torch.float32)
