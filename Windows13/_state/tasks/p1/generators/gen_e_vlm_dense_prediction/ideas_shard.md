# P1 Wave A - Generator E Shard: VLM Dense Prediction (Windows13)

- **task_id**: `p1_gen_e_vlm_dense_prediction`
- **role**: generator (candidate ideas only; NO verified-novelty claims)
- **windows_id**: Windows13 (locked; canonical state untouched)
- **territory**: VLM dense prediction - language-grounded segmentation, referring expressions, open-set pixel labeling, vision-language foundation model failure modes for dense tasks
- **idea_count**: 100 (id_seed range `W13-P1-E-001` .. `W13-P1-E-100`)
- **evidence policy**: every record labels its claims with [KNOWN FACT] / [HYPOTHESIS] / [EXPECTED RESULT] / [MODEL SPECULATION]. No fabricated papers, numbers, datasets, or experimental results. All predictions are EXPECTED, none were run.
- **novelty status**: `why_possibly_novel` fields are UNVERIFIED model speculation; Wave B dedup + novelty verification must treat all of them as unchecked.

## Cluster overview

| cluster | count | ids |
|---|---|---|
| language-grounded-segmentation | 12 | 001-012 |
| referring-expressions | 12 | 013-024 |
| open-set-pixel-labeling | 10 | 025-034 |
| vlm-dense-failure-modes | 12 | 035-046 |
| text-embedding-geometry | 8 | 047-054 |
| spatial-language-grounding | 8 | 055-062 |
| dense-evaluation-protocols | 8 | 063-070 |
| mask-text-alignment-training | 8 | 071-078 |
| granularity-and-parts | 6 | 079-084 |
| negation-counting-attributes | 8 | 085-092 |
| mllm-dense-interfaces | 8 | 093-100 |

## Candidate ideas (one-liners)

### language-grounded-segmentation (12)

- **W13-P1-E-001** - The last transformer layer of contrastively pretrained vision-language models is systematically the worst layer for dense language alignment, because global-pooling pressure concentrates text alignment in summary tokens at the expense of patch tokens.
- **W13-P1-E-002** - Open-vocabulary segmentation leaderboards measure mask-proposal quality, not language grounding: swapping the text encoder barely moves scores while swapping the class-agnostic mask generator moves them dramatically.
- **W13-P1-E-003** - Two-stage segment-then-classify pipelines are structurally biased against stuff categories because cropping a region for classification destroys exactly the context that defines stuff.
- **W13-P1-E-004** - Training-free attention-surgery methods for dense CLIP-style inference gain mostly by spatially denoising features, and simple spatial smoothing of unmodified features recovers much of their improvement.
- **W13-P1-E-005** - Open-vocabulary segmenters are closed-vocabulary in disguise: per-class dense accuracy is largely predictable from the class name's frequency in web caption corpora.
- **W13-P1-E-006** - Text-to-patch similarity maps in contrastive VLMs localize by visual salience rather than by language: irrelevant text queries still highlight the same salient object.
- **W13-P1-E-007** - Class-agnostic mask generators impose a granularity prior that mismatches linguistic category boundaries, capping open-vocabulary segmentation regardless of grounding quality.
- **W13-P1-E-008** - Dense language-grounding quality scales with caption richness (words and noun phrases per image) rather than raw pair count, making data curation for dense tasks orthogonal to curation for classification.
- **W13-P1-E-009** - Retrieval-based dense labeling, transferring labels from retrieved segmented neighbors in frozen VLM feature space, can rival learned open-vocabulary segmentation heads while being training-free and instantly extensible.
- **W13-P1-E-010** - Language-grounded segmenters lean on scene-context correlations so strongly that they segment object regions correctly even when the object itself is erased, revealing context-driven rather than evidence-driven masks.
- **W13-P1-E-011** - Prompt ensembling, a free win for zero-shot classification, is a mixed blessing for dense prediction: it helps region interiors but systematically blurs boundaries by averaging spatially incompatible similarity maps.
- **W13-P1-E-012** - Fine-tuning VLMs on segmentation data narrows the open vocabulary at pixel level much faster than at image level, so standard image-level forgetting checks certify models that have already lost dense open-vocabulary ability.

### referring-expressions (12)

- **W13-P1-E-013** - Referring expression segmentation benchmarks are largely solvable by detecting the head noun and picking the most salient instance, so reported scores overstate relational language understanding.
- **W13-P1-E-014** - Referring segmentation models collapse to near-chance instance selection precisely when relational clauses are necessary, and benchmarks should be stratified by distractor count to expose this.
- **W13-P1-E-015** - A location-and-size prior alone, with no access to the image or the expression's content words, captures a nontrivial share of referring segmentation performance due to annotation biases toward large, central referents.
- **W13-P1-E-016** - Referring segmentation models process negated expressions as if they were affirmative, segmenting exactly the object the expression excludes.
- **W13-P1-E-017** - Referring models fail to ground text-dependent references (objects identified by written labels in the image) even when the same system reads that text correctly in a question-answering mode, revealing an OCR-grounding integration gap.
- **W13-P1-E-018** - No-target referring, correctly refusing to segment when the expression matches nothing, is the dominant unsolved failure mode: models confidently produce masks for absent referents.
- **W13-P1-E-019** - Multi-target and exception referring expressions break single-instance architectural priors: models emit exactly one mask because their decoders structurally assume one referent.
- **W13-P1-E-020** - Referring accuracy is bimodal, near-ceiling when the head-noun category is unique in the image and near the distractor-chance floor otherwise, and single aggregate numbers hide this regime structure.
- **W13-P1-E-021** - Paraphrase inconsistency of referring models, where semantically equivalent expressions yield different masks, is large enough to serve as a free unsupervised error detector.
- **W13-P1-E-022** - Round-trip referring, where a model generates an expression for a region and then must comprehend its own expression, exposes grounding gaps invisible to standard one-way evaluation.
- **W13-P1-E-023** - Referring segmentation built on multimodal LLMs is bottlenecked by vision-encoder resolution, not language reasoning: failures concentrate on small referents regardless of expression clarity.
- **W13-P1-E-024** - Referring models fail on novel attribute-object combinations at segmentation time even when both the attribute and the object are individually well-grounded, exposing missing compositional binding in dense grounding.

### open-set-pixel-labeling (10)

- **W13-P1-E-025** - Open-vocabulary segmentation scores are vocabulary-relative: adding plausible distractor class names to the query list collapses performance, revealing closed-set discrimination masquerading as open-set labeling.
- **W13-P1-E-026** - Per-pixel abstention, the option to label a pixel as none-of-the-provided-classes, is where all open-vocabulary segmenters fail, and it is unmeasured because benchmarks force total assignment.
- **W13-P1-E-027** - Contrastive pretraining's learned temperature makes pixel-level similarity scores relative rankings rather than probabilities, so open-set pixel calibration requires anchoring scores to an absolute alignment reference.
- **W13-P1-E-028** - Vocabulary-granularity mismatch is a dominant unmeasured error source: models are marked wrong for answering at a different but correct level of the concept hierarchy, and hierarchy-aware scoring reranks methods.
- **W13-P1-E-029** - Synonym inconsistency is a cheap unforgiving audit: querying the same class by different correct names yields materially different masks, and consistency across synonyms could be enforced as a free constraint.
- **W13-P1-E-030** - Rare-class pixel labeling is governed by name statistics rather than visual difficulty: classes with common visual appearance but rare names underperform classes with rare appearance but common names.
- **W13-P1-E-031** - Unseen-category generalization claims in open-vocabulary segmentation are inflated because unseen classes are visually near seen ones; stratifying by visual distance to the seen set reveals sharply weaker true generalization.
- **W13-P1-E-032** - Anomaly segmentation via abstract text queries fails because contrastive text encoders cannot ground non-referential language: queries like unusual or out-of-place behave as near-noise directions in alignment space.
- **W13-P1-E-033** - Open-vocabulary segmentation degradation in specialist domains is driven more by the text tower than the vision tower: domain terms are poorly embedded, and text-side interventions recover more than image-side ones.
- **W13-P1-E-034** - Scaling the query vocabulary to encyclopedic size produces confusion patterns predictable from text-embedding neighborhoods alone, enabling a text-only forecast of dense failure before running any image.

### vlm-dense-failure-modes (12)

- **W13-P1-E-035** - High-norm outlier patch tokens in VLM vision towers carry global rather than local content, and filtering or reassigning them yields free dense-prediction gains across methods.
- **W13-P1-E-036** - VLM patch features lack mid-range context integration: they are simultaneously too global for instance boundaries and too local for stuff coherence, and the missing scale is measurable and fixable at inference.
- **W13-P1-E-037** - Language-queried dense prediction inherits texture bias: pixel labels follow texture over shape in cue-conflict scenes, and the bias is stronger densely than at image level within the same model.
- **W13-P1-E-038** - Resolution-scaling tricks for dense inference silently corrupt text alignment: interpolating position embeddings improves geometry while drifting patch features away from the text tower's expected distribution.
- **W13-P1-E-039** - Sliding-window dense inference produces label inconsistencies for the same object across windows, and lightweight global conditioning eliminates a class of errors that post-hoc blending merely hides.
- **W13-P1-E-040** - Anisotropy of contrastive patch embeddings makes cosine similarity a low-information ranking signal densely, and simple whitening of patch features reorders and improves pixel-label decisions.
- **W13-P1-E-041** - Multimodal LLMs contain more spatial detail than their language outputs use: pixel-probing their vision features beats their own verbalized dense answers, locating dense failure at the interface rather than in perception.
- **W13-P1-E-042** - Segmentation-capable multimodal LLMs hallucinate masks for absent objects at rates far exceeding their question-answering hallucination rates, making dense hallucination the field's most undermeasured risk.
- **W13-P1-E-043** - Language-grounded segmenters are internally inconsistent about amodal versus modal extent: whether occluded object parts are included depends on the query phrasing and the occluder's category, not on any coherent convention.
- **W13-P1-E-044** - Aspect-ratio deviation from pretraining crops damages dense predictions much more than global ones: padding, squeezing, and tiling choices at inference are a silent variance source dense benchmarks never control.
- **W13-P1-E-045** - Template context words in prompts spatially bias dense predictions: boundary pixels are more sensitive to prompt wording than interior pixels, so prompt choice partially determines boundary placement.
- **W13-P1-E-046** - The best-aligned layer for dense prediction differs systematically by query type (things versus stuff, objects versus parts), so any single-layer feature choice is guaranteed suboptimal and query-adaptive layer selection is free accuracy.

### text-embedding-geometry (8)

- **W13-P1-E-047** - The confusion matrix of an open-vocabulary segmenter is largely predictable from text-encoder geometry alone, before any image is processed, making text-side audits a cheap proxy for dense error analysis.
- **W13-P1-E-048** - Hub class names, text embeddings abnormally close to many patch features, absorb pixels from many true classes, and hubness-correction techniques from retrieval transfer directly to dense labeling as training-free gains.
- **W13-P1-E-049** - Class-name token length biases dense similarity magnitudes, so multi-word categories are systematically under- or over-predicted, and length normalization is a missing preprocessing step in every open-vocabulary pipeline.
- **W13-P1-E-050** - Polysemous class names produce sense-blended text embeddings that corrupt dense predictions, and sense-disambiguating prompt contexts recover accuracy on quietly polysemous benchmark classes.
- **W13-P1-E-051** - Contrastive text encoders barely encode spatial-relational words: removing them from referring expressions leaves the text embedding nearly unchanged, mechanistically explaining relation-blind dense grounding.
- **W13-P1-E-052** - Negation invariance of contrastive text embeddings transfers directly into dense prediction: negated queries produce near-identical similarity maps to affirmative ones, and the embedding distance between a phrase and its negation predicts which models can be fixed by prompting alone.
- **W13-P1-E-053** - Attribute-binding failure is text-side measurable: swapped-attribute expressions embed nearly identically in contrastive towers, and this bag-of-words geometry upper-bounds dense binding accuracy no matter how good the vision tower is.
- **W13-P1-E-054** - Cross-lingual dense inconsistency, where translated class names yield different masks on the same image, is large, systematic, and a free multilingual audit for text-tower quality in dense pipelines.

### spatial-language-grounding (8)

- **W13-P1-E-055** - Dense grounding models resolve frame-of-reference ambiguity by always choosing the viewer-centric reading, and benchmarks silently reward this because annotators did too, hiding a genuine ambiguity the field has never measured.
- **W13-P1-E-056** - Dense grounding handles canonical categorical relations but fails graded and metric spatial language: nearest, halfway, and almost-touching ground at near-chance despite high scores on left-right-above benchmarks.
- **W13-P1-E-057** - Relational grounding accuracy decays superlinearly with scene clutter because models approximate relations with global position priors that collapse when many candidates occupy every image region.
- **W13-P1-E-058** - Depth-dependent relations fail because VLM features encode little metric depth, and supplying monocular depth as an auxiliary input disproportionately repairs behind and in-front-of while leaving 2D relations unchanged, cleanly attributing the failure.
- **W13-P1-E-059** - Relative-size references ground by image-plane area rather than real-world size: models pick the object with more pixels, failing whenever perspective makes the physically larger object smaller in the frame.
- **W13-P1-E-060** - Dense grounding models trained on web photos fail systematically on egocentric viewpoints, and the failure is viewpoint-distributional rather than object-level: the same objects ground fine in third-person views.
- **W13-P1-E-061** - Grounding accuracy decays multiplicatively per relational hop in nested expressions, and measuring the per-hop decay factor gives a single scalar that predicts model behavior on arbitrarily complex referring chains.
- **W13-P1-E-062** - Spatial terms function as tie-breakers, not constraints: models first shortlist referents by appearance and only consult spatial language when appearance ties, an order of operations exposable by appearance-spatial conflict stimuli.

### dense-evaluation-protocols (8)

- **W13-P1-E-063** - Cross-dataset open-vocabulary evaluation partially measures label-name compatibility: renaming target-dataset classes to equally correct synonyms reranks methods, revealing name-matching as a hidden score component.
- **W13-P1-E-064** - Decomposing open-vocabulary segmentation error into recognition and localization components reranks methods: some celebrated systems win on localization while losing on recognition, and mIoU hides which skill improved.
- **W13-P1-E-065** - Referring benchmarks contain enough annotation ambiguity that top models may already be at the inter-annotator ceiling, making current leaderboard differences unmeasurable noise.
- **W13-P1-E-066** - Zero-shot dense evaluation quietly permits test-distribution prompt tuning: template and vocabulary choices are optimized against the very benchmarks reported, and a strict no-peek protocol measurably deflates published-style numbers.
- **W13-P1-E-067** - Boundary-weighted evaluation reranks open-vocabulary segmenters because interior-pixel dominance in standard metrics rewards blob-correct methods over boundary-correct ones, and users overwhelmingly need boundaries.
- **W13-P1-E-068** - Background-region conventions are inconsistent across dense benchmarks and methods, and harmonizing background handling alone shifts reported open-vocabulary gaps enough to change some published conclusions.
- **W13-P1-E-069** - A query-in-the-wild protocol, evaluating dense models on free-form user queries collected without benchmark vocabulary constraints, would reveal a large gap between benchmark scores and experienced quality.
- **W13-P1-E-070** - Dense benchmark images overlap VLM pretraining corpora, and contamination-stratified scoring shows open-vocabulary methods earning part of their zero-shot reputation on effectively seen images.

### mask-text-alignment-training (8)

- **W13-P1-E-071** - Region-text alignment fine-tuning on detection-vocabulary data narrows the effective open vocabulary while improving benchmarks, and vocabulary-coverage audits before and after would expose the hidden tradeoff.
- **W13-P1-E-072** - Self-training with VLM-generated pseudo-masks amplifies text-side biases round over round: classes favored by text geometry gain pixels each iteration, and the drift is measurable, predictable, and correctable with text-side debiasing.
- **W13-P1-E-073** - Caption-supervised grounding learns co-occurrence, not localization: models ground nouns onto co-occurring context regions, and counterfactual scenes where usual context appears without the object expose the difference cleanly.
- **W13-P1-E-074** - The missing dense alignment in contrastive VLMs is a shallow, learnable transform: a small frozen-backbone decoder trained on limited data recovers most of the gap to full fine-tuning, showing the information was present but misformatted.
- **W13-P1-E-075** - Patch-level contrastive alignment objectives are ill-posed at boundaries because patches straddle classes, and boundary-aware assignment during training removes a systematic soft-boundary artifact that plagues all patch-supervised dense models.
- **W13-P1-E-076** - Fine-tuning the text tower for dense tasks is more damaging to open-vocabulary ability than fine-tuning the vision tower: alignment forgetting is asymmetric across towers, and freezing choice should follow the asymmetry.
- **W13-P1-E-077** - Training dense models on synthetic captions transfers the captioner's blind spots as a hard ceiling: student dense performance per concept is bounded by the teacher captioner's mention behavior, creating invisible inherited gaps.
- **W13-P1-E-078** - Mixing instance-mask and semantic-mask supervision teaches conflicting notions of object extent, and the conflict measurably hurts referring tasks that need instances, suggesting supervision-type should be conditioned, not pooled.

### granularity-and-parts (6)

- **W13-P1-E-079** - Part queries retrieve wholes: language-grounded segmenters asked for object parts return whole-object masks because caption supervision represents parts as attributes of wholes rather than as spatial units.
- **W13-P1-E-080** - Natural-language granularity cues (the whole X, just the Y of the X) fail to control mask extent reliably, while an explicit granularity token interface succeeds, showing granularity is representable but not language-accessible.
- **W13-P1-E-081** - Predicted part and whole masks violate containment at high rates, and enforcing part-whole consistency at inference is a free accuracy and trustworthiness gain no current system exploits.
- **W13-P1-E-082** - Open-vocabulary segmenters exhibit basic-level bias: superordinate queries like animal produce worse masks than basic-level names for the same regions, because caption language overwhelmingly uses basic-level terms.
- **W13-P1-E-083** - Stuff-stuff boundary placement is learned as dataset convention, not visual inference: models transfer their training dataset's boundary style to new domains, and cross-dataset boundary disagreement quantifies this hidden convention learning.
- **W13-P1-E-084** - Linguistic countability drives segmentation topology: mass-noun phrasing yields merged regions and count-noun phrasing yields instance-like masks for the same visual material, an unmeasured coupling between grammar and mask structure.

### negation-counting-attributes (8)

- **W13-P1-E-085** - Ordinal reference (the second cup from the left) grounds at near-chance across dense models because ordinal computation requires an explicit sort the architectures never perform, and errors follow a predictable off-by-adjacency pattern.
- **W13-P1-E-086** - Instance counts derived from language-grounded segmentation systematically undercount in crowded scenes with a density-dependent bias, and the bias curve is stable enough to invert for calibrated counting.
- **W13-P1-E-087** - Complement queries (everything except the sky) fail despite being trivially computable from the affirmative mask, exposing that dense systems lack a negation-as-set-operation pathway even where no perception is required.
- **W13-P1-E-088** - Attribute-only queries (everything red) are object-mediated: models find red objects but miss red stuff and red object-parts, revealing that attributes are grounded through object nouns rather than as pixel properties.
- **W13-P1-E-089** - Comparative attribute grounding (the darker of the two) is near chance because per-pixel scoring has no cross-instance normalization step, and adding an explicit candidate-comparison stage fixes it without touching the backbone.
- **W13-P1-E-090** - Dense systems treat conjunctive and disjunctive queries identically: cats and dogs versus cats or dogs produce indistinguishable masks, revealing that logical connectives are dropped at the grounding interface.
- **W13-P1-E-091** - Metric-quantitative spatial queries (objects larger than half the image, within ten pixels of the border) are wholly ungrounded in dense systems, and their failure profile shows quantities are parsed as vague intensifiers.
- **W13-P1-E-092** - State-conditioned queries (the open door, the empty cup) lag object queries by a wide margin at dense level, and the gap measures a state-grounding deficit distinct from object recognition that paired-state scenes isolate cleanly.

### mllm-dense-interfaces (8)

- **W13-P1-E-093** - Segmentation tokens in multimodal LLMs are a low-bandwidth bottleneck: mask fidelity saturates with the information capacity of the token embedding, measurable by comparing token-decoded masks against directly decoded masks from the same visual features.
- **W13-P1-E-094** - Autoregressive coordinate emission for dense outputs accumulates spatial error along the sequence: later polygon vertices and later boxes in a list are systematically less accurate, an interface artifact invisible to aggregate metrics.
- **W13-P1-E-095** - Chain-of-thought reasoning before mask emission can hurt grounding: reasoning tokens displace visual attention, and mask accuracy on perceptually easy targets drops when models are made to think longer.
- **W13-P1-E-096** - Multimodal LLMs are dense-inconsistent across query formats: pointing at a pixel and asking what it is contradicts asking where a named thing is, and cross-format agreement is a label-free quality audit plus a constraint for free improvement.
- **W13-P1-E-097** - Segmentation-capable multimodal LLMs cannot express spatial uncertainty: their verbalized doubts about mask regions are uncorrelated with actual boundary errors, leaving dense outputs without any usable confidence channel.
- **W13-P1-E-098** - Multi-turn mask correction fails because dialog context does not effectively carry mask state: models treat each correction as a fresh query, and correction success barely exceeds single-turn retry rates.
- **W13-P1-E-099** - Visual prompt overlays (marks, boxes, highlights drawn on the image) contaminate the visual stream: they alter dense predictions for unmarked objects, an interference effect that mark-based prompting studies never control.
- **W13-P1-E-100** - High-resolution tiling strategies for multimodal LLMs improve text-reading tasks far more than segmentation because cross-tile attention fails to reintegrate object geometry, producing task-dependent resolution scaling that current unified benchmarks average away.
