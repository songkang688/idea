"""Surrogate memory-bank tracker (SAM2-*style*, NOT SAM2).

A minimal stand-in for a streaming video-object tracker with a memory bank of
recent (appearance, location) observations of the tracked masklet — the same
functional shape as SAM2's memory attention (recency-weighted appearance
template + a spatial prior around the last confirmed location), but with the
appearance-vs-location arbitration exposed as an explicit parameter
``lambda_loc`` in [0, 1]:

    score(candidate) = (1 - lambda_loc) * appearance_similarity
                       + lambda_loc     * location_prior

Because the surrogate's arbitration is a known ground truth, the probe can be
VALIDATED as a measurement instrument on it: the probe's recovered
location-prior index must increase monotonically with the true ``lambda_loc``.
That validation is the point of this prototype; nothing here measures SAM2.

The hypothesized failure ("memory continues the wrong identity") is
mechanistic here: once the tracker selects the distractor, its memory absorbs
the distractor's appearance and location, so subsequent frames re-confirm the
wrong object (memory pollution). ``update_memory=False`` freezes the bank to
ablate that mechanism.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import numpy as np

from .world import Candidate


@dataclass
class MemoryEntry:
    app: np.ndarray
    loc: np.ndarray
    age: float  # world steps since this observation


class MemoryBankTracker:
    def __init__(
        self,
        lambda_loc: float = 0.5,
        sigma_loc: float = 12.0,
        mem_size: int = 6,
        mem_decay: float = 0.65,
        accept_threshold: float = 0.35,
        update_memory: bool = True,
        score_noise: float = 0.01,
        rng: Optional[np.random.Generator] = None,
    ):
        if not 0.0 <= lambda_loc <= 1.0:
            raise ValueError("lambda_loc must be in [0, 1]")
        self.lambda_loc = lambda_loc
        self.sigma_loc = sigma_loc
        self.mem_size = mem_size
        self.mem_decay = mem_decay
        self.accept_threshold = accept_threshold
        self.update_memory = update_memory
        self.score_noise = score_noise
        self.rng = rng or np.random.default_rng(0)
        self.memory: List[MemoryEntry] = []

    # -- memory readout ----------------------------------------------------
    def template(self) -> np.ndarray:
        """Recency-weighted appearance template over the memory bank."""
        weights = np.array([self.mem_decay**e.age for e in self.memory])
        weights /= weights.sum()
        t = np.sum([w * e.app for w, e in zip(weights, self.memory)], axis=0)
        return t / np.linalg.norm(t)

    def predicted_loc(self) -> np.ndarray:
        """Constant-position prior: most recent confirmed location."""
        most_recent = min(self.memory, key=lambda e: e.age)
        return most_recent.loc

    # -- protocol ----------------------------------------------------------
    def prompt(self, candidate: Candidate) -> None:
        """Frame-0 ground-truth initialization (the 'click' in exp_07)."""
        self.memory = [MemoryEntry(candidate.app.copy(), candidate.loc.copy(), age=0.0)]

    def _scores(self, candidates: List[Candidate]) -> np.ndarray:
        tpl = self.template()
        pred = self.predicted_loc()
        scores = np.empty(len(candidates))
        for i, c in enumerate(candidates):
            app_sim = (1.0 + float(tpl.dot(c.app))) / 2.0  # cosine -> [0, 1]
            dist2 = float(np.sum((c.loc - pred) ** 2))
            loc_score = np.exp(-dist2 / (2.0 * self.sigma_loc**2))
            scores[i] = (1.0 - self.lambda_loc) * app_sim + self.lambda_loc * loc_score
        scores += self.rng.normal(scale=self.score_noise, size=len(candidates))
        return scores

    def step(self, candidates: List[Candidate], dt: float = 1.0) -> Optional[str]:
        """Observe one frame ``dt`` world steps after the previous observation.

        Returns the ident of the selected candidate, or None ("lost") when no
        candidate clears the acceptance threshold. Memory ages by ``dt``
        regardless; on acceptance (and if ``update_memory``) the selected
        observation is appended — this is the identity-continuation mechanism.
        """
        for e in self.memory:
            e.age += dt
        scores = self._scores(candidates)
        best = int(np.argmax(scores))
        if scores[best] < self.accept_threshold:
            return None
        selected = candidates[best]
        if self.update_memory:
            self.memory.append(
                MemoryEntry(selected.app.copy(), selected.loc.copy(), age=0.0)
            )
            if len(self.memory) > self.mem_size:
                self.memory.sort(key=lambda e: e.age)
                del self.memory[self.mem_size :]
        return selected.ident


# -- bracketing dummy baselines (exp_07 'Baselines' section) ----------------

def location_prior_tracker(rng: Optional[np.random.Generator] = None) -> MemoryBankTracker:
    """Pure location prior: always follows the place (upper bracket)."""
    return MemoryBankTracker(
        lambda_loc=1.0, accept_threshold=0.0, score_noise=0.0, rng=rng
    )


def appearance_matcher_tracker(rng: Optional[np.random.Generator] = None) -> MemoryBankTracker:
    """Pure frame-0 template matcher: never updates memory (lower bracket)."""
    return MemoryBankTracker(
        lambda_loc=0.0,
        accept_threshold=0.0,
        update_memory=False,
        score_noise=0.0,
        rng=rng,
    )
