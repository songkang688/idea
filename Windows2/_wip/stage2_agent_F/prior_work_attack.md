# Windows2 Stage-2 Agent F — Adversarial Prior-Work Attack (Batch A)

Attacker: Cloud Sub-Agent F. All citations below come from live web searches performed during this review; no paper is cited from memory alone (the one memory-recalled paper, blob loss, was re-verified by search before citation). Verdict semantics: **KILL** = core claim is published or answered; **MUTATE** = idea survives only in a modified form (mutation given); **SURVIVE** = no direct prior work found, idea stands as written (with mandatory-citation caveats).

Attacked set: the 15 mandated targets, plus 13 ideas I rank at or above them (Tier A of my shortlist).

Summary table:

| ID | Verdict | One-line reason |
|----|---------|-----------------|
| W2-A-0001 | MUTATE | SAM prompt-variance uncertainty is a crowded line (SAM-U etc.); validation against real human disagreement is the surviving sliver |
| W2-A-0017 | KILL (merge sliver into 0203) | WACV 2026 paper already did the correlational AND fine-tuning legs |
| W2-A-0206 | SURVIVE | No SAM-mask-fingerprint forensics found; nearest lines are image-forgery localization and LLM monoculture |
| W2-A-0026 | SURVIVE | Error accumulation documented, online detection exists; prospective static→temporal prediction absent |
| W2-A-0051 | KILL | Lemay et al. MELBA 2022 answers the exact question |
| W2-A-0060 | MUTATE | Mechanism known + mitigated (marginal/exclusion loss); only the dose-response law survives |
| W2-A-0076 | MUTATE | Smoke matting/density datasets exist; the ranking-flip audit is the surviving core |
| W2-A-0107 | MUTATE | Depth-invalidity-as-cue exists; fleet-scale scaling claim survives |
| W2-A-0145 | SURVIVE | No independent-presence-verified COD evaluation found |
| W2-A-0151 | SURVIVE | WACV 2024 decomposes model error only; annotation/metric attribution absent |
| W2-A-0181 | MUTATE | Minority-collapse theory exists; empirical seg cliff survives if it engages that theory |
| W2-A-0198 | MUTATE | Churn known in classification; Bosma 2024 + Lost-in-the-Folds 2026 are adjacent; audit application survives |
| W2-A-0245 | MUTATE | UDA protocol critiques exist; the frozen-HP rank-correlation number survives |
| W2-A-0301 | MUTATE | Ramos et al. ICCVW 2025 is a direct near-hit; SA-1B/dense-specific + memorization stratification survives |
| W2-A-0326 | MUTATE | RF non-monotonicity known in niches; property-decomposed signed curves survive |
| W2-A-0074 | MUTATE | SSN + conformal volumetry cover much; the anti-conservatism audit of pixel-independent propagation survives |
| W2-A-0075 | SURVIVE | STAPLE minority suppression known; outcome-anchored correctness audit absent |
| W2-A-0121 | SURVIVE | Water-hazard detection exists; reverse-direction phantom-object audit absent |
| W2-A-0148 | MUTATE | Soft-vs-hard highlighting literature covers the core; COD-specific + calibration moderator survives |
| W2-A-0150 | SURVIVE | Zoom-precision folklore exists in industry; controlled signed-bias measurement absent |
| W2-A-0163 | SURVIVE | Boundary IoU's scalar tolerance is the nearest; class-pair band measurement absent |
| W2-A-0205 | MUTATE | Acceptance bias established in NLP annotation; dense-mask correlated-contamination legs survive |
| W2-A-0237 | SURVIVE | Label-space conflicts known as engineering problem; gap-decomposition by re-annotation absent |
| W2-A-0300 | MUTATE | Established for LLMs; dense-vision longitudinal version survives as the explicit counterpart |
| W2-A-0331 | MUTATE | blob loss states the premise and fixes it; gradient-instrumentation diagnosis survives |
| W2-A-0334 | MUTATE | Silhouette recognition is classical; scale + scene/activity recovery + privacy framing survives |
| W2-A-0349 | SURVIVE | Minima-rule psychophysics is the foundation, not the competitor; model-vs-human divergence measurement absent |
| W2-A-0352 | MUTATE | Counting is answered (regression wins at density); non-count scalar measurements survive |

Totals: **2 KILL, 15 MUTATE, 11 SURVIVE.**

---

## Mandated targets

### W2-A-0001 — Point-prompt jitter variance predicts human inter-annotator disagreement
- **Closest works:**
  - SAM-U: Multi-box prompts triggered uncertainty estimation for reliable SAM in medical image — https://arxiv.org/abs/2307.04973 — estimates pixel uncertainty from multi-box prompt augmentation and explicitly frames the prompt ensemble as "simulating the annotations of multiple clinical experts".
  - MedSAM-U: Uncertainty-Guided Auto Multi-Prompt Adaptation — https://arxiv.org/html/2409.00924v1 — uses prompt-induced uncertainty to refine prompts.
  - FNPC-SAM (SPIE) — https://doi.org/10.1117/12.3006867 — multi-box augmentation + uncertainty-based FN/FP correction.
- **What they did:** turned prompt-perturbation variance into an uncertainty signal and an engineering tool.
- **Exact difference:** none of them validate the signal against *real held-out multi-rater disagreement* as the referent; they use it as a proxy without testing the psychometric claim (rank correlation with human ambiguity per object).
- **Remaining novelty:** the calibration/validation study itself — treating SAM as a psychophysical ambiguity meter and testing r>0.6 against multi-rater data (LIDC-IDRI, QUBIQ, MS lesion). Modest but real; it is a measurement paper, not a method paper.
- **Confidence:** high (multiple direct hits on the mechanism, none on the validation).
- **Reviewer #2 attack citation:** "SAM-U already interprets multi-prompt variance as simulated expert disagreement (arXiv:2307.04973); what's new?"
- **Verdict: MUTATE.** Mutation: drop any method claim; run the validation on ≥3 multi-rater datasets, report where the correlation breaks (object class, size, modality), and test whether prompt-jitter variance is *redundant* with ensemble variance (ties into W2-A-0198/0021).

### W2-A-0017 — SA-1B imprinted a closed-compact prior; wiry objects structurally outside output space
- **Closest works:**
  - Zhang et al., Quantifying the Limits of Segmentation Foundation Models: Modeling Challenges in Segmenting Tree-Like and Low-Contrast Objects — WACV 2026 — https://arxiv.org/abs/2412.04243 (also https://openaccess.thecvf.com/content/WACV2026/papers/Zhang_Quantifying_the_Limits_of_Segmentation_Foundation_Models_Modeling_Challenges_in_WACV_2026_paper.pdf).
- **What they did:** introduced interpretable tree-likeness and textural-separability metrics; showed SAM/SAM2/HQ-SAM performance correlates with them on synthetic + real data; attributed the failure to SA-1B's low-concavity object statistics; **and ran the targeted fine-tuning experiment, which fails to resolve the failure** — concluding the limitation is architectural (textural confusion), not purely data.
- **Exact difference:** W2-A-0017's two legs — (1) shape-statistics gap predicts per-shape-class failure and (2) causal fine-tune test — are both executed in this paper. The paper's fine-tuning null result also *contradicts* the idea's data-genetics hypothesis.
- **Remaining novelty:** only the formal expressivity question: does there EXIST any prompt for which the decoder emits an open-curve/wiry mask (an output-space characterization, not a performance correlation). That is exactly W2-A-0203.
- **Confidence:** high — the hit is direct, recent, and at the mandated venue tier.
- **Reviewer #2 attack citation:** arXiv:2412.04243, Sec. on fine-tuning: "targeted fine-tuning fails to resolve this issue, indicating a fundamental limitation."
- **Verdict: KILL as stated; merge the expressivity sliver into W2-A-0203.** Demoted from my shortlist.

### W2-A-0206 — SAM fingerprint: assisted datasets carry detectable boundary-style signatures
- **Closest works:**
  - SAFIRE: Segment Any Forged Image Region — https://arxiv.org/html/2412.08197v1 — forensics of forged image regions using SAM (opposite direction: SAM as tool, not SAM as artifact source).
  - GAP-SAM / SARIF / Detective SAM (2025–26, e.g. https://arxiv.org/html/2608.20929) — image-manipulation localization built on SAM backbones.
  - Model-collapse/inbreeding line: A Tale of Tails: Model Collapse as a Change of Scaling Laws — https://doi.org/10.48550/arxiv.2402.07043.
- **What they did:** the forgery-forensics line detects *image* manipulation; the collapse line studies recursive training on generated *data*. Nobody detects machine-annotation style in *mask geometry* or measures its inheritance into downstream models.
- **Exact difference:** target artifact is the mask (boundary micro-statistics: curvature spectra, vertex regularity, snapping-to-edges behavior), not the image; and the ecosystem measurement (prevalence in recent public datasets, inheritance coefficient of the style) has no counterpart.
- **Remaining novelty:** high. This is the flagship of the data-genetics cluster and my searches found no direct competitor.
- **Confidence:** medium — absence of evidence across two searches; a dedicated "detect pseudo-label provenance" niche could exist under other keywords.
- **Reviewer #2 attack citation:** GAN-fingerprint style argument: "model attribution from outputs is an old idea; applying it to masks is incremental." Rebuttal lives in the ecosystem-inheritance measurement, which has no analog.
- **Verdict: SURVIVE.**

### W2-A-0026 — Masklet drift predictable from frame-0 ambiguity
- **Closest works:**
  - SAM2Long (ICCV 2025) — https://openaccess.thecvf.com/content/ICCV2025/papers/Ding_SAM2Long_Enhancing_SAM_2_for_Long_Video_Segmentation_with_a_ICCV_2025_paper.pdf — documents SAM2 error accumulation and fixes it with a memory tree.
  - Prompt Self-Correction for SAM2 (Electronics 2025) — https://www.mdpi.com/2079-9292/14/18/3602 — detects mask inconsistency *online* from object-pointer drift.
  - SAM2Dual — https://arxiv.org/html/2608.18640 — dual memory against drift.
- **What they did:** characterized and mitigated error accumulation; detection is reactive (during tracking).
- **Exact difference:** nobody tests whether *pre-tracking, frame-0 static measurements* (prompt-jitter variance, head disagreement) predict the per-object drift RATE — i.e., whether drift is ambiguity amplification rather than accumulating temporal error. That is a causal-structure claim about where VOS failure comes from, with a cheap triage application.
- **Remaining novelty:** good. The prediction study is unpublished; the mitigation literature actually strengthens motivation.
- **Confidence:** medium-high.
- **Reviewer #2 attack citation:** SAM2Long: "drift is a memory-selection artifact, already fixed by better memory — your static predictor explains the fixed part, not the residual."
- **Verdict: SURVIVE**, with mandatory positioning against SAM2Long-class fixes (test prediction on both vanilla and memory-fixed SAM2).

### W2-A-0051 — Train on rater-disagreement-preserving labels vs consensus
- **Closest works:**
  - Lemay et al., Label fusion and training methods for reliable representation of inter-rater uncertainty — MELBA 2022 — https://doi.org/10.48550/arxiv.2202.07550 / https://beta.melba-journal.org/papers/2022:031.html — directly compares STAPLE vs rater-average vs per-rater random sampling, under two training frameworks, on two public multi-rater datasets, measuring calibration, inter-rater-variability preservation, and segmentation performance.
  - EDUE: Expert Disagreement-Guided Uncertainty Estimation — https://arxiv.org/html/2403.16594 — random-sampling of annotators during training, calibration vs expert disagreement.
  - Supervised UQ with Multiple Annotations (Prob U-Net line) — https://ar5iv.labs.arxiv.org/html/1907.01949 — intergrader variability as aleatoric target.
  - Rater-specific Bayesian nets — https://doi.org/10.48550/arxiv.2306.16556.
- **What they did:** exactly the proposed comparison, including the calibration-vs-accuracy trade-off, across modalities and data splits.
- **Exact difference:** essentially none; the idea's own "<2 Dice cost" quantifier is the only unclaimed decimal.
- **Remaining novelty:** negligible.
- **Confidence:** high.
- **Reviewer #2 attack citation:** Lemay et al. 2022 — "this exact comparison, with the same three fusion regimes, is Table 1 of a journal paper."
- **Verdict: KILL.** (Already KILL in my scores; confirmed.) The nearby survivor is W2-A-0075 (outcome-anchored minority-erasure), which asks a question this literature does not.

### W2-A-0060 — Partial-label multi-dataset training teaches 'organ X is background'
- **Closest works:**
  - Shi et al., Marginal loss and exclusion loss for partially supervised multi-organ segmentation — https://doi.org/10.48550/arxiv.2007.03868 — names the exact mechanism (background is a merged label of unlabeled organs) and fixes it.
  - COSST — https://doi.org/10.48550/arxiv.2304.14030 — comprehensive supervisions + self-training for partial labels.
  - ConDistFL — https://arxiv.org/html/2412.18833v2 — federated variant, explicitly states unlabeled-class-to-background misassignment as the core failure.
- **What they did:** identified the poisoning mechanism years ago and built loss-level mitigations that are now standard.
- **Exact difference:** the *quantified dose-response curve* (recall suppression vs unlabeled-appearance frequency) and the comparison of poisoning effect size against architecture-choice effect size are not published; neither is an audit of how completely marginal-loss-style fixes recover the un-poisoned model.
- **Remaining novelty:** low-to-moderate; it is a measurement wrapper around a solved-in-practice problem.
- **Confidence:** high.
- **Reviewer #2 attack citation:** Shi et al. 2021 — "the problem statement is the related-work section of a 4-year-old paper."
- **Verdict: MUTATE.** Mutation: reframe as "how much background poisoning do the standard fixes actually leave on the table" — a mitigation-completeness audit with the dose-response law as the instrument. BORDERLINE at best.

### W2-A-0076 — Smoke has no true binary boundary: rankings flip under density labels
- **Closest works:**
  - SFMatting-800: smoke/fire alpha-matting dataset — https://dl.acm.org/doi/fullHtml/10.1145/3652628.3652632 — alpha mattes for fire/smoke exist as ground truth.
  - DenSiSeg: density-aware progressive smoke segmentation (Pattern Recognition) — https://www.sciencedirect.com/science/article/abs/pii/S003132032501180X — generates density information, density-aware training.
  - Industrial toxic-emission segmentation with opacity-stratified evaluation — https://doi.org/10.48550/arxiv.2507.22002 — evaluates separately on high/low-opacity smoke.
- **What they did:** built soft/density labels and density-aware methods; evaluation is starting to stratify by opacity.
- **Exact difference:** nobody has (a) measured inter-annotator agreement on binary smoke masks vs model-model agreement (the "benchmarks measure style" claim), or (b) re-scored the existing binary-benchmark leaderboard against density references and reported rank flips.
- **Remaining novelty:** moderate — the audit is unpublished, but the field is visibly migrating to density labels, so the window is closing and the "binary masks are wrong for smoke" message alone is no longer novel.
- **Confidence:** high.
- **Reviewer #2 attack citation:** SFMatting-800 — "the field already annotates smoke with alpha; you're auditing yesterday's benchmarks."
- **Verdict: MUTATE.** Mutation: lead with the agreement analysis (human-human < model-model = style measurement) and the rank-flip audit; use SFMatting-800 itself as one density reference to avoid synthetic-only criticism.

### W2-A-0107 — Depth-sensor dropout is free glass supervision at fleet scale
- **Closest works:**
  - Self-Supervised Transparent Object Depth Completion Using Depth from Non-Transparent Objects — https://arxiv.org/html/2512.05006v1 — masks depth of opaque objects to simulate transparent-object depth deficits (inverse use of the cue).
  - SILICA: joint glass segmentation and depth — https://ar5iv.labs.arxiv.org/html/2607.24249 — documents that depth sensors fail on glass and uses predicted masks to filter invalid sensor points.
  - Bootstrap Perception Under Hardware Depth Failure — https://www.arxiv.org/pdf/2603.28890 — quantifies massive ToF invalidity on glass/polished surfaces in deployment.
- **What they did:** use depth invalidity as a phenomenon to work around, or masks to filter it; some works use invalidity as a heuristic cue.
- **Exact difference:** no work trains RGB glass segmentation *purely from mined LiDAR/ToF invalid-return masks* with geometric filtering of confounders (black/absorbing surfaces, range limits, sun glare), and none tests the fleet-scale scaling claim (>70% of supervised accuracy, improving with fleet-hours).
- **Remaining novelty:** moderate-to-good; the scaling-law leg is what makes it a paper rather than a trick.
- **Confidence:** medium — automotive industry may have internal versions; academic literature shows fragments only.
- **Reviewer #2 attack citation:** SILICA — "depth invalidity on glass is a known, exploited signal."
- **Verdict: MUTATE.** Mutation: make the paper about the *supervision purity* question — what fraction of invalid returns are glass (per sensor, per scene type), how far geometric filtering pushes it, and how pseudo-label accuracy scales with data volume. The confound taxonomy is itself a contribution.

### W2-A-0145 — Findability bias: COD datasets contain only failed camouflage
- **Closest works:**
  - Camera-trap ML bias literature: Understanding External Influences on Target Detection... — https://pmc.ncbi.nlm.nih.gov/articles/PMC9319727/ — detection probability depends on camouflage-like factors; AI/citizen-science classification bias — https://doi.org/10.1111/2041-210x.70132.
  - COD failure analyses noting dataset bias (e.g., CSGNet failure cases — https://www.mdpi.com/2079-9292/14/4/779).
- **What they did:** documented that detection probability in camera traps is condition-dependent and that COD models inherit dataset composition biases.
- **Exact difference:** nobody has constructed an evaluation where *presence is known independently of the photograph* (telemetry collars, baited-site logs) to measure recall on present-but-unfound cases; benchmark camouflage difficulty ceilings are therefore unmeasured, which is the idea's selection-bias claim.
- **Remaining novelty:** high; this is a Heckman-style selection correction imported into COD, and I found nothing close.
- **Confidence:** medium (ecology literature is vast; a telemetry-validated detection study may exist under wildlife-survey keywords, though not framed for COD benchmarks).
- **Reviewer #2 attack citation:** occupancy-modeling literature: "ecologists have modeled imperfect detection for decades; what does CV add?" Rebuttal: the object is the CV benchmark's unmeasured ceiling, not the ecological abundance estimate.
- **Verdict: SURVIVE.** Feasibility (data access) remains the honest risk, not novelty.

### W2-A-0151 — Three-way boundary error decomposition (model vs annotation vs metric)
- **Closest works:**
  - Bernhard et al., What's Outside the Intersection? — WACV 2024 — https://doi.org/10.1109/wacv57701.2024.00101 — decomposes segmentation error into boundary/extent/segment categories, all attributed to the model.
  - Boundary IoU — CVPR 2021 — https://arxiv.org/pdf/2103.16562 — used two-expert annotation consistency to set the tolerance parameter d (annotation ambiguity acknowledged, then folded into one scalar).
  - ARLA — https://arxiv.org/html/2607.11214 — evaluation on unreliable labels via resolution adaptation.
- **What they did:** error-type decomposition (model-side), tolerance calibration from annotator consistency, and noise-robust evaluation — three separate fragments.
- **Exact difference:** no published protocol attributes measured boundary error into model / annotation-imprecision / rasterization-metric shares with per-benchmark error budgets; Boundary IoU's d is a global scalar, not a decomposition.
- **Remaining novelty:** good; this is the enforcement instrument several of my Tier-A keeps (0164, 0330, 0305) depend on.
- **Confidence:** medium-high.
- **Reviewer #2 attack citation:** Bernhard WACV 2024 — "error decomposition for segmentation exists." Rebuttal: theirs decomposes *where* errors are, not *whose fault* they are.
- **Verdict: SURVIVE**, mandatory positioning against WACV 2024 and Boundary IoU.

### W2-A-0181 — The abstention cliff: class death as a predictable phase transition
- **Closest works:**
  - Minority/Neural Collapse under imbalance: Space Alignment Matters (AAAI 2026) — https://doi.org/10.1609/aaai.v40i31.39835 — reviews Minority Collapse (Fang et al. 2021): tail classifier weights degenerate under skewed gradients.
  - Frequency-based Matcher for Long-tailed Semantic Segmentation — https://doi.org/10.48550/arxiv.2406.03917 — engineering fix keyed on a frequency threshold.
  - A Tale of Tails — https://doi.org/10.48550/arxiv.2402.07043 — proves sharp phase transitions in tail-cutoff scaling.
- **What they did:** theory predicts tail-class collapse; long-tail seg methods implicitly assume a frequency threshold; phase transitions proven in adjacent settings.
- **Exact difference:** the empirical characterization for segmentation — per-class prediction frequency vs training frequency showing a sharp cliff, threshold predicted by feature-overlap with head classes, invariant across architectures, plus the no-revival-by-longer-training corollary — is not published.
- **Remaining novelty:** moderate-to-good, conditional on engaging Minority Collapse as the candidate mechanism rather than rediscovering it.
- **Confidence:** medium.
- **Reviewer #2 attack citation:** Fang et al. Minority Collapse (PNAS/NeurIPS line, cited in AAAI 2026 above) — "theory already predicts this cliff."
- **Verdict: MUTATE.** Mutation: position as the *empirical test* of minority-collapse predictions in dense prediction, with the feature-overlap threshold as the quantitative bridge between theory and benchmark.

### W2-A-0198 — Seed-churn maps as a free ambiguity atlas
- **Closest works:**
  - On the Reproducibility of Neural Network Predictions — https://arxiv.org/pdf/2102.03349 — churn defined and studied for classification.
  - Bosma et al., Reproducibility of Training DL Models for Medical Image Analysis — MIDL/PMLR 227 — https://proceedings.mlr.press/v227/bosma24a/bosma24a.pdf — retraining variance invalidates significance claims (15% false-significance rate), including segmentation tasks.
  - Lost in the Folds — https://arxiv.org/html/2605.18329 — CV-fold ensembles vs deep ensembles; finds CV-ensemble disagreement correlates with inter-rater variability on multi-rater seg datasets.
- **What they did:** churn for classification; retraining-variance audits; ensemble-disagreement vs rater-disagreement comparisons.
- **Exact difference:** dense pixelwise churn atlases as *stable, transferable dataset properties* matched against human disagreement, and the leaderboard audit (published gains concentrated in high-churn pixels) are unpublished. But Lost-in-the-Folds is uncomfortably close on the disagreement-correlation leg.
- **Remaining novelty:** moderate; the audit application (which benchmark gains live inside the churn band) is the differentiator, and it connects to Bosma's significance findings.
- **Confidence:** medium-high.
- **Reviewer #2 attack citation:** Bosma et al. 2024 — "we already showed retraining variance invalidates leaderboards"; Lost in the Folds — "ensemble disagreement already proxies rater variability."
- **Verdict: MUTATE.** Mutation: center the *audit*: churn-band-aware re-scoring of published deltas, with churn-vs-ensemble redundancy testing as a secondary result.

### W2-A-0245 — UDA methods overfit their development pair
- **Closest works:**
  - Piva et al., Empirical Generalization Study: UDA vs DG — (video/paper) https://www.youtube.com/watch?v=H5IoSdhq_-4 — fair-comparison framework across unseen domains.
  - Self-adaptive inference paper — http://arxiv.org/pdf/2208.05788v1 — builds a "rigorous evaluation protocol that addresses serious limitations of previous work" in UDA/OOD segmentation evaluation.
  - Cross-domain transformer consistency paper — https://arxiv.org/pdf/2211.14703 — explicitly warns that UDA hyperparameters are tuned on Cityscapes val and advocates held-out test sets.
  - HRDA/DAFormer journal version — https://arxiv.org/pdf/2304.13615 — evaluates across 5 benchmarks (but with method-specific tuning).
- **What they did:** protocol critiques and multi-benchmark evaluations exist; individual papers note hyperparameter overfitting risk.
- **Exact difference:** the specific reproducibility statistic — rank correlation of leading UDA methods across ~6 novel shift pairs under FROZEN hyperparameters, vs strong simple baselines — has not been published as a systematic audit.
- **Remaining novelty:** moderate; Musgrave-style "reality check" for UDA segmentation. The classification analog exists, which both helps (template) and hurts (novelty).
- **Confidence:** medium.
- **Reviewer #2 attack citation:** Piva et al. — "UDA generalization has been studied"; rebuttal: they compare UDA-vs-DG mean performance, not method rank stability under frozen HPs.
- **Verdict: MUTATE.** Mutation: pre-register the shift-pair suite and the rank-correlation statistic; include the shift-composition decomposition of W2-A-0226 as the explanatory layer.

### W2-A-0301 — Did SA-1B swallow the test sets?
- **Closest works:**
  - Ramos et al., Data Leakage in Visual Datasets — ICCV 2025 Workshop — https://openaccess.thecvf.com/content/ICCV2025W/Findings/papers/Ramos_Data_Leakage_in_Visual_Datasets_ICCVW_2025_paper.pdf — near-duplicate leakage analysis across 20 splits / 7 visual datasets (pretraining vs training vs benchmark), with measured impact on zero-shot classification, supervised classification, and retrieval.
  - Contamination Detection for VLMs via Multi-Modal Semantic Perturbation — https://arxiv.org/pdf/2511.03774 — behavioral contamination detection for VLMs.
  - WSI benchmark leakage audit — https://arxiv.org/html/2607.12278 — domain-specific contamination forensics.
- **What they did:** Ramos et al. did the near-duplicate methodology and the downstream-impact measurement for visual datasets — the idea's core recipe.
- **Exact difference:** SA-1B specifically, dense segmentation benchmarks (COCO masks, ADE20K, DAVIS) as targets, per-image zero-shot stratification by duplication status, and mask-level memorization signals are not covered (Ramos et al. focus on classification/retrieval-style tasks and other pretraining sets).
- **Remaining novelty:** moderate and shrinking fast; the dense/mask-level angle is real but the methodological novelty is gone.
- **Confidence:** high.
- **Reviewer #2 attack citation:** Ramos et al. ICCVW 2025 — "visual dataset leakage including pretraining sets has been audited."
- **Verdict: MUTATE.** Mutation: SA-1B/DAVIS/COCO-specific audit where the readout is *mask quality on duplicated vs clean images* (dense memorization, not classification accuracy), plus a decontaminated re-ranking of zero-shot segmentation claims.

### W2-A-0326 — 'More context always helps' is false for boundaries
- **Closest works:**
  - Receptive-field studies with non-monotonic aggregate curves: olfactory-bulb interactive segmentation — https://doi.org/10.3389/fninf.2023.1276891 (performance peaks at intermediate RF); TEM RF study — https://ar5iv.labs.arxiv.org/html/2204.04250; amygdala dual-branch RF work — https://airccse.com/adeij/papers/2419adeij04.pdf (small RF better for small-object boundaries).
  - Training-free open-vocab segmentation resolution analysis — https://arxiv.org/html/2411.09219v1 — non-monotonic resolution/RF interplay.
- **What they did:** found non-monotonic RF/context effects on aggregate Dice/mIoU in niche settings; dual-branch designs implicitly encode "small RF for boundaries".
- **Exact difference:** no systematic *property-decomposed* study (region-classification accuracy vs boundary-localization precision as separate curves) across modern architectures showing the sign flip and its scaling; the folklore exists but the signed, property-resolved law does not.
- **Remaining novelty:** moderate; must survive "we knew this" by making the decomposition and cross-architecture invariance the contribution.
- **Confidence:** medium.
- **Reviewer #2 attack citation:** the amygdala/TEM RF papers — "RF non-monotonicity is known."
- **Verdict: MUTATE.** Mutation: masked-attention-radius sweeps on ViT-class models with the two properties measured separately; deliverable is the crossover-scale law per object scale (connects to W2-A-0286's capacity-localization claim).

## Extra targets (ranked at/above the mandated set)

### W2-A-0074 — Volume CIs are anti-conservative under boundary-correlated errors
- **Closest works:**
  - Stochastic Segmentation Networks — NeurIPS 2020 — https://ar5iv.labs.arxiv.org/html/2006.06015 — models spatially correlated aleatoric uncertainty precisely because pixel-independence is wrong.
  - Conformal volumetry: PSMA-TV conformal intervals — https://jnm.snmjournals.org/content/67/supplement_1/262200; CONSeg (AJNR 2025) — https://www.ajnr.org/content/early/2025/07/03/ajnr.A8914; meningioma volumetric credible intervals with empirical coverage — https://doi.org/10.1038/s41746-026-02902-0.
- **What they did:** SSN models the correlation; conformal papers produce *calibrated* volume intervals and evaluate empirical coverage.
- **Exact difference:** nobody has audited the *anti-conservatism factor* of the standard pixel-independent propagation across published uncertainty pipelines (the 2–5x claim), nor attributed it to boundary error correlation lengths; conformal methods sidestep propagation rather than diagnosing it.
- **Remaining novelty:** moderate — the audit + mechanism attribution survives; the "how to get valid intervals" question is being answered by conformal methods.
- **Confidence:** high.
- **Reviewer #2 attack citation:** the conformal volumetry line — "calibrated volume intervals already exist; who needs your propagation fix?"
- **Verdict: MUTATE.** Mutation: the paper is the *coverage audit* of deployed pixelwise-uncertainty pipelines (how wrong, why, correlation-length law), with conformal as the reference upper bound rather than a competitor.

### W2-A-0075 — Consensus fusion erases correct minority-expert detections
- **Closest works:**
  - Dynamic score function for contradictory annotations (IEEE Access 2023) — https://doi.org/10.1109/access.2023.3278275 — shows STAPLE demotes minority classes on Gleason 2019.
  - COLLATE — https://pmc.ncbi.nlm.nih.gov/articles/PMC3150602/ — rater-behavior model mis-specification in STAPLE.
- **What they did:** established that consensus fusion suppresses minority raters/classes as a statistical artifact.
- **Exact difference:** no outcome-anchored audit exists: on cases with confirmed pathology/follow-up, are majority-rejected minority-flagged regions true findings at above-chance rates, concentrated in rare subtypes? That converts a fusion-algorithm complaint into a patient-safety measurement.
- **Remaining novelty:** high; the outcome anchor is the novel instrument.
- **Confidence:** medium-high.
- **Reviewer #2 attack citation:** IEEE Access 2023 — "STAPLE's minority suppression is known." Rebuttal: known as bias, unmeasured as *clinical truth erasure*.
- **Verdict: SURVIVE.** Data access (outcome-linked multi-rater sets) is the honest risk.

### W2-A-0121 — Puddle mirrors cause phantom-object segmentation
- **Closest works:**
  - Han et al., Single Image Water Hazard Detection with Reflection Attention Units — ECCV 2018 — https://openaccess.thecvf.com/content_ECCV_2018/papers/Xiaofeng_Han_Single_Image_Water_ECCV_2018_paper.pdf — detects water via reflection matching (Puddle-1000).
  - FRED: flooded-road dataset — https://arxiv.org/html/2605.22018v2 — documents false positives and phantom-braking risk framing.
- **What they did:** detect puddles as hazards; reflection modeled as a *cue for water*, not as a *source of phantom objects*.
- **Exact difference:** the reverse-direction audit — rate of vehicle/pedestrian false segments spatially coinciding with reflections, verified by mirror-geometry about the road plane, and its absence from benchmark metrics (wet-scene stratification) — is unpublished in academic literature.
- **Remaining novelty:** good; the geometric-verification instrument (mirror symmetry test) is clean and cheap.
- **Confidence:** medium — AV industry has certainly seen this failure internally; academic novelty holds.
- **Reviewer #2 attack citation:** Han et al. 2018 — "reflections in driving scenes are studied." Rebuttal: as water detection, not as phantom-object error class in segmentation benchmarks.
- **Verdict: SURVIVE.**

### W2-A-0148 — Human-AI camouflage teaming: binary masks induce misses
- **Closest works:**
  - Soft-vs-hard highlighting in classifier-assisted visual search (NSF-funded study) — https://par.nsf.gov/servlets/purl/10074164 — soft (graded-confidence) highlighting beats hard highlighting and no-highlight; hard highlighting risks masking non-highlighted targets; anchoring documented.
  - From Model Uncertainty to Human Attention — https://arxiv.org/html/2605.12303 — uncertainty-guided annotation review, automation-bias risks.
  - Who Goes First? (FAccT 2022) — https://doi.org/10.1145/3531146.3533193 — anchoring in clinical human-AI workflows.
- **What they did:** the core psychological claim — output format (graded vs binary) causally changes human search performance, with binary/hard cues inducing misses — is established in the visual-search literature.
- **Exact difference:** not done for camouflage search with segmentation-mask-shaped proposals, and the calibration-quality moderator ("only if uncertainty is exposed AND calibrated") is untested; the "roughly doubles efficiency" effect size for COD is unmeasured.
- **Remaining novelty:** moderate; this is now a domain-transfer + moderator study, not a new phenomenon.
- **Confidence:** high.
- **Reviewer #2 attack citation:** the soft-highlighting study — "soft beats hard is known in visual search."
- **Verdict: MUTATE.** Mutation: COD-specific, with calibration quality experimentally manipulated (well- vs mis-calibrated heatmaps) — the harm condition (miscalibrated overlays net-increase misses) links to W2-A-0188 and is the unpublished piece.

### W2-A-0150 — Boundary GT is scale-relative
- **Closest works:**
  - Sama-COCO re-annotation study (Benchmarking a Benchmark: How Reliable is MS-COCO?) — https://www.alphaxiv.org/abs/2311.02709 — systematic polygon-tightness and occlusion-convention biases between annotation campaigns.
  - Industry annotation guidance (zoom-level effects, e.g. https://ziloservices.com/blogs/polygon-annotation/) — 100% vs 200–400% zoom changes boundary accuracy (practitioner folklore).
  - HCOMP zoom-behavior telemetry — https://doi.org/10.1609/hcomp.v11i1.27555.
- **What they did:** documented that annotation campaigns differ systematically and that zoom is a quality factor; nobody measured a *signed, scale-dependent bias field* in boundary placement or its consequence for mixed-resolution training.
- **Exact difference:** controlled psychophysics (same annotator, same object, manipulated viewing resolution) with a systematic-shift readout is absent from the literature I can find; only noise-level folklore exists.
- **Remaining novelty:** high; also underpins the C07 metrology keeps (0164, 0175).
- **Confidence:** medium-high.
- **Reviewer #2 attack citation:** Sama-COCO — "annotation conventions differ, we know." Rebuttal: convention differences between campaigns ≠ within-annotator scale-dependence law.
- **Verdict: SURVIVE.**

### W2-A-0163 — Stuff-stuff boundaries are measure-zero fictions
- **Closest works:**
  - Boundary IoU — https://arxiv.org/pdf/2103.16562 — sets a single tolerance d from two-expert consistency; acknowledges contour ambiguity.
  - Beyond-IoU error decomposition (WACV 2024) — https://doi.org/10.1109/wacv57701.2024.00101.
- **What they did:** folded boundary ambiguity into one global scalar tolerance; measured object-centric (thing) consistency.
- **Exact difference:** no work measures class-pair-specific transition-band widths for stuff-stuff boundaries (grass-sidewalk, road-shoulder), tests near-chance annotator agreement inside bands, or evaluates band-aware scoring's effect on stuff rankings.
- **Remaining novelty:** good; the ontological framing (bands, not curves) plus the class-pair band atlas is unclaimed.
- **Confidence:** medium-high.
- **Reviewer #2 attack citation:** Boundary IoU — "tolerance for ambiguity already exists in the metric."
- **Verdict: SURVIVE**, positioned as the class-pair-resolved generalization that replaces one scalar with a measured band atlas.

### W2-A-0205 — Verification bias: annotators accept wrong-but-plausible machine masks
- **Closest works:**
  - Just Put a Human in the Loop? (ACL Findings 2025) — https://aclanthology.org/2025.findings-acl.1323.pdf — 410 annotators; reviewing LLM suggestions shifts label distributions toward the model and inflates model-evaluation F1 substantially.
  - Bias in the Loop — https://arxiv.org/pdf/2509.08514 — correction effort reduces revision rates; skeptics adjudicate better.
  - AICL radiology pilot — https://pure.johnshopkins.edu/en/publications/accelerating-voxelwise-annotation-of-cross-sectional-imaging-thro/ — edited-AI labels indistinguishable from expert labels (quality-graded, small n).
- **What they did:** established acceptance/automation bias in assisted annotation, including the evaluation-inflation consequence — for NLP labels and (pilot-scale) medical masks.
- **Exact difference:** for dense masks: acceptance-error rates for plausible-but-wrong *boundary details/small parts*, the *correlated* (same-model-style) structure of accepted errors across a dataset, and the downstream model-training consequence are unmeasured.
- **Remaining novelty:** moderate; the phenomenon is established, the dense-specific correlated-contamination measurement is not.
- **Confidence:** high.
- **Reviewer #2 attack citation:** ACL Findings 2025 — "human-in-the-loop acceptance bias is documented, including eval inflation."
- **Verdict: MUTATE.** Mutation: dense-mask version with the correlation structure (style inheritance) and the train-on-verified-labels leg as the contributions; pairs with W2-A-0206's fingerprint instrument.

### W2-A-0237 — Annotation-convention shift masquerades as domain shift
- **Closest works:**
  - MSeg / label-unification literature: Automated Label Unification with GNNs (NeurIPS 2024) — https://papers.nips.cc/paper_files/paper/2024/file/92af0c8c2664429de2bb44c2692d84ae-Paper-Conference.pdf; UniSeg (ECCV 2022) — https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136880019.pdf; Resolving Inconsistent Semantics — https://arxiv.org/abs/2409.09893.
- **What they did:** treat cross-dataset label-space and convention conflicts as an engineering problem to unify around (taxonomies, losses, embeddings).
- **Exact difference:** nobody has *decomposed measured cross-dataset performance gaps* into appearance shift vs annotation-convention shift by re-annotating target samples under the source protocol; the ">25% of the gap is label sociology" claim is untested, and it would reinterpret published UDA numbers (links to 0245/0226).
- **Remaining novelty:** good.
- **Confidence:** medium-high.
- **Reviewer #2 attack citation:** MSeg — "cross-dataset label conflicts are known and being engineered away."
- **Verdict: SURVIVE**, with mandatory framing as gap-accounting, not another unification method.

### W2-A-0300 — Ensemble gains are collapsing generation by generation
- **Closest works:**
  - Great Models Think Alike and this Undermines AI Oversight — https://doi.org/10.48550/arxiv.2502.04313 — error similarity rises with capability (LLMs).
  - Correlated Errors in Large Language Models — ICML 2025 — https://proceedings.mlr.press/v267/kim25e.html — 350+ LLMs; larger/more accurate models err together; monoculture effects downstream.
  - Quantifying Correlations of ML Models — https://doi.org/10.48550/arxiv.2502.03937 — foundation-model-descended models have correlated errors.
- **What they did:** established rising error correlation and its aggregation consequences for LLMs/classifiers.
- **Exact difference:** the dense-prediction version — longitudinal ensemble-gain-by-cohort-era measurement for segmentation models, with attribution to shared data lineage (SA-1B/LAION descent) and the spatial structure of shared errors — does not exist.
- **Remaining novelty:** moderate-to-good as the explicit dense-vision counterpart with lineage attribution; the conceptual novelty is spent.
- **Confidence:** high.
- **Reviewer #2 attack citation:** Kim et al. ICML 2025 — "model error correlation is established."
- **Verdict: MUTATE.** Mutation: dense-task-specific, era-stratified ensemble-gain decay curves + pixel-level shared-error maps (which image regions the whole ecosystem fails on — connects to W2-A-0290's shared-vs-unique split).

### W2-A-0331 — Dice's gradient pathology on multi-instance images
- **Closest works:**
  - blob loss (Kofler et al., IPMI 2023) — https://arxiv.org/abs/2205.08209 — states the exact premise ("a large foreground instance can dominate minor instances and still produce a satisfactory DSC") and fixes it with instance-wise loss terms.
  - Do We Really Need Dice? / hidden label-marginal biases — https://ar5iv.labs.arxiv.org/html/2104.08717, https://openreview.net/pdf?id=GrFix2vWsh4 — theoretical region-size bias analysis of Dice vs CE.
  - On the dice loss gradient — https://arxiv.org/pdf/2304.04319 — gradient-level analysis of Dice (weighted negative of label, tiny dynamic range).
- **What they did:** the premise is published (blob loss) and loss-level analyses of Dice exist; the community response has been re-lossing.
- **Exact difference:** the *per-instance gradient-share instrumentation during training* (measured starvation ratio vs size disparity), the starvation→per-lesion-recall predictive law, and a *data-side* (not loss-side) fix are unpublished.
- **Remaining novelty:** moderate; the "diagnose, don't re-loss" instrumentation is genuinely missing, but the phenomenon headline belongs to blob loss.
- **Confidence:** high.
- **Reviewer #2 attack citation:** Kofler et al. — "instance imbalance under Dice is the opening paragraph of blob loss."
- **Verdict: MUTATE.** Mutation: mechanism paper — instrument gradient flow, derive the starvation law, test whether blob-loss-style fixes actually equalize gradient shares or just re-weight outcomes, and compare data-side vs loss-side remedies.

### W2-A-0334 — Class-agnostic masks leak semantics
- **Closest works:**
  - Silhouette-based recognition (classical): Mokhtarian & Murase, curvature scale space — https://www.math.ucdavis.edu/~saito/data/morphometrics/mokhtarian-murase_silhouett-obj-rec.pdf; shape-based video object recognition — https://doi.org/10.1109/cvpr.2009.5206803.
  - Privacy-preserving silhouette activity recognition — https://aaai.org/papers/0012-fs08-02-012-privacy-preserving-recognition-of-activities-in-daily-living-from-multi-view-silhouettes-and-rfid-based-training/ — silhouettes used *as* the privacy mechanism.
  - DCNNs and global shape — https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1006613&type=printable.
- **What they did:** shape-only recognition is classical; ironically, silhouettes have been marketed as privacy-preserving.
- **Exact difference:** scale (hundreds of categories with modern classifiers), scene/activity recovery from *mask ensembles*, and the adversarial framing against "semantic-free"/"privacy-preserving mask release" claims are unpublished as a quantified audit.
- **Remaining novelty:** moderate; the "shape predicts category" leg is dead on arrival, the privacy/audit leg survives.
- **Confidence:** high.
- **Reviewer #2 attack citation:** Mokhtarian & Murase 1993 — "silhouette recognition is thirty years old."
- **Verdict: MUTATE.** Mutation: drop the category-prediction novelty claim; the paper is a privacy attack on released mask corpora and "semantic-free" claims (scene, activity, demographics recovery rates from masks alone), with the silhouette literature as the expected-strength prior.

### W2-A-0349 — Human boundary conventions encode function, not photometry
- **Closest works:**
  - Hoffman & Richards minima rule / part-based representations — http://www.doc.gold.ac.uk/%7Effl/MSC101/Bib/Hoffman.pdf — part boundaries at curvature minima; psychophysically real.
  - Single-part superiority effect — https://www.sciencedirect.com/science/article/pii/S0042698903001664.
  - Affordance-guided part decomposition (WACV 2017) — https://doi.org/10.1109/wacv.2017.17 — affordances correlate with semantic parts.
  - Object concepts and action — https://pubmed.ncbi.nlm.nih.gov/14734242/ — part salience predicted by action relevance.
- **What they did:** established the psychophysics (geometric + functional part structure in human perception) and affordance-part correlation in vision systems.
- **Exact difference:** no work measures the *systematic signed divergence between model and human boundary placement at functional junctions* on segmentation datasets, or tests whether "boundary error" partially reflects a convention disagreement rather than model failure.
- **Remaining novelty:** good; it bridges an established psychophysics literature to benchmark metrology, and the signed-offset-per-junction-type instrument is new.
- **Confidence:** medium (perception literature is deep; a direct model-vs-human boundary-convention study could exist under other terms).
- **Reviewer #2 attack citation:** Hoffman & Richards — "human part boundaries are geometric (minima rule), not functional — your dichotomy is miscast." The experiment must disentangle curvature-minima from function, since they correlate.
- **Verdict: SURVIVE**, with the mandatory control: junctions where curvature minima and functional joints dissociate.

### W2-A-0352 — Segmentation-free measurement: when is the mask an unnecessary middleman?
- **Closest works:**
  - Deep Regression vs Detection for Counting (RA-L 2021) — https://doi.org/10.1109/lra.2021.3062586 — regression beats detection-based counting at density (up to 5x lower error).
  - Crowd-counting literature (systematic reviews) — https://doi.org/10.3390/s22145286 — counting-by-regression is the established default at high density.
  - Object Counting Across Modalities survey — https://arxiv.org/html/2608.23845v1 — taxonomizes when segmentation-based counting wins (auditable boundaries) vs regression.
- **What they did:** for COUNTING, the mask-vs-direct question is answered: regression wins in clutter, segmentation wins when boundaries are auditable.
- **Exact difference:** for non-count scalars — area, volume, growth-rate, coverage fraction — under high boundary ambiguity and matched supervision cost, the systematic comparison does not exist; nor does the predicted interaction (direct regression wins exactly where boundary ambiguity is high — the premature-hardening argument).
- **Remaining novelty:** moderate; the counting result is a strong template and a strong prior that the answer is "yes, masks are often unnecessary" — which is good for feasibility, bad for surprise.
- **Confidence:** high.
- **Reviewer #2 attack citation:** the counting literature — "regression-beats-detection is a decade old."
- **Verdict: MUTATE.** Mutation: exclude counting; pre-register the boundary-ambiguity interaction as the hypothesis (mask pipelines lose *specifically* as referent ambiguity grows), across 3 measurement domains (lesion volume, vegetation cover, wound area).

---

## Method note

Searches were run via live web search between the scoring pass and this report (28 ideas, ~30 queries). Confidence levels reflect search coverage, not certainty: "medium" means one or two query angles came back clean but adjacent niches could hide a hit under different keywords. Two ideas changed verdict as a result of the attack (0017 KEEP→BORDERLINE/KILL-as-stated; 0051 confirmed KILL). All 26 others retain their shortlist/borderline status with mutations recorded in `scores.jsonl` notes where material.
