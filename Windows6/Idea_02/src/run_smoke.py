"""Smoke entry point for Idea_02. Runs with numpy alone: no dataset, no detector.

    python src/run_smoke.py [--config ../configs/default.yaml] [--seed 0]

What this DOES check: the three split protocols have the overlap structure the
hypothesis requires, the probe and metrics run, and the H4 comparison is
computable where it exists.

What this does NOT check: anything about real smoke data. The camera signature
below was planted by `make_corpus`, so any leakage it "finds" is leakage we put
there ourselves.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np  # noqa: E402

from camsplit import (  # noqa: E402
    PLACEHOLDER_BANNER,
    camera_probe,
    empty_frame_gap,
    load_config,
    make_corpus,
    match_equal_n,
    run_protocol,
    set_seed,
    split_camera_disjoint,
    split_event_disjoint,
    split_random,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=None)
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args(argv)

    cfg = load_config(args.config)
    if args.seed is not None:
        cfg.seed = args.seed
    rng = set_seed(cfg.seed)

    print(PLACEHOLDER_BANNER)
    corpus = make_corpus(cfg, rng)
    print(
        f"synthetic corpus: {len(corpus)} frames, {corpus.n_cameras} cameras, "
        f"{corpus.n_events} events, {int(corpus.is_empty.sum())} empty frames, "
        f"camera_signature={cfg.camera_signature}"
    )

    splits = {
        "random": split_random(corpus, rng),
        "event_disjoint": split_event_disjoint(corpus, rng),
        "camera_disjoint": split_camera_disjoint(corpus, rng, cfg.test_cameras),
    }

    print("\n[STRUCTURE] the claim of H2 is that these three rows differ")
    print(f"{'protocol':<18}{'cams shared':>13}{'events shared':>15}")
    for name, split in splits.items():
        result = run_protocol(corpus, split, cfg, rng)
        print(f"{name:<18}{result.cameras_shared:>13}{result.events_shared:>15}")
    print(
        "EXPECTED structure: event_disjoint still SHARES cameras. That residual\n"
        "same-camera different-event leak is precisely what H2 says survives\n"
        "current best practice."
    )

    print("\n[H1/H2] detector performance per protocol (stand-in logistic model)")
    print(f"{'protocol':<20}{'AP':>8}{'FAR@R':>9}{'n_test':>8}{'acc 95% CI':>22}")
    for name, split in splits.items():
        matched = match_equal_n(corpus, split, rng)
        r = run_protocol(corpus, matched, cfg, rng)
        ci = f"[{r.ap_ci[0]:.3f}, {r.ap_ci[1]:.3f}]"
        print(f"{name:<20}{r.ap:>8.3f}{r.far_at_recall:>9.3f}{r.n_test:>8}{ci:>22}")
    print(
        "EXPECTED under H1: camera_disjoint AP < random AP by more than seed std.\n"
        "EXPECTED under H2: event_disjoint AP sits BETWEEN the two, not level with\n"
        "camera_disjoint. CIs resample whole events, never frames."
    )

    print("\n[H3] camera-ID probe on frozen features, evaluated EVENT-DISJOINT")
    split = splits["event_disjoint"]
    probe = camera_probe(corpus.features, corpus.camera, split.train, split.test)
    print(
        f"  accuracy {probe['accuracy']:.3f} vs chance {probe['chance']:.3f} "
        f"(margin {probe['margin']:+.3f})"
    )
    print(
        "EXPECTED under H3: accuracy above chance. A probe at chance kills H3.\n"
        "The probe MUST be evaluated event-disjoint. On a random split it can\n"
        "name the camera by recognising the fire episode instead of the tower,\n"
        "which measures event memorisation and inflates H3 for the wrong reason."
    )

    print("\n[H4] empty-frame memorisation, seen vs unseen cameras")
    gap = empty_frame_gap(corpus, splits["camera_disjoint"])
    print(
        f"  seen-camera FPR {gap['seen_fpr']:.3f} · unseen-camera FPR "
        f"{gap['unseen_fpr']:.3f} · gap {gap['gap']:+.3f}"
    )
    print(
        "Empty frames contain no plume, so a gap here cannot be plume-appearance\n"
        "domain shift. proposal.md: 'Fatal if we only report camera-disjoint drop\n"
        "without H4.' Random and event-disjoint protocols have no unseen cameras,\n"
        "so this comparison only exists under camera-disjoint."
    )

    structure_ok = (
        run_protocol(corpus, splits["event_disjoint"], cfg, rng).cameras_shared > 0
        and run_protocol(corpus, splits["camera_disjoint"], cfg, rng).cameras_shared == 0
        and run_protocol(corpus, splits["event_disjoint"], cfg, rng).events_shared == 0
    )
    print(
        f"\n[E0 GATE] split machinery usable: {'PASS' if structure_ok else 'FAIL'}\n"
        "  Rule: event_disjoint must share cameras while sharing no events, and\n"
        "  camera_disjoint must share neither. If that structure does not hold,\n"
        "  H2 is not even expressible and no real run is worth starting.\n"
        "  Nothing above is evidence about real smoke data: the camera signature\n"
        "  was planted by make_corpus()."
    )
    return 0 if structure_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
