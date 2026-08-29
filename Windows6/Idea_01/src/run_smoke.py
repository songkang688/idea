"""Smoke entry point for Idea_01. Runs with numpy alone: no weights, no data.

    python src/run_smoke.py [--config ../configs/default.yaml] [--seed 0]

What this DOES check: the metrics behave, both counterfactual arms pass their
own validity checks, and the H1/H2 comparison runs end to end.

What this does NOT check: anything at all about SAM. See the banner it prints.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from amgclust import (  # noqa: E402
    PLACEHOLDER_BANNER,
    agreement_profile,
    counterfactual_profile,
    load_config,
    set_seed,
    synthetic_ct,
)
from amgclust.data import apply_window  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=None, help="YAML config; defaults are used if omitted")
    parser.add_argument("--seed", type=int, default=None, help="override config seed")
    args = parser.parse_args(argv)

    cfg = load_config(args.config)
    if args.seed is not None:
        cfg.seed = args.seed
    rng = set_seed(cfg.seed)

    print(PLACEHOLDER_BANNER)
    print(f"config: window={cfg.window} k_means={cfg.k_means} seed={cfg.seed}")

    hu = synthetic_ct(rng=rng)
    img = apply_window(hu, cfg.window)

    print("\n[H1] AMG-mock agreement with each baseline (higher = more alike)")
    print(f"{'baseline':<18}{'hung.IoU':>10}{'ARI':>10}{'boundaryF':>12}{'coverage':>10}{'|A|/|B|':>10}")
    profile = agreement_profile(img, cfg, rng)
    for name, iou, ari, bf, cov, card in profile.as_rows():
        print(f"{name:<18}{iou:>10.3f}{ari:>10.3f}{bf:>12.3f}{cov:>10.3f}{card:>10.2f}")

    print("\nEXPECTED under H1: best intensity baseline > slic_lite, on all three")
    print("pre-registered metrics. Reporting all three because agreeing with only")
    print("the flattering one is the metric-shopping attack (reviewer_attacks.md A4).")
    for metric_name, table in (
        ("hungarian_iou", profile.hungarian_iou),
        ("ari", profile.ari),
        ("boundary_f", profile.boundary_f),
    ):
        intensity_like = max(v for k, v in table.items() if not k.startswith("slic"))
        spatial_like = table["slic_lite"]
        flag = "consistent" if intensity_like > spatial_like else "INCONSISTENT"
        print(f"  {metric_name:<15}{intensity_like:>8.3f} vs slic {spatial_like:>8.3f}  -> {flag}")

    h1_ok = all(
        max(v for k, v in table.items() if not k.startswith("slic")) > table["slic_lite"]
        for table in (profile.hungarian_iou, profile.ari, profile.boundary_f)
    )

    print("\n[H2] Counterfactual arms (self-agreement; lower = intervention moved AMG more)")
    cf = counterfactual_profile(img, cfg, rng)
    for name, value in cf.items():
        print(f"  {name:<38}{value:>8.3f}")
    print(
        "EXPECTED *for real SAM* if the mechanism is intensity:\n"
        "  self_agreement_intensity_remap < self_agreement_texture_shuffle\n"
        "This mock is NOT expected to reproduce that direction and its result here\n"
        "must not be read as evidence either way. Connected components are highly\n"
        "sensitive to per-pixel noise, so the texture arm fragments them for a\n"
        "reason that has nothing to do with objectness. The only thing card E0\n"
        "checks about H2 is that both arms run and pass their validity checks."
    )

    print(
        f"\n[E0 GATE] harness usable: {'PASS' if h1_ok else 'FAIL'}\n"
        "  Rule (Idea_01/experiments.md E0): if the AMG stand-in does not beat the\n"
        "  spatial baseline on synthetic piecewise-constant input, the implementation\n"
        "  is wrong and must be fixed before touching real SAM. This gate can only\n"
        "  fail the harness; it can never confirm the science.\n"
        "  The 'AMG' above is multi-threshold connected components, not SAM."
    )
    return 0 if h1_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
