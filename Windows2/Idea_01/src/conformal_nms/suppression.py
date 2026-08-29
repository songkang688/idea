"""Coverage-preserving suppression (CPS) — the constructive method sketch.

Idea (module 4 of exp_05): suppress duplicates *inside* the conformal
prediction set, and only ever let a box be removed in favour of a kept box
that is a genuine near-duplicate (IoU >= kappa, with kappa high). Combined
with a slightly stricter covering threshold at calibration time, this makes
the conformal coverage guarantee survive suppression *provably*, not just
empirically.

The lemma doing the work
------------------------
The Jaccard / Marczewski–Steinhaus distance d(A, B) = 1 - IoU(A, B) is a
metric on measurable sets (triangle inequality: Kosub 2019, "A note on the
triangle inequality for the Jaccard distance", arXiv:1612.02696). Hence for
boxes a (kept), b (suppressed), g (ground truth):

    1 - IoU(a, g) <= (1 - IoU(a, b)) + (1 - IoU(b, g))
    IoU(a, g)     >= IoU(a, b) + IoU(b, g) - 1.

So if b covers g at IoU >= tau_cal and b was suppressed only by a kept a with
IoU(a, b) >= kappa, then a covers g at IoU >= kappa + tau_cal - 1.

Corollary (the CPS recipe): calibrate the conformal layer at the stricter
covering threshold

    tau_cal = tau + (1 - kappa),

then greedily suppress within the prediction set at merge threshold kappa.
Every GT covered at tau_cal by the pre-suppression set stays covered at tau
by the post-suppression set — deterministically, per scene. Therefore the
marginal 1 - alpha split-conformal guarantee (established at tau_cal on the
full candidate pool) transfers to the *suppressed* output at tau.

Trade-off surface: larger kappa -> weaker suppression (bigger sets) but a
smaller calibration penalty (tau_cal closer to tau); this is the tunable
redundancy/set-size frontier the full paper would map. ``redundancy`` keeps
the top-r members per cluster (r = 1 is maximal suppression).

Greedy suppression here only ever assigns a box to the cluster of a *kept*
representative (no chaining through suppressed boxes), which is exactly what
the lemma needs.
"""

from __future__ import annotations

import numpy as np

from .boxes import iou_matrix


def required_calibration_iou(tau: float, kappa: float) -> float:
    """The covering threshold to calibrate at so post-CPS coverage holds at tau."""
    tau_cal = tau + (1.0 - kappa)
    if not (0.0 < tau_cal < 1.0):
        raise ValueError(
            f"tau_cal = tau + (1 - kappa) = {tau_cal:.3f} not in (0, 1); "
            "increase kappa or decrease tau"
        )
    return tau_cal


def coverage_preserving_suppression(
    boxes: np.ndarray,
    scores: np.ndarray,
    set_mask: np.ndarray,
    kappa: float,
    redundancy: int = 1,
) -> np.ndarray:
    """Suppress near-duplicates inside the conformal prediction set.

    Parameters
    ----------
    boxes, scores : full candidate arrays for the scene.
    set_mask : boolean mask of prediction-set membership (from conformal layer).
    kappa : merge threshold; a box may only be suppressed by a kept cluster
        representative with IoU >= kappa.
    redundancy : keep the top-``redundancy`` scoring members of each cluster.

    Returns indices (into the full candidate arrays) of the kept boxes,
    sorted by descending score. Guarantees: kept is a subset of the set,
    >= 1 member per spatial cluster survives, and every suppressed member has
    IoU >= kappa with its (kept) cluster representative.
    """
    if redundancy < 1:
        raise ValueError("redundancy must be >= 1")
    boxes = np.asarray(boxes, dtype=np.float64).reshape(-1, 4)
    scores = np.asarray(scores, dtype=np.float64).ravel()
    members = np.flatnonzero(np.asarray(set_mask, dtype=bool))
    if members.size == 0:
        return np.empty(0, dtype=np.int64)

    order = members[np.argsort(-scores[members], kind="stable")]
    ious = iou_matrix(boxes[order], boxes[order])

    rep_rows: list[int] = []      # local row index of each cluster representative
    cluster_kept: list[int] = []  # how many members kept per cluster
    kept_local: list[int] = []

    for i in range(order.size):
        assigned = None
        for c, rep in enumerate(rep_rows):
            if ious[rep, i] >= kappa:
                assigned = c
                break
        if assigned is None:
            rep_rows.append(i)
            cluster_kept.append(1)
            kept_local.append(i)
        elif cluster_kept[assigned] < redundancy:
            cluster_kept[assigned] += 1
            kept_local.append(i)
        # else: suppressed — by construction IoU(rep, i) >= kappa and rep is kept.

    return order[np.asarray(kept_local, dtype=np.int64)]
