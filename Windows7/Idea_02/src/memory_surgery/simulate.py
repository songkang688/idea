"""A toy memory-driven tracker with a controllable memory-borne failure share.

This exists so the decision pipeline can be exercised before a GPU is involved,
and so the statistics have a known ground truth to be checked against. The
simulator has two knobs that matter:

  memory_borne_share  how much of failure is caused by corrupted memory entries
                      (recoverable by deleting them) versus by the representation
                      (not recoverable by any surgery)
  recency_sensitivity how much the tracker cares about WHICH recency slot an
                      entry occupies, independent of its content

The second knob is the point. Setting recency_sensitivity high and
memory_borne_share to zero produces a tracker where targeted deletion appears to
help purely through recency re-indexing. If the sham arm cannot detect that, the
sham arm is not doing its job -- and the real experiment would mistake an
encoding artifact for a causal decomposition.

Nothing here is a model of SAM2. It is a testbed for the decision rule.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .bank import MemoryBank, MemoryEntry, build_bank


@dataclass
class SimConfig:
    """Three independent channels by which surgery can appear to help.

    Only the first is the causal story the paper wants to tell. The other two are
    the artifact channels the control arms exist to expose.
    """

    n_frames: int = 120
    capacity: int = 7
    # Channel 1 (the real effect): removing corrupted entries helps.
    memory_borne_share: float = 0.6
    # Channel 2 (hypothesis H2): retaining clean pre-error entries helps, which is
    # what should make `targeted` beat `reset`.
    clean_memory_value: float = 0.30
    # Channel 3 (the artifact): having FEWER entries helps, whatever they contain.
    # Any arm that deletes the same number of entries gets this for free, which is
    # exactly what the vacuous sham arm is built to detect.
    crowding_relief: float = 0.0
    difficulty: float = 0.5  # distractor density proxy; drives BOTH sides of validity
    noise: float = 0.05


class SimulatedTracker:
    """Produces IoU traces whose failures are attributable in a known proportion."""

    def __init__(self, cfg: SimConfig, rng: np.random.Generator):
        self.cfg = cfg
        self.rng = rng

    def build_failure_bank(self, t_f: int, t_r: int) -> MemoryBank:
        """Memory as it stands at the recovery opportunity: clean before t_f,
        corrupted after."""
        entries = []
        entries.append(
            MemoryEntry(frame_idx=0, written_at=0, is_conditioning=True, corruption=0.0)
        )
        for t in range(max(0, t_f - self.cfg.capacity), t_r):
            corrupted = t >= t_f
            entries.append(
                MemoryEntry(
                    frame_idx=t,
                    written_at=t,
                    corruption=1.0 if corrupted else 0.0,
                    tag="post_error" if corrupted else "pre_error",
                )
            )
        return build_bank(entries, capacity=self.cfg.capacity)

    def recovers(self, bank: MemoryBank, t_f: int, n_original: int) -> bool:
        """Recovery probability under the three channels of SimConfig.

        `n_original` is the pre-surgery non-conditioning entry count, so the
        crowding channel can be driven by how many entries were deleted rather
        than by which ones -- the property that makes it an artifact.
        """
        cfg = self.cfg
        non_cond = [e for e in bank.entries() if not e.is_conditioning]
        corruption = bank.mean_corruption()
        n_clean = sum(1 for e in non_cond if e.corruption < 0.5)
        n_deleted = max(n_original - len(non_cond), 0)

        p = (
            (1.0 - cfg.difficulty)
            - cfg.memory_borne_share * corruption
            + cfg.clean_memory_value * (n_clean / max(cfg.capacity, 1))
            + cfg.crowding_relief * (n_deleted / max(cfg.capacity, 1))
        )
        p += self.rng.normal(0, cfg.noise)
        return bool(self.rng.random() < np.clip(p, 0.0, 1.0))

    def comparator_gain(self, rho: float, difficulty: float, quality: float) -> float:
        """A prevention method's per-sequence gain.

        Deliberately contaminated with difficulty so that a naive correlation
        between rho and gain is inflated by the shared confound. This is the whole
        reason the partialled statistic exists; a simulator without the confound
        would let a broken test look fine.
        """
        return (
            quality * rho
            + 0.9 * (1.0 - difficulty)          # the shared-difficulty confound
            + self.rng.normal(0, 0.08)
        )
