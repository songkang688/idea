# Stage 3 — Cluster C KEEP List

10 KEEP + 8 MUTATE = 18 surviving ideas (target 16–18). Every keep names its closest real prior work and the precise untested remainder that justifies survival. Full per-survivor audits in `stage3_cluster_C_priorwork.md`; mutations detailed in `stage3_cluster_C_mutations.md`.

---

## K1. C-0028 — In-batch concept co-occurrence, not loss design, creates dense alignment

- **Closest prior:** JEST — joint example selection for batch curation (Evans et al., DeepMind 2024); NegCLIP hard negatives (Yuksekgonul et al., 2023).
- **Untested remainder:** Causal two-run control (random vs noun-overlap-curated batches, identical loss/data/steps) measuring emergent zero-shot *segmentation* while retrieval is held equal. JEST optimizes learnability and never measures dense grounding.
- **Novelty confidence:** Medium-high.
- **Why it survives harsh review:** Mechanism claim orthogonal to the loss-design literature; cheap at CLIP-small scale; either outcome revises how dense alignment is explained.

## K2. C-0090 — Text-batch rehearsal works by gradient rebalancing, not by content

- **Closest prior:** Text-mix recipes in VLM training (LLaVA-1.5 / VILA data mixes) that show text rehearsal reduces LLM-skill forgetting.
- **Untested remainder:** Content-free control — shuffled/random-token text batches at matched gradient scale vs real rehearsal text. No published experiment separates content replay from gradient rebalancing.
- **Novelty confidence:** Medium-high.
- **Why it survives:** Single decisive control; if random tokens work, rehearsal-data curation effort across the field is misdirected.

## K3. C-0093 — Dimensional collapse doesn't hurt transfer

- **Closest prior:** Jing et al., dimensional collapse in contrastive SSL (ICLR 2022); RankMe effective-rank correlation (Garrido et al., ICML 2023).
- **Untested remainder:** *Interventional* study: artificially induce controlled rank collapse during training (fixed k-dim projection) and measure transfer. All existing evidence is correlational.
- **Novelty confidence:** Medium-high.
- **Why it survives:** Audits the causal assumption behind a family of anti-collapse regularizers; a null result is a genuine correction to the literature.

## K4. C-0128 — Generative editing enables causal measurement of context reliance in segmentation

- **Closest prior:** "The Elephant in the Room" (Rosenfeld et al., 2018) cut-paste context effects; diffusion counterfactual evaluations for classifiers (2023–24).
- **Untested remainder:** Quantitative per-class context-reliance *score* for dense prediction from photorealistic inversion-based counterfactual edits, plus a test linking that score to distribution-shift robustness.
- **Novelty confidence:** Medium-high.
- **Why it survives:** Converts a famous anecdote into a measurable, model-comparable quantity using tools that only recently became good enough.

## K5. C-0229 — Multi-task pretraining's benefit is the data, not the tasks

- **Closest prior:** "Which Tasks Should Be Learned Together" (Standley et al., ICML 2020); multi-task pretrainers (4M, Uni-Perceiver, Florence).
- **Untested remainder:** Pooled-image control: same union of images, one task vs many, matched compute — isolating task-supervision diversity from image-set diversity. Task-relationship studies never pool images across arms.
- **Novelty confidence:** Medium-high.
- **Why it survives:** A missing confound control under a major paradigm; informative in either direction.

## K6. C-0276 — The many ADE20Ks: split drift breaks cross-paper comparability (absorbs C-0279)

- **Closest prior:** SEARCH FOUND NO DIRECT PRIOR — only informal model-zoo/issue-tracker documentation of framework and protocol drift.
- **Untested remainder:** Fixed-checkpoint audit: identical checkpoints run through N frameworks/protocol variants (splits, resizing, TTA, class mappings — the C-0279 inference-protocol axis folded in), quantifying mIoU spread against typical claimed SOTA deltas.
- **Novelty confidence:** Medium (absence-of-prior is the finding).
- **Why it survives:** Cheap, high-utility measurement of the field's comparability budget; no one has quantified it with checkpoints held fixed.

## K7. C-0302 — Last-layer group-robustness fixes fail on spatially entangled bias

- **Closest prior:** DFR — last-layer retraining suffices for spurious-correlation robustness (Kirichenko et al., ICLR 2023); GroupDRO/JTT.
- **Untested remainder:** DFR-style last-layer sufficiency has never been tested on *dense prediction*, where bias is spatially entangled with the target and last-layer surgery cannot re-route spatial features.
- **Novelty confidence:** Medium-high.
- **Why it survives:** Predicted failure mode of a celebrated simple fix, with a constructive follow-up (which layer suffices for dense robustness).

## K8. C-0310 — The camera ISP is a bigger domain axis than the weather

- **Closest prior:** Buckler et al., "Reconfiguring the Imaging Pipeline for Computer Vision" (ICCV 2017); weather benchmarks (ACDC, ImageNet-C).
- **Untested remainder:** Controlled ISP-parameter grid (demosaic/denoise/tone-map/sharpen on RAW) benchmarked head-to-head against weather-shift magnitude on the same scenes and models. Components exist; the magnitude comparison does not.
- **Novelty confidence:** Medium-high.
- **Why it survives:** Quantifies a hidden, controllable domain axis against the field's favorite visible one; directly actionable (ISP randomization as augmentation).

## K9. C-0320 — Mild shifts compound super-linearly

- **Closest prior:** ImageNet-C severity scaling; 3D Common Corruptions (Kar et al., CVPR 2022). SEARCH FOUND NO systematic composition-law study on natural shift axes.
- **Untested remainder:** Whether error under combined mild shifts (weather × sensor × geography) exceeds the additive/independent-failure prediction from single-axis errors — a fitted composition law.
- **Novelty confidence:** Medium.
- **Why it survives:** Deployment-relevant quantitative claim, cheap on frozen models, falsifiable either way.

## K10. C-0332 — Does "accuracy on the line" survive dense prediction?

- **Closest prior:** "Accuracy on the Line" (Miller et al., ICML 2021); "Agreement-on-the-Line" (Baek et al., NeurIPS 2022) — both classification.
- **Untested remainder:** Systematic ID→OOD correlation test for dense structured tasks (mIoU/PQ, spatially correlated errors), plus residual-structure analysis (boundary vs interior, rare vs common classes).
- **Novelty confidence:** Medium-high.
- **Why it survives:** Scope test of a load-bearing empirical law; either outcome changes how OOD performance is predicted for segmentation.

---

## Mutated survivors (details in `stage3_cluster_C_mutations.md`)

| # | Origin | Mutated claim (one line) | Closest prior |
|---|---|---|---|
| M1 | C-0002 (+C-0005 controls) | Orthogonal-classifier + resolution-matched audit of what OV-seg text towers contribute on seen classes | Hoffer et al. 2018; S² 2024 |
| M2 | C-0014 | Tuning-budget-matched post-hoc Gaussian/bilateral filter equivalence audit of the attention-surgery family | NACLIP 2024 |
| M3 | C-0047 | VLM spatial-relation errors show directional asymmetry tracking 1D patch serialization (raster) order | Kamath et al. 2023 |
| M4 | C-0068 | Fresh-vs-transplanted Adam moments isolate optimizer transients from update rank in early fine-tuning forgetting | Biderman et al. 2024; Ash & Adams 2020 |
| M5 | C-0099 | Post-hoc whitening across published SSL checkpoints measures how much leaderboard spread is second-moment bookkeeping | Garrido et al. 2023 |
| M6 | C-0158 | Correlated-noise mechanism: uncertainty sampling selects items where LLM-annotator error spikes; decorrelated acquisition fixes it | FreeAL 2023 |
| M7 | C-0355 | Annotation-budget crossover: when the next head-class label beats a tail-class label, predicted by a feature-sharing score | OLTR 2019; Kang et al. 2020 |
| M8 | C-0365 | Failure-mode-matched revival: unmet classical priors predict which pre-DL components help which foundation models | CRF-decline results; SAM-variant hybrids |
