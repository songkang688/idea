"""P082 threshold-sweep gate (E1) — noise-floor envelope + PROCEED/PIVOT decision.

Fully implemented, numpy-only. This module is the SINGLE code path for threshold
handling in the whole package: the E3 battery imports `tune_threshold` /
`apply_threshold` so gate and battery cannot drift apart (symmetric-threshold
obligation, stage4_r2_setB.md §8).

Data model
----------
The gate operates on *evaluation records*: for one (model, domain, prompt_type)
and one calibration/eval split draw, a matrix `M[t, i]` of the per-image metric
(Dice or IoU) at each threshold t of the pre-registered sweep. Producing M
requires real model outputs; nothing here fabricates it.

Symmetric protocol
------------------
`symmetric_delta` tunes thresholds for the frozen and fine-tuned model on the
SAME calibration matrices and applies both to the SAME eval matrices. Asymmetric
oracle access is structurally impossible through this API.

Envelope
--------
`build_envelope` consumes replicate deltas measured on the FROZEN model only
(prompt-sampling seeds × split draws × threshold sweep), i.e. under the null
"same weights, no forgetting", and returns the empirical 95% band of |Δ|.
Attack B6 (fine-tuned models may be noisier) is answered by `combine_envelopes`
taking the per-cell max.

CLI
---
`python -m promptamnesia.threshold_gate --config ../configs/p082_gate.yaml --self-test`
runs invariant checks on SYNTHETIC data. Self-test output is labeled and is not
an experimental result.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np

# ---------------------------------------------------------------- thresholds


def tune_threshold(cal_matrix: np.ndarray) -> int:
    """Return the index of the threshold maximizing mean per-image metric on
    the calibration split. cal_matrix: shape (T, N_cal)."""
    if cal_matrix.ndim != 2:
        raise ValueError("cal_matrix must be (num_thresholds, num_images)")
    return int(np.argmax(cal_matrix.mean(axis=1)))


def apply_threshold(eval_matrix: np.ndarray, t_idx: int) -> float:
    """Mean per-image metric on the eval split at the tuned threshold."""
    return float(eval_matrix[t_idx].mean())


def symmetric_delta(
    frozen_cal: np.ndarray,
    frozen_eval: np.ndarray,
    ft_cal: np.ndarray,
    ft_eval: np.ndarray,
) -> float:
    """Retention delta Δ = metric(fine-tuned) − metric(frozen), both at their
    own thresholds tuned on the SAME calibration split (symmetric protocol)."""
    t_frozen = tune_threshold(frozen_cal)
    t_ft = tune_threshold(ft_cal)
    return apply_threshold(ft_eval, t_ft) - apply_threshold(frozen_eval, t_frozen)


# ------------------------------------------------------------------ envelope


@dataclass(frozen=True)
class Envelope:
    """Noise-floor band for one (domain, prompt_type) cell."""

    domain: str
    prompt_type: str
    band_95: float          # 95th percentile of |Δ| under the null
    n_replicates: int
    source: str             # "frozen" | "ft" | "max(frozen,ft)"


def build_envelope(
    null_deltas: np.ndarray, domain: str, prompt_type: str, source: str = "frozen"
) -> Envelope:
    """null_deltas: 1-D array of replicate deltas measured with NO weight change
    (frozen model under prompt-seed × split-draw × threshold variance)."""
    null_deltas = np.asarray(null_deltas, dtype=float).ravel()
    if null_deltas.size < 8:
        raise ValueError(
            f"envelope for ({domain},{prompt_type}) needs >=8 replicates, got {null_deltas.size}; "
            "increase prompt seeds / split draws (config: envelope.variance_sources)"
        )
    return Envelope(
        domain=domain,
        prompt_type=prompt_type,
        band_95=float(np.percentile(np.abs(null_deltas), 95)),
        n_replicates=int(null_deltas.size),
        source=source,
    )


def combine_envelopes(a: Envelope, b: Envelope) -> Envelope:
    """Attack-B6 operative envelope: per-cell max of frozen- and FT-based bands."""
    if (a.domain, a.prompt_type) != (b.domain, b.prompt_type):
        raise ValueError("can only combine envelopes of the same cell")
    wider = a if a.band_95 >= b.band_95 else b
    return Envelope(
        domain=a.domain,
        prompt_type=a.prompt_type,
        band_95=wider.band_95,
        n_replicates=min(a.n_replicates, b.n_replicates),
        source="max(frozen,ft)",
    )


# ------------------------------------------------------------------ decision


@dataclass(frozen=True)
class TargetDelta:
    """One pre-registered target (configs/p082_gate.yaml) with its measured Δ."""

    checkpoint: str
    domain: str
    prompt_type: str
    delta: float            # reproduced retention delta (symmetric protocol)


@dataclass(frozen=True)
class GateVerdict:
    decision: str                       # "PROCEED" | "PIVOT"
    outside_cells: tuple[tuple[str, str, str], ...]   # (checkpoint, domain, prompt_type)
    rationale: str


def gate_decision(
    targets: list[TargetDelta],
    envelopes: dict[tuple[str, str], Envelope],
    min_domains: int = 2,
) -> GateVerdict:
    """PROCEED iff ≥1 checkpoint has |Δ| outside the operative envelope on
    ≥`min_domains` retention domains for ≥1 prompt type (pre-registered rule)."""
    outside: list[tuple[str, str, str]] = []
    per_ckpt_domains: dict[str, set[str]] = {}
    for t in targets:
        env = envelopes.get((t.domain, t.prompt_type))
        if env is None:
            raise KeyError(f"no envelope for cell ({t.domain}, {t.prompt_type})")
        if abs(t.delta) > env.band_95:
            outside.append((t.checkpoint, t.domain, t.prompt_type))
            per_ckpt_domains.setdefault(t.checkpoint, set()).add(t.domain)
    proceed = any(len(doms) >= min_domains for doms in per_ckpt_domains.values())
    if proceed:
        rationale = (
            "≥1 released checkpoint shows reproduced deltas outside the operative "
            f"envelope on ≥{min_domains} domains → E2 grid licensed."
        )
        return GateVerdict("PROCEED", tuple(outside), rationale)
    return GateVerdict(
        "PIVOT",
        tuple(outside),
        "All pre-registered deltas inside the noise-floor envelope (or outside on "
        "<2 domains) → Idea_02 re-scopes to the deflation branch (roadmap Phase 2').",
    )


# ------------------------------------------------------------------ self-test


def _self_test(seed: int = 0) -> None:
    """Invariant checks on SYNTHETIC data. Not an experimental result."""
    rng = np.random.default_rng(seed)
    T, n_cal, n_eval, reps = 51, 60, 120, 24

    def synth_model(quality: float) -> tuple[np.ndarray, np.ndarray]:
        base = np.clip(quality + 0.05 * np.sin(np.linspace(0, np.pi, T)), 0, 1)
        cal = np.clip(base[:, None] + rng.normal(0, 0.08, (T, n_cal)), 0, 1)
        ev = np.clip(base[:, None] + rng.normal(0, 0.08, (T, n_eval)), 0, 1)
        return cal, ev

    # (1) Null: frozen vs frozen replicate deltas straddle zero and are small.
    null_deltas = []
    for _ in range(reps):
        c1, e1 = synth_model(0.7)
        c2, e2 = synth_model(0.7)
        null_deltas.append(symmetric_delta(c1, e1, c2, e2))
    env = build_envelope(np.array(null_deltas), "synthetic", "box")
    assert env.band_95 < 0.1, "null envelope implausibly wide on synthetic data"

    # (2) A real degradation (quality 0.7 -> 0.4) lands far outside the envelope.
    c_f, e_f = synth_model(0.7)
    c_t, e_t = synth_model(0.4)
    big_delta = symmetric_delta(c_f, e_f, c_t, e_t)
    assert abs(big_delta) > env.band_95, "degradation should exceed null envelope"

    # (3) Decision rule wiring: outside on 2 domains -> PROCEED; inside -> PIVOT.
    envs = {("d1", "box"): env, ("d2", "box"): env}
    v1 = gate_decision(
        [TargetDelta("ckpt", "d1", "box", big_delta), TargetDelta("ckpt", "d2", "box", big_delta)],
        envs,
    )
    v2 = gate_decision(
        [TargetDelta("ckpt", "d1", "box", 0.0), TargetDelta("ckpt", "d2", "box", 0.0)], envs
    )
    assert v1.decision == "PROCEED" and v2.decision == "PIVOT"

    print("[threshold_gate] SELF-TEST PASSED (synthetic data — not an experimental result)")
    print(f"  synthetic null envelope band_95={env.band_95:.4f} over {env.n_replicates} replicates")
    print(f"  synthetic degradation delta={big_delta:.4f} -> {v1.decision} / null -> {v2.decision}")


def main() -> None:
    ap = argparse.ArgumentParser(description="P082 threshold-sweep gate (E1)")
    ap.add_argument("--config", type=str, default=None, help="configs/p082_gate.yaml (for real runs)")
    ap.add_argument("--self-test", action="store_true", help="run synthetic invariant checks")
    args = ap.parse_args()
    if args.self_test:
        _self_test()
        return
    raise SystemExit(
        "Real gate runs require model outputs (per-threshold metric matrices) produced from "
        "released checkpoints and datasets pinned at roadmap Phase 0. Use --self-test to "
        "verify the machinery. No fake metrics are generated."
    )


if __name__ == "__main__":
    main()
