# Windows2 Stage-2 Agent F — Kills (Batch A)

**51 ideas killed** out of 352. Kill reasons fall into five families:

1. **Already published / community consensus** — the core claim exists in the literature or is folklore backed by papers.
2. **Duplicate within batch** — a near-copy of a stronger sibling idea (Stage-1 agent A's own mutation chains produced overlaps).
3. **Ill-posed or unfalsifiable** — the hypothesis has no decisive readout, or its own risk note concedes the confound is fatal.
4. **Tech-report scope** — outcome is an engineering observation without a scientific question underneath.
5. **Infeasible as stated** — required data/oracle does not exist and no credible proxy was proposed.

A kill here is a recommendation, not a veto: agents D/E and the PI may overrule. Every kill retains full 14-dimension scores in `scores.jsonl`.

## C01-sam-prompt-failure (6)

- **W2-A-0002** — Test whether SAM's three ambiguity heads implement a stable part/object/group hierarchy or an arbitrary mode split.
  - Kill reason: Useful sanity audit but scope is a tech-report; likely outcome 'mostly stable' has no home at a main venue.
- **W2-A-0004** — Box prompts act as scale priors that override image evidence when box and object conflict.
  - Kill reason: Box-perturbation robustness is heavily reported (esp. MedSAM evals); the directional regression law is a delta, not a paper.
- **W2-A-0011** — Sub-patch objects get quantized to the token grid: measure the staircase floor of SAM on <16 px objects.
  - Kill reason: The 'theoretical floor' is ill-defined per its own risk note; W2-A-0015's oracle-zoom decomposition subsumes the useful content.
- **W2-A-0012** — Cluster SAM's mask-token embeddings across millions of prompts to test whether text-free training induced a latent semantic taxonomy.
  - Kill reason: 'SAM features are semantically poor' is already community consensus backed by many SAM+CLIP fusion papers; the shape-covariate control is a footnote, not a paper.
- **W2-A-0019** — Test compositionality of SAM's image embedding: does masked-object feature subtraction behave algebraically?
  - Kill reason: Feature-arithmetic negative result on a dense encoder; decoder-hallucination confound (own risk note) makes any outcome uninterpretable.
- **W2-A-0024** — SAM has an orientation anisotropy: elongated vertical vs horizontal objects segment differently, inherited from photo statistics.
  - Kill reason: Rotation-anisotropy audits are a known genre; the SA-1B-statistics linkage is the only fresh part and it is correlational.

## C02-sam2-video-memory (6)

- **W2-A-0031** — SAM2 accuracy is non-monotonic in frame rate: temporal aliasing hurts fast periodic motion at intermediate fps.
  - Kill reason: Real aliasing physics, but scope is periodic-motion scenes only - a workshop curiosity unless it changes fps guidance for a deployed domain.
- **W2-A-0033** — Which frame you prompt matters more than how well you prompt it: middle-frame prompting beats first-frame in long videos.
  - Kill reason: Frame-selection for interactive VOS is a published genre (frame-recommendation papers, IVOS round protocols); budget framing is a delta, not a discovery.
- **W2-A-0035** — Recency-based memory is provably wrong for periodic scenes: diversity-sampled memory should beat recency at equal size.
  - Kill reason: Inference-time memory-selection improvements for SAM2 are already a small industry (SAMURAI motion-aware memory, SAM2Long memory tree); the regime-split residual is thin.
- **W2-A-0037** — Topology-change events (splitting, merging, pouring) are an unhandled event class in video segmentation - build the taxonomy and measure failure.
  - Kill reason: VOST (CVPR'23) already benchmarks VOS under transformations including cutting/splitting; the area-ratio law is the only unclaimed sliver and is too small alone.
- **W2-A-0038** — Joint multi-object tracking in SAM2 degrades per-object accuracy vs independent runs: measure memory contention.
  - Kill reason: SAM2 keeps per-object memory (own KNOWN note); the residual contention channels (shared backbone, resolution) make any positive finding small and architecture-version-fragile.
- **W2-A-0044** — Fit the memory-size vs drift power law: how much memory buys how much tracking longevity?
  - Kill reason: Memory-size sweeps without retraining may be off-manifold (own risk), and SAM2Long-style work already explores the memory-budget axis with stronger engineering.

## C03-medical-limits (6)

- **W2-A-0051** — Train on rater-disagreement-preserving labels instead of consensus: does keeping disagreement improve calibration more than it costs accuracy?
  - Kill reason: Multi-rater distribution learning on LIDC is a decade-deep literature (Prob U-Net, PHiSeg, SSN, annotator-sampling); the calibration-vs-Dice tradeoff has been quantified repeatedly. Lit-attacked below.
- **W2-A-0053** — Slice-direction inconsistency of 2D models on 3D volumes scales with through-plane anisotropy: derive the consistency-spacing law.
  - Kill reason: Fully subsumed by W2-A-0062's dimensionless crossover law; keeping both dilutes the same experiment.
- **W2-A-0056** — Stain normalization in pathology helps less than stain-diverse training: an assumption audit with controlled compute.
  - Kill reason: Tellez et al. (Med Image Anal 2019) ran essentially this factorial: augmentation dominates normalization cross-site. The per-class sign-flip residual is not enough to resurrect it.
- **W2-A-0066** — Contrast-polarity invariance test: can one model segment T1 and T2 (inverted tissue contrast) without contrast-specific features, and what does it cost?
  - Kill reason: SynthSeg already demonstrated contrast-agnostic segmentation via aggressive synthetic contrast randomization; physics-consistent inversion is an augmentation flavor, not a new question. Pathology-erasure caveat further narrows it.
- **W2-A-0069** — Simulate cross-vendor MRI shift from k-space physics and test how much of the real vendor gap physics-only augmentation closes.
  - Kill reason: Physics augmentation for MRI is established in reconstruction, and the decomposition's ceiling is set by simulation fidelity to proprietary pipelines (own risk note) - the conclusion is uninterpretable when closure fails.
- **W2-A-0073** — Site fingerprints in federated medical segmentation: features encode hospital identity, and removing it costs accuracy - measure the privacy-performance coupling.
  - Kill reason: Site/scanner fingerprints are established in radiomics and site-invariance methods exist in federated medical imaging; the joint quantification is consolidation, not discovery.

## C04-amorphous-smoke-fire (3)

- **W2-A-0079** — Fire flicker has a characteristic temporal frequency signature: a 1-second temporal window beats any single-frame architecture at matched compute.
  - Kill reason: Flicker-frequency analysis is the backbone of 2000s-era video fire detection (wavelet flicker methods, ~10 Hz signatures); the matched-FLOPs modern restaging is engineering, not discovery. Compression caveat is the one live finding.
- **W2-A-0083** — Synthetic-fog robustness does not transfer to real fog because real fog is heterogeneous: quantify the homogeneity gap.
  - Kill reason: Synthetic-to-real fog transfer was the explicit subject of the Foggy Cityscapes/Foggy Zurich/CMAda line (Sakaridis et al.); the heterogeneity-index regression is a residual, not a paper.
- **W2-A-0095** — Smoke motion vs camera motion entanglement in aerial footage: drone ego-motion masquerades as plume dynamics and vice versa.
  - Kill reason: Ego-motion compensation for aerial temporal cues is competent engineering hygiene; the synthetic-ego-motion protocol lacks parallax by its own admission, and the finding is an ablation table.

## C05-transparent-glass-mirror (5)

- **W2-A-0105** — A $30 polarizer beats architecture research for glass segmentation: quantify the sensor-vs-model marginal value.
  - Kill reason: Polarization-cue glass segmentation with a dedicated RGB-P dataset is published at CVPR level (PGSNet line); the marginal-value-vs-architectural-progress accounting is rhetoric on top of a known result.
- **W2-A-0113** — Joint vs sequential reflection-removal and segmentation: does cleaning reflections first help or destroy the very cues glass detectors need?
  - Kill reason: Quantified antagonism between two preprocessing choices is a 3x3 ablation table; useful engineering note, not a research bet.
- **W2-A-0116** — Mirror recursion depth as a scene-understanding stress test: what do models do with mirrors inside mirrors?
  - Kill reason: Fun diagnostic, honestly self-described as a niche probe; zero-representation-of-reflection is better established via 0121's safety-relevant version.
- **W2-A-0120** — A $200 thermal camera makes glass opaque: quantify when cheap LWIR fusion beats years of RGB algorithmic progress on transparent surfaces.
  - Kill reason: RGB-thermal glass segmentation with paired datasets is published (RGB-T glass detection line); the economic-accounting framing does not survive the existence of the dataset papers.
- **W2-A-0125** — Window tint and low-emissivity coatings create a spectral fingerprint: modern architectural glass is detectable by its color cast, old glass is not.
  - Kill reason: Construction-era stratification is a clever confound hunt, but era entangles frames, cleanliness, and context (own note); the multi-covariate story is too soft to headline.

## C06-camouflage-ambiguity (5)

- **W2-A-0129** — Camouflage and saliency are poles of one conspicuity axis: test whether a single linear direction in feature space spans both tasks.
  - Kill reason: Joint SOD-COD modeling exploiting their contradictory relationship is published (uncertainty-aware joint SOD/COD, CVPR 2021); the linear-direction probe is a cleaner instrument for a settled question.
- **W2-A-0133** — Artificial (military/textile) camouflage and biological camouflage do not transfer: two data regimes with different statistics.
  - Kill reason: Bio-vs-artificial camouflage transfer is data-blocked (military camouflage sets are not public) and the phase-statistics story is speculative; defense-adjacent framing also complicates venues.
- **W2-A-0138** — Cross-domain camouflage: does COD pretraining transfer to isointense lesion detection in medical images?
  - Kill reason: The COD-medical bridge is already built: the Concealed Object Detection line explicitly spans camouflage and polyp/lesion segmentation with shared architectures. Channel-ablation localization does not rescue it.
- **W2-A-0146** — Boundary-gradient-direction statistics separate camouflaged from conspicuous objects: a low-level signature of camouflage strategy.
  - Kill reason: May reduce to known contrast measures by its own admission; the angular component is a thin bet for a full project, and COD difficulty-attribute analyses already crowd this space.
- **W2-A-0149** — Model-specific worst-case camouflage synthesis: use texture generation to find each model's blind spots and test whether blindness transfers.
  - Kill reason: Physical/3D adversarial camouflage synthesis is a mature literature (adversarial textures, clothing, vehicle wraps); the transfer-matrix delta does not clear the bar.

## C07-boundary-small-objects (3)

- **W2-A-0154** — Thin structures break at regular intervals set by feature stride: connectivity failure is periodic, not random.
  - Kill reason: The aliasing family (0003, 0154, 0165) is one paper, not three; 0003's phase-sweep causal design is the strongest instantiation - fold gap-periodicity in as a section.
- **W2-A-0157** — For small objects, context carries most of the information: measure the interior-vs-context information ratio as a function of object size.
  - Kill reason: Occlusion-sweep information ratios are a known interpretability recipe; the size-crossover is one figure inside 0171's cleaner attribution question.
- **W2-A-0165** — Sub-stride phase determines tiny-object visibility: shifting the image by 8 pixels changes which small objects a model finds.
  - Kill reason: Shift-variance of CNNs is a published genre (anti-aliasing line); the small-object phase-flip quantification belongs inside 0003's phase-sweep paper, not as a third aliasing project.

## C08-uncertainty-longtail (4)

- **W2-A-0179** — Measure the labeling ROI of uncertainty-routed annotation: does model uncertainty actually direct human effort to where it pays?
  - Kill reason: Uncertainty-sampling vs committee-disagreement routing is textbook active learning with decades of comparisons, including for segmentation; the Dice-per-hour dressing does not make it new.
- **W2-A-0184** — Validate the aleatoric/epistemic decomposition against ground truth ambiguity: at boundaries, current methods conflate what they claim to separate.
  - Kill reason: Referent-anchored validation of aleatoric/epistemic separation in segmentation is the exact program of recent uncertainty-validation frameworks (ValUES-style, ICLR 2024); the boundary-specific conflation figure is a subsection of that existing line.
- **W2-A-0186** — Are tumor-volume confidence intervals valid? Propagate segmentation uncertainty into derived clinical quantities and test empirical coverage.
  - Kill reason: Same study as W2-A-0074 (its C08 restatement); keep 0074 as the canonical entry and kill the duplicate to avoid double-counting a single project.
- **W2-A-0196** — Uncertainty as the first sensor to fail: under gradual weather degradation, which uncertainty signal rises first, and does its order match accuracy decline?
  - Kill reason: Onset-ordering of uncertainty signals is a second-order refinement of 0177; graded natural-weather data scarcity makes the decisive version infeasible and the synthetic version unconvincing.

## C09-annotation-interactive (6)

- **W2-A-0201** — Real crowdworker clicks vs simulated clicks: quantify the sim2real prompting gap that inflates every interactive segmentation benchmark.
  - Kill reason: A real-click corpus with replay evaluation showing simulator inflation and rank changes is exactly the published RClicks benchmark (NeurIPS 2024). Scooped nearly verbatim. Lit-attacked below.
- **W2-A-0202** — Information-per-second of annotation primitives: clicks vs scribbles vs boxes vs verbal corrections, measured properly for once.
  - Kill reason: Time-based comparisons of annotation primitives date to the point-supervision literature (Bearman-era cost accounting) and interface studies since; the shape-conditional map is a refinement, not a discovery.
- **W2-A-0207** — Where should a scribble go? Skeleton vs boundary-following vs freeform strokes have measurably different information gain per pixel drawn.
  - Kill reason: Scribble-simulation and placement studies exist across weakly-supervised segmentation; the region-vs-boundary decomposition of placement value is an ablation, and the guided-human confirmation is costly for its payoff.
- **W2-A-0208** — Region-level active learning with real time-cost models: intra-image selection beats whole-image selection once annotation time is measured honestly.
  - Kill reason: Region-level AL for segmentation is established; the overhead-aware cost-model twist is real but the field's response will be 'so publish the cost model' - a tool, not a thesis.
- **W2-A-0211** — Optimal correction-frame selection in video annotation: model uncertainty peaks beat uniform keyframes, but the real optimum is drift-onset frames.
  - Kill reason: Frame-selection for interactive video annotation is a published genre (frame-recommendation for IVOS); drift-onset timing is a variant gated on the unproven self-diagnosis signal (0047).
- **W2-A-0213** — Gaze as free dense supervision: eye-tracking during ordinary image inspection carries recoverable segmentation signal.
  - Kill reason: Gaze-as-weak-supervision for medical segmentation has multiple recent papers (REFLACX-era eye-tracking supervision line); the performance-accounting delta is not enough, and gaze's extent-vs-hotspot limitation is already documented.

## C10-domain-shift (2)

- **W2-A-0230** — BN-statistics adaptation helps photometric shift but actively harms semantic shift: map when the cheapest TTA trick becomes poison.
  - Kill reason: When-TTA-helps-vs-harms has been mapped by the TTA-pitfalls line (ICML 2023 era) including statistics-adaptation failure under label shift; the channel-statistics pre-test is an increment on a published map.
- **W2-A-0232** — Transferability is spatially structured: sky transfers, road texture does not - build per-region transfer maps and adapt only what fails.
  - Kill reason: Transfer maps + gated adaptation is method engineering downstream of 0226/0231's science; if those decompositions land, this becomes their obvious application section.

## C11-weak-semi-self (1)

- **W2-A-0261** — Temporal correspondence is the missing hard-positive: video-mined positives beat augmentation positives for dense contrastive pretraining at matched compute.
  - Kill reason: Temporal-correspondence positives for dense contrastive pretraining are published repeatedly (space-time correspondence SSL, video-frame-similarity pretraining, dense tracking-based positives); matched-compute bookkeeping does not revive it.

## C12-foundation-dense-science (1)

- **W2-A-0281** — What makes a good visual in-context example? Retrieval laws for one-shot segmentation prompting with image-mask pairs.
  - Kill reason: Support-example selection for visual in-context learning (SegGPT/Painter era) is published, including learned retrieval policies; the pose/scale-dominance law is a residual worth a workshop note at most.

## C13-benchmark-failure-audit (2)

- **W2-A-0303** — The polygon ceiling: COCO's coarse polygons impose a measurable upper bound on learnable and measurable boundary quality.
  - Kill reason: COCO mask coarseness and its consequences are now documented by refined re-annotation efforts; the surviving sliver (straight-segment mimicry in model outputs) should migrate into 0312's style-dialect paper.
- **W2-A-0324** — Model-in-the-loop adversarial test collection for segmentation: does human-sourced hardness transfer across models or just defeat the collection-time model?
  - Kill reason: Dynabench-style adversarial collection is an established methodology; the transfer-validity decomposition is a worthwhile appendix to 0290's shared-blind-spot study rather than a standalone bet.

## C14-assumption-tests (1)

- **W2-A-0332** — Where does adaptation live? Decoder-only fine-tuning matches full fine-tuning under most domain shifts - locate the layers that shift actually touches.
  - Kill reason: Surgical fine-tuning (ICLR 2023) established that different shift types are best handled by tuning different layer blocks, including the photometric-early/semantic-mid structure; the dense-prediction port is an application note.
