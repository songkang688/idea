"""Geometric null: filled ellipse in the box."""
from __future__ import annotations
import numpy as np

def ellipse_mask(h: int, w: int, box: tuple[int, int, int, int]) -> np.ndarray:
    x0, y0, x1, y1 = box
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(w, x1), min(h, y1)
    m = np.zeros((h, w), dtype=np.uint8)
    if x1 <= x0 or y1 <= y0:
        return m
    yy, xx = np.ogrid[0:h, 0:w]
    cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    rx, ry = max((x1 - x0) / 2.0, 1.0), max((y1 - y0) / 2.0, 1.0)
    m = (((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1.0).astype(np.uint8)
    return m
