# Stage-7 prototype — B-0114: 4-arm dense-task VPT decomposition (synthetic)

Runnable minimal prototype of **B-0114 in H's 4-arm dense-task form only**
(`Windows2/_wip/stage5_agent_N/exp_01.md`; pipeline: E bet #1 → G LOCK →
H SURVIVE-IF-EXPERIMENT (4-arm redesign) → L demotion of the naive form →
PI binding: *4-arm dense-task redesign or drop*). Built by Stage-7 Agent T.

This is **not** the original "afternoon frozen-token pilot" — that form is
struck by `PI_BINDING.md` because VPT's own Fig. 11 Prompt-Fixed ablation
already ran it on classification. Everything here is the *dense-task
mechanism* version: which part of a VPT-style gain on a dense prediction
task comes from token **location/register geometry**, which from the
**learned embedding**, and how that interacts with **dense-task invariance
breaking** — all treated as HYPOTHESES to instrument, never as facts.

```
NO NUMBER IN THIS DIRECTORY IS AN ADE20K / Cityscapes / NYUv2 / ImageNet
RESULT. Every quantity printed by run_synthetic.py is MEASURED ON
SYNTHETIC SCENES generated in-process by a tiny CPU ViT sandbox, and is
labelled as such. The synthetic backbone is pretrained with GLOBAL-ONLY
objectives precisely so the hypothesised mechanism has something to act
on: these runs validate the INSTRUMENT (arms, decomposition, signature
metrics), not the scientific claim. Real-data magnitudes are exactly what
the killer experiment in exp_01 must measure.
```

## The hypothesis being instrumented (HYPOTHESIS, not a claim)

On dense tasks, part of VPT's gain over a plain dense readout may come from
prompt tokens acting like *registers* (extra global-workspace slots that
absorb attention/aggregation) rather than from the learned task content of
the token embeddings. Register artifacts are known to corrupt *spatial*
feature maps (Darcet et al., arXiv:2309.16588), so dense tasks are where
the classification-only VPT Fig. 11 ablation (Prompt-Fixed ≈ Linear) may
fail to generalize. H's Stage-4 attack additionally demands that "token
insertion" effects be separated from softmax-temperature confounds — hence
the optional value-zeroed sink arm.

## The four arms (all coded, all runnable)

| # | arm id | tokens | trained? | isolates |
|---|--------|--------|----------|----------|
| 1 | `frozen_random` | K random N(0, .02) tokens | never | insertion / register geometry (confounded with temperature — see `sink_only`) |
| 2 | `learned` | K tokens, VPT-shallow | tokens + head | full VPT |
| 3 | `learned_frozen` | arm-2's tokens, frozen | fresh head only | learned embedding *content* minus head co-adaptation (cheap here, so implemented, not stubbed) |
| 4 | `no_token` | none | head only | dense readout baseline (segmentation-style linear or conv head on frozen patch features) |

Optional 5th arm (`configs/with_sink.yaml`), H's non-negotiable control:
`sink_only` — trainable *keys*, values force-zeroed in every attention
layer, so the token can bend attention geometry / soak attention mass but
can never inject content into patch tokens.

Two frozen backbone variants mirror the DINOv2 / DINOv2-reg sibling pair at
toy scale: `register_free` (global pretraining objectives pooled from patch
tokens — the invariance-breaking leak is built in) and `register_equipped`
(4 dedicated register slots host the global computation; patch tokens stay
comparatively clean). H2's directional readout compares VPT gain across the
pair.

## Quickstart

Requires Python ≥ 3.10, CPU only. No GPU, no datasets, no model weights,
no downloads beyond pip packages.

```bash
cd Windows2/_wip/stage7_proto_B0114
pip install torch --index-url https://download.pytorch.org/whl/cpu   # CPU wheel
pip install -r requirements.txt

# main demo: 4 mandated arms x 2 backbones x 3 seeds  (~60 s CPU)
python run_synthetic.py --config configs/default.yaml

# + H's sink-only attention-bias control as a 5th arm   (~75 s CPU)
python run_synthetic.py --config configs/with_sink.yaml

# light conv decoder instead of the linear readout (head-independence check)
python run_synthetic.py --config configs/conv_head.yaml

# options
python run_synthetic.py --config configs/default.yaml --quick           # 1 seed, ~10 s smoke
python run_synthetic.py --config configs/default.yaml --seeds 0,1,2,3,4 # seed override
python run_synthetic.py --config configs/default.yaml --json out.json   # machine-readable dump
python run_synthetic.py --config configs/default.yaml --with-b0001-hook # quarantined B-0001 hook

# tests (39 tests, ~2 s, CPU)
python -m pytest tests/ -q
```

Output is fully deterministic given the config and seeds (verified by
re-running and diffing the JSON dump).

## What the committed configs measured (SYNTHETIC — instrument demo only)

Produced by the exact commands above at the committed seeds (mIoU on held-out
synthetic scenes, mean ± sd over 3 seeds). Reproducible; claims nothing
about real backbones or real dense tasks.

`configs/default.yaml` — per-arm mIoU:

| arm | register_free | register_equipped |
|---|---|---|
| 4 `no_token` | 0.594 ± 0.018 | 0.667 ± 0.033 |
| 1 `frozen_random` | 0.529 ± 0.048 | 0.668 ± 0.033 |
| 2 `learned` | 0.633 ± 0.041 | 0.681 ± 0.015 |
| 3 `learned_frozen` | 0.640 ± 0.031 | 0.680 ± 0.018 |

Gain decomposition (telescoping: insertion + content_transfer +
co_adaptation = total, asserted seed-wise in tests):

| component | register_free | register_equipped |
|---|---|---|
| total VPT gain | +0.040 ± 0.023 | +0.014 ± 0.019 |
| insertion (geometry) | −0.064 ± 0.030 | +0.000 ± 0.002 |
| content transfer | +0.111 ± 0.019 | +0.012 ± 0.017 |
| co-adaptation | −0.007 ± 0.011 | +0.002 ± 0.003 |
| sink geometry (`with_sink.yaml`) | +0.004 ± 0.041 | +0.018 ± 0.018 |

H2 directional readout: gap (gain|free − gain|equipped) = **+0.025 ± 0.042**
— direction positive on synthetic, but *within 3-seed noise*; with the
default budget this is a direction check, not a significance test.

Register signatures & invariance (register_free backbone, means over seeds):

| arm | prompt sink mass | patch-norm outlier frac | nuisance rel. displacement |
|---|---|---|---|
| `no_token` | 0.000 | 0.000 | 0.347 |
| `frozen_random` | 0.305 | 0.003 | 0.482 |
| `learned` | 0.449 | 0.015 | 0.561 |
| `sink_only` | 0.581 | 0.009 | 0.554 |

Readings (all synthetic; none of this transfers to real data by itself):

- **The learned-embedding axis dominates in this sandbox.** Content
  transfer (+0.111) carries essentially the whole register-free VPT gain;
  frozen-random insertion is *negative* (untrained token content injected
  into patch features acts as noise), and the value-zeroed `sink_only` arm
  — which soaks even more attention mass (0.58) than learned tokens — gains
  ≈ 0. So in this sandbox, attention-geometry-only effects do NOT reproduce
  VPT's gain: the dense analogue of Fig. 11 held here. Whether real dense
  tasks behave this way is precisely exp_01's open question.
- **H2 direction appears (register-equipped baseline is higher, VPT gain
  smaller) but is inside seed noise.** The equipped backbone's cleaner
  patch tokens (built in by construction) raise `no_token` from 0.594 to
  0.667 and shrink every component — the qualitative pattern exp_01
  predicts, demonstrated by a sandbox that was *constructed* to contain it.
- **Invariance breaking runs opposite to the naive expectation.** Injected
  tokens made patch features MORE sensitive to the global-nuisance swap
  (0.347 → 0.561), not less: in this sandbox the winning mechanism is
  *routing global illumination information into patch tokens* (which the
  dense head needs), not absorbing it away. The metric dissociates the two
  branches cleanly — that is its job; which branch real backbones take is
  an open empirical question.
- **Signatures behave sanely:** learned tokens attract ~1.5× the sink mass
  of frozen ones; on the equipped backbone, adding prompts *displaces*
  attention mass from the built-in registers (0.068 → 0.043) — a
  register-competition signature the real experiment should look for.

## Dissociation from B-0001 (PI binding)

The PI binding counts B-0114 × B-0001 as one bet unless dissociated; exp_02
mandates that the B-0114 paper make **no uncertainty claims**. Enforcement
in this prototype:

- Norm statistics in `signatures.py` are reported as *register signatures
  only* (norm ratios, outlier fractions) — nothing compares norms to errors.
- The norm-map-vs-error question (B-0001's headline) lives exclusively in
  `src/vpt_registers/b0001_hook.py`, runs only under the explicit
  `--with-b0001-hook` flag, prints under a "B-0001 TERRITORY" banner, and
  no B-0114 module imports it. Both properties are enforced by tests
  (`tests/test_b0001_hook.py::test_dissociation_no_b0114_module_imports_the_hook`,
  `::test_hook_is_flag_gated_in_runner`).
- The hook exists so the *merged-paper branch* of exp_02's pre-registered
  decision rule has a code seam — not to make claims.

## Layout

```
stage7_proto_B0114/
├── README.md                    # this file
├── ARCHITECTURE.md              # mermaid diagram + module map + invariants
├── requirements.txt
├── pyproject.toml               # optional editable install
├── run_synthetic.py             # entry point (EXPECTED vs MEASURED report)
├── configs/
│   ├── default.yaml             # 4 mandated arms x 2 backbones x 3 seeds
│   ├── with_sink.yaml           # + H's sink_only attention-bias control
│   └── conv_head.yaml           # conv decoder head (head-independence)
├── src/vpt_registers/
│   ├── synthetic_data.py        # scenes w/ global illumination nuisance
│   ├── tiny_vit.py              # ViT-tiny, token injection, sink mode, heads
│   ├── config.py                # dataclasses + YAML
│   ├── train.py                 # backbone pretraining + per-arm training
│   ├── metrics.py               # mIoU, decomposition, H2 readout
│   ├── signatures.py            # sink mass, norm signatures, invariance
│   └── b0001_hook.py            # QUARANTINED B-0001 hook (flag-gated)
└── tests/                       # 39 CPU tests, no downloads
```

## From prototype to the real killer experiment (exp_01)

Everything downstream of the sandbox consumes `(features, labels)` through
the same arm interface. To run the real thing:

1. Swap `TinyViT` for frozen DINOv2 / DINOv2-reg (ViT-B) and the synthetic
   generator for ADE20K; keep `train_arm`, `metrics.py`, `signatures.py`.
2. Replace the toy `sink_only` value-zeroing with the exact test-time-
   registers construction (arXiv:2506.08010) for the attention-bias arm.
3. Add exp_01's mandatory extras this prototype does not implement:
   token-count sweep K ∈ {1, 4, 16, 64} (temperature-confound bounding),
   VPT-deep variant, NOP-vs-broadcast token diagnostics (arXiv:2606.08105),
   the classification control tasks (expected to reproduce Fig. 11), and
   3-seed × 24-run protocol on the ViT-B pair.
4. Mandatory citation set: VPT (2203.12119), Darcet (2309.16588), DA-VPT
   (2505.23694), test-time registers (2506.08010),
   Do-All-ViTs-Need-Registers (2603.25803).

## Honesty & limitations

- **Synthetic ≠ evidence.** The sandbox was *constructed* so that global
  aggregation matters for the dense task and so the register-free /
  register-equipped contrast exists. It can validate the instrument and
  falsify implementation bugs, never the scientific claim.
- **The sandbox's own verdict is content-dominant.** If someone wanted this
  prototype to "show" a register effect, it did not: geometry-only arms
  gained ≈ 0 here. That is reported as measured, per the pre-registered
  falsification branch (the dense analogue of Fig. 11 held *in the
  sandbox*).
- **3 seeds is a direction check.** The H2 gap (+0.025 ± 0.042) is inside
  seed noise; the real experiment budgets 3 seeds × 24 runs on real
  backbones for exactly this reason.
- **VPT-shallow only; single K.** Insertion mechanics differ for VPT-deep
  (H's hidden assumption 4) and the temperature confound is bounded by the
  K-sweep — both are real-experiment concerns, listed above.
- **The toy sink arm is not the exact 2506.08010 construction** (it zeroes
  values inside a *shared* softmax rather than adding a calibrated bias);
  it preserves the property that matters for the decomposition — no content
  injection — and is unit-tested against a reference implementation.
