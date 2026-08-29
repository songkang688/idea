"""Exercise the whole RehearsalGrid decision rule on synthetic eval scores.

No GPU, no model, no training. Every number this prints is SIMULATED and validates
the *decision rule*, not any claim about rehearsal. The purpose is to show that the
rule behaves correctly in three worlds before 2,450 A100-hours are spent finding out
which world we are in -- and, critically, that it refuses to answer in the world
where it has no power.

    python src/run_decision_demo.py
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from rehearsal_grid.arms import (  # noqa: E402
    ARMS,
    bigram_destroyed,
    destroy,
    unigram_preserved,
)
from rehearsal_grid.decision import bootstrap_share, evaluate  # noqa: E402
from rehearsal_grid.matching import (  # noqa: E402
    effective_lr_multiplier,
    global_norm_scale,
    mismatch_under_global,
    per_layer_scale,
)
from rehearsal_grid.power import DenominatorGate, StratumScores, power_check  # noqa: E402
from rehearsal_grid.sampler import (  # noqa: E402
    InterleavedSampler,
    build_matched_budgets,
)

CAPABILITIES = ("fluency", "knowledge", "reasoning", "instruction")
MDE = 0.02
N_SEEDS = 3


def rule(title: str) -> None:
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


# --------------------------------------------------------------------------- #
# 1. arms
# --------------------------------------------------------------------------- #
def check_arms(seed: int) -> None:
    rule("1. Content-destruction transforms")
    rng = np.random.default_rng(seed)
    vocab = 5_000
    docs = [rng.integers(0, vocab, size=int(rng.integers(400, 800))).tolist() for _ in range(40)]

    for arm in ARMS:
        out = destroy(arm.name, docs, np.random.default_rng(seed))
        n_tok = sum(len(d) for d in out)
        n_uniq = len({tuple(d) for d in out})
        print(
            f"  {arm.name:<16} docs={len(out):>3}  tokens={n_tok:>6}  "
            f"distinct_docs={n_uniq:>3}   destroys: {arm.destroys}"
        )

    shuffled = destroy("A3_shuffled", docs, np.random.default_rng(seed))
    print(f"\n  A3 preserves unigram statistics : {unigram_preserved(docs, shuffled)}")
    print(f"  A3 destroys local structure     : {bigram_destroyed(docs, shuffled)}")
    print(
        "  Both must hold, or A3 is not the control the design claims. The real\n"
        "  version of this check is E0b, which asks whether permuted tokens give a\n"
        "  usable gradient at all or just degenerate attention."
    )


# --------------------------------------------------------------------------- #
# 2. token budgets
# --------------------------------------------------------------------------- #
def check_budgets() -> None:
    rule("2. Token-budget re-matching (reviewer attack A1)")
    stripped = 620_000_000
    budgets = build_matched_budgets(stripped, 0.10, [a.name for a in ARMS])
    print(f"  text-stripped mix: {stripped:,} tokens\n")
    print(f"  {'arm':<16}{'total':>14}{'multimodal':>14}{'rehearsal':>13}")
    for name, b in budgets.items():
        print(f"  {name:<16}{b.total_tokens:>14,}{b.multimodal_tokens:>14,}{b.rehearsal_tokens:>13,}")

    totals = {b.total_tokens for b in budgets.values()}
    print(f"\n  all arms on an identical total budget: {len(totals) == 1}")
    print(
        "  A0 has no rehearsal stream, so it draws more multimodal tokens to reach the\n"
        "  same total. Skipping that step makes A0 the shortest run and hands the grid a\n"
        "  training-length confound dressed up as a rehearsal effect."
    )

    sampler = InterleavedSampler(n_multimodal_batches=9_000, interleave=9)
    print(
        f"\n  schedule: {sampler.n_text_batches:,} text / {sampler.n_multimodal_batches:,} "
        f"multimodal batches -> {sampler.realised_fraction():.3f} of batches"
    )
    print(
        "  Note that this is a batch fraction, not a token fraction. They coincide only\n"
        "  when both batch types carry the same token count, which they do not."
    )


# --------------------------------------------------------------------------- #
# 3. gradient matching
# --------------------------------------------------------------------------- #
def check_matching(seed: int) -> None:
    rule("3. Gradient matching: per-layer (PRIMARY) vs global norm (SECONDARY)")
    rng = np.random.default_rng(seed)
    n_layers = 32

    # Per-layer disparity across modalities is documented (arXiv:2606.17296): early
    # and late blocks do not scale alike. The synthetic gradients reproduce that
    # shape so the two conventions have something to disagree about.
    ref, txt = {}, {}
    for i in range(n_layers):
        scale = 1.0 + 3.0 * (i / n_layers) ** 2
        ref[f"block{i}"] = rng.normal(0, 0.01 * scale, size=256)
        txt[f"block{i}"] = rng.normal(0, 0.01 / scale, size=256)

    g = global_norm_scale(ref, txt)
    pl = per_layer_scale(ref, txt)
    mm = mismatch_under_global(ref, txt)
    vals = np.array(list(mm.values()))

    print(f"  global scale (one scalar for the whole tower) : {g:.3f}")
    print(f"  per-layer scales                              : min {min(pl.values()):.3f}  max {max(pl.values()):.3f}")
    print(f"  residual per-layer mismatch under the global rule: {vals.min():.3f} .. {vals.max():.3f}")
    print(f"  effective-LR multiplier on the language tower : {effective_lr_multiplier(pl):.2f}x")
    print(
        "\n  The global convention reports a clean match while individual blocks are off\n"
        f"  by up to {max(vals.max(), 1 / max(vals.min(), 1e-9)):.1f}x. That is why per-layer is the\n"
        "  pre-registered primary. Stage 5 left the two symmetric and said divergence\n"
        "  would be 'the finding' -- which makes every outcome a result, so Stage 6\n"
        "  required naming one in advance.\n"
        "  The LR multiplier is logged because matching changes the step size on the\n"
        "  language tower: that is a training-stability risk, not a free operation."
    )


# --------------------------------------------------------------------------- #
# 4. denominator gate
# --------------------------------------------------------------------------- #
def check_denominators() -> None:
    rule("4. Denominator-adequacy gate (reviewer attack A2)")
    # Base-model scores below are ILLUSTRATIVE placeholders standing in for a
    # Vicuna-7B profile. The real gate runs on measured base scores at E0.
    gates = [
        DenominatorGate("fluency", base_score=0.71, chance_level=0.00, seed_sd=0.006),
        DenominatorGate("knowledge", base_score=0.47, chance_level=0.25, seed_sd=0.008),
        DenominatorGate("reasoning_arc", base_score=0.46, chance_level=0.25, seed_sd=0.009),
        DenominatorGate("reasoning_gsm8k", base_score=0.03, chance_level=0.00, seed_sd=0.007),
        DenominatorGate("instruction_ifeval", base_score=0.28, chance_level=0.22, seed_sd=0.021),
    ]
    print(f"  {'stratum':<22}{'base':>7}{'chance':>8}{'headroom':>10}{'snr':>8}  verdict")
    for gt in gates:
        print(
            f"  {gt.capability:<22}{gt.base_score:>7.2f}{gt.chance_level:>8.2f}"
            f"{gt.headroom:>10.3f}{gt.snr:>8.1f}  {gt.verdict()}"
        )
    dropped = [gt.capability for gt in gates if not gt.usable]
    print(f"\n  strata that cannot support a ratio: {dropped}")
    print(
        "  These are replaced BEFORE the 15 arms run, not explained away afterwards.\n"
        "  A near-floor denominator lets one stratum flip the >=3-of-4 rule on noise."
    )


# --------------------------------------------------------------------------- #
# 5. the decision rule in three worlds
# --------------------------------------------------------------------------- #
def synth(
    cap: str, arm: str, base: float, delta: float, sd: float, rng: np.random.Generator
) -> StratumScores:
    return StratumScores(
        capability=cap,
        arm=arm,
        base_score=base,
        scores=tuple(base + delta + rng.normal(0, sd, size=N_SEEDS)),
    )


def world(
    name: str,
    base: dict[str, float],
    d0: dict[str, float],
    d1: dict[str, float],
    d2: dict[str, float],
    sd: float,
    seed: int,
) -> None:
    rng = np.random.default_rng(seed)
    a0 = {c: synth(c, "A0_none", base[c], d0[c], sd, rng) for c in CAPABILITIES}
    a1 = {c: synth(c, "A1_curated", base[c], d1[c], sd, rng) for c in CAPABILITIES}
    a2 = {c: synth(c, "A2_random_web", base[c], d2[c], sd, rng) for c in CAPABILITIES}

    print(f"\n--- {name} ---")
    print(power_check(a0, a1, mde=MDE).render())
    print()
    print(evaluate(a0, a1, a2, mde=MDE).render())


def check_decision(seed: int) -> None:
    rule("5. The pre-registered rule in four worlds (ALL NUMBERS SIMULATED)")
    base = {"fluency": 0.71, "knowledge": 0.47, "reasoning": 0.46, "instruction": 0.40}
    sd = 0.006

    world(
        "World 1: mechanism is real (any text-shaped gradient rescues everything)",
        base,
        d0={"fluency": -0.14, "knowledge": -0.10, "reasoning": -0.09, "instruction": -0.11},
        d1={"fluency": -0.01, "knowledge": -0.01, "reasoning": -0.01, "instruction": -0.01},
        d2={"fluency": -0.02, "knowledge": -0.02, "reasoning": -0.02, "instruction": -0.02},
        sd=sd,
        seed=seed,
    )

    world(
        "World 2: content is what matters (random web rehearsal helps nowhere)",
        base,
        d0={"fluency": -0.14, "knowledge": -0.10, "reasoning": -0.09, "instruction": -0.11},
        d1={"fluency": -0.02, "knowledge": -0.02, "reasoning": -0.02, "instruction": -0.02},
        d2={"fluency": -0.15, "knowledge": -0.12, "reasoning": -0.10, "instruction": -0.12},
        sd=sd,
        seed=seed,
    )

    world(
        "World 3: stratified -- fluency runs on gradient, knowledge needs content",
        base,
        d0={"fluency": -0.14, "knowledge": -0.10, "reasoning": -0.09, "instruction": -0.11},
        d1={"fluency": -0.01, "knowledge": -0.01, "reasoning": -0.03, "instruction": -0.02},
        d2={"fluency": -0.02, "knowledge": -0.07, "reasoning": -0.05, "instruction": -0.05},
        sd=sd,
        seed=seed,
    )

    world(
        "World 4: forgetting is tiny at this scale -- the gate must REFUSE to answer",
        base,
        d0={"fluency": -0.012, "knowledge": -0.008, "reasoning": -0.007, "instruction": -0.009},
        d1={"fluency": -0.002, "knowledge": -0.001, "reasoning": -0.002, "instruction": -0.002},
        d2={"fluency": -0.010, "knowledge": -0.007, "reasoning": -0.006, "instruction": -0.008},
        sd=sd,
        seed=seed,
    )


# --------------------------------------------------------------------------- #
# 6. share uncertainty
# --------------------------------------------------------------------------- #
def check_share_ci(seed: int) -> None:
    rule("6. How precise is a balance-share at three seeds? (reviewer attack A4)")
    rng = np.random.default_rng(seed)
    for total_gap, label in ((0.13, "large effect"), (0.03, "small effect")):
        balance = [total_gap * 0.85 + rng.normal(0, 0.008) for _ in range(N_SEEDS)]
        total = [total_gap + rng.normal(0, 0.008) for _ in range(N_SEEDS)]
        pt, lo, hi = bootstrap_share(balance, total, seed=seed)
        print(f"  {label:<14} (gap {total_gap:+.3f})  balance share = {pt:.2f}  [{lo:.2f}, {hi:.2f}]")
    print(
        "\n  Same underlying 0.85 share, two very different intervals. The 0.8 threshold is\n"
        "  only meaningful on the top row. This is exactly why P0 gates P1: below the\n"
        "  declared MDE the rule reports the absolute deltas and declines the share."
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    check_arms(args.seed)
    check_budgets()
    check_matching(args.seed)
    check_denominators()
    check_decision(args.seed)
    check_share_ci(args.seed)

    rule("Summary")
    print(
        "  Every number above is SIMULATED. Nothing here is a claim about rehearsal.\n"
        "  What it establishes is that the decision rule fires correctly in the worlds\n"
        "  where an effect exists, and refuses to fire in the world where it does not --\n"
        "  before 2,450 A100-hours are committed to finding out which world is ours."
    )


if __name__ == "__main__":
    main()
