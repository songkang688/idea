# P1 Wave A - Generator D Shard: Object Detection (Windows13)

- **task_id**: `p1_gen_d_object_detection`
- **role**: generator (candidate ideas only; NO verified-novelty claims)
- **windows_id**: Windows13 (locked; canonical state untouched)
- **territory**: Object detection - open-vocabulary, small/dense objects, long-tail, detection-segmentation interplay, foundation-model failure modes. Explicitly NOT architecture mix-and-match.
- **idea_count**: 100 (id_seed range `W13-P1-D-001` .. `W13-P1-D-100`)
- **evidence policy**: every record labels its claims with [KNOWN FACT] / [HYPOTHESIS] / [EXPECTED RESULT] / [MODEL SPECULATION]. No fabricated papers, numbers, datasets, or experimental results. All predictions are EXPECTED outcomes; none were run.
- **novelty status**: `why_possibly_novel` fields are UNVERIFIED model speculation; Wave B dedup + novelty verification must treat all of them as unchecked.

## Cluster overview

| cluster | count | ids |
|---|---|---|
| open-vocabulary | 16 | 001-016 |
| small-dense-objects | 14 | 017-030 |
| long-tail | 14 | 031-044 |
| detection-segmentation-interplay | 12 | 045-056 |
| fm-failure-modes | 14 | 057-070 |
| localization-vs-recognition | 8 | 071-078 |
| counting-density | 6 | 079-084 |
| evaluation-artifacts | 8 | 085-092 |
| annotation-label-noise | 8 | 093-100 |

## Candidate ideas (one-liners)

### open-vocabulary (16)

- **W13-P1-D-001** - Open-vocabulary detectors are effectively closed-vocabulary: novel-class success is concentrated on concepts frequent in web caption pretraining, and performance on genuinely caption-rare concepts collapses.
- **W13-P1-D-002** - Open-vocabulary detection AP is a property of the query vocabulary list, not the detector: adding or removing distractor class names materially changes scores and method rankings.
- **W13-P1-D-003** - Open-vocabulary detectors lack a calibrated none-of-the-above: their scores cannot express that a region matches no queried concept, causing systematic false positives when the true object is outside the vocabulary.
- **W13-P1-D-004** - The open-vocabulary bottleneck is naming, not finding: class-agnostic localization transfers to unseen categories nearly perfectly, so nearly all novel-class error is recognition error.
- **W13-P1-D-005** - Text-embedding geometry predicts open-vocabulary detection confusions: category pairs that are close in the text encoder are non-discriminable for the detector regardless of visual evidence.
- **W13-P1-D-006** - Open-vocabulary detection leaderboards reward lexical luck: replacing benchmark class names with correct but less caption-typical synonyms reshuffles method rankings.
- **W13-P1-D-007** - Open-vocabulary detectors ignore attribute words in queries: detection for a modified query like a color-plus-noun behaves almost identically to the bare noun, failing attribute-constrained retrieval.
- **W13-P1-D-008** - Part queries return whole objects: open-vocabulary detectors asked for object parts systematically box the containing whole object, revealing missing part-whole structure in region-text alignment.
- **W13-P1-D-009** - Multi-word and rare-phrase query degradation in open-vocabulary detection is largely a text-side tokenization and phrase-composition artifact, not a visual difficulty effect.
- **W13-P1-D-010** - Open-vocabulary detectors are context classifiers in disguise: pasting objects into atypical scenes collapses their naming accuracy far more than it collapses closed-vocabulary supervised detectors.
- **W13-P1-D-011** - Detect-anything claims fail at realistic vocabulary scale: open-vocabulary detection quality degrades systematically as the query vocabulary grows toward thousands of concurrent names.
- **W13-P1-D-012** - Open vocabulary means English vocabulary: multilingual queries to open-vocabulary detectors degrade in proportion to the language's share of caption pretraining, even with multilingual text encoders.
- **W13-P1-D-013** - Per-class score incomparability breaks open-vocabulary deployment: a single global confidence threshold is near-meaningless because score distributions differ arbitrarily across queried names.
- **W13-P1-D-014** - Granularity mismatch is scored arbitrarily: open-vocabulary evaluation punishes or rewards near-synonym and super/subcategory predictions inconsistently, distorting method comparisons.
- **W13-P1-D-015** - A scene-prior skyline exposes benchmark weakness: an image-level classifier plus class-agnostic proposals matches open-vocabulary detectors on a large share of benchmark classes without any region-text alignment.
- **W13-P1-D-016** - Open-vocabulary detectors cannot certify absence: their scores on object-free images do not support reliable absence decisions, which is the other half of detection that nobody evaluates.

### small-dense-objects (14)

- **W13-P1-D-017** - Small-object detection is closer to its annotation-noise ceiling than believed: inter-annotator box disagreement on tiny objects bounds achievable AP, and top models already approach that bound.
- **W13-P1-D-018** - IoU is the wrong metric below a size threshold: center-distance-based matching reorders small-object detection methods and agrees better with human quality judgments.
- **W13-P1-D-019** - Sub-pixel translation reveals stride aliasing: small-object detection output oscillates strongly under tiny image shifts because object size interacts with feature stride, a deterministic and fixable artifact.
- **W13-P1-D-020** - Image-level foundation pretraining is a poor donor for small-dense detection: at matched compute, dense-prediction-oriented pretraining beats caption or image-level contrastive pretraining specifically on the small and dense stratum.
- **W13-P1-D-021** - NMS makes detection-based counting undercount predictably in dense scenes: there is a characterizable density crossover beyond which suppression errors dominate and density-map methods win.
- **W13-P1-D-022** - Most claimed small-object method gains are pixel-budget effects: at equal effective input pixels on the object, specialized small-object techniques lose most of their advantage over plain high-resolution inference.
- **W13-P1-D-023** - Tiny-object classification is contextual inference, not appearance recognition: below a resolvable size, detectors name objects from scene context, and context-swap tests expose this hidden dependence.
- **W13-P1-D-024** - Dense-scene errors are dominated by duplicate and merge mistakes that AP barely registers: a dedicated identity-error metric reveals a failure axis invisible in current rankings.
- **W13-P1-D-025** - Fixed query budgets create a silent recall cliff: query-based detectors fail abruptly when instance count approaches the query count, and the failure is invisible on benchmarks dominated by sparse images.
- **W13-P1-D-026** - Benchmark-defined small is not domain small: small-object method rankings established on natural-photo benchmarks invert on scale distributions typical of aerial or microscopy imagery.
- **W13-P1-D-027** - Training assignment starves tiny objects: standard positive-sample assignment gives near-zero learning signal to the smallest objects, and oracle-assignment experiments would recover much of the small-object gap.
- **W13-P1-D-028** - Size priming in detection: small instances are found mainly when larger same-class instances co-occur in the image, and isolated small objects fail disproportionately, a bias hidden by co-occurrence-heavy benchmarks.
- **W13-P1-D-029** - Detectors hallucinate regularity in packed layouts: on grids of repeated identical objects, models fill in missing items at empty positions, revealing pattern-completion behavior in dense detection.
- **W13-P1-D-030** - Super-resolution preprocessing for small-object detection trades localization gains for classification bias: generative upsampling drags tiny-object labels toward visually typical categories.

### long-tail (14)

- **W13-P1-D-031** - Long-tail detection gains from reweighting losses are mostly post-hoc calibration in disguise: per-class score recalibration of a plain baseline recovers the bulk of reported rare-class improvements.
- **W13-P1-D-032** - Rare-class AP is statistically vacuous at current test sizes: bootstrap confidence intervals on tail-class AP dwarf typical method gaps, so many long-tail leaderboard conclusions are noise.
- **W13-P1-D-033** - Federated annotation makes rare-class false positives unfalsifiable: many penalized tail-class detections are actually correct findings of unannotated instances, deflating and distorting long-tail comparisons.
- **W13-P1-D-034** - Web pretraining displaces rather than solves the long tail: per-class gains from vision-language pretraining track web caption frequency, leaving web-rare classes as badly off as before.
- **W13-P1-D-035** - Few-shot detection evaluation measures support-set luck: variance across support samples exceeds method gaps, and single-support reporting has produced unstable conclusions.
- **W13-P1-D-036** - Long-tail methods overfit the benchmark's frequency histogram: retesting under resampled tail shapes reveals that gains are tied to one particular class-frequency profile.
- **W13-P1-D-037** - Tail classes are recognized by their habitats: rare-class detection succeeds mainly in stereotyped contexts, and out-of-context rare instances fail at much higher rates than out-of-context common ones.
- **W13-P1-D-038** - Most tail-class failure is naming, not missing: hierarchical evaluation that credits superclass-correct detections reveals the long-tail gap is largely a fine-grained labeling gap.
- **W13-P1-D-039** - Copy-paste augmentation teaches paste detection: rare-class gains from copy-paste partly reflect boundary and compositing cues, and artifact-free insertion tests would show smaller true gains.
- **W13-P1-D-040** - Long-tail detectors have no usable operating point: score miscalibration across the frequency spectrum means any fixed threshold either buries the tail or floods head-class false positives, a deployment failure hidden by AP.
- **W13-P1-D-041** - Repeat-factor sampling helps through contexts, not instances: oversampling images containing rare classes mostly benefits by re-exposing their scene contexts, which context-only controls can demonstrate.
- **W13-P1-D-042** - Tail-class names are unstable coordinates: rare-category text embeddings shift wildly across synonyms and phrasing, making vision-language long-tail detection fragile in exactly the classes it claims to fix.
- **W13-P1-D-043** - Average tail AP hides intra-tail regression: long-tail methods improve some rare classes while actively degrading others, and worst-group reporting would change which methods look best.
- **W13-P1-D-044** - The tail gap decomposes into proposal recall versus classification differently than assumed: for unusual-shaped rare objects the real bottleneck is objectness transfer, not naming, inverting the standard decomposition.

### detection-segmentation-interplay (12)

- **W13-P1-D-045** - Boxes already contain masks: frozen features of box-only detectors support high-quality mask prediction with tiny mask supervision, suggesting mask annotation budgets are largely wasted.
- **W13-P1-D-046** - Segmentation-first detection wins on irregular objects: deriving boxes from class-agnostic masks beats box-first pipelines for thin, curved, and perforated objects, an advantage hidden by benchmark shape statistics.
- **W13-P1-D-047** - Interior-dominated mask metrics hide boundary failure: instance segmentation progress measured by mask IoU has plateaued at boundaries, and boundary-weighted evaluation reorders methods and better predicts downstream utility.
- **W13-P1-D-048** - Detector-to-segmenter pipelines fail multiplicatively, not independently: promptable segmenters amplify detector box errors on exactly the hard instances, so pipeline quality is worse than the product of component qualities.
- **W13-P1-D-049** - Amodal-modal convention mismatch breaks detection-segmentation stacks under occlusion: components trained with different visibility conventions disagree precisely on occluded objects, and pipelines silently mix the two.
- **W13-P1-D-050** - Training detection through mask-derived objectives improves boxes themselves: replacing box regression targets with boxes derived from predicted masks yields better localization even measured by box AP on non-convex objects.
- **W13-P1-D-051** - Instance segmentation systematically forbids nested instances: overlap-resolution heuristics assume quasi-disjoint objects, making object-inside-object cases a structural blind spot across current methods.
- **W13-P1-D-052** - Detection-segmentation multitask benefit is one-directional: detection supervision helps segmentation, but segmentation supervision adds little to detection at foundation scale, contradicting the mutual-benefit narrative.
- **W13-P1-D-053** - The thing-stuff boundary is a load-bearing arbitrary choice: reclassifying ambiguous categories between thing and stuff swings panoptic comparisons, so panoptic rankings partly measure ontology luck.
- **W13-P1-D-054** - Segmenter stability is a better detection confidence than the detector's own score: rescoring detections by mask agreement under prompt jitter improves ranking quality without retraining anything.
- **W13-P1-D-055** - Dense pretraining transfers to detection through objectness, not classification: pixel-level pretraining gains concentrate in proposal recall, implying cheap class-agnostic dense objectives could replace expensive semantic ones.
- **W13-P1-D-056** - Foundation-distilled pseudo-masks carry a convexity bias that survives training: models trained on segmenter-generated masks inherit systematically inflated, smoothed object supports, capping thin-structure segmentation.

### fm-failure-modes (14)

- **W13-P1-D-057** - Attribute binding fails at the instance level in open-vocabulary detection: with two objects of swapped attributes in one scene, detectors match queries to the wrong instances at near-chance rates.
- **W13-P1-D-058** - Web-pretrained detectors hallucinate companion objects: scores for typically co-occurring categories are elevated even when absent, and this co-occurrence hallucination exceeds that of in-domain supervised detectors.
- **W13-P1-D-059** - Typographic attacks transfer from classification to open-vocabulary detection: text written in the scene shifts region scores, so rendered words act as adversarial detection evidence.
- **W13-P1-D-060** - Foundation detector errors are correlated across model families: shared web data induces shared blind spots, so ensembling different foundation detectors yields far less error diversity than their architectural diversity suggests.
- **W13-P1-D-061** - Foundation detectors have a canonical-scale prior: objects photographed at atypical absolute scales, extreme close-ups or extreme distance, are missed in ways predicted by web photo composition statistics, and rescaling recovers them.
- **W13-P1-D-062** - Foundation detectors are right for the wrong pixels: attribution analysis shows their class decisions rely on context outside the box far more than supervised detectors, predicting brittleness that in-box-only evaluation misses.
- **W13-P1-D-063** - Frozen foundation features hit a localization precision ceiling: high-IoU detection quality saturates regardless of head capacity, because image-level pretraining discards sub-patch spatial precision that fine-tuning must rebuild.
- **W13-P1-D-064** - Foundation detectors have a web-aesthetic prior: semantically harmless but statistically atypical imaging conditions, unusual white balance, nonstandard aspect ratios, flash artifacts, degrade them more than matched supervised detectors.
- **W13-P1-D-065** - Multimodal LLMs are better detection verifiers than detectors: their box generation fails on coordinate production, not perception, so the generation-verification gap argues for verifier-role deployment.
- **W13-P1-D-066** - Multimodal LLM boxes betray tokenizer priors: generated coordinates cluster on round numbers and canonical aspect ratios, a measurable output-distribution distortion that standard AP evaluation never reveals.
- **W13-P1-D-067** - Caption-worthiness bias shapes foundation detection: recall as a function of object size, centrality, and photographic salience is steeper for web-pretrained detectors, penalizing peripheral and incidental objects.
- **W13-P1-D-068** - Vocabulary forgetting outpaces domain gains: fine-tuning open-vocabulary detectors on narrow domains erases their broad-vocabulary competence at a rate that makes naive domain adaptation a net capability loss.
- **W13-P1-D-069** - State breaks detectors before category does: foundation detectors fail on known objects in unusual states, overturned, disassembled, damaged, more than on unseen categories in canonical states.
- **W13-P1-D-070** - Foundation detectors cannot say this image is not for me: on out-of-scope imagery they emit confident structured detections instead of abstaining, and no standard evaluation measures scope awareness.

### localization-vs-recognition (8)

- **W13-P1-D-071** - At foundation scale, detection error is almost all recognition: class-agnostic localization is near ceiling, so architecture work on box mechanisms attacks a solved subproblem.
- **W13-P1-D-072** - Localization and recognition want incompatible features: two-stream detectors reading separate frozen representations for where and what beat single-feature detectors at matched compute.
- **W13-P1-D-073** - IoU-threshold sweeps fingerprint what a method actually improved: most claimed detection advances are either pure-recognition or pure-localization gains, and the sweep signature exposes mislabeled contributions.
- **W13-P1-D-074** - Detectors should output box uncertainty, not just label confidence: cheap per-coordinate uncertainty adds little AP but transforms downstream decision quality, exposing a metric-deployment mismatch.
- **W13-P1-D-075** - Extent errors, not center errors, dominate the high-IoU regime, and they trace to annotation-convention ambiguity about what counts as the object, handles, shadows, occluded parts, rather than to model weakness.
- **W13-P1-D-076** - Detection classification is not crop classification: region labels depend on an optimal, class-specific amount of context, and both context-free crops and whole-image reasoning underperform the learned intermediate.
- **W13-P1-D-077** - Objectness saturates early while recognition keeps scaling: detection-specific pretraining spends compute on a subskill that stops improving, arguing for classification-heavy pretraining plus minimal localization adaptation.
- **W13-P1-D-078** - Duplicate suppression is a recognition problem misassigned to geometry: identity-aware deduplication that asks are these the same object beats overlap-threshold suppression exactly where detection is hardest, adjacent identical objects.

### counting-density (6)

- **W13-P1-D-079** - A scene-statistics decision rule for counting: measurable image properties predict whether detection-based or regression-based counting will be more accurate on a given image, enabling per-image method routing.
- **W13-P1-D-080** - Multimodal LLM counting is subitizing plus guessing: exact counting holds up to a small integer and then collapses to density-conditioned estimation, a signature invisible in benchmarks that average over count ranges.
- **W13-P1-D-081** - Crowding suppresses per-instance recall independent of resolution: detection probability of an instance declines with the number of identical neighbors even when size and image quality are held constant.
- **W13-P1-D-082** - Counts are cheap detection supervision: adding per-image count labels for classes without box annotations improves detection of those classes, unlocking abundant inventory-style metadata as training signal.
- **W13-P1-D-083** - Detector-regressor disagreement finds annotation errors: images where detection-based and density-based counts diverge are enriched for ground-truth mistakes, yielding a free annotation-audit signal.
- **W13-P1-D-084** - Partial-visibility conventions drive counting disagreement: a large share of counting error concentrates on instances whose countability is convention-ambiguous, edge-cropped, mostly occluded, or reflected objects.

### evaluation-artifacts (8)

- **W13-P1-D-085** - Class-averaged detection AP is driven by a volatile minority: bootstrap analysis shows overall benchmark rankings hinge on a handful of high-variance classes, making leaderboard stability an illusion.
- **W13-P1-D-086** - AP rewards unusable predictions: methods gain benchmark points from dense low-confidence box floods that no deployment threshold would keep, so operating-point metrics reorder detection leaderboards.
- **W13-P1-D-087** - Evaluation-implementation drift silently moves detection scores: subtle differences among popular evaluation toolkits in crowd handling, area computation, and tie-breaking are large enough to flip close method comparisons.
- **W13-P1-D-088** - Detection test sets are effectively smaller than they look: image-level and instance-level near-duplicates inflate effective sample size, understating uncertainty and overstating fine-grained method distinctions.
- **W13-P1-D-089** - The default detection-count cap censors dense scenes: standard evaluation truncates predictions per image at a fixed limit, so performance on the densest images is systematically unmeasured and methods are blind-ranked there.
- **W13-P1-D-090** - Greedy confidence-ordered matching biases AP against certain prediction styles: optimal-assignment scoring changes per-method AP unevenly, revealing that part of measured differences is matching-algorithm artifact.
- **W13-P1-D-091** - Unreported inference-time enhancements account for a large share of detection leaderboard deltas: equal-inference-budget re-evaluation collapses many claimed architecture advantages.
- **W13-P1-D-092** - Corruption-suite robustness does not predict natural-shift robustness for detection: model rankings on synthetic corruptions and on natural distribution shifts are close to uncorrelated.

### annotation-label-noise (8)

- **W13-P1-D-093** - Benchmark precision is annotation-limited for top detectors: a substantial share of their scored false positives are correct detections of unannotated objects, so measured precision differences among strong models are annotation artifacts.
- **W13-P1-D-094** - Annotation conventions drift within datasets: box tightness and part-inclusion practices vary across annotation batches, and detectors learn the average, producing systematic per-batch evaluation bias.
- **W13-P1-D-095** - Granularity-ambiguous aggregates drive outsized detection error: stacks, piles, and clusters annotated inconsistently as one-or-many account for a disproportionate share of both false positives and misses.
- **W13-P1-D-096** - High-IoU evaluation operates beyond the human agreement floor: inter-annotator box IoU distributions show that strict-threshold metrics score models against noise, and noise-floor-normalized metrics change conclusions.
- **W13-P1-D-097** - Detectors out-localize their own training labels: model predictions are systematically closer to multi-annotator consensus than the single-annotator boxes they were trained and evaluated on, so evaluation penalizes models for being right.
- **W13-P1-D-098** - Model confusion matrices partially replicate annotator confusion: class-label errors in detection datasets are structured by visual similarity and annotation workflow, and models inherit these exact confusions, inflating measured semantic error.
- **W13-P1-D-099** - Sparse-annotation training teaches contextual self-censorship: detectors trained under incomplete labeling learn context-dependent suppression of valid detections, producing deployment blind spots that complete-annotation fine-tuning reverses.
- **W13-P1-D-100** - Model-assisted annotation launders foundation-model blind spots into ground truth: datasets built with detector-in-the-loop labeling inherit the assistant's misses, making successor models' shared failures unmeasurable.
