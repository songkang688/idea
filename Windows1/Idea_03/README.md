# Idea_03 — DisagreeShift

**Candidate titles**

1. Disagreement Fields that Travel: Pixelwise Rater Variability under Scanner and Stain Shift
2. Temperature Scaling Cannot Reorder Pixels: Why Soft Multi-Rater Training Matters OOD
3. Calibration that Means Something: Sparsification of Segmentation Uncertainty under Shift

## 1. Executive summary

Train segmentation **probability fields on inter-rater distributions** (not majority-vote hard labels). Evaluate with **ordering-sensitive** metrics (sparsification / pixelwise AURC) under **scanner or stain shift**. The kill baseline is hard-label training + temperature scaling (Guo et al., 2017). TS is a **single scalar** and cannot reorder pixels; if it still matches AURC, our training did not produce a better **ranking** of errors, and the project dies.

Original SEG-0074 (histo-validated infiltration maps) was **killed** by existing MRI–histo pipelines. This mutation is a different question: **does disagreement-shaped uncertainty transfer when accuracy does not?**

## 2. Motivation

KNOWN: Probabilistic U-Net, stochastic segmentation networks, LIDC 4 raters, QUBIQ. Community default: report Dice on consensus and maybe ECE. HYPOTHESIS: ECE can be fixed by TS even OOD, while **where** the model is unsure (rater-conflict regions vs random boundaries) does not transfer unless trained on disagreement.

## 3. Problem definition

For image x, raters {y^{(r)}} give a per-pixel frequency f(x)_i ∈ [0,1]. Learn p_θ(x)_i. Under domain shift T(x), compare:

- Dice vs majority vote
- ECE / NLL vs f
- **Sparsification:** remove the k% most-uncertain pixels, measure remaining Dice/error; AURC

## 4. Core hypothesis

**H1:** Under held-out scanner (LIDC) or stain/site (pathology), disagreement-trained p_θ has **lower sparsification error / better AURC** than hard-label + TS, at matched Dice.

**H2:** The gap is larger in bins of high rater entropy.

Kill if TS matches AURC on the primary shift. Pivot to selective prediction / deferral if calibration transfers but Dice story is muddy.

## 5. Key insight

TS cannot implement spatial disagreement. If we still lose, either raters’ spatial conflict is not learnable from the dataset size, or shift destroys the features that encode it.

## 6. Novelty

Prob U-Net predicts distributions **in-domain**. Multi-rater papers exist. **Gap:** shift evaluation with a **structurally incapable** baseline (scalar TS) on **ordering-sensitive** metrics. Confidence: Medium-High on the logical gap; Medium on empirical win.

## 7–10.

See literature, diagrams, math:

\[
\mathcal{L}_{\mathrm{soft}} = \mathrm{KL}\big(f \,\|\, \sigma(z_\theta)\big)
\quad\text{or}\quad
\mathrm{BCE}(\sigma(z_\theta), f)
\]

vs hard CE on majority + TS on logits.

Annotator-specific heads (Tanno-style) optional ablation.

## 11–17.

`src/disagree_shift/` metrics + dummy trainer. Killer: LIDC leave-one-scanner-out if metadata allows; else synthetic stain/noise shift on LIDC as **proxy** (declare proxy).

## 18. Expected

EXPECTED: similar Dice drop under shift for hard vs soft; AURC gap favors soft, especially high-entropy pixels. NOT MEASURED.

## 19–22.

Fatal: too few scanners; TS-on-shifted-val as sneaky oracle. Pre-register: TS fitted **only** on source val.

R2: “QUBIQ already.” Response: QUBIQ is in-domain multi-rater; we add **shift + TS kill**.

## 23. Compute

Killer ~4 GPU-days (2D U-Net). Full ~16.

## 25. Stop

Kill H1 fail. Continue if AURC wins on 2 shifts.

## 27. Story

Hard labels plus a thermometer cannot put uncertainty where doctors disagree once the scanner changes; training on disagreement can — or it cannot, and we should stop pretending ECE is the deployment quantity.
