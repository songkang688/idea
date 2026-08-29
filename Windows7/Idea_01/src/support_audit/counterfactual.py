"""Wrong-support sampling.

Reviewer attack A3 (proposal.md section 21) is that wrong-class supports are not
exchangeable across queries: which classes are available as "wrong" correlates
with query content through co-occurrence structure. Two design choices answer it,
and both live here.

1. Near/far split. A wrong support from the same supercategory (cat -> dog) is a
   different intervention from one drawn across supercategories (cat -> airplane).
   We draw a fixed mix of both and report retention separately for each.
2. Fixed lists, not seeds. The drawn counterfactuals are serialised to disk and
   shipped with the paper. A seed plus a code version is not reproducible across
   library upgrades; an explicit list is.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence

import numpy as np

NEAR = "near"
FAR = "far"

# Pre-registered draw composition: K = 5 wrong supports per episode.
K_NEAR = 2
K_FAR = 3
K_TOTAL = K_NEAR + K_FAR

AREA_TOLERANCE = 0.50  # accept |area_wrong - area_corr| / area_corr <= 0.50
AREA_TOLERANCE_RELAXED = 1.00  # fallback, logged per episode


@dataclass(frozen=True)
class WrongSupport:
    support_image_id: str
    class_id: int
    kind: str  # NEAR or FAR
    area_frac: float
    relaxed: bool


@dataclass(frozen=True)
class CounterfactualList:
    """The shipped artifact: one entry per episode, frozen before inference."""

    episode_id: str
    correct_class_id: int
    correct_area_frac: float
    wrong_supports: list[WrongSupport]

    @property
    def n_relaxations(self) -> int:
        return sum(w.relaxed for w in self.wrong_supports)


def _area_ok(area: float, target: float, tol: float) -> bool:
    if target <= 0:
        return False
    return abs(area - target) / target <= tol


def sample_wrong_supports(
    *,
    episode_id: str,
    correct_class_id: int,
    correct_area_frac: float,
    present_class_ids: set[int],
    fold_class_ids: Sequence[int],
    supercategory: Mapping[int, str],
    support_pool: Mapping[int, Sequence[tuple[str, float]]],
    rng: np.random.Generator,
) -> CounterfactualList:
    """Draw K wrong-class supports for one episode.

    A candidate class is admissible only if it is (a) in this fold's class set,
    (b) not the episode's class, and (c) verified absent from the query. Condition
    (c) is what makes the intervention a counterfactual rather than a relabelling.

    support_pool maps class_id -> [(support_image_id, support_mask_area_frac)].
    """
    banned = {correct_class_id} | set(present_class_ids)
    candidates = [c for c in fold_class_ids if c not in banned and c in support_pool]

    corr_super = supercategory.get(correct_class_id)
    near_pool = [c for c in candidates if supercategory.get(c) == corr_super]
    far_pool = [c for c in candidates if supercategory.get(c) != corr_super]

    drawn: list[WrongSupport] = []
    for pool, kind, k in ((near_pool, NEAR, K_NEAR), (far_pool, FAR, K_FAR)):
        drawn.extend(
            _draw_from_pool(pool, kind, k, correct_area_frac, support_pool, rng)
        )

    # If a pool was too thin (common for rare supercategories), backfill from the
    # other pool so that K is constant across episodes. The kind label records
    # what actually happened, so the near/far analysis stays honest.
    if len(drawn) < K_TOTAL:
        leftovers = [c for c in candidates if c not in {w.class_id for w in drawn}]
        drawn.extend(
            _draw_from_pool(
                leftovers, FAR, K_TOTAL - len(drawn), correct_area_frac, support_pool, rng
            )
        )

    return CounterfactualList(
        episode_id=episode_id,
        correct_class_id=correct_class_id,
        correct_area_frac=correct_area_frac,
        wrong_supports=drawn[:K_TOTAL],
    )


def _draw_from_pool(
    pool: Sequence[int],
    kind: str,
    k: int,
    target_area: float,
    support_pool: Mapping[int, Sequence[tuple[str, float]]],
    rng: np.random.Generator,
) -> list[WrongSupport]:
    out: list[WrongSupport] = []
    if k <= 0 or not pool:
        return out
    order = rng.permutation(len(pool))
    for idx in order:
        if len(out) >= k:
            break
        cls = pool[int(idx)]
        entries = list(support_pool.get(cls, ()))
        if not entries:
            continue
        strict = [e for e in entries if _area_ok(e[1], target_area, AREA_TOLERANCE)]
        relaxed = False
        chosen_pool = strict
        if not chosen_pool:
            chosen_pool = [
                e for e in entries if _area_ok(e[1], target_area, AREA_TOLERANCE_RELAXED)
            ]
            relaxed = True
        if not chosen_pool:
            continue
        img_id, area = chosen_pool[int(rng.integers(len(chosen_pool)))]
        out.append(
            WrongSupport(
                support_image_id=img_id, class_id=cls, kind=kind, area_frac=area, relaxed=relaxed
            )
        )
    return out


def write_lists(lists: Sequence[CounterfactualList], path: str | Path) -> Path:
    """Serialise the frozen counterfactual lists. This file is a paper artifact."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for cl in lists:
            fh.write(json.dumps(asdict(cl), ensure_ascii=False) + "\n")
    return path


def read_lists(path: str | Path) -> list[CounterfactualList]:
    out = []
    with Path(path).open(encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            raw = json.loads(line)
            raw["wrong_supports"] = [WrongSupport(**w) for w in raw["wrong_supports"]]
            out.append(CounterfactualList(**raw))
    return out
