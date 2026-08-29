"""Episode construction and the pre-registered query-complexity strata.

The strata are the reason this audit can separate "the model ignores its support"
from "the benchmark's queries have exactly one salient object". They are computed
from instance annotations only, never from model output, so they are frozen before
any inference runs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

import numpy as np

# Pre-registered stratum labels (proposal.md section 3).
S1_SINGLE = "S1_single_object"
S2_MULTI_SAME = "S2_multi_object_same_class"
S3_DISTRACTOR = "S3_distractor_present"  # PRIMARY
S4_DEGENERATE = "S4_degenerate_control"

STRATA = (S1_SINGLE, S2_MULTI_SAME, S3_DISTRACTOR, S4_DEGENERATE)


@dataclass(frozen=True)
class Instance:
    class_id: int
    mask: np.ndarray


@dataclass
class Episode:
    """A support/query pair plus everything needed to stratify and audit it."""

    episode_id: str
    benchmark: str
    fold: int
    class_id: int
    support_image_id: str
    support_mask: np.ndarray
    query_image_id: str
    query_gt: np.ndarray
    query_instances: list[Instance] = field(default_factory=list)
    is_degenerate_benchmark: bool = False

    @property
    def support_mask_area_frac(self) -> float:
        return float(self.support_mask.mean())

    def present_class_ids(self) -> set[int]:
        return {inst.class_id for inst in self.query_instances}

    def stratum(self) -> str:
        """Assign the pre-registered stratum. Order matters: the distractor test
        dominates, because S3 is where a saliency prior and a support-conditioned
        method are forced to disagree."""
        if self.is_degenerate_benchmark:
            return S4_DEGENERATE
        classes = [inst.class_id for inst in self.query_instances]
        if any(c != self.class_id for c in classes):
            return S3_DISTRACTOR
        if len(classes) >= 2:
            return S2_MULTI_SAME
        return S1_SINGLE


def stratum_counts(episodes: Iterable[Episode]) -> dict[str, int]:
    """Published before any inferential claim (proposal.md section 21, attack A5)."""
    counts = dict.fromkeys(STRATA, 0)
    for ep in episodes:
        counts[ep.stratum()] += 1
    return counts
