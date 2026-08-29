# Stage 3 — Prior-Work Assassination: Medical / SAM2-memory / Smoke-Fire / Glass / RT clusters

Date: 2026-08-28. Role: Prior-Work Assassin. Default stance: **already published**.
Epistemic status: **REVIEW JUDGMENT based on real, publicly verifiable papers** (all citations below were
web-verified during this pass; none are fabricated). Where an exact claim could not be located,
it is explicitly marked **NOT FOUND** — that is the only novelty currency accepted here.

Inputs: `stage2_top200.md` cluster leads, `literature_anchors.md`, original hypothesis text in
`stage1_supervisor_seed.md` / `stage1_A1.md`.

Schema per target: Closest works → what they did → exact difference → remaining novelty
(NONE / SLIVER / REAL) → confidence → R2 citation (the single rejection weapon) → verdict
(KILL / MUTATE / SURVIVE, killer experiment if it lives).

Scoreboard: **15 KILL / 8 MUTATE (→7 merged mutations) / 5 SURVIVE** out of 28 attacked IDs.

---

## 1. Decoder-local medical gap / preprocess > PEFT — S-041, S-044, A1-034, A1-032

**Hypotheses.** S-041: freezing the encoder and fine-tuning only SAM's decoder closes most of the
MedSAM gap. S-044/A1-034: classical despeckling of ultrasound lifts frozen SAM more than (decoder)
LoRA. A1-032: a 1-D per-organ CT window/level search recovers much of SAM's contrast failure
without training.

**Closest works.**
- Gu et al., *How to build the best medical image segmentation algorithm using foundation models: a
  comprehensive empirical study with Segment Anything Model*, arXiv:2404.09957. Systematically ablated
  **mask-decoder-only vs encoder+decoder** fine-tuning (vanilla and PEFT, 18 combinations, 17 radiology
  datasets). Result: decoder-only is *insufficient*; PEFT on **both** encoder and decoder wins.
- Ma et al., *Segment Anything in Medical Images* (MedSAM), Nature Communications 2024 / arXiv:2304.12306
  — full encoder+decoder fine-tuning, prompt encoder frozen.
- Wu et al., *Medical SAM Adapter*, arXiv:2304.12620 — adapter PEFT on SAM for medical (anchor: crowded).
- Chen et al., *RobustSAM: Segment Anything Robustly on Degraded Images*, CVPR 2024 / arXiv:2406.09627 —
  explicitly discusses restoration-preprocessing as the intuitive alternative and argues learned
  degradation-invariant modules beat it.
- Lee et al., *Practical Window Setting Optimization for Medical Image Deep Learning*, arXiv:1812.00572 —
  learned/optimized CT windowing lifts model performance (pre-SAM).
- SAMCT, arXiv:2403.13258 — expert-chosen per-object CT density windows as standard preprocessing.
  Zero-shot SAM2-on-CT papers routinely apply and ablate windowing (a 2026 SAM2 bone-CT study,
  arXiv:2603.23116, reports windowing alone improving segmentation ~30% over raw HU input; the JMIR
  SAM2 abdominal-organ study, PMC12231515, fixes W/L 400/50 as protocol).

**Exact difference.** S-041's *specific experiment has already been run* by Gu et al. — and the published
answer is the opposite of the hypothesis (freezing the encoder costs substantial Dice; encoder adaptation
matters because SAM's encoder is natural-image-tuned). For A1-032, CT windowing as cheap adaptation is
routine practice and already quantified inside SAM2-CT pipelines; nobody needed a paper titled "window
search as PEFT baseline" because every pipeline does it silently. What is genuinely missing: a
**head-to-head despeckle-vs-LoRA on ultrasound** with matched prompts (NOT FOUND), i.e. the
preprocessing-recovers-≥50%-of-PEFT-gain quantification.

**Remaining novelty.** S-041: **NONE** (question asked and answered, adversely). A1-032: **NONE**
(standard practice, partially quantified). S-044/A1-034: **SLIVER** (the head-to-head number).

**Confidence.** High (S-041, A1-032), Medium-High (S-044/A1-034).

**R2 citation.** Gu et al., arXiv:2404.09957 ("fine-tuning only the mask decoder is generally
insufficient"; encoder+decoder PEFT superior across 17 datasets).

**Verdict.** S-041 **KILL**. A1-032 **KILL** (fold as one row of the baseline table below).
S-044/A1-034 **MUTATE** → one compact falsifier paper: "physics-aware preprocessing vs PEFT on
promptable models." Killer experiment: 3 ultrasound sets (e.g. BUSI, TN3K, CAMUS) + 2 CT organ sets;
frozen SAM/SAM2 with {raw, NLM/despeckled, windowed} × {no FT, decoder LoRA, enc+dec LoRA}, identical
box-prompt protocol; claim lives only if preprocessing recovers ≥50% of the LoRA gain on ≥2 datasets.
Cheap, decisive, and its failure mode (preprocessing erases true boundaries) is itself reportable.

---

## 2. Anisotropy vs "medical" 3D / SAM2-as-video — S-042, A1-039

**Hypotheses.** S-042: the 3D failure is anisotropy, not "medicalness"; isotropic resampling lifts SAM
more than medical fine-tuning. A1-039: treat z as time; prompting the largest-cross-section slice and
propagating bidirectionally beats top-slice propagation ("prompt-slice policy unstudied").

**Closest works.**
- Ma et al., *Segment Anything in Medical Images and Videos: Benchmark and Deployment*, arXiv:2408.03322
  — middle-slice box prompt, bidirectional SAM2 propagation as the **default protocol**, chosen "because
  it usually has the largest object size."
- Dong et al. (Mazurowski lab), *Segment anything model 2: an application to 2D and 3D medical images*,
  arXiv:2408.00756 — sweeps prompt-slice choice (largest slice vs center slice, "F-modes"), propagation
  direction (uni- vs bidirectional, "D-modes"), and prediction channel, across 18–21 datasets.
- BioSAM-2 / Biomedical SAM-2, arXiv:2408.03286 — middle-slice prompting with backward-then-forward
  propagation, citing it as the established choice.
- JMIR AI 2025 SAM2 abdominal CT study (PMC12231515) — explicit ablation of prompt slice position
  (caudal / mid / cranial) per organ.
- MedSAM-2, arXiv:2408.00874 — argues slice order/orientation is not meaningful in medical volumes,
  processes 6 orientations, self-sorting memory (anchor).
- CSAM, *A 2.5D Cross-Slice Attention Module for Anisotropic Volumetric Medical Image Segmentation*
  (PMC11349312) — anisotropy as a first-class problem; nnU-Net (Isensee et al., Nature Methods 2021)
  made spacing-aware resampling doctrine.

**Exact difference.** A1-039's "unstudied prompt-slice policy" is studied to exhaustion — largest-slice
vs middle-slice vs positional prompting, both directions, is literally the ablation grid of
arXiv:2408.00756 and the default in arXiv:2408.03322. For S-042 the *decomposition* is the point:
no paper was found that holds data fixed and measures zero-shot SAM2 propagation Dice as a controlled
function of resampled slice spacing, then compares that lift against a medical fine-tune (NOT FOUND).
Everyone resamples as hygiene; nobody published the causal attribution "anisotropy explains X% of the
'medical' gap."

**Remaining novelty.** A1-039: **NONE**. S-042: **SLIVER→REAL** (confound isolation, one clean curve).

**Confidence.** High (A1-039), Medium (S-042 — absence of the exact decomposition is hard to prove;
some benchmark appendix may contain a spacing ablation I did not find).

**R2 citation.** Dong et al., arXiv:2408.00756 (prompt-slice/direction ablations); Ma et al.,
arXiv:2408.03322 (middle-slice bidirectional as default).

**Verdict.** A1-039 **KILL**. S-042 **MUTATE** → pure confound paper. Killer experiment: fix
TotalSegmentator/AMOS volumes with native spacing ≥3 mm; evaluate frozen SAM2 propagation at
{native, 3 mm, 1.5 mm, 1 mm-iso} resampling vs MedSAM-2/fine-tuned SAM2 at native; report fraction of
the "medical gap" closed by resampling alone, plus Dice-vs-anisotropy-ratio curve across datasets.
Dies if resampling moves Dice <30% as much as fine-tuning.

---

## 3. Nested tumor-in-organ objectness — S-054, A1-040

**Hypotheses.** S-054: SAM's objectness prior prefers the whole organ given a tumor point (LiTS
tumor-in-liver failure law). A1-040: SAM's snap-to-edge prior under-segments infiltrative tumors, error
growing with boundary diffuseness.

**Closest works.**
- Mazurowski et al., *Segment Anything Model for Medical Image Analysis: an Experimental Study*,
  Medical Image Analysis 2023 / arXiv:2304.10517 — dedicates analysis to **nested-object prompt
  ambiguity** ("a point in a necrotic tumor component could mean the component, the tumor, the
  hemisphere, the brain, or the head"), shows multimask outputs on it, reports poor tumor performance.
- Kirillov et al., *Segment Anything*, ICCV 2023 — the multimask output exists precisely because of
  nested-object ambiguity (whole/part/subpart).
- Huang et al., *Segment Anything Model for Medical Images?*, MedIA 2024 — prompt-type sensitivity and
  instability on lesions (anchor).
- Self-Prompt-SAM, arXiv:2502.00630 — documents point prompts collapsing to organ/chest-scale regions.
- He et al., arXiv:2304.09324 — zero-shot SAM worst on small / low-contrast (i.e. diffuse) structures.
- Xu et al., *Flaws can be Applause* (A-SAM), NeurIPS 2024 — treats SAM's ambiguity on nested/multi-rater
  structures (LIDC, BraTS) as a modeling target.

**Exact difference.** The phenomenon (point-in-tumor → organ mask; ambiguity of nested anatomy) is
published with illustrations and numbers. What is NOT FOUND: a **parametric law** — signed boundary
error as a monotone function of a controlled edge-diffuseness parameter (A1-040's synthetic
gradient-width sweep), i.e. failure *prediction* rather than failure *description*.

**Remaining novelty.** S-054: **NONE**. A1-040: **SLIVER** (quantitative law + clinical link).

**Confidence.** High.

**R2 citation.** Mazurowski et al., MedIA 2023 / arXiv:2304.10517 (nested-prompt ambiguity section).

**Verdict.** S-054 **KILL**. A1-040 **MUTATE** → "boundary-diffuseness failure law." Killer experiment:
synthetic lesions with parameterized gradient profile width inserted into real CT/MR backgrounds;
plot signed boundary error vs width for SAM/SAM2/MedSAM; validate the fitted law's prediction on LiTS
infiltrative-vs-circumscribed subgroups. Dies if the relationship is non-monotone or dataset-specific.

---

## 4. Patient-level split leakage — S-068

**Hypothesis.** Image-level splits in SAM-medical fine-tuning papers inflate reported gains;
re-splitting by patient deflates the field.

**Closest works.**
- Yagis et al., *Effect of data leakage in brain MRI classification using 2D CNNs*, Scientific Reports
  2021 (PMC8604922) — slice-level vs subject-level splits inflate accuracy 25–55%; randomized labels
  still reach ~96% "accuracy" under slice-level splits.
- *How You Split Matters*, arXiv:2309.00350 — leakage in longitudinal 3D MRI.
- Rouzrokh et al., *Mitigating Bias in Radiology Machine Learning: 1. Data Handling*, RadioGraphics /
  Radiology: AI 2022 (PMC9533091) — patient-level splitting as the canonical rule, with the liver-MRI
  multi-series example.
- medRxiv 2020.04.23.20076406 — re-analysis of Coudray et al. showing slide-level split inflation.

**Exact difference.** The mechanism, magnitude, and remedy are all published across modalities and
tasks; this is textbook methodology now. The only unpublished piece is a *census*: which specific
SAM/MedSAM fine-tuning papers used image-level splits, and how much their deltas shrink on patient-level
re-splits (NOT FOUND as a SAM-specific audit). That is meta-research/journalism, not a hypothesis —
and its impact depends on shaming, not science.

**Remaining novelty.** **NONE** (phenomenon); SLIVER (SAM-field audit, low scientific ceiling).

**Confidence.** High.

**R2 citation.** Yagis et al., Sci Rep 2021 (PMC8604922).

**Verdict.** **KILL** as a hypothesis. Retain patient-level splitting as mandatory hygiene in every
surviving Windows4 experiment; if an audit is wanted, it is one table inside another paper, not a paper.

---

## 5. SAM2 memory: shuffle / memory-off / recency / position collapse — S-073, S-079, S-081, A1-017

**Hypotheses.** S-073: shuffling slice order breaks vanilla SAM2 but not a bag-of-memory variant.
S-081: disabling memory on 2D stills should recover SAM — otherwise training artifact. S-079: memory
embeddings encode position/order rather than appearance (linear probe). A1-017: occlusion recovery
collapses sharply beyond the memory-bank temporal span.

**Closest works.**
- MedSAM-2, arXiv:2408.00874 — *built its self-sorting memory bank on exactly the S-073 premise*:
  "in medical imaging, the order of slices may not be meaningful"; replaces recency with
  confidence/similarity-sorted memory.
- Dong et al., arXiv:2408.00756 — already runs **memory-cleared vs memory-retained** iterative
  refinement on medical volumes (S-081's ablation, executed), and reports SAM2 ≈ SAM on single-frame 2D.
- Ding et al., *SAM2Long*, ICCV 2025 / arXiv:2410.16268 — diagnoses greedy memory selection and error
  accumulation; training-free memory tree; robust to occlusion/reappearance (A1-017 territory).
- Yang et al., *SAMURAI*, arXiv:2411.11922 — motion-aware memory selection replacing naive FIFO recency.
- Videnovic et al., *DAM4SAM* (distractor-aware memory), arXiv:2411.17576 — introspective memory updates.
- SLM-SAM 2, arXiv:2505.01854 — short/long memory banks against over-propagation in medical volumes.
- *An Analysis of Segment Anything 2*, arXiv:2503.00042 — begins interpretability of memory
  cross-attention and object pointers (what memory features/pointers encode).
- Architecture fact (sam2 codebase, facebookresearch/sam2): only 6 learned temporal-position encodings
  for recent-frame memories + 1 for prompted frames — the "explicit constant" A1-017 wanted to expose
  is already visible in code and is what SAM2Long/SAMURAI exploit.

**Exact difference.** The recency/greedy-memory pathology is diagnosed and repeatedly fixed (a crowded
fix-market: SAM2Long, SAMURAI, DAM4SAM, SLM-SAM2, MedSAM-2). Memory-off and order-direction ablations on
medical exist. What is NOT FOUND: a **representation-level probe** of memory content — training linear
probes on memory-bank embeddings to quantify position-vs-appearance information, and linking probe
readout to propagation failure. Nobody has published *what the memory actually encodes*; they publish
*replacements* for it.

**Remaining novelty.** S-073: **NONE** (premise consumed by MedSAM-2; shuffle diagnostic is one figure,
not a paper). S-081: **NONE** (done). A1-017: **NONE→SLIVER** (cutoff plot vs bank size is quantification
of a known failure with existing fixes). S-079: **REAL** (mechanistic content analysis absent).

**Confidence.** High (S-073, S-081, A1-017), Medium (S-079 — interpretability work is accelerating;
arXiv:2503.00042 is adjacent and could scoop within months).

**R2 citation.** MedSAM-2 arXiv:2408.00874 (order-meaninglessness + sorted memory); SAM2Long
arXiv:2410.16268 (error accumulation, occlusion).

**Verdict.** S-073 **KILL**, S-081 **KILL**, A1-017 **KILL**. S-079 **SURVIVE**. Killer experiment for
S-079: freeze SAM2; run medical volumes and natural videos; extract memory-bank entries; train linear
probes for (a) frame/slice index, (b) object/organ identity, (c) appearance cluster; report probe
accuracy ratios and correlate position-dominance with propagation failure cases; then a causal check —
permute temporal-position encodings at inference and measure Dice damage vs permuting memory features.
Dies if appearance information dominates or if position-dominance fails to predict failure.

---

## 6. One-prompt drift — S-074

**Hypothesis.** One prompt on slice 0 degrades with slice distance; a drift curve (Dice vs Δslice)
falsifies one-prompt-per-volume claims.

**Closest works.**
- Dong et al., arXiv:2408.00756 — measured exactly this: single prompt for the whole volume averages
  0.36 vs 0.50 with per-slice prompts; performance decreases with distance from the annotated slice;
  attributes it to propagation error accumulation (prompted-slice IoU stays consistent).
- Ma et al., arXiv:2408.03322 — over-segmentation on the prompted middle slice propagates through PET
  volumes; initializing with better middle-slice masks lifts 3D DSC up to 17.5%.
- SAM2Long, arXiv:2410.16268 — quantifies performance decline over propagation segments (natural video).

**Exact difference.** None of substance. The drift curve exists in multiple benchmarks; the
"one-prompt overclaim" critique is already the stated motivation of SLM-SAM 2 and MedSAM-2 follow-ups.

**Remaining novelty.** **NONE**.

**Confidence.** High.

**R2 citation.** Dong et al., arXiv:2408.00756.

**Verdict.** **KILL**.

---

## 7. Smoke as alpha / metric reversal / ontology — S-096, S-097, A1-046

**Hypotheses.** S-097: smoke is a density field, not an instance — instance-SAM cannot represent
overlapping plumes. A1-046: add a small alpha-regression head to SAM. S-096: model rankings reverse
under alpha-MAE vs binary Dice.

**Closest works.**
- Yuan et al., *A Wave-Shaped Deep Neural Network for Smoke Density Estimation*, IEEE TIP 2020 —
  single-image smoke **density regression**; density explicitly framed as the right target for
  segmentation/detection.
- Yuan et al., *Deep Smoke Segmentation*, Neurocomputing 2019 / arXiv:1809.00774 — synthetic smoke via
  alpha compositing; **ground truth is the alpha channel** (DS01–03 datasets); evaluation includes
  per-pixel MSE against alpha.
- Yan et al., *Transmission-Guided Bayesian Generative Model for Smoke Segmentation*, AAAI 2022 —
  transmission (≈alpha) as physical guide; models labeling uncertainty; SMOKE5K dataset.
- Li et al., *Matting Anything (MAM)*, CVPR Workshops 2024 / arXiv:2306.05399 — **lightweight
  Mask-to-Matte head (2.7 M params) on frozen SAM** predicting alpha mattes from box/point/text prompts.
  Yao et al., *Matte Anything*, arXiv:2306.04121 — same territory.
- Anchor: density-aware progressive smoke segmentation with SAM background priors (Pattern Recognition).
- Rhemann et al., *A Perceptually Motivated Online Benchmark for Image Matting*, CVPR 2009 — the
  standard alpha-error metric suite (SAD/MSE/gradient/connectivity).

**Exact difference.** The ontology claim (S-097) is 5+ years old in the smoke literature — density/
transmittance regression IS the published reformulation. The architecture claim (A1-046) is MAM with
the word "smoke" substituted. The one thing NOT FOUND: a **metric-validity study** — take N published
smoke segmenters, score them under binary IoU/Dice vs alpha-MAE on alpha-GT data, and show rank
reversal (Kendall τ), i.e. evidence that the field's leaderboards are metric artifacts.

**Remaining novelty.** S-097: **NONE**. A1-046: **NONE** (domain port of MAM). S-096: **SLIVER→REAL**
(nobody has run the reversal study; all ingredients exist).

**Confidence.** High.

**R2 citation.** Yuan et al., IEEE TIP 2020 (smoke density estimation); Li et al., arXiv:2306.05399 (MAM).

**Verdict.** S-097 **KILL**. A1-046 **KILL**. S-096 **MUTATE** → metric-reversal paper (merge with
S-612/S-632 per seed-2 mutations). Killer experiment: 8–10 published smoke models + MAM + thresholded
SAM on DS01–03 + SMOKE5K(+alpha subset); compute rank correlation between {IoU, Dice} and {alpha-MAE,
SAD, gradient}; deliverable is the τ matrix and reversal cases among top-3 ranks. Dies if rankings are
stable (τ > 0.8 everywhere) — publish that as a negative result note instead.

---

## 8. Smoke inter-rater ceiling — S-102, A1-054

**Hypothesis.** Inter-annotator IoU on smoke boundaries (~<0.75) is below many published improvement
deltas, bounding meaningful progress; nobody has measured it.

**Closest works.**
- Hyperspectral smoke segmentation dataset paper, arXiv:2602.10858 — three annotators per image;
  reports agreement statistics (only 52.07% of smoke-marked pixels unanimous; 33.79% single-annotator),
  explicitly discussing transparent-region disagreement. The "nobody has measured it" premise is dead.
- Zhu et al., *CoSW: Conditional Sample Weighting for Smoke Segmentation with Label Noise*, NeurIPS 2024
  — inevitable noisy labels in smoke datasets as the core problem.
- Yan et al., AAAI 2022 (above) — labeling-level uncertainty modeled explicitly.
- Concentration-weighted forest-smoke segmentation, Electronics 2021 (doi:10.3390/electronics10212675)
  — labeling ambiguity from translucency as motivating problem.
- General multi-rater ceilings are mature methodology: LIDC-IDRI 4-reader masks, QUBIQ challenge
  (used with alpha mattes by Medical Matting, arXiv:2106.09887).

**Exact difference.** Raw disagreement numbers on smoke now exist (hyperspectral, 3 raters), and
smoke-label-noise is an active NeurIPS-level topic. NOT FOUND: the **confrontation** — pairwise
inter-rater IoU ceiling on standard RGB benchmarks (SSD/SMOKE5K/DS0x-real) tabulated against the
published SOTA deltas on those same benchmarks, with the conclusion "K of M reported improvements are
below the annotation ceiling."

**Remaining novelty.** **SLIVER** (the confrontation table; measurement itself no longer novel).

**Confidence.** Medium-High.

**R2 citation.** arXiv:2602.10858 (inter-annotator smoke statistics); CoSW, NeurIPS 2024.

**Verdict.** **MUTATE** → fold into the S-096 metric paper as its second pillar (ceiling + metric
reversal = one "smoke evaluation is broken" paper). Killer experiment: 3–5 raters × 150 images sampled
from SSD and SMOKE5K test sets; pairwise IoU and alpha-MAE ceilings; overlay published method deltas.
Dies (as a headline) if ceilings exceed 0.85 IoU — then smoke labels are fine and only the metric
critique survives.

---

## 9. Matting→smoke transfer — S-103

**Hypothesis.** Pretraining on alpha-matting data (portrait/natural) transfers to smoke better than
COCO-style segmentation pretraining — the only adjacent-field transfer bet in the pool with a mechanism
(soft boundaries are the shared structure).

**Closest works.**
- Li et al., MAM, arXiv:2306.05399 — trained on five matting datasets, shows cross-task matting
  generalization; smoke never evaluated.
- Yuan et al., arXiv:1809.00774 / TIP 2020 — smoke alpha data exists for the target side.
- He, Sun & Tang, *Single Image Haze Removal Using Dark Channel Prior*, CVPR 2009 / TPAMI 2011 —
  transmission estimation of haze ≈ physics alpha for smoke-like media (training-free adjacent prior).
- Sun et al., *Semantic Image Matting* and general matting-transfer literature exist, but no
  matting→smoke transfer study was located. **NOT FOUND**: any controlled comparison of matting-pretrained
  vs segmentation-pretrained models on smoke alpha/segmentation.

**Exact difference.** All ingredients published, the transfer claim itself untested. Risk is scientific,
not novelty: transfer may simply fail (domain gap portrait→volumetric media), and MAM makes the
engineering trivial, so speed matters.

**Remaining novelty.** **REAL** (narrow but clean, mechanism-bearing).

**Confidence.** Medium (the space around MAM applications moves fast).

**R2 citation.** MAM arXiv:2306.05399 is what a reviewer will wave — answer is that MAM never touched
smoke and the claim is about *pretraining data provenance*, not architecture.

**Verdict.** **SURVIVE**. Killer experiment: identical architecture (MAM head), three pretraining
regimes — (a) COCO/SA-1B segmentation, (b) portrait/natural matting (P3M-10k, AIM-500, Composition-1k),
(c) scratch — fine-tuned with matched budgets on limited smoke alpha data (DS01–03 splits), tested on
SMOKE5K-real and held-out synthetic; report alpha-MAE and sample-efficiency curves; dark-channel
transmission as training-free floor. Claim lives only if matting-pretrain beats segmentation-pretrain
beyond seed noise at every data budget, and the gap grows as smoke data shrinks.

---

## 10. Detector-matched fire SAM — S-126

**Hypothesis.** "Fire segmentation with SAM2" papers are detector-prompted SAM2; gains vanish when
detector AP is matched — an assassination experiment against ProFSAM-style pipelines.

**Closest works.**
- Ugwu & Zhang, *Promptable Fire Segmentation…* (ProFSAM), arXiv:2510.21782 (ICIGP 2026) — YOLOv11n
  boxes → SAM2/MobileSAM/TinySAM; box prompts beat point/auto; the pipeline S-126 wants to attack,
  confirmed real and structured exactly as assumed.
- Huang et al., MedIA 2024 and the broad prompt-sensitivity literature — mask quality tracks prompt/box
  quality; box > point robustness is documented across domains.
- Dong et al./Ma et al. benchmarks — initializing SAM2 with better masks/boxes improves everything
  downstream (same attribution logic).

**Exact difference.** That segmentation quality is chiefly a function of prompt quality is established;
a detector-AP-matched decomposition specifically for fire pipelines is NOT FOUND — but it is a
*rebuttal experiment*, not a standalone contribution. Its result is foreordained by the prompt-sensitivity
literature, and its only publishable form is inside an evaluation-protocol paper.

**Remaining novelty.** **SLIVER** (attribution experiment; conclusion predictable).

**Confidence.** Medium-High.

**R2 citation.** arXiv:2510.21782 (the target itself concedes prompts dominate: box strategies decide
performance).

**Verdict.** **MUTATE** → absorb into the prompt-distribution evaluation cluster (A1-118/A1-091,
cluster 31): a protocol requiring detector-prompted segmentation papers to report gains *conditional on
prompt AP*, demonstrated on fire + medical + glass. As a standalone: dead on arrival at any venue that
isn't a comment track.

---

## 11. Time-to-alarm vs mIoU — S-109, S-134

**Hypotheses.** Early-warning needs detection of thin smoke, not IoU; time-to-alarm is the metric that
matters and is uncorrelated with mIoU; "task redefinition."

**Closest works.**
- Dewangan et al., *FIgLib & SmokeyNet*, Remote Sensing 2022 (doi:10.3390/rs14041007) — wildfire smoke
  benchmark whose headline metric **is time-to-detection in minutes** (TTD tables across architectures;
  3.12 min baseline), including the observation that a low-TTD model (ResNet50, 1.01 min) is unusable
  due to false positives — i.e. the accuracy/TTD tension is already displayed.
- *Multimodal Wildland Fire Smoke Detection*, arXiv:2212.14143 — optimizes and reports TTD deltas.
- Fire-detection standards practice (UL 268 / EN 54 style time-to-alarm) long predates all of this.

**Exact difference.** The metric exists, is primary in the flagship wildfire benchmark, and is actively
optimized. NOT FOUND: a formal correlation study TTD-vs-mIoU across *segmentation* models specifically.
That residue is one scatter plot, and FIgLib's own tables already gesture at it.

**Remaining novelty.** **NONE** for the "task redefinition" claim; SLIVER for the correlation plot.

**Confidence.** High.

**R2 citation.** Dewangan et al., Remote Sensing 14(4):1007, 2022.

**Verdict.** **KILL** both. If the correlation plot is wanted, it is one figure inside the S-096/S-102
smoke-evaluation paper, using FIgLib sequences with segmentation heads.

---

## 12. Glass refraction warp / two-frame parallax — A1-058, A1-063, A1-067

**Hypotheses.** A1-058: background-warp magnitude predicts SAM's per-instance transparent-object IoU.
A1-063: two-frame parallax mismatch between SAM-feature flow and pixel flow localizes refractive
regions, training-free. A1-067: refraction measurably warps ViT feature consistency, matching optical
predictions — mechanistic bridge.

**Closest works.**
- Han et al., *SAM Meets Glass: Mirror and Transparent Objects Cannot Be Easily Detected*,
  arXiv:2305.00278 — SAM fails on glass/mirrors; far below GDNet/TransLab/EBLNet.
- Xu et al., *TransCut*, ICCV 2015 — light-field distortion/linearity as the transparency signal
  (refraction-as-cue precedent, but requires light-field capture).
- Xue et al., *Refraction Wiggles for Measuring Fluid Depth and Velocity from Video*, ECCV 2014 —
  refraction-induced motion-of-motion features across frames; physics-violation-as-signal precedent,
  for fluids, on classical intensity features.
- Xie et al., Trans10K/TransLab, ECCV 2020; Mei et al., GDNet, CVPR 2020 — the supervised baselines and
  datasets.
- Glass-SAM, ICASSP 2026 (doi:10.1109/icassp55912.2026.11461633) — SAM enhanced for transparent objects
  via fractal/shape-context signals — the SAM-for-glass fix-market has opened.

**Exact difference.** Refraction-as-signal exists in light-field (TransCut) and video-magnification
(wiggles) form. NOT FOUND: (a) monocular warp-magnitude as a *per-instance failure predictor* for a
foundation model (A1-058); (b) the *foundation-feature vs pixel-flow* mismatch detector from two
ordinary frames (A1-063); (c) any quantitative regression of ViT feature displacement against optically
predicted refraction warp (A1-067). The novelty is moving the physics violation into foundation-model
representation space.

**Remaining novelty.** A1-058: **SLIVER** (predictor, useful but incremental once 063/067 exist).
A1-063: **REAL**. A1-067: **REAL**.

**Confidence.** Medium (transparent-object niche is small; light-field and polarization threads could
hide a variant — polarization-cue glass segmentation exists, e.g. Mei et al. CVPR 2022, but that is a
sensor cue, not a representation-physics claim).

**R2 citation.** TransCut ICCV 2015 + Xue et al. ECCV 2014 (reviewer: "refraction cues are old");
answer: those need light-field/known-background video; ours reads the violation out of frozen ViT
features from two ordinary frames.

**Verdict.** A1-058 **MUTATE** → the validation section of A1-063 (warp magnitude as the continuous
regressor behind the detector). A1-063 **SURVIVE**. Killer experiment: small-baseline two-frame captures
(handheld) over glass scenes (subset of Trans10K/GDD re-shot + new captures); compute RAFT pixel flow vs
SAM/DINOv2 feature-correspondence flow; mismatch-map AUROC against glass masks; training-free baselines
(saliency, monodepth discontinuities, dark-channel) and supervised ceiling (GDNet). Dies if mismatch
AUROC ≤ saliency baseline or if it fires equally on mirrors/specular metals (no refraction). A1-067
**SURVIVE** as the mechanistic companion: Mitsuba renders with known IOR/geometry → predicted warp
field; regress per-patch ViT feature displacement on predicted optical warp (report R²); then test the
implied analytic correction on real captures. Dies if feature warp is dominated by attention context
rather than geometry (R² ≈ 0) — itself a reportable negative.

---

## 13. Depth-edge auto-prompt for glass — A1-060

**Hypothesis.** Monocular-depth discontinuities generate boxes that recover most of manual-prompt SAM
IoU on glassware — chaining two frozen models where each alone fails.

**Closest works.**
- Han et al., arXiv:2305.00278 — SAM alone fails on glass (one half of the premise, published).
- Sajjan et al., *ClearGrasp*, ICRA 2020 / arXiv:1910.02550 — depth sensors/monodepth fail on
  transparency (the other half, published); predicts masks+normals+boundaries to fix depth — the
  *reverse* chaining direction.
- Glass-SAM, ICASSP 2026 — SAM+priors for glass, but via fractal/shape-context, not depth prompts.
- General auto-prompting SAM via auxiliary models is a large genre (detector boxes, saliency, text).

**Exact difference.** The specific chain (monodepth edge → box prompt → SAM, evaluated on
Trans10K/GDD against manual prompts) is NOT FOUND. But novelty is compositional, not conceptual: both
failure modes are documented, auto-prompting is a genre, and modern monodepth (Depth Anything class)
behaves inconsistently on glass — the chain's premise (depth *edges* are reliable where depth *values*
are not) is the one genuinely untested claim.

**Remaining novelty.** **SLIVER→REAL** (one clean system-science result; C1 audit revived it for a reason).

**Confidence.** Medium.

**R2 citation.** ClearGrasp ICRA 2020 (reviewer: "depth fails on glass, your prompt source is broken");
answer: that failure has structure — boundaries survive — and we quantify exactly how much.

**Verdict.** **SURVIVE** (junior-scope). Killer experiment: MiDaS + Depth-Anything edges → boxes → SAM
on Trans10K and GDD; report % of manual-prompt IoU recovered, stratified by glass type; ablate edge
source (depth vs RGB Canny vs learned boundary); include the failure taxonomy where depth hallucinates.
Dies if RGB edges do as well as depth edges (then the depth model contributes nothing) — that control
is mandatory.

---

## 14. Partial-volume as alpha — S-395

**Hypothesis.** CT partial volume IS alpha matting; unify the two, import the matting toolbox
(protected in Stage 2 as cross-domain unification).

**Closest works.**
- Wang et al., *Medical Matting: Medical Image Segmentation with Uncertainty from the Matting
  Perspective*, MICCAI 2021 + Computers in Biology and Medicine 2023 / arXiv:2106.09887 — alpha matte
  as soft mask for ambiguous lesions; created medical alpha-matte datasets (LIDC-IDRI, QUBIQ
  brain-growth, ISIC); argues alpha > binary as a labeling method.
- Wang et al., *3D Matting: a benchmark study on soft segmentation for pulmonary nodules in CT*,
  Computers in Biology and Medicine 2022 — ports 2D matting algorithms to 3D CT, **calibrates the alpha
  matte with radiodensity**, builds the first 3D medical matting dataset and end-to-end 3D matting net.
- MICCAI 2024, *Multi-scale Region-aware Implicit Neural Network for Medical Images Matting* — the
  medical-matting line is active.
- Van Leemput et al., *A unifying framework for partial volume segmentation of brain MR images*,
  IEEE TMI 22(1):105–119, 2003 — partial volume as explicit mixture fractions via EM; fractional tissue
  membership is 20+-year-old methodology.

**Exact difference.** The "unification" is published twice over: fractional-membership PV modeling
(2003) and alpha-matting-for-medical with radiodensity calibration (2021–2024). The only unclaimed
scrap: an explicit *physical identity* argument (PV fraction = compositing alpha under the imaging
PSF) validated against downsampled high-resolution ground truth — a corollary, not a paper.

**Remaining novelty.** **NONE** (SLIVER at most, of corollary size).

**Confidence.** High.

**R2 citation.** Wang et al., arXiv:2106.09887 + CBM 2022 3D Matting (radiodensity-calibrated alpha).

**Verdict.** **KILL**. Withdraw Stage-2 protection; the mature-toolbox import already happened.

---

## 15. Dose-insensitive RT contour errors — S-513

**Hypothesis.** Characterize segmentation errors that do not change dose; clinical relevance over Dice
(protected in Stage 2 as highest-leverage eval idea).

**Closest works.**
- *Clinically Oriented Contour Evaluation Using Dosimetric Indices Generated From Automated
  Knowledge-Based Planning*, IJROBP 2019 (S0360-3016(18)34045-8) — KBP-generated plans per contour
  variant; geometric-dosimetric correlation weak (R² < 0.2 in 61% of 126 correlations); no geometric
  threshold for acceptability exists; geometric indices are poor classifiers of dosimetric impact.
- Sherer et al., *Metrics to evaluate the performance of auto-segmentation for radiation treatment
  planning: a critical review*, Radiotherapy & Oncology 2021 (PMC9444281) — field-wide conclusion: DSC/HD
  not correlated with clinically meaningful endpoints.
- *The predictive value of segmentation metrics on dosimetry in organs at risk of the brain*,
  Radiother Oncol 2021 (PMID 34293536) — Pearson ≈ −0.11 between Dice and mean-dose effect; direction of
  contour variation relative to target is what matters (i.e. *which* errors are dose-insensitive:
  already characterized).
- ICCR 2024 (Groningen/NKI/Twente) — DIP/DIE decomposition of dosimetric impact of autosegmentation.
- Medical Physics 2025 wDSC paper (doi:10.1002/mp.17840) — distance-weighted Dice built to encode
  dose-proximity; the "fix" generation has already started.

**Exact difference.** The core claim — many geometric errors don't move dose, Dice can't tell you which,
and error location/direction relative to target governs impact — is the established consensus of a
substantial radiotherapy literature, complete with reviews and second-generation corrective metrics.
Nothing SAM-specific rescues it: swapping the segmenter does not change the evaluation science.

**Remaining novelty.** **NONE**.

**Confidence.** High.

**R2 citation.** IJROBP 2019 KBP contour-evaluation study; Sherer et al. 2021 review.

**Verdict.** **KILL**. Withdraw Stage-2 protection. If Windows4 wants a dose-aware angle, the open edge
is upstream (e.g. propagating promptable-segmentation *uncertainty* into NTCP), but that is a new
hypothesis for Stage 1 recycling, not this one.

---

## NOT FOUND register (exact claims searched and not located — the only live novelty)

1. Head-to-head despeckle/NLM vs LoRA on ultrasound for frozen SAM (S-044/A1-034 sliver).
2. Controlled isotropic-resampling vs fine-tuning decomposition of the SAM2 3D "medical gap" (S-042).
3. Signed boundary error as a parametric function of edge-diffuseness for SAM (A1-040).
4. Linear-probe content analysis of SAM2 memory embeddings (position vs appearance) (S-079).
5. Dice-vs-alpha-MAE model-ranking reversal study on smoke (S-096).
6. RGB-benchmark smoke inter-rater ceiling confronted with published SOTA deltas (S-102/A1-054).
7. Matting-pretrain vs segmentation-pretrain transfer test on smoke alpha (S-103).
8. Detector-AP-matched attribution for fire SAM pipelines (S-126).
9. TTD-vs-mIoU correlation across segmentation models (S-109/S-134 residue).
10. Monocular per-instance warp-magnitude → SAM glass IoU predictor (A1-058).
11. Foundation-feature-flow vs pixel-flow refraction violation detector, two ordinary frames (A1-063).
12. ViT feature-warp regressed against optically predicted refraction warp (A1-067).
13. Monodepth-edge → box → SAM chain evaluated on Trans10K/GDD (A1-060).

## Verdict table

| ID(s) | Verdict | Novelty | Conf. |
|---|---|---|---|
| S-041 | KILL | NONE | High |
| A1-032 | KILL | NONE | High |
| S-044 + A1-034 | MUTATE (preprocess-vs-PEFT falsifier) | SLIVER | Med-High |
| A1-039 | KILL | NONE | High |
| S-042 | MUTATE (anisotropy confound decomposition) | SLIVER→REAL | Med |
| S-054 | KILL | NONE | High |
| A1-040 | MUTATE (diffuseness failure law) | SLIVER | High |
| S-068 | KILL (keep as hygiene) | NONE | High |
| S-073 | KILL | NONE | High |
| S-081 | KILL | NONE | High |
| A1-017 | KILL | NONE→SLIVER | Med-High |
| S-079 | SURVIVE (memory content probe) | REAL | Med |
| S-074 | KILL | NONE | High |
| S-097 | KILL | NONE | High |
| A1-046 | KILL | NONE | High |
| S-096 | MUTATE (metric-reversal study) | SLIVER→REAL | High |
| S-102 + A1-054 | MUTATE (fold into S-096 paper) | SLIVER | Med-High |
| S-103 | SURVIVE (matting→smoke transfer test) | REAL | Med |
| S-126 | MUTATE (fold into prompt-distribution eval, cluster 31) | SLIVER | Med-High |
| S-109, S-134 | KILL | NONE | High |
| A1-058 | MUTATE (validation arm of A1-063) | SLIVER | Med |
| A1-063 | SURVIVE (feature-flow refraction violation) | REAL | Med |
| A1-067 | SURVIVE (feature-warp vs optical warp) | REAL | Med |
| A1-060 | SURVIVE (depth-edge prompts, with RGB-edge control) | SLIVER→REAL | Med |
| S-395 | KILL (withdraw protection) | NONE | High |
| S-513 | KILL (withdraw protection) | NONE | High |

Notes for the supervisor: two Stage-2 *protected* ideas (S-395, S-513) die here — protection was based
on cross-domain elegance, and in both cases the target domain had already built the bridge
(Medical/3D Matting; the radiotherapy geometric-vs-dosimetric literature). The surviving set is
coherent: one representation-science probe (S-079), one transfer bet (S-103), and a three-piece glass
physics program (A1-063 + A1-067, with A1-058 as validation and A1-060 as the applied junior project).
