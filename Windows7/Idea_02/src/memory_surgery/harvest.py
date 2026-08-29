"""Failure-event harvesting from an IoU trace.

The protocol is fixed and applied with zero curation: every event meeting the
definition enters the corpus. Ambiguous-reappearance events are not dropped --
they are tagged into a pre-registered stratum and reported separately. That is
what answers the cherry-picking attack (A5): the reader can see exactly what was
harvested and re-derive it from the released traces.

The (IoU threshold, k) pair determines the entire corpus, so it is swept and the
corpus is released alongside the paper.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

IOU_FAIL = 0.1
IOU_HELD = 0.5
K_CONSECUTIVE = 5
RECOVERY_WINDOW = 20


@dataclass(frozen=True)
class FailureEvent:
    sequence_id: str
    object_id: int
    t_f: int  # first frame of sustained failure
    t_r: int  # ground-truth recovery-opportunity frame
    ambiguous: bool  # pre-registered stratum, reported separately
    peak_iou_before: float


def harvest(
    *,
    sequence_id: str,
    object_id: int,
    iou_trace: Sequence[float],
    visible: Sequence[bool],
    ambiguous_frames: Sequence[bool] | None = None,
    iou_fail: float = IOU_FAIL,
    iou_held: float = IOU_HELD,
    k: int = K_CONSECUTIVE,
) -> list[FailureEvent]:
    """Extract failure events from one object's IoU trace.

    A failure begins at t_f if IoU < iou_fail for k consecutive annotated frames,
    having previously been >= iou_held. t_r is the next frame where the object is
    annotated visible again -- the recovery opportunity.
    """
    iou = np.asarray(iou_trace, dtype=float)
    vis = np.asarray(visible, dtype=bool)
    amb = (
        np.asarray(ambiguous_frames, dtype=bool)
        if ambiguous_frames is not None
        else np.zeros_like(vis)
    )
    n = iou.shape[0]
    if vis.shape[0] != n:
        raise ValueError("iou_trace and visible must be the same length")

    events: list[FailureEvent] = []
    held = False
    peak = 0.0
    t = 0
    while t < n:
        if vis[t] and iou[t] >= iou_held:
            held = True
            peak = max(peak, float(iou[t]))
        if held and vis[t] and iou[t] < iou_fail:
            run = 0
            u = t
            while u < n and vis[u] and iou[u] < iou_fail:
                run += 1
                u += 1
            if run >= k:
                t_r = _next_visible(vis, u)
                if t_r is not None:
                    events.append(
                        FailureEvent(
                            sequence_id=sequence_id,
                            object_id=object_id,
                            t_f=t,
                            t_r=t_r,
                            ambiguous=bool(amb[t_r]),
                            peak_iou_before=peak,
                        )
                    )
                held = False
                peak = 0.0
                t = u
                continue
        t += 1
    return events


def _next_visible(vis: np.ndarray, start: int) -> int | None:
    for i in range(start, vis.shape[0]):
        if vis[i]:
            return i
    return None


def recovered(
    iou_trace: Sequence[float], t_r: int, *, window: int = RECOVERY_WINDOW,
    threshold: float = IOU_HELD, sustain: int = 3,
) -> bool:
    """Recovery = IoU >= threshold within `window` frames of t_r, sustained."""
    iou = np.asarray(iou_trace, dtype=float)
    end = min(t_r + window, iou.shape[0])
    run = 0
    for i in range(t_r, end):
        run = run + 1 if iou[i] >= threshold else 0
        if run >= sustain:
            return True
    return False


def reversible_fraction(
    events: Sequence[FailureEvent],
    recovered_targeted: Sequence[bool],
    recovered_no_op: Sequence[bool],
) -> float:
    """Share of a sequence's failures recovered by targeted deletion but not naturally."""
    if not events:
        return float("nan")
    gained = sum(
        1 for t, n in zip(recovered_targeted, recovered_no_op) if t and not n
    )
    return gained / len(events)
