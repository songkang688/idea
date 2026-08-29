#!/usr/bin/env python3
"""Exercise the pilot decision rule (proposal.md section 17) on simulated failures.

This is the 50-failure pilot gate, run against a simulator instead of SAM2 so the
decision logic can be checked before any GPU time is spent. Two scenarios are run,
and the second is the important one:

  scenario A  memory-borne failure is real. Targeted deletion should beat no-op,
              beat reset, and beat the sham.

  scenario B  memory-borne failure is ZERO, but the tracker is sensitive to which
              recency slot an entry occupies. Targeted deletion still appears to
              help -- purely as a temporal-encoding artifact. The sham arm must
              catch this. If it does not, the real experiment would report an
              encoding artifact as a causal decomposition, which is exactly the
              failure mode reviewer attack A2 describes.

The validity section does the same job for attack A1: it prints the naive
correlation next to the difficulty-partialled one, on data where the confound is
present by construction.

    python run_pilot.py --failures 50 --sequences 40 --seed 0
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from memory_surgery import (  # noqa: E402
    SimConfig,
    SimulatedTracker,
    bootstrap_arm_gap,
    check_replay_determinism,
    evaluate_validity,
    partial_correlation,
    recovery_rates,
    run_arms,
)

TARGETED_VS_NOOP_MIN = 0.30
TARGETED_VS_RESET_MIN = 0.10
TARGETED_VS_SHAM_MIN = 0.10


def run_scenario(name: str, cfg: SimConfig, n_failures: int, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    tracker = SimulatedTracker(cfg, rng)

    results = []
    h2_testable = []
    for _ in range(n_failures):
        t_f = int(rng.integers(30, 70))
        # Failure duration is drawn across the memory horizon deliberately. When a
        # failure lasts longer than the bank's capacity, FIFO has already flushed
        # every pre-error entry, so `targeted` and `reset` are the SAME operation
        # and hypothesis H2 is untestable on that failure. The duration/capacity
        # ratio therefore bounds how much of the corpus can speak to H2 at all,
        # which is why the real harvest must report this share (see proposal 19).
        t_r = t_f + int(rng.integers(2, 14))
        bank = tracker.build_failure_bank(t_f, t_r)
        n_original = sum(1 for e in bank.entries() if not e.is_conditioning)
        h2_testable.append(any(e.written_at < t_f for e in bank.recent))
        results.append(
            run_arms(
                bank,
                lambda b: tracker.recovers(b, t_f, n_original),
                t_f=t_f,
                t_r=t_r,
                rng=rng,
            )
        )

    # P2 is evaluated on the H2-testable subset ONLY. On failures that outlasted the
    # memory horizon, FIFO has already flushed every pre-error entry, so `targeted`
    # and `reset` are literally the same operation and contribute an exact zero to
    # the gap. Averaging those in does not measure a smaller effect -- it dilutes a
    # real one toward zero by a factor set by the corpus's failure-duration
    # distribution, which is a property of the benchmark rather than of SAM2.
    h2_results = [r for r, ok in zip(results, h2_testable) if ok]

    rates = recovery_rates(results)
    gaps = {
        "targeted-no_op": bootstrap_arm_gap(results, "targeted", "no_op", seed=seed),
        "targeted-sham": bootstrap_arm_gap(results, "targeted", "sham", seed=seed),
        "slot_control-targeted": bootstrap_arm_gap(
            results, "slot_control", "targeted", seed=seed
        ),
    }
    reset_all = bootstrap_arm_gap(results, "targeted", "reset", seed=seed)
    reset_h2 = bootstrap_arm_gap(h2_results, "targeted", "reset", seed=seed)

    print(f"\n=== scenario {name} ===")
    print(f"    memory_borne_share={cfg.memory_borne_share}  "
          f"clean_memory_value={cfg.clean_memory_value}  "
          f"crowding_relief={cfg.crowding_relief}")
    print(f"    H2-testable failures (pre-error memory survived FIFO): "
          f"{len(h2_results)}/{n_failures}")
    print("    recovery rate by arm: " + "  ".join(f"{a}={r:.2f}" for a, r in rates.items()))
    for k, (p, lo, hi) in gaps.items():
        print(f"    {k:<22} {p:+.3f}  [{lo:+.3f}, {hi:+.3f}]")
    print(f"    {'targeted-reset (all)':<22} {reset_all[0]:+.3f}  "
          f"[{reset_all[1]:+.3f}, {reset_all[2]:+.3f}]   <-- diluted, NOT the test")
    print(f"    {'targeted-reset (H2 set)':<22} {reset_h2[0]:+.3f}  "
          f"[{reset_h2[1]:+.3f}, {reset_h2[2]:+.3f}]   <-- P2 is read here")

    p1 = gaps["targeted-no_op"][0] >= TARGETED_VS_NOOP_MIN
    p2 = reset_h2[0] >= TARGETED_VS_RESET_MIN
    p3 = gaps["targeted-sham"][0] >= TARGETED_VS_SHAM_MIN
    print(f"    P1 (>= {TARGETED_VS_NOOP_MIN:.2f} vs no-op): {'PASS' if p1 else 'FAIL'}")
    print(f"    P2 (>= {TARGETED_VS_RESET_MIN:.2f} vs reset): {'PASS' if p2 else 'FAIL'}")
    print(f"    P3 (>= {TARGETED_VS_SHAM_MIN:.2f} vs sham) : {'PASS' if p3 else 'FAIL'}")
    if p1 and p3 and not p2:
        print("    VERDICT: targeted is no better than a restart. Publishable as a "
              "bounded diagnostic post-mortem, not as a decomposition.")
    elif p1 and p2 and not p3:
        print("    VERDICT: apparent effect is deletion mechanics, not memory content. "
              "Instrument dead.")
    elif p1 and p2 and p3:
        print("    VERDICT: decomposition survives all three arms at pilot scale.")
    else:
        print("    VERDICT: does not clear the pilot gate.")
    return {"rates": rates, "gaps": gaps, "p1": p1, "p2": p2, "p3": p3}


def run_validity(n_sequences: int, seed: int) -> None:
    """Attack A1: does the instrument survive difficulty controls?"""
    rng = np.random.default_rng(seed + 7)
    tracker = SimulatedTracker(SimConfig(), rng)

    difficulty = rng.uniform(0.1, 0.9, size=n_sequences)
    failure_count = rng.integers(1, 12, size=n_sequences).astype(float)
    no_op_recovery = np.clip(1.0 - difficulty + rng.normal(0, 0.08, n_sequences), 0, 1)

    # rho is genuinely tied to difficulty as well as to the memory-borne share.
    rho = np.clip(0.75 * (1 - difficulty) + rng.normal(0, 0.10, n_sequences), 0, 1)

    frozen = ("SAMURAI", "DAM4SAM", "SAM2Long")
    quality = {"SAMURAI": 0.55, "DAM4SAM": 0.45, "SAM2Long": 0.05}
    gains = {
        c: np.array([tracker.comparator_gain(r, d, quality[c])
                     for r, d in zip(rho, difficulty)])
        for c in frozen
    }

    Z = np.column_stack([no_op_recovery, failure_count, difficulty])

    print("\n=== predictive validity (attack A1) ===")
    print(f"{'comparator':<12}{'naive r':>10}{'partial r':>12}")
    for c in frozen:
        naive = float(np.corrcoef(rho, gains[c])[0, 1])
        part = partial_correlation(rho, gains[c], Z)
        print(f"{c:<12}{naive:>10.3f}{part:>12.3f}")

    verdict = evaluate_validity(rho, gains, Z, frozen_set=frozen, seed=seed)
    print()
    print(verdict.report())
    print()
    print("Read the two columns together: the naive correlation is inflated by the")
    print("shared-difficulty confound that the simulator injects by construction.")
    print("The pre-registered statistic is the MINIMUM partial r over the frozen set,")
    print("so a single strong comparator cannot carry the headline on its own.")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--failures", type=int, default=50)
    ap.add_argument("--sequences", type=int, default=40)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    rng = np.random.default_rng(args.seed)
    tracker = SimulatedTracker(SimConfig(noise=0.0), rng)
    bank = tracker.build_failure_bank(40, 55)
    check_replay_determinism(bank, lambda b: b.mean_corruption() < 0.5)
    print("E0 replay-determinism gate: PASS")

    run_scenario(
        "A: memory-borne failure is real",
        SimConfig(memory_borne_share=0.75, clean_memory_value=0.35, crowding_relief=0.0),
        args.failures, args.seed,
    )
    run_scenario(
        "B: NO memory-borne failure, tracker just likes emptier banks",
        SimConfig(memory_borne_share=0.0, clean_memory_value=0.0, crowding_relief=0.75),
        args.failures, args.seed,
    )
    run_validity(args.sequences, args.seed)

    print("\nNOTE: every number above is simulated. It validates the decision rule,")
    print("not SAM2. No claim about any tracker follows from this script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
