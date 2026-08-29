"""Episode-level measurements for the wrong-support counterfactual audit.

Every quantity here is defined in proposal.md section 3. Nothing in this module
touches a network; it operates on boolean masks so it can be unit-tested and so
the statistics can be validated before any checkpoint is downloaded.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np


def iou(a: np.ndarray, b: np.ndarray) -> float:
    """Intersection over union of two boolean masks."""
    a = np.asarray(a, dtype=bool)
    b = np.asarray(b, dtype=bool)
    if a.shape != b.shape:
        raise ValueError(f"mask shape mismatch: {a.shape} vs {b.shape}")
    union = np.logical_or(a, b).sum()
    if union == 0:
        # Both empty. Convention: a correct empty prediction scores 1.0.
        return 1.0
    return float(np.logical_and(a, b).sum() / union)


@dataclass(frozen=True)
class EpisodeMeasurement:
    """One episode scored under the correct support and K wrong supports."""

    episode_id: str
    method: str
    benchmark: str
    stratum: str
    a_corr: float
    a_wrong: list[float]
    insensitivity: list[float]
    a_floor_strong: float
    a_floor_weak: float
    n_area_relaxations: int = 0

    @property
    def wrong_median(self) -> float:
        return float(np.median(self.a_wrong)) if self.a_wrong else float("nan")

    @property
    def retention(self) -> float:
        """R = median wrong-support IoU / correct-support IoU.

        Undefined when a_corr is 0; callers must apply the pre-registered tau
        filter (see keep_for_retention) before aggregating.
        """
        if self.a_corr <= 0:
            return float("nan")
        return self.wrong_median / self.a_corr

    @property
    def insensitivity_median(self) -> float:
        return float(np.median(self.insensitivity)) if self.insensitivity else float("nan")

    @property
    def flipped(self) -> bool:
        """Prediction essentially unchanged by destroying the support."""
        return self.insensitivity_median > 0.9

    def keep_for_retention(self, tau: float) -> bool:
        """Pre-registered episode filter. tau is frozen before the run and its
        sensitivity curve is published (proposal.md section 16)."""
        return self.a_corr >= tau


def support_sensitivity_score(retentions: Sequence[float]) -> float:
    """SSS = 1 - median retention. Higher means the method actually uses its support."""
    finite = [r for r in retentions if np.isfinite(r)]
    if not finite:
        return float("nan")
    return 1.0 - float(np.median(finite))


def flip_rate(measurements: Sequence[EpisodeMeasurement]) -> float:
    if not measurements:
        return float("nan")
    return float(np.mean([m.flipped for m in measurements]))
