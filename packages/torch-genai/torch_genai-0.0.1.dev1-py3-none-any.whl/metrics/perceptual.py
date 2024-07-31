import lpips


class PerceptualLoss:
    def __init__(self, net="vgg"):  # other values: alex, squeeze
        super().__init__()
        self.perceptual_loss = lpips.LPIPS(net=net, verbose=True).eval()

    def get(self, origin, recons, range_01=True):
        self.perceptual_loss = self.perceptual_loss.to(origin.device)
        origin = origin.contiguous()
        recons = recons.contiguous()
        if range_01:  # the range is [0, 1]
            r = self.perceptual_loss(origin * 2 - 1, recons * 2 - 1).mean()
        else:  # assume the range is [-1, 1]
            r = self.perceptual_loss(origin, recons).mean()
        return r


if __name__ == "__main__":
    import torch
    import torch.nn as nn
    import matplotlib.pyplot as plt
    from skimage import data
    from skimage.transform import resize
    import torchvision.transforms as transforms
    import numpy as np

    def add_noise(img, noise_factor=0.2):
        noise = torch.randn_like(img) * noise_factor
        noisy_img = img + noise
        noisy_img = torch.clamp(noisy_img, 0, 1)
        return noisy_img

    def load_astronaut_image(transform=None):
        img = data.astronaut()
        img = resize(img, (256, 256), anti_aliasing=True)
        if transform:
            img = transform(img)
        return img

    def demo(noise_factors=[0, 0.05, 0.1, 0.2, 1, 2, 20]):
        # Define transformations
        transform = transforms.Compose(
            [
                transforms.ToTensor(),
            ]
        )

        # Load and transform the astronaut image
        img = load_astronaut_image(transform)
        img = img.unsqueeze(0)  # Add batch dimension

        # Convert image to float tensor
        img = img.float()

        # Initialize the PerceptualLoss model
        ploss = PerceptualLoss()

        num_factors = len(noise_factors)
        fig, axes = plt.subplots(1, num_factors + 1, figsize=(15, 2.8))

        # Display the original image
        img_np = img.squeeze().permute(1, 2, 0).numpy()
        axes[0].imshow(img_np)
        axes[0].set_title("Original Image")
        axes[0].axis("off")

        # Process each noise factor
        for i, noise_factor in enumerate(noise_factors):
            # Add noise to the image
            noisy_img = add_noise(img, noise_factor)

            # Calculate perceptual loss
            loss = ploss.get(img, noisy_img)
            print(f"Perceptual Loss with noise factor {noise_factor}: {loss.item()}")

            # Display the noisy image
            noisy_img_np = noisy_img.squeeze().permute(1, 2, 0).numpy()
            axes[i + 1].imshow(noisy_img_np)
            axes[i + 1].set_title(
                f"Noise {noise_factor}\nLoss {loss.item():.4f}", fontsize=8
            )
            axes[i + 1].axis("off")

        plt.tight_layout()
        plt.savefig("perceptual_loss.png")
        plt.show()

    # Run the demo with different noise factors
    demo([0, 0.05, 0.1, 0.2, 2, 20])
