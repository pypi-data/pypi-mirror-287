from tqdm import tqdm
import torch
import torch.nn.functional as F
import lightning as L
from contextlib import contextmanager
from collections import OrderedDict
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import lpips
from skimage.metrics import peak_signal_noise_ratio as psnr_loss
from skimage.metrics import structural_similarity as ssim_loss
from .inception import InceptionV3

inception_model = None

def get_inception_model():
    global inception_model
    if inception_model is None:
        block_idx = InceptionV3.BLOCK_INDEX_BY_DIM[2048]
        inception_model = InceptionV3([block_idx])
        inception_model.eval()
    return inception_model


def calculate_recon_metrics(model, val_dataloader, device):
    inception_model = get_inception_model().to(device)
    num_images = 0
    pred_xs = []
    pred_recs = []
    # LPIPS score related
    loss_fn_alex = lpips.LPIPS(net="alex").to(device)
    loss_fn_vgg = lpips.LPIPS(net="vgg").to(device)
    lpips_alex = 0.0
    lpips_vgg = 0.0
    # SSIM score related
    ssim_value = 0.0
    # PSNR score related
    psnr_value = 0.0
    with torch.inference_mode():
        for bid, (images, _) in enumerate(tqdm(val_dataloader)):
            images = images.to(device)
            num_images += images.shape[0]
            recons = model(images)
            # recons = recons.clamp(-1, 1)
            images = (images.float() + 1) / 2
            recons = (recons.float() + 1) / 2
            # calculate fid
            pred_x = inception_model(images)[0]
            pred_x = pred_x.squeeze(3).squeeze(2).cpu().numpy()
            pred_rec = inception_model(recons)[0]
            pred_rec = pred_rec.squeeze(3).squeeze(2).cpu().numpy()
            pred_xs.append(pred_x)
            pred_recs.append(pred_rec)
            # calculate lpips
            lpips_alex += loss_fn_alex(images, recons).sum()
            lpips_vgg += loss_fn_vgg(images, recons).sum()
            rgb_restored = (
                (recons * 255.0)
                .permute(0, 2, 3, 1)
                .to("cpu", dtype=torch.uint8)
                .numpy()
            )
            rgb_gt = (
                (images * 255.0)
                .permute(0, 2, 3, 1)
                .to("cpu", dtype=torch.uint8)
                .numpy()
            )
            rgb_restored = rgb_restored.astype(np.float32) / 255.0
            rgb_gt = rgb_gt.astype(np.float32) / 255.0
            ssim_temp = 0
            psnr_temp = 0
            B, _, _, _ = rgb_restored.shape
            for i in range(B):
                rgb_restored_s, rgb_gt_s = rgb_restored[i], rgb_gt[i]
                ssim_temp += ssim_loss(
                    rgb_restored_s, rgb_gt_s, data_range=1.0, channel_axis=-1
                )
                psnr_temp += psnr_loss(rgb_gt, rgb_restored)
            ssim_value += ssim_temp / B
            psnr_value += psnr_temp / B
    pred_xs = np.concatenate(pred_xs, axis=0)
    pred_recs = np.concatenate(pred_recs, axis=0)
    mu_x = np.mean(pred_xs, axis=0)
    sigma_x = np.cov(pred_xs, rowvar=False)
    mu_rec = np.mean(pred_recs, axis=0)
    sigma_rec = np.cov(pred_recs, rowvar=False)
    fid_value = calculate_frechet_distance(mu_x, sigma_x, mu_rec, sigma_rec)
    lpips_alex_value = lpips_alex / num_images
    lpips_vgg_value = lpips_vgg / num_images
    ssim_value = ssim_value / len(val_dataloader)
    psnr_value = psnr_value / len(val_dataloader)

    print(
        f"rFID:{fid_value}, SSIM:{ssim_value}, PSNR:{psnr_value}, lpips_a:{lpips_alex_value}, lpips_v:{lpips_vgg_value}")
    return fid_value, ssim_value, psnr_value, lpips_alex_value, lpips_vgg_value


class FIDCalc:
    def __init__(self):
        self.pred_xs = []
        self.pred_recs = []
        self.inception_model = get_inception_model()
    def run(self, images, recons):
        self.inception_model = self.inception_model.to(images.device)
        images = (images.float() + 1) / 2
        recons = (recons.float() + 1) / 2
        # ensure images and recons are [0, 1]
        pred_x = inception_model(images)[0]
        pred_x = pred_x.squeeze(3).squeeze(2).cpu().numpy()
        pred_rec = inception_model(recons)[0]
        pred_rec = pred_rec.squeeze(3).squeeze(2).cpu().numpy()
        self.pred_xs.append(pred_x)
        self.pred_recs.append(pred_rec)
    def gather(self):
        pred_xs = np.concatenate(self.pred_xs, axis=0)
        pred_recs = np.concatenate(self.pred_recs, axis=0)
        mu_x = np.mean(pred_xs, axis=0)
        sigma_x = np.cov(pred_xs, rowvar=False)
        mu_rec = np.mean(pred_recs, axis=0)
        sigma_rec = np.cov(pred_recs, rowvar=False)
        fid_value = calculate_frechet_distance(mu_x, sigma_x, mu_rec, sigma_rec)
        return fid_value

    def reset(self):
        self.pred_xs = []
        self.pred_recs = []


def calculate_fid(images, recons):
    pred_xs = []
    pred_recs = []
    inception_model = get_inception_model()
    images = (images + 1) / 2
    recons = (recons + 1) / 2
    # calculate fid
    pred_x = inception_model(images)[0]
    pred_x = pred_x.squeeze(3).squeeze(2).cpu().numpy()
    pred_rec = inception_model(recons)[0]
    pred_rec = pred_rec.squeeze(3).squeeze(2).cpu().numpy()
    pred_xs.append(pred_x)
    pred_recs.append(pred_rec)
    mu_x = np.mean(pred_xs, axis=0)
    sigma_x = np.cov(pred_xs, rowvar=False)
    mu_rec = np.mean(pred_recs, axis=0)
    sigma_rec = np.cov(pred_recs, rowvar=False)
    fid_value = calculate_frechet_distance(mu_x, sigma_x, mu_rec, sigma_rec)
    return fid_value


def calculate_frechet_distance(mu1, sigma1, mu2, sigma2, eps=1e-6):
    """Numpy implementation of the Frechet Distance.
    The Frechet distance between two multivariate Gaussians X_1 ~ N(mu_1, C_1)
    and X_2 ~ N(mu_2, C_2) is
            d^2 = ||mu_1 - mu_2||^2 + Tr(C_1 + C_2 - 2*sqrt(C_1*C_2)).

    Stable version by Dougal J. Sutherland.

    Params:
    -- mu1   : Numpy array containing the activations of a layer of the
               inception net (like returned by the function 'get_predictions')
               for generated samples.
    -- mu2   : The sample mean over activations, precalculated on an
               representative data set.
    -- sigma1: The covariance matrix over activations for generated samples.
    -- sigma2: The covariance matrix over activations, precalculated on an
               representative data set.

    Returns:
    --   : The Frechet Distance.
    """

    mu1 = np.atleast_1d(mu1)
    mu2 = np.atleast_1d(mu2)

    sigma1 = np.atleast_2d(sigma1)
    sigma2 = np.atleast_2d(sigma2)

    assert (
            mu1.shape == mu2.shape
    ), "Training and test mean vectors have different lengths"
    assert (
            sigma1.shape == sigma2.shape
    ), "Training and test covariances have different dimensions"

    diff = mu1 - mu2

    # Product might be almost singular
    covmean, _ = linalg.sqrtm(sigma1.dot(sigma2), disp=False)
    if not np.isfinite(covmean).all():
        msg = (
                  "fid calculation produces singular product; "
                  "adding %s to diagonal of cov estimates"
              ) % eps
        print(msg)
        offset = np.eye(sigma1.shape[0]) * eps
        covmean = linalg.sqrtm((sigma1 + offset).dot(sigma2 + offset))

    # Numerical error might give slight imaginary component
    if np.iscomplexobj(covmean):
        if not np.allclose(np.diagonal(covmean).imag, 0, atol=1e-3):
            m = np.max(np.abs(covmean.imag))
            raise ValueError("Imaginary component {}".format(m))
        covmean = covmean.real

    tr_covmean = np.trace(covmean)

    return diff.dot(diff) + np.trace(sigma1) + np.trace(sigma2) - 2 * tr_covmean


