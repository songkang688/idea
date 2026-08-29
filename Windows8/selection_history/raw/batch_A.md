# Batch A — Research Idea Generation (Full Raw List)

Generated: 2026-08-28. Branch: cursor/windows8-research-idea-evolution-cd91.

## Conventions

- **Idea count:** exactly 350 ideas, IDEA-A-0001 .. IDEA-A-0350.
- **Epistemic markers:** `[KNOWN FACT]` = widely established / uncontroversial background (no specific citation implied). `[HYPOTHESIS]` = a conjecture this idea proposes to test. Every Core Hypothesis is a HYPOTHESIS by definition and is written to be falsifiable.
- **No invented papers, citations, or experimental numbers appear anywhere in this file.**
- **Forbidden-pattern compliance:** no idea proposes module stacking, Transformer+CNN hybrids, apply-X-to-medical transplants, loss swapping, backbone swapping, or attention-adding. Ideas are diagnostic studies, falsifiable behavioral hypotheses, evaluation/benchmark science, data-centric interventions, or task reformulations.
- **Cluster tags:** `SAM-FAIL` (SAM/SAM2 failure modes), `MED-SEG` (medical segmentation limitation), `AMORPH` (smoke/fire/transparent/ambiguous objects), `DET-LIMIT` (detection limitation), `DOMAIN` (domain shift), `PROMPT` (prompt sensitivity), `FT-STAB` (fine-tuning instability / PEFT / forgetting), `DATA-FAIL` (dataset failure), `FM-FAIL` (foundation model failure), `METHOD-FAIL` (existing method / evaluation failure).

### Section map

| Section | IDs | Cluster | Count |
|---|---|---|---|
| 1 | 0001–0040 | SAM-FAIL | 40 |
| 2 | 0041–0080 | MED-SEG | 40 |
| 3 | 0081–0120 | AMORPH | 40 |
| 4 | 0121–0150 | DET-LIMIT | 30 |
| 5 | 0151–0185 | DOMAIN | 35 |
| 6 | 0186–0220 | PROMPT | 35 |
| 7 | 0221–0260 | FT-STAB | 40 |
| 8 | 0261–0295 | DATA-FAIL | 35 |
| 9 | 0296–0325 | FM-FAIL | 30 |
| 10 | 0326–0350 | METHOD-FAIL | 25 |

---

## Section 1 — SAM / SAM2 failure modes (IDEA-A-0001 .. 0040)

### IDEA-A-0001
- Idea: Test whether SAM's mask boundaries systematically snap to the locally strongest image gradient rather than the semantically correct boundary.
- Problem: [KNOWN FACT] SAM was trained on natural-image masks (SA-1B) where semantic boundaries usually coincide with strong gradients; when they diverge (soft shadows, low-contrast borders) it is unclear which cue wins.
- Core Hypothesis (falsifiable): [HYPOTHESIS] On images where the true boundary and the strongest local gradient are deliberately separated (controlled composites), SAM's boundary error is biased toward the gradient by a measurable, consistent offset; if boundary errors are symmetric around the true boundary, the hypothesis is false.
- Why Important: Explains a large family of "near-miss" masks and predicts exactly when SAM cannot be trusted without any retraining.
- Why Possibly Novel: Failure analyses usually report aggregate IoU; a controlled cue-separation psychophysics-style design for a promptable segmenter is rare.
- Minimal Experiment: Build ~200 composite images where object edge and a distractor gradient are offset by k pixels (k swept); prompt SAM with center clicks; measure signed boundary displacement vs k.
- Main Risk: Composites may be too artificial; must confirm the effect on a small set of real low-contrast photos.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0002
- Idea: Use the entropy/disagreement of SAM's multimask outputs as a predictor of human annotation cost for that image region.
- Problem: [KNOWN FACT] SAM emits multiple candidate masks per prompt to handle ambiguity; annotation budgeting currently ignores this signal.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Disagreement among SAM's candidate masks correlates (rank correlation clearly above chance) with human time-to-annotate and inter-annotator variance of that region; no correlation falsifies it.
- Why Important: Would give a free, zero-training difficulty estimator for annotation pipelines and active labeling.
- Why Possibly Novel: Multimask output is usually treated as a nuisance to argmax over, not as a measurement instrument.
- Minimal Experiment: For ~300 objects, record annotator time and multi-rater variance; compute SAM multimask pairwise IoU spread; correlate.
- Main Risk: Multimask spread may mostly encode part/whole hierarchy, not difficulty; must separate the two.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0003
- Idea: Determine whether SAM2's video error accumulation is driven by the number of occlusion events rather than raw sequence length.
- Problem: [KNOWN FACT] Streaming video segmenters with memory accumulate errors; the causal driver (time vs discrete disruptive events) is not established.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Holding length fixed, videos with more occlusion events show proportionally larger final-frame IoU drop; holding occlusion count fixed, length alone adds little. If length dominates, hypothesis is false.
- Why Important: Changes how practitioners budget re-prompting: re-prompt after events, not on a timer.
- Why Possibly Novel: Length and event count are confounded in natural benchmarks; a controlled factorial design decouples them.
- Minimal Experiment: Synthesize/curate videos in a 2-factor grid (length × occlusion count) from existing tracking data; run SAM2 with one initial prompt; regress final IoU on both factors.
- Main Risk: Occlusion "events" are hard to define crisply; need a preregistered operational definition.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0004
- Idea: Map click-position instability "islands": interior regions of an object where a single point prompt flips SAM's output between qualitatively different masks.
- Problem: [KNOWN FACT] Point-prompt outputs vary with click location; the spatial structure of this instability is uncharacterized.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Instability is spatially organized (contiguous flip regions aligned with internal contours/parts), not random; a spatial-autocorrelation test at chance level falsifies it.
- Why Important: Enables click-placement guidance for annotators and defines a reproducible robustness statistic for promptable models.
- Why Possibly Novel: Prompt robustness is usually summarized as a scalar; dense per-pixel prompt-response maps are rarely produced or analyzed.
- Minimal Experiment: For 100 objects, prompt SAM at every pixel on a grid inside the GT mask; cluster resulting masks; visualize and quantify flip-region geometry.
- Main Risk: Compute cost of dense prompting; mitigate with coarse-to-fine grids.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0005
- Idea: Audit SAM for topology blindness: measure performance conditioned on object genus (number of holes) with appearance controlled.
- Problem: [KNOWN FACT] Mask quality metrics average over topology; objects with holes (donuts, handles, lattices) are a distinct regime.
- Core Hypothesis (falsifiable): [HYPOTHESIS] At matched size/contrast, per-object IoU drops monotonically with genus and SAM systematically fills holes; no genus effect falsifies it.
- Why Important: Hole-filling errors are catastrophic in downstream measurement tasks (grasping, area estimation).
- Why Possibly Novel: Topology-stratified evaluation of promptable segmenters is essentially absent from standard reports.
- Minimal Experiment: Assemble ~150 objects stratified by genus from existing datasets; prompt identically; report IoU and a hole-preservation score vs genus.
- Main Risk: Genus confounds with thin structures; control by matching minimum structure width across strata.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0006
- Idea: Attribute SAM's thin-structure failure to a specific stage (encoder resolution loss vs decoder readout) using probing diagnostics, without proposing any architecture change.
- Problem: [KNOWN FACT] SAM struggles on thin elongated structures (wires, spokes); which stage loses the information is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Thin-structure information is still linearly decodable from encoder features (a probe can recover the structure), implicating the decoder readout; if probes also fail, the encoder is the bottleneck and the hypothesis is false.
- Why Important: Correct attribution tells the field where effort is wasted, before anyone proposes fixes.
- Why Possibly Novel: Stage-wise failure attribution via probing is common in interpretability but rarely applied to promptable segmentation failure modes.
- Minimal Experiment: Train linear/pixel probes on frozen SAM encoder features to predict thin-structure masks; compare probe recall vs SAM's own output recall on the same images.
- Main Risk: Probe capacity confounds; use strictly limited probe families and report capacity sweeps.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0007
- Idea: Characterize the inconsistent semantics of negative point prompts: cases where adding a negative click enlarges or teleports the mask.
- Problem: [KNOWN FACT] Negative clicks are meant to exclude regions; anecdotally they sometimes produce counterintuitive global changes, but no systematic census exists.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A non-trivial, quantifiable fraction of negative clicks increases mask area or moves the mask to a different object, and these cases are predictable from the click's distance to the current boundary; if effects are always local and monotone, the hypothesis is false.
- Why Important: Interactive pipelines assume monotone refinement; violations silently corrupt annotation workflows.
- Why Possibly Novel: Refinement is evaluated by average IoU-per-click; non-monotonicity census and its predictors are not standard.
- Minimal Experiment: For 500 objects, run scripted positive+negative click sequences; log mask-area deltas and centroid jumps per negative click; fit a predictor of pathological responses.
- Main Risk: Scripted clicks may not represent human behavior; validate on a small human-in-the-loop sample.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0008
- Idea: Measure the dose-response curve of SAM's box-prompt sensitivity: output IoU as a function of controlled box jitter (translation, scale, aspect).
- Problem: [KNOWN FACT] Box prompts in practice come from noisy detectors or humans; SAM's tolerance envelope is not quantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] IoU degradation is asymmetric — boxes that are too tight hurt substantially more than boxes too loose by the same relative amount; symmetric degradation falsifies it.
- Why Important: Directly informs how upstream detectors should be tuned (favor recall/looseness) when feeding SAM.
- Why Possibly Novel: Jitter robustness is mentioned qualitatively; a standardized dose-response protocol with asymmetry analysis is not established.
- Minimal Experiment: Sweep box perturbations on ~1k objects across scales; plot IoU vs signed perturbation; test asymmetry statistically.
- Main Risk: Effect may be dataset-dependent; run on two visually distinct datasets to check.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0009
- Idea: Scale-consistency audit: quantify how much SAM's mask for the same object changes when the object is presented at different scales (resize/crop pyramid).
- Problem: [KNOWN FACT] Convolution/patch-based encoders are not scale-equivariant; the practical magnitude for promptable segmentation is unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Self-consistency (IoU between rescaled predictions of the same object) drops sharply below a characteristic object size in patch units, revealing a scale floor tied to patch resolution; smooth scale-independence falsifies it.
- Why Important: Gives a concrete operating-range specification (minimum object size) practitioners can apply before trusting outputs.
- Why Possibly Novel: Consistency-under-rescaling as a label-free reliability metric for promptable models is underexplored.
- Minimal Experiment: For 300 objects, build 5-level resize pyramids, prompt equivalently, compute cross-scale self-IoU; locate the breakdown scale.
- Main Risk: Interpolation artifacts confound; use multiple resamplers and report both.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0010
- Idea: Cue-conflict test for promptable segmentation: does SAM follow shape or texture when the two disagree (texture-swapped object composites)?
- Problem: [KNOWN FACT] Cue-conflict stimuli revealed texture bias in image classifiers; the analogous question for boundary placement in promptable segmenters is open.
- Core Hypothesis (falsifiable): [HYPOTHESIS] SAM's boundary follows texture discontinuities over silhouette shape in a majority of conflict trials; a shape-dominant result falsifies it.
- Why Important: Predicts failure classes (camouflage, texture bleed) from a single measurable bias parameter.
- Why Possibly Novel: Cue-conflict methodology has not been ported to boundary-level, prompt-conditioned outputs.
- Minimal Experiment: Generate texture-swap composites where silhouette says A and texture says B; prompt at object center; classify which cue the output boundary tracks.
- Main Risk: Composites may fall off-distribution and trigger degenerate outputs; include realism controls.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0011
- Idea: Quantify SAM2 identity switches between visually similar adjacent instances and build an instance-confusion matrix over appearance similarity.
- Problem: [KNOWN FACT] Trackers confuse look-alike instances; how SAM2's memory-conditioned design behaves under graded similarity is uncharacterized.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Switch probability rises steeply once inter-instance embedding similarity crosses a threshold, and switches are sticky (rarely self-correct); graceful degradation or frequent self-correction falsifies it.
- Why Important: Identity persistence is the whole point of video segmentation; a stickiness result changes recovery strategy design.
- Why Possibly Novel: Failure is usually reported as aggregate video scores; similarity-conditioned switch analysis with recovery statistics is not standard.
- Minimal Experiment: Curate multi-instance clips stratified by instance similarity (e.g., animal herds vs mixed objects); track with SAM2; log switch onset, similarity, and recovery events.
- Main Risk: GT identity in crowded clips is expensive; start with semi-synthetic duplicated-instance videos.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0012
- Idea: Test whether SAM boundaries lock onto JPEG block-artifact edges at high compression, producing grid-quantized masks.
- Problem: [KNOWN FACT] JPEG uses 8×8 block transforms that create artificial edges; deployed images are often heavily compressed.
- Core Hypothesis (falsifiable): [HYPOTHESIS] As quality factor decreases, SAM boundary positions become measurably concentrated at multiples of 8 pixels (block grid), beyond what image content explains; no grid alignment falsifies it.
- Why Important: Compression is ubiquitous in real pipelines (CCTV, web); a quantization bias would corrupt any measurement made from masks.
- Why Possibly Novel: Compression robustness is reported as IoU drop; the structural form of the failure (grid locking) is not analyzed.
- Minimal Experiment: Recompress a fixed evaluation set at descending quality; compute histogram of boundary x/y coordinates modulo 8; test for peaks vs uncompressed baseline.
- Main Risk: Effect may be small relative to boundary noise; use paired per-image statistics.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0013
- Idea: Decouple camouflage failure into "cannot find" vs "cannot delineate" by giving SAM oracle prompts on camouflaged-object data.
- Problem: [KNOWN FACT] Camouflaged-object benchmarks show poor zero-shot results for promptable models; whether localization or delineation fails is conflated.
- Core Hypothesis (falsifiable): [HYPOTHESIS] With oracle center clicks and oracle boxes, SAM recovers most of the gap on camouflaged objects, showing failure is dominantly localization, not boundary delineation; persistent low IoU under oracle prompts falsifies it.
- Why Important: Determines whether camouflage research should target proposal/salience or boundary modeling.
- Why Possibly Novel: The oracle-prompt decomposition is simple but rarely reported as the primary result with effect sizes.
- Minimal Experiment: On an existing camouflage dataset, compare automatic-everything mode vs oracle click vs oracle box; decompose the deficit.
- Main Risk: Oracle prompts leak information beyond localization (box encodes extent); report click-only and box separately.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0014
- Idea: Derive an empirical sampling law for SAM's automatic "everything" mode: small-object recall as a function of prompt-grid density.
- Problem: [KNOWN FACT] Everything mode seeds a finite point grid; objects between grid points can be missed, but the recall/density tradeoff is unquantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Recall of objects of size s follows a predictable function of s × grid density (a coverage law), allowing density to be chosen from a target recall; poor fit of any monotone coverage law falsifies it.
- Why Important: Converts an arbitrary hyperparameter into a principled, budgetable choice for large-scale auto-annotation.
- Why Possibly Novel: Everything-mode is treated as a black box; a quantitative sampling-theory treatment appears missing.
- Minimal Experiment: Sweep grid densities on datasets with size-stratified instances; fit recall(s, density); validate on a held-out dataset.
- Main Risk: Recall also depends on the deduplication post-steps; hold those fixed and document.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0015
- Idea: Memory poisoning in SAM2: measure how a single corrupted frame (occluder, glare, codec glitch) propagates through the memory and how long recovery takes.
- Problem: [KNOWN FACT] SAM2 conditions on a memory of past frames; sensitivity to a one-frame corruption is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A single corrupted frame degrades subsequent masks with an exponential-like recovery profile whose half-life depends on corruption type; instantaneous recovery falsifies it.
- Why Important: Real streams contain glitches; a long recovery half-life implies pipelines need glitch detection and memory resets.
- Why Possibly Novel: Corruption analysis of the memory pathway (as opposed to per-frame robustness) is largely unexplored.
- Minimal Experiment: Inject controlled single-frame corruptions at varying timestamps into clips; track per-frame IoU before/after; fit recovery curves per corruption type.
- Main Risk: Results may depend on internal memory-management heuristics across versions; pin versions and report.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0016
- Idea: Rotation-consistency audit for SAM: same object, image rotated by θ, measure self-consistency of un-rotated predictions across θ.
- Problem: [KNOWN FACT] Patch-based encoders and learned position encodings are not rotation-equivariant; the practical magnitude for masks is unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Self-consistency degrades non-monotonically with θ, worst near 45°, and degradation concentrates on elongated objects; flat consistency falsifies it.
- Why Important: Aerial, microscopy, and document imagery have no canonical orientation; users need an orientation-reliability spec.
- Why Possibly Novel: Rotation studies exist for classifiers; per-object mask-consistency profiles for promptable models are not standard.
- Minimal Experiment: Rotate an evaluation set over 0–90° in steps; prompt equivalently (rotating prompts too); compute cross-θ self-IoU curves by object elongation.
- Main Risk: Rotation resampling artifacts; use high-order interpolation and padding controls.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0017
- Idea: Characterize non-convergent interactive refinement: sequences where additional corrective clicks make SAM oscillate between two masks instead of converging.
- Problem: [KNOWN FACT] Interactive segmentation is evaluated by clicks-to-target-IoU, implicitly assuming convergence; oscillation is not measured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A measurable fraction of objects enters stable two-cycle oscillations under a deterministic corrective-click policy, and these objects share identifiable properties (ambiguous part boundaries); zero oscillation falsifies it.
- Why Important: Oscillation wastes annotator effort invisibly; identifying it enables early stopping and mask arbitration.
- Why Possibly Novel: Click-curve papers report averages; fixed-point/limit-cycle analysis of the interaction loop is new territory.
- Minimal Experiment: Run 20-click deterministic correction policies on ~1k objects; detect cycles in mask-sequence space; profile oscillating objects.
- Main Risk: Oscillation may be policy-specific; test 3 distinct correction policies.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0018
- Idea: Calibration audit of SAM's predicted-IoU head across domains: is its self-reported mask quality trustworthy off-distribution?
- Problem: [KNOWN FACT] SAM outputs a predicted IoU per mask; downstream systems increasingly threshold on it, but its cross-domain calibration is unverified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] The predicted-IoU head is well-ranked but poorly calibrated out of domain, with a domain-specific bias that is stable and correctable by a scalar offset per domain; unstable or unrankable predictions falsify it.
- Why Important: A stable per-domain bias means one tiny labeled sample can recalibrate the head for free.
- Why Possibly Novel: The IoU head is widely used, rarely audited as a measurement instrument with calibration curves.
- Minimal Experiment: On 5 visually distinct datasets, plot predicted vs true IoU; fit per-domain offsets; test transfer of offsets to held-out data.
- Main Risk: Ranking may also collapse in extreme domains; report both calibration and rank metrics.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0019
- Idea: Worst-case prompt search: find the in-object click position that minimizes mask quality, defining an adversarial-prompt robustness gap.
- Problem: [KNOWN FACT] Reported interactive results use favorable (center-like) clicks; the lower bound over legitimate prompts is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] The gap between best-click and worst-click IoU is large for a substantial fraction of objects and is predictable from object part structure; a uniformly small gap falsifies it.
- Why Important: Real users click in unmodeled ways; the worst-case gap bounds deployment risk for interactive tools.
- Why Possibly Novel: Adversarial analysis normally perturbs pixels; treating the legitimate prompt itself as the adversarial variable is underexplored.
- Minimal Experiment: Grid-search clicks within GT masks on ~500 objects; report best/median/worst IoU distributions and predictors of the gap.
- Main Risk: Worst-case may reflect genuinely ambiguous part prompts (user intent), not failure; separate part-consistent outputs from errors.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0020
- Idea: Background-dependence test for transparent objects: does SAM's mask of the same glass object change when only the background behind it changes?
- Problem: [KNOWN FACT] Transparent objects reveal their background; a segmenter could be keying on transmitted background content rather than the object.
- Core Hypothesis (falsifiable): [HYPOTHESIS] With the object and viewpoint fixed and only the backdrop varied, SAM's mask changes substantially (low cross-background self-IoU), demonstrating background-keyed segmentation; background-invariant masks falsify it.
- Why Important: Establishes whether transparent-object failure is a cue problem (what the model looks at) rather than a capacity problem.
- Why Possibly Novel: Requires a physically controlled capture setup (turntable + backdrop swaps) rarely used in segmentation failure analysis.
- Minimal Experiment: Photograph ~20 glass objects under 10 backdrops each with fixed pose; prompt identically; measure cross-backdrop mask self-consistency.
- Main Risk: Small object set limits generality; supplement with synthetic renders for scale.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0021
- Idea: Compare SAM2 against SAM on purely static images to measure whether video-oriented training altered single-image segmentation behavior.
- Problem: [KNOWN FACT] SAM2 supports images and video; whether the video capability came at a cost or benefit to static-image behavior (boundary style, ambiguity handling) is not systematically mapped.
- Core Hypothesis (falsifiable): [HYPOTHESIS] SAM2 differs from SAM on static images in a structured way — e.g., systematically different mask granularity or boundary tightness — not just noise; statistically indistinguishable outputs falsify it.
- Why Important: Practitioners treat the two as interchangeable on images; any systematic behavioral drift matters for reproducibility.
- Why Possibly Novel: Version-to-version behavioral diffing (beyond benchmark scores) is rarely published.
- Minimal Experiment: Run both models with identical prompts on ~2k images; compare paired boundary F-scores, granularity distributions, and multimask diversity; test for systematic shifts.
- Main Risk: Differences may be dataset-specific; use several image distributions.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0022
- Idea: Map SAM's implicit part–whole hierarchy: how click position within an object deterministically selects part vs whole, and whether the induced hierarchy is consistent.
- Problem: [KNOWN FACT] A click on a shirt may segment shirt, torso, or person; the selection rule SAM applies is opaque.
- Core Hypothesis (falsifiable): [HYPOTHESIS] The part-vs-whole choice is predictable from click distance to internal contours and relative part size, forming a consistent (transitive) hierarchy per image; intransitive or unpredictable selections falsify it.
- Why Important: If the hierarchy is consistent, SAM can be used as a zero-shot part-discovery tool; if not, interactive UX must compensate.
- Why Possibly Novel: Multimask output is known to encode hierarchy, but its consistency/transitivity has not been treated as a testable property.
- Minimal Experiment: Dense-click 200 multi-part objects; build induced containment graphs; measure transitivity violations and fit a selection-rule model.
- Main Risk: Hierarchy may differ per multimask slot; analyze slots separately.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0023
- Idea: Predict SAM failure from the image encoder embedding alone: train a lightweight external failure predictor and test whether failures are pre-encoded.
- Problem: [KNOWN FACT] There is no label-free way to know when SAM's output is wrong; if failure is predictable from internal features, monitoring is possible.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A shallow probe on frozen encoder features predicts per-object IoU with useful accuracy across held-out datasets, implying failure is encoded before decoding; chance-level prediction on held-out domains falsifies it.
- Why Important: A validated failure predictor enables selective automation (auto-accept vs route-to-human).
- Why Possibly Novel: Failure prediction exists for classifiers; doing it from a promptable segmenter's own frozen features with cross-domain validation is largely untested.
- Minimal Experiment: Regress true IoU from pooled encoder features on dataset A; evaluate correlation on datasets B/C without retraining.
- Main Risk: Probe may learn dataset identity, not failure; enforce cross-domain evaluation as primary metric.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0024
- Idea: Relighting-consistency audit: quantify SAM mask stability of the same scene under natural illumination changes (time-lapse data), isolating photometric sensitivity.
- Problem: [KNOWN FACT] Deployed cameras see the same scene under changing light; segmentation stability under pure illumination change is rarely isolated from content change.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Mask instability across illumination correlates with shadow-boundary strength, and most instability is attributable to shadow edges rather than global exposure; exposure-dominated instability falsifies it.
- Why Important: Separates a fixable input-normalization problem from a deeper cue-confusion problem (shadows as pseudo-objects).
- Why Possibly Novel: Uses static-camera time-lapse as a natural controlled experiment — cheap and underused for segmentation auditing.
- Minimal Experiment: Collect/curate static-camera day-long sequences; prompt identical objects hourly; decompose instability by shadow presence vs exposure shift.
- Main Risk: Scene micro-changes (wind, people) contaminate; filter frames by pixel-change masks outside the object.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0025
- Idea: Boundary-convention mismatch in overhead imagery: test whether SAM's failures on aerial scenes concentrate on boundary types that have no natural-image analogue (parcel lines, field transitions).
- Problem: [KNOWN FACT] Aerial imagery contains legal/agronomic boundaries that are visually gradual; SA-1B-style training data encodes photographic object conventions.
- Core Hypothesis (falsifiable): [HYPOTHESIS] SAM error stratified by boundary type shows a discrete gap: photographic-style boundaries (buildings, cars) near natural-image performance, convention-style boundaries (field edges) far worse even at matched contrast; uniform degradation falsifies it.
- Why Important: Tells the remote-sensing community whether the gap is a domain problem or a task-definition problem.
- Why Possibly Novel: Boundary-type taxonomies are rarely the unit of analysis; usually it is dataset-level averages.
- Minimal Experiment: Annotate boundary types on an existing aerial dataset; evaluate SAM per boundary type at matched local contrast; compare strata.
- Main Risk: Boundary typing is subjective; use multiple raters and report agreement.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0026
- Idea: Systematically test what survives when non-RGB modalities (depth, thermal, ultrasound) are rendered as pseudo-RGB for SAM: which invariances transfer and which break.
- Problem: [KNOWN FACT] Practitioners feed colormapped non-RGB data to RGB-trained models; the transfer is anecdotally hit-or-miss with no predictive account.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Transfer quality is predictable from low-level statistics of the rendered image (edge density, local contrast distribution similarity to natural images), independent of semantic content; no statistical predictor beating chance falsifies it.
- Why Important: A predictive rule would let engineers assess feasibility before collecting labels in a new modality.
- Why Possibly Novel: Reframes "does SAM work on modality X" into a quantitative image-statistics matching question.
- Minimal Experiment: Evaluate SAM on several colormapped modalities; regress per-image IoU on natural-image-statistics distance measures; validate the regression on a held-out modality.
- Main Risk: Colormap choice is a hidden variable; sweep colormaps as part of the design.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0027
- Idea: Identify the residual regime where classical interactive methods (graph-cut style) still beat SAM — hypothesized to be extreme high-frequency boundaries (fur, foliage) — and characterize its boundary-statistics signature.
- Problem: [KNOWN FACT] Classical energy-based interactive segmentation operates at pixel resolution; learned models operate at feature resolution, suggesting complementary regimes.
- Core Hypothesis (falsifiable): [HYPOTHESIS] There exists a measurable boundary-frequency threshold above which classical pixel-level methods outperform SAM at equal interaction budget; SAM dominating everywhere falsifies it.
- Why Important: Defines when hybrid human workflows should route to which tool — an actionable deployment result, not a new model.
- Why Possibly Novel: Post-foundation-model re-evaluations of classical methods with regime analysis are rare.
- Minimal Experiment: Compare SAM vs a classical interactive baseline at matched click budgets on data stratified by boundary spectral content; locate the crossover.
- Main Risk: Classical baselines are implementation-sensitive; use well-established public implementations and report settings fully.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0028
- Idea: Test whether SAM's boundary error contains a constant per-domain signed offset (systematic over/under-segmentation by k pixels) that can be corrected post hoc by morphological calibration.
- Problem: [KNOWN FACT] Averaged metrics hide whether boundary error is random or a fixed directional bias.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Per domain, the signed distance distribution of predicted vs true boundary has a stable nonzero mean, and applying the inverse fixed offset improves boundary F-score on held-out images; a zero-mean or unstable offset falsifies it.
- Why Important: A one-parameter free calibration that improves masks without touching the model would be immediately useful.
- Why Possibly Novel: Boundary-bias decomposition into systematic vs stochastic components is rarely reported.
- Minimal Experiment: Compute signed boundary distance histograms per dataset; estimate offset on half the data; test correction on the other half.
- Main Risk: Bias may vary by object class/size within a domain; check stratified stability first.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0029
- Idea: Multimask ranking instability: measure how often SAM's top-ranked mask flips identity between near-identical inputs (one-pixel prompt shift, imperceptible noise).
- Problem: [KNOWN FACT] Downstream systems take the argmax mask by predicted score; ranking robustness between close candidates is unexamined.
- Core Hypothesis (falsifiable): [HYPOTHESIS] When two candidate masks have near-equal predicted scores, tiny input perturbations flip the argmax with high probability, producing discontinuous system behavior; stable rankings under perturbation falsify it.
- Why Important: Explains flickering outputs in interactive tools and motivates margin-based abstention in pipelines.
- Why Possibly Novel: Ranking (not mask) instability as the object of study is a new slice on prompt sensitivity.
- Minimal Experiment: For 1k prompts, perturb input/prompt minimally; record argmax flip rate vs candidate score margin; fit flip-probability-vs-margin curve.
- Main Risk: Flips between equivalent masks are harmless; weight flips by inter-candidate IoU distance.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0030
- Idea: Prompt-timing effect in SAM2: quantify how much whole-video quality depends on which frame receives the initial prompt, and learn to predict the optimal prompt frame.
- Problem: [KNOWN FACT] Video annotation workflows prompt the first frame by default; whether that is systematically suboptimal is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Prompting at a frame chosen by simple visibility heuristics (object large, unoccluded, unblurred) beats first-frame prompting by a consistent margin across videos; no timing effect falsifies it.
- Why Important: A zero-cost workflow change (pick a better frame) could recover substantial quality in video annotation.
- Why Possibly Novel: Prompt timing as an optimization variable is largely unstudied; the prompt is treated as given.
- Minimal Experiment: For each video in a standard set, prompt every k-th frame separately; measure whole-video quality per starting frame; test heuristic predictors of the best frame.
- Main Risk: Bidirectional propagation may flatten the effect; report both directions.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0031
- Idea: Modal/amodal confusion audit: determine whether SAM outputs visible-region masks, completed-object masks, or an inconsistent mixture under partial occlusion.
- Problem: [KNOWN FACT] Segmentation datasets define masks as visible regions, but users often intend whole objects; models trained on mixed conventions may interpolate unpredictably.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Under graded occlusion, SAM switches from modal to partially-amodal behavior at a characteristic occlusion fraction rather than staying consistently modal; consistent modal output falsifies it.
- Why Important: Downstream measurement (size, count, grasp planning) breaks silently if the convention shifts with occlusion level.
- Why Possibly Novel: Occlusion studies measure IoU drop; convention drift as the failure mode is a different question.
- Minimal Experiment: Composite controlled occlusions at 0–90% over known objects; classify outputs as modal/amodal/mixture per occlusion level.
- Main Risk: Amodal GT for composites must be exact; use synthetic layering so GT is free.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0032
- Idea: Small-object failure attribution via oracle zoom: diagnose whether small-object failure is information loss at the encoder or readout failure at the decoder.
- Problem: [KNOWN FACT] SAM performs poorly on very small objects; the stage responsible is undetermined, so proposed fixes are unguided.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Running inference on an enlarged crop (oracle zoom) recovers most small-object performance, implicating encoder-resolution information loss rather than decoder readout; no recovery under oracle zoom falsifies it.
- Why Important: Attribution determines whether the community should pursue input-resolution strategies or decoder-side strategies — before building anything.
- Why Possibly Novel: Uses oracle interventions purely diagnostically, producing an attribution result rather than a method.
- Minimal Experiment: For size-stratified objects, compare standard inference vs oracle-crop inference at fixed prompt semantics; quantify recovered fraction per size bin.
- Main Risk: Cropping changes context; add context-preserving controls (zoom with padded context).
- Research Cluster tag: SAM-FAIL

### IDEA-A-0033
- Idea: Overlay interference: measure how burned-in text, watermarks, and UI overlays distort SAM masks of objects beneath them.
- Problem: [KNOWN FACT] Real-world images (broadcast, CCTV, screenshots) carry overlays; their effect on promptable segmentation is unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Overlays cause boundary capture (mask edges snap to overlay glyph edges) with severity predictable from overlay contrast, and the object mask is disrupted well beyond the overlay's own pixels; strictly local disruption falsifies it.
- Why Important: Quantifies a pervasive deployment hazard and yields an overlay-severity score usable as a preflight check.
- Why Possibly Novel: Text-in-image effects are studied for classification (typographic attacks); the dense-mask disruption footprint is not.
- Minimal Experiment: Composite parametric overlays (opacity, contrast, coverage) onto an evaluation set; measure IoU loss vs overlay parameters and the spatial extent of disruption.
- Main Risk: Synthetic overlays may miss real overlay statistics; validate on genuine broadcast frames.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0034
- Idea: Memory-saturation curve for SAM2: controlled measurement of segmentation quality vs sequence length when content difficulty is held constant by construction.
- Problem: [KNOWN FACT] Natural long videos confound length with content change, so raw "long video" results cannot isolate memory saturation.
- Core Hypothesis (falsifiable): [HYPOTHESIS] On loop-constructed videos (same content cycled), quality declines with length despite zero content novelty, isolating a pure memory-mechanism degradation; flat quality falsifies it.
- Why Important: Distinguishes "videos get harder" from "the memory mechanism degrades," which have different engineering consequences.
- Why Possibly Novel: Loop-construction as a control for content difficulty in video segmentation evaluation appears unused.
- Minimal Experiment: Build looped videos of varying lengths from short clips; run SAM2 once per length; plot quality vs length with content fixed.
- Main Risk: Looping introduces unnatural motion discontinuities at seams; crossfade seams and verify no seam-locked errors.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0035
- Idea: Granularity-prior leakage: test whether SAM's preferred mask sizes mirror the mask-size distribution of its training data rather than the query image's object statistics.
- Problem: [KNOWN FACT] SA-1B has a particular distribution of mask granularities; a model could internalize it as a prior on "what a maskable thing is."
- Core Hypothesis (falsifiable): [HYPOTHESIS] In ambiguous scenes, SAM's chosen granularity regresses toward a fixed prior distribution (measurable as a pull toward specific relative-size modes) regardless of scene content; content-driven granularity falsifies it.
- Why Important: A granularity prior would explain systematic over/under-merging in domains whose object-size statistics differ from web photos.
- Why Possibly Novel: Treats training-set annotation granularity as a leaked inductive bias — a dataset-to-behavior causal claim that is testable.
- Minimal Experiment: Construct scenes with tunable hierarchical structure (tileable textures, object grids); measure chosen granularity vs scene parameter; compare to published SA-1B mask-size statistics.
- Main Risk: Access to exact training statistics is partial; use published dataset statistics only, no speculation.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0036
- Idea: Motion-blur bias: test whether SAM systematically widens masks in the blur direction, inflating object area as a function of blur length.
- Problem: [KNOWN FACT] Motion blur smears object boundaries directionally; whether models place the boundary at blur onset, midpoint, or end is uncharacterized.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Mask area inflation grows approximately linearly with blur kernel length and is anisotropic (aligned with blur direction), implying a predictable blur-corrected area estimate; isotropic or non-systematic error falsifies it.
- Why Important: Area/size measurements from masks (sports, traffic, biology) are silently biased on moving objects.
- Why Possibly Novel: Blur robustness is reported as IoU; the geometric structure (directional inflation law) is not.
- Minimal Experiment: Apply parametric directional blur to sharp images with GT; regress area inflation and boundary displacement on kernel length/direction.
- Main Risk: Synthetic blur differs from true camera blur; validate on a small real high-speed-camera set.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0037
- Idea: Evaluate SAM's predicted-IoU head as a zero-training out-of-distribution detector: does self-reported quality drop reliably flag domain shift?
- Problem: [KNOWN FACT] Pipelines need cheap OOD flags; SAM already emits a quality estimate whose OOD behavior is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] The distribution of predicted IoU over automatic prompts separates in-domain from shifted inputs with useful detection scores across several shift types; failure to separate falsifies it.
- Why Important: A no-training OOD monitor from an existing head would be immediately deployable in production segmentation systems.
- Why Possibly Novel: Repurposing an auxiliary regression head as an OOD statistic, with proper detection-theoretic evaluation, is unexplored.
- Minimal Experiment: Compute predicted-IoU distributions on an in-domain set and multiple shifted sets (corruption, new domain, new modality); report detection performance of a simple statistic per shift.
- Main Risk: The head may be overconfident precisely on the failures that matter; report per-shift-type results honestly, including negatives.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0038
- Idea: Repeating-pattern overflow: characterize when SAM "flood-fills" across periodic structures (fences, tiles, windows) instead of segmenting the prompted unit.
- Problem: [KNOWN FACT] Periodic textures make unit boundaries ambiguous; when a user prompts one fence picket, the intended granularity is under-determined for the model.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Overflow probability rises with pattern regularity (autocorrelation peak strength) and falls with inter-unit gaps, yielding a quantitative overflow law; overflow unrelated to periodicity metrics falsifies it.
- Why Important: Periodic structures are everywhere in built environments; a predictive law tells UIs when to demand disambiguating prompts.
- Why Possibly Novel: Links a classic signal property (autocorrelation) to a promptable-model failure with a testable functional form.
- Minimal Experiment: Curate/synthesize periodic scenes sweeping regularity and gap size; single-click prompts on one unit; measure overflow rate vs pattern statistics.
- Main Risk: "Intended unit" is subjective; fix intent operationally via instructions to annotators building GT.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0039
- Idea: Re-detection latency: measure how many frames SAM2 needs to re-acquire an object after full occlusion, as a function of occlusion duration and appearance change during occlusion.
- Problem: [KNOWN FACT] Objects vanish and return in real video; aggregate video metrics do not expose re-acquisition dynamics.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Re-detection latency grows with occlusion duration and sharply with appearance change during occlusion (lighting/pose), revealing a memory-staleness effect; constant latency falsifies it.
- Why Important: Latency after occlusion determines suitability for safety applications (a child re-emerging from behind a car).
- Why Possibly Novel: Event-aligned latency analysis (re-emergence as time zero) is a tracking-community tool not yet applied to promptable video segmentation.
- Minimal Experiment: Curate/construct re-emergence events with controlled gap length and appearance change; measure frames-to-recovery distributions.
- Main Risk: Defining "recovered" needs a threshold; preregister it and show robustness to the choice.
- Research Cluster tag: SAM-FAIL

### IDEA-A-0040
- Idea: Prompt-ensemble variance as an unsupervised quality estimate: validate that the spread of masks across jittered prompts predicts true IoU without labels.
- Problem: [KNOWN FACT] No ground truth exists at deployment; internal consistency across prompt perturbations is a candidate label-free quality signal that has not been rigorously validated.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Cross-prompt mask variance is strongly negatively correlated with true IoU across datasets, and the relationship transfers across domains without refitting; weak or non-transferring correlation falsifies it.
- Why Important: Turns prompt sensitivity — usually a defect — into a practical self-assessment mechanism.
- Why Possibly Novel: Ensemble-disagreement quality estimation is standard for model ensembles, mostly untested for prompt ensembles of a single frozen model.
- Minimal Experiment: For each object, sample 10 jittered prompts; compute pairwise mask IoU spread; correlate with true IoU across 4 datasets; test cross-domain transfer of the fitted relationship.
- Main Risk: Confidently wrong regions (consistent but incorrect) create a blind spot; quantify the rate of consistent-wrong cases explicitly.
- Research Cluster tag: SAM-FAIL

---

## Section 2 — Medical segmentation limitations (IDEA-A-0041 .. 0080)

### IDEA-A-0041
- Idea: Isolate whether SAM-style models fail on medical images because of boundary-contrast statistics rather than semantic unfamiliarity, using contrast-matched natural-image controls.
- Problem: [KNOWN FACT] Promptable foundation models degrade on medical images; "domain gap" is cited without decomposing which image property causes the drop.
- Core Hypothesis (falsifiable): [HYPOTHESIS] On natural images artificially matched to medical boundary-contrast distributions, performance drops by a similar fraction as on real medical data, implying contrast statistics (not anatomy semantics) dominate; a small drop on matched controls falsifies it.
- Why Important: If contrast statistics dominate, cheap photometric data curation matters more than medical semantic pretraining.
- Why Possibly Novel: Causal decomposition of the medical gap via matched-statistics controls, rather than another benchmark report.
- Minimal Experiment: Measure boundary-contrast distributions on CT/MR organ boundaries; remap natural images to match; compare relative IoU drops on both.
- Main Risk: Contrast remapping may introduce its own artifacts; include identity-remap controls.
- Research Cluster tag: MED-SEG

### IDEA-A-0042
- Idea: Build an evaluation protocol that scores medical segmentation models within the inter-rater variance band, so models are not penalized for disagreeing with one annotator by less than humans disagree with each other.
- Problem: [KNOWN FACT] Inter-annotator variability in medical contours is substantial; single-rater ground truth treats one opinion as truth.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Under variance-band scoring, the ranking of existing models changes materially compared with single-rater Dice ranking, meaning current leaderboards partly rank agreement-with-one-rater; identical rankings falsify it.
- Why Important: Misranked models misdirect research and clinical adoption decisions.
- Why Possibly Novel: Multi-rater data exists, but leaderboard-level re-ranking analysis using variance-band scoring is rarely executed.
- Minimal Experiment: On a public multi-rater dataset, re-score existing model outputs with band-aware metrics; compare rank correlation to standard Dice ranking.
- Main Risk: Few multi-rater datasets; results may not generalize beyond those structures.
- Research Cluster tag: MED-SEG

### IDEA-A-0043
- Idea: Use inter-slice inconsistency of 2D segmentation across the z-axis as a label-free failure signal in 3D medical volumes.
- Problem: [KNOWN FACT] Many pipelines segment 3D volumes slice-by-slice; anatomy is smooth in z, so wild slice-to-slice mask changes suggest error — but this signal is not validated as an error detector.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A z-inconsistency statistic correlates strongly with true per-case Dice across organs and scanners, enabling label-free QA; weak correlation falsifies it.
- Why Important: Hospitals need automated QA that works without ground truth on every new case.
- Why Possibly Novel: The signal is folklore among practitioners; a rigorous cross-organ, cross-site validation with operating thresholds is missing.
- Minimal Experiment: Compute z-consistency metrics on predictions over 3 public volumetric datasets; correlate with true Dice; report detection performance for worst-decile cases.
- Main Risk: Some structures are genuinely discontinuous in z; per-organ calibration required.
- Research Cluster tag: MED-SEG

### IDEA-A-0044
- Idea: Quantify the "healthy-anatomy bias": models trained mostly on normal anatomy fail disproportionately on anatomy adjacent to pathology even when the target structure itself is normal.
- Problem: [KNOWN FACT] Public datasets over-represent normal or single-pathology cases; the spillover effect of nearby pathology on normal-structure segmentation is unquantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Segmentation error on a normal organ increases with proximity/volume of neighboring pathology, controlling for image quality; no proximity effect falsifies it.
- Why Important: Real patients have comorbidities; a proximity effect means benchmark scores overstate clinical performance precisely for sick patients.
- Why Possibly Novel: Failure is usually attributed to the pathological structure itself; the collateral effect on adjacent normal anatomy is rarely measured.
- Minimal Experiment: Stratify cases in a public dataset by presence/size of pathology near the target organ; compare organ Dice across strata with matched image quality.
- Main Risk: Pathology correlates with age/scanner; control covariates in regression.
- Research Cluster tag: MED-SEG

### IDEA-A-0045
- Idea: Audit CT-windowing sensitivity: measure how strongly promptable and dedicated models' outputs change under clinically legitimate window/level settings of the same scan.
- Problem: [KNOWN FACT] CT display windowing is a free parameter chosen per task; models consuming windowed images inherit an unacknowledged preprocessing sensitivity.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Output variation across standard clinical windows exceeds the variation across patients for some structures, i.e., preprocessing choice can matter more than biology; smaller-than-patient variation falsifies it.
- Why Important: An uncontrolled preprocessing knob that rivals biological variation invalidates cross-study comparisons.
- Why Possibly Novel: Windowing is treated as a fixed detail; elevating it to a quantified sensitivity axis with variance decomposition is new framing.
- Minimal Experiment: Segment the same scans under 5 standard windows; decompose output variance into window vs patient components (variance components analysis).
- Main Risk: Some models ingest raw intensity values and are immune; scope claims to image-input pipelines.
- Research Cluster tag: MED-SEG

### IDEA-A-0046
- Idea: Evaluate models against ambiguity-aware tumor-margin ground truth: measure how much of the reported error mass lies inside the multi-rater disagreement region.
- Problem: [KNOWN FACT] Tumor margins are often genuinely ambiguous (infiltration); binary GT forces an arbitrary line.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A large share of reported tumor-segmentation error lies within the inter-rater disagreement band, meaning headline errors overstate actionable disagreement; a small share falsifies it.
- Why Important: Reframes "models are bad at tumors" into "the task is partially unresolvable," redirecting effort to uncertainty reporting.
- Why Possibly Novel: The error-mass-inside-ambiguity-band decomposition is a simple statistic that is rarely reported.
- Minimal Experiment: On multi-rater tumor data, compute the fraction of each model's error voxels inside vs outside the rater-disagreement band.
- Main Risk: Rater bands from few raters underestimate true ambiguity; report sensitivity to rater count.
- Research Cluster tag: MED-SEG

### IDEA-A-0047
- Idea: Decompose small-lesion failure into detection (finding the lesion at all) vs delineation (contouring once found) using oracle-localization experiments.
- Problem: [KNOWN FACT] Small-lesion metrics conflate misses with bad contours; the two failures need different research responses.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Given oracle lesion locations, delineation quality of small lesions is close to that of large lesions (per-voxel), showing the bottleneck is detection; persistent delineation gaps under oracle localization falsify it.
- Why Important: Determines whether the field should invest in candidate generation/screening or in contour refinement for small lesions.
- Why Possibly Novel: Oracle decomposition is common in detection literature but rarely applied to medical lesion segmentation with size stratification.
- Minimal Experiment: On a lesion dataset, evaluate models with and without oracle point seeds across lesion-size bins; decompose the deficit.
- Main Risk: Oracle seeds may leak extent info; use point seeds only.
- Research Cluster tag: MED-SEG

### IDEA-A-0048
- Idea: Test whether cross-vendor scanner shift is dominated by low-frequency intensity components, via frequency-band swap experiments between vendors' images.
- Problem: [KNOWN FACT] Models degrade across scanner vendors; the spectral character of the causal difference is not established for segmentation.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Swapping only low-frequency amplitude spectra between vendor A and B images transfers most of the performance change, implying the gap is low-frequency intensity, not texture; no transfer under low-band swap falsifies it.
- Why Important: If low-frequency dominates, simple physics-grounded harmonization suffices and heavy adaptation machinery is unnecessary.
- Why Possibly Novel: Frequency-swap causal probing exists for natural-image domain gaps; a careful medical vendor-shift version with segmentation endpoints is uncommon.
- Minimal Experiment: Construct band-swapped hybrids between paired vendor cohorts; evaluate a fixed model on original vs swapped; attribute the gap by band.
- Main Risk: Vendor cohorts differ in patients too; use traveling-phantom or same-patient-rescanned data where available.
- Research Cluster tag: MED-SEG

### IDEA-A-0049
- Idea: Measure asymmetric capability forgetting when a promptable foundation model is fine-tuned on a single organ: which zero-shot abilities (other organs, natural images, interactivity) die first and fastest.
- Problem: [KNOWN FACT] Fine-tuning improves target-task performance and degrades others; the ordering and rates of capability loss for promptable segmentation are unmapped.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Forgetting is strongly asymmetric — interactive prompt-following degrades before natural-image mask quality — and the ordering is consistent across organs; unordered or inconsistent forgetting falsifies it.
- Why Important: A reproducible forgetting hierarchy tells practitioners exactly what to re-test after any fine-tune.
- Why Possibly Novel: Forgetting is usually a scalar; a capability-resolved forgetting spectrum for promptable models is new.
- Minimal Experiment: Fine-tune on one organ dataset with a standard recipe; evaluate a fixed battery (other organs, natural images, click-response quality) at checkpoints; plot capability-loss trajectories.
- Main Risk: Recipe-dependent results; repeat across 3 seeds and 2 learning rates minimum.
- Research Cluster tag: MED-SEG

### IDEA-A-0050
- Idea: Patient-level leakage audit protocol for public medical segmentation benchmarks: estimate how much reported performance is inflated by same-patient or same-study images spanning train/test splits.
- Problem: [KNOWN FACT] Some public datasets were assembled from overlapping sources; patient-level split hygiene varies and is rarely re-verified by users.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Detectable same-patient leakage exists in at least some widely used splits, and models score measurably higher on leaked test items than on verified-disjoint ones; no score difference falsifies it.
- Why Important: Leakage silently inflates the field's belief about progress in a safety-critical domain.
- Why Possibly Novel: Leakage audits exist in ML broadly; a standardized, reproducible medical-imaging protocol (metadata plus image-similarity based) with per-benchmark reports is missing.
- Minimal Experiment: Run near-duplicate/patient-matching detection across train/test of 3 popular benchmarks; compare model scores on suspected-leak vs clean subsets.
- Main Risk: False-positive duplicate detection; require multi-signal agreement (metadata + image similarity) before labeling leakage.
- Research Cluster tag: MED-SEG

### IDEA-A-0051
- Idea: Characterize metric-induced blind spots: quantify how volume-dominated metrics (Dice) statistically de-prioritize small structures and boundary shells during evaluation, and how model rankings change under size-decoupled reporting.
- Problem: [KNOWN FACT] Dice on large structures is insensitive to boundary-shell errors and small-structure failures; evaluation choices shape which models look good.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Re-ranking existing methods with size-stratified and boundary-shell metrics flips a nontrivial fraction of published pairwise orderings; stable rankings falsify it.
- Why Important: If rankings flip, the community has been partially optimizing an artifact of metric choice.
- Why Possibly Novel: This is a systematic re-ranking study across many existing results, not another metric proposal.
- Minimal Experiment: Collect public predictions/checkpoints for one benchmark; recompute stratified metrics; report ordering flips with confidence intervals.
- Main Risk: Public predictions are scarce; may need to re-run released checkpoints under one pipeline.
- Research Cluster tag: MED-SEG

### IDEA-A-0052
- Idea: Census the "always segment something" bias: how models behave on empty slices/scans where the target structure is absent (post-resection, out-of-range anatomy).
- Problem: [KNOWN FACT] Training sets rarely include target-absent cases; deployment includes them routinely (organ removed, wrong protocol).
- Core Hypothesis (falsifiable): [HYPOTHESIS] Most current models produce confident false-positive structures on target-absent inputs at high rates, and the rate is unrelated to their benchmark Dice, i.e., leaderboards do not predict absence handling; strong correlation with Dice falsifies it.
- Why Important: Hallucinated organs in post-surgical patients are a direct clinical hazard invisible to standard evaluation.
- Why Possibly Novel: Absence-conditioned evaluation as a first-class benchmark axis is largely missing in medical segmentation.
- Minimal Experiment: Assemble target-absent cases (post-nephrectomy scans for kidney models, etc.); measure false-positive volume; correlate with benchmark scores.
- Main Risk: Absence cases are scarce; augment with anatomically valid crops that exclude the organ.
- Research Cluster tag: MED-SEG

### IDEA-A-0053
- Idea: Anisotropy sensitivity: quantify segmentation degradation as a function of through-plane voxel spacing, decoupled from in-plane resolution, to derive per-organ minimum-spacing specifications.
- Problem: [KNOWN FACT] Clinical scans vary widely in slice thickness; models are trained on mixed anisotropy without published operating ranges.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Per-organ error grows smoothly and predictably with through-plane spacing until a structure-specific critical spacing where error jumps (structure thinner than spacing); no critical-spacing behavior falsifies it.
- Why Important: A validated spacing spec tells clinics which protocols are compatible with which models — deployment guidance, not a new method.
- Why Possibly Novel: Resolution studies exist in-plane; controlled through-plane downsampling with critical-point analysis per organ is rarer.
- Minimal Experiment: Downsample thin-slice datasets to synthetic spacings; evaluate fixed models; locate critical spacing per organ.
- Main Risk: Synthetic downsampling ignores reconstruction-kernel effects; validate on natively thick-slice scans of same patients where possible.
- Research Cluster tag: MED-SEG

### IDEA-A-0054
- Idea: Characterize the noise structure of report-derived weak labels (masks seeded from radiology-report findings) and test whether it violates the random-noise assumptions of noise-robust training analyses.
- Problem: [KNOWN FACT] Reports mention findings without spatial precision; weak labels derived from them carry structured, location-correlated noise.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Report-derived label noise is spatially and semantically structured (systematically missing satellite lesions, biased toward the largest finding), and its structure measurably differs from the uniform/class-conditional noise assumed by common analyses; unstructured noise falsifies it.
- Why Important: If noise structure differs, conclusions from synthetic-noise robustness studies do not transfer to the weak-label setting hospitals actually face.
- Why Possibly Novel: Weak-label noise is usually simulated; direct measurement of real report-derived noise structure is scarce.
- Minimal Experiment: On a dataset with both full masks and reports, derive weak labels from reports; empirically characterize the noise (miss patterns, size bias); compare to synthetic-noise statistics.
- Main Risk: Report parsing quality confounds; use datasets with structured findings fields.
- Research Cluster tag: MED-SEG

### IDEA-A-0055
- Idea: Quantify contour-convention leakage: models trained on datasets following different clinical contouring guidelines learn dataset-specific boundary conventions that masquerade as accuracy differences.
- Problem: [KNOWN FACT] Clinical guidelines for contouring the "same" structure differ across institutions and protocols (e.g., inclusion of vessels or capsule).
- Core Hypothesis (falsifiable): [HYPOTHESIS] A model trained on protocol-A data evaluated on protocol-B data shows errors concentrated exactly at guideline-divergence regions (predictable a priori from the guideline text), not uniformly; uniform error distribution falsifies it.
- Why Important: Distinguishes true model error from convention mismatch — critical before claiming cross-institution generalization failure.
- Why Possibly Novel: Guideline-difference regions as a predicted error map is a concrete, testable bridge between clinical documents and model behavior.
- Minimal Experiment: Pick a structure with two documented conventions; annotate divergence regions from the guideline texts; test error concentration of cross-protocol models in those regions.
- Main Risk: Requires clinical collaborator to formalize guideline differences; scope to one well-documented structure.
- Research Cluster tag: MED-SEG

### IDEA-A-0056
- Idea: Measure the decision-level mismatch between voxel-overlap metrics and downstream clinical quantities: how often does the better-Dice model give the worse volumetry/response-assessment decision?
- Problem: [KNOWN FACT] Clinical use consumes derived quantities (volume, diameter, growth rate), not Dice; the metric-to-decision mapping is nonlinear and unstudied at scale.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Across model pairs, a meaningful fraction of "better Dice" comparisons invert at the decision level (volume threshold crossings, response categories), and inversion probability is predictable from lesion size; near-zero inversions falsify it.
- Why Important: If inversions are common, model selection by Dice actively harms clinical utility.
- Why Possibly Novel: Decision-level concordance analysis between segmentation metrics and clinical endpoints is rarely quantified across many models.
- Minimal Experiment: For several public checkpoints on a lesion dataset, compute Dice and derived clinical quantities; count decision inversions across model pairs.
- Main Risk: Clinical decision rules vary; use one published response-criteria framework and state it explicitly.
- Research Cluster tag: MED-SEG

### IDEA-A-0057
- Idea: Failure taxonomy under metal/implant artifacts: characterize whether artifact-region failures are contained (local) or propagate to anatomically distant structures in the same scan.
- Problem: [KNOWN FACT] Metal implants produce streak artifacts in CT; effect on segmentation is assumed local but never delimited.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Segmentation error from metal artifacts extends measurably beyond the visually corrupted region (via context effects), with error at artifact-free distant organs elevated relative to implant-free matched controls; strictly local error falsifies it.
- Why Important: If corruption propagates, "just mask out artifact regions" QA policies are insufficient.
- Why Possibly Novel: Spatial propagation analysis of artifact-induced error (rather than exclusion of artifact cases) is uncommon.
- Minimal Experiment: Match implant vs non-implant scans on demographics; compare error on distant organs; map error vs distance-to-artifact curves.
- Main Risk: Implant patients differ clinically; strengthen matching or use pre/post-implant longitudinal pairs.
- Research Cluster tag: MED-SEG

### IDEA-A-0058
- Idea: Treat contrast-agent phase (non-contrast/arterial/venous/delayed) as a first-class domain-shift axis and measure per-organ phase-transfer matrices for fixed models.
- Problem: [KNOWN FACT] Enhancement phase radically changes organ appearance; datasets mix phases inconsistently and models' phase-transfer behavior is undocumented.
- Core Hypothesis (falsifiable): [HYPOTHESIS] The phase-transfer performance matrix is strongly asymmetric (e.g., venous-trained models transfer to arterial worse than the reverse) and consistent across architectures, indicating a data property rather than a model property; symmetric or architecture-specific transfer falsifies it.
- Why Important: Phase labels exist in scan metadata; a validated transfer matrix converts free metadata into deployment safety rules.
- Why Possibly Novel: Phase is usually a nuisance variable; making it the measured axis with full transfer matrices is a new systematic result.
- Minimal Experiment: Split a multi-phase dataset by phase; train/evaluate all phase pairs with one fixed recipe; report the transfer matrix across 2 architectures.
- Main Risk: Phase labels in metadata are noisy; verify with an automatic phase classifier and manual spot checks.
- Research Cluster tag: MED-SEG

### IDEA-A-0059
- Idea: Pediatric shift beyond scale: test whether rescaling adult-trained models' inputs to match pediatric organ sizes closes the pediatric performance gap, isolating what is size vs what is developmental appearance.
- Problem: [KNOWN FACT] Pediatric imaging is underrepresented; the gap is attributed vaguely to "anatomy differences" without decomposition.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Size-matching alone recovers only a minority of the pediatric gap; the remainder correlates with age-dependent tissue-contrast differences, implying developmental appearance is the dominant factor; full recovery from rescaling falsifies it.
- Why Important: Determines whether pediatric performance needs pediatric data (expensive, ethically constrained) or just input-scale handling.
- Why Possibly Novel: A controlled size-vs-appearance decomposition for the pediatric gap appears missing.
- Minimal Experiment: Evaluate adult-trained models on pediatric scans at native and organ-size-matched scales; quantify recovered vs residual gap by age group.
- Main Risk: Pediatric data access; use existing public pediatric subsets and report their limits.
- Research Cluster tag: MED-SEG

### IDEA-A-0060
- Idea: Post-surgical hallucination census: measure how models behave on anatomy altered by surgery (resections, anastomoses, flaps) — do they reconstruct the pre-surgical atlas?
- Problem: [KNOWN FACT] Training data underrepresents operated anatomy; models may regress toward canonical anatomy priors.
- Core Hypothesis (falsifiable): [HYPOTHESIS] On post-operative scans, model errors are structured toward the canonical pre-surgical configuration (segmenting removed/displaced structures at atlas-expected locations) rather than random; unstructured error falsifies it.
- Why Important: Atlas-regression errors are precisely the ones that mislead surgical follow-up — the highest-stakes reading context.
- Why Possibly Novel: "Prior-driven hallucination" in medical segmentation is anecdotal; a structured census with directionality analysis is new.
- Minimal Experiment: Collect post-operative cases with known procedures; classify errors as atlas-consistent vs other; test the directionality statistically.
- Main Risk: Small cohorts per procedure type; aggregate across procedures with hierarchical statistics.
- Research Cluster tag: MED-SEG

### IDEA-A-0061
- Idea: Characterize registration-propagated label noise: boundary error of atlas/registration-derived labels correlates with local deformation magnitude, creating spatially structured supervision noise.
- Problem: [KNOWN FACT] Many medical labels are produced by propagating contours via image registration; registration is least reliable exactly where anatomy varies most.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Label error in registration-derived datasets is predictable from the local deformation-field statistics, and models trained on such labels inherit errors concentrated in high-deformation regions; spatially uniform inherited error falsifies it.
- Why Important: Identifies which parts of "ground truth" are trustworthy — changes both training-data weighting and evaluation interpretation.
- Why Possibly Novel: Supervision noise is usually modeled as label-flip noise; a geometry-correlated noise model grounded in the labeling process is new.
- Minimal Experiment: On a dataset with both manual and registration-propagated labels, regress label disagreement on deformation statistics; test whether trained-model errors co-locate.
- Main Risk: Needs paired manual labels; scope to one anatomy where both exist.
- Research Cluster tag: MED-SEG

### IDEA-A-0062
- Idea: Dose-response robustness curve: quantify segmentation degradation as a continuous function of CT radiation dose (noise level), producing per-structure minimum-dose operating specs.
- Problem: [KNOWN FACT] Low-dose protocols increase noise; models are deployed across dose regimes without validated operating ranges.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Degradation vs dose follows a smooth curve with a structure-specific knee, and the knee is predicted by the structure's native contrast-to-noise ratio; kneeless or unpredictable curves falsify it.
- Why Important: Gives clinics a physics-grounded rule for when a model's output should be distrusted, per protocol.
- Why Possibly Novel: Noise-robustness studies rarely connect the breakdown point to a measurable per-structure image property.
- Minimal Experiment: Use dose-simulation (noise insertion validated in the CT literature) across dose levels; evaluate fixed models per structure; fit knee-point vs contrast-to-noise.
- Main Risk: Simulated noise fidelity; validate against a small real low-dose/normal-dose paired set.
- Research Cluster tag: MED-SEG

### IDEA-A-0063
- Idea: Motion-artifact failure signatures in MR: test whether motion-corrupted inputs produce a recognizable, detectable error pattern (ghost-aligned errors) usable as an automatic QA flag.
- Problem: [KNOWN FACT] MR motion artifacts create ghosting along the phase-encode direction; segmentation behavior under such structured corruption is uncharacterized.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Segmentation errors under motion are anisotropic and aligned with the phase-encode axis, making motion-induced failure detectable from the error/prediction geometry alone; isotropic errors falsify it.
- Why Important: A signature detectable without ground truth enables automatic rejection of motion-corrupted studies.
- Why Possibly Novel: Uses the physics of the artifact to predict the geometry of the failure — a testable physics-to-failure link.
- Minimal Experiment: Simulate/collect motion-corrupted MR with known phase-encode axis; measure error anisotropy; build and validate a detector on held-out data.
- Main Risk: Real motion is more varied than simulation; include a real corrupted cohort.
- Research Cluster tag: MED-SEG

### IDEA-A-0064
- Idea: Quantify how much 3D context each organ actually needs: context-ablation curves (input extent vs accuracy) to test the assumption that "more 3D context is better."
- Problem: [KNOWN FACT] Pipelines choose 2D/2.5D/3D inputs by convention; the per-structure context requirement has not been measured as a curve.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Context-need is highly structure-specific: some organs saturate with a few slices while others require full-volume context, and the saturation point is predictable from anatomical ambiguity (number of confusable look-alike structures); uniform saturation falsifies it.
- Why Important: Grounds an expensive engineering choice (memory, latency) in measured need rather than habit.
- Why Possibly Novel: Context is usually an architecture debate; converting it into a measured per-structure requirement curve is a different kind of result.
- Minimal Experiment: Train/evaluate one fixed recipe at multiple input extents per organ; plot accuracy vs extent; correlate saturation point with confusability measures.
- Main Risk: Conclusions could be recipe-specific; replicate with a second recipe.
- Research Cluster tag: MED-SEG

### IDEA-A-0065
- Idea: Zero-shot failure census on rare anatomical variants (situs inversus, horseshoe kidney, accessory organs): do models fail loudly or silently on rule-breaking anatomy?
- Problem: [KNOWN FACT] Rare variants are nearly absent from training sets; their frequency in deployment is low but nonzero and clinically critical.
- Core Hypothesis (falsifiable): [HYPOTHESIS] On variant anatomy, models produce confident, atlas-conformant (and therefore wrong) outputs rather than degraded/uncertain outputs — i.e., silent failure dominates; predominantly low-confidence outputs falsify it.
- Why Important: Silent confident failure on variants is the worst-case safety profile; quantifying it motivates variant-aware QA.
- Why Possibly Novel: Variant anatomy is discussed clinically but almost never assembled into a model-evaluation cohort.
- Minimal Experiment: Assemble a small variant cohort from public case repositories; run standard models; classify outputs by confidence and atlas-conformity.
- Main Risk: Tiny cohort sizes; report as a structured case series with per-case analysis, not aggregate claims.
- Research Cluster tag: MED-SEG

### IDEA-A-0066
- Idea: Validate label-free deployment monitors for medical segmentation across hospitals: which self-assessment signals (consistency checks, shape plausibility) actually track true error across sites?
- Problem: [KNOWN FACT] Deployed models drift as scanners/protocols change; hospitals cannot re-annotate continuously to monitor quality.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A small set of label-free signals maintains a strong correlation with true Dice across at least several external sites, while most proposed signals fail cross-site; universal cross-site failure of all signals also falsifies the practical premise.
- Why Important: Regulators and hospitals need validated monitoring; the field lacks head-to-head cross-site evidence.
- Why Possibly Novel: Monitoring signals are proposed individually; a standardized cross-site bake-off with failure analysis is missing.
- Minimal Experiment: Evaluate several published label-free QA signals on multi-site data with ground truth; rank by cross-site correlation stability.
- Main Risk: Multi-site labeled data is scarce; use federated-style evaluation with site-held-out protocols.
- Research Cluster tag: MED-SEG

### IDEA-A-0067
- Idea: Prevalence-shift calibration: measure how segmentation-derived screening decisions degrade when disease prevalence differs between development and deployment populations.
- Problem: [KNOWN FACT] Development datasets are enriched for positives; screening populations have low prevalence, changing the meaning of any fixed operating point.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Detection-from-segmentation pipelines lose most of their positive predictive value under realistic prevalence shift, and the loss is predictable from the enrichment ratio alone; unpredictable or negligible loss falsifies it.
- Why Important: A predictable relationship allows correcting operating points analytically instead of recollecting data.
- Why Possibly Novel: Prevalence effects are classic in epidemiology but rarely propagated through modern segmentation-based pipelines quantitatively.
- Minimal Experiment: Subsample a labeled dataset to multiple synthetic prevalences; measure decision metrics vs prevalence; compare against the analytic prediction.
- Main Risk: Subsampling changes case-mix beyond prevalence; stratify sampling by severity.
- Research Cluster tag: MED-SEG

### IDEA-A-0068
- Idea: Test whether consensus-fusion ground truth (label fusion across raters) creates masks with statistical properties no individual rater produces, and whether models trained on fused labels inherit this "committee style."
- Problem: [KNOWN FACT] Multi-rater labels are often fused into a single consensus mask for training; fusion smooths and reshapes boundaries.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Fused masks are measurably smoother/more convex than any single rater's masks, and models trained on them produce boundaries closer to the fusion style than to any human's style; no stylistic divergence falsifies it.
- Why Important: If models learn a nonexistent committee style, comparisons against individual clinicians are systematically confounded.
- Why Possibly Novel: Fusion is treated as noise reduction; its role as a style generator with downstream behavioral consequences is untested.
- Minimal Experiment: Compare shape statistics of fused vs individual-rater masks; train paired models on fused vs single-rater labels; compare output styles against both.
- Main Risk: Style metrics must be pre-specified to avoid fishing; preregister the shape-statistic battery.
- Research Cluster tag: MED-SEG

### IDEA-A-0069
- Idea: Test whether the reliability ordering of prompt types (box vs point vs scribble) inverts on medical images relative to natural images for promptable segmenters.
- Problem: [KNOWN FACT] Prompt-type guidance for promptable models comes from natural-image studies; medical structures differ in shape statistics (elongated vessels, nested structures).
- Core Hypothesis (falsifiable): [HYPOTHESIS] For at least some structure families, the best prompt type on medical images differs from the natural-image best, in a way predictable from structure elongation and nesting; identical orderings everywhere falsify it.
- Why Important: Prompting policy is the cheapest deployment knob; an inversion result would immediately change annotation-tool defaults.
- Why Possibly Novel: Prompt-type studies exist per-domain; a cross-domain ordering-inversion analysis with shape-statistic predictors is new.
- Minimal Experiment: Evaluate all prompt types on matched structure families across natural and medical datasets; test ordering consistency and fit predictors.
- Main Risk: Confounds from annotation quality differences; use identical evaluation protocols and multiple datasets per domain.
- Research Cluster tag: MED-SEG

### IDEA-A-0070
- Idea: Interface-level evaluation: measure medical segmentation error separately for each organ-to-organ interface, testing whether failures concentrate on a few specific adjacency interfaces.
- Problem: [KNOWN FACT] Organ-level Dice hides where along the boundary the error lives; adjacent-organ interfaces differ hugely in contrast.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A majority of boundary error mass concentrates on a small, consistent subset of interfaces (e.g., organ pairs with matched intensity), stable across models and datasets; evenly spread error falsifies it.
- Why Important: If error is interface-concentrated, targeted data collection at those interfaces beats global dataset growth.
- Why Possibly Novel: Interface-resolved error accounting (a boundary-adjacency matrix of error) is not part of standard evaluation.
- Minimal Experiment: For multi-organ datasets, assign boundary errors to interface labels; build error-by-interface matrices for several models; test concentration and cross-model consistency.
- Main Risk: Interface assignment near triple-junctions is ambiguous; define assignment rules precisely.
- Research Cluster tag: MED-SEG

### IDEA-A-0071
- Idea: Site-fingerprint shortcut detection in federated/multi-site training: test whether models exploit scanner/site-identifiable features instead of anatomy.
- Problem: [KNOWN FACT] Multi-site medical data carries site-specific signal (noise texture, reconstruction kernels) that models can detect; whether segmentation models use it as a shortcut is unresolved.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A model's segmentation behavior measurably changes when site-fingerprint features are neutralized (fingerprint-randomized inputs), revealing shortcut reliance; unchanged behavior falsifies it.
- Why Important: Shortcut reliance on site fingerprints would explain sudden failures at new hospitals despite good multi-site validation.
- Why Possibly Novel: Site-classification leakage is documented; the causal test of whether segmentation depends on it is missing.
- Minimal Experiment: Train a site classifier to identify fingerprint features; construct fingerprint-neutralized test images; compare fixed-model outputs before/after neutralization.
- Main Risk: Neutralization may distort anatomy-relevant signal; include anatomy-preservation checks.
- Research Cluster tag: MED-SEG

### IDEA-A-0072
- Idea: Test-retest benchmark: measure segmentation stability on same-patient, same-scanner, short-interval repeat scans, establishing a necessary-condition reliability floor that current benchmarks never test.
- Problem: [KNOWN FACT] Clinical measurements require test-retest reliability; segmentation models are never evaluated on repeat-scan stability.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Model output variability across clinically identical repeat scans is a large fraction of the biological change models are meant to detect (e.g., tumor growth thresholds), for at least some structures; negligible variability falsifies it.
- Why Important: If retest noise rivals the signal of interest, longitudinal clinical use is invalid regardless of Dice.
- Why Possibly Novel: Test-retest is standard in quantitative imaging but absent from segmentation-model evaluation practice.
- Minimal Experiment: Use public repeat-scan cohorts; run fixed models on both scans; report volume/boundary variability against clinical change thresholds.
- Main Risk: Repeat-scan public data is limited; scope to structures with available cohorts.
- Research Cluster tag: MED-SEG

### IDEA-A-0073
- Idea: Measure whether mixing modalities (CT and MR) during medical pretraining degrades per-modality boundary precision relative to modality-pure pretraining at matched data budgets.
- Problem: [KNOWN FACT] Medical foundation models increasingly mix modalities in pretraining; the per-modality cost/benefit at the boundary level is unquantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] At matched budgets, mixed-modality pretraining trades boundary precision for breadth: region metrics stay comparable while boundary metrics degrade per modality; no boundary-specific tradeoff falsifies it.
- Why Important: Guides the modality-mixture decision for the next generation of medical pretraining runs.
- Why Possibly Novel: Mixture effects are usually reported as a single downstream number; boundary-resolved cost accounting is new.
- Minimal Experiment: Pretrain small models on pure vs mixed corpora at matched size; evaluate downstream with region and boundary metrics per modality.
- Main Risk: Small-scale pretraining may not extrapolate; report as scale-limited evidence with scaling checks at two budgets.
- Research Cluster tag: MED-SEG

### IDEA-A-0074
- Idea: Audit ground-truth protocol divergence for intratumoral subregions (necrosis, edema, enhancing rim): quantify how much apparent model disagreement across datasets is protocol disagreement.
- Problem: [KNOWN FACT] Tumor-subregion definitions vary across annotation protocols; datasets are treated as interchangeable when benchmarking.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A model trained on dataset A and evaluated on dataset B shows subregion errors that reproduce documented protocol differences (systematic inclusion/exclusion patterns), not random degradation; unstructured cross-dataset error falsifies it.
- Why Important: Prevents the field from chasing "generalization failures" that are actually definition mismatches.
- Why Possibly Novel: Protocol-difference forensics via model-error structure is a new use of trained models as measurement probes.
- Minimal Experiment: Cross-evaluate subregion models between two datasets with documented protocol differences; test whether error direction matches the documented differences.
- Main Risk: Protocols are incompletely documented; involve dataset authors for verification where possible.
- Research Cluster tag: MED-SEG

### IDEA-A-0075
- Idea: Out-of-protocol input behavior: characterize what medical segmentation models do when given the wrong sequence/protocol entirely (T1 model fed T2, brain model fed abdomen).
- Problem: [KNOWN FACT] Deployment systems occasionally route wrong series to models; model behavior on categorically wrong input is undocumented.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Models produce plausible-looking, high-confidence masks on categorically wrong inputs at high rates (silent failure), and simple input-verification checks catch most such cases; predominantly degenerate/low-confidence outputs falsify it.
- Why Important: Wrong-series routing is a realistic hospital IT failure; its consequence severity should be measured, not assumed.
- Why Possibly Novel: Robustness studies stay within-protocol; categorical input error is an unstudied but operationally common failure.
- Minimal Experiment: Feed systematically mismatched series to fixed models; classify outputs; evaluate cheap input-verification gates.
- Main Risk: Findings vary by model family; test several public models to avoid single-model conclusions.
- Research Cluster tag: MED-SEG

### IDEA-A-0076
- Idea: Annotation-fatigue drift: test whether label quality within public datasets degrades as a function of annotation order/session position, using timestamps or ordering metadata.
- Problem: [KNOWN FACT] Human performance degrades over long annotation sessions; whether this leaves measurable structure in public medical datasets is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Cases annotated later in sessions show measurably different label statistics (simplified boundaries, fewer vertices, faster acceptance of model pre-segmentations) and higher model-vs-label disagreement; no order effect falsifies it.
- Why Important: Fatigue drift would be a correctable, previously invisible noise source in ground truth.
- Why Possibly Novel: Fatigue is studied in radiology reading; its imprint on segmentation datasets has not been forensically tested.
- Minimal Experiment: Obtain ordering metadata for one or more datasets; regress label-complexity statistics and model-disagreement on session position.
- Main Risk: Ordering metadata often unavailable; partner with dataset creators or use datasets with public annotation logs.
- Research Cluster tag: MED-SEG

### IDEA-A-0077
- Idea: Stain-normalization illusion test in histopathology: does color normalization improve actual segmentation transfer, or only the visual/statistical match while errors persist?
- Problem: [KNOWN FACT] Stain variation is a dominant visible shift in histopathology; normalization methods optimize color similarity, not task performance, and the causal link is often assumed.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Across sites, the improvement in color-distribution match from normalization is only weakly correlated with improvement in segmentation transfer, revealing that color is not the binding constraint; strong correlation falsifies it.
- Why Important: The field spends heavily on stain normalization; a weak-link result would redirect effort to the true constraint.
- Why Possibly Novel: Decouples the optimization target (color match) from the goal (transfer) with a correlation-across-sites design rather than a single before/after comparison.
- Minimal Experiment: For multiple site pairs, apply several normalizers; plot Δcolor-match vs Δtransfer-performance across pairs; test the correlation.
- Main Risk: Few multi-site labeled histo datasets; use existing public multi-center challenges.
- Research Cluster tag: MED-SEG

### IDEA-A-0078
- Idea: Quantify operator-induced domain shift in ultrasound: is probe-handling variability (angle, pressure, gain) a larger shift axis than patient variability for segmentation models?
- Problem: [KNOWN FACT] Ultrasound appearance depends strongly on the operator; datasets rarely control or record operator factors.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Variance-component analysis attributes more segmentation-output variance to operator factors than to patient identity for common exam types; patient-dominated variance falsifies it.
- Why Important: If the operator dominates, data collection should sample operators, not just patients — a reversal of current practice.
- Why Possibly Novel: Operator variability is acknowledged clinically but has not been decomposed as a variance component for segmentation models.
- Minimal Experiment: Collect a small factorial dataset (several operators × several subjects); run fixed models; perform variance-component decomposition.
- Main Risk: Requires new data collection; keep the factorial design tiny (e.g., 5×5) and preregistered.
- Research Cluster tag: MED-SEG

### IDEA-A-0079
- Idea: Longitudinal-consistency benchmark: evaluate whether models segment the same patient consistently across time points, since inconsistency corrupts growth-rate estimates even when each time point looks accurate.
- Problem: [KNOWN FACT] Longitudinal change is a primary clinical endpoint; per-scan metrics do not measure cross-time consistency of the same model.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Cross-time inconsistency (random re-segmentation differences on stable anatomy) contributes error to growth estimates comparable to or larger than per-scan error, for at least some structures; negligible contribution falsifies it.
- Why Important: Growth-rate errors change treatment decisions; this failure axis is invisible to every current leaderboard.
- Why Possibly Novel: Longitudinal consistency as a first-class evaluated property (with stable-anatomy controls) is missing from segmentation benchmarks.
- Minimal Experiment: On longitudinal cohorts with stable structures (verified unchanged), measure model output variation across time points; propagate to growth-estimate error.
- Main Risk: Verifying true stability is hard; use structures with strong prior stability (e.g., fully calcified findings) as controls.
- Research Cluster tag: MED-SEG

### IDEA-A-0080
- Idea: Preprocessing side-effects audit: measure how privacy preprocessing (defacing, skull-stripping) changes segmentation of structures far from the removed region.
- Problem: [KNOWN FACT] Public neuroimaging data is routinely defaced for privacy; models consume these images assuming the modification is inert elsewhere.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Defacing/stripping measurably changes model outputs on anatomically distant structures (via global context effects), with effect size varying by model family; strictly local effects falsify it.
- Why Important: If privacy preprocessing perturbs distant outputs, results on public defaced data misestimate performance on clinical (non-defaced) data.
- Why Possibly Novel: Defacing effects are studied for morphometry pipelines; modern segmentation models' non-local sensitivity to it is untested.
- Minimal Experiment: Use datasets available in both defaced and original form (or deface locally); run fixed models on both; map output differences vs distance from the modified region.
- Main Risk: Access to non-defaced originals is restricted; use internal IRB-approved data or synthetic defacing on public non-human-identifiable scans.
- Research Cluster tag: MED-SEG

---

## Section 3 — Smoke / fire / transparent / ambiguous object segmentation (IDEA-A-0081 .. 0120)

### IDEA-A-0081
- Idea: Measure the annotator-agreement-vs-opacity curve for smoke masks to establish where the segmentation task itself stops being well-defined.
- Problem: [KNOWN FACT] Smoke has no crisp physical boundary; binary masks force annotators to draw a line whose placement is arbitrary at low opacity.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Inter-annotator agreement on smoke boundaries collapses below a characteristic local-opacity level, defining a measurable "task validity threshold"; agreement independent of opacity falsifies it.
- Why Important: Below the validity threshold, model "errors" are unmeasurable in principle — benchmarks should exclude or soft-weight those regions.
- Why Possibly Novel: Treats task well-posedness as an empirically measurable function of a physical variable (opacity), not a philosophical aside.
- Minimal Experiment: Have multiple annotators mask smoke on images with estimated opacity maps (from compositing or dual exposures); plot agreement vs local opacity; locate the collapse point.
- Main Risk: Opacity estimation from single images is rough; anchor with composited images where true alpha is known.
- Research Cluster tag: AMORPH

### IDEA-A-0082
- Idea: Reframe smoke segmentation as opacity (alpha-matte) regression and test whether binary-mask models systematically mispredict in exactly the regions where alpha is intermediate.
- Problem: [KNOWN FACT] Smoke is a volumetric scattering medium; a binary in/out decision discards the physically meaningful quantity (optical density).
- Core Hypothesis (falsifiable): [HYPOTHESIS] Binary-mask model errors concentrate almost entirely in intermediate-alpha regions (alpha between roughly 0.2 and 0.8 in composited ground truth), and error is near-zero elsewhere; errors uniform across alpha falsify it.
- Why Important: Would show the field is optimizing the wrong output type for an entire object class, redirecting dataset design.
- Why Possibly Novel: Alpha-matte framing exists for hair/fur matting; using composited alpha as diagnostic ground truth for smoke failure localization is new.
- Minimal Experiment: Composite real smoke plates (film industry alpha assets) over backgrounds; evaluate existing binary segmenters; histogram error mass by true alpha.
- Main Risk: Composited smoke may differ statistically from in-situ smoke; validate error patterns on a small real set with expert soft labels.
- Research Cluster tag: AMORPH

### IDEA-A-0083
- Idea: Threshold-conditioned segmentation as task definition: require models (and annotators) to produce masks at explicit opacity thresholds τ, and test whether conditioning removes most apparent disagreement.
- Problem: [KNOWN FACT] "Segment the smoke" is under-specified; different annotators implicitly use different opacity cutoffs, inflating both label noise and model error.
- Core Hypothesis (falsifiable): [HYPOTHESIS] When annotators are given an explicit τ (visualized via reference patches), inter-annotator agreement rises substantially at every τ, and a single model's outputs re-scored against τ-conditioned GT show much lower error variance; no improvement falsifies it.
- Why Important: A cheap protocol change could rescue an entire task family from ill-posedness.
- Why Possibly Novel: Conditioning the task on an explicit physical threshold, rather than proposing fuzzy metrics, is an unusual protocol-level intervention.
- Minimal Experiment: Re-annotate a smoke subset at three explicit τ levels with reference cards; compare agreement and model-error variance vs unconditioned annotation.
- Main Risk: Annotators may be unable to judge τ visually; pilot the reference-card protocol first.
- Research Cluster tag: AMORPH

### IDEA-A-0084
- Idea: Quantify fire-segmentation failure as a function of exposure clipping: emissive objects saturate sensors, destroying the texture cues models rely on.
- Problem: [KNOWN FACT] Fire is a light source; cameras clip highlights, so the flame interior is often pure white with no texture.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Segmentation error on flames rises predictably with the fraction of clipped pixels in the flame region, and errors concentrate at the clipped/unclipped transition; error independent of clipping falsifies it.
- Why Important: Suggests exposure bracketing or radiometric capture — a data-acquisition fix — rather than model changes.
- Why Possibly Novel: Fire benchmarks ignore radiometry; linking failure to a measurable sensor property (clipping fraction) is a new axis.
- Minimal Experiment: Capture or curate flame images with varying exposure (including bracketed sets); evaluate segmenters; regress error on clipping fraction.
- Main Risk: Exposure correlates with scene brightness overall; control with bracketed sets of the same scene.
- Research Cluster tag: AMORPH

### IDEA-A-0085
- Idea: Test whether video fire/smoke segmenters rely on temporal flicker signatures by evaluating on temporally shuffled and frame-rate-resampled versions of the same clips.
- Problem: [KNOWN FACT] Flames flicker at characteristic rates; video models could exploit this cue, but its causal contribution is unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Frame-shuffling (destroying temporal order but keeping frames) collapses video-model fire/smoke performance toward single-frame baselines, and performance varies systematically with frame-rate resampling; insensitivity to both falsifies reliance on flicker.
- Why Important: If flicker is load-bearing, models will fail on low-frame-rate CCTV — a deployment-critical prediction.
- Why Possibly Novel: Cue-ablation via temporal shuffling is used in action recognition; porting it to safety-critical amorphous segmentation is new.
- Minimal Experiment: Evaluate video segmenters on original, shuffled, and 2×/4× downsampled-frame-rate clips; compare against per-frame baselines.
- Main Risk: Shuffling breaks tracking assumptions in some models; include models designed per-frame as controls.
- Research Cluster tag: AMORPH

### IDEA-A-0086
- Idea: Confusion-structure prediction from physics: test whether the model confusion matrix among smoke/steam/fog/dust follows the ordering of their physical scattering properties (particle size, density).
- Problem: [KNOWN FACT] These aerosol classes are visually similar; whether learned models confuse them in a physics-predictable order is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Pairwise confusion rates are ordered by physical similarity (particle-size and scattering-regime distance) rather than by dataset co-occurrence statistics; dataset-statistics-ordered confusion falsifies the physics account.
- Why Important: Determines whether disambiguation needs physical cues (polarization, spectra) or just more balanced data.
- Why Possibly Novel: Puts a physical-similarity model and a data-statistics model in direct competition to explain a confusion matrix.
- Minimal Experiment: Assemble a labeled aerosol-class set; compute model confusion matrices; fit both physical-distance and co-occurrence predictors; compare fits.
- Main Risk: Class labels themselves are noisy (steam vs fog); use scenes with known source (kettle, fog machine, dust source).
- Research Cluster tag: AMORPH

### IDEA-A-0087
- Idea: Generalized background-dependence census for transparent object segmentation across model families: rank models by cross-backdrop consistency using a fixed physical rig.
- Problem: [KNOWN FACT] Transparent-object appearance is mostly transmitted background; models may segment "the region where the background looks distorted" rather than the object.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Cross-backdrop mask consistency varies widely across current models and correlates with their training-data diversity of backgrounds, not with their benchmark IoU; uniform consistency falsifies it.
- Why Important: Ranks models by a deployment-relevant invariance that benchmark IoU provably does not capture.
- Why Possibly Novel: A standardized physical consistency rig (same objects, systematically varied backdrops) as a community benchmark is missing.
- Minimal Experiment: Build a 20-object × 10-backdrop capture rig; evaluate several public models; publish consistency scores alongside standard IoU.
- Main Risk: Rig scale limits statistical power; complement with rendered scenes for scale, keeping the real rig as anchor.
- Research Cluster tag: AMORPH

### IDEA-A-0088
- Idea: Rim-localized evaluation for glass: test whether transparent-object failure is concentrated in the thin refractive rim, and define a rim-band metric that predicts downstream grasping/manipulation success better than whole-mask IoU.
- Problem: [KNOWN FACT] Glass boundaries appear as thin bands of refraction/specularity; whole-object IoU dilutes rim errors to insignificance.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Most transparent-object mask error mass lies within a narrow rim band, and rim-band accuracy predicts robotic-grasp success while whole-mask IoU does not; distributed error or no predictive gap falsifies it.
- Why Important: Would change both how transparent benchmarks are scored and what data (rim-focused) is worth collecting.
- Why Possibly Novel: Couples an error-localization claim to a downstream-utility validation (grasping), not just another metric proposal.
- Minimal Experiment: On a transparent-object dataset, compute error-by-distance-to-boundary histograms; if concentrated, correlate rim-band accuracy vs whole IoU with published grasp outcomes or a small robot trial.
- Main Risk: Grasp validation needs robotics access; a simulation-based proxy is an acceptable first step, stated as such.
- Research Cluster tag: AMORPH

### IDEA-A-0089
- Idea: Quantify how much transparent-object signal exists for free in depth-sensor invalid-pixel patterns, without any learning: invalid/NaN regions of consumer depth cameras as a zero-shot glass detector.
- Problem: [KNOWN FACT] Structured-light and ToF depth sensors commonly fail on transparent/specular surfaces, returning invalid pixels; this failure is itself information.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Invalid-pixel maps alone achieve non-trivial transparent-object localization (well above chance), and their union with an RGB model's output measurably improves detection at zero training cost; no localization signal falsifies it.
- Why Important: A hardware-artifact-as-signal result would give robotics an immediately deployable free cue.
- Why Possibly Novel: Sensor failure as a first-class feature (rather than noise to be inpainted) inverts the standard cleanup mindset.
- Minimal Experiment: On RGB-D datasets containing glass, measure localization metrics of raw invalid-pixel maps; combine with model outputs by simple union/intersection rules; report deltas.
- Main Risk: Invalid pixels have many other causes (range, absorption); characterize the false-positive profile honestly.
- Research Cluster tag: AMORPH

### IDEA-A-0090
- Idea: Specular highlights on glass: determine experimentally whether highlights act as anchors (helping models find glass) or distractors (fragmenting masks), using controlled relighting.
- Problem: [KNOWN FACT] Highlights are the most visible feature of glass, but their causal role in segmentation success is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Removing highlights (cross-polarized capture) degrades glass segmentation substantially, showing highlights are load-bearing anchors; improvement or no change under highlight removal falsifies it.
- Why Important: Determines whether glossy-surface data augmentation should preserve or randomize highlights, and predicts failure under diffuse lighting.
- Why Possibly Novel: Cross-polarized paired capture as a causal intervention for segmentation cues appears unused.
- Minimal Experiment: Capture paired highlight/no-highlight images of glass scenes via polarization filtering; evaluate fixed models on both; compare per-object.
- Main Risk: Polarization also alters other appearance aspects; include non-glass control objects to isolate the effect.
- Research Cluster tag: AMORPH

### IDEA-A-0091
- Idea: Mirror-versus-window confusion census: measure how often segmentation models treat reflected scenes as real scene content, and whether reflection errors have a detectable geometric signature.
- Problem: [KNOWN FACT] Mirrors and windows present visually coherent scenes that are not physically present; models lacking scene-geometry reasoning may segment the virtual content.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Reflection-region errors are systematic (models segment virtual objects at high rates) and carry a geometric signature (left-right flip consistency with a visible source object) enabling automatic detection; rare or signature-free errors falsify it.
- Why Important: Virtual-object segmentation causes phantom obstacles in robotics/AV — a concrete safety failure.
- Why Possibly Novel: Mirror datasets exist; the flip-consistency signature as an automatic phantom detector is a new twist.
- Minimal Experiment: On mirror-containing scenes, count virtual-object segmentations; test a flip-matching detector against ground truth mirror annotations.
- Main Risk: Flip-matching needs the source object visible; report coverage of the detector honestly.
- Research Cluster tag: AMORPH

### IDEA-A-0092
- Idea: Annotation-protocol experiment for water surfaces: quantify how much of "water segmentation difficulty" is annotator inconsistency about what counts as the water boundary (wet sand, foam, reflections).
- Problem: [KNOWN FACT] Water boundaries (shoreline, foam, spray) are transitional zones; datasets annotate them inconsistently.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A written boundary-decision protocol (explicit rules for foam, wet regions, reflections) reduces inter-annotator variance on water boundaries by a large factor, and re-scoring models against protocol-consistent GT changes their ranking; no variance reduction falsifies it.
- Why Important: Flood-monitoring and maritime systems depend on water boundaries; label inconsistency directly corrupts their evaluation.
- Why Possibly Novel: Protocol-controlled re-annotation as an experimental manipulation (not just quality control) is rare in segmentation.
- Minimal Experiment: Re-annotate 200 water-boundary images with and without the explicit protocol (different annotator groups); compare variance and model rankings.
- Main Risk: Protocol may not cover all cases; iterate the protocol once and version it.
- Research Cluster tag: AMORPH

### IDEA-A-0093
- Idea: Fractal-boundary metric breakdown: test whether standard boundary metrics become resolution-unstable on scale-free boundaries (clouds, foliage, coastline-like edges), making cross-resolution comparisons invalid.
- Problem: [KNOWN FACT] Some natural boundaries are approximately fractal — measured length grows with resolution; boundary metrics assume a well-defined boundary length.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For objects with high boundary fractal dimension, boundary-F-score rankings of the same model pairs flip across evaluation resolutions, while low-fractal objects give stable rankings; resolution-stable rankings everywhere falsify it.
- Why Important: If rankings depend on evaluation resolution for a whole object class, published comparisons on such classes are unreliable.
- Why Possibly Novel: Importing fractal-dimension analysis into segmentation-metric validity is an unusual cross-disciplinary move.
- Minimal Experiment: Estimate boundary fractal dimension per object; evaluate model pairs at 3 resolutions; measure ranking stability vs fractal dimension.
- Main Risk: Fractal-dimension estimation is noisy at image scales; use robust estimators and report uncertainty.
- Research Cluster tag: AMORPH

### IDEA-A-0094
- Idea: Shadow-versus-object cue isolation: measure whether segmentation models can distinguish attached shadows from dark objects when shape cues are removed, using controlled shadow photography.
- Problem: [KNOWN FACT] Shadows produce strong boundaries that are not object boundaries; in low light, shadow-object confusion is a plausible but unmeasured failure driver.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Models include shadow regions in object masks at rates that increase as luminance contrast between shadow and object decreases, and this inclusion is not reduced by object familiarity; contrast-independent behavior falsifies it.
- Why Important: Quantifies a failure that corrupts area estimates in surveillance and agricultural monitoring every day at dusk.
- Why Possibly Novel: Controlled same-scene shadow manipulation (moving light source) as a segmentation probe is rarely done.
- Minimal Experiment: Photograph objects with a movable light source creating graded shadow configurations; measure shadow-inclusion rate vs contrast and shadow geometry.
- Main Risk: Limited scene diversity; supplement with rendered scenes for coverage and keep real captures as anchors.
- Research Cluster tag: AMORPH

### IDEA-A-0095
- Idea: Event-based evaluation for deformable topology-changing objects (plastic bags, cloth in wind): replace per-frame mask metrics with topology-event accuracy (split/merge/tear detection).
- Problem: [KNOWN FACT] Per-frame IoU cannot express whether a model tracked a topology change correctly; deformables change topology constantly in video.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Models with similar frame-averaged IoU differ dramatically in topology-event accuracy, i.e., current metrics hide most of the behaviorally relevant differences on deformables; near-identical event accuracy falsifies it.
- Why Important: Robotics and cloth manipulation need topology correctness, not average overlap.
- Why Possibly Novel: Event-level scoring for segmentation (borrowed in spirit from event detection) is not part of any deformable benchmark.
- Minimal Experiment: Annotate topology events in deformable-object clips; score existing video segmenters on event detection vs frame IoU; compare discriminative power.
- Main Risk: Event annotation is subjective at fine scales; define event vocabulary and minimum-size thresholds precisely.
- Research Cluster tag: AMORPH

### IDEA-A-0096
- Idea: Effective-resolution limit of spray/splash segmentation: establish the droplet-size floor below which segmentation is information-theoretically meaningless and only density estimation is valid.
- Problem: [KNOWN FACT] Sprays consist of sub-pixel droplets; annotators and models both produce masks whose meaning is unclear below the resolution limit.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Below a measurable droplet-size-to-pixel ratio, human annotations of "spray region" become internally inconsistent (test-retest agreement collapse), while a density-field annotation protocol remains consistent; persistent binary-mask consistency falsifies it.
- Why Important: Defines the boundary between two task formulations (mask vs density), preventing meaningless benchmarks.
- Why Possibly Novel: Test-retest consistency as the criterion for task-formulation validity is a methodological contribution beyond sprays.
- Minimal Experiment: Have annotators label sprays twice (weeks apart) under mask and density protocols across droplet scales; compare self-agreement curves.
- Main Risk: Density protocols are unfamiliar to annotators; provide calibrated visual references and training.
- Research Cluster tag: AMORPH

### IDEA-A-0097
- Idea: Rank the causal factors of the synthetic-to-real gap for smoke by controlled rendering: which simulation dimension (density field realism, illumination coupling, motion dynamics, camera noise) buys the most transfer?
- Problem: [KNOWN FACT] Synthetic smoke is widely used for training because real labels are hard; the gap's factor structure is unknown, so simulation effort is unguided.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Illumination coupling (smoke correctly lit by the scene) accounts for more transfer gain than density-field fidelity or motion realism at matched rendering budgets; a different or flat factor ranking falsifies it.
- Why Important: A factor ranking converts simulation from guesswork into an engineering budget allocation.
- Why Possibly Novel: Factorial simulation studies exist for driving scenes; the smoke/participating-media version with segmentation endpoints appears absent.
- Minimal Experiment: Render smoke datasets in a factorial design (each factor at low/high fidelity); train identical models; evaluate all on a common real test set.
- Main Risk: Factor interactions may dominate main effects; the factorial design measures this — report interactions explicitly.
- Research Cluster tag: AMORPH

### IDEA-A-0098
- Idea: Physics-propagated sparse labels: validate whether advecting a few keyframe smoke masks along optical-flow/wind-field estimates produces training labels competitive with dense manual annotation.
- Problem: [KNOWN FACT] Dense video annotation of smoke is prohibitively expensive; smoke motion approximately follows the local flow field.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Labels propagated by flow-based advection from sparse keyframes retain enough fidelity that models trained on them reach within a small margin of models trained on dense manual labels; a large residual gap falsifies it.
- Why Important: Could reduce smoke-video labeling cost by an order of magnitude using only existing flow tools.
- Why Possibly Novel: Label propagation is common for rigid objects; exploiting the physics of passive transport for amorphous label propagation is largely untested.
- Minimal Experiment: On a densely labeled smoke video set, simulate sparse-keyframe labeling plus advection; train models on propagated vs dense labels; compare on held-out clips.
- Main Risk: Flow estimation fails in low-texture smoke cores; quantify propagation drift vs keyframe spacing.
- Research Cluster tag: AMORPH

### IDEA-A-0099
- Idea: Meta-evaluate fuzzy-boundary metrics: which soft/region/boundary metric best matches human quality judgments specifically on amorphous objects (smoke, hair, foliage)?
- Problem: [KNOWN FACT] Multiple metrics exist for soft or fuzzy segmentation; their agreement with human preference on amorphous classes has not been measured head-to-head.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Metric-human agreement differs substantially across metrics on amorphous objects (while agreeing on crisp objects), and no current metric exceeds a modest agreement ceiling, indicating headroom for measurement innovation; uniformly high agreement falsifies it.
- Why Important: Whatever the field optimizes is defined by the metric; a poorly aligned metric silently misdirects all methods.
- Why Possibly Novel: Human-judgment-anchored metric meta-evaluation is standard in image synthesis but missing for amorphous segmentation.
- Minimal Experiment: Collect pairwise human preferences over mask pairs on amorphous objects; compute each metric's agreement with the human majority; rank metrics with confidence intervals.
- Main Risk: Human preferences may be task-dependent (matting vs alarm); collect preferences under two stated use contexts.
- Research Cluster tag: AMORPH

### IDEA-A-0100
- Idea: Hard-negative taxonomy for fire detection false positives: build a structured census of what non-fire stimuli (sunsets, brake lights, reflective vests, foliage in wind) trigger fire segmenters and why.
- Problem: [KNOWN FACT] Fire alarm systems suffer false positives from fire-colored or flickering stimuli; the failure taxonomy is anecdotal, not measured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] False positives cluster into a small number of cue-defined families (chromatic-only, flicker-only, chromatic+motion), and family membership predicts which input transformation suppresses the error; unstructured false positives falsify it.
- Why Important: A validated taxonomy converts false-alarm engineering from whack-a-mole into targeted stimulus testing.
- Why Possibly Novel: Systematic hard-negative taxonomies with causal cue attribution are rare outside face/biometrics domains.
- Minimal Experiment: Assemble a negative-stimulus battery by family; measure per-family false-positive rates of public fire segmenters; test cue-specific suppressions (e.g., temporal shuffle) per family.
- Main Risk: Battery coverage bias; source negatives from real deployment false-alarm logs where obtainable.
- Research Cluster tag: AMORPH

### IDEA-A-0101
- Idea: Spectral-versus-spatial cue decomposition for white-smoke confusion: determine whether smoke/cloud/snow confusion is driven by color statistics or by spatial texture, via channel-scrambling probes.
- Problem: [KNOWN FACT] White smoke, clouds, and snowfields share color statistics; which cue models actually use to (fail to) separate them is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Scrambling spatial structure while preserving color statistics collapses class separation entirely, showing separation relies on texture; preserved separation under scrambling falsifies it.
- Why Important: Directs data collection: if texture is the separator, resolution matters more than spectral fidelity, and vice versa.
- Why Possibly Novel: Standard cue-ablation applied to a specific confusion triad that matters for wildfire monitoring.
- Minimal Experiment: Construct color-preserving texture scrambles and texture-preserving color remaps of smoke/cloud/snow patches; measure model discrimination under each ablation.
- Main Risk: Scrambles produce off-distribution inputs; include mild-scramble gradations.
- Research Cluster tag: AMORPH

### IDEA-A-0102
- Idea: Container-versus-content ambiguity for transparent vessels: census whether models prompted on a filled glass segment the vessel, the liquid, or an inconsistent mixture.
- Problem: [KNOWN FACT] A filled transparent container presents two nested "objects" occupying overlapping pixels; the intended target is prompt-ambiguous.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Model choice between vessel and content is systematically driven by fill level and liquid color rather than prompt position, revealing an uncontrolled bias; prompt-position-driven choice falsifies it.
- Why Important: Pouring/manipulation robotics needs to know which surface a mask refers to; an appearance-driven bias is a hidden hazard.
- Why Possibly Novel: Nested-transparent-object ambiguity as a measured bias (not just a hard case) is unexamined.
- Minimal Experiment: Photograph vessels across fill levels and liquid colors; prompt at fixed positions; classify outputs as vessel/content/mixture; fit predictors of the choice.
- Main Risk: GT for "correct" answer is intent-dependent; report conditional behavior rather than error rates.
- Research Cluster tag: AMORPH

### IDEA-A-0103
- Idea: Continuous-transparency tracking: use condensation/frost formation time-lapses to measure how segmentation behavior changes as a surface transitions continuously from transparent to opaque.
- Problem: [KNOWN FACT] Transparency is treated as a binary class; real surfaces traverse the continuum (fogging glass, icing windshields) and model behavior along it is unmapped.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Model outputs change discontinuously (a sudden flip from background-following to surface-following masks) at a characteristic opacity rather than smoothly, revealing an internal binary decision; smooth transition falsifies it.
- Why Important: Windshield/visor systems experience this transition daily; a discontinuous flip means unpredictable behavior mid-transition.
- Why Possibly Novel: Time-lapse of a physical transition as a probe of an internal representational boundary is a creative low-cost design.
- Minimal Experiment: Record condensation time-lapses on glass with reference backgrounds; run fixed models per frame; locate and characterize the behavioral transition.
- Main Risk: Condensation is spatially non-uniform; analyze per-region rather than per-frame.
- Research Cluster tag: AMORPH

### IDEA-A-0104
- Idea: Amodal completion feasibility for glass: test whether models (or humans) can consistently complete occluded transparent objects, establishing whether amodal transparent segmentation is a well-posed task.
- Problem: [KNOWN FACT] Amodal segmentation is established for opaque objects; for transparent objects the visible evidence is already weak, and the feasibility of amodal completion is unknown even for humans.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Human amodal completions of occluded glass agree with each other nearly as well as for opaque objects (the task is well-posed), while current models degrade disproportionately; human disagreement collapse falsifies task validity itself.
- Why Important: Prevents the community from building benchmarks for a task that may be ill-posed; or, if well-posed, opens a new task with a human baseline.
- Why Possibly Novel: Human-feasibility gating before benchmark construction is rarely done explicitly.
- Minimal Experiment: Collect human amodal annotations for occluded glass and matched opaque controls; compare inter-human agreement; evaluate any existing amodal models against the human envelope.
- Main Risk: Human performance depends on object familiarity; balance familiar and novel shapes.
- Research Cluster tag: AMORPH

### IDEA-A-0105
- Idea: Refraction-distortion as a measurable cue: quantify how much local background-distortion statistics correlate with true glass regions, establishing the ceiling for distortion-based glass evidence without training anything.
- Problem: [KNOWN FACT] Refraction warps the transmitted background; whether this signal is strong enough to support segmentation, and where it fails (thin glass, distant background), is unquantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A hand-computed local distortion statistic (from background-pattern deformation) achieves above-chance glass localization with performance predictable from glass curvature and background texture density; no correlation falsifies the cue's usefulness.
- Why Important: Establishes an evidence ceiling for a physical cue before anyone invests in learning from it.
- Why Possibly Novel: Cue-ceiling measurement (how much information a cue contains, model-free) is an underused methodology in segmentation.
- Minimal Experiment: On scenes with textured backgrounds and annotated glass, compute distortion statistics; report localization performance stratified by curvature and background texture.
- Main Risk: Distortion statistics need textured backgrounds; explicitly report the coverage limitation.
- Research Cluster tag: AMORPH

### IDEA-A-0106
- Idea: Polarization-augmented dataset study: measure the marginal value of adding a cheap polarization filter channel at capture time for transparent and specular segmentation, as a data-acquisition (not model) intervention.
- Problem: [KNOWN FACT] Polarization strongly interacts with specular reflection and transparency; consumer capture rarely records it, and its marginal task value is unquantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For matched scenes, models trained/evaluated with a polarization-derived channel show large gains specifically on transparent/specular classes and negligible gains elsewhere, quantifying a targeted acquisition dividend; uniform or no gains falsify it.
- Why Important: If a $20 filter buys a large class-specific gain, deployment guidance changes for robotics and inspection.
- Why Possibly Novel: Framed as an acquisition-economics study (cost per IoU point) rather than a sensor-fusion method paper.
- Minimal Experiment: Capture a paired RGB / RGB+polarization dataset of glass-rich scenes; train identical pipelines on each; report per-class deltas and cost accounting.
- Main Risk: Requires modest new data collection; keep scene count small but paired and public.
- Research Cluster tag: AMORPH

### IDEA-A-0107
- Idea: Prove the single-view ambiguity of smoke density: use multi-view captures to quantify how many distinct 3D density fields are consistent with one view, bounding what any single-view smoke segmenter can know.
- Problem: [KNOWN FACT] Volumetric scattering along a ray integrates density; different 3D distributions can produce identical single-view appearances.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Cross-view disagreement of independently computed single-view smoke masks is large and grows with plume depth complexity, empirically demonstrating a fundamental single-view information ceiling; small cross-view disagreement falsifies the practical relevance of the ambiguity.
- Why Important: Establishes which smoke applications require multi-view or active sensing on information-theoretic grounds — before more single-view methods are built.
- Why Possibly Novel: Empirical ambiguity quantification via multi-view consistency (rather than theoretical argument alone) is missing for smoke.
- Minimal Experiment: Capture smoke with a synchronized multi-camera rig; compute per-view masks/densities; measure cross-view consistency vs plume complexity.
- Main Risk: Rig access; a two-camera stereo version already tests the core claim.
- Research Cluster tag: AMORPH

### IDEA-A-0108
- Idea: Subpixel abundance framing for distant wildfire smoke: test whether pixel-mixture (abundance estimation) formulations describe distant-smoke ground truth better than binary masks in existing datasets.
- Problem: [KNOWN FACT] At kilometer distances, each pixel mixes smoke and background; remote-sensing has mixture models for this, but wildfire camera datasets use binary masks.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Re-annotating distant-smoke imagery with per-pixel abundance produces labels with higher inter-annotator reliability than binary masks, and abundance-trained models detect earlier (smaller) plumes at matched false-alarm rates; no reliability or earliness gain falsifies it.
- Why Important: Earlier wildfire detection is directly life-safety relevant; the task formulation may be the bottleneck, not the model.
- Why Possibly Novel: Imports the spectral-unmixing mindset into camera-based smoke detection as a task redefinition with measurable payoff.
- Minimal Experiment: Re-annotate a distant-smoke subset with abundance labels; compare annotator reliability; train matched models on both label types; compare detection latency curves.
- Main Risk: Abundance GT is subjective too; anchor with plumes of known source size/distance where available.
- Research Cluster tag: AMORPH

### IDEA-A-0109
- Idea: Night-fire dynamic-range study: decompose night fire segmentation failure into sensor dynamic-range limits vs model limits by evaluating on HDR-bracketed captures.
- Problem: [KNOWN FACT] Night fire scenes span extreme dynamic range (bright flame, dark surround); standard captures clip both ends, confounding sensor and model failure.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A large fraction of night-fire failure disappears when models receive tone-mapped HDR inputs, attributing failure primarily to capture rather than modeling; persistent failure on HDR inputs falsifies it.
- Why Important: If capture dominates, deployment budgets should buy HDR cameras rather than model development.
- Why Possibly Novel: Failure attribution between the sensor and the model via bracketed capture is rarely done for segmentation.
- Minimal Experiment: Capture bracketed night fire scenes; evaluate fixed models on single-exposure vs HDR tone-mapped versions; decompose the improvement.
- Main Risk: Tone-mapping choice matters; test several standard operators.
- Research Cluster tag: AMORPH

### IDEA-A-0110
- Idea: Establish gas-leak segmentation on optical gas imaging (OGI) infrared video as a benchmark domain, characterizing how its statistics differ from visible-light smoke and why visible-smoke models transfer or fail.
- Problem: [KNOWN FACT] Industrial gas leaks are imaged with specialized IR cameras; the computer-vision community lacks public benchmarks and failure characterizations for this safety-critical modality.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Visible-smoke-trained models transfer to OGI far worse than their corruption-robustness scores would predict, because the plume's appearance model (absorption vs scattering) differs fundamentally; accurate transfer prediction from standard robustness scores falsifies it.
- Why Important: Methane leak detection is an active environmental and industrial safety need; grounding it in measurable failure analysis attracts rigorous work.
- Why Possibly Novel: Positions a new domain via a transfer-prediction falsification test rather than just releasing data.
- Minimal Experiment: Assemble/curate available OGI clips; evaluate visible-smoke models; compare actual transfer against predictions from standard robustness metrics.
- Main Risk: Public OGI data is scarce; partner with industrial sources or use published demonstration clips with permission.
- Research Cluster tag: AMORPH

### IDEA-A-0111
- Idea: Dehazing-destroys-evidence test: measure whether dehazing preprocessing, intended to improve visibility, removes exactly the signal needed to segment smoke/haze itself.
- Problem: [KNOWN FACT] Dehazing is a common preprocessing step in outdoor pipelines; it is optimized to remove the phenomenon that smoke segmenters must detect.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Pipelines with dehazing preprocessing show substantially degraded smoke detection/segmentation at matched settings, and degradation scales with dehazing strength; no degradation falsifies it.
- Why Important: A common "image quality improvement" may be silently disabling safety functions in deployed systems.
- Why Possibly Novel: Preprocessing-goal conflicts (enhancement vs detection of the removed phenomenon) are rarely tested explicitly.
- Minimal Experiment: Evaluate smoke segmenters on original vs dehazed versions (several dehazers, several strengths) of smoke-positive and smoke-negative scenes; report detection deltas and false-alarm changes.
- Main Risk: Dehazers vary widely; use several representative public ones.
- Research Cluster tag: AMORPH

### IDEA-A-0112
- Idea: Keyframe-interpolation validity for smoke annotation: measure how quickly interpolated masks between human keyframes diverge from true smoke extent, as a function of keyframe spacing and wind conditions.
- Problem: [KNOWN FACT] Video annotation tools interpolate between keyframes; smoke deforms non-rigidly, so interpolation validity is unclear yet widely assumed.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Interpolation error grows superlinearly with keyframe spacing for smoke (unlike rigid objects), with a wind-speed-dependent rate, defining maximum valid keyframe spacing per condition; linear or slow growth falsifies it.
- Why Important: Provides annotation-tool guidance that directly controls dataset quality for all future smoke video datasets.
- Why Possibly Novel: Annotation-tool error models conditioned on physical scene variables are essentially absent.
- Minimal Experiment: On densely annotated smoke clips, simulate keyframe-only annotation at various spacings; measure interpolated-vs-true divergence; regress on optical-flow magnitude.
- Main Risk: Depends on the interpolation algorithm; test the 2–3 dominant tool behaviors.
- Research Cluster tag: AMORPH

### IDEA-A-0113
- Idea: Recover each dataset's implicit boundary-band width: estimate the effective uncertainty band annotators used when drawing amorphous boundaries, per dataset, and use it to normalize cross-dataset comparisons.
- Problem: [KNOWN FACT] Different datasets' annotators drew fuzzy boundaries with different implicit tolerances; cross-dataset metric comparisons ignore this.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A dataset-specific boundary-band width is recoverable from label statistics (e.g., boundary curvature spectra and multi-annotator subsets), and normalizing metrics by it reorders cross-dataset model comparisons; unrecoverable or non-reordering bands falsify it.
- Why Important: Makes cross-dataset claims about amorphous segmentation comparable for the first time.
- Why Possibly Novel: Treating annotation tolerance as a latent dataset parameter to be estimated is a fresh measurement idea.
- Minimal Experiment: Estimate band widths on datasets with partial multi-rater data; validate estimates on held-out raters; apply band-normalized scoring to existing results.
- Main Risk: Estimation may be confounded by true boundary complexity; validate on synthetic data with known bands first.
- Research Cluster tag: AMORPH

### IDEA-A-0114
- Idea: Stuff-thing hybrid taxonomy test: establish empirically where smoke-like classes fall on the countability spectrum by measuring which task formulation (instance, semantic, density) humans and models perform most consistently.
- Problem: [KNOWN FACT] Vision splits the world into countable "things" and mass-like "stuff"; smoke, fire, and spray sit awkwardly between, and each dataset picks a formulation arbitrarily.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For each amorphous class there is a measurable consistency ordering over task formulations (human test-retest and inter-rater), and the ordering differs across classes (fire more thing-like, haze more stuff-like); identical orderings falsify class-specific formulation needs.
- Why Important: Provides an evidence-based rule for how future datasets should formulate each amorphous class.
- Why Possibly Novel: Task-formulation selection by measured human consistency, per class, is a methodological contribution.
- Minimal Experiment: Annotate the same clips under three formulations for several amorphous classes; measure human consistency per class per formulation; rank.
- Main Risk: Annotator training effects; counterbalance formulation order across annotators.
- Research Cluster tag: AMORPH

### IDEA-A-0115
- Idea: Downstream-anchored evaluation: measure the correlation between smoke-segmentation IoU and actual alarm-decision quality (latency, false-alarm rate) to test whether IoU is a valid proxy in this domain.
- Problem: [KNOWN FACT] Smoke segmentation is usually a component of an alarm decision; the proxy validity of mask IoU for alarm quality is assumed, not measured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Above a modest IoU level, further IoU gains produce no measurable alarm-quality improvement (a proxy saturation point), and below it the correlation is strong; monotone tight coupling everywhere falsifies saturation.
- Why Important: A saturation result would stop the field from over-optimizing masks and redirect effort to the decision layer.
- Why Possibly Novel: Proxy-validity curves (component metric vs system metric) are rarely computed for segmentation-based systems.
- Minimal Experiment: Sweep segmentation quality (by model choice and degradation) inside a fixed alarm pipeline on labeled event videos; plot alarm metrics vs mask IoU.
- Main Risk: Results depend on the alarm logic; test two standard decision rules and report both.
- Research Cluster tag: AMORPH

### IDEA-A-0116
- Idea: Backlit-vegetation failure study: quantify segmentation degradation on translucent leaves/grass as a function of sun angle, isolating subsurface-scattering-driven appearance change.
- Problem: [KNOWN FACT] Vegetation is translucent; backlighting changes its appearance from surface-reflective to glow-like, a daily cyclic shift that datasets rarely stratify.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Segmentation error on vegetation exhibits a strong, reproducible dependence on relative sun angle (worst when backlit), with time-of-day acting as a hidden performance variable; angle-independent error falsifies it.
- Why Important: Agricultural and ecological monitoring runs all day; a sun-angle effect means silent diurnal performance cycles.
- Why Possibly Novel: Sun geometry as an explanatory variable for segmentation error (with fixed scenes across the day) is rarely isolated.
- Minimal Experiment: Use fixed-camera agricultural time-lapses with known geography; compute error vs solar angle from timestamps; test the angular dependence.
- Main Risk: Confounds with shadows and wind; include shadow-region masking and wind-speed covariates.
- Research Cluster tag: AMORPH

### IDEA-A-0117
- Idea: Frame-rate dependence of precipitation segmentation: measure how rain-streak/snowflake visibility — and therefore segmentation behavior — depends on exposure time and frame rate, defining a capture-parameter operating envelope.
- Problem: [KNOWN FACT] Rain streak appearance is an exposure-time artifact (motion blur of drops); models learn from datasets with unrecorded capture parameters.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Segmentation of precipitation (and of scenes through it) varies strongly and systematically with exposure/frame-rate, and models fail when test capture parameters differ from training-set norms; parameter-independent behavior falsifies it.
- Why Important: Weather robustness claims are meaningless without capture-parameter specification; this makes the hidden variable explicit.
- Why Possibly Novel: Elevates camera capture parameters to first-class domain-shift variables for weather segmentation.
- Minimal Experiment: Capture the same precipitation scenes at multiple exposure/frame-rate settings; evaluate fixed models; map performance vs capture parameters.
- Main Risk: Controlled precipitation capture is weather-dependent; use a rain rig or archived multi-setting captures.
- Research Cluster tag: AMORPH

### IDEA-A-0118
- Idea: Underwater bubble/plume transfer test: measure whether atmospheric-smoke-trained representations transfer to underwater bubble plumes, testing if models learned "participating media" or "smoke-specific appearance."
- Problem: [KNOWN FACT] Underwater plumes share transport physics with smoke but differ in optics (refraction at bubble surfaces vs scattering); transfer would indicate physics-level abstraction.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Transfer from smoke models to underwater plumes is near zero despite structural similarity, showing models encode appearance not transport structure; strong transfer falsifies the appearance-only account.
- Why Important: A clean answer about the abstraction level of learned amorphous representations guides whether cross-domain amorphous pretraining is worth pursuing.
- Why Possibly Novel: Uses a physics-matched/optics-mismatched domain pair as a designed probe of representation content.
- Minimal Experiment: Curate underwater plume/bubble clips; evaluate smoke-trained models zero-shot and after tiny adaptation; compare to matched-baseline transfer from unrelated domains.
- Main Risk: Underwater image quality varies wildly; control turbidity strata in the evaluation.
- Research Cluster tag: AMORPH

### IDEA-A-0119
- Idea: Human prompt-intent study for amorphous targets: measure what humans actually mean when they click on smoke (this puff, the plume, all smoke), and whether any current promptable model's behavior matches the dominant intent.
- Problem: [KNOWN FACT] Promptable segmentation assumes a click identifies an object; for amorphous media, the referent of a click is genuinely ambiguous and user intent is unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Human intent for amorphous clicks is strongly context-dependent but predictable (task framing determines puff-vs-plume choice), and current models match the dominant intent in only a minority of cases; unpredictable intent or high model-intent match falsifies parts of it.
- Why Important: Interactive tools for wildfire/industrial monitoring cannot be designed without knowing the intent distribution.
- Why Possibly Novel: Prompt semantics as an empirical human-subjects question (rather than a model property) is an unusual and needed inversion.
- Minimal Experiment: Show participants smoke scenes with a click marker under different task framings; collect intended-extent annotations; compare intent distributions to model outputs for identical clicks.
- Main Risk: Framing effects dominate; that is itself a finding — report intent conditional on framing.
- Research Cluster tag: AMORPH

### IDEA-A-0120
- Idea: Decision-utility test of soft outputs: measure whether human operators make better real-time decisions (evacuation, dispatch) from opacity/uncertainty maps than from binary smoke masks.
- Problem: [KNOWN FACT] Systems present binary overlays to operators; for amorphous phenomena, the binary form discards graded evidence the operator might use.
- Core Hypothesis (falsifiable): [HYPOTHESIS] In a controlled operator study, graded (soft) smoke visualizations improve decision accuracy and calibration under time pressure relative to binary masks at identical underlying model quality; no operator-level difference falsifies it.
- Why Important: The output representation is a free design choice; evidence-based selection could improve safety outcomes without touching models.
- Why Possibly Novel: Human-in-the-loop evaluation of segmentation output representations is nearly absent from the literature.
- Minimal Experiment: Run a within-subjects operator study on recorded incident videos with binary vs soft overlays; measure decision accuracy, latency, and confidence calibration.
- Main Risk: Ecological validity of lab studies; recruit domain practitioners for a subset.
- Research Cluster tag: AMORPH

---

## Section 4 — Detection limitations (IDEA-A-0121 .. 0150)

### IDEA-A-0121
- Idea: Estimate the missing-annotation rate in detection benchmarks by re-annotating stratified samples, and quantify how many reported "false positives" are actually unlabeled true objects.
- Problem: [KNOWN FACT] Detection benchmarks are known to contain unlabeled objects; penalized detections on them corrupt precision estimates in an unmeasured way.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A substantial, class-dependent fraction of high-confidence "false positives" from strong detectors are verifiable true objects, and correcting them changes model rankings at the top of leaderboards; negligible correction effect falsifies it.
- Why Important: If rankings flip after label completion, the community's recent progress ordering is partly annotation artifact.
- Why Possibly Novel: Uses strong models to guide targeted re-annotation, converting label completeness into a measurable, correctable quantity.
- Minimal Experiment: Sample high-confidence unmatched detections per class; human-verify; recompute metrics with corrected labels; compare rankings.
- Main Risk: Verification bias toward plausible boxes; use blinded review with distractor boxes.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0122
- Idea: Quantify how single-scalar mAP hides small-object collapse: measure the rank instability of detectors when evaluation is stratified by object size, density, and truncation.
- Problem: [KNOWN FACT] mAP averages over sizes and IoU thresholds; two detectors with equal mAP can have wildly different failure profiles.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Across public detectors, stratified evaluation flips a substantial fraction of pairwise rankings relative to headline mAP, with small-object strata driving most flips; stable rankings falsify it.
- Why Important: Practitioners choose detectors by headline mAP; systematic flip evidence would force stratified reporting norms.
- Why Possibly Novel: The flip-rate quantification across many public checkpoints (a meta-evaluation) rather than a metric proposal.
- Minimal Experiment: Evaluate 20+ public detectors stratified by size/density/truncation; compute pairwise rank-flip statistics vs headline mAP.
- Main Risk: Strata sample sizes get small; report confidence intervals per stratum.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0123
- Idea: Measure the intrinsic ceiling that greedy duplicate suppression (NMS-style post-processing) imposes in dense scenes by comparing against oracle assignment on crowded benchmarks.
- Problem: [KNOWN FACT] Overlap-based suppression removes true positives when objects genuinely overlap; the size of this ceiling as a function of crowd density is not commonly quantified per benchmark.
- Core Hypothesis (falsifiable): [HYPOTHESIS] In dense scenes, a measurable fraction of recall loss is attributable to suppression alone (recoverable by oracle keep-decisions on the same raw outputs), and this fraction grows predictably with instance-overlap statistics; negligible oracle-recoverable loss falsifies it.
- Why Important: Separates "detector cannot see the object" from "post-processing deleted it," which require different fixes.
- Why Possibly Novel: Oracle keep-decision analysis on frozen raw outputs turns a folklore complaint into a measured, benchmark-specific number.
- Minimal Experiment: For several detectors on crowded datasets, replay raw pre-suppression outputs with oracle keep decisions; report recovered recall vs overlap statistics.
- Main Risk: Raw outputs depend on score thresholds; sweep thresholds and report surfaces.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0124
- Idea: Class-conditional confidence calibration audit for detectors: measure whether rare classes are systematically miscalibrated relative to frequent classes at identical confidence values.
- Problem: [KNOWN FACT] Detector confidences feed downstream thresholds; calibration is usually assessed globally, not per class frequency.
- Core Hypothesis (falsifiable): [HYPOTHESIS] At a fixed reported confidence, rare-class detections have systematically lower empirical precision than frequent-class detections, with the gap predictable from training-set frequency; frequency-independent calibration falsifies it.
- Why Important: A single global threshold silently applies different effective standards per class — a fairness and safety issue in deployment.
- Why Possibly Novel: Frequency-conditional calibration curves for detection (not classification) with cross-dataset validation are rarely reported.
- Minimal Experiment: Compute per-class reliability diagrams on two benchmarks; regress calibration gap on log class frequency; validate on a third dataset.
- Main Risk: Rare-class reliability estimates are noisy; use pooled frequency bins and bootstrap intervals.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0125
- Idea: Hallucination rate of open-vocabulary detectors under absent-class prompts: measure false-alarm behavior when prompted for objects not present in the image, as a function of prompt specificity.
- Problem: [KNOWN FACT] Open-vocabulary detectors accept arbitrary text queries; their behavior when the queried object is absent is a core deployment property that standard benchmarks (which query present classes) do not measure.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Absent-class false-alarm rates are high and increase with prompt specificity (more specific prompts anchor to plausible look-alikes), and rates are uncorrelated with present-class mAP; low or mAP-correlated false alarms falsify it.
- Why Important: Search-and-rescue or security queries are usually for absent objects; hallucination behavior is the operative property.
- Why Possibly Novel: Absence-conditioned evaluation with prompt-specificity sweeps defines a new, deployment-first benchmark axis.
- Minimal Experiment: Query OV detectors with verified-absent class lists over a large image set; measure false-alarm curves vs prompt specificity; correlate with standard mAP.
- Main Risk: Verifying absence is expensive; use exhaustively annotated subsets.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0126
- Idea: Density-stratified counting validity: measure the instance density at which detection-based counting breaks down per class, and compare against direct density-estimation approaches on the same data.
- Problem: [KNOWN FACT] Counting-by-detection saturates in crowded scenes; the breakdown density and its class dependence are rarely reported, leaving practitioners to guess which regime they are in.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Counting error of detection-based methods exhibits a characteristic knee at a class-specific density (related to typical object overlap), beyond which density estimation dominates; smooth error growth with no crossover falsifies it.
- Why Important: Gives a decision rule for system architects: below density d use detection, above use regression.
- Why Possibly Novel: Cross-paradigm crossover measurement on identical data, presented as an operating-regime map.
- Minimal Experiment: Evaluate detection-counting and density-estimation on density-stratified crowd/vehicle/cell datasets; locate crossovers per class.
- Main Risk: Density strata confound with scale; control object pixel size across strata.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0127
- Idea: Context-dependence quantification via object transplantation: measure how much detector performance on an object drops when it is placed in an unusual but physically plausible context.
- Problem: [KNOWN FACT] Detectors exploit scene context; the size of context reliance per class is not systematically measured with controlled interventions.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Context-swap transplantation (cut-paste with lighting harmonization) reduces detection confidence/recall by a class-characteristic amount that predicts real-world out-of-context failures (e.g., indoor animals); no transplantation effect falsifies it.
- Why Important: Out-of-context objects are exactly the safety-relevant surprises (obstacle on a highway); a per-class context-reliance index is actionable.
- Why Possibly Novel: Systematic per-class context-reliance indices validated against natural out-of-context test sets.
- Minimal Experiment: Build transplanted test sets for 20 classes; measure per-class degradation; validate the index against natural out-of-context images.
- Main Risk: Paste artifacts confound; use harmonization and artifact-detection controls.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0128
- Idea: Co-occurrence shortcut audit: test whether detectors fire on the context alone (water for surfboards) by evaluating on images where the context is present but the object is verifiably absent.
- Problem: [KNOWN FACT] Object classes co-occur with characteristic backgrounds in training data; detectors may partially detect "the context."
- Core Hypothesis (falsifiable): [HYPOTHESIS] For high-co-occurrence classes, detectors produce object detections in object-absent context images at rates far exceeding matched low-co-occurrence controls; equal rates falsify it.
- Why Important: Context-triggered false positives inflate benchmark precision when the context usually contains the object, hiding a systematic error mode.
- Why Possibly Novel: Object-absent-context evaluation sets constructed specifically from co-occurrence statistics of the training corpora.
- Minimal Experiment: Mine object-absent context images for the top co-occurring class-context pairs; measure false-positive rates vs co-occurrence strength.
- Main Risk: Verifying object absence at scale; restrict to small verified sets per pair.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0129
- Idea: Border-truncation blind spot: quantify how detection recall depends on object truncation at image edges, and whether the effect is an annotation convention artifact or a genuine model failure.
- Problem: [KNOWN FACT] Objects at frame borders are truncated; both annotation conventions (whether to label them) and model behavior at borders vary.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Recall drops sharply with truncation fraction beyond what information loss explains (verified by comparing to human recall on the same crops), revealing a learned border bias; recall tracking human performance falsifies model-specific failure.
- Why Important: Panning cameras and vehicle-mounted systems constantly see truncated objects at the frame edge — often the newest, most safety-relevant ones.
- Why Possibly Novel: Human-anchored decomposition of truncation failure into information-limit vs learned-bias components.
- Minimal Experiment: Evaluate detectors and human annotators on truncation-stratified crops; compare recall curves; attribute the gap.
- Main Risk: Human experiments are costly; a small careful sample per stratum suffices.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0130
- Idea: Establish the information floor for small-object detection: at what pixel size does detection become impossible for humans, and how far above that floor do current detectors stop working?
- Problem: [KNOWN FACT] Small-object failure is universally reported, but nobody separates "model deficiency" from "information no longer present in the pixels."
- Core Hypothesis (falsifiable): [HYPOTHESIS] There is a measurable gap band — object sizes where humans detect reliably but models fail — and its width (in octaves of object size) is a stable model-family property; zero-width gap falsifies remaining headroom claims.
- Why Important: The gap width is exactly the available headroom for small-object research; knowing it prevents both defeatism and wasted effort.
- Why Possibly Novel: Human psychophysics as the reference floor for small-object detection benchmarks, reported per class.
- Minimal Experiment: Run size-controlled human detection experiments on benchmark crops; overlay model recall curves; report gap bands per class.
- Main Risk: Human performance depends on viewing conditions; standardize display protocol.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0131
- Idea: Ranking stability across IoU thresholds: measure how often detector rankings invert as the matching IoU threshold varies, and identify which architectural families are threshold-robust.
- Problem: [KNOWN FACT] The choice of IoU threshold for a true positive is arbitrary; averaged metrics blur but do not remove the dependence.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A substantial fraction of published pairwise detector comparisons invert somewhere in the standard threshold range, and inversion frequency correlates with differences in localization-vs-classification error balance; rare inversions falsify it.
- Why Important: Threshold-dependent conclusions are fragile conclusions; quantifying fragility tells readers which claims to trust.
- Why Possibly Novel: Treats the metric hyperparameter as an axis of scientific uncertainty and reports conclusion-stability, a meta-evaluation contribution.
- Minimal Experiment: Recompute pairwise comparisons for many public detectors across a fine threshold grid; report inversion statistics and their predictors.
- Main Risk: Purely computational; main risk is over-interpretation — pre-register which comparisons count as "published claims."
- Research Cluster tag: DET-LIMIT

### IDEA-A-0132
- Idea: Crowd-region convention harmonization: quantify how differing "crowd/ignore region" annotation conventions across datasets change cross-dataset detector comparisons.
- Problem: [KNOWN FACT] Datasets handle dense crowds differently (ignore regions, group boxes, exhaustive labeling); cross-dataset evaluations inherit these inconsistencies silently.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Re-scoring the same predictions under each dataset's crowd convention (applied to the same images) changes detector rankings, demonstrating that part of "cross-dataset generalization" is convention mismatch; invariant rankings falsify it.
- Why Important: Cleans a confound at the heart of every cross-dataset robustness claim involving crowded scenes.
- Why Possibly Novel: Convention-swapped re-scoring isolates the annotation-policy effect from the data effect — rarely done.
- Minimal Experiment: Take one densely annotated dataset; re-derive labels under 3 published crowd conventions; re-score fixed predictions under each; compare rankings.
- Main Risk: Convention re-derivation requires interpretation; document rules and release the re-derived labels.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0133
- Idea: Rare-pose failure census: measure detection performance on pose-stratified data (fallen persons, overturned vehicles, folded bicycles) where the class is common but the configuration is rare.
- Problem: [KNOWN FACT] Training data over-represents canonical poses; safety-critical events often involve exactly the non-canonical poses (a fallen pedestrian).
- Core Hypothesis (falsifiable): [HYPOTHESIS] Detection recall for non-canonical poses is drastically lower than canonical at matched size/visibility, and the deficit is not predicted by overall class AP; pose-independent recall falsifies it.
- Why Important: The rare poses are the emergencies; per-pose reporting would expose a hidden safety gap in deployed systems.
- Why Possibly Novel: Pose-stratified safety evaluation with matched-visibility controls, framed as a deployment audit rather than a long-tail method paper.
- Minimal Experiment: Curate pose-stratified test sets for 3 safety-relevant classes; evaluate public detectors; report canonical/non-canonical recall gaps.
- Main Risk: Rare-pose data is scarce; combine curated real images with staged captures.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0134
- Idea: Attribute low-light detection failure to the camera ISP versus the sensor: compare detection on RAW-processed vs default-ISP images of identical low-light scenes.
- Problem: [KNOWN FACT] Consumer ISPs denoise/sharpen for human viewing, not for detection; in low light, ISP choices may destroy detection-relevant signal.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A meaningful fraction of low-light detection failure is recoverable by re-processing RAW data with detection-oriented settings, attributing the loss to the ISP rather than photon statistics; no recovery falsifies it.
- Why Important: If the ISP is the bottleneck, deployment fixes are configuration-level, not model-level — a much cheaper path.
- Why Possibly Novel: ISP-vs-sensor attribution for detection using paired RAW captures is rarely done outside image-quality research.
- Minimal Experiment: Collect paired RAW+JPEG low-light captures with annotations; evaluate fixed detectors on default vs alternative processing; decompose the gap.
- Main Risk: RAW datasets with detection labels are rare; a small purpose-built capture set is acceptable.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0135
- Idea: Decompose adverse-weather detection degradation into contrast-reduction vs physical-occlusion components using synthetic weather with separable parameters.
- Problem: [KNOWN FACT] Fog/rain degrade detection through multiple mechanisms simultaneously; aggregate degradation numbers cannot guide countermeasures.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For fog, contrast reduction explains the large majority of degradation (occlusion negligible), while for rain the split differs — and the decomposition predicts which enhancement (contrast restoration vs de-raining) helps which weather; equal splits falsify the differential prediction.
- Why Important: Tells engineers which preprocessing is worth deploying per weather type, grounded in causal decomposition.
- Why Possibly Novel: Parameter-separable synthetic weather as a decomposition instrument, validated against real weather captures.
- Minimal Experiment: Render weather with independently controlled contrast/occlusion parameters; measure detector degradation per component; validate the decomposition on real foggy/rainy sets.
- Main Risk: Synthetic weather fidelity; anchor with real paired captures where possible.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0136
- Idea: Blur decouples classification from localization: test whether motion blur degrades box accuracy long before class accuracy, creating well-classified but badly-localized detections.
- Problem: [KNOWN FACT] Detection error metrics blend classification and localization; blur plausibly affects them differently, with distinct downstream consequences.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Under increasing blur, localization error grows much faster than classification error, producing a regime of confidently classified, poorly localized detections that fixed IoU thresholds convert into both FPs and FNs; parallel degradation falsifies it.
- Why Important: For tracking and collision estimation, a well-classified but misplaced box is dangerous; the regime needs to be known and flagged.
- Why Possibly Novel: Component-resolved degradation curves under a parametric corruption, tied to a concrete failure regime.
- Minimal Experiment: Apply parametric blur to annotated video frames; measure classification and localization error curves separately; identify the divergence regime.
- Main Risk: Ground truth on blurred frames inherits ambiguity; use sharp-frame GT propagated to blurred versions.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0137
- Idea: Vocabulary-granularity calibration in open-vocabulary detection: measure how recall changes when the same object is queried at different taxonomy levels ("dog" vs "labrador" vs "animal").
- Problem: [KNOWN FACT] OV detectors accept any text; users don't know which granularity the model "prefers," and the granularity-performance relationship is unmapped.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Each OV model has a granularity sweet spot (typically basic-level categories) with steep recall falloff toward both finer and coarser queries, and the sweet spot location is predictable from pretraining caption statistics; flat granularity response falsifies it.
- Why Important: A granularity-response curve is essential user documentation for any deployed OV system.
- Why Possibly Novel: Systematic taxonomy-level sweeps as a characterization protocol, linked to pretraining text statistics.
- Minimal Experiment: Query hierarchical label chains on a taxonomy-annotated dataset; plot recall vs taxonomy depth per model; correlate sweet spots with caption-frequency statistics.
- Main Risk: Prompt wording confounds granularity; use multiple templates per level.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0138
- Idea: Near-duplicate inflation audit for detection test sets: measure how much benchmark scores and rankings depend on clusters of visually near-identical test images.
- Problem: [KNOWN FACT] Web-collected benchmarks contain near-duplicates; each duplicate cluster effectively votes multiple times in the metric.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Deduplicated re-scoring changes absolute mAP modestly but changes model rankings in a nontrivial fraction of close comparisons, because different models exploit duplicate clusters differently; ranking invariance falsifies it.
- Why Important: Close leaderboard decisions (the ones that drive publication claims) are exactly the ones duplicates can flip.
- Why Possibly Novel: Duplicate-effects quantified at the ranking-decision level rather than the score level.
- Minimal Experiment: Detect near-duplicate clusters in test sets; re-score public detectors with cluster-weighted metrics; report ranking changes among closely matched pairs.
- Main Risk: Duplicate detection thresholds are arbitrary; sweep thresholds and show robustness.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0139
- Idea: Abstention absence in detectors: measure how detectors distribute confidence on genuinely novel objects (not in any training class), testing whether "none of the above" is representable at all.
- Problem: [KNOWN FACT] Closed-set detectors must map every proposal to known classes or background; a novel salient object gets either a wrong label or silent suppression, with unknown proportions.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Novel objects are predominantly assigned confidently to visually nearest known classes (rather than suppressed as background), and the assignment is predictable from feature-space proximity; predominant background-suppression falsifies it.
- Why Important: Confident misclassification of the truly unknown is the worst failure profile for autonomous systems encountering novelty.
- Why Possibly Novel: A directional census of where novelty goes (wrong-class vs background) with feature-space predictors, across detector families.
- Minimal Experiment: Present verified-novel objects to closed-set detectors; classify outcomes; regress wrong-class choice on embedding proximity.
- Main Risk: "Novel" objects may resemble training classes; verify novelty via training-set nearest-neighbor audits.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0140
- Idea: Controlled label-corruption study for detection training: rank which annotation error type (missing boxes, loose boxes, wrong classes, duplicated boxes) damages trained detectors most per unit of error.
- Problem: [KNOWN FACT] Annotation budgets must trade error types against cost; there is no per-error-type damage function to guide QA priorities.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Missing-box noise damages recall-critical applications far more per corrupted instance than equally frequent loose-box noise, and the damage ordering is stable across datasets; unstable orderings falsify general guidance.
- Why Important: Converts annotation QA from taste into a measured cost-benefit table used by every dataset builder.
- Why Possibly Novel: Systematic factorial corruption at matched corruption budgets, reported as a practical damage table.
- Minimal Experiment: Inject each error type at controlled rates into a clean training set; train matched detectors; measure per-type damage curves on clean test data.
- Main Risk: Interactions between error types; include mixed-corruption cells in the design.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0141
- Idea: Scale-distribution mismatch as a data-centric explanation: test how much small-object failure is explained by the mismatch between training and test object-scale distributions, via resampling alone.
- Problem: [KNOWN FACT] Training sets have particular scale distributions; test-time complaints about small objects may partly reflect distribution mismatch rather than architectural limits.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Re-weighting/resampling training data to match the test scale distribution (no architecture or loss change) recovers a substantial fraction of the small-object gap; negligible recovery falsifies the data-centric account.
- Why Important: Quantifies how much of a famous problem dissolves with data curation before any modeling work is justified.
- Why Possibly Novel: A pure-resampling attribution study run across several detector families with matched budgets.
- Minimal Experiment: Train matched detectors on original vs scale-rebalanced training data; compare size-stratified AP; report the recovered fraction.
- Main Risk: Rebalancing reduces effective data diversity; control total training exposure carefully.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0142
- Idea: Equivariance self-audit as a free diagnostic: measure detection output consistency under horizontal flips and small translations as a label-free per-image reliability score.
- Problem: [KNOWN FACT] Detection outputs change under trivially equivalent input transformations; the magnitude of this inconsistency per image is a free signal nobody systematically exploits for reliability scoring.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Per-image flip/translation inconsistency correlates strongly with per-image error measured against GT, and the correlation transfers across datasets, enabling label-free triage; weak or non-transferring correlation falsifies it.
- Why Important: A zero-annotation reliability score enables prioritized human review in production systems.
- Why Possibly Novel: Equivariance violation as a calibrated, validated reliability instrument (with transfer tests) rather than an anecdote.
- Minimal Experiment: Compute inconsistency scores and true per-image error for several detectors on multiple datasets; report correlation and cross-dataset transfer.
- Main Risk: Some scenes are genuinely symmetric-ambiguous; analyze failure cases of the signal itself.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0143
- Idea: Error-propagation map from detection to tracking: identify which detector error types (jitter, misses, duplicates, drift) are fatal versus benign for downstream tracking-by-detection systems.
- Problem: [KNOWN FACT] Detectors are optimized in isolation, but their consumers are trackers; the mapping from detector error profile to tracker failure is unquantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Short bursts of consecutive misses damage tracking far more than a higher rate of isolated misses at equal total miss count, i.e., temporal error correlation (unmeasured by AP) dominates downstream impact; equal damage falsifies it.
- Why Important: Would redefine what detector metric matters for video systems: temporal error structure, not aggregate rates.
- Why Possibly Novel: Controlled injection of temporally structured detector errors into fixed trackers, producing a transferable damage model.
- Minimal Experiment: Corrupt GT detections with controlled temporal error patterns; feed standard trackers; map tracking-metric damage vs error structure.
- Main Risk: Tracker-specific results; test 3 tracker families and report commonalities.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0144
- Idea: Quantify the error floor imposed by axis-aligned box conventions on oriented objects in aerial imagery, separating convention error from model error.
- Problem: [KNOWN FACT] Axis-aligned boxes fit rotated elongated objects poorly; part of reported "error" is representational, not behavioral.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For elongated aerial classes, the IoU ceiling imposed by the axis-aligned convention (computed geometrically from GT orientation statistics) accounts for a large share of the gap between reported and perfect scores; a small share falsifies it.
- Why Important: Separates "models need improving" from "the representation caps the score," directing effort appropriately.
- Why Possibly Novel: An analytically computed convention ceiling reported alongside empirical scores per class.
- Minimal Experiment: Compute the best achievable axis-aligned IoU per GT object from oriented annotations; compare the convention ceiling with actual model scores per class.
- Main Risk: Purely geometric analysis may miss interaction effects; complement with oriented-box model comparisons.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0145
- Idea: Characterize when RGB-pretrained representations help versus hurt thermal-image detection, as a function of class-wise thermal-RGB appearance correlation.
- Problem: [KNOWN FACT] Thermal deployment commonly initializes from RGB pretraining; transfer sometimes underperforms scratch training, and no predictive rule exists for when.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Transfer benefit per class is predictable from a measurable thermal-RGB appearance-correlation score (shape-driven classes transfer, emissivity-driven classes suffer negative transfer); unpredictable benefit falsifies it.
- Why Important: A predictive rule prevents costly wrong initialization choices across the growing thermal-deployment industry.
- Why Possibly Novel: Class-level negative-transfer prediction from a computable cross-modal similarity statistic, not a post-hoc anecdote.
- Minimal Experiment: Train per-class probes from RGB-pretrained vs scratch features on thermal data; regress the transfer delta on cross-modal appearance-correlation measures.
- Main Risk: Confounded by thermal dataset size; replicate at two data scales.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0146
- Idea: Deployment-prior evaluation: recompute detection utility under realistic per-image object prevalence (most frames contain nothing), exposing the gap between benchmark PR curves and field alert precision.
- Problem: [KNOWN FACT] Benchmarks are object-rich by construction; deployed streams are mostly empty, which transforms the practical meaning of any false-positive rate.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Under field-realistic prevalence, the ranking of detectors by alert precision differs from benchmark AP ranking, because empty-frame false-positive behavior is uncorrelated with object-rich AP; preserved rankings falsify it.
- Why Important: Systems are bought on benchmark numbers and fail on empty-frame false alarms; quantifying the disconnect protects deployments.
- Why Possibly Novel: Empty-frame behavior as an explicitly measured, separately reported detector property.
- Minimal Experiment: Assemble large verified-empty frame sets from deployment-like sources; measure per-detector empty-frame FP rates; recompute utility under realistic prevalence mixes.
- Main Risk: "Verified empty" requires care; use multi-model consensus plus human audit of disagreements.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0147
- Idea: Cross-dataset box-tightness bias: measure systematic differences in how tightly datasets draw boxes, and show that detectors regress toward their training dataset's tightness convention on foreign data.
- Problem: [KNOWN FACT] Annotation guidelines differ on box tightness (include accessories? antennas? shadows?); cross-dataset localization errors may encode convention transfer.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Each dataset has a measurable tightness signature, and cross-dataset evaluation shows detectors reproducing their source signature (a constant relative-size bias) rather than adapting to the target convention; no signature transfer falsifies it.
- Why Important: Identifies a correctable constant bias inflating cross-dataset localization error in every transfer study.
- Why Possibly Novel: Dataset conventions treated as measurable, transferable model biases with a simple correction test.
- Minimal Experiment: Estimate per-dataset tightness signatures from matched classes; measure detector output tightness on foreign datasets; test signature persistence and post-hoc correction.
- Main Risk: Class-mix differences confound tightness estimates; match classes and sizes across datasets.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0148
- Idea: Systemic latency-accuracy coupling: measure how detection accuracy degrades end-to-end when compute contention forces frame drops, revealing failure modes invisible to per-frame benchmarks.
- Problem: [KNOWN FACT] Real systems share compute; when detectors slow down, frames drop and the effective input changes — a coupled system effect no standard benchmark measures.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Under realistic load, accuracy-critical events are missed disproportionately (fast events fall between processed frames), making effective accuracy substantially worse than per-frame metrics predict, with the gap predictable from event-speed statistics; negligible gap falsifies it.
- Why Important: Procurement decisions rely on per-frame accuracy that may be systematically unrepresentative under load.
- Why Possibly Novel: Treats the perception system (not the model) as the unit of evaluation, with a reproducible load-injection protocol.
- Minimal Experiment: Replay annotated video through a real pipeline under controlled compute contention; measure event-level recall vs load; compare against per-frame predictions.
- Main Risk: Results depend on pipeline specifics; publish the harness so others can measure their own.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0149
- Idea: Effective test-set size after difficulty weighting: estimate how many benchmark images actually discriminate between modern detectors, and whether progress claims rest on a tiny informative subset.
- Problem: [KNOWN FACT] Most benchmark images are solved by all strong models; metric differences concentrate in a small hard subset whose size and stability are unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A small fraction of test images accounts for the large majority of score differences among top detectors, and this informative subset is stable across model generations, making the effective benchmark far smaller than its nominal size; a diffuse difference distribution falsifies it.
- Why Important: If the effective test set is tiny, statistical claims of superiority are much weaker than they appear — and the informative subset deserves scrutiny.
- Why Possibly Novel: Item-response-style analysis (which items discriminate) applied to detection benchmarks at scale.
- Minimal Experiment: For many public detectors, compute per-image score contributions; identify the discriminative subset; measure its size, stability, and content characteristics.
- Main Risk: Subset instability across metrics; run with several metrics and report agreement.
- Research Cluster tag: DET-LIMIT

### IDEA-A-0150
- Idea: Typographic-trigger audit for detection: measure whether text or logos in scenes (street ads, vehicle liveries) systematically trigger or suppress object detections.
- Problem: [KNOWN FACT] Web-trained models are exposed to text-image correlations; scene text as a detection trigger has been shown for classification-style models but is uncharacterized for detectors in realistic scenes.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Scene text semantically related to a class (a bus ad showing a dog) measurably increases false detections of that class in the text/ad region, scaling with text-image prominence; no semantic-text effect falsifies it.
- Why Important: Advertising is everywhere in urban scenes; semantic-trigger false positives would be a systematic urban-deployment hazard.
- Why Possibly Novel: Realistic in-scene semantic-text interventions (not synthetic patch attacks) with prominence dose-response.
- Minimal Experiment: Composite semantically related vs unrelated ads into street scenes at varied prominence; measure class-specific false-positive rates per condition.
- Main Risk: Compositing artifacts; include unrelated-ad and no-ad controls with matched placement.
- Research Cluster tag: DET-LIMIT

---

## Section 5 — Domain shift (IDEA-A-0151 .. 0185)

### IDEA-A-0151
- Idea: Build a shift-attribution protocol that decomposes any benchmark-pair performance drop into covariate shift, label shift, and concept/definition shift components with uncertainty estimates.
- Problem: [KNOWN FACT] "Domain gap" numbers between dataset pairs are reported as single scalars; the constituent shift types require different remedies but are never separated.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For most popular cross-dataset segmentation/detection pairs, concept/definition shift (differing class meanings and annotation policies) accounts for a larger share of the drop than covariate shift, contradicting the community's implicit assumption; a covariate-dominated decomposition falsifies it.
- Why Important: If definition shift dominates, adaptation methods aimed at image appearance are treating the wrong disease.
- Why Possibly Novel: A general, released attribution protocol applied across many pairs — turning an anecdote into a measured landscape.
- Minimal Experiment: For 5 dataset pairs, estimate each component (label-distribution matching, re-annotation samples for definitions, appearance-transfer probes); publish the decomposition table.
- Main Risk: Components are not perfectly separable; report identifiability limits explicitly.
- Research Cluster tag: DOMAIN

### IDEA-A-0152
- Idea: Frequency-band causal attribution of domain gaps: measure what fraction of specific real-world shift drops (day→night, clear→fog, dataset A→B) is transferred by swapping each spectral band.
- Problem: [KNOWN FACT] Amplitude-spectrum swaps can move images between domains; a systematic per-shift accounting of which frequency bands carry each real gap is missing.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Different shift types have distinct spectral signatures (weather gaps concentrated in low frequencies, sensor gaps in high frequencies), and the signature predicts which restoration strategies work; indistinct signatures falsify it.
- Why Important: A spectral fingerprint per shift type yields a diagnostic tool: measure the fingerprint, predict the remedy.
- Why Possibly Novel: Comparative spectral attribution across many shift types under one protocol, with remedy-prediction validation.
- Minimal Experiment: Construct band-swapped hybrids for several shift pairs; measure per-band gap transfer; validate remedy predictions on held-out shifts.
- Main Risk: Phase-spectrum effects are ignored by amplitude swaps; include phase-swap controls.
- Research Cluster tag: DOMAIN

### IDEA-A-0153
- Idea: Meta-evaluate unsupervised domain-distance measures: which computable distances between unlabeled datasets actually predict segmentation performance drops, across a large grid of domain pairs?
- Problem: [KNOWN FACT] Many domain-distance measures exist; practitioners need to predict deployment drops from unlabeled data, but the measures' predictive validity for dense tasks is unranked.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Predictive validity varies drastically across distance measures, no single measure works across shift types, but a small ensemble of complementary measures achieves usable prediction accuracy; uniform validity of all measures falsifies the premise.
- Why Important: A validated drop predictor is the single most requested tool by anyone deploying vision models to new sites.
- Why Possibly Novel: Large-grid meta-evaluation (many models × many domain pairs × many measures) for dense prediction, not classification.
- Minimal Experiment: Assemble 30+ labeled domain pairs; compute candidate distances on unlabeled data; regress true drops on distances; report per-shift-type validity.
- Main Risk: Grid assembly is laborious; reuse existing public multi-domain benchmarks aggressively.
- Research Cluster tag: DOMAIN

### IDEA-A-0154
- Idea: Validate label-free accuracy estimation for segmentation under shift: test whether agreement-based and confidence-based estimators that work for classification remain valid for dense structured outputs.
- Problem: [KNOWN FACT] Unsupervised accuracy estimation is maturing for classification; segmentation adds spatial correlation of errors, which may break the estimators' independence assumptions.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Classification-derived estimators systematically overestimate segmentation accuracy under shift because spatially correlated errors violate their assumptions, and the bias grows with error spatial-correlation length; unbiased estimates falsify it.
- Why Important: Deployed segmentation needs label-free accuracy monitoring; knowing where current estimators break prevents false confidence.
- Why Possibly Novel: A focused study of the structured-output failure of accuracy-estimation methods, with a diagnosis (correlation length) rather than a score table.
- Minimal Experiment: Apply standard estimators to segmentation models across shifted datasets with ground truth; measure estimation bias vs error correlation statistics.
- Main Risk: Estimators need adaptation choices for dense outputs; document adaptations and test sensitivity.
- Research Cluster tag: DOMAIN

### IDEA-A-0155
- Idea: Predict test-time-adaptation collapse before it happens: identify batch statistics that forecast when entropy-style self-supervised adaptation will degenerate (e.g., collapsing to few classes).
- Problem: [KNOWN FACT] Test-time adaptation can catastrophically collapse on some streams; practitioners have no early-warning signal and discover failure after damage.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Collapse is preceded by measurable statistics (prediction-entropy trajectory shape, class-marginal drift velocity) that predict failure several batches ahead with useful reliability; no predictive signal falsifies it.
- Why Important: An early-warning gate would make TTA deployable in safety-conscious settings where silent collapse is disqualifying.
- Why Possibly Novel: Failure forecasting for adaptation dynamics — treating the adaptation process itself as the object of prediction.
- Minimal Experiment: Run standard TTA methods across many streams (benign and adversarial orderings); log candidate statistics; train/evaluate a collapse predictor with lead-time analysis.
- Main Risk: Collapse modes vary by method; cover several TTA families to test signal generality.
- Research Cluster tag: DOMAIN

### IDEA-A-0156
- Idea: Characterize the conditions under which normalization-statistics adaptation hurts: map the shift-type regimes where recomputing feature statistics on target data degrades performance.
- Problem: [KNOWN FACT] Adapting normalization statistics to the target domain is a widely used cheap fix that sometimes backfires; the boundary between helping and hurting is folklore.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Statistic adaptation hurts precisely when the shift includes label-distribution change (statistics absorb content differences, not just style), and a computable label-shift proxy predicts the sign of the effect; unpredictable sign falsifies it.
- Why Important: Gives practitioners a pre-deployment test for whether the cheapest adaptation trick is safe on their data.
- Why Possibly Novel: A predictive regime map with a decision rule, replacing trial-and-error for a ubiquitous technique.
- Minimal Experiment: Evaluate statistic adaptation across shift pairs with controlled style-vs-content differences; fit and validate the sign predictor.
- Main Risk: Regimes may be architecture-dependent; verify on 3 architectures.
- Research Cluster tag: DOMAIN

### IDEA-A-0157
- Idea: Build gradual-drift evaluation from timestamped archives: test whether continual adaptation methods validated on abrupt-shift benchmarks survive realistic multi-year gradual drift.
- Problem: [KNOWN FACT] Adaptation research evaluates mostly on abrupt synthetic shifts; real deployment drift is gradual and compounding, with different failure dynamics.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Methods ranked highly on abrupt-shift benchmarks reorder substantially under gradual drift (some accumulate adaptation debt, others stay stable), showing abrupt benchmarks are unrepresentative; preserved rankings falsify it.
- Why Important: The community may be selecting methods on the wrong stress profile; the reordering evidence would redirect benchmark design.
- Why Possibly Novel: Uses genuinely timestamped image archives (webcams, satellite, retail) to construct real gradual drift rather than simulating it.
- Minimal Experiment: Assemble timestamped multi-year streams with periodic labels; run leading adaptation methods; compare rankings vs abrupt-shift results.
- Main Risk: Labeling cost across time; label sparse anchor sets and interpolate evaluation carefully.
- Research Cluster tag: DOMAIN

### IDEA-A-0158
- Idea: Prompt-distribution shift as a new axis: measure how promptable segmentation models degrade when the distribution of prompts (click styles, box tightness, text phrasing) shifts between development and deployment users.
- Problem: [KNOWN FACT] Domain shift research covers image shift; promptable models add a second input channel — the prompt — whose distributional shift is unstudied.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Realistic prompt-distribution shift (novice vs expert users, different tools) causes performance changes comparable in magnitude to moderate image shift, and image-shift robustness does not predict prompt-shift robustness; negligible or correlated effects falsify it.
- Why Important: Deployment of interactive tools to new user populations is exactly a prompt-shift event; nobody currently measures readiness for it.
- Why Possibly Novel: Defines and operationalizes a genuinely new shift axis unique to promptable-model deployments.
- Minimal Experiment: Collect prompt logs from distinct user populations; evaluate fixed models under each prompt distribution on fixed images; compare degradation magnitudes.
- Main Risk: User-population data collection; start with two accessible populations (lab experts vs crowdworkers).
- Research Cluster tag: DOMAIN

### IDEA-A-0159
- Idea: Causal factor ranking of the synthetic-to-real gap for driving segmentation via controlled rendering: which rendering dimension (geometry fidelity, texture realism, lighting, sensor simulation) buys the most real-world transfer per unit of effort?
- Problem: [KNOWN FACT] Synthetic driving data is abundant, but the sim-to-real gap persists; rendering effort is allocated by intuition because factor contributions are unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Sensor/optics simulation (noise, optics, tone curve) contributes more transfer gain than texture realism at matched effort, reversing common prioritization; texture-dominant results falsify it.
- Why Important: Simulation teams spend enormously on visual fidelity; a factor ranking could redirect that budget with direct performance payoff.
- Why Possibly Novel: A full-factorial rendering study with effort-normalized accounting, executed on modern renderers with segmentation endpoints.
- Minimal Experiment: Render factorial dataset variants; train matched models; evaluate on real driving benchmarks; report effort-normalized factor effects.
- Main Risk: Factor "effort" quantification is contestable; report both raw and effort-normalized effects.
- Research Cluster tag: DOMAIN

### IDEA-A-0160
- Idea: Geographic definition drift: measure how the visual meaning of segmentation classes ("house," "road," "shop") varies across world regions and how much of geographic performance disparity it explains.
- Problem: [KNOWN FACT] Models underperform on imagery from underrepresented regions; the split between appearance shift and class-definition drift (the same word denoting different visual things) is unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For several common classes, region-conditional visual prototypes differ enough that definition drift explains a substantial share of the cross-region performance gap, measurable by re-annotating with region-localized definitions; appearance-dominated gaps falsify it.
- Why Important: If definitions drift, fair geographic evaluation requires localized ontologies — a different fix than collecting more images.
- Why Possibly Novel: Separates ontology-level from appearance-level geographic bias with a re-annotation intervention.
- Minimal Experiment: Re-annotate region-stratified samples using locally validated class definitions; recompute cross-region gaps; attribute the change.
- Main Risk: Localized definitions require regional collaborators; scope to 3 regions and 5 classes.
- Research Cluster tag: DOMAIN

### IDEA-A-0161
- Idea: Model-rot measurement: quantify the temporal decay rate of frozen segmentation/detection models on genuinely time-stamped data streams as the world drifts (new vehicle designs, fashion, storefronts).
- Problem: [KNOWN FACT] The visual world changes over years; deployed frozen models must age, but the field has no measured decay constants for vision tasks.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Performance decays measurably and approximately monotonically with temporal distance from the training-data epoch, with class-specific decay rates (man-made object classes decay fastest); no measurable temporal decay falsifies it.
- Why Important: Decay constants directly inform retraining budgets and model-expiry policies — currently set blind.
- Why Possibly Novel: Longitudinal model-aging curves on real multi-year visual data, reported like reliability engineering.
- Minimal Experiment: Evaluate epoch-frozen models on year-bucketed test data from archives with stable annotation protocols; fit decay curves per class.
- Main Risk: Annotation-protocol drift confounds temporal drift; use stably annotated archives or re-annotate anchors.
- Research Cluster tag: DOMAIN

### IDEA-A-0162
- Idea: Lens-soiling robustness curves: measure segmentation degradation as a continuous function of physically graded lens contamination (dust, water film, mud), producing maintenance thresholds.
- Problem: [KNOWN FACT] Outdoor cameras accumulate lens contamination gradually; robustness benchmarks use digital corruptions that may not represent the physical optics of soiling.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Physical soiling degrades performance in a pattern (local blur plus scattering veil) poorly approximated by standard digital corruptions, so corruption-benchmark rankings mispredict soiling robustness; accurate prediction falsifies it.
- Why Important: Fleets need "clean the camera at X% soiling" thresholds grounded in actual performance, and benchmark validity for this common hazard is untested.
- Why Possibly Novel: Physically applied, optically measured soiling as ground truth for evaluating digital-corruption benchmark validity.
- Minimal Experiment: Capture scenes through progressively soiled lens filters with reference clean captures; evaluate fixed models; compare against digital-corruption predictions.
- Main Risk: Reproducible soiling application; use calibrated spray/particle protocols and measure optical transfer directly.
- Research Cluster tag: DOMAIN

### IDEA-A-0163
- Idea: Transcoding shift audit: measure how deployment video-compression pipelines (repeated transcoding, bitrate ladders) degrade segmentation relative to the pristine-image conditions models are validated on.
- Problem: [KNOWN FACT] Production video passes through codecs and bitrate adaptation; academic evaluation uses near-lossless frames, leaving a validity gap of unknown size.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Realistic transcoding chains cause substantial, content-dependent degradation concentrated on thin structures and motion boundaries, and degradation is predicted by measurable bitstream statistics (QP, motion-vector density) enabling per-frame quality gating; negligible or unpredictable degradation falsifies it.
- Why Important: A bitstream-statistics-based quality gate is deployable for free since decoders already expose these values.
- Why Possibly Novel: Uses codec-internal metadata as covariates for perception reliability — bridging video engineering and model evaluation.
- Minimal Experiment: Re-encode annotated video through realistic ladders; measure degradation vs bitstream statistics; validate a gating rule on held-out content.
- Main Risk: Codec configurations are endless; sample from actual production configurations of major platforms.
- Research Cluster tag: DOMAIN

### IDEA-A-0164
- Idea: Resampling-kernel shift: quantify how the choice of resize interpolation in deployment preprocessing (differing from training) acts as a hidden domain shift for dense prediction.
- Problem: [KNOWN FACT] Different libraries and hardware paths use different interpolation kernels and anti-aliasing choices; models are silently exposed to a kernel they weren't trained with.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Kernel mismatch between train and test resizing causes measurable, systematic dense-prediction degradation (concentrated at high-frequency structures), comparable to mild compression artifacts, and is fully eliminated by kernel matching; negligible effect falsifies it.
- Why Important: This is perhaps the cheapest fixable shift in existence — one line of configuration — but only if its cost is demonstrated.
- Why Possibly Novel: Elevates a build-configuration detail into a quantified, controlled shift study across model families.
- Minimal Experiment: Evaluate fixed models under all train/test kernel combinations on several datasets; report the mismatch penalty matrix.
- Main Risk: Effects may be small for robust models; even a null result is a useful reproducibility finding — publish either way.
- Research Cluster tag: DOMAIN

### IDEA-A-0165
- Idea: Taxonomy-alignment error census: quantify how much of cross-dataset "domain gap" in semantic segmentation is mechanical label-space mismatch (class merging/splitting/definition differences) rather than image-distribution shift.
- Problem: [KNOWN FACT] Cross-dataset evaluation requires mapping label spaces; mapping choices are ad hoc and their contribution to reported gaps is unquantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Alternative defensible taxonomy mappings between popular dataset pairs change measured cross-dataset performance by amounts comparable to entire published method improvements; mapping-insensitive gaps falsify it.
- Why Important: If mapping choices rival method effects, cross-dataset comparisons need standardized, versioned mappings before further method claims.
- Why Possibly Novel: Sensitivity analysis over the mapping itself, treated as a first-class experimental variable.
- Minimal Experiment: Enumerate defensible mappings for 3 dataset pairs; recompute cross-dataset scores under each; report the mapping-induced spread against published method deltas.
- Main Risk: "Defensible" needs criteria; have multiple experts propose mappings independently.
- Research Cluster tag: DOMAIN

### IDEA-A-0166
- Idea: Predict negative transfer before fine-tuning: test whether measurable source-target representation statistics predict when pretraining hurts rather than helps dense-task adaptation.
- Problem: [KNOWN FACT] Pretraining usually helps but sometimes hurts; practitioners discover negative transfer only after spending the compute.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A computable pre-adaptation statistic (e.g., feature-space class-overlap between source priors and target structure) predicts the sign of transfer with useful accuracy across task pairs; chance-level prediction falsifies it.
- Why Important: A pre-flight negative-transfer test would save enormous wasted compute and prevent silently degraded deployments.
- Why Possibly Novel: Focuses on sign prediction (help vs hurt) as a binary decision problem with deployment semantics, evaluated across a wide task grid.
- Minimal Experiment: Assemble many source-target pairs with known transfer outcomes; compute candidate predictors from unlabeled/frozen features; evaluate sign-prediction accuracy.
- Main Risk: Known-outcome pairs require many training runs; reuse published transfer studies plus targeted new runs.
- Research Cluster tag: DOMAIN

### IDEA-A-0167
- Idea: Test the over-randomization hypothesis in domain randomization: does excessive appearance randomization during synthetic training erase task-relevant cues and produce an inverted-U performance curve?
- Problem: [KNOWN FACT] Domain randomization improves sim-to-real transfer; whether more randomization is monotonically better or eventually harmful is unresolved and matters for pipeline design.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Transfer performance versus randomization strength follows an inverted U — beyond an optimum, randomizing cue-bearing properties (shading, texture statistics that correlate with geometry) removes information the task needs; monotone improvement falsifies it.
- Why Important: Establishes that randomization must be cue-aware, with a measurable optimum, changing how synthetic pipelines are tuned.
- Why Possibly Novel: A controlled randomization-strength dose-response study with cue-specific ablations identifying which randomized property causes the downturn.
- Minimal Experiment: Train models across a randomization-strength sweep (global and per-property); evaluate real transfer; locate optima and attribute downturns to properties.
- Main Risk: Optima may be task-specific; run two tasks (segmentation, detection) to test generality.
- Research Cluster tag: DOMAIN

### IDEA-A-0168
- Idea: Test whether curriculum ordering over intermediate domains helps only when the shift is compositional: sequential adaptation through intermediate domains vs direct adaptation, on shifts with and without natural intermediates.
- Problem: [KNOWN FACT] Gradual adaptation through intermediate domains is intuitively appealing; when it actually beats direct adaptation is empirically unsettled.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Intermediate-domain curricula outperform direct adaptation only when the source-target shift decomposes into the traversed factors (day→dusk→night), and hurt when intermediates introduce off-path variation; universal curriculum benefit falsifies it.
- Why Important: Prevents cargo-cult curriculum construction and gives a testable criterion for when to collect intermediate data.
- Why Possibly Novel: A falsifiable decomposability criterion for curriculum benefit, tested on both natural and deliberately non-compositional paths.
- Minimal Experiment: Construct compositional and non-compositional adaptation paths from multi-condition datasets; compare curriculum vs direct adaptation under matched budgets.
- Main Risk: Path construction bias; preregister path definitions before running.
- Research Cluster tag: DOMAIN

### IDEA-A-0169
- Idea: Calibrate label-free shift detectors for dense prediction: measure false-alarm and detection rates of sequential change-detection on prediction statistics, under both real shifts and benign variation.
- Problem: [KNOWN FACT] Deployed systems need to know when input distribution has shifted; existing shift detectors are rarely evaluated for false-alarm behavior under benign variation (weather cycles, daily rhythms).
- Core Hypothesis (falsifiable): [HYPOTHESIS] Standard shift detectors on segmentation output statistics produce operationally unacceptable false-alarm rates under benign periodic variation unless seasonality is explicitly modeled, and seasonality-adjusted variants recover usable operating points; low false-alarm rates out of the box falsify it.
- Why Important: A shift alarm that cries wolf daily gets disabled; realistic false-alarm characterization determines deployability.
- Why Possibly Novel: Evaluates shift detection as an operations problem (alarm economics) with real periodic streams, not IID benchmark splits.
- Minimal Experiment: Run shift detectors on months-long fixed-camera streams with known shift events and benign cycles; report detection/false-alarm tradeoffs with and without seasonal adjustment.
- Main Risk: Ground-truth shift events need documentation; use streams with logged hardware/scene changes.
- Research Cluster tag: DOMAIN

### IDEA-A-0170
- Idea: Per-class shift heterogeneity: demonstrate that domain shift affects classes non-uniformly and that aggregate adaptation metrics hide class-level regressions introduced by adaptation methods.
- Problem: [KNOWN FACT] Adaptation results are reported as mean scores; a method can improve the mean while damaging specific safety-relevant classes.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Common adaptation methods systematically sacrifice rare/small classes to improve dominant ones (a measurable regression signature), and the sacrifice pattern is method-family-specific; uniform per-class improvements falsify it.
- Why Important: Class-level regressions are exactly what safety cases must exclude; hidden sacrifice patterns would be disqualifying evidence currently invisible.
- Why Possibly Novel: Per-class regression accounting as the primary result across adaptation families, with a public regression-reporting standard.
- Minimal Experiment: Run representative adaptation methods on standard benchmarks; report full per-class deltas; test for systematic sacrifice patterns.
- Main Risk: Per-class noise; use multiple seeds and report distributional statistics.
- Research Cluster tag: DOMAIN

### IDEA-A-0171
- Idea: Day-night failure decomposition with paired data: separate photometric failure (same content, darker) from content failure (different objects/activities at night) using fixed-camera day-night pairs.
- Problem: [KNOWN FACT] Night performance drops are reported as a single number, conflating illumination physics with genuine content distribution change.
- Core Hypothesis (falsifiable): [HYPOTHESIS] On fixed scenes, the photometric component (measured on matched static content) explains less than half of the total night drop for dynamic-object tasks, with the remainder attributable to content shift; a photometric-dominated decomposition falsifies it.
- Why Important: The two components demand opposite investments — sensors/enhancement vs nighttime data collection.
- Why Possibly Novel: Fixed-camera pairing as a decomposition instrument gives an unusually clean separation unavailable in standard day/night datasets.
- Minimal Experiment: Annotate day-night pairs from static cameras; evaluate on matched-content subsets vs full night data; report the decomposition.
- Main Risk: Truly matched content is limited to static elements; carefully define which classes each component claim covers.
- Research Cluster tag: DOMAIN

### IDEA-A-0172
- Idea: Compound-shift interaction study: measure whether combined shifts (fog+night, rain+motion-blur) degrade performance multiplicatively, additively, or super-additively relative to individual shifts.
- Problem: [KNOWN FACT] Robustness is evaluated one corruption at a time; real deployments experience compound conditions whose interaction structure is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Specific shift pairs interact super-additively (compound degradation exceeds the independent-composition prediction), and the interaction sign is predictable from whether the shifts corrupt shared cues; consistently additive behavior falsifies it.
- Why Important: If interactions are super-additive, single-corruption benchmarks systematically overestimate deployed robustness in the worst conditions.
- Why Possibly Novel: A factorial interaction analysis of robustness, borrowing the interaction-effect toolkit from experimental design.
- Minimal Experiment: Evaluate models on a factorial grid of shift combinations (real and synthetic); fit interaction models; test cue-sharing predictions.
- Main Risk: Real compound-condition data is scarce; combine synthetic factorials with available real compound sets as validation anchors.
- Research Cluster tag: DOMAIN

### IDEA-A-0173
- Idea: Validity audit of stylization as a robustness proxy: measure how well performance under artistic style transfer predicts performance under real-world shifts across many models.
- Problem: [KNOWN FACT] Stylized data is used as a convenient robustness probe and training augmentation; its predictive validity for real shift robustness is assumed more than measured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Stylization robustness correlates well with texture-type real shifts (sensor, weather) but fails to predict structure-type shifts (viewpoint, geography), making it a partial proxy with definable scope; uniform predictive validity falsifies the scoping claim.
- Why Important: Establishes the boundaries of validity for a widely used research shortcut, preventing overgeneralized robustness claims.
- Why Possibly Novel: Proxy-validity scoping (where the proxy works, where it fails) rather than binary validation.
- Minimal Experiment: For many public models, compute stylization robustness and real-shift robustness across shift types; report correlation structure by shift type.
- Main Risk: Model set diversity is crucial; include multiple pretraining paradigms.
- Research Cluster tag: DOMAIN

### IDEA-A-0174
- Idea: Target-label sample-efficiency curves: measure how many labeled target-domain images are needed to close given fractions of specific domain gaps, producing practical labeling-budget tables.
- Problem: [KNOWN FACT] Practitioners constantly ask "how many target labels do we need?"; the field answers with unsupervised methods rather than measured supervised efficiency curves.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Gap closure follows a predictable saturating curve whose parameters correlate with measurable shift statistics, allowing labeling budgets to be estimated from unlabeled target data; unpredictable curve parameters falsify it.
- Why Important: A budget-prediction tool has immediate industrial value and resets expectations about when unsupervised adaptation is worth its complexity.
- Why Possibly Novel: Treats supervised target labeling as the baseline to beat, with curve-parameter prediction as the scientific contribution.
- Minimal Experiment: For several domain pairs, fine-tune with increasing target-label counts; fit closure curves; regress parameters on shift statistics; validate predictions on held-out pairs.
- Main Risk: Curves depend on adaptation recipe; fix one standard recipe and state scope.
- Research Cluster tag: DOMAIN

### IDEA-A-0175
- Idea: Target-matched source selection: test whether choosing pretraining data subsets matched to the target domain beats indiscriminately larger pretraining for dense tasks, at matched compute.
- Problem: [KNOWN FACT] Scaling pretraining data generally helps, but for a known deployment target, the marginal value of off-target data versus curation is unresolved for dense prediction.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A target-matched subset (selected by computable similarity from unlabeled target data) outperforms the full corpus at equal compute for dense-task transfer, with the advantage growing as target specificity increases; full-corpus dominance falsifies it.
- Why Important: Would legitimize data curation as an alternative to scale for targeted deployments, with large cost implications.
- Why Possibly Novel: Compute-matched curation-vs-scale comparisons for dense prediction with selection driven only by unlabeled target data.
- Minimal Experiment: Pretrain matched-compute models on full vs matched-subset corpora for 3 targets; compare downstream dense-task transfer.
- Main Risk: Pretraining compute cost; use modest model scale and report scale-sensitivity at two budgets.
- Research Cluster tag: DOMAIN

### IDEA-A-0176
- Idea: Multi-source interference: characterize when mixing multiple source domains for training underperforms the single best source, and whether inter-source distance statistics predict the interference.
- Problem: [KNOWN FACT] Practitioners pool all available datasets by default; anecdotes of pooling hurting exist but the conditions are uncharacterized.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Pooling underperforms the best single source when inter-source annotation-convention distance is high even if image-distribution distance is low, and a convention-distance measure predicts interference; unpredictable interference falsifies it.
- Why Important: A pre-pooling compatibility test would prevent silent performance loss in the most common data decision practitioners make.
- Why Possibly Novel: Separates convention incompatibility from image incompatibility as the driver of multi-source interference.
- Minimal Experiment: Train on all subsets of 4-5 source datasets for a fixed target; measure pooling effects; regress on convention- and image-distance measures.
- Main Risk: Combinatorial training cost; use a fractional design over subsets.
- Research Cluster tag: DOMAIN

### IDEA-A-0177
- Idea: Disentangle annotation-style shift from image shift in cross-dataset tests by re-annotating a sample of each dataset under the other's guidelines.
- Problem: [KNOWN FACT] Cross-dataset evaluation confounds image differences with annotation-guideline differences; the confound's size is unknown for dense tasks.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Cross-annotating (dataset A images under dataset B guidelines and vice versa) reveals that a substantial fraction of the measured cross-dataset gap is annotation-style transfer, not image-distribution failure; a negligible fraction falsifies it.
- Why Important: Every cross-dataset generalization number in the literature inherits this confound; measuring it recalibrates the field's understanding of generalization.
- Why Possibly Novel: The bidirectional re-annotation design directly measures the confound instead of arguing about it.
- Minimal Experiment: Re-annotate 300-image samples of two popular dataset pairs under swapped guidelines; recompute cross-dataset scores against both annotation versions; report the decomposition.
- Main Risk: Guideline documents may be incomplete; involve original-team annotators or published protocols.
- Research Cluster tag: DOMAIN

### IDEA-A-0178
- Idea: Camera-ISP fingerprint dependence: test whether dense-prediction models keyed to their training cameras' ISP pipelines degrade when identical scenes are processed through different ISPs, using RAW-reprocessing experiments.
- Problem: [KNOWN FACT] Every camera's ISP applies distinct demosaicing, denoising, and tone mapping; datasets are ISP-homogeneous in ways nobody controls for.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Reprocessing the same RAW captures through different ISP configurations produces performance variation comparable to recognized mild domain shifts, establishing ISP identity as a hidden domain variable; negligible variation falsifies it.
- Why Important: ISP shift happens invisibly with every camera-hardware refresh in deployed fleets; its cost should be known before hardware transitions.
- Why Possibly Novel: RAW-based ISP-swapping isolates the processing pipeline from scene and optics — a clean instrument rarely used in shift research.
- Minimal Experiment: Collect/annotate RAW scenes; process through several ISP configurations; evaluate fixed models per version; report the ISP-induced spread.
- Main Risk: Annotation transfer across versions is trivial (same pixels geometry) but tone-dependent visibility may affect GT validity; annotate on a neutral rendering.
- Research Cluster tag: DOMAIN

### IDEA-A-0179
- Idea: Source-forgetting audit of continual adaptation: measure how much adaptation methods degrade original-domain performance, and whether the stability-plasticity operating point drifts uncontrolled over long streams.
- Problem: [KNOWN FACT] Continual test-time adaptation updates models indefinitely; guarantees about retained source performance are typically absent, and long-horizon drift is rarely measured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Over long adaptation streams, source-domain performance decays without bound for common methods (no stable equilibrium), and periodic source re-evaluation reveals method-specific decay constants; bounded decay for all methods falsifies it.
- Why Important: Systems that must occasionally return to source conditions (seasonal, geographic cycling) need retention guarantees that current evaluation ignores.
- Why Possibly Novel: Long-horizon retention accounting with equilibrium analysis, treating adaptation as a dynamical system with measurable stability properties.
- Minimal Experiment: Run adaptation methods over extended streams with periodic source-set probes; fit retention curves; classify methods by equilibrium behavior.
- Main Risk: Long streams are compute-heavy; use accelerated stress streams and verify with one realistic-length run.
- Research Cluster tag: DOMAIN

### IDEA-A-0180
- Idea: Meta-analysis protocol for corruption-benchmark validity: measure how well synthetic corruption robustness predicts measured real-world shift robustness across many models and shift types.
- Problem: [KNOWN FACT] Synthetic corruption suites are the field's default robustness measure; their predictive validity for real deployment shifts has been questioned but not comprehensively quantified for dense tasks.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Corruption-benchmark rankings predict real-shift rankings well within corruption-analogous shift families and poorly outside them, and the predictive boundary is stable enough to publish as a validity map; uniformly good or bad prediction falsifies the map's need.
- Why Important: The community optimizes against synthetic suites; a validity map tells everyone which conclusions transfer to reality.
- Why Possibly Novel: Scope-resolved validity quantification (per shift family) across a large model zoo for segmentation and detection jointly.
- Minimal Experiment: Evaluate a large model zoo on corruption suites and on curated real-shift sets; compute rank-prediction validity per shift family.
- Main Risk: Real-shift set curation bias; use multiple independent real-shift sources per family.
- Research Cluster tag: DOMAIN

### IDEA-A-0181
- Idea: Cross-task shift-stability ranking: test whether geometric tasks (depth, surface normals) are systematically more robust to appearance shifts than semantic tasks on identical images, and quantify the stability ordering.
- Problem: [KNOWN FACT] Different visual tasks rely on different image properties; a validated task-level robustness ordering under shared shifts does not exist.
- Core Hypothesis (falsifiable): [HYPOTHESIS] On matched shifts and matched training investments, geometric task performance degrades consistently less than semantic segmentation, and the ordering is stable across shift types — enabling geometry as a shift-robust auxiliary signal; inconsistent orderings falsify it.
- Why Important: If geometry is reliably stabler, system designers can anchor safety functions on geometric outputs during shift events.
- Why Possibly Novel: A controlled multi-task shift comparison designed for the ordering question itself, not incidental multi-task results.
- Minimal Experiment: Train matched models per task on shared data; evaluate under a battery of shifts; report the task degradation ordering with confidence intervals.
- Main Risk: Task metrics are incommensurable; use normalized degradation (relative to in-domain) with sensitivity analysis.
- Research Cluster tag: DOMAIN

### IDEA-A-0182
- Idea: Prompt-space adaptation feasibility bounds: for promptable segmentation under image-domain shift, measure how much of the lost performance is recoverable by optimizing prompts alone, with model weights frozen.
- Problem: [KNOWN FACT] Weight adaptation is costly and risky in deployment; prompts are a free-to-change input, but the recoverable-fraction ceiling via prompts alone is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For moderate shifts, a substantial fraction of the domain-shift loss is recoverable purely by shift-aware prompting policies (placement, count, type), and the recoverable fraction shrinks predictably as shift severity grows; negligible recoverability falsifies it.
- Why Important: Establishes the ceiling for the cheapest possible adaptation channel before anyone invests in weight-space methods.
- Why Possibly Novel: Adaptation entirely within the prompt channel, evaluated as a recoverable-fraction bound rather than a method.
- Minimal Experiment: On shifted datasets, search prompt policies (with target labels, as an oracle bound) for frozen models; report recovered fraction vs shift severity.
- Main Risk: Oracle prompt search may overfit per-image; report both per-dataset policy and per-image oracle bounds separately.
- Research Cluster tag: DOMAIN

### IDEA-A-0183
- Idea: Conformal coverage collapse under shift: empirically measure how fast distribution-free coverage guarantees for segmentation uncertainty degrade as shift severity increases, and whether coverage loss is predictable from unlabeled statistics.
- Problem: [KNOWN FACT] Conformal methods guarantee coverage under exchangeability; deployment shift violates the assumption, and the practical decay profile for dense tasks is unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Coverage degrades smoothly and predictably with measurable shift magnitude (not catastrophically at small shifts), allowing a shift-indexed coverage correction to be calibrated; erratic degradation falsifies practical correction.
- Why Important: Uncertainty guarantees are the backbone of safety cases; knowing their real decay profile determines whether they can be certified for deployment.
- Why Possibly Novel: Systematic coverage-decay curves for dense prediction across graded real shifts, with a correction-calibration test.
- Minimal Experiment: Calibrate conformal predictors in-domain; evaluate coverage across graded shift series; fit and validate decay models against unlabeled shift measures.
- Main Risk: Graded real-shift series are rare; combine graded synthetic series with real anchors.
- Research Cluster tag: DOMAIN

### IDEA-A-0184
- Idea: Construct and validate continuous domain-interpolation dials (mixing two real domains at controllable ratios) as standardized instruments for controlled shift experiments.
- Problem: [KNOWN FACT] Shift research jumps between discrete domains; mechanistic understanding needs continuous control over shift magnitude, which current benchmarks cannot provide.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Interpolated domains (via principled image-statistics blending between real domain pairs) produce performance curves that smoothly connect the endpoint performances and correctly predict behavior at unseen intermediate mixing ratios; discontinuous or unpredictable curves falsify instrument validity.
- Why Important: A validated shift dial would upgrade the entire field's experimental methodology from binary comparisons to dose-response science.
- Why Possibly Novel: Treats benchmark construction as instrument calibration, with explicit validity criteria and held-out-ratio prediction tests.
- Minimal Experiment: Build interpolation dials for 3 domain pairs; verify smoothness and predictive validity at held-out ratios against models of varied families.
- Main Risk: Blending may create off-manifold artifacts; include human-plausibility checks and multiple blending mechanisms.
- Research Cluster tag: DOMAIN

### IDEA-A-0185
- Idea: Cost-optimal adaptation economics: build and validate a decision framework that predicts, for a given deployment, whether to spend budget on target labels, adaptation compute, or sensor changes, from measurable shift diagnostics.
- Problem: [KNOWN FACT] Teams facing domain shift choose remedies by intuition; the remedies have wildly different costs and their expected returns are never estimated beforehand.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Expected returns of the three remedy families are predictable from a small diagnostic battery (shift decomposition, sample-efficiency curve parameters, sensor-attribution tests) accurately enough that the framework's recommended remedy matches the empirically best remedy in most held-out deployment scenarios; near-chance recommendation accuracy falsifies it.
- Why Important: Converts the accumulated science of shift into an actionable engineering decision tool — the missing bridge to practice.
- Why Possibly Novel: Integrative validation of a decision procedure (not a method), scored by recommendation correctness on held-out scenarios.
- Minimal Experiment: For 10 deployment-like scenarios with ground truth, run the diagnostic battery, generate recommendations, execute all remedies, and score recommendation accuracy.
- Main Risk: Executing all remedies is expensive; scope scenarios to modest scale but full coverage.
- Research Cluster tag: DOMAIN

---

## Section 6 — Prompt sensitivity (IDEA-A-0186 .. 0220)

### IDEA-A-0186
- Idea: Paraphrase-variance census for text-prompted segmentation: measure output variance across semantically equivalent prompt phrasings and identify which linguistic dimensions (register, word order, determiner choice) drive it.
- Problem: [KNOWN FACT] Text-prompted segmenters accept natural language; semantically equivalent phrasings are treated as interchangeable by users but not necessarily by models.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Output variance across verified-equivalent paraphrases is large (comparable to moderate image perturbations) and concentrated in specific, identifiable linguistic dimensions; near-zero paraphrase variance falsifies it.
- Why Important: Users cannot be expected to find magic phrasings; quantified paraphrase fragility defines the real usability of text-prompted systems.
- Why Possibly Novel: A controlled linguistic decomposition of prompt variance (which language feature causes it), not just a variance report.
- Minimal Experiment: Build paraphrase sets varying one linguistic dimension at a time (validated for equivalence by annotators); measure per-dimension output variance across models.
- Main Risk: Verifying semantic equivalence; use multi-annotator equivalence validation.
- Research Cluster tag: PROMPT

### IDEA-A-0187
- Idea: Template-sensitivity audit for dense prediction: measure how much prompt templates ("a photo of X" variants) change open-vocabulary segmentation rankings between models, not just absolute scores.
- Problem: [KNOWN FACT] Template choice is known to move absolute scores; whether it changes model comparisons (the basis of scientific claims) is less examined for dense tasks.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Across a standard template battery, a nontrivial fraction of published pairwise model orderings in open-vocabulary segmentation invert, meaning template choice is silently embedded in claimed superiority; stable orderings falsify it.
- Why Important: If rankings are template-dependent, comparison studies need template-marginalized reporting to be trustworthy.
- Why Possibly Novel: The ranking-stability (rather than score-level) analysis of template sensitivity for segmentation.
- Minimal Experiment: Re-evaluate public open-vocabulary segmenters under a large template battery; report ordering-inversion rates and template-marginalized rankings.
- Main Risk: Template battery selection bias; use community-sourced and randomly generated templates.
- Research Cluster tag: PROMPT

### IDEA-A-0188
- Idea: Simulator-validity study for interactive segmentation: compare where real humans click against the simulated click policies used in evaluation, and measure how the mismatch distorts reported performance.
- Problem: [KNOWN FACT] Interactive segmentation is benchmarked with scripted click simulators (center-of-largest-error strategies); real user behavior is different in unquantified ways.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Real-user click distributions differ systematically from simulators (edge-attraction, saliency bias, motor noise), and evaluating with real-user clicks changes both absolute scores and model rankings; simulator-consistent behavior falsifies it.
- Why Important: If simulators mispredict rankings, the interactive-segmentation literature is optimizing for phantom users.
- Why Possibly Novel: A direct behavioral comparison feeding back into benchmark validity, with a released real-click corpus.
- Minimal Experiment: Collect real click trajectories from users correcting masks; compare distributions to simulators; re-evaluate models under real-click replay.
- Main Risk: User pools vary; sample multiple experience levels and report stratified.
- Research Cluster tag: PROMPT

### IDEA-A-0189
- Idea: Standardized negative-prompt battery: characterize how differently current promptable models interpret negative/exclusion prompts and whether any consistent semantics exists across model families.
- Problem: [KNOWN FACT] Negative prompting (excluding regions/concepts) is supported inconsistently across models; users transfer intuitions between tools that may implement opposite behaviors.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Given identical negative-prompt scenarios, model families diverge qualitatively (exclusion vs suppression vs global re-segmentation), and no family implements a semantics matching majority user expectation measured by survey; convergent semantics falsifies it.
- Why Important: Semantics divergence means user skills don't transfer between tools and errors are systematic; documentation and standardization need the evidence.
- Why Possibly Novel: Cross-model behavioral semantics comparison anchored to empirically measured user expectations.
- Minimal Experiment: Design a negative-prompt scenario battery; run it across model families; survey users for expected outcomes; report the semantics matrix and expectation gaps.
- Main Risk: Scenario battery coverage; derive scenarios from real annotation-tool logs.
- Research Cluster tag: PROMPT

### IDEA-A-0190
- Idea: Prompt-ensemble uncertainty calibration: test whether variance over prompt paraphrases/jitters yields calibrated uncertainty for open-vocabulary segmentation, validated against true error.
- Problem: [KNOWN FACT] Open-vocabulary segmenters offer no usable uncertainty; prompt-space ensembling is free at inference and its calibration properties are unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Prompt-ensemble disagreement, after a single monotone recalibration per model, is a well-calibrated error predictor that transfers across datasets; non-transferring calibration falsifies it.
- Why Important: Free calibrated uncertainty would immediately upgrade every deployed open-vocabulary pipeline's safety.
- Why Possibly Novel: Rigorous calibration-theoretic treatment (reliability diagrams, proper scoring) of prompt-space ensembles for dense prediction.
- Minimal Experiment: Compute prompt-ensemble disagreement maps on several datasets; fit one recalibration; report transfer calibration on held-out datasets.
- Main Risk: Overlaps conceptually with click-jitter ensembles (see IDEA-A-0040); differentiate by studying the text-prompt channel specifically.
- Research Cluster tag: PROMPT

### IDEA-A-0191
- Idea: Referring-expression ambiguity benchmark: measure how models behave when a referring prompt legitimately matches multiple objects, and whether any current system signals the ambiguity instead of guessing.
- Problem: [KNOWN FACT] Real referring expressions are often ambiguous ("the person on the left" with three left-side people); models must guess, and their guessing policy is uncharacterized.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Under controlled ambiguity, models choose referents by stable dataset-inherited biases (size, centrality, salience) rather than randomly, and none reliably signals ambiguity; random choice or reliable signaling falsifies it.
- Why Important: Guessing silently on ambiguous instructions is dangerous in robotics; measured bias profiles enable both warnings and better UX design.
- Why Possibly Novel: Ambiguity as a designed experimental variable with per-model bias fingerprints, plus an ambiguity-signaling capability audit.
- Minimal Experiment: Construct scenes with controlled multi-referent ambiguity; measure referent-choice distributions and any confidence signals; fit bias models per system.
- Main Risk: Constructed scenes may look synthetic; complement with mined natural ambiguous cases.
- Research Cluster tag: PROMPT

### IDEA-A-0192
- Idea: Cross-lingual prompt gap census: measure open-vocabulary segmentation performance across languages for identical images and translated prompts, mapping the language-inequality landscape.
- Problem: [KNOWN FACT] Vision-language pretraining is English-dominated; the per-language performance gap for dense prediction is largely unmeasured beyond anecdote.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Performance degrades with language resource level in pretraining corpora, but with class-dependent exceptions (visual concepts with strong native-language web presence resist the gap), making the gap partially predictable per class-language pair; uniform gaps falsify the class-dependence.
- Why Important: Language inequality in vision tools is an accessibility and fairness issue that needs numbers before remedies.
- Why Possibly Novel: Class-language interaction analysis (not just per-language averages) tied to corpus statistics.
- Minimal Experiment: Evaluate open-vocabulary segmenters with professionally translated prompts across 10 languages on a fixed image set; model the gap vs language and class covariates.
- Main Risk: Translation quality confounds; use back-translation validation and native-speaker review.
- Research Cluster tag: PROMPT

### IDEA-A-0193
- Idea: Universal box-jitter response curves: test whether the shape of the prompt-jitter degradation curve is a model-family invariant across promptable and open-vocabulary detectors/segmenters.
- Problem: [KNOWN FACT] Box-prompt sensitivity exists per model (cf. IDEA-A-0008 for SAM); whether degradation-curve shapes are universal or family-specific determines if one robustness spec can cover all models.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Normalized jitter-response curves collapse onto a small number of universal shapes corresponding to prompt-encoding designs, enabling family-level robustness certification; idiosyncratic per-model curves falsify it.
- Why Important: Universality would let system integrators certify prompt-robustness by family instead of per-model testing.
- Why Possibly Novel: A cross-model collapse analysis (in the physics sense of curve collapse) applied to prompt perturbation behavior.
- Minimal Experiment: Measure jitter-response curves for 10+ promptable models; normalize and cluster curve shapes; test alignment with prompt-encoding design categories.
- Main Risk: Normalization choices drive collapse; preregister normalization and show alternatives.
- Research Cluster tag: PROMPT

### IDEA-A-0194
- Idea: Prompt-order effects in sequential multi-object prompting: measure whether earlier prompts/masks change later outputs within a session (state leakage), and characterize the interference structure.
- Problem: [KNOWN FACT] Interactive tools segment many objects sequentially in one session; whether model or implementation state couples the outputs is undocumented for practitioners.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For stateful implementations (video memory, cached features), object masks measurably depend on prompting order, with interference strongest between visually similar objects; order-invariant outputs falsify it.
- Why Important: Order-dependent outputs violate annotator assumptions and make QA irreproducible; the effect must be quantified to be managed.
- Why Possibly Novel: Session-level (not single-prompt) behavioral analysis of promptable systems as they are actually used.
- Minimal Experiment: Segment fixed object sets under permuted prompting orders across implementations; measure per-object output variance attributable to order.
- Main Risk: Stateless implementations trivially pass; focus on video and cached-state systems where the question is live.
- Research Cluster tag: PROMPT

### IDEA-A-0195
- Idea: Exemplar-vs-text disagreement as an error flag: when visual-exemplar prompting and text prompting for the same concept disagree, does the disagreement predict that both are wrong?
- Problem: [KNOWN FACT] Some systems accept both prompt modalities for the same concept; agreement/disagreement between the two channels is free information nobody uses.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Cross-modal prompt disagreement is a strong predictor of true error (regions where they disagree are mostly wrong in at least one), usable as an automatic review flag with quantified precision; disagreement uncorrelated with error falsifies it.
- Why Important: A free error flag from redundant prompting channels would improve auto-annotation pipelines immediately.
- Why Possibly Novel: Treats prompt modalities as redundant sensors and applies agreement-based fault detection logic to them.
- Minimal Experiment: On datasets with GT, prompt models via text and exemplar for identical concepts; measure error rates inside vs outside disagreement regions.
- Main Risk: Channels may share failure modes (both inherited from the same encoder); measure and report correlated-failure rates.
- Research Cluster tag: PROMPT

### IDEA-A-0196
- Idea: Prompt-length dose-response: measure open-vocabulary segmentation quality as description length grows from one word to full sentences, testing for an inverted-U and identifying where added detail starts to hurt.
- Problem: [KNOWN FACT] Users assume more descriptive prompts help; the actual length-performance relationship for dense prediction is unmapped.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Performance follows an inverted-U in description length: initial gains from disambiguation, then degradation as rare constructions and attribute clutter dilute the target signal; monotone behavior in either direction falsifies it.
- Why Important: Produces concrete prompting guidance (optimal length bands) and reveals a capability ceiling of text conditioning for dense tasks.
- Why Possibly Novel: Controlled length manipulation with content held fixed (adding verified-true detail), isolating length from correctness.
- Minimal Experiment: Build nested prompt sets of increasing verified-true detail for fixed targets; measure performance vs length across models.
- Main Risk: Length confounds with syntactic complexity; include matched-complexity controls.
- Research Cluster tag: PROMPT

### IDEA-A-0197
- Idea: Spatial-relation grounding audit: systematically test "left of / behind / on top of" prompts and characterize the reference-frame errors (viewer-centric vs object-centric confusion) models make.
- Problem: [KNOWN FACT] Spatial relations are frequent in real instructions; vision-language models' reference-frame handling is inconsistent and unmapped for segmentation outputs.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Errors are dominated by systematic reference-frame confusion (predictable flips) rather than random failure, and the dominant frame differs by relation type; unsystematic errors falsify it.
- Why Important: Predictable frame confusion can be corrected in the interface layer today, but only if its structure is documented.
- Why Possibly Novel: Reference-frame taxonomy testing borrowed from spatial cognition, applied to dense grounding with output masks as evidence.
- Minimal Experiment: Construct scenes where viewer- and object-centric readings pick different referents; measure which frame each model uses per relation; report the confusion structure.
- Main Risk: Natural scenes rarely isolate frames cleanly; use staged/rendered scenes with natural-image validation anchors.
- Research Cluster tag: PROMPT

### IDEA-A-0198
- Idea: Quantifier blindness test: measure whether prompts containing counts ("three dogs") influence segmentation/detection outputs at all, across current vision-language systems.
- Problem: [KNOWN FACT] Language encoders process quantifiers, but whether dense-prediction heads use them (returning exactly three instances) is doubtful and undocumented.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Outputs are statistically invariant to the numeral in the prompt (quantifier blindness) even when the correct count is visually unambiguous; count-sensitive outputs falsify it.
- Why Important: Users writing counts believe they are constraining the system; documented blindness prevents silent instruction violations in applications.
- Why Possibly Novel: A capability audit isolating one linguistic feature (numerals) with output-level behavioral measurement.
- Minimal Experiment: Prompt with varying numerals on scenes with known instance counts; measure output-count distributions per numeral; test invariance.
- Main Risk: Some systems may partially respond; report effect sizes, not binary verdicts.
- Research Cluster tag: PROMPT

### IDEA-A-0199
- Idea: Attribute-binding stress test for dense prediction: measure whether "red car next to blue truck" prompts bind attributes to the correct objects in segmentation outputs, and how binding failure scales with scene clutter.
- Problem: [KNOWN FACT] Attribute binding is a known weakness of contrastive vision-language representations; its manifestation in dense outputs (masks on the wrong-colored object) is less quantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Binding-failure rate (mask lands on the distractor with swapped attributes) grows steeply with the number of same-category distractors, and failure is asymmetric across attribute types (color binds better than size); clutter-independent binding falsifies it.
- Why Important: Binding failures cause exactly-wrong outputs (confidently segmenting the wrong instance), the most misleading kind for downstream use.
- Why Possibly Novel: Dense-output binding measurement with parametric clutter control and attribute-type decomposition.
- Minimal Experiment: Construct scenes with attribute-swapped distractor pairs at varying clutter; prompt with attribute-composed queries; measure binding accuracy per attribute type and clutter level.
- Main Risk: Constructed scenes; validate on mined natural scenes with verified attribute-swapped pairs.
- Research Cluster tag: PROMPT

### IDEA-A-0200
- Idea: Compositional-prompt scaling law: measure how grounding accuracy decays as prompt compositional depth increases (object → object+attribute → object+attribute+relation → nested clauses).
- Problem: [KNOWN FACT] Real instructions compose several constraints; the decay profile of dense grounding with compositional depth is uncharacterized, so nobody knows the usable-complexity budget.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Accuracy decays approximately geometrically with compositional depth (a per-constraint success factor), and the factor is model-specific but constraint-type-independent, enabling a simple complexity budget; non-multiplicative decay falsifies it.
- Why Important: A "constraints budget" tells interface designers how much to decompose complex user instructions before passing them to models.
- Why Possibly Novel: Treats compositional grounding as a reliability-engineering problem with a measurable per-stage success rate.
- Minimal Experiment: Build prompt hierarchies of increasing depth with verified GT; measure accuracy vs depth; test the multiplicative model per system.
- Main Risk: Deeper prompts are also longer (cf. IDEA-A-0196); include length-matched controls.
- Research Cluster tag: PROMPT

### IDEA-A-0201
- Idea: Prompt-response fingerprinting: test whether a model's identity (family, version) can be recovered purely from its response pattern to a battery of probe prompts, enabling black-box model forensics.
- Problem: [KNOWN FACT] Deployed segmentation APIs hide their underlying models; auditors, customers, and researchers currently cannot verify claims about which model serves an endpoint.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Prompt-sensitivity signatures (response vectors over a designed probe battery) separate model families and even versions with high accuracy, surviving moderate post-processing; non-separable signatures falsify it.
- Why Important: Enables auditing of model-provenance claims and detection of silent model swaps behind APIs — an accountability tool.
- Why Possibly Novel: Turns prompt sensitivity, usually a defect, into an identification instrument with forensic applications.
- Minimal Experiment: Build a probe battery; collect response signatures from many public models/versions; train/test a classifier on held-out instances and post-processing perturbations.
- Main Risk: Fingerprints may drift with serving configurations; test robustness across configuration variants.
- Research Cluster tag: PROMPT

### IDEA-A-0202
- Idea: Prompting-skill learnability study: measure how quickly novice users approach expert prompting efficiency for interactive segmentation, and which skill components (placement, sequencing, modality choice) transfer across models.
- Problem: [KNOWN FACT] Interactive tools implicitly assume users learn effective prompting; the learning curve and the transferability of prompting skills across tools are unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Prompting skill develops in distinct components with different learning rates, and placement skill transfers across models while sequencing skill is model-specific — implying interface standardization priorities; uniform transfer falsifies it.
- Why Important: Annotation workforce training is a large cost; component-level learning data would optimize training and tool design.
- Why Possibly Novel: Human skill-acquisition methodology applied to prompt engineering for vision, with cross-tool transfer testing.
- Minimal Experiment: Longitudinal user study: novices practice on one model, then switch; measure per-component efficiency trajectories and transfer.
- Main Risk: User-study logistics; a two-session design with 20 participants already tests the transfer claims.
- Research Cluster tag: PROMPT

### IDEA-A-0203
- Idea: In-image text overrides user text: measure whether typographic content inside images (labels, signs) can hijack text-prompted segmentation away from the user's actual instruction.
- Problem: [KNOWN FACT] Typographic attacks affect vision-language classifiers; whether written words in a scene override the prompt channel in dense prediction (e.g., prompting "cat" segments a sign reading "cat") is unquantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Scene text semantically matching the prompt attracts masks at rates far above matched no-text controls, with strength growing with text prominence — a prompt-injection channel through the image; no attraction falsifies it.
- Why Important: A working injection channel is a security issue for automated pipelines processing user-supplied or public-scene images.
- Why Possibly Novel: Frames typographic interference as cross-channel prompt injection for dense prediction, with dose-response measurement.
- Minimal Experiment: Composite prompt-matching vs mismatched text into scenes at controlled prominence; prompt for the concept; measure mask-attraction rates per condition.
- Main Risk: Compositing artifacts; include real photographed signage subsets.
- Research Cluster tag: PROMPT

### IDEA-A-0204
- Idea: Per-prompt threshold spread in open-vocabulary segmentation: measure how much the optimal score threshold varies across prompts, invalidating the single-global-threshold assumption.
- Problem: [KNOWN FACT] Deployment pipelines fix one confidence threshold; open-vocabulary scores are prompt-conditional, and their comparability across prompts is assumed without evidence.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Per-prompt optimal thresholds are widely spread (a global threshold sacrifices large performance for many prompts), and the per-prompt optimum is predictable from prompt statistics (frequency, specificity) enabling threshold auto-selection; a tight spread falsifies it.
- Why Important: A predictable threshold correction is a free accuracy gain for every open-vocabulary deployment.
- Why Possibly Novel: Score-comparability across the prompt dimension treated as a measurable calibration problem with a practical predictor.
- Minimal Experiment: Compute per-prompt optimal thresholds on labeled data across many prompts; quantify spread and the cost of a global threshold; fit and validate a threshold predictor from prompt features.
- Main Risk: Optimal thresholds are noisy for rare prompts; use hierarchical estimation.
- Research Cluster tag: PROMPT

### IDEA-A-0205
- Idea: Iterative language-refinement dynamics: test whether conversational prompt refinement ("no, the other one, more to the left") converges, oscillates, or diverges in current referring-segmentation systems.
- Problem: [KNOWN FACT] Real users refine failed instructions with follow-up language; multi-turn refinement behavior of dense grounding systems is essentially unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Under scripted correction dialogues, a substantial fraction of refinement sequences fail to converge (oscillate between wrong referents or drift), with failure predictable from initial-error type; reliable convergence falsifies it.
- Why Important: Multi-turn correction is the natural UX for language-driven vision; its instability profile determines whether it is shippable.
- Why Possibly Novel: Dynamical analysis (convergence/oscillation classification) of multi-turn grounding, parallel in spirit to click-refinement analysis (IDEA-A-0017) but in the language channel.
- Minimal Experiment: Script correction dialogues from error taxonomies; run multi-turn systems; classify trajectory outcomes and predictors.
- Main Risk: Few systems support true multi-turn state; include stateless re-prompting as a comparison condition.
- Research Cluster tag: PROMPT

### IDEA-A-0206
- Idea: Prompt-overfitting generalization gap: measure how much prompt engineering tuned on one dataset transfers to other datasets for the same concepts, quantifying "prompt overfitting."
- Problem: [KNOWN FACT] Papers and practitioners tune prompts on a development set; the transferability of tuned prompts is assumed, and any overfitting inflates reported open-vocabulary performance.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Prompts optimized on dataset A lose a substantial fraction of their gain on dataset B (same concepts, different images), and the loss grows with tuning intensity — a measurable prompt-generalization gap; full transfer falsifies it.
- Why Important: Defines how much of published prompt-based improvement is real capability versus development-set artifact.
- Why Possibly Novel: Treats prompts as parameters subject to overfitting analysis with train/test methodology, quantified across tuning budgets.
- Minimal Experiment: Optimize prompts per concept on dataset A at several search budgets; evaluate on datasets B/C; plot the generalization gap vs budget.
- Main Risk: Concept alignment across datasets; use verified shared-concept subsets.
- Research Cluster tag: PROMPT

### IDEA-A-0207
- Idea: Lexical-robustness index: measure output stability under synonym substitution from standard lexical resources, producing a per-model robustness score for open-vocabulary segmentation.
- Problem: [KNOWN FACT] Different users use different words for the same concept; per-model tolerance to lexical variation is not reported by anyone, though it determines real-world consistency.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Lexical robustness varies widely across models and correlates with text-encoder pretraining corpus breadth rather than with benchmark accuracy — i.e., leaderboards don't reveal it; accuracy-correlated robustness falsifies it.
- Why Important: A standard reported robustness index would let practitioners select models for heterogeneous user populations.
- Why Possibly Novel: A standardized, corpus-grounded lexical perturbation battery with model-property correlation analysis.
- Minimal Experiment: Build synonym-substitution batteries; measure output stability per model; correlate with accuracy and with available pretraining metadata.
- Main Risk: Synonyms carry subtle sense differences; filter pairs via sense-annotated resources and human validation.
- Research Cluster tag: PROMPT

### IDEA-A-0208
- Idea: Graded-quantity prompts for amorphous targets: test whether models respond meaningfully to vague quantity language ("some smoke," "heavy smoke," "a little smoke") and whether responses align with human opacity/extent judgments.
- Problem: [KNOWN FACT] Amorphous phenomena are naturally described with graded language; whether dense models map such gradations to anything measurable is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Model outputs are nearly invariant to graded quantity modifiers even when humans reliably map them to distinct extent/opacity ranges — a documented expressivity gap; graded-responsive outputs falsify it.
- Why Important: For amorphous safety applications, graded language is the natural operator interface; documenting the gap motivates threshold-conditioned formulations (cf. IDEA-A-0083).
- Why Possibly Novel: Connects graded linguistic semantics to dense-output behavior with human-judgment anchoring.
- Minimal Experiment: Collect human extent/opacity mappings for graded modifiers; prompt models with the graded battery on smoke scenes; compare response functions.
- Main Risk: Human mappings vary; model the distribution, not a point estimate.
- Research Cluster tag: PROMPT

### IDEA-A-0209
- Idea: Click-budget laws by object category: fit and validate parametric performance-vs-click-count curves per object category, enabling annotation-cost forecasting from category composition alone.
- Problem: [KNOWN FACT] Annotation project planning needs cost forecasts; clicks-to-quality curves are reported as dataset averages, not as reusable per-category laws.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Click-response curves follow a common parametric family whose parameters are stable per category across datasets, so a project's cost is predictable from its category mix; unstable parameters falsify it.
- Why Important: Turns interactive-segmentation evaluation into an actionable cost model for the annotation industry.
- Why Possibly Novel: Cross-dataset stability testing of curve parameters — the difference between a benchmark number and a reusable law.
- Minimal Experiment: Fit curves per category on dataset A; predict clicks-to-target-quality on dataset B from category mix; measure forecast error.
- Main Risk: Category granularity choice; test at two taxonomy levels.
- Research Cluster tag: PROMPT

### IDEA-A-0210
- Idea: Default-salience census: characterize what promptable models segment when given empty, degenerate, or uninformative prompts, exposing the internal salience prior that biases all prompted outputs.
- Problem: [KNOWN FACT] Every promptable model must resolve underdetermined prompts using internal priors; the prior's content (centrality, size, class biases) is unmeasured yet shapes prompted behavior.
- Core Hypothesis (falsifiable): [HYPOTHESIS] The empty-prompt output distribution reveals a stable, model-specific salience prior that measurably predicts prompted-output biases in ambiguous cases (the prior "leaks" into prompted mode); no predictive relation falsifies it.
- Why Important: If the prior leaks, its biases (e.g., against small/peripheral objects) silently distort even well-prompted usage — a documentable correction target.
- Why Possibly Novel: Connects unprompted behavior to prompted-mode bias with a quantitative leakage test.
- Minimal Experiment: Collect empty/degenerate-prompt outputs at scale; fit prior models; test their prediction of prompted-output choices on ambiguous scenes.
- Main Risk: Degenerate prompts may trigger special-cased behavior; use several degenerate-prompt constructions.
- Research Cluster tag: PROMPT

### IDEA-A-0211
- Idea: Negation blindness in dense grounding: test whether "not," "without," and exclusion constructions in prompts have any measurable effect on segmentation outputs.
- Problem: [KNOWN FACT] Negation is notoriously hard for contrastive text encoders; the consequence for dense outputs (e.g., "the mug without the logo") is unquantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Outputs for negated prompts are statistically indistinguishable from outputs for the un-negated versions (full negation blindness) across current systems, even for visually trivial cases; negation-sensitive outputs falsify it.
- Why Important: Users rely on exclusions constantly; documented blindness with effect sizes should gate what interfaces allow users to type.
- Why Possibly Novel: Behavioral, output-level negation audit for segmentation with matched minimal pairs.
- Minimal Experiment: Build minimal prompt pairs differing only in negation, with scenes where correct outputs differ; measure output divergence per system.
- Main Risk: Some negations are pragmatically odd; validate prompt naturalness with speakers.
- Research Cluster tag: PROMPT

### IDEA-A-0212
- Idea: Fine-tuning shifts the optimal prompt distribution: measure how the best prompting policy for a model changes after domain fine-tuning, and whether stale prompting policies cause hidden post-fine-tuning underperformance.
- Problem: [KNOWN FACT] Teams fine-tune promptable models but keep their old prompting habits; whether prompt policy and weights co-adapt is unexamined.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Fine-tuning systematically shifts optimal prompt characteristics (placement tolerance, type preference), and re-optimizing prompts post-fine-tune recovers a measurable additional gain that most workflows currently leave on the table; policy-invariance falsifies it.
- Why Important: A free post-fine-tuning gain (just change prompting) with quantified size would immediately change practice.
- Why Possibly Novel: Studies the interaction between the two adaptation channels (weights and prompts) instead of either alone.
- Minimal Experiment: Fine-tune models on several domains; re-optimize prompting policies before/after; measure the recoverable gain and characterize the policy shift.
- Main Risk: Interaction may be recipe-specific; replicate over two fine-tuning recipes.
- Research Cluster tag: PROMPT

### IDEA-A-0213
- Idea: Time-normalized interaction comparison: evaluate scribbles vs clicks vs boxes by information delivered per second of real human effort, rather than per interaction count.
- Problem: [KNOWN FACT] Interaction types are compared per-click/per-box, but a scribble costs more human time than a click; count-based comparisons systematically misrank interaction modalities.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Under human-time normalization, the modality ranking changes substantially from count-based rankings (e.g., scribbles lose their apparent advantage), and the time-normalized ranking varies by object category; identical rankings falsify it.
- Why Important: Annotation tools choose default modalities based on per-count studies; time-normalized evidence could reverse those choices and save real money.
- Why Possibly Novel: Grounds interactive-segmentation evaluation in measured human time — the actual scarce resource — with category-conditional recommendations.
- Minimal Experiment: Measure human execution times per modality in a controlled study; re-normalize existing benchmark curves; produce time-based rankings per category.
- Main Risk: Time depends on interface quality; use two interface implementations and report sensitivity.
- Research Cluster tag: PROMPT

### IDEA-A-0214
- Idea: Intent-conditioned evaluation: measure inter-user prompt variability for the same annotation intent and develop an evaluation protocol that scores models against the intent rather than the literal prompt.
- Problem: [KNOWN FACT] Different users express the same target with different prompts; models are evaluated per-prompt, punishing or rewarding them for prompt idiosyncrasies rather than intent satisfaction.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Variance across users' prompts for the same intent contributes a large share of measured output variance (the intent-conditional model performance is much more stable), and intent-based scoring changes model comparisons; prompt-variance being negligible falsifies it.
- Why Important: Separates "the model is inconsistent" from "users are diverse" — a distinction every deployment postmortem needs.
- Why Possibly Novel: Formalizes intent as the evaluation unit with a collected intent-prompt corpus, importing the speaker-variation mindset from linguistics.
- Minimal Experiment: Collect many users' prompts for fixed intents; decompose output variance into user vs model components; compare model rankings under prompt- vs intent-conditioned scoring.
- Main Risk: Operationalizing intent; use scenario cards with unambiguous target definitions.
- Research Cluster tag: PROMPT

### IDEA-A-0215
- Idea: Does multimask diversity track prompt ambiguity? Test whether the diversity of a promptable model's multiple outputs actually correlates with the objective ambiguity of the prompt, across ambiguity types.
- Problem: [KNOWN FACT] Multimask outputs were designed for ambiguity handling; whether their diversity is calibrated to real ambiguity (rather than constant or arbitrary) is unverified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Multimask diversity increases with objectively constructed prompt ambiguity for part-whole ambiguity but fails to respond to instance ambiguity (which candidate object), revealing a specific representational gap; uniform tracking falsifies the gap claim.
- Why Important: If diversity ignores instance ambiguity, downstream systems that trust multimask coverage will miss exactly the multi-object confusions that matter.
- Why Possibly Novel: Ambiguity-type-resolved calibration analysis of the multimask mechanism against designed ground-truth ambiguity.
- Minimal Experiment: Construct prompt scenarios with controlled ambiguity types and known valid-answer sets; measure output-set coverage and diversity per type.
- Main Risk: Valid-answer sets require careful construction; use multi-annotator validation of the answer sets.
- Research Cluster tag: PROMPT

### IDEA-A-0216
- Idea: Tokenizer-fragmentation penalty: test whether class names that fragment into many subword tokens systematically underperform in open-vocabulary detection/segmentation, controlling for concept frequency.
- Problem: [KNOWN FACT] Text encoders tokenize rare words into subword pieces; whether fragmentation itself (beyond rarity) costs dense-task performance is untested.
- Core Hypothesis (falsifiable): [HYPOTHESIS] At matched concept frequency and visual difficulty, higher token-fragmentation names score measurably worse, and single-token aliases for the same concept recover the gap; no fragmentation effect falsifies it.
- Why Important: A fragmentation penalty would justify simple engineering fixes (alias substitution) worth points of recall in technical vocabularies (species, medical terms, product names).
- Why Possibly Novel: Isolates a tokenizer-level mechanism via alias-substitution experiments — a clean causal design in the text channel.
- Minimal Experiment: Assemble concept sets with multiple names of differing fragmentation; evaluate per name; test the alias-recovery prediction.
- Main Risk: Frequency-fragmentation confound; control with corpus-frequency matching.
- Research Cluster tag: PROMPT

### IDEA-A-0217
- Idea: Register gap: measure the performance difference between colloquial and technical prompt vocabulary for identical targets ("kneecap" vs "patella"), mapping which domains suffer the largest register penalties.
- Problem: [KNOWN FACT] Professional users prompt in technical language; pretraining text skews colloquial, but the size and structure of the register penalty for dense tasks is unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Technical-register prompts underperform colloquial equivalents by domain-dependent margins that correlate with the register composition of web text, and mixing both registers in a prompt recovers most of the penalty; no register penalty falsifies it.
- Why Important: Professional deployments (medicine, manufacturing, law enforcement) naturally use technical language; a documented penalty and cheap mitigation matter immediately.
- Why Possibly Novel: Register (not language or length) as the isolated linguistic variable, with a practical mixed-register mitigation test.
- Minimal Experiment: Build colloquial/technical prompt pairs across domains; measure per-domain gaps; test mixed-register prompts as mitigation.
- Main Risk: Pair equivalence; validate with domain experts.
- Research Cluster tag: PROMPT

### IDEA-A-0218
- Idea: Exemplar-scale sensitivity: measure how visual-prompt (exemplar patch) size and framing change one-shot segmentation behavior, defining robust exemplar-construction guidelines.
- Problem: [KNOWN FACT] Visual prompting supplies an example patch; how patch scale, margin, and background inclusion affect the result is folklore rather than measurement.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Exemplar effectiveness varies strongly and systematically with patch framing (tight crops overweight texture, loose crops overweight context), producing predictable error modes per framing choice; framing-invariance falsifies it.
- Why Important: Exemplar construction is a user-controlled free variable; guidelines derived from dose-response data would standardize a currently arbitrary practice.
- Why Possibly Novel: Parametric framing sweeps with error-mode attribution, giving mechanism-level explanations for exemplar failures.
- Minimal Experiment: Sweep exemplar crops (scale, margin) for fixed targets across visual-prompting models; measure performance and classify error modes per framing.
- Main Risk: Model-specific effects; test across at least three visual-prompting systems.
- Research Cluster tag: PROMPT

### IDEA-A-0219
- Idea: Grid-alignment artifacts in point prompting: test whether clicks at patch-boundary positions behave measurably differently from patch-center positions, revealing tokenization-induced spatial nonuniformity in prompt handling.
- Problem: [KNOWN FACT] Vision transformers discretize images into patches; prompt encoders interpolate positions, but whether effective prompt sensitivity is spatially uniform at sub-patch scale is untested.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Prompt effectiveness exhibits periodic structure aligned with the patch grid (measurably different outcomes for boundary-adjacent vs center clicks on identical content), constituting a tokenization artifact in the prompt channel; spatially uniform sensitivity falsifies it.
- Why Important: A periodic artifact would mean annotation outcomes depend on pixel-level luck, and sub-patch prompt placement guidance could exploit or avoid it.
- Why Possibly Novel: Sub-patch spatial analysis of the prompt channel — finer-grained than any existing prompt-robustness work.
- Minimal Experiment: Sample dense sub-patch click grids on translated copies of identical content; measure outcome periodicity against the patch grid; test across models with different patch sizes.
- Main Risk: Effects may be tiny; use paired designs and large samples for statistical power.
- Research Cluster tag: PROMPT

### IDEA-A-0220
- Idea: Test-set prompt-tuning contamination audit: quantify how often published open-vocabulary results depend on prompts selected using test-set feedback, and measure the inflation this causes.
- Problem: [KNOWN FACT] Prompt selection is often done with access to test metrics (implicitly or explicitly); the community lacks an estimate of the resulting inflation for dense tasks.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Re-evaluating published prompt configurations under clean protocols (prompts frozen before test access, or cross-validated) reduces reported open-vocabulary gains by a measurable, nontrivial margin in a substantial fraction of cases; negligible reduction falsifies it.
- Why Important: If prompt-tuning contamination is material, the field's open-vocabulary progress narrative needs correction and future work needs protocol standards.
- Why Possibly Novel: A contamination-quantification study with a proposed clean-protocol standard, parallel to hyperparameter-contamination audits in other areas.
- Minimal Experiment: Select representative published configurations; re-evaluate under prompt-freeze and cross-validation protocols; report the inflation distribution.
- Main Risk: Reconstructing published setups is imperfect; involve original authors where possible and report reconstruction confidence.
- Research Cluster tag: PROMPT

---

## Section 7 — Fine-tuning instability / PEFT / catastrophic forgetting (IDEA-A-0221 .. 0260)

### IDEA-A-0221
- Idea: Map the adapter-capacity/forgetting frontier: measure how low-rank adapter capacity trades off target-task gain against zero-shot capability retention for promptable segmentation models, as an empirical law.
- Problem: [KNOWN FACT] PEFT capacity (e.g., adapter rank) is chosen by convention; its causal relationship to capability retention for dense-prediction foundation models is not established as a reusable curve.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Retention-vs-gain traces a smooth frontier parameterized by adapter capacity, with a capacity threshold beyond which forgetting accelerates sharply, and the threshold scales with target-domain distance; no systematic frontier falsifies it.
- Why Important: Practitioners could pick capacity from measured curves instead of folklore, with predictable retention consequences.
- Why Possibly Novel: Frontier-level characterization across capacity, domain distance, and capability axes simultaneously — not another PEFT method.
- Minimal Experiment: Fine-tune with a capacity sweep across 3 target domains; evaluate target gain and a retention battery; fit and validate the frontier on a held-out domain.
- Main Risk: Frontier may be recipe-sensitive; replicate under two optimizer settings.
- Research Cluster tag: FT-STAB

### IDEA-A-0222
- Idea: Seed-variance census for segmentation fine-tuning: measure run-to-run variance of standard fine-tuning across seeds and compare it to the effect sizes claimed in recent literature.
- Problem: [KNOWN FACT] Fine-tuning is stochastic; papers rarely report multi-seed variance for dense tasks, so the fraction of published gains within noise is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Multi-seed standard deviation of common fine-tuning setups is comparable to or larger than a substantial fraction of recently claimed improvements in the same settings; small variance relative to claims falsifies it.
- Why Important: Establishes the noise floor against which all fine-tuning claims should be judged — basic metrology the field lacks.
- Why Possibly Novel: A dedicated, well-powered variance study for dense-prediction fine-tuning, published as reference tables.
- Minimal Experiment: Run 20-seed replications of several standard fine-tuning configurations; publish variance tables; compare against a survey of claimed effect sizes.
- Main Risk: Compute cost; use modest model sizes with one large-model spot check.
- Research Cluster tag: FT-STAB

### IDEA-A-0223
- Idea: Test whether loss-landscape flatness at the fine-tuned optimum predicts capability retention: a sharpness-forgetting correlation study across recipes.
- Problem: [KNOWN FACT] Flatness correlates with generalization in some settings; whether it predicts forgetting of pretrained capabilities after fine-tuning is an open, decision-relevant question.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Across fine-tuning runs varying only stochastic factors and mild hyperparameters, flatter optima (by standard sharpness measures) retain significantly more zero-shot capability at matched target performance; no correlation falsifies it.
- Why Important: A validated predictor would enable retention-aware checkpoint selection at zero extra training cost.
- Why Possibly Novel: Connects the flatness literature to the forgetting literature with a controlled correlational design at matched target accuracy.
- Minimal Experiment: Generate many matched-accuracy fine-tuned checkpoints; measure sharpness and retention batteries; report the correlation with controls.
- Main Risk: Sharpness measures disagree with each other; use several and report each.
- Research Cluster tag: FT-STAB

### IDEA-A-0224
- Idea: Task-order asymmetry matrix: measure how the order of sequential fine-tuning over task pairs affects final capabilities, building an empirical interference-asymmetry matrix for dense-prediction tasks.
- Problem: [KNOWN FACT] Sequential fine-tuning order matters anecdotally; systematic pairwise asymmetry data (A-then-B vs B-then-A) for segmentation-relevant tasks does not exist.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Order effects are large and systematically asymmetric, with the asymmetry direction predictable from task-pair properties (label density, domain distance) — enabling order-optimized curricula; symmetric outcomes falsify it.
- Why Important: Organizations fine-tune models repeatedly over time; order guidance would be immediately actionable.
- Why Possibly Novel: A complete asymmetry matrix over a task battery with property-based prediction, not isolated case studies.
- Minimal Experiment: Fine-tune all ordered pairs of a 6-task battery; measure final multi-task profiles; fit asymmetry predictors.
- Main Risk: Combinatorial cost; use a fixed compact recipe and modest scale.
- Research Cluster tag: FT-STAB

### IDEA-A-0225
- Idea: Minimal-rehearsal scaling law: measure how many replayed pretraining examples per fine-tuning step are needed to hold zero-shot capabilities within a target retention band, as a function of domain distance.
- Problem: [KNOWN FACT] Rehearsal mitigates forgetting, but the minimal effective dose for dense-prediction foundation models is unquantified, so practitioners either skip it or over-provision.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Retention follows a smooth saturating function of rehearsal fraction with a surprisingly small dose sufficing (logarithmic-like returns), and the required dose grows with target-domain distance; unpredictable dose-response falsifies it.
- Why Important: A dose table would make retention cheap and routine instead of an afterthought.
- Why Possibly Novel: Rehearsal treated as dosing science with validated dose-response curves for promptable segmentation.
- Minimal Experiment: Fine-tune with a rehearsal-fraction sweep across domains; fit dose-response curves; validate the predicted minimal dose on a new domain.
- Main Risk: Rehearsal data access (pretraining corpora may be unavailable); test proxy-corpus rehearsal as a secondary question.
- Research Cluster tag: FT-STAB

### IDEA-A-0226
- Idea: Capability-forgetting hierarchy: establish the reproducible order in which distinct capabilities (boundary precision, instance separation, prompt-following, rare-class recognition) degrade during aggressive fine-tuning.
- Problem: [KNOWN FACT] Forgetting is measured as aggregate score drop; whether capabilities die in a consistent order — enabling early-warning canaries — is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Capability degradation follows a consistent partial order across domains and recipes (e.g., rare-class recognition first, boundary precision last), so a single cheap canary capability predicts broader damage; inconsistent orders falsify it.
- Why Important: A validated canary lets teams monitor one cheap metric during fine-tuning instead of full evaluation batteries.
- Why Possibly Novel: Forgetting decomposed into a capability partial order with cross-recipe reproducibility testing.
- Minimal Experiment: Fine-tune under graded aggressiveness across domains; evaluate the capability battery at checkpoints; test order consistency and canary validity.
- Main Risk: Capability metrics overlap; design near-orthogonal probes and verify their independence.
- Research Cluster tag: FT-STAB

### IDEA-A-0227
- Idea: Promptability dies first: test whether fine-tuning a promptable model on a fixed-class task destroys interactive prompt-following faster than it improves the target task.
- Problem: [KNOWN FACT] Teams fine-tune promptable models into single-task specialists; the collateral loss of interactivity — arguably the model's defining feature — is not tracked by their target metrics.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Prompt-following capability (response fidelity to varied click/box prompts) degrades earlier and faster than target-task gain accrues, crossing a usability floor while target metrics still improve; retained promptability falsifies it.
- Why Important: If true, the standard specialization workflow silently destroys the most valuable property of these models — teams must be warned with evidence.
- Why Possibly Novel: Tracks interactivity as a first-class casualty of specialization, with a defined usability floor.
- Minimal Experiment: Fine-tune on fixed-class tasks; at each checkpoint measure target metrics and a prompt-following battery; identify the crossing point.
- Main Risk: Prompt-following metrics need care; use the pre-fine-tuning model as its own reference.
- Research Cluster tag: FT-STAB

### IDEA-A-0228
- Idea: Multimask-diversity collapse as a fine-tuning canary: test whether the diversity of a model's multiple mask hypotheses shrinks early during fine-tuning, predicting broader capability loss before standard metrics move.
- Problem: [KNOWN FACT] Ambiguity-aware multimask output reflects distributional knowledge; fine-tuning on single-answer data plausibly collapses it, but nobody monitors this signal.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Multimask diversity declines measurably within early fine-tuning and its decline rate predicts eventual zero-shot capability loss better than target-loss trajectories do; no predictive advantage falsifies it.
- Why Important: An early canary computable from the model's own outputs (no external benchmarks) would enable real-time fine-tuning safety monitoring.
- Why Possibly Novel: Uses an internal distributional property (hypothesis diversity) as a leading indicator of forgetting.
- Minimal Experiment: Log multimask diversity on a probe set during many fine-tuning runs; correlate early diversity slopes with final retention; compare predictive power against loss-based signals.
- Main Risk: Diversity metrics may be noisy; standardize the probe set and diversity measure.
- Research Cluster tag: FT-STAB

### IDEA-A-0229
- Idea: PEFT-versus-full-fine-tuning stability crossover: identify the domain-distance regime where each approach dominates the gain-retention tradeoff, with a computable domain-distance predictor of the crossover.
- Problem: [KNOWN FACT] PEFT is assumed safer (less forgetting) but weaker on distant domains; the crossover point is undocumented, so the choice is made by fashion.
- Core Hypothesis (falsifiable): [HYPOTHESIS] There exists a measurable domain-distance threshold below which PEFT dominates the frontier and above which full fine-tuning does, and the threshold is predictable from unlabeled target statistics; no consistent crossover falsifies it.
- Why Important: Converts the most common adaptation decision into a measurement-driven rule.
- Why Possibly Novel: Head-to-head frontier comparison indexed by domain distance with a validated decision rule, rather than single-benchmark comparisons.
- Minimal Experiment: Run both approaches across a domain-distance-ordered target series; map frontiers; locate crossovers; validate the predictor on new targets.
- Main Risk: Distance measures imperfect; use several and report agreement.
- Research Cluster tag: FT-STAB

### IDEA-A-0230
- Idea: Learning-rate primacy test: measure whether learning rate alone explains more variance in forgetting outcomes than the choice among popular fine-tuning methods, at matched target accuracy.
- Problem: [KNOWN FACT] Method papers compare forgetting under their own tuned settings; the community suspects but has not quantified that basic optimization scale dominates method identity.
- Core Hypothesis (falsifiable): [HYPOTHESIS] In a factorial design (methods × learning rates), learning rate explains substantially more forgetting variance than method identity, and method rankings invert across learning rates; method-dominant variance falsifies it.
- Why Important: If the hypothesis holds, much of the continual-learning method literature is comparing learning-rate artifacts — a correction with large field-level consequences.
- Why Possibly Novel: A designed variance-decomposition experiment targeted at the method-vs-hyperparameter attribution question for dense tasks.
- Minimal Experiment: Factorial fine-tuning study over methods and learning-rate grids at matched target accuracy; ANOVA-style variance attribution on retention outcomes.
- Main Risk: Matched-accuracy stopping introduces its own choices; pre-register the stopping protocol.
- Research Cluster tag: FT-STAB

### IDEA-A-0231
- Idea: Label-free early stopping for fine-tuning: validate stopping criteria computable without target-domain validation labels (prediction-consistency plateaus, output-distribution drift) against oracle stopping points.
- Problem: [KNOWN FACT] Small target domains often lack enough labels for a proper validation split; practitioners guess stopping points, risking both underfitting and forgetting.
- Core Hypothesis (falsifiable): [HYPOTHESIS] At least one label-free criterion stops within a small margin of the oracle (labeled-validation) stopping point across domains and recipes; all criteria failing falsifies the practical premise.
- Why Important: Would remove a chronic pain point for low-resource fine-tuning with a directly usable recipe component.
- Why Possibly Novel: Head-to-head validation of label-free stopping rules specifically for dense-prediction fine-tuning, with oracle-gap reporting.
- Minimal Experiment: Fine-tune across domains while logging candidate label-free signals; compare each criterion's stopping point and outcome to the oracle; rank criteria.
- Main Risk: Criteria may be recipe-specific; test across two recipes and report interaction.
- Research Cluster tag: FT-STAB

### IDEA-A-0232
- Idea: Predict fine-tuned model-merging failure from weight-space geometry: test whether the angle/overlap structure between task-specific weight deltas predicts when averaging fine-tuned variants degrades performance.
- Problem: [KNOWN FACT] Averaging fine-tuned models sometimes works remarkably and sometimes fails; a validated pre-merge compatibility test is missing.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Merge outcome is predictable from cheap weight-space statistics of the deltas (interference measures), with high accuracy across task pairs and scales; unpredictable outcomes falsify it.
- Why Important: Merging is free capability composition when it works; a reliable compatibility test would make it an engineering tool rather than a gamble.
- Why Possibly Novel: Focuses on validated prediction of merge failure for dense-prediction models, with released compatibility diagnostics.
- Minimal Experiment: Create a library of fine-tuned variants; merge all pairs; regress outcomes on weight-space statistics; validate on held-out pairs.
- Main Risk: Predictors may not transfer across architectures; test on two model families.
- Research Cluster tag: FT-STAB

### IDEA-A-0233
- Idea: Task-arithmetic failure conditions for dense prediction: characterize when adding/subtracting task vectors produces the intended capability edits in segmentation models, and when it corrupts unrelated capabilities.
- Problem: [KNOWN FACT] Task-vector arithmetic shows promise in classification settings; its reliability envelope for dense, promptable models is unmapped.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Arithmetic succeeds only when task deltas occupy weakly overlapping parameter subspaces (measurable beforehand), and collateral damage to unrelated capabilities is predictable from overlap statistics; unpredictable success falsifies it.
- Why Important: Reliable capability editing would let teams maintain model families compositionally instead of retraining — but only within a known safety envelope.
- Why Possibly Novel: An envelope-mapping study (when it works) with collateral-damage accounting for dense tasks, rather than a demonstration paper.
- Minimal Experiment: Build task vectors over a task battery; apply arithmetic combinations; measure intended and collateral effects; fit the overlap-based predictor.
- Main Risk: Negative results likely for distant tasks; that is itself the envelope — report it.
- Research Cluster tag: FT-STAB

### IDEA-A-0234
- Idea: Localize forgetting in parameter space: use layer-wise probing and selective restoration to identify which layers' changes carry the forgetting after dense-task fine-tuning.
- Problem: [KNOWN FACT] Forgetting is measured behaviorally; where in the network the old capability was overwritten (versus merely masked) is unresolved and matters for cheap restoration.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Restoring a small subset of layers to pretrained values recovers most zero-shot capability while retaining most target gains, implying forgetting is localized and largely masking-like; distributed irrecoverable forgetting falsifies it.
- Why Important: If forgetting is localized masking, trivial post-hoc restoration recipes could give practitioners retention nearly for free.
- Why Possibly Novel: Selective-restoration causal methodology applied systematically to promptable segmentation fine-tuning.
- Minimal Experiment: After fine-tuning, restore each layer (and small groups) to pretrained weights; measure capability recovery vs target loss; map the localization.
- Main Risk: Combinatorial restoration space; use greedy and random-subset baselines.
- Research Cluster tag: FT-STAB

### IDEA-A-0235
- Idea: Memorization onset in low-data fine-tuning: identify the training-set size below which dense-prediction fine-tuning transitions from generalization to mask memorization, with a label-free onset detector.
- Problem: [KNOWN FACT] Small medical/industrial fine-tuning sets are common; the memorization-generalization transition for mask outputs (not classification) lacks measurement tools.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Below a data-size threshold (scaled by model capacity), models reproduce training-mask idiosyncrasies (annotator-specific boundary styles) detectable by style-similarity statistics without test labels, and the detector flags the onset reliably; no detectable transition falsifies it.
- Why Important: A memorization alarm for low-data regimes would prevent shipping models that only replay their training masks.
- Why Possibly Novel: Mask-style similarity as a memorization signature — exploiting the structured-output nature of segmentation.
- Minimal Experiment: Fine-tune across training-size sweeps; measure train-style reproduction vs held-out generalization; validate the label-free onset detector.
- Main Risk: Style statistics may confound with correct behavior; use multi-annotator data to separate style from content.
- Research Cluster tag: FT-STAB

### IDEA-A-0236
- Idea: Noise-amplification comparison: test whether fine-tuning a foundation model on noisy labels amplifies the noise more or less than training a specialist from scratch on the same data.
- Problem: [KNOWN FACT] Practitioners assume pretrained initialization helps with noisy labels, but a strong prior could also make the model fit systematic annotation errors more confidently; the direction is untested for dense tasks.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Fine-tuned foundation models resist random label noise better but absorb systematic annotation biases (consistent boundary offsets) more thoroughly than scratch models, measurable on clean test sets; uniform behavior falsifies the dissociation.
- Why Important: The random-vs-systematic dissociation, if real, changes QA priorities: fixing systematic bias matters more when fine-tuning foundations.
- Why Possibly Novel: Distinguishes noise types in the amplification question, tied to the structured nature of segmentation errors.
- Minimal Experiment: Inject random and systematic label corruptions separately; fine-tune vs train-from-scratch; measure clean-test inheritance of each corruption type.
- Main Risk: Scratch baselines need fair budgets; match compute and tune both fairly.
- Research Cluster tag: FT-STAB

### IDEA-A-0237
- Idea: Calibration forgetting: measure how fine-tuning degrades the uncertainty calibration of segmentation models even when accuracy improves, and whether calibration and accuracy forget on different schedules.
- Problem: [KNOWN FACT] Fine-tuning studies track accuracy metrics; calibration of dense outputs is safety-relevant and plausibly degrades independently, but the joint dynamics are unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Calibration deteriorates earlier and faster than accuracy improves during standard fine-tuning (a calibration-accuracy scissors), and brief post-hoc recalibration recovers most of it; parallel dynamics falsify it.
- Why Important: Deployments consuming confidence values can be silently broken by an accuracy-improving fine-tune — teams need the scissors documented.
- Why Possibly Novel: Trajectory-level joint dynamics of calibration and accuracy during fine-tuning for dense prediction.
- Minimal Experiment: Log calibration and accuracy metrics at fine-tuning checkpoints across recipes; characterize the scissors; test post-hoc recalibration recovery.
- Main Risk: Dense-output calibration metrics have choices; report several standard ones.
- Research Cluster tag: FT-STAB

### IDEA-A-0238
- Idea: The robustness tax of fine-tuning: quantify how much out-of-distribution robustness a segmentation foundation model loses per unit of in-domain gain during fine-tuning, across recipes and domains.
- Problem: [KNOWN FACT] Fine-tuning can reduce effective robustness in classification settings; the exchange rate for dense prediction — and whether any recipe reduces the tax — is unquantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Robustness loss per in-domain gain (the tax rate) is roughly constant within a recipe family but differs across families, enabling tax-aware recipe selection; unstable or zero tax falsifies it.
- Why Important: Teams unknowingly trade deployment robustness for benchmark gains; a published tax table would make the trade explicit.
- Why Possibly Novel: Exchange-rate framing with systematic cross-recipe measurement for segmentation.
- Minimal Experiment: Fine-tune across recipes/domains; measure in-domain gains and OOD-battery losses; estimate and compare tax rates.
- Main Risk: OOD battery composition drives results; use a broad, documented battery.
- Research Cluster tag: FT-STAB

### IDEA-A-0239
- Idea: Normalization-statistics forgetting: measure what fraction of apparent catastrophic forgetting is recoverable by restoring only normalization-layer statistics/parameters to their pretrained state.
- Problem: [KNOWN FACT] Normalization layers absorb domain statistics during fine-tuning; their contribution to measured forgetting (versus deeper weight changes) is unquantified for dense models.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A substantial fraction of zero-shot performance loss is recovered by restoring normalization parameters alone, implying much "forgetting" is statistical recalibration rather than knowledge overwrite; negligible recovery falsifies it.
- Why Important: If normalization dominates, dual-statistics deployment (per-domain norm sets) trivially serves both domains — a huge practical shortcut.
- Why Possibly Novel: A precise attribution experiment separating statistical recalibration from knowledge loss in the forgetting measurement.
- Minimal Experiment: After fine-tuning, swap normalization parameters between pretrained and fine-tuned checkpoints in both directions; measure capability recovery on both domains.
- Main Risk: Architectures vary in normalization design; run across several normalization schemes.
- Research Cluster tag: FT-STAB

### IDEA-A-0240
- Idea: Catastrophic remembering: measure whether strongly regularized continual-learning setups become unable to adapt (over-stability), and map the stability-plasticity operating curve for dense-task sequences.
- Problem: [KNOWN FACT] Anti-forgetting mechanisms bias toward stability; the symmetric failure — inability to learn new tasks — is rarely measured with equal care for segmentation task sequences.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Popular anti-forgetting configurations, tuned to protect old tasks, measurably cap new-task learning (an adaptation ceiling), and the ceiling tightens with sequence length — an accumulating rigidity effect; no ceiling falsifies it.
- Why Important: A model that cannot learn task N+1 is as broken as one that forgets task 1; the field needs both failure modes on the same dashboard.
- Why Possibly Novel: Accumulating-rigidity measurement over long task sequences with an explicit operating-curve deliverable.
- Minimal Experiment: Run continual methods over long dense-task sequences; track per-task adaptation speed/ceiling vs sequence position; map operating curves per method.
- Main Risk: Long sequences are compute-heavy; use compact tasks with verified difficulty matching.
- Research Cluster tag: FT-STAB

### IDEA-A-0241
- Idea: Early-warning gradient-conflict signal: test whether the measurable conflict between target-task gradients and pretraining-proxy gradients in early fine-tuning predicts final forgetting magnitude.
- Problem: [KNOWN FACT] Forgetting is discovered after training completes; a predictive signal available in the first few steps would enable cheap course correction, but none is validated for dense models.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Early-step gradient-conflict statistics (against a small pretraining-proxy batch) correlate strongly with end-of-training retention across domains and recipes, enabling forgetting forecasts before compute is spent; weak correlation falsifies it.
- Why Important: Turning forgetting from a post-mortem into a forecast changes fine-tuning workflow economics.
- Why Possibly Novel: Validated forecasting (with lead-time and accuracy numbers) rather than another regularization method built on conflict intuition.
- Minimal Experiment: Log early gradient-conflict statistics across many fine-tuning runs; regress final retention on them; evaluate forecast accuracy on held-out runs.
- Main Risk: Proxy-batch choice matters; test sensitivity to proxy composition.
- Research Cluster tag: FT-STAB

### IDEA-A-0242
- Idea: Frequency-ordered forgetting: test whether classes/concepts are forgotten in inverse order of their pretraining frequency, making long-tail knowledge the first casualty of any fine-tune.
- Problem: [KNOWN FACT] Pretraining exposure varies enormously across concepts; whether forgetting is frequency-ordered — concentrating damage on already-disadvantaged rare concepts — is untested for dense models.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Retention after fine-tuning correlates strongly with estimated pretraining frequency, so rare-concept capability degrades first and disproportionately; frequency-independent forgetting falsifies it.
- Why Important: Frequency-ordered forgetting would mean every fine-tune silently worsens long-tail equity — a compounding harm needing measurement.
- Why Possibly Novel: Links forgetting dynamics to pretraining exposure statistics at the concept level for segmentation.
- Minimal Experiment: Estimate concept frequencies from public pretraining-corpus statistics; measure per-concept retention after standard fine-tunes; test the correlation.
- Main Risk: Frequency estimates are approximate; use multiple estimation sources and rank-based statistics.
- Research Cluster tag: FT-STAB

### IDEA-A-0243
- Idea: Capacity-distance matching law: test whether the optimal PEFT capacity scales predictably with measured target-domain distance, enabling capacity selection from unlabeled target data alone.
- Problem: [KNOWN FACT] PEFT capacity is tuned by search per project; a transferable law linking required capacity to domain distance would eliminate that search, but none is established.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Across targets, optimal capacity grows monotonically and predictably with unlabeled-domain-distance measures, and the fitted law selects near-optimal capacity for unseen targets; no stable relationship falsifies it.
- Why Important: Replaces a costly hyperparameter search with a measurement — practical value for every PEFT user.
- Why Possibly Novel: Aims at a quantitative transferable law with held-out-target validation, not a per-benchmark tuning report.
- Minimal Experiment: Sweep capacity across a distance-ordered target series; fit the capacity-distance law; validate selection quality on held-out targets.
- Main Risk: Confounded by target dataset size; include size as a covariate in the law.
- Research Cluster tag: FT-STAB

### IDEA-A-0244
- Idea: Self-training drift dynamics: measure how iterative pseudo-label fine-tuning drifts over rounds (confirmation bias accumulation) and derive a validated stopping rule from label-free drift signals.
- Problem: [KNOWN FACT] Iterated self-training amplifies its own errors; practitioners stop after an arbitrary round count because drift is not measured online.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Drift follows a characteristic trajectory (initial gain, plateau, degradation) whose turning point is detectable from label-free signals (pseudo-label entropy distribution, agreement decay) with enough lead time to stop optimally; undetectable turning points falsify it.
- Why Important: A stopping rule would make self-training safe to automate at scale — currently it requires labeled monitoring or luck.
- Why Possibly Novel: Treats self-training as a dynamical process with validated online instrumentation, for dense prediction.
- Minimal Experiment: Run many-round self-training across domains with held-out truth; log candidate signals; validate turning-point detection lead time and stopping quality.
- Main Risk: Trajectories may differ qualitatively by domain; report per-domain dynamics before pooling.
- Research Cluster tag: FT-STAB

### IDEA-A-0245
- Idea: Transitive fine-tuning degradation: measure how model quality and stability change over chains of successive fine-tunes (A→B→C…) compared to always restarting from the original foundation checkpoint.
- Problem: [KNOWN FACT] Organizations iterate on already-fine-tuned checkpoints for convenience; whether chained fine-tuning accumulates hidden damage versus foundation restarts is unquantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Chained fine-tuning accumulates measurable degradation (retention, calibration, robustness) relative to matched foundation restarts, with damage growing in chain length — an argument for checkpoint hygiene; no accumulation falsifies it.
- Why Important: Checkpoint-lineage policy is an unexamined operational decision made daily in industry; evidence would set best practice.
- Why Possibly Novel: Lineage-level experimental design (chains vs restarts at matched budgets) with multi-dimensional damage accounting.
- Minimal Experiment: Build fine-tuning chains of increasing length vs restart controls across task sequences; compare final multi-dimensional profiles.
- Main Risk: Chain outcomes depend on task order (cf. IDEA-A-0224); randomize orders and analyze jointly.
- Research Cluster tag: FT-STAB

### IDEA-A-0246
- Idea: Stability of "important-parameter" selections: measure whether the parameter subsets chosen by sparse fine-tuning criteria are stable across seeds and data resamples, or essentially arbitrary.
- Problem: [KNOWN FACT] Sparse fine-tuning methods select "important" parameters via saliency-like criteria; if selections are unstable, the importance narrative is questionable and reproducibility suffers.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Parameter-selection overlap across seeds/resamples is barely above chance while performance stays constant, implying importance is massively non-unique (many equivalent subsets); high overlap falsifies it.
- Why Important: Non-uniqueness would redirect the field from "finding the important parameters" to characterizing the equivalence class — a conceptual correction.
- Why Possibly Novel: Applies selection-stability methodology (from feature-selection statistics) to parameter-level fine-tuning choices.
- Minimal Experiment: Repeat sparse-selection fine-tuning across seeds/resamples; measure subset overlap and outcome variance; compare against random-subset controls at matched sparsity.
- Main Risk: Overlap metrics need care at scale; use hierarchical (layer-level and parameter-level) overlap analysis.
- Research Cluster tag: FT-STAB

### IDEA-A-0247
- Idea: Hyperparameter transfer across scale for fine-tuning: test whether optimal fine-tuning hyperparameters found on small models transfer predictably to larger models of the same family for dense tasks.
- Problem: [KNOWN FACT] Hyperparameter search on large models is prohibitively expensive; principled small-to-large transfer rules exist for pretraining in some settings but are unvalidated for dense-task fine-tuning.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Optimal fine-tuning hyperparameters follow smooth, predictable scaling trends within a model family, so small-scale search plus extrapolation lands within a small margin of large-scale optima; erratic trends falsify it.
- Why Important: Validated transfer rules would cut fine-tuning search costs by orders of magnitude for everyone using large dense-prediction models.
- Why Possibly Novel: Systematic scale-transfer validation specifically for fine-tuning (not pretraining) with dense-task endpoints.
- Minimal Experiment: Grid-search fine-tuning hyperparameters at 3-4 scales in one family; fit scaling trends; test extrapolation accuracy at the largest scale.
- Main Risk: Family-specific conclusions; replicate on a second family before claiming generality.
- Research Cluster tag: FT-STAB

### IDEA-A-0248
- Idea: Contamination audit of forgetting measurements: test whether pretraining-corpus overlap with forgetting-evaluation benchmarks systematically distorts measured retention (models "remember" test items, not capabilities).
- Problem: [KNOWN FACT] Foundation models may have seen benchmark images during pretraining; forgetting studies using those benchmarks may measure memorized-item retention rather than capability retention.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Retention measured on suspected-contaminated benchmark subsets differs systematically from retention on verified-clean subsets, meaning contamination inflates or distorts forgetting conclusions; identical retention falsifies it.
- Why Important: If contaminated, a slice of the continual-learning literature's measurements needs reinterpretation — a foundational metrology issue.
- Why Possibly Novel: Connects the contamination literature to the forgetting literature, which have so far ignored each other.
- Minimal Experiment: Partition forgetting benchmarks by contamination likelihood (similarity search against known corpora); compare retention statistics across partitions after standard fine-tunes.
- Main Risk: Contamination detection is imperfect; use conservative partitions and sensitivity analysis.
- Research Cluster tag: FT-STAB

### IDEA-A-0249
- Idea: Self-replay feasibility limits: test whether a segmentation model can generate its own rehearsal data (self-produced pseudo-examples of prior capabilities) well enough to prevent forgetting without access to original pretraining data.
- Problem: [KNOWN FACT] Original pretraining corpora are often unavailable for rehearsal (licensing, scale); whether self-generated surrogates preserve dense-prediction capabilities is unresolved.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Self-replay retains a substantial but capability-uneven fraction of zero-shot performance (structure-heavy capabilities like boundary precision survive worst), mapping which capabilities can and cannot be self-preserved; uniform or negligible retention falsifies the map.
- Why Important: A capability-resolved feasibility answer determines whether data-free retention is a real option for practitioners with restricted corpora.
- Why Possibly Novel: Capability-resolved analysis of self-replay for dense prediction, framed as feasibility limits rather than a method victory.
- Minimal Experiment: Construct self-replay pipelines (model-selected/model-labeled surrogate images); fine-tune with and without; measure the capability-resolved retention delta.
- Main Risk: Surrogate construction choices dominate; compare several surrogate sources under one protocol.
- Research Cluster tag: FT-STAB

### IDEA-A-0250
- Idea: Quantization-fine-tuning interaction: measure whether fine-tuning quantized models changes the forgetting profile relative to fine-tuning at full precision followed by quantization.
- Problem: [KNOWN FACT] Efficiency pipelines combine quantization and fine-tuning in different orders; the interaction's effect on capability retention is unquantified for dense models.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Order matters systematically: fine-tuning under quantization constraints produces different (and capability-uneven) retention than post-hoc quantization, with the difference concentrated in boundary-precision capabilities; order-invariance falsifies it.
- Why Important: Edge deployments must pick an order today; evidence-based ordering guidance would prevent silent capability loss on-device.
- Why Possibly Novel: Joint treatment of two pipeline stages usually studied separately, with capability-resolved outcomes.
- Minimal Experiment: Run both orderings across bit-widths and domains; compare capability-resolved retention profiles.
- Main Risk: Many quantization schemes; fix two widely used schemes and state scope.
- Research Cluster tag: FT-STAB

### IDEA-A-0251
- Idea: Metric-resolved forgetting curves: test whether boundary-quality capability forgets on a different schedule than region-overlap capability during fine-tuning, so single-metric monitoring misses early damage.
- Problem: [KNOWN FACT] Forgetting is monitored with one metric (usually region overlap); dense-prediction quality is multi-dimensional and the dimensions may decay at different rates.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Boundary metrics on retained capabilities decay earlier and faster than region metrics during fine-tuning (fine detail is overwritten first), so region-metric monitoring systematically underestimates early forgetting; synchronized decay falsifies it.
- Why Important: Determines what teams must monitor to catch forgetting early — a small change with large practical protection.
- Why Possibly Novel: Decay-schedule comparison across quality dimensions, not just endpoints.
- Minimal Experiment: Log region and boundary metrics on retention probes at dense checkpoint intervals across fine-tuning runs; compare decay onset and rates.
- Main Risk: Boundary metrics are noisier; use large probe sets for stable curves.
- Research Cluster tag: FT-STAB

### IDEA-A-0252
- Idea: Causal decomposition of two-stage schedules: measure which mechanism makes probe-then-tune schedules (head-first training before unfreezing) affect retention — feature preservation, optimization trajectory, or effective learning-rate scheduling.
- Problem: [KNOWN FACT] Two-stage fine-tuning schedules are popular folklore for stability; the causal mechanism behind their effect on forgetting is untested, so the practice cannot be rationally improved.
- Core Hypothesis (falsifiable): [HYPOTHESIS] The retention benefit of two-stage schedules is explained almost entirely by the implied effective learning-rate profile on backbone parameters (replicable by rate scheduling alone, without stages); irreducibility to rate scheduling falsifies it.
- Why Important: If it is just rate scheduling, simpler recipes achieve the same protection; if not, stages contain real mechanism worth understanding.
- Why Possibly Novel: Mechanism-isolation experimental design for a widely used but untheorized practice.
- Minimal Experiment: Compare two-stage schedules against matched single-stage runs whose per-parameter learning-rate profiles replicate the staged effective rates; measure retention differences.
- Main Risk: Matching effective rates precisely is subtle; verify with optimizer-state instrumentation.
- Research Cluster tag: FT-STAB

### IDEA-A-0253
- Idea: Data-order instability: measure how much fine-tuning outcome variance is attributable to training-data ordering alone, and whether order-sensitivity itself predicts fragile (poorly retaining) runs.
- Problem: [KNOWN FACT] Data order is randomized and forgotten; for small fine-tuning sets, order could be a dominant variance source with diagnostic value, but nobody measures it.
- Core Hypothesis (falsifiable): [HYPOTHESIS] In low-data fine-tuning, data-order variance rivals initialization-seed variance, and runs exhibiting high early order-sensitivity (measurable by short probe runs) end with worse retention — a cheap fragility diagnostic; negligible order effects falsify it.
- Why Important: A five-minute fragility probe before committing to a full fine-tune would be a free risk-reduction tool.
- Why Possibly Novel: Data-order as a first-class variance component and early diagnostic, distinct from seed studies.
- Minimal Experiment: Fix seeds, permute data order across runs; decompose outcome variance; test early-sensitivity probes as fragility predictors.
- Main Risk: Interaction with batch size; run at two batch sizes.
- Research Cluster tag: FT-STAB

### IDEA-A-0254
- Idea: Tuning-locus effects in video segmentation models: compare the temporal-capability retention profile when fine-tuning targets different parameter loci (image pathway vs memory/propagation pathway) of SAM2-style models.
- Problem: [KNOWN FACT] Video models contain distinct functional pathways; which locus a fine-tune touches determines what breaks, but locus-resolved retention data does not exist.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Fine-tuning the image pathway on static data degrades temporal propagation capabilities disproportionately (cross-pathway collateral damage), while memory-pathway tuning leaves static capabilities largely intact — an asymmetric damage matrix; symmetric damage falsifies it.
- Why Important: Teams adapt video models with static-image data constantly; an asymmetric damage result would immediately change what they train.
- Why Possibly Novel: Pathway-resolved forgetting analysis exploiting the functional modularity of video segmentation architectures (as measurement, not architecture modification).
- Minimal Experiment: Fine-tune each locus separately on matched data; evaluate static and temporal capability batteries; report the damage matrix.
- Main Risk: Loci are not perfectly separable; define parameter groups explicitly and release the grouping.
- Research Cluster tag: FT-STAB

### IDEA-A-0255
- Idea: Forgetting-metric disagreement: measure how differently the common forgetting metrics rank the same set of fine-tuned checkpoints, and whether any metric predicts practical downstream regret.
- Problem: [KNOWN FACT] Multiple forgetting metrics coexist (average accuracy deltas, backward transfer, retention ratios); if they disagree on rankings, method conclusions depend on an arbitrary metric choice.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Metric disagreement on checkpoint rankings is substantial, and only some metrics correlate with practical regret (performance when the old task unexpectedly returns in deployment scenarios); high metric concordance falsifies it.
- Why Important: Anchors the forgetting-measurement debate to a deployment-meaningful criterion instead of convention.
- Why Possibly Novel: Meta-evaluation of forgetting metrics against an operationalized regret criterion.
- Minimal Experiment: Generate a diverse checkpoint zoo; rank by each metric; simulate task-return scenarios to measure regret; correlate metric rankings with regret rankings.
- Main Risk: Regret operationalization choices; use several scenario families and report robustness.
- Research Cluster tag: FT-STAB

### IDEA-A-0256
- Idea: Weight-displacement universality: test whether total weight-space displacement during fine-tuning predicts forgetting universally across methods, making it a recipe-agnostic retention gauge.
- Problem: [KNOWN FACT] Many anti-forgetting methods implicitly limit weight change; whether displacement is the common currency explaining retention across all of them is an open unification question.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Across diverse recipes at matched target accuracy, retention collapses onto a single function of (suitably normalized, layer-weighted) weight displacement — a universal curve; recipe-specific curves falsify universality.
- Why Important: A universal gauge would reduce retention monitoring to reading one number during training, regardless of method.
- Why Possibly Novel: A deliberate universality test (curve-collapse methodology) over heterogeneous fine-tuning approaches.
- Minimal Experiment: Collect displacement and retention measurements across many recipes/domains at matched accuracy; test collapse under candidate normalizations.
- Main Risk: Normalization choice can manufacture collapse; preregister normalizations and show alternatives.
- Research Cluster tag: FT-STAB

### IDEA-A-0257
- Idea: Vocabulary-retention curves: measure how the effective open-vocabulary breadth of a text-promptable segmenter shrinks during narrow-class fine-tuning, and whether breadth loss precedes in-domain gains.
- Problem: [KNOWN FACT] Open-vocabulary capability is the headline value of text-promptable models; narrow fine-tunes plausibly shrink usable vocabulary, but breadth is never measured as a curve during training.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Effective vocabulary (concepts still segmentable above a quality bar) contracts monotonically during narrow fine-tuning, with contraction rate exceeding target-gain rate early — most vocabulary is spent before most gain arrives; late or minor contraction falsifies it.
- Why Important: Quantifies the real price of specializing open-vocabulary models — currently invisible in target-task dashboards.
- Why Possibly Novel: Vocabulary breadth as a longitudinal training-time observable with an explicit exchange-rate analysis.
- Minimal Experiment: Probe a broad concept battery at fine-tuning checkpoints; plot vocabulary-retention curves against target-gain curves across recipes.
- Main Risk: Probing cost per checkpoint; subsample the battery with stratified coverage.
- Research Cluster tag: FT-STAB

### IDEA-A-0258
- Idea: Positive backward transfer census: identify and characterize the conditions under which fine-tuning on a new task improves previously learned capabilities, rather than degrading them.
- Problem: [KNOWN FACT] The forgetting literature focuses on damage; documented cases of fine-tuning improving old capabilities exist anecdotally but the enabling conditions are uncharacterized for dense tasks.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Positive backward transfer occurs reproducibly when the new task supervises a quality dimension underrepresented in pretraining (e.g., precise boundaries), and the effect is predictable from a task-property checklist; irreproducible or unpredictable occurrences falsify it.
- Why Important: If backward transfer is engineerable, fine-tuning sequences could be designed to strengthen rather than erode foundations.
- Why Possibly Novel: Systematically hunting the positive regime, inverting the field's damage-centric framing.
- Minimal Experiment: Screen a task battery for backward-transfer sign on retained capabilities; characterize positive cases; validate the predictive checklist on new tasks.
- Main Risk: Positive cases may be rare; even a well-documented rarity result reshapes expectations.
- Research Cluster tag: FT-STAB

### IDEA-A-0259
- Idea: Stochastic-regularization effects on retention: measure whether training-time stochasticity (dropout-like noise, data augmentation strength) during fine-tuning systematically modulates forgetting, independent of final target accuracy.
- Problem: [KNOWN FACT] Stochastic regularizers are set for target-task performance; their side effects on capability retention are unmeasured, though plausible through flatness and exploration effects.
- Core Hypothesis (falsifiable): [HYPOTHESIS] At matched target accuracy, higher training stochasticity yields measurably better retention (a stochasticity-retention dividend) up to a level where target learning degrades; no retention effect falsifies it.
- Why Important: If the dividend exists, retention improves via knobs every practitioner already has — no new machinery.
- Why Possibly Novel: Retention treated as the primary outcome of regularization settings, decoupled from target accuracy by matched-accuracy design.
- Minimal Experiment: Fine-tune across stochasticity grids to matched target accuracy; measure retention batteries; map the dividend curve.
- Main Risk: Matched-accuracy stopping interacts with stochasticity; pre-register the protocol (cf. IDEA-A-0230).
- Research Cluster tag: FT-STAB

### IDEA-A-0260
- Idea: Deployable fine-tuning insurance: build and validate a cheap post-fine-tuning acceptance test (small probe battery plus thresholds) that flags checkpoints whose capability damage exceeds policy, calibrated against full evaluation.
- Problem: [KNOWN FACT] Teams ship fine-tuned checkpoints after target-metric checks only; full capability audits are too expensive per iteration, so damaged checkpoints ship undetected.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A probe battery under a strict compute budget (minutes, not hours) can predict full-audit outcomes with high agreement, enabling reliable accept/reject decisions; low agreement at any small budget falsifies practical insurability.
- Why Important: The last-mile safety artifact for all preceding forgetting science — the piece that changes daily practice.
- Why Possibly Novel: Optimized probe selection with quantified agreement guarantees, treated as an acceptance-testing engineering problem.
- Minimal Experiment: Assemble a checkpoint zoo with full audits; search probe subsets maximizing decision agreement per compute budget; validate on held-out checkpoints.
- Main Risk: Probe overfitting to the zoo; enforce checkpoint-family holdouts in validation.
- Research Cluster tag: FT-STAB

---

## Section 8 — Dataset failure (IDEA-A-0261 .. 0295)

### IDEA-A-0261
- Idea: Cross-benchmark near-duplicate contamination map: measure train/test near-duplicate rates within and across popular segmentation datasets and quantify the score inflation they cause.
- Problem: [KNOWN FACT] Web-derived datasets contain near-duplicates; segmentation-specific contamination rates and their inflation effects are less documented than for classification.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Measurable near-duplicate contamination exists across popular segmentation benchmarks, and model scores on duplicate-linked test items are systematically inflated relative to clean items; no score differential falsifies it.
- Why Important: Contamination-adjusted scores may reorder methods and deflate perceived progress — the field should know by how much.
- Why Possibly Novel: A segmentation-specific, cross-dataset contamination atlas with inflation effect sizes, released as cleaning lists.
- Minimal Experiment: Run embedding-based duplicate detection within/across 6 benchmarks; verify samples manually; compare model scores on flagged vs clean partitions.
- Main Risk: Detector threshold sensitivity; publish results across thresholds with manual verification rates.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0262
- Idea: Disagreement-guided label-error estimation: use model-committee disagreement to steer targeted re-annotation and produce statistically grounded label-error rates for segmentation benchmarks.
- Problem: [KNOWN FACT] Label errors exist in all benchmarks, but segmentation error rates are rarely estimated with statistical rigor because exhaustive re-annotation is unaffordable.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Committee disagreement concentrates true label errors strongly enough that stratified re-annotation yields tight error-rate estimates at a small fraction of exhaustive cost, and estimated rates are large enough to matter for near-SOTA comparisons; diffuse errors falsify the efficiency claim.
- Why Important: Every benchmark consumer needs the error bar that label noise puts under reported scores.
- Why Possibly Novel: Statistically principled (stratified estimation with verification) label-error auditing for dense annotations, not just anecdote lists.
- Minimal Experiment: Stratify test items by committee disagreement; re-annotate samples per stratum; compute weighted error-rate estimates with confidence intervals.
- Main Risk: Committee shares blind spots; include a random stratum to bound unseen-error mass.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0263
- Idea: Annotation-instruction drift detection: test whether label statistics within long-running datasets shift over collection time (guideline evolution, annotator turnover), creating internal inconsistency.
- Problem: [KNOWN FACT] Large datasets are annotated over months/years with evolving teams; internal drift is plausible but rarely audited, and models may learn time-dependent conventions.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Datasets with documented long collection periods show statistically detectable temporal drift in label properties (boundary style, class usage), and models can predict an image's annotation period from its labels alone — proving learnable inconsistency; undetectable drift falsifies it.
- Why Important: Internal inconsistency puts a floor under achievable performance and injects convention noise into every trained model.
- Why Possibly Novel: Annotation-period prediction as a drift-detection instrument — using learnability as the evidence standard.
- Minimal Experiment: Obtain collection-order metadata for 2-3 datasets; train period predictors from labels; quantify drift dimensions and their performance floor implications.
- Main Risk: Metadata availability; where absent, use dataset version diffs as coarse temporal signal.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0264
- Idea: Cross-dataset class-definition inconsistency census: systematically measure how the same class name maps to different pixel-level realities across datasets, producing a compatibility matrix for dataset combination.
- Problem: [KNOWN FACT] Practitioners merge datasets by matching class names; the underlying definitions differ in unquantified ways that corrupt combined training (cf. IDEA-A-0176's convention distance).
- Core Hypothesis (falsifiable): [HYPOTHESIS] For a substantial fraction of shared class names, cross-dataset definition differences are large enough that a model can classify which dataset a mask came from at high accuracy — operationalizing incompatibility; near-chance dataset classification falsifies it.
- Why Important: A public compatibility matrix would prevent silent definition clashes in the most common data-scaling move.
- Why Possibly Novel: Learnability-based incompatibility measurement (dataset-of-origin prediction from masks) as a scalable audit tool.
- Minimal Experiment: For shared classes across 5 datasets, train origin classifiers from mask/label properties; report per-class separability as the incompatibility score.
- Main Risk: Image-distribution differences confound; use mask-geometry features only, excluding appearance.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0265
- Idea: Dataset aging measurement: quantify how the visual distribution of dataset categories drifts from the current world (object designs, environments) and how much of modern-model error on old benchmarks reflects the world moving on.
- Problem: [KNOWN FACT] Canonical benchmarks freeze a historical visual world; their continued use assumes category appearance is stable, which is false for many man-made classes.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For fast-evolving categories, benchmark images are measurably unrepresentative of contemporary instances, and models trained on contemporary data score worse on the old benchmark despite being better on current imagery — an aging-inversion effect; no inversion falsifies it.
- Why Important: Aging inversions would mean leaderboard decline can indicate improvement — a paradox the community must account for.
- Why Possibly Novel: Treats benchmark age as a measurable validity variable with inversion tests, not a nostalgia complaint.
- Minimal Experiment: Assemble contemporary counterparts for aged categories; train matched models on old vs new data; test for inversion across both test sets.
- Main Risk: Contemporary data collection effort; scope to 10 fast-evolving categories.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0266
- Idea: Photographer-framing bias exploitation: measure how much segmentation/detection models depend on human photographic conventions (centering, canonical distance, upright framing) using decentered/unconventional captures.
- Problem: [KNOWN FACT] Datasets are photographed by humans making aesthetic choices; robot/embodied cameras violate those conventions, and the dependency size is unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Performance on deliberately unconventionally framed captures of the same scenes drops substantially, and the drop is attributable to framing statistics (position/scale priors) rather than content; framing-invariant performance falsifies it.
- Why Important: Embodied AI consumes non-photographic viewpoints; convention dependency is a hidden deployment gap for that entire sector.
- Why Possibly Novel: Paired conventional/unconventional capture of identical scenes isolates framing as the causal variable.
- Minimal Experiment: Capture paired conventional vs decentered/tilted/odd-distance images of fixed scenes; evaluate fixed models; decompose the drop by framing factor.
- Main Risk: Capture effort; a few hundred paired scenes suffice for the main effect.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0267
- Idea: AI-generated contamination in scraped training corpora: estimate the rate of synthetic images entering new vision datasets and measure its effect on segmentation models trained downstream.
- Problem: [KNOWN FACT] The web now contains large volumes of generated imagery; scraped datasets inherit it, with unknown downstream effects on dense-prediction training.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Contemporary scraped corpora contain a detectable and growing synthetic fraction, and training with it measurably shifts model behavior on real-image boundaries (synthetic images carry characteristic boundary/texture statistics); no behavioral effect falsifies the harm claim (while the rate estimate stands alone).
- Why Important: If synthetic contamination alters models, dataset builders need detection/filtering policies now, before rates grow further.
- Why Possibly Novel: Quantifies the feedback loop's effect specifically on dense-prediction behavior with controlled contamination experiments.
- Minimal Experiment: Estimate synthetic rates in recent scrapes via detectors plus manual verification; train models on controlled synthetic-fraction mixtures; measure real-image behavioral deltas.
- Main Risk: Synthetic detectors are imperfect; bound rates with manual audits.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0268
- Idea: Granularity-fingerprint analysis: characterize each dataset's annotation-granularity distribution (what sizes/levels of things get masked) as a measurable fingerprint, and show models inherit their training fingerprint on neutral inputs.
- Problem: [KNOWN FACT] Datasets differ in how finely scenes are decomposed into masks; this policy variable is uncontrolled and its transmission into model behavior is undemonstrated at scale (cf. IDEA-A-0035 for SAM specifically).
- Core Hypothesis (falsifiable): [HYPOTHESIS] Dataset granularity fingerprints are distinctive and stable, and models trained on each dataset reproduce their source fingerprint on a neutral probe suite — proving policy inheritance; non-inherited fingerprints falsify it.
- Why Important: Granularity inheritance means dataset choice silently sets a model's decomposition behavior — a specification issue for anyone selecting training data.
- Why Possibly Novel: Cross-dataset fingerprint extraction plus inheritance verification as a general audit method.
- Minimal Experiment: Compute granularity statistics for 6 datasets; train matched models per dataset; measure fingerprint reproduction on a shared neutral probe set.
- Main Risk: Architecture effects on granularity; hold architecture fixed across the comparison.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0269
- Idea: Benchmark confidence intervals via test-set resampling: compute bootstrap uncertainty for popular segmentation leaderboards and identify which published rank differences are statistically meaningless.
- Problem: [KNOWN FACT] Leaderboards report point estimates; test sets are finite samples, yet rank claims are made without uncertainty quantification.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Bootstrap confidence intervals overlap for a large fraction of adjacent leaderboard pairs, meaning many published orderings are statistically unresolved; mostly non-overlapping intervals falsify it.
- Why Important: Attaching uncertainty to leaderboards recalibrates which "wins" the field should believe and cite.
- Why Possibly Novel: Not the idea of bootstrap itself, but a comprehensive uncertainty retrofit of existing dense-prediction leaderboards with a maintained public artifact.
- Minimal Experiment: Recompute metrics with image-level bootstrap for many public results on 4 benchmarks; publish interval-annotated leaderboards and the unresolved-pair fraction.
- Main Risk: Correlated errors across images complicate bootstrap validity; use clustered resampling where structure exists.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0270
- Idea: Automatic hidden-stratification discovery validity: test whether unsupervised subgroup-discovery methods find the performance-disparate subgroups that matter, validated against expert-defined strata in segmentation datasets.
- Problem: [KNOWN FACT] Aggregate metrics hide subgroup failures; automatic subgroup discovery promises to expose them, but its validity for dense prediction (do discovered subgroups match real, actionable strata?) is untested.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Current discovery methods recover a substantial fraction of expert-defined disparate subgroups on segmentation tasks but also produce plausible-looking spurious strata at a measurable rate — both numbers being essential for responsible use; either extreme (perfect or useless recovery) falsifies the nuanced claim.
- Why Important: Subgroup auditing is entering regulatory practice; its tooling must be validated before institutions trust it.
- Why Possibly Novel: Ground-truthed validation design for subgroup discovery in dense prediction, with false-discovery accounting.
- Minimal Experiment: On datasets with rich metadata, hide expert strata; run discovery methods on model errors; score recovery and false-discovery rates.
- Main Risk: Expert strata are incomplete truth; treat recovery as lower-bound evidence and document.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0271
- Idea: Dataset-level shortcut census: mine co-occurrence and background-correlation structure in segmentation datasets to predict which shortcuts models will adopt, then verify the predictions behaviorally.
- Problem: [KNOWN FACT] Shortcut learning is diagnosed post hoc, model by model; the dataset-side statistics that generate shortcuts could enable prediction before training, but the predictive link is unvalidated.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A dataset-statistics-based shortcut-risk score predicts which class-context dependencies trained models actually exhibit (verified by intervention tests), with useful precision; unpredictable shortcut adoption falsifies it.
- Why Important: Predictive shortcut auditing would let dataset builders fix risks before anyone trains on the data.
- Why Possibly Novel: Closes the loop from dataset statistics to verified model behavior, rather than stopping at correlation mining.
- Minimal Experiment: Compute shortcut-risk scores for many class-context pairs; train models; verify adopted shortcuts via context-masking interventions; score prediction quality.
- Main Risk: Shortcut adoption may be architecture-dependent; test across 3 architectures.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0272
- Idea: Influence-concentration audit: measure how concentrated benchmark conclusions are on small training subsets by removing top-influence tranches and observing ranking stability.
- Problem: [KNOWN FACT] Training examples contribute unequally; if benchmark conclusions hinge on tiny influential subsets, conclusions are fragile to curation choices nobody scrutinizes.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Removing a small top-influence fraction of training data changes cross-model benchmark rankings substantially more than removing random fractions of equal size — conclusions are influence-concentrated; equal sensitivity falsifies it.
- Why Important: Influence concentration would mean benchmark outcomes are curatorial accidents at the margin — critical context for close comparisons.
- Why Possibly Novel: Influence analysis aimed at conclusion stability (rankings) rather than single-model accuracy.
- Minimal Experiment: Estimate training-example influence cheaply; retrain models on ablated sets (top-influence vs random); compare ranking perturbations.
- Main Risk: Influence estimation cost/quality; use scalable approximations with spot-check validation.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0273
- Idea: Dense-task data-pruning laws: test whether pruning-score methods developed on classification transfer to segmentation, or whether dense prediction needs fundamentally different example-value measures.
- Problem: [KNOWN FACT] Data pruning laws promise compute savings; their score functions were designed for classification, and a segmentation example contains many pixels of heterogeneous value — transfer is doubtful and untested.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Classification-derived pruning scores rank segmentation examples poorly (pruned sets underperform random pruning at high ratios), while region-aware value measures preserve performance — dense pruning needs its own laws; successful naive transfer falsifies it.
- Why Important: Data curation at dense-task scale is expensive; knowing which value measures actually work prevents costly mispruning.
- Why Possibly Novel: A transfer-validity study of the pruning-law framework across task types, with a dense-specific alternative hypothesis.
- Minimal Experiment: Prune segmentation training sets by classification-derived and region-aware scores at several ratios; train matched models; compare against random-pruning baselines.
- Main Risk: Score implementations vary; use published implementations and document adaptations.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0274
- Idea: Evaluation-side hard-negative deficiency: quantify how the absence of near-miss negatives in test sets makes false-positive behavior unmeasurable, and build negative-enriched evaluation extensions.
- Problem: [KNOWN FACT] Benchmarks consist mostly of positive-containing images; systems' behavior on compelling near-miss negatives (the deployment false-alarm driver) goes unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Models indistinguishable on standard test sets separate widely on negative-enriched extensions (near-miss false-positive rates differing by large factors), revealing a hidden quality dimension; no separation falsifies it.
- Why Important: False alarms dominate deployment costs in monitoring applications; evaluation must measure them to drive improvement.
- Why Possibly Novel: Systematic negative-set engineering as an evaluation product, with separation evidence across model zoos.
- Minimal Experiment: Curate near-miss negative sets for 5 classes (visually similar non-instances); measure false-positive separation across models scored equal on standard sets.
- Main Risk: Near-miss curation is class-specific labor; scope classes carefully.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0275
- Idea: Consensus-QC diversity destruction: test whether crowdsourcing quality control that enforces inter-annotator agreement systematically removes valid minority interpretations of ambiguous scenes.
- Problem: [KNOWN FACT] Crowd pipelines filter annotations by agreement; for genuinely ambiguous content, disagreement is signal, and agreement filtering may homogenize the ground truth artificially.
- Core Hypothesis (falsifiable): [HYPOTHESIS] On verified-ambiguous items, agreement-based QC discards annotations that expert adjudication rates as valid at a substantial rate, and datasets built with such QC exhibit artificially low ambiguity compared to expert-panel references; negligible valid-discard rates falsify it.
- Why Important: If QC destroys ambiguity, models trained on QC'd data inherit false confidence about ambiguous scenes — connecting pipeline mechanics to model overconfidence.
- Why Possibly Novel: Audits the QC mechanism itself as a distortion source, with expert adjudication as the reference standard.
- Minimal Experiment: Reprocess raw multi-annotator data (where preserved) under agreement QC; have experts adjudicate discarded annotations; measure valid-discard rates and downstream ambiguity statistics.
- Main Risk: Raw pre-QC data is rarely preserved; partner with annotation platforms or generate fresh raw data on ambiguous subsets.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0276
- Idea: Metric ceilings from ground-truth polygon sparsity: compute per-dataset upper bounds on boundary metrics imposed by polygon vertex density, and flag comparisons that press against the ceiling.
- Problem: [KNOWN FACT] Polygon annotations approximate true boundaries with finite vertices; beyond a quality level, measured "error" is polygon discretization, not model failure.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For several benchmarks, top models already operate near the polygon-imposed boundary-metric ceiling, so recent boundary-quality "improvements" partially measure noise; a large remaining gap to ceiling falsifies it.
- Why Important: Identifies where benchmarks are exhausted for boundary claims and where higher-fidelity ground truth is required for further science.
- Why Possibly Novel: Analytic ceiling computation from annotation geometry, applied across benchmarks with proximity-to-ceiling reporting.
- Minimal Experiment: Estimate discretization ceilings from vertex statistics (validated on high-fidelity re-annotations of samples); compare top-model boundary scores against ceilings per dataset.
- Main Risk: True boundaries needed for validation; re-annotate small samples at high fidelity.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0277
- Idea: Polygon corner-cutting bias: measure the systematic geometric bias (curvature-dependent inward cutting) that polygon annotation imposes on curved boundaries, and its inheritance by trained models.
- Problem: [KNOWN FACT] Straight polygon segments approximate curves from the inside; this predicts a curvature-correlated systematic bias in ground truth whose model inheritance is unverified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Ground-truth boundary bias correlates with local curvature as geometry predicts, and models trained on polygon data reproduce the bias even on smooth-boundary synthetic tests — inherited convention masquerading as behavior; no inheritance falsifies it.
- Why Important: A predictable inherited bias is correctable post hoc — free boundary accuracy for area/shape measurement applications.
- Why Possibly Novel: Closes the chain from annotation-tool geometry to ground-truth bias to model behavior with a correction test.
- Minimal Experiment: Quantify curvature-conditional GT bias against high-fidelity references; test trained models on smooth synthetic boundaries; measure the inherited component and evaluate analytic correction.
- Main Risk: High-fidelity references needed at scale; use rendered scenes with exact boundaries for the inheritance test.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0278
- Idea: Effective sample size of video datasets: quantify inter-frame redundancy in video segmentation benchmarks and report redundancy-corrected dataset sizes and metric uncertainties.
- Problem: [KNOWN FACT] Video datasets report frame counts, but temporally adjacent frames are highly correlated; statistical claims implicitly overstate the independent evidence.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Effective sample sizes of popular video benchmarks are an order of magnitude below nominal frame counts (measured by correlation-corrected estimators), and metric uncertainty recomputed accordingly renders many cross-method claims unresolved; near-nominal effective sizes falsify it.
- Why Important: Puts honest error bars on the entire video-segmentation literature's empirical claims.
- Why Possibly Novel: Effective-sample-size methodology (standard in time-series statistics) imported into video benchmark metrology.
- Minimal Experiment: Estimate temporal correlation structures of per-frame scores across benchmarks; compute effective sizes; republish uncertainty-corrected comparisons for existing results.
- Main Risk: Correlation structure varies by metric; compute per metric and report the range.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0279
- Idea: License-filtered distribution skew: measure how restricting datasets to permissively licensed imagery changes content distribution (subjects, regions, styles) and downstream model behavior.
- Problem: [KNOWN FACT] Legal pressure pushes dataset builders toward permissive-license subsets; licensing correlates with who photographs what, so filtering plausibly skews content in unmeasured ways.
- Core Hypothesis (falsifiable): [HYPOTHESIS] License-filtered corpora differ measurably in content distribution from unfiltered ones (subject classes, geography, production quality), and models trained on filtered data show corresponding behavioral skews on neutral tests; distribution-neutral filtering falsifies it.
- Why Important: The field is drifting toward license-clean data for good reasons; the representational costs should be measured, not discovered later.
- Why Possibly Novel: Treats licensing as a sampling mechanism with quantified distributional consequences for vision training.
- Minimal Experiment: Compare content statistics of license-stratified corpus partitions; train matched models per partition; measure behavioral differences on balanced probes.
- Main Risk: License metadata is noisy; use conservatively verified partitions.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0280
- Idea: Active-learning lock-in: test whether datasets built via model-guided active learning are systematically worse for training future, different models — a dataset myopia effect.
- Problem: [KNOWN FACT] Active learning selects examples informative for the collector model; the resulting dataset's value for architecturally different future models is assumed but plausibly degraded.
- Core Hypothesis (falsifiable): [HYPOTHESIS] At matched budgets, AL-collected datasets underperform random/diversity-collected ones when training model families different from the collector, with the gap growing with model-family distance — a measurable lock-in tax; no cross-family gap falsifies it.
- Why Important: Datasets outlive the models that collected them; lock-in would argue for diversity-based collection as institutional policy.
- Why Possibly Novel: Evaluates collection strategies by future-model value rather than collector-model value — the question institutions actually face.
- Minimal Experiment: Collect budget-matched datasets under AL vs diversity strategies with model A; train models B/C/D on each; compare cross-family training value.
- Main Risk: Simulated collection may understate real AL pipelines; replicate one condition with a real annotation loop.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0281
- Idea: Sequential leaderboard overfitting estimation: apply adaptive-data-analysis corrections to years of benchmark submissions and estimate how much reported progress survives correction.
- Problem: [KNOWN FACT] Test sets are queried repeatedly across years of submissions; statistical theory says repeated adaptive querying inflates apparent progress, but nobody has quantified the effect for vision benchmarks.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Correction methods and fresh-test-set replications agree that a measurable fraction of late-stage leaderboard gains on mature benchmarks does not replicate on freshly collected equivalent test data; full replication falsifies it.
- Why Important: Distinguishing real progress from test-set adaptation is foundational for trusting the field's self-assessment.
- Why Possibly Novel: Empirical adaptive-overfitting quantification for dense-prediction benchmarks using both theory-based corrections and fresh-data replication.
- Minimal Experiment: Collect a fresh statistically matched test set for one mature benchmark; re-evaluate historical submissions; compare progress curves on old vs fresh data.
- Main Risk: Fresh-set matching quality; document collection protocol exhaustively and audit comparability.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0282
- Idea: Annotation-tool style imprinting: demonstrate that the annotation tool used (polygon, brush, superpixel-snapping, model-assisted) leaves a classifiable signature in masks, and that models inherit tool styles as behavioral biases.
- Problem: [KNOWN FACT] Datasets are produced with different tools whose interaction mechanics shape boundary geometry; tool identity is an unrecorded latent variable in every dataset.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Tool identity is predictable from mask geometry at high accuracy, and models trained on tool-homogeneous data reproduce the tool's signature on new images — tools imprint through the data into models; unclassifiable tool signatures falsify it.
- Why Important: Tool imprinting would mean part of what models learn is interface mechanics, and mixed-tool training data contains style conflicts nobody controls for.
- Why Possibly Novel: Identifies the annotation tool as a causal actor in model behavior, with a full transmission-chain demonstration.
- Minimal Experiment: Annotate a common image set with multiple tools; train tool classifiers on mask geometry; train segmentation models per tool condition; test signature reproduction.
- Main Risk: Annotator identity confounds with tool; use within-annotator tool crossover design.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0283
- Idea: Context-leakage in single-object crops: measure how much benchmark performance on object-centric datasets depends on background context leaked into crops, using context-replacement evaluations.
- Problem: [KNOWN FACT] Object-centric datasets crop around targets but retain background; models may exploit background statistics, inflating apparent object-recognition capability.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Replacing backgrounds with neutral or mismatched content (preserving the object pixels exactly) drops performance substantially and heterogeneously across classes, quantifying per-class context dependence embedded in the benchmark; robust performance falsifies it.
- Why Important: Benchmarks intending to measure object understanding may partially measure background statistics — a validity correction with per-class specificity.
- Why Possibly Novel: Context-replacement as a benchmark-validity instrument with published per-class dependence tables.
- Minimal Experiment: Build context-replaced variants of an object-centric benchmark; evaluate model zoos; publish per-class context-dependence scores.
- Main Risk: Compositing artifacts; use high-quality mask-based replacement with artifact controls.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0284
- Idea: Negative-image evaluation gap: quantify how excluding target-absent images from dataset design makes deployment false-alarm behavior unmeasurable, and retrofit negative-image test extensions to popular benchmarks.
- Problem: [KNOWN FACT] Many segmentation datasets include only images containing the classes of interest; deployed systems mostly see target-absent inputs, an evaluation regime the benchmarks structurally cannot cover.
- Core Hypothesis (falsifiable): [HYPOTHESIS] On retrofitted negative-image extensions, models with equal benchmark scores differ by large factors in false-positive area rates, and negative-image behavior is uncorrelated with positive-image scores; strong correlation falsifies the need.
- Why Important: Two models identical on the benchmark can differ 10x in deployment false alarms — buyers and builders need the missing measurement (companion to IDEA-A-0146 for detection).
- Why Possibly Novel: Systematic negative-extension retrofitting with cross-model separation evidence for segmentation benchmarks.
- Minimal Experiment: Assemble verified target-absent extensions for 3 benchmarks; evaluate model zoos; report false-positive separation and correlation with standard scores.
- Main Risk: Verified absence at scale; use multi-model screening plus human audit.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0285
- Idea: Metric-dataset coupling audit: test whether historical metric choices co-evolved with dataset properties in ways that flattered contemporary methods, by re-scoring history under a metric battery.
- Problem: [KNOWN FACT] Communities choose metrics that make their datasets discriminative; whether this coupling has systematically shaped which method families "won" is an open sociotechnical question with measurable substance.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Re-scoring historical method generations under a broad metric battery reveals era-dependent ranking reversals aligned with the era's dominant metric — evidence that metric choice partially selected the winners; era-invariant rankings falsify it.
- Why Important: Understanding metric-driven selection effects informs how the field should choose evaluation standards going forward.
- Why Possibly Novel: A quantitative history-of-science study executed with code and checkpoints rather than narrative.
- Minimal Experiment: Assemble representative method implementations per era; evaluate all under a fixed metric battery; analyze ranking-by-metric-by-era interactions.
- Main Risk: Historical implementations vary in quality; use best-available public reproductions and report caveats.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0286
- Idea: Statistical power audit of rare-class claims: compute the effective test-instance counts behind published rare-class metrics and determine which long-tail improvement claims are statistically supportable.
- Problem: [KNOWN FACT] Rare-class test metrics may rest on a handful of instances; papers report per-class improvements without power analysis.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A large fraction of published rare-class improvement claims fall below reasonable statistical power thresholds (undetectable effect sizes given instance counts), making them unsupported regardless of truth; adequately powered claims falsify it.
- Why Important: Long-tail research direction is being set by potentially unpowered evidence — the field should know its own evidentiary standards.
- Why Possibly Novel: Power-analysis methodology applied retrospectively to a literature's claims, with a usable per-benchmark power table as the artifact.
- Minimal Experiment: Extract rare-class claims from recent papers; compute test-set power per claim; publish the supportability census and per-benchmark minimum-detectable-effect tables.
- Main Risk: Claim extraction subjectivity; use preregistered inclusion criteria and dual extraction.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0287
- Idea: Universal difficulty hypothesis: test whether per-image difficulty rankings are stable across model families and eras, implying difficulty is an image property rather than a model property.
- Problem: [KNOWN FACT] Per-image difficulty is used for curriculum, pruning, and analysis, implicitly assuming model-independence; the assumption's validity for dense prediction is unverified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Per-image difficulty rankings correlate highly across diverse model families (a shared difficulty backbone), with a small model-specific residual concentrated in identifiable image types; low cross-family correlation falsifies it.
- Why Important: If difficulty is image-intrinsic, one-time difficulty annotation is a reusable dataset asset; if not, every difficulty-based method is model-bound.
- Why Possibly Novel: Systematic universality test across families/eras with residual characterization for dense tasks.
- Minimal Experiment: Score per-image difficulty from many diverse models on shared benchmarks; measure cross-family rank correlations; characterize the residual structure.
- Main Risk: Difficulty operationalization choices; use several definitions and report agreement.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0288
- Idea: Ground-truth reproducibility experiment: re-run the original annotation protocol of a benchmark on a sample with fresh annotators and measure how reproducible the dataset's ground truth actually is.
- Problem: [KNOWN FACT] Datasets are treated as fixed truth; the reproducibility of the annotation process itself (same protocol, different people/time) is almost never measured, though it bounds meaningful model comparison.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Protocol re-execution produces ground truth differing from the original by more than the margins separating top leaderboard entries — the benchmark's truth is less reproducible than its rankings pretend; high reproducibility falsifies it.
- Why Important: If truth reproducibility bounds are wider than method differences, leaderboard interpretation must fundamentally change.
- Why Possibly Novel: Treats the dataset as an experiment to be replicated — importing replication-crisis methodology into benchmark science.
- Minimal Experiment: Re-annotate stratified samples of 2 benchmarks under original published protocols; quantify original-vs-replication divergence; compare against leaderboard margins.
- Main Risk: Protocol documentation gaps; choose benchmarks with thorough published guidelines.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0289
- Idea: Sensor-metadata shortcut audit: test whether models exploit camera-model/processing fingerprints correlated with labels in mixed-source datasets (certain classes photographed by certain devices).
- Problem: [KNOWN FACT] Dataset sources correlate with content (wildlife photos from certain cameras, indoor scenes from phones); device-level fingerprints are learnable and could act as label shortcuts.
- Core Hypothesis (falsifiable): [HYPOTHESIS] In popular mixed-source datasets, class labels are partially predictable from device fingerprints alone (content-blind features), and models measurably lose accuracy when fingerprints are neutralized — shortcut confirmed; no fingerprint-label association falsifies it.
- Why Important: Device shortcuts inflate benchmark scores and collapse under deployment device changes — a hidden fragility with a measurable size.
- Why Possibly Novel: Content-blind fingerprint analysis linking forensics techniques to shortcut-learning auditing.
- Minimal Experiment: Extract device fingerprints (noise/ISP signatures) from benchmark images; test label predictability; evaluate models on fingerprint-neutralized images.
- Main Risk: Neutralization may touch content; validate content preservation with human checks.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0290
- Idea: Compression-stratification shortcuts: measure whether JPEG quality levels correlate with labels in popular datasets (different sources, different compression) and whether models exploit compression level as a feature.
- Problem: [KNOWN FACT] Dataset sources apply different compression; if compression level correlates with content classes, models can learn artifact-level shortcuts invisible to human auditors.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Label-compression correlations exist in mixed-source benchmarks, and recompressing test images to uniform quality measurably shifts model accuracy in the direction predicted by the correlation — demonstrating exploitation; no shift falsifies it.
- Why Important: A compression shortcut means reported accuracy partially measures archival practices — and breaks when deployment compression differs.
- Why Possibly Novel: Compression forensics turned into a shortcut-detection protocol with intervention verification.
- Minimal Experiment: Estimate per-image compression parameters across benchmarks; test label association; evaluate models on uniformly recompressed test sets; compare against prediction.
- Main Risk: Recompression alters genuine signal; use modest uniformization and report the tradeoff.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0291
- Idea: Ontology-merge inconsistency: measure the internal contradiction rate introduced when datasets merge classes from different ontologies (mapping decisions that make "the same" class internally heterogeneous).
- Problem: [KNOWN FACT] Composite datasets merge upstream label systems; merge decisions create classes whose members would be distinguished by one upstream ontology and conflated by another, producing internal inconsistency of unknown magnitude.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Merged classes exhibit measurable internal bimodality (upstream-origin predictable from features within the merged class), and models show elevated confusion exactly along merged seams; homogeneous merged classes falsify it.
- Why Important: Merge-seam errors masquerade as model failures; identifying them redirects blame to dataset construction and enables seam-aware evaluation.
- Why Possibly Novel: Seam-level analysis of composite datasets — auditing the merge decisions as an error source.
- Minimal Experiment: For composite benchmarks with documented merges, test within-class origin predictability; measure model error concentration along merge seams.
- Main Risk: Merge documentation may be incomplete; recover origins via provenance matching where possible.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0292
- Idea: Unlabeled-object rate effects in sparsely annotated detection training: quantify how the known-incomplete labeling of some detection datasets biases trained models, using completeness-controlled subsets.
- Problem: [KNOWN FACT] Some large detection datasets annotate only a subset of present objects per image (sparse labeling policies); training treats unlabeled objects as background, a structured supervision error.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Sparse-labeling-trained models systematically suppress detections in contexts where unlabeled objects concentrated (a measurable learned suppression), and completeness-corrected training on the same images recovers the suppressed recall; no suppression signature falsifies it.
- Why Important: Quantifies the training cost of a widespread labeling economy decision and validates cheap correction options.
- Why Possibly Novel: Isolates the sparse-labeling mechanism with completeness-controlled counterfactual training on identical images.
- Minimal Experiment: Take a densely labeled dataset; synthetically sparsify labels under realistic policies; train matched models; map recall suppression vs sparsification pattern; test corrections.
- Main Risk: Synthetic sparsification may miss real policy structure; mirror documented policies of actual datasets.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0293
- Idea: Noise-floor estimation for benchmark saturation: estimate each benchmark's label-noise floor and determine which "remaining headroom" on mature leaderboards is real versus noise-chasing.
- Problem: [KNOWN FACT] Mature benchmarks show shrinking gains; whether the top is pressing against label-noise limits (making further gains meaningless) is rarely computed per benchmark.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For several mature segmentation benchmarks, estimated noise floors lie within the range of current top scores, implying recent incremental gains partially fit annotation noise; floors well above current scores falsify it.
- Why Important: Declares which benchmarks are scientifically exhausted — protecting the field from optimizing noise and prompting successor benchmarks.
- Why Possibly Novel: Benchmark-level noise-floor accounting combining label-error estimates (cf. IDEA-A-0262) and multi-rater variance into a saturation verdict.
- Minimal Experiment: Combine re-annotation-based error rates and rater variance into floor estimates for 4 benchmarks; position current leaderboards against the floors.
- Main Risk: Floor estimation assumptions; report floors as ranges under stated assumptions.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0294
- Idea: Documentation-completeness effects: test whether datasets with more complete documentation (collection process, annotation guidelines, known limitations) show measurably fewer downstream misuse patterns in the literature that cites them.
- Problem: [KNOWN FACT] Dataset documentation practices vary enormously; the community assumes documentation matters but has no measured link from documentation quality to downstream research quality.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Citation-context analysis shows datasets with poor documentation accumulate significantly more identifiable misuse (wrong-task application, ignored known limitations, invalid comparisons) per citation than well-documented peers; no association falsifies it.
- Why Important: An evidence-based case (or counter-case) for documentation standards would move dataset governance from exhortation to policy.
- Why Possibly Novel: Meta-research linking documentation artifacts to measurable downstream research behavior in vision.
- Minimal Experiment: Score documentation completeness for 30 datasets; sample and code citation contexts for misuse patterns; model the association with confounder controls.
- Main Risk: Misuse coding subjectivity; use dual-coder protocols with adjudication.
- Research Cluster tag: DATA-FAIL

### IDEA-A-0295
- Idea: Black-box membership testing for segmentation benchmarks: develop and validate tests detecting whether a foundation model was trained on a given benchmark's test images, using mask-reproduction fidelity signatures.
- Problem: [KNOWN FACT] Foundation-model training corpora are opaque; benchmark contamination inflates evaluation, and segmentation-specific membership tests (exploiting structured outputs) are undeveloped.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Contaminated models reproduce benchmark ground-truth idiosyncrasies (annotator-specific boundary quirks) at rates statistically separable from clean models, yielding a usable membership test with quantified error rates; inseparable behavior falsifies it.
- Why Important: A validated contamination test would let the community audit foundation-model claims on public benchmarks — an accountability instrument.
- Why Possibly Novel: Exploits dense-output structure (boundary idiosyncrasy matching) for membership inference, beyond classification-based tests.
- Minimal Experiment: Train matched models with/without benchmark inclusion; develop the signature test; report detection/false-alarm rates; apply to public models with caveats.
- Main Risk: Legal/ethical sensitivity in applying to commercial models; report methodology and aggregate findings responsibly.
- Research Cluster tag: DATA-FAIL

---

## Section 9 — Foundation model failure (IDEA-A-0296 .. 0325)

### IDEA-A-0296
- Idea: Boundary-precision scaling curves: measure whether boundary-quality metrics scale with model/data size at the same rate as region-overlap metrics, testing if scale fixes fine structure.
- Problem: [KNOWN FACT] Scaling improves aggregate benchmark numbers; whether all quality dimensions benefit equally — or boundary precision lags structurally — is undetermined for segmentation foundations.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Across a model-scale series, boundary metrics improve with a measurably smaller scaling exponent than region metrics, implying scale alone will not close the boundary gap; equal exponents falsify it.
- Why Important: If boundary quality is scale-resistant, the field's "wait for bigger models" strategy fails for precision applications — a directional result for research investment.
- Why Possibly Novel: Dimension-resolved scaling-law analysis for dense prediction, separating what scale buys from what it doesn't.
- Minimal Experiment: Evaluate a public model-scale series with region and boundary metrics across datasets; fit and compare scaling exponents per dimension.
- Main Risk: Few clean scale series exist; use available families and report family effects.
- Research Cluster tag: FM-FAIL

### IDEA-A-0297
- Idea: Patch-grid error forensics: measure whether foundation-model segmentation errors concentrate at patch-boundary positions, quantifying tokenization artifacts in dense outputs.
- Problem: [KNOWN FACT] Vision transformers process fixed patch grids; whether the grid leaves detectable artifacts in output error distributions is unquantified across models.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Error rates exhibit statistically significant periodicity aligned with each model's patch grid (detectable via error histograms modulo patch size), with amplitude varying by decoder design; aperiodic errors falsify it.
- Why Important: Grid artifacts are correctable (test-time shifts, ensembling offsets) but only if demonstrated and measured per model.
- Why Possibly Novel: Systematic spectral/periodicity analysis of dense error fields against architectural constants (companion to prompt-side IDEA-A-0219).
- Minimal Experiment: Accumulate error maps for many models; compute periodograms against patch grids; report artifact amplitudes and test shift-ensembling correction.
- Main Risk: Content periodicity confounds; use phase-randomized controls and translated-input pairs.
- Research Cluster tag: FM-FAIL

### IDEA-A-0298
- Idea: Spatial-information recoverability probe: measure how much precise localization information survives in contrastively pretrained vision-language embeddings, bounding what any dense head can extract from them.
- Problem: [KNOWN FACT] Contrastive image-text pretraining optimizes global agreement; the resulting features power many open-vocabulary segmenters, but their intrinsic spatial-information ceiling is unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Optimal probes recover object-level localization but systematically fail at boundary-precision localization from such features (a measurable spatial ceiling well below supervised features), explaining persistent open-vocabulary boundary weakness; full recoverability falsifies it.
- Why Important: A demonstrated ceiling redirects open-vocabulary segmentation research from decoder engineering to pretraining-objective questions.
- Why Possibly Novel: Information-ceiling measurement (probing sweep with capacity controls) targeted at the spatial content of contrastive features.
- Minimal Experiment: Train capacity-swept probes from frozen contrastive features for localization tasks of graded precision; map the recoverability curve; compare against supervised-feature baselines.
- Main Risk: Probe optimization quality caps conclusions; use generous budgets and report convergence evidence.
- Research Cluster tag: FM-FAIL

### IDEA-A-0299
- Idea: Absence benchmark for language-prompted segmentation: measure hallucinated-mask rates when prompted for objects verifiably absent, across foundation models and prompt phrasings.
- Problem: [KNOWN FACT] Language-prompted segmenters are evaluated on present objects; their behavior under absence — the deployment-common case — is unmeasured at foundation scale (extends IDEA-A-0125 from detection to segmentation).
- Core Hypothesis (falsifiable): [HYPOTHESIS] Absent-object prompts yield confident masks at high rates, hallucination rates vary widely across models independent of present-object accuracy, and grounded phrasings ("if present") reduce but do not eliminate the effect; low uniform hallucination falsifies it.
- Why Important: Establishes the reliability dimension that separates usable from dangerous language-driven segmentation in open-world settings.
- Why Possibly Novel: A standardized absence-conditioned benchmark with phrasing interventions at foundation-model scale.
- Minimal Experiment: Build verified-absence prompt sets over diverse images; measure per-model hallucination-rate profiles and phrasing effects; publish the benchmark.
- Main Risk: Absence verification labor; use exhaustively annotated source datasets.
- Research Cluster tag: FM-FAIL

### IDEA-A-0300
- Idea: Abstention-capability audit: test whether any current segmentation foundation model can be made to output "nothing to segment" reliably, and measure the cost of forcing abstention via output post-processing.
- Problem: [KNOWN FACT] Segmentation heads structurally emit masks; a trustworthy "no answer" capability is absent from interfaces and unmeasured as behavior.
- Core Hypothesis (falsifiable): [HYPOTHESIS] No current model achieves usable abstention operating points natively (high abstention precision without large recall cost), and threshold-based retrofits remain far from an oracle abstention bound — quantifying a capability gap; native or cheap retrofit abstention falsifies it.
- Why Important: Abstention is a prerequisite for autonomous deployment; measuring the gap (and the oracle bound) defines a concrete capability target.
- Why Possibly Novel: Abstention as a first-class measured capability with oracle-gap accounting for dense prediction.
- Minimal Experiment: Define abstention tasks over mixed present/absent inputs; evaluate native signals and retrofits per model against oracle bounds; publish the gap table.
- Main Risk: Retrofit design space is large; standardize a small battery and invite extension.
- Research Cluster tag: FM-FAIL

### IDEA-A-0301
- Idea: Frozen-feature version drift: measure how much downstream dense-prediction heads break when the underlying foundation encoder is updated to a new version, quantifying the hidden cost of "just upgrade the backbone-as-a-service."
- Problem: [KNOWN FACT] Organizations build heads on frozen foundation features and upgrade encoders when providers release new versions; feature-space compatibility across versions is undocumented.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Version upgrades cause severe downstream degradation without head retraining (feature spaces are version-incompatible), and lightweight alignment recovers only part of it — establishing versioning as a real operational hazard; near-compatibility falsifies it.
- Why Important: Quantifies an infrastructure risk affecting every downstream team, informing version-pinning and migration policies.
- Why Possibly Novel: Version-compatibility measurement for vision foundation features with recovery-cost accounting — an MLOps science question the literature skips.
- Minimal Experiment: Train heads on version-N features; evaluate under version-N+1 with/without alignment adapters; report degradation and recovery costs across model families.
- Main Risk: Limited public version series; use families with documented releases.
- Research Cluster tag: FM-FAIL

### IDEA-A-0302
- Idea: Longitudinal API-output drift audit: measure whether hosted vision-model endpoints return changing outputs for identical inputs over months, and quantify the reproducibility hazard for research built on them.
- Problem: [KNOWN FACT] Hosted model APIs may change silently (model updates, infrastructure changes); vision-specific drift rates and magnitudes are undocumented, though research increasingly cites API results.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Repeated identical queries over months show detectable output drift for a substantial fraction of endpoints, with drift events large enough to alter benchmark conclusions drawn from earlier queries; stable outputs falsify it.
- Why Important: If endpoints drift, API-based evaluation results have expiration dates — the community needs the measurement and citation practices to match.
- Why Possibly Novel: A systematic longitudinal reproducibility observatory for vision APIs with event detection and effect sizing.
- Minimal Experiment: Query fixed input batteries against several endpoints on a schedule for months; detect and characterize drift events; simulate their effect on benchmark conclusions.
- Main Risk: Terms-of-service constraints; select endpoints permitting research use and document compliance.
- Research Cluster tag: FM-FAIL

### IDEA-A-0303
- Idea: Distillation-tax census: measure which capabilities (rare classes, boundary precision, prompt fidelity, robustness) efficient distilled variants of segmentation foundations lose first relative to their teachers.
- Problem: [KNOWN FACT] Deployment favors distilled/efficient variants; headline metrics show small gaps, but capability-resolved losses are unreported, so users cannot know what they gave up.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Distillation losses are strongly capability-uneven — long-tail concepts and worst-case robustness degrade disproportionately versus headline metrics — and the loss profile is consistent across distillation recipes; uniform proportional loss falsifies it.
- Why Important: A published tax table per efficient variant lets deployers match model choice to their capability requirements instead of headline numbers.
- Why Possibly Novel: Standardized capability-resolved teacher-student diffing across public efficient segmentation models.
- Minimal Experiment: Evaluate teacher-student pairs on a capability battery; publish loss profiles; test profile consistency across recipes.
- Main Risk: Confounds between distillation and architecture change; note which pairs isolate distillation cleanly.
- Research Cluster tag: FM-FAIL

### IDEA-A-0304
- Idea: Concept-interference measurement in dense features: test whether co-active concepts interfere in foundation features (superposition), degrading segmentation exactly when many concepts overlap spatially.
- Problem: [KNOWN FACT] Features may encode more concepts than dimensions via superposition; for dense prediction, spatial co-activation of many concepts could cause measurable interference, but the link to segmentation failure is untested.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Per-pixel segmentation error grows with the measured number of strongly co-active concept directions at that location (controlling for clutter and scale), evidencing interference-limited capacity; no relationship falsifies it.
- Why Important: Would identify a representational mechanism behind cluttered-scene failure, suggesting capacity (not data) as the binding constraint.
- Why Possibly Novel: Connects interpretability-style concept-direction analysis to spatially resolved dense-task error prediction.
- Minimal Experiment: Extract concept-activation maps from frozen features; regress per-pixel error on co-activation counts across scenes; test the interference prediction on held-out data.
- Main Risk: Concept-direction extraction choices; use multiple extraction methods and report agreement.
- Research Cluster tag: FM-FAIL

### IDEA-A-0305
- Idea: Linear-probe-to-fine-tune gap as a pretraining diagnostic: test whether the gap between probe and fine-tune performance on dense tasks predicts which pretraining produces the best foundation for segmentation.
- Problem: [KNOWN FACT] Pretraining approaches are compared by fine-tuned endpoints; the probe/fine-tune gap carries information about feature readiness that dense-task comparisons rarely exploit.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Pretrainings with small probe-to-fine-tune gaps on dense tasks transfer more robustly across domains (readiness predicts robustness), making the gap a cheap pretraining-quality diagnostic; no predictive relationship falsifies it.
- Why Important: A cheap diagnostic would let pretraining developers evaluate dense-task readiness without full fine-tuning sweeps.
- Why Possibly Novel: The gap as a validated predictor of cross-domain dense transfer, not just a descriptive statistic.
- Minimal Experiment: For many public pretrainings, measure probe and fine-tune dense performance plus cross-domain robustness; test the gap's predictive validity.
- Main Risk: Probe protocols vary; standardize and release the protocol.
- Research Cluster tag: FM-FAIL

### IDEA-A-0306
- Idea: Resolution-extrapolation artifact map: characterize the systematic error patterns dense foundation models produce at inference resolutions unseen in training (position-encoding interpolation regimes).
- Problem: [KNOWN FACT] Deployment feeds models resolutions they weren't trained at, relying on positional-encoding interpolation; the structured artifacts this induces in dense outputs are uncharted.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Off-resolution inference produces spatially structured errors (center-periphery gradients, aspect-ratio-dependent distortions) that are model-family-specific and predictable from the encoding scheme, enabling per-family safe-resolution envelopes; unstructured degradation falsifies it.
- Why Important: Safe-resolution envelopes are missing operational documentation for every deployed dense model.
- Why Possibly Novel: Artifact-geometry characterization tied to encoding schemes, delivered as usable operating envelopes.
- Minimal Experiment: Evaluate models across resolution/aspect grids; map spatial error structure; correlate with encoding designs; publish envelopes.
- Main Risk: Confound with object-scale effects; use scale-controlled synthetic and resampled natural content.
- Research Cluster tag: FM-FAIL

### IDEA-A-0307
- Idea: Benchmark mask memorization detection: test whether segmentation foundations reproduce ground-truth mask idiosyncrasies of benchmark images verbatim, indicating training-set inclusion of test benchmarks.
- Problem: [KNOWN FACT] Web-scale pretraining may ingest benchmark images and even their annotations; verbatim mask-reproduction evidence would demonstrate contamination directly (mechanism for IDEA-A-0295's test).
- Core Hypothesis (falsifiable): [HYPOTHESIS] On suspected-contaminated items, model outputs match ground-truth annotator idiosyncrasies (exact vertex quirks, convention artifacts) at rates unexplainable by image evidence alone — memorization demonstrated; idiosyncrasy-free matches falsify it.
- Why Important: Direct memorization evidence would force disclosure norms for foundation-model evaluation on public benchmarks.
- Why Possibly Novel: Idiosyncrasy-matching methodology (separating image-driven from annotation-driven agreement) for dense outputs.
- Minimal Experiment: Identify annotation idiosyncrasies uncorrelated with image evidence; measure model reproduction rates on benchmark vs matched non-benchmark images; test the separation statistically.
- Main Risk: Distinguishing idiosyncrasy from convention; validate idiosyncrasy sets with annotator-blind re-annotation.
- Research Cluster tag: FM-FAIL

### IDEA-A-0308
- Idea: Text-encoder bottleneck attribution: test whether open-vocabulary dense performance saturates with vision-encoder scale when the text encoder is held fixed, identifying which tower binds current systems.
- Problem: [KNOWN FACT] Open-vocabulary systems scale vision towers eagerly; whether the text tower is the binding constraint for dense grounding is a resource-allocation question without an answer.
- Core Hypothesis (falsifiable): [HYPOTHESIS] At fixed text-encoder capacity, dense open-vocabulary gains saturate quickly with vision scale, while text-tower scaling at fixed vision capacity yields continued gains on linguistically complex prompts — the text tower binds; vision-bound results falsify it.
- Why Important: Directs the next scaling dollar to the correct tower for dense-task goals.
- Why Possibly Novel: Controlled tower-scaling attribution with dense endpoints, distinct from classification-based scaling studies.
- Minimal Experiment: Train/evaluate tower-scale grids at modest scale; measure dense-task saturation patterns per tower; verify on public checkpoints of varying tower ratios.
- Main Risk: Small-scale grids may not extrapolate; anchor with available large-model checkpoints.
- Research Cluster tag: FM-FAIL

### IDEA-A-0309
- Idea: Cross-foundation disagreement as unsupervised error detection: validate whether disagreement among independent foundation models flags segmentation errors reliably enough for production triage.
- Problem: [KNOWN FACT] Multiple independent foundations now exist; their disagreement is a free error signal whose detection-theoretic quality (per error type) is unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Cross-foundation disagreement detects boundary and localization errors with high recall but systematically misses shared-bias errors (all models wrong identically), and the shared-blindness rate is measurable and stable — defining the method's safety envelope; uninformative disagreement falsifies it.
- Why Important: Production teams need validated triage signals with known blind spots, not just plausible heuristics.
- Why Possibly Novel: Detection-theoretic validation including the shared-blindness accounting that ensemble intuitions usually omit.
- Minimal Experiment: Compute cross-model disagreement maps on labeled data; measure detection performance per error type; quantify shared-bias blind spots across datasets.
- Main Risk: Foundations share training data, inflating shared bias; measure and report data-overlap proxies.
- Research Cluster tag: FM-FAIL

### IDEA-A-0310
- Idea: Effective-robustness re-examination for dense tasks: test whether the in-domain-to-OOD performance relationship that holds for classification also governs segmentation foundations, or whether dense tasks break the pattern.
- Problem: [KNOWN FACT] For classification, OOD performance tracks in-domain performance along stable trend lines; whether dense prediction obeys the same law determines how much OOD evaluation dense benchmarks actually need.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Dense-task OOD performance shows substantially larger residual variance around the in-domain trend than classification (in-domain scores predict OOD worse), so dense OOD evaluation cannot be skipped; tight trend adherence falsifies it.
- Why Important: If the trend is loose, every dense-model comparison needs explicit OOD evaluation — a costly but necessary practice change.
- Why Possibly Novel: Trend-line methodology transplanted to dense prediction with residual-variance comparison as the headline result.
- Minimal Experiment: Assemble in-domain/OOD score pairs for many dense models across shift benchmarks; fit trends; compare residual structures against classification baselines.
- Main Risk: Metric non-comparability across tasks; use rank-based residual analysis.
- Research Cluster tag: FM-FAIL

### IDEA-A-0311
- Idea: Nameability bias: test whether segmentation quality of foundation models correlates with how frequently a concept is named in web text, disadvantaging visually distinct but rarely named things.
- Problem: [KNOWN FACT] Vision-language pretraining supervises through captions; things people rarely write about (pipe fittings, weld defects, plant diseases) may be visually learnable yet caption-starved.
- Core Hypothesis (falsifiable): [HYPOTHESIS] At matched visual difficulty, segmentation quality correlates strongly with caption-corpus name frequency, demonstrating language-mediated visual capability gaps; frequency-independent quality falsifies it.
- Why Important: Industrial and scientific applications live exactly in the rarely-named regime; a demonstrated nameability bias justifies vision-only supervision for those domains.
- Why Possibly Novel: Separates visual difficulty from linguistic exposure with matched-difficulty design — attributing the gap to the supervision channel.
- Minimal Experiment: Build concept sets matched on visual difficulty (human-verified) but differing in text frequency; measure per-concept segmentation quality; test the correlation.
- Main Risk: Visual-difficulty matching is hard; use human psychophysics to validate the matching.
- Research Cluster tag: FM-FAIL

### IDEA-A-0312
- Idea: Compute-optimal re-derivation for dense prediction: test whether the data-versus-parameters compute-allocation rules derived for language/classification transfer to segmentation pretraining.
- Problem: [KNOWN FACT] Compute-optimal scaling prescriptions guide large training runs; dense prediction's different supervision density and output structure may shift the optimum, but nobody has re-derived it.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Dense-task compute-optimal allocation differs measurably from classification-derived rules (favoring different data-parameter ratios), and following transplanted rules leaves quantifiable performance on the table; matching optima falsify it.
- Why Important: Every large dense-pretraining run allocates compute by borrowed rules; a corrected prescription has direct large-scale value.
- Why Possibly Novel: Task-specific compute-optimal analysis for dense prediction at accessible scales with careful extrapolation caveats.
- Minimal Experiment: Train dense-pretraining grids over data-parameter allocations at 2-3 compute budgets; fit allocation optima; compare with transplanted rules.
- Main Risk: Small-budget optima may not extrapolate; report scale-trend consistency checks.
- Research Cluster tag: FM-FAIL

### IDEA-A-0313
- Idea: Frequency-reliance profile shift: measure whether modern self-supervised/vision-language foundations rely on different spatial-frequency bands than the supervised CNN generation, and what that predicts about their failure conditions.
- Problem: [KNOWN FACT] Earlier CNN-era models showed characteristic frequency reliance (texture sensitivity); whether the foundation generation shifted its reliance profile — with different consequent vulnerabilities — is unmapped.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Foundation models show a measurably different band-reliance profile (more mid/low-frequency shape reliance), and each model's profile predicts its specific corruption vulnerabilities better than architecture labels do; unchanged profiles falsify it.
- Why Important: Reliance profiles are compact predictors of when a model breaks — better mental models for deployment engineers than architecture names.
- Why Possibly Novel: Generation-spanning comparative reliance analysis with vulnerability-prediction validation for dense tasks.
- Minimal Experiment: Measure band-ablation sensitivity across model generations; correlate profiles with corruption-specific failure patterns; test predictive power.
- Main Risk: Band ablation methods vary; use several and report profile agreement.
- Research Cluster tag: FM-FAIL

### IDEA-A-0314
- Idea: Emergence analysis of promptability: measure whether interactive segmentation capability appears smoothly or discontinuously across a model-scale series, informing whether small models can be prompt-capable.
- Problem: [KNOWN FACT] Emergent-capability debates focus on language; whether promptable dense prediction has scale thresholds (making small prompt-capable models infeasible) or smooth onset (making them an engineering problem) is unresolved.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Prompt-following quality rises smoothly with scale under continuous metrics (no genuine discontinuity), implying capable small models are achievable with the right training rather than blocked by scale; robust discontinuities under fair metrics falsify it.
- Why Important: Determines whether edge-deployable interactive segmentation is a research dead end or an open engineering opportunity.
- Why Possibly Novel: Applies the metric-artifact-aware emergence methodology to interactive dense capabilities.
- Minimal Experiment: Train/evaluate a scale series with continuous prompt-following metrics; test onset shape under multiple metric choices; identify what small models lack.
- Main Risk: Training-recipe confounds with scale; hold recipes fixed and document deviations.
- Research Cluster tag: FM-FAIL

### IDEA-A-0315
- Idea: Preprocessing-default divergence audit: measure how much published foundation-model results change under the silently differing resize/normalization defaults of common libraries, quantifying a reproducibility hazard.
- Problem: [KNOWN FACT] Different frameworks apply different image preprocessing defaults; papers rarely specify them fully, and foundation models are consumed through heterogeneous toolchains.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Cross-library default divergence causes performance differences comparable to small claimed method improvements for a substantial fraction of model-dataset pairs — an unacknowledged noise source in the literature; negligible differences falsify it.
- Why Important: If defaults rival method effects, the community needs preprocessing declarations as a publication standard — cheap fix, large integrity gain.
- Why Possibly Novel: A quantified cross-toolchain reproducibility study for dense-prediction foundations with a proposed declaration checklist.
- Minimal Experiment: Evaluate fixed checkpoints under the default preprocessing of several major libraries across datasets; report the divergence distribution against published effect sizes.
- Main Risk: Endless configuration space; scope to documented defaults of the top toolchains.
- Research Cluster tag: FM-FAIL

### IDEA-A-0316
- Idea: Human-preference divergence from metrics: collect human quality preferences over foundation-model masks and measure where preferences diverge from IoU-family metrics, defining what mask quality means to users.
- Problem: [KNOWN FACT] Mask metrics were designed for benchmark convenience; whether they track human quality judgments for foundation-model outputs (often plausible-but-different masks) is unverified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Human preferences diverge from IoU-family rankings systematically in identifiable regimes (boundary smoothness vs accuracy tradeoffs, semantic-part choices), and a preference model fitted to the data reranks models differently than benchmarks; metric-aligned preferences falsify it.
- Why Important: If metrics and users disagree, model selection by benchmark actively picks outputs users like less — a product-level correction.
- Why Possibly Novel: Large-scale preference elicitation for segmentation quality with divergence-regime analysis (measurement study, not a training method).
- Minimal Experiment: Collect pairwise human preferences over model outputs across regimes; fit preference predictors; quantify metric-preference divergence and reranking effects.
- Main Risk: Preference depends on use case; elicit under several stated task contexts.
- Research Cluster tag: FM-FAIL

### IDEA-A-0317
- Idea: Degradation-regime crossover: map the image-quality regimes (noise, blur, low light) where small specialist models overtake foundation models, testing the assumption that foundations dominate everywhere.
- Problem: [KNOWN FACT] Foundations excel on clean benchmarks; deployment often lives in degraded regimes where specialists trained in-regime might dominate, but the crossover map does not exist.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For each degradation axis, there is a measurable severity beyond which in-regime specialists beat zero-shot foundations, and the crossover severity is predictable from the foundation's training-data quality statistics; foundation dominance everywhere falsifies it.
- Why Important: A crossover map is direct procurement guidance for degraded-environment deployments (industrial, security, underwater).
- Why Possibly Novel: Systematic specialist-versus-foundation regime mapping with predictive crossover modeling.
- Minimal Experiment: Train in-regime specialists across degradation severities; evaluate against foundations; map crossovers per axis and test predictability.
- Main Risk: Specialist quality depends on effort; use standardized recipes and report tuning budgets.
- Research Cluster tag: FM-FAIL

### IDEA-A-0318
- Idea: Task-dependent granularity collapse: test whether foundation models that distinguish fine-grained categories in classification collapse those distinctions in segmentation outputs — a capability inconsistency across output types.
- Problem: [KNOWN FACT] The same foundation backbone serves classification and dense heads; whether fine-grained distinctions survive into dense outputs (or collapse to coarse categories) is unexamined as a systematic property.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For many fine-grained pairs, models classify correctly while segmenting indistinguishably (identical masks and scores for either prompt), demonstrating output-type-dependent granularity — with the collapse predictable from head training data; consistent granularity falsifies it.
- Why Important: Users assume capability consistency across a model's interfaces; documented inconsistency changes how multi-interface systems should be validated.
- Why Possibly Novel: Cross-interface capability-consistency auditing within single models — a new evaluation dimension.
- Minimal Experiment: Assemble fine-grained pairs; measure classification separability vs dense-output separability per model; characterize the collapse and its predictors.
- Main Risk: Interface implementations differ per model; document interface choices exhaustively.
- Research Cluster tag: FM-FAIL

### IDEA-A-0319
- Idea: Membership leakage through mask quality: test whether per-image segmentation quality gaps expose which images were in a foundation model's training set, quantifying a privacy side channel in dense outputs.
- Problem: [KNOWN FACT] Membership inference is studied for classifiers/generators; dense outputs carry far more bits per image, plausibly leaking membership more strongly, but this channel is unmeasured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Membership inference from dense-output statistics (quality, confidence structure, boundary style) achieves substantially higher attack accuracy than classification-based attacks on the same models — dense outputs are a stronger privacy side channel; no advantage falsifies it.
- Why Important: If dense interfaces leak membership, privacy assessments of vision foundations must include their segmentation endpoints, not just labels.
- Why Possibly Novel: First systematic membership-inference treatment of dense-prediction outputs with channel-capacity comparison.
- Minimal Experiment: Train models with known member/non-member splits; build attacks from dense-output features; compare attack performance against classification-channel baselines.
- Main Risk: Findings could enable misuse; follow responsible-disclosure norms and emphasize defenses.
- Research Cluster tag: FM-FAIL

### IDEA-A-0320
- Idea: Familiarity-calibrated confidence: test whether foundation-model self-confidence tracks the web-frequency of the visual domain rather than actual per-image difficulty — confidence as familiarity, not competence.
- Problem: [KNOWN FACT] Confidence signals guide downstream automation; if they encode domain familiarity instead of instance-level correctness, they mislead exactly in unfamiliar domains where guidance matters most.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Across domains, mean self-confidence correlates with estimated domain web-frequency after controlling for actual accuracy — a familiarity bias in confidence — and per-instance calibration degrades as domain frequency drops; frequency-independent calibration falsifies it.
- Why Important: Familiarity-biased confidence would systematically overstate reliability in the rare domains (medical, industrial) where trust decisions are most consequential.
- Why Possibly Novel: Decomposes confidence into familiarity and competence components with corpus-statistics instrumentation.
- Minimal Experiment: Evaluate confidence/accuracy across domains of varying web presence; regress confidence bias on frequency estimates controlling for accuracy.
- Main Risk: Domain frequency estimation is rough; use several independent frequency proxies.
- Research Cluster tag: FM-FAIL

### IDEA-A-0321
- Idea: Multi-task pretraining interference matrix: measure which auxiliary pretraining tasks help or hurt dense-prediction capability in multi-task foundations, producing an empirical task-compatibility matrix.
- Problem: [KNOWN FACT] Foundation training increasingly mixes tasks; dense-prediction quality may be traded against other capabilities in unmeasured ways, and task-mixture design lacks empirical compatibility guidance.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Specific auxiliary tasks measurably degrade dense capabilities at matched compute (negative task interactions), the interaction matrix is stable across scales tested, and mixture design using the matrix outperforms naive mixing; no stable interactions falsify it.
- Why Important: Task-mixture design is a core decision for every foundation-training effort; an interaction matrix converts it from taste to evidence.
- Why Possibly Novel: Systematic pairwise/mixture interaction quantification focused on dense-task outcomes.
- Minimal Experiment: Train matched-compute models over task-mixture grids at modest scale; measure dense outcomes; fit and validate the interaction matrix on new mixtures.
- Main Risk: Scale-dependence of interactions; verify sign stability at two scales.
- Research Cluster tag: FM-FAIL

### IDEA-A-0322
- Idea: Technical-vocabulary tokenization failure: measure open-vocabulary segmentation degradation on domain-technical lexicons (Latin species names, medical terminology, industrial part codes) and attribute it between tokenization and training exposure.
- Problem: [KNOWN FACT] Scientific and industrial users query with technical vocabularies whose tokenization and corpus statistics differ radically from everyday words; the failure attribution (tokenizer vs exposure) determines the fix.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Controlling for concept visual difficulty, technical-lexicon queries fail primarily through exposure (corpus rarity) rather than tokenization fragmentation — established by alias experiments separating the two — directing remedies toward domain text augmentation; tokenizer-dominant attribution falsifies it (and redirects the remedy).
- Why Important: Technical-vocabulary users are the highest-value professional adopters; the attribution decides between cheap fixes (aliases) and expensive ones (domain pretraining).
- Why Possibly Novel: Clean attribution design using alias substitution and frequency matching jointly (extends IDEA-A-0216 to the attribution question).
- Minimal Experiment: Build technical/colloquial/alias query triads for fixed concepts; measure performance per query form; decompose the deficit.
- Main Risk: Triad construction needs domain experts; scope to two professional domains.
- Research Cluster tag: FM-FAIL

### IDEA-A-0323
- Idea: Context-dose sensitivity: measure how dense-prediction outputs change as progressively more global image context is revealed (crop-to-full-image series), characterizing each model's context dependence curve.
- Problem: [KNOWN FACT] Foundation models integrate global context; whether context helps monotonically or induces instability (mask flips when context changes) is uncharacterized, though tiled/cropped inference is standard practice.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Context-response curves are non-monotone for a substantial fraction of objects (context can flip correct local decisions to incorrect global ones), and the instability is predictable from scene-object consistency statistics; monotone stabilization falsifies it.
- Why Important: Tiling strategies for large images (satellite, pathology) implicitly choose a context dose; response curves would ground that choice in evidence.
- Why Possibly Novel: Context as a continuous dosing variable with per-model response-curve characterization for dense outputs.
- Minimal Experiment: Build concentric crop series around fixed objects; run models per dose; classify response-curve shapes and predictors of non-monotonicity.
- Main Risk: Resolution confounds with context dose; hold target resolution fixed across the series.
- Research Cluster tag: FM-FAIL

### IDEA-A-0324
- Idea: Interactive-loop cost profiling: measure where compute time actually goes in deployed interactive segmentation (encoder vs decoder vs orchestration) across hardware, and quantify the amortization opportunities that latency-oriented papers ignore.
- Problem: [KNOWN FACT] Interactive workflows re-use encoded features across many prompts; published efficiency comparisons use single-pass FLOPs that misrepresent interactive-loop economics.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Under realistic interactive workloads, system-level cost rankings of public models differ substantially from single-pass FLOPs rankings (amortization restructures the comparison), and a workload-parameterized cost model predicts real latencies accurately; FLOPs-consistent rankings falsify it.
- Why Important: Tool builders choose models by misleading metrics; workload-aware cost models would correct procurement and research targets alike.
- Why Possibly Novel: Systems-measurement methodology (workload profiling, amortization accounting) applied to interactive dense prediction.
- Minimal Experiment: Profile public models under scripted interactive workloads on several hardware targets; fit workload-parameterized cost models; compare rankings against FLOPs.
- Main Risk: Implementation quality varies across models; use best-available official implementations and document.
- Research Cluster tag: FM-FAIL

### IDEA-A-0325
- Idea: Failure-taxonomy reproducibility: test whether independent teams analyzing the same foundation model's errors converge on the same failure taxonomy, measuring the objectivity of failure-mode science itself.
- Problem: [KNOWN FACT] Failure-mode papers propose taxonomies built by one team's judgment; if taxonomies are not reproducible across analysts, the field's failure knowledge is analyst-dependent narrative.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Independent expert teams given identical model outputs produce taxonomies with only moderate structural agreement (measurable by category-alignment metrics), but agreement rises substantially under a shared coding protocol — failure science needs methodology, not just effort; high unaided agreement falsifies the need.
- Why Important: The reliability of every failure-analysis paper (including most ideas in this file) rests on unexamined analyst objectivity; measuring it is foundational hygiene.
- Why Possibly Novel: Inter-analyst reliability methodology (from qualitative research) applied to ML failure analysis, with a protocol as the deliverable.
- Minimal Experiment: Recruit 4 independent teams; provide identical error corpora; compare taxonomies with alignment metrics; repeat with a structured coding protocol; measure the improvement.
- Main Risk: Team recruitment; small teams of graduate researchers suffice for the core comparison.
- Research Cluster tag: FM-FAIL

---

## Section 10 — Existing method / evaluation failure (IDEA-A-0326 .. 0350)

### IDEA-A-0326
- Idea: Standardized-budget replication study: re-train recent published segmentation methods under one equalized training protocol and measure how much of each claimed improvement survives.
- Problem: [KNOWN FACT] Published methods differ in training budgets, augmentation, and schedules alongside their claimed contribution; the confounded gains have never been separated at field scale for segmentation.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Under equalized budgets and recipes, a substantial fraction of recent claimed improvements shrink to within noise, and the shrinkage is predictable from how much each paper's recipe deviated from baseline recipes; surviving gains falsify it (and would be reassuring).
- Why Important: The field's perceived progress rate calibrates funding and direction; measuring the recipe-confound correction is basic scientific hygiene.
- Why Possibly Novel: An executed large-scale equalized re-benchmarking for dense prediction with shrinkage attribution, not an opinion piece.
- Minimal Experiment: Select 15 recent methods with public code; re-train all under a fixed protocol on 2 benchmarks; report original-vs-equalized effect sizes.
- Main Risk: Equalized recipes may disadvantage some methods unfairly; consult authors and report per-method caveats.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0327
- Idea: Claimed-delta versus seed-noise survey: systematically compare effect sizes claimed in segmentation papers against empirically measured seed variance for the same configurations.
- Problem: [KNOWN FACT] Many papers report single-run comparisons; without variance context, readers cannot distinguish real effects from run luck (companion measurement to IDEA-A-0222's variance census).
- Core Hypothesis (falsifiable): [HYPOTHESIS] A meaningful fraction of surveyed claimed improvements are smaller than the multi-seed standard deviation of their own experimental configuration — statistically unresolved claims published as findings; predominance of resolved claims falsifies it.
- Why Important: Quantifies the field's false-discovery exposure and motivates variance-reporting standards with hard numbers.
- Why Possibly Novel: Direct claim-by-claim comparison against measured (not assumed) noise for dense-prediction literature.
- Minimal Experiment: Sample recent claims; replicate configurations across seeds; compute the fraction of claims within noise; publish the survey with per-venue statistics.
- Main Risk: Replication fidelity; restrict to papers with complete public code and configs.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0328
- Idea: Factorial ablation validity: test whether one-factor-at-a-time ablations mislead by measuring interaction effects among method components in published segmentation systems.
- Problem: [KNOWN FACT] Papers validate components via individual ablations, implicitly assuming additive contributions; interaction effects could invalidate the attributions, but nobody measures them.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Full-factorial re-ablation of published multi-component methods reveals substantial interactions (components' value depends on other components' presence), overturning a measurable fraction of published component attributions; additive contributions falsify it.
- Why Important: Component attributions guide what the community reuses; interaction-blind ablations may have promoted the wrong pieces.
- Why Possibly Novel: Full-factorial designs (standard in experimental science) applied retroactively to published ablation claims.
- Minimal Experiment: Pick 5 multi-component methods; run full factorials on their components; compare interaction-aware attributions against the published ones.
- Main Risk: Factorial cost grows exponentially; select methods with 3-4 separable components.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0329
- Idea: Test-time augmentation as a hidden confound: audit how inconsistent TTA usage across papers distorts reported comparisons, and quantify TTA-normalized leaderboard changes.
- Problem: [KNOWN FACT] Some reported numbers include multi-scale/flip test-time augmentation while comparisons treat them as equivalent; the aggregate distortion on leaderboards has not been quantified.
- Core Hypothesis (falsifiable): [HYPOTHESIS] TTA-normalized re-evaluation changes a nontrivial fraction of published pairwise orderings and reveals that TTA benefit itself varies by method family — making unnormalized comparison doubly misleading; order-invariance falsifies it.
- Why Important: A zero-cost reporting standard (declare and normalize TTA) could remove a systematic comparison bias — but only demonstrated harm will drive adoption.
- Why Possibly Novel: Field-scale quantification of a known-but-unmeasured comparison inconsistency, with family-dependent TTA-benefit analysis.
- Minimal Experiment: Re-evaluate public checkpoints with and without standardized TTA; recompute leaderboard orderings; report flips and family effects.
- Main Risk: TTA configurations vary; standardize two canonical settings.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0330
- Idea: Baseline archaeology: re-train previous-generation segmentation methods with modern data pipelines and training practices, measuring how much of the "architectural progress" narrative survives.
- Problem: [KNOWN FACT] Old baselines are quoted at their historical scores while new methods enjoy modern training practices; the confound systematically inflates perceived architectural progress.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Previous-generation architectures retrained with modern practices close a large fraction of the gap to current methods on standard benchmarks, showing much recent progress is training practice, not architecture; persistent gaps falsify it.
- Why Important: Correct attribution between architecture and practice determines where future research effort should go.
- Why Possibly Novel: Systematic archaeological re-training for dense prediction with progress-attribution accounting.
- Minimal Experiment: Re-train 5 landmark older methods under current recipes; compare modernized-old versus current methods at matched budgets.
- Main Risk: Modernization choices are debatable; define a fixed modernization checklist and apply it uniformly.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0331
- Idea: Improvement portability index: measure how reliably method improvements demonstrated on one benchmark transfer to other datasets, and publish per-method-family portability statistics.
- Problem: [KNOWN FACT] Methods are validated on 1-2 benchmarks and adopted broadly; the transfer reliability of improvements (as opposed to models) is not systematically tracked.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Improvement portability varies drastically by method family (data-centric changes port broadly; benchmark-tuned architectural changes port poorly), and a portability index computed from multi-benchmark evaluation predicts real adoption success; uniform portability falsifies it.
- Why Important: Practitioners need to know which published gains will survive contact with their data — a portability index answers the question they actually have.
- Why Possibly Novel: Treats the improvement (delta), not the model, as the unit of portability measurement across benchmark suites.
- Minimal Experiment: Apply 20 published improvements across 5 benchmarks under fixed recipes; compute per-improvement portability distributions; analyze family patterns.
- Main Risk: Improvement isolation requires careful reimplementation; use author code where available.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0332
- Idea: Significance-testing retrofit: apply paired per-image statistical tests to published segmentation comparisons and report what fraction of claimed superiority survives at standard significance levels.
- Problem: [KNOWN FACT] Dense-prediction papers rarely report statistical tests despite paired per-image data being ideally suited to them; the community lacks a measured survival rate of claims under testing.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A meaningful fraction of published pairwise superiority claims fail paired significance tests on their own evaluation data, and failure probability is predictable from margin size and test-set size; near-universal survival falsifies it.
- Why Important: A survival-rate number would do more for statistical-practice adoption than any methodological exhortation.
- Why Possibly Novel: A field-scale retrofit audit with public per-comparison verdicts, plus power guidance for future papers.
- Minimal Experiment: Recompute per-image paired metrics for many public model pairs; run appropriate tests; publish survival statistics and a testing toolkit.
- Main Risk: Per-image score correlation structure; use tests robust to clustering.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0333
- Idea: Search-budget disclosure effects: measure the correlation between hyperparameter search budgets (where reconstructable) and claimed improvement sizes, estimating how much "method quality" is actually search intensity.
- Problem: [KNOWN FACT] Papers rarely disclose tuning budgets; if claimed gains correlate with search intensity, comparisons reward compute-rich labs' tuning rather than ideas.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Among methods with reconstructable budgets, claimed improvement size correlates substantially with search budget, and budget-matched re-tuning of baselines eliminates a measurable share of claimed gains; no correlation falsifies it.
- Why Important: Would justify budget-disclosure requirements and budget-matched comparison norms with empirical evidence.
- Why Possibly Novel: Budget-effect quantification via both observational correlation and interventional budget-matched re-tuning.
- Minimal Experiment: Reconstruct budgets from papers/repos where possible; correlate with gains; select cases for budget-matched baseline re-tuning; report the eliminated share.
- Main Risk: Budget reconstruction is lossy; treat observational findings as motivation for the interventional arm.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0334
- Idea: Qualitative-figure bias audit: measure the gap between the quality of examples shown in papers' qualitative figures and the true quality distribution of the same models on the same datasets.
- Problem: [KNOWN FACT] Qualitative figures are chosen by authors with an incentive to impress; the systematic size of the resulting impression gap has never been measured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Figure-shown examples score in the top quantiles of their models' quality distribution far more often than random selection would produce (quantifiable cherry-pick index), and the index varies by venue and year; random-consistent selection falsifies it.
- Why Important: Qualitative impressions shape adoption; a measured cherry-pick index would justify random-sample figure requirements at venues.
- Why Possibly Novel: Forensic quantification of presentation bias with a reproducible index and venue-level statistics.
- Minimal Experiment: For papers with public code, locate figure examples in the test set; compute quality quantiles of shown vs random examples; publish the index distribution.
- Main Risk: Figure-example identification effort; automate matching with image retrieval.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0335
- Idea: Error-profile equivalence testing: measure whether methods with indistinguishable aggregate scores differ meaningfully in error-type composition, making error-profile reporting informative where leaderboards are saturated.
- Problem: [KNOWN FACT] On mature benchmarks, top methods cluster within tiny aggregate margins; whether they are behaviorally interchangeable or differ in error structure is unknown to users who must choose among them.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Aggregate-equivalent methods differ substantially and stably in error-type decomposition (boundary vs classification vs presence errors), so profile-based selection outperforms score-based selection for specific deployments; profile equivalence falsifies it.
- Why Important: Gives practitioners a decision procedure for the common case where leaderboards cannot distinguish candidates.
- Why Possibly Novel: Error-decomposition equivalence analysis as a model-selection methodology with deployment-matched validation.
- Minimal Experiment: Decompose errors for aggregate-tied model groups; test profile stability across datasets; validate profile-matched selection on deployment-mimicking tasks.
- Main Risk: Decomposition scheme choices; use two published decomposition frameworks and report agreement.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0336
- Idea: Oracle-bounded prioritization: run oracle experiments that upper-bound the achievable gain from perfecting each component of segmentation pipelines (proposals, boundaries, classification, post-processing), publishing a where-to-work map.
- Problem: [KNOWN FACT] Research effort allocates by fashion; oracle substitution (replace a component with ground truth) bounds each component's available headroom, but no systematic cross-component map exists for modern pipelines.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Component headrooms are highly unequal and dataset-dependent (e.g., presence/detection headroom dominating boundary headroom on some benchmarks), contradicting current effort allocation measurably; equal headrooms falsify it.
- Why Important: A headroom map is the most direct possible evidence for redirecting community effort to where gains exist.
- Why Possibly Novel: Comprehensive oracle-bounding across components, models, and benchmarks as a standing public resource.
- Minimal Experiment: Implement oracle substitutions per component for several pipelines/benchmarks; compute headroom tables; compare against a survey of recent-paper effort distribution.
- Main Risk: Oracle definitions embed assumptions; document substitution semantics precisely.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0337
- Idea: Simulated-versus-real-user evaluation gap in interactive segmentation: quantify how method rankings change when evaluated with real users instead of scripted interaction simulators.
- Problem: [KNOWN FACT] Interactive methods are ranked by simulator-driven protocols (cf. IDEA-A-0188's behavioral comparison); whether the rankings themselves survive real-user evaluation is the decision-relevant unknown.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Real-user evaluation reorders simulator-based method rankings substantially (methods optimized for simulator quirks lose), and the reordering is predictable from each method's sensitivity to click-placement statistics; preserved rankings falsify it.
- Why Important: If rankings flip under real users, the interactive-segmentation subfield has been optimizing the wrong objective for years.
- Why Possibly Novel: Full ranking-level human evaluation of interactive methods with mechanism analysis of the flips.
- Minimal Experiment: Run a within-subjects user study across 6 interactive methods on matched tasks; compare user-derived rankings with simulator rankings; analyze flip mechanisms.
- Main Risk: User-study scale; power analysis first, focus on top-ranked method pairs.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0338
- Idea: Efficiency-claim reality check: measure the correlation between reported theoretical efficiency metrics (FLOPs, parameter counts) and actual latency/energy on deployment hardware for segmentation models.
- Problem: [KNOWN FACT] Papers claim efficiency via FLOPs while deployment cares about latency/energy on specific hardware; the correlation's strength across modern architectures is assumed rather than measured.
- Core Hypothesis (falsifiable): [HYPOTHESIS] FLOPs-latency correlation is weak across modern segmentation architectures (memory patterns and operator support dominate), such that FLOPs-based efficiency rankings mispredict hardware rankings for a large fraction of model pairs; strong correlation falsifies it.
- Why Important: Efficiency claims drive edge-deployment choices; if the proxy fails, the field needs hardware-grounded reporting norms.
- Why Possibly Novel: Comprehensive proxy-validity measurement across architectures and hardware targets with mispairing statistics.
- Minimal Experiment: Benchmark many public models on several hardware targets; correlate theoretical metrics with measured latency/energy; report ranking-disagreement rates.
- Main Risk: Implementation-optimization confounds; use consistent runtimes and report optimization levels.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0339
- Idea: Pseudo-labeling self-confirmation audit: test whether semi-supervised segmentation gains are partially evaluation artifacts arising when test distributions resemble the pseudo-labeled pool the method adapted to.
- Problem: [KNOWN FACT] Semi-supervised methods leverage unlabeled pools often drawn from the same distribution as the test set; gains may partly reflect distribution-matching rather than better learning, a confound standard protocols cannot see.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Semi-supervised gains shrink measurably when evaluated on test data distributionally independent from the unlabeled pool, and the shrinkage grows with pool-test similarity — quantifying the self-confirmation component; pool-independent gains falsify it.
- Why Important: Semi-supervised learning's practical value proposition depends on gains that survive distribution independence — the deployment reality.
- Why Possibly Novel: A designed pool-test-similarity manipulation isolating the self-confirmation component of semi-supervised gains.
- Minimal Experiment: Train semi-supervised methods with pools of varied similarity to multiple test sets; regress gains on pool-test similarity; report the artifact share.
- Main Risk: Similarity manipulation may change pool usefulness; control pool size and quality across conditions.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0340
- Idea: Ensemble-gap diagnostics: use the gap between a model ensemble and its best member as a standing diagnostic of how much accessible headroom current single-model methods leave unexploited per benchmark.
- Problem: [KNOWN FACT] Ensembles reliably beat single models; the size and composition of the gap (diversity structure) quantifies unexploited headroom, but it is not tracked as a benchmark statistic.
- Core Hypothesis (falsifiable): [HYPOTHESIS] The ensemble gap is large and stable on mature benchmarks and its error-type composition identifies specific headroom (e.g., presence errors dominate the gap), predicting which method innovations will succeed next; a negligible gap falsifies remaining-headroom claims.
- Why Important: A public ensemble-gap tracker would tell the field how much single-model headroom exists and where — cheap, continuously updateable strategic intelligence.
- Why Possibly Novel: Ensemble analysis reframed as benchmark-health metrology with predictive validation against subsequent method progress.
- Minimal Experiment: Build ensembles from public checkpoints per benchmark; decompose gap composition; retrospectively test whether past gap composition predicted which later methods succeeded.
- Main Risk: Ensemble construction choices; standardize on simple output-level combination for comparability.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0341
- Idea: Per-class variance transparency: demonstrate that many published aggregate-metric movements are driven by 2-3 classes, and establish class-attribution reporting as verifiable practice.
- Problem: [KNOWN FACT] Mean-over-classes metrics can move because of a few classes while readers assume broad improvement; class-level attribution of published deltas is rarely available.
- Core Hypothesis (falsifiable): [HYPOTHESIS] For a large fraction of recent published improvements, the top 3 contributing classes account for the majority of the aggregate delta, and the contributing classes are often rare classes with high estimate variance — improvements are narrower and noisier than they appear; broad-based deltas falsify it.
- Why Important: Changes how readers should interpret every mean-metric claim, and provides the tooling to check.
- Why Possibly Novel: Systematic delta-decomposition audit across the recent literature with a reusable attribution toolkit.
- Minimal Experiment: Recompute per-class deltas for many public method pairs; measure contribution concentration; cross-reference with per-class estimate variance.
- Main Risk: Public per-class outputs are scarce; re-run released checkpoints where needed.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0342
- Idea: Dual-metric reporting effects: measure how requiring boundary metrics alongside region metrics would have changed the last several years of segmentation method rankings.
- Problem: [KNOWN FACT] Region-overlap metrics saturate while boundary quality often does not; the field's single-metric habit may have systematically promoted region-optimizing methods over boundary-improving ones.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Retrospective dual-metric re-ranking flips a substantial fraction of published method orderings and reveals boundary-quality stagnation periods invisible in region metrics; concordant rankings falsify it.
- Why Important: If flips are common, metric-reporting policy directly shaped which research directions won — evidence for venue-level dual-metric requirements.
- Why Possibly Novel: Retrospective policy counterfactual (what if boundary metrics had been required?) executed with real re-evaluation at scale.
- Minimal Experiment: Re-evaluate historical public checkpoints under region and boundary metrics; construct dual-metric rankings; report flip statistics and stagnation analysis.
- Main Risk: Boundary metrics inherit GT polygon limits (cf. IDEA-A-0276); apply ceiling-aware scoring.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0343
- Idea: Leaderboard rank-churn analysis: measure how stable top-method rankings are under small legitimate evaluation perturbations (test subset resampling, metric parameter jitter, preprocessing variants).
- Problem: [KNOWN FACT] Leaderboard positions drive citation and adoption; their robustness to defensible evaluation-pipeline perturbations is unmeasured, so users cannot distinguish solid rankings from coin flips.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Under a battery of legitimate perturbations, top-5 orderings on mature benchmarks churn substantially (rank instability comparable to random tie-breaking among neighbors), while a minority of gaps are perturbation-proof — separable and reportable; universal stability falsifies it.
- Why Important: A per-leaderboard stability report tells the community which rankings mean something — consumer protection for benchmark users.
- Why Possibly Novel: Perturbation-battery methodology for ranking robustness, delivered as a standing per-benchmark stability index.
- Minimal Experiment: Define the perturbation battery; recompute rankings for public leaderboards under each; publish churn statistics and stable-gap identification.
- Main Risk: Perturbation legitimacy is contestable; publish the battery definition for community review first.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0344
- Idea: Preregistered negative-results replication of segmentation folklore: select widely believed but weakly evidenced practice claims ("trick X helps") and run preregistered replications to publish which fail.
- Problem: [KNOWN FACT] Practice folklore spreads through papers' passing remarks and repository defaults; negative results about these claims are structurally unpublishable, leaving folklore uncorrected.
- Core Hypothesis (falsifiable): [HYPOTHESIS] A meaningful fraction of surveyed folklore claims fail preregistered replication under fair conditions (no measurable benefit or context-inverted effects), and failed claims correlate with weak original evidence; universal replication falsifies it.
- Why Important: Folklore consumes implementation effort field-wide; a replication registry converts hearsay into checked knowledge.
- Why Possibly Novel: Preregistration methodology imported wholesale into vision-practice claims with a public registry as the artifact.
- Minimal Experiment: Survey and rank folklore claims by prevalence; preregister replication protocols for the top 10; execute and publish all outcomes regardless of direction.
- Main Risk: Claim selection bias; use community submission and voting for the claim list.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0345
- Idea: Uncertainty-metric validity for segmentation: test whether the calibration metrics commonly used to validate segmentation uncertainty actually predict downstream decision quality, against proper scoring alternatives.
- Problem: [KNOWN FACT] Segmentation-uncertainty papers validate with aggregate calibration metrics whose connection to downstream decisions (triage, abstention, review routing) is assumed; if the metrics don't predict decision utility, the subfield optimizes a proxy.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Common calibration metrics rank uncertainty methods differently than decision-utility evaluation does (measurable rank divergence), while proper scoring rules align better — the field is using the wrong yardstick; concordant rankings falsify it.
- Why Important: Uncertainty research feeds safety systems; a yardstick error there propagates into every safety case built on it.
- Why Possibly Novel: Decision-theoretic meta-evaluation of uncertainty metrics for dense prediction with realistic decision tasks.
- Minimal Experiment: Evaluate many uncertainty methods under calibration metrics, proper scoring rules, and simulated decision tasks; compare method rankings across yardsticks.
- Main Risk: Decision-task design choices; use several distinct realistic decision settings.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0346
- Idea: Paper-code divergence census: measure how often public implementations differ materially from their papers' descriptions (undocumented tricks, changed hyperparameters) and how much of reported performance depends on the undocumented parts.
- Problem: [KNOWN FACT] Reproduction attempts routinely discover paper-code mismatches; the field lacks prevalence statistics and effect sizes for the undocumented components.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Material divergences are common in a systematic audit, and ablating undocumented components measurably reduces performance in a substantial fraction of cases — undocumented engineering carries real load; rare or inert divergences falsify it.
- Why Important: If undocumented parts carry load, "the method" as described is not what produces the results — a fundamental reporting-integrity measurement.
- Why Possibly Novel: Systematic divergence forensics with load-bearing quantification, beyond anecdotal reproduction complaints.
- Minimal Experiment: Audit 30 paper-code pairs with a structured divergence protocol; ablate discovered undocumented components; report prevalence and load statistics.
- Main Risk: Divergence judgment subjectivity; use dual independent auditors with adjudication.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0347
- Idea: Augmentation-attribution audit: measure how much of recent methods' claimed gains disappear when their (often changed) data-augmentation policies are transplanted to baselines.
- Problem: [KNOWN FACT] Method papers frequently change augmentation alongside their core contribution; augmentation transplant to baselines is the obvious control that papers rarely run.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Transplanting the proposed methods' augmentation policies onto plain baselines recovers a substantial fraction of the claimed gaps in many cases — augmentation is a hidden driver misattributed to method innovations; negligible recovery falsifies it.
- Why Important: Correct attribution between augmentation and method determines what knowledge the field actually gained from recent literature.
- Why Possibly Novel: Systematic augmentation-transplant controls executed retroactively across many published claims.
- Minimal Experiment: Identify recent methods with changed augmentation; re-train baselines under transplanted policies; report recovered-gap fractions.
- Main Risk: Augmentation extraction from code is error-prone; verify with authors where possible.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0348
- Idea: Adversarial metric analysis for Dice-family metrics: characterize the degenerate strategies (small-object omission, conservative boundaries, empty-case handling) that inflate common segmentation metrics without improving usefulness.
- Problem: [KNOWN FACT] Any metric admits gaming strategies; the specific exploitable behaviors of segmentation metrics — and whether published models already exhibit them — have not been cataloged rigorously.
- Core Hypothesis (falsifiable): [HYPOTHESIS] Constructed degenerate strategies achieve measurable metric inflation without utility gains, and signature analysis detects the same strategies (evolved, not designed) in some published models — optimization found the metric exploits; no exploitation signatures falsify it.
- Why Important: Metric exploits found by optimization are invisible progress-fakers; a catalog plus detectors protects benchmark integrity.
- Why Possibly Novel: Adversarial analysis of evaluation metrics with detection of naturally evolved gaming in real model populations.
- Minimal Experiment: Construct explicit metric-gaming strategies; quantify their inflation; build behavioral signatures; scan public model zoos for the signatures.
- Main Risk: Distinguishing gaming from legitimate adaptation; anchor with human-utility judgments on flagged behaviors.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0349
- Idea: Compute-normalized comparison standard: measure how method rankings change when comparisons are normalized to equal total compute (training plus search), and validate a practical compute-reporting protocol.
- Problem: [KNOWN FACT] Methods are compared at unequal and undisclosed compute; compute-normalized rankings could differ, but the size of the distortion for dense prediction is unmeasured (integrating the budget concerns of IDEA-A-0333 at the comparison level).
- Core Hypothesis (falsifiable): [HYPOTHESIS] At equalized total compute, a substantial fraction of published rankings invert (methods trading compute for claimed quality), and a simple compute-reporting protocol captures enough information to enable fair normalization; rank stability falsifies it.
- Why Important: Compute-fairness determines whether the field rewards ideas or budgets; the distortion measurement makes the case for reporting standards.
- Why Possibly Novel: Executed compute-normalized re-ranking with a tested reporting protocol, not just a position statement.
- Minimal Experiment: Re-train method pairs at equalized compute envelopes on 2 benchmarks; report inversion rates; pilot the reporting protocol on new submissions.
- Main Risk: Compute equalization has design freedom; publish the envelope definitions for critique.
- Research Cluster tag: METHOD-FAIL

### IDEA-A-0350
- Idea: Failure-reporting adoption experiment: test whether structured failure documentation ("failure cards" accompanying model releases) measurably changes downstream practitioner decisions compared to standard reporting.
- Problem: [KNOWN FACT] Failure modes are documented ad hoc if at all; whether structured failure reporting would actually change practitioner behavior (model choice, deployment safeguards) is an untested assumption behind all reporting-standard advocacy.
- Core Hypothesis (falsifiable): [HYPOTHESIS] In a controlled study, practitioners given failure cards make measurably different and better-calibrated deployment decisions (appropriate safeguard selection, correct model-task matching) than those given standard reports; no behavioral difference falsifies the advocacy premise.
- Why Important: Reporting standards cost effort; evidence that they change decisions (or don't) should precede institutionalization.
- Why Possibly Novel: Experimental evaluation of a documentation intervention on real decision behavior — meta-research with direct policy consequence.
- Minimal Experiment: Prepare matched model documentation with/without failure cards; run a decision-task study with practitioners; measure decision quality and calibration differences.
- Main Risk: Lab decisions may not mirror organizational ones; recruit practicing engineers and use realistic scenarios.
- Research Cluster tag: METHOD-FAIL

---

# Appendix A — 20 Mutations of the Most Surprising Ideas (MUT-01 .. MUT-20)

Each mutation names its parent idea and changes exactly one load-bearing element (inversion, transplantation to a new regime, extremization, or reversal of the causal arrow). Mutations inherit the parent's constraints (no forbidden patterns, no invented citations).

### MUT-01 (parent: IDEA-A-0015, SAM2 memory poisoning)
- Mutation: Invert the harm into a tool — deliberately inject crafted frames to *erase* a designated object from SAM2's memory, for privacy redaction in video streams.
- Rationale: If memory corruption propagates (parent hypothesis), controlled corruption is a mechanism for targeted forgetting; measuring erasure reliability and collateral damage tests the same dynamics from the constructive side.

### MUT-02 (parent: IDEA-A-0082, smoke as alpha regression)
- Mutation: Apply the intermediate-alpha error-concentration analysis to *hair and fur matting* datasets to test whether the "binary masks fail exactly at soft alpha" law is universal across all soft-boundary object families, not smoke-specific.
- Rationale: A cross-family law would elevate a smoke observation into a general principle about binary-mask task formulations.

### MUT-03 (parent: IDEA-A-0093, fractal boundary metric breakdown)
- Mutation: Reverse the direction — use measured metric instability across evaluation resolutions as an *estimator of boundary fractal dimension*, turning a metrology defect into a shape-analysis instrument.
- Rationale: If instability is systematically fractal-driven (parent hypothesis), the mapping is invertible and freely computable from existing evaluations.

### MUT-04 (parent: IDEA-A-0201, prompt-response fingerprinting)
- Mutation: Extremize to adversarial conditions — test whether fingerprinting survives *deliberate evasion* (output perturbation, ensembling, distillation) by an API provider trying to hide its model identity.
- Rationale: Forensics claims are only as strong as their adversarial robustness; the evasion arms race is the real deployment condition for the parent idea.

### MUT-05 (parent: IDEA-A-0227, promptability dies first)
- Mutation: Invert the training direction — fine-tune *only on prompt-following data* (no new domain content) and measure whether target-domain accuracy degrades symmetrically, mapping the reverse exchange rate.
- Rationale: If interactivity and accuracy trade against each other bidirectionally, the parent finding reflects a capacity conflict, not a data artifact — a decisive mechanistic distinction.

### MUT-06 (parent: IDEA-A-0035, granularity-prior leakage)
- Mutation: Transplant from measurement to intervention — construct a small *granularity-counterbalanced* fine-tuning set and test whether a brief exposure resets the granularity prior without harming other capabilities.
- Rationale: If the prior is shallow (resettable cheaply), it is a calibration artifact; if deep, it is structural — the intervention discriminates the two.

### MUT-07 (parent: IDEA-A-0040, prompt-ensemble variance as quality estimate)
- Mutation: Extremize the blind spot — mine specifically for *consistent-but-wrong* regions (low variance, high error) across datasets and characterize what unites them, making the estimator's failure mode the object of study.
- Rationale: The parent idea's main risk is exactly this blind spot; studying it directly converts a caveat into a research result about confidently shared model biases.

### MUT-08 (parent: IDEA-A-0119, human prompt intent for smoke)
- Mutation: Transplant the intent-ambiguity methodology to *medical lesions with satellite foci* — when a clinician clicks a lesion, do they mean this focus, the lesion complex, or all disease tissue?
- Rationale: The click-referent ambiguity structure may be identical across amorphous phenomena and multifocal pathology; testing transfer probes whether prompt-intent science generalizes.

### MUT-09 (parent: IDEA-A-0282, annotation-tool style imprinting)
- Mutation: Reverse the causal arrow — train models *deliberately on mixed-tool data with tool labels* and test whether tool-conditioning lets one model reproduce any requested annotation style on demand.
- Rationale: If tool style is learnable enough to imprint accidentally (parent), it should be controllable explicitly — turning a contamination finding into a style-controllable annotation capability.

### MUT-10 (parent: IDEA-A-0295/0307, benchmark membership testing via mask idiosyncrasies)
- Mutation: Invert the defense — design benchmark ground truth containing *deliberate cryptographic idiosyncrasies* (imperceptible annotation watermarks) so future contamination becomes provable by construction.
- Rationale: If idiosyncrasy reproduction detects contamination (parent), planted idiosyncrasies give benchmarks a built-in audit mechanism — proactive rather than forensic.

### MUT-11 (parent: IDEA-A-0300, abstention absence)
- Mutation: Extremize the task — build an evaluation where *most* inputs deserve abstention (95% target-absent) and measure whether any training-free wrapper achieves usable operating points under this deployment-realistic prior.
- Rationale: Abstention capability measured at balanced priors understates the deployment problem; the extreme-prior version is the version monitoring systems actually face.

### MUT-12 (parent: IDEA-A-0244, self-training drift)
- Mutation: Transplant the drift-dynamics instrumentation to *interactive annotation pipelines* where model-assisted pre-segmentation shapes human corrections — measuring human-machine co-drift instead of machine-only drift.
- Rationale: The same confirmation-bias loop plausibly operates through human annotators accepting model suggestions; co-drift would corrupt dataset ground truth, a higher-stakes version of the parent.

### MUT-13 (parent: IDEA-A-0068, consensus fusion creates nonexistent style)
- Mutation: Invert the fusion decision — train on a *single randomly selected rater per image* (preserving natural style diversity) and test whether the resulting model matches individual clinicians better without losing accuracy.
- Rationale: If committee style is an artifact (parent), style-preserving training is the constructive counterpart, testable with identical data.

### MUT-14 (parent: IDEA-A-0089, depth-sensor invalid pixels as glass signal)
- Mutation: Generalize to a *sensor-failure atlas* — catalog the informative failure patterns of every common sensor (ToF, stereo, lidar, radar) as zero-cost material-property signals, with glass as one row of the matrix.
- Rationale: If one sensor's failure is signal (parent), the ensemble of heterogeneous sensor failures may constitute a passive material classifier nobody has assembled.

### MUT-15 (parent: IDEA-A-0203, in-image text hijacks prompts)
- Mutation: Extremize to the defense side — measure whether *text-region masking as preprocessing* eliminates the hijack without degrading legitimate segmentation of text-bearing objects (signs users actually want segmented).
- Rationale: The parent establishes the attack; the mutation quantifies the defense's collateral cost — the number a deployer actually needs.

### MUT-16 (parent: IDEA-A-0148, latency-induced event misses)
- Mutation: Reverse the optimization target — given the parent's event-speed damage model, derive and test *content-adaptive frame-skipping policies* that spend compute on frames where fast events are likely, at fixed total budget.
- Rationale: A validated damage model implies an optimal compute-allocation policy; testing the policy validates the damage model's practical sufficiency.

### MUT-17 (parent: IDEA-A-0281, leaderboard adaptive overfitting)
- Mutation: Transplant to the model-selection layer inside single projects — measure how much *internal validation-set reuse* across a project's many decisions inflates final reported numbers, using held-back fresh splits.
- Rationale: The community-level adaptivity problem (parent) recurs at project scale where every lab lives; the measured inflation rate there is arguably more actionable.

### MUT-18 (parent: IDEA-A-0107, single-view smoke ambiguity)
- Mutation: Invert into an active-sensing criterion — use the measured ambiguity structure to compute *where a second camera should be placed* to maximally disambiguate smoke density, validating information-driven sensor placement.
- Rationale: An ambiguity proof (parent) implicitly defines the geometry of its own resolution; testing placement rules converts a negative result into deployment guidance.

### MUT-19 (parent: IDEA-A-0323, context-dose non-monotonicity)
- Mutation: Extremize to *adversarial context* — search for minimal distant-context edits (outside the object's neighborhood) that flip a correct local segmentation, bounding how non-local dense-model decisions are.
- Rationale: If context effects are non-monotone (parent), worst-case context sensitivity is the safety-relevant quantity, and its spatial reach is unknown.

### MUT-20 (parent: IDEA-A-0056, Dice-vs-clinical-decision inversions)
- Mutation: Transplant the decision-inversion methodology to *autonomous-driving perception* — measure how often better-mIoU segmentation models produce worse downstream planning decisions in matched scenarios.
- Rationale: The metric-decision mismatch is domain-general in principle; driving provides a second high-stakes domain with simulable decision layers to test the generality.

# Appendix B — 10 Assumption-Challenging Ideas (ASSUME-01 .. ASSUME-10)

These challenge assumptions so basic they are rarely stated. Each is falsifiable and carries the same epistemic discipline as the main list.

### ASSUME-01 — Binary masks are the wrong output type for a large fraction of the visual world.
- Challenged assumption: Segmentation = per-pixel set membership.
- Claim to test: [HYPOTHESIS] For a measurable fraction of common scene content (soft shadows, hair, smoke, translucency, defocus), human annotators cannot produce test-retest-consistent binary masks, but can produce consistent graded maps — the binary formulation, not model capability, is the accuracy ceiling there.
- Minimal test: Test-retest human annotation under binary vs graded protocols across content families; map where binary consistency collapses (integrates IDEA-A-0081/0096/0114 into one task-validity atlas).
- If true: Benchmarks need output-type stratification; a chunk of "model failure" literature is re-scoped as task-formulation failure.

### ASSUME-02 — Ground truth does not exist; only annotation distributions do.
- Challenged assumption: Each image has a true mask that evaluation approximates.
- Claim to test: [HYPOTHESIS] Model comparisons that treat the annotation as a sample from a rater distribution (scoring against the distribution, not a point) reorder published rankings materially on ambiguity-rich benchmarks.
- Minimal test: Build rater-distribution references on multi-annotator subsets; re-score public models distributionally; measure rank divergence from point-GT scoring.
- If true: Single-annotation benchmarks are systematically misranking methods on all ambiguous content.

### ASSUME-03 — "Domain shift" is mostly preprocessing shift in disguise.
- Challenged assumption: Cross-site performance drops reflect deep distributional differences requiring learned adaptation.
- Claim to test: [HYPOTHESIS] For a substantial fraction of documented cross-site vision failures, exhaustive low-level pipeline harmonization (resize kernels, compression, ISP, windowing — cf. IDEA-A-0045/0163/0164/0178) removes most of the drop without touching the model.
- Minimal test: Take documented shift cases; apply aggressive pipeline forensics and harmonization; measure the residual "true" domain gap.
- If true: A large share of the adaptation literature addresses a problem that configuration management solves cheaper.

### ASSUME-04 — Prompts are measurement instruments, not user interface conveniences.
- Challenged assumption: The prompt is just how users express intent; the science lives in the model.
- Claim to test: [HYPOTHESIS] Standardized prompt batteries characterize model internals (biases, training data, failure modes, identity — cf. IDEA-A-0201/0210) with enough fidelity that prompt-response analysis becomes a primary scientific method, replacing weight access for black-box model science.
- Minimal test: Demonstrate that prompt-battery signatures predict held-out behavioral properties (robustness profiles, granularity priors) better than architecture metadata does.
- If true: Model auditing and comparison can be done rigorously through interfaces alone — regulatory and scientific consequences.

### ASSUME-05 — Fine-tuning should be treated as damage by default, requiring a safety case, not as the default adaptation move.
- Challenged assumption: Fine-tuning is the standard, presumptively beneficial way to specialize a foundation model.
- Claim to test: [HYPOTHESIS] Accounting for all capability dimensions (retention, calibration, robustness, promptability — cf. Section 7), the expected total-utility delta of standard fine-tuning is negative in a substantial fraction of real specialization scenarios relative to prompt-policy and pipeline-level alternatives.
- Minimal test: Full-cost accounting across specialization scenarios comparing fine-tuning against no-training alternatives at matched target performance.
- If true: The default adaptation workflow of the entire applied community inverts: justify fine-tuning, don't presume it.

### ASSUME-06 — Evaluation sets should be dynamic organisms, not frozen artifacts.
- Challenged assumption: A benchmark must be fixed to enable comparison over time.
- Claim to test: [HYPOTHESIS] A continuously refreshed test stream (with statistical continuity corrections) yields method rankings that predict deployment success better than frozen benchmarks, while resisting the adaptive overfitting and aging failures documented in IDEA-A-0265/0281.
- Minimal test: Run a refreshed-stream evaluation in parallel with frozen benchmarks for a year; compare which better predicts held-out deployment-like outcomes.
- If true: The benchmark institution itself — not any particular dataset — is the field's measurement bottleneck.

### ASSUME-07 — The unit of segmentation research should be the human-model system, not the model.
- Challenged assumption: Model-only metrics are the primary scientific object; humans are downstream consumers.
- Claim to test: [HYPOTHESIS] For interactive and assisted workflows (the dominant real use of segmentation), system-level outcomes (human+model time, error, trust calibration — cf. IDEA-A-0120/0188/0213/0337) are so weakly predicted by model-only metrics that model-level leaderboards are uninformative for the technology's actual value.
- Minimal test: Measure correlation between model-only metrics and human-in-loop outcomes across many models and tasks; report the predictive ceiling.
- If true: The field's evaluation apparatus measures the wrong system.

### ASSUME-08 — Detection boxes are a historical accident that the field should sunset.
- Challenged assumption: Axis-aligned rectangles are an acceptable universal object representation.
- Claim to test: [HYPOTHESIS] The convention-imposed error floors (cf. IDEA-A-0144/0147) plus downstream decision distortions of box representations exceed, for a majority of modern applications, the cost of switching to mask-native or point-set-native interfaces that current models can already produce.
- Minimal test: Cost-accounting study across application families comparing box-native vs mask-native pipelines end to end.
- If true: Detection as a task definition (not any detector) is deprecated for most new systems.

### ASSUME-09 — Models should be required to output "I cannot know this from this image" as a first-class answer.
- Challenged assumption: Every pixel deserves a label; abstention is an add-on.
- Claim to test: [HYPOTHESIS] A substantial measurable fraction of benchmark pixels are information-theoretically undecidable from the single image (proven by human undecidability under forced-choice with unlimited time — occlusion, resolution, ambiguity), and current models answer them confidently at near-random accuracy.
- Minimal test: Build an undecidability-verified pixel subset via human forced-choice experiments; measure model confidence and accuracy exactly there (extends IDEA-A-0300 from objects to pixels).
- If true: Dense prediction needs a third output state, and every current benchmark mis-scores the undecidable regions.

### ASSUME-10 — Data collection, not modeling, is where segmentation research should spend its next decade of marginal effort.
- Challenged assumption: Modeling innovations are the primary driver of remaining progress.
- Claim to test: [HYPOTHESIS] Across current failure clusters (this file's Sections 1–10), oracle-data experiments (perfect targeted data at realistic acquisition cost) close more of each measured gap per unit cost than the best published modeling improvements of the last several years (connects IDEA-A-0336's headroom maps to acquisition economics of IDEA-A-0106/0185).
- Minimal test: For 5 documented failure modes, compare targeted-data interventions against best-known modeling interventions at matched total cost.
- If true: The field's incentive structure (which rewards modeling papers) is misaligned with its own progress function.

---

# Appendix C — Near-Duplicate Notes

Ideas were generated to be distinct, but the following groups share machinery or motivation closely enough that a selection pass should treat them as clusters and pick at most one or two representatives per cluster.

- **Box/prompt jitter dose-response:** IDEA-A-0008 (SAM-specific asymmetry) vs IDEA-A-0193 (cross-family universality). 0193 generalizes 0008; run 0008 first as the pilot.
- **Ensemble/consistency as label-free quality signal:** IDEA-A-0002 (multimask entropy), IDEA-A-0040 (prompt-jitter ensembles), IDEA-A-0142 (flip/translation equivariance), IDEA-A-0190 (text-prompt ensembles), IDEA-A-0309 (cross-foundation disagreement). Same statistical skeleton, different perturbation channel; a unified study could absorb all five.
- **Predicted-IoU head auditing:** IDEA-A-0018 (calibration), IDEA-A-0037 (OOD detection), IDEA-A-0320 (familiarity bias). Three lenses on the same head; 0320 is the most conceptually distinct.
- **Transparent-object background dependence:** IDEA-A-0020 (SAM, physical rig) vs IDEA-A-0087 (cross-model census, same rig). 0087 subsumes 0020's apparatus.
- **Temporal/structural consistency as failure signal:** IDEA-A-0043 (medical z-axis) and IDEA-A-0112 (smoke keyframe interpolation validity) share the "physical smoothness as free supervision" logic in different domains.
- **Capability-resolved forgetting:** IDEA-A-0049 (medical organ fine-tuning), IDEA-A-0226 (capability hierarchy), IDEA-A-0227 (promptability first), IDEA-A-0251 (boundary-vs-region schedules), IDEA-A-0257 (vocabulary retention). 0226 is the umbrella; the others are instantiations worth running only if 0226 confirms ordered forgetting.
- **Leakage/contamination audits:** IDEA-A-0050 (medical patient leakage), IDEA-A-0248 (forgetting-benchmark contamination), IDEA-A-0261 (near-duplicate atlas), IDEA-A-0295 (membership testing), IDEA-A-0307 (mask memorization). 0295 and 0307 are method-and-mechanism of the same investigation; 0261 provides their input lists.
- **Annotation ambiguity as task-validity limit:** IDEA-A-0042/0046 (medical variance bands), IDEA-A-0081 (smoke agreement-vs-opacity), IDEA-A-0096 (spray test-retest), IDEA-A-0113 (boundary-band width recovery), ASSUME-01/02. A single "task-validity atlas" program could unify these.
- **Metric meta-evaluation:** IDEA-A-0099 (fuzzy-boundary metrics vs human judgment), IDEA-A-0316 (human preference vs IoU), IDEA-A-0345 (uncertainty-metric validity). Same human-anchored meta-evaluation design at three targets.
- **Hallucination under absence:** IDEA-A-0125 (OV detection), IDEA-A-0299 (language-prompted segmentation), IDEA-A-0052 (medical empty-input), IDEA-A-0284 (negative-image benchmark retrofit), IDEA-A-0146 (empty-frame prevalence). One absence-benchmark program with per-task tracks.
- **Ranking fragility under evaluation perturbation:** IDEA-A-0122/0131 (detection strata/thresholds), IDEA-A-0269 (bootstrap CIs), IDEA-A-0285 (metric-dataset coupling), IDEA-A-0342 (dual-metric flips), IDEA-A-0343 (rank churn). 0343's perturbation battery is the umbrella instrument.
- **Seed/noise vs claimed effects:** IDEA-A-0222 (variance census) and IDEA-A-0327 (claim survey) are the measurement and the application of the same program; IDEA-A-0332 (significance retrofit) completes the trilogy.
- **Synthetic-shift proxy validity:** IDEA-A-0173 (stylization) and IDEA-A-0180 (corruption suites) test the same proxy-validity question on different proxies; mergeable.
- **Medical repeat-scan reliability:** IDEA-A-0072 (test-retest) and IDEA-A-0079 (longitudinal consistency) differ mainly in time horizon and clinical endpoint; a shared cohort could serve both.
- **Ground-truth geometry artifacts:** IDEA-A-0276 (polygon ceilings), IDEA-A-0277 (corner-cutting bias), IDEA-A-0282 (tool imprinting) form one chain from annotation mechanics to model behavior.
- **Default/prior leakage:** IDEA-A-0035 (SAM granularity prior), IDEA-A-0210 (empty-prompt salience prior), IDEA-A-0268 (dataset granularity fingerprints) share the "training policy becomes model prior" template at different scopes.
- **Compute/efficiency honesty:** IDEA-A-0324 (interactive-loop profiling), IDEA-A-0338 (FLOPs-latency validity), IDEA-A-0349 (compute-normalized rankings) form one systems-metrology cluster.
- **Text-channel lexical effects:** IDEA-A-0216 (tokenizer fragmentation), IDEA-A-0217 (register gap), IDEA-A-0322 (technical vocabularies) overlap; 0322 explicitly extends 0216 and could absorb 0217's battery.
- **Context dependence:** IDEA-A-0127/0128 (detection context transplant/co-occurrence), IDEA-A-0283 (crop context leakage), IDEA-A-0323 (context dosing), MUT-19 (adversarial context) are one mechanism studied at increasing rigor.
- **Prompt-intent and simulator validity:** IDEA-A-0119 (smoke click intent), IDEA-A-0188 (real vs simulated clicks), IDEA-A-0214 (intent-conditioned evaluation), IDEA-A-0337 (real-user rankings) form the human-grounding cluster of prompt science; MUT-08 extends it to medical.

---

## File integrity note

- IDEA count: exactly 350 (IDEA-A-0001 .. IDEA-A-0350, no gaps, no duplicates).
- Mutations: 20 (MUT-01 .. MUT-20). Assumption-challenging ideas: 10 (ASSUME-01 .. ASSUME-10).
- No papers, citations, or experimental numbers were invented anywhere in this file; all factual claims are marked [KNOWN FACT] (uncontroversial background) or [HYPOTHESIS] (to be tested).

