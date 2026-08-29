"""Frozen-encoder linear probe — the week-1 killer experiment (STUB where marked).

Question (stage6_battle.md decisive experiment #3): does a matting-pretrained encoder
carry more *linearly available* smoke evidence than a COCO-seg-pretrained encoder, on
real smoke, at small label budgets?

Design (metrics_protocol.md section 7):
- Encoders are FROZEN. The probe is a single 1x1 conv from patch features to a logit
  map, bilinearly upsampled to input resolution. No decoder, no adapters — anything
  bigger would measure fine-tunability, not representation content.
- Budgets N in {25, 50, 100, 250} x 3 seeds; identical schedule for every encoder.
- Endpoint: real-smoke test mIoU (+ f_beta / mmse for continuity), scored with
  src/alphasmoke/metrics under the frozen protocol.
- Decision rule K-A1 (experiments.md section 2): no separation at any budget =>
  the Part-A pretrain grid is NOT funded.

STUB BOUNDARY — what is and is not implemented here:
- Implemented: probe head, training/eval loops, budget/seed sweep driver, metric
  wiring, config parsing. This code is complete and runnable given an encoder.
- STUB (deliberately): `load_encoder` raises with instructions for each registry
  entry. Checkpoint acquisition happens at runbook step R2 after the license audit
  (R0); shipping fake weights or silently downloading unverified checkpoints would
  violate the package's no-fabrication rule.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Callable

import numpy as np

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F

    _TORCH_OK = True
except ImportError:  # torch optional: metrics/baselines must not depend on it
    _TORCH_OK = False


# --------------------------------------------------------------------------------------
# Encoder registry (STUB): filled at runbook step R2, after the R0 license audit.
# Each entry documents exactly which public artifact it expects, so a reviewer can
# reproduce the arm from the paper's checkpoint table.
# --------------------------------------------------------------------------------------

@dataclass
class EncoderSpec:
    name: str
    provenance: str  # 'matting' | 'segmentation' | 'imagenet'
    expected_source: str  # where the checkpoint comes from (documented, not bundled)
    feature_stride: int = 16


ENCODER_REGISTRY: dict[str, EncoderSpec] = {
    "matting_vitb": EncoderSpec(
        name="matting_vitb",
        provenance="matting",
        expected_source=(
            "Public matting-pretrained ViT-B encoder (MAM arXiv:2306.05399 [S3] or "
            "ViTMatte-class [M]); exact checkpoint hash recorded in "
            "configs/linear_probe.yaml at run time."
        ),
    ),
    "cocoseg_vitb": EncoderSpec(
        name="cocoseg_vitb",
        provenance="segmentation",
        expected_source=(
            "Public segmentation-pretrained ViT-B encoder at matched backbone size "
            "(SAM ViT-B image encoder or ViTDet-COCO [M]); recorded at run time."
        ),
    ),
    "imagenet_vitb": EncoderSpec(
        name="imagenet_vitb",
        provenance="imagenet",
        expected_source="timm/torchvision ImageNet ViT-B [M]; control encoder.",
    ),
}


def load_encoder(spec_name: str) -> "Callable[[torch.Tensor], torch.Tensor]":
    """STUB — resolve an EncoderSpec to a frozen feature extractor.

    Must return a callable mapping (B, 3, H, W) float images to (B, C, H/s, W/s)
    features with requires_grad disabled. Implemented at runbook step R2 once the
    checkpoint table in configs/linear_probe.yaml is filled and verified.
    """
    if spec_name not in ENCODER_REGISTRY:
        raise KeyError(f"unknown encoder '{spec_name}'; registry: {sorted(ENCODER_REGISTRY)}")
    spec = ENCODER_REGISTRY[spec_name]
    raise NotImplementedError(
        f"Encoder '{spec.name}' is a stub pending runbook step R2 (checkpoint "
        f"acquisition + verification). Expected source: {spec.expected_source} "
        "Fill configs/linear_probe.yaml:encoders.<name>.checkpoint and implement the "
        "loader here. No checkpoint is bundled with this package by design."
    )


# --------------------------------------------------------------------------------------
# Probe head + training loop (complete, runnable given an encoder callable).
# --------------------------------------------------------------------------------------

if _TORCH_OK:

    class LinearProbeHead(nn.Module):
        """1x1 conv from frozen features to a logit map, upsampled to input size.

        Deliberately minimal: the probe measures linearly available evidence
        (metrics_protocol.md section 7); capacity beyond 1x1 would contaminate the
        comparison.
        """

        def __init__(self, in_channels: int):
            super().__init__()
            self.proj = nn.Conv2d(in_channels, 1, kernel_size=1, bias=True)

        def forward(self, feats: "torch.Tensor", out_hw: tuple[int, int]) -> "torch.Tensor":
            logits = self.proj(feats)
            return F.interpolate(logits, size=out_hw, mode="bilinear", align_corners=False)

    def train_linear_probe(
        encoder: "Callable[[torch.Tensor], torch.Tensor]",
        train_loader,
        val_loader,
        in_channels: int,
        lr: float = 1e-3,
        weight_decay: float = 1e-4,
        max_epochs: int = 50,
        patience: int = 5,
        device: str = "cuda",
        seed: int = 0,
    ) -> tuple["LinearProbeHead", dict]:
        """Train the probe on frozen features; early stop on val loss.

        Loaders yield (image (B,3,H,W) in [0,1], mask (B,1,H,W) in {0,1}). The
        identical schedule is used for every encoder (protocol requirement).
        """
        torch.manual_seed(seed)
        head = LinearProbeHead(in_channels).to(device)
        opt = torch.optim.AdamW(head.parameters(), lr=lr, weight_decay=weight_decay)
        loss_fn = nn.BCEWithLogitsLoss()

        best_val, best_state, bad_epochs = float("inf"), None, 0
        history = {"train_loss": [], "val_loss": []}

        for _epoch in range(max_epochs):
            head.train()
            tr_losses = []
            for img, mask in train_loader:
                img, mask = img.to(device), mask.to(device).float()
                with torch.no_grad():
                    feats = encoder(img)
                logits = head(feats, out_hw=img.shape[-2:])
                loss = loss_fn(logits, mask)
                opt.zero_grad()
                loss.backward()
                opt.step()
                tr_losses.append(loss.item())

            head.eval()
            va_losses = []
            with torch.no_grad():
                for img, mask in val_loader:
                    img, mask = img.to(device), mask.to(device).float()
                    feats = encoder(img)
                    logits = head(feats, out_hw=img.shape[-2:])
                    va_losses.append(loss_fn(logits, mask).item())

            history["train_loss"].append(float(np.mean(tr_losses)))
            history["val_loss"].append(float(np.mean(va_losses)))

            if history["val_loss"][-1] < best_val - 1e-5:
                best_val = history["val_loss"][-1]
                best_state = {k: v.detach().clone() for k, v in head.state_dict().items()}
                bad_epochs = 0
            else:
                bad_epochs += 1
                if bad_epochs >= patience:
                    break

        if best_state is not None:
            head.load_state_dict(best_state)
        return head, history

    @torch.no_grad()
    def evaluate_probe(
        encoder: "Callable[[torch.Tensor], torch.Tensor]",
        head: "LinearProbeHead",
        test_loader,
        threshold: float = 0.5,
        device: str = "cuda",
    ) -> dict:
        """Per-image IoU / f_beta / mmse under the frozen operating threshold.

        Uses src/alphasmoke/metrics so probe numbers and Part-B numbers share one
        metric implementation (no protocol drift between experiments).
        """
        from ..metrics import binary_metrics as bm
        from ..metrics.alpha_metrics import mmse_per_image

        head.eval()
        per_image = {"iou": [], "f_beta": [], "mmse": []}
        for img, mask in test_loader:
            img = img.to(device)
            feats = encoder(img)
            probs = torch.sigmoid(head(feats, out_hw=img.shape[-2:])).cpu().numpy()
            gts = mask.cpu().numpy()
            for i in range(probs.shape[0]):
                p, g = probs[i, 0], gts[i, 0].astype(np.uint8)
                per_image["iou"].append(bm.iou(p >= threshold, g))
                per_image["f_beta"].append(bm.f_beta(p >= threshold, g))
                per_image["mmse"].append(mmse_per_image(np.clip(p, 0, 1), g))
        return {k: float(np.mean(v)) for k, v in per_image.items()} | {
            f"{k}_per_image": v for k, v in per_image.items()
        }


def main() -> None:
    """CLI driver for the budget x seed sweep. Requires the encoder stubs to be
    resolved first (runbook R2); until then this exits with the stub message."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="configs/linear_probe.yaml")
    parser.add_argument("--encoder", required=True, choices=sorted(ENCODER_REGISTRY))
    args = parser.parse_args()

    if not _TORCH_OK:
        raise SystemExit("torch is required for the probe experiment (pip install torch)")

    import yaml

    with open(args.config) as fh:
        cfg = yaml.safe_load(fh)
    print(f"[alphasmoke.probe] config loaded: budgets={cfg['budgets']}, seeds={cfg['seeds']}")
    load_encoder(args.encoder)  # raises with actionable stub instructions


if __name__ == "__main__":
    main()
