import os
import argparse
from collections import Counter

import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F
from torch import nn, norm, cdist, einsum
from einops import rearrange, reduce


from .common import VQRes, pack_one, unpack_one, generate_super_points

class HyperSphere(nn.Module):
    def __init__(
        self, input_dim=18, num_super_points=4096, dim=18, hard=True, no_shrink=True
    ):
        super(HyperSphere, self).__init__()
        self.dim = dim
        self.num_super_points = num_super_points
        self.ori_num_super_points = num_super_points
        self.script_name = os.path.splitext(os.path.basename(__file__))[0]
        self.imgnum = 0
        self.super_points = generate_super_points(self.num_super_points, self.dim)
        assert abs(self.super_points[0].norm() - 1.0) < 1e-6
        self.index_counter = Counter()
        self.pure_ball = dim >= input_dim
        if not self.pure_ball:
            self.down = nn.Linear(input_dim, self.dim)
            self.up = nn.Linear(self.dim, input_dim)
        self.iteration = 0
        self.min_retain_rate = 0.5
        self.hard = hard
        self.no_shrink = no_shrink

    def map_random_points_to_sphere(self, random_points):
        # Ensure the points are torch tensors and move them to the GPU
        random_points = torch.tensor(random_points, dtype=torch.float32)

        # Normalize the random points to lie on the unit sphere
        norms = norm(random_points, dim=-1, keepdim=True)
        mapped_points = random_points / norms

        # Compute Euclidean distances
        distances = cdist(mapped_points, self.super_points)

        # Find the nearest super points
        indices = torch.argmin(distances, dim=1)
        quantized = self.super_points[indices]

        return mapped_points, quantized

    def save_figure(self, fig):
        filename = f"{self.script_name}_{self.imgnum}.png"
        fig.savefig(filename)
        print(f"Figure saved as {filename}")

    def reorder_super_points(
        self, retain_rate=0.999
    ):  # >>> 0.999**100 = 0.9047921471137089
        if self.num_super_points / self.ori_num_super_points < self.min_retain_rate:
            return
        num_points_to_retain = int(len(self.super_points) * retain_rate)
        indices_counts = list(self.index_counter.items())
        sorted_indices_counts = sorted(
            indices_counts, key=lambda item: item[1], reverse=True
        )
        sorted_indices = [index for index, count in sorted_indices_counts]
        retained_indices = sorted_indices[:num_points_to_retain]
        reordered_super_points = torch.empty(
            (num_points_to_retain, self.super_points.shape[1]),
            device=self.super_points.device,
        )
        for new_index, old_index in enumerate(retained_indices):
            reordered_super_points[new_index] = self.super_points[old_index]
        self.super_points = reordered_super_points
        new_index_counter = Counter()
        for new_index, old_index in enumerate(retained_indices):
            new_index_counter[new_index] = self.index_counter[old_index]
        self.index_counter = new_index_counter
        self.num_super_points = num_points_to_retain

    def hard_quantize(self, x):
        """
        x format: NCHW or NCW when H==1
        """
        self.super_points = self.super_points.to(x.device)
        if not self.no_shrink and self.iteration % (1000 + 1) == 1000:
            self.reorder_super_points()
            self.draw_index()
        ori_x_shape = len(x.shape)
        if ori_x_shape == 3:  # for 1D z
            x = x.unsqueeze(2)
        x = rearrange(x, "b d h w -> b h w d")
        if not self.pure_ball:
            x = self.down(x)
        x, ps = pack_one(x, "b * d")
        x = rearrange(x, "b n (c d) -> b n c d", c=1)
        norms = torch.norm(x, dim=-1, keepdim=True)
        x = x / norms
        x_expanded = x.unsqueeze(2)
        super_points_expanded = self.super_points.unsqueeze(0).unsqueeze(0)
        distances = torch.norm(x_expanded - super_points_expanded, dim=-1)  # TODO
        indices = torch.argmin(distances, dim=-1)
        quantized = self.super_points[indices]

        # Calculate commit loss (example)
        if self.training:
            if not self.no_shrink:
                self.iteration += 1
                # Update the counter
                flat_indices = indices.flatten().tolist()
                self.index_counter.update(flat_indices)

            logits = einsum("... i d, j d -> ... i j", x, self.super_points) * 100
            probs = F.softmax(logits, -1)
            log_probs = F.log_softmax(logits + 1e-15, -1)
            sample_entropy = -torch.sum(probs * log_probs, -1)
            avg_probs = reduce(probs, "... D -> D", "mean")
            entro_mean = torch.mean(sample_entropy)
            mean_entro = -torch.sum(avg_probs * torch.log(avg_probs + 1e-15))
            entro_loss = entro_mean - mean_entro

            quantized = x + (quantized - x).detach()  # transfer to quantized
            commit_loss = F.mse_loss(x, quantized.detach(), reduction="none")
            commit_loss = commit_loss.mean()
        else:
            commit_loss = torch.tensor(0.0, device=x.device)
            entro_mean, mean_entro, entro_loss, avg_probs = 0, 0, 0, 0
        if not self.pure_ball:
            quantized = self.up(quantized)
        q = rearrange(quantized, "b n c d -> b n (c d)")
        q = unpack_one(q, ps, "b * d")
        q = rearrange(q, "b ... d -> b d ...")
        indices = unpack_one(indices, ps, "b * c")
        indices = indices.flatten()
        if ori_x_shape == 3:
            q = q.squeeze(2)
        return VQRes(quantized=q, indices=indices, entro_mean=entro_mean, mean_entro=mean_entro,
                     entro_loss=entro_loss, commit_loss=commit_loss, cdbook_loss=0)

    def soft_quantize(self, x, temperature=0.01):
        self.super_points = self.super_points.to(x.device)
        if not self.no_shrink and self.iteration % (1000 + 1) == 1000:
            self.reorder_super_points()
            self.draw_index()

        x = rearrange(x, "b d h w -> b h w d")
        if not self.pure_ball:
            x = self.down(x)
        x, ps = pack_one(x, "b * d")
        x = rearrange(x, "b n (c d) -> b n c d", c=1)

        # Ensure x has the correct shape
        x = x.squeeze(
            2
        )  # Remove the singleton dimension if x has shape (64, 32, 1, 12)

        # Calculate cosine similarity
        cos_sim = torch.matmul(x, self.super_points.T)
        # t = self.super_points  # shape: (4096, 12)
        # cos_sim = torch.einsum('bnd,kd->bnk', x, t)
        # Apply temperature to the cosine similarity
        # cos_sim = cos_sim / temperature

        # Ignore the 90% most distant points by setting their similarities to a large negative value
        # TODO - enable this later
        ##threshold = torch.quantile(cos_sim, 0.1, dim=-1, keepdim=True)
        ##cos_sim[cos_sim < threshold] = -1e9

        # Soft quantization using softmax over cosine similarity
        probs = F.softmax(cos_sim / temperature, dim=-1)
        # super_points_expanded = self.super_points.unsqueeze(0).unsqueeze(0)
        # t = probs.unsqueeze(-1) * super_points_expanded
        # quantized = torch.sum(t, dim=2)

        quantized = torch.matmul(probs, self.super_points)

        # Calculate commit loss (example)
        if self.training:
            if not self.no_shrink:
                self.iteration += 1
                # Update the counter
                flat_indices = torch.argmax(probs, dim=-1).flatten().tolist()
                self.index_counter.update(flat_indices)

            logits_for_entropy = (
                torch.einsum("... i d, j d -> ... i j", x, self.super_points)
                / temperature
            )
            probs_for_entropy = F.softmax(logits_for_entropy, -1)
            log_probs_for_entropy = F.log_softmax(logits_for_entropy + 1e-15, -1)
            sample_entropy = -torch.sum(probs_for_entropy * log_probs_for_entropy, -1)
            avg_probs = reduce(probs_for_entropy, "... D -> D", "mean")
            entro_mean = torch.mean(sample_entropy)
            mean_entro = -torch.sum(avg_probs * torch.log(avg_probs + 1e-15))
            entro_loss = entro_mean - mean_entro

            commit_loss = F.mse_loss(x, quantized, reduction="none")
            commit_loss = commit_loss.mean()
        else:
            commit_loss = torch.tensor(0.0, device=x.device)
            entro_mean, mean_entro, entro_loss, avg_probs = 0, 0, 0, 0
        if not self.pure_ball:
            quantized = self.up(quantized)
        quantized = quantized.unsqueeze(2)
        #q = rearrange(quantized, "b n c d -> b n (c d)")
        #q = unpack_one(q, ps, "b * d")
        #q = rearrange(q, "b ... d -> b d ...")
        indices = torch.argmax(probs, dim=-1)  # Shape (64, 32)
        indices = rearrange(
            indices, "b n -> b n 1"
        )  # Add a singleton dimension to match the expected shape
        indices = unpack_one(indices, ps, "b * c")
        indices = indices.flatten()
        return VQRes(quantized=quantized, indices=indices, entro_mean=entro_mean, mean_entro=mean_entro, entro_loss=entro_loss,
              commit_loss=commit_loss, cdbook_loss=0)

    def forward(self, x) -> VQRes:
        if self.hard:
            return self.hard_quantize(x)
        else:
            return self.soft_quantize(x)

    def get_codebook_entry(self, indices):
        if len(indices.shape) == 1:
            z_quantized = self.super_points[indices]
        elif len(indices.shape) == 2:
            z_quantized = torch.einsum("bd,dn->bn", indices, self.super_points)
        else:
            raise NotImplementedError
        return z_quantized

    def draw_index(self, sort_it=False, bin_size=10):
        if sort_it:
            sorted_items = sorted(
                self.index_counter.items(), key=lambda item: item[1], reverse=True
            )
            indices, counts = zip(*sorted_items)
        else:
            indices, counts = zip(*self.index_counter.items())

            # Flatten the indices based on counts for histogram
        flat_indices = []
        for index, count in zip(indices, counts):
            flat_indices.extend([index] * count)

        # Create a histogram from the counter
        plt.figure(figsize=(10, 6))
        plt.hist(
            flat_indices,
            bins=range(min(flat_indices), max(flat_indices) + bin_size, bin_size),
            edgecolor="black",
        )
        plt.xlabel("Index")
        plt.ylabel("Frequency")
        plt.title("Frequency of Each Index")

        # Calculate the ratio
        non_zero_count = sum(1 for count in counts if count > 0)
        total_count = self.num_super_points
        ratio = non_zero_count / total_count

        # Add the ratio to the plot
        plt.text(
            0.95,
            0.95,
            f"Non-zero Index Ratio: {ratio:.2f}",
            ha="right",
            va="top",
            transform=plt.gca().transAxes,
            fontsize=12,
            bbox=dict(facecolor="white", alpha=0.6),
        )

        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    from hiq import deterministic

    parser = argparse.ArgumentParser(
        description="Map random points to nearest super points on a sphere."
    )
    parser.add_argument(
        "--num_super_points",
        type=int,
        default=4096,
        help="Number of super points (default: 4096)",
    )
    parser.add_argument(
        "--num_random_points",
        type=int,
        default=10240,
        help="Number of random points (default: 10240)",
    )
    parser.add_argument(
        "--dim", type=int, default=12, help="Number of dimensions (default: 3)"
    )

    args = parser.parse_args()

    # 2D case
    batch_size, channel, height, width = 64, 18, 16, 16

    hypersphere = HyperSphere(
        input_dim=channel,
        num_super_points=args.num_super_points,
        dim=args.dim,
    )
    x = torch.randn(batch_size, channel, height, width).cuda()
    hypersphere = hypersphere.to(x.device)
    y0 = hypersphere(x)
    print(y0)
    del hypersphere

    # 1D case
    batch_size, channel, height, width = 64, 12, 1, 32

    hypersphere = HyperSphere(
        input_dim=channel,
        num_super_points=args.num_super_points,
        dim=args.dim,
        hard=False,
    )
    x = torch.randn(batch_size, channel, height, width).cuda()
    hypersphere = hypersphere.to(x.device)
    y = hypersphere(x)
    print(y)

    # import matplotlib.pyplot as plt;plt.hist(x_.flatten().detach().cpu().numpy(), bins=500);plt.show()
