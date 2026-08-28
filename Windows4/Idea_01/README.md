# Idea_01 — SeeingInside

**Does SAM see inside a tight box, or does it interpolate the box into a mask?**

| Field | Value |
|---|---|
| Windows | Windows4 |
| Idea slot | Idea_01 (recommended #1, Stage 6 lock) |
| Project ID | P14 |
| Source idea IDs | S-014 (image-evidence ablation inside tight box), S-604 (patch-shuffle mutation) |
| Stage-3 verdict | SURVIVE (`selection_history/stage3_kill_sam_eval.md`, Cluster 2) |
| Stage-4 verdict | WEAK ACCEPT rank 1 of 20, conditional on the Reviewer-#2 redesign (`selection_history/stage4_r2_setA.md`, P14) |
| Stage-6 lock | Idea_01, vision-only; explicitly **NOT merged** with P107v / HalluSegBench (`selection_history/stage6_battle.md`) |
| Status | Stage 7 package — proposal + runnable prototype. **No scientific results yet.** |

## One paragraph

When SAM receives a tight bounding box, how much of its output mask is driven by image
evidence, and how much by the box geometry itself? We answer this with **on-manifold
counterfactuals**: hold the prompt fixed, and change *what is inside the box* by inpainting
the object out or swapping a different object in — natural images in, natural images out.
Every score is calibrated against three **no-image-evidence nulls**: a per-instance
convexity-matched box-fill, a *prompt-only* SAM forward (image embedding replaced by a
dataset mean), and a small *learned box→mask regressor* that never observes pixels. The
primary endpoint is the low-contrast medical regime, where tight-box prompting is the
deployed protocol (MedSAM-class evaluation): we report **what fraction of box-prompt Dice
is reachable with zero image evidence**. Off-manifold probes (patch-shuffle S-604,
embedding-mean S-014) are demoted to secondary convergence checks, exactly as Reviewer #2
required.

## Directory map

```
Idea_01/
├── README.md                 ← you are here
├── proposal.md               ← full 28-section research proposal
├── literature.md             ← verified citations only (Stage-3 list + Kirillov et al.)
├── experiments.md            ← experiment cards E0–E7, pre-registered thresholds
├── reviewer_attacks.md       ← Reviewer-#2 attacks and how each is answered
├── roadmap.md                ← execution order, decision tree, backup plan
├── diagrams/architecture.md  ← mermaid diagrams of pipeline + decision logic
├── configs/default.yaml      ← single source of truth for the prototype
├── requirements.txt
└── src/                      ← runnable prototype (killer experiment E0/E1 scaffold)
    ├── __init__.py
    ├── utils.py              ← metrics (Dice/IoU/boundary-F), box ops, convexity, contrast
    ├── dataset.py            ← synthetic controllable dataset + COCO/medical interfaces
    ├── model_sam.py          ← PromptableSegmenter interface, official-SAM wrapper,
    │                            BoxFillBaseline stub, OracleThreshold stub, learned null
    ├── interventions.py      ← object-out inpaint, object swap, patch shuffle, nulls
    ├── losses.py             ← Dice+BCE for the learned box→mask null
    ├── train.py              ← trains the learned no-image null
    ├── eval.py               ← killer-experiment runner (conditions × paddings → report)
    └── inference.py          ← single-image demo
```

## Quick start

```bash
pip install -r requirements.txt        # numpy+pyyaml mandatory; torch/cv2 optional-graceful

# Smoke test of the full killer-experiment pipeline on synthetic data with stubs
# (validates the decision logic on a known interpolator and a known "seeing" model):
python -m src.eval --config configs/default.yaml

# Train the learned box→mask no-image null (requires torch):
python -m src.train --config configs/default.yaml

# With official SAM weights (when available):
#   pip install git+https://github.com/facebookresearch/segment-anything.git
#   download sam_vit_h_4b8939.pth (or vit_b), then:
python -m src.eval --config configs/default.yaml \
    --override model.backend=sam model.sam_checkpoint=/path/to/sam_vit_b_01ec64.pth
```

## Epistemic status

Per the Windows4 ledger, every claim in this package is tagged
`KNOWN FACT | EVIDENCE | HYPOTHESIS | MODEL SPECULATION | EXPECTED RESULT | ACTUAL EXPERIMENTAL RESULT`.
**There are no scientific ACTUAL results in this package.** The only ACTUAL items are
pipeline smoke-test outputs on synthetic data with stub models, used to validate the
decision logic (see `experiments.md` §E0). All performance statements about SAM are
EXPECTED or HYPOTHESIS.

## Binding obligations (from Stage 4, non-negotiable)

1. On-manifold inpaint/swap counterfactuals are the **primary** intervention.
2. Prompt-only null and learned box→mask null are **mandatory** comparison arms,
   convexity-matched per instance.
3. Embedding-mean (S-014) and patch-shuffle (S-604) are **secondary** convergence checks only.
4. Low-contrast medical (MedSAM protocol) is the **primary endpoint**.
5. **No merge** with P107v / HalluSegBench: this project intervenes on *pixels inside a box
   prompt* for a promptable segmenter; it makes no VLM/hallucination claim.
