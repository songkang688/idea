"""The teleport probe: run trials, score the trichotomy, aggregate cells.

Per-trial outcome at the manipulation frame (exp_07 'scoring' module):

  - ``follow_object``  tracker selected the true target at its new location
  - ``follow_place``   tracker selected whatever occupies the target's
                       pre-manipulation location (distractor in swap,
                       background phantom in jump)
  - ``lost``           nothing cleared the acceptance threshold
  - ``other``          some other candidate

Identity-continuation readouts over the post-manipulation frames (the
hypothesized failure — the memory keeps confirming the wrong identity):

  - ``wrong_persisted``  wrong at the manipulation frame AND still on a
                         non-target identity at the final frame
  - ``recovered``        wrong at the manipulation frame but back on the
                         target at the final frame
  - ``template_affinity_gap``  cos(memory template, distractor appearance) -
                         cos(memory template, target appearance) at the final
                         frame. Positive = the memory now ENCODES the
                         distractor's identity (representation-level evidence
                         of pollution, not just behavioral).
"""

from __future__ import annotations

import zlib
from dataclasses import dataclass
from typing import Callable, Dict, Optional

import numpy as np

from .metrics import rate_with_ci
from .world import DISTRACTOR, TARGET, Trial, WorldParams, generate_trial

OUTCOMES = ("follow_object", "follow_place", "other", "lost")


@dataclass
class TrialResult:
    outcome: str
    final_ident: Optional[str]
    wrong_persisted: bool
    recovered: bool
    template_affinity_gap: Optional[float]


def stable_seed(*parts) -> int:
    """Deterministic seed from heterogeneous cell coordinates (hash() is
    process-salted, so crc32 of the repr keeps runs reproducible)."""
    return zlib.crc32("|".join(repr(p) for p in parts).encode())


def run_trial(trial: Trial, tracker) -> TrialResult:
    frames = trial.frames
    target0 = next(c for c in frames[0].candidates if c.ident == TARGET)
    tracker.prompt(target0)

    prev_time = frames[0].time
    selected: Optional[str] = None
    outcome: Optional[str] = None
    for i, frame in enumerate(frames[1:], start=1):
        selected = tracker.step(frame.candidates, dt=frame.time - prev_time)
        prev_time = frame.time
        if i == trial.manipulation_idx:
            if selected is None:
                outcome = "lost"
            elif selected == TARGET:
                outcome = "follow_object"
            elif trial.place_ident is not None and selected == trial.place_ident:
                outcome = "follow_place"
            else:
                outcome = "other"
    assert outcome is not None, "trial must contain a manipulation frame"

    wrong_at_manip = outcome in ("follow_place", "other")
    final_ident = selected
    wrong_persisted = wrong_at_manip and final_ident is not None and final_ident != TARGET
    recovered = wrong_at_manip and final_ident == TARGET

    gap = None
    if getattr(tracker, "memory", None):
        tpl = tracker.template()
        last = trial.frames[-1]
        t_app = next(c.app for c in last.candidates if c.ident == TARGET)
        d_app = next(c.app for c in last.candidates if c.ident == DISTRACTOR)
        gap = float(tpl.dot(d_app) - tpl.dot(t_app))

    return TrialResult(outcome, final_ident, wrong_persisted, recovered, gap)


def run_cell(
    condition: str,
    displacement: float,
    gap: int,
    similarity: float,
    n_trials: int,
    tracker_factory: Callable[[np.random.Generator], object],
    world: WorldParams,
    base_seed: int,
) -> Dict:
    """Run one (condition, d, g, s) cell; return outcome rates with Wilson CIs
    plus identity-continuation statistics."""
    counts = {o: 0 for o in OUTCOMES}
    n_wrong = n_persist = n_recover = 0
    affinity_gaps = []
    for t in range(n_trials):
        rng = np.random.default_rng(
            stable_seed(base_seed, condition, displacement, gap, similarity, t)
        )
        trial = generate_trial(condition, displacement, gap, similarity, rng, world)
        tracker = tracker_factory(rng)
        res = run_trial(trial, tracker)
        counts[res.outcome] += 1
        if res.outcome in ("follow_place", "other"):
            n_wrong += 1
            n_persist += int(res.wrong_persisted)
            n_recover += int(res.recovered)
        if res.template_affinity_gap is not None:
            affinity_gaps.append(res.template_affinity_gap)

    out = {
        "condition": condition,
        "displacement": displacement,
        "gap": gap,
        "similarity": similarity,
        "n_trials": n_trials,
        "rates": {o: rate_with_ci(counts[o], n_trials) for o in OUTCOMES},
        "wrong_at_manipulation": rate_with_ci(n_wrong, n_trials),
        "wrong_persisted_given_wrong": rate_with_ci(n_persist, n_wrong)
        if n_wrong
        else None,
        "recovered_given_wrong": rate_with_ci(n_recover, n_wrong) if n_wrong else None,
    }
    if affinity_gaps:
        arr = np.asarray(affinity_gaps)
        out["template_affinity_gap"] = {
            "mean": float(arr.mean()),
            "std": float(arr.std(ddof=1)) if len(arr) > 1 else 0.0,
        }
    return out
