# exp_07 — A-0028: the SAM2 teleport test — appearance vs location tracking (L revive)

**ID:** W2-A-0028.
**Pipeline status:** A original → F keep, "among the best of C02" (ROI 5, feas 5, cheap-falsify, counter-intuitive) → missed F's top-20 → never Reviewer-2 attacked, absent from all ledgers → L revive #3 (only surviving SAM2-video candidate; audit Finding 7 orphaned-cheap-win). **This protocol includes the mandatory built-in Reviewer-2 pass L required.**

## Built-in Reviewer-2 pass (fresh, this session)

Live search (this session) found: **DAM4SAM** (CVPR 2025, arXiv:2509.13864 — distractor-aware memory; documents SAM2 drift toward visually similar distractors, ships the DiDi distractor-distilled dataset) and **a systematic SAM2/SAM3 memory-design study** (arXiv:2512.22624 — decomposes memory into short-term appearance and long-term distractor-resolving components across ten benchmarks). EVIDENCE: distractor-induced identity swap is a documented, actively-fixed phenomenon. **Not found:** any controlled teleport/swap *causal probe* measuring the appearance-vs-location dissociation as a function of displacement and temporal gap — the psychophysics-style quantitative law remains unclaimed. Consequence: the framing must change from "nobody has studied this" to "the fix-papers presuppose an appearance/location arbitration that nobody has measured." SAM3 exists (per 2512.22624) and must be included as a subject model, which *strengthens* the paper (does the next generation change the arbitration?).

## Research question

When target and distractor exchange positions between frames (teleport/swap), does SAM2/SAM3 memory follow appearance or location — and how does the arbitration shift with inter-frame displacement, temporal gap, and distractor similarity?

## Falsifiable hypothesis

H1: P(follow-the-place) increases monotonically with inter-frame displacement and temporal gap — i.e., memory attention degrades toward a location prior under temporal sparsity (original A hypothesis).
Falsified if: SAM2 follows appearance at near-ceiling rates across all gaps/displacements (its memory is appearance-dominant everywhere), or if behavior is unsystematic (no monotone arbitration).

## Prediction

HYPOTHESIS: location-following rises with gap and displacement; distractor similarity shifts the curve left (consistent with DAM4SAM's drift observations, which are EVIDENCE for the phenomenon's existence but contain no dissociation curve).

## Method sketch

Behavioral probe; no training. Modules: (1) **stimulus generator**: composite clips from static images — two objects (target + distractor at parametric similarity: same instance / same class / different class) exchanging positions with controlled displacement d and frame gap g; cut-paste with Poisson blending, plus curated natural hard-cut footage for OOD validation (A's own risk note); (2) **subject models**: SAM2 (multiple sizes), SAM3, plus DAM4SAM as a "fixed-memory" comparator — if the fix works, its dissociation curve should differ measurably (this converts a diagnosis into an evaluation instrument for memory designs); (3) **scoring**: prompt on frame 0, at swap frame measure mask IoU with object-at-old-location vs tracked-object-at-new-location → per-trial trichotomy (follow-object / follow-place / neither); (4) **psychometric fitting**: P(follow-place) as a function of (d, g, similarity) per model.

## Data

Stimuli built from COCO/LVIS crops and DAVIS-class video frames; natural-cut validation set from public edited footage with manual GT (~100 clips). DiDi (DAM4SAM's dataset) as an external anchor where applicable.

## Baselines

A pure location-prior dummy (predict old location always) and a pure appearance matcher (template match) bracket the behavior space; SAM2 vs SAM3 vs DAM4SAM comparisons are the substantive contrasts.

## Metrics

Follow-place rate curves vs d, g, similarity (with CIs over stimuli); area-under-arbitration-curve per model as a scalar "location-prior index"; natural-cut agreement with synthetic-probe predictions (external validity check).

## Killer Experiment

**One model (SAM2-L), synthetic swap battery across the (d, g, similarity) grid — one GPU-day** (L's estimate, confirmed plausible: inference-only, ~10⁴ short clips). Pre-registered either-outcome interpretation: monotone location-prior curve → the arbitration law; appearance-ceiling → "SAM2 memory is appearance-dominant: a controlled refutation of the location-prior worry" — both are findings (F's original assessment).

## GPU/VRAM/time estimate

**1 GPU-day (killer) / 3–5 GPU-days (full: 3 model families + DAM4SAM + natural-cut validation), single 24GB GPU.** Stimulus curation: ~1 week of engineering. Cheapest protocol in this set.

## Stop / pivot / kill criteria

- **Kill** if a teleport-style dissociation probe appears in the literature before execution (mandatory re-search at experiment freeze; the memory-design field is moving fast — 2512.22624 is a preprint being extended).
- **Pivot** if synthetic-cut behavior fails to predict natural-cut behavior (OOD confound realized) → re-scope to natural-cut-only with a smaller factorial grid.
- **Stop** the multi-model extension if SAM2-L shows unsystematic behavior (no curve to characterize — report the instability itself, one short note).

## Reviewer-2 leftover

"You built adversarial stimuli for a model that was never trained on cuts — of course it fails" — answered only by the natural-cut validation arm and by DiDi-anchored comparisons; keep both. The constructive gap remains: this diagnoses, DAM4SAM fixes — position as the *measurement instrument* the fix-papers lack (their ablations report benchmark deltas, not arbitration mechanisms).

## Expected result (HYPOTHESIZED, not measured)

Monotone location-prior curve for SAM2 with similarity modulation; SAM3/DAM4SAM curves shifted toward appearance — establishing the probe as a memory-design metric.

## Negative-result interpretation

Appearance-dominance everywhere is a trust-positive result for cut-heavy deployments (surveillance, medical cine) and directly contradicts the drift folklore the distractor-memory line is built on — a short, citable corrective. Either way the probe battery ships as the video-memory cluster's first standardized instrument (the portfolio's only C02 representative).
