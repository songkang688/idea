# Stage 3 — Prior-Work Assassination: SAM / evaluation clusters (200→50 pass 1)

Date: 2026-08-28. Role: **Prior-Work Assassin**. Default assumption: each idea is already published.
Epistemic status: **LITERATURE JUDGMENT** based on real, verified papers found via arXiv/web search on 2026-08-28.
Rules followed: no invented citations; every arXiv id below was retrieved and read (abstract + relevant sections) during this pass;
where no prior work was found, it is marked **NOT FOUND** rather than filled in.

Inputs: `stage2_top200.md`, `literature_anchors.md`, stage-1 idea texts (S/A1/C1 files).

Scoreboard: **9 KILL / 3 MUTATE / 3 SURVIVE** across the 15 attacked cluster leads.

Two cross-cutting facts that kill multiple clusters at once:

- **The Moscow group already built the "realistic prompt" evaluation program.** RClicks (NeurIPS 2024) for clicks and
  BREPS (arXiv:2601.15123, 2026) for boxes together cover: real-user prompt collection at scale, prompt-distribution
  models, prompt-marginalized metrics, robustness-to-prompt rankings, and worst-case-realistic prompt search — across
  natural and medical datasets. Any Windows4 idea whose payload is "evaluate promptable models under realistic /
  distributional / perturbed prompts" is now re-implementation.
- **The SAM paper itself pre-empts the multimask "discovery."** Kirillov et al. state the three outputs are designed as
  whole / part / subpart nested granularities, trained with min-loss, and they publish the oracle-vs-argmax gap analysis.

---

## Cluster 1 — Oracle-prompt protocol (S-003, A1-118, C1-115)

Claim under attack: GT-derived prompts inflate SAM claims (S-003: GT-box eval is secretly a detector benchmark);
report prompt-marginalized IoU over a realistic prompt distribution (A1-118); oracle-free auto-prompt evaluation
protocol that preserves rankings (C1-115).

**Closest prior works**
- *RClicks: Realistic Click Simulation for Benchmarking Interactive Segmentation.* Antonov, Moskalenko, Shepelev, Krapukhin, Soshin, Konushin, Shakhuro. NeurIPS 2024 Datasets & Benchmarks. arXiv:2410.11722. https://arxiv.org/abs/2410.11722
- *BREPS: Bounding-Box Robustness Evaluation of Promptable Segmentation.* Moskalenko, Kuznetsov, Dudko, Iasakova, Boldyrev, Shepelev, Spiridonov, Kuznetsov, Shakhuro. 2026. arXiv:2601.15123. https://arxiv.org/abs/2601.15123
- *Segment anything model for medical image analysis: an experimental study.* Mazurowski et al. Medical Image Analysis 2023. https://doi.org/10.1016/j.media.2023.102918
- *Benchmarking Human and Automated Prompting in the Segment Anything Model.* 2024. arXiv:2410.22048. https://arxiv.org/abs/2410.22048
- *AoP-SAM: Automation of Prompts for Efficient Segmentation.* AAAI 2025. arXiv:2505.11980. https://arxiv.org/abs/2505.11980

**What they actually did.** RClicks collected 475K real clicks, fit a "clickability" distribution model, and re-benchmarked
interactive methods as an *expectation over realistic clicks*, showing baseline simulators overestimate performance 5–29%
and that method robustness rankings change — that is prompt-marginalized IoU, published. BREPS did the box version:
a controlled user study of real boxes (desktop vs mobile), IoU heatmaps over box placement, a naturalness-constrained
white-box search for worst-case realistic boxes, and a 15-model × 10-dataset benchmark finding ~30% IoU drops vs the
tight-box protocol; it explicitly states that "tight bbox + small jitter" protocols overestimate deployment quality.
Mazurowski et al. formalized "oracle performance" for SAM in medical imaging and showed prompt simulation dominates results.
arXiv:2410.22048 benchmarked human vs six automated prompting strategies (234K prompt sets) and quantified the auto-vs-human
gap. AoP-SAM builds automated prompt generation with an evaluation protocol (greedy-IoU matching).

**Exact remaining difference.** S-003's specific stunt (swap GT boxes for an actual weak detector, e.g. YOLO, and show the
Dice collapse exceeds the encoder-size effect) is a one-figure corollary of BREPS/RoBox-SAM degradation curves.
A1-118 is RClicks/BREPS verbatim. C1-115's open sliver: whether *auto-prompted* (saliency/detector) evaluation preserves
*model rankings* at zero oracle cost — auto-prompting methods exist, the rank-correlation audit of the protocol itself does not.

**Remaining novelty:** NONE (S-003, A1-118); SLIVER (C1-115 rank-preservation audit).
**Novelty confidence:** 5.
**Reviewer #2 likely citation:** RClicks (arXiv:2410.11722) and BREPS (arXiv:2601.15123).
**Verdict:** **KILL.** (If anything is salvaged, fold C1-115's rank-correlation question into an existing-benchmark appendix, not a paper.)

---

## Cluster 2 — Tight-box image ablation / SAM as box interpolator (S-014, S-604)

Claim under attack: with tight boxes, SAM's decoder barely consults image evidence — ablating/shuffling image content
inside the box should barely change Dice; SAM would then be a box-to-mask shape interpolator.

**Closest prior works**
- *Stable Segment Anything Model.* Fan, Tao, Ke, Ye, Zhang, Wan, Wang, Tai, Tang. 2023. arXiv:2311.15776. https://arxiv.org/abs/2311.15776
- *BREPS* (above), arXiv:2601.15123 — per-pixel IoU heatmaps over box placement; 1-pixel box shifts change IoU sharply.
- *Enhancing MedSAM with a Lightweight Box Predictor.* 2026. arXiv:2606.04705 — documents that box-fine-tuned MedSAM's decoder "learned to expect" box geometry, and that predicted boxes impose a rigid rectangular constraint on irregular lesions.
- *Robust Box Prompt based SAM (RoBox-SAM).* Huang et al. MICCAI MLMI 2024. arXiv:2407.21284 — attention-drift analysis under low-quality boxes.

**What they actually did.** Stable-SAM is "the first comprehensive analysis of SAM's segmentation stability across prompt
qualities" and locates the mechanism in *which image features the mask decoder attends to* under bad prompts — i.e., the
decoder's image-vs-prompt reliance has been studied, from the prompt side. BREPS shows output is a steep function of box
coordinates. The MedSAM box-predictor paper documents box-shaped-mask artifacts and geometric-prior dependence in
box-fine-tuned models. Nobody in these works intervenes on the *image evidence* itself.

**Exact remaining difference.** The direct causal intervention is unrun: freeze the prompt (tight GT box), destroy the image
evidence inside it (zeroed/mean image embeddings, patch-shuffle per S-604, matched-noise interior), and measure Dice as a
function of box tightness and object contrast against a literal box-fill null. All published work perturbs the prompt with
the image fixed; this perturbs the image with the prompt fixed. That is a different experiment and a different claim.

**Remaining novelty:** REAL (narrow but genuine causal gap).
**Novelty confidence:** 4.
**Reviewer #2 likely citation:** Stable-SAM (arXiv:2311.15776) — "decoder feature-activation under prompts already analyzed"; BREPS for sensitivity.
**Verdict:** **SURVIVE.**
**Killer experiment:** 500 COCO + 500 medical (low-contrast) instances, tight GT boxes, four interior conditions
{intact, patch-shuffled (S-604), embedding-zeroed (S-014), luminance-matched noise} × box padding {0, 4, 8, 16 px};
report Dice vs the box-fill-rectangle null and vs object contrast. Pre-register the kill condition: if intact-vs-ablated
Dice gap > 15 points everywhere, SAM "sees" and the interpolator claim dies in one week — publish the null-calibrated
sensitivity curve either way only if the low-contrast regime shows interpolator behavior.

---

## Cluster 3 — Nested-scale multimask, not semantics (S-018, C1-061, A1-003)

Claim under attack: SAM's 3 masks encode nested scale rather than distinct semantic objects (S-018); fine-tuning collapses
multimask diversity, "ambiguity forgetting" (C1-061); mask diversity anti-correlates with texture entropy (A1-003).

**Closest prior works**
- *Segment Anything.* Kirillov et al. ICCV 2023. arXiv:2304.02643. https://arxiv.org/abs/2304.02643
- *Semantic-SAM: Segment and Recognize Anything at Any Granularity.* Li et al. 2023. arXiv:2307.04767. https://arxiv.org/abs/2307.04767
- *GraCo: Granularity-Controllable Interactive Segmentation.* Zhao et al. CVPR 2024 (Highlight). arXiv:2405.00587. https://arxiv.org/abs/2405.00587
- *How to build the best medical image segmentation algorithm using foundation models.* 2024. arXiv:2404.09957 — documents zero-shot forgetting (~35% drops) from SAM fine-tuning regimes.
- *MedSAM / Segment Anything in Medical Images.* Ma et al. Nature Communications 2024. arXiv:2304.12306 — fine-tunes to a single-mask objective by construction.

**What they actually did.** The SAM paper *states the design*: "3 mask outputs is enough for most common cases (nested masks
are often at most three deep: whole, part, and subpart)," trains with minimum-loss over the three heads, and analyzes the
oracle-selection gap. S-018's "discovery" is the documented design intent. Semantic-SAM and GraCo went further and made
granularity an explicit, controllable axis. On C1-061: MedSAM-style fine-tuning discards the multimask heads by construction,
and arXiv:2404.09957 quantifies capability forgetting after fine-tuning — but no paper measures *proposal-diversity collapse*
as a continuous forgetting metric. A1-003's texture-entropy anti-correlation: **NOT FOUND** as a published measurement.

**Exact remaining difference.** S-018: none — measuring nesting frequency confirms the training objective. C1-061: the
diversity-collapse *curve* (pairwise mask IoU / granularity spread pre/post fine-tuning, vs fine-tuning depth and data size)
is unmeasured. A1-003 is a covariate analysis, not a paper.

**Remaining novelty:** NONE (S-018), SLIVER→REAL (C1-061), SLIVER (A1-003).
**Novelty confidence:** 5 (S-018), 3 (C1-061).
**Reviewer #2 likely citation:** SAM paper §Resolving Ambiguity; GraCo.
**Verdict:** **MUTATE** — kill S-018 outright; recast the cluster as C1-061 "ambiguity forgetting": a diversity-retention metric
for fine-tuned promptable decoders, with A1-003's texture entropy as one analysis covariate, differenced against GraCo
(which *adds* granularity control) as the constructive foil.

---

## Cluster 4 — Negative-click paradox / asymmetry (S-005, A1-007)

Claim under attack: negative clicks are asymmetric in value to positive clicks (S-005); negative clicks can non-monotonically
enlarge masks / worsen IoU (A1-007).

**Closest prior works**
- *Reviving Iterative Training with Mask Guidance for Interactive Segmentation (RITM).* Sofiiuk, Petrov, Konushin. 2021 (ICIP 2022). arXiv:2102.06583. https://arxiv.org/abs/2102.06583
- *FocSAM: Delving Deeply into Focused Objects in Segmenting Anything.* CVPR 2024. arXiv:2405.18706. https://arxiv.org/abs/2405.18706
- *DiffClick: Click-Differentiated Enhancement Network for Interactive Segmentation.* 2025 journal preprint (Univ. Leicester repository). https://figshare.le.ac.uk/articles/journal_contribution/DiffClick_Click-Differentiated_Enhancement_Network_for_Interactive_Segmentation/29650265
- *ClickAttention: Click Region Similarity Guided Interactive Segmentation.* 2024. arXiv:2408.06021. https://arxiv.org/abs/2408.06021
- *RClicks* (above) — robustness of methods w.r.t. click patterns, including subsequent corrective clicks.

**What they actually did.** RITM documented that "adding a new click can even make the mask worse, contradicting user
expectations," and fixed it with mask-state conditioning. FocSAM showed SAM specifically suffers catastrophic
one-click collapses (IoU 88.6→12.8 on a later click) and published the ΔIoU-per-click distributions — the "paradox" is
measured, plotted, and mitigated. DiffClick quantified the positive/negative imbalance (failure rate rises ~20% without
negative clicks) and built modules that treat the two click types asymmetrically; ClickAttention decouples them
architecturally. The phenomenon and the asymmetric treatment both exist.

**Exact remaining difference.** A clean *marginal-value-per-click-type at matched budget* law (S-005's precise framing,
FP-reduction vs TP-gain per click) is not published as such — but it is one table inside the existing evaluation frameworks,
and DiffClick's imbalance data already implies its direction.

**Remaining novelty:** SLIVER.
**Novelty confidence:** 4.
**Reviewer #2 likely citation:** RITM Fig. 4 and FocSAM Fig. 1/4 ("already documented, already mitigated").
**Verdict:** **KILL.** (The paradox is prior art twice over; the residual "asymmetry law" table is not a paper on its own.)

---

## Cluster 5 — Prompt-evolution scorer failure vs SAMPOT (S-007, S-347)

Claim under attack: test-time prompt evolution guided by an unsupervised scorer chases high-contrast blobs, not the clinical
target; prompt evolution can lower clinical Dice (protected anti-SAMPOT negative).

**Closest prior works**
- *Task-driven Prompt Evolution for Foundation Models (SAMPOT).* Sathish, Venkataramani, Shriram, Sudhakar. 2023. arXiv:2310.17128. https://arxiv.org/abs/2310.17128

**What they actually did.** SAMPOT evolves prompt locations by gradient ascent on an unsupervised segmentation-quality
regressor (lung X-ray) and improves ~75% of cases. Critically, *SAMPOT's own paper reports the exact failure mode S-007
predicts*: in its failure analysis, the optimized prompt drifts out of the lung field because the scorer prefers wrong
high-scoring masks, and the authors call for safeguard logic. Dedicated systematic negative studies of unsupervised
scorers for prompt evolution: **NOT FOUND**.

**Exact remaining difference.** Scale and system: SAMPOT documents the failure anecdotally on one task with one learned
scorer; nobody has published a systematic audit across scorer families (CRF energy, NCut, predicted-IoU head, learned
regressors) × datasets, measuring *when* the proxy objective anti-correlates with clinical Dice. A pure "SAMPOT fails"
replication (S-347) is a workshop note, not a paper.

**Remaining novelty:** SLIVER.
**Novelty confidence:** 3.
**Reviewer #2 likely citation:** SAMPOT §failure analysis ("the authors already told you this").
**Verdict:** **MUTATE** — drop the anti-SAMPOT framing; the survivable form is a scorer-validity study: "which unsupervised
segmentation-quality proxies are safe optimization targets at test time, and in which contrast regimes do they invert" —
with SAMPOT as one point in the design space, and predicted-IoU miscalibration (Windows4 cluster 26/S-361 lineage) folded in.

---

## Cluster 6 — Human vs simulated clicks (A1-105, C1-003)

Claim under attack: real human clicks differ from GT-derived simulated clicks; simulated-click evaluation is optimistic and
re-ranks methods; simulated clicks leak GT boundary information.

**Closest prior works**
- *RClicks.* Antonov et al. NeurIPS 2024 D&B. arXiv:2410.11722. https://arxiv.org/abs/2410.11722
- *Benchmarking Human and Automated Prompting in the Segment Anything Model (PointPrompt).* 2024. arXiv:2410.22048. https://arxiv.org/abs/2410.22048
- *BREPS* (boxes instead of clicks). arXiv:2601.15123.
- Background: *Large-scale interactive object segmentation with human annotators.* Benenson, Popov, Ferrari. CVPR 2019 — real-annotator click behavior at OpenImages scale.

**What they actually did.** RClicks is this idea, executed at a scale Windows4 could not match: 475K crowdsourced real
clicks, a generative clickability model, first-round real-click evaluation, robustness metrics across user groups
(annotation time varies 3–79% across clicking styles), and the demonstration that baseline center-of-error-region
simulation overestimates real-world performance 5–29% and destabilizes rankings. PointPrompt adds ~200K human prompt sets
across 16 datasets and quantifies human-vs-automated gaps. C1-003's "human NoC systematically worse than simulated NoC"
is RClicks Table 4. A1-105's "collect 1k clicks user study" is strictly dominated (475×).

**Exact remaining difference.** Medical-expert clicks (radiologists vs crowdworkers) are not in RClicks — that residue is a
data-collection exercise, not a hypothesis.

**Remaining novelty:** NONE.
**Novelty confidence:** 5.
**Reviewer #2 likely citation:** RClicks.
**Verdict:** **KILL.**

---

## Cluster 7 — Patch-grid aliasing (A1-002)

Claim under attack: SAM boundary-F oscillates with sub-patch (16 px) image translation; nobody measured patch-grid aliasing
in promptable segmentation.

**Closest prior works**
- *Phase Marginalization for Patch-Grid Instability in Vision Transformers.* 2026. arXiv:2606.08132. https://arxiv.org/abs/2606.08132
- *Alias-Free ViT: Fractional Shift Invariance via Linear Attention.* NeurIPS 2025. arXiv:2510.22673. https://arxiv.org/abs/2510.22673
- *Sub-token ViT Embedding via Stochastic Resonance Transformers.* 2023. arXiv:2310.03967. https://arxiv.org/abs/2310.03967
- Ancestor: Zhang, *Making Convolutional Networks Shift-Invariant Again*, ICML 2019.

**What they actually did.** arXiv:2606.08132 defines patch-grid *phase* as an explicit nuisance variable for dense ViT
prediction, measures sub-patch phase instability near semantic boundaries (segmentation and depth), and gives a training-free
phase-marginalization fix with cost–accuracy scaling. Alias-Free ViT formalizes and fixes fractional-shift aliasing in ViTs.
SRT exploits sub-token translations to recover beyond-Nyquist detail from frozen ViTs. The phenomenon, the measurement
methodology, and two remedies are published.

**Exact remaining difference.** Running the same measurement on SAM specifically (with the prompt co-translated) and showing
16 px FFT periodicity in boundary-F. That is an application of arXiv:2606.08132's protocol to one more model.

**Remaining novelty:** NONE-to-SLIVER.
**Novelty confidence:** 4.
**Reviewer #2 likely citation:** arXiv:2606.08132.
**Verdict:** **KILL.**

---

## Cluster 8 — Topology / holes prior (A1-004)

Claim under attack: SAM has a decoder prior against genus>0 masks (donuts filled in); topology-level failure characterization
absent from the SAM literature.

**Closest prior works**
- Topology-aware segmentation is a mature subfield: Hu et al., *Topology-Preserving Deep Image Segmentation*, NeurIPS 2019; Shit et al., *clDice*, CVPR 2021; *Topology Optimization in Medical Image Segmentation with Fast Euler Characteristic*, arXiv:2507.23763; *Topology-Guaranteed Image Segmentation (connectivity, genus, width)*, arXiv:2601.11409.
- *COCO-ReM / Benchmarking Object Detectors with COCO: A New Path Forward.* Singh et al. ECCV 2024. arXiv:2403.18819 — added ~2,000 val masks with **true holes** where COCO-2017 had **zero**, i.e., the "no holes" behavior is substantially an annotation-format convention.
- SAM engineering: the released automatic mask generator post-processes masks by **filling holes** below an area threshold (facebookresearch/segment-anything, `min_mask_region_area`).

**What they actually did.** The topology community has metrics (Betti error, Euler characteristic maps, clDice) and training
fixes; genus constraints are an explicit, published axis. COCO-ReM showed benchmark GT itself lacked holes, so *no* model
trained/evaluated on COCO-style masks is rewarded for genus>0 output. SAM's own pipeline actively deletes small holes.
A SAM-specific genus audit ("hole recovery rate on rings/cups vs U-Net"): **NOT FOUND** — but two of its likely causes
(annotation convention, postprocessing) are already documented, which makes the naive audit confounded on arrival.

**Exact remaining difference.** Disentangling *decoder prior* from *label convention* from *postprocessing*: does raw SAM
(no hole-filling, logits inspected) represent genus>0 at all?

**Remaining novelty:** SLIVER.
**Novelty confidence:** 3.
**Reviewer #2 likely citation:** clDice / Hu et al. ("topology metrics exist") + COCO-ReM ("your GT had no holes").
**Verdict:** **MUTATE** — only viable as the three-way causal decomposition (prior vs convention vs postprocessing), evaluated
on COCO-ReM's genuinely-holed masks with raw logits; as a "SAM fails on donuts" audit it is dead.

---

## Cluster 9 — Prompt-distribution shift (A1-091, A1-118)

Claim under attack: click conventions differ across datasets; evaluating under another dataset's prompt distribution shifts
IoU as much as image-domain shift — "prompt-distribution shift" as a new measurable axis.

**Closest prior works**
- *RClicks* (arXiv:2410.11722) — clickability distributions, user-group stratification, robustness metric ΔGR (3–79% spread across clicking styles).
- *BREPS* (arXiv:2601.15123) — box-style distributions differ by platform (desktop vs mobile), and models re-rank under them.
- *PointPrompt* (arXiv:2410.22048) — human prompting distributions across 16 datasets, features predictive of performance.

**What they actually did.** RClicks/BREPS established that prompt distributions (a) vary by population and platform,
(b) materially move metrics, and (c) change method rankings — which *is* the "prompt-distribution shift is real and
measurable" thesis, with data. A1-118 (marginalized IoU) is their headline metric. The literal cross-dataset
distribution-swap matrix (train clickability on dataset A, evaluate on B) is a re-analysis of their released data.

**Exact remaining difference.** Naming the axis and the swap-matrix experiment; no new data or capability.

**Remaining novelty:** NONE-to-SLIVER.
**Novelty confidence:** 4.
**Reviewer #2 likely citation:** RClicks + BREPS.
**Verdict:** **KILL.**

---

## Cluster 10 — SA-1B leakage (C1-001)

Claim under attack: near-duplicate overlap between SA-1B and the zero-shot evaluation benchmarks inflates SAM's zero-shot
numbers; overlap never audited.

**Closest prior works**
- SA-1B-specific dedup audit vs SA-23 / COCO / LVIS / DAVIS: **NOT FOUND.**
- Genre prior: *On the De-duplication of LAION-2B.* Webster et al. 2023. arXiv:2303.12733 (web-scale image dedup / verbatim-copy analysis).
- *Soft Contamination Means Benchmarks Test Shallow Generalization.* 2026. arXiv:2602.12413 (semantic-duplicate contamination inflates benchmark gains; LLM-side but the framing transfers).
- *Revising RVL-CDIP.* arXiv:2606.31446 (35% test–train near-dup overlap discovered post hoc in a standard vision benchmark).
- Provenance fact: Kirillov et al. state SA-1B images were **licensed from a photo provider**, not scraped from Flickr/web — which lowers, but does not eliminate, prior odds of overlap with Flickr-derived benchmarks.

**What they actually did.** The tooling (SSCD/pHash), the contamination playbook, and precedents of embarrassing post-hoc
overlap discoveries all exist; nobody has pointed them at SA-1B↔segmentation-benchmark pairs.

**Exact remaining difference.** The audit itself. It is genuinely unrun, cheap, and eval-only. The honest risk: SA-1B's
licensed provenance makes a null result the modal outcome, and a null here is a tweet, not a paper.

**Remaining novelty:** REAL (as an unrun audit), conditional value.
**Novelty confidence:** 3.
**Reviewer #2 likely citation:** Webster et al. (arXiv:2303.12733) — "dedup methodology is standard."
**Verdict:** **SURVIVE** (as a gating audit, not a flagship).
**Killer experiment:** SSCD + pHash near-duplicate retrieval between SA-1B (released split) and the 23-dataset SA-23 suite
plus COCO/LVIS/DAVIS vals; pre-register: if overlap ≥0.5% on any suite, report score deltas on overlapped-vs-clean subsets;
if below, publish one paragraph in a broader eval-hygiene paper and stop.

---

## Cluster 11 — Annotator noise floor (C1-016)

Claim under attack: SOTA method gaps on major segmentation benchmarks sit inside the inter-annotator noise floor, and the
floor is "unpublished for major seg sets."

**Closest prior works**
- *Label Convergence: Defining an Upper Performance Bound in Object Recognition through Contradictory Annotations.* Tschirschwitz & Rodehorst. 2024. arXiv:2409.09412. https://arxiv.org/abs/2409.09412
- *Benchmarking Object Detectors with COCO: A New Path Forward (COCO-ReM).* Singh et al. ECCV 2024. arXiv:2403.18819. https://arxiv.org/abs/2403.18819
- *LVIS.* Gupta, Dollár, Girshick. CVPR 2019 (dual-annotation consistency measurement built into the benchmark).
- *Segment Anything* §Dataset (human audit: SA-1B mask quality compared against published COCO/LVIS/OpenImages inter-annotator IoU of ~0.85–0.91).

**What they actually did.** The Label Convergence paper is C1-016 executed: it estimates the annotation-consistency-implied
upper bound (LVIS convergence interval 62.6–67.5 mAP) and observes Co-DETR at 66.8 — i.e., "SOTA is at the noise floor,"
published with the same repeated-labeling methodology C1-016 proposes. COCO-ReM showed COCO's mask noise is large enough to
re-rank 50 detectors. LVIS published annotator-agreement statistics in 2019; the SAM paper's audit *cites* those numbers.
The premise "noise floor unpublished for major seg sets" is factually false.

**Exact remaining difference.** Promptable/interactive metrics (NoC) rather than mAP — a footnote, since RClicks already
handles the human-variance side of interactive metrics.

**Remaining novelty:** NONE.
**Novelty confidence:** 5.
**Reviewer #2 likely citation:** arXiv:2409.09412.
**Verdict:** **KILL.**

---

## Cluster 12 — Scale floor ~16 px (A1-073)

Claim under attack: below ~16 px objects, SAM masks are noise indistinguishable from a box-fill baseline; establish the floor
and rank remedies (tiling, upsampling) before anyone fine-tunes.

**Closest prior works**
- *Computer-Vision Benchmark Segment-Anything Model (SAM) in Medical Images.* He et al. 2023. arXiv:2304.09324 — GLM across 12 datasets: relative target size is the single most significant predictor of SAM Dice.
- *Segment anything model for medical image analysis.* Mazurowski et al. MedIA 2023 — object-size vs performance analysis.
- *Segment Anything Model for Medical Images?* Huang et al. MedIA 2024. arXiv:2304.14660 — size/contrast-stratified failures.
- *Slicing Aided Hyper Inference (SAHI).* Akyon et al. ICIP 2022. arXiv:2202.06934 — tiling as the standard small-object remedy, with size-stratified reporting conventions (COCO AP-small).

**What they actually did.** Size-dependence of SAM quality is among the most-replicated findings in the SAM-eval literature;
the remedy ranking (tiling preserves resolution; upsampling doesn't add information) is the established SAHI story plus
COCO's small/medium/large stratification convention. What is genuinely absent is the *null calibration*: nobody reports the
size threshold below which SAM's Dice is statistically indistinguishable from filling the prompt box.

**Exact remaining difference.** The box-fill-equivalence threshold as a hard floor number. One figure.

**Remaining novelty:** SLIVER.
**Novelty confidence:** 4.
**Reviewer #2 likely citation:** He et al. arXiv:2304.09324 + SAHI.
**Verdict:** **KILL** as a standalone; the box-fill-null figure should be a mandatory reporting arm inside whichever small-object
or medical eval survives elsewhere in the pool.

---

## Cluster 13 — Embedding-scale granularity knob (A1-101)

Claim under attack: multiplying sparse prompt-token embeddings by a scalar monotonically steers frozen-SAM output between
part and whole — a latent, training-free granularity control.

**Closest prior works**
- *GraCo: Granularity-Controllable Interactive Segmentation.* Zhao et al. CVPR 2024 Highlight. arXiv:2405.00587 — continuous granularity slider, achieved via LoRA fine-tuning on auto-generated mask-granularity pairs.
- *Semantic-SAM.* Li et al. 2023. arXiv:2307.04767 — trained multi-granularity segmentation.
- *Segment Anything.* Kirillov et al. — 3-level discrete granularity via multimask heads (the trivial baseline).
- Training-free latent-knob discovery in frozen SAM prompt embeddings: **NOT FOUND.**

**What they actually did.** GraCo delivers the *capability* (user-controllable granularity) with training; Semantic-SAM trains
for it natively; SAM itself exposes three discrete levels. Nobody reports that a scalar on prompt-embedding norms modulates
granularity in the frozen model — if true and monotonic, it is a real mechanism finding about how the decoder encodes scale,
not just a cheaper GraCo.

**Exact remaining difference.** Zero-training vs LoRA-training, plus the interpretability claim (granularity is linearly
encoded in prompt-token magnitude). Capability-wise GraCo wins; mechanism-wise the question is open.

**Remaining novelty:** REAL (mechanism), SLIVER (capability).
**Novelty confidence:** 3.
**Reviewer #2 likely citation:** GraCo ("granularity control exists; what does training-free add?").
**Verdict:** **SURVIVE** — but framed as mechanism discovery, not as a GraCo competitor.
**Killer experiment:** sweep the scalar α ∈ [0.25, 4] on point-prompt embeddings for 1k SA-1B images with nested GT
(plus PartImageNet); pre-register monotonicity (Spearman of α vs mask area, and vs part/whole agreement) and the two kill
conditions: (a) non-monotonic/erratic response, or (b) fails to beat the trivial baseline of selecting among SAM's own
three multimask outputs. Two GPU-days; dead or alive in a week.

---

## Cluster 14 — Channel-lift grayscale (A1-033)

Claim under attack: a tiny learned 1→3-channel lifting (1×1 conv) beats channel replication for grayscale medical modalities
and approaches LoRA at ~0.1% of parameters; the pseudo-RGB interface is an ignored adaptation surface.

**Closest prior works**
- *SAM-aware Test-time Adaptation for Universal Medical Image Segmentation (SAM-TTA).* 2025. arXiv:2506.05221 — a learned Self-adaptive Bézier-Curve Transformation (12 parameters) converting grayscale→3 diverse channels for SAM, explicitly motivated by and shown superior to channel replication.
- *COVID-19 Classification ... with Three-Channel Grayscale CT Images.* MDPI Big Data Cogn. Comput. 7(1):36, 2023 — HE/CLAHE-based 3-channel composition beating replication for pretrained models.
- *RepViT-CXR.* 2025. arXiv:2509.08234 — channel-replication strategies for ViTs on chest X-ray, with the replication-is-suboptimal discussion.
- Clinical practice prior: multi-window CT composited into RGB channels is a standard radiology preprocessing trick.

**What they actually did.** SAM-TTA is the same thesis on the same model class: the pseudo-RGB interface is an adaptation
surface; a few learned parameters mapping 1→3 channels beat replication for SAM on medical images. The MDPI paper made the
non-learned version of the argument in 2023. A1-033's exact instrument (1×1 conv) and exact comparison (vs LoRA at matched
parameter budget) are ablation-level deltas inside SAM-TTA's frame.

**Exact remaining difference.** Parameterization (linear conv vs Bézier intensity curves) and the LoRA-comparison table.

**Remaining novelty:** SLIVER.
**Novelty confidence:** 4.
**Reviewer #2 likely citation:** SAM-TTA (arXiv:2506.05221).
**Verdict:** **KILL.**

---

## Cluster 15 — Detector-box jitter budget (A1-071)

Claim under attack: SAM mask IoU is flat until box jitter exceeds ~20% of object size, then collapses — defining the weakest
usable detector for detector→SAM pipelines.

**Closest prior works**
- *Robust Box Prompt based SAM (RoBox-SAM).* Huang et al. MICCAI MLMI 2024. arXiv:2407.21284 — systematic 0–30% random box-shift sweeps (99,299 images, 5 modalities), degradation curves, and a fix.
- *Segment Anything Model for Medical Images?* Huang et al. MedIA 2024. arXiv:2304.14660 — box-jitter sensitivity established.
- *SAM on Medical Images: A Comprehensive Study on Three Prompt Modes.* Cheng et al. 2023. arXiv:2305.00035 — jitter-scale sweeps; "prediction accuracy decreases with jitter scale."
- *BREPS.* arXiv:2601.15123 — worst-case-realistic box search; ~30% IoU drops; per-pixel box-placement IoU heatmaps; 15 models.
- *FNPC.* 2023. arXiv:2308.10382 — box position/size sensitivity on ultrasound + multi-box augmentation remedy.

**What they actually did.** The jitter–IoU curve has been published at least four independent times, including exactly the
"how much box error can SAM absorb" framing (RoBox-SAM: stable under 10%, collapses toward 30%; BREPS: catastrophic
worst-case within realistic bounds). The "budget" number and its class-dependence are read directly off these curves.
Matching the budget to a *specific detector's* error distribution (the S-126 fire pipeline variant) is systems engineering.

**Exact remaining difference.** None of substance.

**Remaining novelty:** NONE.
**Novelty confidence:** 5.
**Reviewer #2 likely citation:** RoBox-SAM + BREPS.
**Verdict:** **KILL.**

---

## Summary table

| # | Cluster (lead IDs) | Killer prior | Novelty left | Conf | Verdict |
|---|---|---|---|---|---|
| 1 | Oracle-prompt protocol (S-003, A1-118, C1-115) | RClicks; BREPS; Mazurowski MedIA'23 | NONE/SLIVER | 5 | KILL |
| 2 | Tight-box image ablation (S-014, S-604) | Stable-SAM (adjacent only) | REAL | 4 | **SURVIVE** |
| 3 | Nested multimask (S-018, C1-061, A1-003) | SAM paper design; GraCo | NONE / SLIVER→REAL | 5/3 | MUTATE → "ambiguity forgetting" |
| 4 | Negative-click paradox (S-005, A1-007) | RITM; FocSAM; DiffClick | SLIVER | 4 | KILL |
| 5 | Prompt-evolution scorer failure (S-007, S-347) | SAMPOT's own failure analysis | SLIVER | 3 | MUTATE → scorer-validity audit |
| 6 | Human vs simulated clicks (A1-105, C1-003) | RClicks; PointPrompt | NONE | 5 | KILL |
| 7 | Patch-grid aliasing (A1-002) | arXiv:2606.08132; Alias-Free ViT | NONE/SLIVER | 4 | KILL |
| 8 | Topology/holes prior (A1-004) | topology-seg field; COCO-ReM holes | SLIVER | 3 | MUTATE → prior-vs-convention-vs-postproc decomposition |
| 9 | Prompt-distribution shift (A1-091, A1-118) | RClicks; BREPS | NONE/SLIVER | 4 | KILL |
| 10 | SA-1B leakage (C1-001) | NOT FOUND (genre: LAION dedup) | REAL, conditional | 3 | **SURVIVE** (gating audit) |
| 11 | Annotator noise floor (C1-016) | Label Convergence arXiv:2409.09412; COCO-ReM; LVIS | NONE | 5 | KILL |
| 12 | Scale floor ~16 px (A1-073) | He et al. 2304.09324; SAHI | SLIVER | 4 | KILL (keep box-fill null as reporting arm) |
| 13 | Embedding-scale granularity (A1-101) | GraCo (capability only) | REAL (mechanism) | 3 | **SURVIVE** |
| 14 | Channel-lift grayscale (A1-033) | SAM-TTA arXiv:2506.05221 | SLIVER | 4 | KILL |
| 15 | Box-jitter budget (A1-071) | RoBox-SAM; BREPS; 2305.00035 | NONE | 5 | KILL |

## Consequences for the Stage-3 pool

- The entire "realistic-prompt evaluation" wing of Windows4 (clusters 1, 6, 9, 15 here; touches C1-038, S-016, S-019,
  A1-048, A1-094 in the wider pool) is owned by the RClicks/BREPS group. Recommend a pool-wide sweep: any hypothesis whose
  minimal experiment is "perturb or re-distribute prompts and re-measure IoU" should be re-audited against those two papers
  before Stage 4.
- Survivors to carry forward: **S-014/S-604** (image-evidence ablation inside tight boxes — the one genuinely unrun causal
  probe in this batch), **A1-101** (training-free granularity knob, as mechanism), **C1-001** (SA-1B dedup, as a cheap
  gating audit with pre-registered stop rule). Mutations to re-enter the pool: **C1-061** (ambiguity forgetting),
  **S-007-as-scorer-validity-audit**, **A1-004-as-three-way-decomposition**.
- Convergence warning from Stage 2 is vindicated: three of the four highest-confidence kills (clusters 6, 9, 11) were
  ideas that appeared in ≥3 seed batches. Cross-batch convergence predicted *priority*, and indeed the field had already
  published them.
