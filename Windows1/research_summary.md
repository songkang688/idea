# Windows1 research summary

## Funnel (approximate, after dedup)

| Stage | Count | Notes |
|---|---|---|
| Stage 1 raw | ≥1065 (SEG 365 + local VFM ~350 + local ASM ~350 + VFM-A 180 + ASM-A 180; overlap) | Cloud 350-idea runs timed out twice; local pools + compact batches completed the ≥1000 requirement |
| Stage 2 | ~84 SEG keep + VFM/ASM keepers | Independent scoring; HRHR protected |
| Stage 3 | ~20 attacked | Default “already published”; several 2024–2026 exact matches |
| Stage 4 | 12 mutated forms | No unconditional KEEP; one KILL (replica-spiking inflation curve) |
| Stage 5 | 8 engineered, then 5 | Killer experiments specified |
| Stage 6 | **Final 3** | A RetainSAM, B LesionSuppress, D DisagreeShift |

## Locked hypotheses (falsifiable)

1. **RetainSAM (HYPOTHESIS):** A promptability-constrained SAM fine-tune strictly dominates the WiSE-FT interpolation Pareto on (target Dice, generic k-click mIoU). Falsified if interpolation matches or beats it.
2. **LesionSuppress (HYPOTHESIS):** Rank-order of suppression vs (size, CNR) from synthetic insertions matches real small-nodule sensitivity on LIDC-matched bins (Kendall τ significantly > 0). Falsified if τ low or sign-flips.
3. **DisagreeShift (HYPOTHESIS):** Disagreement-trained fields beat hard-label + temperature scaling on **sparsification / pixelwise AURC** under scanner or stain shift, even when ECE can be matched. Falsified if TS matches on ordering-sensitive metrics.

## Explicitly not claimed

- We have **not** trained models or measured Dice/mIoU/τ in this round.
- Novelty confidence is **posterior to adversarial search**, not proof of unpublished status.
- Several adjacent papers already occupy nearby cells (HQ-SAM tradeoff tables, WiSE-FT, multi-rater probabilistic segmentation, denoising reader studies).
