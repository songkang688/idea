"""The three split protocols, and the overlap accounting that distinguishes them.

The scientific content of Idea_02 lives in this file. H2 is the claim that
*event-disjoint is not camera-disjoint* — so the code must make the difference
checkable, not just nameable. `camera_overlap` and `event_overlap` exist for
exactly that, and the self-checks assert:

    random          : cameras shared, events shared
    event_disjoint  : cameras SHARED, events disjoint   <-- the residual leak
    camera_disjoint : cameras disjoint, events disjoint

If `event_disjoint` ever came out camera-disjoint on real data, H2 would be
unfalsifiable on that dataset and the pivot in experiments.md fires.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class Split:
    """Train/test index sets plus the protocol name that produced them."""

    name: str
    train: np.ndarray
    test: np.ndarray

    def __post_init__(self) -> None:
        if np.intersect1d(self.train, self.test).size:
            raise ValueError(f"{self.name}: train and test indices overlap")


def camera_overlap(corpus, split: Split) -> int:
    """How many cameras appear on both sides. 0 means camera-disjoint."""
    return int(
        np.intersect1d(corpus.camera[split.train], corpus.camera[split.test]).size
    )


def event_overlap(corpus, split: Split) -> int:
    """How many real events appear on both sides. Empty frames (event -1) excluded."""
    tr = corpus.event[split.train]
    te = corpus.event[split.test]
    return int(np.intersect1d(tr[tr >= 0], te[te >= 0]).size)


def split_random(corpus, rng: np.random.Generator, frac: float = 0.3) -> Split:
    """Shuffle frames. Breaks nothing: same camera and same event on both sides."""
    idx = rng.permutation(len(corpus))
    cut = int(len(idx) * frac)
    return Split("random", idx[cut:], idx[:cut])


def split_event_disjoint(corpus, rng: np.random.Generator, frac: float = 0.3) -> Split:
    """Hold out whole events. Cameras are still shared — that is the point.

    This is the current best practice (PYRONEAR-style). H2 asserts it leaves a
    residual same-camera different-event leak, so the protocol must NOT
    accidentally become camera-disjoint. Empty frames follow their camera's
    majority side so the negatives stay usable for H4.
    """
    events = np.unique(corpus.event[corpus.event >= 0])
    shuffled = rng.permutation(events)
    n_test = max(int(len(shuffled) * frac), 1)
    test_events = set(shuffled[:n_test].tolist())

    is_test = np.array([e in test_events for e in corpus.event])
    for cam in np.unique(corpus.camera):
        empty_here = (corpus.camera == cam) & corpus.is_empty
        real_here = (corpus.camera == cam) & ~corpus.is_empty
        if real_here.any():
            is_test[empty_here] = bool(is_test[real_here].mean() > 0.5)

    return Split("event_disjoint", np.where(~is_test)[0], np.where(is_test)[0])


def split_camera_disjoint(corpus, rng: np.random.Generator, n_test_cameras: int = 3) -> Split:
    """Hold out whole cameras. Breaks both groupings."""
    cams = rng.permutation(np.unique(corpus.camera))
    if n_test_cameras >= len(cams):
        raise ValueError(
            f"cannot hold out {n_test_cameras} of {len(cams)} cameras and keep a train set"
        )
    test_cams = set(cams[:n_test_cameras].tolist())
    is_test = np.array([c in test_cams for c in corpus.camera])
    return Split("camera_disjoint", np.where(~is_test)[0], np.where(is_test)[0])


def match_equal_n(
    corpus, split: Split, rng: np.random.Generator, tolerance: float = 0.02
) -> Split:
    """Subsample the test side to equal N and a matched positive ratio.

    Without this, camera-disjoint test sets differ from random ones in size and
    class balance, and any AP gap is partly an artifact of the comparison rather
    than of leakage. Reviewer #2 asked for equal-N, class-ratio-matched splits;
    this is that requirement in code.
    """
    target_ratio = float(corpus.labels[split.train].mean())
    test = split.test
    pos = test[corpus.labels[test] == 1]
    neg = test[corpus.labels[test] == 0]
    if len(pos) == 0 or len(neg) == 0:
        return split

    n_pos = min(len(pos), int(round(len(test) * target_ratio)))
    n_neg = min(len(neg), len(test) - n_pos)
    n_pos = min(n_pos, len(pos))
    if n_pos + n_neg == 0:
        return split

    chosen = np.concatenate(
        [rng.choice(pos, n_pos, replace=False), rng.choice(neg, n_neg, replace=False)]
    )
    achieved = float(corpus.labels[chosen].mean())
    if abs(achieved - target_ratio) > tolerance:
        # Report rather than silently ship a mismatched comparison.
        raise RuntimeError(
            f"{split.name}: could not match positive ratio "
            f"(target {target_ratio:.3f}, achieved {achieved:.3f}); "
            "the test side lacks the classes needed for a fair comparison"
        )
    return Split(f"{split.name}+equalN", split.train, np.sort(chosen))
