"""Support-free objectness floors.

The floor is the null model of the whole audit: it answers "what score does a
method that never reads the support get on this episode?". Reviewer attack A2
(proposal.md section 21) is that the verdict depends on which floor you grant,
because SAM's automatic mask generator is a very strong class-agnostic segmenter
while a classical saliency detector is weak. We refuse to pick. Every
floor-dependent claim is reported under both.
"""

from __future__ import annotations

from typing import Protocol

import numpy as np


class Floor(Protocol):
    """A support-free segmenter: it sees the query and nothing else."""

    name: str

    def predict(self, query_image: np.ndarray) -> np.ndarray:  # -> boolean mask
        ...


class CentralLargestMaskFloor:
    """Floor-A (strong): pick the largest SAM-AMG mask whose centroid is central.

    In the real run, `propose` is SAM automatic mask generation. It is injected so
    that the selection rule can be tested without loading SAM.
    """

    name = "floor_a_strong_sam_amg"

    def __init__(self, propose, central_frac: float = 0.5):
        self.propose = propose
        self.central_frac = central_frac

    def predict(self, query_image: np.ndarray) -> np.ndarray:
        masks = list(self.propose(query_image))
        if not masks:
            return np.zeros(query_image.shape[:2], dtype=bool)
        h, w = query_image.shape[:2]
        lo_y, hi_y = h * (1 - self.central_frac) / 2, h * (1 + self.central_frac) / 2
        lo_x, hi_x = w * (1 - self.central_frac) / 2, w * (1 + self.central_frac) / 2

        central = []
        for m in masks:
            ys, xs = np.nonzero(m)
            if ys.size == 0:
                continue
            cy, cx = ys.mean(), xs.mean()
            if lo_y <= cy <= hi_y and lo_x <= cx <= hi_x:
                central.append(m)
        pool = central or masks
        return max(pool, key=lambda m: int(np.count_nonzero(m))).astype(bool)


class SaliencyThresholdFloor:
    """Floor-B (weak): threshold a classical saliency map.

    Deliberately weaker than Floor-A. A conclusion that survives Floor-A is strong;
    one that only holds under Floor-B is reported as exactly that.
    """

    name = "floor_b_weak_saliency"

    def __init__(self, saliency, threshold: float = 0.5):
        self.saliency = saliency
        self.threshold = threshold

    def predict(self, query_image: np.ndarray) -> np.ndarray:
        smap = np.asarray(self.saliency(query_image), dtype=float)
        if smap.max() > smap.min():
            smap = (smap - smap.min()) / (smap.max() - smap.min())
        return smap >= self.threshold


def center_prior_saliency(query_image: np.ndarray) -> np.ndarray:
    """A dependency-free stand-in used by the mock pipeline and by unit tests.

    This is NOT the floor used in the real audit; it exists so the harness runs
    without OpenCV or a saliency checkpoint.
    """
    h, w = query_image.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    cy, cx = (h - 1) / 2, (w - 1) / 2
    r2 = ((yy - cy) / max(cy, 1)) ** 2 + ((xx - cx) / max(cx, 1)) ** 2
    return np.exp(-2.0 * r2)
