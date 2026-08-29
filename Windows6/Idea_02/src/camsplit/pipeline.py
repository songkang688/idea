"""Wiring: run a protocol end to end, and measure the H4 empty-frame gap.

No function here returns a verdict. Thresholds live in `experiments.md` and are
applied by the caller.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .detector import TinyDetector
from .metrics import average_precision, cluster_bootstrap_ci, far_at_recall
from .splits import Split


@dataclass
class ProtocolResult:
    name: str
    ap: float
    far_at_recall: float
    ap_ci: tuple[float, float]
    n_train: int
    n_test: int
    cameras_shared: int
    events_shared: int


def run_protocol(
    corpus,
    split: Split,
    cfg,
    rng: np.random.Generator,
) -> ProtocolResult:
    """Train the stand-in detector on `split.train`, score `split.test`."""
    from .splits import camera_overlap, event_overlap

    model = TinyDetector().fit(corpus.features[split.train], corpus.labels[split.train])
    scores = model.predict_proba(corpus.features[split.test])
    labels = corpus.labels[split.test]

    per_frame_correct = ((scores > 0.5).astype(int) == labels).astype(float)
    clusters = corpus.event[split.test]
    ci = cluster_bootstrap_ci(per_frame_correct, clusters, rng, cfg.bootstrap_resamples)

    return ProtocolResult(
        name=split.name,
        ap=average_precision(scores, labels),
        far_at_recall=far_at_recall(scores, labels, cfg.target_recall),
        ap_ci=ci,
        n_train=int(split.train.size),
        n_test=int(split.test.size),
        cameras_shared=camera_overlap(corpus, split),
        events_shared=event_overlap(corpus, split),
    )


def empty_frame_gap(corpus, split: Split) -> dict[str, float]:
    """H4: do empty frames from *seen* cameras behave differently from unseen?

    Empty frames contain no plume, so a seen-vs-unseen gap here cannot be
    explained by plume-appearance domain shift. That is the whole point:
    `Idea_02/proposal.md` calls the study "Fatal if we only report
    camera-disjoint drop without H4", because without it camera identity is
    indistinguishable from geography.

    Returns nan for both rates when the split shares every camera — there are
    then no unseen cameras and the comparison does not exist. That is a real
    limitation of random and event-disjoint protocols, not a bug.

    Two protocol details that are easy to get wrong, and were got wrong first:

    1. **The detector is trained on non-empty frames only.** Every empty frame
       is therefore held out by construction, and both sides of the comparison
       are scored under identical conditions.
    2. **Empty frames are scored regardless of which side of the split they
       landed on**, partitioned only by whether their camera was seen in
       training. Restricting to the test side puts every empty frame on the
       unseen side under a camera-disjoint split, leaving nothing to compare —
       which produced a `nan` seen-camera FPR when this was first written.
    """
    train_real = split.train[~corpus.is_empty[split.train]]
    model = TinyDetector().fit(corpus.features[train_real], corpus.labels[train_real])

    train_cams = set(np.unique(corpus.camera[train_real]).tolist())
    empties = np.where(corpus.is_empty)[0]
    if empties.size == 0:
        return {"seen_fpr": float("nan"), "unseen_fpr": float("nan"), "gap": float("nan")}

    seen = np.array([i for i in empties if corpus.camera[i] in train_cams], dtype=int)
    unseen = np.array([i for i in empties if corpus.camera[i] not in train_cams], dtype=int)

    def fpr(idx: np.ndarray) -> float:
        if idx.size == 0:
            return float("nan")
        return float((model.predict_proba(corpus.features[idx]) > 0.5).mean())

    seen_fpr, unseen_fpr = fpr(seen), fpr(unseen)
    return {
        "seen_fpr": seen_fpr,
        "unseen_fpr": unseen_fpr,
        "gap": seen_fpr - unseen_fpr,
        "n_seen": float(seen.size),
        "n_unseen": float(unseen.size),
    }
