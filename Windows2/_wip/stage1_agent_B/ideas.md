# Windows2 Stage 1 — Agent B Idea Catalog

Agent: Cloud Sub-Agent B (VFM / multimodal / fine-tuning / PEFT angle clusters).
Total ideas: 345 (IDs W2-B-0001 … W2-B-0345).

Scientific ground rules applied: every idea states a falsifiable hypothesis and a
minimal experiment; no module-stacking / adapter-stacking / backbone-swap proposals;
no fabricated citations — uncertain prior-work claims are marked
"UNVERIFIED — needs lit search".

## Cluster index

- `vfm_failure` — 1. Vision Foundation Model failure modes (35 ideas)
- `vlm_dense_failure` — 2. Multimodal / VLM failure for dense prediction (35 ideas)
- `finetune_instability` — 3. Large-model fine-tuning instability (30 ideas)
- `peft_limits` — 4. Parameter-Efficient Fine-Tuning — when PEFT is wrong (35 ideas)
- `catastrophic_forgetting` — 5. Catastrophic forgetting when adapting VFMs to segmentation/detection (30 ideas)
- `prompt_sensitivity` — 6. Prompt learning / prompt sensitivity in VLMs and promptable segmenters (30 ideas)
- `representation_mismatch` — 7. Representation mismatch: global contrastive features vs pixel-level needs (30 ideas)
- `crossdomain_frozen_vs_tuned` — 8. Cross-domain transfer of frozen vs tuned foundation features (28 ideas)
- `synthetic_adaptation` — 9. Synthetic data for adapting foundation models (25 ideas)
- `medical_vfm_science` — 10. Medical vision foundation models — scientific questions (25 ideas)
- `language_geometry_alignment` — 11. Alignment between language supervision and dense visual geometry (25 ideas)
- `agentic_vision_hypotheses` — 12. Agents/tools around vision models with testable vision hypotheses (17 ideas)

---

## 1. Vision Foundation Model failure modes

Cluster key: `vfm_failure`

### W2-B-0001 — High-norm outlier tokens in DINOv2 spatially predict downstream segmentation error hotspots.

- **problem:** DINOv2-family ViTs produce high-norm "artifact" patch tokens (motivating register tokens), but nobody has mapped whether these artifacts spatially co-locate with dense-prediction failures.
- **core_hypothesis:** Pixel positions covered by high-norm outlier patch tokens have significantly higher segmentation error rates under frozen linear probing, and the norm magnitude is a monotone predictor of per-patch error.
- **why_important:** If true, a free, label-free error map exists inside every frozen ViT, usable for selective prediction and human review routing.
- **why_possibly_novel:** Register tokens were studied for global metrics and feature aesthetics; a quantitative per-pixel error-prediction link is unexplored (UNVERIFIED — needs lit search).
- **minimal_experiment:** Freeze DINOv2 ViT-L, linear-probe on ADE20K; compute per-patch token norm percentile vs per-patch probe error; report AUROC of norm as error predictor against entropy baseline.
- **main_risk:** Outlier tokens may be too sparse to matter for aggregate error, giving a true but practically weak signal.
- **cluster:** `vfm_failure`

### W2-B-0002 — CLIP's dense failure is a readout misalignment, not missing localization information.

- **problem:** CLIP patch features are widely believed to lack localization, but the evidence conflates "information absent" with "information not linearly accessible from the last layer".
- **core_hypothesis:** Nonlinear probes on intermediate CLIP layers recover boundary quality within 10% of DINOv2, implying the deficit is in accessibility, not content.
- **why_important:** Redirects a large body of work from re-pretraining toward cheap readout research and changes how we benchmark "dense quality" of VFMs.
- **why_possibly_novel:** Layerwise linear probing exists; a systematic accessibility-vs-content decomposition using probe capacity sweeps does not (UNVERIFIED — needs lit search).
- **minimal_experiment:** Sweep probe capacity (linear, 1-3 layer MLP, small attention readout) across all CLIP layers on Pascal Context; plot boundary F1 vs probe capacity; compare saturation point against DINOv2.
- **main_risk:** Heavy probes blur the line between "reading out" and "re-learning", requiring careful probe-capacity controls.
- **cluster:** `vfm_failure`

### W2-B-0003 — DINOv2 features are object-centric and systematically fail on "stuff" relative to "things".

- **problem:** Self-distillation pretraining with multi-crop centers on objects; the cost paid on amorphous stuff regions (sky, road, gravel) is uncharacterized.
- **core_hypothesis:** At matched pixel frequency, frozen DINOv2 probes show a larger error on stuff classes than supervised or MAE baselines, and the gap grows with crop-augmentation aggressiveness.
- **why_important:** Stuff dominates driving/remote-sensing scenes; a principled account of the thing-bias would guide model choice for those domains.
- **why_possibly_novel:** Thing/stuff splits are standard in benchmarks but not used as a lens on pretraining-objective bias for frozen VFMs.
- **minimal_experiment:** Frozen linear probes for DINOv2, MAE, CLIP on COCO-Stuff with per-class thing/stuff stratification and matched class-frequency reweighting; correlate gap with pretraining crop parameters where checkpoints exist.
- **main_risk:** Confounds between class frequency, region size, and stuff-ness require careful matching.
- **cluster:** `vfm_failure`

### W2-B-0004 — Contrastive pretraining suppresses high spatial frequencies, and the spectral gap predicts boundary F1 deficits.

- **problem:** We lack a measurable, model-intrinsic quantity that predicts which VFM will produce blurry boundaries before running any segmentation experiment.
- **core_hypothesis:** The ratio of high-frequency to low-frequency energy in patch-feature maps (computed on natural images) linearly predicts boundary F1 rank across VFM families.
- **why_important:** A zero-label spectral audit would let practitioners pick backbones for boundary-critical tasks without benchmark runs.
- **why_possibly_novel:** Frequency analyses exist for CNN robustness; a feature-spectrum-to-boundary-metric predictive law for frozen ViT VFMs is unexplored (UNVERIFIED — needs lit search).
- **minimal_experiment:** Compute 2D FFT energy profiles of feature maps for 10 VFMs on 500 images; rank-correlate spectral ratios with boundary F1 of frozen probes on Cityscapes and ADE20K.
- **main_risk:** Feature resolution differences across models may dominate spectra, requiring resolution-matched extraction.
- **cluster:** `vfm_failure`

### W2-B-0005 — Resolution extrapolation failure in VFMs is driven by attention entropy collapse, not positional-embedding interpolation.

- **problem:** VFMs degrade when evaluated above pretraining resolution; the standard fix (PE interpolation) assumes PEs are the bottleneck without causal evidence.
- **core_hypothesis:** At high resolution, specific attention heads collapse to near-zero entropy (single-token sinks), and patching only those heads (entropy regularization at inference) recovers more dense accuracy than PE fixes.
- **why_important:** High-res inference is essential for segmentation; identifying the true failure locus changes standard practice.
- **why_possibly_novel:** PE interpolation is folklore-standard; head-level entropy collapse as the causal factor at high resolution is a new decomposition (UNVERIFIED — needs lit search).
- **minimal_experiment:** Evaluate DINOv2/CLIP at 2-4x pretraining resolution; measure per-head attention entropy vs resolution; causally intervene per-head (temperature scaling) and compare recovery vs PE-only interpolation.
- **main_risk:** Entropy collapse may correlate with rather than cause failure; intervention experiments must be carefully controlled.
- **cluster:** `vfm_failure`

### W2-B-0006 — MAE and CLIP features are complementary layer-wise, not model-wise, contradicting the ensemble framing.

- **problem:** Fusion papers treat "geometric MAE" and "semantic CLIP" as complementary models, but complementarity may live at specific layer pairs, making whole-model fusion wasteful.
- **core_hypothesis:** The mutual-information overlap between MAE layer i and CLIP layer j features is highly non-uniform, and the best cross-model layer pair beats last-layer fusion at equal dimensionality on dense tasks.
- **why_important:** Reframes fusion research from architecture design to representation cartography, with immediate practical gains.
- **why_possibly_novel:** Layer-pair complementarity maps across pretraining objectives have not been published (UNVERIFIED — needs lit search).
- **minimal_experiment:** Compute CKA grids between all MAE/CLIP layer pairs; probe concatenations of selected pairs vs last-layer pairs on segmentation and depth at matched feature budget.
- **main_risk:** CKA overlap may not track task complementarity; needs task-grounded validation.
- **cluster:** `vfm_failure`

### W2-B-0007 — CLIP zero-shot classification succeeds partly through background context, and dense prediction exposes this reliance.

- **problem:** The same feature space yields strong image-level and weak pixel-level results; one unquantified explanation is that image-level scores exploit background correlations that dense tasks cannot.
- **core_hypothesis:** Foreground-masked CLIP classification drops substantially more than for supervised models, and per-class context reliance predicts that class's open-vocabulary segmentation deficit.
- **why_important:** Links two literatures (context bias, dense CLIP failure) with a single measurable mechanism.
- **why_possibly_novel:** Context reliance was studied for CNN classifiers; using it to predict per-class dense failure of VLMs is new.
- **minimal_experiment:** Classify foreground-only vs background-only crops with CLIP on COCO; regress per-class open-vocab segmentation IoU deficits on the measured context-reliance index.
- **main_risk:** Masking introduces its own distribution shift; needs inpainting controls.
- **cluster:** `vfm_failure`

### W2-B-0008 — SigLIP's sigmoid loss reduces patch-feature hubness relative to CLIP's softmax contrastive loss.

- **problem:** Nearest-neighbor "hub" features distort retrieval-style dense inference, but how the pretraining loss shape affects hubness of patch tokens is unknown.
- **core_hypothesis:** Softmax-contrastive global normalization induces stronger hubness in patch space than pairwise sigmoid loss; SigLIP patch features have measurably lower k-occurrence skew and better k-NN segmentation.
- **why_important:** Loss-geometry effects on dense inference would inform pretraining choices without new architectures.
- **why_possibly_novel:** Hubness is studied in retrieval; connecting pretraining loss functional form to patch-space hubness is unexplored (UNVERIFIED — needs lit search).
- **minimal_experiment:** Compute k-occurrence distributions of patch features for CLIP vs SigLIP at matched scale; run k-NN segmentation on ADE20K; correlate hubness skew with per-image errors.
- **main_risk:** CLIP and SigLIP differ in data too, confounding loss-shape attribution; use OpenCLIP retrainings where possible.
- **cluster:** `vfm_failure`

### W2-B-0009 — LVLM counting failures are decodable-information sufficient: the bottleneck is token pooling, not perception.

- **problem:** LVLMs fail at counting, but whether the visual evidence survives the vision-to-LLM projection is untested; blame is assigned to "perception" without decomposition.
- **core_hypothesis:** A linear probe on pre-projection encoder tokens predicts object counts far above LVLM output accuracy, while post-projection tokens lose count information proportional to pooling ratio.
- **why_important:** Localizes a famous failure to a specific interface, redirecting fixes from bigger encoders to projection design.
- **why_possibly_novel:** Layer-localization of counting information across the LVLM interface has not been systematically mapped (UNVERIFIED — needs lit search).
- **minimal_experiment:** Probe count regression at encoder output, post-projector, and mid-LLM layers for LLaVA-style models on counting benchmarks; plot information loss across the interface vs pooling factor.
- **main_risk:** Probes may exploit spurious size cues; control with density-matched stimuli.
- **cluster:** `vfm_failure`

### W2-B-0010 — Open-vocabulary segmentation errors snap to "hub" classes whose text embeddings dominate cosine neighborhoods.

- **problem:** Failure cases in open-vocab segmentation look systematic (same wrong classes recur) but are reported anecdotally, not mechanistically.
- **core_hypothesis:** A small set of class-text embeddings act as hubs in joint space; their k-occurrence rank predicts false-positive rates, and the effect strengthens as vocabulary size grows.
- **why_important:** Predictable error structure enables vocabulary curation and post-hoc de-hubbing calibration without retraining.
- **why_possibly_novel:** Hubness of the text side as a driver of dense false positives is unquantified.
- **minimal_experiment:** For OpenSeg-style frozen inference, compute text-embedding hubness across 1k-word vocabularies; regress per-class false-positive rates on hubness; test vocabulary-size scaling.
- **main_risk:** Hubness may be confounded with class frequency priors in pretraining text.
- **cluster:** `vfm_failure`
- **mutate_from:** W2-B-0008

### W2-B-0011 — VFM patch features are less equivariant to 90-degree rotations than to translations, creating orientation-anisotropic dense errors.

- **problem:** Dense tasks on aerial/medical images need rotation robustness, but equivariance audits of VFMs collapse all transformations into one robustness number.
- **core_hypothesis:** Frozen VFM segmentation error under image rotation is several times larger than under equal-pixel-displacement translation, and the anisotropy is stronger in language-aligned models than SSL models.
- **why_important:** Quantifies a transferability limit for the growing aerial/medical reuse of natural-image VFMs.
- **why_possibly_novel:** Transformation-decomposed equivariance audits tied to dense metrics per model family are missing.
- **minimal_experiment:** Measure feature equivariance error and probe mIoU under controlled rotations/translations for CLIP, DINOv2, MAE on DOTA (aerial) and natural scenes; compare anisotropy indices.
- **main_risk:** Square-pixel grid artifacts at non-90-degree angles complicate interpolation-free measurement.
- **cluster:** `vfm_failure`

### W2-B-0012 — Semantic and dense information travel through disjoint token routes inside VFMs, testable by targeted token ablation.

- **problem:** We do not know whether the same patch tokens carry classification-relevant and segmentation-relevant signal, or whether the two route separately.
- **core_hypothesis:** Ablating the top-attention tokens (CLS-attended) collapses zero-shot classification but leaves frozen-probe segmentation nearly intact, demonstrating separate routing.
- **why_important:** Route separation would explain why global metrics fail to predict dense quality and enable surgical model editing.
- **why_possibly_novel:** Token-ablation double dissociations between global and dense tasks are unexplored (UNVERIFIED — needs lit search).
- **minimal_experiment:** Rank tokens by CLS attention; ablate top-k at inference; measure classification vs frozen-seg degradation curves; repeat with random-token ablation control.
- **main_risk:** Attention rank is an imperfect proxy for information flow; complement with attribution methods.
- **cluster:** `vfm_failure`

### W2-B-0013 — Inverse scaling for small objects: larger VFMs get worse at segmenting objects below a patch-count threshold.

- **problem:** Scaling studies report aggregate mIoU, hiding the possibility that model scale reallocates capacity away from small structures.
- **core_hypothesis:** Across a model-size ladder at fixed patch size, IoU on objects smaller than ~4 patches decreases or stagnates with scale while large-object IoU rises, producing measurable inverse scaling.
- **why_important:** Small objects (distant pedestrians, lesions) are safety-critical; an inverse-scaling law would caution against naive scale-up.
- **why_possibly_novel:** Object-size-stratified scaling curves for frozen VFMs have not been published (UNVERIFIED — needs lit search).
- **minimal_experiment:** Frozen probes for ViT-S/B/L/g DINOv2 on Cityscapes with object-size-binned IoU; fit per-bin scaling exponents; verify with matched-resolution controls.
- **main_risk:** Small-object metrics are noisy; needs large eval sets and confidence intervals.
- **cluster:** `vfm_failure`

### W2-B-0014 — Feature-smoothing in newer DINO generations trades thin-structure segmentation for regional coherence.

- **problem:** Successive DINO releases report cleaner, smoother dense features, but smoothing plausibly erases wires, poles, and thin limbs; the tradeoff is unmeasured (DINOv3 training details UNVERIFIED — needs lit search).
- **core_hypothesis:** Later DINO versions improve region-interior metrics while regressing on a thin-structure benchmark (skeleton recall), revealing an unacknowledged tradeoff.
- **why_important:** Version upgrades are adopted blindly; a documented regression axis would inform deployment in infrastructure inspection and medical imaging.
- **why_possibly_novel:** Cross-version regression analysis on structure-specific metrics is absent from release comparisons.
- **minimal_experiment:** Build a thin-structure suite (wires, branches, catheters) with skeleton-recall metrics; evaluate frozen probes across DINO v1/v2/v3 checkpoints at matched resolution.
- **main_risk:** Version differences bundle data and recipe changes, limiting causal attribution.
- **cluster:** `vfm_failure`
- **mutate_from:** W2-B-0004

### W2-B-0015 — Zero-shot depth-like signals in VFMs come substantially from positional embeddings, not image content.

- **problem:** Emergent depth probing results on frozen VFMs may be inflated by the strong image-position prior of depth (bottom = near), which PEs encode for free.
- **core_hypothesis:** On position-decorrelated depth stimuli (shuffled crops, inverted scenes), frozen-probe depth accuracy of VFMs drops by a large fraction, and the drop correlates with PE information content.
- **why_important:** Corrects an over-claimed emergent ability and sharpens what "geometry in VFMs" means.
- **why_possibly_novel:** Position-prior deconfounding of emergent depth claims has not been performed systematically.
- **minimal_experiment:** Probe monocular depth on NYUv2 normally, then with vertically flipped and patch-shuffled variants plus PE-ablated features; decompose accuracy into content vs position terms.
- **main_risk:** Shuffling breaks scene statistics; needs naturalistic decorrelation stimuli (e.g., drone imagery with varied gravity direction).
- **cluster:** `vfm_failure`

### W2-B-0016 — Shape-vs-texture bias of a frozen VFM predicts its OOD segmentation transfer better than its ImageNet accuracy.

- **problem:** Backbone selection for OOD dense tasks uses ImageNet or in-distribution mIoU, which are known to be weak OOD predictors; a cheap intrinsic predictor is missing.
- **core_hypothesis:** Across 15+ VFMs, cue-conflict shape bias rank-correlates with corruption/synthetic-to-real segmentation transfer more strongly (rho gap > 0.2) than ImageNet linear-probe accuracy does.
- **why_important:** Provides a one-hour audit replacing days of transfer benchmarking for backbone selection.
- **why_possibly_novel:** Shape bias exists as a classification diagnostic; validating it as a dense-transfer predictor across the modern VFM zoo is new.
- **minimal_experiment:** Measure cue-conflict bias for a VFM zoo; evaluate frozen-probe transfer Cityscapes-to-ACDC and GTA-to-Cityscapes; compare rank correlations with baselines (accuracy, feature rank).
- **main_risk:** The relationship may be family-specific and fail across heterogeneous architectures.
- **cluster:** `vfm_failure`

### W2-B-0017 — The CLIP modality gap geometrically caps patch-text alignment quality for dense prediction.

- **problem:** Image and text embeddings occupy separate cones (modality gap); dense open-vocab methods inherit this geometry, but its causal contribution to dense failure is unquantified.
- **core_hypothesis:** Artificially closing the modality gap (post-hoc affine alignment on held-out pairs) improves patch-text segmentation more than it improves image-level retrieval, revealing dense tasks as the primary victim of the gap.
- **why_important:** Separates geometry-fixable failure from information-missing failure in open-vocab segmentation.
- **why_possibly_novel:** Modality-gap studies target retrieval/classification; a dense-task causal analysis is missing (UNVERIFIED — needs lit search).
- **minimal_experiment:** Estimate gap-closing transforms (mean shift, Procrustes) on COCO captions; apply to patch-text scoring; measure delta mIoU vs delta retrieval R@1 at matched transform budgets.
- **main_risk:** Post-hoc transforms may exploit supervision leakage; use disjoint estimation/eval vocabularies.
- **cluster:** `vfm_failure`

### W2-B-0018 — Patch-grid aliasing makes VFM performance on thin structures predictable from Nyquist-style analysis.

- **problem:** Failures on thin structures are treated as generic weakness rather than a signal-processing consequence of 14-16px patch sampling.
- **core_hypothesis:** Per-structure segmentation recall is a deterministic function of structure width divided by patch stride, with a sharp fall below one patch width, invariant across model scale.
- **why_important:** Gives deployment teams a closed-form feasibility check before choosing patch size or input resolution.
- **why_possibly_novel:** A quantitative aliasing law for ViT dense predictions has not been fitted or tested for invariance across models.
- **minimal_experiment:** Render synthetic scenes with parametric structure widths; measure recall vs width/stride ratio across patch sizes 8/14/16 and scales S/B/L; fit and cross-validate the law on real wire/pole datasets.
- **main_risk:** Learned deconvolution in probes may partially defeat aliasing, blurring the law.
- **cluster:** `vfm_failure`
- **mutate_from:** W2-B-0013

### W2-B-0019 — Pretraining color-augmentation invariance destroys information that color-critical dense tasks need.

- **problem:** VFMs inherit invariances (color jitter, grayscale) chosen for object recognition; tasks like stain-based tissue typing or fruit ripeness segmentation may need exactly the discarded information.
- **core_hypothesis:** The mutual information between frozen features and hue-defined labels is significantly lower in augmentation-heavy SSL models than supervised ones, and this deficit predicts per-task adaptation cost.
- **why_important:** Establishes "invariance audits" as a prerequisite for VFM reuse, especially in scientific imaging.
- **why_possibly_novel:** The invariance-utility conflict is discussed qualitatively; a quantified information audit across VFMs with dense-task validation is new.
- **minimal_experiment:** Build hue-discrimination dense tasks (synthetic and histopathology); measure frozen-probe accuracy across models with known augmentation recipes; regress deficits on augmentation strength.
- **main_risk:** Public checkpoints vary in many recipe dimensions simultaneously.
- **cluster:** `vfm_failure`

### W2-B-0020 — The "best layer" for dense readout varies per class, not per task, undermining single-layer feature extraction.

- **problem:** Practitioners pick one backbone layer per task; if the optimal layer differs by class (texture-defined vs shape-defined), any single choice is systematically suboptimal.
- **core_hypothesis:** Per-class optimal layers span at least a third of network depth within one segmentation task, and a class-agnostic oracle layer loses several mIoU points relative to a per-class-layer oracle.
- **why_important:** Motivates layer-distributed readouts with evidence rather than architecture intuition.
- **why_possibly_novel:** Layer-selection studies report task-level curves; class-level decomposition is unreported (UNVERIFIED — needs lit search).
- **minimal_experiment:** Train per-layer linear probes on ADE20K; compute per-class IoU by layer; quantify oracle gap between best-single-layer and best-per-class-layer readouts.
- **main_risk:** Per-class layer estimates are noisy for rare classes; needs bootstrap confidence intervals.
- **cluster:** `vfm_failure`

### W2-B-0021 — Frozen VFM dense accuracy degrades non-monotonically with corruption severity, revealing phase-transition-like failure.

- **problem:** Robustness curves are assumed smooth; if failures are abrupt (feature-space regime shifts), average-severity metrics hide catastrophic cliffs.
- **core_hypothesis:** For specific corruptions (fog, JPEG), frozen-probe mIoU exhibits a sharp cliff at a critical severity where feature statistics (norm, effective rank) also shift, and the cliff location is model-family-specific.
- **why_important:** Cliff locations, not average robustness, determine deployment safety margins.
- **why_possibly_novel:** Corruption studies report averages; identifying and predicting dense-accuracy phase transitions from feature statistics is new.
- **minimal_experiment:** Fine-grained severity sweeps (20 levels) on Cityscapes-C style data; track mIoU and feature statistics; test whether statistic shifts predict cliff onset within one severity step.
- **main_risk:** Cliffs may be benchmark artifacts of corruption implementations.
- **cluster:** `vfm_failure`

### W2-B-0022 — VFM patch features leak neighboring-object identity, and the "context bleed radius" predicts contour errors.

- **problem:** Each patch token aggregates context via attention; the spatial extent of identity leakage into neighboring tokens is unmeasured yet directly harms crisp boundaries.
- **core_hypothesis:** A probe can decode the neighboring object's class from patches up to a model-specific radius; this radius rank-orders models by boundary F1 inversely.
- **why_important:** Provides a mechanistic, measurable cause for boundary blur differences across VFMs.
- **why_possibly_novel:** Context aggregation is known qualitatively; a quantified bleed radius linked to boundary metrics is new.
- **minimal_experiment:** On two-object composite images, decode object-B identity from object-A patches vs distance; estimate bleed radius per model; correlate with boundary F1 on real benchmarks.
- **main_risk:** Composite images may not reflect natural context statistics.
- **cluster:** `vfm_failure`
- **mutate_from:** W2-B-0004

### W2-B-0023 — LVLMs have measurable "visual acuity" set by encoder input resolution, and it predicts task failures better than LLM scale.

- **problem:** LVLM failures are attributed vaguely to reasoning or perception; a psychophysics-style acuity measurement would separate optics from cognition.
- **core_hypothesis:** A Landolt-C-style acuity battery yields an acuity score per LVLM that predicts fine-grained task failures (small text, small objects, thin gaps) with high correlation, while LLM parameter count adds little.
- **why_important:** Gives the field a standardized eye-chart for multimodal models and a principled resolution-scaling argument.
- **why_possibly_novel:** Psychophysical acuity testing of LVLMs as a predictive covariate is new (UNVERIFIED — needs lit search).
- **minimal_experiment:** Build gap-resolution stimuli at controlled visual angles; test 10 LVLMs; regress downstream fine-grained benchmark errors on measured acuity vs model size covariates.
- **main_risk:** Prompt-format sensitivity may add variance requiring many-template averaging.
- **cluster:** `vfm_failure`
- **mutate_from:** W2-B-0009

### W2-B-0024 — Curated pretraining data gives DINOv2 hidden semantic supervision, measurable via rare-category dense performance.

- **problem:** DINOv2's retrieval-curated data pipeline may implicitly import ImageNet-like class structure, making "self-supervised" dense quality partly an artifact of curation.
- **core_hypothesis:** On categories absent from common curation seeds, DINOv2's dense advantage over uncurated-data SSL models shrinks substantially, exposing curation as a hidden supervisor.
- **why_important:** Clarifies what drives SSL dense quality — objective or data curation — steering future pretraining investments.
- **why_possibly_novel:** Curation-vs-objective attribution for dense tasks has not been isolated (UNVERIFIED — needs lit search).
- **minimal_experiment:** Assemble rare/long-tail category segmentation sets (e.g., unusual tools, non-Western artifacts); compare frozen-probe gaps DINOv2 vs web-random SSL checkpoints at matched scale.
- **main_risk:** Matched-scale uncurated checkpoints are scarce; may require training small-scale controls.
- **cluster:** `vfm_failure`

### W2-B-0025 — Emergent segmentation in ViT attention maps is epiphenomenal, not causally used by the model's own predictions.

- **problem:** Attention maps that "segment objects" are showcased as understanding, but whether the model's outputs causally depend on that structure is untested.
- **core_hypothesis:** Intervening on attention maps to destroy object-alignment (while preserving distributional statistics) barely changes model outputs, showing the maps are byproducts rather than functional segmentations.
- **why_important:** Deflates or validates a widely repeated interpretability claim with causal methodology.
- **why_possibly_novel:** Causal intervention on emergent segmentation structure has not been performed (UNVERIFIED — needs lit search).
- **minimal_experiment:** Swap or shuffle attention across object boundaries in selected heads of DINO/CLIP; measure output drift on classification and dense probes vs random-control interventions.
- **main_risk:** Interventions can push activations off-manifold; needs matched-statistics controls.
- **cluster:** `vfm_failure`

### W2-B-0026 — Language-aligned VFMs fail hardest on image regions that humans find hard to name.

- **problem:** Dense failure analyses use class labels, ignoring that some visual content is linguistically unencodable; language-supervised features may be blind exactly there.
- **core_hypothesis:** Per-region open-vocab segmentation error correlates with psycholinguistic nameability norms (naming latency/agreement), and the correlation is much weaker for SSL models.
- **why_important:** Connects vision failures to language structure, predicting where CLIP-like supervision fundamentally cannot reach.
- **why_possibly_novel:** Psycholinguistic nameability as a predictor of dense model error is unexplored.
- **minimal_experiment:** Collect nameability ratings for region crops (crowdsourced, existing naming norms); correlate with per-region errors of CLIP-based vs DINO-based frozen segmenters.
- **main_risk:** Nameability confounds with visual complexity; include complexity covariates.
- **cluster:** `vfm_failure`

### W2-B-0027 — Patch-token norm is a better free uncertainty signal for frozen dense predictions than softmax entropy.

- **problem:** Uncertainty for frozen-VFM dense pipelines is an afterthought; probe entropy is used by default without validating alternatives intrinsic to the backbone.
- **core_hypothesis:** Per-patch feature norm (or norm deviation from the image median) achieves higher error-detection AUROC than probe entropy on OOD inputs, because norms shift before probe logits do.
- **why_important:** Free, backbone-intrinsic uncertainty would improve selective prediction in safety-critical dense applications.
- **why_possibly_novel:** Feature-norm uncertainty is studied for classification OOD; per-patch dense validation across VFMs is missing.
- **minimal_experiment:** On Cityscapes-to-ACDC shift, compare error-detection AUROC of patch norm, probe entropy, and ensemble disagreement for frozen probes over multiple backbones.
- **main_risk:** Norm behavior may invert across model families, requiring per-family calibration.
- **cluster:** `vfm_failure`
- **mutate_from:** W2-B-0001

### W2-B-0028 — The object-scale histogram of pretraining data imprints a scale prior measurable as scale-dependent dense errors.

- **problem:** VFMs are assumed scale-general, yet pretraining images have characteristic object-size distributions that may set a prior on recognizable scales.
- **core_hypothesis:** Frozen-probe IoU as a function of object scale peaks where the pretraining scale histogram peaks, and models trained on different data (web vs curated) show shifted peaks.
- **why_important:** Explains cross-dataset transfer asymmetries and motivates scale-targeted augmentation at adaptation time.
- **why_possibly_novel:** Direct linkage of pretraining scale statistics to downstream scale-response curves is untested.
- **minimal_experiment:** Estimate object-scale histograms of pretraining corpora via detector pseudo-labels on samples; measure scale-binned IoU for corresponding models; test peak alignment across 4+ models.
- **main_risk:** Pretraining data access is limited for some models; may need proxy corpora.
- **cluster:** `vfm_failure`

### W2-B-0029 — Multi-crop augmentation creates a center-periphery quality gradient in DINO-family dense features.

- **problem:** Multi-crop training statistically over-trains central image regions; a systematic spatial quality gradient in patch features would bias dense predictions toward image centers.
- **core_hypothesis:** Frozen-probe error increases with distance from image center for DINO-family models beyond what content statistics explain, and the gradient magnitude tracks the multi-crop recipe strength.
- **why_important:** Spatial bias matters for panoramic, aerial, and surveillance imagery where content is not center-composed.
- **why_possibly_novel:** Center-bias audits of patch features attributable to augmentation recipes are unreported.
- **minimal_experiment:** Evaluate per-position error maps on spatially-uniform datasets (aerial tiles); compare DINO variants vs MAE; decorrelate content by tile shuffling.
- **main_risk:** Photographer center bias in pretraining data confounds recipe attribution.
- **cluster:** `vfm_failure`
- **mutate_from:** W2-B-0003

### W2-B-0030 — CLIP+DINOv2 fusion gains for dense tasks are largely explained by effective-resolution differences, not representational complementarity.

- **problem:** Fusion works cite complementary "semantic + spatial" information, but the models are typically run at different effective resolutions, confounding the claim.
- **core_hypothesis:** When feature-map resolution and receptive statistics are strictly matched, fusion gains drop by more than half, revealing resolution as the hidden factor.
- **why_important:** Prevents the community from over-investing in fusion architectures when resolution handling is the real lever.
- **why_possibly_novel:** Resolution-controlled fusion ablations are absent from fusion literature (UNVERIFIED — needs lit search).
- **minimal_experiment:** Reproduce a standard CLIP+DINO fusion probe; re-run with resolution-matched extraction and upsampling-matched pipelines; decompose gains into resolution vs representation terms.
- **main_risk:** Perfect matching is hard; partial matching may leave residual confounds.
- **cluster:** `vfm_failure`
- **mutate_from:** W2-B-0006

### W2-B-0031 — Removing register tokens at inference redistributes global information and can improve dense predictions while hurting classification.

- **problem:** Registers absorb global aggregation; whether their inference-time removal reallocates capacity toward spatial fidelity is an open causal question.
- **core_hypothesis:** Masking register tokens at inference in register-trained ViTs degrades classification mildly but improves patch-feature purity and frozen-probe boundary metrics on some tasks.
- **why_important:** A zero-cost inference switch trading global for dense performance would be practically useful and mechanistically revealing.
- **why_possibly_novel:** Inference-time register ablation with dense-vs-global dissociation has not been reported.
- **minimal_experiment:** For register-equipped DINOv2 checkpoints, ablate registers at inference; measure classification, patch-purity metrics, and probe mIoU/boundary F1 across tasks.
- **main_risk:** Effects may be negligible because information already routed during training.
- **cluster:** `vfm_failure`
- **mutate_from:** W2-B-0001

### W2-B-0032 — CLIP patch features are largely order-invariant, exhibiting bag-of-patches behavior at the dense level.

- **problem:** CLIP's bag-of-words behavior is documented for text-image matching; whether its visual patch representation is similarly insensitive to spatial arrangement is untested.
- **core_hypothesis:** Shuffling patch positions (with PE kept consistent) changes CLIP image embeddings far less than DINOv2 embeddings change, and the invariance predicts relational-reasoning failures.
- **why_important:** Grounds compositional failures of CLIP-based systems in a measurable representational property.
- **why_possibly_novel:** Patch-permutation sensitivity as a cross-model dense diagnostic is new.
- **minimal_experiment:** Measure embedding drift under controlled patch permutations across models; correlate drift magnitude with relational benchmark accuracy (spatial relation probes).
- **main_risk:** PE handling choices during shuffling materially affect conclusions; needs multiple protocols.
- **cluster:** `vfm_failure`
- **mutate_from:** W2-B-0007

### W2-B-0033 — Pretraining-seed variance on dense metrics exceeds cross-architecture differences claimed in VFM comparison papers.

- **problem:** VFM comparisons rest on single pretraining runs; if seed-to-seed dense variance is large, many published rankings are statistically unfounded.
- **core_hypothesis:** For small-to-mid scale SSL pretraining, across-seed standard deviation of frozen-probe mIoU is comparable to typical published between-model gaps (1-2 points), making many claims non-significant.
- **why_important:** Forces methodological reform (multi-seed reporting) in VFM benchmarking.
- **why_possibly_novel:** Dense-task seed-variance quantification for SSL pretraining is absent (UNVERIFIED — needs lit search; costly, feasible at ViT-S scale).
- **minimal_experiment:** Pretrain 5 seeds of ViT-S DINO and MAE on ImageNet-100 scale; measure frozen-probe mIoU spread; compare against published between-method gaps at similar scale.
- **main_risk:** Small-scale variance may not extrapolate to flagship scales.
- **cluster:** `vfm_failure`

### W2-B-0034 — VFMs are more brittle to global illumination shifts than to equal-energy local noise, despite heavy augmentation.

- **problem:** Robustness suites emphasize local corruptions; global photometric shifts (exposure, white balance) are common in deployment yet under-benchmarked for dense tasks.
- **core_hypothesis:** At matched feature-space perturbation magnitude, global illumination shifts cause larger frozen-probe dense errors than local noise, because augmentations trained invariance to the wrong perturbation family.
- **why_important:** Redirects robustness engineering toward the perturbations that actually break deployed dense systems.
- **why_possibly_novel:** Energy-matched global-vs-local perturbation comparisons for VFM dense output are new.
- **minimal_experiment:** Construct exposure/white-balance/gamma shifts and pixel-noise variants matched by induced feature drift; compare probe mIoU losses across VFM families.
- **main_risk:** Matching perturbation magnitude fairly across families is nontrivial.
- **cluster:** `vfm_failure`
- **mutate_from:** W2-B-0019

### W2-B-0035 — Token-merging inference accelerators destroy dense information predictably from pre-merge token similarity structure.

- **problem:** Token merging/pruning is tuned on classification, then reused for dense pipelines; the dense cost is unquantified and likely structured, not random.
- **core_hypothesis:** Dense-task degradation under token merging is predicted (R2 > 0.7) by the fraction of merged token pairs that straddle ground-truth object boundaries, enabling a label-free merge-safety score.
- **why_important:** Enables dense-safe acceleration policies without task labels.
- **why_possibly_novel:** A predictive theory of merging damage for dense tasks, rather than empirical tuning, is new.
- **minimal_experiment:** Apply ToMe-style merging at varying ratios to frozen VFMs; regress probe mIoU loss on boundary-straddling merge fraction; validate the score across datasets.
- **main_risk:** Probes may adapt around merging if retrained, muddying the frozen-setting conclusion.
- **cluster:** `vfm_failure`

---

## 2. Multimodal / VLM failure for dense prediction

Cluster key: `vlm_dense_failure`

### W2-B-0036 — Left-right relations in referring segmentation are answered from language priors, not visual evidence.

- **problem:** Referring segmentation models score well on average, but spatial-relation clauses ("left of the chair") may be resolved by object co-occurrence priors rather than geometry.
- **core_hypothesis:** On mirror-flipped image pairs with fixed expressions, referring segmentation models pick the same (now wrong) region far above chance, quantifying prior-driven answering.
- **why_important:** Spatial language is central to human-robot interaction; prior-driven grounding is a silent safety failure.
- **why_possibly_novel:** Flip-consistency as a targeted audit of spatial-clause utilization is not standard in referring-seg evaluation (UNVERIFIED — needs lit search).
- **minimal_experiment:** Build flipped-pair evaluation from RefCOCO with relation-bearing expressions; report flip-consistency error decomposed by relation type across 6 models.
- **main_risk:** Some expressions remain valid under flips; requires clause-aware filtering.
- **cluster:** `vlm_dense_failure`

### W2-B-0037 — Class-name frequency in web text predicts open-vocabulary segmentation IoU better than visual difficulty does.

- **problem:** Open-vocab benchmarks interpret per-class scores as visual capability, ignoring that text-side exposure may dominate what can be segmented.
- **core_hypothesis:** Log word-frequency of class names in pretraining-like corpora explains more per-class IoU variance than visual factors (size, texture complexity, boundary length) combined.
- **why_important:** Reframes open-vocab progress: gains may reflect vocabulary coverage, not dense vision, changing how benchmarks should be stratified.
- **why_possibly_novel:** A variance-decomposition of open-vocab dense performance into linguistic vs visual factors is missing.
- **minimal_experiment:** Regress per-class IoU of 5 open-vocab segmenters on corpus frequency plus visual covariates over 300+ classes; report partial R2 for each factor family.
- **main_risk:** Frequency correlates with image-side frequency too; needs image-frequency controls.
- **cluster:** `vlm_dense_failure`

### W2-B-0038 — Referring segmentation exhibits negation blindness that scales with model confidence, not competence.

- **problem:** Expressions like "the cup not on the table" require excluding a salient match; VLM-based segmenters may systematically segment the negated object.
- **core_hypothesis:** Negated expressions produce the anti-target mask in a majority of cases, and confidence on these errors is as high as on correct positives, making them undetectable by thresholding.
- **why_important:** Negation is common in interactive correction ("no, not that one"); blindness breaks the core interactive loop.
- **why_possibly_novel:** Negation is studied in VQA; a controlled dense-prediction negation battery with confidence analysis is new.
- **minimal_experiment:** Construct minimal-pair negation expressions on COCO scenes; measure anti-target rate and confidence distributions across referring-seg models.
- **main_risk:** Synthetic negations may be linguistically unnatural; validate with human phrasing collection.
- **cluster:** `vlm_dense_failure`

### W2-B-0039 — Hallucinated grounding boxes for absent objects are drawn from a learnable co-occurrence prior, making them predictable.

- **problem:** When asked to ground absent objects, VLMs emit confident boxes; if placements follow scene co-occurrence statistics, hallucinations are systematic rather than random noise.
- **core_hypothesis:** A simple scene-conditioned placement model (trained on real co-occurrence statistics) predicts hallucinated box locations significantly above chance, demonstrating prior-sampling behavior.
- **why_important:** Predictable hallucination enables detection and filtering without model access, and clarifies the generative mechanism of grounding errors.
- **why_possibly_novel:** Modeling the distribution of hallucinated dense outputs, rather than just their rate, is unexplored.
- **minimal_experiment:** Query grounding VLMs for absent objects on COCO; fit placement predictor from co-occurrence data; evaluate predictive likelihood vs uniform and saliency baselines.
- **main_risk:** Different architectures may hallucinate via different mechanisms, fragmenting the result.
- **cluster:** `vlm_dense_failure`

### W2-B-0040 — LVLM counting failure is an enumeration-binding deficit: instances are detected internally but cannot be enumerated.

- **problem:** Counting errors are cited as perception failure, but the model may represent each instance while lacking a mechanism to enumerate distinct bindings.
- **core_hypothesis:** Instance-presence probes on visual tokens find all instances even when the model miscounts, and errors grow with instance similarity (binding interference), not instance size.
- **why_important:** Locates a famous failure at the binding level, informing whether fixes need better encoders or better readout mechanisms.
- **why_possibly_novel:** Dissociating detection from enumeration inside LVLMs with interference-controlled stimuli is new.
- **minimal_experiment:** Controlled arrays varying count, similarity, and spacing; probe token-level instance presence; compare probe-derived counts vs generated counts across conditions.
- **main_risk:** Probing methodology may overcount via texture cues; needs careful stimulus control.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0009

### W2-B-0041 — Spatial information is present in early LLM layers of LVLMs but overwritten by language priors in later layers.

- **problem:** Where spatial grounding dies inside an LVLM is unknown: at the projector, early fusion, or late decoding.
- **core_hypothesis:** Linear probes for target location peak at early-to-mid LLM layers and decline toward output layers, and the decline is steeper for images contradicting co-occurrence priors.
- **why_important:** Identifies the layer range where interventions (steering, early-exit readout) could rescue grounding.
- **why_possibly_novel:** Layerwise spatial-information tracking through the language decoder with prior-congruency manipulation is unexplored (UNVERIFIED — needs lit search).
- **minimal_experiment:** Probe object-position decoding across all LLM layers of LLaVA-class models on congruent vs incongruent scenes; localize the information peak and prior-overwrite point.
- **main_risk:** Probe accuracy conflates information presence with linear accessibility.
- **cluster:** `vlm_dense_failure`

### W2-B-0042 — Synonym instability: open-vocab segmentation varies more across synonyms of one class than across model generations.

- **problem:** Benchmarks fix one name per class, hiding that "couch/sofa" or "spectacles/glasses" may produce wildly different masks.
- **core_hypothesis:** The IoU variance across a synonym set for a fixed class exceeds the IoU difference between successive model releases, making synonym choice a bigger factor than model choice.
- **why_important:** Reveals that reported open-vocab progress is smaller than vocabulary-luck effects; motivates synonym-marginalized evaluation.
- **why_possibly_novel:** Synonym-marginalized dense evaluation protocols do not exist (UNVERIFIED — needs lit search).
- **minimal_experiment:** Build synonym sets via WordNet plus human filtering; evaluate 6 models on synonym-swept open-vocab segmentation; compare within-class synonym variance to between-model variance.
- **main_risk:** Some synonyms genuinely differ in extension (sofa vs couch regionally); needs extension-matched sets.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0037

### W2-B-0043 — Novel attribute-object combinations snap to prototypes: "green couch" masks lean toward prototypical couch colors.

- **problem:** Compositional grounding requires binding attributes to objects; models may instead retrieve prototype instances matching the noun and ignore the modifier.
- **core_hypothesis:** On scenes with two same-noun objects differing in attribute, referring accuracy drops toward chance as attribute-noun combination frequency in web text decreases.
- **why_important:** Quantifies compositional generalization for dense outputs, where failure is spatially observable rather than inferred from answers.
- **why_possibly_novel:** Frequency-stratified compositional dense evaluation ties failures to pretraining statistics rather than generic "compositionality".
- **minimal_experiment:** Generate controlled two-object scenes (rendered plus real curated); vary attribute-noun frequency; measure accuracy vs frequency curve per model.
- **main_risk:** Render-to-real gap; validate a subset on real photographs.
- **cluster:** `vlm_dense_failure`

### W2-B-0044 — Polysemous class names reveal whether open-vocab segmenters use scene context or fail to disambiguate at all.

- **problem:** Words like "bat", "crane", "mouse" have multiple visual extensions; how dense models resolve polysemy is unknown and unbenchmarked.
- **core_hypothesis:** Open-vocab segmenters resolve polysemy by scene context far below LVLM text-side disambiguation ability, showing the dense pathway bypasses contextual sense selection.
- **why_important:** Sense errors produce confident wrong masks in exactly the scenes where users need trust; also isolates where disambiguation lives architecturally.
- **why_possibly_novel:** A polysemy battery for dense prediction does not exist.
- **minimal_experiment:** Curate scenes containing one sense of 40 polysemous words; measure sense-correct mask rate vs an LVLM asked textually which sense is present.
- **main_risk:** Sense frequency imbalance may make some items trivial; balance via curation.
- **cluster:** `vlm_dense_failure`

### W2-B-0045 — Referring models ignore relational clauses: clause-ablation changes masks far less than it changes meaning.

- **problem:** Long referring expressions look compositional, but models may use only head nouns plus salience, making clause processing decorative.
- **core_hypothesis:** Deleting restrictive clauses ("that is under the lamp") changes the predicted mask in fewer than half the cases where it changes the correct target, yielding a low clause-utilization score.
- **why_important:** Provides a per-model "clause utilization" metric exposing shortcut reliance invisible to IoU.
- **why_possibly_novel:** Systematic ablation-based utilization metrics for referring dense models are new (UNVERIFIED — needs lit search).
- **minimal_experiment:** For RefCOCOg expressions, programmatically ablate clauses; measure mask-change rate conditioned on target-change necessity; rank models by utilization.
- **main_risk:** Clause parsing errors introduce noise; use human-validated subsets.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0036

### W2-B-0046 — Under semantics-vs-edges conflict, VLM segmenters anchor masks to color edges, revealing edge-based shortcut inference.

- **problem:** When true object boundaries lack contrast (camouflage) or strong non-boundary edges exist (shadows, patterns), where do VLM-derived masks fall?
- **core_hypothesis:** Mask boundaries systematically follow high-contrast photometric edges over semantic boundaries, and this bias is stronger in VLM-based than fully-supervised segmenters.
- **why_important:** Predicts failure classes (camouflage, shadows, occlusion boundaries) and quantifies how much dense "understanding" is edge-snapping.
- **why_possibly_novel:** Edge-vs-semantics conflict batteries for language-driven segmenters are unexplored.
- **minimal_experiment:** Assemble camouflage and shadow-heavy scenes with ground truth; measure boundary attachment rates to photometric vs semantic edges across model classes.
- **main_risk:** Supervised baselines trained on similar data may share the bias, weakening the contrast.
- **cluster:** `vlm_dense_failure`

### W2-B-0047 — Open-vocab segmentation misses are dominated by the proposal stage for stuff classes and the classification stage for things.

- **problem:** Two-stage open-vocab systems (propose then label) fail differently per class type, but published error rates never attribute failure to stages.
- **core_hypothesis:** Stage-decomposed error analysis shows proposal-stage recall is the binding constraint for stuff and rare-shaped classes, while text-matching dominates errors for common things.
- **why_important:** Tells the field which stage deserves investment per deployment vocabulary, replacing blanket architecture claims.
- **why_possibly_novel:** A stage-attribution error taxonomy across class types is missing from open-vocab literature.
- **minimal_experiment:** Instrument 4 two-stage systems with oracle swaps (oracle proposals, oracle labels); decompose per-class error into stage contributions on ADE20K-Full.
- **main_risk:** Oracle-swap analysis can overestimate stage independence when stages co-adapt.
- **cluster:** `vlm_dense_failure`

### W2-B-0048 — Grounding models segment mirror reflections as real objects because contrastive pretraining never penalized view inconsistency.

- **problem:** Reflections, pictures-of-objects, and screens depict objects without being them; dense grounding behavior on depictions is uncharacterized.
- **core_hypothesis:** Referring models segment reflections/depictions as targets at high rates, while models with any 3D or video pretraining component show significantly lower depiction confusion.
- **why_important:** Depiction errors are safety-relevant (robots grabbing mirror images) and diagnose whether models encode objecthood or appearance.
- **why_possibly_novel:** A depiction-vs-reality benchmark for dense grounding is new.
- **minimal_experiment:** Curate mirror/screen/poster scenes with paired real objects; measure target-selection rates across models grouped by pretraining signal type.
- **main_risk:** Expression phrasing ("the dog" vs "the reflection of the dog") strongly modulates ground truth; requires precise annotation protocol.
- **cluster:** `vlm_dense_failure`

### W2-B-0049 — Region-level typographic attacks hijack referring segmentation more strongly than image-level attacks hijack classification.

- **problem:** Written words in scenes (labels, signs) may capture language-driven segmenters; the dense-level vulnerability is unquantified.
- **core_hypothesis:** Placing a small text patch with a distractor class name shifts referring masks to the text region at a rate exceeding classification-level typographic attack success at matched patch size.
- **why_important:** Dense typographic vulnerability is a concrete deployment attack surface for open-vocab systems in retail/street settings.
- **why_possibly_novel:** Typographic attacks are documented for CLIP classification; the dense/grounding threat model is unmeasured (UNVERIFIED — needs lit search).
- **minimal_experiment:** Paste text patches at controlled sizes/positions; measure mask capture rate vs patch size for referring and open-vocab segmenters; compare with classification attack curves.
- **main_risk:** OCR-capable encoders vary widely; results may split by encoder family.
- **cluster:** `vlm_dense_failure`

### W2-B-0050 — Plurality morphology in queries ("cat" vs "cats") is largely ignored by referring segmentation systems.

- **problem:** Number marking should change target cardinality of the mask, but models may treat plural and singular queries identically.
- **core_hypothesis:** On multi-instance scenes, plural queries yield single-instance masks (or vice versa) in a large fraction of cases, and number-cue utilization is near zero for most models.
- **why_important:** Number is among the simplest compositional cues; failure sets a lower bound on linguistic grounding fidelity.
- **why_possibly_novel:** Morphological-number utilization has not been isolated for dense outputs.
- **minimal_experiment:** Minimal-pair singular/plural queries on scenes with 1 vs many instances; measure cardinality-correct mask rates and per-model utilization scores.
- **main_risk:** Annotation ambiguity on what a plural mask should include; fix protocol first.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0045

### W2-B-0051 — VLMs default to viewer-centric frames for spatial prepositions, failing object-centric readings systematically.

- **problem:** "Left of the car" is ambiguous between viewer frame and the car's own frame; human languages vary, and model conventions are unknown.
- **core_hypothesis:** Models adopt viewer-centric readings almost exclusively, regardless of prompt cues requesting object-centric frames, and fail scenes where frames conflict.
- **why_important:** Frame handling is critical for embodied instruction following; implicit conventions must be documented, not assumed.
- **why_possibly_novel:** Reference-frame disambiguation for dense grounding has no controlled benchmark.
- **minimal_experiment:** Render scenes with oriented objects where frames dissociate; query both readings with explicit frame instructions; measure frame-following accuracy.
- **main_risk:** Renders may lack cues models use for orientation; include real photos of oriented objects.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0036

### W2-B-0052 — Referring segmenters are amodally blind: instructions to include occluded parts do not change masks.

- **problem:** Whether language can switch a model between modal (visible) and amodal (whole-object) segmentation is untested, though applications need both.
- **core_hypothesis:** Explicit amodal instructions ("include the hidden part") change predicted masks in under a small fraction of occlusion cases, revealing that output completeness is architecture-fixed, not language-controllable.
- **why_important:** Language-controllable amodality is a prerequisite for flexible annotation tools and robotic manipulation planning.
- **why_possibly_novel:** Language-conditioned modal/amodal switching has not been evaluated (UNVERIFIED — needs lit search).
- **minimal_experiment:** Use amodal datasets (occlusion-annotated); issue modal vs amodal instructions; measure instruction-conditioned mask delta vs ground-truth delta.
- **main_risk:** Models may lack amodal training data entirely, making the result expected; still valuable as documentation.
- **cluster:** `vlm_dense_failure`

### W2-B-0053 — Open-vocab segmentation confidence does not track IoU, and miscalibration is worst exactly for rare classes.

- **problem:** Downstream users threshold open-vocab masks by confidence; if calibration degrades with class rarity, the long tail becomes silently unreliable.
- **core_hypothesis:** Expected calibration error of mask confidence grows monotonically with class rarity, and risk-coverage curves show rare-class selective prediction near random.
- **why_important:** Calibration-aware evaluation would change how open-vocab systems are deployed for long-tail vocabularies.
- **why_possibly_novel:** Class-rarity-stratified calibration analysis for dense open-vocab outputs is missing.
- **minimal_experiment:** Compute per-class ECE and risk-coverage curves for 5 systems on ADE20K-Full; regress calibration metrics on class frequency; test post-hoc per-bin recalibration.
- **main_risk:** Rare-class sample sizes make ECE estimates noisy; use grouped estimators.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0037

### W2-B-0054 — Multi-hop referring expressions compound errors multiplicatively, exposing pipeline-like internal processing.

- **problem:** "The cup on the table next to the window" requires chained grounding; whether errors compose multiplicatively (independent hops) or better (joint inference) reveals internal mechanism.
- **core_hypothesis:** Accuracy on k-hop expressions is well fit by the product of single-hop accuracies, indicating no joint constraint satisfaction; deviations below product indicate interference.
- **why_important:** A compositional scaling law for grounding predicts feasibility of complex instructions and diagnoses architecture classes.
- **why_possibly_novel:** Hop-factorized accuracy laws for referring segmentation are unexplored.
- **minimal_experiment:** Construct 1/2/3-hop expression sets with matched atomic difficulty; fit product model per architecture; report deviation signs.
- **main_risk:** Matching atomic difficulty across hop depths is hard; needs careful item design.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0045

### W2-B-0055 — Attention-rollout segmentation from LVLMs is biased toward the first-mentioned noun regardless of query intent.

- **problem:** Practitioners extract masks from LVLM attention; serial-position effects of language would systematically corrupt such masks.
- **core_hypothesis:** When two nouns appear in a query, rollout masses concentrate on the first mention even when the second is the target, with an order-effect size exceeding the semantic effect for many models.
- **why_important:** Order artifacts undermine a popular zero-shot segmentation trick and reveal how language order structures visual attention.
- **why_possibly_novel:** Serial-position analysis of attention-derived masks is new.
- **minimal_experiment:** Paired queries with swapped noun order and fixed targets; measure rollout mask shifts attributable to order vs target identity across LVLMs.
- **main_risk:** Rollout method choice affects results; use multiple attribution methods.
- **cluster:** `vlm_dense_failure`

### W2-B-0056 — More specific referring expressions produce worse masks: information monotonicity is violated in dense grounding.

- **problem:** Adding true, disambiguating detail should never hurt, yet longer expressions may push models off their training distribution of short queries.
- **core_hypothesis:** IoU declines as controlled true details are appended beyond 2-3 attributes, and the decline exceeds tokenizer/length artifacts, violating information monotonicity.
- **why_important:** Practical prompt guidance for users and a clean falsifiable rationality test for grounding systems.
- **why_possibly_novel:** Monotonicity violation curves for dense grounding are unmeasured (UNVERIFIED — needs lit search).
- **minimal_experiment:** Incrementally append verified attributes to minimal expressions on fixed targets; plot IoU vs detail count; control with padding tokens.
- **main_risk:** Attribute verification at scale needs careful annotation; start with rendered scenes.
- **cluster:** `vlm_dense_failure`

### W2-B-0057 — Captioning hallucination rates predict open-vocab segmentation false positives class-by-class.

- **problem:** Hallucination is measured in generation (POPE-style), false positives in segmentation; if the two share a prior-driven mechanism, one should predict the other.
- **core_hypothesis:** Per-class hallucination rate in captioning correlates strongly (rho > 0.6) with per-class false-positive segmentation rate for the same underlying VLM family.
- **why_important:** Unifies two failure literatures and lets cheap text-side audits predict dense-side risks.
- **why_possibly_novel:** Cross-task hallucination transfer between generation and dense prediction is untested.
- **minimal_experiment:** Measure POPE-style hallucination and open-vocab false-positive rates for matched class sets across families sharing encoders; report cross-task correlations and family effects.
- **main_risk:** Shared encoders but different heads may break the correlation, which is itself informative.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0039

### W2-B-0058 — Non-basic color terms in referring expressions snap to nearest basic color categories in mask selection.

- **problem:** Color naming has known psychophysical structure (basic vs non-basic terms); how VLM grounding partitions color space is unknown.
- **core_hypothesis:** Targets described with non-basic terms ("teal", "maroon") are grounded as their nearest basic color ("blue", "red") with systematic boundary displacement relative to human color-naming data.
- **why_important:** Reveals whether VLM color grounding replicates human category structure or web-text idiosyncrasies; practical for fashion/e-commerce grounding.
- **why_possibly_novel:** Psychophysics-grade color-term grounding maps for dense models are new.
- **minimal_experiment:** Controlled colored-object scenes sampling color space densely; query with 30 color terms; map model color-naming boundaries vs human World Color Survey-style data.
- **main_risk:** Rendering and display color calibration must be rigorous.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0043

### W2-B-0059 — Referring accuracy decays log-linearly with distractor count, defining a distraction scaling law per architecture.

- **problem:** Benchmarks average over scene complexity, obscuring how grounding degrades as same-class distractors increase — the core difficulty of referring tasks.
- **core_hypothesis:** IoU declines log-linearly in distractor count with an architecture-specific slope, and slopes are steeper for one-stage than two-stage systems, providing a capacity signature.
- **why_important:** A distraction law enables extrapolation to crowded real scenes from small benchmarks.
- **why_possibly_novel:** Parametric distractor-scaling characterization of referring models is unexplored.
- **minimal_experiment:** Curate/render scenes with 1-16 same-class distractors and matched expressions; fit decay curves per model; validate slope stability across categories.
- **main_risk:** Distractor count covaries with object size; control sizes explicitly.
- **cluster:** `vlm_dense_failure`

### W2-B-0060 — Prompt-template sensitivity is several times larger for dense prediction than for classification with the same VLM.

- **problem:** Template effects ("a photo of X" vs "X") are documented for zero-shot classification; dense pipelines inherit templates untested for pixel-level effects.
- **core_hypothesis:** The mIoU range across 20 standard templates exceeds the classification accuracy range (relative terms) by a factor of 2 or more, because patch-text similarity is less template-robust than pooled similarity.
- **why_important:** Dense papers may be comparing template luck, not methods; motivates template-marginalized dense reporting.
- **why_possibly_novel:** Template-sensitivity quantification specific to dense outputs is missing.
- **minimal_experiment:** Sweep templates for open-vocab segmentation and classification with identical backbones; compare normalized sensitivity; test whether template ensembling closes the gap.
- **main_risk:** Template effects may interact with vocabulary size; sweep both.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0042

### W2-B-0061 — Cross-lingual referring segmentation failure is text-encoder-driven and predictable from language pretraining share.

- **problem:** Multilingual users query grounding systems in many languages; failure attribution between text encoding and visual grounding is unmeasured.
- **core_hypothesis:** With human-verified translations, per-language IoU drop correlates with the language's estimated share in text pretraining, and re-encoding queries via translation to English recovers most of the drop, localizing failure to the text side.
- **why_important:** Guides multilingual deployment: translation front-ends vs multilingual re-pretraining.
- **why_possibly_novel:** Language-share-stratified dense grounding audits are new.
- **minimal_experiment:** Translate RefCOCO expressions into 12 languages; evaluate native vs translate-to-English pipelines; regress drops on language-share estimates.
- **main_risk:** Translation quality confounds; use multiple translators and back-translation checks.
- **cluster:** `vlm_dense_failure`

### W2-B-0062 — Size adjectives in referring expressions are interpreted as pixel size, not object-class-relative size.

- **problem:** "The small dog" means small-for-a-dog; models may instead pick the smallest image region, confusing distance with size.
- **core_hypothesis:** On scenes where pixel size and class-relative size dissociate (near small object vs far large object), models choose by pixel size predominantly, revealing absent size constancy.
- **why_important:** Size constancy is fundamental to scene understanding; its absence predicts many embodied-instruction errors.
- **why_possibly_novel:** Size-constancy dissociation tests for grounding are unbenchmarked.
- **minimal_experiment:** Render dissociation scenes with depth cues; query with size adjectives; measure pixel-size vs class-relative choice rates; repeat with depth-cue ablations.
- **main_risk:** Depth cues in renders may be too weak; validate on curated real photos.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0051

### W2-B-0063 — VLMs verify region-class claims far better than they localize, defining an exploitable verification-localization gap.

- **problem:** Direct grounding quality vs verification quality ("is there an X in this region?") has not been compared within the same model, though the gap determines whether search-based inference can rescue localization.
- **core_hypothesis:** Verification accuracy exceeds direct localization accuracy substantially, and verification-guided region search closes much of the grounding gap at quantified extra compute.
- **why_important:** If verification is reliably stronger, dense inference should be reorganized as propose-and-verify, changing system design.
- **why_possibly_novel:** A within-model verification-localization gap measurement for dense outputs is new (UNVERIFIED — needs lit search).
- **minimal_experiment:** For matched targets, measure direct grounding vs verification over candidate regions vs verification-guided search; report accuracy-compute frontiers.
- **main_risk:** Verification may share the same prior-driven failure modes, capping gains.
- **cluster:** `vlm_dense_failure`

### W2-B-0064 — Part-whole mask consistency violations are pervasive: "wheel" masks routinely escape "car" masks.

- **problem:** Independently queried part and whole masks should nest; violation rates measure internal coherence of dense grounding without ground truth.
- **core_hypothesis:** Nesting violations occur in a substantial fraction of part-whole queries, exceed rates implied by boundary noise alone, and correlate with hallucination metrics across models.
- **why_important:** Provides a label-free intrinsic consistency metric usable for monitoring deployed systems.
- **why_possibly_novel:** Part-whole consistency as an unsupervised evaluation axis for grounding is unexplored.
- **minimal_experiment:** Query 50 part-whole pairs over COCO/PACO-style data; compute containment violation rates and correlate with supervised quality metrics across models.
- **main_risk:** Some parts legitimately extend beyond wholes (antenna vs car body definitions); curate pairs.
- **cluster:** `vlm_dense_failure`

### W2-B-0065 — Action words in static grounding ("the man running") are resolved by pose priors and fail on frozen atypical poses.

- **problem:** Grounding action descriptions in still images requires pose-to-verb mapping; reliance on canonical pose templates would fail exactly on unusual but valid poses.
- **core_hypothesis:** Grounding accuracy for action expressions drops sharply on atypical-pose instances (falling, mid-turn) relative to canonical poses at matched visibility, revealing template matching rather than motion understanding.
- **why_important:** Atypical poses are precisely the safety-critical cases (falls, accidents) in monitoring applications.
- **why_possibly_novel:** Pose-typicality-stratified action grounding evaluation is new.
- **minimal_experiment:** Stratify action-grounding items by pose typicality (measured via pose-estimation density models); compare accuracy curves across models.
- **main_risk:** Typicality estimation itself uses learned models; validate with human typicality ratings.
- **cluster:** `vlm_dense_failure`

### W2-B-0066 — Open-vocabulary systems inherit a "thing bias": stuff classes degrade far more than things relative to closed-vocab baselines.

- **problem:** Open-vocab progress is reported on thing-heavy benchmarks; the stuff penalty of language-driven segmentation is uncharacterized.
- **core_hypothesis:** The performance ratio open-vocab/closed-vocab is significantly lower for stuff than things, because caption language under-describes amorphous regions, and the gap correlates with caption-mention statistics.
- **why_important:** Warns against deploying open-vocab systems for stuff-dominated domains (roads, terrain, weather) without targeted fixes.
- **why_possibly_novel:** A things-vs-stuff decomposition of the open-vocab penalty tied to caption statistics is new.
- **minimal_experiment:** Compare matched open/closed-vocab systems per class on COCO-Stuff; regress the penalty on caption-mention frequency of each class.
- **main_risk:** Closed-vocab baselines differ in training data; use distillation-matched pairs where possible.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0037

### W2-B-0067 — Region-caption-then-ground cycle inconsistency is an unsupervised error signal for dense grounding.

- **problem:** Deployed grounding systems lack ground truth; a cycle test (caption a region, then ground the caption) could flag errors without labels.
- **core_hypothesis:** Cycle IoU (original region vs re-grounded region) correlates strongly with supervised accuracy per image, enabling label-free quality monitoring with quantified reliability.
- **why_important:** Practical unsupervised QA for dense VLM systems in production.
- **why_possibly_novel:** Cycle-consistency as a validated error estimator (not training signal) for grounding is unexplored.
- **minimal_experiment:** Run caption-ground cycles on annotated data; measure correlation between cycle IoU and true IoU; characterize failure cases where cycles agree but both are wrong.
- **main_risk:** Correlated errors (shared priors) produce confident wrong cycles; quantify this blind spot explicitly.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0064

### W2-B-0068 — Grounding non-object visual entities (shadows, holes, reflections, gaps) fails categorically, revealing an object-centric ontology.

- **problem:** Language routinely refers to shadows and gaps, but VLM training data may never link such words to their true extents, leaving an ontological blind spot.
- **core_hypothesis:** Grounding accuracy on non-object entities is drastically below matched-difficulty object grounding, and errors default to the casting/adjacent object (grounding "shadow of the man" as the man).
- **why_important:** Non-object references matter in driving (shadows vs obstacles) and inspection (cracks, gaps); the blind spot is safety-relevant.
- **why_possibly_novel:** A non-object reference benchmark for dense grounding does not exist.
- **minimal_experiment:** Annotate shadows/holes/reflections/gaps in curated scenes; compare grounding accuracy and error-target distribution vs matched object controls.
- **main_risk:** Annotation of non-object extents is ambiguous; needs multi-annotator protocols.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0048

### W2-B-0069 — VLM-based segmenters make interior errors where CNNs make boundary errors, so boundary-targeted fixes address the wrong anatomy.

- **problem:** Error-improvement techniques (boundary losses, refinement) assume CNN-era error anatomy; VLM-based dense systems may fail differently (semantic patches missing, interiors mislabeled).
- **core_hypothesis:** Error decomposition shows VLM-based systems have proportionally more interior/semantic errors and fewer pure boundary errors than CNN baselines at matched mIoU, implying boundary-refinement transplants yield little.
- **why_important:** Redirects the adaptation toolbox toward the actual error anatomy of the new model class.
- **why_possibly_novel:** Comparative error-anatomy studies across model generations at matched accuracy are missing.
- **minimal_experiment:** Decompose errors (boundary band vs interior vs missing-segment) for matched-mIoU VLM and CNN systems on ADE20K; test boundary-refinement gains on each class of system.
- **main_risk:** Matching mIoU across paradigms requires careful model selection.
- **cluster:** `vlm_dense_failure`

### W2-B-0070 — Politeness and verbosity tokens in instructions measurably degrade LVLM grounding precision.

- **problem:** Real users wrap requests in pragmatic padding ("could you please maybe show me..."); whether padding degrades dense outputs is untested pragmatic robustness.
- **core_hypothesis:** Padding lowers grounding IoU beyond length-matched neutral controls, because instruction-tuning distributions concentrate on terse imperative phrasings.
- **why_important:** Human-realistic phrasing robustness determines real deployment quality, unmeasured by benchmark phrasing.
- **why_possibly_novel:** Pragmatic-padding robustness for dense outputs is unexplored.
- **minimal_experiment:** Wrap fixed referring expressions in politeness/hedging templates vs length-matched neutral text; measure IoU deltas across models and padding types.
- **main_risk:** Effects may be small; power the study with many items.
- **cluster:** `vlm_dense_failure`
- **mutate_from:** W2-B-0056

---

## 3. Large-model fine-tuning instability

Cluster key: `finetune_instability`

### W2-B-0071 — Fine-tuning loss spikes originate in identifiable attention heads whose entropy collapses steps before the spike.

- **problem:** Loss spikes during VFM fine-tuning are handled by folklore (restart, clip, lower LR) without a mechanistic precursor signal.
- **core_hypothesis:** Per-head attention entropy shows detectable collapse 10-100 steps before loss spikes, and freezing or temperature-patching just those heads prevents the spike without global LR reduction.
- **why_important:** A spike early-warning system would save large fine-tuning runs and replace superstition with mechanism.
- **why_possibly_novel:** Head-level spike precursors have been discussed for pretraining at scale but not for downstream VFM fine-tuning (UNVERIFIED — needs lit search).
- **minimal_experiment:** Instrument ViT-L fine-tuning on segmentation with per-head entropy logging across seeds/LRs; build a spike predictor; test targeted-head interventions vs global LR cuts.
- **main_risk:** Spikes may have heterogeneous causes; predictor may cover only a subset.
- **cluster:** `finetune_instability`

### W2-B-0072 — Learning-rate warmup masks instability rather than removing it: warmed-up runs land in the same fragile basins.

- **problem:** Warmup is universally applied, but whether it changes the reached solution or merely avoids transient divergence is unknown.
- **core_hypothesis:** Runs with and without warmup that both survive land in linearly-connected basins with indistinguishable OOD behavior, showing warmup affects survival probability, not solution quality.
- **why_important:** Clarifies what warmup buys, informing schedule design and how much tuning effort it deserves.
- **why_possibly_novel:** Mode-connectivity analysis of warmup specifically for VFM fine-tuning outcomes is unexplored.
- **minimal_experiment:** Fine-tune with/without warmup across 10 seeds; measure survival rates, then linear-mode-connectivity barriers and OOD metrics between survivors.
- **main_risk:** Survivorship bias complicates comparisons; needs many seeds.
- **cluster:** `finetune_instability`

### W2-B-0073 — Seed-to-seed fine-tuning variance concentrates in LayerNorm gain parameters, not attention weights.

- **problem:** Fine-tuning variance is treated as diffuse noise; locating which parameter groups actually vary across seeds would target stabilization efforts.
- **core_hypothesis:** Across-seed weight variance normalized by parameter scale is largest in LN gains/biases, and transplanting LN parameters between runs transfers most of the functional variance.
- **why_important:** If variance is LN-localized, cheap stabilizers (LN freezing or averaging) could replace expensive multi-seed ensembling.
- **why_possibly_novel:** Parameter-group-resolved variance attribution with transplant experiments is new for VFM fine-tuning.
- **minimal_experiment:** Fine-tune 10 seeds on segmentation; compute groupwise variance; perform cross-run parameter transplants to attribute functional variance to groups.
- **main_risk:** Interaction effects may defeat transplant attribution.
- **cluster:** `finetune_instability`

### W2-B-0074 — The CLIP modality gap collapses abruptly during fine-tuning, and the collapse step predicts zero-shot robustness loss.

- **problem:** Fine-tuning CLIP degrades zero-shot abilities, but the trajectory of the joint-space geometry during fine-tuning is unobserved.
- **core_hypothesis:** The image-text gap statistic stays stable then collapses within a narrow step window (phase transition), and the collapse onset predicts the bulk of OOD/zero-shot degradation better than loss curves.
- **why_important:** A geometric early-stopping signal could preserve zero-shot abilities at negligible task cost.
- **why_possibly_novel:** Tracking modality-gap dynamics as a fine-tuning diagnostic is unexplored (UNVERIFIED — needs lit search).
- **minimal_experiment:** Fine-tune CLIP on classification/segmentation while logging gap statistics per step; correlate collapse onset with zero-shot metric trajectories across LRs.
- **main_risk:** The gap statistic may drift smoothly for some tasks, weakening the phase-transition claim.
- **cluster:** `finetune_instability`

### W2-B-0075 — Small-dataset fine-tuning instability is driven by data order, and gradient-coherence curricula stabilize it.

- **problem:** On small downstream sets, different data orders produce large outcome variance; whether ordering is a primary instability cause (not just noise) is untested.
- **core_hypothesis:** Variance across data orders exceeds variance across weight-init seeds at small data scale, and ordering batches by gradient coherence (agreeing gradients first) reduces outcome variance substantially.
- **why_important:** Data ordering is free; a validated curriculum would improve every few-shot fine-tuning pipeline.
- **why_possibly_novel:** Order-variance vs seed-variance decomposition with coherence-based remediation is new for VFM adaptation.
- **minimal_experiment:** Factorial design (orders x seeds) on 1k-image segmentation fine-tuning; measure variance components; test coherence curriculum vs random ordering.
- **main_risk:** Coherence computation cost may offset benefits; measure total budget.
- **cluster:** `finetune_instability`

### W2-B-0076 — bf16 fine-tuning instability localizes to softmax denominators at high-norm outlier token positions.

- **problem:** Mixed-precision fine-tuning of ViTs occasionally diverges; the numerical failure site is guessed at, not localized.
- **core_hypothesis:** Numerical error concentrates in attention softmax rows involving high-norm outlier tokens, and selectively computing those rows in fp32 removes most divergence at negligible cost.
- **why_important:** A surgical numerical fix beats blanket fp32 fallbacks, and links numerics to the register-token phenomenon.
- **why_possibly_novel:** Connecting outlier-token structure to mixed-precision failure sites is unexplored.
- **minimal_experiment:** Log numerical error maps during bf16 fine-tuning; correlate with token norms; implement row-selective precision and measure divergence rates across seeds.
- **main_risk:** Divergence is rare; needs many runs or amplified settings to get statistics.
- **cluster:** `finetune_instability`
- **mutate_from:** W2-B-0001

### W2-B-0077 — The standard layer-wise LR decay direction is wrong for dense tasks: early layers need larger, not smaller, updates.

- **problem:** Layer-wise decay (smaller LR for early layers) was tuned on classification; dense tasks under sensor/low-level shift may need the opposite profile.
- **core_hypothesis:** For segmentation under low-level domain shift, an inverted decay profile outperforms standard decay, while classification prefers the standard profile — the optimal profile is task-type-dependent, not universal.
- **why_important:** A default hyperparameter used everywhere may be systematically suboptimal for the dense half of the field.
- **why_possibly_novel:** Task-conditional direction of layer-wise decay has not been established.
- **minimal_experiment:** Sweep decay profiles (standard, flat, inverted, V-shaped) for classification vs segmentation fine-tuning under matched budgets; map best profile per task-shift combination.
- **main_risk:** Interactions with absolute LR may dominate; requires joint sweeps.
- **cluster:** `finetune_instability`

### W2-B-0078 — The first 100 fine-tuning steps determine final OOD robustness, enabling early-trajectory diagnosis.

- **problem:** OOD robustness of a fine-tuned model is measured at the end, wasting compute on runs destined to be brittle.
- **core_hypothesis:** Early weight-trajectory features (initial gradient alignment with pretraining-sensitive directions, early feature drift rate) predict final OOD robustness with high rank correlation, long before task metrics separate.
- **why_important:** Early stopping/selection of fine-tuning runs by robustness fate would cut compute and improve deployed robustness.
- **why_possibly_novel:** Early-trajectory forecasting targets in-distribution accuracy in prior work; robustness-fate forecasting is new (UNVERIFIED — needs lit search).
- **minimal_experiment:** Run 50 fine-tunings with varied hyperparameters; extract early-trajectory features; train/test a robustness-fate predictor with proper run-level splits.
- **main_risk:** Predictors may not transfer across tasks/architectures without recalibration.
- **cluster:** `finetune_instability`

### W2-B-0079 — Grokking-like delayed generalization occurs in dense fine-tuning under strong weight decay, hidden by early stopping.

- **problem:** Grokking is documented on algorithmic tasks; whether dense fine-tuning exhibits delayed generalization regimes that standard schedules truncate is unknown.
- **core_hypothesis:** With small data and strong weight decay, segmentation fine-tuning shows a delayed boundary-metric improvement phase after apparent plateau, which common early stopping cuts off.
- **why_important:** If real, standard practice systematically underestimates what small-data fine-tuning can achieve.
- **why_possibly_novel:** Grokking searches in dense vision adaptation are unexplored.
- **minimal_experiment:** Long-horizon (50x standard) fine-tuning runs across weight-decay grid on small segmentation sets; monitor interior vs boundary metrics for delayed transitions.
- **main_risk:** Compute-heavy with plausible null result; mitigate with small backbones.
- **cluster:** `finetune_instability`

### W2-B-0080 — EMA-of-weights gains during fine-tuning are largely equivalent to interpolation toward initialization.

- **problem:** EMA is credited with stabilization magic; if its benefit reduces to implicit init-interpolation (WiSE-FT-like), simpler post-hoc interpolation would suffice.
- **core_hypothesis:** Matched-coefficient post-hoc interpolation between final and initial weights reproduces most of EMA's OOD gains, with residual differences confined to early-training transients.
- **why_important:** Replaces a training-time mechanism with a free post-hoc step and clarifies why EMA helps.
- **why_possibly_novel:** A formal EMA-vs-init-interpolation equivalence test for fine-tuned VFMs is missing.
- **minimal_experiment:** Fine-tune with/without EMA; sweep post-hoc interpolation coefficients; compare ID/OOD frontiers of EMA vs interpolation across tasks.
- **main_risk:** Equivalence may hold only for short fine-tunes; test length dependence.
- **cluster:** `finetune_instability`

### W2-B-0081 — Pretraining loss-surface sharpness transfers: sharper pretrained minima produce less stable fine-tuning.

- **problem:** Fine-tuning stability differences across checkpoints of the same architecture are unexplained; curvature inherited from pretraining is a candidate cause.
- **core_hypothesis:** Checkpoint sharpness measured before fine-tuning predicts fine-tuning spike frequency and seed variance, controlling for task and data.
- **why_important:** A sharpness audit would let practitioners choose checkpoints for stability, and pretraining recipes could optimize for downstream tunability.
- **why_possibly_novel:** The sharpness-transfer hypothesis across the pretrain-finetune boundary is untested (UNVERIFIED — needs lit search).
- **minimal_experiment:** Assemble checkpoints differing in pretraining recipe; measure spectral sharpness; fine-tune each across seeds; correlate sharpness with instability statistics.
- **main_risk:** Sharpness measures are reparameterization-sensitive; use multiple invariant proxies.
- **cluster:** `finetune_instability`

### W2-B-0082 — A "normalization shock" in the first fine-tuning steps causes lasting damage, and brief LN-freezing prevents it.

- **problem:** At fine-tuning onset, LN statistics shift abruptly to the new data distribution; whether this transient causes persistent feature damage is unknown.
- **core_hypothesis:** LN parameters absorb most first-epoch change; freezing LN for a short warm period then unfreezing yields better final OOD metrics at equal ID accuracy, demonstrating transient-induced damage.
- **why_important:** A two-line schedule change with measurable robustness benefits across all VFM fine-tuning.
- **why_possibly_novel:** The transient-damage framing with staged LN unfreezing as a falsifiable test is new.
- **minimal_experiment:** Compare standard vs LN-frozen-warmup fine-tuning across tasks/seeds; track feature drift and final ID/OOD metrics; ablate freeze duration.
- **main_risk:** Effect may be subsumed by existing warmup practices; control carefully.
- **cluster:** `finetune_instability`
- **mutate_from:** W2-B-0073

### W2-B-0083 — Minority-class gradients cause loss spikes under class imbalance, making spikes predictable from batch composition.

- **problem:** Spikes in dense fine-tuning are treated as random; rare-class-heavy batches produce outsized, poorly-conditioned gradients that may explain them.
- **core_hypothesis:** Spike probability increases sharply with batch minority-class pixel share, and per-class gradient-norm caps eliminate most spikes without harming minority-class learning.
- **why_important:** Composition-aware batching is cheap and would stabilize long-tail dense fine-tuning broadly.
- **why_possibly_novel:** Linking spike events to batch class composition quantitatively is unexplored.
- **minimal_experiment:** Log batch composition and gradient norms during long-tail segmentation fine-tuning; fit spike predictors; test per-class norm caps vs global clipping.
- **main_risk:** Caps could slow minority-class fitting; monitor per-class learning curves.
- **cluster:** `finetune_instability`

### W2-B-0084 — Fine-tuning distorts features anisotropically: damage concentrates in the task-relevant subspace, sparing orthogonal directions.

- **problem:** Feature-distortion theory says fine-tuning corrupts pretrained features, but whether distortion is isotropic or targeted determines what is lost and what survives.
- **core_hypothesis:** The weight-update spectrum is low-rank and aligned with task-discriminative directions; probes on orthogonal subspaces retain pretraining abilities almost fully, refining the distortion picture.
- **why_important:** Explains partial-forgetting phenomena and grounds subspace-protective fine-tuning methods in measurement rather than intuition.
- **why_possibly_novel:** Directional decomposition of distortion with ability-resolved probing is new beyond the original LP-FT observations.
- **minimal_experiment:** SVD of weight deltas after fine-tuning; project features onto update-aligned vs orthogonal subspaces; probe old-task and new-task abilities in each subspace.
- **main_risk:** Layerwise subspaces interact nonlinearly; conclusions may not compose across depth.
- **cluster:** `finetune_instability`

### W2-B-0085 — Weight decay during fine-tuning pulls toward zero, not toward pretrained weights, silently eroding pretrained structure.

- **problem:** Standard decay regularizes toward the origin, which for a pretrained model is an arbitrary point; decay-to-init is rarely used and never systematically compared for VFMs.
- **core_hypothesis:** Decay-to-init strictly dominates decay-to-zero on the stability-plasticity frontier for VFM fine-tuning, with the largest gains at high decay coefficients and small datasets.
- **why_important:** A default optimizer setting used in thousands of fine-tunings may be measurably wrong for the pretrained regime.
- **why_possibly_novel:** The comparison exists in continual-learning niches; a systematic VFM fine-tuning study across tasks/scales is missing (UNVERIFIED — needs lit search).
- **minimal_experiment:** Grid over decay type/coefficient/data size for classification and segmentation fine-tuning; map ID accuracy vs zero-shot retention frontiers.
- **main_risk:** Interaction with adaptive optimizers may complicate a clean story.
- **cluster:** `finetune_instability`

### W2-B-0086 — Resolution change at fine-tuning onset causes a positional-embedding transient that inflates instability; freezing PEs briefly fixes it.

- **problem:** Fine-tuning often changes input resolution from pretraining, forcing PE interpolation whose training transient is unstudied as an instability source.
- **core_hypothesis:** Runs with resolution change show early gradient norms dominated by PE-adjacent parameters and higher spike rates; freezing PEs for the first epochs removes the excess instability.
- **why_important:** Resolution changes are ubiquitous in dense adaptation; a validated PE-freeze recipe would be widely applicable.
- **why_possibly_novel:** PE-transient attribution for fine-tuning instability is unexplored.
- **minimal_experiment:** Fine-tune at matched vs changed resolution across seeds; attribute early gradient norms; test PE-freeze schedules on spike rates and final metrics.
- **main_risk:** Modern models with rotary/factorized PEs may not exhibit the transient.
- **cluster:** `finetune_instability`
- **mutate_from:** W2-B-0005

### W2-B-0087 — Models recover accuracy after loss spikes but retain permanent calibration scars.

- **problem:** Post-spike runs that recover their loss are treated as unharmed; slower-recovering properties like calibration may hold hidden damage.
- **core_hypothesis:** Runs that experienced spikes end with significantly worse calibration (ECE) and OOD detection than spike-free runs at matched final accuracy, revealing spike hysteresis.
- **why_important:** Spike tolerance policies ("it recovered, ship it") may be systematically shipping miscalibrated models.
- **why_possibly_novel:** Post-spike property audits beyond accuracy are unexplored.
- **minimal_experiment:** Collect spiked vs non-spiked runs at matched final accuracy (natural experiments plus induced spikes); compare calibration, OOD detection, and adversarial sensitivity.
- **main_risk:** Matching final accuracy while varying spike history requires large run pools.
- **cluster:** `finetune_instability`
- **mutate_from:** W2-B-0071

### W2-B-0088 — Augmentation strength has a non-monotonic destabilizing effect: moderate augmentation is worse than none or heavy.

- **problem:** Augmentation is assumed to regularize monotonically; a destabilization peak at moderate strength would explain contradictory tuning experiences.
- **core_hypothesis:** Fine-tuning outcome variance across seeds peaks at intermediate augmentation strength, where batches mix easy and hard views with maximally conflicting gradients.
- **why_important:** Explains and fixes a common source of irreproducible fine-tuning results.
- **why_possibly_novel:** Variance-vs-augmentation-strength curves (not accuracy curves) are unmeasured.
- **minimal_experiment:** Sweep augmentation magnitude on VFM segmentation fine-tuning with 10 seeds per level; plot outcome variance and gradient-conflict statistics vs strength.
- **main_risk:** The peak location may be task-specific, limiting general guidance.
- **cluster:** `finetune_instability`
- **mutate_from:** W2-B-0075

### W2-B-0089 — Initializing Adam's second-moment estimates from pretraining gradient statistics removes early-phase instability.

- **problem:** Optimizer state resets at fine-tuning start, so early steps use uncalibrated preconditioners — a plausible but untested instability source.
- **core_hypothesis:** Warm-starting second moments from a brief gradient-statistics pass (or shipped pretraining statistics) reduces early gradient-norm variance and spike rates versus standard zero-init, at equal final accuracy.
- **why_important:** Costless recipe change; would also motivate checkpoints shipping optimizer statistics.
- **why_possibly_novel:** Optimizer-state warm-starting across the pretrain-finetune boundary is unexplored for VFMs (UNVERIFIED — needs lit search).
- **minimal_experiment:** Compare zero-init vs statistics-init Adam on VFM fine-tuning across LRs/seeds; measure early-phase stability metrics and final performance.
- **main_risk:** Pretraining and fine-tuning gradient scales differ; statistics may need rescaling rules.
- **cluster:** `finetune_instability`

### W2-B-0090 — Multi-task fine-tuning interference is directional: segmentation destabilizes depth more than depth destabilizes segmentation.

- **problem:** Task interference is reported as symmetric averages; directionality would change task-grouping and scheduling decisions.
- **core_hypothesis:** An interference matrix over dense tasks is strongly asymmetric, with discrete-output tasks destabilizing continuous-output tasks more than the reverse, predictable from gradient-conflict geometry.
- **why_important:** Task curricula and grouping for multi-task adaptation could be designed from the matrix rather than trial and error.
- **why_possibly_novel:** Directional instability (variance transfer), as opposed to final-accuracy interference, is unmeasured.
- **minimal_experiment:** Pairwise multi-task fine-tuning over seg/depth/normals/edges with seed replication; measure per-task variance inflation by partner task; relate to gradient-conflict angles.
- **main_risk:** Head architecture choices may drive asymmetries; standardize heads.
- **cluster:** `finetune_instability`

### W2-B-0091 — The effective rank of features during fine-tuning stabilizes early and predicts final performance, enabling rank-based early stopping.

- **problem:** Early-stopping criteria use validation loss, which needs labels and lags; a label-free trajectory statistic predicting the endpoint would be widely useful.
- **core_hypothesis:** Feature effective-rank trajectories converge within the first tenth of training, and their plateau value predicts final task metrics across hyperparameter settings with high rank correlation.
- **why_important:** Label-free run selection and early termination could save the bulk of fine-tuning compute in sweeps.
- **why_possibly_novel:** Effective-rank as a predictive (not descriptive) fine-tuning statistic is untested.
- **minimal_experiment:** Log feature effective rank during 100 varied fine-tuning runs; evaluate early-rank predictors of final mIoU/accuracy against validation-loss baselines at equal step budgets.
- **main_risk:** Rank may saturate uninformatively for some architectures.
- **cluster:** `finetune_instability`
- **mutate_from:** W2-B-0078

### W2-B-0092 — Instability grows with model scale at fixed fine-tuning data: an inverse stability scaling law.

- **problem:** Scale improves pretraining stability, but fine-tuning ever-larger models on small datasets may become intrinsically less stable — a possibility never characterized as a law.
- **core_hypothesis:** Across a model ladder fine-tuned on fixed small data, seed variance and spike rates increase with scale following a power law, unless LR is shrunk faster than standard heuristics prescribe.
- **why_important:** Establishes safe LR-vs-scale schedules for downstream users who cannot afford instability, complementing pretraining scaling laws.
- **why_possibly_novel:** Downstream-instability scaling laws are absent from the scaling literature (UNVERIFIED — needs lit search).
- **minimal_experiment:** Fine-tune ViT-S/B/L/H on fixed 5k-image tasks across LR grids and 10 seeds; fit variance and spike-rate scaling exponents; derive stable-LR frontier.
- **main_risk:** Expensive at the largest scales; can bound with three points plus extrapolation checks.
- **cluster:** `finetune_instability`

### W2-B-0093 — In CLIP fine-tuning, text-encoder token norms destabilize before the vision side, providing cross-modal spike precursors.

- **problem:** Joint fine-tuning of dual encoders shows instabilities attributed to the vision tower by default; the temporal order of cross-modal destabilization is unmeasured.
- **core_hypothesis:** Rare-token embedding norms in the text encoder inflate measurably before joint-loss spikes, and text-side-only interventions (embedding norm caps) prevent vision-side damage.
- **why_important:** Cross-modal monitoring would stabilize the increasingly common practice of tuning both towers.
- **why_possibly_novel:** Cross-modal ordering of instability events is unexplored.
- **minimal_experiment:** Log per-modality norm/gradient statistics during CLIP fine-tuning; establish temporal precedence via lead-lag analysis; test text-side caps.
- **main_risk:** Precedence may reverse across tasks; needs diverse task battery.
- **cluster:** `finetune_instability`
- **mutate_from:** W2-B-0074

### W2-B-0094 — Sharpness-aware minimization helps in-distribution but harms dense-feature transfer, inverting its reputation for fine-tuning.

- **problem:** SAM-style optimizers are adopted for fine-tuning on the assumption that flatness aids generalization; the effect on the transferability of intermediate dense features is untested.
- **core_hypothesis:** SAM-fine-tuned backbones yield worse frozen-feature performance for secondary dense tasks than SGD/AdamW-tuned ones at equal primary-task accuracy, because flatness is bought by simplifying intermediate representations.
- **why_important:** Optimizer choice may silently trade representation richness for primary-task flatness — critical for models reused as feature extractors.
- **why_possibly_novel:** Optimizer effects on downstream reusability (not primary generalization) are unmeasured.
- **minimal_experiment:** Fine-tune with SAM vs AdamW at matched primary metrics; freeze and probe intermediate features on held-out dense tasks; compare reusability gaps.
- **main_risk:** Matching primary accuracy exactly is fiddly; use accuracy-matched checkpoints along trajectories.
- **cluster:** `finetune_instability`

### W2-B-0095 — Adaptive gradient clipping matched to cumulative weight displacement reproduces PEFT-level stability in full fine-tuning.

- **problem:** PEFT's stability is attributed to parameter scarcity, but it may reduce to constraining total weight displacement — reproducible in full fine-tuning with the right trust region.
- **core_hypothesis:** Full fine-tuning with a displacement-budget constraint (clipping scaled to keep total delta-norm on a LoRA-matched schedule) matches LoRA's stability and OOD retention while exceeding its task accuracy.
- **why_important:** Would unify PEFT and full fine-tuning under a trust-region view and give practitioners the best of both.
- **why_possibly_novel:** Displacement-matched comparisons between PEFT and constrained full fine-tuning are missing.
- **minimal_experiment:** Measure LoRA runs' displacement schedules; impose them on full fine-tuning via adaptive clipping; compare stability, OOD retention, and accuracy across tasks.
- **main_risk:** Layerwise displacement structure, not just total norm, may matter; test structured budgets.
- **cluster:** `finetune_instability`

### W2-B-0096 — Checkpoint averaging along a fine-tuning trajectory improves OOD metrics but degrades boundary sharpness in dense predictions.

- **problem:** Trajectory averaging is a popular free win, evaluated on classification-style metrics; its effect on spatial output structure is unknown.
- **core_hypothesis:** Averaged checkpoints show better OOD mIoU but consistently worse boundary F1 than endpoint checkpoints, because weight-space smoothing acts as prediction-space spatial smoothing.
- **why_important:** Warns dense-prediction users that a standard trick trades away exactly what many applications need.
- **why_possibly_novel:** The weight-smoothing-to-prediction-smoothing link for dense outputs is unexamined.
- **minimal_experiment:** Compare endpoint vs averaged checkpoints on interior/boundary decomposed metrics across segmentation tasks; visualize where predictions blur; test frequency-of-averaging effects.
- **main_risk:** Effect size may be small relative to metric noise; power appropriately.
- **cluster:** `finetune_instability`
- **mutate_from:** W2-B-0080

### W2-B-0097 — Unstable fine-tuning runs are exactly those that exit the pretrained basin, measurable by mode-connectivity barriers to initialization.

- **problem:** "Instability" lacks a geometric definition; connecting it to loss-landscape topology would unify spike behavior, variance, and forgetting.
- **core_hypothesis:** Runs with high spike counts and seed variance show large linear-connectivity barriers to the pretrained weights, while stable runs remain barrier-free; the barrier height predicts zero-shot retention.
- **why_important:** One geometric quantity would summarize stability, forgetting, and interpolatability for practitioners.
- **why_possibly_novel:** Barrier-height-based instability taxonomy for fine-tuning is new.
- **minimal_experiment:** For a pool of fine-tuning runs, compute loss barriers on the pretrained-to-final segment; correlate with spike counts, variance, and zero-shot retention.
- **main_risk:** Barrier estimates depend on evaluation data choice; report across datasets.
- **cluster:** `finetune_instability`
- **mutate_from:** W2-B-0072

### W2-B-0098 — LoRA dynamics are largely reproduced by full fine-tuning with a rescaled learning rate, questioning capacity-based explanations of PEFT stability.

- **problem:** PEFT stability is credited to low-dimensional updates; if a tiny-LR full fine-tune matches LoRA's trajectory in function space, the mechanism is LR rescaling, not dimensionality.
- **core_hypothesis:** Function-space divergence (prediction disagreement over probes) between LoRA and LR-matched full fine-tuning stays within seed-noise levels for most of training, diverging only late.
- **why_important:** Correct mechanistic attribution redirects PEFT research from architecture toward optimization schedules.
- **why_possibly_novel:** Function-space trajectory matching between PEFT and rescaled full fine-tuning is untested (UNVERIFIED — needs lit search).
- **minimal_experiment:** Match early-step function-space movement by LR calibration; track prediction divergence, OOD retention, and final metrics across tasks and ranks.
- **main_risk:** The correct LR-matching rule is nontrivial; test several (gradient-norm, update-norm, NTK-based).
- **cluster:** `finetune_instability`
- **mutate_from:** W2-B-0095

### W2-B-0099 — Boundary-pixel label noise is a hidden driver of dense fine-tuning instability.

- **problem:** Annotation boundaries are inherently noisy (annotator jitter), injecting systematic label noise concentrated at edges; its causal role in training instability is unquantified.
- **core_hypothesis:** Excluding or down-weighting a thin boundary band during loss computation reduces gradient variance and seed variance substantially while leaving interior accuracy unchanged, isolating boundary noise as an instability source.
- **why_important:** A trivially implementable loss-masking choice could stabilize all dense fine-tuning pipelines.
- **why_possibly_novel:** Attribution of instability (not accuracy) to boundary label noise is new.
- **minimal_experiment:** Fine-tune with full vs boundary-masked losses across seeds; compare gradient variance, spike rates, and final interior/boundary metrics with re-annotated ground-truth subsets.
- **main_risk:** Masking may slow legitimate boundary learning; sweep band widths.
- **cluster:** `finetune_instability`
- **mutate_from:** W2-B-0083

### W2-B-0100 — Hardware nondeterminism alone accounts for a measurable mIoU spread, setting a noise floor for fine-tuning claims.

- **problem:** Papers claim sub-point improvements without knowing the irreducible variance from nondeterministic GPU kernels at fixed seed.
- **core_hypothesis:** Bit-identical-seed fine-tuning with nondeterministic kernels yields an mIoU spread comparable to many published method gaps, and the spread grows with training length and model size.
- **why_important:** Establishes reporting standards: any claim below the measured hardware noise floor requires deterministic mode or multi-run statistics.
- **why_possibly_novel:** A quantified hardware-noise floor for dense fine-tuning has not been published (UNVERIFIED — needs lit search).
- **minimal_experiment:** Repeat fixed-seed fine-tuning 20 times with nondeterministic kernels on standard segmentation setups; report spread; repeat with deterministic mode to isolate kernel noise.
- **main_risk:** Results vary by hardware/library version; document configurations exhaustively.
- **cluster:** `finetune_instability`
- **mutate_from:** W2-B-0033

---

## 4. Parameter-Efficient Fine-Tuning — when PEFT is wrong

Cluster key: `peft_limits`

### W2-B-0101 — Dense tasks have higher intrinsic update rank than classification, making common LoRA ranks structurally insufficient.

- **problem:** LoRA ranks tuned on classification/NLP folklore (4-16) are copied to dense adaptation without measuring the rank the task actually demands.
- **core_hypothesis:** The singular-value spectrum of full-fine-tuning weight deltas decays much more slowly for segmentation than classification, and LoRA accuracy tracks the captured spectral mass, yielding a task-indexed required-rank law.
- **why_important:** Practitioners would get a principled rank-selection rule instead of cargo-cult defaults, and PEFT papers a fair-comparison standard.
- **why_possibly_novel:** Task-conditional intrinsic-rank measurement with spectral-mass-to-accuracy mapping is missing (UNVERIFIED — needs lit search).
- **minimal_experiment:** Full-fine-tune VFMs on classification/segmentation/detection; compute delta spectra per layer; train LoRA across ranks; regress accuracy gaps on captured spectral mass.
- **main_risk:** Spectra may vary more across layers than tasks, complicating a clean law.
- **cluster:** `peft_limits`

### W2-B-0102 — LoRA introduces high-rank-orthogonal "intruder" directions whose magnitude predicts OOD forgetting in dense tasks.

- **problem:** Reports suggest LoRA solutions contain singular directions absent from full fine-tuning (intruder dimensions — UNVERIFIED, needs lit search); their downstream consequences for dense OOD behavior are unknown.
- **core_hypothesis:** The energy in intruder directions correlates with zero-shot and OOD dense degradation across ranks and tasks, and projecting intruders out post-hoc recovers OOD performance at small ID cost.
- **why_important:** Would give a post-hoc repair for PEFT damage and a diagnostic for when LoRA silently diverges from full fine-tuning behavior.
- **why_possibly_novel:** Linking intruder-direction energy to dense OOD forgetting with a projection-repair test is new.
- **minimal_experiment:** Compare LoRA vs full-FT delta subspaces; quantify intruder energy; correlate with OOD metrics; evaluate post-hoc intruder projection across tasks.
- **main_risk:** Intruder identification depends on full-FT reference runs, limiting practicality.
- **cluster:** `peft_limits`

### W2-B-0103 — For dense adaptation, MLP-block LoRA beats attention-block LoRA, inverting the standard placement heuristic.

- **problem:** LoRA placement defaults (attention projections) come from NLP; dense tasks may need channel-wise feature recombination (MLP) more than attention remixing.
- **core_hypothesis:** At matched parameter budgets, MLP-only LoRA outperforms attention-only LoRA on segmentation but not classification, and the gap grows with the low-level-ness of the domain shift.
- **why_important:** A placement rule conditioned on task type would improve thousands of PEFT applications at zero cost.
- **why_possibly_novel:** Placement studies exist for NLP; a task-type-conditioned placement law for dense vision is unestablished.
- **minimal_experiment:** Factorial placement study (attention/MLP/both) across ranks on segmentation and classification under semantic vs low-level shifts; map best placement per condition.
- **main_risk:** Optimal placement may be backbone-specific, fragmenting the law.
- **cluster:** `peft_limits`

### W2-B-0104 — PEFT preserves pretrained invariances that dense tasks must break, creating an invariance-inheritance ceiling.

- **problem:** PEFT constrains updates near the pretrained function, which preserves helpful semantics but may also lock in harmful invariances (color, small-shift invariance) that boundary-precise tasks need to undo.
- **core_hypothesis:** After adaptation, LoRA models retain pretrained invariances measurably more than full fine-tuning, and retained-invariance magnitude predicts the residual boundary-metric gap between PEFT and full FT.
- **why_important:** Identifies a principled failure condition for PEFT: tasks requiring invariance-breaking, where no rank increase will help.
- **why_possibly_novel:** Invariance-spectrum audits before/after adaptation comparing PEFT vs full FT are new.
- **minimal_experiment:** Measure invariance spectra (shift, color, blur) pre/post adaptation for LoRA vs full FT; correlate retained invariance with per-task PEFT gaps on boundary-sensitive metrics.
- **main_risk:** Invariance measurement conflates encoder and head effects; probe features directly.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0019

### W2-B-0105 — Prompt tuning cannot correct feature-space OOD: its gains vanish exactly on inputs far from the pretraining manifold.

- **problem:** Prompt/prefix tuning modifies inputs to a frozen network, which can only re-mix existing features; for inputs whose features are already degenerate, no prompt may help — a capacity boundary never characterized.
- **core_hypothesis:** Prompt-tuning gains per input decrease with feature-space distance from the pretraining distribution, approaching zero beyond a threshold, while LoRA gains persist — establishing a mechanism-level capability boundary.
- **why_important:** Tells practitioners when prompt-level PEFT is structurally hopeless, saving misdirected tuning effort.
- **why_possibly_novel:** Input-conditional capability boundaries of prompt tuning are unmeasured (UNVERIFIED — needs lit search).
- **minimal_experiment:** Stratify adaptation-set inputs by feature-space OOD score; compare per-stratum gains of VPT vs LoRA vs full FT on medical and aerial transfer tasks.
- **main_risk:** OOD scores are imperfect; use several (kNN distance, likelihood proxies).
- **cluster:** `peft_limits`

### W2-B-0106 — BitFit works because bias/LN shifts implement approximate feature-distribution alignment, replicable by a closed-form transform.

- **problem:** BitFit's effectiveness is unexplained; if it reduces to first-moment feature alignment, an analytic, training-free transform should match it.
- **core_hypothesis:** A closed-form per-channel affine alignment (matching feature means/variances between pretraining and target data) achieves most of BitFit's gains without any gradient steps, revealing its mechanism.
- **why_important:** Would replace a training procedure with statistics estimation, and clarify what the cheapest PEFT methods actually learn.
- **why_possibly_novel:** Mechanistic reduction of BitFit to moment matching with a training-free equivalence test is new.
- **minimal_experiment:** Compute analytic alignment transforms on target data; compare against trained BitFit across tasks/shifts; analyze residual gains attributable to gradient training.
- **main_risk:** Second-order effects (channel interactions) may carry meaningful signal beyond moments.
- **cluster:** `peft_limits`

### W2-B-0107 — Serial adapters create representational bottlenecks that downstream layers provably cannot compensate for.

- **problem:** Adapter down-projections discard information mid-network; whether later layers recover it or the loss is permanent is unknown.
- **core_hypothesis:** Probing accuracy for task-relevant attributes drops sharply after low-width adapter insertion and never recovers in later layers, and the unrecovered information predicts the adapter-vs-full-FT gap.
- **why_important:** Establishes width-selection rules from information flow rather than accuracy sweeps.
- **why_possibly_novel:** Depth-resolved information-loss accounting for adapters is unexplored.
- **minimal_experiment:** Insert adapters of varying widths; probe attribute decodability at every subsequent layer; correlate information deficits with final task gaps.
- **main_risk:** Probes measure linear accessibility, not full information; use nonlinear probes as bounds.
- **cluster:** `peft_limits`

### W2-B-0108 — PEFT and full fine-tuning sit at different points of the calibration-accuracy plane, and the difference flips sign with distribution shift.

- **problem:** PEFT comparisons report accuracy, almost never calibration; deployed systems need both, and the tradeoff structure is unknown (UNVERIFIED — needs lit search).
- **core_hypothesis:** In-distribution, LoRA models are better calibrated than full FT at matched accuracy (less overfitting), but under shift the ordering reverses because PEFT models inherit overconfident pretrained priors they cannot revise.
- **why_important:** Calibration-aware PEFT guidance would change method choice for safety-critical adaptation.
- **why_possibly_novel:** The shift-conditional calibration comparison across PEFT families is missing.
- **minimal_experiment:** Measure ECE/NLL ID and OOD for LoRA/adapters/BitFit/full-FT at matched accuracy across classification and segmentation; map the calibration-shift interaction.
- **main_risk:** Matched-accuracy checkpoint selection introduces selection artifacts; use trajectory-matched pairs.
- **cluster:** `peft_limits`

### W2-B-0109 — Mathematically-neutral LoRA merging interacts destructively with post-training quantization.

- **problem:** Merging LoRA into base weights is treated as a no-op, but the merged weights' distribution shifts can push layers across quantization-grid boundaries, silently changing deployed behavior.
- **core_hypothesis:** Quantizing merged weights degrades accuracy more than quantizing base weights and applying LoRA separately, with the gap concentrated in layers where LoRA updates are large relative to quantization bins.
- **why_important:** Deployment pipelines routinely merge-then-quantize; a validated warning plus layer-level predictor would prevent silent regressions.
- **why_possibly_novel:** The merge-quantize interaction has not been characterized (UNVERIFIED — needs lit search).
- **minimal_experiment:** Compare merge-then-quantize vs quantize-plus-side-LoRA across bit-widths and tasks; localize damage to layers by update-to-bin ratios.
- **main_risk:** Effects may be negligible at 8-bit; focus on 4-bit and below.
- **cluster:** `peft_limits`

### W2-B-0110 — IA3 scaling vectors are a free interpretability probe: task information concentrates in under 5% of channels.

- **problem:** We lack cheap tools to locate where task-relevant computation lives in adapted VFMs; IA3's per-channel multipliers are a naturally sparse measurement instrument nobody exploits.
- **core_hypothesis:** IA3 multipliers deviate from unity in a small, stable-across-seeds channel subset; ablating those channels in the base model removes most task-specific behavior, validating them as causal task loci.
- **why_important:** Turns a PEFT method into a general representational-localization tool for the community.
- **why_possibly_novel:** IA3-as-measurement (not adaptation) is an unexplored reframing.
- **minimal_experiment:** Train IA3 across seeds/tasks; measure multiplier sparsity and cross-seed stability; causally ablate flagged channels and quantify task-behavior removal.
- **main_risk:** Sparsity may be an artifact of IA3's parameterization rather than the model's structure.
- **cluster:** `peft_limits`

### W2-B-0111 — LoRA dropout is functionally equivalent to interpolation toward the pretrained model, not conventional regularization.

- **problem:** Dropout on LoRA paths is applied by habit; because zeroing the adapter recovers the exact pretrained function, its mechanism should differ fundamentally from standard dropout.
- **core_hypothesis:** LoRA-dropout training matches (in function space and OOD retention) training without dropout followed by post-hoc interpolation toward the base model at a coefficient predicted by the dropout rate.
- **why_important:** Would replace a training-time hyperparameter with a controllable post-hoc dial and correct the community's mental model.
- **why_possibly_novel:** The dropout-as-interpolation equivalence for PEFT paths is untested.
- **minimal_experiment:** Sweep LoRA dropout rates; compare against post-hoc interpolation sweeps on ID/OOD metrics and function-space distances across tasks.
- **main_risk:** Stochastic-during-training effects may leave residuals the equivalence misses.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0080

### W2-B-0112 — There exists a shift-magnitude crossover beyond which LoRA-adapted models degrade faster than fully fine-tuned ones.

- **problem:** PEFT is marketed as robustness-preserving based on mild-shift evaluations; behavior under progressively severe shift is uncharted, and the ordering may reverse.
- **core_hypothesis:** Plotting accuracy vs shift severity, LoRA and full-FT curves cross: PEFT wins under mild shift (preserved priors) but loses under severe shift (cannot revise low-level processing), with the crossover severity predictable from shift type.
- **why_important:** Gives deployment teams a shift-severity criterion for choosing adaptation methods.
- **why_possibly_novel:** Severity-resolved PEFT-vs-full-FT crossover analysis is new.
- **minimal_experiment:** Evaluate matched LoRA/full-FT models across graded corruption/domain-shift severities on segmentation; locate crossovers; relate to low-level vs semantic shift type.
- **main_risk:** Crossovers may be absent for some tasks; a robust null is still informative.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0104

### W2-B-0113 — Required LoRA rank for dense tasks scales with output spatial complexity, approximately linearly in boundary density.

- **problem:** No quantitative rule links properties of the target task's output space to the adapter capacity it needs.
- **core_hypothesis:** Across datasets ordered by boundary density (boundary pixels per image), the rank needed to reach 95% of full-FT performance grows approximately linearly, while classification saturates at tiny ranks regardless of class count.
- **why_important:** A capacity-planning formula for PEFT would replace expensive rank sweeps.
- **why_possibly_novel:** Output-complexity-indexed capacity laws for PEFT are unexplored.
- **minimal_experiment:** Rank sweeps on datasets spanning boundary densities (Potsdam, Cityscapes, ADE20K, medical); fit rank-requirement curves; validate on held-out datasets.
- **main_risk:** Boundary density may proxy for other difficulty factors; include covariates.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0101

### W2-B-0114 — VPT prompt tokens function as trainable register tokens: their benefit comes from absorbing global aggregation, not task learning.

- **problem:** Visual prompt tuning's mechanism is unclear; its learnable tokens occupy the same positional niche as register tokens known to absorb artifact attention.
- **core_hypothesis:** A significant fraction of VPT's gain is reproduced by adding frozen random tokens (no learning), and VPT-trained tokens develop the high-norm signature of registers, especially on models pretrained without registers.
- **why_important:** Would reattribute a popular PEFT method's gains and predict that register-equipped backbones benefit less from VPT.
- **why_possibly_novel:** The VPT-register connection has not been tested (UNVERIFIED — needs lit search).
- **minimal_experiment:** Compare VPT vs frozen-random-token insertion vs no-token baselines on register-free and register-equipped backbones; analyze learned-token norm/attention statistics.
- **main_risk:** Partial reproduction is likely; decomposing learned vs absorptive contributions needs careful ablation.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0031

### W2-B-0115 — Optimal LoRA learning rate follows a predictable scaling in rank and layer width, removing a hyperparameter search.

- **problem:** LoRA LR is re-tuned per project; parameterization theory (muP-style) suggests a transferable scaling rule that nobody has validated for vision adaptation.
- **core_hypothesis:** The optimal LR scales as a simple power law in rank and width; calibrating on a small model/rank transfers within a factor of two across the ladder, matching per-configuration tuning.
- **why_important:** Eliminates the most expensive part of PEFT tuning for the whole community.
- **why_possibly_novel:** An empirically validated LR-transfer rule for vision LoRA is missing (theory exists for general parameterizations — UNVERIFIED for this case).
- **minimal_experiment:** Grid LR x rank x width on VFM segmentation/classification adaptation; fit scaling exponents; test transfer from ViT-S calibration to ViT-L deployment.
- **main_risk:** The rule may break across optimizers or schedules; test at least two.
- **cluster:** `peft_limits`

### W2-B-0116 — Uniform-layer PEFT placement wastes most of its budget: adaptation demand is concentrated in a few shift-dependent layers.

- **problem:** PEFT is applied to all layers by default; if per-layer demand is sparse and predictable from a cheap diagnostic, budgets could shrink dramatically at equal quality.
- **core_hypothesis:** A gradient-based or activation-drift diagnostic computed in one forward/backward pass identifies the top-k layers whose adaptation captures most of full-placement performance, and the demanded layers shift from early (sensor shift) to late (semantic shift).
- **why_important:** Converts placement from convention to measurement, with large practical savings.
- **why_possibly_novel:** Placement-demand diagnostics validated causally (by selective placement) are new.
- **minimal_experiment:** Compute drift diagnostics per layer across shift types; train selectively-placed LoRA at matched budgets; compare against uniform placement and oracle search.
- **main_risk:** Diagnostic may mispredict for compound shifts; test mixtures explicitly.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0103

### W2-B-0117 — Sequential LoRA training on task chains accumulates directional interference that parallel training then merging avoids.

- **problem:** Practitioners fine-tune LoRAs sequentially on evolving data; whether sequence position creates order-dependent interference (unlike merging independently trained LoRAs) is unquantified.
- **core_hypothesis:** Chained training exhibits strong order effects (later tasks reshape earlier subspaces), while independent-then-merged LoRAs show weaker, symmetric interference — measurable as subspace rotation of earlier adapters.
- **why_important:** Guides continual PEFT practice: train in parallel and merge, or accept order-dependence.
- **why_possibly_novel:** Order-effect quantification for sequential PEFT with subspace-rotation metrics is new.
- **minimal_experiment:** Train task chains in multiple orders vs independent merging; measure per-task retention and adapter subspace rotations; relate rotation to retention loss.
- **main_risk:** Merging methods themselves add confounds; standardize on simple addition first.
- **cluster:** `peft_limits`

### W2-B-0118 — PEFT fails silently on minority subgroups: matched-average-accuracy LoRA models hide larger subgroup gaps than full fine-tuning.

- **problem:** PEFT evaluations report averages; constrained capacity plausibly allocates to majority patterns first, worsening subgroup equity invisibly.
- **core_hypothesis:** At matched average accuracy, LoRA models show systematically larger worst-group gaps than full FT, and the disparity grows as rank shrinks, revealing a capacity-fairness tradeoff.
- **why_important:** PEFT is used in resource-constrained settings serving diverse populations — exactly where silent subgroup failure matters most.
- **why_possibly_novel:** The rank-fairness relationship is unmeasured (UNVERIFIED — needs lit search).
- **minimal_experiment:** Evaluate worst-group metrics on subgroup-annotated benchmarks (Waterbirds-style, geographic segmentation data) across ranks and PEFT families at matched averages.
- **main_risk:** Subgroup annotations are scarce for dense tasks; may need to construct them.
- **cluster:** `peft_limits`

### W2-B-0119 — CoOp-style learned prompts overfit the class-name embedding neighborhood, and prompt length inversely predicts novel-class generalization.

- **problem:** Learned text prompts improve seen-class accuracy but their geometric relationship to class-name embeddings — and its cost on unseen classes — is uncharacterized.
- **core_hypothesis:** Learned prompt vectors drift toward seen-class name embeddings (measurable cosine migration), and longer prompts drift more, explaining the documented seen/unseen tradeoff via neighborhood capture rather than generic overfitting.
- **why_important:** A geometric account enables principled prompt-length selection and drift-penalized variants designed from measurement.
- **why_possibly_novel:** Embedding-space drift analysis of prompt tuning is new (base-to-new tradeoff itself is known).
- **minimal_experiment:** Track prompt-embedding trajectories during CoOp training across lengths; correlate drift metrics with novel-class degradation; test drift-constrained training.
- **main_risk:** Drift metrics in token space may not capture function-space effects; validate against outputs.
- **cluster:** `peft_limits`

### W2-B-0120 — Text-encoder LoRA transfers across visual domains better than vision-encoder LoRA for open-vocab dense tasks.

- **problem:** Adaptation effort defaults to the vision tower; but vision-side updates entangle domain specifics while text-side updates may capture domain-portable task structure.
- **core_hypothesis:** For open-vocabulary segmentation adapted on domain A and tested on domain B, text-side LoRA retains more transfer than vision-side LoRA at matched source performance, inverting the default allocation.
- **why_important:** Changes where the community spends its adaptation budget for cross-domain open-vocab systems.
- **why_possibly_novel:** Modality-side transferability comparison for dense adaptation is unexplored.
- **minimal_experiment:** Adapt CLIP-based segmenters with text-only/vision-only/both LoRA on one domain; evaluate cross-domain retention across several target domains at matched source metrics.
- **main_risk:** Results may depend on the shift being semantic vs photometric; stratify shifts.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0116

### W2-B-0121 — Adapter nonlinearities are unnecessary: linear adapters match nonlinear ones, showing adaptation is subspace realignment.

- **problem:** Adapter designs include nonlinearities by convention; if linear bottlenecks suffice, adaptation's nature (feature reuse vs feature creation) is clarified and architectures simplify.
- **core_hypothesis:** Across tasks and budgets, linear adapters reach parity with nonlinear ones, and their learned maps are near-rotations of existing feature subspaces rather than new feature constructors.
- **why_important:** A negative result about nonlinearity would simplify PEFT libraries and sharpen theory about what adaptation does.
- **why_possibly_novel:** A systematic linearity ablation with subspace analysis across vision tasks is missing (UNVERIFIED — needs lit search).
- **minimal_experiment:** Matched-budget linear vs nonlinear adapters on classification/segmentation/detection; analyze learned maps' spectra and alignment with pretrained subspaces.
- **main_risk:** Parity may fail exactly on the hardest shifts, which is itself the finding.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0106

### W2-B-0122 — Forgetting comparisons between PEFT and full FT reverse depending on whether readout is linear or dense.

- **problem:** "LoRA forgets less" is established with linear-probe or zero-shot evals; dense abilities may forget on a different schedule, making the claim readout-dependent.
- **core_hypothesis:** LoRA preserves image-level abilities better than full FT but preserves dense emergent abilities (correspondence, depth probes) no better or worse, because low-rank updates disproportionately disturb spatially-distributed representations.
- **why_important:** Forgetting claims guide method choice; if they are readout-artifacts, the guidance is wrong for dense users.
- **why_possibly_novel:** Readout-stratified forgetting audits are new.
- **minimal_experiment:** Adapt VFMs with LoRA/full-FT; evaluate retention across readout families (zero-shot, linear probe, dense probes, correspondence); test claim reversal.
- **main_risk:** Emergent-ability metrics are noisier; needs careful statistical treatment.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0102

### W2-B-0123 — Quantized-backbone LoRA concentrates its accuracy loss at boundary pixels in dense predictions.

- **problem:** QLoRA-style pipelines are validated on global metrics; quantization noise plausibly harms high-frequency spatial precision most, which mIoU under-reports.
- **core_hypothesis:** At matched mIoU loss, quantized-backbone adaptation shows disproportionate boundary-F1 degradation vs full-precision LoRA, localizing quantization damage spatially.
- **why_important:** Users choosing quantized adaptation for dense tasks need to know what they silently trade away.
- **why_possibly_novel:** Spatially-resolved quantization-damage analysis for PEFT is unexplored.
- **minimal_experiment:** Adapt at 4/8-bit vs fp16 backbones; decompose errors into boundary/interior; visualize damage maps; test whether boundary-aware loss reweighting compensates.
- **main_risk:** Boundary effects may be dataset-dependent; use several dense benchmarks.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0109

### W2-B-0124 — Dense-task LoRAs compose worse than classification LoRAs under task arithmetic, and composition error is predictable from subspace overlap.

- **problem:** Task-arithmetic merging of LoRAs is popular for classification; whether dense-task adapters combine linearly — and when they clash — is unknown.
- **core_hypothesis:** Merging error grows with the principal-angle overlap between adapter subspaces, and dense tasks (which demand higher rank) overlap more, explaining systematically worse dense composition.
- **why_important:** A predictive compatibility score would tell users which adapters can merge before trying.
- **why_possibly_novel:** Subspace-overlap-based composition theory for vision PEFT is untested.
- **minimal_experiment:** Train LoRAs for multiple dense/classification tasks; merge pairs; regress merged-model degradation on subspace principal angles; validate the compatibility score.
- **main_risk:** Overlap may be necessary but not sufficient for interference; include sign structure.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0117

### W2-B-0125 — PEFT hyperparameters tuned on small backbones transfer to large ones, but only within pretraining families.

- **problem:** PEFT sweeps on flagship models are expensive; the validity of small-model proxy tuning is assumed, never quantified, and its failure boundaries are unknown.
- **core_hypothesis:** Rank/LR/placement choices transfer from ViT-S to ViT-L with minor loss within a pretraining family (DINOv2 to DINOv2) but break across families (DINOv2-tuned settings on CLIP), because adaptation demand tracks pretraining geometry, not size.
- **why_important:** Establishes cheap, valid tuning protocols and warns against cross-family extrapolation.
- **why_possibly_novel:** Transferability boundaries of PEFT hyperparameters are unmapped.
- **minimal_experiment:** Full sweeps at small scale; deploy top configurations at large scale within/across families; quantify regret vs full large-scale sweeps.
- **main_risk:** Regret may be nonstationary across tasks; test several.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0115

### W2-B-0126 — LoRA's zero-initialized B matrix forces its first gradient step to coincide with full fine-tuning, and divergence timing predicts the final gap.

- **problem:** When and why LoRA's trajectory departs from full fine-tuning determines its adequacy, but the departure dynamics have never been measured.
- **core_hypothesis:** Function-space divergence between LoRA and full FT begins at a rank-dependent step count and grows monotonically; early divergence onset predicts the final performance gap, enabling a cheap early test of rank adequacy.
- **why_important:** A few hundred steps could reveal whether a rank will suffice, replacing full training runs in rank selection.
- **why_possibly_novel:** Divergence-onset analysis as a rank-adequacy predictor is new.
- **minimal_experiment:** Track prediction divergence between paired LoRA/full-FT runs across ranks/tasks; fit onset-vs-final-gap relationship; validate as early-stopping rank test.
- **main_risk:** Divergence may be non-monotone for some schedules; characterize exceptions.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0098

### W2-B-0127 — The data-size threshold where full fine-tuning overtakes PEFT scales with domain gap, forming a predictable 2D phase boundary.

- **problem:** "Use PEFT for small data" lacks quantitative boundaries; the interaction with domain gap is anecdotal.
- **core_hypothesis:** The crossover dataset size grows near-linearly with feature-space domain gap: close domains favor PEFT until large data, far domains favor full FT even at small data — yielding a usable phase diagram.
- **why_important:** A validated phase diagram is an immediately actionable decision tool for every adaptation project.
- **why_possibly_novel:** The joint (data size x domain gap) characterization does not exist (UNVERIFIED — needs lit search).
- **minimal_experiment:** Grid adaptation experiments across data sizes and domains ordered by measured gap; fit and cross-validate the phase boundary on held-out domains.
- **main_risk:** Boundary may depend on task type; build separate diagrams for dense vs global tasks.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0112

### W2-B-0128 — Prompt-tuning gradients vanish through frozen depth, capping what input-side PEFT can influence in deep VFMs.

- **problem:** Prompts adapt deep networks through long frozen backpropagation paths; the effective gradient signal reaching prompts from late-layer objectives may be structurally attenuated.
- **core_hypothesis:** Gradient norm at prompt tokens decays with backbone depth faster than for LoRA parameters, and prompt-tuning's relative underperformance grows with depth — explaining scale trends and motivating depth-resolved analysis rather than new methods.
- **why_important:** A structural account of when input-side PEFT is hopeless as models deepen.
- **why_possibly_novel:** Depth-resolved gradient-signal analysis comparing PEFT families is new.
- **minimal_experiment:** Measure prompt vs LoRA gradient statistics across backbone depths (ViT-S to g); correlate signal attenuation with performance gaps at matched budgets.
- **main_risk:** Attention shortcuts (CLS paths) may deliver gradient regardless; the measurement itself resolves this.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0105

### W2-B-0129 — In LoRA-per-domain libraries, retrieval failure — not adapter quality — dominates OOD error.

- **problem:** Adapter libraries route inputs to the best LoRA; end-to-end error attribution between routing and adaptation quality has not been performed.
- **core_hypothesis:** With oracle routing, LoRA libraries near-match per-domain upper bounds, but realistic feature-based routing misroutes OOD inputs at high rates, contributing the majority of the end-to-end gap.
- **why_important:** Redirects continual-PEFT research from better adapters to better routing/uncertainty.
- **why_possibly_novel:** Router-vs-adapter error decomposition for PEFT libraries is unexplored.
- **minimal_experiment:** Build domain-adapter libraries; evaluate with oracle vs learned routing on mixed-domain streams; decompose errors; test abstention-based routing.
- **main_risk:** Decomposition depends on domain granularity choices; test multiple partitions.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0117

### W2-B-0130 — Structured-LoRA variants owe their gains to parameter count, not structure, under strictly matched budgets.

- **problem:** A stream of structured low-rank variants claims superiority, but budget-matching is often loose (different effective capacities), leaving the structure-vs-count question open.
- **core_hypothesis:** Under strict trainable-parameter and FLOP matching, most structural variants collapse to vanilla LoRA performance, with surviving differences attributable to optimization conditioning rather than expressivity.
- **why_important:** A rigorous null result would refocus the PEFT field and set budget-matching standards for future claims.
- **why_possibly_novel:** Adversarially budget-matched meta-evaluation of PEFT structure claims is missing.
- **minimal_experiment:** Re-implement representative variants in one codebase; match budgets exactly; evaluate across vision tasks with multi-seed statistics; decompose remaining gaps via conditioning analysis.
- **main_risk:** Faithful re-implementation is laborious; results may draw dispute — pre-register protocols.
- **cluster:** `peft_limits`

### W2-B-0131 — IA3-style channel rescaling breaks feature-norm-based OOD detectors, creating a silent safety regression.

- **problem:** Deployed OOD detectors often rely on feature-norm statistics; multiplicative PEFT directly alters those statistics without changing semantics, a collision nobody has audited.
- **core_hypothesis:** After IA3 adaptation, norm-based OOD detection AUROC drops substantially even where accuracy improves, while gradient- and logit-based detectors survive — a method-detector compatibility matrix emerges.
- **why_important:** Safety tooling and adaptation methods are chosen independently today; documented incompatibilities would prevent silent monitoring failures.
- **why_possibly_novel:** PEFT-vs-OOD-detector interaction audits are new.
- **minimal_experiment:** Adapt with IA3/LoRA/BitFit; evaluate a battery of OOD detectors pre/post adaptation; publish the compatibility matrix with mechanistic explanations.
- **main_risk:** Detector implementations vary; standardize on open-source references.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0027

### W2-B-0132 — For low-level domain shifts, adapting only the patch-embedding stem outperforms distributed transformer LoRA at equal budget.

- **problem:** PEFT budgets are spread across transformer blocks; sensor-style shifts (noise, blur, spectral response) may be correctable at the input stem where they enter.
- **core_hypothesis:** Stem-only adaptation dominates block-distributed LoRA under photometric/sensor shifts, while the ordering reverses for semantic shifts — attributable to where shift-relevant computation lives.
- **why_important:** Matching adaptation locus to shift type is a cheap, general principle awaiting validation.
- **why_possibly_novel:** Stem-vs-blocks allocation as a function of shift type is untested.
- **minimal_experiment:** Adapt stem-only vs blocks-only vs mixed at matched budgets across shift-type-controlled benchmarks; map winning allocation per shift type.
- **main_risk:** Stems differ across architectures (conv vs linear patchify); test both.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0116

### W2-B-0133 — LoRA memorizes few-shot training examples at a higher per-parameter rate than full fine-tuning, inverting the privacy intuition.

- **problem:** Fewer trainable parameters suggests less memorization, but concentrating updates in a small subspace may make individual examples more extractable — the privacy calculus for PEFT is unmeasured.
- **core_hypothesis:** Membership-inference and reconstruction attacks succeed more per-trainable-parameter against LoRA than full FT in few-shot regimes, and attack success concentrates in the adapter subspace.
- **why_important:** PEFT is the default for sensitive-domain few-shot adaptation (medical); its privacy profile must be established.
- **why_possibly_novel:** Per-parameter memorization accounting for PEFT is new (UNVERIFIED — needs lit search).
- **minimal_experiment:** Run membership-inference and data-extraction attacks on LoRA vs full-FT models across shot counts; normalize by parameter budget; localize memorization to subspaces.
- **main_risk:** Attack strength varies; use multiple state-of-practice attacks.
- **cluster:** `peft_limits`

### W2-B-0134 — Seed-ensembles of LoRAs lack the diversity that makes full-model ensembles work, capping their uncertainty value.

- **problem:** Ensembling cheap LoRAs is an appealing substitute for deep ensembles, but shared frozen backbones may collapse functional diversity where it matters (OOD).
- **core_hypothesis:** LoRA ensembles show near-full-ensemble ID gains but a small fraction of the OOD disagreement diversity, because diversity requires differing feature extractors, not differing readout subspaces.
- **why_important:** Quantifies the limits of a tempting cheap-uncertainty recipe before the community adopts it blindly.
- **why_possibly_novel:** Diversity-accounting comparisons between PEFT and full ensembles are missing.
- **minimal_experiment:** Build LoRA-seed and full-FT-seed ensembles at matched member counts; measure ID/OOD accuracy, disagreement diversity, and calibration; decompose where diversity is lost.
- **main_risk:** Diversity metrics are contested; report several (disagreement, KL, feature CKA).
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0108

### W2-B-0135 — Pre-attention and post-MLP adapter placements are functionally dissociable: one changes where the model looks, the other what it represents.

- **problem:** Adapter placement is treated as an accuracy knob; if placements causally control distinct functions (attention routing vs feature content), placement becomes a scientific instrument.
- **core_hypothesis:** Pre-attention adapters change attention maps with minimal feature-content change (and help re-localization tasks), while post-MLP adapters do the reverse (and help re-labeling tasks) — a double dissociation testable across task pairs.
- **why_important:** Gives PEFT a mechanistic dimension, letting practitioners target the function their task needs.
- **why_possibly_novel:** Function-level dissociation of placement effects is unexplored.
- **minimal_experiment:** Adapt with placement-restricted adapters on tasks needing re-localization (shifted domains) vs re-labeling (new taxonomies); measure attention-map and feature-content drift separately; test the dissociation.
- **main_risk:** Effects may mix in deep stacks; use layer-local analyses.
- **cluster:** `peft_limits`
- **mutate_from:** W2-B-0103

---

## 5. Catastrophic forgetting when adapting VFMs to segmentation/detection

Cluster key: `catastrophic_forgetting`

### W2-B-0136 — Most "catastrophic forgetting" in VFM adaptation is feature rotation, not erasure, recoverable by re-fitting readouts.

- **problem:** Forgetting is measured through fixed heads or zero-shot templates, conflating lost information with misaligned readout geometry.
- **core_hypothesis:** After segmentation fine-tuning, re-fitting a linear probe on the old task recovers the majority of the apparent forgetting, and the unrecoverable residue — true erasure — is small and layer-localized.
- **why_important:** Redefines what forgetting means operationally and redirects mitigation from weight protection to readout re-alignment.
- **why_possibly_novel:** Rotation-vs-erasure decomposition with recoverability accounting for VFM dense adaptation is not standard (UNVERIFIED — needs lit search).
- **minimal_experiment:** Fine-tune CLIP/DINOv2 on segmentation; measure old-task performance via frozen head vs re-fitted probes per layer; report recoverable vs permanent components.
- **main_risk:** Probe re-fitting uses old-task data, which strict continual settings forbid; frame as measurement, not method.
- **cluster:** `catastrophic_forgetting`

### W2-B-0137 — Forgetting can be the desired outcome: losing typographic-attack susceptibility during dense adaptation is a measurable benefit.

- **problem:** All forgetting is treated as harm; adaptation might beneficially shed pretraining pathologies (typographic sensitivity, spurious text-region attention).
- **core_hypothesis:** Segmentation fine-tuning of CLIP-derived models reduces typographic-attack success significantly, and the reduction correlates with forgetting of OCR-adjacent abilities — a beneficial-forgetting trade.
- **why_important:** Introduces "curated forgetting" as an adaptation objective, reframing part of the forgetting literature.
- **why_possibly_novel:** Beneficial-forgetting accounting during VFM adaptation is unexplored.
- **minimal_experiment:** Track typographic-attack success, OCR probes, and standard abilities during fine-tuning; map which pathologies die, when, and at what cost to useful abilities.
- **main_risk:** Pathology and ability may be entangled (text reading is sometimes wanted); quantify the entanglement.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0049

### W2-B-0138 — Forgetting is class-asymmetric: classes visually similar to the new task's classes are forgotten first, not last.

- **problem:** Intuition suggests similar old classes benefit from positive transfer; interference theory predicts the opposite — similarity-driven overwriting.
- **core_hypothesis:** Zero-shot accuracy loss per old class correlates positively with feature-space similarity to new-task classes, supporting interference over transfer at the class level.
- **why_important:** Predictable forgetting patterns enable targeted rehearsal of exactly the at-risk classes.
- **why_possibly_novel:** A similarity-forgetting curve for VFM adaptation has not been fitted.
- **minimal_experiment:** Fine-tune on domain-specific segmentation; measure per-class zero-shot degradation across hundreds of classes; regress on class-to-task feature similarity.
- **main_risk:** Similarity metrics choice may drive conclusions; use several embeddings.
- **cluster:** `catastrophic_forgetting`

### W2-B-0139 — Dense adaptation forgets global semantics before local geometry, exhibiting an ordered dissociation.

- **problem:** Forgetting is tracked with one number; if ability families decay at different rates, mitigation timing and early-warning signals should target the fastest-decaying family.
- **core_hypothesis:** During segmentation fine-tuning, image-level retrieval/classification abilities decay earlier and faster than correspondence/depth-probe abilities, establishing a reproducible forgetting order.
- **why_important:** A forgetting timetable lets practitioners stop or checkpoint before the abilities they care about degrade.
- **why_possibly_novel:** Ability-resolved forgetting chronologies are unmeasured.
- **minimal_experiment:** Checkpoint densely during fine-tuning; evaluate ability battery (retrieval, classification, correspondence, depth probes) per checkpoint; fit decay onset/rate per ability across seeds.
- **main_risk:** Ability metrics differ in sensitivity; normalize via effect sizes.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0136

### W2-B-0140 — Zero-shot retrieval degrades before zero-shot classification during dense fine-tuning, forming a forgetting cascade with early-warning value.

- **problem:** Practitioners monitor task loss and maybe one retention metric; ordered cascades would provide leading indicators of impending broader forgetting.
- **core_hypothesis:** Retrieval retention drops measurably earlier than classification retention across tasks and learning rates, and the lag is stable enough to serve as an early-warning signal.
- **why_important:** A validated canary metric allows automatic intervention (LR cuts, early stop) before valuable abilities are lost.
- **why_possibly_novel:** Cross-ability lead-lag structure of forgetting is undocumented.
- **minimal_experiment:** Fine-tune with dense checkpointing; compute lead-lag between retrieval and classification retention curves across configurations; validate canary-triggered interventions.
- **main_risk:** The order might reverse for some task types; map exceptions.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0139

### W2-B-0141 — Distilling features only on non-task classes prevents forgetting better than uniform distillation at equal compute.

- **problem:** Feature-distillation regularizers treat all inputs equally, wasting capacity protecting representations the new task will legitimately reshape.
- **core_hypothesis:** Restricting distillation loss to inputs/classes disjoint from the new task preserves old abilities better and hurts new-task learning less than uniform distillation, at matched regularization budgets.
- **why_important:** A targeting principle for rehearsal-free continual adaptation, applicable to any distillation-based mitigation.
- **why_possibly_novel:** Task-disjoint targeting of distillation for VFM adaptation is untested.
- **minimal_experiment:** Compare uniform vs disjoint-targeted feature distillation during segmentation adaptation; measure retention/new-task frontiers across regularization strengths.
- **main_risk:** Defining "disjoint" needs care when class overlap is partial; use similarity-weighted variants.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0138

### W2-B-0142 — Weight-space movement does not predict functional forgetting: the two measures dissociate across layers and runs.

- **problem:** Forgetting mitigation often minimizes weight change (EWC-style), assuming weight distance proxies functional loss — an assumption rarely validated for VFMs.
- **core_hypothesis:** Across runs, correlation between per-layer weight delta and old-task functional loss is weak; some large-delta runs retain abilities (rotation within null space) while small-delta runs lose them (sensitive-direction hits).
- **why_important:** Undermines the foundation of weight-anchored continual methods for VFMs and motivates function-space alternatives.
- **why_possibly_novel:** A systematic weight-vs-function forgetting dissociation study for VFM adaptation is missing.
- **minimal_experiment:** Generate many fine-tuning runs; regress functional retention on weight-delta statistics (norms, layer profiles, subspace alignment); identify dissociation cases.
- **main_risk:** Aggregate statistics may hide predictive substructure; include subspace-resolved features.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0084

### W2-B-0143 — Weight interpolation recovers zero-shot classification but not emergent dense abilities, exposing asymmetric recoverability.

- **problem:** WiSE-FT-style interpolation is celebrated for restoring robustness/zero-shot metrics; whether it restores dense emergent abilities (correspondence, depth probes) is untested.
- **core_hypothesis:** Along the interpolation path, classification retention recovers smoothly while dense emergent abilities recover non-monotonically or incompletely, because they depend on coordinated multi-layer structure that averaging disrupts.
- **why_important:** Warns dense-ability users that the standard cheap fix does not cover them; motivates ability-resolved interpolation studies.
- **why_possibly_novel:** Ability-family-resolved interpolation analysis is new.
- **minimal_experiment:** Sweep interpolation coefficients for tuned VFMs; evaluate ability battery per point; compare recovery completeness and monotonicity across families.
- **main_risk:** Emergent-ability metrics are noisy; use large probe sets.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0139

### W2-B-0144 — Tuning only the vision tower still breaks the text tower functionally: joint-space drift makes frozen weights insufficient for retention.

- **problem:** Practitioners freeze the text encoder assuming its abilities are preserved; but retention depends on cross-modal alignment, which vision-side drift destroys unilaterally.
- **core_hypothesis:** After vision-only fine-tuning, text-side tasks executed through the joint space (retrieval, open-vocab matching) degrade nearly as much as under joint tuning, demonstrating "frozen but broken" and a drift-based account of multimodal forgetting.
- **why_important:** Corrects a widespread false sense of safety in partial-freezing strategies for multimodal models.
- **why_possibly_novel:** Unilateral-drift quantification of joint-space forgetting is underexplored.
- **minimal_experiment:** Fine-tune vision tower only; track joint-space alignment metrics and cross-modal task retention vs joint-tuning and text-only controls.
- **main_risk:** Some retention loss may be recoverable by re-aligning projections; measure recoverable share.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0074

### W2-B-0145 — Calibration is forgotten before accuracy: confidence quality decays earlier under adaptation than task performance.

- **problem:** Retention monitoring tracks accuracy-like metrics; if calibration decays first, deployed models pass retention checks while becoming untrustworthy.
- **core_hypothesis:** Old-task ECE degrades at substantially lower fine-tuning doses than old-task accuracy, across tasks and methods, making calibration the leading edge of forgetting.
- **why_important:** Adds a required metric to every continual-adaptation evaluation and enables earlier intervention.
- **why_possibly_novel:** Calibration-first forgetting ordering is undocumented (UNVERIFIED — needs lit search).
- **minimal_experiment:** Track old-task accuracy and ECE across fine-tuning trajectories for multiple adaptation methods; compare degradation onset doses; test whether temperature re-tuning restores calibration.
- **main_risk:** ECE estimation noise may blur onset detection; use proper scoring rules too.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0140

### W2-B-0146 — Small learning rates do not prevent forgetting — they postpone it beyond typical evaluation horizons.

- **problem:** "Use a small LR to avoid forgetting" is standard advice validated on short runs; the long-horizon fate is unmeasured.
- **core_hypothesis:** At matched final new-task accuracy, small-LR long runs forget as much as large-LR short runs; forgetting is governed by cumulative update magnitude, yielding a dose-response law rather than an LR threshold.
- **why_important:** Replaces a misleading heuristic with a quantitative forgetting-dose model practitioners can budget against.
- **why_possibly_novel:** Dose-equivalence analysis of LR vs training length for forgetting is new.
- **minimal_experiment:** Grid LR x steps to matched new-task accuracy; measure retention along trajectories; fit forgetting as a function of cumulative displacement vs LR alone.
- **main_risk:** Optimizer adaptivity distorts naive dose measures; use function-space displacement.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0095

### W2-B-0147 — Task-order asymmetry in dense adaptation: segmentation-then-detection forgets differently than detection-then-segmentation.

- **problem:** Continual evaluation averages over orders or uses one; directional transfer/forgetting structure between dense task pairs is unmapped.
- **core_hypothesis:** The forgetting matrix over dense tasks is strongly asymmetric — localization-heavy tasks protect later semantic tasks more than the reverse — and asymmetry is predictable from representation-overlap measurements.
- **why_important:** Order-aware curricula for multi-stage adaptation pipelines could be designed from the matrix.
- **why_possibly_novel:** A dense-task forgetting matrix with overlap-based prediction is missing.
- **minimal_experiment:** Run all order pairs among segmentation/detection/depth/edges with matched budgets; measure directional forgetting; regress on representational-overlap metrics.
- **main_risk:** Head architectures confound task effects; standardize minimal heads.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0090

### W2-B-0148 — PEFT forgetting is stored in adapted layers but expressed in later frozen layers, mislocating where damage "lives".

- **problem:** Forgetting localization assumes damaged layers are where behavior changes; with PEFT, the causal locus (adapter site) and expression locus (downstream computation) may split.
- **core_hypothesis:** Activation-patching shows old-task behavior is disrupted at layers downstream of adapters even though those layers are frozen, meaning locality claims about PEFT damage are systematically misattributed.
- **why_important:** Correct localization matters for targeted repairs and for interpreting probing studies of continual learning.
- **why_possibly_novel:** Causal patching for forgetting localization in PEFT-adapted VFMs is new.
- **minimal_experiment:** Patch clean activations layer-by-layer into adapted models on old-task inputs; identify repair points; compare with adapter placement sites.
- **main_risk:** Patching off-manifold artifacts; use paired-input patching protocols.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0122

### W2-B-0149 — Generated pretraining-proxy data can replace real data for rehearsal, up to a measurable realism threshold.

- **problem:** Rehearsal needs pretraining-like data that is often unavailable (licenses, privacy); whether synthetic proxies suffice, and what fidelity they need, is unquantified.
- **core_hypothesis:** Rehearsal with diffusion-generated proxy data prevents forgetting comparably to real data until a measurable distributional distance threshold, beyond which protection collapses nonlinearly.
- **why_important:** Makes rehearsal practical in data-restricted settings and defines generator requirements.
- **why_possibly_novel:** A realism-threshold law for synthetic rehearsal in VFM adaptation is untested.
- **minimal_experiment:** Rehearse with generated data at varied fidelity (guidance scales, model sizes); measure retention vs distributional-distance metrics; locate protection thresholds.
- **main_risk:** Distributional distance metrics may not capture the protective factor; test several.
- **cluster:** `catastrophic_forgetting`

### W2-B-0150 — Corruption robustness is forgotten faster than clean accuracy, leaving adapted models silently brittle.

- **problem:** Retention checks use clean data; robustness — a distinct, expensively-acquired property of VFMs — may decay on its own faster schedule.
- **core_hypothesis:** Under dense fine-tuning, corruption-robustness retention decays at a higher rate than clean-accuracy retention across corruption families, and the differential is larger for full FT than PEFT.
- **why_important:** Deployment under real conditions depends on robustness; its silent loss is a hidden cost of adaptation that must enter evaluation practice.
- **why_possibly_novel:** Robustness-vs-clean differential forgetting rates are unmeasured.
- **minimal_experiment:** Track clean and corrupted old-task metrics along fine-tuning trajectories; fit per-property decay rates; compare adaptation methods.
- **main_risk:** Corruption benchmarks partially overlap fine-tuning augmentations; control augmentation recipes.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0139

### W2-B-0151 — Forgetting CLIP's text-reading ability during dense adaptation causally changes scene-text region segmentation behavior.

- **problem:** CLIP models read text in images; dense adaptation may destroy this, with unknown consequences for how text regions are segmented (as text? as background? as objects?).
- **core_hypothesis:** As OCR-probe performance decays during fine-tuning, segmentation behavior on text-bearing regions shifts measurably (from semantic-text grouping toward texture grouping), demonstrating a functional consequence of ability loss.
- **why_important:** Documents how the loss of one emergent ability reshapes dense outputs — a concrete case study of forgetting's downstream anatomy.
- **why_possibly_novel:** Linking specific ability decay to dense output behavior change is new.
- **minimal_experiment:** Track OCR probes and text-region segmentation phenotypes across fine-tuning checkpoints; correlate decay curves with phenotype transitions.
- **main_risk:** Phenotype metrics need careful design; pilot on curated text-heavy scenes.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0137

### W2-B-0152 — Emergent-ability forgetting is abrupt while benchmark-task forgetting is gradual, indicating phase-transition loss dynamics.

- **problem:** Forgetting curves are assumed smooth; abilities resting on precise multi-layer coordination might collapse discontinuously, invalidating checkpoint-interpolation safety assumptions.
- **core_hypothesis:** Abilities like zero-shot correspondence show step-like collapse within narrow fine-tuning windows, while linear-probe accuracies decay smoothly — two distinct loss dynamics classes.
- **why_important:** Abrupt loss means sparse checkpointing can silently jump over the last good model; dynamics classes dictate monitoring density.
- **why_possibly_novel:** Loss-dynamics taxonomy (abrupt vs gradual) for VFM abilities is unexplored.
- **minimal_experiment:** Ultra-dense checkpointing across fine-tuning; classify per-ability decay curves by abruptness statistics; test reproducibility of collapse points across seeds.
- **main_risk:** Apparent abruptness may be metric thresholding; use continuous underlying scores.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0140

### W2-B-0153 — Fisher-importance estimates computed on proxy data misidentify which VFM weights matter, breaking EWC-style protection.

- **problem:** Importance-weighted protection needs pretraining data that VFM users lack; proxy-data importance estimates' validity is assumed, not measured.
- **core_hypothesis:** Importance maps estimated on proxy corpora diverge substantially from those on true pretraining-like data, and protection using proxy maps preserves the wrong abilities — quantifying a fundamental practicality gap of importance-based methods for VFMs.
- **why_important:** A negative result would redirect continual-VFM work away from importance weighting toward data-free alternatives.
- **why_possibly_novel:** Proxy-validity analysis of importance estimation for VFMs is missing.
- **minimal_experiment:** Compare Fisher maps across data sources (LAION-like, ImageNet, task data); run EWC with each; measure which abilities each protects; quantify map-divergence-to-protection-failure relationship.
- **main_risk:** True pretraining data is inaccessible for some models; use models with open data.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0142

### W2-B-0154 — Decoder capacity governs backbone forgetting: heavy heads let backbones stay intact, linear heads force destructive rewriting.

- **problem:** The head architecture used during adaptation is chosen for accuracy, ignoring its causal effect on how much the backbone must change — and thus forget.
- **core_hypothesis:** At matched new-task performance, backbone forgetting decreases monotonically with head capacity, because expressive heads absorb task-specific computation; a head-capacity dial trades new-task parameter cost against retention.
- **why_important:** Reframes head design as a forgetting-control mechanism, not just an accuracy choice.
- **why_possibly_novel:** The head-capacity-to-backbone-forgetting law is unquantified (UNVERIFIED — needs lit search).
- **minimal_experiment:** Adapt VFMs to segmentation with heads from linear to heavy decoders at matched final mIoU; measure backbone drift and old-ability retention across head capacities.
- **main_risk:** Matching final performance across head classes requires careful budget tuning.
- **cluster:** `catastrophic_forgetting`

### W2-B-0155 — Adding a self-supervised objective during adaptation anchors representations better than distillation at equal compute.

- **problem:** Forgetting mitigation relies on distilling from a frozen teacher; re-running the original SSL objective on new data is an alternative anchor whose comparative value is untested.
- **core_hypothesis:** Joint task-plus-MAE (or task-plus-DINO) training preserves transferable abilities better than feature distillation at matched compute, because the objective anchors the representation's function rather than its values.
- **why_important:** Objective-based anchoring needs no teacher inference and may become the default retention tool.
- **why_possibly_novel:** Objective-anchoring vs value-distillation comparison for VFM adaptation is missing.
- **minimal_experiment:** Adapt with task-only, task+distillation, task+SSL objectives at matched budgets; evaluate retention battery and new-task metrics; analyze representational drift under each anchor.
- **main_risk:** SSL objectives on small task data may behave pathologically; monitor for collapse.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0141

### W2-B-0156 — Re-grafting the original patch-embedding layer onto a fine-tuned backbone recovers a surprising share of zero-shot loss.

- **problem:** Which layers' changes cause zero-shot degradation is unknown; the earliest layers are candidates because all downstream computation depends on their output statistics.
- **core_hypothesis:** Replacing only the fine-tuned patch-embed (and possibly first block) with pretrained weights recovers a large fraction of zero-shot retention at modest new-task cost, localizing forgetting's chokepoint at the input interface.
- **why_important:** A one-layer swap is the cheapest conceivable mitigation; even partial success would be widely adopted and mechanistically informative.
- **why_possibly_novel:** Layer re-grafting as forgetting archaeology is unexplored.
- **minimal_experiment:** Systematically re-graft pretrained layers (singly and cumulatively) into adapted models; measure retention/new-task tradeoff per graft site; identify chokepoint layers.
- **main_risk:** Grafted layers may be incompatible with adapted downstream weights; measure interface mismatch.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0148

### W2-B-0157 — A measurable share of reported zero-shot "forgetting" is prompt-template staleness, recoverable without touching weights.

- **problem:** Zero-shot retention is measured with pretraining-era templates; fine-tuning shifts feature geometry so old templates misalign — inflating forgetting estimates.
- **core_hypothesis:** Re-optimizing text prompts (templates or lightweight prompt search) on the adapted model recovers several points of apparent zero-shot loss, and the recoverable share grows with fine-tuning dose, biasing forgetting literature upward.
- **why_important:** Corrects measurement practice across the continual-adaptation literature.
- **why_possibly_novel:** Template-staleness accounting in forgetting measurement is new.
- **minimal_experiment:** After adaptation, re-search templates on held-out classes; decompose zero-shot loss into template-recoverable vs weight-intrinsic components across doses and methods.
- **main_risk:** Template re-search can overfit evaluation classes; use strict class splits.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0136

### W2-B-0158 — Dense adaptation improves zero-shot recognition of localization-dependent classes: forgetting is not monotone harm.

- **problem:** Retention studies aggregate over classes, potentially hiding classes that benefit from dense tuning (those whose recognition needs precise spatial features).
- **core_hypothesis:** A reproducible subset of classes (fine-grained, small-object, texture-boundary-defined) shows improved zero-shot accuracy after segmentation fine-tuning, and the subset is predictable from localization-dependence scores.
- **why_important:** Positive backward transfer changes the cost-benefit calculus of adaptation and identifies what dense training adds to recognition.
- **why_possibly_novel:** Class-level positive backward transfer from dense tuning is undocumented.
- **minimal_experiment:** Measure per-class zero-shot deltas after segmentation fine-tuning across many classes; predict beneficiaries from localization-dependence features; replicate across backbones.
- **main_risk:** Multiple-comparison artifacts across many classes; use replication and corrections.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0138

### W2-B-0159 — Forgetting is non-monotonic in new-task dataset size: mid-sized datasets distort pretrained features most.

- **problem:** Intuition says more adaptation data causes more forgetting; but tiny datasets overfit heads while mid-sized ones reshape backbones, and large ones may re-regularize — the shape is unmeasured.
- **core_hypothesis:** Retention as a function of adaptation-set size is U-shaped: minimal forgetting at very small and very large sizes, maximal in a middle regime where backbone rewriting is worthwhile but data diversity cannot constrain it.
- **why_important:** Identifies the most dangerous data regime for adaptation — likely the most common one in practice.
- **why_possibly_novel:** The dataset-size-to-forgetting curve has not been mapped.
- **minimal_experiment:** Adapt across a size ladder (100 to 500k images) with matched schedules; measure retention battery per size; test U-shape and locate the danger zone.
- **main_risk:** Schedule matching across sizes is subtle; use both epoch-matched and step-matched controls.
- **cluster:** `catastrophic_forgetting`

### W2-B-0160 — A sparse mask of trainable weights exists that adapts VFMs to segmentation with near-zero measurable forgetting.

- **problem:** Whether forgetting is intrinsic to adaptation or an artifact of unconstrained parameterization is open; an existence proof of forgetting-free sparse adaptation would settle it.
- **core_hypothesis:** Lottery-style search finds masks (under 5% of weights) achieving within 2% of full fine-tuning on segmentation while keeping the retention battery at pretrained levels — demonstrating forgetting is avoidable in principle, at search cost.
- **why_important:** Separates fundamental stability-plasticity limits from parameterization artifacts, calibrating what mitigation methods should aspire to.
- **why_possibly_novel:** Forgetting-free existence proofs via mask search on VFMs are unexplored.
- **minimal_experiment:** Iterative magnitude/gradient-based mask search with retention constraints on DINOv2-to-ADE20K adaptation; report the achievable frontier vs mask sparsity.
- **main_risk:** Search is expensive and may fail — a bounded negative result still bounds the frontier.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0142

### W2-B-0161 — In continual detection adaptation, forgetting concentrates in query/objectness pathways, not the backbone.

- **problem:** Continual-detection studies treat the detector as a monolith; localizing forgetting among backbone, neck, and query/objectness components would target mitigation where it matters.
- **core_hypothesis:** Component-wise re-grafting shows most cross-domain forgetting in detection lives in query embeddings and objectness calibration, with backbone features remaining largely domain-general.
- **why_important:** Component-targeted retention (protect or replay only small components) would be far cheaper than whole-model methods.
- **why_possibly_novel:** Component-resolved forgetting attribution for detection adaptation is missing.
- **minimal_experiment:** Sequential domain adaptation of DETR-style detectors; re-graft components across time-points; attribute retention loss per component; test component-only rehearsal.
- **main_risk:** Component boundaries blur with end-to-end training; use activation-patching validation.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0156

### W2-B-0162 — Protecting class-selective neurons during adaptation trades plasticity for retention along a measurable frontier.

- **problem:** Weight-importance protection operates blindly; neuron-level functional identification (class-selective units) offers a semantically-targeted protection whose costs are unquantified.
- **core_hypothesis:** Freezing or regularizing the most class-selective units preserves those classes' zero-shot ability at a measurable, superlinear cost to new-task plasticity — mapping a protection-plasticity frontier that blind methods cannot reach.
- **why_important:** Establishes whether interpretability-guided protection beats statistical importance weighting.
- **why_possibly_novel:** Selectivity-guided protection with frontier analysis is new for VFMs.
- **minimal_experiment:** Identify class-selective units via probing; protect varying fractions during segmentation adaptation; trace retention-vs-plasticity frontiers against EWC baselines.
- **main_risk:** Distributed representations may make unit-level protection ineffective — informative either way.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0153

### W2-B-0163 — In-distribution retention probes systematically underestimate forgetting; OOD probes reveal hidden damage.

- **problem:** Retention is audited on the old task's standard test set; damage may concentrate off-distribution where representations lost their pretraining-endowed margin.
- **core_hypothesis:** Models passing ID retention checks show substantially larger degradation on OOD variants of the same old tasks, and the ID-OOD retention gap widens with fine-tuning dose — meaning current audits are biased optimistic.
- **why_important:** Changes evaluation standards for every continual-learning claim on foundation models.
- **why_possibly_novel:** Retention-audit bias quantification is unexplored.
- **minimal_experiment:** Build ID and OOD retention probe pairs (same task, shifted inputs); track both along adaptation trajectories; quantify audit bias across methods and doses.
- **main_risk:** OOD probe construction must avoid conflating shift difficulty with forgetting; use pretrained-model-normalized scores.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0150

### W2-B-0164 — Relearning speed (savings) reveals memory that retention metrics miss: forgotten abilities are cheaper to restore than to learn.

- **problem:** Retention metrics treat lost performance as gone; psychology's savings paradigm suggests latent memory persists, measurable through relearning efficiency — never applied to VFM forgetting.
- **core_hypothesis:** Re-acquiring a forgotten ability requires far fewer examples than learning it from a never-trained control, and savings percentage decays with fine-tuning dose much slower than raw retention — providing a deeper memory measure.
- **why_important:** Savings-based measurement changes forgetting theory (storage vs retrieval failure) and practice (cheap ability restoration).
- **why_possibly_novel:** The savings paradigm has not been ported to foundation-model forgetting (UNVERIFIED — needs lit search).
- **minimal_experiment:** After adaptation, relearn old abilities with few-shot budgets; compare against matched never-pretrained controls; fit savings curves vs fine-tuning dose.
- **main_risk:** Constructing fair never-trained controls is hard; use scratch heads on matched architectures.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0136

### W2-B-0165 — Layer-wise optimal interpolation coefficients form a reproducible "forgetting fingerprint" localizing where damage lives.

- **problem:** Uniform weight interpolation (single coefficient) treats all layers equally; the per-layer optimal profile is unknown and would reveal forgetting's spatial structure in the network.
- **core_hypothesis:** Optimizing per-layer interpolation coefficients between pretrained and adapted weights yields profiles that are stable across seeds, differ by task type, and outperform uniform interpolation on the retention-performance frontier.
- **why_important:** The fingerprint doubles as diagnosis (where forgetting lives) and treatment (better merging), advancing both theory and tools.
- **why_possibly_novel:** Layer-resolved interpolation profiling as forgetting cartography is new.
- **minimal_experiment:** Optimize per-layer coefficients on small validation sets across tasks/seeds; analyze profile structure; compare frontiers vs uniform WiSE-FT-style merging.
- **main_risk:** Per-layer optimization can overfit small validation sets; use cross-validation and profile regularization.
- **cluster:** `catastrophic_forgetting`
- **mutate_from:** W2-B-0143

---

## 6. Prompt learning / prompt sensitivity in VLMs and promptable segmenters

Cluster key: `prompt_sensitivity`

### W2-B-0166 — Mask variance under small point-prompt jitter is an intrinsic instability metric that predicts real-user disagreement.

- **problem:** Promptable segmenters are evaluated at benchmark-chosen prompts; sensitivity to the few-pixel jitter real users produce is unquantified as a first-class metric.
- **core_hypothesis:** Output variance under 5-pixel prompt jitter varies widely across images and models, correlates with boundary complexity, and predicts disagreement rates when real users prompt the same targets.
- **why_important:** An instability score per image/model would let interactive systems warn users or request extra clicks exactly when needed.
- **why_possibly_novel:** Jitter-variance as a validated proxy for human-prompt robustness is new (UNVERIFIED — needs lit search).
- **minimal_experiment:** Systematically jitter prompts on SAM-like interfaces; compute mask variance; collect small real-user prompt sets; validate the variance-to-disagreement correlation.
- **main_risk:** User behavior may differ from isotropic jitter; model empirical click distributions.
- **cluster:** `prompt_sensitivity`

### W2-B-0167 — Multi-point prompt order changes segmentation outputs even though point sets are order-free, revealing sequence artifacts.

- **problem:** Prompt encoders often process points sequentially or with positional structure; whether logically-equivalent prompt permutations yield identical masks is untested.
- **core_hypothesis:** Permuting identical point sets changes output masks at measurable rates, and the effect grows with point count — a formal invariance violation quantifying interface unreliability.
- **why_important:** Order artifacts make interactive systems irreproducible and complicate evaluation; documenting them forces interface fixes.
- **why_possibly_novel:** Permutation-invariance audits for prompt interfaces are unexplored.
- **minimal_experiment:** Evaluate mask agreement across all permutations of 2-6 point prompts on standard benchmarks and models; report violation rates and their correlates.
- **main_risk:** Some implementations are trivially invariant; the audit's value is the cross-model comparison.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0166

### W2-B-0168 — Most of prompt-template engineering's gain is a calibration effect reproducible by temperature adjustment.

- **problem:** Template ensembling and prompt engineering improve zero-shot metrics; whether gains reflect better representations or merely better-calibrated logit scales is unresolved.
- **core_hypothesis:** A large fraction of template-ensembling gains is matched by per-class temperature/bias calibration on the single default template, showing prompts act substantially as calibration knobs.
- **why_important:** Would demystify prompt engineering and replace expensive prompt searches with cheap post-hoc calibration where equivalent.
- **why_possibly_novel:** A calibration-decomposition of prompt-engineering gains is missing.
- **minimal_experiment:** Decompose template-ensemble improvements into ranking changes vs calibration changes; compare against calibrated single-template baselines across tasks including dense.
- **main_risk:** Dense tasks may show true ranking effects; the decomposition itself is the contribution.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0060

### W2-B-0169 — Negative (background) points harm interactive segmentation beyond a small count, inverting the more-information-helps assumption.

- **problem:** Interactive protocols assume added background clicks monotonically refine masks; the actual dose-response of negative prompts is uncharacterized.
- **core_hypothesis:** Beyond 2-3 negative points, additional background clicks degrade mask quality on average — because negative prompts over-constrain ambiguous regions — with the degradation onset predictable from object-background feature similarity.
- **why_important:** Interactive UX guidelines and simulated-user evaluation protocols both depend on the true dose-response curve.
- **why_possibly_novel:** Negative-prompt dose-response analysis is unexplored.
- **minimal_experiment:** Sweep positive/negative point counts factorially with simulated and human clicks; fit response surfaces per model; test similarity-based onset prediction.
- **main_risk:** Click-placement policy strongly affects curves; use multiple policies including human data.
- **cluster:** `prompt_sensitivity`

### W2-B-0170 — Prompt-perturbation variance is a better-calibrated uncertainty signal than model confidence for promptable segmenters.

- **problem:** Promptable models output confidence scores of dubious calibration; the ensemble-over-prompts view of uncertainty is unvalidated.
- **core_hypothesis:** Variance over perturbed prompts (jittered points, paraphrased text) predicts mask error better than native confidence across models and shifts, and the two signals fail in complementary regimes.
- **why_important:** A free uncertainty upgrade for every interactive pipeline, plus a characterization of when each signal fails.
- **why_possibly_novel:** Prompt-ensemble uncertainty validated against native confidence for dense outputs is new.
- **minimal_experiment:** Compare error-prediction AUROC of native confidence vs prompt-perturbation variance on ID and shifted data; analyze complementarity; test combined estimators.
- **main_risk:** Perturbation ensembles cost extra inference; quantify the compute-quality tradeoff.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0166

### W2-B-0171 — Learned prompts amplify distribution-shift damage: under shift, tuned prompts underperform handcrafted ones they beat in-distribution.

- **problem:** Prompt tuning is evaluated in-distribution; learned prompts encode dataset-specific geometry that may invert their advantage under shift — a safety-relevant reversal never mapped.
- **core_hypothesis:** The performance ordering of learned vs handcrafted prompts reverses at a measurable shift magnitude, and reversal severity correlates with prompt-embedding distance from the natural-language token manifold.
- **why_important:** Prompt tuning is deployed as harmless; a documented reversal boundary would change deployment guidance.
- **why_possibly_novel:** Shift-conditional reversal analysis of prompt tuning is missing.
- **minimal_experiment:** Evaluate CoOp-style vs template prompts across graded shifts; locate reversal points; regress severity on prompt off-manifold distance.
- **main_risk:** Reversal may be task-dependent; map which task families exhibit it.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0119

### W2-B-0172 — Replacing class names with definitions collapses dense performance while classification survives, showing names act as dense anchors.

- **problem:** Open-vocab systems assume the text encoder distributes meaning across phrasings; whether dense pathways depend disproportionately on name tokens (vs descriptive content) is unknown.
- **core_hypothesis:** Definition-based queries ("a large gray mammal with a trunk") preserve most classification accuracy but lose disproportionate segmentation quality, revealing name-token anchoring in patch-text alignment.
- **why_important:** Determines whether open-vocab dense systems can serve name-free use cases (descriptions, rare entities) or are fundamentally name-bound.
- **why_possibly_novel:** Name-vs-definition dissociation for dense outputs is untested (UNVERIFIED — needs lit search).
- **minimal_experiment:** Build name/definition/hybrid query sets; compare classification vs segmentation degradation per query type across models; analyze token-level attention to locate anchoring.
- **main_risk:** Definition quality varies; use multiple sources and human validation.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0042

### W2-B-0173 — Box prompts carry an implicit tightness prior; systematic looseness degradation is predictable and correctable by calibration.

- **problem:** Box-promptable models are trained with near-tight boxes; real boxes (from detectors or users) are systematically looser, and the failure profile is undocumented.
- **core_hypothesis:** Mask quality decays smoothly with box looseness following a model-specific curve, and a per-model tightness-calibration (shrink factor) recovers most of the loss without retraining.
- **why_important:** A one-parameter fix for a ubiquitous interface mismatch between detectors and promptable segmenters.
- **why_possibly_novel:** Tightness-prior characterization and calibration for box prompts is new.
- **minimal_experiment:** Sweep box expansion factors on segmentation benchmarks; fit degradation curves per model; learn optimal shrink calibration and validate on detector-generated boxes.
- **main_risk:** Looseness may interact with object shape; stratify by aspect ratio and convexity.
- **cluster:** `prompt_sensitivity`

### W2-B-0174 — Prompt token position (prefix/middle/suffix) systematically shifts VLM outputs via attention-mask asymmetries.

- **problem:** Prompt-tuning implementations choose token positions by convention; causal attention or masking structure makes position semantically consequential in ways never isolated.
- **core_hypothesis:** Identical learned prompts placed at different sequence positions yield measurably different dense and classification outputs, with position effects explained by attention-flow asymmetries rather than content.
- **why_important:** Position becomes a controlled variable rather than hidden confound across prompt-tuning literature.
- **why_possibly_novel:** Position-causal analysis of prompt tokens in VLMs is unexplored.
- **minimal_experiment:** Train position-controlled prompt variants; swap positions at inference; decompose output changes into position vs content effects via attention-flow analysis.
- **main_risk:** Bidirectional encoders may nullify effects; contrast encoder types.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0128

### W2-B-0175 — Interactive segmentation rankings are simulation-policy artifacts: model orderings flip across simulated user policies.

- **problem:** Interactive benchmarks simulate clicks with fixed policies (center-of-error); whether reported model rankings survive policy changes is untested — a validity threat to the whole evaluation practice.
- **core_hypothesis:** Across plausible click policies (center, boundary-biased, human-recorded), model rankings change substantially, and a policy-invariant evaluation (integrating over a policy distribution) yields different winners than any single policy.
- **why_important:** Evaluation validity for a growing product category; would set a new benchmark standard.
- **why_possibly_novel:** Policy-sensitivity meta-evaluation of interactive segmentation is new.
- **minimal_experiment:** Re-evaluate leading interactive models under multiple click policies including human click datasets; quantify rank instability; propose and validate policy-marginalized metrics.
- **main_risk:** Human click data collection is costly; start with policy families spanning realistic behavior.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0169

### W2-B-0176 — Prompt transferability across models is determined by pretraining-data overlap, not architectural similarity.

- **problem:** Prompts tuned on one model are reused on others opportunistically; what actually governs transfer success is unknown.
- **core_hypothesis:** Prompt-transfer performance correlates strongly with pretraining-data overlap between source and target models and weakly with architecture similarity, implying prompts encode data-manifold geometry.
- **why_important:** Predictable transfer would enable prompt libraries portable across model families with known compatibility.
- **why_possibly_novel:** Data-vs-architecture attribution of prompt transfer is untested.
- **minimal_experiment:** Tune prompts on a source-model grid varying data and architecture independently (OpenCLIP variants); transfer all pairs; regress transfer success on data-overlap and architecture-distance measures.
- **main_risk:** Data overlap is hard to quantify for closed models; use open-data model grids.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0171

### W2-B-0177 — Performance versus prompt length follows an inverted-U whose peak location indexes task complexity.

- **problem:** Prompt length is tuned ad hoc; a stable functional relationship between length, task, and performance would replace search with prediction.
- **core_hypothesis:** Across tasks, accuracy vs learned-prompt length rises then falls, and the peak length correlates with task output complexity (classes, output structure), yielding a usable length-selection rule.
- **why_important:** Removes a hyperparameter search and provides a behavioral measure of task complexity from the model's perspective.
- **why_possibly_novel:** Cross-task length-response laws for prompt tuning are unmapped.
- **minimal_experiment:** Sweep prompt lengths across classification/retrieval/dense tasks; fit response curves; test peak-position prediction on held-out tasks.
- **main_risk:** Peaks may be broad/flat, weakening the law; report curvature statistics.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0119

### W2-B-0178 — Human-judged-equivalent prompt paraphrases produce inequivalent masks, defining a semantic-robustness gap metric.

- **problem:** Text-promptable segmenters face natural phrasing variation; the gap between human-judged meaning equivalence and model output equivalence is unmeasured.
- **core_hypothesis:** Across paraphrase sets judged equivalent by humans, mask agreement is far from perfect and varies by model, and the semantic-robustness gap predicts real-user satisfaction better than benchmark IoU.
- **why_important:** A user-aligned robustness metric for text-prompted dense systems, complementing accuracy leaderboards.
- **why_possibly_novel:** Paraphrase-equivalence auditing for dense outputs with user-satisfaction validation is new.
- **minimal_experiment:** Build human-validated paraphrase sets; measure inter-paraphrase mask agreement per model; run small user studies correlating the gap with satisfaction.
- **main_risk:** Paraphrase equivalence is graded, not binary; use continuous equivalence ratings.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0170

### W2-B-0179 — Point prompts on object parts expose a part-whole ambiguity resolved by dataset priors, not user intent.

- **problem:** A click on a shirt could mean shirt, person, or fabric region; how promptable models resolve granularity ambiguity — and whether resolution is principled — is uncharacterized.
- **core_hypothesis:** Granularity choices are strongly predicted by training-data mask-size statistics rather than image evidence or click context, making resolution a dataset artifact users cannot control.
- **why_important:** Understanding the granularity prior is prerequisite to interfaces that let users actually select granularity.
- **why_possibly_novel:** Quantitative attribution of granularity resolution to dataset priors is new.
- **minimal_experiment:** Click identical part locations across object categories; compare output granularity distributions against training-mask statistics of each model; test context manipulations that should shift intent.
- **main_risk:** Multi-mask outputs partially address this; analyze whether ranked outputs span true ambiguity.
- **cluster:** `prompt_sensitivity`

### W2-B-0180 — Calibration quality differs systematically by prompt modality: the same model is trustworthy with boxes but not points.

- **problem:** Confidence calibration of promptable segmenters is reported (if at all) aggregated over prompt types, hiding modality-specific trust profiles.
- **core_hypothesis:** Calibration error differs significantly across point/box/text prompts for identical targets, with sparser prompts producing worse-calibrated confidence — meaning interface choice changes reliability, not just accuracy.
- **why_important:** Downstream consumers threshold on confidence; per-modality calibration profiles are needed for safe automation.
- **why_possibly_novel:** Prompt-modality-conditional calibration analysis is unexplored.
- **minimal_experiment:** Evaluate ECE and risk-coverage per prompt modality on matched targets across models; test per-modality recalibration transferability.
- **main_risk:** Matched-target construction across modalities needs care; use annotation-rich datasets.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0170

### W2-B-0181 — Visual prompts (drawn circles/arrows) influence VLM features globally, not locally, contradicting their intuitive mechanism.

- **problem:** Marking images with visual cues steers VLMs (reported phenomenon — UNVERIFIED, needs lit search), but whether influence is spatially local (attention to the mark's region) or a global feature shift is unknown.
- **core_hypothesis:** Feature-drift maps show visual marks change representations across the whole image (global style shift) as much as near the mark, and steering success correlates with the global component — undermining the "pointing" interpretation.
- **why_important:** Mechanism determines reliability: global effects predict interference with other image content and compositional failures.
- **why_possibly_novel:** Spatial decomposition of visual-prompt influence is new.
- **minimal_experiment:** Add controlled marks; measure per-patch feature drift vs distance from mark; correlate steering success with local vs global drift components across models.
- **main_risk:** Drift metrics may miss functionally-relevant components; validate with behavioral probes.
- **cluster:** `prompt_sensitivity`

### W2-B-0182 — Larger VLMs are more prompt-sensitive on rare classes, inverting the expected robustness-scale relationship.

- **problem:** Scale is assumed to buy robustness, but stronger priors in large models may require more prompt precision to override, especially where evidence is thin (rare classes).
- **core_hypothesis:** Prompt-perturbation sensitivity decreases with scale for common classes but increases for rare classes, producing a scale-rarity interaction opposite to uniform-robustness assumptions.
- **why_important:** Deployment for long-tail vocabularies may not benefit from scale as assumed; prompt-robustness must be evaluated tail-stratified.
- **why_possibly_novel:** The scale-by-rarity interaction in prompt sensitivity is unmeasured.
- **minimal_experiment:** Measure output variance under prompt paraphrase/jitter across model scales, stratified by class frequency; test the interaction across two model families.
- **main_risk:** Rarity estimates for pretraining corpora are approximate; use multiple frequency proxies.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0177

### W2-B-0183 — Adversarially-placed point configurations exist that make promptable segmenters produce absurd masks, defining a prompt attack surface.

- **problem:** Robustness of promptable models is studied against image perturbations, not against the prompt channel itself — which in deployed systems is attacker-influenceable (e.g., automated prompt generators).
- **core_hypothesis:** Optimized 2-4 point configurations reliably induce masks violating basic constraints (disconnected fragments, near-full-image masks) at high success rates, and attack configurations transfer across images and models.
- **why_important:** Establishes the prompt channel as a security surface requiring input validation in automated pipelines.
- **why_possibly_novel:** Prompt-channel adversarial characterization for segmentation is new.
- **minimal_experiment:** Search point configurations maximizing mask absurdity metrics; measure success and transfer rates; analyze what geometric relations make configurations adversarial.
- **main_risk:** "Absurdity" needs a defensible metric; use constraint-violation batteries.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0167

### W2-B-0184 — Where prompt-ensemble aggregation happens (features, logits, or masks) determines whether ensembling helps or hurts boundaries.

- **problem:** Prompt ensembling is applied at whatever level is convenient; the aggregation level's effect on spatial output structure is unexamined.
- **core_hypothesis:** Feature-level averaging blurs boundaries, mask-level voting sharpens them, and logit-level averaging sits between — with the ordering stable across models, making aggregation level a first-class design choice.
- **why_important:** A free quality lever for every prompt-ensemble pipeline in dense prediction.
- **why_possibly_novel:** Aggregation-level analysis for dense prompt ensembling is unexplored.
- **minimal_experiment:** Compare aggregation levels on boundary/interior decomposed metrics across models and prompt types; explain the ordering via smoothing analysis.
- **main_risk:** Interactions with ensemble size may complicate the ordering; sweep both.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0168

### W2-B-0185 — Iterative interactive refinement can oscillate rather than converge, and oscillation is predictable from prompt-response Jacobians.

- **problem:** Interactive loops (click, correct, re-click) assume convergence to the desired mask; fixed-point behavior of prompt-update dynamics has never been analyzed.
- **core_hypothesis:** For a measurable fraction of targets, standard correction policies produce mask oscillations or limit cycles rather than convergence, and local sensitivity (response magnitude to single clicks) predicts non-convergence.
- **why_important:** Oscillation wastes user effort and breaks automation; prediction enables loop-breaking interventions.
- **why_possibly_novel:** Dynamical-systems analysis of interactive segmentation loops is new.
- **minimal_experiment:** Run long simulated correction loops across models/policies; classify trajectories (converge/oscillate/wander); test sensitivity-based prediction of trajectory class.
- **main_risk:** Human users adapt policies dynamically; validate key cases with human-in-the-loop data.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0175

### W2-B-0186 — Morphosyntax leaks into masks: determiners and number marking shift segment size distributions measurably.

- **problem:** Grammatical elements ("a", "the", plural "-s") should modulate reference but their quantitative effect on dense outputs is unknown — a blind spot in interface design.
- **core_hypothesis:** Controlled morphosyntactic minimal pairs ("the crack" vs "cracks" vs "cracking") produce systematic mask-size and mask-count shifts, with effect sizes rivaling content-word changes for some models.
- **why_important:** Users cannot control what they do not know exists; documenting grammar-to-pixels effects enables both exploitation and correction.
- **why_possibly_novel:** Morphosyntactic effect quantification on dense outputs is new.
- **minimal_experiment:** Build minimal-pair grammatical batteries; measure mask statistics shifts per contrast across text-promptable segmenters; compare effect sizes to content-word baselines.
- **main_risk:** Confounds with token frequency; control via frequency-matched pairs.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0050

### W2-B-0187 — Tuned prompts exploit model-specific bugs: their gains evaporate under rephrasing-equivalent evaluation, making them bug detectors.

- **problem:** Learned prompts sometimes gain accuracy without interpretable content; whether gains reflect generalizable task alignment or exploitation of idiosyncratic model defects is unresolved.
- **core_hypothesis:** A measurable fraction of prompt-tuning gain disappears when evaluation uses meaning-preserving input rephrasings/renderings, and the evaporating fraction localizes model-specific shortcuts — turning prompt tuning into an automated bug-mining tool.
- **why_important:** Reframes an adaptation method as a diagnostic instrument for model quality assurance.
- **why_possibly_novel:** Prompts-as-bug-detectors is an unexplored inversion.
- **minimal_experiment:** Tune prompts; evaluate on paraphrase/re-render-invariant test suites; decompose gains into robust vs evaporating components; characterize what the evaporating component exploits.
- **main_risk:** Distinguishing bugs from legitimate distributional alignment requires careful definitions.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0171

### W2-B-0188 — Real-user prompt distributions differ from benchmark prompts enough to reorder model rankings.

- **problem:** Promptable models are compared on curated prompt distributions; ecological validity of those rankings for actual user behavior is assumed without evidence.
- **core_hypothesis:** A modest collected corpus of real user prompts (clicks and phrasings) shifts measured model rankings relative to benchmark prompts, with the shift concentrated in models tuned on synthetic prompt distributions.
- **why_important:** Product decisions ride on benchmark rankings; demonstrating ecological invalidity would redirect evaluation investment.
- **why_possibly_novel:** Ecological-validity audits of prompt benchmarks are missing.
- **minimal_experiment:** Collect real prompts from annotator sessions; re-evaluate model suites under real vs benchmark prompt distributions; quantify rank correlation and identify divergence causes.
- **main_risk:** User populations vary; sample multiple user types (novice, expert annotator).
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0175

### W2-B-0189 — Prompt dropout during training buys prompt robustness at a quantifiable accuracy cost, tracing a controllable frontier.

- **problem:** Prompt-robustness interventions are proposed without characterizing the fundamental robustness-accuracy tradeoff they navigate.
- **core_hypothesis:** Training promptable segmenters with stochastic prompt degradation (jitter, dropout, paraphrase) traces a smooth robustness-accuracy frontier whose shape is consistent across models — establishing the exchange rate between the two.
- **why_important:** Lets system designers purchase exactly the robustness they need instead of guessing.
- **why_possibly_novel:** Frontier characterization (not point solutions) for prompt robustness is new.
- **minimal_experiment:** Train with graded prompt-noise levels; measure clean accuracy vs perturbation robustness per level; fit frontiers; compare across architectures.
- **main_risk:** Requires training runs, not just evaluation; use mid-scale models.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0166

### W2-B-0190 — Prompt-embedding arithmetic composes attributes for dense outputs only within empirically-mappable compatibility regions.

- **problem:** Embedding arithmetic ("red"+"car") is folklore for global tasks; whether composed prompt embeddings produce correct compositional masks — and when composition breaks — is unmapped.
- **core_hypothesis:** Composed prompt embeddings produce correct dense targets for attribute-object pairs whose joint frequency exceeds a threshold, and fail systematically (attribute leakage to wrong objects) below it.
- **why_important:** Defines the safe operating envelope for a widely-assumed compositional capability.
- **why_possibly_novel:** Compositional validity maps for prompt arithmetic in dense prediction are new.
- **minimal_experiment:** Sweep attribute-object compositions across frequency strata; measure mask correctness and leakage patterns; fit the compatibility boundary.
- **main_risk:** Frequency estimation for compositions is noisy; use multiple corpora.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0043

### W2-B-0191 — The same click means different things across datasets: promptable models learn dataset-specific prompt pragmatics.

- **problem:** Training data for promptable segmentation embeds annotation conventions (what a click "means"); models may encode convention rather than a universal prompt semantics, breaking cross-dataset prompt behavior.
- **core_hypothesis:** Models trained on different mask-granularity conventions respond to identical clicks with systematically different granularity/extent choices, and convention signatures are recoverable from the model's responses alone.
- **why_important:** Explains cross-dataset interactive inconsistencies and motivates convention-conditioning interfaces.
- **why_possibly_novel:** Prompt-pragmatics attribution to training conventions is unexplored.
- **minimal_experiment:** Probe click-response distributions of models trained on distinct datasets using a shared neutral image set; classify convention signatures; validate against known annotation guidelines.
- **main_risk:** Public models rarely vary only in data; train controlled variants at mid-scale.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0179

### W2-B-0192 — Prompt influence is layer-localized: early cross-attention sets mask topology, late layers only refine boundaries.

- **problem:** Where prompts causally shape the output inside promptable architectures is unknown, leaving interface improvements to trial and error.
- **core_hypothesis:** Causal patching of prompt-conditioned activations shows topology decisions (which region, connectivity) are fixed in early prompt-image interaction layers, while later layers adjust only boundary detail — a two-stage division of labor.
- **why_important:** Localization tells designers where to intervene for topology errors vs boundary errors, and compresses the search space for interface research.
- **why_possibly_novel:** Layer-causal decomposition of prompt influence is new.
- **minimal_experiment:** Patch prompt-pathway activations across layers between prompt variants; measure which output properties (topology vs boundary metrics) change per layer; verify across architectures.
- **main_risk:** Architectures differ in prompt-injection topology; establish per-family maps.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0181

### W2-B-0193 — Multilingual prompting degrades dense outputs steeper than classification, quantifying a language-tax on spatial grounding.

- **problem:** Text-promptable systems are multilingual by claim (multilingual encoders) but per-language dense quality — and whether the dense pathway is more language-sensitive than global tasks — is unmeasured.
- **core_hypothesis:** Across languages, dense performance drops faster with decreasing language resourcedness than classification does, because patch-text alignment requires finer-grained text representations than pooled matching.
- **why_important:** Quantifies exclusion effects for non-English users of interactive dense tools, guiding data investment.
- **why_possibly_novel:** The dense-vs-global multilingual degradation differential is new.
- **minimal_experiment:** Evaluate text-prompted segmentation and classification across 15 languages with verified translations; fit degradation-vs-resourcedness slopes per task type; localize failure via cross-lingual retrieval probes.
- **main_risk:** Translation artifacts; use native-speaker validation on subsets.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0061

### W2-B-0194 — Interactive models grow more confident with each added prompt even when wrong — segmentation sycophancy.

- **problem:** Confidence should track evidence; if additional user prompts inflate confidence irrespective of correctness, automation thresholds become unsafe exactly in heavy-interaction (hard) cases.
- **core_hypothesis:** Mean confidence rises monotonically with prompt count while conditional accuracy does not, and the confidence-accuracy gap widens with interaction depth — an interaction-induced miscalibration law.
- **why_important:** Interactive pipelines using confidence for auto-accept would systematically over-trust the hardest cases.
- **why_possibly_novel:** Interaction-depth-conditional calibration analysis is new.
- **minimal_experiment:** Track confidence and accuracy as simulated/human prompts accumulate on hard targets; fit the divergence curve; test depth-aware recalibration.
- **main_risk:** Confidence definitions vary by architecture; standardize on mask-probability aggregates.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0180

### W2-B-0195 — The prompt-free "default mask" of promptable models reveals a saliency prior that predicts their prompt-sensitivity map.

- **problem:** Promptable models must output something under empty/degenerate prompts; this default behavior encodes the model's prior, potentially explaining where prompts struggle to override it.
- **core_hypothesis:** Default-mask saliency maps (empty-prompt outputs) predict per-region prompt effort (clicks needed to achieve target masks): high-prior regions are easy to select and hard to deselect, quantifying prior-versus-prompt dynamics.
- **why_important:** Turns a degenerate case into a diagnostic tool for interaction cost prediction and interface design.
- **why_possibly_novel:** Default-output analysis as a predictor of interaction dynamics is unexplored.
- **minimal_experiment:** Extract empty-prompt outputs across image sets; measure per-region click-effort in simulated interaction; test prediction of effort from default saliency across models.
- **main_risk:** Some architectures forbid empty prompts; use minimal-information prompts as proxies.
- **cluster:** `prompt_sensitivity`
- **mutate_from:** W2-B-0179

---

## 7. Representation mismatch: global contrastive features vs pixel-level needs

Cluster key: `representation_mismatch`

### W2-B-0196 — The equivariance deficit spectrum of a frozen VFM predicts its per-task dense transfer better than any accuracy benchmark.

- **problem:** Dense tasks need feature equivariance to specific transformations (translation, scale, rotation); VFMs trained for invariance lack it non-uniformly, but no per-transformation audit exists that predicts task fit.
- **core_hypothesis:** Measuring equivariance error per transformation family yields a deficit spectrum whose task-weighted combination predicts frozen-probe transfer rank across tasks with higher fidelity than ImageNet or mIoU proxies.
- **why_important:** A one-pass, label-free audit replacing expensive per-task benchmarking for backbone selection.
- **why_possibly_novel:** Spectrum-based prediction (not single-number equivariance) validated against multi-task dense transfer is new.
- **minimal_experiment:** Compute equivariance spectra for 12 VFMs; measure frozen transfer on seg/depth/edges/correspondence; fit and cross-validate the spectrum-to-task prediction model.
- **main_risk:** Equivariance measurement depends on feature-comparison metric choices; report robustness across metrics.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0011

### W2-B-0197 — Representation distance between frozen and task-optimal features quantitatively predicts adaptation cost in gradient steps.

- **problem:** "How far" a pretrained representation is from what a task needs has no agreed measure, so adaptation budgets are guessed.
- **core_hypothesis:** CKA distance between frozen features and features of a fully-converged task model predicts the fine-tuning steps needed to reach performance thresholds, forming an adaptation-cost law usable before training.
- **why_important:** Pre-training-time estimates of adaptation cost would rationalize compute planning across the field.
- **why_possibly_novel:** Representation-distance-to-training-cost laws are unestablished (UNVERIFIED — needs lit search).
- **minimal_experiment:** For many (model, task) pairs, measure frozen-to-converged CKA and record training-cost curves; fit the law; validate on held-out pairs.
- **main_risk:** CKA may saturate; test alternative distances (Procrustes, shape metrics).
- **cluster:** `representation_mismatch`

### W2-B-0198 — In contrastive VFMs, localization lives in attention geometry while values carry semantics — a readable division of labor.

- **problem:** Dense readouts consume value vectors by default; if spatial precision is encoded in attention patterns instead, standard readouts systematically discard the localization signal.
- **core_hypothesis:** Readouts given access to attention maps (as features) recover boundary quality that value-only readouts cannot, specifically in contrastive models — establishing that "where" and "what" are stored in different mechanisms.
- **why_important:** Changes what dense pipelines should extract from frozen VFMs, without any backbone modification.
- **why_possibly_novel:** The attention-as-localization-store hypothesis with controlled readout comparisons is untested.
- **minimal_experiment:** Compare probes on values-only, attention-only, and combined features across VFM families; decompose boundary vs interior gains; verify the contrastive-specific pattern.
- **main_risk:** Attention features are high-dimensional; control probe capacity strictly.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0002

### W2-B-0199 — Class semantics are low-frequency and boundaries high-frequency in feature space, explaining why one readout cannot serve both.

- **problem:** Dense readouts jointly optimize region labeling and boundary placement; if these signals occupy disjoint spectral bands of the feature map, joint linear readouts face a structural conflict.
- **core_hypothesis:** Spectrally decomposing feature maps shows class-discriminative energy concentrated at low spatial frequencies and boundary-discriminative energy at high frequencies, and readouts trained on band-split features confirm the dissociation.
- **why_important:** Explains persistent boundary weakness of frozen-VFM segmentation and grounds readout design in measurement.
- **why_possibly_novel:** Spectral dissociation of dense-task signals within VFM features is unexplored.
- **minimal_experiment:** Band-pass feature maps; train probes per band for region-label vs boundary tasks; quantify the spectral separation across models and layers.
- **main_risk:** Band-splitting may interact with feature nonlinearity; verify with nonlinear probes.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0004

### W2-B-0200 — Linear-probe methodology systematically underestimates dense information, misranking VFMs for dense use.

- **problem:** The community ranks VFM dense quality via linear probes; if dense information is present but nonlinearly encoded in some models more than others, the entire ranking practice is biased.
- **core_hypothesis:** Moving from linear to capacity-controlled nonlinear probes changes dense-quality rankings of major VFMs (rank correlation well below 1), with contrastive models gaining most — meaning "poor dense features" often means "nonlinearly-coded dense features".
- **why_important:** Methodological correction affecting dozens of comparison papers and model-selection decisions.
- **why_possibly_novel:** Probe-capacity sensitivity of VFM dense rankings is undocumented.
- **minimal_experiment:** Rank 12 VFMs by dense probes at graded capacities; quantify rank instability; identify models whose dense information is disproportionately nonlinear.
- **main_risk:** Distinguishing readout learning from information presence requires careful data-size controls.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0002

### W2-B-0201 — Each pretraining augmentation destroys a measurable amount of dense-label information, yielding an invariance-cost table.

- **problem:** Augmentation recipes are inherited from classification-era tuning; their per-augmentation cost to pixel-level information has never been itemized.
- **core_hypothesis:** Training matched SSL models with single-augmentation ablations shows each augmentation reduces mutual information between features and dense labels by a characteristic, task-dependent amount — with color and aggressive-crop augmentations most expensive for boundaries.
- **why_important:** An itemized cost table would let pretraining recipes be tuned for intended downstream task families.
- **why_possibly_novel:** Per-augmentation dense-information accounting with controlled retraining is new.
- **minimal_experiment:** Pretrain ViT-S SSL variants with augmentation ablations at matched compute; measure dense-probe performance and feature-label information estimates per variant.
- **main_risk:** Small-scale pretraining may not extrapolate; verify key effects at one larger scale.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0019

### W2-B-0202 — Contrastive features exhibit local dimensional collapse: per-patch effective rank is too low for boundary discrimination.

- **problem:** Dimensional collapse is measured globally; dense tasks require per-location expressivity, and local collapse (uniform features within regions) would specifically kill boundary evidence.
- **core_hypothesis:** Effective rank computed over local patch neighborhoods is significantly lower in contrastive models than SSL-distillation models, and local rank at a location predicts boundary error there.
- **why_important:** A local-geometry diagnosis of the dense deficit, more actionable than global collapse metrics.
- **why_possibly_novel:** Locally-resolved collapse analysis linked to spatial error maps is unexplored.
- **minimal_experiment:** Compute neighborhood-level effective rank across images/models; correlate with per-location boundary errors of frozen probes; compare model families.
- **main_risk:** Local rank estimates are noisy at small neighborhood sizes; use multi-scale estimation.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0004

### W2-B-0203 — Bilinear feature upsampling, not feature content, is the binding constraint in frozen-VFM segmentation pipelines.

- **problem:** Frozen features at stride 14-16 are upsampled naively to pixel resolution; the community attributes resulting errors to features, without isolating the upsampling stage's contribution.
- **core_hypothesis:** An oracle experiment granting ground-truth-guided upsampling (edge-aware, using image but not labels at test) recovers a large share of the gap to supervised models, showing the bottleneck is resolution restoration, not representation.
- **why_important:** Redirects effort from pretraining critique to the neglected upsampling stage — a much cheaper research target.
- **why_possibly_novel:** Stage-isolated attribution of the frozen-dense gap to upsampling is missing.
- **minimal_experiment:** Compare naive vs image-guided vs oracle upsampling on frozen features across models; decompose the supervised-gap into upsampling vs representation components.
- **main_risk:** Image-guided upsampling partially injects new information; bound its contribution carefully.
- **cluster:** `representation_mismatch`

### W2-B-0204 — Contrastive features have systematically higher signal-to-noise on foreground than stuff regions, measurable as SNR maps.

- **problem:** Where in an image contrastive features are reliable is unmapped; if reliability concentrates on foreground objects, stuff-region weakness is a signal-quality issue, not a labeling issue.
- **core_hypothesis:** Per-region feature SNR (class-discriminative variance over within-class variance) is significantly higher for things than stuff in contrastive models, with the disparity smaller in reconstruction-based models, and SNR maps predict per-region probe errors.
- **why_important:** SNR maps provide spatial reliability priors for fusion, uncertainty, and active labeling.
- **why_possibly_novel:** Spatial SNR cartography of VFM features is new.
- **minimal_experiment:** Estimate per-region SNR from features on labeled data; correlate with errors; compare model families; validate SNR-map-guided prediction weighting.
- **main_risk:** SNR estimation needs many samples per region type; use large datasets.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0003

### W2-B-0205 — A k-NN-based estimator can lower-bound the best achievable segmentation loss from frozen features, defining "dense sufficiency".

- **problem:** Debates about whether frozen features suffice for a dense task lack a measurable quantity; an estimator of the minimum achievable risk over all readouts would settle per-task sufficiency questions.
- **core_hypothesis:** A consistent k-NN risk estimator on patch features converges (with data size) toward a stable per-task bound that ranks models identically to expensive readout sweeps, providing a practical sufficiency measure.
- **why_important:** One estimator would standardize frozen-feature evaluation and end probe-architecture disputes.
- **why_possibly_novel:** Formal sufficiency estimation for dense tasks from frozen features is unformalized.
- **minimal_experiment:** Implement k-NN risk estimators with convergence diagnostics; compare bound rankings against exhaustive readout sweeps across models/tasks; publish the protocol.
- **main_risk:** Curse of dimensionality may slow convergence; test dimensionality-reduction preprocessing.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0200

### W2-B-0206 — Objective-specific geometry: reconstruction features encode depth linearly, contrastive features encode semantics linearly, and the tradeoff is continuous in loss mixing.

- **problem:** The folk dichotomy "MAE for geometry, CLIP for semantics" lacks a quantitative account of whether the tradeoff is intrinsic to objectives and how it interpolates.
- **core_hypothesis:** Across checkpoints spanning reconstruction-contrastive loss mixtures (or matched families), linear decodability of depth and semantics trade off monotonically, positioning every VFM on a single geometry-semantics frontier.
- **why_important:** A frontier map lets practitioners choose or mix objectives quantitatively rather than by folklore.
- **why_possibly_novel:** Continuous frontier characterization across objective mixtures is untested.
- **minimal_experiment:** Train small-scale mixture-objective models plus evaluate public families; probe depth/semantics linear decodability; fit and validate the frontier.
- **main_risk:** Public models confound data/scale with objective; anchor conclusions on controlled retrainings.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0006

### W2-B-0207 — A requirements-vs-invariances matrix predicts frozen-VFM failure for intrinsic-image tasks needing discarded physical signals.

- **problem:** Tasks like shadow removal, illuminant estimation, and reflectance decomposition need photometric information contrastive training deliberately discards; the match between task requirements and model invariances is never formalized.
- **core_hypothesis:** Building an explicit matrix (task-required signals x model invariances) predicts frozen-probe failure patterns on intrinsic-image tasks with high accuracy, including counterintuitive successes where invariance is incomplete.
- **why_important:** A predictive framework prevents doomed applications and identifies which physical signals survive pretraining.
- **why_possibly_novel:** Formal requirement-invariance matching for VFM applicability is new.
- **minimal_experiment:** Audit invariances of 10 VFMs; probe intrinsic-image tasks; test matrix-based failure prediction against actual results.
- **main_risk:** Partial invariances complicate binary matrices; use graded invariance scores.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0201

### W2-B-0208 — Sub-patch aliasing is accountable: patch tokens vote for dominant content, and minority-pixel classes vanish predictably.

- **problem:** Pixels sharing a patch share a token; the systematic loss of minority-within-patch content is acknowledged qualitatively but never made quantitatively predictive.
- **core_hypothesis:** Per-class recall of frozen-probe segmentation is predicted by the distribution of that class's within-patch occupancy fractions, with a sharp recall collapse below a model-specific occupancy threshold.
- **why_important:** An occupancy-based feasibility calculator tells practitioners which classes cannot be segmented at a given patch size before running anything.
- **why_possibly_novel:** Quantitative occupancy-to-recall laws are unfitted.
- **minimal_experiment:** Compute occupancy distributions per class across datasets; fit recall-vs-occupancy curves per model/patch size; validate predictions on held-out datasets.
- **main_risk:** Attention may partially rescue minority content; the law's deviations are themselves informative.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0018

### W2-B-0209 — Language alignment quantizes continuous visual attributes, hurting dense regression tasks more than dense classification.

- **problem:** Language supervision imposes discrete category structure; tasks requiring continuous outputs (density estimation, pose fields, gaze) may inherit quantization artifacts undetected by classification-style metrics.
- **core_hypothesis:** Frozen CLIP-family features show measurable clustering (quantization) along continuous attribute manifolds where SSL features vary smoothly, and quantization strength predicts the CLIP-vs-SSL gap on dense regression but not dense classification.
- **why_important:** Identifies a principled task boundary for language-aligned features, guiding backbone choice for regression-like dense tasks.
- **why_possibly_novel:** Feature-manifold quantization analysis tied to a regression-classification dissociation is new.
- **minimal_experiment:** Trace feature trajectories along controlled attribute morphs (pose, density, curvature); quantify clustering; correlate with probe gaps on regression vs classification dense tasks.
- **main_risk:** Morph stimuli must avoid off-manifold artifacts; use real-image attribute series where possible.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0026

### W2-B-0210 — VFM features are smoother than ground-truth label maps, and the oversmoothness ratio predicts boundary displacement error.

- **problem:** Feature smoothness is aesthetically praised, but labels have their own spatial statistics; a mismatch between feature and label smoothness would place a floor on boundary accuracy.
- **core_hypothesis:** The ratio of feature autocorrelation length to label autocorrelation length exceeds one for all major VFMs, varies by family, and linearly predicts each model's mean boundary displacement error.
- **why_important:** A label-free smoothness audit predicting boundary performance would guide model choice and quantify a structural ceiling.
- **why_possibly_novel:** Feature-vs-label spatial-statistics matching is unexamined.
- **minimal_experiment:** Estimate autocorrelation lengths of features and labels across datasets; correlate mismatch ratios with boundary displacement errors of frozen probes across models.
- **main_risk:** Autocorrelation length is content-dependent; use per-image paired estimates.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0199

### W2-B-0211 — Global-pooling pretraining creates attention-sink shortcuts that starve patch tokens of task-usable information.

- **problem:** Objectives supervising only pooled outputs allow information to route through few sink tokens; the cost to the patch-token population that dense tasks read is unquantified.
- **core_hypothesis:** Models pretrained with pooled objectives show higher information concentration (few tokens carry decodable class signal) than densely-supervised counterparts, and concentration inversely predicts frozen dense performance across models.
- **why_important:** An information-routing account of why objective design, not data or scale, drives dense quality.
- **why_possibly_novel:** Token-level information-concentration metrics linked to dense transfer are new.
- **minimal_experiment:** Measure per-token decodability distributions across VFMs; compute concentration indices; correlate with dense probe performance; verify causally via pooled-vs-dense-objective retraining at small scale.
- **main_risk:** Decodability distributions may reflect probing artifacts; use multiple information estimators.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0012

### W2-B-0212 — Task-relevant variance hides in low-eigenvalue feature directions, so whitening reveals dense information that raw features conceal.

- **problem:** Dense readouts consume features dominated by high-variance directions tuned for pretraining objectives; task-critical signal may occupy the covariance tail, invisibly to standard probes.
- **core_hypothesis:** Whitening frozen features before linear probing disproportionately improves dense tasks over classification, and the improvement per model quantifies how much dense signal its pretraining relegated to tail directions.
- **why_important:** A trivial preprocessing step with diagnostic value, reframing "weak dense features" as spectrally-buried features.
- **why_possibly_novel:** Whitening-response as a cross-model dense diagnostic (not a trick) is unexplored.
- **minimal_experiment:** Probe raw vs whitened features across models and tasks; quantify the dense-vs-global whitening response; correlate with covariance-spectrum statistics.
- **main_risk:** Whitening amplifies noise directions too; use shrinkage-regularized variants.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0202

### W2-B-0213 — Resolution-mismatch confounds most published "semantic vs dense" model comparisons; res-matched re-evaluation overturns rankings.

- **problem:** VFMs are compared at their preferred resolutions, conflating representation quality with resolution handling — a confound rarely controlled in dense-quality claims.
- **core_hypothesis:** Re-evaluating major VFM comparisons at strictly matched effective resolutions (same feature-map size and receptive statistics) changes dense rankings materially, attributing a large share of claimed representation differences to resolution artifacts.
- **why_important:** A measurement-hygiene correction with field-wide implications for how VFM comparisons must be run.
- **why_possibly_novel:** Systematic resolution-confound quantification for the dense-comparison literature is missing.
- **minimal_experiment:** Reproduce prominent comparisons; re-run under resolution-matched protocols; report rank changes and decompose original gaps into resolution vs representation.
- **main_risk:** "Fair matching" has multiple defensible definitions; report under several.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0030

### W2-B-0214 — Hard-negative-heavy contrastive training locally distorts feature metric structure, helping discrimination but harming geometric readouts.

- **problem:** Hard-negative mining shapes where the feature metric is stretched; the geometric side effects on dense tasks needing faithful distances (correspondence, depth ordering) are uncharacterized.
- **core_hypothesis:** Models trained with aggressive hard-negative sampling show locally distorted metric structure (violated triangle-inequality proxies, anisotropic neighborhoods) that predicts underperformance on metric-dependent dense tasks despite equal or better discrimination.
- **why_important:** Reveals a hidden cost of a popular training ingredient, guiding objective choice per downstream family.
- **why_possibly_novel:** Metric-geometry side-effect analysis of negative-sampling strategies is new.
- **minimal_experiment:** Compare feature-space metric diagnostics across models with known negative-sampling recipes; correlate distortion indices with correspondence/depth-order probe performance.
- **main_risk:** Training-recipe metadata is incomplete for public models; include controlled retrainings.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0206

### W2-B-0215 — CLIP's visual feature space splits into a text-aligned subspace and a complement that carries most dense information.

- **problem:** Open-vocab dense methods project everything through text alignment; if dense signal predominantly lives in the text-orthogonal complement, the standard pathway structurally discards it.
- **core_hypothesis:** Decomposing CLIP visual features into text-aligned and orthogonal subspaces shows dense probes rely mostly on the complement, while zero-shot classification uses the aligned part — a measurable division exposing why text-mediated dense inference underperforms.
- **why_important:** Explains a core open-vocab limitation and motivates dual-pathway readouts grounded in measured structure.
- **why_possibly_novel:** Subspace-decomposed functional attribution of CLIP features is new (UNVERIFIED — needs lit search).
- **minimal_experiment:** Estimate the text-aligned subspace from caption pairs; probe dense tasks on each subspace; quantify functional split across scales and CLIP variants.
- **main_risk:** Subspace estimation quality depends on caption data; use multiple estimation sets.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0017

### W2-B-0216 — Instance-discrimination pretraining preserves within-class part structure that class-supervised training collapses.

- **problem:** Dense part-level tasks need within-class variation; objectives differ in whether they preserve it, but the effect has not been isolated from data and scale.
- **core_hypothesis:** At matched data/scale, instance-discriminative models retain linearly-decodable part structure (pose, part boundaries) that class-supervised counterparts collapse, and the retention predicts part-segmentation transfer.
- **why_important:** Establishes objective choice as the controlling variable for part-level reuse, relevant to robotics and fine-grained analysis.
- **why_possibly_novel:** Controlled objective-isolation for part-structure retention is missing.
- **minimal_experiment:** Train matched ViT-S with instance vs class objectives; probe part decodability and part-segmentation transfer; correlate retention indices with transfer.
- **main_risk:** Small-scale training may understate flagship behavior; verify with public checkpoint contrasts.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0206

### W2-B-0217 — Dense readouts depend on positional encodings far more than global readouts, making PE-dependency a mismatch index.

- **problem:** How much dense performance rides on PE content vs feature content is unknown; models differing in PE design may owe dense differences to PEs, not representations.
- **core_hypothesis:** PE ablation/randomization at inference degrades dense probes several times more than classification probes, and the PE-dependency ratio varies enough across models to reorder dense rankings when controlled.
- **why_important:** Separates representation quality from positional bookkeeping in model comparisons and localizes a fragile dependency.
- **why_possibly_novel:** PE-dependency as a quantified, cross-model dense metric is new.
- **minimal_experiment:** Ablate/permute PEs at inference across VFMs; measure dense-vs-global degradation ratios; re-rank models on PE-controlled dense metrics.
- **main_risk:** PE ablation is off-distribution; complement with PE-swap between models.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0015

### W2-B-0218 — The layer where dense information peaks shifts with input resolution, invalidating fixed-layer extraction practice.

- **problem:** Dense pipelines hardcode extraction layers tuned at one resolution; if the information peak migrates with resolution, deployed systems silently read the wrong layer (UNVERIFIED — needs lit search).
- **core_hypothesis:** The depth of maximal dense-probe performance moves systematically earlier or later with input resolution, by enough layers to cost several mIoU when extraction is fixed — an interaction effect unmeasured in layer-selection studies.
- **why_important:** A practical correction affecting every multi-resolution deployment of frozen VFMs.
- **why_possibly_novel:** The resolution-by-depth interaction for dense information is unmapped.
- **minimal_experiment:** Probe all layers across a resolution grid for several VFMs; map peak-depth trajectories; quantify the cost of fixed-layer extraction under realistic resolution variation.
- **main_risk:** Effects may be small for some families; the null is also actionable.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0020

### W2-B-0219 — Boundary pixels occupy low-margin "no man's land" between class clusters, and margin geometry alone predicts boundary errors.

- **problem:** Boundary errors are treated as a resolution problem; they may instead reflect feature-space geometry — boundary pixels falling between class clusters with low margins regardless of resolution.
- **core_hypothesis:** Per-pixel distance-to-cluster-margin in frozen feature space predicts boundary error probability with high AUROC, and models differ systematically in boundary-zone margin structure, explaining boundary-metric rankings beyond resolution effects.
- **why_important:** A geometric theory of boundary failure that separates resolution and representation causes, with uncertainty-map side benefits.
- **why_possibly_novel:** Margin-geometry analysis of boundary pixels across VFMs is new.
- **minimal_experiment:** Fit class clusters on frozen features; compute boundary-pixel margins; predict errors; compare margin structures across models controlling resolution.
- **main_risk:** Cluster fitting choices affect margins; test parametric and nonparametric variants.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0199

### W2-B-0220 — Cosine-similarity inference is dominated by few high-magnitude channels, masking dense-relevant low-magnitude channels.

- **problem:** Open-vocab and retrieval-style dense inference uses cosine similarity over raw features; heavy-tailed channel magnitudes mean few channels decide similarities, potentially drowning spatially-informative channels.
- **core_hypothesis:** Channel-magnitude rebalancing (per-channel standardization before similarity) improves patch-level retrieval/segmentation markedly on models with heavy-tailed channel statistics and negligibly on balanced ones — the tail statistics predict who benefits.
- **why_important:** A cost-free inference correction plus a diagnostic explaining cross-model inconsistencies in similarity-based dense methods.
- **why_possibly_novel:** Channel-dominance accounting for dense similarity inference is unexplored.
- **minimal_experiment:** Measure channel-magnitude distributions across VFMs; apply rebalancing; correlate improvement with tail indices; validate on open-vocab segmentation and correspondence.
- **main_risk:** Rebalancing may hurt calibrated global behavior; report both dense and global effects.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0212

### W2-B-0221 — Emergent correspondence and semantic transfer are orthogonal axes of VFM quality, requiring two-dimensional model cards.

- **problem:** Single "dense quality" scores conflate geometric matching ability with semantic labeling ability, though tasks weight them differently and models plausibly dissociate.
- **core_hypothesis:** Across many VFMs, correspondence quality and semantic dense transfer correlate weakly, defining a two-axis space where model families occupy distinct quadrants — and task performance is predicted by task-specific axis weightings.
- **why_important:** Two-axis characterization would fix chronic mispredictions of model fit and structure future VFM evaluation.
- **why_possibly_novel:** Explicit orthogonality testing of dense-quality axes is missing.
- **minimal_experiment:** Evaluate a VFM zoo on correspondence and semantic-transfer batteries; test correlation structure; validate two-axis task-fit predictions on held-out tasks.
- **main_risk:** Benchmarks within each axis may themselves disagree; use multi-benchmark axis scores.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0196

### W2-B-0222 — Video-pretrained image encoders repair the equivariance deficit of image-only VFMs at matched semantic quality.

- **problem:** Temporal objectives naturally supervise equivariance (features must track moving content), suggesting video pretraining fixes exactly what dense tasks miss — but image-vs-video comparisons never isolate this.
- **core_hypothesis:** At matched semantic-probe quality, frozen features from video-pretrained encoders show smaller equivariance deficits and better boundary/correspondence transfer than image-pretrained peers, attributing the gain specifically to temporal supervision.
- **why_important:** Would justify video pretraining for dense-task users on measured grounds rather than intuition.
- **why_possibly_novel:** Equivariance-mediated analysis of the video-pretraining advantage is untested.
- **minimal_experiment:** Compare matched image/video-pretrained encoders on equivariance spectra and dense transfer; perform mediation analysis (does equivariance statistically explain the transfer gap?).
- **main_risk:** Matched pairs are scarce; may require controlled pretraining at moderate scale.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0196

### W2-B-0223 — With enough readout training data, all VFMs converge to the same dense ceiling — testing the "representation doesn't matter" null.

- **problem:** Claims of dense superiority rest on low-data probes; whether differences persist as readout data grows (or all models saturate identically) determines if representation choice matters for data-rich users.
- **core_hypothesis:** Dense-performance gaps between VFMs shrink as readout training data increases, but do not vanish: a persistent representation-dependent gap remains at saturation, refuting the strong null while quantifying its partial truth.
- **why_important:** Tells data-rich practitioners whether backbone choice matters and calibrates how much low-data probe results extrapolate.
- **why_possibly_novel:** Readout-data scaling curves for frozen VFM dense performance are unpublished (UNVERIFIED — needs lit search).
- **minimal_experiment:** Train readouts across a data ladder (1k to 500k images) for several VFMs; fit saturation curves; measure persistent gaps and their task dependence.
- **main_risk:** Saturation may not be reached with feasible data; report extrapolated asymptotes with uncertainty.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0205

### W2-B-0224 — Register-equipped models have purer patch tokens: registers improve dense quality by relocating global garbage, a counterintuitive positive.

- **problem:** Registers were introduced to clean attention maps; whether they causally improve dense task transfer (by evacuating global information from patch tokens) or merely cosmetics is unresolved.
- **core_hypothesis:** At matched pretraining, register-equipped models show measurably higher patch-token class purity and better frozen dense transfer, with the gain concentrated in regions that previously hosted high-norm artifacts.
- **why_important:** Confirms or refutes a mechanism with direct implications for whether future VFMs should always include registers for dense users.
- **why_possibly_novel:** Causal dense-transfer evaluation of registers (beyond attention aesthetics) is incomplete (UNVERIFIED — needs lit search).
- **minimal_experiment:** Compare with/without-register checkpoints at matched recipes; measure patch purity, artifact geography, and dense transfer; localize gains spatially.
- **main_risk:** Matched checkpoint pairs are limited; supplement with controlled retraining.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0031

### W2-B-0225 — Contrastive spaces have cosine geometry but dense tasks need metric structure; the geometry-type mismatch is measurable and consequential.

- **problem:** Dense tasks implicitly require distances with metric properties (comparability, additivity along paths); contrastive training optimizes angular arrangement, potentially breaking metric requirements in ways never audited.
- **core_hypothesis:** Metric-recovery probes (estimating perceptual or physical distances from features) fail systematically on angularly-trained models relative to reconstruction-trained ones, and the metric-fidelity score predicts performance on continuous-structure dense tasks.
- **why_important:** A geometry-type taxonomy of VFMs would predict task fit at a deeper level than benchmark scores.
- **why_possibly_novel:** Geometry-type auditing (angular vs metric fidelity) of VFM spaces is new.
- **minimal_experiment:** Design metric-recovery batteries (physical distances, morph distances); score model families; correlate metric fidelity with continuous-dense-task transfer.
- **main_risk:** Ground-truth perceptual distances are noisy; anchor on physical ground truths where possible.
- **cluster:** `representation_mismatch`
- **mutate_from:** W2-B-0209

---

## 8. Cross-domain transfer of frozen vs tuned foundation features

Cluster key: `crossdomain_frozen_vs_tuned`

### W2-B-0226 — Frozen features degrade gracefully under shift while tuned features fail sharply, defining a measurable "shift budget" per model.

- **problem:** The frozen-vs-tuned choice is made on in-domain accuracy; the shape of degradation curves under increasing shift — gradual vs cliff-like — is the deployment-relevant property nobody reports.
- **core_hypothesis:** Tuned models' accuracy-vs-shift curves have steeper worst-case slopes and identifiable cliffs, while frozen-feature systems degrade near-linearly; each model admits a quantifiable shift budget before crossing below its frozen counterpart.
- **why_important:** Shift budgets belong on model cards: they convert an abstract robustness debate into a deployable number.
- **why_possibly_novel:** Curve-shape (not endpoint) comparison between frozen and tuned regimes is unstudied.
- **minimal_experiment:** Evaluate frozen-probe and fine-tuned versions of several VFMs across graded shift ladders (corruption severity, geographic distance, time); fit curve shapes; extract and validate shift budgets.
- **main_risk:** Shift ladders are hard to order objectively; use multiple orderings and report sensitivity.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0112

### W2-B-0227 — Fine-tuning on cleaner-labeled source data transfers worse: a label-quality paradox for cross-domain dense transfer.

- **problem:** Higher-quality source annotation is assumed universally beneficial; but precise labels may encourage fitting source-specific boundary conventions that generalize worse than noise-regularized fits.
- **core_hypothesis:** Models fine-tuned on precisely-annotated source segmentation transfer worse to differently-annotated target domains than models tuned on noisier labels, at matched source performance — a nonmonotonic label-quality effect.
- **why_important:** Challenges annotation-investment strategy: past a point, buying precision buys brittleness.
- **why_possibly_novel:** Label-quality-to-transfer nonmonotonicity is undocumented (UNVERIFIED — needs lit search).
- **minimal_experiment:** Fine-tune on source labels at controlled noise/precision levels; evaluate cross-domain transfer; map the transfer-vs-quality curve.
- **main_risk:** Synthetic label noise differs from natural annotation variation; include multi-annotator natural noise.
- **cluster:** `crossdomain_frozen_vs_tuned`

### W2-B-0228 — A factorial decomposition separates how much cross-domain gain comes from tuned features vs domain-specific readouts.

- **problem:** Comparisons of frozen-vs-tuned transfer confound backbone adaptation with readout adaptation, so the community cannot say which component earns the gains.
- **core_hypothesis:** A 2x2 design (frozen/tuned backbone x generic/domain-specific readout) shows most cross-domain gain attributable to readout adaptation for photometric shifts, with backbone tuning mattering only for semantic shifts.
- **why_important:** If readouts carry most transfer weight, expensive backbone tuning can often be skipped — a large practical saving.
- **why_possibly_novel:** The factorial attribution has apparently never been run cleanly (UNVERIFIED — needs lit search).
- **minimal_experiment:** Run the full factorial across several domain pairs and shift types; report component and interaction effects with multi-seed statistics.
- **main_risk:** Readout capacity choices affect the split; sweep readout sizes.
- **cluster:** `crossdomain_frozen_vs_tuned`

### W2-B-0229 — Which corruptions hurt a frozen VFM is predictable from the frequency profile of its pretraining augmentations.

- **problem:** Corruption robustness of frozen features is measured empirically per corruption; a predictive account tied to pretraining recipes would replace measurement with computation.
- **core_hypothesis:** A model's corruption-specific vulnerability correlates with the spectral overlap between each corruption's perturbation profile and the complement of its augmentation-covered perturbation space.
- **why_important:** Recipe-based robustness prediction lets users anticipate deployment failures without exhaustive testing.
- **why_possibly_novel:** Spectral augmentation-coverage theory for frozen-feature robustness is untested.
- **minimal_experiment:** Characterize augmentation and corruption frequency profiles; predict per-corruption degradation for models with known recipes; validate against measured frozen-probe robustness.
- **main_risk:** Nonlinear interactions between corruptions and features may defeat spectral-linear reasoning.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0034

### W2-B-0230 — Readout-only test-time adaptation captures most of backbone TTA's gains at a fraction of the catastrophic-failure risk.

- **problem:** Test-time adaptation methods update backbone statistics/weights and are known to collapse under some streams; whether the safer readout-only variant sacrifices much benefit is unquantified.
- **core_hypothesis:** Adapting only readout parameters (or feature post-transforms) at test time achieves a large fraction of full-TTA gains under common shifts while exhibiting near-zero collapse rates on pathological streams — a dominance on the risk-adjusted frontier.
- **why_important:** Establishes a safe-TTA default for dense deployments where collapse is unacceptable.
- **why_possibly_novel:** Risk-adjusted (not average-case) comparison of TTA loci is new.
- **minimal_experiment:** Compare backbone-TTA vs readout-TTA across shift benchmarks and adversarially-ordered streams; measure gains, collapse frequency, and recovery behavior.
- **main_risk:** Readout-TTA may fail exactly on severe shift where full TTA shines; report the conditional structure.
- **cluster:** `crossdomain_frozen_vs_tuned`

### W2-B-0231 — Feature-space domain-gap metrics predict tuned-model transfer but not frozen-feature transfer — the gap metric paradox.

- **problem:** Domain distances (FID-like, MMD) computed in frozen feature space are used to predict transferability generically, without asking which adaptation regime they are valid for.
- **core_hypothesis:** Measured domain gaps correlate strongly with fine-tuned transfer performance but weakly with frozen-probe transfer, because frozen readouts exploit invariant subspaces the global gap metric ignores.
- **why_important:** Prevents systematic misuse of gap metrics in the frozen regime, where they currently misinform model selection.
- **why_possibly_novel:** Regime-conditional validity analysis of domain-gap metrics is missing.
- **minimal_experiment:** Across many domain pairs, correlate gap metrics with both frozen and tuned transfer; identify the invariant-subspace explanation via subspace-restricted gap variants.
- **main_risk:** Correlations vary by task; use several dense tasks to establish generality.
- **cluster:** `crossdomain_frozen_vs_tuned`

### W2-B-0232 — Fine-tuning erases domain-general shape-sensitive channels first, mechanistically explaining the robustness cost of tuning.

- **problem:** Why tuned models lose cross-domain robustness lacks a channel-level account; if tuning selectively overwrites shape-processing channels (in favor of texture shortcuts), the loss is structured and preventable.
- **core_hypothesis:** Channels identified as shape-sensitive pre-tuning show disproportionate weight/function change during fine-tuning on texture-predictive datasets, and the shape-channel erasure rate predicts the model's OOD drop.
- **why_important:** A mechanistic target for robustness-preserving fine-tuning: protect identified channels rather than all weights.
- **why_possibly_novel:** Channel-functional attribution of tuning-induced robustness loss is new.
- **minimal_experiment:** Identify shape/texture channels via probing; track their drift during fine-tuning; correlate erasure with OOD degradation; test selective protection.
- **main_risk:** Channel functions are distributed; use population-level rather than single-channel claims.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0016

### W2-B-0233 — Fine-tuning on Western-centric data degrades non-Western-scene dense performance below the frozen baseline — adaptation as fairness regression.

- **problem:** Geographic bias is studied for classifiers; whether adaptation actively worsens geographic equity relative to leaving models frozen is unmeasured for dense tasks.
- **core_hypothesis:** Models fine-tuned on geographically-skewed segmentation data lose more accuracy on underrepresented regions than they gain on represented ones relative to frozen probes, making tuning a net equity regression under skewed data.
- **why_important:** Deployment guidance for global products: when adaptation data is skewed, frozen features may be the fairer choice.
- **why_possibly_novel:** The frozen-vs-tuned equity comparison is unexplored.
- **minimal_experiment:** Fine-tune on region-skewed driving/scene data; evaluate per-region dense metrics vs frozen baselines; quantify the equity delta and its scaling with skew.
- **main_risk:** Region-stratified dense benchmarks are scarce; may need annotation investment.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0118

### W2-B-0234 — The frozen-vs-tuned crossover forms a smooth 2D phase boundary in the (data size, domain gap) plane.

- **problem:** Practitioners face a binary choice with two continuous inputs — how much target data, how far the domain — but no map of which choice wins where.
- **core_hypothesis:** The crossover locus is a monotone curve: required data size for tuning to win grows with domain proximity paradoxically (near domains: frozen suffices longer) and shrinks with gap up to a reversal at extreme gaps where nothing transfers.
- **why_important:** A validated decision chart directly usable by every adaptation project.
- **why_possibly_novel:** Empirical phase-boundary mapping for the frozen/tuned decision is new.
- **minimal_experiment:** Grid experiments across data sizes and measured domain gaps on dense tasks; fit the boundary; validate on held-out domains and a second backbone.
- **main_risk:** The boundary may be task-family-specific; produce per-family charts.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0127

### W2-B-0235 — Multi-source fine-tuning underperforms best-single-source when sources conflict in low-level statistics, predictably.

- **problem:** More source domains are assumed better for transfer; negative interactions between statistically-conflicting sources are anecdotal, lacking a predictive criterion.
- **core_hypothesis:** When source domains disagree in low-level statistics (noise, color distributions) beyond a threshold, multi-source tuning produces internal normalization compromises that transfer worse than the best single source — and the conflict measure predicts when.
- **why_important:** A source-selection criterion prevents wasted data mixing and degraded deployments.
- **why_possibly_novel:** Statistical-conflict-based negative-transfer prediction for dense adaptation is untested.
- **minimal_experiment:** Construct source sets with controlled statistical conflict; compare multi-source vs single-source transfer; validate the conflict-measure threshold across targets.
- **main_risk:** Semantic complementarity may offset statistical conflict; model both factors jointly.
- **cluster:** `crossdomain_frozen_vs_tuned`

### W2-B-0236 — The freeze-early-layers heuristic inverts under sensor shift: early layers are exactly what needs tuning.

- **problem:** "Freeze early, tune late" is standard advice inherited from semantic-transfer settings; for sensor/photometric shifts the required adaptation may live early, making the heuristic backwards.
- **core_hypothesis:** Under sensor-style shifts, tuning only early layers beats tuning only late layers at matched budgets, reversing the ordering observed under semantic shifts — a shift-type-to-depth correspondence.
- **why_important:** Depth-allocation guidance conditioned on shift type would correct a widespread default.
- **why_possibly_novel:** Systematic shift-type-conditional depth-allocation studies are missing.
- **minimal_experiment:** Adapt early-only/late-only/full across shift-type-controlled benchmarks (sensor vs semantic); map winning allocation; connect to layer-drift diagnostics.
- **main_risk:** Compound real shifts mix types; validate on natural compound cases.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0132

### W2-B-0237 — RGB-to-infrared transfer failure of frozen VFMs is mostly a first-order statistics mismatch, recoverable without tuning.

- **problem:** Cross-spectral reuse of VFMs is assumed to need retraining; if failure is dominated by input-statistics mismatch rather than semantic incompatibility, cheap input-space corrections could suffice.
- **core_hypothesis:** Statistic-matching input transforms (histogram/channel alignment estimated without labels) recover a majority of the frozen-feature performance gap on IR dense tasks, leaving a small semantic residual only for classes with genuinely different IR signatures.
- **why_important:** Enables cheap cross-spectral deployment of frozen VFMs and quantifies what actually requires learning.
- **why_possibly_novel:** A decomposition of cross-spectral failure into statistical vs semantic components is new.
- **minimal_experiment:** Evaluate frozen probes on IR benchmarks with/without unsupervised input alignment; decompose remaining errors by class; compare against tuned baselines.
- **main_risk:** Some IR content has no RGB analogue (thermal signatures); the residual analysis handles this explicitly.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0034

### W2-B-0238 — Sequential domain fine-tuning is path-dependent — domain order changes the final model — while frozen readouts are order-free.

- **problem:** Real systems adapt through domain sequences (winter to summer, sensor upgrades); whether the endpoint depends on the path is unknown, with implications for reproducibility and rollback.
- **core_hypothesis:** Models tuned through different orderings of the same domain set end at functionally different solutions (measurable prediction disagreement and per-domain performance spread), exhibiting hysteresis absent in frozen-readout systems.
- **why_important:** Path dependence means deployment history matters — an underappreciated liability of tuning that frozen pipelines avoid.
- **why_possibly_novel:** Hysteresis quantification for domain-sequence adaptation is new.
- **minimal_experiment:** Permute domain orders in sequential fine-tuning; measure endpoint disagreement and per-domain metrics; contrast with frozen-readout sequential systems.
- **main_risk:** Path effects may shrink with replay; test with and without.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0147

### W2-B-0239 — The ID-OOD linear trend ("accuracy on the line") breaks for dense tasks: boundary metrics leave the line.

- **problem:** The effective-robustness framework (linear ID-OOD relationships) guides robustness research but was established on classification; whether dense tasks and their sub-metrics follow it is unverified (UNVERIFIED — needs lit search).
- **core_hypothesis:** Interior-region dense metrics follow an approximately linear ID-OOD trend across models, but boundary metrics deviate systematically — models trade boundary robustness differently — breaking single-line summaries for dense prediction.
- **why_important:** Determines whether classification-era robustness tools apply to segmentation, or dense robustness needs its own framework.
- **why_possibly_novel:** Effective-robustness analysis for dense sub-metrics is missing.
- **minimal_experiment:** Evaluate a large model zoo on paired ID/OOD dense benchmarks; fit trends per sub-metric (mIoU, boundary F1, per-class); characterize deviations.
- **main_risk:** OOD dense benchmarks are fewer; construct additional shifted pairs.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0226

### W2-B-0240 — Robustness lost to fine-tuning has a price in labels: quantifying the target-data cost of buying back frozen-level robustness.

- **problem:** Tuning gains task accuracy but loses robustness; the exchange rate — how many labeled target-domain examples restore the lost robustness — has never been priced.
- **core_hypothesis:** Restoring a tuned model to frozen-level OOD robustness via additional diverse-domain labels requires an amount of data growing superlinearly with the original fine-tuning dose, making robustness cheaper to preserve than to repurchase.
- **why_important:** A robustness accounting framework turning vague tradeoffs into budget numbers for project planning.
- **why_possibly_novel:** Label-denominated robustness pricing is a new framing.
- **minimal_experiment:** Fine-tune at varying doses; measure robustness loss; incrementally add diverse labeled data until robustness recovers; fit the repurchase-cost curve.
- **main_risk:** "Diverse data" composition affects costs; standardize diversity protocols.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0226

### W2-B-0241 — Frozen features win under style shift, tuned features win under content shift — a clean double dissociation.

- **problem:** "Domain shift" conflates style (texture, color, sensor) and content (object statistics, layouts) changes; the frozen-vs-tuned choice may flip between them, hidden by aggregated benchmarks.
- **core_hypothesis:** On shift suites decomposed into style-only and content-only components (via controlled generation and dataset curation), frozen probes dominate style shifts while tuned models dominate content shifts, at matched in-domain accuracy.
- **why_important:** A shift-typed decision rule directly improves adaptation choices in practice.
- **why_possibly_novel:** The style/content double dissociation for adaptation regimes is untested.
- **minimal_experiment:** Build style-only and content-only shifted pairs; evaluate both regimes across backbones; test the dissociation and its boundary cases.
- **main_risk:** Pure style/content separation is imperfect; quantify leakage between components.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0234

### W2-B-0242 — Much of measured "domain gap" in dense transfer is annotation-convention gap, exposed by cross-dataset same-domain transfer.

- **problem:** Cross-dataset drops are attributed to visual domain differences, but datasets also differ in labeling conventions (class definitions, boundary placement rules) — a confound rarely separated.
- **core_hypothesis:** Transfer between visually-similar datasets with different conventions (e.g., two urban-driving sets) shows drops comparable to genuine visual shifts, and convention-harmonized re-annotation of evaluation subsets recovers a large share of the drop.
- **why_important:** Re-attributes part of the domain-adaptation problem to label semantics, changing what methods should target.
- **why_possibly_novel:** Convention-vs-appearance decomposition of cross-dataset drops is rarely quantified (UNVERIFIED — needs lit search).
- **minimal_experiment:** Cross-evaluate models between visually-matched dataset pairs; re-annotate subsets under unified conventions; decompose the drop into convention vs appearance components.
- **main_risk:** Re-annotation is costly; small carefully-chosen subsets suffice for decomposition.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0227

### W2-B-0243 — Language-described domain shifts can be neutralized through text-space steering of frozen features — but only when the shift is nameable.

- **problem:** Text-aligned VFMs offer a unique free lever: describing the shift ("a foggy road scene") to re-anchor classification of dense features; when this works versus fails is uncharacterized.
- **core_hypothesis:** Text-conditioned adjustment of class embeddings recovers significant frozen-probe performance under nameable shifts (fog, night, snow) but none under unnameable statistical shifts (sensor noise profiles), locating a nameability boundary for language-based adaptation.
- **why_important:** Defines the scope of a zero-training adaptation tool and connects linguistic expressibility to domain robustness.
- **why_possibly_novel:** The nameability boundary for text-steered dense adaptation is unmapped.
- **minimal_experiment:** Compare text-steered vs plain frozen inference across nameable and unnameable shift suites; correlate recovery with human nameability ratings of each shift.
- **main_risk:** Prompt engineering variance; marginalize over description sets.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0018

### W2-B-0244 — Cross-family frozen ensembles beat any single tuned model OOD at matched inference compute.

- **problem:** The compute spent fine-tuning could instead buy inference-time diversity (ensembling frozen heterogeneous backbones); the OOD comparison at matched total budget has not been made.
- **core_hypothesis:** An ensemble of frozen probes over diverse pretraining families matches tuned single models in-domain and exceeds them OOD at equal inference FLOPs, because pretraining diversity provides robustness that single-model tuning destroys.
- **why_important:** Challenges the default adapt-one-model paradigm for robustness-critical dense deployments.
- **why_possibly_novel:** Budget-matched frozen-diversity vs tuned-single comparisons are missing.
- **minimal_experiment:** Build frozen ensembles (CLIP, DINOv2, MAE probes) matched in FLOPs to tuned baselines; evaluate ID and across shift suites; decompose ensemble gains by member diversity.
- **main_risk:** Latency structure differs from FLOPs; report both budgets.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0134

### W2-B-0245 — Per-input routing between frozen and tuned models is a large untapped gain, quantifiable with an oracle-routing gap.

- **problem:** Frozen and tuned models err on different inputs; systems deploy one or the other globally, leaving the complementarity unexploited and even unmeasured.
- **core_hypothesis:** An oracle choosing per-input between frozen and tuned predictions exceeds both by a wide margin under mixed-shift streams, and a feature-distance-based router captures a substantial fraction of the oracle gap.
- **why_important:** Establishes input-conditional regime selection as a practical middle path in the frozen-vs-tuned debate.
- **why_possibly_novel:** Oracle-gap quantification for adaptation-regime routing is new.
- **minimal_experiment:** Measure oracle and learned-router gains over frozen/tuned pairs across mixed-domain streams; analyze which inputs favor which regime.
- **main_risk:** Router errors could erase gains; report risk-adjusted performance.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0129

### W2-B-0246 — Temperature calibration transfers across domains for frozen features but breaks for tuned models.

- **problem:** Calibration is tuned on source validation data and assumed to hold on target domains; whether calibration transferability differs by adaptation regime is unexamined.
- **core_hypothesis:** Source-fitted temperature/vector calibration remains near-optimal on shifted targets for frozen-probe systems but drifts substantially for tuned models, because tuning couples confidence geometry to source specifics.
- **why_important:** Calibration-transfer behavior belongs in the frozen-vs-tuned decision, especially for risk-sensitive dense applications.
- **why_possibly_novel:** Regime-conditional calibration transferability is unstudied.
- **minimal_experiment:** Fit calibration on source; measure calibration drift across targets for frozen vs tuned systems on dense and global tasks; explain drift via confidence-geometry analysis.
- **main_risk:** Calibration metrics on segmentation need careful pixel-vs-region definitions; report both.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0108

### W2-B-0247 — Low-shot target tuning erodes exactly the long-tail classes that OOD scenes contain, an interaction hidden by average metrics.

- **problem:** Few-shot target adaptation optimizes head classes present in the small target set; its effect on tail classes — disproportionately important in the target's own rare-but-critical scenes — is unmeasured.
- **core_hypothesis:** After low-shot tuning, per-class deltas correlate negatively with class rarity: head classes improve while tail classes fall below frozen-baseline levels, and the tail erosion grows as shot count shrinks.
- **why_important:** Warns that the most common adaptation practice (few-shot tuning) may be worst for the classes that matter most in safety terms.
- **why_possibly_novel:** Rarity-resolved accounting of few-shot adaptation effects is new.
- **minimal_experiment:** Few-shot tune across shot ladders; measure per-class deltas vs rarity; compare against frozen and PEFT baselines; test tail-protective mixing.
- **main_risk:** Tail metrics are high-variance; use many episodes and pooled statistics.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0233

### W2-B-0248 — Feature-space augmentation during readout training substitutes for pixel-space domain randomization at a fraction of the cost.

- **problem:** Domain randomization requires expensive image-space rendering/augmentation and full forward passes; augmenting frozen features directly could buy similar robustness cheaply, but validity is unestablished.
- **core_hypothesis:** Readouts trained with feature-space perturbations (noise, interpolation, style statistics swaps in feature space) match pixel-space-randomization robustness on moderate shifts at an order of magnitude less compute, failing only on shifts that alter feature topology.
- **why_important:** Makes robust readout training accessible at low budgets and clarifies which shift effects are feature-linear.
- **why_possibly_novel:** A validity study of feature-space randomization against pixel-space ground truth is missing.
- **minimal_experiment:** Train readouts under matched-strength feature-space vs pixel-space augmentation; compare robustness across shift suites; identify the failure boundary.
- **main_risk:** Feature-space perturbation calibration to realistic shifts is nontrivial; anchor with paired shifted data.
- **cluster:** `crossdomain_frozen_vs_tuned`

### W2-B-0249 — Under gradual real-world drift, frozen systems age linearly while tuned systems age in steps — different maintenance regimes.

- **problem:** Deployment domains drift continuously (seasons, device wear, practice changes); the temporal degradation profile of frozen vs tuned dense systems determines monitoring and retraining schedules but is unmeasured.
- **core_hypothesis:** On time-stamped datasets, frozen-readout performance declines smoothly and predictably with temporal distance, while tuned models hold then drop abruptly when drift crosses their fitted specifics — implying different optimal maintenance policies per regime.
- **why_important:** Converts the frozen-vs-tuned debate into operational maintenance guidance (predictable decay vs cliff monitoring).
- **why_possibly_novel:** Temporal aging-profile comparison across adaptation regimes is new.
- **minimal_experiment:** Use time-stamped satellite/street/medical archives; train at time zero in both regimes; evaluate along the time axis; fit and compare decay profiles.
- **main_risk:** Temporal shifts entangle content and style; decompose using the style/content tools.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0241

### W2-B-0250 — Fine-tuning drags shape-biased VFMs toward texture bias, and the bias trajectory predicts the sim-to-real gap.

- **problem:** Sim-to-real transfer degrades after synthetic-data fine-tuning for reasons beyond pixel realism; a shift in the model's cue preference (shape to texture) may be the mediating variable.
- **core_hypothesis:** Cue-conflict bias measured along the fine-tuning trajectory drifts toward texture on synthetic data, and the drift magnitude predicts the final sim-to-real dense gap better than image-realism metrics of the training data.
- **why_important:** A monitorable mediator would let sim-training pipelines correct course before expensive real-world evaluation.
- **why_possibly_novel:** Bias-trajectory mediation analysis of sim-to-real failure is new.
- **minimal_experiment:** Fine-tune on graded-realism synthetic sets; track cue-conflict bias and sim-to-real gaps; test mediation statistically; compare against realism-metric baselines.
- **main_risk:** Bias measures on dense models need adaptation from classification protocols; validate the transfer of the metric.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0016

### W2-B-0251 — The best extraction layer for frozen transfer moves earlier as domain gap grows — a depth-gap law.

- **problem:** Layer selection for frozen readouts is tuned in-domain; if optimal depth systematically shifts with domain distance, in-domain tuning misconfigures every OOD deployment.
- **core_hypothesis:** Across domain ladders, the optimal readout layer depth decreases monotonically with measured domain gap (late layers overfit pretraining semantics; earlier layers generalize), with a slope stable enough to select layers from gap estimates alone.
- **why_important:** A simple pre-deployment rule (measure gap, pick layer) improving frozen transfer for free.
- **why_possibly_novel:** The depth-gap relationship has not been characterized.
- **minimal_experiment:** Probe all layers across domain ladders for several VFMs; fit depth-vs-gap curves; validate gap-based layer selection on held-out domains.
- **main_risk:** Non-monotonic exceptions may exist for semantic-heavy shifts; characterize exception classes.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0218

### W2-B-0252 — Weight interpolation between pretrained and tuned models sweeps a frontier whose concavities reveal distinct adaptation mechanisms.

- **problem:** Interpolation is used as a robustness trick; the shape of the ID-vs-OOD frontier it traces (convex, concave, kinked) encodes information about what fine-tuning changed, never analyzed as evidence.
- **core_hypothesis:** Interpolation frontiers exhibit reproducible kinks at coefficients where specific ability families (per earlier forgetting chronology) switch on/off, indicating discrete mechanism transitions rather than smooth feature blending.
- **why_important:** Turns a practical trick into a measurement instrument for adaptation structure, and identifies optimal operating points beyond the naive sweep.
- **why_possibly_novel:** Frontier-shape analysis as mechanistic evidence is new.
- **minimal_experiment:** Trace fine-grained interpolation frontiers across tasks/models; detect kinks statistically; align kink locations with ability-battery transitions; test reproducibility across seeds.
- **main_risk:** Kinks may be smoothed by high-dimensional averaging; use per-layer interpolation to sharpen.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0165

### W2-B-0253 — A learned input transform alone (frozen backbone, frozen readout) recovers most tuning gains under sensor shift.

- **problem:** The minimal sufficient intervention for sensor-style domain gaps is unknown; if a small input-space transform suffices, the entire backbone-adaptation apparatus is overkill for a large class of shifts.
- **core_hypothesis:** Training only a lightweight input transform (per-channel curves, small convolutional corrector) with the rest frozen recovers the majority of full fine-tuning's gain on sensor/photometric shifts, but almost none on semantic shifts — cleanly bounding where input-space adaptation suffices.
- **why_important:** The cheapest possible adaptation, deployable even where model weights are locked (API models, certified systems).
- **why_possibly_novel:** Sufficiency analysis of input-only adaptation across shift types is new for VFM dense pipelines.
- **minimal_experiment:** Train input transforms across shift-type-controlled dense benchmarks with everything else frozen; compare against PEFT/full-FT; map the sufficiency boundary.
- **main_risk:** Input transforms may exploit label leakage on small targets; validate with strict splits.
- **cluster:** `crossdomain_frozen_vs_tuned`
- **mutate_from:** W2-B-0237

---

## 9. Synthetic data for adapting foundation models

Cluster key: `synthetic_adaptation`

### W2-B-0254 — Synthetic training data buys mean accuracy but sells calibration: generated-data adaptation systematically miscalibrates dense models.

- **problem:** Synthetic-data papers report accuracy gains; the calibration of models adapted on generated images is essentially unaudited, though mode-collapsed generators plausibly distort confidence structure.
- **core_hypothesis:** At matched accuracy, models adapted with synthetic data show significantly worse ECE and overconfidence on real-data tails, because generators underrepresent exactly the ambiguous cases that teach calibrated uncertainty.
- **why_important:** If synthetic data silently trades calibration for accuracy, every safety-relevant use needs recalibration protocols — a field-wide practice change.
- **why_possibly_novel:** Calibration accounting for synthetic-data adaptation is missing (UNVERIFIED — needs lit search).
- **minimal_experiment:** Adapt segmentation models on real/synthetic/mixed data at matched accuracy; compare calibration on real test sets stratified by ambiguity; test whether real-data recalibration repairs the deficit.
- **main_risk:** Accuracy matching across data sources requires careful budget control.
- **cluster:** `synthetic_adaptation`

### W2-B-0255 — Generator-model circularity: adapting VFMs on data from generators trained on the same corpora creates measurable self-confirmation bias.

- **problem:** Diffusion generators and VFMs share pretraining data lineages; adaptation on generated images may reinforce shared biases rather than add information — an inbreeding effect nobody quantifies.
- **core_hypothesis:** Gains from synthetic adaptation shrink as generator-VFM pretraining overlap grows, and adapted models show amplified agreement with generator biases (measured on bias batteries) relative to real-data adaptation.
- **why_important:** Establishes lineage-awareness as a requirement for synthetic data pipelines, preventing circular self-training at ecosystem scale.
- **why_possibly_novel:** Data-lineage circularity effects in the VFM-generator ecosystem are unstudied.
- **minimal_experiment:** Adapt VFMs on images from generators with varied training-corpus overlap; measure gain vs overlap and bias amplification on controlled batteries.
- **main_risk:** Overlap estimation for closed generators is coarse; anchor with open-data generator pairs.
- **cluster:** `synthetic_adaptation`

### W2-B-0256 — Synthetic rare-class examples fix presence detection but corrupt boundary statistics — a split verdict hidden by mIoU.

- **problem:** Synthetic data is prescribed for rare classes; generated boundaries are systematically smoother than real ones, so the intervention may help detection while degrading localization.
- **core_hypothesis:** Rare-class synthetic augmentation raises detection recall but measurably degrades boundary F1 for those same classes, because generated boundary statistics diverge from real ones — a decomposition invisible to mIoU.
- **why_important:** Practitioners need the decomposed verdict to decide whether synthetic augmentation serves their metric.
- **why_possibly_novel:** Metric-decomposed evaluation of synthetic augmentation is new.
- **minimal_experiment:** Augment rare classes with generated images; evaluate recall vs boundary metrics separately; measure boundary-statistics divergence between real and synthetic instances.
- **main_risk:** Boundary effects may vanish with better generators; report generator-version dependence.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0254

### W2-B-0257 — Models adapted on diffusion data partly learn generator frequency fingerprints, and fingerprint removal changes what was learned.

- **problem:** Diffusion images carry spectral artifacts; adapted models may key on these fingerprints rather than content, silently overfitting the generator instead of the domain.
- **core_hypothesis:** A measurable fraction of synthetic-adaptation gain evaporates when evaluation images are fingerprint-filtered (or when training data is fingerprint-removed), quantifying fingerprint reliance per generator-model pair.
- **why_important:** Fingerprint reliance would explain sim-to-real inconsistencies of synthetic pipelines and mandate spectral hygiene in data generation.
- **why_possibly_novel:** Fingerprint-reliance decomposition of synthetic-data gains is untested.
- **minimal_experiment:** Adapt with raw vs fingerprint-filtered synthetic data; evaluate on real and filtered test sets; decompose gains into content vs fingerprint components.
- **main_risk:** Filtering may remove legitimate high-frequency content; use matched-content controls.
- **cluster:** `synthetic_adaptation`

### W2-B-0258 — Per-class generation quality predicts per-class adaptation gain, making synthetic-data value predictable before training.

- **problem:** Synthetic augmentation is applied uniformly across classes although generators produce some classes (nameable objects) far better than others (stuff, fine structures); a predictive value model is missing.
- **core_hypothesis:** Per-class synthetic-adaptation gain correlates strongly with per-class generation fidelity metrics, enabling a pre-training value estimate that allocates generation budget to classes where it will pay.
- **why_important:** Converts synthetic-data strategy from blanket generation to targeted investment with predicted returns.
- **why_possibly_novel:** Class-level value prediction for synthetic dense data is new.
- **minimal_experiment:** Measure per-class generation fidelity (human and automatic); adapt with class-stratified synthetic data; fit and validate the fidelity-to-gain predictor.
- **main_risk:** Fidelity metrics may miss task-relevant attributes; include probe-based fidelity.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0256

### W2-B-0259 — The real-data fraction, not total data volume, is the binding variable in mixed real-synthetic adaptation — a mixing law.

- **problem:** Mixed-data recipes are tuned ad hoc; a functional law relating performance to (real fraction, total volume) would replace search and reveal whether synthetic data substitutes or merely dilutes.
- **core_hypothesis:** Performance follows a law where synthetic data acts as a diminishing-returns supplement whose value scales with real-data scarcity: at fixed real count, synthetic additions saturate quickly; at fixed total, performance depends dominantly on the real fraction.
- **why_important:** A validated mixing law is immediately actionable for every adaptation pipeline weighing generation costs against collection costs.
- **why_possibly_novel:** Parametric mixing laws for dense adaptation are unfitted (UNVERIFIED — needs lit search).
- **minimal_experiment:** Grid real/synthetic mixtures across totals for segmentation adaptation; fit candidate laws; validate on held-out domains and a second generator.
- **main_risk:** The law may be domain-dependent; test transferability of fitted parameters.
- **cluster:** `synthetic_adaptation`

### W2-B-0260 — Caption-conditioned generation imports language co-occurrence priors into images, and adapted models inherit them as dense hallucinations.

- **problem:** Text-to-image data inherits linguistic co-occurrence structure (beaches with umbrellas); adaptation on such data may teach spurious spatial expectations measurable in dense predictions.
- **core_hypothesis:** Models adapted on caption-generated data show elevated contextual false positives (segmenting expected-but-absent objects) relative to real-data adaptation, with the effect size predictable from the caption corpus's co-occurrence statistics.
- **why_important:** Identifies a hallucination-transmission channel from language through generation into dense vision — an ecosystem-level contamination path.
- **why_possibly_novel:** Language-prior transmission through synthetic images into dense predictions is untested.
- **minimal_experiment:** Adapt on caption-generated vs layout-controlled synthetic data; measure contextual false-positive rates on scenes violating co-occurrence priors; trace effects to corpus statistics.
- **main_risk:** Real data has co-occurrence structure too; the comparison isolates the amplification.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0255

### W2-B-0261 — The tradeoff frontier between perfect-label synthetic data and noisy-label real data is measurable and task-dependent.

- **problem:** Teams choose between cheap synthetic images with exact labels and real images with imperfect annotation; the exchange rate between label quality and domain realism has never been mapped.
- **core_hypothesis:** For boundary-sensitive tasks the frontier favors noisy real data (realistic boundary statistics dominate), while for region-classification tasks perfect-label synthetic data wins at equal budget — a task-conditional frontier with a measurable crossover in annotation-noise level.
- **why_important:** A decision chart for the most common practical data question in dense-model adaptation.
- **why_possibly_novel:** The label-quality-vs-realism frontier is uncharted.
- **minimal_experiment:** Adapt across a grid of (synthetic perfect-label, real noisy-label at controlled noise) mixtures; map performance frontiers per task type; validate the crossover prediction.
- **main_risk:** Controlled real-label noise must mimic natural annotation error; use multi-annotator data.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0227

### W2-B-0262 — Using the VFM to filter its own synthetic training data amplifies selection bias measurably per closed-loop round.

- **problem:** Quality-filtering generated data with the same foundation model being adapted creates a feedback loop favoring images the model already handles — a bias amplifier disguised as quality control.
- **core_hypothesis:** Model-filtered synthetic data yields better in-distribution metrics but progressively worse coverage of the model's current failure modes, and each filter-adapt round measurably narrows the error-type distribution the model can fix.
- **why_important:** Warns against a nearly-universal pipeline pattern and motivates filter-model independence requirements.
- **why_possibly_novel:** Round-by-round selection-bias accounting in self-filtered adaptation is new.
- **minimal_experiment:** Run filter-adapt loops with self vs independent filter models; track failure-mode coverage and per-round gain decay; quantify the bias amplification rate.
- **main_risk:** Effects may need several rounds to appear; budget for multi-round experiments.
- **cluster:** `synthetic_adaptation`

### W2-B-0263 — Generated corruptions transfer worse than procedural corruptions for robustness training, despite superior realism.

- **problem:** Diffusion models can render realistic fog/rain/night for robustness training, presumably better than procedural filters; but realism may not be the property that transfers robustness.
- **core_hypothesis:** Training on procedurally-corrupted images yields better real-corruption robustness than training on more realistic generated corruptions at matched severity coverage, because procedural corruptions preserve the underlying scene's true structure while generation subtly rewrites it.
- **why_important:** Counterintuitive guidance saving compute (procedural is cheap) and correcting a plausible-but-wrong pipeline upgrade path.
- **why_possibly_novel:** The realism-vs-transfer dissociation for corruption training is untested.
- **minimal_experiment:** Train on procedural vs generated corruption variants of the same scenes; evaluate on real adverse-condition benchmarks; analyze structure-preservation differences.
- **main_risk:** Generation quality varies; use several generators and severity calibration.
- **cluster:** `synthetic_adaptation`

### W2-B-0264 — Synthetic medical data for adaptation launders privacy: adapted models retain extractable patient features from the generator's training set.

- **problem:** Sharing generated medical images is treated as privacy-preserving; whether models adapted on such data inherit membership signals of the generator's real patients is unaudited.
- **core_hypothesis:** Membership-inference attacks against the generator's training patients succeed above chance when run against downstream models adapted only on generated images — demonstrating privacy leakage through the synthetic-data channel.
- **why_important:** A positive result would undermine current regulatory assumptions about synthetic medical data; a robust null would support them — either outcome matters.
- **why_possibly_novel:** Transitive privacy-leakage measurement through synthetic adaptation is new for dense medical models.
- **minimal_experiment:** Train generators on known patient sets; adapt segmentation models on generated data; attack downstream models for generator-set membership; quantify leakage vs generation volume.
- **main_risk:** Attack sensitivity may be low; use strong attacks and controlled duplicates as positive controls.
- **cluster:** `synthetic_adaptation`

### W2-B-0265 — Diffusion training data violates geometric consistency (shadows, reflections, perspective), and adapted models lose geometric-reasoning probes.

- **problem:** Generated scenes often contain physically inconsistent lighting and geometry; models adapted on them may unlearn geometric regularities that real-data models absorb implicitly.
- **core_hypothesis:** Models adapted heavily on generated data score measurably worse on geometric-consistency probes (shadow-object direction agreement, reflection plausibility, vanishing-point coherence) than real-data-adapted controls at matched task accuracy.
- **why_important:** Geometric degradation is invisible to standard benchmarks but critical for embodied and forensic applications.
- **why_possibly_novel:** Geometric-consistency cost accounting of synthetic adaptation is unexplored.
- **minimal_experiment:** Build geometric-consistency probe batteries; compare models adapted on real vs generated data at matched accuracy; correlate degradation with measured inconsistency rates in the training data.
- **main_risk:** Probes must isolate geometry from style; validate probes on physically-rendered controls.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0263

### W2-B-0266 — Dense adaptation prefers generator diversity over fidelity: the optimal guidance scale for data generation is far below the aesthetic optimum.

- **problem:** Generation hyperparameters (guidance scale) are tuned for image quality; dense-adaptation value may peak at uglier-but-more-diverse settings, meaning pipelines systematically generate the wrong data.
- **core_hypothesis:** Adaptation performance as a function of guidance scale peaks at low values (high diversity, lower fidelity) for dense tasks, while classification-style adaptation peaks higher — a task-dependent dissociation in optimal generation settings.
- **why_important:** A free improvement to every text-to-image data pipeline: change one number, generate better training data.
- **why_possibly_novel:** Task-conditional generation-parameter optimization for adaptation is new.
- **minimal_experiment:** Generate datasets across guidance-scale grids; adapt dense and classification models on each; map performance-vs-scale curves per task family.
- **main_risk:** Guidance interacts with prompt distribution; sweep both jointly at reduced resolution.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0259

### W2-B-0267 — The real-image exchange rate of synthetic data can worsen as generators improve, when improvement means mode-conformity.

- **problem:** Generator progress is assumed to increase synthetic data's value; but progress measured by fidelity often means tighter mode-conformity, reducing the coverage that adaptation actually needs.
- **core_hypothesis:** Across generator generations, the exchange rate (real images equivalent per thousand synthetic) is non-monotonic: mid-generation models with broader mode coverage provide more adaptation value than newer, higher-fidelity but mode-narrower successors.
- **why_important:** Challenges automatic pipeline upgrades to the latest generator and provides an exchange-rate measurement protocol.
- **why_possibly_novel:** Longitudinal exchange-rate tracking across generator versions is unmeasured (UNVERIFIED — needs lit search).
- **minimal_experiment:** Adapt identical pipelines using data from successive open generator versions; estimate exchange rates via real-data-equivalence matching; correlate with independently-measured mode coverage.
- **main_risk:** Version differences bundle many changes; complement with coverage-controlled ablations.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0266

### W2-B-0268 — Benchmark contamination by synthetic imagery is rising and measurable, distorting adaptation research conclusions.

- **problem:** Web-scraped evaluation and adaptation sets increasingly contain AI-generated images; the contamination rate and its effect on measured adaptation performance are unquantified — a data-ecology problem for the field.
- **core_hypothesis:** Newer web-collected dense benchmarks contain a detectable and growing fraction of generated images, and models adapted on synthetic data score inflated results on contaminated subsets, biasing method comparisons.
- **why_important:** Establishes contamination auditing as a prerequisite for trustworthy benchmarks in the generative era.
- **why_possibly_novel:** Contamination-effect measurement on dense benchmark validity is new.
- **minimal_experiment:** Apply generated-image detectors to benchmark suites by collection date; compare method rankings on contaminated vs clean subsets; estimate ranking distortion.
- **main_risk:** Detector reliability limits estimates; use ensembles and manual verification samples.
- **cluster:** `synthetic_adaptation`

### W2-B-0269 — Closed-loop prompt tuning on generated images amplifies language bias into measurable prompt brittleness.

- **problem:** A tempting pipeline tunes VLM prompts using text-to-image generated validation data; both sides share language priors, so the loop may optimize prompts toward shared bias rather than visual truth.
- **core_hypothesis:** Prompts tuned on generated validation sets show inflated validation scores but degraded real-data performance and increased paraphrase sensitivity, with the inflation proportional to generator-VLM lineage overlap.
- **why_important:** Documents a specific, likely-common contamination pattern in VLM adaptation workflows before it becomes standard practice.
- **why_possibly_novel:** Closed-loop language-bias amplification through generated validation data is untested.
- **minimal_experiment:** Tune prompts on real vs generated validation sets; compare real-test performance and paraphrase robustness; vary generator lineage to test the overlap prediction.
- **main_risk:** Effect may be small for simple tasks; focus on dense and compositional tasks.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0262

### W2-B-0270 — Synthetic hard negatives — near-boundary composites — are worth an order of magnitude more than generic synthetic images for boundary learning.

- **problem:** Synthetic data value is treated as homogeneous per image; targeted generation of the specific structures models fail on (boundary-adjacent compositions, occlusion edges) may concentrate nearly all the value.
- **core_hypothesis:** Training with small quantities of composition-controlled boundary-hard synthetic examples improves boundary F1 more than 10x the volume of generic generated scenes, establishing a value-density hierarchy for synthetic data types.
- **why_important:** Shifts generation budgets from volume to targeting, with large efficiency gains for boundary-critical applications.
- **why_possibly_novel:** Value-density comparison across synthetic data types for dense tasks is new.
- **minimal_experiment:** Generate generic vs boundary-targeted synthetic sets; adapt at matched budgets; compare boundary-metric gains per image; characterize which targeted structures pay most.
- **main_risk:** Composite realism artifacts may limit gains; compare cut-paste vs generative compositing.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0256

### W2-B-0271 — Domain-targeted generation works only for nameable shifts: the generation route inherits the same nameability boundary as text steering.

- **problem:** Generating shifted training data ("the same scene, foggy") is a popular adaptation strategy; its scope condition — which shifts generators can actually render faithfully — is unmapped and likely mirrors linguistic expressibility.
- **core_hypothesis:** Adaptation gains from generation-based domain targeting are large for linguistically-nameable shifts and near zero for unnameable statistical shifts (sensor noise, optics), and per-shift gain correlates with human nameability ratings — paralleling the text-steering boundary.
- **why_important:** Unifies two adaptation channels (generation and steering) under one predictive principle, defining when each is worth attempting.
- **why_possibly_novel:** Cross-channel validation of the nameability boundary is new.
- **minimal_experiment:** Compare generation-based adaptation across nameable and unnameable shift suites; correlate gains with nameability ratings; compare boundaries with the text-steering route.
- **main_risk:** Some unnameable shifts may be image-promptable (exemplar conditioning); include image-conditioned generation as a third channel.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0243

### W2-B-0272 — Likelihood-stratified sampling from generators repairs the calibration damage of synthetic-data adaptation.

- **problem:** If synthetic-data miscalibration stems from generators oversampling high-likelihood modes, deliberately sampling across the generator's likelihood spectrum could fix it — a falsifiable mechanism-based remedy.
- **core_hypothesis:** Training mixtures stratified across generator likelihood levels (including low-likelihood tail samples) restore calibration to real-data levels at matched accuracy, while high-likelihood-only sampling reproduces the miscalibration — confirming the mode-coverage mechanism.
- **why_important:** A generation-side fix requiring no downstream changes, plus mechanistic confirmation of why synthetic data miscalibrates.
- **why_possibly_novel:** Likelihood-stratified generation for calibration repair is untested.
- **minimal_experiment:** Sample training sets at controlled likelihood strata; adapt and measure calibration/accuracy; compare against real-data and unstratified-synthetic baselines.
- **main_risk:** Likelihood estimates from diffusion models are approximate; use multiple estimators.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0254

### W2-B-0273 — Synthetic pretraining for medical VFMs implants impossible-anatomy tolerance measurable as false-plausibility acceptance.

- **problem:** Medical synthetic data can violate anatomical constraints in subtle ways; models adapted on it may learn to accept anatomically impossible configurations — a clinically-relevant corruption of priors.
- **core_hypothesis:** Models adapted on generated medical images rate anatomically impossible test images (controlled violations: organ misplacement, duplicated structures) as more probable and segment them more confidently than real-data-adapted controls.
- **why_important:** An acceptance test for anatomical-prior integrity should gate any synthetic-data use in medical model pipelines.
- **why_possibly_novel:** Impossible-anatomy probing of synthetic-data effects is new.
- **minimal_experiment:** Construct anatomical-violation batteries with radiologist validation; compare confidence and segmentation behavior of synthetic vs real-adapted models on violations.
- **main_risk:** Constructing convincing violations without other artifacts is delicate; use surgical image-editing pipelines.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0265

### W2-B-0274 — At matched budget, procedural copy-paste augmentation rivals diffusion-generated data for segmentation adaptation.

- **problem:** Diffusion generation is orders of magnitude costlier than copy-paste compositing, yet the two are never compared at matched total budget (compute plus curation) for dense adaptation (expectation UNVERIFIED — needs lit search).
- **core_hypothesis:** Budget-normalized comparison shows copy-paste matching or beating diffusion data on boundary metrics (real boundary statistics preserved) while diffusion wins on context-dependent classes — a structured, cost-aware verdict rather than a blanket ranking.
- **why_important:** Could redirect substantial community compute from generation to cheap compositing for a large class of tasks.
- **why_possibly_novel:** Cost-normalized procedural-vs-generative comparison for dense adaptation is missing.
- **minimal_experiment:** Build matched-budget pipelines (compute-inclusive accounting); adapt across several dense tasks; decompose results by class type and metric.
- **main_risk:** Budget accounting choices are contestable; report under multiple accounting schemes.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0270

### W2-B-0275 — Iterative generate-adapt loops collapse dense abilities faster than classification abilities — dense metrics as the canary for model collapse.

- **problem:** Model-collapse studies of recursive training focus on distributional and classification measures; dense tasks require exactly the tail structures (boundaries, small objects) that collapse erodes first, but this is unverified.
- **core_hypothesis:** In repeated generate-train cycles, boundary F1 and small-object recall degrade at measurably higher per-round rates than image-level accuracy, making dense metrics early-warning indicators for recursive-training degradation.
- **why_important:** Provides the ecosystem an actionable canary metric as synthetic data proliferates in training corpora.
- **why_possibly_novel:** Dense-resolved collapse-rate measurement is new.
- **minimal_experiment:** Run multi-round generate-adapt loops; track a metric battery per round; compare decay rates across metric families; validate the canary on independent loops.
- **main_risk:** Multi-round experiments are compute-heavy; use mid-scale models with replicated loops.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0262

### W2-B-0276 — PEFT is structurally protected against synthetic-data shortcuts: low-capacity adaptation cannot absorb generator fingerprints.

- **problem:** Whether adaptation method interacts with synthetic-data pathologies is unasked: full fine-tuning has capacity to exploit generator artifacts, while low-rank updates may be unable to — making PEFT accidentally safer on synthetic data.
- **core_hypothesis:** On fingerprint-bearing synthetic data, full fine-tuning exploits artifacts (large real-vs-filtered evaluation gap) while LoRA at low rank shows a much smaller gap, and the protection decays as rank grows — a capacity-shortcut law.
- **why_important:** Method-data interaction guidance: when training data is synthetic, capacity constraints double as artifact insurance.
- **why_possibly_novel:** The capacity-shortcut interaction for synthetic data is untested.
- **minimal_experiment:** Adapt with full FT and LoRA across ranks on fingerprinted synthetic data; measure real-vs-filtered evaluation gaps per method; fit the rank-protection curve.
- **main_risk:** Shortcuts may be low-rank themselves for some artifacts; the exceptions inform the law.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0257

### W2-B-0277 — Teacher-pseudo-labeled synthetic images amplify the teacher's boundary biases in students by a measurable factor per generation.

- **problem:** A standard pipeline generates images and labels them with a teacher VFM; the student inherits and possibly amplifies teacher biases, but the amplification factor has never been measured for dense labels.
- **core_hypothesis:** Student models trained on teacher-pseudo-labeled synthetic data exhibit the teacher's characteristic boundary displacement biases at amplified magnitude, and amplification compounds across student-teacher generations at a measurable rate.
- **why_important:** Quantifies error-heredity in the most common synthetic-labeling pipeline, setting limits on safe generational depth.
- **why_possibly_novel:** Bias-amplification factors for dense pseudo-labeling are unmeasured.
- **minimal_experiment:** Characterize teacher boundary biases against ground truth; train students on teacher-labeled synthetic data; measure student bias magnitude; iterate generations and fit the amplification rate.
- **main_risk:** Bias characterization requires high-quality ground truth; use densely-annotated subsets.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0275

### W2-B-0278 — Synthetic data helps only where real data undersamples feature-space directions — a spectral coverage criterion predicting the sign of its effect.

- **problem:** Synthetic augmentation sometimes helps and sometimes hurts, with no predictive account of the sign; a coverage-based criterion in feature space could unify the contradictory results.
- **core_hypothesis:** Synthetic additions improve performance when and only when they populate feature-space eigendirections undersampled by real data (measurable before training), and hurt when they oversample already-dense regions — predicting the effect sign from coverage geometry.
- **why_important:** A pre-training test deciding whether to generate at all would save budgets and reconcile the conflicting literature.
- **why_possibly_novel:** Spectral-coverage sign-prediction for synthetic data is a new framework.
- **minimal_experiment:** Compute real-data feature coverage spectra; characterize candidate synthetic sets by coverage complementarity; adapt and test whether the criterion predicts gain sign across many configurations.
- **main_risk:** Feature space choice (which model) may affect the criterion; test with multiple reference encoders.
- **cluster:** `synthetic_adaptation`
- **mutate_from:** W2-B-0259

---

## 10. Medical vision foundation models — scientific questions

Cluster key: `medical_vfm_science`

### W2-B-0279 — A modality-resolved sufficiency map: how much medically-relevant information natural-image VFM features actually contain per imaging modality.

- **problem:** The field debates whether medical imaging needs dedicated foundation models, but no systematic measurement exists of what fraction of medical-task information frozen natural-image features already carry, per modality.
- **core_hypothesis:** Frozen natural-VFM features are near-sufficient (small gap to dedicated models) for photographic-like modalities (dermoscopy, fundus, endoscopy) but structurally insufficient for reconstruction-based modalities (CT, MR), with the sufficiency gap predictable from modality image statistics.
- **why_important:** A sufficiency map would rationalize hundreds of "medical foundation model" projects, showing where they are needed and where they duplicate free capability.
- **why_possibly_novel:** Cross-modality sufficiency quantification with a statistics-based predictive account is missing (landscape claims UNVERIFIED — needs lit search).
- **minimal_experiment:** Probe frozen natural VFMs across modality-stratified task batteries; compare against modality-specific baselines at matched readout budgets; regress gaps on modality statistics.
- **main_risk:** Task selection per modality drives conclusions; use broad, preregistered batteries.
- **cluster:** `medical_vfm_science`

### W2-B-0280 — Pretraining augmentation invariances destroy microtexture diagnostic signals: an invariance audit against radiological needs.

- **problem:** Findings like microcalcifications and ground-glass opacities live in subtle textures that pretraining blur/color/crop invariances may have deliberately erased — a conflict never audited against clinical requirements.
- **core_hypothesis:** Frozen VFM features are measurably invariant to perturbations at the spatial-frequency and contrast scales of key findings, and per-finding invariance overlap predicts frozen-probe diagnostic failure across finding types.
- **why_important:** An invariance-vs-findings compatibility matrix would predict which clinical tasks can safely reuse natural VFMs.
- **why_possibly_novel:** Clinically-indexed invariance auditing is new.
- **minimal_experiment:** Characterize finding-specific perturbation signatures; measure feature invariance at those signatures; correlate with frozen-probe performance across finding-stratified benchmarks.
- **main_risk:** Finding signatures vary across devices; use multi-site data.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0201

### W2-B-0281 — VFM preprocessing discards absolute intensity semantics (Hounsfield units), and the information loss is quantifiable and consequential.

- **problem:** In CT, absolute intensity values carry physical meaning that standard VFM normalization erases; how much diagnostic information this destroys — versus how much survives in relative structure — is unmeasured.
- **core_hypothesis:** Frozen features retain relative-contrast information but lose absolute-HU decodability almost entirely, and tasks depending on absolute values (density quantification, calcium scoring) show frozen-probe failures predicted by the HU-information loss.
- **why_important:** Quantifies a fundamental interface mismatch between natural-image pipelines and physical imaging, guiding input-encoding standards.
- **why_possibly_novel:** Physical-unit information accounting through VFM pipelines is new.
- **minimal_experiment:** Probe HU decodability from frozen features under standard vs unit-preserving encodings; correlate loss with performance on value-dependent vs structure-dependent CT tasks.
- **main_risk:** Unit-preserving encodings change input distributions; control feature-quality side effects.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0207

### W2-B-0282 — Rotation robustness is a bug in medical imaging: VFM orientation invariance destroys laterality and orientation-critical signals.

- **problem:** Medical images have canonical orientations where flips change meaning (situs, laterality markers); natural-VFM robustness to orientation — a feature for photos — may actively harm medical tasks, unquantified.
- **core_hypothesis:** Frozen VFM features barely distinguish orientation-flipped medical images (high invariance), and this invariance predicts failure on laterality-sensitive tasks, while orientation-sensitive lightweight encodings restore the signal.
- **why_important:** Establishes that some pretrained "robustness" properties are anti-features clinically, requiring audit rather than celebration.
- **why_possibly_novel:** Orientation-invariance-as-harm quantification for medical reuse is new.
- **minimal_experiment:** Measure flip-discriminability of frozen features on radiographs; evaluate laterality-dependent task performance; test orientation-channel augmentation of inputs.
- **main_risk:** Some tasks legitimately want invariance; stratify tasks by orientation-relevance.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0280

### W2-B-0283 — Medical adaptations of CLIP-lineage models inherit typographic vulnerability: burned-in text on scans hijacks predictions.

- **problem:** Radiographs carry burned-in annotations (laterality markers, device text); CLIP-derived medical models may attend to and be steered by this text, an inherited pathology never audited in the medical setting.
- **core_hypothesis:** Adding or altering burned-in text shifts medical VLM predictions and segmentations at rates far exceeding natural-image typographic effects, because scan text correlates strongly with labels in training corpora (e.g., "PORTABLE" with disease severity).
- **why_important:** A concrete, auditable safety hazard in deployed medical AI with a clear mitigation path (text masking) whose cost should be measured.
- **why_possibly_novel:** Typographic auditing of medical VLM adaptations is new.
- **minimal_experiment:** Systematically manipulate burned-in text on test radiographs; measure prediction/segmentation shifts; compare models adapted with and without text-masked training data.
- **main_risk:** Text manipulation must avoid other artifacts; use clinical-grade editing protocols.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0137

### W2-B-0284 — Small-lesion miss rates are predictable from patch-grid geometry, giving a closed-form feasibility check for medical VFM reuse.

- **problem:** Lesions near or below patch size (small nodules, polyps) challenge ViT-based pipelines; whether misses follow deterministic grid-geometry laws — enabling feasibility prediction — is untested in the medical regime.
- **core_hypothesis:** Per-lesion detection probability is a sharp function of lesion-diameter-to-stride ratio with a modality-independent shape, allowing a priori computation of achievable sensitivity for any (model, resolution, lesion-size distribution) triple.
- **why_important:** A feasibility calculator would prevent clinically-dangerous deployments and misdirected fine-tuning attempts on structurally-impossible operating points.
- **why_possibly_novel:** Medical-calibrated aliasing laws with clinical sensitivity implications are new.
- **minimal_experiment:** Measure detection curves vs size/stride across CT nodule and polyp datasets and model scales; fit and validate the law; publish the calculator.
- **main_risk:** Contrast and location confound size effects; model them as covariates.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0018

### W2-B-0285 — Prevalence shift breaks adapted medical VFM calibration in a predictable direction, and prevalence-aware evaluation exposes it.

- **problem:** Models adapted on enriched datasets (balanced diseases) deploy under screening prevalence (mostly normal); the resulting calibration failure is systematic yet standard evaluation never simulates prevalence shift.
- **core_hypothesis:** Adapted models' calibration error under screening-prevalence resampling grows with the training-deployment prevalence gap in a predictable direction (overcalling), and prior-correction repairs part but not all of it — the unrepairable residue measuring feature-level entanglement with prevalence.
- **why_important:** Prevalence-robust evaluation should gate clinical deployment; quantifying the unrepairable component reveals a deeper adaptation failure.
- **why_possibly_novel:** Decomposing prevalence-shift damage into prior-correctable vs feature-entangled parts is new.
- **minimal_experiment:** Resample test sets across prevalence levels; measure calibration and post-correction residuals for adapted models; compare adaptation methods by residual size.
- **main_risk:** Resampling reduces effective test size at extreme prevalence; use large screening datasets.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0053

### W2-B-0286 — Frozen natural-VFM features are more site-invariant than dedicated medical foundation models — measured by site-of-origin decodability.

- **problem:** Cross-hospital generalization is the central deployment obstacle; whether medical-specific pretraining increases site-specific entanglement (by fitting site-correlated acquisition traits) relative to natural VFMs is an open, decisive question.
- **core_hypothesis:** Hospital-of-origin is more accurately decodable from medical-FM features than from frozen natural-VFM features on identical images, and site decodability inversely predicts cross-site task transfer — making site-invariance a pretraining-differentiating metric.
- **why_important:** If dedicated pretraining buys accuracy by absorbing site shortcuts, the field's investment calculus changes fundamentally.
- **why_possibly_novel:** Site-decodability as a comparative pretraining audit is new.
- **minimal_experiment:** Decode site labels from features of natural vs medical FMs on multi-site data; correlate site decodability with cross-site transfer across tasks.
- **main_risk:** Site correlates with population; disentangle using scanner-matched patient subsets.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0279

### W2-B-0287 — Hedged report language ("cannot rule out") acts as soft supervision that measurably shifts medical VLM decision thresholds.

- **problem:** Radiology reports systematically hedge; medical VLMs trained on report supervision inherit this pragmatics, but the effect on decision behavior (thresholds, confidence) has never been isolated.
- **core_hypothesis:** Findings frequently described with hedging language yield systematically lower model confidence at matched image evidence, and threshold audits show hedge-frequency predicting per-finding sensitivity — language pragmatics leaking into clinical operating points.
- **why_important:** Understanding this leakage is prerequisite to safe threshold setting in report-supervised systems.
- **why_possibly_novel:** Pragmatics-to-threshold transmission in medical VLMs is unstudied.
- **minimal_experiment:** Quantify hedge frequency per finding in report corpora; measure model confidence distributions at matched evidence levels; test causal effect via hedge-normalized retraining subsets.
- **main_risk:** Matched-evidence sets require careful construction; use longitudinal confirmed cases.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0026

### W2-B-0288 — Adapted segmentation models complete anatomy against image evidence: an evidence-vs-prior stress test for shape hallucination.

- **problem:** Segmentation models adapted to anatomy learn strong shape priors; whether they follow evidence or prior when the two conflict (post-surgical anatomy, congenital variants, devices) determines clinical safety yet is untested systematically.
- **core_hypothesis:** On anatomy-violating cases (resections, transplants, variants), adapted models hallucinate normal-shaped organ boundaries at high rates, and hallucination propensity grows with adaptation-set anatomical homogeneity — quantifying prior dominance.
- **why_important:** Shape hallucination on exactly the abnormal cases that matter clinically is a critical failure mode requiring a standard stress test.
- **why_possibly_novel:** Evidence-prior conflict batteries for medical segmentation are new.
- **minimal_experiment:** Curate post-surgical and variant-anatomy cases; measure completion-vs-evidence behavior of adapted models; correlate with training-set shape statistics.
- **main_risk:** Such cases are rare in public data; partner datasets or careful synthesis needed.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0273

### W2-B-0289 — Stain-color invariance from contrastive pretraining conflicts with stain-based cell identity in histopathology — a measurable utility conflict.

- **problem:** Histopathological cell typing depends on stain uptake colors, precisely the signal color-augmented pretraining suppresses; the conflict is plausible but its magnitude and task structure are unmeasured.
- **core_hypothesis:** Frozen contrastive features underperform on stain-color-dependent distinctions relative to morphology-dependent ones (within the same tissue), and the deficit correlates with pretraining color-augmentation strength across model variants.
- **why_important:** Determines whether pathology pipelines can reuse natural VFMs or need color-faithful pretraining, with per-task-type resolution.
- **why_possibly_novel:** Color-vs-morphology task decomposition of the pretraining conflict is new.
- **minimal_experiment:** Build stain-dependent vs morphology-dependent probe pairs; evaluate frozen VFMs with varied augmentation recipes; correlate deficits with recipe color-invariance.
- **main_risk:** Task pairs must match difficulty; use pathologist-validated batteries.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0019

### W2-B-0290 — Slice-wise 2D adaptation loses inter-slice continuity measurably, and the continuity violation rate predicts 3D clinical utility.

- **problem:** 2D VFMs are adapted slice-by-slice to volumetric modalities; the resulting inter-slice inconsistencies are visible anecdotally but never quantified as a predictor of volumetric task quality.
- **core_hypothesis:** Slice-wise adapted models produce inter-slice segmentation discontinuities at rates far above annotation variability, and a continuity-violation metric predicts downstream volumetric utility (volume estimation error, surgical-planning acceptability) better than per-slice Dice.
- **why_important:** Establishes continuity as a first-class evaluation metric, correcting the per-slice evaluation practice that hides 3D failure.
- **why_possibly_novel:** Continuity-violation metrics validated against volumetric utility are new.
- **minimal_experiment:** Quantify continuity violations of slice-wise pipelines; correlate with volume-error and clinician acceptability ratings; compare against 2.5D and 3D baselines at matched budgets.
- **main_risk:** Clinician ratings are expensive; use small expert panels with high-agreement protocols.
- **cluster:** `medical_vfm_science`

### W2-B-0291 — Cross-modality forgetting in medical adaptation follows a modality-distance law steeper than natural-domain forgetting predicts.

- **problem:** Adapting a VFM to one medical modality (CT) plausibly destroys transferability to others (MR, ultrasound); whether medical modality gaps produce categorically stronger forgetting than natural-domain analyses suggest is unmeasured.
- **core_hypothesis:** Post-adaptation transfer loss to other modalities grows with inter-modality feature distance following a steeper curve than equivalent natural-domain pairs, because medical modalities differ in physics, not just style — a regime where natural-domain forgetting intuitions fail.
- **why_important:** Multi-modality medical deployments need forgetting forecasts; importing natural-domain rules would systematically underestimate damage.
- **why_possibly_novel:** Medical modality-distance forgetting laws are unfitted.
- **minimal_experiment:** Adapt VFMs per modality; measure cross-modality retention matrices; fit distance-loss curves; compare against natural-domain pairs at matched feature distances.
- **main_risk:** Task difficulty varies across modalities; normalize with pre-adaptation baselines.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0138

### W2-B-0292 — Report-derived labels carry class-conditional noise correlated with disease severity, breaking noise-robust training assumptions.

- **problem:** Labels extracted from reports are noisy in structured ways — mild cases underreported, severe cases overdocumented — violating the class-independent noise assumptions of standard noise-robust methods, with consequences never characterized.
- **core_hypothesis:** Label-noise rates estimated against adjudicated ground truth vary systematically with severity within each class, and noise-robust training methods built for uniform noise underperform simple baselines under this structure — a documented mismatch between tool assumptions and medical reality.
- **why_important:** Redirects noisy-label research toward the severity-correlated structure that medical data actually exhibits.
- **why_possibly_novel:** Severity-conditional noise characterization with method-failure demonstration is new.
- **minimal_experiment:** Estimate severity-stratified noise rates on adjudicated datasets; benchmark noise-robust methods under real vs synthetic-uniform noise; document the assumption-violation gap.
- **main_risk:** Adjudicated ground truth is limited; concentrate on findings with consensus panels.
- **cluster:** `medical_vfm_science`

### W2-B-0293 — A matched-budget ablation of "medical foundation models": how much do they beat natural VFMs plus medical readouts, really?

- **problem:** Medical FM papers compare against weak baselines; the decisive comparison — natural VFM with equal medical-data readout/adaptation budget — is systematically absent, leaving the field's core investment question unanswered (landscape UNVERIFIED — needs lit search).
- **core_hypothesis:** Under matched medical-data and compute budgets for adaptation, a large fraction of claimed medical-FM advantages shrink to insignificance outside reconstruction-based modalities, localizing where medical pretraining genuinely pays.
- **why_important:** The result would recalibrate resource allocation across an entire subfield, whichever way it falls.
- **why_possibly_novel:** Budget-matched meta-evaluation across medical FMs is missing.
- **minimal_experiment:** Re-evaluate representative medical FMs against natural VFMs with budget-matched adaptation across modality-stratified tasks; report where gaps survive matching.
- **main_risk:** Faithful reproduction of medical FMs is laborious; select models with open weights and recipes.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0279

### W2-B-0294 — Pixel-wise uncertainty from adapted VFMs aligns with inter-radiologist disagreement only after adaptation-specific recalibration.

- **problem:** Uncertainty maps are proposed for clinical review triage, but whether model uncertainty coincides spatially with genuine expert disagreement — the clinically-meaningful uncertainty — is largely unvalidated.
- **core_hypothesis:** Raw uncertainty maps correlate weakly with inter-radiologist disagreement maps, but a monotone recalibration learned on small multi-annotator sets substantially improves alignment, with residual mismatches concentrated at systematic model blind spots.
- **why_important:** Validated disagreement-aligned uncertainty would make review-triage systems trustworthy; unvalidated maps are decoration.
- **why_possibly_novel:** Spatial validation of uncertainty against expert disagreement for adapted VFMs is scarce.
- **minimal_experiment:** Collect multi-annotator segmentations; compare model uncertainty maps against disagreement maps before/after recalibration; characterize residual mismatch structure.
- **main_risk:** Multi-annotator data is costly; leverage existing multi-reader studies.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0170

### W2-B-0295 — PEFT on rare diseases overfits hospital-specific presentation: a rarity-by-site interaction invisible in single-site validation.

- **problem:** PEFT is the default for rare-disease adaptation (little data); with few cases per site, adapters may encode site-specific presentation (device, protocol, demographics) as disease signal — undetectable without multi-site testing.
- **core_hypothesis:** LoRA-adapted rare-disease models show a larger single-site-to-multi-site performance drop than common-disease models at matched adaptation-set size, and the excess drop correlates with site-feature decodability from adapter-affected representations.
- **why_important:** Defines validation requirements (multi-site) specifically where current practice (single-site, PEFT, rare disease) is most dangerous.
- **why_possibly_novel:** The rarity-site interaction under PEFT is unmeasured.
- **minimal_experiment:** Adapt across rare and common findings at matched case counts from single sites; evaluate multi-site; decompose the excess drop; test site-balanced few-shot sampling.
- **main_risk:** Multi-site rare-disease data access is hard; use federated evaluation collaborations.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0118

### W2-B-0296 — Dice optimization diverges from clinical utility at organ-risk interfaces — quantified with dosimetric proxies.

- **problem:** Segmentation adaptation optimizes overlap metrics, but clinical consequences concentrate at specific interfaces (tumor-organ-at-risk boundaries in radiotherapy); the metric-utility divergence is asserted but rarely quantified with clinical proxies.
- **core_hypothesis:** Among models at equal Dice, dosimetric outcomes (simulated dose to organs-at-risk) vary widely, and a boundary-weighted interface metric predicts dosimetric quality far better — establishing measurable metric-utility divergence and a better target.
- **why_important:** Metric choice silently determines patient-relevant quality; a validated clinically-aligned metric would change adaptation objectives field-wide.
- **why_possibly_novel:** Dosimetric validation of segmentation metrics for adapted VFMs is new at systematic scale.
- **minimal_experiment:** Run treatment-planning simulations over models matched on Dice; correlate candidate metrics with dosimetric outcomes; identify the best-aligned metric family.
- **main_risk:** Simulation pipelines are complex; partner with medical-physics groups and use open planning systems.
- **cluster:** `medical_vfm_science`

### W2-B-0297 — Scanner software updates cause step-function drift that frozen readouts survive better than tuned medical models.

- **problem:** Device software updates change image processing overnight; the differential resilience of adaptation regimes to such discrete real-world drift events has not been measured despite being a routine deployment hazard.
- **core_hypothesis:** Across documented update events in longitudinal archives, tuned models show abrupt performance drops at update boundaries while frozen-feature systems degrade less, and the differential is predictable from how deeply tuning entangled features with processing-specific statistics.
- **why_important:** Regime choice for hospital deployment should weigh update resilience; this provides the first measured basis.
- **why_possibly_novel:** Update-event-resolved deployment analysis is new.
- **minimal_experiment:** Identify update timestamps in PACS archives; evaluate both regimes across event boundaries; correlate drop size with entanglement measures.
- **main_risk:** Update metadata access varies by institution; use archives with documented device histories.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0249

### W2-B-0298 — Report-template frequency predicts medical VLM hallucination content: models describe the most template-frequent absent findings.

- **problem:** Medical VLM hallucinations (reporting absent devices/findings) are documented, but their content structure — what gets hallucinated and why — lacks a predictive account.
- **core_hypothesis:** Hallucination rates per finding correlate strongly with that finding's frequency in report templates and boilerplate, showing hallucinations sample from report-language priors rather than visual confusion — predictable and hence filterable.
- **why_important:** Predictable hallucination content enables targeted post-hoc filters and identifies report-corpus curation as the upstream fix.
- **why_possibly_novel:** Template-prior attribution of medical hallucination content is new.
- **minimal_experiment:** Quantify finding frequencies in report corpora; measure per-finding hallucination rates of medical VLMs on finding-absent images; test the correlation and a prior-based filter.
- **main_risk:** Template statistics vary across institutions; use multi-corpus estimates.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0039

### W2-B-0299 — Convergence test: self-supervised pretraining on medical data recapitulates natural-VFM feature geometry, questioning modality-specific pretraining.

- **problem:** Whether medical SSL learns fundamentally different representations than natural-image SSL — or converges to similar geometry through different data — is a foundational unknown behind the medical-FM investment thesis.
- **core_hypothesis:** CKA and functional-probe comparisons show medical-SSL and natural-SSL features converge substantially at matched scale (especially mid-network), with divergence confined to early layers processing modality statistics — implying most medical pretraining value is replaceable by early-layer adaptation.
- **why_important:** Convergence would collapse the case for full medical pretraining into a case for shallow adaptation, redirecting massive compute.
- **why_possibly_novel:** Representational convergence analysis across pretraining domains at matched scale is new.
- **minimal_experiment:** Pretrain matched SSL models on medical vs natural corpora; compare layerwise geometry and probe batteries; test whether early-layer transplants close the gap.
- **main_risk:** Matched-scale medical corpora are smaller; equalize by subsampling natural data.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0286

### W2-B-0300 — Patient-level leakage in patch-based histopathology adaptation inflates benchmarks enough to reorder methods.

- **problem:** Patch-level splits letting the same patient appear in train and test are known bad practice yet still common; the quantitative inflation and its effect on method rankings in the VFM-adaptation era are undocumented.
- **core_hypothesis:** Re-evaluating published adaptation comparisons under strict patient-level splits reduces absolute scores substantially and changes method rankings in a meaningful fraction of comparisons — demonstrating that leakage doesn't just inflate, it misorders.
- **why_important:** A ranking-reordering demonstration would force split-hygiene standards across medical adaptation research.
- **why_possibly_novel:** Leakage-induced rank-distortion measurement is new for this literature.
- **minimal_experiment:** Reproduce representative benchmarks under patch-level vs patient-level splits; quantify score inflation and rank changes; release corrected splits.
- **main_risk:** Reproduction effort is high; select benchmarks with available code and data.
- **cluster:** `medical_vfm_science`

### W2-B-0301 — Federated LoRA aggregation fails under cross-site subspace misalignment, and alignment metrics predict when.

- **problem:** Hospitals cannot share data but could share LoRA updates; naive adapter averaging assumes sites learn compatible subspaces — an assumption whose validity and failure conditions are unmeasured.
- **core_hypothesis:** Cross-site LoRA subspace principal angles predict federated-averaging degradation: below an alignment threshold, averaging matches centralized training; above it, averaging underperforms the best single site — motivating alignment-aware aggregation.
- **why_important:** Defines when the most practical privacy-preserving adaptation scheme for medical VFMs works, with a measurable precondition.
- **why_possibly_novel:** Subspace-alignment theory for federated PEFT is untested in the medical setting.
- **minimal_experiment:** Simulate federation across real multi-site datasets; measure adapter subspace angles and averaging outcomes; validate the alignment threshold and test alignment-aware aggregation.
- **main_risk:** Simulated federation understates system heterogeneity; include real cross-institution splits.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0124

### W2-B-0302 — Counterfactual lesion editing provides causal evidence attribution for adapted medical models, beyond saliency maps.

- **problem:** Saliency methods for medical model auditing are correlational and unreliable; counterfactual image editing (adding/removing findings with controlled realism) enables causal tests of what evidence adapted models actually use — a methodology needing validation.
- **core_hypothesis:** Counterfactual sensitivity (prediction change under finding removal) dissociates sharply from saliency overlap with findings, identifying models that attend to findings but rely on correlated context — and the dissociation predicts external-validation failure.
- **why_important:** A causal audit standard would materially improve pre-deployment screening of medical adaptations.
- **why_possibly_novel:** Validated counterfactual auditing linked to external-validity prediction is new.
- **minimal_experiment:** Build finding-editing pipelines with radiologist realism validation; measure counterfactual sensitivity vs saliency alignment across models; correlate audit results with cross-site performance.
- **main_risk:** Editing artifacts could cue models; include artifact-only controls.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0288

### W2-B-0303 — Adaptation optimizes the ROC middle while clinical screening lives in the tails: fine-tuning degrades extreme-specificity operating points.

- **problem:** Fine-tuning improves average discrimination (AUC), but screening deployments operate at extreme specificity or sensitivity; whether adaptation helps or harms the ROC tails specifically is unexamined.
- **core_hypothesis:** Compared to frozen-probe baselines at matched AUC, fine-tuned models show degraded partial AUC in extreme-specificity regions, because adaptation reshapes score distributions around the decision bulk at the tails' expense.
- **why_important:** Screening programs choosing models by AUC would systematically pick tail-degraded models; tail-resolved evaluation must become standard.
- **why_possibly_novel:** Tail-resolved ROC analysis of adaptation effects is new.
- **minimal_experiment:** Compare frozen vs tuned models on partial AUCs across operating regions at matched global AUC; analyze score-distribution reshaping; test tail-weighted adaptation objectives.
- **main_risk:** Tail estimates need large negative cohorts; use screening-scale datasets.
- **cluster:** `medical_vfm_science`
- **mutate_from:** W2-B-0285

---

## 11. Alignment between language supervision and dense visual geometry

Cluster key: `language_geometry_alignment`

### W2-B-0304 — Language supervision quantizes continuous shape space: CLIP-lineage features jump along smooth object morphs where SSL features glide.

- **problem:** Whether linguistic category structure imposes discreteness on visual feature geometry — categorical perception in machines — is a foundational question about language-supervised vision never tested with controlled morphs.
- **core_hypothesis:** Feature trajectories along smooth shape morphs (chair-to-stool, cup-to-bowl) show measurable discontinuities at category boundaries in language-aligned models but not SSL models, and discontinuity locations align with human naming boundaries.
- **why_important:** Machine categorical perception would explain dense-regression weaknesses of language-aligned features and connect VLM representation to psychophysics.
- **why_possibly_novel:** Morph-trajectory discontinuity analysis across pretraining objectives is new.
- **minimal_experiment:** Generate controlled 3D-render and image-space morph sequences; trace feature trajectories per model; quantify discontinuity via curvature statistics; compare against human naming data.
- **main_risk:** Morph artifacts may cause spurious jumps; validate with multiple morphing methods.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0209

### W2-B-0305 — English-centric supervision imprints English spatial-category structure, measurable by comparing multilingual CLIP variants on spatial probes.

- **problem:** Languages carve spatial relations differently (e.g., containment vs support distinctions); whether the supervising language's spatial ontology shapes visual relational features is a testable transmission question nobody has run.
- **core_hypothesis:** Models supervised predominantly with English captions encode spatial contrasts English lexicalizes ("on" vs "in") more separably than contrasts it merges but other languages split, and multilingual-supervised variants shift measurably toward their language mixture's structure.
- **why_important:** Demonstrating linguistic-relativity effects in vision models would reframe caption-language composition as a representational design choice.
- **why_possibly_novel:** Cross-linguistic spatial-category transmission into visual features is untested.
- **minimal_experiment:** Build spatial-relation probe batteries contrasting cross-linguistic category structures; compare English-heavy vs multilingual CLIP variants; quantify alignment with each language's ontology.
- **main_risk:** Data composition confounds (image sources differ per language); use caption-translated controls.
- **cluster:** `language_geometry_alignment`

### W2-B-0306 — Boundary vocabulary is rare in captions, and this under-supervision statistically explains language-aligned models' boundary weakness.

- **problem:** The hypothesis "language doesn't talk about boundaries, so language-supervised features don't learn them" is intuitively cited but never quantified against caption corpora and model behavior jointly.
- **core_hypothesis:** Caption-corpus frequency of boundary/edge/contour vocabulary and boundary-descriptive constructions is very low relative to object/attribute vocabulary, and across models, the caption-corpus boundary-language share correlates with frozen boundary-metric performance.
- **why_important:** A supervision-statistics account of a central dense failure would identify caption enrichment (not architecture) as the fix path.
- **why_possibly_novel:** Joint corpus-statistics-to-dense-metric analysis is new.
- **minimal_experiment:** Quantify boundary-language statistics across open caption corpora (LAION subsets); evaluate models trained on those corpora; test the correlation with per-model boundary metrics.
- **main_risk:** Correlational at model level; strengthen with controlled caption-augmentation retraining at small scale.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0026

### W2-B-0307 — Adding language alignment to pretraining degrades metric depth structure relative to purely visual objectives at matched data.

- **problem:** Language supervision helps semantics, but depth is a continuous geometric property language rarely quantifies; whether text alignment actively worsens depth linearity (not just fails to help) is a sharp, decidable question.
- **core_hypothesis:** At matched architecture and data scale, adding a contrastive text head measurably reduces linear decodability of metric depth from frozen features compared to vision-only training — language as negative supervision for geometry.
- **why_important:** A demonstrated negative effect would force explicit tradeoff decisions in pretraining design rather than assuming language is free.
- **why_possibly_novel:** Controlled language-ablation tests of geometric decodability are missing.
- **minimal_experiment:** Train matched models with/without text alignment on identical images (captioned subsets); probe metric and ordinal depth; verify with public family comparisons (SigLIP vs DINO lineage) as convergent evidence.
- **main_risk:** Caption availability constrains matched-data design; use datasets with complete caption coverage.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0206

### W2-B-0308 — VLM numerosity representation plateaus where linguistic number words thin out — the "many" ceiling.

- **problem:** Language marks exact small numbers heavily (one, two, three) and approximates beyond; if numerosity representation in language-supervised models mirrors linguistic number statistics rather than visual capacity, counting failures have a supervision-statistics explanation.
- **core_hypothesis:** Decodable numerosity precision from language-aligned features degrades sharply beyond three to four items, matching caption number-word frequency decay, while SSL features degrade smoothly — a signature of language-imposed structure.
- **why_important:** Locates VLM counting limits in supervision statistics, predicting that caption enrichment (not scale) fixes them.
- **why_possibly_novel:** Number-word statistics as a predictor of numerosity representation is untested.
- **minimal_experiment:** Probe numerosity decodability across set sizes for language-aligned vs SSL models; compare degradation profiles against number-word frequency curves from caption corpora.
- **main_risk:** Visual crowding confounds set size; control density and arrangement.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0040

### W2-B-0309 — Nameable shapes are better represented than unnameable ones in language-aligned models — nameability as a geometric-probe predictor.

- **problem:** Whether language supervision selectively strengthens representation of linguistically-codable geometry (circle, square, spiral) versus equally-simple but unnamed shapes would reveal the granularity of language's imprint on visual geometry.
- **core_hypothesis:** Probe accuracy for shape properties correlates with shape nameability (human naming agreement) in language-aligned models substantially more than in SSL models, at matched visual complexity.
- **why_important:** Establishes the vocabulary of pretraining captions as a boundary on geometric competence, with implications for technical domains using unnamed shapes.
- **why_possibly_novel:** Nameability-stratified geometric probing is new.
- **minimal_experiment:** Construct shape batteries spanning nameability at matched complexity; probe shape-property decoding across model families; test the nameability-correlation difference.
- **main_risk:** Nameability and familiarity covary; include familiarity-controlled subsets.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0026

### W2-B-0310 — Spatial prepositions form a consistent low-dimensional subspace in VLM joint space — but it encodes textual convention, not visual geometry.

- **problem:** Whether relational language ("above", "left of") maps to visually-grounded directions in joint embedding space, or merely to text-statistical structure, decides if VLMs can do relational dense reasoning through their embeddings.
- **core_hypothesis:** Preposition embeddings form a reliable subspace, but its geometry mismatches visual space: arithmetic with preposition vectors fails to move image-region embeddings in corresponding visual directions, revealing text-side structure without visual grounding.
- **why_important:** Diagnoses why embedding-arithmetic approaches to spatial reasoning fail and what "grounding" would measurably require.
- **why_possibly_novel:** Visual-consistency testing of linguistic spatial subspaces is new.
- **minimal_experiment:** Extract preposition subspaces; test whether adding relation vectors to region embeddings retrieves correctly-related regions on controlled scenes; quantify the text-visual geometry mismatch.
- **main_risk:** Region-embedding extraction choices affect results; use multiple region-encoding schemes.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0305

### W2-B-0311 — Canonical-view language ("front of a car") over-canonicalizes pose representation: language-aligned models concentrate errors at non-canonical viewpoints.

- **problem:** Captions describe objects from and in canonical viewpoints; whether this biases viewpoint representation — degrading pose-related dense tasks specifically at rare views — is unquantified.
- **core_hypothesis:** Pose-estimation and viewpoint-decoding error as a function of viewpoint is more sharply concentrated at non-canonical views for language-aligned models than SSL models, and the error profile matches caption viewpoint statistics.
- **why_important:** View-dependent reliability matters for robotics and AR; a supervision-statistics account predicts and locates the failures.
- **why_possibly_novel:** Viewpoint-resolved comparison across supervision types is new.
- **minimal_experiment:** Evaluate viewpoint decoding on controlled multi-view datasets across models; compare error-vs-viewpoint profiles against caption-derived viewpoint frequency estimates.
- **main_risk:** Estimating caption viewpoint statistics is indirect; use VLM-assisted annotation with human verification.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0304

### W2-B-0312 — Compositional caption syntax does not produce compositional feature binding: part-swap composites expose unbound part-whole features.

- **problem:** Captions are compositional ("the handle of the red cup"), but whether this induces compositional binding in visual features — parts bound to correct wholes — is assumed rather than tested at the dense level.
- **core_hypothesis:** On chimeric images (parts swapped between objects), language-aligned patch features represent part identity and whole identity separably but fail to represent the binding (which part belongs to which whole) above SSL baselines, showing caption compositionality does not transfer to feature binding.
- **why_important:** Binding failure predicts systematic dense-grounding errors on multi-object scenes and bounds what caption-scale alone can achieve.
- **why_possibly_novel:** Chimera-based binding tests for dense VLM features are new.
- **minimal_experiment:** Construct part-swap composites; probe part, whole, and binding decodability from patch features across model families; compare binding-specific performance.
- **main_risk:** Chimera unnaturalness may depress all models; include naturalistic occlusion-based binding tests.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0043

### W2-B-0313 — Caption diversity per category predicts within-category feature variance: low-diversity captions collapse visual variability.

- **problem:** If all cups are captioned "a cup", language supervision rewards collapsing cup-to-cup visual differences; the relationship between caption diversity and preserved within-category structure is measurable but unmeasured.
- **core_hypothesis:** Within-category feature variance (and part/pose decodability) correlates with per-category caption diversity across hundreds of categories, and categories with template-like captions show variance collapse harming fine-grained dense tasks.
- **why_important:** Identifies caption-diversity curation as a lever controlling how much visual richness survives language supervision.
- **why_possibly_novel:** Caption-diversity-to-feature-variance mapping is new.
- **minimal_experiment:** Quantify caption diversity per category in open corpora; measure within-category feature variance and fine-grained probe performance; test the correlation with corpus-controlled retraining.
- **main_risk:** Category frequency confounds diversity; include frequency-matched analyses.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0216

### W2-B-0314 — Language rarely names negative space, and language-aligned models are selectively blind to gaps, holes, and apertures.

- **problem:** Dense tasks must represent empty regions (gaps to walk through, holes in materials), which captions rarely mention; whether language supervision creates a measurable negative-space deficit is untested.
- **core_hypothesis:** Frozen language-aligned features support hole/gap/aperture segmentation and topology decoding (does this region have a hole?) substantially worse than matched SSL features, while performing equally on object tasks of matched difficulty.
- **why_important:** Negative-space competence matters for navigation and manipulation; a supervision-based deficit account identifies what data would fix it.
- **why_possibly_novel:** Negative-space representation comparison across supervision types is new.
- **minimal_experiment:** Build gap/hole/aperture batteries with matched-object controls; probe frozen features across model families; test the selective-deficit prediction.
- **main_risk:** Difficulty matching between negative-space and object tasks is delicate; use human-performance-normalized items.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0068

### W2-B-0315 — "X on Y" caption statistics teach co-occurrence, not support relations: physical support is undecodable despite relational language at scale.

- **problem:** Relational captions could in principle supervise physical relations (support, attachment); whether models learn the relation or merely the co-occurrence of the paired objects is a decidable representation question.
- **core_hypothesis:** Probes for physical support (will it fall if the supporter moves?) fail on language-aligned features once object-identity co-occurrence is controlled, showing relational captions supervise object pairing rather than relational geometry.
- **why_important:** Bounds what caption scale can teach about physics and clarifies the supervision gap embodied AI must fill.
- **why_possibly_novel:** Co-occurrence-controlled relational probing is new.
- **minimal_experiment:** Construct support-relation batteries where identical object pairs appear in supporting and non-supporting configurations; probe frozen features; compare against SSL and video-pretrained models.
- **main_risk:** Configuration differences carry low-level cues; balance viewpoint and contact statistics.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0310

### W2-B-0316 — Language-aligned attention tracks nameable-part saliency, dissociating from human visual saliency on unnameable-but-salient content.

- **problem:** Where language-supervised models "look" may follow linguistic describability rather than visual conspicuity; the dissociation between the two saliency types has never been mapped for VFMs.
- **core_hypothesis:** Attention/feature-energy maps of language-aligned models correlate with describability maps (how likely humans are to mention a region) more than with classic visual-saliency maps, while SSL models show the reverse — two saliency regimes.
- **why_important:** Predicts systematic blind spots of language-aligned dense systems on visually-striking-but-unnamed content (stains, damage, anomalies).
- **why_possibly_novel:** Describability-vs-saliency dissociation testing is new.
- **minimal_experiment:** Collect describability and saliency maps for shared images (existing eye-tracking plus captioning datasets); correlate with model attention maps across families.
- **main_risk:** Attention maps are imperfect "looking" proxies; triangulate with feature-energy and probing.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0306

### W2-B-0317 — Image-level caption supervision is multiple-instance learning, and MIL identifiability theory predicts which visual concepts it can never localize.

- **problem:** Captions label bags (images), not instances (regions); MIL theory specifies identifiability conditions (concept co-occurrence structure) under which bag supervision can or cannot localize concepts — never applied to predict CLIP-style dense failures.
- **core_hypothesis:** Concepts violating MIL identifiability conditions (always co-occurring with correlated context, never appearing isolated) show near-zero dense emergence in language-aligned models regardless of scale, and identifiability scores computed from corpus statistics predict per-concept dense quality.
- **why_important:** A theory-driven predictor of dense emergence would replace empirical trial and error and set principled expectations for caption-supervised localization.
- **why_possibly_novel:** MIL-identifiability analysis of caption supervision is new.
- **minimal_experiment:** Compute co-occurrence-based identifiability scores per concept from corpus statistics; measure per-concept dense emergence in open-vocab systems; test the theory's predictions including scale-invariance of violations.
- **main_risk:** Corpus statistics approximate the true training distribution; use models with released data.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0037

### W2-B-0318 — Geometric superlatives ("leftmost", "largest") require readout operations contrastive alignment never trains, dissociating representation from usability.

- **problem:** Answering "the leftmost cup" needs an argmax over grounded candidates — an operation, not a feature; whether failures on such queries reflect missing information or missing operations is unresolved.
- **core_hypothesis:** Position and size information for all candidates is linearly decodable from VLM features (information present), yet text-driven selection of superlative targets fails far below the decodability ceiling (operation absent) — a representation-usability dissociation.
- **why_important:** Locates a class of VLM failures at the interface between representation and computation, predicting that scaling representations won't fix them.
- **why_possibly_novel:** Information-vs-operation dissociation analysis for relational queries is new.
- **minimal_experiment:** Jointly measure candidate-attribute decodability and superlative-query accuracy across models; quantify the dissociation gap; test whether lightweight symbolic readouts close it.
- **main_risk:** Decodability probes may overestimate accessible information; use causal patching as convergent evidence.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0310

### W2-B-0319 — Property-word frequency predicts visual-property probe accuracy, and residuals from the curve reveal what vision learns without language.

- **problem:** Which visual properties language-supervised models represent well is usually explained post hoc; a quantitative frequency-to-representation curve would make the language imprint predictive and expose language-independent learning.
- **core_hypothesis:** Across dozens of visual properties (colors, materials, textures, shapes, states), probe accuracy in language-aligned models follows log-frequency of property vocabulary, and systematic positive residuals (properties learned better than frequency predicts) identify visually-learnable-without-language structure.
- **why_important:** The curve and its residuals decompose VLM competence into language-driven and vision-driven components — a foundational measurement.
- **why_possibly_novel:** Property-level frequency-representation curves with residual analysis are new.
- **minimal_experiment:** Assemble property probe batteries; measure probe accuracy across models; fit frequency curves; characterize residual structure and its consistency across model families.
- **main_risk:** Property probe difficulty varies; normalize with SSL-model baselines.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0306

### W2-B-0320 — Descriptive versus narrative caption styles supervise geometry differently: alt-text-heavy training preserves more spatial structure.

- **problem:** Caption corpora mix descriptive alt-text ("red car parked left of hydrant") and narrative social text ("best day ever!"); the geometric supervision value of caption style — as opposed to volume — is uncharacterized.
- **core_hypothesis:** At matched scale, models trained on descriptive-style captions retain substantially more decodable spatial structure (relations, layout, counts) than narrative-style training, making caption-style composition a controllable geometry-supervision dial.
- **why_important:** Data curation guidance orthogonal to the scale race: style filtering as a cheap lever on dense competence.
- **why_possibly_novel:** Style-controlled caption-supervision experiments are new.
- **minimal_experiment:** Partition open corpora by caption style (classifier plus human validation); train matched models per style mixture; probe spatial-structure batteries; fit the style-to-geometry dose response.
- **main_risk:** Style correlates with image source; control image distributions across partitions.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0313

### W2-B-0321 — Texture vocabulary poverty predicts texture-boundary blindness: language-aligned models underperform exactly where language lacks words.

- **problem:** Texture distinctions often lack lexical labels (two similar fabrics, wood grains); if language-aligned models segment texture-defined boundaries poorly relative to SSL models specifically for unlexicalized contrasts, supervision statistics explain another dense deficit.
- **core_hypothesis:** Segmentation of boundaries defined by lexicalized texture contrasts (striped vs dotted) is comparable across model families, but unlexicalized texture contrasts show a selective language-aligned deficit proportional to the contrast's lexical codability.
- **why_important:** Predicts domain failures (material inspection, geology, dermatology) where critical distinctions are visually clear but linguistically unnamed.
- **why_possibly_novel:** Lexical-codability-stratified texture-boundary evaluation is new.
- **minimal_experiment:** Build texture-boundary batteries stratified by codability (naming-agreement norms); evaluate frozen segmentation across families; test the codability-deficit correlation.
- **main_risk:** Codability norms require collection; use existing texture-naming datasets plus small studies.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0309

### W2-B-0322 — Occlusion language in captions ("behind", "hidden by") provides weak depth-order supervision measurable as above-chance order decoding.

- **problem:** Whether the small fraction of captions expressing occlusion/depth relations suffices to teach depth ordering — and whether that knowledge is caption-driven rather than photometrically learned — is a tractable attribution question.
- **core_hypothesis:** Language-aligned models decode named-object depth order above SSL baselines specifically for object pairs frequently co-mentioned with occlusion language in corpora, and the advantage tracks caption-statistics stratification — isolating the linguistic contribution to depth knowledge.
- **why_important:** Demonstrates (or refutes) that sparse relational language measurably shapes geometric knowledge, informing caption-enrichment strategies.
- **why_possibly_novel:** Caption-stratified attribution of depth-order knowledge is new.
- **minimal_experiment:** Stratify object pairs by occlusion-language frequency; measure depth-order decoding per stratum across model families; test the interaction.
- **main_risk:** Photometric occlusion cues are strong; the SSL baseline subtraction handles shared cues.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0315

### W2-B-0323 — Captions mention salient objects, so unmentioned-but-visible content is systematically under-represented — a "mentioned bias" measurable with counterfactual captions.

- **problem:** Caption supervision weights image content by mention probability; the representational penalty for chronically-unmentioned content (backgrounds, supports, fasteners, shadows) has not been isolated from visual difficulty.
- **core_hypothesis:** At matched visual properties, chronically-unmentioned object categories show weaker frozen-feature decodability in language-aligned models than SSL models, and the deficit correlates with mention probability estimated from corpora — a direct supervision-weighting imprint.
- **why_important:** Quantifies the systematic blind spots language supervision installs, predicting failure domains (industrial parts, infrastructure) dominated by unmentioned content.
- **why_possibly_novel:** Mention-probability-stratified representation auditing is new.
- **minimal_experiment:** Estimate mention probabilities per category; measure decodability gaps between model families across mention strata; verify with caption-intervention retraining at small scale.
- **main_risk:** Unmentioned categories may be visually harder; SSL-baseline normalization controls this.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0316

### W2-B-0324 — Region-text alignment losses fragment same-class instances across synonym clusters — synonymy splitting in dense feature space.

- **problem:** Dense alignment objectives pull region features toward text embeddings; because synonyms occupy different text-space locations, same-class regions captioned differently may be pulled apart — an alignment pathology never audited.
- **core_hypothesis:** In densely-aligned models, within-class region-feature variance is structured by the caption synonym used at training (measurable clustering by synonym), degrading class-consistency of dense predictions relative to models aligned at image level only.
- **why_important:** Identifies a specific harm of the increasingly-popular dense alignment objectives, with a measurable signature and clear fix direction (synonym-collapsed text targets).
- **why_possibly_novel:** Synonymy-fragmentation auditing of dense alignment is new.
- **minimal_experiment:** Probe region-feature clustering structure against training-caption synonyms; compare dense-aligned vs image-aligned models; test synonym-marginalized evaluation and training.
- **main_risk:** Requires models with known training captions; use open dense-alignment reproductions.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0042

### W2-B-0325 — A text-only counterfactual baseline decomposes VLM spatial errors into inherited-linguistic versus visual-processing components.

- **problem:** When a VLM misjudges spatial relations, the error may originate in the language model's geometric priors (text-only behavior) rather than vision — but evaluations never subtract the text-only baseline.
- **core_hypothesis:** A substantial fraction of VLM spatial-relation errors is predictable from the underlying LLM's text-only spatial-prior errors on matched questions, and the inherited fraction grows with LLM confidence — vision often loses to language priors it should override.
- **why_important:** Correct error attribution changes the fix: better visual grounding versus prior-suppression during decoding.
- **why_possibly_novel:** Text-only counterfactual decomposition of multimodal spatial errors is new.
- **minimal_experiment:** Construct matched visual and text-only spatial questions; measure error overlap and prior-strength interactions across VLM families; validate with decoding-time prior-suppression probes.
- **main_risk:** Matching text-only questions to images is delicate; use scene-graph-derived question generation.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0041

### W2-B-0326 — Basic-level naming bias in captions sets the default granularity of dense predictions — models segment at the linguistic basic level.

- **problem:** Captions overwhelmingly use basic-level terms ("dog", not "animal" or "beagle"); whether this fixes the default part-whole granularity of language-aligned dense outputs is a specific, testable transmission hypothesis.
- **core_hypothesis:** Unprompted or ambiguously-prompted dense predictions align with basic-level category boundaries at rates far exceeding chance and exceeding SSL-derived segmenters, and granularity follows each category's naming distribution rather than visual structure.
- **why_important:** Explains granularity behavior of promptable/open-vocab systems from supervision statistics and predicts where non-basic granularities (medical, industrial) will fail.
- **why_possibly_novel:** Basic-level-bias measurement in dense outputs is new.
- **minimal_experiment:** Compare unprompted segmentation granularity against basic-level norms across categories; correlate per-category granularity with caption naming distributions; contrast with SSL-based segmentation granularity.
- **main_risk:** Granularity ground truth needs hierarchical annotation; use datasets with part-whole hierarchies.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0179

### W2-B-0327 — Geometry re-emerges during dense fine-tuning slower in language-aligned models: the categorical prior actively resists geometric re-learning.

- **problem:** When adapting VFMs to geometric dense tasks (depth, normals), the pretrained representation may scaffold or fight the adaptation; the direction and magnitude of this interaction across supervision types is unknown.
- **core_hypothesis:** At matched adaptation budgets, language-aligned models re-acquire geometric competence (depth accuracy per training step) slower than SSL models despite equal final in-distribution performance, and the lag correlates with the categorical-quantization strength of their features.
- **why_important:** Adaptation-speed differences determine method choice under budget constraints and reveal whether language priors are inert or actively resistive.
- **why_possibly_novel:** Adaptation-dynamics comparison across supervision types for geometric tasks is new.
- **minimal_experiment:** Fine-tune matched models on depth/normals; compare learning curves and sample efficiency; correlate lag with pre-measured quantization indices; test whether the lag persists under PEFT.
- **main_risk:** Learning-rate optimality differs per model; sweep schedules to compare best-case dynamics.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0304

### W2-B-0328 — Supervision density maps — words per image region — predict per-region feature quality inside single images.

- **problem:** Language supervision is spatially non-uniform within each image (captions describe some regions, ignore others); whether this within-image supervision gradient imprints as a within-image quality gradient has never been measured.
- **core_hypothesis:** Estimated per-region caption-coverage (via grounding of training-style captions) predicts per-region frozen-feature quality within images — well-described regions carry better features — and the gradient is absent in SSL models trained on the same images.
- **why_important:** A within-image supervision account unifies many observations (thing-stuff gaps, mentioned bias) at finer granularity and motivates region-balanced caption generation.
- **why_possibly_novel:** Within-image supervision-gradient analysis is new.
- **minimal_experiment:** Ground caption distributions to regions on training-like data; measure per-region probe quality across model families; test the coverage-quality correlation within and across images.
- **main_risk:** Grounding the captions uses models with their own biases; use multiple grounding methods and human-annotated subsets.
- **cluster:** `language_geometry_alignment`
- **mutate_from:** W2-B-0323

---

## 12. Agents/tools around vision models with testable vision hypotheses

Cluster key: `agentic_vision_hypotheses`

### W2-B-0329 — Agent confidence is uncorrelated with the quality of the vision-tool outputs it consumes — a broken uncertainty chain, measurable end to end.

- **problem:** Tool-augmented VLM agents call segmenters/detectors and then express confidence in conclusions; whether that confidence reflects the tools' actual output quality is an unexamined link in the reliability chain.
- **core_hypothesis:** Across agent frameworks, final-answer confidence correlates near zero with measured tool-output quality (mask IoU, detection precision) on the same episodes, because language-generated confidence is produced independently of tool evidence quality.
- **why_important:** If agents cannot propagate tool uncertainty, every agentic-vision deployment inherits unquantified risk — a measurable, fixable defect.
- **why_possibly_novel:** End-to-end uncertainty-chain auditing for vision-tool agents is new.
- **minimal_experiment:** Instrument agent episodes with ground-truth-scored tool outputs; regress expressed confidence on tool quality; localize where the chain breaks (tool report format, aggregation, verbalization).
- **main_risk:** Confidence extraction from generated text is noisy; use standardized elicitation formats.
- **cluster:** `agentic_vision_hypotheses`

### W2-B-0330 — Crop-and-zoom agent loops help only when the encoder's measured acuity is the bottleneck — a predictable gain condition.

- **problem:** Iterative visual re-examination (agent crops regions and re-encodes) sometimes helps dramatically and sometimes wastes compute; no predictive account exists of when zooming pays.
- **core_hypothesis:** Zoom-loop gains per instance are predicted by whether the target's angular size falls below the encoder's acuity threshold (measured independently), with near-zero gains above threshold — making zoom a targetable, not blanket, strategy.
- **why_important:** Converts an expensive heuristic into a measurement-gated policy, cutting agent inference costs while preserving accuracy.
- **why_possibly_novel:** Acuity-gated prediction of re-examination value is new.
- **minimal_experiment:** Measure encoder acuity; run zoom-loop agents on size-stratified tasks; test the threshold prediction; deploy and evaluate an acuity-gated zoom policy.
- **main_risk:** Gains may also depend on clutter, not just size; model both factors.
- **cluster:** `agentic_vision_hypotheses`
- **mutate_from:** W2-B-0023

### W2-B-0331 — Self-verification of masks by the same VLM is inflated by correlated errors: quantifying the independence deficit of self-checking agents.

- **problem:** Agent pipelines ask the model to verify its own segmentation/grounding outputs; if verifier and producer share failure modes, self-verification overestimates quality in exactly the failure cases.
- **core_hypothesis:** Self-verification acceptance rates on incorrect outputs substantially exceed cross-model verification rates on the same outputs, and the excess (correlated-error inflation) concentrates on prior-driven errors, quantifying how much independence verification actually needs.
- **why_important:** Measured independence requirements would set design rules for verification in agentic vision systems.
- **why_possibly_novel:** Correlated-error accounting for visual self-verification is new.
- **minimal_experiment:** Generate outputs with known errors; compare self vs cross-model vs human verification acceptance; decompose inflation by error type (prior-driven vs perceptual).
- **main_risk:** Cross-model verifiers have own biases; use diverse verifier families and human anchors.
- **cluster:** `agentic_vision_hypotheses`
- **mutate_from:** W2-B-0067

### W2-B-0332 — Visual chain-of-thought is often post-hoc theater: intermediate boxes change answers even when wrong, and answers persist when boxes are corrected.

- **problem:** Agents that draw intermediate boxes/marks before answering appear to reason visually; whether the intermediate artifacts causally support the final answer or decorate a predetermined one is unestablished.
- **core_hypothesis:** Interventions on intermediate visual artifacts (replacing wrong boxes with correct ones, or vice versa) change final answers in only a minority of episodes, demonstrating that a substantial fraction of visual chain-of-thought is post-hoc rationalization.
- **why_important:** Distinguishes real visual reasoning from theater, determining whether intermediate-artifact training actually improves perception or just style.
- **why_possibly_novel:** Causal intervention testing of visual chain-of-thought faithfulness is new.
- **minimal_experiment:** Run agents with instrumented intermediate artifacts; perform artifact swaps/corrections mid-episode; measure answer-change rates conditioned on artifact correctness.
- **main_risk:** Intervention breaks episode naturalness; use API-level artifact injection to stay in-distribution.
- **cluster:** `agentic_vision_hypotheses`

### W2-B-0333 — Multi-agent debate over ambiguous images converges to language priors, not visual evidence — debate as hallucination amplifier.

- **problem:** Debate between VLM agents is proposed as an error-correction mechanism; on visually-ambiguous inputs, shared language priors may dominate the equilibrium, making debate systematically anti-visual.
- **core_hypothesis:** On controlled-ambiguity images (degraded evidence for prior-incongruent content), debate shifts final answers toward prior-congruent conclusions relative to single-model answers, and the shift grows with debate rounds — the opposite of evidence aggregation.
- **why_important:** A demonstrated amplification effect would warn against debate-style aggregation for perception tasks and quantify when it is safe.
- **why_possibly_novel:** Prior-vs-evidence convergence analysis of visual debate is new.
- **minimal_experiment:** Construct ambiguity-controlled image batteries with prior-incongruent ground truth; run debates across round counts; measure prior-drift vs single-model baselines.
- **main_risk:** Debate protocols vary widely; test several canonical implementations.
- **cluster:** `agentic_vision_hypotheses`
- **mutate_from:** W2-B-0325

### W2-B-0334 — Agents select vision tools by name matching, not capability: misnamed-tool batteries expose capability-blind routing.

- **problem:** Tool selection in vision agents is assumed to reflect understanding of tool capabilities; if selection is driven by lexical similarity between task and tool names, agents fail predictably when names mislead.
- **core_hypothesis:** Swapping tool names (keeping capabilities fixed) redirects a large fraction of tool calls, and providing capability descriptions instead of names only partially repairs selection — quantifying name-driven routing in current agents.
- **why_important:** Establishes evaluation and interface standards (capability cards, verified routing) before agentic-vision systems scale.
- **why_possibly_novel:** Name-vs-capability attribution for vision-tool routing is new.
- **minimal_experiment:** Build tool suites with permuted names, misleading names, and name-free capability descriptions; measure selection accuracy and downstream task cost across agent frameworks.
- **main_risk:** Results may vary with prompt scaffolds; standardize scaffolds and report sensitivity.
- **cluster:** `agentic_vision_hypotheses`

### W2-B-0335 — Uncertainty-driven region querying by an agent beats random querying for dense-label acquisition only above a measurable feature-quality floor.

- **problem:** An agent choosing which regions to send to an oracle (human or premium model) implements active learning with VFM uncertainty; whether the VFM's uncertainty is good enough to beat random selection — and when — is unquantified for dense adaptation.
- **core_hypothesis:** Uncertainty-guided region selection outperforms random by margins that grow with the backbone's calibration quality, falling below random under severe shift where uncertainty is misranked — a floor condition measurable in advance.
- **why_important:** Defines when agentic label-acquisition loops pay, preventing worse-than-random active learning in shifted deployments.
- **why_possibly_novel:** Floor-condition analysis for VFM-uncertainty-driven dense active learning is new.
- **minimal_experiment:** Run region-query loops with uncertainty vs random selection across shift severities; correlate active-learning gains with pre-measured uncertainty quality; validate the floor predictor.
- **main_risk:** Oracle simulation may flatter uncertainty methods; include human-annotator oracles on subsets.
- **cluster:** `agentic_vision_hypotheses`
- **mutate_from:** W2-B-0170

### W2-B-0336 — Retrieval-augmented dense prediction helps under low shift and poisons outputs beyond a shift threshold — retrieval as a double-edged memory.

- **problem:** Agents with episodic memory retrieve similar past images and reuse their masks/labels as context; when the retrieval distribution mismatches the current input, retrieved context may override correct perception.
- **core_hypothesis:** Retrieval-augmented segmentation gains decay with input-to-memory distribution distance and turn negative past a threshold — retrieved masks actively displace correct boundaries — with the threshold predictable from retrieval-score calibration.
- **why_important:** Establishes safety conditions for memory-augmented vision agents before the pattern proliferates.
- **why_possibly_novel:** Harm-threshold characterization for dense retrieval augmentation is new.
- **minimal_experiment:** Sweep memory-input distribution gaps; measure gains and contamination cases; fit the threshold; test retrieval-score gating as mitigation.
- **main_risk:** Retrieval implementations vary; use several standard schemes.
- **cluster:** `agentic_vision_hypotheses`
- **mutate_from:** W2-B-0129

### W2-B-0337 — Program-synthesis visual reasoning fails on continuous quantities because tool interfaces quantize: errors concentrate at inter-tool boundaries.

- **problem:** Code-generating agents (ViperGPT-style — naming UNVERIFIED, needs lit search) decompose visual questions into tool calls; continuous quantities (sizes, distances, shades) must cross discrete tool interfaces, a plausible systematic failure locus never isolated.
- **core_hypothesis:** Error analysis shows compositional programs succeed on categorical subtasks but fail disproportionately on continuous-quantity subtasks, with errors traceable to quantization at tool boundaries (thresholded outputs, discretized labels) rather than tool internals.
- **why_important:** Locates the failure at interface design — actionable — rather than in "reasoning", redirecting agentic-vision engineering.
- **why_possibly_novel:** Interface-quantization attribution for program-based visual reasoning is new.
- **minimal_experiment:** Build matched categorical/continuous question pairs; trace per-step errors through program execution; attribute failures to interfaces vs tools vs planning.
- **main_risk:** Tracing requires instrumented frameworks; use open implementations.
- **cluster:** `agentic_vision_hypotheses`

### W2-B-0338 — Web-browsing vision agents contaminate their own evaluation: benchmark answers are retrievable, and contamination rates are measurable.

- **problem:** Agents with search/browse tools may retrieve benchmark images' published annotations rather than perceiving; the contamination rate of agentic-vision evaluations — and its effect on reported scores — is unmeasured.
- **core_hypothesis:** A measurable fraction of benchmark items are answerable through retrieval alone (no image processing), agents exploit this at detectable rates (answer-provenance tracing), and blinding (perturbing images to break retrieval) drops agent scores significantly more than non-agent baselines.
- **why_important:** Evaluation integrity for the fastest-growing class of vision systems; establishes contamination-resistant protocol requirements.
- **why_possibly_novel:** Contamination-rate measurement for agentic vision evaluation is new.
- **minimal_experiment:** Trace agent tool calls on benchmarks; measure retrieval-answerable fractions; compare scores on retrieval-blinded variants; propose contamination-resistant evaluation.
- **main_risk:** Provenance tracing is framework-dependent; sandbox the browsing environment fully.
- **cluster:** `agentic_vision_hypotheses`

### W2-B-0339 — Agentic loops versus bigger encoders at matched compute: the crossover is task-structured and measurable.

- **problem:** Agent loops (crop, re-query, verify) spend inference compute that could buy a larger single-pass model; the field lacks matched-compute comparisons showing when iteration beats scale.
- **core_hypothesis:** At matched total FLOPs, agentic iteration beats single-pass scale on tasks with localized, sparse evidence (small text, fine details) but loses on tasks needing global integration (scene classification, layout), with the boundary predictable from evidence-locality metrics.
- **why_important:** A compute-allocation rule for system designers choosing between agent loops and model scale.
- **why_possibly_novel:** Matched-compute agent-vs-scale frontiers for vision are unmeasured.
- **minimal_experiment:** Sweep compute budgets for agentic pipelines and encoder scales on evidence-locality-stratified tasks; map crossover boundaries; validate the locality predictor.
- **main_risk:** FLOP accounting for agent episodes is variable; report distributions, not just means.
- **cluster:** `agentic_vision_hypotheses`
- **mutate_from:** W2-B-0330

### W2-B-0340 — Calibrated uncertainty dies at tool boundaries: pipelines discard distributional information at every interface, and the loss is quantifiable per hop.

- **problem:** Vision tools produce calibrated scores that agent pipelines flatten into text or hard decisions before the next stage; the end-to-end calibration loss per interface has never been accounted.
- **core_hypothesis:** Measuring calibration at each pipeline stage shows large, quantifiable information loss at tool-to-agent interfaces (score-to-text conversion dominates), and preserving distributional outputs across just the single worst interface recovers most end-to-end calibration.
- **why_important:** Interface-level accounting tells builders exactly where to invest — likely a one-interface fix rather than system redesign.
- **why_possibly_novel:** Hop-by-hop calibration accounting for vision pipelines is new.
- **minimal_experiment:** Instrument multi-tool pipelines; measure calibration at every hop; ablate interface formats (text, top-k, full distributions); identify and validate the dominant-loss interface.
- **main_risk:** Calibration at intermediate stages needs task-specific ground truth; use densely-annotated episodes.
- **cluster:** `agentic_vision_hypotheses`
- **mutate_from:** W2-B-0329

### W2-B-0341 — External visual scratchpads (agent-annotated images) outperform internal chain-of-thought on multi-step spatial tasks — a working-memory hypothesis for VLMs.

- **problem:** VLMs lack persistent visual working memory across reasoning steps; letting an agent physically annotate its image (marks, masks) externalizes state, but whether externalization causally improves multi-step spatial reasoning is untested.
- **core_hypothesis:** On tasks requiring tracking multiple spatial references (mazes, correspondence chains, multi-object relations), scratchpad-enabled agents beat matched text-only chain-of-thought at equal compute, and the advantage scales with the task's working-memory load, not its difficulty per se.
- **why_important:** Establishes visual working memory as the binding constraint on multi-step spatial reasoning and externalization as a principled remedy.
- **why_possibly_novel:** Working-memory-load-controlled evaluation of visual scratchpads is new.
- **minimal_experiment:** Design task batteries with factorized memory load and difficulty; compare scratchpad vs text reasoning at matched compute; test the load-specific interaction.
- **main_risk:** Scratchpad marks may leak answer structure; use load-matched control conditions.
- **cluster:** `agentic_vision_hypotheses`
- **mutate_from:** W2-B-0332

### W2-B-0342 — Decompose-and-answer agents systematically substitute easier subquestions — question drift is measurable with paired probes.

- **problem:** Agents decomposing visual questions may answer a subtly different, easier question (typicality instead of observation); this substitution bias is hypothesized in human cognition but never measured in vision agents.
- **core_hypothesis:** Comparing agent answers against paired probes (the actual question vs the suspected substituted question, with dissociated ground truths) shows agents agreeing with the substitute significantly above the original on hard perceptual items — quantifying question drift per framework.
- **why_important:** Question drift undermines trust in agentic answers precisely on hard cases; measurement enables drift-resistant decomposition designs.
- **why_possibly_novel:** Substitution-bias measurement for visual agents is new.
- **minimal_experiment:** Build dissociated question pairs (observation vs typicality ground truths differ); run decomposition agents; measure substitution rates and their dependence on decomposition style.
- **main_risk:** Constructing cleanly-dissociated pairs is demanding; validate with human answer patterns.
- **cluster:** `agentic_vision_hypotheses`
- **mutate_from:** W2-B-0333

### W2-B-0343 — Agent self-training loops erode boundary quality first: dense pseudo-label bias compounds at a measurable per-iteration rate.

- **problem:** Agents that label data for their own fine-tuning (auto-labeling loops) inherit and amplify their dense-prediction biases; the compounding rate and its earliest-degrading metric are unmeasured for vision agents specifically.
- **core_hypothesis:** Across self-training iterations, boundary displacement bias grows near-linearly per round while region-level metrics hold, making boundary drift the early-warning signal for self-training collapse in dense agents.
- **why_important:** A measurable canary lets self-improving vision systems stop before silent quality erosion — operationally critical as auto-labeling spreads.
- **why_possibly_novel:** Iteration-resolved bias compounding for agentic self-labeling is new.
- **minimal_experiment:** Run controlled self-training loops on segmentation agents; track metric batteries per round against held-out ground truth; fit compounding rates; validate the boundary-drift canary.
- **main_risk:** Loop design choices affect rates; test several curation/filter policies.
- **cluster:** `agentic_vision_hypotheses`
- **mutate_from:** W2-B-0277

### W2-B-0344 — Delegation frequency maps a VLM's self-knowledge: whether models delegate to tools exactly where they actually err is a testable metacognition question.

- **problem:** Tool-choice behavior implicitly claims self-knowledge (delegate what you can't do); whether delegation correlates with the model's true error landscape — genuine metacognition — or with task-type stereotypes has never been measured.
- **core_hypothesis:** Per-task-type delegation rates correlate only weakly with the model's measured error rates (stereotype-driven delegation), and mismatches are directional: models under-delegate perceptual precision tasks and over-delegate tasks they could answer — a quantified metacognition deficit.
- **why_important:** Metacognitive accuracy bounds how much agents can gain from tools; measuring it identifies where delegation policies need external calibration.
- **why_possibly_novel:** Delegation-vs-error-landscape correlation analysis is new.
- **minimal_experiment:** Measure a VLM's error landscape across task types; then measure free-choice delegation rates with tools available; quantify the correlation and mismatch structure; test calibration-based delegation policies.
- **main_risk:** Delegation behavior is prompt-sensitive; marginalize over instruction phrasings.
- **cluster:** `agentic_vision_hypotheses`
- **mutate_from:** W2-B-0329

### W2-B-0345 — GUI grounding and natural-image grounding share failure mechanisms: transfer between them tests whether spatial grounding is domain-general.

- **problem:** Screen agents ground instructions to UI elements; whether their spatial failures are the same mechanism as natural-image grounding failures (shared spatial-representation deficit) or domain-specific determines if fixes transfer.
- **core_hypothesis:** Fine-tuning on natural-image grounding improves UI grounding (and vice versa) significantly beyond task-format effects, and per-model failure profiles (relation types, distractor sensitivity) correlate across domains — evidence for a shared spatial-grounding mechanism.
- **why_important:** A shared mechanism means the community's natural-image grounding progress transfers to the commercially-critical screen-agent domain for free; separation means duplicate effort is unavoidable.
- **why_possibly_novel:** Cross-domain transfer and failure-profile correlation analysis between UI and natural grounding is new.
- **minimal_experiment:** Cross-train and cross-evaluate grounding on UI and natural benchmarks; correlate failure-type profiles per model; decompose transfer into format vs mechanism components.
- **main_risk:** UI data has text shortcuts (OCR); control by separating text-locatable from purely-spatial UI targets.
- **cluster:** `agentic_vision_hypotheses`
- **mutate_from:** W2-B-0036
