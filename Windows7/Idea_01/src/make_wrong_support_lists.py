#!/usr/bin/env python3
"""Generate and freeze the wrong-support counterfactual lists.

The output of this script is a paper artifact, not a cache. It is generated once,
committed, and never regenerated: a random seed plus a code version is not a
reproducible specification, because a NumPy or Python upgrade can silently change
which episodes were drawn. An explicit list cannot drift.

Run once per benchmark, before any inference:

    python make_wrong_support_lists.py \
        --benchmark coco_20i \
        --annotations /path/to/episodes.json \
        --out ../configs/lists/wrong_supports_coco20i.jsonl
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from support_audit.counterfactual import sample_wrong_supports, write_lists  # noqa: E402


def load_spec(path: Path) -> dict:
    """Expected schema (produced by each benchmark's episode builder):

    {
      "fold_class_ids": [...],
      "supercategory": {"<class_id>": "<name>", ...},
      "support_pool":  {"<class_id>": [["<support_image_id>", <area_frac>], ...], ...},
      "episodes": [
        {"episode_id": "...", "class_id": 3, "support_area_frac": 0.12,
         "present_class_ids": [3, 17]},
        ...
      ]
    }
    """
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--benchmark", required=True)
    ap.add_argument("--annotations", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--seed", type=int, default=20260829)
    args = ap.parse_args()

    spec = load_spec(args.annotations)
    rng = np.random.default_rng(args.seed)

    supercategory = {int(k): v for k, v in spec["supercategory"].items()}
    support_pool = {
        int(k): [(str(i), float(a)) for i, a in v] for k, v in spec["support_pool"].items()
    }
    fold_class_ids = [int(c) for c in spec["fold_class_ids"]]

    lists = []
    short = 0
    for ep in spec["episodes"]:
        cl = sample_wrong_supports(
            episode_id=ep["episode_id"],
            correct_class_id=int(ep["class_id"]),
            correct_area_frac=float(ep["support_area_frac"]),
            present_class_ids={int(c) for c in ep["present_class_ids"]},
            fold_class_ids=fold_class_ids,
            supercategory=supercategory,
            support_pool=support_pool,
            rng=rng,
        )
        if len(cl.wrong_supports) < 5:
            short += 1
        lists.append(cl)

    path = write_lists(lists, args.out)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()

    relaxed = sum(cl.n_relaxations for cl in lists)
    print(f"benchmark        : {args.benchmark}")
    print(f"episodes         : {len(lists)}")
    print(f"short draws (<5) : {short}")
    print(f"area relaxations : {relaxed}")
    print(f"written          : {path}")
    print(f"sha256           : {digest}")
    print()
    print("Record this sha256 in configs/preregistration.yaml and commit the list")
    print("BEFORE running any inference.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
