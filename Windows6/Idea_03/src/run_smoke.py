"""Smoke entry point for Idea_03. Runs with numpy alone: no VLM, no checkpoint.

    python src/run_smoke.py [--config ../configs/default.yaml] [--seed 0]

What this DOES check: the three eval modes behave differently in the way the
argument requires, and the O1/O2/O3 decision function recovers each planted
degradation mode from the measurements alone.

What this does NOT check: anything about a real VLM. The 'base' and 'chat'
models are simulators whose failure mode is chosen by the config.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np  # noqa: E402

from aligntax import (  # noqa: E402
    PLACEHOLDER_BANNER,
    TaxMeasurements,
    chatty_generate,
    classify_outcome,
    constrained_generate,
    fit_box_probe,
    likelihood_rank,
    load_config,
    make_pair,
    mean_iou,
    parse_failure_rate,
    probe_error,
    rank_accuracy,
    set_seed,
)
from aligntax.config import TAX_MODES  # noqa: E402


def _measure(pair, cfg, rng) -> tuple[TaxMeasurements, dict[str, float]]:
    n = len(pair)
    scale = cfg.image_size
    split = int(n * 0.6)
    train_idx, test_idx = np.arange(split), np.arange(split, n)

    detail: dict[str, float] = {}
    gaps: dict[str, float] = {}

    for arm, noise, chatty, tokens in (
        ("base", pair.decode_noise_base, pair.chatty_rate_base, pair.tokens_base),
        ("chat", pair.decode_noise_chat, pair.chatty_rate_chat, pair.tokens_chat),
    ):
        freeform = [chatty_generate(b, chatty, noise, rng, scale) for b in pair.boxes]
        constrained = [constrained_generate(b, noise, rng, scale) for b in pair.boxes]
        ranked = [
            likelihood_rank(b, d, noise, rng, scale)
            for b, d in zip(pair.boxes, pair.distractors)
        ]
        weights = fit_box_probe(tokens, pair.boxes, train_idx)

        detail[f"{arm}_freeform_iou"] = mean_iou(freeform, pair.boxes)
        detail[f"{arm}_freeform_iou_parsed_only"] = mean_iou(
            freeform, pair.boxes, count_failures=False
        )
        detail[f"{arm}_parse_fail"] = parse_failure_rate(freeform)
        detail[f"{arm}_constrained_iou"] = mean_iou(constrained, pair.boxes)
        detail[f"{arm}_rank_acc"] = rank_accuracy(ranked)
        detail[f"{arm}_probe_mae"] = probe_error(weights, tokens, pair.boxes, test_idx)

    gaps["freeform"] = detail["base_freeform_iou"] - detail["chat_freeform_iou"]
    gaps["constrained"] = detail["base_constrained_iou"] - detail["chat_constrained_iou"]
    gaps["likelihood"] = detail["base_rank_acc"] - detail["chat_rank_acc"]
    gaps["probe"] = (detail["chat_probe_mae"] - detail["base_probe_mae"]) / scale

    return (
        TaxMeasurements(
            freeform_gap=gaps["freeform"],
            constrained_gap=gaps["constrained"],
            likelihood_gap=gaps["likelihood"],
            probe_gap=gaps["probe"],
        ),
        detail,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=None)
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args(argv)

    cfg = load_config(args.config)
    if args.seed is not None:
        cfg.seed = args.seed

    print(PLACEHOLDER_BANNER)
    print(
        f"config: n={cfg.n_examples} distractors={cfg.n_distractors} "
        f"planted tax_mode={cfg.tax_mode}"
    )

    rng = set_seed(cfg.seed)
    pair = make_pair(cfg, rng)
    measured, detail = _measure(pair, cfg, rng)

    print("\n[MODES] the three eval modes remove progressively more of the confound")
    print(f"{'metric':<34}{'base':>9}{'chat':>9}")
    for key, label in (
        ("freeform_iou", "free-form IoU (failures = 0)"),
        ("freeform_iou_parsed_only", "free-form IoU (parseable only)"),
        ("parse_fail", "parse failure rate"),
        ("constrained_iou", "grammar-constrained IoU"),
        ("rank_acc", "likelihood rank acc@1"),
        ("probe_mae", "probe MAE (px, lower better)"),
    ):
        print(f"{label:<34}{detail['base_' + key]:>9.3f}{detail['chat_' + key]:>9.3f}")

    print("\n[GAPS] base minus chat; positive = chat worse")
    print(f"  freeform    {measured.freeform_gap:+.3f}")
    print(f"  constrained {measured.constrained_gap:+.3f}")
    print(f"  likelihood  {measured.likelihood_gap:+.3f}   <- generation-free, decisive")
    print(f"  probe       {measured.probe_gap:+.3f}   <- representation")

    verdict = classify_outcome(measured, cfg.gap_tolerance)
    print(f"\n[VERDICT] O1/O2/O3 classification: {verdict.value}")
    print(
        "  none           = no tax\n"
        "  format   (O1)  = gap dies without generation -> write the negative\n"
        "  policy   (O2)  = likelihood gap, probe intact -> decoding-policy tax\n"
        "  representation (O3) = probe drops too -> alignment moved the features"
    )

    print("\n[E0 GATE] round trip: does the decision function recover a planted mode?")
    all_ok = True
    for mode in TAX_MODES:
        cfg.tax_mode = mode
        rng = set_seed(cfg.seed)
        recovered = classify_outcome(_measure(make_pair(cfg, rng), cfg, rng)[0], cfg.gap_tolerance)
        ok = recovered.value == mode
        all_ok &= ok
        print(f"  planted {mode:<15} -> classified {recovered.value:<15} {'ok' if ok else 'MISMATCH'}")

    print(
        f"\n  harness usable: {'PASS' if all_ok else 'FAIL'}\n"
        "  This checks only that the O1/O2/O3 logic is sound on data whose answer\n"
        "  we already knew. It says nothing about any real VLM: Windows6 has run\n"
        "  no VLM eval, and GATE-B (a verified base/chat pair sharing vision\n"
        "  encoder and coordinate tokenization) is still open."
    )
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
