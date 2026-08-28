# Windows2 Stage 1 - Agent C Idea Catalog

Detection, evaluation science, robustness, unproven assumptions, and negative-result-driven research in computer vision.

- Total ideas: **345** (IDs `W2-C-0001` ... `W2-C-0345`)
- Machine-readable source of truth: `ideas.jsonl` (one JSON object per idea, identical content)
- Cluster overview: `clusters.md`

**Standing integrity note:** every idea below is an original proposal drafted without a literature search; novelty of each idea is UNVERIFIED - needs lit search before any is pursued. No citations or empirical results are asserted as fact anywhere in this catalog; empirical statements inside hypotheses are predictions to be tested, not claims. Ideas carrying an additional specific presumption about prior work are individually flagged in their Notes field.

Each idea states: the **problem**, a **falsifiable hypothesis**, and the **cheapest experiment** that could refute or support it.

## Cluster 1: Object detection limitations (W2-C-0001 - W2-C-0040, 40 ideas)

### W2-C-0001 - Open-vocab rare-class AP driven by text-prior frequency, not visual grounding

- **Problem:** Open-vocabulary detectors report strong rare-class AP, but rare-class scores may be predicted by how often the class name appears in pretraining captions rather than by visual evidence quality.
- **Falsifiable hypothesis:** Across LVIS rare classes, per-class AP of open-vocab detectors is better predicted by caption-corpus name frequency than by any visual difficulty measure (object size, occlusion rate); partialling out name frequency removes most of the claimed rare-class advantage.
- **Cheapest experiment:** Take 2-3 public open-vocab detectors, compute per-class AP on LVIS val, regress against LAION/CC caption frequency of class names vs visual difficulty covariates; no training required, one GPU-day of inference.
- **ROI estimate:** high
- **Notes:** UNVERIFIED - needs lit search on existing frequency-vs-AP analyses.

### W2-C-0002 - Small-object gains from resolution are sampling-density artifacts

- **Problem:** Raising input resolution improves small-object AP, but it is unclear whether gains come from better features or simply from denser anchor/query sampling relative to object size.
- **Falsifiable hypothesis:** At fixed input resolution, increasing head sampling density (smaller strides, more queries) recovers the majority of the small-object AP gain attributed to higher resolution.
- **Cheapest experiment:** Train one detector at 640px with stride-4 head vs 1280px with stride-8 head (matched effective sampling), compare AP-small on COCO; two training runs.
- **ROI estimate:** medium

### W2-C-0003 - Oracle-NMS ceiling: how much of crowded-scene error is suppression, not detection

- **Problem:** In crowded scenes it is unknown what fraction of misses are caused by duplicate suppression (NMS and its learned variants) versus the detector never firing on the instance.
- **Falsifiable hypothesis:** On CrowdHuman, replacing NMS with an oracle that keeps exactly the best-matching prediction per ground-truth instance recovers a large fraction (operationally, more than a third) of missed recall, showing suppression is the dominant bottleneck.
- **Cheapest experiment:** Run pretrained detectors on CrowdHuman, compare standard NMS output vs oracle suppression using GT matching; inference-only, under one GPU-day.
- **ROI estimate:** high

### W2-C-0004 - Synthetic occluders overestimate real occlusion robustness

- **Problem:** Occlusion robustness is often benchmarked with pasted synthetic occluders, but real occlusions have correlated geometry, shadows, and depth ordering that synthetic paste-ins lack.
- **Falsifiable hypothesis:** Detector robustness measured with synthetic occluder paste-ins overestimates robustness on naturally occluded instances by a measurable margin, and the two rankings of detectors disagree.
- **Cheapest experiment:** Build a small paired eval: naturally occluded instances (using COCO/CrowdHuman occlusion flags) vs synthetic paste-in occlusions of matched coverage fraction; evaluate 5 pretrained detectors, inference only.
- **ROI estimate:** medium

### W2-C-0005 - Temporal aggregation in video detectors mostly re-ranks confidence, not fixes localization

- **Problem:** Video object detectors claim gains from temporal feature aggregation, but the mechanism of the gain (better boxes vs better scores vs recovered misses) is rarely decomposed.
- **Falsifiable hypothesis:** For representative video detectors on ImageNet-VID, removing temporal aggregation at inference changes confidence ranking of already-detected boxes far more than it changes box coordinates or recovers new instances.
- **Cheapest experiment:** Take one public video detector, log per-frame predictions with and without aggregation, decompose the AP delta into score-change, box-change, and new-detection components; inference only.
- **ROI estimate:** medium

### W2-C-0006 - Open-vocab detectors fail on negated and attribute-composed prompts

- **Problem:** Open-vocabulary detection is marketed as free-form language grounding, but prompts with negation ('dog without leash') or attribute composition ('red car with open door') may be silently reduced to bag-of-words matching.
- **Falsifiable hypothesis:** Open-vocab detectors score no better than a bag-of-words control (same prompt with word order shuffled and negations dropped) on a negation/composition test suite.
- **Cheapest experiment:** Construct 200 image-prompt pairs with negations and compositions from Visual Genome attributes, evaluate 3 public open-vocab detectors against shuffled-prompt controls; annotation of 200 pairs plus inference.
- **ROI estimate:** medium

### W2-C-0007 - The annotation-noise floor for tiny objects: is sub-16px AP meaningful

- **Problem:** Papers report AP improvements on tiny objects, but human annotators may disagree so much on sub-16px boxes that reported model differences sit inside the label-noise floor.
- **Falsifiable hypothesis:** Inter-annotator box agreement (mean IoU) for objects under 16px falls below the 0.5 IoU matching threshold, implying AP on this stratum measures annotation style more than detection quality.
- **Cheapest experiment:** Re-annotate 300 tiny-object instances from COCO/VisDrone with 3 annotators each, compute inter-annotator IoU distribution, compare with model-vs-GT IoU distribution; small annotation budget, no training.
- **ROI estimate:** high

### W2-C-0008 - Detection AP saturates where counting error explodes: density-conditioned evaluation

- **Problem:** Detection metrics are computed pooled over densities, hiding that per-image count error grows sharply with instance density even when AP looks flat.
- **Falsifiable hypothesis:** On CrowdHuman and VisDrone, relative count error of standard detectors grows superlinearly with GT instance count while pooled AP changes little, so AP is a misleading proxy for counting-type deployments.
- **Cheapest experiment:** Stratify existing val predictions of 5 pretrained detectors by GT count deciles, plot AP and MAE-of-count per stratum; pure re-evaluation of cached predictions.
- **ROI estimate:** medium

### W2-C-0009 - Tiling for small objects: gains vs boundary double-counting

- **Problem:** Test-time tiling is the default trick for small-object detection in aerial imagery, but its accounting of objects that straddle tile boundaries is ad hoc and may inflate or deflate AP depending on the merge rule.
- **Falsifiable hypothesis:** A significant share of the AP delta between tiling configurations is explained purely by boundary-object merge policy rather than by detection quality; a boundary-aware oracle merge changes tiling method rankings.
- **Cheapest experiment:** On VisDrone/DOTA val, run one detector with 3 tile sizes and 3 merge policies, decompose AP differences into interior vs boundary strata; inference only.
- **ROI estimate:** medium

### W2-C-0010 - Truncation vs occlusion: two conflated failure modes

- **Problem:** Objects cut by the image border (truncation) and objects hidden by other objects (occlusion) are usually pooled in robustness analyses although the model faces different information structure in each case.
- **Falsifiable hypothesis:** Detectors show systematically different error types for truncated vs occluded instances at matched visible-area fraction: truncation mainly harms box regression while occlusion mainly harms classification confidence.
- **Cheapest experiment:** Use datasets with truncation/occlusion flags (KITTI, CrowdHuman), match instances on visible fraction, compare localization error vs score distributions for 3 detectors; re-evaluation only.
- **ROI estimate:** medium

### W2-C-0011 - Prompt-engineering variance exceeds architecture deltas in open-vocab detection

- **Problem:** Open-vocab detection papers compare architectures while quietly using different prompt templates, so the community may be ranking prompt engineering rather than methods.
- **Falsifiable hypothesis:** Across a grid of reasonable prompt templates, the within-method AP spread on LVIS/ODinW is larger than the between-method spread reported in recent papers.
- **Cheapest experiment:** Evaluate 3 public open-vocab detectors under 10 published prompt templates each on ODinW-13; inference-only grid, a few GPU-days.
- **ROI estimate:** high

### W2-C-0012 - Frame-level metrics hide flicker: temporal stability as a first-class detection metric

- **Problem:** Video detection is evaluated with per-frame mAP, which is blind to prediction flicker that dominates user-perceived and downstream-tracking quality.
- **Falsifiable hypothesis:** A temporal stability metric (identity-consistent detection persistence across adjacent frames) reorders published video detectors relative to their frame-mAP ranking, i.e. frame mAP and stability are only weakly rank-correlated.
- **Cheapest experiment:** Define stability as fraction of GT tracks with contiguous detection coverage, evaluate 5 public detectors on ImageNet-VID/OVIS val, compare rankings; inference and metric code only.
- **ROI estimate:** high

### W2-C-0013 - Small objects are detected from context, not appearance

- **Problem:** It is unknown whether detectors recognize tiny objects from their own pixels or from surrounding scene context, which changes how small-object research should be prioritized.
- **Falsifiable hypothesis:** For objects under 24px, replacing the object interior with matched-statistics noise reduces detection recall by less than replacing the surrounding context ring, i.e. context carries more decision evidence than the object itself.
- **Cheapest experiment:** Counterfactual masking study on 500 COCO/VisDrone small instances: inpaint object vs inpaint context ring, measure recall deltas for 3 pretrained detectors; inference plus cheap inpainting.
- **ROI estimate:** high

### W2-C-0014 - Amodal vs modal box conventions silently corrupt cross-dataset evaluation

- **Problem:** Datasets differ in whether boxes cover the visible region (modal) or the inferred full extent (amodal) of occluded objects, and cross-dataset evaluations ignore this label-convention shift.
- **Falsifiable hypothesis:** A detector trained on modal-convention data loses AP on amodal-convention test sets primarily through localization mismatch on occluded instances, and a simple convention-translation layer recovers most of the gap.
- **Cheapest experiment:** Cross-evaluate detectors between KITTI (amodal tendencies) and COCO-style modal data on occluded strata, then fit a per-class box scaling correction and re-measure; inference plus a linear fit.
- **ROI estimate:** medium
- **Notes:** UNVERIFIED - needs lit search on convention audits.

### W2-C-0015 - Confidence calibration collapses as instance count grows

- **Problem:** Calibration of detector confidences is usually reported pooled over images; crowded images may be systematically miscalibrated, which matters for counting and safety uses.
- **Falsifiable hypothesis:** Expected calibration error of matched detections grows monotonically with per-image instance count, and per-density recalibration yields better deployment thresholds than global recalibration.
- **Cheapest experiment:** Bin existing val predictions by GT density, compute calibration curves per bin for 3 detectors on CrowdHuman; re-evaluation only.
- **ROI estimate:** medium

### W2-C-0016 - Open-vocab detectors inherit bag-of-words behavior on spatial-relation prompts

- **Problem:** CLIP-like text encoders are known to behave like bag-of-words on relations; whether detection heads built on them inherit this failure for prompts like 'cup on the left of the laptop' is untested at detection granularity.
- **Falsifiable hypothesis:** Open-vocab detectors localize the correct relation argument no better than chance between the two candidate objects when the prompt specifies a spatial relation.
- **Cheapest experiment:** Build 300 two-object relation prompts from Visual Genome relations, test whether the top box matches the relation-specified instance vs the distractor; inference only.
- **ROI estimate:** medium

### W2-C-0017 - Extreme aspect ratios: wires, poles, and the IoU-anchor blind spot

- **Problem:** Very elongated objects (cables, rails, poles) are poorly served both by IoU matching (thin structures get near-zero IoU under small offsets) and by anchor/query priors, yet they matter for inspection and AV domains.
- **Falsifiable hypothesis:** For objects with aspect ratio above 10:1, match rate under IoU 0.5 is dominated by annotation and matching geometry rather than by detector quality: perturbing GT boxes by one pixel width changes AP more than swapping detectors.
- **Cheapest experiment:** On a wire/pole subset (from TTPLA or similar public data), measure AP sensitivity to 1-2px GT perturbations vs detector swaps; re-evaluation only.
- **ROI estimate:** medium

### W2-C-0018 - Motion-blur-stratified evaluation for video detection

- **Problem:** Video detectors are trained and evaluated on frames sampled without regard to motion blur, so reported AP hides a blur-conditional failure mode central to real video.
- **Falsifiable hypothesis:** AP conditioned on estimated per-frame blur magnitude declines steeply for image-pretrained detectors, and this decline, not average AP, predicts which detectors win on high-motion deployment footage.
- **Cheapest experiment:** Estimate blur (variance-of-Laplacian or optical-flow magnitude) on ImageNet-VID val frames, stratify AP for 4 detectors; re-evaluation only.
- **ROI estimate:** medium

### W2-C-0019 - Copy-paste augmentation gains: appearance learning or label rebalancing

- **Problem:** Copy-paste augmentation improves detection and segmentation, but the mechanism (more minority-class instances vs new appearance contexts) is unresolved, which determines whether cheaper resampling suffices.
- **Falsifiable hypothesis:** Class-frequency-matched resampling of whole images recovers the majority of copy-paste AP gains, showing rebalancing, not novel composition, is the active ingredient.
- **Cheapest experiment:** Three matched training runs on COCO (baseline, copy-paste, frequency-matched resampling) with one mid-size detector; three training runs on a modest budget.
- **ROI estimate:** medium
- **Notes:** UNVERIFIED - needs lit search on existing copy-paste ablations.

### W2-C-0020 - Zero-shot claims and caption leakage: measuring test-class exposure in pretraining

- **Problem:** Open-vocab detectors claim zero-shot generalization to held-out classes, but pretraining caption corpora likely contain those class names with images, making 'zero-shot' an exposure-frequency statement rather than a capability claim.
- **Falsifiable hypothesis:** Per-class zero-shot AP correlates strongly with the count of pretraining captions containing the class name, and truly unexposed synthetic class names (novel coinages bound to visual concepts) show near-zero transfer.
- **Cheapest experiment:** For one open detector with public pretraining data, count caption matches per held-out class and correlate with AP; then test 20 invented-name classes via prompt-tuned references; mostly counting plus inference.
- **ROI estimate:** high

### W2-C-0021 - Synonym collisions in open-vocab NMS: person vs pedestrian

- **Problem:** Open-vocab detectors run class-wise NMS over user-supplied vocabularies; synonymous or overlapping class names (person, pedestrian, human) create duplicate boxes that closed-set evaluation never sees.
- **Falsifiable hypothesis:** Adding synonyms of existing classes to the inference vocabulary measurably degrades effective precision because duplicates survive class-wise suppression, and class-agnostic NMS over text-embedding clusters repairs most of the damage.
- **Cheapest experiment:** Evaluate 2 open-vocab detectors on COCO with vocabulary augmented by 2 synonyms per class, measure duplicate rate and AP under class-wise vs embedding-clustered NMS; inference only.
- **ROI estimate:** medium

### W2-C-0022 - Visible-fraction confounds in reported occlusion robustness

- **Problem:** Occlusion robustness comparisons rarely control for visible-area fraction, so a method may look occlusion-robust simply because its evaluation instances are less occluded.
- **Falsifiable hypothesis:** After matching instances on visible fraction, published occlusion-robustness gaps between representative methods shrink substantially, and some method orderings reverse.
- **Cheapest experiment:** Use amodal datasets (KINS, COCOA) to bin instances by visible fraction and re-evaluate 4 detectors within bins; re-evaluation only.
- **ROI estimate:** medium

### W2-C-0023 - The impossibility zone: objects smaller than effective stride

- **Problem:** There should exist an object-size regime where detection is information-theoretically crippled by feature stride and antialiasing, but this zone has not been mapped empirically as a function of architecture.
- **Falsifiable hypothesis:** Recall falls to near-zero when object size drops below a constant multiple of the finest feature stride, and this breakpoint is predicted by architecture geometry rather than training data volume.
- **Cheapest experiment:** Synthetic controlled dataset with objects of parametric size on real backgrounds; evaluate detectors with strides 4/8/16 without retraining where possible and with short finetunes otherwise; small compute.
- **ROI estimate:** medium

### W2-C-0024 - Density distribution shift between train and test in crowded benchmarks

- **Problem:** Crowded-scene benchmarks may have different density distributions in train vs test, so models implicitly tuned to train-set density profiles get flattering scores that do not reflect density generalization.
- **Falsifiable hypothesis:** Reweighting the CrowdHuman test set to alternative density profiles (uniform over density deciles) changes the ranking of published detectors.
- **Cheapest experiment:** Compute density histograms of train/test, re-weight per-image AP contributions of 5 detectors under uniform-density weighting; pure re-analysis.
- **ROI estimate:** medium

### W2-C-0025 - Error decomposition for video detection mAP: association vs detection

- **Problem:** Video detection scores mix per-frame detection failures with temporal inconsistency, and no standard decomposition tool attributes the loss between them.
- **Falsifiable hypothesis:** For modern video detectors, the majority of the gap to oracle performance comes from temporally inconsistent confidence (same object, fluctuating score) rather than from frames where the object is entirely missed.
- **Cheapest experiment:** Implement an oracle that stabilizes scores along GT tracks (max-pooled confidence) and measure the mAP recovered vs an oracle that fills fully-missed frames; inference-only analysis on ImageNet-VID.
- **ROI estimate:** medium

### W2-C-0026 - Detectors cannot say 'nothing here': rejection of undetectable prompts

- **Problem:** Open-vocab detectors are always evaluated on prompts that exist in the image; their behavior when the queried class is absent (the everyday deployment case) is unmeasured.
- **Falsifiable hypothesis:** Given prompts for absent classes, open-vocab detectors produce above-threshold false detections at rates that make them unusable for verification-style tasks, and the false-fire rate is uncorrelated with their standard AP.
- **Cheapest experiment:** Query 3 detectors with 50 absent-class prompts per image over 1,000 COCO images, measure false-fire rate vs prompt semantic distance to image content; inference only.
- **ROI estimate:** high

### W2-C-0027 - Aerial vs natural small objects: one scaling law does not fit both

- **Problem:** Small-object methods validated on COCO-small are assumed to transfer to aerial imagery, but the two regimes differ in context density, object orientation statistics, and background clutter.
- **Falsifiable hypothesis:** Method rankings on COCO-small and on VisDrone/DOTA small strata are only weakly rank-correlated, refuting the assumption that COCO-small is a proxy for aerial small-object detection.
- **Cheapest experiment:** Evaluate 6 public detectors on both small-object strata and compute rank correlation; inference only.
- **ROI estimate:** medium

### W2-C-0028 - Occlusion ordering as an unsupervised probe of detector 3D awareness

- **Problem:** Whether 2D detectors encode depth ordering of overlapping instances is unknown, yet it constrains what monocular pipelines can extract for free.
- **Falsifiable hypothesis:** A linear probe on frozen detector instance features predicts pairwise occlusion order significantly above chance, and probe accuracy correlates with the detector's crowded-scene AP.
- **Cheapest experiment:** Extract instance features for overlapping pairs on COCOA/KINS with known order, train a linear probe, correlate with crowded AP across 5 detectors; feature extraction plus logistic regression.
- **ROI estimate:** medium

### W2-C-0029 - Object permanence in long video: detectors plus trackers vs a Kalman baseline

- **Problem:** Modern detect-then-track stacks are assumed to handle temporary occlusion, but their object-permanence behavior over multi-second occlusions is rarely quantified against classical prediction.
- **Falsifiable hypothesis:** For occlusion gaps above 2 seconds, a constant-velocity Kalman coaster on last-seen boxes rehits reappearing objects at higher rates than the learned re-association of common tracker stacks.
- **Cheapest experiment:** On MOT17/DanceTrack val, extract occlusion gap events, compare re-acquisition rates of stock trackers vs a 50-line Kalman coaster; analysis only.
- **ROI estimate:** medium

### W2-C-0030 - Fixed query budgets impose an instance-count ceiling on DETR-family models

- **Problem:** Query-based detectors allocate a fixed number of object queries; their degradation profile as scene instance count approaches and exceeds the query budget is not systematically characterized.
- **Falsifiable hypothesis:** Recall of DETR-family detectors degrades sharply and superlinearly once GT count exceeds roughly half the query budget, at densities where dense-prediction detectors degrade gracefully.
- **Cheapest experiment:** Evaluate 3 query-based and 2 dense detectors on CrowdHuman stratified by GT count, and re-run one query model with 2x and 4x queries at inference; mostly inference.
- **ROI estimate:** medium

### W2-C-0031 - Do feature-upsampling modules improve localization or classification for small objects

- **Problem:** Papers proposing feature upsampling or fusion for small objects report AP but never separate whether the gain lands in localization or classification, leaving the mechanism unclear.
- **Falsifiable hypothesis:** Most AP-small gains from upsampling modules come from higher recall at fixed localization quality (classification/objectness), not from tighter boxes; localization error conditioned on detection is unchanged.
- **Cheapest experiment:** Use TIDE-style error decomposition on published checkpoints with and without such modules on COCO; re-evaluation only.
- **ROI estimate:** medium

### W2-C-0032 - AP-rare on LVIS is statistically unstable at current test sizes

- **Problem:** LVIS rare classes contribute a handful of test instances each, so headline AP-rare differences between methods may be inside sampling noise, yet drive publication claims.
- **Falsifiable hypothesis:** Bootstrap confidence intervals on AP-rare for representative methods overlap for most published pairwise comparisons, i.e. the community is ranking noise.
- **Cheapest experiment:** Bootstrap-resample LVIS val images 1,000 times, compute AP-rare CIs for 6 public checkpoints; pure re-analysis of cached predictions.
- **ROI estimate:** high

### W2-C-0033 - Does amodal completion pretraining causally improve occluded detection

- **Problem:** It is often asserted that reasoning about hidden object parts should help occluded-object detection, but no controlled causal test exists at matched compute.
- **Falsifiable hypothesis:** Pretraining a detector backbone with an amodal mask-completion objective improves occluded-strata AP over a modal-mask control at matched compute, and the gain is specific to occluded instances.
- **Cheapest experiment:** Two matched pretrainings (amodal vs modal completion on COCOA/KINS) followed by identical detection finetunes; two modest training runs.
- **ROI estimate:** medium

### W2-C-0034 - Temporal modeling gains vanish under strong single-frame backbones

- **Problem:** Video detection architectures were validated with weak backbones; whether temporal modules still add value on top of modern strong single-frame features is an open, deployment-relevant question.
- **Falsifiable hypothesis:** At matched inference compute, a strong single-frame detector matches or beats the same detector plus temporal aggregation modules on standard video detection benchmarks.
- **Cheapest experiment:** Train or reuse a modern backbone detector, compare frame-only vs one representative temporal aggregation head at matched FLOPs on ImageNet-VID; one or two finetune runs.
- **ROI estimate:** medium

### W2-C-0035 - Compression-stratified detection curves as a standard report

- **Problem:** Deployed detection consumes compressed streams, but benchmarks evaluate on high-quality JPEGs, hiding that small objects degrade first under compression.
- **Falsifiable hypothesis:** AP-small decays with bitrate at a rate several times steeper than AP-large, and the crossover bitrate where model rankings change lies inside the range used by common CCTV systems.
- **Cheapest experiment:** Re-encode COCO val at 6 bitrates (H.264 or JPEG quality ladder), evaluate 5 pretrained detectors, plot size-stratified AP-vs-bitrate; inference only.
- **ROI estimate:** medium

### W2-C-0036 - Ignore regions teach detectors miscalibrated confidence

- **Problem:** Crowded datasets use ignore regions for unannotatable areas; training samples overlapping these regions receive no gradient, which may systematically distort learned confidence in dense areas.
- **Falsifiable hypothesis:** Detectors trained with ignore regions are overconfident inside dense regions relative to sparse regions at matched visual difficulty, and replacing ignore with soft labels reduces the gap.
- **Cheapest experiment:** Compare calibration inside vs outside former ignore-region-like density strata on CrowdHuman for existing checkpoints, then one retraining run with soft-label treatment; one training run.
- **ROI estimate:** medium

### W2-C-0037 - Hierarchical label confusion is mis-scored in open-vocab evaluation

- **Problem:** When a model answers 'animal' for a 'dog' box, current matching counts a full classification error, though the answer is partially correct in the label hierarchy; open-vocab settings make this ubiquitous.
- **Falsifiable hypothesis:** Scoring with hierarchy-aware credit (WordNet path similarity) changes the ranking of open-vocab detectors, because methods differ mainly in label granularity behavior rather than grounding quality.
- **Cheapest experiment:** Re-score existing predictions of 4 open-vocab detectors on LVIS with hierarchy-aware matching; re-analysis only.
- **ROI estimate:** medium

### W2-C-0038 - Axis-aligned IoU systematically undervalues oriented detection of elongated objects

- **Problem:** Communities using axis-aligned boxes evaluate elongated rotated objects (ships, vehicles from above) with a geometry that punishes correct oriented detections, distorting progress measures.
- **Falsifiable hypothesis:** For objects with aspect ratio above 4:1 and orientation far from axis-aligned, the achievable axis-aligned IoU of a perfect oriented detection is bounded well below common thresholds, and dataset score gaps between oriented and axis-aligned methods are mostly geometric artifacts.
- **Cheapest experiment:** Analytic computation of IoU bounds as a function of aspect ratio and angle, plus re-scoring DOTA predictions under both geometries; analysis only.
- **ROI estimate:** medium

### W2-C-0039 - Saliency-biased backbones and the camouflage blind spot

- **Problem:** Pretrained backbones are optimized on photographer-curated, salient-object imagery, which may impose a saliency prior that structurally limits camouflaged and low-contrast object detection.
- **Falsifiable hypothesis:** Detection recall on camouflaged objects correlates negatively with a backbone saliency-bias score (how strongly its features separate salient from non-salient regions), across backbones at matched detection AP on COCO.
- **Cheapest experiment:** Compute a saliency-bias probe on 6 frozen backbones, finetune identical detection heads briefly, evaluate on COD10K; probes plus short finetunes.
- **ROI estimate:** medium

### W2-C-0040 - Episodic variance makes most few-shot detection deltas unreadable

- **Problem:** Few-shot detection results depend heavily on which support examples are sampled, and papers report single-episode or few-episode results, so many claimed improvements may be sampling luck.
- **Falsifiable hypothesis:** The across-episode standard deviation of few-shot detection AP exceeds the median published method-to-method improvement on standard benchmarks.
- **Cheapest experiment:** Re-run 3 public few-shot detection methods over 30 support-set episodes each on standard splits, report variance vs published deltas; moderate inference plus light finetuning per episode.
- **ROI estimate:** high

## Cluster 2: Evaluation weakness (W2-C-0041 - W2-C-0080, 40 ideas)

### W2-C-0041 - AP integrates over operating points nobody deploys

- **Problem:** AP averages precision over all recall levels, including confidence regimes never used in deployment, so leaderboard AP can diverge from utility at any deployable threshold.
- **Falsifiable hypothesis:** Rankings of published detectors by AP and by F1-at-best-fixed-threshold disagree for a substantial fraction of model pairs, and the disagreement grows on long-tail data.
- **Cheapest experiment:** Re-score cached predictions of 10 public detectors on COCO and LVIS under fixed-threshold F1 and compare rank orders with AP; pure re-analysis.
- **ROI estimate:** high

### W2-C-0042 - Deriving the IoU threshold from annotation noise instead of tradition

- **Problem:** The 0.5 IoU threshold is a historical convention; a principled threshold should depend on the annotation noise level of each dataset, which varies by domain and object size.
- **Falsifiable hypothesis:** Setting the matching threshold at the dataset-specific inter-annotator IoU quantile changes which methods rank highest on at least one major benchmark, showing conclusions are threshold-convention artifacts.
- **Cheapest experiment:** Estimate inter-annotator IoU from existing double-annotated subsets (or re-annotate 500 boxes), re-score public predictions at the derived thresholds; small annotation plus re-analysis.
- **ROI estimate:** high

### W2-C-0043 - Dice on small structures is a coin flip: size-stratified segmentation reporting

- **Problem:** Dice on tiny structures is dominated by a few boundary pixels, so aggregate Dice hides that small-structure segmentation may be statistically meaningless at current annotation quality.
- **Falsifiable hypothesis:** For structures under 100 pixels, the across-annotator Dice between human experts is as low as the model-vs-annotator Dice, implying no measurable model deficit in that stratum.
- **Cheapest experiment:** Use existing multi-annotator medical sets (LIDC) to compute size-stratified human-human vs model-human Dice; re-analysis of public data.
- **ROI estimate:** high

### W2-C-0044 - The 101-point AP interpolation bias in low-data regimes

- **Problem:** COCO AP uses 101-point interpolated precision, which introduces a small but systematic bias whose magnitude relative to reported deltas in few-shot and rare-class settings is unknown.
- **Falsifiable hypothesis:** In evaluations with under 100 positive instances per class, interpolation choice (101-point vs exact area) shifts AP by amounts comparable to published method improvements.
- **Cheapest experiment:** Recompute AP under both integration rules for rare LVIS classes and few-shot benchmarks with cached predictions; re-analysis only.
- **ROI estimate:** medium

### W2-C-0045 - Macro-mAP vs instance-weighted detection quality: whose average is it

- **Problem:** mAP averages per-class AP equally regardless of class frequency, silently encoding a value judgment; nobody has measured how much leaderboard order depends on that judgment.
- **Falsifiable hypothesis:** Switching between macro (per-class) and micro (instance-weighted) averaging reorders published COCO/LVIS leaderboards, and papers claiming long-tail progress benefit disproportionately from the macro convention.
- **Cheapest experiment:** Re-score 15 public checkpoints under both averaging schemes; re-analysis only.
- **ROI estimate:** medium

### W2-C-0046 - Annotation-noise-propagated confidence intervals for COCO AP

- **Problem:** Benchmarks report AP as a point estimate with no uncertainty from annotation noise, so the community cannot tell which SOTA increments are inside the label-noise band.
- **Falsifiable hypothesis:** Propagating measured annotation noise (from multi-annotator re-labeling of a COCO subset) into AP yields uncertainty bands of roughly comparable magnitude to typical year-over-year SOTA increments, rendering many claims indistinguishable.
- **Cheapest experiment:** Triple-annotate 1,000 COCO val images, estimate a box/label noise model, Monte-Carlo perturb the GT and recompute AP bands for 10 checkpoints; modest annotation budget plus re-analysis.
- **ROI estimate:** high

### W2-C-0047 - When does boundary quality matter: an adoption analysis for Boundary IoU

- **Problem:** Boundary IoU exists but the field defaults to mask IoU; there is no systematic map of the task regimes where the two metrics rank methods differently, so adoption arguments are anecdotal.
- **Falsifiable hypothesis:** Mask IoU and Boundary IoU rankings diverge primarily for large objects and articulated categories, and metric choice flips the winner in a nontrivial fraction of published segmentation comparisons.
- **Cheapest experiment:** Re-score public instance segmentation predictions under both metrics stratified by size and category; re-analysis only.
- **ROI estimate:** medium

### W2-C-0048 - Detector confidences are not comparable across models, breaking threshold-based comparisons

- **Problem:** Comparisons at a shared confidence threshold implicitly assume comparable score scales across detectors, but score distributions differ wildly by loss and architecture, contaminating deployment-style evaluations.
- **Falsifiable hypothesis:** After per-model calibration to a common reference (matched precision on a calibration split), threshold-based comparisons of detectors change conclusions relative to naive shared-threshold comparisons in a majority of cases.
- **Cheapest experiment:** Take 8 public detectors, compare naive threshold-0.5 F1 vs calibrated-threshold F1 rankings on COCO val; re-analysis only.
- **ROI estimate:** medium

### W2-C-0049 - AP rewards hedging: low-confidence box spam as metric gaming

- **Problem:** Because AP only requires correct ranking, emitting large numbers of low-confidence boxes can raise AP while making deployment strictly worse; the size of this wedge is unquantified.
- **Falsifiable hypothesis:** Appending calibrated low-confidence guesses to a detector output raises COCO AP measurably while lowering fixed-threshold F1 and increasing deployment review cost, demonstrating AP is gameable by hedging.
- **Cheapest experiment:** Post-process one detector output by adding region-proposal boxes with epsilon confidence, measure AP and F1 deltas; re-analysis only.
- **ROI estimate:** high

### W2-C-0050 - Crowd and ignore-region handling differs across eval implementations

- **Problem:** COCO-style crowd flags and ignore regions are handled differently across evaluation codebases, potentially producing silent AP differences attributed to models.
- **Falsifiable hypothesis:** The same prediction file scored by different popular evaluation implementations differs by up to a few tenths of AP, exceeding some published improvements.
- **Cheapest experiment:** Score identical prediction files with pycocotools, a common reimplementation, and one framework-internal evaluator; diff the outputs per class; pure software study.
- **ROI estimate:** medium
- **Notes:** UNVERIFIED - needs lit search on existing evaluator audits.

### W2-C-0051 - Dice vs boundary-F1 disagreement as a taxonomy of segmentation errors

- **Problem:** Dice and boundary-F1 are used interchangeably, but they respond to different error types; the field lacks a quantitative map of when they disagree and which error types drive it.
- **Falsifiable hypothesis:** Method rankings under Dice and boundary-F1 disagree systematically for categories with thin protrusions and holes, and the disagreement can be predicted from a shape-complexity statistic of the class.
- **Cheapest experiment:** Re-score public segmentation predictions under both metrics per class, regress ranking disagreement on shape complexity; re-analysis only.
- **ROI estimate:** medium

### W2-C-0052 - Panoptic Quality is unstable for rare things: decomposing PQ noise

- **Problem:** PQ multiplies recognition and segmentation terms, amplifying noise for classes with few instances, but the variance structure of PQ has not been characterized against method deltas.
- **Falsifiable hypothesis:** Bootstrap variance of per-class PQ for rare classes exceeds the typical between-method PQ differences reported on standard panoptic benchmarks.
- **Cheapest experiment:** Bootstrap image resampling over cached panoptic predictions of 5 methods; re-analysis only.
- **ROI estimate:** medium

### W2-C-0053 - AP is not a proper scoring rule for detection: constructing and measuring exploitation

- **Problem:** A metric is trustworthy if truthful reporting of beliefs maximizes it; AP with greedy matching may be exploitable by strategic score shaping, but no one has quantified real-model exploitation headroom.
- **Falsifiable hypothesis:** There exists a post-hoc, information-free transformation of a detector's scores and box set that raises AP on standard benchmarks, proving AP violates propriety in practice, and its magnitude is comparable to typical SOTA gaps.
- **Cheapest experiment:** Optimize a score-reshaping and duplicate-injection wrapper on val predictions of one detector, measure AP gain and confirm no new information is used; re-analysis only.
- **ROI estimate:** high

### W2-C-0054 - Disentangled evaluation: separate leaderboards for finding, naming, and outlining

- **Problem:** Detection metrics conflate whether models find objects, name them correctly, and outline them tightly; a method can win by trading one for another invisibly.
- **Falsifiable hypothesis:** Under a disentangled protocol (class-agnostic recall, naming accuracy given location, localization tightness given match), current SOTA rankings differ per axis, and no single model dominates all three.
- **Cheapest experiment:** Implement the three-axis scoring on cached predictions of 10 public models; re-analysis only.
- **ROI estimate:** high

### W2-C-0055 - A fresh i.i.d. test set for COCO: measuring a decade of adaptive overfitting

- **Problem:** COCO has served as a fixed target for ten years; the community-wide degree of adaptive overfitting to its idiosyncrasies is unknown for detection (analogous studies exist for classification).
- **Falsifiable hypothesis:** On a newly collected test set matched to the COCO distribution and annotation protocol, absolute AP drops for all models, and the drop is larger for models developed later, indicating cumulative benchmark adaptation.
- **Cheapest experiment:** Collect and annotate 2,000 new images under the original COCO protocol, evaluate a historical sequence of 15 public checkpoints; annotation cost dominated, no training.
- **ROI estimate:** high
- **Notes:** UNVERIFIED - needs lit search for existing COCO replication studies.

### W2-C-0056 - Arbitrary size buckets: continuous size-AP curves change conclusions

- **Problem:** AP-small/medium/large use fixed area cutoffs (32^2, 96^2) chosen historically; conclusions about which methods help small objects may not survive a continuous treatment of size.
- **Falsifiable hypothesis:** Methods claimed to improve small-object AP show gains concentrated in a narrow band near the bucket boundary, and continuous size-AP curves reveal crossovers hidden by the bucketed report.
- **Cheapest experiment:** Compute AP in sliding size windows from cached predictions of small-object-oriented methods vs baselines; re-analysis only.
- **ROI estimate:** medium

### W2-C-0057 - Missing annotations punish better detectors: the unlabeled-object tax

- **Problem:** Benchmarks contain unlabeled true objects; detectors good enough to find them are charged with false positives, meaning the metric may actively penalize detection improvements beyond the annotation frontier.
- **Falsifiable hypothesis:** Human verification of high-confidence 'false positives' shows that stronger detectors have a higher fraction of correct-but-unlabeled detections, so measured precision gaps understate true gaps and can invert rankings near the frontier.
- **Cheapest experiment:** Sample 500 top-scoring false positives from each of 5 detectors on COCO val, human-verify them, recompute corrected precision; small annotation budget.
- **ROI estimate:** high

### W2-C-0058 - Duplicate-annotation policies are a hidden metric hyperparameter

- **Problem:** Datasets contain near-duplicate GT boxes handled by ad hoc dedup policies during evaluation; the sensitivity of scores to this policy is unmeasured.
- **Falsifiable hypothesis:** Varying the GT dedup policy (IoU threshold for merging duplicate annotations) within reasonable bounds changes per-class AP by more than published deltas for affected classes.
- **Cheapest experiment:** Detect near-duplicate GT pairs in COCO/LVIS, re-score cached predictions under 3 dedup policies; re-analysis only.
- **ROI estimate:** medium

### W2-C-0059 - Slice-wise vs volume-wise aggregation flips 3D medical segmentation rankings

- **Problem:** 3D medical segmentation results are aggregated per-slice, per-volume, or per-dataset with little standardization, and the aggregation axis interacts with lesion-size distributions.
- **Falsifiable hypothesis:** For public 3D benchmarks, per-slice and per-volume Dice aggregation produce different method rankings whenever lesion size distributions are heavy-tailed, and the flip direction is predictable from that distribution.
- **Cheapest experiment:** Re-aggregate cached predictions from public medical segmentation challenges under both schemes; re-analysis only.
- **ROI estimate:** medium

### W2-C-0060 - ECE for detection is ill-posed: ground calibration in downstream decision cost

- **Problem:** Expected calibration error for detectors requires choosing which predictions count and how they match GT, and different choices give contradictory conclusions; calibration should instead be measured by decision cost in a task.
- **Falsifiable hypothesis:** Across plausible ECE variants for detection, method rankings disagree, while a decision-theoretic evaluation (expected cost over a threshold-decision task with specified error costs) yields a stable ranking that ECE variants fail to predict.
- **Cheapest experiment:** Implement 4 ECE variants and one expected-cost metric over cached predictions of 8 detectors; re-analysis only.
- **ROI estimate:** high

### W2-C-0061 - mAP is blind to score magnitudes: what monotone-invariance hides

- **Problem:** mAP is invariant to monotone transforms of confidence, so two detectors with identical mAP can differ enormously in usable-confidence quality, which downstream systems depend on.
- **Falsifiable hypothesis:** Among public detector pairs with near-identical mAP, downstream utility (selective-prediction risk-coverage area) differs substantially, demonstrating that mAP-equal is not deployment-equal.
- **Cheapest experiment:** Find mAP-matched detector pairs among public checkpoints, compare risk-coverage curves on COCO val; re-analysis only.
- **ROI estimate:** medium

### W2-C-0062 - Does average recall of proposals still predict final AP for modern detectors

- **Problem:** The proposal-quality metric AR was validated as a proxy for final detection AP in the two-stage era; whether that correlation survives modern end-to-end and query-based pipelines is untested.
- **Falsifiable hypothesis:** Across modern architectures, AR of intermediate proposals correlates only weakly with final AP, breaking a folk rule still used to justify proposal-stage research.
- **Cheapest experiment:** Extract proposal-stage AR and final AP for 8 public models spanning architectures, compute correlation; inference only.
- **ROI estimate:** medium
- **Notes:** UNVERIFIED - needs lit search for the original AR-AP correlation claims.

### W2-C-0063 - Cost-sensitive AP: confusion costs from real applications

- **Problem:** AP charges all class confusions equally, but confusing a person with a pole is not the same as confusing two furniture types in safety domains; there is no standard cost-weighted detection metric grounded in application data.
- **Falsifiable hypothesis:** Under application-derived confusion cost matrices (from AV incident taxonomies), model rankings differ from mAP rankings, and some widely-used models are dominated once costs are considered.
- **Cheapest experiment:** Build one cost matrix from public AV safety taxonomies, re-score cached nuScenes/COCO-person predictions; re-analysis only.
- **ROI estimate:** medium

### W2-C-0064 - Image-level vs instance-level bootstrap: which CI is right for detection

- **Problem:** Confidence intervals for detection metrics can resample images or instances, and the two choices give different intervals because instances within an image are correlated; the field has no standard.
- **Falsifiable hypothesis:** Instance-level bootstrap systematically underestimates the variance of AP relative to image-level bootstrap by a factor large enough to change significance conclusions in typical comparisons.
- **Cheapest experiment:** Run both bootstrap schemes on cached predictions over COCO val for 5 models, compare interval widths and pairwise significance verdicts; re-analysis only.
- **ROI estimate:** medium

### W2-C-0065 - A survey and re-analysis of significance testing in detection papers

- **Problem:** It is unknown what fraction of detection papers report any statistical uncertainty, and what fraction of their headline claims survive proper tests; this is measurable meta-science, not opinion.
- **Falsifiable hypothesis:** Fewer than one in ten recent detection papers report variance or tests, and among reproducible claims, a nontrivial fraction fail an image-level bootstrap test at conventional levels.
- **Cheapest experiment:** Systematically code 200 recent detection papers for statistical practice, re-test 20 claims with public checkpoints; reading time plus re-analysis.
- **ROI estimate:** high

### W2-C-0066 - Most SOTA claims are Pareto-incomparable: multi-metric honesty

- **Problem:** Single-number metrics manufacture total orders over methods that are actually incomparable across relevant axes (AP, calibration, latency, small-object AP, robustness).
- **Falsifiable hypothesis:** Under a 5-axis evaluation, the majority of consecutive SOTA claims on COCO in recent years are Pareto-incomparable with their predecessor, i.e. they trade one axis for another rather than dominating.
- **Cheapest experiment:** Evaluate a historical chain of 12 public checkpoints on 5 axes with cached inference; re-analysis plus corruption evaluation.
- **ROI estimate:** medium

### W2-C-0067 - Tracking metrics are threshold-tuned on test: MOTA/HOTA sensitivity audit

- **Problem:** Multi-object tracking metrics depend on detection score thresholds that many submissions tune against the evaluation itself, making leaderboard gaps partially an artifact of threshold search.
- **Falsifiable hypothesis:** Re-evaluating public trackers with thresholds tuned only on a held-out split shrinks leaderboard gaps substantially and reorders mid-table methods.
- **Cheapest experiment:** Take 8 public tracker outputs, re-tune thresholds on a val split, score on test split; re-analysis only.
- **ROI estimate:** medium

### W2-C-0068 - Synonym mismatches counted as errors in open-vocab evaluation

- **Problem:** Open-vocab evaluation string-matches predicted labels to GT vocabulary, counting synonyms and lexical variants as failures, which penalizes exactly the models with richer vocabularies.
- **Falsifiable hypothesis:** Fuzzy label matching (embedding or WordNet synonym sets) raises measured AP of generative-vocabulary detectors substantially more than fixed-vocabulary ones, changing cross-paradigm comparisons.
- **Cheapest experiment:** Re-score cached open-vocab predictions with synonym-aware matching on LVIS/ODinW; re-analysis only.
- **ROI estimate:** medium

### W2-C-0069 - Box AP overstates localization quality for articulated objects

- **Problem:** A tight box on an articulated object (spread limbs, tails) can contain mostly background, so box IoU signals localization quality that masks would contradict; the size of this distortion is unquantified.
- **Falsifiable hypothesis:** For high-articulation categories, box-IoU-matched detections show mask-IoU distributions substantially lower than for compact categories, and box AP overstates cross-category localization progress accordingly.
- **Cheapest experiment:** Use COCO instances with both boxes and masks, compare box-IoU vs mask-IoU joint distributions per category from cached predictions; re-analysis only.
- **ROI estimate:** medium

### W2-C-0070 - Minimum detectable effect: power analysis tables for popular benchmarks

- **Problem:** Reviewers and authors have no reference for the smallest AP difference a benchmark can statistically resolve, so undersized test sets keep supporting unresolvable claims.
- **Falsifiable hypothesis:** For several popular domain benchmarks, the minimum detectable AP difference at conventional power exceeds 1 point, larger than many published improvements evaluated on them.
- **Cheapest experiment:** Estimate metric variance by bootstrap on public predictions per benchmark, derive minimum detectable effects, publish lookup tables; re-analysis only.
- **ROI estimate:** high

### W2-C-0071 - Is SOTA above the human agreement ceiling, and what does that mean

- **Problem:** If model-vs-GT agreement exceeds human-vs-human agreement on a benchmark, further gains measure fit to annotation idiosyncrasies rather than perception; benchmarks lack this ceiling measurement.
- **Falsifiable hypothesis:** On at least one major detection benchmark, current SOTA model-GT agreement exceeds measured human-human agreement, implying the benchmark has become a label-style-matching contest.
- **Cheapest experiment:** Re-annotate 500 images with independent annotators, compute human-human AP against original GT, compare with SOTA model AP; small annotation budget.
- **ROI estimate:** high

### W2-C-0072 - NMS and threshold tuning as unreported test leakage

- **Problem:** Post-processing hyperparameters (NMS IoU, score floors, top-k) are commonly tuned per benchmark, effectively fitting the test distribution while the paper narrative credits the architecture.
- **Falsifiable hypothesis:** Standardizing post-processing across methods (single shared configuration tuned on a neutral split) shrinks published between-method gaps on COCO by a measurable fraction and reorders some pairs.
- **Cheapest experiment:** Re-run post-processing sweeps for 8 public checkpoints under a shared protocol; re-analysis only.
- **ROI estimate:** medium

### W2-C-0073 - The empty-mask convention silently decides medical segmentation winners

- **Problem:** When GT and prediction are both empty, Dice is defined by convention (1, 0, or excluded), and conventions differ across papers; in screening datasets with many negatives this choice can dominate scores.
- **Falsifiable hypothesis:** On public medical benchmarks with high negative-slice fractions, switching empty-case conventions changes method rankings, and some published cross-paper comparisons are invalid because they mix conventions.
- **Cheapest experiment:** Re-aggregate cached predictions from 2 public challenges under the 3 conventions; re-analysis only, plus a survey of which papers use which.
- **ROI estimate:** medium

### W2-C-0074 - AP at IoU 0.5:0.95 weights localization unevenly across object sizes

- **Problem:** Averaging AP over IoU 0.5 to 0.95 is treated as balanced, but a fixed IoU increment corresponds to very different pixel tolerances at different object sizes, embedding a hidden size weighting.
- **Falsifiable hypothesis:** Under a pixel-tolerance-equalized IoU ladder (thresholds scheduled by object size), method rankings differ from the standard ladder, revealing that some 'localization improvements' are large-object-specific artifacts.
- **Cheapest experiment:** Define the equalized ladder analytically, re-score cached predictions of 8 detectors; re-analysis only.
- **ROI estimate:** medium

### W2-C-0075 - Evaluation-server vs local-eval discrepancies as a reproducibility hazard

- **Problem:** Test-server evaluations occasionally disagree with local val-based expectations for reasons beyond distribution shift (version drift, flag handling), but no audit quantifies this channel.
- **Falsifiable hypothesis:** For benchmarks offering both, the server-vs-local metric discrepancy on identical prediction files is nonzero for a measurable fraction of submissions and correlates with use of nonstandard prediction formats.
- **Cheapest experiment:** Submit identical files to servers and score locally across 3 benchmarks and several format variants; submission quota plus re-analysis.
- **ROI estimate:** medium

### W2-C-0076 - Annotation style drift across dataset versions invalidates cross-version claims

- **Problem:** Datasets evolve across releases (COCO 2014 vs 2017 splits, LVIS versions), and annotation-style drift between versions may masquerade as method progress in papers comparing across versions.
- **Falsifiable hypothesis:** The same model evaluated on matched images labeled under two dataset versions scores differently by an amount comparable to typical claimed improvements, driven by identifiable annotation-style changes.
- **Cheapest experiment:** Find images present in both versions, evaluate 5 checkpoints against each version's labels; re-analysis only.
- **ROI estimate:** medium

### W2-C-0077 - Minimum-support reporting standards for tail metrics

- **Problem:** AP over classes with under 10 test instances is routinely reported to two decimals without support disclosure; a standard is needed and its adoption case should be empirical, not rhetorical.
- **Falsifiable hypothesis:** Enforcing a minimum-support rule (report AP only for classes above a support threshold, otherwise pooled) changes the qualitative conclusions of a meaningful fraction of recent long-tail papers.
- **Cheapest experiment:** Re-aggregate published per-class results under the rule using cached predictions; re-analysis only.
- **ROI estimate:** medium

### W2-C-0078 - Does benchmark AP predict downstream utility: grasping and safety as ground truth

- **Problem:** The community assumes benchmark AP transfers to downstream utility, but direct measurements linking AP to task success (robotic grasping, AV intervention rates) are scarce and old.
- **Falsifiable hypothesis:** Across detectors spanning 10 AP points, downstream task success in a fixed pipeline saturates or becomes noise-dominated well before the top of the AP range, meaning marginal AP no longer buys utility.
- **Cheapest experiment:** Fix a simulated grasping or driving pipeline, swap 6 public detectors, measure task metrics; simulation compute only.
- **ROI estimate:** high

### W2-C-0079 - Why probabilistic detection metrics failed to be adopted: an empirical autopsy

- **Problem:** Metrics like PDQ that reward spatial and semantic uncertainty were proposed and largely ignored; understanding whether the barrier is conceptual, practical, or evidential would inform future metric design.
- **Falsifiable hypothesis:** On modern detectors, PDQ-style metrics identify uncertainty-quality differences invisible to mAP, and their non-adoption is attributable to tooling friction rather than lack of signal, measurable by correlating PDQ deltas with downstream selective-prediction utility.
- **Cheapest experiment:** Score 8 public detectors with a PDQ implementation, correlate with risk-coverage utility, and survey tooling friction; re-analysis only.
- **ROI estimate:** medium
- **Notes:** UNVERIFIED - needs lit search on PDQ follow-up literature.

### W2-C-0080 - GT tightness conventions vary within single datasets: an intra-dataset audit

- **Problem:** Within one dataset, annotators differ in how tightly boxes hug objects and whether hidden parts are included, creating per-annotator label styles that models can partially learn and metrics cannot see.
- **Falsifiable hypothesis:** Annotator-identity (or batch) signatures are recoverable from GT box statistics, and model AP differs measurably across annotator strata, proving that part of AP measures style matching.
- **Cheapest experiment:** Cluster GT boxes by style features (relative margin, aspect handling), evaluate models per cluster on COCO val; re-analysis only.
- **ROI estimate:** medium

## Cluster 3: Unproven community assumptions (W2-C-0081 - W2-C-0115, 35 ideas)

### W2-C-0081 - Does better classification pretraining actually help dense tasks: a rank-correlation audit

- **Problem:** The community assumes backbones with higher ImageNet or zero-shot classification accuracy transfer better to detection and segmentation, but systematic compute-matched evidence across modern backbone families is thin.
- **Falsifiable hypothesis:** Across 15 backbones at matched detection-finetune compute, the rank correlation between upstream classification accuracy and COCO AP is weak (below 0.5), and breaks down entirely within a backbone family at fixed scale.
- **Cheapest experiment:** Finetune identical detection heads on 15 public backbones with a fixed short schedule, correlate upstream vs downstream metrics; roughly 15 short training runs.
- **ROI estimate:** high

### W2-C-0082 - Mapping where SAM zero-shot actually works: a falsification atlas

- **Problem:** The claim that SAM generalizes zero-shot to arbitrary domains is repeated without a systematic domain map; practitioners need to know the boundary of validity, not anecdotes.
- **Falsifiable hypothesis:** SAM-family zero-shot mask quality degrades below usability (mask IoU under 0.5 against expert labels) on a predictable subset of domains characterized by low edge contrast and non-photographic sensors (ultrasound, sonar, electron microscopy), and prompt engineering does not rescue it.
- **Cheapest experiment:** Evaluate SAM variants on 12 public domain datasets with existing GT, plot quality vs domain descriptors; inference only.
- **ROI estimate:** high

### W2-C-0083 - Is more finetuning data always better: the noisy-web-data inflection point

- **Problem:** Detection practitioners assume more training data monotonically helps, but web-mined detection data carries label noise whose marginal harm may eventually exceed marginal signal.
- **Falsifiable hypothesis:** AP as a function of added web-mined training data is non-monotonic: past an inflection point that depends on noise rate, additional data lowers AP on a clean test set.
- **Cheapest experiment:** Mix COCO with increasing fractions of auto-labeled web images at measured noise rates, train fixed short schedules, trace the curve; 5-6 short training runs.
- **ROI estimate:** medium

### W2-C-0084 - Does mask supervision causally improve box detection

- **Problem:** It is folklore that adding instance-mask supervision improves box AP, but modern evidence at matched annotation budget (masks cost more than boxes) is missing.
- **Falsifiable hypothesis:** At matched annotation cost (fewer masked images vs more boxed images), box-only training beats box-plus-mask training on box AP, reversing the folklore once cost is accounted.
- **Cheapest experiment:** Three matched-budget training runs on COCO subsets (boxes only, masks on all, cost-matched mix); three modest training runs.
- **ROI estimate:** medium

### W2-C-0085 - Is multi-scale training still necessary with modern backbones

- **Problem:** Multi-scale training is inherited as mandatory for detection, but strong pretrained backbones with heavy augmentation may have made it redundant, and it complicates pipelines and batching.
- **Falsifiable hypothesis:** With a modern pretrained backbone and standard augmentation, single-scale training matches multi-scale training on COCO AP within noise at matched compute.
- **Cheapest experiment:** Two matched training runs (single-scale vs multi-scale) at two backbone scales; four training runs total.
- **ROI estimate:** medium

### W2-C-0086 - Frozen foundation backbones for detection: is finetuning overrated

- **Problem:** The assumption that detection requires backbone finetuning predates strong self-supervised foundations; freezing would enable massive multi-task reuse if the penalty is small.
- **Falsifiable hypothesis:** A frozen modern foundation backbone with a trained adapter and detection head reaches within 2 AP of full finetuning on COCO at matched total compute, and beats it under domain shift.
- **Cheapest experiment:** Two training runs (frozen-plus-adapter vs full finetune) with one strong backbone, evaluated in-domain and on corruption/shift suites; two training runs.
- **ROI estimate:** medium

### W2-C-0087 - Longer detection training past the recipe: mapping the overfitting onset

- **Problem:** Recipes assume detection benefits from long schedules, but the shape of the AP-vs-epochs curve past standard schedules on COCO-scale data with modern augmentation is unmeasured public knowledge.
- **Falsifiable hypothesis:** For COCO-scale data, validation AP plateaus and then declines measurably within 3x standard schedule length, and the decline is concentrated in rare classes and small objects.
- **Cheapest experiment:** Extend one standard training run to 3x schedule with dense checkpointing, evaluate the trajectory; one long training run.
- **ROI estimate:** medium

### W2-C-0088 - Domain randomization vs realism matching: which synthetic recipe wins where

- **Problem:** Synthetic-data practice assumes broad domain randomization beats effortful realism matching, but the comparison is rarely run at matched rendering budget for detection.
- **Falsifiable hypothesis:** At matched rendering budget, realism-matched narrow synthetic data beats domain-randomized data when the target domain is known, and the reverse holds only when the target is unknown, quantifying the value of target knowledge.
- **Cheapest experiment:** Render two matched synthetic sets (randomized vs matched to a chosen target camera), train identical detectors, test on the target; two renders plus two training runs.
- **ROI estimate:** medium

### W2-C-0089 - Higher resolution does not help every class: per-class resolution sensitivity

- **Problem:** Resolution scaling is treated as a global knob, but classes with large context dependence may lose accuracy at higher resolution due to reduced receptive-field coverage.
- **Falsifiable hypothesis:** A measurable subset of COCO classes has AP that decreases with input resolution, identifiable in advance by their context-dependence score.
- **Cheapest experiment:** Evaluate 3 pretrained detectors at 5 input resolutions, plot per-class AP-vs-resolution; inference only.
- **ROI estimate:** medium

### W2-C-0090 - Video pretraining for video detection: does temporal pretraining pay for itself

- **Problem:** It is assumed video tasks want video pretraining, but at matched compute, image pretraining plus temporal finetuning may dominate because image data is more diverse per FLOP.
- **Falsifiable hypothesis:** At matched total pretraining compute, image-pretrained backbones finetuned with a lightweight temporal head match or beat video-pretrained backbones on video detection benchmarks.
- **Cheapest experiment:** Compare public image-pretrained and video-pretrained backbones of matched scale under identical video-detection finetunes; two or three finetune runs.
- **ROI estimate:** medium

### W2-C-0091 - Self-supervised vs supervised pretraining for dense tasks: a decontaminated comparison

- **Problem:** Claims that self-supervised pretraining transfers better to dense prediction often compare models differing in data, augmentation, and schedule simultaneously, so the causal factor is unidentified.
- **Falsifiable hypothesis:** When data, augmentation, and compute are strictly matched, the dense-task advantage of self-supervised over supervised pretraining shrinks to near zero, indicating prior comparisons measured recipe differences.
- **Cheapest experiment:** Pretrain two mid-size backbones (one SSL objective, one supervised) on identical data and schedule, finetune identical detectors; two pretraining runs at modest scale.
- **ROI estimate:** medium

### W2-C-0092 - Augmentation gains do not transfer across detector families

- **Problem:** Augmentation policies validated on one detector family are assumed portable, but interaction effects between augmentation and matching/assignment strategies could break transfer.
- **Falsifiable hypothesis:** The AP gain of a fixed augmentation policy varies in sign across detector families (anchor-based, anchor-free, query-based) trained on the same data.
- **Cheapest experiment:** Cross 3 augmentation policies with 3 detector families in short-schedule runs; nine short training runs.
- **ROI estimate:** medium

### W2-C-0093 - Detection does not need large batches: small-batch recipes revisited

- **Problem:** Large-batch training is assumed necessary for detection stability, an assumption inherited from BN-era recipes that may not survive modern normalization and optimizers.
- **Falsifiable hypothesis:** With group normalization and appropriately scaled optimizers, batch-size-2 training reaches within noise of batch-size-32 results on COCO at matched total images seen.
- **Cheapest experiment:** Two matched training runs differing only in batch size and LR scaling; two training runs.
- **ROI estimate:** low

### W2-C-0094 - When does EMA hurt: mapping the EMA failure regime for detection

- **Problem:** Exponential moving average of weights is applied by default in modern detection recipes, but its interaction with short schedules and small datasets is assumed, not mapped.
- **Falsifiable hypothesis:** EMA reduces final AP when the training schedule is short relative to the EMA horizon or when the dataset is small, with a predictable boundary in (schedule, decay) space.
- **Cheapest experiment:** Grid of short training runs over schedule length and EMA decay on two dataset sizes; roughly 12 short runs.
- **ROI estimate:** low

### W2-C-0095 - Why mosaic works: scale jitter or context diversity

- **Problem:** Mosaic augmentation is credited with teaching context diversity, but its gains may reduce to the scale jitter it induces, which would let simpler pipelines replace it.
- **Falsifiable hypothesis:** Matched scale-jitter augmentation without image compositing recovers the majority of mosaic's AP gain, and the residual is concentrated in no measurable stratum.
- **Cheapest experiment:** Three matched training runs (no mosaic, mosaic, scale-jitter-matched) on one mid-size detector; three training runs.
- **ROI estimate:** medium

### W2-C-0096 - Is deformable attention still necessary at modern scale

- **Problem:** Deformable attention was introduced to fix DETR convergence and small-object issues; whether modern training recipes and backbones have made it redundant is unexamined folklore.
- **Falsifiable hypothesis:** With modern recipes, dense global attention matches deformable attention on COCO AP and small-object AP at matched wall-clock compute, removing the case for the added complexity.
- **Cheapest experiment:** Two matched training runs of one query-based detector with each attention type under a current recipe; two training runs.
- **ROI estimate:** medium

### W2-C-0097 - Monocular depth cues are already inside detection features

- **Problem:** Detection pipelines are assumed depth-blind without dedicated sensors or heads, but backbone features may already encode coarse metric depth usable for free.
- **Falsifiable hypothesis:** A frozen detection backbone supports linear-probe depth estimation at accuracy sufficient to order object pairs by distance above 80 percent, without any depth supervision during detection training.
- **Cheapest experiment:** Linear-probe depth on frozen detector features using KITTI depth GT; probe training only.
- **ROI estimate:** medium

### W2-C-0098 - Label smoothing in detection heads: calibration help or NMS poison

- **Problem:** Label smoothing is imported from classification into detection heads without examining its interaction with score-based suppression and ranking metrics.
- **Falsifiable hypothesis:** Label smoothing compresses the score distribution in ways that degrade NMS separation of duplicates, lowering crowded-scene AP even when classification accuracy of matched boxes improves.
- **Cheapest experiment:** Two matched training runs with and without smoothing, evaluated on CrowdHuman and COCO with duplicate-analysis; two training runs.
- **ROI estimate:** low

### W2-C-0099 - Is COCO saturated, or are we measuring annotation errors: a residual-error census

- **Problem:** The belief that COCO is saturated assumes remaining errors are model errors; if most residual errors are annotation artifacts, the benchmark ended earlier than the community thinks.
- **Falsifiable hypothesis:** Human adjudication of residual SOTA errors on COCO shows the majority are annotation problems (missing labels, wrong class, crowd mislabels) rather than genuine model failures.
- **Cheapest experiment:** Sample 1,000 residual errors of a SOTA model, adjudicate with 2 annotators, classify error provenance; small annotation budget.
- **ROI estimate:** high

### W2-C-0100 - Are transformers really more robust than CNNs for dense prediction

- **Problem:** Transformer robustness claims come mostly from classification; whether they hold for detection and segmentation under matched pretraining and compute is assumed rather than shown.
- **Falsifiable hypothesis:** At matched pretraining data and compute, transformer and CNN detectors show equal corruption robustness (relative AP drop on corrupted suites), localizing prior claims to pretraining differences.
- **Cheapest experiment:** Finetune matched CNN and transformer backbones with identical heads, evaluate on corrupted COCO variants; two training runs plus corruption inference.
- **ROI estimate:** medium

### W2-C-0101 - Distillation silently discards robustness: the hidden cost of student models

- **Problem:** Knowledge distillation is assumed to preserve what matters when compressing detectors, but robustness and calibration under shift may not transfer with clean AP.
- **Falsifiable hypothesis:** Distilled detection students matching teachers within 1 clean AP lose disproportionately more AP under corruptions and domain shift, and the loss correlates with distillation temperature and feature-mimicking choices.
- **Cheapest experiment:** Distill one student from one teacher under 3 recipes, evaluate all on corruption and cross-dataset suites; three distillation runs plus inference.
- **ROI estimate:** medium

### W2-C-0102 - Test-time augmentation can hurt: mapping when TTA backfires

- **Problem:** TTA is assumed to be a free AP boost, but flip/scale averaging can distort score distributions and hurt rare classes and calibration in ways the headline number hides.
- **Falsifiable hypothesis:** TTA improves pooled AP while degrading rare-class AP and post-hoc calibration for a measurable fraction of detectors, making it net harmful for threshold-based deployments.
- **Cheapest experiment:** Evaluate 6 public detectors with and without standard TTA, stratify by class frequency and measure calibration; inference only.
- **ROI estimate:** medium

### W2-C-0103 - Frozen BN folklore in small-batch finetuning: retest on modern stacks

- **Problem:** Freezing BatchNorm statistics during detection finetuning is inherited folklore from 2017-era recipes; whether it still matters with modern initialization and normalization is untested public knowledge.
- **Falsifiable hypothesis:** On modern backbones, freezing vs updating BN statistics during finetuning changes final AP by less than seed noise, retiring a ritual that constrains recipe design.
- **Cheapest experiment:** Four training runs (2 settings x 2 seeds) on one standard detector; four short runs.
- **ROI estimate:** low

### W2-C-0104 - Are larger models more label-efficient for detection specifically

- **Problem:** Label-efficiency scaling claims come from classification; detection has structured labels whose scaling behavior with model size may differ qualitatively.
- **Falsifiable hypothesis:** The label-efficiency exponent (AP gain per doubling of labeled data) does not improve with model scale for detection finetuning, unlike classification, because localization supervision saturates differently.
- **Cheapest experiment:** Train 3 model scales on 4 data fractions of COCO with fixed recipes, fit scaling curves; twelve short training runs.
- **ROI estimate:** medium

### W2-C-0105 - Pretrain-finetune resolution matching: how much does it really matter

- **Problem:** The assumed need to match pretraining and finetuning resolution constrains recipe design, but its actual cost for dense tasks has not been isolated from confounds.
- **Falsifiable hypothesis:** Resolution mismatch between pretraining and detection finetuning costs under 1 AP once positional embeddings are properly interpolated, making the matching folklore obsolete.
- **Cheapest experiment:** Finetune one backbone pretrained at 3 resolutions onto a fixed detection resolution with proper interpolation; three training runs.
- **ROI estimate:** low

### W2-C-0106 - Do open-vocab detectors dominate closed-set specialists on their own turf

- **Problem:** The narrative says open-vocab models subsume closed-set detectors, but deployment users care about the gap on a fixed vocabulary and distribution, where specialists may still win at a fraction of the cost.
- **Falsifiable hypothesis:** On fixed-vocabulary deployment-style test sets, compute-matched closed-set specialists beat open-vocab models by a stable margin that has not shrunk across recent open-vocab generations.
- **Cheapest experiment:** Evaluate 3 generations of open-vocab models and matched closed-set baselines on 5 fixed-vocabulary datasets; inference plus a few finetunes.
- **ROI estimate:** high

### W2-C-0107 - SAM pseudo-masks as training data: characterizing the noise ceiling

- **Problem:** Auto-labeling with SAM-style models is assumed good enough to train segmentation students, but the structure of its errors (systematic boundary bias, part-whole confusion) may impose a hard student ceiling.
- **Falsifiable hypothesis:** Students trained on SAM pseudo-masks plateau below students trained on human masks even with unlimited pseudo-labeled data, because pseudo-label errors are systematic rather than random.
- **Cheapest experiment:** Train students on increasing volumes of pseudo-masks vs a fixed human-mask baseline on one domain, extrapolate the plateau; four training runs.
- **ROI estimate:** medium

### W2-C-0108 - VLM benchmark scores do not predict grounding: captioning vs detection dissociation

- **Problem:** Model cards imply that better VQA/captioning VLMs ground language in space better, but grounding may dissociate from language-benchmark quality entirely.
- **Falsifiable hypothesis:** Across 10 VLMs, referring-expression localization accuracy is uncorrelated with VQA/caption benchmark scores once model scale is controlled.
- **Cheapest experiment:** Evaluate public VLMs on RefCOCO-style grounding vs their published language scores, partial-correlate against parameter count; inference only.
- **ROI estimate:** medium

### W2-C-0109 - Was hard negative mining actually made obsolete by focal loss

- **Problem:** The community retired explicit hard-negative mining after focal loss, but the equivalence was shown in balanced regimes; in long-tail and small-data regimes the retirement may be premature.
- **Falsifiable hypothesis:** In long-tail detection, explicit hard-negative mining on top of focal loss improves tail AP beyond focal loss alone, contradicting the assumed subsumption.
- **Cheapest experiment:** Two matched training runs on LVIS (focal only vs focal plus mining); two training runs.
- **ROI estimate:** low

### W2-C-0110 - Multi-task learning with segmentation and depth: measuring interference honestly

- **Problem:** Multi-task training is assumed synergistic for dense tasks, but reported synergies rarely control for the extra supervision and compute the auxiliary tasks bring.
- **Falsifiable hypothesis:** At strictly matched compute and annotation budget, adding segmentation or depth auxiliaries to detection training yields zero or negative AP change, revealing published synergies as budget artifacts.
- **Cheapest experiment:** Three matched-budget runs (detection only, plus segmentation, plus depth) on one dataset with all budgets equalized; three training runs.
- **ROI estimate:** medium

### W2-C-0111 - Resolution scaling vs model scaling for small objects: the real exchange rate

- **Problem:** Practitioners assume raising resolution is the best lever for small objects, but the exchange rate between resolution FLOPs and model-capacity FLOPs for small-object AP has not been published as a curve.
- **Falsifiable hypothesis:** At matched inference FLOPs, allocating compute to resolution beats allocating to model width for small objects only below a resolution threshold, after which model scaling dominates.
- **Cheapest experiment:** Evaluate a FLOP-matched grid (3 resolutions x 3 model widths) with short finetunes on VisDrone; nine short runs.
- **ROI estimate:** medium

### W2-C-0112 - Does crop augmentation teach translation equivariance, or do we just believe it does

- **Problem:** Random cropping is assumed to instill translation robustness in detectors, but learned equivariance has rarely been measured directly at the feature and prediction level.
- **Falsifiable hypothesis:** Detectors trained with and without crop augmentation show indistinguishable prediction equivariance under sub-stride translations, because equivariance is dominated by architecture, not augmentation.
- **Cheapest experiment:** Train two matched models, measure prediction drift under controlled pixel shifts; two short training runs plus analysis.
- **ROI estimate:** low

### W2-C-0113 - Is the syn2real gap mostly texture: a shape-texture decomposition for detection

- **Problem:** The texture-bias story from classification is assumed to explain the synthetic-to-real detection gap, but detection involves localization signals that may not follow classification-derived conclusions.
- **Falsifiable hypothesis:** Style-transferring synthetic training images to real texture closes under half of the syn2real detection gap, showing the dominant gap components are geometric and distributional, not textural.
- **Cheapest experiment:** Train on synthetic, texture-stylized synthetic, and real data; compare gaps on a real test set; three training runs on existing sim datasets.
- **ROI estimate:** medium

### W2-C-0114 - Does CLIP robustness survive a detection head: robustness inheritance audit

- **Problem:** Zero-shot CLIP robustness under distribution shift is assumed to transfer to detection systems built on CLIP features, but heads and finetuning may destroy exactly the robust directions.
- **Falsifiable hypothesis:** Detection heads finetuned on CLIP backbones lose most of the backbone's effective-robustness advantage relative to supervised backbones, measurable as the gap between zero-shot classification robustness and detection robustness under matched shifts.
- **Cheapest experiment:** Compare effective robustness of CLIP-based vs supervised-based detectors on shifted detection sets, holding heads and data fixed; two finetunes plus inference.
- **ROI estimate:** medium

### W2-C-0115 - Annotation quality vs quantity at fixed budget: the detection labeling exchange rate

- **Problem:** Teams assume annotation noise washes out at scale, but the exchange rate between label quality and quantity for detection at fixed labeling budget is unmeasured, leaving budget decisions to intuition.
- **Falsifiable hypothesis:** At fixed annotation budget, a smaller carefully-verified dataset beats a larger single-pass dataset for detection AP whenever single-pass box-error rates exceed a threshold identifiable in advance from annotator agreement statistics.
- **Cheapest experiment:** Simulate budget splits by degrading COCO labels at measured error rates vs subsampling, train matched detectors on each; four training runs.
- **ROI estimate:** high

## Cluster 4: Surprising empirical phenomena (W2-C-0116 - W2-C-0145, 30 ideas)

### W2-C-0116 - Detectors that see ghosts: hallucinated detections of removed objects

- **Problem:** If detectors fire on context alone, they will detect objects that have been physically removed from a scene, a phenomenon with direct safety consequences that lacks systematic measurement.
- **Falsifiable hypothesis:** After high-quality inpainting removal of an object, standard detectors still detect the removed object above deployment thresholds in a substantial fraction of cases, and the ghost rate correlates with class-context strength.
- **Cheapest experiment:** Inpaint 1,000 object instances out of COCO images, run 5 detectors, measure ghost-detection rates per class; inpainting plus inference.
- **ROI estimate:** high

### W2-C-0117 - Compression fingerprints: does re-encoding test images toward the training distribution raise AP

- **Problem:** Models may key on JPEG/codec fingerprints of their training corpus; if re-encoding test images with training-matched settings changes AP, benchmarks partially measure codec matching.
- **Falsifiable hypothesis:** Re-encoding test images to match training-set compression statistics increases AP measurably for models trained on heavily web-scraped data, and the effect disappears for models trained on raw-captured data.
- **Cheapest experiment:** Re-encode COCO val under several codec settings, evaluate a panel of detectors, correlate AP shifts with training-data provenance; inference only.
- **ROI estimate:** medium
- **Notes:** UNVERIFIED - needs lit search on codec-bias studies for detection.

### W2-C-0118 - How far do random features go: detection with frozen random backbones

- **Problem:** The baseline of a frozen randomly-initialized backbone with a trained detection head is almost never reported, so the community cannot say how much of detection performance comes from learned representations versus architectural priors and head capacity.
- **Falsifiable hypothesis:** A frozen random backbone with a trained head achieves a nontrivial fraction of pretrained AP (operationally, over a third on COCO), and the fraction grows with head capacity, revealing substantial architectural prior.
- **Cheapest experiment:** Train heads on frozen random vs frozen pretrained backbones at two head capacities; four short training runs.
- **ROI estimate:** medium

### W2-C-0119 - Rank stability under benign transforms predicts AP without labels

- **Problem:** Estimating detector quality on unlabeled deployment data is an open problem; the stability of confidence rankings under label-preserving transforms might be a free, label-less quality signal.
- **Falsifiable hypothesis:** The rank correlation of detection confidences across benign transforms (small shifts, mild color jitter) of the same images predicts held-out AP across models and domains with correlation above 0.8.
- **Cheapest experiment:** Compute the stability statistic and true AP for 10 models across 5 datasets; inference only.
- **ROI estimate:** high

### W2-C-0120 - Class frequency as a feature: balanced training can hurt balanced testing

- **Problem:** Class rebalancing assumes natural frequency is a nuisance, but frequency priors may be genuine signal that detectors exploit even on balanced test sets via context correlations.
- **Falsifiable hypothesis:** Detectors trained on natural class frequencies outperform frequency-balanced training even on class-balanced test sets, because frequency correlates with informative context statistics.
- **Cheapest experiment:** Two matched training runs (natural vs balanced sampling) evaluated on balanced and natural test splits; two training runs.
- **ROI estimate:** medium

### W2-C-0121 - Action at a distance: local perturbations flip detections elsewhere in the image

- **Problem:** Detection pipelines couple predictions through shared features and NMS, so a small local perturbation might flip detections far away, a nonlocality that has safety implications and no systematic characterization.
- **Falsifiable hypothesis:** Optimized small patches confined to background regions can suppress or create detections at distances beyond any receptive-field overlap, and the effect operates primarily through score-ranking interactions in suppression.
- **Cheapest experiment:** Run patch optimization against 2 detectors with NMS on 100 images, ablate the effect with NMS removed; small adversarial-optimization compute.
- **ROI estimate:** medium

### W2-C-0122 - Train-test duplication in detection benchmarks: a contamination census

- **Problem:** Near-duplicate images across train and test splits inflate benchmark scores, and no recent audit quantifies this for major detection datasets and web-pretrained models.
- **Falsifiable hypothesis:** Perceptual-hash and embedding-based auditing finds a nonzero contamination rate in popular detection benchmarks, and models score measurably higher on contaminated test images than on matched clean ones.
- **Cheapest experiment:** Run duplicate detection between train/test of 3 benchmarks and between web-pretraining corpora and test sets where feasible, compare per-image AP on flagged vs clean subsets; analysis only.
- **ROI estimate:** high

### W2-C-0123 - Does double descent exist for dense prediction

- **Problem:** Double descent is documented for classification, but detection couples classification with regression and matching, and whether the phenomenon appears in dense tasks is unknown.
- **Falsifiable hypothesis:** COCO AP as a function of model width exhibits a measurable non-monotonic region near the interpolation threshold of the classification subtask, i.e. double descent survives task compositionality.
- **Cheapest experiment:** Train a width ladder (8 widths) of a small detector on a subsampled dataset to reach interpolation; eight small training runs.
- **ROI estimate:** low

### W2-C-0124 - Vocabulary ordering effects in open-vocab detectors

- **Problem:** Open-vocab detectors consume class lists whose ordering should be irrelevant, yet tokenization, truncation, and attention position effects may make output depend on class order.
- **Falsifiable hypothesis:** Permuting the inference vocabulary order changes per-class AP beyond numerical noise for at least some open-vocab architectures, revealing an unphysical sensitivity.
- **Cheapest experiment:** Evaluate 3 open-vocab detectors under 10 random vocabulary permutations on COCO; inference only.
- **ROI estimate:** medium

### W2-C-0125 - Boxes snap to the stride grid: quantization artifacts in outputs

- **Problem:** Detector box coordinates may cluster on the feature-stride grid, an artifact that inflates or deflates IoU systematically at small scales and has never been measured across architectures.
- **Falsifiable hypothesis:** Output box coordinates show significant spectral peaks at stride harmonics, the effect grows as object size shrinks, and grid-aware post-hoc decoding improves small-object AP for free.
- **Cheapest experiment:** Fourier-analyze coordinate residuals of cached predictions from 6 detectors, then test a de-quantization correction; analysis only.
- **ROI estimate:** medium

### W2-C-0126 - Canonical-orientation advantage survives rotation augmentation

- **Problem:** If detectors remain better at canonical orientations despite rotation augmentation, augmentation is not delivering the invariance the community assumes it buys.
- **Falsifiable hypothesis:** Detectors trained with rotation augmentation still show a measurable AP advantage at canonical orientations for orientation-canonical classes, indicating augmentation reshapes but does not equalize the orientation prior.
- **Cheapest experiment:** Evaluate rotation-augmented public models on synthetically rotated test suites, plot AP vs rotation angle per class; inference only.
- **ROI estimate:** low

### W2-C-0127 - Early checkpoints are OOD-robust: the robustness-accuracy trade along training time

- **Problem:** If mid-training checkpoints are more robust under shift while worse in-distribution, checkpoint selection is silently choosing a robustness trade-off nobody is measuring.
- **Falsifiable hypothesis:** Relative AP drop under corruption and cross-dataset shift decreases early in training and then worsens as in-distribution AP keeps rising, producing a robustness-optimal checkpoint distinct from the AP-optimal one.
- **Cheapest experiment:** Evaluate a dense checkpoint trajectory of one standard training run on clean and shifted suites; one training run with checkpointing plus inference.
- **ROI estimate:** medium

### W2-C-0128 - Deleting the hardest training images can raise AP

- **Problem:** If a small fraction of training images (heavy noise, pathological annotations) hurts optimization, dataset pruning would beat dataset growth in some regimes, contradicting more-data instincts.
- **Falsifiable hypothesis:** Removing the training images with highest per-image loss variance across seeds improves final COCO AP relative to training on the full set, and the removed set is enriched for annotation errors on inspection.
- **Cheapest experiment:** Score training images by cross-seed loss variance from 2 cheap runs, retrain without the top 5 percent, compare; three training runs.
- **ROI estimate:** medium

### W2-C-0129 - Ensemble disagreement is an annotation-error detector

- **Problem:** Auditing datasets for annotation errors is expensive; if model committees disagree precisely where labels are wrong, disagreement is a free auditing signal with measurable precision.
- **Falsifiable hypothesis:** Instances where a diverse detector ensemble agrees with each other but disagrees with GT are enriched for annotation errors at a precision above 70 percent, validated by human adjudication.
- **Cheapest experiment:** Rank COCO val GT instances by ensemble-vs-GT disagreement, human-verify the top 300; inference plus small annotation.
- **ROI estimate:** high

### W2-C-0130 - White balance flips classes: color constancy failures in detection

- **Problem:** Detectors may rely on absolute color in ways that break under plausible white-balance shifts, a failure mode invisible in standard benchmarks captured under favorable processing.
- **Falsifiable hypothesis:** Physically plausible white-balance shifts (within camera-realistic ranges) change predicted classes for a measurable fraction of instances, concentrated in color-diagnostic categories.
- **Cheapest experiment:** Apply camera-calibrated white-balance transforms to COCO val, measure class-flip rates per category for 4 detectors; inference only.
- **ROI estimate:** low

### W2-C-0131 - Training with box jitter improves calibration for free

- **Problem:** Annotation noise is usually treated as harm, but injecting controlled box jitter during training might act as a calibration regularizer without hurting AP, which would be a cheap deployment win.
- **Falsifiable hypothesis:** Training with small random box jitter yields detectors with measurably better confidence-IoU calibration at unchanged AP, across two architectures.
- **Cheapest experiment:** Four training runs (2 architectures x jitter on/off), measure AP and spatial calibration; four short runs.
- **ROI estimate:** low

### W2-C-0132 - Batch composition effects: who shares your batch changes what you learn

- **Problem:** With batch-dependent statistics and loss normalization, the semantic composition of batches could have lasting effects on detection training beyond learning-rate schedules, an untested source of irreproducibility.
- **Falsifiable hypothesis:** Controlling batch composition (semantically clustered vs dispersed batches) at fixed data and schedule changes final AP beyond seed noise, revealing an unmanaged training hyperparameter.
- **Cheapest experiment:** Three training runs with different batch-composition policies plus seed replicates on a small detector; six short runs.
- **ROI estimate:** low

### W2-C-0133 - Typographic hijacking of open-vocab detectors by scene text

- **Problem:** Open-vocab detectors couple image regions to text embeddings, so written words in the scene may hijack detections (a sticker saying banana on a stop sign), a deployment-relevant confusion channel that is unmeasured at detection granularity.
- **Falsifiable hypothesis:** Inserting printed class names into scenes creates false detections of those classes localized on the text region at rates far above matched non-word textures, for multiple open-vocab architectures.
- **Cheapest experiment:** Paste rendered words vs matched scrambled-letter controls into 500 images, compare false-fire rates; compositing plus inference.
- **ROI estimate:** medium

### W2-C-0134 - Asymmetric cross-dataset generalization: why does A beat B transfer to B but not vice versa

- **Problem:** Cross-dataset transfer between similar detection datasets is often strongly asymmetric, and the field lacks a validated explanation (diversity, label style, image quality) for the direction of the arrow.
- **Falsifiable hypothesis:** Transfer asymmetry between dataset pairs is predicted by a label-convention divergence measure and not by raw dataset size or image diversity, isolating annotation style as the causal factor.
- **Cheapest experiment:** Cross-train and cross-test small detectors over 4 dataset pairs, regress asymmetry on candidate factors; eight short training runs.
- **ROI estimate:** medium

### W2-C-0135 - Co-occurrence overrides appearance: keyboard detected beside monitor-shaped blobs

- **Problem:** Detectors may fire on contextual configurations rather than object appearance, so an appearance-free blob in a canonical context could be detected as the expected object, quantifying context dominance.
- **Falsifiable hypothesis:** Replacing an object with a shape-matched featureless blob preserves detection of its usual co-occurring partner classes at high confidence, and even yields detection of the blob itself as the expected class in a measurable fraction of scenes.
- **Cheapest experiment:** Blob-substitute 500 instances from strong co-occurrence pairs, run 4 detectors, measure context-driven detection rates; compositing plus inference.
- **ROI estimate:** medium

### W2-C-0136 - Seed variance vs published deltas: how much of the leaderboard is luck

- **Problem:** Detection papers rarely report seed variance, so the community cannot tell what fraction of claimed improvements exceed run-to-run noise, a foundational measurement that is simply missing at scale.
- **Falsifiable hypothesis:** The cross-seed standard deviation of COCO AP for standard recipes is large enough that a substantial fraction of published year-over-year improvements fall within two standard deviations of seed noise.
- **Cheapest experiment:** Train 10 seeds each of 3 standard recipes, publish the variance components, compare with a curated list of published deltas; thirty short-to-medium runs, the single most reusable dataset this cluster could produce.
- **ROI estimate:** high

### W2-C-0137 - The interpolation-kernel hyperparameter nobody reports

- **Problem:** Image resize kernels (bilinear, bicubic, area, antialias flags) differ across frameworks and are rarely reported, yet they change small-object statistics and may shift AP measurably.
- **Falsifiable hypothesis:** Switching resize kernels between common defaults changes COCO AP-small by amounts comparable to published method improvements, and mismatched train-test kernels cause a further systematic drop.
- **Cheapest experiment:** Evaluate 5 pretrained detectors under a grid of test-time resize kernels, and finetune one model under two kernels; mostly inference plus two short runs.
- **ROI estimate:** medium

### W2-C-0138 - Dataset-of-origin is readable from local patches: fingerprints and their leakage

- **Problem:** If small patches suffice to classify which dataset an image came from, detectors can exploit dataset fingerprints as shortcuts, undermining cross-dataset conclusions in ways quantifiable by patch classifiers.
- **Falsifiable hypothesis:** A shallow classifier on 32x32 patches distinguishes major detection datasets far above chance, and detector features trained on those datasets encode the same fingerprint dimensions, measurable by probing.
- **Cheapest experiment:** Train a patch classifier across 4 datasets, probe detector features for fingerprint recoverability; small training runs.
- **ROI estimate:** medium

### W2-C-0139 - NMS destroys usable ranking information: pre-suppression logits know more

- **Problem:** Suppression discards nearly-duplicate candidates whose scores collectively carry information about localization uncertainty and ranking quality that single surviving boxes lack.
- **Falsifiable hypothesis:** A post-hoc re-scorer using pre-NMS candidate sets (score distributions over duplicates) improves final AP and calibration over standard NMS output without retraining, proving suppression loses recoverable information.
- **Cheapest experiment:** Implement candidate-set re-scoring on cached pre-NMS outputs of 3 detectors; analysis only.
- **ROI estimate:** medium

### W2-C-0140 - Partial freezing beats full finetuning: mapping implicit regularization

- **Problem:** Occasional reports that freezing random weight subsets improves transfer suggest an unmapped implicit-regularization effect that could deliver free gains in detection finetuning.
- **Falsifiable hypothesis:** For detection finetuning on small datasets, freezing a random fraction of backbone parameters outperforms full finetuning, with an optimal freeze fraction that grows as the dataset shrinks.
- **Cheapest experiment:** Grid over freeze fractions on 3 dataset sizes with one detector; twelve short runs.
- **ROI estimate:** low

### W2-C-0141 - Border effects: padding values leak into detections at image edges

- **Problem:** Zero-padding and letterboxing conventions create artificial statistics at image borders that may systematically distort detections near edges, an artifact never audited across architectures.
- **Falsifiable hypothesis:** Detection recall and box accuracy degrade within a boundary band whose width matches the receptive-field halo of padding, and replacing zero-padding with reflective padding at inference shifts detections measurably without retraining.
- **Cheapest experiment:** Compare edge-band vs interior AP on cached predictions, then re-run inference with altered padding for 3 detectors; inference only.
- **ROI estimate:** low

### W2-C-0142 - Semantic instability of class names: person vs human vs pedestrian

- **Problem:** Open-vocab systems treat class-name choice as a detail, but near-synonymous names may produce materially different detectors, meaning reported numbers are name-conditional in an unreported way.
- **Falsifiable hypothesis:** AP for the same visual category varies by several points across near-synonymous prompt names, and the best name differs across architectures, making single-name evaluation misleading.
- **Cheapest experiment:** Evaluate 3 open-vocab detectors under 8 synonym sets on COCO categories; inference only.
- **ROI estimate:** medium

### W2-C-0143 - Left-right asymmetry: photographer bias becomes model bias

- **Problem:** Human photos have systematic left-right composition biases; if detectors inherit them, horizontal flips at test time should change results in structured ways that reveal learned spatial priors.
- **Falsifiable hypothesis:** Per-class AP differs measurably between original and mirrored test sets for classes with strong composition biases, and the asymmetry correlates with position statistics in training data.
- **Cheapest experiment:** Evaluate 5 detectors on flipped COCO val, correlate per-class asymmetry with train position statistics; inference only.
- **ROI estimate:** low

### W2-C-0144 - Mixed precision changes small-object results beyond noise

- **Problem:** AMP is assumed numerically innocuous, but small objects live in low-magnitude feature regimes where reduced precision could bite, and nobody has isolated this effect for detection.
- **Falsifiable hypothesis:** Training and inference precision changes (FP32 vs FP16 vs BF16) shift AP-small beyond cross-seed noise while leaving AP-large unchanged, revealing a precision-sensitivity gradient with object size.
- **Cheapest experiment:** Six runs (3 precisions x 2 seeds) of one detector, plus precision-swapped inference on fixed checkpoints; six short runs.
- **ROI estimate:** low

### W2-C-0145 - Vocabulary interference: longer class lists degrade detection of the same classes

- **Problem:** Open-vocab detection quality on a fixed target class may depend on what else is in the query vocabulary, an interference effect with direct API-design consequences that is unquantified.
- **Falsifiable hypothesis:** AP on a fixed set of target classes decreases monotonically as unrelated distractor classes are added to the inference vocabulary, and the decay rate differs enough across architectures to change model choice for large-vocabulary applications.
- **Cheapest experiment:** Evaluate 3 open-vocab detectors on fixed targets with vocabulary sizes from 10 to 5,000; inference only.
- **ROI estimate:** high

## Cluster 5: Negative results that would change practice (W2-C-0146 - W2-C-0175, 30 ideas)

### W2-C-0146 - Attention maps fail sanity checks as detection explanations

- **Problem:** Attention visualizations are routinely presented as explanations of detection decisions; if they fail randomization and deletion sanity checks, a large body of interpretability practice in detection is invalid.
- **Falsifiable hypothesis:** Attention-based explanation maps for detections are insensitive to randomization of late-layer weights and their high-attention regions are not causally necessary (deletion barely changes the detection), failing both standard sanity checks.
- **Cheapest experiment:** Apply weight-randomization and deletion tests to attention explanations of 3 detection transformers on 200 detections; inference-scale compute.
- **ROI estimate:** high

### W2-C-0147 - Web-scale pretraining saturates for detection: the flat tail of the data curve

- **Problem:** The assumption that another order of magnitude of pretraining data will lift dense-task transfer keeps enormous scraping efforts alive; a measured saturation point would redirect that effort.
- **Falsifiable hypothesis:** Detection finetuning AP as a function of pretraining corpus size is flat within noise beyond a corpus size achievable at academic scale, for fixed model capacity.
- **Cheapest experiment:** Use public checkpoint families pretrained on nested data scales, finetune identical detection heads, plot the curve; several finetunes only.
- **ROI estimate:** medium

### W2-C-0148 - Video architectures vs frame detector plus tracker: an equal-compute showdown

- **Problem:** Dedicated video detection architectures are compared against weak frame baselines; if a strong frame detector plus a trivial temporal smoother wins at equal compute, the subfield needs redirection.
- **Falsifiable hypothesis:** At matched total inference FLOPs, a strong single-frame detector with score smoothing along tracks matches or beats dedicated video detection architectures on standard benchmarks.
- **Cheapest experiment:** Tune a frame-detector-plus-smoother pipeline at the FLOP budget of 2 video architectures, compare on ImageNet-VID and OVIS; inference plus light tuning.
- **ROI estimate:** high

### W2-C-0149 - Uncertainty methods do not improve detection decisions at matched cost

- **Problem:** MC dropout and deep ensembles are promoted for detection UQ, but if their decision-utility gain disappears once compute is matched against simply using a bigger or better-calibrated single model, current UQ practice is misallocated compute.
- **Falsifiable hypothesis:** At matched inference compute, a single larger detector with post-hoc calibration achieves equal or better risk-coverage utility than MC-dropout or ensemble UQ on the same architecture family.
- **Cheapest experiment:** Compare risk-coverage curves of ensemble/MC variants vs compute-matched single models on COCO and a shifted set; inference plus calibration fitting.
- **ROI estimate:** high

### W2-C-0150 - Domain adaptation for detection loses to 50 labeled target images

- **Problem:** Unsupervised domain adaptation methods for detection claim to avoid target labeling, but if a trivial finetune on a tiny labeled target set dominates them, the practical case for UDA collapses for most applications.
- **Falsifiable hypothesis:** Finetuning on 50 labeled target-domain images beats published unsupervised adaptation methods on standard detection UDA benchmarks, at a labeling cost under one annotator-day.
- **Cheapest experiment:** Label-budgeted finetunes vs public UDA results on 3 standard benchmark pairs; a few short finetunes.
- **ROI estimate:** high

### W2-C-0151 - Curriculum learning does nothing for detection: a preregistered replication

- **Problem:** Curriculum strategies keep being proposed for detection without a preregistered, seed-replicated null test; establishing the null would save the community recurring effort.
- **Falsifiable hypothesis:** Across easy-to-hard curricula defined by object size, count, and loss, no curriculum beats shuffled training beyond seed noise on COCO at matched compute.
- **Cheapest experiment:** Preregister analysis, run 3 curricula x 3 seeds vs 3 shuffled seeds on one detector; nine short runs.
- **ROI estimate:** medium

### W2-C-0152 - Learned augmentation policies for detection: no transfer, no gain

- **Problem:** AutoAugment-style searched policies for detection are expensive and assumed portable; a demonstration that they neither transfer across datasets nor beat simple jitter would retire a costly practice.
- **Falsifiable hypothesis:** Searched augmentation policies transferred across detection datasets perform no better than a two-parameter scale-color jitter baseline at matched training compute.
- **Cheapest experiment:** Train with transferred searched policies vs simple jitter on 2 datasets and 2 detectors; eight short runs.
- **ROI estimate:** medium

### W2-C-0153 - FPN variants under equal tuning: does neck research replicate

- **Problem:** Successive neck designs (path aggregation, bidirectional fusion) claim steady gains over FPN, but the baselines were rarely given equal tuning budgets, casting doubt on the cumulative story.
- **Falsifiable hypothesis:** Under equal hyperparameter search budgets, modern neck variants provide no significant AP gain over a well-tuned FPN across two detector families.
- **Cheapest experiment:** Matched search-budget tuning of FPN vs 2 modern necks on 2 detectors; a bounded tuning grid of short runs.
- **ROI estimate:** medium

### W2-C-0154 - Self-training gains evaporate when the confidence threshold is honestly chosen

- **Problem:** Semi-supervised detection pipelines tune pseudo-label thresholds on labeled validation data from the target distribution, a subtle leakage that may account for much of the reported gains.
- **Falsifiable hypothesis:** When pseudo-label thresholds are chosen without target-distribution validation access (transferred from a disjoint dataset), published self-training gains shrink by more than half.
- **Cheapest experiment:** Re-run 2 public semi-supervised detection methods with honestly transferred thresholds; a few training runs.
- **ROI estimate:** high

### W2-C-0155 - SAM auto-labels cap student quality in crowded scenes

- **Problem:** Auto-labeling pipelines using promptable segmenters are replacing human annotation, but in crowded scenes their systematic merge/split errors may impose a hard ceiling on trainable student quality.
- **Falsifiable hypothesis:** Students trained on promptable-model auto-labels of crowded scenes plateau below 80 percent of the human-label student AP regardless of auto-label volume, because merge/split errors are systematic.
- **Cheapest experiment:** Train students on increasing auto-label volumes vs human labels on CrowdHuman; four training runs.
- **ROI estimate:** medium

### W2-C-0156 - Synthetic pretraining gains vanish under a properly tuned real-data schedule

- **Problem:** Papers report synthetic pretraining boosts for detection against real-data baselines with default schedules; if tuning the baseline erases the boost, the synthetic-pretraining literature needs re-founding.
- **Falsifiable hypothesis:** After tuning the real-data-only schedule (longer training, better LR), the AP advantage of synthetic pretraining drops to within seed noise on standard syn2real detection setups.
- **Cheapest experiment:** Tune the real-only baseline with a bounded budget, compare against published synthetic-pretraining results; several short runs.
- **ROI estimate:** medium

### W2-C-0157 - Distilling open-vocab teachers loses exactly the rare classes

- **Problem:** Distillation of open-vocab teachers into fast students is the standard deployment path, but the distillation objective may transfer head-class behavior while discarding the rare-class ability that motivated open-vocab in the first place.
- **Falsifiable hypothesis:** Distilled students retain head-class AP within 1 point of teachers while losing a disproportionate share of tail-class AP, and the loss is not repaired by rebalancing the distillation data.
- **Cheapest experiment:** Distill one open-vocab teacher under 2 data-balance regimes, evaluate frequency-stratified AP; two distillation runs.
- **ROI estimate:** medium

### W2-C-0158 - Temperature scaling does not survive NMS: post-processing breaks calibration

- **Problem:** Calibration is typically applied to raw scores before suppression, but NMS selects extreme order statistics, which re-distorts calibrated probabilities; if standard recipes fail, detection calibration practice must move post-NMS.
- **Falsifiable hypothesis:** Temperature scaling fitted pre-NMS leaves post-NMS outputs materially miscalibrated (selection bias of maxima), while fitting calibration on post-NMS survivors fixes it, across architectures.
- **Cheapest experiment:** Fit and evaluate calibration at both pipeline stages for 4 detectors on COCO; analysis only.
- **ROI estimate:** high

### W2-C-0159 - Active learning for detection fails at realistic batch sizes: a multi-codebase replication

- **Problem:** Active learning papers report gains with small acquisition batches and single codebases; practitioners use large batches, where diversity effects may reduce AL to random sampling.
- **Falsifiable hypothesis:** At acquisition batches of 5,000-plus images, no published detection AL method beats random sampling beyond seed noise, replicated across two codebases and two datasets.
- **Cheapest experiment:** Run 3 AL methods vs random at large batch on 2 datasets with 2 seeds; a bounded set of short training runs.
- **ROI estimate:** high

### W2-C-0160 - CAM-style weak localization does not beat gradient-norm baselines

- **Problem:** A stream of weakly-supervised localization methods builds on class-activation mapping; if trivial gradient-magnitude baselines match them under fair evaluation, the methodological premise needs revision.
- **Falsifiable hypothesis:** Under a shared evaluation protocol with matched backbones, simple input-gradient-norm maps localize objects as well as CAM descendants on standard weak-localization benchmarks.
- **Cheapest experiment:** Evaluate 5 methods and the gradient baseline on CUB/ImageNet localization with one backbone; inference only.
- **ROI estimate:** medium

### W2-C-0161 - Test-time adaptation collapses under continual shift for detection

- **Problem:** Entropy-minimization TTA methods are being ported to detection; their error-accumulation behavior under long, drifting deployment streams may make them worse than frozen models, which practitioners need to know before adoption.
- **Falsifiable hypothesis:** Under continual shift sequences longer than a few thousand frames, current TTA methods degrade below the frozen-model baseline for detection, with collapse onset predictable from update-rate settings.
- **Cheapest experiment:** Run 2 TTA methods vs frozen baseline over long corrupted video streams, track AP over time; inference-scale compute.
- **ROI estimate:** medium

### W2-C-0162 - Adversarial training buys less than it costs for deployed detectors

- **Problem:** Adversarial training for detection sacrifices clean AP for robustness against threat models rarely realized in deployments; an honest cost-benefit accounting could redirect robustness effort toward realistic corruptions.
- **Falsifiable hypothesis:** Under a deployment threat model of physical and compression perturbations (not norm-bounded attacks), adversarially trained detectors are dominated by corruption-augmented training at every point of the clean-robust trade-off curve.
- **Cheapest experiment:** Train both variants at matched compute, evaluate on physical-style and corruption suites; two training runs plus inference.
- **ROI estimate:** medium

### W2-C-0163 - Bigger vocabularies hurt base classes: negative transfer in open-vocab training

- **Problem:** Scaling training vocabularies is assumed harmless for existing classes, but embedding-space crowding may degrade base-class detection, a trade-off that changes how vocabularies should be grown.
- **Falsifiable hypothesis:** Increasing training vocabulary size at fixed data and compute monotonically decreases base-class AP beyond a vocabulary threshold, demonstrating negative transfer within open-vocab training.
- **Cheapest experiment:** Train one open-vocab detector at 4 vocabulary scales with fixed images, track base-class AP; four training runs.
- **ROI estimate:** medium

### W2-C-0164 - Mask refinement modules polish metrics, not measurements

- **Problem:** Boundary-refinement modules improve mask metrics, but downstream scientific uses (cell area, lesion volume) depend on unbiased measurement; refinement may improve IoU while biasing area estimates.
- **Falsifiable hypothesis:** Refinement modules that raise mask AP leave downstream area-estimation bias unchanged or worse, because they optimize boundary placement toward annotation style rather than physical truth.
- **Cheapest experiment:** Compare area-estimation bias against high-precision GT (calibrated microscopy set) with and without refinement modules; inference only.
- **ROI estimate:** medium

### W2-C-0165 - Depth-aware detection heads die by estimated depth

- **Problem:** Methods injecting depth into detection assume depth is available; with estimated monocular depth, error propagation may cancel the benefit entirely, which determines whether the approach is deployable without depth sensors.
- **Falsifiable hypothesis:** Detection gains from GT-depth injection disappear or invert when depth is replaced by monocular estimates, across two depth-aware architectures.
- **Cheapest experiment:** Swap GT depth for estimated depth in 2 public depth-aware detectors, compare AP; inference plus light finetuning.
- **ROI estimate:** medium

### W2-C-0166 - Few-shot detection methods vs a strong finetuning baseline

- **Problem:** Few-shot detection methods are compared against weak finetuning baselines; if modern augmentation and schedules make plain finetuning win, the specialized-methods literature loses its motivation.
- **Falsifiable hypothesis:** Full-detector finetuning with strong augmentation on the few shots beats published few-shot detection methods on standard splits at matched compute.
- **Cheapest experiment:** Tune the finetuning baseline once, run over standard episodes vs published numbers; light finetune compute.
- **ROI estimate:** high

### W2-C-0167 - Positional-encoding variants for detection transformers: a null at scale

- **Problem:** A stream of positional-encoding proposals for detection transformers reports small gains at small scale; testing whether any survive at modern scale would prune the design space for everyone.
- **Falsifiable hypothesis:** At current-standard model and data scale, positional-encoding variants for detection transformers differ by less than seed noise in final AP.
- **Cheapest experiment:** Train 4 encoding variants x 2 seeds at one modern scale; eight training runs, expensive but decisive.
- **ROI estimate:** low

### W2-C-0168 - Loss reweighting equals resampling for long-tail detection

- **Problem:** Long-tail detection papers propose increasingly complex loss reweighting schemes; if simple resampling matches them all in matched setups, the complexity is unjustified.
- **Falsifiable hypothesis:** Under matched compute and tuning budgets, no published reweighting scheme beats class-frequency resampling on LVIS beyond seed noise.
- **Cheapest experiment:** Re-run 3 reweighting schemes and resampling under one shared recipe with 2 seeds each; eight short runs.
- **ROI estimate:** medium

### W2-C-0169 - Semi-supervised detection dies on truly out-of-distribution unlabeled data

- **Problem:** Semi-supervised detection is benchmarked with unlabeled data drawn from the labeled distribution, but real unlabeled pools are OOD; measuring the gain collapse under honest pools would reset expectations.
- **Falsifiable hypothesis:** When the unlabeled pool comes from a different distribution than the labeled set, semi-supervised detection gains shrink to noise or become negative, across two representative methods.
- **Cheapest experiment:** Re-run 2 methods with OOD unlabeled pools (different dataset as pool); a few training runs.
- **ROI estimate:** medium

### W2-C-0170 - Why model soups fail for detection heads

- **Problem:** Weight averaging (soups) works for classification finetunes but is anecdotally unreliable for detection; establishing and explaining the failure would prevent wasted adoption and might reveal loss-landscape structure specific to dense heads.
- **Falsifiable hypothesis:** Averaging independently finetuned detection models damages AP whenever the heads involve matching-dependent losses, and the damage localizes to the head layers (backbone-only averaging still works).
- **Cheapest experiment:** Finetune 4 runs, evaluate full-soup vs backbone-only-soup vs individuals; four short runs plus evaluation.
- **ROI estimate:** medium

### W2-C-0171 - NAS-found detection architectures do not transfer across datasets

- **Problem:** Neural architecture search for detection reports wins on the search dataset; if found architectures underperform hand-designed ones off-dataset, the search is overfitting and the practice needs course correction.
- **Falsifiable hypothesis:** Architectures searched on one detection dataset lose their advantage (or invert) when trained from scratch on a different dataset, across two published NAS results.
- **Cheapest experiment:** Retrain 2 NAS-found and 2 baseline architectures on a held-out dataset; four training runs.
- **ROI estimate:** low

### W2-C-0172 - Region-contrastive pretraining does not beat plain supervised pretraining, compute-matched

- **Problem:** Dense/region-level contrastive pretraining methods claim detection-specific transfer advantages, but comparisons rarely match total pretraining compute against strong supervised recipes.
- **Falsifiable hypothesis:** At matched pretraining compute and data, region-contrastive objectives provide no detection finetuning advantage over modern supervised pretraining.
- **Cheapest experiment:** Two matched pretrainings at modest scale plus identical finetunes; two pretraining runs.
- **ROI estimate:** medium

### W2-C-0173 - Saliency explanations fail the deletion test for detection

- **Problem:** Deletion-based evaluation of explanations exists for classification; applying it rigorously to detection explanations would test whether any current method identifies causally relevant pixels for localization decisions.
- **Falsifiable hypothesis:** For all tested explanation methods, deleting the top-ranked pixels changes detections less than deleting random pixels of matched area from within the box, failing causal validity for localization.
- **Cheapest experiment:** Run deletion curves for 4 explanation methods over 300 detections and 3 detectors; inference-scale compute.
- **ROI estimate:** medium

### W2-C-0174 - Progressive resizing and multi-stage recipes: no benefit at matched compute

- **Problem:** Multi-stage training recipes (small-to-large resolution) persist in practice without controlled evidence at matched total compute; a decisive null would simplify pipelines everywhere.
- **Falsifiable hypothesis:** At matched total training FLOPs, progressive-resolution schedules match but do not beat single-resolution training on final COCO AP.
- **Cheapest experiment:** Two matched-FLOP training runs per architecture on 2 architectures; four training runs.
- **ROI estimate:** low

### W2-C-0175 - Auxiliary geometric tasks do not help detection at matched budgets

- **Problem:** Auxiliary depth/normal/edge prediction heads are claimed to improve detection through richer representations; matched-budget accounting (the auxiliary labels and compute could buy more detection data) is missing.
- **Falsifiable hypothesis:** When the budget spent on auxiliary supervision is converted into additional detection data or training length, plain detection training dominates auxiliary multi-task training.
- **Cheapest experiment:** Three matched-budget runs (aux-task, longer training, more data) on one dataset; three training runs.
- **ROI estimate:** medium

## Cluster 6: Robustness, calibration, uncertainty quantification (W2-C-0176 - W2-C-0200, 25 ideas)

### W2-C-0176 - One temperature does not fit all classes: class-conditional calibration structure

- **Problem:** Detector calibration is corrected globally, but per-class score distributions differ so much that global calibration may leave every individual class miscalibrated in opposite directions.
- **Falsifiable hypothesis:** Class-conditional recalibration reduces deployment decision cost substantially over global calibration, and the per-class temperature correlates with class frequency and intra-class appearance variance.
- **Cheapest experiment:** Fit global vs per-class calibrators on cached predictions of 5 detectors, compare expected cost on held-out data; analysis only.
- **ROI estimate:** medium

### W2-C-0177 - Confidence should predict IoU: spatial calibration as a first-class metric

- **Problem:** Detection confidence is treated as existence probability, but users read it as overall quality including localization; the actual confidence-IoU relationship is weak and unreported.
- **Falsifiable hypothesis:** For most detectors, confidence explains under a quarter of the variance in matched-detection IoU, and adding a cheap IoU-prediction head fixes this without AP cost, changing downstream filtering quality materially.
- **Cheapest experiment:** Measure confidence-IoU correlation on cached predictions of 8 detectors, finetune one IoU head; analysis plus one short finetune.
- **ROI estimate:** high

### W2-C-0178 - Synthetic corruptions do not predict real degradation: a paired-camera study

- **Problem:** Corruption benchmarks apply synthetic noise/blur/weather to clean images; whether robustness rankings on them predict rankings on genuinely degraded captures is the load-bearing assumption of the whole robustness literature.
- **Falsifiable hypothesis:** Detector robustness rankings on synthetic corruption suites correlate poorly with rankings on paired real degraded captures (same scenes through real fog, low light, dirty optics).
- **Cheapest experiment:** Collect a modest paired set (rig with two cameras, one degraded), evaluate 8 detectors on both, compare rank orders; small capture effort plus inference.
- **ROI estimate:** high

### W2-C-0179 - How to ensemble boxes: fusion rules change calibration more than accuracy

- **Problem:** Detection ensembling lacks a principled combination rule (score averaging, box fusion, union-NMS), and the choice may affect calibration and downstream utility more than raw AP, which is what papers report.
- **Falsifiable hypothesis:** Across fusion rules, AP varies little but calibration and risk-coverage utility vary substantially, making fusion-rule choice a calibration decision misclassified as an accuracy decision.
- **Cheapest experiment:** Implement 4 fusion rules over fixed ensemble members, evaluate AP, calibration, and risk-coverage; inference plus analysis.
- **ROI estimate:** medium

### W2-C-0180 - Unknown objects get confident known labels: measuring open-set overclaiming

- **Problem:** Deployed detectors face objects outside their vocabulary and typically shoehorn them into known classes with high confidence; the rate of this overclaiming is a missing standard measurement.
- **Falsifiable hypothesis:** On scenes containing out-of-vocabulary objects, standard detectors assign above-threshold known-class labels to a large fraction of them, and the overclaiming rate is uncorrelated with in-vocabulary AP, making it an independent model-selection axis.
- **Cheapest experiment:** Build an out-of-vocabulary test set from LVIS-minus-COCO classes, measure overclaim rates of 6 COCO detectors; inference only.
- **ROI estimate:** high

### W2-C-0181 - Confidence should fall as occlusion grows: testing monotonicity

- **Problem:** A trustworthy detector should lower its confidence as evidence is progressively hidden, but confidence-vs-occlusion monotonicity has never been tested systematically and violations would matter for safety filtering.
- **Falsifiable hypothesis:** Under progressive controlled occlusion of the same instance, detector confidence is non-monotonic for a substantial fraction of instances, including confidence increases as objects become more hidden.
- **Cheapest experiment:** Progressively occlude 500 instances with sliding masks, log confidence trajectories for 5 detectors; compositing plus inference.
- **ROI estimate:** medium

### W2-C-0182 - Detectors cannot abstain: risk-coverage as a standard detection report

- **Problem:** Selective prediction (abstaining on uncertain images or regions) is essential in deployment, yet detection benchmarks never report risk-coverage behavior, and detector scores may be poor abstention signals.
- **Falsifiable hypothesis:** Image-level abstention driven by simple aggregates of detection scores leaves large fractions of achievable risk-coverage utility unrealized relative to an oracle, and the gap differs across detectors that share the same AP.
- **Cheapest experiment:** Compute risk-coverage curves from cached predictions with several abstention scores for 8 detectors; analysis only.
- **ROI estimate:** medium

### W2-C-0183 - Label-noise dose-response curves for detection losses

- **Problem:** Detection losses (focal, IoU-based, matching-based) have unknown relative sensitivity to annotation noise, so practitioners cannot choose losses based on their data quality.
- **Falsifiable hypothesis:** Injecting controlled box-jitter and class-flip noise produces distinct dose-response curves per loss family, with matching-based losses degrading fastest under box noise.
- **Cheapest experiment:** Train a small detector grid (3 losses x 4 noise doses) on a subsampled dataset; twelve short runs.
- **ROI estimate:** medium

### W2-C-0184 - Real fog vs rendered fog: the atmospheric-model gap

- **Problem:** Fog robustness is trained and tested with scattering models applied to clear images; the residual gap to real fog determines whether simulation suffices, and it has not been isolated with matched scenes.
- **Falsifiable hypothesis:** Detectors hardened on rendered fog recover only part of their AP loss on real fog, and the residual gap is dominated by illumination and contrast structure absent from standard scattering models.
- **Cheapest experiment:** Use existing paired/comparable clear-fog datasets, evaluate fog-hardened vs baseline models on both fog types, decompose errors; inference only.
- **ROI estimate:** medium

### W2-C-0185 - Do learned box variances mean anything: testing aleatoric UQ against controlled ambiguity

- **Problem:** Detectors with probabilistic box heads output variances that are used as uncertainty, but whether these variances track actual ambiguity (vs just object scale) has not been causally tested.
- **Falsifiable hypothesis:** Learned box variances correlate primarily with object size and only weakly with controlled ambiguity (synthetic blur, occlusion of the same instance), failing as ambiguity meters.
- **Cheapest experiment:** Manipulate ambiguity on fixed instances, log variance responses vs size controls for 2 probabilistic detectors; compositing plus inference.
- **ROI estimate:** medium

### W2-C-0186 - Rare classes are overconfident: calibration under class imbalance

- **Problem:** Calibration analyses pool classes, hiding that tail classes may be systematically overconfident because their scores were shaped by few positives, which corrupts threshold transfer to rare categories.
- **Falsifiable hypothesis:** Calibration error grows monotonically as class frequency falls, and frequency-aware calibration transfers thresholds to unseen rare classes better than global calibration.
- **Cheapest experiment:** Stratify calibration by class frequency on LVIS predictions of 4 detectors, fit and test frequency-aware calibrators; analysis only.
- **ROI estimate:** medium

### W2-C-0187 - Focal length and distortion sweeps: detection robustness to camera intrinsics

- **Problem:** Deployment cameras differ from benchmark cameras in intrinsics (focal length, distortion), and detector sensitivity to these parameters is unmeasured because benchmarks fix them implicitly.
- **Falsifiable hypothesis:** Re-rendering test images under swept intrinsics produces AP degradation curves steep enough that intrinsics mismatch explains a meaningful share of reported cross-dataset gaps.
- **Cheapest experiment:** Warp COCO val under parameterized intrinsics changes, evaluate 5 detectors, then compare against actual cross-dataset gaps; inference only.
- **ROI estimate:** medium

### W2-C-0188 - Multi-view consistency as a free robustness audit

- **Problem:** Multi-camera rigs see the same objects from several views; per-object detection consistency across views is a label-free robustness signal that could audit deployed systems continuously, but its relationship to accuracy is unmeasured.
- **Falsifiable hypothesis:** Cross-view detection inconsistency rate correlates strongly with single-view AP measured against labels, enabling label-free monitoring within a stated error band.
- **Cheapest experiment:** Use existing multi-view datasets (nuScenes, Waymo) to compute consistency vs labeled AP across 6 detectors; analysis only.
- **ROI estimate:** high

### W2-C-0189 - Universal patch vulnerability: transfer structure across detector families

- **Problem:** Adversarial patches are studied per-model; whether a shared vulnerability subspace exists across architectures determines whether patch defense is a per-model or ecosystem problem.
- **Falsifiable hypothesis:** Patches optimized jointly on two detector families transfer to unseen families with attack success above 50 percent, indicating a shared vulnerability structure rooted in low-level feature statistics.
- **Cheapest experiment:** Optimize patches on 2 families, test on 4 held-out detectors; bounded adversarial-optimization compute.
- **ROI estimate:** low

### W2-C-0190 - Flicker predicts failure: temporal inconsistency as free uncertainty in video

- **Problem:** Frame-to-frame prediction flicker in video is treated as a nuisance, but it may be a well-calibrated free uncertainty signal identifying which detections are unreliable without any labels.
- **Falsifiable hypothesis:** Per-object flicker statistics predict per-object error (false positive or misclassification) with useful precision, outperforming raw confidence as an error-flagging signal on video benchmarks.
- **Cheapest experiment:** Compute flicker features and error labels on cached video predictions of 4 detectors; analysis only.
- **ROI estimate:** high

### W2-C-0191 - Valid conformal boxes: what is the right nonconformity score for detection

- **Problem:** Conformal prediction promises distribution-free coverage for boxes, but detection has structured outputs (matching, suppression) where naive nonconformity scores may badly over- or under-cover.
- **Falsifiable hypothesis:** Coverage validity and interval efficiency vary widely across candidate nonconformity scores (corner residuals, IoU-based, score-normalized), and a matching-aware score achieves target coverage with intervals half the size of naive scores.
- **Cheapest experiment:** Implement 4 nonconformity scores over cached predictions with held-out calibration split; analysis only.
- **ROI estimate:** medium

### W2-C-0192 - Scaling attacks: detection failures induced by downsampling pipelines

- **Problem:** Production pipelines downsample images before detection; adversarial and accidental aliasing in the resize step can alter detections, an attack and reliability surface that detection benchmarks never exercise.
- **Falsifiable hypothesis:** Content invisible at full resolution but revealed by specific downsampling kernels can create or suppress detections, and common production resize defaults are more vulnerable than antialiased alternatives by a measurable factor.
- **Cheapest experiment:** Construct scaling-attack images against 2 resize kernels, measure detection deltas across 3 detectors; small optimization plus inference.
- **ROI estimate:** low

### W2-C-0193 - Threshold drift under mild shift: the silent killer of deployed detectors

- **Problem:** Deployments fix a confidence threshold tuned on validation data, but mild distribution shift moves the score distribution so the effective operating point drifts, a failure channel distinct from AP loss and rarely measured.
- **Falsifiable hypothesis:** Under mild shifts that reduce AP by under 2 points, the precision at a fixed threshold can degrade several times more than AP suggests, and score-distribution matching restores most of the loss without retraining.
- **Cheapest experiment:** Evaluate fixed-threshold precision vs AP under a battery of mild shifts for 5 detectors, test quantile-matching correction; inference only.
- **ROI estimate:** high

### W2-C-0194 - Perturb-and-agree: cheap input-perturbation UQ vs deep ensembles

- **Problem:** Deep ensembles are the UQ gold standard but cost multiple models; agreement across cheap input perturbations of a single model might recover most of the uncertainty quality at a fraction of the cost.
- **Falsifiable hypothesis:** Detection uncertainty from agreement over K mild input perturbations achieves at least 80 percent of ensemble risk-coverage utility at one-third the compute, uniformly across shift levels.
- **Cheapest experiment:** Compare perturbation-agreement UQ vs a 3-model ensemble on clean and shifted data for 2 architectures; inference-scale compute.
- **ROI estimate:** medium

### W2-C-0195 - Does adversarial pretraining transfer robustness to detection finetunes

- **Problem:** Robust backbones are advertised as robustness sources for downstream tasks, but detection finetuning may erase adversarially learned invariances, and nobody has isolated how much survives.
- **Falsifiable hypothesis:** Detection finetunes of adversarially pretrained backbones retain corruption robustness but lose most norm-bounded adversarial robustness, quantifying which invariances survive task transfer.
- **Cheapest experiment:** Finetune robust and standard backbones identically, evaluate both robustness types; two finetunes plus inference.
- **ROI estimate:** medium

### W2-C-0196 - Low-light detection: ISP-aware augmentation vs raw-domain training

- **Problem:** Low-light robustness work augments processed sRGB images, but real low-light degradation happens before the ISP; whether raw-domain training buys anything over ISP-aware augmentation is an open, deployment-relevant question.
- **Falsifiable hypothesis:** Training on physically modeled raw-domain noise piped through the target ISP beats equivalent sRGB-space augmentation on real night captures by a margin that justifies the pipeline complexity only below a threshold light level.
- **Cheapest experiment:** Two training runs (raw-modeled vs sRGB augmentation) evaluated on public real night detection sets; two training runs.
- **ROI estimate:** medium

### W2-C-0197 - A cheap failure alarm: predicting detector errors from internal features

- **Problem:** Deployments need per-image failure alarms; internal detector features may support a tiny error-predictor head that flags failures more reliably than confidence heuristics, but this has not been benchmarked as a standard component.
- **Falsifiable hypothesis:** A lightweight probe on frozen internal features predicts image-level detection failure (AP below a floor) with a precision-recall profile substantially better than confidence-aggregate baselines, and transfers across mild shifts.
- **Cheapest experiment:** Train the probe on val-split failures of one detector, test under shifts; probe training only.
- **ROI estimate:** high

### W2-C-0198 - Score-distribution drift as an early-warning system for silent model decay

- **Problem:** Deployed detectors decay silently; label-free monitoring from score-distribution drift could provide early warnings, but the lead time between drift signals and actual AP decay is unmeasured.
- **Falsifiable hypothesis:** Distributional drift statistics on detection scores detect AP degradation with useful lead time (drift alarm precedes a 2-point AP drop) across simulated deployment streams.
- **Cheapest experiment:** Simulate deployment streams with gradual shifts, compare drift-alarm timing vs labeled AP trajectories for 3 detectors; inference-scale compute.
- **ROI estimate:** medium

### W2-C-0199 - Gaussian augmentation does not model sensors: shot-noise-matched robustness

- **Problem:** Noise robustness is trained with Gaussian noise, but real sensor noise is signal-dependent (shot noise dominated); the mismatch may leave detectors fragile exactly in dark regions where it matters.
- **Falsifiable hypothesis:** Detectors augmented with physically parameterized shot-read noise beat Gaussian-augmented ones on real high-ISO captures, with the advantage concentrated in dark image regions.
- **Cheapest experiment:** Two training runs (Gaussian vs physical noise model) evaluated on real high-ISO test data; two training runs.
- **ROI estimate:** medium

### W2-C-0200 - Calibrated counting: prediction intervals for object counts from detections

- **Problem:** Many applications consume object counts derived from detections, but no standard method provides calibrated prediction intervals on counts, and naive per-detection independence assumptions are provably wrong under NMS coupling.
- **Falsifiable hypothesis:** Count intervals built from score-threshold sweeps with conformal calibration achieve nominal coverage where independence-based intervals undercover badly, across density regimes.
- **Cheapest experiment:** Construct both interval types from cached predictions on counting-style datasets, measure empirical coverage; analysis only.
- **ROI estimate:** medium

## Cluster 7: Domain shift and synthetic-to-real (W2-C-0201 - W2-C-0225, 25 ideas)

### W2-C-0201 - Decomposing the syn2real gap: content, appearance, and label convention

- **Problem:** The synthetic-to-real detection gap is reported as one number, hiding that it mixes content mismatch (what scenes contain), appearance mismatch (how things look), and label-convention mismatch (how boxes are drawn), each demanding different fixes.
- **Falsifiable hypothesis:** Using controlled renders that vary one factor at a time, the syn2real AP gap decomposes with content mismatch as the largest component for driving scenes, contradicting the appearance-centric focus of current adaptation research.
- **Cheapest experiment:** Render matched scene sets varying content realism vs appearance realism separately in CARLA, train identical detectors, test on real data; a few rendering and training runs.
- **ROI estimate:** high

### W2-C-0202 - Fidelity return-on-effort curves for simulation axes

- **Problem:** Simulation teams invest in geometry, materials, lighting, and sensor modeling without knowing which axis buys the most downstream detection AP per unit of engineering effort.
- **Falsifiable hypothesis:** AP-per-effort curves across fidelity axes are strongly unequal, with sensor modeling (noise, ISP, optics) dominating material realism for detection transfer, enabling rational simulator budgets.
- **Cheapest experiment:** Ablate fidelity axes independently in an open simulator with effort proxies logged, train and test detectors per cell; a bounded grid of renders and short trains.
- **ROI estimate:** medium

### W2-C-0203 - Synthetic data only for the tail: hybrid real-head syn-tail training

- **Problem:** Synthetic data is usually mixed indiscriminately with real data, but its value may concentrate entirely in rare classes where real examples are scarce, changing how synthetic pipelines should be targeted.
- **Falsifiable hypothesis:** Restricting synthetic data to tail classes achieves the same tail-AP gains as full-distribution synthetic mixing at a tenth of the rendering budget, with less head-class interference.
- **Cheapest experiment:** Compare full-mix vs tail-only synthetic augmentation at matched rendering budgets on a long-tail benchmark; two or three training runs.
- **ROI estimate:** medium

### W2-C-0204 - Per-class geography sensitivity of AV detection

- **Problem:** Cross-geography degradation of driving detectors is reported as aggregate AP, hiding that some classes (signage, vehicles) shift much more than others (pedestrians), which matters for what data to collect where.
- **Falsifiable hypothesis:** Per-class AP drop across geographies is highly unequal and predictable from class-specific appearance variance across regions, enabling targeted data collection that recovers most of the gap at a fraction of full-region labeling cost.
- **Cheapest experiment:** Cross-evaluate public models across geographic splits of existing AV datasets, build the per-class shift table; inference only.
- **ROI estimate:** medium

### W2-C-0205 - Small objects break sim transfer first: size-stratified syn2real analysis

- **Problem:** Syn2real studies report pooled AP, but rendering artifacts (aliasing, texture minification) plausibly hit small objects hardest, meaning simulation may be unusable specifically for the small-object regime it is often bought for.
- **Falsifiable hypothesis:** The syn2real AP gap grows monotonically as object size shrinks, and supersampled rendering closes a large share of the small-object gap without any domain adaptation.
- **Cheapest experiment:** Train on standard vs supersampled renders, evaluate size-stratified AP on real data; two renders plus two training runs.
- **ROI estimate:** medium

### W2-C-0206 - Feature-distance domain metrics do not predict AP drop

- **Problem:** Domain gap is routinely quantified with feature-space distances (MMD, Frechet), but whether these numbers predict actual detection AP drop across domain pairs is largely assumed.
- **Falsifiable hypothesis:** Across 20 domain pairs, feature-distance metrics explain under half the variance in AP drop, while a cheap proxy task (unsupervised box-statistics divergence) predicts it substantially better.
- **Cheapest experiment:** Assemble 20 source-target pairs from public datasets, compute candidate predictors vs measured AP drops of fixed models; inference and analysis only.
- **ROI estimate:** high

### W2-C-0207 - Physics-based weather rendering vs GAN translation at matched effort

- **Problem:** Two schools produce bad-weather training data (physical rendering vs learned translation), and practitioners lack a controlled comparison on downstream detection rather than image realism scores.
- **Falsifiable hypothesis:** At matched data volume, physics-based weather augmentation beats GAN translation for detection robustness on real weather, because translation introduces label-geometry corruption that outweighs its realism advantage.
- **Cheapest experiment:** Generate both augmentation sets from the same clear-weather corpus, train matched detectors, test on real weather sets; two training runs.
- **ROI estimate:** medium

### W2-C-0208 - Label conventions are a domain: quantifying annotation-style shift

- **Problem:** Cross-dataset detection drops are attributed to image distribution shift, but annotation-style differences (box tightness, class granularity, crowd handling) constitute a second, unmeasured domain axis.
- **Falsifiable hypothesis:** A convention-translation layer fitted on a small dual-annotated set (images labeled under both conventions) recovers a large fraction of cross-dataset AP drop without touching the images, proving label style is a major gap component.
- **Cheapest experiment:** Dual-annotate 300 images under two dataset conventions, fit the translation, re-evaluate cross-dataset transfer; small annotation plus analysis.
- **ROI estimate:** high

### W2-C-0209 - Scaling laws for rendered data: where does synthetic volume saturate

- **Problem:** Synthetic data pipelines can generate unbounded volume, but the AP-vs-render-count curve and its saturation point for detection are unpublished, so teams over- or under-render blindly.
- **Falsifiable hypothesis:** Detection AP follows a power law in rendered-image count that saturates at a volume determined by asset diversity, not image count, making asset count the binding constraint.
- **Cheapest experiment:** Train on nested render volumes at 2 asset-diversity levels, fit curves; six short training runs on existing sim stacks.
- **ROI estimate:** medium

### W2-C-0210 - What transfers to exotic sensors: RGB-trained detectors on thermal, event, and fisheye

- **Problem:** Practitioners bootstrap exotic-sensor detection from RGB-pretrained models, but which architectural components (backbone layers, necks, heads) carry transferable structure across sensor types is unmapped.
- **Falsifiable hypothesis:** Transfer to thermal and fisheye preserves value mostly in early and mid backbone layers (measurable by layer-wise re-initialization), while event-camera transfer preserves almost nothing, defining sensor-transfer boundaries.
- **Cheapest experiment:** Layer-wise re-init ablations when finetuning one RGB detector onto public thermal, event, and fisheye datasets; a grid of short finetunes.
- **ROI estimate:** medium

### W2-C-0211 - UDA benchmark rankings vs real deployment pairs: external validity check

- **Problem:** Unsupervised domain adaptation methods are ranked on a handful of canonical benchmark pairs (sim-to-city, city-to-city); whether those rankings generalize to arbitrary real deployment pairs is the field's unexamined external-validity assumption.
- **Falsifiable hypothesis:** Method rankings on canonical UDA detection benchmarks correlate weakly with rankings on freshly constructed deployment-style pairs, indicating benchmark overfitting of the UDA field.
- **Cheapest experiment:** Run 5 public UDA methods on 5 non-canonical pairs assembled from existing datasets, compare rank orders; a bounded set of adaptation runs.
- **ROI estimate:** medium

### W2-C-0212 - Night is an ISP artifact: disentangling photons from processing

- **Problem:** Day-night domain shift conflates photon-level changes with in-camera processing behavior changes (denoising, tone mapping at high gain), and which component breaks detectors determines whether fixes belong in the ISP or the model.
- **Falsifiable hypothesis:** Replaying night raw captures through a day-tuned ISP recovers a substantial share of the night AP drop, showing that a large fraction of the night domain gap is manufactured by processing choices rather than light physics.
- **Cheapest experiment:** Use a raw night dataset, process under two ISP configurations, evaluate fixed detectors; processing plus inference.
- **ROI estimate:** medium

### W2-C-0213 - Asset diversity vs asset count: what actually drives sim transfer

- **Problem:** Synthetic pipelines multiply scenes from limited 3D asset libraries, and the marginal value of a new unique asset vs another instantiation of existing assets is unknown, though it dominates content-creation budgets.
- **Falsifiable hypothesis:** At matched render count, 100 unique assets instantiated 100 times each beat 10 assets instantiated 1,000 times by a large AP margin, and the diversity effect saturates predictably, yielding an asset-budget rule.
- **Cheapest experiment:** Render matched sets at 4 diversity levels, train and evaluate matched detectors; four renders plus four short trains.
- **ROI estimate:** medium

### W2-C-0214 - Randomization breadth vs volume: isolating the active ingredient

- **Problem:** Domain randomization mixes two variables (how broadly parameters vary and how many samples are drawn), and their separate contributions to detection transfer have not been isolated.
- **Falsifiable hypothesis:** Transfer AP depends primarily on randomization breadth with rapidly diminishing returns to volume at fixed breadth, so small broadly-randomized sets beat large narrow ones at equal render cost.
- **Cheapest experiment:** Cross breadth x volume in a 3x3 render grid with matched detectors; nine short training runs.
- **ROI estimate:** medium

### W2-C-0215 - Can simulators evaluate detectors: real2sim validity for rankings

- **Problem:** Evaluating detectors in simulation would be cheap and safe, but whether sim-measured rankings and failure modes match real-world ones (the real2sim eval question) lacks a direct validation study.
- **Falsifiable hypothesis:** Detector rankings measured in a high-fidelity simulator correlate strongly with real-data rankings for aggregate AP but break down for failure-mode-specific metrics (occlusion, night), bounding what simulation can certify.
- **Cheapest experiment:** Evaluate 8 public detectors on matched sim and real scenes, compare rankings globally and per stratum; inference only.
- **ROI estimate:** medium

### W2-C-0216 - Watching confirmation bias happen: class drift in pseudo-label adaptation

- **Problem:** Self-training adaptation is known to reinforce its own errors, but the dynamics (which classes drift, how fast, and what early signals predict collapse) have not been measured longitudinally in detection.
- **Falsifiable hypothesis:** Pseudo-label class distributions drift measurably toward head classes over adaptation rounds, the drift rate predicts final failure, and a simple distribution-anchoring constraint prevents most of it.
- **Cheapest experiment:** Instrument a standard self-training adaptation loop with per-round class-distribution logging on one benchmark pair; a few adaptation runs.
- **ROI estimate:** medium

### W2-C-0217 - How far does amplitude-swap go: the embarrassing FFT baseline for detection UDA

- **Problem:** Fourier amplitude swapping is a trivially cheap domain-alignment trick; establishing how much of published UDA gains it captures would recalibrate the field's sense of progress.
- **Falsifiable hypothesis:** FFT amplitude alignment alone captures more than half of the AP gain of published UDA detection methods on standard benchmarks at essentially zero training complexity.
- **Cheapest experiment:** Train source models with amplitude-swapped augmentation on 3 benchmark pairs, compare against published UDA numbers; three short training runs.
- **ROI estimate:** medium

### W2-C-0218 - The HD-to-SD gap: cross-resolution deployment as a neglected domain axis

- **Problem:** Models trained on high-resolution benchmark imagery are deployed on low-bitrate CCTV and drone feeds; cross-resolution shift is a distinct, quantifiable domain axis that adaptation research largely skips.
- **Falsifiable hypothesis:** Training-resolution mismatch accounts for a larger AP drop than the appearance-domain mismatch in typical surveillance deployments, and resolution-matched finetuning beats generic UDA methods on such pairs.
- **Cheapest experiment:** Construct HD-train SD-test pairs by controlled degradation of existing datasets, compare resolution-matched finetuning vs one UDA method; a few short runs.
- **ROI estimate:** medium

### W2-C-0219 - Seasonal decay curves: measuring detection model rot in fixed deployments

- **Problem:** Fixed-camera deployments experience slow seasonal and infrastructural drift, but the community has no published decay curves quantifying how fast detection quality rots without retraining.
- **Falsifiable hypothesis:** Detection AP in fixed-camera settings decays measurably over months with season as the dominant factor, and a compact set of drift features predicts when retraining is worthwhile.
- **Cheapest experiment:** Use public long-duration camera archives with sparse labeling to estimate quarterly AP of a frozen model; annotation of a few hundred frames per quarter.
- **ROI estimate:** medium

### W2-C-0220 - Synthetic occlusions are too clean: an occlusion-statistics audit of sim datasets

- **Problem:** Simulated datasets claim occlusion coverage, but their occlusion statistics (overlap topology, occluder classes, boundary complexity) may diverge from real scenes, silently limiting transfer for the crowded scenes sim is meant to cover.
- **Falsifiable hypothesis:** Popular synthetic driving datasets differ significantly from real counterparts in occlusion statistics, and re-sampling synthetic scenes to match real occlusion statistics improves transfer AP on occluded strata without new assets.
- **Cheapest experiment:** Compute occlusion-statistics divergence between sim and real datasets, re-sample sim training accordingly, retrain once; analysis plus one training run.
- **ROI estimate:** medium

### W2-C-0221 - Do foundation backbones retire detection UDA: a gap-closure audit

- **Problem:** Domain adaptation methods were developed for ImageNet-pretrained backbones; if modern foundation backbones already close most of the syn2real gap, the UDA toolbox needs re-justification against this new baseline.
- **Falsifiable hypothesis:** Switching to a modern foundation backbone closes more of the syn2real detection gap than the best published UDA method applied to the old backbone, and stacking UDA on the new backbone adds little.
- **Cheapest experiment:** Four training runs (2 backbones x plain vs one UDA method) on a standard syn2real pair; four training runs.
- **ROI estimate:** high

### W2-C-0222 - Known objects in unknown places: compositional shift without appearance shift

- **Problem:** Domain shift research focuses on appearance, but deployment surprises are often compositional (familiar objects in unfamiliar contexts), and detectors' compositional generalization is unmeasured separately from appearance robustness.
- **Falsifiable hypothesis:** Detectors lose substantial AP on context-swapped renders (correct object appearance, implausible context) even with zero appearance shift, and the loss correlates with the strength of learned context priors per class.
- **Cheapest experiment:** Composite objects into implausible contexts with matched lighting using existing assets, evaluate 5 detectors; compositing plus inference.
- **ROI estimate:** medium

### W2-C-0223 - Sim-trained auto-labelers plus human verification: the cost curve nobody published

- **Problem:** A practical syn2real route is to auto-label real data with sim-trained models and pay humans only to verify, but the verification-cost vs final-AP curve that would justify this pipeline is unpublished.
- **Falsifiable hypothesis:** Verification-based labeling reaches 95 percent of full-manual-label AP at under a third of the annotation cost for typical driving scenes, with the ratio predictable from the auto-labeler's precision.
- **Cheapest experiment:** Simulate the pipeline on an already-labeled dataset (verification decisions replayed from GT), sweep verification budgets, train students; analysis plus a few short trains.
- **ROI estimate:** medium

### W2-C-0224 - Renderer fingerprints: does mixing renderers prevent sim-specific overfitting

- **Problem:** Models trained on one renderer may latch onto renderer-specific artifacts (antialiasing patterns, tone mapping), and whether multi-renderer blending prevents this overfitting is untested despite being cheap to implement.
- **Falsifiable hypothesis:** Detectors trained on one renderer transfer worse to real data than matched-volume multi-renderer blends, and a renderer-classifier probe on their features confirms fingerprint absorption as the mechanism.
- **Cheapest experiment:** Train on single vs blended renders from 2 open simulators at matched volume, probe features for renderer identity; three training runs plus probes.
- **ROI estimate:** medium

### W2-C-0225 - Depth-sensor simulation gap for RGB-D detection

- **Problem:** RGB-D detection research uses simulated depth with idealized noise, but real depth sensors fail in structured ways (edges, dark and specular surfaces), and the transfer cost of the idealization is unquantified.
- **Falsifiable hypothesis:** RGB-D detectors trained on idealized simulated depth lose most of their depth-derived advantage on real sensor data, and injecting a measured sensor-noise model during training recovers the majority of it.
- **Cheapest experiment:** Train with idealized vs measured-noise-model depth on existing RGB-D datasets, evaluate on real captures; two training runs.
- **ROI estimate:** low

## Cluster 8: SR, restoration, generation, diffusion tied to dense prediction (W2-C-0226 - W2-C-0250, 25 ideas)

### W2-C-0226 - Does super-resolution help detection or just fool metrics

- **Problem:** SR is routinely inserted before small-object detection, but SR models hallucinate plausible texture; the community has not separated genuine information recovery from hallucination that happens to please detectors trained on similar priors.
- **Falsifiable hypothesis:** SR preprocessing improves small-object AP on benchmark data but yields zero or negative gains on a ground-truth-controlled setup (real high-res images downsampled, detection compared against the true high-res content), exposing part of reported SR gains as shared-prior artifacts.
- **Cheapest experiment:** Build a controlled pipeline (true HR, downsample, SR, detect) on COCO and VisDrone, compare against direct low-res detection and true-HR upper bound for 3 SR models x 3 detectors; inference only.
- **ROI estimate:** high

### W2-C-0227 - Perceptual SR quality and detection utility are anti-correlated in the hallucination regime

- **Problem:** SR models are ranked by perceptual metrics (LPIPS, user studies), but downstream detection cares about factual content; the relationship between perceptual rank and detection utility across the fidelity-hallucination spectrum is unmeasured.
- **Falsifiable hypothesis:** Beyond a fidelity threshold, SR models with better perceptual scores produce worse detection truthfulness (more spurious and shifted detections), making perceptual rank a misleading guide for analytics pipelines.
- **Cheapest experiment:** Score 8 public SR models on perceptual metrics and on detection truthfulness in the controlled HR-downsample protocol; inference only.
- **ROI estimate:** high

### W2-C-0228 - Hallucinated-label noise rates in diffusion-generated detection training data

- **Problem:** Diffusion-generated images with auto-derived boxes are entering detection training sets, but the rate at which generation and auto-labeling jointly fabricate wrong labels (phantom objects, wrong classes) is unreported.
- **Falsifiable hypothesis:** Human audit of popular generated-detection-data pipelines finds label fabrication rates far above accepted human annotation error rates, and training contamination at these rates measurably hurts clean-data AP.
- **Cheapest experiment:** Audit 1,000 generated image-label pairs from a public pipeline, then train with controlled contamination doses; small annotation plus a few short trains.
- **ROI estimate:** high

### W2-C-0229 - Denoise-then-detect vs noise-robust training: an end-to-end accounting

- **Problem:** Pipelines either clean images before detection or train detectors to tolerate noise; the comparison is usually made on image metrics rather than detection outcomes at matched total compute.
- **Falsifiable hypothesis:** Noise-robust detection training dominates denoise-then-detect on real noisy captures at matched inference compute, because denoisers remove small-object evidence along with noise.
- **Cheapest experiment:** Compare both pipelines on real high-ISO data with matched budgets, stratify by object size; one training run plus inference.
- **ROI estimate:** medium

### W2-C-0230 - Detections that exist only after SR are hallucinations: a consistency flag

- **Problem:** When a detection appears in the SR output but has no support in the low-res input, it is likely hallucinated, suggesting a zero-training flag for SR-induced fabrications that analytics pipelines currently lack.
- **Falsifiable hypothesis:** SR-only detections (absent from low-res inference at any threshold) are dominated by hallucinations, verified against true HR content, with precision above 80 percent as a fabrication detector.
- **Cheapest experiment:** In the controlled HR-downsample protocol, compute SR-only detections and verify against true HR labels; analysis only.
- **ROI estimate:** medium

### W2-C-0231 - Restoration erases small objects: measuring the object-destruction rate

- **Problem:** Denoisers and deblurrers are optimized for aggregate image quality and may treat small real objects as noise to remove, a catastrophic failure for downstream detection that image metrics cannot see.
- **Falsifiable hypothesis:** State-of-the-art restoration models measurably erase or degrade a nonzero fraction of true small objects (detectable before, undetectable after restoration against GT), and the erasure rate grows as object size approaches the noise scale.
- **Cheapest experiment:** Run restoration on degraded images with known GT, measure per-size detectability before vs after for 4 restoration models; inference only.
- **ROI estimate:** high

### W2-C-0232 - Generative vs physically-consistent deblurring for video analytics truthfulness

- **Problem:** Generative deblurring produces sharp, plausible frames that may relocate or re-render moving objects, and video analytics consumes these frames as evidence without any truthfulness measurement.
- **Falsifiable hypothesis:** Generative deblurrers shift object positions and alter object identity at rates significantly above physically-constrained deblurring, measurable as detection-box displacement against sharp GT frames.
- **Cheapest experiment:** Use datasets with paired blurred-sharp frames (GoPro-style), compare box displacement and identity flips after each deblurring type; inference only.
- **ROI estimate:** medium

### W2-C-0233 - The bitrate threshold below which artifact removal helps detection

- **Problem:** Compression-artifact removal is applied uniformly before analytics, but it plausibly helps only below some bitrate while wasting compute or hurting above it; the threshold has never been mapped.
- **Falsifiable hypothesis:** Artifact-removal preprocessing improves detection AP only below a codec-specific bitrate threshold, above which it is neutral or harmful, and the threshold is stable across content types.
- **Cheapest experiment:** Sweep bitrate x artifact-removal on-off, evaluate 3 detectors; inference only.
- **ROI estimate:** medium

### W2-C-0234 - Does insertion realism matter: diffusion object insertion vs naive paste for detection training

- **Problem:** Diffusion inpainting can insert objects photorealistically for augmentation, at high compute cost; whether realism (lighting, shadows, harmonization) actually buys AP over naive copy-paste is the economic question nobody has answered cleanly.
- **Falsifiable hypothesis:** Detection gains from object-insertion augmentation are insensitive to insertion realism: naive paste matches diffusion-harmonized insertion at equal instance counts, implying the gains are label-distribution effects.
- **Cheapest experiment:** Three matched training runs (no insertion, naive paste, diffusion insertion) at fixed inserted-instance counts; three training runs.
- **ROI estimate:** high

### W2-C-0235 - Diversity beats fidelity for generative tail-class data

- **Problem:** Generative augmentation for rare classes can spend compute on fidelity (better samples) or diversity (more varied samples), and downstream detection AP should adjudicate this trade-off, not image metrics.
- **Falsifiable hypothesis:** At matched sample count, higher-diversity lower-fidelity generation (higher guidance-scale variance, prompt variety) beats high-fidelity narrow generation for tail-class AP, because coverage matters more than realism for rare classes.
- **Cheapest experiment:** Generate two matched tail-class sets along the fidelity-diversity axis, train matched detectors on LVIS-tail; two training runs plus generation.
- **ROI estimate:** medium

### W2-C-0236 - SR as test-time compute: does it ever beat native high-resolution inference

- **Problem:** SR-then-detect spends compute to upsample before detection, but the same compute could run the detector at higher input resolution directly; the comparison at matched FLOPs is the decision practitioners actually face.
- **Falsifiable hypothesis:** At matched total inference FLOPs, native high-resolution detection dominates SR-then-detect across SR architectures, leaving no compute regime where SR preprocessing is the rational choice.
- **Cheapest experiment:** FLOP-matched grid of SR-plus-detector vs upscaled-input detector on VisDrone; inference only.
- **ROI estimate:** high

### W2-C-0237 - Task-loss SR overfits its detector: transferability of detection-aware SR

- **Problem:** SR models trained with detection-task losses report downstream gains, but if those gains are specific to the detector used in training, the approach fails the modularity requirement of real pipelines.
- **Falsifiable hypothesis:** Detection-aware SR gains collapse when the downstream detector is swapped (different family or training data), revealing the SR model learned detector-specific score inflation rather than information recovery.
- **Cheapest experiment:** Train one detection-aware SR model against detector A, evaluate downstream with detectors B, C, D; one SR training run plus inference.
- **ROI estimate:** medium

### W2-C-0238 - Identity fabrication in face and plate SR: measuring evidentiary harm

- **Problem:** SR applied to faces and license plates fabricates identity-bearing detail, and downstream recognition systems consume it; the fabrication rate as measured by verification models is a safety-critical unknown.
- **Falsifiable hypothesis:** SR of genuinely low-information face and plate crops produces outputs that verification models match to wrong identities at rates far above the low-res baseline, quantifying SR as an evidence-corruption channel.
- **Cheapest experiment:** Downsample identity-labeled face/plate data below the information threshold, SR it, run verification against galleries; inference only.
- **ROI estimate:** medium

### W2-C-0239 - Feature-space SR vs pixel-space SR: where is the small-object bottleneck

- **Problem:** If the information bottleneck for small objects lies in early feature extraction, upsampling backbone features should match pixel SR at far lower cost; the comparison localizes where resolution actually matters.
- **Falsifiable hypothesis:** Learned feature upsampling inside the detector matches pixel-space SR preprocessing on small-object AP at a fraction of the FLOPs, showing the pixel-space detour is wasteful.
- **Cheapest experiment:** Compare pixel-SR preprocessing vs feature-upsampling head modifications at matched accuracy targets; two training runs plus inference.
- **ROI estimate:** medium

### W2-C-0240 - Training on generated images plants fingerprints: bias transfer from diffusion data to detectors

- **Problem:** As generated images enter detection training corpora, detectors may absorb generator-specific artifacts and content biases, changing behavior on real data in ways nobody is monitoring.
- **Falsifiable hypothesis:** Detectors trained with a substantial generated-data fraction show measurable behavioral shifts on real data (class-prior drift toward generator biases, texture-sensitivity changes), detectable even when clean AP is unchanged.
- **Cheapest experiment:** Train matched detectors at 0, 25, and 50 percent generated-data fractions, compare behavioral fingerprints on real probes; three training runs.
- **ROI estimate:** medium

### W2-C-0241 - Synthetic degradations mislead restoration research: detection utility on real degradations

- **Problem:** Restoration models are benchmarked on synthetic degradations; if their detection-utility ranking reverses on real degraded captures, the restoration leaderboard misleads everyone building analytics pipelines.
- **Falsifiable hypothesis:** The ranking of restoration models by downstream detection AP on real degraded data disagrees substantially with their ranking on standard synthetic-degradation benchmarks.
- **Cheapest experiment:** Evaluate 6 restoration models by downstream detection on real low-quality datasets vs synthetic benchmarks; inference only.
- **ROI estimate:** medium

### W2-C-0242 - Text-to-image data vs 3D rendering for detection pretraining at matched cost

- **Problem:** Two synthetic-data routes compete (prompted diffusion generation vs 3D rendering with exact labels), differing in label fidelity and content diversity; a cost-matched downstream comparison for detection does not exist.
- **Falsifiable hypothesis:** At matched dollar cost, 3D-rendered data with exact geometry labels beats diffusion-generated data with derived labels for detection pretraining, because label noise dominates content diversity in the current regime.
- **Cheapest experiment:** Produce cost-matched corpora via both routes for one domain, pretrain and finetune matched detectors; two data pipelines plus two training runs.
- **ROI estimate:** medium

### W2-C-0243 - Objects drift under img2img augmentation: quantifying geometric label corruption

- **Problem:** Img2img diffusion augmentation subtly moves and reshapes objects, corrupting box labels in ways augmented-training pipelines silently absorb; the drift statistics have not been published.
- **Falsifiable hypothesis:** Standard img2img augmentation strengths displace object boundaries by amounts that exceed annotation-noise levels, and training with drift-corrected boxes (re-derived from the augmented image) recovers measurable AP.
- **Cheapest experiment:** Measure box displacement distributions across augmentation strengths using segmentation-model re-localization, then compare training with original vs corrected boxes; analysis plus two short trains.
- **ROI estimate:** medium

### W2-C-0244 - Annotation misalignment when training on SR images with original boxes

- **Problem:** Pipelines that upsample archival low-res datasets with SR reuse the original box annotations, but SR subtly shifts content, creating a systematic train-time label misalignment nobody has quantified.
- **Falsifiable hypothesis:** Training on SR-upsampled images with original-resolution boxes introduces localization bias measurable at test time, and re-deriving boxes on the SR output eliminates it.
- **Cheapest experiment:** Train matched detectors on SR data with original vs re-derived boxes, compare localization error profiles; two short training runs.
- **ROI estimate:** low

### W2-C-0245 - Temporal consistency beats per-frame quality: video SR for video detection

- **Problem:** Video SR models are ranked by per-frame quality, but downstream video detection may care more about temporal consistency of the reconstruction than about any single frame's fidelity.
- **Falsifiable hypothesis:** Across video SR models, downstream video-detection quality correlates more strongly with temporal-consistency measures than with per-frame reconstruction metrics, reversing some model rankings.
- **Cheapest experiment:** Evaluate 5 video SR models by both metric families and by downstream detection on low-res video benchmarks; inference only.
- **ROI estimate:** medium

### W2-C-0246 - Learned codecs and detection: is machine-oriented compression actually better for machines

- **Problem:** Learned compression claims machine-task advantages over classical codecs, but detection evaluations are scattered and rarely bitrate-matched with strong classical baselines properly tuned for analytics.
- **Falsifiable hypothesis:** At matched bitrates with analytics-tuned classical codec settings, learned codecs offer no consistent detection AP advantage in the bitrate range used by real deployments.
- **Cheapest experiment:** Rate-distortion-detection curves for 2 learned codecs vs tuned H.265/JPEG on COCO and a surveillance dataset; inference only.
- **ROI estimate:** medium

### W2-C-0247 - Detection-grounded evaluation of generative models: counting and layout fidelity

- **Problem:** FID-style metrics ignore whether generated scenes have coherent object structure; detectors could measure object-count, co-occurrence, and layout fidelity, giving generative evaluation a dense-prediction foundation.
- **Falsifiable hypothesis:** A detection-grounded scene-structure score separates generative models that FID ranks as equivalent, and correlates better with human judgments of scene coherence than FID does.
- **Cheapest experiment:** Compute detection-based structure statistics on samples from 6 generative models, compare with FID and a small human study; inference plus small study.
- **ROI estimate:** medium

### W2-C-0248 - Which way does SR lie: asymmetry of hallucinated additions vs deletions

- **Problem:** SR errors are treated as symmetric noise, but generative SR may systematically add plausible objects rather than remove real ones (or vice versa), and the error direction determines the harm profile for surveillance vs inspection uses.
- **Falsifiable hypothesis:** Generative SR exhibits a strong asymmetry toward object addition (phantom small objects) over deletion, and the asymmetry grows with the generative prior strength of the SR model.
- **Cheapest experiment:** In the controlled HR-downsample protocol, classify SR-induced detection errors into additions and deletions across 5 SR models; analysis only.
- **ROI estimate:** medium

### W2-C-0249 - Enhancement for humans vs enhancement for detectors: two different optima

- **Problem:** Low-light enhancement is tuned for human-viewed image quality, and deployments reuse the same enhancement for machine analytics, assuming one optimum serves both; the divergence between the two optima is unmeasured.
- **Falsifiable hypothesis:** The enhancement parameter settings maximizing human-rated quality differ systematically from those maximizing detection AP on the same images, and the human-optimal setting sacrifices multiple AP points relative to the machine-optimal one.
- **Cheapest experiment:** Sweep enhancement parameters on real night data, measure detection AP curves and collect small-scale human ratings; inference plus small study.
- **ROI estimate:** medium

### W2-C-0250 - Recapture and re-enhancement loops: pipeline-artifact distributions detectors never trained on

- **Problem:** Real-world images increasingly pass through enhancement, recompression, and screen-recapture loops, creating compound artifact distributions absent from training data, and detector behavior on them is unknown despite their prevalence in user-generated content.
- **Falsifiable hypothesis:** Detection AP on multi-stage-processed images (enhance, compress, recapture) drops substantially more than the sum of single-stage drops predicts, revealing compounding nonlinearity that single-corruption benchmarks miss.
- **Cheapest experiment:** Build a processing-chain corruption suite, evaluate 5 detectors on single vs compound chains; inference only.
- **ROI estimate:** low

## Cluster 9: Long-tail, metric fairness, dataset bias (W2-C-0251 - W2-C-0280, 30 ideas)

### W2-C-0251 - Photographer framing bias: the decentered test set

- **Problem:** Detection datasets inherit photographer composition habits (objects centered, canonical scale and viewpoint), so benchmark AP may overstate performance on machine-captured imagery (fixed cameras, robots) where framing is arbitrary.
- **Falsifiable hypothesis:** Detectors lose substantial AP on a test set re-composed to uniform object position and scale distributions (via crops of wider captures), and the loss exceeds what position statistics alone predict, indicating deeper framing-correlated features.
- **Cheapest experiment:** Construct decentered evaluations by cropping panoramic or wide-angle datasets to controlled framing distributions, evaluate 6 detectors; data wrangling plus inference.
- **ROI estimate:** high

### W2-C-0252 - Geographic performance audit with a purpose-built geo-stratified test set

- **Problem:** Detection models are deployed globally but evaluated on geographically skewed data; per-region AP differences for common classes are anecdotal rather than measured under controlled protocols.
- **Falsifiable hypothesis:** Per-region AP on a geo-stratified test set varies by margins comparable to several years of benchmark progress, and the variation correlates with training-data geographic density per class.
- **Cheapest experiment:** Annotate a modest geo-stratified sample from openly licensed global street imagery under one protocol, evaluate public detectors; annotation budget dominated.
- **ROI estimate:** high

### W2-C-0253 - Class granularity is a hidden progress knob

- **Problem:** Benchmarks decide arbitrarily which concepts get their own class (many dog breeds vs one plant class), and this granularity choice shapes measured progress in ways never quantified.
- **Falsifiable hypothesis:** Re-partitioning benchmark taxonomies at coarser or finer granularity changes both absolute AP and method rankings, with fine-grained partitions penalizing exactly the models that lead current leaderboards.
- **Cheapest experiment:** Re-score cached predictions under merged and split taxonomies built from WordNet on COCO and LVIS; re-analysis only.
- **ROI estimate:** medium

### W2-C-0254 - Do LVIS-tuned long-tail methods survive contact with real deployment tails

- **Problem:** Long-tail detection methods are developed against LVIS's specific tail structure; natural deployment tails (retail catalogs, wildlife cameras) have different shape and semantics, and transfer is assumed rather than measured.
- **Falsifiable hypothesis:** Method rankings on LVIS tail metrics correlate weakly with rankings on naturally long-tailed deployment datasets, exposing LVIS overfitting in the long-tail literature.
- **Cheapest experiment:** Evaluate 5 published long-tail methods on 3 naturally long-tailed public datasets, compare rank orders with LVIS; finetuning plus inference.
- **ROI estimate:** high

### W2-C-0255 - Head-class sacrifice accounting: is total utility actually improved by long-tail methods

- **Problem:** Long-tail methods trade head-class AP for tail-class AP, and whether the trade improves total deployment utility depends on instance frequencies that macro metrics deliberately ignore.
- **Falsifiable hypothesis:** Under instance-frequency-weighted utility (each detection event weighted by its deployment frequency), most published long-tail methods reduce total utility relative to the plain baseline.
- **Cheapest experiment:** Re-score cached predictions of long-tail methods under frequency-weighted utilities across plausible deployment priors; re-analysis only.
- **ROI estimate:** high

### W2-C-0256 - Small and rare are confounded: disentangling size from frequency in long-tail claims

- **Problem:** In natural datasets, rare classes are disproportionately small objects, so long-tail improvements may actually be small-object improvements in disguise, misdirecting the field's causal story.
- **Falsifiable hypothesis:** After stratifying by object size, a large fraction of reported tail-AP gains from representative long-tail methods disappears, showing the methods act through the size channel rather than the frequency channel.
- **Cheapest experiment:** Size-stratified re-analysis of cached predictions from 4 long-tail methods on LVIS; re-analysis only.
- **ROI estimate:** medium

### W2-C-0257 - Watermarks and stock-photo artifacts as shortcut features in web-scraped detection data

- **Problem:** Web-scraped detection corpora contain watermarks, borders, and stock-photo staging correlated with specific classes, providing shortcut features whose contribution to benchmark AP is unmeasured.
- **Falsifiable hypothesis:** Ablating watermark-and-border artifacts at test time (inpainting them away) reduces AP for web-trained detectors on affected classes measurably more than for detectors trained on curated data.
- **Cheapest experiment:** Detect and inpaint watermark artifacts on affected test images, compare AP deltas across differently-trained models; analysis plus inference.
- **ROI estimate:** medium

### W2-C-0258 - Person-detection fairness with proper uncertainty: a benchmark that supports conclusions

- **Problem:** Person-detection fairness studies report subgroup miss-rate gaps without adequate statistical treatment, and dataset sizes often cannot support the published conclusions in either direction.
- **Falsifiable hypothesis:** With subgroup-stratified confidence intervals on adequately powered data, some widely-cited subgroup gaps in person detection are confirmed while others are statistically unsupportable at current benchmark sizes, and the field's evidentiary base needs rebuilding.
- **Cheapest experiment:** Power analysis of existing fairness benchmarks, then targeted annotation to reach adequacy on the underpowered strata, re-evaluate standard detectors; annotation-bounded.
- **ROI estimate:** high

### W2-C-0259 - What counts as an object: annotator salience bias in dataset construction

- **Problem:** Annotators label what draws attention, so datasets encode a salience-filtered definition of objecthood; the unlabeled-but-arguably-object background content shapes both training and the false-positive accounting of every benchmark.
- **Falsifiable hypothesis:** A dense re-annotation pass (label everything nameable) on a benchmark subset finds a large population of unlabeled objects concentrated in low-salience strata, and standard detectors' 'false positives' overlap heavily with this population.
- **Cheapest experiment:** Exhaustively annotate 200 images, quantify the unlabeled-object population, re-score detector false positives against it; annotation-bounded.
- **ROI estimate:** high

### W2-C-0260 - Benchmark monoculture: does COCO ranking predict ranking anywhere else

- **Problem:** Method development optimizes for COCO, assuming its rankings generalize; the cross-benchmark rank correlation that would validate this assumption has not been published systematically for modern methods.
- **Falsifiable hypothesis:** The rank correlation of 15 modern detectors between COCO and each of 10 diverse detection datasets is high for aggregate AP but collapses for size-, density-, and domain-specific strata, meaning COCO ranking is only trustworthy for aggregate claims.
- **Cheapest experiment:** Evaluate 15 public checkpoints across 10 public datasets, compute stratified rank correlations; inference only, highly reusable artifact.
- **ROI estimate:** high

### W2-C-0261 - Which tail is the tail: image, instance, and pixel frequency define different problems

- **Problem:** Long-tail research defines rarity by instance count, but classes can be rare in images, instances, or pixels with different practical consequences, and methods may help one tail while hurting another.
- **Falsifiable hypothesis:** The three rarity definitions produce materially different class orderings on standard datasets, and published long-tail methods improve the instance-count tail while leaving the pixel-count tail (small rare objects) unimproved.
- **Cheapest experiment:** Compute the three tail orderings on LVIS, re-analyze cached long-tail-method predictions per ordering; re-analysis only.
- **ROI estimate:** medium

### W2-C-0262 - Repeat-factor sampling hyperparameters as test-distribution leakage

- **Problem:** Long-tail sampling schemes have hyperparameters commonly tuned against the benchmark's test-frequency profile, a subtle leakage channel that inflates the apparent generality of long-tail recipes.
- **Falsifiable hypothesis:** Repeat-factor-style hyperparameters tuned on LVIS transfer poorly to datasets with different tail shapes, and the transferred configurations underperform simple uniform sampling on some of them.
- **Cheapest experiment:** Sweep sampling hyperparameters on LVIS, apply the best to 3 different-tail datasets vs locally-tuned and uniform baselines; several short trains.
- **ROI estimate:** medium

### W2-C-0263 - Stereotyped contexts imprison tail classes: context-swap evaluation for rarity

- **Problem:** Rare classes appear in few, stereotyped contexts in training data, so models may only detect them there, but tail evaluation never separates context-typical from context-atypical instances.
- **Falsifiable hypothesis:** Tail-class AP on context-atypical instances (measured via context-swapped composites and rare-context real examples) is a small fraction of context-typical AP, and the gap is larger for tail than head classes at matched instance counts.
- **Cheapest experiment:** Composite tail-class instances into atypical contexts, plus mine rare-context real examples, evaluate 4 detectors; compositing plus inference.
- **ROI estimate:** medium

### W2-C-0264 - Duplicate concentration in the tail inflates rare-class metrics

- **Problem:** Web-collected datasets contain near-duplicates that concentrate in rare classes (few source images, many crops), potentially inflating tail metrics through effective train-test leakage within the tail.
- **Falsifiable hypothesis:** Deduplicating tail-class instances across train and test reduces measured tail AP substantially more than head AP, shrinking published long-tail progress.
- **Cheapest experiment:** Run embedding-based duplicate detection per class on LVIS, re-score with duplicates removed; analysis only.
- **ROI estimate:** medium

### W2-C-0265 - Miss-rate parity across density and demographics for crowd person detection

- **Problem:** Person detectors in crowds are used for safety decisions, but miss-rate parity across crowd density levels and demographic subgroups jointly has never been benchmarked, though density and demographics interact (who stands where in crowds).
- **Falsifiable hypothesis:** Detector miss rates show a density-demographic interaction (subgroup gaps grow with density), invisible to marginal audits of either factor alone.
- **Cheapest experiment:** Annotate demographics on an existing dense-crowd benchmark subset, evaluate miss rates in the density-by-subgroup grid for 3 detectors; annotation plus inference.
- **ROI estimate:** medium

### W2-C-0266 - Same word, different concept: cross-dataset taxonomy misalignment as measurable noise

- **Problem:** Cross-dataset training and evaluation assume class names align semantically, but categories like truck, table, or bag cover different visual concepts per dataset, injecting structured noise into every multi-dataset effort.
- **Falsifiable hypothesis:** For a set of shared class names across 4 datasets, models trained on one dataset misclassify a measurable fraction of another dataset's instances of the same-named class, and the confusion structure matches documented definition differences rather than visual difficulty.
- **Cheapest experiment:** Cross-evaluate per-class confusion of single-dataset models across shared names, adjudicate a sample of confusions manually; inference plus small annotation.
- **ROI estimate:** medium

### W2-C-0267 - Benchmarks age: temporal decay of detection AP on contemporary imagery

- **Problem:** Object appearance drifts over years (vehicles, phones, fashion, signage), so models and benchmarks frozen in time may overstate current-world performance, but the decay rate has never been measured for detection.
- **Falsifiable hypothesis:** Detectors trained on decade-old datasets lose AP monotonically on year-stratified contemporary imagery, with class-dependent decay rates largest for design-driven artifacts (phones, cars) and near zero for natural kinds (animals).
- **Cheapest experiment:** Assemble year-stamped test sets from openly licensed imagery, annotate a modest sample per year bucket, evaluate frozen models; annotation-bounded.
- **ROI estimate:** medium

### W2-C-0268 - Tail classes ride on head-class contexts: co-occurrence dependency surgery

- **Problem:** Tail-class detections may depend on co-occurring head-class objects as contextual anchors, making tail performance fragile to context changes in ways aggregate tail metrics cannot reveal.
- **Falsifiable hypothesis:** Removing (inpainting) co-occurring head-class objects from scenes reduces tail-class recall substantially more than removing matched background regions, quantifying contextual dependency of the tail.
- **Cheapest experiment:** Inpaint head-class anchors from 500 tail-class scenes, measure tail recall change across 3 detectors; inpainting plus inference.
- **ROI estimate:** medium

### W2-C-0269 - CLIP-filtered data inherits CLIP blind spots: curation bias propagation

- **Problem:** Modern detection corpora are curated with CLIP-based filtering, so concepts CLIP represents poorly get systematically excluded, propagating one model's blind spots into all downstream datasets and models.
- **Falsifiable hypothesis:** Classes with weak CLIP zero-shot recognition are underrepresented in CLIP-filtered corpora relative to unfiltered crawls, and detectors trained on filtered corpora show correlated per-class weaknesses, tracing a measurable bias-inheritance chain.
- **Cheapest experiment:** Compare per-class frequencies between filtered and unfiltered crawl samples, correlate with CLIP zero-shot scores and with downstream per-class AP; counting plus inference.
- **ROI estimate:** high

### W2-C-0270 - Consent and licensing constraints shape dataset content: an absence audit

- **Problem:** License-conscious datasets exclude imagery from contexts where consent is hard (homes, hospitals, schools), creating systematic domain absences whose downstream detection consequences are unmeasured.
- **Falsifiable hypothesis:** Detectors trained on license-clean corpora underperform specifically on the absent domains relative to web-trained counterparts at matched aggregate AP, quantifying the cost of ethically-constrained data along domain axes rather than aggregate numbers.
- **Cheapest experiment:** Compare per-domain AP of license-clean vs web-trained public models on domain-stratified evaluations; inference only.
- **ROI estimate:** low

### W2-C-0271 - Instance-weighted AP lets dense images dominate: the averaging-axis audit

- **Problem:** Standard AP pools all instances, so a few dense images dominate the metric, while per-image averaging would weight scenes equally; the choice is consequential and undocumented in most papers.
- **Falsifiable hypothesis:** Switching between instance-pooled and image-averaged AP changes method rankings on dense-scene datasets, and the methods advantaged by instance pooling are systematically those tuned on dense benchmarks.
- **Cheapest experiment:** Re-score cached predictions under both averaging conventions on CrowdHuman and VisDrone; re-analysis only.
- **ROI estimate:** medium

### W2-C-0272 - Benchmarks oversample interesting images: difficulty-distribution mismatch with deployment

- **Problem:** Dataset builders select varied, object-rich images, while deployment streams are dominated by boring frames; this difficulty mismatch biases both absolute numbers and method rankings in unknown directions.
- **Falsifiable hypothesis:** Reweighting benchmark evaluation to deployment-like difficulty distributions (mostly sparse frames) changes false-positive-oriented rankings substantially, because methods differ most on empty and near-empty scenes.
- **Cheapest experiment:** Estimate difficulty distributions from public deployment-style streams, reweight benchmark evaluation of 6 detectors accordingly; re-analysis plus light inference.
- **ROI estimate:** medium

### W2-C-0273 - Generative tail augmentation imports generator stereotypes into rare classes

- **Problem:** Teams patch tail classes with generated images, but generators render rare concepts in stereotyped ways, potentially narrowing the very distribution the augmentation was meant to broaden.
- **Falsifiable hypothesis:** Tail classes augmented with generated data improve on generator-typical renditions while stagnating or regressing on real atypical instances, measurable by splitting tail test sets along typicality.
- **Cheapest experiment:** Train with and without generative tail augmentation, evaluate on typicality-split tail test sets; two training runs plus a typicality annotation pass.
- **ROI estimate:** medium

### W2-C-0274 - Occlusion and truncation flags are class-biased: an annotation-quality audit

- **Problem:** Robustness research relies on occlusion/truncation flags, but flag quality likely varies by class and annotator batch, contaminating every occlusion-stratified conclusion downstream.
- **Falsifiable hypothesis:** Re-adjudicating occlusion flags on a stratified sample reveals class-dependent flag error rates large enough to change occlusion-stratified AP comparisons between detectors.
- **Cheapest experiment:** Re-adjudicate flags on 1,000 instances across classes, quantify error structure, propagate corrections into occlusion-stratified evaluation; small annotation budget.
- **ROI estimate:** low

### W2-C-0275 - Person subcategory predictions key on clothing and scene, not people

- **Problem:** Detectors that emit person subcategories (worker, rider, pedestrian) may rely on clothing and background correlations rather than person-intrinsic evidence, which is a fairness and reliability hazard in safety systems.
- **Falsifiable hypothesis:** Counterfactual edits of clothing and background (segmentation-guided recoloring, context swaps) flip person-subcategory predictions at rates far above the same edits' effect on the base person class, exposing spurious feature dependence.
- **Cheapest experiment:** Apply targeted counterfactual edits to 500 instances, measure subcategory flip rates across 3 models; editing plus inference.
- **ROI estimate:** medium

### W2-C-0276 - The tail-progress illusion: are AP-rare gains concentrated in a few easy classes

- **Problem:** Aggregate tail-AP improvements can be driven by a handful of tail classes that are visually easy, while the hard tail stays at zero, but per-class delta distributions are almost never published.
- **Falsifiable hypothesis:** For most published long-tail methods, the majority of AP-rare improvement comes from under a quarter of tail classes, and the median tail class improves negligibly, revising the field's progress narrative.
- **Cheapest experiment:** Compute per-class delta distributions from cached predictions of 5 long-tail methods vs baselines on LVIS; re-analysis only.
- **ROI estimate:** high

### W2-C-0277 - Tracing one bias end-to-end: from pretraining statistics to detection errors

- **Problem:** Bias-inheritance claims (pretraining bias causes downstream detection bias) are plausible but have never been traced quantitatively through the full chain for a single concrete bias.
- **Falsifiable hypothesis:** For a chosen bias axis (indoor vs outdoor context for a class set), pretraining-corpus statistics predict feature-space bias, which predicts detection error asymmetry after finetuning, with each link individually measurable and the chain jointly accounting for most of the final asymmetry.
- **Cheapest experiment:** Instrument all three stages for 2 backbones on one bias axis using public corpora statistics, probes, and stratified detection evaluation; probes plus inference.
- **ROI estimate:** medium

### W2-C-0278 - Standardized budgets for long-tail comparisons: a re-benchmark

- **Problem:** Long-tail methods differ in effective epochs over tail instances, extra passes, and memory banks, so published comparisons conflate method merit with hidden budget differences.
- **Falsifiable hypothesis:** Under strictly matched effective-sample budgets per class, the spread between published long-tail methods on LVIS shrinks by more than half, and the surviving ranking differs from the published one.
- **Cheapest experiment:** Re-train 4 methods under a shared budget-accounting harness with 2 seeds; eight training runs.
- **ROI estimate:** medium

### W2-C-0279 - Open-vocab rarity should be measured against pretraining exposure, not dataset counts

- **Problem:** Open-vocab methods are credited for rare-class performance where rarity is defined by target-dataset counts, but the models' actual exposure comes from web pretraining, making dataset-defined rarity a misleading axis.
- **Falsifiable hypothesis:** Re-defining class rarity by estimated pretraining exposure reorders the rare-class leaderboard of open-vocab detectors and reveals that exposure-rare classes see little of the claimed open-vocab advantage.
- **Cheapest experiment:** Estimate exposure from public caption corpora, re-stratify existing LVIS evaluations by exposure; counting plus re-analysis.
- **ROI estimate:** high

### W2-C-0280 - Dataset dignity for stuff classes: what detection loses by ignoring the uncountable

- **Problem:** Detection taxonomies exclude stuff (road, grass, water) by design, yet many deployment queries concern stuff-object interactions (person on road), and the cost of the thing-only worldview has not been quantified.
- **Falsifiable hypothesis:** For interaction-style queries, pipelines built on thing-only detectors fail at rates far above pipelines with joint thing-stuff representations at matched compute, quantifying the structural cost of the detection taxonomy choice.
- **Cheapest experiment:** Build 200 interaction queries over existing panoptic datasets, compare detector-only vs panoptic pipelines; inference plus query evaluation.
- **ROI estimate:** low

## Cluster 10: Reproducibility and compute-fair comparison (W2-C-0281 - W2-C-0305, 25 ideas)

### W2-C-0281 - Compute-normalized detection leaderboards: AP as a function of training FLOPs

- **Problem:** Detection papers compare endpoint AP while training budgets differ by orders of magnitude, so the literature cannot distinguish methodological progress from compute growth.
- **Falsifiable hypothesis:** When a historical sequence of detection methods is re-trained along matched FLOP budgets, a large fraction of claimed method-over-method gains disappears at equal compute, and the AP-vs-FLOPs frontier moves far less than leaderboards suggest.
- **Cheapest experiment:** Re-train 8 representative methods at 3 matched budget points each with one seed, plot frontiers; a bounded grid of training runs, expensive but foundational.
- **ROI estimate:** high

### W2-C-0282 - The same method across codebases: framework variance vs claimed deltas

- **Problem:** Identical methods produce different AP across mmdetection, detectron2, and YOLO-family codebases, but this framework variance has never been quantified against the size of typical published improvements.
- **Falsifiable hypothesis:** Cross-framework AP variance of the same nominal method exceeds one point for common detectors, overlapping the magnitude of many published method deltas, meaning framework choice is a confound of record.
- **Cheapest experiment:** Train 3 canonical detectors in 3 frameworks under nominally identical configs, 2 seeds each; eighteen short runs.
- **ROI estimate:** high

### W2-C-0283 - Stale baselines: how much of reported progress is baseline decay

- **Problem:** Papers copy baseline numbers from prior work rather than re-running them with modern recipes, so improvements may reflect baseline staleness rather than method merit, an effect size the field has not measured.
- **Falsifiable hypothesis:** Re-running the baselines of 20 recent detection papers with current recipes erases or reverses the claimed improvement in a substantial fraction of cases.
- **Cheapest experiment:** Sample 20 papers with public code, re-train their baselines under the papers' own tuning budgets applied honestly; a bounded set of training runs.
- **ROI estimate:** high

### W2-C-0284 - How many seeds does detection research need: an empirical power standard

- **Problem:** Seed-count conventions in detection are arbitrary because the variance structure of common tasks and recipes is unpublished, so the field cannot say when one seed suffices and when five are needed.
- **Falsifiable hypothesis:** Seed variance varies by an order of magnitude across task regimes (dataset size, schedule length, method family), yielding a practical lookup rule that makes many single-seed papers formally underpowered.
- **Cheapest experiment:** Run 10-seed replicates across a 2x2x2 grid of regimes with small models, publish variance components and the derived seed-count table; many short runs.
- **ROI estimate:** medium

### W2-C-0285 - Shadow tuning: how tuning-budget asymmetry manufactures SOTA

- **Problem:** Papers tune their method extensively while baselines get default configs, an asymmetry whose typical effect size on detection benchmarks has never been isolated experimentally.
- **Falsifiable hypothesis:** Granting the baseline the same hyperparameter search budget as the proposed method closes most of the reported gap in a majority of reproducible recent detection papers.
- **Cheapest experiment:** For 6 papers with released code, spend the paper's stated tuning budget on the baseline instead; a bounded tuning-run grid.
- **ROI estimate:** high

### W2-C-0286 - A decade of adaptive overfitting on test-dev: leaderboard forensics

- **Problem:** Repeated evaluations against the same COCO test-dev split should produce community-level adaptive overfitting, detectable through statistical forensics on submission histories, but no one has run the analysis for detection.
- **Falsifiable hypothesis:** Leaderboard submission statistics show the signature of adaptive overfitting (val-test gap growth over time and regression-to-mean of top entries on fresh data), quantifiable without new annotation using existing val-test paired reports.
- **Cheapest experiment:** Assemble published val and test-dev pairs across years, analyze gap dynamics; literature data collection plus statistics.
- **ROI estimate:** medium

### W2-C-0287 - Do published ablations replicate: sign-flip rates under reseeding

- **Problem:** Ablation tables are the evidentiary core of method papers yet are usually single-seed; the fraction of ablation conclusions that flip sign under reseeding is an unknown, measurable quantity.
- **Falsifiable hypothesis:** Re-running the ablation tables of representative detection papers with 3 seeds flips the sign of a nontrivial fraction of ablation rows, undermining component-level conclusions across the literature.
- **Cheapest experiment:** Reproduce 5 ablation tables (roughly 30 rows) with 3 seeds each using released code; many short runs, bounded scope.
- **ROI estimate:** high

### W2-C-0288 - CUDA and cuDNN versions as silent result modifiers

- **Problem:** Numerical differences across GPU library versions can shift detection results, but the field lacks a measurement of how much environment versioning alone moves AP relative to claimed effects.
- **Falsifiable hypothesis:** Training the same detection config across 3 CUDA/cuDNN stacks produces AP differences beyond within-stack seed noise for at least some standard recipes, establishing environment version as a reportable variable.
- **Cheapest experiment:** Train one recipe x 3 stacks x 3 seeds in containers; nine short runs.
- **ROI estimate:** low

### W2-C-0289 - PIL vs OpenCV: preprocessing divergence as an unreported hyperparameter

- **Problem:** Image decoding and resizing differ subtly across libraries (color conversion, antialiasing), and mixed train-test preprocessing may shift results by amounts that matter, but the effect has not been isolated for detection.
- **Falsifiable hypothesis:** Train-test preprocessing library mismatch shifts COCO AP measurably (with AP-small most affected), and papers that do not report the preprocessing stack are irreproducible at the precision they claim.
- **Cheapest experiment:** Evaluate fixed checkpoints under crossed decode-resize stacks, then finetune under matched vs mismatched stacks; mostly inference plus two short runs.
- **ROI estimate:** medium

### W2-C-0290 - Determinism audit of popular detection repos

- **Problem:** Fixed seeds do not guarantee determinism (data-loading order, atomics, nondeterministic kernels), and the actual reproducibility level of popular detection codebases is undocumented.
- **Falsifiable hypothesis:** A majority of popular detection repos produce different final AP across identical-seed runs, with variance concentrated in data-pipeline nondeterminism rather than kernel nondeterminism, identifiable by controlled toggling.
- **Cheapest experiment:** Run identical-seed replicates in 5 repos with instrumentation isolating nondeterminism sources; several short runs per repo.
- **ROI estimate:** medium

### W2-C-0291 - A reporting-practices census with teeth: re-experiments on the worst gaps

- **Problem:** Meta-claims about poor reporting in detection papers are anecdotal; a systematic census tied to targeted re-experiments would turn the complaint into measured science with actionable standards.
- **Falsifiable hypothesis:** Coding 300 recent detection papers reveals that key reproducibility fields (variance, tuning budget, preprocessing stack, compute) are each reported in under a third of papers, and re-experiments show unreported fields correlate with larger reproduction gaps.
- **Cheapest experiment:** Structured coding of 300 papers plus reproduction of 15 with full instrumentation; reading effort plus bounded compute.
- **ROI estimate:** medium

### W2-C-0292 - Ten detection tricks under matched compute: which survive

- **Problem:** Widely-adopted training tricks (EMA, mosaic, multi-scale, longer schedules, strong jitter) were validated in different eras and codebases; a single matched-compute revisit would establish which still pay their way.
- **Falsifiable hypothesis:** Under one modern recipe with matched compute accounting, at least a third of canonical detection tricks contribute nothing beyond seed noise, and one or more actively hurt.
- **Cheapest experiment:** Factorial-lite design (each trick toggled from a strong base recipe, 2 seeds) on one mid-size detector; roughly 20 short runs.
- **ROI estimate:** high

### W2-C-0293 - Latency claims do not replicate: a standardized detection inference benchmark

- **Problem:** Published detection latency numbers mix batch sizes, precisions, hardware, and warmup conventions, making cross-paper speed claims incomparable in ways that mislead deployment choices.
- **Falsifiable hypothesis:** Re-measuring 15 detectors under one standardized protocol changes latency-based rankings substantially from published claims, and the discrepancy correlates with measurement-convention choices rather than hardware.
- **Cheapest experiment:** One benchmarking harness, 15 public models, 3 hardware targets; pure measurement.
- **ROI estimate:** medium

### W2-C-0294 - Checkpoint selection by test performance: prevalence and inflation size

- **Problem:** Selecting the best checkpoint using test-set metrics is a known but unquantified practice in detection research; its typical inflation size would tell reviewers how much to discount unclear papers.
- **Falsifiable hypothesis:** Best-of-trajectory test selection inflates COCO AP by a measurable margin over last-checkpoint or val-selected reporting, and the inflation grows with evaluation frequency, providing a correction table for meta-analyses.
- **Cheapest experiment:** Instrument several standard training runs with dense checkpointing, compare reporting policies across seeds; a few training runs.
- **ROI estimate:** medium

### W2-C-0295 - Gradient accumulation is not large-batch training: the BN discrepancy audit

- **Problem:** Papers treat gradient accumulation as equivalent to large-batch training, but batch statistics differ, and the size of the resulting discrepancy in detection results is unmeasured folklore in both directions.
- **Falsifiable hypothesis:** Accumulation-vs-true-batch discrepancies in final AP exceed seed noise for BN-bearing detectors and vanish for normalization-free variants, cleanly attributing the effect to batch statistics.
- **Cheapest experiment:** Four training runs (accumulated vs true batch, BN vs GN) with 2 seeds; eight short runs.
- **ROI estimate:** low

### W2-C-0296 - ImageNet init is not one thing: pretrained-weight provenance effects

- **Problem:** Papers write ImageNet-pretrained as if it were a single object, but zoo weights differ across versions and recipes, and downstream detection deltas attributed to methods may ride on provenance differences.
- **Falsifiable hypothesis:** Swapping among commonly-used ImageNet checkpoint provenances for the same architecture shifts downstream detection AP by amounts overlapping published method deltas.
- **Cheapest experiment:** Finetune one detector from 5 different same-architecture pretrained checkpoints, 2 seeds; ten short runs.
- **ROI estimate:** medium

### W2-C-0297 - How much does val reuse cost: adaptive overfitting to validation sets

- **Problem:** Researchers evaluate on val hundreds of times during development, and the resulting val-specific adaptation inflates val-based conclusions by an amount never measured in detection workflows.
- **Falsifiable hypothesis:** A simulated development process (hyperparameter search guided by val) produces models whose val-test gap grows with the number of adaptive queries, quantifying a per-query overfitting tax for detection.
- **Cheapest experiment:** Run scripted adaptive searches of increasing query counts on split-in-half validation data; a grid of short runs plus analysis.
- **ROI estimate:** medium

### W2-C-0298 - Silent benchmark mutations: a hash-audit of public dataset artifacts

- **Problem:** Benchmark annotation files and images change quietly over time (fixes, re-hosting, format migrations), and results across years may be computed against different ground truths without anyone tracking it.
- **Falsifiable hypothesis:** A provenance audit finds multiple materially different versions of widely-used detection benchmark files in circulation, and scoring one model against the variants produces AP differences comparable to published improvements.
- **Cheapest experiment:** Collect circulating copies of 3 benchmarks (mirrors, snapshots), hash-diff them, re-score fixed predictions against variants; pure analysis.
- **ROI estimate:** medium

### W2-C-0299 - Do published improvements stack: the composition test

- **Problem:** Each detection paper claims an additive gain over a shared baseline, implying the field's improvements should compose; the composition experiment (apply all of them together) is never run and would test whether claimed gains are real and independent.
- **Falsifiable hypothesis:** Combining the top 8 published compatible improvements from a recent period yields far less than the sum of claimed individual gains, revealing overlap and interference invisible in per-paper evaluations.
- **Cheapest experiment:** Implement the 8 tricks in one codebase, run baseline, individual, and combined configurations with 2 seeds; a bounded grid of training runs.
- **ROI estimate:** high

### W2-C-0300 - Author-reported vs independently-measured: a systematic reproduction-gap meta-analysis

- **Problem:** Reproduction gaps in detection are documented anecdotally; a systematic paired dataset of author-reported vs independently-reproduced numbers would let the field model where gaps come from.
- **Falsifiable hypothesis:** Across 40 reproducible papers, the mean reproduction gap is measurably negative (independent numbers lower), and gap size is predicted by missing reporting fields more than by method complexity.
- **Cheapest experiment:** Aggregate existing third-party reproduction records (model zoos, reproducibility challenges) and fill targeted gaps with 10 new reproductions; mostly data collection.
- **ROI estimate:** medium

### W2-C-0301 - Energy-honest efficiency claims: end-to-end accounting including search

- **Problem:** Efficient-detection papers report inference FLOPs while ignoring the search and training energy spent finding the efficient design, so the field cannot say whether efficiency research saves energy at the ecosystem level.
- **Falsifiable hypothesis:** For several published efficient detectors, amortized total energy (search plus training plus deployment) exceeds that of tuning a standard architecture to the same accuracy, unless deployment volume exceeds a computable break-even threshold.
- **Cheapest experiment:** Reconstruct energy budgets from paper disclosures and re-measured training costs, compute break-even curves; measurement plus analysis.
- **ROI estimate:** low

### W2-C-0302 - Power tables for the field: minimum detectable effects across popular benchmarks

- **Problem:** No reference exists telling authors the minimum AP difference each popular benchmark can statistically support, so undersized claims proliferate unchecked by reviewers who lack the numbers.
- **Falsifiable hypothesis:** Publishing bootstrap-derived minimum-detectable-effect tables for 15 popular detection benchmarks shows that a large fraction of recent papers claim differences below their benchmark's resolution threshold.
- **Cheapest experiment:** Bootstrap cached predictions across benchmarks, tabulate minimum detectable effects, cross-reference against claims in 100 papers; re-analysis plus survey.
- **ROI estimate:** high

### W2-C-0303 - Tuning on the benchmark generalizes worse: the simplicity dividend

- **Problem:** Methods heavily tuned on a benchmark may generalize off-benchmark worse than simpler untuned approaches, but this generalization penalty of tuning has not been isolated as a measurable quantity in detection.
- **Falsifiable hypothesis:** Across method pairs matched on COCO AP, the more heavily tuned member (by disclosed search budget) performs systematically worse on a battery of unseen datasets, quantifying a tuning-induced generalization tax.
- **Cheapest experiment:** Select tuned-vs-simple pairs from public checkpoints, evaluate on 8 non-COCO datasets; inference only.
- **ROI estimate:** high

### W2-C-0304 - Does code release predict smaller reproduction gaps: an observational test

- **Problem:** Code release is assumed to guarantee reproducibility, but released code with undocumented configs may reproduce no better than clear papers without code; the actual predictive relationship is unmeasured.
- **Falsifiable hypothesis:** In a matched sample of detection papers, code release alone predicts reproduction-gap size weakly, while config completeness (all hyperparameters and environment pinned) predicts it strongly, redirecting what venues should actually require.
- **Cheapest experiment:** Reproduce 20 papers stratified by code and config completeness, regress gap on disclosure features; bounded reproduction compute.
- **ROI estimate:** medium

### W2-C-0305 - Random configurations as the null hypothesis for architecture components

- **Problem:** Published architecture components beat baselines, but the proper null (random configurations from the same design space under the same search budget) is never reported, so component value is confounded with search effort.
- **Falsifiable hypothesis:** Under matched search budgets, random sampling of the design space matches a meaningful fraction of published detection component gains, establishing how much of component research is search rather than insight.
- **Cheapest experiment:** For 2 published design spaces, compare the published component vs best-of-N random configs at the paper's search budget; a bounded grid of short runs.
- **ROI estimate:** medium

## Cluster 11: New combinations with genuine scientific motivation (W2-C-0306 - W2-C-0325, 20 ideas)

### W2-C-0306 - Coverage-preserving suppression: conformal prediction meets NMS

- **Problem:** Conformal prediction can wrap detectors with distribution-free guarantees, but NMS discards the candidate sets those guarantees are computed over, silently destroying coverage; motivation: valid uncertainty must survive the full pipeline, not just the head.
- **Falsifiable hypothesis:** Standard NMS breaks nominal conformal coverage by a measurable margin, and a suppression rule designed to preserve candidate-set coverage restores nominal guarantees at bounded extra prediction-set size.
- **Cheapest experiment:** Measure empirical coverage before and after NMS on cached candidate sets, implement a coverage-aware suppression variant, re-measure; analysis only.
- **ROI estimate:** high

### W2-C-0307 - Inpainting as intervention: a causal-evidence benchmark for detection attribution

- **Problem:** Attribution methods for detection fail sanity checks partly because evaluation lacks ground-truth causal evidence; motivation: inpainting provides real interventions (remove a region, observe the detection), enabling causal validation of explanations.
- **Falsifiable hypothesis:** An intervention benchmark built from systematic inpainting quantifies attribution methods by causal fidelity, and current methods rank near a trivial box-interior baseline, establishing an honest starting point for detection interpretability.
- **Cheapest experiment:** Generate intervention grids for 300 detections, score 5 attribution methods against measured causal effects; inpainting plus inference.
- **ROI estimate:** medium

### W2-C-0308 - Machine psychophysics: staircase procedures for measuring detector thresholds

- **Problem:** Human vision science measures perceptual thresholds with adaptive staircase procedures giving precise psychometric curves; motivation: detectors deserve the same measurement rigor, replacing coarse benchmark averages with threshold functions (contrast, size, occlusion) per model.
- **Falsifiable hypothesis:** Staircase-measured detection thresholds (minimum contrast, minimum size at fixed reliability) differ across architectures in ways aggregate AP does not predict, and threshold functions predict deployment failures better than AP does.
- **Cheapest experiment:** Implement adaptive staircases over parametric image manipulations for 6 detectors, compare threshold maps vs AP; inference-scale compute.
- **ROI estimate:** high

### W2-C-0309 - Item response theory for detection benchmarks: separating instance difficulty from model ability

- **Problem:** Benchmark averages conflate model ability with test-item difficulty; motivation: psychometrics solved this with item response theory, which jointly estimates item difficulty and subject ability, enabling adaptive short tests and difficulty-controlled comparisons.
- **Falsifiable hypothesis:** An IRT model fitted on the per-instance outcomes of many detectors compresses benchmark information into ability scores that reproduce full-benchmark rankings using under a tenth of the test set, and flags misfitting items that turn out to be annotation errors.
- **Cheapest experiment:** Fit IRT on the binary per-instance outcome matrix of 30 public detectors on COCO val, validate short-test ranking fidelity and audit misfit items; pure analysis of cached predictions.
- **ROI estimate:** high

### W2-C-0310 - Design-based test sets: survey sampling for deployment-valid detection estimates

- **Problem:** Test sets are convenience samples, so benchmark estimates carry unknown bias relative to any deployment population; motivation: survey statistics offers design-based sampling and estimators with valid population inference, never applied to detection evaluation.
- **Falsifiable hypothesis:** A stratified probability sample of a deployment image population yields AP estimates with quantified sampling error that differ systematically from convenience-benchmark estimates for the same models, and the direction of the difference is predictable from strata weights.
- **Cheapest experiment:** Define a target population from a public image stream, draw a designed sample, annotate modestly, compare estimates vs convenience benchmarks; annotation-bounded.
- **ROI estimate:** medium

### W2-C-0311 - Metrology for CV: applying measurement-uncertainty standards to detection evaluation

- **Problem:** Engineering metrology has formal standards for stating measurement uncertainty (error budgets, traceability), while CV reports bare point estimates; motivation: importing the error-budget discipline would make benchmark numbers interpretable as measurements.
- **Falsifiable hypothesis:** A full uncertainty budget for COCO AP (annotation noise, sampling error, implementation variance, nondeterminism) shows combined standard uncertainty large enough that many published comparisons are formally inconclusive, and identifies which component to reduce first.
- **Cheapest experiment:** Quantify each budget component from existing sources (re-annotation subsets, bootstrap, cross-framework runs), compose the budget per metrology conventions; mostly analysis.
- **ROI estimate:** high

### W2-C-0312 - Optimal experiment design for ablation studies

- **Problem:** Ablation grids spend compute uniformly over configurations regardless of information value; motivation: optimal experiment design allocates runs to maximize inferential power per FLOP, which matters as training costs grow.
- **Falsifiable hypothesis:** Sequential design (choosing the next ablation run to maximize expected information about component effects) reaches the same conclusions as exhaustive grids at less than half the compute, validated by replaying published full grids.
- **Cheapest experiment:** Replay 3 published full ablation grids as simulation oracles, compare sequential-design trajectories vs exhaustive ordering; pure simulation on existing numbers.
- **ROI estimate:** medium

### W2-C-0313 - Extreme value theory for rare detection failures: tail-risk certificates

- **Problem:** Safety cases need estimates of worst-case failure frequency, which mean AP cannot provide; motivation: extreme value theory is the statistics of rare events and can extrapolate tail risk from finite evaluation, giving detection a principled safety-estimate methodology.
- **Falsifiable hypothesis:** EVT fitted on per-image failure severities extrapolates the frequency of severe failure events (validated on held-out rare events) within stated confidence, where empirical counting fails for events rarer than the test-set size supports.
- **Cheapest experiment:** Fit EVT models on failure severity distributions from large unlabeled streams scored by an oracle-ish committee, validate extrapolation on held-out data; analysis-scale compute.
- **ROI estimate:** medium

### W2-C-0314 - Detection as sequential evidence gathering: information-gain evaluation for active perception

- **Problem:** Static AP presumes a fixed image, but embodied systems choose viewpoints; motivation: formalizing detection quality as information gain per action connects detection evaluation to the decision problem embodied agents actually solve.
- **Falsifiable hypothesis:** Detectors ranked by static AP reorder substantially when ranked by information gain per view in a controlled multi-view environment, because static AP ignores uncertainty quality that drives view-selection value.
- **Cheapest experiment:** Simulate next-view selection over existing multi-view datasets with several detectors, compare static vs sequential rankings; inference plus simulation.
- **ROI estimate:** medium

### W2-C-0315 - Actuarial detection: converting AP into expected deployment cost with domain priors

- **Problem:** Deployment decisions need expected-cost estimates (missed intrusion, false alarm labor), but detection metrics are cost-blind; motivation: actuarial modeling composes error rates with domain frequency and cost priors into decision-grade numbers.
- **Falsifiable hypothesis:** An actuarial layer over standard detection metrics produces deployment-cost estimates that reverse model choices made on AP alone in realistic scenarios, and the reversal boundary is computable in closed form from cost ratios.
- **Cheapest experiment:** Build cost models for 3 deployment archetypes, evaluate 8 public detectors under them using cached predictions; pure analysis.
- **ROI estimate:** medium

### W2-C-0316 - Bandit-allocated annotation: regret-minimizing labeling across classes

- **Problem:** Annotation budgets are allocated to classes by fixed quotas, ignoring the changing marginal value of labels per class as training progresses; motivation: bandit algorithms are the theory of exactly this allocation-under-uncertainty problem.
- **Falsifiable hypothesis:** A bandit allocator using per-class validation-gain estimates as rewards achieves the same final mAP as quota allocation with substantially fewer labels, with the largest savings in mid-frequency classes.
- **Cheapest experiment:** Simulate label-allocation policies on fully-labeled datasets (labels revealed on demand), compare label-efficiency curves; simulation with short retraining cycles.
- **ROI estimate:** medium

### W2-C-0317 - Program synthesis of failure slices: automatic discovery of semantic error strata

- **Problem:** Error analysis relies on manually chosen slices (size, occlusion), missing unknown semantic failure modes; motivation: program synthesis over interpretable predicates can search the slice space systematically, turning error analysis from art into search.
- **Falsifiable hypothesis:** Synthesized slice programs (compositions of interpretable predicates over metadata and features) recover known failure modes and discover previously unreported ones whose within-slice AP deficit exceeds any manually reported stratum.
- **Cheapest experiment:** Implement predicate search over enriched metadata for cached predictions of 5 detectors, human-validate top discovered slices; analysis-scale compute.
- **ROI estimate:** medium

### W2-C-0318 - Complementarity-optimal routing between human and detector

- **Problem:** Deployed systems route images between models and human reviewers with ad hoc rules; motivation: human-AI complementarity research provides the framework to optimize the joint system rather than the model in isolation, which is what deployment accuracy actually is.
- **Falsifiable hypothesis:** A learned router using model uncertainty and image features achieves joint accuracy above both the best model alone and confidence-threshold routing at matched human workload, with gains concentrated where model confidence is miscalibrated.
- **Cheapest experiment:** Simulate routing on benchmarks using annotator labels as the human channel with measured human error rates, compare routing policies; pure simulation.
- **ROI estimate:** medium

### W2-C-0319 - Weak-to-strong generalization in dense prediction: when can weak teachers train stronger students

- **Problem:** Auto-labeling assumes teacher quality upper-bounds student quality, but weak-to-strong results in language models suggest otherwise; motivation: establishing whether and when students exceed their detection teachers determines the economics of every pseudo-labeling pipeline.
- **Falsifiable hypothesis:** Students with stronger backbones trained purely on weak-teacher detection labels exceed teacher AP under identifiable conditions (teacher errors uncorrelated with image features the student can access), and fail to when teacher errors are systematic.
- **Cheapest experiment:** Train strong students on labels from deliberately weakened teachers with controlled error structure; a grid of short training runs.
- **ROI estimate:** high

### W2-C-0320 - Shard Shapley: data valuation for detection at practical granularity

- **Problem:** Data purchasing and pruning decisions need value estimates per data source, but Shapley-style valuation is intractable per image; motivation: valuing shards (sources, batches) instead of images makes principled data valuation computationally feasible for detection.
- **Falsifiable hypothesis:** Shard-level Shapley values computed via truncated sampling identify low-value or harmful data sources whose removal improves AP per training FLOP, and the values transfer across model scales within a family.
- **Cheapest experiment:** Partition training data into 20 shards, estimate Shapley values with truncated Monte Carlo over short trainings, validate by removal; many short runs at small scale.
- **ROI estimate:** medium

### W2-C-0321 - Behavioral contracts for detector updates: regression testing beyond AP

- **Problem:** Model updates that preserve AP can still silently change which instances are detected, breaking downstream systems; motivation: software engineering's contract testing formalizes behavioral compatibility, which detection deployment currently lacks entirely.
- **Falsifiable hypothesis:** AP-matched checkpoint updates flip detection outcomes on a substantial fraction of instances (behavioral churn), and a contract suite (protected-instance sets with flip budgets) can be satisfied with negligible AP cost, making low-churn updates practical.
- **Cheapest experiment:** Measure churn across public checkpoint successions, then finetune with a churn penalty on protected sets; analysis plus one training run.
- **ROI estimate:** high

### W2-C-0322 - Cohort studies on deployment logs: observational epidemiology of detector failure

- **Problem:** Deployment logs record failures under uncontrolled conditions, and naive failure statistics are confounded; motivation: epidemiology's cohort and case-control designs extract causal risk factors from exactly this kind of observational data.
- **Falsifiable hypothesis:** Case-control analysis of deployment-style logs (matched failure and success cohorts) identifies risk factors for detection failure (lighting, density, motion) with effect sizes that replicate in controlled re-tests, validating observational methodology for model monitoring.
- **Cheapest experiment:** Construct cohorts from public video-stream benchmarks with known failures, run matched analyses, verify top factors in controlled evaluation; analysis-scale.
- **ROI estimate:** medium

### W2-C-0323 - Queueing-aware detection: accuracy under frame-drop policies as a co-design problem

- **Problem:** Video analytics systems drop frames under load, and the interaction between drop policies and detection temporal characteristics determines system accuracy; motivation: queueing theory models the load process, enabling principled co-design instead of independent tuning.
- **Falsifiable hypothesis:** Under realistic arrival processes, detection-aware drop policies (drop frames the detector handles worst or redundantly) beat FIFO dropping by a margin that grows with load, computable from queueing parameters plus per-frame detection value curves.
- **Cheapest experiment:** Simulate load traces over video benchmarks with several drop policies and 3 detectors; pure simulation.
- **ROI estimate:** low

### W2-C-0324 - Uncertainty cartography: decision-quality evaluation of detection-map visualization

- **Problem:** Aerial and geospatial detection outputs feed human decisions through maps, and GIS has a mature uncertainty-visualization literature that CV ignores; motivation: the scientific question is whether communicating detection uncertainty spatially changes decision quality, which is measurable.
- **Falsifiable hypothesis:** Decision-makers using uncertainty-annotated detection maps make measurably better resource-allocation decisions (in a controlled task) than those using standard confidence-thresholded maps, with the gain concentrated in low-density ambiguous regions.
- **Cheapest experiment:** Controlled user study (30 participants) on a simulated allocation task over real aerial detection outputs with and without uncertainty encoding; small study.
- **ROI estimate:** low

### W2-C-0325 - Likelihood ratios for detection evidence: forensic reporting standards for CV

- **Problem:** Courts and audits consume detection outputs as evidence, but scores are not calibrated evidence statements; motivation: forensic statistics developed likelihood-ratio frameworks precisely to convert measurements into legally interpretable evidence strength.
- **Falsifiable hypothesis:** A likelihood-ratio wrapper over detector scores (calibrated against defined hypothesis pairs) produces evidence statements that are empirically well-calibrated across conditions where raw scores mislead by orders of magnitude, establishing feasibility of forensic-grade detection reporting.
- **Cheapest experiment:** Fit and validate LR calibration on benchmark data under shifted conditions for one deployment-style scenario; analysis only.
- **ROI estimate:** low

## Cluster 12: Simple hypotheses that challenge accepted beliefs (W2-C-0326 - W2-C-0345, 20 ideas)

### W2-C-0326 - Half the remaining COCO errors are not model errors

- **Problem:** The narrative that detection still has headroom on COCO assumes residual errors reflect model deficiency; if most are annotation artifacts, the field is optimizing against noise and needs new benchmarks more than new methods.
- **Falsifiable hypothesis:** Human adjudication shows that at least half of a SOTA detector's residual COCO errors (misses and false positives at deployment thresholds) are attributable to ground-truth problems rather than model failure.
- **Cheapest experiment:** Adjudicate 1,000 stratified residual errors of one SOTA model with 2 independent annotators and a tie-breaker; small annotation budget, no training.
- **ROI estimate:** high

### W2-C-0327 - 2015 architecture, 2026 recipe: how much progress is training practice

- **Problem:** A decade of detection progress mixes architectural innovation with recipe improvements (augmentation, schedules, pretraining), and the field has never decomposed the total gain into these two components.
- **Falsifiable hypothesis:** Faster R-CNN with a modern backbone-agnostic recipe (current augmentation, schedule, and pretrained initialization of its original backbone family) closes most of the gap to modern architectures on COCO, attributing the bulk of decade-scale progress to recipes rather than architecture.
- **Cheapest experiment:** Train the legacy architecture under a curated modern recipe and compare against matched modern models; a few training runs.
- **ROI estimate:** high

### W2-C-0328 - A 1k-image subset ranks detectors as well as the full benchmark

- **Problem:** Evaluation on full benchmarks is assumed necessary for reliable rankings, inflating iteration costs across the field; the actual subset size sufficient for stable rankings is unmeasured.
- **Falsifiable hypothesis:** A difficulty-stratified 1,000-image COCO subset reproduces full-val detector rankings with rank correlation above 0.95 across 30 public models, making most full-set evaluations during development wasteful.
- **Cheapest experiment:** Optimize and validate subset selection against cached full-val results of 30 checkpoints; pure re-analysis.
- **ROI estimate:** high

### W2-C-0329 - Learned proposals contribute nothing at modern scale

- **Problem:** Two-stage detectors learn region proposals on the premise that learned localization priors matter; with modern backbones the proposal stage may be replaceable by fixed geometric priors without loss, changing how the two-stage story is told.
- **Falsifiable hypothesis:** Replacing the learned proposal network with a fixed dense grid of geometric priors (matched count) costs under half an AP point on COCO with a modern backbone, showing the learned stage has become vestigial.
- **Cheapest experiment:** Two matched training runs (learned proposals vs fixed priors) on one two-stage detector with a modern backbone; two training runs.
- **ROI estimate:** medium

### W2-C-0330 - Augmentation is just data: gains recoverable by more images

- **Problem:** Augmentation is treated as qualitatively special, but its gains may be entirely substitutable by additional real data, which would reframe augmentation research as a data-economics question.
- **Falsifiable hypothesis:** For each standard augmentation policy there exists a data-volume increment that reproduces its AP gain exactly, and the exchange rate (augmentation value in image-equivalents) is stable across scales, making augmentation and data fungible.
- **Cheapest experiment:** Train a grid over augmentation on-off and data fractions, fit the exchange-rate curve; a bounded grid of short runs.
- **ROI estimate:** medium

### W2-C-0331 - Localization is solved; classification is the bottleneck

- **Problem:** Detection research allocates enormous effort to localization machinery, but error decompositions may show classification confusion dominates remaining error, misaligning research investment with the actual bottleneck.
- **Falsifiable hypothesis:** For modern detectors on COCO, replacing predicted boxes with GT boxes (oracle localization) improves AP far less than replacing predicted labels with GT labels (oracle classification), across architectures.
- **Cheapest experiment:** Run both oracle substitutions on cached predictions of 6 detectors; pure re-analysis.
- **ROI estimate:** high

### W2-C-0332 - Detectors barely use global context: the cropping test

- **Problem:** Architectures increasingly pursue global context aggregation on the assumption detection needs it, but the measurable contribution of context beyond a local window around each object is surprisingly undocumented.
- **Falsifiable hypothesis:** Evaluating detectors on tight local crops around GT neighborhoods (context removed beyond 2x object size) preserves the large majority of full-image AP, bounding the value of global context far below what architecture trends assume.
- **Cheapest experiment:** Crop-based evaluation protocol on COCO val for 5 detectors; inference only.
- **ROI estimate:** medium

### W2-C-0333 - Silhouettes are almost enough: shape suffices for most detection classes

- **Problem:** The texture-bias literature implies detectors need texture, but for detection (unlike classification) object shape and layout may carry most class evidence, which would change robustness strategy fundamentally.
- **Falsifiable hypothesis:** Detectors evaluated on silhouette-rendered scenes (shapes filled with flat color, layout preserved) retain the majority of AP for most COCO categories, contradicting the texture-primacy narrative for detection.
- **Cheapest experiment:** Render silhouette versions of COCO val using GT masks, evaluate 5 detectors; rendering plus inference.
- **ROI estimate:** medium

### W2-C-0334 - NMS-free wins are tuning artifacts

- **Problem:** End-to-end NMS-free detectors are claimed to beat NMS pipelines, but the NMS baselines are rarely given equivalent post-processing tuning effort, leaving the core claim uncontrolled.
- **Falsifiable hypothesis:** After matched tuning of classical NMS variants (thresholds, soft-NMS, class-wise settings), the reported advantage of NMS-free architectures on standard benchmarks disappears within seed noise.
- **Cheapest experiment:** Exhaustive post-processing tuning for matched NMS-based checkpoints against published NMS-free results; inference-scale tuning.
- **ROI estimate:** medium

### W2-C-0335 - Label assignment research stops mattering at scale

- **Problem:** A large literature optimizes label assignment (which predictions get supervised), validated at modest scale; if assignment differences wash out with strong pretraining and data scale, the subfield's relevance window has closed.
- **Falsifiable hypothesis:** With foundation-scale pretraining and modern data volume, assignment strategies that differed by multiple AP points at 2020 scale differ by less than seed noise, demonstrating scale subsumption of assignment research.
- **Cheapest experiment:** Train 3 assignment strategies at two scale points (2020-style vs modern pretrained); six training runs.
- **ROI estimate:** medium

### W2-C-0336 - Epoch-1 validation predicts final ranking

- **Problem:** Model development assumes full training is needed to compare configurations, making search expensive; if very-early validation AP already predicts final ordering, most search compute is wasted.
- **Falsifiable hypothesis:** Across a diverse configuration pool, validation AP after one epoch rank-correlates above 0.9 with final AP, enabling early stopping of experimental comparisons at a tenth of current cost.
- **Cheapest experiment:** Log early and final AP over a pool of 30 short-to-full training configurations at small scale; a pool of short runs.
- **ROI estimate:** medium

### W2-C-0337 - Random boxes teach detection: how little box supervision quality matters early

- **Problem:** Weakly-supervised detection invests in mining good boxes from classification data, but early training may only need any plausible spatial prior, with box quality mattering only late, which would invert pipeline design.
- **Falsifiable hypothesis:** Pretraining detection heads with random-but-plausible boxes on classification data, then briefly finetuning with real boxes, matches full box-supervised training curves after a small fraction of labeled-box exposure.
- **Cheapest experiment:** Compare random-box pretraining plus short finetune vs full supervision at matched budgets; a few short training runs.
- **ROI estimate:** low

### W2-C-0338 - The small-object ceiling is human, not machine

- **Problem:** Small-object detection is framed as a model limitation, but humans may disagree with GT as much as SOTA models do on small objects, meaning the reported gap to perfection is an annotation mirage below some size.
- **Falsifiable hypothesis:** Below a measurable size threshold, human annotators re-labeling benchmark images agree with original GT no better than SOTA detectors do, locating the size floor beneath which benchmark-driven progress claims are unfalsifiable.
- **Cheapest experiment:** Human re-annotation of size-stratified samples, compare human-GT vs model-GT agreement curves by size; small annotation budget.
- **ROI estimate:** high

### W2-C-0339 - Only rank matters: confidence magnitudes carry no deployable information

- **Problem:** Calibration research assumes score magnitudes matter beyond ranking, but every standard detection consumer (NMS, AP, top-k) is rank-invariant, so magnitude information may be operationally worthless in current pipelines.
- **Falsifiable hypothesis:** Replacing detector confidences with rank-preserving arbitrary magnitudes changes no standard pipeline output (AP, NMS results, threshold-swept F1 curves up to reparameterization), while breaking exactly the downstream uses (fusion, routing) that justify calibration research, cleanly separating where magnitudes matter.
- **Cheapest experiment:** Apply rank-preserving score transformations across pipelines and downstream fusion tasks, catalog invariances; pure analysis.
- **ROI estimate:** medium

### W2-C-0340 - Resolution is nothing but object pixel count

- **Problem:** Input resolution is treated as a global quality knob, but its entire effect on detection may reduce to the pixel count on each object, which would collapse resolution research into a single per-object variable.
- **Falsifiable hypothesis:** At matched object-pixel counts (achieved by cropping vs scaling), detection accuracy per instance is statistically indistinguishable across input resolutions, proving object pixels, not image resolution, is the causal variable.
- **Cheapest experiment:** Construct matched object-pixel evaluations via crop-scale manipulations of the same instances, evaluate 4 detectors; inference only.
- **ROI estimate:** medium

### W2-C-0341 - Batched inference cross-talk: your detections depend on your batchmates

- **Problem:** Deployments batch images through adaptive components (batch-statistics layers, TTA-style adaptive normalization), so one image's detections may depend on unrelated batchmates, violating the independence users assume; the effect size is unmeasured.
- **Falsifiable hypothesis:** For deployment configurations using any batch-adaptive statistics, per-image detection outputs change measurably with batch composition, and the effect is exploitable (a crafted batchmate suppresses another image's detections).
- **Cheapest experiment:** Permute batch compositions at inference across adaptive configurations of 3 detectors, measure output deltas and craft one adversarial batchmate; inference-scale compute.
- **ROI estimate:** medium

### W2-C-0342 - Scale beats diversity at fixed budget: testing the diversity dogma for detection data

- **Problem:** Data-collection wisdom says diverse sources beat volume, but at fixed labeling budget the trade has never been cleanly measured for detection, leaving collection strategy to intuition.
- **Falsifiable hypothesis:** At matched labeled-image budgets, single-domain volume matches multi-domain diversity for in-domain deployment AP and loses only under explicit domain shift, quantifying exactly when diversity is worth its coordination cost.
- **Cheapest experiment:** Compose matched training budgets at 4 diversity levels from existing multi-domain datasets, train matched detectors, test in- and out-of-domain; a grid of short runs.
- **ROI estimate:** medium

### W2-C-0343 - Coarse features already solve fine-grained detection classification

- **Problem:** Fine-grained detection is assumed to require specialized feature learning, but frozen coarse features plus a linear readout may already contain the needed distinctions, which would redirect fine-grained research toward data rather than features.
- **Falsifiable hypothesis:** Linear probes on frozen general-detector instance features match end-to-end fine-grained detection heads on subcategory classification given matched labels, showing the bottleneck is supervision, not representation.
- **Cheapest experiment:** Probe frozen instance features vs finetuned heads on a fine-grained detection dataset; probe training only.
- **ROI estimate:** low

### W2-C-0344 - Instructions beat annotators: labeling-protocol effects exceed inter-annotator noise

- **Problem:** Dataset quality discussions focus on annotator skill and count, but the instruction document may be the dominant factor, with protocol wording changing what a dataset even measures; this is testable and never tested for detection.
- **Falsifiable hypothesis:** The same images annotated under two reasonable instruction variants (differing in box-tightness and ambiguity rules) produce GT differing enough that a fixed model's AP changes by more than the inter-annotator variance within either protocol.
- **Cheapest experiment:** A-B instruction experiment on 300 images with 3 annotators per arm, evaluate fixed models against both GTs; small annotation budget.
- **ROI estimate:** high

### W2-C-0345 - Foundation-model detection advantage partly reduces to test-set exposure

- **Problem:** Foundation-model detectors beat traditional baselines on public benchmarks, but their pretraining crawls may contain benchmark test images or near-duplicates, and the exposure-attributable share of their advantage is unmeasured.
- **Falsifiable hypothesis:** On verified-clean test splits (no near-duplicates in pretraining crawls), the advantage of web-pretrained detection models over dataset-pretrained baselines shrinks measurably relative to standard test splits, attributing part of the foundation-model advantage to exposure.
- **Cheapest experiment:** Partition existing test sets by pretraining-crawl duplicate detection where crawl indices are public, compare model gaps on clean vs exposed partitions; analysis plus inference.
- **ROI estimate:** high
