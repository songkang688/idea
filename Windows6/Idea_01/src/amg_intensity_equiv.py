"""
Synthetic AMG-vs-clustering agreement (no SAM weights).

This is a MINIMAL prototype of the *metrics and counterfactuals*,
using connected components of a threshold as a stand-in for AMG.
It is NOT a measurement of real SAM.

Run: python amg_intensity_equiv.py
"""
from __future__ import annotations

import numpy as np

try:
    from scipy import ndimage
except ImportError:  # pragma: no cover
    ndimage = None


def hungarian_iou(masks_a: list[np.ndarray], masks_b: list[np.ndarray]) -> float:
    if not masks_a or not masks_b:
        return 0.0
    # greedy matching (not full Hungarian; prototype)
    used = set()
    ious = []
    for a in masks_a:
        best, bj = 0.0, -1
        for j, b in enumerate(masks_b):
            if j in used:
                continue
            inter = np.logical_and(a, b).sum()
            union = np.logical_or(a, b).sum()
            iou = float(inter) / float(union) if union else 0.0
            if iou > best:
                best, bj = iou, j
        if bj >= 0:
            used.add(bj)
            ious.append(best)
    return float(np.mean(ious)) if ious else 0.0


def kmeans_masks(img: np.ndarray, k: int = 4, seed: int = 0) -> list[np.ndarray]:
    rng = np.random.default_rng(seed)
    x = img.reshape(-1, 1).astype(np.float64)
    centers = np.quantile(x, np.linspace(0.1, 0.9, k)).reshape(k, 1)
    for _ in range(8):
        d = (x - centers.T) ** 2
        lab = d.argmin(1)
        for j in range(k):
            if (lab == j).any():
                centers[j] = x[lab == j].mean()
    lab = lab.reshape(img.shape)
    return [(lab == j) for j in range(k) if (lab == j).any()]


def threshold_cc_masks(img: np.ndarray, t: float = 0.5) -> list[np.ndarray]:
    bw = img > t
    if ndimage is None:
        return [bw]
    labeled, n = ndimage.label(bw)
    return [(labeled == i) for i in range(1, n + 1)]


def make_synthetic(n: int = 64) -> np.ndarray:
    img = np.zeros((n, n), dtype=np.float32)
    img[8:24, 8:24] = 0.3
    img[32:50, 12:40] = 0.7
    img[20:28, 40:55] = 1.0
    return img


def texture_shuffle(img: np.ndarray, seed: int = 1) -> np.ndarray:
    """Keep local mean on 8x8 tiles; shuffle high-frequency residual."""
    rng = np.random.default_rng(seed)
    out = img.copy()
    h, w = img.shape
    for y in range(0, h, 8):
        for x in range(0, w, 8):
            tile = out[y : y + 8, x : x + 8]
            m = tile.mean()
            resid = tile - m
            rng.shuffle(resid.reshape(-1))
            out[y : y + 8, x : x + 8] = m + resid.reshape(tile.shape)
    return out


def intensity_remap(img: np.ndarray) -> np.ndarray:
    return np.clip(img**0.5 * 1.2, 0, 1)


def main() -> None:
    img = make_synthetic()
    amg = threshold_cc_masks(img, 0.25)
    km = kmeans_masks(img, k=4)
    print("HYPOTHESIS demo (NOT real SAM)")
    print("AMG-mock vs kmeans IoU:", round(hungarian_iou(amg, km), 3))
    img_tex = texture_shuffle(img)
    amg_tex = threshold_cc_masks(img_tex, 0.25)
    print("After texture shuffle vs original AMG-mock:", round(hungarian_iou(amg, amg_tex), 3))
    img_int = intensity_remap(img)
    amg_int = threshold_cc_masks(img_int, 0.25)
    print("After intensity remap vs original AMG-mock:", round(hungarian_iou(amg, amg_int), 3))
    print("EXPECTED if mechanism is intensity: remap IoU < shuffle IoU")


if __name__ == "__main__":
    main()
