import os
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.utils as vutils
from torch.utils.data import DataLoader
from hiq.cv_torch import get_cv_dataset, DS_PATH_OXFLOWER_7K, ensure_split


def get_dataset(args, num_workers=4):
    transform = transforms.Compose(
        [
            transforms.Resize((args.image_size, args.image_size)),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )
    loader_params = dict(shuffle=False, drop_last=True, pin_memory=True)
    dl = get_cv_dataset(
        path=args.dataset,
        image_size=args.image_size,
        batch_size=args.batch_size,
        num_workers=num_workers,
        transform=transform,
        return_type="pair",
        return_loader=False,
        convert_rgb=True,
        max_num=args.max_num,
        **loader_params,
    )
    dl = ensure_split(dl)
    train_dataset, test_dataset = dl["train"], dl["test"]
    train_loader = DataLoader(
        train_dataset, batch_size=args.batch_size, shuffle=True, num_workers=num_workers
    )
    test_loader = DataLoader(
        test_dataset, batch_size=args.batch_size, shuffle=False, num_workers=num_workers
    )
    return train_loader, test_loader


def get_or_create_directory(path):
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
    else:
        # If the path doesn't exist, create it as a directory
        os.makedirs(path, exist_ok=True)
        return path


if __name__ == "__main__":
    pass

"""
DS_PATH_OXFLOWER_7K = "nelorth/oxford-flowers"  # 8k
DS_PATH_FFHQ256_70K = "merkol/ffhq-256"
DS_PATH_FFHQ512_30K = "cld07/captioned_ffhq_512"
"""
