#!/usr/bin/env python3
"""B-0114 Stage-7 prototype runner — 4-arm dense-task VPT decomposition on
synthetic scenes. CPU-only, no downloads, no real-data numbers.

Every number printed under MEASURED was computed on synthetic scenes
generated in-process. The pre-registered hypotheses from exp_01 are printed
under EXPECTED (HYPOTHESIS) and are never claimed as findings.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from vpt_registers.config import load_config
from vpt_registers.metrics import aggregate, decomposition, h2_gap
from vpt_registers.signatures import collect_signatures
from vpt_registers.train import make_seed_data, pretrain_backbone, train_arm

ARM_ORDER = ["no_token", "frozen_random", "learned", "learned_frozen", "sink_only"]

ARM_LABELS = {
    "no_token": "arm 4  no_token       (dense readout baseline, VPT arm d)",
    "frozen_random": "arm 1  frozen_random  (register-like, never trained)",
    "learned": "arm 2  learned        (full VPT-shallow)",
    "learned_frozen": "arm 3  learned_frozen (arm-2 tokens frozen, fresh head)",
    "sink_only": "extra  sink_only      (H attention-bias control, value=0)",
}

SIGNATURE_KEYS = [
    "prompt_sink_mass_mean",
    "register_sink_mass_mean",
    "patch_norm_outlier_frac",
    "prompt_to_patch_norm_ratio",
    "nuisance_rel_displacement",
]

EXPECTED = """\
EXPECTED (HYPOTHESIS, pre-registered in exp_01 — NOT measured facts):
  H1  On the register-free backbone, non-learned arms (frozen_random /
      sink_only) reproduce a non-zero fraction of the full VPT dense-task
      gain; learned tokens develop register signatures (sink mass, norm
      ratio) beyond frozen ones.
  H2  total VPT gain (learned - no_token) is LARGER on the register-free
      backbone than on the register-equipped sibling (directional).
  Inv Injected tokens absorb global aggregation: patch features become
      LESS sensitive to a global-nuisance swap (lower rel. displacement)
      when tokens are present, most for learned tokens.
  Falsified in-sandbox if: insertion and sink components are ~0 within seed
  noise on the register-free backbone AND the H2 gap is within seed noise
  (the dense analogue of VPT Fig. 11 Prompt-Fixed ~= Linear).
"""

DISCLAIMER = """\
+----------------------------------------------------------------------+
| NO NUMBER BELOW IS AN ADE20K / Cityscapes / NYUv2 / ImageNet RESULT. |
| All MEASURED values come from synthetic scenes generated in-process. |
| The synthetic backbone was PRETRAINED WITH GLOBAL-ONLY OBJECTIVES so |
| that the hypothesised mechanism has something to act on; this run    |
| validates the INSTRUMENT (arms, decomposition, signatures), not the  |
| claim. Real-data magnitudes are exactly what the killer experiment   |
| in exp_01 must measure.                                              |
+----------------------------------------------------------------------+
"""


def fmt(mean: float, sd: float) -> str:
    return f"{mean:+.4f} ± {sd:.4f}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", required=True, help="YAML config path")
    ap.add_argument("--quick", action="store_true", help="1 seed, fewer steps (smoke run)")
    ap.add_argument("--seeds", default=None, help="comma-separated seed override, e.g. 0,1,2")
    ap.add_argument("--json", default=None, help="dump machine-readable results to this path")
    ap.add_argument(
        "--with-b0001-hook",
        action="store_true",
        help="ALSO run the quarantined B-0001 norm-vs-error hook (separate idea)",
    )
    args = ap.parse_args()

    cfg = load_config(args.config)
    if args.seeds is not None:
        cfg.seeds = [int(s) for s in args.seeds.split(",")]
    if args.quick:
        cfg.seeds = cfg.seeds[:1]
        cfg.train.pretrain_steps = min(cfg.train.pretrain_steps, 100)
        cfg.train.arm_steps = min(cfg.train.arm_steps, 120)
        cfg.train.train_scenes = min(cfg.train.train_scenes, 192)
        cfg.train.val_scenes = min(cfg.train.val_scenes, 96)

    arms = [a for a in ARM_ORDER if a in cfg.arms]

    print(DISCLAIMER)
    print(EXPECTED)
    print(
        f"config={cfg.name}  seeds={cfg.seeds}  backbones={cfg.backbones}  "
        f"arms={arms}  K={cfg.num_prompts} prompts  head={cfg.head_kind}"
    )
    t0 = time.time()

    results = []
    signatures = defaultdict(lambda: defaultdict(list))  # [backbone][arm] -> [dict per seed]
    b0001_rows = []

    for seed in cfg.seeds:
        data = make_seed_data(cfg, seed)
        for variant in cfg.backbones:
            backbone = pretrain_backbone(cfg, variant, seed, data)
            learned_tokens = None
            for arm in arms:
                res = train_arm(
                    cfg,
                    backbone,
                    variant,
                    arm,
                    seed,
                    data,
                    learned_tokens=learned_tokens if arm == "learned_frozen" else None,
                )
                if arm == "learned":
                    learned_tokens = res.tokens
                results.append(res)
                sig = collect_signatures(
                    backbone, res.tokens, res.prompt_is_sink, data.val, data.paired, cfg
                )
                signatures[variant][arm].append(sig)
                print(
                    f"  [seed {seed}] {variant:18s} {arm:14s} "
                    f"mIoU={res.miou:.4f} acc={res.pixel_acc:.4f} "
                    f"sink={sig['prompt_sink_mass_mean']:.3f} "
                    f"nuis={sig['nuisance_rel_displacement']:.4f}"
                )
                if args.with_b0001_hook:
                    from vpt_registers.b0001_hook import norm_error_auroc

                    hook = norm_error_auroc(
                        backbone, res.head, res.tokens, res.prompt_is_sink, data.val, cfg
                    )
                    b0001_rows.append(
                        {"seed": seed, "backbone": variant, "arm": arm, **hook}
                    )

    elapsed = time.time() - t0
    agg = aggregate(results)

    print("\n" + "=" * 74)
    print("MEASURED (synthetic) — mIoU per arm, mean ± sd over seeds")
    print("=" * 74)
    for variant in cfg.backbones:
        print(f"\nbackbone: {variant}")
        for arm in arms:
            m, s, _ = agg[variant][arm]
            print(f"  {ARM_LABELS[arm]:62s} {m:.4f} ± {s:.4f}")

    print("\n" + "=" * 74)
    print("MEASURED (synthetic) — gain decomposition (mIoU deltas, seed-wise)")
    print("  telescoping: insertion + content_transfer + co_adaptation = total")
    print("=" * 74)
    decomp_out = {}
    for variant in cfg.backbones:
        decomp = decomposition(agg[variant])
        decomp_out[variant] = decomp
        print(f"\nbackbone: {variant}")
        for name, (m, s, _) in decomp.items():
            print(f"  {name:18s} {fmt(m, s)}")

    h2 = h2_gap(agg)
    print("\n" + "=" * 74)
    print("MEASURED (synthetic) — H2 directional readout")
    print("=" * 74)
    if h2 is None:
        print("  (needs both backbones and arms learned+no_token — not all present)")
    else:
        print(f"  VPT gain | register_free     : {fmt(*h2['gain_register_free'])}")
        print(f"  VPT gain | register_equipped : {fmt(*h2['gain_register_equipped'])}")
        print(f"  gap (free - equipped)        : {fmt(h2['gap'][0], h2['gap'][1])}")
        print(
            f"  H2 direction (gap > 0)       : "
            f"{'CONFIRMED on synthetic' if h2['direction_confirmed'] else 'NOT confirmed on synthetic'}"
            "  [sandbox mechanism check, NOT a real-data finding]"
        )

    print("\n" + "=" * 74)
    print("MEASURED (synthetic) — register signatures & invariance, mean over seeds")
    print("  (sink = attn mass from patch queries onto prompt slots;")
    print("   nuis = patch-feature rel. displacement under global-nuisance swap)")
    print("=" * 74)
    sig_out = {}
    for variant in cfg.backbones:
        print(f"\nbackbone: {variant}")
        header = f"  {'arm':14s}" + "".join(f"{k[:22]:>24s}" for k in SIGNATURE_KEYS)
        print(header)
        sig_out[variant] = {}
        for arm in arms:
            row = {}
            for k in SIGNATURE_KEYS:
                vals = [s[k] for s in signatures[variant][arm] if k in s]
                row[k] = float(sum(vals) / len(vals)) if vals else None
            sig_out[variant][arm] = row
            cells = "".join(
                f"{(f'{row[k]:.4f}' if row[k] is not None else '—'):>24s}"
                for k in SIGNATURE_KEYS
            )
            print(f"  {arm:14s}{cells}")

    if args.with_b0001_hook:
        from vpt_registers.b0001_hook import BANNER

        print("\n" + "=" * 74)
        print(BANNER)
        print("=" * 74)
        for r in b0001_rows:
            print(
                f"  [seed {r['seed']}] {r['backbone']:18s} {r['arm']:14s} "
                f"norm-vs-error AUROC={r['norm_error_auroc']:.4f} "
                f"(patch err rate {r['patch_error_rate']:.3f}, n={r['n_patches']})"
            )

    print(f"\ntotal wall time: {elapsed:.1f}s (CPU)")

    if args.json:
        payload = {
            "config": cfg.name,
            "seeds": cfg.seeds,
            "arms": arms,
            "backbones": cfg.backbones,
            "miou": agg,
            "decomposition": decomp_out,
            "h2": h2,
            "signatures": sig_out,
            "b0001_hook": b0001_rows if args.with_b0001_hook else None,
            "elapsed_s": elapsed,
            "provenance": "SYNTHETIC in-process data only; no real-dataset numbers",
        }
        Path(args.json).write_text(json.dumps(payload, indent=2))
        print(f"wrote {args.json}")


if __name__ == "__main__":
    main()
