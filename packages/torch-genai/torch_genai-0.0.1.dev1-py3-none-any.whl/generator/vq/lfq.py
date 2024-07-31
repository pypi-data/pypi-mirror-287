"""
Lookup Free Quantization
Proposed in https://arxiv.org/abs/2310.05737

In the simplest setup, each dimension is quantized into {-1, 1}.
An entropy penalty is used to encourage utilization.

Refer to
https://github.com/lucidrains/vector-quantize-pytorch/blob/master/vector_quantize_pytorch/lookup_free_quantization.py
https://github.com/theAdamColton/ijepa-enhanced/blob/7edef5f7288ae8f537f0db8a10044a2a487f70c9/ijepa_enhanced/lfq.py
"""

from math import log2
from collections import namedtuple
import torch
from torch import einsum
import torch.nn.functional as F
from torch.nn import Module

from einops import rearrange, reduce, pack, unpack

# constants
LossBreakdown = namedtuple(
    "LossBreakdown",
    ["per_sample_entropy", "codebook_entropy", "commitment", "avg_probs"],
)


# helper functions
def not_none(v):
    return v is not None


def default(*args):
    for arg in args:
        if not_none(arg):
            return arg() if callable(arg) else arg
    return None


def pack_one(t, pattern):
    return pack([t], pattern)


def unpack_one(t, ps, pattern):
    return unpack(t, ps, pattern)[0]


def entropy(prob):
    return (-prob * torch.log(prob + 1e-5)).sum(dim=-1)


def mult_along_first_dims(x, y):
    """
    returns x * y elementwise along the leading dimensions of y
    """
    ndim_to_expand = x.ndim - y.ndim
    for _ in range(ndim_to_expand):
        y = y.unsqueeze(-1)
    return x * y


def masked_mean(x, m):
    """
    takes the mean of the elements of x that are not masked
    the mean is taken along the shared leading dims of m
    equivalent to: x[m].mean(tuple(range(m.ndim)))

    The benefit of using masked_mean rather than using
    tensor indexing is that masked_mean is much faster
    for torch-compile on batches.

    The drawback is larger floating point errors
    """
    x = mult_along_first_dims(x, m)
    x = x / m.sum()
    return x.sum(tuple(range(m.ndim)))


def entropy_loss(
    logits,
    mask=None,
    temperature=0.01,
    sample_minimization_weight=1.0,
    batch_maximization_weight=1.0,
    eps=1e-9,
):
    """
    Entropy loss of un-normalized logits

    logits: Affinities are over the last dimension

    https://github.com/google-research/magvit/blob/05e8cfd6559c47955793d70602d62a2f9b0bdef5/videogvt/train_lib/losses.py#L279
    LANGUAGE MODEL BEATS DIFFUSION — TOKENIZER IS KEY TO VISUAL GENERATION (2024)
    """
    probs = F.softmax(logits / temperature, -1)
    log_probs = F.log_softmax(logits / temperature + eps, -1)
    sample_entropy = -torch.sum(probs * log_probs, -1)

    if mask is None:
        avg_probs = reduce(probs, "... D -> D", "mean")
        entro_mean = torch.mean(sample_entropy)
    else:
        avg_probs = masked_mean(probs, mask)
        entro_mean = masked_mean(sample_entropy, mask).mean()

    mean_entro = -torch.sum(avg_probs * torch.log(avg_probs + eps))
    loss = (sample_minimization_weight * entro_mean) - (
        batch_maximization_weight * mean_entro
    )
    return entro_mean, mean_entro, loss


def approx_entropy_loss(
    logits,
    mask=None,
    temperature=0.01,
    sample_minimization_weight=1.0,
    batch_maximization_weight=1.0,
    eps=1e-5,
):
    """TO BE DONE"""
    # Split logits into subgroups, but logits itself is still big, so need a better way
    sub_group_size = min(2**18, logits.shape[-1])
    num_groups = logits.shape[-1] // sub_group_size
    entropies = []
    avg_probs_list = []

    for i in range(num_groups):
        sub_group_logits = logits[..., i * sub_group_size : (i + 1) * sub_group_size]
        probs = F.softmax(sub_group_logits / temperature, -1)
        log_probs = F.log_softmax(sub_group_logits / temperature + eps, -1)
        sub_group_entropy = -torch.sum(probs * log_probs, -1)
        entropies.append(sub_group_entropy)
        if mask is None:
            avg_probs = reduce(probs, "... D -> D", "mean")
        else:
            avg_probs = masked_mean(probs, mask)
        avg_probs_list.append(avg_probs)
    # Combine results
    entro_mean = torch.mean(torch.stack(entropies))
    avg_probs_combined = torch.mean(torch.stack(avg_probs_list), dim=0)
    mean_entro = -torch.sum(avg_probs_combined * torch.log(avg_probs_combined + eps))
    loss = (sample_minimization_weight * entro_mean) - (
        batch_maximization_weight * mean_entro
    )
    return entro_mean, mean_entro, loss


class LFQ(Module):
    def __init__(
        self,
        *,
        dim=None,
        codebook_size=None,
        num_codebooks=1,
        sample_minimization_weight=1.0,
        batch_maximization_weight=1.0,
        token_factorization=False,
        use_subgroup_entropy=0,  # -1: use entropy_loss, 0: use dim to decide, 1: use appox
    ):
        super().__init__()
        assert not_none(dim) or not_none(
            codebook_size
        ), "either dim or codebook_size must be specified for LFQ"
        assert (
            codebook_size is None or (codebook_size & (codebook_size - 1)) == 0
        ), f"your codebook size must be a power of 2 for lookup free quantization"

        self.codebook_size = default(codebook_size, lambda: 2**dim)
        self.codebook_dim = int(log2(codebook_size))

        codebook_dims = self.codebook_dim * num_codebooks
        dim = default(dim, codebook_dims)

        self.has_projections = dim != codebook_dims
        if use_subgroup_entropy == 1:
            self.entropy_loss_func = approx_entropy_loss
        elif use_subgroup_entropy == -1:
            self.entropy_loss_func = entropy_loss
        elif use_subgroup_entropy == 0:
            self.entropy_loss_func = (
                approx_entropy_loss
                if (dim > 18 or codebook_size > 2**18)
                else entropy_loss
            )

        self.dim = dim
        self.codebook_dims = codebook_dims
        self.num_codebooks = num_codebooks

        # for entropy loss
        self.sample_minimization_weight = sample_minimization_weight
        self.batch_maximization_weight = batch_maximization_weight

        # for no auxiliary loss, during inference
        self.token_factorization = token_factorization  # only utilized in second stage
        if not self.token_factorization:  # for first stage model
            t = 2 ** torch.arange(self.codebook_dim - 1, -1, -1)
            self.register_buffer(
                "mask",
                t,
                persistent=False,
            )
        else:
            k = self.codebook_dim // 2
            self.register_buffer(
                "mask", 2 ** torch.arange(k - 1, -1, -1), persistent=False
            )

        self.register_buffer("zero", torch.tensor(0.0), persistent=False)

        # codes - big memory usage
        all_codes = torch.arange(codebook_size)
        bits = self.indices_to_bits(all_codes)
        codebook = bits * 2.0 - 1.0
        self.register_buffer("codebook", codebook, persistent=False)

    @property
    def dtype(self):
        return self.codebook.dtype

    def indices_to_bits(self, x):
        """
        x: long tensor of indices for constructing codebook, but actually not utilized in all the experiments.
        returns big endian bits
        """
        mask = 2 ** torch.arange(self.codebook_dim, device=x.device, dtype=torch.long)
        # x is now big endian bits, the last dimension being the bits
        z = (x.unsqueeze(-1) & mask) != 0
        return z

    def get_codebook_entry(self, x, bhwc):
        if self.token_factorization:
            k = self.codebook_dim // 2
            mask = 2 ** torch.arange(k - 1, -1, -1, device=x.device, dtype=torch.long)
        else:
            mask = 2 ** torch.arange(
                self.codebook_dim - 1, -1, -1, device=x.device, dtype=torch.long
            )

        x = (x.unsqueeze(-1) & mask) != 0
        x = x * 2.0 - 1.0  # back to the float
        # scale back to the desired shape
        b, h, w, c = bhwc
        x = rearrange(x, "b (h w) c -> b h w c", h=h, w=w, c=c)
        x = rearrange(x, "b h w c -> b c h w")
        return x

    def bits_to_indices(self, bits):
        """
        bits: bool tensor of big endian bits, where the last dimension is the bit dimension

        returns indices, which are long integers from 0 to self.codebook_size
        """
        assert bits.shape[-1] == self.codebook_dim
        indices = 2 ** torch.arange(
            0,
            self.codebook_dim,
            1,
            dtype=torch.long,
            device=bits.device,
        )
        return (bits * indices).sum(-1)

    def decode(self, x):
        """
        x: ... NH
            where NH is number of codebook heads
            A longtensor of codebook indices, containing values from
            0 to self.codebook_size
        """
        x = self.indices_to_bits(x)
        # to some sort of float
        x = x.to(self.dtype)
        # -1 or 1
        x = x * 2 - 1
        x = rearrange(x, "... NC Z-> ... (NC Z)")
        return x

    def forward(
        self,
        x,
        return_loss_breakdown=False,
        mask=None,
        return_loss=True,
    ):
        """
        einstein notation
        b - batch
        n - sequence (or flattened spatial dimensions)
        d - feature dimension, which is also log2(codebook size)
        c - number of codebook dim
        """

        x = rearrange(x, "b d ... -> b ... d")
        x, ps = pack_one(x, "b * d")
        # split out number of codebooks

        x = rearrange(x, "b n (c d) -> b n c d", c=self.num_codebooks)

        codebook_value = torch.Tensor([1.0]).to(device=x.device, dtype=x.dtype)
        quantized = torch.where(
            x > 0, codebook_value, -codebook_value
        )  # higher than 0 filled

        # calculate indices
        if self.token_factorization:
            k = self.codebook_dim // 2
            indices_pre = reduce(
                (quantized[..., :k] > 0).int() * self.mask.int(),
                "b n c d -> b n c",
                "sum",
            )
            indices_post = reduce(
                (quantized[..., k:] > 0).int() * self.mask.int(),
                "b n c d -> b n c",
                "sum",
            )
            # indices_post = 2**k + indices_post #shifter to the 1024
        else:
            indices = reduce(
                (quantized > 0).int() * self.mask.int(), "b n c d -> b n c", "sum"
            )

        # entropy aux loss
        if self.training and return_loss:
            x = x / x.norm(dim=-1, keepdim=True)
            logits = 2 * einsum(
                "... i d, j d -> ... i j", x, self.codebook
            )  # need to optimize here
            # the same as Euclidean distance up to a constant
            per_sample_entropy, codebook_entropy, el = self.entropy_loss_func(
                logits=logits,
                sample_minimization_weight=self.sample_minimization_weight,
                batch_maximization_weight=self.batch_maximization_weight,
            )

            avg_probs = self.zero
        else:
            # calculate the codebook_entropy needed for one batch evaluation
            # ------------------------------------------------------------------
            # logits = 2 * einsum('... i d, j d -> ... i j', x, self.codebook)
            # probs = F.softmax(logits / 0.01, -1)
            # avg_probs = reduce(probs, "b n c d -> b d", "mean")
            # avg_probs = torch.sum(avg_probs, 0) #batch dimension
            # -------------------------------------------------------------------
            # if not training, just return dummy 0
            per_sample_entropy = codebook_entropy = self.zero
            el = self.zero
            avg_probs = self.zero

        # commit loss
        if self.training:
            commit_loss = F.mse_loss(x, quantized.detach(), reduction="none")
            if not_none(mask):
                commit_loss = commit_loss[mask]
            commit_loss = commit_loss.mean()
        else:
            commit_loss = self.zero
        # use straight-through gradients (optionally with custom activation fn) if training
        quantized = x + (quantized - x).detach()  # transfer to quantized

        # merge back codebook dim
        quantized = rearrange(quantized, "b n c d -> b n (c d)")

        # reconstitute image or video dimensions
        quantized = unpack_one(quantized, ps, "b * d")
        quantized = rearrange(quantized, "b ... d -> b d ...")

        if self.token_factorization:
            indices_pre = unpack_one(indices_pre, ps, "b * c")
            indices_post = unpack_one(indices_post, ps, "b * c")
            indices_pre = indices_pre.flatten()
            indices_post = indices_post.flatten()
            indices = (indices_pre, indices_post)
        else:
            indices = unpack_one(indices, ps, "b * c")
            indices = indices.flatten()

        ret = (quantized, el, indices)
        if not return_loss_breakdown:
            return ret

        return ret, LossBreakdown(
            per_sample_entropy, codebook_entropy, commit_loss, avg_probs
        )


def verify_lfq(d=18):
    import matplotlib.pyplot as plt
    from hiq import deterministic, print_model

    batch_size, dim, height, width = 1, d, 16, 16
    codebook_size = 2**dim

    # Create LFQ model in training mode
    lfq = LFQ(dim=dim, codebook_size=codebook_size).train()
    print_model(lfq, show_buffer=True)

    x = torch.randn(batch_size, dim, height, width)
    # x = 2 * torch.rand(batch_size, dim, height, width) - 1

    # Forward pass
    (quantized, emb_loss, indices), loss_breakdown = lfq(
        x, return_loss_breakdown=True, return_loss=True
    )

    # Plotting
    plt.figure(figsize=(10, 8))

    # Original input
    plt.subplot(4, 1, 1)
    t = x[0].view(dim, -1)
    plt.imshow(t.detach().cpu().numpy(), aspect="auto", cmap="viridis")
    plt.colorbar()
    plt.title("Original Input", fontsize=8)

    # Quantized output
    plt.subplot(4, 1, 2)
    plt.imshow(
        quantized[0].view(dim, -1).detach().cpu().numpy(), aspect="auto", cmap="viridis"
    )
    plt.colorbar()
    plt.title("Quantized Output", fontsize=8)

    # Indices
    plt.subplot(4, 1, 3)
    plt.plot(indices.view(-1).detach().cpu().numpy(), marker="o")
    plt.grid(True)
    plt.title("Quantization Indices", fontsize=8)

    # Indices histogram
    plt.subplot(4, 1, 4)
    plt.hist(indices.view(-1).detach().cpu().numpy(), bins=d * 10)
    plt.title("Indices Histogram", fontsize=8)
    plt.xlabel("Index", fontsize=8)
    plt.ylabel("Frequency", fontsize=8)

    plt.suptitle(
        f"d:{d}, Entropy Loss: {emb_loss.item():.2f}, "
        f"breakdown: {loss_breakdown.per_sample_entropy:.2f},"
        f" {loss_breakdown.codebook_entropy:.2f}, {loss_breakdown.commitment:.2f}",
        fontsize=10,
    )
    plt.subplots_adjust(bottom=0.2, top=0.9)
    plt.tight_layout()

    # Save before show to ensure layout is consistent
    plt.savefig(f"docs/lfq_{d}.png")
    # plt.show()


if __name__ == "__main__":
    for i in range(16, 22):
        verify_lfq(i)

    verify_lfq(20)
