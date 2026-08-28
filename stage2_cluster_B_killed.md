# Stage 2 — Cluster B Killed Ideas

**280 ideas killed** (of 366). Kill classes: likely published, module stacking / apply-X-with-no-mechanism, infeasible, vague/narrow novelty, redundant with a kept sibling, and near-misses cut for portfolio balance ("near-miss (painful)" marks ideas that were competitive and may be revisited if the budget widens).

## Medical Image Segmentation (core) (22 killed)

- **B-0001** (composite 6.0): near-miss; spacing conditioning plausibly absorbed by heavy resampling augmentation; metadata-conditioning family thin
- **B-0005** (composite 5.9): near-miss; principled but label-smoothing-adjacent; contour GT precision may cap the signal
- **B-0006** (composite 5.2): narrow contribution; seam variance likely small except tiny lesions
- **B-0008** (composite 6.0): near-miss; metadata conditioning partially explored; shuffled-token control is nice but core is thin
- **B-0009** (composite 5.9): INR decoders for segmentation increasingly explored; through-plane claim decent but crowded space
- **B-0010** (composite 4.9): likely published: segmentation QC / per-case error prediction (RCA and QC-head literature) is crowded
- **B-0011** (composite 5.9): near-miss; metal-artifact simulation exists in MAR literature; needs new annotated implant test set
- **B-0012** (composite 5.8): redundant: protocol/convention-conditioning theme retained via B-0159 and B-0112 (stronger framings)
- **B-0013** (composite 4.2): likely published: paired-timepoint new-lesion/change segmentation is an established challenge task
- **B-0015** (composite 4.6): module-flavored; differentiable cropping explored in 2D; memory-heavy joint training
- **B-0016** (composite 6.1): near-miss; uncertain-band packaging of existing uncertainty tools; workflow angle nice but derivative
- **B-0018** (composite 5.8): near-miss; propose-and-prune for airway/vessel trees partially explored
- **B-0019** (composite 6.4): near-miss (painful); cheap decisive scale-dependence question for topological losses; cut on section balance
- **B-0020** (composite 4.8): shape-prior space crowded; VQ packaging is module novelty; fails exactly on pathological shape outliers
- **B-0021** (composite 4.9): likely published: joint recon-seg explored; k-space+labels public overlap scarce
- **B-0022** (composite 5.6): near-miss; learnable normalization crowded; landmark-anchoring circularity risk
- **B-0024** (composite 4.6): likely published: blob-loss / lesion-wise instance objectives exist; frontier mapping is incremental
- **B-0025** (composite 4.4): likely published: temporal/cyclic consistency for cine cardiac segmentation well explored
- **B-0026** (composite 5.5): near-miss; niche; simulated-vs-real motion gap is the load-bearing risk
- **B-0028** (composite 6.4): near-miss (painful); cheap size-conditional calibration; calibration theme trimmed at portfolio level
- **B-0029** (composite 4.0): likely published: missing-modality robustness (dropout/conditioning) heavily explored (HeMIS lineage)
- **B-0030** (composite 6.0): near-miss; atlas-coordinate auxiliary tasks partially explored; positional-prior theme killed as family

## Medical Vision Foundation Models (22 killed)

- **B-0031** (composite 4.5): likely published: content/attention-guided masking MIM variants exist including medical instantiations
- **B-0033** (composite 4.6): engineering overhead likely eats gains; 2D superpixel tokenization precedent; batching pain
- **B-0034** (composite 6.2): near-miss; HU-faithful physics encoding is a decent mechanism; cut on section balance
- **B-0036** (composite 5.8): near-miss; retrieval-augmented segmentation emerging elsewhere; retrieval-leak confound
- **B-0039** (composite 5.0): pseudo-rehearsal crowded in continual learning; incremental transplant to medical FMs
- **B-0041** (composite 5.7): near-miss; federated modality-expert splitting; simulation-only evidence; heavy
- **B-0042** (composite 6.2): near-miss; frequency-response fingerprint is a nice diagnostic; cut on balance
- **B-0043** (composite 4.9): module: ToMe-style adaptive token merging port to 3D
- **B-0044** (composite 6.4): near-miss (painful); acquisition-sensitivity fingerprints valuable; overlaps kept audits B-0095/B-0327
- **B-0045** (composite 6.2): near-miss; factorial bias attribution; demographic-scanner confounding in available data
- **B-0046** (composite 6.2): near-miss; ontology-graph open-vocab with proximity-scaling claim; crowded open-vocab space
- **B-0047** (composite 4.7): continual SSL with generative replay crowded; 3D replay quality doubtful
- **B-0048** (composite 6.4): near-miss; distillation-residual as instrument for intrinsic 3D value; capacity confound risk
- **B-0049** (composite 6.4): near-miss; nearly-free anatomical-topology probe; model-scale confound
- **B-0051** (composite 6.3): near-miss; registration-vs-MIM pretext twin study; pair-mining collapse risk
- **B-0052** (composite 6.3): near-miss; test-time compute scaling for dense prediction is timely; output-diversity prerequisite risk
- **B-0053** (composite 5.9): near-miss; emergent shared anatomical latent; boundary precision doubtful without paired data
- **B-0054** (composite 5.9): near-miss; resolution/scale transfer partially studied for ViTs; attribution claim moderate
- **B-0055** (composite 5.4): redundant with B-0030 positional-prior family (killed); estimation fails on unusual scans
- **B-0056** (composite 6.4): near-miss; free QC from MIM reconstruction error; texture-not-error correlation risk
- **B-0059** (composite 4.9): module: cross-scale consistency loss stacking
- **B-0060** (composite 4.4): likely published: positional/anatomical contrastive positives explored (PCL-style)

## Smoke/Fire/Transparent/Ambiguous Segmentation (22 killed)

- **B-0063** (composite 6.3): near-miss; turbulence-spectra cue cheap to test; framerate/resolution limits at range
- **B-0064** (composite 4.9): likely published core: flicker-frequency fire detection is classic handcrafted-era work; modern update incremental
- **B-0065** (composite 5.5): polarization glass segmentation datasets/methods exist; context-ablation design is the only new part
- **B-0066** (composite 5.9): near-miss; depth-failure-as-weak-label noted in prior glass work; dark/distant-surface confounders
- **B-0067** (composite 5.8): near-miss; refraction warp-field representation; undistorted-background estimation ill-posed in the wild
- **B-0068** (composite 6.0): near-miss; two-layer decomposition API reframing; benchmark-building heavy
- **B-0070** (composite 6.0): near-miss; multi-rater ambiguity for fuzzy objects; annotation cost; theme kept via B-0003
- **B-0071** (composite 6.2): near-miss; rendering-fidelity factorial for synthetic smoke; fidelity-science theme partly covered by B-0212/B-0222
- **B-0072** (composite 6.3): near-miss; steam-vs-smoke temporal benchmark practical; capture effort; temporal theme kept via B-0090
- **B-0073** (composite 6.1): near-miss; overlaps B-0085 (kept) static-camera background exploitation; night airlight fragility
- **B-0075** (composite 5.9): near-miss; fiducial-derived optical-depth labels; field instrumentation cost; sparse sightlines
- **B-0076** (composite 6.3): near-miss; plume-physics post-hoc rescoring; terrain distortion breaks parametric families
- **B-0077** (composite 5.6): cross-modal distillation is a standard recipe; capture campaign required; thermal-to-RGB instance moderate
- **B-0079** (composite 5.4): redundant with B-0078 (kept); raw-domain vision partially explored; cross-sensor raw generalization poor
- **B-0080** (composite 5.9): near-miss; highlight-parallax self-supervised glass cue; textureless-background failure
- **B-0081** (composite 6.0): near-miss; transmitted-vs-reflected three-way decomposition; reflection-removal adjacency
- **B-0082** (composite 5.8): near-miss; 3D media recovery needs lab multi-camera setup; slow optimization needs amortized variant
- **B-0083** (composite 6.4): near-miss (painful); GGO-as-smoke density-regression bridge; inspiration/scanner confounds; opacity theme kept via B-0061
- **B-0086** (composite 6.4): near-miss; evidence-type taxonomy meta-benchmark; type-purity and domain confounds
- **B-0087** (composite 6.3): near-miss; nested core/extent annotation protocol; annotation-protocol science kept via B-0269
- **B-0088** (composite 5.9): near-miss; multi-membership transparent instances; niche; dirt/liquids may dominate difficulty
- **B-0089** (composite 5.6): near-miss; multi-illumination identical-plume capture physically tricky

## Domain Adaptation & Domain Shift (22 killed)

- **B-0092** (composite 4.9): likely published: entropy-min collapse under small batch/imbalance studied in stable-TTA lineage
- **B-0094** (composite 4.2): likely published: stochastic restoration against continual-TTA drift is the CoTTA mechanism itself
- **B-0097** (composite 5.8): near-miss; windowed frequency alignment is a fix-module on the Fourier-DA family; diagnosis half is thin alone
- **B-0098** (composite 6.0): redundant with B-0096 (kept); geometric-vs-appearance separation subsumed by the factorial locus law
- **B-0099** (composite 4.7): likely published: boundary-band pseudo-label masking is an established self-training trick
- **B-0100** (composite 5.2): open-set DA crowded; segmentation instantiation incremental without a new mechanism
- **B-0101** (composite 4.3): likely published: region-level active DA for segmentation is established (impurity-uncertainty selection)
- **B-0102** (composite 6.1): near-miss; per-case adapt-or-not meter overlaps B-0091 surrogate-signal machinery; kept the more general framing
- **B-0104** (composite 5.8): near-miss; lesion erasure in translation noted in prior medical DA work; contrastive fix is module-flavored
- **B-0106** (composite 5.9): near-miss; dense label-shift EM correction is a sensible port but port nonetheless
- **B-0108** (composite 4.9): module: shape-prior regularizer bolted onto TTA; prior-model quality becomes the hidden variable
- **B-0109** (composite 4.9): module: prompt-restricted TTA is a known parameter-subset choice in the VPT/TTA intersection
- **B-0110** (composite 5.8): near-miss; domain versioning is sound systems engineering but thin as a research claim
- **B-0111** (composite 5.5): module: multi-depth OT feature alignment; heavier machinery without a new question
- **B-0113** (composite 5.9): near-miss; contrast-inversion focus is sharp but sign-invariant edge features are a narrow fix
- **B-0114** (composite 5.8): near-miss; physical weather-parameter conditioning partially explored in adverse-weather driving literature
- **B-0115** (composite 5.7): near-miss; source sketches overlap dataset-distillation and source-free DA exemplar lines; privacy claim needs audit of its own
- **B-0116** (composite 5.9): near-miss; input-space adaptation with frozen certified model is practical but visual-prompt reprogramming adjacent
- **B-0117** (composite 4.9): curriculum self-training UDA explored; easy-to-hard ordering is an established ingredient
- **B-0118** (composite 5.4): near-miss; per-case source routing sensible; multi-source DA space crowded and gains historically small
- **B-0119** (composite 6.1): near-miss; session-level learning from clicks folded into interactive-editing theme kept via B-0027
- **B-0120** (composite 6.2): near-miss; sealed-harness infra heavy; audit core kept via protected B-0107

## Few-shot / Zero-shot Segmentation (22 killed)

- **B-0122** (composite 4.9): module: orthogonal-subspace allocation; feature-geometry surgery without a scientific question
- **B-0125** (composite 4.3): likely published: multi-prototype / prototype-mixture FSS is established
- **B-0126** (composite 4.9): module: test-time geometric alignment block before correlation
- **B-0127** (composite 4.9): near-miss; negative supports partially explored via background prototypes; contrastive packaging thin
- **B-0129** (composite 6.3): likely published in fast-moving space: training-free correspondence baselines (DINO-feature matching) already strong
- **B-0130** (composite 4.9): module: null-space update port from continual-learning classification
- **B-0132** (composite 6.0): near-miss; retrieval + non-parametric decoding is a reasonable fix but method-first; saturation diagnosis is the interesting half
- **B-0134** (composite 6.0): near-miss; one-positive-pixel regime overlaps point-supervision literature; priors do the heavy lifting
- **B-0135** (composite 6.5): near-miss (painful); registration-vs-FSS decision rule valuable; classical-baseline audit theme trimmed at portfolio level
- **B-0136** (composite 4.4): likely published: diffusion-based support/data augmentation for few-shot tasks heavily explored
- **B-0137** (composite 4.9): module: mask-preserving support restyling; style-transfer trick at test time
- **B-0138** (composite 5.9): near-miss; hierarchical-fallback output is good UX but hierarchy-aware segmentation partially explored
- **B-0139** (composite 6.1): near-miss; transferable open-vocab thresholds real pain point; calibration family trimmed at portfolio level
- **B-0140** (composite 5.8): near-miss; ambiguity-aware referring segmentation being absorbed by interactive VLM work
- **B-0141** (composite 5.6): near-miss; part-based transfer substrate partially explored in part-aware FSS
- **B-0142** (composite 4.9): module: scale-searched matching pyramid; explicit scale posterior is a nice touch not a paper
- **B-0144** (composite 4.9): module: prototype whitening/orthogonalization for multi-way interference
- **B-0146** (composite 6.4): near-miss (painful); deployment-realistic episode construction; ranking-stability theme partly covered by B-0124
- **B-0147** (composite 5.8): near-miss; continual FSS enrolment is a real setting but incremental-learning machinery dominates
- **B-0148** (composite 6.0): near-miss; support-annotation cost frontier useful; annotation-economics theme kept via Section 9 picks
- **B-0149** (composite 5.8): near-miss; unsupervised pseudo-episode pretraining adjacent to existing self-supervised FSS work
- **B-0150** (composite 6.5): near-miss (painful); support-sufficiency prediction is fresh but folded under selective-prediction family; B-0124 covers the leverage

## Prompt Learning (24 killed)

- **B-0152** (composite 4.3): likely published: text-manifold anchoring of prompts is established (knowledge-guided prompt regularization)
- **B-0153** (composite 4.9): module: learned point-placement agent for promptable segmenters; auto-prompting space crowded
- **B-0155** (composite 5.9): near-miss; metadata-to-prompt mapping; metadata-conditioning family thin; convention angle kept via B-0159
- **B-0156** (composite 4.3): likely published: prompt pools with key-based retrieval/routing is the L2P recipe
- **B-0157** (composite 5.6): near-miss; negative-prompt subtraction geometry fragile; embedding arithmetic assumptions unproven
- **B-0158** (composite 4.9): pipeline: coarse-to-fine prompt chaining; error-propagation study bolted onto a system
- **B-0160** (composite 4.9): near-miss; TPT objective swap; test-time prompt tuning variants crowded
- **B-0161** (composite 4.9): module: prompt distillation/compression without a scientific question
- **B-0162** (composite 6.4): near-miss (painful); prompt universality across backbones studied in NLP; dense-vision port moderate
- **B-0163** (composite 4.3): likely published: instance-conditional prompt generation is the CoCoOp recipe
- **B-0165** (composite 6.1): near-miss; PEFT-vs-full-FT robustness compared in classification; dense version incremental
- **B-0166** (composite 4.8): narrow: training-order interference curriculum; effect sizes likely small and dataset-specific
- **B-0168** (composite 5.9): near-miss; pixel-vs-token prompt expressivity map; visual-prompt comparisons partially exist
- **B-0169** (composite 4.9): incremental: prompt-ensembling systematization; variance decomposition is bookkeeping not discovery
- **B-0170** (composite 4.3): likely published: prompt-pool domain-incremental learning is the L2P/S-Prompts recipe
- **B-0171** (composite 6.0): redundant with B-0038 (kept); injection-depth law covered by the adapter-placement factorial
- **B-0172** (composite 5.8): near-miss; prompt-length sizing rule useful; scaling-law budget spent on B-0032/B-0037
- **B-0173** (composite 4.8): near-miss; gradient-free discrete prompt search explored in NLP; dense port with weak mechanism
- **B-0174** (composite 5.7): near-miss; attribute-conjunction compositionality crowded in VLM eval space; prompt algebra fragile
- **B-0175** (composite 5.1): likely published: prompt-switchable multi-task dense models are the visual-generalist recipe (Painter-style)
- **B-0176** (composite 4.9): module: spatial+semantic prompt combination is a feature not a finding
- **B-0178** (composite 6.6): near-miss (painful); cross-lingual dense-prompt gap real and understudied; niche venue risk; cut on balance
- **B-0179** (composite 4.8): likely published-adjacent: federated prompt personalization explored; interpretability add-on thin
- **B-0180** (composite 4.9): crowded: self-refinement/self-critique loops; stopping criterion does not rescue novelty

## Weak / Semi / Self-supervised Learning (23 killed)

- **B-0181** (composite 5.8): near-miss; open-set SSL contamination studied in classification; seg port with dual-filter module
- **B-0183** (composite 6.3): near-miss; augmentation-validity audit overlaps protected B-0007 pipeline-bug family; suite publication is service not science
- **B-0184** (composite 4.3): likely published: adaptive per-class thresholds are the FlexMatch/DARS recipe
- **B-0185** (composite 5.5): near-miss; feature-vs-output consistency comparison; useful but incremental controlled study
- **B-0186** (composite 6.5): near-miss (painful); statistical no-worse-than-supervised certificate valuable; theory-heavy and safe-SSL adjacent
- **B-0187** (composite 5.4): likely published-adjacent: gaze-supervised medical AI has datasets and methods; calibration model is incremental delta
- **B-0188** (composite 6.0): infeasible as specified: synchronized dictation-audio + scroll-log data essentially unobtainable outside one health system
- **B-0190** (composite 4.7): likely published: point/centroid-supervised lesion segmentation well explored
- **B-0191** (composite 5.8): near-miss; PU formulation of partial annotation partially explored in detection/seg
- **B-0192** (composite 4.9): near-miss; sparse-slice + registration completion is an established annotation-saving recipe
- **B-0194** (composite 4.8): near-miss; gated temporal propagation is an established weak-label recipe with a new gate
- **B-0195** (composite 5.9): near-miss; unlabeled-pool valuation adjacent to data-valuation literature; curation theme kept via B-0057
- **B-0198** (composite 4.9): module: distribution-aligned crop sampling; sampling trick
- **B-0199** (composite 5.7): near-miss; self-training stopping criterion practical but thin as a paper
- **B-0200** (composite 6.2): near-miss; soft-vs-hard pseudo-label isolation folded into kept factorial B-0207
- **B-0202** (composite 6.0): near-miss; single-atlas + self-training honest baseline; classical-baseline audit theme trimmed at portfolio level
- **B-0203** (composite 5.1): likely published: counterfactual normal-appearance comparison is the anomaly-detection playbook
- **B-0204** (composite 5.9): near-miss; uncertainty-directed boundary annotation; annotation-interface theme kept via Section 9 picks
- **B-0205** (composite 5.2): likely published-adjacent: ViT patch-grid artifacts and sub-patch feature upsampling actively studied
- **B-0206** (composite 6.0): near-miss; physics-based consistency perturbations; physics family kept via B-0105/B-0193
- **B-0208** (composite 6.4): near-miss (painful); value-per-second of verification vs annotation; annotation-economics budget spent in Section 9
- **B-0209** (composite 6.0): redundant with B-0014 (kept); longitudinal-archive free signal already represented
- **B-0210** (composite 6.1): near-miss; when-SSL-stops-paying law partially covered by existing budget studies plus protected B-0196

## Synthetic Data (23 killed)

- **B-0211** (composite 6.0): near-miss; alignment filtering of diffusion masks noted in recent synthetic-seg pipelines
- **B-0215** (composite 5.9): near-miss; label-first synthesis extends SynthSeg lineage; lesion instantiation partially explored
- **B-0216** (composite 6.6): near-miss (painful); synthetic-release leakage audit strong but privacy-audit budget spent on kept B-0040
- **B-0217** (composite 6.1): near-miss; randomization-vs-realism frontier partially mapped in sim2real literature
- **B-0218** (composite 6.3): near-miss (painful); pipeline-placement factorial; synthetic-economics budget spent on B-0213
- **B-0219** (composite 6.6): near-miss (painful); counterfactual same-anatomy pairs partially explored in causal medical augmentation
- **B-0220** (composite 5.9): near-miss; procedural tubular pretraining explored in vessel-synthesis literature
- **B-0221** (composite 4.9): module: error-steered hard-negative generation; adversarial-curriculum packaging
- **B-0224** (composite 5.2): likely published: DP-synthetic medical imaging utility frontiers actively studied
- **B-0225** (composite 4.9): narrow: minimum replay fidelity for continual seg; continual-learning machinery dominates
- **B-0226** (composite 6.1): near-miss; copy-paste harmonization factorial; factorial budget spent on B-0207/B-0197
- **B-0227** (composite 5.9): redundant with B-0214 (kept); per-class utility prediction is a corollary of the utility metric
- **B-0228** (composite 5.1): likely published: CT-to-ultrasound physics simulation for training explored
- **B-0229** (composite 5.8): near-miss; inter-domain interpolation adjacent to style-mixing domain generalization
- **B-0231** (composite 5.3): likely published-adjacent: tail-targeted generation for long-tail explored; per-class accounting incremental
- **B-0232** (composite 5.9): likely published-adjacent: zero-real-data pretraining (formula-driven/SynthSeg lineage) plus FM-scale compute burden
- **B-0233** (composite 6.0): near-miss; qMRI-based contrast simulation partially explored in physics-informed MR augmentation
- **B-0234** (composite 4.3): likely published: depth-aware fog compositing is the Foggy-Cityscapes recipe
- **B-0236** (composite 6.1): redundant with B-0213 (kept); synthetic scaling exponent folded into the exchange-rate study
- **B-0237** (composite 4.9): module: distance-transform conditioning; representation tweak
- **B-0238** (composite 6.0): redundant with B-0131/B-0096 (kept); appearance-vs-content decomposition family already funded
- **B-0239** (composite 5.6): near-miss; closed-loop synthesis dynamics; mode-collapse risk is the finding and the flaw
- **B-0240** (composite 6.4): near-miss (painful); stress-test validity meta-study folded under kept B-0223 trust family

## Annotation Efficiency (24 killed)

- **B-0242** (composite 6.1): redundant with B-0241 (kept); context-reacquisition cost folds into the cost-honest benchmark
- **B-0243** (composite 4.7): likely published: SSL-feature coverage sampling for AL cold start is established
- **B-0245** (composite 6.0): near-miss; accuracy-per-minute objective folds into B-0241 cost-honest family
- **B-0246** (composite 5.9): near-miss; contestability prediction adjacent to inter-rater family kept via B-0003
- **B-0248** (composite 4.9): near-miss; adaptive slice selection is an established annotation-saving recipe variant
- **B-0249** (composite 5.7): near-miss; coarse-then-refine staging is sensible workflow engineering not a finding
- **B-0250** (composite 6.5): near-miss (painful); low-res annotation + label super-resolution fresh; annotation-interface budget spent
- **B-0251** (composite 6.0): near-miss; ontology/protocol mapping folds into convention family kept via B-0159
- **B-0252** (composite 5.9): near-miss; learning-curve extrapolation literature exists; dense validation incremental
- **B-0253** (composite 6.4): near-miss (painful); interesting-case selection bias real; folded under deployment-shift audits kept elsewhere
- **B-0254** (composite 5.7): near-miss; campaign stopping rules sibling of killed B-0199; sequential-analysis port
- **B-0256** (composite 4.9): engineering optimization: keyframe density and verification policy tuning
- **B-0257** (composite 6.3): near-miss (painful); speech-first annotation timely with grounding models; interface-heavy and venue-risky
- **B-0258** (composite 4.8): likely published-adjacent: difficulty-based crowd/expert routing established in crowdsourcing literature
- **B-0259** (composite 5.7): near-miss; per-class marginal-value allocation is an AL variant of killed B-0245 economics
- **B-0260** (composite 5.8): near-miss; statistical process control transplant; service-flavored contribution
- **B-0262** (composite 5.1): likely published: annotator error-process modeling for medical segmentation established (confusion-matrix rater models)
- **B-0263** (composite 5.5): near-miss; tool latency/rendering as causal variable; human-factors venue fit weak for target venues
- **B-0264** (composite 6.0): redundant with B-0244 (kept); pre-annotation threshold is a sub-question of the automation-bias study
- **B-0265** (composite 4.8): likely published-adjacent: crowd-consensus vs expert masks studied in crowdsourced medical annotation
- **B-0266** (composite 4.8): near-miss; retrieval-warp-verify annotation partially explored in label-transfer pipelines
- **B-0267** (composite 6.2): near-miss (painful); label-error cleaning + re-ranking done for classification; benchmark-trust budget spent on protected B-0196
- **B-0268** (composite 4.3): likely published: no-gold-standard rater reliability from agreement structure is the Dawid-Skene lineage
- **B-0270** (composite 5.7): framework-heavy: portfolio optimization over supervision types; each term needs its own validated model first

## Long-tail Recognition & Segmentation (24 killed)

- **B-0273** (composite 6.0): near-miss; interior-only reweighting is a module fix on a real side effect
- **B-0276** (composite 6.0): near-miss; contextual imprisonment adjacent to context-debiasing literature
- **B-0277** (composite 4.3): likely published: head-to-tail variation transfer via feature-space augmentation established
- **B-0278** (composite 4.9): near-miss; hierarchy-mediated supervision partially explored in hierarchical classification/segmentation
- **B-0279** (composite 4.7): likely published-adjacent: expert ensembles with routing for long-tail established (RIDE lineage)
- **B-0280** (composite 6.4): near-miss (painful); parametric-head/non-parametric-tail hybrid; retrieval-augmented dense prediction moving fast
- **B-0281** (composite 4.9): near-miss; context-matched pasting is a plausibility-model module on copy-paste
- **B-0282** (composite 6.0): near-miss; frequency-conditional recalibration; calibration family trimmed at portfolio level
- **B-0283** (composite 6.4): near-miss; long-tail vs open-set tension partially explored; sharp framing not enough to clear the bar
- **B-0284** (composite 4.8): crowded: federated personalization machinery; per-site tail heads are an architecture answer to a data question
- **B-0286** (composite 4.8): likely published-adjacent: post-hoc logit adjustment ports to segmentation exist
- **B-0287** (composite 6.4): redundant with B-0271 (kept); effective-sample-size law is the quantitative sequel of the axes study
- **B-0288** (composite 6.0): near-miss; class-agnostic boundary transfer is a module fix; boundary-quality decomposition folded into B-0271
- **B-0289** (composite 5.8): redundant with B-0292 (kept); zero-frequency composition covered by the compositional long-tail evaluation
- **B-0290** (composite 5.8): near-miss; retrieval-mine-verify collection is the data-engine recipe; economics angle incremental
- **B-0291** (composite 4.9): narrow: sampling-temperature schedule study; answer likely dataset-specific
- **B-0293** (composite 4.8): module: capacity reallocation architecture surgery; capacity measurement is the hard unsolved part
- **B-0294** (composite 5.9): likely published-adjacent: noise-hits-tail-hardest interaction documented in classification; seg replication incremental
- **B-0295** (composite 5.8): redundant with B-0290 (both killed); novelty-scored tail mining is the same data-engine recipe
- **B-0296** (composite 6.2): near-miss (painful); utility-weighted evaluation; benchmark-reform budget spent on B-0274
- **B-0297** (composite 6.4): near-miss (painful); tail-first forgetting order is sharp; continual/forgetting literature adjacency too strong
- **B-0298** (composite 5.8): near-miss; sub-mode discovery below label granularity; unsupervised cluster quality is the load-bearing risk
- **B-0299** (composite 6.0): redundant family: detectability-vs-delineability decomposition kept once via B-0128
- **B-0300** (composite 5.9): redundant with B-0271 family; collection scaling law folds into the axes/effective-sample-size program

## Cross-domain Transfer (24 killed)

- **B-0301** (composite 5.2): likely published-adjacent: what-transfers-to-medical analyses established (Transfusion lineage); layer-transplant delta small
- **B-0303** (composite 6.3): near-miss (painful); video-time as through-plane axis is a cheap creative test; single-hypothesis paper risk
- **B-0304** (composite 4.8): module: channel-statistics reinitialization surgery for spectral transfer
- **B-0305** (composite 5.2): likely published-adjacent: stain-transfer vs stain-invariance comparisons exist across histopath literature
- **B-0307** (composite 6.0): near-miss (painful); homology-guided human-to-animal transfer is genuinely fresh; veterinary label scarcity blocks the falsifier
- **B-0308** (composite 4.5): likely published: pairwise dense-task transfer matrices are the Taskonomy program
- **B-0309** (composite 4.9): module: conflict-aware batch composition; gradient-surgery family established
- **B-0310** (composite 5.9): near-miss; adapter/task arithmetic compositionality actively explored; domain instantiation incremental
- **B-0311** (composite 6.0): near-miss; merging preconditions studied in soups/re-basin line; domain-expert instantiation moderate
- **B-0312** (composite 5.9): near-miss; text-anchored cross-domain alignment emerging in VLM-based DA
- **B-0314** (composite 6.1): redundant with B-0313 (kept); negative-transfer regime is the low end of the same predictor
- **B-0315** (composite 5.1): likely published: checkpoint-selection proxies established (LogME/LEEP lineage); dense extension incremental
- **B-0316** (composite 5.9): near-miss; diffusion-vs-discriminative dense features crowded and fast-moving
- **B-0317** (composite 5.7): near-miss; scale-canonicalizing pyramids; scale shift studied within aerial-to-ground literature
- **B-0318** (composite 4.9): module: relational distillation port across domains
- **B-0320** (composite 5.7): near-miss; layout-statistics canonicalization niche within overhead-ground transfer
- **B-0321** (composite 6.0): redundant with B-0306 (kept); same physical-attribution design pointed at dermoscopy
- **B-0322** (composite 6.0): near-miss (painful); patient-paired fundus-OCT alignment partially explored in cross-modal retinal work
- **B-0323** (composite 6.2): near-miss (painful); surgical sim-to-real factorial valuable; attribution-study budget spent on B-0306
- **B-0324** (composite 5.7): near-miss; bridging-domain curricula explored in intermediate-domain DA
- **B-0325** (composite 6.0): consistency kill: frequency-band diagnostics family cut with B-0042; same fingerprint idea at domain-pair level
- **B-0326** (composite 5.9): redundant with B-0313/B-0328 (kept); freeze-depth rule is a corollary of the distance laws
- **B-0329** (composite 4.4): likely published: domain-conditional normalization established (domain-specific BN lineage)
- **B-0330** (composite 6.4): near-miss (painful); robustness-transfer independence partially studied in classification; dense version cut on balance

## Multimodal Supervision for Dense Prediction (25 killed)

- **B-0332** (composite 5.8): likely published-adjacent: reported-size consistency training overlaps RECIST-supervised lesion segmentation lineage
- **B-0333** (composite 5.8): near-miss; location-phrase-to-atlas grounding partially explored in anatomy-aware report supervision
- **B-0334** (composite 6.3): near-miss (painful); hedging-to-uncertainty mapping creative; calibration family trimmed at portfolio level
- **B-0335** (composite 6.3): near-miss; ordinal longitudinal supervision from comparison statements; longitudinal family funded via B-0014
- **B-0336** (composite 6.4): near-miss (painful); template-leakage audit folded under kept hallucination audit B-0350; one report-shortcut audit suffices
- **B-0337** (composite 4.2): likely published: word-region alignment for report supervision established (local-alignment pretraining lineage)
- **B-0338** (composite 4.8): near-miss; count constraints from text; counting-constrained segmentation partially explored
- **B-0339** (composite 5.2): likely published-adjacent: dense-CLIP repair is a crowded fast-moving subfield
- **B-0340** (composite 4.7): likely published: depth-discontinuity boundary supervision established in RGB-D segmentation
- **B-0341** (composite 5.7): near-miss; misregistration-tolerance characterization useful; graceful-degradation losses are module territory
- **B-0342** (composite 4.9): narrow: dropout-schedule study on the killed missing-modality family (B-0029)
- **B-0343** (composite 6.3): near-miss (painful); surgeon-commentary supervision is fresh; speech-video alignment noise and data curation burden block the falsifier
- **B-0345** (composite 4.4): likely published: PET-guided CT tumor segmentation is an established co-segmentation literature
- **B-0346** (composite 6.4): near-miss (painful); LLM parsing-error noise budget timely; audit budget spent on B-0350/B-0360
- **B-0347** (composite 6.6): redundant with B-0360 (kept); instruction-following benchmark subsumed by the grounding-capability taxonomy
- **B-0348** (composite 6.3): near-miss (painful); covariate conditioning with shortcut separation; prior-vs-shortcut tension deserves a cleaner testbed first
- **B-0349** (composite 5.7): framework-heavy: fusion of weak modalities with correlated errors; each channel needs validation first
- **B-0351** (composite 5.5): near-miss; free-text acquisition-context conditioning; metadata-conditioning family thin across the catalog
- **B-0352** (composite 4.2): likely published: sentence/region-level contrastive alignment established in medical VLP
- **B-0354** (composite 5.8): near-miss; structured-vs-free-text supervision value; policy-relevant but service-flavored
- **B-0355** (composite 6.0): near-miss; report-image consistency QC; QC family trimmed across the catalog
- **B-0356** (composite 6.3): near-miss (painful); elastography as boundary arbiter is physically principled; paired-data scarcity blocks the decisive experiment
- **B-0357** (composite 4.9): likely published: RECIST-diameter-supervised lesion segmentation at archive scale is established (DeepLesion lineage)
- **B-0358** (composite 6.3): near-miss (painful); report-generation-as-auxiliary-task isolation; assumed-transfer question folded under B-0360 program
- **B-0359** (composite 6.3): near-miss; outcome-anchored labels definitionally correct but sparse and access-gated; feasibility caps it

## Cross-cutting Wildcards (3 killed)

- **B-0363** (composite 6.3): near-miss; efficiency-normalized re-ranking partially covered by existing efficiency-audit literature
- **B-0364** (composite 6.7): near-miss (painful); reproducibility audit of dense SOTA; audit budget spent on protected B-0107/B-0196 which target the same trust question
- **B-0365** (composite 5.9): service: standardization protocol; valuable community work but not a research finding

