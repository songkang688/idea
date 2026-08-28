"""Minimal density head on frozen embeddings. FakeEncoder default = runnable prototype."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import yaml


@dataclass
class Cfg:
    seed: int
    image_size: int
    embed_dim: int
    n_amorphous: int
    n_coco: int
    epochs: int
    lr: float
    lambda_bce: float
    lambda_dice: float
    lambda_tv: float
    threshold: float
    fake_encoder: bool
    out_dir: str


def load_cfg(path: str) -> Cfg:
    raw = yaml.safe_load(Path(path).read_text())
    return Cfg(**raw)


def dice_loss(pred: torch.Tensor, target: torch.Tensor, eps: float = 1e-6) -> torch.Tensor:
    pred = pred.clamp(0, 1)
    num = 2 * (pred * target).sum(dim=(1, 2, 3))
    den = pred.sum(dim=(1, 2, 3)) + target.sum(dim=(1, 2, 3)) + eps
    return 1 - (num / den).mean()


class DensityHead(nn.Module):
    def __init__(self, dim: int, extra_ch: int = 1):
        super().__init__()
        self.proj = nn.Conv2d(dim + extra_ch, 1, kernel_size=1)

    def forward(self, z: torch.Tensor, exclusion: torch.Tensor) -> torch.Tensor:
        x = torch.cat([z, exclusion], dim=1)
        return torch.sigmoid(self.proj(x))


class FakeEncoder(nn.Module):
    """STAND-IN. Not SAM. Average-pools RGB so a 1x1 head can overfit the toy blobs."""

    def __init__(self, dim: int):
        super().__init__()
        self.dim = dim

    def forward(self, img: torch.Tensor) -> torch.Tensor:
        z = F.avg_pool2d(img, 4)
        if self.dim > 3:
            pad = z.new_zeros(z.size(0), self.dim - 3, z.size(2), z.size(3))
            z = torch.cat([z, pad], dim=1)
        return z[:, : self.dim]


def blob_mask(n: int, size: int, mode: str, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    yy, xx = np.mgrid[0:size, 0:size]
    imgs, masks = [], []
    for _ in range(n):
        img = rng.normal(0.4, 0.1, (3, size, size)).astype(np.float32)
        if mode == "object":
            cy, cx, r = rng.integers(16, 48), rng.integers(16, 48), rng.integers(6, 12)
            m = ((yy - cy) ** 2 + (xx - cx) ** 2) < r * r
        else:
            # amorphous: elongated noisy band
            cy = rng.integers(10, 54)
            m = np.abs(yy - cy) < rng.integers(3, 8)
            m &= (xx > rng.integers(0, 10)) & (xx < rng.integers(50, 64))
            m |= rng.random((size, size)) > 0.97
        img[:, m] += 0.4
        imgs.append(img)
        masks.append(m.astype(np.float32))
    return np.stack(imgs), np.stack(masks)


def exclusion_from_mask(masks: np.ndarray) -> np.ndarray:
    """Negative ring from a loose box around GT — uses GT (analysis tool; tightness ablation in E1)."""
    n, h, w = masks.shape
    out = np.zeros((n, 1, h, w), np.float32)
    for i, m in enumerate(masks):
        ys, xs = np.where(m > 0.5)
        if len(ys) == 0:
            continue
        y0, y1 = max(0, ys.min() - 4), min(h, ys.max() + 5)
        x0, x1 = max(0, xs.min() - 4), min(w, xs.max() + 5)
        out[i, 0, y0:y1, x0:x1] = 1.0
        out[i, 0] *= (m < 0.5)
    return out


def nsd_proxy(pred: np.ndarray, gt: np.ndarray, thr: float) -> float:
    """Cheap surface-overlap proxy (not official NSD). EXPECTED toy metric only."""
    pb, gb = pred > thr, gt > 0.5
    if pb.sum() == 0 and gb.sum() == 0:
        return 1.0
    inter = np.logical_and(pb, gb).sum()
    return float(2 * inter / (pb.sum() + gb.sum() + 1e-6))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="configs/killer_e0.yaml")
    args = p.parse_args()
    cfg = load_cfg(args.config)
    torch.manual_seed(cfg.seed)
    rng = np.random.default_rng(cfg.seed)
    device = torch.device("cpu")

    xa, ya = blob_mask(cfg.n_amorphous, cfg.image_size, "amorphous", rng)
    xo, yo = blob_mask(cfg.n_coco, cfg.image_size, "object", rng)
    ea = exclusion_from_mask(ya)
    eo = exclusion_from_mask(yo)

    enc = FakeEncoder(cfg.embed_dim).to(device).eval()
    head = DensityHead(cfg.embed_dim).to(device)
    opt = torch.optim.Adam(head.parameters(), lr=cfg.lr)

    def tensors(x, y, e):
        xt = torch.from_numpy(x).to(device)
        yt = torch.from_numpy(y)[:, None].to(device)
        et = torch.from_numpy(e).to(device)
        et = F.interpolate(et, size=(cfg.image_size // 4, cfg.image_size // 4), mode="nearest")
        yt_s = F.interpolate(yt, size=et.shape[-2:], mode="nearest")
        return xt, yt_s, et, yt

    xta, yta, eta, ya_full = tensors(xa, ya, ea)
    with torch.no_grad():
        za = enc(xta)

    for _ in range(cfg.epochs):
        head.train()
        pred = head(za, eta)
        tv = (pred[:, :, :, 1:] - pred[:, :, :, :-1]).abs().mean() + (
            pred[:, :, 1:, :] - pred[:, :, :-1, :]
        ).abs().mean()
        loss = cfg.lambda_bce * F.binary_cross_entropy(pred, yta) + cfg.lambda_dice * dice_loss(pred, yta) + cfg.lambda_tv * tv
        opt.zero_grad()
        loss.backward()
        opt.step()

    out = Path(cfg.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    torch.save(head.state_dict(), out / "density_head.pt")

    head.eval()
    with torch.no_grad():
        pred_a = F.interpolate(head(za, eta), size=(cfg.image_size, cfg.image_size), mode="bilinear")
    nsd_a = nsd_proxy(pred_a.cpu().numpy(), ya[:, None], cfg.threshold)
    dice_a = float(
        (2 * ((pred_a.cpu().numpy() > cfg.threshold) & (ya[:, None] > 0.5)).sum())
        / ((pred_a.cpu().numpy() > cfg.threshold).sum() + (ya > 0.5).sum() + 1e-6)
    )
    pred_mean_a = float(pred_a.mean())

    xto, yto, eto, _ = tensors(xo, yo, eo)
    with torch.no_grad():
        zo = enc(xto)
        pred_o = F.interpolate(head(zo, eto), size=(cfg.image_size, cfg.image_size), mode="bilinear")
    nsd_o = nsd_proxy(pred_o.cpu().numpy(), yo[:, None], cfg.threshold)

    report = (
        "TOY RUN (FakeEncoder). NOT a scientific result.\n"
        f"amorphous_nsd_proxy={nsd_a:.4f} pred_mean={pred_mean_a:.4f} dice_hard={dice_a:.4f}\n"
        f"object_nsd_proxy={nsd_o:.4f}\n"
        "H1/H2 require real SAM embeddings and real datasets.\n"
    )
    (out / "toy_report.txt").write_text(report)
    print(report)


if __name__ == "__main__":
    main()
