# Windows4 / Idea_03 — AlphaSmoke

**Matting-provenance transfer to smoke (P103) + the smoke metric-validity protocol
(P096), one Stage-7 package.**

- Final-3 lock: `../selection_history/stage4_top20.md` (Idea_03), decided in
  `../selection_history/stage6_battle.md`.
- Reviewer-#2 verdicts absorbed: P103 WEAK ACCEPT (conditional,
  `stage4_r2_setA.md`), P096 SILENCED with measured-alpha arm mandatory
  (`stage4_r2_setC.md`).
- **Epistemic status: PLAN.** No experiment has been run. This package contains no
  measured results; all numbers are budgets, pre-registered thresholds, or predictions
  tagged as such. Claims carry `KNOWN FACT | EVIDENCE | HYPOTHESIS |
  MODEL SPECULATION | EXPECTED RESULT` tags; the `ACTUAL EXPERIMENTAL RESULT` tag
  appears zero times.

## TLDR

Smoke's true ground truth is an alpha/transmittance field, but the field trains and
ranks on binary masks. AlphaSmoke asks two coupled questions with one instrument set:

1. **Transfer (P103):** does alpha-matting pretraining beat COCO-segmentation
   pretraining on real smoke — with the soft-label mechanism isolated by a
   **binarized-matting arm** (same images, same budget, softness destroyed)?
   Primary endpoint on **real smoke**; week-1 frozen-encoder linear probe gates all
   training spend.
2. **Metric validity (P096):** do binary metrics (IoU/Dice/**Fβ/mMse**) and alpha
   metrics (MAE/SAD/Grad/Conn) rank models differently (Kendall-τ matrix + top-3
   reversals) — anchored by a **measured-alpha real test set** recovered by
   compositing inversion against known pre-smoke backgrounds, and bounded by a
   **multi-rater ceiling** study with a pre-registered demotion rule?

Training-free **color/physics floors** (dark channel, HSV low-chroma rule) gate every
learned claim. Hard scope guard: this is **not** a detector-prompted fire/SAM2
pipeline (S-126 was folded elsewhere at Stage 3).

## Binding obligations (B1–B10)

Defined with sources in `proposal.md` §2: binarized-matting arm (B1), real-smoke
primary endpoint (B2), measured-alpha arm (B3), mMse/Fβ columns (B4), rater ceiling
with demotion rule (B5), physics floors (B6), head-alignment control (B7), matched
budgets (B8), SFMattingNet in pool (B9), no-detector scope guard (B10).

## Package contents

```
Idea_03/
├── README.md                  ← you are here
├── proposal.md                ← full Stage-7 proposal, hypotheses H1–H4, arms, mermaid overview
├── experiments.md             ← pre-registration: endpoints, kill conditions K-A1..K-B5, decision tree (mermaid), runbook
├── metrics_protocol.md        ← exact metric definitions, τ protocol, alpha-recovery math, ceiling method
├── datasets.md                ← dataset/checkpoint inventory with honest UNVERIFIED access marks
├── reviewer_attacks.md        ← every R2 attack → design answer; residual risks
├── CITATIONS.md               ← citation register with [V]/[S3]/[M] verification tags
├── literature.md              ← narrative literature notes (register: CITATIONS.md)
├── roadmap.md                 ← gate-ordered execution roadmap
├── diagrams/architecture.md   ← architecture-level mermaid
├── references/                ← reviewer-facing reference notes
├── requirements.txt
├── configs/
│   ├── default.yaml           ← index of the task configs below
│   ├── pretrain_arms.yaml     ← arms M / MB / S / S+cal / 0 (B1, B7, B8)
│   ├── datasets.yaml          ← paths + roles (all paths TODO until R0)
│   ├── eval_protocol.yaml     ← metric columns incl. mMse/Fβ (B4), τ spec, kill thresholds, pool spec (B9, B10)
│   ├── linear_probe.yaml      ← week-1 killer experiment
│   ├── rater_study.yaml       ← 3–5 raters × 150 images (B5)
│   └── alpha_capture.yaml     ← measured-alpha capture + QC (B3)
├── src/hsv_baseline.py        ← compatibility shim → alphasmoke.baselines.color_hsv
├── src/metrics_alpha.py       ← compatibility shim → alphasmoke.metrics
├── src/probe.py               ← compatibility shim → alphasmoke.probes
├── src/alphasmoke/
│   ├── metrics/
│   │   ├── alpha_metrics.py       ← MAE/SAD/MSE/mMse/Grad/Conn (Rhemann suite)
│   │   ├── binary_metrics.py      ← IoU/Dice/Fβ/boundary-F
│   │   └── rank_agreement.py      ← sign-aligned Kendall τ matrix, reversals, bootstrap CIs
│   ├── baselines/
│   │   ├── color_hsv.py           ← HSV low-chroma smoke rule (B6)
│   │   └── dark_channel.py        ← dark-channel transmission floor (B6)
│   ├── alpha_recovery/
│   │   └── background_inversion.py ← measured-alpha recovery + validity/sensitivity masks (B3)
│   ├── probes/
│   │   └── encoder_linear_probe.py ← frozen-encoder 1×1-conv probe stub (torch; checkpoints are stubs)
│   └── rater/
│       └── ceiling.py             ← pairwise IoU / alpha-MAE ceilings + confrontation table (B5)
└── tests/
    └── test_selfchecks.py     ← unit self-checks on synthetic arrays (NOT experiments)
```

## Running the self-checks

```bash
cd Windows4/Idea_03
pip install -r requirements.txt   # numpy/scipy/pyyaml; torch optional (probe only)
python -m pytest tests/ -q        # or: python tests/test_selfchecks.py
```

The tests verify metric implementations on synthetic arrays (identity → perfect
scores, constructed reversals detected, known-alpha composites recovered). They are
code-correctness checks, **not** experimental results.

## What runs first

Per `experiments.md` runbook: R0 license audit → R1 metric cross-check against
released FoSp/SMOKE5K eval code → **R2 week-1 linear probe** (gates all pretraining
spend, kill K-A1) → R3 eval-only τ matrix on synthetic alpha. The training-heavy arm
grid is funded only if the probe shows separation.
