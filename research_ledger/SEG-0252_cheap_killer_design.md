# SEG-0252 — Cheap killer experiments (response to R2)

**Claim:** SAM-assisted labeling amplifies mask conventions across annotation generations; drift is inherited by students; an intervention can halt it.
**R2 objection:** requires real annotators for ≥2 generations (expensive).

## Reframing that answers R2

Decompose the claim into falsifiable units:

- **C1 (imprinting):** assist tool biases masks toward its conventions (boundary tightness, hole handling, part inclusion — handles/straps, occlusion completion).
- **C2 (amplification):** labels from generation k, used to retrain the assist model for generation k+1, grow the bias.
- **C3 (inheritance):** students trained on gen-k labels reproduce the drifted conventions on held-out data.
- **C4 (halting):** an intervention (GT anchor replay, assist randomization) stops the growth.

Per-cycle loop gain g ≈ ρ_H · ρ_M, where ρ_H = human transmission of assist conventions
(measurable in **one** generation) and ρ_M = model inheritance of label conventions (measurable with **zero** humans).
Directional amplification requires signed bias with g near/above 1. Multi-generation human cohorts are needed
only for showcase, not for falsification.

## (a) Fully synthetic generations — upper bound on drift

- **Gen-0 GT:** LVIS + HQSeg-44K (high-precision masks); pre-registered **convention probe set** (handles, thin structures, occlusions, holes) where the GT convention is documented.
- **Loop (5 generations, 3 seeds):** fine-tune assist model A_k (LoRA on SAM's mask decoder, or a promptable SegFormer-B0 student) on labels L_{k−1}; propose on **fresh images each generation**; a simulated annotator with anchoring parameter creates L_k: accept proposal if IoU ≥ τ, else apply e boundary-correction edits toward GT (simulated-click protocol as in interactive-segmentation evaluation, e.g. RITM/SimpleClick).
- **Sweep anchoring** from accept-all (pure self-training) to perfect-corrector. Accept-all is the theoretical maximum of convention transmission — real humans lie strictly inside this curve, hence *upper bound*.
- **Metrics (convention, not quality):** signed boundary displacement (px, via distance transform), part-inclusion rate on probes, hole-fill rate, masks-per-image granularity, Boundary IoU vs mask IoU divergence. Drift = monotone trend of **signed** metrics across generations (Mann-Kendall / mixed model over seeds).
- **Cost:** decoder-LoRA fine-tunes on ~10k masks/generation; single GPU, a few GPU-days. No humans.

## (b) Cheapest human protocol that still tests anchoring (one generation)

- **N = 12 annotators × 60 images × 3 conditions** (~2,160 masks, ~40–70 annotator-hours; low-four-figure crowd budget vs. tens of thousands for a 2-generation cohort).
- **What they label:** LVIS-style ambiguous-convention probes (mugs with handles, occluded objects, thin structures, containers with holes).
- **Conditions (within-subject, Latin-square order, annotators blind to variant):**
  1. scratch (brush/polygon, no assist);
  2. assist = vanilla SAM;
  3. assist = "drifted SAM" — same model fine-tuned to carry a known injected convention (e.g., +3 px dilation, hole filling, handle exclusion; produced by the loop in (a), so the injected bias is exactly the kind the loop generates).
- **Measure per convention axis:** transfer coefficient ρ_H = (bias₃ − bias₂) / injected bias; secondary: fraction of proposals accepted unedited, edit time. Mixed-effects model with annotator random effect.
- **Interpretation:** ρ_H ≈ 0 ⇒ humans erase conventions ⇒ amplification impossible ⇒ 0252 dead. ρ_H substantial ⇒ combine with ρ_M from (a) for the loop-gain estimate.

## (c) Results that kill 0252 with no humans at all

- **K1:** accept-all loop shows no directional convention trend over 5 generations (signed biases oscillate within seed noise) ⇒ C2 dead at every anchoring level.
- **K2:** students trained on gen-5 vs gen-0 labels are indistinguishable on convention probes ⇒ C3 dead.
- **K3:** observed drift is fully absorbed by the collapse controls below (no signed, convention-specific component) ⇒ the claim reduces to known self-training degradation ⇒ no paper.
- **K4:** interventions fail to reduce drift in the regime where synthetic drift is largest ⇒ C4 (the actionable half) dead.

Any of K1–K3 kills the hypothesis; K4 kills only the intervention claim.

## (d) Confounders — model collapse ≠ convention amplification

- **Signature difference:** collapse = loss of diversity/variance (blurred boundaries, mode dropping, entropy decrease), roughly isotropic; convention amplification = **signed, structured** bias that can grow while mIoU stays flat.
- **Controls:**
  1. bias/variance decomposition of boundary error per generation;
  2. **frozen-assist control** — vanilla SAM every generation, no retraining: residual drift = one-shot imprinting; amplification requires drift(loop) > drift(frozen);
  3. **GT-retrain control** — assist retrained each generation on gen-0 GT (breaks label inheritance, keeps repeated model mediation);
  4. fresh images per generation (removes overfitting-driven collapse);
  5. **unbiased-noise control** — inject symmetric boundary noise of matched magnitude: students must inherit conventions, not noise level.
- Fix the simulated edit budget across generations (real pipelines drift in effort too — separate phenomenon). Pre-register probe conventions to avoid post-hoc convention hunting.

## Honest limit

The cheap program **can falsify** 0252 and can measure every parameter of the amplification model, but it **cannot positively confirm** that real human pipelines amplify over ≥2 generations: ρ_H is measured against injected conventions in a single round, and composing ρ_H · ρ_M assumes loop stationarity. If everything survives, the flagship human claim still requires one real 2-generation study — now de-risked, with measured effect sizes for the power analysis. Cheap falsification: yes. Cheap full confirmation: no.
