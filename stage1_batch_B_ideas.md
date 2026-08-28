# Stage 1 — Batch B: Original Research Ideas (IDEA-B-0001 to IDEA-B-0340)

**PI:** Windows5
**Stage:** 1 (Autonomous Research Idea Evolution — idea generation only)
**Batch:** B
**Count:** 340 ideas
**Scope priority:** Vision Foundation Models, VLMs, PEFT, SAM, segmentation (medical, smoke/fire, transparent objects), detection. Secondary: domain adaptation, few/zero-shot, prompt learning, synthetic data, representation learning.
**Constraints honored:** no module stacking, no "apply X to medical" retreads, no loss/backbone swaps; no invented results or fabricated citations. Every idea is stated as a falsifiable hypothesis with a minimal experiment.

---

## Cluster 1 — Dataset Failure / Annotation Efficiency / Long-Tail (IDEA-B-0001 … IDEA-B-0040)

### IDEA-B-0001 — Structured (non-i.i.d.) noise in SAM pseudo-labels breaks noise-robust learning theory
**One-sentence idea:** Characterize SAM-generated pseudo-label noise as spatially structured (boundary-biased, systematically dilated/eroded per texture class) and test whether noise-robust losses designed for i.i.d. label noise fail on it.
**Problem:** SAM is widely used as an auto-labeler, but downstream training methods assume label noise is random, while SAM's errors are systematic and correlated with image content.
**Core Hypothesis:** Noise-robust training methods that provably help under symmetric/asymmetric i.i.d. pixel noise give near-zero or negative gains when the noise source is SAM pseudo-labels, because the noise is low-entropy and learnable as a bias.
**Why Important:** Auto-labeling with foundation models is becoming the default way to build segmentation datasets; if the noise model is wrong, the whole pipeline silently trains in a bias.
**Why Possibly Novel:** Label-noise literature is dominated by classification with synthetic i.i.d. noise; a measured noise model of a real foundation-model labeler for dense prediction is largely missing.
**Minimal Experiment:** On 2–3 datasets with expert masks, generate SAM pseudo-labels, fit a spatial noise model (offset/dilation statistics per stratum), train identical students with (a) clean, (b) SAM, (c) synthetic i.i.d. noise matched in rate; compare noise-robust losses across (b) vs (c).
**Main Risk:** The structured-vs-i.i.d. gap may be small at high pseudo-label quality, making the finding true but low-impact.

### IDEA-B-0002 — The precision-vs-count annotation frontier for foundation-model fine-tuning
**One-sentence idea:** Map the iso-budget tradeoff between "many coarse masks" and "few precise masks" when fine-tuning SAM-like models on medical data.
**Problem:** Annotation budgets are fixed, but nobody knows whether an hour is better spent on 40 rough masks or 8 pixel-perfect ones for adapting a foundation model.
**Core Hypothesis:** Above a modest count threshold, boundary precision dominates mask count for fine-tuning gains, because the pretrained model already has objectness and mainly needs boundary-convention calibration.
**Why Important:** Directly prescribes how clinical annotation campaigns should spend money; could cut annotation cost several-fold.
**Why Possibly Novel:** Active learning studies "which images"; almost none study "how precisely to annotate each" as a controlled budget variable for foundation-model adaptation.
**Minimal Experiment:** Take one dataset with high-quality GT; synthesize coarse variants (vertex decimation, boundary jitter at controlled magnitudes); fine-tune identical LoRA configurations across an iso-cost grid (count × precision, using measured annotation-time models); plot the frontier.
**Main Risk:** The frontier may be strongly dataset-dependent, limiting general prescriptions.

### IDEA-B-0003 — Scale long-tail, not class long-tail, as the primary axis of SAM failure
**One-sentence idea:** Test whether object-scale rarity predicts SAM's per-instance failures better than class-frequency rarity, and whether scale-stratified resampling beats class-stratified resampling.
**Problem:** Long-tail methods reweight by class frequency, but prompted segmenters are class-agnostic and may instead fail on rare object scales, aspect ratios, and boundary complexities.
**Core Hypothesis:** A regression from geometric strata (log-scale, thinness, boundary fractal dimension) explains more variance in per-instance SAM IoU than class frequency does, and reweighting by geometric strata yields larger fine-tuning gains.
**Why Important:** Redefines the "long tail" for the prompted-segmentation era and changes what dataset curators should balance.
**Why Possibly Novel:** Long-tail literature is class-centric; a geometry-centric long-tail formulation for class-agnostic foundation models is unexplored.
**Minimal Experiment:** On LVIS-like and medical data, compute per-instance SAM IoU, fit both predictors, compare R²; then fine-tune with class-balanced vs geometry-balanced sampling at equal budget.
**Main Risk:** Class and geometry are correlated; disentangling may require careful stratification and larger n than expected.

### IDEA-B-0004 — Inter-annotator prompt variance as the dominant error source for thin structures
**One-sentence idea:** Quantify how much of interactive-SAM output variance on thin structures (vessels, wires, catheters) comes from human click placement variance versus model stochasticity.
**Problem:** Interactive segmentation evaluations use canonical prompts, hiding the fact that real users click in different places, and thin structures may amplify click variance into large mask variance.
**Core Hypothesis:** For structures thinner than ~2× the encoder patch size, inter-annotator prompt variance accounts for the majority of output IoU variance, exceeding model-side variance by a large factor.
**Why Important:** If prompts dominate, research effort should shift from decoders to prompt-normalization interfaces, and evaluations must report prompt-variance error bars.
**Why Possibly Novel:** Human prompt variability has been discussed anecdotally, but a variance decomposition (human vs model) across structure geometry is missing.
**Minimal Experiment:** Collect clicks from 5–10 annotators on the same 100 thin-structure targets; decompose output variance (ANOVA over annotator × structure); compare against MC variance from the model with fixed prompts.
**Main Risk:** Recruiting enough annotators for statistical power; effect may be obvious for extreme geometries but small elsewhere.

### IDEA-B-0005 — Prompt-perturbation disagreement as an annotation-value signal
**One-sentence idea:** Use disagreement across an ensemble of perturbed prompts (jittered clicks, grown/shrunk boxes) as an acquisition function for active annotation, replacing softmax-entropy heuristics.
**Problem:** Classic active-learning acquisition (entropy, margin) was designed for classifiers and correlates poorly with where prompted segmenters actually fail.
**Core Hypothesis:** Instability of the mask under small prompt perturbations predicts expert-correction cost better than pixel entropy, and selecting by prompt-instability yields steeper annotation-budget curves.
**Why Important:** Annotation efficiency is the practical bottleneck for medical and industrial segmentation; a free, model-native acquisition signal would be widely usable.
**Why Possibly Novel:** Prompt-space perturbation as an epistemic probe is unique to promptable models and has not been formalized as an acquisition function.
**Minimal Experiment:** On two datasets, run active-learning simulations comparing random, entropy, MC-dropout, and prompt-instability acquisition at equal budgets; measure IoU-vs-budget curves.
**Main Risk:** Prompt instability may correlate with irreducible ambiguity (aleatoric), wasting budget on images no annotation can fix.

### IDEA-B-0006 — Label-convention averaging: systematic boundary bias from multi-dataset fine-tuning
**One-sentence idea:** Show that fine-tuning one model on multiple datasets with different annotation conventions (e.g., "organ+capsule" vs "organ only") produces a predictable averaged boundary bias rather than dataset-conditional behavior.
**Problem:** Merged medical datasets silently disagree about where boundaries are by convention, and models trained on the union may learn a compromise that matches no convention.
**Core Hypothesis:** A model fine-tuned on merged conventions exhibits a systematic boundary offset approximating a weighted average of source conventions, measurable as bias (not variance), and a one-token convention indicator removes most of it.
**Why Important:** Data pooling is the standard scaling recipe; convention averaging would mean pooled models are systematically wrong everywhere while appearing good on average.
**Why Possibly Novel:** Domain shift is studied for appearance; label-convention shift as a first-class, measurable bias term is rarely isolated.
**Minimal Experiment:** Construct controlled convention pairs by re-annotating 100 images under two written protocols; train on the union with/without convention conditioning; measure signed boundary offset distributions per test convention.
**Main Risk:** Real conventions may differ non-uniformly along the boundary, making "offset" too coarse a summary.

### IDEA-B-0007 — Positive-unlabeled correction for SAM-based auto-labeling with incomplete GT
**One-sentence idea:** Treat instances missing from sparsely annotated detection/segmentation datasets as unlabeled-not-negative when using them to fine-tune or evaluate SAM auto-labelers.
**Problem:** Many datasets annotate only some instances per image; standard training treats unannotated true objects as background, teaching auto-labelers to suppress valid detections.
**Core Hypothesis:** Fine-tuning with a positive-unlabeled objective (estimating the class prior of missed instances) recovers a measurable fraction of suppressed recall relative to naive training, with the gain proportional to the measured annotation-missingness rate.
**Why Important:** Sparse annotation is the norm at scale; the fix is statistical rather than architectural and applies to every auto-labeling pipeline.
**Why Possibly Novel:** PU learning is established for classification; a calibrated PU treatment of dense auto-labeling against measured missingness rates is not.
**Minimal Experiment:** Take a fully annotated dataset, synthetically delete 20–60% of instance labels, train naive vs PU-corrected fine-tunes, and measure recall recovery as a function of deletion rate; validate on a real sparsely-labeled dataset.
**Main Risk:** Estimating the missingness prior on real data is hard; miscalibrated priors could over-inflate false positives.

### IDEA-B-0008 — Soft consensus beats hard majority vote for amorphous-class ground truth
**One-sentence idea:** For boundary-ambiguous classes like smoke, test whether training on averaged soft masks from multiple annotators outperforms training on majority-vote hard masks, even when evaluation is hard-thresholded.
**Problem:** Smoke, haze, and infiltrative lesions have no objectively correct boundary, yet datasets force a single hard mask, discarding the disagreement structure.
**Core Hypothesis:** Soft-consensus supervision yields higher hard-mask IoU at the consensus threshold and better-calibrated confidence, because the disagreement encodes true boundary uncertainty the model can exploit.
**Why Important:** Determines how the next generation of amorphous-class datasets (fire, smoke, ground-glass opacity) should be collected and released.
**Why Possibly Novel:** Multi-rater fusion exists in medical imaging, but a controlled soft-vs-hard supervision comparison specifically for amorphous "stuff" with foundation-model fine-tuning is missing.
**Minimal Experiment:** Collect 5-rater masks on ~300 smoke images (or reuse an existing multi-rater medical set as proxy); train identical models on soft vs hard targets; evaluate on held-out consensus and per-rater masks.
**Main Risk:** Gains may vanish if the downstream metric itself is defined against a single arbitrary rater.

### IDEA-B-0009 — A geometric-stratum census of SA-1B that predicts fine-tuning gains
**One-sentence idea:** Audit web-scale segmentation pretraining data (SA-1B) for the frequency of hard strata—transparent, wiry, camouflaged, low-contrast, tiny—and test whether stratum frequency predicts where fine-tuning helps most.
**Problem:** We know SAM fails on transparent and thin objects, but we lack a quantitative account tying failures to pretraining-data frequency versus architectural limits.
**Core Hypothesis:** Per-stratum zero-shot IoU and per-stratum fine-tuning gain are both log-linear in the stratum's estimated pretraining frequency; strata that deviate from this line indicate architectural (not data) limits.
**Why Important:** Separates "needs more data" failures from "needs new architecture" failures—the most consequential distinction for planning foundation-model research.
**Why Possibly Novel:** Data-frequency-vs-capability analyses exist for LLMs; the dense-prediction analogue with geometric strata has not been done.
**Minimal Experiment:** Estimate stratum frequencies on a 100k-image SA-1B sample with automated detectors + manual verification; evaluate zero-shot and post-fine-tuning IoU per stratum on curated probe sets; fit and inspect the frequency-capability curve.
**Main Risk:** Automated stratum detectors are themselves imperfect on exactly the hard strata being measured, biasing frequency estimates.

### IDEA-B-0010 — Asymmetric transfer between prompt-type supervisions
**One-sentence idea:** Measure whether fine-tuning a promptable segmenter with only box prompts transfers to point-prompt usage (and vice versa), mapping the prompt-type transfer matrix.
**Problem:** Fine-tuning datasets typically supervise one prompt type, but deployed users prompt differently; if transfer is asymmetric, the training prompt protocol is a hidden design decision.
**Core Hypothesis:** Box-supervised fine-tuning transfers to points substantially better than point-supervised transfers to boxes, because boxes constrain extent while points leave extent to (possibly overwritten) priors.
**Why Important:** Every SAM-adaptation paper picks a prompt protocol arbitrarily; an asymmetry result would set a default and explain cross-paper inconsistencies.
**Why Possibly Novel:** Prompt-type transfer has not been treated as a transfer-learning problem with its own asymmetry structure.
**Minimal Experiment:** Fine-tune identical adapters on one dataset under {point-only, box-only, mixed} supervision; evaluate all three prompt types; repeat on a second domain to check stability of the asymmetry.
**Main Risk:** The result may depend heavily on decoder architecture specifics, limiting generality beyond SAM-family models.

### IDEA-B-0011 — Instance-density long tail and the failure of "everything mode"
**One-sentence idea:** Characterize how automatic whole-image segmentation degrades as instance density grows (cell clusters, crowds, debris fields) and identify the density regime where per-instance prompting becomes information-theoretically necessary.
**Problem:** Everything-mode grid prompting has a fixed proposal budget; densely packed scenes exceed it, but the failure onset is uncharacterized.
**Core Hypothesis:** Everything-mode recall collapses super-linearly beyond a density threshold set by the prompt-grid spacing relative to median instance size, and the threshold is predictable from those two numbers alone.
**Why Important:** Microscopy, remote sensing, and agriculture routinely exceed natural-image densities; a predictive law tells practitioners when SAM-style pipelines cannot work unmodified.
**Why Possibly Novel:** Density-stratified evaluation of prompted segmentation with a predictive threshold model is not in the literature.
**Minimal Experiment:** Build density-controlled test sets (synthetic composites + real microscopy); sweep grid resolutions; fit recall-vs-density curves and validate threshold predictions on held-out datasets.
**Main Risk:** Confounding between density and instance size/contrast in real data may blur the threshold.

### IDEA-B-0012 — Near-duplicate inflation of annotation-efficiency claims
**One-sentence idea:** Measure how near-duplicate images (adjacent video frames, same-patient slices) in medical segmentation datasets inflate few-shot and annotation-efficiency results, and propose deduplication-aware splits.
**Problem:** Many "N-shot" medical results sample training and test images from correlated pools, so reported efficiency reflects memorization of duplicates rather than generalization.
**Core Hypothesis:** After enforcing patient-level and near-duplicate-level splits, published-style few-shot gains shrink substantially, and the shrinkage is predictable from a dataset's duplicate-cluster size distribution.
**Why Important:** Annotation-efficiency numbers drive clinical adoption decisions; inflated numbers misallocate real budgets.
**Why Possibly Novel:** Deduplication is studied for classification pretraining corpora, not for dense-prediction few-shot evaluation protocols.
**Minimal Experiment:** Run perceptual-hash + embedding-based duplicate clustering on 5 public medical datasets; re-evaluate a standard SAM fine-tuning recipe under naive vs dedup-aware splits; report the gap (own measurements only).
**Main Risk:** Some datasets lack patient metadata, making duplicate clustering only approximate.

### IDEA-B-0013 — The annotation-noise ceiling: significance testing against rater disagreement
**One-sentence idea:** Develop and apply a protocol that reports segmentation improvements relative to the inter-rater noise floor of the test set, flagging gains that are statistically indistinguishable from annotation noise.
**Problem:** Test labels have finite precision, yet leaderboard gaps of <1 IoU point are routinely interpreted as progress without reference to that precision.
**Core Hypothesis:** On several widely used benchmarks, the inter-rater noise floor (estimated from multi-rater subsets or re-annotation) exceeds typical inter-method gaps, so many rankings are unstable under plausible relabelings.
**Why Important:** Rebases the field's notion of progress and prevents overfitting research effort to noise.
**Why Possibly Novel:** Noise floors are acknowledged qualitatively; a reusable statistical procedure (relabeling bootstrap for dense metrics) applied across benchmarks is new.
**Minimal Experiment:** Re-annotate stratified samples (100–200 images) of 2 benchmarks with 3 raters; build a label-noise generative model; bootstrap method rankings of public checkpoints under resampled labels.
**Main Risk:** Re-annotation cost; findings could be benchmark-specific.

### IDEA-B-0014 — Report-only spatial supervision: how far can prompts be placed without any masks?
**One-sentence idea:** Quantify how accurately structured radiology-report parsing (laterality, lobe, "apical", sizes) can place prompts for a frozen promptable segmenter, measured as end-mask quality with zero pixel labels.
**Problem:** Millions of images have reports but no masks; the limiting factor for exploiting them is unknown—report parsing, spatial grounding, or the segmenter itself.
**Core Hypothesis:** For anatomically localized findings, report-derived spatial constraints suffice to place prompts within the segmenter's basin of attraction for a majority of cases, and failure is dominated by grounding (not parsing or segmentation).
**Why Important:** Establishes a mask-free adaptation route and an error budget telling researchers which component to improve.
**Why Possibly Novel:** Report-to-prompt pipelines exist as demos; a factorized error-budget analysis (parse vs ground vs segment) does not.
**Minimal Experiment:** On a dataset with paired reports and masks, cascade (LLM parse → anatomical atlas grounding → prompt → SAM); ablate each stage with oracles; attribute end-to-end error.
**Main Risk:** Requires a dataset with reports, masks, and consistent anatomy—few public options.

### IDEA-B-0015 — Polygon-vertex budgets as a hidden bias against thin and fractal structures
**One-sentence idea:** Measure how the vertex-count economics of polygon annotation tools systematically under-represent high-curvature boundary detail, and how models inherit this as a smoothness prior.
**Problem:** Popular datasets were annotated with polygons under time pressure; boundary detail beyond a few dozen vertices is missing by construction, but models are evaluated as if GT were exact.
**Core Hypothesis:** Model boundary smoothness statistics match the vertex-budget statistics of their training datasets (not the true object statistics), and training on re-annotated dense boundaries measurably sharpens predictions on independent high-precision GT.
**Why Important:** Explains a pervasive, invisible ceiling on boundary quality and motivates changes in annotation tooling.
**Why Possibly Novel:** Annotation-tool-induced priors have not been quantified as a transferable property of trained models.
**Minimal Experiment:** Compare boundary curvature spectra of dataset GT vs high-precision re-annotations vs model outputs; fine-tune on dense-boundary subsets and test curvature recovery.
**Main Risk:** High-precision re-annotation is expensive; curvature spectra may be dominated by image resolution limits.

### IDEA-B-0016 — Annotator-identity leakage in crowd-labeled fire/smoke datasets
**One-sentence idea:** Test whether segmentation models trained on crowd-labeled smoke/fire data learn annotator-specific boundary styles that are predictable from held-out annotations, constituting a leakage-based generalization risk.
**Problem:** Crowd workers differ systematically in how far into translucent smoke they extend masks; if worker identity is predictable from a trained model's outputs, the model has fit style rather than physics.
**Core Hypothesis:** A probe can classify which annotator labeled a training image from the model's predicted boundary offsets at above-chance rates, and style-normalizing labels before training improves cross-dataset transfer.
**Why Important:** Reveals a concrete mechanism by which weak annotation protocols cap cross-dataset generalization for amorphous classes.
**Why Possibly Novel:** Annotator-style modeling exists for NLP labels; boundary-style leakage in dense vision labels is unstudied.
**Minimal Experiment:** On a dataset with annotator IDs, fit per-annotator boundary-offset profiles; train with raw vs style-normalized masks; compare cross-dataset IoU and style-probe accuracy.
**Main Risk:** Public datasets rarely release annotator IDs; may need a purpose-built small collection.

### IDEA-B-0017 — The missing-negative problem in transparent-object benchmarks
**One-sentence idea:** Show that transparent-object segmentation benchmarks contain almost no target-absent images, leaving false-positive behavior unmeasured, and build a negative-inclusive evaluation that changes method rankings.
**Problem:** Benchmarks like glass/transparent-object suites evaluate only images containing glass, so models are never penalized for hallucinating transparency on glossy or reflective non-glass surfaces.
**Core Hypothesis:** Method rankings on positives are weakly correlated with false-positive rates on curated hard negatives (mirrors, water, gloss), and some top methods are among the worst on negatives.
**Why Important:** Deployed systems (robot grasping, autonomous navigation) are harmed more by hallucinated glass than by missed glass boundaries.
**Why Possibly Novel:** Target-absent evaluation is standard in detection but effectively absent from transparent-segmentation benchmarking.
**Minimal Experiment:** Curate ~500 hard-negative images; evaluate public checkpoints for FP area rate; correlate with benchmark ranks (report only measured numbers).
**Main Risk:** Defining "hard negative" without bias toward particular failure styles.

### IDEA-B-0018 — Visual nesting of rare classes inside frequent classes in long-tail data
**One-sentence idea:** Test whether long-tail segmentation failures concentrate on rare classes that are visually nested within frequent classes (subtypes, parts), and whether taxonomy-aware evaluation separates nesting errors from true misses.
**Problem:** Long-tail metrics count a rare-class miss the same whether the model predicted a plausible parent class or nothing; these are scientifically different failures with different fixes.
**Core Hypothesis:** The majority of rare-class errors in long-tail instance segmentation are parent-class substitutions rather than omissions, implying the bottleneck is granularity resolution, not detection.
**Why Important:** Redirects long-tail research from "find the rare thing" to "distinguish the rare thing," which needs different data and methods.
**Why Possibly Novel:** Error taxonomies exist for detection (TIDE-style) but not decomposed along class-taxonomy nesting for the long tail.
**Minimal Experiment:** On LVIS-style data with a class hierarchy, re-score public models with substitution-aware metrics; quantify the substitution fraction per rarity bin.
**Main Risk:** Hierarchies are incomplete; some substitutions are annotation errors rather than model errors.

### IDEA-B-0019 — Anchoring bias in correct-the-model annotation workflows
**One-sentence idea:** Measure whether human annotators who correct SAM proposals produce masks systematically biased toward SAM's errors (anchoring), compared to annotating from scratch, and quantify the downstream training cost of that bias.
**Problem:** Model-in-the-loop annotation is faster and now standard, but if humans under-correct systematic model errors, datasets inherit and amplify them across model generations.
**Core Hypothesis:** Corrected-from-proposal masks retain a measurable fraction of the proposal's signed boundary error relative to from-scratch masks by the same annotators, and models trained on corrected masks reproduce the ancestor model's error signature.
**Why Important:** Establishes whether the field's dominant annotation economy is quietly creating model-lineage bias in its ground truth.
**Why Possibly Novel:** Anchoring is documented in HCI for classification; its dense-prediction form and multi-generation propagation are unmeasured.
**Minimal Experiment:** Within-subject study: same annotators label 150 images from scratch and (weeks later, shuffled) via correction; compare error alignment with proposals; train students on each and test error-signature inheritance.
**Main Risk:** Within-subject memory effects; needs careful counterbalancing and washout.

### IDEA-B-0020 — One precise exemplar plus geometric augmentation versus many mediocre labels
**One-sentence idea:** Determine for which anatomical structures a single carefully labeled exemplar with structure-aware geometric augmentation matches dozens of ordinary labels when adapting a promptable segmenter.
**Problem:** Few-shot medical adaptation treats all shots as interchangeable; if one gold-standard exemplar plus deformation modeling suffices for stereotyped anatomy, budgets are misallocated.
**Core Hypothesis:** For anatomies with low shape variance (measured via a statistical shape model), one-exemplar training with plausible-deformation augmentation reaches within a small margin of 30-shot training, while high-variance structures show no such shortcut.
**Why Important:** Gives a decision rule—computable before annotation—for when one expert hour suffices.
**Why Possibly Novel:** Links shape-variance statistics to shot-count requirements quantitatively rather than anecdotally.
**Minimal Experiment:** Across 6 structures spanning shape-variance levels, compare 1-exemplar+augmentation vs k-shot curves; regress the gap against SSM variance.
**Main Risk:** Deformation models may leak test-set shape statistics if built from the same dataset.

### IDEA-B-0021 — Tail classes prefer frozen probes: capacity starvation in the long tail
**One-sentence idea:** Test whether tail classes are better served by frozen-foundation-feature probes while head classes benefit from deeper fine-tuning, implying per-class adaptation-depth allocation.
**Problem:** One global fine-tuning depth is chosen per model, but tail classes with few samples may be degraded by the same weight updates that help head classes.
**Core Hypothesis:** In joint training, per-class optimal adaptation depth correlates with class sample count; a two-branch readout (frozen probe for tail, adapted branch for head) beats any single uniform depth at equal parameters.
**Why Important:** Suggests the long-tail problem is partly an optimization-capacity allocation problem, orthogonal to reweighting.
**Why Possibly Novel:** Adaptation depth as a per-class resource has not been studied; long-tail work varies losses and sampling, not where classes read out from.
**Minimal Experiment:** On a long-tail segmentation dataset, train uniform-depth variants and the two-branch readout; report per-rarity-bin IoU at matched parameter counts.
**Main Risk:** The two-branch model could win via ensembling effects rather than the hypothesized mechanism; needs controls.

### IDEA-B-0022 — Effective sample size of video-derived segmentation datasets
**One-sentence idea:** Estimate the statistical effective sample size (ESS) of surgical/endoscopy video datasets given frame correlation, and show that reported data efficiency should be measured in ESS, not frames.
**Problem:** Video datasets report tens of thousands of "images" that are highly correlated frames; cross-dataset comparisons and scaling claims are distorted by this hidden redundancy.
**Core Hypothesis:** An ESS estimator based on feature-space autocorrelation predicts fine-tuning performance across datasets far better than raw frame count, unifying seemingly inconsistent scaling results.
**Why Important:** Makes dataset size claims comparable and prevents wasted annotation on redundant frames.
**Why Possibly Novel:** ESS is standard in statistics but has not been operationalized as a dataset descriptor for dense-prediction training.
**Minimal Experiment:** Compute ESS for 6 video-derived datasets; fine-tune at matched raw-frame vs matched-ESS budgets; test which predicts held-out IoU.
**Main Risk:** ESS may be task-dependent (boundary detail decorrelates faster than semantics), needing a per-task definition.

### IDEA-B-0023 — Directional label noise: dilated versus eroded ground truth have asymmetric effects
**One-sentence idea:** Establish whether systematically dilated GT and systematically eroded GT (same magnitude) cause asymmetric learned boundary biases and asymmetric downstream harm for prompted segmenters.
**Problem:** Label-noise robustness treats over- and under-segmentation as symmetric; anatomy and physics (partial-volume effects, annotator caution) make real noise directional.
**Core Hypothesis:** Erosion noise harms thin-structure recall disproportionately and is harder to unlearn than dilation noise at equal magnitude, because eroded labels delete supervision for exactly the pixels with least feature support.
**Why Important:** Tells annotation-protocol designers which direction of caution is cheaper and informs noise-correction methods.
**Why Possibly Novel:** Signed, structured boundary noise as an experimental variable (rather than random flip noise) is largely untested.
**Minimal Experiment:** Train matched models on GT dilated/eroded by 1–5 px; measure signed boundary error, thin-structure recall, and recovery speed when clean data is reintroduced.
**Main Risk:** Effects may be small at realistic noise magnitudes (1–2 px).

### IDEA-B-0024 — Nearest-neighbor mask transfer as a baseline that beats few-shot fine-tuning
**One-sentence idea:** Test whether, below ~10 labeled cases, retrieving the most similar labeled case and transferring its mask via dense correspondence outperforms fine-tuning a foundation segmenter.
**Problem:** Few-shot fine-tuning is the default even at n=3–5, where optimization is unstable; a retrieval-plus-correspondence baseline is rarely reported.
**Core Hypothesis:** For anatomies with consistent topology, correspondence-based mask transfer dominates fine-tuning below a crossover n, and the crossover is predictable from registration residuals.
**Why Important:** Establishes an honest baseline for the crowded few-shot-medical-SAM literature and a practical zero-training deployment path.
**Why Possibly Novel:** Atlas registration is classical, but its head-to-head against modern PEFT at controlled n, with a crossover analysis, is missing.
**Minimal Experiment:** On 4 anatomies, sweep n ∈ {1,3,5,10,30}; compare DINO-feature correspondence transfer vs LoRA fine-tuning; locate crossovers.
**Main Risk:** Correspondence quality collapses for pathological/deformed cases, exactly where value is highest.

### IDEA-B-0025 — Does matting-style supervision improve binary segmentation of soft-boundary classes?
**One-sentence idea:** Test whether supervising smoke/haze as continuous alpha mattes (density) improves subsequent binary-mask metrics compared to direct binary supervision, even when only binary GT quality is available at scale.
**Problem:** Binary masks force an arbitrary threshold through a physically continuous quantity (optical density), potentially teaching contradictory gradients near soft boundaries.
**Core Hypothesis:** Models pre-supervised on (even approximate) alpha targets and thresholded at evaluation outperform binary-trained models on binary IoU, because the continuous target removes gradient conflict in transition zones.
**Why Important:** Could change the supervision format for all amorphous classes without requiring new evaluation infrastructure.
**Why Possibly Novel:** Matting and segmentation communities are disjoint; the specific claim that alpha supervision improves binary metrics on amorphous classes is untested.
**Minimal Experiment:** Derive pseudo-alpha from multi-rater soft consensus or compositing; train alpha-then-threshold vs binary-direct at matched capacity; compare binary IoU and boundary F1.
**Main Risk:** Pseudo-alpha quality may be too poor to reveal the effect.

### IDEA-B-0026 — Complexity-normalized annotation value for active dataset construction
**One-sentence idea:** Build an acquisition criterion that ranks images by expected model improvement per annotation-minute, using a learned annotation-time model based on boundary complexity, and test it against accuracy-only acquisition.
**Problem:** Active learning maximizes informativeness per image, but images differ 10× in annotation cost; the right objective is information per unit cost, which requires predicting cost.
**Core Hypothesis:** A cost-aware acquisition (value/predicted-minutes) reaches target IoU with substantially less total annotation time than value-only acquisition, especially on datasets with heterogeneous boundary complexity.
**Why Important:** Time, not image count, is the real budget in expert-annotation settings like radiology.
**Why Possibly Novel:** Annotation-time prediction models exist in HCI, but coupling them into acquisition functions for dense labeling is rare.
**Minimal Experiment:** Fit a time model from logged annotation sessions (or public timing datasets); run simulated + small real active-learning rounds under both criteria; compare wall-clock-to-IoU.
**Main Risk:** Time models may transfer poorly across annotators and tools.

### IDEA-B-0027 — Rater-specific heads versus consensus training for generalizing to new raters
**One-sentence idea:** Compare training with per-rater output heads (then averaging) against training on consensus masks, evaluating on a held-out rater to determine which strategy captures transferable structure versus rater idiosyncrasy.
**Problem:** Multi-rater data can be consumed by consensus (losing information) or by rater modeling (risking overfitting to seen raters); which generalizes to unseen raters is unresolved for segmentation.
**Core Hypothesis:** Rater-specific heads improve fit to seen raters but consensus training generalizes better to unseen raters unless rater count exceeds a threshold where the rater distribution is itself learnable.
**Why Important:** Practical guidance for every multi-rater medical dataset and for defining what "ground truth" a deployed model should target.
**Why Possibly Novel:** Rater-modeling papers rarely evaluate on held-out raters, which is the deployment-relevant test.
**Minimal Experiment:** On a multi-rater dataset (≥6 raters), train both schemes with leave-one-rater-out evaluation; sweep rater counts.
**Main Risk:** Public datasets with many raters per image are scarce.

### IDEA-B-0028 — Are prompted models more or less shortcut-prone than unprompted ones?
**One-sentence idea:** Test whether spatial prompting suppresses reliance on dataset shortcuts (rulers in dermoscopy, scanner tags, positioning artifacts) compared to unprompted segmentation trained on the same data.
**Problem:** Shortcut learning is documented for classifiers; it is unknown whether the prompt's spatial anchor changes a dense model's incentive to exploit contextual shortcuts.
**Core Hypothesis:** Prompted models are measurably less sensitive to shortcut-feature interventions (artifact removal/insertion) than unprompted models at matched accuracy, because prompts absorb the localization role shortcuts otherwise play.
**Why Important:** If true, prompting is a structural mitigation for shortcut learning—a new argument for interactive designs in high-stakes imaging.
**Why Possibly Novel:** Shortcut analyses have not compared prompted vs unprompted paradigms under controlled interventions.
**Minimal Experiment:** Inject controllable shortcuts into training data (synthetic tags correlated with targets); train both paradigms; measure performance change when shortcuts are removed or adversarially placed at test time.
**Main Risk:** Synthetic shortcuts may be unrepresentative of subtle real ones.

### IDEA-B-0029 — Disentangling object rarity from context rarity in the long tail
**One-sentence idea:** Use counterfactual paste-in-context composites to measure how much tail-class failure is due to the object's rare appearance versus its rare context, per class.
**Problem:** Tail objects co-occur with tail contexts; standard evaluation cannot say whether models fail to recognize the object or fail to expect it there.
**Core Hypothesis:** For a substantial fraction of tail classes, placing the object in a frequent context recovers most of the performance gap, indicating context-prior failure rather than appearance failure.
**Why Important:** The two failure modes need opposite remedies (context augmentation vs appearance data), so the decomposition directly guides data collection.
**Why Possibly Novel:** Context-vs-appearance decomposition via controlled compositing has not been applied systematically across a long-tail benchmark.
**Minimal Experiment:** For 30 tail classes, create context-swap composites (object into head-class contexts and vice versa); evaluate public models; report the recovery fraction per class.
**Main Risk:** Compositing artifacts could themselves alter detectability; needs artifact controls (same-context re-pasting).

### IDEA-B-0030 — The annotation-savings frontier of sparse-point video supervision with temporal propagation
**One-sentence idea:** Quantify the tradeoff frontier between annotation sparsity (points per frame, frames per second labeled) and propagated-label error for fire/smoke video, identifying where propagation error overtakes annotation savings.
**Problem:** Temporal propagation multiplies sparse labels but accumulates drift, especially for deforming smoke; the field lacks a quantitative frontier to plan labeling campaigns.
**Core Hypothesis:** Propagated-label error grows with a measurable per-second drift rate that depends on plume deformation statistics, yielding a computable optimal keyframe interval per scene type.
**Why Important:** Wildfire monitoring needs massive labeled video cheaply; a drift-calibrated recipe converts one annotation into a known-quality label set.
**Why Possibly Novel:** Propagation is widely used, but a calibrated error-accumulation model for amorphous deforming targets is missing.
**Minimal Experiment:** On densely labeled smoke clips, subsample keyframes at varying intervals, propagate with a video segmenter, measure error growth curves, and fit the drift model; validate keyframe-interval predictions on held-out clips.
**Main Risk:** Drift may be regime-dependent (wind changes), making a single rate insufficient.

### IDEA-B-0031 — Pixel imbalance treatment changes calibration more than recall
**One-sentence idea:** Test the claim that common remedies for extreme pixel imbalance (small-lesion oversampling, mosaic cropping) primarily alter confidence calibration rather than detection recall of tiny lesions.
**Problem:** Imbalance remedies are evaluated on IoU/recall; if their main effect is calibration shift, published comparisons measure the wrong quantity and clinical thresholds inherited from them are wrong.
**Core Hypothesis:** At matched recall, oversampling-based training produces systematically inflated lesion-pixel confidence relative to natural sampling, and this calibration difference (not recall) explains most downstream threshold-sensitivity differences.
**Why Important:** Deployed medical systems operate at fixed thresholds; miscalibration from training-data engineering is a silent safety issue.
**Why Possibly Novel:** The imbalance literature rarely separates calibration effects from discrimination effects in dense prediction.
**Minimal Experiment:** Train matched models under natural vs oversampled regimes; compare ROC (discrimination) against reliability diagrams (calibration) specifically on lesion pixels; test threshold transfer across regimes.
**Main Risk:** Calibration metrics on tiny-pixel populations are high variance; needs many lesions.

### IDEA-B-0032 — How much boundary "progress" is annotation-schema change? A cross-version audit
**One-sentence idea:** Use images annotated in multiple dataset versions/projects (e.g., the same photos masked by different projects) to estimate how much apparent model improvement on boundaries is attributable to schema differences rather than capability.
**Problem:** Cross-dataset and cross-era comparisons of boundary quality conflate model progress with evolving annotation standards (mask tightness, hole handling, occlusion rules).
**Core Hypothesis:** A schema-transfer function fitted between annotation projects explains a nontrivial share of measured cross-dataset boundary-metric differences among public models, and normalizing by it changes some conclusions about which model is better.
**Why Important:** Keeps the field's measurement of progress honest as benchmarks proliferate and age.
**Why Possibly Novel:** Schema effects are folklore; fitting explicit inter-schema transfer functions from doubly annotated images is new methodology.
**Minimal Experiment:** Identify doubly annotated image sets across projects; fit boundary-offset/hole/occlusion transfer functions; re-score public checkpoints raw vs schema-normalized (report only measured re-scores).
**Main Risk:** Doubly annotated overlaps may be small or unrepresentative.

### IDEA-B-0033 — Name ambiguity, not visual rarity, as a driver of tail-class open-vocabulary failure
**One-sentence idea:** Decompose open-vocabulary segmentation failures on tail classes into linguistic causes (polysemous or obscure class names) versus visual causes (rare appearance), by intervening on the text side only.
**Problem:** Open-vocab models fail on rare classes, and everyone assumes the cause is visual rarity, but tail class names are also rarer and more ambiguous in the text encoder's training distribution.
**Core Hypothesis:** For a meaningful fraction of tail classes, replacing the class name with a disambiguated description (or a name that is frequent in text corpora) recovers a large share of the gap, holding the image pathway fixed.
**Why Important:** If language is the bottleneck, the fix is prompt engineering or text-encoder training—far cheaper than collecting rare visual data.
**Why Possibly Novel:** Text-side interventions as a causal probe for long-tail dense prediction are rarely isolated from visual factors.
**Minimal Experiment:** On a long-tail benchmark, evaluate per-class performance under {original name, synonym set, LLM-generated disambiguated description}; correlate recovery with corpus-frequency and polysemy measures of names.
**Main Risk:** Description prompts can leak spatial hints, inflating recovery for non-linguistic reasons; needs controls.

### IDEA-B-0034 — Negative-supervision leakage in merged partially labeled datasets
**One-sentence idea:** Measure the gradient-level interference caused by the mutually-exclusive-classes assumption when merging datasets in which different organs/classes are labeled in different subsets, and quantify the resulting performance loss versus a leakage-aware objective.
**Problem:** When dataset A labels only livers and dataset B only kidneys, standard training treats A's kidneys as background, actively teaching the model to suppress true structures.
**Core Hypothesis:** The magnitude of suppression scales with the co-occurrence rate of unlabeled true structures, and masking the loss over classes not annotated in each source recovers a predictable fraction of the loss, measurable per class from co-occurrence statistics alone.
**Why Important:** Merged partial datasets are the only realistic route to broad-coverage medical segmentation; quantifying the leakage tax and its predictability makes merging principled.
**Why Possibly Novel:** Partial-label training exists, but a predictive, per-class quantification of leakage harm from co-occurrence statistics is missing.
**Minimal Experiment:** Merge two fully labeled datasets while synthetically hiding label subsets (so truth is known); train naive vs loss-masked; regress per-class damage against co-occurrence rates; verify predictions on a real merged corpus.
**Main Risk:** Real merged corpora have additional shifts (scanners, protocols) that confound the leakage effect.
### IDEA-B-0035 — Annotator fatigue as a measurable, correctable label-quality gradient
**One-sentence idea:** Detect within-session degradation of mask quality from annotation timestamps and test whether fatigue-weighted training improves models over uniform weighting.
**Problem:** Long annotation sessions plausibly degrade boundary care, injecting a time-correlated quality gradient into datasets that training treats as homogeneous.
**Core Hypothesis:** Late-session masks show measurably higher disagreement with expert re-annotation than early-session masks, and down-weighting or re-verifying late-session labels yields models with better boundary metrics at zero extra annotation cost.
**Why Important:** A free quality signal (timestamps) that most datasets already have could be systematically exploited.
**Why Possibly Novel:** Fatigue is studied in ergonomics, not as a usable weighting signal for dense-label training.
**Minimal Experiment:** On datasets with session logs (or a small purpose-run annotation study), quantify quality-vs-session-position; train weighted vs unweighted models; compare boundary F1.
**Main Risk:** Session metadata is rarely released; effect size may be annotator-dependent.

### IDEA-B-0036 — Small-fire long tail in aerial imagery: resolution normalization versus oversampling
**One-sentence idea:** Determine whether the long tail of small/early fires in aerial datasets is better addressed by ground-sample-distance (GSD) normalization than by small-object oversampling, by decomposing failure into resolution effects and frequency effects.
**Problem:** Early fires are both rare and small; detection pipelines conflate the two, and remedies for one (oversampling) do not fix the other (sub-resolution signal).
**Core Hypothesis:** After GSD normalization (rescaling so plumes occupy comparable pixel footprints), most of the small-fire performance gap closes without any resampling, showing the tail is primarily a resolution artifact rather than a data-frequency problem.
**Why Important:** Early-fire detection is the highest-value operating point for wildfire response; identifying the true bottleneck directs sensor and data investments.
**Why Possibly Novel:** GSD as a controlled experimental variable (rather than a nuisance) is rare in fire-detection research.
**Minimal Experiment:** Build GSD-stratified evaluation from aerial datasets with altitude metadata; compare native vs GSD-normalized inference and oversampled training; attribute the gap.
**Main Risk:** Upsampling low-GSD imagery cannot create missing information; normalization may only relabel the problem.

### IDEA-B-0037 — An annotation-tolerance-derived IoU ceiling as a function of object size
**One-sentence idea:** Derive analytically and verify empirically the maximum achievable IoU given a stated annotation boundary tolerance (e.g., ±2 px), as a function of object size and shape, and flag benchmark strata that are already at ceiling.
**Problem:** Guidelines permit small boundary tolerances that translate into large relative errors for small objects, but papers still report and chase IoU differences within the ceiling.
**Core Hypothesis:** For objects below a size threshold determined by the tolerance and perimeter-to-area ratio, top methods are statistically at the annotation ceiling, and residual gaps between them are noise.
**Why Important:** Prevents wasted research chasing unreachable IoU and motivates size-aware reporting standards.
**Why Possibly Novel:** The ceiling has been noted qualitatively; a closed-form, shape-dependent version validated against multi-rater data has not been standard practice.
**Minimal Experiment:** Derive ceiling curves; validate against multi-rater variance on 2 datasets; overlay public leaderboard results per size bin.
**Main Risk:** Real tolerance varies by annotator and structure, complicating a single-parameter model.

### IDEA-B-0038 — Instance versus semantic supervision for clumped-object counting downstream
**One-sentence idea:** For clumped targets (cell clusters, overlapping smoke plumes), test which annotation format—instance masks, semantic masks, or density maps—yields the best downstream counting and area estimation per annotation dollar.
**Problem:** Annotation format is chosen by convention before the downstream use (usually counting/quantification) is considered, and instance boundaries between clumped objects may be arbitrary anyway.
**Core Hypothesis:** For clump-dominated data, density-map supervision achieves better counting accuracy per annotation minute than instance masks, and the instance-mask advantage appears only below a measurable occlusion-rate threshold.
**Why Important:** Aligns annotation spending with the quantity actually consumed by science and monitoring applications.
**Why Possibly Novel:** Cross-format comparisons at matched annotation cost (not matched image count) are rarely done.
**Minimal Experiment:** On microscopy data with full instance GT, derive all three formats, cost each via timing studies, train matched models per format at iso-cost, and compare counting/area errors across occlusion strata.
**Main Risk:** Conclusions may be sensitive to the specific counting model architecture used.

### IDEA-B-0039 — Does data pruning transfer from classification to dense prediction?
**One-sentence idea:** Test whether coreset/data-pruning metrics validated on classification (forgetting scores, EL2N-style scores) select good subsets for segmentation fine-tuning, or whether dense tasks need boundary-aware pruning signals.
**Problem:** Data pruning promises to cut fine-tuning cost, but its scoring functions were designed for image-level labels and may discard images whose value lies in rare boundary configurations.
**Core Hypothesis:** Classification-derived pruning scores are weakly correlated with an image's marginal value for segmentation, and a disagreement-based dense score (SAM-vs-GT residual) retains substantially more performance at 20–40% budgets.
**Why Important:** Fine-tuning foundation models on the right 20% of data would change annotation and compute economics.
**Why Possibly Novel:** Data pruning research is almost entirely classification-based; a dense-prediction transfer study with a native dense score is missing.
**Minimal Experiment:** On 3 datasets, prune to {10,20,40}% with each score; fine-tune identical adapters; compare IoU retention and per-stratum losses.
**Main Risk:** Pruning gains may be dominated by dataset redundancy (duplicates), making all reasonable scores similar.

### IDEA-B-0040 — Ignore-region semantics: the unmeasured effect of "unknown" pixels on open-vocabulary training
**One-sentence idea:** Systematically vary how unlabeled/"other" pixels are treated (hard negative, ignored, soft prior) when training open-vocabulary segmenters, and measure the effect on novel-class recall.
**Problem:** Datasets leave most pixels unlabeled, and training recipes silently choose a semantics for them; treating unknowns as negatives plausibly suppresses exactly the novel classes open-vocab models should discover.
**Core Hypothesis:** Novel-class recall is strongly sensitive to unknown-pixel treatment—more than to several commonly tuned hyperparameters—and ignoring-with-density-prior dominates hard-negative treatment.
**Why Important:** A recipe-level variable that nobody reports may explain large cross-paper variance in open-vocabulary results.
**Why Possibly Novel:** Ignore-region handling has never been the primary manipulated variable in an open-vocab segmentation study.
**Minimal Experiment:** Train matched open-vocab models under 4 unknown-pixel treatments on the same data; evaluate base-class and novel-class metrics; report sensitivity.
**Main Risk:** Effects may interact with the specific text-alignment method used, requiring replication across 2 model families.

---

## Cluster 2 — Domain Shift / Cross-Domain Transfer (IDEA-B-0041 … IDEA-B-0080)

### IDEA-B-0041 — Frequency-band attribution of SAM's medical-domain failures
**One-sentence idea:** Decompose SAM's natural-to-medical performance drop into frequency bands by swapping amplitude spectra between domains and measuring prompted-mask degradation per band.
**Problem:** "Domain gap" is invoked monolithically; we do not know whether SAM fails on medical images because of low-level spectral statistics or because of missing high-level anatomical priors.
**Core Hypothesis:** A large, quantifiable fraction of the zero-shot drop is explained by low/mid-frequency amplitude statistics (recoverable by spectrum matching without any training), with the residual concentrated in structures requiring anatomical priors.
**Why Important:** If much of the gap is spectral, cheap test-time normalization replaces expensive fine-tuning for a known subset of cases; if not, the field can stop pursuing style-transfer fixes.
**Why Possibly Novel:** Frequency-swap causal probes have been used for classifier robustness but not to budget a promptable segmenter's domain gap.
**Minimal Experiment:** On 3 modalities with GT, evaluate zero-shot SAM on original, amplitude-swapped, and band-limited hybrid images with fixed prompts; attribute IoU changes per band.
**Main Risk:** Phase-amplitude interactions may make the decomposition non-additive.

### IDEA-B-0042 — Where does grayscale shift get absorbed? Channel-adapter depth analysis
**One-sentence idea:** Localize where single-channel medical inputs are reconciled with RGB-pretrained encoders by training minimal adapters at different depths and measuring where adaptation capacity is actually spent.
**Problem:** The community replicates grayscale into three channels by habit; whether this wastes early-layer capacity or is harmlessly absorbed is unknown.
**Core Hypothesis:** A learned 1→3 channel stem with ~0.001% of parameters matches full patch-embed retraining, showing the grayscale gap is a stem-level phenomenon, and deeper adapters spend their capacity re-deriving the same correction.
**Why Important:** Establishes the minimal sufficient intervention for the most common medical input mismatch, simplifying dozens of ad hoc pipelines.
**Why Possibly Novel:** Input-channel mismatch has never been isolated as a measurable adaptation-depth question.
**Minimal Experiment:** Compare {channel replication, learned stem, patch-embed fine-tune, LoRA-at-depth-k} on 3 grayscale modalities at matched budgets; analyze where each closes the gap.
**Main Risk:** Modality-specific intensity semantics (CT HU vs X-ray) may make results non-uniform across modalities.

### IDEA-B-0043 — A shift-difficulty ordering within MRI: is cross-sequence harder than cross-anatomy?
**One-sentence idea:** Construct a controlled difficulty ordering of intra-medical domain shifts (cross-sequence, cross-scanner, cross-anatomy, cross-pathology) and test whether adaptation methods preserve their ranking across shift types.
**Problem:** "Medical domain adaptation" lumps together qualitatively different shifts; methods are declared superior based on one shift type and assumed to generalize.
**Core Hypothesis:** Method rankings are not stable across shift types—for example, methods best at cross-scanner (style-like) shifts are systematically worse at cross-sequence (semantics-like) shifts—implying shift-type must be a reported experimental variable.
**Why Important:** Prevents overgeneralized method claims and gives practitioners a lookup from their shift type to the right method family.
**Why Possibly Novel:** A factorial shift-type × method-family study with ranking-stability statistics has not been assembled for segmentation.
**Minimal Experiment:** Use multi-sequence, multi-scanner MRI datasets to build 4 controlled shift axes; evaluate 5 adaptation method families; compute ranking correlations across axes.
**Main Risk:** Public data may not support all cells of the factorial design with matched difficulty.

### IDEA-B-0044 — Prompt-space test-time adaptation: adapting inputs to the model instead of weights
**One-sentence idea:** At deployment, adapt only the prompt embeddings (a few hundred parameters) per target domain via self-consistency objectives, testing whether prompt-space TTA avoids the instability and forgetting of weight-space TTA.
**Problem:** Entropy-minimization TTA is notoriously unstable for dense prediction and permanently drifts weights; promptable models offer an unexplored adaptation surface that leaves weights untouched.
**Core Hypothesis:** Optimizing a domain-level prompt-embedding offset for cross-prompt consistency recovers a meaningful fraction of the fine-tuning gain with zero catastrophic-failure runs, whereas weight-space TTA exhibits nonzero collapse rates on the same streams.
**Why Important:** Safe, reversible test-time adaptation is a requirement for regulated deployments (hospitals, safety monitoring).
**Why Possibly Novel:** TTA literature adapts normalization/weights; the prompt-embedding space as the sole adaptation surface is structurally new.
**Minimal Experiment:** On 3 shifted streams, compare frozen, TENT-style, and prompt-offset TTA over long sequences; report mean IoU and collapse frequency.
**Main Risk:** A single global prompt offset may be too low-capacity for heterogeneous shifts.

### IDEA-B-0045 — Day-to-night smoke segmentation: luminance shift versus texture-cue loss
**One-sentence idea:** Decompose nighttime smoke-segmentation failure into recoverable luminance-distribution shift versus irrecoverable loss of texture cues, using controlled relighting and sensor-simulation counterfactuals.
**Problem:** Night performance collapse is treated as one problem, but fixes differ radically depending on whether information is shifted (normalizable) or destroyed (needs different sensors/cues).
**Core Hypothesis:** A measurable fraction of the night gap is closed by physically calibrated luminance/noise normalization alone, and the residual correlates with local texture SNR falling below a threshold—defining where RGB-only night smoke detection is impossible.
**Why Important:** Wildfire monitoring is 24/7; knowing the information-theoretic limit of night RGB prevents chasing impossible gains and justifies thermal/NIR investment where needed.
**Why Possibly Novel:** Information-destruction versus distribution-shift decomposition has not been applied to nighttime amorphous-target segmentation.
**Minimal Experiment:** Use day/night pairs from fixed cameras (or radiometrically relit day images validated against real night captures); evaluate with/without calibrated normalization; regress residual error against local SNR.
**Main Risk:** Fixed-camera day/night pairs with smoke in both conditions are rare; simulation validity must be checked carefully.

### IDEA-B-0046 — Do stain normalization and adapter tuning fix the same errors in histopathology?
**One-sentence idea:** Compare stain normalization and PEFT adaptation on cross-scanner/cross-lab histopathology not by mean scores but by error-set overlap, testing whether they are redundant or complementary mechanisms.
**Problem:** Both approaches "improve cross-site performance," and labs choose one by culture; whether they correct the same pixels or different ones determines if combining them is principled or redundant.
**Core Hypothesis:** Stain normalization and adapter tuning correct substantially disjoint error sets (color-driven vs morphology-context errors), so their combination is additive on disjoint strata rather than uniformly.
**Why Important:** Replaces vibes-based pipeline choices with a mechanism-level account of what each fix does, and predicts when combination is worth it.
**Why Possibly Novel:** Error-overlap analysis (per-pixel/per-region contingency of corrections) is rarely used to compare adaptation mechanisms.
**Minimal Experiment:** On 2 cross-site pathology tasks, apply each method and both; compute McNemar-style contingency on corrected/uncorrected regions; stratify by color-shift vs morphology-shift measures.
**Main Risk:** Interaction effects may not decompose cleanly at the region level.

### IDEA-B-0047 — Shift-absorption depth: which transformer blocks resolve which shifts during fine-tuning
**One-sentence idea:** Measure, via layer-wise representational drift during fine-tuning, at what depth different shift types (style, resolution, semantics, label-convention) get absorbed in a foundation segmenter, and test whether this predicts optimal adapter placement.
**Problem:** Adapter placement is chosen by grid search per paper; a predictive theory linking shift type to the depth where adaptation must occur is missing.
**Core Hypothesis:** Style-like shifts are absorbed in early blocks and semantic shifts in late blocks (measurable as concentrated representational drift), and placing adapters only at the measured absorption depth matches full-depth adaptation at a fraction of parameters.
**Why Important:** Converts PEFT configuration from search to prediction, saving compute across the entire adaptation literature.
**Why Possibly Novel:** Drift-based absorption-depth measurement as a placement predictor has not been validated for dense prediction.
**Minimal Experiment:** Fine-tune fully on 4 shift types; compute per-block CKA drift; then train depth-targeted adapters at predicted vs mispredicted depths and compare.
**Main Risk:** Absorption may be distributed rather than concentrated for some shifts, weakening placement predictions.

### IDEA-B-0048 — Turbidity versus transparency: which breaks underwater glass/plastic segmentation?
**One-sentence idea:** Factorially separate water-column effects (turbidity, color attenuation) from object transparency effects in underwater transparent-debris segmentation using controlled tank imagery.
**Problem:** Underwater plastic/glass detection fails badly, but the compounding of medium effects and target transparency has never been experimentally separated, so it is unclear what to fix.
**Core Hypothesis:** Moderate turbidity degrades transparent-target segmentation disproportionately versus opaque targets (an interaction effect), because both the medium and the target derive their appearance from background light transport.
**Why Important:** Marine debris monitoring is a growing application; the interaction structure dictates whether solutions should target the medium (dehazing) or the object model.
**Why Possibly Novel:** A controlled turbidity × transparency factorial dataset and analysis does not exist.
**Minimal Experiment:** Tank captures with controlled turbidity levels × {opaque, translucent, transparent} objects; evaluate zero-shot and fine-tuned models; test the interaction term statistically.
**Main Risk:** Tank conditions may not represent open-water optics; needs a small real-world validation set.

### IDEA-B-0049 — Sensor-noise-model matching versus GAN translation for thermal sim-to-real
**One-sentence idea:** Test whether matching the physical sensor noise model (NETD, fixed-pattern noise, halo/blooming) of thermal cameras closes more of the sim-to-real gap for fire segmentation than learned image-to-image translation.
**Problem:** Sim-to-real for thermal fire imagery defaults to GAN translation, which can hallucinate content; the alternative—physically modeling the sensor—has no head-to-head evidence.
**Core Hypothesis:** For thermal imagery, sensor-noise matching explains the majority of the sim-to-real gap (because content is simple radiometry), whereas GAN translation adds little and increases label-image inconsistency.
**Why Important:** Determines whether thermal fire datasets can be synthesized with cheap, controllable physics rather than fragile learned translation.
**Why Possibly Novel:** Component-wise sensor modeling as a rival (not complement) to GAN translation is rarely evaluated for segmentation transfer.
**Minimal Experiment:** Render fire scenes; apply (a) nothing, (b) calibrated sensor model, (c) GAN translation, (d) both; train and evaluate on real thermal fire data; attribute the gap closure.
**Main Risk:** Calibrating a sensor model requires access to the target camera or its specs.

### IDEA-B-0050 — Do learned visual prompts transfer across domains worse than adapters of equal in-domain quality?
**One-sentence idea:** Compare visual prompt tuning and adapter tuning matched on in-domain performance, testing whether prompts—being input-space interventions—transfer worse to related unseen domains.
**Problem:** PEFT methods are compared in-domain; deployment involves related-but-unseen domains, where the geometry of the learned intervention (input-space vs weight-space) may matter.
**Core Hypothesis:** At matched in-domain IoU, adapter-tuned models generalize better to related unseen domains than prompt-tuned models, because prompts encode dataset-specific input statistics rather than reusable computation changes.
**Why Important:** Changes which PEFT to deploy when downstream drift is expected—i.e., always, in real systems.
**Why Possibly Novel:** Transferability (rather than in-domain accuracy) as the primary comparison axis for PEFT families is largely unexamined for dense tasks.
**Minimal Experiment:** Tune both families on domain A to matched IoU; evaluate zero-shot on related domains B, C; repeat over 3 source domains; compare transfer gaps.
**Main Risk:** "Matched in-domain performance" is hard to achieve exactly; requires careful budget sweeps.

### IDEA-B-0051 — The interference matrix of sequential multi-specialty adaptation
**One-sentence idea:** Build the full pairwise interference/transfer matrix for sequentially fine-tuning one foundation segmenter across medical specialties, and test whether interference is predictable from domain-embedding distances.
**Problem:** Hospitals adapt models specialty-by-specialty; whether radiology adaptation damages prior dermatology adaptation (and by how much, and asymmetrically) is unmeasured.
**Core Hypothesis:** Forgetting is strongly asymmetric (adapting to modality-far domains damages modality-near ones more than vice versa) and is predictable (R² meaningful) from distances between domain embeddings of unlabeled samples.
**Why Important:** A predictive interference model enables planning adaptation schedules and deciding when to fork model instances.
**Why Possibly Novel:** Continual-learning studies use toy task sequences; an empirical specialty-level interference matrix with a predictive geometry model is new.
**Minimal Experiment:** Sequentially fine-tune across 6 specialties in multiple orders; measure the 6×6 forgetting matrix; regress against embedding distances.
**Main Risk:** Compute cost of order permutations; may need factorial subsampling.

### IDEA-B-0052 — Ground-to-drone viewpoint shift: scale, geometry, or context priors?
**One-sentence idea:** Decompose the performance drop of ground-trained fire/smoke models on drone imagery into scale distribution, perspective geometry, and background-context factors via homography-controlled resampling.
**Problem:** Aerial deployment of ground-trained models fails, and teams respond by collecting expensive drone data without knowing which factor dominates.
**Core Hypothesis:** After matching apparent scale distributions by resampling, the majority of the residual gap is explained by context priors (sky/horizon composition) rather than perspective geometry per se.
**Why Important:** If context dominates, cheap background-composition augmentation substitutes for drone data collection campaigns.
**Why Possibly Novel:** Viewpoint shift is usually treated as monolithic; a three-factor decomposition with geometric controls is not standard.
**Minimal Experiment:** Construct scale-matched, horizon-matched, and geometry-warped versions of evaluation sets; measure marginal gaps; validate the dominant factor with targeted augmentation training.
**Main Risk:** Factors interact; a strictly additive decomposition may not hold.

### IDEA-B-0053 — Ontology shift disguised as appearance shift across endoscopy datasets
**One-sentence idea:** Estimate what fraction of cross-dataset performance drop between endoscopy benchmarks is due to differing label definitions ("polyp" boundaries, inclusion rules) rather than appearance shift, using a small bridge re-annotation.
**Problem:** Cross-dataset drops are cited as evidence of appearance domain gaps, motivating adaptation methods, but part of the drop may be that the datasets define the target differently.
**Core Hypothesis:** Re-annotating a bridge set of images from dataset B under dataset A's written protocol recovers a substantial fraction of the cross-dataset drop, bounding the true appearance gap well below the reported gap.
**Why Important:** Overestimated appearance gaps misdirect the domain-adaptation literature; honest gap accounting recalibrates the problem.
**Why Possibly Novel:** Protocol-controlled bridge re-annotation as a gap-decomposition instrument is rarely executed.
**Minimal Experiment:** Select 150 images from dataset B, re-annotate under A's protocol with trained annotators, evaluate A-trained models against both label versions; report the decomposition.
**Main Risk:** Written protocols may be too vague to reproduce faithfully.

### IDEA-B-0054 — Which domain-distance metric actually predicts fine-tuning gain?
**One-sentence idea:** Benchmark candidate domain-distance measures (FID in various feature spaces, MMD, spectral divergences, token-distribution shifts) as predictors of how much a foundation segmenter will gain from fine-tuning on a target domain.
**Problem:** Practitioners need to predict, before annotating, whether fine-tuning will pay off; distance metrics are used informally without validation against realized gains.
**Core Hypothesis:** Distances computed in the segmenter's own mid-layer token space predict fine-tuning gain markedly better than generic FID/MMD, because gain depends on mismatch as seen by this model, not any model.
**Why Important:** A validated predictor turns adaptation planning into a measurement problem, saving annotation budgets across the field.
**Why Possibly Novel:** Predictor benchmarking against realized fine-tuning gains (not proxy shift labels) across many segmentation domains is missing.
**Minimal Experiment:** Assemble 15+ target datasets; fine-tune a fixed recipe on each; correlate pre-computed distances with realized gains; report predictor rankings with confidence intervals.
**Main Risk:** Gains also depend on target-task difficulty, requiring careful normalization.

### IDEA-B-0055 — Fog as a negative domain: does adapting to fog worsen smoke detection?
**One-sentence idea:** Test whether robustness-oriented adaptation toward foggy conditions increases false positives on smoke (and vice versa), revealing an adversarial coupling between a nuisance domain and a target class that look alike.
**Problem:** Weather robustness and smoke detection are pursued independently; because fog and smoke are near-identical scattering phenomena, adapting to tolerate one may suppress or hallucinate the other.
**Core Hypothesis:** Models adapted for fog invariance show a measurable increase in smoke false negatives (fog-invariance transfers to smoke-invariance), quantifiable as a robustness-specificity tradeoff curve.
**Why Important:** Safety systems must be robust to fog and sensitive to smoke simultaneously; the coupling, if real, requires joint—not independent—treatment.
**Why Possibly Novel:** The concept of a "negative domain" whose invariance actively harms a confusable target class is not formalized in the robustness literature.
**Minimal Experiment:** Fine-tune with fog augmentation/adaptation at varying strengths; measure smoke TPR/FPR shifts on fixed test sets; map the tradeoff curve.
**Main Risk:** Effect may be avoidable with trivially better class separation, making the finding short-lived.

### IDEA-B-0056 — Positional-embedding interpolation as the dominant cross-resolution failure factor
**One-sentence idea:** Isolate how much of the performance drop when running high-res-trained ViT segmenters on native low-resolution imagery (ultrasound, CCTV) is attributable to positional-embedding interpolation rather than information loss.
**Problem:** Cross-resolution deployment is universal, and pos-embed interpolation is a silent default whose cost has not been separated from genuine resolution limits.
**Core Hypothesis:** A significant fraction of the low-resolution drop persists when images are synthetically degraded but processed at training resolution (isolating information loss), and the remainder—attributable to pos-embed geometry—can be recovered by resolution-specific embedding calibration without touching other weights.
**Why Important:** A pure-implementation fix could recover deployment performance across many low-res domains for free.
**Why Possibly Novel:** Pos-embed interpolation is studied for classification accuracy, not decomposed against information loss for dense prediction.
**Minimal Experiment:** Three-way comparison: native low-res, degraded-then-upsampled at training res, and low-res with calibrated embeddings; attribute the gaps.
**Main Risk:** Findings may differ across pos-embed schemes (learned, sinusoidal, relative), requiring a small matrix of models.

### IDEA-B-0057 — Token-statistics recalibration: a LayerNorm-era replacement for BN-based TTA
**One-sentence idea:** Develop and test the hypothesis that recalibrating token-population statistics (per-layer mean/scale of token distributions) at test time recovers domain performance for ViT segmenters, playing the role BatchNorm adaptation played for CNNs.
**Problem:** The most reliable classic TTA trick—updating BN statistics—has no ViT equivalent, since LayerNorm carries no cross-sample statistics; ViT-era dense TTA lacks a comparably simple mechanism.
**Core Hypothesis:** Domain shift manifests as measurable drift in token-population statistics at specific layers, and matching those statistics to source values via affine token corrections recovers a meaningful fraction of the shift loss without labels.
**Why Important:** A drop-in, optimization-free TTA primitive for transformer segmenters would be adopted immediately and broadly.
**Why Possibly Novel:** Token-population statistics as an explicit adaptation target (rather than a diagnostic) is underexplored for dense prediction.
**Minimal Experiment:** Measure token-statistic drift across 5 shifts; apply per-layer affine matching; evaluate IoU recovery vs TENT and vs oracle fine-tuning.
**Main Risk:** Affine corrections may be too weak for shifts that alter token covariance structure.

### IDEA-B-0058 — Transfer asymmetry as a probe of representation richness
**One-sentence idea:** Measure the asymmetry between natural→medical and medical→natural adaptation at matched adapter capacity, using the asymmetry as an operational measure of which pretraining produces more transferable dense representations.
**Problem:** Claims that natural-image pretraining is "richer" than medical pretraining are made without a symmetric, controlled measurement.
**Core Hypothesis:** Adaptation loss is systematically smaller in the natural→medical direction than the reverse at matched capacity and data, and the asymmetry magnitude varies by modality in a way that ranks pretraining corpora by transferable content.
**Why Important:** Provides an evidence-based answer to whether medical-specific foundation models are necessary or whether natural-image models plus adaptation suffice.
**Why Possibly Novel:** Bidirectional matched-budget transfer asymmetry has not been used as a formal representation-quality metric.
**Minimal Experiment:** Pretrain (or use existing) matched-scale models on natural and medical corpora; adapt each to the other side across 4 tasks at fixed budgets; compute asymmetry indices.
**Main Risk:** Matching pretraining scale/quality across corpora is difficult and may confound the asymmetry.

### IDEA-B-0059 — The prompt-type × shift-type robustness matrix
**One-sentence idea:** Systematically measure which prompt types (point, box, mask, text) degrade most under which domain shifts, producing a robustness matrix that tells deployers which interaction mode to trust under drift.
**Problem:** Prompt types are chosen for convenience; there is no evidence base for which prompting mode is most shift-robust, though anecdotes suggest large differences.
**Core Hypothesis:** Box prompts are systematically more shift-robust than point prompts (they constrain extent, reducing reliance on shifted appearance priors), and the point-box robustness gap widens with shift magnitude.
**Why Important:** Zero-cost deployment guidance: choosing the right prompt type may recover as much performance as expensive adaptation.
**Why Possibly Novel:** Prompt type has not been treated as a robustness variable crossed with shift type in any systematic study.
**Minimal Experiment:** Evaluate frozen promptable models across a 4-prompt × 6-shift grid with matched targets; report the interaction structure and its stability across model scales.
**Main Risk:** Results may be decoder-specific; requires 2–3 model families for external validity.

### IDEA-B-0060 — Specular-highlight handling: invariance training versus physical simulation for endoscopy transfer
**One-sentence idea:** Compare enforcing invariance to specular highlights against physically simulating them, as competing mechanisms for reducing cross-hospital endoscopy segmentation gaps, using highlight-controlled counterfactuals.
**Problem:** Specular highlights vary with scopes and light sources across hospitals and are a suspected driver of cross-site gaps, but the two natural remedies embody opposite philosophies (remove the cue vs teach the cue) and have never been compared causally.
**Core Hypothesis:** Invariance training discards clinically useful wetness/texture information (hurting borderline cases), while calibrated highlight simulation closes more of the cross-site gap by making the cue distribution-matched rather than absent.
**Why Important:** The invariance-vs-simulation question recurs across medical imaging nuisances; a clean causal comparison sets a template.
**Why Possibly Novel:** Highlight-controlled counterfactual evaluation (same frame, edited highlights) for segmentation transfer has not been done.
**Minimal Experiment:** Build highlight-edited counterfactual test sets; train both remedies at matched budgets; compare cross-site gaps and per-stratum losses on highlight-adjacent structures.
**Main Risk:** Highlight editing may introduce artifacts that confound the counterfactual.

### IDEA-B-0061 — Cross-species anatomical transfer: do human-tuned priors help or hurt veterinary segmentation?
**One-sentence idea:** Test whether human-anatomy fine-tuning of a foundation segmenter improves or degrades zero/few-shot performance on homologous veterinary structures, relative to the unadapted base model.
**Problem:** Veterinary imaging has little labeled data and borrows human-trained models, but whether human anatomical priors transfer (homology) or interfere (shape mismatch) is unknown.
**Core Hypothesis:** Human fine-tuning helps for organs with conserved topology (kidneys, bladder) but actively hurts relative to base SAM for organs with divergent morphology, and the sign is predictable from cross-species shape-model divergence.
**Why Important:** Establishes when medical transfer is a free win for the underserved veterinary domain and when it is a trap.
**Why Possibly Novel:** Cross-species transfer as a controlled probe of what anatomical fine-tuning encodes is essentially unstudied in the foundation-model era.
**Minimal Experiment:** Evaluate base vs human-organ-tuned models on labeled canine/feline CT structures; regress transfer delta against shape divergence measures.
**Main Risk:** Veterinary GT scarcity; may need to commission a small expert-labeled set.

### IDEA-B-0062 — Multispectral patch-embedding adaptation versus RGB compositing for satellite smoke
**One-sentence idea:** Determine whether adapting a foundation segmenter's input stem to raw multispectral bands outperforms the standard practice of feeding band-composited pseudo-RGB, and localize where spectral information is consumed in the network.
**Problem:** Satellite smoke/cloud discrimination hinges on spectral signatures that pseudo-RGB compositing collapses; whether foundation models can exploit raw bands through a learned stem is untested.
**Core Hypothesis:** A learned multispectral stem yields measurably better smoke-vs-cloud separation than any fixed band composite, with attribution analysis showing the network uses band ratios early rather than deep.
**Why Important:** Wildfire monitoring from geostationary satellites is scaling now; the input-representation decision affects every downstream system.
**Why Possibly Novel:** Stem-level multispectral adaptation of natural-image foundation segmenters, with consumption-depth analysis, is largely unexplored.
**Minimal Experiment:** On satellite scenes with smoke/cloud labels, compare fixed composites vs learned stems at matched trainable parameters; run band-ablation attribution.
**Main Risk:** Spectral advantages may be dataset-specific (sensor-dependent band sets).

### IDEA-B-0063 — Diversity versus quantity: the site-diversity exchange rate for robust fine-tuning
**One-sentence idea:** Quantify the exchange rate between number of training images and number of source sites for cross-site generalization, e.g., how many single-site images equal one image from an additional site.
**Problem:** Data collection budgets must choose between more images from available sites and onboarding new sites (expensive); the exchange rate has never been measured for segmentation.
**Core Hypothesis:** Cross-site generalization follows a law where site count enters with far greater marginal value than per-site image count once per-site n exceeds a small threshold, and the exchange rate is estimable from within-vs-between-site feature variance.
**Why Important:** Directly prices data-acquisition decisions for medical consortia and monitoring networks.
**Why Possibly Novel:** Diversity-quantity exchange has been examined for speech/classification, but not established for dense medical prediction with a variance-based predictor.
**Minimal Experiment:** With a multi-site dataset, train on grids of (sites × images/site) at matched totals; fit generalization surfaces; validate the variance-based predictor on a held-out consortium.
**Main Risk:** Site effects are heterogeneous; a single exchange rate may oversimplify.

### IDEA-B-0064 — Does classical UDA add anything on top of frozen foundation features? A null-hypothesis benchmark
**One-sentence idea:** Rigorously test whether established unsupervised domain adaptation machinery (adversarial alignment, self-training, entropy minimization) still improves segmentation when the backbone is a frozen modern foundation model with tuned prompts/probes.
**Problem:** UDA methods were validated on weak backbones; the field keeps combining them with foundation models without checking if their assumptions (misaligned features) still hold.
**Core Hypothesis:** For a majority of standard UDA benchmark pairs, frozen-foundation-feature baselines with target-side pseudo-label filtering match or beat classic UDA additions, rendering much of the machinery redundant—except on shift types identifiable in advance.
**Why Important:** Could retire a heavily cited methodology where it no longer helps, refocusing effort on genuinely open shift types.
**Why Possibly Novel:** A systematic "does UDA survive foundation features?" audit with matched budgets has not been published for segmentation.
**Minimal Experiment:** Run 6 UDA methods × 3 backbone regimes (scratch, supervised pretrain, foundation) × 4 benchmark pairs at matched compute; report marginal UDA gains per regime.
**Main Risk:** Benchmark selection bias; must include both stylistic and semantic shifts.

### IDEA-B-0065 — Routing versus merging domain-specific adapters for unseen-domain robustness
**One-sentence idea:** Compare a router over per-domain LoRAs against a single merged LoRA when inputs come from unseen domains, testing whether selection or interpolation degrades more gracefully off-distribution.
**Problem:** Multi-domain deployments must choose between adapter routing (sharp but brittle) and weight merging (smooth but blurred); off-distribution behavior—the common case—is the unmeasured criterion.
**Core Hypothesis:** Merged adapters dominate routing on unseen domains (interpolation covers gaps) while routing dominates on seen domains, with the crossover predictable from the unseen domain's embedding position relative to the training-domain hull.
**Why Important:** This decision is faced by every organization deploying one model across heterogeneous sources.
**Why Possibly Novel:** The seen/unseen crossover geometry for adapter routing vs merging has not been characterized for dense tasks.
**Minimal Experiment:** Train per-domain LoRAs on 5 domains; evaluate routing, merging, and oracle selection on 5 held-out domains at varying hull distances; map the crossover.
**Main Risk:** Router quality confounds the comparison; needs both learned and oracle routers.

### IDEA-B-0066 — Within-experiment drift: photobleaching as a live domain shift requiring online compensation
**One-sentence idea:** Treat photobleaching-induced intensity drift in longitudinal fluorescence microscopy as a continuous, monotonic domain shift and test whether online drift compensation beats periodic retraining.
**Problem:** Live-cell experiments degrade their own imaging domain over hours; models calibrated at t=0 silently decay, and current practice ignores or retrains ad hoc.
**Core Hypothesis:** Bleaching-induced degradation follows a predictable exponential signal-decay model per fluorophore, and a lightweight online intensity-recalibration conditioned on elapsed exposure recovers most late-experiment performance without new labels.
**Why Important:** Longitudinal microscopy underpins much of cell biology; an artifact-aware online correction protects thousands of experiments.
**Why Possibly Novel:** Domain shift with a known physical generator (photochemistry) is an unusual, exploitable structure absent from the adaptation literature.
**Minimal Experiment:** On time-lapse datasets, quantify segmentation decay vs cumulative exposure; implement physics-conditioned recalibration; compare against static and retrained baselines.
**Main Risk:** Bleaching interacts with biology (cells also change), confounding drift attribution.

### IDEA-B-0067 — Background-only adaptation: fixing the negative space instead of the targets
**One-sentence idea:** Test whether adapting a model only to the target domain's background statistics (using abundant target-free frames) reduces false positives as much as full adaptation, for rare-target tasks like fire and lesions.
**Problem:** For rare targets, most domain shift lives in the background (new scenes, scanners), and background-only data is free—yet adaptation methods insist on target-containing data that is scarce.
**Core Hypothesis:** Background-statistic adaptation on target-free imagery eliminates the majority of shift-induced false positives while leaving sensitivity unchanged, because FP causes are background-distribution phenomena.
**Why Important:** Enables adaptation from data every deployment already has (empty scenes) rather than data it lacks (positives).
**Why Possibly Novel:** Deliberate negative-space-only adaptation as a first-class method with FP/TP decomposition is not established.
**Minimal Experiment:** Adapt on target-free target-domain frames (self-supervised or pseudo-labeled background); measure FP and TP changes on held-out positives vs full adaptation.
**Main Risk:** Sensitivity may silently degrade if background adaptation shifts decision boundaries globally.

### IDEA-B-0068 — Layout-matched benchmarks: isolating what domain adaptation actually fixes
**One-sentence idea:** Construct cross-domain evaluation pairs matched in spatial layout (same scene structure, different domain rendering) to decompose adaptation gains into appearance-level and layout-level components.
**Problem:** Standard DA benchmarks (e.g., synthetic-to-real driving) conflate appearance shift with layout/content shift, so reported gains cannot be attributed to a mechanism.
**Core Hypothesis:** A large fraction of claimed adaptation gains on popular benchmarks comes from layout adaptation (object priors, class frequencies) rather than appearance invariance, reversing the standard interpretation of several method families.
**Why Important:** Method development is steered by benchmark interpretation; a decomposition instrument corrects the steering.
**Why Possibly Novel:** Layout-matched counterfactual benchmark construction for DA attribution has not been systematically done.
**Minimal Experiment:** Use paired renderings (same 3D scenes, multiple appearance domains) plus layout-shuffled controls; re-evaluate representative DA methods; report attribution splits.
**Main Risk:** Paired-rendering realism limits external validity to real-world DA.
### IDEA-B-0069 — Is miscalibration shift-invariant enough to correct from source alone?
**One-sentence idea:** Test whether the calibration error a segmenter develops under domain shift has a stable, source-predictable structure, so that a correction fitted on source-side simulated shifts transfers to real target shifts.
**Problem:** Adapted models are tuned for accuracy while their confidence remains miscalibrated on the target domain, and target labels for recalibration rarely exist.
**Core Hypothesis:** Across shift families, the miscalibration function (confidence-to-accuracy mapping) drifts in a low-dimensional, predictable way parameterized by an unsupervised shift-magnitude estimate, enabling label-free target recalibration.
**Why Important:** Calibrated confidence under shift is a precondition for clinical and safety deployments; a label-free recalibration recipe would be broadly adopted.
**Why Possibly Novel:** Calibration-transfer-under-shift has been studied for classifiers, but a shift-magnitude-parameterized correction for dense prediction is new.
**Minimal Experiment:** Fit calibration maps across simulated shift ladders on source data; parameterize by shift-magnitude estimates; test transfer of the fitted family to real cross-site shifts.
**Main Risk:** Real shifts may be multi-axis, breaking the low-dimensional parameterization.

### IDEA-B-0070 — Deployment prompt distributions: evaluating under how clinicians actually click
**One-sentence idea:** Collect and characterize real deployment prompt distributions (clinician clicks under time pressure) and measure the gap between benchmark-protocol prompts and deployment prompts as a domain shift in its own right.
**Problem:** All interactive-segmentation numbers are computed under curated prompt protocols; the prompt distribution at the point of care is unknown and probably harder.
**Core Hypothesis:** Deployment prompts are systematically biased (edge-avoiding, centroid-seeking, faster and sloppier over a session), and evaluating under the measured distribution reorders methods relative to protocol-prompt leaderboards.
**Why Important:** If method rankings flip under real prompts, the field is optimizing for the wrong input distribution.
**Why Possibly Novel:** Prompt distributions have never been treated as an empirically measured deployment condition with its own shift analysis.
**Minimal Experiment:** Log prompts from clinicians using an annotation tool on 200 cases; fit a prompt-distribution model; re-evaluate public models under protocol vs measured prompts; compare rankings.
**Main Risk:** Clinician logging requires IRB and partnerships; small-n prompt models may overfit individual users.

### IDEA-B-0071 — Upstream detector drift silently shifts the downstream segmenter's input distribution
**One-sentence idea:** Quantify how domain shift acting on an upstream fire/lesion detector changes the crop/prompt distribution fed to a downstream segmenter, and whether end-to-end adaptation beats stage-wise adaptation because of this coupling.
**Problem:** Pipelines adapt each stage independently, but the segmenter's effective input domain is defined by the detector's behavior, which itself drifts—an interaction invisible to stage-wise evaluation.
**Core Hypothesis:** Stage-wise adaptation leaves a measurable coupling residual (segmenter tuned for old detector outputs), and jointly adapting with detector-output replay closes it; the residual grows with detector drift magnitude.
**Why Important:** Almost all deployed segmentation runs behind detectors; the coupling term is an unmeasured, systematic loss.
**Why Possibly Novel:** Cross-stage distribution coupling under shift has not been isolated as a measurable quantity in vision pipelines.
**Minimal Experiment:** Build a two-stage pipeline; induce controlled detector drift; compare stage-wise vs joint adaptation; measure the coupling residual as their gap.
**Main Risk:** Results may depend on the detector-segmenter interface (boxes vs crops vs prompts).

### IDEA-B-0072 — Amplitude-only adaptation: testing the "shift is style" hypothesis with Fourier-space adapters
**One-sentence idea:** Constrain all trainable adaptation to a global Fourier amplitude filter and measure how much of various domain gaps this single interpretable component can close, upper-bounding the "style" content of each shift.
**Problem:** The folk claim that scanner/site shifts are mostly "style" has never been operationalized as a capacity-constrained, interpretable test.
**Core Hypothesis:** For scanner and site shifts, an amplitude-only adapter closes the majority of the gap, while for cross-modality or cross-anatomy shifts it closes little, yielding a quantitative style-fraction per shift type.
**Why Important:** Gives the field a standard, cheap diagnostic ("style fraction") to characterize any new domain pair before choosing adaptation machinery.
**Why Possibly Novel:** Fourier augmentation exists, but using an amplitude-only trainable bottleneck as a measurement instrument for shift decomposition is new.
**Minimal Experiment:** Train amplitude-filter-only adaptation across 6 shift pairs at matched budgets vs unrestricted LoRA; report gap-closure ratios as style fractions.
**Main Risk:** Amplitude filters may capture some semantic content via band-specific structures, blurring the interpretation.

### IDEA-B-0073 — Topology consistency as an unsupervised adaptation signal for tubular structures
**One-sentence idea:** Use violations of expected anatomical topology (vessel-tree connectivity, airway loops) as a label-free error signal for adapting segmenters to new domains where intensity-based self-training fails.
**Problem:** Self-training under shift reinforces its own intensity-driven mistakes; tubular anatomy offers a domain-invariant correctness criterion (connectivity) that current adaptation ignores.
**Core Hypothesis:** Optimizing a differentiable topology-consistency objective on unlabeled target data corrects a class of shift errors (breaks, spurious branches) that intensity-based pseudo-labeling cannot, with gains concentrated on connectivity metrics rather than raw IoU.
**Why Important:** Vessel/airway connectivity is the clinically consumed quantity; adaptation that restores it has direct utility even at constant IoU.
**Why Possibly Novel:** Topology as the adaptation objective (not just an evaluation metric or training regularizer with labels) is unexplored.
**Minimal Experiment:** Adapt a vessel segmenter across a scanner shift using persistent-homology-based consistency on unlabeled target volumes; compare connectivity metrics (Betti errors, centerline recall) vs self-training.
**Main Risk:** Topology losses are unstable to optimize and may fix connectivity by hallucinating vessels.

### IDEA-B-0074 — Path dependence of sequential multi-domain adaptation
**One-sentence idea:** Test whether the order of adapting through a sequence of domains (A→B→C vs A→C→B) materially changes final performance, and whether shift-distance-ordered curricula dominate arbitrary orders.
**Problem:** Real systems adapt through domains in the order data arrives, but nobody knows whether order matters or whether there is a principled ordering worth enforcing.
**Core Hypothesis:** Final performance is path-dependent beyond seed noise, and near-to-far ordering (by embedding distance) beats far-to-near, because early far jumps destroy reusable intermediate features.
**Why Important:** If ordering matters, deployment pipelines should buffer and reorder adaptation data—a cheap systems change with free gains.
**Why Possibly Novel:** Curriculum research addresses example ordering within one task; domain-sequence path dependence for foundation-model adaptation is unmeasured.
**Minimal Experiment:** Fix 4 domains; adapt through all 24 orderings (or a balanced subset) with matched budgets; test ordering effects statistically and against distance-based predictions.
**Main Risk:** Path effects may be small relative to per-domain budget effects.

### IDEA-B-0075 — Does SAM segment glass by its reflections? A reflection-swap diagnostic
**One-sentence idea:** Determine whether foundation segmenters localize transparent objects via boundary/refraction cues (domain-stable) or via reflected environmental content (domain-fragile), by swapping reflections between environments in controlled captures.
**Problem:** Transparent-object performance varies wildly across environments, and without knowing which cue the model uses, indoor-trained systems cannot be safely deployed outdoors.
**Core Hypothesis:** Segmentation quality tracks the familiarity of reflected content rather than the physical boundary cues—demonstrable when reflection-swapped objects (same glass, alien reflections) lose performance while boundary cues are held fixed.
**Why Important:** Identifies the true generalization bottleneck for transparent-object perception in robotics and AR, redirecting data collection toward reflection diversity.
**Why Possibly Novel:** Cue attribution via physical reflection manipulation (polarizing filters, environment swaps) has not been applied to segmentation models.
**Minimal Experiment:** Capture the same transparent objects under systematically varied reflection environments (or use paired renders); evaluate frozen models; regress IoU against reflection-environment familiarity vs boundary-contrast measures.
**Main Risk:** Physical captures are labor-intensive; render-based versions may miss real reflection statistics.

### IDEA-B-0076 — Federated adaptation by LoRA-delta averaging: when does weight-space aggregation work?
**One-sentence idea:** Characterize when averaging LoRA updates trained independently at multiple hospitals approximates centralized fine-tuning, and identify the data conditions (heterogeneity, rank, layer placement) under which averaging fails.
**Problem:** Privacy forbids pooling medical images, and federated averaging of full networks is heavy; LoRA-delta exchange is attractive but its aggregation behavior is theoretically and empirically uncharacterized for dense tasks.
**Core Hypothesis:** LoRA averaging matches centralized training when site data are shifted versions of a shared task (style heterogeneity) but fails sharply under label-convention heterogeneity, with the failure predictable from inter-site delta subspace angles.
**Why Important:** A practical recipe plus a failure predictor would unlock multi-site adaptation without data sharing—a top-3 blocker in medical AI.
**Why Possibly Novel:** Aggregation geometry of low-rank adapters (subspace alignment across sites) is a fresh analysis surface distinct from FedAvg theory.
**Minimal Experiment:** Simulate federated sites from multi-site datasets under controlled heterogeneity types; compare averaged-LoRA vs centralized vs per-site; correlate failure with measured subspace angles.
**Main Risk:** Real federated constraints (rounds, stragglers) add dynamics the simulation may miss.

### IDEA-B-0077 — The robustness-distillation gap: do efficient SAM variants inherit robustness or only accuracy?
**One-sentence idea:** Measure whether distilled/efficient segment-anything variants preserve the teacher's robustness to corruption and domain shift, or only its clean in-distribution accuracy, defining a "robustness-distillation gap."
**Problem:** Edge deployments adopt distilled variants based on clean-benchmark parity, implicitly assuming robustness parity that has never been verified.
**Core Hypothesis:** Distillation on in-distribution data transfers accuracy but systematically not robustness—the student's degradation slope under shift is steeper than the teacher's—and adding shifted unlabeled data to distillation closes a large fraction of the gap.
**Why Important:** Safety-relevant edge systems (fire cameras, portable ultrasound) run exactly these distilled models; a hidden robustness deficit is a deployment hazard.
**Why Possibly Novel:** Robustness as a distinct distillation target (and its measurement as a slope gap) is underexamined for dense prediction.
**Minimal Experiment:** Evaluate teacher and public distilled variants across corruption/shift ladders; compute degradation slopes; retrain distillation with shifted data to test the closure claim.
**Main Risk:** Public distilled models differ in more than distillation (architecture changes), requiring controlled re-distillation.

### IDEA-B-0078 — Language as a domain coordinate: text-described domains for zero-shot adaptation
**One-sentence idea:** Test whether natural-language descriptions of a target domain ("underwater, greenish turbidity, particulate backscatter") can condition a segmenter's adaptation—via text-derived feature modulation—without any target images.
**Problem:** Some deployment domains have no data at all before launch (new camera sites, rare modalities), leaving no adaptation signal except human knowledge of the domain.
**Core Hypothesis:** Domains occupy a partially language-describable manifold: text-conditioned modulation recovers a meaningful fraction of the gap that image-conditioned adaptation achieves, and the recoverable fraction correlates with how "describable" the shift is (style vs content).
**Why Important:** Would create a zero-data adaptation channel and quantify the overlap between linguistic and visual domain representations—a basic science question about VLM geometry.
**Why Possibly Novel:** Language-specified domain adaptation for dense prediction (not object classes, but domain conditions) is nearly untouched.
**Minimal Experiment:** Build text descriptions for 8 known shifts; condition modulation layers on text embeddings (trained on a disjoint set of described domains); evaluate zero-shot on held-out described domains vs undescribed baselines.
**Main Risk:** The method may learn generic robustness rather than description-specific adaptation; needs description-permutation controls.

### IDEA-B-0079 — Physics-derived versus search-derived augmentation for ultrasound generalization
**One-sentence idea:** Compare augmentation policies derived from ultrasound physics (speckle statistics, attenuation, beam geometry) against automatically searched augmentation policies, attributing generalization gains to specific error modes.
**Problem:** Augmentation for ultrasound is either borrowed from natural images or auto-searched; whether physical fidelity of augmentation matters—and for which error modes—is unresolved.
**Core Hypothesis:** Physics-derived augmentations improve robustness specifically on physics-mode errors (shadowing, reverberation artifacts) where searched policies plateau, while searched policies win on nuisance modes—implying complementary, attributable roles.
**Why Important:** Provides a principled recipe for the most operator-dependent, shift-prone modality in clinical use.
**Why Possibly Novel:** Error-mode-attributed augmentation comparison (not just mean IoU) with physically parameterized transforms is new for ultrasound segmentation.
**Minimal Experiment:** Implement calibrated physics augmentations; run policy search at matched compute; evaluate cross-device with error-mode-stratified metrics.
**Main Risk:** Physics augmentation fidelity depends on device parameters that public datasets do not document.

### IDEA-B-0080 — When does source data hurt? Locating the negative-transfer crossover
**One-sentence idea:** Map the crossover point where continued joint training with source (natural-image) data stops helping and starts hurting target-domain fine-tuning, as a function of target dataset size and domain distance.
**Problem:** Recipes disagree on whether to mix source data into fine-tuning; the disagreement likely reflects an unmeasured crossover that depends on target size and distance.
**Core Hypothesis:** Negative transfer begins when target sample count exceeds a threshold proportional to (domain distance)^-1, and the crossover is predictable from early-training gradient-conflict statistics between source and target batches.
**Why Important:** A predictive rule replaces per-project trial-and-error for a decision every fine-tuning effort makes.
**Why Possibly Novel:** Negative-transfer thresholds with a gradient-conflict predictor have not been established for dense prediction.
**Minimal Experiment:** Grid over target size × mixing ratio for 4 targets at varying distances; locate crossovers; validate the gradient-conflict predictor's forecasts on 2 held-out targets.
**Main Risk:** Crossover may depend on optimizer details, requiring recipe-stratified analysis.

---

## Cluster 3 — Evaluation Weakness / Calibration / Uncertainty / Robustness (IDEA-B-0081 … IDEA-B-0120)

### IDEA-B-0081 — Which segmentation metric predicts downstream clinical measurement error?
**One-sentence idea:** Determine empirically which mask metric (IoU, boundary F1, HD95, surface Dice) best predicts errors in the downstream clinical quantities actually consumed (volumes, diameters, growth rates), and expose where the standard metrics mispredict utility.
**Problem:** Papers optimize and rank by IoU/Dice, but clinicians consume derived measurements; the metric-to-utility mapping is assumed, not measured.
**Core Hypothesis:** For thin and small structures, boundary-localized metrics predict measurement error far better than region metrics, and metric-induced method rankings materially disagree with utility-induced rankings on at least some structure classes.
**Why Important:** If leaderboard metrics mispredict utility, the field's selection pressure is miscalibrated at the root.
**Why Possibly Novel:** Direct regression from mask metrics to downstream clinical measurement error across structure classes has not been systematically published.
**Minimal Experiment:** On datasets with GT masks, compute derived clinical measurements from predictions of many public models; regress measurement errors on mask metrics; compare rank orders.
**Main Risk:** Utility definitions vary by clinical task; conclusions must be stratified, not global.

### IDEA-B-0082 — A relabeling bootstrap for reporting rank stability under annotation noise
**One-sentence idea:** Introduce an evaluation procedure that resamples plausible test-set relabelings (from a fitted inter-rater noise model) and reports method rankings with rank-stability intervals instead of point estimates.
**Problem:** Benchmarks report point metrics against one arbitrary labeling; small method gaps are then over-interpreted despite being within annotation noise.
**Core Hypothesis:** Under realistic noise models fitted from multi-rater subsets, a substantial share of adjacent leaderboard pairs on popular segmentation benchmarks have unstable rankings (flip probability > 25%).
**Why Important:** Gives the community a practical instrument to distinguish real progress from noise-chasing, changing publication and comparison norms.
**Why Possibly Novel:** Bootstrap over label space (not just test-image resampling) is essentially absent from dense-prediction benchmarking.
**Minimal Experiment:** Fit boundary-noise models from multi-rater data on 2 benchmarks; resample 1,000 pseudo-labelings; recompute rankings of public checkpoints; report flip probabilities (measured, not invented).
**Main Risk:** Noise models fitted on subsets may not represent the full test distribution.

### IDEA-B-0083 — Prompt-protocol sensitivity: how much do medical-SAM rankings depend on the click recipe?
**One-sentence idea:** Quantify how method rankings among medical SAM variants change across published prompt protocols (center click, random-in-mask, box-with-jitter, iterative), and propose reporting a protocol-sensitivity index.
**Problem:** Each paper evaluates under its own prompt recipe; cross-paper comparisons implicitly assume protocol invariance that has never been verified.
**Core Hypothesis:** Rankings among top methods are materially protocol-dependent (rank correlations well below 1 across protocols), and some methods' claimed superiority exists only under their own protocol.
**Why Important:** A field-wide comparability problem with a cheap fix—standardized multi-protocol reporting—but only if the sensitivity is first demonstrated.
**Why Possibly Novel:** Prompt protocol as the manipulated variable in a meta-evaluation across public checkpoints has not been done at scale.
**Minimal Experiment:** Evaluate 8–10 public medical-SAM checkpoints under 5 protocols on 3 datasets; compute cross-protocol rank correlations and per-method protocol sensitivity.
**Main Risk:** Some checkpoints embed protocol assumptions in preprocessing, complicating fair evaluation.

### IDEA-B-0084 — Out-of-domain calibration of SAM's mask-quality head
**One-sentence idea:** Audit whether SAM's predicted-IoU head remains calibrated under domain shift, characterize its failure structure, and test whether a tiny recalibration head fitted on one shifted domain transfers to others.
**Problem:** Pipelines use SAM's self-reported mask quality to filter pseudo-labels and route human review, but its reliability outside natural images is unverified.
**Core Hypothesis:** The quality head systematically overestimates on out-of-domain inputs with an error that grows smoothly with shift magnitude and shares structure across domains—making a single lightweight recalibration broadly transferable.
**Why Important:** Every SAM-based auto-labeling and active-learning loop depends on this head; quantifying and fixing its OOD behavior hardens hundreds of pipelines.
**Why Possibly Novel:** The IoU-prediction head has escaped systematic calibration analysis despite being load-bearing infrastructure.
**Minimal Experiment:** Compare predicted vs actual IoU across 8 domains; fit shift-conditioned recalibration on 2 domains; test transfer to the other 6.
**Main Risk:** Head behavior may differ across SAM versions/scales, fragmenting the conclusions.

### IDEA-B-0085 — Hierarchical uncertainty: existence, extent, and boundary as separate quantities
**One-sentence idea:** Decompose segmentation uncertainty into structure-existence uncertainty, extent uncertainty, and boundary-localization uncertainty, and show the decomposition predicts different downstream actions than monolithic pixel-entropy maps.
**Problem:** Uncertainty is reported as a single per-pixel map, but a surgeon needs to know "is it there?" separately from "where exactly is its edge?"—questions with different costs and different remedies.
**Core Hypothesis:** The three uncertainty components are statistically separable (weakly correlated across cases), are best estimated by different mechanisms (prompt ensembles for existence, multimask spread for extent, boundary sampling for edges), and route review actions with higher utility than entropy maps.
**Why Important:** Makes uncertainty outputs actionable in clinical and safety workflows instead of decorative.
**Why Possibly Novel:** Task-structured uncertainty decomposition for promptable segmenters, validated against action utility, is new.
**Minimal Experiment:** Instrument the three estimators; measure inter-component correlation on 3 datasets; run a simulated review-routing study comparing utility per review minute.
**Main Risk:** Components may be entangled for small objects where existence and extent blur.

### IDEA-B-0086 — Estimating web-pretraining contamination of medical benchmarks
**One-sentence idea:** Apply membership-inference and near-duplicate retrieval to estimate how many images in popular medical segmentation test sets are plausibly present in web-scale pretraining corpora, and bound the contamination effect on zero-shot claims.
**Problem:** "Zero-shot" evaluations assume the model never saw the test data, but medical images circulate in papers, blogs, and teaching files that web scrapers ingest.
**Core Hypothesis:** A nonzero, quantifiable fraction of standard benchmark images have web-visible duplicates, and zero-shot performance on the contaminated subset is measurably higher than on verified-clean subsets.
**Why Important:** Protects the validity of the field's headline zero-shot claims and informs benchmark construction (release hygiene).
**Why Possibly Novel:** Contamination auditing is active for LLMs but essentially unpracticed for dense-prediction benchmarks.
**Minimal Experiment:** Reverse-image-search and embedding-retrieve benchmark images against web indices; partition test sets; compare zero-shot metrics between matched contaminated/clean strata (report measured splits only).
**Main Risk:** Web-visibility is a proxy—presence in a specific model's corpus cannot be confirmed without corpus access.

### IDEA-B-0087 — Do corruption, adversarial, and shift robustness measure the same thing for dense prediction?
**One-sentence idea:** Compute the empirical correlation structure among corruption robustness, adversarial robustness, and natural-shift robustness across many segmentation models to test whether "robustness" is one property or several.
**Problem:** Papers claim robustness after testing one axis; procurement and safety decisions then assume the other axes follow, without evidence for dense tasks.
**Core Hypothesis:** The three robustness axes are only weakly mutually predictive for segmentation (pairwise rank correlations modest), and the correlation is even lower for boundary metrics than region metrics.
**Why Important:** A single-axis robustness claim would be exposed as insufficient for safety cases, changing evaluation requirements.
**Why Possibly Novel:** Cross-axis robustness correlation studies exist for ImageNet classifiers but not for segmentation with boundary-sensitive metrics.
**Minimal Experiment:** Evaluate 20+ public segmentation models on the three axes with matched difficulty ladders; report the correlation matrix and its metric dependence.
**Main Risk:** Axis difficulty matching is nontrivial; poorly matched ladders could fabricate low correlations.

### IDEA-B-0088 — Target-absent evaluation as a first-class metric for rare-event segmentation
**One-sentence idea:** Establish false-positive behavior on verified target-absent imagery (no smoke, no lesion) as a primary reported metric, and measure how current fire/medical models rank when it is included.
**Problem:** Benchmarks are built from positives; a model can lead the leaderboard while hallucinating targets in empty scenes, which is the dominant failure in deployed monitoring.
**Core Hypothesis:** Per-positive metrics and target-absent FP rates are nearly uncorrelated across public models, and composite rankings differ sharply from current leaderboards.
**Why Important:** Aligns evaluation with the actual operating condition of rare-event systems, where negatives outnumber positives thousands-fold.
**Why Possibly Novel:** Absence-conditioned evaluation exists in detection, but standardized absent-set methodology for segmentation (area-based FP rates, scene stratification) does not.
**Minimal Experiment:** Curate absent sets for smoke and lesions with verified negativity; evaluate public models; publish the joint (positive-metric, FP-rate) frontier.
**Main Risk:** Verifying absence is itself an annotation problem (occult positives).

### IDEA-B-0089 — The oracle-prompt inflation factor in interactive segmentation reporting
**One-sentence idea:** Measure the gap between performance under ground-truth-derived prompts (standard practice) and prompts produced by real users seeing only the image, defining a reusable "oracle inflation factor" per task.
**Problem:** Benchmark prompts are computed from the GT mask (centroid, tight box), information a real user does not have; reported numbers therefore bound deployment performance from above by an unknown margin.
**Core Hypothesis:** The oracle inflation factor is large and task-dependent (worst for low-contrast and ambiguous-extent targets) and is itself predictable from target visibility statistics, enabling corrected reporting without user studies for every paper.
**Why Important:** Recalibrates the entire interactive-segmentation literature toward deployment-realistic expectations.
**Why Possibly Novel:** Systematic quantification of GT-derived-prompt bias across tasks, with a predictive correction model, is missing.
**Minimal Experiment:** Collect image-only prompts from users on 4 tasks; compute inflation factors; fit predictors from visibility features; validate on a held-out task.
**Main Risk:** User prompt quality varies with training and interface, adding variance to the factor.

### IDEA-B-0090 — Size-stratified re-ranking: does mean IoU hide small-structure regressions?
**One-sentence idea:** Re-evaluate public medical segmentation checkpoints with size-stratified metrics to test whether dataset-mean IoU systematically hides regressions on small structures, and whether stratified rankings disagree with published ones.
**Problem:** Mean metrics are dominated by large organs and large lesions; a method can win the mean while being worse on precisely the small structures with the most clinical stakes.
**Core Hypothesis:** Among top public checkpoints, stratified small-structure rankings disagree with mean-metric rankings for a substantial fraction of method pairs, and some celebrated improvements are large-structure-only.
**Why Important:** Costless change to reporting practice with direct clinical relevance, justified by measured (not assumed) disagreement.
**Why Possibly Novel:** Stratified re-audits of published checkpoint families, framed as a meta-evaluation with statistical tests, are rare.
**Minimal Experiment:** Download 10+ checkpoints across 2 benchmark families; compute size-stratified metrics; report rank disagreement statistics (measured only).
**Main Risk:** Some checkpoints are not reproducible as published, limiting the audit's coverage.

### IDEA-B-0091 — Prompt ensembles versus weight ensembles versus MC-dropout: the uncertainty-compute frontier
**One-sentence idea:** Benchmark uncertainty estimators unique to promptable models (prompt-perturbation ensembles) against classical weight-space ensembles and MC-dropout on error-prediction quality per unit compute.
**Problem:** Prompted segmenters offer a free ensemble axis (perturbing prompts) whose uncertainty quality relative to expensive classical methods is unknown.
**Core Hypothesis:** Prompt-ensemble uncertainty matches weight-ensemble error-correlation for boundary errors at a fraction of the compute, but underestimates existence-level (whole-structure) errors, defining complementary regimes.
**Why Important:** Establishes the cheapest adequate uncertainty method per error type—critical for real-time and edge deployments.
**Why Possibly Novel:** The prompt axis as an uncertainty source has not been benchmarked head-to-head with established estimators.
**Minimal Experiment:** On 3 datasets, compute error-prediction AUROC (pixel and structure level) for each estimator across compute budgets; plot the frontier.
**Main Risk:** Prompt-perturbation design choices (jitter scale) may dominate results, requiring careful sensitivity analysis.

### IDEA-B-0092 — Conformal boundary bands for promptable segmentation
**One-sentence idea:** Construct distribution-free conformal prediction bands around predicted mask boundaries and test whether prompt-conditioning violates the exchangeability assumptions that conformal guarantees require.
**Problem:** Safety cases want guaranteed coverage ("the true boundary lies within this band with 90% probability"), but conformal theory assumes exchangeable inputs, and user-chosen prompts plausibly break this.
**Core Hypothesis:** Naive conformal bands undercover when prompts are user-generated (prompt selection correlates with difficulty), and prompt-stratified or prompt-conditional conformal calibration restores coverage at acceptable band widths.
**Why Important:** Brings the first distribution-free guarantees to interactive segmentation, a prerequisite for regulated use.
**Why Possibly Novel:** Conformal methods for masks exist in early forms; the prompt-induced exchangeability violation and its correction are unexamined.
**Minimal Experiment:** Calibrate boundary-distance conformal scores on held-out data; evaluate coverage under protocol prompts vs logged user prompts; test stratified calibration.
**Main Risk:** Bands may be too wide to be useful for thin structures.

### IDEA-B-0093 — Best-of-N reporting hides the selection problem: auditing multimask choice
**One-sentence idea:** Separate the quality of SAM-style multimask candidate sets from the quality of the selection mechanism, measuring how much reported performance depends on oracle best-of-N choice versus the model's own ranking.
**Problem:** Ambiguity-aware models output several candidates and papers often score the best one, silently attributing oracle selection ability to the model.
**Core Hypothesis:** The gap between oracle-selected and self-selected candidates is large and domain-dependent (largest under shift), meaning candidate generation has outpaced selection and the selection head is the binding constraint out of domain.
**Why Important:** Redirects research investment to the neglected component and cleans up inflated comparisons.
**Why Possibly Novel:** Generation-vs-selection decomposition with domain-shift interaction has not been reported for multimask segmenters.
**Minimal Experiment:** Evaluate public multimask models in-domain and shifted, scoring {oracle, self-ranked, random} selection; report decomposed gaps.
**Main Risk:** Few model families expose calibrated candidate scores, limiting breadth.

### IDEA-B-0094 — Temporal stability as a first-class metric: does optimizing IoU degrade flicker?
**One-sentence idea:** Define and validate a temporal-stability metric for video segmentation of dynamic targets (fire, smoke) and test whether frame-wise-IoU-optimized models systematically flicker more than slightly-lower-IoU alternatives.
**Problem:** Deployment failures in monitoring are often flicker-driven (alarms toggling), yet evaluation is frame-independent, so the property is invisible and possibly anti-correlated with what we optimize.
**Core Hypothesis:** Across public and retrained models, frame-IoU and temporal stability trade off in a measurable frontier, and small IoU sacrifices buy large stability gains that improve event-level alarm metrics.
**Why Important:** Aligns video-segmentation research with the event-level quantities that operators actually consume.
**Why Possibly Novel:** Stability metrics exist in video segmentation, but the IoU-stability tradeoff and its alarm-level consequences for safety monitoring are unquantified.
**Minimal Experiment:** Score models on frame IoU, flicker rate, and simulated alarm precision/recall; map the frontier; test whether temporal smoothing moves along or off it.
**Main Risk:** Ground-truth temporal consistency itself is imperfect in video datasets.

### IDEA-B-0095 — Worst-case-prompt robustness: a certification perspective on interactive segmentation
**One-sentence idea:** Define robustness as worst-case mask degradation over the set of valid prompts (all clicks inside the target), compute it empirically and with certified bounds for small prompt sets, and compare models on this axis.
**Problem:** Average-prompt evaluation hides catastrophic sensitivity: two valid clicks millimeters apart can yield wildly different masks, which is unacceptable in clinical interaction.
**Core Hypothesis:** Models with similar average performance differ severely in worst-case prompt robustness, and a certified inner region (prompt subsets guaranteeing stable output) can be computed and enlarged by training-time prompt smoothing.
**Why Important:** Worst-case interaction behavior determines user trust and safety; certification brings formal-methods rigor to interactivity.
**Why Possibly Novel:** Certified robustness has addressed input perturbations, never the prompt space of interactive segmenters.
**Minimal Experiment:** Grid/adversarially search prompt space per target for multiple models; report worst-case vs average gaps; prototype certification via Lipschitz bounds on the prompt encoder for restricted prompt sets.
**Main Risk:** Certified bounds may be too loose to be nontrivial for realistic decoders.

### IDEA-B-0096 — Class-conditional calibration for extremely imbalanced dense prediction
**One-sentence idea:** Show that standard expected calibration error on imbalanced segmentation is dominated by background pixels, and develop class- and size-conditional calibration metrics that expose clinically relevant miscalibration hidden by ECE.
**Problem:** A lesion model can be badly miscalibrated on lesion pixels while posting excellent overall ECE, because background swamps the average.
**Core Hypothesis:** Class-conditional calibration on rare-class pixels is largely uncorrelated with overall ECE across models, and threshold-transfer failures observed in deployment are predicted by the former, not the latter.
**Why Important:** Calibration reporting guides threshold choices in practice; the wrong summary statistic causes real clinical threshold errors.
**Why Possibly Novel:** Conditional calibration is known in fairness contexts; its necessity and structure for imbalanced dense prediction have not been established.
**Minimal Experiment:** Evaluate many checkpoints with overall vs conditional calibration; correlate each with cross-site threshold-transfer error; report which predicts deployment behavior.
**Main Risk:** Conditional metrics on rare pixels are high-variance, needing large test sets.

### IDEA-B-0097 — Benchmark replication: measuring overfitting-to-the-test-set in medical SAM research
**One-sentence idea:** Collect a replication test set for a popular medical segmentation benchmark (new images, same acquisition and annotation protocol) and measure the population-level gap between original-test and replication-test performance across published methods.
**Problem:** Years of adaptive method development against a fixed test set plausibly overfits the community to its idiosyncrasies, but medical segmentation lacks the replication studies done for ImageNet/CIFAR.
**Core Hypothesis:** Methods lose performance on the replication set with losses proportional to their original-test ranking recency (later methods overfit more), and relative rankings partially reorder.
**Why Important:** Quantifies how much of recent "progress" is benchmark-specific adaptation—foundational knowledge for the field's epistemics.
**Why Possibly Novel:** Replication-set methodology has not been applied to medical dense prediction.
**Minimal Experiment:** Partner with a data-holding site to release a protocol-matched replication set; evaluate the public checkpoint population; report gap-vs-publication-date regressions (measured values only).
**Main Risk:** Protocol matching is hard; acquisition drift could masquerade as overfitting.

### IDEA-B-0098 — Can a lightweight verifier predict segmentation failure better than the model itself?
**One-sentence idea:** Train small independent verifier networks that predict a frozen segmenter's per-case failure (IoU below threshold) from the image and predicted mask, and benchmark them against the model's own confidence outputs.
**Problem:** Silent failure is the key deployment risk; self-reported confidence is entangled with the very representations that caused the failure.
**Core Hypothesis:** An independent verifier trained on diverse failure examples detects out-of-domain failures with substantially higher AUROC than self-confidence, because it can key on inconsistency cues (mask-image disagreement) the primary model is blind to.
**Why Important:** A reliable external failure detector is the missing component for autonomous labeling and clinical triage pipelines.
**Why Possibly Novel:** Verifier-vs-self-confidence comparisons are established in LLM research but not systematized for dense prediction.
**Minimal Experiment:** Build failure datasets across 6 domains; train verifiers with held-out-domain evaluation; compare AUROC/AUPR vs self-confidence and ensembles.
**Main Risk:** Verifiers may overfit the primary model's specific failure styles and miss novel ones.

### IDEA-B-0099 — Distribution-valued ground truth for amorphous classes
**One-sentence idea:** Replace single-mask ground truth with distribution-valued references (soft density or rater distributions) for smoke/haze evaluation, and test whether metric choice against distributions changes training conclusions reached with hard IoU.
**Problem:** For boundary-undefined classes, hard-mask metrics inject an arbitrary threshold into the ground truth itself, potentially inverting method comparisons.
**Core Hypothesis:** Method rankings under distributional metrics (soft IoU, Wasserstein on density) disagree with hard-IoU rankings for amorphous classes, and the distributional rankings better predict downstream quantitative use (opacity estimation, dispersion modeling).
**Why Important:** Establishes evaluation foundations for an entire class of scientifically important "stuff" targets.
**Why Possibly Novel:** Distributional GT is used in crowd counting; porting the paradigm with validation against downstream physical quantities is new for smoke/haze segmentation.
**Minimal Experiment:** Build distribution-valued references from multi-rater or matting data; evaluate models under both metric families; test which predicts opacity-estimation error.
**Main Risk:** Distribution-valued references are expensive; proxies may be contested.

### IDEA-B-0100 — Codec robustness curves: how compression interacts with amorphous-target segmentation
**One-sentence idea:** Characterize segmentation degradation as a function of video codec, bitrate, and content type for field-deployed smoke/fire cameras, and test whether compression augmentation at train time flattens the curves.
**Problem:** Monitoring cameras stream heavily compressed video, and compression artifacts (blocking, temporal smearing) plausibly interact worst with low-contrast amorphous targets—yet models are developed on pristine data.
**Core Hypothesis:** Smoke segmentation degrades disproportionately versus solid-object segmentation under equal bitrate reduction (compression removes exactly the low-contrast texture that identifies smoke), and matched-codec augmentation recovers most but not all of the loss.
**Why Important:** Bitrate decisions and model training are made by different teams; a quantitative curve enables joint optimization of a real deployed system.
**Why Possibly Novel:** Codec-parameterized robustness analysis specific to amorphous classes has not been published.
**Minimal Experiment:** Re-encode labeled smoke video across codec/bitrate grids; evaluate frozen and augmented-trained models; compare degradation slopes vs solid-object controls.
**Main Risk:** Codec implementations differ across hardware, adding a deployment-matching burden.

### IDEA-B-0101 — Abstention granularity: per-pixel versus per-structure versus per-image rejection
**One-sentence idea:** Compare selective-prediction schemes for segmentation at three abstention granularities, measuring which risk-coverage tradeoff clinicians and operators can actually consume.
**Problem:** Selective prediction research optimizes pixel-level risk-coverage curves, but a workflow cannot act on scattered rejected pixels—the usable rejection unit is a structure or an image.
**Core Hypothesis:** Aggregating pixel uncertainty to structure-level abstention sacrifices little theoretical risk-coverage while multiplying downstream utility (measured via simulated review workflows), and the optimal aggregation rule differs by structure size.
**Why Important:** Bridges the gap between selective-prediction theory and clinical/monitoring practice.
**Why Possibly Novel:** Granularity of abstention as the primary design variable, evaluated with workflow simulations, is unstudied.
**Minimal Experiment:** Implement the three granularities atop identical uncertainty maps; run simulated review pipelines with cost models; report utility per review minute.
**Main Risk:** Workflow simulations may not capture real reviewer behavior; needs a small human validation.

### IDEA-B-0102 — Targeted relabeling of high-disagreement pixels: a rank-stability stress test
**One-sentence idea:** Identify the test-set pixels where top public models maximally disagree, have experts relabel only those regions, and measure how method rankings change under the corrected labels.
**Problem:** Full test-set relabeling is unaffordable, but model-disagreement pixels concentrate exactly where annotation errors and genuine method differences coexist—an efficient audit surface.
**Core Hypothesis:** A small fraction of relabeled pixels (<5% of foreground) changes a disproportionate share of pairwise method-ranking outcomes, and disagreement-targeted relabeling is severalfold more rank-informative per annotation minute than random relabeling.
**Why Important:** Provides an affordable, reusable protocol for auditing any benchmark's label-limited conclusions.
**Why Possibly Novel:** Disagreement-targeted label auditing as a formal evaluation methodology (with efficiency guarantees) is new.
**Minimal Experiment:** On one benchmark, compute model-disagreement maps from 10 checkpoints; relabel top-disagreement regions with 3 experts; recompute rankings; compare information gain vs random-region relabeling.
**Main Risk:** Disagreement regions may be genuinely ambiguous, where "correction" is ill-defined.
### IDEA-B-0103 — How does box uncertainty propagate into mask uncertainty?
**One-sentence idea:** Derive and empirically validate the transfer function from upstream detector localization uncertainty to downstream prompted-mask uncertainty, enabling analytic pipeline-level error budgets.
**Problem:** Detection-then-segment pipelines report component metrics, but system designers cannot predict end-to-end mask reliability from detector reliability because the propagation law is unknown.
**Core Hypothesis:** Mask IoU as a function of box perturbation is locally smooth with target-geometry-dependent sensitivity (high for thin/concave targets), so a second-order propagation model predicts end-to-end uncertainty within useful tolerances without Monte Carlo at deployment.
**Why Important:** Analytic error budgets let engineers allocate accuracy requirements across pipeline stages rationally, as in classical metrology.
**Why Possibly Novel:** Uncertainty propagation theory has not been developed for prompt-conditioned neural pipelines.
**Minimal Experiment:** Measure mask-vs-box-jitter response surfaces across target geometries; fit propagation models; validate predictions against full Monte Carlo on held-out categories.
**Main Risk:** Decoder nonlinearity (mode switching between candidate masks) may break smoothness assumptions.

### IDEA-B-0104 — Wrong-prompt behavior: does SAM fail loudly or silently under semantic prompt errors?
**One-sentence idea:** Characterize what promptable segmenters output when prompts are semantically wrong (clicked on the wrong organ, box around the wrong object), and whether any internal signal flags the mismatch.
**Problem:** Real users make semantic errors, and a model that returns a confident well-formed mask of the wrong structure is more dangerous than one that visibly fails.
**Core Hypothesis:** Under wrong-target prompts, output confidence and mask-quality predictions remain high (silent failure) because the decoder's job is conditional delineation, and detecting the mismatch requires an external image-mask-intent consistency signal, which a small auxiliary model can supply.
**Why Important:** Defines and measures a safety property (loud vs silent failure) that interactive systems should be required to report.
**Why Possibly Novel:** Prompt-error robustness has not been formalized; all evaluations assume prompts are semantically correct.
**Minimal Experiment:** Build wrong-prompt test suites (systematically misplaced prompts with known intent labels); measure output confidence distributions; train and evaluate a mismatch detector.
**Main Risk:** "Intent" ground truth requires task context that pure benchmarks lack.

### IDEA-B-0105 — Statistical power auditing for segmentation method comparisons
**One-sentence idea:** Build a power-analysis toolkit for dense-prediction experiments (accounting for pixel correlation, per-image clustering, and metric variance) and audit what effect sizes typical published experimental designs can actually detect.
**Problem:** Segmentation papers compare methods on n≈100–500 images without power analysis; correlated pixels make effective sample sizes far smaller than they appear, so many reported differences are statistically uninterpretable.
**Core Hypothesis:** Under realistic variance and clustering estimates, common experimental designs cannot detect the 0.5–1.0 point differences they routinely report as findings, and a released toolkit changes what reviewers require.
**Why Important:** Basic statistical hygiene for a field whose comparisons drive clinical and industrial adoption.
**Why Possibly Novel:** Power analysis is standard in biostatistics but absent as a practiced norm and tooling in segmentation research.
**Minimal Experiment:** Estimate variance components from public benchmarks; compute minimum detectable effects for typical designs; validate with seed-replication experiments on 3 methods.
**Main Risk:** Adoption is cultural, not technical; the science is straightforward but the impact depends on uptake.

### IDEA-B-0106 — Complementary-metric gaming: do methods trade HD95 against IoU systematically?
**One-sentence idea:** Audit whether segmentation methods occupy systematically different positions on the IoU-versus-boundary-distance frontier—implying that single-metric leaderboards reward opposite biases—and detect training-recipe signatures (dilation bias) that game one metric.
**Problem:** IoU rewards slight over-segmentation of large objects while HD95 punishes outlier boundary errors; methods may win one metric by design choices that damage the other, invisible in single-metric reporting.
**Core Hypothesis:** Public checkpoints show signed boundary-offset signatures aligned with the metric emphasized in their original evaluation, and re-ranking under the complementary metric flips a meaningful share of comparisons.
**Why Important:** Reveals metric-driven selection effects shaping the literature and motivates mandatory frontier reporting.
**Why Possibly Novel:** Signed-bias signatures as evidence of metric-directed optimization have not been systematically measured.
**Minimal Experiment:** Measure signed boundary offsets and dual-metric positions for 20+ checkpoints; correlate bias direction with each paper's headline metric (measured associations only).
**Main Risk:** Bias signatures may stem from datasets rather than metric optimization; needs dataset-matched comparisons.

### IDEA-B-0107 — Modality-specific miscalibration in text-versus-visual prompted segmentation
**One-sentence idea:** Test whether text-prompted and visually-prompted segmentation from the same model are miscalibrated in different directions and magnitudes, requiring modality-specific confidence calibration.
**Problem:** Unified promptable models emit one confidence scale across prompt modalities, but text conditioning (semantic, distribution-mismatched) and visual conditioning (spatial, in-distribution) plausibly induce different confidence-accuracy relationships.
**Core Hypothesis:** At matched accuracy, text-prompted outputs are systematically more overconfident than point-prompted outputs, and a single temperature cannot calibrate both—modality-conditional calibration measurably improves selective-prediction utility.
**Why Important:** Multimodal prompting is becoming the default interface; per-modality confidence semantics are needed for any downstream thresholding.
**Why Possibly Novel:** Prompt-modality-conditional calibration has not been identified or measured as a phenomenon.
**Minimal Experiment:** Evaluate a text+visual promptable model on shared targets under both modalities; fit joint vs modality-conditional calibrations; compare reliability and risk-coverage curves.
**Main Risk:** Confounding between prompt modality and target difficulty (users choose text for different targets than clicks).

### IDEA-B-0108 — Honest zero-shot: quantifying hidden adaptation through validation-set prompt search
**One-sentence idea:** Measure how much of reported "zero-shot" segmentation performance is attributable to prompt-template and hyperparameter search on validation data from the target distribution, establishing corrected zero-shot bounds.
**Problem:** Papers tune prompt templates, thresholds, and post-processing on target-domain validation splits and still call the result zero-shot, conflating adaptation-free capability with search-based adaptation.
**Core Hypothesis:** Validation-informed prompt/hyperparameter search accounts for a substantial fraction of claimed zero-shot performance, and truly search-free evaluation (fixed universal settings) reorders zero-shot leaderboards.
**Why Important:** Zero-shot claims drive expectations about deployment without target data; inflated claims cause real planning failures.
**Why Possibly Novel:** The prompt-search contribution to zero-shot numbers has not been isolated and quantified across methods.
**Minimal Experiment:** Re-evaluate public zero-shot pipelines under (a) their published settings and (b) frozen universal settings chosen on disjoint domains; report the gap distribution.
**Main Risk:** Defining fair universal settings requires care to avoid disadvantaging any method family.

### IDEA-B-0109 — Train-test interaction of prompt modality mixing
**One-sentence idea:** Measure the interaction between prompt-modality mixing at training time and at test time (e.g., point+text jointly), testing whether mixed-modality inference helps only when training mixed, and whether modality synergy or interference dominates.
**Problem:** Multimodal prompting is deployed compositionally (users combine clicks and text) but models are mostly trained on single modalities per sample; the composition behavior is uncharacterized.
**Core Hypothesis:** For single-modality-trained models, adding a second prompt modality at test time degrades performance on ambiguous targets (conflicting conditioning), while mixed-trained models show super-additive gains precisely on those targets.
**Why Important:** Determines whether interface designers can freely combine prompt modalities or must respect training conventions.
**Why Possibly Novel:** The train-test factorial for prompt-modality composition has not been run.
**Minimal Experiment:** Train matched models under single vs mixed prompt regimes; evaluate the full test-modality grid; analyze the interaction term on ambiguity-stratified targets.
**Main Risk:** Requires training multimodal promptable models from scratch or heavy fine-tuning—nontrivial compute.

### IDEA-B-0110 — Efficient false-positive-rate estimation for rare-event monitoring via importance-sampled negatives
**One-sentence idea:** Develop and validate an importance-sampling estimator for extremely low false-positive rates (FP/day) of fire/smoke systems, replacing infeasible exhaustive negative evaluation with stratified sampling over scene-condition space.
**Problem:** Deployment requires certifying FP rates on the order of one per camera-week, but test sets contain thousands—not billions—of negative frames, so reported FP rates are statistically meaningless at the certification scale.
**Core Hypothesis:** Negative-frame risk is concentrated in identifiable strata (sunsets, fog banks, steam, headlights), and stratified importance sampling with learned proposal distributions estimates deployment FP rates with orders-of-magnitude fewer labeled negatives than uniform sampling, validated against long-duration field logs.
**Why Important:** Makes rare-event performance claims certifiable—the difference between a demo and a deployable safety system.
**Why Possibly Novel:** Importance sampling for rare-event evaluation is standard in reliability engineering but unadapted to learned-vision FP certification.
**Minimal Experiment:** Fit condition-strata proposals from unlabeled field video; run stratified evaluation; compare estimator variance and bias against exhaustive counts on a fully labeled long-duration subset.
**Main Risk:** Unmodeled risk strata (unknown unknowns) escape the proposal distribution.

### IDEA-B-0111 — Do uncertainty visualizations change expert correction behavior?
**One-sentence idea:** Run a controlled human-factors study measuring whether displaying model uncertainty maps changes where and how efficiently clinicians correct segmentation outputs, and whether the change improves final mask quality.
**Problem:** Uncertainty visualization is assumed useful for human-AI collaboration, but there is little controlled evidence that it changes expert behavior beneficially for dense editing tasks.
**Core Hypothesis:** Uncertainty display redirects correction effort toward high-uncertainty regions, reducing time-to-quality when uncertainty is well-calibrated but actively harming it when miscalibrated—making calibration a prerequisite, not an accessory, for uncertainty UX.
**Why Important:** Grounds a widely assumed workflow benefit in measurement, and links the calibration literature to interface design with a causal chain.
**Why Possibly Novel:** Calibration-quality × visualization factorial studies for dense-prediction editing are essentially absent.
**Minimal Experiment:** Within-subject study (n≈12 experts) editing masks under {no map, calibrated map, miscalibrated map}; measure gaze/edit allocation, time-to-quality, and final metrics.
**Main Risk:** Expert recruitment; learning effects across conditions require careful counterbalancing.

### IDEA-B-0112 — Intervention tests for claimed aleatoric-epistemic disentanglement in dense prediction
**One-sentence idea:** Stress-test methods that claim to separate aleatoric from epistemic uncertainty in segmentation by applying causal interventions—injecting label noise (should raise aleatoric only) and shrinking training data (should raise epistemic only)—and scoring specificity.
**Problem:** Disentanglement claims are validated by plausibility arguments; if the components respond to the wrong interventions, downstream uses (active learning uses epistemic, quality control uses aleatoric) are built on sand.
**Core Hypothesis:** Several popular disentanglement estimators fail intervention specificity for dense prediction—both components respond to both interventions—and the failure is worst near boundaries where the two sources genuinely mix.
**Why Important:** Provides the field a falsification standard for uncertainty semantics rather than accepting labels at face value.
**Why Possibly Novel:** Systematic interventional validation of uncertainty decompositions has not been performed for segmentation.
**Minimal Experiment:** Train across a noise-level × data-size grid; measure each estimator's component responses; report specificity matrices per method.
**Main Risk:** Interventions themselves interact (less data amplifies noise effects), complicating clean attribution.

### IDEA-B-0113 — When does augmentation-consistency stop being a valid proxy metric?
**One-sentence idea:** Characterize the conditions under which unsupervised consistency-under-augmentation scores diverge from true segmentation accuracy, mapping the validity boundary of the most popular label-free evaluation proxy.
**Problem:** Label-free model selection and monitoring increasingly rely on prediction consistency across augmentations, but a model can be consistently wrong—and the regimes where the proxy misleads are unmapped.
**Core Hypothesis:** Proxy validity degrades systematically with domain shift magnitude and with shortcut reliance (consistent shortcuts inflate the proxy), and a bias-corrected variant using disagreement-with-weak-model restores ranking validity in most divergent regimes.
**Why Important:** Deployment monitoring needs trustworthy label-free signals; knowing where the standard proxy lies is as valuable as the proxy itself.
**Why Possibly Novel:** The proxy's failure conditions have not been adversarially characterized for dense prediction.
**Minimal Experiment:** Across checkpoints and shifted datasets with hidden labels, correlate proxy vs true metrics; identify divergence regimes; test the corrected variant.
**Main Risk:** Divergence regimes may be dataset-idiosyncratic, limiting general maps.

### IDEA-B-0114 — Seed variance of PEFT fine-tuning versus reported effect sizes
**One-sentence idea:** Measure the cross-seed variance of LoRA/adapter fine-tuning results for segmentation and compare it against the effect sizes typically reported when proposing new PEFT variants.
**Problem:** PEFT papers report single-seed comparisons on small medical datasets; if seed variance rivals reported gaps, much of the PEFT-variant literature is statistically unsupported.
**Core Hypothesis:** Cross-seed standard deviation of standard PEFT fine-tuning on small dense-prediction datasets is of comparable magnitude to typical claimed inter-method differences, and variance grows as dataset size shrinks—exactly where most comparisons are made.
**Why Important:** Establishes reporting standards (seed counts, confidence intervals) calibrated to measured variance for the fastest-growing adaptation literature.
**Why Possibly Novel:** Seed-variance audits exist for RL and NLP; the dense-prediction PEFT version, stratified by dataset size, is missing.
**Minimal Experiment:** Run 10 seeds × 4 PEFT methods × 4 dataset sizes; publish variance components and minimum detectable effects (measured values only).
**Main Risk:** Compute cost of the full grid; may need factorial subsampling.

### IDEA-B-0115 — Does model uncertainty spatially align with human rater disagreement?
**One-sentence idea:** Evaluate uncertainty estimators by their spatial correlation with independent multi-rater disagreement maps, proposing alignment-with-humans as a stricter calibration criterion than error prediction.
**Problem:** Uncertainty is validated against model error, but for ambiguous boundaries the gold standard is the distribution of expert opinion—an estimator could predict errors well while misrepresenting genuine ambiguity structure.
**Core Hypothesis:** Estimators differ sharply in rater-alignment even when matched on error-prediction AUROC, and rater-aligned uncertainty transfers better to new datasets because it captures task-intrinsic ambiguity rather than model-specific weakness.
**Why Important:** Defines what uncertainty should mean for ambiguous medical boundaries and gives a benchmarkable criterion.
**Why Possibly Novel:** Rater-disagreement alignment as a primary uncertainty benchmark (not an anecdotal visualization) is new.
**Minimal Experiment:** On multi-rater datasets, compute spatial correlation between each estimator's maps and rater-variance maps; test cross-dataset transfer of high- vs low-alignment estimators.
**Main Risk:** Multi-rater data scarcity restricts breadth.

### IDEA-B-0116 — Clicks-to-quality curves versus one-shot metrics: do they rank models differently?
**One-sentence idea:** Compare interactive-efficiency rankings (clicks needed to reach target quality) against single-prompt rankings across promptable models, testing whether the field's one-shot leaderboards mispredict interactive value.
**Problem:** Deployment value of interactive models lies in the full correction loop, but evaluation convention is one prompt, one score—models optimized for the first click may respond poorly to corrections.
**Core Hypothesis:** One-shot and clicks-to-quality rankings disagree substantially, with some models exhibiting "correction resistance" (flat click-response curves) invisible in one-shot metrics, and correction responsiveness is a distinct, trainable property.
**Why Important:** Aligns model selection with actual interactive workflows in annotation and clinical use.
**Why Possibly Novel:** Correction responsiveness as a separable model property with its own ranking has not been established.
**Minimal Experiment:** Simulate standardized correction policies on 8 models across 3 datasets; compare ranking pairs; measure per-model click-response slopes.
**Main Risk:** Simulated correction policies may diverge from human correction styles.

### IDEA-B-0117 — Threshold-sweep evaluation: are method differences mostly threshold artifacts?
**One-sentence idea:** Re-evaluate segmentation comparisons across the full binarization-threshold sweep (area under the IoU-threshold curve) to test how many reported method differences reduce to different optimal operating points rather than different capability.
**Problem:** Masks are binarized at 0.5 by convention; two models with identical probabilistic outputs but shifted calibration can differ sharply at 0.5, contaminating comparisons with a nuisance parameter.
**Core Hypothesis:** A measurable fraction of published pairwise differences shrink to insignificance under threshold-sweep metrics, and reporting single-threshold results without sweeps systematically favors models whose calibration matches the benchmark's implicit prevalence.
**Why Important:** A cheap change to evaluation practice that removes a known nuisance from the field's comparisons.
**Why Possibly Novel:** Threshold sensitivity is understood for classifiers; a quantified audit of its contamination of segmentation leaderboards is missing.
**Minimal Experiment:** Recompute sweep metrics for 15 public checkpoints on 3 benchmarks; compare single-threshold vs sweep-based gap distributions.
**Main Risk:** Some pipelines output hard masks only, excluding them from sweep analysis.

### IDEA-B-0118 — Is any single benchmark representative? Measuring benchmark-to-aggregate predictivity
**One-sentence idea:** Quantify how well performance on each individual medical segmentation benchmark predicts a model's aggregate performance across a broad basket, identifying which benchmarks are informative and which are idiosyncratic.
**Problem:** Method claims rest on 1–3 benchmarks chosen by the authors; without knowing each benchmark's predictivity, readers cannot tell general progress from benchmark-specific fitting.
**Core Hypothesis:** Benchmarks differ widely in aggregate-predictivity, an efficient small subset predicts the aggregate nearly as well as the full basket, and predictivity is explained by measurable dataset properties (size, modality diversity, annotation quality).
**Why Important:** Rationalizes evaluation budgets and defines an evidence-based minimal benchmark suite for the community.
**Why Possibly Novel:** Benchmark-predictivity analysis (standard in psychometrics as item analysis) has not been applied to segmentation suites.
**Minimal Experiment:** Evaluate 20+ models on 12+ benchmarks; compute leave-one-out predictivity per benchmark; regress predictivity on dataset properties.
**Main Risk:** The model population sampled may bias predictivity estimates.

### IDEA-B-0119 — Modality-plausible corruption benchmarks: does ImageNet-C robustness transfer?
**One-sentence idea:** Construct corruption suites from physically plausible medical acquisition errors (motion, metal artifact, bias field, dose reduction) and test whether robustness to standard synthetic corruptions predicts robustness to modality-plausible ones.
**Problem:** Robustness certification for medical models borrows ImageNet-C-style corruptions (snow, JPEG) that never occur in scanners, while real acquisition artifacts go untested.
**Core Hypothesis:** Cross-corruption-suite robustness correlation is weak—models robust to generic corruptions are not reliably robust to acquisition physics artifacts—because the artifact structure (correlated, structured, anatomy-dependent) differs fundamentally from i.i.d. pixel corruptions.
**Why Important:** Regulatory and procurement robustness claims should be grounded in corruptions that actually occur; the transfer question determines whether existing audits mean anything.
**Why Possibly Novel:** Physics-grounded corruption benchmarking with a transfer analysis against generic suites has not been systematized for segmentation.
**Minimal Experiment:** Implement calibrated acquisition-artifact simulators for CT/MRI; evaluate public models on both suites; report cross-suite rank correlations.
**Main Risk:** Artifact simulators must be validated against real artifact examples to be credible.

### IDEA-B-0120 — Are SAM's multimask candidates a valid uncertainty sample?
**One-sentence idea:** Test whether the spread among SAM's multiple mask candidates behaves like a statistically valid uncertainty sample—whether candidate variance bounds true error—or whether the candidates are a biased, collapsed representation of the true posterior.
**Problem:** Practitioners increasingly treat multimask outputs as free uncertainty, but the candidates were trained for ambiguity coverage, not posterior fidelity, and their statistical semantics are unknown.
**Core Hypothesis:** Candidate spread underestimates true uncertainty out of domain (candidates collapse toward similar solutions precisely when the model is most wrong), failing coverage tests exactly where uncertainty matters most, while remaining approximately valid in-domain.
**Why Important:** Either certifies a free uncertainty mechanism for thousands of users or documents its unsafe failure mode.
**Why Possibly Novel:** Formal coverage testing of multimask spread as an uncertainty interval has not been published.
**Minimal Experiment:** In- and out-of-domain, compute coverage of candidate-spread intervals against true error distributions; compare with ensembles and conformal baselines.
**Main Risk:** Only a few candidate masks per prompt limits distributional resolution.

---

## Cluster 4 — Representation Mismatch (IDEA-B-0121 … IDEA-B-0155)

### IDEA-B-0121 — Representation profiles: what SAM, DINOv2, and CLIP each encode for dense tasks
**One-sentence idea:** Build a standardized probing battery that measures boundary-decodability, semantic-decodability, and instance-discriminability of frozen features from major vision foundation models, yielding per-model "representation profiles" that predict downstream task fit.
**Problem:** Backbone choice for dense tasks is driven by fashion and anecdote; the field lacks a quantitative account of which representational properties each pretraining paradigm actually produces.
**Core Hypothesis:** The three pretraining families occupy distinct, stable positions in profile space (mask-supervised → boundary-rich/semantics-poor; contrastive-language → semantics-rich/boundary-poor; self-distilled → intermediate), and profile distance predicts transfer performance better than any single benchmark score.
**Why Important:** Converts backbone selection from trial-and-error into measurement, and gives pretraining research a target vocabulary.
**Why Possibly Novel:** Systematic multi-property probing batteries with downstream-predictivity validation are missing for dense prediction.
**Minimal Experiment:** Probe 6+ public backbones on the battery; fine-tune each on 8 dense tasks; test profile-based prediction of the fine-tuning outcomes.
**Main Risk:** Probing results depend on probe capacity; requires careful probe standardization.

### IDEA-B-0122 — Angular aliasing: patch-grid anisotropy against thin oblique structures
**One-sentence idea:** Measure how segmentation quality of thin structures varies with their orientation relative to the ViT patch grid, and determine whether the effect stems from patch embedding, positional encoding, or attention locality.
**Problem:** Patch tokenization imposes a square lattice on images; thin structures crossing patches obliquely are fragmented across tokens in orientation-dependent ways, a potential systematic bias no one has quantified.
**Core Hypothesis:** Thin-structure IoU exhibits measurable periodic dependence on orientation (worst near 45° at widths below patch size), the effect persists after rotation augmentation, and it localizes to the patch-embedding stage via layer-wise interventions.
**Why Important:** Vessels, catheters, cracks, and wires are safety-critical targets; a lattice-induced bias would affect every ViT-based dense predictor.
**Why Possibly Novel:** Orientation-resolved evaluation against the token lattice has not been performed for segmentation.
**Minimal Experiment:** Rotate-and-evaluate protocols on synthetic and real thin structures across model families; fit orientation-response curves; ablate embedding variants (overlapping patches, anti-aliased stems).
**Main Risk:** Real-image confounds (acquisition anisotropy) may mask the lattice effect; synthetic controls are essential.

### IDEA-B-0123 — Preserving physical intensity semantics: learned windowing tokens for CT
**One-sentence idea:** Test whether encoding absolute CT Hounsfield values via learned windowing tokens outperforms the standard practice of normalizing them away, isolating how much diagnostic information ImageNet-style normalization destroys.
**Problem:** CT intensities are physically calibrated measurements (tissue-specific HU ranges), but foundation-model pipelines rescale them like photographs, discarding an information channel no natural-image model ever had.
**Core Hypothesis:** Models given absolute-intensity access through a dedicated input pathway segment intensity-defined boundaries (fat/water, calcification) measurably better at matched capacity, with gains concentrated exactly on tissue pairs whose HU ranges standard normalization collapses.
**Why Important:** Identifies a modality-specific representational loss inflicted by naive foundation-model reuse, with a minimal corrective.
**Why Possibly Novel:** Absolute-intensity preservation as a designed input pathway (rather than multi-window channel hacks) with attribution to specific tissue boundaries is unexplored.
**Minimal Experiment:** Compare standard normalization, multi-window channels, and windowing-token pathways on tissue-boundary-stratified CT segmentation at matched budgets.
**Main Risk:** Gains may be small for tasks where geometry dominates intensity.

### IDEA-B-0124 — Text-space collinearity predicts open-vocabulary confusion for amorphous classes
**One-sentence idea:** Test whether the near-collinearity of related concept embeddings in CLIP text space ("smoke", "steam", "fog", "haze") predicts—and upper-bounds—visual discrimination performance of open-vocabulary segmenters on those classes.
**Problem:** Open-vocab models fail to separate visually distinct but linguistically adjacent phenomena, and it is unknown whether the bottleneck is the visual encoder or the text anchor geometry.
**Core Hypothesis:** Per-class-pair confusion rates correlate strongly with text-embedding cosine similarity even after controlling for visual similarity, and replacing text anchors with visually derived anchors breaks the ceiling—localizing the failure to text-space geometry.
**Why Important:** Safety systems must distinguish smoke from steam; knowing the bottleneck is linguistic redirects the fix from data collection to anchor engineering.
**Why Possibly Novel:** Text-anchor geometry as a causal bound on dense-prediction discrimination has not been isolated.
**Minimal Experiment:** Measure confusion matrices for scattering-phenomena classes; regress on text similarity vs visual-feature similarity; intervene by substituting anchor types.
**Main Risk:** Visual similarity control requires a defensible independent visual metric.

### IDEA-B-0125 — How much does SAM depend on absolute position? A center-bias audit
**One-sentence idea:** Quantify the contribution of absolute spatial position (learned center bias from photographer-framed pretraining data) to SAM's mask predictions, using position-scrambled and off-center evaluation protocols.
**Problem:** Web images center their subjects; a model trained on them may embed positional priors that silently degrade performance on uncentered domains (whole-slide images, surveillance, satellite).
**Core Hypothesis:** Prompted mask quality for identical objects declines measurably toward image peripheries, the decline traces to positional-embedding statistics rather than feature quality, and periphery-heavy domains inherit a predictable performance tax.
**Why Important:** Position bias is a hidden transfer liability for the exact domains (medical scans, monitoring) where subjects are not framed.
**Why Possibly Novel:** Center-bias quantification with causal attribution to positional embeddings has not been done for promptable segmenters.
**Minimal Experiment:** Evaluate identical crops placed at controlled image positions; map position-response surfaces; repeat with positional-embedding ablations/retraining.
**Main Risk:** Border effects (padding, attention edge artifacts) confound pure position bias and must be separated.

### IDEA-B-0126 — Can single-mask decoders represent layered scenes? Transparency as a representation test
**One-sentence idea:** Test whether frozen foundation features contain sufficient information to decode two overlapping layers (transparent surface plus transmitted background) even though standard decoders output only one mask, separating representational capacity from output-format limitation.
**Problem:** Transparent-object failure is attributed to features, but the single-layer mask format cannot even express the correct answer—the two explanations demand different research programs.
**Core Hypothesis:** A two-layer probe decoder on frozen features recovers both the glass surface and the transmitted-content region substantially above chance, demonstrating that the bottleneck is the output format and supervision, not the representation.
**Why Important:** Redirects transparent-object research from feature learning toward layered output formats and supervision—if the hypothesis holds.
**Why Possibly Novel:** Layered-decodability probing as a diagnostic for the format-vs-representation question is new.
**Minimal Experiment:** On datasets with layered annotations (glass + background), train small two-layer probes on frozen SAM/DINOv2 features; compare against full fine-tuning and against chance-level controls.
**Main Risk:** Layered ground truth is scarce; may require purpose-built captures or renders.

### IDEA-B-0127 — Frequency-response mismatch between encoders and diagnostic bands in ultrasound
**One-sentence idea:** Characterize which spatial-frequency bands survive into deep features of ViT versus CNN encoders and test whether mismatch with ultrasound's diagnostic bands (speckle statistics) explains cross-architecture performance differences.
**Problem:** Architecture choices for ultrasound are made by benchmark scores without understanding which image frequencies each architecture preserves—yet ultrasound diagnosis lives in specific texture bands.
**Core Hypothesis:** Encoders act as measurable band-pass filters (estimable by band-limited probing), ultrasound task performance correlates with feature-band overlap with diagnostic bands, and targeted stem modifications that widen retention in those bands close cross-architecture gaps.
**Why Important:** Provides a mechanistic, transferable account of architecture-modality fit, replacing benchmark folklore.
**Why Possibly Novel:** Feature-space frequency-response measurement linked to modality-specific diagnostic bands is an unexplored analysis.
**Minimal Experiment:** Probe band-limited reconstruction from features across architectures; correlate band retention with task metrics across ultrasound tasks; validate with stem interventions.
**Main Risk:** Diagnostic-band definitions vary across ultrasound applications.

### IDEA-B-0128 — Is the prompt-to-mask map continuous? Lipschitz geometry of interactive segmentation
**One-sentence idea:** Measure the continuity structure of the click-position-to-output-mask mapping—identifying discontinuity manifolds where millimeter click changes flip the output—and test whether discontinuity density predicts interactive failure rates.
**Problem:** Users assume nearby clicks give similar masks; if the prompt-response map has dense discontinuities (mode switches between competing objects), interaction becomes unpredictable in ways average metrics never reveal.
**Core Hypothesis:** The prompt space is partitioned into basins separated by discontinuity boundaries that concentrate near object-part junctions and ambiguous regions; per-image discontinuity density is measurable, varies across domains, and predicts human interaction time better than one-shot IoU.
**Why Important:** Defines a geometric usability property of promptable models that interface design and training could explicitly optimize.
**Why Possibly Novel:** The topology/geometry of prompt-response maps has not been characterized for any promptable vision model.
**Minimal Experiment:** Dense prompt-grid evaluation on representative images; map basin structure; correlate discontinuity statistics with logged human interaction effort.
**Main Risk:** Dense grids are compute-heavy; sampling strategies must be validated.

### IDEA-B-0129 — Information-absent or decoder-limited? Oracle decoding of small structures
**One-sentence idea:** Determine whether small-lesion failure at 64×64 feature resolution reflects information truly absent from features or information present but undecodable by the standard mask decoder, using high-capacity oracle probes on frozen features.
**Problem:** The field responds to small-structure failure with higher-resolution inputs (expensive) without knowing whether existing features already contain the signal that a better decoder could extract.
**Core Hypothesis:** For lesions down to a measurable size threshold, oracle probes recover localization signal significantly exceeding the production decoder's output—implying decoder-limited failure—while below the threshold information is genuinely absent, cleanly splitting the regime where decoder research versus resolution research pays off.
**Why Important:** Allocates the field's effort between two expensive research directions with evidence instead of assumption.
**Why Possibly Novel:** Oracle-decodability regime analysis for dense prediction has not been used to partition failure causes by structure size.
**Minimal Experiment:** Train overparameterized probes (pixel-level readouts) on frozen features across lesion-size strata; compare probe vs decoder recall curves; identify the crossover size.
**Main Risk:** Probe overfitting could inflate decodability estimates; needs strict held-out validation.

### IDEA-B-0130 — Does SAM represent background as a class or as absence?
**One-sentence idea:** Probe whether foundation segmenters maintain an explicit representation of "background" (predictive structure in non-object regions) or treat it as mere absence, and link the answer to their behavior on target-absent images.
**Problem:** Hallucination on empty images and unstable negative prompts both plausibly stem from how background is represented, but the representational question has never been posed directly.
**Core Hypothesis:** Non-object regions carry systematic, decodable structure (scene context, "objectness deserts") rather than noise, and the strength of this background structure per image predicts resistance to hallucinated masks under target-absent prompting.
**Why Important:** Explains and predicts a safety-relevant failure (segmenting things that aren't there) from representational first principles.
**Why Possibly Novel:** Background representation as an object of study—rather than a label complement—is essentially untouched in the segmentation literature.
**Minimal Experiment:** Probe background-region features for scene decodability; correlate per-image background-structure metrics with hallucination rates under forced prompting on absent targets.
**Main Risk:** Defining hallucination cleanly requires curated absent-target test sets.

### IDEA-B-0131 — Decoder depth versus topological complexity of targets
**One-sentence idea:** Test whether the shallow cross-attention decoder of SAM-style models imposes a measurable ceiling on segmenting topologically complex targets (branching vessels, perforated structures), by scaling decoder depth at frozen encoder.
**Problem:** Decoder capacity is treated as an efficiency knob, but complex topologies may require iterative relational computation the two-layer decoder cannot express, confounding "hard domain" with "insufficient decode steps."
**Core Hypothesis:** Segmenting targets beyond a topological-complexity threshold (loops, branch count) improves systematically with decoder depth at fixed encoder—unlike simple-topology targets which saturate immediately—revealing a complexity-matched decoder-depth law.
**Why Important:** Gives an architectural design rule tied to target structure, replacing one-size-fits-all decoders.
**Why Possibly Novel:** Topology-stratified decoder-scaling analysis has not been reported.
**Minimal Experiment:** Train decoders of depth 2–12 on frozen features across topology-stratified target sets (synthetic + vessels); fit depth-requirement curves against complexity measures.
**Main Risk:** Depth gains may be conflated with parameter-count gains; requires width-matched controls.

### IDEA-B-0132 — Where do VLMs lose spatial detail? Layer-wise localization decay in vision-language models
**One-sentence idea:** Trace the layer-by-layer decay of pixel-localizable information in LLaVA-style VLMs to identify precisely where dense-prediction capacity is destroyed by token pooling and language-alignment stages.
**Problem:** VLMs are being asked to ground, point, and segment, but their architecture compresses spatial detail at unidentified stages—without a decay map, dense-VLM design is guesswork.
**Core Hypothesis:** Localization information (probed per layer as boundary recovery) collapses sharply at identifiable bottlenecks (projector, resampler) rather than gradually through the language model, implying that dense capability can be restored with taps at pre-collapse layers rather than architectural overhauls.
**Why Important:** Directs the design of dense-capable VLMs—a major current engineering race—with measurement instead of intuition.
**Why Possibly Novel:** Layer-wise dense-decodability tracing through multimodal alignment stages has not been published systematically.
**Minimal Experiment:** Probe boundary/mask decodability at every stage of 3 open VLMs; localize collapse points; validate by attaching dense heads pre- versus post-collapse.
**Main Risk:** Architecture heterogeneity across VLMs may resist a unified narrative.

### IDEA-B-0133 — Texture-shape bias measured natively for dense prediction
**One-sentence idea:** Construct cue-conflict stimuli for segmentation (texture of one class filling the shape of another, with dense labels for both readings) and measure the texture-shape bias of segmenters directly, rather than importing classification-based bias scores.
**Problem:** The influential texture-vs-shape bias literature is classification-based; dense predictors may weigh cues differently per pixel position (interior vs boundary), and no native measurement exists.
**Core Hypothesis:** Segmentation models show spatially structured cue reliance—shape-dominant near boundaries, texture-dominant in interiors—and the interior texture reliance predicts vulnerability to texture-shifted domains (stain changes, sensor swaps) better than classification bias scores.
**Why Important:** Provides the correct diagnostic instrument for a property routinely (and wrongly) inferred from classification experiments.
**Why Possibly Novel:** Pixel-resolved cue-conflict methodology for dense models does not exist.
**Minimal Experiment:** Generate cue-conflict segmentation stimuli; evaluate model families; map per-pixel cue weights; correlate with cross-domain degradation.
**Main Risk:** Synthetic cue-conflict stimuli may sit off-manifold, distorting cue estimates.

### IDEA-B-0134 — The modal-amodal gap: can foundation features support occlusion completion?
**One-sentence idea:** Quantify the gap between modal (visible-region) and amodal (full-extent) mask decodability from frozen foundation features, testing whether SA-1B-style visible-mask pretraining leaves amodal structure recoverable.
**Problem:** Medical and robotic applications need full-extent structure estimates behind occluders, but mask-pretraining supervises only visible regions—whether amodal completion is latent in the features or absent is unknown.
**Core Hypothesis:** Amodal extent is partially decodable from frozen features for familiar shape families (learned shape priors persist despite modal supervision) but collapses for novel shapes, and the decodable fraction predicts which applications can use foundation features without amodal retraining.
**Why Important:** Determines whether amodal perception requires new pretraining or just new decoders—a large fork in research investment.
**Why Possibly Novel:** Amodal decodability probing of modal-supervised foundation models is unexplored.
**Minimal Experiment:** On amodal-annotated datasets, train amodal probes on frozen features; stratify by shape familiarity; compare against amodally fine-tuned baselines.
**Main Risk:** Amodal ground truth is partly conventional, adding label noise to the probe target.

### IDEA-B-0135 — Structured spatial damage from token merging in dense prediction
**One-sentence idea:** Measure the spatially structured errors introduced by token-reduction acceleration methods (merging, pruning) in segmentation, testing whether their classification-validated "losslessness" hides systematic boundary and small-object damage.
**Problem:** Token reduction is certified on classification accuracy, then transplanted into dense pipelines; merged tokens necessarily blur spatial distinctions, but where and how much is unmeasured.
**Core Hypothesis:** Token merging concentrates damage on boundary pixels and small structures with error proportional to local merge density (measurable per image), while leaving region interiors intact—making mean-IoU audits look benign while structure-critical use cases silently degrade.
**Why Important:** Efficiency methods are deployed into safety-relevant dense systems on the strength of the wrong evidence; a spatial damage map corrects the record.
**Why Possibly Novel:** Spatially resolved audits of token-reduction damage for dense tasks are missing.
**Minimal Experiment:** Sweep merge ratios across models; map error against local merge topology; stratify by structure size and boundary distance.
**Main Risk:** Findings vary across merging algorithms; requires covering the main families.

### IDEA-B-0136 — Luminance-only smoke: which color channels actually carry the signal?
**One-sentence idea:** Determine the causal contribution of color-opponent channels versus pure luminance to smoke segmentation across models and datasets, testing whether smoke perception is fundamentally achromatic and color inputs mainly import false-positive risks.
**Problem:** Smoke has weak chromatic signature, yet models consume RGB; whether color helps, is neutral, or actively harms (via sunset/haze confusions) is unknown and matters for sensor and preprocessing choices.
**Core Hypothesis:** Luminance-only inputs preserve nearly all true-positive performance while measurably reducing chromatic false positives (sunset glow, brown dust), implying color is net-negative for smoke segmentation in RGB deployments.
**Why Important:** A counterintuitive, immediately actionable preprocessing recommendation for a deployed safety application—and a clean case study in channel-level cue attribution.
**Why Possibly Novel:** Channel-causal analysis (not just ablation accuracy) for amorphous-target segmentation has not been carried out.
**Minimal Experiment:** Evaluate and retrain models on {RGB, luminance-only, chroma-only, decorrelated} inputs across smoke datasets with FP-stratified reporting.
**Main Risk:** Some smoke types (chemical fires) have genuine chromatic signatures that luminance-only would sacrifice.
### IDEA-B-0137 — Do high-norm outlier tokens corrupt prompted segmentation at specific locations?
**One-sentence idea:** Audit whether the high-norm "artifact/register" tokens known to arise in large ViTs spatially co-locate with prompted-segmentation errors, and whether register-token retrofits repair the affected regions.
**Problem:** Outlier tokens have been characterized for classification and feature quality, but their spatial consequences for dense prediction—where every token is an output location—are unexamined.
**Core Hypothesis:** Prompted-mask errors are significantly enriched at high-norm token positions, prompts landing on such positions produce anomalously unstable masks, and models retrofitted with register tokens show localized error reductions exactly at former outlier sites.
**Why Important:** Connects a known representational pathology to concrete dense-prediction failures, with an available architectural remedy whose dense-task value is unproven.
**Why Possibly Novel:** The outlier-token literature has not been linked to segmentation error geography.
**Minimal Experiment:** Localize high-norm tokens across images; compute error enrichment statistics; compare matched models with and without registers on prompt-on-outlier stress tests.
**Main Risk:** Outlier positions may correlate with genuinely hard content, confounding enrichment.

### IDEA-B-0138 — Is 2D-slice independence a representational ceiling for 3D anatomy?
**One-sentence idea:** Measure how much inter-slice anatomical consistency is already encoded in independently computed 2D foundation features—by testing cross-slice predictability—versus what genuinely requires 3D processing.
**Problem:** Slice-wise application of 2D foundation models to volumetric data is standard, and the community assumes a "2D ceiling" without quantifying how much 3D structure the 2D features implicitly capture.
**Core Hypothesis:** Adjacent-slice feature predictability is high enough to support accurate cross-slice mask propagation for large organs but collapses for tortuous thin structures, defining a measurable per-structure boundary where true 3D architectures become necessary.
**Why Important:** Prevents both over-investment in expensive 3D foundation models where 2D suffices and under-investment where it cannot.
**Why Possibly Novel:** Cross-slice predictability as an information-theoretic proxy for the 2D-vs-3D necessity question is a new measurement approach.
**Minimal Experiment:** Train slice-to-slice feature/mask predictors on frozen 2D features across structure types; compare propagation accuracy against native-3D baselines per structure.
**Main Risk:** Slice spacing heterogeneity across datasets complicates comparable measurement.

### IDEA-B-0139 — Quantifying the compactness prior: how strongly does SAM assume blob-like objects?
**One-sentence idea:** Measure the strength of foundation segmenters' shape priors (compactness, closedness, convexity) using parametric synthetic shape families, and map prior strength against the shape statistics of pretraining data.
**Problem:** Elongated, perforated, and scattered targets (tools, meshes, wires, multifocal lesions) fail in ways attributed loosely to "shape bias" that has never been parameterized or measured.
**Core Hypothesis:** Prompted mask quality declines smoothly along interpretable shape axes (aspect ratio, perimeter²/area, hole count) with a decline rate that quantifies the prior, and the measured prior matches the shape distribution of SA-1B rather than architectural constraints—predicting it is data-fixable.
**Why Important:** Separates data-driven from architecture-driven shape limitations and yields a reusable prior-strength benchmark for future models.
**Why Possibly Novel:** Parametric psychophysics-style prior measurement for segmentation models does not exist.
**Minimal Experiment:** Render shape-family gradients into natural contexts; evaluate models along each axis; compare decline rates with pretraining shape statistics and across model generations.
**Main Risk:** Synthetic-to-real gap in shape rendering may distort prior estimates.

### IDEA-B-0140 — Is segmentation granularity linearly controllable in embedding space?
**One-sentence idea:** Test whether the part-versus-whole granularity of text-prompted segmentation can be continuously controlled by arithmetic in the text-embedding space, or whether granularity is a discrete, non-linear property of current cross-modal representations.
**Problem:** Users need granularity control ("the handle" vs "the cup"), and prompt engineering achieves it unreliably; whether granularity is a navigable direction in embedding space is a basic open question about cross-modal geometry.
**Core Hypothesis:** Interpolating between part-level and whole-level text embeddings produces abrupt, non-monotonic mask transitions (granularity is not linearly encoded), but a low-dimensional non-linear granularity manifold exists and can be learned from few examples.
**Why Important:** Establishes what granularity control is possible via representation manipulation versus what requires architectural mechanisms.
**Why Possibly Novel:** Embedding-space granularity geometry has not been characterized for text-promptable segmentation.
**Minimal Experiment:** Build part-whole prompt pairs across categories; sweep embedding interpolations; measure mask-transition curves; attempt manifold learning on granularity-labeled prompts.
**Main Risk:** Results may be specific to a given text-encoder family.

### IDEA-B-0141 — Early-warning metrics for representation collapse during aggressive fine-tuning
**One-sentence idea:** Identify which representational properties (linear separability, augmentation-equivariance, neighborhood topology) degrade first during over-aggressive fine-tuning of foundation segmenters, and validate them as early-warning signals that predict impending generalization loss before validation metrics show it.
**Problem:** Fine-tuning silently destroys transferable structure; practitioners discover the damage only after downstream failures, lacking online indicators of representational health.
**Core Hypothesis:** A specific ordering of degradation exists (equivariance decays before separability, which decays before in-domain accuracy), is consistent across domains, and thresholding the earliest indicator prevents the majority of generalization-loss events at negligible accuracy cost.
**Why Important:** Turns fine-tuning from an open-loop procedure into a monitored process with tripwires—valuable for every adaptation pipeline.
**Why Possibly Novel:** Degradation-ordering measurement and early-warning validation for dense-model fine-tuning is new.
**Minimal Experiment:** Instrument fine-tuning runs across aggressiveness levels; track candidate indicators; test predictive lead time against later out-of-domain evaluations.
**Main Risk:** Indicator orderings may differ across optimizers and PEFT types.

### IDEA-B-0142 — Context truncation error in gigapixel imagery: what does sliding-window inference lose?
**One-sentence idea:** Quantify the error attributable to context truncation when foundation segmenters process whole-slide pathology through fixed windows, by comparing against oracle-context inference on matched regions.
**Problem:** Gigapixel images force windowed inference, and everyone accepts the resulting context loss without knowing its size, spatial structure, or which decisions it corrupts.
**Core Hypothesis:** Context-truncation error concentrates on identifiable region types (boundary-ambiguous glands, sparse infiltration patterns) where correct segmentation provably requires evidence beyond the window, and a cheap low-resolution global-context side-channel recovers most of the loss without full-resolution global attention.
**Why Important:** Establishes the real cost of the field's default inference mode and bounds the value of long-context vision architectures for pathology.
**Why Possibly Novel:** Oracle-context ablation methodology for windowed dense inference has not been applied rigorously.
**Minimal Experiment:** Evaluate matched regions under window sizes up to memory limits plus downsampled-global conditioning; attribute error deltas per region type.
**Main Risk:** True oracle context is bounded by hardware, capping the measurable ceiling.

### IDEA-B-0143 — Flame-smoke entanglement: are fire features confounded with their own illumination?
**One-sentence idea:** Test whether models detect flames partly through the illumination flames cast on surrounding smoke and scene—an entangled cue that fails for distant, daylight, or occluded fires—using intrinsic-decomposition interventions.
**Problem:** Fire detectors trained on typical footage may bind flame identity to co-occurring glow, explaining systematic failures on daylight fires and smoldering events with no visible flame illumination.
**Core Hypothesis:** Removing cast illumination via intrinsic decomposition (or relighting interventions) degrades flame segmentation far more than it degrades other bright-object segmentation, quantifying an illumination-reliance factor that predicts daylight-fire failure rates.
**Why Important:** Explains a documented operational failure mode (daytime/distant fires) and defines the augmentation needed to fix it.
**Why Possibly Novel:** Cue-entanglement analysis between an object and its own photometric effects has not been formalized in detection research.
**Minimal Experiment:** Build relit counterfactuals of fire scenes; compare degradation profiles across models; correlate illumination-reliance with performance on curated daylight-fire test sets.
**Main Risk:** Intrinsic decomposition quality on fire scenes may limit intervention fidelity.

### IDEA-B-0144 — Do different prompt types read different representations? An RSA study of prompt pathways
**One-sentence idea:** Use representational similarity analysis to test whether point, box, and mask prompts cause the decoder to consume systematically different feature subspaces, predicting per-target which prompt type will succeed.
**Problem:** Prompt types are treated as interchangeable interfaces to one representation, yet empirical prompt-type performance differences suggest they access distinct computational pathways whose structure is unknown.
**Core Hypothesis:** Decoder cross-attention distributions under different prompt types diverge measurably and consistently (boxes attend to extent-defining features, points to local-continuity features), and the divergence structure predicts target-conditional prompt-type superiority (thin targets need boxes; textured blobs tolerate points).
**Why Important:** Grounds practical prompt-selection guidance in mechanism, and informs decoder design for prompt-type robustness.
**Why Possibly Novel:** Mechanistic pathway analysis across prompt types has not been performed on promptable segmenters.
**Minimal Experiment:** Collect attention/feature-usage statistics per prompt type across target strata; test pathway-divergence metrics as predictors of the prompt-type × target performance matrix.
**Main Risk:** Attention statistics are an imperfect proxy for information flow; may need causal patching methods.

### IDEA-B-0145 — Equivariance debt: does orientation bias from photographic pretraining harm medical orientation conventions?
**One-sentence idea:** Measure rotation/reflection equivariance errors of foundation segmenters and test whether they systematically interact with medical imaging's orientation conventions (radiological vs anatomical views, prone/supine flips).
**Problem:** Photographic pretraining bakes in gravity-aligned orientation priors; medical images follow entirely different conventions, and per-orientation performance differences would constitute a silent, correctable bias.
**Core Hypothesis:** Segmentation quality varies measurably under clinically legitimate orientation transforms (beyond augmentation-level noise), the variation traces to orientation-selective features inherited from pretraining, and per-orientation calibration or canonicalization eliminates it at zero architectural cost.
**Why Important:** Orientation is a controlled, documented variable in medical pipelines—an equivariance audit converts an invisible bias into a checklist fix.
**Why Possibly Novel:** Equivariance measurement targeted at conventional (not adversarial) orientation transforms in deployed medical settings is missing.
**Minimal Experiment:** Evaluate models under the group of clinically occurring transforms across modalities; decompose variance; test canonicalization and equivariant-adapter fixes.
**Main Risk:** Some orientation dependence is anatomically legitimate (organs are not symmetric), requiring careful separation.

### IDEA-B-0146 — Feature transplant: does the decoder read identity or only geometry?
**One-sentence idea:** Transplant encoder features between images (swapping feature content within matched spatial layouts) to test whether mask decoders consume object-identity information or operate as pure geometry readers of boundary-like feature patterns.
**Problem:** It is unknown what the decoder actually uses: if it reads only local boundary structure, semantic fine-tuning of encoders is wasted effort for prompted segmentation; if it reads identity, boundary-focused training is insufficient.
**Core Hypothesis:** Decoders produce nearly intact masks when identity-carrying feature components are swapped but geometry-carrying components are preserved (demonstrating geometry-dominant reading), with the identity contribution rising only for low-contrast targets where geometry underdetermines the mask.
**Why Important:** Directly informs where adaptation capacity should be spent (encoder semantics vs boundary sharpening) for prompted pipelines.
**Why Possibly Novel:** Causal feature-transplant methodology for decomposing decoder inputs has not been applied to segmentation.
**Minimal Experiment:** Decompose features (subspace or layer-wise) into identity/geometry candidates via probing; transplant across image pairs; measure mask preservation per component and target contrast level.
**Main Risk:** Feature decompositions may not cleanly separate identity from geometry.

### IDEA-B-0147 — Embedding-density deserts: does a domain's position in feature space predict adaptation gain?
**One-sentence idea:** Test whether the local density of a target domain's images in the foundation model's embedding space (estimated against a large reference corpus) predicts zero-shot performance and fine-tuning gain, making density a pre-annotation planning signal.
**Problem:** Teams cannot cheaply predict whether a new domain will work zero-shot or demand adaptation; embedding-space geometry offers a label-free candidate predictor that has not been validated.
**Core Hypothesis:** Zero-shot IoU falls and fine-tuning gain rises monotonically as target images sit in lower-density regions of the pretraining-representative embedding distribution, with density explaining substantially more variance than simple visual-similarity heuristics.
**Why Important:** A validated density signal converts adaptation planning into a five-minute computation before any annotation spending.
**Why Possibly Novel:** Density-based capability prediction is emerging for LLMs but unvalidated for dense vision tasks.
**Minimal Experiment:** Estimate densities for 20 diverse target datasets against a web-scale reference embedding sample; correlate with measured zero-shot and post-fine-tuning metrics.
**Main Risk:** Density estimation in high dimensions is fragile; requires careful dimensionality-reduction validation.

### IDEA-B-0148 — Do learned upsamplers hallucinate boundary detail? A ground-truth-free consistency audit
**One-sentence idea:** Test whether learned feature upsamplers (from 64×64 features to full-resolution masks) synthesize plausible-but-fabricated boundary micro-geometry, by measuring the consistency of predicted detail across imperceptible input perturbations.
**Problem:** Upsampling decoders necessarily invent sub-feature-resolution detail; if the invented detail is unstable fiction rather than image-grounded inference, boundary metrics reward hallucination—unmeasurable by accuracy alone.
**Core Hypothesis:** A significant fraction of sub-patch boundary detail changes under perturbations that leave the underlying image information equivalent (sensor-noise resampling), identifying hallucinated detail; hallucination fraction varies across decoder designs and predicts boundary-metric non-reproducibility across acquisitions.
**Why Important:** Distinguishes real boundary precision from confabulated precision—critical wherever boundary measurements feed clinical decisions.
**Why Possibly Novel:** Hallucination quantification for segmentation upsampling (as opposed to generative imagery) is unstudied.
**Minimal Experiment:** Acquire or simulate repeated same-scene captures; measure boundary-detail reproducibility per decoder; separate stable inference from unstable invention.
**Main Risk:** Distinguishing hallucination from legitimate aleatoric sensitivity requires careful noise modeling.

### IDEA-B-0149 — The relational prompt gap: spatial-relation language fails dense grounding
**One-sentence idea:** Quantify how segmentation-from-language degrades when prompts require relational reasoning ("the vessel behind the tumor", "the smaller mass left of the kidney") versus attributive reference, isolating relation processing as a distinct failure mode of dense VLM grounding.
**Problem:** Clinical and operational language is heavily relational, but grounding benchmarks are dominated by attributive references, hiding a suspected cliff in relational spatial understanding.
**Core Hypothesis:** Matched-difficulty relational prompts produce a large, consistent performance drop relative to attributive prompts across dense-grounding models, the drop localizes to relation composition rather than entity recognition (verifiable by oracle-entity ablations), and scaling model size barely closes it.
**Why Important:** Defines the real readiness level of language-driven segmentation for professional use, where relations are unavoidable.
**Why Possibly Novel:** Relation-attributive matched-pair methodology for dense grounding, with component-wise attribution, has not been executed.
**Minimal Experiment:** Build matched attributive/relational prompt pairs over identical targets; evaluate dense-grounding models; run oracle-component ablations to localize the failure.
**Main Risk:** Matching difficulty across prompt types is subtle and needs human validation.

### IDEA-B-0150 — One encoder, many dense tasks: testing feature sufficiency beyond masks
**One-sentence idea:** Measure whether frozen mask-pretrained features support depth, normals, and boundary-ownership prediction at quality competitive with task-specific features—testing whether "segment anything" pretraining produces genuinely general dense representations.
**Problem:** The "foundation" label implies task generality, but mask-supervised features may encode precisely the mask-relevant abstraction and discard other scene properties, a question with direct consequences for multi-task deployment.
**Core Hypothesis:** Frozen mask-pretrained features show a characteristic sufficiency profile—strong for occlusion boundaries and ownership, systematically weak for metric depth—revealing that mask supervision teaches topological rather than metric scene structure.
**Why Important:** Multi-task systems (robotics, surgical guidance) want one backbone; a sufficiency profile determines whether that is sound engineering or wishful thinking.
**Why Possibly Novel:** Systematic cross-task sufficiency profiling of mask-supervised features against matched baselines is not established.
**Minimal Experiment:** Train standardized probes for 5 dense tasks on frozen features from mask-, language-, and self-supervised models; compare sufficiency profiles at matched probe capacity.
**Main Risk:** Probe design choices could dominate cross-task comparisons without careful standardization.

### IDEA-B-0151 — Scanner fingerprints in foundation features: measuring the shortcut substrate
**One-sentence idea:** Quantify how strongly frozen foundation features encode acquisition metadata (scanner model, site, protocol) relative to anatomy, and test whether this "fingerprint strength" predicts susceptibility to shortcut learning during fine-tuning.
**Problem:** Site-shortcut failures are diagnosed after deployment; if the shortcut substrate is measurable in frozen features before any training, screening becomes possible.
**Core Hypothesis:** Scanner identity is linearly decodable from frozen features at high accuracy, fingerprint strength varies across backbone families in predictable ways (contrastive > mask-supervised), and pre-training-time fingerprint strength predicts the fine-tuned model's site-transfer gap.
**Why Important:** Provides a cheap pre-screening instrument for shortcut vulnerability, applicable before data labeling begins.
**Why Possibly Novel:** Fingerprint-strength measurement as a predictive screening tool (not a post-hoc explanation) is new.
**Minimal Experiment:** Probe scanner/site decodability across backbones on multi-site data; fine-tune each backbone; correlate fingerprint strength with measured transfer gaps.
**Main Risk:** Fingerprint decodability may be necessary but not sufficient for shortcut adoption, weakening prediction.

### IDEA-B-0152 — Phase information and thin-structure continuity
**One-sentence idea:** Test whether the continuity of thin structures in segmentation outputs depends on image phase information (edge alignment structure) by phase-scrambling interventions, locating where continuity cues live in the input and features.
**Problem:** Vessel and wire segmentations break into fragments under domain shift, and the fragility's source—amplitude statistics versus phase-encoded alignment—determines which augmentations and architectures can fix it.
**Core Hypothesis:** Local phase coherence is the dominant carrier of thin-structure continuity (band-limited phase scrambling fragments predictions while amplitude perturbations do not), and features retaining phase-sensitive channels predict continuity robustness across models.
**Why Important:** Gives a mechanistic target (phase-coherent feature preservation) for the persistent clinical problem of fragmented vessel predictions.
**Why Possibly Novel:** Phase-versus-amplitude causal analysis for dense prediction continuity is absent from the literature.
**Minimal Experiment:** Apply band-limited phase/amplitude perturbations to vessel imagery; measure fragmentation metrics across models; probe features for phase sensitivity and correlate.
**Main Risk:** Global phase scrambling destroys too much; local scrambling methodology needs careful design.

### IDEA-B-0153 — Prompt saturation: why additional clicks stop helping
**One-sentence idea:** Characterize the saturation curve of prompted segmentation quality versus number of prompt points, and identify the architectural cause (attention normalization, token competition) of the observed plateau.
**Problem:** Interactive users report diminishing and sometimes zero returns beyond a few clicks—if saturation is architectural rather than informational, correction workflows are fundamentally capped.
**Core Hypothesis:** Quality saturates after a small number of points even when substantial error remains and later clicks carry decisive information (verified by oracle-decoder comparisons), and the saturation traces to attention weight dilution across prompt tokens—predicting that renormalization schemes lift the ceiling.
**Why Important:** The click-response ceiling bounds every interactive annotation and clinical correction workflow built on promptable models.
**Why Possibly Novel:** Saturation as an architectural phenomenon (with causal localization) rather than a usability observation has not been analyzed.
**Minimal Experiment:** Measure quality-vs-click-count curves with information-controlled click sequences; compare against oracle decoders given identical clicks; intervene on attention normalization.
**Main Risk:** Saturation causes may differ across decoder designs, fragmenting the story.

### IDEA-B-0154 — Static-shape priors versus dynamic textures: is fire fundamentally mis-represented?
**One-sentence idea:** Test whether the object-centric, static-shape representational priors of image-pretrained segmenters actively mis-model flames—whose identity is a temporal texture, not a shape—by comparing against spatiotemporal-feature baselines at matched capacity.
**Problem:** Fire is defined by its dynamics (flicker statistics, turbulent motion), yet frame-wise foundation models represent it as a shaped region, potentially explaining chronic confusion with flame-colored static objects.
**Core Hypothesis:** For flame segmentation, small spatiotemporal models beat much larger static foundation models specifically on discrimination against flame-like static distractors (sunsets, orange fabric, lights), quantifying a representational-category error rather than a capacity gap.
**Why Important:** Redirects fire-perception research from scaling static models toward dynamics-aware representations, with measurable safety consequences.
**Why Possibly Novel:** Framing fire as a representational-category mismatch (object vs dynamic texture) with controlled distractor evaluation is new.
**Minimal Experiment:** Build a static-distractor benchmark; compare frame-wise foundation models against compact temporal models at matched parameters on distractor discrimination.
**Main Risk:** Temporal baselines introduce architecture confounds beyond the static/dynamic distinction.

### IDEA-B-0155 — Can epistemic uncertainty be linearly read from frozen features?
**One-sentence idea:** Test whether a frozen foundation encoder's features linearly encode the information needed to predict the model's own segmentation errors—enabling single-pass, ensemble-free uncertainty at near-zero cost.
**Problem:** Practical uncertainty methods multiply inference cost (ensembles, MC sampling); if error-predictive signal already exists linearly in features, deployment-grade uncertainty is being needlessly overpriced.
**Core Hypothesis:** A linear probe on frozen features predicts per-region segmentation failure with AUROC approaching a deep ensemble's at a small fraction of the cost, and the linearly available signal specifically captures familiarity-based (epistemic) failure while missing ambiguity-based (aleatoric) failure—cleanly splitting the two by capacity.
**Why Important:** Would make meaningful uncertainty free for every frozen-backbone pipeline, and provide an operational epistemic/aleatoric separation criterion.
**Why Possibly Novel:** Linear decodability of self-error signal from foundation features has not been established for dense prediction.
**Minimal Experiment:** Train linear error-prediction probes on frozen features across in- and out-of-domain sets; benchmark against ensembles/MC-dropout on error types stratified by ambiguity.
**Main Risk:** Linear probes may capture dataset difficulty proxies rather than transferable uncertainty signal.

---

## Cluster 5 — Multimodal Supervision (IDEA-B-0156 … IDEA-B-0185)

### IDEA-B-0156 — The exchange rate between radiology reports and pixel labels
**One-sentence idea:** Measure how many report-supervised images (spatial constraints parsed from routine radiology text) equal one expert pixel-labeled image for training lesion segmenters, establishing a supervision exchange rate.
**Problem:** Hospitals hold millions of image-report pairs and few masks, but the quantitative value of report text as segmentation supervision has never been priced against pixel labels.
**Core Hypothesis:** Report-derived constraints (laterality, lobe, size mentions) provide supervision worth a stable, measurable fraction of a pixel label—with the exchange rate varying predictably by finding type (focal high, diffuse low)—so optimal budgets mix both sources according to the measured rate.
**Why Important:** Converts an idle data asset into a quantified training resource and gives planners an evidence-based mixing rule.
**Why Possibly Novel:** Supervision pricing via controlled exchange-rate experiments (not just "text helps") is new for dense medical prediction.
**Minimal Experiment:** On a dataset with reports and masks, train models on grids of (n_masks × n_report-only images); fit iso-performance curves; derive exchange rates per finding type.
**Main Risk:** Report parsing errors could contaminate the supervision signal being priced.

### IDEA-B-0157 — What thermal knowledge is RGB-recoverable? Cross-modal distillation limits for fire
**One-sentence idea:** Determine which components of thermal-camera fire/smoke discrimination can be distilled into RGB-only models and which are physically unrecoverable, producing a decomposition of the thermal advantage.
**Problem:** Thermal cameras solve much of fire detection but cost too much for dense deployment; distillation to RGB is attempted blindly, without knowing which thermal cues have RGB correlates.
**Core Hypothesis:** A measurable fraction of thermal advantage is RGB-recoverable (heat shimmer, smoke-source geometry, glow gradients) while a residual is physically absent from RGB (obscured hotspots), and the recoverable fraction is identifiable in advance by measuring RGB-feature predictability of thermal responses per scene region.
**Why Important:** Bounds the achievable performance of cheap RGB-only fire networks and prevents chasing physically impossible targets.
**Why Possibly Novel:** Recoverability decomposition (rather than aggregate distillation gains) for cross-modal supervision is a new analysis frame.
**Minimal Experiment:** On paired RGB-thermal fire footage, train RGB models to predict thermal channels; map per-region predictability; distill with recoverability-weighted losses and compare against uniform distillation.
**Main Risk:** Paired-modality fire datasets are limited; may require purpose-built captures.

### IDEA-B-0158 — Crackle as a label: audio-derived temporal supervision for fire video
**One-sentence idea:** Use fire's acoustic signature (crackling detected from camera microphones) as free temporal weak labels for training visual fire segmenters on unlabeled surveillance archives.
**Problem:** Vast unlabeled camera archives contain fire events, but mining them for visual training requires temporal localization that manual review cannot scale to.
**Core Hypothesis:** Audio crackle detection provides temporal event boundaries accurate enough that visual models trained with audio-anchored contrastive objectives (fire-time vs pre-fire frames from the same camera) learn fire-discriminative visual features rivaling supervised pretraining on curated data.
**Why Important:** Unlocks self-labeling of operational archives—the cheapest possible data source for a data-starved safety application.
**Why Possibly Novel:** Audio as temporal anchor for dense visual fire learning is unexplored (audio-visual work centers on speech and events, not amorphous safety targets).
**Minimal Experiment:** On videos with audio and visual fire annotations, measure audio-anchor temporal precision; train anchor-supervised visual models; compare against supervised baselines at matched data volume.
**Main Risk:** Wind and compression destroy audio quality on many surveillance systems.

### IDEA-B-0159 — Missing depth as free supervision: exploiting RGB-D sensor failure for transparency
**One-sentence idea:** Use the systematic failure of depth sensors on transparent and reflective surfaces—invalid-depth pixels—as free, automatically harvested training labels for RGB transparency segmentation at scale.
**Problem:** Transparent-object segmentation is label-starved because glass is hard for humans to annotate too, while millions of RGB-D frames already contain physics-generated transparency indicators nobody exploits as supervision.
**Core Hypothesis:** Invalid-depth masks, after filtering confounders (range limits, absorption, occlusion shadows) with geometric consistency rules, provide supervision noisy but abundant enough that models trained on harvested labels approach fully supervised transparency segmentation—with a characterizable, correctable noise structure.
**Why Important:** Converts a sensor weakness into a self-supervision channel, potentially producing the largest transparency training corpus in existence at zero annotation cost.
**Why Possibly Novel:** Depth-invalidity as a deliberate label source (with noise characterization) rather than a nuisance has barely been explored.
**Minimal Experiment:** Harvest invalid-depth masks from public RGB-D corpora; characterize label noise against GT on transparency benchmarks; train and evaluate RGB models on harvested vs manual labels at matched scale.
**Main Risk:** Confounder filtering may remove most volume or leave structured noise that biases learned transparency cues.

### IDEA-B-0160 — Word-level versus sentence-level alignment: supervision granularity for dense grounding
**One-sentence idea:** Isolate the effect of text-supervision granularity—sentence-level contrastive alignment versus word-region alignment—on downstream dense prediction, holding data, capacity, and compute fixed.
**Problem:** Dense-grounding models inherit their text supervision from design conventions; whether finer-grained alignment actually buys dense-task performance, and how much, has not been cleanly measured.
**Core Hypothesis:** Word-region alignment yields disproportionate gains on segmentation relative to its negligible gains on retrieval (the standard evaluation), meaning the field's retrieval-centric evaluation has systematically under-valued fine-grained supervision for dense purposes.
**Why Important:** Guides the supervision design of the next generation of dense-capable VLMs with a controlled result rather than folklore.
**Why Possibly Novel:** Granularity-controlled supervision comparisons targeting dense outcomes (not retrieval) are missing.
**Minimal Experiment:** Pretrain matched models on identical corpora under the two alignment granularities; evaluate on segmentation, grounding, and retrieval; compare gain profiles.
**Main Risk:** Pretraining compute requirements; may need to operate at modest scale and argue trends.

### IDEA-B-0161 — Registered cross-modality disagreement as an annotation trigger
**One-sentence idea:** Use disagreement between segmentations of registered multi-modal pairs (CT vs MRI of the same patient) as an unsupervised signal to filter pseudo-labels and to target expert annotation where modalities conflict.
**Problem:** Pseudo-label filtering relies on single-model confidence, which fails exactly where models are confidently wrong; registered modalities offer independent evidence whose disagreement is a physics-grounded error signal.
**Core Hypothesis:** Cross-modality mask disagreement identifies pseudo-label errors with substantially higher precision than confidence-based filtering, and routing expert annotation to high-disagreement cases yields steeper data-efficiency curves than uncertainty-based active learning.
**Why Important:** Multi-modal acquisitions are routine in clinical practice; their consistency structure is an untapped quality-control channel for label-efficient training.
**Why Possibly Novel:** Registered-modality disagreement as both filter and acquisition function—with head-to-head comparisons—has not been formalized.
**Minimal Experiment:** On registered CT-MRI datasets with GT, measure disagreement-vs-error precision curves; run active-learning simulations comparing disagreement-routing against uncertainty-routing.
**Main Risk:** Registration error itself generates disagreement, requiring deformation-aware disagreement measures.

### IDEA-B-0162 — Polarization-taught transparency: can physics-privileged training transfer to plain RGB?
**One-sentence idea:** Train transparency segmenters with polarization imagery as privileged supervision (available only at training time) and measure how much of the polarization advantage transfers to RGB-only inference.
**Problem:** Polarization cameras see glass through physical cues (polarized specular reflection) but will never be ubiquitous; whether their signal can be internalized by RGB models via privileged learning is untested.
**Core Hypothesis:** Polarization-privileged training transfers a substantial fraction of the polarization advantage to RGB inference—because polarization labels teach the model which subtle RGB cues (reflection gradients, boundary distortions) are transparency-diagnostic—outperforming RGB-only training at matched labels.
**Why Important:** A positive result gives the field a scalable recipe: capture small polarization corpora, train once, deploy on commodity cameras everywhere.
**Why Possibly Novel:** Privileged-modality learning for transparency (with transfer-fraction quantification) is unexplored.
**Minimal Experiment:** Capture or source paired polarization-RGB transparency data; train privileged vs RGB-only models; evaluate both on RGB test sets; quantify the transferred fraction.
**Main Risk:** The polarization advantage may reside in cues with no RGB correlate, yielding near-zero transfer.

### IDEA-B-0163 — Surgical narration as temporal-semantic supervision for scene segmentation
**One-sentence idea:** Align intraoperative verbal narration (already recorded in teaching hospitals) with surgical video to weakly supervise anatomy and instrument segmentation through mention-time co-occurrence.
**Problem:** Surgical video annotation requires scarce expert time, while thousands of hours of narrated procedures encode rich, time-stamped semantic descriptions that current pipelines discard.
**Core Hypothesis:** Narration-mention timing provides weak labels (what is visible and salient now) sufficient to train contrastive region-language alignment that improves downstream few-shot surgical segmentation substantially over video-only self-supervision at equal data.
**Why Important:** Taps an existing, ethically accessible supervision stream for one of the hardest-to-annotate domains in medical vision.
**Why Possibly Novel:** Narrated-procedure alignment has been used for step recognition, not for dense segmentation supervision.
**Minimal Experiment:** On narrated procedures with a small mask-annotated subset, pretrain with narration alignment vs video-only SSL; compare few-shot fine-tuning curves.
**Main Risk:** Narration lags and topical drift (discussing anatomy not on screen) inject temporal label noise.

### IDEA-B-0164 — The information content of expert gaze for lesion segmentation
**One-sentence idea:** Quantify how many bits of localization information radiologist eye-tracking provides per case, and test gaze-derived priors as a supervision source that requires zero additional expert effort beyond routine reading.
**Problem:** Every diagnostic read produces a gaze trajectory that dies unrecorded, while the field pays separately for localization labels containing partially redundant information.
**Core Hypothesis:** Gaze density maps carry substantial, quantifiable localization information about lesions (measured as reduction in localization entropy), and gaze-supervised pretraining plus few pixel labels matches pixel-only training with several-fold more labels—with the gaze value concentrated on subtle lesions where search is deliberate.
**Why Important:** Establishes passive expert-attention capture as a costless supervision channel for medical AI, with a principled information-theoretic valuation.
**Why Possibly Novel:** Gaze-as-supervision exists in small demos; information-content quantification and value-per-lesion-type analysis do not.
**Minimal Experiment:** On gaze-tracked reading datasets with masks, compute localization information metrics; train gaze-prior models across label budgets; identify where gaze value concentrates.
**Main Risk:** Gaze reflects search strategy and distractors, not just findings—noise structure needs modeling.

### IDEA-B-0165 — NIR-supervised smoke density with RGB deployment
**One-sentence idea:** Exploit near-infrared's differential smoke penetration to compute physically grounded smoke-density maps from NIR-RGB camera pairs, using them as automatic dense supervision for RGB-only smoke density estimation.
**Problem:** Smoke density ground truth is essentially unobtainable by human annotation (humans cannot judge optical depth), capping RGB smoke models at binary masks when applications need density.
**Core Hypothesis:** The NIR/visible transmission ratio yields density estimates accurate enough to supervise RGB models that then predict density from single RGB frames—generalizing beyond the paired-camera training sites because the physical relation is scene-independent.
**Why Important:** Elevates smoke perception from detection to quantification (visibility, spread modeling, exposure estimation) using automatically generated physical labels.
**Why Possibly Novel:** Cross-spectral physical self-labeling for dense smoke quantification has not been demonstrated.
**Minimal Experiment:** Deploy paired NIR-RGB rigs at smoke sources (controlled burns); derive density labels via transmission physics; train RGB density predictors; validate against transmissometer readings.
**Main Risk:** The NIR-visible relation varies with particle size distribution, complicating a universal density calibration.

### IDEA-B-0166 — Hallucination-aware weighting: making VLM-generated captions usable as dense supervision
**One-sentence idea:** Characterize the noise structure of VLM-generated image captions used as open-vocabulary segmentation supervision—especially object hallucinations—and test whether hallucination-probability weighting turns net-harmful caption supervision into net-positive.
**Problem:** Synthetic captions are the cheapest scaling route for language-supervised dense models, but VLMs hallucinate objects at significant rates, and hallucinated mentions teach models to segment absent things.
**Core Hypothesis:** Caption noise is structured (hallucinations concentrate on context-plausible objects) and predictable by lightweight verifiers, and down-weighting mentions by hallucination probability recovers most of the clean-caption training value from noisy captions—while naive use of the same captions measurably increases target-absent false positives.
**Why Important:** Determines whether the synthetic-caption scaling path is safe for dense prediction, with a concrete correction mechanism.
**Why Possibly Novel:** Hallucination-structured noise modeling for dense supervision (not caption quality in general) is unaddressed.
**Minimal Experiment:** Generate captions for labeled segmentation corpora; measure hallucination structure against GT; train open-vocab segmenters with naive vs weighted captions; compare novel-class recall and absent-target FP rates.
**Main Risk:** Verifier and captioner may share blind spots, leaving correlated hallucinations unweighted.

### IDEA-B-0167 — How much paired data does a text-to-prompt bridge need?
**One-sentence idea:** Learn a minimal bridge that maps text descriptions into SAM's prompt-embedding space—enabling text-prompted use of a frozen visual-only segmenter—and characterize the paired-data requirement curve for the bridge.
**Problem:** Text-promptable segmentation currently requires jointly trained large models, while an aligned bridge into an existing prompt space might need orders of magnitude less paired supervision—the actual requirement is unknown.
**Core Hypothesis:** Because SAM's prompt space is low-dimensional and structured, a text bridge trained on modest paired data (thousands, not millions, of region-text pairs) achieves a large fraction of jointly trained text-segmentation performance, with the data-requirement curve exhibiting sharp early saturation.
**Why Important:** A cheap bridge democratizes text-driven segmentation for domains (medical, industrial) that can never fund joint pretraining.
**Why Possibly Novel:** Prompt-space bridging with an explicit data-efficiency characterization has not been mapped.
**Minimal Experiment:** Train bridges on nested paired-data subsets; evaluate referring-segmentation transfer per subset size; locate the saturation knee.
**Main Risk:** Prompt space may lack the semantic axes needed for text specificity, capping bridge quality regardless of data.

### IDEA-B-0168 — Supervision phase transitions: contrastive-report pretraining versus pixel labels at scale
**One-sentence idea:** Map the two-dimensional performance surface of report-contrastive pretraining volume versus pixel-label fine-tuning volume for medical segmentation, testing for phase-transition-like regime changes in their marginal exchange rate.
**Problem:** Institutions must split budgets between amassing image-report pairs and commissioning pixel annotation, but the interaction structure of the two supervision types (substitutes, complements, regime-dependent) is unmeasured.
**Core Hypothesis:** The two supervision types are complements at low pixel-label counts (report pretraining multiplies label value) but near-perfect substitutes past a knee, with the knee position predictable from task granularity—yielding a budget-allocation rule with regime boundaries.
**Why Important:** Directly optimizes the largest cost line in medical AI development with a measured production function.
**Why Possibly Novel:** Two-axis supervision surfaces with regime analysis have not been mapped for dense medical tasks.
**Minimal Experiment:** Train across a grid of (report-pairs × pixel-labels) volumes on a task family; fit the surface; identify knees and validate the granularity predictor on a second task family.
**Main Risk:** Compute-intensive grid; interpolation from a sparse grid may miss sharp transitions.

### IDEA-B-0169 — Pulse-motion as free supervision for vascular segmentation in endoscopy
**One-sentence idea:** Amplify cardiac-cycle-locked micro-motion in endoscopic video to generate automatic vascular labels, using pulse-synchronous motion as a physiological supervision signal requiring no annotation.
**Problem:** Intraoperative vessel identification is safety-critical and annotation-starved, while video already contains a periodic physiological signal (pulsatile motion) that uniquely identifies vasculature.
**Core Hypothesis:** Cardiac-band motion magnification localizes pulsating vessels with precision sufficient to train static-frame vessel segmenters that detect even vessels whose pulsation is locally imperceptible—because training generalizes from motion-labeled to appearance-similar vessels.
**Why Important:** A zero-annotation route to intraoperative vessel safety systems, grounded in physiology rather than human labeling.
**Why Possibly Novel:** Physiological-periodicity-derived dense labels for surgical vision remain essentially unexplored.
**Minimal Experiment:** Apply cardiac-band video magnification to endoscopy with GT vessel annotations; measure harvested-label precision/recall; train static segmenters on harvested labels and evaluate against supervised baselines.
**Main Risk:** Camera and tissue motion swamp the cardiac band in much real footage; signal-recovery limits define applicability.

### IDEA-B-0170 — Learning from critique: textual error descriptions as a supervision channel
**One-sentence idea:** Train segmentation models on triples of (image, predicted mask, expert textual critique of the errors) to test whether natural-language error feedback improves aspects of mask quality that pixel-wise losses provably under-penalize.
**Problem:** Expert feedback in deployment arrives as language ("missed the inferior margin", "bleeding into the vessel") but training pipelines can only consume pixel corrections, discarding the cheapest and most abundant form of expert signal.
**Core Hypothesis:** Critique-conditioned refinement training improves precisely the error categories named in critiques (margin placement, topology violations) beyond what equal-effort pixel corrections achieve, because language identifies error type and location jointly at lower expert cost per unit information.
**Why Important:** Opens a scalable expert-in-the-loop channel matching how clinicians naturally communicate, with quantified cost-effectiveness.
**Why Possibly Novel:** Language-critique supervision for dense prediction (beyond instruction-following demos) with controlled cost-matched comparisons is new.
**Minimal Experiment:** Collect critiques on model outputs (cost-tracked); train critique-conditioned refiners vs pixel-correction baselines at matched expert minutes; compare per-error-category improvements.
**Main Risk:** Mapping free-text critiques to trainable signals may require structure that reduces the naturalness advantage.
### IDEA-B-0171 — Device sounds as instrument-usage labels for surgical scene understanding
**One-sentence idea:** Use the distinctive acoustic signatures of surgical devices (cautery buzz, suction, stapler clicks) as automatic temporal labels for which instruments are active, weakly supervising instrument segmentation and interaction detection in surgical video.
**Problem:** Instrument annotation in surgical video is expensive and usually ignores the active/idle distinction that matters for workflow analysis, while operating rooms are full of device sounds that encode exactly this information.
**Core Hypothesis:** Audio-detected device activations provide temporal supervision that, combined with motion cues, localizes active instruments well enough to train segmenters distinguishing active from idle tools—a capability pixel labels alone rarely capture—at near-zero labeling cost.
**Why Important:** Active-instrument understanding underlies surgical skill analysis and safety systems; audio makes it learnable from archives.
**Why Possibly Novel:** Device-acoustics-derived supervision for dense surgical vision has not been developed (distinct from narration, which encodes semantics rather than device state).
**Minimal Experiment:** On surgical videos with audio and instrument annotations, measure device-sound detection accuracy; train audio-anchored active-instrument segmenters; evaluate against supervised baselines.
**Main Risk:** OR audio is noisy and access-restricted; sound-to-instrument mapping varies across devices and rooms.

### IDEA-B-0172 — Multi-camera geometric consistency as free supervision in the operating room
**One-sentence idea:** Use cross-view mask consistency between calibrated multi-camera OR rigs as a label-free training signal, quantifying how much geometric consistency substitutes for manual annotation in surgical scene segmentation.
**Problem:** Modern ORs increasingly have multiple calibrated cameras, but each view is treated as independent data; the epipolar consistency between views is an unexploited supervision source.
**Core Hypothesis:** Enforcing cross-view consistency of predicted masks (through calibrated geometry) on unlabeled multi-view footage recovers a substantial fraction of the improvement that additional manual labels would provide, with the recovered fraction growing with viewpoint diversity.
**Why Important:** Converts existing OR camera infrastructure into a supervision multiplier for one of the most annotation-limited domains.
**Why Possibly Novel:** Multi-view consistency training is known in 3D vision, but its quantified value as annotation substitution in surgical segmentation is unmeasured.
**Minimal Experiment:** On multi-view surgical datasets with labels, train single-view baselines vs consistency-regularized models on unlabeled pairs; measure the label-equivalent value of consistency.
**Main Risk:** Non-rigid anatomy violates simple geometric consistency, requiring deformation-tolerant formulations.

### IDEA-B-0173 — Text versus clicks for resolving segmentation ambiguity
**One-sentence idea:** Measure whether a short text disambiguation ("the whole organ, not the lesion") resolves SAM-style multimask ambiguity more accurately and faster than the equivalent user effort in additional clicks.
**Problem:** Ambiguity resolution in interactive segmentation currently costs clicks, but text can express intent categories (whole vs part, which instance) that clicks encode only indirectly and slowly.
**Core Hypothesis:** For part-whole and instance-selection ambiguities, one text token of intent outperforms 2–3 disambiguation clicks in final accuracy per second of user time, while for boundary-placement ambiguity clicks dominate—yielding an ambiguity-type-to-modality routing rule.
**Why Important:** Grounded guidance for multimodal interactive interface design, replacing modality dogma with measured routing.
**Why Possibly Novel:** Ambiguity-type-stratified modality comparison at matched user cost has not been performed.
**Minimal Experiment:** User study over curated ambiguity cases; measure time and accuracy per modality per ambiguity type; derive and validate the routing rule.
**Main Risk:** Results depend on the text-understanding quality of the underlying model, dating quickly as models improve.

### IDEA-B-0174 — Does text supervision smooth away boundary precision? The semantic-blur hypothesis
**One-sentence idea:** Test whether adding language supervision to segmentation training systematically degrades boundary precision (language groups pixels semantically, not photometrically), quantifying a boundary-semantics tradeoff in multimodal training.
**Problem:** Language-supervised dense models are celebrated for semantic flexibility, but language never specifies boundaries, and its training pressure may actively blur them—an unmeasured cost side of the multimodal ledger.
**Core Hypothesis:** At matched region-level accuracy, models with heavier language supervision show measurably worse boundary-localized metrics, the degradation grows with text-loss weight in a dose-dependent way, and boundary-specific auxiliary supervision eliminates the tradeoff—demonstrating it is an objective-design artifact, not an inherent cost.
**Why Important:** Warns the field about a hidden regression in the rush toward language-native dense models and shows how to avoid it.
**Why Possibly Novel:** The boundary cost of language supervision has not been isolated with dose-response methodology.
**Minimal Experiment:** Train segmentation models across a text-loss-weight ladder at matched data; measure region-vs-boundary metric divergence; add boundary auxiliaries and re-measure.
**Main Risk:** Boundary degradation may be confounded with training-data mask quality differences across supervision sources.

### IDEA-B-0175 — Wind-conditioned plume priors: do meteorological inputs help or just bias?
**One-sentence idea:** Condition wildfire smoke segmentation on available meteorological data (wind vector, humidity) and test whether physical conditioning improves segmentation under visual ambiguity or merely biases predictions toward expected plume geometry.
**Problem:** Smoke appearance is visually ambiguous exactly when stakes are highest (thin, distant plumes), and free meteorological context could resolve ambiguity—or teach the model to hallucinate wind-aligned plumes.
**Core Hypothesis:** Meteorological conditioning improves detection of genuinely ambiguous plumes (verified on positives) while measurably increasing wind-aligned false positives on negatives—a quantifiable benefit-hallucination tradeoff whose net sign depends on prevalence, resolvable by conditioning only the candidate-scoring stage rather than the mask generator.
**Why Important:** Establishes the correct architecture point for injecting physical context into perception—a recurring design question in geo-aware vision.
**Why Possibly Novel:** Benefit-hallucination decomposition of context conditioning has not been measured for physical side information.
**Minimal Experiment:** Train with/without meteorological conditioning at different injection points; evaluate on ambiguous positives and wind-varied negatives separately; report the tradeoff surface.
**Main Risk:** Meteorological data resolution may be too coarse relative to camera scenes.

### IDEA-B-0176 — DICOM metadata as conditioning: exploiting the acquisition record nobody uses
**One-sentence idea:** Condition medical segmentation models on structured DICOM acquisition metadata (sequence parameters, contrast phase, window presets) and quantify how much free performance the routinely discarded acquisition record contains.
**Problem:** Every clinical image ships with a rich machine-readable acquisition description, yet models are trained to infer acquisition context from pixels, spending capacity on information already available for free.
**Core Hypothesis:** Metadata conditioning yields consistent gains concentrated on acquisition-sensitive tasks (contrast-phase-dependent lesion conspicuity), matching the performance of much larger unconditioned models, and its ablation quantifies exactly how much capacity pixel-based context inference currently consumes.
**Why Important:** A cost-free input channel with measurable value would change preprocessing standards across medical AI.
**Why Possibly Novel:** Systematic valuation of DICOM metadata as a conditioning signal (beyond series selection heuristics) is missing.
**Minimal Experiment:** Train matched models with/without metadata conditioning across tasks stratified by acquisition sensitivity; report gain profiles and capacity-equivalence estimates.
**Main Risk:** Metadata quality is inconsistent across institutions (missing fields, vendor idiosyncrasies).

### IDEA-B-0177 — Restain-and-register: immunohistochemistry as automatic ground truth for H&E segmentation
**One-sentence idea:** Generate automatic cell/structure labels for H&E histology by restaining the same physical slides with IHC markers and registering the pair, then characterize and correct the registration-induced label noise for training.
**Problem:** Histology annotation demands pathologist time and suffers known inter-rater problems, while chemistry can produce molecularly defined labels—if the registration noise between stains can be handled.
**Core Hypothesis:** Restain-registered IHC labels train H&E segmenters that match or exceed pathologist-annotation-trained models on molecularly verifiable targets, provided training explicitly models the spatially structured registration noise (which naive training does not tolerate).
**Why Important:** Offers molecular ground truth at chemistry cost instead of expert cost, potentially rebasing histology segmentation datasets.
**Why Possibly Novel:** Restain supervision exists in isolated efforts; the registration-noise-aware training treatment and head-to-head against expert labels are undeveloped.
**Minimal Experiment:** Produce restained-registered pairs for one marker; quantify registration noise structure; train noise-aware vs naive vs expert-labeled models; compare on independent molecular validation.
**Main Risk:** Restaining alters tissue subtly, and some targets lack clean IHC markers.

### IDEA-B-0178 — LiDAR dropout as volumetric weak labels for camera smoke perception
**One-sentence idea:** Use the systematic degradation of LiDAR returns in smoke (dropouts, range artifacts) as automatic volumetric weak labels to supervise camera-based smoke segmentation and density estimation on autonomous-platform logs.
**Problem:** Vehicles and drones log synchronized camera-LiDAR data through smoke events, but the LiDAR channel's physical response to particulates is discarded rather than exploited as a labeling signal for the camera channel.
**Core Hypothesis:** LiDAR return-statistics anomalies localize smoke volumes accurately enough that projected weak labels train camera smoke segmenters approaching manually supervised performance on platform imagery, with density supervision (from return-attenuation magnitude) as a free byproduct.
**Why Important:** Turns every smoke traversal by a sensor-equipped platform into training data, compounding across fleets.
**Why Possibly Novel:** LiDAR-degradation-derived supervision for visual smoke perception is essentially unexplored.
**Minimal Experiment:** On synchronized logs containing smoke, derive dropout-based labels; validate against human annotation; train camera models on projected labels and compare with supervised baselines.
**Main Risk:** Rain, dust, and exhaust produce similar LiDAR signatures, contaminating the label channel.

### IDEA-B-0179 — Atlas-as-prompt: injecting anatomical priors through the prompt interface instead of the loss
**One-sentence idea:** Compare injecting probabilistic anatomical atlas information as spatial prompts to a frozen promptable segmenter against the classical approach of atlas-based loss regularization during fine-tuning.
**Problem:** Anatomical priors are traditionally baked in through training objectives, which requires training and entangles the prior with the weights; promptable models offer an inference-time prior-injection channel whose relative power is unknown.
**Core Hypothesis:** Atlas-derived prompts (registered organ-probability peaks as point/box prompts with soft weighting) capture most of the benefit of atlas-regularized fine-tuning with zero training, and remain robust where registration is good while degrading gracefully—unlike trained priors, which fail silently on atypical anatomy.
**Why Important:** Inference-time priors are auditable, updatable, and per-case controllable—properties regulated medical software strongly prefers over baked-in priors.
**Why Possibly Novel:** The prompt interface as a prior-injection mechanism, compared head-to-head with loss-based priors, is a new framing.
**Minimal Experiment:** Implement atlas-to-prompt conversion; compare against atlas-loss fine-tuning and no-prior baselines across normal and atypical-anatomy test strata.
**Main Risk:** Prompt bandwidth may be too narrow to convey full spatial prior distributions.

### IDEA-B-0180 — Path dependence of multimodal supervision order
**One-sentence idea:** Test whether the order of applying supervision modalities (text-alignment first versus pixel-mask first) changes the final dense-prediction quality of multimodal models at fixed total data and compute, revealing path dependence in multimodal optimization.
**Problem:** Multimodal training recipes fix an ordering by convention (usually language-alignment first), and the field cannot distinguish whether observed capabilities stem from data content or ordering effects.
**Core Hypothesis:** Order matters measurably: pixel-first training establishes boundary-preserving features that survive subsequent language alignment, while text-first training reaches equal region metrics but persistently inferior boundary metrics—demonstrating non-commutativity of supervision types.
**Why Important:** Recipe orderings are being locked into expensive pretraining runs across the industry without evidence; a non-commutativity result would change how multimodal curricula are designed.
**Why Possibly Novel:** Controlled supervision-order experiments for dense multimodal models are absent.
**Minimal Experiment:** Train matched models under both orderings (and interleaved control) on identical data; compare region, boundary, and grounding metrics; replicate at two scales.
**Main Risk:** Conclusions may depend on the relative volumes of the two supervision types.

### IDEA-B-0181 — Spoken corrections: language as a real-time mask-editing channel
**One-sentence idea:** Test whether spoken relative corrections ("extend it down", "too far left") can drive mask editing at competitive time-to-quality with mouse-based correction in sterile or hands-busy environments.
**Problem:** Surgeons and radiologists often cannot touch pointing devices mid-procedure, leaving no viable correction channel for interactive segmentation exactly where it is most needed.
**Core Hypothesis:** A mapping from relative spatial language to prompt-space edits achieves clinically useful correction (measured as time-to-target-quality) within a modest factor of mouse correction, with the gap closing when corrections are categorical (add/remove region) rather than metric (exact boundary placement).
**Why Important:** Voice is the only universally available sterile interaction channel; quantifying its dense-editing viability determines whether interactive segmentation can enter procedure rooms.
**Why Possibly Novel:** Voice-driven dense mask editing with quantitative time-to-quality comparison has not been studied.
**Minimal Experiment:** Build a speech-to-prompt-edit interface over a promptable segmenter; run within-subject corrections studies (voice vs mouse) across correction types; report time-quality curves.
**Main Risk:** Speech recognition errors in noisy clinical environments may dominate the interaction cost.

### IDEA-B-0182 — Absence statements as supervision: teaching models what is not there
**One-sentence idea:** Exploit explicit negative findings in radiology reports ("no pneumothorax", "no focal lesion") as verified-absence supervision, testing whether absence-aware training reduces hallucinated segmentations more effectively than positive-only training augmented with generic negatives.
**Problem:** Reports certify absence with expert authority—information no image-only pipeline possesses—yet current text-mining pipelines discard negative findings, and models hallucinate exactly the findings experts explicitly ruled out.
**Core Hypothesis:** Absence-supervised training reduces false-positive segmentation of the certified-absent classes substantially more than equal volumes of unlabeled or randomly negative data, because certified absence provides class-specific hard negative supervision at the image level.
**Why Important:** False positives drive alarm fatigue and clinical distrust; certified-absence mining is a free, targeted remedy at hospital scale.
**Why Possibly Novel:** Negation-mined, class-specific absence supervision for dense prediction is undeveloped (negation is studied for classification labels, not dense hallucination control).
**Minimal Experiment:** Mine negative findings from reports; train with/without absence losses; measure class-conditional FP rates on certified-absent test cases and overall sensitivity for balance.
**Main Risk:** Report negations are sometimes hedged or wrong; negation-extraction quality bounds the supervision purity.

### IDEA-B-0183 — Flow-discontinuity boundaries: motion as a boundary teacher for deforming smoke
**One-sentence idea:** Use optical-flow discontinuity surfaces in smoke video as automatic boundary supervision, testing whether motion-derived boundaries teach better smoke edges than intensity-derived pseudo-labels.
**Problem:** Smoke boundaries are nearly invisible in single frames (low contrast, translucency) but often become apparent through differential motion against the background—information static pseudo-labeling pipelines never access.
**Core Hypothesis:** Flow-discontinuity-derived boundary labels are complementary to appearance-based pseudo-labels (correcting different error regions), and boundary-supervised training with motion labels improves static-frame smoke segmentation, transferring the motion knowledge into appearance features.
**Why Important:** Provides a self-supervision channel specific to the amorphous, low-contrast targets where standard pseudo-labeling fails worst.
**Why Possibly Novel:** Motion-boundary supervision has been used for rigid objects; its transfer-to-static-inference formulation for amorphous deforming media is unexplored.
**Minimal Experiment:** Extract flow-discontinuity boundaries on smoke video; measure their accuracy against annotation; train static segmenters with motion-derived vs appearance-derived supervision; compare error geographies.
**Main Risk:** Flow estimation itself degrades inside smoke, making the supervision noisiest where it is most needed.

### IDEA-B-0184 — Contrast-enhancement differencing as automatic vessel ground truth—and its hidden bias
**One-sentence idea:** Use registered pre/post-contrast CT differencing to generate automatic vessel labels at scale, and characterize the systematic bias this induces (only perfused vessels enhance) on models trained from such labels.
**Problem:** Contrast physics offers free, precise vessel labels, but the labeling mechanism is physiologically selective—occluded and hypo-perfused vessels never enhance—creating a training signal whose bias directly opposes key clinical use cases (finding occlusions).
**Core Hypothesis:** Models trained on enhancement-derived labels inherit measurable blindness to non-enhancing vessel segments (quantified on occlusion-annotated test sets) even while excelling on healthy vasculature, and mixing a small fraction of expert-labeled pathological cases disproportionately corrects the bias.
**Why Important:** Documents a paradigmatic case of physically generated labels encoding a clinically dangerous selection bias—and prices the correction.
**Why Possibly Novel:** The perfusion-selection bias of contrast-derived supervision has not been isolated and quantified.
**Minimal Experiment:** Build enhancement-derived labels; train and evaluate on healthy and occlusion-rich test strata; sweep the corrective fraction of expert pathological labels.
**Main Risk:** High-quality registration of pre/post-contrast series is itself error-prone near vessels.

### IDEA-B-0185 — Knowledge conflict in VLM segmenters: when text priors contradict image evidence
**One-sentence idea:** Construct controlled conflicts between linguistic anatomical priors ("the liver is homogeneous") and image evidence (nodular cirrhotic liver) to measure which source dense VLMs trust, and whether the arbitration is calibrated to evidence strength.
**Problem:** Language-supervised dense models import textual world knowledge whose priors can contradict individual images—the arbitration behavior is unknown but determines safety on atypical (i.e., diseased) cases, which are exactly the cases that matter.
**Core Hypothesis:** Dense VLMs systematically over-trust text priors when image evidence is degraded (noise, low contrast), producing prior-conforming segmentations of atypical anatomy, and the over-trust is measurable as miscalibrated evidence weighting that worsens with language-model scale.
**Why Important:** "Regression toward the textbook" on abnormal cases is the most dangerous conceivable failure mode for medical VLMs.
**Why Possibly Novel:** Knowledge-conflict methodology from NLP has not been ported to dense medical grounding.
**Minimal Experiment:** Assemble typical/atypical anatomy pairs with matched image quality ladders; measure prior-conformity of segmentations versus evidence strength; compare across model scales.
**Main Risk:** Constructing convincing conflict cases requires clinical curation to avoid strawman stimuli.

---

## Cluster 6 — Synthetic Data Pitfalls (IDEA-B-0186 … IDEA-B-0215)

### IDEA-B-0186 — Does generative augmentation actually cover the tail it promises to fix?
**One-sentence idea:** Measure the mode coverage of diffusion-generated medical images against the true long tail of pathology presentations, testing whether synthesis concentrates near dataset modes precisely where data was never scarce.
**Problem:** Synthetic data is prescribed as the cure for rare presentations, but generators are trained on the same skewed distributions and may reproduce the skew—delivering volume without coverage.
**Core Hypothesis:** Synthetic pathology images occupy a measurably narrower support than real data (quantified by coverage metrics on curated rare-presentation references), and segmentation gains from synthetic augmentation concentrate on already-common presentations while rare-presentation performance is unchanged or harmed.
**Why Important:** If synthesis fails exactly on the tail, the field's main data-scarcity remedy is a placebo for its stated purpose—an urgent measurement.
**Why Possibly Novel:** Tail-coverage auditing of medical generative augmentation (against clinically curated rarity strata) has not been performed.
**Minimal Experiment:** Curate rarity-stratified references; compute generator coverage per stratum; train with synthetic augmentation; report per-stratum (not mean) segmentation deltas.
**Main Risk:** Defining clinically meaningful rarity strata requires expert partnership.

### IDEA-B-0187 — What matters in rendering transparency: optical fidelity or context realism?
**One-sentence idea:** Factorially disentangle physically accurate refraction/reflection rendering from context realism (backgrounds, clutter, lighting ecology) in synthetic training data for transparent-object segmentation.
**Problem:** Synthetic transparency pipelines spend heavily on physically based rendering, yet the transfer bottleneck might be the impoverished scene context around the glass rather than the glass optics themselves.
**Core Hypothesis:** Beyond a modest optical-fidelity threshold, context realism dominates sim-to-real transfer for transparency segmentation—cheap approximate optics in rich contexts beats path-traced optics in sterile contexts at equal rendering budget.
**Why Important:** Redirects synthetic-data budgets to whichever factor the evidence supports, across an application area where synthesis is the primary data source.
**Why Possibly Novel:** Optics-versus-context factorial ablation for transparency has not been isolated.
**Minimal Experiment:** Render a 2×3 grid (optics fidelity × context richness) at matched budget; train per cell; evaluate on real transparency benchmarks; attribute transfer variance.
**Main Risk:** Fidelity and context interact with specific renderer implementations, complicating clean factor separation.

### IDEA-B-0188 — Scattering statistics versus shape realism in simulated smoke
**One-sentence idea:** Test whether matching the optical scattering statistics of real smoke (phase functions, extinction spectra) matters more for sim-to-real segmentation transfer than matching plume shape dynamics from fluid simulation.
**Problem:** Smoke synthesis invests in expensive fluid dynamics for realistic shapes, while the radiative transfer that determines how smoke actually appears against backgrounds is often approximated crudely—the wrong priority if appearance statistics dominate transfer.
**Core Hypothesis:** Models trained on shape-simple but scattering-accurate smoke transfer better to real imagery than models trained on shape-realistic but scattering-naive smoke, because segmentation cues live in translucency gradients and background interaction, not silhouette dynamics.
**Why Important:** Establishes the correct fidelity budget allocation for all participatory-media synthesis (smoke, fog, dust, haze).
**Why Possibly Novel:** Radiometric-versus-morphological fidelity decomposition for participating-media training data is untested.
**Minimal Experiment:** Generate the 2×2 fidelity grid; train per cell; evaluate on real smoke benchmarks; attribute transfer to each fidelity axis.
**Main Risk:** Real-smoke evaluation sets have their own annotation ambiguity, adding noise to transfer measurement.

### IDEA-B-0189 — The inpainting fingerprint: do models learn the lesion or the paste?
**One-sentence idea:** Test whether segmentation models trained on lesions synthetically inpainted into healthy images learn to detect the generative fingerprint (boundary statistics, noise discontinuities) rather than lesion appearance, by evaluating on fingerprint-free presentations.
**Problem:** Inpainting-based augmentation reports strong in-benchmark gains, but if models key on synthesis artifacts, the gains are circular—the model detects the augmentation, not the disease.
**Core Hypothesis:** A detector can distinguish inpainted from real lesions at high accuracy using local statistics (proving a fingerprint exists), models trained on inpainted data degrade disproportionately on real-only test sets versus inpainted test sets, and artifact-suppressed synthesis (noise-matched blending) closes part of the circularity gap.
**Why Important:** Protects a rapidly spreading augmentation practice from a validity flaw that standard evaluation cannot see.
**Why Possibly Novel:** Fingerprint-circularity auditing of inpainting augmentation for dense medical tasks is not established practice.
**Minimal Experiment:** Train fingerprint detectors on inpainted-vs-real patches; compare augmented-model performance on real versus synthetic test lesions; test artifact-suppression variants.
**Main Risk:** Absence of a detectable fingerprint for the best generators would make the audit reassuring but unpublishable-negative in style (still scientifically valuable).

### IDEA-B-0190 — The synthetic poisoning threshold: robustness costs of synthetic fractions
**One-sentence idea:** Map how out-of-distribution robustness of segmentation models changes as the synthetic fraction of training data increases, testing for a threshold beyond which in-domain gains coexist with silent robustness degradation.
**Problem:** Synthetic fractions in training corpora are rising without monitoring of the robustness dimension—in-domain benchmarks may improve while the model increasingly fits generator-specific regularities.
**Core Hypothesis:** There exists a measurable synthetic-fraction threshold (generator- and task-dependent) beyond which corruption and cross-site robustness decline even as in-domain IoU rises, and the threshold is detectable without OOD labels via generator-classifier probes on the learned features.
**Why Important:** Provides the monitoring instrument the field needs before synthetic-heavy training becomes irreversible standard practice.
**Why Possibly Novel:** Robustness-versus-synthetic-fraction dose-response curves for dense prediction have not been mapped.
**Minimal Experiment:** Train across synthetic-fraction ladders with two generator families; evaluate in-domain, cross-site, and corruption metrics; test the probe-based threshold detector.
**Main Risk:** Thresholds may vary so strongly across generators that only the methodology (not the numbers) generalizes.

### IDEA-B-0191 — Error amplification in self-consuming segmentation pipelines
**One-sentence idea:** Measure the generational dynamics of pipelines where models pseudo-label data used to train successor models (the standard auto-labeling loop), quantifying which error types amplify, stay stable, or self-correct across generations.
**Problem:** Foundation-model auto-labeling has made recursive training loops ubiquitous in dense prediction, while the collapse dynamics studied for generative models have no dense-task analogue to guide practice.
**Core Hypothesis:** Boundary biases amplify geometrically across generations (each student sharpens its teacher's systematic offsets) while random errors wash out, so multi-generation loops drift toward confident, consistent, wrong boundaries—detectable early via generational bias-trend monitoring and preventable with small fresh-label injections whose required rate is measurable.
**Why Important:** Defines the stability conditions of the data flywheel the entire field is now building on.
**Why Possibly Novel:** Multi-generation error-dynamics measurement for dense-prediction self-training (as opposed to generative-model collapse) is largely unexplored.
**Minimal Experiment:** Run 5-generation loops on datasets with held-out truth; track error decomposition (bias vs variance, boundary vs region) per generation; test fresh-data injection rates.
**Main Risk:** Compute cost of multi-generation training; dynamics may depend on loop details (filtering, thresholds).

### IDEA-B-0192 — Does copy-paste augmentation erode context reasoning?
**One-sentence idea:** Test whether copy-paste augmentation—which deliberately violates context consistency—improves object-level robustness at the cost of degrading the model's use of legitimate context cues, measured via context-dependent test conditions.
**Problem:** Copy-paste is adopted for its recall gains, but its central mechanism (decorrelating objects from context) may teach models to ignore context even where context is diagnostically necessary (shadows for fire, surrounding tissue for lesions).
**Core Hypothesis:** Copy-paste-trained models show measurably reduced context sensitivity (smaller performance change under context randomization) and this transfers to real errors on context-dependent cases—camouflaged targets and low-contrast lesions where context is the only disambiguator.
**Why Important:** Quantifies a hidden cost of a near-universal augmentation, enabling informed rather than default use.
**Why Possibly Novel:** Context-reliance shift as a measured side effect of copy-paste has not been isolated.
**Minimal Experiment:** Train with/without copy-paste; measure context-randomization sensitivity and performance on context-dependent test strata; correlate the two shifts.
**Main Risk:** Reduced context reliance is sometimes desirable; the net verdict is task-dependent and must be reported per stratum.

### IDEA-B-0193 — Programmatic prompts versus human clicks: the prompt-distribution gap in SAM-style training
**One-sentence idea:** Measure the performance consequences of training promptable segmenters with programmatically sampled prompts (centroid points, tight boxes) rather than human-realistic prompt distributions, and characterize the resulting deployment gap.
**Problem:** SAM-style training samples prompts synthetically for scale, but deployment prompts come from humans with different spatial statistics; the training-deployment prompt mismatch is an unquantified domain gap inside the interaction channel itself.
**Core Hypothesis:** Models trained on programmatic prompts underperform measurably under human prompt distributions (especially early-click behavior on ambiguous targets), and training with a learned human-prompt model closes most of the gap at no additional annotation cost.
**Why Important:** The fix is nearly free (better prompt sampling), but only measurable motivation will change entrenched training recipes.
**Why Possibly Novel:** The prompt-sampling distribution as a training-design variable with deployment consequences has not been isolated.
**Minimal Experiment:** Collect human prompt logs; fit a prompt-distribution model; fine-tune segmenters with programmatic vs human-modeled prompts; evaluate under real human prompting.
**Main Risk:** Human prompt distributions vary across tools and expertise levels, complicating a single target distribution.

### IDEA-B-0194 — A taxonomy of error modes induced by different synthesis paradigms
**One-sentence idea:** Systematically characterize which distinct downstream error modes GAN-based, diffusion-based, and physics-simulation synthetic data each induce in trained ultrasound segmenters, replacing the "which generator is best" question with an error-mode attribution map.
**Problem:** Synthesis paradigms are compared on mean downstream metrics, obscuring the possibility that each injects characteristic, complementary failure signatures that mean scores cannot reveal.
**Core Hypothesis:** Each synthesis paradigm produces an identifiable error-mode signature in downstream models (e.g., diffusion: over-smoothed boundary priors; simulation: artifact-blindness to unmodeled physics; GAN: mode-restricted texture generalization), and the signatures are stable enough to guide paradigm mixing by error-mode complementarity.
**Why Important:** Enables engineering synthetic-data portfolios by predicted error compensation rather than aggregate scores.
**Why Possibly Novel:** Error-mode-level attribution of synthesis paradigms is absent from the synthetic-data literature.
**Minimal Experiment:** Train matched segmenters on each paradigm's data (and mixtures); evaluate on error-mode-stratified real test suites; test signature stability across tasks.
**Main Risk:** Signatures may be dominated by specific implementation choices rather than paradigm essence.

### IDEA-B-0195 — Does privacy-motivated synthetic replacement preserve subgroup fairness?
**One-sentence idea:** Audit whether replacing real medical training data with privacy-preserving synthetic data preserves performance equity across patient subgroups, testing the hypothesis that synthesis amplifies underrepresentation.
**Problem:** Synthetic replacement is promoted as the privacy solution for medical data sharing, but generators fit demographic majorities better, and a fairness-blind swap could institutionalize subgroup performance gaps at the dataset level.
**Core Hypothesis:** Models trained on synthetic replacements show subgroup performance gaps measurably wider than their real-data-trained counterparts, the widening is proportional to subgroup rarity in generator training data, and subgroup-conditioned generation with reweighting eliminates most of it.
**Why Important:** The privacy-fairness interaction must be measured before synthetic replacement becomes regulatory practice—afterward is too late.
**Why Possibly Novel:** Fairness auditing of synthetic-replacement pipelines for dense medical tasks is essentially unexamined.
**Minimal Experiment:** Train on real vs synthetic-replaced data with subgroup-stratified evaluation; regress gap widening on subgroup representation; test conditioned-generation mitigation.
**Main Risk:** Subgroup labels are themselves incomplete in many datasets, limiting audit resolution.

### IDEA-B-0196 — Hallucinated physics in text-to-image fire data
**One-sentence idea:** Audit text-to-image-generated wildfire imagery for physically impossible content (flame color–temperature violations, inconsistent smoke-wind shear, impossible illumination) and measure whether physics violations in training data degrade real-world detection reliability.
**Problem:** Prompt-generated fire imagery is an appealing source for rare scenarios (night crown fires, urban interface), but generators optimize plausibility to humans, not physics—and detectors may internalize the violations as valid fire signatures.
**Core Hypothesis:** A physics-rule auditor detects violations in a substantial fraction of generated fire images, models trained on unfiltered generations acquire measurable false-positive vulnerabilities aligned with the violation types (e.g., alarm on physically impossible flame colors in decorations), and physics-filtered training data removes the vulnerability at modest volume cost.
**Why Important:** Safety-critical detection trained on physically wrong data is a concrete, checkable hazard—and the filter is buildable now.
**Why Possibly Novel:** Physics-consistency auditing of generative training data for safety perception has not been formalized.
**Minimal Experiment:** Build rule-based physics auditors; quantify violation rates across generators; train on filtered vs unfiltered data; compare FP profiles on violation-aligned real distractors.
**Main Risk:** Physics rules cover only auditable violations; subtler statistical wrongness escapes rule-based filtering.

### IDEA-B-0197 — Which distribution statistics actually predict synthetic-to-real transfer?
**One-sentence idea:** Identify which measurable statistics of synthetic datasets (beyond FID) actually predict downstream real-world segmentation performance, by training across many synthetic variants and regressing transfer against candidate statistics.
**Problem:** Synthetic data quality is optimized against FID-style perceptual metrics that were designed for image realism, not task transfer—teams may be tuning generators toward the wrong objective entirely.
**Core Hypothesis:** Task-relevant statistics (boundary-contrast distributions, object-scale spectra, context co-occurrence matrices) predict transfer far better than perceptual realism scores, and FID-optimized generators are measurably suboptimal for transfer at equal compute—establishing a replacement objective family for task-oriented synthesis.
**Why Important:** Redirects generator development toward statistics that matter, potentially improving every synthetic-data pipeline without new generative technology.
**Why Possibly Novel:** Large-scale predictor identification for dense-task transfer (with FID as a tested competitor, not an assumption) has not been executed.
**Minimal Experiment:** Produce 30+ synthetic variants spanning statistic space; train matched segmenters; regress real-test performance on candidate statistics; validate the top predictor prospectively on new variants.
**Main Risk:** Predictor validity may be task-family-specific, requiring replication across task types.

### IDEA-B-0198 — The controllability-realism frontier: parametric anatomy versus learned generation
**One-sentence idea:** Map the frontier between controllable parametric anatomy simulation (explicit shape/pathology parameters) and realistic learned generation for producing segmentation training data, identifying which regions of the frontier maximize downstream value per sample.
**Problem:** Synthetic medical data comes from two philosophies—controllable-but-stylized simulation and realistic-but-uncontrollable generation—and the field lacks evidence on where the downstream-value optimum lies between them.
**Core Hypothesis:** Downstream value is maximized at hybrid points (parametric geometry with learned appearance synthesis), and the optimum shifts predictably toward controllability as target pathology rarity increases—because rare cases need guaranteed coverage more than photorealism.
**Why Important:** Provides a design map for the growing investment in medical data synthesis, indexed by the rarity of what must be synthesized.
**Why Possibly Novel:** The controllability-realism tradeoff has not been operationalized as a measurable frontier with downstream validation.
**Minimal Experiment:** Implement points along the frontier (pure parametric, hybrid, pure learned) for one anatomy; train per point across rarity-stratified targets; map value surfaces.
**Main Risk:** Frontier position estimates may be sensitive to the quality of each implementation rather than the paradigm.

### IDEA-B-0199 — Detecting compositional blind spots in generators before training on their output
**One-sentence idea:** Develop pre-training audits that detect a generator's compositional blind spots (attribute combinations it cannot produce, e.g., small+transparent+occluded) and test whether audit results predict downstream segmentation failures on exactly those compositions.
**Problem:** Generators fail silently on rare attribute combinations, synthetic datasets inherit the holes, and downstream models fail on the same compositions—but the chain is only discovered after deployment failures.
**Core Hypothesis:** Compositional coverage of a generator is measurable by structured prompting plus attribute verification, coverage holes predict downstream per-composition performance with useful accuracy, and hole-targeted real-data collection (guided by the audit) is severalfold more efficient than uniform collection.
**Why Important:** Converts synthetic-data risk management from reactive to predictive with an auditable procedure.
**Why Possibly Novel:** Compositional-coverage auditing as a predictive instrument for dense-task synthetic pipelines is new.
**Minimal Experiment:** Audit two generators over attribute grids; train on their outputs; correlate per-composition downstream performance with audited coverage; test guided-collection efficiency.
**Main Risk:** Attribute verification models have their own blind spots, potentially aligned with the generator's.

### IDEA-B-0200 — Too-clean ground truth: when perfect synthetic labels teach the wrong tolerance
**One-sentence idea:** Test whether the pixel-perfect labels of rendered data teach segmentation models boundary-tolerance expectations that mismatch real-world annotation conventions, and whether deliberately degrading synthetic labels toward realistic annotator statistics improves real-data performance.
**Problem:** Synthetic pipelines celebrate their perfect geometric labels, but models fine-tuned or evaluated against human-annotated data face systematically looser, convention-laden boundaries—a mismatch in the label-generating process itself.
**Core Hypothesis:** Models trained on geometrically perfect synthetic labels develop over-sharp boundary posteriors that are miscalibrated against human-annotated evaluations, and injecting realistic annotator-noise models into synthetic labels (matched to target-dataset conventions) improves both accuracy and calibration on real benchmarks.
**Why Important:** Identifies an inverted data-quality intuition—sometimes worse labels train better models for the actual evaluation regime.
**Why Possibly Novel:** Deliberate label-realism engineering (annotator-noise simulation on synthetic GT) is an unexplored design dimension.
**Minimal Experiment:** Train on perfect vs annotator-noise-matched synthetic labels; evaluate on human-annotated real data measuring accuracy and boundary-confidence calibration; compare across noise models.
**Main Risk:** The effect may be small relative to the synthetic-real appearance gap it rides on.

### IDEA-B-0201 — Generated hard negatives: do they patch decision boundaries or warp them?
**One-sentence idea:** Use prompted diffusion generation to synthesize targeted hard negatives (steam for smoke detectors, benign mimics for lesion detectors) and measure whether they reduce false positives cleanly or introduce new decision-boundary artifacts elsewhere.
**Problem:** Hard negatives are the scarcest data class (rare confusable phenomena), generation can supply them on demand, but training on synthetic negatives may teach generator-artifact-based discrimination rather than genuine phenomenon discrimination.
**Core Hypothesis:** Synthetic hard negatives reduce false positives on the targeted confusion measurably, but a fraction of the reduction stems from artifact detection (verifiable by testing on real confusers), and the artifact dependence is removable by cross-generator negative mixing.
**Why Important:** Prices the real value of the most operationally attractive use of generative data—on-demand negatives for safety systems.
**Why Possibly Novel:** Artifact-decomposed evaluation of synthetic negative training has not been done.
**Minimal Experiment:** Generate steam/mimic negatives; train with them; evaluate FP reduction on real confusers vs synthetic confusers separately; test cross-generator mixing.
**Main Risk:** Real confuser test sets (real steam near infrastructure) are themselves scarce, limiting verification resolution.

### IDEA-B-0202 — Acquisition-space versus image-space synthesis for MRI artifacts
**One-sentence idea:** Test whether synthesizing MRI training-data variation at the acquisition level (k-space corruption, undersampling, coil sensitivity) transfers better to real artifact robustness than visually equivalent image-space augmentation.
**Problem:** MRI artifacts arise from acquisition physics with characteristic global structure, but augmentation pipelines imitate them with local image-space filters—two generative processes that can look similar while differing in exactly the statistics models learn.
**Core Hypothesis:** Acquisition-space synthesis yields measurably better robustness to real scanner artifacts than image-space imitations matched for visual similarity, because artifact phase structure and spatial correlations (which models exploit) are only correct in k-space generation.
**Why Important:** Determines whether medical augmentation must be physics-native—a significant engineering-investment question for every modality.
**Why Possibly Novel:** Controlled acquisition-space versus image-space augmentation comparisons with matched visual statistics are missing.
**Minimal Experiment:** Build matched artifact ladders both ways; train per ladder; evaluate on real artifact-affected scans; compare robustness profiles.
**Main Risk:** Real artifact-labeled evaluation data is limited; may need prospective collection with scanner cooperation.

### IDEA-B-0203 — Which randomization axes matter? Attribution for surgical sim-to-real
**One-sentence idea:** Decompose domain-randomization value for surgical-tool segmentation across its axes (lighting, tissue texture, tool material, kinematic pose priors, camera model), measuring each axis's marginal transfer contribution instead of randomizing everything blindly.
**Problem:** Domain randomization is applied as an undifferentiated bundle at maximal strength, wasting rendering budget on axes that contribute nothing and possibly diluting the ones that matter.
**Core Hypothesis:** Transfer value is concentrated in a small subset of randomization axes (predicted: specular/lighting and camera-model axes dominate; texture diversity contributes marginally), and axis-optimized randomization at half the rendering budget matches full randomization.
**Why Important:** Rationalizes synthetic-data engineering for surgical vision, where rendering budgets are significant and transfer is the entire game.
**Why Possibly Novel:** Marginal-attribution methodology for randomization axes (leave-one-axis-out at scale) is rarely executed rigorously.
**Minimal Experiment:** Render leave-one-axis-out and single-axis datasets at matched budget; train per condition; evaluate on real surgical footage; compute axis attributions.
**Main Risk:** Axis interactions may defeat clean marginal attribution, requiring factorial subsets.

### IDEA-B-0204 — Provenance laundering: is restricted-data ancestry detectable through synthetic intermediaries?
**One-sentence idea:** Test whether models trained purely on synthetic data—generated by a generator that was itself trained on restricted datasets—retain statistically detectable traces of the restricted ancestry, informing both auditing capability and privacy claims.
**Problem:** Synthetic data is marketed as severing legal/privacy links to source data, but if downstream models measurably inherit source-specific statistics through the generator, both compliance claims and audit mechanisms need rethinking.
**Core Hypothesis:** Membership and dataset-inference attacks succeed above chance against models trained only on synthetic intermediaries (ancestry leaks through the generator), with leakage strength growing with generator overfitting and detectable by dataset-level canary insertion.
**Why Important:** The answer determines whether synthetic intermediaries genuinely provide privacy/licensing insulation—a question regulators and hospitals are actively deciding on assumption rather than evidence.
**Why Possibly Novel:** Two-hop provenance detection (source→generator→downstream model) has barely been studied for dense-prediction pipelines.
**Minimal Experiment:** Train generators on datasets with inserted canaries; train segmenters on generator output only; run dataset-inference and canary-detection attacks on the segmenters.
**Main Risk:** Negative results (no detectable leakage) are consistent with either true insulation or weak attacks—needs attack-strength calibration.
### IDEA-B-0205 — Counterfactual pairs versus independent samples: the value of paired training data
**One-sentence idea:** Use diffusion-based editing to create matched counterfactual training pairs (same scene with and without smoke/lesion) and test whether paired training teaches invariance and sensitivity more sample-efficiently than the same volume of independent examples.
**Problem:** Standard training data varies everything at once between samples, forcing models to learn what matters statistically; counterfactual pairs isolate the target factor explicitly, but their training value has not been quantified against volume-matched independent data.
**Core Hypothesis:** Counterfactual-pair training achieves matched performance with substantially fewer samples (an effective-sample multiplier) and yields measurably better target-absent specificity, because pairs directly supervise the decision boundary rather than its statistical shadow.
**Why Important:** If pairs carry a large multiplier, editing-based data engineering beats volume scaling for rare-target tasks—a strategic redirection.
**Why Possibly Novel:** Volume-matched paired-versus-independent training comparisons for dense prediction have not been reported.
**Minimal Experiment:** Build edit-based pairs (with edit-artifact controls); train pair-supervised vs independent-sample models at matched volumes; measure the efficiency multiplier and specificity gains.
**Main Risk:** Edit artifacts could serve as shortcuts; artifact controls (edited-but-unchanged pairs) are essential.

### IDEA-B-0206 — Frequency-fingerprint reliance: do synthetic-trained models depend on generator artifacts?
**One-sentence idea:** Measure whether segmentation models trained on synthetic data lose their apparent robustness when generator-specific frequency fingerprints are filtered out at test time, quantifying artifact reliance as a hidden component of synthetic-data gains.
**Problem:** Synthetic-trained models are evaluated on real data (fingerprint-free) or synthetic data (fingerprint-present) but never on fingerprint-manipulated inputs, leaving unknown how much of the learned function keys on generation artifacts.
**Core Hypothesis:** A measurable fraction of synthetic-data performance gains disappears under fingerprint-removal filtering of synthetic test data, artifact reliance grows with the synthetic fraction in training, and fingerprint-randomized training (spectral augmentation of synthetic images) forces artifact-free learning at small cost.
**Why Important:** Separates real knowledge transfer from artifact fitting in the fastest-growing training-data source in the field.
**Why Possibly Novel:** Fingerprint-intervention testing of downstream (non-forensic) models has not been standard methodology.
**Minimal Experiment:** Identify generator fingerprints spectrally; evaluate synthetic-trained models on fingerprint-removed inputs; sweep synthetic fractions; test fingerprint-randomized training.
**Main Risk:** Fingerprint removal may also remove genuine high-frequency content, requiring careful matched controls.

### IDEA-B-0207 — Joint scaling laws for real and synthetic data
**One-sentence idea:** Fit a joint scaling law for segmentation performance as a function of real-data volume and synthetic-data volume, estimating the marginal substitution rate between them and how it evolves with scale.
**Problem:** Teams decide real-versus-synthetic budget splits with no quantitative model of their interaction—whether synthetic data substitutes for real at a stable rate, a decaying rate, or becomes worthless past a threshold is unknown.
**Core Hypothesis:** Performance follows a two-resource scaling law in which synthetic data's substitution rate decays with real-data volume (synthetic helps most when real data is scarce) and asymptotes to zero or negative, with law parameters transferable enough across related tasks to support budget planning.
**Why Important:** Scaling laws changed how language-model compute is planned; a data-composition law would do the same for dense-vision data budgets.
**Why Possibly Novel:** Two-resource (real×synthetic) scaling-law fitting for dense prediction has not been published.
**Minimal Experiment:** Train across a log-spaced (real × synthetic) grid on two task families; fit candidate law forms; test extrapolation accuracy on held-out grid points.
**Main Risk:** Law parameters may vary strongly with generator quality, dating the numeric results quickly (the methodology persists).

### IDEA-B-0208 — Occlusion-generalization phase transitions revealed by controllable rendering
**One-sentence idea:** Use rendering's precise control of occlusion rates to map how segmentation generalization across occlusion levels behaves—testing for sharp phase-transition-like failures invisible in real data where occlusion cannot be controlled.
**Problem:** Occlusion robustness is characterized anecdotally because real data offers no way to sweep occlusion systematically while holding everything else fixed—leaving unknown whether generalization degrades smoothly or collapses at thresholds.
**Core Hypothesis:** Models trained below a critical occlusion rate exhibit sharp (non-linear) performance collapse when tested above it, the critical rate is architecture-dependent (query-based decoders tolerate more), and training with a small fraction of super-critical occlusion examples eliminates the transition—an actionable curriculum prescription.
**Why Important:** Occlusion is a dominant failure source in surgical, robotic, and crowd domains; knowing the transition structure changes training-data design.
**Why Possibly Novel:** Controlled occlusion-sweep methodology and the phase-transition question have not been examined for segmentation.
**Minimal Experiment:** Render occlusion-swept datasets; train on capped-occlusion subsets; evaluate across the sweep; locate and characterize transitions across architectures.
**Main Risk:** Rendered occlusion statistics may miss real-world occluder correlations (tools occlude tissue non-randomly).

### IDEA-B-0209 — Compositing-statistics overfitting in matting-based smoke synthesis
**One-sentence idea:** Test whether smoke segmenters trained on alpha-matte-composited synthetic imagery overfit the compositing statistics (edge blending, color transfer) rather than smoke appearance, by evaluating against composites made with alternative compositing pipelines and real smoke.
**Problem:** Compositing real smoke plumes onto new backgrounds is the dominant cheap synthesis method for smoke data, but the composite operation itself has learnable statistics that real smoke lacks.
**Core Hypothesis:** Models trained on one compositing pipeline degrade measurably on identical smoke content composited by a different pipeline (proving compositing-statistics reliance), and the reliance predicts the real-data transfer gap better than smoke-content realism measures.
**Why Important:** Diagnoses why compositing-trained smoke models underdeliver in deployment and identifies the pipeline (not content) as a hidden factor to randomize.
**Why Possibly Novel:** Compositing-pipeline sensitivity as a measured confound in synthetic training is unexamined.
**Minimal Experiment:** Composite identical smoke assets via 3 pipelines; run the 3×3 train-test matrix plus real-data evaluation; correlate cross-pipeline drops with real transfer gaps.
**Main Risk:** Pipeline differences may be too subtle to matter for modern augmentation-heavy training.

### IDEA-B-0210 — Site-specific digital twins versus generic synthetic data
**One-sentence idea:** Quantify the marginal value of deployment-site-specific synthetic data (rendered from a 3D scan of the actual site with its actual camera) over generic synthetic data for fixed-camera monitoring tasks like fire detection.
**Problem:** Synthetic data is generated generically for economies of scale, but fixed-camera deployments have fully knowable geometry, backgrounds, and optics—personalization value that has never been priced.
**Core Hypothesis:** Site-twin synthetic data reduces false positives severalfold relative to volume-matched generic synthetic data (background-specific confusers get trained away), with the advantage concentrated in FP reduction rather than sensitivity, and amortizing twin-construction cost across a camera network is favorable above a computable network size.
**Why Important:** Provides the cost-benefit analysis for an operationally concrete decision facing every monitoring-network operator.
**Why Possibly Novel:** Site-personalized synthesis valuation with FP/TP decomposition has not been published.
**Minimal Experiment:** Build twins for 3 instrumented sites; train site-twin vs generic vs mixed; evaluate on real site footage; decompose gains and model amortization.
**Main Risk:** Twin fidelity (vegetation change, seasonal drift) decays, requiring maintenance-cost inclusion.

### IDEA-B-0211 — Label validity under latent-space augmentation
**One-sentence idea:** Measure how far latent-space augmentations (perturbing diffusion latents of training images) can push appearance variation before the paired segmentation masks become invalid, establishing safe operating envelopes for the practice.
**Problem:** Latent augmentation generates diverse variants cheaply, but unlike geometric transforms, its effect on label validity is unquantified—objects can move, deform, or vanish while the mask stays fixed.
**Core Hypothesis:** Mask validity decays measurably with latent perturbation magnitude at rates that vary by content type (amorphous targets tolerate less than rigid ones), a lightweight validity checker (mask-image consistency scoring) predicts invalid pairs reliably, and validity-filtered latent augmentation outperforms both unfiltered augmentation and conventional augmentation at matched compute.
**Why Important:** Converts an appealing but risky augmentation family into a controlled tool with known safety margins.
**Why Possibly Novel:** Label-validity dose-response measurement for generative augmentation has not been systematized.
**Minimal Experiment:** Sweep latent perturbation magnitudes; measure mask validity via human audit and automated scoring; train with filtered/unfiltered variants; compare downstream metrics.
**Main Risk:** Validity checking models may share failure modes with the generator being checked.

### IDEA-B-0212 — Fitting the simulator to reality: parameter estimation versus randomization
**One-sentence idea:** Test whether automatically fitting simulator parameters to unlabeled real target data (matching feature statistics) produces better segmentation transfer than the field-standard alternative of randomizing over broad parameter ranges.
**Problem:** Domain randomization concedes ignorance of true parameters by covering everything, paying a diversity tax; simulator fitting promises precision but risks overfitting to the feature statistics used for matching—the tradeoff is unresolved.
**Core Hypothesis:** Sim-fitting beats randomization when the simulator's parameter space contains a good approximation of reality (measurable post hoc by fit residuals) and loses otherwise, so the fit residual itself predicts which strategy to use per deployment—unifying the two approaches under a diagnostic.
**Why Important:** Replaces a philosophical debate (randomize vs calibrate) with a measurable decision rule for synthetic-data pipelines.
**Why Possibly Novel:** Residual-conditioned strategy selection between fitting and randomization has not been formalized.
**Minimal Experiment:** Across simulators of varying expressiveness and real targets, run fitting and randomization arms; correlate transfer outcomes with fit residuals; validate the decision rule prospectively.
**Main Risk:** Feature-statistic matching objectives may be gameable by degenerate parameter settings.

### IDEA-B-0213 — Synthetic validation sets: can model selection outsource to generated data?
**One-sentence idea:** Test whether synthetic data, even when inadequate for training, can serve for model selection and hyperparameter tuning—measuring the rank correlation between synthetic-validation and real-validation performance across checkpoint populations.
**Problem:** Real labeled validation data is often the scarcest resource (it must be held out from tiny label budgets), while validation demands less of data fidelity than training does—an asymmetry nobody has exploited systematically.
**Core Hypothesis:** Synthetic-validation ranking correlates strongly with real-validation ranking for coarse decisions (architecture, augmentation) but breaks down for fine decisions (early stopping, threshold selection), and the breakdown point is predictable from the synthetic-real feature distance—enabling a validated hybrid protocol that reallocates real labels from validation to training.
**Why Important:** Frees scarce real labels for training across every low-data project, if the protocol's limits are mapped honestly.
**Why Possibly Novel:** Synthetic data's differential adequacy for validation versus training is an unexamined asymmetry.
**Minimal Experiment:** Generate synthetic validation sets for 3 tasks; rank large checkpoint populations on both; measure rank correlation by decision granularity; test the reallocation protocol end to end.
**Main Risk:** Selection decisions correlated with synthetic-real gaps (e.g., augmentation choices) may be systematically misranked.

### IDEA-B-0214 — Memorization versus augmentation value in medical diffusion models
**One-sentence idea:** Jointly measure patient-data memorization and downstream augmentation value as functions of diffusion-model training (duration, data size, regularization), mapping the tradeoff frontier between privacy risk and synthetic utility.
**Problem:** The same overfitting that makes generators memorize (and potentially re-identify) patients may also make their outputs most realistic—if privacy risk and utility are coupled, privacy-safe operating points must be located, not assumed.
**Core Hypothesis:** Memorization and augmentation value are positively coupled through training progression but decouple under appropriate regularization (differential-privacy training, data deduplication), yielding operating points with near-maximal utility at near-minimal extraction risk—which can be certified with standardized extraction attacks.
**Why Important:** Provides the evidence base for policies on sharing medical generative models—currently written without measured tradeoff curves.
**Why Possibly Novel:** Joint memorization-utility frontier mapping for medical dense-prediction augmentation has not been done.
**Minimal Experiment:** Train diffusion models across regularization/duration grids; run extraction attacks and downstream augmentation evaluations per grid point; map the joint frontier.
**Main Risk:** Extraction-attack strength bounds the privacy-side measurement; conclusions are attack-relative.

### IDEA-B-0215 — Does multi-generator mixing cancel artifacts? Testing the decorrelation hypothesis
**One-sentence idea:** Test whether mixing synthetic data from multiple independent generators decorrelates their individual artifacts—yielding models free of any single generator's fingerprint reliance—or whether models simply learn the union of artifacts.
**Problem:** A natural remedy for generator-artifact overfitting is diversification across generators, but whether artifact effects average out (decorrelation) or accumulate (union learning) determines if the remedy works, and no evidence exists either way.
**Core Hypothesis:** Artifact reliance measured by fingerprint-intervention tests decreases superlinearly with generator count when generators are architecturally diverse, but plateaus when generators share architectural families (correlated fingerprints)—making generator-family diversity, not count, the operative variable.
**Why Important:** Provides the mixing recipe for the synthetic-data supply chains being built now, grounded in artifact mechanics.
**Why Possibly Novel:** Artifact-decorrelation analysis of generator ensembles has not been performed for dense-prediction training.
**Minimal Experiment:** Train on data from 1–5 generators (varying family diversity); measure fingerprint reliance per condition via spectral interventions; test real-data transfer per condition.
**Main Risk:** Access to genuinely diverse capable generators for a given medical/industrial domain may be limited.

---

## Cluster 7 — Detection Limitations (IDEA-B-0216 … IDEA-B-0245)

### IDEA-B-0216 — The compute-optimal operating point for early tiny-plume detection
**One-sentence idea:** Characterize the latency-resolution-recall tradeoff surface for detecting sub-10-pixel smoke plumes, identifying compute-optimal operating points (input resolution, tiling strategy, temporal integration) for early-fire detection under fixed hardware budgets.
**Problem:** Early plumes occupy a handful of pixels where standard detector strides discard the signal, and naive resolution scaling explodes compute quadratically—deployments need the actual tradeoff surface, which has never been mapped.
**Core Hypothesis:** The recall-versus-compute surface has strong non-linearities (tiling with overlap beats uniform upscaling at matched FLOPs; temporal integration substitutes for spatial resolution at a measurable exchange rate), so optimized configurations achieve severalfold earlier detection than default configurations at identical hardware cost.
**Why Important:** Minutes of earlier wildfire detection have direct, quantifiable damage-reduction value; the optimization is free once the surface is known.
**Why Possibly Novel:** Compute-indexed operating-surface mapping for tiny-target detection (rather than architecture proposals) is missing from the literature.
**Minimal Experiment:** Sweep resolution × tiling × temporal-integration grids on plume datasets with size-stratified evaluation; map iso-compute recall contours; validate optimal points on held-out cameras.
**Main Risk:** Optimal points may be camera- and scene-specific, requiring per-deployment calibration.

### IDEA-B-0217 — The box-to-mask error transfer function
**One-sentence idea:** Characterize how upstream box-localization errors transform into downstream mask errors in detect-then-segment pipelines, and test whether training the segmenter under the detector's actual error distribution (rather than clean boxes) hardens the pipeline.
**Problem:** Detectors and promptable segmenters are developed and evaluated separately; the coupling—how box jitter, scale error, and drift propagate through prompt conditioning into mask failure—is the unmodeled interface where pipelines actually break.
**Core Hypothesis:** Mask degradation as a function of box perturbation is non-linear with a target-geometry-dependent cliff (small targets tolerate almost no box error), and matching the segmenter's training-time box-noise distribution to the deployed detector's measured error distribution recovers most of the pipeline loss at zero inference cost.
**Why Important:** Detect-then-segment is the dominant production architecture; hardening its interface is broadly and immediately applicable.
**Why Possibly Novel:** Interface-error-distribution matching as a training principle for composed vision pipelines is not established.
**Minimal Experiment:** Measure detector error distributions; map mask-vs-box-perturbation response surfaces; retrain segmenters under matched vs default noise; compare end-to-end.
**Main Risk:** Detector error distributions drift over time, requiring the matching to be maintained.

### IDEA-B-0218 — Can region-text alignment represent unbounded "stuff"? The open-vocabulary stuff gap
**One-sentence idea:** Measure the systematic gap between open-vocabulary detection of discrete objects and unbounded "stuff" (smoke, water, spills, haze), and test whether the object-centric region-proposal machinery—not the vision-language alignment—is the binding constraint.
**Problem:** Open-vocabulary detectors inherit object-centric architectures (proposals, queries, boxes) while safety applications need them for stuff-like phenomena that have no canonical extent, and the failure structure has not been decomposed.
**Core Hypothesis:** Given oracle regions, vision-language alignment scores stuff classes nearly as well as object classes (alignment is not the bottleneck), while proposal machinery recalls stuff regions drastically worse—localizing the failure to region generation and predicting that mask-based proposal alternatives close most of the gap.
**Why Important:** Determines which component must be redesigned for open-vocabulary safety monitoring—a live architectural question.
**Why Possibly Novel:** Component-wise decomposition of the stuff gap in open-vocabulary detection has not been published.
**Minimal Experiment:** Evaluate OV detectors on object-vs-stuff class suites with oracle-region ablations; attribute the gap; test mask-proposal substitutions.
**Main Risk:** Stuff ground truth (extent conventions) is itself ambiguous, requiring distribution-based evaluation.

### IDEA-B-0219 — Is duplicate suppression the binding constraint for amorphous-target detection?
**One-sentence idea:** Test whether non-maximum suppression and its query-based equivalents systematically destroy correct detections of amorphous, fragmenting targets (smoke plumes splitting and merging), by comparing suppression-free architectures at matched capacity on plume-dense scenes.
**Problem:** NMS assumes one box per discrete object, but plumes are non-discrete—overlapping detections of one plume and separate detections of split plumes are both correct answers that suppression logic cannot represent.
**Core Hypothesis:** A measurable fraction of missed detections on multi-plume scenes occurs at the suppression stage (recoverable by oracle suppression), the loss grows with plume fragmentation degree, and set-prediction architectures without hard suppression recover most of it—reframing amorphous detection as a suppression-design problem.
**Why Important:** Attributes a chronic failure to a specific, replaceable pipeline stage rather than to feature quality, where effort is currently spent.
**Why Possibly Novel:** Suppression-stage attribution analysis for non-discrete targets has not been isolated.
**Minimal Experiment:** Instrument detection pipelines to log pre/post-suppression candidates on fragmented-plume scenes; compute suppression-stage losses; compare against DETR-style models at matched capacity.
**Main Risk:** Defining instance ground truth for fragmenting plumes is itself convention-laden.

### IDEA-B-0220 — The annotation-jitter ceiling for tiny-object detection
**One-sentence idea:** Derive the performance ceiling that box-annotation jitter imposes on tiny-object detection as a function of object size (relative jitter grows as size shrinks), and measure how much of the reported tiny-object performance gap is annotation-limited rather than model-limited.
**Problem:** Tiny-object detection is treated as a modeling challenge, but a 2-pixel annotation error on an 8-pixel object devastates IoU-based training and evaluation—the field may be optimizing against noise below a computable floor.
**Core Hypothesis:** Below a size threshold determined by measured annotator jitter, inter-method performance differences on standard benchmarks are statistically indistinguishable from annotation-noise effects, and jitter-aware training objectives (loosened matching for tiny objects) recover measurable performance that standard objectives waste fighting noise.
**Why Important:** Redirects tiny-object research away from noise-chasing and toward annotation protocols and noise-aware objectives.
**Why Possibly Novel:** Annotation-jitter ceilings have been derived for segmentation masks but not propagated through detection matching and evaluation logic.
**Minimal Experiment:** Measure multi-annotator box jitter by size; derive ceiling curves through the detection-matching pipeline; re-analyze benchmark method gaps against the ceiling; test jitter-aware matching.
**Main Risk:** Jitter statistics vary across annotation tools and interfaces, complicating universal ceilings.

### IDEA-B-0221 — The temporal information value curve for low-contrast smoke detection
**One-sentence idea:** Measure how detection performance for low-contrast smoke grows with the number of temporally integrated frames, mapping the information-value curve of motion versus appearance and locating where temporal integration saturates.
**Problem:** Smoke is defined as much by motion coherence as appearance, yet deployment systems choose frame counts (single-frame vs clip-based) by latency convenience rather than measured information value.
**Core Hypothesis:** Detection performance rises steeply over the first seconds of integration (motion coherence disambiguates smoke from static low-contrast textures), saturates at a scene-dependent horizon, and the saturation point is predictable from plume motion statistics—yielding a principled latency-accuracy contract per deployment.
**Why Important:** Alarm latency is a safety parameter; grounding it in measured information curves replaces arbitrary engineering choices.
**Why Possibly Novel:** Temporal information-value curves (bits gained per added frame) for amorphous detection have not been quantified.
**Minimal Experiment:** Train/evaluate detectors across frame-count ladders on time-stamped smoke datasets; fit value curves; correlate saturation with plume motion statistics.
**Main Risk:** Camera frame rates and compression differ widely, complicating a unified curve.

### IDEA-B-0222 — SAM's everything mode as a region-proposal engine: where does mask-derived objectness fail?
**One-sentence idea:** Benchmark class-agnostic mask proposals from foundation segmenters against classical region-proposal networks on hard detection domains (low-contrast lesions, camouflage, clutter), and characterize where mask-derived objectness breaks.
**Problem:** SAM-style proposals are replacing RPNs by default, but their objectness prior was learned from photographs of discrete things—its recall structure on the targets that matter (subtle lesions, camouflaged objects) is uncharted.
**Core Hypothesis:** Mask-derived proposals dominate RPNs on boundary-defined objects but fail systematically on contrast-defined targets whose evidence is textural rather than geometric, and the failure is predictable per image from a computable boundary-evidence score—enabling hybrid routing between proposal mechanisms.
**Why Important:** Proposal recall upper-bounds every downstream detection pipeline; knowing the failure geography prevents silent recall ceilings in medical and safety systems.
**Why Possibly Novel:** Failure-structure characterization (not aggregate benchmarking) of foundation-model proposals against classical mechanisms is missing.
**Minimal Experiment:** Compare proposal recall across target-evidence strata on medical and camouflage datasets; fit the boundary-evidence predictor; test hybrid routing.
**Main Risk:** Fair capacity matching between proposal mechanisms is nontrivial.

### IDEA-B-0223 — Assigner-induced bias against elongated objects
**One-sentence idea:** Isolate how label-assignment rules in detector training (IoU thresholds, center sampling) systematically under-train on extreme-aspect-ratio objects (catheters, tubes, wires), separately from feature or anchor limitations.
**Problem:** Elongated-object detection failures are attributed to features or anchors, but the training-time assigner silently discards or mislabels candidate-to-GT matches for thin objects (center points miss thin diagonal structures; IoU thresholds are unreachable), starving them of gradient signal.
**Core Hypothesis:** Gradient-flow accounting shows elongated objects receive disproportionately few positive assignments under standard assigners, aspect-ratio-conditional assignment restores training signal and recovers a large share of the performance gap without any architectural change, and the effect explains cross-detector consistency of elongated-object failure.
**Why Important:** A training-logic fix (cheap, universal) would improve every detector on a clinically and industrially critical object family.
**Why Possibly Novel:** Assigner-stage attribution for shape-conditional detection failure has not been isolated from architecture effects.
**Minimal Experiment:** Instrument assignment statistics by aspect ratio across detector families; train with ratio-conditional assigners; compare per-shape performance at matched everything-else.
**Main Risk:** Multiple assigner families exist; findings must replicate across them for generality.

### IDEA-B-0224 — The crowding threshold: when detection must become density estimation
**One-sentence idea:** Locate the instance-density threshold beyond which detection-based counting of clumped objects (cells, colonies, seedlings) becomes fundamentally inferior to direct density regression, and identify the threshold's dependence on overlap statistics.
**Problem:** Practitioners choose detection or density paradigms by habit, yet the two degrade differently with crowding—detection loses instances to suppression and matching ambiguity while density methods lose localization—and the crossover has never been mapped.
**Core Hypothesis:** A measurable crowding threshold (parameterized by overlap fraction and instance-size variance) separates regimes where each paradigm dominates for counting accuracy, the threshold is stable across domains at matched overlap statistics, and hybrid switching (density in crowded regions, detection elsewhere) beats both globally.
**Why Important:** Counting underlies quantitative biology and agriculture; a validated regime map replaces paradigm guesswork with measurement.
**Why Possibly Novel:** Paradigm-crossover mapping under controlled crowding is not established methodology.
**Minimal Experiment:** Build crowding-controlled datasets (synthetic composites plus real microscopy strata); evaluate both paradigms across the sweep; locate crossovers; test region-adaptive hybrids.
**Main Risk:** Real crowding correlates with other difficulty factors (staining density, focus), confounding pure-density attribution.

### IDEA-B-0225 — Decomposing detector confidence: localization versus classification failure under shift
**One-sentence idea:** Decompose detection confidence into calibrated localization-quality and classification-correctness components, and measure which component's calibration collapses first under domain shift for medical and safety detectors.
**Problem:** A detector's single confidence score conflates "it is there" with "the box is right"; downstream consumers (prompted segmenters, alarm logic) need the components separately, and shift may corrupt them differently.
**Core Hypothesis:** Under cross-site shift, classification confidence decalibrates severely while localization-quality prediction remains comparatively stable (it depends on local geometry, not distribution-level semantics), so component-wise recalibration outperforms global temperature scaling and enables smarter downstream routing.
**Why Important:** Every detect-then-act pipeline thresholds on confidence; knowing which component to trust under shift changes deployment logic.
**Why Possibly Novel:** Component-wise calibration-under-shift analysis for detection has not been systematically published.
**Minimal Experiment:** Instrument detectors to output component scores; evaluate calibration per component across shift ladders; compare component-wise vs global recalibration downstream.
**Main Risk:** Component separation requires architectural access; some detector families entangle the scores irrecoverably.

### IDEA-B-0226 — Detection recall as a function of boundary contrast: the camouflage-transparency continuum
**One-sentence idea:** Measure detection recall as a continuous function of target boundary contrast—placing camouflaged, low-contrast, and transparent objects on one quantitative continuum—to test whether the failures currently studied as separate problems follow a single contrast-recall law.
**Problem:** Camouflaged-object detection, transparency detection, and low-contrast lesion detection are separate literatures with separate methods, but all may be points on one underlying objectness-versus-contrast curve—if so, methods and insights should transfer, and benchmarks should be unified.
**Core Hypothesis:** Recall across all three literatures collapses onto a shared curve when plotted against a common boundary-contrast measure (controlling for size), method improvements in one literature shift the same curve for the others, and the unified view exposes contrast regimes no existing benchmark covers.
**Why Important:** Unification would consolidate three fragmented research communities and reveal shared mechanisms behind "invisible object" failures.
**Why Possibly Novel:** Cross-literature quantitative unification via a common contrast axis has not been attempted.
**Minimal Experiment:** Compute standardized boundary-contrast measures across camouflage, transparency, and lesion benchmarks; plot recall curves per method family; test curve-collapse statistically.
**Main Risk:** A single contrast measure may not capture the distinct physics of the three phenomena.

### IDEA-B-0227 — A taxonomy of negatives: pricing the marginal value of each hard-negative type
**One-sentence idea:** Build a taxonomy of hard-negative categories for fire/smoke detection (sunsets, fog, steam, dust, headlights, reflections) and measure each category's marginal false-positive-reduction value per training example, enabling optimal negative-set composition.
**Problem:** Negative sets are assembled opportunistically, and teams cannot answer basic questions: how many sunset examples are enough, and is steam worth 10× sunset—leaving FP reduction to chance.
**Core Hypothesis:** Marginal FP-reduction value per negative category follows measurable diminishing-returns curves with strongly heterogeneous initial slopes (physics-similar confusers like steam are worth orders of magnitude more per example than appearance-similar ones like sunsets), and portfolio-optimized negative sets halve FP rates at fixed negative-set size.
**Why Important:** Negative-data budgeting is a universal, unglamorous decision with direct alarm-fatigue consequences; pricing it changes practice immediately.
**Why Possibly Novel:** Category-wise marginal-value curves for negative data have not been measured for any detection task.
**Minimal Experiment:** Assemble categorized negative pools; train across composition grids; fit per-category value curves; validate portfolio optimization on held-out deployment footage.
**Main Risk:** Category value likely interacts with positive-set composition, requiring joint analysis.

### IDEA-B-0228 — The energy-latency-recall frontier for always-on edge fire detection
**One-sentence idea:** Map the three-way frontier between energy consumption, detection latency, and recall for always-on edge fire monitoring using early-exit cascades, and locate where distilled foundation-model backbones sit relative to purpose-built lightweight models on that frontier.
**Problem:** Solar-powered and battery-constrained camera deployments must ration inference energy, but the field optimizes accuracy-latency while ignoring energy—the binding constraint for exactly the remote deployments where fire detection matters most.
**Core Hypothesis:** Cascade architectures with scene-adaptive early exits dominate fixed-model configurations across most of the energy-recall frontier (quiet scenes exit early at negligible energy), and distilled foundation backbones occupy a specific frontier region (high-recall/high-energy) that suits only mains-powered installations—a deployment-matching result.
**Why Important:** Grounds hardware and model procurement for wildfire-monitoring networks in measured frontiers rather than benchmark accuracy.
**Why Possibly Novel:** Energy-inclusive frontier mapping for safety detection cascades is rarely published with real power measurements.
**Minimal Experiment:** Implement cascades and monolithic baselines on representative edge hardware; measure true energy per scene type; map frontiers on long-duration field footage.
**Main Risk:** Hardware-specific energy results may not generalize across edge platforms.

### IDEA-B-0229 — The economic crossover between training detectors and prompting foundation models
**One-sentence idea:** Model and measure the total-cost crossover between deploying a trained detector versus a human-prompted foundation segmenter for recurring visual tasks, as a function of task volume, target rarity, and required accuracy.
**Problem:** Teams now face a genuine economic choice—annotate and train a specialized detector, or pay per-use human prompting of a foundation model—and no framework quantifies where the crossover lies.
**Core Hypothesis:** The crossover volume (images per month above which training wins) is predictable from measurable task parameters (prompting time per image, annotation cost, achievable zero-shot quality), and for a large class of low-volume professional tasks the prompting regime permanently dominates—implying tooling investment should target prompting workflows, not training pipelines, for that class.
**Why Important:** This build-versus-prompt decision is made constantly across industries with ad hoc reasoning; a validated cost model changes resource allocation broadly.
**Why Possibly Novel:** Economic crossover analysis between interaction-based and training-based vision deployment has not been formalized with measured parameters.
**Minimal Experiment:** Measure per-image prompting costs and quality across tasks; measure training-pipeline costs to matched quality; fit and validate the crossover model on held-out task types.
**Main Risk:** Cost parameters drift quickly with model progress, requiring the model (not numbers) to be the contribution.

### IDEA-B-0230 — Center-line matching: fixing detection evaluation for thin elongated objects
**One-sentence idea:** Replace IoU-based matching with center-line-based matching criteria for elongated-object detection evaluation, and measure how the metric change reorders methods and redirects error analysis for tubes, wires, and instruments.
**Problem:** Box IoU is nearly meaningless for thin diagonal objects (a perfect detection of a wire has low box IoU due to background dominance), so current benchmarks may systematically mismeasure which methods actually localize elongated structures well.
**Core Hypothesis:** Under center-line matching (distance and coverage along the medial axis), method rankings on elongated-object benchmarks change substantially, several "failures" of standard methods are revealed as metric artifacts, and the new metric correlates better with downstream task success (grasping, catheter tracking) than box IoU.
**Why Important:** Elongated objects are pervasive in surgical, industrial, and infrastructure inspection domains; measuring them wrongly steers the field's method development.
**Why Possibly Novel:** Alternative matching geometry for detection evaluation (validated against downstream utility) has not been standardized for elongated targets.
**Minimal Experiment:** Implement center-line matching; re-evaluate public detectors on elongated-object suites; correlate both metrics with downstream-task proxies; report rank changes.
**Main Risk:** Center-line ground truth must be derived from existing annotations, adding a processing-noise layer.

### IDEA-B-0231 — Edge-truncation bias: detection of partially out-of-frame targets
**One-sentence idea:** Quantify the systematic detection-performance drop for targets partially outside the image frame (fire at frame edges, lesions at scan borders), attribute it between training-data statistics and architectural edge effects, and test targeted corrections.
**Problem:** Frame-edge targets are both operationally critical (fire entering the field of view) and systematically underrepresented in curated datasets—yet edge behavior is unmeasured because evaluation protocols often exclude truncated instances entirely.
**Core Hypothesis:** Edge-truncated targets suffer a measurable recall penalty beyond what their visible-area reduction predicts, the excess penalty decomposes into learned center bias (data) and convolution/attention boundary artifacts (architecture) with data effects dominating, and truncation-augmented training removes most of the excess penalty.
**Why Important:** Monitoring systems see targets enter frames edge-first; the first moments of visibility are exactly when detection matters most.
**Why Possibly Novel:** Edge-truncation as a distinct, decomposable failure mode (rather than an excluded evaluation case) has not been analyzed.
**Minimal Experiment:** Build truncation-controlled evaluation via cropping protocols; measure excess penalties across architectures; attribute via padding/position ablations; test truncation augmentation.
**Main Risk:** Truncation interacts with object identifiability in target-specific ways that complicate a unified account.

### IDEA-B-0232 — Multifocality conventions: one lesion or many, and what it does to training
**One-sentence idea:** Measure how inconsistent annotation conventions for multifocal findings (one box around a cluster versus many boxes around components) inject contradiction into detector training, and test convention-robust matching that tolerates both readings.
**Problem:** Multifocal lesions, fire clusters, and debris fields have no canonical instance decomposition, datasets mix conventions silently, and standard matching penalizes the model whichever way it answers—an unrecognized noise source in detection training.
**Core Hypothesis:** Convention inconsistency is measurable in existing datasets (systematic disagreement between annotator cluster/split choices), it inflates training loss variance and suppresses confidence on multifocal cases specifically, and hierarchical matching (accepting either the cluster or its components) recovers measurable performance on multifocal test strata.
**Why Important:** Multifocality is clinically meaningful (disease staging) and operationally common; convention noise corrupts exactly these high-stakes cases.
**Why Possibly Novel:** Instance-decomposition convention as a measured training noise source has not been isolated in detection research.
**Minimal Experiment:** Quantify convention disagreement via multi-annotator relabeling of clustered findings; train with standard vs hierarchical matching; compare multifocal-strata performance.
**Main Risk:** Hierarchical matching may relax evaluation in ways that require careful, honest metric redesign.

### IDEA-B-0233 — What does a detector add over change detection for static-camera monitoring?
**One-sentence idea:** Rigorously measure the marginal value of learned object detection over classical background-model change detection for static-camera fire/smoke monitoring at matched false-positive budgets, identifying which detections genuinely require semantics.
**Problem:** Static cameras permit strong background modeling that flags any appearance change; the expensive learned detector may only be needed to classify changes, not find them—but deployments run full-frame detection anyway, and nobody has cleanly decomposed the roles.
**Core Hypothesis:** At matched FP budgets, change detection recovers the large majority of true events on static cameras (finding is cheap), learned semantics matter mainly for change triage (rejecting benign changes), and a change-gated detector architecture achieves equal recall at a fraction of the compute—with the residual detector-only detections concentrated in slow-onset events that defeat background models.
**Why Important:** Right-sizes the role of deep detection in the most common monitoring configuration, with large compute and energy savings.
**Why Possibly Novel:** Role decomposition between change finding and semantic triage has not been quantified for modern detectors.
**Minimal Experiment:** Run background-model, detector-only, and change-gated pipelines on long-duration static-camera footage; decompose detections by which mechanism found them; compare compute and FP profiles.
**Main Risk:** Modern PTZ and auto-exposure cameras violate static-background assumptions in ways that must be stratified.

### IDEA-B-0234 — Query-count scaling laws for dense-instance scenes
**One-sentence idea:** Characterize how query-based detectors (DETR family) scale with instance density—measuring recall saturation as instance counts approach and exceed query counts—and derive the query-budget law needed for microscopy and aerial dense scenes.
**Problem:** Query-based architectures fix a maximum instance capacity at design time, natural-image defaults (around 100–300 queries) are silently inadequate for cell imagery with thousands of instances, and the degradation structure near saturation is uncharacterized.
**Core Hypothesis:** Recall degrades non-linearly as instance count approaches the query budget (competition effects begin well below nominal capacity, around a measurable utilization fraction), scaling queries has compute costs that interact with token counts predictably, and a utilization-targeted query-budget rule (queries ≈ k × expected instances) generalizes across dense domains.
**Why Important:** Dense-instance domains are adopting query architectures on natural-image defaults; a scaling law prevents silent recall ceilings.
**Why Possibly Novel:** Query-utilization scaling analysis under extreme instance density has not been systematically mapped.
**Minimal Experiment:** Train/evaluate query detectors across query-budget × instance-density grids on microscopy and synthetic dense scenes; fit the saturation law; validate the budget rule.
**Main Risk:** Attention-collapse behaviors near saturation may be implementation-specific across DETR variants.

### IDEA-B-0235 — Near-vocabulary unknowns: does open-vocabulary detection know what it doesn't know?
**One-sentence idea:** Test whether open-vocabulary detectors produce calibrated unknown-object scores for objects semantically near their vocabulary (novel surgical tools among known ones) versus far from it, measuring the confusion between "similar known thing" and "unknown thing."
**Problem:** Open-set safety (flagging unknown instruments, foreign objects) requires distinguishing near-vocabulary novelty from vocabulary members, but text-embedding-based scoring plausibly assigns confident known-class labels to near-vocabulary unknowns—the most dangerous direction of error.
**Core Hypothesis:** Unknown-detection performance degrades sharply with semantic proximity to the vocabulary (measurable as a proximity-calibration curve), current OV detectors misclassify near-unknowns as their nearest known class with high confidence, and vocabulary-expansion with contrastive negative prompts ("a tool that is not X") measurably improves near-unknown flagging.
**Why Important:** Deployed open-set claims rest on far-unknown evaluations; the near-unknown regime is where real safety failures live.
**Why Possibly Novel:** Proximity-stratified open-set evaluation for detection has not been established.
**Minimal Experiment:** Build proximity-stratified unknown test suites (held-out classes at graded text-embedding distances); measure unknown-score calibration per stratum; test negative-prompt mitigation.
**Main Risk:** Semantic proximity measures and visual proximity diverge; both axes must be controlled.

### IDEA-B-0236 — Event-level supervision: how weak can fire-detection labels be?
**One-sentence idea:** Determine the minimal label granularity (event timestamps alone, versus frame labels, versus boxes) sufficient to train usable spatial fire detectors, by measuring the label-granularity versus performance exchange across expansion methods that convert weak labels to trainable signal.
**Problem:** Fire archives come with alarm timestamps—orders of magnitude cheaper than boxes—but the field lacks a map of how much spatial detection quality each label granularity can support.
**Core Hypothesis:** Event timestamps plus camera metadata support spatial detector training within a measurable gap of frame-labeled training (via temporal-difference mining around event onsets), the gap closes with archive scale at a fitted rate, and the timestamp-to-frame-label exchange rate makes archive mining strictly dominant over annotation for organizations holding large archives.
**Why Important:** Every fire service and camera network holds timestamped archives; quantifying their trainability converts dormant data into detection capability.
**Why Possibly Novel:** Label-granularity exchange-rate measurement for safety detection has not been systematized.
**Minimal Experiment:** On archives with full labels, train across granularity ladders (timestamps → frames → boxes) with expansion pipelines; fit exchange rates and scale trends.
**Main Risk:** Alarm timestamps have variable lag from visual onset, injecting temporal noise that expansion must model.

### IDEA-B-0237 — Extrapolation versus interpolation: decomposing multi-scale generalization in aerial detection
**One-sentence idea:** Decompose detectors' scale generalization into interpolation (within trained scale range) and extrapolation (beyond it), testing whether multi-scale training only densifies interpolation while extrapolation remains architecturally broken for aerial fire imagery.
**Problem:** Multi-scale augmentation is assumed to confer scale robustness, but aerial deployments encounter scales (extreme altitudes) outside any training range—and the interpolation/extrapolation distinction is never separated in evaluation.
**Core Hypothesis:** Detection performance inside the trained scale envelope is near-uniform (interpolation works), collapses sharply beyond the envelope regardless of augmentation density (extrapolation fails), and scale-equivariant architectural components—not more augmentation—measurably extend the envelope, redefining how scale robustness should be pursued.
**Why Important:** Distinguishes a data problem (solvable by augmentation) from an architecture problem (not), preventing wasted augmentation effort for out-of-envelope deployments.
**Why Possibly Novel:** The interpolation-extrapolation decomposition for scale in detection has not been cleanly executed.
**Minimal Experiment:** Train with controlled scale envelopes; evaluate inside and beyond; compare augmentation-densification against equivariant components at matched budgets.
**Main Risk:** True scale extrapolation is entangled with resolution and blur effects that must be controlled via careful resampling.

### IDEA-B-0238 — Transferring mask-derived objectness into detector initialization
**One-sentence idea:** Test whether initializing detection heads with objectness priors distilled from mask-pretrained foundation models improves low-contrast medical detection more than standard ImageNet or self-supervised initialization, isolating the value of boundary-based objectness as an inductive prior.
**Problem:** Detector initialization transfers classification features by default, while the hardest detection domains fail on objectness (what counts as a thing) rather than classification—and mask-pretrained models encode exactly that missing prior in an untransferred form.
**Core Hypothesis:** Objectness-distilled initialization improves proposal recall specifically on low-contrast and boundary-ambiguous targets during early training (a prior effect that persists at convergence for small datasets but washes out for large ones), with the gain predicted by the target domain's boundary-evidence statistics.
**Why Important:** Initialization is a zero-inference-cost intervention; if objectness transfers, every low-data detection project benefits immediately.
**Why Possibly Novel:** Cross-paradigm prior transfer (mask-model objectness into detection initialization) with regime analysis has not been isolated.
**Minimal Experiment:** Distill objectness maps into detector necks/heads as initialization; train across dataset-size ladders on medical detection; compare recall trajectories against standard initializations.
**Main Risk:** Gains may be replicated by simply adding the foundation model to the pipeline, questioning the initialization framing.
### IDEA-B-0239 — Event-level evaluation across camera networks: deduplicating detection credit
**One-sentence idea:** Develop event-level evaluation for multi-camera monitoring networks—where one fire seen by five cameras is one event, not five detections—and measure how frame-level metrics misrank systems relative to event-level response value.
**Problem:** Camera networks are evaluated with per-frame, per-camera metrics that multiply-count easy events (large visible fires) and under-weight the single-camera marginal detections that actually extend network coverage.
**Core Hypothesis:** Frame-level and event-level rankings of detection systems diverge substantially on networked deployments (systems tuned for per-frame AP overinvest in redundant confirmations), and event-level metrics reveal coverage-extending capabilities that frame metrics render invisible—changing which systems operators should procure.
**Why Important:** Public-safety procurement and research both optimize the measurable; aligning metrics with event response directly improves real outcomes.
**Why Possibly Novel:** Event-deduplication evaluation methodology for detection networks has not been formalized in the vision literature.
**Minimal Experiment:** On multi-camera datasets with event ground truth, evaluate systems under frame vs event metrics; quantify ranking divergence; identify capability differences the event view exposes.
**Main Risk:** Event identity across cameras requires geometric/temporal association that introduces its own errors.

### IDEA-B-0240 — The spatial-grounding precision limit of VLM-proposed boxes
**One-sentence idea:** Measure the spatial precision ceiling of boxes proposed by current vision-language models from text descriptions—as prompts for downstream segmentation—across target sizes, quantifying where VLM grounding is and is not sufficient to replace human prompting.
**Problem:** Text-driven automation of prompting pipelines (describe the finding, VLM boxes it, SAM segments it) is being deployed on the assumption that VLM localization is adequate, without a precision-by-size characterization.
**Core Hypothesis:** VLM box precision degrades sharply below a target-size threshold (relative to image size) and for off-center targets, the degradation structure is consistent across model families (a shared architectural signature of resolution-limited visual tokenization), and precision predicts end-to-end mask quality through the measurable box-to-mask transfer function.
**Why Important:** Defines the current automation boundary for language-driven dense pipelines—which tasks can drop the human today and which cannot.
**Why Possibly Novel:** Size- and position-stratified grounding-precision audits oriented to prompting sufficiency have not been published.
**Minimal Experiment:** Evaluate VLM box proposals across size/position strata on grounding datasets; propagate through prompted segmentation; map end-to-end quality against target size.
**Main Risk:** Rapid VLM progress dates specific numbers; the methodology and thresholds framework must carry the value.

### IDEA-B-0241 — Prevalence-conditioned prompting: hallucinated detections under leading questions
**One-sentence idea:** Measure how text-conditioned detectors and VLMs hallucinate requested-but-absent objects as a function of query prevalence expectations ("find the smoke" in smoke-free images), and test prevalence-calibrated prompting protocols.
**Problem:** Language-conditioned detection inherits the leading-question problem: asking for an object biases the system toward finding it, which is catastrophic for monitoring where most queries should return nothing.
**Core Hypothesis:** Hallucinated-detection rates under target-absent querying are substantial and grow with linguistic assertiveness of the prompt, the effect exceeds what score thresholding can remove (hallucinations are confident), and protocols that include explicit absence options with calibrated abstention reduce hallucination severalfold at fixed sensitivity.
**Why Important:** Text-driven monitoring interfaces are being productized now; their leading-question failure mode needs quantification before deployment norms solidify.
**Why Possibly Novel:** Prevalence-expectation manipulation as an experimental variable for language-conditioned detection is unexplored.
**Minimal Experiment:** Query detectors/VLMs on curated absent-target suites with prompt-assertiveness ladders; measure hallucination-rate curves; test absence-option protocols.
**Main Risk:** Distinguishing hallucination from genuine ultra-low-contrast detection requires rigorously verified absence.

### IDEA-B-0242 — Zoom policies as sequential decisions: formalizing coarse-to-fine detection for gigapixel inputs
**One-sentence idea:** Formalize dynamic zoom-in for gigapixel detection (whole-slide imaging, wide-area surveillance) as a sequential decision problem with explicit compute budgets, and benchmark learned zoom policies against exhaustive tiling on recall-per-FLOP.
**Problem:** Gigapixel inputs make exhaustive high-resolution detection computationally prohibitive, practitioners hand-craft coarse-to-fine heuristics, and the field lacks both a formal framing and standardized comparison for adaptive-resolution detection.
**Core Hypothesis:** Learned zoom policies achieve equal recall at a small fraction of exhaustive-tiling compute (concentrating resolution where coarse evidence is ambiguous), the advantage grows with target sparsity, and policy value decomposes into a coarse-detectability term measurable in advance—predicting per-domain whether adaptive zoom is worth its complexity.
**Why Important:** Compute-proportional scaling with image size is the only viable path for gigapixel-native applications now hitting practice.
**Why Possibly Novel:** Budgeted sequential-decision formalization with standardized recall-per-FLOP benchmarking for zoom policies is not established.
**Minimal Experiment:** Implement policy-learned and heuristic zoom on whole-slide and aerial datasets; compare recall-per-FLOP frontiers; fit the coarse-detectability predictor.
**Main Risk:** Policy training may overfit dataset-specific spatial priors (where targets tend to be).

### IDEA-B-0243 — Deblur-then-detect versus blur-robust features for pan-tilt-zoom motion blur
**One-sentence idea:** Compare restoration-first (deblur, then detect) against robustness-first (train detection features on blurred data) strategies for the characteristic motion blur of scanning pan-tilt-zoom fire cameras, decomposing which strategy preserves tiny-plume recall.
**Problem:** PTZ cameras scan continuously, blurring exactly the small distant plumes that early detection needs, and the two natural remedies embed opposite failure modes (hallucinated deblurred texture versus lost discriminative detail) that have never been compared for tiny targets.
**Core Hypothesis:** For targets near the resolution limit, deblurring destroys or fabricates the few discriminative pixels (net-negative for recall despite better visual quality) while blur-matched training preserves detection-sufficient statistics, reversing the intuition that restoration helps downstream tasks—with the reversal point predictable from target size relative to blur kernel.
**Why Important:** PTZ scanning is standard in wildfire networks; choosing the wrong blur strategy silently costs early detections.
**Why Possibly Novel:** Restoration-versus-robustness decomposition at the tiny-target regime (where the answer plausibly flips) has not been isolated.
**Minimal Experiment:** Build blur-calibrated PTZ test data; run both strategies across target-size strata; locate the reversal point; validate on real scanning footage.
**Main Risk:** Deblurring model quality is a moving target; conclusions need blur-strength-conditioned framing.

### IDEA-B-0244 — Temporal correlation of false positives: why FP-per-frame mispredicts FP-per-day
**One-sentence idea:** Measure the temporal correlation structure of false positives in continuous monitoring (FPs cluster in condition episodes—sunsets, fog banks—rather than occurring independently), and build the corrected statistical bridge from per-frame FP rates to operational alarm burden.
**Problem:** Systems are validated on i.i.d. frame sets and deployed on temporally correlated streams; correlated FP episodes produce alarm storms that per-frame rates drastically mispredict, breaking deployment planning.
**Core Hypothesis:** FP processes are strongly overdispersed relative to Poisson (episode-driven), the overdispersion is predictable from condition-classifier statistics on unlabeled site footage, and episode-aware alarm logic (condition-conditional thresholds) reduces operator-experienced alarm burden severalfold at unchanged sensitivity—none of which per-frame evaluation can see.
**Why Important:** Alarm fatigue is the primary cause of monitoring-system abandonment; modeling the actual alarm process addresses the real adoption barrier.
**Why Possibly Novel:** Point-process modeling of detection false positives on continuous streams has not entered the vision evaluation literature.
**Minimal Experiment:** Analyze long-duration monitoring logs; fit clustered point-process models to FP streams; validate burden predictions; test episode-aware thresholding.
**Main Risk:** Long-duration labeled monitoring logs are scarce and site-idiosyncratic.

### IDEA-B-0245 — Soft-prompt weighting: consuming the detector's score distribution instead of its top-1
**One-sentence idea:** Test whether feeding the downstream segmenter a weighted set of candidate boxes (the detector's post-NMS score distribution) outperforms the standard top-1 box prompt, especially under detector uncertainty.
**Problem:** Pipelines collapse the detector's rich output distribution to a single box before prompting, discarding uncertainty information exactly when the detector is least sure—the cases that determine pipeline reliability.
**Core Hypothesis:** Distribution-weighted prompting (multiple weighted box prompts or their expectation in prompt space) degrades gracefully with detector uncertainty while top-1 prompting fails discontinuously, with the advantage concentrated in the detector's low-margin decisions and near-zero cost elsewhere—a strict-dominance result for pipeline design.
**Why Important:** A drop-in interface change to the dominant production pipeline with asymmetric upside.
**Why Possibly Novel:** Uncertainty-preserving interfaces between detection and prompted segmentation have not been evaluated.
**Minimal Experiment:** Compare top-1, top-k-weighted, and expectation prompting across detector-confidence strata on two detect-then-segment tasks; measure conditional and overall performance.
**Main Risk:** Prompt-space aggregation of multiple boxes may confuse decoders trained on single-intent prompts.

---

## Cluster 8 — Parameter Efficiency vs Quality (IDEA-B-0246 … IDEA-B-0280)

### IDEA-B-0246 — The intrinsic rank of a domain shift
**One-sentence idea:** Test whether each domain adaptation task has a measurable "intrinsic rank"—the minimal LoRA rank achieving near-ceiling performance—and whether it is predictable from unlabeled data properties before training.
**Problem:** LoRA rank is chosen by grid search per project, wasting compute and obscuring a potentially lawful relationship between shift structure and required adaptation capacity.
**Core Hypothesis:** Rank-performance curves exhibit consistent knee points per task (the intrinsic rank), knees correlate strongly with spectral properties of the feature-space shift (effective dimensionality of the source-target mean-difference and covariance rotation), and a pre-training estimator predicts the knee within a small factor—eliminating rank search.
**Why Important:** Converts the most-tuned PEFT hyperparameter into a measurable quantity, saving compute across thousands of adaptation projects and revealing shift structure.
**Why Possibly Novel:** The rank-requirement-as-shift-property framing with a validated unlabeled-data predictor is absent from PEFT literature.
**Minimal Experiment:** Sweep ranks across 12 diverse adaptation tasks; locate knees; regress knees on candidate spectral predictors; validate predictions on held-out tasks.
**Main Risk:** Knees may be optimizer- and schedule-dependent, blurring the intrinsic-rank concept.

### IDEA-B-0247 — Predicting adapter placement from shift type
**One-sentence idea:** Test whether the optimal depth placement of adapters in a foundation segmenter is predictable from the shift type (style shifts → early layers, semantic/label shifts → late layers, resolution shifts → embedding), replacing placement search with diagnosis.
**Problem:** Placement grids multiply PEFT tuning cost, and placement folklore ("adapt everything", "adapt attention only") lacks a principled basis connected to what actually changed between domains.
**Core Hypothesis:** A cheap shift-diagnosis (layer-wise feature-drift profile computed from unlabeled target data through the frozen model) predicts the placement that grid search would select, achieving within-noise performance at a fraction of the search cost, and the diagnosis-placement mapping is stable across model scales.
**Why Important:** Makes PEFT configuration principled and cheap simultaneously—a methodology contribution applicable to every adaptation.
**Why Possibly Novel:** Drift-profile-based placement prediction with validation against exhaustive search is undeveloped.
**Minimal Experiment:** Compute drift profiles for 10 shifts; run placement grids as ground truth; measure prediction accuracy of the diagnostic; replicate on two model scales.
**Main Risk:** Placement interactions (early+late synergies) may defeat single-depth predictions.

### IDEA-B-0248 — Does PEFT protect zero-shot generality? The retention-adaptation frontier
**One-sentence idea:** Measure the frontier between target-domain adaptation gain and retained zero-shot generality across PEFT methods and full fine-tuning, testing whether parameter efficiency causally protects generality or merely correlates with undertraining.
**Problem:** "LoRA forgets less" is folklore supported by confounded comparisons (different effective learning rates, budgets); whether the low-rank constraint itself preserves generality—at matched target performance—is unresolved and matters for every deployed adapter.
**Core Hypothesis:** At strictly matched target-domain performance, low-rank and sparse PEFT retain substantially more zero-shot capability than full fine-tuning (the constraint geometrically restricts interference with pretrained directions), with retention scaling inversely with effective update rank—a causal, capacity-indexed law rather than a training artifact.
**Why Important:** Retention is the property that lets one foundation model serve many masters; establishing its causal relationship to update geometry guides all adapter deployment.
**Why Possibly Novel:** Matched-target-performance retention comparisons with rank-indexed analysis are missing from PEFT evaluations.
**Minimal Experiment:** Adapt to 4 domains at swept budgets, selecting checkpoints at matched target IoU; evaluate zero-shot suites; fit retention-versus-effective-rank curves.
**Main Risk:** Matching target performance exactly across methods requires dense checkpointing and careful selection.

### IDEA-B-0249 — Do dense tasks need spatially structured PEFT? Ranking adaptation families by task type
**One-sentence idea:** Test whether the PEFT-method ranking established on classification (bias tuning ≈ LoRA ≈ adapters) breaks down for dense prediction, where adaptation plausibly requires spatially heterogeneous corrections that global methods cannot express.
**Problem:** PEFT methods are validated on classification and language, then transplanted to segmentation on the assumption of task-independence—but dense tasks may have structurally different adaptation needs (boundary-local corrections, resolution-specific fixes).
**Core Hypothesis:** PEFT families reorder on dense tasks: methods offering token-wise or spatially varying modulation outperform global methods (bias/scale tuning) by margins that grow with the spatial heterogeneity of the domain shift, measurable as spatial variance in the full-fine-tune update—establishing task-conditional PEFT selection.
**Why Important:** Prevents cargo-culting classification PEFT conclusions into the dense-prediction domain where deployment decisions now depend on them.
**Why Possibly Novel:** Task-type-conditional PEFT ranking with a spatial-heterogeneity mechanism analysis has not been done.
**Minimal Experiment:** Benchmark 6 PEFT families on matched classification vs segmentation adaptations across shifts; measure ranking stability; correlate dense-task gaps with update spatial-variance.
**Main Risk:** Rankings may be dominated by per-method tuning quality rather than family essence.

### IDEA-B-0250 — Global tokens versus local corrections: decomposing what prompt tuning can and cannot adapt
**One-sentence idea:** Decompose adaptation needs into globally coherent corrections (color, contrast, style) versus spatially local corrections (structure-specific boundaries), and test the hypothesis that learned prompt tokens can express only the former, explaining prompt tuning's inconsistent dense-task results.
**Problem:** Visual prompt tuning sometimes matches adapters and sometimes fails badly on segmentation, with no predictive account of when—leaving practitioners to gamble.
**Core Hypothesis:** Prompt tokens act through global attention modulation and therefore capture shift components that are low-rank in the spatial dimension, so prompt tuning's gap to adapters on a given task is predictable from the spatial rank of the required correction (measurable from a small probe fine-tune)—unifying the scattered empirical record.
**Why Important:** Provides the missing selection rule for the cheapest PEFT family and a mechanistic account of its expressivity boundary.
**Why Possibly Novel:** Spatial-rank expressivity analysis of prompt tuning has not been formalized or tested.
**Minimal Experiment:** Measure spatial rank of full-fine-tune corrections across tasks; correlate with the prompt-tuning-versus-adapter gap; verify with synthetic shifts of controlled spatial rank.
**Main Risk:** Deep prompt variants (tokens at every layer) blur the global-only characterization.

### IDEA-B-0251 — Predicting adapter-merging success from task-vector geometry
**One-sentence idea:** Test whether the success of merging multiple dataset-specific LoRAs into one (versus training jointly) is predictable from the geometry of their updates (subspace angles, task-vector cosines), enabling merge-or-retrain decisions without trial training.
**Problem:** Organizations accumulate per-dataset adapters and want consolidated models, but merging sometimes works and sometimes collapses—with no predictive theory, every consolidation is a gamble.
**Core Hypothesis:** Merge degradation correlates strongly with inter-adapter subspace interference (principal angles between update subspaces weighted by singular values), the predictor computed from adapter weights alone forecasts merge quality within useful tolerance, and interference-guided merging (orthogonalization before averaging) recovers most losses in the risky regime.
**Why Important:** Adapter consolidation is a routine operational need; a weight-space predictor makes it an engineering calculation instead of an experiment.
**Why Possibly Novel:** Merge-quality prediction from adapter geometry (validated against joint training) is not established for dense tasks.
**Minimal Experiment:** Train adapters on 8 datasets; merge all pairs/triples; regress merge quality on geometric predictors; test orthogonalization rescue on worst cases.
**Main Risk:** Geometry may predict interference but not data-conflict effects (label-convention clashes) that also break merges.

### IDEA-B-0252 — Where does 4-bit damage go? Structured quantization error in dense prediction
**One-sentence idea:** Characterize the spatial and semantic structure of errors introduced by aggressive quantization (4-bit weights/activations) in segmentation models, testing whether quantization damage concentrates on boundary features rather than distributing uniformly.
**Problem:** Quantization is certified on mean metrics for edge deployment, but dense outputs can hide structured damage (systematic boundary erosion, small-object loss) inside unchanged means—exactly what safety and clinical uses cannot tolerate.
**Core Hypothesis:** Quantization error concentrates measurably on high-frequency feature channels and thus on boundary localization and small structures (the features with least redundancy), the concentration is predictable from channel-wise activation kurtosis, and mixed-precision schemes guided by that prediction eliminate the structured damage at minimal memory cost.
**Why Important:** Edge medical and monitoring deployments quantize by necessity; knowing where the damage lands converts a blind risk into a managed one.
**Why Possibly Novel:** Spatially and structurally resolved quantization audits for dense prediction are missing (existing work reports means).
**Minimal Experiment:** Quantize segmenters across bit-widths; map error by structure size and boundary distance; correlate channel damage with kurtosis; test guided mixed precision.
**Main Risk:** Findings may vary across quantization algorithms, requiring coverage of the main families.

### IDEA-B-0253 — Attention adapts "where", MLP adapts "what": a causal placement test
**One-sentence idea:** Causally test the hypothesis that adapting attention weights primarily corrects spatial-relational errors (grouping, extent) while adapting MLP weights corrects appearance-semantic errors (what counts as target texture), by targeted-placement fine-tuning with error-type-stratified evaluation.
**Problem:** LoRA placement on attention versus MLP layers is debated with aggregate metrics that cannot see whether the two placements fix different errors—leaving the design question unresolved because it is asked with the wrong instrument.
**Core Hypothesis:** Attention-only adaptation disproportionately reduces grouping/extent errors while MLP-only adaptation disproportionately reduces appearance-classification errors (a double dissociation), and the domain's error-type profile therefore predicts optimal placement—explaining contradictory placement findings across prior tasks.
**Why Important:** Provides mechanistic grounding for PEFT design and a practical error-profile-based placement rule.
**Why Possibly Novel:** Error-type double-dissociation methodology for PEFT placement has not been applied.
**Minimal Experiment:** Adapt attention-only vs MLP-only across domains with error-typed evaluation suites; test the dissociation; validate the placement rule prospectively.
**Main Risk:** Error-type taxonomies for segmentation are imperfect; dissociation may be partial.

### IDEA-B-0254 — Compositional adapter arithmetic: does organ A + organ B = both organs?
**One-sentence idea:** Test whether adding independently trained organ-specific LoRA updates yields a model competent at all constituent organs—characterizing when adapter arithmetic composes, interferes, or produces emergent errors on organ boundaries.
**Problem:** Compositional reuse is PEFT's promised economy (train once per organ, combine on demand), but weight-space addition has no correctness guarantee, and the failure structure for dense tasks—where composed organs physically border each other—is uncharted.
**Core Hypothesis:** Adapter addition preserves most single-organ performance when update subspaces are near-orthogonal (measurable in advance) but produces characteristic new errors precisely at inter-organ boundaries where composed corrections overlap spatially—errors invisible to per-organ metrics and requiring boundary-zone evaluation.
**Why Important:** Composability determines whether the PEFT ecosystem scales like software libraries or requires combinatorial retraining.
**Why Possibly Novel:** Spatial failure analysis of adapter composition (boundary-zone emergent errors) is unexamined.
**Minimal Experiment:** Train per-organ adapters; compose pairs/triples; evaluate per-organ, boundary-zone, and full-scene metrics; correlate composition quality with subspace orthogonality.
**Main Risk:** Composition results may depend on shared-backbone choice and rank, requiring a small design matrix.

### IDEA-B-0255 — Locating the PEFT-to-full-fine-tuning crossover for dense tasks
**One-sentence idea:** Map the target-data-size threshold at which full fine-tuning reliably overtakes the best PEFT for segmentation—across shift magnitudes—and test whether the crossover is predictable, giving practitioners a data-indexed method-selection rule.
**Problem:** The community holds contradictory rules of thumb ("PEFT always suffices" versus "full FT wins with enough data") because the crossover has never been mapped systematically for dense prediction.
**Core Hypothesis:** A crossover exists and shifts predictably: it occurs at larger data sizes for near-domain shifts (PEFT competitive longer) and smaller sizes for far shifts requiring representation restructuring, with the crossover location estimable from early-training loss trajectories of both regimes—enabling cheap forecasting.
**Why Important:** This is among the most common practical decisions in applied vision; an evidence-based rule replaces contradictory folklore.
**Why Possibly Novel:** Systematic crossover cartography with predictive early-stopping diagnostics is missing for dense tasks.
**Minimal Experiment:** Train PEFT and full FT across data-size ladders on near and far shifts; locate crossovers; fit and validate the early-trajectory predictor.
**Main Risk:** Crossover positions may drift with model scale, requiring scale-stratified reporting.

### IDEA-B-0256 — Sensitivity-guided rank allocation across layers
**One-sentence idea:** Test whether allocating a fixed LoRA parameter budget non-uniformly across layers—proportional to measured layer sensitivity (Fisher information of the shift)—beats uniform-rank allocation for segmentation adaptation.
**Problem:** Uniform per-layer rank is the unexamined default, yet shifts plausibly demand wildly different adaptation capacity at different depths, meaning uniform budgets systematically overfeed some layers and starve others.
**Core Hypothesis:** Sensitivity-guided allocation dominates uniform allocation at matched total parameters (largest gains at tight budgets), the optimal allocation profile is shift-type-specific and stable across datasets sharing a shift type, and profiles transfer—so one profiling run amortizes across a family of adaptations.
**Why Important:** Free performance at fixed parameter cost, plus a reusable diagnostic that reveals where shifts live in the network.
**Why Possibly Novel:** Budget allocation as an explicit optimization guided by shift-sensitivity profiling is underdeveloped for dense adaptation.
**Minimal Experiment:** Profile layer sensitivities on 8 shifts; adapt with uniform vs guided allocations at multiple budgets; test profile transfer within shift families.
**Main Risk:** Fisher-based sensitivity may mispredict where low-rank (versus full) updates help most.

### IDEA-B-0257 — The boundary tax of parameter efficiency
**One-sentence idea:** Test whether PEFT methods that match full fine-tuning on region-level metrics systematically underperform on boundary-localized metrics—a hidden "boundary tax" of constrained adaptation—and identify which constraint geometries avoid it.
**Problem:** PEFT equivalence claims rest on region-dominated metrics (mIoU, Dice); if constrained updates preferentially sacrifice high-frequency boundary corrections (which plausibly require higher-rank changes), the equivalence is an artifact of metric choice with clinical consequences.
**Core Hypothesis:** At matched region metrics, standard low-rank adaptation shows measurable boundary-metric deficits versus full fine-tuning, the deficit scales with boundary-correction spatial frequency (mechanistic link to rank constraints), and boundary-targeted PEFT variants (higher rank in early/high-resolution pathways) eliminate the tax at small parameter cost.
**Why Important:** Boundary precision is exactly what medical and industrial applications pay for; a hidden tax would mean PEFT claims systematically overpromise for those users.
**Why Possibly Novel:** Metric-stratified PEFT auditing focused on the boundary-frequency mechanism has not been executed.
**Minimal Experiment:** Adapt with PEFT ladder vs full FT on boundary-critical tasks; report region and boundary metrics separately; test frequency-targeted variants.
**Main Risk:** Boundary metrics are noisier, requiring larger evaluation sets for significance.

### IDEA-B-0258 — Adapting only the prompt encoder: interaction-style personalization at negligible cost
**One-sentence idea:** Test whether adapting only the prompt encoder (hundreds of parameters) to a user's or site's clicking style recovers most of the interactive-performance loss caused by prompt-distribution mismatch, without touching image processing.
**Problem:** Deployment prompt distributions differ from training distributions (clinicians click differently than curators), and the standard response—full adaptation—retrains image understanding to fix what is plausibly an interaction-interface mismatch.
**Core Hypothesis:** Prompt-encoder-only adaptation on small logs of user prompts (hundreds of interactions, no new masks—using self-consistency objectives) recovers the majority of the user-mismatch performance gap, demonstrating that interaction style and image understanding are factorized enough to personalize independently and cheaply.
**Why Important:** Per-user personalization at near-zero parameter and data cost would change interactive deployment economics and safety review scope (image pathway untouched).
**Why Possibly Novel:** Interaction-channel-only adaptation as a personalization mechanism is unexplored.
**Minimal Experiment:** Collect per-user prompt logs; adapt prompt encoders per user; evaluate against full adaptation and no adaptation under each user's prompting.
**Main Risk:** Prompt and image factors may be entangled for hard targets, capping the recoverable fraction.

### IDEA-B-0259 — Does update geometry matter beyond parameter count? Sparse versus low-rank versus multiplicative
**One-sentence idea:** Compare PEFT families with fundamentally different update geometries (unstructured sparse, low-rank, multiplicative scaling) at strictly matched trainable-parameter counts on dense adaptation, isolating whether the geometry—not just the budget—determines adaptation quality.
**Problem:** PEFT comparisons confound parameter count with update structure, so the field cannot answer whether low-rank's dominance reflects a genuine geometric advantage or merely tuning culture and budget conventions.
**Core Hypothesis:** At matched budgets, geometry matters systematically: low-rank excels on distributed style shifts, sparse excels on localized semantic shifts (a few features need rewiring), multiplicative excels on channel-gain shifts (modality changes)—implying shift-conditional geometry selection worth several points over any fixed choice.
**Why Important:** Elevates PEFT selection from brand loyalty to a principled match between shift structure and update geometry.
**Why Possibly Novel:** Geometry-isolated comparisons at matched budgets with shift-type stratification have not been reported for dense tasks.
**Minimal Experiment:** Implement budget-matched geometry variants; adapt across a shift-type battery; test the geometry × shift-type interaction.
**Main Risk:** Optimizer interactions with each geometry may masquerade as geometric effects.

### IDEA-B-0260 — Do adapters overfit sites harder? Update locality and out-of-site transfer
**One-sentence idea:** Test whether PEFT-adapted models, at matched in-site performance, transfer worse to new sites than fully fine-tuned models—because concentrated low-dimensional updates encode site idiosyncrasies more sharply than distributed full updates.
**Problem:** PEFT is deployed per-site under the assumption that its conservatism aids generality, but the opposite is plausible—cramming site adaptation into few parameters may distill exactly the site-specific shortcuts—and the question is empirically open.
**Core Hypothesis:** At matched in-site IoU, adapter-tuned models show measurably larger out-of-site degradation than full fine-tunes when the adaptation data is single-site, the effect reverses with multi-site adaptation data (adapters then encode the shared shift), and the single-site risk is detectable from adapter-weight alignment with site-fingerprint directions.
**Why Important:** Determines safe deployment patterns for the dominant adaptation method in multi-site systems like hospital networks.
**Why Possibly Novel:** The update-locality-versus-transfer question has not been tested at matched in-domain performance.
**Minimal Experiment:** Adapt via PEFT and full FT on single-site data to matched in-site IoU; evaluate across held-out sites; repeat with multi-site adaptation; test the fingerprint-alignment diagnostic.
**Main Risk:** Matching in-site performance while controlling optimization intensity is delicate.

### IDEA-B-0261 — Gradient-free PEFT: adaptation without backpropagation access
**One-sentence idea:** Characterize how far zeroth-order optimization of ultra-low-dimensional adapters can adapt segmentation models in deployment environments where gradients are unavailable (locked-down clinical software, encrypted models), mapping the feasibility frontier of black-box PEFT.
**Problem:** Regulated and proprietary deployments often forbid backpropagation access entirely, making all standard adaptation impossible—yet the black-box adaptation capacity of modern PEFT parameterizations is unmeasured.
**Core Hypothesis:** Zeroth-order methods adapt effectively up to a parameter-dimension ceiling (scaling theory predicts hundreds to low thousands of parameters at realistic query budgets), structured parameterizations (spectral shifts, prompt offsets) fit under that ceiling while achieving a useful fraction of gradient-based PEFT gains, and the query-budget-versus-gain curve is stable enough for deployment planning.
**Why Important:** Opens adaptation to the substantial fraction of clinical and industrial deployments that are cryptographically or contractually gradient-free.
**Why Possibly Novel:** Black-box PEFT feasibility mapping for dense prediction has not been established.
**Minimal Experiment:** Adapt segmenters via zeroth-order methods across parameterization dimensions and query budgets on 3 shifts; map gain surfaces against gradient-based ceilings.
**Main Risk:** Zeroth-order variance may interact badly with dense-task loss landscapes, capping gains below usefulness.

### IDEA-B-0262 — Forgetting dynamics of sequential adapter strategies in hospital rollouts
**One-sentence idea:** Compare continual-adaptation strategies for site-by-site rollout (sequential LoRA stacking, running merges, orthogonal-subspace constraints) on their forgetting dynamics, measured longitudinally as sites accumulate.
**Problem:** Real deployments onboard sites sequentially over years, but continual-PEFT strategies are evaluated on short academic task sequences—their long-horizon forgetting structure (which early sites decay, and when) is unknown.
**Core Hypothesis:** Strategies differ qualitatively in forgetting structure: stacking exhibits recency bias with monotone early-site decay, merging exhibits uniform blurring, and orthogonality constraints preserve early sites at growing cost to new-site plasticity—with the crossover site-count (where constrained methods win) measurable and small enough to matter in practice.
**Why Important:** The choice locks in at rollout start and is expensive to reverse; longitudinal evidence should precede ecosystem-wide commitments.
**Why Possibly Novel:** Long-horizon (10+ site) forgetting-structure comparisons for adapter strategies on dense tasks are missing.
**Minimal Experiment:** Simulate 12-site sequential rollouts from multi-site datasets under each strategy; track per-site performance longitudinally; locate crossovers and failure structures.
**Main Risk:** Simulated rollouts may understate real temporal drift that compounds with site sequence effects.

### IDEA-B-0263 — Does parameter-efficient adaptation recover calibration or only accuracy?
**One-sentence idea:** Measure whether PEFT adaptation that restores target-domain accuracy also restores confidence calibration, testing the hypothesis that accuracy and calibration adapt at different rates and parameter budgets.
**Problem:** Adaptation success is declared on accuracy, but downstream systems consume confidences; if calibration lags accuracy under constrained updates, adapted models silently mislead exactly the thresholding logic built on them.
**Core Hypothesis:** Calibration recovery requires systematically more adaptation capacity than accuracy recovery (confidence heads depend on distribution-tail behavior that low-rank updates fix last), so standard PEFT produces accurate-but-miscalibrated models—and a small calibration-targeted addition (adapted final-layer temperature conditioning) closes the gap at negligible cost.
**Why Important:** Warns the field about a specific, checkable blind spot in adaptation practice with direct deployment consequences.
**Why Possibly Novel:** Differential adaptation-rate analysis of accuracy versus calibration under PEFT is unexamined.
**Minimal Experiment:** Adapt across PEFT budget ladders; track accuracy and calibration metrics jointly; identify the lag structure; test the targeted calibration addition.
**Main Risk:** Calibration metrics on small target datasets are noisy, requiring careful aggregation.

### IDEA-B-0264 — The depth-capacity law of injected prompts
**One-sentence idea:** Establish how the adaptation capacity of injected visual prompt tokens depends on their insertion depth—testing the theory that prompts at depth k can only implement functions expressible by the remaining depth—yielding placement laws for prompt-based adaptation.
**Problem:** Prompt tokens are inserted at arbitrary depths by convention, with contradictory empirical reports, and no theoretical account links insertion depth to what the prompts can possibly correct.
**Core Hypothesis:** Prompt adaptation power decays predictably with insertion depth for corrections requiring multi-layer recomposition (semantic regrouping) but stays flat for late-expressible corrections (output rescaling, threshold shifts), so matching insertion depth to correction type—diagnosed from error structure—recovers most of exhaustive placement search at zero search cost.
**Why Important:** Converts another expensive PEFT search dimension into a principled computation and links prompt tuning to depth-computational theory.
**Why Possibly Novel:** Depth-expressivity analysis of injected prompts, with correction-type-conditioned placement rules, is undeveloped.
**Minimal Experiment:** Sweep insertion depths across correction-type-controlled adaptation tasks (synthetic and real); fit decay curves per correction type; validate the placement rule.
**Main Risk:** The clean theory may be muddied by residual-stream shortcuts that let late prompts affect early-like computation.

### IDEA-B-0265 — Micro-adapters at scale: what is the right granularity for scanner-specific adaptation?
**One-sentence idea:** Determine the optimal granularity for hardware-conditioned micro-adapters (per-scanner-model, per-site, per-protocol, per-modality) by measuring where the marginal gain of finer conditioning crosses its data-fragmentation cost.
**Problem:** Acquisition metadata enables conditioning at many granularities, but finer conditioning splits training data into smaller pools—the granularity that optimizes this bias-variance tradeoff has never been measured, so deployments guess.
**Core Hypothesis:** The optimal granularity follows a data-volume law (finer conditioning wins only above a per-condition sample threshold), scanner-model granularity dominates site granularity at equal data (hardware drives more variance than site practice), and hierarchical adapters (coarse-to-fine with fallback) capture near-oracle performance across all data regimes.
**Why Important:** Provides the design rule for metadata-conditioned deployment across radiology networks—an immediately consumable operational answer.
**Why Possibly Novel:** Conditioning-granularity optimization with fragmentation-cost accounting is unstudied for dense adaptation.
**Minimal Experiment:** Train adapters at each granularity across data-volume ladders on multi-scanner datasets; map the granularity-versus-volume optimum; test hierarchical fallback.
**Main Risk:** Metadata reliability varies; misregistered scanner labels would blur granularity effects.

### IDEA-B-0266 — Warm-starting adapters from related task vectors
**One-sentence idea:** Test whether initializing a new LoRA from the dominant subspace of related prior adaptations (SVD of accumulated task vectors) accelerates and improves low-data adaptation, versus standard random/zero initialization.
**Problem:** Every adaptation starts from scratch even inside organizations holding dozens of prior adapters for related tasks—an untapped transfer resource whose value and mechanics are unquantified.
**Core Hypothesis:** Related-task subspaces contain the generic components of domain adaptation (style axes, modality corrections), so subspace-initialized adapters reach target performance with substantially fewer labels (largest gains below 50 samples) and the gain is predictable from subspace alignment between the new task's early gradients and the prior basis.
**Why Important:** Compounds organizational adaptation experience into an asset—each adaptation makes the next cheaper—changing PEFT economics at fleet scale.
**Why Possibly Novel:** Cross-task adapter initialization via accumulated task-vector bases is undeveloped for dense prediction.
**Minimal Experiment:** Build task-vector bases from adapter libraries; adapt new tasks with subspace vs standard initialization across label ladders; test the alignment predictor.
**Main Risk:** Negative transfer from misaligned bases could harm exactly the low-data regime being targeted.

### IDEA-B-0267 — Is the decoder the right place to spend? Component-wise adaptation value for dense quality
**One-sentence idea:** Systematically measure where adaptation parameters buy the most dense-prediction quality across model components (backbone blocks, neck/upsampler, decoder, prompt pathway), testing the hypothesis that upsampling pathways—not the celebrated backbone—dominate boundary-quality adaptation.
**Problem:** PEFT attention centers on backbone injection by habit inherited from NLP, while dense quality plausibly bottlenecks in the resolution-recovery pathway whose adaptation value has never been isolated.
**Core Hypothesis:** Per-parameter adaptation value is strongly non-uniform across components with upsampler/decoder adaptation dominating boundary metrics and backbone adaptation dominating region/semantic metrics, so metric-targeted component budgets beat uniform injection—and the component-value profile is stable across domains, enabling default recipes.
**Why Important:** Redirects the default PEFT recipe for dense tasks toward the components that actually control the qualities users need.
**Why Possibly Novel:** Component-wise value accounting for dense adaptation (beyond backbone-centric studies) is missing.
**Minimal Experiment:** Adapt each component in isolation and combination at matched budgets across 6 tasks; decompose metric gains by component; test recipe transfer.
**Main Risk:** Component boundaries differ across architectures, complicating general profiles.

### IDEA-B-0268 — Difficulty-adaptive capacity: routing hard tokens to bigger adapters
**One-sentence idea:** Test whether routing computation heterogeneously—sending boundary and ambiguous tokens through higher-capacity adapter paths while easy interior tokens use minimal paths—beats uniform adapter capacity at matched average FLOPs for segmentation.
**Problem:** Dense-prediction difficulty is extremely non-uniform across space (most pixels are easy interior, few are hard boundary), yet adaptation capacity is spent uniformly—a mismatch between where parameters go and where errors live.
**Core Hypothesis:** Token-difficulty routing (learned or geometry-based) concentrates effective capacity on the pixels that carry most residual error, outperforming uniform adapters at matched compute with gains proportional to the dataset's difficulty concentration (measurable in advance), and routing decisions transfer across domains (boundary tokens are universally hard).
**Why Important:** Introduces compute-allocation thinking—standard in LLM inference—into dense adaptation where spatial structure makes it even more natural.
**Why Possibly Novel:** Difficulty-routed heterogeneous adapter capacity for dense tasks is unexplored.
**Minimal Experiment:** Implement two-path routed adapters; compare against uniform at matched FLOPs across tasks with varying difficulty concentration; analyze routing-decision transfer.
**Main Risk:** Routing overhead and training instability could eat the theoretical allocation gains.

### IDEA-B-0269 — Adapting the choice, not the masks: selection-head-only adaptation for granularity conventions
**One-sentence idea:** Test whether adapting only the multimask selection head—which candidate mask to prefer—captures most of the benefit of full adaptation for domains whose conventions differ mainly in granularity (whole-organ versus sub-structure), at near-zero parameter cost.
**Problem:** Many "domain gaps" in prompted segmentation may actually be convention gaps: the model already generates the right candidate but selects the wrong granularity, and full adaptation wastefully retrains generation to fix a selection problem.
**Core Hypothesis:** For convention-type domain gaps (identified by high oracle-candidate performance), selection-head adaptation on tiny label budgets (tens of examples) recovers the majority of the full-adaptation gain, while appearance-type gaps show near-zero selection-only recovery—yielding a cheap diagnostic (oracle-candidate audit) that routes each domain to the right adaptation depth.
**Why Important:** Could reclassify a fraction of the medical-SAM adaptation literature as solving selection problems with generation-sized tools.
**Why Possibly Novel:** The generation-versus-selection decomposition of domain gaps, with selection-only adaptation, is unexamined.
**Minimal Experiment:** Audit oracle-candidate performance across domains; adapt selection-only vs full on both gap types; validate the routing diagnostic.
**Main Risk:** Real domains mix gap types; the clean dichotomy may blur in practice.

### IDEA-B-0270 — Is the input stem the whole story for modality shift? Stem-only adaptation
**One-sentence idea:** Test how much of cross-modality adaptation (RGB→grayscale, RGB→multispectral, natural→radiograph) is captured by adapting only the patch-embedding stem, holding the entire transformer frozen—isolating the input interface as an adaptation bottleneck.
**Problem:** Modality transfer conflates two changes—input statistics and semantic content—and if the transformer's computation is modality-agnostic once inputs are properly embedded, most current whole-network adaptation is redundant.
**Core Hypothesis:** For modality shifts preserving semantic task structure, stem-only adaptation recovers a large majority of full-adaptation performance (the transformer is an input-agnostic computer), while shifts that alter semantic granularity show large residuals—splitting "modality gap" into interface and semantic components with a cheap measurement.
**Why Important:** A validated interface/semantics decomposition would simplify modality adaptation to stem engineering for a large class of shifts.
**Why Possibly Novel:** Stem-only sufficiency analysis across modality-shift types has not been systematically executed.
**Minimal Experiment:** Adapt stem-only vs LoRA vs full across 6 modality shifts at matched data; decompose recovery fractions; correlate residuals with semantic-shift measures.
**Main Risk:** Stem capacity choices (kernel structure) may drive results more than the interface principle.

### IDEA-B-0271 — Allocated versus used: effective-rank dynamics of LoRA training on dense tasks
**One-sentence idea:** Measure the effective rank actually utilized by trained LoRA updates (spectral concentration of the learned BA product) across tasks, testing whether dense tasks exploit allocated rank differently than classification and whether utilization predicts when rank increases help.
**Problem:** Rank is allocated blindly because nobody measures how much of it training actually uses—the utilization structure could explain contradictory rank-sensitivity findings and provide a principled stopping rule for rank growth.
**Core Hypothesis:** Trained updates concentrate spectrally well below allocated rank for classification-like adaptation but utilize substantially more rank for dense tasks (spatially heterogeneous corrections need more directions), and utilization saturation—not performance saturation—predicts the rank beyond which allocation is wasted, giving an online rank-sizing signal.
**Why Important:** Replaces rank grid search with a measurable utilization diagnostic and reveals a structural difference in what dense adaptation demands.
**Why Possibly Novel:** Effective-rank utilization analysis across task types is missing from the PEFT literature.
**Minimal Experiment:** Train LoRA across rank ladders on classification and segmentation adaptations; track spectral utilization dynamics; validate utilization-based rank prediction against grid-search outcomes.
**Main Risk:** Spectral utilization may be optimizer-dependent (Adam's preconditioning shapes spectra).

### IDEA-B-0272 — Capacity as regularization: are small adapters implicitly noise-robust?
**One-sentence idea:** Test whether low-capacity PEFT confers implicit robustness to label noise in fine-tuning data—the constrained update cannot fit structured annotation errors—making PEFT strictly preferable to full fine-tuning for noisy medical labels beyond its efficiency benefits.
**Problem:** Medical fine-tuning data is systematically noisy (rushed annotations, convention mixtures), noise-robust training methods add complexity, and an implicit regularization already present in PEFT would change the cost-benefit of both.
**Core Hypothesis:** Under controlled label-noise injection, the PEFT-versus-full-FT performance gap reverses sign as noise increases (full FT fits the noise, low-rank cannot), the protection scales inversely with adapter capacity in a lawful way, and the effect is strongest for spatially structured noise (boundary offsets) that low-rank updates are geometrically unable to express.
**Why Important:** Would establish noise regimes where PEFT is the accuracy-optimal choice—not a compromise—inverting how practitioners frame the efficiency-quality tradeoff.
**Why Possibly Novel:** The implicit noise-robustness of constrained adaptation has not been characterized for dense prediction.
**Minimal Experiment:** Fine-tune across noise-type × noise-level × adapter-capacity grids; locate gap reversals; test the structured-noise mechanism via noise-geometry manipulations.
**Main Risk:** Real annotation noise may differ from injected models enough to shift the reversal points.
### IDEA-B-0273 — Hypernetwork-generated adapters from unlabeled domain samples
**One-sentence idea:** Train a hypernetwork that maps a handful of unlabeled target-domain images to LoRA weights directly, testing whether zero-label, zero-gradient-step adapter generation can approach conventionally trained adapters for segmentation.
**Problem:** Every new domain currently requires an optimization run with labels; if adaptation updates are predictable from domain appearance alone (because shifts of a given type induce similar corrections), adaptation could become a single forward pass.
**Core Hypothesis:** Across a training distribution of domains, the mapping from unlabeled domain statistics to useful adapter weights is learnable, generated adapters recover a substantial fraction of trained-adapter gains on held-out domains within the shift families seen in meta-training, and the recovery fraction collapses predictably outside those families—defining the method's honest envelope.
**Why Important:** Instant adaptation would change deployment workflows (per-hospital adapters generated at install time from a calibration scan), and the envelope characterization tells users when to trust it.
**Why Possibly Novel:** Amortized adapter generation for dense prediction, with an explicit generalization-envelope analysis, is largely unexplored.
**Minimal Experiment:** Meta-train the hypernetwork over a corpus of domain-adaptation pairs; evaluate generated adapters on held-out domains inside and outside the shift families; map the recovery envelope.
**Main Risk:** The domain-to-update mapping may be too multimodal for regression, requiring generative formulations.

### IDEA-B-0274 — Spectral-token adapters: global structure adaptation with tiny parameter budgets
**One-sentence idea:** Adapt segmentation models through learned filters on the spectral decomposition of token features (global mixing with few parameters), testing whether globally structured shifts (illumination fields, bias gradients, large-organ context) are better served by spectral than spatially local adapters.
**Problem:** Standard adapters modify computation token-locally, making globally coherent corrections parameter-expensive to express—yet many medical and monitoring shifts are precisely global (field inhomogeneity, illumination gradients).
**Core Hypothesis:** Spectral-domain adapters express global corrections with orders-of-magnitude fewer parameters than local adapters at matched quality on global-shift tasks (bias-field-type shifts), while losing to local adapters on structure-specific shifts—establishing a shift-structure-conditioned adapter-type selection rule with a cheap diagnostic (spatial autocorrelation of the residual shift).
**Why Important:** Adds a missing tool to the PEFT toolbox for a well-defined shift class and grounds adapter choice in shift structure.
**Why Possibly Novel:** Spectral parameterization of adapters for dense-task adaptation is undeveloped.
**Minimal Experiment:** Implement spectral adapters; compare against LoRA at matched budgets on global-shift and local-shift task batteries; validate the autocorrelation diagnostic.
**Main Risk:** Token-spectral operations may interact poorly with attention's existing global mixing, muddying attribution.

### IDEA-B-0275 — Inference-time capacity: prompt ensembles versus trained adapters at matched total compute
**One-sentence idea:** Compare spending a fixed compute budget on training-time capacity (an adapter) versus inference-time capacity (ensembling multiple learned prompts per image), mapping when inference-compute substitutes for trained parameters in dense adaptation.
**Problem:** The train-once-infer-cheap convention ignores deployments with idle inference capacity and no training infrastructure (edge devices with intermittent load), where inference-time adaptation strategies could substitute—but the exchange rate between the two capacity types is unmeasured.
**Core Hypothesis:** Prompt-ensemble inference recovers a substantial fraction of adapter gains without any backbone training (with the fraction largest for uncertainty-type errors and smallest for systematic-bias errors), yielding an error-type-dependent substitution law that lets deployments choose capacity placement by their infrastructure constraints.
**Why Important:** Formalizes a trade every resource-constrained deployment implicitly faces, in the spirit of inference-scaling analyses now central to LLMs.
**Why Possibly Novel:** Train-time versus inference-time capacity accounting for dense-prediction adaptation is unexamined.
**Minimal Experiment:** Adapt via adapters vs k-prompt ensembles at matched total compute across error-type-stratified tasks; fit substitution curves.
**Main Risk:** Fair compute accounting across the two regimes requires careful, contestable bookkeeping.

### IDEA-B-0276 — Matryoshka adapters: one training run, every deployment size
**One-sentence idea:** Train a single nested adapter whose rank-ordered sub-adapters can be truncated at deployment to any parameter budget, and measure the quality cost of sliced sub-adapters relative to individually trained adapters at each size.
**Problem:** Organizations serve heterogeneous hardware (workstations to edge probes) and currently train separate adapters per budget—multiplying training costs and creating version-consistency risks across the fleet.
**Core Hypothesis:** Nested training with importance-ordered rank structure yields sub-adapters within a small margin of individually trained equivalents across a wide budget range (the adaptation solution space admits nested approximations), with the nesting penalty concentrated at the smallest budgets where solution geometry differs qualitatively.
**Why Important:** One-run-serves-all-budgets would simplify fleet deployment operationally and guarantee behavioral consistency across device tiers—a property regulators favor.
**Why Possibly Novel:** Nested elastic structure for adaptation modules (rather than backbone widths) is unexplored for dense tasks.
**Minimal Experiment:** Train matryoshka adapters on 4 adaptation tasks; slice at 5 budgets; compare against individually trained adapters; characterize the penalty structure.
**Main Risk:** Nested constraints may harm the full-rank optimum enough to make the scheme unattractive at the high end.

### IDEA-B-0277 — Adapter-subspace Monte Carlo: cheap epistemic uncertainty from the adaptation manifold
**One-sentence idea:** Generate uncertainty estimates by sampling within the low-dimensional adapter subspace (perturbing or dropout-masking adapter components) at inference, testing whether adaptation-manifold uncertainty captures domain-shift epistemic error at a fraction of deep-ensemble cost.
**Problem:** Epistemic uncertainty for adapted models is priced at full-ensemble cost (training multiple adaptations), while the adapter subspace—which concentrates exactly the domain-specific knowledge whose reliability is in question—offers a natural, untested cheap sampling space.
**Core Hypothesis:** Adapter-subspace sampling produces uncertainty that correlates with adaptation-related errors (shift-boundary cases, underrepresented target strata) nearly as well as adapter deep-ensembles at 1/10 the training cost, while remaining blind to backbone-inherited errors—a scoped-but-useful uncertainty whose scope is precisely characterizable.
**Why Important:** Makes epistemic uncertainty affordable for every adapted deployment, with an honest statement of what it can and cannot flag.
**Why Possibly Novel:** The adapter subspace as an uncertainty sampling manifold has not been developed.
**Minimal Experiment:** Compare adapter-subspace MC against adapter ensembles and single models on error-attribution-stratified evaluations across 4 adapted deployments.
**Main Risk:** Subspace perturbation scales need per-task calibration that could erode the cheapness claim.

### IDEA-B-0278 — Does the adapter create a new attack surface? Adversarial robustness of the adaptation subspace
**One-sentence idea:** Test whether PEFT-adapted models inherit their backbone's adversarial robustness or acquire a concentrated new vulnerability in the low-dimensional adapter subspace that attackers can target specifically.
**Problem:** Security audits certify backbones, adapters are added post-audit as "minor" changes, but a low-rank modification concentrated on task-critical features may be exactly the efficient attack direction—an unexamined gap between audit practice and deployment reality.
**Core Hypothesis:** Attacks constructed to excite the adapter subspace degrade adapted-task performance at substantially lower perturbation budgets than attacks on the full model (the adapter concentrates task-critical sensitivity), the vulnerability grows as rank shrinks (more concentration), and adversarial training within the adapter subspace alone restores robustness cheaply.
**Why Important:** Establishes whether the PEFT deployment pattern silently invalidates backbone security certifications—a question regulated industries need answered.
**Why Possibly Novel:** Subspace-targeted adversarial analysis of PEFT has not been performed for dense prediction.
**Minimal Experiment:** Craft subspace-projected attacks against adapted segmenters across ranks; compare perturbation-budget curves against full-model attacks; test subspace adversarial training.
**Main Risk:** Subspace attacks require white-box adapter knowledge; the threat model needs careful, honest scoping.

### IDEA-B-0279 — Label-free PEFT: distilling prompt-ensemble consensus into adapters
**One-sentence idea:** Adapt segmentation models to new domains without any labels by distilling the consensus of prompt-perturbation ensembles (the base model's own agreement structure on unlabeled target data) into a lightweight adapter, and measure how close label-free PEFT gets to supervised PEFT.
**Problem:** Most deployment domains have unlabeled data in abundance and labels not at all; existing unsupervised adaptation either drifts (self-training) or under-delivers (feature alignment), while promptable models contain an internal consistency signal that has not been harnessed for weight adaptation.
**Core Hypothesis:** Prompt-consensus pseudo-labels are systematically more reliable than confidence-filtered standard pseudo-labels on shifted data (agreement across prompts filters shift-induced instability), so consensus-distilled adapters recover a meaningful fraction of supervised-PEFT gains with near-zero collapse risk, quantifiable as a fraction-of-supervised-gain metric across shift types.
**Why Important:** A safe label-free adaptation recipe would be applied at essentially every deployment of promptable segmenters.
**Why Possibly Novel:** Prompt-consensus as the distillation target for label-free weight adaptation is a mechanism unique to promptable models and undeveloped.
**Minimal Experiment:** Distill consensus into adapters across 6 shifted domains; compare against supervised PEFT, TENT-style TTA, and standard self-training on gain and collapse-rate metrics.
**Main Risk:** Consensus may be systematically wrong (agreeing on the same shifted mistake), capping reliability where all prompts share a bias.

### IDEA-B-0280 — Cross-scale adapter transplantation: reusing adaptations across model sizes
**One-sentence idea:** Test whether adapters trained on a small model variant can be transformed and transplanted onto a larger variant of the same family (via subspace alignment between the two models' representations), avoiding re-adaptation costs at every scale tier.
**Problem:** Fleets run multiple model scales (edge/small, server/large), adaptations are trained per scale at multiplied cost, and whether adaptation knowledge is scale-portable—given the models share training lineage—has not been tested.
**Core Hypothesis:** Adapter updates encode corrections in representation directions that correspond across scales of the same model family (findable by linear alignment on shared calibration data), so transplanted-then-lightly-tuned adapters reach target performance with a small fraction of the labels and compute of scratch adaptation at the new scale—with transplant quality predicted by cross-scale representation-alignment scores.
**Why Important:** Scale-portable adaptation would collapse the adaptation cost matrix (domains × scales) to a single row—major operational leverage.
**Why Possibly Novel:** Cross-scale transplantation of adaptation modules with alignment-based transformation is unexplored.
**Minimal Experiment:** Align representations across two model scales; transplant transformed adapters; measure zero-shot and few-label-tuned transplant performance against scratch adaptation.
**Main Risk:** Representation correspondence across scales may be too nonlinear for practical alignment.

---

## Cluster 9 — Surprising Empirical Phenomena Worth Testing (IDEA-B-0281 … IDEA-B-0315)

### IDEA-B-0281 — The off-center click advantage: is the prompt sweet spot where users don't click?
**One-sentence idea:** Rigorously test the anecdotal observation that slightly off-center clicks sometimes yield better SAM masks than centroid clicks, and if confirmed, map the geometry of the per-object "prompt sweet spot" and its predictability.
**Problem:** Evaluation and interface conventions assume the centroid is the canonical best prompt, but decoder behavior near object centers (ambiguity between part and whole, symmetric attention competition) may make centers locally suboptimal—an untested assumption baked into protocols everywhere.
**Core Hypothesis:** For a measurable class of objects (those with internal part structure or central texture anomalies), the IoU-maximizing click location is systematically displaced from the centroid toward specific geometric loci (skeleton branch points, texture-homogeneous zones), and the displacement is predictable from image evidence—enabling automatic prompt-placement optimization.
**Why Important:** If centers are suboptimal, every centroid-based evaluation underestimates model capability and every interface nudging users toward centers costs accuracy for free.
**Why Possibly Novel:** Prompt-placement response surfaces have never been mapped at object-population scale.
**Minimal Experiment:** Dense click-grid evaluation over thousands of objects across datasets; map optimal-click displacement statistics; train a placement predictor and test its gain over centroid prompting.
**Main Risk:** The effect may be small and object-class-specific, dissolving into noise at population scale.

### IDEA-B-0282 — Non-monotonic interactive refinement: when more clicks make masks worse
**One-sentence idea:** Quantify how often adding a correction click degrades SAM-family mask quality (non-monotonic refinement), characterize the conditions triggering it, and identify the decoder mechanism responsible.
**Problem:** Interactive pipelines assume monotone improvement with user effort, but practitioners observe occasional regressions after corrections—if regressions are common, click-efficiency metrics and user trust are both built on a false monotonicity assumption.
**Core Hypothesis:** Click-induced regressions occur at a measurable, non-trivial rate concentrated in identifiable conditions (corrections near ambiguity boundaries triggering candidate-mask mode switches), the mechanism is decoder mode competition rather than noise (verifiable by candidate-trajectory logging), and a mode-stabilized decoding rule eliminates most regressions without harming normal refinement.
**Why Important:** Regression-free refinement is a basic usability contract; violating it silently corrupts both user experience and interactive benchmarks.
**Why Possibly Novel:** The non-monotonicity phenomenon has never been measured, attributed, or systematically mitigated.
**Minimal Experiment:** Run simulated and logged-human correction sequences at scale; measure regression rates and conditions; log candidate trajectories to test the mode-switch mechanism; prototype stabilized decoding.
**Main Risk:** Regression rates may depend heavily on correction-simulation policy, requiring human-log validation.

### IDEA-B-0283 — Unexplained cross-organ transfer: does fine-tuning recalibrate objectness rather than features?
**One-sentence idea:** Investigate the reported phenomenon that fine-tuning a promptable segmenter on one anatomy improves unrelated anatomies, testing whether the gain travels through generic objectness/boundary recalibration rather than shared appearance features.
**Problem:** Cross-task transfer between visually unrelated anatomies contradicts feature-similarity accounts of transfer and suggests fine-tuning changes something task-general—identifying what would reshape how adaptation sets are designed.
**Core Hypothesis:** The transferred component lives in late decoder/objectness calibration (verifiable by component-swap experiments: transplanting only the fine-tuned decoder confers most of the unrelated-organ gain), implying medical fine-tuning largely teaches "medical mask conventions" rather than anatomy-specific appearance—so a small diverse convention-tuning set could replace organ-specific collections for a large fraction of the gain.
**Why Important:** Would redefine the data-collection strategy for medical foundation-model adaptation around conventions rather than coverage.
**Why Possibly Novel:** Component-level attribution of cross-anatomy transfer has not been performed.
**Minimal Experiment:** Fine-tune on single anatomies; measure unrelated-anatomy gains; run encoder/decoder swap matrices to localize the transferred component; test convention-set training.
**Main Risk:** Transfer magnitudes may be too small for reliable component attribution.

### IDEA-B-0284 — Augmentation inversion at low data: when standard recipes actively hurt
**One-sentence idea:** Map the data-regime boundary below which standard heavy augmentation recipes (designed for large-scale training) degrade foundation-model fine-tuning rather than helping, and identify which augmentation components invert first.
**Problem:** Augmentation defaults were tuned for from-scratch large-data training, few-shot fine-tuning inherits them unexamined, and anecdotes suggest they can hurt—but the inversion boundary and its mechanism are unmapped, so practitioners can't know which side they're on.
**Core Hypothesis:** Below a measurable shot-count threshold, aggressive geometric/photometric augmentation degrades performance by pulling scarce examples off the target distribution faster than it adds invariance (mechanistically: augmented-batch gradient direction decorrelates from true-distribution gradient at low n), the inversion point varies by augmentation type in a consistent order, and shot-count-scheduled augmentation strength dominates any fixed recipe.
**Why Important:** Few-shot fine-tuning is the modal use case for foundation models; a wrong default silently taxes thousands of projects.
**Why Possibly Novel:** Augmentation dose-response as a function of shot count, with gradient-alignment mechanism analysis, has not been mapped for dense tasks.
**Minimal Experiment:** Sweep augmentation strength × shot count grids across 4 tasks; locate inversion boundaries per augmentation type; test the gradient-decorrelation mechanism and scheduled strength.
**Main Risk:** Inversion points may vary across datasets enough to prevent a usable general boundary.

### IDEA-B-0285 — Compression that helps: does JPEG act as a matched filter for smoke?
**One-sentence idea:** Test the counterintuitive observation that mild lossy compression sometimes improves smoke segmentation, evaluating the hypothesis that compression's frequency truncation suppresses exactly the high-frequency background clutter that generates smoke false positives.
**Problem:** Preprocessing dogma treats compression purely as degradation, but if amorphous low-frequency targets like smoke gain discriminability when high-frequency distractors are removed, deployment pipelines are leaving free accuracy on the table—and the robustness literature's monotone-degradation assumption is wrong for a target class.
**Core Hypothesis:** Segmentation quality for low-frequency amorphous targets is non-monotonic in compression strength with a measurable optimum at mild compression (the effect absent for high-frequency targets), the mechanism is spectral overlap between target and clutter (predictable per class from their power-spectra separation), and a learned band-suppression filter beats JPEG at the same principle—confirming the matched-filter account.
**Why Important:** Reveals that input "quality" is target-relative, with immediate preprocessing implications for smoke/fog/haze systems and a caution for robustness benchmarking.
**Why Possibly Novel:** Beneficial-degradation phenomena and their spectral mechanism have not been characterized for segmentation.
**Minimal Experiment:** Sweep compression strength across smoke and solid-object segmentation; test non-monotonicity; compute spectral-separation predictors; compare against designed band filters.
**Main Risk:** The effect may be dataset-specific (certain clutter types) rather than a general spectral phenomenon.

### IDEA-B-0286 — Subgroup regression under fine-tuning: who loses when the average improves?
**One-sentence idea:** Systematically test whether fine-tuning that improves average performance regresses identifiable subgroups (rare acquisition settings, atypical anatomy, minority demographics) below the zero-shot baseline—making the pre-fine-tuning model strictly better for some patients.
**Problem:** Fine-tuning decisions are made on aggregate metrics, subgroup regressions would be clinically and ethically material, and the zero-shot-versus-fine-tuned comparison at subgroup granularity is simply not part of current adaptation practice.
**Core Hypothesis:** Fine-tuning on realistically skewed target data produces measurable subgroup regressions relative to zero-shot in a substantial fraction of adaptation runs (the adapted model trades tail robustness inherited from web-scale pretraining for target-majority fit), regressions concentrate in subgroups underrepresented in fine-tuning data relative to pretraining, and lightweight interpolation between base and adapted weights recovers most subgroup loss at minor average cost.
**Why Important:** Establishes whether the field's default adaptation practice violates "do no harm" at subgroup level—and provides the monitoring protocol to catch it.
**Why Possibly Novel:** Zero-shot-versus-fine-tuned subgroup regression auditing has not been formalized for dense medical tasks.
**Minimal Experiment:** Run standard adaptations across datasets with subgroup metadata; compute subgroup-level base-versus-adapted deltas; test weight-interpolation mitigation.
**Main Risk:** Subgroup metadata availability limits which regressions are observable.

### IDEA-B-0287 — Color as a saboteur: when grayscale conversion improves RGB medical segmentation
**One-sentence idea:** Test the reported phenomenon that discarding color improves some endoscopy/dermoscopy segmentation tasks, evaluating whether color channels carry shortcut signals (lighting, device tints) whose removal forces more robust structure-based features.
**Problem:** More input information should never hurt in theory, but if color correlates with site/device confounds more than with targets, models exploit it as a shortcut—and the phenomenon, if real, indicts standard input pipelines for a whole modality class.
**Core Hypothesis:** For tasks where chromatic target signal is weak (structure-defined polyps) and chromatic confounds are strong (device white balance, illumination), grayscale-trained models transfer measurably better across sites while matching in-site performance—with the effect direction predictable per task from a chromatic signal-to-confound ratio computable on training data.
**Why Important:** A validated predictor would tell every medical vision team when the standard RGB pipeline is actively hurting cross-site robustness.
**Why Possibly Novel:** The color-as-shortcut hypothesis has not been tested with site-transfer-controlled experiments and a per-task predictor.
**Minimal Experiment:** Train color/grayscale/decorrelated variants across multi-site endoscopy and dermoscopy datasets; measure in-site vs cross-site gaps; validate the ratio predictor.
**Main Risk:** Color genuinely matters for some target subtypes (pigmented lesions), demanding careful stratification.

### IDEA-B-0288 — Bigger models, smaller structures: an inverse scaling pocket for dense prediction?
**One-sentence idea:** Test whether larger foundation-segmenter variants perform relatively worse on very small structures than smaller variants—an inverse-scaling pocket where capacity is allocated to global coherence at the expense of tiny-target fidelity.
**Problem:** Scaling is assumed monotone-beneficial across all strata, procurement defaults to the largest affordable model, but if scale redistributes capacity away from small-structure precision, the default is wrong for exactly the medical and early-detection tasks where small things matter most.
**Core Hypothesis:** Size-stratified evaluation reveals a crossing: larger variants dominate on medium/large structures while smaller variants match or beat them on structures below a threshold size (mechanism: deeper attention integrates global context that overrides weak local evidence, verifiable via attention-rollout analysis), and the crossing replicates across model families—establishing stratum-conditional model selection.
**Why Important:** An inverse-scaling pocket would change model-selection guidance for small-structure-critical deployments and expose a blind spot in scale-is-all reasoning.
**Why Possibly Novel:** Size-stratified scaling analysis for dense prediction has not been reported.
**Minimal Experiment:** Evaluate model-scale ladders (within families) on size-stratified suites across domains; test for crossings; run attention-integration analyses on small-target failures.
**Main Risk:** Scale ladders confound capacity with training-data and recipe differences within some families.

### IDEA-B-0289 — When does decoder pretraining matter? The random-decoder anomaly
**One-sentence idea:** Investigate the observation that randomly initialized decoders sometimes match pretrained decoders atop frozen encoders, mapping when decoder pretraining adds value and what that reveals about where dense-task knowledge lives.
**Problem:** The field pretrains and ships full encoder-decoder stacks, but if decoder knowledge is cheap to re-derive from good frozen features, decoder pretraining is wasted effort—and conversely, identifying where it matters locates the tasks whose knowledge genuinely resides in decoding.
**Core Hypothesis:** Decoder pretraining value is near-zero when encoder features are strongly linearly decodable for the task (the decoder only reformats) and grows sharply with feature-task misalignment (the decoder must compute), so a cheap feature-probing score predicts per-task whether to transfer, retrain, or redesign decoders—unifying scattered anomalous reports.
**Why Important:** Decoder decisions are made constantly in adaptation pipelines; a predictive rule replaces cargo-cult transfer of decoder weights.
**Why Possibly Novel:** Decoder-pretraining value as a function of measured feature-task alignment has not been characterized.
**Minimal Experiment:** Train random-vs-pretrained decoders on frozen features across tasks spanning alignment levels; correlate the pretraining gain with probing scores; validate the decision rule.
**Main Risk:** Decoder architectures differ in retrainability, adding variance beyond the alignment story.

### IDEA-B-0290 — Free accuracy from test-time augmentation: why do prompted models benefit unevenly?
**One-sentence idea:** Characterize when test-time augmentation ensembling (averaging masks across augmented copies) helps prompted segmentation, testing the hypothesis that TTA gains concentrate on specific error types and can be predicted—and thus selectively applied—per image.
**Problem:** TTA is applied uniformly or not at all, its compute cost is per-image, and for prompted models the interaction between augmentation and prompt geometry (prompts must transform consistently) creates failure modes nobody has mapped—leaving free accuracy unclaimed and wasted compute unexamined.
**Core Hypothesis:** TTA gains are strongly image-conditional (large for boundary-uncertainty errors, near-zero for semantic errors, negative when prompt transformation lands near decision discontinuities), a cheap instability probe (two-augmentation disagreement) predicts per-image TTA value, and selective TTA achieves most of uniform-TTA's gain at a small fraction of its cost.
**Why Important:** Converts TTA from a blunt cost-accuracy trade into a targeted tool, and maps a prompt-specific failure mode of a ubiquitous technique.
**Why Possibly Novel:** Conditional-value analysis of TTA for prompted dense models has not been done.
**Minimal Experiment:** Measure per-image TTA deltas at scale across datasets; train the value predictor; evaluate selective-TTA policies on accuracy-per-FLOP.
**Main Risk:** The value predictor may capture dataset-specific difficulty proxies that don't transfer.

### IDEA-B-0291 — Anti-curriculum for dense tasks: does hard-first training beat easy-first?
**One-sentence idea:** Test the counterintuitive reports that training on hard examples first can beat easy-first curricula for segmentation fine-tuning, and connect the outcome to boundary-learning dynamics (which features are acquired in which training phase).
**Problem:** Curriculum intuitions imported from cognitive analogies dominate practice without dense-task evidence, and if hard-first wins in fine-tuning regimes (where a pretrained model doesn't need gentle introduction), standard data ordering advice is backwards for the modal use case.
**Core Hypothesis:** For fine-tuning pretrained dense models, hard-first ordering accelerates boundary-precision acquisition (hard examples carry the gradient signal for exactly what pretraining lacks) and reaches higher final boundary metrics, while easy-first only wins from-scratch training—resolving the contradiction in curriculum reports via the pretraining-state variable.
**Why Important:** Data ordering is free; knowing the correct direction for the fine-tuning regime is immediately actionable everywhere.
**Why Possibly Novel:** Curriculum-direction analysis conditioned on pretraining state, with boundary-dynamics tracking, has not been executed for dense tasks.
**Minimal Experiment:** Run difficulty-ordered (both directions, plus random) fine-tuning across tasks and pretraining states; track boundary-versus-region metric trajectories; test the interaction.
**Main Risk:** Difficulty scoring choices may drive results more than ordering direction.

### IDEA-B-0292 — Training-time prompt jitter: calibration benefits without accuracy costs?
**One-sentence idea:** Test the observation that injecting prompt-position noise during promptable-model fine-tuning improves confidence calibration while leaving accuracy unchanged, and characterize this accuracy-calibration decoupling as a training phenomenon.
**Problem:** Calibration interventions usually trade accuracy or add post-hoc stages, and if a zero-cost training-time perturbation improves calibration through a distinct mechanism (teaching the model its own conditional variability), the finding would both help practice and illuminate what mask confidence represents.
**Core Hypothesis:** Prompt-jitter training leaves the accuracy frontier unchanged while measurably flattening calibration error (mechanism: the model learns the prompt-conditional output variance, which is exactly what its confidence should express), the effect scales with jitter magnitude up to a breakdown point, and it composes additively with post-hoc calibration—indicating a genuinely different mechanism.
**Why Important:** Free calibration would be adopted universally in promptable-model training, and the mechanism clarifies confidence semantics for interactive systems.
**Why Possibly Novel:** Training-perturbation effects on calibration (decoupled from accuracy) have not been isolated for prompted dense models.
**Minimal Experiment:** Fine-tune with jitter ladders; jointly track accuracy and calibration; test composition with temperature scaling; probe the variance-learning mechanism.
**Main Risk:** The decoupling may be an artifact of specific calibration metrics; needs multi-metric verification.

### IDEA-B-0293 — The freezing paradox: why does freezing early layers hurt more for the "closer" domain?
**One-sentence idea:** Investigate reports that freezing early encoder layers harms adaptation to modality-distant domains (CT) less than to seemingly closer domains (endoscopy), overturning the depth-distance heuristic that guides freezing decisions.
**Problem:** The standard heuristic—freeze more for closer domains—drives freezing choices everywhere, but scattered contradictions suggest the mapping between perceived domain distance and required adaptation depth is wrong, and no one has measured actual adaptation-depth demand across domains.
**Core Hypothesis:** Adaptation-depth demand tracks low-level statistics mismatch (noise character, dynamic range, spectral content) rather than semantic distance, so photographically-similar-but-sensor-different domains (endoscopy: extreme illumination, specularity) need early-layer plasticity while semantically alien but statistically tame domains (windowed CT) do not—predictable by early-layer feature-drift measurement, replacing the depth-distance heuristic.
**Why Important:** Freezing decisions are among the most common adaptation choices; correcting the heuristic prevents systematic misconfiguration.
**Why Possibly Novel:** Empirical adaptation-depth-demand mapping against statistics-versus-semantics distance decomposition has not been published.
**Minimal Experiment:** Run freezing-depth ladders across domains spanning the statistics/semantics distance grid; measure demand curves; validate the drift-based predictor.
**Main Risk:** Freezing interacts with learning-rate schedules, requiring careful optimization control.

### IDEA-B-0294 — Bimodal test losses: detecting pretraining contamination from loss distributions alone
**One-sentence idea:** Test whether per-image loss distributions on evaluation sets exhibit mixture structure (a memorized low-loss mode and a genuine-generalization mode) that reveals pretraining contamination without any access to the pretraining corpus.
**Problem:** Contamination auditing requires corpus access nobody has, but if memorized images betray themselves through anomalously low loss relative to their difficulty, contamination becomes statistically detectable from model behavior alone—turning an intractable provenance problem into a mixture-modeling problem.
**Core Hypothesis:** Evaluation-set loss residuals (after regressing out measurable difficulty) are bimodal for contaminated benchmarks and unimodal for verified-clean ones, the low-residual mode's images disproportionately have web-visible duplicates (external validation), and mode-membership provides per-image contamination probabilities that materially change benchmark conclusions when used as weights.
**Why Important:** Provides the community a corpus-free contamination detector applicable to every existing benchmark and model.
**Why Possibly Novel:** Difficulty-adjusted loss-mixture analysis for dense-prediction contamination detection has not been developed.
**Minimal Experiment:** Fit difficulty models and residual mixtures across benchmarks and model families; validate mode membership against web-duplicate retrieval; re-evaluate benchmarks with contamination weights.
**Main Risk:** Difficulty regression may be too weak to separate modes, blurring memorization into natural easiness.

### IDEA-B-0295 — Super-resolution as preprocessing: real detail, useful smoothing, or harmful hallucination?
**One-sentence idea:** Decompose why upscaling images with super-resolution models before segmentation sometimes helps—separating genuine detail recovery, beneficial noise smoothing, and hallucinated structure—and determine when each component dominates.
**Problem:** SR preprocessing is adopted on aggregate gains without knowing whether the mechanism is legitimate (recovering real information) or dangerous (hallucinating plausible boundaries that segmenters then trace), a distinction that determines whether the practice is safe for clinical use.
**Core Hypothesis:** SR preprocessing gains decompose measurably (via frequency-controlled and hallucination-controlled SR variants): most gains on natural-image tasks come from smoothing and resampling effects reproducible by non-generative filters, while genuine detail recovery is rare and hallucination actively harms boundary reliability on medical data—implying cheap filters should replace SR in most pipelines and SR should be barred from measurement-critical ones.
**Why Important:** Separates a safe practice from an unsafe one that current aggregate evaluation cannot distinguish—directly relevant to medical deployment guidelines.
**Why Possibly Novel:** Mechanism decomposition of SR-for-segmentation (versus aggregate benchmarking) has not been performed.
**Minimal Experiment:** Compare segmentation under {bicubic, non-generative filters, SR with hallucination-strength ladders} across natural and medical tasks; attribute gains per mechanism; measure boundary-reliability effects.
**Main Risk:** Hallucination strength is hard to isolate as a single controllable variable across SR architectures.

### IDEA-B-0296 — The soft-label sharpness tradeoff: mapping and breaking the smoothing dilemma for dense prediction
**One-sentence idea:** Quantify the tradeoff by which label smoothing improves segmentation calibration while degrading boundary sharpness, and test schedule- and space-varying smoothing (smooth early training or smooth interiors only) as ways to break the tradeoff.
**Problem:** Teams choose between calibrated-but-soft and sharp-but-overconfident models via a global smoothing constant, without knowing the tradeoff's shape or whether it is fundamental—both determinable with targeted experiments.
**Core Hypothesis:** The calibration-sharpness tradeoff under uniform smoothing follows a consistent frontier across tasks, but the frontier is not fundamental: boundary-distance-conditioned smoothing (full supervision sharpness at edges, smoothing in interiors) achieves calibration comparable to uniform smoothing with near-zero boundary degradation—because the two properties are controlled by spatially disjoint pixel populations.
**Why Important:** Delivers calibrated and sharp dense models simultaneously—both properties are deployment requirements that currently compete.
**Why Possibly Novel:** Spatially structured smoothing as a frontier-breaking mechanism has not been tested for segmentation.
**Minimal Experiment:** Map the uniform-smoothing frontier across tasks; implement distance-conditioned smoothing; test frontier dominance; verify the disjoint-population mechanism.
**Main Risk:** Interior calibration may not suffice for downstream uses that consume boundary confidences specifically.

### IDEA-B-0297 — Weak partners, strong rare-class recall: the asymmetric value of heterogeneous ensembles
**One-sentence idea:** Test the phenomenon that ensembling a strong model with a much weaker but architecturally different one improves rare-class and rare-stratum recall even while degrading nothing else—locating when diversity beats strength locally.
**Problem:** Ensemble practice pairs similar strong models, weak models are discarded as obsolete, but if weak models retain coverage of strata the strong model abandoned during optimization (rare classes, unusual scales), discarding them throws away irreplaceable recall—an unexamined asymmetry in ensemble value.
**Core Hypothesis:** Strong-weak heterogeneous ensembles improve tail-stratum recall beyond strong-strong ensembles at matched compute (the weak partner's errors are anticorrelated exactly on strata where the strong model's training distribution was thin), the effect is predictable from per-stratum error-correlation profiles, and stratum-gated fusion (weak model consulted only on its advantage strata) captures the gains without the weak model's global noise.
**Why Important:** Rescues discarded models as tail-coverage assets and gives long-tail deployments a cheap recall mechanism.
**Why Possibly Novel:** Asymmetric ensemble-value analysis conditioned on strata has not been formalized.
**Minimal Experiment:** Build strong-weak and strong-strong ensembles at matched compute across long-tail segmentation tasks; measure per-stratum deltas; test gated fusion.
**Main Risk:** Gains may vanish when the strong model is trained with modern tail-aware recipes.

### IDEA-B-0298 — Scars from restarts: do learning-rate warm restarts permanently damage boundary quality?
**One-sentence idea:** Test the observation that cyclic learning-rate restarts cause boundary-metric dips that never fully recover in dense-prediction training—unlike region metrics which recover—suggesting boundary features live in sharper minima that restarts destroy.
**Problem:** Restart schedules imported from classification are used in segmentation training without dense-specific validation, and if fine boundary features are selectively fragile to perturbation, common schedules silently cap boundary quality—an invisible tax measurable only with metric-stratified trajectory tracking.
**Core Hypothesis:** Post-restart recovery is metric-asymmetric (region metrics recover fully, boundary metrics plateau below pre-restart levels), the asymmetry traces to curvature differences (boundary-relevant parameter directions show higher loss curvature, verifiable by Hessian spectrum analysis on metric-specific losses), and restart-free schedules or boundary-parameter-protected restarts eliminate the deficit.
**Why Important:** Identifies a concrete, avoidable training-schedule harm for every boundary-critical application.
**Why Possibly Novel:** Metric-stratified analysis of optimization-schedule effects on dense training has not been done.
**Minimal Experiment:** Train with and without restarts tracking stratified metrics; measure recovery asymmetries; run curvature analyses; test protected-restart variants.
**Main Risk:** Effects may be small at well-tuned restart amplitudes, making the phenomenon marginal.

### IDEA-B-0299 — The border penalty of resolution extrapolation
**One-sentence idea:** Characterize the phenomenon that ViT segmenters evaluated above their training resolution gain accuracy in image centers while losing it near borders, attribute it to positional-embedding extrapolation asymmetry, and test border-corrected embedding schemes.
**Problem:** Inference above training resolution is standard for dense tasks (more detail per token), the net gains hide a spatial redistribution (center improves, borders degrade), and applications with border-critical content (whole-slide tiles, panoramas, edge-entering fire) silently pay for the average improvement.
**Core Hypothesis:** Resolution extrapolation degrades positional-embedding fidelity super-linearly with distance from image center (interpolation is anchored to the center of the training grid), the border penalty is measurable and architecture-consistent, and boundary-anchored embedding recalibration eliminates most of it—converting a hidden spatial tradeoff into a uniform gain.
**Why Important:** Tiled and monitoring deployments process border pixels as often as centers; a corrected embedding turns a systematic weakness into a free improvement.
**Why Possibly Novel:** Spatially resolved analysis of resolution-extrapolation effects has not been published for dense prediction.
**Minimal Experiment:** Evaluate resolution ladders with position-stratified metrics across models; map the border penalty; test recalibrated embeddings.
**Main Risk:** Border effects mix positional extrapolation with attention edge artifacts requiring careful separation.

### IDEA-B-0300 — Objectness erosion: when self-supervised continued pretraining hurts promptable segmentation
**One-sentence idea:** Investigate the phenomenon that continued self-supervised pretraining (MAE-style) on target-domain data before supervised fine-tuning sometimes degrades promptable segmentation, testing whether reconstruction objectives erode the objectness/grouping structure that prompt decoding depends on.
**Problem:** The domain-adaptive-pretraining recipe (SSL on target, then fine-tune) is standard advice inherited from NLP and classification, but promptable segmentation relies on representational properties (grouping, boundary salience) that reconstruction objectives do not preserve and may actively trade away—an unexamined recipe conflict.
**Core Hypothesis:** MAE-style continued pretraining measurably degrades frozen-feature grouping quality (probeable before any fine-tuning) while improving pixel-reconstruction-aligned properties, the degradation propagates to prompted-segmentation performance in low-label fine-tuning regimes (insufficient supervision to rebuild grouping), and grouping-preserving SSL variants (contrastive or distillation-anchored) avoid the trap—defining which SSL is safe for promptable models.
**Why Important:** Corrects a default recipe at the intersection of two major practices before it becomes further entrenched in dense-model adaptation.
**Why Possibly Novel:** The SSL-objective-versus-objectness conflict for promptable models has not been isolated.
**Minimal Experiment:** Continue-pretrain with objective ladders; probe grouping properties; fine-tune across label budgets; map where each SSL objective helps or harms.
**Main Risk:** Effects may depend on pretraining duration and masking ratio in ways that complicate clean recommendations.

### IDEA-B-0301 — Stable mistakes: do early-training error maps predict final-model errors?
**One-sentence idea:** Test whether the spatial error maps of a dense model early in training predict the errors of the fully trained model well enough to drive annotation triage and hard-case mining from a fraction of the training compute.
**Problem:** Error-driven data strategies (mining, active labeling, curriculum) wait for trained models to reveal errors, paying full training cost per iteration; if errors are largely determined early (stable difficulty structure), the field is over-paying by an order of magnitude for the same information.
**Core Hypothesis:** Per-region error at 10–20% of training correlates strongly with final-model error for a stable majority of regions (persistent difficulty), the unstable minority is identifiable online by loss-trajectory variance, and early-error-guided annotation triage matches full-training-guided triage in downstream value at a fraction of compute.
**Why Important:** Cuts the compute cost of every error-driven data pipeline and characterizes a basic property of dense-learning dynamics.
**Why Possibly Novel:** Early-late error predictability has been studied for example-level classification but not spatially for dense prediction.
**Minimal Experiment:** Track per-region error trajectories across full training runs on 4 tasks; measure early-final correlation structure; run triage-value comparisons.
**Main Risk:** Predictability may break exactly for the boundary regions where triage matters most.

### IDEA-B-0302 — Are class labels dead weight for prompted models? Class-agnostic versus class-labeled supervision
**One-sentence idea:** Test whether class-agnostic mask supervision (no semantic labels) trains prompted segmenters as effectively as class-labeled supervision at equal pixel volume—and where semantic labels actually matter—challenging the assumption that semantics aid delineation.
**Problem:** Semantic labeling multiplies annotation cost, prompted models receive localization from users at inference (arguably making semantics redundant for delineation), and the marginal value of the semantic component of supervision has never been cleanly isolated for the prompted paradigm.
**Core Hypothesis:** For prompted delineation, class-agnostic supervision matches class-labeled supervision on boundary and region quality (semantics contribute nothing to tracing given localization), with class labels mattering only for ambiguity resolution (choosing among nested plausible masks)—so annotation budgets should buy more class-agnostic masks plus a small ambiguity-labeled subset, a strictly cheaper recipe.
**Why Important:** Could cut mask-annotation costs substantially across every prompted-model training effort by dropping a component that may be dead weight.
**Why Possibly Novel:** Component-isolated supervision valuation (semantics versus geometry) for prompted training is missing.
**Minimal Experiment:** Train prompted segmenters on class-stripped versus full supervision at matched volumes; evaluate delineation and ambiguity-resolution separately; test the mixed cheap recipe.
**Main Risk:** Semantics may aid delineation indirectly (feature shaping) at scales this experiment can't reach.

### IDEA-B-0303 — Prompts as shortcut blockers: are interactive models structurally more robust?
**One-sentence idea:** Test whether prompt-conditioned models resist context shortcuts (background-target correlations) better than unprompted models trained on identical data—because the prompt supplies localization that shortcuts otherwise provide—making interactivity a structural robustness mechanism.
**Problem:** Shortcut learning is fought with data curation and augmentation, while a structural difference between paradigms—prompted models don't need to learn "where" from context—could make part of the problem dissolve by architecture choice, a possibility nobody has isolated.
**Core Hypothesis:** Under controlled shortcut injection (targets correlated with context cues), unprompted models absorb the shortcut (large performance drop on de-correlated tests) while prompted models remain measurably more stable at matched clean accuracy—with the protection proportional to how much localization information the prompt carries (points < boxes < masks), confirming the mechanism.
**Why Important:** Would add "shortcut resistance" to the case for interactive designs in high-stakes imaging and quantify how much robustness a prompt buys.
**Why Possibly Novel:** Paradigm-level shortcut-susceptibility comparison under controlled correlation injection has not been executed.
**Minimal Experiment:** Inject graded context-target correlations into training data; train both paradigms; evaluate on correlation-broken tests; verify the prompt-information dose-response.
**Main Risk:** Prompted models may exploit subtler within-mask shortcuts that this design doesn't expose.

### IDEA-B-0304 — Style leaks through skips: do skip connections undermine cross-domain robustness?
**One-sentence idea:** Test the phenomenon that removing or bottlenecking encoder-decoder skip connections sometimes improves cross-domain segmentation—evaluating whether skips pipe domain-specific low-level statistics (style) directly into predictions, bypassing the domain-invariant deep pathway.
**Problem:** Skip connections are unquestioned dense-architecture dogma for boundary precision, but they structurally exempt low-level features from the abstraction that confers invariance—if style leaks through skips, the field's default architecture trades robustness for sharpness without anyone measuring the exchange rate.
**Core Hypothesis:** Skip-carried features encode domain identity far more strongly than bottleneck features (probeable), cross-domain degradation is disproportionately attributable to skip pathways (verifiable by skip-ablation and skip-swap interventions), and style-normalized skips (instance-normalized or spectrally filtered) retain boundary precision while removing most of the leaked fragility—breaking the assumed tradeoff.
**Why Important:** A robustness-preserving redesign of the most standard dense-architecture component would apply to virtually every deployed segmentation system.
**Why Possibly Novel:** Pathway-level domain-fragility attribution for skip connections has not been isolated.
**Minimal Experiment:** Probe domain decodability per pathway; run skip-ablation/normalization variants across cross-domain benchmarks; decompose robustness and sharpness effects.
**Main Risk:** Skip value varies with decoder design; findings need replication across architecture families.

### IDEA-B-0305 — Periodic performance in input size: aliasing between resolution and patch grid
**One-sentence idea:** Characterize the reported oscillation of segmentation quality with input resolution (periodic dips at specific sizes) as an aliasing interaction between resize interpolation and patch tokenization, and validate anti-aliased pipelines that remove it.
**Problem:** Resolution is treated as a monotone quality knob, but if quality oscillates with period related to patch size, deployments choosing "slightly larger" inputs may land on dips—and benchmark comparisons at different resolutions silently mix aliasing effects into model comparisons.
**Core Hypothesis:** Quality-versus-resolution curves exhibit statistically significant periodicity locked to patch-size harmonics (worst near resolutions where object boundaries beat against the token grid), thin structures suffer most, the phenomenon replicates across ViT families, and anti-aliased resizing plus sub-patch-aligned padding flattens the oscillation—recovering the dips for free.
**Why Important:** A free correction to a systematic artifact affecting every resolution decision and cross-paper comparison in ViT-based dense prediction.
**Why Possibly Novel:** Fine-grained resolution sweeps with periodicity analysis have not been published for dense tasks.
**Minimal Experiment:** Evaluate models across dense resolution sweeps (step 2–4 px); test periodicity spectrally; stratify by structure thinness; validate anti-aliasing fixes.
**Main Risk:** The oscillation amplitude may be small relative to noise except for thin-structure strata.

### IDEA-B-0306 — Less rank, more accuracy: the low-rank advantage on tiny datasets
**One-sentence idea:** Test the counterintuitive observation that very low LoRA ranks (1–2) sometimes outperform standard ranks (8–16) on tiny fine-tuning datasets, characterizing the capacity-data-size interaction and its implication that rank should scale with data.
**Problem:** Rank defaults are data-size-agnostic, tiny-dataset fine-tuning is the modal medical scenario, and if minimal-rank updates act as strong implicit regularizers precisely where overfitting risk peaks, current defaults are systematically wrong for the most common regime—but the interaction has never been mapped.
**Core Hypothesis:** The optimal-rank-versus-data-size relationship is monotone with a measurable slope (approximately logarithmic), rank-1 dominance below ~20 samples reflects genuine generalization advantage rather than optimization artifact (verifiable by extensive tuning of higher ranks), and a simple rank-selection rule (rank as a function of sample count and shift magnitude) removes the need for per-project search in the low-data regime.
**Why Important:** A data-indexed rank rule would immediately improve the majority of real-world fine-tuning projects, which operate at small n.
**Why Possibly Novel:** The rank × data-size interaction with a validated selection rule has not been established for dense tasks.
**Minimal Experiment:** Grid rank × sample-count across 6 tasks with exhaustive per-cell tuning; map the optimum surface; fit and prospectively validate the selection rule.
**Main Risk:** The interaction may be confounded by learning-rate coupling with rank, requiring joint tuning.
### IDEA-B-0307 — Hidden language priors: do class names leak into visually prompted segmentation?
**One-sentence idea:** Test whether models trained with mixed text-visual supervision exhibit class-name-dependent behavior even when used with purely visual prompts—hidden linguistic priors shaping ostensibly language-free predictions.
**Problem:** Mixed-supervision models are deployed in visual-only prompting modes under the assumption that unused text pathways are inert, but if language-derived category priors persist in shared representations, "visual-only" outputs carry invisible linguistic biases (e.g., segmenting to lexical category boundaries rather than visual evidence).
**Core Hypothesis:** Visually prompted outputs of mixed-trained models align measurably better with lexical category boundaries than outputs of visually-trained-only controls on ambiguous part-whole cases (the language prior persists), the effect strengthens with text-supervision fraction, and it is detectable by comparing segmentation granularity distributions against language-free baselines on identical prompts.
**Why Important:** Deployments assuming visual-prompt neutrality (measurement applications, cross-lingual settings) need to know their outputs embed English lexical structure.
**Why Possibly Novel:** Cross-modal prior leakage into non-text inference paths has not been measured for dense prediction.
**Minimal Experiment:** Compare granularity/boundary statistics of mixed-trained vs visual-only models under identical visual prompts on part-whole ambiguous suites; correlate effects with text-supervision fraction.
**Main Risk:** Matched visual-only control models at comparable scale may be hard to source.

### IDEA-B-0308 — Pure-noise negatives: an unreasonably effective false-positive suppressor?
**One-sentence idea:** Test the phenomenon that adding a small fraction of pure-noise or structureless images with empty masks to training reduces false positives more effectively than curated hard negatives—probing what "nothing to segment" teaches a dense model.
**Problem:** Negative-set curation is expensive, the folk observation that trivial noise negatives help disproportionately lacks verification and mechanism, and if true it implies models otherwise never learn a well-defined "absence" output mode—revealing something basic about dense-prediction training.
**Core Hypothesis:** Standard training leaves the all-background output mode undertrained (models always see something to segment), noise negatives specifically calibrate the global-absence mode (measurable as recalibrated output-mass priors rather than better discrimination), and the effect complements rather than substitutes hard negatives—each fixing a different FP mechanism (prior miscalibration versus confusable-feature discrimination).
**Why Important:** A near-free training addition with a mechanistic account would improve every rare-target system and clarify how dense models represent absence.
**Why Possibly Novel:** The absence-mode-calibration mechanism has not been isolated from discrimination effects in negative-data research.
**Minimal Experiment:** Train with {no negatives, noise negatives, hard negatives, both} across rare-target tasks; decompose FP reductions into prior-shift versus discrimination effects; verify the complementarity.
**Main Risk:** The effect may be an artifact of specific loss normalizations rather than a general phenomenon.

### IDEA-B-0309 — The inertia tax: temporal smoothing versus rapidly growing fires
**One-sentence idea:** Quantify the detection latency that temporal-consistency methods (smoothing, tracking, temporal ensembling) add for rapidly evolving targets, testing whether stability mechanisms tuned on slowly varying benchmarks systematically delay exactly the events monitoring exists to catch.
**Problem:** Temporal smoothing is added to suppress flicker and false alarms, validated on stability metrics, but a growing fire is a distribution its own history mispredicts—stability mechanisms may impose a growth-rate-dependent detection lag that no current benchmark measures.
**Core Hypothesis:** Temporal-consistency methods impose latency proportional to their effective memory length times the target's growth rate (a derivable inertia law), the lag is worst for the highest-value events (fast-growing fires), and asymmetry-aware temporal logic (fast-attach, slow-release) achieves flicker suppression with a small fraction of the detection lag—dominating symmetric smoothing on the latency-stability frontier.
**Why Important:** Exposes a safety-relevant hidden cost of a standard practice and provides the corrected design with measurable frontier dominance.
**Why Possibly Novel:** Latency-stability frontier analysis for dynamic-target segmentation has not been formalized.
**Minimal Experiment:** Evaluate smoothing-method ladders on growth-rate-stratified fire sequences; measure detection-latency curves; test asymmetric logic against the frontier.
**Main Risk:** Growth-rate ground truth requires well-annotated event onsets, which are scarce.

### IDEA-B-0310 — Confidence inversion: why soft-label training can produce harder predictions
**One-sentence idea:** Investigate the paradoxical observation that models trained on soft labels (matting-style, multi-rater averages) sometimes output more extreme confidences than hard-label-trained models, characterizing when and why softness in, sharpness out.
**Problem:** Soft labels are used specifically to convey uncertainty to models, the inversion—if real—means the mechanism backfires (models resolve soft supervision into confident interpolation rather than calibrated doubt), and downstream consumers reading confidence as uncertainty are then systematically misled.
**Core Hypothesis:** Soft-label training with standard losses teaches models to predict the label-generating process's mean rather than its uncertainty (the loss is minimized by confident mean prediction), producing sharpened outputs in ambiguous zones unless the loss explicitly separates value and confidence channels—a loss-structure account testable by comparing distribution-matching versus mean-regression objectives on identical soft labels.
**Why Important:** Corrects a widespread misunderstanding about what soft supervision achieves, with direct consequences for every multi-rater and matting-supervised pipeline.
**Why Possibly Novel:** The soft-label-to-confidence mapping and its loss dependence have not been analyzed for dense prediction.
**Minimal Experiment:** Train on identical soft labels under mean-regression versus distribution-matching objectives; compare output confidence distributions against rater-disagreement ground truth; verify the mechanism.
**Main Risk:** Multiple soft-label semantics (ambiguity versus partial coverage) may require separate treatments.

### IDEA-B-0311 — Seeds as annotation auditors: cross-seed disagreement locates label errors
**One-sentence idea:** Test whether the spatial disagreement between identically configured training runs differing only in random seed localizes annotation errors better than uncertainty estimates from any single model—turning training stochasticity into a label-auditing instrument.
**Problem:** Label-error detection relies on single-model confidence or loss ranking, both entangled with genuine difficulty, while multi-seed disagreement plausibly isolates supervision inconsistency (models agree where labels are consistent, diverge where supervision conflicts)—an unexploited signal every lab already generates incidentally.
**Core Hypothesis:** Cross-seed disagreement maps enrich for verified annotation errors substantially above single-model uncertainty at matched review budgets (validated against expert re-annotation), the mechanism is supervision conflict rather than difficulty (disagreement correlates with inter-annotator inconsistency, not image entropy), and two seeds already capture most of the auditing value—making the method nearly free.
**Why Important:** A cheap, principled label-auditing tool would improve dataset quality across the field, with the mechanism clarifying what seed variance means.
**Why Possibly Novel:** Seed-disagreement as a label-error detector (versus a nuisance to average away) has not been developed.
**Minimal Experiment:** Train seed ensembles on datasets with known injected and natural label errors; compare error-retrieval curves against uncertainty baselines; verify the supervision-conflict mechanism.
**Main Risk:** Disagreement may concentrate on genuinely ambiguous regions where "error" is undefined.

### IDEA-B-0312 — Sleeper domains: when zero-shot performance mispredicts fine-tuning outcomes
**One-sentence idea:** Test the reliability of zero-shot performance as a predictor of post-fine-tuning performance across many domains, and characterize the "sleeper" exceptions—domains that look hopeless zero-shot but adapt exceptionally well, or look promising but plateau.
**Problem:** Teams triage domains by zero-shot performance (abandoning low scorers, investing in high scorers), the triage assumes rank stability under adaptation, and systematic exceptions—if identifiable in advance—would redirect investment toward recoverable domains currently being abandoned.
**Core Hypothesis:** Zero-shot and fine-tuned rankings correlate strongly overall but with a structured exception class: domains whose failure is interface-level (input statistics, conventions) rather than representation-level adapt far beyond their zero-shot rank (sleepers), the two failure levels are separable in advance by frozen-feature probing (features good, outputs bad → sleeper), and the probe-based triage dominates zero-shot triage on investment-return metrics.
**Why Important:** Corrects a resource-allocation heuristic used implicitly across the field, rescuing viable domains from premature abandonment.
**Why Possibly Novel:** The zero-shot-versus-adaptability dissociation and its predictive probe have not been characterized.
**Minimal Experiment:** Fine-tune uniformly across 20+ domains spanning zero-shot levels; identify sleepers/plateauers; validate the probe-based predictor prospectively.
**Main Risk:** Uniform fine-tuning recipes may disadvantage some domains, confounding adaptability measurement.

### IDEA-B-0313 — Random features, real boundaries: where pretrained encoders don't matter
**One-sentence idea:** Test the observation that frozen randomly initialized encoders with trained decoders approach pretrained-encoder performance on certain high-resolution texture-driven medical tasks, mapping where pretraining's value concentrates and where it is replaceable by decoder capacity.
**Problem:** Pretrained features are assumed universally necessary, licensing and compute decisions follow, but for tasks where discrimination is local-texture-statistical (some histology, some ultrasound), random projections plus sufficient decoding may suffice—and nobody has mapped the boundary of pretraining's actual value.
**Core Hypothesis:** The pretrained-versus-random gap varies enormously and predictably across tasks: near-zero for locally decidable texture tasks (decision information within small receptive fields, measurable by patch-shuffling invariance of expert performance) and large for context-dependent shape tasks—yielding a task-level predictor of pretraining value that also predicts which tasks foundation-model scaling will not help.
**Why Important:** Identifies where the field's foundation-model investments genuinely pay and where simple models suffice—strategic knowledge for both research and procurement.
**Why Possibly Novel:** Systematic pretraining-value cartography with a locality-based predictor has not been executed for dense medical tasks.
**Minimal Experiment:** Train random-vs-pretrained frozen encoders with matched decoders across tasks spanning the locality spectrum; correlate gaps with locality measures; validate the predictor.
**Main Risk:** Decoder capacity choices could mask or exaggerate encoder differences without careful matching.

### IDEA-B-0314 — Prompts don't transfer: the scale-specificity of prompt engineering
**One-sentence idea:** Measure whether optimized prompts (text templates, visual prompt configurations, click strategies) transfer across model scales and versions within the same family, testing the suspicion that prompt engineering overfits to individual checkpoints.
**Problem:** Organizations invest heavily in prompt optimization then upgrade models assuming prompt assets carry over, pipelines chain prompts tuned on one model into another (VLM-proposed prompts consumed by SAM), and if prompts are checkpoint-specific, both practices silently lose their optimization value at every upgrade.
**Core Hypothesis:** Prompt-optimization gains transfer only partially across scales (a measurable transfer fraction well below one), the non-transferring component grows with optimization intensity (harder-optimized prompts are more checkpoint-specific—an overfitting signature), and transfer-aware optimization (optimizing across a checkpoint ensemble) sacrifices small immediate gains for large retained value across upgrades.
**Why Important:** Prompt assets are becoming organizational investments; their depreciation schedule under model upgrades has never been measured.
**Why Possibly Novel:** Prompt-transferability across scale/version within model families is an unexamined dimension of prompt engineering.
**Minimal Experiment:** Optimize prompts per checkpoint across a model-family ladder; evaluate the full transfer matrix; test ensemble-optimized prompts for retained value.
**Main Risk:** Results may differ qualitatively between text and visual prompt types, fragmenting conclusions.

### IDEA-B-0315 — Five percent of elsewhere: out-of-domain data as a superior regularizer
**One-sentence idea:** Test the phenomenon that mixing a small fraction (~5%) of unrelated out-of-domain data into fine-tuning outperforms optimally tuned conventional regularization (weight decay, dropout, early stopping) at preventing overfitting on small target datasets.
**Problem:** Small-data fine-tuning fights overfitting with parameter-space regularizers whose strength is hard to tune, while data-space anchoring (keeping a trickle of diverse data in the mix) may regularize in exactly the directions that matter—preserving general features—yet it is unstudied as a first-class regularization alternative.
**Core Hypothesis:** Anchor-data mixing dominates tuned parameter-space regularization on small-target fine-tuning (measured on target and transfer metrics jointly), the mechanism is gradient-subspace anchoring (target gradients are projected against directions that damage general features—verifiable by update-subspace analysis), and the optimal anchor fraction follows a predictable schedule in target-data size—making the method turnkey.
**Why Important:** A simple, tunable-by-rule regularizer that also preserves generality would improve the modal fine-tuning scenario across applications.
**Why Possibly Novel:** Anchor-data regularization has not been characterized against tuned conventional regularization with mechanism analysis for dense tasks.
**Minimal Experiment:** Compare anchor mixing against exhaustively tuned conventional regularizers across target sizes and domains; verify the subspace mechanism; fit the anchor-fraction schedule.
**Main Risk:** Anchor-data choice (which out-of-domain source) may matter enough to complicate the turnkey claim.

---

## Cluster 10 — Genuinely Motivated Combinations (IDEA-B-0316 … IDEA-B-0330)

### IDEA-B-0316 — Conformal stopping: coverage-guaranteed click budgets for interactive segmentation
**One-sentence idea:** Combine conformal prediction with interactive segmentation to derive a statistically guaranteed stopping rule—stop requesting clicks when the conformal boundary band is narrow enough for the downstream use—replacing heuristic click budgets with coverage-controlled interaction.
**Genuine motivation for the combination:** Interactive segmentation has a sequential-decision problem (when is the mask good enough to stop paying for clicks?) that currently uses heuristics, while conformal prediction supplies exactly the distribution-free sufficiency certificates the stopping decision needs—the combination answers a question neither field answers alone.
**Problem:** Annotation and clinical workflows either over-click (wasting expert time) or under-click (accepting silent errors), with no principled instrument for the stop decision.
**Core Hypothesis:** Conformal band width computed after each click is a valid stopping statistic (maintaining target coverage over the stopped population despite the adaptive stopping—verifiable empirically against martingale-corrected baselines), and coverage-controlled stopping reduces mean clicks substantially at guaranteed quality relative to fixed budgets.
**Why Important:** Turns interactive annotation into a process with statistical quality contracts—what clinical and industrial QA actually require.
**Why Possibly Novel:** Adaptive-stopping conformal guarantees for interactive dense prediction have not been developed.
**Minimal Experiment:** Calibrate conformal scores per click count; implement stopped-population coverage evaluation; compare click costs against fixed and heuristic budgets at matched realized quality.
**Main Risk:** Adaptive stopping violates vanilla exchangeability; the correction may widen bands enough to erode the click savings.

### IDEA-B-0317 — Prompt-consistency objectives for weight-space test-time adaptation
**One-sentence idea:** Use agreement across prompt perturbations—a supervision-free correctness signal unique to promptable models—as the objective for cautious test-time weight adaptation, replacing entropy minimization whose collapse modes stem from having no external anchor.
**Genuine motivation for the combination:** TTA fails because its self-supervision (entropy) is gameable by degenerate solutions, while promptable models carry a built-in multi-view consistency check (different prompts should yield compatible masks) that is much harder to satisfy degenerately—the prompt structure supplies exactly the anchor TTA lacks.
**Problem:** Existing TTA on dense models is unstable on long shifted streams, limiting adoption where it is most needed (continuously drifting deployments).
**Core Hypothesis:** Prompt-consistency-optimized TTA matches entropy-based TTA's peak gains while exhibiting an order-of-magnitude lower collapse rate on long streams (consistency cannot be satisfied by uniform or degenerate outputs), and the objective's gradient directions correlate with supervised-adaptation gradients far better than entropy's—a mechanistic verification.
**Why Important:** A collapse-resistant TTA objective would unlock continuous adaptation for deployed promptable segmenters.
**Why Possibly Novel:** Prompt-structure-derived objectives for weight-space TTA are unexplored.
**Minimal Experiment:** Run long-stream TTA comparisons (consistency versus entropy versus frozen) across drift scenarios; measure gains and collapse statistics; compare gradient alignments.
**Main Risk:** Consistency computation multiplies inference cost per adaptation step.

### IDEA-B-0318 — Differentiable scattering: a physics head for volumetric smoke from single images
**One-sentence idea:** Attach a differentiable single-scattering radiative-transfer head to a segmentation backbone so smoke predictions are expressed as volumetric density fields rendered into 2D—making the physical quantity the output and the 2D mask merely its projection.
**Genuine motivation for the combination:** Smoke labels are 2D but the object is a 3D participating medium; a physics renderer in the loop lets 2D supervision constrain a 3D physically meaningful representation—the combination resolves the dimensional mismatch that pure 2D segmentation cannot.
**Problem:** 2D smoke masks conflate optically thin and thick smoke, cannot support downstream physics (dispersion, visibility), and force models to make arbitrary threshold decisions at soft boundaries.
**Core Hypothesis:** Training a density-field head through a differentiable scattering renderer against ordinary 2D masks yields (a) binary segmentation at least matching direct mask prediction, (b) density estimates that correlate with independent physical measurements (transmissometers, paired-view consistency) despite never being directly supervised—demonstrating that physics structure extracts 3D information from 2D labels.
**Why Important:** Elevates smoke perception to physically grounded quantification using only existing annotation types.
**Why Possibly Novel:** Physics-rendered volumetric heads supervised by ordinary segmentation masks have not been demonstrated for atmospheric media.
**Minimal Experiment:** Implement the differentiable single-scattering head; train on standard smoke datasets; validate density outputs against paired-view consistency and any available physical measurements.
**Main Risk:** Single-scattering approximations may be too crude for dense smoke, and the inverse problem may be under-constrained from single views.

### IDEA-B-0319 — Refraction has a motion signature: flow anomalies as a transparency cue in video
**One-sentence idea:** Exploit the unique optical-flow anomalies that refraction and specular reflection produce (background flow warped through glass moves differently than the glass surface itself) as a physics-grounded cue for transparent-object segmentation in video.
**Genuine motivation for the combination:** Transparency defeats appearance-based segmentation because glass has almost no appearance of its own, but it has a distinctive motion signature—flow fields transmitted through refractive media are geometrically inconsistent with the scene's rigid motion in a characteristic, detectable way; motion analysis supplies the cue appearance lacks.
**Problem:** Transparent-object segmentation from single RGB images remains unreliable, while video—abundant in robotics—contains unexploited motion evidence of transparency.
**Core Hypothesis:** Flow-consistency residuals (observed flow versus flow predicted by dominant scene motion) systematically localize refractive and reflective surfaces (measurable enrichment), a segmenter consuming flow-residual channels substantially outperforms appearance-only models on moving-camera transparency benchmarks, and the cue degrades gracefully to zero (not negatively) in static scenes—making it a safe additive channel.
**Why Important:** Provides robotics and AR a physically principled transparency channel from sensors they already have.
**Why Possibly Novel:** Refractive flow-anomaly analysis as a trainable segmentation cue is essentially unexplored.
**Minimal Experiment:** Compute flow residuals on moving-camera transparency datasets; measure localization enrichment; train residual-augmented versus appearance-only segmenters; compare across motion regimes.
**Main Risk:** Textureless backgrounds defeat flow estimation exactly where transparency cues are most needed.

### IDEA-B-0320 — Positive-unlabeled statistics for everything-mode auto-labeling
**One-sentence idea:** Treat SAM everything-mode outputs as what they statistically are—high-precision positives over an unknown-recall support—and develop positive-unlabeled estimation for training detectors/segmenters from them, replacing the false closed-world assumption of current auto-labeling.
**Genuine motivation for the combination:** Everything-mode output is structurally PU data (found masks are mostly real; unfound regions are unknown, not negative), and PU learning theory exists precisely to handle this—yet auto-labeling pipelines apply standard supervised losses that treat unfound objects as background, a statistical error PU theory corrects by construction.
**Problem:** Models trained on everything-mode pseudo-labels systematically suppress object classes and strata the proposal engine under-recalls, inheriting and hardening its blind spots.
**Core Hypothesis:** PU-corrected training (with per-stratum class priors estimated from small audits) recovers a substantial fraction of the recall lost to naive training (largest on low-contrast and small-object strata where everything-mode recall is worst), and the required audit budget for prior estimation is tiny relative to the gains—making the correction nearly free.
**Why Important:** Repairs a foundational statistical flaw in the field's dominant auto-labeling pattern.
**Why Possibly Novel:** PU formalization of foundation-model auto-labeling with stratified prior estimation has not been developed.
**Minimal Experiment:** Auto-label with everything mode on datasets with held-out truth; train naive versus PU-corrected students; measure stratified recall recovery versus audit budget.
**Main Risk:** PU corrections are sensitive to prior misestimation; stratified priors multiply the estimation burden.

### IDEA-B-0321 — Shape-statistics-constrained adapters: anatomical plausibility as a PEFT constraint
**One-sentence idea:** Constrain adapter-based fine-tuning so that outputs remain within a statistical shape model of the target anatomy—regularizing the adaptation, not the prediction, to preserve anatomical plausibility under tiny training sets.
**Genuine motivation for the combination:** Few-shot PEFT loses exactly the shape priors that classical statistical shape models (SSMs) encode compactly from modest data; putting the SSM into the adaptation constraint (penalizing adapter updates whose outputs leave the plausible shape manifold) supplies the missing prior at the right place—the combination addresses PEFT's specific low-data failure with the tool built for low-data shape modeling.
**Problem:** Adapters fine-tuned on few medical cases produce anatomically impossible outputs on hard inputs (fragmented organs, impossible topologies), which erodes clinical trust disproportionately to their frequency.
**Core Hypothesis:** SSM-constrained adaptation eliminates the large majority of anatomically implausible outputs at equal or better mean accuracy (the constraint binds only where evidence is weak), with the benefit concentrated at the smallest training sizes and vanishing gracefully as data grows—exactly the profile of a well-placed prior.
**Why Important:** Anatomical plausibility guarantees are a distinct clinical requirement that accuracy metrics don't capture; a PEFT-native mechanism delivers them cheaply.
**Why Possibly Novel:** Shape-manifold constraints applied to the adaptation process (rather than as output post-processing or loss terms on predictions) are undeveloped.
**Minimal Experiment:** Build SSMs from modest datasets; implement constrained adaptation; compare implausibility rates and accuracy against unconstrained PEFT and post-hoc SSM projection across training sizes.
**Main Risk:** SSM expressiveness limits could suppress genuine pathological shape variation—the cases that matter most.

### IDEA-B-0322 — Retrieval-of-prompts: transferring interaction knowledge instead of masks
**One-sentence idea:** For each new image, retrieve the most similar previously annotated cases and transfer their successful prompt configurations (click patterns, box placements)—not their masks—to initialize prompting, treating interaction strategies as the retrievable, transferable asset.
**Genuine motivation for the combination:** Retrieval-augmented methods transfer labels, which fail under deformation and appearance change, but prompt configurations are low-dimensional, deformation-tolerant summaries of how to interact with a class of images—retrieval supplies per-case adaptivity while prompts supply the robust transferable representation; each component covers the other's weakness.
**Problem:** Every image is currently prompted from scratch, discarding accumulated interaction knowledge from thousands of prior annotations of similar cases.
**Core Hypothesis:** Retrieved-prompt initialization reduces clicks-to-target-quality substantially versus centroid defaults (with gains growing with corpus size in a measurable retrieval-scaling curve), and prompt transfer outperforms mask transfer (via registration) precisely on deformable and appearance-shifted anatomy where masks misalign but interaction logic persists.
**Why Important:** Makes annotation systems learn from their own usage—compounding value with every annotation session at near-zero infrastructure cost.
**Why Possibly Novel:** Interaction-configuration retrieval (versus label retrieval) is an unexplored transfer channel.
**Minimal Experiment:** Log prompt sessions to build corpora; implement retrieval-initialized prompting; measure click savings versus corpus size; compare against mask-transfer baselines on deformable anatomy.
**Main Risk:** Prompt success may be too conditioned on fine image details for similarity-based retrieval to capture.

### IDEA-B-0323 — Counterfactual shortcut audits: measuring causal reliance with generative interventions
**One-sentence idea:** Combine generative image editing with causal-inference methodology to measure segmentation models' causal reliance on suspected shortcut features (rulers, tags, ink marks)—editing the suspected cause out of real images and measuring the effect—replacing correlational saliency evidence with interventional evidence.
**Genuine motivation for the combination:** Shortcut claims require causal evidence that saliency and correlation analyses cannot provide, while modern generative editors finally make faithful interventions on real images feasible—the causal framework tells us what to measure and the generator makes the measurement possible; neither suffices alone.
**Problem:** Shortcut accusations and defenses in medical AI rest on suggestive but non-causal evidence, leaving deployment decisions to argument rather than measurement.
**Core Hypothesis:** Interventional reliance scores (performance change under counterfactual artifact removal/insertion, with edit-fidelity controls) reveal a substantially different reliance ranking than saliency-based audits (some salient features are causally inert, some non-salient ones are load-bearing), and interventional scores predict cross-site transfer failures markedly better—validating the causal audit as the deployment-relevant instrument.
**Why Important:** Establishes the evidentiary standard for shortcut claims in high-stakes imaging, with a practical tool implementing it.
**Why Possibly Novel:** Generative-interventional shortcut auditing with transfer-predictivity validation has not been systematized for dense prediction.
**Minimal Experiment:** Build edit-based intervention suites for known suspected shortcuts; compute reliance scores across models; compare saliency versus interventional rankings; validate against measured cross-site failures.
**Main Risk:** Edit artifacts could themselves perturb models, requiring rigorous edit-fidelity controls.

### IDEA-B-0324 — Boundary Shapley values: principled multi-rater consensus from cooperative game theory
**One-sentence idea:** Apply cooperative-game credit assignment (Shapley-style analysis over rater coalitions) to multi-rater segmentation fusion—assigning each rater region-wise credibility from coalition consistency—to construct consensus ground truth with per-region reliability weights.
**Genuine motivation for the combination:** Multi-rater fusion needs a principled answer to "whose boundary do we trust where," which is exactly the credit-assignment problem cooperative game theory solved axiomatically; majority voting ignores rater-region expertise structure that coalition analysis recovers—the theory supplies the fairness axioms the fusion problem needs.
**Problem:** Consensus construction (majority vote, STAPLE) treats rater reliability as global or globally estimated, while real raters have spatially structured expertise (one is careful on vessels, another on parenchyma), producing consensus that is locally worse than the best rater.
**Core Hypothesis:** Region-wise coalition-consistency credit recovers spatial expertise structure (validated against known-expertise designs where rater skill is experimentally manipulated), and the resulting weighted consensus is measurably closer to held-out super-expert annotation than majority vote and STAPLE—especially on boundary regions where expertise varies most.
**Why Important:** Ground-truth quality bounds everything downstream; a better fusion rule improves datasets at their source.
**Why Possibly Novel:** Game-theoretic spatial credit assignment for annotation fusion is undeveloped.
**Minimal Experiment:** Run fusion methods on multi-rater datasets with super-expert reference; include a controlled-expertise annotation study; compare consensus quality region-wise.
**Main Risk:** Shapley computation over rater coalitions scales combinatorially, requiring approximations whose fidelity needs its own validation.

### IDEA-B-0325 — Information-optimal clicking: querying the mask posterior where it is most uncertain
**One-sentence idea:** Select each next click to maximize expected information gain over the model's mask posterior (approximated by its multimask candidates and their scores)—putting interactive segmentation on decision-theoretic foundations that the multimask architecture makes computable for the first time.
**Genuine motivation for the combination:** Optimal-experiment-design theory requires a posterior to compute information gain over, which segmentation never had—but multimask promptable models expose an explicit (if coarse) posterior over hypotheses, making the classical theory finally applicable; the architecture unlocks the math.
**Problem:** Click-placement guidance (center of largest error region, heuristic sampling) is untheorized, and users click suboptimally on ambiguous cases, wasting the most expensive resource (expert attention).
**Core Hypothesis:** Information-gain-optimal click suggestions reduce clicks-to-quality measurably versus error-centroid heuristics (largest gains on high-ambiguity cases where candidates disagree most), the coarse candidate posterior suffices for near-optimal selection (verifiable against dense-posterior oracles), and suggested clicks are interpretable to users as "asking about the genuine ambiguity"—supporting adoption.
**Why Important:** Optimal interaction directly multiplies expert throughput in annotation and clinical correction—the binding resource across medical AI.
**Why Possibly Novel:** Posterior-based optimal click selection using multimask outputs has not been formalized or tested.
**Minimal Experiment:** Implement candidate-posterior information gain; compare against heuristic click policies in simulation and a small user study; test posterior sufficiency against oracle refinements.
**Main Risk:** The 3-candidate posterior may be too coarse to represent the ambiguities that matter.

### IDEA-B-0326 — Topology-first evaluation: making connectivity the primary endpoint for vascular segmentation
**One-sentence idea:** Combine persistent-homology-based topological metrics with rigorous statistical testing to build an evaluation framework where vascular connectivity (not pixel overlap) is the primary endpoint—then re-examine which training and architecture choices actually help the clinically consumed quantity.
**Genuine motivation for the combination:** Clinical use of vessel segmentation consumes connectivity (can a catheter pass, is the tree complete), persistent homology is the mathematics of connectivity structure, and statistical testing frameworks make endpoint changes rigorous—the combination re-aligns an entire evaluation regime with its clinical purpose rather than adding a module.
**Problem:** Vessel-segmentation research optimizes and reports pixel metrics that are near-blind to breaks and spurious bridges—the errors that actually matter—so published progress may not track clinical value.
**Core Hypothesis:** Method rankings under topology-primary evaluation differ materially from pixel-metric rankings across public vessel-segmentation methods (some celebrated methods lose, some dismissed ones win), and topology-primary model selection during training produces models that clinicians rate as more usable in blinded reading studies—validating the endpoint switch.
**Why Important:** Re-anchors a substantial research area to its purpose, with a reusable statistical framework for endpoint-driven evaluation.
**Why Possibly Novel:** Topology metrics exist, but a complete primary-endpoint evaluation framework with ranking re-analysis and clinical validation does not.
**Minimal Experiment:** Re-evaluate public vessel methods under the topology-primary framework; quantify ranking shifts; run a small blinded clinician usability study on topology- versus pixel-selected models.
**Main Risk:** Topology metrics are sensitive to small-scale noise, requiring careful scale-filtration choices that could be contested.

### IDEA-B-0327 — Bandit-routed annotation: sequential budget allocation between model and expert
**One-sentence idea:** Frame per-image annotation routing (accept model output, request cheap human check, or commission expert annotation) as a contextual bandit with measured costs and learned per-image success predictions, optimizing total dataset quality per budget with regret guarantees.
**Genuine motivation for the combination:** Annotation pipelines make exactly the sequential decision-under-uncertainty that bandit theory formalizes (explore model reliability across image types while exploiting known-safe routing), and image-conditioned failure predictors supply the context—the theory contributes regret-bounded policies where current practice uses static rules; the combination is the problem's native formalism.
**Problem:** Hybrid human-AI annotation pipelines route by fixed confidence thresholds tuned once, wasting budget on unnecessary reviews while missing systematic model failures on unmodeled strata.
**Core Hypothesis:** Bandit routing achieves measurably better quality-per-budget than tuned static thresholds (with the advantage growing over the campaign as the policy learns strata-specific reliability), and empirical regret matches theoretical bounds closely enough to certify budget planning—making annotation campaigns plannable financial objects.
**Why Important:** Dataset construction is the dominant cost in applied dense prediction; regret-bounded routing converts it from art to engineering.
**Why Possibly Novel:** Bandit formalization of annotation routing with cost-normalized dense-quality rewards has not been deployed and analyzed.
**Minimal Experiment:** Simulate routing on fully annotated datasets with measured cost models; compare bandit versus static policies over campaign trajectories; validate on a small live annotation campaign.
**Main Risk:** Non-stationarity (annotator learning, data drift within campaigns) may violate bandit assumptions enough to erode guarantees.

### IDEA-B-0328 — The identifiability of masks from k clicks: a sample-complexity theory of interaction
**One-sentence idea:** Develop compressed-sensing-style theory for interactive segmentation—characterizing which masks are uniquely determined by k prompt points given an image prior—and validate its predictions of per-image minimum interaction requirements against model and human behavior.
**Genuine motivation for the combination:** Interactive segmentation lacks any theory of how much interaction a target fundamentally requires, while compressed sensing solved the analogous problem (when do k measurements determine a structured signal); prompts are measurements, the image prior plays the sparsity role, and identifiability analysis transfers—the combination imports the right mathematical frame for a question the field cannot currently pose.
**Problem:** Without lower bounds, we cannot distinguish models that interact inefficiently from targets that inherently need many clicks—confounding model evaluation with task hardness.
**Core Hypothesis:** A computable identifiability index (derived from the image's segmentation-hypothesis space under a learned prior) predicts both the click counts strong models empirically need and the cases where humans require extra interaction, and model-versus-bound gaps expose specific inefficiencies (models needing clicks where the mask was already determined)—separating task hardness from model waste for the first time.
**Why Important:** Gives interactive segmentation the hardness-versus-inefficiency decomposition that any maturing field needs for honest evaluation.
**Why Possibly Novel:** Identifiability/sample-complexity theory for prompted dense prediction does not exist.
**Minimal Experiment:** Construct the index via hypothesis-space analysis on datasets with interaction logs; correlate with empirical click requirements; audit model-bound gaps.
**Main Risk:** The theory may only be tractable under priors too simplified to predict real behavior.

### IDEA-B-0329 — Weak-to-strong generalization in dense prediction: does the student surpass the labeler?
**One-sentence idea:** Test whether a strong foundation segmenter fine-tuned on labels produced by a much weaker model can exceed its weak teacher's quality (weak-to-strong generalization), establishing whether the phenomenon documented for language models operates in dense prediction—and through what mechanism.
**Genuine motivation for the combination:** Weak-to-strong generalization is a foundational alignment-era question (can strong models extract latent knowledge from imperfect supervision?) whose dense-prediction instantiation is untested yet practically urgent—weak-model auto-labeling is exactly how segmentation datasets are now built, so the question and the field's dominant practice have converged.
**Problem:** If strong students merely imitate weak teachers, auto-labeling pipelines cap at teacher quality; if they surpass them, the field's data economics change—but nobody has measured which occurs for segmentation or when.
**Core Hypothesis:** Strong students exceed weak teachers on strata where teacher errors are inconsistent (the student's prior resolves noise toward truth) but inherit and harden systematic teacher biases (consistent boundary offsets), yielding a measurable decomposition—surpassing on variance-type errors, imitating bias-type errors—that predicts when auto-labeling lifts versus caps quality, and prescribes bias-breaking label perturbations that unlock surpassing.
**Why Important:** Determines the ceiling of the field's dominant dataset-construction strategy and how to raise it.
**Why Possibly Novel:** Weak-to-strong analysis with a bias/variance error decomposition has not been performed for dense tasks.
**Minimal Experiment:** Fine-tune strong models on weak-model labels across teacher-quality ladders with held-out truth; decompose student-versus-teacher deltas by error type; test bias-breaking interventions.
**Main Risk:** Results may depend strongly on the student's pretraining overlap with the evaluation domains.

### IDEA-B-0330 — Refinement as curve evolution: stability conditions for iterative mask decoders
**One-sentence idea:** Formalize iterative mask-refinement decoders as discretized curve-evolution processes (level-set dynamics), importing stability and step-size theory that predicts when refinement iterations converge, oscillate, or destroy masks—then validate the predictions on real decoder failures.
**Genuine motivation for the combination:** Iterative refinement modules are designed heuristically and fail unpredictably (oscillating boundaries, runaway erosion), while level-set theory long ago characterized stability conditions for exactly this class of boundary-evolution dynamics; mapping decoder updates onto evolution equations makes forty years of numerical-stability theory applicable to a current architecture problem.
**Problem:** Refinement depth and step behavior are tuned by trial and error, and failure modes (masks degrading with more refinement steps) lack any predictive account.
**Core Hypothesis:** Learned refinement updates approximate curvature-dependent evolution flows (verifiable by regressing update fields on geometric quantities), observed instabilities coincide with violations of the corresponding CFL-style stability conditions computed from the learned dynamics, and constraining decoder updates to provably stable regimes eliminates refinement-degradation failures with negligible accuracy cost.
**Why Important:** Replaces trial-and-error refinement design with predictive theory—and provides stability certificates relevant to regulated deployments.
**Why Possibly Novel:** The decoder-as-discretized-evolution correspondence with validated stability predictions has not been established.
**Minimal Experiment:** Extract update fields from trained iterative decoders; fit evolution-equation approximations; test stability-condition predictions against observed failure cases; evaluate stability-constrained variants.
**Main Risk:** Learned updates may be too far from any local evolution law for the theory to bind.

---

## Cluster 11 — SR / Restoration / Generation / Diffusion / LLM Agents (only where they create genuine dense-prediction or foundation-model questions) (IDEA-B-0331 … IDEA-B-0340)

### IDEA-B-0331 — The hallucination-utility frontier of super-resolution for downstream dense prediction
**One-sentence idea:** Using SR models with controllable generative strength (guidance/hallucination knobs), map the frontier between detail hallucination and downstream segmentation utility on gigapixel pathology and low-res monitoring—establishing when generative SR is a legitimate preprocessing stage versus a boundary-fabrication hazard.
**Dense-prediction question created:** Does generative detail help or corrupt pixel-accurate downstream inference—and is the effect measurable and controllable?
**Problem:** Generative SR is entering medical and monitoring pipelines on visual-quality evidence, while its effect on downstream boundary fidelity—the property those pipelines actually need—is uncharacterized as a function of generative strength.
**Core Hypothesis:** Downstream segmentation quality is non-monotonic in SR generative strength (mild strength recovers resolvable structure; high strength fabricates confident boundaries that segmenters trace), the optimum differs systematically between texture-driven and boundary-driven tasks, and hallucinated-boundary harm is detectable without ground truth via SR-seed ensembling (fabricated details vary across seeds, real details don't)—yielding a deployable safety check.
**Why Important:** Provides the evidence and the audit tool needed before generative preprocessing becomes silently embedded in measurement-critical pipelines.
**Why Possibly Novel:** Guidance-parameterized downstream-utility frontiers and seed-based hallucination detection for dense pipelines are unexamined.
**Minimal Experiment:** Sweep SR generative strength; measure downstream segmentation across task types; validate the seed-ensemble hallucination detector against known fabrications.
**Main Risk:** Generative-strength knobs differ across SR architectures, complicating a unified frontier.

### IDEA-B-0332 — Generative versus discriminative features for amorphous stuff: diffusion representations on smoke
**One-sentence idea:** Test whether intermediate features of image diffusion models—trained to model full appearance distributions including textures and media—support segmentation of amorphous "stuff" (smoke, haze, wet surfaces) better than discriminatively or mask-supervised features that were optimized for object boundaries.
**Foundation-model question created:** Do generative and discriminative pretraining yield systematically different representational coverage—objects versus media—and is stuff segmentation the regime where generative features win?
**Problem:** Feature-source choice for dense tasks is settled by object-centric benchmarks, potentially mis-ranking feature families for the media-like targets where discriminative pretraining had no supervision pressure.
**Core Hypothesis:** Frozen diffusion features outperform SAM/DINO features for smoke and haze segmentation at matched probe capacity (generative training was forced to model participating media that mask supervision ignores), while losing on crisp-object boundaries—a double dissociation demonstrating complementary representational coverage and motivating target-type-conditioned feature selection.
**Why Important:** Establishes a principled account of what each pretraining paradigm actually learned, beyond aggregate benchmark ordering.
**Why Possibly Novel:** Stuff-versus-object stratified feature comparisons across generative/discriminative families are missing.
**Minimal Experiment:** Probe frozen features from diffusion, mask-supervised, and self-distilled models on stuff-versus-object segmentation batteries at matched probe capacity; test the dissociation.
**Main Risk:** Diffusion feature extraction choices (timestep, layer) add degrees of freedom that must be honestly searched for all families.

### IDEA-B-0333 — Does restoration reintroduce a domain gap? The restored-image distribution problem
**One-sentence idea:** Test whether restoration preprocessing (dehazing, denoising, deblurring) helps downstream segmentation less than expected—or hurts—because restored images occupy a novel distribution (the restorer's output manifold) that downstream models have never seen, effectively swapping one domain gap for another.
**Dense-prediction question created:** Is "restore then predict" self-defeating because restoration outputs are themselves out-of-distribution for the predictor?
**Problem:** The restore-then-predict pattern assumes restoration moves degraded inputs toward the predictor's training distribution, but restorers have characteristic output statistics (smoothing signatures, artifact palettes) that may land images in a third distribution unlike both degraded and clean data.
**Core Hypothesis:** Restored images are measurably distinguishable from clean images by simple probes (proving the third distribution exists), downstream degradation on restored inputs correlates with that distinguishability across restorer families, and jointly fine-tuning the predictor on restored-image distributions—or matching the restorer's output statistics to clean data—recovers the loss, confirming the mechanism.
**Why Important:** The restore-then-predict pattern is ubiquitous; understanding its hidden distribution mechanics determines when it should be replaced by degradation-robust training.
**Why Possibly Novel:** The restored-image manifold as a distinct domain with measurable downstream cost has not been characterized.
**Minimal Experiment:** Probe restored-versus-clean distinguishability across restorers; correlate with downstream deltas; test restored-distribution fine-tuning and statistics matching.
**Main Risk:** Effects may be small for state-of-the-art restorers on mild degradations, confining relevance to heavy-degradation regimes.

### IDEA-B-0334 — Is cycle-consistency a valid generation metric? Independent-segmenter verification of mask-conditioned synthesis
**One-sentence idea:** Evaluate mask-conditioned image generators by whether an independent segmenter recovers the conditioning mask from the generated image—and test the validity of this popular consistency metric itself, since it can be gamed by generators that render segmenter-legible but unrealistic cues.
**Foundation-model question created:** When are model-based evaluation loops (one model judging another's output) valid measurement instruments, and when do they collude?
**Problem:** Segmentation-recovery scores are becoming the standard automatic metric for conditional generation quality, without evidence that they track human-judged conditioning fidelity rather than generator-segmenter mutual exploits.
**Core Hypothesis:** Segmentation-recovery scores diverge from human-judged fidelity in measurable regimes (generators that overdraw boundary cues score perfectly while looking wrong; subtle-but-faithful generations score poorly), the divergence grows when generator and segmenter share pretraining lineage (collusion through shared features), and ensembling architecturally disjoint verifier segmenters restores metric validity—a general lesson for model-judged evaluation.
**Why Important:** Model-judging-model evaluation is spreading across generative vision; its validity conditions need establishing before it entrenches.
**Why Possibly Novel:** Metric-validity analysis (including the lineage-collusion effect) for consistency-based generation evaluation has not been performed.
**Minimal Experiment:** Correlate recovery scores with human fidelity judgments across generator families and verifier lineages; test collusion via lineage manipulation; validate disjoint-ensemble verification.
**Main Risk:** Human fidelity judgment for mask conditioning is itself noisy, requiring careful protocol design.

### IDEA-B-0335 — Denoising as uncertainty grounding: do noise-trained features know the local noise level?
**One-sentence idea:** Test whether pretraining a backbone on modality-realistic denoising produces features from which local noise level—and therefore aleatoric segmentation uncertainty—is linearly decodable, grounding uncertainty estimation in a physically meaningful pretext task.
**Dense-prediction question created:** Can aleatoric uncertainty be inherited from a pretext task's physics rather than estimated post hoc from labels?
**Problem:** Aleatoric uncertainty estimates are trained from segmentation labels that confound annotator noise with image noise, while denoising pretraining forces explicit representation of exactly the local signal-to-noise structure that determines true aleatoric limits—an untapped grounding.
**Core Hypothesis:** Denoising-pretrained features support linear decoding of local noise level far better than classification- or mask-pretrained features, segmentation heads on such features produce uncertainty maps that track physical noise manipulations (dose reduction, gain changes) quantitatively—unlike label-trained uncertainty which tracks annotation difficulty—and the two uncertainty types are complementary and separable.
**Why Important:** Physically grounded aleatoric uncertainty would let medical systems distinguish "the image cannot support this decision" from "the model is unfamiliar"—a clinically actionable distinction current methods blur.
**Why Possibly Novel:** Pretext-task-inherited uncertainty with physical-manipulation validation has not been developed for dense prediction.
**Minimal Experiment:** Pretrain denoisers on modality data with calibrated noise; probe noise-level decodability across feature sources; validate uncertainty maps under controlled physical noise interventions.
**Main Risk:** Real acquisition noise structure may be too complex for the pretext inheritance to survive fine-tuning.

### IDEA-B-0336 — LLM agents as guideline compilers: automated QA of segmentation annotations against written protocols
**One-sentence idea:** Test whether an LLM agent that reads a dataset's written annotation guidelines and inspects mask-image pairs (via VLM tools) can flag guideline violations at useful precision—treating annotation QA as a guideline-compilation problem that language models are uniquely positioned to solve.
**Dense-prediction question created:** Can natural-language annotation specifications be operationalized into automated dense-label auditing—closing the loop between protocol documents and pixel-level compliance?
**Problem:** Annotation guidelines are enforced by spot-checking; systematic violations (inclusion-rule drift, boundary conventions) survive into published datasets because no scalable mechanism connects the written rules to the pixels.
**Core Hypothesis:** Agent-based auditing achieves precision/recall on seeded guideline violations sufficient for QA triage (verified against expert audits), performance depends measurably on guideline explicitness (creating pressure toward machine-auditable protocols), and agent-flagged real datasets contain substantial confirmed violation rates—demonstrating both the tool and the latent problem it exposes.
**Why Important:** Dataset quality is the field's foundation, and guideline compliance is its only definition of correctness; automating the audit scales a function that currently doesn't scale at all.
**Why Possibly Novel:** Guideline-grounded (rather than statistics-based) automated annotation auditing has not been developed.
**Minimal Experiment:** Seed controlled violations into annotated sets; run agent audits with varied guideline explicitness; measure detection performance; audit real datasets with expert confirmation of flags.
**Main Risk:** VLM visual-inspection limits (fine boundary judgments) may cap achievable precision below QA-useful thresholds.

### IDEA-B-0337 — Are diffusion mask priors valid posteriors? Testing generative uncertainty against ground truth ensembles
**One-sentence idea:** Train mask-space diffusion models as generative priors over plausible segmentations conditioned on images, and rigorously test whether their sample spread constitutes a statistically valid posterior—coverage-calibrated against multi-rater ground truth distributions—rather than merely diverse-looking samples.
**Foundation-model question created:** Do generative models over structured outputs produce calibrated posteriors, or stylistic diversity that mimics uncertainty without its statistical properties?
**Problem:** Mask-diffusion sampling is increasingly presented as segmentation uncertainty, but diversity and calibrated posterior spread are different properties, and no validation against genuine ambiguity distributions (rater populations) has been performed.
**Core Hypothesis:** Mask-diffusion sample distributions fail coverage tests against multi-rater distributions in characteristic ways (over-dispersed on easy regions where training saw rater noise, under-dispersed on genuinely ambiguous structures underrepresented in training), and posterior-calibration fine-tuning against rater-distribution supervision corrects both failures—establishing what it takes to make generative uncertainty statistically real.
**Why Important:** Generative uncertainty is being consumed as if calibrated in medical prototypes; its actual statistical status needs establishing with reference distributions.
**Why Possibly Novel:** Coverage validation of mask-diffusion posteriors against rater populations has not been executed.
**Minimal Experiment:** Train mask-diffusion on multi-rater datasets (holding raters out); run coverage and dispersion tests against held-out rater distributions; test calibration fine-tuning.
**Main Risk:** Multi-rater datasets rich enough for distributional validation are scarce.

### IDEA-B-0338 — Noise as signal: does restoration destroy the forensic cues tiny-target detection relies on?
**One-sentence idea:** Test whether denoising preprocessing harms detection of near-resolution-limit targets (distant smoke plumes, micro-calcifications) because sensor-noise interaction statistics around real structures carry discriminative information that restoration removes along with the noise.
**Dense-prediction question created:** Is image "quality" adversarial to detectability at the resolution limit—and where is the crossover?
**Problem:** Denoising is applied universally on the assumption that noise only obscures, but at the resolution limit, how a faint structure perturbs the local noise field may be a genuine detection cue—one that cleaner-looking restored images no longer contain.
**Core Hypothesis:** Detection performance for sub-5-pixel targets is measurably higher on raw than denoised inputs for detectors trained on each respectively (the noise-interaction cue is real and learnable), the effect reverses above a target-size crossover (noise becomes pure nuisance), and the crossover is predictable from target-contrast-to-noise ratios—yielding a size-conditional preprocessing rule that contradicts uniform-restoration practice.
**Why Important:** Early-detection systems (wildfire, screening mammography) operate exactly at the resolution limit where this reversal—if real—means standard preprocessing is deleting the earliest detectable signal.
**Why Possibly Novel:** The noise-as-cue hypothesis at the tiny-target regime has not been isolated with trained-on-matched-input controls.
**Minimal Experiment:** Train detectors on raw versus denoised inputs across target-size ladders with matched pipelines; locate the crossover; verify the noise-interaction mechanism via noise-resampling controls.
**Main Risk:** The cue may be sensor-specific, limiting generality across camera and scanner types.

### IDEA-B-0339 — Interactive segmentation as Bayesian inversion: posterior-driven interaction from image priors
**One-sentence idea:** Reformulate interactive segmentation as a Bayesian inverse problem—prompts are measurements, a learned generative image-conditioned mask prior defines the posterior—and test whether explicit posterior maintenance outperforms feedforward prompt decoding in interaction efficiency and uncertainty validity.
**Dense-prediction question created:** Does maintaining an explicit posterior over masks (rather than decoding point estimates from prompts) change what interactive systems can do—optimal querying, valid uncertainty, principled stopping?
**Problem:** Feedforward promptable decoders conflate prior, evidence, and decision into one opaque map, making principled interaction (where to click, when to stop, what to trust) impossible to derive rather than heuristically bolt on.
**Core Hypothesis:** An explicit posterior formulation (amortized where needed for speed) matches feedforward decoders on single-prompt accuracy while dominating them on the derived quantities—click efficiency under posterior-optimal querying, uncertainty coverage validity, and stopping-rule quality—demonstrating that the probabilistic structure, not raw accuracy, is where the formulation pays.
**Why Important:** Provides the principled foundation that interactive dense prediction currently lacks, unifying querying, stopping, and uncertainty in one framework.
**Why Possibly Novel:** Full Bayesian-inversion treatment of prompted segmentation with empirical head-to-head against feedforward decoding has not been executed.
**Minimal Experiment:** Build an amortized posterior system on standard backbones; compare against SAM-style decoding on accuracy, click efficiency, coverage validity, and stopping quality across datasets.
**Main Risk:** Posterior maintenance may be too slow for interactive latency budgets without approximations that forfeit its advantages.

### IDEA-B-0340 — Agentic pipelines versus monolithic fine-tunes: error attribution across tool boundaries
**One-sentence idea:** Systematically compare LLM-agent-orchestrated vision pipelines (agent composes detector, promptable segmenter, verifier per task) against monolithically fine-tuned models at matched compute—measuring not just accuracy but error attributability, failure containment, and adaptation cost across task distributions.
**Foundation-model question created:** For dense visual tasks, when does compositional tool orchestration beat end-to-end optimization—and does composition's inspectability constitute measurable engineering value?
**Problem:** The field is splitting into agentic-composition and end-to-end-fine-tuning camps on ideology; the actual tradeoff structure (which task properties favor which paradigm, and what the interpretability of tool boundaries is worth operationally) has not been measured.
**Core Hypothesis:** Monolithic fine-tunes win on narrow stationary tasks at matched compute while agentic pipelines win as task heterogeneity and drift increase (composition amortizes adaptation across tools), tool-boundary logging enables error attribution that measurably accelerates debugging and targeted improvement (quantifiable as time-to-fix in controlled engineering studies), and the crossover is predictable from task-distribution entropy—giving the paradigm choice an evidence basis.
**Why Important:** This architecture decision is being made across the industry now, largely on taste; measured tradeoff structure would ground it.
**Why Possibly Novel:** Controlled paradigm comparisons including operational metrics (attributability, time-to-fix) rather than accuracy alone have not been published for dense vision.
**Minimal Experiment:** Build both paradigms for a task battery spanning heterogeneity levels at matched compute; measure accuracy, drift response, and engineer time-to-fix in controlled debugging exercises.
**Main Risk:** Agent-framework implementation quality could dominate paradigm effects, requiring multiple framework instantiations.

---

*End of Stage 1 Batch B: 340 ideas (IDEA-B-0001 through IDEA-B-0340). No results reported anywhere in this document are empirical claims; all quantities described are hypotheses to be tested by the minimal experiments specified.*
