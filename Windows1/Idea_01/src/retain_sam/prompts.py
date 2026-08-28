"""Prompt sampling for SAM-style tensors. Prototype."""

from __future__ import annotations

import torch


def random_positive_clicks(masks: torch.Tensor, n: int = 1) -> torch.Tensor:
    """masks (B,1,H,W) in {0,1} -> click coords (B,n,2) as (y,x). Fallback to center."""
    B, _, H, W = masks.shape
    clicks = torch.zeros(B, n, 2, device=masks.device)
    for b in range(B):
        ys, xs = torch.where(masks[b, 0] > 0.5)
        if len(ys) == 0:
            clicks[b] = torch.tensor([[H / 2, W / 2]], device=masks.device).repeat(n, 1)
            continue
        idx = torch.randint(0, len(ys), (n,), device=masks.device)
        clicks[b, :, 0] = ys[idx].float()
        clicks[b, :, 1] = xs[idx].float()
    return clicks


def noisy_box_from_mask(masks: torch.Tensor, pad: float = 0.1) -> torch.Tensor:
    """Return xyxy (B,4)."""
    B, _, H, W = masks.shape
    boxes = torch.zeros(B, 4, device=masks.device)
    for b in range(B):
        ys, xs = torch.where(masks[b, 0] > 0.5)
        if len(ys) == 0:
            boxes[b] = torch.tensor([0, 0, W - 1, H - 1], device=masks.device)
            continue
        y0, y1 = ys.min().float(), ys.max().float()
        x0, x1 = xs.min().float(), xs.max().float()
        h, w = (y1 - y0).clamp(min=1), (x1 - x0).clamp(min=1)
        y0 = (y0 - pad * h).clamp(0, H - 1)
        x0 = (x0 - pad * w).clamp(0, W - 1)
        y1 = (y1 + pad * h).clamp(0, H - 1)
        x1 = (x1 + pad * w).clamp(0, W - 1)
        boxes[b] = torch.stack([x0, y0, x1, y1])
    return boxes
