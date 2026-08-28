"""Toy spectral audit of a LoRA-like delta. NOT measured SAM results."""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import yaml


class LoRALinear(nn.Module):
    def __init__(self, dim: int, rank: int):
        super().__init__()
        self.W = nn.Linear(dim, dim, bias=False)
        self.A = nn.Linear(dim, rank, bias=False)
        self.B = nn.Linear(rank, dim, bias=False)
        nn.init.zeros_(self.B.weight)
        for p in self.W.parameters():
            p.requires_grad = False

    def forward(self, x):
        return self.W(x) + self.B(self.A(x))


def radial_energy_fraction(delta: np.ndarray, kc_ratio: float) -> float:
    # delta: n, h, w
    acc = []
    for d in delta:
        f = np.fft.fftshift(np.fft.fft2(d))
        p = np.abs(f) ** 2
        h, w = p.shape
        cy, cx = h // 2, w // 2
        yy, xx = np.mgrid[0:h, 0:w]
        r = np.sqrt((yy - cy) ** 2 + (xx - cx) ** 2)
        kc = kc_ratio * np.sqrt(cy**2 + cx**2)
        acc.append(p[r <= kc].sum() / (p.sum() + 1e-12))
    return float(np.mean(acc))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="configs/killer_fft.yaml")
    args = p.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    torch.manual_seed(cfg["seed"])
    dim, sp, n, rank = cfg["dim"], cfg["spatial"], cfg["n"], cfg["rank"]
    layer = LoRALinear(dim, rank)
    opt = torch.optim.Adam([*layer.A.parameters(), *layer.B.parameters()], lr=1e-2)
    x = torch.randn(n, sp * sp, dim)
    y = torch.randn(n, sp * sp, dim)
    for _ in range(40):
        loss = (layer(x) - y).pow(2).mean()
        opt.zero_grad()
        loss.backward()
        opt.step()
    with torch.no_grad():
        delta = (layer(x) - layer.W(x)).mean(-1).reshape(n, sp, sp).cpu().numpy()
    frac = radial_energy_fraction(delta, cfg["kc_ratio"])
    out = Path(cfg["out_dir"])
    out.mkdir(parents=True, exist_ok=True)
    txt = (
        "TOY LoRA on random tensors. NOT a scientific result.\n"
        f"low_freq_energy_fraction={frac:.4f} kc_ratio={cfg['kc_ratio']}\n"
        "H1 requires real SAM/ViT feature deltas after medical PEFT.\n"
    )
    (out / "toy_report.txt").write_text(txt)
    print(txt)


if __name__ == "__main__":
    main()
