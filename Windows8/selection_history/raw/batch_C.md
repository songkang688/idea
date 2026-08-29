# Stage-1 Idea Batch C — Adjacent High-Upside Scientific Questions

**Generator mandate:** ideas that failure-of-methods and evaluation/robustness generators would miss — negative-result science, hidden benchmark confounders, training-dynamics hypotheses, data-centric hypotheses, compute-economics-as-science, cross-field transplants with a mechanism, amorphous/hard-material domains that expose general vision principles, and simple anti-modular ideas.

**Scope:** Vision Foundation Models (VFMs), SAM-family adaptation, PEFT, VLMs for dense prediction, medical VFM, prompt learning, weak/semi/self-supervision, few/zero-shot segmentation, domain adaptation.

**Contents:** IDEA-C-0001 … IDEA-C-0350 (350 ideas), followed by 20 mutations, 10 community-assumption challenges, and near-duplicate notes.

**Cluster key:**

| Tag | Cluster | IDs |
|---|---|---|
| NEG | Negative-result science (things that "should work" but plausibly don't) | 0001–0030 |
| CONF | Hidden confounders in popular benchmarks | 0031–0060 |
| DYN | Training-dynamics hypotheses | 0061–0095 |
| DATA | Data-centric hypotheses (label noise geometry, slice inconsistency, leakage) | 0096–0130 |
| ECON | Compute/economics hypotheses that become scientific | 0131–0150 |
| XFER | Cross-field transplants with an explicit mechanism | 0151–0180 |
| AMORPH | Smoke/fire/transparent/amorphous objects exposing general principles | 0181–0200 |
| MED | Medical VFM science | 0201–0230 |
| RSIND | Remote sensing and industrial inspection exposing general principles | 0231–0255 |
| PROMPT | Prompt learning / prompting science for SAM-family and VLMs | 0256–0280 |
| PEFT | PEFT science (LoRA/adapters/prompt-tuning mechanics) | 0281–0305 |
| FSS | Few/zero-shot segmentation | 0306–0320 |
| DA | Domain adaptation | 0321–0335 |
| SSL | Weak/semi/self-supervision | 0336–0350 |

All experiments are designed to be cheap: single-GPU scale, frozen or PEFT-adapted public checkpoints, existing public datasets, or small controlled synthetic sets. No invented citations; where prior work plausibly exists, the "Why Possibly Novel" field states the distinguishing delta as a claim to be verified during literature check.

---
## Cluster NEG — Negative-Result Science (IDEA-C-0001 … IDEA-C-0030)

### IDEA-C-0001 — Decoder-resolution ceiling makes SAM boundary errors scale-invariant
- **One-sentence idea:** Test whether SAM-family boundary errors on high-curvature objects are set by the mask decoder's token/upsampling resolution rather than encoder capacity, so scaling the image encoder cannot fix them.
- **Problem:** The community scales encoders expecting better masks, but boundary quality may be bottlenecked by the lightweight decoder.
- **Core Hypothesis (falsifiable):** Boundary F-score on objects whose contour curvature spectrum exceeds the decoder's effective spatial bandwidth is statistically identical across SAM-B/L/H encoders, while interior IoU improves with scale.
- **Why Important:** If true, most compute spent on encoder scaling for interactive segmentation is wasted; the fix is architectural, not scale.
- **Why Possibly Novel:** Scaling analyses report aggregate mIoU; a curvature-stratified decomposition attributing error to decoder bandwidth appears untested.
- **Minimal Experiment:** Take SAM-B/L/H with identical decoders; evaluate on a curvature-stratified subset of SA-1B-style masks and synthetic star-shapes with swept curvature; plot boundary-F vs curvature per encoder; then swap in a higher-resolution decoder head trained briefly and show the curve shifts.
- **Main Risk:** Encoder scale may partially compensate via better token features, blurring the predicted flat scaling curve.
- **Research Cluster:** NEG

### IDEA-C-0002 — LoRA on the encoder cannot fix prompt-decoder interaction errors
- **One-sentence idea:** Show that a specific, identifiable class of SAM errors (ambiguity resolution given multiple prompts) is invariant to encoder-side PEFT because it originates in the prompt-encoder/decoder interaction.
- **Problem:** Practitioners default to LoRA on the image encoder for SAM adaptation without knowing which errors that can even address.
- **Core Hypothesis (falsifiable):** Errors where two prompt sets that should produce different masks produce the same mask persist at the same rate after encoder-only LoRA, but drop after decoder-only fine-tuning with 100x fewer trainable parameters.
- **Why Important:** Establishes an error-to-component attribution methodology that would redirect much SAM-adaptation effort.
- **Why Possibly Novel:** Component-wise causal attribution of SAM error types (vs. ablation of accuracy) is rarely done; most papers tune everything.
- **Minimal Experiment:** Build a 500-image "prompt-discrimination" test (pairs of prompt sets with distinct ground-truth masks); fine-tune encoder-LoRA vs decoder-only on the same small train set; compare error-type histograms, not just mIoU.
- **Main Risk:** Error types may not cleanly separate by component; interaction effects could dominate.
- **Research Cluster:** NEG

### IDEA-C-0003 — Pretraining-scale does not improve thin-structure segmentation
- **One-sentence idea:** Test the negative result that VFM pretraining scale (data and parameters) leaves segmentation of thin structures (vessels, cracks, wires) flat because contrastive/MIM objectives are area-biased.
- **Problem:** Thin structures carry little pixel area, so pretraining losses weight them negligibly, yet everyone expects "better features" to help them.
- **Core Hypothesis (falsifiable):** Linear-probe segmentation accuracy stratified by structure width shows near-zero slope vs pretraining scale for widths under ~4 px, while wide-structure accuracy scales log-linearly.
- **Why Important:** Thin structures dominate medical/industrial value; if scaling doesn't buy them, targeted objectives are needed and scaling claims need width-stratified reporting.
- **Why Possibly Novel:** Scaling-law papers report aggregate metrics; width-stratified scaling curves for dense prediction appear absent.
- **Minimal Experiment:** Freeze DINOv2/CLIP/SAM encoders of multiple sizes; train identical linear/light decoders on DRIVE (vessels), CrackForest, and a wire dataset; plot accuracy-vs-model-scale per width decile.
- **Main Risk:** Confound between model scale and pretraining recipe across public checkpoints; mitigate with same-family checkpoints only.
- **Research Cluster:** NEG

### IDEA-C-0004 — Medical zero-shot SAM failure is prompt-ambiguity, not domain gap
- **One-sentence idea:** Disentangle whether zero-shot SAM fails on medical images because of texture/domain shift or because medical targets are ambiguous under point prompting (nested organs, no closed contrast boundaries).
- **Problem:** "SAM fails on medical" is attributed wholesale to domain gap, driving expensive re-pretraining (MedSAM-style) that may be misdirected.
- **Core Hypothesis (falsifiable):** On medical structures with unambiguous closed boundaries (e.g., full-contrast implants, air pockets), zero-shot SAM matches natural-image performance; the measured "medical gap" concentrates almost entirely in structures with nested/ambiguous prompt semantics.
- **Why Important:** If the gap is ambiguity, the fix is prompt protocol and multi-mask supervision, far cheaper than domain pretraining.
- **Why Possibly Novel:** Existing medical-SAM evaluations do not stratify by an operationalized prompt-ambiguity score.
- **Minimal Experiment:** Define ambiguity as the number of plausible nested masks containing a click (computable from ground-truth label hierarchies); evaluate zero-shot SAM on CT/MR structures stratified by this score and matched natural-image controls.
- **Main Risk:** Texture statistics and ambiguity are correlated in real anatomy; needs careful matched controls.
- **Research Cluster:** NEG

### IDEA-C-0005 — PEFT fails exactly when the task needs new early-layer frequency response
- **One-sentence idea:** Characterize the boundary of PEFT applicability by showing it fails when the target task requires changing the stem/early layers' frequency selectivity (e.g., speckle, moiré, halftone domains).
- **Problem:** PEFT vs full fine-tuning comparisons are empirical grab-bags with no predictive theory of when PEFT is insufficient.
- **Core Hypothesis (falsifiable):** On synthetic tasks whose discriminative signal is placed at controlled spatial frequencies, PEFT (late-layer LoRA/adapters) matches full FT for frequencies inside the pretrained stem's passband and degrades sharply outside it, at a predictable cutoff measurable from the frozen stem's transfer function.
- **Why Important:** Gives practitioners an a-priori test ("is my domain outside the stem passband?") replacing trial-and-error.
- **Why Possibly Novel:** Frequency-domain characterization of the PEFT/full-FT boundary appears unexplored; existing work compares accuracy on natural datasets where frequency demands are uncontrolled.
- **Minimal Experiment:** Generate band-pass-filtered texture segmentation tasks at swept center frequencies; adapt a frozen ViT with LoRA at various depths vs full FT; plot accuracy vs frequency vs adaptation depth.
- **Main Risk:** ViT patch embedding is one linear layer, so "frequency response" may be broader than hypothesized, weakening the effect.
- **Research Cluster:** NEG

### IDEA-C-0006 — Open-vocabulary segmentation cannot name materials, only objects
- **One-sentence idea:** Establish a negative result that CLIP-derived dense predictors systematically fail on material queries ("glass", "metal", "wet") because caption supervision binds nouns to object identity, not surface properties.
- **Problem:** Open-vocab segmentation is marketed as "segment anything you can name," but material and state words may be structurally unsupported.
- **Core Hypothesis (falsifiable):** For query pairs (object noun vs material noun) on the same regions, IoU for material queries is lower by a large margin and does not improve with model scale, while object-noun IoU does.
- **Why Important:** Materials matter for robotics, recycling, and inspection; identifying a structural gap redirects data collection (material-labeled captions) rather than architecture work.
- **Why Possibly Novel:** Material perception is studied separately; a controlled object-vs-material query benchmark inside open-vocab segmentation appears missing.
- **Minimal Experiment:** Reuse a materials dataset with object labels; query the same open-vocab segmenter with object names vs material names for identical regions; compare IoU distributions and scaling across model sizes.
- **Main Risk:** Some material words (e.g., "glass") double as object nouns; requires careful query vocabulary design.
- **Research Cluster:** NEG

### IDEA-C-0007 — Inverse scaling under weak evidence: bigger SAMs hallucinate more on camouflage
- **One-sentence idea:** Test whether larger interactive segmenters perform worse than smaller ones on camouflaged/low-contrast targets given sparse prompts, because stronger shape priors override weak image evidence.
- **Problem:** Scaling is assumed monotone; prior-dominated regimes may show inverse scaling that aggregate benchmarks hide.
- **Core Hypothesis (falsifiable):** With one point prompt on camouflaged-object datasets, mask IoU decreases (or precision drops with confident overreach) as encoder scale increases; with dense prompts the ordering reverses.
- **Why Important:** Identifies a prompt-density-dependent scaling regime, informing when to deploy small vs large models.
- **Why Possibly Novel:** Inverse-scaling phenomena are documented in LLMs; a controlled analog for promptable segmentation is not established.
- **Minimal Experiment:** Evaluate SAM-B/L/H and Efficient-SAM variants on COD10K with 1, 3, 10 clicks; plot IoU vs scale per prompt budget; inspect whether large-model errors are confident prior-shaped masks.
- **Main Risk:** Public checkpoints differ in more than scale; use distilled families where only capacity varies for confirmation.
- **Research Cluster:** NEG

### IDEA-C-0008 — Semi-supervised segmentation gains evaporate under label/unlabeled distribution mismatch
- **One-sentence idea:** Show that consistency-based semi-supervised segmentation methods implicitly assume the unlabeled pool matches the labeled class-mixture, and their gains invert when the unlabeled pool is class-shifted.
- **Problem:** Real unlabeled pools (hospital archives, web scrapes) are never distribution-matched, but benchmarks always match them.
- **Core Hypothesis (falsifiable):** Sweeping the unlabeled pool's class mixture away from the labeled mixture produces a monotone decay in semi-supervised gain, crossing zero (worse than supervised-only) at a measurable mixture distance.
- **Why Important:** Defines the operating envelope of a whole method family, and gives a pre-deployment diagnostic (estimate mixture distance first).
- **Why Possibly Novel:** Class-mismatch is studied in semi-supervised classification; a quantitative gain-vs-mismatch curve for dense prediction appears absent.
- **Minimal Experiment:** On Cityscapes/Pascal-VOC, hold labeled set fixed; resample unlabeled pools at controlled class-mixture divergences (using ground truth for pool construction only); train a standard mean-teacher method; plot gain vs divergence.
- **Main Risk:** Pixel-level class mixing (multiple classes per image) makes clean mixture control harder than in classification.
- **Research Cluster:** NEG

### IDEA-C-0009 — Test-time adaptation improves mIoU while silently destroying calibration
- **One-sentence idea:** Quantify the negative result that entropy-minimization TTA for segmentation trades calibration for accuracy, making downstream uncertainty consumers (auto-labeling, safety monitors) worse off.
- **Problem:** TTA papers report accuracy; deployed dense predictors are consumed via confidence thresholds that TTA may corrupt.
- **Core Hypothesis (falsifiable):** Across standard TTA methods on corrupted Cityscapes, expected calibration error and over-confidence on wrong boundary pixels increase superlinearly with adaptation steps even while mIoU improves, and pseudo-label pipelines fed by the adapted model perform worse than with the unadapted model.
- **Why Important:** Reveals that a metric improvement can be an end-to-end regression, arguing for calibration-constrained TTA.
- **Why Possibly Novel:** TTA calibration has been noted in classification; the downstream pseudo-labeling consequence for segmentation pipelines is unmeasured.
- **Minimal Experiment:** Run TENT-style TTA on Cityscapes-C; track mIoU, ECE, and boundary-pixel confidence; then use adapted vs unadapted models to pseudo-label a second dataset and compare student model quality.
- **Main Risk:** Some TTA variants include confidence regularizers that partially mask the effect; must test several.
- **Research Cluster:** NEG

### IDEA-C-0010 — Prompt tuning cannot express negation regardless of token budget
- **One-sentence idea:** Establish an expressivity negative result: continuous prompt tuning on frozen VLM dense predictors cannot implement "everything except X" semantics, no matter how many prompt tokens are used.
- **Problem:** Prompt tuning is treated as a universal adapter; its logical expressivity limits over a frozen model are unknown.
- **Core Hypothesis (falsifiable):** For complement-class tasks (segment all non-X pixels) constructed from existing datasets, prompt tuning plateaus far below a linear head on frozen features, and the gap does not shrink with prompt length, because the frozen attention cannot invert similarity orderings.
- **Why Important:** Negation/exclusion queries are common in practice (defect = anything not normal); knowing prompts can't do it changes method choice.
- **Why Possibly Novel:** Prompt expressivity theory exists for transformers abstractly; a concrete falsifiable test on dense prediction with complement semantics is new territory.
- **Minimal Experiment:** Build complement tasks from VOC (segment everything-but-dogs); compare prompt tuning (lengths 1–256) vs linear probe vs LoRA on a frozen CLIP-DenseCRF-style pipeline; plot accuracy vs prompt length.
- **Main Risk:** The model might implement negation via background-class shortcuts, requiring careful task construction to block.
- **Research Cluster:** NEG

### IDEA-C-0011 — Iterated self-training on SAM pseudo-masks is morphological erosion
- **One-sentence idea:** Test whether repeated self-distillation on SAM-generated pseudo-masks systematically shrinks high-curvature details, acting like a curvature-dependent erosion operator across generations.
- **Problem:** Auto-labeling loops (SAM labels → train → re-label) are becoming standard; their fixed-point geometry is unstudied.
- **Core Hypothesis (falsifiable):** Across N self-training generations, mask curvature spectra lose high-frequency energy at a constant per-generation rate, and protrusions below a critical width vanish entirely, independent of dataset.
- **Why Important:** Predicts a hard limit for iterated auto-labeling and motivates curvature-preserving regularizers before the community locks in the pipeline.
- **Why Possibly Novel:** Self-training degradation is discussed for class balance; a geometric/spectral characterization of mask shape drift is missing.
- **Minimal Experiment:** Run 5 generations of pseudo-label self-training on VOC with a fixed architecture; measure per-generation contour Fourier descriptors and protrusion survival vs width; verify the same decay constants on a second dataset.
- **Main Risk:** Decay may be architecture-specific rather than universal; test two decoder families.
- **Research Cluster:** NEG

### IDEA-C-0012 — Prompt-following does not distill: capability-selective distillation failure
- **One-sentence idea:** Show that distilling SAM into efficient students preserves single-prompt mask quality but selectively destroys multi-prompt compositional behavior (prompt-following), i.e., capabilities distill non-uniformly.
- **Problem:** Efficient-SAM-style students are validated on the same single-prompt metrics as teachers, hiding capability loss.
- **Core Hypothesis (falsifiable):** On a prompt-composition test suite (add/remove points, box+point conflicts), student-teacher agreement is high for one prompt and collapses monotonically with prompt count, even when single-prompt mIoU matches.
- **Why Important:** Warns that "97% of teacher performance" claims can be false for interactive use, and gives a distillation-target fix (compositional traces).
- **Why Possibly Novel:** Capability-selective distillation loss is discussed in LLMs; no dense-prediction analog with a concrete prompt-composition suite exists.
- **Minimal Experiment:** Evaluate MobileSAM/EfficientSAM vs SAM-H on scripted prompt sequences; report agreement vs prompt count; then re-distill with multi-prompt traces and show the gap closes.
- **Main Risk:** Effect size may be small for well-trained students; suite must include genuinely conflicting prompts.
- **Research Cluster:** NEG

### IDEA-C-0013 — Click simulators are information-optimal agents that inflate interactive benchmarks
- **One-sentence idea:** Quantify how much standard "click at center of largest error region" simulators overstate real-user performance because they implement a near-optimal information-seeking policy humans do not follow.
- **Problem:** Interactive segmentation progress is measured in NoC under simulators; the human-simulator gap is unmeasured and may reorder methods.
- **Core Hypothesis (falsifiable):** With a small real-user study, per-method NoC increases nonuniformly (methods tuned on the simulator degrade most), changing at least some benchmark rankings; simulated clicks have measurably higher information gain per click than human clicks.
- **Why Important:** If rankings flip, years of interactive-segmentation comparisons are partially artifacts of the evaluation policy.
- **Why Possibly Novel:** Human studies exist for usability, but an information-theoretic comparison of click policies tied to method ranking stability is new.
- **Minimal Experiment:** Collect ~20 users × 50 images of real click sequences on a web tool; replay against 4 public interactive models; compare NoC rankings vs simulator rankings; compute per-click entropy reduction for both policies.
- **Main Risk:** Small user studies are noisy; power analysis needed on ranking-flip detection.
- **Research Cluster:** NEG

### IDEA-C-0014 — Adapter gains in domain shift are mostly normalization-statistics gains
- **One-sentence idea:** Test whether a large fraction of reported adapter/PEFT gains under domain shift is reproduced by updating only normalization statistics/affine parameters, implying many adapter papers re-discover BN/LN adaptation.
- **Problem:** New adapter modules for domain shift are published continuously without a normalization-only control.
- **Core Hypothesis (falsifiable):** Across several published adapter setups for shifted dense prediction, norm-only tuning recovers a large, consistent share of the adapter's gain over frozen baseline, and adapters constrained to leave normalization untouched lose most of their advantage.
- **Why Important:** Establishes the missing control experiment and deflates fake novelty in the adaptation literature.
- **Why Possibly Novel:** Norm-tuning is known to be strong, but a systematic decomposition attributing published adapter gains to the normalization channel is not standard practice.
- **Minimal Experiment:** Reimplement 3 representative adapter methods on GTA→Cityscapes and natural→medical transfer; run norm-only, adapter-only, adapter-minus-norm arms; report gain decomposition.
- **Main Risk:** Fraction may vary widely by shift type, complicating a single headline number — which is itself a useful finding.
- **Research Cluster:** NEG

### IDEA-C-0015 — CLIP patch tokens encode object context, making "stuff" unsegmentable
- **One-sentence idea:** Mechanistically test whether CLIP-based dense predictors fail on stuff classes (road, sky, water) because patch tokens are contaminated by object-centric context aggregation from pretraining.
- **Problem:** Open-vocab segmenters underperform on stuff vs things, usually blamed on vocabulary, not representation geometry.
- **Core Hypothesis (falsifiable):** Patch-token probes for stuff classes degrade sharply when surrounding objects are shuffled/replaced (context-swap test), while things-class probes do not; a DINO-style objective on identical data shows much weaker context contamination.
- **Why Important:** Points to the pretraining objective (caption alignment) as the cause, redirecting fixes from decoders to objectives.
- **Why Possibly Novel:** Things-vs-stuff gaps are reported; a causal context-swap methodology attributing them to token contamination is new.
- **Minimal Experiment:** Build context-swapped composites (same stuff region, different surrounding objects) via copy-paste; measure per-patch CLIP feature drift and probe accuracy vs DINOv2 under identical swaps.
- **Main Risk:** Copy-paste artifacts themselves perturb features; needs blur/harmonization controls.
- **Research Cluster:** NEG

### IDEA-C-0016 — Attention collision: scaling does not fix many-similar-instance separation
- **One-sentence idea:** Test whether instance separation among many visually identical objects (bolts on a tray, cells, penguins) fails to improve with model scale because self-attention averages identical tokens ("collision"), an architectural rather than capacity limit.
- **Problem:** Dense instance tasks in industry involve hundreds of identical items; scaling reports never stratify by instance multiplicity.
- **Core Hypothesis (falsifiable):** Instance-segmentation quality vs number-of-identical-instances curves are flat across model scales beyond a small multiplicity, while heterogeneous-instance curves improve with scale; token similarity analysis shows near-duplicate keys causing attention averaging.
- **Why Important:** Identifies a structural failure mode with a testable mechanism, motivating position-diversified attention or iterative grouping rather than scale.
- **Why Possibly Novel:** Attention collision is discussed theoretically; connecting it to a multiplicity-stratified empirical scaling flatline in segmentation is new.
- **Minimal Experiment:** Synthetic scenes with k identical sprites (k=2…200) plus real cell/crowd data; evaluate Mask2Former/SAM-everything across scales; plot quality vs k per scale; measure key-vector collision rates.
- **Main Risk:** Query-based decoders may partially mitigate collisions, requiring per-architecture analysis.
- **Research Cluster:** NEG

### IDEA-C-0017 — A predictable shot-count threshold where fine-tuning starts beating linear probes
- **One-sentence idea:** Establish that below a critical number of labeled examples, fine-tuning a VFM (even with PEFT) underperforms a frozen linear probe due to feature drift, and that this threshold is predictable from a cheap curvature/Fisher estimate.
- **Problem:** Practitioners choose probe-vs-tune by folklore; the crossover is task-dependent and never predicted a priori.
- **Core Hypothesis (falsifiable):** The probe-vs-tune crossover shot count N* correlates strongly (rank correlation > 0.8 across ≥10 tasks) with a one-batch estimate of loss curvature in feature space, allowing prediction of N* without training.
- **Why Important:** Converts an expensive hyper-decision into a one-batch measurement; also maps when PEFT is actively harmful.
- **Why Possibly Novel:** Probe-vs-tune comparisons exist; a predictive, pre-training-free estimator of the crossover for dense tasks does not.
- **Minimal Experiment:** For 10 segmentation tasks × shot counts {5..500}, train probes and LoRA-tunes; locate N*; regress against cheap estimators (feature-space class separation, gradient variance, curvature) computed from one forward/backward pass.
- **Main Risk:** N* may be noisy at small shots; needs multiple seeds and a robust crossover definition.
- **Research Cluster:** NEG

### IDEA-C-0018 — The perceptual ceiling: leaderboard deltas smaller than human-visible differences
- **One-sentence idea:** Measure the mask-quality difference threshold below which human experts cannot distinguish two models' outputs, and show that a substantial share of recent leaderboard improvements falls below this perceptual ceiling.
- **Problem:** Dense-prediction leaderboards celebrate sub-point gains whose real-world meaning is unknown.
- **Core Hypothesis (falsifiable):** In two-alternative forced-choice trials, expert raters cannot distinguish model pairs whose boundary-F differs by less than a measurable threshold δ, and ≥ half of the last N leaderboard improvements on a popular benchmark are < δ.
- **Why Important:** Provides an evidence-based significance floor for the field's progress claims.
- **Why Possibly Novel:** Human-perception studies of metric deltas exist for image quality (JND) but not for segmentation leaderboard increments.
- **Minimal Experiment:** Sample output pairs from public checkpoints at controlled metric gaps; run 2AFC with ~15 raters; fit a psychometric curve; overlay historical leaderboard deltas.
- **Main Risk:** Perceptual indistinguishability doesn't imply downstream-task equivalence; scope claims carefully.
- **Research Cluster:** NEG

### IDEA-C-0019 — Sequentially trained adapters do not compose
- **One-sentence idea:** Test whether a domain adapter and a task adapter trained separately on the same frozen VFM interfere destructively when stacked, and identify the layer ranges where interference concentrates.
- **Problem:** The modular dream (one adapter per domain, one per task, compose freely) underlies many systems but lacks falsification.
- **Core Hypothesis (falsifiable):** Stacked independently-trained adapters underperform jointly-trained ones by a gap that grows with the subspace overlap of their weight updates, and forcing orthogonal update subspaces during training eliminates most of the gap.
- **Why Important:** Either kills or rescues the composable-adapter paradigm with a concrete mechanism (subspace overlap).
- **Why Possibly Novel:** Adapter fusion is studied in NLP for merging, but a subspace-overlap causal account of dense-prediction composition failure is untested.
- **Minimal Experiment:** Train domain adapter (clean→corrupted) and task adapter (classes A→B) separately on frozen DINOv2; evaluate stacked vs joint; measure principal-angle overlap of update subspaces; retrain with orthogonality penalty.
- **Main Risk:** Interference could be dominated by normalization interactions rather than subspaces; include norm-frozen controls.
- **Research Cluster:** NEG

### IDEA-C-0020 — Grid-prompt aliasing: SAM "everything mode" has a Nyquist blind spot
- **One-sentence idea:** Show that automatic mask generation with regular grid prompts systematically misses objects whose size/spacing falls near the grid's aliasing frequencies, a sampling-theory failure invisible in aggregate recall.
- **Problem:** Everything-mode recall is treated as an intrinsic model property when it is partly a property of the prompt sampling lattice.
- **Core Hypothesis (falsifiable):** Object recall as a function of object diameter shows periodic dips at predictable fractions of the grid pitch, and jittered/blue-noise prompt sampling at equal budget removes the dips.
- **Why Important:** A free (zero-training) recall improvement and a clean demonstration that evaluation artifacts masquerade as model limits.
- **Why Possibly Novel:** Grid density ablations exist; a sampling-theoretic analysis with predicted dip locations and a blue-noise fix appears new.
- **Minimal Experiment:** Synthetic scenes with objects at swept diameters/spacings; run everything-mode at fixed grid pitch; plot recall vs diameter; repeat with jittered sampling; confirm on LVIS small-object subset.
- **Main Risk:** Non-maximum suppression stages may mask or mimic aliasing dips; instrument each pipeline stage.
- **Research Cluster:** NEG

### IDEA-C-0021 — Preference-tuned segmentation drifts toward plausible-but-wrong smoothness
- **One-sentence idea:** Test whether optimizing segmentation models on human preference feedback (which mask looks better) degrades geometric fidelity because raters prefer smooth, closed, convex-ish masks over accurate ragged ones.
- **Problem:** Preference/RLHF-style tuning is arriving in vision; its objective misalignment with geometric ground truth is unquantified.
- **Core Hypothesis (falsifiable):** A reward model trained on pairwise mask preferences assigns higher reward to smoothed ground truth than to true ground truth for objects above a measurable boundary-roughness threshold, and preference-tuned models show corresponding IoU drops concentrated on rough-boundary classes.
- **Why Important:** Predicts a systematic bias before the community adopts preference tuning for dense tasks.
- **Why Possibly Novel:** Reward hacking is known in text; a geometric characterization (roughness threshold) for masks is new.
- **Minimal Experiment:** Collect ~5k pairwise preferences on (true mask vs morphologically smoothed mask) pairs; fit a reward model; measure where smoothed beats true as a function of roughness; fine-tune briefly against the reward and audit IoU by class roughness.
- **Main Risk:** Rater instructions strongly modulate the bias; report under multiple instruction framings.
- **Research Cluster:** NEG

### IDEA-C-0022 — Prompt-ensemble gains in open-vocab segmentation are calibration, not knowledge
- **One-sentence idea:** Decompose the standard 80-template CLIP prompt-ensembling gain for dense prediction into (a) logit calibration/variance reduction and (b) genuine semantic coverage, testing whether a single temperature-matched template recovers almost all of it.
- **Problem:** Prompt ensembles are universally used and interpreted as adding semantic robustness, at 80x text-encoder cost.
- **Core Hypothesis (falsifiable):** Per-class logit rescaling (fit on a tiny calibration set) with one template matches ensemble mIoU within noise on most datasets; residual ensemble gains concentrate in polysemous class names only.
- **Why Important:** Either eliminates a costly ritual or precisely localizes where ensembling truly adds information.
- **Why Possibly Novel:** Ensembling ablations exist for classification; the calibration-vs-coverage decomposition for dense prediction with polysemy stratification is untested.
- **Minimal Experiment:** On 3 open-vocab segmentation setups, compare single-template, single-template+per-class scaling, and full ensemble; stratify residuals by class-name polysemy (WordNet sense count).
- **Main Risk:** Some pipelines fuse templates nonlinearly; restrict to standard mean-embedding ensembling for clean attribution.
- **Research Cluster:** NEG

### IDEA-C-0023 — Boundary memorization in long fine-tunes of small dense datasets
- **One-sentence idea:** Test whether fine-tuning VFMs past interpolation on small segmentation datasets causes verbatim memorization of annotation boundary idiosyncrasies, detectable as excess agreement with annotator-specific error patterns.
- **Problem:** Small-data fine-tuning is standard in medical/industrial practice; memorization is studied for labels, not boundary geometry.
- **Core Hypothesis (falsifiable):** After long fine-tuning, model boundaries correlate with individual annotator error residuals (vs consensus) significantly above chance on training images, and this correlation predicts generalization drop on re-annotated test data.
- **Why Important:** Gives a concrete overfitting diagnostic for dense tasks that val-mIoU misses (val labels share the same annotator biases).
- **Why Possibly Novel:** Label memorization literature is classification-centric; annotator-residual correlation as a dense memorization probe is new.
- **Minimal Experiment:** Use a dataset with multi-annotator masks (e.g., LIDC); train on single-annotator labels for long schedules; measure agreement with that annotator's residuals vs consensus over epochs; correlate with consensus-test performance.
- **Main Risk:** Requires multi-annotator data; few public options outside medical imaging.
- **Research Cluster:** NEG

### IDEA-C-0024 — Synthetic data helps detection but hurts segmentation of the same classes
- **One-sentence idea:** Test the dissociation that rendered synthetic data improves object detection while degrading segmentation boundary quality for the same classes, because rendered boundary statistics (anti-aliasing, no motion blur, perfect alpha) mismatch real boundary statistics.
- **Problem:** Synthetic data is added wholesale; task-dependent sign flips would change how it's used.
- **Core Hypothesis (falsifiable):** Mixing rendered data improves box AP but reduces boundary-F on real test sets, with the segmentation harm proportional to the divergence between synthetic and real boundary-gradient-profile histograms; matching boundary statistics via post-hoc degradation removes the harm.
- **Why Important:** Provides a measurable pre-flight check (boundary statistic divergence) for synthetic data value per task.
- **Why Possibly Novel:** Sim2real gaps are studied globally; a boundary-microstatistics account predicting a detection/segmentation sign flip is new.
- **Minimal Experiment:** Mix varying fractions of a rendered dataset into COCO-subset training for a shared backbone with det+seg heads; track AP vs boundary-F; measure boundary gradient histograms; add synthetic boundary degradation and re-test.
- **Main Risk:** Renderer-specific; use two rendering sources to check generality.
- **Research Cluster:** NEG

### IDEA-C-0025 — Video-pretrained VFMs trade spatial acuity for temporal priors
- **One-sentence idea:** Test whether video-pretrained encoders, evaluated frame-wise, systematically underperform image-pretrained encoders of equal scale on fine spatial tasks (boundaries, thin structures), quantifying a spatial-temporal representation tradeoff.
- **Problem:** Video foundation models are assumed to subsume image capabilities; a controlled acuity comparison is missing.
- **Core Hypothesis (falsifiable):** At matched parameter count and data scale, video-pretrained models show lower single-frame boundary-F and thin-structure probes, with the deficit proportional to the temporal downsampling/tubelet size used in pretraining.
- **Why Important:** Informs whether the field should expect one universal encoder or task-specialized ones, with a concrete architectural knob (tubelet size).
- **Why Possibly Novel:** Video-vs-image comparisons focus on video tasks; the reverse direction (spatial cost of temporal pretraining) is rarely quantified.
- **Minimal Experiment:** Linear-probe frozen VideoMAE-style vs MAE-style encoders (matched size) on boundary-heavy segmentation; stratify by structure width; correlate deficit with tubelet configuration across available checkpoints.
- **Main Risk:** Perfectly matched checkpoint pairs are scarce; may require small-scale controlled pretraining runs.
- **Research Cluster:** NEG

### IDEA-C-0026 — Language-encoder scaling stops helping grounding once spatial pooling saturates
- **One-sentence idea:** Test whether scaling the text encoder in VLM dense predictors yields no grounding improvement beyond a threshold because the visual-side spatial pooling is the information bottleneck.
- **Problem:** Compute is allocated to bigger text towers on the assumption that better language understanding improves dense grounding.
- **Core Hypothesis (falsifiable):** Holding the vision tower fixed, referring-segmentation accuracy vs text-encoder scale saturates early, while holding text fixed and increasing visual token resolution keeps improving; mutual-information estimates localize the bottleneck at the pooling interface.
- **Why Important:** Directly reallocates compute in VLM design for dense tasks.
- **Why Possibly Novel:** Tower-scaling ablations exist for retrieval/classification; a bottleneck-localization study for dense grounding is missing.
- **Minimal Experiment:** Pair frozen vision towers with text encoders of 4 sizes (and vice versa) in a light referring-segmentation head trained identically; plot both scaling curves; estimate information transmitted through the pooling layer.
- **Main Risk:** Head capacity could confound; keep heads tiny and identical.
- **Research Cluster:** NEG

### IDEA-C-0027 — Negative clicks are second-class citizens in SAM's decoder
- **One-sentence idea:** Quantify the asymmetry between positive and negative point prompts in SAM-family decoders, testing whether negative points causally remove far less probability mass than positive points add, due to how prompt tokens are attended.
- **Problem:** Interactive correction workflows rely on negative clicks that anecdotally "don't work"; no mechanistic account exists.
- **Core Hypothesis (falsifiable):** Matched-perturbation experiments show the per-click mask change (in symmetric-difference area) for negative clicks is a small fraction of positive clicks at equal geodesic distance from the boundary, and attention maps show negative tokens receive systematically lower attention weight from mask tokens.
- **Why Important:** Explains a pervasive UX failure and motivates retraining with click-type-balanced simulated interaction.
- **Why Possibly Novel:** Click ablations exist; a controlled symmetry analysis with attention-level mechanism and a retraining fix is new.
- **Minimal Experiment:** For 1k images, apply single positive vs negative clicks at matched positions relative to the current boundary; measure mask deltas; extract decoder attention to prompt tokens; fine-tune decoder with balanced click curricula and re-measure.
- **Main Risk:** Asymmetry may be partially task-appropriate (background is bigger); normalize by achievable correction.
- **Research Cluster:** NEG

### IDEA-C-0028 — Classification-tuned augmentation policies actively hurt VFM segmentation fine-tuning
- **One-sentence idea:** Test whether RandAugment-style policies inherited from classification degrade segmentation fine-tuning because coupled photometric+geometric ops create label-geometry inconsistency at boundaries (interpolation, occlusion-order changes).
- **Problem:** Augmentation defaults are copied across tasks without dense-task validation; nobody checks per-op boundary effects.
- **Core Hypothesis (falsifiable):** Per-operation ablation shows a consistent subset of ops (e.g., shear+posterize combinations, aggressive translate with fill) reduce boundary-F despite improving interior robustness, and a dense-task-audited policy beats RandAugment across three datasets.
- **Why Important:** Free accuracy from fixing defaults, and a reusable per-op boundary-harm audit methodology.
- **Why Possibly Novel:** Segmentation-specific augmentation papers exist, but a systematic boundary-harm attribution of the standard classification policies does not.
- **Minimal Experiment:** Fine-tune SAM/DINOv2 heads on VOC with per-op leave-one-out RandAugment variants; report interior-IoU vs boundary-F per op; assemble and validate a filtered policy.
- **Main Risk:** Effects may be small and dataset-dependent; needs many seeds for tight confidence intervals.
- **Research Cluster:** NEG

### IDEA-C-0029 — Model soups fail for dense prediction because decoder heads don't align
- **One-sentence idea:** Test whether weight averaging of independently fine-tuned dense predictors fails (unlike classification) because mask-decoder query/channel permutations create loss barriers, and whether alignment-then-soup restores the benefit.
- **Problem:** Soups are a free-lunch trick in classification; dense practitioners report it silently failing, without diagnosis.
- **Core Hypothesis (falsifiable):** Linear interpolation between two same-init fine-tuned segmentation models shows a loss barrier concentrated in decoder parameters (per-layer barrier decomposition), and permutation/feature alignment of decoder queries before averaging recovers most of the soup gain seen in classification.
- **Why Important:** Rescues a cheap ensembling technique for dense tasks and localizes why it fails.
- **Why Possibly Novel:** Mode connectivity and re-basin are studied for classifiers; a decoder-localized barrier analysis for segmentation soups is new.
- **Minimal Experiment:** Fine-tune 4 seeds of a ViT+Mask2Former on VOC; interpolate pairwise; decompose barrier by parameter group; apply query-matching (Hungarian on query similarity) and re-interpolate.
- **Main Risk:** Barriers may also live in cross-attention with no clean permutation structure.
- **Research Cluster:** NEG

### IDEA-C-0030 — Continual SAM fine-tuning causes prompt-semantics drift without accuracy loss
- **One-sentence idea:** Show that sequentially fine-tuning SAM across datasets preserves per-dataset mask accuracy while silently changing what prompts mean (click-to-mask mapping drifts), breaking downstream tools that assume stable prompt semantics.
- **Problem:** Accuracy-centric continual learning metrics miss interface-contract violations in promptable models.
- **Core Hypothesis (falsifiable):** After a 5-dataset sequential fine-tune, the same click on held-out images yields masks whose expected granularity (part vs whole) shifts measurably relative to the original model, even where IoU against flexible ground truth is unchanged.
- **Why Important:** Defines "prompt-contract stability" as a new continual-learning axis essential for deployed interactive systems.
- **Why Possibly Novel:** Continual segmentation work tracks forgetting of classes; drift of the prompting interface itself is unstudied.
- **Minimal Experiment:** Sequentially fine-tune SAM on 5 public datasets; on a fixed probe set, record mask-granularity distribution (relative area, hierarchy level) per click before/after; quantify drift and its correlation with dataset order.
- **Main Risk:** Granularity ground truth requires hierarchical annotations; use existing part-whole datasets (PACO/PartImageNet).
- **Research Cluster:** NEG
## Cluster CONF — Hidden Benchmark Confounders (IDEA-C-0031 … IDEA-C-0060)

### IDEA-C-0031 — Center bias makes interactive benchmarks solvable by position alone
- **One-sentence idea:** Quantify how much of interactive/salient segmentation benchmark performance is explained by object centering, by evaluating models on translation-decentered versions of the same images.
- **Problem:** Photographer framing centers objects; models may exploit positional priors that fail in robotic/surveillance viewpoints.
- **Core Hypothesis (falsifiable):** A position-only predictor (no image content) achieves nontrivial IoU on standard benchmarks; model rankings change measurably when objects are decentered via crop-shifting, and the models that drop most have the strongest learned positional priors (probe-detectable).
- **Why Important:** Reveals that leaderboard gaps partly measure prior exploitation, not perception, affecting deployment predictions.
- **Why Possibly Novel:** Center bias is folklore in saliency; a decentring re-evaluation tied to ranking stability for modern promptable models is missing.
- **Minimal Experiment:** Build decentered variants of DAVIS/DUTS/COCO subsets by asymmetric cropping with content preserved; evaluate 6 public models before/after; train a coordinates-only baseline for reference.
- **Main Risk:** Cropping changes context and resolution; control with equal-area random crops that keep objects centered.
- **Research Cluster:** CONF

### IDEA-C-0032 — Polygon vertex budgets leave a learnable fingerprint in COCO masks
- **One-sentence idea:** Test whether models trained on COCO learn the piecewise-linear geometry of low-vertex polygon annotations, and are then unfairly penalized on benchmarks with dense (curved) annotations — and vice versa.
- **Problem:** Cross-dataset mask evaluation conflates model quality with annotation-geometry style transfer.
- **Core Hypothesis (falsifiable):** COCO-trained models produce measurably straighter boundary segments (lower curvature entropy) than models trained on high-vertex datasets (LVIS re-annotations, ADE fine); a style-transfer correction (contour smoothing/densification) closes a predictable share of the cross-dataset gap.
- **Why Important:** Separates real generalization gaps from annotation-style gaps in every cross-dataset comparison.
- **Why Possibly Novel:** Annotation quality is discussed; a quantitative "vertex-budget fingerprint" carried by models and correctable post-hoc is new.
- **Minimal Experiment:** Measure boundary curvature statistics of predictions from COCO-trained vs LVIS-trained models on identical images; apply contour resampling corrections; re-evaluate cross-dataset boundary-F.
- **Main Risk:** Curvature differences may reflect architecture too; hold architecture fixed across training sets.
- **Research Cluster:** CONF

### IDEA-C-0033 — Scanner fingerprints as train/test leakage detectors in medical benchmarks
- **One-sentence idea:** Use a scanner/institution-fingerprint classifier to audit how much popular medical segmentation benchmarks leak acquisition identity across train/test, and re-estimate method gaps under fingerprint-stratified splits.
- **Problem:** Random splits of multi-scanner data let models exploit shared acquisition signatures, inflating apparent generalization.
- **Core Hypothesis (falsifiable):** A lightweight classifier can identify scanner/site from image patches at high accuracy on several public benchmarks; re-splitting by fingerprint reduces reported SOTA gaps and reorders at least some methods.
- **Why Important:** Provides an automatic leakage audit usable on any medical benchmark, including those without site metadata.
- **Why Possibly Novel:** Site effects are known; an automated fingerprint-based audit tool with ranking-impact quantification across benchmarks is not standard.
- **Minimal Experiment:** Train a small CNN to predict site/scanner (where metadata exists) on BraTS/AMOS; verify fingerprint accuracy; cluster fingerprints where metadata is absent; re-evaluate 5 published methods under fingerprint-blocked splits.
- **Main Risk:** Fingerprint clusters may correlate with genuine population differences; report both interpretations.
- **Research Cluster:** CONF

### IDEA-C-0034 — Few-shot segmentation episodes leak scene statistics between support and query
- **One-sentence idea:** Audit PASCAL-5i/COCO-20i episode construction for photographer/scene-level correlation between support and query images that lets models match backgrounds rather than learn the class.
- **Problem:** FSS benchmarks sample support/query from the same dataset distribution, possibly the same scenes/photographers, inflating "few-shot learning" claims.
- **Core Hypothesis (falsifiable):** Episodes where support and query share high scene-embedding similarity show substantially higher FSS accuracy; restricting evaluation to scene-dissimilar episodes drops all methods and shrinks method gaps.
- **Why Important:** Redefines what FSS benchmarks measure and provides a stratified protocol.
- **Why Possibly Novel:** Class-information leakage via backgrounds is occasionally noted; a scene-similarity-stratified re-evaluation with ranking impact is not.
- **Minimal Experiment:** Compute scene embeddings (Places-CNN) for all support-query pairs in standard episodes; bin episodes by similarity; re-report 5 published FSS methods per bin.
- **Main Risk:** Scene similarity partially reflects legitimate class-context association; disentangle by background-swap controls.
- **Research Cluster:** CONF

### IDEA-C-0035 — Pretraining contamination in "unseen class" zero-shot benchmarks
- **One-sentence idea:** Quantify how much zero-shot segmentation benchmarks' "unseen" classes are effectively seen in VFM pretraining data, using memorization probes rather than name matching.
- **Problem:** Zero-shot claims rest on class exclusion from fine-tuning data while pretraining corpora (LAION, SA-1B) almost certainly contain the classes.
- **Core Hypothesis (falsifiable):** Behavioral memorization probes (canonical-instance recognition, prototype-recall tests) show high familiarity for most "unseen" classes, and zero-shot accuracy per class correlates more with pretraining familiarity than with visual similarity to seen classes.
- **Why Important:** Reframes zero-shot benchmarks as measuring pretraining recall, not compositional generalization, and motivates truly novel-class test sets (new products, synthetic species).
- **Why Possibly Novel:** Contamination analysis exists for LLM benchmarks; a behavioral (non-string-matching) contamination methodology for dense vision benchmarks is new.
- **Minimal Experiment:** For each "unseen" class, build familiarity scores from frozen-VFM retrieval density and name-free prototype probes; regress per-class zero-shot IoU on familiarity vs semantic-similarity covariates.
- **Main Risk:** Familiarity metrics are proxies; triangulate with several independent probes.
- **Research Cluster:** CONF

### IDEA-C-0036 — Class-correlated JPEG compression as a shortcut feature in web-scraped benchmarks
- **One-sentence idea:** Audit whether compression level/chroma-subsampling correlates with class identity in popular web-scraped datasets and whether dense models exploit it.
- **Problem:** Classes scraped from different site types (news vs e-commerce vs forums) carry different compression pipelines, creating a non-semantic shortcut.
- **Core Hypothesis (falsifiable):** Compression parameters predicted from images correlate with class labels above chance in at least some benchmark classes, and re-compressing all images to uniform quality changes per-class accuracy in proportion to the original correlation.
- **Why Important:** Identifies an invisible, easily-fixable confounder affecting both training and evaluation of open-vocab models.
- **Why Possibly Novel:** Compression shortcuts are shown for forensics/deepfakes; a benchmark-audit connecting compression-class correlation to dense-prediction accuracy shifts is new.
- **Minimal Experiment:** Estimate quantization tables/quality per image on ADE20K/OpenImages subsets; test class-compression association; re-encode uniformly and re-evaluate frozen open-vocab segmenters per class.
- **Main Risk:** Re-encoding removes genuine high-frequency information; use matched-quality controls.
- **Research Cluster:** CONF

### IDEA-C-0037 — Rectification and ego-vehicle artifacts give Cityscapes models spatial cheat codes
- **One-sentence idea:** Quantify how much Cityscapes-family performance is explained by fixed camera geometry (hood position, rectification vignetting, horizon line) by evaluating with geometry randomization.
- **Problem:** Driving benchmarks share a rigid camera setup; "generalization" numbers partly measure geometry memorization.
- **Core Hypothesis (falsifiable):** A row-index-only classifier achieves high per-class accuracy for several classes; augmenting evaluation with horizon shifts and crop jitter drops methods nonuniformly, reordering some; models with explicit positional encodings drop most.
- **Why Important:** Explains part of the notorious Cityscapes→other-city transfer gap as geometry overfitting, separate from appearance shift.
- **Why Possibly Novel:** Spatial priors in driving data are known informally; a ranking-impact quantification with positional-encoding attribution is not.
- **Minimal Experiment:** Train row-only and (row, column)-only baselines; evaluate 6 public models under vertical crop shifts of ±15%; correlate degradation with positional-prior probe strength.
- **Main Risk:** Crop shifts alter class distributions (more sky/road); reweight metrics accordingly.
- **Research Cluster:** CONF

### IDEA-C-0038 — First-frame annotation quality drives video object segmentation rankings
- **One-sentence idea:** Test whether semi-supervised VOS benchmark rankings are dominated by robustness to first-frame mask imperfections rather than temporal propagation ability.
- **Problem:** VOS methods are compared assuming a perfect first-frame mask, but their sensitivity to realistic initialization noise differs and is never reported.
- **Core Hypothesis (falsifiable):** Injecting realistic annotation noise (boundary jitter, small holes) into first-frame masks changes DAVIS/YouTube-VOS rankings measurably, and per-method degradation is uncorrelated with clean-init performance.
- **Why Important:** Real deployments never have perfect initialization; adds a required robustness axis to VOS evaluation.
- **Why Possibly Novel:** Initialization-robustness sweeps with ranking-impact analysis are not part of standard VOS protocols.
- **Minimal Experiment:** Perturb first-frame masks with calibrated noise models (fit from inter-annotator data); re-evaluate 6 public VOS models; report rank correlation between clean and noisy leaderboards.
- **Main Risk:** Noise model realism; fit it from actual multi-annotator VOS frames.
- **Research Cluster:** CONF

### IDEA-C-0039 — Camouflage benchmarks are biased toward found animals
- **One-sentence idea:** Quantify the selection bias in camouflaged-object datasets (images kept only when a human spotted the animal), and measure how models trained on them fail on statistically representative camouflage (e.g., trail-camera archives with verified-empty and verified-present frames).
- **Problem:** COD datasets exclude the hardest cases by construction — cases where camouflage worked — biasing both training and evaluation.
- **Core Hypothesis (falsifiable):** On trail-camera data with ground truth from motion/tag verification, COD-trained models show a large recall drop concentrated in images where human annotators also fail, and dataset difficulty distributions differ measurably (detectability scores) between COD benchmarks and representative sources.
- **Why Important:** Selection-on-detectability is a general benchmark pathology (also in defect and lesion datasets); camouflage makes it measurable.
- **Why Possibly Novel:** COD papers acknowledge difficulty but not the selection mechanism; using externally-verified presence data to measure it is new.
- **Minimal Experiment:** Assemble a small verified trail-camera set (public wildlife-monitoring data with tags/motion triggers); run 4 COD models; compare recall vs a human baseline on the same frames; fit a detectability-based selection model to the COD training set.
- **Main Risk:** Trail-camera domain shift confounds with selection bias; include domain-adapted controls.
- **Research Cluster:** CONF

### IDEA-C-0040 — Two valid annotation styles flip boundary-metric rankings
- **One-sentence idea:** Demonstrate that boundary F-score rankings of segmentation methods are contingent on annotation smoothness conventions, by re-annotating a benchmark subset under two documented, equally defensible styles.
- **Problem:** Boundary metrics assume one true boundary; annotation guidelines (tight vs smooth, include-fuzz vs exclude-fuzz) vary and are rarely documented.
- **Core Hypothesis (falsifiable):** On a re-annotated 300-image subset with "tight" vs "perceptual-smooth" styles, at least some method pairs swap order in boundary-F under the two styles, while interior IoU rankings remain stable.
- **Why Important:** Shows boundary-metric leaderboards carry an unacknowledged style dependence, motivating style-conditioned reporting or annotation-style metadata.
- **Why Possibly Novel:** Inter-annotator noise is studied as variance; systematic style as a ranking-flipping factor with a controlled two-style protocol is new.
- **Minimal Experiment:** Re-annotate 300 VOC/ADE images under two written style guides (same annotators, counterbalanced); evaluate 8 public models; report ranking stability per metric.
- **Main Risk:** Annotator consistency within style must be verified with intra-style agreement checks.
- **Research Cluster:** CONF

### IDEA-C-0041 — Scene-context shortcuts in ADE20K measured with a blind-context baseline
- **One-sentence idea:** Quantify per-class how much ADE20K segmentation accuracy is achievable from scene context alone (heavily blurred image + layout), establishing a "context floor" that models should be credited only for exceeding.
- **Problem:** Reported per-class accuracies mix genuine object recognition with scene-layout inference, exaggerating fine-grained capability.
- **Core Hypothesis (falsifiable):** A model trained on strongly low-passed images (objects unrecognizable, layout preserved) reaches a substantial fraction of full-model accuracy for many classes, and the residual (full minus context floor) reorders published methods relative to raw mIoU.
- **Why Important:** Context-floor-corrected metrics measure what dense models actually add beyond scene priors.
- **Why Possibly Novel:** Context effects are studied qualitatively; a per-class context-floor metric integrated into benchmark reporting is new.
- **Minimal Experiment:** Train identical architecture on σ-swept Gaussian-blurred ADE20K; find the blur level erasing object identity (verified by human/classifier tests); report context floors and residual rankings for 6 methods.
- **Main Risk:** Blur choice is contestable; triangulate with patch-shuffle and texture-scramble variants.
- **Research Cluster:** CONF

### IDEA-C-0042 — Much of medical leaderboard progress lies inside the inter-rater noise floor
- **One-sentence idea:** Systematically compare year-over-year Dice improvements on popular medical segmentation challenges against measured inter-rater variability, quantifying the fraction of "progress" that is statistically indistinguishable from annotation noise.
- **Problem:** Challenge leaderboards report Dice to 4 digits; annotation noise floors are known but never overlaid on progress curves.
- **Core Hypothesis (falsifiable):** For several structures (e.g., small lesions, prostate zones), the majority of leaderboard deltas over recent years fall within the 95% interval implied by inter-rater Dice, whereas large-organ deltas mostly exceed it.
- **Why Important:** Recalibrates the field's sense of progress and prioritizes annotation improvements over model improvements where noise dominates.
- **Why Possibly Novel:** Inter-rater studies and leaderboards both exist; joining them into a noise-floor-adjusted progress analysis across challenges is new.
- **Minimal Experiment:** Collect published inter-rater Dice for 6 structures; bootstrap the implied ranking-noise on each challenge's test size; overlay historical leaderboard trajectories; report the within-noise fraction.
- **Main Risk:** Inter-rater estimates come from different populations than test sets; propagate this uncertainty explicitly.
- **Research Cluster:** CONF

### IDEA-C-0043 — Spatial autocorrelation leakage in remote-sensing tile splits
- **One-sentence idea:** Audit popular remote-sensing segmentation benchmarks for train/test tiles that are spatially adjacent or overlapping, and re-estimate method performance under autocorrelation-controlled (buffered) splits.
- **Problem:** Random tile splits from contiguous rasters let models memorize local texture/geography, inflating scores in a way ranking consumers cannot see.
- **Core Hypothesis (falsifiable):** Reported accuracies drop substantially under buffered splits (minimum geographic distance between train and test), the drop varies by method (bigger for high-capacity models), and some rankings change.
- **Why Important:** Provides corrected baselines for a whole application field and a reusable split-auditing tool.
- **Why Possibly Novel:** Spatial CV is standard in geostatistics; its systematic application to deep segmentation benchmarks with ranking-impact reporting remains rare.
- **Minimal Experiment:** Reconstruct tile geolocations for iSAID/LoveDA-style benchmarks; compute train-test nearest distances; retrain 4 methods under buffered splits at swept buffer radii; plot accuracy vs buffer.
- **Main Risk:** Some datasets hide geolocation; use image-matching to reconstruct adjacency.
- **Research Cluster:** CONF

### IDEA-C-0044 — Pixel-Dice on thin-structure datasets is decided by a few thick segments
- **One-sentence idea:** Show that vessel/crack benchmark rankings computed with pixel Dice are dominated by the thickest few percent of structure pixels, and that width-decomposed metrics reorder methods.
- **Problem:** Thin-structure datasets exist to test fine perception, but the standard metric re-weights them toward coarse perception.
- **Core Hypothesis (falsifiable):** Removing the thickest width-decile pixels from scoring changes Dice-based rankings of published vessel-segmentation methods; a width-balanced metric correlates better with clinically-relevant topology metrics (connectivity, missed branches).
- **Why Important:** Aligns thin-structure evaluation with its purpose, likely changing which methods are considered SOTA.
- **Why Possibly Novel:** Alternative metrics (clDice) exist; a width-stratified audit quantifying how much current rankings are thick-pixel artifacts is the missing empirical piece.
- **Minimal Experiment:** On DRIVE/STARE/CrackSeg, compute skeleton-distance-based width maps; re-score 8 published outputs per width decile; compare rankings under pixel-Dice, width-balanced Dice, and clDice.
- **Main Risk:** Public prediction files may be unavailable; retrain reference implementations.
- **Research Cluster:** CONF

### IDEA-C-0045 — Class-name web frequency predicts open-vocab per-class IoU
- **One-sentence idea:** Test whether per-class open-vocabulary segmentation accuracy is largely predicted by the class name's frequency in web caption corpora, making benchmarks partly a vocabulary-frequency measurement.
- **Problem:** Open-vocab benchmarks interpret per-class differences as visual difficulty; caption-frequency confounding is unquantified.
- **Core Hypothesis (falsifiable):** Log caption-corpus frequency of class names explains a large share of per-class IoU variance across open-vocab methods, and matching classes on frequency eliminates most cross-benchmark "difficulty" differences.
- **Why Important:** Enables frequency-controlled evaluation, separating visual grounding capability from vocabulary coverage.
- **Why Possibly Novel:** Frequency effects are studied for classification zero-shot; dense-prediction benchmarks have not been frequency-audited.
- **Minimal Experiment:** Count class-name frequencies in a public caption corpus (LAION metadata); regress per-class IoU of 5 open-vocab methods on frequency plus visual covariates (size, texture); report partial R².
- **Main Risk:** Frequency correlates with real-world commonness (also affecting visual data); use synonym pairs with different frequencies as a control.
- **Research Cluster:** CONF

### IDEA-C-0046 — NoC metrics conflate model quality with simulator determinism
- **One-sentence idea:** Show that Number-of-Clicks benchmark results depend heavily on the click simulator's tie-breaking and determinism, and propose reporting NoC distributions under stochastic simulators as the fix.
- **Problem:** Deterministic simulators pick one trajectory through a branching interaction process; models are effectively tuned to that trajectory.
- **Core Hypothesis (falsifiable):** Randomizing click positions within the valid error region (instead of max-distance points) changes mean NoC nonuniformly across methods and flips at least some published comparisons; per-method NoC variance under stochastic clicking is itself informative and uncorrelated with deterministic NoC.
- **Why Important:** A one-line evaluation change that makes interactive benchmarks meaningful for real users.
- **Why Possibly Novel:** Simulator design papers exist; a ranking-stability analysis under simulator stochasticity is not standard.
- **Minimal Experiment:** Re-evaluate 6 interactive models on GrabCut/Berkeley/DAVIS with 20 stochastic simulator seeds; report NoC distributions and rank stability.
- **Main Risk:** None substantial — this is cheap; the risk is that rankings are stable, which is itself a publishable robustness result.
- **Research Cluster:** CONF

### IDEA-C-0047 — Part of the synthetic-to-real "domain gap" is a label-noise gap
- **One-sentence idea:** Decompose GTA→Cityscapes-style adaptation gaps into appearance shift vs label-quality shift, exploiting that synthetic labels are pixel-perfect while real labels are noisy.
- **Problem:** UDA methods are credited for closing an "appearance gap" that partly consists of the model being evaluated against noisy real labels after training on perfect ones.
- **Core Hypothesis (falsifiable):** Injecting calibrated Cityscapes-style label noise into GTA training labels closes a measurable fraction of the sim2real gap on its own, and correcting Cityscapes test labels (high-quality re-annotation subset) shrinks the measured gap for all methods.
- **Why Important:** Changes how much headroom actually exists for UDA research and how gains should be attributed.
- **Why Possibly Novel:** Label noise and domain gap literatures are disjoint; their decomposition on the field's flagship benchmark is unperformed.
- **Minimal Experiment:** Fit a boundary-noise model from Cityscapes coarse-vs-fine annotations; retrain source-only models on noise-injected GTA; evaluate on standard and re-annotated test subsets; report gap decomposition.
- **Main Risk:** Noise model fidelity; validate against held-out fine annotations.
- **Research Cluster:** CONF

### IDEA-C-0048 — Resolution-protocol heterogeneity silently reorders segmentation leaderboards
- **One-sentence idea:** Audit how much of cross-paper performance differences on standard benchmarks comes from inconsistent inference-resolution protocols (resize policy, sliding window, aspect handling) rather than models.
- **Problem:** Papers self-report with heterogeneous inference protocols; readers attribute differences to methods.
- **Core Hypothesis (falsifiable):** Re-running public checkpoints under one standardized protocol changes reported gaps by amounts comparable to typical claimed improvements, and protocol sensitivity varies by architecture family (ViTs vs CNNs) in a predictable direction.
- **Why Important:** Quantifies a reproducibility tax and produces a protocol-standardized re-leaderboard.
- **Why Possibly Novel:** Protocol sensitivity is known anecdotally; a systematic cross-paper audit with variance attribution is missing.
- **Minimal Experiment:** Take 10 public semantic-segmentation checkpoints; evaluate each under 5 common protocols; report per-model protocol variance vs cross-model differences.
- **Main Risk:** None major; mostly engineering care in protocol reproduction.
- **Research Cluster:** CONF

### IDEA-C-0049 — Perceptual-hash audit of near-duplicates across train/eval in VFM evaluation suites
- **One-sentence idea:** Audit widely-used dense-prediction evaluation suites for near-duplicates of images in VFM pretraining corpora, and measure the score inflation attributable to memorized instances.
- **Problem:** Frozen-VFM evaluations assume test images are unseen; web-scale pretraining makes this false in unknown proportion.
- **Core Hypothesis (falsifiable):** A measurable fraction of benchmark images have near-duplicates in accessible pretraining indexes; frozen-VFM performance on duplicated images exceeds non-duplicated matched controls by a significant margin, and the effect grows with model scale.
- **Why Important:** Establishes contamination-corrected numbers for the frozen-backbone evaluation paradigm everyone relies on.
- **Why Possibly Novel:** Duplicate detection exists for classification test sets; dense-prediction suites and scale-dependence of the inflation are unexamined.
- **Minimal Experiment:** Run perceptual-hash + embedding retrieval of ADE20K/VOC val images against LAION indexes; stratify frozen-probe performance by duplication status with matched difficulty controls.
- **Main Risk:** Pretraining corpora for some VFMs are closed; report on open-corpus models and bound the rest.
- **Research Cluster:** CONF

### IDEA-C-0050 — Photographic composition rules are a hidden supervisory signal in saliency data
- **One-sentence idea:** Test whether salient-object models exploit composition regularities (rule of thirds, depth-of-field blur) by evaluating on recomposed images where composition cues are neutralized but objects unchanged.
- **Problem:** Saliency benchmarks inherit photographer intent; models may detect "what photographers frame" not "what is salient."
- **Core Hypothesis (falsifiable):** Neutralizing composition (refocusing blur uniformly, off-thirds recomposition via inpainting-assisted shifts) degrades saliency models substantially more than it degrades human saliency judgments collected on the same recomposed images.
- **Why Important:** Distinguishes perception from photographic-convention detection, relevant wherever saliency feeds cropping/attention systems for non-photographic imagery (medical, industrial).
- **Why Possibly Novel:** Center bias is measured; a full composition-cue neutralization protocol with human controls is new.
- **Minimal Experiment:** Create 500 recomposed images (uniform blur, shifted composition); collect lightweight human saliency clicks; compare model-vs-human degradation ratios for 5 models.
- **Main Risk:** Inpainting artifacts introduce their own cues; use artifact-detection controls.
- **Research Cluster:** CONF

### IDEA-C-0051 — Mask improvements are invisible below the detection bottleneck in AP
- **One-sentence idea:** Quantify how instance-segmentation AP hides mask-quality progress whenever detection quality is the binding constraint, using oracle-box decompositions across a decade of models.
- **Problem:** AP mixes detection and mask quality; the field may be over- or under-investing in mask heads without knowing which stage binds.
- **Core Hypothesis (falsifiable):** With oracle boxes substituted, mask-quality differences between many model generations are much larger than their AP differences suggest (or vice versa), and the binding stage flips at an identifiable model generation.
- **Why Important:** Tells the field where marginal effort actually shows up in AP, and provides a decomposition protocol for future reporting.
- **Why Possibly Novel:** Oracle analyses appear in individual papers; a longitudinal binding-constraint analysis across model history is missing.
- **Minimal Experiment:** Evaluate 8 public instance-segmentation models spanning eras with (a) standard AP, (b) oracle-box mask quality, (c) oracle-mask detection AP; chart the binding constraint over time.
- **Main Risk:** Oracle protocols must be implemented uniformly across heterogeneous codebases.
- **Research Cluster:** CONF

### IDEA-C-0052 — Patient-level leakage in frame-based endoscopy/polyp benchmarks
- **One-sentence idea:** Audit polyp and surgical-scene benchmarks for same-patient or same-sequence frames split across train and test, and measure the inflation via patient-blocked re-splits.
- **Problem:** Frame-sampled medical video datasets often split at frame level; near-identical frames land on both sides.
- **Core Hypothesis (falsifiable):** Embedding-based sequence clustering reveals cross-split near-duplicates in several popular benchmarks; patient/sequence-blocked re-splits reduce reported Dice by a nontrivial margin and shrink method gaps.
- **Why Important:** These benchmarks gate clinical claims; corrected numbers matter for translation.
- **Why Possibly Novel:** Individual dataset papers note this; a systematic cross-benchmark audit with published corrected splits is the contribution.
- **Minimal Experiment:** Cluster frames by embedding similarity on Kvasir-SEG/CVC families; identify cross-split clusters; retrain 4 methods on blocked splits; publish the corrected split files.
- **Main Risk:** Without patient metadata, clustering conflates similar-looking different patients; use conservative thresholds.
- **Research Cluster:** CONF

### IDEA-C-0053 — Rare-class seed variance decides long-tail benchmark rankings
- **One-sentence idea:** Measure how much LVIS-style long-tail benchmark rankings depend on training-seed variance concentrated in rare classes, and propose seed-marginalized reporting.
- **Problem:** Rare-class AP is estimated from few instances and is highly seed-sensitive, yet single-seed results decide publications.
- **Core Hypothesis (falsifiable):** Across 5 seeds, rare-class AP variance is several times common-class variance; bootstrap analysis shows a substantial probability that published method orderings would flip under reseeding.
- **Why Important:** Establishes statistically honest reporting standards for long-tail dense prediction.
- **Why Possibly Novel:** Seed variance is documented for classification; its concentration structure (rare classes) and ranking impact for long-tail segmentation is unquantified.
- **Minimal Experiment:** Train 2 representative methods × 5 seeds on LVIS-subset; decompose AP variance by class frequency bin; simulate ranking-flip probabilities for typical published gaps.
- **Main Risk:** Compute for multiple seeds; mitigate with shorter schedules shown to preserve variance structure.
- **Research Cluster:** CONF

### IDEA-C-0054 — Depth-separable classes inflate multi-task benchmark synergy claims
- **One-sentence idea:** Test whether reported segmentation gains from joint depth-segmentation training come disproportionately from classes that are trivially separable in depth, rather than from general representation synergy.
- **Problem:** Multi-task synergy is claimed at the dataset level; per-class attribution against a depth-only baseline is missing.
- **Core Hypothesis (falsifiable):** A depth-only segmenter (no RGB) achieves high IoU on an identifiable class subset; multi-task gains concentrate on exactly those classes, and vanish on depth-ambiguous classes.
- **Why Important:** Sharpens what multi-task learning contributes and predicts when adding depth heads is worthwhile.
- **Why Possibly Novel:** Multi-task ablations report aggregates; the depth-separability stratification is a simple missing control.
- **Minimal Experiment:** On NYUv2/Cityscapes-depth, train depth-only, RGB-only, and joint models; report per-class gains vs depth-only performance; test rank correlation.
- **Main Risk:** Depth sensor noise varies by class distance; control by distance-stratified analysis.
- **Research Cluster:** CONF

### IDEA-C-0055 — Annotation-tool fingerprints create learnable style clusters
- **One-sentence idea:** Detect which annotation tool (polygon, brush, superpixel-snap, SAM-assisted) produced each benchmark mask, and test whether models learn tool-specific boundary styles that corrupt cross-dataset evaluation.
- **Problem:** Datasets increasingly mix annotation tools (including SAM-assisted labeling), embedding tool artifacts into "ground truth."
- **Core Hypothesis (falsifiable):** A classifier distinguishes annotation tools from mask geometry alone at high accuracy; models trained on tool-X data score higher against tool-X test masks than tool-Y masks of equal semantic quality; SAM-assisted labels make SAM-family models look spuriously better.
- **Why Important:** The SAM-assisted-labeling feedback loop (models evaluated on their own ancestors' label style) threatens benchmark validity going forward.
- **Why Possibly Novel:** The circularity risk of model-assisted annotation for benchmark evaluation is discussed informally but unmeasured.
- **Minimal Experiment:** Collect masks of known tool provenance (dataset documentation + controlled re-annotation); train the tool classifier; cross-evaluate models trained on different tool styles; specifically test SAM-vs-non-SAM-labeled test subsets.
- **Main Risk:** Tool and dataset identity are confounded; requires controlled same-image multi-tool annotation for the core claim.
- **Research Cluster:** CONF

### IDEA-C-0056 — Camera-era signatures (ISP pipelines) as temporal confounders
- **One-sentence idea:** Test whether models exploit image-signal-processor era signatures (denoising, sharpening styles across camera generations) that correlate with class content in datasets assembled over many years.
- **Problem:** Long-lived datasets mix camera eras; content drifts with era (e.g., older images contain older object designs), coupling ISP style to semantics.
- **Core Hypothesis (falsifiable):** Camera-era is predictable from local texture statistics; per-class accuracy of dense models correlates with era-class association strength, and era-normalization (re-processing through a common ISP simulation) reduces specific class accuracies that depended on the shortcut.
- **Why Important:** Reveals a temporal shortcut relevant to any archive-based dataset, including medical PACS archives.
- **Why Possibly Novel:** ISP forensics exists; connecting era fingerprints to dense-benchmark class performance is new.
- **Minimal Experiment:** Where EXIF exists (OpenImages subsets), train an era predictor from texture patches; measure era-class mutual information; re-process images through a unified ISP simulator and re-evaluate per class.
- **Main Risk:** ISP normalization degrades genuine detail; use matched-degradation controls.
- **Research Cluster:** CONF

### IDEA-C-0057 — Adverse-weather benchmark gains are mostly exposure normalization
- **One-sentence idea:** Test whether much of the reported improvement of specialized night/fog segmentation methods over baselines is reproduced by classical exposure/contrast normalization preprocessing, isolating the truly semantic component of adverse-condition robustness.
- **Problem:** Adverse-condition papers compare against un-normalized baselines, conflating photometric preprocessing with semantic robustness.
- **Core Hypothesis (falsifiable):** Histogram-matching/retinex preprocessing plus a standard model recovers a large fraction of specialized methods' gains on ACDC/Dark-Zurich, and the residual specialized gain concentrates in classes with genuinely changed appearance (wet reflections, light sources), not globally.
- **Why Important:** Redirects adverse-weather research toward the classes where semantics actually change.
- **Why Possibly Novel:** Simple-baseline audits are common in other subfields but have not been run systematically for adverse-condition segmentation.
- **Minimal Experiment:** Evaluate 4 specialized methods vs (standard model + 3 classical normalizations) on ACDC; decompose residual gains per class.
- **Main Risk:** Normalization helps unevenly across condition types; report per-condition.
- **Research Cluster:** CONF

### IDEA-C-0058 — Referring-expression benchmarks rarely require the expression
- **One-sentence idea:** Quantify what fraction of referring-expression segmentation items are solvable from the object category alone (single instance of the category present), and re-report methods on the truly referential subset.
- **Problem:** RefCOCO-style benchmarks include many items where "the red cup on the left" reduces to "cup," inflating grounding claims.
- **Core Hypothesis (falsifiable):** A category-only baseline (detect category, return largest/only instance) solves a substantial fraction of items; method rankings on the residual multi-instance subset differ from full-benchmark rankings, with relational-reasoning methods gaining.
- **Why Important:** Gives the community the "hard split" that actually measures referring, cheaply derived from existing data.
- **Why Possibly Novel:** Dataset biases in RefCOCO are known for language; a category-sufficiency split with ranking impact for segmentation specifically is worth pinning down.
- **Minimal Experiment:** Compute per-item category-instance counts from COCO annotations; run the category-only baseline; re-evaluate 6 public referring-segmentation models on sufficiency-stratified splits.
- **Main Risk:** Category detection errors leak into the baseline; use ground-truth category masks for the upper bound.
- **Research Cluster:** CONF

### IDEA-C-0059 — Density-resolution coupling in crowd and aerial benchmarks
- **One-sentence idea:** Audit crowd/aerial segmentation-and-counting benchmarks for systematic correlation between object density and image resolution/GSD, which lets models use resolution as a density prior.
- **Problem:** Dense scenes tend to be photographed/zoomed differently; models may read sensor resolution cues instead of counting.
- **Core Hypothesis (falsifiable):** Density and effective resolution correlate strongly in popular benchmarks; models tested on resolution-decoupled data (same density, resampled resolutions) show density-estimation errors that track the training correlation.
- **Why Important:** Density estimates feed public-safety and agricultural decisions; a resolution shortcut is a deployment hazard.
- **Why Possibly Novel:** Scale augmentation is standard, but the dataset-level density-resolution coupling audit and decoupled re-evaluation protocol are not.
- **Minimal Experiment:** Measure density-resolution correlation in ShanghaiTech/DOTA; build decoupled evaluation via controlled resampling; compare model error curves against the measured coupling.
- **Main Risk:** Resampling changes texture detail confounding density cues; use camera-simulation-based resampling.
- **Research Cluster:** CONF

### IDEA-C-0060 — Linear-probe backbone comparisons confound feature quality with feature conditioning
- **One-sentence idea:** Test whether frozen-backbone linear-probe rankings for dense tasks are distorted by feature dimensionality and covariance conditioning (whitening changes winners), which probe training absorbs unevenly.
- **Problem:** The community ranks VFMs by linear-probe mIoU, implicitly assuming probes extract equal fractions of available information from differently-conditioned feature spaces.
- **Core Hypothesis (falsifiable):** After per-backbone whitening and dimensionality matching (random projection to common d), some standard backbone rankings change; probe optimizer sensitivity is systematically higher for ill-conditioned feature spaces.
- **Why Important:** Backbone-selection decisions across the field rest on these comparisons; conditioning-corrected protocols make them meaningful.
- **Why Possibly Novel:** Probing-methodology critiques exist in NLP interpretability; dense-vision backbone leaderboards have not adopted or tested conditioning controls.
- **Minimal Experiment:** Rank 6 frozen backbones on ADE20K linear probes under raw, whitened, and dimension-matched conditions with swept probe hyperparameters; report ranking stability.
- **Main Risk:** Whitening estimated on limited data adds its own noise; use large unlabeled pools for covariance estimation.
- **Research Cluster:** CONF
## Cluster DYN — Training-Dynamics Hypotheses (IDEA-C-0061 … IDEA-C-0095)

### IDEA-C-0061 — Effective-rank decay of LoRA products during long fine-tunes
- **One-sentence idea:** Track the effective rank of LoRA update matrices (BA) over long dense-task fine-tunes to test whether they collapse toward rank far below the nominal r, wasting the allocated capacity.
- **Problem:** LoRA rank is chosen a priori, but nothing guarantees the optimizer uses the allocated subspace; capacity may silently collapse.
- **Core Hypothesis (falsifiable):** Effective rank (entropy of singular values of BA) decays during training toward a task-dependent floor much smaller than r, the floor is predictable from gradient covariance spectrum at initialization, and a spectral-floor regularizer that prevents collapse improves final boundary metrics at equal r.
- **Why Important:** Explains why raising r often doesn't help and yields a principled rank-selection/regularization recipe.
- **Why Possibly Novel:** LoRA rank ablations abound; the training-time spectral trajectory and its predictability from initialization gradients are unmeasured for dense tasks.
- **Minimal Experiment:** Fine-tune LoRA (r=4..64) on 3 segmentation datasets; log BA singular spectra per epoch; correlate final effective rank with first-epoch gradient covariance spectra; add nuclear-norm-floor regularizer and compare.
- **Main Risk:** Effective rank definitions differ; report several (entropy, stable rank) for robustness.
- **Research Cluster:** DYN

### IDEA-C-0062 — Layer-wise forgetting timescales: boundary detail dies first in early layers
- **One-sentence idea:** Measure per-layer, per-capability forgetting during VFM fine-tuning to test whether high-frequency boundary sensitivity (early layers) is forgotten on a faster timescale than semantics (late layers).
- **Problem:** "Catastrophic forgetting" is treated as scalar; a timescale hierarchy would dictate where to freeze or apply EWC-style protection.
- **Core Hypothesis (falsifiable):** During fine-tuning on a texture-shifted target, frozen-probe boundary metrics computed from early-layer features degrade with a time constant several times shorter than semantic-probe degradation from late layers, consistently across datasets.
- **Why Important:** Converts forgetting mitigation from uniform recipes to layer-timescale-matched protection at lower cost.
- **Why Possibly Novel:** Layer-wise probing exists; a timescale (dynamics) formulation with capability decomposition for dense features is new.
- **Minimal Experiment:** Fine-tune DINOv2 on a medical dataset; every N steps, freeze and probe each layer for boundary detection and for semantic classes on natural images; fit exponential decay constants per (layer, capability).
- **Main Risk:** Probe capacity confounds; use fixed tiny probes with matched training budgets.
- **Research Cluster:** DYN

### IDEA-C-0063 — Prompt-token norm explosions as loss-spike precursors in mask decoder training
- **One-sentence idea:** Test whether training instabilities (loss spikes) in SAM-style decoder fine-tuning are preceded by measurable norm growth in prompt/mask token embeddings, yielding an early-warning signal and a targeted normalization fix.
- **Problem:** Decoder fine-tuning instabilities are handled with global tricks (gradient clipping, LR drops) without localizing the mechanism.
- **Core Hypothesis (falsifiable):** Across many runs, prompt-token norm z-scores exceed a threshold consistently several steps before loss spikes (high precision/recall as a predictor), and per-token norm capping eliminates most spikes without hurting final accuracy.
- **Why Important:** Cheap stability diagnostics beat blanket clipping, and localize which architectural component is fragile.
- **Why Possibly Novel:** Token-norm pathologies are studied in LLM pretraining (attention entropy collapse); mask/prompt-token-specific instability forensics for segmentation decoders is unexplored.
- **Minimal Experiment:** Instrument 20 fine-tuning runs with per-token-norm logging at varied LR; build spike predictor; ablate with norm capping vs gradient clipping at matched final accuracy.
- **Main Risk:** Spikes may have multiple causes; predictor evaluation must use held-out runs.
- **Research Cluster:** DYN

### IDEA-C-0064 — Prompt-conditional forgetting: boxes forgotten before points
- **One-sentence idea:** Test whether fine-tuning SAM on point-only interaction data causes selective degradation of box-prompt performance (and vice versa), i.e., forgetting is conditional on prompt type, not just data domain.
- **Problem:** Adaptation pipelines fine-tune with one prompt type for convenience, implicitly assuming prompt capabilities are coupled.
- **Core Hypothesis (falsifiable):** Point-only fine-tuning degrades box-prompt IoU significantly while point-prompt IoU improves, with the degradation localized (by weight-diff analysis) to prompt-encoder parameters specific to box embedding.
- **Why Important:** Establishes prompt-type balance as a required ingredient of SAM adaptation recipes.
- **Why Possibly Novel:** Forgetting across datasets is studied; forgetting across prompt modalities within one model is not.
- **Minimal Experiment:** Fine-tune SAM on a target dataset with point-only, box-only, and mixed prompts; evaluate all prompt types before/after; localize weight changes by parameter group.
- **Main Risk:** Effect may be small if prompt encodings share pathways; the localization analysis handles either outcome informatively.
- **Research Cluster:** DYN

### IDEA-C-0065 — A sharp EMA-decay phase transition in teacher-student confirmation bias
- **One-sentence idea:** Test whether semi-supervised segmentation with EMA teachers exhibits a sharp phase transition in confirmation bias (error self-amplification) as EMA decay crosses a critical value tied to the student's learning rate.
- **Problem:** EMA decay is tuned by folklore (0.99–0.9999); if a critical surface exists in (decay, LR) space, tuning could be principled.
- **Core Hypothesis (falsifiable):** Error persistence time of injected pseudo-label mistakes diverges as decay approaches a critical value predicted by a two-timescale analysis (teacher averaging window vs student adaptation time), with the transition sharp rather than gradual.
- **Why Important:** Converts the most sensitive semi-supervised hyperparameter into a computable quantity.
- **Why Possibly Novel:** EMA ablations exist; a dynamical-systems analysis with an experimentally verified critical surface for dense pseudo-labeling is new.
- **Minimal Experiment:** Inject controlled label errors into a mean-teacher pipeline on VOC; measure error survival time vs (decay, LR) grid; test for scaling collapse of survival curves around the predicted critical line.
- **Main Risk:** Transitions may be smeared by data heterogeneity; use per-class analysis.
- **Research Cluster:** DYN

### IDEA-C-0066 — Delayed generalization (grokking) on thin structures
- **One-sentence idea:** Look for grokking-like delayed generalization in segmentation fine-tuning, where thin-structure accuracy jumps long after interior accuracy converges, and identify the weight-space signature of the transition.
- **Problem:** Practitioners stop training when val-mIoU plateaus; if fine structures grok later, standard early stopping systematically sacrifices them.
- **Core Hypothesis (falsifiable):** On small vessel/crack datasets with long schedules and weight decay, boundary/thin-structure metrics show a delayed jump after interior-metric convergence in a reproducible fraction of runs, coinciding with a measurable drop in weight norm / emergence of sparse frequency-selective filters.
- **Why Important:** Would change early-stopping practice for fine-structure tasks and connect grokking research to a practical vision setting.
- **Why Possibly Novel:** Grokking is documented in algorithmic tasks; a dense-prediction manifestation with structure-stratified metrics has not been reported.
- **Minimal Experiment:** Train small ViT/UNet on DRIVE with 20x standard schedule length, multiple weight decays and seeds; log width-stratified metrics and weight-space statistics; test for delayed transitions.
- **Main Risk:** May simply not occur; a well-powered null result still informs early-stopping practice.
- **Research Cluster:** DYN

### IDEA-C-0067 — Tokenizer cliffs make discrete prompt optimization non-smooth
- **One-sentence idea:** Characterize how discrete text-prompt optimization for open-vocab segmentation is dominated by tokenizer geometry — nearby embedding points decode to semantically unrelated tokens — producing cliff-like objective landscapes.
- **Problem:** Hard-prompt search methods behave erratically for dense tasks; the role of tokenizer discretization is unquantified.
- **Core Hypothesis (falsifiable):** The segmentation objective as a function of prompt-embedding position is locally smooth in continuous space but its projection to nearest-token sequences has discontinuities whose density is predictable from local token-embedding packing density; regions of high packing density yield systematically better discrete prompts.
- **Why Important:** Explains discrete prompt search failures and suggests searching in high-density embedding regions, a concrete algorithmic prior.
- **Why Possibly Novel:** Hard-vs-soft prompt gaps are known in NLP; a geometric account tied to token packing density, tested on dense vision tasks, is new.
- **Minimal Experiment:** For a CLIP-based segmenter, sample continuous prompt embeddings along interpolation paths; measure objective smoothness vs nearest-token decoding stability; correlate discrete-search success with local packing density.
- **Main Risk:** Findings may be tokenizer-specific; test BPE and SentencePiece variants.
- **Research Cluster:** DYN

### IDEA-C-0068 — Adapters silently reshape the effective receptive field of frozen backbones
- **One-sentence idea:** Measure how the effective receptive field (ERF) of a frozen VFM changes when adapters are trained, testing whether adapters act primarily by re-routing spatial context rather than re-encoding appearance.
- **Problem:** Adapters are interpreted as feature modulators; if their main effect is spatial-context rerouting, adapter placement theory changes.
- **Core Hypothesis (falsifiable):** Gradient-based ERF maps shift substantially (measurable spread/shape change) after adapter training on tasks requiring different context sizes, and the ERF change magnitude predicts adaptation gain better than weight-change magnitude.
- **Why Important:** Provides a functional (not parametric) account of what PEFT learns, guiding placement and capacity decisions.
- **Why Possibly Novel:** ERF analysis exists for CNN training; applying it as the primary observable of PEFT dynamics on frozen ViTs is new.
- **Minimal Experiment:** Train adapters on small-object vs large-context segmentation tasks; compute ERF before/after per layer; regress task gain on ERF change vs parameter-space change.
- **Main Risk:** ERF measurement on ViTs is noisy; average over many inputs and locations.
- **Research Cluster:** DYN

### IDEA-C-0069 — The last 5% of the cosine schedule buys most of the boundary sharpness
- **One-sentence idea:** Test whether the final low-LR tail of cosine schedules contributes disproportionately to boundary-F while interior IoU is settled early, implying two distinct learning phases with different LR needs.
- **Problem:** Schedule design treats dense metrics as one objective; if boundary learning is a low-LR phenomenon, truncated schedules silently sacrifice edges.
- **Core Hypothesis (falsifiable):** Checkpoint trajectories show interior-IoU convergence within the first 60% of training while boundary-F keeps improving until the end; truncating the tail costs boundary-F several times more than interior IoU, and extending only the tail (constant low LR) recovers it.
- **Why Important:** Directly actionable for compute-constrained fine-tuning: allocate schedule tails when boundaries matter.
- **Why Possibly Novel:** LR schedule studies target loss/accuracy; a metric-decomposed phase analysis for dense prediction is missing.
- **Minimal Experiment:** Fine-tune on ADE20K with full/truncated/tail-extended schedules; plot interior vs boundary metric trajectories; verify on a second dataset and architecture.
- **Main Risk:** Effect may be entangled with EMA/augmentation annealing; ablate those.
- **Research Cluster:** DYN

### IDEA-C-0070 — Attention-entropy collapse as a pre-metric OOD-failure predictor
- **One-sentence idea:** Test whether the entropy of attention distributions in fine-tuned ViT segmenters collapses during training in a way that predicts later OOD failure, before any validation metric moves.
- **Problem:** Fine-tuning silently narrows models; practitioners discover brittleness only at deployment.
- **Core Hypothesis (falsifiable):** Attention entropy averaged over mid-layer heads decreases monotonically during fine-tuning, and its final value (or decay rate) predicts corruption-benchmark degradation across runs/datasets with high rank correlation, beating weight-space distance predictors.
- **Why Important:** A free training-time dial for the robustness-specialization tradeoff.
- **Why Possibly Novel:** Attention entropy is studied in LLM stability; as a quantitative OOD-robustness predictor for dense fine-tuning it is untested.
- **Minimal Experiment:** Fine-tune 20 model/dataset configurations; log attention entropy trajectories; evaluate all on corruption suites; fit and cross-validate the predictor.
- **Main Risk:** Correlation may be confounded by fine-tuning length; include length-matched controls.
- **Research Cluster:** DYN

### IDEA-C-0071 — Query churn: decoder queries specialize, then destabilize
- **One-sentence idea:** Track the object-query-to-instance assignment dynamics in DETR/Mask2Former-style training to test whether queries undergo a churn phase (specialization followed by re-assignment cascades) that explains late-training instance-segmentation instability.
- **Problem:** Query-based segmentation training exhibits unexplained late-stage metric oscillations; assignment dynamics are rarely instrumented.
- **Core Hypothesis (falsifiable):** Hungarian-assignment stability per query decreases (churn events) in bursts that coincide with AP oscillations; freezing assignment (soft-anchoring queries to their specializations) after the specialization phase removes the oscillations without hurting final AP.
- **Why Important:** Explains and fixes a practical instability, and characterizes an emergent division-of-labor process.
- **Why Possibly Novel:** Query specialization is described statically (what queries learn); its temporal stability dynamics and a churn-suppression intervention are new.
- **Minimal Experiment:** Log per-image query-instance assignments across training on COCO-subset; define churn metrics; correlate with AP oscillations; implement assignment-anchoring and compare.
- **Main Risk:** Churn may be beneficial exploration; the anchoring ablation directly tests this.
- **Research Cluster:** DYN

### IDEA-C-0072 — Dice and cross-entropy gradients alternate conflict on a predictable schedule
- **One-sentence idea:** Measure the gradient cosine between Dice and CE loss components during segmentation training to test whether conflict is phase-structured (aligned early, conflicting at boundary-refinement phase) rather than random.
- **Problem:** Compound losses are summed with fixed weights despite unknown, possibly time-varying interference between components.
- **Core Hypothesis (falsifiable):** Dice-CE gradient cosine follows a reproducible trajectory across datasets — positive early, negative in late training concentrated on boundary pixels — and phase-scheduled weighting (CE→Dice handoff) beats any fixed weighting at equal budget.
- **Why Important:** Replaces loss-weight grid search with a measurement-driven schedule, and explains contradictory loss-comparison results in the literature.
- **Why Possibly Novel:** Gradient conflict is studied across tasks (multi-task learning); within-loss-component conflict dynamics for segmentation are uninstrumented.
- **Minimal Experiment:** Log component gradient cosines (global and boundary-restricted) across training on 3 datasets; verify trajectory reproducibility; implement handoff schedule and compare with fixed-weight baselines.
- **Main Risk:** Cosine in full parameter space may hide layer-wise structure; log per-layer.
- **Research Cluster:** DYN

### IDEA-C-0073 — LayerNorm affine parameters carry most of PEFT's domain adaptation
- **One-sentence idea:** Test the falsifiable claim that during PEFT of VFMs onto shifted domains, the functionally decisive changes are recoverable from LayerNorm gain/bias trajectories alone, with adapter weights providing mostly redundant capacity.
- **Problem:** Attribution of what PEFT actually changes functionally is missing; parameters updated ≠ parameters that matter.
- **Core Hypothesis (falsifiable):** Re-applying only the LN-parameter trajectory (adapters reset to identity) recovers the large majority of the adapted model's gain on style/domain-shift tasks but not on semantic-shift tasks, cleanly dissociating shift types by which parameters carry them.
- **Why Important:** If LN carries style shifts, deployment can ship tiny LN deltas per domain; also yields a diagnostic for classifying shift type.
- **Why Possibly Novel:** LN-only tuning is known to work; the trajectory-transplant methodology attributing gains within full PEFT runs, and the style/semantic dissociation, are new.
- **Minimal Experiment:** Run adapter-PEFT on style-shift (Cityscapes→ACDC) and semantic-shift (VOC→medical) tasks; transplant LN trajectories into fresh models; measure recovered gain fraction per shift type.
- **Main Risk:** LN and adapter updates may be entangled (compensating each other); include joint-null controls.
- **Research Cluster:** DYN

### IDEA-C-0074 — Small-batch gradient variance systematically biases against small objects
- **One-sentence idea:** Derive and verify a quantitative relationship between batch size, per-object gradient variance, and the systematic under-segmentation of small objects in dense training.
- **Problem:** Small-object performance differences across labs may be a batch-size artifact, not a method difference.
- **Core Hypothesis (falsifiable):** Small-object recall at convergence is a decreasing function of per-batch object-size variance (not batch size per se), predictable from the dataset's object-size distribution; object-size-stratified batch construction at small batch size recovers large-batch small-object recall.
- **Why Important:** Explains a reproducibility failure mode and provides a zero-cost sampler fix for memory-constrained training.
- **Why Possibly Novel:** Batch-size effects are studied via LR scaling; an object-size-mediated mechanism with a sampler-based causal test is new.
- **Minimal Experiment:** Train identical models at batch sizes {2..32} with random vs size-stratified sampling on COCO-subset; plot small-object recall vs measured gradient variance; test the predicted collapse of the batch-size effect under stratification.
- **Main Risk:** LR-batch interactions confound; use LR sweeps at each batch size.
- **Research Cluster:** DYN

### IDEA-C-0075 — Warmup length decides whether fine-tunes stay in the pretrained basin
- **One-sentence idea:** Test whether LR warmup duration controls a discrete outcome — remaining linearly mode-connected to the pretrained model vs escaping to a disconnected basin — with consequences for robustness and model merging.
- **Problem:** Warmup is tuned for stability; its role in basin selection (and downstream mergeability/robustness) is uncharacterized.
- **Core Hypothesis (falsifiable):** Below a critical warmup length, fine-tuned dense models exhibit a loss barrier to the pretrained weights (basin escape) and lose OOD robustness; above it, they remain barrier-free and mergeable, with the transition sharp in warmup length and predictable from early gradient norms.
- **Why Important:** Ties three practical properties (stability, robustness, mergeability) to one cheap knob with a geometric explanation.
- **Why Possibly Novel:** Basin analyses exist for classification fine-tuning; the warmup-as-basin-selector hypothesis with a critical threshold is untested for dense tasks.
- **Minimal Experiment:** Fine-tune with warmup lengths {0..10%} on ADE20K; measure linear-path barriers to the pretrained model, corruption robustness, and pairwise mergeability; locate the transition.
- **Main Risk:** Barrier presence may vary continuously; report barrier magnitude, not just presence.
- **Research Cluster:** DYN

### IDEA-C-0076 — Prompt tuning has two phases: retrieval, then deformation
- **One-sentence idea:** Test whether learned prompt vectors first converge toward the nearest pretraining concept embedding (retrieval phase) and only later drift away to encode task-specific information (deformation phase), explaining prompt-tuning's characteristic loss plateaus.
- **Problem:** Prompt-tuning dynamics are opaque; understanding phases would inform initialization and early stopping.
- **Core Hypothesis (falsifiable):** Distance from learned prompts to the nearest token-embedding cluster decreases then increases during training (non-monotone), the turn point coincides with a loss plateau, and initializing directly at the retrieved concept skips the first phase, cutting training time substantially at equal accuracy.
- **Why Important:** Halves prompt-tuning cost with a principled initialization and gives an interpretable account of what prompts encode.
- **Why Possibly Novel:** Prompt interpretability work decodes final prompts; the two-phase temporal structure and skip-initialization are untested, especially for dense prediction.
- **Minimal Experiment:** Track prompt-to-vocabulary distances during CoOp-style tuning for segmentation; identify phase structure; implement retrieval-initialization and compare convergence curves.
- **Main Risk:** Phases may blur for multi-token prompts; analyze per token.
- **Research Cluster:** DYN

### IDEA-C-0077 — Neural collapse onset in dense features marks the end of useful self-distillation
- **One-sentence idea:** Test whether iterated self-distillation of dense features progressively induces neural-collapse-like geometry (within-class patch feature variance collapse), and whether collapse onset predicts when further distillation stops helping downstream segmentation.
- **Problem:** Self-distillation rounds are chosen blindly; a geometric stopping criterion would save compute and prevent degradation.
- **Core Hypothesis (falsifiable):** Within-class patch-feature variance ratios decay monotonically across distillation generations; downstream transfer peaks at a characteristic variance ratio and declines after, consistently across datasets — making the ratio a valid early-stopping signal.
- **Why Important:** Provides the first principled stopping rule for feature self-distillation pipelines used in building VFMs.
- **Why Possibly Novel:** Neural collapse is characterized for classification heads; its emergence in patch-token space across distillation generations, tied to transfer, is new.
- **Minimal Experiment:** Run 5 generations of DINO-style self-distillation at small scale; measure patch-level collapse metrics per generation; evaluate frozen-probe segmentation transfer; test the predicted peak.
- **Main Risk:** Small-scale distillation may not reproduce large-scale dynamics; validate trends on two scales.
- **Research Cluster:** DYN

### IDEA-C-0078 — Stochastic depth randomizes adapter inputs into instability
- **One-sentence idea:** Test whether adapters inserted into backbones trained/fine-tuned with stochastic depth receive inconsistent input distributions (block present vs dropped), causing a measurable share of PEFT training instability.
- **Problem:** PEFT recipes inherit regularization settings from full fine-tuning without checking interactions with frozen-backbone assumptions.
- **Core Hypothesis (falsifiable):** Adapter gradient variance is significantly higher immediately downstream of stochastically-dropped blocks; disabling stochastic depth (or making drops consistent within a batch) removes a quantifiable fraction of loss spikes and improves final accuracy at equal regularization strength (compensated by other means).
- **Why Important:** A simple recipe correction affecting all adapter users, with a clean mechanistic account.
- **Why Possibly Novel:** Stochastic-depth interactions with PEFT modules appear unstudied; recipes silently mix them.
- **Minimal Experiment:** Fine-tune adapters with/without stochastic depth and with drop-consistent variants on 3 datasets; log adapter gradient variance by position; compare stability and final metrics.
- **Main Risk:** Effect size may depend on drop rate; sweep it.
- **Research Cluster:** DYN

### IDEA-C-0079 — fp16 loss-scaling underflow selectively kills thin-structure gradients
- **One-sentence idea:** Test whether mixed-precision training underflows gradients originating from small/thin structures first (few pixels × small per-pixel gradients), creating a precision-induced bias that full-precision training doesn't have.
- **Problem:** Mixed precision is universal; its error is assumed uniform, but gradient magnitude scales with structure area.
- **Core Hypothesis (falsifiable):** Per-structure gradient norms below the fp16 representable threshold occur predominantly for structures under a size threshold; models trained in fp16 (vs bf16/fp32, same seed) show a specific thin-structure recall deficit that disappears with per-class loss scaling.
- **Why Important:** Identifies a silent hardware-numerics bias against exactly the structures many applications care about, with a one-line fix.
- **Why Possibly Novel:** Mixed-precision studies target convergence/stability; a structure-size-stratified bias analysis is new.
- **Minimal Experiment:** Train same-seed fp16/bf16/fp32 models on vessel and small-lesion datasets; log gradient-magnitude histograms per structure size; compare size-stratified recall; test per-class scaling fix.
- **Main Risk:** Modern loss-scaling may already prevent this; then the result is a reassuring bound — still useful.
- **Research Cluster:** DYN

### IDEA-C-0080 — Token-merging during training leaves permanent high-frequency blind spots
- **One-sentence idea:** Test whether efficiency techniques that merge/prune tokens during fine-tuning bias the model against high-frequency regions permanently — the bias persisting even when all tokens are restored at inference.
- **Problem:** Token reduction is treated as an inference-time approximation; its effect on what is learned during training is unexamined.
- **Core Hypothesis (falsifiable):** Models fine-tuned with token merging show boundary/texture deficits (vs full-token training) that persist under full-token inference, localized (via feature attribution) to regions that were most frequently merged during training; a merge-schedule that protects high-frequency tokens removes the deficit.
- **Why Important:** Warns that training-time efficiency shortcuts change the learned function, not just the computation, and provides a protective schedule.
- **Why Possibly Novel:** ToMe-style methods are evaluated for accuracy drop at inference; the training-dynamics footprint with persistence testing is new.
- **Minimal Experiment:** Fine-tune with/without token merging (and with frequency-protective merging) on ADE20K; evaluate all under full-token inference; map spatial deficit against per-region merge frequency statistics.
- **Main Risk:** Deficits may be small at moderate merge ratios; sweep aggressiveness.
- **Research Cluster:** DYN

### IDEA-C-0081 — Forgetting exponents are set by boundary complexity, not class frequency
- **One-sentence idea:** In continual segmentation, test whether per-class forgetting follows power laws whose exponents are determined by the class's boundary complexity (shape entropy) rather than its frequency or order in the task sequence.
- **Problem:** Continual-learning theory predicts forgetting by task similarity/frequency; dense prediction adds geometry that may dominate.
- **Core Hypothesis (falsifiable):** Fitting per-class forgetting curves across task sequences, boundary-complexity measures predict decay exponents better than frequency or recency, and complexity-weighted replay buffers beat frequency-weighted ones at equal memory.
- **Why Important:** Gives continual segmentation a task-specific theory and a better replay policy.
- **Why Possibly Novel:** Continual segmentation benchmarks exist; a geometric predictor of forgetting rates with a replay-policy consequence is new.
- **Minimal Experiment:** Run class-incremental training on VOC/ADE sequences; fit per-class forgetting exponents; regress on complexity/frequency/recency; implement complexity-weighted replay and compare.
- **Main Risk:** Curve fitting on few checkpoints is noisy; log densely.
- **Research Cluster:** DYN

### IDEA-C-0082 — Minima sharpness predicts cross-dataset transfer better than validation mIoU
- **One-sentence idea:** Test whether flatness measures of dense-prediction minima predict cross-dataset generalization better than in-distribution validation metrics, enabling checkpoint selection for transfer without target data.
- **Problem:** Checkpoint selection for deployment-to-new-domains uses val-mIoU, which may anti-correlate with transferability.
- **Core Hypothesis (falsifiable):** Across a pool of checkpoints (varying seed, schedule, augmentation), sharpness metrics (SAM-style perturbed loss, Hessian trace estimates) rank cross-dataset mIoU better (higher rank correlation) than source-val mIoU does, especially among checkpoints within a narrow source-val band.
- **Why Important:** Provides a target-free model-selection criterion for the ubiquitous train-here-deploy-there scenario.
- **Why Possibly Novel:** Flatness-generalization links are contested in classification; a dense-prediction, cross-dataset, selection-oriented formulation is unresolved and testable.
- **Minimal Experiment:** Generate 30 checkpoints on Cityscapes; measure sharpness cheaply; evaluate on 4 other driving datasets; compare rank correlations of predictors.
- **Main Risk:** Sharpness measures are parameterization-sensitive; use scale-invariant variants.
- **Research Cluster:** DYN

### IDEA-C-0083 — Registers as gradient lightning rods: artifact absorption during fine-tuning
- **One-sentence idea:** Test whether register tokens in ViTs act as sinks for artifact gradients during dense fine-tuning, and whether removing them redirects high-norm outlier behavior into patch tokens, producing spatial speckle in segmentation outputs.
- **Problem:** Registers were introduced to clean attention maps at pretraining; their dynamical role during downstream fine-tuning is unknown.
- **Core Hypothesis (falsifiable):** Fine-tuning register-free variants (registers ablated or masked) of the same backbone produces measurably more high-norm outlier patch tokens over training and more isolated-pixel errors in predictions, while register-equipped models concentrate outlier dynamics in registers.
- **Why Important:** Informs whether registers should be kept, added, or expanded when adapting VFMs for dense tasks.
- **Why Possibly Novel:** Registers are studied as a pretraining/representation phenomenon; their fine-tuning dynamics and output-artifact consequences are new territory.
- **Minimal Experiment:** Fine-tune DINOv2-with-registers vs register-masked controls on ADE20K; track outlier-token statistics through training; quantify speckle (isolated error components) in outputs.
- **Main Risk:** Masking registers post-hoc differs from training without them; also compare to natively register-free checkpoints.
- **Research Cluster:** DYN

### IDEA-C-0084 — Positional-embedding interpolation transients follow a predictable annealing law
- **One-sentence idea:** Characterize the transient spatially-periodic error patterns that appear when fine-tuning ViTs at a new resolution (interpolated positional embeddings) and test whether their decay follows a predictable law that dictates minimum fine-tuning length.
- **Problem:** Resolution changes are routine; the adaptation cost is folklore ("fine-tune a bit"), with no quantitative guidance.
- **Core Hypothesis (falsifiable):** Immediately after PE interpolation, prediction error exhibits spatial periodicity at the original patch-grid frequency; its amplitude decays exponentially with steps at a rate proportional to PE learning rate, giving a closed-form minimum schedule length to reach a target artifact level.
- **Why Important:** Replaces guesswork about resolution-transfer fine-tuning budgets with a formula, saving compute at scale.
- **Why Possibly Novel:** PE interpolation is standard practice; nobody has characterized the transient error structure or derived budget rules from it.
- **Minimal Experiment:** Fine-tune at 2x resolution on ADE20K; compute spatial FFTs of error maps across checkpoints; fit decay rates across LR settings; validate the budget formula on a second backbone.
- **Main Risk:** Modern relative/RoPE-style encodings may not show the effect; scope to absolute-PE models and report the contrast.
- **Research Cluster:** DYN

### IDEA-C-0085 — A required two-timescale LR ratio between prompt encoder and mask decoder
- **One-sentence idea:** Test whether stable SAM-style fine-tuning requires the prompt-encoder learning rate to exceed the decoder's by a roughly constant ratio, reflecting a fast-variable/slow-variable structure in the interaction dynamics.
- **Problem:** Component-wise LRs for promptable models are set ad hoc; instability and prompt-ignoring behavior may share a root cause.
- **Core Hypothesis (falsifiable):** In a 2D LR grid (prompt-encoder × decoder), the stable-and-accurate region is a diagonal band (ratio, not absolute values), consistent across datasets; ratios below the band produce prompt-ignoring solutions (decoder learns unconditional masks), above it produce oscillations.
- **Why Important:** One reusable hyperparameter law for everyone adapting promptable segmenters.
- **Why Possibly Novel:** Two-timescale analyses exist in GAN/actor-critic training; mapping this structure onto promptable-segmentation components is new.
- **Minimal Experiment:** LR-grid fine-tunes of SAM decoder+prompt-encoder on 2 datasets; map stability/accuracy/prompt-influence (gradient of output wrt prompts) over the grid; test band consistency.
- **Main Risk:** The band may depend on prompt type mixture; include it as a third axis in a reduced design.
- **Research Cluster:** DYN

### IDEA-C-0086 — Curriculum-by-size changes final boundary quality at equal final loss
- **One-sentence idea:** Test path dependence in dense training: whether ordering training data by object size (small-first vs large-first) changes final boundary quality even when final training loss is matched, implying optimization path determines feature allocation.
- **Problem:** Loss-matched path dependence would undermine the assumption that convergence level summarizes training, guiding curriculum design.
- **Core Hypothesis (falsifiable):** Small-first curricula produce measurably better final boundary-F and worse large-object smoothness than large-first, at matched final train loss and steps, with feature-space analysis showing earlier-formed frequency-selective filters persisting (first-mover advantage in feature allocation).
- **Why Important:** Establishes curriculum as a lever over the interior/boundary quality tradeoff at zero extra cost.
- **Why Possibly Novel:** Curricula are studied for convergence speed; loss-matched final-quality path dependence with a feature-allocation mechanism for dense tasks is new.
- **Minimal Experiment:** Train size-ordered curricula (both directions + shuffled control) on COCO-subset to matched loss; compare metric decompositions and early-filter analyses; replicate on a second dataset.
- **Main Risk:** Matching final loss exactly is fiddly; match within tight tolerance and report sensitivity.
- **Research Cluster:** DYN

### IDEA-C-0087 — Optimal weight-averaging window scales with object-scale diversity
- **One-sentence idea:** Test whether the optimal window length for checkpoint averaging (EMA/SWA) in segmentation grows with the dataset's object-scale diversity, reflecting that scale-diverse data induces slower, oscillatory convergence that averaging must span.
- **Problem:** EMA/SWA windows are copied between datasets; a dataset-property-based rule would remove a tuning dimension.
- **Core Hypothesis (falsifiable):** Across datasets with measured object-scale entropy, the accuracy-maximizing averaging window correlates strongly with scale entropy; controlled experiments that artificially reduce scale diversity (size-filtered subsets) shrink the optimal window accordingly.
- **Why Important:** A predictive hyperparameter law tied to measurable data statistics, plus insight into why dense training oscillates.
- **Why Possibly Novel:** Averaging windows are studied generically; linking them causally to a dense-data property is new.
- **Minimal Experiment:** Sweep EMA windows on 5 datasets with computed scale entropy; fit the relationship; run the causal size-filter intervention on one dataset.
- **Main Risk:** Other data properties co-vary with scale entropy; the intervention experiment carries the causal weight.
- **Research Cluster:** DYN

### IDEA-C-0088 — Semantic torque: frozen text encoders slowly rotate visual class prototypes
- **One-sentence idea:** Measure whether gradients flowing through frozen text embeddings in VLM dense fine-tuning induce a slow, coherent rotation of visual class prototypes (rather than isotropic drift), with predictable consequences for zero-shot retention.
- **Problem:** Fine-tuning VLM-based segmenters degrades zero-shot ability in poorly understood ways; the geometry of the degradation is uncharacterized.
- **Core Hypothesis (falsifiable):** Visual prototype trajectories during fine-tuning are dominated by a low-dimensional rotation component (aligning trained-class prototypes to their text anchors) that measurably drags untrained-class prototypes along, and counter-rotating untrained prototypes post-hoc restores most zero-shot loss.
- **Why Important:** Turns zero-shot forgetting from a mystery into a correctable geometric transformation.
- **Why Possibly Novel:** Feature drift is measured as distance; identifying a coherent rotational structure with a post-hoc correction is new.
- **Minimal Experiment:** Fine-tune an open-vocab segmenter on a class subset; log prototype trajectories; fit rotation+residual decomposition; apply inverse rotation to held-out class prototypes and measure zero-shot recovery.
- **Main Risk:** Drift may be genuinely high-dimensional; the decomposition quality is itself the test.
- **Research Cluster:** DYN

### IDEA-C-0089 — Dice-loss plateaus are saddle escapes with predictable duration
- **One-sentence idea:** Test whether the characteristic long plateaus of Dice-loss training correspond to saddle-point escapes whose duration is predictable from the loss's degenerate behavior on empty-prediction regions, enabling plateau-skipping initialization.
- **Problem:** Dice training famously stalls (especially small structures); the community works around it with loss mixtures rather than understanding it.
- **Core Hypothesis (falsifiable):** Plateau duration scales with structure smallness according to a law derived from Dice gradient structure near all-background predictions; initializing the output bias to match target foreground prevalence removes the plateau, saving a predictable number of steps.
- **Why Important:** A mechanistic account plus a free convergence speedup for every Dice user.
- **Why Possibly Novel:** Dice pathologies are described empirically; a quantitative saddle analysis with a validated duration law is missing.
- **Minimal Experiment:** Train on synthetic structures of swept size with pure Dice; measure plateau lengths; derive/fit the scaling law; test bias-initialization fix on real small-lesion data.
- **Main Risk:** Adam's normalization complicates gradient analysis; analyze under both SGD and Adam.
- **Research Cluster:** DYN

### IDEA-C-0090 — Adapter initialization scale selects lazy vs feature-learning regimes
- **One-sentence idea:** Test whether adapter/LoRA initialization scale places dense-task PEFT into a lazy (kernel-like) vs rich (feature-learning) regime, with boundary sharpness achievable only in the rich regime.
- **Problem:** Init scales are folklore (LoRA B=0); if regime selection is at stake, the choice governs what PEFT can learn at all.
- **Core Hypothesis (falsifiable):** Small-init PEFT solutions stay close to the tangent-kernel prediction (verified by kernel-distance metrics) and cap boundary-F below large-init solutions on tasks needing new edge features; the regime boundary follows the theoretically expected init-scale/LR relationship.
- **Why Important:** Connects PEFT practice to feature-learning theory with a concrete, dense-task-relevant capability consequence.
- **Why Possibly Novel:** Lazy/rich analysis exists for training from scratch; applying it to PEFT modules on frozen VFMs with a capability-based readout is new.
- **Minimal Experiment:** Sweep adapter init scales on a boundary-demanding task; measure kernel distance (function-space movement vs linearized prediction) and boundary-F; map the regime diagram.
- **Main Risk:** Frozen backbone may blur the regimes; the empirical diagram is informative either way.
- **Research Cluster:** DYN

### IDEA-C-0091 — Label smoothing shrinks masks by a computable morphological offset
- **One-sentence idea:** Show that label smoothing in segmentation systematically contracts predicted masks by a boundary offset computable from the smoothing coefficient and local boundary contrast, and provide the closed-form unbiasing correction.
- **Problem:** Label smoothing is used for calibration but its geometric side effect on mask extent is unquantified, biasing area/volume estimates downstream.
- **Core Hypothesis (falsifiable):** The argmax boundary under smoothed training shifts inward by a distance predicted by a first-order analysis of the smoothed target crossing point, verified across smoothing coefficients and datasets; applying the inverse offset restores unbiased areas.
- **Why Important:** Volume/area bias matters clinically (tumor volumetry) and industrially; a principled correction beats re-training.
- **Why Possibly Novel:** Label smoothing analyses target calibration/confidence; the geometric mask-contraction law appears underived.
- **Minimal Experiment:** Train with smoothing ∈ {0, 0.05, 0.1, 0.2} on 2 datasets; measure signed boundary displacement vs prediction-contrast; compare to the derived formula; validate the correction on volume estimation.
- **Main Risk:** Interaction with Dice-type losses changes the analysis; scope to CE-family first.
- **Research Cluster:** DYN

### IDEA-C-0092 — Anti-phase precision/recall oscillations in long-tail fine-tuning
- **One-sentence idea:** Characterize periodic oscillations between rare-class precision and recall during long-tail dense training, testing whether the period is set by the resampling ratio and whether phase-aware checkpoint selection beats last/best-mIoU selection.
- **Problem:** Long-tail training curves oscillate; checkpoint choice effectively samples a random phase, adding unrecognized variance to reported results.
- **Core Hypothesis (falsifiable):** Rare-class precision and recall oscillate in anti-phase with a period proportional to the effective epoch length of rare-class resampling; selecting checkpoints at matched phase reduces cross-seed variance substantially and phase-averaged models beat either extreme.
- **Why Important:** Explains variance in long-tail results and yields a better selection/averaging rule.
- **Why Possibly Novel:** Oscillations are visible in logs everywhere but undocumented as a phenomenon with a mechanism and a selection fix.
- **Minimal Experiment:** Train LVIS-subset models with varied resampling ratios; spectrally analyze per-class precision/recall trajectories; test period scaling; compare checkpoint-selection policies.
- **Main Risk:** Oscillations may be aperiodic under some schedulers; characterize across schedulers.
- **Research Cluster:** DYN

### IDEA-C-0093 — Two clocks: interior metrics converge before boundary metrics, breaking early stopping
- **One-sentence idea:** Establish that interior-overlap metrics and boundary metrics converge on systematically different timescales across dense tasks, quantify the lag distribution, and derive corrected early-stopping rules.
- **Problem:** Early stopping monitors mIoU; if boundary quality converges later (the "second clock"), standard practice ships models with immature boundaries.
- **Core Hypothesis (falsifiable):** Across architectures/datasets, the boundary-metric convergence step exceeds the interior-metric convergence step by a consistent multiplicative factor; stopping by a boundary-aware criterion improves downstream boundary-sensitive applications at bounded extra cost.
- **Why Important:** A field-wide practice correction backed by a measured dynamical regularity (also underpins IDEA-C-0069's schedule design).
- **Why Possibly Novel:** Metric-specific convergence timescales are unreported; everyone logs them but nobody has systematized the lag.
- **Minimal Experiment:** Meta-analyze training logs from 20 fine-tuning runs (varied tasks); define convergence steps per metric; fit the lag factor distribution; validate a corrected stopping rule prospectively.
- **Main Risk:** Convergence definitions are threshold-sensitive; report robustness across thresholds.
- **Research Cluster:** DYN

### IDEA-C-0094 — Confidence-threshold pseudo-labeling creates self-locking gradient dead zones
- **One-sentence idea:** Test whether fixed-confidence-threshold pseudo-labeling in semi-supervised segmentation creates spatial regions that never exceed threshold and therefore never receive gradient — dead zones that self-perpetuate and are invisible in aggregate metrics.
- **Problem:** Thresholded self-training is standard; its fixed-point pathology (regions locked out of learning forever) is unexamined spatially.
- **Core Hypothesis (falsifiable):** Pixels below threshold at training start have a much higher probability of remaining below threshold throughout training than a calibrated-improvement null model predicts (self-locking); dead zones cluster on identifiable content (boundaries, rare textures); annealed or stochastic thresholds unlock them and recover accuracy specifically there.
- **Why Important:** Explains where semi-supervised methods fail and converts threshold scheduling from heuristic to principled.
- **Why Possibly Novel:** Confirmation bias is discussed class-wise; a spatial fixed-point (dead zone) analysis with locking statistics is new.
- **Minimal Experiment:** Instrument FixMatch-style segmentation training with per-pixel threshold-crossing histories; measure locking probabilities vs null; characterize dead-zone content; compare threshold schedules.
- **Main Risk:** Heavy logging; subsample pixels smartly.
- **Research Cluster:** DYN

### IDEA-C-0095 — Multi-scale training grows scale-specific subnetworks
- **One-sentence idea:** Test whether random-resize training causes VFM segmenters to develop functionally separable scale-specific subnetworks — prunable independently per scale — rather than scale-invariant features.
- **Problem:** Multi-scale augmentation is assumed to produce invariance; if it produces modular specialization instead, compression and adaptation strategies change.
- **Core Hypothesis (falsifiable):** Units/heads identified as important (by ablation saliency) at one test scale differ substantially from those at another scale; pruning scale-A-critical units leaves scale-B performance largely intact, violating the invariance account and confirming emergent modularity.
- **Why Important:** Enables scale-targeted pruning/adapters and revises the mental model of what multi-scale training does.
- **Why Possibly Novel:** Emergent modularity is studied in language models; a scale-axis modularity analysis in dense vision training is new.
- **Minimal Experiment:** Train with random-resize on ADE20K; compute per-unit ablation importance at 3 test scales; measure importance-set overlap; perform cross-scale pruning tests.
- **Main Risk:** Importance measures are noisy; use multiple attribution methods for agreement.
- **Research Cluster:** DYN
## Cluster DATA — Data-Centric Hypotheses (IDEA-C-0096 … IDEA-C-0130)

### IDEA-C-0096 — Annotator boundary noise is anisotropic: normal vs tangential error geometry
- **One-sentence idea:** Measure the geometry of human boundary-annotation errors (decompose into boundary-normal and boundary-tangential components) and exploit the anisotropy with a direction-weighted loss.
- **Problem:** Label-noise models for segmentation assume isotropic jitter; if errors are mostly normal-direction offsets with tangential smoothing, standard robust losses are mis-specified.
- **Core Hypothesis (falsifiable):** Multi-annotator data shows normal-direction error variance several times tangential variance, with a characteristic spatial correlation length along the boundary; a loss down-weighting normal-direction disagreement (matched to the measured covariance) improves generalization to consensus labels over isotropic robust losses.
- **Why Important:** Correctly-specified noise models are the foundation of learning from imperfect labels — the dominant regime in practice.
- **Why Possibly Novel:** Boundary noise is treated as scalar "annotation quality"; its directional covariance structure and a matched loss appear unexplored.
- **Minimal Experiment:** From multi-rater datasets (LIDC, multi-rater VOC subsets), compute signed distance residuals along consensus boundaries; fit the anisotropic covariance; train with matched vs isotropic noise-robust losses; evaluate against consensus.
- **Main Risk:** Consensus itself is biased; use held-out-rater evaluation as well.
- **Research Cluster:** DATA

### IDEA-C-0097 — 3D-inconsistency cleaning of slice-wise medical labels
- **One-sentence idea:** Quantify contradictions between adjacent-slice annotations in 3D medical datasets (labels violating anatomical continuity) and test whether consistency-based label cleaning improves 2D and 3D model training.
- **Problem:** Volumes are annotated slice-by-slice, producing physically impossible label sequences (organs flickering in/out) that models must average over.
- **Core Hypothesis (falsifiable):** A 3D total-variation/continuity score identifies label contradictions at a measurable rate in public datasets; retraining on continuity-projected labels improves held-out (independently annotated) accuracy, with the gain proportional to the dataset's measured inconsistency rate.
- **Why Important:** A dataset-side fix that transfers to every model trained on these widely-used volumes.
- **Why Possibly Novel:** Label cleaning exists per-slice; a cross-slice physical-consistency framework with gain-vs-inconsistency prediction is new.
- **Minimal Experiment:** Compute inter-slice label continuity metrics on AMOS/BTCV; project labels onto continuity constraints (3D morphological regularization); retrain nnU-Net-style baselines; compare on independently-annotated test cases.
- **Main Risk:** Pathological anatomy genuinely violates smoothness; use organ-specific constraint strengths.
- **Research Cluster:** DATA

### IDEA-C-0098 — Temporal-neighbor leakage audit for video-derived image datasets
- **One-sentence idea:** Audit image benchmarks assembled from video sources for temporally-adjacent frames landing in train and test, and quantify score inflation as a function of the temporal gap distribution.
- **Problem:** Frame-sampled datasets (driving, sports, wildlife) place near-identical viewpoints across splits, and nobody reports the temporal-gap distribution.
- **Core Hypothesis (falsifiable):** Embedding-retrieval identifies cross-split frame pairs with sub-minute temporal proximity in several popular datasets; per-image test performance is significantly higher for images with a close train neighbor, and the inflation decays smoothly with estimated temporal gap.
- **Why Important:** Produces a leakage-decay curve — a reusable calibration for how much proximity inflates dense metrics.
- **Why Possibly Novel:** Duplicate audits check exact/near duplicates; the graded temporal-distance analysis with an inflation curve is new.
- **Minimal Experiment:** Run cross-split retrieval on BDD/KITTI-derived sets; where timestamps exist, bin test images by nearest-train temporal gap; plot per-bin accuracy for several public models.
- **Main Risk:** Visual similarity confounds temporal proximity; control by matching similarity within bins.
- **Research Cluster:** DATA

### IDEA-C-0099 — Annotator fatigue leaves a within-session label-quality gradient
- **One-sentence idea:** Test whether annotation quality degrades within annotator work sessions (fatigue), producing a recoverable per-image quality covariate from timestamps that can weight training.
- **Problem:** All labels are weighted equally; if session position predicts noise level, a free quality signal is being ignored.
- **Core Hypothesis (falsifiable):** In datasets with annotation timestamps/order metadata, later-in-session masks show measurably higher disagreement with re-annotations (or lower vertex density, more shortcuts); training with session-position-based loss weighting improves over uniform weighting.
- **Why Important:** Introduces annotation-process metadata as a first-class training signal, at zero collection cost for future datasets.
- **Why Possibly Novel:** Fatigue is studied in HCI/crowdsourcing quality control; its exploitation as a training-loss covariate for dense labels is new.
- **Minimal Experiment:** Obtain order metadata (some open datasets publish it; otherwise run a small controlled annotation session); measure quality-vs-position; implement weighted training and compare.
- **Main Risk:** Order metadata is scarce; the controlled-collection fallback (20 annotator-hours) keeps it cheap.
- **Research Cluster:** DATA

### IDEA-C-0100 — Boundary-ownership bias: annotation order decides which class gets shared pixels
- **One-sentence idea:** Test whether the class annotated first systematically "owns" ambiguous boundary pixels in overlapping-object scenes, creating a directional label bias that models learn as depth/occlusion priors.
- **Problem:** Polygon layering resolves shared boundaries by annotation order, an arbitrary process variable that becomes systematic signal.
- **Core Hypothesis (falsifiable):** In datasets with layered annotation formats, boundary pixels between class pairs are assigned to one class at rates far from 50% in a direction predicted by typical annotation order (large/background-first), and models reproduce this ownership bias on held-out data even where true occlusion is reversed.
- **Why Important:** Reveals that occlusion-boundary "knowledge" in models may partly be annotation-pipeline archaeology.
- **Why Possibly Novel:** Occlusion reasoning is evaluated as capability; its confounding with annotation-order artifacts is unexamined.
- **Minimal Experiment:** Extract pairwise boundary-ownership statistics from COCO panoptic layering; verify with a small controlled re-annotation varying order; test model ownership predictions on physically-verified occlusion pairs.
- **Main Risk:** True occlusion statistics also favor certain directions; the controlled re-annotation isolates the process effect.
- **Research Cluster:** DATA

### IDEA-C-0101 — Crowd-vs-expert curvature bias transfers into models
- **One-sentence idea:** Quantify systematic shape-style differences between crowd-sourced and expert annotations of identical images (curvature smoothing, concavity avoidance) and show models inherit their trainer's style, measurable on neutral test sets.
- **Problem:** Datasets mix annotation workforces; "model style" differences across papers may be workforce artifacts.
- **Core Hypothesis (falsifiable):** On same-image dual annotations, crowd masks show lower curvature energy and fewer deep concavities than expert masks by consistent margins; models trained on each inherit these statistics (blind style classification of model outputs succeeds above chance).
- **Why Important:** Annotation workforce becomes a documented modeling decision, and style-transfer corrections become possible.
- **Why Possibly Novel:** Quality differences are studied as accuracy; style (shape-statistics) inheritance by models is new.
- **Minimal Experiment:** Collect dual crowd/expert annotations on 300 images (or use existing dual-source sets); compute shape-statistic contrasts; train matched models; classify output provenance on neutral images.
- **Main Risk:** Workforce differences confound with instruction differences; hold instructions fixed.
- **Research Cluster:** DATA

### IDEA-C-0102 — Missing-instance noise clusters at image borders
- **One-sentence idea:** Test whether unlabeled-object noise (instances annotators skipped) concentrates near image borders and partial visibility, and whether border-aware loss masking recovers the lost recall.
- **Problem:** Missing labels teach models to suppress detections in specific spatial/visibility conditions, but the spatial structure of missingness is unmeasured.
- **Core Hypothesis (falsifiable):** Exhaustive re-annotation of benchmark subsets shows missing-instance rates several times higher within a border band and for sub-50%-visible objects; training with spatially-weighted negative-loss masking (down-weighting background loss where missingness is likely) improves border recall without inflating false positives centrally.
- **Why Important:** A structural noise model beats generic label-noise handling, and border objects matter for robotics/driving safety.
- **Why Possibly Novel:** Missing labels are handled by pseudo-labeling; a measured spatial missingness prior driving the loss is new.
- **Minimal Experiment:** Exhaustively re-annotate 200 COCO images; map missingness spatially; implement missingness-weighted training on original labels; evaluate on the re-annotated set.
- **Main Risk:** Re-annotation is itself imperfect; use multiple annotators for the audit set.
- **Research Cluster:** DATA

### IDEA-C-0103 — Copy-paste augmentation harm is predictable from context dependence
- **One-sentence idea:** Test whether copy-paste augmentation helps context-free classes and hurts context-dependent classes, with the per-class effect predictable in advance from a context mutual-information score.
- **Problem:** Copy-paste is applied uniformly; its contradictory reported effects may hide a predictable per-class structure.
- **Core Hypothesis (falsifiable):** Per-class copy-paste gain correlates negatively with the class's context dependence (accuracy drop under background randomization, measured once on a baseline); a selective policy (paste only low-context-dependence classes) beats uniform copy-paste on the same budget.
- **Why Important:** Converts an unreliable augmentation into a targeted one via a one-time measurement.
- **Why Possibly Novel:** Copy-paste ablations report aggregates; the context-dependence predictor and selective policy are untested.
- **Minimal Experiment:** Measure per-class context dependence on COCO via background-swap probes; train uniform vs selective copy-paste; compare per-class deltas against predictions.
- **Main Risk:** Context dependence measured on one model may not transfer; verify with two probe models.
- **Research Cluster:** DATA

### IDEA-C-0104 — Hard-example mining mostly mines label errors
- **One-sentence idea:** Audit what fraction of pixels selected by online hard-example mining (OHEM) in mature training runs are actually mislabeled, testing whether "hard examples" become "wrong labels" as models improve.
- **Problem:** OHEM assumes high-loss pixels are informative; late in training they may be predominantly annotation errors, making mining actively harmful.
- **Core Hypothesis (falsifiable):** Expert re-adjudication of top-loss pixels shows the label-error fraction rises steeply with training progress (crossing 50% at a measurable point); switching OHEM off (or inverting to loss-capping) after that point improves final consensus-set accuracy.
- **Why Important:** Reverses a standard recipe component conditionally, with a measurable switch point.
- **Why Possibly Novel:** Noise-vs-hardness ambiguity is known abstractly; the temporal crossover measurement and schedule fix for dense mining are new.
- **Minimal Experiment:** During Cityscapes training, sample top-loss pixels at 5 checkpoints; adjudicate 500 per checkpoint against fine re-annotations; plot error fraction vs progress; test the schedule fix.
- **Main Risk:** Adjudication labor; keep samples small but statistically powered.
- **Research Cluster:** DATA

### IDEA-C-0105 — Near-duplicates inflate fine-tuning data scaling exponents
- **One-sentence idea:** Test whether measured data-scaling exponents for dense fine-tuning are substantially inflated by near-duplicate images, and establish deduplication-corrected scaling curves.
- **Problem:** "More data helps with exponent α" guides collection budgets, but web/clinical archives are duplicate-heavy, and duplicates contribute differently than fresh samples.
- **Core Hypothesis (falsifiable):** Scaling curves on deduplicated data show measurably different (steeper per-unique-image) exponents than raw data; the raw-data exponent is recoverable from the deduplicated one plus the duplication spectrum, validating a correction formula.
- **Why Important:** Data-collection economics (how much to gather) depend directly on the exponent; corrections change budget decisions.
- **Why Possibly Novel:** Deduplication is studied for memorization/privacy; its effect on dense-task scaling-law estimation is unmeasured.
- **Minimal Experiment:** Build scaling curves (5 sizes × 3 seeds) on raw vs deduplicated subsets of a large segmentation corpus with a measured duplication spectrum; fit exponents; test the correction formula on a second corpus.
- **Main Risk:** Deduplication thresholds are arbitrary; sweep them and report exponent sensitivity.
- **Research Cluster:** DATA

### IDEA-C-0106 — Coarse labels transfer better than fine labels at matched budget
- **One-sentence idea:** Test whether pretraining/auxiliary training on coarsely-labeled data (superclasses, rough masks) yields more transferable dense representations than the same annotation budget spent on fewer finely-labeled images.
- **Problem:** Annotation budgeting assumes finer is better; information-bottleneck reasoning suggests coarse labels may preserve more transfer-general structure per dollar.
- **Core Hypothesis (falsifiable):** At matched annotation cost (measured in annotator-seconds), coarse-label pretraining beats fine-label pretraining for transfer to novel classes/datasets, with the advantage growing with domain distance and reversing only for transfer to the same fine taxonomy.
- **Why Important:** Directly guides how organizations should spend annotation money for foundation-style reusability.
- **Why Possibly Novel:** Label granularity studies exist for classification hierarchy; the cost-normalized transfer comparison for dense labels is missing.
- **Minimal Experiment:** Using COCO with cost models from annotation-time literature, construct cost-matched coarse vs fine training sets; pretrain identical models; evaluate transfer to 4 target datasets at varied domain distance.
- **Main Risk:** Cost models are approximate; report results across plausible cost ratios.
- **Research Cluster:** DATA

### IDEA-C-0107 — Interpolated 3D labels leave frequency-domain fingerprints models learn
- **One-sentence idea:** Detect the through-plane frequency artifacts left by sparse-slice annotation with interpolation in 3D medical datasets, and test whether models learn to reproduce interpolation smoothness rather than true anatomy.
- **Problem:** Many volumes are labeled on every k-th slice and interpolated; the resulting labels are anatomically over-smooth in a spectrally detectable way.
- **Core Hypothesis (falsifiable):** Through-plane spectra of labels reveal interpolation (energy cutoff at 1/k) in identifiable public datasets; models trained on them produce under-complex 3D surfaces measurably closer to interpolation than to densely-annotated ground truth, and training with interpolation-aware masking (supervise only annotated slices) restores surface complexity.
- **Why Important:** Affects 3D shape fidelity everywhere sparse annotation was used — likely a large share of public volumetric data.
- **Why Possibly Novel:** Sparse annotation is a known practice; its spectral detectability and inherited-smoothness consequence are unquantified.
- **Minimal Experiment:** Spectral audit of public volumetric labels; identify interpolated datasets; train with full vs annotated-slice-only supervision; compare surface curvature spectra against densely-annotated references.
- **Main Risk:** True anatomy also varies in smoothness; use organs with known high-frequency structure as sentinels.
- **Research Cluster:** DATA

### IDEA-C-0108 — Depth-sensor shadows became negative-space labels
- **One-sentence idea:** Test whether datasets whose masks were derived from depth sensors carry sensor-shadow artifacts (missing returns at edges, reflective surfaces) as systematic label negative space that RGB models then learn.
- **Problem:** Depth-derived "ground truth" inherits sensor physics; RGB models trained on it learn to avoid regions where the depth sensor failed, not where objects end.
- **Core Hypothesis (falsifiable):** Label erosion patterns in depth-derived datasets align with predictable sensor-failure geometry (grazing angles, specular materials); RGB models trained on them under-segment shiny/edge regions on independent RGB-annotated test data, and physics-aware label dilation removes the deficit.
- **Why Important:** Sensor-transfer label bias is a general trap as auto-labeling from auxiliary sensors grows (depth, lidar, thermal).
- **Why Possibly Novel:** Depth noise is studied for depth tasks; its transformation into RGB segmentation label bias is unexamined.
- **Minimal Experiment:** Compare depth-derived vs human masks on overlapping data (e.g., indoor datasets with both); characterize erosion vs surface properties; train and evaluate on human-annotated tests with and without corrective dilation.
- **Main Risk:** Overlapping dual-annotation data is limited; small controlled captures suffice.
- **Research Cluster:** DATA

### IDEA-C-0109 — Cross-version label drift creates contradictory supervision
- **One-sentence idea:** Measure semantic and boundary drift between versions of long-lived datasets (re-annotations, guideline updates) and test whether training on mixed versions produces measurably averaged, internally contradictory boundary behavior.
- **Problem:** Practitioners mix dataset versions freely; if class definitions drifted, models are trained toward the average of two conventions.
- **Core Hypothesis (falsifiable):** Same-image cross-version label comparisons reveal systematic definition shifts for identifiable classes; models trained on mixed versions show bimodal boundary placement (matching neither convention) and higher boundary variance than single-version models on those classes.
- **Why Important:** Version hygiene becomes an evidence-backed requirement, and drift-aware training (version as conditioning variable) becomes motivated.
- **Why Possibly Novel:** Version differences are noted in changelogs; their measurable effect on trained-model boundary behavior is not documented.
- **Minimal Experiment:** Align same-image annotations across COCO/ADE version pairs; quantify per-class drift; train mixed vs pure models; compare boundary placement distributions on drifted classes.
- **Main Risk:** Version overlaps may be small; even a few hundred same-image pairs suffice for the drift audit.
- **Research Cluster:** DATA

### IDEA-C-0110 — Alt-text quality anti-correlates with visual difficulty
- **One-sentence idea:** Test whether web alt-text (the supervision source for VLMs) is systematically richer for visually easy images and near-absent for hard ones, creating a difficulty-dependent supervision gap that shapes what dense VLM features can do.
- **Problem:** Caption supervision is treated as unbiased-if-noisy; a difficulty-correlated sampling bias would explain why VLM features underperform precisely on hard content.
- **Core Hypothesis (falsifiable):** In public caption corpora, caption informativeness (length, object-word count) correlates negatively with image difficulty proxies (clutter, occlusion, low contrast); VLM dense-probe performance stratified by difficulty shows a steeper decline than supervised baselines, matching the supervision gap.
- **Why Important:** Locates a data-root cause for VLM dense-prediction weaknesses, motivating difficulty-targeted caption collection over more scale.
- **Why Possibly Novel:** Caption noise is studied as random; its structured correlation with visual difficulty and downstream dense consequences are new.
- **Minimal Experiment:** Score LAION-subset captions for informativeness and images for difficulty; measure the correlation; compare difficulty-stratified probe curves of CLIP vs supervised features on dense tasks.
- **Main Risk:** Difficulty proxies are imperfect; use several and human-validate a subset.
- **Research Cluster:** DATA

### IDEA-C-0111 — Predicting inter-annotator disagreement is a transferable skill
- **One-sentence idea:** Train models to predict per-pixel inter-annotator disagreement (not just labels) and test whether disagreement prediction transfers across datasets better than segmentation itself, providing a universal ambiguity channel.
- **Problem:** Disagreement is averaged away as noise, but it encodes reusable information about where visual evidence underdetermines labels.
- **Core Hypothesis (falsifiable):** A disagreement-prediction head trained on multi-rater dataset A predicts disagreement zones on unrelated multi-rater dataset B substantially above baseline (transfer), while segmentation heads transfer worse; using predicted disagreement to modulate losses on single-rater datasets improves their consensus-set accuracy.
- **Why Important:** Turns annotation noise from a nuisance into a portable supervision signal with immediate uses (loss weighting, active learning, calibration).
- **Why Possibly Novel:** Disagreement modeling exists per-dataset; the cross-dataset transferability claim — implying ambiguity is a general visual property — is untested.
- **Minimal Experiment:** Train disagreement predictors on LIDC; test zero-shot on multi-rater natural-image sets (and vice versa); apply predicted-disagreement loss weighting to a single-rater dataset and evaluate.
- **Main Risk:** Disagreement includes protocol-specific components; measure the transferable fraction honestly.
- **Research Cluster:** DATA

### IDEA-C-0112 — Upright-world pretraining makes VFMs orientation-brittle in predictable classes
- **One-sentence idea:** Quantify which visual concepts VFMs encode orientation-canonically (due to gravity-aligned pretraining photos) and predict, per class, the accuracy cost in orientation-free domains (aerial, microscopy, endoscopy).
- **Problem:** Rotation robustness is tested globally; a per-concept canonicality map would tell practitioners exactly which classes need rotation handling.
- **Core Hypothesis (falsifiable):** Per-class accuracy drop under test-time rotation correlates strongly with the orientation concentration of that class in pretraining-like corpora (measurable via pose statistics of retrieved examples); classes with orientation-diverse pretraining exposure are naturally robust without augmentation.
- **Why Important:** Replaces blanket rotation augmentation with targeted intervention and predicts failure classes for overhead/medical deployments a priori.
- **Why Possibly Novel:** Rotation equivariance is an architecture topic; the data-side per-concept canonicality census and its predictive use are new.
- **Minimal Experiment:** Measure orientation statistics of web-retrieved examples for 50 classes; evaluate frozen VFM probes under rotation per class; regress robustness on canonicality; validate predictions on aerial data.
- **Main Risk:** Retrieval-based orientation statistics are approximate; hand-verify a subset.
- **Research Cluster:** DATA

### IDEA-C-0113 — Display-resolution annotation causes a recoverable subpixel offset
- **One-sentence idea:** Test whether masks annotated on downscaled displays carry a systematic subpixel boundary offset (from annotators tracing at display resolution) recoverable as a global correction per dataset.
- **Problem:** Annotation tools show images below native resolution; the induced boundary bias is unknown, yet boundary metrics operate at native resolution.
- **Core Hypothesis (falsifiable):** Comparing annotations of the same images made at different display zoom levels reveals a consistent signed offset (and corner-rounding) proportional to the zoom factor; applying the inverse correction to existing dataset labels improves agreement with high-zoom re-annotations and changes boundary-metric model rankings at the margin.
- **Why Important:** A dataset-wide free accuracy fix at the boundary-metric scale where modern models compete.
- **Why Possibly Novel:** Annotation-tool effects are studied for speed/quality; the zoom-induced geometric bias with a correction protocol is new.
- **Minimal Experiment:** Controlled annotation of 100 images at 3 zoom levels; fit the offset model; apply to a benchmark's labels; re-evaluate model boundary metrics against corrected labels.
- **Main Risk:** Offset may vary with annotator and tool; model it hierarchically.
- **Research Cluster:** DATA

### IDEA-C-0114 — Tail-class boundary noise exceeds head-class noise, distorting long-tail conclusions
- **One-sentence idea:** Measure whether rare classes carry systematically noisier boundaries (annotators are less practiced at them) and re-evaluate long-tail methods against noise-corrected tail metrics.
- **Problem:** Long-tail method comparisons attribute tail errors to models; if tail labels are noisier, part of the measured tail gap is irreducible and method rankings are distorted.
- **Core Hypothesis (falsifiable):** Re-annotation shows tail-class boundary inter-rater variance exceeding head-class variance by a significant factor; adjusting tail metrics for the measured noise floor shrinks the head-tail model gap and reorders methods whose gains were within noise.
- **Why Important:** Corrects the empirical basis of an entire subfield's progress narrative.
- **Why Possibly Novel:** Long-tail work assumes label quality is frequency-independent; this assumption appears never audited.
- **Minimal Experiment:** Dual-annotate 50 head-class and 50 tail-class instances from LVIS; compare noise levels; propagate noise floors into published method comparisons via bootstrap.
- **Main Risk:** Tail instances are heterogeneous; sample across many tail classes.
- **Research Cluster:** DATA

### IDEA-C-0115 — Slice-level negative data scaling: identifying pretraining data that hurts dense tasks
- **One-sentence idea:** Test whether specific pretraining data slices (screenshots, documents, memes, watermarked stock) measurably harm dense-prediction transfer, making "more data" locally negative and slice-curation a principled science.
- **Problem:** Pretraining corpora are curated for classification-style quality; dense tasks may be hurt by slices that flatten spatial statistics, but slice-level attribution is missing.
- **Core Hypothesis (falsifiable):** Controlled pretraining runs with/without identified slices show that removing certain slices improves dense-probe transfer despite reducing data volume, with the harmful slices identifiable in advance by their spatial-statistics divergence from natural scenes.
- **Why Important:** Converts corpus curation from taste to measurement, potentially improving all future VFMs at negative cost.
- **Why Possibly Novel:** Data curation studies target classification quality/dedup; dense-transfer slice attribution with a predictive harm criterion is new.
- **Minimal Experiment:** Pretrain small MAE/DINO models on corpus variants (±screenshots, ±documents) at fixed compute; evaluate dense probes on 4 tasks; correlate harm with slice spatial statistics.
- **Main Risk:** Small-scale pretraining may not extrapolate; test two scales for trend consistency.
- **Research Cluster:** DATA

### IDEA-C-0116 — Capture metadata predicts label quality and should weight the loss
- **One-sentence idea:** Test whether image capture metadata (ISO, exposure, blur proxies) predicts annotation error rates — dark/blurry images being annotated worse — and whether metadata-conditioned loss weighting improves training.
- **Problem:** Label quality varies with image quality (annotators can't see what the sensor barely captured), yet this coupled noise is treated as uniform.
- **Core Hypothesis (falsifiable):** Re-annotation disagreement rates rise measurably with ISO/blur metrics in benchmarks with EXIF data; metadata-based per-image loss weighting (fit on a small audit set) yields consistent gains over uniform weighting, biggest on low-quality-image test slices.
- **Why Important:** A free, generalizable quality covariate available in most raw datasets before it is stripped.
- **Why Possibly Novel:** Image quality affects model input difficulty (studied); its effect on the labels themselves and use as a loss covariate is new.
- **Minimal Experiment:** Dual-annotate 300 images spanning quality metadata; fit disagreement vs metadata; train weighted vs uniform on a metadata-rich dataset; evaluate on quality-stratified test slices.
- **Main Risk:** Metadata missing in processed datasets; use no-reference quality metrics as fallback covariates.
- **Research Cluster:** DATA

### IDEA-C-0117 — Annotated frames are motion-selected: the still-frame bias in video datasets
- **One-sentence idea:** Test whether frames chosen for annotation in video datasets are systematically low-motion (annotators/tools prefer sharp frames), leaving models untrained and untested on motion blur despite deployment on continuous video.
- **Problem:** Frame-selection procedures create a blur-free training and evaluation world; deployment sees every frame.
- **Core Hypothesis (falsifiable):** Optical-flow magnitude distributions of annotated frames are significantly shifted toward stillness vs random frames in the same videos; per-frame model accuracy on unannotated in-between frames (verified by propagated labels) drops sharply with flow magnitude, exceeding what image-quality alone predicts.
- **Why Important:** Quantifies a deployment gap invisible to every existing video benchmark and motivates blur-representative annotation sampling.
- **Why Possibly Novel:** Motion blur robustness is studied with synthetic blur; the dataset-construction selection bias and its measured field consequence are new.
- **Minimal Experiment:** Compare flow statistics of annotated vs random frames in DAVIS/YouTube-VOS source videos; evaluate models on label-propagated high-motion frames; fit accuracy-vs-flow curves.
- **Main Risk:** Propagated labels on blurry frames are imperfect; use conservative propagation with manual spot checks.
- **Research Cluster:** DATA

### IDEA-C-0118 — Synthetic data lacks occlusion-type diversity, not realism
- **One-sentence idea:** Test whether the sim2real gap for segmentation is driven more by missing occlusion-configuration diversity (types of partial views) than by appearance realism, using an occlusion-taxonomy census of synthetic vs real datasets.
- **Problem:** Sim2real work optimizes photorealism; if the binding constraint is occlusion diversity, that effort is misallocated.
- **Core Hypothesis (falsifiable):** A taxonomy census (occluder class, fraction, boundary type) shows synthetic datasets cover far fewer occlusion configurations than real data; enriching synthetic occlusion diversity at fixed (low) realism closes more of the real-test gap than increasing realism at fixed occlusion diversity.
- **Why Important:** Redirects synthetic-data investment from renderers to scene-composition logic — much cheaper.
- **Why Possibly Novel:** Domain randomization touches this implicitly; an explicit occlusion-taxonomy accounting with a controlled realism-vs-diversity comparison is new.
- **Minimal Experiment:** Census occlusion configurations in GTA-style vs Cityscapes data; generate low-realism/high-occlusion-diversity synthetic variants; train the 2×2 (realism × diversity) grid; evaluate on real data.
- **Main Risk:** Occlusion taxonomy design choices; validate the census against human judgments on a sample.
- **Research Cluster:** DATA

### IDEA-C-0119 — Test-set era drift: old benchmarks measure old annotation conventions
- **One-sentence idea:** Test whether models trained on modern data are penalized on decade-old test sets for following current annotation conventions, quantifying convention drift as a component of measured "progress" and "gaps."
- **Problem:** The community treats old test sets as fixed rulers, but the ruler encodes its era's labeling conventions (class definitions, boundary styles, exhaustiveness norms).
- **Core Hypothesis (falsifiable):** Re-annotating old test subsets under modern conventions changes absolute scores substantially and method gaps moderately; the discrepancy between old-convention and new-convention scores has grown over model generations (modern models increasingly agree with modern conventions).
- **Why Important:** Grounds cross-era comparisons and "superhuman" claims in convention-aware measurement.
- **Why Possibly Novel:** Individual re-annotation efforts exist (e.g., for classification test sets); a convention-drift decomposition for dense benchmarks over time is new.
- **Minimal Experiment:** Re-annotate 200 images of an old benchmark under current guidelines; score historical model generations against both versions; plot the convention-agreement trend.
- **Main Risk:** Guideline reconstruction for old datasets is partly speculative; document assumptions explicitly.
- **Research Cluster:** DATA

### IDEA-C-0120 — Device-class (phone vs DSLR) is a scale confounder masquerading as domain
- **One-sentence idea:** Test whether apparent domain gaps between consumer-photo and professional-photo datasets are substantially explained by focal-length/working-distance-induced object-scale and perspective distributions rather than appearance.
- **Problem:** Domain adaptation methods are deployed on gaps that may be mostly geometric (scale/perspective statistics), which requires different fixes than appearance adaptation.
- **Core Hypothesis (falsifiable):** Matching object-scale and perspective distributions via cropping/warping between two "domains" closes a large fraction of the transfer gap without any appearance adaptation; the residual gap correlates with measured appearance statistics.
- **Why Important:** Provides a decomposition protocol that should precede any domain-adaptation effort (fix geometry first, adapt appearance second).
- **Why Possibly Novel:** Scale augmentation is universal, but the diagnosis-first decomposition of named benchmark gaps into geometry vs appearance is not practiced.
- **Minimal Experiment:** Between two photo-source-distinct datasets with shared classes, apply distribution-matching crops; measure gap closure; compare with appearance-only adaptation (style transfer) at matched effort.
- **Main Risk:** Cropping alters context availability; include context-preserving rescale controls.
- **Research Cluster:** DATA

### IDEA-C-0121 — Hole conventions (fill vs preserve) are inconsistent within datasets
- **One-sentence idea:** Audit mask-hole handling (donut holes, handle gaps, occluder cutouts) for within-dataset inconsistency and measure how much boundary/topology metrics are corrupted by convention noise rather than model error.
- **Problem:** Whether enclosed background regions belong to the mask is decided inconsistently by annotators, and topology-aware methods are evaluated against this noise.
- **Core Hypothesis (falsifiable):** Hole-handling consistency within popular datasets is measurably low for identifiable object types (mugs, chairs, bikes); topology-metric differences between published methods are smaller than the convention-noise floor for those types, invalidating topology-based ranking claims there.
- **Why Important:** Topology-aware segmentation is a growing subfield whose evaluation may rest on annotation coin flips.
- **Why Possibly Novel:** Hole conventions are unmentioned in dataset papers; nobody has measured their consistency or metric impact.
- **Minimal Experiment:** Automatically detect enclosed-background configurations in COCO/ADE; audit consistency per object type; bootstrap the convention-noise floor into topology-metric comparisons of 4 methods.
- **Main Risk:** Automated hole detection needs care with true multi-part objects; human-verify samples.
- **Research Cluster:** DATA

### IDEA-C-0122 — Unlabeled-pool cleanliness beats quantity in semi-supervised segmentation
- **One-sentence idea:** Test whether semi-supervised segmentation gains scale more strongly with unlabeled-data cleanliness (absence of out-of-distribution and corrupted images) than with unlabeled quantity, establishing exchange rates between the two.
- **Problem:** Practitioners maximize unlabeled pool size; if a small fraction of OOD contamination negates volume gains, curation should precede collection.
- **Core Hypothesis (falsifiable):** Controlled contamination curves (fraction of OOD/corrupt images × pool size) show gain iso-contours where removing contamination is worth large multiples of added clean data, with the exchange rate consistent across two methods.
- **Why Important:** Provides the missing quantitative guidance for the most common practical semi-supervised decision.
- **Why Possibly Novel:** OOD-in-unlabeled-data is studied as a failure mode; the quantity-cleanliness exchange-rate framing with measured iso-contours is new.
- **Minimal Experiment:** On VOC with a web-image contamination source, run a (contamination × size) grid for FixMatch-style training; fit the gain surface; extract exchange rates.
- **Main Risk:** Contamination type matters; test two contamination sources (near-domain and far-domain).
- **Research Cluster:** DATA

### IDEA-C-0123 — CT window settings silently scope label validity
- **One-sentence idea:** Test whether CT annotations are only valid under the intensity window the annotator viewed, by measuring how structure boundaries move across windows and whether models trained at mismatched windows inherit systematic offsets.
- **Problem:** CT display windowing changes visible boundaries (soft tissue vs bone windows); labels encode the viewing window, but training pipelines choose windows independently.
- **Core Hypothesis (falsifiable):** Annotating identical structures under different standard windows yields measurable systematic boundary offsets for identifiable structure types; training with a window different from the annotation window reproduces the offset as model bias, and matching windows removes it.
- **Why Important:** A pervasive, unmentioned medical pipeline mismatch with a zero-cost fix (record and match the annotation window).
- **Why Possibly Novel:** Windowing is discussed for model input normalization; its role in defining what the labels mean is unexamined.
- **Minimal Experiment:** Have annotators segment 50 structures under 3 windows each; quantify offsets; train models with matched vs mismatched windows on public data with known annotation-window conventions; measure inherited bias.
- **Main Risk:** Annotation-window provenance is often undocumented; the controlled study establishes the effect size regardless.
- **Research Cluster:** DATA

### IDEA-C-0124 — Polysemous class names corrupt specific directions of VLM embedding space
- **One-sentence idea:** Test whether visually polysemous words in caption supervision ("mouse", "crane", "bat") create measurably corrupted text-embedding directions whose dense-grounding quality is predictably below monosemous controls.
- **Problem:** Open-vocab dense prediction relies on class-name embeddings; polysemy mixes incompatible visual modes into single directions, but the damage is unquantified.
- **Core Hypothesis (falsifiable):** For frequency-matched polysemous/monosemous word pairs, dense grounding accuracy is systematically lower for polysemous words; the deficit correlates with the visual-mode mixture entropy measured from retrieved images, and sense-disambiguated prompts (added context words) recover a predictable fraction.
- **Why Important:** Quantifies a structural supervision defect and validates cheap prompt-side mitigation for practitioners.
- **Why Possibly Novel:** Polysemy is a known nuisance; its measured geometry (mixture entropy → grounding deficit law) for dense prediction is new.
- **Minimal Experiment:** Build frequency-matched word pair lists; evaluate open-vocab segmenters on datasets containing both senses; measure mixture entropy via image retrieval clustering; test disambiguation prompts.
- **Main Risk:** Frequency matching is imperfect; use multiple corpora for frequency estimates.
- **Research Cluster:** DATA

### IDEA-C-0125 — Scribbles are skeleton-biased, and models inherit a free medial-axis prior
- **One-sentence idea:** Test whether human scribble annotations concentrate near object medial axes, and whether scribble-supervised models therefore learn implicit skeleton estimators — extractable as a free byproduct capability.
- **Problem:** Scribble supervision is treated as sparse random labels; if placement is systematically skeletal, models learn geometry beyond class labels that nobody exploits or accounts for.
- **Core Hypothesis (falsifiable):** Scribble-to-medial-axis distance distributions are far from uniform-placement nulls across scribble datasets; features of scribble-trained models linearly decode medial axes significantly better than mask-trained counterparts, and this skeleton prior explains their documented shape-regularization behavior.
- **Why Important:** Reveals hidden information content in a popular weak-supervision form and yields a free skeleton estimator for downstream shape tasks.
- **Why Possibly Novel:** Scribble methods focus on propagating labels; the placement-bias measurement and inherited-capability claim are new.
- **Minimal Experiment:** Measure scribble-medial-axis statistics on ScribbleSup-style data; train scribble vs mask models; probe both for skeleton decoding on held-out shapes.
- **Main Risk:** Scribble tools/instructions vary; analyze per-source.
- **Research Cluster:** DATA

### IDEA-C-0126 — Annotation-tool edge magnetism makes labels gradient-biased
- **One-sentence idea:** Test whether edge-snapping annotation tools systematically pull labels toward image gradients, teaching models to trust gradients and fail on true low-contrast boundaries — a tool-induced bias distinguishable from human perception limits.
- **Problem:** Modern tools snap contours to edges for speed; the resulting labels over-align with gradients relative to true object extent, especially where boundaries are smooth.
- **Core Hypothesis (falsifiable):** Same-image annotations made with snapping on vs off differ systematically (snapped labels sit on gradient maxima; unsnapped sit at perceived boundaries); models trained on snapped labels show a measurable performance cliff on low-gradient boundary segments that unsnapped-trained models don't have.
- **Why Important:** As tool-assisted labeling scales, this bias compounds into VFM training data; measuring it now informs tool design and correction.
- **Why Possibly Novel:** Tool-assisted labeling is evaluated for speed/agreement; the gradient-bias inheritance chain into model failure modes is untested.
- **Minimal Experiment:** Annotate 200 images with snapping on/off (counterbalanced annotators); quantify gradient alignment differences; train matched models; evaluate on low-contrast boundary test segments.
- **Main Risk:** Unsnapped annotation is slower/noisier; separate bias from variance in the comparison.
- **Research Cluster:** DATA

### IDEA-C-0127 — Resampling-kernel mismatches between repos create phantom method differences
- **One-sentence idea:** Audit popular dataset-loading pipelines for divergent resize implementations (antialiasing, kernel choice, corner alignment) and quantify how much cross-paper performance difference these silently generate for dense tasks.
- **Problem:** The "same benchmark" differs numerically across frameworks; dense metrics are boundary-sensitive to resampling details nobody reports.
- **Core Hypothesis (falsifiable):** Common loader configurations produce label/image misalignments up to the half-pixel scale and measurable metric differences on identical checkpoints; a fraction of typical claimed improvements is within the cross-loader variation band.
- **Why Important:** A reproducibility audit with a concrete checklist fix (declare and standardize resampling), directly protecting comparison validity.
- **Why Possibly Novel:** Resize-implementation differences are documented in image-quality contexts; their dense-benchmark metric impact and cross-paper contamination estimate are new.
- **Minimal Experiment:** Evaluate 5 public checkpoints under 6 loader configurations spanning real framework defaults; report per-model metric spread vs typical published deltas.
- **Main Risk:** None substantive — worst case documents that pipelines are consistent, itself valuable.
- **Research Cluster:** DATA

### IDEA-C-0128 — Straight-line laziness in stuff-boundary annotation
- **One-sentence idea:** Measure excess straightness in "stuff" region boundaries (sky/tree, road/sidewalk transitions) relative to image evidence, testing whether annotator tessellation shortcuts became learned model behavior.
- **Problem:** Diffuse stuff transitions get annotated with a few straight segments; models trained on them may reproduce polygonal boundaries where reality is fractal.
- **Core Hypothesis (falsifiable):** Stuff-stuff boundaries in popular datasets show straightness statistics incompatible with underlying image-gradient structure (excess long straight runs); model outputs inherit the excess straightness, and it persists even on synthetic scenes with known fractal boundaries — confirming learned convention over evidence.
- **Why Important:** Stuff boundaries feed free-space estimation in robotics/driving; polygonal artifacts there are safety-relevant.
- **Why Possibly Novel:** Boundary quality audits target objects; stuff-boundary annotation geometry appears never characterized.
- **Minimal Experiment:** Compute run-length/curvature statistics of stuff boundaries vs gradient-following nulls in ADE/Cityscapes; test model outputs for inherited straightness on natural and synthetic fractal-boundary scenes.
- **Main Risk:** Some stuff boundaries are genuinely straight (curbs); condition the analysis on boundary type.
- **Research Cluster:** DATA

### IDEA-C-0129 — Site label-protocol variance dominates site image variance in federated medical data
- **One-sentence idea:** Decompose multi-site medical segmentation heterogeneity into image-distribution differences vs annotation-protocol differences, testing whether the protocol component dominates — reframing federated personalization as label harmonization.
- **Problem:** Federated methods personalize models to site "domains" assuming pixel-level shift; if the dominant shift is in labeling conventions, image-side adaptation is aimed at the wrong target.
- **Core Hypothesis (falsifiable):** Cross-site experiments with exchanged annotators (site-A annotators label site-B images) show that annotator provenance explains more cross-site performance variance than image provenance for identifiable structures; harmonizing labels (mapping between protocols) beats image-side adaptation at equal effort.
- **Why Important:** Redirects a major medical-ML engineering effort from model adaptation to protocol reconciliation.
- **Why Possibly Novel:** Site effects are treated monolithically; the annotator-exchange decomposition design is rarely if ever executed.
- **Minimal Experiment:** With two collaborating sites (or public dual-annotated data), build the 2×2 (image source × annotator source) matrix on shared cases; decompose variance; test label-mapping vs image-adaptation interventions.
- **Main Risk:** Requires modest new annotation; 2×2 on 50 cases suffices for the variance decomposition.
- **Research Cluster:** DATA

### IDEA-C-0130 — Binary tumor labels destroy recoverable infiltration-gradient information
- **One-sentence idea:** Test whether the intensity structure inside "boundary-adjacent" tumor regions contains recoverable infiltration-gradient information that binarized labels discard, by reformulating segmentation as boundary-zone regression.
- **Problem:** Tumor margins are biologically gradual (infiltration), but annotation forces a binary line, training models to hallucinate sharp boundaries and discard clinically-relevant gradation.
- **Core Hypothesis (falsifiable):** Models trained to regress a soft infiltration proxy (constructed from multi-rater label distributions and image intensity profiles) predict the spatial spread of rater disagreement and, where available, histopathology-verified extension better than calibrated binary-model probabilities do.
- **Why Important:** Better margin characterization affects radiotherapy planning and resection margins — direct clinical value from a label-format change.
- **Why Possibly Novel:** Soft/probabilistic labels exist for uncertainty; grounding the soft target in infiltration biology and validating against extension ground truth is a different claim.
- **Minimal Experiment:** On multi-rater glioma data (BraTS-style), build soft margin targets; train regression vs binary+calibration; evaluate disagreement-spread prediction and, on any registered-pathology subset, extension accuracy.
- **Main Risk:** Histopathology-registered validation data is scarce; the rater-disagreement endpoint alone still tests the core recoverability claim.
- **Research Cluster:** DATA
## Cluster ECON — Compute/Economics Hypotheses That Become Scientific (IDEA-C-0131 … IDEA-C-0150)

### IDEA-C-0131 — A rank-vs-dataset-size law makes PEFT's regularization quantitative
- **One-sentence idea:** Establish an empirical law relating optimal LoRA rank to fine-tuning dataset size for dense tasks, testing whether PEFT beats full FT on small data specifically because constrained update dimension acts as a data-matched regularizer.
- **Problem:** "PEFT is cheaper and sometimes better" conflates economics with statistics; the better needs a quantitative mechanism.
- **Core Hypothesis (falsifiable):** Optimal rank r* scales as a power law in labeled-pixel count N across tasks (r* ∝ N^α with consistent α); at r*, PEFT matches or beats full FT below a predictable N threshold and loses above it, with the crossover computable from the fitted law.
- **Why Important:** Turns the field's most common adaptation decision into a formula, and reframes PEFT's benefit as measurable capacity control.
- **Why Possibly Novel:** Rank ablations exist per-paper; a cross-task scaling law with a full-FT crossover prediction for dense prediction is absent.
- **Minimal Experiment:** Grid (rank × dataset size) on 5 segmentation tasks with subsampled training sets; locate r*(N); fit the law; validate the crossover prediction on 2 held-out tasks.
- **Main Risk:** r* may be flat/noisy on some tasks; report law fit quality honestly per task family.
- **Research Cluster:** ECON

### IDEA-C-0132 — The marginal-FLOP frontier: when adaptation compute beats pretraining compute
- **One-sentence idea:** Measure the iso-accuracy exchange rate between pretraining FLOPs and adaptation FLOPs for dense tasks, testing whether the optimal split shifts predictably with pretraining-target similarity.
- **Problem:** Organizations choose between using bigger pretrained models vs adapting longer with no quantitative exchange rate.
- **Core Hypothesis (falsifiable):** Iso-accuracy contours in (pretrain-FLOPs, adapt-FLOPs) space have slopes that vary systematically with a measurable pretrain-target similarity score (frozen-feature transfer accuracy), such that beyond a similarity threshold, marginal adaptation FLOPs dominate marginal pretraining FLOPs by an order of magnitude.
- **Why Important:** The most common industrial compute decision gets a measured decision boundary instead of folklore.
- **Why Possibly Novel:** Scaling laws exist for pretraining alone; the joint pretrain-adapt allocation frontier for dense tasks with a similarity covariate is unmapped.
- **Minimal Experiment:** Use checkpoint families with multiple pretraining budgets (open ViT/MAE series); adapt each at multiple budgets on 4 targets of varying similarity; fit contours and slope-vs-similarity.
- **Main Risk:** Public checkpoint series confound budget with recipe; supplement with small controlled pretraining runs.
- **Research Cluster:** ECON

### IDEA-C-0133 — A capability-gap law for when dense distillation pays
- **One-sentence idea:** Test whether distillation efficiency for segmentation (student gain per teacher-inference FLOP) collapses onto a single curve governed by the teacher-student capability gap, giving a pre-computable go/no-go rule for distillation projects.
- **Problem:** Distillation sometimes transfers little; teams discover this only after spending the teacher-inference budget.
- **Core Hypothesis (falsifiable):** Across teacher-student pairs, student improvement is a non-monotone function of the capability gap (measured by frozen-probe difference), peaking at intermediate gaps and collapsing for large ones, with the curve stable enough across datasets to predict outcomes from the gap alone.
- **Why Important:** Converts a costly trial-and-error decision into a one-measurement prediction.
- **Why Possibly Novel:** Gap effects are noted in classification distillation; a quantitative predictive curve for dense prediction with FLOP accounting is new.
- **Minimal Experiment:** Distill across a 4×4 teacher-student grid on 2 segmentation datasets; plot gain vs measured gap; test curve transfer to a third dataset.
- **Main Risk:** "Capability gap" needs a robust operationalization; compare several candidates.
- **Research Cluster:** ECON

### IDEA-C-0134 — Task ambiguity decides the inference-vs-training compute tradeoff
- **One-sentence idea:** Test whether the crossover between spending compute at inference (prompt/augmentation ensembling) vs training (tuning) is governed by measurable task ambiguity, with ambiguous tasks favoring inference-time compute for a mechanistic reason (multimodal posterior averaging).
- **Problem:** Teams choose between test-time ensembling and fine-tuning by habit; a task-property-based rule is missing.
- **Core Hypothesis (falsifiable):** At matched total FLOPs, ensembling beats tuning precisely on tasks with high output ambiguity (multi-rater disagreement, multimodal SAM outputs), and the advantage size correlates with measured ambiguity across tasks; on low-ambiguity tasks the ordering reverses.
- **Why Important:** A deployment-relevant allocation rule grounded in why averaging helps (posterior multimodality), not just that it does.
- **Why Possibly Novel:** TTA-vs-tuning comparisons exist ad hoc; the ambiguity covariate as the governing variable is untested.
- **Minimal Experiment:** On 6 tasks with measured ambiguity (from multi-rater or multi-mask statistics), compare iso-FLOP ensembling vs LoRA tuning; regress the advantage on ambiguity.
- **Main Risk:** FLOP matching across paradigms requires care; publish the accounting.
- **Research Cluster:** ECON

### IDEA-C-0135 — The segmentation iso-FLOP frontier prefers resolution over parameters
- **One-sentence idea:** Map the accuracy iso-FLOP frontier over (model size, input resolution) for segmentation and test whether it is resolution-dominated — opposite to classification — because boundary information scales with pixels, not parameters.
- **Problem:** Model-scaling intuitions imported from classification may misallocate dense-prediction compute budgets.
- **Core Hypothesis (falsifiable):** At fixed FLOPs, segmentation accuracy (especially boundary metrics) is maximized at smaller-model/higher-resolution combinations than classification accuracy is, with the frontier shift largest for boundary-F and smallest for interior IoU — localizing the mechanism in boundary information density.
- **Why Important:** Directly changes how practitioners size models for dense workloads at every budget.
- **Why Possibly Novel:** Resolution-vs-size tradeoffs are studied for classification efficiency; a metric-decomposed dense-task frontier with the boundary-information account is missing.
- **Minimal Experiment:** Train a (4 sizes × 4 resolutions) grid at matched FLOPs on ADE20K; plot frontiers per metric; replicate the classification frontier on the same backbones for contrast.
- **Main Risk:** Attention FLOPs scale quadratically with resolution, complicating matching; use windowed variants and exact FLOP accounting.
- **Research Cluster:** ECON

### IDEA-C-0136 — Gradient concentration predicts when sparse fine-tuning suffices
- **One-sentence idea:** Test whether the success of sparse fine-tuning (updating a tiny weight subset) is predicted by the natural concentration of fine-tuning gradients in weight space, measured in one epoch — making "how few weights can I train" a measurement, not a search.
- **Problem:** Sparse-FT methods report wins on some tasks and losses on others with no a-priori signal for which regime applies.
- **Core Hypothesis (falsifiable):** The Gini coefficient of accumulated gradient magnitudes over one epoch predicts (rank correlation across ≥10 tasks) the accuracy retention of top-k% sparse fine-tuning, and the relationship is stable enough to choose k in advance within a factor of 2.
- **Why Important:** Saves search compute for every adaptation project and connects sparse-FT to a measurable property of the task-model pair.
- **Why Possibly Novel:** Sparse-FT selection criteria exist (magnitude, Fisher); using early gradient concentration as a predictive law across dense tasks is untested.
- **Minimal Experiment:** For 10 task-model pairs, measure epoch-1 gradient concentration; run sparse FT at k ∈ {0.1%..10%}; fit retention-vs-concentration; validate on held-out pairs.
- **Main Risk:** Concentration may shift during training; test predictor stability across measurement epochs.
- **Research Cluster:** ECON

### IDEA-C-0137 — Backpropagating through augmentations is the hidden value of unfrozen backbones
- **One-sentence idea:** Test whether a major benefit of full fine-tuning over cached-feature adaptation comes specifically from augmentations being processed through the backbone (fresh features per augmented view), separable from weight plasticity itself.
- **Problem:** Cached frozen features make adaptation cheap but silently change the learning problem (one feature per image, no augmentation diversity in feature space); the cost of this is unquantified.
- **Core Hypothesis (falsifiable):** A three-arm comparison — (a) cached features, (b) frozen backbone with per-augmentation recomputed features, (c) full FT — shows (b) recovers a large fraction of the (a)→(c) gap at frozen weights, isolating augmentation-through-backbone as a distinct value source with its own compute-vs-accuracy exchange rate.
- **Why Important:** Reframes the caching decision: teams may buy most of full-FT's benefit by paying inference (not training) compute on augmented views.
- **Why Possibly Novel:** Frozen-vs-tuned comparisons never isolate this factor; the decomposition is simple and missing.
- **Minimal Experiment:** Run the three arms on 4 segmentation tasks at matched adapter/head capacity; report gap decomposition and FLOP accounting.
- **Main Risk:** Feature-space augmentation baselines could partially substitute; include them as a fourth arm.
- **Research Cluster:** ECON

### IDEA-C-0138 — Per-pixel compute demand is predictable from local label entropy
- **One-sentence idea:** Test whether the compute needed to classify each pixel correctly (measured by early-exit depth) is predictable from local label entropy statistics, yielding a principled per-pixel compute-allocation law rather than heuristic early-exit thresholds.
- **Problem:** Adaptive-compute segmentation uses confidence heuristics; a data-property law would make efficiency predictable at design time.
- **Core Hypothesis (falsifiable):** In early-exit segmenters, the exit depth required per pixel correlates strongly with dataset-level local label entropy (boundary density, class confusability maps) computed without the model; total-compute savings for a target accuracy are then predictable from dataset statistics alone within a small error.
- **Why Important:** Enables pre-deployment compute budgeting per dataset and explains where adaptive methods can and cannot save.
- **Why Possibly Novel:** Early-exit methods exist; the model-free predictability claim (entropy → compute map) is a scientific step beyond engineering.
- **Minimal Experiment:** Train a multi-exit segmenter on 3 datasets; extract per-pixel required depth; regress on precomputed label-entropy maps; test the budget-prediction formula on a fourth dataset.
- **Main Risk:** Required depth depends on architecture; test two exit architectures for law stability.
- **Research Cluster:** ECON

### IDEA-C-0139 — Quantization noise attacks boundaries first: a bit-width/boundary law
- **One-sentence idea:** Characterize how post-training quantization degrades segmentation as a function of bit width, testing whether errors concentrate on boundary pixels with a predictable onset — so interior-serving applications can quantize far more aggressively than boundary-serving ones.
- **Problem:** Quantization decisions use aggregate accuracy; dense consumers care about spatially heterogeneous degradation nobody has mapped.
- **Core Hypothesis (falsifiable):** Across models/datasets, boundary-F degrades at a bit width 2+ bits higher than interior IoU does, with the boundary-error onset predictable from activation dynamic range statistics near boundary pixels; mixed-precision schemes protecting boundary-relevant layers recover boundary quality at near-uniform-low-bit cost.
- **Why Important:** Gives deployment engineers a metric-specific quantization rule and localizes why boundaries are numerically fragile.
- **Why Possibly Novel:** Quantization studies report mIoU; the spatial decomposition with an onset law and targeted mixed-precision fix is new.
- **Minimal Experiment:** Quantize 4 public segmenters at 8/6/4/3 bits; report interior-vs-boundary degradation curves; correlate onset with activation statistics; test the targeted mixed-precision scheme.
- **Main Risk:** Quantizer choice matters; use two standard PTQ methods.
- **Research Cluster:** ECON

### IDEA-C-0140 — One-percent-compute fine-tune outcome prediction
- **One-sentence idea:** Build and validate a predictor of final fine-tuning accuracy from statistics measurable at ~1% of the training budget (feature-space class geometry, early loss curvature), testing whether dense-task adaptation outcomes are determined early enough for cheap model selection.
- **Problem:** Choosing among candidate backbones/PEFT configs requires full training runs, multiplying costs by the candidate count.
- **Core Hypothesis (falsifiable):** A regression on early observables predicts final mIoU within a small margin (sufficient to rank candidates correctly in most cases) across a diverse task suite, and the predictor transfers to unseen backbone families with modest degradation.
- **Why Important:** Order-of-magnitude savings on the ubiquitous model-selection loop, plus insight into how early outcomes are determined.
- **Why Possibly Novel:** Learning-curve extrapolation exists; a dense-task-specific predictor exploiting feature-geometry observables (not just loss curves) at the 1% mark is untested.
- **Minimal Experiment:** For 40 (backbone × PEFT × dataset) combos, log early observables and final accuracy; fit/cross-validate the predictor; report ranking accuracy vs full-training selection.
- **Main Risk:** Late-training phenomena (IDEA-C-0093's second clock) may cap predictability for boundary metrics; report per-metric limits.
- **Research Cluster:** ECON

### IDEA-C-0141 — Optimal data-pruning fraction is set by pretrain-target similarity
- **One-sentence idea:** Test whether the fraction of fine-tuning data that can be pruned without accuracy loss is predictable from pretrain-target feature similarity — similar targets tolerate aggressive pruning because the backbone already encodes most examples' content.
- **Problem:** Data pruning for fine-tuning uses per-example scores requiring full-data passes and mysterious task-dependent keep-ratios.
- **Core Hypothesis (falsifiable):** The lossless-pruning fraction across tasks correlates strongly with frozen-feature transfer accuracy (similarity proxy); the relationship predicts safe pruning ratios for new tasks within useful tolerance, and pruning beyond it harms boundary metrics before interior metrics.
- **Why Important:** Annotation and training budgets shrink predictably where similarity is high — an economics decision made scientific.
- **Why Possibly Novel:** Pruning-score literature optimizes which examples; the how-many-as-a-function-of-similarity law is unaddressed.
- **Minimal Experiment:** On 8 tasks spanning similarity levels, sweep keep-ratios with a standard pruning score; locate lossless thresholds; fit and validate the similarity law.
- **Main Risk:** Pruning-score choice may interact with the law; verify with two scores.
- **Research Cluster:** ECON

### IDEA-C-0142 — Annotation-ROI curves for clicks vs scribbles vs masks cross at predictable scales
- **One-sentence idea:** Measure accuracy-per-annotation-second curves for click, scribble, box, and full-mask supervision at multiple dataset scales, testing whether the optimal annotation type switches at predictable scale thresholds — making labeling-strategy selection a computable decision.
- **Problem:** Teams pick an annotation modality once and keep it; if ROI curves cross with scale, the optimal strategy is stage-dependent and currently nobody knows the crossing points.
- **Core Hypothesis (falsifiable):** Weak modalities dominate ROI at small budgets and are overtaken by dense masks at a budget threshold that is predictable from class boundary complexity; mixed schedules (weak-first, dense-later) beat any pure strategy at equal cost.
- **Why Important:** Direct, quantitative guidance for every dataset-building effort — the most expensive part of applied vision.
- **Why Possibly Novel:** Individual weak-supervision papers claim efficiency; a unified cost-normalized crossing-point analysis across modalities and scales is missing.
- **Minimal Experiment:** Using published annotation-time models and one small timing study, train across (modality × budget) grids on 2 datasets; map ROI curves and crossings; test the mixed schedule.
- **Main Risk:** Annotation-time models vary across workforces; report sensitivity to cost assumptions.
- **Research Cluster:** ECON

### IDEA-C-0143 — Perimeter statistics govern token-dropping efficiency for segmentation
- **One-sentence idea:** Test whether the achievable compute saving from inference-time token dropping in ViT segmenters is governed by dataset perimeter statistics (total boundary length per image), giving a closed-form efficiency bound per dataset.
- **Problem:** Token-reduction papers report savings on particular datasets; deployment needs to predict savings on new data without experiments.
- **Core Hypothesis (falsifiable):** Accuracy-preserving token-keep ratios across datasets collapse onto a single function of measured perimeter density (boundary tokens must be kept; interior tokens are droppable), predicting per-dataset savings within a small margin from label statistics alone — or from cheap edge-detector statistics when labels are absent.
- **Why Important:** Converts an engineering trick into a predictable resource law usable at procurement time.
- **Why Possibly Novel:** Content-aware token pruning exists; the dataset-level predictive law framed on perimeter statistics is new.
- **Minimal Experiment:** Apply boundary-aware token dropping to 5 datasets with measured perimeter densities; fit keep-ratio-vs-perimeter; validate prediction on 2 more datasets using edge statistics only.
- **Main Risk:** Long-range context needs may force keeping some interior tokens; the residual defines the law's error bar.
- **Research Cluster:** ECON

### IDEA-C-0144 — Texture-defined classes are TTA-compressible; shape-defined classes are not
- **One-sentence idea:** Test whether small models with test-time augmentation match large models specifically on texture-defined classes while failing on shape-defined classes at iso-FLOPs, because TTA averages texture noise but cannot supply missing long-range shape integration.
- **Problem:** "Small+TTA ≈ large" claims are made at dataset level; if the equivalence is class-type-dependent, deployment substitutions are unsafe for shape-critical applications.
- **Core Hypothesis (falsifiable):** Classifying benchmark classes into texture-vs-shape-defined (via texture-scramble sensitivity), the small+TTA vs large gap concentrates almost entirely in shape-defined classes across datasets, and grows with the shape-integration range required.
- **Why Important:** A mechanistic boundary for a common compute-saving substitution, protecting shape-critical uses (medical margins, industrial geometry).
- **Why Possibly Novel:** TTA and scaling are both studied; the class-definition-type interaction hypothesis is untested.
- **Minimal Experiment:** Score classes by texture-scramble sensitivity; compare small+TTA vs large at iso-FLOPs on ADE/Cityscapes; report gap by class type.
- **Main Risk:** Class-type scoring is a continuum; use it as a covariate, not a dichotomy.
- **Research Cluster:** ECON

### IDEA-C-0145 — Log-rank growth: optimal LoRA rank scales logarithmically with data
- **One-sentence idea:** Test the specific functional form that optimal LoRA rank grows logarithmically (not polynomially) with fine-tuning data volume for dense tasks, implying a hard economic sweet spot where extra rank is wasted beyond log-scale growth.
- **Problem:** IDEA-C-0131 establishes a law exists; the functional form matters for extrapolating to large adaptation datasets.
- **Core Hypothesis (falsifiable):** Across 2 orders of magnitude of data, r*(N) fits log growth significantly better than power laws with α > 0.2, implying most adaptation information content saturates a low-dimensional update subspace; direct subspace-overlap measurements between r* solutions at different N confirm nested structure.
- **Why Important:** Log growth means adaptation memory/serving costs stay near-constant with data scale — a strong economic statement with a representational explanation.
- **Why Possibly Novel:** No published functional-form fits for rank-data scaling in dense adaptation exist to our knowledge; claims are anecdotal.
- **Minimal Experiment:** Extend the IDEA-C-0131 grid to wider N ranges on 3 tasks; run model comparison (log vs power) on r*(N); measure update-subspace nesting across N.
- **Main Risk:** r* plateaus could reflect optimization limits rather than information saturation; control with longer training at high ranks.
- **Research Cluster:** ECON

### IDEA-C-0146 — Progressive-resolution fine-tuning exploits the two-clock structure for free savings
- **One-sentence idea:** Test whether low-to-high-resolution fine-tuning schedules save large compute fractions with no boundary-quality loss precisely because interior semantics converge early (cheap at low resolution) and boundaries converge late (only the tail needs full resolution).
- **Problem:** Resolution schedules exist as engineering tricks; connecting them to metric-specific convergence timescales would make savings predictable and principled.
- **Core Hypothesis (falsifiable):** A schedule spending the interior-convergence phase (predicted from IDEA-C-0093's lag factor) at quarter resolution matches full-resolution training on all metrics at a large FLOP saving, and the achievable saving is predictable from the measured metric-lag factor per dataset.
- **Why Important:** Immediately deployable savings with a dynamics-grounded design rule instead of hand tuning.
- **Why Possibly Novel:** Progressive resizing is known (classification training recipes); the boundary-clock-based design rule and prediction of savings for dense tasks is new.
- **Minimal Experiment:** Measure per-dataset metric-lag factors; run predicted vs naive vs full-resolution schedules on 3 datasets; verify iso-accuracy and predicted savings.
- **Main Risk:** Resolution changes interact with BN/PE adaptation transients (IDEA-C-0084); include transition-annealing controls.
- **Research Cluster:** ECON

### IDEA-C-0147 — Task-gradient cosine predicts when shared adapters pay off
- **One-sentence idea:** Test whether the economics of sharing one adapter across multiple dense tasks (vs one adapter each) is governed by inter-task gradient cosine similarity measured cheaply upfront, with a critical similarity threshold below which sharing always loses.
- **Problem:** Multi-task adapter sharing halves serving costs when it works, but failures are discovered only after joint training.
- **Core Hypothesis (falsifiable):** Across task pairs, shared-adapter accuracy retention correlates strongly with epoch-1 inter-task gradient cosine on the adapter parameters; a threshold rule chosen on one task pool transfers to a held-out pool with high decision accuracy.
- **Why Important:** A one-epoch measurement replaces combinatorial joint-training experiments for multi-tenant serving decisions.
- **Why Possibly Novel:** Gradient conflict is a multi-task-learning topic; its use as a predictive economic decision rule for adapter consolidation is new.
- **Minimal Experiment:** For 15 task pairs, measure early gradient cosine and joint-vs-separate outcomes; fit the threshold; validate on 5 held-out pairs.
- **Main Risk:** Cosine at epoch 1 may drift; test predictor timing sensitivity.
- **Research Cluster:** ECON

### IDEA-C-0148 — Retrieval beats fine-tuning below a dataset-intrinsic-dimension threshold
- **One-sentence idea:** Test whether nearest-neighbor label transfer over frozen VFM features (retrieval-based segmentation) beats any fine-tuning at small dataset sizes, with the crossover N predictable from the dataset's intrinsic dimension in feature space.
- **Problem:** Teams fine-tune reflexively even at tiny data scales where non-parametric transfer may dominate — but nobody knows where the boundary lies or what controls it.
- **Core Hypothesis (falsifiable):** The retrieval-vs-fine-tuning crossover point across tasks scales with feature-space intrinsic dimension (estimated by standard ID estimators): low-ID tasks favor retrieval up to large N, high-ID tasks favor fine-tuning almost immediately, and the fitted relationship predicts held-out task crossovers.
- **Why Important:** Retrieval systems are trivially updatable and auditable; knowing when they dominate changes deployment architecture, not just accuracy.
- **Why Possibly Novel:** Retrieval baselines appear in few-shot work; the intrinsic-dimension-governed crossover law is untested.
- **Minimal Experiment:** Implement dense retrieval segmentation (per-patch kNN + label transfer) on 8 tasks; sweep N against LoRA fine-tunes; estimate IDs; fit and validate the crossover law.
- **Main Risk:** Retrieval performance depends on the transfer mechanism (patch vs region); standardize one strong variant.
- **Research Cluster:** ECON

### IDEA-C-0149 — The free-adaptation floor: what CPU-only adaptation always buys
- **One-sentence idea:** Quantify the "free adaptation floor" — the fraction of full fine-tuning's domain-shift gain recoverable by CPU-feasible adaptation (normalization statistics + linear head on cached features) — testing whether this floor is stable across shift types and predictable.
- **Problem:** Many deployments (edge, clinical, air-gapped) cannot GPU-fine-tune; knowing the guaranteed-recoverable fraction changes what's promised and planned.
- **Core Hypothesis (falsifiable):** Across a broad shift suite, the floor is substantial and clusters by shift type (photometric shifts: high fraction; semantic shifts: low), with the per-case floor predictable from a cheap shift-type classifier — enabling pre-deployment guarantees.
- **Why Important:** Establishes deployment-planning numbers for the compute-constrained majority of real users, and cleanly decomposes what adaptation actually requires gradients through the backbone.
- **Why Possibly Novel:** Each cheap technique is known; the systematic floor measurement, shift-type structure, and predictive framing are not.
- **Minimal Experiment:** For 12 shift scenarios, compare frozen, CPU-adapted, and full-FT models; tabulate floor fractions by shift type; build and validate the floor predictor.
- **Main Risk:** "CPU-feasible" boundaries are fuzzy; define a strict compute budget and stick to it.
- **Research Cluster:** ECON

### IDEA-C-0150 — Perimeter-to-area ratio predicts when correcting SAM beats annotating from scratch
- **One-sentence idea:** Test whether the economic crossover between correcting model-proposed masks and annotating from scratch is governed by object perimeter-to-area ratio (correction cost scales with erroneous boundary length; scratch cost with total perimeter), yielding a per-object routing rule.
- **Problem:** Assisted annotation pipelines apply one workflow to all objects; if the optimal workflow flips by object geometry, budgets are silently wasted.
- **Core Hypothesis (falsifiable):** Measured per-object correction times exceed scratch-annotation times exactly for objects above a perimeter-complexity threshold (given current model quality); a geometry-based router (choose workflow per object from a cheap complexity estimate) reduces total annotation time significantly versus either pure workflow.
- **Why Important:** Direct cost savings for every SAM-assisted labeling operation, and a quantitative model linking assistance value to object geometry and model quality.
- **Why Possibly Novel:** Assisted-annotation studies report average speedups; the geometry-governed routing rule and its crossover model are new.
- **Minimal Experiment:** Small timing study (3 annotators × 300 objects spanning complexity) under both workflows; fit the crossover model; simulate/validate router savings on a full dataset's geometry distribution.
- **Main Risk:** Annotator skill variance; use within-annotator paired design.
- **Research Cluster:** ECON
## Cluster XFER — Cross-Field Transplants With a Mechanism (IDEA-C-0151 … IDEA-C-0180)

### IDEA-C-0151 — CTC-style forced alignment for image-level labels to pixels
- **One-sentence idea:** Transplant speech recognition's forced-alignment mechanism (CTC's monotonic latent alignment) to weakly-supervised segmentation by treating scanline label sequences as utterances to be aligned to pixel columns.
- **Problem:** Image-level and ordered-region labels (e.g., "sky above trees above road") carry alignment structure that CAM-style methods ignore entirely.
- **Core Hypothesis (falsifiable):** For scenes with known vertical class ordering (driving, landscapes, document layouts), a CTC-style column-wise alignment loss on ordered label sequences recovers pixel boundaries with accuracy approaching scribble supervision, because the monotonicity constraint supplies the localization information that image-level labels lack.
- **Why Important:** Ordered weak labels are nearly free to collect (class lists in spatial order) and the mechanism — marginalizing over all monotone alignments — is exactly what dense weak supervision is missing.
- **Why Possibly Novel:** CAM/erasure dominates weak supervision; explicit alignment-marginalization losses from speech appear untransplanted to pixel labeling.
- **Minimal Experiment:** On Cityscapes with vertical-order label sequences derived from ground truth (simulating cheap annotation), train a CTC-column loss model; compare against CAM-based weak supervision and scribbles at matched annotation cost.
- **Main Risk:** Monotonicity holds only along specific directions/scene types; scope to structured scenes and measure violation rates.
- **Research Cluster:** XFER

### IDEA-C-0152 — Motif discovery (EM over position weight matrices) for recurring defect discovery
- **One-sentence idea:** Transplant genomics motif-discovery (unsupervised EM for recurring subsequences in noise) to industrial imagery for discovering recurring defect appearance patterns without labels.
- **Problem:** Industrial defects recur in families (same die scratch, same weld pore signature), but anomaly detection treats each anomaly independently, discarding recurrence structure.
- **Core Hypothesis (falsifiable):** An EM procedure alternating between defect-template estimation and soft assignment over image patches (the PWM mechanism, adapted to feature space) discovers recurring defect families with higher purity than clustering post-hoc anomaly detections, and improves few-shot defect classification when families are used as pseudo-classes.
- **Why Important:** Recurrence is the exploitable structure in manufacturing data; the mechanism (probabilistic template EM under a background model) is mature elsewhere and directly matched.
- **Why Possibly Novel:** Anomaly clustering exists; the explicit background-model-plus-template EM formulation with genomics-style significance testing (motif enrichment) is new to inspection.
- **Minimal Experiment:** On MVTec-AD-style data pooled across products, run feature-space motif EM; compare family purity against DBSCAN-on-detections; test pseudo-class pretraining value.
- **Main Risk:** Feature-space templates may be less identifiable than sequence motifs; validate identifiability on synthetic planted defects.
- **Research Cluster:** XFER

### IDEA-C-0153 — Error-correcting output structure for mask tokens
- **One-sentence idea:** Transplant channel-coding redundancy (parity constraints) into mask decoding: predict masks plus parity codes over mask token groups so that decoding can detect and correct single-token corruption, improving robustness to input perturbations.
- **Problem:** Mask decoders fail unpredictably under perturbation; there is no mechanism for detecting that an output region is internally inconsistent.
- **Core Hypothesis (falsifiable):** Training decoders to emit parity-consistent auxiliary outputs (XOR-like constraints over region indicator functions) enables inference-time inconsistency detection that flags erroneous regions with useful precision, and parity-based correction recovers a measurable fraction of corruption-induced errors at minimal compute overhead.
- **Why Important:** Brings the detect-then-correct reliability mechanism of communications into dense prediction, where silent failure is the norm.
- **Why Possibly Novel:** Redundant output coding exists for classification (ECOC); a spatial parity formulation for segmentation with correction (not just detection) is new.
- **Minimal Experiment:** Add parity heads to a segmenter on Cityscapes; corrupt inputs (noise, patches); measure error-detection ROC and post-correction accuracy vs plain and ensemble baselines at matched compute.
- **Main Risk:** Parity heads may just learn the same features (correlated failures); enforce decorrelation via structured group design and measure it.
- **Research Cluster:** XFER

### IDEA-C-0154 — Compressed-sensing click budgets: recovery conditions predict required prompts
- **One-sentence idea:** Apply compressed-sensing recovery theory to interactive segmentation: treat clicks as measurements of a mask sparse in a wavelet/shape basis, and test whether CS recovery conditions predict the click budget needed per object.
- **Problem:** Nobody can predict how many clicks an object needs; interactive budgeting is empirical.
- **Core Hypothesis (falsifiable):** The minimum click count for accurate SAM segmentation correlates strongly with the object's mask compressibility (coefficient decay rate in a wavelet basis), following the qualitative form of CS sampling bounds (clicks ∝ sparsity × log factors), and this predicts per-object NoC better than area or perimeter.
- **Why Important:** A theory-grounded predictor of interaction cost enables annotation pricing, batch planning, and principled click-placement design.
- **Why Possibly Novel:** CS theory is used for image reconstruction; casting prompt budgets as a sampling-complexity problem with empirical validation is new.
- **Minimal Experiment:** For 2k objects, compute mask compressibility; record simulator NoC with SAM; regress NoC on compressibility vs geometric baselines; test prediction transfer across datasets.
- **Main Risk:** Clicks are adaptive measurements (not random projections), so CS bounds are analogies; frame claims as empirical correlation with a mechanism-inspired form.
- **Research Cluster:** XFER

### IDEA-C-0155 — Backdoor adjustment for scene-context confounding in segmentation evaluation
- **One-sentence idea:** Transplant epidemiology's causal adjustment (backdoor criterion) into benchmark analysis: estimate class-segmentation performance de-confounded from scene context by stratified reweighting over an explicit causal graph.
- **Problem:** Per-class metrics mix object recognition with scene-context inference (IDEA-C-0041 measures the floor; this idea corrects estimates causally).
- **Core Hypothesis (falsifiable):** Treating scene type as a confounder (scene → context cues; scene → class presence) and reweighting evaluation across scene strata yields per-class scores that predict cross-dataset transfer performance substantially better than raw scores — validating the causal adjustment as measuring transportable skill.
- **Why Important:** Introduces transportability-oriented evaluation: scores that predict performance elsewhere, the actual quantity practitioners need.
- **Why Possibly Novel:** Causal evaluation frameworks exist in fairness/medicine; applying identification-based adjustment to dense-vision benchmarks with transfer-prediction validation is new.
- **Minimal Experiment:** Build the scene-stratified estimator on ADE20K; compute adjusted vs raw per-class scores for 6 models; test which better predicts the same classes' performance on 3 other datasets.
- **Main Risk:** The causal graph is contestable; run sensitivity analysis over graph variants.
- **Research Cluster:** XFER

### IDEA-C-0156 — Annotator-PSF deconvolution of label noise
- **One-sentence idea:** Transplant astronomy's point-spread-function deconvolution: model each annotator as a boundary-blurring PSF estimable from repeated annotations, then deconvolve dataset labels to sharper consensus estimates before training.
- **Problem:** Averaging multi-rater labels blurs boundaries; the blur is treated as irreducible instead of an estimable instrument response.
- **Core Hypothesis (falsifiable):** Annotator boundary responses are stable, estimable kernels (per annotator, per boundary-contrast level); deconvolving labels with estimated PSFs produces training targets that yield models with better agreement to high-effort reference annotations than models trained on raw averages.
- **Why Important:** Recovers boundary resolution from existing noisy data — the astronomy playbook of getting sharper images than your instrument.
- **Why Possibly Novel:** Rater models exist (confusion matrices for classes); a spatial instrument-response formulation with deconvolution for boundaries is new.
- **Minimal Experiment:** Estimate per-rater kernels from LIDC-style repeated annotations; deconvolve; train on raw-average vs deconvolved targets; evaluate against expert-panel reference contours.
- **Main Risk:** PSF stationarity may fail across image content; fit contrast-conditional kernels.
- **Research Cluster:** XFER

### IDEA-C-0157 — Item response theory for benchmark items and model abilities
- **One-sentence idea:** Transplant psychometrics' item response theory (IRT) to dense benchmarks: jointly estimate per-image difficulty/discrimination and per-model ability, yielding adaptive test subsets and ability estimates robust to test composition.
- **Problem:** Benchmarks average over items as if equally informative; model comparisons are hostage to test-set composition, and evaluation cost scales with test size.
- **Core Hypothesis (falsifiable):** A 2-parameter IRT fit on per-image model outcomes across many public models yields ability rankings that are stable under item resampling (unlike mean-mIoU rankings), identifies low-discrimination items (noise), and enables adaptive testing that recovers full-test rankings from a small fraction of items.
- **Why Important:** Cheaper, more stable, composition-robust evaluation — psychometrics solved this decades ago for human testing.
- **Why Possibly Novel:** IRT has touched NLP benchmark analysis; a dense-prediction instantiation with continuous outcomes and adaptive-testing validation is new.
- **Minimal Experiment:** Collect per-image IoU for 30 public models on ADE20K val; fit IRT (with continuous-response link); compare ranking stability and adaptive-test efficiency vs standard averaging.
- **Main Risk:** Model population is small and correlated (shared architectures); model family as a random effect.
- **Research Cluster:** XFER

### IDEA-C-0158 — Kalman-filtered normalization statistics for streaming adaptation
- **One-sentence idea:** Transplant Kalman filtering to test-time adaptation on video streams: treat normalization statistics as latent states with process noise (scene drift) and measurement noise (per-frame estimation error), replacing heuristic momentum with optimal filtering.
- **Problem:** Streaming TTA uses fixed-momentum running stats, which lag during fast drift and overreact during noise — the exact tradeoff Kalman filters optimize.
- **Core Hypothesis (falsifiable):** A Kalman formulation with drift/noise parameters identified online yields normalization estimates that track ground-truth batch statistics with lower error than any fixed momentum, translating into higher segmentation accuracy on drift-heavy streams (weather transitions, tunnel entries) with provable non-divergence under bounded drift.
- **Why Important:** Replaces the most fragile component of streaming adaptation with a mechanism carrying optimality and stability guarantees.
- **Why Possibly Novel:** Momentum tuning for streaming BN is ad hoc in the literature; the state-space formulation with online noise identification appears absent.
- **Minimal Experiment:** On driving videos with injected drift events, compare Kalman-filtered vs fixed-momentum normalization adaptation on frozen segmenters; measure statistic-tracking error and downstream accuracy.
- **Main Risk:** Layer-wise statistics are high-dimensional; use diagonal approximations and verify they suffice.
- **Research Cluster:** XFER

### IDEA-C-0159 — Weight-statistics phylogenetics for model provenance and contamination
- **One-sentence idea:** Transplant phylogenetic tree inference to model populations: reconstruct fine-tuning ancestry from weight statistics, testing whether shared ancestry (undisclosed common checkpoints) explains correlated benchmark errors across "independent" methods.
- **Problem:** Benchmark comparisons assume method independence, but many models descend from common checkpoints, correlating their errors and inflating consensus confidence.
- **Core Hypothesis (falsifiable):** Distance metrics on weight/feature statistics reconstruct known ancestry (validated on documented lineages) with high accuracy; applying the tree to leaderboard model populations shows error correlation increasing with inferred relatedness, quantifying how much apparent method diversity is genealogical illusion.
- **Why Important:** Ensemble and consensus-based claims (and benchmark-progress narratives) depend on independence that this would directly measure.
- **Why Possibly Novel:** Model-lineage detection exists for licensing/forensics; the population-genetics framing linking relatedness to error correlation on benchmarks is new.
- **Minimal Experiment:** Build validation lineages (fine-tune trees with known topology); test reconstruction; apply to 30 public segmentation checkpoints; regress pairwise error correlation on inferred relatedness.
- **Main Risk:** Convergent training (same data) mimics ancestry; include data-overlap covariates.
- **Research Cluster:** XFER

### IDEA-C-0160 — Nucleation theory for region growing: energy barriers predict click efficacy
- **One-sentence idea:** Transplant nucleation theory from materials science to interactive segmentation: model mask growth from a click as nucleation-and-growth over an image-defined energy landscape, where barrier heights predict which clicks succeed.
- **Problem:** Click placement advice is heuristic; a physical model of when a seed "takes" vs stalls would make placement principled.
- **Core Hypothesis (falsifiable):** Defining an energy landscape from local feature affinity, the barrier between click-seeded and full-object states predicts single-click IoU across objects better than distance-to-boundary heuristics, and optimal click positions computed as minimum-barrier seeds beat centroid clicking in simulator and human tests.
- **Why Important:** A predictive physical theory for interaction design, plus interpretable failure diagnosis (which barrier blocked growth).
- **Why Possibly Novel:** Region growing is classical, but the nucleation framing with barrier computation as a click-quality predictor for modern promptable models is new.
- **Minimal Experiment:** Compute affinity landscapes from frozen VFM features; estimate barriers for candidate clicks on 1k objects; correlate with SAM single-click outcomes; test minimum-barrier click policy.
- **Main Risk:** SAM's decoder is not literal region growth; the theory is a surrogate — its predictive power is exactly what's tested.
- **Research Cluster:** XFER

### IDEA-C-0161 — Mark-recapture estimation of missing annotations
- **One-sentence idea:** Transplant ecology's mark-recapture population estimation to dataset auditing: use overlapping independent annotation passes as "captures" to estimate the total number of unlabeled instances without exhaustive re-annotation.
- **Problem:** Missing-annotation rates (IDEA-C-0102) are usually estimated by expensive exhaustive re-annotation; ecology solved abundance estimation from partial sightings a century ago.
- **Core Hypothesis (falsifiable):** Applying capture-recapture estimators (with heterogeneity models for object detectability) to two or three cheap independent annotation passes yields missing-instance estimates that match exhaustive re-annotation ground truth within tight confidence intervals, at a fraction of the cost.
- **Why Important:** Makes dataset-completeness auditing affordable and statistically principled for every dataset maintainer.
- **Why Possibly Novel:** Capture-recapture appears in epidemiology and software-defect estimation; its application to vision annotation completeness with detectability heterogeneity is new.
- **Minimal Experiment:** On 200 images with exhaustive reference annotation, run 3 independent quick passes; apply heterogeneous capture-recapture estimators; compare estimates and CIs to ground truth; publish the audit protocol.
- **Main Risk:** Annotator passes aren't independent (shared salience biases); use heterogeneity-robust estimators and quantify dependence.
- **Research Cluster:** XFER

### IDEA-C-0162 — CFAR detection for anomaly segmentation with guaranteed false-alarm rates
- **One-sentence idea:** Transplant radar's constant-false-alarm-rate (CFAR) detection into anomaly segmentation: threshold anomaly scores adaptively against locally-estimated background statistics to deliver calibrated, guaranteed false-positive rates per region.
- **Problem:** Anomaly segmentation thresholds are set globally on validation data, so false-alarm rates vary wildly across textures and scenes — unacceptable for inspection deployment.
- **Core Hypothesis (falsifiable):** CFAR-style local normalization of anomaly scores (order-statistics-based, as in radar) achieves empirical false-positive rates within a small factor of the design rate uniformly across texture strata, where global thresholds deviate by orders of magnitude, at equal or better detection power.
- **Why Important:** Delivers the deployment property inspection actually needs (guaranteed FAR), imported with its established theory.
- **Why Possibly Novel:** Local normalization appears informally; the explicit CFAR formulation with distribution-free order-statistic guarantees for dense anomaly maps is new.
- **Minimal Experiment:** Apply CA-CFAR/OS-CFAR post-processing to anomaly maps from standard detectors on MVTec-AD; measure per-texture FPR stability and detection-power curves vs global thresholds.
- **Main Risk:** Spatially correlated scores violate radar independence assumptions; use block-based order statistics and verify calibration empirically.
- **Research Cluster:** XFER

### IDEA-C-0163 — Sequence alignment as an annotation-style-robust boundary metric
- **One-sentence idea:** Transplant bioinformatics sequence alignment (affine-gap Smith-Waterman) to boundary evaluation: score predicted vs ground-truth contours by optimal alignment with gap penalties, making metrics robust to annotation-style differences that corrupt distance-based boundary scores.
- **Problem:** Boundary metrics (BF-score, Hausdorff) conflate style mismatches (vertex density, smoothing) with real errors (IDEA-C-0040 shows rankings flip); alignment with gaps distinguishes local offsets from structural misses.
- **Core Hypothesis (falsifiable):** An alignment-based contour metric with tuned gap penalties ranks method outputs more consistently across annotation styles (higher cross-style rank correlation than BF/Hausdorff) while preserving sensitivity to true structural errors (validated on synthetic error taxonomies).
- **Why Important:** Gives the community a boundary metric that survives the annotation-style problem the CONF cluster documents.
- **Why Possibly Novel:** Curve alignment exists in shape analysis; a gap-penalty formulation designed and validated for style-robust benchmark ranking is new.
- **Minimal Experiment:** Implement contour alignment scoring; evaluate ranking stability across the two-style re-annotations of IDEA-C-0040 (or synthetic style transforms); test sensitivity on planted structural errors.
- **Main Risk:** Gap-penalty tuning could hide real errors; calibrate penalties on the synthetic taxonomy first.
- **Research Cluster:** XFER

### IDEA-C-0164 — Replica-theory phase diagram for PEFT generalization
- **One-sentence idea:** Transplant statistical-mechanics replica analysis of low-rank learning to PEFT: derive and test a phase diagram (rank × data × noise) predicting where LoRA generalization transitions between under-parameterized, benign, and overfitting regimes.
- **Problem:** PEFT generalization behavior (why moderate ranks generalize best at some data scales) lacks theory; statistical physics has exact asymptotics for related low-rank estimation problems.
- **Core Hypothesis (falsifiable):** A replica-derived phase diagram for low-rank adaptation of a linearized model predicts the qualitative locations of empirical LoRA phase boundaries (double-descent-like ridges in rank-data space) measured on real dense-task fine-tunes, including the shift of boundaries with label noise level.
- **Why Important:** Would give PEFT its first predictive theory, unifying the ECON cluster's empirical laws under a mechanism.
- **Why Possibly Novel:** Replica methods cover matrix factorization and shallow networks; mapping them to PEFT-on-frozen-VFM with empirical dense-task validation is new.
- **Minimal Experiment:** Derive the phase diagram for low-rank adaptation of a random-feature model; measure empirical generalization surfaces over (rank × data × injected label noise) on 2 segmentation tasks; compare boundary topology.
- **Main Risk:** Real VFM features violate random-feature assumptions; the test is whether qualitative topology survives — stated as the falsifiable claim.
- **Research Cluster:** XFER

### IDEA-C-0165 — Cartographic generalization as semantics-aware label-scale augmentation
- **One-sentence idea:** Transplant cartography's map-generalization rules (feature simplification under scale change with semantic constraints: preserve connectivity, collapse-but-don't-delete) as the correct way to generate multi-scale training labels, replacing naive mask downsampling.
- **Problem:** Multi-scale training downsamples labels by interpolation, destroying thin structures and topology in ways cartographers explicitly solved for maps.
- **Core Hypothesis (falsifiable):** Models trained with cartographic label generalization at low scales (topology-preserving simplification) retain measurably better thin-structure and connectivity performance at full scale than interpolation-downsampled training, with the gain concentrated on classes cartographic rules protect (linear features, small salient objects).
- **Why Important:** A principled fix for a silent lossy step present in nearly every dense-training pipeline.
- **Why Possibly Novel:** Label downsampling is treated as an implementation detail; importing the formal generalization operators (with their semantic constraint hierarchy) is new.
- **Minimal Experiment:** Implement topology-preserving label simplification; train multi-scale models with cartographic vs interpolated labels on road/vessel datasets; compare connectivity metrics at full resolution.
- **Main Risk:** Cartographic operators need per-class configuration; start with the linear-feature subset where rules are clearest.
- **Research Cluster:** XFER

### IDEA-C-0166 — Negative selection (immune-inspired) for open-set pixel flagging
- **One-sentence idea:** Transplant immunology's negative-selection principle — train detectors on "self" and flag everything that no self-detector claims — as an anti-modular mechanism for open-set segmentation over frozen VFM features.
- **Problem:** Open-set segmentation methods model outliers directly or calibrate confidence, both of which fail when unknowns resemble knowns; negative selection instead certifies coverage of the known.
- **Core Hypothesis (falsifiable):** A dense ensemble of simple self-region detectors (covering the known-class feature manifold with local hyperspheres, immune-algorithm style) flags unknown-class pixels with better coverage-precision tradeoffs than softmax/energy baselines specifically for near-distribution unknowns, because detection is by non-membership rather than low confidence.
- **Why Important:** Near-distribution unknowns are the practically dangerous case (new defect types, rare pathologies); a coverage-complement mechanism targets them directly.
- **Why Possibly Novel:** Negative-selection algorithms exist in intrusion detection; a dense-vision instantiation on VFM patch features with rigorous open-set benchmarking is new.
- **Minimal Experiment:** Build self-coverage detectors on frozen features of known classes (Cityscapes); evaluate unknown flagging on anomaly benchmarks (RoadAnomaly/FS-LostFound) stratified by unknown-to-known similarity; compare against energy/softmax baselines.
- **Main Risk:** Coverage in high dimensions is hard; use per-class subspace projections and report dimension sensitivity.
- **Research Cluster:** XFER

### IDEA-C-0167 — Markowitz portfolio construction for segmentation ensembles under shift
- **One-sentence idea:** Transplant portfolio theory to ensemble selection: choose model weights by mean-variance optimization over estimated error covariance across conditions, buying robustness to distribution shift the way investors buy risk-adjusted return.
- **Problem:** Ensembles are averaged uniformly or by validation accuracy, ignoring error correlation structure — exactly the mistake diversification theory corrects.
- **Core Hypothesis (falsifiable):** Weighting ensemble members by mean-variance optimization over per-condition error estimates (conditions = corruption types/domains on a small probe set) yields worst-case-condition accuracy significantly better than uniform or accuracy-weighted ensembles at equal membership, with the gain predicted by the measured error-correlation matrix.
- **Why Important:** Deployment cares about worst-case conditions; this imports a decades-refined mechanism for exactly that objective with closed-form solutions.
- **Why Possibly Novel:** Ensemble diversity is qualitatively invoked; the explicit covariance-based portfolio optimization with worst-case validation for dense predictors appears untried.
- **Minimal Experiment:** Estimate per-model error vectors across 15 conditions from a small probe set; construct portfolio weights; evaluate worst-case and mean accuracy on held-out conditions vs baselines.
- **Main Risk:** Covariance estimated from small probes is noisy; use shrinkage estimators (also imported from finance).
- **Research Cluster:** XFER

### IDEA-C-0168 — Little's law and queueing design for human-model annotation pipelines
- **One-sentence idea:** Transplant queueing theory to assisted-annotation systems: model the human-correction stage as a queue fed by model proposals, and use Little's law and service-time distributions to derive the throughput-optimal confidence threshold for routing masks to humans.
- **Problem:** Assisted pipelines route proposals to review by fixed confidence cutoffs, causing reviewer idle time or backlog; the routing threshold is a queueing-control variable nobody treats as one.
- **Core Hypothesis (falsifiable):** Measured correction-time distributions plus arrival statistics let a queueing model predict pipeline throughput as a function of routing threshold within a small error, and the model-derived optimal threshold beats accuracy-derived thresholds on total verified-masks-per-hour in simulation replays of real annotation logs.
- **Why Important:** Dataset production is the field's biggest cost; treating it with the operations science it deserves yields immediate, quantified savings.
- **Why Possibly Novel:** Human-in-the-loop papers optimize model accuracy; the queueing-theoretic pipeline optimization with validated throughput predictions is new.
- **Minimal Experiment:** Instrument a small annotation session (or reuse public logs) for service/arrival distributions; fit the queueing model; validate throughput predictions across thresholds via replay simulation.
- **Main Risk:** Human service times are non-stationary (fatigue, learning); use time-varying queue models.
- **Research Cluster:** XFER

### IDEA-C-0169 — Wallpaper-group detection makes pattern inspection zero-shot
- **One-sentence idea:** Transplant crystallography's symmetry-group formalism to industrial inspection: detect the wallpaper group of a repeating pattern, canonicalize by its symmetry, and segment defects as symmetry-breaking residuals — no defect training data required.
- **Problem:** Pattern-product inspection (textiles, wafers, grids) trains per-product models even though the exploitable structure — the pattern's symmetry group — is discoverable from a single good image.
- **Core Hypothesis (falsifiable):** Automatic wallpaper-group identification plus group-consistent reconstruction detects defects on periodic products at accuracy matching trained anomaly detectors while transferring zero-shot to unseen products, with failures confined to non-periodic products (predictable in advance from a periodicity score).
- **Why Important:** A mathematically-grounded zero-shot mechanism for a large industrial segment, replacing hundreds of per-product models; also probes what VFMs lack (explicit symmetry reasoning).
- **Why Possibly Novel:** Fourier/self-similarity inspection heuristics exist; the full group-theoretic formulation (17 wallpaper groups, canonicalization, residual segmentation) with transfer benchmarking is new.
- **Minimal Experiment:** Implement group detection (peak lattice + symmetry tests); evaluate zero-shot on the periodic subset of MVTec-AD and a textile dataset vs trained baselines; report periodicity-score failure prediction.
- **Main Risk:** Real products have quasi-periodic distortions; include elastic lattice fitting.
- **Research Cluster:** XFER

### IDEA-C-0170 — Instrumental variables to de-confound context from object appearance
- **One-sentence idea:** Transplant econometrics' instrumental-variable (IV) estimation to representation analysis: use capture-parameter variation (focal length, viewpoint from metadata) as instruments to estimate how much a model's class prediction is caused by object appearance vs correlated context.
- **Problem:** Context-vs-object attribution methods (occlusion, background swap) intervene on images unnaturally; IV estimates causal contributions from natural variation without synthetic edits.
- **Core Hypothesis (falsifiable):** Using metadata that shifts context exposure without changing object identity (e.g., focal length changing background visibility) as instruments, IV-estimated object-appearance effects differ systematically from correlational attributions, and better predict model behavior on context-shifted test sets.
- **Why Important:** Brings identification rigor to interpretability claims that currently rest on unnatural interventions.
- **Why Possibly Novel:** Causal inference enters ML via invariance penalties; the IV estimation strategy with capture metadata as instruments for vision-model attribution is new.
- **Minimal Experiment:** On EXIF-rich datasets, define instruments; estimate IV object-effects for 20 classes; validate against background-swap ground truth and context-shifted transfer prediction.
- **Main Risk:** Instrument validity (exclusion restriction) is arguable; test multiple instruments and report overidentification checks.
- **Research Cluster:** XFER

### IDEA-C-0171 — Surround suppression as an architectural prior for low-contrast boundaries
- **One-sentence idea:** Transplant neuroscience's center-surround suppression (contrast normalization by surrounding statistics) as a lightweight input/feature transform, testing whether it specifically rescues camouflage and low-contrast boundary segmentation in frozen VFMs.
- **Problem:** VFMs underperform biological vision on low-contrast figure-ground separation; cortical surround suppression is the specific mechanism credited with local contrast amplification, and it is trivially implementable.
- **Core Hypothesis (falsifiable):** Inserting parameter-free divisive normalization by local surround statistics (at input or early features) improves frozen-VFM probe performance on camouflage/low-contrast boundary tasks by a margin that scales with measured local contrast deficit, while leaving high-contrast performance unchanged — matching the mechanism's selectivity.
- **Why Important:** A simple, anti-modular, mechanism-specified fix for an identified VFM weakness, testable in a day.
- **Why Possibly Novel:** Divisive normalization appears in early-vision modeling; its targeted evaluation as a frozen-VFM front-end for camouflage segmentation is new.
- **Minimal Experiment:** Add divisive-normalization preprocessing to frozen DINOv2/SAM pipelines; evaluate COD10K and low-contrast medical boundaries vs unmodified inputs; stratify gains by local contrast.
- **Main Risk:** Pretrained models expect natural input statistics; normalization may shift inputs off-manifold — test feature-level insertion as the alternative.
- **Research Cluster:** XFER

### IDEA-C-0172 — k-median facility location for optimal prompt-point placement
- **One-sentence idea:** Transplant operations research's facility-location optimization to prompting: choose k click positions as a k-median solution over the object's feature-affinity graph, testing whether OR-optimal prompts beat heuristic and human placement.
- **Problem:** Multi-click prompting places clicks greedily or by error-maximum heuristics; covering an object's feature diversity is literally a facility-location problem with known approximation algorithms.
- **Core Hypothesis (falsifiable):** k-median prompt placement over frozen-feature affinity achieves target IoU with fewer clicks than center/error-max policies across object categories, with the advantage growing for multi-part and textured objects whose feature diversity demands coverage.
- **Why Important:** Better automated prompting improves auto-labeling economics directly, and the coverage framing explains why some objects need many clicks (IDEA-C-0154's budget theory gets a constructive counterpart).
- **Why Possibly Novel:** Click selection heuristics exist; the formal facility-location formulation with approximation guarantees, evaluated on SAM-family models, is new.
- **Minimal Experiment:** Implement k-median placement on feature graphs; compare NoC/IoU-at-k against standard simulators on 1k objects across categories; ablate the affinity definition.
- **Main Risk:** Optimal coverage of features may not align with decoder expectations; include decoder-in-the-loop refinement as a variant.
- **Research Cluster:** XFER

### IDEA-C-0173 — Watershed-ensemble uncertainty as a calibrated mask distribution
- **One-sentence idea:** Transplant hydrology's ensemble-calibration practice (perturbed-parameter watershed model ensembles) to mask post-processing: generate mask distributions by sweeping watershed/threshold parameters over model probability maps, calibrated to match empirical annotation variability.
- **Problem:** Segmentation uncertainty methods (MC dropout, deep ensembles) are expensive and poorly calibrated to the actual variability that matters — human annotation spread.
- **Core Hypothesis (falsifiable):** A parameter-swept post-processing ensemble on a single model's outputs, with sweep ranges fit to reproduce multi-rater variability statistics on a calibration set, matches or beats deep ensembles at predicting inter-rater disagreement zones at a tiny fraction of the compute.
- **Why Important:** Cheap, calibrated, annotation-relevant uncertainty for deployment — sidestepping the expensive Bayesian machinery.
- **Why Possibly Novel:** Post-hoc threshold sweeps exist informally; formal calibration of the sweep to rater-variability targets (the hydrology forecasting recipe) is new.
- **Minimal Experiment:** Fit sweep distributions on LIDC calibration cases; evaluate disagreement-zone prediction and calibration (reliability diagrams vs rater spread) against MC-dropout/ensembles on held-out cases at matched and unmatched compute.
- **Main Risk:** Post-processing can't express all model uncertainty (semantic confusions); characterize which uncertainty components it captures.
- **Research Cluster:** XFER

### IDEA-C-0174 — Bundle adjustment for multi-view label reconciliation
- **One-sentence idea:** Transplant photogrammetry's bundle adjustment to annotation: jointly optimize a single 3D-consistent labeling from multiple inconsistent 2D annotations of the same scene/object, treating each annotation as a noisy projection with annotator-specific error models.
- **Problem:** Multi-view and multi-slice annotations (medical volumes, multi-camera rigs, video) are reconciled by ad-hoc voting per view, discarding the geometric constraint that they observe one underlying object.
- **Core Hypothesis (falsifiable):** Joint geometric reconciliation (optimize a 3D label field minimizing reprojection disagreement with all 2D annotations under annotator noise models) produces per-view labels that agree with held-out expert views significantly better than per-view consensus, with gains largest where views disagree most.
- **Why Important:** Upgrades label quality for every multi-view/volumetric dataset without new annotation — the classic photogrammetry payoff of joint over pairwise estimation.
- **Why Possibly Novel:** Multi-view consistency is used at inference; the joint annotation-reconciliation formulation with annotator noise models in the bundle is new.
- **Minimal Experiment:** On multi-view datasets with per-view masks (or medical volumes as orthogonal-slice views), implement joint reconciliation; evaluate against held-out expert annotations vs per-view voting.
- **Main Risk:** Requires camera geometry or slice registration; start with medical volumes where geometry is exact.
- **Research Cluster:** XFER

### IDEA-C-0175 — BPE over boundary chain codes: a learned discrete shape vocabulary
- **One-sentence idea:** Transplant NLP's byte-pair encoding to mask contours: learn a merge-based vocabulary over boundary chain-code sequences, testing whether the induced discrete shape tokens act as a transferable compression prior for segmentation refinement and shape anomaly detection.
- **Problem:** Shape priors are either handcrafted (smoothness) or implicit (learned decoders); compression-derived discrete vocabularies — which revolutionized sequence modeling — have not been applied to boundary geometry.
- **Core Hypothesis (falsifiable):** BPE vocabularies learned on large mask corpora compress natural object contours far better than random or synthetic contours (validating that shape regularity is BPE-capturable); using vocabulary-likelihood as a refinement prior improves boundary plausibility on corrupted predictions, and low-likelihood contours flag annotation errors with useful precision.
- **Why Important:** A simple, data-driven, generative-model-free shape prior with three immediate uses (refinement, anomaly flagging, shape statistics) and a compression-theoretic mechanism.
- **Why Possibly Novel:** Chain codes are classical and BPE is standard, but their combination as a learned shape vocabulary with downstream validation appears unexplored.
- **Minimal Experiment:** Learn BPE on SA-1B-subset contour chain codes; measure compression ratios by contour source; apply likelihood-guided refinement to perturbed masks; test annotation-error flagging on datasets with known errors.
- **Main Risk:** Chain codes are resolution/rotation sensitive; use differential encoding and multi-scale vocabularies.
- **Research Cluster:** XFER

### IDEA-C-0176 — Brightness-constancy-style label constancy with explicit occlusion handling
- **One-sentence idea:** Transplant optical flow's constancy-plus-occlusion formalism to label propagation: treat label constancy along motion/slice direction as the data term and learn an explicit occlusion/violation mask, rather than applying uniform consistency losses.
- **Problem:** Temporal/slice consistency losses penalize all label change, including genuine appearance/topology events, degrading learning exactly at the interesting moments (occlusions, organ appearance in slices).
- **Core Hypothesis (falsifiable):** Adding an occlusion-style violation estimator (trained jointly, as in unsupervised flow) to consistency-regularized semi-supervised segmentation improves accuracy specifically at motion boundaries and slice-topology events, where uniform-consistency baselines are measurably worst.
- **Why Important:** Fixes a known blind spot of the most common structure-exploiting loss with a mechanism proven in the flow literature.
- **Why Possibly Novel:** Consistency losses are pervasive; the explicit violation-mask mechanism (flow's key ingredient) has not been ported to label consistency.
- **Minimal Experiment:** Compare uniform vs violation-masked consistency on video (VSPW) and volumetric (AMOS) semi-supervised setups; report per-region gains at events vs elsewhere.
- **Main Risk:** The violation mask can degenerate (mask everything); use the flow literature's regularization (violation budget penalties).
- **Research Cluster:** XFER

### IDEA-C-0177 — Douglas-Peucker asymmetry: tolerance-swept simplification as a probe of shape information
- **One-sentence idea:** Transplant cartography's tolerance-parameterized line simplification as a measurement instrument: sweep simplification tolerance on training labels to measure each class's shape-information content and each model's sensitivity to it, defining a shape-bandwidth profile.
- **Problem:** There is no standard way to quantify how much boundary detail a task actually requires or a model actually uses; augmentation and metric choices are made blind to this.
- **Core Hypothesis (falsifiable):** Training on tolerance-swept simplified labels produces accuracy-vs-tolerance curves whose knee (shape bandwidth) varies consistently by class and predicts which classes are hurt by label downsampling, metric smoothing, and PEFT-vs-full-FT choices (linking to IDEA-C-0165 and the PEFT cluster).
- **Why Important:** A cheap, universal instrument for shape-information accounting that several other design decisions can consume.
- **Why Possibly Novel:** Simplification is used for storage; its systematic use as a scientific probe of shape bandwidth with cross-decision predictive validation is new.
- **Minimal Experiment:** Generate tolerance-swept label sets on VOC/Cityscapes; train small models per tolerance; extract per-class knees; test knee-based predictions on two downstream decisions.
- **Main Risk:** Knee estimation needs several training runs; use efficient low-epoch proxies validated once.
- **Research Cluster:** XFER

### IDEA-C-0178 — Coda-wave-style scattering statistics for transparent-object detection
- **One-sentence idea:** Transplant seismology's coda-wave analysis (information in multiply-scattered late arrivals) to imaging: use high-order scattering statistics of local texture (phase congruency residuals, speckle-like signatures) as features for transparent/translucent material segmentation.
- **Problem:** Transparent objects defeat appearance features because their signal is not reflectance but subtle multiple-scattering and refraction residues — structurally similar to seismic coda carrying scatterer information after direct waves pass.
- **Core Hypothesis (falsifiable):** Handcrafted-then-learned scattering-statistic channels (local phase disorder, micro-contrast dispersion across scales) added to RGB improve transparent-object segmentation on frozen VFMs by margins exceeding generic texture features, with per-region gains tracking measured scattering strength.
- **Why Important:** Grounds transparent-object perception in a physical signal model rather than dataset-specific appearance learning, promising better transfer.
- **Why Possibly Novel:** Polarization and depth cues are studied for transparency; scattering-statistics features imported from wave physics are not.
- **Minimal Experiment:** Compute scattering-statistic maps on Trans10K images; train light heads on RGB vs RGB+scattering over frozen features; stratify gains by scattering-strength estimates.
- **Main Risk:** Single-image scattering statistics are weak proxies of the physics; the empirical gain test is the arbiter.
- **Research Cluster:** XFER

### IDEA-C-0179 — Morphological decomposition of class names for compositional grounding
- **One-sentence idea:** Transplant linguistic morphology to open-vocabulary segmentation: decompose compound class names into morphemes with individually-grounded visual expectations ("fire|hydrant", "wind|shield"), testing whether morpheme-level grounding predicts and improves compound-class performance.
- **Problem:** Open-vocab models treat class names as atomic tokens-sequences; compound words whose meaning is non-compositional ("hot dog") vs compositional ("street lamp") should ground differently, and failures may be predictable from morphology.
- **Core Hypothesis (falsifiable):** Compound classes with compositional morphology show grounding accuracy predictable from their morphemes' individual grounding quality; non-compositional compounds deviate systematically; and morpheme-aware prompt construction (explicitly querying head morphemes) improves compositional-compound segmentation without hurting others.
- **Why Important:** Provides a linguistic-structure-based error prediction and a cheap prompt-side fix, and probes how much visual grounding is compositional at all.
- **Why Possibly Novel:** Compositionality is studied via attributes and phrases; systematic morphological analysis of class-name vocabulary with grounding-prediction validation is new.
- **Minimal Experiment:** Classify benchmark class names by morphological compositionality; regress per-class open-vocab IoU on morpheme grounding scores; test morpheme-aware prompting on the compositional subset.
- **Main Risk:** English-centric; validate on a second language's benchmarks to test generality.
- **Research Cluster:** XFER

### IDEA-C-0180 — Mixed-effects models as the missing statistical layer for benchmark claims
- **One-sentence idea:** Transplant the mixed-effects (hierarchical) modeling standard from psychology/ecology into vision evaluation: model per-image, per-class, and per-seed random effects when comparing methods, testing how many published segmentation improvements survive proper hierarchical inference.
- **Problem:** Vision compares methods by aggregate means over images that are treated as independent, though they cluster by scene, class, and source — the exact pseudo-replication error other fields spent decades eliminating.
- **Core Hypothesis (falsifiable):** Re-analyzing standard benchmark comparisons with crossed random effects (image, class, seed) inflates confidence intervals enough that a substantial fraction of typical published deltas lose significance, and the inflation is predictable from measured intra-cluster correlations.
- **Why Important:** Upgrades the field's inferential hygiene with an off-the-shelf, mechanism-understood statistical technology.
- **Why Possibly Novel:** Statistical-significance critiques exist in ML; the specific hierarchical-model transplant with intra-class-correlation accounting for dense benchmarks is not established practice.
- **Minimal Experiment:** Re-analyze 5 recent method comparisons (public per-image results or re-runs) under mixed-effects models; report which deltas survive; publish the analysis toolkit.
- **Main Risk:** Requires per-image outputs often unavailable; re-run open-source pairs where needed.
- **Research Cluster:** XFER
## Cluster AMORPH — Smoke/Fire/Transparent/Amorphous Objects Exposing General Principles (IDEA-C-0181 … IDEA-C-0200)

### IDEA-C-0181 — Smoke has no ground-truth boundary: density fields as the honest label format
- **One-sentence idea:** Establish empirically that binary smoke masks are ill-posed (inter-annotator boundary variance diverges as density thresholds are unstated) and validate density-field regression as the replacement supervision format for all amorphous classes.
- **Problem:** Smoke/fog/dust segmentation benchmarks force a binary boundary onto a continuous density field, so both training and evaluation measure an annotator's arbitrary threshold.
- **Core Hypothesis (falsifiable):** Multi-annotator smoke masks show boundary variance an order of magnitude beyond solid-object variance, structured as consistent per-annotator density thresholds (recoverable by ordering annotators' masks by inclusion); training density regression on synthetic-smoke-calibrated targets predicts every annotator's mask better than binary training predicts any of them.
- **Why Important:** Exposes a general benchmark principle — label formats must match the object's physical ontology — with immediate impact on fire-safety systems.
- **Why Possibly Novel:** Soft matting exists for hair/fur aesthetics; the ill-posedness demonstration via threshold-ordering structure and the density-regression validation protocol are new for amorphous classes.
- **Minimal Experiment:** Collect 5-annotator masks on 200 smoke images; test the inclusion-ordering structure; render synthetic smoke with known density for calibration; compare binary vs density-regression training on predicting held-out annotators.
- **Main Risk:** Synthetic-to-real density calibration is approximate; anchor with a few real multi-exposure sequences.
- **Research Cluster:** AMORPH

### IDEA-C-0182 — Transparent objects as refraction-flow operators, not appearance regions
- **One-sentence idea:** Test whether segmenting transparent objects by estimating the background-distortion field they induce (a refraction flow) outperforms appearance-based segmentation, establishing the principle that some objects are light-field operators rather than reflectance regions.
- **Problem:** Appearance-based models fail on glass because glass has almost no appearance; its visual evidence is the systematic warping of what's behind it.
- **Core Hypothesis (falsifiable):** A model trained to predict local background-distortion fields (supervised from synthetic refraction rendering) segments real transparent objects via distortion-magnitude thresholding with accuracy exceeding appearance-trained baselines of equal capacity, especially under novel backgrounds where appearance methods collapse.
- **Why Important:** Reframes a category of hard objects around their physical mechanism, with transfer robustness as the testable payoff.
- **Why Possibly Novel:** Refraction cues appear in glass-detection features; making the distortion field the primary prediction target with background-transfer stress tests is new.
- **Minimal Experiment:** Render paired scenes (with/without glass objects) for distortion-field supervision; fine-tune a small head on frozen VFM features; evaluate on Trans10K with background-swap stress tests vs appearance baselines.
- **Main Risk:** Textureless backgrounds provide no distortion signal; quantify this failure mode explicitly as part of the theory.
- **Research Cluster:** AMORPH

### IDEA-C-0183 — Fire labels conflate emission with illumination
- **One-sentence idea:** Quantify how fire-segmentation datasets mix true flame regions (emitters) with fire-illuminated surfaces (reflectors of flame light), and test whether emission/illumination disentanglement — via color-line physics or multi-frame flicker — fixes the systematic false positives models inherit.
- **Problem:** Annotators label glow, models learn glow, and deployed detectors alarm on sunsets and reflections; the root cause is an ontological confusion in the labels.
- **Core Hypothesis (falsifiable):** Auditing fire datasets shows a substantial fraction of labeled area is illuminated-surface rather than flame (verifiable by flicker analysis on video sources); models trained on emission-purified labels (flicker-verified) reduce reflection/sunset false positives by a large factor at unchanged flame recall.
- **Why Important:** Fire detection is safety-critical with notorious false-alarm costs; and source-vs-effect labeling confusion generalizes (shadows, caustics, ship wakes — see IDEA-C-0255).
- **Why Possibly Novel:** Fire detection papers tune models; the label-ontology audit with physical verification and purified retraining is new.
- **Minimal Experiment:** Flicker-analyze video-sourced fire datasets to separate emitters from illuminated surfaces; retrain on purified labels; evaluate false-positive rates on reflection/sunset hard-negative suites.
- **Main Risk:** Flicker verification needs video provenance; restrict the audit to video-derived subsets.
- **Research Cluster:** AMORPH

### IDEA-C-0184 — Prompt ambiguity on amorphous targets should produce threshold-family outputs
- **One-sentence idea:** Test how SAM-family models respond to clicks on amorphous regions (smoke, fog, spray), hypothesizing they arbitrarily commit to one density threshold, and that exposing the internal threshold family (multiple masks ordered by inclusion) matches the true ambiguity structure users need.
- **Problem:** A click on smoke is ambiguous over a continuous mask family, but interactive models return a small fixed set of nested proposals designed for part-whole, not density, ambiguity.
- **Core Hypothesis (falsifiable):** On amorphous targets, SAM's multi-mask outputs cover the annotator-threshold family poorly (low coverage of the inclusion-ordered human masks from IDEA-C-0181), and a light decoder head trained to output masks conditioned on a threshold scalar achieves near-complete coverage at equal parameters.
- **Why Important:** Interactive tools are increasingly used to label amorphous phenomena (plumes, clouds, spray) and currently impose hidden arbitrary thresholds on science and safety data.
- **Why Possibly Novel:** SAM ambiguity handling is studied for part-whole; density-family ambiguity as a distinct type with a conditioning fix is unexplored.
- **Minimal Experiment:** Evaluate SAM multi-mask coverage against multi-annotator smoke mask families; train a threshold-conditioned decoder head on synthetic density data; compare coverage on real data.
- **Main Risk:** Coverage metrics for mask families need care; use inclusion-aware matching costs.
- **Research Cluster:** AMORPH

### IDEA-C-0185 — Threshold-free supervision: alpha matting as the universal soft-boundary format
- **One-sentence idea:** Test whether training soft-boundary classes (hair, fur, foliage edges, smoke) with alpha-matte supervision instead of binary masks improves not only those classes but also hard-boundary calibration, by removing the systematic falsehood that all boundaries are step functions.
- **Problem:** Binary supervision teaches models that every boundary is sharp, corrupting confidence calibration in mixed-content scenes and wasting the sensor's sub-pixel information.
- **Core Hypothesis (falsifiable):** Models trained with matte targets on soft classes (mattes generated by established matting pipelines) show better boundary calibration on all classes (reliability of boundary-zone probabilities), and binarizing matte-trained outputs at 0.5 loses nothing on hard classes — making mattes a strict-improvement label format.
- **Why Important:** Proposes a concrete, backward-compatible upgrade to the field's default label format, with calibration as the general principle at stake.
- **Why Possibly Novel:** Matting is its own subfield; the claim that matte supervision improves general segmentation calibration (a cross-task benefit) is untested.
- **Minimal Experiment:** Generate mattes for soft-class boundary zones on VOC/COCO subsets; train binary vs matte-target models; evaluate boundary-zone calibration on both soft and hard classes plus standard metrics.
- **Main Risk:** Matting pipelines introduce their own biases; validate mattes against small trimap-based ground truth.
- **Research Cluster:** AMORPH

### IDEA-C-0186 — Shadow-first detection for weak-appearance objects
- **One-sentence idea:** Test whether transparent and low-visibility objects are more reliably detected via their shadows than their direct appearance, establishing shadows as first-class evidence channels rather than nuisances.
- **Problem:** Glass, clear plastic, and wire objects cast fully-opaque shadows that carry their shape, yet all pipelines treat shadows as clutter to be invariant to.
- **Core Hypothesis (falsifiable):** In directionally-lit scenes, a shadow-analysis pathway (detect shadow, invert projection using estimated light direction) localizes transparent objects that appearance models miss, and fusing the shadow channel improves transparent-object recall substantially at fixed false-positive rates.
- **Why Important:** Introduces a physically-grounded evidence channel usable wherever lighting geometry is known or estimable (industrial stations, outdoor sun), and inverts a universal invariance assumption.
- **Why Possibly Novel:** Shadow detection exists as a task; using shadows as the primary detection evidence for the casting object, with projection inversion, is new.
- **Minimal Experiment:** Collect/render directionally-lit scenes with transparent objects; build the shadow-inversion pathway on frozen features; measure recall gains over appearance-only on objects stratified by direct-appearance strength.
- **Main Risk:** Requires light-direction estimates; scope to single-source lighting and measure sensitivity to direction error.
- **Research Cluster:** AMORPH

### IDEA-C-0187 — Reflection-transmission layer decomposition as the correct glass task
- **One-sentence idea:** Reformulate glass-surface understanding as two-layer decomposition (reflected scene + transmitted scene) rather than region segmentation, testing whether layer decomposition supervision resolves the systematic confusion between reflections and transmitted objects that plagues all glass benchmarks.
- **Problem:** Glass regions contain two superimposed scenes; segmentation labels arbitrarily assign visible content to "glass," producing inconsistent supervision (a reflected person labeled glass; a transmitted person labeled person).
- **Core Hypothesis (falsifiable):** Auditing glass datasets reveals inconsistent reflected/transmitted content handling at high rates; models trained with explicit two-layer targets (from synthetic compositing) resolve reflected-vs-transmitted content correctly on real images where region-trained models fail at chance, and downstream tasks (person detection through windows) improve accordingly.
- **Why Important:** Layered representation is the general principle — many surfaces superimpose light paths — and window-rich urban/vehicle imagery makes the error safety-relevant.
- **Why Possibly Novel:** Reflection removal and glass segmentation exist separately; unifying them as the supervision format for glass understanding with a downstream-task validation is new.
- **Minimal Experiment:** Audit label consistency on GSD/Trans10K reflective cases; train two-layer decomposition on synthetic composites; evaluate reflected-vs-transmitted classification and through-glass detection on real annotated probes.
- **Main Risk:** Real-world two-layer ground truth is scarce; lean on synthetic training with careful real probe-set construction.
- **Research Cluster:** AMORPH

### IDEA-C-0188 — Turbulence spectra as the signature feature for smoke vs its imitators
- **One-sentence idea:** Test whether temporal texture statistics matching turbulent-flow structure (spectral cascades characteristic of advected scalar fields) separate smoke from its visual imitators (clouds, dust, steam, shadows) better than any appearance feature, embedding a physics constraint into video segmentation.
- **Problem:** Smoke false positives come from statically-similar phenomena; the discriminative physics — turbulence with the specific statistics of buoyancy-driven flow — lives in temporal structure that per-frame models discard.
- **Core Hypothesis (falsifiable):** Spatio-temporal spectral descriptors of candidate regions show smoke occupying a distinct region of cascade-statistic space vs imitator classes (measurable separation); adding these descriptors to per-frame VFM features improves smoke-vs-imitator discrimination by a large margin at unchanged compute order.
- **Why Important:** Demonstrates the general principle that class identity can live in dynamical statistics, not appearance — applicable to water, fire, foliage, and crowd flows.
- **Why Possibly Novel:** Dynamic-texture classification is classical; grounding descriptors in turbulence phenomenology and benchmarking against modern VFMs for safety-relevant discrimination is new.
- **Minimal Experiment:** Compute spatio-temporal spectra for smoke/steam/cloud/dust video regions from public datasets; visualize class separation; train fusion heads on frozen features ± spectral channels; evaluate on hard-negative suites.
- **Main Risk:** Camera motion contaminates temporal spectra; stabilize or use flow-compensated statistics.
- **Research Cluster:** AMORPH

### IDEA-C-0189 — The water-steam-smoke confusion triangle probes VFM cue hierarchies
- **One-sentence idea:** Use the three-way confusion structure among water spray, steam, and smoke as a controlled probe of which cues (color, motion, context) VFMs prioritize, testing whether confusion asymmetries reveal a stable cue hierarchy that predicts other failures.
- **Problem:** VFM error analysis is usually class-by-class; structured confusion triangles among physically-related classes could expose the model's internal cue ordering, but nobody exploits them.
- **Core Hypothesis (falsifiable):** Confusion rates among the triangle are strongly asymmetric in a direction consistent across VFMs (e.g., steam→smoke confusion exceeds smoke→steam), the asymmetry flips under targeted cue ablations (grayscale, freeze-frame, context removal) in a way that identifies the responsible cue, and the inferred hierarchy predicts confusion asymmetries in a second phenomenon triangle (dust/fog/haze).
- **Why Important:** Provides a general, cheap methodology for extracting cue hierarchies from confusion structure — a reusable interpretability instrument.
- **Why Possibly Novel:** Cue-conflict studies exist for shape-vs-texture; systematic confusion-triangle analysis with cross-triangle prediction is new.
- **Minimal Experiment:** Assemble balanced triangle datasets from public sources; measure confusion matrices for 4 VFMs under cue ablations; infer hierarchies; test predictions on the second triangle.
- **Main Risk:** Dataset assembly bias could shape confusions; balance contexts across classes carefully.
- **Research Cluster:** AMORPH

### IDEA-C-0190 — Flame flicker and temporal aliasing: frame rate as a hidden model parameter
- **One-sentence idea:** Test whether video models' fire detection depends critically on the relationship between flame flicker frequencies and the camera/model frame rate, exposing temporal aliasing as an unmeasured deployment variable for all dynamic-texture classes.
- **Problem:** Models trained at one frame rate are deployed at others; for phenomena with characteristic frequencies (flames flicker in a known band), sampling-rate mismatch could silently destroy the discriminative signal.
- **Core Hypothesis (falsifiable):** Fire-detection accuracy of temporal models varies non-monotonically with input frame rate, degrading sharply where sampling aliases the flicker band into imitator-like frequencies, and the degradation is predictable from the flicker spectrum and Nyquist analysis — with frame-rate augmentation eliminating it.
- **Why Important:** Establishes temporal sampling as a first-class robustness axis (analogous to spatial resolution), affecting every dynamic-phenomenon detector.
- **Why Possibly Novel:** Frame-rate robustness is studied for action recognition accuracy; the aliasing-mechanism analysis with spectral predictions for safety detection is new.
- **Minimal Experiment:** Resample fire/imitator videos across frame rates; evaluate temporal models per rate; compare degradation curves against aliasing predictions from measured flicker spectra; test frame-rate augmentation.
- **Main Risk:** Compression artifacts covary with resampling; regenerate all rates from high-fps originals.
- **Research Cluster:** AMORPH

### IDEA-C-0191 — Sub-pixel structures expose the raster-mask representation ceiling
- **One-sentence idea:** Use wires, fences, and hair as extreme cases to measure the representation ceiling of raster masks (structures thinner than one pixel cannot be represented, only anti-aliased), and test vector/implicit output representations against it.
- **Problem:** The field's output format — per-pixel labels — cannot express sub-pixel structures at all, yet benchmarks score them with pixel metrics, hiding a fundamental format limitation.
- **Core Hypothesis (falsifiable):** For structures below ~1.5 px width, raster-mask models hit an accuracy ceiling (measured against super-resolved ground truth) regardless of capacity or training, while parametric curve/implicit-function outputs surpass it at equal parameters; the crossover width is predictable from sampling theory.
- **Why Important:** Identifies where the universal output format fails and quantifies the case for vector outputs — relevant to power-line inspection, hair matting, and biological filament analysis.
- **Why Possibly Novel:** Vector outputs exist for specific tasks (lane detection); the format-ceiling framing with a sampling-theoretic crossover and controlled comparison is new.
- **Minimal Experiment:** Render synthetic scenes with swept sub-pixel wire widths and exact geometric ground truth; train raster and curve-output models at matched capacity; measure the ceiling and crossover; validate on real power-line imagery with surveyed geometry.
- **Main Risk:** Fair capacity matching across output formats; report sweeps rather than single configurations.
- **Research Cluster:** AMORPH

### IDEA-C-0192 — Specular highlights are labeled inconsistently and models inherit the incoherence
- **One-sentence idea:** Audit how datasets handle specular highlights (labeled as object, as separate reflection, or excluded) and test whether the resulting supervision incoherence explains models' unstable behavior on shiny objects.
- **Problem:** A highlight on an apple is apple; a highlight on a car window might be labeled glass, sky, or ignored — annotation conventions are silent, and models trained on mixtures may behave erratically on gloss.
- **Core Hypothesis (falsifiable):** Highlight-region label conventions vary measurably within and across datasets; model confidence on highlight pixels is systematically depressed and prediction flips under small viewpoint/exposure changes at rates far exceeding matte regions — with convention-consistent relabeling of a training subset reducing the instability.
- **Why Important:** Gloss is everywhere in products, vehicles, and wet surfaces; supervision incoherence is a fixable root cause of a widespread instability.
- **Why Possibly Novel:** Specularity is studied in intrinsic imaging; the label-convention audit connecting supervision incoherence to prediction instability is new.
- **Minimal Experiment:** Detect highlight regions photometrically across datasets; audit their labels; measure prediction instability on highlight vs matte pixels under exposure jitter; retrain with consistent conventions on a subset.
- **Main Risk:** Highlight detection itself is imperfect; use conservative photometric criteria.
- **Research Cluster:** AMORPH

### IDEA-C-0193 — Stuff-inside-things: liquid levels test nested-region reasoning
- **One-sentence idea:** Use liquid-in-transparent-container segmentation (water level in a glass) as a minimal probe of nested-region reasoning — segmenting stuff whose extent is defined by both its own boundary and its container's — testing whether VFMs represent containment at all.
- **Problem:** Containment relations ("the liquid inside the glass") require composing two segmentations with an occlusion-aware intersection; standard models have no mechanism for this, and no benchmark isolates it.
- **Core Hypothesis (falsifiable):** VFM-based segmenters fail systematically on liquid-level tasks in ways attributable to missing containment composition (errors follow container boundaries, not liquid boundaries); a minimal compositional head (predict container, predict fill fraction, compose) dramatically outperforms direct segmentation at equal capacity — showing the failure is representational, not perceptual.
- **Why Important:** Containment is a basic scene-structure primitive (cups, tanks, vessels in medicine and industry); a minimal isolating probe tells us whether current architectures need compositional structure.
- **Why Possibly Novel:** Liquid perception appears in robotics niches; framing it as the minimal nested-region reasoning probe with a compositional-vs-direct comparison is new.
- **Minimal Experiment:** Assemble/render liquid-level datasets with varied containers; compare direct vs compositional heads on frozen features; analyze direct-model error geometry against the container-following prediction.
- **Main Risk:** Synthetic-real transfer for liquids; include a small real photographed set with measured fill levels.
- **Research Cluster:** AMORPH

### IDEA-C-0194 — Heat shimmer as natural adversarial distortion and a free robustness benchmark
- **One-sentence idea:** Characterize atmospheric heat-shimmer distortion as a naturally-occurring adversarial perturbation (spatially-correlated, physically-parameterized warping) and test whether shimmer-robustness training transfers to other refractive-distortion domains (underwater, turbulence in long-range imaging).
- **Problem:** Robustness suites use synthetic corruptions (noise, blur, JPEG); refractive warping — common over roads, fires, deserts, and water — has different structure (measure-preserving, spatially-coherent) and is unrepresented.
- **Core Hypothesis (falsifiable):** Standard segmenters degrade under calibrated shimmer far more than under intensity corruptions of matched perceptual severity; models fine-tuned on physics-parameterized shimmer augmentation recover most of the loss and transfer that robustness to underwater and long-range turbulence footage — validating a shared refractive-distortion robustness axis.
- **Why Important:** Adds a physically-grounded corruption family to the robustness canon, unifying several deployment domains under one augmentation.
- **Why Possibly Novel:** Turbulence mitigation is its own imaging field; connecting it to segmentation robustness benchmarking with cross-domain transfer claims is new.
- **Minimal Experiment:** Implement physics-based shimmer simulation; benchmark public segmenters vs matched-severity standard corruptions; fine-tune with shimmer augmentation; test on real underwater/long-range clips.
- **Main Risk:** Perceptual severity matching across corruption types is delicate; use human-rated severity anchors.
- **Research Cluster:** AMORPH

### IDEA-C-0195 — Bimodal appearance from backlighting: smoke's illumination-conditioned identity
- **One-sentence idea:** Test whether models represent smoke's illumination-dependent bimodality (bright when front-lit, dark when back-lit) as one concept or two, and whether illumination-conditioning resolves the notorious dark-smoke miss rate.
- **Problem:** Smoke's appearance flips sign with lighting geometry; datasets are dominated by one mode, and models may encode "smoke = bright translucent," missing dark smoke — the mode that indicates the most dangerous fires.
- **Core Hypothesis (falsifiable):** Feature-space analysis shows front-lit and back-lit smoke forming separated clusters with the decision boundary cutting one off (explaining measured dark-smoke recall deficits); explicitly conditioning on estimated illumination direction (or balancing modes in training) closes most of the deficit without new architectures.
- **Why Important:** A concrete safety gap with a representational diagnosis, and a general lesson: classes whose appearance is conditioned on hidden physical variables need those variables surfaced.
- **Why Possibly Novel:** Dark-smoke difficulty is noted in fire literature; the bimodality diagnosis in VFM feature space with a conditioning fix is new.
- **Minimal Experiment:** Partition smoke datasets by lighting geometry (annotate from context); visualize/measure feature clustering; compare mode-balanced and illumination-conditioned training against baselines on dark-smoke recall.
- **Main Risk:** Lighting-geometry annotation is approximate; use sun-position metadata where available.
- **Research Cluster:** AMORPH

### IDEA-C-0196 — Fresnel-edge brightening: extreme sparse-cue integration as a VFM stress test
- **One-sentence idea:** Use glass-edge Fresnel brightening — often the only reliable local evidence for clean glass — as a maximally-sparse-cue benchmark measuring how well VFMs integrate rare, thin, high-precision evidence into region-level decisions.
- **Problem:** Most benchmarks provide redundant cues; the ability to leverage a single thin evidence line (one-pixel-wide edge brightening determining a large region's label) is untested, though many hard cases (clean glass, clear water surfaces) depend on it.
- **Core Hypothesis (falsifiable):** VFM segmentation of clean glass correlates strongly with the visibility of Fresnel edges (accuracy collapsing when edges are occluded/cropped, verified by controlled occlusion), showing models do use the cue but integrate it over limited range; explicit edge-evidence propagation (a single learned diffusion from edge evidence) extends the integration range and recovers accuracy on partially-occluded-edge cases.
- **Why Important:** Sparse-cue long-range integration is a general capability question (relevant to boundary-only evidence in medical and industrial imaging), given a clean physical testbed.
- **Why Possibly Novel:** Glass cues are listed in detection papers; the controlled cue-occlusion methodology measuring integration range is new.
- **Minimal Experiment:** On glass datasets, measure per-object accuracy vs Fresnel-edge visibility; run controlled edge-occlusion interventions; test an evidence-propagation head on frozen features.
- **Main Risk:** Edge visibility annotation is manual; keep the probe set small but controlled.
- **Research Cluster:** AMORPH

### IDEA-C-0197 — Local smoke and global fog are the same task at different scales
- **One-sentence idea:** Test whether a single density-estimation model handles both localized smoke segmentation and global fog/haze estimation (dehazing's transmission map), unifying two separate literatures under the hypothesis that both are scalar-field estimation of the same physical quantity.
- **Problem:** Smoke segmentation and dehazing evolved separately with incompatible formats (masks vs transmission maps), though both estimate suspended-particle density along light paths.
- **Core Hypothesis (falsifiable):** A density-field model trained jointly on smoke data (converted per IDEA-C-0181) and haze transmission data outperforms specialist models on both tasks at matched capacity, and exhibits zero-shot generalization between regimes (dense local plumes ↔ thin global haze) that specialists lack — confirming a shared underlying estimation problem.
- **Why Important:** Task unification reduces the field's fragmentation and tests whether physical-quantity-based task definitions beat appearance-based ones — a general principle for task taxonomy.
- **Why Possibly Novel:** Both literatures are mature but disjoint; the unification hypothesis with cross-regime zero-shot tests appears untried.
- **Minimal Experiment:** Convert smoke masks to density proxies and haze data to the same units; train joint vs specialist models; evaluate within-task and cross-regime.
- **Main Risk:** Unit calibration across data sources is the hard part; use rank-based objectives where absolute density is unavailable.
- **Research Cluster:** AMORPH

### IDEA-C-0198 — Foam and bubbles: instances defined by tessellation, not figure-ground
- **One-sentence idea:** Use foam/bubble imagery — where instances are cells of a space-filling tessellation with shared boundaries — to test whether instance-segmentation architectures built on figure-ground assumptions can represent tessellation instancehood at all.
- **Problem:** Standard instance formulations (detect-then-mask, query-per-object) assume objects are figures on ground; tessellated materials (foams, grains, biological tissue) violate this, and failures are attributed to difficulty rather than formulation mismatch.
- **Core Hypothesis (falsifiable):** Detect-then-mask models show systematic errors on tessellations that boundary-based formulations (predict shared walls, then cells) avoid at equal capacity — specifically double-assignment and missed-cell errors scaling with cell-count in a way boundary methods' errors do not — establishing formulation-dependence of instance segmentation.
- **Why Important:** Materials science, biology, and food industry imagery is tessellated; and the result clarifies that "instance segmentation" bundles at least two mathematically different problems.
- **Why Possibly Novel:** Cell-segmentation tools use boundary methods pragmatically; the formulation-mismatch analysis with error-scaling signatures is new as a general claim.
- **Minimal Experiment:** Benchmark query-based vs boundary-based methods on foam/grain datasets with cell-count sweeps; classify error types; test the predicted error-scaling difference.
- **Main Risk:** Confounding architecture quality with formulation; implement both formulations on the same backbone.
- **Research Cluster:** AMORPH

### IDEA-C-0199 — Emissive-source rendering fidelity is the binding constraint for synthetic fire
- **One-sentence idea:** Test whether sim2real transfer for fire/flame segmentation is limited specifically by light-transport correctness of emission rendering (volumetric emission, bloom, sensor saturation), not by shape or texture realism — localizing the rendering budget that matters.
- **Problem:** Synthetic fire data is generated with game-engine effects; teams don't know which rendering dimension (shape dynamics, spectra, camera response) to invest in for transfer.
- **Core Hypothesis (falsifiable):** A rendering-dimension ablation (correct emission spectra + sensor saturation vs correct shape dynamics vs correct smoke coupling, each varied independently) shows real-data transfer is most sensitive to the emission/sensor axis, with saturated-pixel-region statistics being the measurable mediator that predicts per-variant transfer.
- **Why Important:** Rendering budgets are finite; identifying the binding dimension makes synthetic safety-data generation efficient, and the mediator analysis (saturation statistics) is a reusable sim2real diagnostic.
- **Why Possibly Novel:** Sim2real ablations exist for driving; dimension-wise rendering ablations for emissive phenomena with mediator analysis are new.
- **Minimal Experiment:** Generate fire data variants along three rendering axes; train and evaluate on real fire benchmarks; regress transfer on the saturation-statistics divergence per variant.
- **Main Risk:** Axes interact; use a factorial design rather than one-at-a-time.
- **Research Cluster:** AMORPH

### IDEA-C-0200 — Is a smoke plume one instance? Instancehood as convention vs perception
- **One-sentence idea:** Measure human inter-annotator agreement on instance counts for amorphous phenomena (plumes, clouds, spills) and test whether model instance outputs match human convention distributions — probing whether instancehood for amorphous matter is learnable perception or arbitrary convention.
- **Problem:** Instance benchmarks assume countable objects; amorphous phenomena merge and split, and the field has never established whether their "instances" are perceptually real (high human agreement) or convention (low agreement) — yet models are scored against single annotations.
- **Core Hypothesis (falsifiable):** Human instance-count agreement on amorphous scenes is far below solid-object agreement but structured (agreement predictable from topological separability of the density field); models trained on single-annotator instances produce count distributions matching their annotator, not the human consensus distribution — and evaluation against distributions rather than single answers reorders methods.
- **Why Important:** Defines the measurement limits of instance segmentation for an entire phenomenon class before more benchmarks bake in arbitrary conventions.
- **Why Possibly Novel:** Instance ambiguity is acknowledged anecdotally; the agreement-structure measurement with topological predictors and distribution-based evaluation is new.
- **Minimal Experiment:** Collect instance annotations from 8 annotators on 150 amorphous scenes; measure agreement structure vs topological separability; evaluate model count distributions against human distributions.
- **Main Risk:** Annotation instructions strongly shape conventions; run two instruction framings and report both.
- **Research Cluster:** AMORPH
## Cluster MED — Medical VFM Science (IDEA-C-0201 … IDEA-C-0230)

### IDEA-C-0201 — Layer-wise census of scanner-vs-anatomy encoding in VFM features
- **One-sentence idea:** Map, layer by layer, how strongly VFM features encode scanner/vendor identity vs anatomical content in medical images, and test whether adapter placement targeted at peak-vendor-encoding layers beats uniform placement.
- **Problem:** Medical adaptation places adapters uniformly or by heuristic; if vendor confounds concentrate at specific depths, targeted intervention should dominate.
- **Core Hypothesis (falsifiable):** Linear probes show vendor information peaking at identifiable early-middle layers while anatomy peaks later; adapters placed only at vendor-peak layers achieve cross-vendor generalization matching full-depth adaptation at a fraction of parameters, while anatomy-peak-only placement does not.
- **Why Important:** Converts adapter placement from art to measurement for the dominant confound in multi-site medical imaging.
- **Why Possibly Novel:** Site effects and probing both exist; the layer-resolved vendor/anatomy census with placement-consequence validation is new.
- **Minimal Experiment:** Probe frozen DINOv2/MedSAM layers for vendor and structure decoding on multi-vendor MRI (fastMRI metadata); train placement variants; compare cross-vendor Dice.
- **Main Risk:** Vendor correlates with protocol/population; use vendor-balanced probe sets.
- **Research Cluster:** MED

### IDEA-C-0202 — Dice optimization induces a lesion-size-dependent volumetric bias law
- **One-sentence idea:** Characterize the systematic volume bias of Dice-trained segmentation models as a function of lesion size, and derive the correction curve clinical volumetry needs.
- **Problem:** Dice is size-normalized per structure but its optimization geometry over/under-segments differently by size, corrupting longitudinal volume measurements clinicians rely on.
- **Core Hypothesis (falsifiable):** Across models and datasets, predicted-to-true volume ratio follows a reproducible monotone curve in true volume (small lesions over-segmented, large under-segmented, or the reverse — the direction itself is the discovery), with the curve's shape derivable from Dice's gradient structure and removable by a post-hoc calibration fit on held-out cases.
- **Why Important:** Volumetric change drives treatment decisions; a systematic size-dependent bias silently biases clinical trials that use automated volumetry.
- **Why Possibly Novel:** Dice's counting biases are noted qualitatively; the quantitative size-conditional bias law and calibration protocol are missing.
- **Minimal Experiment:** Evaluate 5 public lesion models on datasets with size ranges spanning two orders of magnitude; fit volume-ratio curves; test cross-dataset stability; validate the calibration on longitudinal pairs.
- **Main Risk:** Annotation bias also varies with size (IDEA-C-0114); separate with multi-rater subsets.
- **Research Cluster:** MED

### IDEA-C-0203 — The anisotropy crossover: when 2D slice models beat 3D networks
- **One-sentence idea:** Establish the slice-spacing threshold at which 2D (per-slice) segmentation surpasses 3D convolution/attention on anisotropic volumes, testing whether the crossover is predictable from the ratio of in-plane to through-plane information content.
- **Problem:** The 2D-vs-3D choice is remade ad hoc for every anisotropic dataset (thick-slice CT/MR); a predictive rule would settle a perennial engineering debate with science.
- **Core Hypothesis (falsifiable):** Across datasets with resampled anisotropy levels, the 2D/3D accuracy crossover occurs at a consistent value of measurable through-plane information (autocorrelation decay across slices), allowing the winner to be predicted from data statistics before training.
- **Why Important:** Saves duplicated engineering across the medical field and identifies what 3D context is actually worth as a function of sampling.
- **Why Possibly Novel:** 2D-vs-3D comparisons exist per-dataset; the controlled anisotropy sweep with an information-theoretic crossover predictor is new.
- **Minimal Experiment:** Resample isotropic datasets (AMOS) to anisotropy levels {1:1…1:10}; train matched 2D/3D models per level; locate crossovers; regress on through-plane autocorrelation.
- **Main Risk:** Resampling isn't identical to native thick-slice acquisition (partial volume); validate at native thick-slice datasets.
- **Research Cluster:** MED

### IDEA-C-0204 — Atlas-propagated labels imprint atlas topology onto models
- **One-sentence idea:** Test whether models trained on registration-propagated (atlas-based) labels inherit the atlas's topology and smoothness, failing systematically on pathology that violates atlas assumptions — and quantify how much public "ground truth" is atlas-propagated.
- **Problem:** Many large medical label sets were bootstrapped by registration from atlases; the deformation model's smoothness becomes invisible label bias against exactly the abnormal anatomy models must catch.
- **Core Hypothesis (falsifiable):** Atlas-propagated labels show measurably lower shape-complexity variance than manual labels of the same structures; models trained on them underperform manual-label-trained models specifically on topology-violating pathology (resections, congenital variants), with the deficit proportional to the atlas-label fraction in training.
- **Why Important:** Reveals a structural bias in medical training data that targets the clinically-critical abnormal cases.
- **Why Possibly Novel:** Registration error is studied as noise; its systematic topological-prior imprint on downstream models is unexamined.
- **Minimal Experiment:** Compare shape statistics of atlas-propagated vs manual labels on shared structures; train on each; evaluate on post-surgical/variant-anatomy test cases; sweep atlas-fraction mixtures.
- **Main Risk:** Provenance of public labels is partly undocumented; use datasets with known pipelines and controlled re-propagation.
- **Research Cluster:** MED

### IDEA-C-0205 — A universal rater-noise model transferable across organs
- **One-sentence idea:** Test whether inter-rater variability in medical segmentation follows a common structural form across organs and modalities (variance predictable from local contrast, boundary curvature, and structure size), enabling a single transferable rater-noise model where multi-rater data is unavailable.
- **Problem:** Uncertainty methods need rater-noise estimates, but multi-rater data exists for few structures; if noise structure is universal, it can be transferred rather than re-collected.
- **Core Hypothesis (falsifiable):** A noise model fit on multi-rater datasets for organs A/B predicts held-out rater disagreement maps for organ C and a different modality with useful accuracy (substantially beating uniform or size-only baselines), confirming a shared functional form.
- **Why Important:** Unlocks calibrated uncertainty and noise-aware training for the majority of tasks that will never have multi-rater annotation.
- **Why Possibly Novel:** Per-dataset rater models exist; the cross-organ transferability claim with covariate-based structure is untested.
- **Minimal Experiment:** Fit disagreement-prediction models (features: contrast, curvature, size, gradient strength) on LIDC + prostate multi-rater data; test zero-shot on cardiac/abdominal multi-rater sets; report transfer accuracy.
- **Main Risk:** Protocol-specific disagreement components cap transfer; quantify the transferable fraction (connects to IDEA-C-0111).
- **Research Cluster:** MED

### IDEA-C-0206 — Contrast-phase is an unlabeled latent confounder in abdominal CT benchmarks
- **One-sentence idea:** Audit abdominal CT segmentation benchmarks for uncontrolled contrast-phase composition (arterial/venous/delayed) and test whether phase imbalance across train/test splits explains cross-dataset performance anomalies.
- **Problem:** Contrast phase changes organ/lesion appearance dramatically but is rarely annotated in public benchmarks, entering silently as a latent variable.
- **Core Hypothesis (falsifiable):** A phase classifier (trainable from small labeled sets) reveals phase distributions differing significantly between popular benchmarks and between their train/test splits; per-phase evaluation shows model rankings and absolute Dice varying strongly by phase, with cross-dataset gaps largely explained by phase-composition differences.
- **Why Important:** A correctable confounder affecting liver/pancreas benchmarks that gate clinical model claims.
- **Why Possibly Novel:** Phase effects are known clinically; the benchmark-level audit with gap decomposition appears undone.
- **Minimal Experiment:** Train a phase classifier on phase-labeled data; audit LiTS/AMOS/MSD-liver; re-evaluate 4 methods phase-stratified; decompose cross-dataset gaps.
- **Main Risk:** Phase classifier errors propagate; validate classifier accuracy on held-out labeled scans first.
- **Research Cluster:** MED

### IDEA-C-0207 — Zero-shot click cost as a transferability meter for medical fine-tuning
- **One-sentence idea:** Test whether the number of clicks zero-shot SAM needs to reach target Dice on a new medical task predicts the fine-tuning data requirement for that task, making a one-afternoon interactive session a quantitative project-planning instrument.
- **Problem:** Teams cannot estimate annotation/fine-tuning budgets for new medical tasks before committing resources.
- **Core Hypothesis (falsifiable):** Across many medical tasks, zero-shot NoC (to fixed Dice) correlates strongly with the labeled-volume count needed for fine-tuned models to reach clinical-target Dice, and the fitted relationship predicts held-out task budgets within a factor of ~2.
- **Why Important:** Converts an unavoidable planning guess into a cheap measurement, valuable for every clinical ML project.
- **Why Possibly Novel:** SAM zero-shot medical evaluations exist descriptively; their calibration as a prospective budget predictor is new.
- **Minimal Experiment:** For 12 public medical tasks, record zero-shot NoC and fine-tuning learning curves; fit the predictor; validate prospectively on 3 held-out tasks.
- **Main Risk:** NoC depends on prompt protocol; standardize the simulator and report protocol sensitivity.
- **Research Cluster:** MED

### IDEA-C-0208 — Stain normalization is adaptation pretending to be augmentation
- **One-sentence idea:** Disentangle whether histopathology stain normalization helps as training augmentation (invariance learning) or as test-time adaptation (distribution matching), because the two mechanisms imply opposite deployment designs.
- **Problem:** Stain handling is applied both ways interchangeably; if the benefit is adaptation, augmentation-only pipelines leave accuracy on the table (and vice versa).
- **Core Hypothesis (falsifiable):** A factorial design (stain augmentation at train × stain normalization at test) shows the test-time component dominating cross-site gains for models below a capacity/diversity threshold, with the balance shifting toward augmentation as training-site diversity grows — a measurable interaction that dictates pipeline choice by data census.
- **Why Important:** Resolves a long-running practice ambiguity in computational pathology with a decision rule based on measurable site diversity.
- **Why Possibly Novel:** Stain methods are compared head-to-head; the mechanism-separating factorial with the diversity interaction is not established.
- **Minimal Experiment:** Run the 2×2 (± train augmentation, ± test normalization) across site-diversity-controlled training subsets on CAMELYON-style data; map the interaction surface.
- **Main Risk:** Normalization method choice matters; use two standard methods to check robustness.
- **Research Cluster:** MED

### IDEA-C-0209 — Topology-simplifying reparameterization: segment vessels in curved-planar space
- **One-sentence idea:** Test whether segmenting tubular structures in curved-planar-reformatted (CPR) coordinates — where vessels become straight tubes — outperforms native-space segmentation, establishing task-adapted reparameterization as a general alternative to architectural complexity.
- **Problem:** Vessel segmentation fights curvature and branching with heavy 3D architectures, while radiologists routinely straighten vessels (CPR) because the task is easier in that space.
- **Core Hypothesis (falsifiable):** A simple 2D model on CPR-transformed data (initialized from cheap centerline estimates) beats specialized 3D vessel architectures at matched compute on stenosis-relevant metrics, with the gain proportional to vessel tortuosity — showing the coordinate transform substitutes for architectural capacity.
- **Why Important:** Reparameterization-before-learning is an underused general principle (log-polar for rotation, CPR for tubes); a clean win here motivates the family.
- **Why Possibly Novel:** CPR is a visualization tool; using it as the learning space with a tortuosity-stratified comparison against native-space SOTA is new.
- **Minimal Experiment:** Build CPR pipelines from rough centerlines on coronary/airway datasets; train matched 2D-CPR vs 3D-native models; evaluate per-tortuosity-stratum.
- **Main Risk:** Centerline errors corrupt the transform; measure sensitivity and use iterative refinement.
- **Research Cluster:** MED

### IDEA-C-0210 — Annotator attention dies at volume boundaries: first/last-slice label decay
- **One-sentence idea:** Test whether lesion annotations systematically degrade at the superior/inferior extremes of annotated ranges (annotators under-extend structures at their fade-out slices), creating a z-direction label bias models inherit as premature structure termination.
- **Problem:** Structures fade gradually at their axial extremes; deciding the terminal slice is the hardest annotation call and plausibly biased toward early termination, but nobody has measured it.
- **Core Hypothesis (falsifiable):** Multi-rater data shows disagreement concentrating at terminal slices with a systematic under-extension bias relative to intensity-based structure evidence; models reproduce the truncation (predicted extents terminate earlier than intensity evidence supports), and extent-corrected training labels improve volume accuracy on reference-standard cases.
- **Why Important:** Terminal-slice bias directly corrupts volume and extent measurements used for staging and treatment response.
- **Why Possibly Novel:** Slice inconsistency is known generally (IDEA-C-0097); the specific terminal-slice bias direction and its model inheritance are unmeasured.
- **Minimal Experiment:** Analyze LIDC multi-rater terminal-slice statistics against intensity profiles; test model extent truncation on held-out cases; retrain with extent-corrected labels on a subset.
- **Main Risk:** Intensity evidence at fade-out is genuinely ambiguous; use pathology-verified extent where available for anchoring.
- **Research Cluster:** MED

### IDEA-C-0211 — What report text can and cannot supervise: a property-decomposition study
- **One-sentence idea:** Decompose which mask properties (presence, laterality, rough location, size category, extent) radiology-report text can supervise, testing the hypothesis that text-supervised medical grounding hits a hard ceiling on extent/boundary information absent from language.
- **Problem:** Report-supervised learning is booming, but reports systematically omit precise spatial extent — the property segmentation needs most — and the field lacks a supervision-content accounting.
- **Core Hypothesis (falsifiable):** Information analysis of report corpora shows extent/boundary descriptors are rare and coarse; models trained with report supervision saturate on presence/laterality metrics while extent metrics plateau near location-prior baselines regardless of text-model scale — localizing the ceiling in the supervision, not the architecture.
- **Why Important:** Sets realistic expectations and redirects effort toward hybrid supervision (reports + sparse clicks) where each signal covers its measured strengths.
- **Why Possibly Novel:** Report-supervised methods report aggregate localization; the property-wise supervision-content accounting with ceiling identification is new.
- **Minimal Experiment:** Annotate a report corpus for property mentions; train report-supervised grounding at 3 text-encoder scales; evaluate property-decomposed metrics; compare against the corpus content statistics.
- **Main Risk:** Extraction of property mentions is NLP-dependent; hand-verify a sample.
- **Research Cluster:** MED

### IDEA-C-0212 — LayerNorm-only personalization captures most federated site variance
- **One-sentence idea:** Test whether per-site personalization in federated medical segmentation is nearly saturated by LayerNorm-affine-only site heads, implying site variation is predominantly low-dimensional style shift and enabling drastically cheaper federation.
- **Problem:** Federated personalization methods ship increasingly complex per-site modules without establishing how much site variance actually requires expressive capacity.
- **Core Hypothesis (falsifiable):** Across multi-site datasets, LN-only personalization recovers the large majority of the gap between global and fully-personalized models, with residuals concentrated at sites whose shift a protocol audit reveals to be label-convention (not image) differences — connecting capacity needs to shift type.
- **Why Important:** Simplifies federated deployment (tiny per-site deltas) and provides a diagnostic separating image shift from protocol shift per site.
- **Why Possibly Novel:** LN-tuning is known (IDEA-C-0073 relates); its systematic sufficiency measurement in the federated medical setting with residual attribution is new.
- **Minimal Experiment:** On FedProstate/multi-site cardiac data, compare global, LN-personalized, and fully-personalized models; attribute residual gaps via label-protocol audits at outlier sites.
- **Main Risk:** Site count in public federated datasets is small; aggregate across several benchmarks.
- **Research Cluster:** MED

### IDEA-C-0213 — Rank-transform invariance beats GAN translation for cross-modality transfer
- **One-sentence idea:** Test whether cross-modality medical transfer (CT→MR) for structures with preserved intensity rank ordering succeeds with simple monotone rank-transform preprocessing where expensive GAN-based modality translation is unnecessary — and predict per-structure which regime applies.
- **Problem:** Cross-modality adaptation defaults to learned translation networks, though many structures differ across modalities mainly by a monotone intensity remapping.
- **Core Hypothesis (falsifiable):** For structures whose cross-modality intensity relationship is near-monotone (measurable from a few paired/registered scans), rank-normalized transfer matches GAN-translation pipelines within noise; failures concentrate exactly on structures with non-monotone relationships (signal inversions), making a cheap monotonicity measurement the method-selection rule.
- **Why Important:** Replaces a heavy, artifact-prone component with a measurement-guided cheap alternative where valid — and explains when translation is genuinely needed.
- **Why Possibly Novel:** Histogram/rank normalization is old; its head-to-head against GAN translation with a monotonicity-based selection rule is untested.
- **Minimal Experiment:** Measure per-structure cross-modality intensity monotonicity on paired data; run rank-transform vs CycleGAN-style transfer for structures in both regimes; validate the selection rule.
- **Main Risk:** Spatial context differences (not just intensity) may matter; the per-structure stratification will reveal this.
- **Research Cluster:** MED

### IDEA-C-0214 — Contact-state supervision: what masks miss in surgical scene understanding
- **One-sentence idea:** Test whether adding tool-tissue contact-state labels (touching/not/deforming) to surgical video segmentation improves downstream surgical tasks more than improving mask quality itself, because the clinically-meaningful events live at contact, not extent.
- **Problem:** Surgical scene understanding optimizes mask metrics, but phase recognition and skill assessment depend on interactions that masks represent only implicitly.
- **Core Hypothesis (falsifiable):** At matched annotation budget, spending on sparse contact-state labels (cheap per frame) plus coarser masks beats spending on finer masks alone for downstream phase-recognition and event-detection accuracy — showing the marginal information value of interaction labels exceeds boundary precision in this domain.
- **Why Important:** Reorients an application field's annotation economics toward the labels its actual objectives need — a general lesson about task-aligned supervision.
- **Why Possibly Novel:** Contact estimation appears in robotics; the annotation-budget-allocation experiment against mask refinement for surgical understanding is new.
- **Minimal Experiment:** Annotate contact states on CholecSeg-style clips at low cost; train mask-only vs mask+contact models at matched budgets; compare downstream phase/event metrics.
- **Main Risk:** Contact is sometimes visually ambiguous; measure annotator agreement first.
- **Research Cluster:** MED

### IDEA-C-0215 — Prompt-jitter ensembles as a calibrated surrogate for rater variability
- **One-sentence idea:** Test whether jittering SAM-style prompts according to a fitted human-clicking noise distribution produces mask ensembles whose spread calibratedly matches inter-rater segmentation variability — cheap uncertainty grounded in the interaction interface.
- **Problem:** Clinical uncertainty estimates require expensive multi-rater data or ensemble training; promptable models offer a free ensemble dimension nobody has calibrated against the quantity that matters (rater spread).
- **Core Hypothesis (falsifiable):** With prompt-noise parameters fit on a small rater-behavior dataset, prompt-jitter mask distributions match multi-rater variability (variogram/coverage metrics) significantly better than MC-dropout and temperature-based baselines across organs, and transfer across tasks without refitting.
- **Why Important:** Deployable, near-zero-cost uncertainty for interactive clinical tools, with calibration to the clinically-accepted reference (human variability).
- **Why Possibly Novel:** Prompt perturbation is used for robustness testing; its calibration as a rater-variability surrogate is new.
- **Minimal Experiment:** Fit click-noise models from annotator logs; generate jitter ensembles on multi-rater datasets; evaluate distributional calibration vs baselines; test cross-organ transfer.
- **Main Risk:** SAM's mask diversity may be too low to span rater spread (connects to IDEA-C-0274); measure coverage explicitly.
- **Research Cluster:** MED

### IDEA-C-0216 — Age-confounded features make cross-sectional models fail at change detection
- **One-sentence idea:** Test whether models trained on cross-sectional medical data entangle disease features with normal-aging features, making them systematically unreliable for longitudinal change detection even when cross-sectional accuracy is high.
- **Problem:** Most training data is cross-sectional (one scan per patient), but deployment increasingly asks longitudinal questions (has this changed?); the aging-disease entanglement is a structural confounder for that transfer.
- **Core Hypothesis (falsifiable):** Feature-space probes show age decodable from disease-feature directions (entanglement); on longitudinal test sets, cross-sectionally-trained models' change estimates correlate spuriously with inter-scan age gaps on stable patients, and age-decorrelated training (residualizing features against age) reduces the false-change rate substantially.
- **Why Important:** Longitudinal reliability is the actual clinical use case for many tools; this identifies and fixes a data-structural failure mode.
- **Why Possibly Novel:** Confounder adjustment exists in medical ML for demographics; the specific cross-sectional-to-longitudinal transfer failure with a false-change endpoint is rarely tested.
- **Minimal Experiment:** Probe age entanglement in features of brain-MRI models; evaluate change-detection false-positive rates vs age gap on stable longitudinal cohorts (ADNI stable subgroups); test decorrelation training.
- **Main Risk:** Truly stable longitudinal cohorts are imperfectly defined; use short-interval rescans as the stability gold standard.
- **Research Cluster:** MED

### IDEA-C-0217 — Decoder suppression undercounts dense small findings
- **One-sentence idea:** Test whether the systematic undercounting of numerous small findings (microbleeds, micro-nodules) by modern segmenters stems from decoder-level mutual suppression (query competition/NMS-like effects) rather than detection sensitivity, and fix it with count-calibrated decoding.
- **Problem:** Clinical counts (number of microbleeds) drive decisions, and models undercount as density rises — usually blamed on visibility, possibly caused by architecture.
- **Core Hypothesis (falsifiable):** Synthetic density sweeps (planting known findings at controlled densities) show per-finding recall dropping with local density even at fixed individual visibility — the signature of mutual suppression, localizable to decoder attention/NMS stages — and density-aware decoding (local count calibration) restores linear count fidelity.
- **Why Important:** Count fidelity is a distinct clinical requirement no segmentation metric currently protects; the mechanism localization tells architects what to fix.
- **Why Possibly Novel:** Crowding effects are studied in detection benchmarks; the clinical counting framing with planted-density causal sweeps and decoder attribution is new.
- **Minimal Experiment:** Plant synthetic microbleeds at controlled densities in real backgrounds; measure recall-vs-density for query-based and dense decoders; instrument suppression; evaluate the calibration fix on real counted datasets.
- **Main Risk:** Synthetic planting realism; validate visibility with reader studies on a sample.
- **Research Cluster:** MED

### IDEA-C-0218 — Speckle is signal: despeckling preprocessing hurts ultrasound VFM transfer
- **One-sentence idea:** Test the negative result that ultrasound despeckling — standard preprocessing inherited from human-viewing pipelines — removes diagnostically-informative texture and degrades VFM-based segmentation, reversing an entrenched practice.
- **Problem:** Speckle is treated as noise because it hinders human reading, but it encodes tissue microstructure that learned models may exploit.
- **Core Hypothesis (falsifiable):** Frozen-VFM probes and fine-tuned models perform measurably worse on despeckled inputs than raw inputs across ultrasound segmentation tasks, with the gap largest for tissue-differentiation boundaries (where microstructure is the cue) and absent for anechoic-structure boundaries (where speckle truly is uninformative).
- **Why Important:** A pipeline default affecting all ultrasound ML, tested with a mechanism-resolving stratification (which boundaries need speckle).
- **Why Possibly Novel:** Speckle's information content is known in ultrasound physics (tissue characterization); the preprocessing-harm test for modern learned pipelines is undone.
- **Minimal Experiment:** Train/probe matched models on raw vs despeckled versions of public ultrasound datasets (CAMUS, breast); stratify by boundary type; report the interaction.
- **Main Risk:** Despeckling algorithms vary; test two standard ones.
- **Research Cluster:** MED

### IDEA-C-0219 — Window-conditioned multi-annotation reveals label multiplicity in CT
- **One-sentence idea:** Extend IDEA-C-0123's window-validity finding into a training paradigm: treat CT structures as having window-conditional ground truths and train window-conditioned models, testing whether explicit conditioning beats window-averaged training.
- **Problem:** If boundaries legitimately differ by viewing window (bone vs soft-tissue windows yield different valid contours), single-label training forces an incoherent average.
- **Core Hypothesis (falsifiable):** Window-conditioned models (window parameters as input conditioning) reproduce each window's annotation convention accurately, while unconditioned models trained on mixed-window labels produce intermediate contours matching neither; on downstream tasks with a declared window standard, conditioned models win by a measurable margin.
- **Why Important:** Introduces label multiplicity as a legitimate structure (one image, several correct answers indexed by a parameter) — generalizing beyond CT to exposure/gamma-conditioned labels anywhere.
- **Why Possibly Novel:** Conditioning on acquisition parameters exists; conditioning on the viewing convention that defines the label is a different, untested notion.
- **Minimal Experiment:** Use the IDEA-C-0123 multi-window annotations; train conditioned vs mixed models; evaluate per-window fidelity and downstream volume consistency.
- **Main Risk:** Requires the multi-window annotation set; piggyback on the earlier study's data.
- **Research Cluster:** MED

### IDEA-C-0220 — Allometric failure: pediatric transfer breaks along predictable scaling laws
- **One-sentence idea:** Test whether adult-trained medical segmentation models fail on pediatric anatomy in ways predicted by allometric scaling (organs scale non-uniformly with body size), enabling targeted scale-equivariant fixes instead of pediatric re-annotation.
- **Problem:** Pediatric data is scarce and adult models are deployed cross-age with unknown failure structure; if errors follow allometry, they are predictable and correctable.
- **Core Hypothesis (falsifiable):** Per-organ error of adult-trained models on pediatric scans correlates with that organ's allometric deviation from adult proportions (published growth curves), not with appearance difference; spatially-anisotropic rescaling informed by age-specific allometry recovers a large fraction of the deficit without any pediatric training data.
- **Why Important:** Pediatric imaging chronically lacks data; a physics-of-growth-informed correction sidesteps the data problem and demonstrates knowledge-based transfer.
- **Why Possibly Novel:** Age robustness is reported descriptively; the allometric prediction-and-correction framework is new.
- **Minimal Experiment:** Evaluate adult models on pediatric abdominal/brain datasets; regress per-organ deficits on allometric deviation; test age-conditioned anatomical rescaling as preprocessing.
- **Main Risk:** Pediatric appearance (ossification, contrast) also differs; the regression separates size from appearance components.
- **Research Cluster:** MED

### IDEA-C-0221 — Treatment-margin conventions masquerade as anatomy in radiotherapy labels
- **One-sentence idea:** Test whether models trained on radiotherapy target volumes (GTV/CTV) learn institution-specific margin-expansion conventions rather than tumor anatomy, making cross-hospital transfer fail in the specific geometry of margin policies.
- **Problem:** Target volumes encode clinical decisions (margins for microscopic spread) layered on anatomy; models can't distinguish the two, and institutions differ in policy.
- **Core Hypothesis (falsifiable):** Cross-institution evaluation shows systematic margin-sized boundary offsets (not random errors) aligned with documented policy differences; decomposed training (predict GTV anatomy + learn separable margin operator) transfers across institutions dramatically better than direct CTV prediction, isolating convention from anatomy.
- **Why Important:** Radiotherapy auto-contouring is deploying now; conflating policy with anatomy creates silent systematic dose-planning errors.
- **Why Possibly Novel:** Auto-contouring variability is documented; the anatomy/policy decomposition with a learnable margin operator as the transfer fix is new.
- **Minimal Experiment:** Compare cross-institution CTV predictions on shared-anatomy cases; measure offset structure vs policy documentation; train decomposed vs direct models; evaluate transfer.
- **Main Risk:** Public multi-institution radiotherapy data is limited; use challenge datasets with institution metadata.
- **Research Cluster:** MED

### IDEA-C-0222 — Lighting-pose entanglement makes endoscopic reflectance unlearnable
- **One-sentence idea:** Test whether the rigid camera-light coupling in endoscopy (illumination moves with viewpoint) makes reflectance-based tissue features fundamentally unidentifiable from standard video, explaining cross-scope generalization failures and motivating minimal hardware-side disentanglement.
- **Problem:** Endoscopic models generalize poorly across scopes/procedures; if illumination-pose entanglement prevents separating tissue reflectance from shading, no amount of data from standard scopes fixes it.
- **Core Hypothesis (falsifiable):** Models trained on standard endoscopy encode features where reflectance and shading are provably mixed (probes cannot decode albedo-like invariants that multi-light captures show exist); training data from even sparse multi-illumination captures (scope with alternating light sources) enables disentangled features that transfer across scopes measurably better at matched data volume.
- **Why Important:** Identifies a sensor-side root cause of a persistent clinical-ML failure, with a concrete minimal-hardware remedy — an identifiability argument, not a model tweak.
- **Why Possibly Novel:** Photometric endoscopy exists in reconstruction; the identifiability framing for learned segmentation features with a transfer endpoint is new.
- **Minimal Experiment:** Use existing multi-illumination endoscopic datasets (or phantom captures) to train entangled vs disentangled features; probe for albedo invariants; compare cross-device segmentation transfer.
- **Main Risk:** Multi-illumination clinical data is rare; phantom and ex-vivo captures suffice for the identifiability core.
- **Research Cluster:** MED

### IDEA-C-0223 — Where does bias-field invariance form? MRI's natural PEFT laboratory
- **One-sentence idea:** Use MRI bias fields (smooth multiplicative intensity variation) as a controlled testbed to locate where in a VFM invariance to a known nuisance forms during PEFT, testing whether invariance depth predicts which PEFT placements can learn it.
- **Problem:** PEFT placement theory (which layers to adapt) lacks a controlled nuisance whose invariance can be measured precisely; bias fields are parametrically generable and clinically real.
- **Core Hypothesis (falsifiable):** Bias-field invariance (feature stability under synthetic fields) forms at characteristic layers during full fine-tuning; PEFT placed at or before those layers achieves invariance and downstream robustness, while later placement provably cannot (invariance requires transforming features before nuisance mixing) — validated by the placement-performance pattern.
- **Why Important:** Delivers a general placement principle (adapt at or before the nuisance-mixing depth) from a clean measurable case.
- **Why Possibly Novel:** PEFT placement studies are empirical grab-bags; using a parametric nuisance to derive and test a placement law is new.
- **Minimal Experiment:** Apply synthetic bias fields to MRI datasets; measure layer-wise feature sensitivity; run PEFT placement sweeps; test the predicted placement cutoff.
- **Main Risk:** Findings may be nuisance-specific; replicate with a second parametric nuisance (gamma shifts).
- **Research Cluster:** MED

### IDEA-C-0224 — Touching-cell boundaries are a third class, not a boundary case
- **One-sentence idea:** Formalize and test the claim that cell-cell interfaces in dense microscopy are semantically distinct from cell-background boundaries (different physics, different error costs) and should be a separate prediction class rather than an edge case of binary segmentation.
- **Problem:** Instance separation of touching cells is handled by post-hoc watersheds and boundary weighting; the underlying issue — two boundary types with different statistics collapsed into one class — remains unformalized.
- **Core Hypothesis (falsifiable):** Three-class training (cell / background / cell-cell interface) with interface-specific loss outperforms binary+watershed and boundary-weighted baselines specifically on merge-error rates at high densities, and the interface class's learned features are measurably distinct (interface ≠ background-boundary features), confirming semantic separateness.
- **Why Important:** Merge errors dominate error budgets in dense microscopy pipelines feeding biology; and the type-distinct-boundary principle generalizes (touching organs, adjacent buildings).
- **Why Possibly Novel:** Three-class tricks exist in cell-segmentation folklore; the systematic formalization with feature-level validation and cross-domain generalization claims is worth establishing rigorously.
- **Minimal Experiment:** Train the three formulations on dense-cell benchmarks with density sweeps; decompose merge/split errors; probe feature separation between boundary types.
- **Main Risk:** Mostly confirms folklore — but quantifying it and extending to non-cell domains carries the novelty.
- **Research Cluster:** MED

### IDEA-C-0225 — Clinically-weighted metrics reorder segmentation models: dose-error as the endpoint
- **One-sentence idea:** Test whether ranking radiotherapy-adjacent segmentation models by simulated dosimetric consequence (dose-volume errors from contour errors) reorders them relative to Dice ranking, quantifying how misaligned the field's metric is with clinical harm.
- **Problem:** Contour errors matter nonlinearly by location (near organs-at-risk) and direction; Dice weights all errors equally, so model selection may be optimizing the wrong thing.
- **Core Hypothesis (falsifiable):** Running published contours through standard treatment-planning simulation shows dose-error rankings diverging from Dice rankings for a substantial fraction of model pairs, with divergence predictable from where (relative to risk structures) each model's errors concentrate.
- **Why Important:** If rankings flip under the clinically-meaningful metric, challenge design and model selection across medical segmentation need revision.
- **Why Possibly Novel:** Dosimetric evaluation exists in medical-physics case studies; a systematic model-ranking comparison against Dice at benchmark scale is new to the ML community.
- **Minimal Experiment:** Take public contour predictions from a head-neck challenge; run automated planning simulation; compare metric rankings and characterize the error-geography that drives divergence.
- **Main Risk:** Planning simulation choices affect results; use two planning systems/protocols.
- **Research Cluster:** MED

### IDEA-C-0226 — Bilateral symmetry is free augmentation: an organ-symmetry sample-efficiency law
- **One-sentence idea:** Test whether few-shot segmentation sample efficiency for bilateral organs (kidneys, lungs, hippocampi) is predictably higher than for midline organs because reflection provides a valid free augmentation — and formalize the symmetry-to-efficiency exchange rate.
- **Problem:** Few-shot medical budgeting treats all organs alike; anatomical symmetry is an obvious but unquantified data multiplier.
- **Core Hypothesis (falsifiable):** Learning curves show bilateral organs reaching target Dice at roughly half the labeled volumes of asymmetry-matched midline controls when reflection augmentation is used, with the gain disappearing when reflection is disabled — a clean causal chain from anatomical symmetry to sample efficiency, extendable to other symmetry groups (tubular translation symmetry).
- **Why Important:** Refines annotation budgeting (IDEA-C-0207's meter) with anatomy-aware priors and exemplifies exploiting known structure instead of collecting data.
- **Why Possibly Novel:** Flipping is universal augmentation; its organ-symmetry-conditional value quantification and budgeting integration are new.
- **Minimal Experiment:** Fit few-shot learning curves for bilateral vs midline organs (AMOS) with reflection on/off; measure the efficiency ratio; test extension to vertebra translation symmetry.
- **Main Risk:** Organ difficulty confounds; match control organs on size/contrast.
- **Research Cluster:** MED

### IDEA-C-0227 — The silent DICOM-preprocessing variance across public codebases
- **One-sentence idea:** Audit divergence in DICOM preprocessing (rescale slope/intercept handling, orientation, spacing resampling) across popular public medical-ML codebases, quantifying how much reported cross-paper performance difference it silently generates.
- **Problem:** Medical pipelines re-implement DICOM handling with subtle differences; models are compared as if inputs were identical.
- **Core Hypothesis (falsifiable):** Running identical checkpoints through the actual preprocessing code of 6 popular repositories produces Dice differences on standard benchmarks comparable to typical published method deltas, with orientation/spacing handling as the dominant contributors — establishing a reproducibility noise floor for the field.
- **Why Important:** A concrete, fixable reproducibility hazard in the highest-stakes application domain, with a standardization artifact (reference preprocessing + conformance tests) as the deliverable.
- **Why Possibly Novel:** Preprocessing sensitivity is acknowledged; the cross-codebase audit with variance attribution and a conformance suite is not done.
- **Minimal Experiment:** Wrap 6 repos' preprocessing on the same DICOM sets; evaluate 3 checkpoints through each; decompose variance by preprocessing stage; publish conformance tests.
- **Main Risk:** None substantial; engineering-heavy but low-risk and high-service value.
- **Research Cluster:** MED

### IDEA-C-0228 — Curvature-spectrum-optimal slice selection for sparse 3D annotation
- **One-sentence idea:** Test whether the optimal spacing/selection of slices to annotate in 3D volumes is predictable from the structure's through-plane curvature spectrum (annotate densely where shape changes fast), beating uniform spacing at matched budget.
- **Problem:** Sparse-slice annotation (then interpolation or interpolation-free training, IDEA-C-0107) uses uniform spacing by default, ignoring that shape information density varies enormously along the axis.
- **Core Hypothesis (falsifiable):** Given a target reconstruction error, curvature-adaptive slice selection (computable from a cheap initial contour or registration prior) requires substantially fewer annotated slices than uniform spacing across organ types, with the saving predicted by the measured spectrum — a sampling-theory result for annotation.
- **Why Important:** Directly reduces the largest cost in volumetric dataset construction with a principled, per-structure rule.
- **Why Possibly Novel:** Active slice selection exists heuristically; the spectral-sampling formulation with predicted savings is new.
- **Minimal Experiment:** On fully-annotated volumes, simulate annotation budgets under uniform vs curvature-adaptive selection; measure reconstruction/downstream-training error; validate the spectral prediction of savings across organs.
- **Main Risk:** The initial shape estimate needed for adaptivity may be circular; test with deliberately crude priors.
- **Research Cluster:** MED

### IDEA-C-0229 — Sequence-dropout reveals shortcut hierarchies in multi-sequence MRI models
- **One-sentence idea:** Test whether multi-sequence MRI segmentation models collapse onto one dominant sequence (shortcut reliance), using systematic sequence-dropout at inference to measure reliance hierarchies and sequence-dropout training to force distributed use.
- **Problem:** Multi-sequence models are assumed to integrate complementary contrasts; if they secretly rely on one sequence, they fail silently when that sequence is missing/degraded — common in practice.
- **Core Hypothesis (falsifiable):** Inference-time sequence ablation reveals strongly skewed reliance (one sequence's removal collapsing performance, others' removal costing little) inconsistent with each sequence's standalone information content (measured by single-sequence models) — proving shortcut collapse; dropout-style sequence masking during training equalizes reliance and improves missing-sequence robustness at minor clean-data cost.
- **Why Important:** Missing sequences are the norm in real-world MRI; reliance auditing should become a standard reporting item, and the fix is one line of training code.
- **Why Possibly Novel:** Modality dropout exists in multimodal learning; the reliance-vs-information-content mismatch analysis quantifying shortcut collapse in medical multi-sequence models is new.
- **Minimal Experiment:** On BraTS, measure ablation reliance vs single-sequence informativeness; train with sequence dropout; evaluate the missing-sequence robustness frontier.
- **Main Risk:** Some skew is information-appropriate; the mismatch metric (reliance minus informativeness) handles this.
- **Research Cluster:** MED

### IDEA-C-0230 — Free-text laterality errors: a label-noise channel unique to report-mined datasets
- **One-sentence idea:** Quantify left-right laterality errors in datasets auto-mined from radiology reports (a documented human-error class in reporting), and test whether symmetric-anatomy models trained on such data inherit measurable laterality confusion correctable by consistency filtering.
- **Problem:** Report-mined supervision inherits clinical documentation errors; laterality mistakes are a known, discrete, auditable error class whose downstream imprint nobody has measured.
- **Core Hypothesis (falsifiable):** Cross-checking report-derived laterality labels against image-derived anatomical laterality (cheap to automate for many findings) reveals error rates consistent with clinical-documentation literature; models trained on unfiltered data show inflated left-right confusion on balanced test sets, and consistency-filtered training removes the excess.
- **Why Important:** Report-mining is scaling medical datasets rapidly; characterizing its specific error channels (starting with the cleanest one) is due diligence the field is skipping.
- **Why Possibly Novel:** Report-label noise is treated as generic; isolating a discrete, verifiable error class with an imprint-and-fix study is new.
- **Minimal Experiment:** Build an image-based laterality checker for selected findings; audit a report-mined dataset; train with/without filtering; evaluate laterality confusion on curated balanced tests.
- **Main Risk:** Image-based laterality checking has its own errors; bound them with manual verification on a sample.
- **Research Cluster:** MED
## Cluster RSIND — Remote Sensing & Industrial Inspection Exposing General Principles (IDEA-C-0231 … IDEA-C-0255)

### IDEA-C-0231 — Early-layer rotation retrofits suffice for overhead imagery
- **One-sentence idea:** Test whether the orientation brittleness of ground-level-pretrained VFMs on aerial imagery is concentrated in early layers, so that rotation-equivariant retrofitting (or rotation-augmented PEFT) of only the first few blocks recovers full rotation robustness at minimal cost.
- **Problem:** Remote-sensing practitioners either retrain VFMs on overhead data or use full rotation augmentation; if orientation priors live shallow, the fix is far cheaper.
- **Core Hypothesis (falsifiable):** Layer-wise rotation-sensitivity profiles show early layers dominating orientation variance; rotation-adapting only those layers achieves rotation-invariance and aerial accuracy statistically matching full-model adaptation, while late-layer-only adaptation fails — localizing where gravity priors are stored.
- **Why Important:** A general "where do priors live" methodology with an immediate cost saving for a major application field.
- **Why Possibly Novel:** Rotation equivariance and aerial adaptation are studied separately; the layer-localization claim with a targeted-retrofit test is new.
- **Minimal Experiment:** Measure per-layer feature rotation-sensitivity of DINOv2 on aerial data; run depth-restricted rotation-augmented PEFT variants on iSAID; compare rotation-robustness and accuracy.
- **Main Risk:** Orientation handling may be distributed; the profile measurement answers this either way.
- **Research Cluster:** RSIND

### IDEA-C-0232 — GSD is a hidden shortcut variable: absolute scale leaks into land-cover models
- **One-sentence idea:** Test whether remote-sensing models exploit ground-sample-distance (GSD) as a shortcut (predicting class from apparent texture scale rather than content), and whether GSD-conditioned normalization removes systematic cross-sensor failures.
- **Problem:** Datasets couple classes to acquisition GSD (crops imaged at one resolution, urban at another); models may bind semantics to absolute scale and break on new sensors.
- **Core Hypothesis (falsifiable):** Models trained on GSD-confounded data misclassify GSD-resampled test imagery in the direction predicted by the training coupling (texture-scale-following errors); explicit GSD conditioning (metadata input) or scale-decoupled training removes the error mode and improves cross-sensor transfer measurably.
- **Why Important:** Cross-sensor generalization is the central practical problem of the field; a named, testable shortcut mechanism focuses the fix.
- **Why Possibly Novel:** Scale augmentation is routine; the GSD-class coupling audit and metadata-conditioning comparison against it are not.
- **Minimal Experiment:** Measure class-GSD coupling in public land-cover datasets; construct resampled counterfactual tests; compare augmentation vs conditioning fixes.
- **Main Risk:** Resampling artifacts confound; use sensor-simulation-based resampling.
- **Research Cluster:** RSIND

### IDEA-C-0233 — Sun-geometry consistency as free physics supervision for aerial imagery
- **One-sentence idea:** Exploit known sun position (from timestamp/geolocation metadata) as a physics constraint: shadows must be consistent with solar geometry, providing free supervision for shadow segmentation, height estimation, and false-positive rejection.
- **Problem:** Aerial pipelines treat shadows as noise or learn them statistically, ignoring that the light source's exact position is in the metadata — an unused hard constraint.
- **Core Hypothesis (falsifiable):** A consistency loss tying predicted shadow masks to sun-geometry-projected object masks improves both shadow and object segmentation over unconstrained training at zero annotation cost, and flags label errors (shadows mislabeled as objects) with high precision via constraint violation.
- **Why Important:** Demonstrates metadata-physics as a supervision channel — a general principle extendable to any geometry-documented imaging (satellite angles, medical gantry positions).
- **Why Possibly Novel:** Shadow-geometry reasoning exists in photogrammetry; wiring it as a training loss and label-audit tool for learned segmentation is new.
- **Minimal Experiment:** On timestamped aerial datasets, implement the solar-consistency loss for buildings; measure segmentation gains and label-error-flagging precision against manual audit.
- **Main Risk:** Terrain slope complicates projection; start with flat-scene subsets and add DEMs later.
- **Research Cluster:** RSIND

### IDEA-C-0234 — Climate is a confounder: cloud statistics correlate with land-cover class
- **One-sentence idea:** Audit satellite benchmarks for geographic-climatic confounding — cloud/haze frequency correlating with land-cover classes by latitude/climate zone — and test whether models exploit atmospheric statistics as class evidence.
- **Problem:** Tropical classes co-occur with tropical atmospheres; models may read haze signatures instead of land cover, failing on atypical-weather acquisitions.
- **Core Hypothesis (falsifiable):** Atmospheric parameters estimated from imagery predict land-cover class above chance in popular benchmarks; evaluation on atmosphere-decoupled data (same class, atypical atmospheric conditions, or physically haze-normalized) drops accuracy in proportion to the measured coupling, and atmospheric normalization at train time restores it.
- **Why Important:** Climate-confounded models will systematically mispredict under climate change and season shifts — the exact deployment conditions monitoring systems exist for.
- **Why Possibly Novel:** Atmospheric correction is standard preprocessing; auditing residual atmosphere-class coupling as a learned shortcut is not.
- **Minimal Experiment:** Estimate atmospheric parameters on benchmark tiles; measure class coupling; build decoupled test splits; evaluate models with and without physics-based atmospheric normalization.
- **Main Risk:** Some coupling is legitimate ecology (rainforests are cloudy); distinguish acquisition atmosphere from climate class by multi-date imagery of the same tiles.
- **Research Cluster:** RSIND

### IDEA-C-0235 — Log-transform gets SAR most of the way: multiplicative noise is the domain gap
- **One-sentence idea:** Test whether the optical-to-SAR transfer gap for VFMs is dominated by the multiplicative (speckle) noise structure rather than content statistics, so that log-domain input transformation plus light PEFT rivals dedicated SAR architectures.
- **Problem:** SAR is treated as an alien modality requiring specialist models; if the gap is mostly noise-model mismatch (multiplicative vs additive), a one-line transform changes the economics.
- **Core Hypothesis (falsifiable):** Frozen-VFM probe performance on SAR segmentation improves dramatically under log-transform (converting multiplicative to additive noise) relative to raw or linearly-normalized input, closing most of the gap to SAR-pretrained models; residual gaps concentrate in geometry-specific phenomena (layover, shadow) identifiable a priori.
- **Why Important:** Vastly cheaper SAR capability if true, and a clean demonstration that noise-model alignment is a first-order transfer variable.
- **Why Possibly Novel:** Log-scaling is common SAR practice; the decomposition of the VFM transfer gap into noise-model vs content components, with residual attribution, is new.
- **Minimal Experiment:** Probe frozen VFMs on SAR benchmarks under input-transform sweeps; compare against SAR-pretrained baselines; attribute residual errors to geometric phenomena via incidence-angle stratification.
- **Main Risk:** SAR geometry effects may dominate for urban scenes; the stratified attribution keeps the result informative regardless.
- **Research Cluster:** RSIND

### IDEA-C-0236 — Roof-vs-footprint conventions create geometrically correctable cross-dataset offsets
- **One-sentence idea:** Show that building-extraction datasets inconsistently annotate roof outlines vs ground footprints, producing off-nadir-angle-dependent systematic offsets that can be corrected geometrically (angle × height) rather than learned away.
- **Problem:** Cross-dataset building benchmarks mix two label ontologies (roof vs footprint) whose difference is a deterministic function of viewing geometry and building height, but treat it as generic noise.
- **Core Hypothesis (falsifiable):** Cross-dataset evaluation errors on buildings correlate with off-nadir angle × estimated height exactly as the parallax model predicts; applying the geometric correction (or conditioning on the declared ontology) removes the majority of the cross-dataset gap for buildings without any adaptation training.
- **Why Important:** Buildings are the most-mapped object class on Earth; a deterministic ontology reconciliation beats data-hungry adaptation and exemplifies convention-vs-content decomposition (echoing MED's IDEA-C-0221).
- **Why Possibly Novel:** Roof/footprint discrepancies are known in GIS; quantifying them as the dominant cross-dataset ML gap with a closed-form fix is new to the learning community.
- **Minimal Experiment:** Measure prediction offsets vs off-nadir metadata across building datasets; fit the parallax model; apply correction; re-evaluate cross-dataset transfer.
- **Main Risk:** Height estimates needed for full correction; use shadow-derived heights (IDEA-C-0233 synergy) or offset-direction-only tests.
- **Research Cluster:** RSIND

### IDEA-C-0237 — Mosaic seam lines are learned as phantom boundaries
- **One-sentence idea:** Test whether models trained on mosaicked satellite products learn seam-line artifacts (radiometric steps between acquisition swaths) as boundary evidence, hallucinating land-cover edges along seams in deployment.
- **Problem:** Training tiles cut from mosaics contain invisible-to-curators seam discontinuities that correlate with nothing on the ground, yet look exactly like class boundaries to a model.
- **Core Hypothesis (falsifiable):** Seam locations (recoverable from product metadata or step-detection) attract predicted boundaries at rates far above matched non-seam radiometric gradients; seam-aware training (masking loss near seams or seam augmentation on seamless data) removes the phantom-boundary behavior measurably.
- **Why Important:** Phantom edges corrupt change detection and cadastral mapping downstream; and it is a clean instance of the general pipeline-artifact-as-feature trap.
- **Why Possibly Novel:** Mosaic artifacts are a remote-sensing production concern; their imprint on learned segmentation behavior is undocumented.
- **Minimal Experiment:** Recover seams on public mosaicked training sets; measure boundary-attraction statistics; retrain seam-aware; evaluate on seamless single-acquisition test data.
- **Main Risk:** Seam metadata may be unavailable; step-detection recovery works but needs validation.
- **Research Cluster:** RSIND

### IDEA-C-0238 — Fixture alignment is the secret feature of industrial anomaly detectors
- **One-sentence idea:** Test whether industrial anomaly-detection performance on standard benchmarks depends on the rigid fixture alignment of "good" training images — detectors keying on positional deviation rather than defect appearance — by evaluating under controlled pose jitter.
- **Problem:** MVTec-style benchmarks photograph parts in near-perfect registration; deployed lines have pose variation, and it is unknown how much reported performance is alignment-dependence in disguise.
- **Core Hypothesis (falsifiable):** Introducing small in-plane pose jitter (within realistic line tolerances) at test time degrades reconstruction- and embedding-based detectors far more than defect-visibility changes justify, with degradation proportional to each method's measured positional sensitivity; alignment-free methods (registration front-ends or pose-invariant features) show flat curves.
- **Why Important:** Predicts real-line performance from a benchmark property nobody controls, and reframes method comparison around pose-robustness — the deployment-binding axis.
- **Why Possibly Novel:** Augmentation studies exist for anomaly detection; framing fixture alignment as the hidden benchmark variable with jitter-response curves as the diagnostic is new.
- **Minimal Experiment:** Evaluate 6 anomaly methods on MVTec-AD under pose-jitter sweeps; decompose degradation into alignment vs visibility components using registered-back comparisons.
- **Main Risk:** Jitter simulation vs real refixturing differences; validate with a small real re-shoot of one product.
- **Research Cluster:** RSIND

### IDEA-C-0239 — Texture-statistic coverage, not defect count, predicts unseen-defect generalization
- **One-sentence idea:** Test whether generalization to novel defect types scales with the coverage of background texture statistics in training (how well normal-appearance space is charted) rather than with the number of defect types seen — reframing inspection data collection around normality coverage.
- **Problem:** Inspection teams collect ever-more defect examples, though anomaly generalization may be governed by how completely "normal" is modeled, not how many anomalies were seen.
- **Core Hypothesis (falsifiable):** Across controlled training mixtures, novel-defect detection correlates strongly with measured normal-texture coverage (density-model likelihood of held-out normal patches) and weakly with training defect-type count once a small count is exceeded — with the coverage metric predicting per-product generalization prospectively.
- **Why Important:** Redirects the biggest cost in inspection ML (defect collection is expensive; normal data is free) with a measurable planning criterion.
- **Why Possibly Novel:** One-class vs supervised inspection are compared as methods; the data-property law (coverage vs count) governing both is untested.
- **Minimal Experiment:** On multi-defect datasets, train mixtures varying (normal diversity × defect-type count); evaluate on held-out defect types; regress generalization on both factors.
- **Main Risk:** Coverage metrics are estimator-dependent; use two density estimators for agreement.
- **Research Cluster:** RSIND

### IDEA-C-0240 — Zero-shot self-similarity beats trained models on novel repeating products
- **One-sentence idea:** Test whether a training-free method using only within-image self-similarity (each patch compared to the same product's other periods) outperforms models trained on other products for defect segmentation on novel periodic items — quantifying when learning is unnecessary.
- **Problem:** Inspection deployments face constant product turnover; per-product training is the cost bottleneck, yet the periodic structure of each new product carries its own normal model.
- **Core Hypothesis (falsifiable):** On unseen periodic products, self-similarity defect scoring (feature-space comparison across detected periods, building on IDEA-C-0169's lattice detection) beats cross-product-trained detectors by a margin that grows with product novelty, with the crossover predictable from a periodicity-strength score — defining the regime where zero-shot structure exploitation dominates learning.
- **Why Important:** Establishes a learning-vs-structure decision boundary for a large industrial segment and challenges the train-for-everything default.
- **Why Possibly Novel:** Self-similarity heuristics exist in classical inspection; benchmarking them against modern learned detectors under novelty gradients with a regime rule is new.
- **Minimal Experiment:** Implement feature-space periodic self-similarity scoring; compare against cross-product-trained SOTA on held-out periodic products stratified by novelty; fit the regime boundary.
- **Main Risk:** Aperiodic defects spanning whole periods evade self-similarity; characterize this failure class explicitly.
- **Research Cluster:** RSIND

### IDEA-C-0241 — Emissivity-temperature confusion structures thermal segmentation errors
- **One-sentence idea:** Test whether thermal-image segmentation errors are structured by the physical confound that observed radiance mixes temperature with material emissivity, predicting systematic confusions (low-emissivity hot objects read as cool) that RGB-thermal fusion resolves in a physics-predictable pattern.
- **Problem:** Thermal segmentation is treated as grayscale RGB; its errors look random unless viewed through the radiance equation, which predicts exactly which materials will be confused.
- **Core Hypothesis (falsifiable):** Error analysis on thermal benchmarks shows confusion pairs concentrated where emissivity differences oppose temperature differences (metallic surfaces); per-class error rates are predictable from tabulated emissivity ranges, and fusion gains concentrate precisely on the predicted pairs — validating a physics-driven error model.
- **Why Important:** Physics-predictable error structure enables deployment risk assessment without exhaustive testing — a general template for sensor-physics-aware evaluation.
- **Why Possibly Novel:** Thermal-RGB fusion is studied for accuracy; the emissivity-based error prediction framework is new to learned segmentation.
- **Minimal Experiment:** Analyze confusion matrices of thermal segmenters on driving/industrial thermal datasets against emissivity tables; test the fusion-gain localization prediction.
- **Main Risk:** Emissivity tables are approximate for real surfaces; use relative predictions (ordering) rather than absolutes.
- **Research Cluster:** RSIND

### IDEA-C-0242 — Sub-pixel co-registration error is the performance bound for small-change detection
- **One-sentence idea:** Quantify how residual co-registration error between image pairs bounds change-detection performance for small changes, testing whether reported method differences on standard benchmarks fall below this geometric noise floor.
- **Problem:** Change-detection methods compete on benchmarks whose image pairs have unmeasured registration residuals; for changes near the residual scale, rankings may reflect nothing but noise-fitting.
- **Core Hypothesis (falsifiable):** Injecting controlled sub-pixel misregistration shows detection accuracy for changes below k× the registration residual degrading to chance (measurable k); auditing benchmark residuals (via stable-region matching) reveals that a substantial fraction of "small change" test instances fall below the bound, where published method differences are statistically meaningless.
- **Why Important:** Establishes a physical noise floor that change-detection evaluation must report — the field's equivalent of a detection limit.
- **Why Possibly Novel:** Registration sensitivity is known qualitatively; the quantitative bound derivation and benchmark audit against it are new.
- **Minimal Experiment:** Measure benchmark registration residuals from invariant regions; run controlled misregistration sweeps on 4 methods; locate the degradation bound; stratify published comparisons by change-size-to-residual ratio.
- **Main Risk:** Residual measurement itself has error; use multiple estimation approaches.
- **Research Cluster:** RSIND

### IDEA-C-0243 — Cadastral vs agronomic boundaries: national labeling ontologies clash in field delineation
- **One-sentence idea:** Test whether cross-country failure of crop-field boundary models stems from datasets mixing two boundary ontologies — legal parcel (cadastral) vs agronomic management boundaries — that coincide in some countries and diverge in others.
- **Problem:** Field-delineation models trained in one region fail elsewhere; appearance shift takes the blame, but the target concept itself may differ (what counts as a field boundary is jurisdiction-dependent).
- **Core Hypothesis (falsifiable):** In regions where cadastral and agronomic boundaries diverge (verifiable from public parcel registries vs imagery), model errors concentrate exactly on divergence sites, with error geometry matching the ontology mismatch rather than appearance difficulty; ontology-conditioned training (predict both boundary types) restores cross-region transfer.
- **Why Important:** Agricultural monitoring underpins subsidy and food-security systems; ontology confusion produces confidently-wrong maps, and the diagnosis generalizes to all cross-jurisdiction mapping.
- **Why Possibly Novel:** Cross-region transfer failure is documented; the label-ontology decomposition with registry-based verification is new.
- **Minimal Experiment:** Overlay parcel registries on imagery for two divergent regions; classify test errors by divergence-site status; train dual-ontology models; measure transfer recovery.
- **Main Risk:** Registry access varies; the EU's public parcel systems suffice.
- **Research Cluster:** RSIND

### IDEA-C-0244 — The texture-to-instance phase transition as resolution crosses object scale
- **One-sentence idea:** Characterize the resolution threshold at which object classes transition from texture (statistical aggregate: "parking lot") to instances (countable: "cars"), testing whether models exhibit a sharp representational phase transition and whether task definitions should switch at the measured boundary.
- **Problem:** The same ground content is a texture at 2 m GSD and instances at 15 cm; datasets and models treat the task as fixed, producing incoherent supervision near the transition.
- **Core Hypothesis (falsifiable):** Model behavior (feature statistics, count-vs-area prediction reliability) changes sharply rather than smoothly across a resolution sweep at a class-specific threshold predictable from object size and spacing; hybrid supervision (density below threshold, instances above) beats either pure formulation in the transition zone.
- **Why Important:** Establishes task identity as resolution-dependent — a foundational point for multi-resolution systems, with practical supervision guidance.
- **Why Possibly Novel:** Scale-adaptive models exist; the phase-transition characterization with a task-switching rule is a new framing.
- **Minimal Experiment:** Resolution-sweep experiments on vehicle/tree classes in high-res aerial data; measure representational discontinuities and prediction-reliability crossovers; test the hybrid supervision in the transition band.
- **Main Risk:** Transitions may be gradual for irregular objects; the sharpness measurement is itself the finding.
- **Research Cluster:** RSIND

### IDEA-C-0245 — Band-permutation sensitivity reveals color-semantic binding in VFMs
- **One-sentence idea:** Measure how VFM performance on multispectral false-color composites depends on which bands map to RGB channels, testing whether pretrained color-semantic bindings (green=vegetation) persist and distort spectral reasoning.
- **Problem:** Remote-sensing practice feeds arbitrary band composites into RGB-pretrained VFMs; if the model attributes meaning to channel identity, composite choice becomes an invisible hyperparameter with semantic consequences.
- **Core Hypothesis (falsifiable):** Performance across band-to-channel permutations of identical spectral content varies far beyond seed noise, with the best permutation being the one aligning spectral roles to natural color-semantic conventions (vegetation→green); channel-symmetrized adaptation (permutation augmentation) removes the sensitivity at a small cost to the best case — quantifying the binding's strength and price.
- **Why Important:** A hidden hyperparameter audit for the entire multispectral-VFM practice, plus a measurement of how deeply color semantics are baked into VFMs.
- **Why Possibly Novel:** Band selection is studied for information content; the channel-binding sensitivity of pretrained VFMs is unexamined.
- **Minimal Experiment:** Evaluate frozen and PEFT-adapted VFMs across band permutations on Sentinel-2 segmentation; quantify permutation variance; test symmetrized training.
- **Main Risk:** Permutation effects may interact with normalization statistics; control input scaling carefully.
- **Research Cluster:** RSIND

### IDEA-C-0246 — Netlists as label grammar: circuit topology constrains PCB segmentation
- **One-sentence idea:** Use PCB inspection to test structured-prior segmentation: the design netlist specifies exactly which conductive regions must be connected/isolated, providing a formal correctness grammar that pixel supervision lacks — and a testbed for grammar-constrained dense prediction generally.
- **Problem:** PCB defect detection treats boards as textures, ignoring that the ground-truth electrical topology is available by construction and defines defects (shorts/opens) exactly.
- **Core Hypothesis (falsifiable):** Decoding trace segmentation under netlist connectivity constraints (differentiable connectivity penalties or constrained post-processing) detects electrically-meaningful defects (shorts, opens) with far higher precision than unconstrained segmentation at equal recall, and the constraint value grows as visual evidence degrades (low contrast, occlusion) — quantifying what formal structure buys.
- **Why Important:** A clean, economically-relevant instance of grammar-constrained dense prediction, informing how to exploit formal priors (maps, CAD, anatomy graphs) elsewhere.
- **Why Possibly Novel:** Design-data-assisted inspection exists industrially in ad-hoc forms; the formal constrained-decoding formulation with degradation-response quantification is new to the research literature.
- **Minimal Experiment:** On public PCB datasets with reconstructed netlists, compare constrained vs unconstrained decoding across synthetic degradation sweeps; report the constraint-value curve.
- **Main Risk:** Netlist reconstruction for public data takes effort; a small set of boards suffices.
- **Research Cluster:** RSIND

### IDEA-C-0247 — Single-image gloss segmentation has a measurable irreducible error
- **One-sentence idea:** Quantify the fundamental ill-posedness of surface-finish (gloss/matte) segmentation from single images — the same pixels being consistent with multiple finish/illumination explanations — establishing the irreducible error floor that no model can beat without illumination sweeps.
- **Problem:** Inspection buyers demand single-image gloss classification; vendors train ever-bigger models against an ill-posedness bound nobody has measured.
- **Core Hypothesis (falsifiable):** Physically-based rendering of finish-illumination ambiguity classes establishes a confusion floor; human experts and models both converge to this floor on single images (validated on multi-light ground truth), while two-image illumination variation eliminates it — proving the limit is informational, not model capacity.
- **Why Important:** Separates model-solvable from physically-unsolvable inspection problems, redirecting procurement toward capture design — a general lesson in ill-posedness accounting before model shopping.
- **Why Possibly Novel:** Gloss perception ambiguity is studied in vision science; its formalization as an inspection error floor with capture-design implications is new to applied ML.
- **Minimal Experiment:** Render ambiguity-matched finish pairs; test experts and models single- vs multi-image; measure convergence to the predicted floor; validate on real multi-light captures.
- **Main Risk:** Real materials may be less ambiguous than worst-case renders; report floor distributions across material families.
- **Research Cluster:** RSIND

### IDEA-C-0248 — Visibility-conditioned recall: crack detection depends on sun angle by geometry
- **One-sentence idea:** Test whether surface-crack detectability in outdoor inspection (blades, bridges, pavement) follows a predictable function of illumination angle relative to crack orientation (raking light reveals; frontal light hides), making inspection scheduling a measurable part of system performance.
- **Problem:** Inspection ML reports single recall numbers, though crack contrast is a strong function of controllable capture geometry — conflating model quality with lucky lighting.
- **Core Hypothesis (falsifiable):** Recall as a function of (sun-angle, crack-orientation) follows the shadow-contrast model's prediction across datasets, with orientation-integrated recall varying severalfold across capture times; angle-aware evaluation (report recall surfaces, not scalars) reorders methods whose training data had different lighting distributions.
- **Why Important:** Establishes capture-geometry-conditioned evaluation for outdoor inspection — the difference between a model that works and an inspection system that works.
- **Why Possibly Novel:** Lighting effects are folklore among practitioners; the quantitative visibility model with evaluation-protocol consequences is unformalized.
- **Minimal Experiment:** Use timestamped inspection datasets (or controlled captures of cracked samples across angles); fit the visibility model; re-evaluate methods under angle-stratified protocols.
- **Main Risk:** Crack orientation annotation needed; automate from ground truth masks.
- **Research Cluster:** RSIND

### IDEA-C-0249 — Canonicalize, don't augment: constant motion blur should be inverted, not learned
- **One-sentence idea:** Use conveyor-belt imaging (known constant blur direction/magnitude) to test the general principle that deterministic, parameterized nuisances are better removed by canonicalization (deconvolution to a canonical frame) than absorbed by augmentation-trained invariance.
- **Problem:** The field defaults to augmentation for every nuisance; when the nuisance is known and invertible, invariance wastes capacity and loses information — but the comparison is rarely run cleanly.
- **Core Hypothesis (falsifiable):** At matched compute, canonicalization (motion deblur with known kernel) plus standard training beats blur-augmented invariance training on defect segmentation, with the gap growing as blur magnitude increases and as model capacity shrinks — mapping the regime where each strategy wins.
- **Why Important:** A clean decision rule (canonicalize known nuisances, augment unknown ones) with immediate line-deployment value and general applicability (rectification, exposure, orientation).
- **Why Possibly Novel:** Both strategies are old; the controlled head-to-head with regime mapping on a real parameterized nuisance is missing.
- **Minimal Experiment:** Simulate/capture conveyor blur at known parameters; train canonicalized vs augmented pipelines across blur levels and model sizes; map the winner regime.
- **Main Risk:** Deconvolution artifacts at high blur; include artifact-aware variants.
- **Research Cluster:** RSIND

### IDEA-C-0250 — Colorimetric grounding beats domain adaptation for chemistry-linked classes
- **One-sentence idea:** Test whether corrosion/contamination segmentation transfers across cameras better via colorimetric calibration (color-chart-based mapping to device-independent color space) than via learned domain adaptation, because the class is defined by chemistry-linked spectral properties.
- **Problem:** Cross-camera transfer for color-critical classes is attacked with adaptation networks, ignoring that a physical color-management solution exists whenever the class's evidence is genuinely colorimetric.
- **Core Hypothesis (falsifiable):** For corrosion-type classes, chart-calibrated pipelines transfer across devices with accuracy matching or beating unsupervised DA at a tiny fraction of complexity; for shape-defined control classes the calibration provides no benefit — cleanly diagnosing which classes are colorimetric and validating physical grounding as the method-selection criterion.
- **Why Important:** Reintroduces color science into a field that abandoned it for learned adaptation, with a class-property-based selection rule.
- **Why Possibly Novel:** Color constancy and DA literatures don't intersect on this comparison; the class-stratified head-to-head is new.
- **Minimal Experiment:** Capture corrosion samples with multiple cameras ± color charts; compare calibrated-transfer vs DA methods per class type.
- **Main Risk:** Requires a small controlled capture campaign; keep it to two devices and one afternoon of samples.
- **Research Cluster:** RSIND

### IDEA-C-0251 — Process ordering as a spatial prior: weld defects follow the torch path
- **One-sentence idea:** Test whether encoding manufacturing process order (the weld torch's temporal path over the spatial seam) as a positional prior improves weld-defect segmentation, exploiting that defect probability and type evolve along the process trajectory.
- **Problem:** Inspection models see static images of objects produced by temporal processes; the process coordinate (where in the manufacturing sequence each pixel was made) is discarded although defect physics is process-stationary, not space-stationary.
- **Core Hypothesis (falsifiable):** Reparameterizing weld images by seam arc-length (the process coordinate) reveals defect statistics that are stationary along the path but non-stationary in image space; models with process-coordinate conditioning outperform image-space models at matched capacity, with gains proportional to the measured non-stationarity — validating process-space learning.
- **Why Important:** Introduces manufacturing-process coordinates as a general conditioning principle for industrial ML (additive manufacturing layers, extrusion length, batch sequence).
- **Why Possibly Novel:** Process monitoring uses time series; fusing process coordinates into image segmentation as a spatial prior is new.
- **Minimal Experiment:** On weld datasets, extract seam paths; compare image-space vs arc-length-conditioned models; measure defect-statistic stationarity in each coordinate.
- **Main Risk:** Path extraction errors; use datasets with documented weld geometry.
- **Research Cluster:** RSIND

### IDEA-C-0252 — Socioeconomic confounders in rooftop-solar and infrastructure benchmarks
- **One-sentence idea:** Audit overhead infrastructure-detection benchmarks (solar panels, pools, roads) for socioeconomic-geographic confounding — targets co-varying with roof type, vegetation, and urban form — and measure how much reported accuracy depends on the confound rather than target appearance.
- **Problem:** Detection targets cluster by wealth and geography; models may detect neighborhoods, not panels, then fail (or discriminate) when deployed in underrepresented areas — a validity and fairness issue in one.
- **Core Hypothesis (falsifiable):** A target-blind model (trained on context with targets masked) predicts target presence well above chance on popular benchmarks; per-region performance of standard models tracks the context-predictability rather than target visibility, and context-decorrelated evaluation (matched-context positives/negatives) reveals substantially lower true detection capability with regional disparities.
- **Why Important:** These maps feed energy policy and taxation; context-inflated accuracy claims misallocate resources against exactly the underrepresented regions.
- **Why Possibly Novel:** Geographic bias is discussed in fairness literature; the context-blind-baseline audit methodology for overhead detection benchmarks is not standard.
- **Minimal Experiment:** Train context-only baselines on solar-panel datasets; build matched-context evaluation splits; re-report methods with disparity metrics.
- **Main Risk:** Context correlation is partly legitimate prior; report both raw and decorrelated numbers as complementary.
- **Research Cluster:** RSIND

### IDEA-C-0253 — Connectivity-calibrated training for linear infrastructure
- **One-sentence idea:** Test whether directly optimizing topological connectivity metrics (via differentiable connectivity surrogates) for road/pipeline extraction changes the accuracy-connectivity trade-off qualitatively, given that pixel metrics and network usability diverge severely for linear structures.
- **Problem:** Road extraction is scored by pixel overlap, but a one-pixel gap destroys routing utility while barely moving IoU; models tuned on pixel losses inherit the wrong priorities.
- **Core Hypothesis (falsifiable):** Models trained with connectivity-aware surrogates achieve dramatically better graph-level metrics (route completeness) at slight pixel-metric cost, and the trade-off frontier they trace is unreachable by post-processing pixel-trained models — proving the objective, not the decoding, is the binding constraint.
- **Why Important:** Establishes for a practically-huge task family that metric-aligned training beats post-hoc fixing — with the frontier-unreachability test as the rigorous version of that claim.
- **Why Possibly Novel:** Topology losses exist (clDice et al.); the frontier-unreachability comparison against exhaustive post-processing of pixel-trained models is the missing decisive experiment.
- **Minimal Experiment:** Train pixel vs connectivity-surrogate models on DeepGlobe roads; sweep post-processing exhaustively on the pixel models; compare achievable frontiers in (pixel, graph) metric space.
- **Main Risk:** Exhaustive post-processing is a strong claim; define a broad but explicit post-processing family.
- **Research Cluster:** RSIND

### IDEA-C-0254 — Context hallucination audit: models draw roads the terrain suggests
- **One-sentence idea:** Quantify how much overhead-imagery models hallucinate plausible-but-absent structures (roads through gaps, building corners) from context, using counterfactually-edited imagery where the structure is verifiably absent — measuring the prior-vs-evidence balance in dense prediction.
- **Problem:** Context priors help benchmarks but produce confident false mapping in atypical scenes (roads that don't exist get mapped, with real navigation consequences); no standard measurement separates evidence-driven from prior-driven predictions.
- **Core Hypothesis (falsifiable):** On counterfactual edits (inpainted structure removal with verified quality), models predict the removed structure at rates far above their calibrated confidence claims, with hallucination rate increasing with model scale on context-rich scenes (stronger priors) — an inverse-scaling result for evidential reliability.
- **Why Important:** Mapping pipelines feed navigation and disaster response; a standardized hallucination metric is due diligence, and the scale-dependence is scientifically loaded (echoes IDEA-C-0007).
- **Why Possibly Novel:** Hallucination is quantified in captioning/LLMs; a dense-prediction hallucination protocol with counterfactual edits and scaling analysis is new.
- **Minimal Experiment:** Build a counterfactual road/building removal set with quality verification; evaluate segmenters' hallucination rates vs confidence across model scales.
- **Main Risk:** Inpainting artifacts could cue models; verify edits fool patch-level detectors and humans.
- **Research Cluster:** RSIND

### IDEA-C-0255 — Ship wakes vs hulls: effect-detection as the general principle
- **One-sentence idea:** Quantify how maritime detection models split their evidence between ships (objects) and wakes (effects), unifying source-vs-effect confusion across domains (fire glow IDEA-C-0183, shadows IDEA-C-0186) into one measurable principle with a wake-only/hull-only decomposition.
- **Problem:** Effects (wakes) are often more visible than sources (hulls) — especially in SAR — and datasets label sources while models learn effects, breaking exactly when effects decouple (anchored ships, wake-free conditions).
- **Core Hypothesis (falsifiable):** Wake-masked evaluation shows a large fraction of detection performance attributable to wake evidence; models fail on wake-free ships at rates matching the measured wake reliance, and explicit two-channel training (detect source and effect as linked but separate outputs) improves both decoupled cases (anchored ships; empty wakes from departed vessels) — validating the source/effect decomposition as a design pattern.
- **Why Important:** Maritime monitoring has direct security/safety uses, and the source-effect design pattern generalizes to fire, shadow, contrail, and dust-plume detection.
- **Why Possibly Novel:** Wake detection exists as its own task; the reliance quantification via masking and the linked-decomposition training pattern are new.
- **Minimal Experiment:** On maritime SAR/optical datasets, run wake-masked and hull-masked ablations for public detectors; train the two-channel decomposition; evaluate on anchored-ship and wake-only subsets.
- **Main Risk:** Wake masking requires wake annotations; annotate a modest evaluation subset.
- **Research Cluster:** RSIND
## Cluster PROMPT — Prompting Science for SAM-Family and VLMs (IDEA-C-0256 … IDEA-C-0280)

### IDEA-C-0256 — The diminishing-bits law of interactive clicks
- **One-sentence idea:** Measure the information content (in bits of mask-posterior entropy reduction) of each successive click in interactive segmentation, testing whether it follows a universal diminishing curve predictable from object shape complexity.
- **Problem:** NoC metrics count clicks without weighting their informativeness; a bits-per-click law would ground interaction design and budget prediction in information theory.
- **Core Hypothesis (falsifiable):** Entropy reduction per click (estimated from mask-ensemble variance over plausible completions) decays with click index following a shape-complexity-parameterized law, consistent across datasets; total bits-to-convergence predicts NoC better than area/perimeter and connects to the compressibility account of IDEA-C-0154.
- **Why Important:** A quantitative theory of interaction value that unifies click budgeting, placement, and stopping criteria.
- **Why Possibly Novel:** Click studies are empirical; an information-accounting framework with measured per-click bits is new.
- **Minimal Experiment:** For 1k objects, estimate mask-posterior entropy per interaction step via SAM multi-mask sampling and perturbation ensembles; fit decay laws vs shape complexity; validate NoC prediction.
- **Main Risk:** Entropy estimation from limited mask samples is biased; use multiple estimators and synthetic validation.
- **Research Cluster:** PROMPT

### IDEA-C-0257 — Humans click centroids; models want maximum-uncertainty points
- **One-sentence idea:** Quantify the mismatch between where humans naturally click (object centroids, salient parts) and where models extract maximal information (posterior-uncertainty maxima), and measure the interaction cost of this misalignment plus the gain from model-guided click suggestions.
- **Problem:** Interactive models are trained/evaluated on simulator policies (see IDEA-C-0013); the complementary question — how much performance is lost to natural human policy, and whether guidance recovers it — is unmeasured.
- **Core Hypothesis (falsifiable):** Human click distributions concentrate far from model-uncertainty maxima; per-click IoU gain under human policy is a measurable fraction of optimal-policy gain, and lightweight guidance (highlighting suggested click regions) recovers most of the gap without harming user experience in a small study.
- **Why Important:** Converts interactive-segmentation research from simulator optimization to human-loop optimization, with a deployable guidance mechanism.
- **Why Possibly Novel:** Click simulators and user studies exist separately; the policy-gap quantification with a guidance intervention is new.
- **Minimal Experiment:** Collect natural click sequences (20 users × 50 images); compare against uncertainty-optimal policies on the same models; run a guided-clicking arm; measure NoC across arms.
- **Main Risk:** Guidance may bias users toward model errors; include error-case analysis.
- **Research Cluster:** PROMPT

### IDEA-C-0258 — Box prompts smuggle an aspect-ratio prior into mask completion
- **One-sentence idea:** Test whether SAM-family models use box-prompt aspect ratio as a shape prior for mask completion (beyond localization), systematically biasing masks toward box-conformal shapes when image evidence is weak.
- **Problem:** Boxes are treated as pure localization; if their geometry leaks into shape inference, auto-labeling pipelines using detector boxes inherit detector-box biases in mask shape.
- **Core Hypothesis (falsifiable):** For matched objects prompted with equivalent-coverage boxes of varying aspect ratio (padding manipulations), predicted masks shift measurably toward box-conformal shapes with the effect inversely proportional to local image contrast — and the bias transfers into training data generated by box-prompted auto-labeling, detectable in student models.
- **Why Important:** Box-prompted SAM labeling is the dominant auto-annotation pipeline; characterizing its systematic shape bias protects the datasets being built now.
- **Why Possibly Novel:** Prompt sensitivity is studied as robustness; the aspect-ratio-as-shape-prior mechanism and its dataset-contamination consequence are new.
- **Minimal Experiment:** Run padding-controlled box-prompt sweeps on 2k objects; measure mask-shape shift vs contrast; train a student on box-prompted pseudo-labels and test for inherited bias on neutral evaluation.
- **Main Risk:** Padding changes context visibility too; use context-matched controls.
- **Research Cluster:** PROMPT

### IDEA-C-0259 — Caption-template archaeology explains prompt-format sensitivity
- **One-sentence idea:** Test whether the sensitivity of open-vocab dense prediction to prompt templates ("a photo of X") is explained by the frequency of matching caption constructions in pretraining corpora — making prompt engineering an act of pretraining-distribution retrieval.
- **Problem:** Template effects are treated as mysterious folklore; if template utility is corpus-frequency in disguise, prompt engineering becomes predictable and corpus-auditable.
- **Core Hypothesis (falsifiable):** Across many templates, dense-task performance correlates strongly with the template's construction frequency in accessible caption corpora; novel templates' performance is predictable from corpus statistics before evaluation, and the correlation weakens for models trained on caption-diversified data — confirming the mechanism.
- **Why Important:** Replaces trial-and-error prompt search with corpus lookup and quantifies how superficial VLM language understanding is for dense grounding.
- **Why Possibly Novel:** Template ensembling is standard; the corpus-frequency predictive account tested on dense tasks is new.
- **Minimal Experiment:** Measure 50 templates' performance on open-vocab segmentation; count construction frequencies in LAION captions; fit and validate the predictor on held-out templates and a second model.
- **Main Risk:** Frequency and syntactic quality covary; include syntactic controls.
- **Research Cluster:** PROMPT

### IDEA-C-0260 — Is prompt space a logic? Testing embedding arithmetic for mask composition
- **One-sentence idea:** Test whether logical mask compositions (A∧B, A∨B, A∖B) are computable by arithmetic in prompt-embedding space (intersection of text/prompt embeddings), mapping which logical structure the prompt interface actually supports.
- **Problem:** Users need compositional queries ("wooden chairs", "cars except vans"); whether the learned prompt geometry supports composition operators — and which ones — is unknown.
- **Core Hypothesis (falsifiable):** Conjunctions of visually-independent attributes compose approximately by embedding operations (measurable IoU against ground-truth intersections), while negation and exclusive disjunction fail systematically regardless of operator choice — establishing an asymmetric logical profile consistent with the training objective's structure (co-occurrence can teach AND but not NOT, connecting to IDEA-C-0010).
- **Why Important:** Defines the compositional API of promptable segmentation — what can be queried directly vs what needs decomposition into multiple queries.
- **Why Possibly Novel:** Embedding arithmetic is studied for word analogies and generation; a systematic logical-operator census for dense prediction is new.
- **Minimal Experiment:** Build compositional ground truth from attribute-annotated datasets (chairs∧wooden); sweep embedding-composition operators; report the operator-by-logic performance matrix across 2 models.
- **Main Risk:** Failures may reflect operator choice, not geometry; include learned (fitted) composition operators as the strongest attempt.
- **Research Cluster:** PROMPT

### IDEA-C-0261 — Learned prompts are dataset fingerprints
- **One-sentence idea:** Test whether tuned prompt vectors (textual or visual prompt tokens) encode identifiable signatures of their tuning dataset — recoverable by a classifier — with implications for provenance auditing and unintended information leakage.
- **Problem:** Prompt tuning is marketed as a minimal, shareable adaptation artifact; if prompts fingerprint their training data (source, site, even demographic mix), sharing them leaks more than intended and enables provenance forensics.
- **Core Hypothesis (falsifiable):** Prompts tuned on different datasets (and different sites of the same task) are classifiable by source with high accuracy from the prompt vectors alone; some dataset properties (class balance, acquisition site) are decodable, and the leakage scales with prompt length — quantifying a privacy-utility trade-off unique to prompt sharing.
- **Why Important:** Prompt/adapter marketplaces are emerging; their information-leakage profile should be measured before sharing norms solidify — and provenance detection has positive auditing uses.
- **Why Possibly Novel:** Membership inference targets models; the artifact-level fingerprinting of prompts as shared objects is unstudied.
- **Minimal Experiment:** Tune prompts across 20 dataset/site configurations with multiple seeds; train source classifiers on prompt vectors; probe for property decoding; sweep prompt length.
- **Main Risk:** Seed variance may swamp signals at short prompts — itself an informative negative result for the leakage question.
- **Research Cluster:** PROMPT

### IDEA-C-0262 — Interaction hysteresis: click order changes the final mask
- **One-sentence idea:** Quantify path dependence in iterative interactive segmentation — identical final click sets producing different masks depending on order — and determine whether hysteresis is a decoder-state artifact or an ambiguity-resolution feature.
- **Problem:** Interactive protocols assume the final annotation state determines the mask; if order matters, reproducibility of interactive labeling is compromised and evaluation is ill-defined.
- **Core Hypothesis (falsifiable):** Order-permuted replays of identical click sets yield mask variance far above model stochasticity baselines, concentrated on ambiguous objects; the variance is eliminated by stateless re-decoding (feeding all clicks at once), localizing hysteresis in the iterative previous-mask conditioning — and revealing whether iterative conditioning helps or just adds noise.
- **Why Important:** Interactive labeling is producing the field's next datasets; order-dependent ground truth is a reproducibility hazard nobody documents.
- **Why Possibly Novel:** Robustness to click position is studied; order-permutation hysteresis with mechanism localization is not.
- **Minimal Experiment:** Replay permuted click sequences through SAM-style models with and without previous-mask conditioning; decompose variance; correlate with object ambiguity scores.
- **Main Risk:** Some order dependence is arguably desirable UX; separate the reproducibility question from the UX question explicitly.
- **Research Cluster:** PROMPT

### IDEA-C-0263 — Decodable rules of part-whole ambiguity resolution
- **One-sentence idea:** Reverse-engineer the implicit rules by which SAM-family models resolve part-vs-whole ambiguity from click position (interior vs near-part-boundary clicks), testing whether resolution follows decodable geometric rules users could learn and exploit.
- **Problem:** Users experience part-whole selection as unpredictable; if systematic rules exist, they can be documented (better UX), exploited (deliberate granularity control), or retrained (better defaults).
- **Core Hypothesis (falsifiable):** The granularity of the returned mask is predictable (high accuracy) from a small set of click-geometry features (distance to part boundaries, relative position within part hierarchies) — constituting an implicit grammar; communicating the grammar to users measurably reduces their clicks-to-target-granularity in a study.
- **Why Important:** Converts a UX pain point into a documented interface contract and reveals what hierarchy representation the model learned without hierarchical supervision.
- **Why Possibly Novel:** Multi-mask outputs acknowledge ambiguity; decoding the deterministic resolution rules and closing the loop with user training is new.
- **Minimal Experiment:** On part-annotated datasets (PACO), sweep click positions systematically; fit granularity predictors from click geometry; run a small user study with and without rule instruction.
- **Main Risk:** Rules may be model-version-specific; test two SAM variants for rule stability.
- **Research Cluster:** PROMPT

### IDEA-C-0264 — Visual exemplar prompts and text prompts encode complementary invariances
- **One-sentence idea:** Test whether visual-exemplar prompting (reference patch) and text prompting select systematically different invariance classes — text generalizing over appearance within a concept, exemplars generalizing over context for an appearance — such that their union covers failure modes neither covers alone.
- **Problem:** Prompt modalities are compared on average accuracy; if they carry structurally different generalization, the choice should be case-driven and their combination principled rather than heuristic.
- **Core Hypothesis (falsifiable):** Error-set analysis shows text prompts failing on atypical appearances of the concept while exemplar prompts fail on typical appearances in atypical contexts (double dissociation); the error overlap is far below independence expectations, and a confidence-based router between modalities beats both and their naive score fusion.
- **Why Important:** Establishes the first structural account of prompt-modality complementarity, directly improving open-vocabulary systems with a simple router.
- **Why Possibly Novel:** Multi-modal prompting exists in specific systems; the invariance-class dissociation analysis is new.
- **Minimal Experiment:** Evaluate matched text vs exemplar prompting on datasets with typicality annotations (or typicality scores from retrieval density); analyze error structure; build and test the router.
- **Main Risk:** Available models implement modalities with different quality; use a model supporting both natively (SEEM-style) plus cross-checks.
- **Research Cluster:** PROMPT

### IDEA-C-0265 — Spatial-shift vs semantic-shift dissociation between prompt tuning and adapters
- **One-sentence idea:** Test whether prompt tuning preferentially fixes semantic errors (what things are) while adapter tuning preferentially fixes spatial errors (where boundaries lie), reflecting their architectural loci — a dissociation that would give the first principled method-selection rule for dense PEFT.
- **Problem:** Prompt tuning vs adapters is decided by habit or single-metric comparisons that hide error-type structure.
- **Core Hypothesis (falsifiable):** At matched parameter budgets across tasks engineered to require mostly-semantic vs mostly-spatial correction (label remapping vs boundary-convention shifts), prompt tuning wins the semantic tasks and adapters win the spatial ones, with mixed tasks showing additive combination — the double dissociation confirming distinct functional channels.
- **Why Important:** Converts PEFT-method choice from benchmarking lottery to error-type diagnosis, and maps where in the architecture "what" and "where" corrections live.
- **Why Possibly Novel:** PEFT comparisons abound; the engineered-shift dissociation design isolating error types is new.
- **Minimal Experiment:** Construct semantic-shift (synonym class remaps) and spatial-shift (systematic boundary offset conventions) variants of standard datasets; run both methods at matched budgets; report the interaction effect.
- **Main Risk:** Pure shift construction is artificial; validate conclusions on natural tasks with measured shift composition.
- **Research Cluster:** PROMPT

### IDEA-C-0266 — Dense prompt maps collapse to low rank
- **One-sentence idea:** Measure the effective rank of learned dense (per-location) prompt maps for dense-prediction tasks, testing whether spatial prompting collapses to a low-dimensional structure that a compressed parameterization can match at a fraction of parameters.
- **Problem:** Visual prompt tuning for dense tasks allocates per-position parameters without knowing whether the learned solution actually uses spatial diversity.
- **Core Hypothesis (falsifiable):** Trained dense prompts have effective rank far below their nominal dimensionality (dominated by a few spatial modes resembling positional/border corrections); rank-constrained prompt parameterizations chosen at the measured rank match full dense prompting across tasks — turning prompt-capacity selection into spectrum measurement.
- **Why Important:** Shrinks visual-prompt storage/compute and reveals what spatial prompting actually does (global geometry correction, not local content adaptation).
- **Why Possibly Novel:** Prompt compression exists in NLP; the spatial-spectrum analysis of dense visual prompts with matched-rank validation is new.
- **Minimal Experiment:** Train dense prompts on 5 dense tasks; compute SVD spectra of prompt maps; retrain rank-constrained variants at measured ranks; compare.
- **Main Risk:** Rank may vary widely across task types — which is itself the useful map.
- **Research Cluster:** PROMPT

### IDEA-C-0267 — CKA predicts cross-model prompt transferability
- **One-sentence idea:** Test whether prompts tuned on one VFM transfer to another with effectiveness predicted by feature-space similarity (CKA) between the models at the prompt-injection layers — establishing a transferability law for the growing prompt-artifact ecosystem.
- **Problem:** Prompts are shared as artifacts, but nobody can predict whether a prompt tuned on model A helps model B without full re-evaluation.
- **Core Hypothesis (falsifiable):** Across a model-pair grid, transferred-prompt performance retention correlates strongly with injection-layer CKA (and poorly with architecture-family labels or parameter counts); the fitted law predicts held-out pair transfer within useful error — making compatibility computable from cheap unlabeled forward passes.
- **Why Important:** Enables a functioning prompt-reuse ecosystem (compatibility scores instead of trial-and-error) and adds evidence on what representational similarity metrics actually predict.
- **Why Possibly Novel:** CKA predicts probing/transfer in analysis papers; its use as a prompt-artifact compatibility law is untested.
- **Minimal Experiment:** Tune prompts on 6 backbones × 4 dense tasks; evaluate all cross-transfers; regress retention on CKA and baselines; validate on 2 held-out backbones.
- **Main Risk:** Prompt-injection interfaces differ across models; standardize via a common wrapper.
- **Research Cluster:** PROMPT

### IDEA-C-0268 — Prompt-length saturation is set by task class-structure, not model size
- **One-sentence idea:** Test whether the prompt-length at which dense-task prompt tuning saturates is determined by the task's class/structure count (information to be specified) rather than by model capacity — an information-capacity matching law for prompt budgeting.
- **Problem:** Prompt length is grid-searched per task; a task-property law would eliminate the search and explain what prompt tokens carry.
- **Core Hypothesis (falsifiable):** Saturation length scales with task class count and boundary-convention complexity across tasks (holding the model fixed) and is nearly invariant to model scale (holding the task fixed) — supporting prompts-as-task-specification over prompts-as-capacity; measured per-token information estimates match the task's specification complexity.
- **Why Important:** Grounds prompt budgeting in task information content and clarifies the semantics of prompt tokens for dense prediction.
- **Why Possibly Novel:** Prompt-length ablations are routine; the cross-factor design (task complexity × model scale) testing the invariance claim is new.
- **Minimal Experiment:** Sweep prompt lengths across (6 tasks of varying class count) × (3 model scales); locate saturation points; test the two invariance predictions.
- **Main Risk:** Saturation detection is noisy; define it via fitted curves with confidence intervals.
- **Research Cluster:** PROMPT

### IDEA-C-0269 — Typographic attacks transfer to dense prediction: scene text hijacks segmentation
- **One-sentence idea:** Test whether text written in scenes hijacks text-prompted segmentation (the dense analog of CLIP's typographic attacks), measuring whether written class names attract masks and whether the vulnerability survives into distilled/derived dense models.
- **Problem:** Text-prompted segmenters inherit CLIP-family lineage; their typographic vulnerability profile in the dense regime (where masks localize the hijack) is uncharacterized despite auto-labeling deployment.
- **Core Hypothesis (falsifiable):** Class names physically present in scenes (signs, labels, graffiti — natural or composited) attract segmentation masks toward text regions at rates far above visual-similarity controls; the effect strength tracks the model's text-recognition capability, and defensive prompting or text-region masking reduces it — quantifying an exploitable auto-labeling contamination channel.
- **Why Important:** Auto-labeling pipelines processing web/street imagery will ingest typographic contamination into datasets; measuring the channel now is cheap insurance.
- **Why Possibly Novel:** Typographic attacks are classification-era results; the dense localization version with pipeline-contamination framing is new.
- **Minimal Experiment:** Composite class-name text into scenes at controlled saliences; measure mask attraction for 4 open-vocab segmenters; test natural scene-text cases; evaluate mitigations.
- **Main Risk:** Compositing artifacts; include natural-text-only validation subsets.
- **Research Cluster:** PROMPT

### IDEA-C-0270 — Prompt dropout at training buys calibrated sparse-prompt behavior
- **One-sentence idea:** Test whether randomly dropping prompts during SAM-style training (forcing the model to sometimes predict from partial or no prompts) produces calibrated uncertainty under prompt sparsity at deployment — a one-line fix for overconfident single-click masks.
- **Problem:** Promptable models trained with full prompt supervision are overconfident when users provide minimal prompts, silently committing to one interpretation.
- **Core Hypothesis (falsifiable):** Prompt-dropout-trained decoders produce confidence (and multi-mask spread) that tracks actual ambiguity under sparse prompting significantly better than standard training (measured against multi-annotator ambiguity ground truth), at negligible cost to dense-prompt accuracy — establishing dropout rate as a calibration dial.
- **Why Important:** Sparse prompting is the common real-world case; calibrated behavior there determines whether interactive tools can be trusted for triage.
- **Why Possibly Novel:** Dropout for robustness is generic; targeting the prompt channel specifically for ambiguity calibration in promptable segmentation is untested.
- **Minimal Experiment:** Fine-tune SAM decoders with prompt-dropout schedules; evaluate confidence calibration against multi-rater mask distributions at prompt budgets {1,3,dense}; sweep dropout rates.
- **Main Risk:** Excessive dropout may induce prompt-ignoring (see IDEA-C-0276); monitor prompt-influence metrics jointly.
- **Research Cluster:** PROMPT

### IDEA-C-0271 — Coarse-mask self-prompting: chain-of-thought for segmentation
- **One-sentence idea:** Test whether feeding a model's own coarse mask back as a prompt for refined prediction (iterated self-conditioning) improves fine mask quality — a minimal dense analog of chain-of-thought that trades inference passes for accuracy without any retraining.
- **Problem:** Single-pass dense prediction commits to boundary detail and global structure simultaneously; staged self-conditioning may decouple these, but the field lacks a clean test of whether iteration helps frozen promptable models.
- **Core Hypothesis (falsifiable):** Iterated self-prompting of frozen SAM-family models improves boundary metrics monotonically for the first few iterations on complex objects (with predictable saturation), outperforming equal-compute ensembling, and the gains concentrate on objects where first-pass global structure was correct but detail was poor — confirming the decoupling mechanism.
- **Why Important:** A free (training-less) quality dial with a mechanistic account, informing whether iterative decoding deserves architectural investment.
- **Why Possibly Novel:** Iterative refinement exists as trained architecture; the zero-training self-prompting protocol on frozen promptable models with mechanism analysis is new.
- **Minimal Experiment:** Implement mask→prompt feedback loops on SAM variants; sweep iterations across object complexity strata; compare against compute-matched ensembles.
- **Main Risk:** Feedback may amplify initial errors on some objects; characterize the divergence set.
- **Research Cluster:** PROMPT

### IDEA-C-0272 — Patch-grid quantization of click coordinates causes boundary snap artifacts
- **One-sentence idea:** Test whether the quantization of prompt coordinates to the patch grid in ViT-based promptable models causes systematic mask-boundary snapping (outputs preferring patch-aligned boundaries near clicks), and whether subpixel prompt encoding removes it.
- **Problem:** Click positions are continuous but positional encodings live on the token grid; any induced spatial aliasing in outputs corrupts precision applications (measurement, medical margins) invisibly.
- **Core Hypothesis (falsifiable):** Sweeping click positions continuously across patch boundaries produces discontinuous mask-boundary responses (snap events at patch edges) with amplitude predictable from positional-encoding interpolation; continuous (Fourier/subpixel) prompt-coordinate encoding retrofitted with brief fine-tuning eliminates the discontinuities and improves boundary accuracy near prompts.
- **Why Important:** A precision defect in the dominant interactive architecture, with a cheap targeted fix — and another instance of discrete-grid artifacts (complementing IDEA-C-0084).
- **Why Possibly Novel:** Prompt-encoding design is treated as settled; the continuous-sweep artifact measurement appears undone.
- **Minimal Experiment:** Measure mask response to sub-patch click sweeps on SAM; quantify snap amplitude; retrofit subpixel encoding and re-measure.
- **Main Risk:** Effects may be small relative to decoder upsampling artifacts; instrument both sources separately.
- **Research Cluster:** PROMPT

### IDEA-C-0273 — SAM's three masks undercover human ambiguity mode counts
- **One-sentence idea:** Compare the number and structure of segmentation modes humans produce for ambiguous prompts against SAM's fixed three-mask output, testing whether the architecture's mode budget systematically undercovers real ambiguity distributions.
- **Problem:** The three-mask design was a pragmatic choice; whether it matches the true modality of human segmentation ambiguity — and what coverage is lost — has not been measured.
- **Core Hypothesis (falsifiable):** Human mask distributions for ambiguous prompts (collected at scale) exhibit more than three well-separated modes for a substantial fraction of cases (nested part hierarchies × delineation conventions), with SAM's outputs covering the top modes but missing systematic others (measured by distribution coverage metrics); a variable-mode decoder head trained on the same backbone closes most of the coverage gap.
- **Why Important:** Sets the empirical requirements for ambiguity-aware interfaces and datasets before the three-mask convention hardens into infrastructure.
- **Why Possibly Novel:** Multi-mask outputs exist; the human mode-census benchmarking of their sufficiency is new.
- **Minimal Experiment:** Collect ~10 human masks per prompt on 300 ambiguous cases; cluster into modes; measure SAM coverage; train a variable-mode head for comparison.
- **Main Risk:** Mode definition depends on clustering choices; use multiple granularities.
- **Research Cluster:** PROMPT

### IDEA-C-0274 — Negation prompts are handled by suppression, not by concept
- **One-sentence idea:** Probe how text-promptable segmenters process negated queries ("the region without wires"), testing whether they implement negation as post-hoc score suppression of the negated concept rather than composing a genuine complement concept — predicting characteristic failure geometry.
- **Problem:** Negation is linguistically routine and practically needed (exclusion zones, contraindicated regions); the mechanism models actually use determines when negation can be trusted.
- **Core Hypothesis (falsifiable):** Negated-query outputs equal (up to calibration) the complement of the positive query's thresholded mask in most cases (suppression signature), failing exactly where the positive concept is undetected but present — while a true complement concept would fail differently; the signature holds across models and phrasings, confirming a mechanism-level account (extending IDEA-C-0010 from expressivity to mechanism).
- **Why Important:** Tells practitioners negated queries inherit all false negatives of positive queries — a specific, checkable trust boundary.
- **Why Possibly Novel:** Negation failure is documented in VLMs behaviorally; the mechanism-signature analysis for dense outputs is new.
- **Minimal Experiment:** Build positive/negative query pairs; test the complement-equality signature across models and paraphrases; analyze failure geometry on planted undetected-instance cases.
- **Main Risk:** Instruction-tuned models may vary; report per-model signatures.
- **Research Cluster:** PROMPT

### IDEA-C-0275 — Metadata prompts: injecting physical scale fixes scale-ambiguous classes
- **One-sentence idea:** Test whether providing physical scale as a prompt (mm-per-pixel from capture metadata) resolves the class confusions that are provably scale-ambiguous from appearance alone (moss vs forest canopy, crack vs canyon), establishing metadata prompting as a channel for non-visual context.
- **Problem:** Many confusion pairs are visual metamers differing only in physical scale; models guess from context while the disambiguating variable sits unused in capture metadata.
- **Core Hypothesis (falsifiable):** A scale-conditioned model (metadata embedding added to prompts) eliminates the identified metamer confusions almost entirely while leaving other errors unchanged (specificity), and degrades gracefully with metadata noise — validating a general capture-parameter prompting interface whose value is predictable from a task's metamer census.
- **Why Important:** Opens a systematically-unused information channel with clean falsifiable structure, relevant across microscopy, aerial, and macro photography.
- **Why Possibly Novel:** Camera-parameter conditioning exists in 3D tasks; metamer-targeted scale prompting for semantic segmentation with specificity analysis is new.
- **Minimal Experiment:** Assemble scale-metamer class pairs across magnification datasets; train scale-conditioned vs blind models; measure targeted confusion reduction and specificity.
- **Main Risk:** Metamer pairs partially resolvable by subtle texture cues; quantify the residual visual signal in blind-model performance.
- **Research Cluster:** PROMPT

### IDEA-C-0276 — Prompt-influence decay: fine-tuned SAMs learn to ignore their prompts
- **One-sentence idea:** Track the causal influence of prompts on outputs during task-specific SAM fine-tuning, testing whether models progressively ignore prompts (converging to unconditional task-specific segmenters) — silently destroying the interactive contract while metrics improve.
- **Problem:** Teams fine-tune SAM on single-task data and assume prompt control is retained; if prompt influence decays, the deployed tool no longer responds to corrections — a failure invisible to accuracy metrics.
- **Core Hypothesis (falsifiable):** Prompt-influence metrics (output sensitivity to prompt perturbation; mutual information between prompt and mask given the image) decay monotonically during narrow-task fine-tuning at rates increasing with dataset homogeneity; a prompt-diversity regularizer (training with contradictory prompt-target pairs) preserves influence at minor accuracy cost — defining the retention recipe.
- **Why Important:** Protects the core interactive capability during the most common adaptation workflow, with a monitoring metric and a fix.
- **Why Possibly Novel:** Catastrophic forgetting concerns class knowledge; forgetting of interface responsiveness is an unmeasured axis (complementing IDEA-C-0030's semantic drift).
- **Minimal Experiment:** Fine-tune SAM on homogeneous vs diverse task data; log prompt-influence trajectories; verify with correction-response tests; evaluate the regularizer.
- **Main Risk:** Influence metrics must separate prompt-ignoring from correct prompt-independence (unambiguous cases); condition analysis on ambiguity.
- **Research Cluster:** PROMPT

### IDEA-C-0277 — In-context segmentation retrieves pretraining modes rather than inducing rules
- **One-sentence idea:** Test whether visual in-context segmentation (one exemplar pair defines the task) performs task induction or merely retrieves the nearest pretraining task mode, using synthetic tasks that cannot exist in pretraining as the discriminating probe.
- **Problem:** In-context abilities of vision models are marketed as few-shot task learning; the retrieval-vs-induction distinction determines whether novel tasks (custom industrial conventions) can ever work.
- **Core Hypothesis (falsifiable):** On natural task variants, in-context performance is high and insensitive to exemplar informativeness (retrieval signature: the exemplar just selects a known mode); on synthetic rule-based tasks impossible in pretraining (segment-every-second-stripe conventions), performance collapses to near-chance regardless of exemplar count — while genuine induction would scale with exemplars; the dissociation quantifies the retrieval fraction.
- **Why Important:** Sets honest expectations for in-context dense prediction and defines what pretraining changes would be needed for true induction.
- **Why Possibly Novel:** The retrieval-vs-induction debate is active in LLMs; the controlled synthetic-task discriminator for dense visual in-context learning is new.
- **Minimal Experiment:** Evaluate visual in-context models (Painter/SegGPT-style) on natural vs impossible-in-pretraining synthetic tasks with exemplar-count sweeps; report the dissociation.
- **Main Risk:** "Impossible in pretraining" needs care; verify synthetic conventions are absent via retrieval audits.
- **Research Cluster:** PROMPT

### IDEA-C-0278 — Models should ask for the next click: learned query-by-uncertainty
- **One-sentence idea:** Invert the interactive protocol: train the model to output where it wants the next user click (its maximum-value query), testing whether model-directed interaction reduces clicks-to-target beyond user-directed and simulator-directed baselines.
- **Problem:** All interaction burden of deciding where to click sits with users, who lack access to the model's uncertainty structure (IDEA-C-0257 measures the resulting gap; this idea closes it architecturally).
- **Core Hypothesis (falsifiable):** A query head trained to maximize expected IoU gain per requested click achieves target quality with measurably fewer interactions than uncertainty-heuristic and human-choice baselines in simulator and small human studies, with the advantage largest on multi-part and low-contrast objects where user intuition misallocates clicks.
- **Why Important:** Reframes interactive segmentation as active learning at inference, with direct annotation-cost consequences and a general pattern (model-directed human input) for other interactive systems.
- **Why Possibly Novel:** Active learning selects images; per-interaction query generation inside a promptable decoder with human-loop validation is largely unexplored.
- **Minimal Experiment:** Train a light query head on SAM features via simulated rollouts; compare NoC against baselines; run a 15-user confirmation study.
- **Main Risk:** Users may distrust or misinterpret query suggestions; measure compliance and its effect separately.
- **Research Cluster:** PROMPT

### IDEA-C-0279 — Resolution changes the meaning of a click
- **One-sentence idea:** Test whether the effective semantics of a point prompt (how much area/granularity it selects) drifts with input resolution in SAM-family models, making interactive behavior resolution-dependent in ways users and pipelines don't account for.
- **Problem:** The same physical click on the same scene at different processing resolutions may select different granularities (patch-relative receptive fields change), corrupting cross-resolution reproducibility of interactive labeling.
- **Core Hypothesis (falsifiable):** Holding the scene and click fixed while sweeping input resolution shifts the returned mask's granularity distribution systematically (finer selections at higher resolution) beyond boundary-precision effects; the drift is predictable from token-grid geometry and correctable by resolution-aware prompt encoding — restoring a resolution-invariant interaction contract.
- **Why Important:** Auto-labeling pipelines mix resolutions freely; an undocumented granularity drift contaminates datasets built with resolution-heterogeneous SAM labeling.
- **Why Possibly Novel:** Resolution robustness is studied for accuracy; the prompt-semantics drift question is different and unexamined.
- **Minimal Experiment:** Sweep processing resolution on fixed scenes/clicks; measure granularity metrics (relative area, hierarchy level) of outputs; fit drift against token-grid predictions; test the encoding correction.
- **Main Risk:** Granularity metrics need part-hierarchy ground truth; reuse PACO-style annotations.
- **Research Cluster:** PROMPT

### IDEA-C-0280 — The prompt-format census: what fraction of "prompting" gains is interface bureaucracy
- **One-sentence idea:** Systematically decompose reported prompting-method improvements in dense prediction into (a) genuine information added by the prompt content and (b) interface effects (format, position encoding, normalization changes), testing how much of the prompting literature's gains survive interface-matched controls.
- **Problem:** Prompting papers vary content and interface simultaneously; if a substantial share of gains comes from interface side effects (extra parameters, changed normalization statistics, longer effective context), the literature's causal claims are misattributed.
- **Core Hypothesis (falsifiable):** Re-running representative prompting methods with content-randomized controls (same interface, shuffled/meaningless prompt content) recovers a measurable fraction of their reported gains on dense benchmarks; the residual (content-specific) gain correlates with task ambiguity — separating prompting-as-information from prompting-as-architecture.
- **Why Important:** A field-hygiene result establishing the control experiment every prompting paper should include, with a reusable decomposition protocol.
- **Why Possibly Novel:** Random-prompt controls appear sporadically in NLP; a systematic decomposition audit for dense-prediction prompting is missing.
- **Minimal Experiment:** Reproduce 5 published dense-prompting methods; add content-randomized and interface-matched arms; report gain decompositions with confidence intervals.
- **Main Risk:** Reproduction fidelity; use released code and confirm baseline numbers before decomposing.
- **Research Cluster:** PROMPT
## Cluster PEFT — PEFT Science: LoRA/Adapter/Prompt-Tuning Mechanics (IDEA-C-0281 … IDEA-C-0305)

### IDEA-C-0281 — Value/output projections carry dense-task LoRA; query/key are semantic-only
- **One-sentence idea:** Test whether LoRA placed on attention value/output projections dominates query/key placement for dense prediction (spatial routing vs similarity re-weighting), reversing or refining placement heuristics inherited from NLP.
- **Problem:** LoRA placement conventions were tuned on language tasks; dense tasks need spatial-information routing whose architectural locus may differ.
- **Core Hypothesis (falsifiable):** At matched parameter budgets across segmentation tasks, V/O-only LoRA outperforms Q/K-only LoRA on boundary and localization metrics while Q/K-only suffices for class-remapping tasks — a dissociation reflecting that Q/K changes where attention looks (semantic matching) while V/O changes what is transported (spatial content).
- **Why Important:** Placement is the cheapest PEFT decision; a task-type-resolved rule with a mechanism beats blanket defaults.
- **Why Possibly Novel:** Placement ablations exist mostly for language/classification; the dense-task metric-decomposed dissociation is untested.
- **Minimal Experiment:** Run {Q/K, V/O, MLP, all} LoRA placements at matched budgets on 4 dense tasks including one pure class-remap; report metric-decomposed results.
- **Main Risk:** Findings may vary across backbone families; test ViT and hybrid architectures.
- **Research Cluster:** PEFT

### IDEA-C-0282 — Mask fractal dimension predicts required LoRA rank
- **One-sentence idea:** Test whether the LoRA rank a dense task needs is predictable from the geometric complexity of its target masks (fractal dimension/curvature entropy), linking adaptation capacity to output-geometry information content.
- **Problem:** Rank selection (beyond dataset-size effects, IDEA-C-0131) lacks task-content predictors; boundary-complex tasks plausibly need more expressive updates.
- **Core Hypothesis (falsifiable):** Across tasks matched on dataset size but differing in measured mask complexity, the accuracy-saturating rank correlates strongly with complexity metrics; complexity-based rank prediction transfers to held-out tasks within a factor of 2 — establishing geometry as a second axis of the rank law.
- **Why Important:** Completes a practical rank-selection formula (size × geometry) and reveals what LoRA capacity is spent on.
- **Why Possibly Novel:** Rank studies ignore output geometry entirely; the complexity-capacity link is unexplored.
- **Minimal Experiment:** Assemble size-matched task pairs with contrasting mask complexity (organs vs vessels; buildings vs vegetation); sweep ranks; regress saturating rank on complexity.
- **Main Risk:** Complexity and semantic difficulty covary; include semantic-difficulty covariates.
- **Research Cluster:** PEFT

### IDEA-C-0283 — Adapters spontaneously become input-conditional gates
- **One-sentence idea:** Test whether trained adapters develop emergent input-dependent gating (near-zero output for some inputs, large for others) without any gating architecture — implying adapters learn when to intervene, not just how.
- **Problem:** Adapters are modeled as static feature transforms; if they self-organize into conditional interventions, capacity accounting and interpretability change.
- **Core Hypothesis (falsifiable):** Adapter output norms across inputs are strongly bimodal/heavy-tailed (vs unimodal for random projections of the same features), with the low-intervention inputs being those the frozen backbone already handles (verified by frozen-model accuracy on the partition) — demonstrating emergent conditionality; explicitly gated adapters then add nothing, confirming the implicit mechanism saturates the benefit.
- **Why Important:** Explains PEFT's efficiency (intervention only where needed) and provides a free difficulty estimator (adapter norm as sample hardness signal).
- **Why Possibly Novel:** Conditional adapters are designed intentionally; discovering emergent conditionality in plain adapters is a new observation.
- **Minimal Experiment:** Analyze adapter output-norm distributions across inputs on 4 tasks; correlate with frozen-model per-sample accuracy; compare against explicitly-gated variants.
- **Main Risk:** Norm bimodality thresholds are arbitrary; use distributional tests, not cutoffs.
- **Research Cluster:** PEFT

### IDEA-C-0284 — Why PEFT preserves calibration: frozen logit geometry
- **One-sentence idea:** Test the mechanism behind PEFT's better calibration retention vs full fine-tuning: frozen features constrain logit geometry (norm growth and margin inflation are bounded), preventing the overconfidence drift full FT exhibits.
- **Problem:** PEFT's calibration advantage is reported anecdotally without a mechanism, so nobody knows when it holds or fails.
- **Core Hypothesis (falsifiable):** During full FT, logit norms and confidence margins grow continuously (classic overconfidence dynamics), while PEFT's are bounded by the frozen feature norms; the calibration gap between methods is quantitatively predicted by the measured logit-norm growth difference, and artificially constraining full-FT logit norms recovers PEFT-level calibration — confirming the geometric mechanism.
- **Why Important:** Calibration governs deployment trust; a mechanistic account tells practitioners when PEFT's advantage applies and how to import it into full FT.
- **Why Possibly Novel:** Overconfidence dynamics are studied for training from scratch; the PEFT-vs-FT calibration mechanism comparison is new.
- **Minimal Experiment:** Track logit-geometry statistics during PEFT vs full FT on 4 dense tasks; correlate with calibration trajectories; run the norm-constrained full-FT intervention.
- **Main Risk:** Dense-prediction calibration is spatially heterogeneous; analyze boundary and interior separately.
- **Research Cluster:** PEFT

### IDEA-C-0285 — Serial vs parallel adapters differ in accessible frequency bands
- **One-sentence idea:** Characterize serial (inserted in-path) vs parallel (residual side-path) adapters as filters, testing whether they can modify systematically different spatial-frequency content of feature maps — explaining task-dependent wins of each topology.
- **Problem:** Serial-vs-parallel choices are empirical coin flips; a transfer-function account would predict the winner from task frequency demands.
- **Core Hypothesis (falsifiable):** Measured input-output transfer functions show parallel adapters limited to additive corrections (preserving backbone passbands) while serial adapters can attenuate/reshape existing bands; consequently serial wins on tasks requiring suppression of pretrained responses (de-texturing, artifact removal) and parallel wins on augmentation tasks (new detail) — validated by the task-type × topology interaction.
- **Why Important:** Converts a topology choice into a task-diagnostic rule with a signal-processing rationale.
- **Why Possibly Novel:** Adapter topologies are compared by accuracy; the filter-analysis framing with interaction predictions is new.
- **Minimal Experiment:** Measure adapter transfer functions on probe stimuli; run topology × task-type (suppression vs augmentation, synthetically constructed) factorial; test the predicted interaction.
- **Main Risk:** Nonlinearities complicate transfer-function measurement; use local linearization at multiple operating points.
- **Research Cluster:** PEFT

### IDEA-C-0286 — Shift-type taxonomy predicts when bias-only tuning suffices
- **One-sentence idea:** Test whether BitFit-style bias-only tuning works on dense tasks precisely when the domain shift is additive in feature space (verifiable by a cheap shift decomposition), failing for multiplicative/rotational shifts — a pre-adaptation diagnostic choosing the cheapest sufficient method.
- **Problem:** Bias-only tuning is astonishingly effective sometimes and useless elsewhere, with no predictive rule.
- **Core Hypothesis (falsifiable):** Decomposing measured feature-distribution shifts into additive/scaling/rotational components, bias-tuning recovery of full-FT gains correlates strongly with the additive fraction across many shift scenarios; the decomposition (computable from unlabeled target data) predicts method sufficiency in advance with high decision accuracy.
- **Why Important:** A one-forward-pass diagnostic that routes each deployment to the cheapest adequate adaptation — economics from measurement (complements IDEA-C-0149).
- **Why Possibly Novel:** BitFit results are catalogued; the shift-decomposition predictive framework is untested.
- **Minimal Experiment:** For 15 shift scenarios, compute feature-shift decompositions; run bias-only vs LoRA vs full FT; fit and validate the sufficiency predictor.
- **Main Risk:** Layer-wise shift heterogeneity; compute decompositions per layer and aggregate carefully.
- **Research Cluster:** PEFT

### IDEA-C-0287 — Attention-LoRA fixes "what", MLP-LoRA fixes "where" errors
- **One-sentence idea:** Test the dissociation that LoRA on attention blocks preferentially reduces semantic (class-confusion) errors while LoRA on MLP blocks preferentially reduces spatial (boundary/localization) errors in dense prediction.
- **Problem:** Attention-vs-MLP placement is decided by budget heuristics; error-type-resolved effects would enable targeted repair of diagnosed model weaknesses.
- **Core Hypothesis (falsifiable):** At matched budgets, error-decomposed evaluation (confusion vs boundary displacement) shows a double dissociation between placement and error type across tasks; moreover, the mix of a given task's error types predicts its optimal placement mix — validated prospectively (complementing IDEA-C-0265's prompt-vs-adapter axis and IDEA-C-0281's within-attention axis).
- **Why Important:** Builds a placement-by-diagnosis workflow: measure your error profile, choose your PEFT surgery.
- **Why Possibly Novel:** Component roles (attention=mixing, MLP=memory) are studied in LLM interpretability; the dense-error-type mapping is new.
- **Minimal Experiment:** Attention-only vs MLP-only LoRA on tasks with contrasting error profiles; decomposed metrics; prospective placement-mix prediction on 2 held-out tasks.
- **Main Risk:** Error types interact (bad semantics ruins boundaries); use conditional error metrics.
- **Research Cluster:** PEFT

### IDEA-C-0288 — Forgetting fingerprints: each PEFT method forgets differently, not less
- **One-sentence idea:** Test whether PEFT methods differ mainly in the structure of what they forget (LoRA: class knowledge; prompts: resolution/format robustness; norm-tuning: calibration) rather than the amount — establishing method-specific forgetting fingerprints for retention-critical deployments.
- **Problem:** "PEFT forgets less" is the standard claim, measured on scalar retention; if forgetting is method-structured, the right question is what each method sacrifices.
- **Core Hypothesis (falsifiable):** Across matched-budget adaptations, a broad retention battery (zero-shot classes, resolutions, corruptions, calibration, prompt-following) shows method × capability interactions far exceeding method main effects — stable fingerprints reproducible across tasks and backbones, enabling retention-requirement-driven method choice.
- **Why Important:** Replaces a one-dimensional retention narrative with an actionable capability-preservation map.
- **Why Possibly Novel:** Forgetting comparisons use aggregate metrics; the structured-fingerprint hypothesis with a capability battery is new.
- **Minimal Experiment:** Adapt one backbone with 5 PEFT methods × 4 tasks; run the retention battery; test fingerprint stability across tasks.
- **Main Risk:** Battery design choices shape fingerprints; pre-register the battery and report all components.
- **Research Cluster:** PEFT

### IDEA-C-0289 — Style shifts need rank 1; semantic shifts need rank ≥ class count
- **One-sentence idea:** Test the sharp quantitative claim that photometric/style domain shifts are correctable by rank-1 LoRA updates while semantic remappings require rank scaling with the number of remapped classes — a shift-taxonomy-to-rank dictionary.
- **Problem:** The rank laws (IDEA-C-0131/0145/0282) need a mechanistic anchor: what does one rank dimension actually buy?
- **Core Hypothesis (falsifiable):** On synthetic shift ladders (parametric style shifts; k-class label remaps), required rank is ~1 for style regardless of shift magnitude, and grows near-linearly in k for remaps — with mixed natural shifts decomposable into measured style+semantic components whose predicted rank sum matches the empirical requirement.
- **Why Important:** Gives rank a concrete semantic (one dimension ≈ one global transform or one class-level correction), unifying the PEFT cluster's laws into an interpretable model.
- **Why Possibly Novel:** Rank requirements have never been tied to a shift taxonomy with additive predictions.
- **Minimal Experiment:** Build style-shift and k-remap ladders on VOC; find minimal sufficient ranks per rung; test additivity on constructed mixed shifts and one natural shift with estimated components.
- **Main Risk:** Semantic shifts in feature space may be cheaper than class count suggests (shared structure); the measured exponent is the finding either way.
- **Research Cluster:** PEFT

### IDEA-C-0290 — A CKA threshold governs adapter mergeability
- **One-sentence idea:** Test whether two adapters trained separately can be merged by weighted averaging if and only if their induced feature spaces exceed a CKA similarity threshold — giving the adapter-fusion practice a measurable precondition.
- **Problem:** Adapter merging works unpredictably (IDEA-C-0019 shows composition failures); a cheap compatibility test would prevent failed merges in multi-domain systems.
- **Core Hypothesis (falsifiable):** Across many adapter pairs, merged-model performance retention exhibits a sharp transition as a function of inter-adapter CKA (computed on shared unlabeled data), with the threshold stable across tasks and backbones — enabling merge/don't-merge decisions from forward passes alone.
- **Why Important:** Multi-tenant serving wants merged adapters; a validated precondition converts merging from gamble to engineering.
- **Why Possibly Novel:** Model-merging conditions are studied for full networks (basins, permutations); the adapter-level CKA-threshold law is untested.
- **Minimal Experiment:** Train 30 adapter pairs spanning task/domain distances; measure CKA and merge outcomes; locate and validate the transition on held-out pairs.
- **Main Risk:** Threshold may drift with adapter capacity; include rank as a covariate.
- **Research Cluster:** PEFT

### IDEA-C-0291 — Where should parameters live: PEFT backbone vs heavy decoder at iso-budget
- **One-sentence idea:** Resolve the allocation question — given a fixed trainable-parameter budget on a frozen VFM, does dense-task accuracy favor spending it inside the backbone (LoRA/adapters) or in a larger task decoder — and test whether the answer flips with task-to-pretraining similarity.
- **Problem:** Papers default to one allocation without comparing; the choice plausibly interacts with how much the backbone's features already suffice.
- **Core Hypothesis (falsifiable):** At iso-parameter budgets, decoder-heavy allocation wins when frozen-feature probes are already strong (similar tasks: parameters buy readout), while backbone-PEFT wins when probes are weak (dissimilar tasks: parameters must fix features) — with the crossover predictable from probe accuracy, unifying allocation with the similarity metrics of the ECON cluster.
- **Why Important:** The most basic architecture decision in every adaptation project gets a measured decision rule.
- **Why Possibly Novel:** Both allocations are used everywhere; the controlled iso-budget comparison with a similarity-based crossover law is missing.
- **Minimal Experiment:** Sweep allocation ratios at 3 budgets on 6 tasks spanning similarity; fit the crossover; validate on 2 held-out tasks.
- **Main Risk:** Decoder architecture choice adds a dimension; fix one strong decoder family and vary only capacity.
- **Research Cluster:** PEFT

### IDEA-C-0292 — Enforced orthogonality prevents multi-dataset adapter interference
- **One-sentence idea:** Test whether constraining sequentially-trained LoRA updates to mutually orthogonal subspaces eliminates cross-dataset interference in continual PEFT, at a measurable capacity cost — quantifying the interference-capacity trade-off that unconstrained continual adaptation hides.
- **Problem:** Continual PEFT on dataset sequences interferes (new updates overwrite old task directions), but the geometric structure of interference and the cost of preventing it are unmeasured.
- **Core Hypothesis (falsifiable):** Interference magnitude between sequential tasks correlates with their update-subspace overlap (principal angles); hard orthogonality constraints reduce backward interference to near zero while costing forward accuracy proportional to the "natural overlap" the tasks wanted to share — mapping the trade-off curve and identifying when soft (partial) orthogonality is optimal.
- **Why Important:** Continual adaptation of shared VFMs is the deployment norm; a geometric control knob with a measured trade-off beats replay heuristics.
- **Why Possibly Novel:** Orthogonal gradient methods exist in continual learning; the LoRA-subspace instantiation with trade-off quantification for dense tasks is new (and directly tests IDEA-C-0019's mechanism).
- **Minimal Experiment:** Sequentially adapt across 5 dense datasets with {none, soft, hard} orthogonality; measure interference vs subspace angles; map the trade-off frontier.
- **Main Risk:** Orthogonality in weight space may not imply functional orthogonality; measure both.
- **Research Cluster:** PEFT

### IDEA-C-0293 — PEFT's sample efficiency is inherited augmentation invariance
- **One-sentence idea:** Test whether PEFT's small-data advantage over full FT is substantially explained by preservation of pretrained invariances (augmentation robustness the pretrained model owns and full FT destroys), rather than by parameter-count regularization per se.
- **Problem:** The standard explanation for PEFT's low-shot wins is fewer parameters; an invariance-retention mechanism predicts different interventions (invariance-protected full FT should match PEFT).
- **Core Hypothesis (falsifiable):** Measured invariance retention (feature stability under transforms) during adaptation predicts low-shot generalization across methods better than trainable-parameter count; full FT with invariance-preserving regularization (feature-consistency penalties to the pretrained model under augmentation) matches PEFT at low shots — dissociating the two explanations.
- **Why Important:** Identifies the active ingredient of PEFT's most-cited advantage, enabling its transplantation into any tuning scheme.
- **Why Possibly Novel:** Parameter-efficiency and invariance literatures are disjoint; the mediation analysis with a transplantation test is new.
- **Minimal Experiment:** Track invariance metrics during PEFT/full-FT at shot sweeps; run mediation analysis; test invariance-regularized full FT.
- **Main Risk:** Invariance metrics must cover the right transform family; use a broad measured battery.
- **Research Cluster:** PEFT

### IDEA-C-0294 — Single-layer sensitivity profiling finds the one layer worth adapting
- **One-sentence idea:** Test whether adapting only the single layer with maximal measured feature-distribution shift captures most of full-PEFT's gain across domain-shift tasks — the extreme-economy end of placement science.
- **Problem:** Placement studies compare coarse strategies (early/late/all); if shift concentrates in one identifiable layer per domain pair, adaptation cost collapses.
- **Core Hypothesis (falsifiable):** Layer-wise shift profiles (frozen-feature divergence between source and target) are strongly peaked for style-type shifts; adapting the peak layer recovers a large majority of all-layer PEFT gains, while adapting an off-peak layer of equal capacity does not — and profile peakedness (measurable upfront) predicts when single-layer economy is safe.
- **Why Important:** Minimal-footprint adaptation for edge deployment, plus a shift-localization diagnostic reusable across the cluster (connects to IDEA-C-0223's placement law).
- **Why Possibly Novel:** Layer-wise probing exists; the peak-layer-sufficiency claim with a peakedness precondition is untested.
- **Minimal Experiment:** Profile shifts for 10 domain pairs; run peak/off-peak/all-layer adaptation; fit the sufficiency-vs-peakedness relationship.
- **Main Risk:** Semantic shifts will be distributed; the precondition explicitly scopes the method.
- **Research Cluster:** PEFT

### IDEA-C-0295 — LoRA dropout is rank annealing in disguise
- **One-sentence idea:** Test whether dropout applied inside LoRA modules functions as implicit rank annealing (stochastically reducing effective update rank early, growing it as training stabilizes), explaining its benefits and enabling a deterministic replacement schedule.
- **Problem:** LoRA dropout is cargo-culted from NLP recipes with no dense-task account of what it does to the low-rank structure.
- **Core Hypothesis (falsifiable):** Effective-rank trajectories under LoRA dropout show suppressed early rank converging to the no-dropout ceiling late; a deterministic rank-growth schedule matched to the measured trajectory reproduces dropout's final accuracy and stability without stochasticity — confirming the annealing mechanism and yielding a cleaner control (linking to IDEA-C-0061's collapse dynamics from the opposite direction).
- **Why Important:** Replaces an unexplained hyperparameter with an interpretable schedule and completes the picture of rank dynamics during adaptation.
- **Why Possibly Novel:** Dropout theory exists generically; the rank-annealing interpretation specific to low-rank adapters is untested.
- **Minimal Experiment:** Log effective-rank trajectories under dropout sweeps on 3 dense tasks; design matched deterministic schedules; compare accuracy/stability.
- **Main Risk:** Dropout may also regularize direction (not just rank); include direction-noise controls.
- **Research Cluster:** PEFT

### IDEA-C-0296 — Boundary sharpness requires leaving the kernel regime
- **One-sentence idea:** Test whether the residual gap between PEFT and full fine-tuning on boundary-precision metrics is explained by PEFT remaining in the lazy/kernel regime (function changes representable by the frozen tangent space), with boundary sharpening specifically requiring rich-regime feature learning.
- **Problem:** PEFT matches full FT on interior metrics but often lags on boundaries; if the gap is regime-theoretic, no amount of rank tuning closes it — only regime-crossing interventions do.
- **Core Hypothesis (falsifiable):** Kernel-distance measurements show PEFT solutions close to linearized-model predictions while full FT departs; the per-task boundary gap correlates with the measured regime distance, and regime-crossing PEFT variants (large-init adapters per IDEA-C-0090, or brief full-FT warm phases) close the boundary gap specifically — confirming the mechanism.
- **Why Important:** Explains the one metric family where PEFT reliably lags and prescribes the minimal fix, uniting PEFT practice with feature-learning theory.
- **Why Possibly Novel:** Lazy/rich analysis hasn't been connected to the boundary-metric gap, the dense-prediction community's concrete pain point.
- **Minimal Experiment:** Measure kernel distances and metric-decomposed gaps across PEFT configurations on 4 tasks; test regime-crossing variants; report the mediation.
- **Main Risk:** Kernel-distance estimation on large models is approximate; use multiple probes (linearization error, feature movement).
- **Research Cluster:** PEFT

### IDEA-C-0297 — Quantization noise and low-rank correction interact on thin structures
- **One-sentence idea:** Test whether QLoRA-style adaptation (quantized backbone + LoRA) concentrates its residual errors on thin structures because quantization noise is spatially white while low-rank corrections are spatially smooth — a structural mismatch invisible in aggregate metrics.
- **Problem:** Quantized-backbone PEFT is the default efficient recipe; its error anatomy for dense tasks is unexamined (extending IDEA-C-0139's inference-time result to the training loop).
- **Core Hypothesis (falsifiable):** At matched aggregate mIoU, QLoRA models show a specific thin-structure/boundary deficit relative to full-precision LoRA, with the deficit's spatial spectrum matching the prediction (high-frequency error uncorrectable by low-rank smooth updates); allocating a small high-resolution correction channel (sparse full-precision layers at the stem) removes it.
- **Why Important:** Protects the fine-structure applications (medical, industrial) most likely to adopt efficient recipes, with a targeted architectural patch.
- **Why Possibly Novel:** QLoRA evaluations are aggregate; the spatial-spectrum error analysis with the smoothness-mismatch mechanism is new.
- **Minimal Experiment:** Compare QLoRA vs LoRA at matched configs on vessel/crack tasks; compute error spectra and width-stratified metrics; test the stem-precision patch.
- **Main Risk:** Quantization scheme dependence; test two (NF4-style and int8).
- **Research Cluster:** PEFT

### IDEA-C-0298 — Temporal-attention-only adapters convert image VFMs to video segmenters
- **One-sentence idea:** Test whether adapting only newly-inserted temporal attention (leaving all spatial computation frozen) suffices to convert image VFMs into competitive video segmenters — establishing the minimal sufficient "motion adapter" and what temporal reasoning it cannot capture.
- **Problem:** Video adaptation of image VFMs ranges from full fine-tuning to elaborate temporal modules; the minimal-intervention baseline is never rigorously established.
- **Core Hypothesis (falsifiable):** Frozen-spatial + trained-temporal-attention models match full video fine-tuning on association-driven metrics (identity persistence, temporal smoothness) while showing a specific residual deficit on motion-appearance interaction cases (deformation, motion blur) that spatial adaptation demonstrably requires — cleanly factoring video capability into cheap association and expensive appearance-dynamics components.
- **Why Important:** Defines the real cost structure of image-to-video conversion and gives most applications the cheap sufficient recipe.
- **Why Possibly Novel:** Temporal adapters exist in video recognition; the sufficiency-and-residual factorization for dense video prediction is unmapped.
- **Minimal Experiment:** Train temporal-only vs spatial+temporal adaptation on VOS/VSS benchmarks; decompose metrics into association vs appearance-dynamics components; locate the residual.
- **Main Risk:** Metric factorization requires careful definition; adapt existing VOS decomposition protocols.
- **Research Cluster:** PEFT

### IDEA-C-0299 — Hypernetwork-generated per-image adapters for heterogeneous datasets
- **One-sentence idea:** Test whether a small hypernetwork generating image-conditional LoRA parameters outperforms both a single shared adapter and a mixture-of-adapters on heterogeneous datasets (multi-site, multi-condition), by matching adaptation to per-image latent domain continuously.
- **Problem:** Real datasets are mixtures of latent domains (sites, weather, devices); a single adapter averages over them and discrete mixtures need domain labels or clustering.
- **Core Hypothesis (falsifiable):** On controlled heterogeneous mixtures, per-image generated adapters recover most of the oracle per-domain-adapter performance without domain labels, beating shared adapters by margins proportional to measured dataset heterogeneity, and the hypernetwork's latent input space recovers the true domain structure (interpretability check).
- **Why Important:** Removes the homogeneity assumption baked into standard PEFT, matching the messy composition of deployment data.
- **Why Possibly Novel:** Hypernetworks for adapters exist in multi-task NLP; the continuous latent-domain formulation for dense vision with heterogeneity-scaled validation is new.
- **Minimal Experiment:** Build controlled mixtures (sites/corruption types); train shared vs mixture vs hypernetwork adapters; evaluate vs oracle; probe the latent space against true domain labels.
- **Main Risk:** Hypernetwork instability; use low-dimensional generation targets (rank-1 modulations) first.
- **Research Cluster:** PEFT

### IDEA-C-0300 — Adapter capacity is a label-noise filter: the clean-data rank discount
- **One-sentence idea:** Test whether optimal PEFT capacity shrinks measurably with label quality — noisy labels demanding extra capacity that is spent fitting noise — making the rank law noise-aware and PEFT a diagnostic of dataset cleanliness.
- **Problem:** Rank/capacity laws (IDEA-C-0131/0282) implicitly assume fixed label quality; if noise inflates apparent capacity needs, teams over-provision on dirty data and mis-estimate laws.
- **Core Hypothesis (falsifiable):** Injecting calibrated boundary/class noise into clean datasets shifts the accuracy-vs-rank curve peak upward in rank and downward in accuracy, with the peak shift proportional to injected noise level; inversely, the measured peak shift on a natural dataset estimates its noise level, validated against re-annotation audits — turning capacity sweeps into a noise meter.
- **Why Important:** Corrects capacity budgeting for real (noisy) data and yields a free label-quality estimator from experiments teams already run.
- **Why Possibly Novel:** Noise-capacity interactions are studied for memorization in full training; the PEFT-rank version with the inverse (noise-metering) application is new.
- **Minimal Experiment:** Rank sweeps at noise-injection levels on 2 clean datasets; fit peak-shift vs noise; apply inversely to 2 natural datasets with audit-verified noise levels.
- **Main Risk:** Noise type matters (boundary vs class); calibrate separate curves per type.
- **Research Cluster:** PEFT

### IDEA-C-0301 — Is there a universal PEFT scaling exponent?
- **One-sentence idea:** Test whether fine-tuning loss vs LoRA rank follows a power law with an exponent that is universal across dense tasks (task-independent slope, task-dependent offset) — the PEFT analog of universality claims in pretraining scaling laws.
- **Problem:** Scattered rank ablations hint at diminishing returns but no one has tested whether the functional form and exponent replicate across tasks, which determines whether PEFT budgeting can use one master curve.
- **Core Hypothesis (falsifiable):** Across ≥10 diverse dense tasks at matched optimization quality, log-loss vs log-rank is linear over a substantial range with exponents clustered tightly (universality), deviations concentrating in tasks with extreme mask-geometry statistics (predictable via IDEA-C-0282's complexity axis) — or exponents scatter widely, refuting universality and requiring per-task calibration; either outcome settles a planning-relevant question.
- **Why Important:** Universality would collapse PEFT budgeting to one measurement per task family; its refutation would redirect effort to task-property models.
- **Why Possibly Novel:** No systematic cross-task PEFT scaling-form study exists; individual ablations don't test universality.
- **Minimal Experiment:** Rank sweeps (8 points, 3 seeds) on 10 tasks with standardized optimization; fit power laws; test exponent homogeneity statistically.
- **Main Risk:** Optimization quality confounds at extreme ranks; use per-rank LR sweeps.
- **Research Cluster:** PEFT

### IDEA-C-0302 — PEFT edits near prototypes; full FT edits the periphery
- **One-sentence idea:** Test where in feature space each tuning method changes decisions: PEFT preferentially moving decision boundaries near class prototypes (dense data regions) while full FT also reshapes far-from-prototype periphery — explaining their different OOD behaviors from geometry.
- **Problem:** PEFT-vs-FT robustness differences are reported without a spatial account of what changed in representation space.
- **Core Hypothesis (falsifiable):** Measuring per-sample decision-change rates as a function of distance-to-prototype, PEFT's changes decay sharply with distance while full FT's persist; consequently PEFT preserves pretrained behavior on outliers (better OOD retention, worse OOD adaptation) — with the geometry quantitatively predicting each method's corruption-benchmark deltas.
- **Why Important:** A geometric mechanism unifying scattered robustness observations into a predictive account, informing method choice by where a deployment's hard cases live.
- **Why Possibly Novel:** Feature-space change analysis exists for full FT; the prototype-distance-resolved comparison across tuning methods is new.
- **Minimal Experiment:** Compare decision-change-vs-distance profiles for PEFT/full FT on 4 tasks; correlate profiles with measured OOD retention/adaptation deltas.
- **Main Risk:** Prototype-distance is representation-dependent; compute in the frozen pretrained space as the fixed reference.
- **Research Cluster:** PEFT

### IDEA-C-0303 — Merged vs unmerged LoRA differ numerically exactly at boundaries
- **One-sentence idea:** Test whether merging LoRA weights into the backbone (vs keeping the side-branch at inference) changes dense predictions measurably — with differences concentrating on boundary pixels where logit margins are thin — an unexamined numerics choice contaminating reproducibility.
- **Problem:** Merging is treated as mathematically neutral (it is, in exact arithmetic), but float summation order and quantized-inference interactions differ, and dense outputs threshold thin margins everywhere along boundaries.
- **Core Hypothesis (falsifiable):** Merged and unmerged inference of identical adapters produce pixel-level prediction differences at rates far above zero, concentrated at low-margin (boundary) pixels, amplified under fp16/quantized inference — with boundary-F differences occasionally exceeding typical reported method deltas, establishing a required reporting convention (merge state + precision).
- **Why Important:** A cheap reproducibility audit protecting boundary-metric comparisons across the entire adapter ecosystem.
- **Why Possibly Novel:** Numerics-sensitivity studies target training; the merge-state inference discrepancy for dense outputs is undocumented.
- **Minimal Experiment:** Compare merged/unmerged inference across precisions on 4 adapted models; map disagreement vs pixel margin; quantify metric impact.
- **Main Risk:** Effects may be negligible at fp32 — the precision-stratified result is the contribution either way.
- **Research Cluster:** PEFT

### IDEA-C-0304 — Greedy rank growth beats fixed-rank training at equal final capacity
- **One-sentence idea:** Test whether growing LoRA rank during training (adding singular directions as prior ones converge) beats fixed-rank training at identical final rank — because sequential subspace discovery avoids the interference and collapse (IDEA-C-0061) of joint optimization.
- **Problem:** Rank is fixed at initialization by convention; if adaptation subspaces are best discovered greedily (largest correction first), the convention wastes capacity.
- **Core Hypothesis (falsifiable):** Rank-growth schedules reach higher final accuracy and effective-rank utilization than fixed-rank baselines at matched final rank and compute across dense tasks, with per-added-direction gains following a decreasing profile that validates the greedy-discovery mechanism (each new direction targets the largest residual error mode, verifiable by error-mode analysis).
- **Why Important:** A free training-recipe improvement with a mechanistic account, and independent evidence for the nested-subspace structure claimed in IDEA-C-0145.
- **Why Possibly Novel:** Progressive-capacity training exists (net2net, progressive GANs); the LoRA-subspace instantiation with error-mode validation is new.
- **Minimal Experiment:** Compare fixed vs grown rank at matched endpoints on 4 tasks; track per-direction contributions and effective-rank utilization; run the error-mode alignment analysis.
- **Main Risk:** Growth schedules add hyperparameters; use convergence-triggered automatic growth.
- **Research Cluster:** PEFT

### IDEA-C-0305 — Adaptation-path dependence: A→B→C is not A→C
- **One-sentence idea:** Test whether sequential PEFT through an intermediate task (A→B→C) systematically outperforms or underperforms direct adaptation (A→C) depending on measurable relations among the tasks — mapping the geometry of "adaptation space" and its triangle-inequality violations.
- **Problem:** Practitioners chain adaptations opportunistically (natural→general-medical→specific-organ) with no theory of when intermediate stepping stones help or hurt.
- **Core Hypothesis (falsifiable):** Stepping-stone benefit is predicted by whether B lies "between" A and C in measurable feature-shift geometry (B reduces the maximum single-step shift) and hurt by B introducing orthogonal shifts (measurable as added update-subspace dimensions unused by C); the fitted geometric rule predicts held-out path outcomes with useful accuracy — establishing adaptation-route planning as a computable problem.
- **Why Important:** Multi-step adaptation is common practice with zero guidance; route planning from cheap measurements would change workflows and reveal the metric structure of task space.
- **Why Possibly Novel:** Transferability estimation targets single hops; multi-hop path geometry with violation analysis is unexplored.
- **Minimal Experiment:** Construct 12 (A,B,C) triples spanning betweenness structures; run both routes at matched budgets; fit and validate the geometric predictor.
- **Main Risk:** Path outcomes are seed-noisy; use multiple seeds and effect-size thresholds.
- **Research Cluster:** PEFT
## Cluster FSS — Few/Zero-Shot Segmentation (IDEA-C-0306 … IDEA-C-0320)

### IDEA-C-0306 — The pose-gap law of support-query correspondence
- **One-sentence idea:** Quantify few-shot segmentation accuracy as a function of the pose/viewpoint gap between support and query objects, testing whether correlation-based FSS methods fail beyond a predictable pose threshold that prototype-based methods survive.
- **Problem:** FSS methods are compared on pose-uncontrolled episodes; if method families have different pose-gap tolerances, aggregate rankings hide the deployment-relevant structure.
- **Core Hypothesis (falsifiable):** Accuracy-vs-pose-gap curves (episodes stratified by estimated relative pose) show correlation/matching methods degrading steeply beyond a measurable gap while prototype-pooling methods degrade gently — a crossover implying method choice should depend on expected pose diversity, with pose-canonicalized supports recovering the matching methods' losses.
- **Why Important:** Turns an invisible episode covariate into a method-selection rule and a cheap fix (support canonicalization).
- **Why Possibly Novel:** Pose sensitivity is unexamined in FSS evaluation; episodes have never been pose-stratified.
- **Minimal Experiment:** Estimate relative poses for PASCAL-5i/COCO-20i episodes (keypoint or retrieval-based); re-evaluate 6 FSS methods pose-stratified; test canonicalization.
- **Main Risk:** Pose estimation for arbitrary categories is rough; validate the stratification on rigid-object subsets first.
- **Research Cluster:** FSS

### IDEA-C-0307 — Is FSS solved by nearest-neighbor matching at VFM scale?
- **One-sentence idea:** Establish whether a pure training-free baseline — per-patch nearest-neighbor matching from query to support over frozen VFM features — matches modern FSS methods, testing if the task's benchmarks still measure anything beyond backbone quality.
- **Problem:** FSS methods grow more complex while backbone features improve underneath them; the field lacks a periodically-updated strongest-trivial-baseline audit.
- **Core Hypothesis (falsifiable):** Frozen DINOv2-scale features with careful NN-matching (multi-scale, spatial regularization but no learning) fall within a small margin of published SOTA on standard FSS benchmarks, with the residual method gains concentrated in identifiable episode types (multi-instance, scale mismatch) — redefining where FSS research should focus.
- **Why Important:** Prevents the field from optimizing machinery whose benefits the backbone already provides, and localizes the genuinely open sub-problems.
- **Why Possibly Novel:** Training-free baselines appear occasionally; a rigorous audit with residual-episode characterization at current backbone scale is due and missing.
- **Minimal Experiment:** Implement the strongest NN pipeline on frozen features; evaluate on 3 FSS benchmarks against published numbers; characterize surviving-gap episodes.
- **Main Risk:** Pipeline tuning could be criticized as learning-in-disguise; freeze all choices on a dev split, report sensitivity.
- **Research Cluster:** FSS

### IDEA-C-0308 — Background co-occurrence leaks class identity into FSS episodes
- **One-sentence idea:** Measure how much FSS performance derives from background/context matching between support and query (class-correlated backgrounds), using background-swapped episodes to isolate genuine object-level few-shot learning.
- **Problem:** Support and query images of a class share habitats (boats/water); methods may match contexts rather than learn objects, inflating benchmark numbers (sharpening IDEA-C-0034's audit into an interventional test).
- **Core Hypothesis (falsifiable):** Replacing episode backgrounds via compositing (objects preserved, contexts randomized) drops FSS methods nonuniformly — context-reliant methods losing most — and reorders at least some rankings; the per-method context reliance is predictable from attention-map analysis on original episodes.
- **Why Important:** Distinguishes object-learning from context-matching capability, which behave oppositely under deployment distribution shift.
- **Why Possibly Novel:** Context bias is measured in classification; the interventional background-swap protocol for FSS ranking stability is new.
- **Minimal Experiment:** Build background-swapped versions of standard episodes with compositing quality controls; re-evaluate 6 methods; correlate drops with attention-based context-reliance scores.
- **Main Risk:** Compositing artifacts; include artifact-matched control episodes (swap with same-class backgrounds).
- **Research Cluster:** FSS

### IDEA-C-0309 — One positive plus many cheap negatives beats k positives
- **One-sentence idea:** Test whether few-shot class definition is more sample-efficient through negatives — one positive support plus several negative supports from confusable classes — than through additional positives, because class boundaries are defined by contrast, not central tendency.
- **Problem:** FSS protocol fixates on k positive shots; negatives from other classes are nearly free (existing datasets) but the positive/negative budget trade-off has never been mapped.
- **Core Hypothesis (falsifiable):** At matched total support budgets, 1-positive + (k−1)-confusable-negatives episodes outperform k-positive episodes whenever the target class has close confusers (measurable in feature space), with the advantage predicted by confuser proximity — reframing support-set design around contrastive information.
- **Why Important:** Changes how few-shot systems should solicit examples from users (ask for confusers, not more positives) at zero data-collection cost.
- **Why Possibly Novel:** Negative supports appear in some formulations; the budget-controlled trade-off law with confuser-proximity prediction is unmapped.
- **Minimal Experiment:** Construct budget-matched episode variants on COCO-20i with confuser selection; evaluate prototype and matching methods; fit advantage vs confuser proximity.
- **Main Risk:** Confuser choice policies vary; compare oracle, retrieval-based, and random confusers.
- **Research Cluster:** FSS

### IDEA-C-0310 — Pretraining diversity, not scale, drives in-context segmentation
- **One-sentence idea:** Test whether visual in-context segmentation ability scales with pretraining task/domain diversity rather than model size or data volume — a controlled decomposition of what makes generalist dense models few-shot capable.
- **Problem:** In-context vision models confound scale, data volume, and diversity; if diversity is the active ingredient, small diverse models beat large narrow ones — inverting the scaling narrative for this capability.
- **Core Hypothesis (falsifiable):** In controlled small-scale pretraining (fixed compute/parameters, varied task-diversity), in-context generalization to held-out tasks grows steeply with diversity and weakly with volume-at-fixed-diversity; the diversity effect saturates at a measurable task-count, and the same ordering holds across two model scales — establishing diversity as the binding variable.
- **Why Important:** Redirects generalist-model investment from scale to curriculum breadth, with a measured saturation point for planning.
- **Why Possibly Novel:** Diversity effects are studied for classification transfer; controlled diversity-vs-volume decomposition for in-context dense ability is new.
- **Minimal Experiment:** Pretrain SegGPT-style small models on task-mixture grids (diversity × volume at fixed compute); evaluate held-out-task in-context performance; replicate at a second scale.
- **Main Risk:** Small-scale results may not extrapolate; the two-scale consistency check addresses trend validity.
- **Research Cluster:** FSS

### IDEA-C-0311 — Support choice matters more than support quality
- **One-sentence idea:** Measure the headroom from optimal support selection (which examples to use) vs support annotation quality (how well they're masked), testing whether FSS research optimizes the wrong variable.
- **Problem:** Methods refine how supports are used and assume masks must be precise; if selection dominates quality, the practical lever is retrieval, not annotation care.
- **Core Hypothesis (falsifiable):** Oracle support selection (best-of-pool per query) improves FSS accuracy several times more than upgrading support masks from rough to precise (controlled degradation sweeps); moreover, learned support-retrieval (selecting by feature affinity to the query) captures most of the oracle headroom — making selection a solved-in-principle, unexploited gain.
- **Why Important:** Reorders the field's effort allocation and enables an immediate system improvement (retrieve good supports, annotate them roughly).
- **Why Possibly Novel:** Support sensitivity is noted anecdotally; the selection-vs-quality headroom comparison with a retrieval solution is unquantified.
- **Minimal Experiment:** On standard benchmarks with support pools, measure oracle-selection and mask-degradation effects for 4 methods; implement retrieval-based selection; report captured headroom.
- **Main Risk:** Oracle selection overfits the metric; use disjoint pools for selection and evaluation.
- **Research Cluster:** FSS

### IDEA-C-0312 — Nameability predicts when a word beats an example
- **One-sentence idea:** Test whether the choice between zero-shot (class name) and one-shot (visual example) is governed by the class's measurable "nameability" (naming agreement/entropy from psycholinguistics), giving a per-class modality-selection rule.
- **Problem:** Zero-shot and few-shot dense methods are benchmarked separately; practitioners choosing per class have no principled rule for when language suffices.
- **Core Hypothesis (falsifiable):** Per-class zero-shot-minus-one-shot accuracy differences correlate strongly with naming-agreement scores (high-agreement classes: names win or tie; low-agreement/visually-defined classes: examples win), and the fitted rule transfers across datasets — unifying the two paradigms under a psycholinguistic covariate (complementing IDEA-C-0264's error-structure analysis).
- **Why Important:** A deployment-ready selection rule and a quantitative bridge between human concept-naming research and machine grounding.
- **Why Possibly Novel:** Language-vs-example comparisons exist in aggregate; the nameability covariate analysis is new.
- **Minimal Experiment:** Collect/reuse naming-agreement norms for benchmark classes; measure per-class zero- vs one-shot deltas for 3 systems; fit and transfer-test the rule.
- **Main Risk:** Naming norms exist mainly for common object classes; collect lightweight norms (10 namers) for the rest.
- **Research Cluster:** FSS

### IDEA-C-0313 — Cross-domain FSS failure is style, not semantics
- **One-sentence idea:** Decompose cross-domain few-shot segmentation failure (natural→medical/aerial supports) into style-statistics mismatch vs semantic-structure mismatch, testing whether cheap style normalization recovers most of the cross-domain gap.
- **Problem:** Cross-domain FSS is treated as a hard open problem; if the dominant failure is first-order style statistics (contrast, texture spectra) rather than semantic incompatibility, the fix is preprocessing, not new meta-learners.
- **Core Hypothesis (falsifiable):** Style-normalizing supports and queries into a shared statistics frame (histogram/feature-moment matching) recovers a large fraction of the natural-to-X FSS gap across target domains, with the residual gap correlating with semantic-structure divergence measures — cleanly budgeting the problem between preprocessing and research.
- **Why Important:** Redirects a subfield toward its actually-open component and provides an immediately usable boost.
- **Why Possibly Novel:** Style normalization is standard in DA; its decomposition role in cross-domain FSS specifically is untested.
- **Minimal Experiment:** Evaluate 4 FSS methods natural→{medical, aerial, industrial} with and without style normalization arms; report gap decomposition per target domain.
- **Main Risk:** Style normalization may destroy domain-relevant cues (speckle, IDEA-C-0218); include per-domain cue audits.
- **Research Cluster:** FSS

### IDEA-C-0314 — The transductive-gain curve: unlabeled query sets as the hidden budget
- **One-sentence idea:** Quantify how transductive FSS gains (using the query set's own statistics) scale with the number of unlabeled queries available, testing whether reported transductive advantages depend critically on an evaluation-protocol variable nobody standardizes.
- **Problem:** Transductive methods report wins under fixed (often generous) query-batch assumptions; deployment batch sizes vary from one image to thousands, and the gain-vs-batch curve is unmapped.
- **Core Hypothesis (falsifiable):** Transductive gains follow a predictable saturating curve in query-batch size, crossing zero benefit below a measurable batch threshold (where statistics mislead) — with methods differing mainly in their curve's threshold, so single-image deployment eliminates most published transductive advantages.
- **Why Important:** Corrects a protocol-sensitivity blind spot that determines whether a method family is deployable at all in streaming settings.
- **Why Possibly Novel:** Transduction is compared at fixed protocols; the batch-size response curve as the method-characterizing object is new.
- **Minimal Experiment:** Re-evaluate 4 transductive FSS/zero-shot methods across query-batch sizes {1..1000}; fit gain curves; report thresholds and reordering.
- **Main Risk:** Batch composition (class mixture) interacts with size; control composition explicitly.
- **Research Cluster:** FSS

### IDEA-C-0315 — Component attribution: recent FSS progress may be feature denoising
- **One-sentence idea:** Attribute recent FSS method gains to their shared implicit component — outlier-token suppression/feature denoising on frozen VFM features — testing whether a standalone denoising step reproduces most published improvements.
- **Problem:** FSS papers bundle many components; if a common unacknowledged ingredient (cleaning DINOv2's outlier tokens) drives gains, the literature's causal narratives are wrong and the ingredient deserves direct study.
- **Core Hypothesis (falsifiable):** Adding a simple token-denoising step (outlier suppression, feature smoothing) to a plain baseline recovers a large fraction of the gap to recent SOTA on FSS benchmarks, and ablating denoising-like components from published methods costs them most of their advantage — establishing the shared mechanism.
- **Why Important:** Prevents redundant architectural elaboration and isolates the transferable core that also benefits other frozen-feature tasks.
- **Why Possibly Novel:** Feature-artifact cleanup (register tokens) is known in representation analysis; its role as the hidden engine of FSS progress is untested.
- **Minimal Experiment:** Implement 3 denoising variants on a plain NN baseline (extends IDEA-C-0307); ablate corresponding components in 3 recent methods; report attribution.
- **Main Risk:** Attribution requires faithful reproductions; use released code only.
- **Research Cluster:** FSS

### IDEA-C-0316 — Part-visibility mismatch breaks prototype FSS on articulated objects
- **One-sentence idea:** Test whether prototype-based FSS fails on multi-part objects specifically when support and query show different part subsets (visibility mismatch), and whether minimal part-aware prototypes (unsupervised part decomposition) fix it.
- **Problem:** Single-vector prototypes average over parts; when the query shows parts absent from support (or vice versa), matching degrades — a structured failure that aggregate metrics record as generic difficulty.
- **Core Hypothesis (falsifiable):** Stratifying episodes by measured part-overlap (via unsupervised part discovery), accuracy drops steeply with decreasing overlap for single-prototype methods but not for multi-prototype/part-aware variants; the overlap covariate explains a substantial share of within-class episode variance — turning "hard episodes" into a predictable geometry.
- **Why Important:** Articulated and partially-visible objects dominate real deployments (people, animals, machinery); a predictable failure covariate enables both stratified evaluation and targeted fixes.
- **Why Possibly Novel:** Part-based FSS exists as architecture; the visibility-mismatch causal analysis with episode stratification is new.
- **Minimal Experiment:** Compute part-overlap scores for episodes via DINO-feature clustering; re-evaluate single- vs multi-prototype methods stratified; test a minimal part-aware baseline.
- **Main Risk:** Unsupervised parts are imperfect; validate part discovery against annotated-parts subsets.
- **Research Cluster:** FSS

### IDEA-C-0317 — Shape transfers across classes better than texture in the few-shot regime
- **One-sentence idea:** Test whether few-shot boundary quality is supported by cross-class shape priors (transferable from other classes' abundant masks) more than texture priors, implying FSS systems should import a class-agnostic shape model rather than learn everything from supports.
- **Problem:** FSS treats each novel class as informationally isolated, though object boundaries share class-agnostic regularities (smoothness statistics, closure, part structure) learnable from any labeled class.
- **Core Hypothesis (falsifiable):** A class-agnostic shape prior trained on base classes (boundary-statistics model or mask autoencoder) improves novel-class FSS boundary metrics by margins exceeding equivalent-capacity texture priors, with the gain invariant to base-novel semantic distance (confirming class-agnosticity) — while interior/semantic metrics are unaffected (specificity).
- **Why Important:** Decomposes few-shot learning into what truly needs the supports (appearance) and what doesn't (shape statistics), reducing effective sample complexity.
- **Why Possibly Novel:** Shape priors are classical; their controlled class-transfer analysis in the modern FSS regime with specificity tests is new.
- **Minimal Experiment:** Train shape and texture priors on base classes; add each to an FSS baseline; evaluate novel-class metric decomposition across semantic distances.
- **Main Risk:** Shape/texture prior capacities must be matched carefully; use parameter- and data-matched implementations.
- **Research Cluster:** FSS

### IDEA-C-0318 — Generated supports only work when the generator hasn't seen the class
- **One-sentence idea:** Test whether diffusion-generated support images for FSS help through genuine visual-concept synthesis or through leaking the generator's pretraining knowledge of the "novel" class — using generator-training-data audits as the control.
- **Problem:** Synthetic-support FSS reports gains, but if the generator saw the class abundantly, the pipeline is retrieval-from-generator-memory dressed as few-shot learning — invalid exactly for genuinely novel deployment classes.
- **Core Hypothesis (falsifiable):** Synthetic-support gains correlate strongly with the class's estimated presence in generator training data (retrieval-density audits); for verifiably-rare or post-dataset-cutoff classes, gains shrink toward zero or negative — bounding the method's real-world applicability and quantifying the contamination channel (a generative sibling of IDEA-C-0035).
- **Why Important:** Determines whether a popular data-augmentation direction survives contact with actually-novel classes — its sole raison d'être.
- **Why Possibly Novel:** Generator contamination is discussed for evaluation; its role in synthetic-support FSS gains is unmeasured.
- **Minimal Experiment:** Reproduce a synthetic-support FSS pipeline; stratify class-wise gains by generator-corpus retrieval density; test on post-cutoff product/species classes.
- **Main Risk:** Retrieval-density is an imperfect contamination proxy; triangulate with generation-fidelity measures.
- **Research Cluster:** FSS

### IDEA-C-0319 — Function-vs-appearance: human few-shot segmentation as the missing baseline
- **One-sentence idea:** Collect human few-shot segmentation behavior on the same episodes as machine FSS, testing whether humans generalize by function/affordance (segmenting what the object is for) where machines generalize by appearance — and whether the divergence predicts machine failure cases.
- **Problem:** FSS lacks a human baseline, so the field doesn't know whether machine errors reflect information limits of the episode or a generalization-strategy gap.
- **Core Hypothesis (falsifiable):** On episodes designed to dissociate appearance from function (novel-looking instances of familiar functions, e.g., unconventional chairs), human one-shot segmentation succeeds where machines fail, with the machine-human gap concentrated on function-defined classes (quantifiable per class); on pure-texture classes the gap vanishes — mapping which classes need function-aware representations.
- **Why Important:** Sets the information-theoretic vs strategy-gap decomposition every benchmark needs, and identifies the class families where current FSS is structurally insufficient.
- **Why Possibly Novel:** Human baselines exist for classification; a controlled human-FSS study with the appearance/function dissociation design is new.
- **Minimal Experiment:** Build 100 dissociation episodes; collect segmentations from 20 humans and 5 FSS systems; compare gap structure across class types.
- **Main Risk:** Human annotation conventions differ from dataset conventions; use consensus-based scoring.
- **Research Cluster:** FSS

### IDEA-C-0320 — The meta-learning obsolescence threshold
- **One-sentence idea:** Test whether episodic meta-learning's advantage over plain fine-tuning/probing vanishes above a measurable pretraining-scale threshold for dense tasks — dating the obsolescence of a paradigm as backbones grow.
- **Problem:** Meta-learning was designed for weak features; whether its machinery still adds anything on modern VFM features — and at what backbone scale it stopped — is disputed and unmeasured for segmentation.
- **Core Hypothesis (falsifiable):** Across a backbone-scale ladder (same family, increasing pretraining), the meta-learning-vs-simple-baseline gap on FSS shrinks monotonically and crosses zero at an identifiable scale; beyond it, meta-learning's episodic machinery adds variance without accuracy — with the crossover replicating across two method families and two benchmarks (the FSS-specific sharpening of the general audit in IDEA-C-0307).
- **Why Important:** A dated obsolescence result prevents continued investment in machinery the substrate has outgrown, and characterizes what meta-learning was actually compensating for.
- **Why Possibly Novel:** Meta-learning critiques exist for classification circa small backbones; the scale-resolved crossover measurement for dense prediction is missing.
- **Minimal Experiment:** Run 2 meta-learners vs tuned simple baselines across 4 backbone scales on 2 FSS benchmarks; locate crossovers; test replication.
- **Main Risk:** Meta-learner hyperparameters must be honestly re-tuned per scale; budget-matched tuning protocols required.
- **Research Cluster:** FSS
## Cluster DA — Domain Adaptation (IDEA-C-0321 … IDEA-C-0335)

### IDEA-C-0321 — The three-component domain gap: ISP, content, label protocol
- **One-sentence idea:** Build a decomposition benchmark that splits any measured domain gap into camera-pipeline (ISP), scene-content, and label-protocol components, testing the claim that most published DA methods only address the ISP component.
- **Problem:** "Domain gap" is treated as a scalar; methods claiming general adaptation may fix only the easiest (photometric) slice, which existing benchmarks cannot reveal.
- **Core Hypothesis (falsifiable):** Constructing intermediate domains that isolate each component (re-ISP'd source images; content-matched subsets; protocol-harmonized labels per IDEA-C-0129), the gap decomposes approximately additively; published UDA methods close most of the ISP component, little of content, and none of protocol — a reproducible profile across benchmark pairs.
- **Why Important:** Gives DA research an honest scoreboard per component and tells practitioners which gaps their tools cannot fix.
- **Why Possibly Novel:** Gap decompositions are discussed conceptually; an operational benchmark with additivity tests and method profiling is not established.
- **Minimal Experiment:** Build the three intermediate domains for GTA→Cityscapes and Cityscapes→ACDC; measure component gaps; profile 5 UDA methods against components.
- **Main Risk:** Additivity may fail (interactions); report interaction terms explicitly.
- **Research Cluster:** DA

### IDEA-C-0322 — Staged adaptation should mirror the shift hierarchy: norms, then attention, then MLP
- **One-sentence idea:** Test whether adapting parameter groups in a staged order matched to shift structure (normalization first, attention second, MLP last) outperforms joint adaptation at equal budget, because early stages condition the optimization landscape for later ones.
- **Problem:** All-at-once adaptation is the default; if shifts have a natural hierarchy (global statistics → spatial relations → content memory), matched staging should dominate and mis-ordered staging should underperform — a testable ordering theory.
- **Core Hypothesis (falsifiable):** Across shift types, matched-order staging beats joint and reverse-order adaptation at equal total steps, with the benefit proportional to how hierarchical the measured shift is (norm-explainable fraction first); reverse ordering shows characteristic transient degradation as later-stage groups fit unstabilized statistics.
- **Why Important:** A free scheduling improvement plus evidence about the causal structure of domain shift in transformer features.
- **Why Possibly Novel:** Parameter-group scheduling for DA is unexplored; existing staged methods stage data (curricula), not parameters.
- **Minimal Experiment:** Compare {joint, matched-order, reverse-order} adaptation on 6 shift scenarios at equal budgets; correlate staging benefit with measured shift hierarchy.
- **Main Risk:** Optimal stage lengths add hyperparameters; use validation-triggered transitions.
- **Research Cluster:** DA

### IDEA-C-0323 — Geometry-aware pseudo-label curricula: schedule by boundary complexity, not confidence
- **One-sentence idea:** Test whether ordering self-training pseudo-labels by class boundary complexity (simple-shape classes first) beats confidence-based curricula for segmentation UDA, because shape-simple classes yield geometrically reliable pseudo-labels that scaffold harder ones.
- **Problem:** Confidence-based curricula are miscalibrated exactly under domain shift; geometric reliability (simple shapes are hard to get wrong) is shift-invariant but unused as a curriculum signal.
- **Core Hypothesis (falsifiable):** Complexity-ordered self-training reaches higher final target mIoU than confidence-ordered at matched budgets across UDA benchmarks, with pseudo-label error audits confirming the mechanism (early-round error rates lower for shape-simple classes than confidence ranking predicts under shift).
- **Why Important:** Replaces a shift-fragile curriculum signal with a shift-robust one at zero cost, and adds to the geometry-first theme (IDEA-C-0081) a practical adaptation payoff.
- **Why Possibly Novel:** Curriculum self-training is standard; geometric complexity as the ordering variable with an error-audit mechanism check is new.
- **Minimal Experiment:** Run confidence- vs complexity- vs hybrid-ordered self-training on GTA→Cityscapes; audit per-round pseudo-label error by class; compare final performance.
- **Main Risk:** Complexity and frequency covary; include frequency-controlled orderings.
- **Research Cluster:** DA

### IDEA-C-0324 — Why Fourier domain adaptation works, and exactly when it must fail
- **One-sentence idea:** Validate the mechanism of Fourier-based DA (low-frequency amplitude swaps carry the ISP/illumination signature) and derive its predicted failure boundary — shifts living in phase or high-frequency structure — as a falsifiable applicability rule.
- **Problem:** FDA-style tricks are used as magic; a mechanism-validated applicability rule would prevent misapplication to shifts they cannot address (texture, geometry).
- **Core Hypothesis (falsifiable):** Across a shift taxonomy, FDA's gain correlates strongly with the fraction of inter-domain divergence residing in low-frequency amplitude spectra (measurable a priori); for constructed and natural shifts with amplitude-matched but phase/texture-divergent statistics, FDA yields near-zero or negative gains exactly as predicted — completing the method's operating envelope.
- **Why Important:** Converts a popular heuristic into a diagnosable tool with a one-measurement pre-check, exemplifying mechanism-first method characterization.
- **Why Possibly Novel:** FDA's empirical success is documented; the divergence-decomposition predictive rule with adversarial counterexamples is not.
- **Minimal Experiment:** Measure spectral divergence decompositions for 10 domain pairs; run FDA; fit gain vs low-frequency-amplitude fraction; construct and test the predicted failure cases.
- **Main Risk:** Spectral decompositions of natural-domain divergence are estimator-sensitive; use several estimators.
- **Research Cluster:** DA

### IDEA-C-0325 — A curvature-based safety criterion for test-time adaptation
- **One-sentence idea:** Derive and validate a criterion predicting when entropy-minimization TTA will collapse (all pixels one class), based on the curvature structure of the entropy landscape at adaptation start — a pre-flight check for the field's most fragile technique.
- **Problem:** TTA collapse is documented and feared; practitioners have no way to predict on which streams it will occur before it does.
- **Core Hypothesis (falsifiable):** Collapse occurrence across streams/corruptions is predicted with high accuracy by an initial-state measurement (alignment between entropy-gradient direction and class-collapse directions, computable in one backward pass), and constraining updates orthogonal to collapse directions prevents collapse while retaining most TTA gains — validating the geometric account.
- **Why Important:** Makes TTA deployable with a safety certificate, and explains collapse as geometry rather than bad luck (complementing IDEA-C-0009's calibration critique).
- **Why Possibly Novel:** TTA stabilization tricks exist; a predictive pre-adaptation criterion with a validated geometric mechanism is new.
- **Minimal Experiment:** Run TENT-style TTA across 50 stream configurations; measure the proposed criterion at start; evaluate prediction accuracy; test the orthogonal-update fix.
- **Main Risk:** Multiple collapse mechanisms may exist; classify failures and report criterion coverage.
- **Research Cluster:** DA

### IDEA-C-0326 — Does pretraining diversity make UDA obsolete? A scale-resolved audit
- **One-sentence idea:** Measure how the benefit of unsupervised domain adaptation methods shrinks as backbone pretraining diversity/scale grows, testing whether modern VFMs have absorbed the invariances UDA methods were built to create — and locating the residual niche where UDA still pays.
- **Problem:** UDA benchmarks froze on old backbones; whether the field's methods add anything on current VFMs is a live, unmeasured question steering research investment.
- **Core Hypothesis (falsifiable):** Across a backbone ladder, UDA-over-source-only gains shrink monotonically with pretraining scale on classic benchmarks, approaching zero for style-type shifts while remaining substantial for label-protocol and content shifts (per IDEA-C-0321's decomposition) — establishing that UDA's surviving value is exactly the components current pretraining cannot see.
- **Why Important:** A field-level course correction: either UDA is done (for its classic benchmarks) or its real remit is redefined — both outcomes actionable.
- **Why Possibly Novel:** Individual papers note strong baselines; the systematic scale-resolved obsolescence audit with component attribution is missing.
- **Minimal Experiment:** Run 3 representative UDA methods over 4 backbone scales on GTA→Cityscapes and 2 other pairs; plot gain vs scale per shift component.
- **Main Risk:** Method hyperparameters tuned for old backbones; re-tune honestly per scale.
- **Research Cluster:** DA

### IDEA-C-0327 — Source-free DA works because BN statistics are sufficient statistics of the shift
- **One-sentence idea:** Test the mechanism claim that source-free adaptation succeeds because normalization statistics encode a near-sufficient summary of style-type domain shifts — and that its documented failures occur exactly where the shift has components BN statistics cannot express.
- **Problem:** Source-free DA's surprising effectiveness lacks a mechanism, so its reliability envelope is unknown for safety-relevant deployment.
- **Core Hypothesis (falsifiable):** The fraction of a shift expressible as feature-wise mean/variance change (measurable with source and target unlabeled data) predicts source-free method gains across scenarios with high correlation; residual failures concentrate in shifts with high non-BN-expressible components (spatial correlation changes, semantic remaps) — the sufficiency account's direct test.
- **Why Important:** Deployment guidance for the most practical DA family (no source data needed), grounded in a checkable statistic.
- **Why Possibly Novel:** BN adaptation is old; the sufficiency framing with predictive validation across shift types is new.
- **Minimal Experiment:** Compute BN-expressible shift fractions for 12 scenarios; run 3 source-free methods; fit and validate the gain predictor.
- **Main Risk:** Modern backbones use LN, changing the statistics available; run the analysis per normalization family.
- **Research Cluster:** DA

### IDEA-C-0328 — Adaptation-rate matching for continuous drift: a tracking-theory bound
- **One-sentence idea:** Treat continuously-drifting domains (weather transitions, diurnal cycles) as a tracking problem and test whether the optimal adaptation rate follows the control-theoretic rule (adaptation bandwidth matched to drift bandwidth), with mismatch in either direction producing predictable failure signatures.
- **Problem:** Continual TTA methods pick update rates by grid search per benchmark; drifting deployments need a principled rate rule and diagnostics for rate mismatch.
- **Core Hypothesis (falsifiable):** On streams with controlled drift rates, accuracy as a function of adaptation rate is unimodal with the optimum tracking measured drift bandwidth (validated across drift types); under-adaptation shows lag signatures (errors correlated with drift derivative) and over-adaptation shows noise-amplification signatures (errors correlated with frame-to-frame variance) — enabling online rate diagnosis from error statistics alone (extending IDEA-C-0158's filtering view to the whole adaptation loop).
- **Why Important:** Converts continual-TTA tuning into measurement, with online diagnostics deployable in real systems.
- **Why Possibly Novel:** Continual TTA is benchmarked at fixed corruption schedules; the tracking-theoretic rate law and mismatch signatures are untested.
- **Minimal Experiment:** Build controlled-drift streams (interpolated corruption parameters); sweep adaptation rates for 2 methods; verify the matching rule and signature-based diagnosis.
- **Main Risk:** Real drift is multi-band; test with mixed-rate composite streams.
- **Research Cluster:** DA

### IDEA-C-0329 — Which classes get hurt by adaptation: an entanglement-based casualty predictor
- **One-sentence idea:** Test whether the classes that degrade under domain adaptation (negative transfer casualties) are predictable in advance from the entanglement of their features with the domain factors being aligned — enabling casualty forecasts before running adaptation.
- **Problem:** Adaptation helps on average while silently hurting specific classes; deployments discover casualties post hoc, and no predictive account exists.
- **Core Hypothesis (falsifiable):** Per-class degradation under standard UDA correlates strongly with a pre-computable entanglement score (how much the class's discriminative feature directions overlap with inter-domain shift directions); the predictor transfers across benchmarks, and entanglement-aware selective alignment (excluding high-risk directions) eliminates most casualties at small average cost.
- **Why Important:** Average-metric adaptation is unshippable in safety domains without per-class risk forecasts; this supplies them with a mechanism.
- **Why Possibly Novel:** Negative transfer is documented; a pre-hoc geometric casualty predictor with a mitigation is new.
- **Minimal Experiment:** Compute entanglement scores on 4 UDA pairs; run 3 methods; validate casualty predictions; test selective alignment.
- **Main Risk:** Feature-direction attribution per class is noisy; use multiple attribution estimators.
- **Research Cluster:** DA

### IDEA-C-0330 — Adversarial alignment fixes global statistics while scrambling boundary frequencies
- **One-sentence idea:** Analyze where in spatial-frequency space adversarial feature alignment operates, testing whether discriminator-based DA matches global/low-frequency statistics while actively distorting the high-frequency feature content that boundary precision requires.
- **Problem:** Adversarial DA improves mIoU but practitioners report boundary degradation; a frequency-resolved account would explain the trade-off and motivate frequency-scoped discriminators.
- **Core Hypothesis (falsifiable):** Feature-spectrum analysis before/after adversarial alignment shows convergence in low-frequency statistics and divergence (increased noise) in high-frequency bands, with boundary-F degradation proportional to the high-frequency distortion; band-limiting the discriminator (aligning only low frequencies) retains the mIoU gain while removing the boundary cost — confirming the mechanism and fixing it.
- **Why Important:** A mechanism-and-fix result for the field's most-used alignment strategy, protecting the boundary metrics dense applications care about.
- **Why Possibly Novel:** Adversarial DA critiques are about instability; the frequency-resolved distortion analysis is new.
- **Minimal Experiment:** Instrument feature spectra during adversarial UDA on GTA→Cityscapes; correlate high-frequency divergence with boundary metrics; implement band-limited discriminators.
- **Main Risk:** Feature-frequency analysis needs careful definition on token grids; use both spatial-FFT and graph-spectral variants.
- **Research Cluster:** DA

### IDEA-C-0331 — Cross-geography driving gaps are convention gaps, not appearance gaps
- **One-sentence idea:** Decompose cross-country driving-segmentation failure into appearance shift vs infrastructure-convention shift (lane markings, sign systems, road furniture taxonomies), testing whether convention adaptation — a discrete, enumerable mapping — dominates the continuous appearance component everyone models.
- **Problem:** Cross-geography transfer is attacked with appearance DA, though a car in Japan vs Germany differs less than the road grammar around it; the components have never been separated.
- **Core Hypothesis (falsifiable):** Error audits of cross-geography transfer show the majority of degradation concentrated in convention-defined classes (markings, signage, curb types) rather than appearance-defined ones (vehicles, pedestrians, vegetation); explicit convention mapping (small labeled dictionaries of per-country class realizations) recovers more accuracy than full unsupervised appearance adaptation at a fraction of the complexity.
- **Why Important:** Reframes a major autonomous-driving problem from statistical adaptation to knowledge-base engineering, with a cheap high-yield fix.
- **Why Possibly Novel:** Geographic robustness is benchmarked (e.g., multi-country datasets); the convention-vs-appearance decomposition with a dictionary-based remedy is new.
- **Minimal Experiment:** Cross-evaluate models between two country-distinct driving datasets; audit errors by class type; build convention dictionaries for the top classes; compare against UDA baselines.
- **Main Risk:** Class-type assignment (convention vs appearance) needs care; validate with human raters.
- **Research Cluster:** DA

### IDEA-C-0332 — Retinex-decomposed day-night adaptation: physics anchors beat statistics
- **One-sentence idea:** Test whether day-to-night adaptation improves when anchored on reflectance constancy (adapting illumination-related components while pinning estimated reflectance features) versus unconstrained statistical alignment — physics as the invariance certificate.
- **Problem:** Night adaptation methods align distributions blindly, discarding the physical fact that surface reflectance is illumination-invariant while only lighting changed — an unused anchor for what should not be adapted.
- **Core Hypothesis (falsifiable):** Decomposing features into illumination-sensitive and reflectance-like components (via retinex-guided probes), constraining adaptation to the illumination subspace outperforms unconstrained alignment on night benchmarks, with the advantage concentrated in classes whose night appearance is purely lighting-changed (vs classes with genuine content change like headlights) — validating the anchor precisely where physics says it applies.
- **Why Important:** Demonstrates physics-scoped adaptation — adapt what changed, pin what didn't — as a general DA design principle beyond day-night.
- **Why Possibly Novel:** Retinex preprocessing exists; feature-subspace-scoped adaptation with the physics-derived pinning constraint is new.
- **Minimal Experiment:** Identify illumination/reflectance feature subspaces via controlled relighting probes; run scoped vs unconstrained adaptation on Dark-Zurich; report class-stratified results.
- **Main Risk:** Feature-subspace decomposition is approximate; validate with synthetic relighting ground truth.
- **Research Cluster:** DA

### IDEA-C-0333 — The photorealism saturation point for synthetic-to-real transfer
- **One-sentence idea:** Measure the transfer-value curve of rendering photorealism (fixed content, swept rendering fidelity) for segmentation sim2real, testing whether returns saturate at a measurable fidelity level beyond which only content diversity matters — with the saturation point predictable from feature-space divergence.
- **Problem:** Synthetic-data budgets chase photorealism indefinitely; if transfer saturates early (backbone features become insensitive to residual rendering differences), the marginal renderer dollar is wasted (the driving-scene generalization of IDEA-C-0199's emissive-specific result).
- **Core Hypothesis (falsifiable):** Holding scene content fixed while sweeping rendering fidelity tiers, real-world transfer improves then plateaus at a fidelity level identifiable by the VFM feature divergence between synthetic and real falling below inter-camera real-world divergence — the natural "good enough" criterion — and content-diversity investment beyond that point dominates fidelity investment at equal cost.
- **Why Important:** A quantitative allocation rule for the synthetic-data industry, anchored to a measurable feature-space criterion rather than human perceptual judgment.
- **Why Possibly Novel:** Realism-vs-diversity debates are qualitative; the fixed-content fidelity sweep with a feature-divergence saturation criterion is new.
- **Minimal Experiment:** Render one scene set at 4 fidelity tiers (lighting/material/AA settings); train and evaluate transfer per tier; locate saturation; compare marginal fidelity vs diversity value at matched rendering cost.
- **Main Risk:** Fidelity is multi-dimensional; use factorial tiers over the main axes.
- **Research Cluster:** DA

### IDEA-C-0334 — Multi-domain training superposes domain codes instead of building invariance
- **One-sentence idea:** Test whether domain generalization from multi-domain training works by superposing domain-specific feature codes (with inference-time implicit domain inference) rather than by learning domain-invariant features — two mechanisms with opposite predictions for novel-domain behavior.
- **Problem:** Domain generalization is theorized as invariance learning, but models may instead store per-domain solutions and classify the test domain implicitly — which fails differently (catastrophically on truly novel domains, gracefully on interpolatable ones).
- **Core Hypothesis (falsifiable):** Probes on multi-domain-trained features decode training-domain identity accurately (superposition signature, incompatible with invariance); novel-domain performance correlates with the test domain's proximity to the training-domain convex hull (interpolation prediction) rather than being uniform (invariance prediction); and ablating domain-code directions degrades in-hull generalization while leaving out-of-hull unchanged — three converging discriminating tests.
- **Why Important:** Determines what multi-domain training actually buys and how to predict its failure on genuinely new domains — central to deployment claims of "domain generalized" models.
- **Why Possibly Novel:** Invariance-vs-ensemble accounts are debated theoretically; the three-test empirical discrimination on dense tasks is new.
- **Minimal Experiment:** Train on multi-domain segmentation suites; run domain-decoding probes, hull-proximity regression, and code-ablation tests on held-out domains.
- **Main Risk:** Hull proximity in feature space is metric-dependent; use several metrics for convergence.
- **Research Cluster:** DA

### IDEA-C-0335 — The corruption-to-domain transfer topology
- **One-sentence idea:** Map which synthetic-corruption robustness transfers to which natural domain shifts (a transfer topology), testing whether corruption families cluster into equivalence classes with natural shifts — so robustness engineering can target the right corruptions instead of all of them.
- **Problem:** Corruption augmentation is applied wholesale on the folk assumption that corruption robustness ≈ domain robustness; the actual transfer structure (which corruption buys which real-world robustness) is unmapped.
- **Core Hypothesis (falsifiable):** A transfer matrix (train-with-corruption-X → evaluate-on-natural-shift-Y) exhibits strong block structure: corruption families and natural shifts cluster into interpretable equivalence classes (e.g., blur family ↔ focus/motion domains; noise family ↔ sensor domains; but weather shifts unserved by any standard corruption) — with the unserved shifts identifying where new augmentation research is actually needed.
- **Why Important:** Converts robustness training from superstition to a lookup table, and identifies the natural shifts current corruption suites cannot buy.
- **Why Possibly Novel:** Corruption benchmarks and natural-shift benchmarks exist separately; the systematic transfer matrix between them for dense prediction is unbuilt.
- **Minimal Experiment:** Train per-corruption-family models on Cityscapes; evaluate each on ACDC conditions, cross-city, cross-sensor sets; cluster the transfer matrix; validate block predictions on held-out shifts.
- **Main Risk:** Matrix scale (families × shifts × seeds); use efficient shared-backbone protocols.
- **Research Cluster:** DA

## Cluster SSL — Weak/Semi/Self-Supervision (IDEA-C-0336 … IDEA-C-0350)

### IDEA-C-0336 — The mask-ratio/boundary-sensitivity curve of masked image modeling
- **One-sentence idea:** Map how MIM pretraining's mask ratio controls the boundary sensitivity of learned features, testing whether boundary-relevant information peaks at a different (lower) ratio than the semantic-transfer optimum — implying dense tasks need their own MIM recipes.
- **Problem:** MIM recipes are tuned for classification transfer; dense tasks inherit the same ratio (75%) without evidence it serves boundary perception.
- **Core Hypothesis (falsifiable):** Boundary-detection and thin-structure probes on MIM features peak at substantially lower mask ratios than classification probes (fine reconstruction requires local evidence that heavy masking destroys), with the two curves crossing at a measurable point — establishing a task-conditioned ratio choice and explaining part of the VFM thin-structure deficit (IDEA-C-0003).
- **Why Important:** One hyperparameter, re-examined per task family, could improve every dense-focused pretraining run at zero architectural cost.
- **Why Possibly Novel:** Ratio ablations report classification metrics; the boundary-probe-resolved curve is unmeasured.
- **Minimal Experiment:** Pretrain small MAEs at ratios {0.4..0.9}; probe boundary, thin-structure, and semantic transfer; locate the divergent optima.
- **Main Risk:** Small-scale pretraining generality; verify the trend at two scales.
- **Research Cluster:** SSL

### IDEA-C-0337 — Crop co-occurrence statistics predict segmentation emergence in contrastive models
- **One-sentence idea:** Test whether the emergence of object-segmentation structure in contrastive/self-distilled features is quantitatively predicted by the crop-pair co-occurrence statistics of pretraining augmentation (how often crops split objects), making "objectness for free" a measurable consequence of augmentation geometry.
- **Problem:** DINO-style features exhibit emergent object boundaries with no agreed mechanism; if crop statistics are the driver, emergence becomes controllable by augmentation design.
- **Core Hypothesis (falsifiable):** Varying crop-scale distributions in controlled pretraining changes emergent segmentation quality (unsupervised mask probes) in the direction predicted by the object-splitting statistics of the crops (computable from data object-size distributions); crop policies optimized to maximize predicted co-segmentation signal yield measurably better emergent masks at fixed compute.
- **Why Important:** Turns a celebrated emergent phenomenon into an engineered, predictable one — and explains cross-dataset variation in emergence quality.
- **Why Possibly Novel:** Emergent segmentation is described; the crop-statistics causal account with predictive control is untested.
- **Minimal Experiment:** Pretrain small DINO variants under crop-policy sweeps on datasets with different object-size statistics; measure emergent-mask quality; fit against the co-occurrence predictor.
- **Main Risk:** Other augmentations interact; hold all else fixed and ablate factorially.
- **Research Cluster:** SSL

### IDEA-C-0338 — Scribble information value is placement entropy, not length
- **One-sentence idea:** Test whether a scribble's supervision value is governed by the diversity/entropy of its placement (regions and boundary-distances covered) rather than its length, yielding an optimal scribble policy that halves annotation effort.
- **Problem:** Scribble guidelines say "draw more"; if a short high-entropy scribble equals a long redundant one, annotation-effort budgeting is systematically wasteful.
- **Core Hypothesis (falsifiable):** At matched length, high-placement-entropy scribbles (spanning texture variants and boundary distances within the object) yield trained-model accuracy exceeding low-entropy scribbles by large margins; accuracy-vs-length curves saturate at lengths predictable from the object's feature diversity — with a placement-guidance policy achieving target accuracy at a fraction of standard scribble effort (dovetailing with IDEA-C-0125's placement-bias finding).
- **Why Important:** Direct annotation-cost reduction with an information-theoretic account of what weak labels actually deliver.
- **Why Possibly Novel:** Scribble methods optimize learning from given scribbles; the scribble-design (policy) question is largely unaddressed.
- **Minimal Experiment:** Generate controlled scribble variants (entropy × length) from full masks; train scribble-supervised models per variant; fit the value model; validate with a small human-annotator study following the policy.
- **Main Risk:** Simulated scribbles differ from human ones; the human validation arm is essential.
- **Research Cluster:** SSL

### IDEA-C-0339 — The single-point sufficiency threshold at VFM scale
- **One-sentence idea:** Establish at what backbone scale single-point-per-instance supervision becomes sufficient to match full-mask supervision for segmentation training, testing whether the weak-to-full gap closes entirely as frozen features improve.
- **Problem:** Point supervision was weak with old backbones; if VFM features have made masks redundant (points + feature affinity recover them), full-mask annotation budgets are obsolete — a threshold worth dating precisely.
- **Core Hypothesis (falsifiable):** The point-vs-mask training gap shrinks monotonically with backbone scale, falling below annotation-noise-floor differences at an identifiable scale for common-object classes while persisting for boundary-complex classes (predictable via IDEA-C-0282's geometry axis) — yielding a class-resolved sufficiency map for annotation planning.
- **Why Important:** Potentially retires the field's most expensive annotation practice for a large class subset, with a principled residual list of where masks still pay.
- **Why Possibly Novel:** Point-supervision methods exist; the scale-resolved sufficiency-threshold measurement with class stratification is new.
- **Minimal Experiment:** Train point- vs mask-supervised heads across 4 backbone scales on COCO subsets; locate per-class-type sufficiency crossings against measured annotation-noise floors.
- **Main Risk:** Point-supervision method choice matters; use the strongest current recipe and one alternative.
- **Research Cluster:** SSL

### IDEA-C-0340 — Context-decoupled CAM: separating localization failure from context reliance
- **One-sentence idea:** Build a benchmark separating the two failure modes of class-activation-based weak supervision — genuine localization failure vs systematic activation on co-occurring context — and test whether modern VFM-based CAMs have shifted from the first to the second.
- **Problem:** CAM failures are lumped together; the fix differs completely (better attribution vs context decorrelation), and the mix has plausibly changed as backbones improved.
- **Core Hypothesis (falsifiable):** On context-controlled test sets (objects composited into atypical contexts with quality controls), older backbones' CAM errors are dominated by diffuse localization failure while VFM-era CAMs localize crisply but on the wrong (contextual) regions — a measurable failure-mode migration that dictates which research direction still matters for weakly-supervised segmentation.
- **Why Important:** Redirects an active subfield's effort to the failure mode that actually remains, with a reusable diagnostic benchmark.
- **Why Possibly Novel:** Context bias in CAMs is known; the failure-mode-decomposition benchmark with the era-migration hypothesis is new.
- **Minimal Experiment:** Construct context-swap evaluation sets; decompose CAM errors for 4 backbone generations; report the mode mixture per era.
- **Main Risk:** Compositing artifacts; reuse the control machinery of IDEA-C-0308.
- **Research Cluster:** SSL

### IDEA-C-0341 — Geometric consistency teaches equivariance; photometric teaches invariance — measure each
- **One-sentence idea:** Decompose semi-supervised consistency regularization's benefit into its equivariance-teaching (geometric transforms) and invariance-teaching (photometric transforms) components, testing whether their contributions are separable, additive, and task-predictable.
- **Problem:** Consistency recipes bundle transform families; without decomposition, recipe transfer across tasks is cargo cult (medical tasks may need different mixtures than driving).
- **Core Hypothesis (falsifiable):** Factorial consistency training (geometric-only, photometric-only, both) shows separable contributions whose relative size varies systematically with task properties (boundary-complexity favors geometric; appearance-variability favors photometric), with the two combining near-additively — enabling mixture prediction from task statistics measured upfront.
- **Why Important:** Converts the most-used semi-supervised ingredient into a task-tunable instrument with a measurement-based recipe.
- **Why Possibly Novel:** Augmentation ablations exist per paper; the equivariance/invariance decomposition framework with cross-task mixture prediction is new.
- **Minimal Experiment:** Run the factorial on 4 diverse segmentation tasks; fit contribution shares against task statistics; validate mixture predictions on 2 held-out tasks.
- **Main Risk:** Transform families overlap (crops change both geometry and statistics); design clean factor sets.
- **Research Cluster:** SSL

### IDEA-C-0342 — Motion as the better teacher: iso-compute video SSL vs image SSL for dense tasks
- **One-sentence idea:** Test whether self-supervised temporal correspondence learning from video produces better dense-prediction features than image SSL at strictly matched compute and data-collection cost — quantifying the widely-assumed but unmeasured value of motion as a segmentation teacher.
- **Problem:** The claim that motion teaches objectness underlies decades of theory, but modern comparisons confound architecture, data volume, and compute; a controlled iso-cost comparison is missing.
- **Core Hypothesis (falsifiable):** At matched total compute and matched frame counts, correspondence-based video SSL beats image SSL on segmentation/boundary probes (motion supplies grouping supervision images lack) while losing on semantic classification probes — a capability trade with the crossover measurable, settling how pretraining portfolios should mix video (and complementing IDEA-C-0025's opposite-direction finding).
- **Why Important:** Pretraining-data strategy for dense-first applications (robotics, medical video) hinges on this unmeasured exchange rate.
- **Why Possibly Novel:** Video SSL papers compare to image baselines loosely; the strict iso-cost, probe-decomposed comparison is absent.
- **Minimal Experiment:** Pretrain matched architectures on frames-as-images vs frames-with-correspondence objectives at equal compute; run the dense/semantic probe battery; replicate at two scales.
- **Main Risk:** Objective implementations differ in maturity; use best-established recipes for both.
- **Research Cluster:** SSL

### IDEA-C-0343 — Pseudo-label ensembling gains live almost entirely in the geometric ensemble
- **One-sentence idea:** Attribute the gains of multi-augmentation pseudo-label ensembling to its components, testing whether geometric-transform ensembling (flips/scales) accounts for nearly all benefit while photometric ensembling is deadweight — halving the compute of a ubiquitous pipeline step.
- **Problem:** Pseudo-label generation ensembles over many augmentations by convention; the per-component value has never been isolated, and the compute is charged on every unlabeled image.
- **Core Hypothesis (falsifiable):** Component-ablated ensembling shows geometric transforms contributing the large majority of pseudo-label quality gains (they correct equivariance errors that photometric ensembling cannot address), with photometric members adding within-noise value on most tasks — a stable attribution enabling a cheaper standard recipe.
- **Why Important:** Semi-supervised pipelines run at dataset scale; a validated half-cost recipe is an immediate field-wide saving.
- **Why Possibly Novel:** Ensembling is used, not analyzed; the component attribution for dense pseudo-labels is undone.
- **Minimal Experiment:** Generate pseudo-labels under component-ablated ensembles on 3 datasets; measure pseudo-label quality and downstream student accuracy per configuration.
- **Main Risk:** Photometric value may emerge under strong domain shift; include one shifted-unlabeled-pool condition.
- **Research Cluster:** SSL

### IDEA-C-0344 — The box-tightness assumption fails on articulated objects at measurable rates
- **One-sentence idea:** Audit the tightness assumption of box-supervised segmentation (every box edge touches the object) across object categories, testing whether articulated/thin objects violate it at rates that explain box-supervised methods' category-specific failures — and whether tightness-free formulations fix exactly those categories.
- **Problem:** Box-supervised losses (projection/tightness constraints) encode an assumption inherited from rigid objects; its violation statistics and downstream damage have never been measured.
- **Core Hypothesis (falsifiable):** Measured per-category tightness-violation rates (from mask+box datasets) predict box-supervised methods' per-category accuracy deficits with high correlation; replacing tightness constraints with violation-tolerant alternatives recovers accuracy specifically on high-violation categories, leaving others unchanged — the assumption audit becoming the method fix.
- **Why Important:** Box supervision is the most practical weak-label form; knowing exactly where its core assumption breaks converts unpredictable failures into a category-resolved reliability map.
- **Why Possibly Novel:** Box-supervised methods cite tightness as motivation; nobody has audited the assumption empirically or connected violations to failures.
- **Minimal Experiment:** Compute violation statistics on COCO (masks give ground truth); correlate with published box-supervised per-category results; implement and test a violation-tolerant loss.
- **Main Risk:** Violation metric definitions vary; report several (per-edge slack distributions).
- **Research Cluster:** SSL

### IDEA-C-0345 — Objective-difference predicts co-training value between VFM pairs
- **One-sentence idea:** Test whether the benefit of co-training two frozen VFMs (e.g., DINO+CLIP pseudo-labeling each other) is predictable from their pretraining-objective difference — measurable as error-decorrelation — making teacher-pair selection a computable decision.
- **Problem:** Co-training/mutual-learning setups pick model pairs by availability; the mechanism (complementary errors) suggests pair value is predictable, but no selection rule exists.
- **Core Hypothesis (falsifiable):** Across VFM pairs, semi-supervised co-training gains correlate strongly with pre-measured error decorrelation on a small probe set (and with objective-family difference as its cheap proxy), while pairs from the same objective family add little regardless of scale — a validated pair-selection rule replacing trial and error.
- **Why Important:** Multi-teacher pipelines are expensive; selecting pairs by measured complementarity buys the diversity benefit at minimum model count.
- **Why Possibly Novel:** Co-training theory requires view independence; the operational VFM-pair selection rule via error decorrelation is untested at foundation scale.
- **Minimal Experiment:** Measure pairwise error decorrelation among 6 frozen VFMs on probe segmentation; run co-training for high/low-decorrelation pairs; fit and validate the gain predictor.
- **Main Risk:** Decorrelation on probes may not match target domains; measure transfer of the predictor itself.
- **Research Cluster:** SSL

### IDEA-C-0346 — Where the gains live: semi-supervised improvements concentrate in mid-confidence pixels
- **One-sentence idea:** Test whether all semi-supervised segmentation methods, despite architectural diversity, deliver their gains in the same place — mid-confidence pixels near decision boundaries — implying the methods are interchangeable implementations of one mechanism and the metric to optimize is mid-band mass.
- **Problem:** New semi-supervised methods claim distinct mechanisms; if their gains are spatially/confidence-wise identical, the field is re-deriving one effect with different machinery.
- **Core Hypothesis (falsifiable):** Confidence-stratified gain profiles (improvement over supervised-only as a function of the supervised model's pixel confidence) collapse onto a single mid-band-peaked curve across 6 diverse methods, with method differences reducing to the curve's amplitude — supporting a unified account (label-propagation into the uncertain band) and a shared cheap progress metric.
- **Why Important:** Unification would deflate method proliferation and focus research on the actual limiting factor (extreme-band pixels no current method touches, connecting to IDEA-C-0094's dead zones).
- **Why Possibly Novel:** Methods are compared by aggregate mIoU; the gain-profile collapse hypothesis is untested.
- **Minimal Experiment:** Run 6 semi-supervised methods on shared splits; compute confidence-stratified gain profiles; test curve collapse statistically.
- **Main Risk:** Confidence must come from a fixed reference model; use the shared supervised baseline for stratification.
- **Research Cluster:** SSL

### IDEA-C-0347 — Parts before wholes: the emergence order of SSL feature structure
- **One-sentence idea:** Test whether self-supervised features become linearly separable for object parts before whole objects during pretraining (parts-first emergence), constraining theories of SSL and enabling early-stopped part-specialist encoders.
- **Problem:** What SSL learns first is unknown; emergence order would discriminate between competing accounts (co-occurrence statistics vs reconstruction demands) and has practical value (checkpoint selection by target granularity).
- **Core Hypothesis (falsifiable):** Probing checkpoints across pretraining, part-level segmentation probes reach a fixed fraction of their final accuracy consistently earlier than whole-object probes (in effective epochs), across SSL families — with the lag predicted by the co-occurrence account (parts co-occur within crops more reliably than wholes) and not by reconstruction accounts — a discriminating measurement between theories.
- **Why Important:** Emergence-order facts are the empirical bedrock theory needs, and mid-training checkpoints may be better part-feature sources than final ones — a free resource.
- **Why Possibly Novel:** Layer-wise feature analysis is common; the training-time emergence-order question for part/whole structure is unasked.
- **Minimal Experiment:** Probe dense part and object decodability across DINO/MAE pretraining checkpoints (public intermediate checkpoints or small reruns); compare emergence curves; test the co-occurrence prediction quantitatively.
- **Main Risk:** Part probe datasets are limited; use PartImageNet plus synthetic part hierarchies.
- **Research Cluster:** SSL

### IDEA-C-0348 — EMA teachers are low-pass filters with a computable optimal cutoff
- **One-sentence idea:** Formalize the EMA teacher in self/semi-supervised dense learning as a low-pass filter on function space and test whether its optimal decay is computable from measured student-update spectra — replacing the field's most sensitive magic number with a derived quantity.
- **Problem:** EMA decay values are copied between papers and break silently at different dataset scales/batch sizes; a signal-processing account would make the choice principled (deepening IDEA-C-0065's phase-transition finding into a design equation).
- **Core Hypothesis (falsifiable):** The student's function-space update sequence has a measurable power spectrum (signal at slow timescales, noise at fast ones); the accuracy-optimal EMA decay across settings matches the cutoff separating these bands (predictable from batch size, LR, and dataset size), with mismatch costs following the filter-theory prediction — validated across 3 frameworks.
- **Why Important:** One derived formula replacing per-setting grid search in dozens of popular methods, with transparent failure diagnostics.
- **Why Possibly Novel:** EMA is analyzed as averaging; the spectral matching rule with cross-setting validation is new.
- **Minimal Experiment:** Log function-space update spectra (on probe sets) across settings; sweep decay; test the cutoff-matching rule and its predicted scaling with batch size/LR.
- **Main Risk:** Function-space spectra estimated on probes may miss task-relevant bands; use multiple probe sets.
- **Research Cluster:** SSL

### IDEA-C-0349 — Redundancy-reduction SSL wins the small-batch dense regime
- **One-sentence idea:** Map the batch-size regime structure of SSL objectives for dense features, testing whether redundancy-reduction methods (Barlow/VICReg-family) dominate InfoNCE-family methods below a batch threshold — because contrastive negatives, not features, are what small batches starve.
- **Problem:** SSL objective choice ignores the compute reality that most labs pretrain at small batches; if the objective ranking flips with batch size, much guidance is backwards for the majority regime.
- **Core Hypothesis (falsifiable):** Dense-probe quality as a function of batch size shows InfoNCE-family methods degrading steeply below a threshold (negative-sample starvation, verifiable by negative-count interventions at fixed batch) while redundancy-reduction methods stay flat — with the crossover batch size stable across datasets and the mechanism confirmed by decoupling batch size from negative count via memory banks.
- **Why Important:** Regime-resolved guidance for every resource-constrained pretraining effort, with the mechanism (negatives vs statistics estimation) cleanly isolated.
- **Why Possibly Novel:** Batch-size sensitivity is known per method; the cross-family regime map with mechanism-isolating interventions for dense probes is new.
- **Minimal Experiment:** Pretrain 4 SSL objectives across batch sizes {32..2048} at fixed compute; run dense probes; perform the negative-count decoupling intervention.
- **Main Risk:** Per-method hyperparameters interact with batch size; re-tune LR per cell.
- **Research Cluster:** SSL

### IDEA-C-0350 — Free saliency from compression: JPEG bit allocation as a supervision prior
- **One-sentence idea:** Test whether the bit-allocation maps of standard image compression (bits spent per JPEG block, recoverable from any compressed file) constitute a free saliency/information prior usable to weight self-supervised losses and weak-label propagation — supervision mined from the codec.
- **Problem:** Every web image carries its encoder's implicit judgment of local information content, discarded on decode; SSL treats all regions equally while this free signal sits in the file.
- **Core Hypothesis (falsifiable):** Bits-per-block maps correlate meaningfully with object presence and boundary density (validated against segmentation ground truth); weighting SSL objectives or pseudo-label confidence by bit allocation improves dense-probe transfer at zero data cost, with gains proportional to the measured bit-object correlation per dataset — and the signal survives (with measurable degradation) recompression generations.
- **Why Important:** A genuinely free, universally available supervision channel with a clear mechanism (codecs allocate bits to unpredictable structure, which correlates with semantic content) — the anti-modular idea taken to its limit.
- **Why Possibly Novel:** Compression features appear in forensics; their use as an SSL weighting prior with correlation-conditioned gains is new.
- **Minimal Experiment:** Extract bit-allocation maps on COCO/OpenImages; measure object/boundary correlation; add bit-weighted loss variants to MAE/DINO small-scale pretraining; compare dense probes.
- **Main Risk:** Bit allocation also tracks non-semantic texture (grass, noise); the correlation-conditioned analysis quantifies exactly this limit.
- **Research Cluster:** SSL
---

# Appendix A — 20 Mutations (recombinations/variations of base ideas)

Each mutation names its parent idea(s) and states the delta. Mutations are offered as cheap extensions, not double-counted as base ideas.

**MUT-01 (from IDEA-C-0003 × IDEA-C-0336):** Thin-structure-targeted pretraining — after establishing the width-stratified scaling flatline (0003) and the mask-ratio/boundary curve (0336), pretrain one model with a low-ratio MIM phase appended to standard pretraining and test whether the thin-structure flatline lifts. Delta: from measurement to intervention.

**MUT-02 (from IDEA-C-0011 × IDEA-C-0175):** Curvature-preserving self-training — inject the BPE contour-vocabulary likelihood (0175) as a regularizer into the self-training loop shown to erode curvature (0011); test whether generation-wise spectral decay stops. Delta: pairs a diagnosed pathology with a shape-prior cure from another cluster.

**MUT-03 (from IDEA-C-0020):** Blue-noise everything-mode as a product — extend the aliasing analysis to content-adaptive prompt sampling (density proportional to local feature-gradient energy) and test recall at equal prompt budget. Delta: from artifact demonstration to optimal sampling design.

**MUT-04 (from IDEA-C-0035 × IDEA-C-0318):** Post-cutoff benchmark construction — build a small evergreen test set from verifiably post-training-cutoff imagery (new products, new species descriptions, recent construction) and re-evaluate zero-shot claims annually. Delta: turns two contamination audits into a standing instrument.

**MUT-05 (from IDEA-C-0040 × IDEA-C-0163):** Style-conditioned ground truth — release the two-style re-annotations (0040) as a dual-truth benchmark scored with the alignment metric (0163); methods must report per-style and style-marginalized numbers. Delta: from audit to benchmark artifact.

**MUT-06 (from IDEA-C-0061 × IDEA-C-0304):** Collapse-triggered rank growth — use the effective-rank collapse detector (0061) as the automatic trigger for greedy rank growth (0304), closing the loop into a self-sizing LoRA. Delta: two dynamics results composed into one adaptive algorithm.

**MUT-07 (from IDEA-C-0065 × IDEA-C-0348):** Unified EMA theory test — check whether the critical-decay phase boundary (0065) coincides with the spectral cutoff rule (0348) on the same runs; if they disagree, the discrepancy localizes missing theory. Delta: consistency test between two proposed laws.

**MUT-08 (from IDEA-C-0074):** Gradient-variance-aware batch construction generalized to class rarity — replace object-size stratification with rare-class stratification and test whether long-tail oscillations (IDEA-C-0092) shrink. Delta: same mechanism, second nuisance variable.

**MUT-09 (from IDEA-C-0096 × IDEA-C-0156):** Anisotropic deconvolution — combine the directional noise covariance (0096) with the annotator-PSF estimation (0156) into a single anisotropic label-deconvolution operator; test against each alone. Delta: merges two noise models into their natural joint form.

**MUT-10 (from IDEA-C-0102 × IDEA-C-0161):** Capture-recapture-weighted negatives — use mark-recapture missingness estimates (0161) to set the spatial loss-masking weights (0102) without any exhaustive re-annotation. Delta: replaces the expensive calibration step of one idea with the cheap estimator of another.

**MUT-11 (from IDEA-C-0131 × IDEA-C-0300):** Noise-corrected rank law — refit the rank-vs-N law (0131) after correcting for label-noise inflation (0300); test whether cross-dataset law scatter collapses. Delta: tests whether one confounder explains the residuals of another idea's law.

**MUT-12 (from IDEA-C-0150):** Router with model-quality drift — extend the perimeter-based annotation router to update its crossover threshold online as the assisting model improves from the collected labels; test total-cost savings over a static router. Delta: adds the feedback loop the static analysis ignores.

**MUT-13 (from IDEA-C-0169 × IDEA-C-0240):** Symmetry-group-conditioned self-similarity — use the detected wallpaper group (0169) to restrict the self-similarity comparison set (0240) to true group orbits; test false-positive reduction on quasi-periodic products. Delta: composition makes both zero-shot methods stricter.

**MUT-14 (from IDEA-C-0181 × IDEA-C-0197):** Density-field SAM head — add the threshold-conditioned decoder (0184) trained on unified smoke+haze density data (0197) to a frozen SAM; release as a general amorphous-matter prompting mode. Delta: three amorphous ideas composed into one deployable head.

**MUT-15 (from IDEA-C-0207 × IDEA-C-0226):** Symmetry-adjusted budget meter — correct the click-cost transferability meter (0207) with the organ-symmetry efficiency factor (0226); test improved budget-prediction accuracy on bilateral organs. Delta: one predictor refined by another's covariate.

**MUT-16 (from IDEA-C-0256 × IDEA-C-0278):** Bits-optimal query head — train the ask-for-next-click head (0278) to maximize the measured per-click information (0256) rather than expected IoU; test whether information-greedy queries generalize better across datasets. Delta: swaps the objective of one idea for the currency defined by another.

**MUT-17 (from IDEA-C-0265 × IDEA-C-0287):** Full PEFT dissociation matrix — run prompt-vs-adapter (0265) and attention-vs-MLP (0287) in one factorial on the same engineered shifts, yielding a 2×2 method-by-error-type selection table. Delta: unifies two dissociation designs into one experiment.

**MUT-18 (from IDEA-C-0290 × IDEA-C-0292):** Pre-merge orthogonalization — when the CKA test (0290) predicts merge failure, apply post-hoc subspace orthogonalization (0292's machinery) before averaging and test how much mergeability is rescued. Delta: one idea's diagnostic routes into another's intervention.

**MUT-19 (from IDEA-C-0335):** Corruption-portfolio optimization — given the transfer topology matrix, select the minimal corruption-training portfolio covering a deployment's expected natural shifts (set-cover over the matrix); test against train-on-everything at equal compute. Delta: from map to optimizer.

**MUT-20 (from IDEA-C-0350 × IDEA-C-0110):** Codec-informativeness as difficulty covariate — test whether bit-allocation maps (0350) predict the caption-informativeness gap (0110) per image, unifying the two free-signal ideas: regions where codecs spend bits but captions spend no words are exactly where VLM dense features should be weakest. Delta: cross-validates two independent data-side signals against each other.

---

# Appendix B — 10 Community-Assumption Challenges

Assumptions the field treats as settled, each with the specific batch ideas that operationalize the challenge.

**CH-01 — "Better mIoU means a better model."** Interior and boundary quality converge on different clocks (IDEA-C-0069/0093), leaderboard deltas fall below perceptual (0018) and statistical (0180, 0053) significance floors, and clinically-weighted metrics reorder models (0225). The scalar-metric monoculture is the field's largest unexamined assumption.

**CH-02 — "Ground truth is true."** Labels encode tool magnetism (0126), display resolution (0113), viewing windows (0123), annotation order (0100), atlas topology (0204), and fatigue (0099). The batch's DATA cluster collectively challenges the assumption that annotation is a noisy oracle rather than a biased instrument with estimable response functions (0156).

**CH-03 — "Scaling fixes perception."** Width-stratified flatlines (0003), attention collision (0016), inverse scaling under weak evidence (0007), and context hallucination growing with scale (0254) challenge the assumption that dense-perception failures are capacity problems rather than objective/architecture/data-format problems.

**CH-04 — "PEFT is a cheaper approximation of full fine-tuning."** The batch treats PEFT as a qualitatively different estimator: kernel-regime confinement (0296), prototype-local edits (0302), calibration geometry (0284), and invariance retention (0293) imply PEFT and full FT trade different capabilities, not just cost — "approximation" is the wrong frame.

**CH-05 — "Zero-shot benchmarks measure generalization to the unseen."** Pretraining contamination (0035), generator contamination (0318), vocabulary-frequency confounds (0045), and retrieval-not-induction in-context behavior (0277) jointly challenge whether any current "unseen" evaluation measures what it claims.

**CH-06 — "The interactive interface is stable."** Prompt semantics drift under fine-tuning (0030, 0276), resolution (0279), click order (0262), and grid quantization (0272). The community assumes the prompt contract is a fixed API; the batch treats it as an unversioned, drifting one.

**CH-07 — "Binary masks are the natural output format."** Amorphous matter (0181, 0184), sub-pixel structures (0191), infiltration gradients (0130), soft boundaries (0185), two-layer surfaces (0187), and tessellations (0198) all break the raster-binary format. The assumption that segmentation = per-pixel classification is a historical accident worth re-deriving.

**CH-08 — "Domain gap is an appearance problem."** Label-protocol components (0047, 0129, 0321), convention gaps (0331, 0236, 0243), and geometry/scale confounds (0120, 0232) argue that much of "domain adaptation" is ontology reconciliation misdiagnosed as distribution shift.

**CH-09 — "More unlabeled/synthetic/augmented data is monotonically good."** Cleanliness exchange rates (0122), negative data slices (0115), task-dependent synthetic sign flips (0024), duplication-inflated scaling (0105), and augmentation harm audits (0028) challenge data-volume monotonicity across all of its usual forms.

**CH-10 — "Evaluation is a solved logistics problem."** Simulator determinism (0046), resampling kernels (0127), inference protocols (0048), preprocessing divergence (0227), merge-state numerics (0303), and model-relatedness pseudo-replication (0159, 0180) argue that the field's comparison infrastructure carries error bars comparable to its claimed effect sizes.

---

# Appendix C — Near-Duplicate Notes

Internal near-duplicate risks flagged during generation, with the distinguishing deltas that justify keeping both members. Downstream selection should treat each group as a family and pick the strongest formulation.

1. **Rank laws family (IDEA-C-0131, 0145, 0282, 0289, 0300, 0301):** All concern LoRA-rank selection. Kept distinct because they isolate different independent variables: dataset size (0131), functional form (0145), mask geometry (0282), shift taxonomy (0289), label noise (0300), and universality of exponents (0301). A merged program would run them as one factorial; as ideas they are separable falsifiable claims.
2. **Two-clock family (IDEA-C-0069, 0093, 0146):** 0093 establishes the interior/boundary convergence lag; 0069 is its LR-schedule consequence; 0146 is its compute-saving exploitation. Ordered as phenomenon → mechanism-adjacent consequence → application; not duplicates but a dependency chain, flagged so selectors don't fund all three independently.
3. **Prompt-contract drift family (IDEA-C-0030, 0276, 0279):** Drift of prompt semantics under fine-tuning (0030: granularity semantics; 0276: causal prompt influence; 0279: resolution dependence). Distinct axes of the same contract-stability concept; 0030 and 0276 are closest — keep both only if the influence-metric and granularity-metric versions genuinely diverge in pilot data.
4. **Contamination family (IDEA-C-0035, 0049, 0318):** Pretraining-data contamination of evaluations, measured behaviorally (0035), by retrieval (0049), and through generators (0318). Same threat model, three channels; near-dup risk is low but they should share infrastructure.
5. **Simulator/protocol validity family (IDEA-C-0013, 0046, 0257):** All concern click-simulator realism. 0013 measures the human-simulator ranking gap, 0046 the determinism artifact, 0257 the policy-information gap with a guidance fix. 0013 and 0257 overlap most; distinguishing delta is ranking-validity (0013) vs interaction-optimization (0257).
6. **Norm-adaptation family (IDEA-C-0014, 0073, 0212, 0327):** Normalization statistics/affine parameters as the carrier of adaptation. 0014 is the debunking control, 0073 the trajectory-transplant attribution, 0212 the federated sufficiency claim, 0327 the source-free sufficiency mechanism. Same substrate, four claims; a single strong paper could absorb 0014+0073, so selectors should not count them as independent wins.
7. **Placement-dissociation family (IDEA-C-0265, 0281, 0287, 0294, 0223):** Which-component-fixes-which-error studies. Axes differ (prompt-vs-adapter; QK-vs-VO; attention-vs-MLP; single-layer; nuisance-depth), and MUT-17 proposes the merged factorial. Flagged as the batch's most compressible group.
8. **Source-vs-effect family (IDEA-C-0183, 0186, 0255):** Fire glow, shadows, wakes. Deliberate triptych establishing one principle in three domains; 0255 explicitly frames the unification. Keep at most two for execution; cite the third as replication target.
9. **Benchmark-statistics family (IDEA-C-0053, 0157, 0180):** Seed variance, IRT, mixed-effects. All are "evaluation inference done right"; they use different statistical machinery on different variance components and compose into one evaluation-reform toolkit rather than competing.
10. **Ambiguity-as-signal family (IDEA-C-0111, 0205, 0215, 0273):** Inter-rater disagreement as transferable signal (0111), universal noise model (0205), prompt-jitter surrogate (0215), and mode-count census (0273). 0111 and 0205 overlap in fitting disagreement predictors — the delta is transfer-across-datasets (0111) vs universal-functional-form (0205); merge if pilot data supports both simultaneously.
11. **Cross-batch caution:** Several CONF-cluster audits (0033, 0043, 0049, 0052, 0098) share the leakage-audit template applied to different leakage channels (scanner, spatial, duplication, patient, temporal). They are scientifically distinct (different mechanisms, different fields harmed) but methodologically siblings; an evaluation-focused generator may propose overlapping audits — dedupe against external batches on the channel, not the template.
12. **Self-training geometry pair (IDEA-C-0011, 0323):** Both use boundary/shape complexity in self-training contexts — 0011 diagnoses spectral erosion of iterated pseudo-labels; 0323 uses complexity as a curriculum signal. Different claims, shared measurement code.

*End of Batch C: 350 ideas (IDEA-C-0001…IDEA-C-0350), 20 mutations, 10 assumption challenges, 12 near-duplicate notes.*
