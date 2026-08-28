# exp_09 — C-0082-mut: a SAM failure-prediction law from computable image properties (L revive)

**ID:** W2-C-0082-mut (D's mutation: "atlas exists piecewise; survive only as a validated quantitative failure-prediction law").
**Pipeline status:** D MUTATE (atlas dead: concealed-scenes arXiv:2304.06022, SAM-Adapter ICCVW 2023, et al. — all KNOWN) → mutation lost its slot in G's merge machinery → never attacked by K (K covered the C LOCK set only) → L revive #4, with mandatory fresh scoop-check.

## Fresh scoop-check (this session — the check L mandated)

Live search found the space **more crowded than L's revive assumed**: (1) **RUAC** (ICML 2026, arXiv:2605.10603) — learned pixel-wise uncertainty head for SAM with robust uncertainty-accuracy correlation across 23 zero-shot domains; (2) **TCSR-Monitor** (public repo, surgical video) — post-hoc learned failure monitor for frozen segmenters incl. SAM2 from observable shape/temporal/quality features with conformal alarms; (3) Stable-SAM (ICLR 2025) — prompt-quality instability analysis; (4) GleSAM (arXiv:2503.12507) — low-quality-image robustness. **EVIDENCE: learned failure monitors and uncertainty heads exist. Not found: a zero-training, interpretable LAW mapping computable image properties → failure probability, fitted and validated across held-out domains on frozen SAM.** The wedge narrows to: interpretability + zero-training + cross-domain extrapolation, and the killer experiment must now include a **learned-monitor baseline** — if XGBoost-on-features beats the law by a wide margin everywhere, the law is a worse monitor, and only its scientific reading (capability-boundary characterization) survives.

## Research question

Can SAM/SAM2 failure probability (mask IoU < τ against expert GT) be predicted *before inference* by a small, interpretable set of computable image properties (contrast, clutter/edge density, boundary complexity, object scale, sensor type) — a law that extrapolates to unseen domains?

## Falsifiable hypothesis

H1: a ≤6-term regression on computable properties predicts per-image failure with AUROC substantially above a domain-identity baseline **on held-out domains never used in fitting**.
H2: the law's coefficients are stable across SAM variants (the boundary is a property of the training distribution/task, not the checkpoint).
Falsified if: held-out-domain AUROC ≈ domain-identity baseline (the "law" merely memorizes domains — atlas redux), or coefficients flip sign across variants (no law, just per-model quirks).

## Prediction

HYPOTHESIS: within photographic domains, contrast + boundary complexity + object scale carry most of the predictable variance; non-photographic sensors (ultrasound, EM) sit off the law — and the *structured residual* is itself the capability-boundary finding (where SAM fails for reasons pixels don't explain).

## Method sketch

Inference-only. Modules: (1) **property extractor**: local contrast at GT boundary, global clutter (edge density), boundary tortuosity/fractal dimension, object relative scale, texture similarity fg/bg, sensor/domain tags; (2) **SAM harness**: SAM + SAM2 (2 sizes each), fixed prompt protocols (center point, box, 3-click) — prompt policy is a confound, so it is a *factor*, not a constant; (3) **law fitter**: regularized logistic regression / GAM on N fit domains; (4) **validation**: strict leave-domain-out on ≥2 held-out domains; (5) **learned-monitor comparator** (new, mandated by scoop-check): gradient-boosted model on the same features + TCSR-style observable features — the interpretability-vs-accuracy frontier is reported honestly; (6) **constructive readout**: a pre-inference routing rule (send predicted-failure images to human/other model) evaluated on the held-out domains.

## Data

7–9 public domain-shifted segmentation datasets with expert GT spanning: natural (COCO/LVIS subset), camouflage (concealed-scenes line, KNOWN per D), medical (2 modalities), aerial, industrial defect, EM/microscopy. Fit on ~5, hold out ≥2 (one photographic, one non-photographic).

## Baselines

Domain-identity oracle (upper bound for memorization); SAM's own predicted-IoU head (the model's self-estimate — must be beaten or complemented); mask-quality post-hoc signals (entropy of mask logits); the learned monitor (frontier comparator); trivial object-scale-only law.

## Metrics

Held-out-domain AUROC/AUPRC per prompt protocol; calibration of predicted failure probability; coefficient stability across SAM variants; routing-rule utility (failure caught per image deferred).

## Killer Experiment

**Fit the ≤6-term law on 5 domains, validate on 2 held-out domains, against the domain-identity and predicted-IoU baselines.** Pure inference + regression: **2–4 GPU-days.** The held-out-domain AUROC against the two baselines decides between law / atlas-redux / SAM-already-knows.

## GPU/VRAM/time estimate

SAM/SAM2 inference over ~50–100k masks across 9 datasets: **2–4 GPU-days on one 24GB GPU** (SAM2 is fast; batching amortizes). Analysis CPU. Full study with prompt-protocol factor and learned-monitor frontier: ≤1.5 GPU-weeks.

## Stop / pivot / kill criteria

- **Kill** if held-out AUROC ≤ domain-identity baseline (no law) or if SAM's own predicted-IoU head already achieves the law's AUROC pre-inference-equivalent (the model self-reports its boundary; nothing to add).
- **Pivot** to "the interpretable capability-boundary study" if the learned monitor dominates predictive accuracy by a wide margin: the law's value is then scientific (which properties bound SAM) not operational, and the paper shrinks to an analysis note — publish only if coefficient structure is clean.
- **Stop** if a computable-properties failure-law paper for SAM appears (this space produced 4 adjacent papers since D's review; re-search at proposal AND freeze — highest scoop hazard in this set after C-0306).

## Reviewer-2 leftover

"You built a worse failure monitor than a learned one and called it a law" — survivable only via the interpretability/extrapolation framing and the routing utility on unseen domains. GT-quality heterogeneity across the 9 datasets injects label noise into the failure labels themselves (the C-batch GT-epistemology problem, recursively); report per-dataset noise sensitivity.

## Expected result (HYPOTHESIZED, not measured)

Law holds within photographic domains, degrades gracefully on the photographic hold-out, breaks on the non-photographic one — and the break-point is the quotable capability-boundary statement.

## Negative-result interpretation

If failure is unpredictable from image properties, SAM's failure boundary is intrinsically model-internal (prompt- and decoder-dependent) — an argument *for* learned monitors and predicted-IoU heads, and a clean negative for the "capability boundaries are image-legible" intuition the atlas literature implicitly assumes.
