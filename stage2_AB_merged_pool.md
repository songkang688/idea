# Stage 2 — A+B Merged Working Pool (partial merge; Batch C pending)

**Inputs:** 73 Batch A survivors + 75 Batch B survivors = 148.
**Merges:** 18 (16 cross-batch, 2 within-B) — full rationale in `stage2_AB_duplicates.md`.
**Unique pool: 130 ideas.** Clusters defined in `stage2_AB_clusters.md`. Top selections in `stage2_AB_top30.md`.

**Entry format:** `ID [flags] — one-line`. Merged entries carry both constituent IDs; flags are the union of the constituents' protections. Original Stage-1/Stage-2 text remains authoritative in the batch survivor files; this pool is the dedup roster.

**Protection legend:** HR/HRHR high-risk/high-reward · CI counter-intuitive · RM/DM disagreement magnet · CF cheap-to-falsify · M merit (unprotected).

---

## AB-C1 — Auto-labeling ecology & ground-truth contamination (9)

1. **MERGE-01** (A-0029 + B-0019) [HR+RM / HRHR·DM] — Model-in-the-loop annotation corrupts its own ground truth: within-annotator crossover (scratch / SAM-assisted / correct-the-proposal) measuring anchoring and agreement-with-SAM inflation, plus student training on each corpus to test error-signature inheritance.
2. **A-0007** [RM] — SAM's everything-mode granularity distributions match SA-1B's far more than independent annotations of the same images: the model is a protocol replicator, not a neutral segmenter.
3. **MERGE-09** (A-0267 + B-0329) [HRHR·DM] — Weak-to-strong dense distillation: students on SAM/weak-teacher labels inherit bias-type errors (signature match) and surpass variance-type errors; bias-breaking perturbations and mixing-dilution curves define auto-labeling's ceiling.
4. **B-0001** [CF] — SAM pseudo-label noise is spatially structured and content-correlated; noise-robust losses built for i.i.d. noise fail on the field's actual noise model.
5. **B-0191** [—] — Error amplification in self-consuming segmentation pipelines: boundary biases amplify geometrically across generations; measure the fresh-label injection rate that stabilizes the loop.
6. **B-0320** [—] — Everything-mode output is positive-unlabeled data; PU-corrected training with tiny-audit stratum priors repairs the closed-world error in auto-labeling.
7. **B-0009** [HRHR] — A geometric-stratum census of SA-1B: per-stratum frequency vs capability separates data-limited from architecture-limited failures — where scaling stops working.
8. **B-0006** [DM] — Pooling datasets with different annotation conventions produces an averaged boundary *bias*, not variance; a one-token convention indicator removes it.
9. **B-0053** [DM] — Part of the endoscopy cross-dataset "domain gap" is label-ontology shift, decomposable with a 150-image bridge re-annotation under the other dataset's written protocol.

## AB-C2 — Benchmark validity & evaluation instruments (12)

10. **MERGE-15** (A-0091 + B-0082) [RM / CF·DM] — Label-noise-aware leaderboards: expert re-annotation measures inter-annotator floors and fits noise models; a relabeling bootstrap converts them into rank-flip probabilities and per-benchmark death verdicts.
11. **MERGE-14** (A-0166 + B-0037) [CI / CF] — The annotation-tolerance ceiling: closed-form max-IoU from tolerance and object size, empirically anchored by multi-rater jitter; annotator-identity prediction from model residuals proves style-fitting.
12. **A-0340** [CF] — Bootstrap the leaderboards: the fraction of published orderings that are statistically fictional under test-set sampling alone.
13. **A-0336** [CI] — Human floors and ceilings for segmentation benchmarks: time-budgeted and unlimited human performance — the anchor dense evaluation never had.
14. **A-0337** [RM] — Annotation instructions as an experimental treatment: reasonable instruction variants shift GT at SOTA-gap scale and can invert model rankings.
15. **B-0012** [CF·DM] — Near-duplicates (adjacent frames, same-patient slices) inflate few-shot/annotation-efficiency claims; dedup-aware splits shrink them predictably.
16. **B-0017** [CF] — Transparency benchmarks contain almost no target-absent images; ~500 curated hard negatives (mirrors, water, gloss) may invert method rankings.
17. **B-0108** [DM] — Honest zero-shot: quantify hidden adaptation from validation-set prompt/hyperparameter search; frozen universal settings may reorder leaderboards.
18. **B-0110** [—] — Certifiable FP/day estimation for rare-event monitoring via stratified importance-sampled negatives — orders of magnitude fewer labeled negatives.
19. **B-0294** [HRHR] — Bimodal difficulty-adjusted test-loss residuals as a corpus-free pretraining-contamination detector with per-image probabilities.
20. **A-0254** [RM] — A provably-novel procedurally-synthesized zero-shot benchmark: the first uncontaminated zero-shot number, difficulty-anchored by human segmentability.
21. **A-0246** [CF] — Few-shot segmentation scores are base-class proximity in disguise; distance-maximized re-splits drop reported SOTA and test ranking stability.

## AB-C3 — Meta-science, replication & attribution (5)

22. **A-0245** [RM] — A 2015 U-Net with a 2026 recipe: recipe-equalized retraining measures what fraction of a decade's reported progress is recipe rather than architecture.
23. **A-0226** [RM] — Powered replication of "attention module + U-Net" medical papers under tuned baselines and 5 seeds: how much of the genre survives?
24. **A-0242** [RM] — Publication-bias z-curve for segmentation deltas: a discontinuity at the publishability threshold quantifies field-level selection bias.
25. **MERGE-11** (A-0250 + B-0024) [CF / DM·CF] — Deflationary few-shot baselines: retrieval + dense-correspondence transfer and direct PEFT fine-tuning vs episodic meta-learning across shot ladders and cross-domain targets; locate the crossovers.
26. **A-0261** [RM] — WSSS's residual gap decomposed by oracle substitution (seeds/extent/boundaries): is the CAM paradigm structurally exhausted?

## AB-C4 — PEFT & fine-tuning recipe science (12)

27. **A-0055** [CI+RM] — Tuned layer-wise LR decay alone may come within 0.5 mIoU of the best PEFT methods on most benchmarks — the missing baseline of a literature.
28. **A-0067** [HR+RM] — One dial: the effective encoder/decoder LR ratio may explain most variance among fine-tuning recipes (R²>0.7 or bust).
29. **A-0072** [RM] — Strong augmentation + frozen features vs LoRA at matched compute: how much of "adaptation" is invariance injection, not representation change?
30. **B-0114** [DM] — Seed variance of PEFT fine-tuning vs reported effect sizes: variance components and minimum-detectable-effect tables for the subfield.
31. **B-0253** [—] — Attention adapts "where", MLP adapts "what": an error-type-stratified double dissociation grounding PEFT placement in mechanism.
32. **B-0257** [CI·DM] — The boundary tax: PEFT that matches full FT on mIoU may systematically underperform on boundary metrics — an artifact of region-dominated reporting.
33. **B-0269** [CI·CF] — Adapting the choice, not the masks: oracle-candidate audits + selection-head-only adaptation reclassify convention-type "domain gaps".
34. **B-0270** [CI] — Is the input stem the whole story for semantics-preserving modality shift? Stem-only adaptation splits interface from semantics.
35. **B-0272** [CI] — Capacity as regularization: under structured label noise the PEFT-vs-full-FT gap may reverse — constrained updates cannot fit annotation errors.
36. **B-0306** [CI·CF] — Less rank, more accuracy below ~20 samples: a data-size-indexed rank-selection rule for the modal medical regime.
37. **B-0315** [CI] — Five percent of elsewhere: a small out-of-domain anchor fraction may dominate tuned weight decay/dropout via gradient-subspace anchoring.
38. **A-0238** [CI] — Depth auxiliary vs semantically-empty auxiliary: the matched-control instrument separating multi-task synergy from generic regularization.

## AB-C5 — Forgetting, retention & update geometry (5)

39. **MERGE-07** (A-0076 + B-0248) [RM / DM] — The gain/retention frontier: matched-target checkpoint selection traces the Pareto frontier, places published recipes inside it (forgetting as unforced error), and fits retention-vs-effective-rank laws.
40. **A-0078** [CI] — Forgetting is mostly readout drift: linear re-probing of fine-tuned encoders recovers most "lost" zero-shot dense performance.
41. **A-0089** [HR] — Forgetting hysteresis: brief re-exposure restores suppressed capabilities at ~5% of original cost; time-constants define cheap refresh schedules.
42. **MERGE-08** (A-0058 + B-0260) [HR+CI / CI·DM] — Low-rank adaptation amplifies shortcuts: worst-group degradation on constructed spurious correlations and sharper site-fingerprint encoding on natural hospital shifts, with rank sweeps as the mechanism test.
43. **B-0251** [—] — Predicting adapter-merging success from task-vector subspace angles: merge-or-retrain decided from weights alone.

## AB-C6 — Domain shift: diagnostics & test-time adaptation (9)

44. **MERGE-05** (A-0296 + B-0064) [RM / DM] — The UDA reality audit: published methods on fresh pairs (frozen + bounded-retuning) against source-only and frozen-foundation baselines at matched compute; ranking transfer and marginal value per shift regime.
45. **MERGE-06** (A-0303 + B-0057) [CF] — Token/norm-statistics recalibration: an optimization-free ViT TTA primitive whose recovery fraction doubles as a minutes-cheap shift-tier diagnostic.
46. **B-0054** [—] — Which domain-distance metric actually predicts realized fine-tuning gain? Validated against 15+ real fine-tunes, not proxy shift labels.
47. **B-0072** [CI] — Amplitude-only Fourier adapters as a capacity-constrained instrument measuring the "style fraction" of any domain shift.
48. **B-0078** [HRHR] — Language as a domain coordinate: can a text description of a domain condition adaptation with zero target images? Permutation-controlled.
49. **B-0279** [—] — Label-free PEFT: distilling prompt-ensemble consensus into adapters — a collapse-resistant, architecturally native TTA signal.
50. **A-0239** [CF] — Entropy-minimization TTA silently collapses rare classes while improving averages; trigger conditions from batch statistics.
51. **B-0304** [CI·DM] — Style leaks through skip connections, piping low-level domain statistics past the invariant deep pathway; probe, ablate, normalize.
52. **A-0305** [CI] — Night segmentation: adaptation gap or information deficit? A human-ceiling decomposition into recoverable and unfixable components.

## AB-C7 — Language–vision grounding & dense-VLM failure modes (13)

53. **A-0041** [HR+CI] — Does chain-of-thought causally change *where* VLMs ground, or is reasoning post-hoc rationalization? Wrong-reasoning injection with mask endpoints.
54. **A-0187** [CI+CF] — Negation anti-accuracy: models select the negated object above chance; probes locate it as a fusion failure, not an encoding failure.
55. **A-0183** [CF] — Spatial-relation minimal pairs: relations may be near chance — the core value proposition of language-guided segmentation tested in isolation.
56. **MERGE-02** (A-0185 + B-0241) [CF+RM / CI·CF] — The absent-target hallucination benchmark: presence × plausibility × prompt-assertiveness; scene-prior targeting of hallucinated masks; refusal protocols at fixed sensitivity.
57. **A-0199** [CF] — Scene text hijacks grounding toward regions containing matching words, scaling with OCR capability — typographic attacks reach masks.
58. **A-0181** [M] — CLIP dense misalignment is co-occurrence-structured: leak strength per class is predicted by caption statistics, enabling targeted fixes.
59. **B-0124** [CF] — Text-anchor collinearity upper-bounds open-vocab confusion for smoke/steam/fog; anchor substitution localizes the fix to text space.
60. **A-0031** [CF+RM] — Paraphrase variance in open-vocab segmentation exceeds reported SOTA gaps; ranking stability under prompt resampling.
61. **A-0033** [CI+CF] — Prompt-specificity inverse-U: basic-level categories optimal, over-specific prompts fail via pretraining frequency — Rosch meets VLMs.
62. **A-0049** [CI+CF] — Lay vs expert terminology for medical grounding: register mismatch as a free performance lever and text-tower diagnostic.
63. **B-0132** [—] — Layer-wise localization decay in VLM stacks: where dense information dies (projector? resampler?) and validated pre-collapse tap points.
64. **B-0174** [CI·DM] — The semantic-blur hypothesis: heavier language supervision degrades boundary metrics at matched region accuracy; boundary auxiliaries as the remedy.
65. **B-0185** [HRHR·DM] — Knowledge conflict: dense medical VLMs regress toward textbook priors exactly on abnormal anatomy; scale-dependence of over-trust.

## AB-C8 — Interactive segmentation & the prompt interface (5)

66. **MERGE-17** (B-0089 + B-0193) [DM] — The human-prompt distribution gap: oracle-prompt inflation factors at evaluation and human-modeled prompt sampling at training, from one shared prompt-log collection.
67. **B-0083** [CF·DM] — Medical-SAM rankings under 5 click protocols: cross-protocol rank correlations and a protocol-sensitivity index for mandatory reporting.
68. **B-0104** [CF] — Wrong-prompt behavior: does SAM fail loudly or silently under semantically wrong prompts? A safety property nobody reports.
69. **B-0128** [CF] — Lipschitz geometry of the click-to-mask map: discontinuity density as a usability property that predicts human interaction cost.
70. **B-0282** [CI·CF] — Non-monotonic refinement: correction clicks can make masks worse via decoder mode competition; regression rates + stabilized decoding.

## AB-C9 — Transparency, camouflage & layered scenes (6)

71. **MERGE-10** (A-0141 + B-0126) [HR+CI / CI] — What frozen features know about layered scenes: probes decode {glass, background, both}; the verdict routes transparency work to pretraining vs output-format fixes.
72. **MERGE-16** (A-0142 + B-0159) [CI / HRHR] — Depth failure as transparency signal: naive RGB-D fusion hurts while explicit depth-invalidity features help; harvested invalid-depth pixels become the largest free transparency corpus.
73. **B-0075** [HRHR·CI] — Does SAM segment glass by its reflections? Reflection-environment swaps give a causal cue attribution for transparency.
74. **B-0162** [HRHR] — Polarization-taught transparency: train with privileged polarization, measure the fraction of the advantage that survives RGB-only inference.
75. **A-0157** [CI] — The human floor on near-invisible glass: brief-presentation psychophysics decides whether competence or information is the bottleneck.
76. **A-0154** [CF] — Camouflage failure: attentional or perceptual? Oracle-prompt recovery decomposes find-vs-delineate and could redirect COD research.

## AB-C10 — Amorphous matter full stack: smoke, fire, wildfire (11)

77. **A-0121** [RM] — Binary smoke masks are ill-posed GT: per-annotator density thresholds explain inter-annotator variance; density-graded GT redefines the task.
78. **A-0122** [HR] — Beer–Lambert transmittance from paired frames as physically defined smoke ground truth — supervision without human thresholding.
79. **MERGE-03** (A-0006 + B-0226) [CI / DM] — One boundary-contrast law: a single standardized contrast measure may predict IoU and recall across amorphous, camouflage, transparency, and lesion targets; causal contrast-enhancement arm included.
80. **A-0128** [CF] — No prompt strategy rescues SAM on smoke; failures follow a density-conditioned shrinkage law that any SAM-derived smoke dataset inherits.
81. **A-0126** [RM] — Detection latency, not IoU, as the wildfire metric: latency and IoU rankings disagree; latency winners share low-density recall.
82. **A-0123** [CI+CF] — Fire segmenters are color detectors: hue-shifted flames and colored-distractor batteries expose a spectral shortcut with predictable catastrophic failures.
83. **A-0125** [HR] — Turbulence spectra as a label-free smoke signal: buoyant-plume statistics separate smoke from rigid-world motion; distance-regime gate first.
84. **B-0318** [HRHR] — Differentiable single-scattering rendering lets 2D smoke masks supervise 3D density fields — physical quantification from existing labels.
85. **B-0055** [CI·DM] — Fog as a negative domain: fog-invariance training may transfer to smoke-invariance — robustness and sensitivity in direct conflict.
86. **A-0319** [M] — Boxes are the wrong primitive for amorphous targets: blob/level-set formulations judged on downstream decision quality.
87. **B-0219** [CI] — Is NMS the binding constraint for fragmenting-plume detection? Oracle-suppression accounting attributes the loss to the suppression stage.

## AB-C11 — Small structures & token-lattice artifacts (9)

88. **MERGE-04** (A-0161 + B-0129) [RM] — The small-structure bottleneck: frozen-feature oracle probes locate the decodability crossover; decoder-capacity × patch-size grids test tokenization irreversibility.
89. **A-0003** [CF] — The IoU-vs-size failure law: a knee at 2–3 patch widths; curve collapse in patch units under context-controlled zoom.
90. **A-0313** [RM] — Resolution beats architectural small-object remedies at matched compute (FLOPs/latency/memory all reported).
91. **B-0288** [CI·DM] — An inverse-scaling pocket: smaller model variants may beat larger ones on tiny structures as capacity reallocates to global coherence.
92. **A-0176** [CI] — Benchmark JPEG already deleted the small objects: compression as a benchmark-construction confounder for the small-object literature.
93. **A-0174** [CF] — Register-token artifacts collide with small instances: matched-statistics recall comparison across register/no-register models.
94. **B-0122** [CI·CF] — Angular aliasing: thin-structure quality oscillates with orientation relative to the patch lattice; synthetic controls isolate the embedding stage.
95. **B-0305** [CI·CF] — Periodic performance in input size: resolution × patch-grid aliasing contaminates cross-paper comparisons; anti-aliased resizing fixes it.
96. **A-0170** [CI] — INR decoders hallucinate sub-pixel boundaries: synthetic-truth dissociation separates recovered information from metric-pleasing smoothing.

## AB-C12 — Uncertainty, calibration & confidence validity (6)

97. **A-0103** [CI] — Uncertainty maps ≠ clinician disagreement: after boundary-band exclusion, standard uncertainty barely correlates with expert ambiguity.
98. **MERGE-18** (B-0120 + B-0337) [CF / CF·DM] — Are free mask ensembles valid posteriors? Coverage tests of SAM multimask spread and diffusion samples against held-out rater distributions.
99. **B-0084** [CF] — Out-of-domain calibration of SAM's predicted-IoU head: the never-audited gate inside thousands of auto-labeling pipelines.
100. **A-0097** [RM] — Dice loss destroys calibration, scaling with class imbalance; a CE→Dice schedule may keep accuracy without the penalty.
101. **B-0310** [CI] — Confidence inversion: mean-regression losses turn soft labels into *harder* predictions — softness in, sharpness out.
102. **A-0280** [CI+CF] — Uncertainty routes labels to the wrong pixels: confident-but-wrong regions beat high-uncertainty regions for annotation value.

## AB-C13 — Representation science of visual foundation models (10)

103. **A-0001** [CI] — SAM follows edges, not objects: a 2×2 camouflage/texture-edge dissociation converts failure anecdotes into one mechanism claim.
104. **A-0013** [CI+CF] — SAM2 lost static fine-boundary quality relative to SAM1: the newest-isn't-better modality trade-off audit.
105. **MERGE-13** (A-0021 + B-0136) [CI+CF / CI·CF] — Functional achromaticity: hue/grayscale/equiluminant interventions on SAM-class models plus luminance-only smoke retraining — which dense capabilities are colorblind.
106. **A-0202** [M] — The definitive task×backbone matrix for frozen dense features under one matched probing protocol; objective family predicts the winner per task.
107. **A-0203** [HR+CI] — SSL "object emergence" as a crop-statistics artifact: decentered-cropping retraining tests the causal origin of a celebrated narrative.
108. **A-0266** [CI] — Object discovery or texture grouping? Dissociation scenes measure what unsupervised segmentation actually clusters.
109. **A-0211** [CI] — Texture-vs-shape verdict inverts for dense readouts: the same backbone may be shape-biased in classification and texture-biased in masks.
110. **A-0223** [CI] — In-context segmentation: abstraction or sophisticated copying? Semantic-match × visual-match support grids decide.
111. **A-0225** [RM] — Platonic convergence is semantics-only at patch level: affine alignment preserves class decodability but not geometry.
112. **A-0207** [RM] — Data vs method: a data-overlap kernel may predict inter-VFM behavioral similarity better than objective or architecture indicators.

## AB-C14 — Composed pipelines & preprocessing skepticism (6)

113. **B-0217** [—] — The box-to-mask error transfer function: train segmenters under the detector's measured error distribution — a zero-inference-cost fix.
114. **B-0223** [CI] — Assigner-induced gradient starvation of elongated objects; ratio-conditional assignment recovers a safety-critical family with no architecture change.
115. **B-0233** [DM·CI] — What does a detector add over background-model change detection for static cameras? Role decomposition at matched FP budgets.
116. **B-0331** [DM] — The hallucination-utility frontier of generative SR for downstream dense prediction, plus a seed-ensemble fabrication detector.
117. **B-0338** [CI] — Noise as signal: denoising deletes the forensic cues tiny-target detection relies on; a predictable contrast-to-noise crossover.
118. **B-0285** [CI·CF] — Compression that helps: mild JPEG may improve amorphous-target segmentation by deleting high-frequency clutter — non-monotonic quality curves.

## AB-C15 — Medical supervision economics & deployment safety (6)

119. **A-0118** [CI] — Models hallucinate surgically removed organs: atlas-prior dependence quantified with a positional-consistency predictor — a patient-safety benchmark.
120. **A-0093** [HR+RM] — Why nnU-Net still wins: matched-budget component swaps (3D context, augmentation policy, resolution handling) causally decompose the gap.
121. **A-0100** [CI+CF] — Flip-TTA harms lateralized anatomy: an anatomically invalid invariance inside standard pipelines and challenge winners.
122. **B-0156** [—] — The exchange rate between radiology reports and pixel labels: iso-performance grids price an idle hospital-scale data asset per finding type.
123. **B-0182** [—] — Absence statements as supervision: certified report negations as class-specific hard negatives against hallucinated segmentations.
124. **B-0184** [CI·DM] — Contrast-enhancement vessel GT is physiologically selective: models inherit blindness to occluded segments — the clinical cases that matter.

## AB-C16 — Synthetic training data: coverage, artifacts & dose (6)

125. **B-0186** [DM] — Does generative augmentation cover the tail it promises to fix? Per-stratum coverage and per-stratum segmentation deltas, not means.
126. **MERGE-12** (A-0285 + B-0190) [CI] — Synthetic-fraction dose-response: the within-class threshold where rare-class real recall inverts and the global threshold where OOD robustness silently decays, with a label-free probe detector.
127. **B-0189** [CI·CF] — The inpainting fingerprint: do augmented models learn the lesion or the paste? A fingerprint classifier plus real-only test sets.
128. **B-0200** [CI] — Too-clean ground truth: annotator-noise-matched synthetic labels may beat pixel-perfect ones on real data.
129. **A-0283** [M] — Which realism factor buys sim-to-real transfer: a 2⁴ factorial over geometry/texture/lighting/sensor realism prices rendering effort.
130. **A-0287** [M] — Procedural beats diffusion on web-sparse phenomena: the coverage-circularity limit of generative augmentation, measured in physical parameter space.

---

## Accounting

- Unique ideas: **130** (57 standalone A + 55 standalone B + 18 merged).
- Protected HRHR/HR entries: 17 (incl. merged carriers) · CI-protected: ~48 · RM/DM: ~40 · CF: ~38 (flags overlap; unions kept on merged entries).
- Reviewer-disagreement conflicts flagged: 14 (`stage2_AB_duplicates.md` §3).
- Expected Batch C effect: +new survivors, additional merges appended as MERGE-19+; cluster set may grow beyond 16.

*End of merged working pool (A+B partial). Awaiting Batch C.*
