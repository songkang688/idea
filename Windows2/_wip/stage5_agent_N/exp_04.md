# exp_04 — A-0206: SAM fingerprint & inheritance (diagnosis + constructive check)

**ID:** W2-A-0206.
**Pipeline status:** F flagship survivor → J SURVIVE-IF-EXPERIMENT (controlled-provenance corpus is the gate; dialect confound is the killer) → L spot-check: window still open (no mask-space provenance paper found; adjacent image-attribution literature, e.g. model-genealogy arXiv:2608.15652, is both method shelf and "why is this different" question).

## Research question

(1) Do SAM-assisted masks carry a boundary-geometry fingerprint **separable from dataset dialect** and surviving human post-editing? (2) Do models trained on fingerprinted labels inherit SAM's specific failure modes (wire breakage, hole filling) — and (3, constructive) can a released provenance-audit tool + de-fingerprinting check mitigate it?

## Falsifiable hypothesis

H1 (fingerprint): a classifier on boundary micro-statistics separates raw-SAM from hand-drawn masks within one controlled corpus AND generalizes to held-out datasets with documented provenance (dataset identity controlled).
H2 (inheritance): matched models trained on SAM-assisted vs hand-drawn labels **of identical images** show systematically different failure-mode profiles on a neutral probe set, in SAM's known directions.
Falsified if: (H1) within-corpus separation fails or collapses at realistic edit depths / fails cross-dataset; (H2) failure profiles are within seed noise.

## Prediction

HYPOTHESIS: raw-SAM vs hand-drawn separates easily; edit depth degrades the fingerprint monotonically; inheritance effect exists but is small and class-dependent. No numbers claimed.

## Method sketch (modules / dataflow)

1. **Controlled-provenance corpus** (the killer-experiment asset, per J): ONE dataset's images, SAME annotator pool, three conditions — (a) hand-drawn, (b) SAM-assisted-then-edited with **logged edit depth** (time, vertex edits), (c) raw SAM.
2. **Fingerprint module:** boundary micro-features (curvature spectrum, vertex-simplification statistics, edge-snapping offsets to image gradients, hole/blob topology stats) → classifier; trained (a)-vs-(c), tested on (b) by edit-depth stratum and on held-out documented-provenance datasets.
3. **Inheritance module:** two segmenter families × 3 seeds trained on (a)-labels vs (b)-labels of identical images (identical images/classes — only label provenance differs); failure-mode profiler (wire-class breakage rate, enclosed-region fill rate, boundary curvature bias) on a neutral probe set.
4. **Constructive check:** (i) release the classifier as a dataset-provenance audit tool with calibrated abstention; (ii) a *de-fingerprinting* intervention — retrain on (b)-labels with boundary jitter/re-snapping matched to hand-drawn statistics — testing whether inheritance shrinks. This converts diagnosis into a usable mitigation (the audit-to-artifact conversion L demanded).

## Data

Corpus base: one existing dataset's images (e.g., a COCO/LVIS subset or ADE20K subset — chosen at execution for annotator-pool compatibility), ~600–1000 images × 3 conditions. Held-out provenance-documented datasets for H1 transfer. Neutral probe set for H2 assembled from classes with known SAM failure modes (thin structures, enclosed holes).

## Baselines

Dataset-dialect null (J's central attack): a classifier trained to distinguish *datasets* on hand-drawn masks only — its cross-dataset confusion pattern calibrates how much "fingerprint" signal is just dialect. Chance-level and mask-resolution-matched controls. Image-attribution ports (2608.15652-style features) as method baselines.

## Metrics

H1: AUROC within-corpus, by edit-depth stratum, and cross-dataset with dialect control subtracted. H2: failure-mode rate differences with seed CIs; effect direction agreement with SAM's documented failure modes. Constructive: inheritance reduction after de-fingerprinting.

## Killer Experiment

**The controlled corpus + (a)-vs-(c) classifier + cross-dataset transfer with the dialect null.** Everything else is gated on it. If cross-dataset transfer with dialect controlled fails, the prevalence-survey ambition dies immediately and cheaply (before any inheritance training is spent).

## GPU/VRAM/time estimate

GPU: minor — fingerprint classifier is CPU/small-GPU; inheritance = 2 families × 2 label-conditions × 3 seeds = 12 segmenter trainings ≈ **1–2 GPU-weeks (24GB)**. The real cost is **annotation: ~600–1000 images × 2 human conditions with logged edit depth** (weeks of calendar time, ~low-thousands USD or lab-internal). This is the batch's most expensive killer experiment and the reason its ROI ranking is mid-table despite flagship upside.

## Stop / pivot / kill criteria

- **Kill** if within-corpus (a)-vs-(c) separation fails (no fingerprint even in the clean case).
- **Pivot** to a within-dataset edit-depth study ("how much human editing erases SAM style") if separation exists but cross-dataset transfer fails after dialect control — smaller, still publishable, still the first controlled corpus of its kind (the corpus itself is a releasable artifact either way).
- **Stop-and-reposition** if any mask-space provenance paper appears (J and L both verified absence; re-check at proposal and experiment freeze — the image-attribution field is one port away).

## Reviewer-2 leftover

Even with the dialect null, "annotation-guideline dialect vs model fingerprint" cannot be fully separated for *found* datasets — the prevalence survey will carry an irreducible caveat; the paper's defensible core is the controlled corpus + inheritance experiment, with the survey as a calibrated-uncertainty appendix. Inheritance attribution ("because of the labels") holds only in the matched-images design — do not generalize it to wild datasets.

## Expected result (HYPOTHESIZED, not measured)

H1 clean-case separation succeeds; edit-depth degradation strong; cross-dataset transfer partial. H2 small but directionally consistent effect. De-fingerprinting shrinks inheritance partially.

## Negative-result interpretation

No fingerprint, or dialect-dominated transfer → "SAM-assisted annotation is stylistically absorbed by human editing" — a reassuring, publishable negative for the dataset-governance conversation, and the corpus remains the field's first provenance-controlled annotation asset. Inheritance null → provenance worries about *style* propagation are overblown at current edit practices; the audit tool still ships for raw-SAM detection.
