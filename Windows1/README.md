# Windows1 — Research Idea Evolution

- **Windows number:** 1 (no prior Windows directories in this repository)
- **Created:** 2026-08-28
- **Supervisor identity:** Windows1
- **Repo:** `songkang688/idea`

## This round's three ideas

| ID | Short name | One-sentence idea | Status |
|---|---|---|---|
| **Idea_01** | **RetainSAM** | Fine-tune SAM on a target domain **subject to a promptability-retention constraint**, and require the method to **strictly dominate WiSE-FT interpolation** on a prompt-behavior Pareto front. | Ready for killer experiment |
| **Idea_02** | **LesionSuppress** | Measure **lesion-suppression probability** as a function of size, contrast, and enhancement strength; validate rank-order against real LIDC small nodules; drop any “universal law” claim unless it survives. | Ready for killer experiment |
| **Idea_03** | **DisagreeShift** | Train **pixelwise uncertainty fields on inter-rater disagreement** and test whether they keep **ordering-sensitive** meaning under scanner/stain shift, where hard labels + temperature scaling structurally cannot. | Ready for killer experiment |

## #1 recommendation

**Idea_01 RetainSAM.**

It is the only method-building project in the final three, it has the cheapest decisive falsifier (WiSE-FT must be beaten), and a failure still leaves a reusable promptability-retention benchmark. If WiSE-FT already traces the Pareto front, kill Idea_01 in week 1 and promote Idea_03 to #1.

## First experiment to run

**RetainSAM kill test (Week 1):**

1. Fine-tune SAM ViT-B on one medical set (Kvasir-SEG or ISIC) with a standard recipe.
2. Interpolate `θ(α) = (1−α) θ_SAM + α θ_FT` for α ∈ {0, 0.1, …, 1} (WiSE-FT).
3. Evaluate target Dice **and** a frozen promptability suite (1/3/5-click mIoU, box prompt, iterative NoC) on COCO/LVIS held-out images.
4. Train the constrained objective once.
5. **Kill Idea_01** if constrained FT does not strictly dominate interpolation at ≥2 operating points.

## Next experiments (if Idea_01 survives or is killed)

- In parallel (low GPU): Idea_02 synthetic-vs-LIDC rank correlation on one lesion family; Idea_03 LIDC sparsification vs hard-label+TS on a held-out scanner.

## Portfolio composition (why not three eval papers)

Stage 6 locked **method + medical-safety characterization + medical uncertainty method**. Runner-up **SEG-0276-M** (prior-shape interpolation α) is HRHR and inference-only; revive it if Idea_01 dies to WiSE-FT *and* Idea_03’s TS baseline unexpectedly matches.

## Epistemic rules used in this folder

KNOWN FACT, EVIDENCE, HYPOTHESIS, MODEL SPECULATION, EXPECTED RESULT, and ACTUAL EXPERIMENTAL RESULT are labeled. **No numbers in this archive are measured by us.** Predicted curves are EXPECTED only.
