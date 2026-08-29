# Windows2 Stage 1 - Agent A Idea Catalog (SAM / segmentation science)

Total ideas: **352**. Fields per idea: problem, falsifiable core hypothesis, importance, novelty status, minimal (cheapest) experiment, main risk, cluster, optional parent.

Epistemic labels used inside entries: **KNOWN** (established prior work I am confident exists), **HYPOTHESIS** (falsifiable claim proposed here), **SPECULATION** (weaker conjecture), **UNVERIFIED - needs lit search** (novelty not yet checked against literature; no citation invented).

## Table of contents

- [C01-sam-prompt-failure](#c01-sam-prompt-failure) (25 ideas: W2-A-0001..W2-A-0025)
- [C02-sam2-video-memory](#c02-sam2-video-memory) (25 ideas: W2-A-0026..W2-A-0050)
- [C03-medical-limits](#c03-medical-limits) (25 ideas: W2-A-0051..W2-A-0075)
- [C04-amorphous-smoke-fire](#c04-amorphous-smoke-fire) (25 ideas: W2-A-0076..W2-A-0100)
- [C05-transparent-glass-mirror](#c05-transparent-glass-mirror) (25 ideas: W2-A-0101..W2-A-0125)
- [C06-camouflage-ambiguity](#c06-camouflage-ambiguity) (25 ideas: W2-A-0126..W2-A-0150)
- [C07-boundary-small-objects](#c07-boundary-small-objects) (25 ideas: W2-A-0151..W2-A-0175)
- [C08-uncertainty-longtail](#c08-uncertainty-longtail) (25 ideas: W2-A-0176..W2-A-0200)
- [C09-annotation-interactive](#c09-annotation-interactive) (25 ideas: W2-A-0201..W2-A-0225)
- [C10-domain-shift](#c10-domain-shift) (25 ideas: W2-A-0226..W2-A-0250)
- [C11-weak-semi-self](#c11-weak-semi-self) (25 ideas: W2-A-0251..W2-A-0275)
- [C12-foundation-dense-science](#c12-foundation-dense-science) (25 ideas: W2-A-0276..W2-A-0300)
- [C13-benchmark-failure-audit](#c13-benchmark-failure-audit) (25 ideas: W2-A-0301..W2-A-0325)
- [C14-assumption-tests](#c14-assumption-tests) (27 ideas: W2-A-0326..W2-A-0352)

---

## C01-sam-prompt-failure

### W2-A-0001 - Point-prompt jitter variance of SAM masks predicts human inter-annotator disagreement per object.

- **Problem:** SAM outputs change under tiny prompt displacements, but nobody has established what this instability measures. It is treated as a nuisance rather than a signal.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the variance of SAM masks under small point jitter (e.g. 5-15 px perturbations) correlates strongly (rank r>0.6) with human inter-annotator mask disagreement on the same object, i.e. prompt sensitivity is an intrinsic object-ambiguity meter, not model noise.
- **Why important:** Would give a free, model-based ambiguity estimator usable for annotation routing, QA, and uncertainty without any labels.
- **Why possibly novel:** Prompt sensitivity is usually reported as a robustness defect; recasting it as a calibrated measurement of stimulus ambiguity is a different scientific claim. UNVERIFIED - needs lit search.
- **Minimal experiment:** Take a multi-annotator dataset (e.g. LVIS double annotations or a multi-rater medical set), compute SAM jitter-variance per object, correlate with inter-rater IoU. One GPU-day.
- **Main risk:** Correlation may be driven trivially by object size or boundary length; must partial these out.

### W2-A-0002 - Test whether SAM's three ambiguity heads implement a stable part/object/group hierarchy or an arbitrary mode split.

- **Problem:** SAM returns 3 masks for ambiguous prompts. The community assumes they represent whole/part/subpart levels, but this has not been verified across categories.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the identity of each output head is not semantically stable; head-to-granularity assignment flips across categories and even across prompt positions within one object, refuting the implicit 'hierarchy heads' assumption.
- **Why important:** Many pipelines pick a fixed head or trust head order; if assignment is unstable, those pipelines have a silent failure mode.
- **Why possibly novel:** Papers use the multimask output constantly but rarely audit what each head means. UNVERIFIED - needs lit search.
- **Minimal experiment:** For 1k objects with part annotations (PartImageNet, PACO), classify each head output as part/object/group by IoU and measure head-assignment consistency statistics.
- **Main risk:** Result may be 'mostly stable', a weaker but still publishable calibration finding.

### W2-A-0003 - SAM thin-structure failure is caused by patch-grid aliasing, not decoder capacity.

- **Problem:** SAM notoriously breaks wires, poles, and thin legs. The default explanation is decoder capacity or training data, but thin structures alias against the 16-px patch grid.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for structures thinner than ~1 patch, SAM mask quality is a strong function of the structure's sub-patch phase and orientation relative to the tokenization grid; phase-averaging inputs (sub-patch shifts) recovers a large fraction of the error without any retraining.
- **Why important:** Locates the failure in tokenization physics rather than learning, which changes what fixes are rational.
- **Why possibly novel:** Aliasing analyses exist for CNN downsampling (KNOWN: Zhang, 'Making Convolutional Networks Shift-Invariant Again'), but a phase-sweep causal study on promptable ViT segmenters is UNVERIFIED - needs lit search.
- **Minimal experiment:** Render synthetic bars of controlled width/orientation, sweep sub-pixel translation, plot SAM IoU vs phase; then test phase-jitter ensembling on real wire/pole classes.
- **Main risk:** Failure may be dominated by training-data scarcity of thin objects, with aliasing a minor term.

### W2-A-0004 - Box prompts act as scale priors that override image evidence when box and object conflict.

- **Problem:** Box-prompted SAM is assumed to segment 'the object in the box', but boxes also carry scale/aspect information the model may trust more than pixels.
- **Core hypothesis (falsifiable):** HYPOTHESIS: when a box is systematically inflated or squashed (e.g. 1.5x width), SAM's mask follows the box geometry rather than the true object boundary in a predictable, measurable way (mask aspect regresses toward box aspect), demonstrating that boxes are priors, not just localizers.
- **Why important:** Auto-labeling pipelines feed detector boxes into SAM; detector box errors would then be copied into masks, correlated and invisible.
- **Why possibly novel:** Box-perturbation robustness is reported as a scalar; the directional 'mask follows box geometry' regression law is unquantified. UNVERIFIED - needs lit search.
- **Minimal experiment:** On COCO GT boxes, apply controlled aspect/scale perturbations, fit mask-aspect vs box-aspect response curves per category.
- **Main risk:** Effect may be small for well-textured objects and only matter for low-contrast ones; need stratified analysis.

### W2-A-0005 - Negative clicks carve masks asymmetrically: exclusion near boundaries works, exclusion inside homogeneous regions fails.

- **Problem:** Interactive SAM correction assumes positive and negative clicks are symmetric information. Practitioners observe negatives often do nothing or overshoot.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the information gain of a negative click is a strong function of local feature contrast: negatives placed in feature-homogeneous regions (same texture as the object) reduce error far less per click than positives of matched placement, making click budgets asymmetric.
- **Why important:** Click-budget benchmarks (NoC) average over this; interfaces could route users toward the click type with higher expected gain.
- **Why possibly novel:** Click simulators treat clicks symmetrically; a measured positive/negative information asymmetry law would be new. UNVERIFIED - needs lit search.
- **Minimal experiment:** On DAVIS/COCO objects, exhaustively grid-place a single corrective negative vs positive click, map per-pixel error reduction, compare distributions.
- **Main risk:** Asymmetry might be an artifact of one model version; verify on SAM-HQ and SAM2 image mode.

### W2-A-0006 - SAM snaps to luminance edges even when the semantic boundary is texture- or material-defined; quantify the edge-snapping bias.

- **Problem:** SAM boundaries look crisp, but crispness may come from locking onto intensity gradients rather than the true semantic boundary (e.g. shadow edges, printed patterns).
- **Core hypothesis (falsifiable):** HYPOTHESIS: on stimuli where the semantic boundary and the strongest local intensity edge are deliberately separated (shadow crossing an object, texture-defined figure), SAM boundary placement is biased toward the intensity edge by a measurable offset that scales with edge contrast ratio.
- **Why important:** Explains a family of confident-but-wrong boundaries (shadow inclusion, pattern following) that boundary metrics currently lump into generic error.
- **Why possibly novel:** Edge-snapping is folklore; a psychophysics-style controlled quantification with synthesized conflict stimuli appears missing. UNVERIFIED - needs lit search.
- **Minimal experiment:** Composite objects with controllable shadow/texture edges (cut-and-paste with relighting), sweep contrast, measure boundary displacement toward distractor edge.
- **Main risk:** Synthetic conflict stimuli may be out-of-distribution in ways that exaggerate the bias.

### W2-A-0007 - SAM's predicted-IoU head is miscalibrated in a shape-dependent way: overconfident on concave and perforated objects.

- **Problem:** Predicted IoU is widely used to filter auto-generated masks (SA-1B itself was built this way), but its calibration as a function of object geometry is unexamined.
- **Core hypothesis (falsifiable):** HYPOTHESIS: predicted-IoU error is systematically structured by shape statistics (convexity, genus, boundary tortuosity): calibration is good for convex blobs and degrades monotonically with concavity/holes, so IoU-filtered datasets are silently biased toward simple shapes.
- **Why important:** If true, every dataset distilled through SAM confidence filtering under-represents complex shapes, and models trained on them inherit a simplicity prior - a compounding ecosystem bias.
- **Why possibly novel:** Connects mask-confidence calibration to dataset evolution/inbreeding; per-geometry calibration audits of SAM are UNVERIFIED - needs lit search.
- **Minimal experiment:** On COCO/ADE GT, bin objects by convexity and genus, plot predicted vs actual IoU per bin; then measure shape statistics of SA-1B vs a human-annotated reference.
- **Main risk:** SA-1B shape bias could stem from its prompting grid rather than the IoU filter; needs an ablation to attribute.

### W2-A-0008 - Iterative click sequences are path-dependent: the same click set in different orders yields different SAM masks.

- **Problem:** Interactive segmentation evaluation assumes the final mask depends on the set of corrections, but SAM conditions on previous mask state, making the process a dynamical system.
- **Core hypothesis (falsifiable):** HYPOTHESIS: permuting the order of an identical set of 4-6 clicks changes final mask IoU by a nontrivial margin (>5 IoU on ambiguous objects), and there exist 'trap' orders from which no small click set recovers - i.e. interactive SAM has attractor states.
- **Why important:** Path dependence means NoC benchmarks measure simulator policy as much as model quality, and real users can get stuck through no fault of their own.
- **Why possibly novel:** Framing interactive segmentation as a dynamical system with attractors and measuring order effects is not standard. UNVERIFIED - needs lit search.
- **Minimal experiment:** Sample 200 hard objects, enumerate permutations of a fixed 4-click set, report IoU dispersion and identify absorbing bad states.
- **Main risk:** Effect may vanish on easy objects, limiting scope to the ambiguous tail (which is arguably where it matters).

### W2-A-0009 - Predict SAM failure before decoding from encoder attention statistics alone.

- **Problem:** Failure detection for SAM currently uses output-side signals (predicted IoU, stability score). Whether failure is already legible in the encoder is unknown.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a linear probe on encoder attention-map statistics (entropy, sink mass, head disagreement) at the prompt location predicts mask failure (IoU<0.5) with AUROC>0.8, i.e. most failures are encoder-representation failures, not decoder mistakes.
- **Why important:** Locates the failure stage (representation vs readout), and gives a cheap abort/route-to-human signal that does not require running multiple decodes.
- **Why possibly novel:** Stage-attribution of promptable segmentation failures is largely unexplored. UNVERIFIED - needs lit search.
- **Minimal experiment:** Log encoder statistics + outcome over 20k prompts on 3 datasets, train the probe, compare AUROC vs predicted-IoU baseline.
- **Main risk:** Probe may just re-learn object size/contrast correlates of difficulty rather than model-internal evidence.

### W2-A-0010 - SAM merges instances of periodic textures (fences, railings, book spines) when spatial period is below token resolution.

- **Problem:** Repeated near-identical instances are a known annoyance, but the quantitative relationship between texture period and instance-merging has not been mapped.
- **Core hypothesis (falsifiable):** HYPOTHESIS: instance-level prompting accuracy on periodic arrays collapses sharply when the array period drops below ~2 patch widths, and the collapse point shifts predictably with input resolution - a measurable 'instance Nyquist limit'.
- **Why important:** Defines a hard operating boundary for promptable segmentation in retail, agriculture (crop rows), and document images, and predicts exactly when zooming will fix it.
- **Why possibly novel:** A Nyquist-style law for instance separability in promptable models is a crisper claim than 'small objects are hard'. UNVERIFIED - needs lit search.
- **Minimal experiment:** Procedurally render object arrays with controlled period/count, prompt the center instance, plot single-instance IoU vs period/patch ratio across resolutions.
- **Main risk:** Real scenes add occlusion and perspective; the clean law may blur in the wild.

### W2-A-0011 - Sub-patch objects get quantized to the token grid: measure the staircase floor of SAM on <16 px objects.

- **Problem:** SAM small-object failure is usually attributed to semantics or data. A simpler mechanical explanation: masks cannot express detail below feature-map resolution regardless of semantics.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for objects below ~16 px, SAM's best-achievable IoU (even with oracle prompts and oracle head choice) is bounded by a resolution floor computable from the mask-decoder upsampling path, and observed errors match this floor - meaning small-object failure is mostly resolution, not recognition.
- **Why important:** Separates 'model cannot see it' from 'model cannot draw it'; the fix differs completely (zoom pipelines vs retraining).
- **Why possibly novel:** An explicit computed-vs-observed error floor comparison for promptable segmenters is missing. UNVERIFIED - needs lit search.
- **Minimal experiment:** Take objects at many scales, segment at native + digitally zoomed resolution, compare the error decomposition against the theoretical decoder floor.
- **Main risk:** Decoder nonlinearity may make the 'theoretical floor' hard to define cleanly; may need an empirical oracle-upsampler proxy.

### W2-A-0012 - Cluster SAM's mask-token embeddings across millions of prompts to test whether text-free training induced a latent semantic taxonomy.

- **Problem:** SAM was trained without labels. Whether its object-level tokens organize into semantic structure (animal vs artifact, etc.) or purely geometric structure is an open representational question.
- **Core hypothesis (falsifiable):** HYPOTHESIS: mask-token embeddings cluster by geometry (shape, size, texture) and NOT by semantic category - i.e. semantic clustering accuracy will be near chance once shape covariates are controlled, contradicting casual claims that 'SAM knows objects'.
- **Why important:** Clarifies what class-agnostic pretraining actually learns, informing when SAM features can and cannot substitute for semantic backbones.
- **Why possibly novel:** Controlled geometry-vs-semantics decomposition of SAM token space (with shape covariates regressed out) is UNVERIFIED - needs lit search.
- **Minimal experiment:** Extract mask tokens for 50k labeled COCO/ADE objects, run category linear probe before/after regressing out shape descriptors; compare with a CLIP-feature control.
- **Main risk:** Shape and semantics are naturally confounded; the covariate control must be convincing.

### W2-A-0013 - Define 'prompt compressibility' - the minimum click set reproducing a GT mask - as a measurable object complexity scale.

- **Problem:** There is no principled per-object measure of how hard an object is for promptable segmentation; NoC conflates simulator policy with intrinsic difficulty.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the minimal sufficient prompt set size (found by search, not by a fixed simulator) forms a stable complexity measure that (a) is consistent across SAM variants and (b) predicts real human annotation time better than object area, boundary length, or NoC from standard simulators.
- **Why important:** Would give datasets an intrinsic difficulty axis and annotation-cost predictor, useful for budgeting and curriculum design.
- **Why possibly novel:** Kolmogorov-style 'description length in clicks' framing of segmentation difficulty appears new. UNVERIFIED - needs lit search.
- **Minimal experiment:** Beam-search minimal click sets on 500 objects, correlate with logged human annotation times (e.g. from an internal labeling session).
- **Main risk:** Search cost per object; and minimality may be model-specific despite the cross-variant claim.

### W2-A-0014 - Map the phase diagram of prompt positions that flip SAM mask topology - the 'topological instability atlas' of an image.

- **Problem:** Some single-pixel prompt moves cause categorical mask changes (object vs part vs background leak). Where these cliff edges live and what image structure creates them is uncharacterized.
- **Core hypothesis (falsifiable):** HYPOTHESIS: topology-flip boundaries in prompt space concentrate along medial-axis and low-contrast corridors of the underlying objects, so the instability atlas is predictable from image structure without running SAM densely.
- **Why important:** Predictable instability zones let interfaces warn users, let simulators sample fairly, and reveal what the decoder's implicit object model is.
- **Why possibly novel:** Dense prompt-space mapping exists in robustness papers as averages; structural prediction of instability geography is UNVERIFIED - needs lit search.
- **Minimal experiment:** Densely evaluate prompts on 100 images, compute flip boundaries, test prediction from medial axis + local contrast features.
- **Main risk:** Atlas may be high-frequency noise rather than structured, making prediction fail (itself an informative negative).

### W2-A-0015 - Attribute SAM small-object errors to resolution vs recognition with a zoom-oracle: how much failure survives perfect zoom?

- **Problem:** Zoom-in cascades are the standard small-object fix, but nobody has cleanly measured what fraction of failure is unfixable by resolution alone.
- **Core hypothesis (falsifiable):** HYPOTHESIS: with an oracle crop centered on each small object at optimal zoom, SAM recovers >70% of the IoU gap on natural images, but a hard residual remains concentrated in low-contrast and cluttered contexts where recognition, not resolution, is the limit.
- **Why important:** Quantifies the ceiling of all zoom-based engineering fixes and identifies the residual scientific problem.
- **Why possibly novel:** The oracle-zoom decomposition, reported per failure type, is a cleaner attribution than existing multi-scale ablations. UNVERIFIED - needs lit search.
- **Minimal experiment:** On LVIS-small and xView-like imagery, run SAM native vs oracle-crop, decompose the gap by contrast/clutter strata.
- **Main risk:** Oracle crops change context available to the model, conflating context loss with resolution gain; needs padded-crop controls.
- **Mutated from:** W2-A-0011

### W2-A-0016 - SAM draws sharper boundaries than humans do on intrinsically fuzzy objects - measure the sharpness mismatch distribution.

- **Problem:** On hair, fur, foliage, and smoke-like regions, ground truth is soft but SAM outputs hard crisp curves. The statistical mismatch between model boundary sharpness and human boundary width is undocumented.
- **Core hypothesis (falsifiable):** HYPOTHESIS: SAM's boundary transition width is near-constant (a decoder property) regardless of the stimulus' physical edge width, whereas human annotations widen with stimulus fuzziness - so a single scalar 'sharpness mismatch' per class predicts where SAM boundary metrics are meaningless.
- **Why important:** Identifies where binary mask evaluation stops being well-posed and matting-style evaluation must take over.
- **Why possibly novel:** Boundary-width statistics as a function of stimulus edge width, compared human-vs-model, appears unmeasured. UNVERIFIED - needs lit search.
- **Minimal experiment:** Estimate edge transition widths from alpha mattes (Adobe matting datasets), compare with SAM logit transition widths per stimulus.
- **Main risk:** Logit sharpness may be an artifact of the final threshold rather than the representation; inspect pre-threshold logits.

### W2-A-0017 - SA-1B's auto-mask pipeline imprinted a closed-compact-region prior on SAM; open curves and wiry objects are structurally outside its output space.

- **Problem:** SAM fails on wires, cracks, and open contours. This is usually attributed to rarity, but SA-1B's generation process (grid prompts + IoU filtering) may have structurally excluded non-blob masks.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the shape-statistics gap between SA-1B masks and a reference human-annotated distribution (elongation, genus, solidity tails) quantitatively predicts SAM's per-shape-class failure rates - data-generating-process bias, not visual difficulty, explains wiry-object failure.
- **Why important:** Reframes a famous failure mode as an auditable dataset-construction artifact with a testable fingerprint, guiding what data (not architecture) to fix.
- **Why possibly novel:** Causal linking of SA-1B pipeline choices to specific inference-time failure geometry is UNVERIFIED - needs lit search.
- **Minimal experiment:** Compute shape-statistic histograms of SA-1B (public) vs OpenImages/ADE masks; regress SAM failure rate per shape bin against representation gap.
- **Main risk:** Correlation not causation; a small targeted fine-tune on synthetic wiry masks would be needed for the causal leg.

### W2-A-0018 - At high JPEG compression, SAM boundaries snap to 8x8 block-grid artifacts; quantify compression-boundary coupling.

- **Problem:** Deployment images are heavily compressed; block artifacts create fake edges aligned to a fixed grid. Whether promptable models lock onto them is untested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: as JPEG quality decreases, the phase histogram of SAM boundary positions modulo 8 px develops peaks at block boundaries, and this grid-snapping accounts for a measurable share of the compression-induced IoU drop.
- **Why important:** A concrete, correctable deployment failure (choose compression settings / add dither) with a clean forensic signature.
- **Why possibly novel:** Compression robustness is studied as an aggregate score; the grid-phase forensic analysis of boundary placement appears new. UNVERIFIED - needs lit search.
- **Minimal experiment:** Sweep JPEG quality on COCO, compute boundary-position phase histograms and IoU deltas; test dithered decompression as mitigation.
- **Main risk:** Modern webp/HEIC pipelines differ; scope must include them to stay relevant.

### W2-A-0019 - Test compositionality of SAM's image embedding: does masked-object feature subtraction behave algebraically?

- **Problem:** SAM's encoder embedding is treated as a black box. Whether object presence is encoded additively (removable by subtraction, movable by translation in feature space) is unknown.
- **Core hypothesis (falsifiable):** HYPOTHESIS: SAM embeddings are NOT compositional - subtracting the pooled feature of an object region does not suppress its segmentability, showing objectness is encoded relationally rather than additively (falsifiable: if subtraction works, hypothesis is dead).
- **Why important:** Determines whether feature-space editing (fast object removal, counterfactual segmentation) is possible without pixel-space editing, and probes the representation's algebra.
- **Why possibly novel:** Feature-arithmetic tests are common for word/CLIP embeddings, rare for dense promptable encoders. UNVERIFIED - needs lit search.
- **Minimal experiment:** For 500 objects: embed image, ablate object features (zero/subtract/shuffle), re-run decoder with same prompt, measure mask persistence.
- **Main risk:** Decoder may re-hallucinate objects from context, confounding 'representation holds object' with 'decoder guesses'.

### W2-A-0020 - Grid-prompted 'segment everything' mode has a recall geometry: elongated and off-grid objects are systematically missed as a function of grid density.

- **Problem:** Everything-mode uses a regular point grid + NMS; its recall is assumed to rise smoothly with density, but object geometry interacts with the grid non-uniformly.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at fixed grid density, per-object recall is predicted by the probability that a grid point lands in the object's 'promptable core' (a computable region smaller than the mask), so everything-mode recall can be forecast per dataset without running the model, and elongated objects need quadratically denser grids.
- **Why important:** Everything-mode underlies many auto-annotation pipelines; a predictive recall law would let people budget grid density instead of guessing.
- **Why possibly novel:** Treats prompt-grid coverage as a geometric sampling problem with a testable analytic form. UNVERIFIED - needs lit search.
- **Minimal experiment:** Estimate promptable cores on 1k objects (dense prompting), derive predicted recall vs grid density, verify against actual everything-mode runs.
- **Main risk:** NMS interactions between neighboring objects may break the independent-coverage approximation.

### W2-A-0021 - Disagreement among SAM's three heads beats its predicted-IoU score as an out-of-distribution failure detector.

- **Problem:** Pipelines filter SAM outputs by predicted IoU, but that head was trained in-distribution and may be blind to OOD failure; the multimask heads provide a free ensemble signal.
- **Core hypothesis (falsifiable):** HYPOTHESIS: inter-head mask disagreement (pairwise IoU among the 3 outputs) is a better OOD failure predictor than predicted IoU on shifted domains (medical, thermal, art), with the gap growing with shift severity.
- **Why important:** A zero-cost reliability signal for the most common filtering decision in SAM pipelines.
- **Why possibly novel:** Using ambiguity-head disagreement specifically as an OOD detector, benchmarked against the IoU head, is UNVERIFIED - needs lit search.
- **Minimal experiment:** On 5 shifted datasets with GT, compute AUROC of both signals for predicting IoU<0.5; one GPU-day.
- **Main risk:** Both signals may fail together on strong shift, leaving no winner (still a useful negative result).
- **Mutated from:** W2-A-0002

### W2-A-0022 - The Jacobian of SAM's mask w.r.t. prompt location is a label-free edge/structure detector - characterize what it computes.

- **Problem:** Differentiating mask output with respect to prompt coordinates yields a sensitivity field over the image. What classical quantity this field approximates (edges, medial axis, affordance boundaries) is unknown.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the prompt-Jacobian field concentrates on object-ownership boundaries rather than photometric edges, so it matches human-annotated occlusion/ownership boundaries (BSDS-style) better than Canny or learned edge detectors that use photometry alone.
- **Why important:** Would extract a new dense output (boundary ownership) from a frozen model for free, and reveal what geometric structure prompt conditioning learned.
- **Why possibly novel:** Prompt-space differentiation as a readout mechanism appears unexplored. UNVERIFIED - needs lit search.
- **Minimal experiment:** Finite-difference the prompt over a coarse grid on BSDS500 images, evaluate against boundary GT vs Canny/HED baselines.
- **Main risk:** Field may be too noisy at feasible grid resolutions; smoothing may destroy the claimed specificity.

### W2-A-0023 - A dataset-level 'promptability score' measured on unlabeled images predicts downstream annotation cost and model fine-tuning difficulty.

- **Problem:** Teams choose datasets/domains to annotate with no quantitative predictor of how much SAM-assisted annotation will actually save.
- **Core hypothesis (falsifiable):** HYPOTHESIS: an unlabeled-data statistic built from SAM behavior (jitter stability, head agreement, everything-mode mask density entropy) predicts realized human correction time per image with r>0.7 across domains, enabling annotation budgeting before any labeling starts.
- **Why important:** Converts anecdotal 'SAM works/doesn't work on our data' into a forecastable quantity with direct economic value.
- **Why possibly novel:** Dataset-level meta-prediction of assisted-annotation cost is UNVERIFIED - needs lit search.
- **Minimal experiment:** Across 8 public datasets with known annotation protocols, compute the score and correlate with measured correction effort on 50 images each.
- **Main risk:** Ground-truth 'annotation cost' is hard to standardize across domains; needs a controlled labeling study.
- **Mutated from:** W2-A-0001

### W2-A-0024 - SAM has an orientation anisotropy: elongated vertical vs horizontal objects segment differently, inherited from photo statistics.

- **Problem:** Natural photo datasets have anisotropic orientation statistics (gravity, horizons). Whether promptable segmenters are measurably anisotropic - and whether that transfers as failure on rotated/aerial imagery - is untested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: SAM IoU on matched elongated objects differs by orientation (e.g. worse for diagonal orientations), the anisotropy profile mirrors SA-1B orientation statistics, and it predicts a large share of SAM's aerial/rotated-image degradation.
- **Why important:** Aerial, microscopy, and document images have no canonical orientation; an inherited gravity prior would be a systematic transfer failure with a cheap fix (orientation TTA).
- **Why possibly novel:** Orientation-anisotropy audits exist for CN classifiers; for promptable segmentation with a data-statistics linkage, UNVERIFIED - needs lit search.
- **Minimal experiment:** Rotate a fixed object set through 24 angles (with anti-aliased resampling controls), plot IoU vs angle; compare with SA-1B mask orientation histogram.
- **Main risk:** Resampling artifacts can masquerade as model anisotropy; controls must be strict.

### W2-A-0025 - SAM is biased toward simply-connected masks: objects with holes get their holes filled, at a rate predictable from training statistics.

- **Problem:** Donut-topology objects (mugs seen through handles, rings, fences around gaps) require genus>0 masks. Whether promptable models can express and choose them is unquantified.
- **Core hypothesis (falsifiable):** HYPOTHESIS: SAM fills genus>0 regions at a high rate even when photometric evidence for the hole is strong, and the fill rate tracks the (near-zero) frequency of holed masks in SA-1B - an expressivity-through-data limitation, falsifiable by fine-tuning on synthetic holed masks and watching the rate drop.
- **Why important:** Topology errors corrupt measurement applications (porosity, occlusion reasoning) and are invisible in IoU at small hole sizes.
- **Why possibly novel:** Genus-statistics audit linking training-mask topology to inference topology bias is UNVERIFIED - needs lit search.
- **Minimal experiment:** Curate 300 holed-object images, measure hole preservation vs hole size/contrast; count genus>0 masks in SA-1B sample for the comparison.
- **Main risk:** Annotated GT for holes is scarce; may need manual curation effort.
- **Mutated from:** W2-A-0017

## C02-sam2-video-memory

### W2-A-0026 - Masklet drift rate in SAM2 is predictable from first-frame single-image ambiguity before any tracking happens.

- **Problem:** Video object segmentation failures appear frame-by-frame, but the community treats drift as a temporal phenomenon; it may be pre-determined by initial mask ambiguity.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-object drift rate (IoU decay slope over frames) is predicted (r>0.6) by frame-0 measurements alone (prompt-jitter variance, head disagreement), meaning drift is mostly ambiguity amplification, not accumulating temporal error.
- **Why important:** Enables pre-flight triage of which objects need human keyframing before wasting tracking compute, and reorients drift research from temporal machinery to initial disambiguation.
- **Why possibly novel:** Prediction of temporal failure from purely static initial measurements is UNVERIFIED - needs lit search.
- **Minimal experiment:** On DAVIS/MOSE, regress observed drift slopes on frame-0 ambiguity features; compare against motion-based predictors.
- **Main risk:** Drift may be dominated by discrete events (occlusions) that no frame-0 signal can foresee.
- **Mutated from:** W2-A-0001

### W2-A-0027 - SAM2 re-identification after occlusion falls off a cliff, not a slope: map the memory-horizon discontinuity.

- **Problem:** How re-acquisition probability depends on occlusion duration is unmeasured; a cliff vs gradual decay implies different mechanisms (buffer eviction vs feature fade).
- **Core hypothesis (falsifiable):** HYPOTHESIS: re-ID success is roughly flat until an occlusion-length threshold tied to the memory-bank capacity/eviction rule, then collapses discontinuously - and the threshold moves when memory size is reconfigured, causally implicating eviction policy rather than appearance change.
- **Why important:** A sharp, configurable failure boundary is exactly what deployment safety cases need, and the causal knob test tells us what to redesign.
- **Why possibly novel:** Occlusion-duration response curves with memory-size interventions are UNVERIFIED - needs lit search.
- **Minimal experiment:** Procedurally insert variable-length full occlusions into videos, plot re-ID rate vs duration for 3 memory configurations.
- **Main risk:** Entangled confound: longer occlusion often co-occurs with more scene change; synthetic occluders control this.

### W2-A-0028 - Test whether SAM2 tracks appearance or location: teleport experiments separating the two.

- **Problem:** When target and distractor swap positions between frames, does SAM2 follow the pixels or the place? The relative weighting of location prior vs appearance matching is unknown.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at low frame rates or after cuts, SAM2 follows spatial location over appearance (segmenting whatever now occupies the old position) with probability rising as inter-frame displacement grows - i.e. its memory attention degrades into a location prior under temporal sparsity.
- **Why important:** Determines trustworthiness on cut-heavy or low-fps footage (surveillance, wildlife cameras, medical cine loops).
- **Why possibly novel:** Teleport/swap causal probes are standard in psychology, rare for VOS models. UNVERIFIED - needs lit search.
- **Minimal experiment:** Construct swap/teleport clips from static images (two similar objects exchanging positions with controlled gaps), measure follow-the-object vs follow-the-place rates.
- **Main risk:** Synthetic cuts may be OOD; validate on natural cut footage with manual GT.

### W2-A-0029 - SAM2 masklets shrink over time: an erosion bias in memory-conditioned decoding.

- **Problem:** Anecdotally, tracked masks lose thin parts and extremities over long sequences. Whether there is a systematic signed area bias (erosion vs dilation) and what causes it is unstudied.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the signed relative-area error of SAM2 masklets trends negative over time, concentrated at high-curvature and thin regions, because memory features average over past masks and act as a low-pass shape filter - falsifiable by measuring area drift on constant-size rigid objects.
- **Why important:** Systematic bias (unlike variance) is correctable post-hoc if characterized; also matters for measurement uses (lesion tracking, plant growth).
- **Why possibly novel:** Signed morphological bias analysis of memory-based VOS is UNVERIFIED - needs lit search.
- **Minimal experiment:** Track rigid constant-scale objects (fixed camera) for 500+ frames, plot signed area and per-curvature-bin boundary offset vs time.
- **Main risk:** Bias might be dataset-specific (motion blur correlates with extremities), needs controlled rigid-object footage.

### W2-A-0030 - Distractor-swap probability in SAM2 is a logistic function of feature-space similarity between target and distractor - fit the curve.

- **Problem:** Identity switches to similar-looking instances are the canonical multi-object failure, but there is no quantitative model of when they happen.
- **Core hypothesis (falsifiable):** HYPOTHESIS: swap probability during a crossing event follows a logistic curve in embedding cosine similarity between target and distractor, with a threshold that is stable across videos - giving a predictive, per-scene identity-risk score computable before tracking.
- **Why important:** Predictive risk scoring for identity switches would let pipelines pre-allocate human checks in crowded scenes (cell tracking, sports, herds).
- **Why possibly novel:** A fitted psychometric-style swap curve for memory-based VOS is UNVERIFIED - needs lit search.
- **Minimal experiment:** Mine crossing events in MOSE/OVIS, log embedding similarity and swap outcome, fit and cross-validate the logistic.
- **Main risk:** Similarity measured with the model's own embedding may be circular; test external embeddings too.

### W2-A-0031 - SAM2 accuracy is non-monotonic in frame rate: temporal aliasing hurts fast periodic motion at intermediate fps.

- **Problem:** Everyone assumes more fps is better or at worst neutral. For periodic or oscillating motion, intermediate sampling may alias into confusing pseudo-motion.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for objects with periodic motion (wings, wheels, machinery), tracking quality vs frame rate has a dip where sampling aliases the motion (near integer ratios of motion period), recoverable by either higher fps or, counter-intuitively, lower fps.
- **Why important:** Frame-rate is a controllable deployment knob; a non-monotonic law changes how people configure cameras and subsample videos for annotation.
- **Why possibly novel:** Temporal-aliasing analysis of memory-based segmentation trackers is UNVERIFIED - needs lit search.
- **Minimal experiment:** High-fps source videos of periodic motion, subsample at many rates, plot J&F vs rate; look for aliasing dips at predicted ratios.
- **Main risk:** Effect may be confined to a narrow class of scenes; scope must be honest.

### W2-A-0032 - Memory poisoning: quantify how one corrupted frame propagates through SAM2's memory bank - is error injection sub- or super-linear?

- **Problem:** Robustness of memory-augmented trackers to single-frame corruption (glare, compression burst, occluder) is unmeasured; the memory could either dilute or amplify a bad write.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a single adversarially bad mask written to memory degrades subsequent frames super-linearly in time for ambiguous targets (self-reinforcing retrieval) but is diluted for distinctive targets - the bifurcation is predicted by target-distractor similarity.
- **Why important:** Determines whether memory needs write-gating/quarantine, and defines a concrete attack surface for safety-critical tracking.
- **Why possibly novel:** Error-injection response analysis of segmentation memory banks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Inject controlled mask corruptions at frame t, measure IoU trajectories after t vs matched controls across target types.
- **Main risk:** Injection method may not represent natural corruption; use both synthetic and natural (glare/blur) events.

### W2-A-0033 - Which frame you prompt matters more than how well you prompt it: middle-frame prompting beats first-frame in long videos.

- **Problem:** The universal convention prompts frame 0. Information-theoretically the best anchor frame is the one minimizing appearance distance to the rest of the video.
- **Core hypothesis (falsifiable):** HYPOTHESIS: prompting the medoid frame (closest to all others in feature space) improves whole-video J&F more than upgrading the frame-0 prompt from 1 click to a perfect mask - anchor selection dominates prompt quality beyond a video-length threshold.
- **Why important:** Zero-cost accuracy gains for every SAM2 pipeline, and reframes interactive video annotation as a frame-selection problem first.
- **Why possibly novel:** Anchor-frame optimality vs prompt-quality tradeoff quantification is UNVERIFIED - needs lit search.
- **Minimal experiment:** On LVOS/long videos, compare first-frame perfect-mask vs medoid-frame single-click prompting under matched budgets.
- **Main risk:** Medoid selection needs the whole video (offline only); streaming variant may lose the effect.

### W2-A-0034 - VOS metrics reward temporal smoothness, not correctness: an oracle temporal smoother improves J&F without new information.

- **Problem:** If post-hoc smoothing of masks (no access to images) improves benchmark scores, the metric partially measures smoothness style rather than segmentation quality.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a model-free temporal mask smoother (shape-consistent filtering of existing predictions) improves J&F on standard VOS benchmarks by a nontrivial margin for many methods, and method rankings change when evaluation adds unsmoothable per-frame probes - demonstrating metric gaming headroom.
- **Why important:** If rankings are partially smoothness rankings, years of architecture conclusions need re-reading; also a cheap test-time trick that should be disclosed.
- **Why possibly novel:** Smoothing-only ablation as a metric audit for VOS is UNVERIFIED - needs lit search.
- **Minimal experiment:** Apply temporal morphological smoothing to frozen predictions of 5 public methods, report J&F deltas and rank flips.
- **Main risk:** If gains are negligible the audit vindicates the metric (still worth publishing as a check).

### W2-A-0035 - Recency-based memory is provably wrong for periodic scenes: diversity-sampled memory should beat recency at equal size.

- **Problem:** SAM2-style memories favor recent frames. For periodic or revisiting content (orbiting views, back-and-forth motion), recency discards the most predictive exemplars.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at matched memory budget, exemplar selection by appearance-diversity (k-center over frame features) outperforms recency on videos with periodicity/revisits, while recency wins on smooth-drift videos - a measurable regime split that current fixed policies straddle badly.
- **Why important:** Identifies a principled scene-conditional memory policy question rather than a bigger-memory arms race.
- **Why possibly novel:** Regime-mapped comparison of memory selection policies in promptable video segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Reconfigure SAM2 memory selection at inference (no retraining) with diversity sampling; evaluate on periodic vs drift video subsets.
- **Main risk:** Inference-time policy swap without retraining may be off-manifold for the memory attention.

### W2-A-0036 - Does temporal context help or hurt on static camouflaged objects? SAM2 vs per-frame SAM on motionless targets.

- **Problem:** Temporal models are assumed to help always. For a static camouflaged animal, memory frames add no new information but may add noise accumulation.
- **Core hypothesis (falsifiable):** HYPOTHESIS: on static targets in moving-texture scenes (wind, water), SAM2's memory hurts relative to independent per-frame segmentation of the anchor mask, because background texture change is misread as object change - temporal context has a sign-flipping value depending on motion source.
- **Why important:** Establishes when video machinery should be bypassed - important for camouflage, surveillance, and medical cine where targets barely move.
- **Why possibly novel:** Signed value-of-temporal-context analysis conditioned on motion source is UNVERIFIED - needs lit search.
- **Minimal experiment:** MoCA-Mask static-segment subset: compare SAM2 propagation vs frozen anchor mask + per-frame refinement under matched prompts.
- **Main risk:** Truly static targets are rare in benchmarks; may need curated clips.

### W2-A-0037 - Topology-change events (splitting, merging, pouring) are an unhandled event class in video segmentation - build the taxonomy and measure failure.

- **Problem:** Masklets assume persistent object identity, but real objects split (dough, cells, liquids) and merge. What trackers do at these events is uncharacterized.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at split events, memory-based trackers deterministically follow the larger fragment (area-weighted attention), losing the smaller one at a rate predicted by fragment area ratio - a simple law that a fragment-aware evaluation would expose.
- **Why important:** Cell biology, cooking/robotics, and material handling all need split/merge tracking; knowing the default failure law is step one.
- **Why possibly novel:** An event-taxonomy benchmark for topology changes in VOS is UNVERIFIED - needs lit search.
- **Minimal experiment:** Curate 100 split events (cell videos, cutting food), measure which fragment retains identity vs area ratio.
- **Main risk:** Annotation ambiguity about which fragment 'is' the original; needs a convention.

### W2-A-0038 - Joint multi-object tracking in SAM2 degrades per-object accuracy vs independent runs: measure memory contention.

- **Problem:** SAM2 tracks multiple objects with shared compute/memory. Whether objects interfere (contention) or help (context) compared to isolated single-object runs is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-object J&F drops as tracked-object count rises even without spatial interaction, and the drop concentrates on objects sharing appearance clusters - evidence of representational contention in shared memory attention rather than mere occlusion effects.
- **Why important:** Determines scaling behavior for dense-instance video annotation and whether parallel independent runs (costly) are secretly necessary.
- **Why possibly novel:** Contention-vs-context decomposition with non-interacting object sets is UNVERIFIED - needs lit search.
- **Minimal experiment:** On multi-object videos, compare joint tracking vs one-object-at-a-time runs on identical prompts; stratify by pairwise similarity.
- **Main risk:** Implementation details (per-object memory in SAM2) may already isolate objects; verify against the actual architecture first (KNOWN: SAM2 keeps per-object state; contention could still arise via shared backbone resolution and NMS-like interactions).

### W2-A-0039 - Camera-zoom sequences reveal scale lag: memory features anchor to old object scale and delay mask growth.

- **Problem:** During zoom (optical or dolly), object scale changes smoothly, but memory frames encode stale scales. Scale-adaptation dynamics of memory trackers are unquantified.
- **Core hypothesis (falsifiable):** HYPOTHESIS: under monotonic zoom, SAM2 mask area lags true object area with a measurable time constant proportional to memory length, producing systematic under-segmentation during zoom-in and over-segmentation during zoom-out.
- **Why important:** Zoom is ubiquitous (broadcast, drones, microscopy autofocus); a signed predictable lag is correctable but only if characterized.
- **Why possibly novel:** Scale-lag time-constant measurement for memory trackers is UNVERIFIED - needs lit search.
- **Minimal experiment:** Synthesize exact-zoom sequences from high-res stills (crop pyramids), measure mask-area lag vs zoom rate and memory length.
- **Main risk:** Synthetic zoom lacks parallax; confirm on real dolly footage subset.
- **Mutated from:** W2-A-0029

### W2-A-0040 - Forward-backward tracking asymmetry as a free uncertainty signal: where the two directions disagree, the tracker is wrong.

- **Problem:** Tracking a video forward vs backward should ideally give the same masks; divergence indicates unreliability, but this self-consistency signal is not exploited or characterized for modern VOS.
- **Core hypothesis (falsifiable):** HYPOTHESIS: forward-backward mask disagreement per frame predicts actual error (AUROC>0.85) better than model confidence outputs, and the asymmetry is directional - errors accumulate on the direction that first encounters ambiguity - enabling label-free error localization in time.
- **Why important:** Gives annotation pipelines an automatic 'inspect here' signal, cutting human video-QA cost.
- **Why possibly novel:** Cycle-consistency is classic for optical flow (KNOWN); its calibration as an error detector for memory-based masklets is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run SAM2 both directions on DAVIS/MOSE from the same anchor, correlate disagreement with per-frame IoU error.
- **Main risk:** Backward tracking may fail identically on the same hard segments, blinding the signal exactly where needed.

### W2-A-0041 - Occlusion boundary ownership errors: SAM2 assigns the occluder's edge to the occluded object during partial occlusion.

- **Problem:** When object A passes in front of B, B's visible-region boundary is A's silhouette. Whether video segmenters represent this distinction (boundary ownership) is untested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: during partial occlusions, the tracker's boundary error on the shared edge is asymmetric - the occluded object's mask systematically 'sticks' to the occluder's silhouette even after separation begins (measurable hysteresis in boundary release), revealing absence of ownership representation.
- **Why important:** Boundary ownership is the core of amodal reasoning; a measurable hysteresis gives a concrete probe for whether models have any occlusion model at all.
- **Why possibly novel:** Boundary-release hysteresis as an amodal-representation probe is UNVERIFIED - needs lit search.
- **Minimal experiment:** Curate crossing events with GT, measure shared-edge error before/during/after separation, quantify release lag in frames.
- **Main risk:** Requires accurate GT at occlusion boundaries, the noisiest annotation region.

### W2-A-0042 - Micro-motion as a segmentation cue: can temporal aggregation segment objects invisible in any single frame (breathing, vibration)?

- **Problem:** Some objects are single-frame-invisible but reveal themselves through sub-pixel periodic motion. Current video segmenters aggregate over time yet nobody tests whether they exploit micro-motion.
- **Core hypothesis (falsifiable):** HYPOTHESIS: SAM2 and peers extract near-zero information from sub-pixel periodic motion (performance equals static-frame baseline), while an explicit temporal-amplification preprocessing (Eulerian-style) makes the same targets segmentable - locating a concrete representational gap between possible and actual temporal use.
- **Why important:** Defines an entire class of targets (hidden animals, machinery defects, breathing patients under blankets) where temporal information is the ONLY signal.
- **Why possibly novel:** Micro-motion segmentation as a benchmark task is UNVERIFIED - needs lit search; motion magnification itself is KNOWN (Wu et al., Eulerian Video Magnification).
- **Minimal experiment:** Collect/synthesize clips with sub-pixel oscillating targets, compare SAM2 vs SAM2-on-motion-amplified input.
- **Main risk:** Amplification also amplifies noise; careful SNR-controlled synthesis needed.

### W2-A-0043 - Once lost, always lost: quantify whether SAM2 failure is an absorbing state and what spontaneous recovery requires.

- **Problem:** Practitioners report that after a tracker loses its target, it rarely recovers without re-prompting, but recovery statistics have never been formalized.
- **Core hypothesis (falsifiable):** HYPOTHESIS: SAM2's per-frame recovery probability after a loss event is <5% and roughly constant (memoryless), so expected lost-time is geometric and long - and recovery events are almost exclusively triggered by the object re-entering high-similarity poses to memory exemplars, not by search behavior (the model has no search).
- **Why important:** Absorbing-state failure changes deployment math: the metric that matters is time-to-loss, not average IoU; also motivates re-detection modules with clear expected value.
- **Why possibly novel:** Survival-analysis treatment of masklet life/death/recovery is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run long videos (LVOS), detect loss events (IoU<0.1), fit survival and recovery hazard curves.
- **Main risk:** Loss definition threshold shapes conclusions; report sensitivity across thresholds.

### W2-A-0044 - Fit the memory-size vs drift power law: how much memory buys how much tracking longevity?

- **Problem:** Memory capacity is a compute knob without a published scaling relationship; teams size it by folklore.
- **Core hypothesis (falsifiable):** HYPOTHESIS: median time-to-loss scales as a power law in memory slots with exponent <1 (diminishing returns), and the exponent differs by scene type (crowded vs sparse), so optimal memory allocation is scene-conditional and mostly small.
- **Why important:** Turns an arbitrary hyperparameter into a budgeted engineering decision with published curves.
- **Why possibly novel:** Scaling-law methodology applied to tracking memory rather than model/data size is UNVERIFIED - needs lit search.
- **Minimal experiment:** Sweep memory configurations on LVOS/MOSE, fit time-to-loss curves per scene category.
- **Main risk:** Architecture may not expose memory size cleanly without retraining; may need the open-source variants.
- **Mutated from:** W2-A-0043

### W2-A-0045 - Equal-budget video annotation: sparse clicks on many frames beats a perfect mask on one frame.

- **Problem:** The standard video annotation protocol (dense mask on frame 0, then propagate) has never been tested against spreading the same human-time across the video as sparse corrections.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at matched human-seconds, K single-click corrections spread over the video outperform one dense frame-0 mask by a growing margin with video length, because temporal information (where drift happens) is worth more than spatial precision (pixel-perfect anchor).
- **Why important:** Could halve real-world video annotation cost with zero model changes - protocol science rather than architecture.
- **Why possibly novel:** Budget-matched protocol comparisons for video annotation are rare; UNVERIFIED - needs lit search.
- **Minimal experiment:** Simulate both protocols with timed human cost models on DAVIS/LVOS + SAM2, then a small real-annotator study (5 people).
- **Main risk:** Human time models for clicks vs masks vary; the real-annotator confirmation is essential.
- **Mutated from:** W2-A-0033

### W2-A-0046 - Ultrasound video breaks SAM2's memory attention because speckle decorrelates: modality-specific drift signature.

- **Problem:** SAM2 memory matches features across frames. Ultrasound speckle decorrelates within milliseconds while anatomy persists - the opposite statistics of natural video.
- **Core hypothesis (falsifiable):** HYPOTHESIS: SAM2 drift on ultrasound cine is dominated by speckle decorrelation (drift correlates with speckle decorrelation rate, not anatomical motion), so mild despeckling preprocessing improves tracking MORE than fine-tuning the model on ultrasound masks at matched effort.
- **Why important:** Ultrasound is the highest-volume medical video modality; identifying the true bottleneck (input statistics vs model weights) redirects adaptation effort.
- **Why possibly novel:** Attribution of medical-video tracking failure to speckle statistics vs anatomy is UNVERIFIED - needs lit search.
- **Minimal experiment:** On CAMUS/echo videos, correlate frame-pair feature similarity with speckle decorrelation; compare despeckled input vs LoRA-tuned model at matched cost.
- **Main risk:** Despeckling may destroy diagnostic boundaries; need boundary-quality co-evaluation.

### W2-A-0047 - Self-diagnosing drift onset: within-track feature statistics detect the exact frame where a masklet starts failing.

- **Problem:** Drift detection currently needs ground truth or human review. The track's own feature stream (memory attention entropy, mask-embedding velocity) may mark failure onset.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a change-point detector on the masklet's internal statistics localizes drift onset within +-5 frames for a majority of failures, without images or GT - failure has an internal signature preceding visible error.
- **Why important:** Automatic QA for large-scale video auto-annotation (SA-V style) - review only flagged spans instead of whole videos.
- **Why possibly novel:** Change-point analysis on tracker internals as self-diagnosis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Log internal statistics over DAVIS/MOSE runs, train change-point detector, evaluate onset localization against GT-derived failure times.
- **Main risk:** Gradual drifts may lack a change point; report by failure type.
- **Mutated from:** W2-A-0040

### W2-A-0048 - Shot-change as a natural memory-reset probe: what SAM2 retains across cuts tells us what its memory encodes.

- **Problem:** Across a hard cut, low-level correspondence dies but object identity may persist (same object, new view). SAM2 behavior at cuts is an untested window into memory content.
- **Core hypothesis (falsifiable):** HYPOTHESIS: SAM2 survival across cuts is predicted almost entirely by pose/scale similarity of the object across the cut and not by scene continuity, showing memory encodes object-centric appearance templates rather than scene context.
- **Why important:** Edited video (film, broadcast, social media) is most of watched video; cut robustness defines applicability, and the probe clarifies representation content.
- **Why possibly novel:** Using editing structure as a controlled representational probe is UNVERIFIED - needs lit search.
- **Minimal experiment:** Assemble cut pairs with graded object-pose and scene changes (from multi-view datasets), measure survival rates per condition.
- **Main risk:** SAM2 may fail at essentially all cuts, flattening the analysis (still a clean negative result).
- **Mutated from:** W2-A-0028

### W2-A-0049 - Sub-frame mask interpolation: do memory features support generating masks BETWEEN frames (temporal super-resolution)?

- **Problem:** Applications need masks at higher temporal rates than compute allows (or between saved keyframes). Whether tracker features interpolate linearly in time is unknown.
- **Core hypothesis (falsifiable):** HYPOTHESIS: interpolating SAM2 memory/mask embeddings between frames yields valid intermediate masks whose error grows sub-linearly with gap size for smooth motion - i.e. the learned representation is approximately temporally linear, enabling 4-10x cheaper video segmentation via keyframing + latent interpolation.
- **Why important:** Direct compute savings for video pipelines and a fundamental finding about temporal geometry of the learned space.
- **Why possibly novel:** Latent temporal interpolation for masklets is UNVERIFIED - needs lit search.
- **Minimal experiment:** On high-fps videos, decode masks from interpolated embeddings at held-out timestamps, compare vs true frames and vs mask-space (pixel) interpolation baselines.
- **Main risk:** Embedding space may be far from linear; pixel-space interpolation might trivially win.

### W2-A-0050 - Background persistence pollution: in fixed-camera streams, background objects entering memory create recurring false positives.

- **Problem:** Surveillance-style fixed cameras repeatedly show the same background structures; if any frame's mask leaks onto background, memory can immortalize the leak.
- **Core hypothesis (falsifiable):** HYPOTHESIS: in fixed-camera long streams, false-positive persistence (same wrong region recurring across frames) accounts for the majority of accumulated error - unlike moving-camera video where errors are transient - implying stationarity is a distinct and unmodeled failure regime for memory trackers.
- **Why important:** Fixed cameras dominate real deployments (traffic, retail, wildlife, factory QA) yet benchmarks are handheld/moving; a regime-specific error structure would show benchmarks mis-sample reality.
- **Why possibly novel:** Error-recurrence analysis conditioned on camera stationarity is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run SAM2 on fixed-camera datasets (VIRAT-like), measure spatial autocorrelation of errors over time vs handheld controls.
- **Main risk:** Fixed-camera GT for masks is scarce; may need semi-automatic GT with heavy review.
- **Mutated from:** W2-A-0032

## C03-medical-limits

### W2-A-0051 - Train on rater-disagreement-preserving labels instead of consensus: does keeping disagreement improve calibration more than it costs accuracy?

- **Problem:** Medical segmentation datasets collapse multiple expert opinions into one consensus mask, discarding the disagreement structure that encodes true ambiguity.
- **Core hypothesis (falsifiable):** HYPOTHESIS: models trained on the full rater distribution (sampling raters per example, not averaging) produce uncertainty maps that match held-out expert disagreement far better than consensus-trained models with post-hoc uncertainty, at <2 Dice cost - the disagreement is learnable signal, not noise.
- **Why important:** Clinical decisions need to know WHERE experts would disagree; consensus training makes models confidently arbitrary exactly there.
- **Why possibly novel:** Multi-rater modeling exists (KNOWN: probabilistic U-Net line of work); the specific calibration-vs-Dice tradeoff quantification against held-out raters across modalities is less established. UNVERIFIED - needs lit search.
- **Minimal experiment:** LIDC-IDRI (4 raters): train consensus vs rater-sampling models, evaluate uncertainty against held-out rater disagreement maps.
- **Main risk:** Rater identity confounds (systematic rater styles) may dominate genuine case ambiguity.

### W2-A-0052 - CT models secretly depend on window/level preprocessing conventions: randomized windowing collapses them, revealing intensity brittleness.

- **Problem:** CT pipelines bake in windowing presets (e.g. soft-tissue window). Models may learn the preset, not the anatomy, making them fragile to any acquisition/preprocessing change.
- **Core hypothesis (falsifiable):** HYPOTHESIS: state-of-the-art CT segmenters lose disproportionate Dice under clinically-plausible window/level perturbations (which preserve all diagnostic information a radiologist needs), and a model trained window-agnostic recovers the gap with no in-distribution cost - proving the fragility is a preprocessing artifact, not a capacity limit.
- **Why important:** Windowing varies across hospitals and PACS exports; this is a silent, ubiquitous deployment shift nobody benchmarks.
- **Why possibly novel:** Windowing as a formal domain-shift axis with an information-preservation argument is UNVERIFIED - needs lit search.
- **Minimal experiment:** Take 3 public CT models, sweep window/level within radiologically-valid ranges, plot degradation; retrain one with randomized windows.
- **Main risk:** Some windows genuinely destroy information for specific organs; must define validity ranges with a radiologist.

### W2-A-0053 - Slice-direction inconsistency of 2D models on 3D volumes scales with through-plane anisotropy: derive the consistency-spacing law.

- **Problem:** 2D slice-wise segmentation (including SAM-based) produces jagged 3D shapes. How inconsistency scales with slice spacing/anisotropy has not been formalized, so nobody knows when 2D is 'good enough'.
- **Core hypothesis (falsifiable):** HYPOTHESIS: inter-slice mask inconsistency grows linearly with slice spacing up to an organ-dependent correlation length, beyond which 2D and 3D models converge in quality - giving a per-organ spacing threshold that predicts when 3D context stops helping.
- **Why important:** Answers the perpetual 2D-vs-3D question with a measurable law instead of anecdote, guiding architecture choice per dataset.
- **Why possibly novel:** An explicit anatomical correlation-length framing of the 2D/3D tradeoff is UNVERIFIED - needs lit search.
- **Minimal experiment:** Downsample isotropic CT volumes to various spacings, train/evaluate matched 2D and 3D models, fit the crossover per organ.
- **Main risk:** Confounded by training-data volume differences between 2D slices and 3D patches; must match supervision bits.

### W2-A-0054 - MedSAM-style box prompting leaks organ-size priors: models segment the expected organ size, failing on pathological sizes.

- **Problem:** Box prompts encode expected extents. Medical models fine-tuned with GT boxes may learn organ-size priors that break precisely on the abnormal cases that matter clinically (atrophy, hypertrophy, tumors).
- **Core hypothesis (falsifiable):** HYPOTHESIS: MedSAM-style models' error grows sharply with an organ's deviation from population-median size (controlling for boundary difficulty), and prompting with deliberately wrong-size boxes drags predictions toward the box size - demonstrating prior leakage that inflates benchmark scores on normal anatomy while hiding failure on pathology.
- **Why important:** Clinical value concentrates in abnormal cases; a size prior is exactly the wrong inductive bias, and current benchmarks (mostly normal-ish anatomy) cannot see it.
- **Why possibly novel:** Size-deviation-stratified evaluation of promptable medical models is UNVERIFIED - needs lit search.
- **Minimal experiment:** Stratify public organ datasets by size percentile, plot Dice vs deviation; run wrong-box perturbation response curves.
- **Main risk:** Extreme sizes correlate with genuinely harder boundaries; needs matched-difficulty controls.
- **Mutated from:** W2-A-0004

### W2-A-0055 - Is ultrasound speckle noise or signal? Despeckling ablation to test whether models use speckle texture as anatomical cue.

- **Problem:** Speckle is treated as noise to be removed, but speckle statistics are tissue-dependent - models may rely on it as discriminative texture, in which case despeckling harms segmentation.
- **Core hypothesis (falsifiable):** HYPOTHESIS: segmentation models trained on raw ultrasound lose significant accuracy when tested on despeckled inputs (and vice versa), and per-tissue analysis shows speckle statistics carry class information comparable to boundary information for homogeneous organs - speckle is signal.
- **Why important:** Resolves a preprocessing controversy with direct consequences for every ultrasound pipeline and for cross-device generalization (speckle is device-dependent).
- **Why possibly novel:** Information-content quantification of speckle for segmentation (not detection/denoising) is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train/test 2x2 (raw/despeckled) on CAMUS + thyroid datasets; add a texture-only probe (boundary-masked patches) for class information.
- **Main risk:** Results may be despeckling-algorithm dependent; use 3 different filters.

### W2-A-0056 - Stain normalization in pathology helps less than stain-diverse training: an assumption audit with controlled compute.

- **Problem:** Stain normalization is near-universal in computational pathology, assumed necessary for cross-lab transfer. Modern augmentation/diverse pretraining may have made it redundant or harmful.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at matched compute, stain augmentation dominates stain normalization for cross-site segmentation transfer, and normalization actively destroys discriminative chromatic information for some tissue classes (measurable per-class sign flips).
- **Why important:** Normalization is a preprocessing tax on every pathology pipeline; if it is obsolete or harmful, the field should know. KNOWN: augmentation-vs-normalization comparisons exist in classification contexts; segmentation-specific and per-class sign analysis is UNVERIFIED - needs lit search.
- **Why possibly novel:** Per-class harm analysis of normalization for segmentation, rather than aggregate AUC comparisons.
- **Minimal experiment:** CAMELYON-derived segmentation with multi-site splits: 2x2 normalization/augmentation factorial at matched budgets.
- **Main risk:** Conclusions may not transfer across stain types (H&E vs IHC); scope both.

### W2-A-0057 - Text-report-derived weak labels vs 5 minutes of scribbles: the annotation-economics showdown for medical segmentation.

- **Problem:** Two weak-supervision currencies compete - mining radiology reports (free but noisy/indirect) vs minimal expert scribbles (costly but spatial). Their exchange rate has never been measured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per unit of final Dice, expert scribble-seconds outperform report-derived labels by an order of magnitude for spatially-precise structures, but report labels win for presence/coverage of diffuse pathology - the modality of weak supervision must match the spatial statistics of the target.
- **Why important:** Hospitals sit on millions of reports; knowing when they are worth mining vs when to just pay for scribbles is a real resource-allocation question.
- **Why possibly novel:** A quantified exchange rate between supervision types under matched outcomes is UNVERIFIED - needs lit search.
- **Minimal experiment:** On a chest CT dataset with reports, train (a) report-mined weak labels, (b) budget-matched scribbles, (c) mixtures; compare Dice-per-dollar curves.
- **Main risk:** Report-mining quality depends heavily on NLP extraction quality, a moving target.

### W2-A-0058 - Tumor boundary uncertainty is directionally structured (infiltration axes); isotropic uncertainty models are wrong in a measurable way.

- **Problem:** Infiltrative tumors grow along anatomical corridors (white-matter tracts, tissue planes), so true boundary ambiguity is anisotropic - but every uncertainty method outputs isotropic per-pixel variance.
- **Core hypothesis (falsifiable):** HYPOTHESIS: held-out multi-rater disagreement on glioma boundaries is significantly anisotropic (aligned with local tissue orientation), and current uncertainty methods' outputs are near-isotropic - a representational mismatch that directional evaluation will expose and that matters for radiotherapy margins.
- **Why important:** Radiotherapy margin expansion is currently isotropic partly because tools are; demonstrating structured anisotropy could change margin design.
- **Why possibly novel:** Directional decomposition of segmentation uncertainty against anatomical orientation fields is UNVERIFIED - needs lit search.
- **Minimal experiment:** BraTS-style multi-rater subset + DTI atlas orientations: measure disagreement anisotropy; compare uncertainty-method outputs directionally.
- **Main risk:** Multi-rater glioma data with enough raters is scarce; may need to commission a small re-annotation.

### W2-A-0059 - Longitudinal self-supervision: same-patient scan pairs give free consistency labels that beat generic pretraining for segmentation.

- **Problem:** Hospitals have massive longitudinal archives (same patient, months apart) that are unused for pretraining; stable anatomy between visits is a free correspondence signal stronger than augmentation-based SSL.
- **Core hypothesis (falsifiable):** HYPOTHESIS: pretraining with cross-visit anatomical correspondence objectives (predicting stable vs changed regions without registration GT) transfers to downstream segmentation better than in-modality SimCLR/MAE at matched data and compute, especially for small-structure Dice.
- **Why important:** Uses data hospitals already have with zero extra annotation; targets the medical-specific structure (longitudinal stability) generic SSL ignores.
- **Why possibly novel:** Longitudinal-pair pretraining for dense medical tasks appears under-explored. UNVERIFIED - needs lit search.
- **Minimal experiment:** Assemble public longitudinal MRI (ADNI/OASIS), pretrain correspondence vs MAE at matched compute, fine-tune on hippocampus/lesion segmentation.
- **Main risk:** Registration shortcuts could let the model cheat; objective design must prevent trivial solutions.

### W2-A-0060 - Partial-label multi-dataset training silently teaches 'organ X is background': quantify negative-transfer from unlabeled structures.

- **Problem:** Combining datasets where each labels different organs means every dataset actively teaches that other organs are background - a contradiction that everyone works around ad hoc.
- **Core hypothesis (falsifiable):** HYPOTHESIS: naive multi-dataset training suppresses each organ's recall proportionally to how often it appears unlabeled in partner datasets (a measurable dose-response 'background poisoning' curve), and the effect size exceeds architecture-choice effects in typical setups.
- **Why important:** Multi-dataset training is how everyone scales medical models now; an unmeasured poisoning law means the ecosystem's scaling curves are bent by label sociology, not learning capacity.
- **Why possibly novel:** KNOWN: partial-label learning methods exist (e.g. marginal losses); the quantified dose-response poisoning law is UNVERIFIED - needs lit search.
- **Minimal experiment:** Controlled mixes of 3 abdominal datasets with disjoint labels; vary the fraction of poisoning images per organ, fit recall vs poisoning-dose.
- **Main risk:** Effect confounds with dataset appearance shift; use single-source synthetic label-hiding as the clean control.

### W2-A-0061 - Vessel and airway models optimize Dice but break topology: measure the Dice-topology Pareto frontier and show current models sit at its wrong end.

- **Problem:** For tubular structures, a 1-voxel break destroys downstream use (flow simulation, navigation) while barely moving Dice; the field optimizes and reports the wrong quantity.
- **Core hypothesis (falsifiable):** HYPOTHESIS: across public vessel/airway models, topology error (Betti number mismatch, broken-branch count) is nearly uncorrelated with Dice above Dice=0.8, and models selected by validation Dice are strictly dominated on the topology axis by differently-selected checkpoints of the SAME training run - the problem is checkpoint selection, not capacity.
- **Why important:** If correct, large topology gains are available for free (different model selection), and benchmark rankings for tubular tasks are misleading.
- **Why possibly novel:** KNOWN: clDice and topology losses exist; the checkpoint-selection reframing (topology is lost at selection time, not training time) is UNVERIFIED - needs lit search.
- **Minimal experiment:** Retrain a standard vessel model, log Dice and topology metrics for ALL checkpoints, test whether topology-selected checkpoints dominate.
- **Main risk:** May be true only near convergence for specific architectures; test 3 architectures.

### W2-A-0062 - Find the through-plane spacing threshold where 3D convolution stops beating 2D - a reusable crossover law for the field.

- **Problem:** Whether to use 2D, 2.5D, or 3D models is re-litigated in every medical paper without a governing quantitative rule.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the 3D-over-2D Dice advantage decays monotonically with slice spacing normalized by structure diameter, crossing zero near spacing~0.5x structure diameter, consistently across organs and modalities - a dimensionless law that predicts the right architecture from dataset metadata alone.
- **Why important:** Would eliminate a whole genre of redundant ablation studies and guide architecture choice from acquisition parameters.
- **Why possibly novel:** Dimensionless scaling analysis (spacing/diameter) for the 2D-3D question is UNVERIFIED - needs lit search.
- **Minimal experiment:** Resample 5 isotropic datasets to a spacing grid, train matched 2D/3D models, fit the crossover in dimensionless units.
- **Main risk:** Anisotropic acquisition artifacts (slice profile, gap) differ from clean downsampling; validate on natively anisotropic data.
- **Mutated from:** W2-A-0053

### W2-A-0063 - Annotation fatigue leaves order signatures in public medical datasets: label quality drifts within annotation sessions and is detectable post hoc.

- **Problem:** Medical labels are made by humans in long sessions; fatigue and drift should leave statistical traces (boundary quality vs slice index / case order), but no one audits datasets for it.
- **Core hypothesis (falsifiable):** HYPOTHESIS: in public volumetric datasets, boundary smoothness and model-vs-label disagreement vary systematically with slice order within volumes (start vs end of stacks) and with case ID order, revealing session-position effects large enough to bias per-region evaluation (e.g. organ ends are labeled worse).
- **Why important:** If label quality is spatially/temporally structured, benchmark errors attributed to models are partly annotation fatigue - affecting especially the apex/base slices clinicians care about.
- **Why possibly novel:** Forensic fatigue analysis of existing datasets (no new labels needed) is UNVERIFIED - needs lit search.
- **Minimal experiment:** For 5 public datasets, regress label-quality proxies (curvature statistics, inter-slice coherence, model consensus disagreement) on slice position and case order.
- **Main risk:** Proxies for 'label quality' without re-annotation are indirect; commission spot re-annotations for validation.

### W2-A-0064 - Low-level statistics distance (power spectrum, noise model) predicts MedSAM transfer failure better than semantic/anatomical distance.

- **Problem:** Foundation medical models fail unpredictably on new modalities/protocols. The community assumes semantic novelty drives failure; it may be mundane signal statistics.
- **Core hypothesis (falsifiable):** HYPOTHESIS: transfer performance of promptable medical models across 20+ dataset pairs is predicted (r>0.7) by low-level statistics divergence (radially-averaged power spectra, noise floor, intensity histogram transport cost) and only weakly by anatomy/modality labels - most 'domain gap' is signal-processing gap.
- **Why important:** A cheap pre-deployment compatibility test from unlabeled images, plus redirection of adaptation research toward signal harmonization.
- **Why possibly novel:** Systematic low-level-vs-semantic attribution of medical transfer failure is UNVERIFIED - needs lit search.
- **Minimal experiment:** Evaluate MedSAM/SAM across the modality grid of public datasets, regress performance drops on statistics divergences vs semantic dummies.
- **Main risk:** Low-level and semantic distances correlate across natural dataset pairs; needs synthetic-perturbation legs to break the confound.

### W2-A-0065 - Clinician clicks differ from simulated clicks: measure the sim2real prompting gap that inflates interactive medical benchmarks.

- **Problem:** Interactive medical segmentation is evaluated with simulated prompts (center-of-error clicks). Real clinicians click based on anatomical salience and diagnostic habit, not error geometry.
- **Core hypothesis (falsifiable):** HYPOTHESIS: real clinician click distributions differ measurably from simulators (clicks favor anatomically meaningful landmarks and avoid ambiguous tissue), and evaluating with real click traces drops reported model performance by a clinically meaningful margin, reordering methods - simulator choice is a hidden hyperparameter of the entire subfield.
- **Why important:** If benchmark rankings do not survive real users, the field is optimizing simulator-fit; protocols must change before clinical deployment claims.
- **Why possibly novel:** Collected clinician-click corpora for evaluation replay are rare/absent. UNVERIFIED - needs lit search.
- **Minimal experiment:** Record 3 clinicians x 100 cases of real interactive use, replay traces against 4 models, compare with simulator-based rankings.
- **Main risk:** Small-N clinician study; click styles may vary more between clinicians than between simulators (itself a finding).

### W2-A-0066 - Contrast-polarity invariance test: can one model segment T1 and T2 (inverted tissue contrast) without contrast-specific features, and what does it cost?

- **Problem:** MRI sequences flip which tissue is bright. Models either specialize per sequence or are claimed 'sequence-agnostic' without a controlled test of what invariance costs.
- **Core hypothesis (falsifiable):** HYPOTHESIS: enforcing polarity invariance (training with random contrast inversions consistent with tissue physics) costs little on seen sequences but roughly doubles zero-shot transfer to unseen sequences - i.e. most cross-sequence failure is polarity/contrast coding, a low-dimensional and fixable factor, not anatomy understanding.
- **Why important:** Sequence proliferation is the main practical obstacle to universal MRI models; identifying the failure as low-dimensional makes it tractable.
- **Why possibly novel:** Physics-consistent contrast-inversion invariance analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train on T1 with physics-based contrast remapping augmentation, test zero-shot on T2/FLAIR; compare against multi-sequence-trained upper bound.
- **Main risk:** Some pathologies are only visible in specific sequences; invariance may erase pathology signal - stratify by lesion visibility.

### W2-A-0067 - Below a lesion-size threshold, segmentation-first pipelines beat detection-first: locate the crossover.

- **Problem:** Tiny lesion pipelines either detect-then-segment or segment-then-group. Which paradigm wins at which size regime is undocumented, so teams choose by habit.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-lesion recall of detection-first pipelines collapses below a size threshold (relative to receptive-field stride) where dense segmentation-first retains sensitivity, producing a crossover point measurable in voxels that generalizes across modalities when normalized by resolution.
- **Why important:** Metastasis screening and microbleed detection live exactly in the tiny regime; the field needs the regime map.
- **Why possibly novel:** Head-to-head paradigm comparison stratified by object size in physical units is UNVERIFIED - needs lit search.
- **Minimal experiment:** On microbleed/metastasis datasets, run matched detection-first and segmentation-first pipelines, plot per-lesion recall vs size.
- **Main risk:** Implementation quality asymmetry between paradigms could masquerade as a paradigm effect; use strong tuned baselines for both.

### W2-A-0068 - Extreme class imbalance has a phase transition: below a foreground-fraction threshold, per-lesion recall decouples from Dice and both metrics stop constraining each other.

- **Problem:** At foreground fractions below ~0.1%, standard metrics and training dynamics enter a regime the field treats with the same tools as moderate imbalance; whether this regime is qualitatively different is untested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: as foreground fraction decreases, there is a measurable transition where (a) the correlation between Dice and per-lesion recall across checkpoints drops toward zero, and (b) training becomes bimodal (models either find lesions or ignore them entirely, seed-dependent) - a phase structure implying different evaluation and early-stopping rules are needed in the extreme regime.
- **Why important:** Screening applications live in the extreme regime; if metric decoupling and seed-bimodality are real, current papers' single-seed Dice claims there are close to meaningless.
- **Why possibly novel:** Phase-transition framing with checkpoint-level correlation analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Synthetic imbalance ladder (subsample lesion voxels progressively), train 10 seeds per level, measure metric decoupling and outcome bimodality.
- **Main risk:** Transition may be gradual, not sharp - report as regime change rather than critical point if so.

### W2-A-0069 - Simulate cross-vendor MRI shift from k-space physics and test how much of the real vendor gap physics-only augmentation closes.

- **Problem:** Cross-vendor generalization is attacked with generic augmentation or adaptation, but vendor differences are substantially physics (k-space filtering, coil combination, reconstruction) that can be forward-simulated.
- **Core hypothesis (falsifiable):** HYPOTHESIS: augmenting a single-vendor training set with physics-simulated vendor transforms closes >60% of the measured cross-vendor Dice gap, and the residual gap localizes to protocol (not reconstruction) differences - decomposing 'vendor shift' into simulable and non-simulable parts.
- **Why important:** Would replace data-hungry multi-vendor collection with physics simulation for a large fraction of the problem, and produce the first quantitative decomposition of vendor shift.
- **Why possibly novel:** KNOWN: MRI physics augmentation exists in reconstruction literature; the segmentation-gap decomposition claim is UNVERIFIED - needs lit search.
- **Minimal experiment:** Use multi-vendor brain datasets, implement k-space filter/noise/bias-field simulation, measure gap closure per component.
- **Main risk:** Faithful vendor simulation requires proprietary details; approximate simulation may cap the closure fraction for reasons unrelated to the hypothesis.

### W2-A-0070 - Probe-pressure deformation is the dominant unmodeled augmentation for ultrasound: geometric, physics-parameterized, and testable.

- **Problem:** Ultrasound anatomy deforms under operator probe pressure. No standard augmentation models this; models may fail across operators simply due to compression states.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a biomechanically-plausible compression augmentation (depth-dependent anisotropic strain) improves cross-operator segmentation transfer more than any standard photometric/geometric augmentation at matched strength, because compression is the leading axis of real operator variation.
- **Why important:** Operator dependence is ultrasound's defining weakness; naming and modeling its main geometric factor would be broadly reusable.
- **Why possibly novel:** Compression-specific augmentation validated on cross-operator splits is UNVERIFIED - needs lit search.
- **Minimal experiment:** Datasets with repeated sweeps by different operators (or phantom studies): augmentation ablation over cross-operator splits.
- **Main risk:** Cross-operator datasets are scarce; a phantom + small clinical validation may be the only path.

### W2-A-0071 - Benchmarks reporting Dice above the inter-rater ceiling are fitting annotator style: audit which medical leaderboards have crossed their own noise floor.

- **Problem:** Each dataset has a Dice ceiling given by expert-vs-expert agreement. Leaderboard scores near or above single-rater agreement indicate style overfitting, not superhuman accuracy - but ceilings are rarely computed or compared.
- **Core hypothesis (falsifiable):** HYPOTHESIS: several prominent medical segmentation leaderboards have SOTA scores within noise of (or above) the inter-rater ceiling for their structure types, and the models' residual 'errors' correlate with rater-style dimensions rather than anatomy - meaning further leaderboard progress there is epistemically empty.
- **Why important:** Redirects effort away from saturated benchmarks and toward datasets/metrics with real headroom; protects clinical claims from style-fitting artifacts.
- **Why possibly novel:** Cross-benchmark systematic ceiling audit is UNVERIFIED - needs lit search (individual inter-rater studies are KNOWN).
- **Minimal experiment:** Collect published inter-rater figures per structure, compare with leaderboard SOTA; for 2 datasets, commission small re-rating to measure style-vs-anatomy error decomposition.
- **Main risk:** Published inter-rater numbers use varying protocols; harmonization needed before comparison.

### W2-A-0072 - Anatomy-relative coordinates transfer prompts across patients: one expert prompt reused on a thousand scans.

- **Problem:** Promptable models need per-image prompts. In medical imaging, anatomy provides a shared coordinate system that could let one prompt (defined relative to landmarks) transfer across patients - turning interactive into automatic segmentation.
- **Core hypothesis (falsifiable):** HYPOTHESIS: prompts expressed in anatomy-normalized coordinates (via cheap landmark detection, no deformable registration) retain >90% of per-patient manual-prompt Dice on organs with stable topology, and the transfer failure cases are exactly the clinically abnormal anatomies - making prompt-transfer failure itself an anomaly detector.
- **Why important:** Amortizes expert interaction across cohorts (huge for population studies), and the failure-as-anomaly-signal is a free second product.
- **Why possibly novel:** Prompt-space anatomical normalization (rather than image registration) is UNVERIFIED - needs lit search.
- **Minimal experiment:** Abdominal CT cohort: define prompts on 5 template patients, transfer via landmark alignment, measure retained Dice and abnormality enrichment among failures.
- **Main risk:** Landmark detectors fail on the same abnormal cases, entangling the anomaly signal.

### W2-A-0073 - Site fingerprints in federated medical segmentation: features encode hospital identity, and removing it costs accuracy - measure the privacy-performance coupling.

- **Problem:** Features of medical segmentation models may encode acquisition-site identity (scanner, protocol), which is simultaneously a privacy leak, a shortcut-learning risk, and possibly useful signal. The three roles have not been jointly quantified.
- **Core hypothesis (falsifiable):** HYPOTHESIS: site identity is linearly decodable from mid-level features of standard models with high accuracy; enforcing site-invariance degrades in-site accuracy only marginally but improves cross-site transfer - i.e. the site code is mostly shortcut, not signal, and its removal is nearly free.
- **Why important:** Directly informs federated learning design and shortcut mitigation in the setting where regulatory stakes are highest.
- **Why possibly novel:** KNOWN: site effects in radiomics are documented; the joint decodability-invariance-transfer quantification for segmentation features is UNVERIFIED - needs lit search.
- **Minimal experiment:** Multi-site public data (e.g. multi-site prostate MRI): site probes on features, invariance-constrained retraining, transfer matrix comparison.
- **Main risk:** Site correlates with population case-mix; invariance may remove genuine epidemiological signal - needs case-mix controls.

### W2-A-0074 - Volume measurements inherit uncalibrated uncertainty from segmentation: are downstream tumor-volume confidence intervals valid even when masks look good?

- **Problem:** Clinical endpoints are derived quantities (volumes, diameters), yet uncertainty is evaluated at pixel level. Pixel-calibrated models can still yield badly mis-calibrated volume estimates because errors are spatially correlated.
- **Core hypothesis (falsifiable):** HYPOTHESIS: volume confidence intervals derived from per-pixel uncertainties are anti-conservative by large factors (2-5x too narrow) because pixel errors are positively correlated along boundaries, and a boundary-correlation-aware propagation restores near-nominal coverage without changing the model.
- **Why important:** RECIST-style measurements drive treatment decisions; invalid CIs are a direct clinical safety issue that pixel metrics cannot reveal.
- **Why possibly novel:** Coverage analysis of derived clinical quantities from segmentation uncertainty is UNVERIFIED - needs lit search.
- **Minimal experiment:** Multi-rater lesion datasets: compare nominal vs empirical coverage of volume CIs across uncertainty methods; measure boundary error correlation lengths.
- **Main risk:** Multi-rater 'true volume' is itself uncertain; use synthetic lesions with exact GT as the anchor condition.

### W2-A-0075 - Consensus fusion (STAPLE-style) systematically erases minority-expert detections that are disproportionately correct on rare pathologies.

- **Problem:** Multi-rater fusion assumes the majority is right. For rare or subtle findings, the specialist minority may carry the correct signal, and consensus training deletes it.
- **Core hypothesis (falsifiable):** HYPOTHESIS: on cases with confirmed outcomes (pathology/follow-up), regions flagged by exactly one expert (majority-rejected) contain true findings at a rate far above chance and concentrated in rare disease subtypes - so consensus-trained models are structurally biased against the rare cases that matter most, in a measurable, outcome-anchored way.
- **Why important:** Challenges the default label-fusion practice for the exact case class (rare, subtle) where AI assistance is most valuable.
- **Why possibly novel:** Outcome-anchored audit of minority-rater regions is UNVERIFIED - needs lit search.
- **Minimal experiment:** Dataset with rater annotations + outcome verification (e.g. screening cohorts with follow-up): measure precision of minority-only regions vs chance.
- **Main risk:** Outcome-linked multi-rater datasets are rare and access-restricted; may require collaboration for data.
- **Mutated from:** W2-A-0051

## C04-amorphous-smoke-fire

### W2-A-0076 - Smoke has no true binary boundary: model rankings on smoke benchmarks flip when evaluated against density (alpha) labels instead of binary masks.

- **Problem:** Smoke segmentation benchmarks use binary masks over a physically continuous density field; annotator thresholds are arbitrary, so benchmarks may rank annotator-style-matching, not smoke understanding.
- **Core hypothesis (falsifiable):** HYPOTHESIS: inter-annotator agreement on smoke binary masks is lower than model-model agreement (benchmarks measure style), and re-evaluating existing models against soft density references (from synthetic smoke composites with known alpha) produces materially different rankings.
- **Why important:** If rankings are unstable under label formulation, published progress in smoke segmentation is partly an artifact - and safety systems are being selected on the wrong criterion.
- **Why possibly novel:** Density-referenced re-evaluation of binary smoke benchmarks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Composite real smoke plumes (alpha known from studio capture or simulation) onto scenes; evaluate public smoke models against binary vs alpha references; run a 5-annotator agreement study on 100 frames.
- **Main risk:** Synthetic composites may not represent real smoke edge statistics; include a small real multi-annotator set.

### W2-A-0077 - Reformulate smoke segmentation as alpha-matte regression: binary masks impose a measurable performance ceiling.

- **Problem:** Binary segmentation of translucent media discards the concentration information that downstream users (fire response, emissions monitoring) actually need.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a density-regression formulation trained on composited data with true alpha outperforms binary-mask models even when both are evaluated on the binary task (thresholded density beats direct binary prediction), because the continuous target regularizes the ill-posed boundary - falsifiable by direct comparison.
- **Why important:** Would show binary supervision is not just lossy for users but actively harmful for learning on translucent classes.
- **Why possibly novel:** KNOWN: matting exists as a field; the claim that regression supervision dominates binary supervision ON the binary metric for smoke is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train matched models (same backbone/budget) with binary vs alpha supervision on composited smoke, evaluate both on binary IoU + downstream density error.
- **Main risk:** Compositing realism gap; validate on held-out real annotated smoke.
- **Mutated from:** W2-A-0076

### W2-A-0078 - Fire segmentation models exploit sensor blooming and saturation artifacts, so they collapse across cameras: quantify the artifact reliance.

- **Problem:** Fire is a light emitter that saturates sensors, causing blooming/streaks that are camera-specific. Models may key on these artifacts rather than fire appearance, predicting cross-camera fragility.
- **Core hypothesis (falsifiable):** HYPOTHESIS: masking saturated pixels and blooming halos at test time degrades fire-segmentation models far more than masking equal-area random regions, and cross-camera transfer loss correlates with inter-camera differences in saturation behavior - most 'fire recognition' is sensor-artifact recognition.
- **Why important:** Fire detection is deployed across wildly heterogeneous cameras; artifact reliance would explain field failures that benchmarks never show.
- **Why possibly novel:** Artifact-reliance decomposition for emissive phenomena is UNVERIFIED - needs lit search.
- **Minimal experiment:** Occlusion-based attribution on saturation regions across 3 fire datasets; cross-camera evaluation where saturation statistics are matched vs mismatched.
- **Main risk:** Saturation is also genuine signal (fires do saturate); the question is reliance degree - needs careful counterfactuals with HDR captures.

### W2-A-0079 - Fire flicker has a characteristic temporal frequency signature: a 1-second temporal window beats any single-frame architecture at matched compute.

- **Problem:** Flame combustion produces documented flicker (~1-15 Hz region, KNOWN from combustion literature). Whether video fire segmentation actually needs or uses this cue is untested against strong single-frame baselines.
- **Core hypothesis (falsifiable):** HYPOTHESIS: adding a short temporal window with explicit frequency-band features improves fire/no-fire pixel discrimination against hard negatives (sunsets, reflective orange surfaces, foliage in wind) more than scaling the single-frame model by the equivalent compute - temporal spectrum is the discriminative axis, not appearance.
- **Why important:** Hard negatives are the practical fire-alarm problem (false positives); a physically-grounded cue that separates them is directly deployable.
- **Why possibly novel:** Frequency-domain evaluation against curated hard negatives at matched compute is UNVERIFIED - needs lit search.
- **Minimal experiment:** Assemble hard-negative video set (sunsets, brake lights, reflections), compare single-frame vs temporal-spectral models at matched FLOPs.
- **Main risk:** Camera compression may destroy flicker at typical bitrates - itself an important deployment finding.

### W2-A-0080 - Smoke-vs-cloud/fog discrimination is context-borne, not appearance-borne: source-region occlusion collapses model accuracy.

- **Problem:** Smoke, cloud, and fog patches can be locally indistinguishable; humans disambiguate by source attribution (rising from a point) and context. What information models actually use is unknown.
- **Core hypothesis (falsifiable):** HYPOTHESIS: occluding the plume's source region (bottom of plume, fire location) reduces smoke-vs-cloud discrimination accuracy to near chance for current models, showing classification is source-context-based, while texture-only patches carry <20% of the decision information - a measurable information decomposition.
- **Why important:** Determines minimum viable input context for wildfire early-warning crops/tiles - a deployed-system design constraint derived from science.
- **Why possibly novel:** Context-vs-texture information decomposition for atmospheric classes is UNVERIFIED - needs lit search.
- **Minimal experiment:** Patch-occlusion and crop-size sweeps on smoke/cloud datasets; report accuracy vs available context radius.
- **Main risk:** Dataset biases (smoke images differ from cloud images in irrelevant ways) can inflate texture-only accuracy; control with matched-scene pairs.

### W2-A-0081 - Optical-flow divergence detects smoke before appearance does: advection physics as a detection signal for incipient smoke.

- **Problem:** Early smoke is nearly transparent - appearance models fail at exactly the high-value moment. But smoke's motion field (expanding, buoyant, divergent) differs from scene motion from the very first frames.
- **Core hypothesis (falsifiable):** HYPOTHESIS: divergence/curl statistics of dense optical flow in smoke regions differ measurably from all common scene motions (foliage, water, crowds) even at contrast levels where appearance models are at chance, moving time-to-detection earlier by a measurable margin on ignition videos.
- **Why important:** Time-to-detection is THE metric for wildfire monitoring; a physics-grounded earliness gain matters more than IoU gains.
- **Why possibly novel:** Flow-topology (divergence) statistics as an early smoke feature, evaluated on time-to-detect, is UNVERIFIED - needs lit search.
- **Minimal experiment:** On ignition-time videos (controlled burns), plot detection latency of flow-based vs appearance-based signals at matched false-positive rates.
- **Main risk:** Optical flow is noisy exactly at low contrast; may need long temporal integration that erodes the earliness advantage.

### W2-A-0082 - Measure the annotator alpha-threshold distribution: at what transparency do humans stop labeling smoke, and how much benchmark variance does it explain?

- **Problem:** Every smoke/fog annotation implicitly chooses a transparency cutoff. The distribution of these cutoffs across annotators and datasets has never been measured, though it defines what the labels mean.
- **Core hypothesis (falsifiable):** HYPOTHESIS: annotator alpha cutoffs vary widely (roughly 2x range in implied alpha) across individuals and datasets, and this single scalar explains the majority of inter-dataset label inconsistency for translucent classes - cutting cross-dataset training gains when unharmonized.
- **Why important:** Provides the missing calibration constant for merging translucent-class datasets, and a general method for auditing implicit label thresholds.
- **Why possibly novel:** Psychophysical measurement of implicit annotation thresholds is UNVERIFIED - needs lit search.
- **Minimal experiment:** Show annotators composited smoke with known alpha ramps, elicit boundaries, estimate individual cutoffs; compare dataset-level implied cutoffs via composite probes.
- **Main risk:** Cutoffs may be context-dependent (background luminance), making the scalar model too simple - the richer model is still measurable.
- **Mutated from:** W2-A-0076

### W2-A-0083 - Synthetic-fog robustness does not transfer to real fog because real fog is heterogeneous: quantify the homogeneity gap.

- **Problem:** Fog robustness is benchmarked with homogeneous Koschmieder-model synthetic fog (KNOWN: standard in robustness suites). Real fog has patchiness, depth-correlated density, and scattering halos.
- **Core hypothesis (falsifiable):** HYPOTHESIS: models hardened on homogeneous synthetic fog gain little or nothing on real fog scenes (transfer coefficient <30%), and the residual failure correlates with fog spatial heterogeneity statistics - synthetic-fog benchmarks systematically overstate robustness progress.
- **Why important:** Autonomous-driving robustness claims rest partly on synthetic corruption suites; a measured transfer coefficient recalibrates those claims.
- **Why possibly novel:** Direct synthetic-to-real fog transfer measurement for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train/harden on synthetic fog ladders, evaluate on real foggy datasets (ACDC fog split), regress residual error on measured heterogeneity indices.
- **Main risk:** Real-fog GT is limited; heterogeneity indices from single images are approximate.

### W2-A-0084 - Background luminance flips smoke difficulty: dark-smoke-on-sky vs light-smoke-on-ground asymmetry as an untested dataset bias.

- **Problem:** Smoke visibility depends on the sign of contrast with background (scattering vs shadowing regimes). Datasets may over-sample one regime, biasing models trained on them.
- **Core hypothesis (falsifiable):** HYPOTHESIS: public smoke datasets are dominated by positive-contrast configurations (bright smoke against dark ground or dark smoke against bright sky in fixed proportions), and model performance collapses on the under-represented contrast-sign regime - a bias measurable and correctable via regime-stratified evaluation.
- **Why important:** Wildfire cameras see both regimes daily (sun angle changes); a hidden regime bias means diurnal reliability swings in deployment.
- **Why possibly novel:** Contrast-sign regime analysis for translucent classes is UNVERIFIED - needs lit search.
- **Minimal experiment:** Auto-classify contrast regimes in 4 smoke datasets, report regime distributions and per-regime model performance.
- **Main risk:** Regime auto-classification itself needs validation; start with manual labeling of a subset.

### W2-A-0085 - Smoke shadows are systematically mislabeled as smoke in aerial datasets: an audit with atmospheric-geometry verification.

- **Problem:** From aerial/satellite view, dense smoke casts dark shadows displaced by sun angle; annotators plausibly include shadows in smoke masks. Nobody has audited for this confusion.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a geometrically verifiable fraction (sun-angle-consistent displacement) of 'smoke' pixels in public aerial smoke datasets are actually shadow, and models trained on them systematically over-segment in the shadow direction - a directional error signature reproducible from sun metadata.
- **Why important:** Burned-area and plume-volume estimates feed emissions science; a shadow contamination bias propagates into climate-relevant numbers.
- **Why possibly novel:** Sun-geometry forensic auditing of smoke annotations is UNVERIFIED - needs lit search.
- **Minimal experiment:** For datasets with timestamps/geolocation, compute sun vectors, test whether label boundaries show sun-aligned asymmetry vs plume physics.
- **Main risk:** Smoke and its shadow genuinely overlap when viewed off-nadir; geometry must handle view angle carefully.

### W2-A-0086 - Rain streak and snowflake segmentation depends on exposure time, not weather intensity: the shutter-speed confound in weather datasets.

- **Problem:** The image of falling precipitation is determined jointly by physical rate and camera shutter speed (streak length ~ exposure). Datasets ignore shutter metadata, confounding weather severity with camera settings.
- **Core hypothesis (falsifiable):** HYPOTHESIS: model performance and even class definition ('rain streak' vs 'rain fog') vary more with exposure-time differences than with actual precipitation-rate differences at matched rates - weather segmentation datasets encode camera physics as much as meteorology.
- **Why important:** Weather robustness claims should transfer across cameras; if not, deployed reliability varies with shutter policies (auto-exposure), a controllable but ignored factor.
- **Why possibly novel:** Exposure-time-controlled analysis of precipitation appearance in segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Capture matched scenes at multiple shutter speeds under controlled sprinkler 'rain'; test models across shutter conditions.
- **Main risk:** Controlled precipitation capture is logistically heavy; simulation (streak rendering with exposure models) can substitute initially.

### W2-A-0087 - Models segment reflections on water as if they were the reflected objects: quantify the reflection-confusion rate and its structure.

- **Problem:** Water surfaces mirror the scene; segmentation models may label reflected trees/people as real ones. The error rate and its dependence on water roughness is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: on calm-water scenes, mainstream models assign real-object classes to reflection pixels at high rates, and the confusion rate drops sharply with surface ripple amplitude (a measurable psychometric-style curve) - revealing that reflection rejection is driven by high-frequency distortion cues, not scene reasoning.
- **Why important:** Waterside deployment (drones, boats, flood monitoring) needs reflection rejection; knowing the operative cue tells us when it fails (calm dawn water = worst case).
- **Why possibly novel:** Ripple-amplitude-controlled reflection confusion curves are UNVERIFIED - needs lit search.
- **Minimal experiment:** Curate calm-to-rippled water scene ladder, measure per-class confusion into reflection regions across models.
- **Main risk:** GT for 'reflection region' needs annotation, but polygon-level water masks make it tractable.

### W2-A-0088 - Steam vs smoke as the minimal-pair discrimination task for translucent media: what cue actually separates them?

- **Problem:** Steam (condensed water) and smoke (combustion aerosol) look similar but have different dynamics, color temperature, and dissipation. Alarm systems must separate them; the discriminative cue set is unknown.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the separating information is temporal (dissipation rate, buoyancy profile) rather than static appearance - static-frame classifiers plateau near chance-plus-context, while short-clip models separate well; and the temporal advantage survives across cameras (unlike appearance cues).
- **Why important:** False alarms from steam are a leading cause of fire-system distrust in kitchens/industry; a validated minimal cue set enables robust designs.
- **Why possibly novel:** Steam-smoke minimal-pair benchmark with cue ablation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Collect matched steam/smoke clips (kitchen + controlled sources), run static vs temporal models, ablate color/motion/context channels.
- **Main risk:** Collection diversity (steam types vs smoke types) drives conclusions; needs deliberate source variety.
- **Mutated from:** W2-A-0079

### W2-A-0089 - Exposure bracketing beats model scaling for fire scenes: sensor dynamic range, not model capacity, is the current bottleneck.

- **Problem:** Fire scenes span extreme dynamic range (flame core to dark smoke); single-exposure images clip both ends. The community scales models on clipped data instead of asking whether the sensor is the binding constraint.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at matched total cost, adding exposure-bracketed/HDR input to a small model outperforms scaling a single-exposure model by 10x parameters on fire-region segmentation and near-fire structure delineation - the information is destroyed before the model, and no capacity recovers clipped photons.
- **Why important:** Would redirect investment from model scale toward capture policy for safety-critical fire perception - a cheap, actionable systems conclusion.
- **Why possibly novel:** Sensor-vs-model marginal-value comparison for fire segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Capture bracketed fire footage (controlled burns), train matched models on single vs bracketed inputs, compare against a parameter-scaling ladder.
- **Main risk:** HDR capture is unavailable on legacy deployed cameras, limiting immediate applicability (but informing procurement).

### W2-A-0090 - Time-to-detect as the primary smoke metric: temporal-accumulation detectors dominate spatial models in the sub-visible regime.

- **Problem:** Smoke benchmarks report IoU on established plumes; the deployment task is detecting the transition from nothing to barely-something, which is a change-detection problem, not a segmentation problem.
- **Core hypothesis (falsifiable):** HYPOTHESIS: on ignition sequences, simple long-horizon temporal accumulation (background modeling over minutes) detects smoke minutes earlier than frame-wise segmentation models at equal false-alarm rates - the field is optimizing the wrong problem formulation for the highest-value use case.
- **Why important:** Minutes of earliness in wildfire detection have enormous real value; showing the formulation (not the model) is wrong would redirect the subfield.
- **Why possibly novel:** Ignition-anchored time-to-detect benchmarking of segmentation models is UNVERIFIED - needs lit search.
- **Minimal experiment:** Assemble ignition-timestamped fixed-camera videos (controlled burns, tower cameras), compare detection-latency ROC of accumulation vs segmentation approaches.
- **Main risk:** Fixed-camera assumption; moving-camera earliness is a different, harder problem.
- **Mutated from:** W2-A-0081

### W2-A-0091 - IoU is the wrong loss surface for amorphous regions: measure human-judgment vs IoU ranking disagreement on smoke/fog masks.

- **Problem:** For amorphous media, many different masks are equally 'right'. Whether IoU-style metrics agree with expert human quality judgments on such classes has not been tested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for smoke/fog masks, human expert pairwise preferences disagree with IoU-based rankings on a large fraction of comparisons (>30%), and the disagreement is systematic (humans forgive boundary variation but punish topology/coverage errors) - implying a validated perceptual metric would reorder the field's results.
- **Why important:** Metric validity precedes all benchmarking; a documented human-metric divergence forces metric reform for a whole class family.
- **Why possibly novel:** Human-preference validation of segmentation metrics for amorphous classes is UNVERIFIED - needs lit search.
- **Minimal experiment:** Collect 1k expert pairwise preferences over model masks on smoke scenes; fit which metric family predicts preferences.
- **Main risk:** Expert preference may be application-dependent (emissions vs alarm); collect per-use-case preferences.
- **Mutated from:** W2-A-0076

### W2-A-0092 - Layered translucency compositions (smoke behind glass, fog over water) break single-layer models: a compositional generalization test for translucent classes.

- **Problem:** Datasets contain single translucent phenomena; reality composes them (smoke seen through a window). Whether models generalize compositionally to stacked translucency is untested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: models trained on isolated smoke and isolated glass fail on their composition at rates far exceeding the product of individual error rates (super-multiplicative failure), demonstrating absence of compositional structure in learned translucency representations.
- **Why important:** Compositional failure modes are silent in standard evaluation but common in deployment (indoor fires seen through windows are THE fire-alarm case).
- **Why possibly novel:** Compositional stress testing for translucent phenomena is UNVERIFIED - needs lit search.
- **Minimal experiment:** Composite controlled stacks (real captures through glass with/without smoke machine), evaluate single-phenomenon models on compositions.
- **Main risk:** Physical capture effort; partial substitution with principled rendering possible.

### W2-A-0093 - Is fire scale-invariant for segmentation? Test transfer from candle to wildfire along a pure scale ladder.

- **Problem:** Flames are quasi-fractal; if their image statistics are scale-invariant, small-fire data (cheap, safe to collect) should train large-fire models. Nobody has measured the transfer curve along scale.
- **Core hypothesis (falsifiable):** HYPOTHESIS: fire-region segmentation transfers across ~2 orders of magnitude of physical scale with <10% relative loss (supporting scale-invariance), but smoke does NOT (buoyancy regime changes plume morphology qualitatively) - a clean split between the two phenomena's scaling behavior.
- **Why important:** Data-collection economics: if candle/bonfire data trains wildfire models, safe cheap data replaces dangerous expensive data.
- **Why possibly novel:** Scale-transfer curves for combustion phenomena are UNVERIFIED - needs lit search.
- **Minimal experiment:** Assemble scale-ladder dataset (candle, campfire, bonfire, controlled burn, wildfire footage), train at one scale, test across the ladder.
- **Main risk:** Scale confounds with camera distance/atmosphere; normalize by apparent size and control compression.

### W2-A-0094 - What matters in synthetic smoke: factor-ablate density-field realism vs lighting realism vs background realism for sim2real transfer.

- **Problem:** Fluid-simulated smoke is a promising data source, but rendering has many realism axes and nobody knows which one pays. Teams max out all axes at great cost.
- **Core hypothesis (falsifiable):** HYPOTHESIS: transfer performance is dominated by illumination/scattering realism (single-vs-multi-scatter, correct sun/sky) with density-field fidelity (simulation resolution) contributing little beyond coarse plume shape - i.e. cheap simulations with expensive lighting beat the reverse at matched render budget.
- **Why important:** Defines the cost-optimal synthetic data recipe for all translucent media, transferable to fog/steam/dust.
- **Why possibly novel:** Factorial realism ablation for participating-media training data is UNVERIFIED - needs lit search.
- **Minimal experiment:** 2x2x2 factorial render (density res x scattering model x background source), train per cell, evaluate on real smoke benchmarks.
- **Main risk:** Interaction effects may defeat the factorial simplification; the design still detects them.

### W2-A-0095 - Smoke motion vs camera motion entanglement in aerial footage: drone ego-motion masquerades as plume dynamics and vice versa.

- **Problem:** Drone-based wildfire monitoring adds ego-motion that corrupts the temporal cues (drift, divergence) that smoke detection depends on; how much of temporal-model advantage survives ego-motion is unknown.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the accuracy advantage of temporal smoke models over static ones disappears almost entirely under drone ego-motion unless flow is ego-compensated, and compensation via cheap homography recovers most (not all) of it - the residual loss localizes to parallax-heavy terrain.
- **Why important:** Quantifies exactly what stabilization/compensation infrastructure aerial fire systems need, and where terrain will still defeat them.
- **Why possibly novel:** Ego-motion ablation for temporal smoke cues is UNVERIFIED - needs lit search.
- **Minimal experiment:** Take fixed-camera smoke videos, synthetically inject ego-motion (crop-path animation), measure temporal-model degradation with/without compensation.
- **Main risk:** Synthetic ego-motion lacks true parallax; complement with real paired drone/tower footage if available.
- **Mutated from:** W2-A-0081

### W2-A-0096 - Cloud-shadow vs smoke-plume confusion in satellite imagery: which spectral bands are actually load-bearing?

- **Problem:** Satellite smoke products confuse smoke with cloud shadows and haze. Band-importance for this specific confusion (not general segmentation) is unquantified in modern learned models.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the smoke-vs-shadow decision in learned models rests almost entirely on 1-2 SWIR bands, and models degrade to near chance on this confusion pair when those bands are ablated - making sensor-band availability (differs across satellites) the primary cross-satellite transfer factor, above resolution.
- **Why important:** Cross-satellite model reuse is constrained by band sets; knowing the load-bearing bands turns transfer failure from mystery to checklist.
- **Why possibly novel:** Confusion-pair-specific band attribution is UNVERIFIED - needs lit search.
- **Minimal experiment:** Band-ablation study on Sentinel/Landsat smoke datasets, scored specifically on smoke-vs-shadow confusion subsets.
- **Main risk:** Band ablation in-model differs from retraining without the band; do both for the key bands.

### W2-A-0097 - Heat shimmer (refractive turbulence) as a segmentable phenomenon: detecting invisible hot-air regions from background distortion alone.

- **Problem:** Hot air above fires/engines/roads is invisible in RGB appearance but visibly distorts the background. No benchmark or method targets refractive-media segmentation, though it precedes visible flame/smoke.
- **Core hypothesis (falsifiable):** HYPOTHESIS: temporal distortion statistics (local nonrigid displacement variance with characteristic frequency) suffice to segment shimmer regions with useful IoU on fixed cameras, and shimmer onset precedes visible smoke in a measurable fraction of ignition videos - a genuinely new early-fire channel.
- **Why important:** Adds a new physical channel to early fire detection and defines a novel task class (segmenting media visible only through their distortion field).
- **Why possibly novel:** Refractive-region segmentation as a task is UNVERIFIED - needs lit search (Schlieren imaging is KNOWN but requires special optics; this is passive RGB).
- **Minimal experiment:** Collect fixed-camera footage over heat sources, compute distortion-field features, label shimmer regions, benchmark simple classifiers; check shimmer-before-smoke timing on ignition clips.
- **Main risk:** Wind and camera vibration create confusable distortions; needs vibration controls.

### W2-A-0098 - Koschmieder-law self-supervision: single-image fog density fields learnable from depth-luminance coupling without any fog labels.

- **Problem:** Fog density estimation lacks labels almost entirely. But atmospheric physics (KNOWN: Koschmieder attenuation model) couples scene depth, luminance shift, and fog density in a testable way that could supervise itself.
- **Core hypothesis (falsifiable):** HYPOTHESIS: enforcing consistency between a monocular depth estimate and the physically-implied luminance attenuation yields per-pixel fog-density maps that correlate strongly with transmissometer/visibility ground truth - label-free fog quantification from ordinary cameras.
- **Why important:** Every traffic/airport camera becomes a visibility sensor; also provides dense fog supervision for downstream robustness training.
- **Why possibly novel:** KNOWN: dehazing uses these physics; closing the loop as self-supervised density REGRESSION validated against meteorological ground truth is UNVERIFIED - needs lit search.
- **Minimal experiment:** Use webcam archives near airports (with METAR visibility records), fit the self-supervised model, validate against recorded visibility.
- **Main risk:** Depth estimators are themselves fog-sensitive - circularity must be broken with clear-day depth priors of fixed scenes.

### W2-A-0099 - Auto-exposure dynamics leak global fire evidence: models 'detect' fire from image-wide brightness adaptation, not fire pixels.

- **Problem:** When a camera auto-exposes to a bright flame, the whole image changes. Models may exploit this global cue, inflating benchmark scores and failing on manually-exposed or HDR cameras.
- **Core hypothesis (falsifiable):** HYPOTHESIS: fire-classification/segmentation models retain substantial accuracy when fire pixels are fully masked (evidence of global-cue reliance), and this reliance predicts their failure rate on constant-exposure footage - a shortcut with a measurable deployment cost.
- **Why important:** Shortcut detection with direct deployment implications; also a general warning for any emissive-target dataset collected with auto-exposure cameras.
- **Why possibly novel:** Auto-exposure shortcut analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Mask fire regions on test sets, measure retained accuracy; compare model performance on auto- vs fixed-exposure paired captures.
- **Main risk:** Masked-region inpainting artifacts can themselves leak information; use multiple masking strategies.
- **Mutated from:** W2-A-0078

### W2-A-0100 - Deduplicate smoke/fire benchmarks by video provenance: same-event frames in train and test inflate scores, and rankings change after cleanup.

- **Problem:** Smoke/fire datasets are assembled from scraped videos; frames of the same event often land in both train and test splits, making benchmarks partially a memorization test.
- **Core hypothesis (falsifiable):** HYPOTHESIS: provenance-level deduplication (event/video-level splits) drops reported performance substantially (>10 points for some methods) and reorders methods, with the biggest drops for highest-capacity models - current smoke/fire SOTA is partly leakage measurement.
- **Why important:** Safety-critical procurement decisions cite these benchmarks; leakage-corrected numbers are the ones that predict field performance.
- **Why possibly novel:** Provenance-forensic re-splitting of fire/smoke benchmarks is UNVERIFIED - needs lit search (leakage audits in other domains are KNOWN).
- **Minimal experiment:** Perceptual-hash + temporal correlation clustering across 4 public datasets to find leaked pairs; re-evaluate public models on clean splits.
- **Main risk:** Aggressive dedup may over-merge distinct-but-similar events; manual verification of clusters needed.

## C05-transparent-glass-mirror

### W2-A-0101 - Glass segmentation models are frame detectors in disguise: frameless glass collapses them, quantifying boundary-cue dependence.

- **Problem:** Glass region datasets are dominated by framed windows/doors. Models may segment the frame context, not glass itself - a decomposable and testable reliance.
- **Core hypothesis (falsifiable):** HYPOTHESIS: occluding frames (while keeping glass interiors visible) collapses glass-detection accuracy toward chance, while occluding glass interiors (keeping frames) barely hurts - the learned representation contains almost no glass-intrinsic evidence.
- **Why important:** Frameless glass (glass walls, barriers, shower doors) is precisely where collisions and robot failures happen; benchmark scores hide this.
- **Why possibly novel:** Interior-vs-frame information decomposition for glass models is UNVERIFIED - needs lit search.
- **Minimal experiment:** Region-swap occlusion tests on GDD/GSD datasets across 3 public glass models; report interior-only vs frame-only accuracy.
- **Main risk:** Occlusion masks introduce artifacts; use both blur-fill and inpainting controls.

### W2-A-0102 - Mirror detection relies on scene-duplication matching: mirrors reflecting textureless regions become invisible to current models.

- **Problem:** Mirror segmentation models are believed to detect reflected-content correspondence with the surrounding scene. If so, mirrors showing featureless content (white walls, sky) should fail catastrophically - untested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: mirror-detection accuracy is a monotonic function of feature-correspondence density between mirror interior and visible scene, approaching chance for low-texture reflections - and this single variable explains most inter-image difficulty variance in mirror benchmarks.
- **Why important:** Predictable failure conditions (bathroom mirrors reflecting blank walls) matter for robot navigation; and the analysis reveals the actual algorithm learned.
- **Why possibly novel:** Correspondence-density difficulty law for mirror detection is UNVERIFIED - needs lit search.
- **Minimal experiment:** Compute cross-region feature-match counts on mirror datasets, regress per-image accuracy on match density; validate causally with controlled captures (same mirror, varied reflected content).
- **Main risk:** Confounds with mirror size and frame visibility; include them as covariates.

### W2-A-0103 - Estimate the background refraction-distortion field as a pretext task: transparency becomes visible through what it does to the background.

- **Problem:** Transparent objects lack own-appearance; their signature is the distortion they impose on background. No mainstream method explicitly measures its usable information content.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a model trained to regress the local background-warp field (self-supervised from paired with/without-object captures or synthetic refraction) segments transparent objects with accuracy competitive with fully-supervised appearance methods, and generalizes better across object types because refraction physics is object-independent.
- **Why important:** Physics-grounded signals should transfer where appearance signals do not - the central hope for robotic manipulation of glassware.
- **Why possibly novel:** KNOWN: refraction cues appear in classic vision; a warp-field pretext for transparent segmentation with cross-category transfer measurement is UNVERIFIED - needs lit search.
- **Minimal experiment:** Render synthetic refractive objects over textured backgrounds, train warp-regression, transfer to real ClearGrasp-style data; compare cross-category generalization vs supervised baseline.
- **Main risk:** Textureless backgrounds carry no warp signal - method has a principled blind spot to characterize honestly.

### W2-A-0104 - Two-frame parallax separates glass from mirror: highlight/reflection motion direction is a deterministic physical discriminator.

- **Problem:** Static images confuse transmissive (glass) and reflective (mirror) surfaces. Under camera motion, transmitted and reflected content move with opposite parallax signs relative to the surface - a clean physical signature nobody benchmarks.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a simple two-frame parallax-sign test resolves glass-vs-mirror with >90% accuracy where single-frame SOTA models are near chance, using no learning beyond flow estimation - physics beats appearance learning for this decision.
- **Why important:** Robots move anyway; exploiting mandatory ego-motion for free surface-type disambiguation is immediately usable.
- **Why possibly novel:** KNOWN: layer separation via motion exists (reflection removal literature); its use as a surface-type CLASSIFIER benchmarked against segmentation SOTA is UNVERIFIED - needs lit search.
- **Minimal experiment:** Capture short baseline pairs of glass/mirror scenes, implement parallax-sign voting, compare with single-frame models.
- **Main risk:** Small parallax + distant reflected content weakens the signal; characterize the operating envelope.

### W2-A-0105 - A $30 polarizer beats architecture research for glass segmentation: quantify the sensor-vs-model marginal value.

- **Problem:** Specular reflections from dielectric surfaces are strongly polarized (KNOWN physics). The field pursues architectural gains on RGB while ignoring that a rotating polarizer may deliver larger gains for trivial cost.
- **Core hypothesis (falsifiable):** HYPOTHESIS: two-shot cross-polarized capture + a small model outperforms the best RGB-only architectures by a larger margin than 3 years of published architectural progress on glass/mirror segmentation - the field's bottleneck is sensing, not modeling.
- **Why important:** A cost-benefit result that could redirect the subfield's effort allocation and immediately upgrade deployed systems that control their cameras.
- **Why possibly novel:** Head-to-head sensing-vs-architecture marginal-value accounting for transparent surfaces is UNVERIFIED - needs lit search (polarization vision itself is KNOWN).
- **Minimal experiment:** Capture a 200-scene polarized glass dataset, train matched small models on RGB vs polarization pairs, compare with published RGB SOTA deltas.
- **Main risk:** Doesn't help legacy imagery; framing must be prospective (system design), not retrospective.

### W2-A-0106 - Prompt-through-glass confusion: point prompts inside glass regions make SAM segment the background object - measure the transparency-prompt pathology.

- **Problem:** Promptable models assume prompts land 'on' an object, but for transparent surfaces the prompt pixel contains two surfaces (glass + background). Which one SAM returns, and how consistently, is uncharacterized.
- **Core hypothesis (falsifiable):** HYPOTHESIS: SAM resolves the two-surface ambiguity by returning the background object in the overwhelming majority of cases (glass is never a hypothesis), and no prompt engineering (multi-point, box) reliably retrieves the glass surface - transparency is outside SAM's implicit object ontology, a categorical (not gradual) failure.
- **Why important:** Defines a hard ontological boundary of promptable segmentation, relevant to any pipeline that might encounter windows/vitrines (retail, driving, indoor robotics).
- **Why possibly novel:** Two-surface prompt-resolution analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Prompt-grid evaluation on glass datasets: classify outputs as glass-surface/background/mixed; try prompt-engineering ladders for glass retrieval.
- **Main risk:** Some 'glass' pixels are dominated by reflections (surface-like appearance) - stratify by transmission/reflection ratio.
- **Mutated from:** W2-A-0006

### W2-A-0107 - Depth-sensor dropout is free glass supervision: mine LiDAR/ToF invalid-return masks as automatic transparent-surface labels at fleet scale.

- **Problem:** Transparent surfaces are exactly where depth sensors return invalid/void measurements - a systematically informative failure that every robot fleet records and discards.
- **Core hypothesis (falsifiable):** HYPOTHESIS: RGB models trained purely on depth-dropout-derived pseudo-labels (with geometric filtering of other dropout causes) reach a large fraction (>70%) of fully-supervised glass segmentation accuracy with zero human labels, and scale with fleet data volume where supervised methods cannot.
- **Why important:** Converts a sensor weakness into a self-annotating data engine for a notoriously label-starved problem.
- **Why possibly novel:** KNOWN: individual works use depth invalidity as a cue; the fleet-scale self-training scaling claim is UNVERIFIED - needs lit search.
- **Minimal experiment:** Use existing RGB-D datasets (ScanNet-like), extract dropout masks, filter (specular metals, range limits), train RGB-only model, evaluate on GDD.
- **Main risk:** Dropout also fires on dark/absorptive and distant surfaces; the filtering step determines everything.

### W2-A-0108 - Mirror-boundary ownership is annotated inconsistently across datasets: the frame/content confusion audit.

- **Problem:** Does a mirror mask include its frame? The reflected content's boundary or the physical glass edge? Datasets answer differently, and models inherit incoherent supervision.
- **Core hypothesis (falsifiable):** HYPOTHESIS: public mirror/glass datasets disagree systematically on boundary conventions (measurable via matched-scene or protocol probing), and this convention noise accounts for a substantial fraction of apparent cross-dataset generalization failure - harmonizing conventions post hoc recovers several points of transfer performance for free.
- **Why important:** Convention noise masquerades as model failure, corrupting scientific conclusions about architecture differences in the whole subfield.
- **Why possibly novel:** Cross-dataset convention forensics for specular/transparent classes is UNVERIFIED - needs lit search.
- **Minimal experiment:** Annotate 100 shared-protocol probe images under each dataset's inferred convention, quantify convention distance, re-evaluate cross-dataset transfer after convention mapping.
- **Main risk:** Inferring conventions from data is noisy; contact dataset authors where possible.

### W2-A-0109 - Transparent vs translucent is a bimodal task hiding in one benchmark: clear glass and frosted glass are solved by different cues and should be split.

- **Problem:** Benchmarks pool clear (see-through) and frosted/textured (diffusing) surfaces. If the discriminative cues differ fundamentally (background continuity vs surface texture), pooled scores obscure two distinct problems.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-image performance across glass benchmarks is bimodal along a measurable transmission-clarity axis; model families rank DIFFERENTLY on the two modes (texture-based models win frosted, context-based win clear), so pooled leaderboards are not measuring a single capability.
- **Why important:** Correct taxonomy is prerequisite for progress; a documented mode split would restructure how the subfield evaluates and designs.
- **Why possibly novel:** Clarity-axis bimodality analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Estimate per-region clarity (background visibility metrics) on GDD/Trans10K, plot per-model accuracy distributions along the axis, test rank inversion.
- **Main risk:** Clarity estimation without GT optics is approximate; hand-label a calibration subset.

### W2-A-0110 - Day-night transmission/reflection flip: the same window changes optical class by time of day, and models trained on one phase fail on the other.

- **Problem:** Windows transmit by day (interior view) and reflect by night (mirror-like from lit side). This physically-forced within-scene domain shift is undocumented in segmentation.
- **Core hypothesis (falsifiable):** HYPOTHESIS: glass segmentation models exhibit a strong day-night performance asymmetry aligned with their training-set illumination statistics, and the SAME physical surfaces flip between 'easy' and 'hard' across the transition - fixed-scene time-lapse evaluation will show a characteristic sigmoid degradation tied to the transmission/reflection ratio, not to general low-light difficulty.
- **Why important:** Building-scale vision (energy audits, security, robotics) operates around the clock; a physics-driven diurnal failure cycle is predictable and correctable once measured.
- **Why possibly novel:** Fixed-scene diurnal analysis for transparent surfaces is UNVERIFIED - needs lit search.
- **Minimal experiment:** Collect webcam/time-lapse footage of glass facades across day-night cycles, annotate once (geometry is fixed), evaluate models across the cycle against illumination covariates.
- **Main risk:** Low-light degradation confounds; include matched non-glass control surfaces for baseline drift.

### W2-A-0111 - Establish the human ceiling for clean-glass detection in single RGB images: some transparency is information-theoretically invisible.

- **Problem:** Claims of glass-detection progress never report the human ceiling. Perfectly clean, non-reflective glass may be undetectable in principle from single images - meaning benchmarks contain unsolvable pixels that cap and distort scores.
- **Core hypothesis (falsifiable):** HYPOTHESIS: human experts given unlimited time fail on a measurable subset of benchmark glass regions (near-zero mutual information cases), models fail on a superset of these, and removing information-theoretically-invisible regions from evaluation changes both absolute scores and method rankings.
- **Why important:** Separates 'model limitation' from 'task impossibility' - required for honest progress claims and for deciding when extra sensors are mandatory rather than optional.
- **Why possibly novel:** Human-ceiling calibration for transparency benchmarks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run a careful human study (N=10, unlimited time, zoom allowed) on 300 glass regions; classify regions by human solvability; re-score public models on the solvable subset.
- **Main risk:** Human performance depends on display conditions and effort; strict protocol needed.

### W2-A-0112 - Interior-blindness test: mask out glass interiors entirely - if performance is unchanged, models never look at the glass.

- **Problem:** Related to frame reliance but stronger: perhaps NO pixel inside glass regions contributes to detection decisions - models may operate exclusively on surrounding geometry (door frames, wall openings).
- **Core hypothesis (falsifiable):** HYPOTHESIS: replacing all glass-interior pixels with scrambled or neutral content changes glass-region predictions by <5% IoU for current models - a falsifiable 'interior blindness' claim implying the task, as learned, is contextual opening detection, and that models will hallucinate glass in glassless openings (testable corollary on open windows).
- **Why important:** The corollary - false glass on open frames - is a real robotics hazard (robot refuses to pass an open doorway) and reveals the true learned task.
- **Why possibly novel:** The open-frame hallucination corollary test is UNVERIFIED - needs lit search.
- **Minimal experiment:** Interior-scramble evaluation + a curated open-window/empty-frame probe set; measure hallucinated glass rate.
- **Main risk:** Overlaps conceptually with W2-A-0101; kept because the corollary (hallucination on open frames) is a distinct falsifiable prediction.
- **Mutated from:** W2-A-0101

### W2-A-0113 - Joint vs sequential reflection-removal and segmentation: does cleaning reflections first help or destroy the very cues glass detectors need?

- **Problem:** Reflections are noise for scene segmentation but SIGNAL for glass detection. Pipelines that remove reflections before segmentation may improve object masks while blinding glass detection - an unmeasured interaction.
- **Core hypothesis (falsifiable):** HYPOTHESIS: reflection-removal preprocessing improves general scene segmentation inside glass regions but strictly degrades glass-region detection itself, with the tradeoff strong enough that optimal pipelines must run both paths - a quantified antagonism between two subfields' objectives.
- **Why important:** Both communities publish independently; demonstrating their objectives are antagonistic in composition changes how full systems should be built.
- **Why possibly novel:** The antagonism quantification is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run 3 reflection-removal methods before 3 glass detectors and 3 scene segmenters; measure the two metrics' movement directions.
- **Main risk:** Reflection-removal quality varies; conclusions should be method-robust.

### W2-A-0114 - LiDAR-camera disagreement mining auto-labels glass at driving-fleet scale: the free training set nobody harvests.

- **Problem:** In driving stacks, LiDAR passes through glass while camera sees surfaces (or vice versa for mirrors) - systematic cross-sensor disagreement localizes transparent surfaces, yet is discarded as noise.
- **Core hypothesis (falsifiable):** HYPOTHESIS: cross-sensor disagreement patterns (camera-detects-surface + LiDAR-returns-far) yield glass pseudo-labels with precision >80% after geometric filtering in urban scenes, sufficient to train camera-only glass detection that generalizes to buildings/bus-stops/storefronts absent from any human-labeled dataset.
- **Why important:** Storefront/bus-shelter glass matters for driving safety and is essentially unlabeled at scale today.
- **Why possibly novel:** Disagreement-mining for transparent-class auto-labeling in driving data is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run the mining rule on nuScenes/Waymo sequences, manually audit 500 mined regions for precision, train and evaluate a camera-only model.
- **Main risk:** LiDAR behavior on glass varies with angle/coating (sometimes returns); precision audit is the gating step.
- **Mutated from:** W2-A-0107

### W2-A-0115 - Liquid-level segmentation in transparent containers: the meniscus is a 1-pixel curve whose cues are refraction discontinuities, not edges.

- **Problem:** Estimating fill levels through glass (labs, kitchens, industry) requires localizing the liquid-air interface, which presents as a refraction-index discontinuity - a signal class no segmentation paradigm targets.
- **Core hypothesis (falsifiable):** HYPOTHESIS: meniscus localization from single RGB fails with standard segmentation (boundary F-score near chance) but becomes reliable using background-distortion discontinuity features across the interface - and container curvature can be jointly inferred, making level estimation metrically accurate to <5% of container height.
- **Why important:** Lab automation and food robotics need fill-level perception; also a clean scientific instance of 'segmenting an index-of-refraction boundary'.
- **Why possibly novel:** Meniscus segmentation as a benchmark task is UNVERIFIED - needs lit search.
- **Minimal experiment:** Capture container ladder (shapes x liquids x backgrounds) with measured fill levels; benchmark segmentation vs distortion-feature approaches.
- **Main risk:** Opaque liquids trivialize the task, colorless liquids in textureless scenes may be impossible - the dataset must span the difficulty axis honestly.
- **Mutated from:** W2-A-0103

### W2-A-0116 - Mirror recursion depth as a scene-understanding stress test: what do models do with mirrors inside mirrors?

- **Problem:** Nested reflections (mirror showing a mirror) produce recursive scene copies. Model behavior on recursion - treating each level as real, or collapsing all - probes whether any scene-graph reasoning exists in dense predictors.
- **Core hypothesis (falsifiable):** HYPOTHESIS: current models segment first-level reflected content as real objects at the same rate as directly-viewed objects (no reflection discount at all), and behavior is IDENTICAL at deeper recursion levels - demonstrating zero representation of the reflection relation, falsifiable by any level-dependent behavior.
- **Why important:** A crisp probe separating 'pixel classification' from 'scene understanding' - useful as a diagnostic axis for foundation model claims.
- **Why possibly novel:** Recursion-depth-graded evaluation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Stage two-mirror scenes with controlled recursion, run panoptic/promptable models, tabulate per-level treatment of duplicated objects.
- **Main risk:** Small niche; value is diagnostic, framed as a probe rather than a benchmark.
- **Mutated from:** W2-A-0087

### W2-A-0117 - Caustics as transparent-object shadows: the bright patterns under glassware are a detection cue with known physics that no model uses.

- **Problem:** Transparent objects cast structured light patterns (caustics) and faint darkened shadows. These secondary evidence sources are visible when the object is not, and are absent from all training objectives.
- **Core hypothesis (falsifiable):** HYPOTHESIS: caustic/shadow regions are detectable with high precision and their presence improves transparent-object localization recall substantially in tabletop scenes (especially for rim-lit invisible glassware), with the geometric back-projection from caustic to object being learnable from synthetic optics.
- **Why important:** Robotic grasping of glassware fails on exactly the invisible cases; secondary-evidence detection is a fundamentally different attack on the problem.
- **Why possibly novel:** Caustic-mediated object localization for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Render synthetic tabletop scenes with physically-correct caustics, train caustic detector + back-projection, test on real captured glassware scenes with directional light.
- **Main risk:** Requires directional lighting; diffuse-lit scenes lose the cue - operating conditions must be characterized.

### W2-A-0118 - Glass boundary is physically a gradient, not a curve: annotations pretend a sharp edge exists where refraction blends millimeters of scene.

- **Problem:** At glass edges (especially curved surfaces), the image transitions through a refraction gradient several pixels wide. Sharp-polygon annotations impose a fictional boundary whose placement varies by annotator - structurally identical to smoke's problem but unrecognized for rigid transparent objects.
- **Core hypothesis (falsifiable):** HYPOTHESIS: boundary-localization variance among annotators on curved-glass edges is several times higher than on opaque-object edges (measurable), and boundary-quality metric differences between competing methods on transparency benchmarks fall INSIDE this annotation noise band - boundary-level rankings there are statistically meaningless.
- **Why important:** Guards the community against over-interpreting boundary-metric progress on transparency benchmarks.
- **Why possibly novel:** Annotation-noise-floor analysis specific to refractive edges is UNVERIFIED - needs lit search.
- **Minimal experiment:** Multi-annotator re-labeling of 200 curved-glass edges, compute noise floor, compare with published method deltas.
- **Main risk:** Straightforward but requires funding a small annotation study.
- **Mutated from:** W2-A-0016

### W2-A-0119 - Cross-dataset transparency transfer is near zero, and the cause is photographic setting bias, not object diversity: lab-vs-wild forensics.

- **Problem:** Transparency datasets are collected in narrow settings (lab turntables, stock photos, specific cities). Cross-dataset generalization numbers are rarely reported and anecdotally terrible - but WHY they fail is unattributed.
- **Core hypothesis (falsifiable):** HYPOTHESIS: cross-dataset performance drops are predicted by capture-setting statistics (lighting type, background depth structure, camera height) rather than object-category overlap - transfer fails on photography, not on objects - implying collection-protocol diversification beats category diversification for the next dataset.
- **Why important:** Directly instructs how the community should spend its next data-collection dollar for transparent objects.
- **Why possibly novel:** Setting-vs-category attribution of transfer failure is UNVERIFIED - needs lit search.
- **Minimal experiment:** Full cross-evaluation matrix over 5 transparency datasets; regress transfer drops on setting statistics vs category-overlap measures.
- **Main risk:** Setting statistics are post-hoc descriptors; causal confirmation needs controlled recapture of matched objects across settings.

### W2-A-0120 - A $200 thermal camera makes glass opaque: quantify when cheap LWIR fusion beats years of RGB algorithmic progress on transparent surfaces.

- **Problem:** Long-wave infrared does not transmit through glass (KNOWN physics) - glass is opaque and boundary-crisp in thermal. The economic tradeoff between adding a thermal channel and pursuing RGB-only algorithms is never computed.
- **Core hypothesis (falsifiable):** HYPOTHESIS: RGB+LWIR late fusion with a trivial model exceeds the best RGB-only glass segmentation by a margin larger than the total published RGB architectural progress since the task's inception, and the fusion model's failures are confined to thermally-equilibrated scenes (measurable operating boundary).
- **Why important:** If a cheap sensor dominates the algorithmic frontier, safety-critical system builders (robots near glass) should know before funding more RGB research.
- **Why possibly novel:** KNOWN: thermal glass opacity is textbook optics; the quantified benchmark-level economic comparison is UNVERIFIED - needs lit search.
- **Minimal experiment:** Collect 150 aligned RGB-LWIR glass scenes, train small fusion model, compare against RGB SOTA reproduced on the RGB channel of the same scenes.
- **Main risk:** Thermal-RGB alignment and resolution mismatch; scene temperature equilibrium cases where thermal contrast vanishes.
- **Mutated from:** W2-A-0105

### W2-A-0121 - Puddles are mirrors on the road: wet-surface reflections are systematically mislabeled and cause phantom-object segmentation in driving scenes.

- **Problem:** After rain, road puddles reflect vehicles, lights, and sky. Driving datasets label puddle pixels as 'road', and models inherit both phantom objects (reflected cars segmented as cars) and missed hazards (puddle itself unrecognized).
- **Core hypothesis (falsifiable):** HYPOTHESIS: on wet-scene driving data, a measurable rate of false vehicle/pedestrian segments spatially coincides with puddle reflections (verifiable by geometric mirroring about the road plane), and this error class is absent from benchmark metrics because puddle regions are labeled road and errors there are diluted - a hidden safety-relevant failure mode with a geometric verification method.
- **Why important:** Phantom pedestrians in reflections can trigger emergency braking; the geometric verification makes the audit rigorous rather than anecdotal.
- **Why possibly novel:** Mirror-geometry-verified phantom-object auditing in driving segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Mine wet scenes from BDD/ACDC, detect vertically-mirrored segment pairs about the road plane, quantify phantom rate per model.
- **Main risk:** True objects and their reflections co-occur; the mirroring test must be strict to avoid false audit positives.
- **Mutated from:** W2-A-0087

### W2-A-0122 - Shadow-density inversion recovers translucency alpha for free: an object's shadow encodes its transmission coefficient.

- **Problem:** Ground-truth alpha for translucent objects requires studio matting. But the shadow a translucent object casts has attenuation proportional to its transmission - physics offers free alpha labels outdoors.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-region transmission coefficients recovered from shadow luminance ratios (object shadow vs adjacent opaque-reference shadow) agree with studio-measured alpha within usable tolerance, enabling automatic construction of translucency-supervised datasets from ordinary sunlit footage.
- **Why important:** Would unlock large-scale translucency supervision without studios - feeding every idea that needs alpha ground truth (smoke, frosted glass, fabrics).
- **Why possibly novel:** Shadow-mediated alpha recovery as a dataset-construction tool is UNVERIFIED - needs lit search.
- **Minimal experiment:** Capture objects with known transmission (calibrated filters) in sunlight, invert shadow ratios, validate against ground truth; then mine web imagery.
- **Main risk:** Multiple light sources and ambient bounce corrupt the inversion; restrict to strong-sun regimes and quantify error bars.

### W2-A-0123 - Screens are emissive fake windows: displays fool glass/scene segmentation, and their temporal artifacts (refresh, moire) are the untapped tell.

- **Problem:** TVs and monitors show scenes that models segment as real 3D content (a person on a billboard segmented as pedestrian). Their physical tells - refresh flicker, moire against sensor grid, spectral spikiness - are never exploited.
- **Core hypothesis (falsifiable):** HYPOTHESIS: display-region false-positive rates for person/vehicle classes are substantial in urban scenes, and a rolling-shutter-aware temporal probe (banding detection) identifies emissive displays with high precision, eliminating most phantom segments at negligible compute.
- **Why important:** Billboards with faces/cars are ubiquitous; driving and surveillance stacks need display rejection, and the physics tell is robust across display content.
- **Why possibly novel:** Display-rejection via sensor-display temporal interaction for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Curate urban scenes with active displays, measure phantom-class rates across models; implement banding detector, measure rejection precision/recall.
- **Main risk:** Modern displays at high refresh with global-shutter cameras may lack banding; enumerate the sensor-display compatibility matrix.

### W2-A-0124 - Dirt makes glass visible: performance vs surface-condition curves reveal that benchmarks oversample dirty, easy glass.

- **Problem:** Dust, smudges, and rain droplets give glass surfaces detectable texture. If benchmarks oversample real-world dirty glass, reported performance overstates ability on clean architectural glass - the dangerous case.
- **Core hypothesis (falsifiable):** HYPOTHESIS: model accuracy on glass regions is a strong increasing function of surface-contamination level (quantifiable via micro-texture statistics), benchmark distributions are skewed toward contaminated glass relative to modern building stock, and re-weighting evaluation to clean-glass-heavy distributions drops SOTA scores dramatically.
- **Why important:** Deployment environments (offices, malls) feature professionally-cleaned glass - exactly the underrepresented hard case; the analysis recalibrates safety expectations.
- **Why possibly novel:** Contamination-conditioned evaluation for transparency is UNVERIFIED - needs lit search.
- **Minimal experiment:** Score contamination level on benchmark glass regions (annotator + texture statistics), plot accuracy vs contamination, reweight and re-rank.
- **Main risk:** Contamination scoring is subjective at the margins; anchor with controlled dirty-to-clean captures of one facade.

### W2-A-0125 - Window tint and low-emissivity coatings create a spectral fingerprint: modern architectural glass is detectable by its color cast, old glass is not.

- **Problem:** Contemporary buildings use coated/tinted glazing with subtle spectral signatures (green/blue edge casts, reflectance curves), while historic clear glass lacks them. Detection difficulty may be stratified by construction era - an unexamined structure in the data.
- **Core hypothesis (falsifiable):** HYPOTHESIS: glass-detection accuracy correlates with coating-induced spectral signatures measurable in RGB statistics; controlling for context, coated glazing is substantially easier than heritage clear glass - implying reported urban benchmark performance silently rides on modern construction practice and will degrade in historic districts.
- **Why important:** Geographic/architectural generalization of glass detection has direct safety implications for delivery robots and drones operating across city ages.
- **Why possibly novel:** Construction-era stratification of transparency performance is UNVERIFIED - needs lit search.
- **Minimal experiment:** Tag benchmark glass by building era/coating evidence, stratify performance; capture matched modern vs heritage facades for causal confirmation.
- **Main risk:** Era correlates with frame style and cleanliness; multi-covariate analysis required.
- **Mutated from:** W2-A-0124

## C06-camouflage-ambiguity

### W2-A-0126 - Do models and humans find the same camouflage hard? Correlate model difficulty with human search time per image.

- **Problem:** Camouflaged object detection (COD) difficulty is assumed to align with human difficulty, but models use different cues; misalignment would mean COD benchmarks measure something other than camouflage.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-image model error and human search time correlate only moderately (rank r about 0.3-0.5), with systematic divergence classes: humans fail on semantic mimicry (leaf-shaped insects), models fail on low-level texture continuity - two dissociable camouflage mechanisms confounded in one benchmark.
- **Why important:** If difficulty axes dissociate, defense/wildlife applications need mechanism-specific evaluation, and 'superhuman COD' claims need re-reading.
- **Why possibly novel:** Human-search-time-anchored difficulty decomposition for COD is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run a timed human search study (N=20, 300 COD images), correlate with per-image model errors, factor-analyze the divergences.
- **Main risk:** Search time is noisy and display-dependent; needs psychophysics rigor.

### W2-A-0127 - COD benchmarks have a center-and-single-object bias: randomized multi-instance evaluation collapses reported SOTA.

- **Problem:** COD datasets typically frame one centered camouflaged subject (photographer bias). Models may learn 'find the centered anomaly' rather than camouflage-breaking.
- **Core hypothesis (falsifiable):** HYPOTHESIS: SOTA COD models degrade disproportionately (vs a saliency-model control) when evaluated on off-center crops, multi-instance composites, and empty scenes (false-positive stress) - a large fraction of measured COD skill is compositional prior, not camouflage analysis.
- **Why important:** Real camouflage scenarios (wildlife surveys, search-and-rescue) have arbitrary composition and mostly-empty frames; benchmark bias hides deployment failure.
- **Why possibly novel:** Composition-bias stress testing specific to COD is UNVERIFIED - needs lit search.
- **Minimal experiment:** Re-render COD test sets with controlled recomposition (offset crops, mosaics, negatives), report degradation ratios per model.
- **Main risk:** Recomposition artifacts; use camera-trap footage as the natural-composition validation.

### W2-A-0128 - Quantify the information motion adds to camouflage breaking: matched-frame video-vs-still analysis on camouflaged animals.

- **Problem:** Motion famously breaks camouflage, but the magnitude - how many bits motion adds over the best static analysis - has never been quantified for models or humans on matched data.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for strongly-camouflaged targets, 3-5 frames of motion raise model detection from near-chance to high accuracy (most of the task's information is temporal), implying static COD is a fundamentally information-starved formulation and the field's static focus is misallocated.
- **Why important:** Redirects COD research investment toward temporal formulations where the information actually lives.
- **Why possibly novel:** Bits-added-by-motion quantification on matched still/video pairs is UNVERIFIED - needs lit search.
- **Minimal experiment:** MoCA dataset: evaluate matched models on single frames vs short clips, sweep clip length, plot information gain curves.
- **Main risk:** Camera motion contaminates object motion; use stabilized subsets.
- **Mutated from:** W2-A-0036

### W2-A-0129 - Camouflage and saliency are poles of one conspicuity axis: test whether a single linear direction in feature space spans both tasks.

- **Problem:** Salient object detection and COD are run as separate subfields with separate models, yet they plausibly measure opposite ends of one perceptual quantity.
- **Core hypothesis (falsifiable):** HYPOTHESIS: in foundation-model feature space, a single learned 'conspicuity' direction supports both SOD and COD via thresholding at opposite ends (linear probe transfers between tasks with minor loss), implying the two literatures are duplicating one problem - falsifiable if cross-task probes fail.
- **Why important:** Would unify two benchmark ecosystems and reveal that dozens of specialized architectures encode one scalar function.
- **Why possibly novel:** Cross-task linear-direction unification test is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train linear probes on DINOv2 features for SOD, evaluate on COD (inverted) and vice versa; compare with specialized SOTA.
- **Main risk:** Task definitions differ beyond conspicuity (object-hood, boundaries); partial transfer needs careful interpretation.

### W2-A-0130 - Split camouflage into texture-matching vs shape-disruption mechanisms and show current benchmarks confound them.

- **Problem:** Biological camouflage uses distinct strategies (background matching, disruptive coloration, edge mimicry). Datasets pool them, so 'COD performance' averages over mechanistically different problems.
- **Core hypothesis (falsifiable):** HYPOTHESIS: annotating COD images by camouflage mechanism reveals strongly method-dependent performance profiles (edge-based methods fail on disruptive coloration, texture methods fail on background matching), and mechanism composition varies across datasets enough to explain most cross-dataset ranking instability.
- **Why important:** A mechanistic taxonomy converts an appearance-shuffled benchmark into interpretable sub-problems with different optimal designs.
- **Why possibly novel:** Mechanism-stratified COD evaluation is UNVERIFIED - needs lit search (mechanisms themselves are KNOWN in biology, e.g. Cott's principles).
- **Minimal experiment:** Have biologists annotate mechanism labels on 1k COD images, stratify existing model results, quantify ranking flips.
- **Main risk:** Mechanisms co-occur in single animals; multi-label annotation needed.

### W2-A-0131 - Region-core evaluation for ambiguous boundaries: scoring only the indisputable interior changes COD/boundary-class rankings.

- **Problem:** For camouflaged and fuzzy-boundary objects, annotator disagreement concentrates at boundaries, yet metrics weight boundary pixels heavily - rankings may reflect boundary-style matching rather than detection ability.
- **Core hypothesis (falsifiable):** HYPOTHESIS: evaluating on eroded 'consensus cores' plus a separate detection-level score reorders published COD methods materially, and the reordering correlates with which annotation team produced each training set - boundary-heavy metrics have been rewarding style imitation.
- **Why important:** Cheap re-evaluation protocol that could correct a whole leaderboard's conclusions without new data collection.
- **Why possibly novel:** Core-based re-ranking audit for ambiguity-heavy tasks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Erode GT masks at multiple radii, re-score public COD predictions, measure rank stability vs erosion radius.
- **Main risk:** Erosion destroys legitimately-informative boundary skill for thin animals; report per-shape-class.
- **Mutated from:** W2-A-0091

### W2-A-0132 - COD models exploit chromatic micro-contrast that humans cannot see: grayscale and chroma-noise ablations reveal non-perceptual shortcuts.

- **Problem:** If models detect camouflaged animals via sub-perceptual color differences (JPEG chroma noise, sensor pattern), they solve a different problem than camouflage perception - and will fail when those artifacts change.
- **Core hypothesis (falsifiable):** HYPOTHESIS: COD SOTA drops far more than human performance under chroma removal and chroma-noise matching (models rely on machine-visible chromatic microstructure), and this reliance predicts cross-camera generalization failure - the shortcut is measurable and consequential.
- **Why important:** Determines whether COD progress is perceptual science or artifact mining; guides dataset re-collection with camera diversity.
- **Why possibly novel:** Perceptual-vs-machine cue decomposition in COD is UNVERIFIED - needs lit search.
- **Minimal experiment:** Evaluate models and humans on original vs chroma-ablated COD images; correlate model reliance with cross-dataset drops.
- **Main risk:** Human baseline collection needed; ablation must preserve perceptual equivalence (verify psychophysically).

### W2-A-0133 - Artificial (military/textile) camouflage and biological camouflage do not transfer: two data regimes with different statistics.

- **Problem:** COD datasets are mostly biological; applications often target artificial camouflage (nets, patterns, clothing). Whether learned camouflage-breaking transfers between the regimes is untested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: cross-regime transfer (bio-trained to artificial, and reverse) loses most performance because the two regimes break different statistical assumptions (biological camouflage matches local texture statistics; printed patterns match texture class but violate phase statistics) - a measurable statistical signature separates them.
- **Why important:** Security and conservation users assume COD models generalize; a documented regime boundary with statistical explanation prevents misdeployment.
- **Why possibly novel:** Bio-vs-artificial camouflage transfer quantification is UNVERIFIED - needs lit search.
- **Minimal experiment:** Assemble small artificial-camouflage test set, run bio-trained SOTA, analyze failures via texture-statistics comparisons.
- **Main risk:** Artificial-camouflage data availability; may require synthetic rendering with real patterns.

### W2-A-0134 - The zoom paradox: camouflage vanishes at high magnification, so scale selection IS the camouflage problem - test scale-oracle decomposition.

- **Problem:** Camouflage works at the scale where object texture matches background; zoom in enough and micro-texture differences appear. Whether model failure is scale-selection failure vs discrimination failure is unresolved.
- **Core hypothesis (falsifiable):** HYPOTHESIS: with an oracle providing optimal analysis scale per region, simple texture discriminators match SOTA COD models (discrimination is easy at the right scale), so COD progress has mostly been implicit scale-search progress - reframing the problem as attention/search, not representation.
- **Why important:** Identifies the actual hard sub-problem, redirecting architecture effort toward scale policy learning.
- **Why possibly novel:** Scale-oracle attribution for COD is UNVERIFIED - needs lit search.
- **Minimal experiment:** Grid-search analysis scale per image region on COD data, compare oracle-scale simple features vs end-to-end SOTA.
- **Main risk:** Oracle defined via GT leaks information; careful protocol (scale chosen on held-out criterion) required.

### W2-A-0135 - Matting-vs-masking crossover for fuzzy classes: measure the boundary-alpha entropy above which binary annotation becomes counterproductive.

- **Problem:** Hair, fur, feathers, and foliage boundaries are partial-coverage zones. The field lacks a criterion for when to switch from binary masks to alpha mattes, so datasets choose arbitrarily.
- **Core hypothesis (falsifiable):** HYPOTHESIS: there exists a measurable boundary-alpha entropy threshold above which training with binary labels actively degrades both binary AND soft evaluation performance relative to matte supervision (label noise exceeds signal), and common classes (fur, hair, foliage) sit above it while most objects sit below.
- **Why important:** Provides a principled annotation-policy rule for every future dataset touching fuzzy classes.
- **Why possibly novel:** A quantified supervision-type crossover criterion is UNVERIFIED - needs lit search.
- **Minimal experiment:** On matting datasets with true alpha, threshold alphas into binary labels at various entropy levels, train matched models, locate the crossover.
- **Main risk:** Threshold may be architecture-dependent; test across 3 model families.
- **Mutated from:** W2-A-0016

### W2-A-0136 - Train on disagreement maps directly: predicting WHERE annotators disagree transfers across datasets better than predicting masks.

- **Problem:** Annotator disagreement is discarded as noise, but disagreement structure (what confuses humans) may be a more universal, transferable target than any single mask convention.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a model trained to predict inter-annotator disagreement maps on one dataset predicts disagreement on unseen datasets and unseen classes better than mask-trained models' uncertainty predicts either - ambiguity is a more domain-invariant signal than object identity.
- **Why important:** A transferable ambiguity detector has universal uses: annotation routing, evaluation weighting, and safe-deployment gating - one model serving all segmentation efforts.
- **Why possibly novel:** Disagreement as the primary (not auxiliary) prediction target with cross-dataset transfer claims is UNVERIFIED - needs lit search.
- **Minimal experiment:** Use multi-annotator datasets (LVIS/LIDC/COD multi-rater subsets), train disagreement predictor, test zero-shot on held-out multi-rater sets.
- **Main risk:** Disagreement conflates stimulus ambiguity with protocol/skill differences; needs dataset-effect controls.
- **Mutated from:** W2-A-0051

### W2-A-0137 - Camouflage needs global context more than saliency does: context-radius sweeps as a signature that separates the two tasks computationally.

- **Problem:** Whether COD is locally solvable (texture anomaly) or requires scene-level reasoning (what background SHOULD look like here) determines correct architectures - but no one has measured the context-requirement curve.
- **Core hypothesis (falsifiable):** HYPOTHESIS: COD accuracy grows with input context radius much longer than SOD accuracy does (context saturation at ~2x object size for SOD vs >8x for COD), because detecting background-matching requires modeling background statistics far from the object - a measurable computational signature of the task's structure.
- **Why important:** Context curves are architecture-independent task descriptors that tell designers what receptive fields are actually necessary.
- **Why possibly novel:** Comparative context-requirement curves across SOD/COD are UNVERIFIED - needs lit search.
- **Minimal experiment:** Crop-radius sweep evaluation of matched models on SOD and COD datasets, plot accuracy-vs-context curves.
- **Main risk:** Crop-based context control confounds resolution; use masking-based context control too.
- **Mutated from:** W2-A-0080

### W2-A-0138 - Cross-domain camouflage: does COD pretraining transfer to isointense lesion detection in medical images?

- **Problem:** Isointense tumors (same intensity as surrounding tissue) are literally camouflaged anatomy. Whether camouflage-breaking skills learned on animals transfer to medical camouflage would reveal if COD models learn generalizable 'subtle-difference amplification'.
- **Core hypothesis (falsifiable):** HYPOTHESIS: COD-pretrained models fine-tune to isointense-lesion segmentation with significantly less medical data than generic-pretrained models (positive transfer of camouflage-breaking), and the transferred capability localizes to texture-discrepancy feature channels identifiable by ablation.
- **Why important:** Would establish camouflage-breaking as a portable capability and give medical imaging a new pretraining source; negative result equally informative about COD's true content.
- **Why possibly novel:** COD-to-medical transfer study is UNVERIFIED - needs lit search.
- **Minimal experiment:** Fine-tune COD-pretrained vs ImageNet/DINO-pretrained models on low-contrast liver/brain lesion sets across data-budget ladder.
- **Main risk:** Modality gap may swamp task-similarity benefits; include modality-adapted controls.

### W2-A-0139 - COD models lack inhibition-of-return: they find one instance and stop, missing conspecific groups - measure multi-instance recall collapse.

- **Problem:** Camouflaged animals often occur in groups, but COD models (and datasets) are single-instance biased; sequential search behavior (find, inhibit, continue) has no model analogue.
- **Core hypothesis (falsifiable):** HYPOTHESIS: on multi-instance camouflage scenes, per-instance recall for the 2nd..Nth instances drops steeply conditional on finding the 1st (models' spatial attention collapses onto the found instance), while human searchers show much flatter conditional recall - a measurable architectural deficit in iterative search.
- **Why important:** Wildlife population surveys (the main COD application) require counting, not detecting one; conditional-recall metrics expose the real gap.
- **Why possibly novel:** Conditional multi-instance recall analysis for COD is UNVERIFIED - needs lit search.
- **Minimal experiment:** Composite calibrated multi-instance scenes + real herd/flock camera-trap images, measure conditional recall curves for models and humans.
- **Main risk:** Compositing realism; camera-trap GT requires expert annotation.
- **Mutated from:** W2-A-0127

### W2-A-0140 - Compression halos leak object boundaries in COD datasets: an artifact audit of whether benchmarks are accidentally easy.

- **Problem:** JPEG compression creates ringing/blocking artifacts that differ between smooth animal bodies and textured backgrounds, potentially outlining 'camouflaged' objects with machine-visible halos.
- **Core hypothesis (falsifiable):** HYPOTHESIS: COD datasets contain compression-artifact gradients along object boundaries detectable by simple filters, models exploit them (performance drops on re-compressed or raw-recaptured versions), and artifact strength correlates with reported per-image accuracy - part of COD performance is compression forensics.
- **Why important:** Determines whether benchmark difficulty is real; parallels found in deepfake detection where compression artifacts dominated (KNOWN phenomenon in that field).
- **Why possibly novel:** Compression-forensic audit of COD specifically is UNVERIFIED - needs lit search.
- **Minimal experiment:** Measure boundary-aligned artifact energy across COD datasets; re-evaluate models on artifact-normalized versions.
- **Main risk:** Re-compression changes many things at once; include artifact-matched control regions.
- **Mutated from:** W2-A-0132

### W2-A-0141 - Humans improve on camouflage with viewing time; models are anytime-flat: the missing iterative-inference dimension.

- **Problem:** Human camouflage-breaking is a temporal process (seconds of scrutiny), while feedforward models emit one answer. Whether iterative computation (recurrence, diffusion steps, TTA loops) recovers the human time-accuracy curve shape is unexplored.
- **Core hypothesis (falsifiable):** HYPOTHESIS: model families with iterative inference show accuracy-vs-compute curves qualitatively matching human time-accuracy curves on COD (log-linear gains), while feedforward models are flat - and the iterative gains concentrate on exactly the images where humans need long viewing, suggesting shared computational structure in the search process.
- **Why important:** Connects camouflage perception to a concrete computational property (iterative refinement) with architecture-agnostic evidence.
- **Why possibly novel:** Time-accuracy curve matching between humans and iterative models on COD is UNVERIFIED - needs lit search.
- **Minimal experiment:** Collect human time-accuracy data (masked-exposure protocol); run diffusion/recurrent segmenters at varying step counts; compare curve families per image.
- **Main risk:** Curve similarity is weak evidence for mechanism sharing; frame claims carefully.
- **Mutated from:** W2-A-0126

### W2-A-0142 - Background-statistics complexity predicts COD difficulty better than any object property: difficulty lives in the scene, not the animal.

- **Problem:** COD difficulty is intuitively attributed to the animal's camouflage quality, but the background's statistical richness (how many plausible hiding textures it offers) may dominate.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-image model error is predicted more strongly by background texture-diversity statistics (entropy of local texture descriptors) than by object-side features (size, contrast, edge density), and manipulating backgrounds alone (same animal composited into richer scenes) moves difficulty as predicted - difficulty is a scene property.
- **Why important:** Difficulty prediction from unlabeled scenes enables dataset design, active collection, and deployment risk maps (which habitats defeat detection).
- **Why possibly novel:** Scene-side difficulty attribution with compositing causality is UNVERIFIED - needs lit search.
- **Minimal experiment:** Regress errors on scene vs object features across COD datasets; run compositing intervention study.
- **Main risk:** Compositing artifacts alter difficulty independently; needs artifact-controlled composites.

### W2-A-0143 - Part-level ambiguity in camouflage: where the animal ends and the mimicked substrate begins is sometimes objectively undecidable - propose decision-theoretic annotation.

- **Problem:** A stick insect's legs against twigs create regions where even experts cannot delimit the boundary (occlusion + mimicry). Forcing binary annotation there manufactures noise that training and evaluation both inherit.
- **Core hypothesis (falsifiable):** HYPOTHESIS: expert annotators given an explicit 'undecidable' label option use it on a stable, reproducible subset of pixels (high inter-expert agreement on WHERE decisions are impossible), and excluding those regions from training improves model performance on the decidable majority - undecidability is itself reliably annotatable.
- **Why important:** Introduces a third label state with measurable reliability, applicable to every ambiguity-heavy domain (medical margins, smoke edges).
- **Why possibly novel:** Reproducibility measurement of explicit undecidability annotation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Three-state re-annotation of 300 hard COD images by 5 experts, measure agreement on the undecidable state, retrain with exclusion masks.
- **Main risk:** Annotators may use the escape hatch inconsistently without strict protocol; instructions design is critical.
- **Mutated from:** W2-A-0118

### W2-A-0144 - Eulerian micro-motion amplification as COD preprocessing: breathing and heartbeat make hidden animals visible to ordinary segmenters.

- **Problem:** Living camouflaged animals exhibit involuntary micro-motions invisible per-frame. Motion amplification could convert the temporal signal into spatial signal that any static model can use - untested as a COD pipeline.
- **Core hypothesis (falsifiable):** HYPOTHESIS: applying temporal motion amplification to static-camera clips converts a substantial fraction of model-undetectable camouflaged animals into detectable ones at fixed false-positive rate, with gains concentrated on live-and-still subjects (validating the biological mechanism).
- **Why important:** A cheap, model-agnostic capability jump for wildlife monitoring and search applications, grounded in a physical signal orthogonal to appearance.
- **Why possibly novel:** Motion-magnification preprocessing for COD is UNVERIFIED - needs lit search (magnification itself is KNOWN: Eulerian Video Magnification, Wu et al. 2012).
- **Minimal experiment:** Fixed-camera wildlife clips with hidden animals: run detection with and without amplification preprocessing at matched FPR.
- **Main risk:** Wind-driven vegetation motion amplifies too; needs frequency-band selection tuned to biological motion.
- **Mutated from:** W2-A-0042

### W2-A-0145 - Findability bias: COD datasets contain only camouflage that FAILED (someone photographed it) - true camouflage performance is unbounded above benchmarks.

- **Problem:** Every COD image exists because a human found the animal. Camouflage that succeeds is systematically absent from data, meaning benchmarks sample the easy tail of the true distribution - an unmeasurable-seeming selection bias that can actually be bounded.
- **Core hypothesis (falsifiable):** HYPOTHESIS: using camera-trap archives where animal presence is known independently (telemetry-collared animals, baited sites with activity logs), the recall of both humans and models on 'present-but-unphotographable' cases is drastically lower than benchmark numbers - and the gap (findability bias magnitude) can be estimated quantitatively for the first time.
- **Why important:** All COD performance claims inherit this bias; measuring it converts an epistemological worry into a correction factor for real-world deployment planning.
- **Why possibly novel:** Independent-presence-verified COD evaluation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Partner with ecology telemetry datasets: sample camera-trap frames where collar GPS confirms in-view presence, measure detection rates vs standard benchmarks.
- **Main risk:** GPS-to-camera-frame alignment uncertainty; requires ecology collaboration and careful geometry.

### W2-A-0146 - Boundary-gradient-direction statistics separate camouflaged from conspicuous objects: a low-level signature of camouflage strategy.

- **Problem:** Camouflaged boundaries should have systematically weaker and differently-oriented image gradients than normal object boundaries, but this low-level statistical characterization of camouflage has not been built - it could ground difficulty measures and detection priors in measurable image structure.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the joint distribution of (gradient magnitude, gradient-to-boundary-normal angle) along GT boundaries cleanly separates camouflaged from conspicuous objects, and the separation axis predicts per-object model failure better than global contrast measures - camouflage has a quantitative boundary signature.
- **Why important:** Provides an image-computable camouflage-strength scale (useful for dataset design, difficulty stratification, and even camouflage design/assessment in biology).
- **Why possibly novel:** Boundary-statistics-based camouflage quantification is UNVERIFIED - needs lit search.
- **Minimal experiment:** Compute the joint statistics on COD vs COCO boundaries, train a difficulty predictor, validate against per-object model errors.
- **Main risk:** Statistic may reduce to known contrast measures; the angular component is the novelty bet.
- **Mutated from:** W2-A-0142

### W2-A-0147 - Shadow inconsistency betrays camouflaged objects: texture can mimic, but cast shadows obey geometry that mimicry cannot fake.

- **Problem:** An animal matching background texture still casts a body-shaped shadow inconsistent with flat substrate. Shadow-based camouflage-breaking is documented in biology (countershading counters it) but unused in computational COD.
- **Core hypothesis (falsifiable):** HYPOTHESIS: explicit shadow-geometry analysis (detecting shadow regions inconsistent with local surface relief implied by the rest of the scene) detects a meaningful subset of camouflaged objects that texture-based models miss entirely, and the two detection channels' errors are near-independent (large ensemble gain).
- **Why important:** An orthogonal physical channel with near-independent errors is the most valuable kind of ensemble component for high-stakes search.
- **Why possibly novel:** Shadow-consistency reasoning for COD is UNVERIFIED - needs lit search.
- **Minimal experiment:** Annotate shadow evidence on COD subsets with strong directional light, build shadow-anomaly detector, measure complementary recall.
- **Main risk:** Only works under directional lighting; diffuse-light scenes contribute nothing (operating-envelope caveat).

### W2-A-0148 - Human-AI teaming for camouflage search: model proposals + human verification exceeds either alone, but only if model uncertainty is exposed.

- **Problem:** COD applications are human-in-the-loop (rangers, searchers), yet benchmarks evaluate models solo. Team performance - and what model outputs (masks, heatmaps, uncertainty) maximize it - is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: showing calibrated model heatmaps (not binary masks) roughly doubles human search efficiency on hard camouflage while binary masks INDUCE misses via anchoring (humans stop searching after verifying shown proposals) - output format causally changes team recall, with binary masks the worst choice despite being the field's standard output.
- **Why important:** The deliverable format question affects every deployed search system; anchoring-induced misses are a safety-relevant human-factors failure invisible to model-only evaluation.
- **Why possibly novel:** Output-format causal study for camouflage search teaming is UNVERIFIED - needs lit search.
- **Minimal experiment:** Controlled search study (N=30) with format conditions (none/mask/heatmap/uncertainty), measure team recall, time, and anchoring miss rates.
- **Main risk:** Human-subject logistics; effects may depend on searcher expertise (recruit both novices and experts).
- **Mutated from:** W2-A-0126

### W2-A-0149 - Model-specific worst-case camouflage synthesis: use texture generation to find each model's blind spots and test whether blindness transfers.

- **Problem:** COD evaluates on nature's camouflage, but each model has its own worst-case textures. Whether adversarially-synthesized camouflage transfers across models would reveal if camouflage vulnerability is architectural or universal.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-model optimized camouflage textures (differentiable rendering of object surface texture against fixed backgrounds) reduce that model's detection to near zero while remaining human-detectable, and transfer across model families at rates well below adversarial-perturbation transfer - camouflage blind spots are model-specific, unlike pixel-attack vulnerability.
- **Why important:** Maps the difference between perceptual camouflage (universal) and model camouflage (idiosyncratic), with defense implications for anyone relying on automated detection.
- **Why possibly novel:** Cross-model transferability analysis of synthesized 3D-consistent camouflage is UNVERIFIED - needs lit search (adversarial texture work is KNOWN, e.g. adversarial patches/clothing).
- **Minimal experiment:** Optimize textures against 3 detector families in simulation, cross-evaluate the transfer matrix, verify human-visibility with a small study.
- **Main risk:** Simulation-optimized textures may not survive real rendering conditions; physical validation is a larger follow-up.

### W2-A-0150 - Ambiguous boundaries drift with image resolution: the same object gets objectively different 'correct' boundaries at different scales - boundary GT is scale-relative.

- **Problem:** A fuzzy boundary annotated at 4K differs from the same boundary annotated at 512px, not by error but by information availability. Datasets mix annotation scales silently, and evaluation assumes scale-absolute GT.
- **Core hypothesis (falsifiable):** HYPOTHESIS: annotator boundary placement on ambiguous edges shifts systematically (not just noisily) with viewing resolution - a measurable scale-dependent bias field - and models trained on mixed-resolution annotations learn an average boundary that is optimal at NO resolution, degrading boundary metrics at every scale.
- **Why important:** Establishes that boundary ground truth is scale-relative, forcing resolution metadata into annotation protocols and scale-conditional evaluation - a foundational correction for boundary research.
- **Why possibly novel:** Scale-relativity of boundary annotation as a measured phenomenon is UNVERIFIED - needs lit search.
- **Minimal experiment:** Have annotators label identical fuzzy boundaries at 4 zoom levels (order-randomized), quantify systematic placement shifts vs noise.
- **Main risk:** Zoom interfaces confound with interaction affordances (brush size); strict interface control needed.
- **Mutated from:** W2-A-0118

## C07-boundary-small-objects

### W2-A-0151 - Three-way boundary error decomposition: how much reported boundary error is model, annotation, or metric artifact?

- **Problem:** Boundary metrics lump together model mislocalization, annotation imprecision, and rasterization/metric artifacts; the field optimizes the sum without knowing its composition.
- **Core hypothesis (falsifiable):** HYPOTHESIS: on standard benchmarks, at least half of measured boundary error within 3px of GT is attributable to annotation imprecision and rasterization (estimable via multi-annotation and re-rasterization controls), meaning models are closer to the achievable boundary ceiling than metrics suggest and sub-3px 'progress' claims are mostly noise-fitting.
- **Why important:** Recalibrates what boundary improvements are real, and defines the achievable frontier every method should be compared against.
- **Why possibly novel:** A formal decomposition protocol with published per-benchmark error budgets is UNVERIFIED - needs lit search.
- **Minimal experiment:** Multi-annotate 200 object boundaries at high zoom, estimate annotation noise spectra, propagate through metrics, compare against published method deltas.
- **Main risk:** Extrapolating from 200 objects to benchmark-wide claims needs careful sampling design.

### W2-A-0152 - Size-stratified reporting flips leaderboards: mIoU improvements of recent methods concentrate entirely in large objects.

- **Problem:** mIoU weights pixels, so large objects dominate; two methods with equal mIoU can differ enormously on small objects, and progress claims may hide small-object stagnation.
- **Core hypothesis (falsifiable):** HYPOTHESIS: re-scoring the last 5 years of leading semantic/panoptic methods with size-stratified metrics shows near-zero progress in the smallest object decile (progress has been large-object progress), and ranking inversions occur for a substantial fraction of published comparisons.
- **Why important:** If small-object performance has been flat while headlines improved, the field has been optimizing a metric artifact - a meta-finding that redirects evaluation practice.
- **Why possibly novel:** Longitudinal size-stratified meta-analysis of published models is UNVERIFIED - needs lit search.
- **Minimal experiment:** Download 10 public checkpoints spanning 5 years, evaluate size-stratified on ADE20K/Cityscapes, plot per-decile progress curves.
- **Main risk:** Checkpoint availability and preprocessing comparability; must reproduce official numbers first.

### W2-A-0153 - The upsampling ceiling: bilinear decoder interpolation imposes a hard boundary-sharpness floor that no training can cross.

- **Problem:** Virtually all decoders upsample coarse features with smooth interpolation; this architecturally bounds achievable boundary sharpness, but the bound has never been computed and compared with observed errors.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for each common decoder design, there is a computable minimum boundary transition width (from the interpolation kernel and feature stride), observed model boundaries sit AT this floor (not above it), and boundary-error differences between published methods largely reduce to their upsampling-path differences - training and losses are second-order for sharpness.
- **Why important:** Would reduce a confusing literature of boundary methods to an analyzable signal-processing property, telling designers exactly where sharpness comes from.
- **Why possibly novel:** Analytic sharpness-floor computation validated against model zoo behavior is UNVERIFIED - needs lit search.
- **Minimal experiment:** Derive floors for 5 decoder designs, measure boundary transition widths of corresponding checkpoints on step-edge probes, test floor-attainment.
- **Main risk:** Learned upsampling components complicate the analysis; treat them as measurable empirical kernels.

### W2-A-0154 - Thin structures break at regular intervals set by feature stride: connectivity failure is periodic, not random.

- **Problem:** Segmented wires, branches, and vessels show gaps. If gaps are periodic (aligned with stride/receptive-field geometry) rather than random, the failure is architectural aliasing with a specific signature and fix path.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the autocorrelation of gap positions along thin structures shows peaks at multiples of the effective feature stride across architectures, and gap probability depends on the structure's sub-stride phase - connectivity failure is deterministic aliasing, falsifiable by phase-shifted re-inference reducing gaps.
- **Why important:** Periodic failure implies cheap test-time fixes (phase ensembling) and indicts stride design rather than data or capacity for a classical failure mode.
- **Why possibly novel:** Gap-periodicity forensics on thin-structure segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Segment synthetic and real thin structures, compute gap-position autocorrelation vs stride, test phase-jitter ensembling.
- **Main risk:** Multiple strides in pyramidal models blur the periodicity; analyze per-scale contributions.
- **Mutated from:** W2-A-0003

### W2-A-0155 - Which boundary errors do humans actually notice? Build the perceptual boundary metric from discrimination experiments.

- **Problem:** Boundary metrics (BF-score, boundary IoU) weight all deviations equally, but human observers notice some errors (corner cutting, protrusion loss) far more than others (smooth in/out breathing) - the perceptual weighting is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: human detection thresholds for boundary deviations vary by an order of magnitude across error types (systematic offsets vs high-frequency wiggle vs feature deletion), and a perceptually-weighted metric built from measured thresholds predicts human quality judgments far better than existing boundary metrics - which misrank a meaningful share of comparisons.
- **Why important:** Boundary quality ultimately serves human consumers (editors, clinicians); a psychophysically-grounded metric would reset how boundary progress is scored.
- **Why possibly novel:** Threshold-measurement-based metric construction for segmentation boundaries is UNVERIFIED - needs lit search.
- **Minimal experiment:** 2AFC discrimination study over parameterized boundary distortions, fit threshold model, validate on preference prediction of real model outputs.
- **Main risk:** Perceptual weights may be task-dependent (editing vs measuring); collect per use case.
- **Mutated from:** W2-A-0091

### W2-A-0156 - Polygon-vs-pixel ground truth is a hidden treatment: rasterization conventions systematically bias boundary supervision across datasets.

- **Problem:** Masks originate as polygons (COCO), brush strokes, or pixel labels, each with different rasterization and corner behavior; models trained across datasets inherit conflicting micro-boundary conventions.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a classifier can identify a mask's annotation tool from boundary micro-statistics alone with high accuracy (tool fingerprints exist), and cross-dataset boundary-metric gaps shrink measurably after fingerprint-normalizing GT - part of 'domain gap' in boundary quality is tooling, not imagery.
- **Why important:** Identifies an ignored confounder in every cross-dataset boundary comparison and offers a normalization remedy.
- **Why possibly novel:** Annotation-tool fingerprint forensics on mask boundaries is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train tool classifier on masks from datasets with known tooling, apply cross-dataset, re-evaluate transfer gaps after harmonizing rasterization.
- **Main risk:** Tool and content are confounded across datasets; validate fingerprints on same-content multi-tool annotations.

### W2-A-0157 - For small objects, context carries most of the information: measure the interior-vs-context information ratio as a function of object size.

- **Problem:** Small objects have few interior pixels; recognition may rest almost entirely on context. The interior/context information balance as a function of size has not been quantified, though it dictates correct architecture and augmentation choices.
- **Core hypothesis (falsifiable):** HYPOTHESIS: masking object interiors reduces small-object segmentation accuracy by far less than masking equivalent context rings, with the interior contribution rising steeply above ~32px - a measurable crossover implying sub-crossover objects are 'context-defined' and interior-focused methods are wasted on them.
- **Why important:** Explains why small-object performance resists resolution increases in some regimes, and quantifies exactly what supervision small objects need.
- **Why possibly novel:** Size-conditional information-source decomposition is UNVERIFIED - needs lit search.
- **Minimal experiment:** Interior/context masking sweeps across object-size bins on COCO/LVIS, plot information-ratio curves per class family.
- **Main risk:** Masking artifacts; use multiple fill strategies and report agreement.
- **Mutated from:** W2-A-0080

### W2-A-0158 - GPU-budget-matched showdown: high-resolution crops vs bigger models for small-object segmentation.

- **Problem:** Two competing recipes claim small-object gains - spend compute on resolution (crops, tiling) or on capacity (larger backbones). They are never compared at matched total compute, so the field lacks an exchange rate.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at matched training+inference FLOPs, resolution investment dominates capacity investment for objects below ~2% image area (with a measurable crossover size), and the advantage compounds under domain shift because resolution gains are shift-invariant while capacity gains partially memorize.
- **Why important:** An exchange-rate law between resolution and capacity would guide every deployment with small objects (aerial, medical, defect inspection).
- **Why possibly novel:** Budget-matched resolution-vs-capacity frontier for dense prediction is UNVERIFIED - needs lit search.
- **Minimal experiment:** Grid of (resolution, model size) at fixed FLOP budgets on aerial + medical datasets, map iso-compute performance contours vs object size.
- **Main risk:** Conclusions may be architecture-family-specific; replicate across CNN and ViT families.

### W2-A-0159 - Optimal polygon click budget allocation: where should an annotator spend the next vertex for maximal mask fidelity?

- **Problem:** Polygon annotation spends vertices uniformly or by habit, but boundary information density varies enormously along contours (corners vs straight runs); the optimal allocation policy and its savings are unknown.
- **Core hypothesis (falsifiable):** HYPOTHESIS: curvature-adaptive vertex allocation achieves target boundary fidelity with 30-50% fewer clicks than uniform or annotator-natural allocation (measurable on re-annotation studies), and existing dataset polygons are far from the efficient frontier - quantifying wasted annotation spend at ecosystem scale.
- **Why important:** Annotation budgets are the binding constraint on dataset scale; a proven allocation policy converts directly into more labeled data per dollar.
- **Why possibly novel:** Information-theoretic vertex-allocation analysis of real datasets is UNVERIFIED - needs lit search.
- **Minimal experiment:** Compute fidelity-vs-vertex-count curves for optimal (dynamic programming on GT contours) vs actual COCO polygons; run small human study with guided placement.
- **Main risk:** Human motor/attention costs may not follow vertex-count economics; the human study is the decisive leg.

### W2-A-0160 - Per-class signed boundary bias: models systematically over- or under-segment each class by a constant offset that morphological recalibration removes.

- **Problem:** Boundary error is reported as unsigned distance, hiding a possible constant signed bias per class (e.g. 'person' always 2px eroded, 'sky' always dilated) that would be trivially correctable if measured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a large fraction of per-class boundary error is a constant signed offset (bias, not variance) stable across images and datasets for a given model - and per-class morphological recalibration (single dilation/erosion parameter fitted on validation) recovers a large share of boundary-metric error at zero architecture cost.
- **Why important:** Free accuracy lying on the table for every deployed model, plus a diagnostic separating systematic from stochastic boundary behavior.
- **Why possibly novel:** Signed-bias decomposition with recalibration accounting is UNVERIFIED - needs lit search.
- **Minimal experiment:** Measure per-class signed boundary offsets for 5 public models, fit recalibration on val, report test boundary-metric recovery.
- **Main risk:** Bias may vary with object scale/context, making constant-offset correction too crude - measure the residual structure.

### W2-A-0161 - Corners are the hardest pixels: boundary error grows superlinearly with local curvature, exposing decoders as low-pass shape filters.

- **Problem:** Errors concentrate at high-curvature boundary features (fingertips, leaf tips, corners), consistent with spectral bias, but the error-vs-curvature law and its architecture dependence have not been established.
- **Core hypothesis (falsifiable):** HYPOTHESIS: boundary displacement error grows superlinearly with local GT curvature, with an architecture-specific cutoff frequency measurable from the error spectrum - CNNs and ViTs show different cutoff signatures, and the cutoff predicts performance on curvature-heavy domains (text, machinery, foliage) better than aggregate metrics.
- **Why important:** A transferable spectral characterization of decoders enables domain-model matching from first principles (measure domain curvature spectrum, pick decoder with adequate cutoff).
- **Why possibly novel:** Curvature-resolved error laws with spectral cutoffs are UNVERIFIED - needs lit search.
- **Minimal experiment:** Bin boundary errors by local curvature across model zoo and datasets, fit error-vs-curvature laws, extract cutoffs, validate domain-matching predictions.
- **Main risk:** Curvature estimation on noisy GT is delicate; use analytically-known synthetic shapes as anchors.
- **Mutated from:** W2-A-0153

### W2-A-0162 - Uncertainty glint: tiny objects announce themselves as anomalous uncertainty texture even when the class prediction misses them entirely.

- **Problem:** Small objects below the detection threshold often leave no trace in hard predictions, but they may perturb the model's uncertainty/feature maps in a detectable way - a second-channel signal for recall recovery.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at locations of missed small objects, per-pixel predictive-entropy neighborhoods have statistically distinct texture (localized entropy spikes) relative to matched background, supporting a recall-recovery detector that finds a meaningful fraction of misses at low false-positive cost - the model 'flinches' where it cannot 'see'.
- **Why important:** Missed small objects are the costliest errors in screening applications; harvesting sub-threshold evidence directly attacks the recall frontier.
- **Why possibly novel:** Uncertainty-texture mining for sub-threshold objects is UNVERIFIED - needs lit search.
- **Minimal experiment:** On LVIS/aerial datasets, extract entropy-map patches at missed-object locations vs matched negatives, train shallow detector, report recall-at-FPR added.
- **Main risk:** Entropy spikes also occur at texture boundaries; the discriminator must beat that base rate.

### W2-A-0163 - Stuff-stuff boundaries are measure-zero fictions: grass-to-sidewalk transitions are physically bands, and the label model should say so.

- **Problem:** Between stuff classes (grass/dirt, sand/water) there is often a mixed transition band, not a curve. Datasets draw arbitrary curves through the band, and models are penalized for reasonable placements within it.
- **Core hypothesis (falsifiable):** HYPOTHESIS: annotator agreement within stuff-stuff transition bands is near chance (band placement is arbitrary), band widths are measurable and class-pair-specific, and introducing band-aware evaluation (no penalty within measured band) changes stuff-class rankings while leaving thing-class rankings intact - showing current stuff boundary scores are substantially noise.
- **Why important:** Stuff classes dominate scene area; noise-driven rankings there corrupt aggregate metrics that guide the field.
- **Why possibly novel:** Transition-band measurement and band-aware evaluation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Multi-annotate stuff transitions on ADE/Cityscapes subsets, measure band widths, re-score public models band-aware.
- **Main risk:** Some stuff transitions ARE sharp (curb edges); the method must classify band vs edge cases first.
- **Mutated from:** W2-A-0118

### W2-A-0164 - Below the annotation noise floor: SOTA claims on tiny-object benchmarks assert precision the labels cannot support.

- **Problem:** For an 8px object, a 1px annotation error swings IoU by tens of points. Benchmarks report tiny-object metrics to decimals without computing the label-noise floor, so some published gains are unfalsifiable.
- **Core hypothesis (falsifiable):** HYPOTHESIS: propagating measured annotation position noise through IoU for small size bins yields uncertainty intervals wider than most published method-to-method gaps in those bins - a decisive fraction of tiny-object SOTA claims are statistically vacuous, and the community's smallest evaluable object size is derivable per dataset.
- **Why important:** Defines the epistemic limit of small-object benchmarking and prevents wasted effort chasing noise.
- **Why possibly novel:** Noise-floor-derived minimum-evaluable-size analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Estimate annotation jitter from double-labeled subsets, Monte-Carlo propagate through size-binned metrics, overlay published deltas.
- **Main risk:** Jitter estimates from small double-labeled samples have their own uncertainty; report meta-intervals.
- **Mutated from:** W2-A-0151

### W2-A-0165 - Sub-stride phase determines tiny-object visibility: shifting the image by 8 pixels changes which small objects a model finds.

- **Problem:** Feature-map stride quantizes where evidence lands; a tiny object's alignment with the stride grid (its phase) may decide detection - implying single-pass evaluation undercounts model capability and phase-TTA recovers it.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-object detection outcomes for sub-stride objects flip with input translation at rates far above large-object rates (phase sensitivity), aggregate phase-averaged recall exceeds single-phase recall substantially, and phase sensitivity per architecture is predictable from its stride pyramid - a deterministic, correctable component of small-object failure.
- **Why important:** Distinguishes 'cannot represent' from 'unlucky alignment', with an immediately usable inference fix and a design principle (anti-aliased strides) validated by the phase signature.
- **Why possibly novel:** Systematic phase-sensitivity accounting for small-object segmentation is UNVERIFIED - needs lit search (shift-variance of CNNs in general is KNOWN).
- **Minimal experiment:** Translate test images over a stride-period grid, measure per-object outcome flip rates by size, evaluate phase-ensembled recall.
- **Main risk:** Border effects from translation; use central-crop evaluation regions.
- **Mutated from:** W2-A-0154

### W2-A-0166 - Shadow edges poison boundary supervision: models trained with gradient-aligned boundary rewards learn to follow illumination, not objects.

- **Problem:** Many pipelines sharpen boundaries using image gradients (CRF-style refinement, edge-guided training). Shadow edges are strong gradients that do not bound objects; the systematic confusion rate this induces is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: models with gradient-coupled boundary refinement place object boundaries onto shadow edges at measurably higher rates than gradient-free models (a shadow-following bias), and the bias grows with refinement strength - quantifying a hidden cost of a ubiquitous technique and predicting its failure in harsh-light domains (aerial noon imagery, surgical lighting).
- **Why important:** CRF/edge-guidance is folklore-good; measuring its shadow tax would qualify decades of accepted practice with domain-specific guidance.
- **Why possibly novel:** Shadow-specific failure accounting of gradient-based refinement is UNVERIFIED - needs lit search.
- **Minimal experiment:** Curate shadow-crossing object boundaries, compare boundary placement of refined vs unrefined variants of the same models, sweep refinement strength.
- **Main risk:** Isolating refinement as the only difference requires careful model surgery; use toggleable refinement implementations.
- **Mutated from:** W2-A-0006

### W2-A-0167 - Hairline cracks defeat both training and evaluation: 1-pixel objects need sub-pixel offset-field formulations, not masks.

- **Problem:** Infrastructure cracks, cell membranes, and hairline defects are ~1px structures where binary masks cannot even represent the target faithfully, yet the field forces mask formulations onto them.
- **Core hypothesis (falsifiable):** HYPOTHESIS: representing thin structures as sub-pixel center-line + width fields (continuous offsets) instead of binary masks improves BOTH detection recall and downstream measurement accuracy (crack width estimation) at matched supervision cost, because the continuous formulation matches the object's actual dimensionality - falsifiable by direct formulation comparison.
- **Why important:** Thin-structure measurement is an economically huge application (infrastructure inspection) currently served by a mismatched formulation.
- **Why possibly novel:** KNOWN: center-line representations exist in vessel literature; the sub-pixel measurement-accuracy comparison against mask formulations at matched supervision is UNVERIFIED - needs lit search.
- **Minimal experiment:** On crack datasets with caliper-measured widths, train mask vs offset-field formulations, compare detection and physical-measurement error.
- **Main risk:** Requires physically-measured GT (width calipers); small but real collection effort.

### W2-A-0168 - Depth-of-field is a per-pixel boundary-sharpness oracle that models ignore: defocused boundaries deserve wide predictions, focused ones sharp.

- **Problem:** Within one photo, optical defocus varies boundary sharpness continuously, but models emit uniform-sharpness boundaries everywhere - a mismatch between optics and output that nobody exploits or measures.
- **Core hypothesis (falsifiable):** HYPOTHESIS: model boundary error correlates strongly with local defocus (measurable via blur estimation), models do NOT modulate their boundary confidence with defocus (uniform sharpness output), and defocus-conditioned evaluation reveals current boundary metrics penalize physically-inevitable uncertainty as if it were model error.
- **Why important:** Separates optical information limits from model limits per pixel, enabling fairer evaluation and defocus-aware outputs for editing applications.
- **Why possibly novel:** Defocus-conditioned boundary analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Estimate local blur on benchmark images, bin boundary errors by blur level, test whether model confidence tracks blur.
- **Main risk:** Blur estimation errors propagate; use focal-stack captures with known defocus as calibration.

### W2-A-0169 - Contour-domain error autocorrelation reveals each decoder's effective receptive field along boundaries - a fingerprint measurable without internals.

- **Problem:** How far boundary errors correlate ALONG the contour (error wavelength) encodes the decoder's spatial coupling, but boundary evaluation collapses everything to scalars, discarding this diagnostic structure.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the autocorrelation length of signed boundary error along contours is a stable architecture fingerprint (invariant across datasets, distinct across model families), predicts which post-processing helps (short-wavelength errors respond to smoothing, long-wavelength to re-recognition), and can identify anonymous model families from outputs alone.
- **Why important:** Gives practitioners a black-box diagnostic that prescribes the right fix, and gives forensics a model-attribution tool.
- **Why possibly novel:** Contour-frequency-domain error analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Compute along-contour error spectra for 8 public models over 3 datasets, test cross-dataset stability and family separability.
- **Main risk:** Contour parameterization ambiguities at junctions; restrict to simple closed contours initially.
- **Mutated from:** W2-A-0161

### W2-A-0170 - Upstream JPEG kills small objects before the model ever sees them: pipeline compression bounds recall independent of model quality.

- **Problem:** Data pipelines (dashcams, drones, cloud upload) compress images before inference; tiny low-contrast objects may be erased at the compression stage, making model improvements irrelevant - yet compression is absent from benchmark methodology.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for objects under ~12px, realistic pipeline compression (bitrates of deployed dashcams/drones) removes recoverable evidence for a large fraction of instances (verified by human inspection of decompressed crops), establishing a compression-determined recall ceiling that no model surpasses - and benchmark images, being lightly compressed, systematically overstate deployable recall.
- **Why important:** Redirects small-object investment toward capture/codec policy where the recall is actually lost, with quantitative ceilings per bitrate.
- **Why possibly novel:** Compression-ceiling accounting for small-object segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Re-compress benchmarks at deployment bitrates, measure model + human recall ceilings vs original, tabulate evidence destruction per size bin.
- **Main risk:** Codec diversity (H.264/H.265/AV1) requires a matrix, not a single number.

### W2-A-0171 - Attribute the small-object gap: with oracle localization, is segmentation of small objects actually solved?

- **Problem:** Small-object segmentation failure conflates finding (localization) and delineating (mask quality). The conditional performance - mask quality GIVEN correct localization - isolates which stage fails.
- **Core hypothesis (falsifiable):** HYPOTHESIS: conditioned on oracle boxes, small-object mask quality is close to large-object mask quality (normalized for pixel count), so the small-object problem is >80% a search/detection problem, not a segmentation problem - implying segmentation-architecture work on small objects is largely misdirected.
- **Why important:** Cleanly splits a conflated problem and reallocates effort to the failing stage (search strategies, high-recall proposals).
- **Why possibly novel:** Stage-conditional gap attribution for small objects is UNVERIFIED - needs lit search.
- **Minimal experiment:** Evaluate promptable and two-stage models with GT-box prompts across size bins, compare conditional mask quality profiles.
- **Main risk:** Normalizing mask quality across sizes is subtle (IoU size-sensitivity); use boundary-normalized metrics.
- **Mutated from:** W2-A-0015

### W2-A-0172 - Decompose boundary uncertainty into normal and tangential components: only normal errors matter, and metrics that mix them misrank methods.

- **Problem:** Boundary deviations perpendicular to the contour (position error) change the region; deviations along it (parameterization wiggle) often do not matter - yet distance-based boundary metrics penalize both indiscriminately.
- **Core hypothesis (falsifiable):** HYPOTHESIS: decomposing boundary error into normal/tangential components shows the tangential component contributes substantial metric variance while being nearly uncorrelated with human quality judgments and downstream task success - normal-only metrics agree better with both, and re-scoring benchmarks with them changes method orderings.
- **Why important:** A geometrically-principled metric correction that removes a systematic noise source from all boundary evaluation.
- **Why possibly novel:** Normal/tangential decomposition for segmentation evaluation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Implement decomposed metrics, re-score model zoo, correlate both components with human preferences from a small study.
- **Main risk:** Correspondence between predicted and GT contours is ambiguous at large errors; define robust matching first.
- **Mutated from:** W2-A-0155

### W2-A-0173 - Instance merging obeys a crowding law: adjacent-instance merge probability is a universal function of gap-to-size ratio, like human visual crowding.

- **Problem:** Dense instances (cells, crowds, grapes) get merged by segmenters. If merge probability follows a universal law in dimensionless gap/size units - analogous to crowding in human peripheral vision (KNOWN: Bouma's law) - dense-scene capability could be predicted and compared principledly.
- **Core hypothesis (falsifiable):** HYPOTHESIS: merge probability across models and domains collapses onto a single curve in (gap/object-size, contrast) coordinates with model-specific scale factors - a 'machine Bouma law' - enabling dataset-independent dense-scene capability ratings and principled prediction of failure density in novel domains.
- **Why important:** Universal laws compress messy benchmarks into transferable engineering constants; a crowding constant per model would be a durable, comparable capability spec.
- **Why possibly novel:** Dimensionless-collapse analysis of instance merging is UNVERIFIED - needs lit search.
- **Minimal experiment:** Measure merge rates on synthetic instance grids (controlled gap/size/contrast) plus cell/crowd datasets, test curve collapse across 5 models.
- **Main risk:** Real-scene occlusion patterns may break the two-parameter description; add occlusion fraction as third axis if needed.

### W2-A-0174 - Models have a blob prior: error statistics reveal systematic shape simplification toward compact blobs, measurable as a shape-frequency transfer function.

- **Problem:** Predictions tend toward smoother, rounder shapes than GT, but 'shape simplification' has never been characterized as a transfer function (which shape frequencies are attenuated how much) that would make the bias precisely correctable and comparable.
- **Core hypothesis (falsifiable):** HYPOTHESIS: comparing shape-descriptor spectra (elliptic Fourier coefficients) of predictions vs GT yields a stable per-model attenuation curve (the blob-prior transfer function), consistent across datasets, whose inverse partially restores fine shape structure post hoc - shape bias is a measurable filter, not a vague tendency.
- **Why important:** Converts a folklore bias into an engineering object (measurable, invertible, comparable across models) with direct value for shape-critical applications (typography, machining, biology morphometrics).
- **Why possibly novel:** Transfer-function characterization of segmentation shape bias is UNVERIFIED - needs lit search.
- **Minimal experiment:** Compute EFD spectra ratios prediction/GT per model, verify cross-dataset stability, test spectral re-inflation on held-out data.
- **Main risk:** Inversion amplifies noise along with signal; regularized inversion needed and honest failure reporting.
- **Mutated from:** W2-A-0161

### W2-A-0175 - Photograph printed calibration shapes to get camera-true boundary ground truth with exact sub-pixel geometry - the first zero-annotation boundary benchmark.

- **Problem:** All boundary evaluation inherits annotation noise. Printing precisely-known vector shapes, photographing them under controlled conditions, and registering the known geometry yields ground truth with certainty no annotator can provide - yet no such benchmark exists for segmentation.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a physically-photographed benchmark of exactly-known shapes (varying size, curvature, contrast, blur, texture) will reveal sub-pixel systematic biases of segmentation models (chromatic offsets, contrast-dependent placement, curvature attenuation) that are invisible on annotated data because they are smaller than annotation noise - opening a metrology-grade regime of boundary science.
- **Why important:** Establishes an absolute measurement foundation the entire boundary literature lacks; every sharpness/bias claim becomes precisely testable.
- **Why possibly novel:** Metrology-style physical-ground-truth benchmarks for segmentation are UNVERIFIED - needs lit search (camera calibration targets are KNOWN but serve geometry, not segmentation evaluation).
- **Minimal experiment:** Print vector shape set, photograph across cameras/lighting/scales, register via fiducials, evaluate model zoo at sub-pixel precision.
- **Main risk:** Printed shapes are unnatural stimuli; complement with textured/embedded variants to test ecological validity.
- **Mutated from:** W2-A-0151

## C08-uncertainty-longtail

### W2-A-0176 - Pixel entropy does not predict object-level failure: the granularity mismatch at the heart of segmentation uncertainty.

- **Problem:** Uncertainty is produced per-pixel but consumed per-object (is THIS lesion trustworthy?). Whether pixel-level uncertainty aggregates into valid object-level confidence has not been rigorously tested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: standard aggregations of pixel uncertainty (mean/max entropy over mask) predict object-level errors (misses, hallucinations, gross misshaping) only weakly (AUROC<0.7), because object failures are correlated-error events invisible to independent-pixel statistics - and object-level failure needs its own predictor trained on object-level outcomes.
- **Why important:** Every clinical/industrial consumer needs object-level confidence; if the standard recipe is invalid, the field's uncertainty outputs are decorative.
- **Why possibly novel:** Granularity-mismatch quantification for segmentation uncertainty is UNVERIFIED - needs lit search.
- **Minimal experiment:** On 3 datasets, compute pixel-aggregate vs learned object-level confidence, compare AUROC for object-failure prediction.
- **Main risk:** Learned object-level predictors may overfit failure modes of specific models; test cross-model transfer.

### W2-A-0177 - Calibration degrades before accuracy under distribution shift: miscalibration as an early-warning canary for silent segmentation failure.

- **Problem:** Deployed models fail silently under gradual shift (weather, sensor aging). If calibration metrics degrade earlier along shift gradients than accuracy does, they provide label-free advance warning - the lead-lag relationship is unmeasured for dense prediction.
- **Core hypothesis (falsifiable):** HYPOTHESIS: along parameterized shift ladders (fog density, noise level, geography), expected calibration error inflects at milder shift levels than mIoU does (a measurable lead), and the lead size is consistent enough to define actionable monitoring thresholds - calibration is the canary, not just a companion metric.
- **Why important:** Label-free failure forecasting is the missing piece of deployment monitoring; a validated lead-lag law would be immediately adopted.
- **Why possibly novel:** Lead-lag analysis of calibration vs accuracy under graded shift is UNVERIFIED - needs lit search.
- **Minimal experiment:** Evaluate models along synthetic and natural shift ladders (ACDC severity levels), plot ECE and mIoU inflection points, quantify lead consistency.
- **Main risk:** ECE estimation needs labels too; the deployment version must use proxy calibration signals (agreement-based), adding a validation step.

### W2-A-0178 - Instance count, not pixel count, governs long-tail segmentation: disentangle the two supervision currencies.

- **Problem:** Rare-class performance is attributed to 'few pixels', but classes vary independently in instances-per-class and pixels-per-instance; which currency actually buys performance is confounded in natural datasets.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at matched total pixels, many-small-instances classes substantially outperform few-large-instances classes (instance diversity teaches shape/context variation that pixel volume cannot), with a measurable exchange rate - so long-tail interventions should target instance acquisition, not pixel acquisition.
- **Why important:** Directly changes data-collection strategy for rare classes (many quick examples beat few thorough ones), a high-leverage economics result.
- **Why possibly novel:** Controlled pixel-vs-instance supervision disentanglement is UNVERIFIED - needs lit search.
- **Minimal experiment:** Subsample LVIS classes into matched-pixel/varied-instance and matched-instance/varied-pixel grids, train and compare per-class outcomes.
- **Main risk:** Class semantics confound (small-instance classes differ in kind); use within-class subsampling designs.

### W2-A-0179 - Measure the labeling ROI of uncertainty-routed annotation: does model uncertainty actually direct human effort to where it pays?

- **Problem:** Uncertainty-guided active labeling is widely assumed beneficial, but for segmentation the regions models are uncertain about (boundaries, ambiguous textures) may be exactly where human labels are ALSO noisy - buying little.
- **Core hypothesis (falsifiable):** HYPOTHESIS: routing annotation to high-model-uncertainty regions yields lower marginal model improvement per annotation-hour than routing to high-DISAGREEMENT-between-models regions, because self-uncertainty concentrates on irreducibly ambiguous pixels while cross-model disagreement marks learnable errors - an economics experiment with a counter-intuitive predicted winner.
- **Why important:** Annotation routing policies move real budgets; identifying the right routing signal has direct multiplicative value across the industry.
- **Why possibly novel:** Head-to-head routing-signal comparison measured in Dice-per-hour is UNVERIFIED - needs lit search.
- **Minimal experiment:** Fixed-budget annotation simulation plus small real-annotator study comparing routing signals on a medical and a driving dataset.
- **Main risk:** Results may depend on annotator skill and label noise model; report across annotator pools.
- **Mutated from:** W2-A-0136

### W2-A-0180 - Ensemble disagreement decomposes into boundary jitter vs semantic conflict, and only the second predicts real failure.

- **Problem:** Deep-ensemble disagreement for segmentation mixes two phenomena: small spatial jitter of agreed boundaries, and genuine semantic conflicts (different labels/regions). Treating them as one scalar wastes the signal.
- **Core hypothesis (falsifiable):** HYPOTHESIS: after registering member boundaries (factoring out sub-3px jitter), the residual semantic-conflict component predicts object-level errors and OOD inputs far better than raw disagreement, while the jitter component tracks stimulus edge blur - two useful signals recoverable from one ensemble by simple decomposition.
- **Why important:** Upgrades the most common uncertainty tool for dense prediction at zero training cost, and explains why raw ensemble variance underperforms expectations.
- **Why possibly novel:** Jitter/conflict decomposition of segmentation ensembles is UNVERIFIED - needs lit search.
- **Minimal experiment:** Decompose disagreement for a 5-member ensemble on clean and shifted data, compare failure-prediction AUROC of components vs raw variance.
- **Main risk:** Registration of member boundaries is nontrivial at large conflicts - exactly where it matters; needs robust matching.

### W2-A-0181 - The abstention cliff: models never predict classes below a training-frequency threshold, and the threshold is predictable from loss geometry.

- **Problem:** Rare classes are not just less accurate - below some frequency, models predict them literally never (silent class death). The location and universality of this cliff is uncharacterized.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-class prediction frequency vs training frequency shows a sharp cliff (not smooth decline) at a threshold determined by the class's feature-space overlap with head classes, consistent across architectures - class death is a phase transition predictable from data statistics, and no amount of training-length increase revives dead classes.
- **Why important:** Practitioners assume more training or mild reweighting recovers rare classes; a documented death threshold with a predictor would change how teams triage the long tail.
- **Why possibly novel:** Class-death phase-transition characterization for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Frequency-ladder subsampling of LVIS/ADE classes across seeds, map prediction-frequency cliffs, regress thresholds on feature-overlap measures.
- **Main risk:** Cliff position may drift with loss/sampler choices used in practice; map across common configurations.
- **Mutated from:** W2-A-0068

### W2-A-0182 - Conformal inner-outer mask pairs: distribution-free coverage guarantees for segmentation, tested for usability where it matters.

- **Problem:** Conformal prediction offers guaranteed-coverage regions, which for masks naturally become nested inner (surely-object) and outer (possibly-object) contours - but whether achievable interval widths are narrow enough to be USEFUL in real tasks is unknown.
- **Core hypothesis (falsifiable):** HYPOTHESIS: conformalized inner/outer mask pairs achieve nominal coverage with width overheads small enough for radiotherapy-margin and robot-grasp use in most cases (median annulus width under 15% of object diameter), but widths blow up predictably on ambiguity-heavy classes - producing the first usability map of conformal segmentation.
- **Why important:** Guarantees without usability are academic; a domain-by-domain width atlas tells practitioners where conformal methods are deployable today.
- **Why possibly novel:** KNOWN: conformal segmentation papers exist; the usability-atlas framing with task-anchored width thresholds is UNVERIFIED - needs lit search.
- **Minimal experiment:** Implement split-conformal masks on medical + driving datasets, tabulate coverage and width distributions against task-derived width budgets.
- **Main risk:** Exchangeability violations under shift void guarantees; report shift sensitivity honestly.

### W2-A-0183 - Anomaly-segmentation benchmarks are boundary detectors in disguise: SOTA methods flag object-background transitions, not anomalies.

- **Problem:** Road-anomaly benchmarks reward high anomaly scores on unusual objects; but if methods' scores concentrate on ALL boundaries (of normal objects too), leaderboard success may reflect boundary-affinity, not anomaly understanding.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for leading anomaly-segmentation methods, a large fraction of their positive signal lies within thin bands around object boundaries (normal or anomalous alike), and a boundary-band-excluded re-evaluation collapses the leaderboard while a simple interior-focused baseline climbs - current metrics conflate edge-awareness with anomaly detection.
- **Why important:** Anomaly segmentation feeds safety cases in driving; knowing whether methods detect anomalies or just edges is not optional.
- **Why possibly novel:** Boundary-band ablation audits of anomaly benchmarks are UNVERIFIED - needs lit search.
- **Minimal experiment:** Re-score public anomaly methods with boundary-band exclusion on SegmentMeIfYouCan-style data, quantify rank changes.
- **Main risk:** Some anomaly signal legitimately lives at boundaries; interpret with both included/excluded views.

### W2-A-0184 - Validate the aleatoric/epistemic decomposition against ground truth ambiguity: at boundaries, current methods conflate what they claim to separate.

- **Problem:** Methods claim to separate data uncertainty (aleatoric) from model uncertainty (epistemic), but both explode at boundaries, and no one validates the decomposition against measured stimulus ambiguity (annotator variance) and measured model ignorance (OOD-ness).
- **Core hypothesis (falsifiable):** HYPOTHESIS: at object boundaries, reported aleatoric and epistemic maps correlate with each other far more than either correlates with its ground-truth referent (annotator variance for aleatoric, holdout-domain error for epistemic) - the decomposition largely fails exactly where uncertainty is largest, and honest evaluation requires referent-anchored validation.
- **Why important:** The decomposition justifies real decisions (collect more data vs accept ambiguity); if it is invalid at boundaries, those decisions are misinformed.
- **Why possibly novel:** Referent-anchored validation of the decomposition for dense prediction is UNVERIFIED - needs lit search.
- **Minimal experiment:** On multi-annotator datasets with OOD splits, correlate each uncertainty type with its referent at boundary vs interior pixels.
- **Main risk:** Referents are imperfect proxies; triangulate with multiple referent definitions.
- **Mutated from:** W2-A-0051

### W2-A-0185 - Miscalibration direction flips between head and tail classes: one temperature cannot fix a structured, sign-changing bias.

- **Problem:** Segmentation calibration is usually addressed with global temperature scaling, implicitly assuming uniform miscalibration; class-conditional structure (overconfident on rare, underconfident on common, or the reverse) is undocumented.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-class calibration curves show a systematic sign flip along the frequency axis (head classes underconfident, tail classes overconfident, driven by loss dynamics and label noise asymmetries), so global temperature scaling worsens one end - and the flip point is predictable from class frequency and co-occurrence entropy.
- **Why important:** A sign-changing bias makes the standard remedy actively harmful for part of the label space - important for any consumer of segmentation confidences.
- **Why possibly novel:** Frequency-resolved calibration-sign analysis for dense prediction is UNVERIFIED - needs lit search.
- **Minimal experiment:** Compute per-class reliability diagrams on ADE/LVIS models, locate sign structure, test global-vs-per-class temperature consequences.
- **Main risk:** Per-class calibration estimates are noisy for the rarest classes; use hierarchical estimation.

### W2-A-0186 - Are tumor-volume confidence intervals valid? Propagate segmentation uncertainty into derived clinical quantities and test empirical coverage.

- **Problem:** Downstream users consume derived scalars (volumes, diameters, areas) with error bars produced from pixel uncertainties under independence assumptions that boundary-correlated errors violate.
- **Core hypothesis (falsifiable):** HYPOTHESIS: volume CIs computed under pixel-independence are anti-conservative by 2-5x (empirical coverage far below nominal) because boundary errors are long-range correlated, and correlation-aware propagation (sampling coherent boundary perturbations) restores near-nominal coverage without model changes - a purely statistical fix to a clinically dangerous underestimate.
- **Why important:** Treatment monitoring uses volume changes; overconfident CIs can turn measurement noise into false progression/response calls.
- **Why possibly novel:** Coverage-validated propagation for segmentation-derived scalars is UNVERIFIED - needs lit search.
- **Minimal experiment:** Multi-rater or synthetic-GT lesion data: compare nominal vs empirical coverage across propagation schemes and uncertainty methods.
- **Main risk:** Requires trustworthy reference volumes; synthetic-lesion anchoring mitigates.
- **Mutated from:** W2-A-0074

### W2-A-0187 - Region-level selective prediction dominates image-level: reject the 5% of regions causing 50% of risk instead of whole images.

- **Problem:** Selective prediction for segmentation typically abstains per-image, discarding mostly-correct outputs; per-region abstention could retain value while excising risk, but its operating curves are unmapped.
- **Core hypothesis (falsifiable):** HYPOTHESIS: risk-coverage curves for region-level abstention strictly dominate image-level abstention by large margins across datasets (same risk at 3-5x higher coverage), and the optimal rejection granularity (region size) is predictable from the spatial autocorrelation of errors - a complete recipe for deployable selective segmentation.
- **Why important:** Converts selective prediction from an academic exercise into a practical tool: most of the image is usually fine.
- **Why possibly novel:** Granularity-optimized selective segmentation with dominance quantification is UNVERIFIED - needs lit search.
- **Minimal experiment:** Build risk-coverage curves at multiple abstention granularities on medical + driving models, verify dominance and granularity predictor.
- **Main risk:** Region abstention needs downstream handling protocols (what fills rejected holes) - application-specific.

### W2-A-0188 - Do uncertainty overlays help or hypnotize? Measure over-reliance dynamics when clinicians see model confidence maps.

- **Problem:** Uncertainty visualization is assumed to improve human oversight, but confidence maps could induce automation bias (trusting confident-but-wrong regions MORE) - the behavioral effect is unmeasured for segmentation review.
- **Core hypothesis (falsifiable):** HYPOTHESIS: showing uncertainty overlays reduces human error-catch rates in high-confidence-but-wrong regions (attention is captured by flagged areas, unflagged errors get a pass) while improving catch rates in flagged areas - net effect on total misses can be NEGATIVE when model calibration is poor, making overlay deployment conditional on calibration quality.
- **Why important:** A pre-deployment behavioral law (when overlays help vs harm) is needed before uncertainty visualization becomes standard in clinical tools.
- **Why possibly novel:** Automation-bias quantification for segmentation uncertainty display is UNVERIFIED - needs lit search (automation bias in general is KNOWN in human factors).
- **Minimal experiment:** Controlled review study: radiology trainees correct model masks with/without overlays where some errors are confident; measure catch rates by condition.
- **Main risk:** Human-subject study logistics; effects may vary with expertise level (include as factor).
- **Mutated from:** W2-A-0148

### W2-A-0189 - Context prior vs class prior in the tail: rare classes fail because their contexts are rare, not because their appearance is unlearned.

- **Problem:** Rare-class failure is attributed to insufficient appearance examples, but rare classes also occupy rare contexts; the two deficits (appearance model vs context prior) have different remedies and are never separated.
- **Core hypothesis (falsifiable):** HYPOTHESIS: pasting rare-class instances into common contexts recovers a large fraction of their segmentation accuracy (context prior dominates appearance deficit), while common classes pasted into rare contexts degrade sharply - most 'long-tail appearance learning' framing misattributes a context-prior problem, redirecting fixes toward context-decorrelated training.
- **Why important:** Copy-paste augmentation works (KNOWN empirically); this explains WHY and predicts when it will not (appearance-limited classes), converting a trick into a diagnostic-driven method.
- **Why possibly novel:** Context/appearance deficit decomposition via bidirectional pasting is UNVERIFIED - needs lit search.
- **Minimal experiment:** Bidirectional paste experiments on LVIS tail/head classes, decompose error recovery by manipulation direction.
- **Main risk:** Pasting artifacts help models detect pasted objects; use high-quality harmonization and artifact controls.

### W2-A-0190 - TTA-disagreement as epistemic proxy fails exactly under systematic shift: characterize the validity boundary of consistency-based uncertainty.

- **Problem:** Test-time-augmentation disagreement is a popular free uncertainty signal, but under systematic shift all augmented views are fooled identically, silencing the alarm precisely when needed - the validity envelope is unmapped.
- **Core hypothesis (falsifiable):** HYPOTHESIS: TTA-disagreement tracks error well under stochastic corruptions (noise, blur) but decouples under systematic shifts (new sensor, new geography) with near-zero failure-prediction power there - and the decoupling is detectable ONLINE via disagreement-distribution shape, giving a self-diagnosing uncertainty signal that knows when it is blind.
- **Why important:** Prevents dangerous false confidence in the cheapest uncertainty method, and the self-diagnosis extension rescues its deployability.
- **Why possibly novel:** Validity-envelope mapping with online self-diagnosis for TTA uncertainty is UNVERIFIED - needs lit search.
- **Minimal experiment:** Correlate TTA-disagreement with error across stochastic vs systematic shift suites; test distribution-shape detector for decoupling onset.
- **Main risk:** The taxonomy stochastic-vs-systematic is fuzzy at edges; define operationally by augmentation-space coverage.

### W2-A-0191 - Top-2 logit margin at each pixel is a free boundary-ambiguity map: validate it against annotator disagreement without any uncertainty machinery.

- **Problem:** Models already compute per-pixel class margins; whether this zero-cost signal matches human boundary ambiguity as well as expensive Bayesian machinery does has never been benchmarked head-to-head.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the top-2 margin map correlates with annotator disagreement maps nearly as strongly as deep ensembles do (within 10% of ensemble correlation) at 1/Nth the cost, but ONLY for in-distribution boundary ambiguity - establishing a practical uncertainty hierarchy: margins for boundaries, ensembles for OOD, nothing extra needed in between.
- **Why important:** A validated cost-capability hierarchy stops teams from paying ensemble costs for boundary questions margins already answer.
- **Why possibly novel:** Head-to-head referent-anchored comparison of margin vs ensemble for boundary ambiguity is UNVERIFIED - needs lit search.
- **Minimal experiment:** On multi-annotator data, correlate margin maps and ensemble maps with disagreement; stratify by in/out-of-distribution condition.
- **Main risk:** Margins are miscalibrated per-class (see frequency sign-flip idea); may need per-class normalization to shine.
- **Mutated from:** W2-A-0184

### W2-A-0192 - Semantically-weighted confusion: wrong-but-adjacent (car-truck) vs wrong-and-absurd (car-sky) errors have identical metric cost but wildly different consequences - measure the absurdity distribution.

- **Problem:** Confusion severity is flat in all standard metrics. The distribution of error 'semantic distance' - and whether newer models err more reasonably - is unmeasured, though consumers care mostly about absurd errors.
- **Core hypothesis (falsifiable):** HYPOTHESIS: models with similar mIoU differ up to severalfold in absurd-error rates (semantic distance above safety thresholds), the absurdity rate is NOT monotonically improved by scale or recency (some new models err more absurdly), and absurdity-weighted rankings disagree with mIoU rankings enough to matter for safety-driven selection.
- **Why important:** Safety cases hinge on worst-case severity, not average overlap; an absurdity metric with published model profiles fills a real selection gap.
- **Why possibly novel:** Systematic absurdity-distribution profiling of segmentation models is UNVERIFIED - needs lit search (hierarchical metrics exist but adoption-focused profiling of the model zoo does not, to my knowledge).
- **Minimal experiment:** Define semantic distance via ontology + human severity ratings, profile 10 public models, compare rankings vs mIoU.
- **Main risk:** Semantic distance definition is contestable; validate against human severity judgments.

### W2-A-0193 - Near-duplicate training images create overconfidence pockets: data attribution for segmentation miscalibration.

- **Problem:** Web-scraped training sets contain near-duplicate clusters; models see some visual patterns many times, plausibly producing spatially-localized overconfidence unrelated to true reliability - a data-side cause of miscalibration nobody audits.
- **Core hypothesis (falsifiable):** HYPOTHESIS: test-image regions visually similar to high-duplication training clusters show systematically inflated confidence at equal accuracy (an overconfidence pocket signature), and deduplicated retraining flattens these pockets - a measurable causal path from data redundancy to calibration structure.
- **Why important:** Connects dataset hygiene to trustworthiness (not just accuracy), giving calibration auditors a new data-side lever.
- **Why possibly novel:** Duplication-conditioned calibration analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Cluster training data by similarity, map test-time confidence vs nearest-cluster duplication level, retrain deduplicated for the causal leg.
- **Main risk:** Similarity-to-training measurement is itself model-dependent; use external embedding for neutrality.

### W2-A-0194 - What hides in ignore regions? Benchmarks' void labels conceal systematic model failures that count in deployment.

- **Problem:** Evaluation protocols exclude 'void/ignore' pixels (ambiguous, boundary, unlabeled regions). Models are unconstrained there, and deployment consumes those predictions anyway - what models actually emit in ignored zones is undocumented.
- **Core hypothesis (falsifiable):** HYPOTHESIS: within ignore regions, model predictions are strongly model-specific and often absurd (class flicker, impossible layouts), inter-model agreement collapses (revealing that supervision, not learning, was constraining them), and downstream metrics that consume full maps (planning, rendering) degrade measurably due to ignore-zone behavior invisible to benchmarks.
- **Why important:** The gap between evaluated pixels and consumed pixels is a silent deployment liability; quantifying it forces protocol honesty.
- **Why possibly novel:** Ignore-region behavioral audit is UNVERIFIED - needs lit search.
- **Minimal experiment:** Extract ignore-region predictions from public models on Cityscapes/ADE, measure inter-model agreement and downstream-task sensitivity to those zones.
- **Main risk:** No GT there by definition; evaluation must use consistency, plausibility, and downstream proxies.

### W2-A-0195 - Sub-10-example classes are retrieval, not generalization: feature-space nearest-neighbor tests reveal the memorization regime of the extreme tail.

- **Problem:** Classes with a handful of training instances still show nonzero test performance; whether this reflects generalization or disguised memorization (matching near-identical training instances) determines whether extreme-tail scores mean anything.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for classes under ~10 training instances, test-set successes overwhelmingly occur on test instances with near-duplicate training matches (feature distance below a threshold), and success probability drops toward zero as match distance grows - extreme-tail performance is retrieval performance, and benchmark tails measure dataset redundancy rather than model capability.
- **Why important:** Recalibrates every long-tail leaderboard's bottom decile and separates two capabilities (retrieval vs generalization) that current metrics blend.
- **Why possibly novel:** Match-distance-conditioned success analysis for tail segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** For LVIS rare classes, compute per-test-instance nearest-training distances, plot success vs distance, compare against head-class curves.
- **Main risk:** Feature space choice affects distance; replicate across embeddings.
- **Mutated from:** W2-A-0193

### W2-A-0196 - Uncertainty as the first sensor to fail: under gradual weather degradation, which uncertainty signal rises first, and does its order match accuracy decline?

- **Problem:** Multi-signal uncertainty stacks (entropy, margin, ensembles, TTA) are compared on static benchmarks, but deployment needs to know their ONSET ORDER under gradually worsening conditions - who warns first, who warns falsely.
- **Core hypothesis (falsifiable):** HYPOTHESIS: signals have a reproducible onset ordering along weather-degradation trajectories (e.g. ensemble disagreement first, entropy last), the ordering is stable across scenes but differs across shift types, and combining onset order with signal levels identifies the shift TYPE label-free - uncertainty dynamics carry diagnostic information that static levels discard.
- **Why important:** Deployment monitoring needs early, interpretable alarms; onset-order fingerprints add a diagnosis capability to mere detection.
- **Why possibly novel:** Temporal onset-order analysis of uncertainty signals is UNVERIFIED - needs lit search.
- **Minimal experiment:** Drive models along graded weather ladders (synthetic + ACDC), record all signals, test ordering stability and shift-type classification.
- **Main risk:** Graded natural weather data is limited; synthetic gradients must be validated against natural anchor points.
- **Mutated from:** W2-A-0177

### W2-A-0197 - Confidence dilutes with vocabulary size in open-vocabulary segmentation: a predictable law makes scores incomparable across vocabularies.

- **Problem:** Open-vocabulary models score each pixel against arbitrary user-supplied class lists; adding distractor classes necessarily redistributes probability mass, so confidence (and thresholded decisions) depend on vocabulary size - a structural effect nobody models or corrects.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-pixel confidence for the true class decays with vocabulary size following a predictable law (driven by embedding-space crowding around the true class), decision flips under vocabulary growth concentrate on tail/ambiguous classes, and a crowding-aware confidence normalization restores vocabulary-invariant behavior - fixing silent incomparability across deployments.
- **Why important:** Open-vocabulary models are deployed with wildly different class lists; vocabulary-dependent behavior means the same model+image gives different answers by list choice - users deserve a characterization and correction.
- **Why possibly novel:** Vocabulary-scaling laws for dense open-vocabulary confidence are UNVERIFIED - needs lit search.
- **Minimal experiment:** Sweep vocabulary sizes with controlled distractor sampling on OV segmentation models, fit decay laws, test normalization for invariance.
- **Main risk:** Distractor choice affects the law's parameters; characterize semantic-proximity dependence explicitly.

### W2-A-0198 - Seed-churn maps: pixels that flip between training runs form a free, model-intrinsic ambiguity atlas that matches human disagreement.

- **Problem:** Retraining with different seeds flips predictions on specific pixels (churn). This intrinsic instability is treated as noise, but its spatial structure may encode exactly the stimulus ambiguity that expensive uncertainty methods try to estimate.
- **Core hypothesis (falsifiable):** HYPOTHESIS: pixelwise churn across 5-10 seeds correlates with human annotator disagreement as strongly as deep-ensemble variance does (they are near-duplicate signals), churn maps are stable dataset properties (transferable across architectures), and published per-method 'improvements' concentrate suspiciously on high-churn pixels - simultaneously offering a cheap ambiguity atlas and a benchmark-noise audit tool.
- **Why important:** One artifact (churn atlas) serves three uses: free uncertainty referent, benchmark noise floor, and reproducibility diagnostics for claimed gains.
- **Why possibly novel:** KNOWN: churn is studied in classification; dense churn atlases with the benchmark-audit application are UNVERIFIED - needs lit search.
- **Minimal experiment:** Train 10 seeds of 2 architectures on Cityscapes, build churn atlases, correlate with multi-annotator data, overlay published method deltas.
- **Main risk:** Compute cost of multi-seed training (moderate); mitigated by using smaller proxy models if transfer holds.

### W2-A-0199 - Rare-context hallucination: models paint plausible-but-absent stuff classes (water under bridges, sky through gaps) driven by context priors overpowering evidence.

- **Problem:** Segmentation errors are usually studied as misclassification of present things; systematic hallucination of ABSENT classes in strongly-suggestive contexts (context-completion errors) is unquantified for dense prediction.
- **Core hypothesis (falsifiable):** HYPOTHESIS: in contexts statistically associated with a class (bridge implies water below), models predict the associated class at measurable rates even when it is verifiably absent, the hallucination rate scales with context-class association strength mined from training co-occurrence, and evidence-ablation shows these pixels rely on context, not appearance - dense prediction has a measurable prior-override failure mode analogous to LLM hallucination.
- **Why important:** Establishes hallucination as a quantifiable dense-prediction phenomenon with a data-statistics predictor - relevant for safety and for understanding context integration generally.
- **Why possibly novel:** Context-completion hallucination quantification for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Curate context-strong/class-absent images (dry canals, drained pools, bridges over roads), measure per-model hallucination vs mined association strength.
- **Main risk:** Verifying true absence needs careful curation; some cases are genuinely ambiguous from single views.

### W2-A-0200 - The tail is where annotation noise lives: rare-class 'errors' are disproportionately label errors, making measured tail performance a lower bound with a computable correction.

- **Problem:** Rare classes are annotated by workers with less exposure and lower agreement; model 'failures' there may substantially be annotator failures, systematically understating true tail capability.
- **Core hypothesis (falsifiable):** HYPOTHESIS: expert re-audit of model-GT disagreements will show the label-fault rate rising steeply from head to tail classes (annotator unfamiliarity effect), and correcting evaluated labels compresses the head-tail performance gap substantially - part of the long-tail problem is a long-tail-of-annotation-quality problem, with different implied remedies.
- **Why important:** If the tail gap is partly measurement artifact, expensive tail-focused training methods are being judged against corrupted references - the field should fix references before methods.
- **Why possibly novel:** Frequency-resolved label-error auditing for segmentation is UNVERIFIED - needs lit search (classification label-error work is KNOWN: Northcutt et al.).
- **Minimal experiment:** Sample model-GT disagreements across frequency deciles on LVIS, expert-adjudicate 2k cases, fit fault-rate vs frequency, re-estimate corrected gaps.
- **Main risk:** Expert adjudication is itself imperfect for genuinely ambiguous tail categories; use multi-expert panels.

## C09-annotation-interactive

### W2-A-0201 - Real crowdworker clicks vs simulated clicks: quantify the sim2real prompting gap that inflates every interactive segmentation benchmark.

- **Problem:** Interactive segmentation is evaluated with simulators (click at center of largest error). Real users click by salience, habit, and motor economy; the distribution gap and its score inflation are unmeasured for general annotators.
- **Core hypothesis (falsifiable):** HYPOTHESIS: replayed real-user click sessions yield measurably worse NoC/IoU curves than simulator evaluation for the same models (inflation >20% in clicks-to-target), and models RANK differently under real clicks - some architectures are robust to human click styles, others are simulator-tuned.
- **Why important:** If rankings flip under real usage, years of interactive-segmentation comparisons need re-reading, and future evaluation must include click-style robustness.
- **Why possibly novel:** A public real-click corpus with replay evaluation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Collect 2k real click sessions via crowdsourcing on COCO objects, replay against 5 models, compare with simulator curves.
- **Main risk:** Interface design shapes click behavior; use multiple interface variants to bound the effect.
- **Mutated from:** W2-A-0065

### W2-A-0202 - Information-per-second of annotation primitives: clicks vs scribbles vs boxes vs verbal corrections, measured properly for once.

- **Problem:** Annotation-efficiency papers compare supervision types by count (10 clicks vs 1 box), not by human time and cognitive cost - the actual currency. The efficiency ordering may invert under time-based accounting.
- **Core hypothesis (falsifiable):** HYPOTHESIS: under wall-clock accounting with real annotators, scribbles dominate clicks for organic shapes and boxes dominate for convex objects (a shape-conditional efficiency map), while the field's per-interaction accounting has promoted clicks beyond their true standing - and optimal interfaces should switch primitives per object geometry.
- **Why important:** Every labeling operation allocates budget by these tradeoffs; a shape-conditional efficiency map is directly actionable industry-wide.
- **Why possibly novel:** Time-based shape-conditional efficiency measurement is UNVERIFIED - needs lit search.
- **Minimal experiment:** Timed annotation study (N=20) across primitive types and object-shape strata, fit efficiency map, validate model-training outcomes per budget.
- **Main risk:** Annotator skill heterogeneity; use within-subject designs.

### W2-A-0203 - Unpromptable objects exist: characterize the reachable mask space of frozen interactive models and what lies outside it.

- **Problem:** Interactive models are assumed universal - enough clicks reach any mask. But the decoder's output manifold may exclude some masks entirely (certain topologies, textures), making some objects unreachable at ANY click budget.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for frozen interactive segmenters there exist GT masks whose best reachable IoU (under exhaustive prompt search) plateaus below 0.7 (structural unreachability), unreachable objects share identifiable properties (wiry topology, translucency, extreme aspect), and unreachability persists across prompt types - defining the model's true expressivity boundary, distinct from its average behavior.
- **Why important:** Annotation pipelines assume humans+model can always produce GT; unreachable objects silently corrupt datasets built with model assistance.
- **Why possibly novel:** Reachability analysis of interactive segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Exhaustive/beam prompt search on 1k diverse objects, identify plateau cases, cluster their properties, verify with human super-users.
- **Main risk:** Search may miss exotic prompt combinations; bound claims by search budget honestly.
- **Mutated from:** W2-A-0013

### W2-A-0204 - Label order shapes the final model: easy-first vs hard-first annotation curricula produce different models at identical final budgets.

- **Problem:** Datasets are annotated in some order (often easy-first), and models are periodically retrained during collection (model-assisted labeling). Whether the ORDER leaves a permanent imprint on the final dataset+model is unexamined.
- **Core hypothesis (falsifiable):** HYPOTHESIS: in model-in-the-loop annotation, easy-first ordering converges to datasets with systematically different error profiles than hard-first (assistance quality compounds: early model errors seed persistent label styles), and the final-model performance difference at identical budgets exceeds typical method deltas - collection order is a hidden hyperparameter of dataset quality.
- **Why important:** Every assisted-labeling operation implicitly chooses an order; knowing the compounding effect would change collection protocols cheaply.
- **Why possibly novel:** Order-effect quantification in assisted dataset construction is UNVERIFIED - needs lit search.
- **Minimal experiment:** Simulated assisted-labeling runs with order policies on a fully-labeled dataset (labels revealed per policy), compare final model quality and error styles.
- **Main risk:** Simulation fidelity to real human-model interaction; a small real study for anchoring.

### W2-A-0205 - Verification bias: annotators accept wrong-but-plausible machine masks at high rates, and the accepted errors are systematically correlated with model style.

- **Problem:** Verify-and-fix workflows (machine proposes, human approves) are the industry standard, but acceptance decisions under time pressure may pass through model errors that free-drawing annotators would never make - contaminating datasets with model-correlated noise.
- **Core hypothesis (falsifiable):** HYPOTHESIS: acceptance error rates for plausible-but-wrong proposals exceed free-drawing error rates severalfold for boundary details and small parts, the accepted errors correlate across the dataset (same model style), and models trained on verified data inherit and AMPLIFY these correlated errors - a measurable contamination loop absent from noise-model assumptions (which assume independent noise).
- **Why important:** Correlated label noise breaks the independence assumptions behind noise-robust training; quantifying the loop is prerequisite to fixing dataset factories.
- **Why possibly novel:** Correlated-contamination quantification of verify-workflows is UNVERIFIED - needs lit search.
- **Minimal experiment:** Controlled study: same images labeled by verify-vs-draw protocols, measure error correlation structure, train models on each, compare inherited biases.
- **Main risk:** Time-pressure realism in lab studies; partner with a real annotation vendor for ecological validity.

### W2-A-0206 - Detect the SAM fingerprint: datasets annotated with SAM assistance carry identifiable boundary-style signatures that future models inbreed on.

- **Problem:** Post-2023 datasets are increasingly SAM-assisted. If SAM's boundary style (edge-snapping, blob bias, characteristic curvature spectrum) marks these labels, models trained on them converge toward SAM's biases - ecosystem inbreeding that nobody tracks.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a classifier distinguishes SAM-assisted from human-drawn masks at high accuracy using boundary micro-statistics (fingerprint exists), the fingerprint's prevalence in recent public datasets is substantial and rising, and models trained on fingerprinted data reproduce SAM's specific failure modes (holes filled, wires broken) even on classes where SAM was never involved - measurable style inheritance.
- **Why important:** Dataset provenance transparency and bias tracking for the foundation-model era; inbreeding could silently homogenize the field's failure modes into single points of failure.
- **Why possibly novel:** SAM-fingerprint forensics and inheritance measurement is UNVERIFIED - needs lit search.
- **Minimal experiment:** Build fingerprint classifier on known SAM/human mask pairs, survey 10 recent datasets, test failure-mode inheritance in models trained on high-fingerprint data.
- **Main risk:** Post-editing by humans blurs fingerprints; classifier must handle mixed provenance.
- **Mutated from:** W2-A-0017

### W2-A-0207 - Where should a scribble go? Skeleton vs boundary-following vs freeform strokes have measurably different information gain per pixel drawn.

- **Problem:** Scribble supervision treats all strokes equally, but stroke PLACEMENT geometry (medial axis, near-boundary, random) plausibly changes information delivered per unit effort - the placement policy question is unstudied.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for equal stroke length, skeleton-placed scribbles train better region models while near-boundary parallel strokes train better boundary models (a decomposable placement effect), and a mixed policy tuned per class geometry outperforms natural human scribbling by a meaningful margin - placement policy is worth more than scribble quantity within realistic budgets.
- **Why important:** Scribble platforms can guide stroke placement with simple UI nudges; validated policies convert to free accuracy across weak-supervision projects.
- **Why possibly novel:** Stroke-placement information analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Synthesize placement-controlled scribbles from GT masks, train per policy at matched stroke budgets, decompose gains by region/boundary metrics.
- **Main risk:** Synthetic scribbles idealize human motor behavior; verify with guided-human study.

### W2-A-0208 - Region-level active learning with real time-cost models: intra-image selection beats whole-image selection once annotation time is measured honestly.

- **Problem:** Active learning for segmentation mostly selects whole images, but annotation cost varies enormously within images; region-level selection with realistic time models (travel time, context acquisition, zooming) has never been evaluated under honest cost accounting.
- **Core hypothesis (falsifiable):** HYPOTHESIS: under measured per-region annotation time models (including the overhead of context re-acquisition when jumping between regions), region-level selection still dominates image-level by >30% Dice-per-hour at practical budgets, but naive per-pixel-uncertainty region selection UNDERPERFORMS image selection because it ignores overhead - cost-model realism determines the ranking of AL strategies.
- **Why important:** AL research optimizes proxy costs; showing rankings flip under real time models forces the field toward deployable protocols.
- **Why possibly novel:** Overhead-aware regional AL evaluation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Measure annotation time components in a small study, build cost model, re-simulate AL strategy comparison on 3 datasets.
- **Main risk:** Time models vary by tooling; publish the cost model as configurable artifact.
- **Mutated from:** W2-A-0179

### W2-A-0209 - Shape predictability determines point-supervision efficiency: one point suffices exactly when class shape entropy is low - fit the law.

- **Problem:** Single-point supervision recovers surprising performance for some classes and fails for others. The determining property is presumably how predictable the class's shape is given one point - a measurable quantity nobody has connected.
- **Core hypothesis (falsifiable):** HYPOTHESIS: the fraction of full-mask performance recoverable from single-point supervision per class is predicted (r>0.8) by class shape entropy (variance of shape descriptors across instances), yielding a practical law: measure shape entropy from a handful of masks, predict point-supervision viability before committing to an annotation scheme.
- **Why important:** Converts supervision-scheme selection from trial-and-error into a measurement-driven decision - direct savings for every new dataset.
- **Why possibly novel:** Shape-entropy-based supervision-efficiency law is UNVERIFIED - needs lit search.
- **Minimal experiment:** Across 40 classes from COCO/LVIS, train point-supervised models, regress recovered-performance fraction on shape-entropy estimates from 20 masks per class.
- **Main risk:** Context predictability confounds shape predictability; include context-entropy covariate.

### W2-A-0210 - Expertise routing: measure WHERE expert annotation beats crowd annotation at the pixel level, and route only those pixels to experts.

- **Problem:** Datasets choose expert or crowd annotation wholesale, but expertise plausibly matters only in specific regions (ambiguous boundaries, rare structures); the pixel-level expertise premium map is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: expert-vs-crowd label agreement analysis will show the expertise premium concentrates in <20% of pixels (identifiable a priori by ambiguity predictors), and a routing policy sending only those regions to experts achieves expert-level dataset quality at a fraction of expert cost - measurable end-to-end via models trained on routed datasets.
- **Why important:** Expert time is the scarcest resource in specialized domains (medical, scientific imagery); pixel-level routing is the efficient frontier of annotation economics.
- **Why possibly novel:** Pixel-resolved expertise-premium mapping with routed-dataset validation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Double-annotate (expert+crowd) 500 medical/complex images, map premium regions, test predictor, train models on routed vs pure datasets at matched cost.
- **Main risk:** Premium maps may be domain-specific; replicate across two domains.

### W2-A-0211 - Optimal correction-frame selection in video annotation: model uncertainty peaks beat uniform keyframes, but the real optimum is drift-onset frames.

- **Problem:** Video annotation corrects the tracker at chosen frames; the frame-selection policy (uniform, uncertainty-based, drift-onset-based) determines total cost, but policies have not been compared under matched click budgets.
- **Core hypothesis (falsifiable):** HYPOTHESIS: correcting at detected drift-onset frames (from self-diagnosis signals) yields better final video masks than uniform or uncertainty-peak selection at equal correction budget, with the advantage growing with video length - because corrections BEFORE error compounding are worth multiples of corrections after.
- **Why important:** Video annotation is the current cost bottleneck for VOS datasets; a validated frame-selection policy compounds savings across the ecosystem.
- **Why possibly novel:** Drift-onset-timed correction policy evaluation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Simulate correction policies with SAM2 on DAVIS/LVOS at matched budgets, compare final-quality curves; small human study for timing realism.
- **Main risk:** Drift-onset detection quality gates the policy; co-develop with the self-diagnosis idea.
- **Mutated from:** W2-A-0047

### W2-A-0212 - The good-enough plateau: humans stop correcting at ~90% quality, leaving systematic residual errors aligned with model biases in every assisted dataset.

- **Problem:** Assisted annotation ends when the human judges the mask 'good enough', not when it is correct. The residual errors are thus model-biased (humans fix salient errors, keep model-style subtle ones) - a structured contamination whose form is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: assisted-annotation residuals concentrate in low-salience error types (boundary offsets in blurry regions, small holes) while free-drawn labels distribute errors differently, the residual structure matches the assisting model's bias profile, and datasets can be forensically dated/attributed to their assisting model by residual structure alone.
- **Why important:** Defines the quality ceiling of the assisted-annotation paradigm and provides provenance forensics; also predicts what SECOND-generation models can and cannot learn from such data.
- **Why possibly novel:** Residual-structure analysis of the good-enough threshold is UNVERIFIED - needs lit search.
- **Minimal experiment:** Have annotators 'finish' assisted masks, then expert-audit at high zoom; compare residual profiles across assisting models and against free-drawing.
- **Main risk:** Good-enough thresholds vary with pay/incentives; sample multiple annotation economies.
- **Mutated from:** W2-A-0205

### W2-A-0213 - Gaze as free dense supervision: eye-tracking during ordinary image inspection carries recoverable segmentation signal.

- **Problem:** Wherever humans inspect images professionally (radiology, quality control), gaze data is potentially collectible at zero marginal effort; its information content for segmentation supervision is essentially unquantified.
- **Core hypothesis (falsifiable):** HYPOTHESIS: gaze density and scanpath features around objects contain enough localization signal that gaze-weak-supervised models reach a meaningful fraction (>50%) of point-supervised performance without ANY deliberate annotation, and gaze fixation ORDER additionally encodes object saliency structure usable for curriculum construction.
- **Why important:** Free supervision from existing professional workflows would be transformative for domains where deliberate annotation competes with real work (medicine).
- **Why possibly novel:** KNOWN: gaze studies exist in radiology perception research; segmentation-supervision extraction with performance accounting is UNVERIFIED - needs lit search.
- **Minimal experiment:** Use public radiology gaze datasets (e.g. REFLACX-like), derive gaze-based pseudo-labels, train and compare against point-supervised baselines.
- **Main risk:** Gaze concentrates on diagnostic hotspots, not object extents; may supervise detection better than delineation (report both).

### W2-A-0214 - Language vs clicks for disambiguation: when scenes get crowded, referring expressions become cheaper than pointing - find the crossover.

- **Problem:** Disambiguating a target among similar instances can be done by clicking (spatial) or describing ('the third cup from the left') - the interaction-cost crossover between modalities as scene complexity grows is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: measured in time-to-correct-mask, clicking dominates in sparse scenes but language dominates beyond a measurable instance-density threshold (pointing precision degrades with crowding faster than description length grows), and hybrid systems that ROUTE by predicted density beat either modality alone by >20% throughput.
- **Why important:** Multimodal annotation interfaces are buildable today; the routing law tells builders when each modality pays, grounded in measurement rather than fashion.
- **Why possibly novel:** Modality-crossover measurement for segmentation disambiguation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Timed human study across instance-density ladder with click-only, language-only, and routed interfaces on crowded scenes (shelves, crowds).
- **Main risk:** Language grounding model quality gates the language arm; use the best available grounding models and report sensitivity.

### W2-A-0215 - Annotation protocol is a stronger treatment than architecture: same images labeled boundary-first vs region-first produce measurably different trained models.

- **Problem:** Protocols (labeling order, tool, instructions) are considered logistics, not science. If protocol-induced differences in trained models exceed typical architecture deltas, the field's controlled comparisons are missing a dominant variable.
- **Core hypothesis (falsifiable):** HYPOTHESIS: training identical architectures on the same images labeled under two professional protocols (boundary-tracing-first vs region-filling-first) produces models whose performance difference on neutral test sets exceeds the median published architecture improvement - protocol choice silently dominates a meaningful fraction of reported progress.
- **Why important:** A provocative, testable claim about what actually drives measured differences in the literature; would force protocol reporting standards.
- **Why possibly novel:** Protocol-as-treatment controlled experiments are UNVERIFIED - needs lit search.
- **Minimal experiment:** Commission dual-protocol labeling of 2k images by the same vendor, train matched models, compare deltas against a survey of published architecture gains.
- **Main risk:** Annotation cost of the dual corpus; mitigate with a focused domain (e.g. one driving subset).
- **Mutated from:** W2-A-0156

### W2-A-0216 - Negative-space labels for rare classes: marking 'definitely-not-X' regions is cheap and disproportionately valuable for tail-class learning.

- **Problem:** All annotation effort goes into positive labels; explicit negatives (this region certainly contains no X) are never collected, though for rare classes the model's main confusion is what ISN'T the class.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for tail classes, a budget split that spends 30% on definitely-not-X region marking (fast, low-cognitive-load) beats 100%-positive budgets by a measurable margin on precision-critical metrics, because rare-class errors are dominated by hard-negative confusion that positives cannot teach - the value of negative space is class-frequency-dependent and predictable.
- **Why important:** A cheap new annotation primitive with a theory of when it pays - immediately testable by any labeling operation struggling with tail precision.
- **Why possibly novel:** Explicit negative-region annotation economics is UNVERIFIED - needs lit search.
- **Minimal experiment:** On LVIS tail classes, simulate budget splits using existing annotations to synthesize negatives, then run a small real-annotation confirmation.
- **Main risk:** Negatives may be too easy (uninformative regions get marked); guided negative selection needed.
- **Mutated from:** W2-A-0005

### W2-A-0217 - Annotator zoom telemetry is a free boundary-uncertainty ground truth: where humans zoom in, ambiguity lives.

- **Problem:** Annotation interfaces record zoom/pan behavior that nobody analyzes; zoom-in events plausibly mark exactly the boundary regions annotators find uncertain - a free, behavioral ambiguity signal at dataset scale.
- **Core hypothesis (falsifiable):** HYPOTHESIS: zoom-event density along boundaries correlates strongly with inter-annotator disagreement (validating telemetry as ambiguity GT), and models calibrated against zoom-density maps achieve boundary-uncertainty quality comparable to expensive multi-annotator supervision - telemetry replaces redundant labeling for uncertainty training.
- **Why important:** Multi-annotator redundancy is the current (expensive) route to ambiguity ground truth; telemetry is already being recorded and discarded industry-wide.
- **Why possibly novel:** Telemetry-derived ambiguity supervision is UNVERIFIED - needs lit search.
- **Minimal experiment:** Instrument an annotation tool, collect telemetry on multi-annotated images, validate zoom-disagreement correlation, train uncertainty heads on telemetry.
- **Main risk:** Zoom behavior also reflects object size and tool ergonomics; regression controls required.
- **Mutated from:** W2-A-0136

### W2-A-0218 - Let the model ask: binary yes/no questions about parts ('is the strap included?') beat clicks for ambiguity resolution per second of human time.

- **Problem:** Interactive segmentation only accepts spatial gestures, but much residual ambiguity is SEMANTIC (include the handle? the shadow? the attached cable?) - resolvable by one binary answer instead of several corrective clicks.
- **Core hypothesis (falsifiable):** HYPOTHESIS: an interaction budget spent on model-generated binary part-inclusion questions resolves granularity/attachment ambiguity faster (in human-seconds to target IoU) than the same budget in clicks, specifically on objects whose ambiguity is compositional rather than boundary-metric - a measurable interaction-modality advantage on a definable object subset.
- **Why important:** Identifies the right interaction primitive per ambiguity TYPE, moving interactive segmentation beyond pure spatial correction toward mixed-initiative dialogue.
- **Why possibly novel:** Question-generation for segmentation disambiguation with time-based evaluation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Wizard-of-Oz study: humans answer scripted part-questions vs click corrections at matched time budgets on ambiguous objects (bags with straps, tools with cables).
- **Main risk:** Automatic question generation is a hard subproblem; the study establishes value before building it.
- **Mutated from:** W2-A-0002

### W2-A-0219 - Correction propagation: one human fix retrieved-and-applied across thousands of images sharing the same systematic model error.

- **Problem:** Model errors are systematic (same failure on similar inputs), but human corrections are consumed once. Retrieving past corrections for similar contexts could amortize each fix across the corpus - the amortization factor is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: corrections cluster in feature space (systematic error families), retrieval-based correction transfer (apply the nearest past correction's local transformation) fixes a substantial fraction of same-family errors without new human input, and the human-effort amortization factor exceeds 10x on homogeneous corpora (aerial tiles, pathology slides) - correction reuse is a neglected order-of-magnitude lever.
- **Why important:** Changes annotation economics fundamentally on large homogeneous corpora, which is exactly where annotation costs bite hardest.
- **Why possibly novel:** Retrieval-based correction propagation for dense labels is UNVERIFIED - needs lit search.
- **Minimal experiment:** On aerial/pathology corpora, collect corrections, cluster error contexts, measure transfer precision of retrieved fixes vs fresh model predictions.
- **Main risk:** Bad transfers corrupt labels silently; needs conservative confidence gating and audit sampling.

### W2-A-0220 - Noisy-many vs precise-few for pretraining: fit the exchange rate between mask quantity and mask quality at fixed annotation budget.

- **Problem:** A fixed budget buys either many rough masks or few precise ones. The quality-quantity exchange rate for segmentation pretraining/training - and whether it depends on downstream task boundary-sensitivity - has never been mapped.
- **Core hypothesis (falsifiable):** HYPOTHESIS: on the quality-quantity frontier at matched budget, region-level downstream tasks favor quantity strongly (rough masks nearly free of penalty) while boundary-level tasks favor quality with a sharp threshold effect (below some precision, masks are worse than useless for boundary learning) - two regimes with a measurable phase boundary that should govern annotation-spec decisions.
- **Why important:** The single most common annotation-planning question, currently answered by intuition; a published frontier with the phase boundary would be a standard reference.
- **Why possibly novel:** Budget-matched quality-quantity frontier mapping is UNVERIFIED - needs lit search.
- **Minimal experiment:** Degrade GT masks at controlled precision levels, train at matched simulated budgets across quality-quantity mixes, map the frontier for region vs boundary metrics.
- **Main risk:** Synthetic degradation may not mimic real cheap-annotation error structure; anchor with real dual-quality annotations.

### W2-A-0221 - Multi-view agreement replaces annotation: photos of the same scene from different angles provide free correspondence-based mask supervision.

- **Problem:** Multi-view captures (real-estate scans, photogrammetry, casual multi-shots) constrain segmentation geometrically - a mask valid in one view must reproject consistently to others - but this free supervision channel is unexploited for training 2D segmenters.
- **Core hypothesis (falsifiable):** HYPOTHESIS: cross-view mask-consistency training on unlabeled multi-view corpora (enforcing reprojection agreement via estimated geometry) improves single-view segmentation of view-dependent failure cases (glare, oblique angles, partial occlusion) by a measurable margin over single-view SSL at matched data volume - geometry is a supervisor that photometric SSL cannot replicate.
- **Why important:** Taps enormous existing multi-view corpora (mapping, real estate, e-commerce turntables) as free dense supervision, targeting exactly the failures single views cannot teach.
- **Why possibly novel:** KNOWN: multi-view consistency is used in 3D reconstruction; its harvest as 2D segmentation supervision at scale is UNVERIFIED - needs lit search.
- **Minimal experiment:** Use ScanNet/RealEstate-style corpora, add reprojection-consistency objectives to an SSL baseline, evaluate single-view improvements on shifted test sets.
- **Main risk:** Geometry estimation errors inject noise; restrict supervision to high-confidence correspondences.

### W2-A-0222 - Click order is a cognitive probe: the sequence in which annotators click parts reveals a shared human object-decomposition that models lack.

- **Problem:** Multi-click annotation sequences encode which parts humans consider primary, ambiguous, or boundary-critical - a behavioral window into human object structure that is recorded everywhere and studied nowhere.
- **Core hypothesis (falsifiable):** HYPOTHESIS: click sequences across annotators show strong order regularities (canonical part order per category: face before limbs, body before accessories), the regularities predict which parts models most often mis-segment (late-clicked parts are model-hardest), and sequence-derived part priorities improve error prediction beyond appearance features - human interaction order encodes a difficulty structure models share.
- **Why important:** A zero-cost behavioral dataset for studying object decomposition, with practical use in error prediction and annotation UI design.
- **Why possibly novel:** Click-order regularity analysis as cognitive/difficulty probe is UNVERIFIED - needs lit search.
- **Minimal experiment:** Mine click logs from open annotation projects (or collect via crowdsourcing), quantify order regularities, correlate with per-part model error rates.
- **Main risk:** Order reflects UI layout and motor efficiency too; experimental designs must separate these.
- **Mutated from:** W2-A-0201

### W2-A-0223 - Give annotators an explicit 'uncertain' brush: does three-state labeling (yes/no/unsure) improve downstream models over forced binary?

- **Problem:** Forced-binary interfaces convert annotator uncertainty into silent noise. An explicit unsure-label preserves the information, but whether models trained with it beat models trained on forced-binary labels (at equal annotation time) is untested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: three-state annotation costs <10% extra time, the unsure-regions reproduce across annotators (they mark signal, not laziness), and excluding-or-downweighting unsure pixels during training improves test performance on the confident-consensus region more than the removed supervision costs - explicit uncertainty capture is annotation-time-positive.
- **Why important:** A minimal interface change with dataset-wide benefits, directly adoptable by every labeling tool if validated.
- **Why possibly novel:** Controlled three-state protocol evaluation with downstream accounting is UNVERIFIED - needs lit search.
- **Minimal experiment:** Dual-protocol labeling study (binary vs three-state) on ambiguous-heavy imagery, train matched models, compare on high-confidence test regions.
- **Main risk:** Unsure-label semantics drift between annotators without careful instruction design.
- **Mutated from:** W2-A-0143

### W2-A-0224 - Tool fingerprints across public datasets: identify which annotation software made each mask and quantify tool-induced bias in the ecosystem.

- **Problem:** Public datasets were annotated with different tools (polygon editors, brushes, assisted systems) whose geometric artifacts (vertex spacing, curvature quantization, snap behaviors) enter the labels - the ecosystem-wide composition and its downstream effects are unmapped.
- **Core hypothesis (falsifiable):** HYPOTHESIS: mask micro-geometry classifies annotation tooling with high accuracy across major datasets, tool composition differs strongly by dataset era and domain, and models trained cross-dataset devote measurable capacity to tool-style translation (probeable as tool-predictive features in the trained weights) - the ecosystem carries a tooling-bias layer nobody accounts for.
- **Why important:** Meta-transparency for the entire benchmark ecosystem, and a concrete confounder to control in cross-dataset studies.
- **Why possibly novel:** Ecosystem-scale tool forensics is UNVERIFIED - needs lit search.
- **Minimal experiment:** Assemble tool-labeled mask corpora (known-provenance datasets), train fingerprint classifier, survey 15 public datasets, probe trained segmenters for tool-feature encoding.
- **Main risk:** Provenance ground truth for older datasets is scarce; bootstrap from documented cases.
- **Mutated from:** W2-A-0156

### W2-A-0225 - The 100-labeled-pixels challenge: map the extreme-low-budget frontier of segmentation to find where each supervision paradigm collapses.

- **Problem:** Label-efficiency papers compare at comfortable budgets (1-10% of pixels); the extreme regime (say 100 labeled pixels per class total) has no map, though it reveals which paradigms extract the most information per label bit and where each breaks.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at extreme budgets, paradigm rankings invert relative to comfortable budgets (foundation-feature probing dominates fine-tuning; consistency methods collapse entirely below a measurable threshold; point-supervision beats mask-supervision per pixel), producing a budget-vs-paradigm phase map with actionable regime boundaries - the field's efficiency conclusions are budget-regime-specific and do not extrapolate down.
- **Why important:** Scientific applications (rare phenomena, expert-only labels) live in the extreme regime the literature never visits; the phase map is their missing guidance.
- **Why possibly novel:** Extreme-budget phase mapping is UNVERIFIED - needs lit search.
- **Minimal experiment:** Budget ladder from 100 to 100k labeled pixels across 5 paradigms on 3 datasets, plot the phase map with collapse thresholds.
- **Main risk:** High variance at tiny budgets demands many seeds; compute cost is real but bounded.

## C10-domain-shift

### W2-A-0226 - Decompose any domain gap into photometric, geometric, and semantic components with controlled re-rendering - then publish the composition per benchmark.

- **Problem:** 'Domain gap' is treated as a scalar, but its composition (color/sensor vs viewpoint/layout vs class-distribution differences) determines which adaptation method can possibly work - and no benchmark reports its composition.
- **Core hypothesis (falsifiable):** HYPOTHESIS: using controlled transformations (photometric transplants, geometry-preserving style transfer, label-distribution reweighting), each popular shift benchmark decomposes into stable component fractions; adaptation methods' gains align with the component they address (photometric methods win only on photometric-heavy gaps), explaining most of the notorious inconsistency of UDA results across benchmarks.
- **Why important:** Gives the field a diagnostic vocabulary: measure your gap's composition first, then choose methods - replacing the current lottery.
- **Why possibly novel:** Systematic gap-composition accounting across benchmarks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Build the three controlled transforms, measure component fractions on 6 shift pairs, correlate method-gain profiles with compositions.
- **Main risk:** Components interact (not perfectly separable); report interaction terms honestly.

### W2-A-0227 - Sim2real gap lives in materials, not geometry: hybrid renders (real textures on synthetic geometry, and vice versa) isolate what synthetic data gets wrong.

- **Problem:** Synthetic training data underperforms real data for segmentation, but WHERE the deficit lives (shape/layout realism vs material/lighting appearance) is folklore, not measurement - though it determines where rendering effort should go.
- **Core hypothesis (falsifiable):** HYPOTHESIS: crossing the factors (synthetic geometry + real-photograph textures vs real geometry + synthetic materials) shows the material/appearance factor explains the large majority of the sim2real segmentation gap, geometry realism contributing little - implying cheap geometry with photo-real materials is the optimal synthetic-data recipe, opposite to where most rendering compute goes.
- **Why important:** Synthetic data budgets are large and misallocated if the geometry-heavy intuition is wrong; factor attribution redirects the spend.
- **Why possibly novel:** Factor-crossed hybrid rendering attribution for dense prediction is UNVERIFIED - needs lit search.
- **Minimal experiment:** Construct the 2x2 render conditions in a driving simulator with texture transplants, train per cell, evaluate on real benchmarks.
- **Main risk:** Texture transplantation introduces its own artifacts; needs artifact-matched controls.

### W2-A-0228 - Night failure is mostly ISP failure: models degrade on processed JPEGs, not on darkness itself - RAW-domain evaluation separates the two.

- **Problem:** Nighttime segmentation failure is attributed to insufficient light, but consumer ISP pipelines (denoising, tone mapping, white balance) transform night captures aggressively and variably; models may fail on ISP artifacts rather than photon scarcity.
- **Core hypothesis (falsifiable):** HYPOTHESIS: evaluating on RAW-processed-with-fixed-simple-pipeline night images recovers a substantial fraction of the day-night performance drop relative to camera-ISP JPEGs (the ISP is a major failure contributor), and the recovered fraction varies by ISP vendor - night robustness research is partly chasing vendor-specific artifacts.
- **Why important:** If the ISP is a first-order factor, night perception should be co-designed with capture pipelines, and existing night benchmarks measure entangled camera stacks rather than vision capability.
- **Why possibly novel:** ISP-vs-photon attribution for night dense prediction is UNVERIFIED - needs lit search.
- **Minimal experiment:** Use datasets with RAW night captures (or collect paired RAW/JPEG), evaluate models across processing pipelines, decompose the drop.
- **Main risk:** RAW night data with segmentation GT is scarce; may need targeted collection with transfer-annotated labels.

### W2-A-0229 - Camera ISP fingerprint as an unbenchmarked shift axis: same scenes through different phone pipelines measurably move dense predictions.

- **Problem:** Every camera brand applies proprietary processing (sharpening, denoising, color science). Models trained on one ISP mix may silently degrade on another - an axis orthogonal to weather/geography that no benchmark isolates.
- **Core hypothesis (falsifiable):** HYPOTHESIS: capturing identical scenes with multiple devices (tripod-locked) and evaluating fixed models shows per-model prediction shifts comparable in magnitude to mild weather shift, with boundary-level metrics most affected (sharpening halos) - ISP variation is a first-class shift axis deserving its own benchmark. UNVERIFIED - needs lit search on existing cross-device studies.
- **Why important:** Deployments span device fleets; an ignored first-order shift axis means fleet-wide QA is currently blind to a real variance source.
- **Why possibly novel:** Tripod-locked cross-ISP dense-prediction benchmarking appears missing.
- **Minimal experiment:** Capture 200 locked scenes with 5 devices, run model zoo, quantify prediction divergence and metric movement per device pair.
- **Main risk:** Perfect pixel alignment across devices is impossible (optics differ); evaluate with alignment-tolerant metrics.

### W2-A-0230 - BN-statistics adaptation helps photometric shift but actively harms semantic shift: map when the cheapest TTA trick becomes poison.

- **Problem:** Test-time normalization-statistics adaptation is the default cheap fix under shift, applied indiscriminately; its failure conditions (when target statistics differences reflect content, not style) are anecdotal.
- **Core hypothesis (falsifiable):** HYPOTHESIS: across a controlled shift taxonomy, statistics adaptation improves photometric/sensor shifts consistently but DEGRADES performance under label-distribution and content shifts (it 'corrects' real signal), with the harm predictable from the correlation between channel statistics and class evidence - yielding a practical pre-test that decides whether to adapt.
- **Why important:** A deploy-time go/no-go test for the most-used adaptation trick prevents silent self-inflicted damage.
- **Why possibly novel:** Shift-type-conditional harm characterization with a predictive pre-test is UNVERIFIED - needs lit search.
- **Minimal experiment:** Apply statistics adaptation across shift-type ladders (photometric, weather, geographic, class-mix), measure signed effects, validate the harm predictor.
- **Main risk:** Modern normalization-free architectures reduce the scope; include them for completeness.

### W2-A-0231 - Geographic shift decomposes into stuff-appearance and thing-longtail: cross-region failure has two mechanisms needing opposite remedies.

- **Problem:** Models trained in one region degrade in another, but the degradation conflates two mechanisms - unfamiliar background appearance (road surfaces, vegetation) and unfamiliar object variants (vehicle types, dress) - which respond to different fixes (style adaptation vs data collection).
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-class cross-region degradation splits bimodally - stuff classes fail by appearance statistics (fixable by style-level adaptation, no new labels) while thing classes fail by variant novelty (fixable only by target-region examples) - and the split predicts which classes any adaptation method can rescue, explaining heterogeneous published UDA results class-by-class.
- **Why important:** Region expansion is the standard deployment problem (driving, agriculture, mapping); a mechanism-level failure map converts adaptation from alchemy to engineering.
- **Why possibly novel:** Mechanism-split analysis of geographic shift per class is UNVERIFIED - needs lit search.
- **Minimal experiment:** Cross-evaluate on multi-region datasets (Mapillary regions, IDD vs Cityscapes), classify per-class failures by style-transfer-recoverability, validate the two-mechanism model.
- **Main risk:** Some classes fail by both mechanisms; use continuous mixture attribution, not hard split.

### W2-A-0232 - Transferability is spatially structured: sky transfers, road texture does not - build per-region transfer maps and adapt only what fails.

- **Problem:** Adaptation methods treat images uniformly, but shift affects scene regions unequally (sky is universal; ground textures are local). Spatially-selective adaptation could preserve what already transfers - if transfer geography were measured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-pixel cross-domain performance retention has strong reproducible spatial/semantic structure (a transfer map stable across model families), uniform adaptation methods measurably damage well-transferring regions while fixing bad ones (netting less than possible), and transfer-map-gated adaptation beats uniform adaptation at matched compute.
- **Why important:** Reveals adaptation's hidden collateral damage and provides a general recipe (measure, gate, adapt) applicable to every UDA method.
- **Why possibly novel:** Transfer-geography mapping with gated adaptation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Compute per-class/per-region retention across 4 shift pairs and 3 models, verify map stability, implement gated variant of one standard UDA method.
- **Main risk:** Gating needs target labels to validate - use held-out target labels for science, proxy signals for the method.
- **Mutated from:** W2-A-0226

### W2-A-0233 - Weather shifts do not compose additively: rain+night is worse than rain-effect plus night-effect - measure the interaction matrix.

- **Problem:** Robustness studies test single factors (rain OR night OR fog), but deployment presents combinations; if degradations interact super-additively, single-factor benchmarks systematically understate real risk - the interaction structure is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: factorial evaluation over weather-condition combinations reveals significant super-additive interactions for specific pairs (night amplifies rain's effect via reflections; fog amplifies backlight), the interaction matrix is stable across models (physics-driven, not model-driven), and worst-case combinations are predictable from single-factor physics rather than requiring exhaustive testing.
- **Why important:** Safety validation currently extrapolates from single factors; a measured interaction matrix corrects the risk model where it is most wrong.
- **Why possibly novel:** Factorial interaction analysis of weather robustness is UNVERIFIED - needs lit search.
- **Minimal experiment:** Use condition-rich datasets (ACDC, BDD) plus controlled synthesis for missing cells, fit interaction terms per class, test cross-model stability.
- **Main risk:** Natural data has sparse combination coverage; synthesis fills cells but needs realism validation.

### W2-A-0234 - Geometry as the shift-invariant channel: does routing through depth (RGB to depth to segmentation) transfer better than direct RGB segmentation?

- **Problem:** Appearance shifts (weather, sensors, geography) barely change scene geometry. If segmentation via an intermediate geometric representation retains more accuracy under shift, the invariance structure of the task itself becomes exploitable - a question about representations, not methods.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a pipeline segmenting from predicted depth+normals (with a thin appearance channel) loses less under photometric/weather shift than matched direct-RGB models (geometry mediates invariance), but pays a measurable in-distribution penalty on texture-defined classes - a quantified invariance-vs-acuity tradeoff with a computable optimal mixing ratio per deployment shift profile.
- **Why important:** Establishes which invariances are worth buying at what acuity price - a design law for robustness rather than another method.
- **Why possibly novel:** Geometry-mediated transfer quantification for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train matched direct and geometry-mediated segmenters, evaluate across shift ladders, fit the tradeoff frontier and mixing-ratio optimum.
- **Main risk:** Depth estimators carry their own shift sensitivity; measure and account for it explicitly.

### W2-A-0235 - Benchmark the shift-measures: which unsupervised domain-distance metric actually predicts segmentation performance drop?

- **Problem:** Teams estimate deployment risk with feature-space distances (FID-like, MMD, proxy accuracies), but these metrics have never been systematically validated as PREDICTORS of dense-prediction degradation - the meta-question the field skipped.
- **Core hypothesis (falsifiable):** HYPOTHESIS: common distribution distances correlate weakly with segmentation drop across a broad shift matrix (r<0.5), because they weight global appearance over the boundary- and minority-class evidence segmentation depends on; a dense-prediction-specific measure (built from label-free prediction statistics like churn, margin distributions, connected-component statistics) predicts drops substantially better - and the validated predictor becomes a deployment tool.
- **Why important:** Every go/no-go deployment decision under shift implicitly trusts some distance measure; validating them is basic metrological hygiene the field lacks.
- **Why possibly novel:** Predictive-validity benchmarking of shift measures for dense tasks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Assemble 30+ source-target segmentation pairs with known drops, correlate candidate measures, build and validate the dense-specific predictor.
- **Main risk:** Conclusions depend on shift-pair diversity; deliberately include adversarially-mild and severe pairs.

### W2-A-0236 - Adaptation hysteresis: a model adapted A-to-B differs from one trained at B directly, and the path-dependence predicts continual-adaptation drift.

- **Problem:** Continual test-time adaptation walks models through condition sequences (day to dusk to night). Whether the endpoint depends on the path (hysteresis) - and whether looping conditions returns the model to its start - determines if continual adaptation is stable or secularly drifting.
- **Core hypothesis (falsifiable):** HYPOTHESIS: adapted models exhibit measurable hysteresis (A-to-B-to-A does not recover the original A performance; the gap grows with loop count - secular drift), drift accumulates in specific layers (normalization and early convolutions), and periodic anchor-replay eliminates it at negligible cost - continual adaptation without anchoring is quantifiably unsafe over long deployments.
- **Why important:** Continual TTA is heading into products; its long-horizon stability has never been characterized, and drift would be a slow silent failure.
- **Why possibly novel:** Hysteresis/drift analysis of adaptation dynamics is UNVERIFIED - needs lit search.
- **Minimal experiment:** Cycle models through condition loops (synthetic + ACDC sequences), measure return-gap growth, localize drifting parameters, test anchor-replay.
- **Main risk:** Results depend on the specific TTA algorithm; cover the 3 main families.

### W2-A-0237 - Annotation-convention shift masquerades as domain shift: cross-country dataset gaps are partly label-sociology gaps.

- **Problem:** Cross-dataset evaluation (Cityscapes to IDD to BDD) conflates appearance shift with annotation-convention differences (what counts as 'road' vs 'parking'; curb handling; rider/vehicle splits) - the convention fraction of the measured gap is unknown.
- **Core hypothesis (falsifiable):** HYPOTHESIS: re-annotating a sample of target-domain images under the SOURCE dataset's written protocol recovers a substantial fraction (>25%) of the measured cross-dataset performance gap for affected classes - meaning published cross-domain numbers systematically overstate appearance-driven failure and adaptation methods get credit for learning label conventions.
- **Why important:** Separates two entangled research problems (visual robustness vs ontology mapping) that need entirely different solutions.
- **Why possibly novel:** Protocol-controlled re-annotation accounting for domain-gap decomposition is UNVERIFIED - needs lit search.
- **Minimal experiment:** Re-annotate 300 target images under source protocol, re-evaluate the gap per class, tabulate the convention fraction.
- **Main risk:** Written protocols under-specify actual annotator behavior; use annotators trained on source-dataset examples.
- **Mutated from:** W2-A-0108

### W2-A-0238 - Resolution regime shift: models trained at 1024px meet 4K deployment - effective receptive fields misalign with object scales in a predictable, correctable way.

- **Problem:** Training and deployment resolutions diverge (datasets are downsampled; cameras improve). The resulting scale mismatch between learned receptive fields and presented object sizes is a shift axis handled today by ad hoc resizing folklore.
- **Core hypothesis (falsifiable):** HYPOTHESIS: performance under resolution shift follows a predictable curve in the ratio of object-pixels-per-receptive-field between train and test, is asymmetric (upscale deployment hurts more than downscale), and optimal test-time resizing is computable from dataset object-size statistics alone - replacing folklore with a scaling rule that recovers most of the mismatch loss.
- **Why important:** Resolution mismatch is ubiquitous and silently mishandled; a validated rule converts a recurring engineering headache into a formula.
- **Why possibly novel:** Dimensionless resolution-shift law for dense prediction is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train at multiple resolutions, test across a resolution ladder, fit the law in ratio coordinates, validate the resizing rule on held-out datasets.
- **Main risk:** Architecture-dependent effects (ViT patchification vs CNN strides) may split the law; fit per family.
- **Mutated from:** W2-A-0011

### W2-A-0239 - Compression asymmetry: benchmarks are compressed, deployment streams are rawer - models overfit artifacts they will not see, an inverted shift nobody tests.

- **Problem:** Shift studies assume deployment is degraded relative to clean benchmarks, but for compression the arrow can invert: web-scraped training data is heavily compressed while deployment feeds (industrial cameras, medical scanners) are near-lossless - models may DEPEND on compression artifacts.
- **Core hypothesis (falsifiable):** HYPOTHESIS: models trained on web-compressed data measurably degrade on lossless imagery (artifact dependence: denoising-like artifacts act as learned features), the effect concentrates in texture-defined classes, and light recompression of deployment inputs (deliberately degrading them toward training statistics) IMPROVES accuracy - a counter-intuitive, immediately testable prescription.
- **Why important:** The recompression prescription is deployable in an afternoon if validated; the phenomenon also reframes 'data quality' - matching beats maximizing.
- **Why possibly novel:** Inverted compression-shift analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Evaluate web-trained models on lossless captures vs recompressed versions of the same, measure the signed effect per class.
- **Main risk:** Effect size may be small for modern diverse training sets; report honestly across training-data eras.
- **Mutated from:** W2-A-0018

### W2-A-0240 - Where does foundation-feature robustness come from - data diversity or training objective? Checkpoint-ladder analysis separates the credit.

- **Problem:** DINOv2/SAM features transfer robustly, credited vaguely to 'scale'. Whether robustness accrues from data diversity, objective choice, or training duration - decomposable via public checkpoint series - matters for what to invest in next.
- **Core hypothesis (falsifiable):** HYPOTHESIS: analyzing robustness (shift-retention of downstream segmentation) across public checkpoint ladders and matched-data reruns shows data diversity dominates objective choice by a wide margin (matched-data models converge in robustness across objectives; matched-objective models diverge with data), and robustness saturates earlier in training than in-distribution accuracy - actionable credit assignment for the ecosystem's biggest investment question.
- **Why important:** Billions of compute dollars ride on the diversity-vs-objective question; even partial credit assignment from existing artifacts is high-value.
- **Why possibly novel:** Robustness credit-assignment via checkpoint forensics is UNVERIFIED - needs lit search.
- **Minimal experiment:** Probe segmentation robustness across available checkpoint series (DINO variants, MAE, CLIP at multiple data scales), fit robustness-accrual curves per factor where artifacts allow.
- **Main risk:** Public artifacts confound factors; where reruns are needed, use small-scale matched experiments and extrapolate cautiously.

### W2-A-0241 - Predict per-pixel performance drop from the source model alone: performance forecasting as a first-class dense-prediction task.

- **Problem:** Before deployment, teams need per-region risk maps for the target domain without target labels - a forecasting task distinct from adaptation, with no benchmark or standard method for dense prediction.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-pixel drop is forecastable (correlation >0.6 with realized drop) from source-model-computable signals (feature-space distance to training manifold, margin statistics, augmentation sensitivity), forecast errors are themselves structured (over-optimistic on novel classes, over-pessimistic on style variation) - and a benchmark of forecasting quality would expose large differences between signals the field currently treats as interchangeable.
- **Why important:** Risk forecasting is the deployment decision-maker's actual question; formalizing it as a benchmarked task channels research toward what practitioners need.
- **Why possibly novel:** Dense performance-forecasting benchmark construction is UNVERIFIED - needs lit search.
- **Minimal experiment:** Build forecast-vs-realized evaluation on 10 shift pairs, compare 6 forecasting signals, publish the benchmark protocol.
- **Main risk:** Forecast quality varies by shift type; the benchmark must stratify to avoid misleading averages.
- **Mutated from:** W2-A-0235

### W2-A-0242 - Natural adversarial weather mining: search real archives for the worst-case conditions per model, instead of averaging over benchmark weather.

- **Problem:** Robustness is reported as averages over available conditions, but safety depends on worst cases; mining large unlabeled archives (webcams, dashcams) for each model's WORST natural conditions - and checking if they are shared across models - is unexplored.
- **Core hypothesis (falsifiable):** HYPOTHESIS: guided search over unlabeled archives (optimizing a label-free failure proxy) discovers natural condition clusters where model performance is far below benchmark-average robustness numbers (hidden failure modes: specific sun angles, wet-road glare geometries, mixed precipitation), and a substantial fraction of these clusters transfer across model families - natural worst cases are systematic, findable, and shared.
- **Why important:** Averages hide the failures that cause accidents; a mining methodology gives safety teams a repeatable worst-case discovery tool.
- **Why possibly novel:** Label-free worst-case mining in natural archives for dense prediction is UNVERIFIED - needs lit search.
- **Minimal experiment:** Implement failure-proxy-guided search over webcam archives, verify mined clusters with spot annotation, test cross-model transfer of hardness.
- **Main risk:** Failure proxies may mine proxy-artifacts rather than true failures; spot annotation is the essential control.

### W2-A-0243 - Time-of-day is a hidden label prior: models learn that parked cars appear at night and fail on time-swapped scenes - anti-causal shortcut measurement.

- **Problem:** Class distributions correlate with capture time (delivery trucks by day, parked rows by night); models may encode time-conditioned priors rather than appearance evidence, failing when the correlation breaks (night football game, daytime empty streets).
- **Core hypothesis (falsifiable):** HYPOTHESIS: models infer global time-of-day from image statistics and modulate class priors accordingly (probeable: time is linearly decodable from features and causally influences predictions via controlled relighting), and prior-override errors occur at measurable rates on time-atypical scenes - a quantifiable anti-causal shortcut with a stress-test suite as the deliverable.
- **Why important:** Time-atypical scenes (emergencies, events) are exactly when perception must work; a validated stress suite would catch this failure class pre-deployment.
- **Why possibly novel:** Time-conditioned prior measurement for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Probe time decodability in features, evaluate on curated time-atypical scenes, use relighting interventions to separate appearance from prior effects.
- **Main risk:** Relighting realism; complement with natural time-atypical collections.
- **Mutated from:** W2-A-0199

### W2-A-0244 - Per-class transfer matrix of synthetic data: adding simulation helps some real classes and quantifiably harms others - the negative-transfer ledger.

- **Problem:** Synthetic data is added wholesale on the assumption of average benefit, but per-class effects (sim vehicles helping, sim pedestrians hurting via uncanny appearance) are rarely itemized - teams cannot make class-level decisions.
- **Core hypothesis (falsifiable):** HYPOTHESIS: mixed real+synthetic training produces a stable per-class signed-effect ledger (consistent across seeds and architectures), harms concentrate in classes where synthetic appearance diverges most from real (measurable via per-class feature distances), and class-selective synthetic mixing (include only positive-ledger classes) beats wholesale mixing by a meaningful margin - synthetic data needs itemized accounting, not blanket adoption.
- **Why important:** Turns synthetic-data decisions from faith into ledger-driven engineering, with immediate gains from selective mixing.
- **Why possibly novel:** Signed per-class transfer accounting with selective-mixing validation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train real-only vs mixed vs class-selective mixes on driving data (GTA/SYNTHIA + Cityscapes), tabulate signed ledgers, validate the divergence predictor.
- **Main risk:** Ledger stability across simulators must be tested, not assumed; use two simulators.

### W2-A-0245 - UDA methods overfit their development benchmark pair: rank correlation across novel shift pairs is the reproducibility number nobody reports.

- **Problem:** Unsupervised domain adaptation methods are developed and tuned overwhelmingly on GTA-to-Cityscapes; whether their rankings hold on fresh shift pairs (different domains, modalities, directions) is the field's unasked generalization question about itself.
- **Core hypothesis (falsifiable):** HYPOTHESIS: re-running leading UDA methods with frozen hyperparameters on 6 novel shift pairs yields low rank correlation with their canonical-benchmark ranking (methods overfit the development pair's shift composition), while simple baselines (strong augmentation, self-training) rank far more stably - the field's method-ranking signal is substantially benchmark-specific noise.
- **Why important:** A meta-scientific audit determining whether UDA progress is real; stability-ranked methods are what practitioners should actually adopt.
- **Why possibly novel:** Cross-pair rank-stability auditing of UDA is UNVERIFIED - needs lit search.
- **Minimal experiment:** Reproduce 8 UDA methods, evaluate frozen on novel pairs (medical, aerial, reversed directions), compute rank correlations and stability scores.
- **Main risk:** Frozen hyperparameters may be unfair to methods needing tuning - but that itself is a deployability finding; report both regimes.

### W2-A-0246 - Metric anchors survive shift: physical size priors (via camera geometry) remain valid when appearance shifts - measure how much of robustness they could carry.

- **Problem:** Appearance shifts destroy learned texture cues, but physical regularities (pedestrians ~1.7m, lane widths standardized) survive any weather; how much segmentation robustness metric-scale priors could contribute is unquantified because models entangle scale with appearance.
- **Core hypothesis (falsifiable):** HYPOTHESIS: probing shows current models' implicit size priors degrade under shift (they are appearance-entangled, not geometric), while models given explicit metric conditioning (camera intrinsics + horizon) retain class discrimination under severe appearance shift measurably better - the shift-invariant information in metric geometry is real, quantifiable, and currently unexploited.
- **Why important:** Identifies an invariance channel that is free at deployment (intrinsics are known) and orthogonal to all appearance-based robustness work.
- **Why possibly novel:** Metric-prior shift-invariance quantification is UNVERIFIED - needs lit search.
- **Minimal experiment:** Probe size-prior stability under shift ladders; train matched models with/without metric conditioning; compare shift retention per class.
- **Main risk:** Intrinsics conditioning helps mainly ground-plane-anchored classes; scope claims accordingly.
- **Mutated from:** W2-A-0234

### W2-A-0247 - The domain-randomization sweet spot is predictable: too much randomization hurts, and the optimum tracks target-domain variance - fit the curve.

- **Problem:** Domain randomization strength is tuned blindly; the community knows extremes fail (too little = overfit, too much = unlearnable invariance) but has no predictive theory of the optimum's location.
- **Core hypothesis (falsifiable):** HYPOTHESIS: transfer performance vs randomization strength is reliably non-monotonic with a single optimum whose location scales with measured target-domain variance along each factor (color, texture, lighting independently), so the optimal randomization recipe is computable from a small unlabeled target sample - replacing grid search with measurement.
- **Why important:** Randomization tuning consumes large simulation budgets; a predictive rule compresses it to one estimation step, and the variance-matching principle would generalize across factors.
- **Why possibly novel:** Variance-matched optimal-randomization law is UNVERIFIED - needs lit search.
- **Minimal experiment:** Sweep per-factor randomization strengths training on synthetic driving data, locate optima across target datasets with different measured variances, test the scaling law.
- **Main risk:** Factor interactions may shift optima jointly; fit both marginal and joint models.

### W2-A-0248 - Amplitude-swap explains most photometric-shift benefit - but where does PHASE matter? Locate the residual that frequency-domain adaptation cannot touch.

- **Problem:** Fourier amplitude transfer between domains is a known cheap adaptation trick (KNOWN: FDA, Yang & Soatto CVPR 2020 - existence confident, details need verification); what remains AFTER amplitude alignment - the phase-borne shift component - has not been characterized, though it defines the method's ceiling.
- **Core hypothesis (falsifiable):** HYPOTHESIS: after optimal amplitude alignment, residual cross-domain error concentrates in phase-borne structures (layout differences, object-shape variants, edge geometry), is class-structured (things retain more residual than stuff), and no amplitude-space method can reduce it - establishing a measurable decomposition of photometric vs structural shift with amplitude methods' ceiling made explicit.
- **Why important:** Tells the field precisely what the popular cheap trick cannot fix, preventing wasted iterations and directing effort at the structural residual.
- **Why possibly novel:** Phase-residual characterization of shift is UNVERIFIED - needs lit search.
- **Minimal experiment:** Apply exhaustive amplitude alignment on 5 shift pairs, decompose residual error by class and spatial-frequency band, compare against phase-perturbation sensitivity curves.
- **Main risk:** Amplitude/phase decomposition is a linear-systems view of a nonlinear problem; treat as first-order analysis and validate conclusions behave stably.

### W2-A-0249 - Part of every 'domain gap' is an annotation-quality gap: target-domain labels are often worse, inflating measured shift.

- **Problem:** Cross-domain evaluation assumes both domains' labels are equally good, but target datasets (developing-region driving data, rare-modality medical sets) often have younger annotation pipelines - measured 'domain gaps' partially reflect reference-quality differences.
- **Core hypothesis (falsifiable):** HYPOTHESIS: expert re-annotation of target-domain test samples to source-grade quality reduces measured domain gaps by a nontrivial fraction (>15% of the gap for at least some benchmark pairs), and the label-quality component is diagnosable WITHOUT re-annotation via model-consensus statistics - separating true shift from reference noise in every cross-domain claim.
- **Why important:** Domain-gap numbers steer research priorities and product decisions; systematically inflated gaps misdirect both.
- **Why possibly novel:** Reference-quality decomposition of measured domain gaps is UNVERIFIED - needs lit search.
- **Minimal experiment:** Re-annotate 200 target test images at source-grade for 2 benchmark pairs, recompute gaps, validate the consensus-based diagnostic against realized corrections.
- **Main risk:** Which pairs have quality asymmetry is unknown a priori; survey with the diagnostic first, then re-annotate the flagged pairs.
- **Mutated from:** W2-A-0200

### W2-A-0250 - Camera height is a geometric shift solvable in closed form: dashcam-to-bodycam transfer needs homography priors, not learned adaptation.

- **Problem:** Viewpoint-height shift (vehicle roof vs handheld vs robot-dog height) is treated with generic adaptation machinery, though it is substantially a known geometric transformation of ground-plane layout - suggesting geometry should replace learning for this axis.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for height shifts, ground-plane homography-based training augmentation (exact geometric reprojection given height priors) recovers more of the cross-height performance gap than generic UDA methods at a fraction of the complexity, and the residual after geometric correction isolates the truly appearance-borne component (occlusion pattern changes) - geometry-first decomposition beats learning-first for geometrically-caused shifts.
- **Why important:** A class of shifts where the right answer is 100-year-old projective geometry would recalibrate the learn-everything reflex, with immediate value for robot/drone deployment from vehicle-collected data.
- **Why possibly novel:** Geometric-vs-learned adaptation head-to-head for height shift is UNVERIFIED - needs lit search.
- **Minimal experiment:** Construct height-paired data (multi-mount captures or synthetic), compare homography augmentation vs 3 UDA methods on cross-height segmentation.
- **Main risk:** Homography assumes planar ground; cluttered 3D scenes violate it - measure where the assumption breaks.

## C11-weak-semi-self

### W2-A-0251 - When is the whole object recoverable from image-level labels alone? Formalize and measure the part-to-whole information gap of CAM-style supervision.

- **Problem:** Class-activation-based weak supervision finds discriminative parts, not whole objects (KNOWN limitation). But the field lacks a principled account of WHEN whole-object extent is even inferable from image labels - which classes are structurally recoverable and which need shape priors.
- **Core hypothesis (falsifiable):** HYPOTHESIS: whole-object recoverability from image-level supervision is predicted by a measurable class property - the mutual information between object presence and non-discriminative object regions' appearance (context-part coupling) - producing a per-class recoverability score that forecasts weak-supervision performance before training and identifies classes where NO CAM-descendant can succeed.
- **Why important:** Ends the per-method trial-and-error of weakly-supervised segmentation with a data-side impossibility diagnostic - saving effort and setting honest expectations.
- **Why possibly novel:** An information-theoretic recoverability criterion validated against method outcomes is UNVERIFIED - needs lit search.
- **Minimal experiment:** Estimate context-part coupling for 30 classes (via masked-region prediction proxies), correlate with published + reproduced weak-supervision per-class results.
- **Main risk:** Estimating the information quantity is itself model-dependent; triangulate with multiple estimators.

### W2-A-0252 - Error inheritance coefficient: measure how teacher mistakes replicate into students under pseudo-labeling, per error type.

- **Problem:** Self-training assumes student models average away teacher noise, but teacher errors are systematic, and their inheritance rate (which error types replicate vs wash out) has never been itemized for segmentation.
- **Core hypothesis (falsifiable):** HYPOTHESIS: boundary-style errors and context-prior errors inherit at high rates (>70% persistence into students) while stochastic errors wash out, the inheritance coefficient per error type is stable across datasets, and it predicts the ceiling of iterated self-training in advance - pseudo-label pipelines have a computable error-genetics.
- **Why important:** Semi-supervised pipelines dominate practical segmentation; knowing which teacher flaws are heritable tells teams what to fix BEFORE distillation, not after.
- **Why possibly novel:** Error-type-resolved inheritance measurement is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train teacher, categorize its errors (boundary/semantic/context), train students on pseudo-labels, measure per-type persistence across two generations.
- **Main risk:** Error categorization is partly subjective; use automatic taxonomies with human validation.

### W2-A-0253 - Why does consistency regularization work - decision-boundary geometry or augmentation coverage? A controlled disentanglement.

- **Problem:** Consistency training (agree across augmentations) is the semi-supervised workhorse, credited to two mechanisms with different implications - smoothing decision boundaries in low-density regions vs implicitly expanding data coverage - never separated experimentally for dense prediction.
- **Core hypothesis (falsifiable):** HYPOTHESIS: holding augmentation-space coverage fixed while varying the consistency term (and vice versa) shows coverage explains most of the gain (consistency acts primarily as data amplification, not geometric smoothing), predicting that consistency helps only where augmentations bridge real distribution gaps - a testable mechanistic account that would demystify a ubiquitous method.
- **Why important:** Mechanism determines when the method fails (augmentation-unreachable variation); the field applies it blind to this boundary.
- **Why possibly novel:** Coverage-vs-geometry disentanglement for dense consistency training is UNVERIFIED - needs lit search.
- **Minimal experiment:** Factorial design: supervised-with-augmentation vs consistency-with-matched-augmentation across augmentation families, measure gain attribution on 3 datasets.
- **Main risk:** Perfectly matching coverage across arms is subtle; use augmentation-distribution diagnostics to verify the control.

### W2-A-0254 - Does object-centric data cause segmentation emergence in SSL? Train DINO-style models on scene-only crops and watch attention objects disappear (or not).

- **Problem:** Self-supervised ViTs develop object-segmenting attention (KNOWN: DINO attention maps, Caron et al. 2021). Whether emergence requires object-centric training photos (ImageNet's bias) or arises from the objective on any natural data is an open causal question about where 'free objects' come from.
- **Core hypothesis (falsifiable):** HYPOTHESIS: training identical SSL recipes on deliberately de-object-centrified data (scene crops with no dominant object, matched scale/diversity) substantially degrades emergent objectness (attention-mask quality drops by half or more), demonstrating that 'objects for free' are inherited from photographic framing bias, not discovered by the objective - with direct implications for SSL on scene-heavy domains (driving, aerial, medical).
- **Why important:** If emergence is data-borne, domains without object-centric framing cannot expect it - explaining known SSL disappointments there and redirecting pretraining design.
- **Why possibly novel:** Controlled data-causality test for objectness emergence is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train matched small ViTs (DINO recipe) on object-centric vs scene-crop corpora at equal scale, compare emergent attention segmentation quality.
- **Main risk:** Emergence may need scale beyond affordable reruns; use the largest feasible scale and report scaling caveats.

### W2-A-0255 - Unsupervised segmentation evaluation is circular: Hungarian matching to GT classes rewards granularity luck - novel-class evaluation breaks the illusion.

- **Problem:** Unsupervised segmentation reports mIoU after optimally matching discovered clusters to GT classes, which silently forgives arbitrary granularity choices and rewards matching the benchmark's ontology by chance - the evaluation partially measures its own matching step.
- **Core hypothesis (falsifiable):** HYPOTHESIS: current unsupervised methods' rankings are unstable under matching-protocol changes (over/under-clustering penalties, novel-class holdouts), and a matching-free evaluation (consistency, boundary agreement, cross-image co-segmentation coherence) reorders the field while better predicting downstream usefulness of discovered segments - a substantial fraction of reported 'unsupervised understanding' is matching artifact.
- **Why important:** Unsupervised segmentation guides pretraining research; if its measurement is circular, the field is steering by a broken compass.
- **Why possibly novel:** Matching-protocol sensitivity audit for unsupervised segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Re-evaluate 6 unsupervised methods under matching-protocol variants and matching-free criteria, quantify rank instability and downstream predictivity.
- **Main risk:** Matching-free criteria need their own validation; anchor with human usefulness judgments on discovered segments.

### W2-A-0256 - What fraction of supervised segmentation is recoverable from motion alone? Train with only optical-flow-derived boundaries and count the percentage.

- **Problem:** Motion boundaries supervise object boundaries for free in video, but the ceiling of motion-only supervision - what percentage of fully-supervised static segmentation it recovers, and for which classes - has never been established as a reference number.
- **Core hypothesis (falsifiable):** HYPOTHESIS: motion-derived supervision recovers a class-dependent fraction of supervised performance with a bimodal structure - articulated/mobile classes recover >70% while static-only classes (furniture, buildings) recover near zero - and mobile-class features transfer to static instances of the same classes (motion teaches appearance), quantifying exactly what the 'motion as teacher' hypothesis delivers.
- **Why important:** A reference decomposition for the oldest idea in developmental vision applied to modern models - tells the field which supervision motion can actually replace.
- **Why possibly novel:** Class-resolved recovery accounting of motion-only supervision is UNVERIFIED - needs lit search.
- **Minimal experiment:** Derive motion pseudo-labels from unlabeled video (flow discontinuities + temporal grouping), train static segmenters, tabulate per-class recovery on standard benchmarks.
- **Main risk:** Flow quality gates the pseudo-labels; use multiple flow methods to bound sensitivity.

### W2-A-0257 - Depth discontinuities vs semantic boundaries: map where they disagree, because disagreement zones are exactly what depth-based self-supervision cannot teach.

- **Problem:** Depth edges are used as free boundary supervision, assuming co-location with semantic boundaries; the systematic disagreement structure (material boundaries on flat surfaces, depth edges inside objects) defines the method's blind spots but has never been atlased.
- **Core hypothesis (falsifiable):** HYPOTHESIS: depth-semantic boundary disagreement follows a stable taxonomy (co-planar material transitions, self-occlusion edges within objects, contact boundaries) with measurable per-class rates, and depth-supervised models' errors concentrate precisely in the disagreement atlas - making the atlas a predictive map of where depth supervision fails and where photometric cues must take over.
- **Why important:** Depth self-supervision is scaling with cheap depth sensors and monocular estimators; its predictable blind spots should be known before the ecosystem leans on it.
- **Why possibly novel:** Systematic disagreement atlasing between boundary types is UNVERIFIED - needs lit search.
- **Minimal experiment:** On RGB-D datasets with semantic GT, compute the boundary disagreement taxonomy, train depth-boundary-supervised models, verify error concentration in atlas zones.
- **Main risk:** Sensor depth noise inflates disagreement estimates; use high-quality depth subsets for the atlas.

### W2-A-0258 - Supervision mixing is super-additive: image tags plus a few points beat the sum of their separate contributions - map the synergy matrix.

- **Problem:** Weak supervision types (tags, points, scribbles, boxes) are studied in isolation; whether combinations interact synergistically (each resolving the other's ambiguity) or redundantly determines optimal annotation portfolios, and the interaction matrix is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: specific pairs are strongly super-additive (tags resolve point-supervision's class ambiguity; points resolve tags' localization ambiguity) with measurable interaction terms exceeding 20% of individual contributions, while other pairs are redundant (boxes+scribbles) - a supervision-portfolio theory with a measurable payoff matrix that annotation planners can use directly.
- **Why important:** Budget-constrained projects mix supervision types by intuition; a measured synergy matrix upgrades this to portfolio optimization.
- **Why possibly novel:** Systematic interaction-term measurement across weak-supervision pairs is UNVERIFIED - needs lit search.
- **Minimal experiment:** Factorial supervision-mix training grid at matched budgets on COCO-derived weak labels, fit interaction terms per pair.
- **Main risk:** Interactions may depend on class geometry; report per class family.
- **Mutated from:** W2-A-0202

### W2-A-0259 - Pseudo-label entropy drift is the collapse early-warning: self-training failure is forecastable several epochs before performance falls.

- **Problem:** Iterated self-training sometimes collapses (confirmation bias spiral), detected only after damage via labeled validation. A label-free early-warning signal from pseudo-label statistics would make self-training safely automatable.
- **Core hypothesis (falsifiable):** HYPOTHESIS: collapse events are preceded by a characteristic signature in pseudo-label statistics - falling entropy with rising spatial autocorrelation of confident regions (the model agreeing with itself in growing homogeneous patches) - detectable at least several epochs before labeled-metric decline, with low false-alarm rates on healthy runs; collapse has label-free precursors, making it preventable rather than diagnosable.
- **Why important:** Turns a supervision-hungry safety check into a free one, unblocking self-training on domains with no validation labels at all (the setting where it matters most).
- **Why possibly novel:** Precursor-signature analysis for self-training collapse is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run many self-training trajectories with varied configs (some induced to collapse), log statistics, train collapse-precursor detector, evaluate lead time and false alarms.
- **Main risk:** Collapse may be multi-modal (different signatures per cause); collect a taxonomy of collapse types.

### W2-A-0260 - Rich-get-richer amplification in semi-supervised segmentation: fit the exponent by which pseudo-labeling amplifies class imbalance per iteration.

- **Problem:** Pseudo-labels over-represent head classes (confident) and starve tail classes, compounding across iterations - the amplification dynamics are known qualitatively but never fitted quantitatively, so nobody can predict end-state imbalance from initial conditions.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-iteration class-frequency evolution under standard self-training follows a measurable multiplicative dynamic (amplification exponent per class predicted by initial confidence gaps), the fitted dynamic accurately forecasts class death after N iterations from iteration-1 statistics, and forecast-guided per-class threshold correction prevents predicted deaths at minimal head-class cost.
- **Why important:** Prediction beats postmortem: teams could know which classes their pipeline will kill before spending the compute.
- **Why possibly novel:** Fitted amplification dynamics with forecast validation are UNVERIFIED - needs lit search (the qualitative bias is KNOWN).
- **Minimal experiment:** Instrument self-training on LVIS-style imbalanced data across iterations, fit per-class dynamics, validate forecasts on held-out runs.
- **Main risk:** Dynamics may be architecture/threshold-policy specific; fit across the common policy families.
- **Mutated from:** W2-A-0181

### W2-A-0261 - Temporal correspondence is the missing hard-positive: video-mined positives beat augmentation positives for dense contrastive pretraining at matched compute.

- **Problem:** Dense contrastive SSL uses augmentation views as positives - geometrically trivial matches that may teach mostly low-level invariance. Video offers positives across real deformation, lighting, and viewpoint changes; the head-to-head value at matched compute is unresolved.
- **Core hypothesis (falsifiable):** HYPOTHESIS: replacing augmentation positives with tracked temporal correspondences (same surface point across seconds of video) improves downstream segmentation transfer specifically on deformation- and viewpoint-heavy classes by a measurable margin at matched pretraining compute, while degrading nothing - the positive-pair distribution, not the objective, is dense SSL's binding constraint.
- **Why important:** Identifies WHERE dense SSL's remaining headroom lives (pair quality, not loss design), redirecting a crowded methods literature toward data construction. KNOWN: temporal SSL works exist; the controlled matched-compute pair-source comparison is the missing piece. UNVERIFIED - needs lit search.
- **Why possibly novel:** Pair-source-isolated comparison at matched compute.
- **Minimal experiment:** Pretrain matched models with augmentation vs correspondence positives from the same video corpus, transfer to 4 segmentation benchmarks, stratify gains by class deformability.
- **Main risk:** Tracking errors poison positives; gate by correspondence confidence and report sensitivity.

### W2-A-0262 - The language granularity ceiling: measure the boundary precision that text supervision can possibly deliver, and how far CLIP-style dense models sit from it.

- **Problem:** Text-supervised dense models learn from captions that describe objects but never boundaries ('a dog on grass' says nothing about fur-edge pixels). The information-theoretic boundary ceiling of language supervision - and whether current models saturate it - is uncharacterized.
- **Core hypothesis (falsifiable):** HYPOTHESIS: boundary localization precision extractable from caption-supervised models has a hard ceiling well above photometric-edge precision (language never disambiguates within edge-bands), current open-vocabulary segmenters already sit near this ceiling (their boundary errors are irreducible by more text data), and all boundary precision beyond it must come from non-linguistic signals - quantifying an inherent division of labor between supervision modalities.
- **Why important:** Prevents the ecosystem from expecting text scale-up to fix boundaries, and formalizes which supervision each output property requires.
- **Why possibly novel:** Boundary-information ceiling analysis for language supervision is UNVERIFIED - needs lit search.
- **Minimal experiment:** Compare boundary-metric scaling of text-supervised models across text-data scale ladders (available checkpoints), test for saturation against photometric-refinement upper bounds.
- **Main risk:** Ceiling estimation from finite checkpoints is extrapolation; state confidence intervals honestly.

### W2-A-0263 - EXIF is a weak supervisor: focal length, GPS, and timestamps carry measurable segmentation-relevant priors that models never see.

- **Problem:** Every photo carries metadata correlating with scene scale (focal length + distance), content priors (GPS: beach vs city), and lighting (time) - free conditioning information that dense pipelines strip away at ingestion. Whether it buys measurable accuracy is untested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: conditioning segmentation on cheap metadata embeddings improves per-class accuracy measurably (>1 point mIoU) concentrated in scale-ambiguous and region-typical classes, at zero annotation and negligible compute cost - and the gain SURVIVES metadata noise (wrong GPS) because conditioning is learned soft, quantifying a free-lunch the field discards by habit.
- **Why important:** If a free input channel yields standing gains, every production pipeline is leaving accuracy on the table; also probes how much context priors contribute versus pixels.
- **Why possibly novel:** Systematic metadata-conditioning accounting for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train matched models with/without metadata conditioning on datasets retaining EXIF (Mapillary-like), itemize per-class gains and noise robustness.
- **Main risk:** Metadata correlates with dataset collection artifacts; test cross-dataset to ensure priors are real, not leakage.

### W2-A-0264 - SAM-generated panoptic pseudo-labels have a characteristic error anatomy: itemize it before the ecosystem trains a generation of models on it.

- **Problem:** Pipelines increasingly auto-label with SAM masks + classifier-assigned classes. The systematic error structure of this label source (granularity mismatches, boundary style, class-boundary misalignment) - and its downstream inheritance - is undocumented while adoption accelerates.
- **Core hypothesis (falsifiable):** HYPOTHESIS: SAM-pipeline pseudo-labels exhibit a stable error anatomy (over-segmentation of textured objects, under-segmentation of adjacent same-class instances, systematic part-whole granularity flips per class) quantifiably different from human-label noise, and models trained on them inherit the anatomy at high fidelity - making 'SAM-labeled' datasets scientifically distinct references whose results cannot be compared naively against human-labeled baselines.
- **Why important:** Ecosystem-scale quality control: the field is about to run many comparisons confounded by label provenance without a characterization of the confound.
- **Why possibly novel:** Error-anatomy characterization of SAM-pipeline labels is UNVERIFIED - needs lit search.
- **Minimal experiment:** Generate SAM pseudo-labels on human-labeled benchmarks, itemize disagreement taxonomy, train on each, compare inherited error profiles.
- **Main risk:** Anatomy depends on the assembly pipeline variant; characterize the 2-3 dominant public recipes.
- **Mutated from:** W2-A-0206

### W2-A-0265 - Cross-scene object co-occurrence mining: the same physical object photographed in different scenes is a free supervision pair nobody harvests.

- **Problem:** Web archives contain the same objects (landmarks, products, individual animals) across many scenes and conditions - instance-level correspondence at scale without labels. Its value as dense supervision (this exact thing, varied context) is unassessed.
- **Core hypothesis (falsifiable):** HYPOTHESIS: instance-matched cross-scene pairs (minable via retrieval) provide supervision that specifically improves segmentation invariance to context and lighting (the axes those pairs vary) beyond what within-scene or augmentation pairs teach, measurable as targeted transfer gains on context-shifted evaluations - a distinct, harvestable supervision signal between category-level and augmentation-level.
- **Why important:** Identifies an untapped intermediate supervision granularity (instance-across-context) with a concrete mining path from existing archives.
- **Why possibly novel:** Instance-across-context supervision harvesting for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Mine product/landmark instance pairs via retrieval, add correspondence objectives to SSL pretraining, evaluate context-shift transfer against matched controls.
- **Main risk:** Retrieval false matches inject noise; precision-gate the mining and measure the noise sensitivity curve.
- **Mutated from:** W2-A-0221

### W2-A-0266 - Self-training drifts toward the blob prior: iterated pseudo-labeling smooths mask shapes measurably generation by generation.

- **Problem:** Each self-training generation re-learns from its own smoothed outputs; shape detail (concavities, thin parts) may erode cumulatively - a mask-space analogue of repeated compression, unmeasured across generations.
- **Core hypothesis (falsifiable):** HYPOTHESIS: shape-complexity statistics of pseudo-labels (boundary tortuosity, concavity counts, thin-part frequency) decline monotonically across self-training generations at a measurable rate, the decline transfers to real-image predictions (the model becomes blob-biased everywhere), and shape-diverse anchor supervision (retaining a small human-labeled shape-rich subset each generation) arrests the drift - iterated self-training has a quantifiable shape half-life.
- **Why important:** Multi-generation self-training underlies auto-labeling factories; shape erosion would be a compounding quality tax invisible to IoU until late.
- **Why possibly novel:** Generational shape-statistics tracking is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run 5 self-training generations, track shape statistics of labels and predictions, test anchor-subset arrest of the drift.
- **Main risk:** Confounded with genuine error correction (some smoothing removes noise); separate via shape-known synthetic insets.
- **Mutated from:** W2-A-0174

### W2-A-0267 - Cross-class shape transfer: can point-supervised rare classes borrow shape models from shape-similar head classes, and can we predict which donor helps?

- **Problem:** Point supervision localizes but cannot teach shape. Head classes have rich learned shape models that might transfer to shape-similar tail classes (scissors borrowing from pliers) - but shape-donorship has no predictive theory.
- **Core hypothesis (falsifiable):** HYPOTHESIS: point-supervised tail-class mask quality improves substantially when the model has a shape-similar head class (measurable donor effect), donor benefit is predicted by shape-descriptor distance between classes (not semantic distance), and adversarial donor pairs (semantically close, shape-far: snake vs lizard) actively hurt - shape, not semantics, is the transferable currency for mask completion under weak supervision.
- **Why important:** Provides a principled rule for which tail classes weak supervision suffices for (shape-donor available) versus which need full masks - direct annotation-planning value.
- **Why possibly novel:** Predictive shape-donorship analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Construct donor-controlled training sets (include/exclude shape-similar head classes), train point-supervised models, regress tail mask quality on donor shape distance.
- **Main risk:** Disentangling shape from co-occurrence and context similarity requires careful class-set design.
- **Mutated from:** W2-A-0209

### W2-A-0268 - Do semi-supervised methods still matter under DINOv2-grade features? Systematic re-evaluation of SSL-for-segmentation on top of modern foundations.

- **Problem:** The semi-supervised segmentation literature largely predates strong foundation features; its methods were designed for label-starved randomly-initialized or ImageNet-pretrained regimes. Whether their gains survive when the backbone already encodes most structure is the field's uncomfortable open question.
- **Core hypothesis (falsifiable):** HYPOTHESIS: on DINOv2-class frozen features, the gains of leading semi-supervised methods shrink to a small fraction of their reported values (foundation features already deliver what pseudo-labeling used to add), with the surviving gains concentrated in dataset-specific ontology learning - a large part of the sub-field's methodology is obsolete in the foundation regime, and honest re-baselining would reset its research agenda.
- **Why important:** Prevents continued investment in methods whose problem has been dissolved (not solved) by pretraining progress; recalibrates what semi-supervision is FOR now.
- **Why possibly novel:** Foundation-regime re-baselining of the semi-supervised segmentation literature is UNVERIFIED - needs lit search.
- **Minimal experiment:** Re-run 6 leading semi-supervised methods with modern frozen/fine-tuned foundations across label budgets, compare gain profiles against original settings.
- **Main risk:** Provocative framing invites pushback on implementation fairness; pre-register protocols and use authors' code where available.

### W2-A-0269 - Boundary noise and region noise are different diseases: dense-label noise robustness has two regimes with opposite remedies.

- **Problem:** Label-noise-robust learning treats mask noise as one phenomenon, but boundary jitter (correct region, wrong edges) and region noise (wrong areas included/excluded) plausibly corrupt learning through different mechanisms needing different treatments - the two-regime structure is unverified.
- **Core hypothesis (falsifiable):** HYPOTHESIS: controlled noise-type injection shows boundary noise degrades boundary metrics but leaves region learning nearly intact (models average jitter away) while region noise poisons both (models learn the wrong extent), robustness techniques sort cleanly by which regime they address, and real datasets' noise composition (measurable) predicts which technique family will help - a diagnostic-then-treat framework replacing one-size-fits-all noise robustness.
- **Why important:** Noise-robust training choices currently ignore noise composition; matching treatment to diagnosis is basic but absent.
- **Why possibly novel:** Noise-type-regime decomposition for dense labels is UNVERIFIED - needs lit search.
- **Minimal experiment:** Inject calibrated boundary vs region noise on clean datasets, map degradation profiles, classify robustness methods by regime, validate on real noisy datasets.
- **Main risk:** Real noise mixes both types; the composition estimator is the load-bearing deliverable.
- **Mutated from:** W2-A-0220

### W2-A-0270 - The granularity control problem: unsupervised instance discovery finds parts or groups unpredictably - measure what determines the discovered granularity.

- **Problem:** Clustering-based unsupervised instance discovery returns segments at uncontrolled granularity (wheels vs cars vs traffic). What data and algorithmic factors determine discovered granularity - and whether it can be dialed - is the unsolved usability question of the area.
- **Core hypothesis (falsifiable):** HYPOTHESIS: discovered granularity is predictable from measurable factors (feature layer depth, clustering scale parameter, and crucially the training data's own object-scale statistics), granularity is approximately a monotonic function of a single identifiable direction in hyperparameter space (a 'granularity dial' exists), and dial positions transfer across datasets after object-scale normalization - unsupervised discovery is controllable once its determinants are mapped.
- **Why important:** Uncontrolled granularity blocks all practical use of unsupervised discovery; a validated dial converts it from curiosity to tool.
- **Why possibly novel:** Granularity-determinant mapping is UNVERIFIED - needs lit search.
- **Minimal experiment:** Sweep the candidate factors on multi-granularity-annotated data (PartImageNet-style), measure discovered-granularity response surfaces, test dial transfer.
- **Main risk:** Granularity may be irreducibly multi-modal per image; report distributional (not scalar) dial behavior.

### W2-A-0271 - One labeled frame per video: quantify the propagation-quality law as a function of motion complexity to price video weak supervision.

- **Problem:** The cheapest video supervision is one labeled frame per clip, propagated by tracking. Its effective label quality varies wildly with clip content, and without a predictive law relating motion complexity to propagated-label quality, annotation planners cannot price this supervision.
- **Core hypothesis (falsifiable):** HYPOTHESIS: propagated-label quality decays with measurable clip statistics (flow magnitude variance, occlusion event rate, deformation energy) following a stable fitted law, the law transfers across trackers (it reflects content difficulty, not tracker identity), and law-guided clip selection (label the frames whose propagation will be reliable) yields dataset-quality improvements at fixed budget over uniform or random frame choice.
- **Why important:** Converts video annotation planning from guesswork to forecast, with immediate value for every VOS/video-dataset builder.
- **Why possibly novel:** Fitted propagation-quality laws with planning application are UNVERIFIED - needs lit search.
- **Minimal experiment:** Propagate labels on fully-annotated video benchmarks, fit quality-vs-statistics laws across trackers, validate selection policy at matched budgets.
- **Main risk:** Law stability across domains (sports vs surgery) needs testing; fit per domain and compare.
- **Mutated from:** W2-A-0045

### W2-A-0272 - Layered source files (PSD/SVG) are the largest untapped mask corpus: design assets contain millions of human-made segmentations nobody trains on.

- **Problem:** Designers produce layered compositions (product cutouts, photo composites, vector scenes) whose layers ARE segmentation masks with human-grade boundaries - a massive, growing, permissively-licensed-in-part corpus outside the field's data pipeline entirely.
- **Core hypothesis (falsifiable):** HYPOTHESIS: masks harvested from layered design files (deduplicated, quality-filtered) constitute a boundary-quality distribution SUPERIOR to crowdsourced polygons (designers cut edges pixel-perfectly for a living), pretraining on them transfers measurably to natural-image segmentation (especially boundary metrics), and their bias profile (product-centric, studio-lit) is quantifiable and complementary to web-photo datasets - a new data source with different economics than annotation.
- **Why important:** Data sources, not methods, have driven recent leaps; a large orthogonal mask corpus with professional boundary quality could matter more than another architecture.
- **Why possibly novel:** Design-file mask harvesting at scale is UNVERIFIED - needs lit search.
- **Minimal experiment:** Harvest masks from openly-licensed layered assets, quantify boundary-quality distribution vs COCO, pretrain and measure transfer on boundary-heavy benchmarks.
- **Main risk:** Licensing and composition bias; both are characterizable and the bias may complement (not duplicate) existing sources.

### W2-A-0273 - What can sound NOT teach about segmentation? Build the taxonomy of audio-supervisable versus audio-invisible visual structure.

- **Problem:** Audio-visual segmentation learns to segment sounding objects (KNOWN field: AVS benchmarks exist). But the systematic limits - which object properties and classes audio supervision can never reach (silent, ambient-sound, many-to-one sources) - are uncharted, leaving the modality's true supervision value unquantified.
- **Core hypothesis (falsifiable):** HYPOTHESIS: audio supervision produces segmentation competence sharply stratified by a definable acoustic taxonomy (impulsive-sound rigid objects learn well; continuous-drone sources learn poorly; silent classes learn only via co-occurrence hitchhiking, measurable as indirect transfer), and the hitchhiking effect (silent objects learned through sounding companions) is a quantifiable, previously unmeasured supervision pathway.
- **Why important:** Prevents over-claiming of audio-visual learning while identifying its genuine (and surprising: hitchhiking) contributions - honest boundaries for a fashionable modality.
- **Why possibly novel:** Supervision-limit taxonomy with hitchhiking quantification is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train audio-visually on video corpora, evaluate per-class against the acoustic taxonomy, isolate hitchhiking via co-occurrence-controlled test sets.
- **Main risk:** Taxonomy boundaries are fuzzy (most objects CAN sound); define by empirical sound-emission rates in the corpus.

### W2-A-0274 - Physical support constraints prune impossible masks: 'objects rest on surfaces' as a validity filter measurably improves weak-supervision pipelines.

- **Problem:** Weakly-supervised masks routinely violate physics (floating fragments, gravity-defying extents), yet physical plausibility (support relations, contact consistency) is never used as a filter - a source of constraint that requires no labels at all.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a support-consistency checker (estimating ground plane and contact relations, flagging unsupported mask fragments) rejects pseudo-label errors with high precision (most flagged masks are indeed wrong), integrating it into self-training measurably improves final models, and the improvement concentrates on exactly the error types (floating fragments, shadow inclusion) that confidence-based filtering cannot catch - physics is an orthogonal, free filter for label factories.
- **Why important:** Pseudo-label filtering currently relies solely on model confidence (circular); an independent physical validity channel breaks the circularity cheaply.
- **Why possibly novel:** Support-relation filtering for pseudo-label pipelines is UNVERIFIED - needs lit search.
- **Minimal experiment:** Implement plausibility checker on self-training pipelines for driving/indoor data, measure flag precision and end-model gains vs confidence-only filtering.
- **Main risk:** Physics checks fail on genuinely airborne/occluded-support objects; measure the false-flag taxonomy.

### W2-A-0275 - Annotation-free model ranking: can cross-model consensus plus perturbation stability rank segmentation models without any ground truth?

- **Problem:** Choosing among models for a new unlabeled domain currently requires labeling an evaluation set - often the deployment bottleneck. Whether label-free signals (inter-model agreement patterns, perturbation stability, physical plausibility) can reproduce GT-based rankings is a practical meta-question with scattered, task-inconsistent prior evidence.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a composite label-free ranking signal reproduces GT rankings with high fidelity (rank correlation >0.8) when candidate models are architecturally diverse, but FAILS predictably when candidates share training lineage (shared blind spots defeat consensus) - and the failure condition is detectable from the agreement structure itself, yielding a self-aware evaluation-free ranking protocol with known validity conditions.
- **Why important:** Deployment teams face this exact decision weekly; a validated protocol WITH its validity detector would be adopted immediately.
- **Why possibly novel:** Validity-aware label-free ranking for dense prediction is UNVERIFIED - needs lit search.
- **Minimal experiment:** Across 10 datasets and 12 models of varied lineage, compare label-free composite rankings against GT rankings, characterize failure conditions by lineage overlap.
- **Main risk:** Lineage overlap is becoming universal (everything descends from few foundations) - which itself would be a headline finding about ecosystem monoculture.

## C12-foundation-dense-science

### W2-A-0276 - Dense-prediction scaling laws diverge from classification: boundary quality scales with a smaller exponent than region accuracy - fit both.

- **Problem:** Scaling laws exist for classification/LLMs (KNOWN), but dense prediction may scale differently per output property: region-level semantics might follow data/model power laws while boundary precision saturates early (limited by resolution and label noise, not knowledge). No one has fitted property-resolved scaling curves.
- **Core hypothesis (falsifiable):** HYPOTHESIS: fitting scaling curves separately for region metrics and boundary metrics across model/data ladders reveals significantly different exponents (boundary exponent near zero beyond moderate scale - scale does not buy sharpness), implying the field's scaling investments improve WHAT models segment but not HOW WELL they trace it - a structural argument for redirecting boundary research away from scale.
- **Why important:** Scaling strategy is the biggest resource decision in the field; property-resolved laws would show which problems scale can and cannot solve.
- **Why possibly novel:** Property-decomposed scaling analysis for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train/collect model ladders (existing checkpoint series + controlled small-scale runs), fit region-vs-boundary scaling exponents with confidence intervals.
- **Main risk:** Boundary metrics hit label-noise floors that masquerade as saturation; use metrology-grade evaluation subsets (see physical-GT benchmark idea).
- **Mutated from:** W2-A-0175

### W2-A-0277 - The probing atlas: layer-by-layer, which foundation models linearly encode boundaries, parts, materials, and occlusion - a standardized dense-knowledge inventory.

- **Problem:** Claims like 'DINOv2 knows objects' rest on scattered probes with incompatible protocols. The field lacks a standardized, property-resolved inventory of what dense information each foundation model encodes linearly, at which layer, at what spatial precision.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a standardized probing battery (boundaries, part hierarchies, material vs shape, occlusion ordering, metric size) across major foundations will reveal strongly model-family-specific knowledge profiles (contrastive models encode materials better; MAE-style encode layout better; SAM encodes boundary-ownership uniquely) that PREDICT downstream fine-tuning outcomes per task better than aggregate benchmark scores - knowledge profiles, not leaderboard positions, should drive backbone selection.
- **Why important:** Backbone choice is every project's first decision, currently made by leaderboard folklore; a validated knowledge inventory would replace it with measurement.
- **Why possibly novel:** Standardized cross-foundation dense-probing with downstream-predictivity validation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Build the probe battery on 5 properties x 6 foundations x all layers, correlate profile-task match scores with realized fine-tuning outcomes on 8 tasks.
- **Main risk:** Linear probes underestimate nonlinearly-encoded knowledge; include lightweight nonlinear probes as sensitivity analysis.

### W2-A-0278 - Sub-patch information is not lost - it hides in neighboring tokens: measure recoverable sub-tokenization detail across ViT foundations.

- **Problem:** Patch tokenization (14-16px) supposedly destroys sub-patch spatial detail, capping dense tasks. But convolution-free ViTs may distribute sub-patch information across neighboring tokens' interactions - whether fine detail is destroyed or merely delocalized is a measurable representational question.
- **Core hypothesis (falsifiable):** HYPOTHESIS: sub-patch edge positions are decodable from local token NEIGHBORHOODS (not single tokens) at precision well below patch size (2-4px) in mid layers, decoding precision varies strongly across pretraining objectives, and the delocalized detail is exactly what boundary-refinement heads fail to exploit - foundation features contain more sharpness than any current decoder extracts.
- **Why important:** If detail survives delocalized, boundary quality is a readout problem (fixable cheaply), not a representation problem (needing new pretraining) - a fork in the road for boundary research.
- **Why possibly novel:** Neighborhood-decoding analysis of sub-patch information is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train sub-pixel edge-position probes on token neighborhoods across layers/models using synthetic exact-edge stimuli, map recoverable precision.
- **Main risk:** Synthetic edges may over-estimate recoverability on natural texture; validate on the physical-GT benchmark stimuli.
- **Mutated from:** W2-A-0011

### W2-A-0279 - Attention-sink artifacts corrupt dense features in predictable spatial patterns: map the damage and its downstream cost per task.

- **Problem:** KNOWN: ViTs develop high-norm artifact tokens (Darcet et al., 'Vision Transformers Need Registers'). What remains unmeasured is the spatial structure of artifact damage in dense downstream tasks - where in the image artifacts land, which classes suffer, and how much performance the artifacts actually cost end-to-end.
- **Core hypothesis (falsifiable):** HYPOTHESIS: artifact tokens localize preferentially in low-information regions (sky, walls) but their attention distortion damages predictions in a measurable halo AROUND those regions (displaced errors), the per-task cost is significant for segmentation but negligible for classification (explaining why the problem went unnoticed), and artifact-location prediction enables test-time feature cleaning worth a consistent fraction of the gap to register-equipped models.
- **Why important:** Quantifies a known pathology's real dense-task cost and offers retrofit mitigation for the enormous installed base of artifact-bearing checkpoints.
- **Why possibly novel:** Spatial damage-mapping and retrofit-cleaning accounting is UNVERIFIED - needs lit search (the artifact phenomenon itself is KNOWN).
- **Minimal experiment:** Localize artifacts across images, correlate with spatial error maps on segmentation, implement cleaning, measure recovered performance vs register-model upper bound.
- **Main risk:** Artifact behavior differs across model families; scope claims per family.

### W2-A-0280 - Generative vs discriminative pretraining for boundaries: diffusion features encode edges sharper than contrastive features - a controlled spectral comparison.

- **Problem:** Diffusion models must synthesize exact boundaries (generation demands sharpness), while contrastive objectives reward invariance (blur tolerance). Whether generative pretraining therefore yields sharper dense features - controlled for data and scale - is a fundamental objective-level question tangled in uncontrolled comparisons.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at matched data and compute, diffusion-pretrained features support higher boundary-precision readout (measurable via edge-position probing and boundary metrics) while contrastive features support better semantic discrimination - a principled objective-property tradeoff, implying optimal dense systems should read boundaries and semantics from DIFFERENT pretraining lineages.
- **Why important:** Resolves a foundational which-objective-for-what question with design consequences for every dense pipeline.
- **Why possibly novel:** Matched-budget objective comparison focused on boundary spectra is UNVERIFIED - needs lit search (uncontrolled diffusion-feature studies are KNOWN to exist).
- **Minimal experiment:** Pretrain matched mid-scale models (diffusion, contrastive, MAE) on identical data, run boundary-precision and semantic probes, compare property profiles.
- **Main risk:** Matched-budget pretraining is expensive at meaningful scale; use the largest affordable scale with scaling-trend checks.
- **Mutated from:** W2-A-0277

### W2-A-0281 - What makes a good visual in-context example? Retrieval laws for one-shot segmentation prompting with image-mask pairs.

- **Problem:** Visual in-context segmentation (prompt with example image-mask pairs, e.g. SegGPT-style - KNOWN to exist) is acutely sensitive to support-example choice, but support selection is folk art; the quantitative laws (what similarity dimensions matter, how gains scale with support-set size and diversity) are unmapped.
- **Core hypothesis (falsifiable):** HYPOTHESIS: in-context segmentation quality is predicted by a learnable composite of support-query similarities where POSE and SCALE similarity dominate semantic similarity (opposite to text-LLM intuitions), gains saturate at very few supports (2-4) unless supports are diversity-selected, and a retrieval policy trained on these laws beats random/semantic retrieval by a large margin - in-context vision has its own retrieval science distinct from NLP's.
- **Why important:** In-context dense models are the most annotation-efficient adaptation path; their usability hinges entirely on support retrieval, currently unprincipled.
- **Why possibly novel:** Support-retrieval law-fitting for dense in-context learning is UNVERIFIED - needs lit search.
- **Minimal experiment:** Sweep support choice along controlled similarity axes on in-context segmenters, fit gain predictors, validate learned retrieval on held-out tasks.
- **Main risk:** Laws may be model-specific; test across 2-3 in-context architectures.

### W2-A-0282 - When does nearest-neighbor label transfer beat fine-tuning? Map the regime boundary for non-parametric segmentation over foundation features.

- **Problem:** With strong frozen features, segmenting by retrieving similar labeled patches and transferring their labels (non-parametric) competes with parametric fine-tuning. The regime map - along labeled-set size, domain shift, and class granularity - of which paradigm wins where has not been drawn.
- **Core hypothesis (falsifiable):** HYPOTHESIS: nearest-neighbor transfer dominates fine-tuning below a measurable labeled-data threshold (a few hundred masks) and under moderate shift (retrieval adapts instance-wise; parameters overfit), while fine-tuning wins on fine-grained class boundaries requiring feature reshaping - and the crossover locations are predictable from feature-space class separability statistics, giving practitioners a measurement-driven paradigm selector.
- **Why important:** The low-label regime is where most real projects start; knowing when to skip training entirely (retrieval only) saves widespread wasted effort.
- **Why possibly novel:** Paradigm regime-mapping with predictive crossover is UNVERIFIED - needs lit search.
- **Minimal experiment:** Grid over labeled-set size x shift x granularity comparing kNN-transfer vs fine-tuning on frozen DINOv2/SAM features, fit crossover predictors.
- **Main risk:** kNN implementation quality (feature aggregation, spatial priors) strongly affects the frontier; use well-tuned versions of both paradigms.

### W2-A-0283 - Resolution extrapolation failures are radially structured: positional-encoding interpolation breaks dense prediction from the image border inward.

- **Problem:** Models trained at low resolution are deployed at high resolution via positional-embedding interpolation; failures are treated as uniform degradation, but interpolation error geometry (extrapolation at borders, compression at center) predicts spatially structured damage nobody has mapped.
- **Core hypothesis (falsifiable):** HYPOTHESIS: under resolution extrapolation, dense-prediction error increases with a characteristic radial profile (worst at borders and corners, tracking positional-embedding interpolation error), the profile shape is predictable from the embedding scheme (learned absolute vs RoPE-style vs conv-derived), and border-cropped evaluation recovers most of the reported extrapolation gap - 'resolution generalization failure' is substantially a positional-geometry artifact with scheme-specific signatures.
- **Why important:** Correct attribution changes the fix (positional scheme surgery, not retraining) and warns that border-heavy applications (panorama, document edges) suffer most.
- **Why possibly novel:** Radial error-profiling of resolution extrapolation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Evaluate models across resolution ladders, map spatial error profiles per positional scheme, test border-crop recovery predictions.
- **Main risk:** Content statistics also vary radially in photos (center bias); control with content-shuffled synthetic layouts.
- **Mutated from:** W2-A-0238

### W2-A-0284 - Do vision foundations share an object space? Measure cross-model representational alignment specifically on object-level axes, not global features.

- **Problem:** The platonic-representation debate (do independently trained models converge?) has been argued with global similarity metrics (KNOWN: representational-alignment literature exists); whether alignment holds specifically for OBJECT-level structure (boundaries, part decompositions, instance separations) - the part dense prediction cares about - is finer-grained and unresolved.
- **Core hypothesis (falsifiable):** HYPOTHESIS: object-level alignment between foundations (measured by transferability of object-axis linear maps between SAM/DINOv2/CLIP feature spaces) is substantially higher than global feature alignment, alignment grows with each model's downstream dense performance (convergence tracks competence), and residual misalignment localizes to specific properties (part granularity, boundary ownership) that differ by pretraining objective - the ecosystem is converging on WHAT objects are but not on their decomposition.
- **Why important:** Convergence structure determines whether ensembling/stitching pays and what unique value each pretraining lineage retains - portfolio-level strategy for the field.
- **Why possibly novel:** Object-axis-resolved alignment measurement is UNVERIFIED - needs lit search.
- **Minimal experiment:** Fit cross-model linear maps on object-centric probe tasks, quantify transfer per property, correlate alignment with performance across checkpoint ladders.
- **Main risk:** Alignment metrics are subtle (CKA critiques are KNOWN); use multiple alignment measures and behavioral (not just geometric) tests.

### W2-A-0285 - Vocabulary is a confounder in open-vocabulary segmentation: performance depends on distractor-list composition as much as on the model - benchmark the benchmark.

- **Problem:** Open-vocabulary segmentation scores depend on the evaluation vocabulary (which distractor classes compete), yet benchmarks fix arbitrary small vocabularies, making cross-paper numbers incomparable and inflating apparent competence relative to open-world deployment with thousands of candidate labels.
- **Core hypothesis (falsifiable):** HYPOTHESIS: OV segmentation scores decay predictably with vocabulary size and semantic density (distractor proximity), model RANKINGS flip between small-vocabulary and large-vocabulary regimes (some models are precision-optimized, others recall-optimized), and reporting vocabulary-scaling CURVES instead of point scores restores comparability - one protocol fix rescuing an incoherent evaluation ecosystem.
- **Why important:** OV segmentation is the field's deployment-facing product; incomparable evaluation blocks real progress assessment.
- **Why possibly novel:** Vocabulary-scaling evaluation protocol with rank-flip demonstration is UNVERIFIED - needs lit search.
- **Minimal experiment:** Evaluate 6 OV models across controlled vocabulary ladders (size x density), demonstrate rank instability, propose and validate curve-based reporting.
- **Main risk:** Overlaps conceptually with confidence-dilution idea (W2-A-0197) but targets evaluation protocol rather than confidence mechanics; keep both with distinct deliverables.
- **Mutated from:** W2-A-0197

### W2-A-0286 - How small can a decoder be? Localize where dense-task capacity actually lives by scaling decoders down over frozen foundations.

- **Problem:** Dense architectures allocate large decoders by convention, but if frozen foundation features already contain the needed information, decoder capacity might shrink drastically without loss - the capacity-localization question (encoder vs decoder) has never been answered with systematic decoder-scaling curves.
- **Core hypothesis (falsifiable):** HYPOTHESIS: over strong frozen encoders, segmentation performance vs decoder size shows a sharp knee at surprisingly small capacity (<1% of encoder parameters) for region metrics, but boundary metrics keep improving with decoder size (boundary computation genuinely lives in the decoder), and the knee position shifts predictably with encoder quality - a capacity-localization law separating what encoders know from what decoders compute.
- **Why important:** Design efficiency (edge deployment) plus scientific attribution: knowing where each output property is computed directs both compression and improvement efforts.
- **Why possibly novel:** Property-resolved decoder-scaling laws are UNVERIFIED - needs lit search.
- **Minimal experiment:** Decoder-size ladders over 3 frozen foundations x 3 datasets, fit property-resolved capacity curves, locate knees vs encoder quality.
- **Main risk:** Decoder architecture family may matter as much as size; replicate across 2 families.

### W2-A-0287 - How precisely can MLLMs localize without a pixel decoder? Measure the text-coordinate segmentation ceiling of GPT-4V-class models.

- **Problem:** Multimodal LLMs describe and point at image content via text coordinates (boxes, polygon vertices as numbers). Their intrinsic localization precision - the ceiling of language-emitted geometry - determines whether pixel decoders are necessary or just convenient, and it has not been carefully measured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: MLLM text-coordinate boundary precision plateaus around coarse levels (5-10% of object scale) regardless of prompt engineering (a representation bottleneck, not an interface artifact - verifiable by probing whether visual tokens contain finer position information than the text head extracts), implying pixel-space readouts are structurally required for boundary tasks while detection-grade localization is already language-achievable.
- **Why important:** Architectural guidance for the merging of MLLMs and dense vision: what must be grafted on versus what emerges from scale.
- **Why possibly novel:** Ceiling measurement with internal-information comparison (tokens vs text head) is UNVERIFIED - needs lit search.
- **Minimal experiment:** Elicit coordinate outputs from 4 MLLMs across precision-demanding tasks, compare against linear probes on their visual tokens for the same geometry.
- **Main risk:** Closed-model probing is limited; use open MLLMs for the internal-information leg.

### W2-A-0288 - Does a granularity dial exist in prompt space? Search for a continuous direction controlling part-object-group level in promptable segmenters.

- **Problem:** SAM's granularity is controlled crudely (multimask choice); whether the underlying prompt-embedding space contains a continuous, monotonic granularity direction (allowing smooth part-to-whole dialing) is a concrete representational geometry question with direct interface value.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a single direction in SAM's prompt-token space monotonically controls output granularity across categories (found via paired part/whole supervision on a small set, transferring zero-shot to unseen categories), demonstrating granularity is linearly represented - and its transferability failure cases (categories with non-nested part structures) reveal where object decomposition is genuinely non-hierarchical.
- **Why important:** A working dial would fix promptable segmentation's most common practical failure (wrong granularity), and the geometry finding informs how composition is encoded.
- **Why possibly novel:** Prompt-space granularity-direction search is UNVERIFIED - needs lit search.
- **Minimal experiment:** Fit granularity directions on part-annotated categories (PACO/PartImageNet), test zero-shot transfer, characterize monotonicity and failure taxonomy.
- **Main risk:** Granularity may be encoded nonlinearly or per-category; a negative result still maps the encoding structure.
- **Mutated from:** W2-A-0002

### W2-A-0289 - Trace a bad mask to its training data: feasibility of influence-function attribution for promptable segmentation failures.

- **Problem:** When SAM fails on a mask, nobody can say WHICH training data (or absence thereof) is responsible - data attribution methods exist for classification (KNOWN: influence functions, TracIn lineage) but their feasibility, cost, and validity for billion-mask promptable models is untested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: scalable attribution approximations (gradient-sketch retrieval over training shards) identify training-set regions whose removal/addition causally changes specific failure behaviors (validated by targeted fine-tuning on attributed shards fixing the failure at above-random rates), making failure-driven data curation - fix the model by editing data, not weights - a practical loop for segmentation foundations.
- **Why important:** Data curation is the main lever for foundation model quality; closing the failure-to-data loop would industrialize it.
- **Why possibly novel:** Attribution-driven repair loops for dense foundations are UNVERIFIED - needs lit search.
- **Minimal experiment:** On an open SAM-scale-down reproduction, attribute 100 failure cases, run targeted-data interventions, measure repair rates vs random-data controls.
- **Main risk:** Attribution approximations may be too noisy at scale; the scaled-down setting bounds feasibility honestly.

### W2-A-0290 - Shared blind spots across the model zoo: pixels where ALL foundations fail mark data-ecosystem holes, not architecture limits.

- **Problem:** Per-model error analysis cannot distinguish 'this architecture's weakness' from 'nobody's training data covers this'. Cross-model failure correlation - the shared-vs-unique error decomposition across independent lineages - has never been systematically computed for dense prediction.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a large fraction of segmentation errors (>40%) are shared across architecturally-independent models (data-ecosystem holes: web-photo biases, absent domains), shared-error regions are predictable from data-frequency estimates (how rare such pixels are online), and unique errors cluster by architectural family - producing an actionable split: fix shared errors with data expeditions, unique errors with architecture work.
- **Why important:** The field's error-fixing effort is misallocated without this decomposition; shared holes need collection campaigns no single lab's method work can fill.
- **Why possibly novel:** Ecosystem-level error-correlation decomposition is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run 10 diverse models on 5 benchmarks, decompose per-pixel error correlation, correlate shared-error regions with web-frequency proxies.
- **Main risk:** Lineage independence is eroding (shared data everywhere); quantify lineage overlap as a covariate.
- **Mutated from:** W2-A-0275

### W2-A-0291 - Image pretraining plus explicit tracking versus native video pretraining: budget-matched showdown for dense video tasks.

- **Problem:** Video foundation models cost far more to train than image models; whether native temporal pretraining buys anything over strong image features composed with lightweight tracking machinery - at matched total budget - is the central economics question of video representation learning, never cleanly tested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for video segmentation tasks dominated by appearance continuity, image-pretraining + tracking matches or beats native video pretraining at equal budget (temporal structure is cheap to add post hoc), but a specific task subset (occlusion reasoning, motion-defined objects, temporal event boundaries) shows irreducible native-video advantages - defining precisely WHICH temporal capabilities require temporal pretraining and which do not.
- **Why important:** Directly prices the video-pretraining premium and would redirect large compute investments if the composed alternative suffices for most tasks.
- **Why possibly novel:** Budget-matched composed-vs-native comparison with capability decomposition is UNVERIFIED - needs lit search.
- **Minimal experiment:** Match total budgets between (image SSL + tracking head) and video SSL pipelines, evaluate across a task battery stratified by temporal-dependence, itemize where native wins.
- **Main risk:** Budget matching across paradigms has degrees of freedom; pre-register the accounting rules.

### W2-A-0292 - Can a segmentation foundation be trained on zero real images? Push procedural-data pretraining (fractals, formulas, simulations) to its dense-prediction limit.

- **Problem:** Formula/fractal pretraining works surprisingly well for classification (KNOWN: FractalDB line of work exists); whether procedurally-generated data - with its perfect free labels and zero licensing/privacy burden - can carry DENSE pretraining to competitive levels, and what procedural ingredients matter, is largely unmapped.
- **Core hypothesis (falsifiable):** HYPOTHESIS: procedural pretraining reaches a substantial fraction (>70%) of real-data pretraining transfer for segmentation IF the generator includes specific ingredients - occlusion layering, boundary-complexity distributions matched to natural statistics, and material-like texture gradients - and ingredient ablations identify occlusion structure as the single most transfer-critical property, revealing what dense pretraining actually needs from data (compositional structure, not semantics).
- **Why important:** A viable real-image-free pretraining path solves licensing/privacy constraints (medical!) and scientifically isolates which data properties dense learning consumes.
- **Why possibly novel:** Ingredient-ablated procedural pretraining for dense tasks is UNVERIFIED - needs lit search beyond the KNOWN classification-focused work.
- **Minimal experiment:** Build parameterized procedural generator, pretrain matched models across ingredient ablations, measure segmentation transfer against real-data controls.
- **Main risk:** The gap may be irreducible for semantic tasks; even so, the ingredient-importance map is standalone valuable.

### W2-A-0293 - Compression kills boundaries first: quantization and distillation degrade dense outputs in a property-ordered sequence worth mapping.

- **Problem:** Model compression is validated on aggregate metrics, but dense-output properties (region semantics, boundary precision, small-object recall, calibration) may degrade at very different rates - the degradation ORDER determines which applications can use compressed models, and it is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: across compression methods (quantization, pruning, distillation), dense properties degrade in a consistent order - boundary precision first, small-object recall second, region semantics last (mirroring their dependence on high-frequency feature content) - and the ordering enables property-targeted compression (protecting boundary-critical channels identified by sensitivity analysis) that shifts the frontier for boundary-dependent applications.
- **Why important:** Edge deployment of segmentation is exploding; property-ordered degradation maps tell each application what compression it can afford.
- **Why possibly novel:** Property-resolved compression analysis for dense prediction is UNVERIFIED - needs lit search.
- **Minimal experiment:** Compress 3 segmentation models along method ladders, track property-resolved metrics, test the protection scheme on boundary-critical channels.
- **Main risk:** Ordering may vary by architecture; establish across families before claiming universality.
- **Mutated from:** W2-A-0276

### W2-A-0294 - Decode what learned dense prompts encode: continuous prompt vectors trained for segmentation tasks are interpretable dataset fingerprints.

- **Problem:** Visual prompt tuning learns small parameter sets that adapt frozen models to datasets; these vectors must encode the dataset's distinctive properties (class priors, boundary conventions, granularity), but nobody has tried to READ them - an interpretability opportunity with practical payoffs (dataset similarity, transfer prediction).
- **Core hypothesis (falsifiable):** HYPOTHESIS: learned dense-task prompts are decodable - prompt-space distances between datasets predict cross-dataset transfer performance (prompt geometry is a transfer map), prompt arithmetic works (combining prompts of dataset A's classes with dataset B's boundary convention), and specific prompt components isolate annotation-convention information - making prompts both a scientific instrument for dataset comparison and an engineering tool for convention translation.
- **Why important:** A working dataset-fingerprint algebra would answer 'how similar are these datasets' and 'will transfer work' from cheap artifacts instead of expensive experiments.
- **Why possibly novel:** Prompt-space decoding and arithmetic for dense tasks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train prompts across 12 datasets on one frozen foundation, test distance-transfer correlation and convention-swap arithmetic on held-out pairs.
- **Main risk:** Prompt solutions are non-unique (different seeds, same behavior); test geometry stability across seeds first.

### W2-A-0295 - Is promptable segmentation emergent or smooth? Train a mini-SAM scaling series and settle whether the capability has a threshold.

- **Problem:** Emergence debates (capabilities appearing suddenly at scale) are unresolved for dense prediction: does promptability - responding correctly to spatial prompts - develop smoothly with scale or exhibit threshold behavior? The SAM training recipe at reduced scales provides a clean testbed nobody has exploited.
- **Core hypothesis (falsifiable):** HYPOTHESIS: prompt-following ability measured with fine-grained metrics develops SMOOTHLY across a mini-SAM scaling series (no emergence - apparent thresholds in prior anecdotes are metric artifacts, consistent with the KNOWN emergence-as-metric-artifact critique in LLMs), but specific sub-capabilities (negative-prompt understanding, multi-prompt integration) show genuinely delayed development - a capability-resolved developmental timeline for promptable vision.
- **Why important:** Whether capabilities emerge or accrue determines training-investment risk (can you extrapolate from small pilots?) - a first-order question for anyone training dense foundations.
- **Why possibly novel:** Scaling-series developmental analysis of promptability is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train 6 SAM-recipe models from tiny to small scale on SA-1B subsets, evaluate capability-resolved prompt-following curves with continuous metrics.
- **Main risk:** Mini-scale conclusions may not extrapolate to frontier scale; frame as developmental science with stated bounds.

### W2-A-0296 - Feature quality is spatially anisotropic: foundation features degrade toward image borders, and panoramic/tiled applications inherit the damage.

- **Problem:** Foundation features are treated as spatially homogeneous, but training photos have strong center bias (subjects centered, borders contain periphery), plausibly training center-privileged features - a spatial quality gradient that tiled inference and panorama processing would repeatedly sample at its worst.
- **Core hypothesis (falsifiable):** HYPOTHESIS: probing tasks show systematic center-to-border feature quality gradients across foundations (matched-content probes decoding worse near borders), the gradient magnitude tracks each training corpus's measured center bias (data-borne, not architectural), and tiling strategies that avoid placing content at tile borders recover measurable accuracy in tiled high-resolution inference - a hidden spatial prior with direct engineering consequences.
- **Why important:** Tiled inference is universal for high-res imagery (satellite, pathology); an unrecognized border penalty means widespread silent quality loss with a cheap layout fix.
- **Why possibly novel:** Spatial feature-quality gradient measurement is UNVERIFIED - needs lit search.
- **Minimal experiment:** Probe matched content at controlled positions across foundations, correlate gradients with corpus center-bias statistics, benchmark border-aware tiling.
- **Main risk:** Positional embeddings entangle with content statistics; use content-controlled synthetic placements.
- **Mutated from:** W2-A-0283

### W2-A-0297 - Object tokens or distributed objectness? Causal feature-surgery to locate WHERE promptable models represent each object.

- **Problem:** Whether SAM-style models maintain discrete object-centric representations (tokens 'owning' objects) or distributed objectness (objects as patterns over patch features) is a resolvable representational question - via causal intervention (ablate/swap candidate representations, observe mask behavior) rather than correlational probing.
- **Core hypothesis (falsifiable):** HYPOTHESIS: causal interventions will show object identity is carried by a low-rank subspace of the mask-token pathway (swapping it transfers masks between objects; ablating it deletes specific objects while preserving scene features) - promptable models ARE object-centric in a strong causal sense, and the object subspace's dimensionality measures how many objects the model can simultaneously individuate (predicting multi-object interference limits).
- **Why important:** Resolves a foundational representation question with a measurable capacity constant (simultaneous-object limit) that predicts practical failure in crowded scenes.
- **Why possibly novel:** Causal object-representation surgery on promptable segmenters is UNVERIFIED - needs lit search.
- **Minimal experiment:** Implement token/subspace swap-and-ablate interventions on SAM's decoder pathway, quantify mask-transfer and deletion specificity, estimate object-subspace rank.
- **Main risk:** Interventions may push activations off-manifold, producing artifacts misread as structure; use manifold-constrained interventions.
- **Mutated from:** W2-A-0019

### W2-A-0298 - Transformers' low-frequency bias caps boundary precision architecturally: same-data CNN-vs-ViT boundary spectroscopy.

- **Problem:** Spectral-bias theory says different architectures preferentially learn different frequency bands; boundary precision is a high-frequency output property, so architecture-level frequency bias should produce measurable boundary-quality differences at matched data and training - a clean theory-to-practice test never run for segmentation.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at matched data/compute/parameters, boundary-error spectra (error energy vs spatial frequency along contours) show architecture-specific cutoffs consistent with spectral-bias theory (ViTs attenuate high-frequency boundary detail more than CNNs at equal aggregate mIoU), the difference persists across scale, and hybrid stems (conv early, attention late) inherit the CNN cutoff - architecture choice imposes a measurable boundary-frequency ceiling independent of learning.
- **Why important:** Would ground the CNN-vs-ViT debate in a measurable, property-specific law rather than aggregate benchmarks, guiding architecture choice for boundary-critical applications.
- **Why possibly novel:** Boundary-spectral architecture comparison at matched budgets is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train matched CNN/ViT/hybrid segmenters on identical data, compute boundary error spectra (using the physical-GT stimuli for precision), compare cutoffs.
- **Main risk:** Matched training across architecture families is never perfectly fair; sweep learning configurations and report robustness.
- **Mutated from:** W2-A-0161

### W2-A-0299 - Segmentation as retrieval at scale: how does non-parametric mask transfer scale with memory size, and does it ever beat parametric knowledge?

- **Problem:** A segmentation system could store millions of labeled region exemplars and segment by retrieval+transfer, scaling knowledge by growing memory rather than retraining - the scaling behavior of memory size versus parametric capacity for dense tasks (retrieval's sweet spots, its ceiling) is uncharted.
- **Core hypothesis (falsifiable):** HYPOTHESIS: retrieval-based segmentation accuracy scales log-linearly with memory size well past the point where matched-parameter models plateau (memory beats parameters for tail classes and rare configurations), with retrieval's advantage concentrated in the frequency tail while parametric models retain the head - implying optimal systems are frequency-split hybrids, and the crossover frequency is measurable and stable.
- **Why important:** Memory-augmented architectures are rising everywhere else (LLM RAG); establishing the dense-prediction scaling equivalent would guide the next architecture generation.
- **Why possibly novel:** Memory-scaling laws for dense prediction are UNVERIFIED - needs lit search.
- **Minimal experiment:** Build exemplar-memory segmenter over frozen features, scale memory across orders of magnitude, compare per-frequency-bin against parametric models at matched total footprint.
- **Main risk:** Retrieval latency and memory engineering may dominate practicality; the science stands regardless of deployment economics.
- **Mutated from:** W2-A-0282

### W2-A-0300 - If all strong models converge, ensembles die: test whether dense-model ensemble gains are collapsing generation by generation.

- **Problem:** Ensembling assumes error diversity; if foundation-era models increasingly share data, objectives, and representations (monoculture convergence), ensemble gains should be measurably shrinking over model generations - a trend with major implications that nobody has tracked.
- **Core hypothesis (falsifiable):** HYPOTHESIS: measuring ensemble gain (over best member) across model cohorts by era shows monotonic decline for dense tasks (error-diversity collapse as lineages share SA-1B/LAION-descended data), the decline is steeper than in the classification ecosystem (dense labels are scarcer, forcing more sharing), and remaining diversity concentrates in models with genuinely disjoint data (medical vs web) - quantifying the ecosystem's convergence tax on reliability engineering.
- **Why important:** Safety-critical systems rely on ensembling/redundancy; if diversity is evaporating ecosystem-wide, redundancy-based safety arguments weaken - better to know now, with numbers.
- **Why possibly novel:** Longitudinal ensemble-gain trend analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Assemble model cohorts by era (2019-2025), measure ensemble gains and error correlations on fixed benchmarks, regress against lineage-overlap measures.
- **Main risk:** Era confounds with scale and performance level; normalize gains by member accuracy and test scale-matched cohorts.
- **Mutated from:** W2-A-0284

## C13-benchmark-failure-audit

### W2-A-0301 - Did SA-1B swallow the test sets? Measure foundation-training contamination of segmentation benchmarks with near-duplicate forensics.

- **Problem:** Foundation models train on web-scale corpora that plausibly contain benchmark test images (or near-duplicates); for segmentation this contamination has never been quantified, though it silently converts zero-shot claims into memorization measurements.
- **Core hypothesis (falsifiable):** HYPOTHESIS: near-duplicate detection between foundation training sets (SA-1B, LAION-derived) and standard segmentation test sets (COCO, ADE20K, DAVIS) will find nontrivial contamination rates, per-image zero-shot performance is measurably higher on contaminated items (memorization signal), and decontaminated re-scoring shrinks published zero-shot gaps between foundations - benchmark contamination is a live confounder in dense prediction, not just NLP.
- **Why important:** Zero-shot segmentation claims underpin the foundation-model narrative; contamination-corrected numbers are the ones that matter.
- **Why possibly novel:** Dense-benchmark contamination forensics is UNVERIFIED - needs lit search (NLP contamination studies are KNOWN).
- **Minimal experiment:** Run scalable near-dup detection (embedding + hash) between public shards of SA-1B/LAION and test sets, stratify model performance by contamination status.
- **Main risk:** Only public shards are checkable; report bounds, not point estimates, for closed corpora.

### W2-A-0302 - Correct the test sets: estimate dense-label error rates on major benchmarks and measure how repairs reorder the leaderboards.

- **Problem:** KNOWN: classification test sets contain pervasive label errors (Northcutt et al.). Dense benchmarks likely contain region- and boundary-level errors at higher rates (harder annotation), but error-rate estimates and leaderboard sensitivity to repairs do not exist for segmentation.
- **Core hypothesis (falsifiable):** HYPOTHESIS: model-consensus-guided expert re-audit will find pixel-level label fault rates of several percent on major benchmarks (concentrated in occlusion boundaries and class confusions), repairing them changes top-model rankings in a measurable fraction of comparisons, and - critically - the models that gain most from repair are those trained WITHOUT the benchmark's sibling training set (label errors currently favor style-matched models).
- **Why important:** Leaderboards steer the field; if their references are faulty in a direction that favors in-ecosystem models, progress measurement is structurally biased.
- **Why possibly novel:** Repair-sensitivity analysis of dense leaderboards is UNVERIFIED - needs lit search.
- **Minimal experiment:** Consensus-flag suspicious regions on 2 benchmarks, expert-adjudicate 3k regions, re-score public models on repaired references.
- **Main risk:** Adjudication of genuinely ambiguous regions; use the three-state protocol (decidable-error vs ambiguous) to keep claims clean.
- **Mutated from:** W2-A-0200

### W2-A-0303 - The polygon ceiling: COCO's coarse polygons impose a measurable upper bound on learnable and measurable boundary quality.

- **Problem:** COCO masks average few vertices per object; both training signal and evaluation reference inherit this coarseness. The exact ceiling it imposes - on what models can learn and on what evaluation can detect - has not been quantified, though COCO remains the field's central training source.
- **Core hypothesis (falsifiable):** HYPOTHESIS: comparing COCO polygons against high-fidelity re-annotations will yield a per-size boundary-error floor (the polygon artifact spectrum), models trained on COCO plateau AT this floor (their boundary style measurably mimics polygon geometry - straight-segment artifacts detectable in predictions), and boundary-metric differences between models evaluated on COCO below the floor are meaningless - one number (the ceiling) reframing hundreds of comparisons.
- **Why important:** Establishes when 'better boundaries on COCO' can even be a real claim, and quantifies the training tax of polygon supervision that the ecosystem inherits.
- **Why possibly novel:** Polygon-artifact ceiling quantification with mimicry detection is UNVERIFIED - needs lit search.
- **Minimal experiment:** High-fidelity re-annotation of 500 COCO objects, compute artifact spectra, test for straight-segment mimicry in model predictions, derive the evaluable floor.
- **Main risk:** Re-annotation cost; 500 objects suffice for the spectrum but per-class claims need more.
- **Mutated from:** W2-A-0156

### W2-A-0304 - Class definitions drift across dataset versions and papers: 'road' 2016 is not 'road' 2024 - measure semantic versioning debt.

- **Problem:** Long-lived benchmarks evolve through relabeling campaigns, errata, and papers' preprocessing choices; the same class name can denote drifting pixel sets across versions, corrupting longitudinal comparisons that the field reads as progress.
- **Core hypothesis (falsifiable):** HYPOTHESIS: diffing dataset versions and reconstructing papers' actual evaluation pixel-sets will reveal class-definition drift large enough to explain measurable fractions of reported multi-year 'progress' on affected classes, and papers citing the same benchmark differ silently in effective test sets (preprocessing forks) at a rate that makes a subset of published comparisons non-comparable - the field lacks semantic versioning and pays for it in phantom progress.
- **Why important:** Longitudinal progress claims are the field's self-narrative; auditing their consistency is basic metrology.
- **Why possibly novel:** Version-drift accounting for segmentation benchmarks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Diff Cityscapes/ADE versions and 20 papers' preprocessing forks, recompute a fixed model's score under each effective test set, tabulate the spread.
- **Main risk:** Reconstructing papers' exact pipelines is laborious; prioritize the most-cited comparison chains.

### W2-A-0305 - Effective headroom estimation: how much of each benchmark's remaining error is model-fixable versus reference noise - the saturation audit.

- **Problem:** Benchmarks near saturation reward noise-fitting, but the field lacks a standard estimate of each benchmark's effective headroom (remaining error that a correct model could actually reduce), so effort allocation across benchmarks is blind.
- **Core hypothesis (falsifiable):** HYPOTHESIS: decomposing residual error on major benchmarks (via multi-annotation, model consensus, and ambiguity measurement) will show several popular benchmarks have effective headroom below 2 points (further gains are style-fitting), while others retain large real headroom concentrated in specific classes - and publishing per-benchmark headroom would measurably shift where new methods report results (a testable sociological prediction).
- **Why important:** Effort follows benchmarks; headroom accounting redirects the field's marginal week of work toward real problems.
- **Why possibly novel:** Systematic headroom estimation across dense benchmarks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Apply the decomposition to 6 benchmarks using existing multi-annotation where available plus targeted re-annotation, publish headroom table.
- **Main risk:** Headroom estimates depend on ambiguity modeling assumptions; report ranges under stated models.
- **Mutated from:** W2-A-0071

### W2-A-0306 - Within-benchmark duplication inflates scores: near-duplicate test images act as multipliers on style-matched models.

- **Problem:** Test sets assembled from web sources contain internal near-duplicates (same scene, same event, burst shots); metrics implicitly weight duplicated content multiply, favoring models that happen to fit the duplicated styles - the duplication structure of dense benchmarks is unmapped.
- **Core hypothesis (falsifiable):** HYPOTHESIS: near-duplicate clustering of major test sets will find measurable duplication (several percent of images with intra-set near-dups), deduplicated re-scoring changes method rankings in close comparisons, and duplication is topic-biased (certain scene types over-weighted), meaning current scores encode hidden topical weightings nobody chose deliberately.
- **Why important:** A cheap, definitive hygiene audit; close SOTA races are exactly where duplicate-weighting artifacts decide outcomes.
- **Why possibly novel:** Intra-benchmark duplication analysis for dense tasks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run embedding-based near-dup clustering on 5 test sets, re-score public models deduplicated, report rank sensitivity.
- **Main risk:** Near-dup thresholds are judgment calls; report across threshold sweeps.
- **Mutated from:** W2-A-0100

### W2-A-0307 - Segmentation performance by geography of image origin: dense prediction has an unmeasured global-equity profile.

- **Problem:** KNOWN: object recognition performs worse on images from lower-income regions (Facebook's Dollar Street analyses). For segmentation - where infrastructure, vehicles, and household objects differ even more visually - the geographic performance profile has not been measured, though these models deploy globally.
- **Core hypothesis (falsifiable):** HYPOTHESIS: mainstream segmentation models show substantial performance gradients across image-origin geography (worse boundary AND recognition quality in under-represented regions), the gradient persists for supposedly universal classes (person, food, bed) not just region-specific ones, and gradient magnitude correlates with training-corpus geo-distribution estimates - making the data-origin ledger an actionable fairness instrument for dense prediction.
- **Why important:** Segmentation increasingly gates real services (medical triage, agricultural tools, AR); an unmeasured geographic performance cliff is an equity failure waiting to surface.
- **Why possibly novel:** Geographic stratification of dense-prediction quality is UNVERIFIED - needs lit search.
- **Minimal experiment:** Annotate geo-diverse image samples (Dollar-Street-style) with masks, evaluate model zoo, regress performance on region and corpus-representation estimates.
- **Main risk:** Annotation quality must be uniform across regions to avoid reproducing the artifact under audit; use one centralized expert team.

### W2-A-0308 - The sensor gap: benchmarks are smartphone/DSLR photos, deployments are industrial/scientific sensors - quantify the unbenchmarked capture-hardware shift.

- **Problem:** Public benchmarks overwhelmingly sample consumer camera output (processed, sharpened, tone-mapped), while deployments run on machine-vision cameras, line-scan sensors, and scientific detectors with alien noise/optics profiles - a capture-hardware distribution gap that no benchmark measures.
- **Core hypothesis (falsifiable):** HYPOTHESIS: models transferred from consumer-photo training to industrial-sensor imagery degrade substantially even for identical scene content (verifiable with dual-capture rigs: consumer + machine-vision camera imaging the same scenes), the degradation localizes to texture- and noise-sensitive classes, and simple sensor-simulation augmentation (noise/optics models) recovers a large fraction - the gap is real, measurable, and cheaply mitigable once acknowledged.
- **Why important:** Industrial vision is a huge deployment share served by benchmarks that never sampled its input distribution; the dual-capture measurement would ground years of anecdotal complaints.
- **Why possibly novel:** Dual-capture sensor-gap quantification is UNVERIFIED - needs lit search.
- **Minimal experiment:** Build dual-camera rig, capture 300 matched scenes, evaluate models cross-sensor, test sensor-simulation recovery.
- **Main risk:** One industrial camera does not represent all; use 3 sensor types to bound diversity.
- **Mutated from:** W2-A-0229

### W2-A-0309 - PQ's 0.5-IoU matching cliff makes panoptic rankings noise-sensitive: measure how many published gaps live at the threshold.

- **Problem:** Panoptic Quality matches predictions to GT at a hard IoU>0.5 threshold; instances near the threshold flip between matched and unmatched under tiny changes, injecting discontinuous noise into scores - the fraction of published PQ differences attributable to near-threshold instances is unknown.
- **Core hypothesis (falsifiable):** HYPOTHESIS: perturbation analysis (jittering predictions/GT within annotation noise) shows PQ variance is dominated by near-threshold instances, a smooth-matching variant (soft credit around the threshold) reduces ranking noise substantially while preserving interpretation, and re-scoring recent panoptic literature with the smooth variant erases a measurable fraction of published gaps - the metric's discontinuity has been manufacturing significance.
- **Why important:** Metric-induced noise wastes the field's effort ratifying phantom differences; a validated smooth variant is a drop-in repair.
- **Why possibly novel:** Threshold-cliff noise accounting for PQ is UNVERIFIED - needs lit search.
- **Minimal experiment:** Jitter-based variance decomposition of PQ on COCO-panoptic across models, implement smooth matching, re-score and compare rank stability.
- **Main risk:** Any new metric fights adoption inertia; position as diagnostic first, replacement second.

### W2-A-0310 - Longitudinal val-test gap growth: leaderboards teach the community to overfit validation sets - measure the ecosystem-level adaptive overfitting rate.

- **Problem:** KNOWN: adaptive overfitting on reused test sets was studied for classification (Recht et al. line of work) with reassuring results - but segmentation's smaller, older, more-reused validation sets and richer hyperparameter surfaces may behave worse, and nobody has run the equivalent audit for dense prediction.
- **Core hypothesis (falsifiable):** HYPOTHESIS: reproducing the fresh-test-set methodology for segmentation (new Cityscapes/ADE-protocol test images collected today) will show larger val-to-fresh performance drops for recent methods than early ones (growing adaptive overfitting), with the growth concentrated in methods using validation-heavy development (NAS, heavy tuning) - dense prediction's reassurance on this question is currently borrowed from classification without evidence.
- **Why important:** If the drop grows with method recency, recent SOTA gains partly measure validation-set adaptation - the most fundamental audit a benchmark ecosystem can run on itself.
- **Why possibly novel:** Fresh-test-set replication for dense benchmarks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Collect and annotate protocol-faithful fresh test sets (500 images) for 2 benchmarks, evaluate the historical model zoo, plot drop vs publication year.
- **Main risk:** Fresh collection can accidentally shift distribution; protocol fidelity (same cities, seasons, cameras where possible) is the crux.

### W2-A-0311 - Difficulty drift: modern models find different images hard than old models did - curated 'hard subsets' expire and need versioning.

- **Problem:** Curated hard-example subsets (built from some era's model failures) are used as fixed difficulty benchmarks, but difficulty is model-relative; whether old hard subsets remain hard - and whether difficulty ORDER is stable across model generations - determines their continued validity.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-image difficulty rankings correlate only moderately across model generations (difficulty drift is substantial), hard subsets curated pre-foundation-era are disproportionately solved by modern models (their hardness encoded era-specific weaknesses, not intrinsic difficulty), and a stable 'intrinsically hard' core (hard for ALL generations) exists and is characterizable - separating timeless difficulty (ambiguity, information limits) from era difficulty (fixable gaps).
- **Why important:** Hard-subset benchmarks steer robustness research; expired hardness wastes effort and understates progress, while the intrinsic-core characterization is a durable scientific object.
- **Why possibly novel:** Cross-generation difficulty-drift measurement is UNVERIFIED - needs lit search.
- **Minimal experiment:** Evaluate model-zoo generations on fixed benchmarks, compute cross-era difficulty correlations, characterize the all-era-hard core.
- **Main risk:** Generation boundaries are fuzzy; define by training-data era and capability cohorts.

### W2-A-0312 - Masks reveal their dataset: annotation-style leakage is strong enough to classify a mask's source benchmark from geometry alone.

- **Problem:** If mask geometry alone (no image) identifies the source dataset with high accuracy, then dataset-specific annotation style is a large learnable signal - and cross-dataset evaluation partially tests style transfer rather than visual capability. The magnitude of style leakage has never been measured ecosystem-wide.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a geometry-only classifier distinguishes masks from 8 major datasets well above chance (style signatures are strong), models trained on each dataset reproduce its signature on NEW images (style is learned, not content-driven), and regressing cross-dataset performance drops on style distance shows style explains a substantial share of measured 'domain gaps' between datasets with similar imagery - the ecosystem's labels are dialects, and models learn the dialect.
- **Why important:** Dialect effects contaminate every cross-dataset conclusion; measuring them enables style-normalized evaluation, a cleaner science.
- **Why possibly novel:** Ecosystem-wide style-leakage quantification is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train mask-geometry dataset classifier, verify signature reproduction in model outputs, decompose cross-dataset gaps into style vs content components.
- **Main risk:** Content differences (different class geometries per dataset) confound style; control by comparing within shared classes at matched size.
- **Mutated from:** W2-A-0224

### W2-A-0313 - Statistical power audit of segmentation SOTA claims: how many published gains survive bootstrap significance testing on their own benchmarks?

- **Problem:** Segmentation papers claim SOTA on point estimates over test sets with unquantified variance (image sampling, seed variance, near-threshold instances); the fraction of published gains that are statistically distinguishable from noise has never been computed for the field.
- **Core hypothesis (falsifiable):** HYPOTHESIS: applying image-level bootstrap plus seed-variance accounting to recent top-venue segmentation comparisons will show a substantial fraction (>30%) of claimed improvements are within noise (not significant at reasonable levels), non-significant gains concentrate in small-benchmark and small-delta papers, and the field's effective discovery rate is far lower than its publication rate implies - a meta-scientific measurement with direct norms-changing potential (report CIs, multiple seeds).
- **Why important:** Publication-level noise pollutes meta-decisions (what directions 'work'); quantifying it is the prerequisite for fixing incentive structures.
- **Why possibly novel:** Field-wide significance auditing for dense prediction is UNVERIFIED - needs lit search (similar audits exist in other ML subfields - KNOWN pattern, e.g. metric-learning reality checks).
- **Minimal experiment:** Reproduce 20 recent comparisons from public checkpoints, bootstrap test-set CIs and seed spread, tabulate survival rates.
- **Main risk:** Reproduction burden; restrict to papers with released models to stay feasible.
- **Mutated from:** W2-A-0164

### W2-A-0314 - Video benchmarks annotate the easy frames: keyframe selection bias means reported VOS accuracy skips blur, transitions, and bad light.

- **Problem:** Video annotation pipelines select frames for labeling where annotation is feasible (sharp, well-lit, unambiguous), so evaluation systematically avoids the frames where models most likely fail - a sampling bias baked into every video benchmark's reported number.
- **Core hypothesis (falsifiable):** HYPOTHESIS: annotated frames in major video benchmarks differ measurably from unannotated neighbors (sharper, better-exposed, less motion - quantifiable via image statistics), model performance on pseudo-evaluable hard frames (via high-confidence temporal interpolation of GT) is substantially lower than reported numbers, and the bias grows with scene dynamism - published VOS scores are upper bounds with a measurable optimism gap.
- **Why important:** Deployment consumes every frame, not curated ones; the optimism gap is exactly the deployment surprise waiting in video products.
- **Why possibly novel:** Annotated-frame selection-bias measurement for video benchmarks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Compare image statistics of annotated vs neighboring frames across 4 VOS benchmarks, construct interpolation-based hard-frame evaluation, measure the gap.
- **Main risk:** Interpolated GT on hard frames is imperfect; use conservative confidence gating and human spot checks.

### W2-A-0315 - Patient-level leakage in public medical segmentation datasets: audit how many benchmarks let the same patient into train and test.

- **Problem:** Medical volumes from one patient (multiple slices, studies, or visits) appearing across train/test splits inflate performance via patient-specific memorization (anatomy, implants, scanner metadata burned into pixels); the prevalence of this leakage across public medical segmentation benchmarks is unaudited.
- **Core hypothesis (falsifiable):** HYPOTHESIS: patient-identity forensics (anatomical fingerprint matching across split boundaries) will find leakage in a meaningful fraction of public medical segmentation datasets (especially aggregated/multi-source ones), leakage-affected benchmarks show measurably inflated scores (re-split evaluation drops performance), and the inflation is largest for high-capacity models - a hygiene audit with direct clinical-claims consequences.
- **Why important:** Medical performance claims feed regulatory and clinical decisions; patient leakage is the most consequential form of benchmark inflation in this domain.
- **Why possibly novel:** Cross-dataset patient-leakage forensics at ecosystem scale is UNVERIFIED - needs lit search (individual dataset issues are occasionally reported - KNOWN pattern).
- **Minimal experiment:** Build anatomical-fingerprint matcher (bone structure, vessel trees), scan 10 public datasets' splits, re-split and re-evaluate where leakage is found.
- **Main risk:** Fingerprint false positives (similar anatomy) must be controlled; validate matcher on datasets with known patient IDs.
- **Mutated from:** W2-A-0100

### W2-A-0316 - Negative-set poverty in safety datasets: smoke/fire benchmarks lack the hard negatives (fog, steam, sunsets) that dominate deployment false alarms.

- **Problem:** Detection benchmarks report false-positive rates against their own negative sets, but safety datasets' negatives are conveniences (random frames), not the confusable phenomena that cause real false alarms - so reported FPRs bear no relation to deployed FPRs, in an unquantified way.
- **Core hypothesis (falsifiable):** HYPOTHESIS: constructing a hard-negative bank (fog banks, steam vents, dust, sunsets, orange lighting, reflective surfaces) and re-evaluating public smoke/fire models will show deployment-realistic FPRs orders of magnitude above benchmark FPRs, model rankings will reorder substantially (benchmark-FPR optimization does not transfer), and the hard-negative bank composition needed to PREDICT deployed FPR is discoverable from false-alarm logs - benchmark negatives need engineering as much as positives.
- **Why important:** False alarms determine whether safety systems get trusted or unplugged; benchmark-to-deployment FPR translation is the missing number for the whole application class.
- **Why possibly novel:** Hard-negative-bank methodology with deployment-FPR validation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Assemble hard-negative video bank, re-evaluate 6 public models, compare with any obtainable deployment false-alarm statistics.
- **Main risk:** Deployment FPR data is proprietary; partner with one camera-network operator or use public wildfire-camera archives.
- **Mutated from:** W2-A-0088

### W2-A-0317 - Turntable bias in transparent-object datasets: background diversity deficit makes lab-collected benchmarks trivially solvable by background memorization.

- **Problem:** Transparent/reflective object datasets are heavily lab-collected (turntables, repeated backgrounds); models may key on the small background vocabulary rather than object evidence, making benchmark scores unrepresentative - the background-diversity deficit and its exploitation are unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: background-swap evaluation (same objects composited onto novel backgrounds) collapses transparent-object SOTA disproportionately compared to opaque-object controls (transparency models are more background-dependent by necessity - but current ones are background-MEMORIZING, a different thing), and per-dataset background vocabulary size predicts the collapse magnitude - turning an intuition about lab bias into a measured validity criterion for the whole dataset family.
- **Why important:** Transparent-object perception feeds robotics safety; validity criteria for its benchmarks protect against false confidence.
- **Why possibly novel:** Background-vocabulary auditing for transparency datasets is UNVERIFIED - needs lit search.
- **Minimal experiment:** Quantify background diversity across 5 transparency datasets, run background-swap collapse tests on public models with opaque controls.
- **Main risk:** Compositing transparent objects onto new backgrounds is technically hard (refraction must be re-rendered); use capture-based swaps where possible.
- **Mutated from:** W2-A-0119

### W2-A-0318 - Aesthetic bias: benchmarks oversample well-composed photographs, and performance correlates with photographic quality - ugly images are the real test.

- **Problem:** Dataset images pass through human selection filters (what people photograph, upload, and curators keep) biased toward aesthetic composition; deployment sees uncomposed frames (fixed cameras, robots, egocentric streams). Whether model performance secretly tracks aesthetic quality has not been measured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: per-image segmentation performance correlates measurably with aesthetics scores (composition, exposure) even controlling for content difficulty, benchmarks' aesthetics distributions sit far above deployment-stream distributions (quantifiable gap), and reweighting evaluation toward deployment-realistic aesthetics drops scores and reorders methods - the ecosystem has been grading models on portfolio shots while deploying them on security-camera reality.
- **Why important:** A quantified aesthetics-performance coupling would explain systematic deployment disappointments and motivate uncomposed-image benchmarks.
- **Why possibly novel:** Aesthetics-stratified performance analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Score benchmark and deployment-stream images with aesthetics models, measure performance-aesthetics correlation with content-difficulty controls, construct reweighted evaluation.
- **Main risk:** Aesthetics scores entangle with genuine difficulty (blur IS harder); careful covariate design is the whole game.

### W2-A-0319 - Annotation-display resolution is missing metadata: masks were drawn at unknown zoom levels, making boundary precision claims unanchorable.

- **Problem:** A mask's boundary precision is bounded by the resolution at which the annotator VIEWED the image, but datasets never record display/zoom conditions - so boundary supervision quality varies invisibly within and across datasets, and evaluation cannot distinguish model error from annotation-viewing artifacts.
- **Core hypothesis (falsifiable):** HYPOTHESIS: viewing-resolution signatures are forensically recoverable from mask geometry (quantization patterns, minimum feature sizes reveal the annotation zoom), datasets show wide internal variance in recovered viewing resolution, and boundary-metric noise correlates with recovered viewing resolution - establishing display metadata as a required annotation-protocol field and providing retroactive quality stratification for existing data.
- **Why important:** An entire hidden quality dimension of every existing dataset becomes measurable, enabling resolution-stratified training and honest boundary evaluation.
- **Why possibly novel:** Viewing-resolution forensics for annotations is UNVERIFIED - needs lit search.
- **Minimal experiment:** Validate the forensic estimator on controlled-zoom annotations, apply to major datasets, correlate recovered resolution with boundary-noise estimates.
- **Main risk:** Forensic recovery may be too noisy per-mask; dataset-level distributions may be the honest granularity.
- **Mutated from:** W2-A-0150

### W2-A-0320 - Intra-dataset ontology noise: the same dataset labels identical object types inconsistently, and the confusion structure is measurable and learnable-around.

- **Problem:** Within one dataset, borderline objects (armchair vs chair, path vs road, shrub vs tree) are labeled inconsistently across images by different annotators - intra-dataset ontology noise that models must absorb, distinct from inter-dataset convention differences and never separately quantified.
- **Core hypothesis (falsifiable):** HYPOTHESIS: intra-dataset labeling of borderline categories is inconsistent at measurable rates (findable via visually-near-duplicate object pairs with different labels within one dataset), models resolve the inconsistency by learning context-dependent arbitrary rules (probeable), and class-merging evaluation (scoring confusable-pair classes jointly) recovers substantial apparent performance - separating true recognition failure from ontology noise absorption in every dataset's confusion matrix.
- **Why important:** Confusion-matrix entries between sibling classes drive per-class conclusions and long-tail claims; knowing which entries are ontology noise re-reads much of that literature.
- **Why possibly novel:** Within-dataset ontology-noise quantification via near-duplicate label disagreement is UNVERIFIED - needs lit search.
- **Minimal experiment:** Mine visually-similar object pairs with conflicting labels within ADE/COCO, estimate per-class-pair inconsistency rates, re-evaluate models under class-merged protocols.
- **Main risk:** Visual similarity does not guarantee same true class; human adjudication of mined pairs needed.
- **Mutated from:** W2-A-0237

### W2-A-0321 - LVIS federated annotation makes rare-class scores statistically fragile: put confidence intervals on every rare-class claim.

- **Problem:** Federated annotation (KNOWN: LVIS design - not every image checked for every class) means rare-class evaluation rests on few positives and unverified negatives; the resulting statistical fragility of rare-class AP - and how many published rare-class gains fall inside it - has not been systematically computed.
- **Core hypothesis (falsifiable):** HYPOTHESIS: bootstrap confidence intervals on LVIS rare-class metrics are wide enough to contain most published method-to-method rare-class improvements (the celebrated gains are statistically unresolvable), the unverified-negative assumption injects additional bias measurable via exhaustive re-annotation of an image sample, and rare-class conclusions require aggregation protocols (class grouping, hierarchical models) the field does not use - current rare-class science runs below its own noise floor.
- **Why important:** Long-tail methods are ranked by exactly these fragile numbers; the field needs to know which of its conclusions the data can actually support.
- **Why possibly novel:** Fragility quantification of federated rare-class evaluation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Bootstrap LVIS rare-class metrics across published models, exhaustively re-annotate 500 images to measure the negative-assumption bias, overlay published deltas on CIs.
- **Main risk:** None serious - this is careful statistics on existing artifacts; main cost is the re-annotation sample.
- **Mutated from:** W2-A-0313

### W2-A-0322 - Same dataset, different numbers: meta-analysis of score spread for identical model-benchmark pairs across papers reveals the reproduction noise floor.

- **Problem:** The same model evaluated on the same benchmark yields different numbers across papers (preprocessing, resolution, checkpoint, protocol forks); this reproduction spread - the ecosystem's effective measurement noise - has never been compiled, though it bounds what score differences can mean.
- **Core hypothesis (falsifiable):** HYPOTHESIS: compiling reported scores for identical model-benchmark pairs across 100+ papers will show reproduction spreads (often 1-3 points) comparable to typical claimed improvements, spread correlates with protocol under-specification per benchmark (some benchmarks are reproducible, others are not), and the analysis yields a reproduction-noise table that any reviewer can use to sanity-check claimed gains - the field's measurement infrastructure quantified from its own literature, no new experiments needed.
- **Why important:** The cheapest possible meta-audit (literature mining only) that would immediately recalibrate how everyone reads improvement claims.
- **Why possibly novel:** Cross-paper reproduction-spread compilation for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Mine reported baseline numbers from open-access papers for 10 model-benchmark pairs, tabulate spreads, correlate with protocol specification completeness.
- **Main risk:** Papers may cite each other's numbers (spread underestimated); track citation provenance of each number.
- **Mutated from:** W2-A-0304

### W2-A-0323 - Measure human mIoU: segmentation benchmarks lack the human-performance baselines that every claims discussion needs.

- **Problem:** Unlike ImageNet classification (KNOWN: human baselines exist), segmentation benchmarks have no measured human performance under the benchmark's own protocol - so 'superhuman' or 'approaching human' claims float free of data, and the human-model error comparison (WHERE they differ) has no reference.
- **Core hypothesis (falsifiable):** HYPOTHESIS: careful human evaluation under benchmark protocols will show humans BELOW current SOTA on consistency-demanding aspects (class-boundary conventions, per-pixel diligence over large stuff regions) but far ABOVE on ambiguity resolution and rare-object recognition - a crossing profile, not a single number - and human-vs-model error decorrelation identifies exactly the residual capabilities models lack, sharpening what 'progress toward human-level segmentation' should even mean.
- **Why important:** Reference points anchor a field's self-assessment; segmentation has been running without one for fifteen years.
- **Why possibly novel:** Protocol-faithful human baselines for standard segmentation benchmarks are UNVERIFIED - needs lit search.
- **Minimal experiment:** Run trained human annotators through Cityscapes/ADE evaluation subsets under time-controlled conditions, score identically to models, publish the profile.
- **Main risk:** Human performance depends heavily on time budget and training; report as curves over effort, not points.

### W2-A-0324 - Model-in-the-loop adversarial test collection for segmentation: does human-sourced hardness transfer across models or just defeat the collection-time model?

- **Problem:** Adversarial benchmark collection (humans search for model failures, Dynabench-style - KNOWN in NLP/classification) has not been seriously run for segmentation, and its core validity question - whether collected hardness is model-specific or generalizes - is open for dense tasks where failure modes are more structured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: human-in-the-loop collection against one segmentation model yields examples that transfer as hard to unrelated models at high rates for certain failure families (ambiguous boundaries, rare configurations - shared data holes) but not others (model-specific texture quirks), and the transferable/non-transferable split aligns with the shared-blind-spot decomposition - making adversarial collection a practical shared-hole prospecting tool, with known limits, for dense prediction.
- **Why important:** If hardness transfers, adversarial collection becomes the cheapest way to find the ecosystem's real gaps; if not, a popular methodology is invalid for dense tasks - either answer matters.
- **Why possibly novel:** Transfer-validity analysis of adversarial collection for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run collection sessions against one public model (annotators photograph/find failure scenes), evaluate collected set on 8 other models, decompose transfer by failure family.
- **Main risk:** Collector creativity bounds what is found; use diverse collector pools and seed taxonomies.
- **Mutated from:** W2-A-0290

### W2-A-0325 - The ignore-region census: what fraction of each benchmark's pixels are excluded from evaluation, what lives there, and who benefits?

- **Problem:** Benchmarks exclude void/ignore/ambiguous pixels from scoring at rates nobody tabulates; the excluded content is non-random (crowds, boundaries, distant clutter - often the hardest content), so exclusion rates and composition silently shape what benchmarks measure and which methods look good.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a census across 10 benchmarks will show ignore fractions varying widely (2-20%) with systematically hard content over-represented in exclusions, models disagree most exactly there (confirming difficulty), and hypothetically scoring ignore regions with best-effort reference labels would reorder methods (some methods' advantages evaporate outside the scored region) - exclusion policy is an unacknowledged benchmark design choice with ranking consequences, deserving explicit reporting standards.
- **Why important:** What benchmarks refuse to measure defines them as much as what they measure; the census makes an invisible design choice visible and comparable.
- **Why possibly novel:** Cross-benchmark ignore-region census is UNVERIFIED - needs lit search.
- **Minimal experiment:** Tabulate ignore statistics and content composition across benchmarks, obtain best-effort labels for samples of ignored regions, measure model disagreement and ranking sensitivity.
- **Main risk:** Best-effort labels in ignored regions are noisy by construction (that is why they were ignored); use consensus protocols and report uncertainty.
- **Mutated from:** W2-A-0194

## C14-assumption-tests

### W2-A-0326 - 'More context always helps' is false for boundaries: context-size sweeps show boundary precision peaks at small context and degrades with more.

- **Problem:** The field assumes larger receptive fields and global attention monotonically help. For boundary placement - a local decision - distant context may act as noise or prior-override, but the sign of context's marginal value per output property has not been measured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: sweeping usable context (masked attention radius) shows region-classification accuracy rises monotonically with context while boundary-localization precision is NON-monotonic - peaking at modest context and declining as global context grows (attention dilution and prior-override at edges) - so single-architecture designs necessarily trade one property against the other, and property-split readouts (local for edges, global for semantics) beat unified designs at matched compute.
- **Why important:** Overturns a monotonicity assumption embedded in a decade of architecture design and explains why global-attention models did not deliver boundary gains proportional to their semantic gains.
- **Why possibly novel:** Property-resolved signed context-value curves are UNVERIFIED - needs lit search.
- **Minimal experiment:** Context-radius sweep via attention masking on trained models plus retrained variants, plot per-property curves on 3 datasets.
- **Main risk:** Masked-attention inference is off-manifold for models trained global; retrained-variant arm controls this.
- **Mutated from:** W2-A-0137

### W2-A-0327 - 'Pretraining always helps medical segmentation' - map the regime where random initialization plus long schedules matches or beats transfer.

- **Problem:** Transfer from natural-image pretraining is default practice in medical segmentation, but the regime where it actually pays (versus long-schedule random init) - as a function of target-data volume, modality distance, and 3D-ness - has not been mapped since foundation-scale pretraining arrived. KNOWN: Rethinking-pretraining-style results exist for detection in natural images; the medical dense-prediction regime map is the missing piece.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for 3D medical tasks above a measurable data threshold (thousands of volumes), random-init with matched total compute matches foundation-transfer within noise (pretrained features encode natural-image priors that 3D medical never uses), while below the threshold transfer wins decisively - and the threshold is predictable from modality distance, giving practitioners a computable transfer-or-not rule.
- **Why important:** Transfer choices shape every medical project's pipeline and licensing constraints; an evidence-based regime map replaces cargo-cult defaults.
- **Why possibly novel:** Compute-matched transfer regime mapping for 3D medical dense tasks is UNVERIFIED - needs lit search.
- **Minimal experiment:** Grid over target-data volume x init strategy at matched compute on 4 medical datasets spanning modality distance, fit the crossover surface.
- **Main risk:** Foundation models keep improving, moving the frontier; publish the methodology as much as the numbers.

### W2-A-0328 - 'Higher resolution always helps' - native 4K inference can UNDERPERFORM downsampled inference through aliasing and receptive-field mismatch.

- **Problem:** Teams assume feeding maximum resolution maximizes accuracy, but models trained at moderate resolution meet 4K inputs with mismatched object scales and un-antialiased downsampling paths inside the network - the sign of the resolution effect at the high end is untested folklore.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for models trained at 1024-class resolutions, native 4K inference measurably underperforms properly-antialiased 2x-downsampled inference on standard content (the extra pixels arrive at scales the model never learned and alias in strided ops), with the crossover resolution predictable from training statistics - 'feed it everything' is quantifiably wrong, and correct test-time scale selection is a free win.
- **Why important:** High-res cameras are universal; a validated scale-selection rule with the counter-intuitive warning would immediately correct widespread silent quality loss.
- **Why possibly novel:** High-end resolution-response measurement with aliasing attribution is UNVERIFIED - needs lit search.
- **Minimal experiment:** Evaluate model zoo across inference-resolution ladders on 4K-native content with and without proper antialiasing, locate crossovers and attribute via aliasing diagnostics.
- **Main risk:** Effect depends on content object-scale distribution; report per scale-profile.
- **Mutated from:** W2-A-0238

### W2-A-0329 - How far does per-frame + matching go on video segmentation? Establish the strong frame-independent baseline the VOS literature skips.

- **Problem:** Video architectures (memory, propagation) are justified against weak per-frame baselines; with modern foundation features, per-frame segmentation + lightweight Hungarian identity matching may close most of the gap - the honest baseline that would price temporal machinery has not been established.
- **Core hypothesis (falsifiable):** HYPOTHESIS: frame-independent segmentation with optimal-transport identity linking recovers a large majority of specialized video architectures' J&F on standard benchmarks (temporal modeling's real contribution is far smaller than the literature implies, concentrated in occlusion gaps), and the gap decomposition (what per-frame+matching CANNOT do) yields the actual justification spec for temporal machinery - benchmark inflation by weak baselines has obscured what video models are for.
- **Why important:** Correct baselining redirects video-architecture research toward its true residual value; the compute savings of per-frame pipelines are also practically large.
- **Why possibly novel:** Foundation-era strong per-frame baselining is UNVERIFIED - needs lit search (older per-frame baselines are KNOWN but pre-date current features).
- **Minimal experiment:** Build per-frame + matching pipeline over modern features, evaluate on DAVIS/MOSE/LVOS, decompose remaining gap by failure type.
- **Main risk:** Matching design choices affect results; publish tuned and naive variants for honesty.
- **Mutated from:** W2-A-0291

### W2-A-0330 - Do boundary losses actually improve boundaries? Meta-analysis plus controlled reruns of the boundary-loss literature under noise-floor-aware evaluation.

- **Problem:** Dozens of papers claim boundary-loss gains measured by boundary metrics on annotation-noisy references; given measured annotation noise floors (few px), many claimed gains may be statistically indistinguishable from noise or artifacts of style-matching - the literature has never been audited as a whole.
- **Core hypothesis (falsifiable):** HYPOTHESIS: rerunning representative boundary-loss methods under noise-aware evaluation (multi-annotated references, significance testing, physical-GT stimuli) will show a substantial fraction of published boundary gains do not survive (they were within annotation noise or reflected style-matching to the reference dataset's annotation conventions), while a minority survive robustly - separating the real effects from the noise-fitting in a literature that currently cannot tell them apart.
- **Why important:** Practitioners choose losses from this literature; an audited shortlist of actually-working methods is directly useful, and the meta-finding disciplines future evaluation.
- **Why possibly novel:** Noise-floor-aware audit of the boundary-loss literature is UNVERIFIED - needs lit search.
- **Minimal experiment:** Reproduce 8 boundary-loss methods on common backbones, evaluate on multi-annotated and physical-GT references with CIs, tabulate survival.
- **Main risk:** Reproduction fidelity disputes; use released code and pre-registered protocols.
- **Mutated from:** W2-A-0151

### W2-A-0331 - Dice's gradient pathology on multi-instance images: the loss concentrates learning on the largest lesion and starves the rest - diagnose, don't re-loss.

- **Problem:** Dice-family losses are the medical default, computed image-wise over union of instances; their gradient structure mathematically over-weights large components, plausibly explaining chronic small-lesion misses - but the pathology has been argued loosely, not measured as gradient flow per instance.
- **Core hypothesis (falsifiable):** HYPOTHESIS: instrumenting per-instance gradient contributions during Dice training shows small co-occurring lesions receive gradient shares far below their count share (a measurable starvation ratio growing with size disparity), starvation predicts which lesions the final model misses, and the SAME model trained on per-component-normalized sampling (a data-side fix, not a new loss) recovers most missed instances - locating the failure in gradient allocation, with the measurement mattering more than any specific remedy.
- **Why important:** Small-lesion misses are THE clinical failure mode; a mechanistic gradient-level diagnosis converts loss-choice debates into measurable engineering.
- **Why possibly novel:** Per-instance gradient-flow instrumentation of Dice training is UNVERIFIED - needs lit search.
- **Minimal experiment:** Instrument gradient contributions on multi-lesion datasets during training, correlate starvation ratios with final per-lesion recall, validate the sampling fix.
- **Main risk:** Gradient bookkeeping at instance level is implementation-heavy; start with 2D to keep it tractable.
- **Mutated from:** W2-A-0068

### W2-A-0332 - Where does adaptation live? Decoder-only fine-tuning matches full fine-tuning under most domain shifts - locate the layers that shift actually touches.

- **Problem:** Fine-tuning practice assumes shift requires updating the whole network, but if most domain shift is readout-level (recombining stable features) rather than feature-level, tiny adaptations suffice - the locus-of-adaptation question, answerable by layer-restricted tuning grids, is unresolved for dense prediction.
- **Core hypothesis (falsifiable):** HYPOTHESIS: across shift types, layer-restricted fine-tuning shows a structured locus map - photometric shifts are absorbed almost entirely in the first two conv/embedding layers, annotation-convention shifts in the final decoder layers, and only semantic-novelty shifts require mid-network updates - so shift-type-diagnosed minimal tuning matches full fine-tuning at a few percent of trainable parameters, and the locus map itself is a diagnostic of what kind of shift one faces.
- **Why important:** Adaptation cost and forgetting both scale with touched parameters; a validated locus map makes adaptation surgical instead of wholesale.
- **Why possibly novel:** Shift-type-resolved locus mapping is UNVERIFIED - needs lit search (parameter-efficient tuning is KNOWN but not organized as shift-diagnostic locus science).
- **Minimal experiment:** Layer-restricted tuning grids across shift-type ladders on 2 architectures, map recovery fraction per (layer-set, shift-type) cell.
- **Main risk:** Architectures differ in where they put capacity; replicate across CNN/ViT.
- **Mutated from:** W2-A-0226

### W2-A-0333 - Attention maps are not explanations for masks: perturbation-faithfulness testing of the field's default segmentation interpretability.

- **Problem:** Papers routinely present decoder attention maps as explanations of segmentation decisions, but attention-faithfulness critiques from NLP (KNOWN: 'Attention is not Explanation' debate) have never been rigorously transplanted to dense prediction, where the spatial structure makes faithfulness both more checkable and more consequential.
- **Core hypothesis (falsifiable):** HYPOTHESIS: perturbation-based faithfulness tests (occlude regions the attention claims matter, measure mask change) will show segmentation attention maps are weakly faithful at best - high-attention regions often contribute little causally while low-attention context drives decisions - and faithfulness varies systematically by architecture (cross-attention decoders less faithful than per-pixel heads), meaning a large fraction of published qualitative 'the model attends to X' claims in segmentation papers are unsupported by causal evidence.
- **Why important:** Interpretability claims inform trust and debugging; if the default tool is unfaithful for dense tasks, the field's explanatory practice needs replacement with causal methods.
- **Why possibly novel:** Systematic attention-faithfulness auditing for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Run occlusion-based causal tests against attention rankings across 5 segmentation architectures, quantify faithfulness scores per family.
- **Main risk:** Occlusion perturbations are off-manifold; complement with in-painting-based counterfactuals.

### W2-A-0334 - Class-agnostic masks leak semantics: mask shape alone predicts object category - with privacy and 'semantic-free' claim consequences.

- **Problem:** SAM-style outputs are called class-agnostic, and mask-only data is shared as if semantically anonymized; but shape is strongly class-informative, so 'agnostic' masks may carry recoverable semantics - the leakage magnitude is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: classifiers on mask geometry alone (no pixels) recover object categories at high accuracy for hundreds of classes (shape IS semantics for most artifacts and organisms), scene-level mask ensembles recover scene types and activities at troubling rates (privacy: floor plans, medical conditions from mask silhouettes), and therefore both the 'class-agnostic' framing and mask-only data-sharing practices need revision - a measurement with simultaneously scientific (shape-semantics coupling) and policy implications.
- **Why important:** Mask-only sharing is treated as safe anonymization in medical and enterprise contexts; quantified leakage would change data-governance practice, and the shape-semantics coupling number is fundamental.
- **Why possibly novel:** Mask-only semantic-leakage quantification at scale is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train shape-only classifiers on COCO/LVIS masks, measure category and scene recovery rates, demonstrate leakage on a mask-only 'anonymized' release scenario.
- **Main risk:** Leakage rates depend on mask quality; report across quality levels.
- **Mutated from:** W2-A-0012

### W2-A-0335 - The boundary is in the image: measure how much boundary precision is recoverable post hoc by model-free image-adherence, revisiting CRF-era wisdom with modern measurements.

- **Problem:** Pre-deep-learning systems sharpened masks with image-adherent post-processing (CRF-style - KNOWN); modern pipelines dropped this, assuming learned decoders internalized it. Whether today's model boundary errors are still largely recoverable from the image itself - model-free - quantifies how much 'boundary learning' decoders actually do versus could delegate.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a strong model-free image-adherence step (modern edge-aware filtering, no learning) recovers a large fraction of the boundary-metric gap between current models and the annotation noise floor on high-contrast boundaries (the information was in the image all along; decoders under-use it), while recovering nothing on semantic boundaries (where models genuinely decide) - splitting every model's boundary error into 'lazy' (image-recoverable) and 'hard' (semantic) components, a decomposition the field lost when it abandoned post-processing.
- **Why important:** If a big lazy component exists, cheap universal post-processing beats architecture work for boundary quality, and boundary benchmarking should report the split.
- **Why possibly novel:** Lazy/hard boundary decomposition with modern models is UNVERIFIED - needs lit search.
- **Minimal experiment:** Apply tuned model-free refinement to model-zoo outputs, measure per-boundary-type recovery against noise floors on multi-annotated references.
- **Main risk:** Refinement can hurt on soft/fuzzy boundaries; report signed effects per boundary class.
- **Mutated from:** W2-A-0153

### W2-A-0336 - Assistance can slow experts down: measure the expertise-assistance interaction in interactive segmentation before assuming tools help everyone.

- **Problem:** Interactive tools are evaluated on average productivity, assuming universal benefit; for domain experts with fast manual routines, correction-based workflows may be slower and more error-inducing than unassisted annotation (verification overhead, anchoring) - the interaction between user expertise and assistance value is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: a crossed study (expert/novice x assisted/manual) will show a significant interaction - novices gain large speedups from assistance while experts gain little or lose time on their specialty content (their manual routines outpace correction workflows, and machine proposals anchor them toward accepting subtle errors they would not make manually) - so deployment policy should route assistance by user-task expertise, not blanket-mandate it.
- **Why important:** Hospitals and labeling firms are mandating assisted workflows on productivity claims measured on novices; the interaction term determines whether experts should be exempted.
- **Why possibly novel:** Expertise-assistance interaction measurement for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Timed crossed-design study (N=24, radiologists + trainees) on specialty content, measure speed, accuracy, and anchoring errors per cell.
- **Main risk:** Expert recruitment cost; single-domain results need replication before generalizing.
- **Mutated from:** W2-A-0188

### W2-A-0337 - Mask metrics don't predict task success: measure the mIoU-to-downstream correlation for grasping, measurement, and navigation consumers.

- **Problem:** Segmentation quality is assumed to transfer monotonically to downstream task success (grasp planning, volume measurement, obstacle avoidance), but different consumers weight different mask properties, and the metric-task correlation - the justification for the whole benchmark enterprise - is rarely measured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: across three instrumented downstream tasks, standard mask metrics predict task success only moderately (rank r 0.4-0.7) with large method-ranking disagreements - grasping cares about boundary normals at contact regions, measurement about signed area bias, navigation about worst-case misses - and per-task weighted metrics constructed from failure analysis predict success far better, demonstrating that 'better segmentation' is task-relative and benchmark rankings mislead consumers who take them at face value.
- **Why important:** Downstream users select models by benchmark rank; quantified rank-task disagreement would justify task-conditioned model selection and metric design.
- **Why possibly novel:** Multi-task metric-validity measurement for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Instrument simulated grasping + volume-measurement + navigation consumers over model-zoo outputs, correlate task success with metric families.
- **Main risk:** Simulated consumers may not represent physical ones; add one small real-robot validation leg.
- **Mutated from:** W2-A-0155

### W2-A-0338 - Panoptic unification tax: joint things+stuff training interferes - measure per-task gradient conflict and the interference cost against split models.

- **Problem:** Panoptic segmentation unified things and stuff on elegance grounds; whether unification HELPS each sub-task or taxes both (gradient conflict between instance-discrimination and region-classification objectives) at matched capacity has not been cleanly measured since unification became default.
- **Core hypothesis (falsifiable):** HYPOTHESIS: matched-capacity comparisons (joint panoptic vs separate things/stuff models vs shared-encoder-split-decoder) will show a measurable unification tax on at least one sub-task (predicted: stuff boundary quality suffers from instance-objective gradients), per-layer gradient-conflict metrics will localize the interference, and task-arithmetic analysis will show the two tasks want measurably different feature geometries in late layers - elegance has a quantifiable cost that deployment-focused users should know.
- **Why important:** Unified models are chosen by default; an itemized interference bill lets users decide when separation is worth the extra weights.
- **Why possibly novel:** Interference accounting for panoptic unification is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train the three configurations at matched capacity on COCO-panoptic/ADE, measure per-task deltas and layer-wise gradient conflict.
- **Main risk:** Capacity matching across configurations has degrees of freedom; sweep capacity to show robustness.

### W2-A-0339 - Is 3D really harder than 2D? Per-supervision-bit accounting suggests volumetric segmentation may be intrinsically EASIER than the field believes.

- **Problem:** 3D segmentation is treated as the harder problem (compute, memory, data scarcity), but per unit of supervision, 3D provides massive spatial-context redundancy (anatomy continuity constrains solutions); the information-normalized comparison - performance per supervision bit - has never been computed, leaving the field's difficulty intuition untested.
- **Core hypothesis (falsifiable):** HYPOTHESIS: normalizing by supervision information (labeled voxels, annotation time) rather than raw case counts, 3D models reach target accuracy with FEWER supervision bits than 2D models on matched anatomy (volumetric context does the missing supervision's work), so 3D's reputation for difficulty is an artifact of comparing per-case instead of per-bit - with the practical corollary that sparse 3D annotation (few slices per volume) dominates dense 2D annotation at fixed budget.
- **Why important:** Annotation-budget allocation between 2D and 3D protocols is a recurring real decision made under a possibly-inverted difficulty assumption.
- **Why possibly novel:** Information-normalized 2D-vs-3D difficulty accounting is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train 2D/3D models across supervision-bit ladders on isotropic datasets, compare bits-to-target-accuracy per formulation.
- **Main risk:** Defining supervision bits fairly across formulations is delicate; use annotation-time as the practical common currency.
- **Mutated from:** W2-A-0062

### W2-A-0340 - TTA is not a free lunch: test-time augmentation buys accuracy but degrades calibration and boundary sharpness - itemize the hidden bill.

- **Problem:** Test-time augmentation ensembling is deployed as pure upside, but averaging predictions across geometric views plausibly blurs boundaries (misaligned view predictions) and flattens confidence in ways that harm downstream consumers - the side effects are unitemized.
- **Core hypothesis (falsifiable):** HYPOTHESIS: TTA improves region metrics while measurably degrading boundary sharpness (view-misalignment blur, quantifiable as transition-width increase) and distorting calibration non-uniformly (overconfident where views agree by symmetry, underconfident on asymmetric structures), so TTA's net value is property- and consumer-dependent - positive for classification-like uses, negative for measurement and editing uses - and property-selective TTA (aggregate labels, not boundaries) captures the good without the bill.
- **Why important:** TTA is ubiquitous and unexamined; an itemized cost-benefit per output property immediately improves deployment choices.
- **Why possibly novel:** Property-resolved TTA side-effect accounting is UNVERIFIED - needs lit search.
- **Minimal experiment:** Measure per-property deltas (region, boundary width, calibration) under standard TTA across model zoo, validate the selective-TTA variant.
- **Main risk:** Effects may be small for well-aligned TTA implementations; quantify against alignment quality.

### W2-A-0341 - Prompt sensitivity may INCREASE with model scale on ambiguous objects: bigger promptable models represent more granularity hypotheses to flip between.

- **Problem:** Scale is assumed to buy robustness, including prompt robustness; but for genuinely ambiguous prompts (part-vs-whole), a richer model represents MORE valid alternatives, plausibly increasing output sensitivity to prompt nuance - the scale-ambiguity interaction has never been measured and its sign is genuinely unclear.
- **Core hypothesis (falsifiable):** HYPOTHESIS: across a promptable-model scale ladder, prompt-jitter sensitivity DECREASES with scale on unambiguous objects (standard robustness) but INCREASES or stays flat on ambiguous objects (more represented hypotheses = more flip destinations) - a sign-splitting interaction meaning scale changes the CHARACTER of instability rather than removing it, and prompt-robustness engineering must target ambiguity resolution, not model size.
- **Why important:** Corrects a scale-solves-it assumption before the ecosystem invests further, and dissects what robustness even means under genuine ambiguity.
- **Why possibly novel:** Scale-ambiguity interaction measurement for promptable models is UNVERIFIED - needs lit search.
- **Minimal experiment:** Measure jitter sensitivity across SAM variants and mini-SAM scale series, stratified by ambiguity (multi-annotator objects vs consensus objects).
- **Main risk:** Scale ladders confound data and architecture changes; the controlled mini-SAM series is the clean leg.
- **Mutated from:** W2-A-0001

### W2-A-0342 - Models as arbiters of human disagreement: when annotators disagree, does the model side with the eventually-verifiable answer?

- **Problem:** Humans are the gold standard, but on ambiguous cases humans disagree and someone is wrong; where external verification exists (pathology outcomes, multi-view geometry, higher-resolution follow-up imaging), one can ask whether model predictions on disputed pixels align with the verified answer more often than the average human - a carefully-scoped 'model as arbiter' question nobody has quantified.
- **Core hypothesis (falsifiable):** HYPOTHESIS: on disagreement pixels with external verification, strong models side with the verified answer at rates above the average individual annotator for texture- and intensity-driven disputes (models integrate more measurement evidence) but below for knowledge-driven disputes (anatomical plausibility, rare-entity recognition) - a two-regime arbiter profile that defines exactly when model opinion should be weighted into consensus protocols and when it must be ignored.
- **Why important:** Label-fusion protocols currently ignore model opinion or use it circularly; a verification-anchored arbiter profile would put adjudication weighting on evidence.
- **Why possibly novel:** Verification-anchored arbiter analysis is UNVERIFIED - needs lit search.
- **Minimal experiment:** Assemble disputed-pixel sets with external verification (multi-view scenes, pathology-confirmed lesions), compare model vs individual-human agreement with verified answers.
- **Main risk:** Verification-available cases are a biased sample of disputes; state scope honestly.
- **Mutated from:** W2-A-0075

### W2-A-0343 - Relational grounding gap: models segment 'the cup' but fail 'the handle of the second cup from the left' - compositional queries expose a missing capability layer.

- **Problem:** Segmentation is treated as a solved perception primitive to build on, but downstream systems need relationally-specified targets (ordinal, possessive, spatial-relative references); whether current promptable/language-grounded segmenters handle compositional specifications - versus bag-of-words matching - is untested systematically.
- **Core hypothesis (falsifiable):** HYPOTHESIS: on a controlled compositional-query benchmark (ordinals, relations, part-of-instance chains), current language-grounded segmenters perform near bag-of-words baselines (they match nouns and ignore structure - verifiable by permutation tests: scrambled queries score similarly), failure is uniform across model scale (structure, not capacity), and humans find the same queries trivial - isolating a discrete missing capability layer between perception and language rather than a smooth performance gap.
- **Why important:** Robotics and AR need relational grounding daily; establishing that the capability is absent (not just weak) redirects effort from scaling to structural integration.
- **Why possibly novel:** Permutation-controlled compositional segmentation benchmarking is UNVERIFIED - needs lit search (referring-expression datasets are KNOWN but conflate cues).
- **Minimal experiment:** Build controlled query benchmark with scrambling controls on synthetic and real crowded scenes, evaluate grounded-segmentation model families.
- **Main risk:** Synthetic query distributions may miss natural relational usage; mine real instruction data for ecological queries too.

### W2-A-0344 - Which realism factors matter is task-relative: the same synthetic data ranks differently for segmentation vs depth vs detection - test the task-relativity of the sim2real gap.

- **Problem:** Synthetic-data realism is discussed as a scalar (more real = better transfer), but different tasks consume different image properties, so realism factors (lighting, texture, geometry, layout) should matter differently per task - if true, 'realistic enough' has no task-independent meaning and shared synthetic pipelines are mis-specified for someone.
- **Core hypothesis (falsifiable):** HYPOTHESIS: factorial realism ablations evaluated across three tasks (segmentation, depth, detection) on the same scenes will show strong task-factor interactions - segmentation transfer depends most on boundary-adjacent material/lighting fidelity, depth on geometry/shading consistency, detection on layout statistics - with factor rankings reordering across tasks, proving realism budgets must be task-allocated and generic 'photorealism' spends rendering compute on the wrong factors for most consumers.
- **Why important:** Synthetic-data pipelines serve multiple downstream teams from one render budget; task-relative factor maps would restructure how that budget is spent.
- **Why possibly novel:** Cross-task factorial realism comparison is UNVERIFIED - needs lit search.
- **Minimal experiment:** Render factor-ablated scene sets, train per task per cell, compare factor-importance rankings across tasks.
- **Main risk:** Render-pipeline confounds across factors; use one engine with modular factor toggles.
- **Mutated from:** W2-A-0227

### W2-A-0345 - Segmentation models are secret amodal completers: measure how often models segment plausibly-present-but-invisible object parts, and whether it helps or hurts.

- **Problem:** Models are trained on modal (visible-region) masks, but network priors may complete occluded parts anyway (predicting mask where the object plausibly continues behind an occluder); whether this happens, how often, and whether the amodal tendency helps (robustness) or hurts (metric penalty, false extents) is uncharacterized.
- **Core hypothesis (falsifiable):** HYPOTHESIS: on curated occlusion scenes, standard modal-trained models predict into occluded regions at measurable rates that grow with occluder thinness and object-shape predictability (an emergent amodal prior), the tendency is penalized by modal metrics but correlates POSITIVELY with downstream tracking robustness (completed masks survive occlusions better) - an emergent capability being actively trained away by modal supervision, quantified for the first time.
- **Why important:** Reveals a hidden tension between benchmark optimization and downstream utility, and grounds the amodal-vs-modal supervision choice in measurement.
- **Why possibly novel:** Emergent-amodal-tendency measurement in modal-trained models is UNVERIFIED - needs lit search (deliberate amodal segmentation is a KNOWN subfield).
- **Minimal experiment:** Curate occlusion scenes with amodal GT, measure modal models' occluded-region predictions, correlate amodal tendency with tracking robustness.
- **Main risk:** Amodal GT is expensive; use synthetic occlusion composites for scale plus real subsets for validation.
- **Mutated from:** W2-A-0041

### W2-A-0346 - The augmentation-invariance tax: aggressive augmentation buys robustness by destroying exactly the cues needed for fine-grained boundary decisions - measure the property-level tradeoff.

- **Problem:** Strong augmentation (color jitter, blur, geometric distortion) is universally applied for robustness, but each augmentation teaches an invariance that discards a cue - and some discarded cues (subtle color transitions, texture gradients) are precisely what fine boundary and material segmentation need; the per-property tax of each augmentation family is unmeasured.
- **Core hypothesis (falsifiable):** HYPOTHESIS: augmentation-family ablations will show a measurable tradeoff structure - color-jitter improves cross-domain region accuracy while degrading material-boundary and translucency segmentation (color-cue destruction), blur augmentation degrades thin-structure recall - with the tax concentrated exactly on the hard classes this catalog cares about (transparent, camouflaged, thin), implying hard-class pipelines need augmentation policies OPPOSITE to the community default.
- **Why important:** Augmentation defaults propagate through every training recipe; property-level tax tables would let hard-class practitioners stop importing policies that sabotage their targets.
- **Why possibly novel:** Property-resolved augmentation-tax accounting is UNVERIFIED - needs lit search.
- **Minimal experiment:** Train augmentation-family ablation grids, evaluate on hard-class benchmarks (transparency, camouflage, thin structures) alongside standard ones, tabulate signed effects.
- **Main risk:** Interactions between augmentation families complicate attribution; factorial design with interaction terms.

### W2-A-0347 - Frozen-feature Pareto myth: fine-tuning the encoder may WORSEN out-of-domain dense performance while improving in-domain - the forgetting frontier nobody plots.

- **Problem:** Fine-tuning versus freezing is decided by in-domain validation alone, but encoder updates plausibly destroy the foundation's broad robustness (catastrophic forgetting of dense-relevant generality); the in-domain-gain versus out-of-domain-loss frontier for dense tasks is never plotted, so practitioners cannot see what fine-tuning costs them.
- **Core hypothesis (falsifiable):** HYPOTHESIS: plotting the tradeoff across tuning intensities (frozen, LoRA-scale, full) will show full fine-tuning sits far off the Pareto frontier for deployment profiles including moderate shift (its in-domain gains are dwarfed by out-of-domain losses), light-touch tuning dominates most realistic mixtures, and the frontier position is predictable from tuning-data diversity - making 'how hard to fine-tune' a computable deployment decision instead of a habit.
- **Why important:** Fine-tuning intensity is among the most common practical decisions in applied segmentation, currently made blind to its robustness bill.
- **Why possibly novel:** Dense-task forgetting-frontier mapping is UNVERIFIED - needs lit search (NLP forgetting studies are KNOWN).
- **Minimal experiment:** Tune across intensity ladders on 3 target datasets, evaluate in-domain plus shifted suites, plot frontiers and validate the diversity predictor.
- **Main risk:** Frontier depends on the foundation's initial robustness; replicate across 2 foundations.
- **Mutated from:** W2-A-0332

### W2-A-0348 - Order-of-magnitude compute asymmetry: inference-time search (prompt search, multi-scale, self-consistency) is undervalued versus training-time scale in segmentation - measure the exchange rate.

- **Problem:** The field spends compute overwhelmingly at training time, while inference-time compute (searching prompts, scales, and self-consistency checks per image) is barely explored for dense prediction - the accuracy-per-inference-FLOP exchange rate between the two spending modes is unknown, though LLM experience (KNOWN: inference-time scaling works there) suggests it may favor inference for hard inputs.
- **Core hypothesis (falsifiable):** HYPOTHESIS: on the hardest decile of inputs, inference-time search over a frozen model (prompt ensembles, scale search, cycle-consistency selection) buys accuracy that would require 10x+ training-scale increase to match (a strongly input-conditional exchange rate), while on easy inputs it buys nothing - so adaptive inference-compute allocation (spend on hard inputs, detected label-free) dominates uniform training-scale investment for deployment mixtures with difficulty tails.
- **Why important:** A favorable measured exchange rate would legitimize an entire underexplored axis of dense-prediction improvement that requires no retraining.
- **Why possibly novel:** Inference-vs-training compute exchange measurement for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Implement inference-search suite over frozen models, measure accuracy-vs-FLOPs curves against training-scale ladders, stratify by input difficulty.
- **Main risk:** Search needs a selection signal without GT; cycle-consistency and agreement signals must be validated first.
- **Mutated from:** W2-A-0141

### W2-A-0349 - Human boundary conventions encode function, not photometry: models place boundaries where image evidence says, humans where object USE says - measure the systematic divergence.

- **Problem:** Human annotators draw boundaries informed by function (the handle 'belongs' to the mug even where shadow obscures the junction; the rider is separate from the bike at the functional interface), while models follow photometric evidence; this convention-versus-evidence divergence has never been isolated as a measurable, systematic offset distinct from random error.
- **Core hypothesis (falsifiable):** HYPOTHESIS: at functional part junctions and object-accessory interfaces, human-model boundary disagreement is systematically structured (humans cut at functional joints, models at photometric edges - a reproducible signed offset per junction type), the divergence survives across model families (it is supervision-philosophy-deep, not architecture-specific), and junction-type-aware evaluation separates this convention mismatch from genuine model error - revealing that part of the measured 'boundary error' is actually an unresolved disagreement about what boundaries MEAN.
- **Why important:** Robotics consumers need functional boundaries (grasp the handle), photometric consumers need evidence boundaries (matting); making the divergence explicit lets datasets and metrics choose deliberately.
- **Why possibly novel:** Functional-vs-photometric boundary divergence measurement is UNVERIFIED - needs lit search.
- **Minimal experiment:** Annotate junction taxonomy on part-rich datasets, measure signed human-model offsets per junction type across model zoo.
- **Main risk:** Junction taxonomy design shapes findings; ground it in affordance literature and multiple annotator pools.

### W2-A-0350 - Silent class collapse under fine-tuning: adapting a segmenter to a target dataset quietly deletes its competence on classes the target lacks - measure the deletion curve.

- **Problem:** Fine-tuning on datasets with reduced class vocabularies is universal practice (adapt COCO-pretrained to a 5-class industrial task); the fate of the other classes' competence - deleted, dormant, or recoverable - determines model reusability and is never measured, just assumed lost or assumed fine.
- **Core hypothesis (falsifiable):** HYPOTHESIS: off-target class competence decays during fine-tuning along measurable curves (fast for classes visually similar to target negatives - they become 'background' - slow for dissimilar ones), the decay is largely RECOVERABLE with tiny rehearsal (competence is dormant, not deleted, verifiable by cheap re-probing), and a rehearsal budget of a few percent preserves the full vocabulary at negligible target-task cost - fine-tuning's destructiveness is real but cheaply preventable, and the deletion-similarity law predicts which classes die first.
- **Why important:** Organizations maintain fleets of fine-tuned variants because they assume specialization destroys generality; if preservation is nearly free, model-fleet economics change.
- **Why possibly novel:** Deletion-curve measurement with dormancy testing for dense models is UNVERIFIED - needs lit search.
- **Minimal experiment:** Fine-tune across target tasks, track off-target class probes over training, test rehearsal-fraction ladders for preservation.
- **Main risk:** Interaction with model scale (bigger models may resist deletion); include scale as a factor.
- **Mutated from:** W2-A-0347

### W2-A-0351 - The two-annotator myth: pairwise agreement statistics systematically underestimate ambiguity because disagreement is multi-modal, not binary - remeasure with dense rater panels.

- **Problem:** Dataset quality is certified with two-annotator agreement (kappa, pairwise IoU), implicitly modeling disagreement as noise around one truth; if ambiguous regions have MULTIPLE stable interpretations (modes), pairwise statistics conflate mode-diversity with noise and underestimate true ambiguity in a structured way that panel-size experiments can expose.
- **Core hypothesis (falsifiable):** HYPOTHESIS: scaling rater panels (2 to 10+ annotators per item) on ambiguity-heavy content will show disagreement statistics do NOT converge as noise models predict - instead distinct interpretation modes stabilize (2-4 modes per ambiguous region, each internally consistent), pairwise-agreement-certified datasets contain substantial undetected multi-modality, and mode-aware quality measures reorder dataset-quality rankings - the field's standard quality certification instrument is structurally blind to the most important kind of label uncertainty.
- **Why important:** Every dataset paper reports pairwise agreement as quality evidence; demonstrating its structural blindness with panel data would upgrade certification practice field-wide.
- **Why possibly novel:** Panel-scaling mode-discovery analysis for segmentation is UNVERIFIED - needs lit search.
- **Minimal experiment:** Collect 10-rater panels on 300 ambiguity-heavy items, fit mode structure vs noise models, compare pairwise-statistic predictions against panel reality.
- **Main risk:** Panel cost; 300 items suffice for the structural claim if items are sampled to span ambiguity types.
- **Mutated from:** W2-A-0051

### W2-A-0352 - Segmentation-free measurement: for many 'segmentation' applications (area, count, growth-rate), direct regression from images beats segment-then-measure - test when the mask is an unnecessary middleman.

- **Problem:** Applications often want scalar quantities (lesion volume, crop coverage, cell count) and obtain them via segmentation as an intermediate; the mask may be an information bottleneck and error amplifier (boundary errors compound into measurement bias), but the direct-regression alternative is rarely benchmarked because segmentation is assumed to be the principled route.
- **Core hypothesis (falsifiable):** HYPOTHESIS: for scalar-output applications, direct regression models trained on the scalars (bypassing masks entirely) match or beat segment-then-measure pipelines at equal supervision cost when boundary ambiguity is high (the mask forces premature hard decisions that regression avoids), while segmentation-mediated pipelines win when spatial auditability or multi-purpose reuse is needed - a decision rule mapping application properties to the right paradigm, deflating segmentation's assumed universality as a middleware layer.
- **Why important:** If a large application class does not need masks, the field's effort allocation and these applications' accuracy both improve - an unasked question with immediate practical stakes.
- **Why possibly novel:** Systematic mask-vs-direct benchmarking across measurement applications is UNVERIFIED - needs lit search.
- **Minimal experiment:** On three measurement tasks (lesion volume, vegetation coverage, cell count) with GT scalars, compare direct regression vs segment-then-measure at matched supervision budgets.
- **Main risk:** Direct regression loses auditability (a real deployment requirement); frame the decision rule to include it as a factor, not a footnote.

