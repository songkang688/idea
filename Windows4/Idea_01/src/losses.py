"""Losses for the learned box->mask null (the only trained component in this project;
SAM itself is always frozen — rubric compliance, proposal §11)."""

from __future__ import annotations

try:
    import torch
    import torch.nn.functional as F
except Exception as e:  # pragma: no cover
    raise ImportError("src.losses requires torch: pip install torch") from e


def soft_dice_loss(logits: "torch.Tensor", target: "torch.Tensor", eps: float = 1e-6):
    """logits/target: (B, G*G) or (B, G, G); target in {0,1}."""
    p = torch.sigmoid(logits).flatten(1)
    t = target.flatten(1)
    inter = (p * t).sum(dim=1)
    denom = p.sum(dim=1) + t.sum(dim=1)
    return (1.0 - (2 * inter + eps) / (denom + eps)).mean()


def dice_bce_loss(logits, target, bce_weight: float = 0.5):
    bce = F.binary_cross_entropy_with_logits(logits.flatten(1), target.flatten(1))
    return bce_weight * bce + (1.0 - bce_weight) * soft_dice_loss(logits, target)
