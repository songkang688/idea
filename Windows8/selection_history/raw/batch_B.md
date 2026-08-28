# Windows8 — Stage 1 Raw Idea Batch B

- **Batch:** B (small-object / boundary / uncertainty / long-tail / annotation efficiency / generalization / calibration / robustness / synthetic data / cross-domain / multimodal supervision / representation mismatch / evaluation weakness / phenomena / assumptions / negative results)
- **Generator:** independent Research Idea Generator (batch-B file writer)
- **Date:** 2026-08-28 (UTC)
- **Count:** 350 primary ideas (IDEA-B-0001 .. IDEA-B-0350) + 20 mutations (IDEA-B-M-0001 .. IDEA-B-M-0020) + 10 assumption-challenging ideas (IDEA-B-X-0001 .. IDEA-B-X-0010) + near-duplicate notes.
- **Domain frame:** dense visual prediction (semantic / instance / panoptic segmentation, detection) and its data, evaluation, and deployment ecosystem. Ideas are research-science-shaped: each states a falsifiable hypothesis and a minimal experiment. No module salad, no loss swaps, no backbone swaps as "novelty."
- **Integrity rules honored:** no invented papers, citations, or measured numbers. Where an idea references a known practice or effect, the minimal experiment is designed to (re)measure it rather than assert it.

**Cluster tag legend:** SMALL-OBJ, BOUNDARY, UNCERTAINTY, CALIBRATION, LONG-TAIL, ANNOT-EFF, GENERALIZATION, ROBUSTNESS, SYNTH-DATA, CROSS-DOMAIN, MULTIMODAL-SUP, REP-MISMATCH, EVAL-WEAK, PHENOMENON, ASSUMPTION, NEG-RESULT.

---

## Part 1 — Primary ideas (IDEA-B-0001 .. IDEA-B-0350)

### IDEA-B-0001 — Resolution gains for small objects are partly an NMS artifact
- **One-sentence idea:** Test whether the small-object AP gains from higher inference resolution come from better features or merely from changed duplicate-suppression geometry in NMS.
- **Problem:** Higher input resolution is the default fix for small objects, but it changes both feature quality and the pixel-space behavior of NMS/matching simultaneously, so the community attributes gains to "features" without evidence.
- **Core Hypothesis (falsifiable):** A significant fraction (>30%) of small-object AP gain from 2x resolution persists when features are computed at low resolution and only box post-processing operates in high-resolution coordinates; if the gain vanishes, the feature story wins.
- **Why Important:** Resolution scaling is the single most expensive lever in deployment; knowing which stage actually benefits would let systems pay the cost only where it matters.
- **Why Possibly Novel:** Resolution ablations exist, but a stage-decoupled attribution (features vs. assignment vs. suppression) for the small-object regime has not been the object of a dedicated study.
- **Minimal Experiment:** Train one detector; at test time cross all combinations of {low, high} feature resolution with {low, high} coordinate-space suppression via box rescaling, and report size-stratified AP for each cell of the 2x2.
- **Main Risk:** The decoupling may be leaky (rescaled boxes are not exactly what a high-res model would predict), muddying attribution.
- **Research Cluster:** SMALL-OBJ

### IDEA-B-0002 — Label assignment noise, not feature resolution, bottlenecks small objects
- **One-sentence idea:** Measure how much small-object detection improves when label assignment is replaced by an oracle, holding features fixed.
- **Problem:** IoU-based positive/negative assignment is extremely sensitive to pixel-level jitter for small boxes, so many small objects may get inconsistent or zero positive samples during training.
- **Core Hypothesis (falsifiable):** With oracle assignment (positives chosen using ground-truth correspondence rather than IoU thresholds), small-object AP rises substantially more than large-object AP; if gains are uniform across sizes, assignment is not the size-specific bottleneck.
- **Why Important:** If assignment dominates, the field's focus on higher-resolution features and heavier necks for small objects is misdirected effort.
- **Why Possibly Novel:** Oracle-assignment upper-bound studies exist for detection generally, but a size-stratified accounting that isolates the small-object regime is missing.
- **Minimal Experiment:** Train matched detectors with standard vs. oracle assignment on COCO; report AP_small/AP_medium/AP_large deltas and per-size positive-sample count statistics.
- **Main Risk:** Oracle assignment changes optimization globally, so the size-stratified difference could be confounded by overall convergence changes.
- **Research Cluster:** SMALL-OBJ

### IDEA-B-0003 — Annotation jitter puts a hard ceiling on small-object AP
- **One-sentence idea:** Quantify the AP ceiling imposed by ground-truth box jitter for small objects by high-zoom re-annotation of a benchmark subset.
- **Problem:** A 1–2 px annotation error on a 10 px object is a 20–40% IoU perturbation, so the reported small-object AP of any method is bounded by label noise, yet no benchmark reports this bound.
- **Core Hypothesis (falsifiable):** Independent expert re-annotation of small objects will disagree with existing GT enough that the implied AP@0.5 ceiling for small objects is far below 100 (measurably below current SOTA plus typical claimed gains).
- **Why Important:** If the ceiling is close to current SOTA, incremental small-object papers are fitting noise, and the benchmark needs revision rather than the methods.
- **Why Possibly Novel:** Label-noise audits exist for classification; a jitter-derived AP-ceiling analysis specific to the small-object detection regime is not standard practice.
- **Minimal Experiment:** Re-annotate ~1,000 small instances in COCO/VisDrone at 8x zoom with multiple annotators; compute inter-annotator IoU distribution and the implied evaluation ceiling under standard thresholds.
- **Main Risk:** Re-annotators may share systematic biases with the original annotators, underestimating the true noise.
- **Research Cluster:** SMALL-OBJ

### IDEA-B-0004 — Small-object AP is statistically fragile across seeds and categories
- **One-sentence idea:** Establish the seed- and category-level variance of AP_small on standard benchmarks to test whether typical published gains are significant.
- **Problem:** AP_small is computed over few instances concentrated in a handful of categories, so its variance is likely much higher than headline AP, but papers treat a +0.5 AP_small delta as meaningful.
- **Core Hypothesis (falsifiable):** The across-seed standard deviation of AP_small for a fixed method exceeds the median published AP_small improvement in recent small-object detection papers.
- **Why Important:** A field-wide significance floor would immediately re-sort which small-object contributions are real.
- **Why Possibly Novel:** Seed-variance studies exist for detection overall; nobody has made the size-stratified variance the headline object and connected it to the published-claims distribution.
- **Minimal Experiment:** Train one standard detector 10 times with different seeds; bootstrap test instances; report AP_small confidence intervals and compare against a curated table of claimed deltas (collected, not invented).
- **Main Risk:** Variance is architecture-dependent, so a single-model estimate may not generalize to all published settings.
- **Research Cluster:** SMALL-OBJ / EVAL-WEAK

### IDEA-B-0005 — Pyramid level assignment by scale alone is miscalibrated for small objects
- **One-sentence idea:** Test whether the optimal FPN level for a small object depends on local context density rather than object scale alone.
- **Problem:** FPN-style architectures route objects to levels by size heuristics, assuming scale is the sufficient statistic for where detection is easiest.
- **Core Hypothesis (falsifiable):** For a nontrivial fraction of small objects, an oracle that picks the best pyramid level per instance prefers a different level than the size heuristic, and the preference is predicted by local clutter/context measures.
- **Why Important:** If routing is the problem, gains are available with zero new parameters by changing assignment policy — and many "multi-scale fusion" modules may just be compensating for bad routing.
- **Why Possibly Novel:** Level-assignment studies exist (e.g., learned routing), but a diagnostic that quantifies per-instance level-optimality and identifies its non-scale predictors is missing.
- **Minimal Experiment:** For a trained FPN detector, evaluate each GT small object against every pyramid level's raw predictions; measure how often the best level differs from the assigned one and regress the mismatch on clutter statistics.
- **Main Risk:** Per-level evaluation of a jointly trained model conflates training assignment with inference capability.
- **Research Cluster:** SMALL-OBJ

### IDEA-B-0006 — Anti-aliased downsampling matters more than architecture for small objects
- **One-sentence idea:** Isolate the contribution of aliasing in strided downsampling to small-object failure by controlling the anti-aliasing filter while holding everything else fixed.
- **Problem:** Strided convolutions and pooling alias high-frequency content; small objects live almost entirely in the frequencies that aliasing corrupts, yet aliasing is treated as a signal-processing footnote.
- **Core Hypothesis (falsifiable):** Adding proper low-pass filtering before each stride improves AP_small significantly more than AP_large, and the improvement scales with the object's frequency content; if gains are size-uniform, aliasing is not the mechanism.
- **Why Important:** A cheap, principled fix at fixed FLOPs would beat expensive resolution scaling for a large class of deployments.
- **Why Possibly Novel:** Anti-aliasing has been studied for shift-invariance in classification; a size-stratified causal account for detection/segmentation of small objects is unexplored territory.
- **Minimal Experiment:** Train pairs of detectors identical except for blur-before-stride; report size-stratified AP and correlate per-instance gains with a per-instance frequency-content measure.
- **Main Risk:** Anti-aliasing also smooths useful texture, so effects may cancel in a way that is informative but hard to headline.
- **Research Cluster:** SMALL-OBJ / PHENOMENON

### IDEA-B-0007 — Small-object recognition is mostly context recognition
- **One-sentence idea:** Measure how much small-object detection survives when the object's own pixels are ablated, to quantify context reliance.
- **Problem:** For sub-16px objects the object appearance carries few bits; models may be detecting "the place where an X would be" rather than X, which changes how robustness and transfer should be reasoned about.
- **Core Hypothesis (falsifiable):** Replacing small-object pixels with matched noise reduces detection recall by less than 50% for the smallest size decile, while the same ablation on large objects reduces recall by more than 90%.
- **Why Important:** If small-object detection is context-driven, then small-object benchmarks measure scene priors, and domain shift will hit small objects hardest — a testable deployment prediction.
- **Why Possibly Novel:** Context studies exist for detection broadly; the size-conditional decomposition and its link to shift-fragility of small objects specifically is not established.
- **Minimal Experiment:** On a trained detector, in-place ablate GT object pixels (noise/inpaint) at test time; report recall-vs-size curves with and without object evidence, on in-domain and shifted data.
- **Main Risk:** Inpainting artifacts may themselves be detectable, inflating apparent context reliance.
- **Research Cluster:** SMALL-OBJ / GENERALIZATION

### IDEA-B-0008 — Tiling-inference gains are a train-test resolution mismatch artifact
- **One-sentence idea:** Test whether SAHI-style tiled inference gains disappear when training uses matched-scale random crops.
- **Problem:** Tiled/sliced inference is widely used for small objects and treated as inherently beneficial, but it may only compensate for a mismatch between training crop statistics and test-time object scales.
- **Core Hypothesis (falsifiable):** For models trained with scale-matched cropping, tiled inference adds <20% of the AP_small gain it provides to conventionally trained models.
- **Why Important:** Tiling multiplies inference cost several-fold in production aerial/medical pipelines; if it is avoidable by training policy, that is a large real-world saving.
- **Why Possibly Novel:** Tiling is evaluated as a tool, never as a symptom; framing it as a diagnostic of train-test scale mismatch is a new lens.
- **Minimal Experiment:** Train detectors on VisDrone/DOTA with conventional vs. scale-matched crop policies; evaluate both with and without tiled inference; compare the four cells.
- **Main Risk:** Scale-matched training may hurt large-object AP, making the practical conclusion mixed.
- **Research Cluster:** SMALL-OBJ / EVAL-WEAK

### IDEA-B-0009 — Loss share, not capacity, starves small objects in dense losses
- **One-sentence idea:** Quantify the fraction of total training loss (and gradient norm) attributable to small objects, and test whether instance-normalized loss allocation removes the size gap.
- **Problem:** Pixel-averaged and box-averaged losses give small objects a vanishing share of the training signal, but the community treats the small-object gap as a representation problem.
- **Core Hypothesis (falsifiable):** Equalizing per-instance loss contribution across sizes (without any architectural change) closes at least a third of the AP gap between small and large objects; if it closes almost none, the bottleneck is representational.
- **Why Important:** Distinguishes an optimization-accounting problem (cheap to fix) from an information problem (expensive to fix) at the heart of a whole subfield.
- **Why Possibly Novel:** Reweighting has been tried ad hoc; the contribution here is the measurement of gradient share by size and a clean falsification framing, not a new loss.
- **Minimal Experiment:** Instrument training to log per-size loss/gradient shares; train matched models with size-equalized allocation; report size-stratified AP deltas.
- **Main Risk:** Aggressive upweighting of tiny noisy instances may amplify label-noise effects (interacts with IDEA-B-0003).
- **Research Cluster:** SMALL-OBJ

### IDEA-B-0010 — Benchmarks conflate smallness with occlusion and truncation
- **One-sentence idea:** Disentangle "small" from "occluded/truncated/blurred" in benchmark GT and re-measure the pure size effect on detection performance.
- **Problem:** In natural-image benchmarks, small objects are disproportionately distant, occluded, or truncated, so the measured "small-object problem" is partly a different problem wearing a size costume.
- **Core Hypothesis (falsifiable):** After conditioning on occlusion/truncation/blur annotations, the size-performance slope flattens by at least half relative to the unconditioned slope.
- **Why Important:** Methods designed for "small objects" may actually need to target occlusion or blur; correct problem attribution redirects a research area.
- **Why Possibly Novel:** Size-stratified reporting is universal, but a covariate-adjusted causal decomposition of the size effect has not been done.
- **Minimal Experiment:** Use datasets with occlusion flags (KITTI, CrowdHuman) plus a blur estimator; fit performance as a function of size with and without covariates; compare slopes.
- **Main Risk:** Covariates are imperfectly annotated, and residual confounding may persist in both directions.
- **Research Cluster:** SMALL-OBJ / EVAL-WEAK

### IDEA-B-0011 — Copy-paste helps small objects via positive-sample count, not diversity
- **One-sentence idea:** Decompose copy-paste augmentation's small-object gains into "more positives per epoch" vs. "more visual diversity" using degenerate paste controls.
- **Problem:** Copy-paste is a standard small-object remedy, with the gain folk-attributed to visual diversity, but it also mechanically multiplies the count of positive training samples for rare small instances.
- **Core Hypothesis (falsifiable):** Pasting the same instance repeatedly (zero added diversity) recovers most (>70%) of the AP_small gain of diverse copy-paste at matched paste counts.
- **Why Important:** If count is the mechanism, simpler oversampling schedules achieve the same effect without paste artifacts, and diversity-focused augmentation research for small objects is chasing the wrong variable.
- **Why Possibly Novel:** Copy-paste papers ablate paste probability but never separate count from diversity with degenerate-paste controls.
- **Minimal Experiment:** Train with (a) no paste, (b) diverse paste, (c) single-instance repeated paste, (d) loss-upweighting matched to paste count; compare AP_small.
- **Main Risk:** Repeated pasting may cause memorization effects that mimic diversity gains for the wrong reason.
- **Research Cluster:** SMALL-OBJ / ASSUMPTION

### IDEA-B-0012 — JPEG compression in dataset pipelines disproportionately erases small objects
- **One-sentence idea:** Measure the size-stratified performance cost of the compression levels silently baked into popular datasets and re-train/evaluate on less-compressed sources where available.
- **Problem:** Benchmarks are distributed as compressed JPEGs; compression removes exactly the high-frequency content small objects depend on, yet compression level is never treated as an experimental variable.
- **Core Hypothesis (falsifiable):** Recompressing images at typical web-quality factors degrades AP_small at least 3x more (relatively) than AP_large, and part of the "small-object problem" magnitude is compression-level dependent.
- **Why Important:** It reframes some of the small-object gap as a data-pipeline artifact and gives deployments a concrete, cheap knob (capture/storage quality).
- **Why Possibly Novel:** Compression robustness is studied as a corruption; treating dataset-native compression as a confounder of the small-object literature is new.
- **Minimal Experiment:** Sweep JPEG quality on validation sets, report size-stratified degradation curves; where RAW/PNG sources exist, compare models trained on each.
- **Main Risk:** For most benchmarks, uncompressed originals do not exist, limiting the training-side arm of the study.
- **Research Cluster:** SMALL-OBJ / EVAL-WEAK

### IDEA-B-0013 — Stride-quantized regression targets impose a floor on small-object localization
- **One-sentence idea:** Test whether the discretization of regression targets to feature-grid stride creates an irreducible localization error that binds only for small objects.
- **Problem:** Box/mask heads predict offsets relative to a stride-s grid; a fixed sub-cell error is negligible for a 200 px object and fatal for a 10 px object, but this arithmetic is rarely confronted directly.
- **Core Hypothesis (falsifiable):** The empirical localization error distribution of small objects concentrates near the stride-implied quantization floor, and predicting offsets in a finer coordinate system (same backbone) shifts the distribution off the floor.
- **Why Important:** A confirmed floor turns "small-object localization" from a learning problem into a numerics problem with a known fix.
- **Why Possibly Novel:** Sub-pixel tricks exist in keypoint estimation; a quantization-floor analysis connecting stride arithmetic to size-stratified detection error is not established.
- **Minimal Experiment:** Plot per-size localization error against the stride-implied floor for standard detectors; retrain heads with finer offset parameterization and re-plot.
- **Main Risk:** Modern heads with continuous offsets may already sit above the floor, yielding a null (which is itself publishable but less exciting).
- **Research Cluster:** SMALL-OBJ

### IDEA-B-0014 — Per-size score calibration recovers small-object AP without retraining
- **One-sentence idea:** Test whether small objects are systematically under-scored (not under-localized) and whether size-conditional score recalibration alone recovers a meaningful share of the size gap.
- **Problem:** A single confidence scale is used across object sizes, but correct small detections may sit below the operating threshold while equally correct large detections sit above it.
- **Core Hypothesis (falsifiable):** Post-hoc monotone recalibration of scores conditioned on predicted box size improves AP_small by a nontrivial margin with zero effect on AP_large, on multiple detector families.
- **Why Important:** A training-free fix that transfers across models would immediately benefit every deployed small-object system and expose a scoring bias in evaluation.
- **Why Possibly Novel:** Score calibration for detection exists, but size-conditional calibration framed as a small-object remedy and as evidence of a systematic scoring bias is unexplored.
- **Minimal Experiment:** Fit isotonic regression per size bin on a validation split; evaluate AP by size on test; repeat across three detector families to test universality.
- **Main Risk:** AP is rank-based within class, so gains only materialize where cross-size rank distortions actually occur — the effect could be small.
- **Research Cluster:** SMALL-OBJ / CALIBRATION

### IDEA-B-0015 — Query starvation limits transformer detectors on dense small-object scenes
- **One-sentence idea:** Characterize how DETR-family recall degrades as scene object count approaches the query count, and whether the failure is capacity or competition.
- **Problem:** Set-prediction detectors allocate a fixed query budget; aerial and crowd scenes can exceed it, but the failure mode (silent recall collapse vs. graceful sharing) is not characterized.
- **Core Hypothesis (falsifiable):** Recall of small objects begins degrading when instance count exceeds a fixed fraction (<100%) of query count, and the lost instances are predicted by pairwise query-competition metrics rather than instance appearance.
- **Why Important:** Defines a hard applicability boundary for a dominant architecture family and gives dataset builders a diagnostic before choosing detectors.
- **Why Possibly Novel:** Query-count ablations exist; a competition-based mechanistic account of which instances get dropped in over-subscribed scenes is new.
- **Minimal Experiment:** Evaluate a DETR-family model on scenes binned by instance count; measure per-bin recall and correlate dropped instances with Hungarian-matching competition statistics.
- **Main Risk:** Confounding between object count and object size/density in natural data may require synthetic-scene controls.
- **Research Cluster:** SMALL-OBJ / REP-MISMATCH

### IDEA-B-0016 — Size-adaptive IoU thresholds change small-object method rankings
- **One-sentence idea:** Re-evaluate the small-object literature's method rankings under IoU thresholds that equalize localization tolerance in pixels rather than in ratio.
- **Problem:** A fixed IoU threshold demands sub-pixel precision from small objects and generous slack from large ones, so AP_small partially measures noise sensitivity rather than detection competence.
- **Core Hypothesis (falsifiable):** Under a size-adaptive threshold schedule (matched expected pixel tolerance), the ranking of representative small-object methods changes materially (rank correlation with standard AP_small below ~0.8).
- **Why Important:** If rankings flip, the community has been selecting methods with the wrong ruler for a decade of small-object work.
- **Why Possibly Novel:** Alternative localization metrics exist (e.g., normalized distance metrics in aerial detection), but a systematic ranking-stability study across the mainstream small-object literature has not been done.
- **Minimal Experiment:** Re-score public predictions (or rerun open-source methods) on COCO/VisDrone under standard vs. size-adaptive thresholds; report rank correlations and case studies of flips.
- **Main Risk:** The "right" size-adaptive schedule is a free parameter; conclusions must be shown stable across reasonable schedules.
- **Research Cluster:** SMALL-OBJ / EVAL-WEAK

### IDEA-B-0017 — Many small-object "false positives" are missing ground truth
- **One-sentence idea:** Human-verify high-confidence small-object false positives on standard benchmarks to estimate the missing-annotation rate and its effect on AP.
- **Problem:** Small objects are the easiest for annotators to miss; every missed GT converts a correct detection into a scored false positive, punishing exactly the most sensitive models.
- **Core Hypothesis (falsifiable):** Among the top-confidence "false positive" small detections of a strong model, a substantial fraction (>25%) are verified true objects absent from GT, and correcting them changes AP_small by more than typical method gains.
- **Why Important:** It would show benchmarks systematically penalize high-recall small-object models, distorting the field's incentive gradient.
- **Why Possibly Novel:** Missing-annotation audits exist for large-vocabulary datasets; a size-focused audit tied to the FP accounting of AP is new.
- **Minimal Experiment:** Sample 2,000 high-confidence small FPs from a SOTA model on COCO val; three-way human adjudication; recompute AP with adjudicated GT.
- **Main Risk:** Adjudicators may over-accept plausible-looking detections (confirmation bias); needs blinded protocol with injected decoys.
- **Research Cluster:** SMALL-OBJ / EVAL-WEAK

### IDEA-B-0018 — Background-dominated normalization statistics wash out small-object features
- **One-sentence idea:** Test whether global normalization layers (BN/LN statistics dominated by background) suppress the activation signal of small objects.
- **Problem:** Normalization statistics are computed over entire feature maps where small objects occupy <0.1% of positions, so their activations are normalized "as background," potentially attenuating their distinctiveness.
- **Core Hypothesis (falsifiable):** The activation SNR of small-object regions (relative to local background) drops measurably after each global normalization layer, and masking small-object regions out of statistic computation at inference increases their SNR and recall.
- **Why Important:** Would identify a pervasive, architecture-agnostic mechanism that silently taxes small objects in every modern network.
- **Why Possibly Novel:** Normalization research targets optimization and robustness; the spatial-minority suppression effect on dense-prediction targets is uncharted.
- **Minimal Experiment:** Instrument a trained segmenter to log per-region activation statistics through the network; intervene on normalization statistics (exclude object regions) and measure per-size recall change.
- **Main Risk:** Statistic interventions at inference create train-test mismatch that could confuse attribution.
- **Research Cluster:** SMALL-OBJ / REP-MISMATCH

### IDEA-B-0019 — Pretraining never shows backbones sub-8px objects
- **One-sentence idea:** Quantify the object-scale distribution seen during classification/SSL pretraining and test whether matching it to downstream small-object scales closes the transfer gap.
- **Problem:** Backbones pretrained at ~224 px on object-centric photos essentially never see semantically labeled sub-8px objects, so "pretrained features" may be structurally blind at small scales.
- **Core Hypothesis (falsifiable):** Injecting scale-matched small-object views into pretraining (same data, different cropping curriculum) improves downstream AP_small significantly more than AP_large at matched pretraining compute.
- **Why Important:** Moves small-object research upstream to pretraining policy, where a one-time cost benefits every downstream user.
- **Why Possibly Novel:** Resolution curricula exist for efficiency; a pretraining-scale-distribution account of the small-object transfer gap is a fresh causal target.
- **Minimal Experiment:** Estimate the effective object-scale histogram of standard pretraining; pretrain two matched backbones with standard vs. small-scale-enriched cropping; fine-tune on detection and compare size-stratified AP.
- **Main Risk:** Pretraining ablations are compute-heavy; effect could be entangled with augmentation strength.
- **Research Cluster:** SMALL-OBJ / CROSS-DOMAIN

### IDEA-B-0020 — Zoom TTA only helps undertrained-at-scale detectors
- **One-sentence idea:** Test whether multi-scale test-time augmentation gains for small objects shrink to zero as training-time scale augmentation coverage increases.
- **Problem:** Multi-scale TTA is treated as free small-object accuracy, but it may only patch a training deficiency, meaning its persistence in benchmarks signals under-optimized baselines.
- **Core Hypothesis (falsifiable):** The AP_small gain from zoom TTA is a decreasing function of training scale-augmentation range, reaching statistical zero for sufficiently wide training scale coverage.
- **Why Important:** TTA multiplies inference cost; showing when it is redundant saves compute and cleans up benchmark comparisons where TTA usage is inconsistent.
- **Why Possibly Novel:** TTA and train-time augmentation are studied separately; their substitutability curve for the small-object regime has not been mapped.
- **Minimal Experiment:** Train a detector grid over scale-augmentation ranges; evaluate each with and without zoom TTA; plot TTA gain vs. training coverage.
- **Main Risk:** Very wide training scale ranges may lower peak in-distribution accuracy, complicating the "matched baseline" comparison.
- **Research Cluster:** SMALL-OBJ / ASSUMPTION

### IDEA-B-0021 — Mosaic augmentation's seam artifacts hurt small-object localization
- **One-sentence idea:** Measure whether mosaic-style augmentation improves small-object classification recall while degrading localization precision near tile seams.
- **Problem:** Mosaic is a default in modern detector recipes and credited with small-object gains, but it creates unnatural boundaries and truncated context whose costs are never itemized.
- **Core Hypothesis (falsifiable):** Models trained with mosaic show a measurable increase in localization error for objects whose training-time counterparts frequently landed near seams, and seam-aware mosaic (no object-seam intersections) retains recall gains while removing the localization penalty.
- **Why Important:** Recipe components adopted for headline AP can carry hidden error-profile costs; itemizing them enables better recipe design than aggregate ablation.
- **Why Possibly Novel:** Mosaic ablations report aggregate AP; a decomposition into recall vs. localization and a seam-interaction mechanism is new.
- **Minimal Experiment:** Train with/without mosaic and with seam-aware mosaic; decompose errors with TIDE-style analysis stratified by object size.
- **Main Risk:** Seam effects may be too small relative to mosaic's scale-mixing effect to isolate cleanly.
- **Research Cluster:** SMALL-OBJ

### IDEA-B-0022 — Temporal aggregation for tiny objects works via motion, not appearance accumulation
- **One-sentence idea:** Determine whether video-based small-object detection gains come from integrating appearance over frames or from motion cues, using frame-shuffle and static-scene controls.
- **Problem:** Video detectors that aggregate frames improve tiny-object detection, and the standard story is "appearance accumulation," but shuffling or motion cues could explain the gains differently.
- **Core Hypothesis (falsifiable):** Aggregation gains for the smallest size decile drop by more than half when frame order is shuffled (destroying coherent motion but preserving appearance samples), while large-object gains are order-insensitive.
- **Why Important:** The mechanism dictates system design: appearance accumulation favors alignment modules, motion favors explicit temporal differencing, and they have very different compute profiles.
- **Why Possibly Novel:** Video detection ablations rarely include order-destroying controls that separate the two information sources.
- **Minimal Experiment:** Evaluate a temporal detector with ordered, shuffled, and repeated-single-frame inputs on a UAV video benchmark; report size-stratified deltas.
- **Main Risk:** Architectures with explicit alignment may degrade under shuffle for reasons unrelated to information content.
- **Research Cluster:** SMALL-OBJ / PHENOMENON

### IDEA-B-0023 — There is a size threshold below which detection is the wrong abstraction
- **One-sentence idea:** Locate the object-size crossover point where density/counting formulations outperform instance detection, and characterize what determines it.
- **Problem:** The field applies instance detection at all scales, but below some size, instance separation may be information-theoretically unsupportable while aggregate quantities (counts, density) remain estimable.
- **Core Hypothesis (falsifiable):** On benchmarks with both detection and density GT, there exists a size threshold below which density-based counting has lower count error than detection-then-count, and the threshold shifts predictably with image noise level.
- **Why Important:** Would give practitioners a principled decision rule for tool choice and mark a boundary of the detection paradigm rather than another increment inside it.
- **Why Possibly Novel:** Counting and detection communities coexist without an explicit, empirically located crossover analysis parameterized by object size and noise.
- **Minimal Experiment:** On crowd/vehicle benchmarks, evaluate matched detection and density models on count error stratified by object size; locate the crossover; perturb noise to test threshold movement.
- **Main Risk:** Crossover location may be heavily dataset-specific, weakening the general claim.
- **Research Cluster:** SMALL-OBJ / EVAL-WEAK

### IDEA-B-0024 — Super-resolution preprocessing helps detection only when it doesn't hallucinate
- **One-sentence idea:** Test whether SR-for-detection gains are predicted by SR fidelity metrics or anti-correlated with SR hallucination propensity.
- **Problem:** Super-resolution front-ends are a popular small-object remedy, but generative SR invents plausible texture, and no one has separated "sharper true signal" from "confident fabrication" in the downstream effect.
- **Core Hypothesis (falsifiable):** Downstream AP_small gain across SR models correlates with distortion-oriented fidelity (e.g., reconstruction error on held-out pairs) and anti-correlates with generative sharpness measures, with GAN/diffusion SR underperforming regression SR at matched PSNR.
- **Why Important:** Provides a selection rule for a widely deployed pipeline pattern and a caution about generative preprocessing in safety-relevant sensing.
- **Why Possibly Novel:** SR-for-detection papers report gains for single SR models; a cross-SR-model study linking hallucination propensity to downstream harm is missing.
- **Minimal Experiment:** Fix one detector; sweep 6–8 SR front-ends spanning regression-to-generative; measure AP_small and per-image correlation between SR artifacts and detection errors.
- **Main Risk:** SR models differ along many axes simultaneously; attribution needs careful matching or within-model sharpness knobs.
- **Research Cluster:** SMALL-OBJ / SYNTH-DATA

### IDEA-B-0025 — Center-sampling radii in anchor-free detectors are size-biased in pixels
- **One-sentence idea:** Test whether anchor-free center-sampling rules, defined in feature-grid units, systematically under-sample positives for small overlapping objects.
- **Problem:** Anchor-free detectors take positives within a radius of the object center measured in grid cells, which is a size-dependent fraction of the object; for tiny adjacent objects the sampling regions collide or vanish.
- **Core Hypothesis (falsifiable):** The number of positive samples per instance drops superlinearly with object size below a threshold, and re-parameterizing sampling in object-relative units increases small-object recall in crowded scenes without harming isolated-object performance.
- **Why Important:** A concrete, checkable geometry bug in a dominant detector family, with a fix that is a parameterization change rather than a new module.
- **Why Possibly Novel:** Center sampling is treated as a solved hyperparameter; its object-relative geometry and collision behavior in crowds has not been analyzed as the object of study.
- **Minimal Experiment:** Instrument positive-sample counts by size and crowding on FCOS-style training; retrain with object-relative radii; compare recall in crowded vs. sparse scenes.
- **Main Risk:** Modern assigners (e.g., optimal-transport-based) may already mitigate this, making the finding version-specific.
- **Research Cluster:** SMALL-OBJ

### IDEA-B-0026 — Distillation amplifies teacher bias against small objects
- **One-sentence idea:** Measure whether knowledge distillation transfers the teacher's size-dependent error profile to students and whether size-filtered distillation targets prevent it.
- **Problem:** Teachers are noisiest exactly on small objects; distillation treats all teacher outputs as equally trustworthy, potentially compounding the size gap across model generations.
- **Core Hypothesis (falsifiable):** Students distilled from a size-biased teacher show a larger small-vs-large AP gap than students trained on GT alone at matched total accuracy, and masking distillation loss on low-teacher-confidence small regions removes the excess gap.
- **Why Important:** Distillation is the default compression path to edge deployment, where small-object performance often matters most (drones, driving); a systematic bias amplification would be a deployment hazard.
- **Why Possibly Novel:** Distillation bias studies focus on class imbalance; the size axis and its interaction with dense-prediction distillation is unexamined.
- **Minimal Experiment:** Distill matched students with full, size-masked, and confidence-masked teacher targets; compare size-stratified AP gaps against a GT-only student.
- **Main Risk:** The teacher's soft labels on small objects may actually carry useful dark knowledge, making masking harmful and the result mixed.
- **Research Cluster:** SMALL-OBJ / UNCERTAINTY

### IDEA-B-0027 — Meta-analysis: do published "small-object" methods improve smalls specifically?
- **One-sentence idea:** Systematically re-run open-source small-object methods and test whether their AP_small gains exceed what their overall AP gain predicts.
- **Problem:** Many papers claim small-object improvements, but AP_small co-moves with total AP; the field lacks a test of whether any method improves smalls beyond the generic tide.
- **Core Hypothesis (falsifiable):** For most published small-object methods with public code, the residual of AP_small after regressing on total AP across methods is statistically indistinguishable from zero.
- **Why Important:** Would either validate or deflate a large literature, and establish "size-specificity residual" as a required reporting statistic.
- **Why Possibly Novel:** Method-level meta-analyses with controlled re-runs are rare in detection; the specific size-residual formulation is new.
- **Minimal Experiment:** Re-run 15–20 open-source methods under one training harness; fit the cross-method AP_small vs. AP regression; report residuals with bootstrap CIs.
- **Main Risk:** Re-implementation and harness standardization may not reproduce original numbers, inviting disputes about faithfulness.
- **Research Cluster:** SMALL-OBJ / EVAL-WEAK / NEG-RESULT

### IDEA-B-0028 — Effective stride, not receptive field, is the binding constraint for smalls
- **One-sentence idea:** At matched FLOPs, compare reducing effective output stride vs. enlarging receptive field to determine which constraint binds small-object performance.
- **Problem:** Small-object architecture work oscillates between "more resolution" and "more context" without a controlled comparison isolating which quantity is actually limiting.
- **Core Hypothesis (falsifiable):** At matched compute, halving effective output stride improves AP_small significantly more than doubling receptive field via dilation/attention, and the two do not interact synergistically.
- **Why Important:** A clean answer would collapse a large design space and stop redundant architecture exploration.
- **Why Possibly Novel:** Both knobs are studied, but almost never against each other under matched-compute accounting with size-stratified reporting.
- **Minimal Experiment:** Construct a 2x2 (stride x receptive field) grid of variants of one backbone at matched FLOPs; train identically; report AP by size.
- **Main Risk:** "Matched FLOPs" hides memory/latency differences that matter in practice, limiting the design-guidance value.
- **Research Cluster:** SMALL-OBJ

### IDEA-B-0029 — The optimal focal-loss gamma is object-size-dependent
- **One-sentence idea:** Test whether hard-example weighting optima differ systematically by object size, making any single gamma a compromise that taxes small objects.
- **Problem:** Focal-loss-style hard-example weighting uses one global focusing parameter, but small objects produce systematically lower confidences, so a global gamma treats them as permanently "hard" in a way that may saturate learning.
- **Core Hypothesis (falsifiable):** Sweeping gamma separately for small and large objects yields different optima, and size-conditional gamma improves AP_small over the best global gamma at no cost to AP_large.
- **Why Important:** Reveals that "one loss hyperparameter fits all sizes" silently allocates optimization difficulty, a pattern likely repeated across many loss designs.
- **Why Possibly Novel:** Focal loss variants abound, but the size-conditional structure of its optimum has not been mapped as an empirical object.
- **Minimal Experiment:** Grid-search gamma jointly and size-conditionally on RetinaNet-style training; compare best configurations with seed-replicated runs.
- **Main Risk:** This flirts with "loss tweaking"; the contribution must stay the measurement of size-dependence, not the tweak itself.
- **Research Cluster:** SMALL-OBJ / ASSUMPTION

### IDEA-B-0030 — Physical-scale conditioning beats scale augmentation in aerial imagery
- **One-sentence idea:** Test whether conditioning aerial detectors on ground-sample distance (GSD) outperforms scale augmentation for small vehicles across altitude shifts.
- **Problem:** Aerial pipelines treat scale as a nuisance to augment away, discarding the physically known meters-per-pixel signal that fully determines object pixel size.
- **Core Hypothesis (falsifiable):** A detector given GSD as input generalizes across held-out altitudes/sensors better than a scale-augmented but GSD-blind detector, and the gap grows with altitude extrapolation distance.
- **Why Important:** Aerial and satellite deployments always know GSD; exploiting free physical metadata could beat expensive augmentation and define a pattern (physical conditioning over invariance) applicable to other sensors.
- **Why Possibly Novel:** GSD normalization is used in preprocessing heuristics, but a controlled conditioning-vs-invariance study with extrapolation stress tests is missing.
- **Minimal Experiment:** Train matched models (GSD-conditioned, GSD-normalized-resample, scale-augmented) on multi-altitude data; evaluate on held-out altitudes; plot error vs. extrapolation distance.
- **Main Risk:** Public multi-altitude datasets with reliable GSD metadata are limited, constraining the extrapolation range testable.
- **Research Cluster:** SMALL-OBJ / GENERALIZATION

### IDEA-B-0031 — Polygon-smoothed GT caps achievable small-instance mask quality
- **One-sentence idea:** Bound the achievable mask AP for small instances by re-annotating polygon-based GT at pixel accuracy and measuring the polygon-induced quality ceiling.
- **Problem:** COCO-style polygon masks over-smooth small instances (few vertices spread over few pixels), so mask metrics for small objects may saturate at a GT-imposed ceiling no method can pass.
- **Core Hypothesis (falsifiable):** Pixel-accurate re-annotation of small-instance masks disagrees with polygon GT by an IoU margin exceeding the gap between current SOTA and perfect scores, implying published small-mask comparisons operate inside GT noise.
- **Why Important:** Establishes whether small-instance mask research is currently measurable at all on standard benchmarks.
- **Why Possibly Novel:** Mask quality audits exist (e.g., for boundary sharpness generally); the small-instance polygon-ceiling framing with an explicit method-gap comparison is new.
- **Minimal Experiment:** Re-annotate ~500 small instances at pixel level; compute polygon-vs-pixel GT IoU distribution; compare against SOTA-to-perfect gaps on the same instances.
- **Main Risk:** Pixel-accurate annotation of tiny instances is itself noisy; requires multi-annotator consensus protocols.
- **Research Cluster:** SMALL-OBJ / EVAL-WEAK

### IDEA-B-0032 — Long-range context helps small objects in-domain but hurts under shift
- **One-sentence idea:** Test whether context reliance that boosts small-object accuracy in-distribution becomes a liability under domain shift, creating a context-robustness tradeoff.
- **Problem:** Global context modules improve small-object benchmarks, but if the gains come from scene priors (see IDEA-B-0007), they should invert when scene statistics shift.
- **Core Hypothesis (falsifiable):** Across matched models with varying context aperture, in-domain AP_small increases with aperture while out-of-domain AP_small peaks at an intermediate aperture and declines beyond it.
- **Why Important:** Would establish a quantified tradeoff curve practitioners can position themselves on, instead of assuming "more context is free."
- **Why Possibly Novel:** Context ablations and robustness studies exist separately; the interaction curve specifically for small objects has not been traced.
- **Minimal Experiment:** Train segmenters/detectors with restricted attention/context windows at several apertures; evaluate on in-domain and cross-domain aerial/driving sets; plot both curves.
- **Main Risk:** Aperture restriction also changes capacity utilization, requiring careful compute matching.
- **Research Cluster:** SMALL-OBJ / GENERALIZATION

### IDEA-B-0033 — High-res features already contain small-object information the head can't use
- **One-sentence idea:** Probe frozen high-resolution feature maps with size-specialized lightweight heads to test whether small-object information exists but is unexploited by standard joint training.
- **Problem:** The small-object gap is attributed to features lacking information, but it could instead be that joint training allocates head capacity and gradients to the dominant size regime.
- **Core Hypothesis (falsifiable):** Linear or shallow probes trained only on small objects atop frozen features recover substantially more small-object recall than the jointly trained head extracts, demonstrating unexploited information.
- **Why Important:** Locates the bottleneck (feature vs. decoding) with a cheap experiment, redirecting either architecture or optimization research accordingly.
- **Why Possibly Novel:** Probing is standard in representation learning but rarely applied as a bottleneck-locator for the size axis in dense prediction.
- **Minimal Experiment:** Freeze a trained detector's backbone; fit size-restricted probes per pyramid level; compare probe recall against the deployed head's recall on the same instances.
- **Main Risk:** Probes trained on the test distribution's size range have an unfair specialization advantage; needs careful train/probe splits.
- **Research Cluster:** SMALL-OBJ / REP-MISMATCH

### IDEA-B-0034 — Token merging in ViTs deletes small objects at a measurable rate
- **One-sentence idea:** Quantify the size-stratified accuracy cost of token pruning/merging schemes and identify the merge-decision statistics that predict small-object deletion.
- **Problem:** Token reduction methods report near-lossless aggregate accuracy, but small objects occupy few tokens, and merging decisions based on similarity may treat them as redundant background.
- **Core Hypothesis (falsifiable):** At token-reduction ratios that cost <1% overall mIoU, small-object recall drops by several times that amount, and the deleted instances are predictable from token-similarity margins before merging.
- **Why Important:** Token reduction is heading into production inference stacks; a hidden size-selective tax would matter for exactly the safety-critical detections least visible in aggregate metrics.
- **Why Possibly Novel:** Token-reduction papers report aggregate metrics; a size-stratified failure analysis with predictive merge statistics is absent.
- **Minimal Experiment:** Apply public token-merging methods to a ViT segmenter at several ratios; report size-stratified recall curves; regress instance deletion on merge statistics.
- **Main Risk:** Results may vary widely across merging schemes, requiring several to be tested for a general claim.
- **Research Cluster:** SMALL-OBJ / ROBUSTNESS

### IDEA-B-0035 — Label smoothing selectively harms rare weak-signal (small) objects
- **One-sentence idea:** Test whether label smoothing, benign in aggregate, disproportionately suppresses learning of small/faint objects whose evidence is already weak.
- **Problem:** Label smoothing is a default recipe ingredient validated on aggregate metrics; its interaction with instances whose signal-to-noise is marginal has not been isolated.
- **Core Hypothesis (falsifiable):** Removing label smoothing (or applying it size-conditionally) increases small-object recall at equal overall accuracy, with the effect size growing as instance SNR decreases.
- **Why Important:** Recipe defaults tuned on aggregate benchmarks may systematically tax minority regimes; this is a concrete, checkable instance of that general failure pattern.
- **Why Possibly Novel:** Label smoothing's effects on calibration and distillation are studied; its size/SNR-conditional effect in dense prediction is not.
- **Minimal Experiment:** Train matched detectors with smoothing on/off/size-conditional; report size- and contrast-stratified recall with seed replication.
- **Main Risk:** Effect may be small and interact with other recipe components (e.g., focal loss), demanding a larger factorial design.
- **Research Cluster:** SMALL-OBJ / ASSUMPTION

### IDEA-B-0036 — AP_small follows a predictable power law in test resolution
- **One-sentence idea:** Characterize AP_small as a function of inference resolution across models and test whether a simple scaling law lets resolution-confounded comparisons be normalized.
- **Problem:** Papers evaluate at different resolutions, and small-object results are exquisitely resolution-sensitive, making cross-paper comparison of AP_small nearly meaningless.
- **Core Hypothesis (falsifiable):** For fixed models, AP_small(resolution) follows a two-parameter saturating power law with model-specific parameters, enabling normalization of reported results to a common resolution within ~1 AP.
- **Why Important:** A validated normalization would retroactively clean up an entire literature's comparisons and expose which "gains" were resolution artifacts.
- **Why Possibly Novel:** Resolution scaling curves exist for classification compute studies; fitting and validating a normalization law for size-stratified detection metrics is new.
- **Minimal Experiment:** Evaluate 10 public detectors over a dense resolution sweep; fit the law per model; validate extrapolation on held-out resolutions.
- **Main Risk:** Architectures with resolution-specialized components (fixed positional grids, window sizes) may break any simple law.
- **Research Cluster:** SMALL-OBJ / EVAL-WEAK

### IDEA-B-0037 — Annotation-tool minimum sizes truncate the GT object-size distribution
- **One-sentence idea:** Audit whether benchmark size distributions are truncated by annotation-tool ergonomics, using synthetic object insertion to measure the recall of the annotation pipeline itself.
- **Problem:** If annotators practically cannot mark objects below some pixel size, benchmarks silently exclude the smallest real objects, and "small-object performance" is measured only above the tool floor.
- **Core Hypothesis (falsifiable):** The empirical GT size distribution shows a non-physical cutoff inconsistent with the optics-implied object-size distribution, and human annotators asked to re-annotate images with synthetically inserted tiny objects miss them at a rate that reproduces the cutoff.
- **Why Important:** Deployment distributions include the sub-floor regime; models will face objects benchmarks never measured, an unquantified safety gap.
- **Why Possibly Novel:** Dataset bias audits rarely treat the annotation tool as a measurement instrument with its own response function.
- **Minimal Experiment:** Fit size distributions of several benchmarks against scene-geometry-implied expectations; run an insertion-recall study with the original annotation tooling.
- **Main Risk:** Reconstructing "expected" physical size distributions requires assumptions that critics can dispute.
- **Research Cluster:** SMALL-OBJ / EVAL-WEAK / ANNOT-EFF

### IDEA-B-0038 — Small-object mask metrics need signed-distance scoring, not overlap
- **One-sentence idea:** Show that overlap-based mask metrics collapse to near-binary behavior for small objects and evaluate a signed-boundary-distance alternative for metric stability.
- **Problem:** For a 30-pixel mask, one pixel of erosion swings IoU dramatically, making small-object mask comparisons dominated by quantization noise rather than quality differences.
- **Core Hypothesis (falsifiable):** The test-retest reliability (across seeds and across equivalent-quality masks) of a signed-distance-based score is several times higher than IoU for objects under 32 px, while the two metrics agree for large objects.
- **Why Important:** Metric noise at small scales silently blocks progress measurement; a stability-validated alternative would make small-instance research legible.
- **Why Possibly Novel:** Boundary-distance metrics exist; the contribution is the reliability analysis demonstrating when overlap metrics become un-usable and a validated switch-over rule.
- **Minimal Experiment:** Generate controlled mask perturbations at various object sizes; compute metric response curves and test-retest reliability for IoU, boundary-F, and signed-distance scores.
- **Main Risk:** Signed-distance metrics have their own pathologies (topology changes, multi-component masks) needing careful handling.
- **Research Cluster:** SMALL-OBJ / EVAL-WEAK

### IDEA-B-0039 — Human small-object detection sets the information-theoretic reference
- **One-sentence idea:** Measure human detection performance on benchmark small objects under matched viewing conditions to determine whether the "small-object gap" is model-side or information-side.
- **Problem:** The community assumes small objects are "hard but solvable"; without a human (or ideal-observer) reference, we cannot tell whether the remaining gap is closable in principle.
- **Core Hypothesis (falsifiable):** Human recall on the smallest size decile, given unlimited time and zoom, exceeds SOTA model recall by a wide margin, localizing the gap on the model side; if humans match models, the residual gap is informational.
- **Why Important:** Determines whether continued small-object research targets a real headroom or a wall, which changes resource allocation for the whole subfield.
- **Why Possibly Novel:** Human-vs-model comparisons exist for classification; a controlled psychophysics study on benchmark small-object detection with protocol-matched scoring is missing.
- **Minimal Experiment:** Psychophysics study (n≈20) on sampled benchmark images with zoom allowed; score humans with the same matching rules as models; compare recall/precision by size.
- **Main Risk:** Humans bring open-world priors that models trained on the closed vocabulary lack, complicating fairness of the comparison.
- **Research Cluster:** SMALL-OBJ / PHENOMENON

### IDEA-B-0040 — Negative result: learned feature super-resolution fails to beat input upsampling
- **One-sentence idea:** Rigorously test whether feature-space super-resolution modules for small objects beat simple input upsampling at matched inference compute.
- **Problem:** A line of work adds learned feature-SR modules for small objects, but baselines rarely include the trivially available alternative — spending the same compute on larger inputs.
- **Core Hypothesis (falsifiable):** At matched latency/FLOPs, plain input upsampling matches or exceeds published feature-SR modules on AP_small across multiple detector families.
- **Why Important:** If confirmed, it deflates a module genre and establishes compute-matched input scaling as the mandatory baseline for the area.
- **Why Possibly Novel:** The compute-matched comparison against input scaling is systematically absent from the module papers; making the negative result the paper is the contribution.
- **Minimal Experiment:** Re-implement 3–4 feature-SR modules from public code; construct latency-matched input-upsampling baselines; evaluate on COCO and one aerial benchmark with seed replication.
- **Main Risk:** "Matched compute" is contestable (memory vs. FLOPs vs. latency), and module authors may dispute the accounting.
- **Research Cluster:** SMALL-OBJ / NEG-RESULT

### IDEA-B-0041 — Boundary losses fit annotator style, not true edges
- **One-sentence idea:** Test whether boundary-loss gains persist when evaluated against independent re-annotations rather than the same annotator distribution the model trained on.
- **Problem:** Boundary-aware losses improve boundary metrics computed on GT from the same annotation pipeline; they may be learning the annotators' tracing habits rather than physical object boundaries.
- **Core Hypothesis (falsifiable):** The boundary-metric gains of boundary losses shrink by more than half when evaluated on independently re-annotated boundaries, while interior-region gains are unaffected.
- **Why Important:** Distinguishes genuine boundary understanding from stylistic overfitting, which determines whether these methods transfer across datasets and annotation vendors.
- **Why Possibly Novel:** Cross-annotator evaluation of boundary-specific methods has not been performed; boundary work always evaluates against the native GT.
- **Minimal Experiment:** Collect dual-annotation boundaries for a benchmark subset; evaluate boundary-loss and baseline models against both annotation sets; compare gain retention.
- **Main Risk:** Independent annotations are expensive, and their own noise must be sub-dominant for the comparison to be conclusive.
- **Research Cluster:** BOUNDARY / EVAL-WEAK

### IDEA-B-0042 — Boundary-metric gains concentrate in high-curvature regions
- **One-sentence idea:** Decompose boundary-quality improvements by local curvature to test whether methods differ only at corners and protrusions.
- **Problem:** Boundary metrics aggregate over all boundary pixels, but straight-edge segments may be saturated for all modern methods, hiding that competition happens only in a small high-curvature subset.
- **Core Hypothesis (falsifiable):** Over 70% of the boundary-F difference between representative methods comes from the top curvature quintile of boundary pixels, and straight-segment performance is statistically indistinguishable across methods.
- **Why Important:** Would refocus boundary research on the actual contested regime (corners, thin protrusions) and enable much cheaper targeted evaluation.
- **Why Possibly Novel:** Curvature-stratified boundary evaluation has not been used as a comparative lens across methods.
- **Minimal Experiment:** Compute per-boundary-pixel curvature on GT; stratify boundary-F differences of several public models by curvature quintile.
- **Main Risk:** Curvature estimation on discrete masks is noisy at exactly the high-curvature regions of interest.
- **Research Cluster:** BOUNDARY / EVAL-WEAK

### IDEA-B-0043 — Segmentation models share a universal inward-bias at boundaries
- **One-sentence idea:** Measure the signed boundary displacement of many segmentation models to test for a universal systematic bias (under- vs. over-segmentation) and identify its cause.
- **Problem:** Boundary error is always reported unsigned; if models systematically place boundaries inside the true object (e.g., due to background pixel majority), a zero-cost global correction exists and error analyses are misinterpreting noise as variance.
- **Core Hypothesis (falsifiable):** Across architectures and datasets, the mean signed displacement of predicted boundaries is significantly negative (inward), with magnitude correlated to local class pixel-frequency imbalance, and a single learned offset per class removes most of it.
- **Why Important:** A universal bias with a one-parameter fix would be an embarrassing and valuable discovery about the entire field's outputs.
- **Why Possibly Novel:** Signed displacement distributions across model families have not been published; boundary work jumps straight to unsigned scores.
- **Minimal Experiment:** For 10+ public models, compute signed distance from predicted to GT boundaries along normals; test the sign, cross-model consistency, and the frequency-imbalance correlation; apply per-class dilation correction and re-score.
- **Main Risk:** Annotator bias (IDEA-B-0062) may be the true source, in which case the "correction" fits GT style rather than reality.
- **Research Cluster:** BOUNDARY / PHENOMENON

### IDEA-B-0044 — Mask label downsampling policy is a hidden driver of boundary results
- **One-sentence idea:** Quantify how the choice of label downsampling/interpolation during training (nearest vs. area vs. ignore-band) affects boundary metrics relative to celebrated method differences.
- **Problem:** Training pipelines downsample masks to output stride with library-default interpolation, an undocumented choice that directly corrupts boundary supervision but is never reported in papers.
- **Core Hypothesis (falsifiable):** Across common frameworks' defaults, the boundary-F spread induced by label-resizing policy alone exceeds 50% of the typical gap between competing published boundary-focused methods.
- **Why Important:** If a silent preprocessing default rivals method effects, the boundary literature's comparisons need re-examination and papers need to report the setting.
- **Why Possibly Novel:** Implementation-detail audits exist for detection recipes; the mask-resizing pathway specifically has escaped scrutiny despite touching every experiment.
- **Minimal Experiment:** Train matched segmenters varying only label-resize policy; report interior and boundary metrics; survey defaults across popular codebases.
- **Main Risk:** Effect size may vary strongly with output stride, requiring a stride-crossed design to characterize honestly.
- **Research Cluster:** BOUNDARY / EVAL-WEAK

### IDEA-B-0045 — Did CRF post-processing die for the right reason?
- **One-sentence idea:** Re-evaluate classical CRF/filtering post-processing on modern architectures using boundary-sensitive metrics to test whether it was abandoned because it stopped helping or because evaluation stopped seeing its help.
- **Problem:** CRFs vanished from segmentation pipelines around the time evaluation emphasis settled on region IoU; whether modern models genuinely subsume CRF's boundary benefits is an assumption, not a measurement.
- **Core Hypothesis (falsifiable):** On modern segmenters, CRF post-processing still improves boundary-F and human-judged edge quality significantly despite negligible mIoU change, meaning its abandonment reflects metric insensitivity rather than obsolescence.
- **Why Important:** If true, a zero-training, well-understood tool has been prematurely discarded for boundary-critical applications (matting, medical, mapping).
- **Why Possibly Novel:** Nobody has run the "was the folklore right?" study with boundary metrics and human evaluation on current-generation models.
- **Minimal Experiment:** Apply tuned dense-CRF to outputs of several modern segmenters; report mIoU, boundary-F, and a small human preference study on boundary quality.
- **Main Risk:** CRF hyperparameters tuned per dataset could overfit, requiring honest cross-validation to keep the claim clean.
- **Research Cluster:** BOUNDARY / ASSUMPTION / NEG-RESULT

### IDEA-B-0046 — Output-stride choices masquerade as architectural boundary progress
- **One-sentence idea:** Re-run representative segmentation architectures from several eras at equalized output stride to measure how much reported boundary progress reflects stride policy rather than architecture.
- **Problem:** Architectures across the literature use different effective output strides and upsampling schemes, which dominate boundary behavior; era-over-era boundary improvements may partly be stride bookkeeping.
- **Core Hypothesis (falsifiable):** At equalized output stride and upsampling, the boundary-F spread between old and new architecture families shrinks by at least half relative to their published configurations.
- **Why Important:** Correct attribution of progress determines what the field should keep investing in — decoder resolution engineering vs. representational advances.
- **Why Possibly Novel:** Controlled-stride architecture comparisons across generations, with boundary-specific reporting, have not been published.
- **Minimal Experiment:** Train FCN/DeepLab/SegFormer/Mask2Former-class models under one harness at matched stride; report interior vs. boundary metric progressions.
- **Main Risk:** Some architectures cannot honestly run at other strides without distorting their design intent.
- **Research Cluster:** BOUNDARY / EVAL-WEAK

### IDEA-B-0047 — Estimate each dataset's irreducible boundary noise floor
- **One-sentence idea:** Use multi-annotator disagreement to estimate a per-dataset boundary-accuracy noise floor and test whether current SOTA has already reached it.
- **Problem:** Boundary benchmarks are treated as having unbounded headroom, but annotator disagreement defines a floor below which "improvement" is fitting one annotator's style over another's.
- **Core Hypothesis (falsifiable):** On mature benchmarks (e.g., Cityscapes-quality data), SOTA boundary-F is within the inter-annotator disagreement band, implying no measurable headroom without better GT.
- **Why Important:** Declaring saturation, where real, stops wasted effort and motivates investment in evaluation data rather than methods.
- **Why Possibly Novel:** Noise floors are estimated in medical imaging via multi-rater studies but have not been systematically ported to mainstream segmentation benchmarks as a saturation test.
- **Minimal Experiment:** Multi-annotate boundary bands on benchmark subsets; compute annotator-vs-annotator boundary-F distribution; place current SOTA models within it.
- **Main Risk:** Recruited annotators may be noisier than the original professional pipelines, overestimating the floor.
- **Research Cluster:** BOUNDARY / EVAL-WEAK

### IDEA-B-0048 — Hard-label training makes calibrated soft boundaries impossible
- **One-sentence idea:** Test whether models trained on hard mask labels are structurally unable to represent boundary ambiguity, by comparing against training on soft (alpha-like or multi-rater) boundary targets at matched accuracy.
- **Problem:** Physical boundaries under blur/mixed pixels are genuinely soft, but hard 0/1 supervision forces arbitrary hardening, which should surface as boundary overconfidence.
- **Core Hypothesis (falsifiable):** Models trained with soft boundary targets show substantially better boundary-zone calibration (confidence matching pixel mixing ratios) at equal region accuracy, and hard-label models cannot be recalibrated to match post hoc.
- **Why Important:** Boundary confidence drives downstream fusion (matting, AR, mapping); if hard labels destroy it irreversibly, supervision formats need to change.
- **Why Possibly Novel:** Matting and segmentation are separate communities; the calibration-at-boundaries consequence of hard supervision has not been isolated as a falsifiable claim.
- **Minimal Experiment:** Construct soft boundary targets from high-res GT downsampling (exact mixing ratios); train matched models on hard vs. soft targets; compare boundary-zone reliability diagrams and post-hoc recalibration limits.
- **Main Risk:** Soft-target gains could come from label smoothing side effects rather than genuine ambiguity representation; needs smoothing-matched controls.
- **Research Cluster:** BOUNDARY / CALIBRATION

### IDEA-B-0049 — Learned boundary-refinement branches are re-inventing classical edge detection
- **One-sentence idea:** Test whether learned boundary branches can be replaced by fixed classical edge evidence (zero learned parameters) without losing their reported gains.
- **Problem:** Many segmentation methods attach boundary-prediction branches whose gains are attributed to learned semantics, but the branch may only inject generic edge information that a fixed filter bank already provides.
- **Core Hypothesis (falsifiable):** Substituting the learned boundary branch's input contribution with fixed multi-scale classical edge maps retains most (>75%) of the boundary-metric gain across several such architectures.
- **Why Important:** If a fixed prior suffices, the community can stop training boundary branches and papers must demonstrate value beyond classical edge evidence.
- **Why Possibly Novel:** The "replace learned module with fixed classical equivalent" falsification test is rarely applied, and never systematically to boundary branches.
- **Minimal Experiment:** Take 3 public boundary-branch architectures; swap branch outputs for Sobel/structured-edge maps (calibrated); retrain heads only; compare boundary metrics.
- **Main Risk:** Integration details (feature scale, normalization) may unfairly handicap the fixed substitute, requiring good-faith tuning of the baseline.
- **Research Cluster:** BOUNDARY / NEG-RESULT

### IDEA-B-0050 — Polygon GT induces measurable straight-line bias in model outputs
- **One-sentence idea:** Detect and quantify polygonal artifacts in the curvature spectrum of model predictions trained on polygon-annotated data, using synthetic smooth-shape probes.
- **Problem:** If models inherit the piecewise-linear geometry of polygon annotations, their outputs systematically distort curved boundaries — a dataset-format fingerprint contaminating all downstream uses.
- **Core Hypothesis (falsifiable):** Models trained on polygon GT reproduce ellipses/circles with measurably flattened curvature spectra (excess low-curvature segments and corner clusters) relative to models trained on pixel-accurate GT of the same scenes.
- **Why Important:** Demonstrates that annotation format, not just annotation accuracy, propagates into model geometry — relevant to every polygon-annotated dataset in use.
- **Why Possibly Novel:** Annotation-format effects on the geometry of model outputs (as opposed to their accuracy) have not been characterized.
- **Minimal Experiment:** Insert synthetic smooth shapes into real images; compare predicted-boundary curvature spectra between models trained on polygon vs. pixel GT; quantify polygonality indices.
- **Main Risk:** Networks' own output-stride smoothing may mask or mimic polygonal artifacts, requiring careful spectral separation.
- **Research Cluster:** BOUNDARY / PHENOMENON

### IDEA-B-0051 — Boundary refinement transfers worse than interior segmentation
- **One-sentence idea:** Test whether boundary-refinement gains are dataset-specific (annotation-style-locked) by measuring cross-dataset transfer of boundary vs. interior improvements separately.
- **Problem:** If boundary modules fit annotation style (IDEA-B-0041), their gains should evaporate across datasets even when semantic transfer succeeds — but transfer studies never decompose by region.
- **Core Hypothesis (falsifiable):** Under cross-dataset evaluation (train A, test B), interior IoU gains of boundary-refinement methods are largely retained while boundary-F gains drop to near zero, and the drop correlates with distance between the datasets' annotation-style statistics.
- **Why Important:** Practitioners deploying across data sources need to know boundary quality claims may be non-portable; it also gives a concrete measurable definition of "annotation style."
- **Why Possibly Novel:** Region-decomposed transfer analysis is new; annotation-style distance as a predictive covariate is new.
- **Minimal Experiment:** Train boundary-refinement and baseline models on Cityscapes/ADE/COCO; cross-evaluate all pairs; decompose gain retention into interior vs. boundary bands.
- **Main Risk:** Cross-dataset label-space mismatches complicate clean region decomposition.
- **Research Cluster:** BOUNDARY / GENERALIZATION

### IDEA-B-0052 — Boundary difficulty is predictable from image statistics alone
- **One-sentence idea:** Build and validate a model-free boundary-difficulty map (from local contrast, texture, blur) that predicts where any segmenter's boundary errors will occur.
- **Problem:** Boundary errors are treated as model-specific, but if they are largely determined by image-level evidence quality, a universal difficulty map exists — useful for evaluation weighting, annotation triage, and uncertainty priors.
- **Core Hypothesis (falsifiable):** A regressor from purely local image statistics predicts per-pixel boundary error of unseen models on unseen datasets with high rank correlation, and residual model-specific error is a small fraction of total variance.
- **Why Important:** Would show most boundary error is evidence-limited rather than model-limited, redefining what boundary "improvement" can mean.
- **Why Possibly Novel:** Difficulty prediction exists at image level; a model-agnostic pixel-level boundary-difficulty account validated across model families is new.
- **Minimal Experiment:** Fit the statistic-based predictor on errors of 3 models on one dataset; test rank correlation on 5 unseen models and 2 unseen datasets.
- **Main Risk:** Shared training data among "unseen" models could inflate apparent universality.
- **Research Cluster:** BOUNDARY / UNCERTAINTY

### IDEA-B-0053 — Multi-stage refinement saturates after one stage
- **One-sentence idea:** Replicate cascaded/iterative boundary-refinement methods to test whether stages beyond the first contribute anything outside seed noise.
- **Problem:** Iterative refinement papers report per-stage gains, but later-stage improvements are small and rarely accompanied by variance estimates.
- **Core Hypothesis (falsifiable):** Across public multi-stage refinement methods, stage-2+ gains are statistically indistinguishable from zero under seed replication, while stage-1 gains are robust.
- **Why Important:** Refinement stages cost inference latency; establishing the saturation point trims deployed models and disciplines the genre's reporting.
- **Why Possibly Novel:** Nobody has run the seed-replicated per-stage significance audit across the refinement literature.
- **Minimal Experiment:** Rerun 3–4 open-source iterative refinement methods with 5 seeds each; report per-stage deltas with CIs.
- **Main Risk:** One genuinely non-saturating method would complicate the headline, though the audit remains valuable.
- **Research Cluster:** BOUNDARY / NEG-RESULT

### IDEA-B-0054 — IoU is blind to thin structures; skeleton recall re-ranks methods
- **One-sentence idea:** Show that region-overlap metrics assign negligible weight to thin structures (poles, wires, limbs) and that skeleton-based recall changes method rankings on standard benchmarks.
- **Problem:** A wire crossing an image contributes almost nothing to IoU, so models can drop entire thin objects with minimal metric penalty — likely shaping what architectures have learned to ignore.
- **Core Hypothesis (falsifiable):** On existing benchmarks, per-method thin-structure skeleton recall varies widely among models with near-identical mIoU, and thin-structure-weighted rankings disagree materially with mIoU rankings.
- **Why Important:** Thin structures are safety-critical (wires for drones, poles for driving); a metric that cannot see them corrupts the field's incentive structure.
- **Why Possibly Novel:** Skeleton metrics exist in medical vessel segmentation; porting them as a re-ranking audit of mainstream benchmarks is new.
- **Minimal Experiment:** Extract thin-structure subsets from Cityscapes/ADE GT via skeleton-width analysis; re-score public models; compare rankings.
- **Main Risk:** GT for thin structures is itself unreliable (annotation floors), interacting with IDEA-B-0037.
- **Research Cluster:** BOUNDARY / EVAL-WEAK

### IDEA-B-0055 — Inference-time interpolation choices rival published boundary gains
- **One-sentence idea:** Quantify the boundary-metric variation caused solely by logit upsampling method (bilinear/bicubic/nearest, align-corners flags) across frameworks.
- **Problem:** The final logit-to-full-resolution interpolation is an invisible implementation choice, but at object boundaries it directly determines pixel assignments.
- **Core Hypothesis (falsifiable):** Switching interpolation settings on identical trained weights changes boundary-F by an amount comparable to typical published boundary-method gains, while mIoU changes negligibly.
- **Why Important:** Another "nuisance parameter exceeds effect size" audit that boundary papers must control for; immediately actionable for fair comparison.
- **Why Possibly Novel:** Align-corners bugs are known anecdotes; a systematic effect-size comparison against the method literature is not published.
- **Minimal Experiment:** Evaluate 10 public checkpoints under a grid of interpolation settings; tabulate boundary-F spreads vs. a survey of published method gains.
- **Main Risk:** Modern codebases may have converged on one setting, shrinking the observed spread (a useful null).
- **Research Cluster:** BOUNDARY / EVAL-WEAK

### IDEA-B-0056 — Dice loss trades boundary precision for region recall by construction
- **One-sentence idea:** Derive and empirically verify the systematic boundary bias (over-segmentation of small structures) implied by Dice-family losses' gradient geometry.
- **Problem:** Dice loss is the default in medical segmentation, chosen for class-imbalance robustness, but its gradient structure implies predictable boundary placement biases nobody validates.
- **Core Hypothesis (falsifiable):** The signed boundary displacement of Dice-trained models is systematically outward for small structures and the effect scales as predicted by the derived gradient ratio, while cross-entropy-trained models show a different, also-predicted, signature.
- **Why Important:** Medical measurements (tumor diameters, volumes) are downstream of these biases; a validated prediction converts loss choice from folklore to engineering.
- **Why Possibly Novel:** Dice vs. CE comparisons are empirical horse races; a derived-then-verified mechanistic bias signature is a different kind of result.
- **Minimal Experiment:** Derive per-pixel gradient magnitudes near boundaries for both losses; train matched models on controlled synthetic and medical data; compare signed displacement distributions against predictions.
- **Main Risk:** Optimizer dynamics and augmentation could swamp the derived first-order effect.
- **Research Cluster:** BOUNDARY / PHENOMENON

### IDEA-B-0057 — Boundary uncertainty is anisotropic: uncertain along the normal, confident along the tangent
- **One-sentence idea:** Decompose boundary prediction uncertainty into normal and tangential components and test whether current UQ methods misrepresent the anisotropy.
- **Problem:** Pixelwise uncertainty maps treat boundary uncertainty isotropically, but the true ambiguity is almost entirely "where along the normal," suggesting current representations waste and distort uncertainty information.
- **Core Hypothesis (falsifiable):** Empirical boundary error distributions are strongly anisotropic (normal variance >> tangential variance), and a 1-D normal-displacement uncertainty parameterization achieves better calibration per bit than pixelwise entropy maps.
- **Why Important:** Downstream consumers (tracking, fusion, human review) act on boundary uncertainty; a representation matched to the true error geometry improves all of them.
- **Why Possibly Novel:** Contour-based uncertainty exists in level-set traditions; the explicit anisotropy measurement and bit-efficiency comparison against dense UQ is new.
- **Minimal Experiment:** For public models, estimate error displacement fields along GT normals/tangents; fit both uncertainty representations on held-out data; compare calibration and information content.
- **Main Risk:** Junctions and thin structures break the normal-direction parameterization and need principled handling.
- **Research Cluster:** BOUNDARY / UNCERTAINTY

### IDEA-B-0058 — Same-class instance boundaries and class boundaries fail differently
- **One-sentence idea:** Separate boundary errors between different-class transitions and same-class instance transitions to show they arise from different mechanisms needing different fixes.
- **Problem:** "Boundary error" is reported as one number, but the boundary between two cars touching involves instance evidence (shading, geometry) while car-road boundaries involve class evidence (semantics, texture) — conflating them hides mechanism.
- **Core Hypothesis (falsifiable):** Error rates, error signatures (displacement vs. deletion), and responses to interventions (contrast augmentation vs. semantic pretraining) differ significantly between the two boundary types across models.
- **Why Important:** Method development targets "boundaries" generically; a validated taxonomy would let interventions be matched to the failing mechanism.
- **Why Possibly Novel:** Panoptic metrics distinguish things/stuff but no analysis splits boundary error by transition type as a mechanistic probe.
- **Minimal Experiment:** Partition GT boundaries by transition type on panoptic datasets; profile per-type errors for several models; test differential response to two targeted interventions.
- **Main Risk:** Same-class instance boundaries are rarer and noisier in GT, limiting statistical power.
- **Research Cluster:** BOUNDARY / PHENOMENON

### IDEA-B-0059 — Benchmarks penalize correctly-blurry boundaries on motion-blurred inputs
- **One-sentence idea:** Test whether models predicting soft/uncertain boundaries on genuinely blurred image regions are penalized by hard-GT evaluation, distorting incentives toward false crispness.
- **Problem:** GT boundaries are drawn crisp even where the image evidence is blurred; evaluation therefore rewards hallucinated sharpness and punishes honest ambiguity.
- **Core Hypothesis (falsifiable):** On motion-blurred regions, models with sharper (more confident) boundaries score better on standard metrics while scoring worse on multi-annotator-agreement and downstream-fusion measures, demonstrating a metric-incentive inversion.
- **Why Important:** Deployed systems (AR compositing, video editing) suffer from falsely crisp boundaries; the inversion means benchmarks actively select for the failure.
- **Why Possibly Novel:** Blur-region-conditional analysis of the crispness incentive has not been articulated or measured.
- **Minimal Experiment:** Identify blurred boundary zones via local blur estimation; compare model rankings on standard vs. soft-GT (multi-rater or alpha) evaluation within those zones.
- **Main Risk:** Obtaining trustworthy soft GT for blurred zones is hard; may need controlled capture with ground-truth motion.
- **Research Cluster:** BOUNDARY / EVAL-WEAK

### IDEA-B-0060 — Demosaicing sets a physical floor on boundary accuracy
- **One-sentence idea:** Estimate the boundary-localization floor imposed by Bayer demosaicing and ISP sharpening, and test whether SOTA models already operate at this sensor-imposed limit.
- **Problem:** Every camera image's edges are partially synthesized by the ISP; sub-pixel boundary research may be competing against artifacts rather than optics, without anyone quantifying the floor.
- **Core Hypothesis (falsifiable):** Boundary localization error against RAW-derived ground truth has a floor (dependent on demosaicing algorithm) that current models approach within a small margin on high-quality data, and ISP choice shifts model boundary error predictably.
- **Why Important:** Defines the physically meaningful precision target for boundary research and adds ISP as an ignored experimental variable.
- **Why Possibly Novel:** ISP effects are studied for detection robustness; a boundary-localization floor analysis tied to demosaicing is new.
- **Minimal Experiment:** Capture RAW scenes with known geometry (calibration targets, straight edges); process through multiple ISPs; measure model boundary error against geometric truth per ISP.
- **Main Risk:** Constructing geometric boundary truth for natural objects (beyond targets) is difficult, possibly limiting scope to semi-synthetic scenes.
- **Research Cluster:** BOUNDARY / PHENOMENON

### IDEA-B-0061 — Annotators trace boundaries with a luminance-dependent bias
- **One-sentence idea:** Audit whether human annotators systematically place boundaries toward the darker side of edges, contaminating GT with a correctable photometric bias.
- **Problem:** Perceptual edge localization in humans is known to depend on local contrast polarity; if annotators inherit this, all GT shares a directional bias that models learn and metrics enforce.
- **Core Hypothesis (falsifiable):** Across datasets, GT boundary positions deviate from physically calibrated edges (from RAW gradients or depth discontinuities) with a sign that correlates with local luminance polarity, and models trained on this GT reproduce the bias.
- **Why Important:** A dataset-wide directional bias would matter for measurement applications (medical, mapping) and would be correctable once characterized.
- **Why Possibly Novel:** Annotator-bias studies cover class labels and saliency; a photometric boundary-placement bias audit is unexplored.
- **Minimal Experiment:** Compare GT boundary positions against gradient-maximum and depth-edge references on datasets with aligned depth/LiDAR; regress signed offsets on luminance polarity.
- **Main Risk:** The "physical reference" definition is contestable; multiple references must agree for the claim to stand.
- **Research Cluster:** BOUNDARY / ANNOT-EFF / PHENOMENON

### IDEA-B-0062 — Students can exceed teachers at boundaries under soft-label distillation
- **One-sentence idea:** Test whether distillation with soft spatial logits transfers super-teacher boundary information (ensemble-like averaging of the teacher's boundary noise) enabling students to localize better than their teacher.
- **Problem:** Distillation is assumed to upper-bound students at teacher quality; but if teacher boundary errors are noise-like across augmented views, the distillation average could be sharper than any single teacher pass.
- **Core Hypothesis (falsifiable):** Students distilled from multi-view-averaged teacher logits exceed the single-pass teacher's boundary-F on held-out data, while interior accuracy remains at or below teacher level.
- **Why Important:** Would identify a free boundary-quality amplifier in standard pipelines and clarify what information distillation actually transfers at spatial detail.
- **Why Possibly Novel:** "Student surpasses teacher" reports exist for classification robustness; a boundary-specific mechanism via view-averaged targets is untested.
- **Minimal Experiment:** Distill matched students from single-pass vs. K-view-averaged teacher logits; compare boundary-F against the teacher across datasets.
- **Main Risk:** View averaging may blur genuinely sharp teacher boundaries, canceling the effect it aims to exploit.
- **Research Cluster:** BOUNDARY / PHENOMENON

### IDEA-B-0063 — Zoomed annotation creates scale-inconsistent boundary precision within images
- **One-sentence idea:** Detect whether annotation-tool zoom behavior produces GT whose boundary precision varies with object size in ways models then inherit.
- **Problem:** Annotators zoom in for small objects and out for large ones, plausibly producing relatively more precise boundaries on small structures — an inconsistency that shapes both training and evaluation invisibly.
- **Core Hypothesis (falsifiable):** GT boundary precision (measured via re-annotation agreement) as a function of object size follows a non-monotonic profile inconsistent with constant pixel precision, and model boundary errors track the GT profile rather than image evidence quality.
- **Why Important:** Shows benchmark boundary numbers encode tool ergonomics, and provides a size-dependent correction for fair evaluation.
- **Why Possibly Novel:** Zoom-protocol effects on GT precision have never been measured despite being mechanically inevitable.
- **Minimal Experiment:** Re-annotate objects across the size spectrum under controlled zoom protocols; compare agreement profiles; correlate model error profiles against GT-precision profiles.
- **Main Risk:** Original tools/protocols vary by dataset; conclusions may need dataset-specific qualification.
- **Research Cluster:** BOUNDARY / ANNOT-EFF

### IDEA-B-0064 — Boundary metrics don't predict downstream task success
- **One-sentence idea:** Measure the correlation between boundary-F/IoU and actual downstream utility (grasp success, clinical measurement error, AR compositing preference) to test whether boundary metrics rank models correctly for use.
- **Problem:** Boundary metrics are proxies; robotics, medical, and AR consumers care about task outcomes, and the proxy-task correlation above a quality threshold is assumed rather than known.
- **Core Hypothesis (falsifiable):** Above a moderate quality threshold, boundary-F differences between models explain little variance in downstream task outcomes, and task-specific error weightings (e.g., only the graspable rim matters) reorder models.
- **Why Important:** If proxies decouple from utility, model selection for deployment is currently mis-optimized across several industries.
- **Why Possibly Novel:** Metric-utility validation studies are common in medical imaging for region metrics but absent for boundary metrics across tasks.
- **Minimal Experiment:** Take 6 segmenters spanning boundary quality; run a simulated grasping benchmark, a lesion-measurement protocol, and a human AR-compositing preference study; correlate outcomes with metrics.
- **Main Risk:** Each downstream task adds its own pipeline noise, requiring large samples to resolve correlations.
- **Research Cluster:** BOUNDARY / EVAL-WEAK

### IDEA-B-0065 — Segmentation networks are low-pass filters with a measurable cutoff
- **One-sentence idea:** Characterize each architecture's boundary behavior as an effective spatial low-pass filter and test whether a single cutoff-frequency parameter predicts its boundary errors.
- **Problem:** Boundary error analyses are anecdotal; if a model's contour output is well-described by frequency-domain attenuation, a compact transferable descriptor of boundary capability exists.
- **Core Hypothesis (falsifiable):** Predicted contours' curvature spectra relative to GT show architecture-specific attenuation curves stable across datasets, and the fitted cutoff predicts per-object boundary-F from GT shape spectra alone with high accuracy.
- **Why Important:** A one-number boundary capability index would enable principled architecture selection and honest reporting ("this model cannot represent detail below X px wavelength").
- **Why Possibly Novel:** Frequency analyses exist for CNN receptive fields; treating trained segmenters as measurable contour filters with validated predictive power is new.
- **Minimal Experiment:** Compute GT-vs-predicted contour spectra for many models across two datasets; fit attenuation curves; validate error predictions on held-out shape classes.
- **Main Risk:** Nonlinear, class-dependent behavior may defeat any single-filter summary (an informative failure, but weaker).
- **Research Cluster:** BOUNDARY / PHENOMENON

### IDEA-B-0066 — Boundary quality degrades with distance from image center
- **One-sentence idea:** Measure spatial position dependence of boundary accuracy and attribute it among lens distortion, resolution falloff, dataset composition bias, and padding effects.
- **Problem:** Evaluation averages over image space, but optics and photographer framing make image corners statistically different; any position-dependent boundary degradation is currently invisible and unattributed.
- **Core Hypothesis (falsifiable):** Boundary-F declines measurably from center to corners on standard benchmarks, and the decline persists after controlling for object class and size (implicating optics/padding rather than content).
- **Why Important:** Full-frame deployment (driving, mapping) uses the periphery; a systematic peripheral deficit would be a hidden safety factor and an evaluation blind spot.
- **Why Possibly Novel:** Position-conditional performance auditing exists for detection center bias, but boundary quality vs. field position with causal attribution has not been done.
- **Minimal Experiment:** Stratify boundary metrics by radial position across models/datasets; use undistorted vs. distorted variants and padding ablations to attribute the effect.
- **Main Risk:** Content confounds (peripheral objects differ) may resist full statistical control.
- **Research Cluster:** BOUNDARY / EVAL-WEAK

### IDEA-B-0067 — Fixed-size mask heads impose object-size-proportional boundary error
- **One-sentence idea:** Verify that RoI-based mask heads (fixed 28x28-style grids) produce boundary error growing linearly with object size, making head resolution, not the backbone, the binding constraint for large-object boundaries.
- **Problem:** Mask R-CNN-style heads predict masks on a fixed grid regardless of object size; the implied boundary quantization error is simple arithmetic but never verified as the dominant error source or bounded against backbone contributions.
- **Core Hypothesis (falsifiable):** For large objects, measured boundary error tracks the grid-resolution prediction (proportional to object size / grid size) and is largely eliminated by increasing head resolution alone, with backbone changes contributing marginally.
- **Why Important:** Cleanly attributes a major error component to a cheap-to-fix design choice, refocusing "better masks" research away from expensive backbone work for this regime.
- **Why Possibly Novel:** High-res mask heads exist as engineering, but the quantitative attribution study (predicted vs. measured error scaling) has not been published.
- **Minimal Experiment:** Plot per-object boundary error vs. size for fixed-grid models against the arithmetic prediction; retrain with 2x/4x head resolution only; re-plot.
- **Main Risk:** RoIAlign interpolation partially mitigates quantization, so the arithmetic bound may be loose in a way that weakens the attribution.
- **Research Cluster:** BOUNDARY / REP-MISMATCH

### IDEA-B-0068 — Can models extrapolate boundaries they never saw? The eroded-label probe
- **One-sentence idea:** Train on systematically eroded masks and test whether models recover true boundaries, distinguishing "boundary placement is learned from evidence" from "boundary placement is copied from labels."
- **Problem:** Whether segmentation models locate boundaries using image evidence or simply reproduce label statistics is fundamental but untested; the two theories predict different behavior under label perturbation.
- **Core Hypothesis (falsifiable):** Models trained on k-pixel-eroded masks predict boundaries displaced by significantly less than k (partial evidence-driven recovery), with recovery fraction depending on local edge strength — while the label-copying theory predicts full displacement k everywhere.
- **Why Important:** Establishes how much boundary supervision quality actually matters, informing annotation-budget decisions (interacts with IDEA-B-0152) and the interpretation of all boundary metrics.
- **Why Possibly Novel:** Label-perturbation training exists for noise robustness studies; using calibrated erosion as a mechanistic probe of evidence-vs-label reliance is new.
- **Minimal Experiment:** Train models on masks eroded by k∈{1,2,4,8} px; measure signed displacement of predictions vs. both eroded and true boundaries; stratify by edge strength.
- **Main Risk:** Erosion changes region statistics (small structures vanish), confounding the boundary-specific conclusion; dilation and mixed controls needed.
- **Research Cluster:** BOUNDARY / ASSUMPTION

### IDEA-B-0069 — Temporal boundary jitter predicts per-frame boundary quality without GT
- **One-sentence idea:** Validate the frame-to-frame instability of predicted boundaries in video as an unsupervised estimator of boundary accuracy for deployment monitoring.
- **Problem:** Deployed systems cannot measure boundary quality without GT; if temporal jitter (after motion compensation) correlates strongly with GT boundary error, quality monitoring becomes free wherever video exists.
- **Core Hypothesis (falsifiable):** Motion-compensated boundary jitter correlates with per-frame boundary-F at rank correlation above 0.7 across models and domains, and the correlation survives domain shift better than confidence-based estimators.
- **Why Important:** Provides a practical GT-free quality signal and, scientifically, tests whether boundary errors are stable model properties or stochastic per-frame events.
- **Why Possibly Novel:** Temporal consistency is used as a training regularizer; its validation as a calibrated quality estimator against GT is missing.
- **Minimal Experiment:** On video segmentation benchmarks with dense GT, compute jitter-vs-boundary-F correlations for several models, in-domain and under corruption shifts; compare against softmax-confidence baselines.
- **Main Risk:** Systematic (consistent) boundary errors are invisible to jitter, bounding achievable correlation.
- **Research Cluster:** BOUNDARY / UNCERTAINTY

### IDEA-B-0070 — Boundary-ownership errors follow class-prior occlusion statistics
- **One-sentence idea:** Test whether models assign ambiguous boundary pixels according to learned occlusion-order priors (which class tends to be in front) rather than image evidence.
- **Problem:** At contact boundaries the owning class is ambiguous; if models resolve ambiguity by dataset co-occurrence priors, they will make systematic, predictable errors when the priors are violated.
- **Core Hypothesis (falsifiable):** On curated prior-violating cases (e.g., unusual occlusion orders), boundary-ownership errors flip in the direction predicted by dataset occlusion statistics significantly above chance, and the effect strength tracks the prior's strength per class pair.
- **Why Important:** Reveals a hidden relational prior in segmentation outputs, relevant for safety (novel scene configurations) and for understanding what dense models encode beyond appearance.
- **Why Possibly Novel:** Co-occurrence priors are studied for classification context bias; occlusion-order priors at boundary-pixel granularity are unexplored.
- **Minimal Experiment:** Mine dataset occlusion-order statistics per class pair; construct/collect violating test cases; measure directional ownership errors against prior predictions.
- **Main Risk:** Constructing convincing prior-violating imagery without synthesis artifacts is challenging.
- **Research Cluster:** BOUNDARY / GENERALIZATION

### IDEA-B-0071 — GT-free boundary scoring via superpixel alignment
- **One-sentence idea:** Validate boundary-to-superpixel alignment as a no-GT proxy for boundary quality, calibrated against GT metrics across models and datasets.
- **Problem:** Boundary evaluation requires expensive GT; low-level segmentation (superpixels) provides evidence-driven boundaries whose agreement with predictions might proxy quality well enough for triage and monitoring.
- **Core Hypothesis (falsifiable):** Alignment between predicted boundaries and classical superpixel boundaries rank-correlates with GT boundary-F above 0.6 across models, but the correlation collapses in textureless regions in a predictable, flaggable way.
- **Why Important:** A calibrated cheap proxy enables continuous quality tracking on unlabeled deployment data and cheap dataset-wide audits.
- **Why Possibly Novel:** Superpixels as evaluation instruments (rather than model components) with explicit validity-domain characterization is a fresh use.
- **Minimal Experiment:** Compute the proxy for many public models on labeled datasets; map correlation strength as a function of local texture; define and test a validity mask.
- **Main Risk:** Superpixel boundaries encode contrast, not semantics; the proxy may reward contrast-snapped errors.
- **Research Cluster:** BOUNDARY / EVAL-WEAK

### IDEA-B-0072 — Panoptic Quality can rise while boundary quality falls
- **One-sentence idea:** Demonstrate and quantify the anti-correlation regime where PQ improvements coexist with boundary degradation, using real model families rather than adversarial constructions.
- **Problem:** PQ's matching threshold (IoU>0.5) makes it insensitive to boundary detail once matches lock in; the community optimizes PQ assuming it summarizes mask quality.
- **Core Hypothesis (falsifiable):** Across training runs and model families, a measurable fraction of PQ improvements co-occur with boundary-F declines, and PQ's recognition term can be shown to dominate its quality term in practice.
- **Why Important:** If the field's headline panoptic metric is boundary-blind in practice (not just in theory), leaderboard progress may hide regression on a quality axis users care about.
- **Why Possibly Novel:** PQ critiques exist theoretically; an empirical prevalence study of the divergence in real training trajectories is new.
- **Minimal Experiment:** Log PQ and boundary-F across checkpoints of several panoptic models and across leaderboard submissions with public outputs; quantify divergence frequency and magnitude.
- **Main Risk:** Divergence may be rare in practice, yielding a mostly-null (still useful for validating PQ).
- **Research Cluster:** BOUNDARY / EVAL-WEAK

### IDEA-B-0073 — Boundary-region hard-example mining is mostly thin-object upweighting
- **One-sentence idea:** Decompose the gains of boundary-focused sampling/OHEM schemes to test whether they reduce to implicit upweighting of thin and small structures.
- **Problem:** Boundary-pixel oversampling improves benchmarks, credited to "boundary learning," but boundary pixels are disproportionately from thin/small objects, so the gain may be object-level reweighting in disguise.
- **Core Hypothesis (falsifiable):** Matching the object-size reweighting profile induced by boundary sampling — without any boundary-specific targeting — reproduces most (>70%) of its benchmark gains.
- **Why Important:** Correct mechanism attribution prevents the field from building on a misread effect and simplifies training recipes.
- **Why Possibly Novel:** The confound between boundary-pixel density and object thinness has not been noted or tested in the sampling literature.
- **Minimal Experiment:** Instrument the effective per-object weight distribution of boundary sampling; train a control with the same object-weight profile but uniform spatial sampling; compare gains.
- **Main Risk:** Partial mediation (some genuine boundary effect remains) will demand careful quantitative language.
- **Research Cluster:** BOUNDARY / ASSUMPTION

### IDEA-B-0074 — Query-based mask decoders improve regions, not boundaries
- **One-sentence idea:** Test whether the transformer mask-decoder generation (Mask2Former-class) improved boundary quality at all relative to per-pixel decoders at matched output stride.
- **Problem:** The narrative credits query-based decoding with better masks overall, but its architectural advantages (global reasoning, instance separation) target region-level errors; boundary detail may be unchanged or worse.
- **Core Hypothesis (falsifiable):** At matched backbone and output resolution, query-based decoders match per-pixel decoders on boundary-F within noise while exceeding them on region/recognition metrics, decomposing the generation's progress into recognition-only gains.
- **Why Important:** Guides decoder choice for boundary-critical applications and corrects the attribution of a major architectural transition.
- **Why Possibly Novel:** Head-to-head decoder comparisons at controlled resolution with boundary/interior decomposition have not been the object of a paper.
- **Minimal Experiment:** Train per-pixel and query-based decoders on identical frozen backbones at matched strides; decompose metric differences into interior vs. boundary bands.
- **Main Risk:** "Matched" configurations may handicap one family's intended operating point.
- **Research Cluster:** BOUNDARY / NEG-RESULT

### IDEA-B-0075 — The uncertainty map is mostly a boundary-distance map
- **One-sentence idea:** Quantify how much of pixelwise segmentation uncertainty is explained by distance-to-predicted-boundary alone, and isolate whatever interior uncertainty signal remains.
- **Problem:** Uncertainty maps are marketed as revealing model doubt, but softmax entropy is mechanically high at class transitions; the informative content beyond "near a boundary" is unmeasured.
- **Core Hypothesis (falsifiable):** A trivial predictor using only distance-to-boundary explains most of the variance of standard uncertainty maps, and after regressing it out, the residual uncertainty's error-prediction power (AUSE-style) drops by more than half for most UQ methods — but not for all, identifying which methods carry genuine interior signal.
- **Why Important:** Separates trivial from informative uncertainty, providing a mandatory baseline for the segmentation-UQ literature and a diagnostic for method development.
- **Why Possibly Novel:** The boundary-distance confound is occasionally mentioned but has never been made the quantitative centerpiece with a residualized evaluation protocol.
- **Minimal Experiment:** For MC-dropout, ensembles, and single-pass entropy on several datasets, fit distance-only predictors; report explained variance and residualized sparsification metrics per method.
- **Main Risk:** Distance-to-boundary is legitimately correlated with true error, so "trivial" and "informative" partly overlap; the analysis must handle shared variance carefully.
- **Research Cluster:** UNCERTAINTY / EVAL-WEAK

### IDEA-B-0076 — Deep ensembles' segmentation value is calibration, not accuracy
- **One-sentence idea:** Decompose deep-ensemble gains in segmentation into accuracy vs. uncertainty-quality components under accuracy-matched comparisons.
- **Problem:** Ensembles are the gold standard for segmentation UQ, but their headline superiority mixes two effects — slightly better predictions and better confidence — and the literature never separates them.
- **Core Hypothesis (falsifiable):** When a single model is accuracy-matched to an ensemble (via longer training or distillation), the ensemble's remaining advantage is almost entirely in calibration/error-detection metrics, not in mIoU.
- **Why Important:** If uncertainty is the only real ensemble benefit, cheap calibration methods compete directly with 5x-compute ensembles, changing deployment economics.
- **Why Possibly Novel:** Accuracy-matched decomposition of ensemble benefits has been done for classification in places, but not for dense prediction where spatial correlation changes the story.
- **Minimal Experiment:** Build accuracy-matched single models vs. 5-member ensembles on two segmentation datasets; report the full metric decomposition with seed CIs.
- **Main Risk:** Perfect accuracy matching is hard; small mismatches leak into the decomposition.
- **Research Cluster:** UNCERTAINTY / CALIBRATION

### IDEA-B-0077 — Where does each UQ method put its uncertainty mass?
- **One-sentence idea:** Build a spatial taxonomy (boundary / interior-ambiguity / OOD-object / label-noise zones) and profile which uncertainty methods allocate mass to which zone.
- **Problem:** UQ methods are compared by scalar metrics (ECE, AUSE) that hide where uncertainty lives; two methods with equal scores may be useful for completely different failure types.
- **Core Hypothesis (falsifiable):** UQ methods differ significantly and consistently in their zone allocation profiles (e.g., MC-dropout concentrates at boundaries while ensembles allocate more to OOD objects), and zone profiles predict which downstream task each method serves best.
- **Why Important:** Converts UQ method selection from leaderboard-following into requirement matching, and exposes blind zones shared by all methods.
- **Why Possibly Novel:** Zone-resolved profiling of uncertainty mass across methods is not an established evaluation; scalar comparisons dominate.
- **Minimal Experiment:** Construct zone labels on datasets with OOD insertions and multi-rater ambiguity annotations; compute per-zone uncertainty allocation for 6 UQ methods; test profile stability across datasets.
- **Main Risk:** Zone definitions involve judgment calls that could be contested; needs sensitivity analysis over definitions.
- **Research Cluster:** UNCERTAINTY / EVAL-WEAK

### IDEA-B-0078 — Segmentation ECE is an artifact of class imbalance and spatial correlation
- **One-sentence idea:** Show that standard pixelwise ECE conclusions invert under class-stratified and spatially-decorrelated estimation, and propose a statistically defensible protocol.
- **Problem:** Pixelwise ECE pools billions of correlated, imbalanced pixels; the resulting number is dominated by easy background and can rank methods opposite to their per-class or per-region calibration quality.
- **Core Hypothesis (falsifiable):** On standard benchmarks, method rankings by pooled pixel ECE disagree with rankings by class-balanced, autocorrelation-corrected ECE for a substantial fraction of method pairs.
- **Why Important:** Calibration claims in dense prediction ride on this metric; if it inverts under proper accounting, a chunk of the literature's conclusions are unreliable.
- **Why Possibly Novel:** ECE's binning pathologies are known for classification; the spatial-correlation and imbalance pathology specific to dense prediction has not been quantified with ranking-impact analysis.
- **Minimal Experiment:** Recompute calibration for public models under pooled vs. stratified/decorrelated estimators (block bootstrap); tabulate ranking flips and CI widths.
- **Main Risk:** There is no single "correct" estimator; the paper must defend its protocol against alternatives.
- **Research Cluster:** CALIBRATION / EVAL-WEAK

### IDEA-B-0079 — Per-image temperature beats global temperature: miscalibration is image-level
- **One-sentence idea:** Test whether segmentation miscalibration is primarily an image-difficulty effect (fixable by per-image temperature) rather than a global model bias.
- **Problem:** Post-hoc calibration fits one global temperature, implicitly assuming miscalibration is a model constant; if difficulty varies per image, global scaling under-corrects hard images and over-corrects easy ones simultaneously.
- **Core Hypothesis (falsifiable):** An oracle per-image temperature removes most (>70%) of residual calibration error left by global scaling, and a cheap image-difficulty predictor recovers most of the oracle's gain.
- **Why Important:** Locates miscalibration's structure (global vs. conditional), which dictates whether calibration research should target models or difficulty estimation.
- **Why Possibly Novel:** Conditional calibration exists in theory; the empirical decomposition of segmentation miscalibration variance into image-level vs. model-level components is new.
- **Minimal Experiment:** Fit global, oracle-per-image, and predicted-per-image temperatures for several models; report residual calibration error at each level.
- **Main Risk:** Per-image fitting on small pixel-effective-sample sizes can overfit, requiring the correlation-aware estimation from IDEA-B-0078.
- **Research Cluster:** CALIBRATION

### IDEA-B-0080 — "Calibration degrades under shift" is confounded by accuracy
- **One-sentence idea:** Re-examine the canonical finding that calibration deteriorates under distribution shift, controlling for the mechanical coupling between accuracy drop and calibration metrics.
- **Problem:** Calibration error necessarily grows when accuracy falls at fixed confidence; the field's shift-calibration story may be restating "accuracy drops" rather than identifying a distinct confidence pathology.
- **Core Hypothesis (falsifiable):** After conditioning on accuracy (matched-accuracy subsets or accuracy-adjusted metrics), a substantial portion of the reported calibration degradation under shift disappears, and what remains differs qualitatively across shift types.
- **Why Important:** The claim shapes deployment folklore and mitigation research; decoupling it would redirect effort toward the shift types where confidence genuinely misbehaves.
- **Why Possibly Novel:** The accuracy-calibration coupling is acknowledged in passing but has not been used to systematically re-analyze the shift-calibration literature's conclusions for dense prediction.
- **Minimal Experiment:** Evaluate models across corruption/domain shifts; compare raw vs. accuracy-conditioned calibration trajectories; classify shift types by residual behavior.
- **Main Risk:** Conditioning schemes each have their own artifacts; multiple independent adjustments must agree.
- **Research Cluster:** CALIBRATION / GENERALIZATION / ASSUMPTION

### IDEA-B-0081 — Aleatoric/epistemic decompositions disagree with each other
- **One-sentence idea:** Benchmark the consistency of popular aleatoric/epistemic decomposition methods against each other and against operational ground truth (label noise injections and OOD insertions).
- **Problem:** Papers rely on decomposition to justify methods ("epistemic uncertainty detects OOD"), but if different decomposition estimators disagree on the same model and data, the constructs may not be measuring anything stable.
- **Core Hypothesis (falsifiable):** Across standard estimators (variance-of-expectation vs. expectation-of-variance families, evidential methods), pairwise pixel-level rank correlations of "epistemic" maps are low (<0.5), and none dominates on operational tests where the true source of uncertainty is controlled.
- **Why Important:** A negative consistency result would force the field to replace metaphysical labels with operational definitions tied to interventions.
- **Why Possibly Novel:** Individual decomposition critiques exist; a controlled multi-method consistency audit with injected uncertainty sources in dense prediction is missing.
- **Minimal Experiment:** Inject controlled label noise and OOD objects into training/eval; run 5 decomposition methods on matched models; report cross-method agreement and detection performance per injected source.
- **Main Risk:** Disagreement could reflect implementation choices rather than conceptual failure; needs careful standardization.
- **Research Cluster:** UNCERTAINTY / NEG-RESULT

### IDEA-B-0082 — Most measured "aleatoric" uncertainty is annotation noise
- **One-sentence idea:** Test how much of the uncertainty models attribute to data ambiguity disappears when trained and evaluated on cleaner re-annotations of the same images.
- **Problem:** Aleatoric uncertainty is defined as irreducible, but if it largely tracks annotator error rather than image ambiguity, it is reducible with better labels — inverting practical recommendations.
- **Core Hypothesis (falsifiable):** Models trained on consensus re-annotations show substantially lower predicted aleatoric uncertainty in regions where original labels were noisy but images are unambiguous, while genuinely ambiguous regions (blur, occlusion) retain uncertainty.
- **Why Important:** Distinguishes "buy better labels" from "accept the noise" — a first-order budget decision — and stress-tests the aleatoric concept's operational meaning.
- **Why Possibly Novel:** Label noise and aleatoric UQ are studied separately; the identification experiment connecting them via re-annotation is not established.
- **Minimal Experiment:** On a dataset with multi-rater re-annotations, train heteroscedastic models on original vs. consensus labels; compare predicted-uncertainty maps stratified by image-ambiguity measures.
- **Main Risk:** Consensus labels are not ground truth either; some residual circularity is unavoidable.
- **Research Cluster:** UNCERTAINTY / ANNOT-EFF

### IDEA-B-0083 — Abstention is better spent on whole images than on pixels
- **One-sentence idea:** Compare selective-prediction value at pixel, region, and image granularity under a fixed abstention budget to find the operationally optimal rejection unit.
- **Problem:** Segmentation abstention research defaults to pixelwise rejection, but downstream consumers (clinicians, safety monitors) act at region or image level, and error correlation across pixels means budget allocation across granularities is a real, unstudied optimization.
- **Core Hypothesis (falsifiable):** For realistic error distributions, image-level rejection achieves better risk-coverage tradeoffs than pixel-level rejection at equal budget in error-clustered regimes, with the crossover governed by measurable error clustering statistics.
- **Why Important:** Provides deployment guidance grounded in error correlation structure and reframes selective prediction around the actionable unit.
- **Why Possibly Novel:** Risk-coverage analysis across abstention granularities with a clustering-based theory of the crossover is new for dense prediction.
- **Minimal Experiment:** For several models/datasets, compute risk-coverage curves at pixel/region/image levels using the same underlying confidence; relate crossovers to error-clustering indices.
- **Main Risk:** Conclusions depend on the assumed downstream cost model; results must be presented across cost structures.
- **Research Cluster:** UNCERTAINTY

### IDEA-B-0084 — Active-learning acquisition gains vanish against strong random baselines
- **One-sentence idea:** Replicate uncertainty-based active learning for segmentation against random sampling with matched, modern training pipelines (augmentation, semi-supervised co-use of unlabeled pool).
- **Problem:** AL papers often compare against weak baselines; modern recipes (strong augmentation, self-supervised pretraining, semi-supervised learning) may absorb the value acquisition functions used to provide.
- **Core Hypothesis (falsifiable):** Under a modern pipeline, the label-efficiency advantage of uncertainty acquisition over random shrinks below practical significance on standard segmentation benchmarks, except in identifiable regimes (severe class rarity).
- **Why Important:** AL adds pipeline complexity in real annotation projects; knowing when it is worthless at current-recipe strength saves real money.
- **Why Possibly Novel:** Strong-baseline AL audits exist for classification; the dense-prediction version with SSL-integrated baselines and regime analysis is missing.
- **Minimal Experiment:** Run AL loops (entropy, BALD-style, coreset) vs. random on two segmentation datasets under a modern semi-supervised recipe; report label-budget curves with seed CIs.
- **Main Risk:** AL might still win in the very-low-budget regime, requiring nuanced (regime-conditional) conclusions.
- **Research Cluster:** UNCERTAINTY / ANNOT-EFF / NEG-RESULT

### IDEA-B-0085 — Confidence ranks errors within images but not across images
- **One-sentence idea:** Quantify the gap between within-image and cross-image error-ranking power of confidence scores and identify what breaks comparability across images.
- **Problem:** A single confidence threshold is deployed across all images, implicitly assuming score comparability; if scores are only rank-consistent within an image, global thresholds silently misfire on whole images at a time.
- **Core Hypothesis (falsifiable):** Within-image error-detection AUROC of softmax confidence substantially exceeds cross-image AUROC for the same models, and per-image score normalization (rank or z-score) closes most of the gap.
- **Why Important:** Threshold-based deployment (the dominant pattern) rests on cross-image comparability; measuring and fixing its failure is directly actionable.
- **Why Possibly Novel:** The within/across decomposition of confidence quality has not been articulated as the central object for dense prediction.
- **Minimal Experiment:** Compute both AUROC variants for several models/datasets; test simple normalizers; relate cross-image failures to image-level covariates (contrast, clutter).
- **Main Risk:** Per-image normalization discards genuinely informative absolute confidence differences, possibly harming other use cases.
- **Research Cluster:** UNCERTAINTY / CALIBRATION

### IDEA-B-0086 — Spatially coherent conformal masks: coverage vs. coherence tradeoff
- **One-sentence idea:** Characterize the fundamental tradeoff between pixelwise conformal coverage guarantees and the spatial coherence of the resulting prediction sets in segmentation.
- **Problem:** Conformal methods give per-pixel coverage but produce speckled, unusable uncertainty sets; whether coherence can be imposed without breaking validity (or at what coverage cost) is unresolved.
- **Core Hypothesis (falsifiable):** Enforcing connectivity/smoothness constraints on conformal sets costs a quantifiable coverage-efficiency penalty that grows with the spatial autocorrelation mismatch between scores and errors, and there is a Pareto frontier no method can cross under exchangeability assumptions.
- **Why Important:** Real users consume regions, not pixels; a mapped Pareto frontier tells the field what is achievable versus what requires new assumptions.
- **Why Possibly Novel:** Conformal segmentation exists; the coherence-coverage frontier and its dependence on score-error autocorrelation is an open, formalizable question.
- **Minimal Experiment:** Implement pixelwise and morphology-constrained conformal variants; sweep constraint strength; trace the empirical frontier on multiple datasets against a derived bound.
- **Main Risk:** The theoretical bound may only exist under restrictive assumptions, making the contribution primarily empirical.
- **Research Cluster:** UNCERTAINTY

### IDEA-B-0087 — Label smoothing's calibration damage is superficial (last-layer)
- **One-sentence idea:** Test whether the calibration and distillation harms attributed to label smoothing live only in the final layer, reversible by brief re-training, rather than corrupting the representation.
- **Problem:** Label smoothing is reported to hurt distillation and distort confidence; if the damage is confined to the classifier layer, the practical cost is trivially reversible and the folklore overstates the harm.
- **Core Hypothesis (falsifiable):** Re-fitting only the final layer (without smoothing) on a smoothing-trained backbone restores calibration and distillation-teacher quality to within noise of a never-smoothed model, implying representations are unharmed.
- **Why Important:** Resolves a live recipe controversy with a mechanism-level answer, and demonstrates a general "where does the damage live" methodology for recipe choices.
- **Why Possibly Novel:** Smoothing's effects are documented; the layer-localization and reversibility experiment has not been run for dense prediction.
- **Minimal Experiment:** Train with/without smoothing; cross-graft final layers with brief re-fits; evaluate calibration, accuracy, and student-distillation quality in all four combinations.
- **Main Risk:** Effects may be architecture-dependent (BN interactions), demanding replication across families.
- **Research Cluster:** CALIBRATION / ASSUMPTION

### IDEA-B-0088 — Focal loss "calibrates" by symmetric error cancellation
- **One-sentence idea:** Decompose focal loss's reported calibration benefit into genuine reliability vs. cancellation of overconfident and underconfident regions that average to zero ECE.
- **Problem:** Focal loss is recommended for calibrated dense predictors, but aggregate ECE can look excellent while conditional calibration (per-region, per-confidence-band) is poor — the aggregate may hide a lucky cancellation.
- **Core Hypothesis (falsifiable):** Focal-trained models show systematic underconfidence on easy pixels and overconfidence on hard pixels whose aggregate cancels; conditional calibration metrics rank them below temperature-scaled CE models.
- **Why Important:** If a widely recommended recipe achieves its headline metric via cancellation, the recommendation misleads safety-relevant deployments that operate in specific confidence bands.
- **Why Possibly Novel:** Focal-calibration papers report aggregate metrics; the cancellation decomposition for dense prediction is unexamined.
- **Minimal Experiment:** Train CE, CE+temperature, and focal variants; report reliability diagrams stratified by difficulty and region type, plus band-conditional ECE.
- **Main Risk:** Results may vary with gamma and dataset, requiring a sweep to establish generality.
- **Research Cluster:** CALIBRATION / EVAL-WEAK

### IDEA-B-0089 — Uncertainty benchmarks are gameable by predicting boundary distance
- **One-sentence idea:** Construct a trivial geometry-only baseline (uncertainty = f(distance to predicted boundary, object size)) and test whether it matches SOTA UQ methods on standard sparsification benchmarks.
- **Problem:** Popular UQ evaluation metrics (AUSE, sparsification error) may be satisfiable by trivially predictable error geography, meaning the benchmarks cannot distinguish learned uncertainty from geometric heuristics.
- **Core Hypothesis (falsifiable):** The geometry-only baseline achieves sparsification metrics within a small margin of published MC-dropout/ensemble results on standard segmentation-UQ benchmarks.
- **Why Important:** If a no-learning baseline matches SOTA, the field's evaluation is broken and needs residualized protocols (see IDEA-B-0075) before further method claims.
- **Why Possibly Novel:** Trivial-baseline audits are a known genre (e.g., in video or NLP), but this specific one has not been run for dense-prediction UQ.
- **Minimal Experiment:** Fit the two-feature geometric predictor on validation errors; evaluate on standard UQ benchmark protocols against published methods' numbers reproduced from open code.
- **Main Risk:** Some benchmarks with OOD components will defeat the baseline, requiring honest scoping of the claim.
- **Research Cluster:** UNCERTAINTY / EVAL-WEAK / NEG-RESULT

### IDEA-B-0090 — Ensemble diversity in segmentation comes from data order, not initialization
- **One-sentence idea:** Factorially decompose the sources of deep-ensemble diversity (init, data order, augmentation randomness) for dense prediction to find the cheapest way to reproduce it.
- **Problem:** Ensembles are expensive; if their diversity is driven by one cheap randomness source, equally diverse ensembles could be built with shared computation (e.g., branch late, vary data order only).
- **Core Hypothesis (falsifiable):** Fixing initialization while varying data order yields ensembles with disagreement and UQ quality statistically indistinguishable from fully independent ensembles, whereas fixing data order and varying init yields significantly less diversity.
- **Why Important:** Identifies the operative randomness for dense-prediction ensembles and enables cost-reduced designs with predictable quality.
- **Why Possibly Novel:** Diversity-source decompositions exist for classification; dense prediction (where errors are spatially structured) may behave differently and is unstudied.
- **Minimal Experiment:** Train ensemble grids varying each randomness factor in isolation; measure pairwise disagreement, UQ metrics, and OOD detection.
- **Main Risk:** Interactions between factors may prevent clean attribution.
- **Research Cluster:** UNCERTAINTY / PHENOMENON

### IDEA-B-0091 — Last-layer Bayesian methods match full-network ones in dense prediction
- **One-sentence idea:** Test whether epistemic uncertainty in segmentation is linearly decodable — i.e., whether Bayesian treatment of only the final layer captures everything full-network approximations provide.
- **Problem:** Full-network Bayesian approximations are costly and their extra value over last-layer treatments has not been honestly measured for dense prediction.
- **Core Hypothesis (falsifiable):** On error detection, OOD localization, and calibration under shift, last-layer Bayesian inference performs within noise of full-network variational/Laplace/MC methods at a fraction of the cost, across architectures.
- **Why Important:** A confirmed equivalence collapses a research direction into a cheap default; a refutation identifies exactly which uncertainty information lives deep in the network.
- **Why Possibly Novel:** Last-layer sufficiency has support in classification; dense prediction's spatial structure and skip connections make extrapolation non-obvious and untested.
- **Minimal Experiment:** Implement matched last-layer vs. full-network Bayesian variants on two segmentation architectures; compare across the UQ metric suite with compute accounting.
- **Main Risk:** Approximation quality differences (not layer coverage) could drive results; needs multiple inference methods per coverage level.
- **Research Cluster:** UNCERTAINTY / NEG-RESULT

### IDEA-B-0092 — Segmentation OOD detectors detect texture novelty, not semantic novelty
- **One-sentence idea:** Disentangle whether anomaly-segmentation methods respond to unfamiliar semantics or unfamiliar low-level statistics, using style-transferred and texture-swapped controls.
- **Problem:** Road-anomaly benchmarks confound "novel object class" with "novel appearance statistics"; methods may pass by flagging texture outliers and fail on semantically novel objects with familiar textures.
- **Core Hypothesis (falsifiable):** Restyling known-class objects (novel texture, familiar semantics) triggers OOD scores comparable to genuinely novel objects, while novel objects re-textured with in-distribution materials evade detection at high rates.
- **Why Important:** Deployment risk comes from semantic novelty (an unknown obstacle), not from texture drift; if detectors track the wrong variable, benchmark success is safety-hollow.
- **Why Possibly Novel:** Texture-vs-semantics controls are used in recognition bias studies but have not been ported to anomaly segmentation evaluation.
- **Minimal Experiment:** Build a controlled test set of (familiar-class, novel-texture) and (novel-class, familiar-texture) insertions; evaluate leading anomaly segmenters on both axes.
- **Main Risk:** Insertion artifacts may themselves drive detections; requires artifact-matched controls.
- **Research Cluster:** UNCERTAINTY / ROBUSTNESS / EVAL-WEAK

### IDEA-B-0093 — Correct small-object detections are systematically under-confident
- **One-sentence idea:** Measure size-conditional calibration curves to test whether models assign lower confidence to correct predictions on small objects, and fix it with size-aware recalibration.
- **Problem:** Calibration is evaluated pooled over sizes; if confidence is size-biased, thresholded deployments silently drop correct small detections — the regime where misses are most dangerous.
- **Core Hypothesis (falsifiable):** At matched correctness, predicted confidence decreases with object size across model families, and size-conditional temperature scaling improves small-object recall at fixed precision without retraining.
- **Why Important:** A cheap post-hoc fix with immediate deployment value, plus evidence that calibration must be reported conditionally to be meaningful.
- **Why Possibly Novel:** Size-conditional reliability analysis has not been published as a systematic cross-model study (complements IDEA-B-0014's ranking effect with a calibration lens).
- **Minimal Experiment:** Compute size-binned reliability diagrams for detectors/instance segmenters; apply size-conditional scaling fitted on validation; report threshold-based operating-point changes.
- **Main Risk:** Overlaps with IDEA-B-0014; must be scoped to calibration (probability meaning) rather than AP ranking to stay distinct.
- **Research Cluster:** CALIBRATION / SMALL-OBJ

### IDEA-B-0094 — Model uncertainty and human uncertainty live in different places
- **One-sentence idea:** Map pixelwise model uncertainty against annotator-disagreement maps to quantify where they align and where each is blind.
- **Problem:** Model uncertainty is often marketed as approximating human ambiguity, but the spatial correlation between the two has never been measured systematically — they may capture disjoint phenomena.
- **Core Hypothesis (falsifiable):** The pixel-level correlation between model uncertainty and multi-rater disagreement is weak overall, with alignment concentrated at boundaries and systematic divergence in interior ambiguity zones (where humans disagree but models are confident).
- **Why Important:** Human-facing uses of uncertainty (review triage, clinical flags) assume alignment; measuring the mismatch defines what current UQ can and cannot promise.
- **Why Possibly Novel:** Multi-rater datasets exist (medical, ambiguous scenes), but the systematic model-vs-human uncertainty geography comparison across methods is missing.
- **Minimal Experiment:** On multi-rater benchmarks, compute correlation and zone-resolved alignment (per IDEA-B-0077's taxonomy) for several UQ methods; identify blind-spot case categories.
- **Main Risk:** Annotator disagreement mixes ambiguity with sloppiness; disentangling requires protocol metadata.
- **Research Cluster:** UNCERTAINTY / ANNOT-EFF

### IDEA-B-0095 — TTA variance vs. MC-dropout at matched compute
- **One-sentence idea:** Head-to-head compare test-time-augmentation disagreement against MC-dropout and ensembles as uncertainty sources under strict compute matching.
- **Problem:** TTA variance is a folk uncertainty signal that costs the same forward passes as MC-dropout, yet the literature rarely compares them under matched budgets or explains when input-space vs. weight-space perturbation captures more error information.
- **Core Hypothesis (falsifiable):** At matched forward-pass budgets, TTA-based uncertainty matches or exceeds MC-dropout on error detection for in-distribution data, while weight-space methods win on OOD localization — a dissociation stable across architectures.
- **Why Important:** Gives practitioners a compute-rational choice and a conceptual account of what each perturbation family probes.
- **Why Possibly Novel:** Scattered comparisons exist; the compute-matched, dissociation-focused study for dense prediction is not established.
- **Minimal Experiment:** Fix budgets of {4, 8, 16} passes; evaluate all three methods on error detection and OOD tasks over two datasets and two architectures.
- **Main Risk:** TTA design space (which augmentations) is a confound requiring principled selection or sweeping.
- **Research Cluster:** UNCERTAINTY

### IDEA-B-0096 — When does calibration actually matter downstream?
- **One-sentence idea:** Empirically identify which deployment decision patterns (thresholding, ranking, averaging, human handoff) are sensitive to calibration error and at what magnitude, in dense-prediction pipelines.
- **Problem:** Calibration is treated as an unconditional good, but many pipelines consume ranks or argmaxes that are invariant to monotone miscalibration — the field lacks a map of when calibration effort pays.
- **Core Hypothesis (falsifiable):** For a majority of common pipeline patterns, realistic calibration error levels change downstream outcomes negligibly; the exceptions (probability-weighted fusion, cost-sensitive thresholds, human trust interfaces) are identifiable in advance from pipeline structure.
- **Why Important:** Prevents wasted calibration engineering and focuses it where it changes decisions — an efficiency result for the whole applied community.
- **Why Possibly Novel:** Decision-theoretic calibration analyses exist in the abstract; an empirical pipeline-pattern survey with dense-prediction case studies is missing.
- **Minimal Experiment:** Simulate/instantiate 6 representative pipelines consuming segmentation outputs; inject controlled miscalibration; measure downstream metric sensitivity curves per pattern.
- **Main Risk:** Pipeline taxonomy could be contested as unrepresentative; needs grounding in surveyed real systems.
- **Research Cluster:** CALIBRATION / ASSUMPTION

### IDEA-B-0097 — Checkpoint ensembles capture most of deep-ensemble uncertainty for free
- **One-sentence idea:** Test whether temporal ensembles (checkpoints along one training run) reproduce the uncertainty quality of independent deep ensembles for segmentation at ~1x training cost.
- **Problem:** Deep ensembles multiply training cost; if late-training checkpoints are diverse enough in function space for dense prediction, the expensive independence is unnecessary.
- **Core Hypothesis (falsifiable):** Checkpoint ensembles (with cyclical learning-rate sampling) achieve within-noise uncertainty metrics relative to independent ensembles on error detection and calibration, but measurably lag on OOD-object localization where weight-space diversity matters.
- **Why Important:** A validated cheap substitute changes the default recommendation for uncertainty-needing deployments; the predicted OOD lag also sharpens theory about what independence buys.
- **Why Possibly Novel:** Snapshot ensembles exist for accuracy; the uncertainty-quality decomposition (where they match, where they lag) for dense prediction is unmeasured.
- **Minimal Experiment:** Train matched independent vs. cyclical-checkpoint ensembles; run the full UQ suite including OOD insertion tests; compare per-axis.
- **Main Risk:** Checkpoint diversity depends heavily on LR schedule, adding a tuning dimension that complicates "for free" claims.
- **Research Cluster:** UNCERTAINTY

### IDEA-B-0098 — Showing annotators model uncertainty biases their labels
- **One-sentence idea:** Run a controlled human study testing whether uncertainty-guided annotation interfaces anchor annotators to model beliefs and degrade label independence.
- **Problem:** Uncertainty-guided review is a celebrated human-in-the-loop pattern, but displaying model beliefs plausibly anchors humans, converting independent labels into model-echoes precisely where the model is unsure.
- **Core Hypothesis (falsifiable):** Annotators shown uncertainty overlays produce labels measurably closer to model predictions (and farther from blind-consensus GT) in ambiguous regions than annotators without overlays, with the effect persisting after training/warnings.
- **Why Important:** If the standard efficiency pattern corrupts the labels that are supposed to correct the model, dataset feedback loops (see IDEA-B-0157) accelerate — a serious process-level finding.
- **Why Possibly Novel:** Anchoring is established in psychology; its quantitative effect in segmentation annotation interfaces has not been measured.
- **Minimal Experiment:** Randomized annotation study (n≈30) with/without uncertainty display on ambiguous regions with pre-established blind consensus; measure model-agreement shift and quality change.
- **Main Risk:** Lab annotators may not represent professional workforce behavior; needs at least one professional-vendor arm.
- **Research Cluster:** UNCERTAINTY / ANNOT-EFF / NEG-RESULT

### IDEA-B-0099 — Test-time adaptation destroys the uncertainty needed for safety
- **One-sentence idea:** Measure the calibration and OOD-detection cost of entropy-minimization-based test-time adaptation, testing whether TTA and uncertainty quality are fundamentally in tension.
- **Problem:** TTA methods (TENT-style) explicitly minimize predictive entropy — the very signal used for error detection and abstention — so accuracy gains may be purchased with silent destruction of the safety channel.
- **Core Hypothesis (falsifiable):** After entropy-minimizing TTA, error-detection AUROC and OOD-localization performance drop substantially even when accuracy rises, and the degradation scales with adaptation steps; uncertainty-preserving TTA variants pay a measurable accuracy price, tracing a tradeoff frontier.
- **Why Important:** TTA is being adopted in deployment pipelines that simultaneously rely on confidence monitoring; an inherent conflict would be a deployment-critical warning.
- **Why Possibly Novel:** TTA is evaluated on accuracy; its effect on the uncertainty channel has not been the object of systematic study.
- **Minimal Experiment:** Run TENT-family methods on corrupted segmentation benchmarks; track accuracy, calibration, error-detection, and anomaly metrics vs. adaptation steps; map the frontier.
- **Main Risk:** Some TTA variants may not exhibit the tradeoff, requiring per-family analysis rather than a blanket claim.
- **Research Cluster:** UNCERTAINTY / ROBUSTNESS

### IDEA-B-0100 — Post-hoc calibration with more parameters is more shift-fragile
- **One-sentence idea:** Test whether richer post-hoc calibrators (per-class, per-region, spline-based) that win in-distribution lose to single-temperature scaling under distribution shift.
- **Problem:** Calibration research trends toward expressive post-hoc maps validated in-distribution; expressiveness fitted to validation idiosyncrasies may invert into harm precisely when calibration matters most (under shift).
- **Core Hypothesis (falsifiable):** Across shift benchmarks, calibration-method ranking inverts with shift severity: expressive calibrators dominate in-distribution but underperform single-parameter scaling beyond moderate shift, with the crossover predictable from validation-set effective sample size.
- **Why Important:** Delivers a robustness-aware selection rule for a ubiquitous post-processing step and a clean instance of the bias-variance tradeoff operating at the meta level.
- **Why Possibly Novel:** Calibration-under-shift studies compare training methods; the post-hoc-calibrator complexity axis has not been isolated.
- **Minimal Experiment:** Fit calibrators of increasing complexity on clean validation; evaluate calibration across a corruption-severity ladder; locate ranking crossovers.
- **Main Risk:** Results may depend on validation size; must be swept to support the predictive claim.
- **Research Cluster:** CALIBRATION / ROBUSTNESS

### IDEA-B-0101 — Input-sensitivity is a competitive zero-training uncertainty baseline
- **One-sentence idea:** Benchmark local input-sensitivity measures (finite-difference logit change under tiny perturbations) as an uncertainty signal against learned UQ methods.
- **Problem:** UQ methods add training or inference machinery, but the local smoothness of the network around an input is available for free and may carry much of the same error information — a baseline the literature omits.
- **Core Hypothesis (falsifiable):** Perturbation-sensitivity maps achieve error-detection performance within a small margin of MC-dropout on in-distribution data across architectures, establishing a mandatory baseline for UQ claims.
- **Why Important:** If free signals match trained machinery, the bar for publishing UQ methods rises and deployments get a cheap default.
- **Why Possibly Novel:** Gradient-norm baselines appear in classification OOD work but are absent from dense-prediction UQ comparisons.
- **Minimal Experiment:** Compute sensitivity maps (k random perturbations) for several segmenters; evaluate on error-detection and sparsification protocols against standard UQ methods at matched inference cost.
- **Main Risk:** Sensitivity may collapse to the boundary-distance confound (IDEA-B-0075), requiring residualized analysis.
- **Research Cluster:** UNCERTAINTY

### IDEA-B-0102 — Ignore-label regions silently distort confidence around them
- **One-sentence idea:** Audit how void/ignore-label handling during training shapes confidence and error rates in a halo around ignored regions.
- **Problem:** Every pipeline masks ignore-labels out of the loss, assuming locality of supervision; but convolutional receptive fields and normalization couple ignored regions to their surroundings, potentially creating unaudited confidence artifacts.
- **Core Hypothesis (falsifiable):** Prediction confidence and error rates show a measurable gradient as a function of distance to ignore regions, and the artifact's magnitude depends on the masking implementation (loss-mask vs. label-fill choices) more than on architecture.
- **Why Important:** Ignore regions sit exactly at hard places (boundaries, ambiguous zones); implementation-dependent artifacts there contaminate both training and the evaluation protocols that also skip void pixels.
- **Why Possibly Novel:** Void handling is treated as bookkeeping; nobody has measured its spatial side effects on model behavior.
- **Minimal Experiment:** Train matched models varying only void-handling implementation; map confidence/error vs. distance-to-void; compare across implementations.
- **Main Risk:** Effects may be small relative to local content variation, needing careful matched-content analysis.
- **Research Cluster:** CALIBRATION / EVAL-WEAK

### IDEA-B-0103 — Error locations are model-independent: uncertainty transfers across models
- **One-sentence idea:** Measure cross-model error-location correlation to test whether a small proxy model's uncertainty predicts a large model's errors well enough to serve as its uncertainty estimator.
- **Problem:** If errors are mostly data-driven (ambiguous evidence) rather than model-driven, uncertainty estimation can be delegated to a cheap side model — but the field assumes uncertainty must come from the deployed model itself.
- **Core Hypothesis (falsifiable):** Pixel error overlap between independently trained models of very different capacity is high enough that a small model's uncertainty achieves >80% of the large model's own-uncertainty error-detection performance at a fraction of the cost.
- **Why Important:** Would decouple UQ cost from model cost — major for large-model deployments — and quantify the data-driven share of segmentation error.
- **Why Possibly Novel:** Error-agreement studies exist for classification ("agreement-on-the-line" style); using them to justify proxy-model UQ for dense prediction is new.
- **Minimal Experiment:** Train small and large segmenters; compute cross-model error correlations; evaluate small-model uncertainty against large-model errors on detection metrics, in- and out-of-distribution.
- **Main Risk:** Under shift, model-specific failure modes may decorrelate, bounding the proxy's safe operating domain.
- **Research Cluster:** UNCERTAINTY / PHENOMENON

### IDEA-B-0104 — Miscalibration lives in a few feature-space clusters
- **One-sentence idea:** Test whether segmentation miscalibration concentrates in a small number of identifiable feature-space regions, enabling targeted low-parameter recalibration.
- **Problem:** Global calibration treats miscalibration as uniform, but if it is concentrated (specific ambiguous prototypes: shadowed vegetation, reflective surfaces), global temperature both under- and over-corrects, and the structure itself is diagnostic.
- **Core Hypothesis (falsifiable):** Clustering penultimate features and fitting per-cluster temperatures shows a heavy-tailed miscalibration distribution (few clusters carry most calibration error), and cluster-conditional scaling with <50 parameters outperforms global scaling by a large margin in conditional calibration.
- **Why Important:** Reveals the semantic structure of confidence failure and gives an interpretable, auditable calibration map ("this model is overconfident on wet roads").
- **Why Possibly Novel:** Cluster-conditional recalibration with an accompanying concentration analysis has not been reported for dense prediction.
- **Minimal Experiment:** Cluster features of validation pixels; measure per-cluster reliability; fit and evaluate cluster-conditional temperatures on held-out data and under mild shift.
- **Main Risk:** Cluster granularity is a free parameter; conclusions must be stable across reasonable choices.
- **Research Cluster:** CALIBRATION

### IDEA-B-0105 — Multi-rater soft labels buy calibration, not accuracy
- **One-sentence idea:** Test whether training on soft multi-annotator label distributions improves anything beyond calibration — isolating what information rater disagreement actually contains.
- **Problem:** Multi-rater datasets are expensive and their soft labels are presumed to improve models broadly, but the improvement may be entirely in the confidence channel with zero effect on decision accuracy.
- **Core Hypothesis (falsifiable):** At matched training, soft-label models equal hard-consensus models on accuracy metrics while significantly improving calibration and human-disagreement prediction — and distilling soft-label models back to hard outputs preserves nothing of value.
- **Why Important:** Quantifies the marginal value of multi-rater annotation budgets and clarifies whether disagreement encodes recoverable signal or only noise statistics.
- **Why Possibly Novel:** Multi-rater training papers report mixed metrics; the sharp accuracy-vs-calibration decomposition with distillation controls is not established.
- **Minimal Experiment:** On multi-rater medical/ambiguous benchmarks, train hard vs. soft label variants; report accuracy, calibration, and disagreement-prediction; run the distillation control.
- **Main Risk:** Consensus construction method (majority vs. STAPLE-style) confounds the hard-label arm.
- **Research Cluster:** CALIBRATION / ANNOT-EFF

### IDEA-B-0106 — The background class is an implicit reject option with unexamined calibration
- **One-sentence idea:** Characterize how the background/"stuff-other" class absorbs uncertainty and how its calibration asymmetrically controls false-positive vs. false-negative behavior of deployed segmenters.
- **Problem:** Background is treated as just another class, but operationally it is a rejection channel; its confidence semantics differ from object classes, and miscalibration there directly sets hallucination and miss rates.
- **Core Hypothesis (falsifiable):** Background-class confidence exhibits systematically different reliability structure than object classes across models (e.g., overconfident absorption of ambiguous object pixels), and recalibrating the background margin alone shifts the FP/FN operating curve more than recalibrating all object classes together.
- **Why Important:** Provides a single high-leverage calibration knob for deployment tuning and reframes background as the safety-critical class it operationally is.
- **Why Possibly Novel:** Class-wise calibration is standard; the operational-asymmetry analysis of background as implicit rejection has not been articulated or measured.
- **Minimal Experiment:** Compute background-vs-object reliability decompositions for several models; perform margin-targeted recalibration; trace FP/FN operating curves.
- **Main Risk:** Datasets differ in background ontology (explicit class vs. absence), complicating cross-dataset generalization.
- **Research Cluster:** CALIBRATION

### IDEA-B-0107 — Confidence decays from object center in a universal geometric profile
- **One-sentence idea:** Test whether per-object confidence profiles (as a function of normalized distance from center/skeleton) collapse to a shared curve across classes, sizes, and architectures.
- **Problem:** If confidence geography is dominated by a universal geometric profile rather than image evidence, much of the confidence map is redundant, predictable, and should be factored out of uncertainty evaluation and communication.
- **Core Hypothesis (falsifiable):** After normalizing by object scale, per-object confidence profiles collapse to a low-variance universal curve explaining most within-object confidence variance, with residuals — not the raw map — carrying the error-predictive information.
- **Why Important:** A confirmed universal profile simplifies uncertainty representation (store residuals), strengthens the trivial-baseline critique of UQ benchmarks, and is a clean, surprising empirical regularity.
- **Why Possibly Novel:** Object-normalized confidence geometry has not been characterized as a phenomenon in its own right.
- **Minimal Experiment:** Extract normalized confidence profiles for millions of instances across models/datasets; measure collapse quality; compare error prediction of raw vs. residual maps.
- **Main Risk:** Elongated/multi-part objects may defy any single normalization scheme.
- **Research Cluster:** UNCERTAINTY / PHENOMENON

### IDEA-B-0108 — Loss reweighting miscalibrates predictably — and correctably in closed form
- **One-sentence idea:** Derive the confidence distortion induced by class-frequency loss reweighting and verify that the closed-form inverse correction restores calibration exactly.
- **Problem:** Class rebalancing is ubiquitous and known to distort probabilities, but practitioners recalibrate empirically; a derived correction would make the distortion a solved bookkeeping issue and test how well idealized theory describes real training.
- **Core Hypothesis (falsifiable):** For models trained with weight w_c per class, applying the derived logit correction recovers calibration within noise of an unweighted model, across weighting schemes — deviations localize where the theory's assumptions (calibrated conditional learning) break.
- **Why Important:** Ends an avoidable source of deployment miscalibration and provides a sharp test of whether networks learn reweighted posteriors as theory predicts.
- **Why Possibly Novel:** Logit-adjustment theory exists for balanced-error objectives; the verification program treating deviation-from-theory as the measurement, in dense prediction, is new.
- **Minimal Experiment:** Train segmenters under several weighting schemes; apply closed-form corrections; compare reliability against unweighted baselines; map where residuals concentrate.
- **Main Risk:** Spatial correlation and augmentation may violate the derivation's assumptions broadly, leaving mostly deviations (still informative, less clean).
- **Research Cluster:** CALIBRATION / PHENOMENON

### IDEA-B-0109 — Early-stopping epoch, not architecture, determines calibration
- **One-sentence idea:** Run a large sweep to test whether where you stop training explains more calibration variance than which architecture you train.
- **Problem:** Calibration comparisons between architectures use each one's accuracy-optimal checkpoint, but calibration evolves nonmonotonically during training; reported "architecture X is better calibrated" claims may be checkpoint-selection artifacts.
- **Core Hypothesis (falsifiable):** Across a grid of architectures and stopping points, variance decomposition attributes more calibration variance to stopping epoch than to architecture, and architecture rankings by calibration invert across reasonable stopping criteria.
- **Why Important:** Would reduce a genre of architecture-calibration claims to a training-schedule footnote and mandate calibration-vs-epoch reporting.
- **Why Possibly Novel:** Calibration dynamics during training are documented in isolation; the variance-attribution framing against architecture claims is new.
- **Minimal Experiment:** Train 5 architectures with dense checkpointing; compute calibration trajectories; run variance decomposition and ranking-stability analysis.
- **Main Risk:** Interactions (architecture-specific calibration dynamics) may resist clean decomposition.
- **Research Cluster:** CALIBRATION / EVAL-WEAK

### IDEA-B-0110 — Scaling improves accuracy but degrades failure detectability
- **One-sentence idea:** Test whether larger segmentation models, while more accurate, produce errors that are harder to detect from their own confidence — a safety-relevant inverse scaling law.
- **Problem:** Scaling studies report accuracy; deployment safety depends on the detectability of the residual errors, which could worsen as models become confidently wrong on their remaining failures.
- **Core Hypothesis (falsifiable):** Across a model-scale ladder, error-detection AUROC from self-confidence declines with scale even as error rate falls, making the absolute rate of undetectable errors non-monotonic in scale.
- **Why Important:** If the deployable-safety optimum is not the biggest model, scaling recommendations for safety-critical dense prediction need revision.
- **Why Possibly Novel:** Inverse scaling has been explored for language phenomena; the failure-detectability axis for dense prediction is unmeasured.
- **Minimal Experiment:** Evaluate a scale family (matched recipe) on error rate, detection AUROC, and undetectable-error rate across in-distribution and shifted data.
- **Main Risk:** Recipe differences across scales (schedules, augmentation) could confound the trend; needs a controlled ladder.
- **Research Cluster:** UNCERTAINTY / PHENOMENON

### IDEA-B-0111 — Instance-existence and mask-quality uncertainty are different axes
- **One-sentence idea:** Show that "is this object real?" and "is this mask accurate?" uncertainties are weakly correlated and require separate estimation and evaluation in instance segmentation.
- **Problem:** Instance segmenters emit one confidence scalar consumed for both purposes, but hallucinated-instance detection and boundary-quality prediction are different failure modes plausibly requiring different signals.
- **Core Hypothesis (falsifiable):** Across models, the score's ability to predict instance existence errors is much stronger than its ability to predict mask-quality (IoU) — and independently estimated quality heads decorrelate from existence confidence, confirming two axes.
- **Why Important:** Downstream systems make different decisions for "maybe not there" vs. "there but poorly outlined"; conflating them in one scalar loses actionable structure.
- **Why Possibly Novel:** IoU-prediction heads exist as engineering; the two-axis decomposition with evaluation protocol and cross-model measurement is not established as science.
- **Minimal Experiment:** For several instance segmenters, measure the score's predictive power for each error type; train lightweight quality estimators; quantify axis correlation.
- **Main Risk:** The axes may correlate strongly in practice for well-trained models, yielding a null (informative for parsimony).
- **Research Cluster:** UNCERTAINTY

### IDEA-B-0112 — Strong augmentation trains away legitimate aleatoric cues
- **One-sentence idea:** Map the tradeoff between augmentation strength and the model's ability to represent genuine input ambiguity (lighting, blur, transparency).
- **Problem:** Aggressive photometric augmentation teaches invariance to exactly the cues (dimness, blur) that should legitimately raise uncertainty, potentially producing accurate but ambiguity-blind models.
- **Core Hypothesis (falsifiable):** As photometric augmentation strength increases, models' uncertainty on genuinely degraded inputs decreases (they become confidently wrong in low-information conditions), tracing a measurable accuracy-vs-ambiguity-awareness tradeoff curve.
- **Why Important:** Recipe design currently optimizes accuracy alone; if it silently deletes ambiguity awareness, safety-oriented training needs augmentation-aware uncertainty targets.
- **Why Possibly Novel:** Augmentation-calibration interactions are noted anecdotally; the systematic tradeoff curve with degradation-conditional evaluation is unmapped.
- **Minimal Experiment:** Train an augmentation-strength ladder; evaluate accuracy and uncertainty quality on controlled degradation suites; plot both curves.
- **Main Risk:** Distinguishing "appropriately confident because robust" from "inappropriately confident" requires ground truth on what is truly recoverable — needs careful stimulus design.
- **Research Cluster:** UNCERTAINTY / ROBUSTNESS

### IDEA-B-0113 — Coarse-level confidence is well-calibrated even when fine-level is not
- **One-sentence idea:** Test whether errors concentrate within superclasses such that hierarchical aggregation of confidence yields reliable coarse probabilities from unreliable fine ones.
- **Problem:** Deployments often need only coarse decisions (drivable vs. not; tissue vs. lesion), but calibration is evaluated and repaired at the fine class level where it is hardest — possibly wasted effort.
- **Core Hypothesis (falsifiable):** Aggregating fine-class probabilities into a semantic hierarchy yields coarse-level calibration errors several times smaller than fine-level ones across models, without any recalibration — because most miscalibration is within-superclass confusion.
- **Why Important:** Enables reliable coarse-grained deployment from existing models and locates miscalibration's semantic structure.
- **Why Possibly Novel:** Hierarchical evaluation exists for accuracy; the calibration-transfer-under-aggregation phenomenon is unquantified.
- **Minimal Experiment:** Define hierarchies over benchmark label spaces; compare fine vs. aggregated reliability for many public models; decompose miscalibration into within- vs. across-superclass components.
- **Main Risk:** Hierarchy choice affects results; multiple independently motivated hierarchies must agree.
- **Research Cluster:** CALIBRATION

### IDEA-B-0114 — Sparse supervision produces better-calibrated models than dense masks
- **One-sentence idea:** Test whether point/scribble-supervised models, at matched accuracy, are better calibrated than densely supervised ones because they never receive overconfident boundary supervision.
- **Problem:** Dense masks assert pixel-level certainty everywhere including genuinely ambiguous zones; sparse supervision only asserts labels where annotators chose to click — plausibly a more honest signal whose calibration consequences are unexplored.
- **Core Hypothesis (falsifiable):** At matched mIoU (achieved via more images for the sparse regime), sparsely supervised models show significantly better boundary-zone calibration and human-disagreement alignment than densely supervised ones.
- **Why Important:** Would add calibration as a hidden benefit to the annotation-efficiency case for sparse labels, changing the dense-vs-sparse budget calculus.
- **Why Possibly Novel:** Sparse supervision is studied for accuracy-per-cost; its calibration signature has not been examined.
- **Minimal Experiment:** Train matched-accuracy dense vs. point-supervised models; compare zone-resolved calibration and disagreement alignment on multi-rater test data.
- **Main Risk:** Accuracy matching across supervision regimes requires unequal data, introducing a dataset-size confound to control.
- **Research Cluster:** CALIBRATION / ANNOT-EFF

### IDEA-B-0115 — Non-parametric feature-distance beats learned UQ at scale
- **One-sentence idea:** Benchmark k-NN distance to training features as pixel uncertainty against parametric UQ methods, testing whether memory beats machinery as training sets grow.
- **Problem:** Parametric UQ compresses training-distribution knowledge into weights; with cheap vector search, directly measuring "have I seen this before" may dominate — but scaling behavior of both families is unmeasured for dense prediction.
- **Core Hypothesis (falsifiable):** k-NN feature-distance uncertainty improves with training-set size faster than parametric methods' UQ quality, overtaking them beyond a dataset scale on OOD localization and error detection.
- **Why Important:** Establishes whether the future of dense UQ is retrieval-based, with practical implications for systems already deploying feature stores.
- **Why Possibly Novel:** k-NN OOD detection exists for classification; the scaling-crossover framing for pixel-level uncertainty is new.
- **Minimal Experiment:** Build feature indices at multiple training-set scales; evaluate k-NN vs. MC-dropout/ensembles on the UQ suite as functions of scale.
- **Main Risk:** Feature choice (which layer, which model) is a large design space that could dominate the comparison.
- **Research Cluster:** UNCERTAINTY

### IDEA-B-0116 — Why sigmoid heads calibrate differently than softmax under shift
- **One-sentence idea:** Mechanistically compare multi-label (sigmoid) vs. mutually exclusive (softmax) output parameterizations for calibration behavior under distribution shift in segmentation.
- **Problem:** The output normalization couples class confidences in softmax (evidence for one class suppresses others), which under shift may propagate errors across classes; sigmoid decouples them — a structural difference whose calibration consequences are asserted in scattered places but not mechanistically established.
- **Core Hypothesis (falsifiable):** Under label-space-preserving shifts, softmax models show coupled miscalibration (confidence redistribution among wrong classes) while sigmoid models degrade independently per class, yielding measurably better shift calibration at matched clean accuracy — with the difference traced to the normalization term via logit-intervention analysis.
- **Why Important:** Output parameterization is a free choice at design time; a mechanism-level answer (not a horse race) would settle it per deployment type.
- **Why Possibly Novel:** The intervention-based mechanistic attribution (manipulating the coupling term directly) distinguishes this from empirical loss-swap comparisons.
- **Minimal Experiment:** Train matched pairs; evaluate shift calibration; perform logit-space interventions isolating the normalization coupling; verify the mechanism accounts for the difference.
- **Main Risk:** Training dynamics differences (not just inference coupling) may drive results, complicating the clean mechanistic story.
- **Research Cluster:** CALIBRATION / REP-MISMATCH

### IDEA-B-0117 — Optimizer schedule is a hidden calibration variable
- **One-sentence idea:** Quantify how much final calibration is predictable from schedule parameters (warmup length, decay shape, final LR) independent of architecture and data.
- **Problem:** Calibration differences between published models are attributed to architectures and losses while their training schedules differ wildly; if schedule explains much of it, the literature's causal stories are misattributed.
- **Core Hypothesis (falsifiable):** In a controlled sweep, schedule parameters explain a large share of calibration variance at fixed architecture, and a simple schedule-based predictor forecasts a new run's calibration error within tight bounds.
- **Why Important:** Turns calibration partially into a predictable training-configuration property and forces schedule-matched comparisons in calibration research.
- **Why Possibly Novel:** LR schedule effects on accuracy are studied; a predictive calibration model over schedule space for dense prediction is not.
- **Minimal Experiment:** Sweep warmup/decay/final-LR grids on two architectures; fit and validate the calibration predictor on held-out configurations.
- **Main Risk:** Interactions with batch size and augmentation may limit predictor transferability across labs.
- **Research Cluster:** CALIBRATION / PHENOMENON

### IDEA-B-0118 — Uncertainty maps break before accuracy under compression and resizing
- **One-sentence idea:** Measure the relative fragility of uncertainty quality vs. prediction accuracy under deployment-pipeline transformations (JPEG, resizing, quantization).
- **Problem:** Models are validated for UQ in lab conditions, then deployed behind pipelines that compress and rescale inputs and quantize weights; if the uncertainty channel degrades faster than accuracy, safety monitoring silently fails while predictions look fine.
- **Core Hypothesis (falsifiable):** Across models, error-detection AUROC and calibration degrade at substantially lower transformation severities than accuracy does, with weight quantization affecting the uncertainty channel disproportionately.
- **Why Important:** Defines UQ-specific deployment requirements (pipeline tolerances) that current practice ignores entirely.
- **Why Possibly Novel:** Robustness of predictions is studied extensively; robustness of the uncertainty channel itself is nearly untouched.
- **Minimal Experiment:** Sweep compression/resize/quantization severities; track accuracy and the full UQ metric suite; locate the divergence points per transformation.
- **Main Risk:** Results may be strongly method-dependent, requiring several UQ families for general claims.
- **Research Cluster:** UNCERTAINTY / ROBUSTNESS

### IDEA-B-0119 — Seed variance swamps method differences in segmentation-UQ benchmarks
- **One-sentence idea:** Establish the seed-level variance of standard uncertainty metrics and test how much of the published UQ-method literature's gaps fall inside it.
- **Problem:** UQ metrics (AUSE, ECE, OOD AUROC) are reported from single runs; their run-to-run variance in dense prediction is unknown, so the significance of typical method gaps is unverifiable.
- **Core Hypothesis (falsifiable):** The across-seed standard deviation of common UQ metrics for a fixed method exceeds a large fraction of the typical between-method gaps reported in the segmentation-UQ literature.
- **Why Important:** A variance floor for the subfield would separate robust findings from noise-fitting and set reporting standards (multi-seed CIs) for future work.
- **Why Possibly Novel:** Seed-variance audits exist for accuracy; nobody has done one for the uncertainty metric suite in dense prediction.
- **Minimal Experiment:** Train 10 seeds each for 3 UQ methods on 2 datasets; report metric CIs; compare against a systematic survey of published between-method gaps.
- **Main Risk:** Compute-heavy; and one benchmark's variance may not generalize to all settings.
- **Research Cluster:** UNCERTAINTY / EVAL-WEAK

### IDEA-B-0120 — Selective-prediction results are inflated by threshold selection on test
- **One-sentence idea:** Audit the selective-prediction / failure-detection literature for threshold and operating-point selection using test-set information, and measure the honest-performance drop under strictly held-out selection.
- **Problem:** Risk-coverage and abstention results often involve choices (thresholds, rejection rates, bin edges) implicitly tuned where they are evaluated, inflating reported safety gains in ways invisible to readers.
- **Core Hypothesis (falsifiable):** Re-evaluating representative methods with all selection performed on disjoint validation data reduces reported gains substantially, and for some methods eliminates their advantage over baselines entirely.
- **Why Important:** Safety numbers taken at face value drive deployment decisions; an inflation audit protects against overtrust and fixes the protocol going forward.
- **Why Possibly Novel:** Threshold-leakage audits exist in other areas (e.g., anomaly detection); the dense-prediction selective-prediction literature has not been audited.
- **Minimal Experiment:** Reproduce 5–6 published pipelines from code; re-run with strict validation/test separation of every selection step; tabulate deltas.
- **Main Risk:** Identifying implicit leakage in each codebase requires meticulous forensic work open to dispute.
- **Research Cluster:** UNCERTAINTY / EVAL-WEAK / NEG-RESULT

### IDEA-B-0121 — Long-tail reweighting gains concentrate at head-tail confusion boundaries
- **One-sentence idea:** Localize where class-rebalancing methods actually change predictions, testing whether gains come from tail-instance recognition or from moving decision boundaries against specific head competitors.
- **Problem:** Rebalancing improves tail metrics, interpreted as "learning tail classes better," but the mechanism could be narrow: shifting a few head-vs-tail decision margins, with different implications for robustness and further method design.
- **Core Hypothesis (falsifiable):** Most of the tail-IoU improvement from standard rebalancing is accounted for by prediction flips within a small set of head-tail class pairs (confusion-flow concentration), rather than broad improvements against all competitors.
- **Why Important:** Mechanism localization tells us whether tail research should target representation (broad) or margins (narrow), and predicts side effects on the involved head classes.
- **Why Possibly Novel:** Confusion-flow accounting of rebalancing gains has not been used as the primary analysis in long-tail dense prediction.
- **Minimal Experiment:** Train baseline and rebalanced models; compute pixel-level prediction-flip flows between class pairs; quantify concentration and head-class collateral damage.
- **Main Risk:** Flow accounting is descriptive; linking it causally to the reweighting mechanism needs targeted interventions.
- **Research Cluster:** LONG-TAIL

### IDEA-B-0122 — Tail classes have noisier labels, and that — not scarcity — binds performance
- **One-sentence idea:** Audit annotation quality as a function of class frequency and test whether tail-class performance is limited more by label error than by sample count.
- **Problem:** The long-tail literature attributes tail failure to data scarcity, but annotators are less familiar with rare classes, plausibly making tail labels disproportionately wrong — a competing explanation with opposite remedies.
- **Core Hypothesis (falsifiable):** Expert re-annotation shows label error rates rising steeply with class rarity, and cleaning tail labels (at fixed count) recovers more tail performance than doubling tail sample count (at fixed quality).
- **Why Important:** Determines whether long-tail budgets should buy more data or better verification — a first-order resource decision the field has never grounded.
- **Why Possibly Novel:** Label-noise and long-tail research are separate literatures; the frequency-conditional noise audit with the clean-vs-more intervention comparison is new.
- **Minimal Experiment:** Re-annotate stratified samples across the frequency spectrum on a long-tail benchmark; measure error-rate-vs-frequency; run the matched cleaning-vs-doubling training comparison.
- **Main Risk:** Expert re-annotation of rare classes is expensive and itself error-prone, requiring adjudication protocols.
- **Research Cluster:** LONG-TAIL / ANNOT-EFF

### IDEA-B-0123 — The tail is even smaller than it looks: redundancy inflates tail counts
- **One-sentence idea:** Measure near-duplicate redundancy as a function of class frequency and re-estimate effective tail sample sizes after deduplication.
- **Problem:** Tail-class images often come from few sources (same scene, same photographer, video frames), so nominal counts overstate independent evidence; effective sample size may be far smaller than reported, changing the interpretation of every count-based analysis.
- **Core Hypothesis (falsifiable):** Effective sample size (after embedding-based near-duplicate clustering) shrinks proportionally more for tail than head classes, and effective count predicts tail performance better than nominal count across datasets.
- **Why Important:** Corrects the fundamental x-axis of long-tail research and explains cross-dataset inconsistencies in how performance scales with "count."
- **Why Possibly Novel:** Deduplication is used for test-set hygiene; frequency-conditional redundancy as a corrected covariate for long-tail science is unexamined.
- **Minimal Experiment:** Cluster near-duplicates on long-tail benchmarks; compute nominal vs. effective counts per class; compare their predictive power for per-class performance.
- **Main Risk:** Duplicate-threshold choice affects effective counts; robustness across thresholds must be shown.
- **Research Cluster:** LONG-TAIL / EVAL-WEAK

### IDEA-B-0124 — Head-trained features already contain the tail: it's a classifier problem
- **One-sentence idea:** Test whether features learned from head classes alone linearly support tail-class segmentation, localizing the long-tail problem in the classifier rather than the representation.
- **Problem:** Long-tail methods intervene throughout training, but if frozen head-only features admit accurate tail probes, most of that machinery targets the wrong component.
- **Core Hypothesis (falsifiable):** Probes trained on frozen head-only representations reach within a small margin of joint-training tail IoU, and the gap correlates with tail classes' visual distance to the head-class manifold — identifying the minority of genuinely representation-limited tail classes.
- **Why Important:** Decoupled analysis redirects long-tail effort toward cheap classifier-stage fixes for most classes and representation work only where warranted.
- **Why Possibly Novel:** Decoupling is established in long-tail classification; the dense-prediction version with a per-class representational-distance account is not.
- **Minimal Experiment:** Train head-only backbones; fit tail probes at several capacities; compare against joint training per class; regress gaps on feature-space distances.
- **Main Risk:** "Head-only" training still sees tail pixels as unlabeled context, leaking information that complicates interpretation.
- **Research Cluster:** LONG-TAIL / REP-MISMATCH

### IDEA-B-0125 — Mean-per-class IoU rewards reckless rare-class prediction
- **One-sentence idea:** Quantify how mIoU's class averaging incentivizes false-positive-heavy behavior on rare classes and evaluate FP-sensitive alternatives for ranking stability.
- **Problem:** For a rare class, predicting it liberally costs little IoU on other classes' scores but can raise its own from zero, so mIoU-optimal behavior includes hallucinating rare classes — an incentive baked into the field's headline metric.
- **Core Hypothesis (falsifiable):** Models tuned to maximize mIoU exhibit rare-class FP rates far above their base rates, and re-ranking benchmarks with FP-adjusted metrics changes leaderboard order materially while agreeing better with human quality judgments.
- **Why Important:** The headline metric shapes a decade of method development; demonstrating and fixing a hallucination incentive matters for every downstream consumer.
- **Why Possibly Novel:** mIoU criticism is folklore; the incentive quantification with tuning experiments and human-validated alternative rankings is not published.
- **Minimal Experiment:** Tune models under mIoU vs. FP-adjusted objectives; measure rare-class FP behavior; run human preference validation of both rankings.
- **Main Risk:** Alternative metrics import their own incentive pathologies, requiring careful analysis rather than advocacy.
- **Research Cluster:** LONG-TAIL / EVAL-WEAK

### IDEA-B-0126 — Tail classes need discrimination, not segmentation: the two-stage test
- **One-sentence idea:** Test whether tail-class failure is a recognition problem by comparing end-to-end tail segmentation against class-agnostic segmentation followed by region classification.
- **Problem:** Long-tail segmentation entangles two abilities — delineating regions and naming them; if class-agnostic masks for tail instances are already good, the tail problem reduces to few-shot classification of regions, a much better-understood problem.
- **Core Hypothesis (falsifiable):** Class-agnostic mask quality (matched against GT regions) shows little frequency dependence, while region-naming accuracy shows steep frequency dependence — and a two-stage pipeline beats end-to-end training on tail IoU at matched compute.
- **Why Important:** Reframing the long tail as post-hoc region classification would reroute the subfield toward retrieval/few-shot techniques and away from segmentation-specific machinery.
- **Why Possibly Novel:** Class-agnostic mask generalization is known informally (promptable models), but the frequency-decomposition of the two abilities and the head-to-head pipeline comparison is not established science.
- **Minimal Experiment:** Evaluate class-agnostic proposals on tail GT regions across frequencies; train a region classifier; compare full pipelines per frequency bin.
- **Main Risk:** Errors compound across stages; fair end-to-end comparison requires tuning both pipelines honestly.
- **Research Cluster:** LONG-TAIL

### IDEA-B-0127 — Context compatibility predicts when copy-paste helps tail classes
- **One-sentence idea:** Build and validate a context-compatibility score that predicts, per class, whether copy-paste augmentation will help or hurt tail performance.
- **Problem:** Copy-paste for rare classes sometimes fails, folk-attributed to "unrealistic context," but there is no predictive account of when pasting out-of-context helps (diversity) versus hurts (teaching wrong context priors).
- **Core Hypothesis (falsifiable):** The per-class effect of copy-paste on tail IoU is predicted (sign and rough magnitude) by a measurable compatibility statistic between paste contexts and the class's natural context distribution, with a zero-crossing that separates helped from harmed classes.
- **Why Important:** Converts a hit-or-miss augmentation into a predictable tool and quantifies how much dense models rely on context priors per class.
- **Why Possibly Novel:** Context effects on detection are studied; a validated predictive compatibility score for augmentation planning is new.
- **Minimal Experiment:** Run per-class copy-paste ablations on a long-tail benchmark; fit the compatibility statistic from context embeddings; validate prediction on held-out classes.
- **Main Risk:** Per-class effects are noisy (few test instances), demanding aggregated validation designs.
- **Research Cluster:** LONG-TAIL / SYNTH-DATA

### IDEA-B-0128 — The tail must be measured against pretraining, not the fine-tuning set
- **One-sentence idea:** Test whether class frequency in web-scale pretraining data predicts downstream tail-class performance better than frequency in the task dataset.
- **Problem:** Long-tail benchmarks define rarity by task-dataset counts, but foundation-model-era systems arrive with knowledge from pretraining; a "rare" class common on the web may not behave like a tail class at all.
- **Core Hypothesis (falsifiable):** For models fine-tuned from web-pretrained backbones, estimated pretraining-corpus frequency explains more variance in per-class performance than task-dataset frequency, and the classic long-tail performance curve flattens when re-plotted against pretraining frequency.
- **Why Important:** Redefines the operative variable of an entire subfield for the current era and predicts which benchmark tails are already solved by scale.
- **Why Possibly Novel:** Concept-frequency effects on zero-shot performance are studied for classification; the reframing of supervised long-tail dense-prediction benchmarks around it is not.
- **Minimal Experiment:** Estimate class frequencies in an open pretraining corpus (caption matching); fit per-class performance against both frequency variables for several fine-tuned models; compare explanatory power.
- **Main Risk:** Pretraining frequency estimation is noisy and correlated with task frequency, requiring careful statistical separation.
- **Research Cluster:** LONG-TAIL / CROSS-DOMAIN

### IDEA-B-0129 — Pixel frequency, not instance frequency, is the operative long-tail variable
- **One-sentence idea:** Disentangle class rarity by instance count from rarity by pixel share and determine which one performance actually follows in dense prediction.
- **Problem:** A class can be instance-rare but pixel-abundant (few large objects) or instance-common but pixel-scarce (many tiny objects); long-tail methods bin classes by instance counts while the training signal scales with pixels.
- **Core Hypothesis (falsifiable):** Per-class IoU correlates substantially more strongly with pixel share than instance count across benchmarks, and rebalancing by pixel share outperforms instance-count rebalancing at matched configuration.
- **Why Important:** If the field has been stratifying and rebalancing on the wrong variable, a simple bookkeeping correction improves both analysis and methods.
- **Why Possibly Novel:** The instance/pixel frequency distinction is rarely made explicit and never tested as competing explanatory variables for dense prediction.
- **Minimal Experiment:** Compute both frequency variables for standard benchmarks; compare correlation structures; run the matched rebalancing comparison.
- **Main Risk:** The two variables correlate strongly for many classes, limiting statistical separability to specific class subsets.
- **Research Cluster:** LONG-TAIL

### IDEA-B-0130 — Tail-class learning shows phase-transition dynamics
- **One-sentence idea:** Characterize the training dynamics of tail-class performance to test whether tail classes are acquired abruptly (and forgotten abruptly) rather than gradually.
- **Problem:** Training curves are monitored in aggregate; if tail classes flip between learned/unlearned states discontinuously, single-checkpoint evaluation misrepresents capability and per-class early stopping could harvest large gains.
- **Core Hypothesis (falsifiable):** Per-tail-class IoU trajectories exhibit abrupt transitions and inter-seed timing variance far exceeding head classes, and per-class checkpoint selection (oracle) yields a substantial aggregate tail improvement over any single checkpoint.
- **Why Important:** Reveals optimization-dynamics structure in the long tail and quantifies how much performance current single-checkpoint practice leaves on the table.
- **Why Possibly Novel:** Example-level learning dynamics are studied in classification ("forgetting events"); class-level phase behavior in dense prediction is uncharted.
- **Minimal Experiment:** Log dense per-class metrics across training for multiple seeds; classify trajectory shapes; compute the oracle-checkpoint bound.
- **Main Risk:** Per-class trajectories on small validation sets are noisy; needs larger evaluation slices or smoothing that could mask transitions.
- **Research Cluster:** LONG-TAIL / PHENOMENON

### IDEA-B-0131 — The unreported hallucination cost of long-tail methods
- **One-sentence idea:** Systematically measure how rare-class false-positive rates scale with rebalancing strength across long-tail methods, quantifying a safety cost the literature does not report.
- **Problem:** Long-tail papers report tail recall-oriented metrics; if methods buy tail IoU by hallucinating rare classes on head pixels, deployed systems inherit unquantified false-alarm behavior.
- **Core Hypothesis (falsifiable):** Across method families, rare-class FP rate grows superlinearly with the effective rebalancing strength, and methods with equal tail IoU differ by large factors in FP cost — an axis invisible in standard reporting.
- **Why Important:** Establishes a two-axis (recall/hallucination) reporting standard for long-tail work and identifies which methods are deployable in false-alarm-sensitive settings.
- **Why Possibly Novel:** Individual papers note precision drops; a cross-method FP-cost scaling study with a proposed reporting standard is missing.
- **Minimal Experiment:** Re-run representative long-tail methods across strength settings; plot tail-IoU-vs-FP-rate frontiers; compare frontier positions across families.
- **Main Risk:** Overlaps conceptually with the metric critique of IDEA-B-0125; must stay focused on method behavior rather than metric design.
- **Research Cluster:** LONG-TAIL / EVAL-WEAK

### IDEA-B-0132 — Open-vocabulary models convert the long tail into prompt sensitivity
- **One-sentence idea:** Measure whether open-vocab segmentation "solves" tail classes or relocates the problem into variance across prompt phrasings for rare concepts.
- **Problem:** Open-vocabulary systems claim to escape closed-set long-tail limits, but rare concepts have unstable name-to-appearance mappings in web data; performance may swing wildly with synonym choice, making the tail problem a prompt-engineering problem.
- **Core Hypothesis (falsifiable):** Across-prompt performance variance for tail classes is several times larger than for head classes in open-vocab segmenters, and the best-prompt-vs-median-prompt gap for tail classes exceeds typical closed-set long-tail method gains.
- **Why Important:** Deployment reliability requires knowing whether a class "works" or only "works when phrased luckily"; prompt variance is the honest metric for open-vocab tail claims.
- **Why Possibly Novel:** Prompt sensitivity is studied for classification zero-shot; the frequency-conditional variance analysis for dense prediction is new.
- **Minimal Experiment:** Build synonym/phrasing sets per class; evaluate open-vocab segmenters across them; report frequency-conditional variance and best-median gaps.
- **Main Risk:** Synonym set construction affects results; requires principled generation and sensitivity analysis.
- **Research Cluster:** LONG-TAIL / MULTIMODAL-SUP

### IDEA-B-0133 — Few-shot tail fine-tuning damages head classes at shared boundaries
- **One-sentence idea:** Localize the interference caused by fine-tuning on new tail classes, testing whether forgetting concentrates at decision boundaries the tail shares with specific head classes.
- **Problem:** Adding rare classes post hoc is common practice; aggregate metrics show mild head degradation, but if the damage concentrates on particular head classes and spatial contexts, aggregate reporting hides operationally serious regressions.
- **Core Hypothesis (falsifiable):** Head-class degradation after tail fine-tuning is strongly concentrated in feature-space neighborhoods of the added classes (predictable in advance from class similarity), rather than diffuse, and rehearsal targeted at only the predicted-vulnerable classes prevents most of it at a fraction of full-rehearsal cost.
- **Why Important:** Enables safe incremental class addition with cheap targeted protection — a recurring industrial need — and maps interference structure in dense models.
- **Why Possibly Novel:** Catastrophic forgetting is studied broadly; the predictive locality claim and targeted-rehearsal validation for segmentation class-addition is specific and new.
- **Minimal Experiment:** Fine-tune on held-out tail classes; measure per-head-class and per-region degradation; test the similarity-based vulnerability predictor; run targeted vs. full rehearsal.
- **Main Risk:** Interference may partly propagate through shared normalization statistics, adding a diffuse component that weakens the locality claim.
- **Research Cluster:** LONG-TAIL / GENERALIZATION

### IDEA-B-0134 — Oversampling tail images teaches their contexts, not their classes
- **One-sentence idea:** Test whether image-level oversampling for tail classes creates context shortcuts, evaluated by context-swapped test sets.
- **Problem:** Repeating the few images containing tail classes also repeats their backgrounds; models may learn "this scene type contains class X" rather than X's appearance, inflating benchmark tail scores that share those contexts.
- **Core Hypothesis (falsifiable):** Tail-class performance of oversampling-trained models drops disproportionately (relative to baseline models) when tail instances are evaluated in swapped or neutralized contexts, and the drop scales with per-class context repetition during training.
- **Why Important:** Identifies a hidden overfitting mode of the most common long-tail remedy and motivates context-diversifying alternatives measured honestly.
- **Why Possibly Novel:** Context bias and oversampling are both known; their interaction as a measurable shortcut mechanism with repetition-scaling evidence is not.
- **Minimal Experiment:** Train with varying repeat factors; build context-swapped tail evaluations (inpainting/compositing); plot context-dependence vs. repetition.
- **Main Risk:** Compositing artifacts may differentially affect models, requiring artifact controls.
- **Research Cluster:** LONG-TAIL / GENERALIZATION

### IDEA-B-0135 — The within-class size tail behaves like a class tail
- **One-sentence idea:** Test whether rare sizes within a common class (e.g., very large pedestrians, tiny cars) fail analogously to rare classes and respond to the same rebalancing machinery.
- **Problem:** Long-tail analysis stops at class granularity, but training distributions are also skewed over intra-class factors (size, pose); if rare-factor instances fail like rare classes, long-tail theory generalizes and per-class metrics hide a second tail.
- **Core Hypothesis (falsifiable):** Per-size-bin performance within head classes follows the same frequency-performance law as across-class tails (matched exponents), and size-rebalanced sampling improves rare-size performance the way class rebalancing improves rare classes.
- **Why Important:** Unifies long-tail phenomena at the factor level, exposes hidden failure regimes inside "solved" classes, and transfers a mature toolbox to a new axis.
- **Why Possibly Novel:** Size stratification exists descriptively; the quantitative frequency-law comparison and rebalancing transfer test make it a science question.
- **Minimal Experiment:** Fit frequency-performance curves across class and size axes on detection/segmentation benchmarks; run size-rebalancing training; compare law parameters.
- **Main Risk:** Size effects entangle with the resolution mechanisms of the SMALL-OBJ cluster, requiring joint controls.
- **Research Cluster:** LONG-TAIL / SMALL-OBJ

### IDEA-B-0136 — Geographic clustering makes tail evaluations leak
- **One-sentence idea:** Quantify how geographically clustered tail-class instances cause random train/test splits to overestimate tail generalization, using location-disjoint re-splits.
- **Problem:** Rare classes often come from few places (one country's trams, one hospital's scanner); random splits put near-identical instances on both sides, so measured tail performance reflects memorization of a site, not the class.
- **Core Hypothesis (falsifiable):** Location-disjoint splits reduce measured tail-class performance substantially more than head-class performance, and the per-class drop is predicted by the geographic concentration of that class's instances.
- **Why Important:** Corrects the field's estimate of how solved the tail actually is and motivates split standards that report geographic disjointness.
- **Why Possibly Novel:** Geographic bias in datasets is documented; its interaction with frequency (why tails leak worse) and the concentration-based predictor are new.
- **Minimal Experiment:** Use datasets with location metadata; construct random vs. location-disjoint splits; compare per-class deltas against concentration indices.
- **Main Risk:** Location metadata is missing for many benchmarks, restricting the study to a subset of datasets.
- **Research Cluster:** LONG-TAIL / EVAL-WEAK

### IDEA-B-0137 — Tail masks are right, tail labels are wrong: decomposing tail IoU
- **One-sentence idea:** Decompose tail-class IoU deficits into delineation error vs. naming error to test whether tail regions are correctly segmented under wrong labels.
- **Problem:** Low tail IoU is read as total failure, but if the model segments the region correctly and merely names it as a similar head class, the deficit is a classification margin issue with cheap remedies (post-hoc renaming, margin tuning).
- **Core Hypothesis (falsifiable):** For a majority of tail-class errors, a GT-region-matched analysis finds an accurate predicted region under an incorrect label, and oracle relabeling of predicted regions recovers most of the tail-IoU gap — far more than oracle boundary correction does.
- **Why Important:** Redirects tail remedies from segmentation machinery to naming calibration, and changes how tail progress should be measured (complementary to IDEA-B-0126's pipeline test).
- **Why Possibly Novel:** Error decomposition tools exist for detection (TIDE-style); the naming-vs-delineation decomposition as the central long-tail diagnosis is not established.
- **Minimal Experiment:** Implement the two oracle corrections on several models' predictions over a long-tail benchmark; report recovered IoU per correction per frequency bin.
- **Main Risk:** Region matching for badly fragmented predictions is ambiguous, requiring robust matching protocols.
- **Research Cluster:** LONG-TAIL

### IDEA-B-0138 — Does logit-adjustment theory survive spatial correlation?
- **One-sentence idea:** Test whether the classification-theory equivalence between loss reweighting and post-hoc logit adjustment holds in dense prediction, where pixels are correlated and context couples classes.
- **Problem:** Long-tail theory built on IID classification predicts certain rebalancing equivalences; segmentation violates IID (spatial correlation, co-occurrence), and nobody has checked whether the theory's guidance transfers or misleads.
- **Core Hypothesis (falsifiable):** The predicted equivalence fails systematically in segmentation: post-hoc adjustment and training-time reweighting produce measurably different solutions (different confusion flows and boundary placements), with the divergence growing with class co-occurrence strength.
- **Why Important:** Determines whether the field can safely import long-tail classification theory or needs dense-prediction-specific theory — a foundational question for method design.
- **Why Possibly Novel:** The equivalence is assumed in practice; a purpose-built test of its failure modes under spatial statistics is new.
- **Minimal Experiment:** Train matched reweighted vs. adjusted models on segmentation benchmarks; compare per-class results, confusion flows, and boundary behavior; correlate divergence with co-occurrence statistics.
- **Main Risk:** Optimization noise may swamp the theoretical divergence at practical scales.
- **Research Cluster:** LONG-TAIL / PHENOMENON

### IDEA-B-0139 — Timing beats weighting: introduce tail classes late
- **One-sentence idea:** Compare curriculum timing (training head classes first, introducing tail supervision late) against standard rebalancing at matched compute for long-tail dense prediction.
- **Problem:** Rebalancing manipulates the loss landscape throughout training, risking early overfitting to few tail examples; if tail classes are best learned briefly atop mature representations, when matters more than how much.
- **Core Hypothesis (falsifiable):** Late-introduction schedules match or beat the best reweighting baselines on tail IoU while causing less head-class damage, and the optimal introduction point tracks a measurable representation-maturity statistic rather than a fixed epoch fraction.
- **Why Important:** A schedule-level solution is simpler and more composable than loss machinery, and the maturity-statistic link would connect long-tail practice to representation-learning dynamics.
- **Why Possibly Novel:** Curricula and rebalancing are both studied, but the direct timing-vs-weighting comparison with a predictive introduction criterion is not.
- **Minimal Experiment:** Sweep introduction schedules against tuned reweighting at matched budgets; track the maturity statistic; validate the predicted optimal timing on a second dataset.
- **Main Risk:** Schedule space is large; unfair tuning asymmetry between arms could bias conclusions either way.
- **Research Cluster:** LONG-TAIL

### IDEA-B-0140 — Negative result: meta-learning for long-tail segmentation
- **One-sentence idea:** Rigorously test whether meta-learning-based long-tail segmentation methods beat simple logit-adjustment and rebalancing baselines under matched tuning budgets.
- **Problem:** A strand of long-tail work employs meta-learned weighting/adaptation with substantial complexity; their comparisons often feature under-tuned simple baselines, leaving the genre's real value unknown.
- **Core Hypothesis (falsifiable):** Under equalized hyperparameter search budgets and modern recipes, meta-learning methods provide no significant tail-IoU advantage over logit adjustment plus square-root sampling on standard long-tail segmentation benchmarks.
- **Why Important:** Complexity that adds nothing costs the field in reproducibility and adoption; a careful negative would prune the method space and raise baseline standards.
- **Why Possibly Novel:** Strong-baseline audits exist for long-tail classification; the segmentation-specific audit with tuning-budget matching is missing.
- **Minimal Experiment:** Reproduce 3–4 meta-learning long-tail methods from code; grant baselines equal search budget; report multi-seed comparisons on two benchmarks.
- **Main Risk:** Reproduction fidelity disputes; must engage original code and authors' recommended settings.
- **Research Cluster:** LONG-TAIL / NEG-RESULT

### IDEA-B-0141 — Long-tail rankings are unstable under benchmark re-splits
- **One-sentence idea:** Measure how much long-tail method rankings change under alternative reasonable train/test partitions of the same data.
- **Problem:** Tail metrics depend on which few instances land in the test set; a single canonical split may make method comparisons an artifact of one partition rather than a property of methods.
- **Core Hypothesis (falsifiable):** Across resampled splits (preserving frequency structure), the ranking of representative long-tail methods varies enough that a majority of published pairwise orderings reverse in a nontrivial fraction of splits.
- **Why Important:** If rankings are split-artifacts, the subfield needs multi-split evaluation as standard practice — a cheap fix with large epistemic payoff.
- **Why Possibly Novel:** Split-sensitivity is studied for small datasets in other fields; the long-tail segmentation ranking-stability audit is new.
- **Minimal Experiment:** Generate 20 stratified re-splits of a long-tail benchmark; evaluate 6 methods (retrained per split); report ranking-reversal statistics.
- **Main Risk:** Retraining per split is expensive; a prediction-reuse approximation must be validated first.
- **Research Cluster:** LONG-TAIL / EVAL-WEAK

### IDEA-B-0142 — Long-tail methods overfit the tail's shape (Zipf exponent)
- **One-sentence idea:** Test whether long-tail methods tuned on one frequency distribution transfer to datasets with different tail shapes, using the fitted Zipf exponent as the predictive variable.
- **Problem:** Methods are developed on benchmarks with particular frequency decay; real deployments have different decay shapes, and nothing is known about whether method choices (weighting exponents, sampling powers) transfer across tail geometries.
- **Core Hypothesis (falsifiable):** The optimal rebalancing configuration shifts systematically with the dataset's Zipf exponent, and per-method transfer loss across tail shapes is predicted by exponent mismatch — with some method families measurably more shape-robust than others.
- **Why Important:** Provides deployment guidance (how to adapt configurations to a new distribution) and exposes shape-overfitting as an unrecognized generalization axis.
- **Why Possibly Novel:** Frequency-distribution shape as an explicit experimental variable, with resampled-tail controlled datasets, has not been studied for dense prediction.
- **Minimal Experiment:** Construct resampled variants of one dataset with controlled Zipf exponents; tune methods per variant; measure cross-variant transfer matrices.
- **Main Risk:** Resampling changes total data volume alongside shape; matched-volume designs are essential.
- **Research Cluster:** LONG-TAIL / GENERALIZATION

### IDEA-B-0143 — Compositional relabeling structurally shrinks the tail
- **One-sentence idea:** Test whether relabeling tail classes as compositions (modifier + head class, e.g., "police car" = "car" + attribute) recovers tail performance by routing learning through abundant head data.
- **Problem:** Many tail classes are fine-grained variants of head classes; forcing them to be independent categories discards their shared structure and manufactures artificial scarcity.
- **Core Hypothesis (falsifiable):** A compositional labeling scheme (head class + attribute head) achieves higher effective tail-class accuracy than flat classification at matched data, with gains proportional to the tail class's semantic overlap with its head parent.
- **Why Important:** Suggests the long tail is partly an ontology-design artifact — fixable in the label space rather than the learning algorithm.
- **Why Possibly Novel:** Compositional recognition exists as a topic; its use as a long-tail intervention with an overlap-based predictive account in dense prediction is fresh.
- **Minimal Experiment:** Re-express a benchmark's tail classes compositionally where semantically valid; train flat vs. compositional heads; compare per-class results against overlap measures.
- **Main Risk:** Only a subset of tail classes decompose cleanly; the method's scope must be honestly bounded.
- **Research Cluster:** LONG-TAIL / REP-MISMATCH

### IDEA-B-0144 — Background pixels are contaminated with unlabeled tail instances
- **One-sentence idea:** Audit the rate at which tail-class instances hide unlabeled inside "background" regions and measure the training damage this contamination causes.
- **Problem:** Annotation vocabularies and annotator familiarity mean rare objects often go unmarked, becoming hard negatives that actively teach the model to suppress exactly the classes it most needs to learn.
- **Core Hypothesis (falsifiable):** Model-assisted plus human-verified auditing finds tail-class contamination rates in background regions several times higher than head-class rates, and masking suspected contamination out of the negative loss improves tail IoU measurably without hurting head classes.
- **Why Important:** Identifies a self-sabotage mechanism built into standard training and a cheap mitigation, while quantifying a dataset-quality dimension nobody reports.
- **Why Possibly Novel:** Missing-annotation effects are studied in detection (sparse-annotation training); the frequency-conditional contamination audit and its long-tail interpretation are new for segmentation.
- **Minimal Experiment:** Run high-recall detectors for tail classes over background regions of a benchmark; verify samples with humans; retrain with contamination-masked negatives; compare tail metrics.
- **Main Risk:** Verification of rare classes is exactly where humans err too, requiring expert adjudication for a subset.
- **Research Cluster:** LONG-TAIL / ANNOT-EFF

### IDEA-B-0145 — Open-set abstention improves closed-set tail metrics
- **One-sentence idea:** Test whether allowing an explicit "unknown object" output improves tail-class performance even under closed-set evaluation, by relieving forced misclassification pressure.
- **Problem:** Closed-set training forces every ambiguous rare region into some known class, distorting decision boundaries; an unknown channel might absorb that pressure and paradoxically improve the known-class tail.
- **Core Hypothesis (falsifiable):** Models trained with an unknown-region objective (using held-out-class proxies) show improved tail-class IoU under standard closed-set evaluation compared to matched closed-set baselines, with gains concentrated on tail classes bordering high-ambiguity regions.
- **Why Important:** Would show open-set machinery is not just a safety add-on but a training-quality intervention for the long tail — unifying two subfields' motivations.
- **Why Possibly Novel:** Open-set segmentation targets unknown detection; its causal back-effect on closed-set tail quality is unexamined.
- **Minimal Experiment:** Train with/without unknown-channel objectives (leave-out-class protocol); evaluate closed-set tail metrics on the retained vocabulary; localize gains.
- **Main Risk:** Proxy-unknown construction choices may drive results, needing multiple protocols to agree.
- **Research Cluster:** LONG-TAIL / UNCERTAINTY

### IDEA-B-0146 — Frequency predicts fragility: the tail is also less robust
- **One-sentence idea:** Test whether class frequency predicts corruption/shift sensitivity, unifying the long-tail and robustness axes into one empirical law.
- **Problem:** Robustness is evaluated in aggregate and long-tail in clean conditions; if rare classes degrade faster under corruption, deployed systems fail earliest exactly where monitoring is thinnest, and the two literatures need joint treatment.
- **Core Hypothesis (falsifiable):** Per-class robustness slopes (performance vs. corruption severity) correlate strongly with training frequency across datasets and models, and the correlation survives controls for class difficulty and object size.
- **Why Important:** A frequency-fragility law would let practitioners predict shift behavior from training statistics alone and force long-tail methods to report robustness effects.
- **Why Possibly Novel:** Both axes are heavily studied separately; the systematic coupling law with confound controls has not been established for dense prediction.
- **Minimal Experiment:** Evaluate per-class metrics across a corruption ladder for several models/datasets; fit and validate the frequency-slope relationship with covariate controls.
- **Main Risk:** Frequency confounds with many class properties; residual confounding will be the main critique to preempt.
- **Research Cluster:** LONG-TAIL / ROBUSTNESS

### IDEA-B-0147 — Repeat-factor sampling and strong augmentation are substitutes, not complements
- **One-sentence idea:** Map the interaction between tail oversampling and augmentation strength to test whether they supply the same missing ingredient (effective diversity).
- **Problem:** Recipes stack oversampling and augmentation as if independent; if both act by inflating effective tail diversity, their combination wastes compute and overfits differently than either alone.
- **Core Hypothesis (falsifiable):** The tail-IoU response surface over (repeat factor x augmentation strength) exhibits strong negative interaction — the marginal value of each collapses when the other is high — consistent with a shared mechanism, not additive benefits.
- **Why Important:** Interaction maps replace one-factor-at-a-time recipe lore with dose-response understanding, directly informing budget allocation.
- **Why Possibly Novel:** Both knobs are universally used but their interaction surface has never been mapped for long-tail dense prediction.
- **Minimal Experiment:** Train a factorial grid over both knobs on a long-tail benchmark; fit interaction terms; test the shared-mechanism prediction on effective-diversity statistics.
- **Main Risk:** Factorial training grids are compute-hungry; needs efficient (smaller-model) pilot generalization checks.
- **Research Cluster:** LONG-TAIL

### IDEA-B-0148 — Describability predicts when generated data can fix a tail class
- **One-sentence idea:** Test whether the benefit of text-to-image synthetic data for a tail class is predicted by how well language specifies that class's visual appearance.
- **Problem:** Generative augmentation for rare classes works unevenly; practitioners cannot predict which classes will benefit, and the folk explanation ("generation quality") is circular without a measurable predictor.
- **Core Hypothesis (falsifiable):** Per-class synthetic-data gains correlate strongly with a describability score (text-image alignment consistency for the class name/description), and classes below a describability threshold are actively harmed by synthetic data.
- **Why Important:** Provides an actionable pre-generation triage tool and connects multimodal alignment structure to data-augmentation efficacy.
- **Why Possibly Novel:** Synthetic-data-for-tail studies report aggregate gains; the per-class predictive model based on language-vision alignment is new.
- **Minimal Experiment:** Generate matched synthetic sets for many tail classes; train with each; regress per-class gains on describability scores; validate the threshold prospectively on held-out classes.
- **Main Risk:** Describability scores derived from the same model family as the generator risk circularity; needs independent scoring models.
- **Research Cluster:** LONG-TAIL / SYNTH-DATA / MULTIMODAL-SUP

### IDEA-B-0149 — Thing-vs-stuff assignment errors dominate rare-class panoptic scores
- **One-sentence idea:** Audit whether rare classes are disproportionately mis-assigned between thing/stuff regimes in GT and measure the panoptic-metric damage from this ontology noise.
- **Problem:** Panoptic annotation forces every class into thing or stuff treatment; rare classes get this assignment with little scrutiny, and a wrong regime (e.g., countable objects annotated as amorphous regions) makes their panoptic scores structurally unachievable.
- **Core Hypothesis (falsifiable):** Expert review finds regime-assignment disputes concentrated in rare classes, and re-scoring under corrected assignments changes rare-class PQ substantially more than typical method gains on those classes.
- **Why Important:** Ontology noise is invisible infrastructure error; quantifying it protects method research from optimizing against category mistakes.
- **Why Possibly Novel:** Panoptic ontology design has not been audited as an error source, especially in its interaction with class rarity.
- **Minimal Experiment:** Expert-review regime assignments for a benchmark's rare classes; re-annotate disputed ones both ways on a subset; re-score public models under both ontologies.
- **Main Risk:** "Correct" regime is genuinely contested for some classes; the study must report ranges, not single answers.
- **Research Cluster:** LONG-TAIL / EVAL-WEAK

### IDEA-B-0150 — How many tail claims survive per-class bootstrap confidence intervals?
- **One-sentence idea:** Re-analyze published long-tail segmentation results with instance-level bootstrap CIs to determine what fraction of claimed tail improvements are statistically supportable.
- **Problem:** Tail metrics rest on tiny per-class test counts (often tens of instances), yet papers report point estimates without uncertainty; the field cannot currently distinguish progress from sampling noise.
- **Core Hypothesis (falsifiable):** Under per-class bootstrap analysis of reproduced results, a large fraction of published tail-class improvements have CIs overlapping their baselines, and aggregate "tail mIoU" gains are frequently driven by a small number of high-variance classes.
- **Why Important:** Establishes statistical reporting standards for a subfield whose core quantity is intrinsically high-variance, retroactively clarifying what is known.
- **Why Possibly Novel:** Bootstrap re-analysis campaigns exist in NLP benchmarking; the long-tail dense-prediction version, with per-class variance decomposition, is missing.
- **Minimal Experiment:** Reproduce 8–10 published methods from code; compute per-class and aggregate bootstrap CIs; tabulate survival rates of claimed improvements.
- **Main Risk:** Reproduction gaps could be conflated with statistical fragility; both must be reported separately.
- **Research Cluster:** LONG-TAIL / EVAL-WEAK / NEG-RESULT

### IDEA-B-0151 — Locate the budget crossover where dense mask annotation stops paying
- **One-sentence idea:** Empirically map the annotation-budget crossover between dense mask drawing and point/box prompts refined by promptable segmenters, as a function of target model quality.
- **Problem:** Promptable segmentation has changed the cost structure of mask creation, but projects still choose annotation modes by habit; the field lacks a measured frontier saying when full masks are worth their cost.
- **Core Hypothesis (falsifiable):** For most natural-image domains, point-prompted machine masks with human acceptance checks reach the same downstream model quality as hand-drawn masks at a small fraction of the cost, with the crossover reversing only for domains where promptable models systematically fail (identified in advance by a probe set).
- **Why Important:** Annotation is the dominant cost of applied vision; a validated decision curve directly moves budgets across the industry.
- **Why Possibly Novel:** Tool papers report their own efficiency; a neutral, downstream-model-quality-grounded crossover study across domains is missing.
- **Minimal Experiment:** Annotate matched subsets with both pipelines under timed conditions across three domains; train identical models on each; plot quality-vs-cost frontiers.
- **Main Risk:** Results are tied to the current promptable-model generation and may age quickly (though the methodology persists).
- **Research Cluster:** ANNOT-EFF

### IDEA-B-0152 — The time-precision curve of boundary annotation is superlinear
- **One-sentence idea:** Measure annotation time as a function of required boundary precision to quantify how much of the budget the last pixel of accuracy consumes.
- **Problem:** Dataset specifications demand uniform boundary precision without knowing its cost curve; if precision cost is superlinear, large savings are available wherever downstream models cannot exploit the final pixel anyway (see IDEA-B-0068).
- **Core Hypothesis (falsifiable):** Annotation time grows superlinearly with precision targets, and combining the measured cost curve with a measured model-sensitivity curve identifies a precision level where marginal cost exceeds marginal model benefit for typical training sets.
- **Why Important:** Provides the first principled precision specification for annotation contracts — an immediately usable economic result.
- **Why Possibly Novel:** Annotation cost studies measure per-item times; the precision-parameterized cost curve joined to model sensitivity analysis is new.
- **Minimal Experiment:** Timed annotation trials at controlled precision targets (verified against high-res references); model-training sensitivity sweep over label precision; intersect the curves.
- **Main Risk:** Precision enforcement in trials is tricky; annotators may not hit targets consistently, blurring the curve.
- **Research Cluster:** ANNOT-EFF

### IDEA-B-0153 — Region-level acquisition beats image-level acquisition at fixed budget
- **One-sentence idea:** Test whether active learning for segmentation gains more from choosing which regions to label within images than from choosing which images to label.
- **Problem:** AL research selects whole images, but annotation cost lives at the region/instance level and informativeness is spatially concentrated; the granularity of acquisition may matter more than the acquisition function.
- **Core Hypothesis (falsifiable):** At matched annotation-time budgets, region-level acquisition with a mediocre scoring function outperforms image-level acquisition with the best scoring function, across two datasets.
- **Why Important:** Would reorder AL research priorities from function design to interaction design and produce immediately deployable protocol guidance.
- **Why Possibly Novel:** Region-level AL exists in isolated papers; the granularity-vs-function-quality decomposition making granularity the headline variable is not established.
- **Minimal Experiment:** Implement matched AL loops at both granularities with two scoring functions each; use timed-cost accounting rather than image counts; compare label-efficiency curves.
- **Main Risk:** Region-level annotation has interaction overheads (context re-orientation) that must be honestly measured, not assumed away.
- **Research Cluster:** ANNOT-EFF

### IDEA-B-0154 — Many cheap noisy annotators beat few careful ones at matched cost
- **One-sentence idea:** Map the quality-quantity frontier of segmentation annotation spending — one careful pass vs. multiple fast passes aggregated — grounded in downstream model performance.
- **Problem:** Annotation vendors price carefulness steeply; whether models prefer fewer precise labels or more noisy ones (with or without aggregation) is an empirical question projects currently answer by intuition.
- **Core Hypothesis (falsifiable):** At matched total cost, aggregated fast-pass labels train models that match or exceed careful-pass models on interior accuracy, with careful passes retaining an advantage only on boundary metrics — and the frontier's shape is predicted by the noise structure (unbiased jitter vs. systematic misses).
- **Why Important:** A validated frontier converts a recurring procurement decision into engineering, and the noise-structure insight guides aggregation design.
- **Why Possibly Novel:** Noisy-label learning studies synthetic noise; real cost-matched procurement experiments with downstream grounding are rare to nonexistent for segmentation.
- **Minimal Experiment:** Commission both spending patterns on the same image set with real timing/cost data; train matched models; compare across metric axes.
- **Main Risk:** Results depend on the specific workforce and interface; needs replication across at least two annotation platforms.
- **Research Cluster:** ANNOT-EFF

### IDEA-B-0155 — Weak supervision's gap is concentrated in thin and small structures
- **One-sentence idea:** Decompose the performance gap between scribble/point supervision and full supervision by structure type, testing whether the entire gap lives in thin/small regions.
- **Problem:** Weak supervision is evaluated by aggregate mIoU gap, hiding what the missing dense signal actually provides; if the gap is structurally concentrated, hybrid schemes (dense labels only for thin structures) could close it at minimal cost.
- **Core Hypothesis (falsifiable):** Stratified evaluation shows weakly supervised models within noise of fully supervised ones on large-region interiors, with the aggregate gap dominated by thin structures and small instances — and targeted dense supervision on only those structures recovers most of the gap at <20% of full-annotation cost.
- **Why Important:** Turns weak supervision from an accuracy compromise into a precision instrument for budget allocation.
- **Why Possibly Novel:** Weakly supervised papers report aggregates; the structural decomposition and the targeted-hybrid validation are new.
- **Minimal Experiment:** Train weak/full/hybrid supervision variants; evaluate with structure-stratified metrics (skeleton recall, size bins); cost-account the hybrid.
- **Main Risk:** Structure categories overlap with class identity, requiring careful class-controlled analysis.
- **Research Cluster:** ANNOT-EFF / BOUNDARY

### IDEA-B-0156 — Model-assisted annotation creates measurable bias feedback loops
- **One-sentence idea:** Quantify how much of the assisting model's error profile is inherited by datasets created with model-in-the-loop annotation, across successive generations.
- **Problem:** Most modern datasets are produced with model pre-annotation; if annotators under-correct model errors, datasets encode model biases, and models trained on them re-validate those biases — a feedback loop nobody has measured end to end.
- **Core Hypothesis (falsifiable):** Datasets annotated with assistance from model M show error-pattern correlation with M (beyond content-driven correlation, established via assisted-vs-blind annotation of the same images), and a second-generation model trained on the assisted dataset reproduces M's characteristic errors at measurably higher rates than one trained on blind annotations.
- **Why Important:** The field's data substrate is increasingly model-shaped; quantifying inheritance rates determines how much benchmark progress is self-confirmation.
- **Why Possibly Novel:** Bias amplification is studied within models; the annotation-pipeline transmission channel with generation-over-generation measurement is new.
- **Minimal Experiment:** Annotate one image pool blind and assisted; fingerprint the assistant's errors; train next-generation models on each dataset; measure error-pattern inheritance.
- **Main Risk:** Distinguishing model-inherited errors from shared-difficulty errors requires the blind-annotation control to be well executed.
- **Research Cluster:** ANNOT-EFF / NEG-RESULT

### IDEA-B-0157 — Session drift: annotation quality decays predictably within work sessions
- **One-sentence idea:** Detect and model within-session quality drift (fatigue, habituation) in annotation timestamps, and audit public datasets for its fingerprints.
- **Problem:** Label quality is treated as annotator-constant, but sustained attention degrades; if quality varies systematically with session position, datasets carry a structured noise process that models may partially learn.
- **Core Hypothesis (falsifiable):** Controlled annotation sessions show boundary precision and instance recall declining measurably with time-on-task, and public datasets with recoverable ordering metadata show correlated artifacts (quality autocorrelation along annotation order).
- **Why Important:** A predictable noise process enables reweighting or targeted re-review, and adds a process-level variable to dataset documentation standards.
- **Why Possibly Novel:** Fatigue is studied in HCI generally; its quantitative imprint on vision dataset quality and its recoverability from metadata are unexamined.
- **Minimal Experiment:** Run timed multi-hour annotation sessions with hidden gold instances throughout; fit drift curves; apply fingerprint detection to datasets with ordering metadata.
- **Main Risk:** Most public datasets lack ordering metadata, limiting the audit arm to a few cases.
- **Research Cluster:** ANNOT-EFF / PHENOMENON

### IDEA-B-0158 — Pre-annotation makes assistant blind spots permanently unreviewable
- **One-sentence idea:** Measure the compounding miss rate for object categories the pre-annotation assistant fails on, testing whether review protocols ever recover assistant-missed instances.
- **Problem:** Review-based pipelines show humans the assistant's proposals; instances the assistant misses generate no proposal and may never receive human attention, so assistant recall silently upper-bounds dataset recall.
- **Core Hypothesis (falsifiable):** In standard review interfaces, human recovery rate for assistant-missed instances is far below their recovery rate in from-scratch annotation of the same images, and dataset versions accumulate a growing deficit for exactly the assistant's weak categories.
- **Why Important:** Identifies a structural censorship mechanism in modern dataset production that biases benchmarks against whatever current models can't see — the worst possible selection effect for measuring progress.
- **Why Possibly Novel:** Assisted-annotation studies measure speed and per-item quality, not the miss-recovery channel and its longitudinal compounding.
- **Minimal Experiment:** Seed images with verified instances the assistant misses; run standard review vs. from-scratch annotation; compare recovery rates; simulate multi-generation accumulation.
- **Main Risk:** Interface design strongly affects recovery rates; conclusions need testing across at least two common review interfaces.
- **Research Cluster:** ANNOT-EFF / EVAL-WEAK

### IDEA-B-0159 — Click-count metrics do not predict real annotation time
- **One-sentence idea:** Validate (or refute) number-of-clicks as a proxy for wall-clock annotation cost in interactive segmentation, using timed human studies.
- **Problem:** The interactive segmentation literature ranks methods by NoC@IoU, assuming clicks proxy effort, but thinking time, precision demands per click, and correction cascades may dominate real cost and reorder methods.
- **Core Hypothesis (falsifiable):** Wall-clock time per accepted mask correlates only weakly with NoC across methods, and time-based rankings of current interactive methods differ materially from NoC rankings.
- **Why Important:** If the field's headline metric misranks tools for their actual purpose (saving time), tool selection and research incentives are miscalibrated.
- **Why Possibly Novel:** Occasional user studies exist for single tools; a cross-method timed re-ranking against the NoC leaderboard is missing.
- **Minimal Experiment:** Timed study (n≈20 annotators) using 5 public interactive methods on matched instance sets; record time, clicks, quality; compare ranking structures.
- **Main Risk:** Annotator skill variance is large; within-subject designs and adequate samples are essential.
- **Research Cluster:** ANNOT-EFF / EVAL-WEAK

### IDEA-B-0160 — Semi-supervised gains shrink as labeled-set curation improves
- **One-sentence idea:** Test whether semi-supervised segmentation methods' gains depend on the labeled subset being carelessly (randomly) chosen, shrinking when the same budget is spent on a curated labeled set.
- **Problem:** SSL benchmarks sample labeled subsets uniformly, but real projects curate; if SSL's value partially duplicates what curation provides (coverage of modes), published gains overstate real-world value.
- **Core Hypothesis (falsifiable):** The SSL-over-supervised gain at fixed label budget decreases significantly when labeled subsets are diversity-curated rather than random, with a measurable fraction of SSL's benefit attributable to compensating for poor subset coverage.
- **Why Important:** Corrects the deployment-value estimate of a popular technique family and unifies SSL evaluation with realistic data practices.
- **Why Possibly Novel:** SSL and data curation are separate literatures; their substitutability has not been measured for dense prediction.
- **Minimal Experiment:** Run SSL and supervised baselines over random vs. curated labeled subsets at several budgets; compare gain surfaces.
- **Main Risk:** Curation method choice affects results; several curation strategies must be tested.
- **Research Cluster:** ANNOT-EFF / ASSUMPTION

### IDEA-B-0161 — The useful unlabeled-to-labeled ratio saturates predictably
- **One-sentence idea:** Characterize how semi-supervised segmentation performance scales with unlabeled pool size and whether the saturation point is predictable from dataset statistics.
- **Problem:** Practitioners hoard unlabeled data assuming more always helps, but SSL's marginal value must saturate; knowing the saturation law would size data pipelines rationally.
- **Core Hypothesis (falsifiable):** Performance vs. unlabeled-pool size follows a saturating curve whose knee is predicted by a measurable redundancy statistic of the pool (embedding-space coverage), transferring across datasets within error bars.
- **Why Important:** Data storage/transport of unlabeled imagery has real costs; a validated sizing rule is directly actionable engineering guidance.
- **Why Possibly Novel:** Scaling laws exist for labeled data and model size; the unlabeled-pool axis with a coverage-based predictor is unmapped for dense prediction.
- **Minimal Experiment:** Train SSL at nested unlabeled-pool sizes on two datasets; fit saturation curves; test the coverage statistic's predictive transfer.
- **Main Risk:** The law may depend on SSL method family, requiring multiple methods for generality.
- **Research Cluster:** ANNOT-EFF / PHENOMENON

### IDEA-B-0162 — Boundary supervision is redundant: partial contours train full models
- **One-sentence idea:** Test how much of each object's boundary must actually be annotated for full-supervision-equivalent training, exploiting boundary self-redundancy.
- **Problem:** Annotators trace complete contours, but if models interpolate untraced boundary segments from image evidence (per IDEA-B-0068's mechanism), most tracing effort duplicates information the model already extracts.
- **Core Hypothesis (falsifiable):** Training with masks whose boundaries are only k% traced (rest marked uncertain) matches full-supervision accuracy for k well below 50%, with the required k predicted by local edge-evidence strength.
- **Why Important:** Directly converts a redundancy measurement into an annotation-protocol change with large cost savings.
- **Why Possibly Novel:** Sparse supervision exists at region level (points/scribbles); calibrated partial-contour supervision with an evidence-based sufficiency account is unexplored.
- **Minimal Experiment:** Construct partial-boundary training sets at various k from existing dense GT; train matched models; find the sufficiency threshold and its evidence-strength dependence.
- **Main Risk:** The loss treatment of untraced segments (ignore vs. soft) may dominate results, requiring careful design.
- **Research Cluster:** ANNOT-EFF / BOUNDARY

### IDEA-B-0163 — Decouple delineation from naming: two-pass annotation wins
- **One-sentence idea:** Test whether splitting annotation into a class-agnostic mask pass and a separate region-naming pass beats joint annotation at fixed budget on both cost and quality.
- **Problem:** Joint annotation forces simultaneous spatial precision and taxonomic decisions, likely interfering with each other (context switching, taxonomy lookup during tracing); the decomposition hypothesis has never been tested experimentally.
- **Core Hypothesis (falsifiable):** Two-pass annotation yields measurably better boundary quality and naming accuracy per unit cost than joint annotation, with the advantage growing with taxonomy size.
- **Why Important:** A protocol-level result that any annotation operation can adopt immediately, grounded in task-switching cognition.
- **Why Possibly Novel:** Pipeline decompositions are used ad hoc in industry; controlled comparisons with taxonomy-size scaling analysis are absent from the literature.
- **Minimal Experiment:** Randomized annotation study across taxonomy sizes (10/100/500 classes) comparing joint vs. two-pass protocols with full cost accounting and gold-standard scoring.
- **Main Risk:** Two-pass introduces region-handoff ambiguities (what counts as one region) that may add hidden costs.
- **Research Cluster:** ANNOT-EFF

### IDEA-B-0164 — The expert premium varies by domain more than assumed
- **One-sentence idea:** Quantify where crowdworkers match domain experts in segmentation annotation and where they catastrophically fail, building a domain-difficulty predictor for workforce routing.
- **Problem:** Projects either overpay experts for everything or overtrust crowds for everything; the expertise premium is surely domain- and structure-dependent, but no quantitative routing guidance exists.
- **Core Hypothesis (falsifiable):** Crowd-vs-expert quality gaps vary by an order of magnitude across domains (natural/aerial/medical) and structure types, and a predictor based on visual familiarity plus decision-ambiguity statistics forecasts the gap well enough to route tasks.
- **Why Important:** Workforce routing is a major cost lever in dataset production; a validated predictor converts it from guesswork to policy.
- **Why Possibly Novel:** Crowd-vs-expert comparisons exist per domain in isolation; the cross-domain gap model with routing validation is new.
- **Minimal Experiment:** Commission matched crowd/expert annotation across a domain-structure grid with gold standards; fit the gap predictor; validate routing decisions on held-out task types.
- **Main Risk:** Expert availability constrains the gold-standard arm in exactly the domains where the question matters most.
- **Research Cluster:** ANNOT-EFF / CROSS-DOMAIN

### IDEA-B-0165 — Replication: dynamic pseudo-label thresholds vs. one tuned constant
- **One-sentence idea:** Test whether the genre of adaptive/curriculum pseudo-label thresholding beats a single well-tuned global threshold in semi-supervised segmentation under matched tuning budgets.
- **Problem:** Many SSL papers introduce per-class or time-varying threshold schemes, but their baselines' fixed thresholds are often un-tuned; the genre's cumulative value over honest baselines is unknown.
- **Core Hypothesis (falsifiable):** With equal hyperparameter search spent on the fixed threshold, published dynamic-thresholding methods provide no significant benefit on standard semi-supervised segmentation benchmarks, except in strongly class-imbalanced regimes where per-class adaptation retains value.
- **Why Important:** Prunes recipe complexity and establishes the regime map (when adaptation earns its complexity) for a heavily used technique family.
- **Why Possibly Novel:** Threshold schemes are compared to each other; the tuning-budget-matched audit against the simplest baseline has not been done.
- **Minimal Experiment:** Reproduce 4 dynamic-threshold methods; grant the fixed-threshold baseline equal search; compare across balanced and imbalanced benchmarks with seeds.
- **Main Risk:** Interaction with augmentation strength may differ across methods, complicating a clean verdict.
- **Research Cluster:** ANNOT-EFF / NEG-RESULT

### IDEA-B-0166 — Optimal video keyframe labeling density follows motion statistics
- **One-sentence idea:** Derive and validate a rule linking scene motion statistics to the keyframe annotation spacing that minimizes labels for target video-segmentation quality.
- **Problem:** Video datasets pick annotation frame rates by convention (every Nth frame); the information value of an extra keyframe plainly depends on scene dynamics, but no quantitative spacing rule exists.
- **Core Hypothesis (falsifiable):** Downstream quality as a function of keyframe spacing collapses across videos when spacing is normalized by a measurable motion statistic (e.g., median optical-flow magnitude), yielding a transferable optimal-spacing rule that beats fixed-rate annotation at matched budget.
- **Why Important:** Video annotation costs scale with frame count; a content-adaptive spacing rule saves real budget across every video dataset project.
- **Why Possibly Novel:** Label propagation research optimizes the propagator; the annotation-density planning question with a validated normalization law is untouched.
- **Minimal Experiment:** Subsample dense-GT video benchmarks at controlled spacings; train/propagate; test curve collapse under motion normalization; validate the rule prospectively on new videos.
- **Main Risk:** Scene cuts and irregular motion may break any single-statistic normalization, requiring piecewise treatment.
- **Research Cluster:** ANNOT-EFF

### IDEA-B-0167 — Review passes catch the wrong errors: verification is precision-biased
- **One-sentence idea:** Characterize the error-type profile of annotation review passes, testing whether second-pass QA fixes boundary details while systematically failing to add missed instances.
- **Problem:** QA budgets assume review "improves quality" generically; if reviewers predominantly adjust visible annotations rather than discover absent ones, datasets end up boundary-polished but recall-deficient — the same failure axis as IDEA-B-0158, here for human-only pipelines.
- **Core Hypothesis (falsifiable):** In controlled review experiments with known error seeds, correction rates for boundary/label errors are several times higher than discovery rates for planted omissions, and recall-oriented review protocols (checklist prompts, region coverage tools) close most of the discovery deficit.
- **Why Important:** Redirects QA design toward the dominant residual error type and quantifies what a "reviewed" dataset actually guarantees.
- **Why Possibly Novel:** Annotation QA is an industry practice without published error-type efficacy measurements or protocol comparisons.
- **Minimal Experiment:** Seed datasets with calibrated error mixtures; run standard vs. recall-oriented review; compare per-error-type detection rates and costs.
- **Main Risk:** Seeded errors may be easier or harder than natural ones; needs natural-error validation subsets.
- **Research Cluster:** ANNOT-EFF

### IDEA-B-0168 — Correcting machine masks is faster than drawing, even at high error rates
- **One-sentence idea:** Measure the correction-vs-creation time asymmetry to find the pre-annotation quality threshold below which machine proposals stop saving time.
- **Problem:** Teams assume pre-annotation only helps when the model is good; but if correcting even mediocre masks beats drawing from scratch, assistance thresholds can be far more permissive — while a too-low threshold may cost quality via anchoring (link to IDEA-B-0098).
- **Core Hypothesis (falsifiable):** Wall-clock time to acceptable masks remains below from-scratch time until proposal quality drops beneath a surprisingly low IoU threshold, but final quality degrades via under-correction before the time advantage disappears — the two thresholds do not coincide.
- **Why Important:** The gap between the time threshold and quality threshold defines a danger zone (fast but silently degraded labels) that operations must know about.
- **Why Possibly Novel:** Assisted-annotation timing studies exist for single tools; the two-threshold structure (speed vs. fidelity) has not been articulated or measured.
- **Minimal Experiment:** Present annotators proposals at controlled quality levels; measure time and final accuracy against gold; locate both thresholds.
- **Main Risk:** Threshold locations likely depend on interface affordances (eraser vs. vertex editing), requiring multi-interface replication.
- **Research Cluster:** ANNOT-EFF

### IDEA-B-0169 — Payment structure shapes boundary bias direction
- **One-sentence idea:** Test whether per-item vs. hourly annotator compensation causally changes not just quality level but the direction of systematic boundary errors.
- **Problem:** Datasets inherit workforce incentive structures invisibly; piece rates reward speed (predicting corner-cutting: overly smooth, inside-drawn boundaries) while hourly rates permit care — if incentive leaves a directional fingerprint, datasets encode economics, not just imagery.
- **Core Hypothesis (falsifiable):** Randomizing compensation scheme across matched annotator pools produces measurably different signed boundary offsets and vertex-density distributions, and these fingerprints are detectable in public datasets with known procurement histories.
- **Why Important:** Connects dataset bias to production economics, informing both procurement standards and cross-dataset comparability analyses (interacts with IDEA-B-0043's model-bias findings).
- **Why Possibly Novel:** Incentive effects on quality are studied in crowdsourcing generally; directional geometric fingerprints in vision GT are unmeasured.
- **Minimal Experiment:** Randomized compensation experiment with gold-standard geometry scoring; fingerprint search in datasets with documented pipelines.
- **Main Risk:** Ethical/IRB constraints on compensation experiments; effect may be swamped by individual annotator variance.
- **Research Cluster:** ANNOT-EFF / PHENOMENON

### IDEA-B-0170 — Annotating finer classes than needed improves the coarse labels
- **One-sentence idea:** Test whether requiring annotators to label at finer granularity than the target ontology improves the accuracy of the (merged) coarse labels enough to justify the extra cost.
- **Problem:** Ontology granularity is chosen to match the target task, assuming finer labeling is pure overhead; but finer categories force closer looking, plausibly improving boundary care and reducing category confusion even after merging.
- **Core Hypothesis (falsifiable):** Labels collected at fine granularity and merged to coarse outperform directly coarse labels on boundary precision and rare-structure recall at the same coarse ontology, with the quality gain exceeding the measured cost increase for boundary-critical applications.
- **Why Important:** A counterintuitive protocol lever: paying for apparently unnecessary distinctions may be the cheapest route to quality where it matters.
- **Why Possibly Novel:** The attention-mechanism hypothesis for ontology granularity has not been experimentally tested in annotation practice.
- **Minimal Experiment:** Randomize granularity conditions on matched image sets; merge and score against gold; account costs; test on a boundary-critical downstream task.
- **Main Risk:** Fine ontologies also increase taxonomy errors and time; net effect may be domain-dependent.
- **Research Cluster:** ANNOT-EFF / ASSUMPTION

### IDEA-B-0171 — Estimate the information ceiling of image-level supervision
- **One-sentence idea:** Empirically bound the mutual information between image-level labels and pixel masks to test whether weakly supervised semantic segmentation has hit an information-theoretic ceiling.
- **Problem:** CAM-based weak supervision progress has slowed; whether the plateau reflects method immaturity or exhaustion of the information actually present in image-level labels is a fundamental open question.
- **Core Hypothesis (falsifiable):** A non-parametric estimate of achievable mask accuracy given only image-label information (via retrieval-based ideal-observer construction on large data) sits close to current best weakly supervised results, implying method-side headroom is nearly exhausted.
- **Why Important:** Tells the subfield whether to keep optimizing methods or to change the supervision signal — a resource-allocation answer for a large community.
- **Why Possibly Novel:** Information-ceiling estimation for supervision signals, as opposed to method benchmarking, has not been attempted for weak segmentation.
- **Minimal Experiment:** Construct ideal-observer mask predictors using image labels plus class-agnostic priors at increasing capability; extrapolate the ceiling; position current methods against it.
- **Main Risk:** Any ceiling estimate is only as good as the ideal-observer construction; must present bounds, not point claims.
- **Research Cluster:** ANNOT-EFF / EVAL-WEAK

### IDEA-B-0172 — Guidelines beat examples: instruction design dominates annotation quality
- **One-sentence idea:** Factorially test whether written edge-case guidelines or worked examples contribute more to annotation consistency, and how fast returns diminish in each.
- **Problem:** Annotation onboarding invests in instructions and examples by convention; nobody has decomposed which ingredient buys consistency, though the answer determines how to spend protocol-design effort.
- **Core Hypothesis (falsifiable):** Inter-annotator agreement responds more strongly to edge-case rule count than to example count at matched onboarding time, with example value saturating quickly — and the dominant disagreement categories are predictable from rule-coverage gaps.
- **Why Important:** Protocol design is cheap relative to labeling; knowing its highest-leverage component improves every dataset produced afterward.
- **Why Possibly Novel:** Instruction design is folk knowledge in dataset construction; controlled decomposition experiments are absent from the vision literature.
- **Minimal Experiment:** Randomize onboarding conditions across annotator groups on ambiguous imagery; measure agreement and error taxonomies against rule coverage.
- **Main Risk:** Effects may depend on task ambiguity level, requiring at least two task difficulty tiers.
- **Research Cluster:** ANNOT-EFF

### IDEA-B-0173 — Past a scale, re-annotation beats new annotation
- **One-sentence idea:** Locate the dataset-growth crossover where a marginal annotation dollar buys more model improvement through label refinement of existing images than through new images.
- **Problem:** Dataset budgets default to growth (more images), but as scale increases, marginal new images duplicate existing modes while label errors persist as a fixed quality tax — implying a crossover the field has never located.
- **Core Hypothesis (falsifiable):** Model improvement per unit budget from cleaning worst-label images (identified by disagreement mining) exceeds that from adding new images once training sets pass a measurable redundancy threshold, with the crossover predictable from dataset coverage statistics.
- **Why Important:** Reframes dataset strategy for the mature-dataset era and operationalizes "data-centric AI" with a concrete decision rule.
- **Why Possibly Novel:** Cleaning and growth are studied separately; the budget-matched crossover analysis with a predictive threshold is new.
- **Minimal Experiment:** At several training-set scales, spend matched budgets on refinement vs. growth; measure model deltas; fit the crossover against redundancy statistics.
- **Main Risk:** Refinement value depends on initial label quality, so results must be reported as a function of measured error rates.
- **Research Cluster:** ANNOT-EFF

### IDEA-B-0174 — Ontology bridging recovers most of the value of new annotation
- **One-sentence idea:** Measure how much downstream performance is recoverable by systematically mapping and merging label spaces of existing public datasets instead of annotating new data.
- **Problem:** Teams re-annotate because label spaces mismatch, treating taxonomy alignment as too messy; the actual recoverable value of principled ontology bridging (including partial and conditional mappings) has never been quantified against the cost of equivalent new annotation.
- **Core Hypothesis (falsifiable):** For common target ontologies, training on bridge-mapped unions of public datasets achieves within a small margin of what an equivalently sized newly annotated dataset provides, at near-zero annotation cost — with failures concentrated in classes whose definitions genuinely conflict (detectable in advance via cross-dataset annotation comparison).
- **Why Important:** If bridging recovers most value, the community's marginal annotation spending is largely redundant — an enormous efficiency claim worth testing carefully.
- **Why Possibly Novel:** Multi-dataset training exists; the controlled bridging-vs-new-annotation value comparison with conflict prediction is not established.
- **Minimal Experiment:** Build bridges among 4–5 public segmentation datasets; train on unions vs. matched new-annotation baselines (simulated by held-out data); quantify recovery rates and conflict-class failures.
- **Main Risk:** Definitional conflicts (what counts as "road") may be more pervasive than mapping optimists assume, capping recovery.
- **Research Cluster:** ANNOT-EFF / CROSS-DOMAIN

### IDEA-B-0175 — Review the confident errors, not the uncertain regions
- **One-sentence idea:** Test whether annotation-review budgets find more true label errors by targeting model-confident disagreements with GT than by targeting model-uncertain regions.
- **Problem:** Uncertainty-guided review is the default triage heuristic, but model-uncertain regions are often legitimately hard (correctly labeled, genuinely ambiguous), while label errors in easy regions hide behind confident model-GT disagreement — the standard heuristic may search where errors aren't.
- **Core Hypothesis (falsifiable):** Per reviewed region, confident-disagreement targeting yields a several-fold higher verified-label-error discovery rate than uncertainty targeting, across datasets and model families.
- **Why Important:** A drop-in improvement to every label-cleaning pipeline, plus evidence about the distinct geographies of ambiguity and error (complements IDEA-B-0094).
- **Why Possibly Novel:** Confident-learning ideas exist for classification labels; the region-level comparison against the entrenched uncertainty heuristic in segmentation review is new.
- **Minimal Experiment:** Rank regions by both criteria on benchmarks; human-verify equal-sized samples from each ranking; compare error yields and error-type profiles.
- **Main Risk:** Discovery-rate advantages may shrink after the first cleaning iteration as easy errors are exhausted.
- **Research Cluster:** ANNOT-EFF / UNCERTAINTY

### IDEA-B-0176 — One-bit human verification as the scalable supervision signal
- **One-sentence idea:** Test whether large volumes of accept/reject judgments on machine-proposed masks train quality-reward models that improve segmenters more per annotation dollar than conventional labels.
- **Problem:** Human verification (yes/no on a proposal) is many times faster than mask creation, but the field has no measurement of how much model improvement per unit cost this weaker-but-cheaper signal buys when used to train reward/quality models for filtering or fine-tuning.
- **Core Hypothesis (falsifiable):** At matched annotation cost, a pipeline of proposal generation + one-bit verification + reward-model-filtered self-training outperforms direct mask annotation for improving a base segmenter, once the base model passes a quality threshold.
- **Why Important:** If verification dominates creation economically, dataset production should restructure around it — the same asymmetry that reshaped language-model training.
- **Why Possibly Novel:** RLHF-style pipelines are standard in NLP; a cost-grounded comparison against conventional annotation for dense vision supervision is missing.
- **Minimal Experiment:** Run both pipelines at matched measured cost on the same base model and image pool; compare downstream metrics across domains and base-model strengths.
- **Main Risk:** Verification-trained reward models may inherit proposal-distribution blind spots (interacts with IDEA-B-0158).
- **Research Cluster:** ANNOT-EFF

### IDEA-B-0177 — Tool vertex budgets, not annotator care, bound polygon dataset quality
- **One-sentence idea:** Audit annotation-tool configurations (default vertex counts, simplification tolerances) across public datasets and measure how much of inter-dataset GT quality difference they explain.
- **Problem:** Datasets are compared as if their quality reflects annotator effort and QA, but tool-level geometry settings (auto-simplification, vertex limits) may mechanically cap boundary fidelity regardless of care.
- **Core Hypothesis (falsifiable):** Reconstructed tool parameters (inferred from vertex-density and curvature statistics of published GT) explain a large share of cross-dataset boundary-precision variance, exceeding the share explained by documented QA differences.
- **Why Important:** Attributes dataset quality differences to reproducible engineering settings, enabling cheap quality upgrades (change the tolerance) and fairer cross-dataset comparisons.
- **Why Possibly Novel:** GT quality audits look at annotator behavior; the tool-parameter forensic approach is unexplored.
- **Minimal Experiment:** Fit per-dataset vertex/curvature signatures; where possible confirm against known tool configurations; regress boundary-precision estimates on inferred parameters.
- **Main Risk:** Tool parameters and workforce quality are historically correlated, complicating causal separation.
- **Research Cluster:** ANNOT-EFF / EVAL-WEAK

### IDEA-B-0178 — Annotator disagreement is free auxiliary supervision
- **One-sentence idea:** Test whether predicting annotator-disagreement maps as an auxiliary task (using disagreement already present in multi-pass datasets) improves segmentation generalization at zero extra annotation cost.
- **Problem:** Multi-pass and QA-ed datasets contain disagreement information that is discarded after consensus; if disagreement encodes ambiguity structure useful for representation learning, throwing it away wastes collected signal.
- **Core Hypothesis (falsifiable):** Adding disagreement-map prediction as an auxiliary objective improves out-of-distribution segmentation and calibration relative to matched consensus-only training, with gains proportional to the informativeness of the disagreement (not its volume).
- **Why Important:** Converts a discarded byproduct of existing pipelines into a free performance and robustness resource.
- **Why Possibly Novel:** Multi-rater learning focuses on consensus quality; disagreement-as-auxiliary-target for generalization (not calibration alone) is untested.
- **Minimal Experiment:** On datasets with recoverable multi-pass data, train with/without the auxiliary head; evaluate ID/OOD accuracy and calibration; ablate disagreement informativeness.
- **Main Risk:** Disagreement may be dominated by sloppiness rather than ambiguity in some datasets, diluting the signal.
- **Research Cluster:** ANNOT-EFF / GENERALIZATION

### IDEA-B-0179 — Simulate annotation protocols with VLM annotators before spending money
- **One-sentence idea:** Validate whether VLM-simulated annotators reproduce human error patterns well enough to pre-optimize annotation protocols (instructions, ontologies, interfaces) in silico.
- **Problem:** Protocol design (see IDEA-B-0172) is currently tested on expensive human pilots; if simulated annotators rank protocol variants the same way humans do, protocol search becomes cheap and thorough.
- **Core Hypothesis (falsifiable):** Across a suite of protocol variants, VLM-simulated annotation quality rankings correlate strongly with human-pilot rankings — even if absolute error rates differ — making simulation a valid screening instrument.
- **Why Important:** A validated simulator changes the economics of dataset design, allowing hundreds of protocol variants to be screened before human deployment.
- **Why Possibly Novel:** LLM-simulated users exist in HCI research; validated annotation-protocol screening for vision labeling is new territory.
- **Minimal Experiment:** Define 10+ protocol variants; run VLM simulations and matched human pilots; compare ranking concordance and failure-mode overlap.
- **Main Risk:** VLM errors may be systematically unlike human errors (different ambiguity responses), capping validity to certain protocol dimensions.
- **Research Cluster:** ANNOT-EFF / MULTIMODAL-SUP

### IDEA-B-0180 — Interface latency causally degrades label geometry
- **One-sentence idea:** Measure the causal effect of annotation-tool latency (cursor lag, render delay) on boundary tracing accuracy, establishing infrastructure quality as a dataset-quality variable.
- **Problem:** Annotation platforms differ in responsiveness; motor control research predicts lag degrades tracing precision, implying datasets encode their platforms' performance characteristics — an unexamined quality factor.
- **Core Hypothesis (falsifiable):** Experimentally injected latency degrades boundary accuracy monotonically with a measurable dose-response curve, and the effect size at realistic platform latencies rivals differences attributed to annotator skill tiers.
- **Why Important:** If infrastructure explains a meaningful quality share, cheap engineering fixes (local rendering) beat expensive workforce upgrades.
- **Why Possibly Novel:** Latency effects are studied in HCI pointing tasks; the transfer to annotation geometry and dataset-level consequences is unmeasured.
- **Minimal Experiment:** Within-subject latency-injection study on tracing tasks with gold-standard geometry; dose-response fitting; comparison against skill-tier variance.
- **Main Risk:** Annotators may adapt strategies (more clicks, more zoom) that mask latency effects on final quality while raising time cost.
- **Research Cluster:** ANNOT-EFF / PHENOMENON

### IDEA-B-0181 — Quantify the annotation budget wasted on near-duplicates
- **One-sentence idea:** Audit popular datasets and typical collection pipelines for near-duplicate redundancy and measure how much annotation spending deduplication-before-annotation would have saved at equal model quality.
- **Problem:** Deduplication is applied (if at all) after annotation; collection pipelines (video sampling, burst photos, web scraping) produce redundancy that is then expensively labeled, but the waste has never been priced.
- **Core Hypothesis (falsifiable):** For several public datasets, removing near-duplicate clusters before (simulated) annotation would reduce labeling cost substantially at negligible downstream model cost — with savings predictable from the collection method.
- **Why Important:** A concrete, transferable cost-reduction number motivates a trivial pipeline change across the industry.
- **Why Possibly Novel:** Dedup research targets test-set contamination and training efficiency; the annotation-budget framing with collection-method attribution is new.
- **Minimal Experiment:** Cluster near-duplicates in 4 datasets; train on dedup-then-label simulations vs. full sets at matched label budgets; report quality-vs-savings curves.
- **Main Risk:** Aggressive dedup thresholds may remove genuinely informative hard variations (lighting/pose near-duplicates).
- **Research Cluster:** ANNOT-EFF

### IDEA-B-0182 — A sample-complexity law for sparse pixel supervision
- **One-sentence idea:** Establish how segmentation accuracy scales with the number of labeled pixels per image and test whether the curve is predicted by image spatial-autocorrelation statistics.
- **Problem:** Point-supervision papers pick label densities arbitrarily; a validated scaling law would specify the minimum labels needed for a target accuracy and reveal what dense supervision adds beyond its first few bits per region.
- **Core Hypothesis (falsifiable):** Accuracy vs. labeled-pixels-per-image follows a saturating curve whose knee position is predicted across datasets by a measurable label-field autocorrelation length, with dense supervision exceeding the sparse asymptote only on boundary metrics.
- **Why Important:** Converts sparse-supervision design from trial-and-error to prediction and quantifies the true information content of dense masks.
- **Why Possibly Novel:** Individual sparse-supervision results exist; the cross-dataset scaling law with an autocorrelation-based predictor does not.
- **Minimal Experiment:** Train across a label-density grid on datasets with varied spatial statistics; fit curves; validate knee predictions on held-out datasets.
- **Main Risk:** Loss design for sparse labels (how unlabeled pixels are treated) may shift curves more than the data statistics do.
- **Research Cluster:** ANNOT-EFF / PHENOMENON

### IDEA-B-0183 — Buy calibration with ambiguity annotations, not more masks
- **One-sentence idea:** Test whether spending a small annotation budget on explicitly marked ambiguous regions improves model calibration more than spending the same budget on additional standard masks.
- **Problem:** Calibration is trained for indirectly; if humans cheaply marking "this region is genuinely unclear" provides targeted supervision for the confidence channel, a small dedicated budget may beat generic data addition for reliability goals.
- **Core Hypothesis (falsifiable):** Models trained with an ambiguity-supervised confidence objective on a small marked set achieve better calibration and selective-prediction metrics than budget-matched additions of standard labels, without accuracy loss.
- **Why Important:** Creates a direct annotation product for reliability — currently not a thing anyone collects — with immediate deployment relevance.
- **Why Possibly Novel:** Uncertainty supervision from explicit human ambiguity marks (rather than disagreement byproducts) is essentially unexplored in segmentation.
- **Minimal Experiment:** Collect ambiguity marks on a benchmark subset; train confidence-supervised vs. budget-matched control models; compare reliability metrics.
- **Main Risk:** Humans may mark ambiguity inconsistently, making the new signal noisier than hoped (measurable within the study).
- **Research Cluster:** ANNOT-EFF / CALIBRATION

### IDEA-B-0184 — Test-set label fragility: relabeling reorders leaderboards
- **One-sentence idea:** Re-annotate benchmark test subsets under matched protocols and measure how much model rankings change purely from GT replacement.
- **Problem:** Leaderboard differences between top methods are small; if independent relabeling of the same test images produces ranking changes of similar magnitude, current leaderboards partly measure agreement with one particular annotation pass rather than model quality.
- **Core Hypothesis (falsifiable):** On mature benchmarks, ranking correlation between original-GT and relabeled-GT evaluations of public models is imperfect enough that a meaningful fraction of adjacent leaderboard pairs reverse, with reversals concentrated among methods within the GT-noise band.
- **Why Important:** Quantifies the resolution limit of benchmarks — the precision below which leaderboard positions are meaningless — a number every reader needs and none has.
- **Why Possibly Novel:** Label-error studies exist (test-set cleaning); the ranking-stability-under-relabeling framing with a published resolution limit is new for segmentation.
- **Minimal Experiment:** Professionally relabel ~1,000 test images of one benchmark; evaluate 20+ public models against both GTs; report ranking-stability statistics and the implied resolution limit.
- **Main Risk:** The relabeling protocol must match the original's definitions closely enough that changes reflect noise, not ontology drift.
- **Research Cluster:** ANNOT-EFF / EVAL-WEAK

### IDEA-B-0185 — Modal/amodal confusion silently contaminates ground truth
- **One-sentence idea:** Audit how inconsistently annotators handle occlusion (labeling visible extent vs. inferred full extent) within single datasets, and measure the training/evaluation damage from this instruction-level ambiguity.
- **Problem:** Most protocols nominally request visible (modal) extent, but humans naturally complete shapes; if a fraction of GT instances are silently amodal, models receive mixed supervision about the meaning of a mask — an ontological inconsistency, not mere noise.
- **Core Hypothesis (falsifiable):** Systematic audits of occluded instances in popular datasets reveal a substantial fraction with amodal contamination, the rate varies by class and occlusion type, and models trained on the mixed signal predict inconsistent occlusion behavior reproducing the contamination statistics.
- **Why Important:** Modal/amodal consistency underlies every use of masks for measurement and interaction; contamination bounds achievable consistency for all models trained on these datasets.
- **Why Possibly Novel:** Amodal segmentation is a task; the contamination audit of standard modal datasets and its behavioral transmission to models is unstudied.
- **Minimal Experiment:** Expert-audit occluded instances across 3 datasets against depth/multi-view evidence where available; correlate model occlusion behavior with per-dataset contamination profiles.
- **Main Risk:** Determining the "true" visible extent under complex occlusion is itself hard, requiring auxiliary evidence for a solid audit.
- **Research Cluster:** ANNOT-EFF / EVAL-WEAK

### IDEA-B-0186 — Corruption robustness benchmarks only measure the encoder
- **One-sentence idea:** Decompose segmentation robustness by processing stage (encoder vs. decoder vs. head) via cross-stage feature-injection experiments to test whether standard corruption benchmarks characterize only early-stage sensitivity.
- **Problem:** Robustness is reported per model, but corruptions attack low-level statistics that encoders absorb; whether decoders contribute robustness variance — and thus whether decoder design matters for robustness at all — is unknown.
- **Core Hypothesis (falsifiable):** Injecting clean-image encoder features into models fed corrupted inputs recovers almost all performance loss, attributing corruption sensitivity nearly entirely to encoder stages; decoder-swap experiments show negligible robustness variance across decoder designs.
- **Why Important:** Would focus robustness engineering exclusively on early processing (or refute that focus), preventing wasted decoder-side robustness work.
- **Why Possibly Novel:** Stage-wise robustness attribution via activation transplantation has not been done systematically for dense prediction.
- **Minimal Experiment:** Build transplantation harnesses for 3 architectures; measure stage-wise recovery on corruption suites; run decoder-swap robustness comparisons.
- **Main Risk:** Feature transplantation across stages requires distributional compatibility; mismatch artifacts could inflate encoder attribution.
- **Research Cluster:** ROBUSTNESS / GENERALIZATION

### IDEA-B-0187 — Robustness training trades away boundary quality
- **One-sentence idea:** Test whether standard robustness interventions (strong augmentation, corruption training) systematically degrade clean boundary precision while improving interior-region robustness.
- **Problem:** Robustness gains are reported as aggregate mIoU under corruption; if the mechanism is increased spatial smoothing (integration over larger neighborhoods), boundary detail should pay the price — a hidden tradeoff relevant to boundary-critical uses.
- **Core Hypothesis (falsifiable):** Across intervention families, corruption robustness gains correlate with clean boundary-F losses at matched clean mIoU, and the tradeoff curve's slope differs by intervention type — identifying which robustness techniques are boundary-cheapest.
- **Why Important:** Reveals a systematic cost of robustness recipes invisible in standard reporting, and ranks interventions for boundary-sensitive deployments.
- **Why Possibly Novel:** Accuracy-robustness tradeoffs are studied; the boundary-interior decomposition of the cost is not.
- **Minimal Experiment:** Train an intervention grid; report clean/corrupted metrics decomposed into boundary and interior bands; fit tradeoff curves per intervention family.
- **Main Risk:** The correlation may reflect confounded training-strength choices rather than an inherent tradeoff; dose-response designs needed.
- **Research Cluster:** ROBUSTNESS / BOUNDARY

### IDEA-B-0188 — Texture-bias conclusions from classification don't transfer to segmentation
- **One-sentence idea:** Re-run the cue-conflict methodology (texture vs. shape) on segmentation-trained models to test whether the celebrated "CNNs are texture-biased" narrative applies to dense prediction at all.
- **Problem:** The texture-bias literature is built on classification probes, yet its conclusions inform robustness thinking everywhere; segmentation training forces spatial delineation that plausibly induces shape sensitivity, making the imported narrative potentially wrong for dense models.
- **Core Hypothesis (falsifiable):** Segmentation-trained backbones show substantially higher shape reliance than classification-trained ones on matched cue-conflict probes, and their corruption-robustness profile correspondingly deviates from texture-bias predictions.
- **Why Important:** Corrects a foundational belief where it doesn't apply, and repositions "task shapes bias" as the operative principle over "architecture shapes bias."
- **Why Possibly Novel:** Cue-conflict probes have rarely been adapted to dense-prediction models with task-controlled comparisons.
- **Minimal Experiment:** Construct segmentation cue-conflict stimuli (texture-swapped regions); compare bias indices across task-matched backbones; correlate with corruption profiles.
- **Main Risk:** Designing cue-conflict stimuli for dense outputs involves choices that could bias the measured index.
- **Research Cluster:** ROBUSTNESS / ASSUMPTION

### IDEA-B-0189 — Resolution generalization has a predictable aliasing signature
- **One-sentence idea:** Characterize how segmentation fails on resolutions outside the training range and test whether the failure pattern is predicted by sampling theory (aliasing of architecture-specific frequency responses).
- **Problem:** Deployment resolution rarely matches training resolution; failures are treated as generic domain shift, but if they follow computable signal-processing structure, they are predictable and correctable without retraining.
- **Core Hypothesis (falsifiable):** Per-class degradation under resolution shift is predicted by the interaction between class-characteristic spatial frequencies and the model's measured frequency response (IDEA-B-0065's descriptor), and pre-filtering inputs according to the prediction recovers a large fraction of the loss.
- **Why Important:** Replaces "retrain per resolution" with cheap principled correction and unifies resolution robustness under measurable theory.
- **Why Possibly Novel:** Resolution sensitivity is well-known; the predictive frequency-theoretic account with validated correction is not established.
- **Minimal Experiment:** Measure model frequency responses; predict and verify per-class degradation across resolution sweeps; test the pre-filtering correction.
- **Main Risk:** Nonlinear network behavior may deviate from linear-systems predictions enough to break the correction.
- **Research Cluster:** ROBUSTNESS / GENERALIZATION / PHENOMENON

### IDEA-B-0190 — Synthetic weather robustness doesn't transfer to real weather
- **One-sentence idea:** Quantify the gap between robustness to simulated weather (fog/rain filters) and robustness to genuine adverse-weather captures, decomposing the difference into physics and style components.
- **Problem:** Weather robustness is standardly claimed via synthetic corruption training/evaluation; real weather changes scene physics (wet surfaces, light scattering geometry, sensor responses) in ways filters don't model, so claims may not survive contact with reality.
- **Core Hypothesis (falsifiable):** Models hardened on synthetic weather retain only a small fraction of their robustness gain on paired real-weather data, and the unexplained gap is dominated by physical effects absent from simulation (identified via targeted ablations like wet-road reflections).
- **Why Important:** Deployment safety cases cite synthetic-weather results; measuring their external validity is prerequisite to trusting them.
- **Why Possibly Novel:** Real-vs-synthetic corruption validity has been probed for blur/noise; the decomposed weather study on paired real data is missing.
- **Minimal Experiment:** Use datasets with real adverse-weather captures of overlapping scenes; compare synthetic-hardened models against controls; ablate physical effect categories via targeted synthetic upgrades.
- **Main Risk:** Paired real-weather data with matched content is scarce, constraining decomposition precision.
- **Research Cluster:** ROBUSTNESS / SYNTH-DATA

### IDEA-B-0191 — Adversarial vulnerability is object-size-dependent
- **One-sentence idea:** Measure how the attack budget required to flip predictions scales with object size in dense prediction, testing whether small objects are structurally cheapest to erase.
- **Problem:** Adversarial robustness for segmentation is reported in aggregate; if perturbation cost scales with object evidence (pixel count), small safety-critical objects are the soft underbelly, and aggregate metrics conceal it.
- **Core Hypothesis (falsifiable):** The minimum perturbation norm to delete or relabel an object scales sublinearly but strongly with object size across models, making per-pixel attack cost for small objects several times lower — and size-stratified robustness rankings of defenses differ from aggregate rankings.
- **Why Important:** Threat models for deployed perception should be object-size-aware; defenses should be selected for the regime that matters.
- **Why Possibly Novel:** Segmentation attacks exist; the size-scaling law of vulnerability and its consequence for defense ranking is uncharacterized.
- **Minimal Experiment:** Run per-object minimum-perturbation attacks across size bins on several models/defenses; fit scaling curves; compare defense rankings by size stratum.
- **Main Risk:** Per-object attack optimization is expensive; needs efficient attack formulations to scale the measurement.
- **Research Cluster:** ROBUSTNESS / SMALL-OBJ

### IDEA-B-0192 — Natural domain shift hurts mostly through label-frequency shift
- **One-sentence idea:** Decompose cross-domain segmentation degradation into appearance shift vs. class-frequency (label) shift, testing whether cheap prior correction recovers most of the loss.
- **Problem:** Domain adaptation methods target appearance alignment with heavy machinery, but a large share of measured degradation may come from shifted class priors (different amounts of road, vegetation, sky) which a reweighting fixes for free.
- **Core Hypothesis (falsifiable):** On standard cross-domain pairs, post-hoc logit prior correction using target label frequencies (estimated without labels via prediction-marginal matching) recovers a substantial fraction of the domain gap, and the residual — not the headline gap — is the true appearance-shift problem.
- **Why Important:** Re-baselines the domain adaptation field: methods must beat prior correction, not raw source models, to claim appearance-level contributions.
- **Why Possibly Novel:** Label-shift correction is classical in classification; its magnitude accounting within dense-prediction domain gaps is rarely isolated.
- **Minimal Experiment:** Evaluate source models across domain pairs with and without marginal-matching prior correction; tabulate recovered fractions; re-rank published DA methods against the corrected baseline.
- **Main Risk:** Spatially varying priors (scene layout shift) exceed what global reweighting captures, possibly understating the label-shift share.
- **Research Cluster:** GENERALIZATION / CROSS-DOMAIN

### IDEA-B-0193 — Evaluate robustness against the camera, not the corruption library
- **One-sentence idea:** Build robustness evaluation from RAW captures processed through varied ISP configurations, testing whether corruption-suite robustness predicts robustness to real camera-pipeline variation.
- **Problem:** Deployed models face distribution shift primarily via camera/ISP differences (tone mapping, denoising, sharpening), yet robustness research optimizes for a fixed synthetic corruption library whose relevance to ISP variation is unverified.
- **Core Hypothesis (falsifiable):** Model rankings on corruption suites correlate poorly with rankings on ISP-variation suites generated from identical RAW scenes, and ISP-variation robustness is better predicted by sensitivity to specific pipeline stages (sharpening, denoising) than by aggregate corruption scores.
- **Why Important:** Aligns robustness evaluation with the shifts deployments actually encounter, potentially redirecting robustness training targets.
- **Why Possibly Novel:** ISP effects appear in low-level vision; a segmentation robustness benchmark axis built on RAW-reprocessing with ranking-validity analysis is new.
- **Minimal Experiment:** Collect/reuse RAW segmentation-annotated scenes; render through an ISP-parameter grid; evaluate model rankings against corruption-suite rankings.
- **Main Risk:** RAW datasets with segmentation labels are rare; may require annotating a purpose-built set.
- **Research Cluster:** ROBUSTNESS / EVAL-WEAK

### IDEA-B-0194 — Multi-dataset training gains come from taxonomy union, not image diversity
- **One-sentence idea:** Decompose the generalization benefit of multi-dataset training into label-space enrichment vs. image-distribution coverage via label-projection controls.
- **Problem:** Training across datasets improves generalization, credited to visual diversity; but merging also enriches the label space (finer distinctions, complementary ontologies), and the two explanations imply different data strategies.
- **Core Hypothesis (falsifiable):** Training on multi-dataset images with labels projected onto a single dataset's taxonomy captures much less of the generalization gain than full-taxonomy training at matched images — showing taxonomy union, not pixel diversity, carries most of the benefit.
- **Why Important:** If taxonomy is the active ingredient, teams should invest in richer label spaces over more images — a cheap, counterintuitive strategy shift.
- **Why Possibly Novel:** Multi-dataset training papers ablate datasets, never the taxonomy-vs-images factorization.
- **Minimal Experiment:** Train the 2x2 (single/multi images x single/union taxonomy) grid; evaluate zero-shot transfer to held-out datasets; attribute gains.
- **Main Risk:** Label projection loses information non-uniformly, requiring careful projection design to keep the comparison fair.
- **Research Cluster:** GENERALIZATION / CROSS-DOMAIN

### IDEA-B-0195 — Domain generalization methods audit in the foundation-model era
- **One-sentence idea:** Test whether classical DG methods (invariance penalties, episodic training, style randomization) retain any benefit over plain fine-tuning when applied atop modern web-pretrained backbones.
- **Problem:** The DG literature largely predates strong pretraining; its methods may address a shortfall that scale already solved, but benchmarks and papers keep citing them as the robustness toolkit.
- **Core Hypothesis (falsifiable):** With modern pretrained initialization and tuned baselines, the median DG method's out-of-domain gain on dense-prediction benchmarks falls within seed noise, and residual gains concentrate in a small identifiable subclass of shifts (e.g., strict style shifts).
- **Why Important:** Prevents continued default adoption of superseded machinery and locates where DG thinking still earns its complexity.
- **Why Possibly Novel:** Strong-baseline DG audits exist for classification; the dense-prediction version against current pretraining is missing.
- **Minimal Experiment:** Re-run 6 representative DG methods on segmentation DG benchmarks over modern backbones with matched tuning; report seed-replicated deltas per shift type.
- **Main Risk:** Choice of "modern backbone" ages quickly; conclusions should be reported as functions of pretraining strength.
- **Research Cluster:** GENERALIZATION / NEG-RESULT

### IDEA-B-0196 — Self-consistency under nuisance transforms predicts OOD accuracy without labels
- **One-sentence idea:** Validate prediction consistency across test-time nuisance transforms as a label-free estimator of out-of-distribution segmentation accuracy for deployment monitoring.
- **Problem:** Deployments cannot measure accuracy on shifted data without labels; if internal consistency (agreement of predictions across flips/crops/photometric jitter) tracks true accuracy tightly, monitoring becomes free.
- **Core Hypothesis (falsifiable):** Consistency scores correlate with true mIoU across shift types and severities with high rank correlation, with characterizable failure regions (consistent-but-wrong regimes) that can be flagged by complementary statistics.
- **Why Important:** Provides deployable accuracy telemetry and tests a conceptual claim — that shift-induced errors are unstable under nuisance perturbation rather than systematic.
- **Why Possibly Novel:** Agreement-based accuracy estimation exists for classification; the dense-prediction version with failure-regime mapping is not established.
- **Minimal Experiment:** Compute consistency-accuracy relationships across corruption ladders and real domain shifts for multiple models; identify and characterize deviation regimes.
- **Main Risk:** Confidently systematic errors (consistent hallucinations) create blind spots that may be common precisely in the worst shifts.
- **Research Cluster:** GENERALIZATION / UNCERTAINTY

### IDEA-B-0197 — Early-training shortcut probes forecast final OOD gaps
- **One-sentence idea:** Test whether the shortcuts a model adopts in its first epochs (detectable via probing) predict its final out-of-distribution generalization, enabling early abort/reconfiguration of training runs.
- **Problem:** OOD failure is diagnosed after full training; if shortcut adoption is determined early and predictive, expensive runs destined for poor generalization could be identified and modified at a fraction of the cost.
- **Core Hypothesis (falsifiable):** Probes measuring reliance on known shortcut features (position, texture statistics, context priors) at 5–10% of training predict final OOD performance across recipes with strong rank correlation, and early interventions triggered by the probes improve final OOD outcomes.
- **Why Important:** Converts generalization from a post-hoc property into a monitorable, steerable training signal — practical and scientifically clarifying about when generalization fate is sealed.
- **Why Possibly Novel:** Shortcut learning and training dynamics are studied separately; the early-forecast-plus-intervention loop for dense prediction is new.
- **Minimal Experiment:** Train a recipe grid with dense early probing; fit forecast models; validate predictive power and closed-loop interventions on held-out recipes.
- **Main Risk:** Probes may capture recipe identity rather than causal shortcut reliance, inflating apparent forecasting skill.
- **Research Cluster:** GENERALIZATION / PHENOMENON

### IDEA-B-0198 — Most "domain shift" error is novel class-context composition
- **One-sentence idea:** Decompose cross-domain segmentation errors into appearance novelty vs. compositional novelty (familiar classes in unfamiliar configurations), using within-dataset compositional splits as controls.
- **Problem:** Domain shift bundles many changes; if the dominant error source is compositional (a couch outdoors, a cow on a beach), then adaptation should target context priors, not feature alignment — a different research program.
- **Core Hypothesis (falsifiable):** Compositional-novelty splits constructed within a single dataset (no appearance shift) reproduce a large fraction of the error observed under real cross-domain evaluation, and cross-domain errors concentrate on instances whose class-context pairs are rare in source data.
- **Why Important:** Correctly apportions the domain-shift problem between appearance and composition, redirecting adaptation research toward the larger component.
- **Why Possibly Novel:** Context bias and domain shift are separate literatures; the quantitative apportionment via matched compositional splits is new.
- **Minimal Experiment:** Build compositional held-out splits from large datasets; compare error structure against real cross-domain pairs; regress per-instance cross-domain error on source-data context rarity.
- **Main Risk:** Compositional and appearance novelty correlate in real domain pairs, requiring careful statistical separation.
- **Research Cluster:** GENERALIZATION / CROSS-DOMAIN

### IDEA-B-0199 — OOD behavior of equal-validation models spans few modes
- **One-sentence idea:** Characterize the diversity of out-of-distribution behaviors among models indistinguishable in-distribution, testing whether underspecification collapses to a small number of discrete behavior modes.
- **Problem:** Underspecification (identical validation scores, divergent OOD behavior) is documented, but if the divergence occupies a low-dimensional space of modes, small probe sets could identify a model's mode cheaply, taming the phenomenon.
- **Core Hypothesis (falsifiable):** Clustering many equal-validation training runs by their OOD error profiles reveals a small number of stable modes (predictable from early-training probes per IDEA-B-0197), rather than a continuum, and mode membership predicts behavior on new shift types.
- **Why Important:** Makes underspecification manageable: certify the mode, not the infinite behavior space — with direct consequences for model auditing practice.
- **Why Possibly Novel:** Underspecification papers document variance; the mode-structure hypothesis and its predictive validation are unexplored.
- **Minimal Experiment:** Train 50+ matched runs; profile each across a shift battery; cluster profiles; test mode-predictiveness on held-out shifts.
- **Main Risk:** Mode structure may be an artifact of the chosen shift battery rather than intrinsic; requires battery-robustness checks.
- **Research Cluster:** GENERALIZATION / PHENOMENON

### IDEA-B-0200 — Loss-landscape flatness does not predict dense-prediction generalization
- **One-sentence idea:** Test whether flatness measures and sharpness-aware training, validated on classification, predict or improve out-of-distribution generalization in segmentation.
- **Problem:** Flatness-generalization claims migrate into dense prediction by citation rather than evidence; dense tasks' loss geometry (structured outputs, heavy decoders) may break the classification-derived relationships.
- **Core Hypothesis (falsifiable):** Across matched segmentation runs, standard flatness measures correlate weakly or inconsistently with OOD performance, and sharpness-aware optimization yields no reliable OOD improvement at matched compute — refuting the imported assumption for this task class.
- **Why Important:** Stops the uncritical import of a popular theory into a domain where it may not hold, and sharpens understanding of when flatness matters.
- **Why Possibly Novel:** Flatness critiques exist within classification; a purpose-built dense-prediction test of the transferred claim is missing.
- **Minimal Experiment:** Train segmentation model grids with varied recipes; measure multiple flatness proxies and OOD suites; run sharpness-aware training comparisons with seeds.
- **Main Risk:** Flatness measurement choices are contested; multiple measures must be reported to preempt "wrong metric" objections.
- **Research Cluster:** GENERALIZATION / NEG-RESULT / ASSUMPTION

### IDEA-B-0201 — "Zero-shot robustness" is mostly pretraining overlap
- **One-sentence idea:** Measure how much of foundation-backbone robustness on shifted benchmarks is explained by near-duplicate or same-domain content in the pretraining corpus.
- **Problem:** Web-pretrained models appear robust to shifts that older models fail, interpreted as emergent generalization; but if the "shifted" domains are simply represented in pretraining data, the robustness is familiarity, with different implications for truly novel deployment shifts.
- **Core Hypothesis (falsifiable):** Robustness gains of web-pretrained segmenters shrink substantially on shift benchmarks after removing (or statistically controlling for) pretraining-corpus proximity, and per-domain robustness is predicted by estimated corpus density around that domain.
- **Why Important:** Determines whether scale bought genuine out-of-support generalization or a bigger support — the central question for trusting foundation models in novel conditions.
- **Why Possibly Novel:** Contamination analysis exists for classification test sets; the robustness-attribution version for dense prediction with corpus-density regression is new.
- **Minimal Experiment:** Estimate corpus proximity for shift benchmarks via retrieval over open pretraining corpora; correlate per-domain robustness with proximity; validate on deliberately out-of-corpus captures.
- **Main Risk:** Proximity estimation over web-scale corpora is approximate; conclusions need robustness to the retrieval method.
- **Research Cluster:** ROBUSTNESS / CROSS-DOMAIN / EVAL-WEAK

### IDEA-B-0202 — BatchNorm's shift fragility is statistics staleness, nothing deeper
- **One-sentence idea:** Test whether the reported robustness disadvantage of batch normalization disappears entirely once normalization statistics are recalibrated on unlabeled target data.
- **Problem:** BN's fragility under shift fuels architecture recommendations (prefer LN/GN), but the failure may be entirely the stale running statistics — a deployment bookkeeping issue — rather than anything about the learned function.
- **Core Hypothesis (falsifiable):** After statistics recalibration on modest unlabeled target samples, BN models match or exceed LN/GN counterparts across shift benchmarks, eliminating the normalization-choice robustness gap reported under frozen statistics.
- **Why Important:** Prevents architecture decisions from being driven by a fixable artifact and standardizes recalibration as mandatory in robustness comparisons.
- **Why Possibly Novel:** BN adaptation is known as a TTA method; using it to nullify a widely cited architectural claim, with the claim's re-evaluation as the headline, is a different contribution.
- **Minimal Experiment:** Compare matched BN/LN/GN segmenters under shift with frozen vs. recalibrated statistics at several unlabeled-sample budgets.
- **Main Risk:** Recalibration needs target samples, which some deployment models genuinely cannot obtain — scoping the practical claim.
- **Research Cluster:** ROBUSTNESS / ASSUMPTION

### IDEA-B-0203 — Robust backbones are worse transfer learners
- **One-sentence idea:** Test whether corruption- or adversarially-hardened backbones systematically underperform standard ones as initialization for downstream dense-prediction fine-tuning.
- **Problem:** Robust pretraining is marketed as strictly better; but robustness training constrains representations (smoother, less texture-sensitive), which may remove exactly the features downstream tasks need — a transferability cost nobody prices.
- **Core Hypothesis (falsifiable):** Across downstream segmentation/detection tasks, robust-pretrained initializations yield lower fine-tuned accuracy than standard ones at matched pretraining compute, with the deficit scaling with robustness-training strength and concentrating in fine-detail (boundary, small-object) metrics.
- **Why Important:** Establishes the robustness-transferability tradeoff curve needed for rational pretraining choices in model ecosystems where one backbone serves many tasks.
- **Why Possibly Novel:** Scattered observations exist for classification transfer; the dense-prediction transfer cost with metric decomposition is unmeasured.
- **Minimal Experiment:** Fine-tune a matrix of {standard, corruption-robust, adversarially-robust} backbones on 4 downstream dense tasks; report decomposed metrics vs. robustness strength.
- **Main Risk:** Robust checkpoints differ from standard ones in more than robustness (recipes, data), requiring controlled re-pretraining for clean attribution.
- **Research Cluster:** ROBUSTNESS / CROSS-DOMAIN

### IDEA-B-0204 — Honest single-image evaluation of test-time adaptation
- **One-sentence idea:** Re-evaluate TTA methods under strict single-image, no-state protocols to measure how much of their reported gains come from transductive batch-statistics leakage.
- **Problem:** TTA benchmarks feed methods batches of same-shift test images, letting them estimate the shift distribution — information a deployed model processing one image at a time does not have; reported gains may be largely this leak.
- **Core Hypothesis (falsifiable):** Under single-image stateless evaluation, the median published TTA method loses most of its benchmark gain, and the survivors share identifiable single-image mechanisms (input-level normalization) rather than statistics estimation.
- **Why Important:** Aligns TTA evaluation with actual deployment constraints and re-ranks the method space accordingly.
- **Why Possibly Novel:** Episodic-vs-online TTA distinctions exist; the systematic leakage accounting across the method literature for dense prediction is missing.
- **Minimal Experiment:** Re-run 8 public TTA methods under batch, online, and single-image protocols on segmentation shift benchmarks; attribute gains to protocol information.
- **Main Risk:** Some deployments do process batches; conclusions must be presented per deployment pattern rather than as blanket debunking.
- **Research Cluster:** ROBUSTNESS / EVAL-WEAK

### IDEA-B-0205 — Video instability predicts static corruption robustness
- **One-sentence idea:** Test whether a model's temporal prediction instability on clean video forecasts its robustness to static corruptions, unifying two robustness notions under one cheap measurement.
- **Problem:** Robustness evaluation requires corruption suites and labels; if instability under natural frame-to-frame perturbation (free, label-less) captures the same model property, robustness screening becomes trivially cheap and the two phenomena share a mechanism.
- **Core Hypothesis (falsifiable):** Across many models, temporal instability scores on clean unlabeled video rank-correlate strongly with corruption-benchmark robustness, and interventions that improve one reliably improve the other — supporting a common perturbation-sensitivity mechanism.
- **Why Important:** A validated cheap proxy democratizes robustness measurement, and the mechanistic unification would consolidate fragmented robustness research.
- **Why Possibly Novel:** Temporal consistency and corruption robustness are separate literatures; their empirical equivalence hypothesis is untested.
- **Minimal Experiment:** Compute both measures for 20+ public segmenters; test rank correlation; run intervention studies (augmentation, smoothing) checking co-movement.
- **Main Risk:** Motion-specific effects (flicker from genuine appearance change) may contaminate the instability measure, requiring motion-compensated protocols.
- **Research Cluster:** ROBUSTNESS / PHENOMENON

### IDEA-B-0206 — Global attention spreads local corruption: locality as a robustness probe
- **One-sentence idea:** Measure how far spatially localized corruptions propagate through predictions as a function of architecture connectivity, testing whether global attention converts local damage into global damage.
- **Problem:** Architectures differ in how they couple distant locations; a mud splat on the lens should degrade predictions locally, but global context mechanisms may propagate the disturbance — an unmeasured failure-geometry difference with direct deployment meaning.
- **Core Hypothesis (falsifiable):** The spatial decay profile of error induced by localized patches is measurably heavier-tailed for global-attention models than for convolutional ones at matched clean accuracy, and the propagation strength predicts real-world partial-occlusion robustness.
- **Why Important:** Failure locality is a safety property (graceful degradation); characterizing it per architecture family informs perception-stack choices beyond aggregate scores.
- **Why Possibly Novel:** Corruption studies use full-image perturbations; the propagation-geometry analysis of localized damage across architectures is new.
- **Minimal Experiment:** Apply controlled local patches/occlusions; map induced error vs. distance across architectures; validate against camera-soiling datasets.
- **Main Risk:** Matched-accuracy model pairs differ in more than connectivity; multiple family pairs needed for attribution.
- **Research Cluster:** ROBUSTNESS / REP-MISMATCH

### IDEA-B-0207 — Aggregate corruption scores hide oppositely-behaving corruption clusters
- **One-sentence idea:** Show that corruption benchmarks average over corruption families (noise-like vs. blur-like vs. photometric) on which methods rank in opposite orders, making aggregate robustness scores ranking-unstable.
- **Problem:** Mean corruption error compresses structurally different sensitivities into one number; if method rankings invert across corruption clusters, the aggregate drives wrong model choices for any specific deployment threat profile.
- **Core Hypothesis (falsifiable):** Cluster analysis of per-corruption performance across many models reveals stable corruption families with strong ranking inversions between them, and aggregate-score model selection is measurably suboptimal for cluster-specific deployment profiles.
- **Why Important:** Replaces a misleading scalar with a small vector of cluster scores — an easy fix with immediate benchmark-practice impact.
- **Why Possibly Novel:** Per-corruption breakdowns are published but the ranking-inversion structure and its selection-cost consequence have not been the focus.
- **Minimal Experiment:** Evaluate 30+ public models per corruption; cluster corruption response profiles; quantify inversion rates and selection regret under cluster-weighted objectives.
- **Main Risk:** Cluster structure may be dataset-dependent, requiring multi-dataset confirmation.
- **Research Cluster:** ROBUSTNESS / EVAL-WEAK

### IDEA-B-0208 — Cross-city generalization results are confounded by sensors
- **One-sentence idea:** Disentangle geography effects from camera/ISP effects in cross-city driving benchmarks using same-city-different-sensor and same-sensor-different-city controls.
- **Problem:** Cross-city evaluation is the standard probe of geographic generalization, but cities in different datasets are captured with different vehicles, cameras, and pipelines; the measured "geography gap" may be mostly hardware.
- **Core Hypothesis (falsifiable):** Same-sensor cross-city gaps are several times smaller than cross-dataset cross-city gaps, attributing the majority of conventional measurements to sensor/pipeline factors rather than scene content.
- **Why Important:** Correct attribution changes what adaptation research targets (ISP harmonization vs. content adaptation) and reinterprets a decade of cross-dataset results.
- **Why Possibly Novel:** The confound is acknowledged informally; controlled decomposition using sensor-overlapping collections has not been published.
- **Minimal Experiment:** Assemble evaluation cells crossing {sensor, city} from datasets with overlapping hardware or multi-city single-platform captures; decompose gap variance.
- **Main Risk:** Suitable sensor-controlled data is scarce; may require a small purpose-built capture effort.
- **Research Cluster:** GENERALIZATION / CROSS-DOMAIN / EVAL-WEAK

### IDEA-B-0209 — Night robustness is an exposure-pipeline problem, not a darkness problem
- **One-sentence idea:** Decompose night-time segmentation failure into photon-limited information loss vs. ISP/exposure processing artifacts, testing whether RAW-space processing removes most of the "night gap."
- **Problem:** Night performance is treated as a semantic domain gap requiring adaptation methods; but consumer ISPs make aggressive low-light choices (denoising, tone mapping) that may destroy recoverable signal before the model sees it.
- **Core Hypothesis (falsifiable):** Models operating on appropriately processed RAW night captures close a large fraction of the day-night gap without any domain adaptation, bounding the truly semantic component of night difficulty to a minority share.
- **Why Important:** Redirects night-robustness work from learned adaptation toward capture-pipeline engineering where the larger recoverable share lives.
- **Why Possibly Novel:** Low-light enhancement exists as preprocessing; the decomposition claim with RAW-based bounding of the semantic gap is not established for segmentation.
- **Minimal Experiment:** Use paired RAW/processed night datasets; train/evaluate across processing variants; attribute the day-night gap between information and processing components.
- **Main Risk:** RAW night data with segmentation labels is rare; annotation on enhanced renders introduces its own biases.
- **Research Cluster:** ROBUSTNESS / PHENOMENON

### IDEA-B-0210 — Class-camera correlations are an unmeasured spurious channel
- **One-sentence idea:** Audit benchmarks for correlations between class occurrence and capture hardware/settings, and test whether models exploit camera fingerprints as class evidence.
- **Problem:** Datasets aggregate sources whose content differs (one contributor photographs boats, another kitchens); models may partially recognize the camera rather than the scene, inflating in-distribution scores and breaking under hardware change.
- **Core Hypothesis (falsifiable):** Camera-fingerprint features (noise residuals, JPEG signatures) predict class distributions on benchmark images above chance, and models show measurable performance drops when fingerprints are normalized away — with per-class drops matching the audit's correlation strengths.
- **Why Important:** Identifies a shortcut channel orthogonal to visible content, relevant to both benchmark validity and deployment robustness across devices.
- **Why Possibly Novel:** Camera forensics and recognition shortcuts are separate fields; their intersection as a dataset-bias audit for dense prediction is unexplored.
- **Minimal Experiment:** Extract fingerprint features on benchmarks; measure class-fingerprint mutual information; evaluate models on fingerprint-normalized images; correlate drops.
- **Main Risk:** Fingerprint normalization also alters legitimate texture signal, requiring careful controls to separate the channels.
- **Research Cluster:** ROBUSTNESS / EVAL-WEAK

### IDEA-B-0211 — Datasets drift internally: train-on-early, test-on-late
- **One-sentence idea:** Quantify within-dataset temporal drift by splitting benchmarks along their collection timelines and measuring the generalization gap between chronological and random splits.
- **Problem:** Benchmarks are treated as IID samples of a distribution, but collection spans months/years of changing hardware, locations, and annotation practices; random splits hide a drift that deployment (always chronological) will encounter.
- **Core Hypothesis (falsifiable):** Chronological splits show measurably worse test performance than random splits on several benchmarks, with the gap attributable to identifiable drift factors (device turnover, protocol updates) recovered from metadata.
- **Why Important:** Reveals that even "in-distribution" numbers overstate deployment performance, and provides a cheap standard practice (report chronological-split results) to fix it.
- **Why Possibly Novel:** Temporal splits are standard in ML for time series; auditing static vision benchmarks for internal drift is rarely done.
- **Minimal Experiment:** Recover collection ordering for datasets with timestamps; train/evaluate under both split types; decompose the gap using metadata covariates.
- **Main Risk:** Timestamps are unavailable or unreliable for many datasets, limiting the audit's breadth.
- **Research Cluster:** GENERALIZATION / EVAL-WEAK

### IDEA-B-0212 — Fourier sensitivity fingerprints transferably predict corruption vulnerability
- **One-sentence idea:** Validate per-model frequency-sensitivity profiles as transferable predictors of which corruptions will hurt, enabling robustness forecasting without running corruption suites.
- **Problem:** Robustness must currently be measured corruption-by-corruption; if a model's Fourier sensitivity fingerprint (cheaply measured with perturbation probes) predicts its response to arbitrary corruptions via their spectral signatures, robustness evaluation compresses dramatically.
- **Core Hypothesis (falsifiable):** A linear model over fingerprint-corruption spectral overlap predicts per-corruption degradation across held-out models and held-out corruption types with high accuracy, including real-world degradations not in any suite.
- **Why Important:** Converts robustness evaluation from enumeration to prediction and gives a compact, comparable robustness descriptor per model.
- **Why Possibly Novel:** Fourier perspectives on robustness exist; the validated transferable forecasting framework with held-out generalization tests is not established for dense prediction.
- **Minimal Experiment:** Measure fingerprints for 20 models; fit degradation predictors; validate on unseen corruptions and real degradation datasets.
- **Main Risk:** Nonlinear interactions between frequency bands may cap predictive accuracy below usefulness.
- **Research Cluster:** ROBUSTNESS / PHENOMENON

### IDEA-B-0213 — The error-compounding law of pseudo-labeling under shift
- **One-sentence idea:** Measure how teacher errors amplify through student generations in self-training pipelines under domain shift, and identify the shift severity beyond which self-training becomes self-poisoning.
- **Problem:** Self-training on shifted unlabeled data is standard practice; its failure mode (students confidently learning teacher mistakes) is anecdotal, and no quantitative compounding model tells practitioners when the pipeline crosses from helpful to harmful.
- **Core Hypothesis (falsifiable):** Per-class error amplification across self-training rounds follows a measurable multiplicative dynamic driven by initial teacher error and pseudo-label confidence filtering strength, yielding a predictable critical shift severity where iteration harms — validated across domain pairs.
- **Why Important:** Provides operational stopping/tuning rules for a ubiquitous pipeline and a quantitative theory of confirmation bias in dense self-training.
- **Why Possibly Novel:** Confirmation bias in self-training is acknowledged; the quantitative compounding law with critical-point prediction is not established.
- **Minimal Experiment:** Run multi-round self-training across a shift-severity ladder; track per-class error dynamics; fit and validate the compounding model on a second domain pair.
- **Main Risk:** Dynamics may be architecture- and filter-specific, demanding a factorial design to find law-like structure.
- **Research Cluster:** ROBUSTNESS / GENERALIZATION / ANNOT-EFF

### IDEA-B-0214 — Scale collapses error diversity: big models fail together
- **One-sentence idea:** Test whether independently trained large models make increasingly correlated errors (especially OOD), undermining ensemble and redundancy strategies exactly where they are most needed.
- **Problem:** Safety architectures rely on redundancy (ensembles, cross-checking models), assuming independent failures; if scale and shared pretraining homogenize error patterns, redundancy value silently evaporates as the field scales up.
- **Core Hypothesis (falsifiable):** Pairwise error correlation between independently fine-tuned models rises with both model scale and pretraining-corpus overlap, and the marginal ensemble benefit OOD shrinks correspondingly — with pretraining overlap, not scale itself, as the dominant factor.
- **Why Important:** Quantifies a systemic-risk trend in the model ecosystem and identifies diversity-preserving practices (disjoint pretraining) with measured value.
- **Why Possibly Novel:** Error correlation is studied within ensembles; the scale-and-overlap trend analysis with its safety-architecture implications is new.
- **Minimal Experiment:** Build model grids varying scale and pretraining source; measure pairwise error correlations and ensemble gains, ID and OOD; regress on scale and overlap.
- **Main Risk:** Truly disjoint pretraining corpora at scale are hard to arrange, constraining the overlap axis.
- **Research Cluster:** ROBUSTNESS / PHENOMENON

### IDEA-B-0215 — Illumination robustness lives almost entirely in the first layers
- **One-sentence idea:** Localize where in the network illumination invariance is implemented, testing whether early layers alone absorb illuminant variation while later layers are illumination-blind.
- **Problem:** Robustness is treated as a whole-network property; if specific robustness types are implemented at specific depths, targeted interventions (freezing, swapping, augmenting particular stages) become possible and mechanistic understanding improves.
- **Core Hypothesis (falsifiable):** Feature dissimilarity between illumination-varied image pairs collapses within the first few layers for illumination-robust models, layer-swap experiments transfer illumination robustness with early layers alone, and illumination-targeted training of only those layers matches full-network robustness training.
- **Why Important:** Establishes a modularity map of robustness that enables cheap targeted hardening and informs theories of what depth does.
- **Why Possibly Novel:** Layer-wise invariance analyses exist descriptively; the causal swap-and-retrain localization for a specific robustness type in dense prediction is new.
- **Minimal Experiment:** Measure layer-wise invariance profiles under controlled relighting; run early-layer swap and targeted-training experiments across model pairs.
- **Main Risk:** Invariance may be distributed rather than localized in some architectures, making the map family-specific.
- **Research Cluster:** ROBUSTNESS / REP-MISMATCH

### IDEA-B-0216 — Object removal changes predictions far away: non-local fragility audit
- **One-sentence idea:** Measure how much editing one scene element (removing/inserting an object) changes predictions on distant, unedited regions, as a consistency property across architectures.
- **Problem:** Ideally, distant regions' labels shouldn't depend on an unrelated object's presence; context integration makes some dependence rational, but excessive non-local sensitivity signals brittle entanglement — never quantified as a model property.
- **Core Hypothesis (falsifiable):** Non-local sensitivity (prediction change beyond a radius from clean edits) varies by an order of magnitude across equal-accuracy architectures, correlates with context-window design, and predicts robustness to natural scene rearrangement (same place, different day).
- **Why Important:** Defines an auditable stability property relevant to mapping/change-detection deployments and quantifies the context-integration tradeoff (with IDEA-B-0032).
- **Why Possibly Novel:** Contextual-dependence probes exist for classification; a scene-editing-based non-locality audit for dense prediction with deployment validation is new.
- **Minimal Experiment:** Use high-quality inpainting to create edit pairs; map prediction-change fields vs. distance; compare architectures; validate against revisit-imagery robustness.
- **Main Risk:** Inpainting artifacts contribute their own prediction changes; artifact-only controls are essential.
- **Research Cluster:** ROBUSTNESS / GENERALIZATION

### IDEA-B-0217 — Geographic transfer includes annotation-culture shift, not just scene shift
- **One-sentence idea:** Quantify how much cross-country dataset transfer gaps reflect differing annotation conventions (what counts as "road," "building," "vegetation") rather than visual differences.
- **Problem:** Cross-geography gaps are read as visual domain shift, but ontology interpretation is culturally and organizationally local; a model may segment the scene correctly by the source convention and be scored wrong by the target's — mislabeled as a robustness failure.
- **Core Hypothesis (falsifiable):** Having annotators from each dataset's convention relabel the same images reveals systematic convention differences, and re-scoring cross-dataset transfer under convention-harmonized GT removes a substantial fraction of the measured gap.
- **Why Important:** Corrects the attribution of a widely measured phenomenon and quantifies the "ontology shift" component that adaptation methods cannot and should not fix.
- **Why Possibly Novel:** Ontology mismatch is acknowledged qualitatively; the convention-controlled re-annotation experiment isolating its share of transfer gaps has not been done.
- **Minimal Experiment:** Cross-annotate image samples under both datasets' guidelines; measure convention deltas; re-evaluate transfer with harmonized GT.
- **Main Risk:** Recruiting annotators faithful to each original convention is operationally delicate.
- **Research Cluster:** CROSS-DOMAIN / ANNOT-EFF / EVAL-WEAK

### IDEA-B-0218 — Robustness gains are corruption-library overfitting
- **One-sentence idea:** Test whether augmentation-based robustness methods generalize to corruption types held out from their design/tuning loop, auditing the field for benchmark overfitting.
- **Problem:** Robustness methods are developed and tuned against the same public corruption suites they report on; apparent progress may be library-specific, evaporating on held-out degradation families.
- **Core Hypothesis (falsifiable):** Across published augmentation strategies, robustness gains on the standard suite substantially exceed gains on disjoint corruption families (constructed from real degradations and novel synthetic ones), with the generalization ratio varying widely across methods — identifying which techniques learned "robustness" versus "the library."
- **Why Important:** Distinguishes real robustness progress from benchmark memorization at the level of the field, and establishes held-out-corruption evaluation as standard.
- **Why Possibly Novel:** The train/test-corruption disjointness principle is stated occasionally; a systematic method-space audit with a generalization-ratio metric is not published.
- **Minimal Experiment:** Re-train representative augmentation methods; evaluate on standard vs. curated held-out corruption sets; rank by generalization ratio.
- **Main Risk:** Constructing genuinely disjoint yet realistic held-out corruptions requires care; overlap disputes are foreseeable.
- **Research Cluster:** ROBUSTNESS / EVAL-WEAK / NEG-RESULT

### IDEA-B-0219 — Output-distribution drift beats input monitors for shift detection
- **One-sentence idea:** Compare shift-detection latency and sensitivity of monitoring prediction statistics (class histograms, confidence profiles) against monitoring input statistics, for deployed segmentation systems.
- **Problem:** Deployment monitoring convention watches input distributions (pixel statistics, embeddings), but the model's own outputs integrate exactly the features it cares about; which monitor detects consequential shift earlier is an unanswered practical question.
- **Core Hypothesis (falsifiable):** Prediction-statistic monitors detect performance-relevant shifts at lower severity and with fewer false alarms than input-statistic monitors across shift types, except for shifts the model is invariant to (correctly ignored) — making output monitoring the better default.
- **Why Important:** Directly upgrades deployment practice with a cheap change, and clarifies the principle that shift matters only as the model experiences it.
- **Why Possibly Novel:** Drift detection literatures exist in ML ops; the controlled head-to-head with performance-relevance grounding for dense prediction is missing.
- **Minimal Experiment:** Simulate deployment streams with controlled shift onsets; run both monitor families; compare detection ROC and lead time against true performance degradation.
- **Main Risk:** Output monitors are blind to shifts that change errors without changing output statistics (systematic swaps), needing characterization.
- **Research Cluster:** ROBUSTNESS / UNCERTAINTY

### IDEA-B-0220 — At fixed compute, more data beats robustness methods
- **One-sentence idea:** Test whether spending a fixed training-compute budget on additional diverse data outperforms spending it on robustness-specific training techniques, across shift benchmarks.
- **Problem:** Robustness methods (adversarial training, elaborate augmentation pipelines) cost compute; the opportunity-cost comparison against simply training longer on more diverse data is almost never run, though it is the decision practitioners actually face.
- **Core Hypothesis (falsifiable):** At matched total compute, data scaling matches or exceeds the median robustness method's OOD gains on natural-shift benchmarks, with robustness methods retaining advantages only on the specific perturbation families they encode (e.g., adversarial norms).
- **Why Important:** Reframes robustness research economics: methods must beat the data-scaling baseline at matched cost to claim practical value.
- **Why Possibly Novel:** Compute-matched baselines are becoming standard in scaling literature; applying the discipline to the robustness method space for dense prediction is new.
- **Minimal Experiment:** Fix compute budgets; train {more-data, longer-training, robustness-method} arms from identical starting points; evaluate across natural and synthetic shift suites.
- **Main Risk:** "More diverse data" availability is domain-dependent, so conclusions must be conditioned on data-acquisition cost assumptions.
- **Research Cluster:** ROBUSTNESS / ASSUMPTION

### IDEA-B-0221 — A mixing law for synthetic training data
- **One-sentence idea:** Establish how downstream performance scales with the synthetic-to-real mixing ratio and test whether the optimal ratio is predicted by the generator's measured fidelity/diversity statistics.
- **Problem:** Teams choose synthetic data fractions by trial and error; a validated law linking generator quality metrics to the optimal mix and the harm threshold would make synthetic data engineering predictable.
- **Core Hypothesis (falsifiable):** Performance vs. mixing ratio follows a consistent unimodal curve whose optimum and zero-crossing shift predictably with generator precision/recall measures, transferring across generator families within error bars.
- **Why Important:** Converts a ubiquitous ad hoc decision into a computable one, and connects generative evaluation metrics to downstream utility — validating or refuting their meaning.
- **Why Possibly Novel:** Individual mixing ablations abound; the cross-generator predictive law is not established for dense prediction.
- **Minimal Experiment:** Sweep mixing ratios across 4 generators of varied measured quality on two tasks; fit and validate the predictive relationship on a held-out generator.
- **Main Risk:** Task- and class-conditional effects (IDEA-B-0247) may defeat any single aggregate law.
- **Research Cluster:** SYNTH-DATA / PHENOMENON

### IDEA-B-0222 — Synthetic data's value is concentrated where real data is thin
- **One-sentence idea:** Test whether synthetic data helps only in undersampled regions of the real data distribution (rare poses, lighting, contexts), making targeted generation strictly better than distribution-matched generation.
- **Problem:** Generation pipelines aim to imitate the real distribution, but duplicated coverage of well-sampled modes may add nothing; if all value lies in the thin regions, generation strategy should invert from imitation to complementarity.
- **Core Hypothesis (falsifiable):** Per-sample synthetic utility (measured by influence-style attribution on downstream performance) is strongly negatively correlated with local real-data density around that sample, and density-targeted generation beats distribution-matched generation at matched volume.
- **Why Important:** Changes the objective for synthetic data pipelines from realism to coverage — a directly actionable strategy with measurable payoff.
- **Why Possibly Novel:** Rare-case generation is practiced ad hoc; the density-utility law and the head-to-head strategy comparison are not established.
- **Minimal Experiment:** Estimate real-data density in embedding space; generate matched vs. thin-region-targeted sets; train and compare; validate the density-utility correlation.
- **Main Risk:** Generators are least reliable exactly in thin regions, coupling coverage targeting with quality degradation.
- **Research Cluster:** SYNTH-DATA

### IDEA-B-0223 — Layout realism beats rendering fidelity in synthetic training data
- **One-sentence idea:** Factorially disentangle photorealism from scene-layout realism in synthetic data to determine which axis drives downstream transfer.
- **Problem:** Synthetic pipelines invest heavily in photorealistic rendering, assuming appearance fidelity drives transfer; but object co-occurrence, scale, and placement statistics may matter more — with big cost implications since layout is cheap and rendering is expensive.
- **Core Hypothesis (falsifiable):** Low-fidelity renders with real-data-matched layout statistics transfer better than photoreal renders with randomized layouts, and the two axes' contributions are additive with layout dominating for context-dependent classes.
- **Why Important:** Redirects synthetic data budgets toward the higher-leverage axis and clarifies what "domain gap" means for generated data.
- **Why Possibly Novel:** Fidelity ablations exist within single pipelines; the clean two-axis factorial with class-conditional analysis is missing.
- **Minimal Experiment:** Generate the 2x2 (fidelity x layout realism) synthetic sets in a controllable simulator; train and evaluate transfer per cell and per class type.
- **Main Risk:** Fidelity and layout interact with the specific simulator's asset quality, requiring at least two simulation stacks.
- **Research Cluster:** SYNTH-DATA

### IDEA-B-0224 — The sim-to-real gap is mostly sensor noise, not semantics
- **One-sentence idea:** Test whether injecting real sensor-noise residuals into synthetic images closes most of the sim-to-real transfer gap, attributing the gap to low-level statistics rather than content realism.
- **Problem:** Sim-to-real research targets semantic realism (better assets, materials), but the persistent gap may live in the sensor layer (noise correlations, ISP artifacts, optical imperfections) that renders lack — cheap to add if identified as dominant.
- **Core Hypothesis (falsifiable):** Applying measured real-camera noise/ISP transforms to existing synthetic datasets recovers a majority of the sim-to-real performance gap at zero content change, while equivalent-effort content upgrades recover less.
- **Why Important:** A confirmed sensor-dominance result would refocus an expensive research area onto a solved-in-principle engineering step.
- **Why Possibly Novel:** Sensor modeling appears in isolated pipelines; the head-to-head attribution against content realism at matched effort is not established.
- **Minimal Experiment:** Characterize target-camera noise/ISP from real captures; retrofit synthetic sets; compare transfer against content-upgraded controls.
- **Main Risk:** The gap's composition likely varies by task and domain; claims must be conditioned accordingly.
- **Research Cluster:** SYNTH-DATA / CROSS-DOMAIN

### IDEA-B-0225 — Synthetic test sets preserve model rankings even when absolute scores lie
- **One-sentence idea:** Test whether cheap synthetic evaluation sets rank models the same as expensive real test sets, legitimizing synthetic benchmarking for relative comparisons.
- **Problem:** Building real evaluation sets is often the binding constraint (rare hazards, privacy-restricted domains); if synthetic sets preserve rankings despite score offsets, they suffice for model selection — a claim nobody has validated systematically.
- **Core Hypothesis (falsifiable):** Across model families and domains, rank correlation between synthetic-set and real-set evaluations is high for aggregate metrics but degrades predictably for fine-grained comparisons (nearby models) and specific capability axes (boundary quality), defining a validity envelope for synthetic evaluation.
- **Why Important:** A validated envelope would unlock evaluation in data-poor domains and prevent misuse outside it.
- **Why Possibly Novel:** Synthetic training data is heavily studied; synthetic evaluation validity, as its own question with an envelope characterization, is nearly untouched.
- **Minimal Experiment:** Build paired synthetic/real evaluation sets in three domains; evaluate 15+ models on both; map ranking preservation vs. comparison granularity and metric type.
- **Main Risk:** Generator biases may systematically favor architecturally similar models, corrupting rankings in hard-to-detect ways.
- **Research Cluster:** SYNTH-DATA / EVAL-WEAK

### IDEA-B-0226 — Generative models leak benchmark test sets into synthetic training data
- **One-sentence idea:** Audit whether popular image generators reproduce benchmark test images (or close variants) such that training on generated data constitutes indirect test-set contamination.
- **Problem:** Generators trained on web scrapes have likely seen benchmark test images; teams training on generated data may unknowingly train on morphed test content, inflating scores through a laundering channel no contamination check currently covers.
- **Core Hypothesis (falsifiable):** Retrieval between large samples of generated images and benchmark test sets finds near-matches at rates far above chance, and models trained on contaminated generated subsets show localized performance inflation on the matched test items.
- **Why Important:** Establishes whether "synthetic data" preserves train/test hygiene — foundational for the growing practice of generative augmentation and for interpreting benchmark results in that era.
- **Why Possibly Novel:** Memorization in generators is documented; the downstream benchmark-contamination pathway with inflation measurement is unstudied.
- **Minimal Experiment:** Generate large samples from popular generators with benchmark-adjacent prompts; run near-duplicate retrieval against test sets; train on matched/unmatched splits and compare per-item test performance.
- **Main Risk:** Near-match thresholds are contestable; inflation effects per item are small and need careful statistics.
- **Research Cluster:** SYNTH-DATA / EVAL-WEAK

### IDEA-B-0227 — Exact labels beat pretty pixels: copy-paste vs. diffusion augmentation
- **One-sentence idea:** Test whether geometric composition (copy-paste with exact masks) outperforms diffusion-generated instances for segmentation augmentation because generated data carries label noise that offsets its realism.
- **Problem:** Diffusion augmentation is displacing copy-paste on the assumption that realism wins; but generated instances come with imperfect masks (derived, not exact), and segmentation may care more about label exactness than photometric realism.
- **Core Hypothesis (falsifiable):** At matched augmentation volume, copy-paste yields better mask-quality metrics than diffusion insertion while diffusion wins only on recognition-level metrics, and diffusion's deficit is eliminated when its labels are corrected by oracle masks — proving label noise, not image quality, as the mechanism.
- **Why Important:** Prevents the field from replacing a cheap effective tool with an expensive worse one for the wrong task, and quantifies the label-exactness premium of segmentation.
- **Why Possibly Novel:** Both augmentation families are studied separately; the controlled label-noise attribution between them is new.
- **Minimal Experiment:** Train with copy-paste vs. diffusion-inserted instances (matched counts); decompose metric differences; run the oracle-mask correction arm.
- **Main Risk:** Diffusion insertion quality varies wildly by implementation; needs multiple insertion pipelines for fairness.
- **Research Cluster:** SYNTH-DATA

### IDEA-B-0228 — Pixel-perfect synthetic masks teach overconfident boundaries
- **One-sentence idea:** Test whether training on synthetic data's perfectly crisp mask GT causes boundary overconfidence and miscalibration when transferring to real annotator-noisy evaluation, fixable by boundary-noise injection during synthetic training.
- **Problem:** Synthetic data's exact labels are considered a pure advantage, but real-world boundary GT is noisy; models trained on perfection may allocate confidence in ways mismatched to real evaluation and deployment.
- **Core Hypothesis (falsifiable):** Synthetic-trained models show boundary-zone overconfidence on real data relative to real-trained models at matched accuracy, and injecting annotator-noise-calibrated boundary jitter into synthetic labels improves real-data calibration without hurting accuracy.
- **Why Important:** Identifies a subtle cost of synthetic supervision and a zero-cost fix, refining how synthetic pipelines should prepare labels.
- **Why Possibly Novel:** Synthetic-real gaps are studied for images; the label-statistics gap (too-perfect GT) and its calibration consequence are unexamined.
- **Minimal Experiment:** Train on synthetic with exact vs. noise-injected labels; evaluate boundary-zone reliability on real benchmarks; compare against real-trained controls.
- **Main Risk:** Choosing the "right" noise model requires measuring real annotator noise (leverages IDEA-B-0047 outputs).
- **Research Cluster:** SYNTH-DATA / CALIBRATION

### IDEA-B-0229 — Asset diversity saturates: the 3D-asset scaling curve
- **One-sentence idea:** Measure downstream performance as a function of unique 3D asset count in simulation-generated training data to locate the point where buying more assets stops paying.
- **Problem:** Simulation pipelines license ever-larger asset libraries on the assumption that asset diversity drives transfer; the marginal value curve of assets (vs. scene composition variety from the same assets) has never been isolated.
- **Core Hypothesis (falsifiable):** At fixed rendered-image count, performance vs. unique-asset count saturates early (well below current library sizes) for most classes, while composition/viewpoint variety at fixed assets continues yielding gains — inverting current spending priorities.
- **Why Important:** Asset acquisition is a major synthetic-data cost; a measured saturation point converts procurement into engineering.
- **Why Possibly Novel:** Rendering-volume ablations exist; the asset-count vs. composition-variety factorization is not published.
- **Minimal Experiment:** Generate datasets over an (asset count x composition variety) grid in one simulator; train and evaluate transfer; fit saturation curves per class type.
- **Main Risk:** Saturation points likely differ by class granularity (vehicles vs. rare animals), requiring per-category reporting.
- **Research Cluster:** SYNTH-DATA

### IDEA-B-0230 — Optical effects beat material realism in rendering for transfer
- **One-sentence idea:** Factorially compare the transfer value of simulating camera optics (depth of field, motion blur, chromatic aberration) against improving material/lighting realism in synthetic training data.
- **Problem:** Rendering effort concentrates on materials and illumination (expensive, artist-driven), while optical effects (cheap, procedural) are often skipped; their relative contribution to sim-to-real transfer is unknown.
- **Core Hypothesis (falsifiable):** Adding measured-camera optical effects to basic renders improves real-data transfer more than upgrading materials/lighting at far lower cost, with the advantage concentrated in classes whose real appearance is optics-dominated (small, distant, moving objects).
- **Why Important:** Reorders the synthetic-pipeline investment stack with a cheap procedural win, complementing the sensor-noise attribution of IDEA-B-0224 at the optics stage.
- **Why Possibly Novel:** Individual pipelines include optics ad hoc; the controlled cost-matched comparison against material realism is missing.
- **Minimal Experiment:** Render 2x2 (optics on/off x materials basic/advanced) datasets; train and evaluate transfer per class; account effort/cost per cell.
- **Main Risk:** Optics parameters must match the target camera; mismatched optics could even hurt, complicating general claims.
- **Research Cluster:** SYNTH-DATA

### IDEA-B-0231 — Stress-testing the privacy promise of synthetic human data
- **One-sentence idea:** Test whether models trained on "privacy-safe" synthetic humans still enable re-identification or attribute inference about real individuals represented in the generator's training data.
- **Problem:** Synthetic person datasets are marketed as eliminating privacy risk; but generators fit on real people may transmit identifying information through the synthetic samples into downstream models — a laundering pathway the privacy claims ignore.
- **Core Hypothesis (falsifiable):** Membership-inference and attribute-linkage attacks against models trained purely on synthetic humans succeed at rates significantly above baseline for individuals in the generator's training set, refuting the categorical privacy claim.
- **Why Important:** Synthetic-data privacy claims are driving regulatory and procurement decisions; empirical stress tests must precede trust.
- **Why Possibly Novel:** Generator memorization and downstream privacy are studied separately; the end-to-end pipeline attack for dense vision tasks is unexplored.
- **Minimal Experiment:** Train segmenters on synthetic-person data from generators with known training rosters; run membership-inference attacks targeting roster individuals; compare against non-member controls.
- **Main Risk:** Attack success may be weak and heavily generator-dependent, requiring careful statistical treatment of near-null results.
- **Research Cluster:** SYNTH-DATA / NEG-RESULT

### IDEA-B-0232 — Prompt-space coverage predicts synthetic data value better than volume
- **One-sentence idea:** Test whether the embedding-space diversity of generation prompts predicts downstream gains from text-to-image synthetic data better than the number of generated images.
- **Problem:** Generation budgets are spent on image count with casual prompt design; if prompt diversity is the binding variable, the same budget produces far more value under coverage-optimized prompting.
- **Core Hypothesis (falsifiable):** At matched image counts, downstream performance scales with measured prompt-embedding coverage, and coverage-optimized prompt sets beat naive prompting by margins exceeding a several-fold increase in generation volume.
- **Why Important:** Provides a computable objective (coverage) for the prompt-engineering stage of synthetic pipelines, replacing folklore with optimization.
- **Why Possibly Novel:** Prompt diversity is intuited in practice; the quantitative coverage law and its exchange rate against volume are unmeasured.
- **Minimal Experiment:** Generate datasets under prompt sets of controlled coverage at fixed volume; train and compare; fit the coverage-performance relationship and the volume exchange rate.
- **Main Risk:** Coverage in text-embedding space may not translate to visual-mode coverage for all generators.
- **Research Cluster:** SYNTH-DATA / MULTIMODAL-SUP

### IDEA-B-0233 — Domain randomization works as regularization, not domain coverage
- **One-sentence idea:** Test the mechanism of domain randomization by comparing it against non-domain-related regularizers matched for effective augmentation strength.
- **Problem:** Domain randomization's story is that random textures/lighting force invariance to nuisance domains; but its gains might be generic regularization (input diversity preventing overfitting), predicting that matched-strength ordinary augmentation reproduces them — different mechanisms imply different scaling advice.
- **Core Hypothesis (falsifiable):** At matched augmentation-strength measures (feature-space perturbation magnitude), conventional strong augmentation on non-randomized renders recovers most of domain randomization's sim-to-real gain, and the residual specifically tracks nuisance dimensions that real deployment varies.
- **Why Important:** Mechanistic clarity determines whether teams should invest in physically plausible randomization ranges or just crank generic augmentation.
- **Why Possibly Novel:** Domain randomization is widely used but rarely mechanism-tested against strength-matched regularization controls.
- **Minimal Experiment:** Train on fixed renders + strong augmentation vs. randomized renders at matched perturbation budgets; evaluate real transfer; decompose residual gains by nuisance dimension.
- **Main Risk:** Defining and matching "augmentation strength" across image-space and render-space interventions is methodologically delicate.
- **Research Cluster:** SYNTH-DATA / ASSUMPTION

### IDEA-B-0234 — Synthetic-then-real ordering matters only below a real-data threshold
- **One-sentence idea:** Map when curriculum ordering (synthetic pretraining then real fine-tuning) beats mixing, as a function of real-data volume, to produce a practical decision rule.
- **Problem:** Pipelines argue about pretrain-then-finetune vs. joint mixing with anecdotal answers; the strategies' relative value plausibly depends on real-data volume and shift size, and the interaction map has never been drawn.
- **Core Hypothesis (falsifiable):** Below a real-data threshold, ordering strategies differ substantially (with sequential winning by avoiding synthetic-real interference), while above it all reasonable strategies converge — with the threshold predictable from the measured synthetic-real feature gap.
- **Why Important:** Ends a recurring engineering argument with a validated decision surface instead of another single-point ablation.
- **Why Possibly Novel:** Individual comparisons exist at single operating points; the volume-parameterized strategy map with threshold prediction is new.
- **Minimal Experiment:** Cross {sequential, mixed, curriculum-annealed} strategies against a real-data-volume ladder on two sim-real pairs; fit the strategy-preference map.
- **Main Risk:** Results may depend on optimization details (LR restarts) as much as strategy, requiring recipe standardization.
- **Research Cluster:** SYNTH-DATA / CROSS-DOMAIN

### IDEA-B-0235 — Generate hard negatives, not more positives
- **One-sentence idea:** Test whether synthetic near-miss examples (almost-instances that should not be detected) improve precision and boundary discipline more than the standard practice of generating additional positives.
- **Problem:** Generative augmentation exclusively produces positive examples; discrimination problems are usually bounded by confusable negatives, which generation could manufacture on demand (object-like textures, partial structures, look-alike classes) but never does.
- **Core Hypothesis (falsifiable):** Adding generated near-miss negatives at matched volume reduces false positives and improves calibrated precision substantially more than adding generated positives, with the biggest gains on classes whose errors are dominated by look-alike confusion.
- **Why Important:** Opens a new direction for generative augmentation targeting the error type (false positives) that positive generation cannot address.
- **Why Possibly Novel:** Hard-negative mining exists over real data; deliberate generative synthesis of near-misses for dense prediction is largely unexplored.
- **Minimal Experiment:** Build near-miss generation recipes (inpainting partial objects, morphing classes); train with positive vs. negative augmentation at matched volume; decompose error-type changes.
- **Main Risk:** Near-misses that are accidentally true positives poison training; quality control of "negativeness" is critical.
- **Research Cluster:** SYNTH-DATA

### IDEA-B-0236 — Asset-library taxonomies silently define synthetic label semantics
- **One-sentence idea:** Audit how simulator class definitions (inherited from asset-library folder structures) mismatch real-dataset ontologies, and test whether taxonomy alignment predicts per-class sim-to-real transfer.
- **Problem:** Synthetic datasets label pixels by asset category, which encodes the asset store's organization rather than any real ontology; per-class transfer failures may be definitional mismatches masquerading as domain gap.
- **Core Hypothesis (falsifiable):** A class-level taxonomy-alignment score (measured by cross-annotating samples under both definitions) predicts per-class sim-to-real transfer substantially better than visual-realism scores, and fixing high-mismatch classes' mappings recovers their transfer deficit.
- **Why Important:** Separates fixable bookkeeping failure from genuine appearance gap in sim-to-real analysis — reframing part of a research area as data hygiene.
- **Why Possibly Novel:** Ontology mismatch is studied across real datasets (IDEA-B-0217); the simulator-side version with transfer prediction is untouched.
- **Minimal Experiment:** Cross-annotate synthetic and real samples under both taxonomies for popular sim-real pairs; regress per-class transfer on alignment; test mapping corrections.
- **Main Risk:** Alignment scoring requires human annotation effort per class pair, bounding scale.
- **Research Cluster:** SYNTH-DATA / EVAL-WEAK

### IDEA-B-0237 — Models don't care about physics violations in generated data
- **One-sentence idea:** Test whether physically impossible generated training images (wrong shadows, floating objects, inconsistent illumination) transfer as well as physically correct ones, probing whether segmentation models use physical-consistency cues at all.
- **Problem:** Generation pipelines invest in physical plausibility assuming models need it; but if dense models are indifferent to physics-level scene coherence, that budget is wasted — and the finding would reveal something basic about what these models perceive.
- **Core Hypothesis (falsifiable):** Training sets matched in local appearance but differing in physical consistency yield statistically indistinguishable downstream performance, demonstrating that current segmenters exploit only local evidence and short-range context, not scene physics.
- **Why Important:** Either saves substantial generation compute or discovers that physics matters — both outcomes redirect synthetic-data practice, and the null would be a striking statement about model perception.
- **Why Possibly Novel:** Physical plausibility is assumed valuable; a controlled indifference test has not been run for dense prediction training data.
- **Minimal Experiment:** Construct paired physically-correct/violated synthetic sets via controlled rendering; train matched models; compare transfer with equivalence testing.
- **Main Risk:** Physics violations may correlate with local artifact differences, requiring careful appearance matching.
- **Research Cluster:** SYNTH-DATA / ASSUMPTION

### IDEA-B-0238 — Synthetic rare-hazard benchmarks may not rank models like real hazards do
- **One-sentence idea:** Validate whether model rankings on synthetically generated safety-critical edge cases (driving hazards) agree with rankings on real near-miss data.
- **Problem:** Safety evaluation increasingly relies on generated rare scenarios because real ones are scarce; if generated hazards systematically favor certain model families or miss real failure modes, safety cases built on them are unsound — a sharper, safety-specific instance of the general question in IDEA-B-0225.
- **Core Hypothesis (falsifiable):** Rankings of perception models on synthetic hazard suites correlate only weakly with rankings on curated real near-miss datasets, with divergence concentrated in hazard categories where generation fidelity is measurably poor (unusual object geometry, extreme lighting).
- **Why Important:** Directly tests the validity of an evaluation practice entering regulatory and industrial safety processes.
- **Why Possibly Novel:** Synthetic scenario generation is a growth area whose ranking validity against real incident data has not been measured.
- **Minimal Experiment:** Assemble matched synthetic and real hazard evaluation sets in one driving domain; evaluate 10+ perception models on both; analyze ranking agreement by hazard category.
- **Main Risk:** Real near-miss data access is restricted; partnerships or public incident datasets bound the study's scope.
- **Research Cluster:** SYNTH-DATA / EVAL-WEAK

### IDEA-B-0239 — What is multi-view consistency worth in generated training data?
- **One-sentence idea:** Quantify the downstream value of 3D-consistent generation (multi-view coherent scenes) over independent 2D generation at matched image quality and volume.
- **Problem:** 3D-aware generation is expensive; its pitch for training data is that geometric consistency teaches better representations, but the premium has never been isolated from image quality differences.
- **Core Hypothesis (falsifiable):** At matched per-image quality and count, multi-view-consistent training sets improve depth-dependent and occlusion-related capabilities (boundary ownership, amodal reasoning) over independent 2D generations, while pure appearance tasks show no difference — pricing consistency's specific value.
- **Why Important:** Tells synthetic-data engineering when 3D-aware generation earns its cost, and identifies which capabilities require geometric supervision.
- **Why Possibly Novel:** 3D-consistent generators are benchmarked on generation quality; their differential training value for dense tasks is unmeasured.
- **Minimal Experiment:** Generate matched 2D vs. multi-view-consistent sets; train segmenters; evaluate on capability-decomposed metrics including occlusion-boundary tests.
- **Main Risk:** Matching image quality across generation paradigms is hard; quality confounds could dominate.
- **Research Cluster:** SYNTH-DATA / MULTIMODAL-SUP

### IDEA-B-0240 — Sim-to-real transfers asymmetrically for things vs. stuff
- **One-sentence idea:** Characterize whether synthetic training transfers systematically better for object classes ("things") or amorphous regions ("stuff"), and identify the asset-vs-material mechanism behind the asymmetry.
- **Problem:** Sim-to-real results are reported in aggregate, but simulators construct things (meshes) and stuff (textures/shaders) through entirely different pipelines with different realism ceilings — predicting a structured transfer asymmetry nobody has isolated.
- **Core Hypothesis (falsifiable):** Per-class sim-to-real transfer efficiency differs systematically between things and stuff across simulators, and the direction/magnitude is predicted by which pipeline (geometry vs. material) dominates the class's appearance.
- **Why Important:** Guides hybrid data strategies (synthetic for one regime, real for the other) and explains cross-paper inconsistencies in sim-to-real results.
- **Why Possibly Novel:** The things/stuff axis has not been applied to sim-to-real transfer analysis.
- **Minimal Experiment:** Train on synthetic driving/indoor sets; evaluate per-class real transfer; group by thing/stuff and appearance mechanism; test the predictive account across two simulators.
- **Main Risk:** Class difficulty confounds (stuff classes are often easier) require careful normalization against real-data-trained baselines.
- **Research Cluster:** SYNTH-DATA / CROSS-DOMAIN

### IDEA-B-0241 — Insertion artifacts, not inserted objects, drive some augmentation gains
- **One-sentence idea:** Test whether models trained with diffusion-inpainted object insertion learn to detect insertion artifacts rather than object appearance, inflating benchmark gains that vanish on artifact-free data.
- **Problem:** Inpainting-based augmentation leaves subtle boundary and statistics artifacts co-located with the new labels; a model can satisfy the training objective by keying on artifacts, which generalizes to artifact-bearing validation sets but not to reality.
- **Core Hypothesis (falsifiable):** Models trained on inserted instances show a measurable performance gap between artifact-bearing and artifact-free test instances of the same classes, and artifact-detector probes confirm the shortcut's presence in proportion to that gap.
- **Why Important:** Protects the growing generative-augmentation practice from a self-deceiving evaluation loop and motivates artifact-suppressed insertion protocols.
- **Why Possibly Novel:** Shortcut learning on synthesis artifacts is suspected but unquantified for dense-prediction augmentation pipelines.
- **Minimal Experiment:** Train with inserted instances; evaluate on real instances vs. inserted instances; train artifact-presence probes; correlate probe strength with the generalization gap.
- **Main Risk:** Fully artifact-free insertion for the control arm is difficult; may require real photographed composites.
- **Research Cluster:** SYNTH-DATA / EVAL-WEAK

### IDEA-B-0242 — Synthetic test-set clones measure benchmark overfitting per method
- **One-sentence idea:** Build layout-matched synthetic clones of real test sets and use the real-vs-clone performance gap as a per-method benchmark-overfitting detector.
- **Problem:** Methods tuned for years on one benchmark may exploit its idiosyncrasies (annotation style, photographer bias); a controlled clone sharing content statistics but not those idiosyncrasies would expose which methods' scores are benchmark-specific — a measurement tool the field lacks.
- **Core Hypothesis (falsifiable):** The real-minus-clone performance gap varies systematically across methods, is larger for methods with more benchmark-specific development history, and predicts those methods' underperformance on genuinely new data collections.
- **Why Important:** Provides an early-warning instrument for benchmark overfitting without waiting years for new datasets to reveal it.
- **Why Possibly Novel:** Benchmark overfitting is studied via longitudinal holdouts; the synthetic-clone instrument is a new methodology.
- **Minimal Experiment:** Construct clones of one benchmark's val set via scene-matched rendering/generation; evaluate 20 methods on both; validate gap-based predictions against a held-back new collection.
- **Main Risk:** Clone imperfections affect methods differentially for reasons unrelated to overfitting, requiring careful calibration of the instrument itself.
- **Research Cluster:** SYNTH-DATA / EVAL-WEAK

### IDEA-B-0243 — Physics-based relighting helps only geometry-dependent classes
- **One-sentence idea:** Test whether relighting-model augmentation (physically plausible illumination changes) beats image-space photometric jitter specifically for classes whose appearance depends on 3D structure, and nowhere else.
- **Problem:** Relighting augmentation is much costlier than color jitter; its value should be concentrated where illumination interacts with geometry (shading, shadows, specularity), but the class-conditional value map has never been drawn.
- **Core Hypothesis (falsifiable):** Relighting augmentation's advantage over strength-matched photometric jitter is significant only for geometry/material-sensitive classes and near-zero for texture-flat classes, with the class ranking predictable from surface-property statistics.
- **Why Important:** Enables selective deployment of expensive augmentation where it pays, and clarifies the mechanism by which illumination augmentation works.
- **Why Possibly Novel:** Relighting augmentation exists; the class-conditional mechanism-mapped comparison against matched simple baselines is new.
- **Minimal Experiment:** Train with relighting vs. matched jitter; evaluate per-class under real illumination shifts; regress advantage on surface-property measures.
- **Main Risk:** Relighting model artifacts could suppress its measured value below the true ceiling.
- **Research Cluster:** SYNTH-DATA / ROBUSTNESS

### IDEA-B-0244 — Synthetic data stops helping once pretraining has seen everything
- **One-sentence idea:** Test whether generative data augmentation still adds value when fine-tuning web-scale-pretrained backbones, or whether its benefits were an artifact of information-poor initialization.
- **Problem:** Most synthetic-data evidence predates strong pretraining; if a web-pretrained backbone already encodes the visual modes synthetic data supplies, the practice may be obsolete for modern stacks — a live budget question for many teams.
- **Core Hypothesis (falsifiable):** The marginal gain from synthetic augmentation decreases sharply with pretraining strength across tasks, remaining significant only for genuinely out-of-corpus content (novel sensors, rare configurations) identifiable in advance via corpus-proximity measures (per IDEA-B-0201).
- **Why Important:** Prevents cargo-cult continuation of synthetic pipelines whose value era has passed, while precisely identifying where they still pay.
- **Why Possibly Novel:** Synthetic-data value and pretraining strength have not been crossed as experimental axes in a systematic study.
- **Minimal Experiment:** Cross pretraining-strength ladder with synthetic-augmentation arms on several tasks including an out-of-corpus domain; map the value surface.
- **Main Risk:** "Pretraining strength" is multidimensional; results need reporting against several pretraining variants.
- **Research Cluster:** SYNTH-DATA / ASSUMPTION

### IDEA-B-0245 — Synthetic fine-tuning silently erodes real-world calibration
- **One-sentence idea:** Measure the calibration cost of synthetic-data fine-tuning on real-data confidence behavior, even when accuracy improves.
- **Problem:** Synthetic data changes the statistics of the training distribution (perfect labels per IDEA-B-0228, unrealistic frequencies, artifact regularities); accuracy-focused evaluation would miss a degradation of the confidence channel that safety deployments rely on.
- **Core Hypothesis (falsifiable):** Models fine-tuned with substantial synthetic fractions show systematically worse real-data calibration and error-detection metrics than matched-accuracy real-only models, with degradation scaling with the synthetic fraction and concentrated in regions where synthetic and real statistics diverge.
- **Why Important:** Adds a mandatory reporting axis to synthetic-data papers and warns deployments that accuracy-positive synthetic data can be reliability-negative.
- **Why Possibly Novel:** Synthetic data's accuracy effects are extensively studied; its effect on the uncertainty channel is essentially unmeasured.
- **Minimal Experiment:** Train a synthetic-fraction ladder; evaluate real-data calibration/error-detection alongside accuracy; localize degradation via divergence maps.
- **Main Risk:** Effects may be small for well-mixed pipelines, requiring sensitive calibration metrics (IDEA-B-0078's protocol).
- **Research Cluster:** SYNTH-DATA / CALIBRATION

### IDEA-B-0246 — Dataset ecosystems inherit model collapse through republication
- **One-sentence idea:** Measure whether successive generations of public datasets (increasingly built with model assistance and synthetic content) show statistical convergence toward model outputs — ecosystem-level model collapse.
- **Problem:** Individual-pipeline feedback (IDEA-B-0156) scales to the ecosystem: published model-assisted datasets become training data for models that assist the next datasets; if diversity contracts across generations, the field's data substrate is degrading invisibly.
- **Core Hypothesis (falsifiable):** Dataset generations show measurable trends toward model-typical statistics (boundary smoothness signatures, label-distribution regularization, reduced annotation idiosyncrasy) correlated with their documented use of model assistance, and models trained on later generations show reduced behavioral diversity (per IDEA-B-0214).
- **Why Important:** An ecosystem-level diagnosis would motivate provenance standards and blind-annotation reserves before the substrate degrades further.
- **Why Possibly Novel:** Model collapse is studied in generative-loop simulations; the empirical audit of the real vision-dataset ecosystem is missing.
- **Minimal Experiment:** Chronologically order datasets with documented pipelines; measure model-typicality statistics per generation; correlate with assistance documentation; test downstream diversity effects.
- **Main Risk:** Confounds (changing content, tools, and conventions over time) are severe; requires careful causal humility and multiple markers.
- **Research Cluster:** SYNTH-DATA / ANNOT-EFF / PHENOMENON

### IDEA-B-0247 — Per-class generation quality predicts per-class downstream gain
- **One-sentence idea:** Validate class-conditional generative quality metrics as predictors of which classes benefit from synthetic augmentation, enabling budget allocation before training.
- **Problem:** Synthetic augmentation helps some classes and hurts others within the same dataset; without a per-class predictor, teams discover the allocation by expensive trial and error.
- **Core Hypothesis (falsifiable):** Class-conditional fidelity/diversity metrics of the generator predict the sign and rough magnitude of per-class downstream changes with useful accuracy, and metric-guided selective generation beats uniform generation at matched volume.
- **Why Important:** Turns synthetic augmentation from a blanket intervention into a targeted one, with the predictor doubling as a generator evaluation grounded in utility.
- **Why Possibly Novel:** Generative metrics and downstream utility are rarely connected at class granularity with prospective validation.
- **Minimal Experiment:** Compute per-class generator metrics; run uniform-augmentation training to obtain per-class deltas; fit the predictor; validate via selective-generation training.
- **Main Risk:** Per-class deltas are noisy (echoing IDEA-B-0150), demanding aggregated validation.
- **Research Cluster:** SYNTH-DATA

### IDEA-B-0248 — Controllability is synthetic data's unique asset: occlusion curricula
- **One-sentence idea:** Test whether procedurally controlled occlusion curricula (impossible to collect in real data) teach occlusion robustness that transfers to real scenes, isolating controllability as synthetic data's distinctive value.
- **Problem:** Synthetic data debates focus on realism deficits, ignoring the one axis where synthesis strictly dominates collection: precise control of factors (occlusion level, order, geometry); whether factor-controlled training buys transferable capability is the right question and it is untested.
- **Core Hypothesis (falsifiable):** Models trained with graded occlusion curricula on synthetic scenes outperform models trained on occlusion-matched but uncontrolled synthetic data on real occlusion-stratified evaluation, demonstrating value from control itself, not content.
- **Why Important:** Reframes the synthetic-data value proposition around controllability, opening a family of factor-curriculum methods no real-data pipeline can replicate.
- **Why Possibly Novel:** Curriculum learning and synthetic data are old; using synthesis's factor control as the experimental variable (against content-matched controls) is a fresh design.
- **Minimal Experiment:** Generate matched controlled vs. shuffled occlusion datasets; train; evaluate on real occlusion-stratified benchmarks; extend to one more factor (scale) for generality.
- **Main Risk:** Gains may be curriculum-schedule sensitive, requiring schedule sweeps to distinguish control value from tuning luck.
- **Research Cluster:** SYNTH-DATA

### IDEA-B-0249 — Sim-to-real gaps are content gaps, not style gaps
- **One-sentence idea:** Decompose the sim-to-real gap into style (low-level appearance) and content (object/layout co-occurrence) components using style-transfer bridges in both directions.
- **Problem:** Sim-to-real research overwhelmingly attacks style (translation, alignment); if the dominant residual is content statistics — what appears where, with what — then style-focused effort is optimizing the minority component.
- **Core Hypothesis (falsifiable):** Style-neutralized comparisons (synthetic restyled as real, real restyled as synthetic) leave most of the transfer gap intact, attributing the majority share to content statistics, with the split varying predictably by class type (extending IDEA-B-0240).
- **Why Important:** Redirects a large research area toward layout/content realism (cheap, per IDEA-B-0223) and away from saturated style alignment.
- **Why Possibly Novel:** Style-transfer bridges have been used as methods; using them bidirectionally as measurement instruments for gap decomposition is a different purpose.
- **Minimal Experiment:** Build bidirectional restyling for a sim-real pair; evaluate the four content-style combinations; attribute gap shares per class.
- **Main Risk:** Imperfect style transfer leaks content changes, contaminating the decomposition; needs transfer-quality controls.
- **Research Cluster:** SYNTH-DATA / CROSS-DOMAIN

### IDEA-B-0250 — Negative result: GAN sim-to-real translation vs. simple photometric augmentation
- **One-sentence idea:** Rigorously test whether image-translation preprocessing of synthetic training data (GAN/diffusion sim-to-real style transfer) beats strength-matched photometric augmentation at matched compute.
- **Problem:** Translation-based sim-to-real pipelines are widely assumed valuable and add significant complexity; their evaluations rarely include the trivial alternative of strong photometric augmentation with the saved compute.
- **Core Hypothesis (falsifiable):** Across sim-real pairs, translation preprocessing provides no significant transfer benefit over compute-matched photometric-augmentation baselines, with translation's apparent gains in prior work explained by weak baselines and unmatched budgets.
- **Why Important:** If confirmed, a standard pipeline stage can be deleted across many projects; if refuted under fair conditions, the technique's real value is finally established.
- **Why Possibly Novel:** The genre has never faced a strength- and compute-matched baseline audit in dense prediction.
- **Minimal Experiment:** Reproduce 3 translation pipelines; construct compute-matched augmentation baselines; evaluate transfer on two sim-real pairs with seeds.
- **Main Risk:** Translation quality varies by implementation era; must use the strongest available translators to keep the negative meaningful.
- **Research Cluster:** SYNTH-DATA / NEG-RESULT

### IDEA-B-0251 — Which layers actually transfer from natural to medical images?
- **One-sentence idea:** Perform layer-resolved transfer surgery (keep/reset/re-train each stage independently) to map where natural-image pretraining helps, is neutral, or actively hurts medical segmentation.
- **Problem:** Natural-to-medical transfer is standard practice justified by aggregate gains, but the aggregate may hide a mixture: early filters helping, middle semantic layers encoding natural-image priors that mislead, and the mixture has never been mapped.
- **Core Hypothesis (falsifiable):** Transfer benefit is concentrated in early layers, middle layers are replaceable by random re-initialization with no loss, and for some modalities keeping middle layers is measurably worse than resetting them — a non-monotonic transfer profile.
- **Why Important:** Enables surgical transfer recipes (keep what helps, reset what hurts) and corrects the mental model of pretraining as uniformly beneficial.
- **Why Possibly Novel:** Layer-wise transfer analysis exists for classification; the keep/reset/re-train factorial for cross-domain dense prediction with harm detection is not established.
- **Minimal Experiment:** Cross layer-block treatments on natural-pretrained backbones fine-tuned for 3 medical modalities; map per-block contribution profiles.
- **Main Risk:** Block interactions (co-adapted layers) may make single-block attribution unstable; needs paired-block conditions.
- **Research Cluster:** CROSS-DOMAIN / REP-MISMATCH

### IDEA-B-0252 — Cross-domain few-shot segmentation: episodic training audit
- **One-sentence idea:** Test whether episodic meta-training for few-shot segmentation survives against simple fine-tuning with strong augmentation when the domain gap is large.
- **Problem:** Few-shot segmentation methods are built on episodic meta-learning, but growing classification evidence suggests simple baselines win, and the cross-domain regime (where few-shot matters practically) is exactly where episodic training's in-domain assumptions break.
- **Core Hypothesis (falsifiable):** Under matched backbones and tuning budgets, episodic methods lose to fine-tuning-based baselines on cross-domain few-shot segmentation benchmarks, with the deficit growing with domain gap magnitude.
- **Why Important:** The practical use case of few-shot segmentation is new domains; if the dominant methodology fails exactly there, the subfield needs redirection.
- **Why Possibly Novel:** Baseline audits exist for few-shot classification; the cross-domain segmentation version with gap-magnitude analysis is missing.
- **Minimal Experiment:** Re-run 4 episodic methods and 3 simple baselines across domain-gap-graded few-shot tasks (natural→aerial→medical); report performance vs. gap.
- **Main Risk:** Few-shot evaluation variance is high; needs many episodes and seeds for conclusive comparisons.
- **Research Cluster:** CROSS-DOMAIN / NEG-RESULT

### IDEA-B-0253 — A cheap transferability index from frequency statistics
- **One-sentence idea:** Test whether spectral-content similarity between source and target datasets predicts transfer performance better than semantic similarity measures, yielding a compute-free transferability estimate.
- **Problem:** Choosing a source dataset/checkpoint for a new domain is done by intuition or expensive trial; existing transferability metrics require forward passes and labels, while simple image statistics might suffice.
- **Core Hypothesis (falsifiable):** Across a source-target transfer matrix, frequency-content similarity correlates with fine-tuned performance at least as strongly as embedding-based semantic similarity, and a combined two-statistic index predicts the best source for held-out targets reliably.
- **Why Important:** A validated cheap index removes guesswork from a decision every applied team makes, and its success/failure teaches what transfer actually depends on.
- **Why Possibly Novel:** Transferability estimation is an active area, but image-statistics-only predictors benchmarked against learned ones for dense prediction are unexplored.
- **Minimal Experiment:** Build a 6x6 source-target transfer matrix; compute candidate indices; compare predictive power; validate source selection prospectively.
- **Main Risk:** Frequency similarity may proxy resolution/sensor rather than transfer-relevant structure, failing on semantic gaps.
- **Research Cluster:** CROSS-DOMAIN / EVAL-WEAK

### IDEA-B-0254 — Aerial-ground transfer fails on scale-context statistics, not viewpoint
- **One-sentence idea:** Decompose the aerial-to-ground (and reverse) transfer gap into viewpoint geometry vs. object-scale/context statistics by constructing scale-normalized intermediate evaluations.
- **Problem:** The severe transfer gap between overhead and ground imagery is attributed to viewpoint, but the accompanying changes in object scale distributions and context density are confounded with it — and each explanation implies different bridging strategies.
- **Core Hypothesis (falsifiable):** Scale-and-context-normalized transfer (resampling ground images to aerial-like object-size and density statistics) closes a large fraction of the gap without any viewpoint correction, attributing the majority share to statistics rather than geometry.
- **Why Important:** If statistics dominate, cheap normalization bridges the domains and viewpoint-invariance research is deprioritized for this pair.
- **Why Possibly Novel:** Aerial domain adaptation exists; the explicit viewpoint-vs-statistics decomposition with normalized intermediates has not been done.
- **Minimal Experiment:** Construct normalized evaluation ladders between a ground and aerial dataset with shared classes; measure gap closure per normalization step.
- **Main Risk:** Full normalization changes image realism, potentially introducing its own artifacts into the measurement.
- **Research Cluster:** CROSS-DOMAIN / SMALL-OBJ

### IDEA-B-0255 — Self-supervised features cross bigger domain gaps than supervised ones
- **One-sentence idea:** Systematically compare SSL vs. supervised pretraining transfer as a function of domain gap magnitude, testing whether SSL's advantage appears only beyond a gap threshold.
- **Problem:** SSL and supervised pretraining trade wins across scattered transfer papers; the confusion may resolve into a clean pattern — supervised wins near-domain, SSL wins far-domain — but nobody has ordered the comparison along a gap axis.
- **Core Hypothesis (falsifiable):** At matched in-domain accuracy, the SSL-minus-supervised transfer difference increases monotonically with measured domain gap, crossing zero at a characterizable threshold — because supervised features commit to source-label abstractions that stop being valid.
- **Why Important:** Converts an unresolved either/or debate into a conditional rule practitioners can apply using the gap measures of IDEA-B-0253.
- **Why Possibly Novel:** Individual comparisons exist; the gap-ordered synthesis with a crossing-point account is new.
- **Minimal Experiment:** Fine-tune matched SSL/supervised backbones across a gap-graded target ladder; plot the difference curve; test threshold stability across SSL methods.
- **Main Risk:** "Matched" pretraining across paradigms is hard to define; multiple matching criteria must agree.
- **Research Cluster:** CROSS-DOMAIN

### IDEA-B-0256 — Transferable knowledge is destroyed in the first fine-tuning steps
- **One-sentence idea:** Measure when during fine-tuning the source-domain capabilities are lost, testing whether most forgetting is an early-transient effect preventable by brief protective schedules.
- **Problem:** Catastrophic forgetting in transfer is treated as gradual erosion; if it is instead concentrated in the first optimization steps (large mismatched gradients through unadapted heads), cheap interventions (head warmup, early LR shaping) could preserve source capability nearly for free.
- **Core Hypothesis (falsifiable):** Source-task performance drops most steeply within the first ~1% of fine-tuning steps, the drop is causally linked to gradient magnitude through randomly initialized heads (verified by head-warmup ablations), and protective schedules retain most source capability at no target-performance cost.
- **Why Important:** Timing-resolved understanding turns forgetting mitigation from heavyweight methods (rehearsal, regularization) into schedule hygiene.
- **Why Possibly Novel:** Forgetting curves are rarely measured at step resolution with causal head-gradient attribution for dense prediction transfer.
- **Minimal Experiment:** Fine-tune with dense source-eval checkpointing; ablate head warmup and early LR policies; report forgetting-time profiles and retention outcomes.
- **Main Risk:** The early-transient pattern may hold only for large domain gaps or particular optimizers, needing scoped claims.
- **Research Cluster:** CROSS-DOMAIN / PHENOMENON

### IDEA-B-0257 — "Frozen features suffice" conclusions are probe-design artifacts
- **One-sentence idea:** Test how strongly conclusions about frozen-representation quality for segmentation depend on probe architecture (linear per-pixel vs. attention-pooled vs. multi-scale probes).
- **Problem:** The field infers representation quality from probing, but dense tasks require spatial reassembly that a linear probe cannot perform; the same frozen features may look poor under one probe and excellent under another, making probe choice an uncontrolled parameter in representation claims.
- **Core Hypothesis (falsifiable):** Rankings of pretrained representations by frozen-probe segmentation performance change substantially across probe designs, and probe capacity interacts with representation type (e.g., contrastive features need different readout than MAE features) — invalidating cross-paper probe comparisons.
- **Why Important:** Probing underpins how the field evaluates pretraining; establishing its design sensitivity forces standardized protocols and reinterprets published rankings.
- **Why Possibly Novel:** Probe-sensitivity critiques exist in NLP; the dense-prediction version with representation-probe interaction analysis is missing.
- **Minimal Experiment:** Evaluate 8 pretrained backbones under 4 probe designs on 2 segmentation datasets; quantify ranking stability and interaction effects.
- **Main Risk:** An unbounded probe space invites "you didn't try the right probe" criticism; needs principled probe taxonomy.
- **Research Cluster:** CROSS-DOMAIN / EVAL-WEAK / REP-MISMATCH

### IDEA-B-0258 — Adversarial domain alignment corrupts conditionals exactly at boundaries
- **One-sentence idea:** Localize the failure of marginal-alignment domain adaptation, testing whether matching feature marginals systematically distorts class-conditional structure in boundary regions.
- **Problem:** Domain-adversarial methods align feature distributions without labels; theory says marginal alignment can harm conditional alignment, but where this damage lands in dense prediction — and whether it is predictable — is unknown.
- **Core Hypothesis (falsifiable):** Adversarially aligned models show error increases concentrated in boundary zones and minority-class regions (where conditional structure is fragile), with damage magnitude predicted by the class-frequency mismatch between domains — while interior majority-class regions benefit.
- **Why Important:** Turns a theoretical caveat into a spatial diagnosis, telling practitioners when adversarial alignment is safe and motivating conditional-aware alternatives only where needed.
- **Why Possibly Novel:** The marginal-vs-conditional tension is known abstractly; its spatial localization and frequency-mismatch predictor in segmentation are not.
- **Minimal Experiment:** Train adversarial DA models across domain pairs with varied frequency mismatch; map error deltas by region type; test the predictive relationship.
- **Main Risk:** Alignment strength is a confound; requires dose-response designs over the adversarial weight.
- **Research Cluster:** CROSS-DOMAIN / BOUNDARY

### IDEA-B-0259 — The modality gap is an input-adapter problem
- **One-sentence idea:** Test whether transferring RGB models to thermal/depth/NIR requires only re-learning the earliest layers, with everything downstream frozen and intact.
- **Problem:** Cross-modality transfer is treated like severe domain shift requiring full adaptation; but if mid-level structure (shapes, layouts) is modality-invariant, the gap should be bridgeable by a thin input adapter — a much cheaper and more maintainable pattern.
- **Core Hypothesis (falsifiable):** Re-training only the first block (or a small adapter) on modest modality-specific data recovers most of full-fine-tuning performance across RGB→thermal/depth transfers, and the residual gap concentrates in classes whose modality appearance is semantically different (hot objects in thermal), not merely restyled.
- **Why Important:** A validated adapter-sufficiency result changes deployment architecture for multi-sensor systems (one trunk, thin per-sensor stems) and maps what is truly modality-specific in visual representations.
- **Why Possibly Novel:** Input adapters exist as engineering; the sufficiency measurement with a semantic-residual account across modalities is not established.
- **Minimal Experiment:** Compare {stem-only, adapter, full} fine-tuning across three modality transfers at several data budgets; decompose residuals per class.
- **Main Risk:** Normalization statistics throughout the trunk may need updating, blurring the "frozen downstream" claim.
- **Research Cluster:** CROSS-DOMAIN / MULTIMODAL-SUP

### IDEA-B-0260 — Is language anchoring causal for cross-domain robustness?
- **One-sentence idea:** Isolate whether text alignment in vision-language pretraining causally improves visual domain transfer, or merely correlates with the data scale that accompanies it.
- **Problem:** CLIP-style models transfer domains well, and language anchoring is credited — but such models also see uniquely diverse data, and no controlled experiment separates the objective's contribution from the corpus's.
- **Core Hypothesis (falsifiable):** At matched data and compute, language-aligned pretraining yields better cross-domain segmentation transfer than image-only contrastive pretraining on the same image corpus, with the advantage concentrated in classes whose names are stable across domains — supporting a semantic-anchor mechanism.
- **Why Important:** Determines whether future robust-transfer pretraining needs text or just scale — a major strategic question for anyone training foundation vision models.
- **Why Possibly Novel:** CLIP-vs-SSL comparisons exist but rarely control the corpus; the matched-corpus causal design focused on dense-task domain transfer is new.
- **Minimal Experiment:** Pretrain matched text-aligned and image-only models on one captioned corpus; fine-tune/probe across domain-graded segmentation targets; compare transfer profiles per class.
- **Main Risk:** Matched pretraining at meaningful scale is expensive; conclusions from affordable scales may not extrapolate.
- **Research Cluster:** CROSS-DOMAIN / MULTIMODAL-SUP

### IDEA-B-0261 — Early gradient conflict predicts negative transfer
- **One-sentence idea:** Validate gradient-alignment statistics measured in the first fine-tuning steps as a predictor of whether a source checkpoint will help or hurt on a target task.
- **Problem:** Negative transfer (pretrained worse than random) occurs unpredictably; teams discover it only after full training, and no cheap early-warning indicator exists for dense tasks.
- **Core Hypothesis (falsifiable):** The conflict between (proxy) source-preserving gradients and target-task gradients during early fine-tuning predicts final transfer benefit sign across source-target pairs with high accuracy, enabling checkpoint selection after <1% of training cost.
- **Why Important:** A validated early predictor saves large amounts of compute in checkpoint selection and gives mechanistic insight into what makes transfer fail.
- **Why Possibly Novel:** Gradient-conflict analysis exists in multi-task learning; its use as a prospective negative-transfer predictor for dense-prediction fine-tuning is untested.
- **Minimal Experiment:** Build a transfer matrix with known outcomes; measure early gradient statistics per pair; fit and prospectively validate the predictor on held-out pairs.
- **Main Risk:** The predictor may capture LR-schedule interactions rather than intrinsic compatibility, failing under recipe changes.
- **Research Cluster:** CROSS-DOMAIN / PHENOMENON

### IDEA-B-0262 — Source diversity beats source size for transfer
- **One-sentence idea:** Test whether the diversity of source-domain training data predicts downstream transfer better than its volume, at matched pretraining compute.
- **Problem:** Pretraining data strategy defaults to scale, but transfer to new domains may depend on the breadth of visual modes seen rather than the count of images; the two are conflated in every natural corpus comparison.
- **Core Hypothesis (falsifiable):** At matched image count and compute, pretraining corpora curated for diversity (cluster-coverage-maximized) transfer better to held-out domains than volume-matched random or redundancy-heavy corpora, and transfer scales more steeply with measured diversity than with count.
- **Why Important:** Provides a data-curation objective for transfer-oriented pretraining, cheaper than raw scaling and directly actionable for domain-specific foundation models.
- **Why Possibly Novel:** Data curation research targets quality filtering; the diversity-vs-volume factorial for dense-task transfer is unmeasured.
- **Minimal Experiment:** Construct matched corpora varying diversity at fixed size; pretrain; evaluate transfer across a target ladder; fit both scaling relationships.
- **Main Risk:** Diversity measures are embedding-dependent; conclusions need robustness across measurement choices.
- **Research Cluster:** CROSS-DOMAIN

### IDEA-B-0263 — Domain knowledge is not modular: the mixture-of-experts test
- **One-sentence idea:** Test whether per-domain expert models with learned routing match a single jointly trained model, probing whether domain competence factorizes into separable modules.
- **Problem:** Architectures increasingly assume domain knowledge is modular (per-domain adapters, experts); if joint training instead builds entangled shared representations that outperform any routed combination of specialists, the modularity assumption misleads system design.
- **Core Hypothesis (falsifiable):** At matched total capacity and compute, jointly trained models outperform ideally routed domain-expert mixtures on both seen and unseen domains, with the gap growing on domain-boundary inputs — evidence that cross-domain shared structure, not separable expertise, drives multi-domain competence.
- **Why Important:** Settles a live architecture question (experts vs. monoliths) for multi-domain perception with implications for continual domain addition.
- **Why Possibly Novel:** MoE research optimizes efficiency; the modularity-of-domain-knowledge question as a falsifiable scientific claim for dense prediction is distinct.
- **Minimal Experiment:** Train experts, oracle-routed mixtures, learned-routed mixtures, and joint models at matched capacity across a multi-domain suite; compare on seen/unseen/boundary conditions.
- **Main Risk:** Routing quality confounds the modularity conclusion; oracle-routing arms are essential.
- **Research Cluster:** CROSS-DOMAIN / REP-MISMATCH

### IDEA-B-0264 — Domain ordering matters: near-to-far curricula in sequential transfer
- **One-sentence idea:** Test whether the order of adapting through a sequence of domains (near-to-far vs. far-to-near vs. random) changes final multi-domain competence and forgetting.
- **Problem:** Continual/sequential domain adaptation treats domain order as given; if order causally shapes outcomes (stepping-stone effects), deployment schedules and data-release strategies should be planned rather than accepted.
- **Core Hypothesis (falsifiable):** Near-to-far ordering yields higher final performance on the farthest domain and lower cumulative forgetting than random or far-first orders at matched exposure, with the benefit predicted by inter-domain distance structure.
- **Why Important:** Establishes curriculum principles for the domain axis, applicable to fleets that encounter environments in controllable orders (staged rollouts).
- **Why Possibly Novel:** Task-order effects are studied in continual learning; systematic domain-geometry-based ordering experiments for dense prediction are missing.
- **Minimal Experiment:** Define a domain ladder with measured distances; train all order permutations of 4–5 domains; compare final competence and forgetting profiles.
- **Main Risk:** Order effects may be small relative to method effects (replay, regularization), requiring interaction analysis.
- **Research Cluster:** CROSS-DOMAIN

### IDEA-B-0265 — Sketch transfer as a unified shape-competence diagnostic
- **One-sentence idea:** Validate transfer performance to line-drawing/sketch domains as a compact diagnostic that predicts a model's shape reliance, corruption robustness, and cross-domain generalization simultaneously.
- **Problem:** Shape bias, robustness, and transferability are measured with separate expensive protocols; if sketch-domain transfer (which strips texture entirely) predicts all three, one cheap test could replace a battery.
- **Core Hypothesis (falsifiable):** Zero-shot/probe performance on sketch-rendered segmentation correlates strongly across models with cue-conflict shape indices, corruption robustness, and natural-domain transfer — and adding sketch performance to model cards improves downstream model-selection outcomes measurably.
- **Why Important:** A validated single diagnostic simplifies model auditing and supports the theory that shape competence underlies multiple desirable properties.
- **Why Possibly Novel:** Sketch domains are used as transfer targets; their validation as a predictive diagnostic instrument is a different use.
- **Minimal Experiment:** Render sketch versions of benchmark scenes; evaluate 25+ models; correlate against the three target properties; test selection utility prospectively.
- **Main Risk:** Sketch rendering style choices may drive results; multiple rendering pipelines needed.
- **Research Cluster:** CROSS-DOMAIN / ROBUSTNESS

### IDEA-B-0266 — Intensity standardization explains most cross-modality adaptation gains
- **One-sentence idea:** Audit medical cross-modality (CT→MR and cross-sequence) adaptation methods against the trivial baseline of histogram/intensity standardization to isolate their genuine contribution.
- **Problem:** Medical domain adaptation papers demonstrate gains over source-only baselines while omitting classical intensity-normalization preprocessing that radiology pipelines have used for decades — the reported gains may largely duplicate it.
- **Core Hypothesis (falsifiable):** Standard intensity harmonization recovers a majority of published adaptation gains across method families, and the ranking of adaptation methods changes materially when all are evaluated on standardized inputs.
- **Why Important:** Re-baselines a clinically consequential subfield, separating genuine methodological progress from rediscovered preprocessing.
- **Why Possibly Novel:** The systematic strong-baseline audit against classical harmonization has not been performed across the modern medical-DA literature.
- **Minimal Experiment:** Re-run representative medical DA methods with and without harmonized preprocessing on public cross-modality benchmarks; tabulate residual gains.
- **Main Risk:** Harmonization interacts with some methods' assumptions, requiring per-method integration care to keep comparisons fair.
- **Research Cluster:** CROSS-DOMAIN / NEG-RESULT

### IDEA-B-0267 — Dataset-distance metrics don't predict transfer outcomes
- **One-sentence idea:** Benchmark popular domain-gap measures (FID-style, MMD, embedding distances) against actual transfer performance across many source-target pairs to test whether "domain distance" as currently measured means anything for dense prediction.
- **Problem:** Papers justify difficulty and method choices with domain-distance numbers, but the predictive validity of these measures for transfer outcomes has never been established — they may measure style differences irrelevant to what transfer needs.
- **Core Hypothesis (falsifiable):** Across a large transfer matrix, standard gap metrics correlate weakly with fine-tuned transfer performance and inconsistently with each other, while task-aware measures (label-conditional feature distances) predict substantially better — demonstrating the standard metrics' invalidity for their common use.
- **Why Important:** Removes a pseudo-quantitative crutch from the literature and replaces it with validated alternatives, affecting how hundreds of papers frame their problems.
- **Why Possibly Novel:** Individual metric critiques exist; the comprehensive predictive-validity benchmark for dense-prediction transfer is missing.
- **Minimal Experiment:** Compute 8 gap measures over a 10x10 source-target matrix with measured transfer outcomes; report predictive validity and inter-metric agreement.
- **Main Risk:** Transfer outcomes depend on recipes; the matrix must standardize training to isolate the metrics' validity.
- **Research Cluster:** CROSS-DOMAIN / EVAL-WEAK

### IDEA-B-0268 — Domain vectors compose: adapter arithmetic for unseen domain pairs
- **One-sentence idea:** Test whether domain adaptations learned as parameter deltas compose additively — combining a "night" vector and a "rain" vector to handle never-seen rainy nights.
- **Problem:** Real deployments face compositional conditions (weather x time x sensor) that can't all be trained; if domain knowledge in parameter space composes linearly, coverage of the combinatorial space becomes tractable from single-factor data.
- **Core Hypothesis (falsifiable):** Adapter/task-vector arithmetic for single-factor domain shifts produces combined-condition performance substantially above the base model and approaching jointly trained two-factor adapters, with composition error predicted by the vectors' interference (inner product) statistics.
- **Why Important:** Compositional coverage from factored training data is a scaling shortcut for robustness engineering, and success would reveal surprising linearity in how networks encode domain transformations.
- **Why Possibly Novel:** Task arithmetic is studied for classification abilities; factored environmental-domain composition for dense prediction with interference-based error prediction is new.
- **Minimal Experiment:** Train single-factor adapters on driving data (night, rain, fog); evaluate arithmetic combinations on real multi-factor conditions; compare against joint training and test the interference predictor.
- **Main Risk:** Multi-factor real evaluation data is scarce for exactly the rare combinations of interest.
- **Research Cluster:** CROSS-DOMAIN / PHENOMENON

### IDEA-B-0269 — Backward transfer: target fine-tuning can improve the source domain
- **One-sentence idea:** Characterize when fine-tuning on a new domain improves (rather than degrades) source-domain performance, testing the hypothesis that shared-physics domains donate regularization to each other.
- **Problem:** Transfer is assumed unidirectional (target gains, source forgets); scattered observations of backward improvement suggest an unexplored regime where domains are mutually informative, whose conditions nobody has mapped.
- **Core Hypothesis (falsifiable):** Backward transfer is systematically positive when target domains share generative physics with the source but differ in nuisance statistics (new city, new season), and systematically negative for gaps involving semantic redefinition — a predictable sign structure rather than noise.
- **Why Important:** Positive backward transfer would change data strategy (new-domain data as free source-domain improvement) and sharpen theories of what fine-tuning changes.
- **Why Possibly Novel:** Backward transfer is a continual-learning metric; its sign-structure mapping across domain-relationship types for dense prediction is unstudied.
- **Minimal Experiment:** Fine-tune across a taxonomy of domain relationships with dense source evaluation; map backward-transfer sign against relationship type; validate the predictor on new pairs.
- **Main Risk:** Effects may be small and recipe-dependent, requiring many seeds for reliable sign estimation.
- **Research Cluster:** CROSS-DOMAIN / PHENOMENON

### IDEA-B-0270 — Shared preprocessing pipelines inflate cross-domain claims
- **One-sentence idea:** Measure how much cross-domain evaluation results depend on source and target sharing the same resize/crop/normalization pipeline, a hidden alignment real deployments won't have.
- **Problem:** Benchmarks process all domains through identical preprocessing, silently harmonizing resolution, aspect ratio, and intensity statistics; deployed systems receive data through heterogeneous pipelines, so published cross-domain robustness may overstate reality.
- **Core Hypothesis (falsifiable):** Introducing realistic preprocessing heterogeneity (different resize kernels, crop policies, normalization constants) degrades cross-domain performance substantially beyond the content-level domain gap, and some published method rankings invert under preprocessing-mismatched evaluation.
- **Why Important:** Exposes an evaluation-realism gap that is trivial to fix in benchmarks and materially affects deployment predictions.
- **Why Possibly Novel:** Preprocessing effects are studied for reproducibility; their role as hidden domain alignment in transfer evaluation is unexamined.
- **Minimal Experiment:** Re-evaluate cross-domain results under a grid of preprocessing mismatches; quantify degradation and ranking stability; propose a heterogeneity-robust protocol.
- **Main Risk:** The space of "realistic" mismatches is large; needs grounding in surveyed deployment pipelines.
- **Research Cluster:** CROSS-DOMAIN / EVAL-WEAK

### IDEA-B-0271 — Documented acquisition parameters explain cross-site medical variance
- **One-sentence idea:** Test how much cross-site performance variance in medical segmentation is explained by documented acquisition metadata (scanner model, protocol parameters), enabling metadata-conditional harmonization instead of blind adaptation.
- **Problem:** Cross-site degradation is treated as opaque domain shift requiring learned adaptation; but sites differ in recorded, structured ways (device, sequence parameters, dose), and if these explain most variance, principled physics-aware harmonization beats black-box methods.
- **Core Hypothesis (falsifiable):** Regression of per-site performance drops on acquisition metadata explains the majority of cross-site variance across public multi-site datasets, and conditioning normalization on metadata recovers a large share of the drop — leaving a small residual for true population/anatomy shift.
- **Why Important:** Decomposes a clinically critical problem into a solvable engineering part and a genuine distribution-shift part, right-sizing the adaptation-method effort.
- **Why Possibly Novel:** Scanner effects are known in medical imaging; the variance-decomposition framing with metadata-conditional correction benchmarked against learned DA is not established.
- **Minimal Experiment:** Use multi-site public datasets with metadata; fit variance decompositions; implement metadata-conditional normalization; compare against DA baselines.
- **Main Risk:** Metadata completeness varies; missing-field patterns may correlate with the outcome, biasing the decomposition.
- **Research Cluster:** CROSS-DOMAIN / PHENOMENON

### IDEA-B-0272 — Frozen normalization statistics across the gap-magnitude spectrum
- **One-sentence idea:** Systematically map when freezing vs. re-estimating vs. fine-tuning normalization layers wins during cross-domain fine-tuning, as a function of domain gap and data budget.
- **Problem:** Practice contains contradictory folklore (freeze BN for small data; adapt BN for domain shift); both are right somewhere, and the crossover structure — the actual decision rule — has never been mapped.
- **Core Hypothesis (falsifiable):** The optimal normalization treatment is a predictable function of gap magnitude and target data volume, with re-estimation winning at large-gap/low-data, fine-tuning at large-data, and freezing at small-gap/small-data — forming a phase diagram stable across architectures.
- **Why Important:** Replaces contradictory rules of thumb with a validated decision surface for one of the most common transfer configuration choices.
- **Why Possibly Novel:** Individual comparisons abound; the two-axis phase diagram with cross-architecture validation is not published.
- **Minimal Experiment:** Cross normalization treatments with a (gap x budget) grid over three architectures; map the winning-treatment regions; validate on a held-out domain pair.
- **Main Risk:** Norm-layer type (BN/GN/LN) adds a third axis that may fragment the phase diagram.
- **Research Cluster:** CROSS-DOMAIN

### IDEA-B-0273 — Transfer works by retrieval: source neighbors explain target predictions
- **One-sentence idea:** Test whether fine-tuned models' predictions on target-domain inputs are largely explained by their nearest source-training neighbors in feature space, supporting a memorization-interpolation account of transfer.
- **Problem:** Competing accounts of transfer (abstract feature reuse vs. example-based interpolation) predict different failure modes and different data strategies, but they are rarely discriminated empirically for dense prediction.
- **Core Hypothesis (falsifiable):** Target predictions (including errors) are predicted by label statistics of retrieved source neighbors substantially above chance, the dependence weakens with target fine-tuning data volume in a measurable way, and neighbor-poor target regions are exactly where transfer fails.
- **Why Important:** A retrieval-based account would make transfer auditable (inspect the neighbors), predictable (coverage analysis), and improvable by targeted source curation.
- **Why Possibly Novel:** Retrieval explanations exist for language models; systematic neighbor-attribution analysis for cross-domain dense prediction is new.
- **Minimal Experiment:** Build source feature indices; regress target predictions/errors on neighbor statistics across transfer pairs; test the coverage-failure correspondence.
- **Main Risk:** Feature space choice determines neighbors; conclusions need stability across representation layers.
- **Research Cluster:** CROSS-DOMAIN / PHENOMENON

### IDEA-B-0274 — Where to split shared-vs-specific parameters is predictable from gap type
- **One-sentence idea:** Test whether the optimal depth at which to branch domain-specific parameters from a shared trunk is determined by whether the domain gap is appearance-level or layout/semantic-level.
- **Problem:** Multi-domain architectures place the shared/specific split by convention (shared encoder, specific decoders); if appearance gaps need early splits and semantic gaps need late splits, a measurable gap-typology would replace convention with design rules.
- **Core Hypothesis (falsifiable):** Across domain pairs typed by an appearance-vs-layout decomposition (per IDEA-B-0249's instruments), the empirically optimal branch depth shifts systematically — early for appearance gaps, late for semantic gaps — and the typology predicts optimal splits for held-out pairs.
- **Why Important:** Provides principled multi-domain architecture design and confirms that domain gaps have identifiable "depths" in representation space.
- **Why Possibly Novel:** Branch-placement studies exist for multi-task learning; the gap-typology-predictive version for multi-domain dense prediction is new.
- **Minimal Experiment:** Sweep branch depths for domain pairs of measured gap types; map optimal depth vs. type; validate predictions prospectively.
- **Main Risk:** Optimal depth may be shallow-basin (many depths near-equal), making the "law" weak even if directionally real.
- **Research Cluster:** CROSS-DOMAIN / REP-MISMATCH

### IDEA-B-0275 — Calibration transfers across domains better than accuracy
- **One-sentence idea:** Test whether post-hoc calibration maps fitted on the source domain remain valid under domain shift even as accuracy collapses — making calibration a more domain-invariant model property than performance.
- **Problem:** Deployments assume everything degrades together under shift; if the confidence-to-correctness mapping is preserved while accuracy falls, systems can still trust their uncertainty even when performance is degraded — a crucial and untested property for graceful degradation.
- **Core Hypothesis (falsifiable):** Source-fitted temperature/calibration maps retain most of their validity (small calibration-error increase relative to accuracy decrease) across moderate domain shifts and model families, with identifiable failure at shifts that alter the error-type composition.
- **Why Important:** Underpins the entire "safe degradation" deployment pattern: act on confidence when accuracy is unknown — validating or demolishing it changes safety architectures.
- **Why Possibly Novel:** Calibration under shift is studied as degradation (IDEA-B-0080); the relative-invariance framing against accuracy, with failure typology, is a different and sharper question.
- **Minimal Experiment:** Fit source calibration for many models; evaluate calibration-vs-accuracy degradation ratios across a shift battery; characterize where the ratio inverts.
- **Main Risk:** Interacts with the accuracy-conditioning subtleties of IDEA-B-0080; metrics must be chosen to avoid mechanical coupling.
- **Research Cluster:** CROSS-DOMAIN / CALIBRATION

### IDEA-B-0276 — What granularity of information does text supervision actually add?
- **One-sentence idea:** Decompose the contribution of caption supervision to segmentation into class-level, attribute-level, and instance-level information via controlled caption ablations.
- **Problem:** Language supervision is credited broadly for open-vocabulary segmentation, but captions may only convey class presence — with spatial extent, instance identity, and attributes contributing nothing — and knowing what text carries determines what still needs visual supervision.
- **Core Hypothesis (falsifiable):** Training with captions reduced to bags of class nouns loses little segmentation-relevant capability relative to full captions, while removing nouns is catastrophic — localizing text's value almost entirely at class-level vocabulary and calibrating expectations for caption-based supervision.
- **Why Important:** Prevents over-attribution to language and quantifies exactly which supervision gaps (extent, instances) must be filled by other signals.
- **Why Possibly Novel:** Caption ablations exist for retrieval; the granularity decomposition targeted at dense-prediction capability is not established.
- **Minimal Experiment:** Pretrain matched models on full/noun-only/noun-free/shuffled captions; probe dense capabilities (semantic, instance, attribute segmentation); attribute capability to caption components.
- **Main Risk:** Caption reduction changes optimization difficulty alongside information content, requiring compute-matched controls.
- **Research Cluster:** MULTIMODAL-SUP

### IDEA-B-0277 — Depth pseudo-labels are boundary-targeted free supervision
- **One-sentence idea:** Test whether auxiliary supervision from monocular-depth pseudo-labels improves segmentation boundaries specifically, because depth discontinuities coincide with object boundaries.
- **Problem:** Auxiliary tasks are chosen by availability rather than mechanism; depth's error-reduction geography (does it help boundaries, interiors, or classes?) has never been mapped, though its edge-aligned structure predicts a specific effect.
- **Core Hypothesis (falsifiable):** Adding depth-prediction auxiliaries improves boundary-F substantially more than interior metrics at matched compute, the gains concentrate on depth-discontinuous boundaries (not texture boundaries), and the effect persists when depth labels come from imperfect monocular estimators.
- **Why Important:** Establishes a free (estimator-generated) supervision stream with a predictable, targeted benefit — and demonstrates mechanism-mapped auxiliary-task selection as a methodology.
- **Why Possibly Novel:** Depth-segmentation multi-task results exist in aggregate; the boundary-specific mechanistic account with discontinuity-stratified evaluation is new.
- **Minimal Experiment:** Train with/without depth auxiliaries; evaluate boundary-stratified metrics split by depth-edge alignment; sweep pseudo-label quality.
- **Main Risk:** Gains may be architecture-dependent (where depth heads attach), requiring several integration points.
- **Research Cluster:** MULTIMODAL-SUP / BOUNDARY

### IDEA-B-0278 — Web caption statistics predict per-class open-vocabulary segmentation quality
- **One-sentence idea:** Test whether a class's naming frequency and naming consistency in web alt-text predicts its open-vocabulary segmentation quality, making performance forecastable from corpus statistics.
- **Problem:** Open-vocab models fail unevenly across classes with no predictive account; if web-language statistics (how often and how consistently people name a thing) explain the variation, per-class reliability can be predicted before deployment (complementing IDEA-B-0128 and IDEA-B-0132).
- **Core Hypothesis (falsifiable):** Per-class open-vocab segmentation quality is jointly predicted by caption frequency and naming-consistency measures with high explanatory power, and residuals identify classes failing for visual (not linguistic) reasons.
- **Why Important:** Provides deployment-readiness forecasting per vocabulary item and separates language-side from vision-side failure causes in multimodal models.
- **Why Possibly Novel:** Concept frequency effects are studied for classification zero-shot; the naming-consistency variable and dense-prediction focus are new.
- **Minimal Experiment:** Estimate both statistics from open caption corpora; regress per-class performance of several open-vocab segmenters; validate predictions on held-out vocabularies.
- **Main Risk:** Corpus statistics are estimated from proxies of the actual (closed) training data, adding noise to the predictor.
- **Research Cluster:** MULTIMODAL-SUP / LONG-TAIL

### IDEA-B-0279 — Does audio add anything beyond motion for video segmentation?
- **One-sentence idea:** Test whether audio-visual segmentation models extract information from sound beyond what visual motion already provides, using silent-video and motion-matched controls.
- **Problem:** Audio-visual models improve sounding-object segmentation, but sounding objects also move; without controls, "audio helps" may just be "motion helps," misdirecting multimodal research investment.
- **Core Hypothesis (falsifiable):** With motion held constant (motion-matched clips with true vs. shuffled vs. silenced audio), genuine audio contribution persists only for specific conditions (off-screen context, ambiguous visual motion), constituting a small identified fraction of the reported aggregate benefit.
- **Why Important:** Correctly prices the value of audio pipelines in video understanding systems and sharpens what cross-modal information genuinely flows.
- **Why Possibly Novel:** Audio-visual benchmarks rarely include motion-matched controls; the decomposition is missing from the literature.
- **Minimal Experiment:** Build motion-matched audio-permutation evaluations on AV segmentation benchmarks; measure per-condition audio contribution across models.
- **Main Risk:** Motion matching is imperfect; residual motion differences could masquerade as audio effects.
- **Research Cluster:** MULTIMODAL-SUP / ASSUMPTION

### IDEA-B-0280 — Auxiliary supervision signals are redundant: the interaction matrix
- **One-sentence idea:** Measure the pairwise and joint contributions of common auxiliary supervision streams (text, depth, edges, surface normals) to segmentation, testing whether their benefits overlap almost completely.
- **Problem:** Papers add auxiliary tasks one at a time against plain baselines, implying additive value; if all auxiliaries inject the same few bits (mostly boundary evidence, per IDEA-B-0277), stacking them wastes compute and the reported individual gains all describe the same underlying improvement.
- **Core Hypothesis (falsifiable):** The auxiliary-task interaction matrix is strongly sub-additive — the best single auxiliary achieves most of the full-stack gain — and the shared component is identifiable as boundary-zone improvement common to all streams.
- **Why Important:** Redirects multi-task design from accumulation to selection, and reveals what the auxiliary-supervision genre has actually been contributing.
- **Why Possibly Novel:** Multi-task interference is studied; the redundancy decomposition of auxiliary supervision for dense prediction with mechanism identification is not.
- **Minimal Experiment:** Train the power set (or fractional design) of 4 auxiliaries on one segmenter; fit interaction terms; decompose shared gains by region type.
- **Main Risk:** Redundancy structure may depend on base-model strength — strong backbones may extract these bits already.
- **Research Cluster:** MULTIMODAL-SUP / NEG-RESULT

### IDEA-B-0281 — Part-level and object-level text supervision conflict
- **One-sentence idea:** Test whether mixing part-level language ("wheel," "sleeve") with object-level language in text-supervised segmentation training degrades object-extent prediction, revealing a granularity conflict in language-aligned features.
- **Problem:** Web captions mention parts and wholes indiscriminately; if the visual-text alignment objective forces one embedding to serve both granularities, extent prediction (choosing where objects end) should suffer in measurable ways nobody has isolated.
- **Core Hypothesis (falsifiable):** Models trained with part-enriched captions show systematic object-extent errors (part-boundary snapping) relative to whole-object-caption controls, and the effect scales with part-mention frequency per class — demonstrating a granularity interference mechanism.
- **Why Important:** Identifies a structural limit of caption supervision for extent-critical tasks and motivates granularity-disambiguated training text.
- **Why Possibly Novel:** Part-whole hierarchies are studied in segmentation; the caption-granularity interference effect on text-supervised models is unexamined.
- **Minimal Experiment:** Construct caption variants with controlled part-mention rates; train matched models; measure extent errors and part-snapping statistics per class.
- **Main Risk:** Constructed captions may differ from natural ones in ways that limit external validity.
- **Research Cluster:** MULTIMODAL-SUP / REP-MISMATCH

### IDEA-B-0282 — VLM attention finds the discriminative part, not the object
- **One-sentence idea:** Quantify the systematic bias of vision-language attention/relevance maps toward discriminative object parts (faces, wheels, text) versus full spatial extents, across model families.
- **Problem:** VLM-derived maps are increasingly used as free pseudo-masks for training segmenters, but contrastive objectives only require discriminative evidence, predicting part-concentrated maps whose bias would propagate into every downstream pseudo-labeled model.
- **Core Hypothesis (falsifiable):** VLM relevance maps cover a small, class-characteristic fraction of GT extents with a consistent part-topology (predictable per class), and segmenters distilled from them inherit measurable extent-shrinkage matching the source bias.
- **Why Important:** The part-bias fingerprint determines how much correction pseudo-mask pipelines need and documents a systematic artifact entering the training-data ecosystem.
- **Why Possibly Novel:** CAM part-bias is known for classifiers; the cross-VLM characterization with inheritance measurement in modern pseudo-labeling pipelines is new.
- **Minimal Experiment:** Score relevance-map coverage against GT extents for several VLMs; train distilled segmenters; measure extent-bias inheritance.
- **Main Risk:** Relevance-map extraction methods vary; results must be shown robust across extraction techniques.
- **Research Cluster:** MULTIMODAL-SUP / EVAL-WEAK

### IDEA-B-0283 — Cross-modal agreement is a free mask-quality signal
- **One-sentence idea:** Validate agreement between independently prompted predictions (text-prompted vs. visual-prompted vs. exemplar-prompted) as a GT-free estimator of mask quality for auto-labeling pipelines.
- **Problem:** Auto-labeling at scale needs quality control without human review; if masks that multiple prompting routes agree on are reliably correct, agreement provides a cheap acceptance filter — but its calibration against true quality is unmeasured.
- **Core Hypothesis (falsifiable):** Cross-prompt agreement rank-correlates strongly with GT mask IoU across datasets, and agreement-filtered pseudo-labels train better downstream models than confidence-filtered ones at matched retention rates.
- **Why Important:** A validated free quality signal changes the economics of dataset generation with promptable models (feeding pipelines like IDEA-B-0151's).
- **Why Possibly Novel:** Ensemble agreement is classical; the cross-modal-prompting version with downstream training validation for segmentation auto-labeling is new.
- **Minimal Experiment:** Generate masks via three prompting routes on labeled data; calibrate agreement against IoU; run the filtered-pseudo-label training comparison.
- **Main Risk:** Prompting routes share the same backbone, so agreement may miss correlated (model-family) errors.
- **Research Cluster:** MULTIMODAL-SUP / UNCERTAINTY

### IDEA-B-0284 — Referring expressions teach relations; class names teach appearance
- **One-sentence idea:** Test whether training on referring-expression supervision transfers different capabilities (relational/spatial reasoning) to plain segmentation than class-name supervision (appearance recognition), using capability-decomposed evaluation.
- **Problem:** Language supervision types are used interchangeably as "text," but grammar-rich referring expressions ("the cup left of the plate") and bare nouns plausibly train different competences — knowing which transfers what would let supervision be composed intentionally.
- **Core Hypothesis (falsifiable):** Referring-trained models outperform class-name-trained ones specifically on relationally ambiguous cases (multiple same-class instances) while matching or trailing on isolated-object appearance cases — a double dissociation stable across architectures.
- **Why Important:** Turns "add language" into a structured design space where supervision grammar is matched to target capability.
- **Why Possibly Novel:** Referring segmentation is its own task; the transfer-decomposition question (what each supervision grammar teaches general segmentation) is unasked.
- **Minimal Experiment:** Train matched models on referring vs. class-name supervision from overlapping image sets; evaluate on relational-ambiguity vs. appearance-only test partitions.
- **Main Risk:** Data volume and diversity differ naturally between supervision types, requiring careful matching.
- **Research Cluster:** MULTIMODAL-SUP

### IDEA-B-0285 — Privileged thermal co-training pays off only where RGB is weak
- **One-sentence idea:** Test whether training-time-only thermal supervision (privileged modality distillation) improves RGB-only inference specifically in low-contrast conditions, mapping where privileged modalities are worth collecting.
- **Problem:** Privileged multimodal training is appealing (extra sensors at training, cheap RGB at deployment), but its value geography — which conditions and classes actually benefit — has never been mapped, leaving collection decisions unguided.
- **Core Hypothesis (falsifiable):** RGB models co-trained with thermal supervision match RGB-only models in good conditions but outperform them substantially on low-light/low-contrast partitions, with per-condition gains predicted by the thermal channel's information advantage in that condition.
- **Why Important:** Provides an evidence-based rule for when to invest in privileged sensor collection, and tests whether cross-modal knowledge genuinely transfers into unimodal inference.
- **Why Possibly Novel:** Privileged distillation exists as a method; the condition-resolved value map with information-advantage prediction is not established.
- **Minimal Experiment:** Co-train RGB models with/without thermal on paired datasets; evaluate on condition-stratified partitions; correlate gains with measured per-condition modality information gaps.
- **Main Risk:** Paired RGB-thermal segmentation data is limited, constraining condition diversity.
- **Research Cluster:** MULTIMODAL-SUP / ROBUSTNESS

### IDEA-B-0286 — Caption noise asymmetry: robust to dropout, fragile to drift
- **One-sentence idea:** Characterize how text-supervised segmentation degrades under different caption-corruption types, testing whether random noise is harmless while systematic naming drift is catastrophic.
- **Problem:** Web captions are noisy in structured ways (regional synonyms, trend-driven renaming, machine-translated text); training robustness to "noise" is claimed generically, but different noise structures plausibly have wildly different effects that data-cleaning policy should reflect.
- **Core Hypothesis (falsifiable):** Random word dropout/swap at high rates barely affects downstream dense performance, while systematic synonym drift (consistent renaming of a class subset) degrades those classes severely at much lower corruption rates — an asymmetry quantifiable as a noise-structure sensitivity profile.
- **Why Important:** Tells caption-cleaning pipelines what to fix (consistency, not typos) and predicts which real-world caption ecosystems produce fragile classes.
- **Why Possibly Novel:** Label-noise structure is studied for classification labels; the caption-noise-structure profile for dense multimodal training is unmeasured.
- **Minimal Experiment:** Pretrain matched models under controlled caption-corruption regimes; evaluate per-class dense transfer; map the sensitivity profile.
- **Main Risk:** Full pretraining sweeps are costly; may require smaller-scale proxies validated at one larger scale.
- **Research Cluster:** MULTIMODAL-SUP / ROBUSTNESS

### IDEA-B-0287 — Geometric supervision improves where, semantic supervision improves what
- **One-sentence idea:** Test whether LiDAR/geometry-derived supervision for 2D segmentation improves localization (boundaries, extents) while leaving classification errors untouched — a supervision-type-to-error-type mapping.
- **Problem:** Multi-sensor supervision is evaluated by aggregate metrics that obscure which error component each signal fixes; a validated mapping would let teams choose sensors by their dominant error type instead of by availability.
- **Core Hypothesis (falsifiable):** Geometry-supervised models improve boundary and extent metrics with no significant change in region-classification confusion, while extra semantic supervision shows the reverse profile — a clean double dissociation across datasets.
- **Why Important:** Establishes a compositional theory of supervision streams, turning sensor-suite design into error-profile engineering.
- **Why Possibly Novel:** LiDAR-camera fusion is studied for inference; the supervision-only error-decomposition mapping is not.
- **Minimal Experiment:** Train 2D segmenters with geometry-derived vs. semantic auxiliary supervision on driving data; decompose error changes into localization vs. classification components.
- **Main Risk:** Projection errors between sensors inject label noise correlated with exactly the boundary regions under study.
- **Research Cluster:** MULTIMODAL-SUP / BOUNDARY

### IDEA-B-0288 — Alignment quality beats data quantity past a threshold
- **One-sentence idea:** Test whether image-text alignment quality (how well captions describe their images) dominates raw pair count for downstream dense-task transfer once volume passes a threshold.
- **Problem:** Multimodal pretraining strategy debates quantity vs. curation with classification-centric evidence; dense tasks may depend more on caption groundedness (spatially relevant descriptions) than on volume, changing what data pipelines should optimize.
- **Core Hypothesis (falsifiable):** At matched compute, corpora filtered for high measured alignment outperform volume-matched unfiltered corpora on dense-task transfer, with the advantage growing for extent- and relation-sensitive evaluations, and the quantity-quality exchange rate is measurable and stable.
- **Why Important:** Provides the dense-prediction-specific answer to the field's central data-strategy question, likely differing from the classification answer.
- **Why Possibly Novel:** Data-filtering studies target zero-shot classification; the dense-task-focused exchange-rate measurement is missing.
- **Minimal Experiment:** Pretrain across a (volume x alignment-quality) grid; evaluate dense transfer; fit the exchange-rate surface.
- **Main Risk:** Alignment filters correlate with content type (simple scenes score higher), confounding quality with difficulty.
- **Research Cluster:** MULTIMODAL-SUP

### IDEA-B-0289 — Language as a calibration interface: hedged prompts, softened masks
- **One-sentence idea:** Test whether uncertainty-expressing language in prompts ("possibly," "partially visible") systematically and usefully modulates open-vocabulary segmentation confidence.
- **Problem:** Deployment systems need runtime control over model conservativeness, currently achieved by threshold engineering; if linguistic hedging maps onto calibrated confidence changes, language becomes a zero-training control interface for the reliability channel.
- **Core Hypothesis (falsifiable):** Hedged prompts produce monotonically softer, measurably better-calibrated masks for genuinely ambiguous cases across open-vocab models, and the hedging-response curve is consistent enough to serve as a documented control knob.
- **Why Important:** A natural-language reliability interface would be operationally valuable and scientifically revealing about how uncertainty concepts are encoded in multimodal training.
- **Why Possibly Novel:** Prompt engineering targets accuracy; the calibration-control mapping of epistemic language for dense prediction is unexplored.
- **Minimal Experiment:** Sweep hedging formulations across models on ambiguity-stratified evaluations; measure confidence-response curves and calibration under each formulation.
- **Main Risk:** Hedging responses may be erratic artifacts of caption statistics rather than usable control surfaces — itself an informative outcome.
- **Research Cluster:** MULTIMODAL-SUP / CALIBRATION

### IDEA-B-0290 — Language supervision helps things and hurts stuff
- **One-sentence idea:** Test whether adding text supervision differentially benefits countable-object classes while degrading amorphous-region (stuff) segmentation, revealing a class-type-conditional value of language.
- **Problem:** Language is noun-centric and object-biased; captions rarely describe pavement extents or vegetation boundaries, so text-aligned features may trade stuff-relevant texture representation for object semantics — an unexamined cost of the open-vocabulary transition.
- **Core Hypothesis (falsifiable):** At matched training, text-supervised models beat vision-only counterparts on thing classes but underperform on stuff classes (especially their boundary placement), with the per-class effect predicted by caption-mention statistics.
- **Why Important:** Warns that the field's language-alignment shift may be silently regressing half the label space, and motivates hybrid supervision for stuff.
- **Why Possibly Novel:** Thing/stuff analyses and language supervision are separate threads; their interaction as a systematic cost-benefit structure is unmeasured.
- **Minimal Experiment:** Compare matched text-supervised and vision-only models per class type; regress per-class deltas on caption statistics; test stuff-targeted supervision repair.
- **Main Risk:** Thing/stuff differences confound with class difficulty; needs baseline-normalized effect measures.
- **Research Cluster:** MULTIMODAL-SUP / REP-MISMATCH

### IDEA-B-0291 — Spatial-preposition grounding is the weak link in referring segmentation
- **One-sentence idea:** Build a controlled diagnostic isolating spatial-relation understanding (left/right/behind/between) and test whether it predicts real-world referring-segmentation failures better than aggregate benchmark scores.
- **Problem:** Referring benchmarks entangle appearance, salience, and relations; models can score well while resolving relations by dataset priors (the referred object is usually the salient one), leaving true spatial grounding unmeasured and deployments surprised.
- **Core Hypothesis (falsifiable):** On salience-controlled minimal-pair diagnostics (identical scenes, relation-only differences), leading referring models perform near chance on several relation types, and diagnostic scores predict per-instance failures on natural data better than benchmark aggregates.
- **Why Important:** Human-robot interaction and assistive systems rely precisely on relational language; a validated diagnostic exposes and tracks a safety-relevant capability gap.
- **Why Possibly Novel:** Spatial-reasoning probes exist for VQA; the salience-controlled minimal-pair methodology with predictive validation for dense referring is new.
- **Minimal Experiment:** Construct minimal-pair scenes (rendered and curated real); evaluate leading models per relation type; correlate diagnostic scores with natural-data error analysis.
- **Main Risk:** Rendered diagnostics may underestimate models that exploit natural co-occurrence cues legitimately.
- **Research Cluster:** MULTIMODAL-SUP / EVAL-WEAK

### IDEA-B-0292 — 3D consistency is an annotation multiplier
- **One-sentence idea:** Quantify how much 2D annotation multi-view geometric consistency saves — labeling one view and propagating through 3D structure — as a function of scene rigidity and view coverage.
- **Problem:** Teams with multi-view capture rigs still annotate views independently; geometry makes most of that redundant, but the multiplier's size and its failure conditions (dynamic objects, occlusion) have not been measured for modern pipelines.
- **Core Hypothesis (falsifiable):** Geometry-propagated labels from a fraction of views train models equivalent to full multi-view annotation, with the achievable multiplier predicted by scene rigidity statistics and view overlap — yielding a planning formula for capture-rig annotation budgets.
- **Why Important:** Direct, large cost savings for any multi-camera dataset effort (driving, robotics, AR), with a principled applicability rule.
- **Why Possibly Novel:** Label propagation via geometry is used ad hoc; the multiplier quantification with a validated planning formula is not published.
- **Minimal Experiment:** On multi-view datasets, train on propagated-from-k-views labels across k; measure quality-vs-multiplier curves; validate the rigidity/overlap predictor.
- **Main Risk:** Propagation errors concentrate at occlusion boundaries — exactly the high-value label regions.
- **Research Cluster:** MULTIMODAL-SUP / ANNOT-EFF

### IDEA-B-0293 — Narration timing localizes objects: speech as temporal supervision
- **One-sentence idea:** Measure the dense-supervision information content of narration timestamps in instructional video (when a thing is named, it tends to be visible and often manipulated) and test its value for training segmenters without masks.
- **Problem:** Instructional video with aligned speech is abundant and free, but its use for dense tasks is limited to representation pretraining; the explicit temporal-naming signal ("now take the whisk") may support direct localization supervision whose strength nobody has quantified.
- **Core Hypothesis (falsifiable):** Narration-timing-based pseudo-supervision (name-time windows crossed with visual saliency and hand proximity) trains segmenters that reach a meaningful fraction of weakly supervised baselines' performance with zero image-level annotation, and the signal strength is predictable from narration style statistics.
- **Why Important:** Opens a genuinely free supervision stream at internet scale for vocabulary far beyond curated datasets.
- **Why Possibly Novel:** Narrated-video pretraining exists for representations; extracting and quantifying explicit localization supervision from timing structure for segmentation is largely unexplored.
- **Minimal Experiment:** Build the timing-based pseudo-label pipeline on narrated-video corpora; train segmenters; benchmark against weakly supervised baselines; analyze signal strength by narration style.
- **Main Risk:** Timing-visibility correlation varies enormously across video genres, potentially limiting the method to instructional niches.
- **Research Cluster:** MULTIMODAL-SUP

### IDEA-B-0294 — Masking the image, not the text, teaches localization
- **One-sentence idea:** Test whether masked-image objectives contribute more to downstream localization ability than masked-text objectives in multimodal pretraining, isolating which modality's reconstruction builds spatial competence.
- **Problem:** Multimodal pretraining stacks masking objectives on both modalities by default; if spatial competence for dense tasks comes almost entirely from image-side masking, text-side compute can be reallocated and the mechanism of emergent localization becomes clearer.
- **Core Hypothesis (falsifiable):** At matched compute, varying image-masking while holding text-masking fixed changes downstream segmentation transfer substantially, while the converse manipulation changes it little — an asymmetry consistent across masking ratios.
- **Why Important:** Optimizes a major compute allocation in multimodal pretraining and localizes the origin of spatial ability in these models.
- **Why Possibly Novel:** Masking-ratio ablations exist per modality in isolation; the cross-modality attribution for dense-task competence is missing.
- **Minimal Experiment:** Pretrain a factorial grid over (image-mask ratio x text-mask ratio) at modest scale; evaluate dense transfer; test the asymmetry at one larger scale.
- **Main Risk:** Asymmetry may reverse at scales beyond experimental reach, bounding the claim's applicability.
- **Research Cluster:** MULTIMODAL-SUP / REP-MISMATCH

### IDEA-B-0295 — Emergent localization in contrastive VLMs is a negative-sampling effect
- **One-sentence idea:** Test whether the emergent segmentation ability of contrastive vision-language models is driven by effective negative-sample count (batch size) rather than data volume or model scale.
- **Problem:** Emergent localization in CLIP-style models is attributed vaguely to scale; contrastive theory suggests hard negatives force spatially discriminative features, predicting batch size as the causal lever — a testable, mechanism-level alternative.
- **Core Hypothesis (falsifiable):** At matched data, compute, and model size, increasing contrastive batch size (or negative-sampling sophistication) improves downstream zero-shot localization steeply, while equivalent-compute data-volume increases at small batches do not — establishing negatives as the operative variable.
- **Why Important:** Identifies the training lever that buys spatial competence, informing cheaper recipes for localization-capable multimodal models.
- **Why Possibly Novel:** Batch-size effects on retrieval metrics are known; the localization-emergence attribution with controlled disentanglement is new.
- **Minimal Experiment:** Pretrain matched models across batch-size and data-volume grids (with gradient-accumulation controls separating optimization from negative-count effects); evaluate zero-shot dense capabilities.
- **Main Risk:** Batch size entangles with optimization dynamics; accumulation controls are essential and delicate.
- **Research Cluster:** MULTIMODAL-SUP / PHENOMENON

### IDEA-B-0296 — Pretraining teaches invariance; segmentation needs equivariance
- **One-sentence idea:** Measure the invariance-vs-equivariance profile of pretrained representations across layers and test whether the mismatch with dense-task requirements predicts fine-tuning cost and final quality.
- **Problem:** Classification pretraining explicitly rewards translation/augmentation invariance, while dense prediction requires spatially equivariant features; the size of this structural mismatch, where it lives in the network, and how much fine-tuning spends undoing it are all unmeasured.
- **Core Hypothesis (falsifiable):** Pretrained networks show increasing invariance with depth that fine-tuning partially reverses (measurable as equivariance recovery), and pretraining objectives that preserve equivariance (dense SSL) show proportionally cheaper fine-tuning and better boundary metrics — with the invariance profile predicting transfer quality across objectives.
- **Why Important:** Provides a mechanistic, measurable account of why some pretrainings transfer better to dense tasks, replacing leaderboard empiricism with a predictive quantity.
- **Why Possibly Novel:** Invariance measurement exists descriptively; connecting the profile causally to fine-tuning dynamics and dense-task outcomes is new.
- **Minimal Experiment:** Measure layer-wise equivariance for diverse pretrained models; track its evolution during fine-tuning; regress transfer outcomes on initial profiles.
- **Main Risk:** Equivariance metrics are definition-sensitive; several formulations must agree for robustness.
- **Research Cluster:** REP-MISMATCH

### IDEA-B-0297 — How many boundary bits does patch tokenization destroy?
- **One-sentence idea:** Quantify the boundary-localization information lost at ViT patch embedding (16x16 aggregation) and test whether it is recoverable downstream or permanently absent.
- **Problem:** Sub-patch boundary detail must survive tokenization through incidental encoding if at all; whether ViT segmenters' boundary limits are a tokenization information bottleneck or a decoding deficiency determines where boundary research effort should go.
- **Core Hypothesis (falsifiable):** Probes trained to recover sub-patch edge position from single patch embeddings show substantial but incomplete information retention that degrades with patch size in a predictable way, and models' actual boundary errors track the probe-measured information floor — implying decoding is near-optimal and the bottleneck is tokenization itself.
- **Why Important:** Locates the binding constraint on transformer boundary quality with an information measurement rather than architecture trial-and-error.
- **Why Possibly Novel:** Patch-size ablations report metrics; the information-theoretic accounting connecting embedding-recoverable detail to realized boundary error is new.
- **Minimal Experiment:** Train sub-patch edge-position probes on frozen embeddings across patch sizes; compare probe floors against fine-tuned segmenters' boundary error distributions.
- **Main Risk:** Probes lower-bound information only; a stronger decoder could exceed probe estimates, weakening the floor claim.
- **Research Cluster:** REP-MISMATCH / BOUNDARY

### IDEA-B-0298 — Global pooling in pretraining causes irreversible spatial damage
- **One-sentence idea:** Test whether pretraining through global-average-pooled objectives permanently degrades the spatial quality of features in ways downstream fine-tuning cannot repair.
- **Problem:** Most classification pretraining funnels all supervision through pooled global vectors, allowing spatial scrambling that costs nothing in pretraining; whether fine-tuning can undo the scrambling or whether the damage persists — arguing for dense-objective pretraining — is a foundational open question.
- **Core Hypothesis (falsifiable):** Matched pretrainings differing only in pooling structure (global vs. dense/attentive supervision paths) converge to different dense-task ceilings even under unlimited fine-tuning, with the pooled models' deficit concentrated in spatial-precision metrics — demonstrating irreversibility.
- **Why Important:** If pooling damage is permanent, the field's reliance on classification-pretrained backbones has a hard ceiling that only new pretraining objectives escape.
- **Why Possibly Novel:** Dense-SSL papers compare methods holistically; the isolated pooling-pathway manipulation with irreversibility testing (long-fine-tuning asymptotics) is not done.
- **Minimal Experiment:** Pretrain matched models with pooled vs. spatially supervised objectives on identical data; fine-tune to convergence plateaus on dense tasks; compare asymptotes and spatial metric profiles.
- **Main Risk:** "Unlimited fine-tuning" is finite in practice; asymptote estimation requires careful convergence evidence.
- **Research Cluster:** REP-MISMATCH

### IDEA-B-0299 — Instance discrimination fights instance segmentation
- **One-sentence idea:** Test whether contrastive instance-discrimination pretraining, by pulling same-class instances together, degrades the instance-separability of features that instance segmentation needs.
- **Problem:** SSL objectives that treat augmented views as positives and other images as negatives implicitly cluster same-class objects; instance segmentation needs the opposite (same-class neighbors distinguishable), suggesting a task-objective conflict hidden inside the "SSL transfers well" narrative.
- **Core Hypothesis (falsifiable):** Features from instance-discrimination SSL show measurably lower same-class instance separability (probe-based) than reconstruction-based SSL at matched semantic quality, and the separability measure predicts instance-segmentation transfer differences between SSL families.
- **Why Important:** Explains structured differences among SSL methods for dense tasks and provides a probe-based selection criterion aligned to instance-level applications.
- **Why Possibly Novel:** SSL comparisons report task metrics; the instance-separability mechanism with predictive validation across SSL families is unexamined.
- **Minimal Experiment:** Build same-class instance-pair separability probes; evaluate across SSL checkpoints; correlate with instance-segmentation fine-tuning outcomes.
- **Main Risk:** Separability differences may wash out during fine-tuning, making the probe predictive of speed but not final quality.
- **Research Cluster:** REP-MISMATCH

### IDEA-B-0300 — High-res features are semantically starved, not structurally incapable
- **One-sentence idea:** Test whether the low semantic level of high-resolution feature maps is an optimization artifact (gradient starvation through deep paths) rather than an architectural necessity, using gradient-rebalancing interventions.
- **Problem:** The "resolution-semantics tradeoff" is treated as architectural law — early high-res layers carry low-level features — but supervision reaches them through long gradient paths dominated by deeper layers; if targeted gradient delivery makes high-res features semantic, the tradeoff is a training accident, not a constraint.
- **Core Hypothesis (falsifiable):** Auxiliary supervision or gradient-scaling delivered directly to high-resolution branches increases their measured semantic content (probe accuracy) substantially and improves boundary-adjacent classification, without architecture changes — falsifying the necessity claim.
- **Why Important:** Would dissolve a foundational assumption behind decoder design (the entire fuse-deep-into-shallow paradigm) and open training-side routes to detailed semantic features.
- **Why Possibly Novel:** Deep supervision exists as a trick; framing and testing it as a falsification of the resolution-semantics tradeoff with probe-based mechanistic evidence is a different scientific target.
- **Minimal Experiment:** Train matched models with standard vs. high-res-targeted supervision; probe per-layer semantic content; evaluate boundary-zone classification accuracy.
- **Main Risk:** Gains may plateau quickly, showing the tradeoff is partially optimization-driven but still substantially architectural.
- **Research Cluster:** REP-MISMATCH / PHENOMENON

### IDEA-B-0301 — Text embedding geometry is taxonomic; visual geometry is appearance-based
- **One-sentence idea:** Measure the structural mismatch between language-embedding similarity (taxonomy-driven) and visual-feature similarity (appearance-driven) and test whether open-vocabulary segmentation errors follow the language geometry rather than the visual one.
- **Problem:** Open-vocab segmenters classify pixels by matching visual features to text embeddings; the two spaces organize concepts differently (a dolphin is taxonomically a mammal but visually a fish), predicting a specific, diagnosable error structure nobody has characterized.
- **Core Hypothesis (falsifiable):** Confusion matrices of open-vocab segmenters are predicted significantly better by text-embedding proximity than by visual-feature proximity of the confused classes, and the effect strengthens with more language-dominant training — establishing that errors are imported from language geometry.
- **Why Important:** Identifies the failure signature of an entire model class, enabling targeted fixes (visual-geometry-corrected matching) and error prediction for unseen vocabularies.
- **Why Possibly Novel:** Modality-gap geometry is studied abstractly; its causal imprint on dense-prediction confusion structure is unexamined.
- **Minimal Experiment:** Compute both proximity structures for benchmark vocabularies; regress observed confusions on each; compare across models with varying language-supervision strength.
- **Main Risk:** Text and visual proximities correlate for many classes, requiring careful analysis on the disagreement subset.
- **Research Cluster:** REP-MISMATCH / MULTIMODAL-SUP

### IDEA-B-0302 — Padding-derived position information is a shortcut with an OOD bill
- **One-sentence idea:** Quantify how much segmentation models rely on absolute position (learned via padding artifacts and positional encodings) and measure the out-of-distribution cost when scene layouts shift.
- **Problem:** Networks encode absolute position through boundary effects, and dense models plausibly exploit it (sky is up, road is down); this helps on layout-conventional benchmarks but must fail on unconventional framings — a reliance-cost tradeoff never jointly measured.
- **Core Hypothesis (falsifiable):** Position-reliance probes reveal substantial absolute-position usage in trained segmenters, position-scrambling interventions (crop-shift training, padding changes) reduce reliance with small in-distribution cost, and reduced-reliance models are measurably more robust on rotated/cropped/unconventional-framing evaluations.
- **Why Important:** Reveals a shortcut with a controllable dial, letting deployments choose their point on the layout-prior vs. framing-robustness curve.
- **Why Possibly Novel:** Padding position-encoding is documented; the dense-prediction reliance quantification with the joint cost-benefit curve is not.
- **Minimal Experiment:** Probe position decodability across models; train reliance-reduced variants; evaluate on framing-shifted and rotation test suites against standard benchmarks.
- **Main Risk:** Some position reliance is task-legitimate (gravity priors); the analysis must separate legitimate from shortcut usage.
- **Research Cluster:** REP-MISMATCH / ROBUSTNESS

### IDEA-B-0303 — Equal mIoU, different error anatomy: pixel losses are structure-blind
- **One-sentence idea:** Characterize how models with identical aggregate scores differ in error structure (coherent region shifts vs. scattered speckle vs. boundary erosion) and build a structure-aware evaluation that downstream utility validates.
- **Problem:** Pixelwise losses and metrics are invariant to the spatial arrangement of errors, but downstream consumers are not (a coherent misplaced region is one wrong decision; speckle is noise); the field cannot currently see — let alone optimize — the difference.
- **Core Hypothesis (falsifiable):** Public models matched within 1 mIoU differ severalfold on error-structure statistics (component size distributions, boundary-alignment of errors), and structure metrics predict downstream task outcomes (from IDEA-B-0064's harness) far better than mIoU differences do.
- **Why Important:** Introduces a missing dimension into evaluation that reorders model choices for real applications and creates a target for structure-aware training.
- **Why Possibly Novel:** Error-structure analysis exists in medical imaging niches; the general framework with downstream-utility validation for mainstream benchmarks is not established.
- **Minimal Experiment:** Compute error-structure profiles for 20 matched-mIoU model pairs; run downstream utility evaluations; quantify each metric family's predictive power.
- **Main Risk:** Structure metrics are many; without pre-registration the analysis risks metric-fishing criticism.
- **Research Cluster:** REP-MISMATCH / EVAL-WEAK

### IDEA-B-0304 — Mutually exclusive labels break on transparent and reflective matter
- **One-sentence idea:** Quantify how the softmax single-label-per-pixel assumption fails on transparent, reflective, and translucent surfaces, and test whether multi-layer (foreground-plus-background) output formulations fix the measured failure without hurting opaque classes.
- **Problem:** A pixel viewing water, glass, or a reflection legitimately belongs to two surfaces at once; exclusive labeling forces models into systematic, physically wrong predictions on such matter — a representational mismatch whose cost is folded invisibly into per-class scores.
- **Core Hypothesis (falsifiable):** Error rates on transparency/reflection-affected pixels are severalfold higher than matched opaque pixels across all softmax models, the errors show a characteristic bistability (flipping between the two surfaces), and two-layer output models eliminate the bistability while matching single-layer models elsewhere.
- **Why Important:** Transparent matter is ubiquitous (windows, water, glass doors) and safety-relevant (robots walk into glass); establishing the representational cause enables a principled fix.
- **Why Possibly Novel:** Transparent-object segmentation is a niche task; framing exclusivity as the measured root cause with layered-output falsification is a different, general contribution.
- **Minimal Experiment:** Build a transparency-annotated evaluation overlay for existing benchmarks; profile errors and flip statistics; train layered-output variants and compare.
- **Main Risk:** Layered GT for training/evaluation is expensive to produce at scale.
- **Research Cluster:** REP-MISMATCH

### IDEA-B-0305 — Mean-vector object queries predictably fail on elongated and multi-part objects
- **One-sentence idea:** Test whether query-based segmenters' representation of each object as a single feature vector causes predictable failures on objects whose parts are visually heterogeneous or spatially extended.
- **Problem:** Query decoders compress an object into one embedding whose dot products generate the mask; geometry says heterogeneous objects (a mop: handle + head; a train spanning the image) fit a single prototype poorly, predicting a specific class-conditional failure set nobody has verified.
- **Core Hypothesis (falsifiable):** Per-class mask quality of query-based models (relative to per-pixel baselines) decreases with measured intra-object feature heterogeneity, mask errors concentrate on the parts most distant from the object's feature mean, and multi-vector query variants close precisely those gaps.
- **Why Important:** Converts an architectural limitation from anecdote to predictive theory, guiding when query architectures are the wrong choice.
- **Why Possibly Novel:** Query architectures are compared by aggregate metrics; the heterogeneity-based failure geometry with within-object error localization is unexamined.
- **Minimal Experiment:** Compute intra-object heterogeneity per class; regress query-vs-pixel model gaps on it; map within-object error positions against feature-mean distance.
- **Main Risk:** Modern multi-scale query refinements may already mitigate the effect, requiring version-resolved analysis.
- **Research Cluster:** REP-MISMATCH

### IDEA-B-0306 — The semantic-depth profile predicts dense-task transfer
- **One-sentence idea:** Characterize at what depth each pretrained backbone's features become semantic (class-predictive) versus textural, and test whether this profile predicts dense-prediction transfer better than headline benchmark scores.
- **Problem:** Backbone selection for segmentation uses classification accuracy as the proxy, but dense decoding needs semantics at high resolution; two equal-accuracy backbones can distribute semantics across depth very differently, plausibly explaining unexplained transfer differences.
- **Core Hypothesis (falsifiable):** A "semantic depth" profile (probe accuracy vs. layer/resolution) varies substantially among equal-accuracy backbones and predicts segmentation fine-tuning outcomes (especially boundary and small-object metrics) better than ImageNet accuracy across a model zoo.
- **Why Important:** Replaces a misleading selection proxy with a mechanistic one, cheaply computable from frozen features before committing to fine-tuning.
- **Why Possibly Novel:** Layer-wise probing exists descriptively; its validation as a transfer predictor superior to standard proxies for dense tasks is missing.
- **Minimal Experiment:** Profile 15+ backbones; fine-tune all on two segmentation tasks; compare predictive power of profiles vs. classification accuracy.
- **Main Risk:** Profiles and accuracy correlate across the zoo; the predictive comparison needs models where they dissociate.
- **Research Cluster:** REP-MISMATCH / CROSS-DOMAIN

### IDEA-B-0307 — Discrete classes misrepresent continuous scene matter
- **One-sentence idea:** Measure the information and accuracy cost of forcing continuous scene properties (material transitions, vegetation density, wetness) through discrete class outputs, using datasets with continuous attribute GT.
- **Problem:** Scenes contain continua (dry-to-wet road, grass-to-dirt transitions) that discrete ontologies chop arbitrarily; models waste capacity fighting over arbitrary bin boundaries and downstream consumers lose the gradation entirely — a representational mismatch whose size is unmeasured.
- **Core Hypothesis (falsifiable):** In regions of genuine continuity (identified via continuous auxiliary GT), discrete models show inflated disagreement across seeds and elevated confidence oscillation, and hybrid discrete-plus-continuous output heads improve both stability and downstream regression tasks at no cost elsewhere.
- **Why Important:** Diagnoses a mismatch between world structure and output format affecting every ontology-based system, with a testable remedy.
- **Why Possibly Novel:** Continuous segmentation exists in niches (matting, depth); the systematic cost measurement of discretization on standard semantic tasks is new.
- **Minimal Experiment:** Overlay continuous-attribute GT on benchmark subsets; measure discrete-model instability in continuum zones; evaluate hybrid heads.
- **Main Risk:** Continuum-zone identification itself requires judgment; needs multiple independent operationalizations.
- **Research Cluster:** REP-MISMATCH

### IDEA-B-0308 — Reconstruction pretraining hoards nuisance information
- **One-sentence idea:** Test whether masked-autoencoder features, optimized to reconstruct pixels, retain nuisance information (illumination, camera characteristics) that measurably harms robustness relative to discriminative SSL at matched accuracy.
- **Problem:** Reconstruction objectives require keeping everything about appearance, including factors dense tasks should ignore; whether this nuisance retention has a robustness cost — and whether it explains SSL-family robustness differences — is untested.
- **Core Hypothesis (falsifiable):** Nuisance-information probes (illuminant, ISP, JPEG-level decoders) extract substantially more from reconstruction-based than contrastive features, and the per-model nuisance retention predicts corruption-robustness differences after fine-tuning at matched clean accuracy.
- **Why Important:** Provides a mechanistic selection criterion among SSL families for robustness-critical deployments and sharpens theory about what pretraining objectives make features keep.
- **Why Possibly Novel:** SSL comparisons are outcome-based; the nuisance-retention mechanism with predictive validation is unexplored.
- **Minimal Experiment:** Train nuisance probes on frozen features of diverse SSL checkpoints; fine-tune all for segmentation; correlate retention measures with robustness outcomes.
- **Main Risk:** Fine-tuning may discard nuisance content, decoupling frozen-feature measurements from final behavior.
- **Research Cluster:** REP-MISMATCH / ROBUSTNESS

### IDEA-B-0309 — Things need slots, stuff needs fields: a representational dichotomy
- **One-sentence idea:** Test whether object-centric (slot) and dense (field) representations have complementary, class-type-locked strengths — slots failing structurally on amorphous stuff, fields failing on countable instance separation — implying hybrid necessity.
- **Problem:** Slot-based and dense paradigms compete as universal answers; if each is structurally matched to one half of the thing/stuff dichotomy, the competition is misframed and hybrid designs are not engineering conveniences but representational necessities.
- **Core Hypothesis (falsifiable):** At matched capacity, slot models beat dense models on instance-separation metrics but show irreducible deficits on stuff boundary/extent quality (and vice versa), with each deficit robust to scaling within paradigm — demonstrating structural rather than capacity limitation.
- **Why Important:** Settles a paradigm debate with a structural result and grounds hybrid architecture design in measured necessity.
- **Why Possibly Novel:** Slot models are evaluated on object-centric benchmarks; the systematic thing/stuff dichotomy test with scaling controls is not done.
- **Minimal Experiment:** Train matched slot/dense/hybrid models across capacities on panoptic tasks; profile per-class-type metrics; test deficit persistence under scaling.
- **Main Risk:** Slot methods evolve fast; conclusions need framing around representational structure, not specific implementations.
- **Research Cluster:** REP-MISMATCH

### IDEA-B-0310 — Feature-space neighbors straddle boundaries: the metric-geometry defect
- **One-sentence idea:** Measure how often adjacent pixels across a true object boundary are closer in feature space than same-object pixels farther apart, and test whether this metric defect predicts boundary errors.
- **Problem:** Dense heads implicitly assume feature distance tracks semantic grouping, but local appearance continuity across boundaries (shadow, contact regions) can invert the geometry; the prevalence of such inversions and their causal link to boundary failure are unmeasured.
- **Core Hypothesis (falsifiable):** Metric inversions (cross-boundary similarity exceeding within-object similarity) occur at a substantial rate concentrated at low-contrast boundaries, their local density predicts per-pixel boundary error across models, and representation-shaping objectives that reduce inversions improve boundary metrics proportionally.
- **Why Important:** Provides a feature-level causal account of boundary failure with a measurable intermediate quantity that training can target.
- **Why Possibly Novel:** Contrastive boundary losses exist as methods; the defect measurement, its predictive validation, and the proportionality test constitute a mechanism study the literature lacks.
- **Minimal Experiment:** Compute inversion statistics on frozen features of many models; correlate with boundary errors; run the intervention arm with inversion-targeted objectives.
- **Main Risk:** Inversions may be a symptom (of insufficient training) rather than a cause, requiring the intervention arm to carry the causal weight.
- **Research Cluster:** REP-MISMATCH / BOUNDARY

### IDEA-B-0311 — Positional-embedding interpolation fails at predictable image locations
- **One-sentence idea:** Test whether accuracy degradation when running ViT segmenters above training resolution concentrates at spatial positions where positional-embedding interpolation error is largest, enabling location-targeted fixes.
- **Problem:** Resolution transfer via positional-embedding interpolation is standard, and its aggregate cost is known to be modest — but if the cost is spatially structured (grid-artifact locations), aggregate reporting hides localized failure stripes that matter for dense prediction.
- **Core Hypothesis (falsifiable):** Per-position error increase under resolution transfer correlates with a computable interpolation-error map of the positional embeddings, producing periodic spatial artifacts in prediction quality that alternative extrapolation schemes remove.
- **Why Important:** Converts a diffuse "resolution transfer hurts a bit" into a located, fixable phenomenon relevant to every high-resolution ViT deployment.
- **Why Possibly Novel:** Resolution adaptation tricks exist; the spatial-failure-map analysis tying errors to embedding interpolation structure is new.
- **Minimal Experiment:** Evaluate ViT segmenters across resolutions; map per-position error deltas; correlate with interpolation-error predictions; test alternative schemes.
- **Main Risk:** Content-position correlations in benchmarks could mimic or mask periodic artifacts; needs shifted-crop controls.
- **Research Cluster:** REP-MISMATCH

### IDEA-B-0312 — Segmentation ability occupies a low-dimensional weight subspace
- **One-sentence idea:** Test whether the weight-space difference that converts a pretrained backbone into a segmenter is low-rank and transplantable across fine-tunes, implying dense-task competence is a compact, portable weight-space direction.
- **Problem:** Every downstream user re-learns segmentation ability from scratch during fine-tuning; if the acquired ability is a low-dimensional weight delta approximately shared across datasets, it could be extracted once and reused, and its structure would illuminate what fine-tuning changes.
- **Core Hypothesis (falsifiable):** Task vectors from independent segmentation fine-tunes of one backbone share high subspace overlap, their low-rank approximations retain most performance, and applying an averaged segmentation vector to the raw backbone yields substantial zero-shot dense capability on unseen datasets.
- **Why Important:** Portable task directions would change fine-tuning economics and provide a concrete handle on the geometry of task knowledge in weight space.
- **Why Possibly Novel:** Task arithmetic is studied for classification abilities; the rank structure and cross-dataset portability analysis for dense prediction is new.
- **Minimal Experiment:** Fine-tune one backbone on several segmentation datasets; analyze task-vector subspace overlap and rank; test transplantation to held-out datasets.
- **Main Risk:** Head/decoder parameters may carry most of the ability, trivializing the backbone-vector analysis; requires decoder-controlled designs.
- **Research Cluster:** REP-MISMATCH / PHENOMENON

### IDEA-B-0313 — Soft-label similarity helps only if it is visually derived
- **One-sentence idea:** Test whether class-similarity-informed soft targets improve segmentation when the similarity comes from visual co-confusability but hurt (or do nothing) when it comes from semantic taxonomies.
- **Problem:** Soft-label and hierarchy-aware training import class-similarity structure from convenient sources (WordNet, embeddings) assuming any structure beats one-hot; but the model's errors live in visual space, and taxonomy-derived similarity may teach precisely the wrong confusions (per IDEA-B-0301's geometry mismatch).
- **Core Hypothesis (falsifiable):** Soft targets built from measured visual confusability improve rare-class and boundary-region accuracy, while targets built from taxonomic similarity yield no improvement or measurable harm on visually distinct taxonomic neighbors — a source-dependence that falsifies the generic soft-label recommendation.
- **Why Important:** Sharpens a common training practice with a causal account of when auxiliary similarity structure helps, unifying with the language-geometry findings.
- **Why Possibly Novel:** Soft-label methods rarely control the similarity source as the experimental variable.
- **Minimal Experiment:** Construct matched soft-target variants (visual-derived, taxonomy-derived, random-structured); train matched models; compare per-class effects against the source structures.
- **Main Risk:** Visual confusability must be estimated from a reference model, risking circularity that the design must break with held-out estimation.
- **Research Cluster:** REP-MISMATCH

### IDEA-B-0314 — Static-frame features misplace motion boundaries
- **One-sentence idea:** Test whether video segmentation errors at motion boundaries stem from representations optimized on static frames, by measuring whether motion-boundary error persists when appearance evidence is strong.
- **Problem:** Video models built on image backbones inherit representations that never needed to encode motion discontinuities; errors at motion boundaries are attributed to temporal fusion design, but the deficit may live in the frame representation itself — a different fix location.
- **Core Hypothesis (falsifiable):** Motion-boundary errors remain elevated even where static appearance evidence is strong (high contrast), implicating representation rather than evidence; and brief motion-aware representation training (optical-flow-aligned objectives) reduces the residual more than equivalent temporal-fusion capacity additions.
- **Why Important:** Locates the binding constraint for a persistent video-segmentation failure mode, redirecting architecture effort toward representation training.
- **Why Possibly Novel:** Temporal architectures are compared extensively; the representation-vs-fusion attribution for motion-boundary error is not isolated.
- **Minimal Experiment:** Stratify video segmentation errors by motion-boundary presence and appearance evidence strength; run the matched intervention comparison (representation training vs. fusion capacity).
- **Main Risk:** Motion boundaries co-occur with blur and occlusion, requiring careful evidence-strength controls.
- **Research Cluster:** REP-MISMATCH / BOUNDARY

### IDEA-B-0315 — Skips carry boundaries, bottlenecks carry classes: an information map
- **One-sentence idea:** Quantify with mutual-information probes what each encoder-decoder pathway (skip connections vs. bottleneck) actually transmits, testing the folk theory that skips carry spatial detail and bottlenecks carry semantics.
- **Problem:** U-Net-style design rests on an untested information story; a validated pathway-information map would predict which architecture modifications matter for which error types and expose redundancy (pathways carrying duplicated information) that efficiency work could exploit.
- **Core Hypothesis (falsifiable):** Pathway-resolved probes show strong specialization (boundary position decodable from skips but not bottleneck; class identity the reverse), pathway-ablation error profiles match the information map's predictions, and pathways with high measured redundancy can be pruned at predicted (small) cost.
- **Why Important:** Converts encoder-decoder design folklore into measured information routing, enabling prediction-driven architecture editing instead of ablation roulette.
- **Why Possibly Novel:** Skip ablations exist; the quantitative information mapping with predictive validation of ablation outcomes is a different level of analysis.
- **Minimal Experiment:** Train probes on pathway activations of several encoder-decoder segmenters; build the information map; validate against systematic pathway-ablation error profiles.
- **Main Risk:** MI estimation on high-dimensional activations is approximate; needs multiple estimators and probe families to be credible.
- **Research Cluster:** REP-MISMATCH / PHENOMENON

### IDEA-B-0316 — Decompose mIoU or keep misranking models
- **One-sentence idea:** Establish decomposed reporting (classification error vs. localization error vs. boundary error components) by showing that models tied on mIoU differ dramatically in composition, with different components predicting different downstream uses.
- **Problem:** A single overlap score aggregates failures with entirely different downstream consequences and remedies; methods get selected on totals while their error composition — which determines real-world fit — remains invisible.
- **Core Hypothesis (falsifiable):** Across public model pairs within 1 mIoU of each other, decomposition reveals component differences exceeding 20% relative magnitude in a majority of pairs, and component profiles predict which model wins on component-sensitive downstream tasks.
- **Why Important:** A low-cost reporting change that re-informs every model comparison in the field, grounded in demonstrated ranking consequences.
- **Why Possibly Novel:** Detection has TIDE-style decomposition; a standardized, validated equivalent driving segmentation reporting practice does not exist.
- **Minimal Experiment:** Implement the decomposition; profile 30 public checkpoints; run component-sensitive downstream validations; publish the tool and profiles.
- **Main Risk:** Decomposition definitions involve choices (what counts as localization vs. classification error at boundaries) that need consensus-building.
- **Research Cluster:** EVAL-WEAK

### IDEA-B-0317 — Benchmarks lack the statistical power for the claims made on them
- **One-sentence idea:** Perform formal power analyses of popular segmentation benchmarks to determine the minimum detectable effect sizes and compare them against the distribution of claimed improvements in the literature.
- **Problem:** Test-set sizes were chosen by convenience, not statistics; if the minimum detectable mIoU difference at reasonable confidence exceeds typical claimed gains, a large fraction of published comparisons are statistically uninterpretable — a field-level problem no individual paper can see.
- **Core Hypothesis (falsifiable):** For several major benchmarks, the 95%-confidence minimum detectable difference (accounting for image-level correlation) exceeds the median claimed improvement in recent proceedings, implying most published deltas are within noise.
- **Why Important:** Establishes what benchmarks can and cannot adjudicate, motivating either larger evaluation sets or humbler claims — infrastructure for honest science.
- **Why Possibly Novel:** Power analysis is standard elsewhere in science; applying it systematically to dense-prediction benchmarks against the claims distribution is new.
- **Minimal Experiment:** Estimate metric variance structures via bootstrap on public predictions; compute detectable-effect thresholds; survey claimed deltas from recent papers (as reported, not re-measured) for comparison.
- **Main Risk:** Variance estimation depends on modeling image correlation correctly; multiple estimators must agree.
- **Research Cluster:** EVAL-WEAK

### IDEA-B-0318 — Benchmarks age: val-test gaps grow with years of community tuning
- **One-sentence idea:** Measure benchmark aging by tracking how the gap between validation performance (visible to developers) and truly held-out performance evolves over methods published across a benchmark's lifetime.
- **Problem:** Years of community hyperparameter tuning against fixed validation sets should produce adaptive overfitting; whether it has — and how much of recorded "progress" it accounts for — is measurable but unmeasured for segmentation.
- **Core Hypothesis (falsifiable):** Evaluating methods from different publication years on a newly collected protocol-matched test set shows later methods' advantages shrinking relative to their validation-set advantages — a growing adaptivity gap that quantifies benchmark aging.
- **Why Important:** Tells the field how much leaderboard progress is real, and provides the aging-rate parameter needed to schedule benchmark refreshes.
- **Why Possibly Novel:** Adaptive-overfitting studies exist for classification (new-test-set replications); the segmentation version with lifetime-resolved analysis is missing.
- **Minimal Experiment:** Collect a protocol-matched fresh test set for one mature benchmark; evaluate era-spanning public models; compare progress slopes on old vs. new sets.
- **Main Risk:** A protocol-matched fresh collection is hard to achieve (annotation drift confounds aging), requiring the protocol-fidelity work of IDEA-B-0184.
- **Research Cluster:** EVAL-WEAK

### IDEA-B-0319 — Per-image vs. per-dataset averaging silently reorders methods
- **One-sentence idea:** Quantify how the unstated choice of metric aggregation order (average IoU per image then over images, vs. pooled pixels per dataset) changes reported numbers and method rankings.
- **Problem:** Codebases differ silently in aggregation order, which weights images and classes differently (per-image averaging upweights sparse images; pooled counting upweights large regions); papers compare numbers across this hidden fork without knowing it.
- **Core Hypothesis (falsifiable):** Recomputing published-model results under both aggregation orders produces differences comparable to typical claimed method gains, with ranking reversals among closely matched methods, and popular codebases split between the two conventions.
- **Why Important:** A pure bookkeeping audit that could invalidate many close comparisons and is fixable by a one-line reporting standard.
- **Why Possibly Novel:** The fork is known to implementers but its quantitative consequence and prevalence have never been documented.
- **Minimal Experiment:** Survey aggregation conventions across major codebases; recompute results for 20 public models both ways; report deltas and reversals.
- **Main Risk:** Minimal — the main challenge is exhaustiveness of the codebase survey.
- **Research Cluster:** EVAL-WEAK

### IDEA-B-0320 — Boundary metrics differ across implementations more than methods differ
- **One-sentence idea:** Audit boundary-metric implementations (tolerance defaults, distance transforms, edge extraction) across public codebases and measure whether implementation variance exceeds published method gains.
- **Problem:** Boundary-F and similar metrics involve implementation choices that codebases resolve differently and silently; boundary-method papers cite improvements smaller than the plausible implementation spread, making the literature potentially incomparable.
- **Core Hypothesis (falsifiable):** Scoring identical predictions through the boundary-metric implementations of several major codebases yields spreads exceeding half of typical published boundary-method gains, with tolerance-parameter defaults as the dominant source.
- **Why Important:** Forces metric standardization before further boundary-method claims can be interpreted — foundational hygiene for a whole sub-literature.
- **Why Possibly Novel:** Metric-implementation audits exist in other fields; boundary metrics in segmentation have escaped scrutiny despite their sensitivity.
- **Minimal Experiment:** Collect implementations; score a fixed prediction set through each; decompose variance by implementation choice; publish a reference implementation.
- **Main Risk:** Some spread reflects legitimately different metric definitions, requiring careful taxonomy rather than blanket "bug" framing.
- **Research Cluster:** EVAL-WEAK / BOUNDARY

### IDEA-B-0321 — Train-test near-duplicates reward big models disproportionately
- **One-sentence idea:** Test whether benchmark contamination by train-test near-duplicates inflates high-capacity models' scores more than small models', biasing architecture conclusions toward scale.
- **Problem:** Near-duplicate leakage is known to inflate scores; the unexamined question is whether the inflation is capacity-dependent — bigger models memorize near-duplicates better — which would mean contamination systematically distorts the field's scale narratives.
- **Core Hypothesis (falsifiable):** On contamination-stratified evaluations, the performance advantage of large over small models is substantially bigger on near-duplicate test items than on verified-novel items, and removing contamination shrinks measured scaling benefits for affected benchmarks.
- **Why Important:** Scale conclusions drive enormous investment; a capacity-dependent contamination bias would require re-reading the evidence behind them.
- **Why Possibly Novel:** Contamination audits measure prevalence; the capacity-interaction hypothesis with its scaling-narrative consequence is untested for dense prediction.
- **Minimal Experiment:** Identify near-duplicate test items for popular benchmarks; evaluate a capacity ladder stratified by contamination; compare scaling slopes across strata.
- **Main Risk:** Near-duplicate detection thresholds affect strata composition; results need threshold-robustness analysis.
- **Research Cluster:** EVAL-WEAK

### IDEA-B-0322 — Standardize inference protocol or stop comparing: the leaderboard re-run
- **One-sentence idea:** Re-evaluate leaderboard segmentation methods under one standardized inference protocol (resolution, TTA, sliding-window policy, output stride) to measure how much ranking structure is protocol rather than method.
- **Problem:** Published numbers mix inference-time choices that individually rival method effects (multi-scale testing, window overlap, resolution); leaderboards thus compare protocol stacks, not methods, and nobody knows how much reshuffling standardization would cause.
- **Core Hypothesis (falsifiable):** Under protocol-standardized re-evaluation, a substantial fraction of adjacent leaderboard orderings reverse, and protocol contributions (measured per method) frequently exceed the gaps those methods claimed over their baselines.
- **Why Important:** Quantifies the protocol share of "progress" and delivers a standardized harness the community can adopt — complementary to the resolution-law normalization of IDEA-B-0036.
- **Why Possibly Novel:** Protocol sensitivity is known anecdotally; the systematic leaderboard-scale re-run with protocol-attribution accounting is missing.
- **Minimal Experiment:** Re-run 20+ open-source methods under fixed and native protocols; decompose score differences; report ranking stability.
- **Main Risk:** Some methods are co-designed with their protocols; a single standard protocol may unfairly penalize them, requiring dual reporting.
- **Research Cluster:** EVAL-WEAK

### IDEA-B-0323 — Void regions hide the hardest pixels from evaluation
- **One-sentence idea:** Relabel ignore/void regions on benchmark test sets and measure how including these systematically excluded (and systematically hard) pixels changes model scores and rankings.
- **Problem:** Benchmarks exclude ambiguous boundary bands and unlabeled regions from scoring; these exclusions concentrate exactly where models differ most, so current metrics evaluate models only on the easy consensus subset — potentially hiding the real quality differences.
- **Core Hypothesis (falsifiable):** Void regions, once expert-relabeled, show model error rates several times higher than scored regions and larger inter-model spreads, and including them changes method rankings and shrinks measured "saturation" of mature benchmarks.
- **Why Important:** Reveals how much of the remaining segmentation problem has been defined out of existence by evaluation convention.
- **Why Possibly Novel:** Void conventions are inherited unquestioned; their systematic effect on measured progress has not been quantified.
- **Minimal Experiment:** Relabel void regions on benchmark subsets with expert protocols; re-score public models with void included; compare spreads and rankings.
- **Main Risk:** Some void regions are genuinely unlabelable; the relabeling protocol must separate "hard but decidable" from "undecidable."
- **Research Cluster:** EVAL-WEAK / ANNOT-EFF

### IDEA-B-0324 — Score against any plausible annotation, not the one you happened to buy
- **One-sentence idea:** Develop and validate multi-hypothesis evaluation (credit for matching any of k independent annotations) and measure how it changes absolute scores and method rankings relative to single-GT scoring.
- **Problem:** Single-annotation GT treats one plausible segmentation as truth, penalizing models for legitimate alternative interpretations (granularity choices, ambiguous boundaries); this punishes models in proportion to how often they pick a different-but-valid answer — a bias of unknown size and direction.
- **Core Hypothesis (falsifiable):** Under any-of-k evaluation with independently collected annotations, absolute scores rise non-uniformly across models (some models' "errors" are disproportionately valid alternatives), producing ranking changes and identifying which architectures happen to match annotation-pipeline conventions.
- **Why Important:** Separates "wrong" from "differently right" in evaluation — a fundamental fairness upgrade wherever ambiguity exists (most of segmentation).
- **Why Possibly Novel:** Multi-rater evaluation exists in medical niches; its consequences for mainstream benchmark rankings have never been measured.
- **Minimal Experiment:** Collect k=3 independent annotations for benchmark subsets; implement any-of-k and distribution-matching metrics; re-score public models; analyze non-uniformity.
- **Main Risk:** Any-of-k can be gamed by hedged predictions; the metric design must anticipate strategic softness.
- **Research Cluster:** EVAL-WEAK / ANNOT-EFF

### IDEA-B-0325 — How were these checkpoints chosen? The selection-leakage audit
- **One-sentence idea:** Audit and quantify checkpoint- and hyperparameter-selection practices in segmentation papers, measuring how much reported gains shrink when selection is done strictly without test-set feedback.
- **Problem:** Papers rarely document how final checkpoints were selected; selection on test (direct or via repeated submission) inflates results in ways invisible to readers, and the aggregate inflation across the literature is unknown.
- **Core Hypothesis (falsifiable):** Re-running representative methods with pre-registered, validation-only selection reduces their advantage over baselines by a meaningful fraction on average, and the reduction correlates with the number of selectable degrees of freedom each method exposes.
- **Why Important:** Quantifies a pervasive soft-leakage channel and supports concrete norms (selection documentation, submission limits) with measured stakes.
- **Why Possibly Novel:** Selection leakage is discussed abstractly; a measured audit with degrees-of-freedom analysis for dense prediction is new.
- **Minimal Experiment:** Reproduce 10 methods under strict selection protocols with matched budgets; compare against reported numbers; regress inflation on method degrees of freedom.
- **Main Risk:** Distinguishing selection inflation from ordinary reproduction gaps requires careful experimental bookkeeping.
- **Research Cluster:** EVAL-WEAK / NEG-RESULT

### IDEA-B-0326 — Add empty images: hallucination rates are invisible to mIoU
- **One-sentence idea:** Extend standard benchmarks with verified-empty images (no target classes present) and measure per-model hallucination rates that current metrics structurally cannot see.
- **Problem:** Every test image contains target classes, so models are never scored on their behavior when nothing is there — yet false detection on empty scenes is a primary deployment failure (alarms, phantom obstacles).
- **Core Hypothesis (falsifiable):** Models with near-identical benchmark scores differ by an order of magnitude in empty-scene hallucination rates, and hallucination propensity is uncorrelated with mIoU — an independent quality axis benchmarks currently ignore.
- **Why Important:** Adds a cheap, deployment-critical evaluation dimension and exposes which training practices (rebalancing per IDEA-B-0131, mIoU tuning per IDEA-B-0125) inflate phantom predictions.
- **Why Possibly Novel:** Open-set segmentation adds unknown objects; the systematic empty-scene protocol quantifying hallucination as a standard reporting axis is missing.
- **Minimal Experiment:** Curate verified-empty image sets matched to benchmark domains; evaluate 20+ public models; report hallucination distributions and correlations with standard metrics.
- **Main Risk:** "Verified empty" requires careful curation — residual small instances would corrupt the measurement (interacts with IDEA-B-0037).
- **Research Cluster:** EVAL-WEAK / LONG-TAIL

### IDEA-B-0327 — Efficiency claims don't survive hardware normalization
- **One-sentence idea:** Re-benchmark "efficient segmentation" methods under standardized hardware/compiler conditions to test how much of the claimed speed-accuracy frontier is measurement inconsistency.
- **Problem:** Latency numbers are reported on heterogeneous hardware, batch sizes, and compilation stacks; the published efficiency frontier aggregates incomparable measurements, and method rankings may reorder wholesale under uniform conditions.
- **Core Hypothesis (falsifiable):** Under one standardized benchmark harness, a substantial fraction of published efficiency-ranking claims reverse, and the reversals correlate with identifiable measurement choices (unfused ops, favorable batch sizes) in the original papers.
- **Why Important:** The efficiency literature guides edge deployment decisions; a normalization audit either validates or repairs its practical usefulness.
- **Why Possibly Novel:** MLPerf-style standardization exists for training; the efficiency-segmentation literature audit with reversal attribution is not done.
- **Minimal Experiment:** Re-measure 15 efficiency-focused models on two standardized hardware targets with consistent compilation; compare frontiers against published claims.
- **Main Risk:** Hardware-specific optimization is legitimate; the audit must distinguish unfair measurement from genuine hardware specialization.
- **Research Cluster:** EVAL-WEAK

### IDEA-B-0328 — Above a threshold, humans stop agreeing with IoU
- **One-sentence idea:** Measure where human quality judgments of segmentation masks decouple from IoU-family metrics and build a perceptually validated mask-quality metric for the high-quality regime.
- **Problem:** Metric-based rankings among high-quality masks may not reflect any difference users perceive or care about — or worse, may invert against perceived quality (e.g., penalizing smooth plausible boundaries) — leaving top-end method competition perceptually meaningless.
- **Core Hypothesis (falsifiable):** Human pairwise preferences correlate strongly with IoU below a quality threshold and near-zero above it, with systematic inversions in identifiable categories (boundary smoothness, topological correctness), and a metric fit to preference data predicts human judgments far better in the high-quality regime.
- **Why Important:** Defines where current metrics stop measuring anything users value, and provides the replacement for quality-critical applications (editing, AR).
- **Why Possibly Novel:** Perceptual metrics exist for image quality; the segmentation-mask version with a decoupling-threshold analysis is missing.
- **Minimal Experiment:** Collect large-scale pairwise human preferences over mask pairs stratified by IoU; locate the decoupling; fit and validate the perceptual metric.
- **Main Risk:** Preferences are application-dependent; the study needs several judgment framings to claim generality.
- **Research Cluster:** EVAL-WEAK / BOUNDARY

### IDEA-B-0329 — Per-frame metrics ignore the flicker users actually see
- **One-sentence idea:** Develop flicker-weighted video segmentation evaluation and measure how method rankings change when temporal instability is priced according to its perceptual and downstream cost.
- **Problem:** Video segmentation is evaluated frame-by-frame, but users and downstream consumers (tracking, AR occlusion) are dominated by temporal artifacts; two methods with equal per-frame accuracy can differ enormously in stability, invisible to current benchmarks.
- **Core Hypothesis (falsifiable):** Flicker measures vary widely at matched per-frame accuracy across methods, human video-quality preferences track flicker more than per-frame IoU in the high-accuracy regime, and flicker-weighted rankings reorder existing leaderboards materially.
- **Why Important:** Aligns video evaluation with actual consumption of video predictions, redirecting method development toward stability.
- **Why Possibly Novel:** Temporal consistency metrics exist scattered; the perceptually validated weighting with leaderboard consequence analysis is not established.
- **Minimal Experiment:** Compute stability profiles for public video segmenters; run human preference studies on stabilized-vs-accurate variants; construct and apply the weighted metric.
- **Main Risk:** Ground-truth-free flicker measures can reward over-smoothed (confidently wrong but stable) predictions; the metric must penalize that regime.
- **Research Cluster:** EVAL-WEAK

### IDEA-B-0330 — Membership inference as a benchmark-contamination detector for foundation methods
- **One-sentence idea:** Apply membership-inference techniques to test whether foundation-model-based segmentation methods have effectively seen benchmark test images during pretraining, and quantify the score inflation attributable to membership.
- **Problem:** Methods built on web-pretrained models are compared on benchmarks whose test images circulate on the web; direct contamination checking is impossible without pretraining-corpus access, but membership-inference signals offer an audit route nobody has exercised for dense prediction.
- **Core Hypothesis (falsifiable):** Membership-inference scores on benchmark test images are elevated for foundation-based methods relative to scratch-trained controls, and per-image performance correlates with membership evidence — yielding a quantitative contamination-inflation estimate for affected leaderboards.
- **Why Important:** Restores interpretability to comparisons between foundation-era and classical methods, and pressures pretraining-corpus transparency.
- **Why Possibly Novel:** Membership inference targets privacy; its use as a benchmark-hygiene instrument for dense prediction is new (extends IDEA-B-0201 and IDEA-B-0321 to the method-audit level).
- **Minimal Experiment:** Calibrate membership signals on models with known corpora; apply to popular foundation-based segmenters over benchmark test sets; correlate membership evidence with per-image scores.
- **Main Risk:** Membership-inference reliability at web scale is contested; conclusions must carry calibrated uncertainty.
- **Research Cluster:** EVAL-WEAK / NEG-RESULT

### IDEA-B-0331 — What fraction of residual "error" on mature benchmarks is GT error?
- **One-sentence idea:** Adjudicate model-GT disagreements on mature benchmarks with expert panels to measure the fraction of scored errors where the model is right and the ground truth is wrong.
- **Problem:** As models approach benchmark ceilings, an unknown share of their measured errors are actually GT mistakes; without measuring that share, remaining-error analyses and saturation claims are uninterpretable.
- **Core Hypothesis (falsifiable):** For top models on mature benchmarks, expert adjudication finds the model correct in a substantial fraction of disagreement pixels/instances, concentrated in systematic GT failure categories (missed instances per IDEA-B-0017, boundary bias per IDEA-B-0061), and correcting them changes both absolute scores and model rankings.
- **Why Important:** Determines whether continued optimization on these benchmarks measures model improvement or GT-error fitting — the practical end-of-life criterion for a benchmark.
- **Why Possibly Novel:** Label-error studies exist for classification test sets; the disagreement-adjudication protocol at dense granularity with ranking consequences is rare and unsystematized.
- **Minimal Experiment:** Sample disagreement regions between top models and GT; run blinded three-expert adjudication with decoys; report the model-correct fraction and re-scored rankings.
- **Main Risk:** Expert adjudication is itself imperfect exactly where GT failed; blinding and decoy protocols are essential.
- **Research Cluster:** EVAL-WEAK / ANNOT-EFF

### IDEA-B-0332 — The same baseline scores differently in every paper
- **One-sentence idea:** Meta-audit the spread of reported numbers for identical baseline methods across the literature and identify the reproduction choices that generate the spread.
- **Problem:** Baseline numbers for the same method on the same benchmark vary across papers by margins rivaling claimed contributions; the spread's size, sources, and its correlation with papers' own-method framing have never been quantified.
- **Core Hypothesis (falsifiable):** Surveyed baseline reports show cross-paper standard deviations exceeding half of typical claimed gains, the spread is explained by identifiable configuration deltas (schedule, resolution, augmentation), and baselines are reported systematically lower in papers proposing competitors than in reproduction studies.
- **Why Important:** Quantifies both the reproducibility crisis and the adversarial-baseline effect in one measurable audit, motivating standardized baseline registries.
- **Why Possibly Novel:** Anecdotes abound; the systematic survey with configuration forensics and directional-bias testing is not published for dense prediction.
- **Minimal Experiment:** Extract baseline reports from proceedings (as reported); catalog configurations; fit variance attributions; test the directional-bias hypothesis statistically.
- **Main Risk:** Configuration details are often unreported, limiting forensic attribution to a subset.
- **Research Cluster:** EVAL-WEAK / NEG-RESULT

### IDEA-B-0333 — Threshold-based and threshold-free metrics tell different stories
- **One-sentence idea:** Measure how often model comparisons flip between threshold-based metrics (mIoU at argmax) and threshold-free metrics (AP-style, calibration-weighted), and determine which family predicts deployment-tuned performance.
- **Problem:** Argmax-based metrics evaluate one operating point chosen implicitly by training, while deployments tune operating points; a model worse at argmax but better across thresholds is the better deployment choice, yet standard evaluation would reject it.
- **Core Hypothesis (falsifiable):** A meaningful fraction of model pairs invert between the two metric families, and threshold-free metrics predict post-tuning deployment performance substantially better — establishing that argmax evaluation systematically misranks models for tuned use.
- **Why Important:** Clarifies which evaluation family to trust for deployment decisions, with concrete stakes measured rather than argued.
- **Why Possibly Novel:** The metric families coexist without a systematic inversion-rate and deployment-prediction comparison for segmentation.
- **Minimal Experiment:** Evaluate many public models under both families; simulate deployment tuning on held-out data; compare each family's predictive power for tuned outcomes.
- **Main Risk:** Deployment tuning simulation choices affect the answer; several tuning regimes must be covered.
- **Research Cluster:** EVAL-WEAK / CALIBRATION

### IDEA-B-0334 — Panoptic Quality double-counts boundary errors
- **One-sentence idea:** Derive and empirically demonstrate how PQ's structure (IoU inside the matched-segment term and boundary-sensitive matching in the recognition term) penalizes boundary errors twice, and evaluate a corrected decomposition.
- **Problem:** PQ multiplies a recognition term by an average-IoU term, both of which degrade with boundary error near the matching threshold, so boundary mistakes are charged twice while other error types are charged once — a structural bias shaping panoptic method development invisibly.
- **Core Hypothesis (falsifiable):** Controlled error injections show boundary perturbations reduce PQ disproportionately versus equal-magnitude recognition or interior errors, real method comparisons change under a double-counting-corrected metric, and the correction better matches human quality judgments.
- **Why Important:** The headline panoptic metric's incentive structure directs a subfield; a demonstrated structural bias plus validated correction re-tunes those incentives.
- **Why Possibly Novel:** PQ alternatives exist; the double-counting derivation with injection-based demonstration and preference validation is a specific uncontributed analysis.
- **Minimal Experiment:** Inject calibrated error types into predictions; trace PQ responses; re-rank public panoptic models under corrected metrics; run a small preference study.
- **Main Risk:** Metric-design debates are contentious; the empirical injection results must carry the argument regardless of which correction wins.
- **Research Cluster:** EVAL-WEAK / BOUNDARY

### IDEA-B-0335 — Nondeterminism noise exceeds small claimed gains
- **One-sentence idea:** Quantify the evaluation variance caused solely by framework nondeterminism (kernel selection, atomics, data-order jitter at fixed seeds) and compare it against the distribution of small published improvements.
- **Problem:** Even "seeded" runs vary across hardware and library versions; if this irreducible nondeterminism band is comparable to the ~0.2–0.5-point gains commonly claimed, such claims are unfalsifiable as reported — a floor nobody has measured for dense prediction.
- **Core Hypothesis (falsifiable):** Repeated fixed-seed training/evaluation across hardware and library configurations produces metric spreads overlapping a nontrivial fraction of small published gains, with identifiable dominant sources (nondeterministic kernels) whose control shrinks the band at measurable compute cost.
- **Why Important:** Establishes the reproducibility noise floor that any claimed improvement must clear, plus practical guidance on when determinism is worth its cost.
- **Why Possibly Novel:** Nondeterminism is documented technically; its quantitative comparison against the field's claims distribution is not.
- **Minimal Experiment:** Train/evaluate fixed configurations across GPU generations and library versions with and without determinism flags; report spread decompositions against a survey of claimed deltas.
- **Main Risk:** The band varies by model family and scale, requiring several representative configurations for a general statement.
- **Research Cluster:** EVAL-WEAK / NEG-RESULT

### IDEA-B-0336 — Structured hallucination: what segmenters see in pure noise
- **One-sentence idea:** Characterize the segmentation prior by analyzing what models predict on structureless inputs (noise, textures, constant fields) and test whether the hallucinated layouts reproduce training-set scene statistics.
- **Problem:** Model behavior off the data manifold reveals the internalized prior that shapes ambiguous-input behavior everywhere, yet dense models' hallucination structure (layout grammar, class placement) has never been systematically mapped or connected to dataset statistics.
- **Core Hypothesis (falsifiable):** Predictions on matched-statistics noise are far from uniform — reproducing training-set layout regularities (road-below-sky geometry, class adjacency statistics) with high fidelity — and the hallucination prior's strength predicts the model's behavior on genuinely ambiguous real regions.
- **Why Important:** Provides a direct read-out of the learned scene prior, useful for dataset-bias auditing, ambiguity behavior prediction, and comparing what different training regimes internalize.
- **Why Possibly Novel:** Feature-visualization exists for classifiers; the systematic hallucination-cartography of dense predictors with dataset-statistics matching is new.
- **Minimal Experiment:** Feed matched-spectrum noise ensembles to many segmenters; extract layout statistics of predictions; compare against training-set statistics; correlate prior strength with ambiguous-region behavior.
- **Main Risk:** Off-manifold behavior may be dominated by numerically fragile pathways with limited relevance to on-manifold ambiguity — the correlation arm must carry that burden.
- **Research Cluster:** PHENOMENON

### IDEA-B-0337 — Boundary quality keeps learning after interiors converge
- **One-sentence idea:** Characterize the two-phase training dynamic where region/interior accuracy converges early while boundary precision continues improving (or begins only) much later, and identify what controls the second phase.
- **Problem:** Training-length decisions use aggregate validation curves that interior accuracy dominates; if boundary learning follows a distinct delayed schedule, standard early stopping systematically truncates it — and the phenomenon would reveal ordered feature learning in dense tasks.
- **Core Hypothesis (falsifiable):** Across architectures and datasets, boundary-F improves on a substantially delayed schedule relative to interior mIoU (measurable phase separation), the delay scales with factors predicted by learning-order theories (feature frequency, gradient share per IDEA-B-0009), and extended training beyond aggregate convergence buys measurable boundary gains.
- **Why Important:** Changes training-schedule practice for boundary-critical applications and provides a clean dense-prediction instance of ordered/delayed feature learning.
- **Why Possibly Novel:** Loss-curve analyses are aggregate; the component-resolved learning-dynamics study for dense prediction is missing.
- **Minimal Experiment:** Log decomposed metrics at high checkpoint frequency across long training runs; characterize phase structure; test the predicted controlling factors via intervention (gradient reallocation).
- **Main Risk:** The delayed phase may be tiny in magnitude even if real, limiting practical significance.
- **Research Cluster:** PHENOMENON / BOUNDARY

### IDEA-B-0338 — Measure the effective context radius; stop assuming more is better
- **One-sentence idea:** Measure, per class and dataset, the context radius beyond which additional visual context stops changing (or starts hurting) predictions, challenging the assumption that context is monotonically valuable.
- **Problem:** Architecture evolution relentlessly expands context (global attention, larger crops) on the assumption of monotone benefit; the actual information-value curve of context radius — where it saturates, for what, and when it turns negative — has never been mapped.
- **Core Hypothesis (falsifiable):** Prediction quality as a function of available context radius saturates at class-characteristic radii far smaller than typical model receptive fields for most classes, with measurable negative returns for some (context-overfitting per IDEA-B-0032), and the radius map transfers across architectures.
- **Why Important:** A validated context-value map would justify cheaper local architectures for most of the label space and identify the minority of classes needing global reasoning.
- **Why Possibly Novel:** Receptive-field analysis measures what models use; the information-value curve of context as a property of the task (architecture-transferable) is unmeasured.
- **Minimal Experiment:** Evaluate models on context-masked inputs across radii; fit per-class saturation curves; test cross-architecture transfer of the radius map.
- **Main Risk:** Context masking introduces artifacts; requires multiple masking strategies to agree (blur, crop, inpaint).
- **Research Cluster:** PHENOMENON / ASSUMPTION

### IDEA-B-0339 — The logit lens for segmentation: predictions form early, boundaries form late
- **One-sentence idea:** Apply intermediate-layer decoding to dense models to characterize when (at what depth) predictions crystallize, testing whether class decisions form early while boundary placement is decided in the final layers.
- **Problem:** Dense networks are read out only at the end; knowing where decisions form would enable early-exit inference for easy regions, targeted interventions at the deciding depth, and a mechanistic picture of dense computation that currently doesn't exist.
- **Core Hypothesis (falsifiable):** Linear decoders at intermediate depths recover final class decisions for most pixels well before the final layers (with agreement depth predicting pixel difficulty), while boundary-pixel decisions crystallize systematically later — a depth-ordered division of labor consistent across architectures.
- **Why Important:** Supports adaptive-compute segmentation (exit early where decided) with measured foundations and maps the computational anatomy of dense prediction.
- **Why Possibly Novel:** Logit-lens analysis is established for language models; its systematic application to dense visual prediction with the interior/boundary crystallization contrast is new.
- **Minimal Experiment:** Train per-depth linear decoders on frozen intermediate activations; map decision-crystallization depth per pixel type; validate early-exit inference against the map.
- **Main Risk:** Linear decodability underestimates information; crystallization depth may partly reflect probe capacity rather than decision formation.
- **Research Cluster:** PHENOMENON / REP-MISMATCH

### IDEA-B-0340 — Sparse tickets transfer across datasets but not across tasks
- **One-sentence idea:** Test whether lottery-ticket sparse structures found for segmentation transfer to new segmentation datasets but fail across task types (to detection or depth), locating what sparsity structures encode.
- **Problem:** Pruning research finds transferable "tickets" within classification; whether sparse structure encodes task-generic visual computation or task-specific wiring determines both the practicality of reusable sparse models and the interpretation of what pruning preserves.
- **Core Hypothesis (falsifiable):** Segmentation-derived tickets retrain to full quality on other segmentation datasets but show significant deficits when retrained for detection/depth at matched sparsity — a task-boundary in sparsity transferability that survives dataset-difficulty controls.
- **Why Important:** Defines reuse boundaries for sparse deployment pipelines and reveals that task identity is imprinted in connectivity structure, not just weights.
- **Why Possibly Novel:** Ticket transfer is studied within classification; the task-type boundary question for dense prediction is unexplored.
- **Minimal Experiment:** Derive tickets on one segmentation setup; retrain across a dataset/task transfer matrix at matched sparsity; map transfer quality against task relatedness.
- **Main Risk:** Ticket-finding is recipe-sensitive; results need stability across pruning methods.
- **Research Cluster:** PHENOMENON / CROSS-DOMAIN

### IDEA-B-0341 — Attention maps don't explain dense predictions better than gradients
- **One-sentence idea:** Subject attention-based explanations of segmentation/detection transformers to sanity checks (model randomization, faithfulness deletion tests) against simple gradient baselines.
- **Problem:** Attention visualizations are routinely presented as explanations of dense-model behavior in papers and applications, but their faithfulness has mainly been challenged in NLP and classification; the dense-prediction community continues using them unaudited.
- **Core Hypothesis (falsifiable):** Attention-based explanations for dense transformers fail parameter-randomization sanity checks and deletion-faithfulness tests at rates comparable to known-broken methods, and simple gradient baselines dominate them on faithfulness metrics — invalidating common explanatory practice.
- **Why Important:** Interpretability claims support safety cases and scientific conclusions; an audit protects both from decorative explanations.
- **Why Possibly Novel:** Sanity-check methodology exists; its systematic application to dense-prediction explanation practice is missing.
- **Minimal Experiment:** Run randomization and deletion tests on attention, rollout, and gradient explanations across DETR/Mask2Former-class models; rank faithfulness.
- **Main Risk:** Faithfulness metrics themselves are contested; multiple complementary tests must agree.
- **Research Cluster:** PHENOMENON / NEG-RESULT

### IDEA-B-0342 — Different error components scale with different exponents
- **One-sentence idea:** Fit separate scaling laws (versus data, model size, compute) for decomposed error components (classification, localization, boundary) to test whether "scaling solves everything" hides components that barely improve.
- **Problem:** Scaling analyses use aggregate metrics; if boundary error scales with a much flatter exponent than classification error, scale-centric strategy will asymptotically fail boundary-critical applications — a divergence invisible in aggregate curves.
- **Core Hypothesis (falsifiable):** Component-resolved scaling fits show significantly different exponents, with boundary/localization error improving markedly slower than classification error across the model/data ladder, implying component-specific interventions rather than scale are required for the flat components.
- **Why Important:** Refines the field's central strategic belief (scale fixes everything) into component-resolved guidance about what scale will and won't buy.
- **Why Possibly Novel:** Scaling laws for dense prediction exist in aggregate; the component decomposition of exponents is unmeasured.
- **Minimal Experiment:** Train a controlled scale ladder; decompose errors per IDEA-B-0316's tooling; fit and compare component exponents with uncertainty.
- **Main Risk:** Component metrics have different noise floors (GT limits per IDEA-B-0047), which must be modeled to avoid mistaking floors for flat exponents.
- **Research Cluster:** PHENOMENON / EVAL-WEAK

### IDEA-B-0343 — Does pretraining still matter? The foundation-era rethinking replication
- **One-sentence idea:** Re-examine, under current recipes and dataset scales, whether ImageNet-style pretraining retains any benefit for dense-prediction training compared to random initialization with modern schedules.
- **Problem:** Classic findings that pretraining mainly buys convergence speed (not final quality) at sufficient data scale predate modern augmentation, schedules, and architectures; the community defaults to pretraining without knowing whether the old conclusion strengthened, weakened, or reversed.
- **Core Hypothesis (falsifiable):** With modern recipes, the pretraining-vs-scratch final-quality gap at practical dataset sizes has narrowed for CNNs but widened for ViT-class models (which are recipe-hungrier), with the crossover dataset size measurable per architecture family — updating a foundational recommendation with current evidence.
- **Why Important:** Pretraining choices shape licensing, privacy exposure, and compute budgets; the recommendation should rest on current-regime evidence rather than inherited results.
- **Why Possibly Novel:** The original rethinking predates the ViT/foundation era; a rigorous re-run across current architecture families is due and absent.
- **Minimal Experiment:** Train scratch-vs-pretrained arms across dataset-size ladders for CNN and ViT segmenters under tuned modern recipes; map crossovers per family.
- **Main Risk:** "Tuned modern recipe" for scratch training requires substantial search to be fair — under-tuning would bias toward pretraining.
- **Research Cluster:** ASSUMPTION / CROSS-DOMAIN

### IDEA-B-0344 — Models fail at image edges, and benchmarks barely look there
- **One-sentence idea:** Audit performance as a function of distance to the image border — where truncated objects, padding effects, and photographer framing bias converge — and quantify how little current evaluation weights this deployment-critical zone.
- **Problem:** Deployed systems (driving, robotics) care intensely about objects entering the frame at borders, but benchmark objects are center-biased by photographer framing and models see borders mainly through padding artifacts — a triple alignment of neglect nobody has quantified end-to-end.
- **Core Hypothesis (falsifiable):** Detection/segmentation quality degrades substantially in the outer image band even after controlling for object truncation and size, the degradation traces to both training exposure statistics and padding behavior (separable via augmentation interventions), and border-zone performance is nearly uncorrelated with headline metrics across models.
- **Why Important:** Frame-entry objects are the highest-urgency perceptions in dynamic deployments; an uncorrelated quality axis there demands its own evaluation and training attention.
- **Why Possibly Novel:** Center bias is known for saliency; the border-zone performance audit with cause attribution and metric-independence analysis is new (complements IDEA-B-0066's boundary-quality focus with a detection/recall focus).
- **Minimal Experiment:** Stratify benchmark metrics by border distance with truncation/size controls; run padding and crop-augmentation interventions; measure cross-model correlation between border and central performance.
- **Main Risk:** Border GT is itself least reliable (truncation ambiguity per IDEA-B-0185), requiring adjudicated evaluation subsets.
- **Research Cluster:** PHENOMENON / EVAL-WEAK

### IDEA-B-0345 — Sticky segments: temporal hysteresis in video predictions
- **One-sentence idea:** Quantify prediction hysteresis in video segmentation — regions retaining their initial label despite accumulating contrary evidence — and determine whether it is an architecture property or an emergent training effect.
- **Problem:** Video models exhibit anecdotal "stickiness" (a region labeled X stays X too long), which is a safety issue for changing scenes; the phenomenon has no quantitative characterization, no known mechanism, and no measurement standard.
- **Core Hypothesis (falsifiable):** Label-switch latency in response to controlled evidence changes is asymmetric (staying beats switching) across recurrent and attention-based video models, the asymmetry grows with temporal-context length, and it originates in training-data label persistence statistics (testable by retraining on persistence-manipulated data).
- **Why Important:** Characterizes a deployment-relevant temporal failure mode with a mechanism test, informing video-architecture and training-data design.
- **Why Possibly Novel:** Temporal consistency research optimizes for stability; the pathological excess-stability regime and its causal origin are unstudied.
- **Minimal Experiment:** Construct controlled label-change sequences (synthetic and staged real); measure switch-latency asymmetries across models; run the persistence-statistics retraining intervention.
- **Main Risk:** Hysteresis and legitimate temporal smoothing are entangled; the evidence-controlled stimuli must cleanly separate them.
- **Research Cluster:** PHENOMENON

### IDEA-B-0346 — When test-time augmentation quietly hurts
- **One-sentence idea:** Map the regimes where test-time augmentation degrades dense-prediction accuracy — under domain shift, on boundary detail, and for minority classes — challenging its reputation as free accuracy.
- **Problem:** TTA averaging is deployed as a costless improvement, but averaging across views can destroy high-frequency detail, suppress minority predictions (majority views win votes), and behave unpredictably off-distribution — harms invisible in the aggregate in-domain evaluations that built its reputation.
- **Core Hypothesis (falsifiable):** TTA improves aggregate in-domain scores while measurably degrading boundary-F and rare-class recall, and under moderate domain shift its aggregate benefit inverts — a regime map stable enough to derive usage rules (which augmentations, which conditions).
- **Why Important:** Corrects a near-universal deployment default with component- and regime-resolved evidence, at zero methodological complexity.
- **Why Possibly Novel:** TTA is evaluated in aggregate; the component-decomposed, shift-conditional harm analysis for dense prediction is missing (complements IDEA-B-0020's training-interaction analysis).
- **Minimal Experiment:** Evaluate TTA variants across models with decomposed metrics, in-domain and across a shift ladder; construct the harm-regime map.
- **Main Risk:** Harm regimes may be model-specific, requiring many models for transferable rules.
- **Research Cluster:** ASSUMPTION / EVAL-WEAK

### IDEA-B-0347 — Class-index symmetry breaks at small scale: label-permutation variance
- **One-sentence idea:** Measure whether the arbitrary assignment of classes to logit indices affects training outcomes in small-data/small-model regimes, quantifying a symmetry that theory says shouldn't matter and reproducibility practice assumes doesn't.
- **Problem:** Class-to-index assignment is a bookkeeping choice presumed irrelevant, but initialization interacts with output-layer geometry, and in low-data regimes the symmetry breaking could produce measurable per-class variance — an unexamined component of run-to-run irreproducibility.
- **Core Hypothesis (falsifiable):** Permuting class indices (with fixed seeds otherwise) changes per-class IoU in small-scale regimes by margins comparable to seed variance, the effect decays predictably with scale, and it traces to output-layer initialization geometry (testable via symmetric initialization schemes that eliminate it).
- **Why Important:** Identifies and eliminates a gratuitous variance source in exactly the low-resource settings where every fraction of a point matters, while probing how arbitrary symmetries break in practice.
- **Why Possibly Novel:** Seed variance is studied; the label-permutation axis has apparently never been isolated for dense prediction.
- **Minimal Experiment:** Train permutation grids at several scales with fixed other randomness; decompose variance; test symmetric-init elimination.
- **Main Risk:** The effect may be negligible beyond toy scales — a useful null, but of modest impact.
- **Research Cluster:** PHENOMENON / NEG-RESULT

### IDEA-B-0348 — Fine-tunability is not predicted by source performance
- **One-sentence idea:** Test whether a checkpoint's benchmark score predicts how well it fine-tunes to new tasks/domains, challenging the universal practice of selecting the highest-scoring checkpoint as the starting point.
- **Problem:** Practitioners initialize from the best-performing available checkpoint, assuming performance and adaptability coincide; but high scores may reflect specialization (sharp fitting to source idiosyncrasies) that actively resists adaptation — the correlation has never been measured across a checkpoint zoo.
- **Core Hypothesis (falsifiable):** Above a competence threshold, source benchmark score explains little variance in fine-tuned target performance across checkpoints, while measurable representation properties (equivariance profile per IDEA-B-0296, semantic-depth profile per IDEA-B-0306) explain substantially more — overturning the selection heuristic.
- **Why Important:** Checkpoint selection is among the most frequent decisions in applied ML; replacing a wrong heuristic with validated predictors saves compute and improves outcomes field-wide.
- **Why Possibly Novel:** Transferability estimation research targets task selection; the checkpoint-selection heuristic audit with alternative-predictor comparison is distinct.
- **Minimal Experiment:** Fine-tune 30+ public checkpoints (spanning scores) onto several targets; measure the score-transfer correlation; benchmark alternative predictors.
- **Main Risk:** Checkpoints differ along many correlated axes (data, recipe, architecture), demanding careful statistical treatment.
- **Research Cluster:** ASSUMPTION / CROSS-DOMAIN

### IDEA-B-0349 — Augmentation policies transfer across datasets but break across label densities
- **One-sentence idea:** Test whether learned/tuned augmentation policies transfer along the dataset axis (new data, same task) but fail along the task axis (classification-tuned policies harming dense prediction), locating the transfer boundary of augmentation knowledge.
- **Problem:** Augmentation policies tuned on classification are imported wholesale into segmentation pipelines; if policy optimality is determined by label density (geometric transforms corrupt dense labels differently than image labels), this import is systematically wrong in a predictable direction.
- **Core Hypothesis (falsifiable):** Policies tuned per-dataset within one task type transfer with minor loss, while classification-tuned policies applied to segmentation are measurably suboptimal (particularly in geometric-transform strength) relative to dense-tuned policies, with the deficit concentrated in boundary and small-object metrics.
- **Why Important:** Corrects a silent default in most dense-prediction recipes and defines which axes augmentation knowledge generalizes along.
- **Why Possibly Novel:** Augmentation search exists per task; the transfer-boundary characterization across the dataset-vs-label-density axes is unmeasured.
- **Minimal Experiment:** Tune policies on classification and segmentation datasets; cross-apply along both axes; decompose transfer losses by transform type and metric component.
- **Main Risk:** Policy search noise may swamp transfer effects, requiring repeated searches for reliable policy estimates.
- **Research Cluster:** ASSUMPTION / GENERALIZATION

### IDEA-B-0350 — The field's default recipes encode the benchmarks they were tuned on
- **One-sentence idea:** Test whether standard training recipes (schedules, augmentation defaults, loss weights inherited across hundreds of papers) are overfit to the handful of benchmarks they evolved on, by measuring recipe-vs-architecture contributions on genuinely new datasets.
- **Problem:** The community's shared recipe stack evolved through years of tuning on COCO/Cityscapes-class benchmarks; on new domains, practitioners import recipes assuming neutrality, but the recipes may encode benchmark-specific choices whose misfit is attributed to data difficulty or architecture instead.
- **Core Hypothesis (falsifiable):** On newly collected datasets, per-dataset recipe re-tuning changes performance by margins comparable to architecture changes, the standard recipes' deficit correlates with the dataset's statistical distance from legacy benchmarks, and recipe components rank differently in importance than on legacy benchmarks — demonstrating recipe-benchmark coupling.
- **Why Important:** Quantifies how much of "architecture progress" is recipe-benchmark co-evolution and gives new-domain practitioners evidence for budgeting recipe search rather than architecture search.
- **Why Possibly Novel:** Recipe importance is acknowledged within benchmarks; the coupling-to-legacy-benchmarks measurement on fresh data with distance prediction is new.
- **Minimal Experiment:** On 3 fresh datasets spanning statistical distances from legacy benchmarks, compare imported vs. re-tuned recipes across 3 architectures; attribute variance between recipe and architecture factors.
- **Main Risk:** Fair recipe re-tuning budgets are expensive; conclusions are conditional on the search budget granted.
- **Research Cluster:** ASSUMPTION / EVAL-WEAK

---

## Part 2 — Mutations (IDEA-B-M-0001 .. IDEA-B-M-0020)

Crossovers and variants of primary ideas. Parent IDs given; each mutation is a distinct executable study, not a restatement.

### IDEA-B-M-0001 — GT-noise-floor atlas (parents: 0003, 0031, 0047)
- **One-sentence idea:** Unify jitter, polygon-ceiling, and disagreement measurements into a per-benchmark, per-metric noise-floor atlas so every leaderboard can display "distance to floor."
- **Core Hypothesis (falsifiable):** Noise floors estimated by the three independent methods agree within stated uncertainty, and several benchmark-metric pairs show SOTA already inside the floor band.
- **Minimal Experiment:** Run all three estimation protocols on shared subsets of three benchmarks; publish the atlas and floor-adjusted rankings.
- **Main Risk:** Method disagreement would prevent a single floor number (informative, but kills the atlas framing).
- **Research Cluster:** EVAL-WEAK

### IDEA-B-M-0002 — Size-conditional recalibration as a shipping standard (parents: 0014, 0093)
- **One-sentence idea:** Package size-conditional score recalibration as a model-agnostic post-processor and validate it jointly for AP ranking and probability calibration across detector families and domains.
- **Core Hypothesis (falsifiable):** One fitted monotone family per size decade transfers across datasets within a domain, improving both AP_small and size-binned reliability with no retraining.
- **Minimal Experiment:** Fit on one dataset per domain; test transfer to two others; report both metric families.
- **Main Risk:** Transfer may fail across capture conditions, reducing this to per-dataset tooling.
- **Research Cluster:** SMALL-OBJ / CALIBRATION

### IDEA-B-M-0003 — The context-reliance stress card (parents: 0007, 0032, 0338)
- **One-sentence idea:** Combine object-evidence ablation and context-radius masking into a standard two-axis "context reliance card" reported per model, and validate that card scores predict domain-shift fragility.
- **Core Hypothesis (falsifiable):** The card's two scores predict cross-domain per-class degradation better than any headline metric.
- **Minimal Experiment:** Produce cards for 15 models; regress measured shift degradation on card scores.
- **Main Risk:** Masking-protocol artifacts could dominate card values (mitigated by multi-protocol agreement per 0338).
- **Research Cluster:** GENERALIZATION / EVAL-WEAK

### IDEA-B-M-0004 — Residualized UQ benchmarking (parents: 0075, 0089, 0101)
- **One-sentence idea:** Re-run the segmentation-UQ literature under a protocol that subtracts the geometric baseline (boundary distance + object size + sensitivity) before scoring, producing the first residual-information ranking of UQ methods.
- **Core Hypothesis (falsifiable):** Residualized rankings differ materially from published rankings, and several methods carry near-zero residual information.
- **Minimal Experiment:** Implement the baseline stack; re-score 8 UQ methods from public code on two datasets.
- **Main Risk:** Over-subtraction (removing legitimately shared variance) must be handled with explicit variance-partition reporting.
- **Research Cluster:** UNCERTAINTY / EVAL-WEAK

### IDEA-B-M-0005 — Phase-targeted gradient reallocation (parents: 0009, 0337)
- **One-sentence idea:** Reallocate per-size/per-region loss share only during the late (boundary) learning phase, testing whether timing-aware allocation beats static reweighting for closing size and boundary gaps.
- **Core Hypothesis (falsifiable):** Late-phase reallocation matches or beats always-on reweighting on small-object and boundary metrics at equal compute, with less interior degradation.
- **Minimal Experiment:** Compare {none, static, late-phase} allocation on two datasets with decomposed metrics.
- **Main Risk:** Phase boundaries vary by run; requires the phase-detection machinery from 0337 to be reliable.
- **Research Cluster:** SMALL-OBJ / BOUNDARY

### IDEA-B-M-0006 — One missing-annotation correction pipeline (parents: 0017, 0144)
- **One-sentence idea:** Build a single audited correction pipeline for missing GT (verified FP-adjudication + background-contamination masking) and remeasure benchmark scores and long-tail method rankings after correction.
- **Core Hypothesis (falsifiable):** Post-correction, high-recall models gain systematically and a measurable fraction of long-tail method gaps change sign or significance.
- **Minimal Experiment:** Apply the pipeline to one benchmark; re-score 15 public models pre/post.
- **Main Risk:** Adjudication cost limits the corrected subset's size, bounding statistical power.
- **Research Cluster:** EVAL-WEAK / LONG-TAIL

### IDEA-B-M-0007 — Extrapolation-aware boundary annotation (parents: 0068, 0162)
- **One-sentence idea:** Design an annotation protocol that traces only boundary segments where models cannot extrapolate (evidence-weak zones flagged by the 0068 recovery model), skipping segments models reconstruct for free.
- **Core Hypothesis (falsifiable):** Evidence-adaptive partial tracing reaches full-supervision quality at a lower traced fraction than the uniform partial tracing of 0162.
- **Minimal Experiment:** Compare uniform-k% vs. adaptive tracing at matched annotation time on one dataset.
- **Main Risk:** The evidence-strength flagger must generalize across datasets or the protocol won't ship.
- **Research Cluster:** ANNOT-EFF / BOUNDARY

### IDEA-B-M-0008 — Two-axis open-world stress suite (parents: 0092, 0326)
- **One-sentence idea:** Merge empty-scene hallucination testing with texture-vs-semantic novelty controls into one open-world stress suite that scores false-alarm and missed-novelty behavior on separate axes.
- **Core Hypothesis (falsifiable):** The two axes are close to uncorrelated across models, proving both must be reported.
- **Minimal Experiment:** Assemble the suite; profile 20 models; report axis correlation and per-family patterns.
- **Main Risk:** Insertion/curation artifacts (shared with parents) need one clean artifact-control arm.
- **Research Cluster:** UNCERTAINTY / EVAL-WEAK

### IDEA-B-M-0009 — Stacked GT-free quality estimation (parents: 0103, 0283, 0069)
- **One-sentence idea:** Combine proxy-model uncertainty, cross-prompt agreement, and temporal jitter into one stacked GT-free mask-quality estimator, and test whether the signals are additive or redundant.
- **Core Hypothesis (falsifiable):** The stacked estimator predicts per-image quality substantially better than any single signal, with measurable complementary coverage (each signal catching different failure types).
- **Minimal Experiment:** Fit the stack on labeled data; evaluate on held-out models and one shifted domain.
- **Main Risk:** All three signals may share the boundary-distance confound, collapsing the ensemble's value.
- **Research Cluster:** UNCERTAINTY / ANNOT-EFF

### IDEA-B-M-0010 — One corpus-statistics covariate to rule the class axis (parents: 0128, 0278)
- **One-sentence idea:** Build a single web-corpus statistics score per class (frequency + naming consistency) and test it as a unified covariate explaining per-class performance in supervised long-tail, open-vocab, and synthetic-augmentation (0148) settings simultaneously.
- **Core Hypothesis (falsifiable):** One fitted covariate transfers across all three settings with high explanatory power, unifying three literatures' "class difficulty" notions.
- **Minimal Experiment:** Compute the score for benchmark vocabularies; fit/validate across the three settings' per-class outcomes.
- **Main Risk:** Different settings may need different corpus statistics, fragmenting the unification.
- **Research Cluster:** LONG-TAIL / MULTIMODAL-SUP

### IDEA-B-M-0011 — Frequency predicts the robustness exponent (parents: 0146, 0342)
- **One-sentence idea:** Join the frequency-fragility law with component-resolved scaling: test whether training frequency predicts each class's robustness scaling exponent, not just its level.
- **Core Hypothesis (falsifiable):** Rare classes improve their robustness more slowly with scale (flatter exponents), meaning scaling widens the head-tail robustness gap.
- **Minimal Experiment:** Evaluate a scale ladder per class across corruption severities; fit per-class exponents; regress on frequency.
- **Main Risk:** Per-class exponent fits are noisy; needs class-group aggregation.
- **Research Cluster:** LONG-TAIL / ROBUSTNESS / PHENOMENON

### IDEA-B-M-0012 — Dataset provenance ledger with measured inheritance (parents: 0156, 0246)
- **One-sentence idea:** Define a dataset release standard recording model-assistance provenance, plus a measurable bias-inheritance score computed from assistant-error fingerprints, and validate the score on datasets with known pipelines.
- **Core Hypothesis (falsifiable):** The inheritance score computed from release artifacts alone predicts blind-vs-assisted error-correlation measurements within useful error bars.
- **Minimal Experiment:** Validate on the controlled datasets produced in 0156's experiment; apply to public datasets with documented pipelines.
- **Main Risk:** Fingerprints of unknown assistant models may be unrecoverable, limiting retroactive application.
- **Research Cluster:** ANNOT-EFF / EVAL-WEAK

### IDEA-B-M-0013 — The cheap-first adaptation battery (parents: 0192, 0202)
- **One-sentence idea:** Bundle label-prior correction, normalization-statistics recalibration, and preprocessing harmonization (0270) into a mandatory "cheap-first" baseline battery, and re-baseline the domain adaptation literature against it.
- **Core Hypothesis (falsifiable):** The battery recovers the majority of the domain gap on standard DA benchmarks, and most published DA methods add no significant value beyond it.
- **Minimal Experiment:** Implement the battery; re-evaluate 8 DA methods on two benchmark pairs against battery-corrected baselines.
- **Main Risk:** Battery components interact; ordering/tuning of the stack needs principled specification.
- **Research Cluster:** CROSS-DOMAIN / NEG-RESULT

### IDEA-B-M-0014 — Quality-gated coverage-targeted generation (parents: 0222, 0247)
- **One-sentence idea:** Generate synthetic data only where real data is thin AND per-class generation quality is verified good, testing whether the intersection rule beats either criterion alone.
- **Core Hypothesis (falsifiable):** Intersection-gated generation dominates density-only and quality-only strategies at matched volume, because their failure modes (bad generations in thin regions; redundant good generations) are complementary.
- **Minimal Experiment:** Train under the three strategies at matched volume on one long-tail benchmark; compare per-class outcomes.
- **Main Risk:** Thin-region quality may be so poor that the intersection is nearly empty for the classes that matter.
- **Research Cluster:** SYNTH-DATA / LONG-TAIL

### IDEA-B-M-0015 — Harmonized compositing with exact masks (parents: 0227, 0241)
- **One-sentence idea:** Test whether diffusion-harmonized copy-paste (exact geometric masks, generative blending only for photometrics) dominates both plain copy-paste and full generative insertion.
- **Core Hypothesis (falsifiable):** Harmonized compositing retains copy-paste's label-exactness benefits while removing the artifact shortcut, beating both parents on real-instance generalization.
- **Minimal Experiment:** Three-arm training comparison with artifact-probe and real-vs-inserted evaluation from 0241.
- **Main Risk:** Harmonization may itself perturb boundary pixels, reintroducing label error at small scale.
- **Research Cluster:** SYNTH-DATA

### IDEA-B-M-0016 — Enter the statistics index in the transferability race (parents: 0253, 0267)
- **One-sentence idea:** Enter the frequency-statistics transferability index as a challenger in the predictive-validity benchmark of domain-distance measures, testing cheap-vs-learned predictors head-to-head.
- **Core Hypothesis (falsifiable):** The cheap index places in the top tier of the 0267 benchmark, outperforming FID-style measures at a tiny fraction of their compute.
- **Minimal Experiment:** Add the index to the 0267 evaluation matrix; report validity and compute cost per predictor.
- **Main Risk:** Wholly parasitic on 0267's matrix being built first.
- **Research Cluster:** CROSS-DOMAIN / EVAL-WEAK

### IDEA-B-M-0017 — Composing sensor adapters with environment vectors (parents: 0259, 0268)
- **One-sentence idea:** Test whether input-stem modality adapters (thermal) compose with parameter-space environment vectors (night, rain) to handle unseen sensor-environment combinations.
- **Core Hypothesis (falsifiable):** Adapter-plus-vector composition achieves most of jointly trained performance on unseen combinations, showing the two adaptation loci (input stem vs. weight delta) are independent and composable.
- **Minimal Experiment:** Train components separately on paired driving data; evaluate compositions on held-out combined conditions.
- **Main Risk:** Thermal-night interactions may be exactly where independence fails (hot objects at night differ qualitatively).
- **Research Cluster:** CROSS-DOMAIN / MULTIMODAL-SUP

### IDEA-B-M-0018 — The representation-property checkpoint selector (parents: 0296, 0306, 0348)
- **One-sentence idea:** Combine equivariance and semantic-depth profiles into a single checkpoint-selection score and run a prospective trial against score-based selection on new fine-tuning tasks.
- **Core Hypothesis (falsifiable):** Property-based selection picks better starting checkpoints than benchmark-score selection in a majority of prospective trials, with the largest margins on dense, boundary-critical targets.
- **Minimal Experiment:** Freeze the selector; run 10 pre-registered fine-tuning tasks; compare selected-checkpoint outcomes.
- **Main Risk:** Profiles cost compute to measure; the selector must beat the heuristic by enough to pay for itself.
- **Research Cluster:** REP-MISMATCH / CROSS-DOMAIN

### IDEA-B-M-0019 — The decomposed, protocol-controlled community harness (parents: 0316, 0322, 0342)
- **One-sentence idea:** Release one evaluation harness enforcing protocol standardization, error decomposition, and floor-adjustment (M-0001), then publish the re-ranked state of the field as a living document.
- **Core Hypothesis (falsifiable):** Under the harness, a substantial fraction of adjacent published orderings reverse or collapse into statistical ties, and component profiles reveal progress concentrated in recognition rather than localization.
- **Minimal Experiment:** Harness release plus a 30-model re-evaluation campaign on two benchmarks.
- **Main Risk:** Community adoption is social, not technical; the artifact must be trivially easier than the status quo.
- **Research Cluster:** EVAL-WEAK

### IDEA-B-M-0020 — Per-component checkpoint compositing (parents: 0130, 0337)
- **One-sentence idea:** Exploit phase-separated learning by compositing final models from phase-specific checkpoints (interior-optimal, boundary-optimal, tail-class-optimal) via weight averaging or output routing, capturing each component's peak.
- **Core Hypothesis (falsifiable):** Composited models beat any single checkpoint on the joint metric profile, recovering a meaningful share of the per-class/per-component oracle gains measured in the parent studies.
- **Minimal Experiment:** Identify component-optimal checkpoints from dense logging; test weight-averaging and routing composites against best-single-checkpoint baselines.
- **Main Risk:** Weight averaging across distant checkpoints can underperform both endpoints; routing adds inference cost.
- **Research Cluster:** PHENOMENON / LONG-TAIL

---

## Part 3 — Assumption-challenging ideas (IDEA-B-X-0001 .. IDEA-B-X-0010)

Deliberately contrarian, full-format ideas targeting accepted beliefs not already challenged above.

### IDEA-B-X-0001 — Challenge: "pixel masks are the right output abstraction"
- **One-sentence idea:** Test whether downstream tasks served by segmentation (measurement, grasping, editing, navigation) are better served by task-direct output heads, making the pixel mask an unnecessary and error-amplifying intermediate.
- **Problem:** The field optimizes mask fidelity as an end in itself, but every consumer converts masks into something else (a diameter, a grasp point, a matte, a costmap); the conversion step weights mask errors in ways mask metrics ignore entirely.
- **Core Hypothesis (falsifiable):** For a majority of surveyed downstream uses, end-to-end task heads trained at matched compute beat segmentation-then-convert pipelines, and the pipeline deficit is predicted by the mismatch between mask metrics and the conversion's error weighting.
- **Why Important:** If masks are a legacy intermediate rather than a necessary one, a large fraction of the field's optimization target is misdirected.
- **Why Possibly Novel:** End-to-end vs. modular is debated per application; the systematic cross-application audit framing segmentation itself as the questioned module is not done.
- **Minimal Experiment:** Implement matched direct-vs-pipeline systems for four downstream tasks; compare outcomes and attribute pipeline losses to metric-weighting mismatch.
- **Main Risk:** Masks retain advantages (auditable, reusable across tasks) that outcome metrics undervalue; the study must price modularity honestly.
- **Research Cluster:** ASSUMPTION / EVAL-WEAK

### IDEA-B-X-0002 — Challenge: "ground truth is the quality ceiling"
- **One-sentence idea:** Run blind tournaments where expert panels judge model predictions against original GT annotations without knowing which is which, testing whether current models already exceed average annotation quality on mainstream benchmarks.
- **Problem:** All evaluation assumes GT superiority, but if models now beat the average annotator, benchmarks measure agreement-with-noise, and "progress" beyond that point is actively misleading (interacts with 0331 but poses the stronger, model-superiority claim).
- **Core Hypothesis (falsifiable):** On mature natural-image benchmarks, blinded experts prefer model output over original GT in a substantial fraction of instances (approaching or exceeding half for top models), with preference concentrated in boundary precision and missed-instance recall.
- **Why Important:** A confirmed crossover inverts the evaluation paradigm: models should be judged by adjudication protocols, not GT agreement, from that point onward.
- **Why Possibly Novel:** Model-vs-human comparisons exist for classification; the blinded mask-quality tournament on standard benchmarks has not been run.
- **Minimal Experiment:** Sample 2,000 instances from two benchmarks; render model-vs-GT pairs blinded and order-randomized; collect expert preferences with decoy calibration.
- **Main Risk:** Expert preference may reward plausible smoothness over fidelity to the true scene; needs physical-evidence anchors (zoom, multi-view) where possible.
- **Research Cluster:** ASSUMPTION / EVAL-WEAK / ANNOT-EFF

### IDEA-B-X-0003 — Challenge: "standard augmentation is harmless"
- **One-sentence idea:** Inventory the invariances injected by default augmentation stacks (flips, scale jitter, color jitter) and demonstrate task families where each injected invariance is provably wrong and measurably harmful.
- **Problem:** Augmentation defaults encode invariance assumptions (chirality doesn't matter, absolute scale doesn't matter, color doesn't matter) that are false for real tasks — medical laterality, physical size estimation, material identification — yet stacks are copied verbatim into those domains.
- **Core Hypothesis (falsifiable):** For each default augmentation, there exist mainstream task families where its removal or inversion improves performance by margins larger than typical method gains, and the harm is predictable from a task-property checklist (does the task depend on chirality/scale/color as signal?).
- **Why Important:** Converts augmentation from copied ritual into a task-conditional decision with a published decision checklist — preventing silent damage across applied domains.
- **Why Possibly Novel:** Individual cases (flip harm in medical) are known anecdotally; the systematic inventory with a validated checklist is not.
- **Minimal Experiment:** For four default augmentations, run with/without arms on tasks predicted harmed vs. predicted safe; validate the checklist's predictions.
- **Main Risk:** Harms may be dataset-size-dependent (augmentation helps small data even when invariance is wrong), demanding size-crossed designs.
- **Research Cluster:** ASSUMPTION / GENERALIZATION

### IDEA-B-X-0004 — Challenge: "bigger label vocabularies make the task harder"
- **One-sentence idea:** Test whether enlarging the label vocabulary improves per-class segmentation accuracy on the original classes, because finer distinctions sharpen decision boundaries and mutual-exclusion structure adds constraints.
- **Problem:** Vocabulary size is treated as pure difficulty (more confusion possibilities), driving ontology minimalism in dataset design; but finer labels may act as auxiliary supervision that disambiguates coarse classes (echoing 0170 at the model level rather than the annotator level).
- **Core Hypothesis (falsifiable):** Models trained on fine vocabularies and evaluated after merging to a coarse vocabulary outperform models trained directly on the coarse vocabulary at matched data, with gains concentrated on classes whose fine-grained children have distinct contexts or appearances.
- **Why Important:** Would reverse a dataset-design default, arguing for maximal ontologies with post-hoc merging as the standard.
- **Why Possibly Novel:** Fine-to-coarse transfer is studied in classification; the segmentation-training recommendation with mechanism analysis (which classes benefit) is not established.
- **Minimal Experiment:** Train fine-vs-coarse vocabulary arms on datasets with hierarchical labels; compare merged-evaluation accuracy per coarse class.
- **Main Risk:** Fine labels cost annotation accuracy (taxonomy errors), which may offset the modeling benefit outside curated datasets.
- **Research Cluster:** ASSUMPTION / LONG-TAIL

### IDEA-B-X-0005 — Challenge: "image-level random splits produce valid test sets"
- **One-sentence idea:** Demonstrate that image-level random splitting leaks scene-level information (same location, session, or subject across splits) in most dense-prediction benchmarks, and quantify the inflation by re-evaluating under scene-blocked splits.
- **Problem:** Dense datasets are collected in sessions (video frames, photo bursts, one hospital's patients); image-level splits place near-identical content on both sides, so benchmarks measure interpolation within scenes while claiming generalization across them.
- **Core Hypothesis (falsifiable):** Scene-blocked re-splitting reduces measured performance on several benchmarks by margins exceeding typical method gains, with the reduction predicted by each dataset's session-clustering statistics — and method rankings compress or reorder under blocked splits.
- **Why Important:** Split methodology is more fundamental than any metric choice; demonstrated leakage would require re-baselining affected literatures (generalizes the geographic case of 0136 and temporal case of 0211).
- **Why Possibly Novel:** Blocked splitting is standard in other empirical sciences; the systematic vision-benchmark audit with inflation quantification is missing.
- **Minimal Experiment:** Reconstruct session structure via metadata/near-duplicate clustering for four benchmarks; retrain representative models under blocked splits; compare against canonical numbers.
- **Main Risk:** Session reconstruction is imperfect without collection metadata; conservative and aggressive blocking must bracket the truth.
- **Research Cluster:** ASSUMPTION / EVAL-WEAK

### IDEA-B-X-0006 — Challenge: "decoders are necessary"
- **One-sentence idea:** Test whether learned decoders add anything beyond coordinate-conditioned readout of frozen encoder features at matched compute — treating the entire decoder design space as a null-hypothesis candidate.
- **Problem:** Decades of decoder engineering assume progressive upsampling machinery is required; if a minimal coordinate-based readout (query any pixel's label from encoder features plus position) matches elaborate decoders, the design space is vestigial and the field's decoder effort is misallocated.
- **Core Hypothesis (falsifiable):** At matched compute and output resolution, coordinate-readout heads on modern encoders come within noise of heavyweight decoders on interior metrics, with any residual decoder advantage confined to boundary detail — bounding what decoders actually contribute.
- **Why Important:** Either collapses a major architecture-design industry into a simple default or produces the first clean measurement of what decoding machinery uniquely provides.
- **Why Possibly Novel:** Implicit/coordinate readouts exist in niches; positioning them as the null model for decoder value, with a bounding analysis, is a different scientific use.
- **Minimal Experiment:** Train coordinate-readout vs. representative decoders on frozen and end-to-end encoders; decompose metric differences by region type.
- **Main Risk:** End-to-end training may let decoders shape encoder features (their real value), requiring the frozen/unfrozen contrast to detect it.
- **Research Cluster:** ASSUMPTION / REP-MISMATCH

### IDEA-B-X-0007 — Challenge: "annotation consensus improves labels"
- **One-sentence idea:** Test whether consensus aggregation of multiple annotations produces worse training signal than the single best annotator's labels, because averaging destroys the coherent geometry of individual annotations.
- **Problem:** Multi-annotator pipelines aggregate by majority/averaging on the assumption that consensus approaches truth; but masks are structured objects — averaging plausible-but-different segmentations can produce geometrically incoherent labels worse than any contributor (unlike averaging scalar labels).
- **Core Hypothesis (falsifiable):** Models trained on best-single-annotator labels (selected by held-out agreement) outperform models trained on consensus-aggregated labels at matched annotation budget, with the consensus deficit concentrated in boundary geometry and thin structures.
- **Why Important:** Would invert a standard aggregation practice and redirect multi-annotation budgets from redundant labeling toward annotator selection and disagreement capture (per 0178).
- **Why Possibly Novel:** Aggregation methods are compared against each other; the aggregation-vs-selection question with geometric-coherence analysis is unexamined for masks.
- **Minimal Experiment:** On multi-annotated datasets, train consensus vs. selected-annotator arms; compare decomposed metrics; analyze coherence statistics of the label sets.
- **Main Risk:** Best-annotator selection needs its own held-out data, which must be charged against its budget in the comparison.
- **Research Cluster:** ASSUMPTION / ANNOT-EFF

### IDEA-B-X-0008 — Challenge: "evaluate at a fixed resolution"
- **One-sentence idea:** Reframe inference resolution as a test-time parameter (like an operating point) and require full resolution-performance curves in evaluation, testing whether single-resolution reporting systematically misranks methods.
- **Problem:** Every model has a resolution-performance curve with different shape (per 0036), yet benchmarks compare single points chosen by authors; two methods can each "beat" the other at their chosen resolutions, and deployment picks resolutions by latency budgets papers never report against.
- **Core Hypothesis (falsifiable):** Across public models, pairwise ranking flips as a function of evaluation resolution are common, and curve-based comparison (dominance analysis across the resolution-latency plane) yields materially different method recommendations than point comparison.
- **Why Important:** Converts an arbitrary hidden choice into a reported dimension, aligning benchmark practice with how deployments actually select operating points.
- **Why Possibly Novel:** Speed-accuracy curves exist for efficiency papers; mandatory resolution-curve evaluation as a general ranking methodology with flip-rate measurement is not established.
- **Minimal Experiment:** Evaluate 20 models across dense resolution sweeps; count pairwise ranking flips; publish curve-based dominance analysis vs. reported point comparisons.
- **Main Risk:** Some architectures cannot honestly run off their design resolution, requiring per-model validity ranges on the curves.
- **Research Cluster:** ASSUMPTION / EVAL-WEAK

### IDEA-B-X-0009 — Challenge: "matching human annotation is the goal"
- **One-sentence idea:** Construct physically grounded evaluation (multi-view consistency, depth-edge agreement, temporal coherence of the real scene) as an alternative gold standard, and test whether models optimized toward human GT diverge from physical truth in measurable, correctable ways.
- **Problem:** Human annotation carries systematic perceptual biases (per 0061, 0185); optimizing agreement with it optimizes toward those biases, capping models at human-perceptual truth rather than physical truth — which measurement applications actually need.
- **Core Hypothesis (falsifiable):** On scenes with physical reference structure (calibrated multi-view, LiDAR), model-GT agreement and model-physics agreement dissociate measurably, top models already exceed their GT's physical accuracy in identifiable respects, and physics-anchored fine-tuning improves measurement-task performance while slightly reducing GT agreement.
- **Why Important:** Establishes a second, bias-independent evaluation axis and demonstrates that "worse on the benchmark" can mean "better in reality" — a foundational correction for measurement-grade vision.
- **Why Possibly Novel:** Physical validation exists in photogrammetry; importing it as a systematic gold-standard alternative for semantic segmentation evaluation is new.
- **Minimal Experiment:** Assemble a physically instrumented evaluation set; score public models on both axes; run the physics-anchored fine-tuning arm on a measurement task.
- **Main Risk:** Physical references cover geometry better than semantics; the alternative standard may only apply to boundary/extent aspects.
- **Research Cluster:** ASSUMPTION / EVAL-WEAK / BOUNDARY

### IDEA-B-X-0010 — Challenge: "occlusion is a nuisance"
- **One-sentence idea:** Treat occlusion structure as signal rather than noise — test whether requiring models to predict occlusion relations (who occludes whom) as a primary output improves standard segmentation itself, because occlusion supervises depth ordering and boundary ownership for free.
- **Problem:** Pipelines treat occlusion as degradation to be robust against, discarding the rich relational structure it encodes; boundary-ownership errors (per 0070) and amodal inconsistencies (per 0185) both trace to models never being asked to represent the occlusion graph.
- **Core Hypothesis (falsifiable):** Adding occlusion-relation prediction (derivable from existing panoptic GT overlaps plus video parallax at no new annotation cost) improves modal segmentation's boundary-ownership accuracy and contact-boundary quality beyond matched-compute controls, with gains concentrated exactly where the occlusion graph is dense.
- **Why Important:** Reframes a universally negative concept as free supervision, unifying several observed failure modes (ownership, amodal confusion, contact boundaries) under one missing output structure.
- **Why Possibly Novel:** Occlusion-order prediction exists in layout niches; its use as auxiliary supervision to improve standard segmentation, with cost-free label derivation, is untested as a general claim.
- **Minimal Experiment:** Derive occlusion-relation labels from existing GT and video; train with/without the relational head; evaluate ownership-stratified boundary metrics.
- **Main Risk:** Derived occlusion labels are noisy at exactly the contested boundaries, potentially capping the auxiliary signal's value.
- **Research Cluster:** ASSUMPTION / BOUNDARY / MULTIMODAL-SUP

---

## Part 4 — Near-duplicate notes (within Batch B)

These groups are related-but-distinct; each entry states the distinction that justifies keeping members separate. Stage-2 reviewers may merge where the distinction doesn't survive scrutiny.

1. **0014 / 0093 / M-0002 — size-conditional score correction.** 0014 targets AP ranking effects; 0093 targets probability calibration semantics; M-0002 is the merged deliverable. Merge candidates if Stage 2 finds the two lenses inseparable.
2. **0003 / 0031 / 0047 / 0184 / 0331 / M-0001 — GT-noise and GT-error family.** Distinct axes: box jitter (0003), polygon smoothing (0031), boundary disagreement floors (0047), relabeling ranking fragility (0184), adjudicated GT-error share (0331). Same instrumentation could serve all five.
3. **0007 / 0032 / 0338 / 0216 / M-0003 — context reliance.** 0007 = evidence ablation; 0032 = shift tradeoff; 0338 = value-radius mapping; 0216 = non-local edit sensitivity. Overlapping stimuli, different measurements.
4. **0017 / 0037 / 0144 / 0158 / 0167 / M-0006 — missing annotations.** Missed-GT-as-FP (0017), tool floor (0037), background contamination (0144), assistant blind spots (0158), review recall bias (0167). Shared verification protocols.
5. **0075 / 0089 / 0101 / 0107 / M-0004 — trivial-baseline critique of UQ.** Boundary-distance confound (0075), gameable benchmarks (0089), sensitivity baseline (0101), universal confidence profile (0107). One residualized protocol serves all.
6. **0076 / 0090 / 0095 / 0097 — ensemble mechanics.** Value decomposition (0076), diversity sources (0090), TTA-vs-dropout (0095), checkpoint substitution (0097). Distinct hypotheses over shared training grids.
7. **0080 / 0275 — calibration under shift.** 0080 removes the accuracy confound from the degradation claim; 0275 poses relative invariance of calibration vs. accuracy. Opposite emphases; results must be reconciled.
8. **0084 / 0153 / 0165 / 0175 — annotation targeting audits.** Acquisition functions (0084), granularity (0153), thresholds (0165), review targeting (0175). All strong-baseline audits in labeling workflows.
9. **0128 / 0278 / 0201 / 0226 / 0244 / 0321 / 0330 / M-0010 — pretraining-corpus statistics and contamination.** Frequency-as-covariate (0128, 0278), robustness attribution (0201), generative leakage (0226), value-era dependence (0244), capacity-dependent inflation (0321), method-level audit (0330). Shared corpus-proximity tooling; distinct claims.
10. **0125 / 0131 / 0326 — rare-class hallucination.** Metric incentive (0125), method side-effect (0131), missing evaluation axis (0326). Three layers of one phenomenon.
11. **0190 / 0193 / 0209 / 0224 / 0230 — sensor/pipeline realism.** Weather validity (0190), ISP-variation benchmark (0193), night decomposition (0209), synthetic sensor noise (0224), optics vs. materials (0230). All argue low-level capture physics is underweighted; different arenas.
12. **0223 / 0249 — layout vs. style.** 0223 manipulates generation; 0249 measures decomposition on existing pairs. Method-vs-measurement complement.
13. **0036 / 0322 / 0327 / 0335 / X-0008 — protocol and nuisance normalization.** Resolution law (0036), protocol re-run (0322), hardware normalization (0327), nondeterminism floor (0335), resolution-curve reporting (X-0008). A coherent "evaluation hygiene" program.
14. **0066 / 0344 — spatial position audits.** 0066 = boundary quality vs. radial position; 0344 = recall/quality at image borders with cause attribution. Merge candidate under "field-position bias."
15. **0020 / 0346 — TTA skepticism.** 0020 = training-coverage substitutability; 0346 = component/shift harm map. Same tool, different failure axes.
16. **0162 / 0182 / 0183 / M-0007 — sparse supervision design.** Partial boundaries (0162), density law (0182), ambiguity marks (0183). Complementary supervision-budget science.
17. **0041 / 0051 / 0063 / 0169 / 0177 — annotation-style fingerprints.** Style overfitting (0041), style transfer failure (0051), zoom protocol (0063), incentive geometry (0169), tool parameters (0177). One "GT forensics" toolkit.
18. **0016 / 0038 — size-adaptive metrics.** 0016 = detection IoU thresholds; 0038 = mask metric reliability. Same principle, different metric families.
19. **0225 / 0238 / 0242 — synthetic evaluation validity.** General ranking preservation (0225), safety-hazard specificity (0238), overfitting instrument (0242).
20. **0296 / 0306 / 0348 / M-0018 — representation-property predictors of transfer.** Equivariance (0296), semantic depth (0306), heuristic audit (0348), combined selector (M-0018).
21. **0009 / 0029 / 0035 — size-conditional loss allocation.** Loss share (0009), focal gamma (0029), label smoothing (0035): three probes of "one loss setting taxes minority regimes"; keep separate only if mechanisms dissociate.
22. **0156 / 0246 / M-0012 — annotation feedback loops.** Pipeline-level (0156) vs. ecosystem-level (0246) vs. standardization (M-0012).
23. **0068 / 0162 — boundary evidence extrapolation.** 0068 is the mechanism probe; 0162 is the protocol exploit. Ordered dependency, not duplication.
24. **0136 / 0211 / X-0005 — split leakage family.** Geographic (0136), temporal (0211), scene/session blocking (X-0005, the general case). X-0005 subsumes the others if resources force a merge.
25. **Cross-batch caution:** Batch A (methods/SAM/medical/domain-shift failures) and Batch C (negative results/confounders/training dynamics) plausibly contain neighbors for: 0045 (CRF revival), 0140/0195/0250/0266 (negative-result audits), 0197/0130/0337 (training dynamics), 0251/0266/0271 (medical transfer), and the evaluation-hygiene family (13). Supervisor-side dedup against those batches is required at ingest; within-batch IDs above are the anchors to compare against.

---

**End of Batch B.** Totals: 350 primary ideas (IDEA-B-0001..IDEA-B-0350), 20 mutations (IDEA-B-M-0001..0020), 10 assumption-challenging ideas (IDEA-B-X-0001..0010), 25 near-duplicate note groups.
