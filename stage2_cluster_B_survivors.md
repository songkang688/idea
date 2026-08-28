# Stage 2 — Cluster B Survivors

Reviewer: Cloud Sub-Agent E (independent) for Supervisor Windows7.
Source: `stage1_cluster_B_ideas.md` / `stage1_cluster_B_index.csv` (branch `cursor/stage1-cluster-b-ideas-6596`), 366 ideas.

**Verdict counts: 74 KEEP + 12 PROTECTED = 86 survivors; 280 killed.**

Selection was NOT by mean score alone: portfolio balance across sections, explicit protection of high-risk/high-reward, simple counter-intuitive, cheaply falsifiable, and disagreement-prone ideas, and family-level dedup (one representative per idea family) all overrode raw composites. Several ideas with higher composites than some keeps were killed for redundancy or portfolio balance (marked "near-miss (painful)" in the scores file).

## PROTECTED set (12)

These are shielded from later-stage mean-score culling per the protection mandate.

### B-0007 [PROTECTED] — Medical Image Segmentation (core) (composite 7.5)
- **Idea:** Replace naive left-right flip augmentation with laterality-aware flipping that swaps paired labels, and audit how much silent damage naive flipping causes.
- **Why protected:** protected: simple counter-intuitive pipeline-bug audit; nearly free; disagreement-prone (everyone uses naive flips)

### B-0017 [PROTECTED] — Medical Image Segmentation (core) (composite 7.6)
- **Idea:** Replace fixed 0.5 thresholding of soft masks with a decision-theoretic per-case threshold chosen to maximize expected Dice/minimize expected volume error under the model's own predictive distribution.
- **Why protected:** protected: cheaply falsifiable free-gain claim (decision-theoretic thresholding); weekend compute; theory-practice gap

### B-0035 [PROTECTED] — Medical Vision Foundation Models (composite 8.2)
- **Idea:** Systematically audit train-test contamination between medical FM pretraining corpora and popular benchmarks via near-duplicate patient/scan detection, and publish decontaminated benchmark splits.
- **Why protected:** protected: disagreement-prone contamination audit; null result still publishable; could reorder FM rankings

### B-0058 [PROTECTED] — Medical Vision Foundation Models (composite 7.5)
- **Idea:** Train mixture-of-experts medical FMs and test whether unsupervised expert routing spontaneously discovers pathology (routing as a free abnormality detector).
- **Why protected:** protected: high-risk high-reward emergent-capability probe (MoE routing discovers pathology for free)

### B-0074 [PROTECTED] — Smoke/Fire/Transparent/Ambiguous Segmentation (composite 7.7)
- **Idea:** Repurpose pretrained dehazing networks' transmission-map estimators as zero-shot smoke segmenters, testing whether dehazing is secretly the strongest smoke prior available.
- **Why protected:** protected: days-of-work cross-field transfer test (dehazing as zero-shot smoke prior); decisive either way

### B-0107 [PROTECTED] — Domain Adaptation & Domain Shift (composite 7.8)
- **Idea:** Benchmark TTA under honest single-patient streaming (batch=1, no shuffling, no test-set reuse) and expose how much published gain depends on unrealistic batch composition.
- **Why protected:** protected: cheaply falsifiable disagreement-prone audit; honest batch=1 streaming may erase published TTA gains

### B-0121 [PROTECTED] — Few-shot / Zero-shot Segmentation (composite 7.9)
- **Idea:** Audit and quantify "foreground bias" in few-shot segmentation — models segmenting the salient object regardless of what the support actually shows — via wrong-support counterfactual testing.
- **Why protected:** protected: cheap counterfactual audit (wrong-support testing); disagreement-prone — could show FSS models ignore supports

### B-0177 [PROTECTED] — Prompt Learning (composite 7.5)
- **Idea:** Validation-free prompt overfitting detection: predict from prompt-space geometry (distance traveled from initialization, alignment with text manifold) whether a tuned prompt has overfit — no held-out data required.
- **Why protected:** protected: simple counter-intuitive claim — prompt-space geometry predicts overfitting with zero held-out data; cheap decisive test

### B-0196 [PROTECTED] — Weak / Semi / Self-supervised Learning (composite 7.8)
- **Idea:** Expose labeled-split variance in semi-supervised segmentation benchmarks: re-run standard protocols across many labeled-subset draws and test whether published method gaps exceed split noise.
- **Why protected:** protected: cheaply falsifiable disagreement-prone audit — labeled-split variance may exceed published SSL method gaps

### B-0230 [PROTECTED] — Synthetic Data (composite 8.0)
- **Idea:** Decompose synthetic data's advantage into label cleanliness versus image distribution: how much of the benefit is just that synthetic labels are perfect?
- **Why protected:** protected: simple counter-intuitive decomposition — synthetic data's benefit may be mostly perfect labels not images; cheap swap experiments settle it

### B-0272 [PROTECTED] — Long-tail Recognition & Segmentation (composite 7.7)
- **Idea:** Demonstrate that image-level resampling — the standard long-tail remedy — barely changes pixel-level class exposure in segmentation, and replace it with crop-level rebalancing.
- **Why protected:** protected: simple counter-intuitive audit — image-level resampling may barely change pixel-level exposure; one afternoon to falsify

### B-0353 [PROTECTED] — Multimodal Supervision for Dense Prediction (composite 7.0)
- **Idea:** Doppler audio as vessel supervision: the audio stream of Doppler ultrasound encodes flow presence and velocity — use it as free supervision for vessel segmentation in B-mode images.
- **Why protected:** protected: high-risk high-reward free signal — Doppler audio supervising vessel segmentation in B-mode; lab-recordable; nobody agrees it can work which is the point

## KEEP set (74)

### Medical Image Segmentation (core)

- **B-0002 [KEEP]** (composite 7.4) — Replace mask prediction for vessels/airways with prediction of a centerline flow field (direction + radius) from which the mask is reconstructed, to make connectivity the primary learned quantity.
  - *Verdict rationale:* connectivity-first output parameterization for tubular trees; clear falsifier (Betti error at matched Dice)
- **B-0003 [KEEP]** (composite 7.2) — Train segmentation models to predict the full inter-rater mask distribution and evaluate them against a fresh, unseen rater rather than a majority-vote consensus.
  - *Verdict rationale:* held-out-rater evaluation reframing; regulatory-relevant; changes conclusions of probabilistic seg work
- **B-0004 [KEEP]** (composite 7.9) — Optimize segmentation networks directly for downstream biomarker error (volume, diameter, ejection fraction) with the biomarker computed differentiably from the soft mask.
  - *Verdict rationale:* cheap decisive fine-tune experiment; Dice-biomarker decoupling claim directly clinically consequential
- **B-0014 [KEEP]** (composite 7.4) — Exploit unlabeled test-retest repeat scans as a free training signal by penalizing prediction disagreement between same-patient repeats.
  - *Verdict rationale:* unused free signal (unlabeled repeat scans); repeatability coefficient is the clinically binding metric
- **B-0023 [KEEP]** (composite 7.4) — Replace foreground-oversampled patch training with dual-stream training (whole-volume low-res context + local high-res patch) to fix false positives far from the target organ.
  - *Verdict rationale:* names an unarticulated failure (sampling-induced context starvation) plus distal-FP metric; cheap audit first
- **B-0027 [KEEP]** (composite 7.3) — Formulate 3D interactive correction as a conditional update network: one corrected slice (or scribble) plus current prediction in, corrected volume out — optimizing clicks-to-acceptable, not Dice.
  - *Verdict rationale:* repair-distribution training for interactive editing; clicks-to-acceptable as the honest cost function

### Medical Vision Foundation Models

- **B-0032 [KEEP]** (composite 7.5) — Run a controlled scaling-law study for 3D medical foundation models that separates the axes of dataset size, voxel resolution, and patient diversity.
  - *Verdict rationale:* axis-separated scaling laws (patients vs scans vs resolution); directs consortium data spending
- **B-0037 [KEEP]** (composite 7.8) — Train a medical in-context segmentation model (prompt with k example image-mask pairs, segment the query) and measure how in-context ability scales with pretraining task diversity, not data volume.
  - *Verdict rationale:* task-diversity vs data-volume scaling for in-context dense learning; strategic redirection of labeling investment
- **B-0038 [KEEP]** (composite 7.7) — Map where parameter-efficient adaptation must be placed in volumetric transformers: test the hypothesis that appearance shift requires early-layer adapters while label/task shift requires late-layer adapters.
  - *Verdict rationale:* cheap factorial; adapter-placement law (appearance=early / task=late) for volumetric transformers
- **B-0040 [KEEP]** (composite 8.0) — Measure whether medical FMs memorize rare patients — via membership-inference and near-copy reconstruction attacks on MIM-pretrained models — and identify which pretraining choices modulate it.
  - *Verdict rationale:* memorization/membership-inference science for volumetric MIM; legal stakes both directions; fully controlled design
- **B-0050 [KEEP]** (composite 7.6) — Establish a frozen-feature dense-probing benchmark for medical FMs and test whether FM rankings flip between linear probing and full fine-tuning.
  - *Verdict rationale:* frozen-probe vs fine-tune ranking-flip hypothesis; separates representation quality from recipe
- **B-0057 [KEEP]** (composite 7.7) — Test whether aggressive dedup + diversity-pruning of medical pretraining corpora (removing near-identical slices/series) lets a 10× smaller corpus match full-corpus FM quality.
  - *Verdict rationale:* data-curation law via dedup/density pruning; order-of-magnitude pretraining savings if true

### Smoke/Fire/Transparent/Ambiguous Segmentation

- **B-0061 [KEEP]** (composite 7.7) — Reformulate smoke segmentation as alpha-matte/optical-density regression instead of binary masking, because smoke physically has no boundary.
  - *Verdict rationale:* problem reframing (opacity regression; smoke has no boundary); convention-transfer falsifier
- **B-0062 [KEEP]** (composite 7.6) — Create physically grounded smoke ground truth by capturing smoke in front of calibrated patterned backgrounds, recovering true per-pixel transmittance analytically.
  - *Verdict rationale:* first physically calibrated smoke ground truth; unlocks entire measurement chain; lab capture feasible
- **B-0069 [KEEP]** (composite 8.0) — Develop and validate soft-boundary evaluation metrics for fuzzy objects by measuring which candidate metrics best predict human quality judgments of smoke/fire masks.
  - *Verdict rationale:* metric-vs-human-judgment validation for fuzzy masks; upstream of all smoke method claims; zero training
- **B-0078 [KEEP]** (composite 7.4) — Build a hard-negative stress benchmark for fire segmentation (sunsets, sodium lights, reflections, red foliage, welding) and show that radiometric cues from HDR/raw capture separate what tone-mapped RGB cannot.
  - *Verdict rationale:* confuser stress benchmark plus tone-mapping-destroys-evidence claim; re-anchors fire evaluation to deployment failures
- **B-0084 [KEEP]** (composite 7.5) — Model ultrasound acoustic shadows as first-class ambiguous regions: jointly predict shadow maps (from attenuation physics) and shadow-aware anatomy segmentation with explicit "no-evidence" outputs.
  - *Verdict rationale:* ultrasound shadow-stratified evaluation plus physics-derived evidence gating; shadows cheap to annotate
- **B-0085 [KEEP]** (composite 7.4) — Harvest free supervision from surveillance timelapses that capture the same static scene with and without smoke, using the clean frame as the known background in a compositing model.
  - *Verdict rationale:* archive-scale self-labeling from before/during camera pairs; derived-vs-hand-label showdown falsifier
- **B-0090 [KEEP]** (composite 7.9) — Formulate early smoke detection as sequential evidence accumulation with an explicit detection-latency-vs-false-alarm operating curve, instead of per-frame segmentation.
  - *Verdict rationale:* sequential-evidence accumulation with latency-vs-false-alarm curves; latency is the true objective the field cannot express

### Domain Adaptation & Domain Shift

- **B-0091 [KEEP]** (composite 7.5) — Solve the test-time-adaptation model-selection problem with a label-free surrogate validation signal (cross-augmentation prediction agreement) validated against oracle selection.
  - *Verdict rationale:* label-free surrogate validation for TTA model selection; unblocks honest deployment of the whole TTA family
- **B-0093 [KEEP]** (composite 7.5) — Disentangle covariate shift from label-distribution shift in BN-statistic adaptation: recalibrating BN on target batches silently conflates the two and mis-adapts when class prevalence differs.
  - *Verdict rationale:* covariate-vs-label-shift conflation in BN recalibration; names a silent failure with a clean factorial test
- **B-0095 [KEEP]** (composite 7.3) — Empirically decompose cross-site medical performance drop into scanner, protocol, and population components using matched-cohort counterfactual datasets.
  - *Verdict rationale:* scanner/protocol/population decomposition of cross-site drop; matched-cohort audit the field cites but lacks
- **B-0096 [KEEP]** (composite 7.7) — Establish a "shift-type → adaptation-locus" law: appearance shifts are correctable by normalization-layer adaptation alone, while geometric shifts require spatial-module adaptation, tested via controlled factorial shifts.
  - *Verdict rationale:* shift-type to adaptation-locus law via controlled factorial shifts; mechanistic and directly prescriptive
- **B-0103 [KEEP]** (composite 6.6) — Audit which self-supervised auxiliary losses actually correlate with segmentation improvement in single-image test-time training, across shift types — and expose anti-correlated ones.
  - *Verdict rationale:* audit of which auxiliary losses actually track segmentation gain in test-time training; exposes anti-correlated ones
- **B-0105 [KEEP]** (composite 6.8) — Replace learned style transfer with physics-derived acquisition mappings (e.g., CT kernel changes as measurable convolution kernels) for adaptation across reconstruction protocols.
  - *Verdict rationale:* physics-derived kernel mappings replace learned style transfer; mechanism-first adaptation with measurable ground truth
- **B-0112 [KEEP]** (composite 7.6) — Build a taxonomy and detector for label-consistent shift — cases where appearance is in-distribution but the label convention differs — where any feature-level adaptation is guaranteed harmful.
  - *Verdict rationale:* label-consistent shift taxonomy (adaptation guaranteed harmful); genuinely unnamed failure class; referenced by B-0012 kill

### Few-shot / Zero-shot Segmentation

- **B-0123 [KEEP]** (composite 7.8) — Construct a genuinely-novel-class benchmark (classes verifiably absent from web-scale pretraining) and measure how much "zero-shot segmentation" performance evaporates on it.
  - *Verdict rationale:* genuinely-novel-class benchmark; quantifies how much zero-shot performance is pretraining contamination
- **B-0124 [KEEP]** (composite 7.8) — Show that support-set selection explains more performance variance than method choice in FSS, and build active support selection (choosing which k examples to label) as the highest-leverage intervention.
  - *Verdict rationale:* support-selection variance vs method variance; if supports dominate the leaderboard the field is measuring the wrong thing
- **B-0128 [KEEP]** (composite 7.4) — Disentangle recognition from delineation in FSS evaluation: measure separately whether the model found the right object and how well it drew the boundary, since these have different failure causes and cures.
  - *Verdict rationale:* recognition-vs-delineation decomposition of FSS error; different causes need different cures; zero-training eval science
- **B-0131 [KEEP]** (composite 7.4) — Factor cross-domain FSS failure (natural-image supports/training → medical/industrial queries) into feature-transfer failure vs. matching-mechanism failure with swap experiments.
  - *Verdict rationale:* feature-transfer vs matching-mechanism factorization of cross-domain FSS failure via swap experiments; clean causal design
- **B-0133 [KEEP]** (composite 7.4) — Few-shot segmentation of relationally defined targets ("the handle of any tool", "the damaged part") where the class is a role, not an appearance category.
  - *Verdict rationale:* relationally-defined targets (class as role not appearance); genuinely new task with hard negatives built in
- **B-0143 [KEEP]** (composite 7.2) — Settle when test-time fine-tuning on the support set helps versus hurts FSS, as a function of shot count, support-query domain gap, and parameter subset — producing a practitioner's decision table.
  - *Verdict rationale:* when test-time fine-tuning helps vs hurts as a function of shots/gap/parameter-subset; practitioner decision table
- **B-0145 [KEEP]** (composite 7.6) — Text-plus-shots division of labor: use language to solve recognition (which object) and the few shots only to define the boundary convention (how to delineate it).
  - *Verdict rationale:* division of labor — language solves recognition and shots define the boundary convention; testable decomposition of what shots are for

### Prompt Learning

- **B-0151 [KEEP]** (composite 7.4) — Determine what learned soft prompts actually encode — class semantics or dataset-specific bias — via nearest-text projection and cross-dataset prompt-transplant experiments.
  - *Verdict rationale:* what soft prompts actually encode (semantics vs dataset bias) via projection and transplant; interpretability with teeth
- **B-0154 [KEEP]** (composite 6.8) — Quantify prompt-position sensitivity of promptable segmenters (output variance across equivalent clicks inside the same object) and use that variance as a per-case failure predictor.
  - *Verdict rationale:* prompt-position sensitivity as a per-case failure predictor; nearly free to measure; practical reliability signal
- **B-0159 [KEEP]** (composite 7.7) — Convention tokens: train one segmenter on multiple datasets with conflicting delineation conventions, exposing the convention as a switchable prompt, so one model serves all conventions on demand.
  - *Verdict rationale:* convention tokens expose delineation convention as a switchable prompt; one model serves conflicting conventions; anchors the convention family
- **B-0164 [KEEP]** (composite 7.0) — Uncertainty-eliciting prompts: learn prompts whose output channel is a calibrated per-pixel confidence for a frozen dense model, extracting reliability information the model has but does not express.
  - *Verdict rationale:* uncertainty-eliciting prompts extract calibrated confidence a frozen dense model has but does not express; new use of the prompt channel
- **B-0167 [KEEP]** (composite 7.2) — Textual inversion for domain jargon: learn pseudo-word embeddings for concepts VLMs don't know ("GGO", "slag inclusion", "delamination") from a few masked examples, enabling open-vocabulary segmentation of specialist vocabularies.
  - *Verdict rationale:* textual inversion for specialist jargon (GGO/slag/delamination); practical open-vocab entry to expert domains; cheap

### Weak / Semi / Self-supervised Learning

- **B-0182 [KEEP]** (composite 7.5) — Quantify pseudo-label error heritability across self-training generations (which errors persist, amplify, or die out) and design error-decorrelated co-training informed by the heritability map.
  - *Verdict rationale:* pseudo-label error heritability across self-training generations; population-genetics lens on error dynamics; genuinely unasked
- **B-0189 [KEEP]** (composite 7.4) — Re-measure the scribble-supervision cost curve in the foundation-model era: how few scribbles suffice when combined with strong class-agnostic mask priors, and where does scribble information still matter?
  - *Verdict rationale:* re-measuring the scribble cost curve in the foundation-model era; where does scribble information still matter; directly actionable
- **B-0193 [KEEP]** (composite 7.4) — Speckle-native self-supervised pretraining for ultrasound: pretext tasks built on speckle statistics (decorrelation prediction, statistics-map estimation) instead of natural-image SSL recipes that treat speckle as noise.
  - *Verdict rationale:* speckle-native SSL pretexts treat ultrasound physics as signal not noise; mechanism-grounded modality-specific pretraining
- **B-0197 [KEEP]** (composite 7.2) — Test whether anatomically impossible mixing augmentations (CutMix/CopyPaste across patients) help or hurt medical semi-supervised segmentation, against the assumption that unrealistic mixes are harmless regularization.
  - *Verdict rationale:* simple counter-intuitive factorial: do anatomically impossible mixes help or hurt medical SSL; weekend compute; either answer publishable
- **B-0201 [KEEP]** (composite 6.8) — Co-training on genuinely independent views (frontal/lateral X-rays, multi-parametric MRI sequences) versus artificially augmented views, quantifying how much real view independence is worth.
  - *Verdict rationale:* genuine view independence (frontal/lateral and mpMRI) vs augmented views in co-training; quantifies an assumption the field inherited
- **B-0207 [KEEP]** (composite 7.2) — Factorial dissection of noise types in noisy-student self-training for segmentation: which perturbation channel (input noise, feature dropout, label perturbation, depth/stochastic path) actually drives the dense-prediction gains.
  - *Verdict rationale:* factorial dissection of which noise channel drives noisy-student gains for dense prediction; cheap and directly prescriptive

### Synthetic Data

- **B-0212 [KEEP]** (composite 8.1) — Demonstrate and defeat the blending-artifact shortcut: models trained on lesions inpainted into healthy scans learn to detect inpainting boundaries, not lesions.
  - *Verdict rationale:* blending-artifact shortcut — inpainted-lesion training may teach inpainting detection; cheap decisive control experiments; indicts a popular recipe
- **B-0213 [KEEP]** (composite 7.5) — Estimate the real-synthetic exchange rate — how many synthetic samples substitute for one real labeled sample — as a measurable function of generator, task, and domain.
  - *Verdict rationale:* real-synthetic exchange rate as a measurable function of generator/task/domain; turns synthetic-data hype into a number
- **B-0214 [KEEP]** (composite 7.5) — Build a utility-predictive quality metric for synthetic segmentation data, benchmarked by correlation with actual downstream training gains — replacing FID, which predicts nothing about dense-task utility.
  - *Verdict rationale:* utility-predictive quality metric benchmarked against downstream gains; FID demonstrably predicts nothing for dense tasks
- **B-0222 [KEEP]** (composite 8.0) — Measure the thin-structure fidelity floor of latent diffusion (structures below which latent compression destroys them) and establish when pixel-space generation is required for training data.
  - *Verdict rationale:* thin-structure fidelity floor of latent compression; measurable law with direct consequences for medical synthetic data
- **B-0223 [KEEP]** (composite 7.5) — Quantify when synthetic validation sets can be trusted for model selection: measure rank correlation between synthetic-val and real-val decisions across realistic model pools.
  - *Verdict rationale:* rank correlation between synthetic-val and real-val model selection; can synthetic data be trusted for decisions not just training
- **B-0235 [KEEP]** (composite 7.1) — Build generator blind-spot maps — a systematic catalog of visual phenomena a given generator cannot produce — and use them to predict where synthetic-trained models will fail and what real data to collect.
  - *Verdict rationale:* generator blind-spot maps predict where synthetic-trained models fail and what real data to collect; diagnostic with procurement value

### Annotation Efficiency

- **B-0241 [KEEP]** (composite 7.3) — A sealed, cost-honest benchmark for active learning in segmentation — realistic batch sizes, cold starts, and time-based (not image-count) budgets — testing whether published AL gains survive.
  - *Verdict rationale:* sealed cost-honest active-learning benchmark (time budgets not image counts); tests whether published AL gains survive realistic accounting
- **B-0244 [KEEP]** (composite 7.4) — Measure automation-bias contamination in model-assisted annotation — annotators anchoring on pre-segmentations — and design blind-review protocols that keep the speed without inheriting the model's errors.
  - *Verdict rationale:* automation-bias contamination of model-assisted annotation; measures whether assisted datasets silently inherit model errors
- **B-0247 [KEEP]** (composite 7.5) — Show that consensus label fusion (STAPLE-style) fails when raters share training lineage (correlated biases), and build lineage-aware fusion that models rater covariance.
  - *Verdict rationale:* STAPLE fails under correlated rater lineage; testable indictment of a canonical fusion tool plus a principled fix
- **B-0255 [KEEP]** (composite 7.5) — Measure the gap between simulated and real users in interactive-segmentation evaluation, then build empirically calibrated user models — because current click simulators may be crowning the wrong methods.
  - *Verdict rationale:* simulated-vs-real user gap in interactive segmentation evaluation; click simulators may be crowning the wrong methods
- **B-0261 [KEEP]** (composite 6.8) — Validate micro-verification as a supervision channel: 3-second binary questions ("is the boundary correct in this circle?") aggregated across many viewers into training-grade boundary supervision.
  - *Verdict rationale:* micro-verification (3-second binary checks) validated as a supervision channel; aggregation-to-training-grade is the open question
- **B-0269 [KEEP]** (composite 7.7) — Treat annotation-guideline wording as an experimental variable: controlled guideline A/B tests measuring how phrasing and example choice shift the resulting labels.
  - *Verdict rationale:* guideline wording as a controlled experimental variable; annotation-protocol science; upstream of every dataset in the catalog

### Long-tail Recognition & Segmentation

- **B-0271 [KEEP]** (composite 7.9) — Disentangle the three conflated imbalance axes in long-tail segmentation — image frequency, instance frequency, and pixel area — and show each requires a different remedy.
  - *Verdict rationale:* disentangles image/instance/pixel imbalance axes conflated by the entire long-tail-segmentation literature; each needs a different remedy
- **B-0274 [KEEP]** (composite 7.6) — Run the statistical power analysis of long-tail benchmarks: with a handful of test instances per tail class, published per-class improvements may be statistically meaningless — quantify and fix the reporting.
  - *Verdict rationale:* statistical power audit of long-tail benchmarks; per-class gains on a handful of test instances may be noise; reporting fix included
- **B-0275 [KEEP]** (composite 7.4) — Test whether the decoupling result from long-tail classification (representations are fine, only the classifier needs rebalancing) transfers to dense prediction, where the "classifier" is a spatial decoder.
  - *Verdict rationale:* does the classification decoupling result (representations fine; rebalance the classifier) survive dense prediction with spatial decoders
- **B-0285 [KEEP]** (composite 7.2) — Rare anatomical variants as medical long-tail: build a variant-enriched evaluation (situs inversus, accessory organs, post-surgical anatomy) and a variant-detection safety layer that flags when standard models should not be trusted.
  - *Verdict rationale:* rare anatomical variants (situs inversus and post-surgical) as the medical long tail; safety layer that flags when standard models should abstain
- **B-0292 [KEEP]** (composite 7.0) — Compositional long-tail: build evaluation and methods for rare class-attribute combinations (rusty car, flooded road) that class-level long-tail analysis cannot see.
  - *Verdict rationale:* compositional long-tail (rare class-attribute combinations) invisible to class-level analysis; new evaluation axis with hallucination accounting

### Cross-domain Transfer

- **B-0302 [KEEP]** (composite 7.4) — Establish the science of 2D→3D weight inflation: which inflation strategy wins, when inflation beats native 3D pretraining, and what property of the 2D source predicts inflated performance.
  - *Verdict rationale:* science of 2D-to-3D weight inflation; when inflation beats native 3D pretraining and what predicts it; practical for every 3D group
- **B-0306 [KEEP]** (composite 7.0) — Attribute the histopathology scanner gap to its physical components — optics (PSF, focus), color pipeline, and compression — via component-wise simulation, enabling targeted physics-informed calibration transfer.
  - *Verdict rationale:* physical attribution of the histopath scanner gap (optics/color/compression) via component-wise simulation; mechanism not style
- **B-0313 [KEEP]** (composite 7.3) — Benchmark domain-distance metrics as transfer predictors: which cheap measurement between source and target best predicts realized fine-tuning gain across many domain pairs — building a validated "transferability oracle" for dense tasks.
  - *Verdict rationale:* validated transferability oracle for dense tasks; which cheap domain-distance measurement predicts realized fine-tuning gain
- **B-0319 [KEEP]** (composite 7.0) — Test the anomaly-segmentation universality hypothesis: joint training on industrial defects and medical lesions improves both, because both tasks share a "deviation from learned normality" core.
  - *Verdict rationale:* anomaly-universality hypothesis: joint industrial-defect + medical-lesion training tests a shared deviation-from-normality core; either result informative
- **B-0327 [KEEP]** (composite 7.7) — Audit "universal" segmentation models on verifiably held-out domains and publish domain-coverage cartography: where universality claims actually hold.
  - *Verdict rationale:* universality audit on verifiably held-out domains with coverage cartography; directly tests the field's loudest current claim
- **B-0328 [KEEP]** (composite 7.1) — Fit the annotation-versus-distance law for porting: the minimum target annotation needed to close a cross-domain gap as a function of measured domain distance — pricing every port in labels.
  - *Verdict rationale:* annotation-versus-distance law prices every cross-domain port in labels; the number every deployment team actually needs

### Multimodal Supervision for Dense Prediction

- **B-0331 [KEEP]** (composite 7.8) — Mine negations from radiology reports ("no pneumothorax", "unremarkable liver") into certified-negative spatial supervision — the report's most reliable content, currently discarded.
  - *Verdict rationale:* negation mining turns reports' most reliable content (certified absence) into spatial supervision; currently discarded by every pipeline
- **B-0344 [KEEP]** (composite 7.8) — Mine historical radiotherapy dose maps and plans as free dense supervision: clinically approved dose distributions encode organ-at-risk and target geometry with life-critical precision.
  - *Verdict rationale:* radiotherapy dose maps as free dense supervision; clinically approved plans encode organ and target geometry with life-critical precision; public RT archives exist
- **B-0350 [KEEP]** (composite 8.1) — Audit suggestion-induced hallucination in text-conditioned medical segmentation: does asking for a finding make the model draw one that isn't there?
  - *Verdict rationale:* suggestion-induced hallucination audit for text-conditioned medical segmentation; does asking for a finding make the model draw one; safety-critical and cheap
- **B-0360 [KEEP]** (composite 7.4) — A grounding-capability taxonomy for medical vision-language segmenters: systematically measure what current models actually ground — anatomy terms, finding terms, spatial modifiers, quantities — as the diagnostic foundation for the report-supervision program.
  - *Verdict rationale:* grounding-capability taxonomy for medical vision-language segmenters; measures what models actually ground (anatomy / findings / modifiers / quantities); diagnostic foundation for the report-supervision program

### Cross-cutting Wildcards

- **B-0361 [KEEP]** (composite 7.7) — Test whether ambiguity handling is one transferable skill: does a model trained to express uncertainty on multi-rater medical boundaries transfer that competence to smoke boundaries and camouflage, or is ambiguity handling domain-bound?
  - *Verdict rationale:* is ambiguity handling one transferable skill; bridges multi-rater medical boundaries and smoke/camouflage; cross-cutting question no single community can ask
- **B-0362 [KEEP]** (composite 8.0) — Measure the metric-decision correlation: which segmentation metric improvements actually change downstream decisions (treatment choice, alarm raised, robot action), and how much published "progress" is decision-invisible.
  - *Verdict rationale:* metric-decision correlation; how much published segmentation progress is invisible to downstream decisions; reframes what improvement means
- **B-0366 [KEEP]** (composite 7.8) — Simulate the multi-generation dataset ecosystem: models assist annotation, the resulting datasets train the next models, which assist the next annotation — measuring whether dense-prediction data ecosystems drift toward model-error fixation ("annotation collapse").
  - *Verdict rationale:* annotation-collapse dynamics of multi-generation model-assisted dataset ecosystems; the dataset analog of model collapse; simulatable now with archival generations

