#!/usr/bin/env python3
"""Run the SupportAudit harness end to end on synthetic episodes.

This is not the MVE of proposal.md section 17 -- that one needs real checkpoints.
This is the harness validation that must pass before those checkpoints are worth
downloading: it exercises strata assignment, frozen counterfactual lists, both
floors, the bootstrap, and the pre-registered killer decision rule.

The positive control is the point. `MockSegmenter(support_reliance=0.0)` ignores
its support completely, so the audit must report retention near 1.0 for it and
markedly lower retention for the support-reliant mock. If it does not, the
harness is broken and no real number from it would mean anything.

    python run_mve.py --episodes 120 --seed 0
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from support_audit import (  # noqa: E402
    AuditConfig,
    CentralLargestMaskFloor,
    Episode,
    Instance,
    SaliencyThresholdFloor,
    kendall_tau,
    positions_changed,
    run_audit,
    sample_wrong_supports,
)
from support_audit.adapters import MockSegmenter  # noqa: E402
from support_audit.floors import center_prior_saliency  # noqa: E402

H = W = 64
N_CLASSES = 12
SUPERCATEGORY = {c: f"super_{c // 4}" for c in range(N_CLASSES)}


def _blob(rng: np.random.Generator, *, central: bool) -> np.ndarray:
    yy, xx = np.mgrid[0:H, 0:W]
    if central:
        cy, cx = H / 2 + rng.normal(0, 2), W / 2 + rng.normal(0, 2)
        rad = rng.uniform(10, 16)
    else:
        cy, cx = rng.uniform(6, H - 6), rng.uniform(6, W - 6)
        rad = rng.uniform(5, 9)
    return ((yy - cy) ** 2 + (xx - cx) ** 2) < rad**2


def class_palette(seed: int) -> np.ndarray:
    """One well-separated RGB prototype per class.

    Scalar brightness codes are a bad fixture here: with classes on a line, a
    wrong-class support is often still closest to the correct object, so a
    support-driven mock keeps hitting the target and the control collapses.
    Independent RGB prototypes remove that accident.
    """
    rng = np.random.default_rng(seed)
    return np.clip(rng.uniform(0.45, 0.95, size=(N_CLASSES, 3)), 0, 1)


def build_world(n_episodes: int, seed: int):
    """Synthetic benchmark with a controllable distractor rate."""
    rng = np.random.default_rng(seed)
    palette = class_palette(seed + 99)
    images: dict[str, np.ndarray] = {}
    masks: dict[tuple[str, int], np.ndarray] = {}
    episodes: list[Episode] = []
    support_pool: dict[int, list[tuple[str, float]]] = {c: [] for c in range(N_CLASSES)}

    def paint(img, mask, cls):
        img[mask] = np.clip(palette[cls] + rng.normal(0, 0.02, size=(mask.sum(), 3)), 0, 1)

    for c in range(N_CLASSES):
        for k in range(4):
            sid = f"sup_{c}_{k}"
            m = _blob(rng, central=True)
            img = rng.uniform(0, 0.25, size=(H, W, 3))
            paint(img, m, c)
            images[sid] = img
            masks[(sid, c)] = m
            support_pool[c].append((sid, float(m.mean())))

    for i in range(n_episodes):
        c = int(rng.integers(N_CLASSES))
        qid = f"qry_{i}"
        target = _blob(rng, central=True)
        img = rng.uniform(0, 0.25, size=(H, W, 3))
        paint(img, target, c)

        instances = [Instance(class_id=c, mask=target)]
        # ~55% of queries get a distractor of a different class -> S3 stratum.
        if rng.random() < 0.55:
            dc = int((c + 1 + rng.integers(N_CLASSES - 1)) % N_CLASSES)
            dm = _blob(rng, central=False) & ~target
            if dm.any():
                paint(img, dm, dc)
                instances.append(Instance(class_id=dc, mask=dm))

        images[qid] = img
        sid, _ = support_pool[c][int(rng.integers(len(support_pool[c])))]
        episodes.append(
            Episode(
                episode_id=f"ep_{i}",
                benchmark="synthetic",
                fold=0,
                class_id=c,
                support_image_id=sid,
                support_mask=masks[(sid, c)],
                query_image_id=qid,
                query_gt=target,
                query_instances=instances,
            )
        )
    return images, masks, episodes, support_pool


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--episodes", type=int, default=120)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--tau", type=float, default=0.2)
    args = ap.parse_args()

    images, masks, episodes, support_pool = build_world(args.episodes, args.seed)
    rng = np.random.default_rng(args.seed + 1)

    counterfactuals = {}
    for ep in episodes:
        counterfactuals[ep.episode_id] = sample_wrong_supports(
            episode_id=ep.episode_id,
            correct_class_id=ep.class_id,
            correct_area_frac=ep.support_mask_area_frac,
            present_class_ids=ep.present_class_ids(),
            fold_class_ids=list(range(N_CLASSES)),
            supercategory=SUPERCATEGORY,
            support_pool=support_pool,
            rng=rng,
        )

    def propose(query_image):
        gray = query_image.mean(axis=2)
        return [gray > np.quantile(gray, q) for q in (0.70, 0.80, 0.90)]

    methods = [
        MockSegmenter("mock_support_blind", support_reliance=0.0, seed=1),
        MockSegmenter("mock_partial", support_reliance=0.5, seed=2),
        MockSegmenter("mock_support_driven", support_reliance=1.0, seed=3),
    ]

    report = run_audit(
        methods=methods,
        episodes=episodes,
        counterfactuals=counterfactuals,
        floor_strong=CentralLargestMaskFloor(propose),
        floor_weak=SaliencyThresholdFloor(center_prior_saliency),
        load_image=lambda i: images[i],
        load_support_mask=lambda i, c: masks[(i, c)],
        config=AuditConfig(
            tau=args.tau,
            seed=args.seed,
            specialist_methods={"mock_support_blind", "mock_partial"},
        ),
    )

    print("stratum counts:", report.stratum_counts)
    print()
    hdr = (
        f"{'method':<22}{'stratum':<26}{'n':>4}{'retention (ratio of means)':>28}"
        f"{'med':>7}{'SSS':>7}"
    )
    print(hdr)
    print("-" * len(hdr))
    for r in sorted(report.results, key=lambda r: (r.method, r.stratum)):
        ci = f"{r.retention.point:.3f} [{r.retention.lo:.3f},{r.retention.hi:.3f}]"
        flag = " *" if r.estimators_disagree else ""
        print(
            f"{r.method:<22}{r.stratum:<26}{r.n_episodes:>4}{ci:>28}"
            f"{r.retention_median.point:>7.3f}{r.sss:>7.3f}{flag}"
        )
    print("  * primary and median estimators disagree by >0.2 (bimodal episodes)")

    print()
    verdict = report.killer_verdict()
    print("killer decision rule on S3:", verdict.detail)
    print("headline survives:", verdict.headline_survives)

    published = report.leaderboard("synthetic", "S3_distractor_present", key="acc")
    adjusted = report.leaderboard("synthetic", "S3_distractor_present", key="sss")
    print()
    print("accuracy order  :", published)
    print("sensitivity order:", adjusted)
    print(f"kendall tau = {kendall_tau(published, adjusted):.3f}, "
          f"positions changed = {positions_changed(published, adjusted)}")
    print()
    print("NOTE: every number above comes from MockSegmenter fixtures. It validates the")
    print("harness only and is not an experimental result about any published method.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
