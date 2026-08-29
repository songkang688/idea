"""Per-repository adapters.

Each audited method keeps its own preprocessing, resizing and post-processing.
That is deliberate: unifying them would destroy the evaluator-discrepancy table
that is the paper's second headline (proposal.md section 15, E5). An adapter
therefore does exactly one thing -- inject an arbitrary support pair into an
otherwise untouched episode -- and nothing else.
"""

from __future__ import annotations

from typing import Protocol

import numpy as np


class FSSAdapter(Protocol):
    """The single hook every audited repository must expose."""

    name: str
    family: str  # "specialist" or "foundation"

    def segment(
        self,
        support_image: np.ndarray,
        support_mask: np.ndarray,
        query_image: np.ndarray,
    ) -> np.ndarray:
        """Return a boolean query mask. Must not read any label of the query."""
        ...


def connected_components(mask: np.ndarray, min_size: int = 8) -> list[np.ndarray]:
    """4-connected components, dependency-free (no scipy)."""
    mask = np.asarray(mask, dtype=bool)
    seen = np.zeros_like(mask)
    out: list[np.ndarray] = []
    h, w = mask.shape
    for sy, sx in zip(*np.nonzero(mask)):
        if seen[sy, sx]:
            continue
        comp = np.zeros_like(mask)
        stack = [(int(sy), int(sx))]
        seen[sy, sx] = True
        while stack:
            y, x = stack.pop()
            comp[y, x] = True
            for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True
                    stack.append((ny, nx))
        if comp.sum() >= min_size:
            out.append(comp)
    return out


class MockSegmenter:
    """Reference implementation used to validate the harness end to end.

    It proposes candidate objects in the query and picks one by a weighted sum of
    a class-blind centrality prior and a support-conditioned appearance match.
    `support_reliance` interpolates between the two:

      0.0 -> picks the most central object, whatever the support says. The audit
             must report retention near 1.0: destroying the support changes
             nothing. This is the failure mode the whole project exists to detect.
      1.0 -> picks the object whose appearance matches the support. A wrong-class
             support should drag it onto a distractor, so retention must fall.

    Those two behaviours are the harness's positive and negative controls. If a
    run does not separate them, the harness is broken and no number it produces
    about a real method would mean anything.

    This is a test fixture. It is not a baseline and it produces no result that
    appears in any table of the paper.
    """

    family = "mock"

    def __init__(self, name: str, support_reliance: float, seed: int = 0):
        if not 0.0 <= support_reliance <= 1.0:
            raise ValueError("support_reliance must lie in [0, 1]")
        self.name = name
        self.support_reliance = support_reliance
        self._rng = np.random.default_rng(seed)

    @staticmethod
    def _descriptor(img: np.ndarray, mask: np.ndarray | None = None) -> np.ndarray:
        """Mean RGB of the masked region -- a stand-in for a class prototype."""
        img = img if img.ndim == 3 else np.repeat(img[..., None], 3, axis=2)
        if mask is None:
            return img.reshape(-1, img.shape[2]).mean(axis=0)
        m = np.asarray(mask, dtype=bool)
        if not m.any():
            return img.reshape(-1, img.shape[2]).mean(axis=0)
        return img[m].mean(axis=0)

    def segment(
        self,
        support_image: np.ndarray,
        support_mask: np.ndarray,
        query_image: np.ndarray,
    ) -> np.ndarray:
        # Prototype read from the SUPPORT image only. Reading the query here would
        # silently make every mock support-blind and the controls meaningless.
        proto = self._descriptor(support_image, support_mask)

        qgray = query_image.mean(axis=2) if query_image.ndim == 3 else query_image
        fg = qgray > (float(np.median(qgray)) + 0.5 * float(qgray.std()) + 1e-6)
        candidates = connected_components(fg)
        if not candidates:
            return np.zeros_like(fg)

        h, w = qgray.shape
        cy, cx = (h - 1) / 2, (w - 1) / 2
        diag = np.hypot(cy, cx)
        best, best_score = candidates[0], -np.inf
        for cand in candidates:
            ys, xs = np.nonzero(cand)
            centrality = 1.0 - float(np.hypot(ys.mean() - cy, xs.mean() - cx) / diag)
            # Exponential rather than a clipped linear falloff: clipping saturates
            # for every wrong-class support, which produces ties that argmax
            # resolves by candidate order and silently destroys the control.
            d = float(np.linalg.norm(self._descriptor(query_image, cand) - proto))
            appearance = float(np.exp(-d / 0.25))
            score = (
                (1 - self.support_reliance) * centrality
                + self.support_reliance * appearance
            )
            if score > best_score:
                best, best_score = cand, score
        return best
