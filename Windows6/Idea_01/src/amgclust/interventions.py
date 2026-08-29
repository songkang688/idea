"""The counterfactual instruments — the part Reviewer #2 made binding.

Residual obligation (verbatim, `stage4_reviewer2_cheap5.jsonl`):
    "Must earn mechanistic via intensity vs texture counterfactuals;
     else evaluation note"

Two arms, each designed to move exactly one factor:

  intensity_remap  changes intensity ordering-preserving values, keeps edges
  texture_shuffle  changes local texture, keeps per-tile mean intensity

An arm that fails its own validity check is not evidence. The `check_*`
functions exist so a run can abort rather than report a broken intervention.
"""

from __future__ import annotations

import numpy as np


def intensity_remap(img: np.ndarray, gamma: float = 0.5) -> np.ndarray:
    """Strictly monotone remap of intensity. Edge *locations* are preserved.

    Monotonicity matters: a non-monotone map could create or destroy edges,
    which would confound the arm with the very thing it is controlling for.
    """
    if gamma <= 0:
        raise ValueError("gamma must be positive to stay monotone")
    x = np.asarray(img, dtype=np.float64)
    lo, hi = float(x.min()), float(x.max())
    if hi - lo < 1e-12:
        return x.copy()
    norm = (x - lo) / (hi - lo)
    return (norm**gamma) * (hi - lo) + lo


def texture_shuffle(img: np.ndarray, tile: int = 8, rng: np.random.Generator | None = None) -> np.ndarray:
    """Permute the high-frequency residual inside each tile; keep tile means.

    The mean-preservation is what makes this the intensity-preserving arm: any
    AMG response to it cannot be attributed to a change in local HU level.
    """
    rng = rng or np.random.default_rng(0)
    x = np.asarray(img, dtype=np.float64).copy()
    h, w = x.shape
    for y0 in range(0, h, tile):
        for x0 in range(0, w, tile):
            block = x[y0 : y0 + tile, x0 : x0 + tile]
            mean = block.mean()
            residual = (block - mean).reshape(-1)
            rng.shuffle(residual)
            x[y0 : y0 + tile, x0 : x0 + tile] = mean + residual.reshape(block.shape)
    return x


def sobel_magnitude(img: np.ndarray) -> np.ndarray:
    """Sobel gradient magnitude, used to check that remap keeps edge structure."""
    x = np.asarray(img, dtype=np.float64)
    padded = np.pad(x, 1, mode="edge")
    kx = np.array([[-1.0, 0.0, 1.0], [-2.0, 0.0, 2.0], [-1.0, 0.0, 1.0]])
    ky = kx.T
    gx = np.zeros_like(x)
    gy = np.zeros_like(x)
    for i in range(3):
        for j in range(3):
            shifted = padded[i : i + x.shape[0], j : j + x.shape[1]]
            gx += kx[i, j] * shifted
            gy += ky[i, j] * shifted
    return np.sqrt(gx * gx + gy * gy)


def check_shuffle_preserves_tile_means(
    original: np.ndarray, shuffled: np.ndarray, tile: int = 8, atol: float = 1e-9
) -> bool:
    """Validity check for the texture arm."""
    a = np.asarray(original, dtype=np.float64)
    b = np.asarray(shuffled, dtype=np.float64)
    if a.shape != b.shape:
        return False
    h, w = a.shape
    for y0 in range(0, h, tile):
        for x0 in range(0, w, tile):
            m1 = a[y0 : y0 + tile, x0 : x0 + tile].mean()
            m2 = b[y0 : y0 + tile, x0 : x0 + tile].mean()
            if abs(m1 - m2) > atol:
                return False
    return True


def check_remap_is_monotone(original: np.ndarray, remapped: np.ndarray, samples: int = 2000) -> bool:
    """Validity check for the intensity arm: order of pixel values is preserved."""
    a = np.asarray(original, dtype=np.float64).reshape(-1)
    b = np.asarray(remapped, dtype=np.float64).reshape(-1)
    if a.shape != b.shape:
        return False
    idx = np.argsort(a, kind="stable")
    if len(idx) > samples:
        idx = idx[np.linspace(0, len(idx) - 1, samples).astype(int)]
    ordered = b[idx]
    return bool(np.all(np.diff(ordered) >= -1e-9))
