#!/usr/bin/env python3
"""A-0028 synthetic teleport-probe runner (CPU-only, no SAM2, no weights).

Runs four experiments on a surrogate memory-bank tracker and writes
results.json + report.md. Every number produced is labeled
MEASURED (synthetic surrogate); no SAM2 behavior is measured or implied.

  E1  arbitration curves    P(follow-place) over the (d, g, s) grid for the
                            surrogate at its configured lambda, bracketed by
                            the pure-location and pure-appearance dummies
  E2  instrument validation lambda sweep: the probe's location-prior index
                            must recover the surrogate's known arbitration
                            (the dissociation probe is the claim — this is
                            the check that the instrument measures it)
  E3  identity continuation memory-pollution readouts after a wrong pick
                            (persistence, recovery, template rebinding),
                            with a frozen-memory ablation
  E4  Reviewer-2 controls   paste-artifact placebo (no move) and
                            appearance-flip condition

Usage:
    python run_synthetic.py --config configs/default.yaml --out results/
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from a0028.config import load_config  # noqa: E402
from a0028.metrics import location_prior_index, spearman_rho  # noqa: E402
from a0028.probe import run_cell  # noqa: E402
from a0028.tracker import (  # noqa: E402
    MemoryBankTracker,
    appearance_matcher_tracker,
    location_prior_tracker,
)
from a0028.sam2_wrapper import ENV_FLAG, real_sam2_enabled  # noqa: E402

MEASURED = "MEASURED (synthetic surrogate)"


def surrogate_factory(tracker_cfg: dict, lambda_loc: float | None = None, **overrides):
    cfg = dict(tracker_cfg)
    if lambda_loc is not None:
        cfg["lambda_loc"] = lambda_loc
    cfg.update(overrides)

    def factory(rng: np.random.Generator) -> MemoryBankTracker:
        return MemoryBankTracker(rng=rng, **cfg)

    return factory


def iter_grid(grid: dict):
    for d in grid["displacements"]:
        for g in grid["gaps"]:
            for s in grid["similarities"]:
                yield d, g, s


def exp1_arbitration(cfg: dict) -> dict:
    grid, world, seed = cfg["grid"], cfg["world_params"], cfg["seed"]
    exps = cfg["experiments"]
    out = {"label": MEASURED, "cells": [], "baseline_cells": []}
    for condition in exps["arbitration_conditions"]:
        for d, g, s in iter_grid(grid):
            out["cells"].append(
                run_cell(
                    condition, d, g, s, grid["trials_per_cell"],
                    surrogate_factory(cfg["tracker"]), world, seed,
                )
            )
    baselines = {
        "location_prior_dummy": lambda rng: location_prior_tracker(rng),
        "appearance_matcher_dummy": lambda rng: appearance_matcher_tracker(rng),
    }
    for name, factory in baselines.items():
        for d, g, s in iter_grid(grid):
            cell = run_cell(
                "swap", d, g, s, exps["baseline_trials_per_cell"],
                factory, world, seed + 1,
            )
            cell["tracker"] = name
            out["baseline_cells"].append(cell)
    return out


def exp2_instrument_validation(cfg: dict) -> dict:
    exps, world, seed = cfg["experiments"], cfg["world_params"], cfg["seed"]
    sub = exps["lambda_sweep_subgrid"]
    lambdas = exps["lambda_sweep"]
    indices = []
    per_lambda = []
    for lam in lambdas:
        rates = []
        for d, g, s in iter_grid(sub):
            cell = run_cell(
                "swap", d, g, s, exps["lambda_sweep_trials"],
                surrogate_factory(cfg["tracker"], lambda_loc=lam), world, seed + 2,
            )
            rates.append(cell["rates"]["follow_place"]["rate"])
        idx = location_prior_index(rates)
        indices.append(idx)
        per_lambda.append({"lambda_loc": lam, "location_prior_index": idx})
    rho = spearman_rho(lambdas, indices)
    return {
        "label": MEASURED,
        "claim": "probe recovers the surrogate's known arbitration parameter",
        "per_lambda": per_lambda,
        "spearman_rho_lambda_vs_index": rho,
        "monotone_recovery": bool(rho > 0.99),
    }


def exp3_identity_continuation(cfg: dict) -> dict:
    exps, world, seed = cfg["experiments"], cfg["world_params"], cfg["seed"]
    p = exps["persistence"]
    cell_spec = p["cell"]
    rows = []
    for lam in p["lambdas"]:
        for update_memory in (True, False):
            cell = run_cell(
                "swap",
                cell_spec["displacement"], cell_spec["gap"], cell_spec["similarity"],
                p["trials"],
                surrogate_factory(cfg["tracker"], lambda_loc=lam, update_memory=update_memory),
                world, seed + 3,
            )
            rows.append(
                {
                    "lambda_loc": lam,
                    "memory_update": update_memory,
                    "wrong_at_manipulation": cell["wrong_at_manipulation"],
                    "wrong_persisted_given_wrong": cell["wrong_persisted_given_wrong"],
                    "recovered_given_wrong": cell["recovered_given_wrong"],
                    "template_affinity_gap": cell.get("template_affinity_gap"),
                }
            )
    return {
        "label": MEASURED,
        "cell": cell_spec,
        "readout": "does the memory continue the wrong identity after a wrong pick?",
        "rows": rows,
    }


def exp4_controls(cfg: dict) -> dict:
    exps, world, seed = cfg["experiments"], cfg["world_params"], cfg["seed"]
    tracker_factory = surrogate_factory(cfg["tracker"])
    # displacement doubles as the target-distractor separation; nothing moves
    # in these conditions, so 32 px just keeps the distractor non-degenerate
    placebo = run_cell(
        "placebo", 32.0, 4, 0.8, exps["placebo_trials"], tracker_factory, world, seed + 4
    )
    flip = run_cell(
        "appearance_flip", 32.0, 4, 0.8, exps["appearance_flip_trials"],
        tracker_factory, world, seed + 4,
    )
    disruption = 1.0 - placebo["rates"]["follow_object"]["rate"]
    return {
        "label": MEASURED,
        "reviewer2_note": (
            "placebo = paste-artifact-only, nothing moves; if trackers were "
            "disrupted here the probe would measure compositing artifacts, "
            "not appearance-vs-location arbitration"
        ),
        "placebo": placebo,
        "placebo_disruption_rate": disruption,
        "appearance_flip": flip,
    }


# --- report rendering -------------------------------------------------------

def _fmt_rate(r: dict | None) -> str:
    if r is None:
        return "n/a"
    return f"{r['rate']:.3f} [{r['ci_lo']:.3f}, {r['ci_hi']:.3f}]"


def marginal(cells, axis: str, condition: str):
    """Mean P(follow-place) marginalized over the other two grid axes."""
    from collections import defaultdict

    acc = defaultdict(list)
    for c in cells:
        if c["condition"] != condition:
            continue
        acc[c[axis]].append(c["rates"]["follow_place"]["rate"])
    return {k: sum(v) / len(v) for k, v in sorted(acc.items())}


def render_report(cfg_path: str, results: dict, elapsed: float) -> str:
    e1, e2, e3, e4 = (
        results["exp1_arbitration"],
        results["exp2_instrument_validation"],
        results["exp3_identity_continuation"],
        results["exp4_controls"],
    )
    lines = [
        "# A-0028 synthetic teleport-probe report",
        "",
        f"Config: `{cfg_path}` — runtime {elapsed:.1f}s, CPU only, no SAM2, no weights.",
        "",
        "**Every number below is MEASURED on the synthetic surrogate memory tracker**",
        "(a SAM2-*style* memory bank with a known arbitration parameter lambda_loc).",
        "**No SAM2 behavior is measured here.** SAM2/SAM3 predictions remain",
        "EXPECTED (hypothesis) — see README and `Windows2/_wip/stage5_agent_N/exp_07.md`.",
        "",
        "## E1 — arbitration curves (swap condition, surrogate lambda_loc="
        + str(results["config"]["tracker"]["lambda_loc"])
        + ")",
        "",
        "P(follow-place), marginal over the other two axes:",
        "",
    ]
    for axis, label in (
        ("displacement", "displacement d (px)"),
        ("gap", "temporal gap g (world steps)"),
        ("similarity", "distractor similarity s (cosine)"),
    ):
        m = marginal(e1["cells"], axis, "swap")
        lines.append(f"| {label} | " + " | ".join(str(k) for k in m) + " |")
        lines.append("|" + "---|" * (len(m) + 1))
        lines.append(
            "| P(follow-place) | " + " | ".join(f"{v:.3f}" for v in m.values()) + " |"
        )
        lines.append("")
    lines += [
        "Dummy brackets on the same swap grid (mean P(follow-place) over all cells):",
        "",
    ]
    for name in ("location_prior_dummy", "appearance_matcher_dummy"):
        vals = [
            c["rates"]["follow_place"]["rate"]
            for c in e1["baseline_cells"]
            if c["tracker"] == name
        ]
        lines.append(f"- `{name}`: {sum(vals)/len(vals):.3f}")
    lines += [
        "",
        "## E2 — instrument validation (the probe is the claim)",
        "",
        "| true lambda_loc | probe location-prior index |",
        "|---|---|",
    ]
    for row in e2["per_lambda"]:
        lines.append(f"| {row['lambda_loc']} | {row['location_prior_index']:.3f} |")
    lines += [
        "",
        f"Spearman rho(lambda, index) = **{e2['spearman_rho_lambda_vs_index']:.3f}** "
        f"(monotone recovery: {e2['monotone_recovery']}).",
        "",
        "## E3 — identity continuation (memory pollution) at cell "
        + str(e3["cell"]),
        "",
        "| lambda_loc | memory update | P(wrong at manip) | P(persist given wrong) | P(recover given wrong) | template affinity gap (mean) |",
        "|---|---|---|---|---|---|",
    ]
    for r in e3["rows"]:
        gap = r["template_affinity_gap"]
        gap_s = f"{gap['mean']:+.3f}" if gap else "n/a"
        lines.append(
            f"| {r['lambda_loc']} | {'on' if r['memory_update'] else 'frozen'} "
            f"| {_fmt_rate(r['wrong_at_manipulation'])} "
            f"| {_fmt_rate(r['wrong_persisted_given_wrong'])} "
            f"| {_fmt_rate(r['recovered_given_wrong'])} | {gap_s} |"
        )
    lines += [
        "",
        "Positive template affinity gap = the memory bank now encodes the",
        "distractor's appearance (representation-level identity continuation).",
        "",
        "## E4 — Reviewer-2 controls",
        "",
        f"- Placebo (paste-artifact only, nothing moves): disruption rate "
        f"**{e4['placebo_disruption_rate']:.3f}** "
        f"(follow-object {_fmt_rate(e4['placebo']['rates']['follow_object'])}).",
        f"- Appearance flip (no move): follow-object "
        f"{_fmt_rate(e4['appearance_flip']['rates']['follow_object'])}, "
        f"lost {_fmt_rate(e4['appearance_flip']['rates']['lost'])}.",
        "",
        e4["reviewer2_note"] + ".",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", default="configs/default.yaml")
    ap.add_argument("--out", default="results")
    args = ap.parse_args()

    if real_sam2_enabled():
        print(
            f"NOTE: {ENV_FLAG}=1 is set, but this runner is synthetic-only; "
            "the real-SAM2 adapter is a separate stub (src/a0028/sam2_wrapper.py)."
        )
    else:
        print(f"Real-SAM2 path DISABLED (default; set {ENV_FLAG}=1 plus weights to enable).")

    cfg = load_config(args.config)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    t0 = time.time()
    results = {
        "provenance": {
            "idea": "W2-A-0028 SAM2 teleport test (exp_07)",
            "labeling": MEASURED,
            "note": "no SAM2 numbers; surrogate memory tracker only",
        },
        "config": {k: cfg[k] for k in ("seed", "world", "tracker", "grid", "experiments")},
    }
    print("E1: arbitration curves over (d, g, s) grid ...")
    results["exp1_arbitration"] = exp1_arbitration(cfg)
    print("E2: instrument validation (lambda sweep) ...")
    results["exp2_instrument_validation"] = exp2_instrument_validation(cfg)
    print("E3: identity continuation / memory pollution ...")
    results["exp3_identity_continuation"] = exp3_identity_continuation(cfg)
    print("E4: Reviewer-2 controls (placebo, appearance flip) ...")
    results["exp4_controls"] = exp4_controls(cfg)
    elapsed = time.time() - t0

    (out_dir / "results.json").write_text(json.dumps(results, indent=2))
    report = render_report(args.config, results, elapsed)
    (out_dir / "report.md").write_text(report)
    print(f"\nWrote {out_dir/'results.json'} and {out_dir/'report.md'} ({elapsed:.1f}s).")
    print("\n" + report)


if __name__ == "__main__":
    main()
