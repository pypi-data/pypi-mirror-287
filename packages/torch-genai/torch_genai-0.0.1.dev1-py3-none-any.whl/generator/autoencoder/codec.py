from collections import OrderedDict

import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from einops.layers.torch import Rearrange


class RotaryPositionalEmbedding(nn.Module):
    def __init__(self, dim):
        super().__init__()
        inv_freq = 1.0 / (10000 ** (torch.arange(0, dim, 2).float() / dim))
        self.register_buffer("inv_freq", inv_freq)

    def forward(self, x):
        t = torch.arange(x.size(1), device=x.device).type_as(self.inv_freq)
        freqs = torch.einsum("i,j->ij", t, self.inv_freq)
        emb = torch.cat((freqs.sin(), freqs.cos()), dim=-1)
        return emb[None, :, :]


class MyAttention(nn.Module):
    def __init__(self, d_model, qk_dim, v_dim, n_head, use_pos_emb=False):
        super().__init__()
        self.n_head = n_head
        self.qk_dim = qk_dim
        self.v_dim = v_dim
        self.query_proj = nn.Linear(d_model, qk_dim * n_head)
        self.key_proj = nn.Linear(d_model, qk_dim * n_head)
        self.value_proj = nn.Linear(d_model, v_dim * n_head)
        self.output_proj = nn.Linear(v_dim * n_head, d_model)
        self.use_pos_emb = use_pos_emb
        if self.use_pos_emb:
            self.positional_embedding = RotaryPositionalEmbedding(qk_dim)

    def forward(self, x):
        batch_size, seq_length, d_model = x.size()
        # Project inputs to query, key, and value
        q = (
            self.query_proj(x)
            .view(batch_size, seq_length, self.n_head, self.qk_dim)
            .transpose(1, 2)
        )
        k = (
            self.key_proj(x)
            .view(batch_size, seq_length, self.n_head, self.qk_dim)
            .transpose(1, 2)
        )
        v = (
            self.value_proj(x)
            .view(batch_size, seq_length, self.n_head, self.v_dim)
            .transpose(1, 2)
        )
        # Apply positional embedding if required
        if self.use_pos_emb:
            pos_emb = self.positional_embedding(x).unsqueeze(1)
            q = q + pos_emb
            k = k + pos_emb
        # Compute scaled dot-product attention
        attn_scores = torch.matmul(q, k.transpose(-2, -1)) / (self.qk_dim**0.5)
        attn_weights = torch.softmax(attn_scores, dim=-1)
        attn_output = torch.matmul(attn_weights, v)
        # Concatenate heads and project to output
        attn_output = (
            attn_output.transpose(1, 2)
            .contiguous()
            .view(batch_size, seq_length, self.n_head * self.v_dim)
        )
        output = self.output_proj(attn_output)
        return output, attn_weights

def _o(s, reload=False):
    if not isinstance(s, str):
        return s
    import importlib
    module, cls = s.rsplit(".", 1)
    if reload:
        module_imp = importlib.import_module(module)
        importlib.reload(module_imp)
    return getattr(importlib.import_module(module, package=None), cls)

class ResidualAttentionBlock(nn.Module):
    def __init__(
        self,
        d_model,
        qk_dim,
        v_dim,
        n_head,
        mlp_ratio,
        norm_layer,
        act_layer,
        use_pos_emb=False,
    ):
        super().__init__()
        self.norm_1 = _o(norm_layer)(d_model)
        self.attn = MyAttention(d_model, qk_dim, v_dim, n_head, use_pos_emb)
        mlp_width = int(d_model * mlp_ratio)
        self.mlp = nn.Sequential(
            OrderedDict(
                [
                    ("c_fc", nn.Linear(d_model, mlp_width)),
                    ("act", _o(act_layer)()),
                    ("c_proj", nn.Linear(mlp_width, d_model)),
                ]
            )
        )
        self.norm_2 = _o(norm_layer)(d_model)

    def forward(self, x):
        x_norm = self.norm_1(x)
        attn_output, attn_weights = self.attn(x_norm)
        x = x + attn_output
        x = x + self.mlp(self.norm_2(x))
        return x, attn_weights


class MyEncoder(nn.Module):
    def __init__(
        self,
        d_model,
        qk_dim,
        v_dim,
        n_head,
        original_seq_length,
        compressed_seq_length,
        num_layers,
        target_channels=12,
        mlp_ratio=4.0,
        patch_size=16,
        act_layer=nn.GELU,
        norm_layer=nn.LayerNorm,
        tiny_latent=0,
        use_linear_instead_of_conv=False,
    ):
        super().__init__()
        self.tl = tiny_latent
        self.use_linear_instead_of_conv = use_linear_instead_of_conv
        channels = 3
        self.to_patch_embedding = nn.Sequential(
            nn.Conv2d(channels, d_model, kernel_size=patch_size, stride=patch_size),
            Rearrange("b c h w -> b (h w) c"),
        )

        self.layers = nn.ModuleList()

        seq_lengths = (
            torch.linspace(original_seq_length, compressed_seq_length, num_layers + 1)
            .long()
            .tolist()
        )
        channels = (
            torch.linspace(d_model, target_channels, num_layers + 1).long().tolist()
        )
        for i in range(num_layers):
            use_pos_emb = i == 0  # Only use positional embedding in the first layer
            self.layers.append(
                ResidualAttentionBlock(
                    d_model,
                    qk_dim,
                    v_dim,
                    n_head,
                    mlp_ratio,
                    norm_layer,
                    act_layer,
                    use_pos_emb,
                )
            )
            self.layers.append(nn.Linear(seq_lengths[i], seq_lengths[i + 1]))
            if self.tl:
                if self.use_linear_instead_of_conv:
                    self.layers.append(
                        nn.Linear(channels[i], channels[i + 1], bias=True)
                    )
                else:
                    self.layers.append(
                        nn.Conv2d(channels[i], channels[i + 1], kernel_size=1, bias=True)
                    )
                d_model = channels[i + 1]

        self.norm_final = _o(norm_layer)(d_model)

    def forward(self, x):
        """output format: NCW (H is 1)"""
        x = self.to_patch_embedding(x)
        attn_weights_list = []
        for layer in self.layers:
            if isinstance(layer, ResidualAttentionBlock):
                x, attn_weights = layer(x)
                attn_weights_list.append(attn_weights)
            elif isinstance(layer, nn.Linear):
                # Only transpose if we are compressing the middle dimension (d_model)
                if x.size(-1) == layer.in_features:  # Check if we need to compress the last dimension
                    x = layer(x)
                else:  # Otherwise, we transpose to compress the middle dimension
                    x = x.transpose(1, 2)
                    x = layer(x).transpose(1, 2)
            elif isinstance(layer, nn.Conv2d):
                x = x.permute(0, 2, 1).unsqueeze(-1)  # Reshape for Conv2D
                x = layer(x)
                x = x.squeeze(-1).permute(0, 2, 1)  # Reshape back

        x = self.norm_final(x)
        #if self.use_linear_instead_of_conv:
        x = x.permute(0, 2, 1)
        assert 3 == len(x.shape)
        return x, attn_weights_list


class MyDecoder(nn.Module):
    def __init__(
        self,
        d_model,
        qk_dim,
        v_dim,
        n_head,
        compressed_seq_length,
        original_seq_length,
        num_layers,
        target_channels=12,
        mlp_ratio=4.0,
        patch_size=16,
        image_size=256,
        act_layer=nn.GELU,
        norm_layer=nn.LayerNorm,
        tiny_latent=0,
        use_linear_instead_of_conv=False,
    ):
        super().__init__()
        self.tl = tiny_latent
        self.use_linear_instead_of_conv = use_linear_instead_of_conv
        self.layers = nn.ModuleList()

        seq_lengths = (
            torch.linspace(compressed_seq_length, original_seq_length, num_layers + 1)
            .long()
            .tolist()
        )
        channels = (
            torch.linspace(target_channels, d_model, num_layers + 1).long().tolist()
        )

        for i in range(num_layers):
            if self.tl:
                if self.use_linear_instead_of_conv:
                    self.layers.append(
                        nn.Linear(channels[i], channels[i + 1], bias=True)
                    )
                else:
                    self.layers.append(
                        nn.Conv2d(channels[i], channels[i + 1], kernel_size=1, bias=True)
                    )
                d_model = channels[i + 1]
            self.layers.append(nn.Linear(seq_lengths[i], seq_lengths[i + 1]))
            self.layers.append(
                ResidualAttentionBlock(
                    d_model, qk_dim, v_dim, n_head, mlp_ratio, norm_layer, act_layer
                )
            )

        self.norm_final = _o(norm_layer)(d_model)
        self.to_image = nn.Sequential(
            Rearrange(
                "b (h w) c -> b c h w",
                h=image_size // patch_size,
                w=image_size // patch_size,
            ),
            nn.ConvTranspose2d(d_model, 3, kernel_size=patch_size, stride=patch_size),
        )

    def forward(self, x):
        """NCW - H is implicitly equal to 1. like 16x18x32
        input is NC1W, but we need NWC inside this function"""
        x = x.permute(0, 2, 1)  # Change from NC1W to NWC
        attn_weights_list = []
        for layer in self.layers:
            if isinstance(layer, ResidualAttentionBlock):
                x, attn_weights = layer(x)
                attn_weights_list.append(attn_weights)
            elif isinstance(layer, nn.Linear):
                if x.size(-1) == layer.in_features:
                    x = layer(x)
                else:
                    x = x.transpose(1, 2)
                    x = layer(x).transpose(1, 2)
            elif isinstance(layer, nn.Conv2d):
                x = x.permute(0, 2, 1).unsqueeze(-1)  # Reshape for Conv2D
                x = layer(x)
                x = x.squeeze(-1).permute(0, 2, 1)  # Reshape back
        x = self.norm_final(x)
        x_reconstructed = self.to_image(x)  # Inverse patch embedding
        return x_reconstructed, attn_weights_list
