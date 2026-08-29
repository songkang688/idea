# exp_06 — C-0338: the size-resolved human ceiling (crossing-point experiment)

**ID:** W2-C-0338 (hosts the C-0071 consensus-ceiling arm and absorbs C-0007 per K).
**Pipeline status:** D bet #6 → G LOCK (census UPGRADE: LVIS double annotations public) → K SURVIVE-IF-EXPERIMENT (size-resolved crossing-point with census precondition; Label Convergence + Noise-Aware Evaluation must be paragraph-one citations).

## Research question

Below what object size s does human-human annotation agreement fall to the level of model-GT agreement — the size floor beneath which claimed AP-small progress is unfalsifiable on current benchmarks?

## Falsifiable hypothesis

H1: There exists a size bin s* such that for objects below s*, human re-annotation agrees with original GT **no better** than SOTA detectors do (per-size-bin human-GT agreement AP ≤ model-GT AP), while above s* humans dominate clearly.
H2 (claims audit): a measurable share of published AP-small improvement claims fall inside the sub-s* noise band.
Falsified if: human-GT agreement dominates model-GT agreement at ALL sizes (no crossing) — the "small-object gap is real headroom" null, which is itself a strong publishable answer.

## Prediction

HYPOTHESIS: a crossing exists somewhere in the small-object regime; supporting EVIDENCE (not proof): Noise-Aware Evaluation (WACV 2025) shows AP is most distorted for small objects and strict IoU thresholds; TOLF (arXiv:2601.00617) finds ~34.2% of AI-TOD test boxes noisy and 2-px shift → >20% IoU drop at 10×10 px; Label Convergence (arXiv:2409.09412) puts SOTA at the aggregate ceiling already. The size-resolved curve is the unclaimed piece (K: "the one neither WACV paper ran").

## Method sketch

Measurement study. Modules: (1) **size census** of the LVIS double-annotated subset: instance counts per size bin, especially sub-16px (K flags this count as HYPOTHESIS/unverified — hence the precondition); (2) **agreement engine**: treat annotator-2 as "predictor" against annotator-1 GT and compute per-size-bin agreement AP with the same matching pipeline used for models (convention-symmetry: swap annotators and average); (3) **model arm**: per-size-bin AP of SOTA detectors on the identical instances; (4) **crossing-point estimator** with bootstrap CIs over images and annotator pairs; (5) **claims audit**: published AP-small deltas (from papers' own tables) compared against the bin noise band; (6) optional fresh double-annotation of small-object strata only, if the census fails.

## Data

LVIS doubly-annotated subset (public per G census); COCO for the model arm on shared instances; AI-TOD + TOLF's noise findings as the tiny-object extreme anchor. Fresh annotation (contingency): small-object strata only, 2+ annotators, size-stratified sampling — budget-bounded because only sub-32px strata need new labels.

## Baselines

Aggregate (non-size-resolved) ceiling from Label Convergence — the paper must show the size-resolved curve *adds* information beyond it (K's hidden assumption (a)). Model-side: 3+ detectors spanning AP-small performance range. Matching-convention sensitivity arm (IoU thresholds 0.25/0.5/0.75) because at 10×10 px the convention IS the result (TOLF evidence).

## Metrics

Per-size-bin: human-human AP, human-GT AP, model-GT AP with bootstrap CIs; crossing point s* with CI; fraction of published AP-small claims inside the noise band; sensitivity of s* to IoU threshold.

## Killer Experiment

**The census (one day, CPU-only) then the per-size-bin agreement-vs-model curve on existing double annotations.** No training anywhere. The single figure (three curves vs size, with CIs) is the paper; the crossing point either exists with a CI or provably doesn't.

## GPU/VRAM/time estimate

GPU: **1–2 GPU-days** (inference of 3+ detectors on the shared instance set; cached predictions may reduce this to hours). Everything else CPU. Contingent annotation budget: small-strata double labels (~thousands of instances, days of annotator time) only if the census fails. Cheapest killer experiment in the C batch after the census gate.

## Stop / pivot / kill criteria

- **Precondition stop:** if the LVIS census shows too few sub-16px doubly-annotated instances AND no annotation budget → pivot to AI-TOD strata using TOLF's manual-review protocol as the second annotator proxy (weaker; state it plainly) or park the idea.
- **Kill** the "unfalsifiability" headline if no crossing exists at any size (publish the null: small-object headroom is real — a pro-progress result the field will cite anyway).
- **Pivot** if the crossing exists but is entirely convention-driven (s* swings wildly with IoU threshold) → the paper becomes "the small-object evaluation convention determines whether progress is measurable" — folds toward C-0311's uncertainty-budget territory; coordinate to avoid salami-slicing.

## Reviewer-2 leftover

K's deepest objection stands as a feature and a bug: at small sizes the human-ceiling estimate itself has huge error bars **exactly where the claim lives** — the paper must present s* as an interval, not a point, and resist the headline "below N pixels benchmarks are meaningless". Also, human re-annotators are not the original annotation pipeline (instructions differ) — the Nature MI 2023 instruction-effect result (cited by J/K) caps how sharply "human ceiling" can be interpreted; use multiple instruction conditions on a subsample if budget allows.

## Expected result (HYPOTHESIZED, not measured)

Crossing exists in the small-object regime with a wide but usable CI; a non-trivial share of published AP-small deltas fall inside the noise band at strict IoU thresholds.

## Negative-result interpretation

No crossing → benchmark-driven small-object progress is falsifiable all the way down; this de-fangs a popular skepticism, complements Label Convergence's aggregate result, and redirects the GT-epistemology family away from a dead end — high option value for the whole C portfolio (0057, 0344-mut, 0259 share this infrastructure).
