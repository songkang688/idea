# SEG-0046-M (revived) — 3-day public-data killer

**Claim:** transmittance/compositing (soft alpha) supervision beats binary masks for smoke/glass segmentation, and the gain scales with the object's transparency.
**Status:** Stage 3 killed the framing paper; this is a kill-or-promote gate only.

## Prior-art warning (read before spending GPU)

- SMOKE5K's own paper *is* transmission-guided smoke segmentation (Yan, Zhang, Barnes, "Transmission-Guided Bayesian Generative Model for Smoke Segmentation," AAAI 2022).
- The matting literature *is* compositing supervision (Deep Image Matting / Composition-1k, CVPR 2017; TransMatting / Transparent-460, ECCV 2022).

0046-M survives only as (i) the controlled causal comparison at matched everything, and (ii) the **transparency-scaling law**. Not as "we invented transmittance supervision."

## Verified public data (all real; nothing else may be cited)

| Source | Supervision | Role |
|---|---|---|
| Transparent-460 (Cai et al., ECCV 2022): 410 train + 50 test alpha mattes, highly transparent objects | GT alpha | glass-leg train + internal test |
| Composition-1k (Xu et al., CVPR 2017), transparent-foreground subset | GT alpha | glass-leg train; 1,000-composite test for stratified stats (cluster-bootstrap by foreground) |
| AIM-500 (Li et al., IJCAI 2021): 34 transparent / 43 STM-type real photos | GT alpha | real-image (non-composite) eval |
| Trans10K (Xie et al., ECCV 2020); GDD (Mei et al., CVPR 2020) | binary only | external transfer eval, glass |
| SMOKE5K (AAAI 2022): 1,400 real + 4,000 synthetic, binary pixel masks; 400-image real test incl. 100 "difficult" | binary only | external transfer eval, smoke |
| Foggy Cityscapes (Sakaridis et al., IJCV 2018): transmittance analytic, t = exp(−β·depth) | GT transmittance | participating-medium leg train |

Smoke alpha does not exist publicly; the smoke/fog leg trains on Foggy Cityscapes transmittance and transfers to SMOKE5K real test (fog→smoke gap acknowledged). Optional stronger variant: self-composited Blender smoke renders with known alpha over COCO backgrounds (our own compositing procedure, not a named dataset).

## Design (single GPU, 3 days)

**Arms** — identical architecture (SegFormer-B0), schedule, augmentation; 3 seeds:

- **A:** binary masks = alpha thresholded at 0.5 (BCE + Dice).
- **B:** alpha/transmittance regression (L1 + gradient loss).
- **C (decisive control):** Gaussian-softened version of A's binary mask, entropy-matched to B's labels — separates true compositing structure from generic soft-label regularization.

**Evaluations:**

- **E1 internal:** Transparent-460 test + AIM-500 transparent/STM slices; common currency = threshold all arms at 0.5 → IoU + Boundary IoU (plus SAD/MSE for B).
- **E2 scaling law (the core claim):** stratify test objects by mean opacity (mean alpha over FG); Δ(B−A) per stratum; Spearman ρ of per-image Δ vs (1 − mean alpha), bootstrap 95% CI, paired per-image design pooled over seeds.
- **E3 external utility:** transfer to Trans10K test, GDD test (glass) and SMOKE5K 400-image real test incl. the 100-image difficult subset (fog-trained twins).

**Schedule:** day 1 — data prep, arms A/C; day 2 — arm B, remaining seeds; day 3 — eval + stats.

## Kill conditions (any one kills)

- **K1:** Δ(B−A) ≤ 0 in the highest-transparency stratum — no gain where the theory is strongest.
- **K2:** scaling fails — Spearman CI includes 0 or the trend is non-monotone: the "-M" mechanism dies even if B > A on average.
- **K3:** B ≈ C — entropy-matched blurred binary does as well; gains are generic soft-label smoothing, not compositing structure. (Predicted most likely outcome.)
- **K4:** no transfer gain on any binary benchmark (Trans10K, GDD, SMOKE5K-real) — the effect survives only as a matting-internal fact already owned by the matting literature; not a paper.

**Confounder guard:** composite artifacts (halo exploitation) — mitigated by E1 including AIM-500 real photos and E3 being entirely real-image benchmarks.
