# Idea_02 — Spectral Locality of Dense PEFT

Status: HYPOTHESIS. No measured FFT results.

## Executive summary

**One sentence:** LoRA (and related PEFT) on SAM/ViT encoders for segmentation is a **spatial low-pass adapter**: extra rank buys Dice on large organs, not boundary frequencies — so a tiny high-frequency residual adapter should beat a larger LoRA rank on NSD at matched parameter count.

## Motivation

KNOWN FACT: LoRA (Hu et al., ICLR 2022) is used in SAMed / LoRA-MedSAM for medical SAM. EVIDENCE: those papers report Dice/time, not a spectral decomposition of the adapter delta.

Community assumption: higher rank ≈ more capacity ≈ better segmentation.

## Problem

Let \(W\) be a frozen weight, \(\Delta = BA\) LoRA. Let \(\delta(x) = f_{W+\Delta}(x) - f_W(x)\) at a chosen feature map. Analyze the 2D power spectrum of \(\delta\).

## Hypotheses

**H1:** For organs/lesions, \(\geq 80\%\) of \(\|\delta\|_2^2\) energy lies below a cutoff \(k_c\) too coarse for 1-pixel boundaries (cutoff chosen from patch size; pre-register \(k_c\)).

**H2:** Rank 64 vs rank 4 does not move energy above \(k_c\) (rank ≠ frequency).

**H3:** Adding a depthwise high-pass residual (DoG / Laplacian conv, few k params) improves NSD more than increasing LoRA rank by the same parameter budget. Dice may be unchanged.

## Novelty

| Closest | Difference |
|---------|------------|
| LoRA-MedSAM / SAMed | Efficiency + Dice, no spectrum |
| Med-SA | Adapter design, not frequency diagnosis |
| Fourier / FNet / spectral CNN papers | Not about PEFT deltas on SAM |

Exact difference: **the object of study is \(\delta(x)\), not a new SOTA adapter**, unless H3 holds.

## Method

1. Fine-tune LoRA on a small organ set (Synapse/AMOS subset).
2. Cache \(\delta\) on 64 images.
3. Radial power spectrum; energy fraction \(<k_c\).
4. If H1–H2: train HighPassResidual (depthwise 3×3 Laplacian + 1×1) with LoRA rank 4 vs LoRA rank 64.

\[\Delta W = BA, \quad y = W x + \alpha BA x + \gamma \mathrm{HP}(x)\]

## Killer experiment

One GPU: LoRA-r4 vs LoRA-r64 vs r4+HP on 64 images. Report Dice **and** NSD **and** spectral energy. Stop if H1 false (LoRA already high-pass).

## Expected (not measured)

Dice: r64 ≈ r4+HP > r4. NSD: r4+HP > r64 ≥ r4. Spectrum: r64 still low-pass.

## Reviewer #2

“Low-rank implies low frequency” is false in general (rank and spatial frequency are different). The paper must show the empirical coupling and that HP is not just “another convolution module.” Control: low-pass residual with same param count should **hurt** NSD if the story is frequency.

## Compute

Killer < 1 GPU-day. Full Synapse/AMOS 3–5 days.
