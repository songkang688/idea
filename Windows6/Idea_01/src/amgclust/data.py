"""Data sources. Synthetic phantoms are available; real CT is not."""

from __future__ import annotations

import numpy as np

# Approximate HU plateaus for a soft-tissue phantom. These are textbook tissue
# ranges used only to give the synthetic phantom a realistic dynamic range;
# they are not a measurement and nothing in the analysis depends on them.
_HU_PLATEAUS = {"air": -1000.0, "fat": -90.0, "soft": 45.0, "liver": 60.0, "bone": 700.0}

WINDOWS = {
    "abdomen": (400.0, 40.0),
    "bone": (2000.0, 400.0),
    "lung": (1500.0, -600.0),
}


def apply_window(hu: np.ndarray, window: str) -> np.ndarray:
    """Map HU to [0, 1] through a documented width/level pair."""
    if window not in WINDOWS:
        raise ValueError(f"unknown window {window!r}; known: {sorted(WINDOWS)}")
    width, level = WINDOWS[window]
    lo, hi = level - width / 2.0, level + width / 2.0
    return np.clip((np.asarray(hu, dtype=np.float64) - lo) / (hi - lo), 0.0, 1.0)


def synthetic_ct(
    size: int = 96,
    rng: np.random.Generator | None = None,
    texture_sigma: float = 8.0,
) -> np.ndarray:
    """Piecewise-constant HU phantom with additive texture.

    Piecewise-constant is the right shape for the harness test: if the metrics
    cannot see clustering structure *here*, they will not see it on CT either.
    Texture is added so the texture-shuffle arm has something to shuffle.
    """
    rng = rng or np.random.default_rng(0)
    img = np.full((size, size), _HU_PLATEAUS["air"], dtype=np.float64)
    ys, xs = np.mgrid[0:size, 0:size]

    body = (ys - size / 2) ** 2 / (0.42 * size) ** 2 + (xs - size / 2) ** 2 / (0.45 * size) ** 2 <= 1
    img[body] = _HU_PLATEAUS["soft"]

    fat_ring = body & ~(
        (ys - size / 2) ** 2 / (0.36 * size) ** 2 + (xs - size / 2) ** 2 / (0.39 * size) ** 2 <= 1
    )
    img[fat_ring] = _HU_PLATEAUS["fat"]

    organ = (ys - size * 0.42) ** 2 / (0.20 * size) ** 2 + (xs - size * 0.38) ** 2 / (
        0.24 * size
    ) ** 2 <= 1
    img[organ] = _HU_PLATEAUS["liver"]

    spine = (np.abs(xs - size * 0.5) < size * 0.07) & (np.abs(ys - size * 0.75) < size * 0.07)
    img[spine] = _HU_PLATEAUS["bone"]

    img[body] += rng.normal(scale=texture_sigma, size=int(body.sum()))
    return img


def load_real_ct_slices(*_args, **_kwargs) -> np.ndarray:
    """Real CT loader. Not implemented here on purpose."""
    raise NotImplementedError(
        "No real CT data ships with this repository. The pre-registered protocol "
        "(Idea_01/experiments.md, card E1) needs 100 TotalSegmentator or MSD slices "
        "with documented window/level. Implement this against nibabel/pydicom in the "
        "lab. Windows6 has produced NO real SAM numbers to date."
    )
