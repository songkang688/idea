"""Axis-aligned bounding-box utilities.

Boxes are float arrays in xyxy format: (x_min, y_min, x_max, y_max).
The synthetic image is the unit square, but nothing here assumes that.
"""

from __future__ import annotations

import numpy as np


def box_area(boxes: np.ndarray) -> np.ndarray:
    """Areas of an (..., 4) array of xyxy boxes (degenerate boxes -> 0)."""
    boxes = np.asarray(boxes, dtype=np.float64)
    w = np.clip(boxes[..., 2] - boxes[..., 0], 0.0, None)
    h = np.clip(boxes[..., 3] - boxes[..., 1], 0.0, None)
    return w * h


def iou_matrix(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Pairwise IoU between (N, 4) and (M, 4) xyxy boxes -> (N, M) float64."""
    a = np.asarray(a, dtype=np.float64).reshape(-1, 4)
    b = np.asarray(b, dtype=np.float64).reshape(-1, 4)
    if a.shape[0] == 0 or b.shape[0] == 0:
        return np.zeros((a.shape[0], b.shape[0]), dtype=np.float64)
    lt = np.maximum(a[:, None, :2], b[None, :, :2])
    rb = np.minimum(a[:, None, 2:], b[None, :, 2:])
    wh = np.clip(rb - lt, 0.0, None)
    inter = wh[..., 0] * wh[..., 1]
    union = box_area(a)[:, None] + box_area(b)[None, :] - inter
    return np.where(union > 0.0, inter / np.maximum(union, 1e-12), 0.0)
