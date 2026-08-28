# Stage 1 — Cluster C: Massive Original Research Idea Catalog

**Agent:** Cloud Sub-Agent C (research scientist), reporting to Supervisor Windows7
**Repo:** github.com/songkang688/idea
**Stage:** 1 — massive original idea generation (no filtering, no archival packaging)
**Total ideas:** 372 (C-0001 – C-0372)

**Scope of Cluster C:** Multimodal / vision-language large models; VLMs for dense prediction; large-model fine-tuning instability; representation learning; super-resolution/restoration/generation/diffusion only where they create a real scientific question for vision understanding or segmentation; LLM agents for annotation; surprising empirical phenomena; unproven community assumptions; negative-result hypotheses; evaluation protocol failures; robustness; generalization; simple hypotheses that challenge accepted beliefs.

**Quality contract applied to every idea:** each entry must (a) challenge an accepted belief, or (b) explain a surprising failure, or (c) propose a cheaper explanation than the current SOTA story — with a precise mechanism and a falsifiable claim. Trivial combinations ("CLIP + SAM", "add LLM to detector", "diffusion for augmentation" without mechanism) were excluded by construction. No papers or measured results are invented anywhere in this catalog; named models/datasets/phenomena are referenced only as objects of proposed study, and all numbers appearing inside hypotheses are predictions to be tested, not reported measurements.

## Sub-cluster map

| Sub-cluster tag | ID range | Theme | Count |
|---|---|---|---|
| VLM-DENSE | C-0001 – C-0030 | Vision-language models for dense prediction / segmentation | 30 |
| VLM-ARCH | C-0031 – C-0060 | Multimodal architecture, tokens, fusion phenomena | 30 |
| FT-INSTAB | C-0061 – C-0090 | Large-model fine-tuning instability | 30 |
| REP-LEARN | C-0091 – C-0120 | Representation learning | 30 |
| GEN4SEG | C-0121 – C-0150 | Generative models / SR / restoration as scientific questions for understanding & segmentation | 30 |
| LLM-ANNOT | C-0151 – C-0180 | LLM/VLM agents for annotation | 30 |
| EMP-PHEN | C-0181 – C-0210 | Surprising empirical phenomena | 30 |
| ASSUMP | C-0211 – C-0240 | Unproven community assumptions | 30 |
| NEG-HYP | C-0241 – C-0270 | Negative-result hypotheses | 30 |
| EVAL-FAIL | C-0271 – C-0300 | Evaluation protocol failures | 30 |
| ROBUST | C-0301 – C-0330 | Robustness and distribution shift | 30 |
| GENERAL | C-0331 – C-0360 | Generalization & simple belief-challenging hypotheses | 30 |
| WILDCARD | C-0361 – C-0372 | Meta-science, tooling, cross-cutting bets | 12 |

**Record format per idea:** Idea ID · One-sentence idea · Problem · Core Hypothesis · Why Important · Why Possibly Novel · Minimal Experiment · Main Risk · Research Cluster tag.

**Companion file:** `stage1_cluster_C_index.csv` (machine-readable index: id, one_sentence_idea, cluster).

---
## Sub-cluster VLM-DENSE — Vision-Language Models for Dense Prediction (C-0001 – C-0030)

### C-0001 · High-norm artifact tokens, not global pooling, break CLIP dense features
- **One-sentence idea:** Test whether CLIP's poor patch-level segmentation is caused primarily by a small set of high-norm "register-like" artifact tokens rather than by the global contrastive objective itself.
- **Problem:** The community explains CLIP's weak dense features by "image-level contrastive training destroys spatial information," but this story has never been isolated from the artifact-token phenomenon observed in large ViTs.
- **Core Hypothesis:** Masking or reassigning the top-k highest-norm patch tokens at inference recovers a large fraction of the mIoU gap between CLIP and dense-pretrained backbones, without any retraining.
- **Why Important:** If true, cheap inference-time surgery replaces expensive dense-alignment pretraining for many open-vocabulary segmentation pipelines.
- **Why Possibly Novel:** Artifact tokens and dense-prediction failure are studied by disjoint communities; nobody has quantified how much of the "contrastive objective destroys locality" narrative is actually token-norm pathology.
- **Minimal Experiment:** Linear-probe segmentation on ADE20K with frozen CLIP ViT-L, comparing vanilla patch tokens vs. tokens with the top-1% norm outliers replaced by neighborhood averages; report mIoU delta against a DINOv2 upper bound.
- **Main Risk:** Artifact removal may help only specific ViT sizes/training recipes, making the claim non-general.
- **Cluster:** VLM-DENSE

### C-0002 · Text embeddings are just an arbitrary linear classifier for open-vocab segmentation
- **One-sentence idea:** Claim that in fine-tuned open-vocabulary segmentation, replacing CLIP text embeddings with a frozen random orthogonal matrix of class vectors loses almost nothing, showing "language priors" contribute far less than advertised.
- **Problem:** Open-vocabulary segmentation papers attribute gains to semantic structure in the text embedding space, but never ablate against structure-free class vectors under identical fine-tuning.
- **Core Hypothesis:** After any visual-side fine-tuning, the text tower acts as a fixed linear classifier whose semantic geometry matters only for truly zero-shot classes, not for the seen-class mIoU that dominates reported numbers.
- **Why Important:** It would reveal that many "language-driven" segmentation results are ordinary supervised learning wearing a language costume, redirecting research effort toward genuine zero-shot transfer.
- **Why Possibly Novel:** The random-orthogonal-classifier control is standard in classification literature but essentially absent from open-vocabulary dense prediction papers.
- **Minimal Experiment:** Fine-tune the same mask decoder on COCO-Stuff with (a) CLIP text embeddings, (b) random orthogonal vectors, (c) shuffled text embeddings; compare seen-class and held-out-class mIoU.
- **Main Risk:** Result may be dominated by the seen/unseen split choice, requiring several splits to be convincing.
- **Cluster:** VLM-DENSE

### C-0003 · Open-vocabulary gains are caption-vocabulary overlap, not compositional generalization
- **One-sentence idea:** Quantify how much of open-vocabulary segmentation's "novel class" performance is predicted purely by the frequency of the class name (and its synonyms) in the pretraining caption corpus.
- **Problem:** "Zero-shot" dense benchmarks treat all unseen classes equally, ignoring that most target class names appear millions of times in web captions.
- **Core Hypothesis:** A single scalar — log caption frequency of the class term — explains the majority of variance in per-class zero-shot IoU, leaving little residual for architectural innovations to explain.
- **Why Important:** It would show current benchmarks reward vocabulary memorization, and would define a corrected benchmark stratified by caption frequency.
- **Why Possibly Novel:** Term-frequency analyses exist for image classification, but no one has built the per-class frequency-vs-IoU regression for dense prediction or used it to re-rank published methods.
- **Minimal Experiment:** For one open-vocab segmenter on ADE20K-847, regress per-class IoU on LAION caption term frequency; report R² and the method ranking after frequency stratification.
- **Main Risk:** Frequency correlates with visual class difficulty, requiring careful controls (object size, pixel share) to isolate the vocabulary effect.
- **Cluster:** VLM-DENSE

### C-0004 · LLM decoding actively destroys spatial information in pixel-grounded VLMs
- **One-sentence idea:** Show that in "segmenting" multimodal LLMs, localization quality of hidden states monotonically degrades through LLM layers, so the best mask queries come from the earliest fusion layers, contradicting the "deep reasoning improves grounding" narrative.
- **Problem:** Pixel-grounding VLMs (LISA-style) assume the LLM adds grounding ability, but nobody measures where spatial information lives across the LLM stack.
- **Core Hypothesis:** A linear read-out for mask prediction attached at LLM layer k shows peak performance at small k, with deeper layers strictly worse for localization even as answer quality improves.
- **Why Important:** It suggests decoupling the mask pathway from LLM depth, saving compute and improving masks simultaneously.
- **Why Possibly Novel:** Layer-wise probing is common for semantics but has not been done for dense mask decoding inside instruction-tuned multimodal LLMs.
- **Minimal Experiment:** Freeze a pixel-grounding VLM, train identical lightweight mask heads on hidden states from every 4th LLM layer, plot RefCOCO cIoU vs. layer index.
- **Main Risk:** Positional information may be re-encoded non-linearly in deep layers, which a linear probe would miss.
- **Cluster:** VLM-DENSE

### C-0005 · One high-resolution forward pass explains most "language-guided" dense gains
- **One-sentence idea:** Test whether the gains attributed to language guidance in VLM-based dense predictors are mostly reproduced by simply running the vision encoder at the higher resolution these pipelines quietly adopt.
- **Problem:** VLM-based segmentation systems change resolution, crops, and ensembling alongside adding language, making attribution impossible from published tables.
- **Core Hypothesis:** A resolution- and TTA-matched vision-only baseline closes more than half of the reported gap to language-guided systems on standard dense benchmarks.
- **Why Important:** Correct attribution prevents the field from investing in language machinery when the operative variable is pixels-per-token.
- **Why Possibly Novel:** Resolution-matched controls are rarely reported because they are unglamorous; a systematic audit across several published pipelines would be new.
- **Minimal Experiment:** Reproduce two open-vocab segmentation pipelines, strip the text branch and substitute a learned class-query bank, match resolution/TTA exactly, and compare mIoU.
- **Main Risk:** Reproduction fidelity of published pipelines; conclusions could be contested as implementation gaps.
- **Cluster:** VLM-DENSE

### C-0006 · The best segmentation layer of a VLM is class-dependent, not "the last layer"
- **One-sentence idea:** Establish that different semantic categories peak at different encoder depths in VLMs, so single-layer feature extraction is fundamentally suboptimal and per-class layer routing is a free lunch.
- **Problem:** Frozen-backbone dense evaluation conventionally uses the last (or a single fixed) layer, an unexamined convention inherited from classification.
- **Core Hypothesis:** Stuff classes (sky, grass) peak several layers earlier than thing classes (person, car), and a per-class optimal-layer oracle beats the best single layer by a nontrivial mIoU margin.
- **Why Important:** It reframes "which backbone is best for dense tasks" into "which depth profile," changing how frozen features should be benchmarked and consumed.
- **Why Possibly Novel:** Layer-wise probing exists in aggregate, but per-class depth profiles and a routing head exploiting them have not been characterized for VLM encoders.
- **Minimal Experiment:** Train linear probes on every layer of frozen CLIP/SigLIP on ADE20K, compute per-class IoU-vs-depth curves, and evaluate a per-class argmax-layer oracle.
- **Main Risk:** The oracle gain may shrink to noise once a practical (non-oracle) router must be learned.
- **Cluster:** VLM-DENSE

### C-0007 · Prompt engineering for segmentation is logit calibration in disguise
- **One-sentence idea:** Show that elaborate prompt templates ("a photo of a {} in a scene") improve open-vocabulary segmentation only by shifting per-class logit priors, and a 1-parameter-per-class bias fitted on a handful of images matches them.
- **Problem:** Prompt engineering is treated as injecting semantic knowledge, yet its measurable effect on dense predictions has never been decomposed into calibration vs. representation change.
- **Core Hypothesis:** Post-hoc per-class temperature and bias fitted on 10 labeled images reproduces ≥90% of the mIoU gain of hand-tuned prompt ensembles.
- **Why Important:** It replaces prompt folklore with a principled, cheaper calibration step and clarifies what prompts can and cannot do for dense tasks.
- **Why Possibly Novel:** Calibration explanations exist for zero-shot classification but the decomposition has not been done where spatial competition between classes (softmax over pixels) changes the dynamics.
- **Minimal Experiment:** On Pascal-Context, compare vanilla prompts, 80-prompt ensembles, and single prompt + fitted per-class bias/temperature; report mIoU and per-class logit distribution shifts.
- **Main Risk:** Some prompt effects may genuinely alter the embedding direction (not just magnitude), which would cap the calibration-only reproduction.
- **Cluster:** VLM-DENSE

### C-0008 · Referring segmentation models mostly ignore the referring expression
- **One-sentence idea:** Demonstrate that current referring-segmentation models retain most of their accuracy when the linguistic content of the expression is scrambled, because saliency and object-size priors do the work.
- **Problem:** RefCOCO-style benchmarks are saturated, but it is unknown how much performance survives destruction of the language signal.
- **Core Hypothesis:** Word-shuffled or template-replaced expressions ("the object") preserve a large fraction of cIoU on RefCOCO, and the gap widens dramatically only on expressions requiring spatial relations between same-category instances.
- **Why Important:** It would show the benchmark rewards salient-object segmentation, motivating adversarially re-split evaluation for genuine language grounding.
- **Why Possibly Novel:** Text-ablation studies exist for VQA but systematic language-destruction baselines with modern referring-segmentation models and a difficulty taxonomy are missing.
- **Minimal Experiment:** Evaluate two public referring-segmentation models on RefCOCO/+/g with intact, shuffled, and template expressions; stratify results by number of same-class distractors.
- **Main Risk:** Older models may fail the ablation while the newest ones pass, turning the result into a moving target.
- **Cluster:** VLM-DENSE

### C-0009 · Patchification aliasing, not attention, bounds VLM boundary quality
- **One-sentence idea:** Attribute the chronically blurry boundaries of VLM-based segmenters to spectral aliasing introduced by strided patch embedding, and show an anti-aliased (blur-pooled, overlapping) patch stem fixes boundaries without touching attention.
- **Problem:** Boundary errors are usually blamed on low token resolution or attention smoothing, and fixed with heavy decoders; the signal-processing root cause is unexamined.
- **Core Hypothesis:** Replacing the 16×16 strided conv stem with an anti-aliased overlapping stem (at equal token count) significantly improves boundary F-score while leaving interior mIoU unchanged.
- **Why Important:** A stem-level fix is orders of magnitude cheaper than cascaded refinement decoders, and reframes dense-VLM design around sampling theory.
- **Why Possibly Novel:** Anti-aliasing is studied for CNN shift-invariance, but its interaction with patch tokenization and open-vocabulary boundary metrics is unexplored.
- **Minimal Experiment:** Retrain a small ViT-B CLIP on a public captions subset with standard vs. anti-aliased stems, then compare boundary F-score on Cityscapes linear probing.
- **Main Risk:** Requires (modest) pretraining compute, and the effect could be washed out by decoder choice.
- **Cluster:** VLM-DENSE

### C-0010 · Grounding ability emerges then degrades with more caption data
- **One-sentence idea:** Hypothesize a non-monotonic relationship where patch-text alignment (dense grounding) peaks at intermediate pretraining scale and then degrades as noisy web captions push the model toward bag-of-words global matching.
- **Problem:** Scaling studies report only image-level metrics, implicitly assuming dense grounding improves monotonically with data scale.
- **Core Hypothesis:** Zero-shot pointing/segmentation accuracy of intermediate checkpoints rises then falls across a pretraining data sweep, while retrieval keeps improving — a divergence invisible to standard evals.
- **Why Important:** If dense grounding anti-scales beyond a point, checkpoint selection and data curation for dense tasks must diverge from retrieval-optimal recipes.
- **Why Possibly Novel:** No public study tracks dense-alignment metrics across pretraining data scale; the retrieval/grounding divergence would be a new scaling phenomenon.
- **Minimal Experiment:** Train small CLIP variants on 10M/50M/200M caption subsets, evaluate zero-shot segmentation via patch-text similarity on Pascal VOC at each scale, plot both curves against retrieval R@1.
- **Main Risk:** The effect may only appear at scales beyond available academic compute.
- **Cluster:** VLM-DENSE

### C-0011 · The frozen LLM in segmentation decoders is replaceable by a random-init transformer
- **One-sentence idea:** Test whether the pretrained weights of the LLM inside reasoning-segmentation systems matter at all, versus an identically-sized randomly initialized transformer trained with the same recipe.
- **Problem:** "LLM knowledge transfers to segmentation" is asserted from end-to-end scores; capacity and architecture are perfect confounds.
- **Core Hypothesis:** For standard referring segmentation (not multi-step reasoning), a random-init transformer of equal size matches the pretrained LLM within noise, because the task consumes only shallow condition-encoding capacity.
- **Why Important:** It would demote a whole line of "LLM-empowered segmentation" claims to capacity effects and identify which (if any) task slices genuinely need pretrained language knowledge.
- **Why Possibly Novel:** Random-init controls exist for classification heads but have never been run at LLM scale inside dense-prediction pipelines.
- **Minimal Experiment:** Train a LISA-style pipeline on RefCOCO with (a) pretrained 1.3B LLM, (b) random-init same architecture, (c) pretrained-but-shuffled-weights; compare cIoU on standard vs. reasoning-heavy splits.
- **Main Risk:** Training a random-init LLM-sized decoder stably may need recipe changes that muddy the comparison.
- **Cluster:** VLM-DENSE

### C-0012 · 2D-aware positional interpolation is the whole story of high-res transfer
- **One-sentence idea:** Claim that most of the accuracy loss when running VLM encoders above training resolution stems from naive positional-embedding interpolation, and that a principled 2D spectral resampling closes the gap without any high-res fine-tuning.
- **Problem:** The field treats high-resolution fine-tuning as mandatory for dense tasks, an expensive step whose necessity is asserted rather than isolated.
- **Core Hypothesis:** Bicubic PE interpolation induces systematic radial distortion in attention patterns, and Fourier-domain PE resampling recovers most of the fine-tuned model's dense accuracy at 2–4× training resolution.
- **Why Important:** Eliminating high-res fine-tuning would cut the dominant adaptation cost for dense deployment of every frozen VLM.
- **Why Possibly Novel:** PE interpolation tricks exist, but a causal decomposition attributing the high-res gap specifically to PE distortion (vs. attention entropy, patch statistics) is missing.
- **Minimal Experiment:** Evaluate frozen SigLIP at 2× resolution on ADE20K with bicubic vs. Fourier PE resampling vs. high-res fine-tuned reference; attribute the gap fractionally.
- **Main Risk:** Attention-entropy collapse at long sequence length may be a co-equal cause, leaving PE fixes insufficient alone.
- **Cluster:** VLM-DENSE

### C-0013 · Novel-class recall in open-vocab detection is pretraining leakage
- **One-sentence idea:** Measure how much "novel class" performance of open-vocabulary detectors/segmenters survives when images visually similar to benchmark novel-class instances are deduplicated out of the vision-language pretraining set.
- **Problem:** Benchmarks define novelty by annotation absence in the detection dataset, ignoring that the pretraining corpus contains abundant labeled-by-caption examples of the same classes.
- **Core Hypothesis:** Near-duplicate and same-instance leakage from web pretraining accounts for a substantial fraction of novel-class AP, and dedup-retrained models show a much smaller zero-shot gap over supervised baselines.
- **Why Important:** It would recalibrate how much genuine category generalization current open-vocab systems have, affecting deployment expectations in truly novel domains.
- **Why Possibly Novel:** Dedup studies exist for classification (e.g., test-set contamination) but not for region-level open-vocabulary benchmarks.
- **Minimal Experiment:** Train a small open-vocab detector on a caption corpus before/after removing images with high embedding similarity to LVIS rare-class instances; compare rare-class AP.
- **Main Risk:** Compute cost of retraining and difficulty defining leakage thresholds defensibly.
- **Cluster:** VLM-DENSE

### C-0014 · Self-attention "surgery" methods for CLIP segmentation equal Gaussian smoothing
- **One-sentence idea:** Show that the family of training-free attention modifications (value-value attention, self-self attention, correlation reweighting) used to make CLIP segment is functionally equivalent to simple spatial smoothing of the patch-text similarity map.
- **Problem:** A growing zoo of attention-surgery papers claims mechanistic insight, but no common baseline of plain post-hoc smoothing at matched hyperparameter budget exists.
- **Core Hypothesis:** A tuned Gaussian (or bilateral) filter over vanilla CLIP similarity maps matches the mIoU of published attention-surgery methods on standard training-free segmentation benchmarks.
- **Why Important:** If a filter suffices, the mechanistic narratives are over-claims, and the field should report smoothing-matched baselines by default.
- **Why Possibly Novel:** Nobody has published the embarrassing-baseline comparison at matched tuning budget across the attention-surgery family.
- **Minimal Experiment:** Reimplement three training-free CLIP-segmentation methods, tune a bilateral filter baseline with the same validation budget, and compare on VOC/Context/ADE.
- **Main Risk:** Some surgery methods may genuinely exceed smoothing on fine structures, requiring boundary-metric nuance in the claim.
- **Cluster:** VLM-DENSE

### C-0015 · Dense contrastive objectives rediscover what crop augmentation already provides
- **One-sentence idea:** Argue that region-level contrastive pretraining objectives for VLMs add little beyond global objectives trained with aggressive multi-crop augmentation, because both induce the same patch-level invariance structure.
- **Problem:** Dense pretraining losses are credited for dense-task gains without controlling for the augmentation distribution differences between recipes.
- **Core Hypothesis:** Global contrastive training with matched multi-crop/local-crop augmentation reaches within a small margin of dense-objective models on segmentation linear probes, implying the objective is a secondary factor.
- **Why Important:** It would simplify pretraining recipes and clarify that data-view design, not loss design, is the operative lever for dense transfer.
- **Why Possibly Novel:** Loss-vs-augmentation attribution has been studied in self-supervised learning but not for language-supervised dense pretraining.
- **Minimal Experiment:** Pretrain matched ViT-B models on the same captions with (global loss, standard crops), (global loss, multi-crop), (dense loss, standard crops); linear-probe all on ADE20K.
- **Main Risk:** Interaction effects (dense loss + multi-crop) may dominate, complicating the clean additive story.
- **Cluster:** VLM-DENSE

### C-0016 · "Emergent grounding" in multimodal LLMs is an instruction-format artifact
- **One-sentence idea:** Test whether the celebrated ability of multimodal LLMs to output boxes/points reflects genuine internal grounding or merely the formatting distribution of instruction-tuning data, by probing grounding before and after instruction tuning with format-neutral probes.
- **Problem:** Grounding is measured through the model's output format (coordinate tokens), conflating knowing-where with saying-where.
- **Core Hypothesis:** Linear probes on pre-instruction-tuning checkpoints already extract localization equal to post-tuning models, showing instruction tuning teaches the output syntax, not the spatial knowledge.
- **Why Important:** It changes what "adding grounding data" buys — interface, not capability — and suggests far cheaper interface-only tuning.
- **Why Possibly Novel:** The capability-vs-interface decomposition for spatial outputs of multimodal LLMs has not been explicitly measured.
- **Minimal Experiment:** Take a base VLM and its grounding-tuned variant; train identical point-prediction probes on frozen features of both; compare probe accuracy against the tuned model's native coordinate outputs.
- **Main Risk:** Probes may under-extract nonlinear spatial knowledge, biasing toward the "interface" conclusion.
- **Cluster:** VLM-DENSE

### C-0017 · Box-supervised grounding data actively hurts pixel-level ability
- **One-sentence idea:** Quantify a granularity-interference effect where training VLMs with box-level grounding annotations degrades their latent pixel-level (mask) separability relative to models trained with none.
- **Problem:** Grounding data is assumed to be monotonically helpful across granularities; possible negative transfer from coarse boxes to fine masks is never measured.
- **Core Hypothesis:** Box supervision teaches rectangle-shaped attention prototypes that measurably reduce boundary fidelity of downstream mask heads compared to caption-only pretraining plus mask fine-tuning.
- **Why Important:** Data-mixture design for grounding VLMs currently maximizes box data volume; a demonstrated interference would reshape mixture policy.
- **Why Possibly Novel:** Cross-granularity negative transfer within grounding supervision is an unexamined hypothesis.
- **Minimal Experiment:** Fine-tune identical mask decoders on frozen features from caption-only vs. caption+box-tuned VLMs; compare boundary F-score and rectangle-bias of attention maps.
- **Main Risk:** Effect size may be small relative to backbone variance across seeds.
- **Cluster:** VLM-DENSE

### C-0018 · SAM-proposal pipelines structurally undercount stuff classes
- **One-sentence idea:** Demonstrate that the now-dominant recipe "SAM proposals + VLM labels" systematically fails amorphous stuff regions, so reported open-vocab mIoU improvements are concentrated entirely in thing classes.
- **Problem:** Aggregate mIoU hides that proposal-based open-vocab methods and pixel-based methods have complementary error profiles; the community is converging on proposals without noticing the stuff-class regression.
- **Core Hypothesis:** Decomposing published-style results into things-mIoU and stuff-mIoU shows proposal-based pipelines losing to dense-similarity baselines on stuff by a large margin across benchmarks.
- **Why Important:** Stuff classes dominate pixel area in scenes (roads, sky, vegetation) and matter for robotics/AD applications adopting these pipelines.
- **Why Possibly Novel:** Thing/stuff decomposition of the open-vocab literature has not been reported; the field optimizes a metric mixture that masks the regression.
- **Minimal Experiment:** Run one proposal-based and one dense-similarity open-vocab method on ADE20K; report things/stuff mIoU separately and the per-class rank correlation between methods.
- **Main Risk:** Newer mask-proposal models may already mitigate stuff failure, dating the finding quickly.
- **Cluster:** VLM-DENSE

### C-0019 · Softmax vocabulary interference caps zero-shot segmentation at scale
- **One-sentence idea:** Characterize a negative interference law where adding more candidate class names to an open-vocabulary segmenter's prompt set monotonically degrades per-class IoU of the original classes due to probability mass competition among correlated text embeddings.
- **Problem:** Practitioners silently tune the evaluated vocabulary per dataset; the sensitivity of dense predictions to vocabulary size and composition is undocumented.
- **Core Hypothesis:** Per-class IoU decays approximately logarithmically with the number of distractor synonyms/hypernyms added, and calibration-free softmax over text similarities is the mechanism (sigmoid-per-class scoring removes most decay).
- **Why Important:** Real open-world deployment implies huge vocabularies; a quantified interference law determines whether current architectures can scale to them at all.
- **Why Possibly Novel:** Vocabulary-size ablations exist anecdotally but no mechanistic account (softmax competition vs. representation limits) or scaling curve has been published for dense tasks.
- **Minimal Experiment:** On ADE20K-150, sweep vocabulary from 150 to 5,000 WordNet-expanded terms, plot original-class mIoU under softmax vs. per-class sigmoid scoring.
- **Main Risk:** The effect may be trivially fixable by calibration, reducing the finding's depth (though raising its utility).
- **Cluster:** VLM-DENSE

### C-0020 · VLM segmenters segment texture, not shape
- **One-sentence idea:** Build a dense-prediction cue-conflict benchmark (texture of class A pasted into shape of class B) to show language-supervised segmenters are dramatically more texture-biased than supervised segmenters, inverting the classification-level finding that CLIP is shape-biased.
- **Problem:** The claim "CLIP models are shape-biased" comes from image-level classification and is uncritically extrapolated to dense predictions.
- **Core Hypothesis:** At pixel level, CLIP-derived segmenters label cue-conflict regions by texture far more often than DINOv2- or supervised-backbone segmenters, because patch-text matching keys on local texture statistics.
- **Why Important:** Shape/texture bias at pixel level predicts out-of-distribution behavior (weather, style shift) for deployed segmentation, and the classification-derived intuition may be exactly wrong.
- **Why Possibly Novel:** No cue-conflict methodology exists for dense prediction; all bias measurements are image-level.
- **Minimal Experiment:** Generate 500 cue-conflict scenes via texture transfer within COCO masks; measure texture-vote fraction per backbone family under identical linear-probe decoders.
- **Main Risk:** Texture-transfer artifacts could confound the measurement and must be controlled with human sanity checks.
- **Cluster:** VLM-DENSE

### C-0021 · Text-side brittleness dominates image-side brittleness in language-driven segmentation
- **One-sentence idea:** Show that mIoU of open-vocabulary segmenters drops more from replacing class names with common synonyms than from strong image corruptions, i.e., the text tower is the weakest robustness link.
- **Problem:** Robustness studies of segmentation exhaustively perturb images but never perturb the query vocabulary, though both are inputs in language-driven systems.
- **Core Hypothesis:** Synonym substitution ("sofa"→"couch", "person"→"human being") causes larger and more erratic per-class IoU swings than ImageNet-C-level corruption severity 3 applied to images.
- **Why Important:** Deployed systems receive user vocabulary, not benchmark vocabulary; text-side robustness is the operative failure mode and is unmeasured.
- **Why Possibly Novel:** A controlled image-vs-text perturbation budget comparison for dense prediction has not been formulated.
- **Minimal Experiment:** On Pascal-Context with a fixed segmenter, measure mIoU under (a) 5 synonym sets, (b) corruption severities 1–5; compare variance and worst-case drops.
- **Main Risk:** Choosing "fair" perturbation budgets across modalities is contestable and needs a principled equivalence (e.g., human-recognizability matched).
- **Cluster:** VLM-DENSE

### C-0022 · Feature upsampling choice matters more than backbone choice
- **One-sentence idea:** Claim that at fixed compute, the mIoU variance across feature-upsampling strategies (bilinear, JBU, learned guided filters) exceeds the variance across frozen VLM backbones, inverting the field's attention allocation.
- **Problem:** Benchmark papers sweep dozens of backbones with a fixed bilinear upsampler, implicitly assuming the upsampler is a neutral constant.
- **Core Hypothesis:** A 2×2 factorial (4 backbones × 4 upsamplers) shows upsampler main effect larger than backbone main effect for boundary F-score and comparable for mIoU on high-resolution benchmarks.
- **Why Important:** It redirects effort from backbone shopping to the cheap, understudied upsampling stage, and invalidates backbone rankings made under one upsampler.
- **Why Possibly Novel:** Guided-upsampling works exist, but the variance-decomposition framing that ranks its importance against backbone identity is new.
- **Minimal Experiment:** Run the factorial on Cityscapes linear probing with CLIP/SigLIP/DINOv2/MAE × bilinear/JBU/FeatUp-style/learned-deconv; ANOVA the results.
- **Main Risk:** Effect may hold only for high-res boundary-sensitive datasets, limiting generality.
- **Cluster:** VLM-DENSE

### C-0023 · WordNet synonym averaging matches learned prompt tuning for dense tasks
- **One-sentence idea:** Show that averaging text embeddings over automatically retrieved WordNet synonyms/definitions per class equals gradient-based prompt tuning for open-vocabulary segmentation at zero training cost.
- **Problem:** Prompt-tuning methods for dense tasks require labeled data and per-dataset optimization, but their advantage over trivial lexical expansion has not been established.
- **Core Hypothesis:** The main effect of learned prompts is variance reduction of the class centroid in text space, which synonym averaging achieves for free.
- **Why Important:** Removes a training stage from every open-vocab deployment and provides a much stronger "zero-shot" baseline for future papers to beat.
- **Why Possibly Novel:** Synonym ensembling is known for classification; its head-to-head against learned prompts under dense metrics with matched vocabularies is unreported.
- **Minimal Experiment:** Compare CoOp-style tuned prompts vs. WordNet-averaged embeddings on ADE20K/VOC open-vocab segmentation with the same frozen segmenter.
- **Main Risk:** Learned prompts may encode dataset-specific visual context (e.g., "aerial view") that lexical expansion cannot reach.
- **Cluster:** VLM-DENSE

### C-0024 · Grounding fine-tuning exhibits strong recency bias over data curriculum
- **One-sentence idea:** Establish that in multi-source grounding fine-tuning of VLMs, final performance per source is dominated by which data appeared in the last fraction of training, making curriculum claims mostly ordering artifacts.
- **Problem:** Papers attribute grounding gains to data mixtures, but training order is rarely controlled or reported, and forgetting dynamics at VLM scale are unquantified for dense abilities.
- **Core Hypothesis:** Swapping the order of two grounding datasets while keeping the mixture identical changes per-benchmark results by more than typical claimed SOTA margins.
- **Why Important:** If ordering noise exceeds reported improvements, a whole tier of "data recipe" papers needs order-randomized error bars.
- **Why Possibly Novel:** Recency/forgetting is studied in continual learning, but not as a confound audit of grounding-data-mixture literature.
- **Minimal Experiment:** Fine-tune one VLM on RefCOCO+Visual-Genome-regions in two orders and interleaved; evaluate all three on four grounding benchmarks; compare spread to published SOTA deltas.
- **Main Risk:** Interleaved training may dominate both orders, making the point moot for standard practice (which already interleaves).
- **Cluster:** VLM-DENSE

### C-0025 · Domain transfer failure of open-vocab segmentation is prior mismatch, not feature mismatch
- **One-sentence idea:** Show that most of the accuracy collapse when moving open-vocabulary segmenters to remote sensing or medical imagery is recovered by correcting class-prior and scale statistics, without touching the representation.
- **Problem:** Poor cross-domain results are read as "features don't transfer," prompting costly domain-specific pretraining, but the decision layer's priors (class frequency, object scale) are never re-fit.
- **Core Hypothesis:** Fitting only per-class logit priors and a global scale factor on 20 labeled target images recovers the majority of the gap to domain-pretrained models.
- **Why Important:** A 20-image adaptation beats a pretraining run economically; the result would redefine when domain-specific VLMs are actually necessary.
- **Why Possibly Novel:** Prior-correction is classic, but nobody has used it to decompose the "domain gap" narrative for open-vocab dense models on aerial/medical data.
- **Minimal Experiment:** Evaluate a generic open-vocab segmenter on LoveDA (aerial) raw vs. prior-corrected vs. a domain-pretrained specialist; report gap closure fraction.
- **Main Risk:** Domains with genuinely novel visual primitives (histopathology textures) may show small recovery, splitting the conclusion by domain.
- **Cluster:** VLM-DENSE

### C-0026 · Dense tasks tolerate aggressive token pruning better than classification
- **One-sentence idea:** Contradict the belief that dense prediction needs all tokens by showing segmentation mIoU degrades more gracefully under token merging/pruning than classification accuracy does, because local redundancy is higher than global.
- **Problem:** Token-reduction methods are benchmarked on classification and assumed inapplicable to dense tasks, so dense inference pays full quadratic cost.
- **Core Hypothesis:** With merge-then-unmerge bookkeeping, 50% token reduction costs <1 point mIoU on ADE20K while the same reduction costs more relative accuracy on ImageNet, due to spatially correlated token redundancy.
- **Why Important:** Halving dense-inference cost for free would matter for every high-resolution deployment, and the redundancy asymmetry is scientifically interesting.
- **Why Possibly Novel:** ToMe-style methods report classification; a careful dense-task degradation curve with unmerging protocols and the classification comparison is not established.
- **Minimal Experiment:** Apply training-free token merging at ratios 0–70% to a frozen backbone + linear head on ADE20K and to ImageNet classification; plot normalized degradation curves.
- **Main Risk:** Boundary metrics may degrade faster than mIoU, requiring the claim to be metric-qualified.
- **Cluster:** VLM-DENSE

### C-0027 · Chain-of-thought adds words, not localization, to reasoning segmentation
- **One-sentence idea:** Test whether the intermediate reasoning text in "reason-then-segment" VLMs carries any information used by the mask decoder, by corrupting the rationale while holding the final hidden state pathway intact.
- **Problem:** Reasoning-segmentation papers showcase rationales but never causally test whether masks depend on them.
- **Core Hypothesis:** Replacing generated rationales with shuffled or generic text at inference changes mask IoU negligibly, because the mask token attends to visual features directly and the rationale is decorative.
- **Why Important:** If rationales are epiphenomenal, compute spent generating them at inference is wasted and interpretability claims are unfounded.
- **Why Possibly Novel:** Rationale-corruption causality tests exist for NLP chain-of-thought but not for pixel-output multimodal models.
- **Minimal Experiment:** On ReasonSeg-style queries, intervene on the rationale tokens (shuffle/truncate/replace) before mask-token decoding; measure IoU deltas per intervention.
- **Main Risk:** Some architectures feed rationale tokens into the mask query by design, so results may be architecture-specific and need 2–3 model families.
- **Cluster:** VLM-DENSE

### C-0028 · In-batch concept co-occurrence, not loss design, creates dense alignment
- **One-sentence idea:** Attribute the emergence of patch-level alignment in contrastive VLMs to the statistics of hard negatives within batches (co-occurring concepts forcing spatial disambiguation), predicting that batch composition manipulation alone can create or destroy dense grounding.
- **Problem:** Dense alignment emergence is credited to objectives and architectures, while batch construction — a silent hyperparameter — is never studied as the causal factor.
- **Core Hypothesis:** Training with batches curated to contain caption-overlapping images (shared nouns) yields markedly better zero-shot segmentation than random batches at identical loss and data, while retrieval stays equal.
- **Why Important:** Batch curation is nearly free and would offer a controllable dial for dense ability without new objectives.
- **Why Possibly Novel:** Hard-negative mining is known for retrieval quality, but its causal role in spatial grounding emergence is an untested mechanism.
- **Minimal Experiment:** Train two matched CLIP-small runs (random vs. noun-overlap-curated batches) on the same 20M captions; compare patch-text segmentation on VOC and retrieval on COCO.
- **Main Risk:** Curated batches change effective task difficulty, requiring temperature retuning that complicates matched comparison.
- **Cluster:** VLM-DENSE

### C-0029 · Frozen linear-probe mIoU rank-predicts full fine-tuning outcomes
- **One-sentence idea:** Validate (or refute) the implicit assumption that cheap frozen-feature segmentation probes rank backbones the same way full fine-tuning does, which underlies nearly all "foundation model dense benchmark" papers.
- **Problem:** Frozen probes are used as proxies for deployability, but the rank correlation between probe mIoU and fine-tuned mIoU across modern VLM backbones is unknown.
- **Core Hypothesis:** Rank correlation is high among same-family backbones but breaks down across pretraining paradigms (contrastive vs. generative vs. self-supervised), where fine-tuning plasticity differences reorder the ranking.
- **Why Important:** If the proxy fails across paradigms, backbone selection studies must fine-tune — or the community needs a plasticity-corrected probe.
- **Why Possibly Novel:** Probe-vs-fine-tune correlation studies exist for classification; the dense-task, cross-paradigm version with modern VLMs is missing.
- **Minimal Experiment:** For 8 backbones spanning paradigms, measure linear-probe and full fine-tune mIoU on ADE20K; report Spearman correlation overall and within paradigm groups.
- **Main Risk:** Fine-tuning 8 backbones properly is compute-heavy and recipe-sensitive; conclusions need per-backbone recipe tuning to be fair.
- **Cluster:** VLM-DENSE

### C-0030 · Negation is geometrically impossible in current text-conditioned segmentation
- **One-sentence idea:** Explain why queries like "everything except the road" or "the cup that is not red" fail in text-driven segmenters: negation requires set-complement operations that cosine-similarity scoring cannot represent, and quantify the failure with a constructed negation benchmark.
- **Problem:** Negated referring expressions fail almost universally, but the failure is anecdotal, unbenchmarked, and lacks a representational explanation.
- **Core Hypothesis:** Text embeddings of negated phrases lie close to their non-negated counterparts (measurably small angular displacement), so any similarity-threshold segmenter must confuse them; performance is restored by logit-space subtraction of the negated concept rather than by embedding the negation.
- **Why Important:** Negation is central to practical query languages (safety exclusions, filtering), and knowing it is architectural rather than data-fixable prevents wasted data-collection effort.
- **Why Possibly Novel:** Negation failure is documented for CLIP classification; the geometric account plus a compositional logit-algebra fix for dense prediction is unexplored.
- **Minimal Experiment:** Build 300 negation queries over COCO panoptic scenes; measure embedding displacement of negated vs. base phrases and compare native segmenter accuracy against logit-subtraction inference.
- **Main Risk:** Logit algebra may fix simple negation but not scoped negation ("the person not wearing a hat"), fragmenting the claim.
- **Cluster:** VLM-DENSE
## Sub-cluster VLM-ARCH — Multimodal Architecture, Tokens, and Fusion Phenomena (C-0031 – C-0060)

### C-0031 · Visual tokens collapse into a few carrier tokens inside the LLM
- **One-sentence idea:** Measure attention flow to show that after the first few LLM layers, hundreds of visual tokens are effectively ignored and their information is routed through a handful of "carrier" tokens, implying most visual KV-cache is dead weight.
- **Problem:** VLM inference cost is dominated by visual tokens whose layer-wise utility is unknown; token-pruning works assume utility is spread across tokens and layers.
- **Core Hypothesis:** Beyond layer k (small), attention mass from text tokens concentrates on <5% of visual tokens, and deleting the rest after layer k preserves benchmark accuracy within noise.
- **Why Important:** Enables layer-dependent visual KV eviction with large memory/latency savings, and reveals where cross-modal integration actually happens.
- **Why Possibly Novel:** Attention-sink analyses exist for text; the layer-resolved carrier-token phenomenon for visual tokens and its exploitation for eviction are uncharacterized.
- **Minimal Experiment:** For LLaVA-class models, compute per-layer text→visual attention concentration (Gini), then evaluate benchmarks with post-layer-k visual token deletion at varying k and retention rates.
- **Main Risk:** Carrier structure may vary per task (counting may need distributed tokens), demanding a per-task analysis.
- **Cluster:** VLM-ARCH

### C-0032 · The modality gap is a harmless optimization artifact
- **One-sentence idea:** Test the belief that the "modality gap" (separated image/text cones in CLIP space) hurts downstream performance, by showing gap size is controlled by temperature initialization and its removal changes nothing on transfer tasks.
- **Problem:** Numerous papers propose gap-closing objectives assuming the gap is pathological, without causal evidence linking gap size to any downstream metric.
- **Core Hypothesis:** Across matched training runs differing only in initial temperature and thus final gap size, retrieval, classification, and dense probes are statistically indistinguishable, falsifying the gap-is-harmful narrative.
- **Why Important:** It would retire a research subfield built on an unvalidated premise, or, if refuted, finally give causal evidence for the premise.
- **Why Possibly Novel:** Existing gap studies are correlational post-hoc analyses of public checkpoints; a controlled interventional study is absent.
- **Minimal Experiment:** Train 6 CLIP-small runs with temperature/init manipulations producing gaps from near-0 to large; evaluate a fixed downstream battery; regress performance on gap size.
- **Main Risk:** Gap effects may only matter for arithmetic in embedding space (interpolation, editing), requiring those tasks in the battery.
- **Cluster:** VLM-ARCH

### C-0033 · Projector architecture debates reduce to token count
- **One-sentence idea:** Show that the MLP-vs-QFormer-vs-cross-attention projector debate in VLM assembly is confounded by output token count, and at matched visual token budget all projectors perform equivalently.
- **Problem:** Papers claim architectural superiority of projector designs while silently varying the number of visual tokens fed to the LLM, a first-order performance driver.
- **Core Hypothesis:** Token count explains nearly all variance among projector types; conditional on it, projector choice affects only convergence speed, not final accuracy.
- **Why Important:** It would collapse a noisy design space into one scalar knob and stop misattributed architecture claims.
- **Why Possibly Novel:** No published controlled sweep crosses projector family × token count on identical data and LLM.
- **Minimal Experiment:** Train LLaVA-style models with {linear, MLP, QFormer, perceiver} × {16, 64, 256, 576} tokens on identical data; two seeds each; report benchmark means.
- **Main Risk:** Interaction effects at very low token counts (QFormer may win at 16) could soften the headline claim.
- **Cluster:** VLM-ARCH

### C-0034 · Task-specific information bottlenecks of visual resampling
- **One-sentence idea:** Characterize which capabilities die first as visual tokens are compressed: a capability-resolved bottleneck curve showing VQA saturates at very few tokens while counting, OCR, and spatial relations degrade at predictable, distinct compression thresholds.
- **Problem:** Token compression is evaluated on aggregate benchmarks, hiding that the same compression is lossless for some capabilities and catastrophic for others.
- **Core Hypothesis:** Each capability has a characteristic token budget (an intrinsic dimensionality), and these budgets are stable across model families, enabling principled compression policies.
- **Why Important:** Provides the missing engineering table — tokens needed per capability — and a scientific measure of visual task complexity.
- **Why Possibly Novel:** Existing compression papers report averages; capability-stratified bottleneck curves and their cross-model stability are unmeasured.
- **Minimal Experiment:** Sweep resampler token count over {4..576} for two VLMs, evaluate capability-tagged benchmark slices (counting/OCR/spatial/recognition), plot degradation thresholds.
- **Main Risk:** Capability tags in benchmarks are noisy; may require hand-curating clean capability subsets.
- **Cluster:** VLM-ARCH

### C-0035 · VLMs are bag-of-patches models on most benchmarks
- **One-sentence idea:** Quantify how much of multimodal benchmark performance survives random spatial shuffling of visual patch embeddings, exposing which "understanding" results require no spatial structure at all.
- **Problem:** High benchmark scores are read as evidence of scene understanding, but the degree to which tasks are solvable from an orderless bag of local features is unknown.
- **Core Hypothesis:** Patch-shuffled inference preserves a large fraction of accuracy on most VQA/captioning benchmarks, with drops concentrated in a small set of genuinely spatial questions, thereby defining a "spatiality score" per benchmark.
- **Why Important:** Gives the field a cheap contamination-free diagnostic separating recognition from spatial understanding, re-ranking benchmarks by what they actually measure.
- **Why Possibly Novel:** Shuffling controls exist for CNN-era classification; a systematic patch-shuffle audit of modern VLM benchmark suites is missing.
- **Minimal Experiment:** Evaluate two VLMs on 8 benchmarks with intact vs. permuted visual token positions (keeping position embeddings intact); report per-benchmark retention.
- **Main Risk:** Position embeddings entangled with content could make shuffling implementation-dependent; needs both PE-preserving and PE-shuffling variants.
- **Cluster:** VLM-ARCH

### C-0036 · Unfreezing the vision encoder mostly re-fits normalization statistics
- **One-sentence idea:** Test whether the gains from unfreezing vision encoders during VLM training are reproduced by tuning only LayerNorm/bias parameters, implying the encoder learns no genuinely new features during multimodal alignment.
- **Problem:** Full encoder unfreezing is expensive and risks catastrophic drift, yet the mechanism of its benefit (new features vs. statistical recalibration) is unexamined.
- **Core Hypothesis:** LayerNorm-and-bias-only tuning (<0.1% of parameters) captures most of the full-unfreezing gain on multimodal benchmarks while preserving the encoder's original linear-probe quality.
- **Why Important:** Massively cheaper training, less forgetting, and a mechanistic clarification of what "vision-language alignment" does to the vision tower.
- **Why Possibly Novel:** Norm-tuning is known in NLP (BitFit) but has not been used as a mechanistic probe of encoder unfreezing in VLM assembly.
- **Minimal Experiment:** Train same VLM with encoder frozen / norm-only / fully unfrozen on identical data; report benchmark deltas and encoder ImageNet linear-probe before/after.
- **Main Risk:** High-resolution adaptation may genuinely require attention-weight changes, making the claim resolution-dependent.
- **Cluster:** VLM-ARCH

### C-0037 · Blind baselines should be subtracted from every multimodal score
- **One-sentence idea:** Systematize "language-prior-corrected" scoring where each VLM's benchmark score is reported as improvement over its own image-blind version, revealing that model rankings change substantially under prior correction.
- **Problem:** Multimodal leaderboards mix visual capability with language-prior strength, so models with stronger LLM backbones look visually superior without being so.
- **Core Hypothesis:** Blind-baseline subtraction re-ranks popular VLMs on several benchmarks, and some celebrated capability gaps between models disappear entirely.
- **Why Important:** It cleanly separates perception progress from LLM inheritance — the central attribution question for the field's progress narrative.
- **Why Possibly Novel:** Blind baselines are computed occasionally for datasets, but per-model blind correction (same weights, no image) as a standard metric is not established practice.
- **Minimal Experiment:** Evaluate 6 open VLMs with and without images on 6 benchmarks; publish raw, blind, and corrected scores with rank correlations.
- **Main Risk:** Blind evaluation protocol choices (empty image vs. no image token) can change blind scores; needs a defensible standard.
- **Cluster:** VLM-ARCH

### C-0038 · Multimodal in-context learning is resampler capacity, not interleaved pretraining
- **One-sentence idea:** Challenge the claim that interleaved image-text pretraining creates few-shot multimodal ability, by testing whether single-image-trained models given enough visual context tokens at inference perform comparable in-context learning.
- **Problem:** Interleaved data is expensive to curate and credited with emergent ICL, but the confound — models trained on interleaved data also allocate more visual context — is never controlled.
- **Core Hypothesis:** Much of multimodal ICL is attributable to the LLM's native text ICL plus sufficient visual token bandwidth per exemplar, not to interleaving statistics in pretraining.
- **Why Important:** Would redirect pretraining data investment and clarify the mechanism behind a headline "emergent" capability.
- **Why Possibly Novel:** No controlled comparison exists between interleaved-pretrained and single-image-pretrained models matched on context token budgets at inference.
- **Minimal Experiment:** Take a single-image VLM, enable multi-image contexts at inference by concatenating projector outputs, and compare few-shot classification/VQA curves against an interleaved-pretrained model of matched scale.
- **Main Risk:** Positional extrapolation issues for long visual contexts may bottleneck the single-image model for reasons unrelated to the hypothesis.
- **Cluster:** VLM-ARCH

### C-0039 · VLMs inherit CLIP's bag-of-words bottleneck through the projector
- **One-sentence idea:** Show that compositional failures of LLaVA-class models (attribute binding, word order) are inherited from the vision encoder's contrastively-trained feature geometry, not from the LLM, by swapping encoders with different composition sensitivity.
- **Problem:** Compositionality failures are usually blamed on the LLM's reasoning or data; the encoder's role as the bottleneck is untested because encoder swaps confound many properties.
- **Core Hypothesis:** VLM performance on binding tasks (Winoground-style) tracks the encoder's own composition score and is nearly independent of LLM scale, demonstrating a perception-side ceiling.
- **Why Important:** Locating the compositional bottleneck determines whether the field should fix encoders or scale LLMs — currently a billion-dollar ambiguity.
- **Why Possibly Novel:** Encoder-vs-LLM attribution for compositionality via controlled swaps at fixed data is not in the literature.
- **Minimal Experiment:** Assemble VLMs from {CLIP, SigLIP, DINOv2+lin-align} × {1B, 7B LLM} on identical tuning data; evaluate binding benchmarks; decompose variance.
- **Main Risk:** DINOv2 lacks a text-aligned space, making its assembly pipeline slightly non-comparable.
- **Cluster:** VLM-ARCH

### C-0040 · Resolution scaling dominates LLM scaling for perception tasks
- **One-sentence idea:** Establish compute-matched trade-off curves showing that for fine-grained perception benchmarks, spending FLOPs on higher input resolution beats spending them on LLM parameters by a wide margin, contradicting default scaling allocation.
- **Problem:** VLM scaling folklore says "bigger LLM helps everything," but compute-matched comparisons between resolution and decoder scale are absent.
- **Core Hypothesis:** At fixed total inference FLOPs, a 2B LLM at high resolution beats a 13B LLM at low resolution on OCR, small-object, and fine-grained recognition, while the reverse holds only for knowledge/reasoning tasks.
- **Why Important:** It provides the allocation rule practitioners lack and reframes "multimodal scaling laws" as a two-axis problem.
- **Why Possibly Novel:** Existing scaling studies vary one axis at a time without FLOP matching across axes.
- **Minimal Experiment:** Train a grid {LLM size × input resolution} at matched training/inference FLOPs on identical data; fit capability-specific iso-FLOP frontiers.
- **Main Risk:** Requires several training runs; conclusions may be architecture-specific (AnyRes schemes shift the frontier).
- **Cluster:** VLM-ARCH

### C-0041 · Visual instruction tuning is 300 examples of style, not capability
- **One-sentence idea:** Test a LIMA-style hypothesis for VLMs: a few hundred carefully formatted visual instruction examples achieve most of what 600K-sample instruction datasets achieve, since tuning teaches response format rather than visual capability.
- **Problem:** The community scales visual instruction data aggressively without knowing the capability-vs-style split of its benefits.
- **Core Hypothesis:** Benchmarks scores of a VLM tuned on 300 curated examples fall within a small margin of the full-data model, and the residual gap concentrates in benchmark-specific formats rather than perception quality.
- **Why Important:** Data-collection economics for multimodal instruction tuning would change by orders of magnitude, and the result would sharpen what benchmarks measure.
- **Why Possibly Novel:** LIMA was text-only; no rigorous minimal-data study exists for the visual instruction stage with capability-stratified evaluation.
- **Minimal Experiment:** Tune identical base VLMs on 300 / 3K / 30K / 600K instruction samples; evaluate on perception-heavy vs. format-heavy benchmark splits.
- **Main Risk:** Base model choice (how aligned it already is) heavily conditions the result; needs 2 base models.
- **Cluster:** VLM-ARCH

### C-0042 · Hallucination lives in identifiable language-prior attention heads
- **One-sentence idea:** Localize object hallucination in VLMs to a small set of attention heads where language-prior signals override visual evidence, and show that inference-time down-weighting of those heads reduces hallucination without retraining or decoding tricks.
- **Problem:** Hallucination mitigation is dominated by decoding heuristics and data curation; a mechanistic circuit-level account is missing.
- **Core Hypothesis:** Heads whose outputs correlate with co-occurrence statistics (e.g., "kitchen→refrigerator") and anti-correlate with visual token attention causally drive hallucinated objects, and ablating them cuts POPE-style hallucination at minor fluency cost.
- **Why Important:** A causal handle on hallucination is more robust than decoding patches and transfers across tasks.
- **Why Possibly Novel:** Head-level causal attribution for multimodal hallucination (as opposed to logit-lens observations) has not been demonstrated.
- **Minimal Experiment:** Rank heads by co-occurrence alignment on held-out data, ablate top-k at inference in LLaVA-1.5, measure POPE/CHAIR deltas vs. random-head ablation controls.
- **Main Risk:** Distributed redundancy across heads may make single-head ablations ineffective, requiring circuit-level (multi-head) interventions.
- **Cluster:** VLM-ARCH

### C-0043 · Multi-image confusion is an image-boundary encoding problem
- **One-sentence idea:** Attribute VLM failures at multi-image tasks (attribute swapping across images, wrong-image references) to inadequate encoding of image boundaries in the token stream, and show cheap boundary tokens/2-level positions fix most of it.
- **Problem:** Multi-image failures are treated as reasoning deficits requiring more data, while the token-interface hypothesis is untested.
- **Core Hypothesis:** With explicit learned separator tokens and per-image position offsets, cross-image binding errors drop sharply without any additional training data, showing the deficit was representational bookkeeping.
- **Why Important:** Multi-image and video applications depend on reliable image indexing; a token-level fix is nearly free compared to data scaling.
- **Why Possibly Novel:** Separator/position design is folklore in codebases; a controlled study isolating its causal impact on binding errors does not exist.
- **Minimal Experiment:** Fine-tune the same VLM with 4 boundary-encoding schemes on identical multi-image data; evaluate on a constructed cross-image binding benchmark with swap-detection metrics.
- **Main Risk:** Some failures may be genuine attention-capacity limits that boundary encoding cannot address.
- **Cluster:** VLM-ARCH

### C-0044 · Fusion depth matters only for spatial and counting tasks
- **One-sentence idea:** Provide a task taxonomy showing early-fusion and late-fusion VLMs are equivalent at matched compute on recognition and knowledge tasks, with early fusion winning only where iterative visual re-attention is required (counting, spatial relations, fine OCR).
- **Problem:** The early-vs-late fusion debate is argued globally, though its answer plausibly depends on task structure; no capability-resolved comparison exists at matched scale.
- **Core Hypothesis:** Fusion depth is irrelevant for tasks solvable by one-shot visual summarization and decisive for tasks requiring query-conditioned revisiting of visual detail.
- **Why Important:** It converts an architecture religion into an engineering decision table and predicts which applications justify expensive early fusion.
- **Why Possibly Novel:** Matched-compute, capability-stratified fusion comparisons are absent; existing comparisons confound data, scale, and tokenizers.
- **Minimal Experiment:** Train small early-fusion and late-fusion models on identical data/compute; evaluate a capability-tagged suite; test the interaction statistically.
- **Main Risk:** "Early fusion" implementations vary widely; results may not generalize across instantiations.
- **Cluster:** VLM-ARCH

### C-0045 · The first visual token is an attention sink that starves fine details
- **One-sentence idea:** Show that VLMs develop sink behavior on the first visual token(s), absorbing attention that would otherwise reach detail-bearing tokens, and that sink-aware attention renormalization improves fine-grained tasks for free.
- **Problem:** Attention sinks are documented in text LLMs, but their multimodal counterpart and its cost to visual detail extraction are uncharacterized.
- **Core Hypothesis:** A significant share of text→vision attention mass lands on positionally-first visual tokens regardless of content, and redistributing it (temperature or sink-token insertion) improves OCR/small-object accuracy without hurting other tasks.
- **Why Important:** A training-free accuracy gain and a mechanistic account of a systematic multimodal attention pathology.
- **Why Possibly Novel:** Sink analysis has not been extended to the vision segment of multimodal streams nor linked to fine-grained failures.
- **Minimal Experiment:** Measure content-independence of attention to first visual tokens (shuffle content, watch attention persist); insert dedicated sink tokens before visual stream; evaluate fine-grained benchmarks.
- **Main Risk:** Renormalization may destabilize generation quality in long outputs, requiring careful calibration.
- **Cluster:** VLM-ARCH

### C-0046 · Zero-shot classification accuracy is the wrong metric for choosing VLM encoders
- **One-sentence idea:** Demonstrate that vision encoders' zero-shot ImageNet accuracy — the default selection criterion — poorly predicts their quality as VLM towers, and captioning-pretrained encoders outperform contrastive ones for assembly despite worse zero-shot numbers.
- **Problem:** Encoder selection for VLM assembly relies on classification-centric leaderboards with no validated correlation to multimodal downstream quality.
- **Core Hypothesis:** Across a pool of encoders, rank correlation between zero-shot ImageNet and post-assembly multimodal benchmark scores is weak, and the mismatch is systematic: contrastive training optimizes linear separability that assembly doesn't need, while captioning preserves detail the LLM can exploit.
- **Why Important:** Every VLM project makes this selection; a validated predictor (or the demonstration that none exists) changes standard practice.
- **Why Possibly Novel:** Encoder-selection studies at fixed assembly recipe with paradigm-diverse encoders remain unpublished.
- **Minimal Experiment:** Assemble 8 encoders (contrastive/captioning/self-supervised) into identical LLM+projector recipes; correlate pre-assembly metrics with post-assembly benchmark scores.
- **Main Risk:** One assembly recipe may favor certain encoder families, requiring at least two recipes for robustness.
- **Cluster:** VLM-ARCH

### C-0047 · Patch serialization order shapes VLM spatial reasoning
- **One-sentence idea:** Test whether the raster-scan serialization of visual patches — an arbitrary choice — measurably biases VLM spatial reasoning (e.g., better horizontal than vertical relations) and whether Hilbert-curve or column-major orders shift the bias predictably.
- **Problem:** Serialization order is treated as irrelevant because attention is permutation-capable, but position-embedding priors from language pretraining make the LLM sequence-order sensitive.
- **Core Hypothesis:** VLMs answer horizontal spatial-relation questions better than vertical ones under raster order, and the asymmetry flips or shrinks under alternative space-filling serializations.
- **Why Important:** A confirmed serialization bias would reveal an overlooked, zero-cost design lever and explain reported spatial-reasoning error asymmetries.
- **Why Possibly Novel:** Serialization-order interventions for multimodal LLM reasoning have not been studied; the interaction with pretrained 1D position priors is unexplored.
- **Minimal Experiment:** Fine-tune matched models with raster/column/Hilbert orders; evaluate directional spatial-relation accuracy (left/right vs. above/below) on controlled synthetic scenes.
- **Main Risk:** Effects may vanish with 2D-aware position embeddings, confining relevance to 1D-PE architectures.
- **Cluster:** VLM-ARCH

### C-0048 · AnyRes gains are ensemble denoising, not added resolution
- **One-sentence idea:** Decompose the improvements of multi-crop "AnyRes" schemes to show much of the gain comes from feature averaging across overlapping crops (a denoising ensemble) rather than from genuinely finer spatial sampling.
- **Problem:** High-resolution tiling schemes are motivated by resolution, but they simultaneously introduce multi-view ensembling — an uncontrolled confound.
- **Core Hypothesis:** Matched-pixel single-pass high-resolution inference underperforms tiled inference at the same effective resolution, while adding jittered same-resolution crops to low-res inference recovers a large share of the tiling gain.
- **Why Important:** If ensembling is the operative mechanism, cheaper stochastic-crop averaging replaces expensive tiling, and "resolution" claims in papers need reinterpretation.
- **Why Possibly Novel:** Nobody has separated the ensemble effect from the resolution effect in modern VLM tiling pipelines.
- **Minimal Experiment:** Evaluate one VLM under {low-res, low-res+5 jittered crops averaged, tiled AnyRes, matched-pixel single-pass} on OCR and fine-grained suites.
- **Main Risk:** Single-pass high-res inference may be limited by position-embedding extrapolation, unfairly penalizing that arm.
- **Cluster:** VLM-ARCH

### C-0049 · "Visual chain-of-thought" equals a center-zoom heuristic
- **One-sentence idea:** Show that agentic look-again pipelines (model crops a region, re-encodes, answers) provide gains that a fixed heuristic — zoom to the most attended region — matches, deflating the "visual reasoning" framing to a resolution patch.
- **Problem:** Multi-step visual reasoning pipelines are credited with reasoning ability without a heuristic-matched control at equal compute.
- **Core Hypothesis:** On small-object VQA, attention-argmax zooming captures ≥80% of the agentic pipeline's improvement, with the residual attributable to a small class of genuinely sequential queries.
- **Why Important:** Correct attribution stops overselling agentic complexity and identifies where sequential visual decisions genuinely pay off.
- **Why Possibly Novel:** Heuristic-zoom baselines at matched inference budget are absent from visual-CoT evaluations.
- **Minimal Experiment:** Compare base model / attention-zoom heuristic / full agentic recropping on V*-style small-object benchmarks with identical total pixels processed.
- **Main Risk:** Attention maps may be too noisy in some models to implement the heuristic well, making the control weaker than intended.
- **Cluster:** VLM-ARCH

### C-0050 · A single affine recalibration closes most of the frozen-encoder gap
- **One-sentence idea:** Claim the visual-token distribution mismatch (mean/covariance) with the LLM embedding space explains most of the frozen-vs-finetuned encoder gap, fixable by one whitening-coloring transform fitted without labels.
- **Problem:** Projector training is credited with complex alignment, but the low-order statistics of what it learns are never examined, and expensive end-to-end tuning may be compensating for a fixable distribution shift.
- **Core Hypothesis:** Fitting only a whitening transform of visual features to match LLM token statistics recovers a large fraction of full projector-tuning quality, showing "alignment" is mostly second-order moment matching.
- **Why Important:** Enables near-training-free assembly of new encoder-LLM pairs and demystifies what projectors do.
- **Why Possibly Novel:** Moment-matching analyses of learned projectors and their sufficiency have not been reported.
- **Minimal Experiment:** Compare identity / whitening-coloring / trained-linear / trained-MLP projectors on a fixed VLM recipe, plus CKA between whitened features and trained-projector outputs.
- **Main Risk:** Semantic (not just statistical) alignment may dominate for text-heavy tasks, capping the recovery fraction.
- **Cluster:** VLM-ARCH

### C-0051 · Bigger LLMs can make perception worse
- **One-sentence idea:** Document a perception-interference effect where, holding the vision tower and tuning data constant, larger LLM decoders perform worse on purely perceptual tasks because stronger language priors override visual evidence more aggressively.
- **Problem:** "Scale the LLM" is assumed monotonically beneficial; capability-stratified scaling curves for perception-only slices are not reported.
- **Core Hypothesis:** On tasks with prior-conflicting content (unusual colors, rare object configurations), accuracy decreases with LLM scale, while prior-consistent tasks improve — a measurable crossover.
- **Why Important:** Identifies a genuine cost of decoder scaling and motivates evidence-weighting mechanisms rather than blind scale.
- **Why Possibly Novel:** Inverse-scaling has been studied in text; the visual-evidence-vs-prior interference version with controlled counterfactual images is new.
- **Minimal Experiment:** Assemble 1B/7B/70B-class LLMs with the same frozen encoder and tuning data; evaluate on counterfactual perception sets (green stop signs, five-legged dogs) vs. standard sets.
- **Main Risk:** Tuning-data quantity may need to scale with LLM size for fairness, complicating "matched" training.
- **Cluster:** VLM-ARCH

### C-0052 · Multimodal in-context exemplars act as retrieval keys, not task teachers
- **One-sentence idea:** Test whether few-shot multimodal ICL uses exemplar image-label pairings for task learning or merely for output-space priming, by measuring performance under systematically corrupted exemplar pairings.
- **Problem:** Multimodal ICL gains are interpreted as task adaptation, but the text-domain finding that label correctness barely matters has no multimodal counterpart.
- **Core Hypothesis:** Randomly re-pairing exemplar images with wrong labels leaves most of the few-shot gain intact (format/priming effect), except in genuinely novel-concept tasks where correct pairing matters — cleanly separating two ICL mechanisms.
- **Why Important:** Determines whether multimodal ICL can teach genuinely new visual concepts at inference (a headline hope) or only re-formats existing knowledge.
- **Why Possibly Novel:** Corrupted-exemplar studies exist for text ICL; the multimodal version with a novel-concept axis is missing.
- **Minimal Experiment:** Few-shot evaluation of an ICL-capable VLM with correct/shuffled/adversarial exemplar labels on (a) known-category classification, (b) synthetic novel-category tasks.
- **Main Risk:** Novel-concept synthetic tasks may be too easy/too hard, requiring careful difficulty calibration to reveal the separation.
- **Cluster:** VLM-ARCH

### C-0053 · Absolute-position blindness is an interface bug, not a scale problem
- **One-sentence idea:** Show that VLMs' inability to report where things are (absolute coordinates) stems from projector-induced destruction of positional phase information, fixable by concatenating explicit coordinate channels — no scaling required.
- **Problem:** Positional failures are commonly filed under "will improve with scale/data," delaying a cheap architectural diagnosis.
- **Core Hypothesis:** Adding two normalized coordinate channels to visual features before projection dramatically improves localization outputs at negligible cost, with no gain from doubling instruction data instead — proving the bottleneck is representational, not statistical.
- **Why Important:** Localization is prerequisite for agentic UI control and robotics; identifying it as an interface bug saves misdirected scaling spend.
- **Why Possibly Novel:** Coordinate-channel fixes are known in CNN literature (CoordConv) but their diagnostic use against the scaling narrative in VLMs is new.
- **Minimal Experiment:** Fine-tune matched VLMs (± coordinate channels, ± doubled grounding data) and evaluate point-localization error on held-out layouts.
- **Main Risk:** Modern 2D RoPE variants may already preserve enough position, making the effect model-dependent.
- **Cluster:** VLM-ARCH

### C-0054 · Video benchmarks are mostly single-frame benchmarks in disguise
- **One-sentence idea:** Quantify the fraction of each popular video-LLM benchmark solvable from one uniformly sampled frame plus language priors, producing a "temporal necessity score" that likely exposes most benchmarks as near-frame-solvable.
- **Problem:** Video-LLM progress is claimed on benchmarks whose temporal information requirement has never been audited, so temporal architecture innovations may be rewarded for frame-level improvements.
- **Core Hypothesis:** Single-frame models reach within a few points of video models on most benchmarks, and the ranking of temporal architectures changes drastically once evaluation is restricted to certified temporally-necessary questions.
- **Why Important:** Redirects video-model research toward genuinely temporal capabilities and provides a benchmark-cleaning methodology.
- **Why Possibly Novel:** Single-frame baselines appear scattered in papers; a systematic audit with a formal necessity score and a filtered benchmark release does not exist.
- **Minimal Experiment:** Run frame-count sweeps (1/4/16/64) for two video LLMs across 6 benchmarks; label questions by performance-vs-frames profile; release the temporally-necessary subset.
- **Main Risk:** Frame-sampling strategy interacts with the audit; multiple sampling seeds required for clean necessity labels.
- **Cluster:** VLM-ARCH

### C-0055 · Encoder-ensemble gains are receptive-field diversity, not semantic complementarity
- **One-sentence idea:** Test whether the popular practice of concatenating multiple vision encoders (e.g., CLIP+DINOv2) helps because of "complementary semantics" or simply because it ensembles different effective receptive fields and resolutions — reproducible with one encoder at multiple scales.
- **Problem:** Multi-encoder VLMs claim semantic synergy without controlling for the trivial multi-scale ensemble effect.
- **Core Hypothesis:** A single encoder applied at two resolutions (features concatenated) matches dual-encoder performance on most benchmarks, isolating true cross-paradigm complementarity to a small residual on specific capabilities.
- **Why Important:** Simplifies VLM architecture and corrects the mechanism story guiding encoder-pairing choices.
- **Why Possibly Novel:** The same-encoder multi-scale control for multi-tower VLM claims has not been published.
- **Minimal Experiment:** Compare {CLIP@336}, {CLIP@336+CLIP@672}, {CLIP@336+DINOv2@336}, {CLIP@336+DINOv2@672} assemblies on a capability-stratified suite.
- **Main Risk:** Compute matching across arms (dual encoders cost more) must be handled to avoid confounded conclusions.
- **Cluster:** VLM-ARCH

### C-0056 · Cross-modal attention entropy is an intrinsic quality metric
- **One-sentence idea:** Propose and validate that the entropy profile of text→vision attention during generation predicts a VLM's fine-grained accuracy better than parameter count or benchmark aggregates, providing a task-free intrinsic diagnostic.
- **Problem:** Model selection requires expensive benchmark suites; no intrinsic, evaluation-free indicator of multimodal integration quality exists.
- **Core Hypothesis:** Models whose attention entropy collapses (uniform or single-token) during answer generation systematically fail detail-dependent tasks, and the entropy statistic computed on 100 unlabeled images rank-predicts fine-grained benchmark scores across model families.
- **Why Important:** A cheap intrinsic metric enables rapid architecture iteration and checkpoint selection without benchmark overfitting.
- **Why Possibly Novel:** Attention statistics have been used descriptively; their validation as a predictive intrinsic metric across VLM families is new.
- **Minimal Experiment:** Compute entropy profiles for 10 public VLMs on unlabeled images; correlate with their published/reproduced fine-grained scores; test predictive power on held-out models.
- **Main Risk:** Correlation may be family-specific and fail across architectural paradigms (e.g., cross-attention vs. self-attention fusion).
- **Cluster:** VLM-ARCH

### C-0057 · Joint tuning quietly destroys the encoder's general-purpose value
- **One-sentence idea:** Measure the collateral damage of end-to-end VLM tuning on the vision encoder's transferable representation quality, testing the belief that joint tuning is harmless or beneficial for the tower itself.
- **Problem:** Encoders extracted from tuned VLMs are increasingly reused for other tasks, but whether multimodal tuning improved or silently degraded their general dense/global representations is unmeasured.
- **Core Hypothesis:** Instruction-stage joint tuning improves VLM benchmarks while degrading the encoder's standalone linear-probe and dense-probe quality, with damage concentrated in late layers and high-frequency features.
- **Why Important:** Informs whether the ecosystem should reuse VLM-tuned encoders and whether tuning recipes need representation-preservation constraints.
- **Why Possibly Novel:** Post-assembly encoder autopsies (layer-wise, task-stratified) have not been reported.
- **Minimal Experiment:** Extract encoders before/after joint tuning from two VLM recipes; run ImageNet linear probes, ADE20K dense probes, and layer-wise CKA against the original.
- **Main Risk:** Damage may be recipe-specific (learning rate on encoder), demanding a sweep to make general claims.
- **Cluster:** VLM-ARCH

### C-0058 · VLM digit errors in OCR are tokenizer artifacts, not perception failures
- **One-sentence idea:** Attribute a specific, predictable class of OCR errors in VLMs (digit substitutions, decimal misplacements) to subword tokenization of numerals in the language decoder rather than to visual encoding limits.
- **Problem:** OCR errors are lumped into "perception limits," motivating bigger encoders, while decoder-side tokenization pathologies are a cheaper explanation nobody has isolated.
- **Core Hypothesis:** Error rates spike exactly where numeral token boundaries fall (multi-digit merges), are invariant to image quality above a threshold, and drop sharply when digits are forced to single-character tokenization.
- **Why Important:** Numeric OCR reliability gates document-AI deployment; a tokenizer-level fix is trivially cheap compared to encoder scaling.
- **Why Possibly Novel:** Tokenizer-induced numeric errors are studied in text LLM arithmetic but not causally traced through the multimodal reading pipeline.
- **Minimal Experiment:** Evaluate digit-level OCR confusion matrices on synthetic clean text renders across image qualities; re-decode with digit-split tokenization; compare error structure.
- **Main Risk:** Constrained decoding changes may interact with the LLM's learned numeric distribution, requiring careful like-for-like decoding.
- **Cluster:** VLM-ARCH

### C-0059 · The self-caption bottleneck test: how much does a benchmark need vision?
- **One-sentence idea:** For each multimodal benchmark, replace the image with the model's own generated caption and measure the score retained, yielding a "vision necessity" coefficient that likely exposes many benchmarks as caption-sufficient.
- **Problem:** Benchmarks claiming to test visual understanding may be solvable through a lossy text bottleneck, meaning they test captioning + language reasoning rather than integrated multimodal processing.
- **Core Hypothesis:** A large fraction of benchmark items are caption-sufficient, and cross-benchmark vision-necessity coefficients reorder the perceived difficulty and value of popular evaluations.
- **Why Important:** Provides a principled tool for benchmark triage and for claims about "integrated" multimodal reasoning versus pipeline sufficiency.
- **Why Possibly Novel:** Caption-replacement has been used ad hoc; a standardized self-caption (same-model) protocol removing captioner-capability confounds is new.
- **Minimal Experiment:** For two VLMs and eight benchmarks, evaluate image-input vs. self-caption-input scores; publish per-item necessity labels and aggregate coefficients.
- **Main Risk:** Caption length/detail is a free parameter that must be controlled (fixed token budgets) for meaningful coefficients.
- **Cluster:** VLM-ARCH

### C-0060 · Cross-model projector transplants test the universal-geometry claim
- **One-sentence idea:** Test the "platonic representation" hypothesis concretely by transplanting a projector trained for encoder-A/LLM-B into encoder-C/LLM-B after only a cheap linear stitch, predicting near-full performance if semantic geometries are truly convergent.
- **Problem:** Claims that large models converge to compatible representation geometries are supported by correlation analyses (CKA) but never by functional transplant tests at VLM scale.
- **Core Hypothesis:** A linear map fitted on unpaired features (Procrustes on 10K images) suffices to swap vision encoders under a frozen projector with small benchmark loss, and failure cases pinpoint exactly which capabilities are geometry-incompatible.
- **Why Important:** Functional stitching would enable mix-and-match VLM assembly without retraining and give the representation-convergence debate a decisive, usable test.
- **Why Possibly Novel:** Model stitching exists for CNN classifiers; frozen-projector transplants across modern encoder families in full VLMs are unexplored.
- **Minimal Experiment:** Fit Procrustes maps between CLIP/SigLIP/DINOv2 patch features; run LLaVA with transplanted encoders; report benchmark retention vs. retrained-projector upper bound.
- **Main Risk:** Token-count and normalization mismatches between encoders may dominate results unless carefully standardized.
- **Cluster:** VLM-ARCH
## Sub-cluster FT-INSTAB — Large-Model Fine-Tuning Instability (C-0061 – C-0090)

### C-0061 · Loss spikes are caused by identifiable samples, not bad luck
- **One-sentence idea:** Attribute fine-tuning loss spikes to specific, re-identifiable training samples with characteristic gradient geometry (high norm, low alignment with the average gradient), showing spike prediction and prevention via sample screening.
- **Problem:** Loss spikes during large-model fine-tuning are treated as stochastic events handled by rollback heuristics, without a causal account at the data level.
- **Core Hypothesis:** A small percentile of samples with outlier gradient statistics causes a large majority of spikes across seeds — the same samples spike different runs — and pre-filtering them eliminates most spikes without hurting final quality.
- **Why Important:** Replaces wasteful rollback-and-skip engineering with principled data screening, and reframes "instability" as a data property rather than an optimizer property.
- **Why Possibly Novel:** Spike forensics at sample granularity with cross-seed reproducibility tests has not been published for multimodal fine-tuning.
- **Minimal Experiment:** Fine-tune a 7B VLM twice with different seeds, log per-batch sample IDs at spikes, test cross-seed overlap of spike-implicated samples against chance, then rerun with those samples removed.
- **Main Risk:** Spikes may be caused by sample-state interactions (same sample harmless at other times), weakening pure data attribution.
- **Cluster:** FT-INSTAB

### C-0062 · A µP-style learning-rate transfer rule for LoRA ranks
- **One-sentence idea:** Derive and empirically validate a scaling rule for how optimal LoRA learning rate must change with rank and layer width, replacing the folklore "LoRA needs ~10× higher lr" with a predictive law.
- **Problem:** LoRA hyperparameters are re-tuned per rank/model by trial and error, and instability at high ranks is misread as an intrinsic LoRA property.
- **Core Hypothesis:** With initialization- and rank-aware lr scaling (analogous to µP), the optimal lr becomes rank-invariant, and previously "unstable" high-rank LoRA trains as stably as low-rank.
- **Why Important:** Removes the dominant tuning cost of the most-used fine-tuning method and clarifies which LoRA phenomena are artifacts of unscaled optimization.
- **Why Possibly Novel:** µP theory exists for pretraining widths; its adaptation to the low-rank adapter geometry with empirical transfer curves is not established practice.
- **Minimal Experiment:** Sweep lr × rank ∈ {4..256} on a fixed fine-tuning task with and without the proposed scaling; show collapse of optimal-lr curves onto one point under scaling.
- **Main Risk:** Adam's per-parameter normalization may already absorb part of the scaling, making gains regime-dependent.
- **Cluster:** FT-INSTAB

### C-0063 · Warmup is just Adam second-moment initialization
- **One-sentence idea:** Test the claim that learning-rate warmup in fine-tuning exists solely to let Adam's second-moment estimates stabilize, by replacing warmup with a proper v-initialization from a few estimation-only batches.
- **Problem:** Warmup length is a superstition-driven hyperparameter costing wall-clock time, with competing loss-landscape and optimizer-state explanations never disentangled in the fine-tuning regime.
- **Core Hypothesis:** Initializing Adam's second moments from ~50 gradient-estimation batches allows warmup-free fine-tuning at full lr with no instability, showing the landscape explanation is unnecessary in this regime.
- **Why Important:** Simplifies every fine-tuning recipe and adjudicates a basic optimization question on the practically dominant workload.
- **Why Possibly Novel:** v-initialization has been discussed for pretraining theory, but a clean falsification study in large-model fine-tuning (where landscape arguments differ) is missing.
- **Minimal Experiment:** Fine-tune a 7B model with {standard warmup, no warmup, no warmup + v-init} at multiple lrs; compare spike frequency and final metrics.
- **Main Risk:** Landscape effects may reappear only at the largest scales or with unfrozen vision encoders, limiting the claim's scope.
- **Cluster:** FT-INSTAB

### C-0064 · Forgetting is embedding drift, not body rewiring
- **One-sentence idea:** Show that most catastrophic forgetting during instruction/multimodal fine-tuning is caused by drift of embedding and unembedding matrices rather than changes in transformer blocks, so freezing those two matrices retains generality at no adaptation cost.
- **Problem:** Forgetting is fought with rehearsal data and regularization, without knowing which parameter groups actually cause the capability loss.
- **Core Hypothesis:** Transplanting the original embedding/unembedding into a fine-tuned model recovers most lost general-benchmark performance while retaining most new-task gains, localizing forgetting to interface layers.
- **Why Important:** A parameter-group-level account of forgetting yields free mitigation (freeze two matrices) and changes theories of what fine-tuning modifies.
- **Why Possibly Novel:** Parameter-group swap-back forensics for forgetting in large multimodal models has not been systematically reported.
- **Minimal Experiment:** Fine-tune a 7B LLM/VLM, then evaluate hybrids (original vs. tuned embeddings × original vs. tuned body) on old-task and new-task suites.
- **Main Risk:** Embeddings and body co-adapt, so swap-backs may produce incoherent models unless drift is small.
- **Cluster:** FT-INSTAB

### C-0065 · Pretraining attention entropy predicts fine-tunability
- **One-sentence idea:** Validate attention-entropy collapse in a pretrained checkpoint as a cheap forward-only predictor of downstream fine-tuning instability, enabling checkpoint screening before any tuning run.
- **Problem:** Teams discover a checkpoint is "hard to fine-tune" only after burning compute; no accepted pre-hoc fine-tunability diagnostic exists.
- **Core Hypothesis:** Checkpoints with low attention-entropy margins (heads near saturation) exhibit higher spike rates and narrower stable-lr ranges when fine-tuned, with rank correlation strong enough for practical screening.
- **Why Important:** A validated pre-flight diagnostic saves large amounts of wasted fine-tuning compute across the industry.
- **Why Possibly Novel:** Entropy collapse has been linked to pretraining divergence; its use as a transferable predictor of fine-tuning stability across checkpoints is unexplored.
- **Minimal Experiment:** Take 10 public checkpoints of similar size, measure entropy statistics, fine-tune each on a fixed task across 5 lrs, and correlate stability metrics with the diagnostic.
- **Main Risk:** Confounds across public checkpoints (data, architecture tweaks) may swamp the entropy signal; may need controlled checkpoint families.
- **Cluster:** FT-INSTAB

### C-0066 · Grokking exists in multimodal fine-tuning
- **One-sentence idea:** Look for delayed-generalization (grokking) dynamics when fine-tuning VLMs on small structured datasets, where val performance jumps long after train convergence, controlled by weight decay strength.
- **Problem:** Fine-tuning runs are stopped at train-loss convergence; if grokking-like dynamics exist in this regime, standard early stopping systematically discards better models.
- **Core Hypothesis:** On small compositional multimodal tasks (attribute-object binding), held-out accuracy improves substantially for many epochs after train accuracy saturates, with the delay modulated by weight decay — mirroring algorithmic-task grokking in a realistic setting.
- **Why Important:** Would change stopping criteria for low-data fine-tuning and connect grokking theory to practically relevant multimodal learning.
- **Why Possibly Novel:** Grokking is documented on algorithmic toys; its presence in realistic multimodal fine-tuning is an open empirical question.
- **Minimal Experiment:** Fine-tune a VLM on 2K compositional examples for 200 epochs across weight decays; track train/val curves for delayed jumps.
- **Main Risk:** Realistic data noise may destroy the clean phase transition, yielding ambiguous slow improvement instead.
- **Cluster:** FT-INSTAB

### C-0067 · Seed variance exceeds SOTA margins in fine-tuning literature
- **One-sentence idea:** Systematically quantify run-to-run variance (seed + data order) of standard fine-tuning recipes on popular multimodal benchmarks and compare it against the margins by which recent papers claim improvements.
- **Problem:** Fine-tuning papers report single runs; if variance is comparable to claimed deltas, a substantial fraction of reported progress is noise.
- **Core Hypothesis:** For common 7B-scale recipes, cross-seed standard deviation on several benchmarks exceeds the median improvement margin claimed by papers in the last two years of the subfield.
- **Why Important:** Establishes the field's effective noise floor and forces variance-aware reporting norms.
- **Why Possibly Novel:** Variance audits exist for small NLP models (BERT era); the multimodal 7B-scale audit tied to a survey of claimed margins is new.
- **Minimal Experiment:** Run one standard recipe 10 times varying only seed/order; report per-benchmark sd; compile claimed deltas from a systematic paper sample for comparison.
- **Main Risk:** Compute cost of 10 runs; findings may be dismissed as recipe-specific unless 2–3 recipes are covered.
- **Cluster:** FT-INSTAB

### C-0068 · Fresh optimizer state, not full-rank updates, causes early fine-tuning damage
- **One-sentence idea:** Show that the rapid feature destruction in the first steps of full fine-tuning is driven by cold-started Adam statistics (huge effective steps), and warm-starting optimizer state removes most of the LoRA-vs-full-FT forgetting gap.
- **Problem:** Full fine-tuning's higher forgetting is attributed to update expressiveness, guiding methods toward parameter restriction, while the optimizer-state confound goes untested.
- **Core Hypothesis:** Full FT with second-moment estimates warm-started (from an estimation phase) forgets no more than LoRA at matched new-task performance, relocating the cause from geometry to optimization transients.
- **Why Important:** Would overturn the standard justification for parameter-efficient methods and provide a free fix for full fine-tuning.
- **Why Possibly Novel:** Optimizer-state warm-starting as the explanation for the forgetting gap has not been isolated.
- **Minimal Experiment:** Compare {LoRA, full-FT cold Adam, full-FT warm Adam} on a multimodal tuning task; measure new-task gain vs. general-benchmark retention trade-off curves.
- **Main Risk:** Warm-started statistics may slow adaptation, shifting rather than closing the trade-off curve.
- **Cluster:** FT-INSTAB

### C-0069 · Norm-layer gradients are the spike amplifier
- **One-sentence idea:** Localize fine-tuning loss spikes to gradient amplification through LayerNorm/RMSNorm scale parameters in low-loss regions, and show that a reduced lr on norm parameters alone eliminates spikes without slowing adaptation.
- **Problem:** Spike mitigation uses global clipping and rollbacks; the parameter-group locus of amplification is folklore, not measurement.
- **Core Hypothesis:** At spike onset, norm-parameter gradient norms rise earlier and proportionally more than any other group, and a 10× lr reduction on norms removes the majority of spikes at unchanged convergence speed.
- **Why Important:** A one-line recipe change replacing rollback infrastructure, plus a mechanistic account of the edge-of-stability behavior in fine-tuning.
- **Why Possibly Novel:** Per-group spike forensics with interventional confirmation on large-model fine-tuning is unreported.
- **Minimal Experiment:** Instrument per-group gradient norms during spiking runs; verify temporal precedence of norm-group growth; rerun with group-wise lr intervention.
- **Main Risk:** Precedence may be architecture-dependent (pre-norm vs post-norm), requiring qualification.
- **Cluster:** FT-INSTAB

### C-0070 · bf16 attention-logit rounding is a hidden instability source in long-context fine-tuning
- **One-sentence idea:** Isolate low-precision attention-logit accumulation as a cause of divergence when fine-tuning on longer contexts than pretraining, showing fp32 attention (only) restores stability at negligible cost.
- **Problem:** Long-context fine-tuning instability is blamed on position-embedding extrapolation, with numerical precision as an untested cheaper explanation.
- **Core Hypothesis:** As context grows, bf16 rounding in logit/softmax pipelines creates gradient noise floors that interact with large logits to trigger divergence; enabling fp32 attention math removes instability where PE fixes alone do not.
- **Why Important:** Distinguishing numerics from representational causes prevents misdirected architectural work and gives a free stability lever.
- **Why Possibly Novel:** Precision ablations for training stability at long context (vs. inference quality) are not systematically published.
- **Minimal Experiment:** Fine-tune at 4×-pretraining context under {bf16, fp32-attention, PE-fix, both}; factorial analysis of divergence rates and downstream long-context scores.
- **Main Risk:** Modern fused kernels already use fp32 accumulation in places, so the effect may depend on implementation details that must be documented precisely.
- **Cluster:** FT-INSTAB

### C-0071 · Self-generated data is optimization-easier at equal distribution shift
- **One-sentence idea:** Explain why fine-tuning on model-generated (self-distilled) data is empirically smoother than on human data by showing self-generated targets induce lower gradient-norm variance at matched task shift, formalizing why synthetic-data recipes stabilize training.
- **Problem:** The stability benefit of training on self-outputs is anecdotal, with no controlled comparison isolating distribution shift from target smoothness.
- **Core Hypothesis:** At matched KL-to-base distribution shift, self-generated targets yield lower per-sample gradient norm variance and fewer spikes than human-written targets, because targets lie near the model's high-probability manifold.
- **Why Important:** Provides the missing theory for widely used synthetic-data pipelines and a principled dial for stability-vs-novelty in data design.
- **Why Possibly Novel:** Gradient-geometry comparisons between human and self-generated supervision at matched shift have not been reported.
- **Minimal Experiment:** Construct human and self-generated datasets matched on task and measured shift; fine-tune identically; compare gradient statistics, spike rates, and final quality.
- **Main Risk:** Matching "distribution shift" across data types is nontrivial and the result may hinge on the chosen matching metric.
- **Cluster:** FT-INSTAB

### C-0072 · LoRA finds different minima, not low-rank shadows of full FT
- **One-sentence idea:** Refute the mental model that LoRA approximates full fine-tuning in a low-rank subspace, by showing LoRA and full FT converge to functionally different solutions with distinct generalization and forgetting profiles even when full-FT updates are post-hoc rank-reducible.
- **Problem:** Method development treats LoRA as compressed full FT, guiding rank-selection heuristics from an unvalidated equivalence.
- **Core Hypothesis:** The measured effective rank of full-FT weight deltas is often low, yet projecting full-FT deltas to LoRA's rank does not reproduce LoRA's behavior — the two procedures explore different basins with characteristic OOD differences.
- **Why Important:** Correct mental models drive method design; if LoRA is a different algorithm rather than an approximation, rank heuristics and theory need rebuilding.
- **Why Possibly Novel:** Spectrum analyses of FT deltas exist; the functional-equivalence test (projection + behavioral comparison) closing the loop does not.
- **Minimal Experiment:** Fine-tune both ways on one task; SVD-project full-FT deltas to matched rank; compare all three models on ID, OOD, and forgetting suites plus mode-connectivity between solutions.
- **Main Risk:** Results may vary strongly with rank and lr, requiring a sweep to support general claims.
- **Cluster:** FT-INSTAB

### C-0073 · End-of-pretraining sharpness predicts downstream tuning stability
- **One-sentence idea:** Test whether the top Hessian eigenvalue (or SAM-style sharpness proxy) of a checkpoint predicts its fine-tuning spike propensity and stable-lr range, giving a principled checkpoint-selection criterion beyond validation loss.
- **Problem:** Checkpoint selection for release/fine-tuning uses perplexity, though checkpoints with equal loss can differ in curvature and hence tuning behavior.
- **Core Hypothesis:** Across same-run checkpoints (same data/architecture, different steps or lr schedules), sharpness rank-predicts spike frequency under a standardized fine-tuning probe better than loss does.
- **Why Important:** Cheap curvature probes could become a standard release gate, reducing downstream instability across the ecosystem.
- **Why Possibly Novel:** Sharpness-generalization links are studied; sharpness-*tunability* links with controlled checkpoint families are not.
- **Minimal Experiment:** From one pretraining run, save 8 checkpoints under varied final-lr schedules; measure sharpness; fine-tune each with a fixed probe recipe; correlate.
- **Main Risk:** Sharpness estimates at 7B scale are noisy; may need multiple probe directions and careful estimators.
- **Cluster:** FT-INSTAB

### C-0074 · Instability is noise around a good trajectory: the EMA test
- **One-sentence idea:** Test whether a weight-space EMA of an unstable fine-tuning run silently tracks a high-quality solution even through loss spikes, implying spikes are excursions around a sound mean trajectory rather than trajectory derailments.
- **Problem:** Spikes trigger rollbacks and recipe changes under the assumption they corrupt the run; if EMA weights sail through unharmed, the operational response to instability is wrong.
- **Core Hypothesis:** EMA checkpoints evaluated at spike times show no quality dip, and EMA-final of an unstable high-lr run beats the stable low-lr run's final model — instability is oscillation, not derailment, in a broad regime.
- **Why Important:** Would replace rollback engineering with free EMA tracking and change how the community interprets loss curves.
- **Why Possibly Novel:** EMA is used for generalization gains; its use as an instability diagnostic/rescue with spike-time evaluation is unexamined.
- **Minimal Experiment:** Run deliberately high-lr fine-tuning with EMA tracking; evaluate raw vs. EMA weights at and after spikes; compare against conservative-lr baselines.
- **Main Risk:** True divergences (NaN cascades) obviously break the story; the claim must delimit oscillatory vs. catastrophic regimes.
- **Cluster:** FT-INSTAB

### C-0075 · Rare-token unembedding geometry causes token-level loss explosions
- **One-sentence idea:** Localize a class of fine-tuning instabilities to rare tokens with large unembedding norms, where a few target tokens produce exploding per-token losses, and show per-token gradient clipping outperforms global clipping.
- **Problem:** Global gradient clipping treats instability as batch-level, though loss explosions may be concentrated in specific vocabulary geometry that global norms handle poorly.
- **Core Hypothesis:** Spike batches disproportionately contain rare tokens whose unembedding norm grew during pretraining; clipping at the per-token-loss level prevents these spikes with less optimization distortion than global clipping.
- **Why Important:** More surgical stabilization preserves learning signal, and the vocabulary-geometry account connects tokenizer design to training stability.
- **Why Possibly Novel:** Token-resolved spike forensics and per-token clipping comparisons are absent from fine-tuning practice.
- **Minimal Experiment:** Log per-token losses during spiking runs, test rare-token enrichment at spikes, compare global vs. per-token clipping on stability and final metrics.
- **Main Risk:** Multimodal fine-tuning may show different loci (image-token positions), requiring the analysis per modality.
- **Cluster:** FT-INSTAB

### C-0076 · A critical window governs when vision encoders can be safely unfrozen
- **One-sentence idea:** Establish that unfreezing the vision encoder during VLM training has a phase boundary: unfreezing before the projector converges causes irreversible representation collapse, while after it, unfreezing is uniformly safe — turning two-stage folklore into a measurable criterion.
- **Problem:** The freeze-then-unfreeze recipe is universal but unexplained; failures are handled by superstition rather than a monitorable readiness signal.
- **Core Hypothesis:** Collapse occurs iff encoder gradients at unfreeze time are dominated by projector-misalignment error, and a simple readiness statistic (projector loss plateau or gradient-alignment score) predicts safe unfreezing across recipes.
- **Why Important:** Converts a fragile scheduling heuristic into a monitored criterion, preventing silent encoder damage in every VLM training run.
- **Why Possibly Novel:** The existence and predictability of a sharp unfreeze phase boundary has not been mapped.
- **Minimal Experiment:** Sweep unfreeze step across training on a fixed recipe; measure final benchmarks and encoder linear-probe retention; test the readiness statistic's predictive accuracy.
- **Main Risk:** The boundary may be soft (graded damage), yielding a less crisp but still useful result.
- **Cluster:** FT-INSTAB

### C-0077 · Cleaner pretraining data makes models harder to fine-tune
- **One-sentence idea:** Test the counterintuitive hypothesis that models pretrained on aggressively filtered, high-quality data are more brittle under fine-tuning (narrower stable-lr range, more forgetting) because their representations are sharper and less redundant.
- **Problem:** Data-quality improvements are assumed strictly beneficial; their effect on downstream *adaptability* has never been measured as an outcome.
- **Core Hypothesis:** Holding compute and architecture fixed, higher pretraining-data filtering strength correlates with higher fine-tuning spike rates and larger old-capability losses at matched new-task gains.
- **Why Important:** If quality trades off against tunability, foundation-model data curation must optimize for a new objective the field is not tracking.
- **Why Possibly Novel:** The data-quality → tunability causal chain is unstudied; existing work stops at pretraining benchmarks.
- **Minimal Experiment:** Pretrain three small LMs on unfiltered/lightly/heavily filtered versions of one corpus at matched tokens; run a standardized fine-tuning battery; compare stability and forgetting.
- **Main Risk:** "Quality" operationalization strongly shapes results; requires multiple filtering axes to be credible.
- **Cluster:** FT-INSTAB

### C-0078 · Gradient clipping is a covert data filter
- **One-sentence idea:** Reinterpret gradient clipping during fine-tuning as implicit data curation — the steps it truncates correspond to identifiable low-quality or mislabeled samples — and show explicit removal of those samples beats clipping.
- **Problem:** Clipping is understood as optimizer protection; its selective silencing of specific data, and whether that silencing is beneficial or harmful, is unexamined.
- **Core Hypothesis:** Samples whose batches trigger clipping are enriched for annotation errors and format anomalies (verifiable by human audit), and training without clipping but with those samples removed matches or beats clipped training.
- **Why Important:** Unifies optimization hygiene and data cleaning, and suggests clipping telemetry as a free data-quality signal in every run.
- **Why Possibly Novel:** The clipping-as-curation equivalence with human-validated audits has not been established.
- **Minimal Experiment:** Log clip-triggering samples on an instruction dataset, audit 200 of them vs. random controls for error rates, then compare {clipping, removal, both} training arms.
- **Main Risk:** At large batch sizes, per-batch clipping poorly localizes offending samples; may require micro-batch attribution.
- **Cluster:** FT-INSTAB

### C-0079 · Layer-wise lr decay is disguised early-layer early stopping
- **One-sentence idea:** Decompose the benefit of layer-wise learning-rate decay (LLRD) in fine-tuning to show it is functionally equivalent to training early layers for fewer effective steps, and that simple early-layer freezing schedules reproduce it.
- **Problem:** LLRD is a standard recipe ingredient with a vague "preserve general features" justification and an untested mechanism.
- **Core Hypothesis:** Matching each layer's total update norm between LLRD and a freeze-schedule baseline produces indistinguishable final models, establishing that LLRD's decay constant is just a reparametrized stopping time per depth.
- **Why Important:** Mechanistic clarity collapses a hyperparameter into an interpretable schedule and predicts when LLRD should fail (tasks needing early-layer change).
- **Why Possibly Novel:** LLRD has never been given a controlled mechanistic equivalence test.
- **Minimal Experiment:** Fine-tune with LLRD vs. matched-update-norm freezing schedules on tasks that do and do not require low-level feature change (e.g., new modality vs. same-domain instructions); compare outcomes.
- **Main Risk:** Equivalence may hold for loss but not for OOD behavior, complicating the headline.
- **Cluster:** FT-INSTAB

### C-0080 · Preference-tuning instability from reward-policy feature entanglement
- **One-sentence idea:** Explain oscillatory divergence in multimodal preference tuning (DPO/RLHF variants) as a degenerate feedback loop arising when reward model and policy share vision-encoder features, and show de-correlating the towers stabilizes training.
- **Problem:** Preference optimization on VLMs is notoriously unstable, attributed vaguely to reward hacking, while the shared-representation feedback mechanism is untested.
- **Core Hypothesis:** When reward and policy share (or start from) the same vision encoder, policy updates move both scoring and generation in correlated directions, producing runaway drift; using an independently pretrained reward encoder removes most instability at equal reward quality.
- **Why Important:** Gives an actionable design rule for multimodal RLHF and a concrete mechanism for a widely suffered failure.
- **Why Possibly Novel:** Reward-policy representational coupling as a stability variable has not been isolated experimentally.
- **Minimal Experiment:** Run DPO on a VLM with reward signals from (a) same-encoder reward model, (b) different-encoder reward model, matched on preference accuracy; compare training stability and end quality.
- **Main Risk:** Constructing equally accurate reward models on different encoders takes care; residual accuracy gaps confound stability comparisons.
- **Cluster:** FT-INSTAB

### C-0081 · The LoRA-forgets-less claim fails under matched update norms
- **One-sentence idea:** Test whether LoRA's celebrated forgetting advantage over full fine-tuning survives when both methods are matched on total functional change (update norm or KL from base), rather than on epochs and default lrs.
- **Problem:** Comparisons underlying "parameter-efficient = forgetting-robust" use default hyperparameters that give full FT far larger effective updates, confounding method with dosage.
- **Core Hypothesis:** At matched KL-to-base or matched new-task performance, LoRA and full FT show equal forgetting, revealing the advantage as a dosage artifact rather than a geometric property.
- **Why Important:** The claim guides method choice across the industry; a dosage-controlled refutation (or confirmation) would materially update practice.
- **Why Possibly Novel:** Dosage-matched forgetting comparisons are absent; papers match epochs, not functional change.
- **Minimal Experiment:** Sweep lrs for both methods on one task; plot forgetting vs. new-task-gain trade-off curves; test whether curves coincide.
- **Main Risk:** Choice of "functional change" metric (KL, norm, benchmark delta) may itself decide the outcome; report several.
- **Cluster:** FT-INSTAB

### C-0082 · Freezing norm parameters stabilizes fine-tuning at zero cost
- **One-sentence idea:** Contradict the norm-tuning intuition (BitFit-style) by showing that *freezing* LayerNorm/RMSNorm scales during fine-tuning removes most instability while leaving final task performance unchanged, because norm scales are high-leverage, low-information parameters.
- **Problem:** Norm parameters are always trained by default; their causal contribution to instability vs. their contribution to adaptation quality has never been separated.
- **Core Hypothesis:** Norm-frozen fine-tuning matches full recipes on final benchmarks across tasks while cutting spike frequency substantially, showing norms contribute leverage (instability) but negligible task information in the fine-tuning regime.
- **Why Important:** A recipe simplification with stability benefits, and a counterpoint to the parameter-efficiency literature that tunes exactly these parameters.
- **Why Possibly Novel:** Norm-freezing is untested as a stabilization method; the field has only studied norm-only tuning, not norm-excluded tuning.
- **Minimal Experiment:** Fine-tune 7B models on 3 tasks with norms trainable vs. frozen across an lr sweep; compare stability envelopes and final scores.
- **Main Risk:** Distribution-shifted inputs (new modality) may genuinely require norm adaptation, restricting the claim to same-modality tuning.
- **Cluster:** FT-INSTAB

### C-0083 · Progressive unfreezing returns as necessary at large scale
- **One-sentence idea:** Test the scale-dependence of the abandoned progressive-unfreezing technique, hypothesizing that it becomes beneficial again at 7B+ parameters where cold full-parameter fine-tuning damages high-leverage layers before optimizer statistics stabilize.
- **Problem:** Techniques discarded at small scale (BERT era found unfreezing schedules unnecessary) are assumed dead, but scale reverses many optimization phenomena and nobody re-tests folklore across scale.
- **Core Hypothesis:** The benefit of progressive unfreezing over one-shot full FT is negative or zero below 1B parameters and grows positive with scale, driven by early-step damage measurable via layer-wise CKA-to-init.
- **Why Important:** Establishes "re-test folklore across scale" as a finding class, with a concrete recipe consequence for large-model tuning.
- **Why Possibly Novel:** Scale-resolved re-evaluation of unfreezing schedules with mechanistic damage metrics has not been done.
- **Minimal Experiment:** Compare one-shot vs. progressive unfreezing at 0.5B/3B/7B on the same task; track early-step CKA damage and final quality per scale.
- **Main Risk:** The crossover point may sit above accessible scale, yielding an unresolved trend rather than a demonstration.
- **Cluster:** FT-INSTAB

### C-0084 · Epoch-wise double descent in instruction tuning
- **One-sentence idea:** Document a non-monotonic epoch-performance curve in instruction tuning where benchmark scores dip around train-set interpolation and recover with continued training, implying popular 1–3-epoch heuristics stop inside the dip.
- **Problem:** Epoch counts for instruction tuning are folklore (train ~2 epochs); if double descent exists here, the field's stopping heuristic is systematically suboptimal.
- **Core Hypothesis:** With sufficient data reuse, held-out benchmark performance follows a dip-recover pattern positioned at memorization onset, and the recovered region yields better OOD robustness than the pre-dip early stop.
- **Why Important:** Directly actionable for every instruction-tuning run and connects modern practice to double-descent theory in a regime where it is presumed absent.
- **Why Possibly Novel:** Double descent is characterized for pretraining-style setups; epoch-wise curves for instruction tuning at 7B scale are not carefully mapped.
- **Minimal Experiment:** Instruction-tune for 20 epochs on a mid-size dataset with dense checkpointing; evaluate benchmark trajectories; locate memorization onset via train-loss statistics.
- **Main Risk:** The dip may be shallow relative to eval noise, requiring many evaluation seeds for significance.
- **Cluster:** FT-INSTAB

### C-0085 · The loss-benchmark decoupling point of instruction tuning
- **One-sentence idea:** Characterize when and why held-out instruction loss stops correlating with benchmark performance during fine-tuning, giving a measurable "decoupling point" after which loss-based decisions (early stopping, lr selection) become actively misleading.
- **Problem:** Practitioners select checkpoints and hyperparameters by validation loss, yet anecdotes abound of lower-loss models scoring worse; the phenomenon lacks quantification and mechanism.
- **Core Hypothesis:** Correlation between val loss and benchmark scores decays predictably as tuning progresses, driven by loss concentrating on format tokens whose mastery saturates — token-class-decomposed loss restores the correlation.
- **Why Important:** Restores a usable cheap selection signal (decomposed loss) and warns precisely when raw loss lies.
- **Why Possibly Novel:** Loss-score decoupling is complained about but not measured, timed, or mechanistically decomposed by token class.
- **Minimal Experiment:** Dense-checkpoint one tuning run; compute loss (total and split into content/format tokens) and 6 benchmark scores per checkpoint; plot correlation vs. training time.
- **Main Risk:** Token-class labeling (content vs. format) is heuristic; conclusions depend on defensible splits.
- **Cluster:** FT-INSTAB

### C-0086 · Data ordering variance rivals data mixture effects
- **One-sentence idea:** Show that reshuffling the order of an identical fine-tuning data mixture changes final benchmark scores by as much as swapping between competing published mixtures, undermining mixture-attribution claims in data-recipe papers.
- **Problem:** Data-recipe papers attribute gains to composition while training order — pure noise with respect to their claims — is neither controlled nor reported.
- **Core Hypothesis:** Across 5 order-reshuffles of one mixture, the benchmark score spread overlaps the reported differences between prominent mixture recipes at the same scale.
- **Why Important:** If ordering noise ≈ mixture effect, the data-recipe literature needs order-randomized replication to say anything at all.
- **Why Possibly Novel:** Order-vs-composition variance decomposition at instruction-tuning scale is not published.
- **Minimal Experiment:** Fix one mixture, train 5 order-shuffles + 2 alternative mixtures; compare within-mixture spread to between-mixture gaps on standard benchmarks.
- **Main Risk:** Result may differ strongly by dataset size (ordering matters more for small data), requiring at least two data scales.
- **Cluster:** FT-INSTAB

### C-0087 · Noise injection beats batch skipping for spike recovery
- **One-sentence idea:** Test the landscape-vs-data explanation of recurrent loss spikes by comparing standard rollback-and-skip-data recovery against rollback-plus-parameter-noise, which should work better if spikes stem from entering pathological curvature regions rather than from bad batches.
- **Problem:** Rollback-and-skip is universal but assumes data causality; if the same region of weight space re-triggers spikes with any data, skipping batches wastes data for nothing.
- **Core Hypothesis:** After rollback, injecting small isotropic weight noise avoids spike recurrence at a higher rate than skipping the implicated batches, evidencing landscape (not data) causality for a substantial spike class.
- **Why Important:** Directly improves large-run reliability engineering and adjudicates between the two dominant informal theories of spikes.
- **Why Possibly Novel:** Controlled comparisons of spike-recovery strategies with causal interpretation are absent from the literature.
- **Minimal Experiment:** On a spiking fine-tuning configuration, deploy both recovery policies across many spike events; compare recurrence rates and final model quality.
- **Main Risk:** Spike populations are heterogeneous; the answer may be "both mechanisms exist," demanding a classifier of spike types.
- **Cluster:** FT-INSTAB

### C-0088 · Adapter placement decides OOD behavior, not ID accuracy
- **One-sentence idea:** Show that placing adapters in attention vs. MLP blocks yields identical in-distribution fine-tuning results but systematically different out-of-distribution robustness, because MLP adapters edit stored knowledge while attention adapters edit routing.
- **Problem:** Adapter-placement studies compare ID accuracy, find small differences, and conclude placement is a non-issue — without ever measuring OOD or forgetting profiles where the mechanistic difference should surface.
- **Core Hypothesis:** At matched parameter budgets and ID accuracy, attention-placed adapters preserve factual knowledge better under distribution shift, while MLP-placed adapters transfer better to tasks needing new associations — a dissociation predicted by the routing/knowledge division of labor.
- **Why Important:** Turns adapter placement from an arbitrary choice into a task-dependent design rule grounded in transformer mechanistics.
- **Why Possibly Novel:** The interaction of placement with OOD/forgetting axes (rather than ID accuracy) is untested.
- **Minimal Experiment:** Fine-tune with attention-only vs. MLP-only adapters at matched budget on 3 tasks; evaluate ID, OOD variants, and knowledge-retention probes.
- **Main Risk:** The routing/knowledge division is itself approximate; results may be muddier than the clean prediction.
- **Cluster:** FT-INSTAB

### C-0089 · A sharp learning-rate phase boundary separates adaptation from reorganization
- **One-sentence idea:** Map fine-tuning into two phases divided by a critical learning rate: below it, representations stay near init (adaptation); above it, they reorganize globally (CKA-to-init collapse) — with benchmark consequences that make the boundary, not the lr value, the object to tune.
- **Problem:** Learning-rate selection for fine-tuning is treated as a smooth trade-off, but scattered evidence suggests qualitatively distinct regimes that current sweeps blur.
- **Core Hypothesis:** Layer-wise CKA-to-init as a function of lr shows a sharp transition at a critical lr*, which co-locates with forgetting onset and OOD-robustness loss, and lr* is predictable from initial gradient statistics.
- **Why Important:** Reduces lr tuning to boundary estimation, and gives a principled definition of "safe" fine-tuning intensity.
- **Why Possibly Novel:** Phase-transition framing with CKA order parameters for fine-tuning lr has not been established.
- **Minimal Experiment:** Fine-tune across a dense lr grid; plot CKA-to-init, forgetting, and new-task gain vs. lr; test sharpness of the transition and its predictability across tasks.
- **Main Risk:** The transition may be smooth at some depths and sharp at others, complicating a single-boundary story.
- **Cluster:** FT-INSTAB

### C-0090 · Text-batch rehearsal works by gradient rebalancing, not by content
- **One-sentence idea:** Test why interleaving text-only batches during multimodal fine-tuning prevents language-capability forgetting: the standard rehearsal-content explanation vs. the hypothesis that any gradient of matched scale on the language pathway (even from random text) rebalances update norms and prevents drift.
- **Problem:** Rehearsal data is carefully curated at real cost under the assumption that its content matters, an assumption never tested against content-free controls.
- **Core Hypothesis:** Interleaving random web text (or even repeated single documents) preserves language benchmarks nearly as well as curated rehearsal mixtures, showing the mechanism is optimization balance rather than knowledge refreshing.
- **Why Important:** Would eliminate rehearsal-data curation costs and reveal a general principle for multi-capability fine-tuning.
- **Why Possibly Novel:** Content-free rehearsal controls are missing from multimodal training literature.
- **Minimal Experiment:** Multimodal fine-tuning with rehearsal arms {none, curated text, random text, repeated single text} at matched token budgets; compare language-benchmark retention.
- **Main Risk:** Content-free rehearsal may protect fluency but not knowledge, requiring capability-stratified evaluation to resolve.
- **Cluster:** FT-INSTAB
## Sub-cluster REP-LEARN — Representation Learning (C-0091 – C-0120)

### C-0091 · Linear probes measure separability, not usability
- **One-sentence idea:** Demonstrate that linear-probe accuracy — the field's default representation-quality metric — fails to predict how useful features are to realistic nonlinear heads under distribution shift, and propose a "tunability probe" that does.
- **Problem:** Representation learning progress is scored by linear probes, though deployment always uses nonlinear heads and shifted data; the probe-deployment correlation is assumed, not measured.
- **Core Hypothesis:** Across a diverse backbone set, linear-probe rank correlates weakly with performance of lightweight nonlinear heads evaluated OOD, and the disagreement is systematic: probes reward compressed, augmentation-aligned features that generalize worse.
- **Why Important:** If the field's primary metric misranks models for actual use, years of method comparisons need reinterpretation and a better standard metric.
- **Why Possibly Novel:** Probe-vs-deployment correlation studies with OOD endpoints across modern backbone families are missing.
- **Minimal Experiment:** For 12 backbones, measure ID linear probe, ID MLP probe, and OOD MLP probe on 4 dataset pairs (e.g., ImageNet→Sketch); report rank correlations and disagreement structure.
- **Main Risk:** OOD endpoint choice may drive conclusions; needs several shift types (style, corruption, dataset).
- **Cluster:** REP-LEARN

### C-0092 · The top principal components of SSL features are nuisance, not signal
- **One-sentence idea:** Show that the leading PCA directions of self-supervised features encode photometric and camera nuisances (lighting, blur, JPEG), and simply deleting the top-k components improves k-NN and few-shot transfer.
- **Problem:** Feature post-processing folklore (whitening helps retrieval) lacks a content-level account of *what* occupies dominant variance directions in modern SSL features.
- **Core Hypothesis:** Top components correlate with nuisance factors measurable from EXIF/synthetic perturbations, and top-k removal yields consistent transfer gains across SSL (but not supervised) backbones, exposing an objective-specific pathology.
- **Why Important:** A zero-cost universal improvement plus a diagnostic of what contrastive/distillation objectives overweight.
- **Why Possibly Novel:** Component-level semantic audits linking variance structure to nuisance factors across paradigms are unpublished.
- **Minimal Experiment:** Correlate top-10 PCs of DINOv2/CLIP/MAE features with controlled photometric perturbation axes; evaluate k-NN transfer with ablated components on 6 datasets.
- **Main Risk:** "Nuisance" is task-dependent (blur matters for quality assessment), so gains may not be universal.
- **Cluster:** REP-LEARN

### C-0093 · Dimensional collapse doesn't hurt transfer
- **One-sentence idea:** Test the assumed harm of dimensional collapse in contrastive learning by constructing models with controlled effective ranks and showing transfer performance is flat over a wide collapse range.
- **Problem:** A substantial method literature adds anti-collapse regularizers, motivated by rank metrics whose causal link to downstream quality has not been established.
- **Core Hypothesis:** Effective rank can vary by an order of magnitude at fixed transfer accuracy; collapse metrics are correlates of training configurations, not causes of quality loss, except at extreme collapse.
- **Why Important:** Would retire a class of regularizers and stop rank statistics being used as quality gates in practice.
- **Why Possibly Novel:** Interventional rank control (via projector dimensionality/objective mixing) with transfer endpoints is missing; existing evidence is correlational.
- **Minimal Experiment:** Train SimCLR-style models with rank manipulated via projector bottlenecks and decorrelation strengths; map effective rank vs. transfer accuracy on 5 tasks.
- **Main Risk:** Rank manipulation levers may affect quality through other channels, requiring multiple independent levers to isolate rank.
- **Cluster:** REP-LEARN

### C-0094 · Emergent invariances exceed the augmentation menu
- **One-sentence idea:** Catalog invariances that SSL models acquire without corresponding augmentations (viewpoint, occlusion, illumination direction), and identify which dataset symmetries — not objectives — supply them.
- **Problem:** The canonical story "augmentations define invariances" cannot explain robustness to transformations never applied during training, leaving the true origin of invariances unexplained.
- **Core Hypothesis:** Emergent invariances mirror the natural variation statistics of the pretraining corpus (co-occurring views of similar instances act as implicit positives through batch structure), so corpus manipulation transfers predictable invariances at fixed augmentation policy.
- **Why Important:** Shifts invariance engineering from augmentation design to data design and explains cross-dataset robustness differences between checkpoints.
- **Why Possibly Novel:** Systematic emergent-invariance catalogs with corpus-manipulation causal tests are absent.
- **Minimal Experiment:** Measure invariance spectra (response change under 12 transformation axes) for models trained on corpora with curated variation statistics (e.g., single-viewpoint-filtered vs. multi-view-rich) under identical augmentations.
- **Main Risk:** Constructing corpora that differ only in one variation statistic is difficult; residual confounds likely.
- **Cluster:** REP-LEARN

### C-0095 · Pretraining pooling choice silently shapes patch-token quality
- **One-sentence idea:** Show that whether a model is pretrained with CLS-token or mean-pooled objectives — usually treated as an implementation detail — determines the gradient distribution over patches and thereby the dense-task quality of patch tokens, independent of the objective family.
- **Problem:** Backbones are compared as "DINO vs CLIP vs MAE" while the pooling choice, which changes what gradients patches receive, varies unacknowledged across implementations.
- **Core Hypothesis:** Mean-pool pretraining spreads gradient signal across patches and yields uniformly better dense linear probes than CLS pretraining at matched global-task quality, across objectives.
- **Why Important:** Identifies a free, first-order design lever for dense-friendly backbones and removes a confound from paradigm comparisons.
- **Why Possibly Novel:** Pooling has been ablated for accuracy but not causally linked to patch-gradient statistics and dense transfer within controlled runs.
- **Minimal Experiment:** Pretrain matched ViT-S pairs (CLS vs. mean-pool heads) under two objectives; compare per-patch gradient statistics during training and ADE20K probes after.
- **Main Risk:** Interaction with objective may dominate main effect, complicating the general claim.
- **Cluster:** REP-LEARN

### C-0096 · MIM features hide their value from linear probes in high frequencies
- **One-sentence idea:** Explain the puzzle that masked-image-modeling features probe poorly but fine-tune excellently by showing their advantages live in high-frequency, nonlinearly-coded components that linear probes cannot read but fine-tuning can exploit.
- **Problem:** The linear-probe/fine-tune dissociation of MIM vs. contrastive models is well known but unexplained, leaving backbone selection guidance contradictory.
- **Core Hypothesis:** Band-pass analyses show MIM features carry more mid/high-frequency image information; quadratic or shallow-MLP probes recover much of the probe gap; and the frequency content predicts fine-tuning advantage per task.
- **Why Important:** Resolves a central representation-learning puzzle and yields probe protocols that fairly rank generative-pretrained models.
- **Why Possibly Novel:** Frequency-resolved information accounting connecting the probe gap to fine-tune gains has not been done.
- **Minimal Experiment:** For MAE vs. DINO features, measure reconstructible image bandwidth, run linear/quadratic/MLP probes, and correlate per-task fine-tuning gaps with frequency profiles.
- **Main Risk:** Frequency content may proxy for something else (locality), requiring disentangling analyses.
- **Cluster:** REP-LEARN

### C-0097 · The best-representation layer migrates with scale
- **One-sentence idea:** Establish that the depth at which representations are most transferable moves systematically toward earlier (relative) layers as models scale, making the last-layer convention progressively wrong and predictable via a scaling law of "representation peak depth."
- **Problem:** Feature-extraction depth is fixed by convention, and cross-scale comparisons of backbones silently compare different distances from each model's true peak.
- **Core Hypothesis:** Relative peak depth (best layer ÷ total layers) decreases with model scale across families, because late layers increasingly specialize to the pretraining objective; a two-parameter law predicts the peak from model size.
- **Why Important:** Every frozen-feature user benefits from knowing where to tap; backbone rankings change when each model is evaluated at its peak.
- **Why Possibly Novel:** Layer-wise probing exists per model; the cross-scale law and its consequence for fair backbone comparison are unformulated.
- **Minimal Experiment:** Probe every layer of 3 sizes × 3 families on classification + dense tasks; fit and validate peak-depth scaling; re-rank backbones at-peak vs. last-layer.
- **Main Risk:** The peak may be task-dependent enough to preclude a single law; may need task-conditioned laws.
- **Cluster:** REP-LEARN

### C-0098 · Cosine normalization discards transferable information in feature norms
- **One-sentence idea:** Quantify what the near-universal practice of L2-normalizing features throws away, testing whether feature norms carry transferable signal (familiarity, image quality, object count) that norm-aware transfer methods can exploit.
- **Problem:** Cosine similarity is default in retrieval/few-shot pipelines; the information content of the discarded radial coordinate is unmeasured.
- **Core Hypothesis:** Feature norms predict pretraining-data density (familiarity) and simple image statistics well above chance, and retaining a calibrated norm term improves OOD detection and few-shot calibration at zero training cost.
- **Why Important:** A free improvement to ubiquitous pipelines and a corrective to an unexamined default.
- **Why Possibly Novel:** Norm semantics have been noted anecdotally (e.g., for OOD) but not audited across paradigms with transfer-relevant endpoints.
- **Minimal Experiment:** Regress norms of 6 backbones against familiarity/quality/count factors; compare cosine vs. norm-augmented scoring on OOD detection and few-shot benchmarks.
- **Main Risk:** Norm semantics likely differ per training objective, fragmenting the story into per-paradigm findings.
- **Cluster:** REP-LEARN

### C-0099 · Whitening erases most claimed differences between SSL methods
- **One-sentence idea:** Show that after simple feature whitening at transfer time, the performance differences among major SSL methods (contrastive, distillation, redundancy-reduction) largely vanish, implying much of the method literature differs in second-moment structure, not information content.
- **Problem:** SSL methods are ranked by raw-feature evaluations sensitive to feature conditioning, conflating what features know with how they are scaled.
- **Core Hypothesis:** Whitened k-NN and linear evaluations compress the inter-method spread substantially, and residual differences isolate the genuinely informative distinctions (which the field can then focus on).
- **Why Important:** Cleans up a crowded method space and redefines fair evaluation protocol for representation quality.
- **Why Possibly Novel:** Whitening is known to help retrieval; using it as a method-equivalence test across the SSL literature is a new framing.
- **Minimal Experiment:** Evaluate 8 SSL checkpoints on 6 transfer tasks raw vs. whitened; report spread compression and surviving differences.
- **Main Risk:** Whitening estimates from small transfer sets can be noisy, requiring shrinkage estimators for fairness.
- **Cluster:** REP-LEARN

### C-0100 · The "object-centric bias of SSL" is a crop-policy artifact
- **One-sentence idea:** Attribute the object-centric character of SSL representations to the random-resized-crop policy rather than to dataset content, by training on scene-centric data with crop distributions manipulated to be object-covering vs. scene-covering.
- **Problem:** SSL's ImageNet-centric behavior is blamed on data bias, motivating expensive scene-centric corpora, while the augmentation-geometry explanation remains untested.
- **Core Hypothesis:** With scene-scale crops, SSL on COCO-like data learns strong stuff/context features (better scene parsing probes); with standard object-scale crops, the same data yields object-centric features — the policy, not the corpus, sets the bias.
- **Why Important:** Redirects investment from data collection to a free hyperparameter and enables task-targeted pretraining bias control.
- **Why Possibly Novel:** Crop-scale distribution as the causal factor for object-centricity has not been isolated on fixed data.
- **Minimal Experiment:** Train DINO-style models on COCO with three crop-scale distributions; probe on object classification vs. scene parsing; compare bias metrics.
- **Main Risk:** Multi-crop schemes entangle scale with number of views; careful factorial design needed.
- **Cluster:** REP-LEARN

### C-0101 · Retrieval quality and probe accuracy are orthogonal axes
- **One-sentence idea:** Establish that k-NN retrieval quality and linear-probe accuracy measure distinct representation properties (local metric fidelity vs. global separability), that models trade them off in characteristic family-specific ways, and that downstream tasks split cleanly by which axis they need.
- **Problem:** Papers use retrieval and probes interchangeably as "representation quality," though models demonstrably rank differently on them, causing contradictory conclusions across studies.
- **Core Hypothesis:** A 2D characterization (probe score × retrieval score) clusters backbones by training paradigm, and each downstream task's best backbone is predicted by its position along the relevant axis, not by any single aggregate.
- **Why Important:** Replaces one-dimensional "which backbone is best" discourse with a validated two-axis selection tool.
- **Why Possibly Novel:** The orthogonality claim, its paradigm clustering, and task-axis matching have not been formalized or tested at scale.
- **Minimal Experiment:** Measure both axes for 15 backbones; cluster; validate task-axis predictions on 8 downstream tasks against aggregate-metric selection.
- **Main Risk:** The two axes may correlate too strongly within modern high-quality models to be useful separators.
- **Cluster:** REP-LEARN

### C-0102 · Contrastive temperature is a semantic-granularity dial
- **One-sentence idea:** Show that the temperature in contrastive objectives controls the granularity level (instance vs. fine class vs. coarse class) at which features separate, enabling granularity-targeted pretraining with a single scalar.
- **Problem:** Temperature is tuned for loss stability, and its representational consequences are treated as incidental, while granularity mismatch between pretraining and task is a recognized transfer problem with no controllable lever.
- **Core Hypothesis:** Sweeping temperature moves a measurable "granularity spectrum" (ratio of within-class to within-instance similarity) monotonically, and tasks at different granularities (re-ID vs. coarse classification) peak at different temperatures on the same data.
- **Why Important:** Converts an opaque hyperparameter into a task-alignment control and explains contradictory temperature recommendations across applications.
- **Why Possibly Novel:** Temperature's effect on uniformity is known; its systematic mapping to semantic granularity with task-matched validation is not.
- **Minimal Experiment:** Train matched contrastive models across 6 temperatures; measure granularity spectra; evaluate on instance retrieval, fine-grained, and coarse classification.
- **Main Risk:** Granularity effects may saturate quickly, leaving a narrow useful range.
- **Cluster:** REP-LEARN

### C-0103 · Supervised pretraining matches SSL at equal data scale
- **One-sentence idea:** Test whether the celebrated superiority of modern SSL (DINOv2-style) over supervised pretraining survives when supervised training is given equal data scale via weak labels, modern augmentation, and matched schedules — or whether "SSL is better" is a data-scale confound.
- **Problem:** SSL flagships train on curated 100M+ image corpora while supervised baselines cite ImageNet-1k-era results, making the paradigm comparison an apples-to-oranges artifact that shapes the field's direction.
- **Core Hypothesis:** Supervised/weakly-supervised training on the same corpus (auto-labeled) with modern recipes reaches parity on most transfer tasks, with SSL retaining an edge only on dense correspondence tasks.
- **Why Important:** The paradigm choice steers enormous compute investment; a confound-corrected comparison is foundational.
- **Why Possibly Novel:** Matched-corpus, matched-recipe paradigm comparisons at modern scale are conspicuously absent.
- **Minimal Experiment:** On one 20M-image corpus, train SSL vs. pseudo-label-supervised ViT-B with matched compute; evaluate a broad transfer battery.
- **Main Risk:** Pseudo-label quality becomes a hidden variable; needs sensitivity analysis over labelers.
- **Cluster:** REP-LEARN

### C-0104 · Registers do more than absorb artifacts — they re-localize patch tokens
- **One-sentence idea:** Show that adding register tokens changes the fundamental locality structure of patch representations (patch tokens become more local as registers take over global aggregation), with consequences beyond artifact removal for dense and correspondence tasks.
- **Problem:** Registers are understood as artifact sinks; whether they qualitatively reorganize the division of labor between global and local information is unknown.
- **Core Hypothesis:** With registers, patch-token receptive fields (measured by feature-perturbation footprints) shrink toward locality, improving correspondence tasks but slightly degrading tasks that exploited global-context leakage in patches.
- **Why Important:** Predicts task-dependent effects of a now-default architecture choice and gives a mechanistic account of global/local information routing in ViTs.
- **Why Possibly Novel:** Locality-spectrum measurement pre/post registers and the predicted task dissociation are untested.
- **Minimal Experiment:** Train matched ViTs ± registers; measure patch-token effective receptive fields; evaluate correspondence (dense matching) vs. context-dependent tasks (segmentation with context ablations).
- **Main Risk:** Effects may be small at typical scales, requiring careful statistical treatment.
- **Cluster:** REP-LEARN

### C-0105 · Objects are low-rank neighborhoods in patch-feature space
- **One-sentence idea:** Exploit the hypothesis that patch features within a single object span a low-dimensional subspace while boundaries mark rank transitions, enabling training-free object discovery from local rank statistics and giving a new geometric definition of "objectness" in ViT features.
- **Problem:** Unsupervised object discovery uses attention heuristics or spectral clustering without a principled feature-geometric account of what makes an object segment coherent.
- **Core Hypothesis:** Local intrinsic dimension of patch features is systematically lower inside objects than across boundaries, and a sliding-window rank detector produces competitive unsupervised segmentation with zero learning.
- **Why Important:** A geometry-first account of objectness would unify scattered discovery heuristics and provide diagnostics of which backbones encode objects as subspaces.
- **Why Possibly Novel:** Local-rank structure of patch tokens as an objectness signal is unexplored; existing methods use similarity graphs, not dimensionality.
- **Minimal Experiment:** Compute windowed PCA effective ranks over DINOv2 patch grids on VOC images; threshold rank transitions into segments; compare against spectral-method baselines.
- **Main Risk:** Textured objects may be high-rank internally, breaking the geometric premise for material-heavy scenes.
- **Cluster:** REP-LEARN

### C-0106 · EMA teachers are replaceable by periodic hard snapshots
- **One-sentence idea:** Challenge the necessity of exponential-moving-average teachers in self-distillation SSL by testing whether infrequent hard teacher snapshots (copy every k steps) reach the same quality, isolating what property of the teacher trajectory actually matters.
- **Problem:** EMA is a load-bearing but unexplained component; its smoothness story is untested against simpler alternatives, and EMA complicates distributed training.
- **Core Hypothesis:** Snapshot teachers with appropriate lag match EMA within noise, showing the requirement is only teacher-student lag (a trust region), not weight-space smoothness — while zero-lag (self) teachers collapse, mapping the stability boundary.
- **Why Important:** Simplifies SSL systems and replaces folklore with a quantified lag requirement transferable across methods.
- **Why Possibly Novel:** Controlled EMA-vs-snapshot-vs-lag studies at modern SSL scale are missing.
- **Minimal Experiment:** Train DINO-style models with EMA vs. snapshot teachers across lag values; map final quality and collapse incidence vs. lag.
- **Main Risk:** Interaction with schedule (teacher temperature warmup) may require re-tuning per arm, complicating equivalence claims.
- **Cluster:** REP-LEARN

### C-0107 · Similarity metrics don't predict functional interchangeability
- **One-sentence idea:** Run a meta-evaluation showing that popular representation-similarity metrics (CKA, SVCCA, Procrustes) fail to predict whether two models' features are functionally interchangeable (via stitching or head transfer), and derive which metric properties are needed for functional prediction.
- **Problem:** High-CKA claims underpin scientific conclusions ("models converge to similar representations"), yet the metric's relationship to any operational notion of similarity is unvalidated.
- **Core Hypothesis:** CKA correlates poorly with stitching accuracy across model pairs (especially across architectures), while cheap task-conditioned metrics (probe-agreement) predict interchangeability far better.
- **Why Important:** The field's convergence narratives and model-comparison methodology rest on these metrics; a validity audit affects many downstream claims.
- **Why Possibly Novel:** Stitching-grounded metric validation across diverse modern backbones has not been done comprehensively.
- **Minimal Experiment:** For 20 model pairs, compute 5 similarity metrics and measure stitching/head-transfer performance; rank metrics by predictive power.
- **Main Risk:** Stitching-layer training details introduce their own variance; requires standardized stitching protocols.
- **Cluster:** REP-LEARN

### C-0108 · Paradigm differences reduce to phase-spectrum sensitivity
- **One-sentence idea:** Test whether the practical differences between supervised, contrastive, and generative pretraining reduce to how much they rely on the image phase spectrum (structure) vs. amplitude spectrum (texture statistics), yielding a single Fourier-based signature that predicts downstream behavior.
- **Problem:** Paradigm comparisons invoke vague notions (semantics vs. texture) without a common measurable basis, so the debates persist without resolution.
- **Core Hypothesis:** Phase-swap and amplitude-swap invariance tests give each backbone a 2D Fourier signature that clusters by paradigm and predicts shape-bias, corruption robustness, and style-transfer sensitivity better than paradigm labels themselves.
- **Why Important:** A compact, physical characterization of what pretraining objectives extract would replace fuzzy narratives and enable signature-targeted training.
- **Why Possibly Novel:** Phase/amplitude sensitivity has been used in psychophysics-style CNN studies but not as a unifying cross-paradigm signature with predictive validation.
- **Minimal Experiment:** Measure phase/amplitude-swap feature drift for 12 backbones; correlate signatures with robustness and bias metrics; test predictive transfer to held-out models.
- **Main Risk:** The 2D signature may be too coarse, requiring band-resolved extensions that reduce elegance.
- **Cluster:** REP-LEARN

### C-0109 · Frozen features know tail classes that probes can't see
- **One-sentence idea:** Show that rare/tail classes are well represented in frozen-feature geometry (recoverable with few-shot exemplar matching) even when linear probes trained on the full imbalanced distribution fail them, relocating the long-tail problem from representation to readout.
- **Problem:** Long-tail performance failures are attributed to representations lacking tail information, driving re-sampling and re-weighting pretraining methods, but readout-vs-representation attribution is missing.
- **Core Hypothesis:** Per-class recoverability with balanced few-shot probes is nearly frequency-independent, while full-distribution probe accuracy is strongly frequency-dependent — the gap quantifying how much of "long-tail failure" is pure readout bias.
- **Why Important:** If tail information is present, cheap readout fixes replace expensive pretraining interventions for imbalanced applications.
- **Why Possibly Novel:** The representation/readout decomposition of long-tail failure with frequency-resolved recoverability curves is unreported.
- **Minimal Experiment:** On iNaturalist-style data with frozen backbones, compare full-probe vs. balanced-16-shot per-class accuracy as functions of class frequency.
- **Main Risk:** Extreme tail classes (<10 pretraining occurrences) may genuinely lack representation, bounding the claim.
- **Cluster:** REP-LEARN

### C-0110 · Deduplication shapes representations more than objective choice
- **One-sentence idea:** Quantify the effect of near-duplicate density in pretraining data on representation geometry, testing whether dedup-level explains more variance in downstream quality than the choice among modern SSL objectives.
- **Problem:** Objectives receive the research attention while corpus duplication — which directly shapes what contrastive negatives and distillation targets mean — varies wildly and unreported across studies.
- **Core Hypothesis:** Sweeping dedup aggressiveness on a fixed corpus changes transfer scores by more than switching among {DINO, iBOT, MoCo-v3} at fixed data, with duplication inflating instance-discrimination shortcuts.
- **Why Important:** Re-prioritizes data processing over objective innovation and adds a mandatory reporting variable for reproducibility.
- **Why Possibly Novel:** Dedup effects are studied for memorization in generative models, not as a first-order factor in SSL representation quality.
- **Minimal Experiment:** Train one objective on 4 dedup levels of a web corpus and 3 objectives on one level; ANOVA transfer results across 6 tasks.
- **Main Risk:** Dedup interacts with corpus size; careful token-matched comparisons required.
- **Cluster:** REP-LEARN

### C-0111 · Motion invariance is why video pretraining fails static tasks
- **One-sentence idea:** Explain the persistent underperformance of video-pretrained encoders on static image tasks via a specific mechanism — temporal-invariance objectives collapse pose/state distinctions that static recognition needs — and validate by controlling the invariance horizon.
- **Problem:** Video pretraining "should" subsume image pretraining but empirically doesn't; the field lacks a mechanistic account, so it responds by scaling video data further.
- **Core Hypothesis:** Increasing the temporal span of positive pairs monotonically degrades fine-grained static recognition (pose, state, expression) while helping action recognition, and span-limited video pretraining closes most of the static-task gap.
- **Why Important:** Determines whether video pretraining needs different objectives rather than more data — a major resource-allocation question.
- **Why Possibly Novel:** The invariance-horizon dial as a causal test of the video-image transfer gap is unexplored.
- **Minimal Experiment:** Pretrain video models with positive-pair spans {0.2s, 1s, 5s}; evaluate static fine-grained benchmarks and action recognition; trace the trade-off curve.
- **Main Risk:** Other video-specific factors (motion blur, codec artifacts) may contribute; requires matched-frame-quality controls.
- **Cluster:** REP-LEARN

### C-0112 · OOD robustness peaks in the middle of the network
- **One-sentence idea:** Demonstrate that mid-network features are systematically more robust to distribution shift than the penultimate features everyone uses, so the standard practice of building on final-layer features actively sacrifices robustness.
- **Problem:** Robust-transfer research operates exclusively on final features by convention, potentially missing that depth choice is itself a robustness intervention.
- **Core Hypothesis:** Under style/corruption shift, probe accuracy vs. depth peaks mid-network with a widening ID-OOD gap toward the top, because late layers specialize to pretraining-distribution shortcuts; a depth-ensembled readout beats penultimate readouts OOD at equal ID accuracy.
- **Why Important:** A free robustness gain and a revision of default practice in every frozen-feature pipeline.
- **Why Possibly Novel:** Depth-resolved robustness curves with the ID-OOD gap decomposition across backbone families are not established.
- **Minimal Experiment:** Layer-wise probes on ImageNet→{Sketch, R, C} for 8 backbones; plot ID and OOD accuracy vs. depth; evaluate multi-depth readouts.
- **Main Risk:** The peak location may vary too much across shifts to give one actionable rule.
- **Cluster:** REP-LEARN

### C-0113 · Trained heads barely beat random projections on good backbones
- **One-sentence idea:** Test how much head training actually contributes on top of modern frozen backbones by comparing trained MLP heads against frozen random-feature heads (random MLP + linear readout), predicting near-parity that exposes "head engineering" as low-value on strong features.
- **Problem:** Transfer pipelines invest in head architecture and training tricks, without a random-feature control that would reveal whether the backbone already does all the work.
- **Core Hypothesis:** For strong backbones, frozen random nonlinear expansions plus ridge regression match trained MLP heads on most classification transfers, with trained heads mattering only under severe class imbalance or low-data regimes.
- **Why Important:** Simplifies deployment (closed-form heads, no tuning) and calibrates where readout research can and cannot add value.
- **Why Possibly Novel:** Random-feature head baselines are standard in kernel literature but absent from modern transfer benchmarking.
- **Minimal Experiment:** Compare {linear, trained MLP, random MLP + ridge} heads on 10 transfer datasets × 4 backbones with matched capacity.
- **Main Risk:** Detection/segmentation heads (structured outputs) likely break the parity, so scope must be stated carefully.
- **Cluster:** REP-LEARN

### C-0114 · Do vision embeddings support linear attribute analogies?
- **One-sentence idea:** Systematically test whether vision (and vision-language) embedding spaces support word2vec-style linear analogies over visual attributes (red car − red + blue ≈ blue car), mapping which attribute families are linearly factored and which are entangled.
- **Problem:** Linear semantic arithmetic is assumed in editing and compositional methods but has never been rigorously audited for vision encoders, so methods build on unverified structure.
- **Core Hypothesis:** Color and size factor approximately linearly in VLM image embeddings, while material, pose, and count do not — and the linearity spectrum predicts which zero-shot compositional edits and queries work.
- **Why Important:** Provides the empirical foundation (or refutation) for a whole class of embedding-arithmetic techniques and compositional retrieval systems.
- **Why Possibly Novel:** Analogy audits are canonical in NLP but lack a controlled visual counterpart with synthetic attribute grids.
- **Minimal Experiment:** Render a controlled attribute grid (object × color × size × material); test analogy completion accuracy per attribute family across 6 encoders.
- **Main Risk:** Synthetic-render conclusions may not transfer to natural-image embeddings; needs a natural-image validation subset.
- **Cluster:** REP-LEARN

### C-0115 · Normalization statistics are a dataset fingerprint
- **One-sentence idea:** Show that the running/adaptive normalization statistics of a network encode enough dataset identity to classify which domain a model was tuned on — and exploit this as a fast domain-shift detector and transfer-compatibility test.
- **Problem:** Estimating domain mismatch between a model and incoming data currently requires labeled evaluation; a label-free, forward-pass-only compatibility signal is missing.
- **Core Hypothesis:** Feature first/second moments per layer form a domain fingerprint: distance between a model's stored statistics and statistics of new data predicts its accuracy drop on that data with useful precision.
- **Why Important:** Enables cheap deployment-time monitoring (will this model work here?) and model-zoo routing without labels.
- **Why Possibly Novel:** BN-statistics adaptation is known; the fingerprint-as-accuracy-predictor calibration across models and domains is not established.
- **Minimal Experiment:** For 10 models × 10 domains, regress accuracy drop on layer-wise statistic distances; evaluate prediction error on held-out model-domain pairs.
- **Main Risk:** Transformer LayerNorm has no running stats, requiring activation-statistic estimation that adds a calibration pass.
- **Cluster:** REP-LEARN

### C-0116 · Numerosity emerges in contrastive embeddings without counting supervision
- **One-sentence idea:** Probe whether CLIP-style embeddings encode approximate object counts as a monotone direction (emergent numerosity), challenging the belief that counting requires explicit supervision or architectural machinery.
- **Problem:** VLMs fail counting *tasks*, which is read as absence of numerical representation, but task failure may be a readout/decoding problem masking present-but-unread numerosity signals.
- **Core Hypothesis:** A linear probe recovers log-count from frozen embeddings of controlled multi-object scenes far above chance, with Weber-law-like error scaling — numerosity is represented but not verbalized by the decoder.
- **Why Important:** Separates representation from readout in a canonical VLM failure and points to cheap decoding fixes instead of counting-specific architectures.
- **Why Possibly Novel:** Numerosity probing with psychophysics-style controls (area, density decorrelated) has not been applied to modern VLM embeddings.
- **Minimal Experiment:** Generate scenes with count decorrelated from total area/density; probe log-count from 6 encoders; compare probe accuracy against the same models' verbal counting accuracy.
- **Main Risk:** Probes may exploit residual low-level confounds despite controls; needs multiple confound-decorrelation schemes.
- **Cluster:** REP-LEARN

### C-0117 · Positive-pair mutual information predicts transfer before training ends
- **One-sentence idea:** Validate a data-centric predictor of SSL quality: the estimated mutual information (or proxy overlap statistics) between augmented positive pairs on a corpus predicts final transfer accuracy across augmentation policies, enabling policy selection without full training runs.
- **Problem:** Augmentation policy search requires training many models to completion; no validated cheap predictor of policy quality exists.
- **Core Hypothesis:** A U-shaped relationship links positive-pair information overlap to transfer quality (too much overlap = trivial task, too little = noise), and the optimum is stable across datasets, making the statistic a practical policy-tuning target.
- **Why Important:** Reduces SSL recipe search from GPU-months to statistics computable in minutes, and formalizes the "task difficulty" intuition of augmentation design.
- **Why Possibly Novel:** InfoMin-style intuitions exist; a quantitatively validated, pre-training-time predictive statistic with cross-dataset stability does not.
- **Minimal Experiment:** For 10 augmentation policies, compute pair-overlap statistics and train matched models; fit and cross-validate the predictor on a second dataset.
- **Main Risk:** MI proxies on images are estimator-dependent; conclusions must be robust across estimators.
- **Cluster:** REP-LEARN

### C-0118 · Keep the projector for fine-grained transfer
- **One-sentence idea:** Overturn the universal discard-the-projector convention by showing projector features are superior for fine-grained and instance-level transfer, because the projector holds the invariances while the backbone retains nuisance detail — the standard story backwards for a class of tasks.
- **Problem:** Everyone throws away SSL projectors post-training based on category-level probe results, without task-stratified evidence for what the projector representation is good at.
- **Core Hypothesis:** On instance retrieval and re-identification, projector-output features outperform backbone features from the same models, reversing the category-level ranking, and the reversal is predicted by each task's need for augmentation invariance.
- **Why Important:** Provides free performance for a task family and corrects an unexamined universal practice with a principled task-conditioned rule.
- **Why Possibly Novel:** Task-stratified projector-vs-backbone comparisons with the invariance-based prediction are absent.
- **Minimal Experiment:** Compare backbone vs. projector features for 6 SSL models on {coarse classification, fine-grained classification, instance retrieval, re-ID}.
- **Main Risk:** Projectors are low-dimensional, and dimensionality (not invariance) may explain results; control with matched-dim backbone projections.
- **Cluster:** REP-LEARN

### C-0119 · A universal frequency law of representation quality across paradigms
- **One-sentence idea:** Test whether per-class representation quality follows the same log-linear dependence on pretraining exposure frequency across supervised, contrastive, and self-supervised paradigms — refuting the belief that SSL is inherently fairer to rare classes.
- **Problem:** SSL is promoted as less frequency-biased than supervised learning, but no paradigm-controlled frequency-response curves exist to support the claim.
- **Core Hypothesis:** All paradigms show statistically indistinguishable slopes of per-class probe accuracy vs. log corpus frequency once total exposure is matched, implying frequency bias is a property of gradient learning, not of objectives.
- **Why Important:** The fairness narrative shapes paradigm choice for long-tail applications; a universal law would refocus effort on data reweighting rather than objective design.
- **Why Possibly Novel:** Cross-paradigm frequency-response comparison with matched corpora is missing from the literature.
- **Minimal Experiment:** Pretrain three paradigms on one corpus with measured concept frequencies; fit per-class accuracy vs. frequency curves; compare slopes.
- **Main Risk:** Concept-frequency estimation in images (via captions/detectors) is noisy and could bias slope estimates.
- **Cluster:** REP-LEARN

### C-0120 · Shape bias is a continuous function of crop-scale statistics
- **One-sentence idea:** Show that a model's position on the shape-texture bias spectrum is continuously controllable via the crop-scale distribution during pretraining, collapsing the shape-bias literature's paradigm comparisons into a single augmentation parameter.
- **Problem:** Shape-vs-texture bias differences are attributed to objectives, architectures, and data, in studies that never control the crop-scale distribution — a variable that directly determines whether global shape is visible in training views.
- **Core Hypothesis:** Sweeping minimum crop scale from 0.08 to 0.8 moves cue-conflict shape bias monotonically and reproduces most of the reported between-paradigm bias spread at fixed objective and data.
- **Why Important:** Bias becomes an engineering dial rather than a paradigm mystery, with direct consequences for robustness-targeted pretraining.
- **Why Possibly Novel:** Crop-scale has not been isolated as the dominant causal factor for shape bias in controlled sweeps.
- **Minimal Experiment:** Train matched models across 5 crop-scale distributions × 2 objectives; measure cue-conflict shape bias and corruption robustness.
- **Main Risk:** Bias may saturate at scales where accuracy degrades, entangling bias control with quality loss.
- **Cluster:** REP-LEARN
## Sub-cluster GEN4SEG — Generative Models, SR, and Restoration as Scientific Questions for Understanding/Segmentation (C-0121 – C-0150)

### C-0121 · Diffusion timestep is a semantic-granularity dial, not a single "best layer"
- **One-sentence idea:** Replace the folklore that "middle timesteps give the best diffusion features for segmentation" with a characterization showing the optimal timestep varies systematically by semantic granularity (parts vs. objects vs. scenes), making timestep a controllable granularity selector.
- **Problem:** Diffusion-feature papers pick one timestep by validation and report it as a constant, obscuring a structured dependence that could be exploited.
- **Core Hypothesis:** Part-level segmentation peaks at low noise, object-level at mid noise, and scene/stuff at high noise, consistently across diffusion backbones — because noise level sets the spatial correlation length the denoiser must model.
- **Why Important:** Turns an arbitrary hyperparameter into a principled task-matching rule and explains contradictory timestep recommendations across papers.
- **Why Possibly Novel:** Granularity-resolved timestep curves and the correlation-length account have not been mapped.
- **Minimal Experiment:** Probe Stable-Diffusion UNet features at 10 timesteps on part (PartImageNet), object (VOC), and stuff (ADE stuff subset) segmentation; plot per-granularity peaks.
- **Main Risk:** Layer choice interacts with timestep; requires a full layer×timestep grid to avoid confounded conclusions.
- **Cluster:** GEN4SEG

### C-0122 · Diffusion cross-attention localization comes from the text encoder, not generative training
- **One-sentence idea:** Test whether the celebrated zero-shot localization of text-to-image cross-attention maps is attributable to the frozen text encoder's representations rather than to anything learned by generative training, using matched text encoders in discriminative pipelines.
- **Problem:** Cross-attention segmentation results are cited as evidence that generative training teaches grounding, without controlling for the text tower shared with discriminative alternatives.
- **Core Hypothesis:** A discriminative model trained with the same text encoder and comparable image data develops equally good word-to-region attribution, showing the generative objective contributes little to localization beyond what the language embedding provides.
- **Why Important:** Correct attribution determines whether the field should mine generative models for dense knowledge or just reuse their text towers.
- **Why Possibly Novel:** Text-encoder-matched attribution controls are absent from the diffusion-for-segmentation literature.
- **Minimal Experiment:** Compare word-region attribution quality of SD cross-attention vs. a CLIP-text-conditioned discriminative grounding model trained on similar data volume, on the same evaluation suite.
- **Main Risk:** Matching "comparable data" between generative and discriminative training is contestable; needs multiple matching criteria.
- **Cluster:** GEN4SEG

### C-0123 · The honest generative-vs-discriminative pretraining comparison for dense tasks
- **One-sentence idea:** Run the missing controlled comparison — generative (diffusion) vs. discriminative (contrastive) pretraining at strictly matched data, compute, and architecture — to isolate what generative pretraining actually adds for dense prediction.
- **Problem:** Claims that diffusion features rival or beat discriminative features rest on comparisons across wildly different data scales, architectures, and resolutions.
- **Core Hypothesis:** At matched budgets, generative pretraining wins on boundary precision and part correspondence but loses on semantic classification of regions, netting near-zero aggregate mIoU difference — the paradigms differ in error structure, not quality.
- **Why Important:** The field is investing in generative feature extraction based on uncontrolled evidence; error-structure knowledge would guide hybrid designs.
- **Why Possibly Novel:** No published matched-budget paradigm comparison exists for dense endpoints with error decomposition.
- **Minimal Experiment:** Train a UNet-free ViT diffusion model and a contrastive ViT on identical 20M images/compute; probe both on segmentation with boundary/interior error decomposition.
- **Main Risk:** Architectural choices favoring one paradigm (ViT suits contrastive) may be impossible to fully neutralize.
- **Cluster:** GEN4SEG

### C-0124 · Super-resolution hallucinations flip downstream segmentation labels
- **One-sentence idea:** Quantify how texture hallucination in modern perceptual SR systematically corrupts downstream segmentation/recognition (inventing plausible-but-wrong material and class evidence), and propose semantic-consistency as a mandatory SR evaluation axis.
- **Problem:** SR is evaluated by PSNR/LPIPS and user studies; its silent injection of false semantic evidence into analysis pipelines is undocumented.
- **Core Hypothesis:** GAN/diffusion SR changes downstream segment labels on a measurable fraction of regions where bicubic upsampling does not, with errors concentrated in material/texture-defined classes, and the flip rate anti-correlates with distortion metrics — perceptual quality trades against semantic fidelity.
- **Why Important:** SR is deployed inside medical, forensic, and mapping pipelines where hallucinated semantics cause real harm; the trade-off needs measurement, not assumption.
- **Why Possibly Novel:** Downstream-semantic-flip metrics for SR are not part of any standard benchmark.
- **Minimal Experiment:** Downsample-then-SR Cityscapes/ADE images through 4 SR models; run a fixed segmenter on originals vs. SR outputs; report label-flip maps and their correlation with SR metric profiles.
- **Main Risk:** Flips may partly reflect segmenter brittleness rather than SR hallucination; needs human adjudication on a subsample.
- **Cluster:** GEN4SEG

### C-0125 · Denoising destroys evidence that recognition models secretly use
- **One-sentence idea:** Test whether image restoration (denoising) removes informative signal — sensor noise correlates with materials, depth, and lighting — such that segmentation on restored images is worse than on raw noisy images for models trained appropriately.
- **Problem:** The clean-image pipeline (restore, then analyze) assumes noise is pure nuisance, an assumption inherited from human viewing that has never been tested for machine consumers.
- **Core Hypothesis:** Models trained on raw noisy images outperform restore-then-segment pipelines at matched noise levels, and the gap grows for material and depth-adjacent classes, showing denoisers destroy task-relevant micro-statistics.
- **Why Important:** Camera-ISP and pipeline design for machine vision (automotive, robotics) currently optimizes for human-referenced restoration that may be counterproductive.
- **Why Possibly Novel:** Raw-vs-restored comparisons exist for detection speed/quality trade-offs, but the evidence-destruction hypothesis with class-resolved analysis is untested.
- **Minimal Experiment:** Train segmenters on (raw-noisy, denoised, clean) versions of a raw-sensor dataset; evaluate all on matched conditions; decompose deltas by class type.
- **Main Risk:** Results depend on noise model realism; synthetic noise may not carry the informative correlations that real sensor noise does.
- **Cluster:** GEN4SEG

### C-0126 · Diffusion data augmentation works by rebalancing, not by new information
- **One-sentence idea:** Show that reported gains from adding diffusion-generated training images to segmentation datasets are mostly reproduced by reweighting/oversampling the real data to the same class-frequency profile the synthetic data induces.
- **Problem:** Synthetic-data papers claim generative models add novel visual information, but generation is prompted toward rare classes, confounding new-information effects with trivial rebalancing.
- **Core Hypothesis:** Matched-frequency real-data reweighting captures the majority of the synthetic-data gain, with the residual concentrated in classes whose real data lacks pose/context diversity — giving a falsifiable rule for when generation truly helps.
- **Why Important:** Prevents expensive generation pipelines where a sampler weight change suffices, and isolates the genuine value-add of generative augmentation.
- **Why Possibly Novel:** Frequency-matched controls are absent from the diffusion-augmentation literature for dense tasks.
- **Minimal Experiment:** Compare {baseline, +synthetic, frequency-matched-resampled real} segmentation training on Cityscapes/ADE with per-class analysis.
- **Main Risk:** Interaction effects (synthetic data enabling stronger augmentation) may complicate the clean decomposition.
- **Cluster:** GEN4SEG

### C-0127 · Generated images are a shortcut detector for recognition models
- **One-sentence idea:** Use human-indistinguishable diffusion-generated images as a diagnostic set: any accuracy drop of a recognition/segmentation model on them (relative to real images of the same content) measures the model's reliance on natural-image statistical shortcuts invisible to humans.
- **Problem:** Shortcut reliance is hard to measure because constructing stimuli that differ only in non-semantic statistics is difficult with natural data.
- **Core Hypothesis:** Models with worse OOD robustness show larger real-vs-generated performance gaps at matched human-verified content fidelity, validating the gap as a cheap shortcut-reliance index.
- **Why Important:** Provides a scalable, label-efficient robustness diagnostic that does not require collecting distribution-shifted real data.
- **Why Possibly Novel:** Generated images are used for augmentation and detection-of-fakes, but not as calibrated instruments for measuring shortcut reliance of understanding models.
- **Minimal Experiment:** Build content-matched real/generated pairs (human-verified), evaluate 10 classifiers/segmenters on both, and correlate the gap with independent robustness scores (ImageNet-C/R).
- **Main Risk:** Residual detectable generation artifacts could make the gap measure artifact-sensitivity rather than shortcut reliance; requires artifact-strength controls.
- **Cluster:** GEN4SEG

### C-0128 · Generative editing enables causal measurement of context reliance in segmentation
- **One-sentence idea:** Use inversion-based object insertion/removal to build counterfactual scene pairs and measure, causally, how much modern segmenters rely on context vs. local evidence per class — replacing correlational context studies.
- **Problem:** Context reliance is measured by occlusion or cropping, which introduce distribution artifacts; clean causal interventions on real scenes were previously impossible.
- **Core Hypothesis:** Context reliance measured via generative counterfactuals differs substantially from occlusion-based estimates, is highly class-structured (small objects depend on context most), and predicts each class's robustness to domain shift.
- **Why Important:** A valid context-reliance measurement underpins debates on whether context use is a feature or a shortcut, with per-class deployment implications.
- **Why Possibly Novel:** Generative counterfactual methodology for dense-prediction context analysis is nascent; the link to shift robustness is untested.
- **Minimal Experiment:** For 20 object classes, create 100 insertion/removal counterfactual pairs each; measure segmentation confidence changes on unedited regions; correlate class context-scores with cross-dataset transfer drops.
- **Main Risk:** Edit artifacts could leak into measurements; requires artifact-only control edits.
- **Cluster:** GEN4SEG

### C-0129 · The leakage laws of attention-supervised synthetic masks
- **One-sentence idea:** Characterize systematically when text-to-image attention maps used to auto-generate image-mask training pairs produce corrupted supervision ("attention leakage" onto associated regions like shadows and reflections), yielding quantitative laws of where free synthetic mask data can be trusted.
- **Problem:** Pipelines that mine diffusion attention for free segmentation labels are proliferating without a characterization of their systematic label noise structure.
- **Core Hypothesis:** Leakage is predictable — it scales with concept co-occurrence strength (dog→leash), attribute status (color words leak globally), and prompt syntax — enabling a leakage-aware filter that improves downstream training more than scale does.
- **Why Important:** Synthetic dense supervision could bypass annotation costs entirely, but only if its noise structure is known and filterable.
- **Why Possibly Novel:** Attention-mask mining exists; its error taxonomy and predictive leakage model do not.
- **Minimal Experiment:** Generate 10K image-mask pairs across controlled prompt structures; human-audit leakage categories; fit leakage predictors; train segmenters on filtered vs. unfiltered sets.
- **Main Risk:** Leakage laws may be model-version-specific, dating quickly as generators evolve.
- **Cluster:** GEN4SEG

### C-0130 · Amodal completion for free from generative inpainting
- **One-sentence idea:** Extract amodal (occlusion-completed) segmentation from off-the-shelf inpainting diffusion models — by inpainting the occluder and reading the revealed object extent — testing whether generative models implicitly learned object completion that discriminative amodal methods must supervise.
- **Problem:** Amodal segmentation requires rare, expensive amodal annotations; whether generative world knowledge already contains completion information is untested.
- **Core Hypothesis:** Occluder-inpainting ensembles produce amodal masks competitive with supervised amodal methods on standard benchmarks, demonstrating that completion knowledge exists in generative priors and needs only extraction, not supervision.
- **Why Important:** Would eliminate a whole annotation category and provide evidence that generative training learns object persistence — a cognitively meaningful capability.
- **Why Possibly Novel:** Inpainting is used for editing; its systematic use and evaluation as a zero-shot amodal segmenter with ensemble uncertainty is new.
- **Minimal Experiment:** On COCO-Amodal, inpaint detected occluders with multiple seeds, segment revealed completions, aggregate into amodal masks; compare against supervised baselines.
- **Main Risk:** Inpainting may hallucinate contextually plausible but wrong completions, requiring uncertainty-aware evaluation.
- **Cluster:** GEN4SEG

### C-0131 · Denoising at fixed noise equals contrastive learning at matched augmentation strength
- **One-sentence idea:** Empirically test a proposed correspondence: features learned by denoising at noise level σ match (in transfer behavior and CKA) features learned contrastively with augmentation strength calibrated to the same information removal, unifying generative and discriminative SSL on one axis.
- **Problem:** Generative and contrastive pretraining are treated as fundamentally different paradigms, blocking transfer of tuning knowledge between them.
- **Core Hypothesis:** There exists a monotone mapping σ↔augmentation-strength under which the two training procedures produce functionally interchangeable representations (stitchable, same transfer profile), implying "paradigm" is a superficial label over a shared information-destruction principle.
- **Why Important:** A validated correspondence would let the field port scaling laws, schedules, and theory across paradigms.
- **Why Possibly Novel:** The information-destruction equivalence has been theorized loosely but never operationalized as a falsifiable matched-training experiment.
- **Minimal Experiment:** Train single-noise-level denoisers at 4 σ values and contrastive models at 4 augmentation strengths on identical data; build the correspondence via transfer-profile matching; test stitchability of matched pairs.
- **Main Risk:** The correspondence may hold for low-level features only, failing at the semantic top — still informative, but less unifying.
- **Cluster:** GEN4SEG

### C-0132 · The VAE, not the UNet, bounds dense quality of latent-diffusion features
- **One-sentence idea:** Show that dense-prediction studies using Stable-Diffusion features inherit a hard resolution/fidelity ceiling from the 8×-downsampling VAE, and that conclusions about "diffusion features" drawn from latent-space models substantially understate pixel-space diffusion capabilities.
- **Problem:** Nearly all diffusion-feature literature uses latent diffusion for cost reasons, silently attributing VAE bottleneck effects to the diffusion paradigm itself.
- **Core Hypothesis:** Matched pixel-space diffusion features beat latent-space features on boundary metrics by a margin that accounts for much of the diffusion-vs-discriminative dense gap reported in prior comparisons.
- **Why Important:** Corrects paradigm-level conclusions built on an infrastructure artifact and quantifies what is lost by the latent shortcut.
- **Why Possibly Novel:** Latent-vs-pixel feature comparisons for dense understanding endpoints are missing because pixel-space models are rarely probed.
- **Minimal Experiment:** Probe matched-size pixel-space and latent-space diffusion models (trained on same data) on segmentation with boundary-resolved metrics; additionally probe VAE-encoder features alone as the bottleneck control.
- **Main Risk:** Public matched model pairs are scarce; may require training small diffusion models from scratch.
- **Cluster:** GEN4SEG

### C-0133 · Perceptual SR wins human ratings while corrupting machine consumers
- **One-sentence idea:** Establish an inverse relationship between SR perceptual quality (human preference) and machine-task fidelity (detection/segmentation accuracy on SR outputs), showing the field's optimization target actively harms the growing machine-consumer use case.
- **Problem:** SR progress is measured by human preference, while an increasing share of SR outputs are consumed by downstream models — two objectives whose alignment is assumed.
- **Core Hypothesis:** Across the distortion-perception frontier, machine-task accuracy peaks near the distortion end, and recent perception-optimized models sit measurably below older "worse" methods for machine consumption — a quantified misalignment.
- **Why Important:** Argues for task-conditional SR standards and warns against deploying perception-optimized enhancement inside analysis pipelines.
- **Why Possibly Novel:** The distortion-perception trade-off is theorized; its systematic mapping onto downstream machine-task performance across modern SR models is not.
- **Minimal Experiment:** Evaluate 8 SR models spanning the frontier on downstream COCO detection and ADE segmentation of SR-processed inputs; plot machine accuracy against human-preference scores.
- **Main Risk:** Downstream models trained with SR-processed data could adapt, so conclusions must specify the (common) mismatched-training deployment case.
- **Cluster:** GEN4SEG

### C-0134 · Diffusion-classifier robustness is bought with test-time compute
- **One-sentence idea:** Test whether the reported adversarial/OOD robustness of diffusion-based zero-shot classifiers reflects the generative paradigm or simply their orders-of-magnitude larger test-time compute, by giving discriminative models matched inference-compute via ensembling and test-time augmentation.
- **Problem:** Diffusion classifiers evaluate hundreds of denoising queries per decision, but robustness comparisons against single-forward-pass discriminative models are framed as paradigm differences.
- **Core Hypothesis:** Compute-matched discriminative ensembles (TTA + multi-crop + model soup sampling) close most of the robustness gap, leaving a small residual attributable to the likelihood-based decision rule.
- **Why Important:** Attribution determines whether robustness research should pursue generative classification or just spend inference compute better.
- **Why Possibly Novel:** Compute-matched robustness accounting between paradigms has not been performed.
- **Minimal Experiment:** Match total FLOPs per decision between a diffusion classifier and TTA-ensembled discriminative baselines; evaluate on adversarial and corruption suites.
- **Main Risk:** "Matched compute" has multiple defensible definitions (FLOPs, latency, queries); report several.
- **Cluster:** GEN4SEG

### C-0135 · Model collapse hits dense structure before class statistics
- **One-sentence idea:** Characterize self-consuming training loops (models trained on model-generated images) for dense tasks, hypothesizing that spatial/boundary fidelity degrades generations earlier than class-frequency statistics, so segmentation canaries detect collapse before classification metrics move.
- **Problem:** Model-collapse studies track distributional and classification metrics; the dense/structural dimension of collapse — most relevant for scene understanding data pipelines — is uncharacterized.
- **Core Hypothesis:** Across synthetic-data generations, boundary complexity and object-layout diversity decay measurably faster than class marginals, making dense statistics the sensitive early-warning instrument for data-pipeline contamination.
- **Why Important:** As web data fills with generated images, dense-task training is the first casualty to detect and mitigate; collapse monitoring needs the right instruments.
- **Why Possibly Novel:** Generation-wise dense-structure decay curves have not been measured; collapse work is classification/distribution-centric.
- **Minimal Experiment:** Iterate a small T2I model 5 generations on its own outputs; per generation, train a segmenter on generated data and measure boundary/layout statistics plus downstream mIoU.
- **Main Risk:** Small-model collapse dynamics may differ from frontier-scale dynamics, limiting extrapolation.
- **Cluster:** GEN4SEG

### C-0136 · Restoration-model disagreement is a free OOD and uncertainty signal
- **One-sentence idea:** Use the disagreement among independent blind restoration models (or one model under seed resampling) as a zero-training uncertainty map for downstream segmentation — regions where restoration is ambiguous are exactly where semantic predictions should not be trusted.
- **Problem:** Segmentation uncertainty estimation requires ensembles or specialized training; a task-independent, plug-in ambiguity signal derived from generative priors is unexplored.
- **Core Hypothesis:** Pixelwise restoration variance correlates with segmentation error location better than the segmenter's own softmax entropy, especially under distribution shift where softmax confidence is miscalibrated.
- **Why Important:** A model-agnostic uncertainty side-channel would improve safety of deployed dense prediction without touching the task model.
- **Why Possibly Novel:** Restoration ensembles as uncertainty oracles for *other* tasks is an unexploited connection between communities.
- **Minimal Experiment:** On corrupted ADE/Cityscapes, compute restoration-variance maps and segmenter softmax entropy; compare both as predictors of pixel error (sparsification plots).
- **Main Risk:** Restoration variance may track texture complexity rather than semantic ambiguity, inflating false alarms in benign textured regions.
- **Cluster:** GEN4SEG

### C-0137 · Concept tokens from five images rival few-shot segmentation methods
- **One-sentence idea:** Test whether personalization techniques (textual inversion / DreamBooth) that learn a concept token from ~5 images provide, via cross-attention readout, a few-shot segmentation mechanism competitive with purpose-built few-shot discriminative methods.
- **Problem:** Few-shot segmentation research builds specialized meta-learning architectures, while generative personalization — solving an adjacent inverse problem — has never been benchmarked as a segmenter.
- **Core Hypothesis:** Attention maps of learned concept tokens segment novel concepts at accuracy comparable to specialized few-shot methods, but with different failure modes (better on distinctive textures, worse on shape-defined concepts) — revealing what personalization actually learns.
- **Why Important:** A competitive result would unify two research lines and clarify whether generative inversion captures localized concept extent or only global style.
- **Why Possibly Novel:** Personalization-as-segmentation has anecdotal demos but no controlled comparison against few-shot segmentation baselines on standard splits.
- **Minimal Experiment:** On PASCAL-5i style splits, learn concept tokens per novel class from support sets; extract attention masks on queries; compare against two few-shot segmentation baselines.
- **Main Risk:** Personalization needs minutes of optimization per concept, making the comparison contested on efficiency grounds.
- **Cluster:** GEN4SEG

### C-0138 · Harmonized copy-paste generalizes better despite lower benchmark scores
- **One-sentence idea:** Test whether diffusion-harmonized copy-paste augmentation (removing lighting/boundary inconsistencies) produces segmenters that score *lower* on the training-distribution benchmark but generalize better across datasets, because vanilla copy-paste teaches an exploitable paste-artifact cue.
- **Problem:** Copy-paste's benchmark gains are assumed to reflect better object learning, but models may partly learn to use paste artifacts as segmentation cues — inflating ID scores and harming transfer.
- **Core Hypothesis:** Artifact-probe tests show vanilla-copy-paste models respond to boundary inconsistencies as objectness cues; harmonization removes the shortcut, trading ID benchmark points for cross-dataset gains.
- **Why Important:** Copy-paste is a default augmentation; knowing it installs a shortcut would change augmentation practice and benchmark interpretation.
- **Why Possibly Novel:** The shortcut hypothesis for copy-paste and the ID/OOD trade-off test have not been examined.
- **Minimal Experiment:** Train instance segmenters with {no CP, vanilla CP, harmonized CP}; evaluate ID (COCO) and transfer (LVIS, Objects365 subsets); probe sensitivity to synthetic paste artifacts.
- **Main Risk:** Harmonization may also blur useful boundary supervision, confounding the shortcut explanation with label-quality effects.
- **Cluster:** GEN4SEG

### C-0139 · Generation frequency audits dataset bias quantitatively
- **One-sentence idea:** Validate text-to-image generation frequency (how often unprompted attributes appear) as a calibrated instrument for auditing the training corpus's conditional biases, turning generators into measurement devices for dataset bias that annotation audits cannot scale to.
- **Problem:** Dataset bias auditing requires expensive annotation of the corpus; generative models have absorbed corpus statistics but are not validated as quantitative bias readouts.
- **Core Hypothesis:** For attributes with known corpus statistics (measurable on a labeled subset), unconditional-generation frequencies recover the corpus conditionals with predictable distortion (mode amplification following a measurable law), enabling corrected bias estimates for unmeasurable attributes.
- **Why Important:** Scalable bias metrology matters for both fairness auditing and for understanding what segmentation/recognition models trained on such corpora inherit.
- **Why Possibly Novel:** Generation-based bias probing exists qualitatively; the calibration against ground-truth corpus statistics and the amplification law are missing.
- **Minimal Experiment:** Train a mid-size T2I model on a corpus with fully annotated attributes; compare generation frequencies to corpus conditionals across prompts; fit and validate the amplification law.
- **Main Risk:** Amplification may be attribute-specific and non-transferable, breaking calibrated correction.
- **Cluster:** GEN4SEG

### C-0140 · When does segmentation knowledge emerge inside diffusion training?
- **One-sentence idea:** Track the emergence of segmentation-usable structure across diffusion pretraining checkpoints, testing whether dense semantic knowledge appears early (with generation quality irrelevant) — implying cheap, short-trained diffusion models suffice as dense feature extractors.
- **Problem:** Diffusion feature extraction uses fully trained expensive checkpoints under the assumption that generation quality and representation quality track each other.
- **Core Hypothesis:** Segmentation probe quality of diffusion features saturates within the first small fraction of training, long before FID meaningfully improves, decoupling representation learning from generative fidelity.
- **Why Important:** If confirmed, dense-representation users can train (or select) drastically cheaper diffusion models, and the result informs what long diffusion training actually optimizes.
- **Why Possibly Novel:** Checkpoint-wise developmental probing of diffusion models for dense endpoints is not published.
- **Minimal Experiment:** Save 10 checkpoints across a small diffusion training run; probe each for segmentation on VOC/ADE; overlay probe curves with FID curves.
- **Main Risk:** Small-model dynamics may not represent frontier models where late training could reorganize features.
- **Cluster:** GEN4SEG

### C-0141 · Adversarial training pressure gives GAN features better boundaries than diffusion
- **One-sentence idea:** Make the contrarian case that GAN discriminator/generator features carry sharper boundary information than diffusion features at matched scale, because adversarial objectives concentrate model capacity on exactly the high-frequency structure that likelihood-weighted diffusion training downweights.
- **Problem:** The field abandoned GAN representations wholesale when diffusion won generation quality, without checking whether the adversarial objective retains advantages for specific understanding endpoints.
- **Core Hypothesis:** At matched data/compute, GAN-derived features beat diffusion-derived features on boundary F-score and edge-sensitive tasks while losing on semantic region classification — objective-specific division of labor, not overall superiority.
- **Why Important:** Recovers potentially discarded value and sharpens the theory of what different generative objectives encode.
- **Why Possibly Novel:** Post-diffusion-era controlled GAN-vs-diffusion feature comparisons for dense understanding do not exist.
- **Minimal Experiment:** Train StyleGAN-class and DDPM-class models on identical data; probe discriminator, generator, and UNet features for segmentation with boundary-resolved metrics.
- **Main Risk:** GAN training instability at matched budgets may produce weak models, confounding objective with optimization success.
- **Cluster:** GEN4SEG

### C-0142 · Text conditioning contributes little to diffusion features for segmentation
- **One-sentence idea:** Test whether unconditional diffusion models yield dense features nearly as good as text-conditioned ones, challenging the assumption that language conditioning is what organizes diffusion representations semantically.
- **Problem:** Diffusion-feature papers use text-conditioned models and often credit language for their semantic structure, without unconditional controls at matched data/compute.
- **Core Hypothesis:** The segmentation-relevant structure of diffusion features arises from the denoising task itself (objects are units of joint appearance statistics), with text conditioning adding mainly class-name alignment rather than better spatial-semantic organization.
- **Why Important:** Determines whether caption data is necessary for dense-quality generative pretraining — a major data-cost question.
- **Why Possibly Novel:** Conditional-vs-unconditional feature quality comparisons for dense endpoints at matched budgets are absent.
- **Minimal Experiment:** Train matched conditional/unconditional diffusion models on the same images; probe segmentation (category-agnostic and semantic); measure the gap per endpoint type.
- **Main Risk:** Classifier-free-guidance training tricks entangle conditioning with optimization; requires careful recipe matching.
- **Cluster:** GEN4SEG

### C-0143 · Denoising trajectories encode metric depth without depth supervision
- **One-sentence idea:** Extract and quantify implicit 3D/depth knowledge in image diffusion models by analyzing how denoising trajectories treat geometry (e.g., disocclusion behavior, perspective-consistent completion), testing whether generative pretraining learns usable depth without any 3D labels.
- **Problem:** Whether 2D generative training induces genuine geometric representations — a core question about what generation teaches — remains anecdotal, argued from cherry-picked samples.
- **Core Hypothesis:** Simple probes on diffusion features (linear depth probes; occlusion-order readouts from inpainting behavior) recover relative depth competitive with self-supervised depth baselines, and the geometric information concentrates at specific noise levels.
- **Why Important:** Establishes generative pretraining as a source of geometric supervision for segmentation/scene understanding, or refutes a widely repeated claim.
- **Why Possibly Novel:** Systematic geometric probing of diffusion representations with quantitative depth benchmarks (not demos) is largely missing.
- **Minimal Experiment:** Linear-probe NYUv2 relative depth from SD features across timesteps; compare against DINOv2 probes and self-supervised depth methods.
- **Main Risk:** Depth probes may exploit 2D cues (position, size) rather than learned geometry, requiring cue-controlled evaluation sets.
- **Cluster:** GEN4SEG

### C-0144 · Train on degraded images instead of restoring test images
- **One-sentence idea:** Challenge the restore-then-analyze deployment pattern by showing that training segmenters directly on realistically degraded (compressed, low-light) images beats pipelines that restore inputs at test time, across matched degradation severities.
- **Problem:** Production systems insert restoration modules before analysis models trained on clean data, assuming restoration moves inputs into the training distribution better than retraining moves the model.
- **Core Hypothesis:** Degradation-native training dominates restoration pipelines everywhere except extreme degradations, because restoration introduces its own distribution shift (restoration artifacts) that clean-trained models have never seen.
- **Why Important:** A clear decision rule (retrain vs. restore) with measured crossover points would rationalize a ubiquitous engineering choice currently made by default.
- **Why Possibly Novel:** Head-to-head retrain-vs-restore comparisons with severity-resolved crossover analysis are not systematically published.
- **Minimal Experiment:** On Cityscapes with controlled JPEG/low-light degradations, compare {clean-trained, clean-trained+restoration, degradation-trained} segmenters across severities.
- **Main Risk:** Conclusions depend on restoration model quality; needs current-generation restorers to be fair.
- **Cluster:** GEN4SEG

### C-0145 · "SR helps small-object detection" is resolution mismatch in disguise
- **One-sentence idea:** Test whether reported gains from super-resolving inputs for small-object detection vanish when the detector is simply trained and run at the matched effective resolution, exposing SR as an expensive resampling operator in this role.
- **Problem:** SR-for-detection papers compare SR-enhanced inputs against low-resolution baselines with detectors trained at mismatched scales, confounding SR's generative contribution with trivial resolution alignment.
- **Core Hypothesis:** A detector trained natively at the SR output resolution on bicubic-upsampled data matches the SR pipeline's accuracy, showing learned hallucination adds nothing over resampling plus appropriate training.
- **Why Important:** Removes a costly component from small-object pipelines and corrects a persistent attribution error in applied literature.
- **Why Possibly Novel:** Resolution-matched training controls are consistently absent from SR-for-detection studies.
- **Minimal Experiment:** On VisDrone/small-COCO subsets, compare {LR-trained on LR, SR pipeline, bicubic-up + matched-resolution-trained} detectors at equal inference cost accounting.
- **Main Risk:** For extreme upscaling factors, SR may genuinely help; the claim needs a factor-resolved boundary.
- **Cluster:** GEN4SEG

### C-0146 · Inpainted regions reveal how much context segmenters consume
- **One-sentence idea:** Use inpainting to replace object interiors with context-consistent but object-inconsistent content, measuring per-class how much segmentation decisions are driven by surrounding context rather than object appearance — a clean instrument for the context-shortcut question.
- **Problem:** Whether segmenters label pixels from local evidence or contextual priors is central to robustness but hard to measure without unnatural occluders.
- **Core Hypothesis:** For many classes (especially small and habitual-location objects), segmenters maintain confident original-class predictions on fully content-replaced interiors, quantifying a context-override rate that predicts hallucinated segments under domain shift.
- **Why Important:** Context-override rates give a per-class safety profile for deployment and a target for training interventions.
- **Why Possibly Novel:** Content-replacement (rather than deletion) as a context-measurement instrument for dense predictions is methodologically new.
- **Minimal Experiment:** Inpaint 50 instances per class in COCO with neutral content; measure persistence of original-class pixel predictions across 4 segmenters; correlate with cross-domain error patterns.
- **Main Risk:** Inpainting may leave low-level traces of the original object; requires trace-detection controls.
- **Cluster:** GEN4SEG

### C-0147 · Diffusion features encode parts; discriminative features encode instances
- **One-sentence idea:** Test the hypothesis that generative (diffusion) features excel at part-level correspondence while discriminative SSL features excel at instance-level discrimination — a principled division predicting which paradigm serves which dense task.
- **Problem:** Diffusion-vs-DINO feature comparisons produce mixed results across papers because tasks mix part- and instance-level demands uncontrolledly.
- **Core Hypothesis:** On decomposed benchmarks, diffusion features win semantic part matching (same part across instances) and lose instance matching (same instance across views), because generation requires compositional part structure while discrimination requires instance identity — an objective-driven dissociation stable across scales.
- **Why Important:** Converts noisy paradigm debates into a predictive task-to-paradigm mapping and motivates targeted feature fusion.
- **Why Possibly Novel:** The part/instance dissociation framing with matched-budget tests is absent from feature-comparison literature.
- **Minimal Experiment:** Evaluate SD and DINOv2 features on SPair-71k part correspondence vs. instance re-identification/multi-view matching at matched extraction cost.
- **Main Risk:** Public models differ in data/scale; a fully controlled version needs matched pretraining, raising cost.
- **Cluster:** GEN4SEG

### C-0148 · A mode-coverage statistic predicts when synthetic data helps
- **One-sentence idea:** Develop and validate a falsifiable decision rule: generative augmentation improves a segmentation task if and only if a measurable mode-coverage gap exists between the real training set and the target distribution that the generator demonstrably covers.
- **Problem:** Synthetic-data results are inconsistent across studies, and the field lacks any predictive criterion for when generation will help, leading to costly trial-and-error.
- **Core Hypothesis:** A coverage statistic (target-domain samples' likelihood under densities fitted to real-train vs. real-train+synthetic embeddings) predicts the sign and rough magnitude of synthetic-data gains across tasks and datasets.
- **Why Important:** Replaces anecdote with an actionable pre-training diagnostic, saving generation and training compute across the industry.
- **Why Possibly Novel:** Predictive (rather than post-hoc) criteria for synthetic-data utility with cross-task validation have not been established.
- **Minimal Experiment:** Across 8 task/dataset configurations with known synthetic-data outcomes, compute the coverage statistic and test its prediction accuracy; preregister thresholds and validate on 4 new configurations.
- **Main Risk:** A single statistic may not transfer across task types; may need task-family-specific calibration.
- **Cluster:** GEN4SEG

### C-0149 · Layout diversity, not photorealism, is what synthetic training data needs
- **One-sentence idea:** Show that heavily stylized (non-photorealistic) generated scenes train segmentation models as well as photorealistic ones at matched layout/annotation diversity, refuting the assumption that closing the realism gap is the key to synthetic data utility.
- **Problem:** Synthetic-data pipelines spend heavily on photorealism (rendering quality, diffusion realism) under the untested belief that realism gap = domain gap.
- **Core Hypothesis:** Segmentation transfer from synthetic to real depends primarily on scene-layout and object-configuration diversity; style-transferred or cartoon-shaded versions of the same layouts lose almost no transfer performance.
- **Why Important:** Would redirect synthetic-data investment from expensive realism to cheap layout diversity, changing pipeline economics.
- **Why Possibly Novel:** Realism-vs-layout factorial designs are missing; existing domain-gap studies confound the two axes.
- **Minimal Experiment:** Generate matched-layout scene sets at 3 realism levels (photoreal, stylized, flat-shaded); train segmenters on each; evaluate real-data transfer on Cityscapes/ADE.
- **Main Risk:** Extremely unrealistic styles may break pretrained-backbone priors, requiring from-scratch and pretrained arms.
- **Cluster:** GEN4SEG

### C-0150 · Tracking emerges inside video diffusion attention
- **One-sentence idea:** Test whether video generation models implicitly solve temporal correspondence — readable as object tracking from their spatiotemporal attention — providing supervision-free tracking/video-segmentation and evidence that generation learns object permanence.
- **Problem:** Video understanding trains correspondence explicitly at high annotation cost, while video generators must implicitly bind objects across frames to generate coherently — an untapped, unmeasured capability.
- **Core Hypothesis:** Attention-derived correspondences from a video diffusion model achieve competitive label-propagation scores (video object segmentation) without any tracking supervision, and correspondence quality scales with the generator's temporal coherence metrics.
- **Why Important:** Would establish video generative pretraining as a correspondence teacher and link generation quality to a measurable understanding capability.
- **Why Possibly Novel:** Extracting and quantitatively benchmarking tracking from video diffusion internals (vs. using generation for augmentation) is largely unexplored.
- **Minimal Experiment:** Extract cross-frame attention/feature matches from an open video diffusion model; evaluate on DAVIS label propagation against self-supervised tracking baselines.
- **Main Risk:** Attention may bind by appearance rather than identity, failing on similar-instance scenes — itself an informative failure to characterize.
- **Cluster:** GEN4SEG
## Sub-cluster LLM-ANNOT — LLM/VLM Agents for Annotation (C-0151 – C-0180)

### C-0151 · Does LLM annotator disagreement mirror human ambiguity?
- **One-sentence idea:** Test whether disagreement among LLM/VLM annotators concentrates on the same items where humans disagree — i.e., whether machine disagreement is a valid measurement of intrinsic label ambiguity or a different phenomenon entirely.
- **Problem:** LLM ensembles are proposed as replacements for human annotation committees, implicitly assuming their disagreement structure carries the same meaning as human disagreement.
- **Core Hypothesis:** Item-level disagreement correlation between VLM ensembles and human committees is only moderate, with machines disagreeing on prior-conflicting items and humans on genuinely ambiguous ones — two separable ambiguity types with different downstream uses.
- **Why Important:** Ambiguity-aware training and evaluation increasingly rely on disagreement signals; using the wrong disagreement source corrupts both.
- **Why Possibly Novel:** Direct item-matched comparisons of machine vs. human disagreement structure on vision datasets are missing.
- **Minimal Experiment:** On datasets with released per-annotator human labels (e.g., CIFAR-10H-style resources), collect labels from 8 diverse VLMs; compare item-level disagreement correlations and error-type taxonomies.
- **Main Risk:** Model diversity may be too low (shared pretraining data) to produce meaningful machine disagreement at all — itself a publishable finding.
- **Cluster:** LLM-ANNOT

### C-0152 · Self-consistency overestimates annotation reliability by correlated errors
- **One-sentence idea:** Quantify how much repeated sampling of the same VLM ("self-consistency") inflates apparent annotation confidence because same-model errors are strongly correlated, and derive a corrected confidence estimator from cross-model agreement.
- **Problem:** Annotation pipelines use sample agreement as a quality gate, treating repeated model samples as independent votes, which they are not.
- **Core Hypothesis:** Same-model agreement at high temperature massively underestimates error rates on prior-driven mistakes (agreeing confidently on wrong labels), whereas small cross-family ensembles restore calibration — with a measurable "effective vote count" for self-samples far below the nominal count.
- **Why Important:** Confidence gates decide which labels enter datasets; miscalibrated gates systematically admit correlated errors that poison training.
- **Why Possibly Novel:** Correlated-error accounting with effective-sample-size corrections for LLM annotation has not been formalized.
- **Minimal Experiment:** Annotate 5K images with 10 self-samples vs. 5 cross-family models; compare agreement-conditioned error rates against ground truth; fit the effective vote count.
- **Main Risk:** Cross-family models may share pretraining corpora enough to correlate errors too, reducing the fix's headroom.
- **Cluster:** LLM-ANNOT

### C-0153 · Do annotation-hardness predictors transfer across tasks?
- **One-sentence idea:** Test whether the "hardness" signal used to route annotation cascades (cheap model first, escalate hard items) is a task-general property of images or task-specific, determining whether routing models can be trained once and reused.
- **Problem:** Cascade annotation systems retrain routing per task, an expensive practice justified only if hardness is task-idiosyncratic — an unexamined question with direct cost implications.
- **Core Hypothesis:** A shared "annotation hardness" factor (clutter, ambiguity, atypicality) explains most routing value across classification, detection, and captioning annotation, so a single frozen hardness scorer loses little versus per-task routers.
- **Why Important:** A universal hardness scorer would make cascade annotation plug-and-play and reveal a structural property of visual data.
- **Why Possibly Novel:** Cross-task transfer of annotation-difficulty predictors has not been measured; difficulty research is task-siloed.
- **Minimal Experiment:** Train hardness predictors (from cheap-model disagreement) on 3 annotation tasks; evaluate routing value matrices across all task pairs; factor-analyze the difficulty structure.
- **Main Risk:** Hardness may decompose into a general factor plus large task-specific components, giving a mixed answer.
- **Cluster:** LLM-ANNOT

### C-0154 · Ground truth becomes a function of the annotating model's prompt
- **One-sentence idea:** Demonstrate that optimizing annotation-guideline prompts for LLM annotators shifts the resulting label distributions in ways that materially change trained-model behavior — making "ground truth" an artifact of prompt engineering choices that are never reported.
- **Problem:** Dataset papers report annotator instructions for humans, but LLM-annotation pipelines tune prompts for throughput/agreement without documenting how prompt variants change the labels themselves.
- **Core Hypothesis:** Reasonable guideline paraphrases produce label distributions differing by several percent on boundary cases, and models trained on different-prompt versions of the "same" dataset show benchmark differences comparable to method-level improvements.
- **Why Important:** Reproducibility and comparability of LLM-annotated datasets require prompt-sensitivity reporting; the field currently lacks even an estimate of the effect size.
- **Why Possibly Novel:** Prompt sensitivity is studied for model evaluation, not for its propagation through annotation into downstream trained models.
- **Minimal Experiment:** Annotate one dataset with 5 semantically equivalent guideline prompts; train identical models on each version; measure label divergence and downstream benchmark spread.
- **Main Risk:** Effects may concentrate in a small boundary-case subset, requiring careful stratified analysis to detect.
- **Cluster:** LLM-ANNOT

### C-0155 · VLM-generated masks carry a systematic boundary bias that trained models inherit
- **One-sentence idea:** Characterize the geometric error structure of VLM/foundation-model-generated segmentation masks (systematic dilation/erosion, corner rounding) and show that models trained on such labels inherit measurable, correctable boundary offsets.
- **Problem:** Auto-generated dense labels are consumed as if their errors were unbiased noise, but mask-generation pipelines plausibly have consistent geometric biases that supervised training will absorb.
- **Core Hypothesis:** Auto-labels exhibit a stable signed boundary offset (e.g., systematic over-segmentation of a few pixels, class-dependent), student models reproduce this bias on clean test data, and a post-hoc morphological calibration of labels removes most of the inherited error.
- **Why Important:** As auto-labeling replaces human masks at scale, uncharacterized systematic biases become permanent features of the ecosystem's models.
- **Why Possibly Novel:** Bias (vs. noise) decomposition of auto-generated dense labels and its inheritance analysis are unreported.
- **Minimal Experiment:** Compare auto-labels against high-quality human masks on a calibration set; fit per-class signed offset models; train students on raw vs. calibrated auto-labels; measure inherited offsets.
- **Main Risk:** Bias may vary with image content in ways too complex for simple calibration, weakening the corrective payoff.
- **Cluster:** LLM-ANNOT

### C-0156 · Verification-only agents beat generation-plus-filtering at matched cost
- **One-sentence idea:** Exploit the generation-verification asymmetry by designing annotation pipelines where LLM agents only verify or choose among candidate labels (produced by cheap specialized models), testing whether verify-only pipelines dominate generate-then-filter at equal compute.
- **Problem:** LLM annotation pipelines default to having the LLM produce labels, though verification is plausibly both easier and better calibrated for these models — an untested architectural choice.
- **Core Hypothesis:** At matched cost, [cheap proposer + LLM verifier] yields higher-quality labels than [LLM generator + self-filter], with the advantage growing for structured outputs (boxes, masks, relations) where generation is hardest.
- **Why Important:** A validated division of labor would restructure annotation economics and clarify what LLMs are actually good for in labeling systems.
- **Why Possibly Novel:** The proposer/verifier decomposition is used in reasoning research but has not been evaluated as an annotation architecture with cost accounting.
- **Minimal Experiment:** Build both pipelines for detection annotation on a labeled evaluation set; sweep compute budgets; compare label quality curves.
- **Main Risk:** Verifier acceptance bias (rubber-stamping plausible candidates) may cap verification quality below expectations.
- **Cluster:** LLM-ANNOT

### C-0157 · Rationales don't make labels better — they make errors findable
- **One-sentence idea:** Test the claim that requiring chain-of-thought rationales improves LLM annotation accuracy, hypothesizing instead that rationales leave accuracy unchanged but make erroneous labels much easier to detect post-hoc (by humans or auditor models).
- **Problem:** Rationale generation doubles annotation cost, justified by an accuracy assumption that has not been isolated from its auditability benefit.
- **Core Hypothesis:** Rationale-conditioned labels match direct labels in accuracy, but error-detection AUC from rationale features (contradictions, hedging, unsupported claims) substantially exceeds detection from labels alone — rationales are audit trails, not accuracy boosters.
- **Why Important:** Changes the economic case for rationales: pay for them where audit matters (safety-critical datasets), skip them elsewhere.
- **Why Possibly Novel:** The accuracy/auditability decomposition of annotation rationales has not been experimentally separated.
- **Minimal Experiment:** Annotate a ground-truthed set with and without rationales; compare label accuracy; train error detectors on rationale text; compare detection performance across conditions.
- **Main Risk:** Rationales may causally change labels for specific hard categories, making the null accuracy result category-dependent.
- **Cluster:** LLM-ANNOT

### C-0158 · Uncertainty sampling poisons active learning when the LLM is the annotator
- **One-sentence idea:** Show that classic active learning breaks under LLM annotation because uncertainty-based acquisition preferentially selects exactly the items where LLM labels are least reliable, creating a feedback loop that concentrates label noise where the student is most sensitive.
- **Problem:** Active learning theory assumes oracle labels; pipelines now pair acquisition functions with fallible LLM annotators without re-deriving what acquisition should optimize.
- **Core Hypothesis:** Student-uncertainty sampling with LLM labels underperforms random sampling in final accuracy under realistic annotator error, and acquisition functions that jointly model informativeness and annotator reliability restore the advantage.
- **Why Important:** Active learning + LLM annotation is a default modern pipeline; if the combination is toxic, much applied practice is silently suboptimal.
- **Why Possibly Novel:** The interaction between acquisition strategy and structured (non-random) annotator error is unstudied.
- **Minimal Experiment:** Simulate and run real AL loops (random vs. uncertainty vs. reliability-aware) with a VLM annotator on a ground-truthed pool; compare student learning curves.
- **Main Risk:** Effect size depends on annotator error structure; needs several annotator models to establish generality.
- **Cluster:** LLM-ANNOT

### C-0159 · Noisy-label theory fails on LLM-generated labels
- **One-sentence idea:** Demonstrate that established noisy-label learning methods, built for (conditionally) independent human noise, systematically fail on LLM-annotated data whose errors are confident, correlated, and prior-structured — and characterize the new noise model needed.
- **Problem:** Practitioners apply noisy-label toolboxes (loss correction, co-teaching, confidence filtering) to LLM labels, assuming the noise assumptions transfer from the human-noise literature.
- **Core Hypothesis:** LLM label noise concentrates in low-entropy, high-confidence clusters (systematic bias) that confidence-based filtering cannot detect and loss-correction matrices misestimate, so classical methods underperform even simple bias-aware baselines calibrated on small clean sets.
- **Why Important:** The dominant future noise source is machine annotation; the field's noise-robustness toolkit may be built for the wrong noise.
- **Why Possibly Novel:** A systematic stress-test of the noisy-label literature under measured LLM-noise statistics has not been performed.
- **Minimal Experiment:** Create parallel corpora with human-noise and LLM-noise at matched rates; run 6 noisy-label methods on both; analyze failure modes against noise structure statistics.
- **Main Risk:** Some modern methods may be incidentally robust, requiring nuanced per-method conclusions rather than a clean headline.
- **Cluster:** LLM-ANNOT

### C-0160 · Circular gains from shared pretraining between annotator and student
- **One-sentence idea:** Measure the contamination effect when the same foundation model family both annotates a dataset and is fine-tuned on it, testing whether apparent quality gains are partially circular (the student is rewarded for reproducing its own priors, not for learning the task).
- **Problem:** The dominant pipeline — frontier model annotates, related models train — has an unexamined circularity: evaluation on similarly-annotated splits cannot distinguish task learning from prior amplification.
- **Core Hypothesis:** Students fine-tuned on same-family annotations outperform on same-family-annotated test sets but underperform on human-annotated test sets, relative to students trained on cross-family annotations — a measurable circularity gap.
- **Why Important:** Quantifies a structural validity threat in the modern data ecosystem and motivates cross-family annotation as methodological hygiene.
- **Why Possibly Novel:** Annotator-student family confounding has been raised for LLM-as-judge, but not measured through the full annotate-train-evaluate loop in vision.
- **Minimal Experiment:** Annotate a dataset with two model families; train students of both families on each; evaluate all four cells on human-labeled gold data; test the interaction term.
- **Main Risk:** Family differences in annotation quality (not circularity) could explain results; needs quality-matched annotation subsets.
- **Cluster:** LLM-ANNOT

### C-0161 · The error taxonomy of VLM attribute annotation is a map of language priors
- **One-sentence idea:** Build a systematic taxonomy of VLM annotation errors on objective visual attributes (color, count, material, orientation) and show errors are predictable from language co-occurrence statistics — enabling prior-corrected annotation without any visual improvement.
- **Problem:** Attribute annotation errors are treated as random capability limits, though many plausibly reproduce text-corpus regularities (bananas are yellow) that can be modeled and subtracted.
- **Core Hypothesis:** A text-only co-occurrence model predicts VLM attribute-annotation error direction significantly above chance, and importance-reweighting annotations against this prior improves dataset accuracy at zero visual-model cost.
- **Why Important:** Cheap, principled correction of the largest systematic error source in machine attribute labeling, plus a quantitative window into prior-vs-perception arbitration.
- **Why Possibly Novel:** Using language-prior models as explicit error predictors and correction terms for visual annotation is unexplored.
- **Minimal Experiment:** Annotate a controlled attribute dataset (rendered objects with known properties) with 3 VLMs; fit error predictors from caption-corpus statistics; validate prior-corrected labels.
- **Main Risk:** Prior and perception errors may interact nonlinearly, limiting subtractive correction.
- **Cluster:** LLM-ANNOT

### C-0162 · Multi-agent debate helps annotation only when errors anti-correlate
- **One-sentence idea:** Establish the precise condition under which debate/discussion between VLM annotators improves label quality — predicted to be error anti-correlation between agents — and show that same-family debate (the common setup) fails this condition and can amplify shared errors.
- **Problem:** Debate protocols are adopted for annotation on intuition; when they help, hurt, or do nothing is unquantified, and failures are invisible without ground truth.
- **Core Hypothesis:** Debate gain over independent voting is a monotone function of pairwise error decorrelation; same-model debate produces confident convergence to shared priors (negative gain on prior-conflicting items), while cross-family debate with enforced perspective diversity yields positive gain.
- **Why Important:** Converts debate from ritual to engineering: measure decorrelation first, deploy debate only where the condition holds.
- **Why Possibly Novel:** The decorrelation condition, though intuitive, has not been formulated and tested as a quantitative predictor for annotation debate.
- **Minimal Experiment:** Run debate vs. voting across agent-pair combinations with measured error correlations on a ground-truthed set; regress debate gain on decorrelation.
- **Main Risk:** Debate dynamics (persuasiveness ≠ correctness) may add variance that obscures the clean correlation prediction.
- **Cluster:** LLM-ANNOT

### C-0163 · Silent API model updates fracture dataset consistency
- **One-sentence idea:** Quantify how mid-annotation updates of commercial LLM/VLM APIs shift label distributions within a single dataset, and measure the downstream effect of such invisible temporal seams on trained models and benchmark comparisons.
- **Problem:** Long-running annotation jobs span silent model-version changes; datasets carry undocumented internal distribution shifts that no one measures or controls for.
- **Core Hypothesis:** Version seams produce detectable label-distribution discontinuities (findable by change-point detection on label statistics), and models trained on pre/post-seam halves differ on benchmarks by margins comparable to claimed method improvements.
- **Why Important:** Establishes versioning discipline as a validity requirement for machine-annotated datasets and provides seam-detection tools for auditing existing ones.
- **Why Possibly Novel:** Temporal instability of annotation infrastructure as a dataset-validity threat is undocumented empirically.
- **Minimal Experiment:** Re-annotate a fixed image set weekly via the same API endpoint for months; measure label drift; simulate seam effects by training on temporally split annotations.
- **Main Risk:** Providers may not update during the study window, requiring either long horizons or documented historical version changes.
- **Cluster:** LLM-ANNOT

### C-0164 · Machines and crowdworkers have inverted annotation difficulty profiles
- **One-sentence idea:** Map the per-task-type accuracy of VLM annotators against crowdworkers to test the hypothesis that their difficulty profiles are inverted — machines better at relations, reading, and consistency; humans better at counting, fine discrimination, and unusual instances — deriving an empirically optimal division of labor.
- **Problem:** Human-vs-machine annotation decisions are made globally per project, though comparative advantage likely varies sharply by micro-task type.
- **Core Hypothesis:** A task-type × annotator-type accuracy matrix shows strong interaction effects, and routing micro-tasks by comparative advantage beats either pure strategy and naive cost-based routing at matched budget.
- **Why Important:** Directly actionable for every dataset-construction effort, and characterizes machine annotation as a complement, not substitute, with measured boundaries.
- **Why Possibly Novel:** Micro-task-resolved comparative-advantage measurement between crowdworkers and VLMs has not been published.
- **Minimal Experiment:** Have both annotator pools label the same stratified task battery (10 micro-task types); build the accuracy matrix; simulate and validate optimal routing.
- **Main Risk:** Crowdworker quality varies enormously with pay/QC, making the human column contentious without careful protocol.
- **Cluster:** LLM-ANNOT

### C-0165 · Promptable confusion matrices make weak-supervision theory work for VLM annotators
- **One-sentence idea:** Treat multiple prompt-variants of VLM annotators as weak labeling functions whose confusion matrices can be estimated and, uniquely, *manipulated via prompt design* — bringing Snorkel-style aggregation theory to machine annotation with a controllable diversity dial.
- **Problem:** Weak-supervision aggregation assumes diverse labeling functions with estimable error structures; VLM annotation pipelines use naive majority voting without error modeling, and diversity among prompts is uncontrolled.
- **Core Hypothesis:** Prompt variants can be engineered toward complementary confusion structures (each prompt reliable on different class subsets), and matrix-aware aggregation over engineered-diverse prompts beats majority voting by a larger margin than adding more samples of one prompt.
- **Why Important:** Provides a principled, theory-backed aggregation layer for the dominant new annotation modality and a new use for prompt engineering (diversity, not accuracy).
- **Why Possibly Novel:** Deliberate confusion-matrix shaping via prompts and its integration with weak-supervision estimators is unexplored.
- **Minimal Experiment:** Engineer 8 prompt variants targeting different reliability profiles; estimate confusion matrices on a small clean set; compare aggregation strategies on a large ground-truthed pool.
- **Main Risk:** Prompt-induced diversity may be shallow (correlated deep errors persist), capping aggregation gains.
- **Cluster:** LLM-ANNOT

### C-0166 · Counterfactual questioning elicits better boundaries than direct labeling
- **One-sentence idea:** Test whether decomposing dense annotation into counterfactual queries ("if this region were removed, would the object still be complete?") yields more accurate mask boundaries from VLM annotators than direct "segment the object" instructions.
- **Problem:** VLMs are poor at direct dense output but strong at answering targeted verification questions; annotation interfaces haven't been redesigned around this asymmetry.
- **Core Hypothesis:** Boundary accuracy from aggregated counterfactual Q&A (queried on superpixel candidates) exceeds direct mask generation at matched query budget, because each binary question operates in the VLM's reliable regime.
- **Why Important:** A query-design principle could unlock dense annotation quality from models that fail at dense generation, changing what "VLM annotator" pipelines can label.
- **Why Possibly Novel:** Question-decomposition strategies for dense structure elicitation (vs. classification) are undeveloped.
- **Minimal Experiment:** Implement direct vs. counterfactual-decomposed mask annotation on 500 COCO instances at equal API cost; compare boundary F-scores against ground truth.
- **Main Risk:** Query budgets for fine boundaries may explode combinatorially, requiring smart candidate selection to stay cost-competitive.
- **Cluster:** LLM-ANNOT

### C-0167 · The net value of hallucinating captioners as dense supervisors
- **One-sentence idea:** Quantify the trade-off when detailed VLM-generated captions supervise segmentation vocabularies: hallucinated nouns inject false classes at a measurable rate while true novel nouns extend coverage — determine the operating points where caption supervision is net-positive.
- **Problem:** Caption-derived supervision pipelines celebrate coverage gains without an accounting framework for hallucination-induced poisoning of dense training.
- **Core Hypothesis:** Hallucination rate is predictable from caption length and object-context typicality; below a length threshold caption supervision is net-positive, above it poisoning dominates — yielding a falsifiable operating rule rather than a blanket verdict.
- **Why Important:** Detailed-caption pipelines are becoming standard data infrastructure; a validated net-value curve prevents both over-adoption and over-caution.
- **Why Possibly Novel:** Poisoning-vs-coverage accounting with operating thresholds for caption-supervised dense learning is missing.
- **Minimal Experiment:** Generate captions at 4 detail levels for a labeled corpus; measure noun precision/novel-recall; train open-vocab segmenters per level; map downstream quality vs. detail level.
- **Main Risk:** Hallucination structure may shift across captioner models, requiring the rule to be re-fit per model generation.
- **Cluster:** LLM-ANNOT

### C-0168 · The fixed point of self-annotation is below teacher quality — and computable
- **One-sentence idea:** Characterize the convergence of bootstrapped self-annotation (model labels data, retrains on it, repeats) for dense tasks, testing whether the process has a predictable fixed point strictly below the initial annotator's quality and identifying which interventions (confidence gating, disagreement injection) raise it.
- **Problem:** Self-training loops are deployed at scale on the hope of self-improvement, without theory or measurement of where iteration converges for structured prediction.
- **Core Hypothesis:** Iterated self-annotation converges within a few rounds to a fixed point determined by the bias (not variance) of the initial annotator; variance-reduction interventions do not move the fixed point but external disagreement sources do.
- **Why Important:** Establishes the fundamental limits of the self-improvement narrative for perception and identifies the minimal external signal needed to exceed them.
- **Why Possibly Novel:** Fixed-point characterization of dense-task self-annotation with intervention analysis has not been reported.
- **Minimal Experiment:** Run 6 rounds of segmentation self-training from a mid-quality teacher on unlabeled data; track quality trajectory; repeat with gating and cross-model disagreement interventions.
- **Main Risk:** Convergence behavior may be dataset-size dependent, requiring multiple scales for a clean characterization.
- **Cluster:** LLM-ANNOT

### C-0169 · Choice-ordering artifacts are fossilized into LLM-annotated datasets
- **One-sentence idea:** Audit deployed machine-annotated datasets for fossilized position/order biases (first-option preference, recency effects in candidate lists) and measure how these structured artifacts propagate into models trained on the data.
- **Problem:** LLM position biases are documented in evaluation contexts, but annotation pipelines present candidate labels in systematic orders (alphabetical, detector-confidence), potentially baking selection artifacts permanently into datasets nobody re-examines.
- **Core Hypothesis:** Existing machine-annotated datasets contain statistically detectable order-bias signatures (label frequency correlated with canonical presentation order), and students trained on them inherit corresponding prediction biases measurable on order-neutral test sets.
- **Why Important:** Identifies a silent, correctable corruption channel in the data ecosystem and provides forensic tools for dataset auditing.
- **Why Possibly Novel:** Forensic detection of annotation-time interface biases in released datasets is an unexplored methodology.
- **Minimal Experiment:** Reconstruct plausible candidate orderings for 3 public auto-annotated datasets; test frequency-order correlations against human-annotated controls; verify causally by re-annotating with randomized orders.
- **Main Risk:** Presentation order in original pipelines may be unrecoverable, limiting analysis to datasets with documented protocols.
- **Cluster:** LLM-ANNOT

### C-0170 · Self-generated benchmarks are systematically too easy
- **One-sentence idea:** Measure the "self-generated easiness" effect: referring expressions, questions, and captions produced by VLMs for benchmark construction are systematically easier for VLMs to solve than human-authored equivalents on the same images, inflating reported progress.
- **Problem:** Benchmark construction increasingly uses VLMs to generate queries at scale, without measuring whether machine-generated queries preferentially occupy regions of task space that machines already handle.
- **Core Hypothesis:** Model-generated queries avoid constructions models find hard (viewpoint-dependent language, negation, non-canonical attributes), yielding a quantifiable easiness gap versus human queries matched on image and target — and the gap persists even for models from other families.
- **Why Important:** If machine-built benchmarks are intrinsically easy, the field's evaluation base inflates progressively as generation replaces human authorship.
- **Why Possibly Novel:** The easiness gap has not been measured with image-and-target-matched human/machine query pairs.
- **Minimal Experiment:** For 1K image-target pairs, collect human and VLM-generated referring expressions; evaluate multiple solver models on both sets; decompose the gap by linguistic phenomena.
- **Main Risk:** Human query quality varies; needs annotation protocols ensuring human queries aren't artificially convoluted.
- **Cluster:** LLM-ANNOT

### C-0171 · Annotation language reshapes visual ground truth
- **One-sentence idea:** Show that annotating the same images via prompts in different languages produces systematically different label distributions (category boundaries, attribute salience), demonstrating that machine-annotated "ground truth" silently inherits one language's ontology.
- **Problem:** Global datasets are machine-annotated almost exclusively through English prompts, presuming visual categories are language-neutral — a claim linguistics disputes and vision has never tested at annotation scale.
- **Core Hypothesis:** Cross-language annotation of identical images differs beyond translation noise on category granularity (e.g., container words, color boundaries) in directions predicted by lexical typology, and models trained per-language inherit measurable behavioral differences.
- **Why Important:** Affects dataset validity for global deployment and operationalizes linguistic-relativity questions with unprecedented scale and control.
- **Why Possibly Novel:** Language-of-annotation as an experimental variable in machine labeling pipelines is unstudied.
- **Minimal Experiment:** Annotate 10K images in 6 languages with matched prompts via multilingual VLMs; align label spaces; test divergences against typological predictions; train and compare per-language students.
- **Main Risk:** Multilingual VLM quality asymmetries confound language effects with capability effects; needs capability-matched analysis.
- **Cluster:** LLM-ANNOT

### C-0172 · Elicited label distributions beat hard labels plus smoothing
- **One-sentence idea:** Test whether training on full label *distributions* elicited from LLM annotators (via calibrated probability queries) outperforms hard labels with label smoothing, distinguishing whether machine-annotator uncertainty carries real information about item ambiguity.
- **Problem:** Machine annotation discards the annotator's uncertainty by design, then training re-injects fake uniform uncertainty via smoothing — an obviously suboptimal round-trip if elicited uncertainty is informative.
- **Core Hypothesis:** Elicited distributions correlate with human label distributions on ambiguous items, and students trained on them beat smoothed-hard-label students on calibration and ambiguous-item accuracy while matching on clear items.
- **Why Important:** A free upgrade to every machine-annotation pipeline and a test of whether LLM annotators possess meaningful metacognition about visual labels.
- **Why Possibly Novel:** Distribution-elicitation protocols for machine annotators and their end-to-end training value are unevaluated.
- **Minimal Experiment:** Elicit label distributions on datasets with human distribution ground truth; compare distribution quality; train students on {hard, smoothed, elicited} targets; evaluate accuracy and calibration.
- **Main Risk:** Elicited probabilities may be verbal artifacts (round numbers, anchoring) requiring calibration layers that complicate the story.
- **Cluster:** LLM-ANNOT

### C-0173 · The annotation pipeline is an attack surface
- **One-sentence idea:** Demonstrate that imperceptible or innocuous-looking image perturbations can reliably flip VLM annotator outputs, enabling scalable data poisoning through public data that later gets machine-labeled — and measure how such poisoned labels propagate to student models.
- **Problem:** Adversarial robustness research targets deployed classifiers, while the annotation stage — which now determines what all future models learn — has no characterized threat model.
- **Core Hypothesis:** Perturbations optimized against one open VLM annotator transfer to commercial annotators at nontrivial rates, and poisoning a small fraction of a scraped corpus shifts student-model behavior on targeted classes measurably.
- **Why Important:** Establishes annotation-time security as a distinct problem with different constraints (attacker controls data before labeling) and motivates defenses at the pipeline level.
- **Why Possibly Novel:** Threat modeling and empirical attacks on the machine-annotation stage (rather than on trained models) are largely absent.
- **Minimal Experiment:** Craft perturbations flipping an open VLM's labels; measure transfer to 2 other annotators; run a small-scale poisoning-through-annotation study on a controlled corpus with student retraining.
- **Main Risk:** Responsible-disclosure and dual-use considerations constrain publishable detail; experiments must stay in controlled settings.
- **Cluster:** LLM-ANNOT

### C-0174 · Instruction flywheels collapse data diversity across iterations
- **One-sentence idea:** Measure diversity decay in the self-referential data flywheel where models generate instruction/annotation data for their successors, testing whether linguistic and task-type diversity contracts generation-over-generation even as quality metrics rise.
- **Problem:** Successive model generations increasingly train on predecessor-generated data; quality is tracked but distributional narrowing — the slow failure mode — is not.
- **Core Hypothesis:** Across simulated flywheel iterations, instruction-space entropy (task types, syntactic diversity, topic coverage) contracts monotonically while per-item quality scores rise, and the contraction predicts degraded generalization to human-authored long-tail requests.
- **Why Important:** Identifies and quantifies a systemic risk in the ecosystem's dominant data strategy before it becomes irreversible.
- **Why Possibly Novel:** Model-collapse studies address distribution fidelity for generative outputs; the instruction/annotation flywheel with capability-generalization endpoints is a distinct, unmeasured loop.
- **Minimal Experiment:** Run 4 flywheel iterations at small scale (model → generated instruction data → fine-tuned successor); track diversity metrics and long-tail human-eval performance per iteration.
- **Main Risk:** Small-scale flywheels may exaggerate collapse relative to production pipelines that mix in fresh human data.
- **Cluster:** LLM-ANNOT

### C-0175 · Pre-labeling anchors humans and changes the ground truth itself
- **One-sentence idea:** Quantify the anchoring effect when human annotators correct LLM pre-labels — measuring how far final "human-verified" labels drift toward machine suggestions relative to blind annotation — and derive the true cost of the speed-accuracy trade in hybrid pipelines.
- **Problem:** Pre-labeling is universally adopted for annotation speed, with verification framed as preserving human ground truth; the psychology literature predicts anchoring, but its magnitude on modern vision tasks is unmeasured.
- **Core Hypothesis:** Verified-from-prelabel annotations agree with machine suggestions far above blind-human/machine agreement rates, including on items where blind humans disagree with the machine — a drift that materially changes trained-model behavior on ambiguous classes.
- **Why Important:** "Human-verified" is treated as gold; measured anchoring rates would force error bars onto that assumption and inform interface design (e.g., blind-first protocols for critical subsets).
- **Why Possibly Novel:** Anchoring is documented in HCI generally, but its dataset-level and downstream-model consequences in vision annotation are unquantified.
- **Minimal Experiment:** Randomize annotators between blind and pre-labeled conditions on the same 5K images; measure agreement structures; train models on each version and compare.
- **Main Risk:** Anchoring magnitude depends on pay/time pressure; requires realistic (not artificially careful) annotation conditions.
- **Cluster:** LLM-ANNOT

### C-0176 · LLM auditors find enough label errors to reorder benchmarks
- **One-sentence idea:** Deploy VLM agents as error auditors (not annotators) over classic vision benchmarks, and test whether correcting the discovered label errors changes published model rankings — turning the known "benchmarks have errors" observation into a measured ranking-stability result.
- **Problem:** Label errors in canonical test sets are documented, but the community lacks a scalable audit methodology and, crucially, an answer to whether errors actually change which methods win.
- **Core Hypothesis:** Verification-mode VLM auditing achieves high precision on flagged errors (human-confirmable), corrected test sets shift model rankings for closely-matched methods, and error concentration in specific classes systematically favors models with particular biases.
- **Why Important:** Ranking stability under label correction is the actual quantity of interest for the field's decision-making, and remains unmeasured at scale.
- **Why Possibly Novel:** Prior error-detection work stopped at error rates; the audit-correct-rerank loop with modern VLM auditors on multiple benchmarks is new.
- **Minimal Experiment:** Audit two benchmark test sets with a verification-prompted VLM ensemble; human-confirm flagged items; re-evaluate 15 published models on corrected sets; report rank changes.
- **Main Risk:** Auditor biases could preferentially flag errors that disadvantage certain model families, requiring bias controls in the audit protocol.
- **Cluster:** LLM-ANNOT

### C-0177 · Recursive decomposition depth has predictable returns for mask quality
- **One-sentence idea:** Characterize the scaling behavior of agentic annotation quality with decomposition depth — an agent that recursively splits "segment the dog" into part- and boundary-level queries — testing for a predictable quality-vs-cost law and its saturation point.
- **Problem:** Agentic annotation pipelines choose decomposition granularity ad hoc, with no characterization of how quality scales with query recursion or where returns diminish.
- **Core Hypothesis:** Mask quality follows a saturating law in decomposition depth with task-dependent exponents (articulated objects benefit from deeper decomposition than blob-like ones), enabling per-instance adaptive depth policies that beat fixed-depth pipelines at matched cost.
- **Why Important:** Provides the cost-model foundation that agentic annotation currently lacks, analogous to inference-scaling laws for reasoning.
- **Why Possibly Novel:** Scaling-law treatment of annotation-agent decomposition depth is unformulated.
- **Minimal Experiment:** Implement recursive segmentation annotation at depths 1–4 over object categories stratified by shape complexity; fit quality-cost curves; validate an adaptive-depth policy.
- **Main Risk:** Deeper decomposition compounds per-query errors; the law may be non-monotonic in ways that resist clean parameterization.
- **Cluster:** LLM-ANNOT

### C-0178 · LLM-generated hard negatives beat more positives for fine-grained data
- **One-sentence idea:** Test the data-centric claim that having LLMs generate *confusable class descriptions* (hard negative definitions) to guide targeted negative mining improves fine-grained datasets more than adding equivalent budgets of positive examples.
- **Problem:** Dataset improvement defaults to collecting more positives, while the discriminative information bottleneck in fine-grained tasks is arguably the absence of curated near-miss negatives — a hypothesis without direct tests.
- **Core Hypothesis:** At matched annotation budget, augmenting training with LLM-specified hard-negative distinctions (mined images matching confusable descriptions, labeled as negatives with contrastive rationales) improves fine-grained accuracy more than doubling positives.
- **Why Important:** Would redirect data budgets across fine-grained applications and validate LLM world knowledge as a source of discriminative structure, not just labels.
- **Why Possibly Novel:** LLM-driven hard-negative specification (semantic, pre-collection) differs from standard embedding-based hard-negative mining and is untested.
- **Minimal Experiment:** On fine-grained bird/car datasets, compare budget-matched {+positives, +random negatives, +LLM-specified hard negatives} training arms.
- **Main Risk:** LLM-specified confusions may not match the student model's actual confusion matrix, misallocating the negative budget.
- **Cluster:** LLM-ANNOT

### C-0179 · Benchmarks annotated by generation N favor generation N+1 of the same family
- **One-sentence idea:** Test for lineage bias in machine-annotated benchmarks: evaluation sets labeled by a model family systematically advantage later models of that family (shared priors, formats, blind spots) over equally capable models from other lineages.
- **Problem:** Benchmark construction increasingly relies on frontier-model annotation, and cross-family fairness of the resulting evaluations is assumed without measurement — while family-correlated priors make bias plausible.
- **Core Hypothesis:** On benchmarks annotated by family A, the score gap between family-A and family-B models exceeds their gap on human-annotated benchmarks matched for task and difficulty — a lineage-bias term that grows with annotation ambiguity.
- **Why Important:** If lineage bias is real, the ecosystem's benchmark supply is quietly non-neutral, distorting model comparisons that drive research and procurement decisions.
- **Why Possibly Novel:** Family-of-annotator as a bias factor in benchmark validity has been speculated for LLM-judges but not measured through annotation-constructed vision benchmarks.
- **Minimal Experiment:** Construct matched benchmark variants annotated by two model families plus humans; evaluate model panels from both families; estimate the interaction (annotator-family × model-family) effect.
- **Main Risk:** Capability differences between annotator families produce quality differences that must be separated from bias via difficulty matching.
- **Cluster:** LLM-ANNOT

### C-0180 · Error correlation, not error rate, should drive human/machine budget splits
- **One-sentence idea:** Derive and validate an allocation rule for splitting annotation budgets between humans and LLM annotators based on measured human-machine error *correlation* per task stratum, showing it dominates the standard practice of allocating by error rate and cost alone.
- **Problem:** Hybrid annotation budgeting treats human and machine labels as interchangeable units of differing quality/cost, ignoring that the value of adding an annotator type depends on how correlated its errors are with those already collected.
- **Core Hypothesis:** In strata where machine errors correlate with each other but decorrelate from human errors, small human allocations yield outsized aggregate accuracy (and vice versa), and a correlation-aware optimizer beats rate-based allocation by a significant accuracy margin at fixed budget.
- **Why Important:** Every large dataset project makes this allocation; a validated decision rule converts folklore budgeting into measurable optimization.
- **Why Possibly Novel:** Portfolio-style (correlation-aware) treatment of annotation sourcing has not been formalized or validated on real pipelines.
- **Minimal Experiment:** On a triple-annotated corpus (2 machine families + humans), measure stratified error correlations; simulate allocation policies; validate the winning policy prospectively on a new task.
- **Main Risk:** Correlation estimates need per-stratum sample sizes that partially eat the budget savings the method promises.
- **Cluster:** LLM-ANNOT
## Sub-cluster EMP-PHEN — Surprising Empirical Phenomena (C-0181 – C-0210)

### C-0181 · Models know when they're wrong better than their softmax says
- **One-sentence idea:** Show that a linear probe on intermediate features predicts a model's own errors substantially better than its softmax confidence, revealing an internal "self-error signal" that standard readouts discard.
- **Problem:** Confidence estimation research builds external machinery (ensembles, temperature scaling) while the possibility that error-predictive information already exists inside the network, unread, has not been systematically quantified.
- **Core Hypothesis:** Error-predicting probes trained on penultimate and mid-layer features achieve significantly higher error-detection AUC than calibrated softmax across architectures, with the signal concentrated in feature directions orthogonal to class logits.
- **Why Important:** A free upgrade to selective prediction and monitoring for every deployed model, and evidence that miscalibration is a readout problem, not an information problem.
- **Why Possibly Novel:** Probing for self-error information as a systematic phenomenon (across layers, architectures, and shifts) rather than a method paper has not been done.
- **Minimal Experiment:** Train error-prediction probes on features of 8 classifiers/segmenters; compare error-detection AUC against softmax/temperature/energy baselines, ID and OOD.
- **Main Risk:** Probes may exploit dataset-specific difficulty correlates and fail on new distributions, requiring cross-domain validation.
- **Cluster:** EMP-PHEN

### C-0182 · Forgetting order is a universal constant of datasets
- **One-sentence idea:** Establish that the order in which training examples are forgotten (under continued training on new data) is highly stable across architectures, seeds, and even paradigms — making forgetting order an intrinsic, model-free property of data.
- **Problem:** Forgetting studies treat example-level dynamics as model-specific noise, missing the possibility of a universal data-intrinsic ordering with practical uses (curriculum, dataset audit).
- **Core Hypothesis:** Rank correlation of example forgetting times across independently trained models exceeds 0.8, the ordering correlates with measurable example properties (label consistency, feature-space isolation), and it transfers across model families.
- **Why Important:** A universal ordering would give a principled, transferable data-difficulty scale — useful for curriculum design, dataset pruning, and label-error detection — grounded in a robust phenomenon.
- **Why Possibly Novel:** Example-forgetting statistics exist per-model; the cross-model universality claim and its exploitation are unestablished.
- **Minimal Experiment:** Fine-tune 6 diverse models through the same distribution shift, log per-example forgetting times, compute cross-model rank correlations, and regress against example properties.
- **Main Risk:** Universality may hold only within data modalities/task types, requiring careful scoping.
- **Cluster:** EMP-PHEN

### C-0183 · More labeled data can hurt: sample-wise double descent in dense fine-tuning
- **One-sentence idea:** Document a non-monotonic relationship between labeled-data quantity and fine-tuned dense-model quality, where intermediate dataset sizes underperform both smaller and larger ones — sample-wise double descent in a practically relevant regime.
- **Problem:** Data-collection planning assumes monotone returns; if a performance valley exists at intermediate scales, teams may abandon strategies exactly at the valley floor.
- **Core Hypothesis:** For frozen-backbone segmentation heads and light fine-tuning, per-class mIoU vs. training-set size shows a reproducible dip whose location shifts with head capacity, consistent with interpolation-threshold theory — and label noise widens the valley.
- **Why Important:** Direct guidance for annotation budgeting and a bridge between double-descent theory and dense prediction practice where it has never been mapped.
- **Why Possibly Novel:** Sample-wise double descent is documented for classification with linear models; dense-prediction fine-tuning regimes are unexplored.
- **Minimal Experiment:** Train segmentation heads across 12 dataset sizes × 3 head capacities × 2 label-noise levels on ADE20K subsets; map the performance surface.
- **Main Risk:** The valley may be shallow and confined to unrealistic capacity/noise corners, limiting practical significance.
- **Cluster:** EMP-PHEN

### C-0184 · Winning tickets transfer across tasks but not across seeds
- **One-sentence idea:** Characterize the puzzling asymmetry whereby sparse trainable subnetworks (lottery tickets) found on one task often transfer to different tasks, yet fail to transfer across random seeds of the same task — inverting the intuitive generalization hierarchy.
- **Problem:** Pruning-at-initialization research treats ticket transferability inconsistently, and the seed/task asymmetry, if real, contradicts the story that tickets encode task-relevant structure.
- **Core Hypothesis:** Ticket masks encode data-generic optimization pathways tied to the specific initialization draw, so mask×init pairs are the transferable unit — masks transfer across tasks with matched init but not across inits with matched task.
- **Why Important:** Resolves what lottery tickets actually are (initialization artifacts vs. task structure), redirecting sparse-training research.
- **Why Possibly Novel:** The seed-vs-task transfer factorial has not been run cleanly at modern scale.
- **Minimal Experiment:** Find tickets on task A/init 1; evaluate all four transfer cells {task A/B} × {init 1/2}; repeat across sparsities; quantify the asymmetry.
- **Main Risk:** Results may depend heavily on pruning method and rewinding point, requiring several ticket-finding protocols.
- **Cluster:** EMP-PHEN

### C-0185 · Patch-embedding filters are a two-minute training-quality diagnostic
- **One-sentence idea:** Show that the emergence (or absence) of structured Gabor-like and color-opponent filters in a ViT's patch-embedding layer is a reliable early diagnostic of training health, predicting final performance within the first fraction of training.
- **Problem:** Practitioners lack cheap early-warning signals for doomed pretraining runs; existing loss-curve heuristics ignore the structural information in first-layer weights.
- **Core Hypothesis:** A structuredness score of patch-embedding filters (frequency-domain concentration, symmetry) at 5% of training predicts final downstream accuracy across recipes with usable correlation, and pathological runs (bad lr, broken augmentation) show diagnostic filter signatures before loss curves diverge.
- **Why Important:** Saves large-scale compute by enabling early termination decisions, and revives first-layer analysis as a practical tool rather than a visualization curiosity.
- **Why Possibly Novel:** First-layer filters are widely visualized but never validated as quantitative early predictors of run quality across recipes.
- **Minimal Experiment:** Train 20 ViT runs spanning good/broken recipes; compute filter-structure scores over time; measure early-score → final-accuracy prediction quality.
- **Main Risk:** Modern stem variants (conv stems, patch merging) may hide the signal in deeper layers, complicating a universal diagnostic.
- **Cluster:** EMP-PHEN

### C-0186 · Feature-space boundary geometry predicts class-wise robustness
- **One-sentence idea:** Demonstrate that classes whose decision boundaries in feature space are geometrically irregular (high curvature, fragmented regions) are precisely the classes that fail under distribution shift — a measurable geometric fingerprint of fragile classes.
- **Problem:** Class-wise robustness differences are documented but unexplained, leaving no way to predict which classes will fail OOD without collecting OOD data.
- **Core Hypothesis:** Per-class boundary-geometry statistics (margin distribution, boundary curvature estimated via interpolation probing) computed purely on ID data rank-predict per-class OOD degradation across shift types.
- **Why Important:** Enables shift-free robustness auditing at class granularity — actionable for deciding where to collect data or add safeguards.
- **Why Possibly Novel:** Geometry-robustness links exist at the model level; per-class geometric fingerprints with OOD-prediction validation are new.
- **Minimal Experiment:** Estimate class-wise boundary statistics for ImageNet models; correlate with per-class drops on ImageNet-{C,R,Sketch}; validate predictions on held-out shift types.
- **Main Risk:** Boundary estimation in high dimensions is noisy; conclusions must be robust across estimators.
- **Cluster:** EMP-PHEN

### C-0187 · Random labels still teach real early-layer features
- **One-sentence idea:** Quantify how much of a network's early-layer feature quality arises independently of label content by training with fully random labels and measuring transferability layer by layer, separating "data-driven" from "supervision-driven" representation depth.
- **Problem:** The division of labor between input statistics and label information across network depth is assumed (early = generic, late = semantic) but rarely measured against the random-label control at modern scale.
- **Core Hypothesis:** Random-label training on ImageNet-scale data produces early layers whose transfer value matches correctly-supervised training up to a characteristic depth (the "supervision horizon"), which shifts predictably with data scale and augmentation strength.
- **Why Important:** Locates exactly where labels start mattering — informing layer-freezing strategies, SSL theory, and how much annotation buys at each depth.
- **Why Possibly Novel:** Random-label experiments target memorization; the depth-resolved transfer-value comparison defining a supervision horizon is unmapped.
- **Minimal Experiment:** Train matched ViTs with true vs. random labels; probe every layer's transfer on 5 downstream tasks; locate the divergence depth across augmentation regimes.
- **Main Risk:** Random-label training instability may require recipe changes that weaken the matched comparison.
- **Cluster:** EMP-PHEN

### C-0188 · Deployed segmenters change answers with batch composition
- **One-sentence idea:** Quantify the underappreciated instability whereby segmentation outputs for a fixed image change depending on what other images share its inference batch (through batch normalization or cross-batch statistics), violating the implicit determinism assumption of evaluation and deployment.
- **Problem:** Models are evaluated in fixed-batch settings, while deployment batches vary; the magnitude of batch-composition sensitivity across modern architectures is undocumented.
- **Core Hypothesis:** BN-bearing segmenters show per-pixel prediction flips on a measurable fraction of pixels purely from batch-mate changes, the effect concentrates near decision boundaries, and it constitutes a privacy side channel (batch-mates are partially inferable from output changes).
- **Why Important:** Determinism violations matter for certification, reproducibility, and security; the field lacks even a magnitude estimate.
- **Why Possibly Novel:** BN train/test discrepancies are known; systematic inference-time batch-composition sensitivity audits with a side-channel analysis are not.
- **Minimal Experiment:** For 6 segmentation architectures, measure prediction variance of fixed probe images across 100 random batch compositions; test batch-mate inference from output deltas.
- **Main Risk:** Pure-LN transformers may show near-zero effect, narrowing the finding's scope to BN-era models (still widely deployed).
- **Cluster:** EMP-PHEN

### C-0189 · Modern ViTs are low-frequency-fragile, inverting the shortcut story
- **One-sentence idea:** Test whether the classic "networks over-rely on high-frequency shortcuts" narrative inverts for modern large-scale-pretrained ViTs, which may be *more* sensitive to low-frequency (global structure) perturbations than to high-frequency noise.
- **Problem:** Frequency-sensitivity conclusions from CNN-era studies still guide augmentation and robustness design, while architectural and data-scale changes plausibly reversed the sensitivity profile.
- **Core Hypothesis:** Frequency-resolved perturbation sensitivity curves show a crossover: CNNs trained on ImageNet-1k are high-frequency-dominated, while large-pretrained ViTs are low-frequency-dominated — implying frequency-based defenses and augmentations are miscalibrated for current models.
- **Why Important:** Robustness engineering (augmentation menus, adversarial defenses, compression choices) is tuned to an outdated sensitivity profile if the inversion holds.
- **Why Possibly Novel:** Frequency-sensitivity audits have not been re-run systematically across the architecture/data-scale transition.
- **Minimal Experiment:** Measure accuracy degradation under band-limited perturbations at matched perceptual budgets for 12 models spanning eras; plot sensitivity spectra by family and pretraining scale.
- **Main Risk:** Perceptual budget matching across frequency bands is methodologically delicate and could be contested.
- **Cluster:** EMP-PHEN

### C-0190 · The model zoo is converging on identical errors
- **One-sentence idea:** Document a monotonic rise in error correlation across independently developed vision models over the last decade — an emerging monoculture where new models make the same mistakes — and quantify its consequences for ensembling and benchmark headroom.
- **Problem:** Progress is tracked by accuracy while error *diversity*, which determines ensemble value, benchmark information content, and systemic-failure risk, goes unmeasured.
- **Core Hypothesis:** Pairwise error overlap (beyond chance given accuracy) has increased with shared pretraining data and recipes; consequently ensemble gains have shrunk, and residual benchmark errors are increasingly "universally hard" items where scaling yields no marginal signal.
- **Why Important:** A quantified monoculture trend affects safety arguments (redundancy assumptions), evaluation design, and the economics of ensembling.
- **Why Possibly Novel:** Error-consistency snapshots exist for specific comparisons; the longitudinal trend analysis across model generations with its systemic implications is missing.
- **Minimal Experiment:** Evaluate 40 models spanning 2015–2025 on fixed test sets; compute era-stratified error-consistency statistics; relate to training-data/recipe overlap metadata.
- **Main Risk:** Disentangling accuracy-driven overlap from genuine error correlation requires careful null models.
- **Cluster:** EMP-PHEN

### C-0191 · Pretraining-set images act as immovable anchors during fine-tuning
- **One-sentence idea:** Show that images seen during pretraining retain anomalously stable features through subsequent fine-tuning (relative to unseen images of the same distribution), creating "memorized anchors" that shape what fine-tuning can and cannot change.
- **Problem:** Fine-tuning dynamics are analyzed distributionally; per-example dependence on pretraining exposure — which would make fine-tuning behavior data-provenance-dependent — is unexamined.
- **Core Hypothesis:** Feature drift under fine-tuning is significantly smaller for pretraining-set members than for matched non-members, the effect scales with exposure count, and anchor density around a test example predicts its post-fine-tuning behavior.
- **Why Important:** Reveals a hidden mechanism coupling data provenance to adaptability, with implications for membership inference, unlearning, and why fine-tuning generalizes unevenly.
- **Why Possibly Novel:** Exposure-conditioned drift analysis during fine-tuning has not been performed.
- **Minimal Experiment:** Pretrain with a held-out twin set; fine-tune on new tasks; compare per-example feature drift between exposed/unexposed twins matched on content.
- **Main Risk:** Twin matching quality limits causal interpretation; needs synthetic duplicates for a clean exposure manipulation.
- **Cluster:** EMP-PHEN

### C-0192 · Adjacent transformer layers commute
- **One-sentence idea:** Characterize the surprising robustness of trained ViTs/VLMs to swapping adjacent transformer blocks at inference, mapping where the network is "order-sensitive" and what that reveals about the computational role of depth.
- **Problem:** Depth is assumed to implement ordered sequential computation, but if many layer pairs commute, middle depth may implement an unordered bag of refinements — with consequences for pruning, parallelization, and theory.
- **Core Hypothesis:** Swap tolerance is high in the middle third of depth and near-zero at the ends, tolerance predicts which layers can be executed in parallel branches with minor loss, and order-sensitivity localizes exactly where representational phase changes occur.
- **Why Important:** A commutativity map is both a scientific window into what depth computes and an engineering guide for depth-parallel inference.
- **Why Possibly Novel:** Layer-swap experiments exist anecdotally for LMs; systematic commutativity mapping across vision architectures with structural interpretation is not established.
- **Minimal Experiment:** For 6 models, evaluate all adjacent-pair swaps (and k-step permutations) on benchmarks; correlate swap damage with representation-change metrics between layers.
- **Main Risk:** Commutativity may reflect residual-stream dominance trivially; needs controls separating "layers do little" from "layers commute."
- **Cluster:** EMP-PHEN

### C-0193 · Easy pixels resolve early: prediction depth for dense tasks
- **One-sentence idea:** Establish that per-pixel segmentation decisions stabilize at characteristic depths (easy interior pixels early, boundary/rare-class pixels late), and exploit this "pixel prediction depth" phenomenon for adaptive-compute segmentation with per-pixel early exits.
- **Problem:** Dense inference spends uniform compute per pixel although difficulty is wildly heterogeneous; the layer-wise stabilization structure of dense predictions is uncharted.
- **Core Hypothesis:** Readouts at intermediate layers already agree with final predictions for a large majority of pixels, agreement depth correlates with human-perceived difficulty and error probability, and early-exit routing recovers most accuracy at a fraction of compute.
- **Why Important:** Both a scientific characterization of how dense computation unfolds with depth and a direct efficiency mechanism for high-resolution deployment.
- **Why Possibly Novel:** Prediction-depth analyses exist for classification; the dense, per-pixel version and its exploitation are new.
- **Minimal Experiment:** Attach probes at every layer of a segmenter; measure per-pixel stabilization depth distributions on Cityscapes; implement threshold-based early exits and map the accuracy-compute frontier.
- **Main Risk:** Probe-induced artifacts may misestimate true stabilization; requires training-free readout controls.
- **Cluster:** EMP-PHEN

### C-0194 · Classifiers decide from a handful of patches — even for huge objects
- **One-sentence idea:** Quantify the "sparse evidence" phenomenon: final-layer decisions of ViTs rest on a remarkably small number of patch tokens regardless of object size, and measure the sufficiency and necessity of those few patches for the decision.
- **Problem:** Attribution maps suggest distributed evidence use, but deletion/insertion tests at token granularity may reveal decisions are effectively k-sparse — changing how we think about robustness and explanation.
- **Core Hypothesis:** For most correctly classified images, keeping only the top-k attended patches (k≈5–10) preserves the decision while deleting them flips it, k is nearly independent of object pixel area, and sparse-evidence images are precisely the adversarially fragile ones.
- **Why Important:** Evidence sparsity would explain patch-attack effectiveness, guide evidence-diversification training, and calibrate trust in explanation heatmaps.
- **Why Possibly Novel:** Sufficiency/necessity measured jointly at token level with the object-size independence claim has not been established.
- **Minimal Experiment:** Token-masking sufficiency/necessity curves across 5K images and 6 models; regress minimal sufficient k against object size; correlate sparsity with patch-attack vulnerability.
- **Main Risk:** Masked-input distribution shift inflates flip rates; requires infilled (not zeroed) masking controls.
- **Cluster:** EMP-PHEN

### C-0195 · Discriminative models are secretly better at what they can compress
- **One-sentence idea:** Test whether purely discriminatively trained networks show a likelihood-accuracy coupling — being more accurate on images they can implicitly compress/reconstruct better — revealing a generative substrate inside discriminative learning.
- **Problem:** Discriminative and generative accounts of learning are treated as separate, and per-example accuracy variation in classifiers lacks an explanatory variable beyond "difficulty."
- **Core Hypothesis:** Reconstruction error from lightweight decoders trained on frozen classifier features predicts per-example classification correctness within class, and this coupling strengthens with model quality — good discriminators are implicitly good density models of their success regions.
- **Why Important:** Would unify paradigms empirically, provide an unsupervised per-example confidence signal, and explain OOD failures as density failures.
- **Why Possibly Novel:** The within-class, per-example coupling test on modern discriminative models has not been formulated.
- **Minimal Experiment:** Train feature-inversion decoders for 6 classifiers; correlate per-example reconstruction quality with correctness and confidence, ID and OOD.
- **Main Risk:** Reconstruction quality may proxy for image typicality trivially; needs typicality controls to establish added value.
- **Cluster:** EMP-PHEN

### C-0196 · Redundant neurons are optimization scaffolding, not representational waste
- **One-sentence idea:** Show that the large fraction of functionally duplicate units in trained networks can be pruned without harm *after* training but cannot be removed *before or during* training without severe damage — establishing redundancy as scaffolding required for optimization, not representation.
- **Problem:** Pruning research reads post-hoc removability as proof of overparameterization waste, conflating what the final function needs with what the training trajectory needs.
- **Core Hypothesis:** Duplicate-unit groups (high weight/activation similarity) can be collapsed post-training with negligible loss, but architecturally removing the same capacity from initialization, or penalizing duplication during training, degrades final quality disproportionately — quantifying the "scaffolding tax."
- **Why Important:** Reframes the overparameterization debate with a clean dissociation and informs when parameter-efficient training can and cannot replace prune-after-training.
- **Why Possibly Novel:** The pre/post removability dissociation with matched capacity accounting has not been cleanly measured.
- **Minimal Experiment:** Identify duplicate groups in trained ViTs; compare {post-hoc collapse, matched-smaller-from-scratch, anti-duplication-regularized} models at equal final parameter counts.
- **Main Risk:** "Duplicate" detection thresholds strongly shape results; needs robustness across similarity criteria.
- **Cluster:** EMP-PHEN

### C-0197 · Suppressed capabilities resurrect after unrelated fine-tuning
- **One-sentence idea:** Document "capability resurrection": behaviors removed by fine-tuning (e.g., a suppressed classification bias or forgotten task skill) spontaneously reappear after further fine-tuning on unrelated data, revealing that suppression edits are shallow and reversible perturbations.
- **Problem:** Fine-tuning is used to remove behaviors (debiasing, unlearning, safety edits) under the assumption that removal is durable; the persistence of removal under subsequent training is rarely tested.
- **Core Hypothesis:** Suppressed capabilities return to a measurable fraction of their original strength after unrelated fine-tuning, resurrection rate is predicted by how localized the suppressing update was, and deeper (distributed) suppression methods resist resurrection at a cost in side effects.
- **Why Important:** Durability is the core requirement of unlearning/debiasing in a world of continual model updates; resurrection would invalidate current removal-verification practice.
- **Why Possibly Novel:** Sequential-training durability audits of behavior removal are largely absent from vision and multimodal literature.
- **Minimal Experiment:** Remove a planted capability (backdoor trigger or synthetic bias) via fine-tuning; apply unrelated fine-tuning stages; track capability strength across stages for several removal methods.
- **Main Risk:** Resurrection may be strong only for shallow removal methods, turning the finding into method critique rather than a general phenomenon (still valuable).
- **Cluster:** EMP-PHEN

### C-0198 · Interpretability has a width threshold
- **One-sentence idea:** Test whether human-alignable, monosemantic units in vision models appear at characteristic width thresholds — an interpretability phase transition — implying narrow models are not just weaker but structurally less interpretable per unit.
- **Problem:** Interpretability results are collected on arbitrary model sizes, and disagreements between studies may reflect width-dependent representational regimes (superposition vs. dedicated features) rather than methodological differences.
- **Core Hypothesis:** Below a width threshold (per layer, relative to data complexity), features exist predominantly in superposition (measured by dictionary-learning reconstruction sparsity), and above it, dedicated monosemantic units emerge abruptly rather than gradually.
- **Why Important:** Establishes when unit-level interpretability is even possible, guiding both analysis-tool choice and "interpretable-by-design" scaling decisions.
- **Why Possibly Novel:** Superposition theory predicts capacity effects; the empirical phase-transition mapping across systematically varied vision-model widths is unmeasured.
- **Minimal Experiment:** Train width families (×8 range) on fixed data; quantify monosemanticity via sparse-probing and human-rated unit interpretability; locate transition points against width.
- **Main Risk:** "Monosemanticity" metrics are contested; conclusions must replicate across at least two operationalizations.
- **Cluster:** EMP-PHEN

### C-0199 · Segmentation models learn boundaries before interiors
- **One-sentence idea:** Characterize the learning-order phenomenon in dense prediction where boundary localization is acquired earlier in training than interior classification — contradicting the coarse-to-fine assumption — and exploit it for principled early stopping and curriculum design.
- **Problem:** Training dynamics of dense models are monitored by aggregate mIoU, hiding the structured order in which spatial competencies emerge and leaving schedule design uninformed.
- **Core Hypothesis:** Boundary F-score saturates in early training while interior class accuracy continues improving long after (label-dependent semantics lag geometry), and this ordering is invariant across architectures — implying late training refines "what" not "where."
- **Why Important:** Diagnoses what additional training buys, informs when boundary-focused losses are wasted, and revises the coarse-to-fine picture of dense learning.
- **Why Possibly Novel:** Competency-resolved training curves (boundary vs. interior vs. class confusion) for segmentation have not been systematically reported.
- **Minimal Experiment:** Track boundary/interior/confusion metric trajectories across training for 4 segmentation architectures on 2 datasets; test ordering invariance.
- **Main Risk:** Pretrained-backbone initialization may compress the dynamics, requiring both scratch and pretrained regimes.
- **Cluster:** EMP-PHEN

### C-0200 · Some random initializations are just better — everywhere
- **One-sentence idea:** Test whether a fixed random initialization that performs well on one dataset also performs well on unrelated datasets and tasks — i.e., "lucky inits" are init-intrinsic rather than init-task matches — with implications for init reuse as a free performance lever.
- **Problem:** Init variance is treated as i.i.d. noise per experiment; if init quality is a stable transferable property, the field is discarding a reusable resource and misattributing variance.
- **Core Hypothesis:** Final-performance rank correlation of identical inits across disjoint datasets/tasks is significantly positive, the effect persists at modern scale, and lucky inits are identifiable cheaply (early loss statistics on any dataset) — enabling "init banks."
- **Why Important:** Even 0.2–0.5 point free gains from init selection would matter at scale, and stable init quality challenges standard random-seed statistics practice.
- **Why Possibly Novel:** Cross-task init-quality correlation at realistic scale has not been established; existing evidence is anecdotal or small-scale.
- **Minimal Experiment:** Train 30 inits × 4 datasets (small models); measure cross-dataset rank correlations of final accuracy; test early-signal identifiability of top inits.
- **Main Risk:** Effect size likely shrinks with scale and schedule length; must characterize where it survives.
- **Cluster:** EMP-PHEN

### C-0201 · The last layers only calibrate — decisions are made in the middle
- **One-sentence idea:** Show via layer-wise readout that vision-model decisions are essentially fixed by mid-depth and that the final third of layers primarily reshapes confidence (calibration and margin structure), redefining what "deep" buys at inference.
- **Problem:** Depth is credited with hierarchical abstraction to the end, but if terminal layers mostly calibrate, both efficiency (early exit) and interpretability (where to look) strategies are misdirected.
- **Core Hypothesis:** Argmax agreement between mid-depth readouts and final predictions exceeds 95% on standard benchmarks while confidence distributions keep changing to the end; ablating late layers harms calibration metrics far more than accuracy.
- **Why Important:** Separates decision formation from confidence formation — with direct payoffs for early-exit design, calibration research, and mechanistic accounts of depth.
- **Why Possibly Novel:** Logit-lens style analyses are LM-centric; the decision/calibration decomposition across depth in vision models is unformalized.
- **Minimal Experiment:** Attach tuned readouts at all depths of 8 vision models; report agreement, accuracy, and calibration (ECE, margin) trajectories versus depth, ID and OOD.
- **Main Risk:** Readout tuning quality could inflate mid-depth agreement; needs training-free and trained readout agreement to bracket the truth.
- **Cluster:** EMP-PHEN

### C-0202 · Attentional capture: distant salient distractors degrade recognition
- **One-sentence idea:** Quantify a capture phenomenon in feedforward vision models whereby adding a salient but task-irrelevant object far from the target measurably degrades target recognition/segmentation — despite zero pixel overlap — mapping the "attentional budget" of architectures.
- **Problem:** Robustness evaluation perturbs targets or global statistics; the compositional failure mode of salient elsewhere-objects is unmeasured, though ubiquitous in real scenes.
- **Core Hypothesis:** Target accuracy declines monotonically with distractor saliency (not size), the effect is stronger in token-budget-constrained models (small ViTs, aggressive token pruning), and it localizes to attention reallocation measurable in attention maps.
- **Why Important:** A measurable capture law characterizes model reliability in cluttered scenes and directly tests whether attention mechanisms create human-like interference costs.
- **Why Possibly Novel:** Saliency-controlled distant-distractor psychophysics for modern architectures has not been performed.
- **Minimal Experiment:** Composite controlled scenes varying distractor saliency/distance/size; measure target task degradation and attention-mass shifts across 8 models.
- **Main Risk:** Compositing artifacts could confound; requires generative harmonization and real multi-object control scenes.
- **Cluster:** EMP-PHEN

### C-0203 · Universally hard images are predictable from simple statistics
- **One-sentence idea:** Characterize the set of images misclassified by essentially all models ("universal residue") and test whether membership is predictable from simple image-intrinsic statistics — making the ceiling of benchmark progress a measurable property of data, not models.
- **Problem:** The residual error at the top of leaderboards is treated as a modeling frontier, though it may be dominated by intrinsically ambiguous or mislabeled items identifiable without any model consensus.
- **Core Hypothesis:** Universal-residue membership is predicted (AUC > 0.8) by a compact set of statistics — label-distribution entropy from human raters, object scale, occlusion fraction, atypicality in feature-density terms — and removing/reweighting the residue changes model rankings meaningfully.
- **Why Important:** Distinguishes benchmark headroom that scaling can win from headroom that only relabeling or task redefinition can win — recalibrating progress narratives.
- **Why Possibly Novel:** Universal-error analyses exist for specific datasets; the prediction-from-statistics framing and ranking-impact analysis are undeveloped.
- **Minimal Experiment:** Intersect error sets of 30 diverse models on ImageNet/COCO; fit residue predictors from image statistics; audit residue composition with human raters.
- **Main Risk:** Residue may shrink with future models, but the methodology remains valid; conclusions should be framed dataset-relative.
- **Cluster:** EMP-PHEN

### C-0204 · Loss spikes that help: post-spike generalization improvements
- **One-sentence idea:** Test the contrarian hypothesis that certain training loss spikes are followed by measurable *improvements* in generalization relative to spike-free counterfactual trajectories — spikes as basin-escaping exploration rather than pure pathology.
- **Problem:** Spike-avoidance engineering assumes spikes are strictly harmful, but if some spike classes relocate optimization to better basins, aggressive stabilization forfeits those gains — an untested trade-off.
- **Core Hypothesis:** Runs with moderate spike incidence end at flatter minima and better OOD performance than matched spike-suppressed runs (same data/compute, stronger clipping), and post-spike trajectories show measurable basin changes (mode-connectivity barriers to pre-spike weights).
- **Why Important:** Would revise the universal spike-suppression doctrine into a calibrated tolerance policy, affecting every large training run's stability recipe.
- **Why Possibly Novel:** Spikes are studied as failures to prevent; their causal effect on final generalization via controlled suppression comparisons is unexamined.
- **Minimal Experiment:** Train matched runs across clipping/lr settings inducing {zero, moderate, severe} spike regimes; compare final ID/OOD quality, sharpness, and barrier heights to pre-spike checkpoints.
- **Main Risk:** Spike incidence covaries with effective lr, an aggressive confound requiring careful matched-schedule design.
- **Cluster:** EMP-PHEN

### C-0205 · Per-class learning proceeds by discrete jumps
- **One-sentence idea:** Show that while aggregate accuracy rises smoothly, individual class accuracies improve via abrupt, step-like transitions at class-specific times — a staircase of per-class phase changes hidden by averaging — and identify what triggers each step.
- **Problem:** Training dynamics are studied through smooth aggregate curves, potentially averaging over discrete representational events that would reveal how concepts are actually acquired.
- **Core Hypothesis:** A majority of classes exhibit identifiable jump events (accuracy moving from near-chance to near-final within a small training window), jump times are consistent across seeds for the same class, and jumps coincide with measurable feature-space reorganizations (cluster separation events).
- **Why Important:** A discrete picture of concept acquisition would connect deep learning to phase-transition theory, enable class-resolved curriculum timing, and explain seed-to-seed variance structure.
- **Why Possibly Novel:** Per-class temporal dynamics with jump detection and cross-seed consistency analysis have not been systematically characterized at scale.
- **Minimal Experiment:** Log per-class accuracy at high temporal resolution across ImageNet training (3 seeds); run change-point detection; correlate jump times with class properties and feature-cluster metrics.
- **Main Risk:** Jumps may be prevalent only for rare/hard classes, making the phenomenon a tail effect rather than a general law.
- **Cluster:** EMP-PHEN

### C-0206 · Averaging specialists creates a generalist: cross-task soup
- **One-sentence idea:** Investigate the surprising effectiveness of weight-averaging models fine-tuned on *different tasks* (a cross-task soup), testing whether the average outperforms each specialist on its own task's OOD variants — implying task-specific solutions share a common beneficial direction.
- **Problem:** Model soups are validated within single tasks; the cross-task case, which would reveal deep structure about how fine-tuning solutions relate geometrically, is unmapped.
- **Core Hypothesis:** For tasks fine-tuned from a shared base, uniform weight averaging retains most per-task ID accuracy while *improving* each task's OOD robustness beyond its own specialist — because task-specific overfitting directions cancel while shared robustification directions add.
- **Why Important:** Free multi-task deployment (one checkpoint) plus geometric insight into the shared structure of fine-tuning updates.
- **Why Possibly Novel:** Model merging exists as engineering; the OOD-improvement claim and its cancellation mechanism are untested scientific predictions.
- **Minimal Experiment:** Fine-tune a base ViT on 5 tasks separately; evaluate the uniform soup on each task's ID and OOD suites; decompose updates into shared/idiosyncratic components (SVD across task deltas).
- **Main Risk:** Task interference may dominate for dissimilar tasks; the phenomenon may require a task-similarity precondition worth mapping itself.
- **Cluster:** EMP-PHEN

### C-0207 · Positional embeddings store photographer bias
- **One-sentence idea:** Show that learned positional embeddings absorb dataset-specific spatial priors (sky-up, subjects-centered, ground-below) that measurably help ID performance but systematically harm transfer to rotated, aerial, or unconventional-framing domains — PEs as a hidden bias store.
- **Problem:** PEs are considered content-neutral geometric infrastructure; if they encode dataset framing statistics, transfer failures attributed to features may actually live in the position pathway.
- **Core Hypothesis:** Trained PEs deviate from geometric symmetry in directions matching training-set spatial statistics, ablating/symmetrizing PEs costs ID accuracy but improves aerial/rotated transfer, and PE-only surgery closes a meaningful share of the framing-domain gap.
- **Why Important:** Locates a specific, correctable carrier of dataset bias and separates "what" from "where" biases in transfer diagnostics.
- **Why Possibly Novel:** PE content analysis targets geometry recovery; the bias-storage hypothesis with transfer-causal tests is unexplored.
- **Minimal Experiment:** Analyze PE anisotropy across models; evaluate framing-shifted benchmarks before/after PE symmetrization surgery; compare against feature-space adaptation baselines.
- **Main Risk:** PE and content pathways entangle during training, so surgery may under- or over-estimate the stored bias.
- **Cluster:** EMP-PHEN

### C-0208 · Modern networks remain strangely brightness-fragile
- **One-sentence idea:** Quantify the anomalous sensitivity of state-of-the-art models to global mean shifts (DC component / brightness) that survive standard normalization — a trivial-seeming perturbation causing outsized accuracy drops that the augmentation pipeline was supposed to have solved.
- **Problem:** Brightness robustness is assumed solved by normalization and augmentation, so it is no longer measured — allowing regressions to accumulate unnoticed in modern training recipes that reduced photometric augmentation strength.
- **Core Hypothesis:** Recent large-scale-pretrained models are *more* brightness-sensitive than older supervised CNNs (measured at matched accuracy), because web-data curation and weak augmentation narrowed the exposure distribution; sensitivity concentrates in specific normalization-adjacent layers and is cheaply repairable.
- **Why Important:** Brightness shift is among the most common deployment conditions (lighting, exposure); a regression here is a silent field-wide reliability bug.
- **Why Possibly Novel:** Nobody audits trivial perturbation axes on modern models; the hypothesized robustness regression across model generations would be a striking finding.
- **Minimal Experiment:** Sweep global brightness/contrast shifts across 20 models spanning eras; plot sensitivity vs. model generation; localize sensitive layers via per-layer statistic analysis.
- **Main Risk:** The effect may be small for classification and only matter for dense tasks; scope accordingly.
- **Cluster:** EMP-PHEN

### C-0209 · Late training makes networks more linear — and more distillable
- **One-sentence idea:** Document that networks become functionally more linear (lower effective nonlinearity, better low-order approximability) late in long training runs, and show this predicts the empirical observation that late checkpoints distill into small students far better than accuracy-matched early checkpoints.
- **Problem:** What long training changes after accuracy saturates is poorly understood, and teacher-selection for distillation is guided by accuracy despite its weak correlation with distillation quality.
- **Core Hypothesis:** Linearity metrics (Jacobian stability, CKA to linearized model, polynomial approximability of logits) increase monotonically late in training, and they predict student quality under distillation better than teacher accuracy — long training performs implicit function simplification.
- **Why Important:** Provides a principled teacher-selection criterion and a new account of what overtraining buys (simpler functions, not better ones).
- **Why Possibly Novel:** The linearity-distillability link with checkpoint-resolved measurements has not been established.
- **Minimal Experiment:** For accuracy-matched checkpoint pairs (early/late) from long runs, measure linearity metrics and distill into fixed students; correlate metrics with student quality.
- **Main Risk:** Accuracy-matching early and late checkpoints exactly is hard; may require interpolated schedules.
- **Cluster:** EMP-PHEN

### C-0210 · Batch size is an ID/OOD trade-off dial at fixed validation loss
- **One-sentence idea:** Show that fine-tuning batch size systematically trades in-distribution accuracy against OOD robustness even when runs are matched on ID validation loss — small batches buy robustness with noise — making batch size a hidden robustness hyperparameter reported by nobody.
- **Problem:** Batch size is chosen for throughput and treated as performance-neutral after lr scaling, and robustness differences across published models may partly reflect this uncontrolled variable.
- **Core Hypothesis:** At matched ID validation metrics, small-batch fine-tuned models occupy flatter minima and outperform large-batch counterparts on corruption/style shift by consistent margins, with gradient-noise scale as the mediating variable that unifies batch size, lr, and data-order effects on robustness.
- **Why Important:** A free robustness lever and a confound that robustness comparisons must start controlling; also a bridge between optimization noise theory and OOD generalization.
- **Why Possibly Novel:** Batch-size effects are studied for speed/ID-generalization in pretraining; the matched-ID OOD trade-off in fine-tuning regimes is unquantified.
- **Minimal Experiment:** Fine-tune across batch sizes {8..1024} with lr scaled to match ID validation loss; evaluate OOD suites; measure sharpness and gradient-noise scale as mediators.
- **Main Risk:** Matching on ID loss vs. ID accuracy gives different comparisons; both must be reported to preempt criticism.
- **Cluster:** EMP-PHEN
## Sub-cluster ASSUMP — Unproven Community Assumptions (C-0211 – C-0240)

### C-0211 · Repeating curated data beats streaming fresh data at matched compute
- **One-sentence idea:** Test the assumption that pretraining should always prefer more unique data by comparing multi-epoch training on a curated subset against single-epoch training on the full corpus at exactly matched compute.
- **Problem:** "More unique data is better" drives corpus-scaling economics, but the unique-data premium over repeated high-quality data has not been isolated at matched token/image budgets for vision-language pretraining.
- **Core Hypothesis:** Below a corpus-quality threshold, 4–8 epochs on the best-scoring quarter of data beats one epoch on everything, with the crossover point predictable from a data-quality distribution statistic — making dataset size claims meaningless without quality-conditioned repetition analysis.
- **Why Important:** Directly determines data-acquisition strategy and reframes scaling-law inputs from "dataset size" to "effective unique information."
- **Why Possibly Novel:** Repetition studies exist for text LLMs; the vision-language version with quality-conditioned crossover prediction is missing.
- **Minimal Experiment:** Pretrain CLIP-small at fixed compute under {1×full, 2×half, 4×quarter, 8×eighth} using quality-ranked subsets; map performance vs. repetition; validate the crossover predictor on a second corpus.
- **Main Risk:** Quality-ranking method choice may drive results; requires 2–3 independent quality scorers.
- **Cluster:** ASSUMP

### C-0212 · Is dynamic attention actually necessary at scale?
- **One-sentence idea:** Challenge the assumption that input-dependent attention is the essential ingredient of ViTs by training scale-matched models with fixed (learned-but-static) token-mixing matrices and measuring exactly which capabilities require dynamism.
- **Problem:** The field attributes transformer success to dynamic attention, though mixer-style results hint otherwise at small scale, and no capability-resolved comparison exists at modern pretraining scale.
- **Core Hypothesis:** Static-mixing models match attention models on classification and coarse dense tasks at matched scale, with dynamic attention providing measurable advantages only on relational/compositional slices — quantifying, rather than assuming, attention's contribution.
- **Why Important:** If dynamism is rarely load-bearing, architectures can be made dramatically cheaper; if it is, we finally know precisely where.
- **Why Possibly Novel:** Mixer-vs-attention comparisons never used capability-stratified evaluation at matched large-scale pretraining.
- **Minimal Experiment:** Pretrain attention vs. static-mixing ViT-B on identical 20M-image data; evaluate a battery stratified by relational demands; report where the gap opens.
- **Main Risk:** Optimization recipes tuned for attention may disadvantage static models, requiring per-arm tuning honesty.
- **Cluster:** ASSUMP

### C-0213 · Human labels are not the ceiling: model-relabeled datasets train better models
- **One-sentence idea:** Test the assumption that human annotation defines the quality ceiling by comparing models trained on original human labels vs. model-relabeled versions of the same images, evaluated on independent human-verified gold sets and transfer tasks.
- **Problem:** Human labels are treated as ground truth even though they contain systematic errors and granularity mismatches (single-label on multi-object images) that models must now fit.
- **Core Hypothesis:** Training on carefully model-relabeled data (soft multi-labels, corrected errors) yields better transfer and even better performance on independently-verified test items than training on original human labels — human annotation is a noisy teacher, not a ceiling.
- **Why Important:** Changes the epistemics of dataset construction: the question becomes when to trust models over humans, with measurable criteria.
- **Why Possibly Novel:** Relabeling studies exist for test sets; the training-side ceiling question with independent gold evaluation is less settled and unexamined at dense-task level.
- **Minimal Experiment:** Relabel ImageNet-train with a strong model ensemble (soft labels); train matched students on original vs. relabeled; evaluate on human-consensus gold subsets and 8 transfer tasks.
- **Main Risk:** Circularity (evaluators share biases with relabelers) must be controlled via cross-family relabeling and human-verified gold data.
- **Cluster:** ASSUMP

### C-0214 · ImageNet-21k pretraining gains come from images, not from extra classes
- **One-sentence idea:** Decompose the celebrated benefit of pretraining on larger-vocabulary datasets (21k classes vs. 1k) to test whether gains derive from label-space richness or simply from more images, by ablating vocabulary at fixed image count.
- **Problem:** "More classes teach richer features" is a standard justification for large-vocabulary pretraining, but class count and image count are perfectly confounded in the canonical comparisons.
- **Core Hypothesis:** Pretraining on 21k images with labels coarsened to 1k super-classes loses almost none of the transfer advantage, showing the vocabulary story is mostly false and image diversity is the operative variable.
- **Why Important:** Guides label-collection investment (coarse labels suffice) and corrects the mechanistic story of what supervised pretraining transfers.
- **Why Possibly Novel:** The vocabulary-vs-images decomposition at fixed data has not been run despite the claim's ubiquity.
- **Minimal Experiment:** Pretrain matched ViTs on ImageNet-21k with {original 21k labels, coarsened 1k labels, random-merged 1k labels}; compare transfer on classification and dense suites.
- **Main Risk:** Coarsening scheme choice (semantic vs. random merges) may itself matter, requiring both.
- **Cluster:** ASSUMP

### C-0215 · Augmentation is not equivalent to dataset enlargement
- **One-sentence idea:** Refute the folk equivalence "augmentation ≈ more data" by comparing online augmentation against training on a materialized, statically augmented dataset of matched effective size, isolating the stochastic-regularization component of augmentation from its data-quantity component.
- **Problem:** Augmentation's mechanism is loosely explained as increasing effective dataset size, but online resampling also injects gradient noise and prevents memorization dynamics — mechanisms with different implications that no one has separated.
- **Core Hypothesis:** Online augmentation beats the materialized-static equivalent at matched unique-view counts, the gap grows with training length (memorization onset), and the difference is attributable to per-epoch view resampling (verified by shuffling view assignment per epoch).
- **Why Important:** Correct mechanism understanding determines whether synthetic-data pipelines (which materialize views) can replace augmentation, a live infrastructure question.
- **Why Possibly Novel:** The online-vs-materialized control at matched view budgets is basic but absent from the augmentation literature.
- **Minimal Experiment:** Train classifiers/segmenters with online vs. materialized augmentation at {1, 4, 16, 64} views per image; compare accuracy trajectories and memorization metrics.
- **Main Risk:** Very large materialized multiplicities approximate online sampling, so the design must include the practically relevant low-multiplicity regimes.
- **Cluster:** ASSUMP

### C-0216 · Pixel-precise masks are unnecessary for training segmenters
- **One-sentence idea:** Test the assumption that segmentation training requires precise boundary annotation by training with deliberately coarsened masks (blobs, polygons, scribbles) plus boundary-agnostic losses, measuring how much final boundary quality actually derives from label precision versus from image evidence.
- **Problem:** Boundary-precise annotation dominates dataset cost, justified by an untested belief that models need precise supervision to produce precise outputs.
- **Core Hypothesis:** Models trained on 10×-cheaper coarse masks with edge-aware regularization reach within 1–2 boundary-F points of precise-mask training, because boundary localization is learned from image gradients while labels mainly provide region semantics — making precision spend largely wasted.
- **Why Important:** Could cut dense-annotation budgets by an order of magnitude and redefine annotation-tool design priorities.
- **Why Possibly Novel:** Weak-supervision segmentation exists, but the precision-ablation curve (systematically degrading label precision on full datasets) quantifying the marginal value of precision is unmapped.
- **Minimal Experiment:** Train identical segmenters on ADE20K with masks degraded at 5 precision levels (±2 to ±32 px boundary jitter, polygon simplification); plot final boundary-F and mIoU vs. label precision.
- **Main Risk:** Thin-structure classes (poles, fences) may depend critically on precision, requiring class-stratified conclusions.
- **Cluster:** ASSUMP

### C-0217 · Train/test resolution folklore lacks a mechanism — and maybe a justification
- **One-sentence idea:** Re-examine the accepted practice of testing at higher resolution than training (and its "fix" via resolution fine-tuning), testing whether the benefit is an artifact of object-size distribution matching that disappears under scale-aware evaluation.
- **Problem:** The train-test resolution discrepancy literature established rules of thumb whose mechanism (apparent object size distribution shift from random-resized-crop) implies the rules should change with augmentation policy and dataset — yet they are applied universally.
- **Core Hypothesis:** The optimal test-resolution ratio is fully predicted by the crop-scale distribution used in training (a computable statistic), and datasets/augmentations exist where the standard "test bigger" advice inverts — replacing folklore with a formula.
- **Why Important:** Resolution choices affect every deployment's compute budget; a predictive formula replaces cargo-cult settings.
- **Why Possibly Novel:** The original analyses stopped at ImageNet with standard augmentation; the predictive-formula generalization and its inversion cases are unexplored.
- **Minimal Experiment:** Train models under 5 crop-scale distributions; sweep test resolutions; verify the predicted optimal ratio against the crop-statistic formula; exhibit an inversion case.
- **Main Risk:** Position-embedding interpolation effects at changed resolutions add a confound requiring careful separation.
- **Cluster:** ASSUMP

### C-0218 · Batch class composition is irrelevant at modern scale
- **One-sentence idea:** Test the persistent belief that class-balanced or class-diverse batches matter for training quality, hypothesizing that at modern batch sizes and schedule lengths, batch composition effects on final models are statistically zero.
- **Problem:** Considerable engineering (balanced samplers, class-aware batching) rests on small-scale-era evidence that has not been re-validated under current batch sizes, augmentation, and schedules.
- **Core Hypothesis:** Across batch-composition policies {random, class-balanced, class-clustered (adversarially imbalanced)}, final accuracy and per-class metrics differ by less than seed noise once batch size exceeds a few hundred — the sampler literature's effects were small-batch artifacts.
- **Why Important:** Removing dead engineering simplifies pipelines; alternatively, discovering surviving effects would locate exactly where samplers still matter (e.g., contrastive losses).
- **Why Possibly Novel:** Sampler ablations at modern scale with adequate statistical power (many seeds) are absent — everyone inherits old defaults.
- **Minimal Experiment:** Train ImageNet classifiers and COCO detectors under 4 batch-composition policies × 5 seeds at batch sizes {64, 1024}; test effect sizes against seed noise.
- **Main Risk:** Loss-type interactions (contrastive vs. CE) may split the verdict, requiring the claim to be loss-conditioned.
- **Cluster:** ASSUMP

### C-0219 · Zero-shot beats few-shot more often than the field admits
- **One-sentence idea:** Characterize the regime where few-shot fine-tuning of foundation models *underperforms* their own zero-shot behavior — testing the default assumption that any labeled target data should be used for adaptation.
- **Problem:** Practitioners reflexively fine-tune on available shots, but small-sample adaptation can destroy calibrated zero-shot structure; the boundary between help and harm is unmapped.
- **Core Hypothesis:** For distribution-matched tasks with fewer than ~50 examples per class, standard fine-tuning underperforms zero-shot with tuned inference (prompting, calibration) in a majority of cases, and a simple pre-adaptation diagnostic (zero-shot margin distribution) predicts which regime applies.
- **Why Important:** A validated use-your-shots-or-not decision rule affects every applied deployment of foundation models.
- **Why Possibly Novel:** Few-shot literature compares adaptation methods against each other, rarely against optimized zero-shot with honest per-arm tuning budgets.
- **Minimal Experiment:** Across 15 tasks × shot counts {4..128}, compare tuned zero-shot vs. 4 adaptation methods with matched tuning budgets; fit the decision-boundary predictor.
- **Main Risk:** "Tuned zero-shot" budget definitions can be contested; requires transparent, preregistered tuning protocols.
- **Cluster:** ASSUMP

### C-0220 · Softmax cross-entropy is not essential — regression to class anchors suffices
- **One-sentence idea:** Test the assumption that softmax cross-entropy is a necessary ingredient of large-scale visual classification by training scale-matched models with pure regression losses onto fixed class-anchor embeddings, examining what (if anything) the softmax geometry contributes.
- **Problem:** CE is universal and its necessity untested at scale; if regression matches it, several theory narratives (margin maximization, probability calibration during training) lose their claimed role in why vision models work.
- **Core Hypothesis:** L2 regression to fixed orthogonal class anchors matches CE accuracy at scale, differing predictably in feature geometry (no neural-collapse-style simplex) and confidence behavior — establishing the loss function as a second-order choice and isolating what genuinely requires the softmax.
- **Why Important:** Loss-agnosticism at scale would simplify multi-task/dense systems (regression composes better) and prune incorrect theory.
- **Why Possibly Novel:** Squared-loss classification studies exist at small scale; matched large-scale runs with geometry and transfer endpoints are missing.
- **Minimal Experiment:** Train ViT-B on ImageNet-21k with CE vs. anchor regression at matched schedules; compare accuracy, transfer, calibration, and feature geometry (collapse metrics).
- **Main Risk:** Recipe defaults (label smoothing, mixup) are CE-shaped and need principled regression analogues for fairness.
- **Cluster:** ASSUMP

### C-0221 · Curriculum ordering effects vanish under tuned schedules
- **One-sentence idea:** Test whether easy-to-hard curriculum benefits — a persistent community belief — survive when baseline training has properly tuned learning-rate schedules and augmentation ramps, hypothesizing curricula mostly compensate for untuned baselines.
- **Problem:** Curriculum papers compare against fixed baselines, but lr warmup and augmentation scheduling already implement implicit curricula, making explicit data ordering potentially redundant — an equivalence never audited.
- **Core Hypothesis:** With per-arm tuned schedules, explicit data curricula provide no significant final-accuracy gain in supervised and self-supervised vision training, and reported gains in the literature correlate with baseline under-tuning (measurable via reproduced baselines).
- **Why Important:** Curriculum design consumes research and engineering effort; establishing its redundancy (or its genuine niche) cleans up a noisy literature.
- **Why Possibly Novel:** A meta-experimental audit with tuning-budget matching has not been applied to visual curriculum claims.
- **Minimal Experiment:** Reproduce 3 published curriculum gains; re-tune baselines with equal budget; report gain shrinkage; run fresh curricula on tuned baselines across 2 tasks.
- **Main Risk:** Some curriculum niches (noisy-label regimes, tiny data) may genuinely survive, requiring careful scoping rather than a blanket verdict.
- **Cluster:** ASSUMP

### C-0222 · Model selection doesn't need in-distribution validation data
- **One-sentence idea:** Test the assumption that hyperparameter/checkpoint selection requires validation data from the target distribution, by measuring how often selection on a *different* dataset picks the same winner — potentially eliminating validation-split costs for many workflows.
- **Problem:** Every training pipeline reserves target-distribution validation data, an expensive default whose necessity (versus selecting on any reasonable proxy dataset) is unquantified.
- **Core Hypothesis:** Checkpoint and hyperparameter rankings are highly rank-correlated across datasets within a task family (selection transfers), except for a small identifiable set of distribution-sensitive hyperparameters (augmentation strength, calibration) — enabling validation-free adaptation for the rest.
- **Why Important:** Frees labeled data for training in low-resource settings and reveals which choices are genuinely distribution-coupled.
- **Why Possibly Novel:** Cross-dataset selection-transfer matrices for modern training pipelines have not been published.
- **Minimal Experiment:** Train grids (lr × wd × schedule × augmentation) on 4 datasets; compute cross-dataset ranking correlations per hyperparameter; identify the distribution-coupled subset.
- **Main Risk:** Task families with strong domain idiosyncrasies (medical) may break transfer, requiring family-scoped claims.
- **Cluster:** ASSUMP

### C-0223 · Width beats depth for dense prediction at matched FLOPs
- **One-sentence idea:** Challenge the depth-oriented design of dense-prediction backbones by testing whether wider-shallower models dominate deeper-narrower ones at matched compute for segmentation — the opposite of classification-era intuitions the field inherited.
- **Problem:** Backbone aspect ratios were optimized for classification and inherited by dense tasks, though dense prediction's need for spatial detail preservation plausibly favors width (more channels, fewer destructive downsampling stages).
- **Core Hypothesis:** At matched FLOPs and pretraining, shallow-wide ViT/ConvNet variants beat deep-narrow ones on segmentation boundary and small-object metrics while losing slightly on classification — a task-dependent aspect-ratio law the community has not mapped.
- **Why Important:** Free accuracy from re-proportioning existing budgets, plus design guidance for dense-first architectures.
- **Why Possibly Novel:** Depth-width trade-off studies target classification; dense-task-endpoint versions at matched budgets are missing.
- **Minimal Experiment:** Train 5 aspect-ratio variants at fixed FLOPs on ImageNet, fine-tune all on ADE20K/Cityscapes; compare dense metrics against classification.
- **Main Risk:** Optimal lr/schedules differ by aspect ratio; per-variant tuning is required for a fair map.
- **Cluster:** ASSUMP

### C-0224 · Attention visualizations still aren't explanations — the causal audit
- **One-sentence idea:** Perform the missing causal audit of the community's continued use of ViT attention maps as explanations, measuring across models and tasks how well attention agrees with causal attribution (deletion/insertion effects) and when the practice actively misleads.
- **Problem:** Despite NLP-era warnings, vision papers routinely present attention rollouts as evidence of what models use; the vision-specific validity conditions are uncharacterized.
- **Core Hypothesis:** Attention-attribution agreement is high for single-object images but collapses in multi-object and fine-grained settings (exactly where explanations are consulted), and registers/artifact tokens further decouple attention from causal use — yielding a practical validity checklist for when attention maps may be shown.
- **Why Important:** Explanation misuse propagates wrong mechanistic conclusions through the literature; a quantified validity boundary is the constructive fix.
- **Why Possibly Novel:** Attention-vs-attribution audits exist for NLP and CNN saliency; a systematic modern-ViT audit with a validity-condition deliverable does not.
- **Minimal Experiment:** For 8 models on stratified image sets, compute agreement between attention maps and causal deletion metrics; identify moderators (object count, token norms); publish the checklist.
- **Main Risk:** Causal attribution baselines are themselves imperfect; must triangulate with multiple attribution families.
- **Cluster:** ASSUMP

### C-0225 · The frozen-BN fine-tuning default deserves an autopsy
- **One-sentence idea:** Audit the universal practice of freezing BatchNorm statistics during detection/segmentation fine-tuning — inherited from small-batch-era constraints — testing whether it silently costs accuracy under modern batch sizes and normalization variants.
- **Problem:** Frozen BN became default when detection batches were tiny; the practice persists unexamined in codebases even where its original justification (noisy small-batch statistics) no longer applies.
- **Core Hypothesis:** With batch sizes ≥32, unfreezing BN (or converting to GN/LN equivalents with tuned recipes) improves fine-tuned dense-task accuracy, and the frozen default persists purely by replication of legacy configs — measurable as a field-wide artifact via config archaeology.
- **Why Important:** A pointless legacy constraint on thousands of pipelines; also a case study in how defaults fossilize.
- **Why Possibly Novel:** Nobody has systematically re-evaluated the frozen-BN default across modern batch/normalization regimes.
- **Minimal Experiment:** Fine-tune detectors/segmenters across batch sizes with BN {frozen, unfrozen, sync, converted-GN}; map where each wins; survey public configs for the default's prevalence.
- **Main Risk:** Interactions with pretrained-weight statistics may make unfreezing sensitive to lr, demanding careful recipe reporting.
- **Cluster:** ASSUMP

### C-0226 · Test-time augmentation gains are a miscalibration symptom
- **One-sentence idea:** Test the assumption that test-time augmentation (TTA) is a benign accuracy booster, hypothesizing that TTA gains occur precisely where models are miscalibrated or shortcut-reliant — making TTA gain a diagnostic of model pathology rather than a free lunch.
- **Problem:** TTA is applied ritually without understanding what its gains signify; if well-trained models gain nothing, TTA magnitude carries unexploited diagnostic information.
- **Core Hypothesis:** TTA gain per model anti-correlates with calibration quality and augmentation-invariance of features; for the best modern models TTA is neutral-to-harmful OOD (averaging over views the model treats inconsistently amplifies bias), and per-image TTA disagreement predicts errors better than confidence.
- **Why Important:** Reframes a ubiquitous inference trick as a measurement instrument, and warns where TTA actively hurts.
- **Why Possibly Novel:** TTA has never been characterized as a model-pathology diagnostic with cross-model correlational structure.
- **Minimal Experiment:** Measure TTA gains, calibration, and invariance metrics for 15 models ID and OOD; test the correlational predictions; evaluate TTA-disagreement as an error signal.
- **Main Risk:** TTA policy choice (which augmentations) modulates everything; requires a standardized TTA battery.
- **Cluster:** ASSUMP

### C-0227 · Where exactly does pretraining stop paying? The crossover map
- **One-sentence idea:** Re-test the assumption that pretrained initialization always dominates random initialization by mapping the crossover frontier (labels × task type × architecture) where from-scratch training catches up, updated for modern ViTs, recipes, and dense tasks.
- **Problem:** The "rethinking pretraining" findings (random init catches up on COCO with enough data) predate ViTs and modern pretraining; today's practitioners extrapolate pretrained-always-wins from classification-era evidence without a current map.
- **Core Hypothesis:** The crossover point has moved substantially with architecture era: modern web-pretrained ViTs retain advantages far longer on semantic tasks but lose them *faster* on geometry-heavy tasks (depth, boundaries), where pretraining priors misalign — a task-structured frontier, not a single answer.
- **Why Important:** Determines when domain-specific from-scratch training is rational — a recurring industrial decision made today on stale evidence.
- **Why Possibly Novel:** No post-ViT, multi-task-family crossover study exists.
- **Minimal Experiment:** Train pretrained vs. scratch across label budgets {10k..1M} on {segmentation, detection, depth}; locate per-task crossovers; compare against CNN-era results.
- **Main Risk:** From-scratch recipes need real tuning effort to be fair, and compute cost is substantial.
- **Cluster:** ASSUMP

### C-0228 · Contrastive learning doesn't need many negatives
- **One-sentence idea:** Test the foundational assumption that contrastive methods require large negative pools (huge batches or memory banks), hypothesizing that with retuned temperature and schedule, a few dozen negatives match tens of thousands — collapsing a major systems requirement.
- **Problem:** The large-batch requirement shaped contrastive-learning infrastructure (memory banks, cross-device gathers), justified by early ablations that entangled negative count with temperature and lr settings tuned for large batches.
- **Core Hypothesis:** The effective number of *informative* negatives per step is small; with temperature scaled to negative count, quality is flat from ~64 to 65k negatives, and the historical large-batch gains were optimization (lr-batch coupling), not statistics.
- **Why Important:** Removes the systems barrier that pushed the field toward negative-free methods for the wrong reason, and corrects the theoretical account of what negatives do.
- **Why Possibly Novel:** Negative-count ablations with per-count temperature/lr retuning have not been done cleanly.
- **Minimal Experiment:** Train SimCLR-style models across negative counts {32..65k} with per-arm tuned temperature/lr at fixed total compute; compare transfer quality.
- **Main Risk:** Effects may differ between image-only and image-text contrastive settings, requiring both.
- **Cluster:** ASSUMP

### C-0229 · Multi-task pretraining's benefit is the data, not the tasks
- **One-sentence idea:** Decompose multi-task pretraining benefits by comparing multi-task models against single-task models trained on the *pooled images* (with only one task's labels), testing the assumption that task diversity itself — rather than image diversity — improves representations.
- **Problem:** Multi-task pretraining conflates two variables (more images, more supervision types), and its celebrated generality gains have never been attributed between them.
- **Core Hypothesis:** Most of the multi-task advantage on held-out tasks is reproduced by single-task training on the pooled image set; genuine task-synergy effects are small and confined to related task pairs, with measurable negative transfer elsewhere — deflating the "tasks teach generality" story.
- **Why Important:** Determines whether to invest in diverse *labels* or diverse *images* — different cost structures by orders of magnitude.
- **Why Possibly Novel:** The pooled-image control is missing from multi-task pretraining literature.
- **Minimal Experiment:** Train {multi-task on pooled data, single-task on pooled images, single-task on own data} at matched compute; evaluate on held-out task transfer; decompose gains.
- **Main Risk:** Label-availability asymmetries make exact pooling constructions delicate; synthetic task setups may be needed for full control.
- **Cluster:** ASSUMP

### C-0230 · Label smoothing's benefits are a calibration illusion
- **One-sentence idea:** Re-audit label smoothing — a near-universal default — testing the hypothesis that its apparent generalization gains are largely evaluation artifacts (better ECE, minor top-1 noise) while it measurably damages feature transferability, distillation, and rare-class geometry.
- **Problem:** Smoothing is applied by default from classification-era results, while scattered evidence of its harms (distillation, transfer) has never been consolidated into an overall accounting that could change the default.
- **Core Hypothesis:** Across modern recipes, smoothing's top-1 gains are within seed noise, its calibration gains vanish after temperature scaling, and its feature-space costs (class-cluster collapse, lost intra-class structure) measurably harm transfer, retrieval, and long-tail performance — netting negative for foundation-style training.
- **Why Important:** A default applied to virtually every supervised run deserves a full cost-benefit audit; flipping it is free.
- **Why Possibly Novel:** Individual harms are documented in isolation; the consolidated net-value audit against tuned baselines is missing.
- **Minimal Experiment:** Train matched models ± smoothing across 3 scales; evaluate top-1, post-hoc-calibrated ECE, transfer, distillation, retrieval, and long-tail metrics; report the ledger.
- **Main Risk:** Smoothing may interact with other regularizers (mixup), requiring factorial rather than univariate design.
- **Cluster:** ASSUMP

### C-0231 · Heavy augmentation compensates for optimization, not data
- **One-sentence idea:** Test the belief that ViTs inherently need heavy augmentation (RandAugment, mixup, cutmix) by checking whether longer schedules with tuned optimization at larger data scale eliminate the augmentation requirement — reframing augmentation as an optimization crutch of the ImageNet-1k regime.
- **Problem:** The "ViTs are data-hungry / augmentation-hungry" doctrine comes from ImageNet-1k-era training constraints; whether augmentation adds value beyond compensating for limited optimization/data has not been isolated.
- **Core Hypothesis:** At 10×-ImageNet scale with tuned schedules, removing heavy augmentation costs little final accuracy and *improves* feature calibration and fine-grained sensitivity (augmentation-induced invariances destroy real signal, e.g., color for species), making the heavy-augmentation default scale-inappropriate.
- **Why Important:** Augmentation policies impose invariances with task costs; knowing when they are pure crutches allows cleaner pretraining at scale.
- **Why Possibly Novel:** Augmentation-necessity re-audits across data scales with capability-cost accounting (what invariances destroy) are not available.
- **Minimal Experiment:** Train ViT-B at {1×, 3×, 10×} ImageNet-scale data with {heavy, light, none} augmentation, tuned per arm; evaluate accuracy plus invariance-sensitive tasks (color/texture-dependent fine-grained sets).
- **Main Risk:** Compute cost of the grid; interactions with weight decay may complicate attribution.
- **Cluster:** ASSUMP

### C-0232 · OOD detection is a readout problem, not a training problem
- **One-sentence idea:** Test the assumption that good out-of-distribution detection requires specialized training (outlier exposure, contrastive OOD objectives) by showing simple density estimation on frozen foundation-model features matches or beats trained detectors across standard benchmarks.
- **Problem:** OOD detection research concentrates on training interventions, while the null hypothesis — that modern pretrained features already suffice and only the scoring rule matters — has not been given a serious, tuned defense.
- **Core Hypothesis:** Gaussian-mixture or kNN density scores on frozen DINOv2/CLIP features, with feature-layer and preprocessing tuned honestly, match specialized OOD-trained methods on far- and near-OOD suites, implying the field is optimizing the wrong component.
- **Why Important:** Would redirect OOD research toward scoring/readout theory and hand practitioners a training-free strong baseline.
- **Why Possibly Novel:** Frozen-feature baselines appear in papers as strawmen without tuning parity; an aggressively tuned version as the central claim is different.
- **Minimal Experiment:** Tune frozen-feature detectors (layer, dimensionality, scorer) with the same budget given to 5 trained methods; compare on OpenOOD-style suites.
- **Main Risk:** Near-OOD fine-grained cases may genuinely require task-adapted features, splitting the verdict.
- **Cluster:** ASSUMP

### C-0233 · ViTs learn position without position embeddings
- **One-sentence idea:** Quantify how much spatial position ViTs can recover with position embeddings removed entirely — via content cues like vignetting, chromatic aberration, and layout statistics — testing the assumption that PEs are a necessity rather than a convenience.
- **Problem:** PE necessity is asserted from early ablations at small scale; if large-scale training recovers position from content, PE design debates (learned/2D/RoPE) may matter less than believed, and models may be using photographic side channels no one accounts for.
- **Core Hypothesis:** PE-free ViTs trained at scale recover most position-dependent task performance, position is decodable from their features (probes), and the recovery is driven by identifiable photographic statistics (verified by ablating vignetting/aberration via synthetic correction) — revealing a hidden cue channel present in all models.
- **Why Important:** Exposes side channels that affect robustness (models depending on camera artifacts) and re-scopes the PE literature.
- **Why Possibly Novel:** PE-free training exists as ablation folklore; the cue-attribution analysis (which image statistics carry position) is new.
- **Minimal Experiment:** Train PE-free vs. standard ViTs at moderate scale; probe positional decodability; retrain on artifact-corrected images to attribute the position signal.
- **Main Risk:** PE-free optimization may be unstable, requiring architectural accommodations that complicate comparisons.
- **Cluster:** ASSUMP

### C-0234 · Skip connections to the decoder are legacy, not necessity
- **One-sentence idea:** Test whether the encoder-decoder-with-skips design (UNet-style), assumed necessary for precise dense prediction, is matched by plain single-stream ViTs with simple learned upsampling once pretraining is strong — relegating skip architecture to a small-model-era artifact.
- **Problem:** Skip connections are universal in segmentation architectures based on CNN-era evidence; whether strong pretrained representations still need multi-scale skip routing is untested at modern scale.
- **Core Hypothesis:** With strong pretrained ViT features, a skip-free decoder (single-scale features + learned upsampler) reaches within 0.5 mIoU and 1 boundary-F point of skip-based designs, with the residual gap confined to thin structures — because modern features already preserve recoverable high-frequency information.
- **Why Important:** Simplifies dense architectures substantially (memory, engineering) and updates design lore to the pretrained-feature era.
- **Why Possibly Novel:** Plain-ViT dense heads exist, but a rigorous skip-ablation study controlling decoder capacity and pretraining strength is missing.
- **Minimal Experiment:** Compare skip-full/skip-free decoders at matched decoder FLOPs over {weak, strong} pretrained backbones on ADE20K/Cityscapes with structure-stratified metrics.
- **Main Risk:** Thin-structure classes may show large gaps, making the claim metric-dependent.
- **Cluster:** ASSUMP

### C-0235 · Architectural diversity no longer buys ensemble gains
- **One-sentence idea:** Test the assumption that ensembling diverse architectures beats ensembling seeds of one architecture, hypothesizing that convergent training data and recipes have erased the architecture-diversity premium in the modern era.
- **Problem:** Ensemble design lore prescribes architectural diversity, from an era when architectures induced genuinely different error patterns; with shared pretraining corpora, that premise may be dead — but nobody has re-measured it.
- **Core Hypothesis:** At matched member accuracy, cross-architecture ensembles (ViT+ConvNeXt+MLP-mixer) now outperform same-architecture seed ensembles by a statistically negligible margin, because error correlation is dominated by shared data, not shared architecture — with the premium's disappearance traceable across model generations.
- **Why Important:** Simplifies production ensembling and quantifies the data-monoculture effect from a decision-relevant angle.
- **Why Possibly Novel:** Diversity-premium tracking across eras with data-overlap controls has not been done.
- **Minimal Experiment:** Build matched-accuracy ensembles (cross-arch vs. seed) at 3 member counts on ImageNet/COCO; compare gains; repeat with members trained on disjoint data splits to isolate the data effect.
- **Main Risk:** Matched member accuracy across architectures requires careful checkpoint selection, and OOD conclusions may differ from ID.
- **Cluster:** ASSUMP

### C-0236 · Transfer quality peaks before pretraining converges
- **One-sentence idea:** Test the assumption that longer pretraining monotonically improves transfer by measuring downstream fine-tuning quality across pretraining checkpoints, hypothesizing a transfer peak followed by decline (ossification) even as pretraining metrics improve.
- **Problem:** Pretraining runs are extended as long as budget allows under a monotonicity assumption; if late pretraining specializes representations and reduces adaptability, the field systematically over-trains for transfer purposes.
- **Core Hypothesis:** Fine-tuning performance on dissimilar downstream tasks peaks at intermediate pretraining, the decline correlates with decreasing feature plasticity (measured by fine-tuning CKA movement), and linear-probe metrics — which keep rising — actively mislead checkpoint selection for transfer.
- **Why Important:** Changes checkpoint-release policy and pretraining-budget allocation for the entire ecosystem of downstream users.
- **Why Possibly Novel:** Ossification is hypothesized in continual-learning contexts; the pretraining-length vs. fine-tuning-quality curve for modern vision models has not been mapped.
- **Minimal Experiment:** Fine-tune 10 checkpoints from one long pretraining run on 6 diverse tasks; plot transfer vs. pretraining time against linear-probe curves; measure plasticity metrics.
- **Main Risk:** The effect may exist only for distant tasks, requiring a task-similarity-resolved analysis.
- **Cluster:** ASSUMP

### C-0237 · Hard-example mining is dead weight under modern losses
- **One-sentence idea:** Audit whether hard-example mining — folklore from the OHEM/SSD era that persists in pipelines — adds anything on top of modern loss functions (focal, sample-reweighting) and augmentation, hypothesizing full redundancy.
- **Problem:** Mining heuristics survive in production configs and papers by inheritance; their marginal contribution under current losses has not been re-isolated, wasting complexity and possibly hurting calibration.
- **Core Hypothesis:** With focal-style losses and modern augmentation, all tested mining schemes change final detection/segmentation metrics by less than seed noise while measurably degrading calibration and rare-class recall (mining over-focuses on label noise) — a net-negative legacy component.
- **Why Important:** Removing dead complexity from widely copied configs, plus a case study of loss-function evolution obsoleting data heuristics.
- **Why Possibly Novel:** Nobody re-audits inherited pipeline components; mining × modern-loss factorial studies don't exist.
- **Minimal Experiment:** Factorial {mining on/off} × {CE, focal} × {light, heavy augmentation} on COCO detection with 5 seeds; report effects on accuracy, calibration, and noisy-label sensitivity.
- **Main Risk:** Extreme class-imbalance settings may still benefit from mining, requiring imbalance-stratified conclusions.
- **Cluster:** ASSUMP

### C-0238 · Global context modules don't actually use global context
- **One-sentence idea:** Test the assumption that segmentation improvements from global-context modules (large kernels, global attention, context pooling) come from using long-range information, by measuring effective receptive fields and performing context-ablation at inference — hypothesizing gains are parameter/optimization effects with decisions remaining local.
- **Problem:** Context modules are justified by "segmentation needs global reasoning," yet effective-receptive-field studies suggest decisions stay local; the causal contribution of long-range pathways has not been separated from added capacity.
- **Core Hypothesis:** Masking all information beyond a local window at inference degrades context-module models no more than plain models for the vast majority of pixels; capacity-matched local-only variants of context modules match their accuracy — the "global" story is mostly unearned.
- **Why Important:** Redirects architecture design away from decorative globality and identifies the small pixel population (if any) that genuinely needs long-range evidence.
- **Why Possibly Novel:** Inference-time context-ablation accounting with capacity-matched controls has not been applied to the context-module literature.
- **Minimal Experiment:** For 5 segmentation architectures, measure accuracy vs. context-window ablation radius; train capacity-matched local variants of 2 context modules; compare.
- **Main Risk:** Certain classes (large stuff regions, relative-position-defined classes) may show genuine global dependence, requiring class-stratified reporting.
- **Cluster:** ASSUMP

### C-0239 · Weight decay at scale is learning-rate control, not regularization
- **One-sentence idea:** Test the textbook assumption that weight decay prevents overfitting in large-scale training, against the mechanistic alternative that its role is controlling effective learning rate through weight-norm dynamics — with the regularization story predicting effects that fail to materialize.
- **Problem:** WD is tuned in every run under a regularization narrative, but normalization layers make loss scale-invariant in weights, so WD's textbook mechanism cannot apply — leaving practice guided by a wrong story whose competing prediction has not been decisively tested in vision pretraining.
- **Core Hypothesis:** Matching the effective-lr trajectory of a WD run (via explicit norm control or scheduled lr) without any decay reproduces its accuracy and generalization, across data scales — including regimes where the regularization story predicts WD should matter most (small data) — unifying WD effects under optimization dynamics.
- **Why Important:** Correct mechanism yields principled joint lr/WD scheduling instead of 2D grid searches, saving tuning compute everywhere.
- **Why Possibly Novel:** The norm-dynamics account exists theoretically; the decisive matched-trajectory falsification experiments in realistic vision training are incomplete.
- **Minimal Experiment:** Train matched runs {WD, no-WD + norm-matched lr schedule, no-WD} across {small, large} data; compare accuracy, sharpness, and margin distributions; test where the arms diverge.
- **Main Risk:** Unnormalized parameter subsets (final layers, embeddings) genuinely receive regularization from WD, requiring parameter-group-resolved analysis.
- **Cluster:** ASSUMP

### C-0240 · The "frozen backbone preserves robustness" doctrine mismeasures robustness
- **One-sentence idea:** Challenge the accepted claim that freezing pretrained backbones (or linear probing) preserves OOD robustness better than fine-tuning, by testing whether the effect is an artifact of measuring robustness on shifts aligned with the pretraining distribution — with the conclusion reversing on shifts aligned with the target task.
- **Problem:** The influential probing-vs-fine-tuning robustness result guides adaptation practice, but its evaluation shifts (ImageNet variants) are pretraining-adjacent, plausibly building in the conclusion.
- **Core Hypothesis:** Fine-tuned models beat frozen-feature models on task-native shifts (new hospitals for medical tasks, new cities for driving) even while losing on pretraining-adjacent shifts — robustness rankings are shift-relative, and the doctrine holds only for one (often irrelevant) shift family.
- **Why Important:** Adaptation policy for safety-relevant deployments currently follows a rule that may be backwards for the shifts practitioners actually face.
- **Why Possibly Novel:** Shift-taxonomy-resolved re-evaluation of the probing/fine-tuning robustness trade-off has not been performed.
- **Minimal Experiment:** Compare probing/fine-tuning/LP-FT across 3 task domains, each with pretraining-adjacent and task-native shift suites; test the predicted ranking reversal.
- **Main Risk:** Constructing genuinely task-native shift suites requires domain data collection effort.
- **Cluster:** ASSUMP
## Sub-cluster NEG-HYP — Negative-Result Hypotheses (C-0241 – C-0270)

### C-0241 · Attention-guided augmentation does nothing under matched budgets
- **One-sentence idea:** Predict a null result for the popular family of attention-guided data augmentation methods (crop/mask where the model attends), hypothesizing they fail to beat random-policy baselines once tuning budgets and augmentation strength are matched.
- **Problem:** Saliency/attention-guided augmentation papers report gains against default random policies without matching the hyperparameter search invested in the guided variant.
- **Core Hypothesis:** At equal search budget over strength/probability parameters, guided and random policies are statistically indistinguishable on final accuracy, because the guidance signal correlates with what random cropping already samples at typical object scales.
- **Why Important:** A confirmed null would deflate a method family and establish budget-matched augmentation evaluation as the reporting standard.
- **Why Possibly Novel:** Budget-matched adversarial audits of guided augmentation have not been published; the literature accumulates positive results without controls.
- **Minimal Experiment:** Reimplement 3 guided-augmentation methods; tune each and the random baseline with identical 50-trial budgets on 2 datasets × 2 architectures; compare with seed-level statistics.
- **Main Risk:** One method may genuinely survive, converting the paper from a clean null into a mixed audit (still valuable).
- **Cluster:** NEG-HYP

### C-0242 · Synthetic formula-driven pretraining doesn't survive strong baselines
- **One-sentence idea:** Test the null hypothesis that pretraining on synthetic formula-generated images (fractals, procedural textures) provides no transfer advantage over training from scratch with modern augmentation at matched total compute.
- **Problem:** Formula-driven pretraining claims rest on comparisons to weakly augmented from-scratch baselines, leaving open whether synthetic pretraining adds anything beyond what strong augmentation already provides.
- **Core Hypothesis:** With RandAugment-class recipes and matched compute (pretraining epochs folded into longer target training), the synthetic-pretraining advantage disappears or inverts on most downstream tasks, because both interventions supply the same low-level inductive bias.
- **Why Important:** Synthetic pretraining is pitched as a privacy/copyright-safe substitute for web data; knowing its real value against honest baselines matters for that agenda.
- **Why Possibly Novel:** Compute-folded baselines (spending the pretraining budget on the target task) are absent from this literature.
- **Minimal Experiment:** Compare {formula-pretrained → fine-tune} vs. {from-scratch with equal total compute and tuned augmentation} on 5 downstream tasks at 2 data scales.
- **Main Risk:** Very-low-data downstream regimes may preserve a synthetic-pretraining niche, requiring regime-resolved conclusions.
- **Cluster:** NEG-HYP

### C-0243 · NAS gains for dense prediction were training-recipe gains
- **One-sentence idea:** Predict that architectures discovered by neural architecture search for segmentation/detection do not outperform hand-designed baselines once both are trained with identical modern recipes — the reported gains having come from recipe co-optimization.
- **Problem:** NAS papers necessarily co-tune training procedures during search, then compare against baselines trained with older recipes, leaving architecture-vs-recipe attribution unresolved for dense tasks.
- **Core Hypothesis:** Re-training published NAS-derived dense architectures and their hand-designed contemporaries under one standardized modern recipe compresses the reported gaps to statistical insignificance.
- **Why Important:** If architecture search bought nothing beyond recipes, the field's compute is better spent on recipe research and the NAS-for-dense literature needs re-baselining.
- **Why Possibly Novel:** Recipe-equalized re-evaluations exist for classification NAS; the dense-prediction version does not.
- **Minimal Experiment:** Select 4 NAS and 4 manual dense architectures of matched FLOPs; train all under one tuned recipe with 3 seeds; compare against originally reported gaps.
- **Main Risk:** A standardized recipe may inadvertently favor one design family; requires two recipe variants for robustness.
- **Cluster:** NEG-HYP

### C-0244 · Depth-segmentation multi-task synergy fails under capacity matching
- **One-sentence idea:** Test the null that jointly learning depth and semantic segmentation — a canonical "synergistic" task pair — provides no benefit to either task over single-task models at matched capacity and compute.
- **Problem:** Multi-task synergy claims for geometry+semantics rely on comparisons where the multi-task model effectively receives more supervision or capacity, and the field repeats the synergy story without controlled evidence.
- **Core Hypothesis:** With capacity and compute matched (single-task models widened to consume the same budget), joint depth+segmentation training shows zero or negative transfer on both tasks, because the tasks share input statistics but not decision structure.
- **Why Important:** Multi-task architectures complicate systems; if the flagship synergy pair fails controlled testing, the burden of proof across the MTL literature shifts.
- **Why Possibly Novel:** Capacity-matched nulls are rarely published; synergy claims persist because negative evidence is unreported.
- **Minimal Experiment:** Train {seg-only, depth-only, joint} at matched budgets on NYUv2/Cityscapes with 5 seeds; report per-task deltas with confidence intervals.
- **Main Risk:** Specific architectural couplings (cross-task attention) might rescue synergy, so the null must be scoped to standard shared-encoder designs.
- **Cluster:** NEG-HYP

### C-0245 · ViT attribution methods fail the sanity checks too
- **One-sentence idea:** Extend the classic attribution sanity checks (parameter randomization, data randomization) to the modern ViT explanation stack (attention rollout, ViT-specific Grad-CAM variants, relevance propagation), predicting widespread failure that the community has not registered.
- **Problem:** Sanity-check results from CNN-era saliency methods prompted no equivalent audit of the ViT explanation tools now used in papers and applications.
- **Core Hypothesis:** A majority of popular ViT attribution methods produce visually plausible maps that are substantially invariant to randomizing late-layer parameters — failing the basic dependence test — with attention-based methods failing worst due to artifact-token dominance.
- **Why Important:** Explanations that ignore the model mislead debugging, auditing, and scientific claims; a public failure table would reset tool choice.
- **Why Possibly Novel:** The sanity-check protocol has not been systematically applied to the post-2021 ViT explanation ecosystem.
- **Minimal Experiment:** Run cascading parameter/data randomization tests on 8 ViT attribution methods across 3 models; report similarity-to-original curves and a pass/fail table.
- **Main Risk:** Some methods may pass, requiring nuanced reporting rather than a blanket negative (a better paper anyway).
- **Cluster:** NEG-HYP

### C-0246 · Multimodal "emergent abilities" dissolve under continuous metrics
- **One-sentence idea:** Test whether claimed emergent capabilities of VLMs at scale (sudden appearance of counting, OCR, spatial reasoning) disappear when measured with continuous proxies instead of thresholded accuracy — predicting smooth capability growth misread as emergence.
- **Problem:** Emergence claims drive scaling policy and safety narratives for multimodal models, but the metric-artifact critique established for LLMs has not been carried over to the multimodal capability literature.
- **Core Hypothesis:** For most claimed multimodal emergent abilities, per-item partial-credit metrics (edit distance for OCR, count error magnitude, calibrated log-likelihoods) show smooth, predictable scaling with no discontinuity — locating "emergence" in the metric, not the model.
- **Why Important:** Whether capabilities appear predictably or discontinuously changes forecasting, evaluation design, and safety arguments for multimodal systems.
- **Why Possibly Novel:** The continuous-metric re-analysis has not been performed on multimodal capability suites across model scale families.
- **Minimal Experiment:** Evaluate a scale family of VLMs on 6 "emergent" tasks with both thresholded and continuous metrics; compare scaling-curve shapes and breakpoint statistics.
- **Main Risk:** A minority of abilities may remain discontinuous under all metrics — which would itself be the more interesting finding.
- **Cluster:** NEG-HYP

### C-0247 · MAE pretraining on small domain datasets is worthless
- **One-sentence idea:** Predict a null for the widespread practice of masked-autoencoder self-pretraining on small domain-specific corpora (tens of thousands of medical/aerial images) before fine-tuning, against simply fine-tuning a general checkpoint or training from scratch with strong augmentation.
- **Problem:** Domain-MAE pipelines are popular in applied fields under the assumption that in-domain self-supervision at any scale helps, though MIM's benefits may require orders of magnitude more data than these corpora contain.
- **Core Hypothesis:** Below a corpus-size threshold (~10⁵ images), domain-MAE pretraining adds nothing over general-checkpoint fine-tuning at matched total compute, and sometimes hurts by overwriting transferable features with domain low-level statistics.
- **Why Important:** Applied communities spend real compute on a ritual step; a threshold-resolved null would redirect that budget.
- **Why Possibly Novel:** Scale-threshold characterization of domain-specific MIM value is missing; applied papers report unmatched comparisons.
- **Minimal Experiment:** On 3 medical/aerial tasks, compare {general checkpoint FT, domain-MAE→FT, scratch+augmentation} at matched compute across corpus sizes {5k, 50k, 500k}.
- **Main Risk:** Extreme domain gaps (e.g., spectral imagery) may preserve value at small scale, requiring domain-gap-conditioned conclusions.
- **Cluster:** NEG-HYP

### C-0248 · Ensemble robustness doesn't survive distillation
- **One-sentence idea:** Test the null that distilling an ensemble into a single student transfers its accuracy but not its OOD robustness or calibration — the properties for which ensembles are actually valued — making "distill the ensemble" a false economy for reliability purposes.
- **Problem:** Ensemble distillation is standard for deployment, implicitly assuming the ensemble's reliability profile transfers along with its logits; the assumption is largely untested on modern shift benchmarks.
- **Core Hypothesis:** Students match ensemble ID accuracy while recovering only a small fraction of the ensemble's OOD gain and calibration advantage, because those derive from prediction *diversity* that pointwise logit matching cannot encode.
- **Why Important:** Safety-motivated ensembling followed by distillation may silently discard the safety; deployment practice needs this measured.
- **Why Possibly Novel:** Distillation evaluations report ID accuracy; the reliability-transfer decomposition (accuracy vs. robustness vs. calibration vs. uncertainty quality) is not systematically done.
- **Minimal Experiment:** Distill deep ensembles into matched students; evaluate ID accuracy, corruption/shift robustness, calibration, and selective-prediction metrics for {member, ensemble, student}.
- **Main Risk:** Diversity-aware distillation variants may close the gap, requiring inclusion as arms rather than dismissal.
- **Cluster:** NEG-HYP

### C-0249 · LLM-generated class descriptors don't beat tuned templates
- **One-sentence idea:** Predict that the popular technique of augmenting zero-shot classifiers with LLM-generated class descriptions ("a tiger has stripes...") provides no gain over properly tuned generic prompt templates, its reported improvements being baseline-tuning artifacts.
- **Problem:** Descriptor methods compare enriched prompts against default templates, not against templates given the same tuning attention, so the semantic-knowledge claim is confounded with prompt-quality effort.
- **Core Hypothesis:** After matching template-search budgets, descriptor ensembles add nothing on standard benchmarks, and their apparent gains reduce to ensemble-size and calibration effects reproducible with content-free template variations.
- **Why Important:** The result would sharpen what kind of language knowledge actually reaches zero-shot visual classification, and impose budget-matched controls on the prompt-engineering literature.
- **Why Possibly Novel:** Content-free ensemble controls (matched-size ensembles of paraphrased generic templates) are absent from descriptor papers.
- **Minimal Experiment:** Compare {default template, tuned template, k generic paraphrases, k LLM descriptors} at matched k across 8 classification datasets on 2 VLMs.
- **Main Risk:** Fine-grained domains (birds, aircraft) may show genuine descriptor value, splitting the verdict by dataset type.
- **Cluster:** NEG-HYP

### C-0250 · Adversarial robustness still doesn't cross perturbation families — at any scale
- **One-sentence idea:** Test whether the long-standing negative result that adversarial training fails to generalize across perturbation types (L∞→L2, pixel→spatial) persists at foundation-model scale, against the increasingly voiced hope that scale induces general robustness.
- **Problem:** Cross-perturbation generalization failures were established on small models; scaling-era optimism asserts, without systematic evidence, that large adversarially trained models generalize their robustness more broadly.
- **Core Hypothesis:** Cross-family robust accuracy remains near zero even for the largest available adversarially trained models, with scale improving within-family robustness only — the transfer matrix stays block-diagonal at every scale.
- **Why Important:** If scale doesn't buy robustness generality, deployment threat models cannot rely on it, and the robustness research agenda keeps its hard shape.
- **Why Possibly Novel:** Scale-resolved cross-perturbation transfer matrices have not been assembled for the current generation of robust models.
- **Minimal Experiment:** Evaluate robust models across scales on a 6×6 perturbation-family transfer matrix; test scale trends per matrix cell.
- **Main Risk:** Availability of large robust checkpoints limits the scale axis; may require training mid-scale models.
- **Cluster:** NEG-HYP

### C-0251 · More than two views adds nothing to contrastive learning
- **One-sentence idea:** Predict that multi-view (>2) contrastive formulations provide no representation-quality benefit over standard two-view training at matched compute, with multi-crop's celebrated gains attributable entirely to its resolution asymmetry, not view count.
- **Problem:** Multi-view objectives add cost and complexity based on the intuition that more views mean better invariance estimates, without controlled accounting against the two-view baseline given equal compute.
- **Core Hypothesis:** At fixed total forward-pass budget, distributing compute over more views per image underperforms spending it on more images with two views; multi-crop's advantage disappears when its low-resolution views are replaced by matched-resolution ones, isolating resolution (not multiplicity) as the driver.
- **Why Important:** Simplifies SSL recipes and corrects the mechanistic story behind one of the field's most-copied tricks.
- **Why Possibly Novel:** View-count vs. image-count compute allocation and the resolution-decoupled multi-crop control have not been published.
- **Minimal Experiment:** Train matched models at fixed compute across {2 views × N images, 4 × N/2, 8 × N/4} and multi-crop variants with resolution controls; compare transfer.
- **Main Risk:** Interaction with batch statistics could produce view-count effects unrelated to the hypothesis, requiring careful normalization handling.
- **Cluster:** NEG-HYP

### C-0252 · Domain-adaptation methods lose to statistics correction plus pseudo-labels
- **One-sentence idea:** Test the null that the feature-alignment domain-adaptation literature (adversarial alignment, discrepancy minimization) provides no gain over the trivial pipeline of target-statistics normalization update plus confidence-filtered pseudo-labeling, at modern backbone strength.
- **Problem:** DA methods are compared against source-only baselines and each other, rarely against the strongest trivial pipeline, and pretrained-backbone improvements may have erased the alignment methods' relevance.
- **Core Hypothesis:** With strong pretrained backbones, the trivial pipeline matches or beats representative alignment methods across standard DA benchmarks, showing the field's benchmark progress has been absorbed by better features.
- **Why Important:** Redirects DA research toward the residual problems trivial pipelines cannot solve (label-shift, category mismatch) and re-baselines a large literature.
- **Why Possibly Novel:** Strong-trivial-baseline audits at modern backbone strength are missing from DA benchmarking.
- **Minimal Experiment:** Run 5 DA methods and the trivial pipeline on Office-Home/VisDA/DomainNet with DINOv2-class backbones, matched tuning budgets, 3 seeds.
- **Main Risk:** Some benchmarks with severe shift may preserve method value, requiring shift-severity-resolved conclusions.
- **Cluster:** NEG-HYP

### C-0253 · Continual-learning methods don't scale past their benchmarks
- **One-sentence idea:** Predict that regularization- and architecture-based continual-learning methods developed on small benchmarks provide no benefit over naive experience replay when applied to foundation-model fine-tuning sequences, where replay is cheap and forgetting dynamics differ.
- **Problem:** The CL literature optimizes for artificially replay-free settings at small scale, while real large-model practice has cheap replay buffers — a mismatch that may nullify the methods where they would actually be used.
- **Core Hypothesis:** On sequential fine-tuning of a pretrained ViT/VLM over 5 realistic tasks, EWC/LwF-style methods and parameter-isolation schemes underperform simple 5% replay at matched compute, with their small-benchmark advantages failing to transfer to the pretrained regime.
- **Why Important:** Clarifies which CL research transfers to the foundation-model era, potentially redirecting the field toward replay-buffer design and privacy-constrained niches.
- **Why Possibly Novel:** Systematic CL-method audits in the pretrained-sequential-fine-tuning regime with honest replay baselines are scarce.
- **Minimal Experiment:** Run 6 CL methods + replay baselines over two 5-task sequences starting from pretrained checkpoints; report average accuracy/forgetting with seeds.
- **Main Risk:** Method implementations tuned for small nets may underperform unfairly; requires per-method adaptation effort to be credible.
- **Cluster:** NEG-HYP

### C-0254 · Visual prompt tuning loses to a linear head at matched parameters
- **One-sentence idea:** Test the null that visual prompt tuning (learnable input/latent tokens) offers no advantage over a parameter-matched linear or shallow head for adapting frozen backbones on dense and classification tasks.
- **Problem:** Prompt tuning is presented as qualitatively superior adaptation, but comparisons rarely match trainable-parameter counts or tuning budgets against simple head baselines.
- **Core Hypothesis:** At matched parameter and tuning budgets, prompt tuning and head tuning reach statistically indistinguishable accuracy across tasks, with prompts' occasional wins confined to distribution shifts that headroom analysis explains as regularization effects reproducible by head weight decay.
- **Why Important:** Prunes an over-mythologized method category down to its real value and enforces parameter-matched adaptation comparisons.
- **Why Possibly Novel:** Parameter-matched prompt-vs-head audits across task families with shift-stratified analysis are unavailable.
- **Minimal Experiment:** Adapt 3 frozen backbones to 8 tasks with {prompts, linear, 2-layer head} at matched parameters and search budgets; compare ID and OOD.
- **Main Risk:** Very-low-parameter regimes may genuinely favor prompts, requiring a budget-resolved verdict.
- **Cluster:** NEG-HYP

### C-0255 · Semi-supervised consistency methods are obsolete under foundation features
- **One-sentence idea:** Predict that the consistency-regularization semi-supervised learning stack (FixMatch-style) adds nothing over simple fine-tuning of modern pretrained backbones on the labeled subset alone, across realistic label budgets.
- **Problem:** SSL-for-classification methods were developed against from-scratch baselines; foundation features may have absorbed their entire benefit, but the field still cites and builds on the method stack.
- **Core Hypothesis:** With DINOv2/SigLIP backbones, labeled-only fine-tuning matches FixMatch-class pipelines at label budgets above a few dozen per class, with unlabeled data helping only below that — and there, simple pseudo-labeling on frozen features suffices.
- **Why Important:** Would retire a heavily cited pipeline for most practical regimes and re-scope semi-supervised research to the extreme-low-label frontier.
- **Why Possibly Novel:** Foundation-backbone re-baselining of the semi-supervised literature has not been comprehensively published.
- **Minimal Experiment:** Compare {labeled-only FT, FixMatch, frozen-feature pseudo-labeling} across label budgets {4..256}/class on 4 datasets with modern backbones.
- **Main Risk:** Domain-shifted unlabeled pools (the realistic case) may revive consistency methods, requiring both matched and shifted unlabeled settings.
- **Cluster:** NEG-HYP

### C-0256 · Sharpness-aware minimization stops working at scale
- **One-sentence idea:** Test the null that SAM-family optimizers, celebrated on ImageNet-1k-scale training, provide no generalization benefit at large data scale — their gains being a small-data regularization effect that vanishes when data supplies the regularization.
- **Problem:** SAM doubles training cost and is being adopted into large-scale recipes on faith, while its mechanism (flatness-seeking) predicts diminishing returns as data grows — an unexamined extrapolation.
- **Core Hypothesis:** SAM's accuracy gain over tuned SGD/AdamW decays monotonically with dataset size and reaches zero before web-scale pretraining regimes, and its residual effects at scale (calibration, corruption robustness) also vanish under matched schedules.
- **Why Important:** Prevents a 2× compute tax from becoming ritual in large-scale training if it buys nothing there.
- **Why Possibly Novel:** Scale-resolved SAM audits beyond ImageNet-1k are not available; adoption is running ahead of evidence.
- **Minimal Experiment:** Train matched models with/without SAM at {1M, 10M, 100M} images; plot the gain vs. scale curve for accuracy, calibration, and robustness.
- **Main Risk:** Fine-tuning (small-data) regimes will still benefit, so scope must clearly separate pretraining from adaptation claims.
- **Cluster:** NEG-HYP

### C-0257 · "Important attention heads" are not stable objects
- **One-sentence idea:** Test whether attention-head importance rankings — the basis of head-pruning methods and mechanistic claims about specialized heads — replicate across random seeds of the same training run, predicting they largely do not.
- **Problem:** Papers ascribe stable functional identities to particular heads ("the counting head") and prune by importance scores, assuming head roles are properties of the architecture-task pair rather than accidents of one training draw.
- **Core Hypothesis:** Cross-seed overlap of top-importance head sets is barely above chance, functional roles redistribute across heads per seed while the *distribution* of roles is preserved, and pruning masks transferred across seeds destroy performance — head identity is seed-level noise.
- **Why Important:** Undermines head-level mechanistic claims made from single models and forces pruning/interpretability methods to operate on function space, not head indices.
- **Why Possibly Novel:** Seed-replication audits of head importance have not been systematically done for vision or multimodal transformers.
- **Minimal Experiment:** Train 5 seeds of a ViT; compute head importance by 3 methods; measure cross-seed rank overlap; test cross-seed transfer of pruning masks.
- **Main Risk:** Some universal heads (positional, sink) may replicate, requiring a two-population (stable core + fluid rest) description.
- **Cluster:** NEG-HYP

### C-0258 · No post-hoc calibrator survives distribution shift
- **One-sentence idea:** Run a preregistered falsification tournament testing whether any popular post-hoc calibration method (temperature scaling, vector scaling, spline, histogram binning) maintains calibration under even mild distribution shift, predicting all fail and shift-stable calibration requires different machinery.
- **Problem:** Calibration methods are validated ID, deployed OOD, and cited as reliability solutions; scattered evidence of shift-fragility has never been consolidated into a decisive comparative audit.
- **Core Hypothesis:** All standard post-hoc calibrators lose most of their ECE advantage at corruption severity 2 and can *worsen* calibration beyond severity 3, with failure magnitude predictable from the shift's effect on the confidence-accuracy relationship's shape (not just its scale).
- **Why Important:** Calibrated confidence is the interface between models and downstream decisions; knowing that current tools are ID-only changes deployment guidance everywhere.
- **Why Possibly Novel:** Comprehensive shift-resolved calibrator tournaments with mechanistic failure analysis are missing despite the topic's maturity.
- **Minimal Experiment:** Calibrate 10 models with 6 methods on ID validation; evaluate ECE/reliability curves across shift suites; model failure as a function of shift statistics.
- **Main Risk:** The conclusion could be dismissed as expected; the contribution must include the predictive failure model, not just the null.
- **Cluster:** NEG-HYP

### C-0259 · Emergent text-supervised segmentation evaporates outside object-centric images
- **One-sentence idea:** Characterize the failure conditions of "segmentation emerges from caption supervision alone" claims, predicting the emergent grouping collapses on cluttered multi-object scenes and stuff regions — the majority of real pixels — and exists mainly for centered single objects.
- **Problem:** Emergence claims are demonstrated on object-centric benchmarks (VOC-style), and the community generalizes them to "language supervision teaches segmentation" without stress tests on scene-complexity axes.
- **Core Hypothesis:** Emergent-segmentation quality degrades sharply with object count, occlusion, and off-center composition, approaching noise for stuff classes — showing the mechanism is figure-ground saliency alignment, not semantic partitioning.
- **Why Important:** Corrects an influential narrative about what caption supervision provides and redefines what dense self-emergence would actually require.
- **Why Possibly Novel:** Complexity-stratified stress evaluation of emergent-segmentation claims has not been reported.
- **Minimal Experiment:** Evaluate 3 caption-only-trained segmentation-emergence methods on splits stratified by object count/centrality/stuff-fraction; fit degradation curves.
- **Main Risk:** Newer methods may partially survive, converting the null into a boundary-mapping result (still useful).
- **Cluster:** NEG-HYP

### C-0260 · Retrieval-augmented classification gains are leakage in disguise
- **One-sentence idea:** Test the null that retrieval-augmented visual classification (retrieving similar labeled images at test time) provides no benefit once near-duplicate and same-source leakage between retrieval database and test sets is removed.
- **Problem:** RAG-for-vision reports gains using web-scale retrieval databases that plausibly contain test-set near-duplicates; the leakage-corrected value of retrieval remains unmeasured.
- **Core Hypothesis:** After embedding-level dedup between database and test data, retrieval augmentation's accuracy gain shrinks to near zero on standard benchmarks, surviving only on genuinely long-tail queries where the parametric model lacks coverage.
- **Why Important:** Establishes whether retrieval is a real capability amplifier or a benchmark-contamination amplifier — decisive for the architecture direction it motivates.
- **Why Possibly Novel:** Leakage-controlled audits of visual RAG have not been conducted; text-domain contamination lessons haven't crossed over.
- **Minimal Experiment:** Reproduce a retrieval-augmented classification pipeline; ablate database dedup at 3 similarity thresholds; decompose gains by query-frequency strata.
- **Main Risk:** Aggressive dedup may remove legitimately helpful neighbors, requiring careful threshold sensitivity analysis.
- **Cluster:** NEG-HYP

### C-0261 · Distilled datasets don't transfer across architectures
- **One-sentence idea:** Predict that dataset distillation — compressing datasets into small synthetic sets — produces sets so architecture-specific that training any architecture other than the distillation target on them fails, nullifying the "compressed dataset" interpretation.
- **Problem:** Dataset distillation is framed as extracting task-essential information, implying architecture independence, but evaluation is almost always on the architecture used during distillation.
- **Core Hypothesis:** Cross-architecture training on distilled sets loses most of the accuracy relative to same-architecture training, with the gap growing with architectural distance — distilled sets encode inductive-bias-specific optimization shortcuts, not task information.
- **Why Important:** Determines whether dataset distillation is a data-compression technology (broadly useful) or an architecture-coupled curiosity, resolving its practical trajectory.
- **Why Possibly Novel:** Cross-architecture transfer matrices for modern distillation methods are incomplete and never headline the papers.
- **Minimal Experiment:** Distill CIFAR/ImageNet-subset data with 3 methods on ViT and CNN targets; train a 5-architecture panel on each set; report the transfer matrix.
- **Main Risk:** Recent trajectory-matching methods may partially transfer, requiring method-resolved conclusions.
- **Cluster:** NEG-HYP

### C-0262 · Mixup's calibration benefit doesn't survive temperature scaling
- **One-sentence idea:** Test the null that mixup's celebrated calibration improvement is entirely reproducible by temperature scaling a mixup-free model — i.e., mixup changes confidence scale, not the confidence-accuracy relationship's informativeness.
- **Problem:** Mixup is recommended for calibration in deployment guides based on raw ECE comparisons that conflate scale miscalibration (fixable post-hoc for free) with genuine uncertainty-quality differences.
- **Core Hypothesis:** After per-model temperature scaling on identical validation data, mixup and no-mixup models show indistinguishable ECE and selective-prediction curves ID, and mixup's OOD confidence behavior (systematic underconfidence) is a liability rather than a benefit for shift detection.
- **Why Important:** Corrects deployment guidance and sharpens the standard for claiming "calibration improvements" (must survive post-hoc scaling).
- **Why Possibly Novel:** The scale-vs-shape decomposition applied specifically to mixup's calibration claims, with OOD liability analysis, is not published.
- **Minimal Experiment:** Train matched models ± mixup; compare pre- and post-temperature-scaling calibration ID, plus OOD confidence and selective risk; 5 seeds.
- **Main Risk:** Results may differ across mixup variants (cutmix, manifold), requiring the family to be covered.
- **Cluster:** NEG-HYP

### C-0263 · Spectral shortcut defenses only fix synthetic corruptions
- **One-sentence idea:** Predict that defenses removing "frequency shortcuts" (spectral filtering, frequency augmentation) improve scores on synthetic corruption benchmarks while providing zero gain on natural distribution shifts — the defenses overfit the benchmark's frequency structure rather than fixing shortcut learning.
- **Problem:** Frequency-based robustness methods validate on ImageNet-C-style suites whose corruptions live in the exact frequency bands the methods manipulate, a circularity the field has not confronted.
- **Core Hypothesis:** Across frequency-defense methods, gains on synthetic corruption suites are large while gains on natural shifts (dataset replication sets, real-world drift benchmarks) are statistically zero — with the dissociation explained by the mismatch between synthetic corruption spectra and natural shift statistics.
- **Why Important:** Warns that a whole robustness subfield may be optimizing an artifact, and pushes evaluation toward natural-shift endpoints.
- **Why Possibly Novel:** The synthetic-vs-natural gain dissociation for frequency defenses has not been measured systematically.
- **Minimal Experiment:** Evaluate 5 frequency-domain robustness methods on {ImageNet-C, ImageNet-V2/replication sets, real drift benchmarks}; compare gain profiles.
- **Main Risk:** Natural-shift benchmarks have their own quirks; needs several to make the null credible.
- **Cluster:** NEG-HYP

### C-0264 · Bigger teachers make worse students — the capacity gap survives modernity
- **One-sentence idea:** Re-test the capacity-gap phenomenon (distillation quality non-monotone in teacher size) with modern VLM/foundation teachers, predicting it persists — the biggest available teacher remains the wrong choice — against the practitioner default of always distilling from the largest model.
- **Problem:** Distillation pipelines increasingly default to frontier-scale teachers, while the old evidence that over-large teachers hurt students has not been re-validated (or refuted) for foundation-scale teachers and multimodal tasks.
- **Core Hypothesis:** Student quality peaks at intermediate teacher scale across student sizes, the optimal teacher/student ratio is roughly constant, and teacher-confidence geometry (margin structure too sharp for the student to match) mediates the effect — all replicating at VLM scale.
- **Why Important:** Direct cost savings (smaller optimal teachers) and a persistent, theoretically informative counterexample to bigger-is-better.
- **Why Possibly Novel:** The capacity-gap curve has not been mapped for the current model generation or for multimodal distillation.
- **Minimal Experiment:** Distill a fixed student from a 6-point teacher scale ladder on classification and VLM captioning tasks; map student quality vs. teacher scale.
- **Main Risk:** Modern distillation tricks (patient teaching, feature distillation) may flatten the curve, converting the result into a method-conditional map.
- **Cluster:** NEG-HYP

### C-0265 · Chain-of-thought does not improve VLM perception
- **One-sentence idea:** Test the null that chain-of-thought prompting improves multimodal *perception* accuracy (recognition, counting, OCR, localization), as opposed to multi-step reasoning tasks — predicting zero or negative effects because verbalization cannot add visual information and may overwrite it with priors.
- **Problem:** CoT is applied indiscriminately to VLM evaluation and deployment, and reported gains on mixed benchmarks may come entirely from reasoning-format items while perception items silently degrade.
- **Core Hypothesis:** On perception-isolated evaluation slices, CoT prompting changes accuracy by ≤0 on average, with degradation concentrated where language priors conflict with image evidence (the model talks itself out of correct perceptions) — while genuine multi-step items still benefit.
- **Why Important:** Establishes when inference-time verbalization is wasted or harmful compute for multimodal systems — a live deployment decision.
- **Why Possibly Novel:** Perception-vs-reasoning decomposition of multimodal CoT effects has not been cleanly published.
- **Minimal Experiment:** Evaluate 4 VLMs with/without CoT on perception-pure vs. reasoning-pure slices; analyze error flips (correct→incorrect under CoT) for prior-conflict signatures.
- **Main Risk:** CoT formats vary widely; requires several prompting styles to make the null robust.
- **Cluster:** NEG-HYP

### C-0266 · Attribution maps don't help humans debug models
- **One-sentence idea:** Run controlled user studies testing the null that providing state-of-the-art attribution maps does not improve ML practitioners' actual model-debugging performance (finding planted bugs: spurious cues, label errors, backdoors) over seeing only inputs, predictions, and confidences.
- **Problem:** The utility of explanation tools is asserted through plausibility and proxy metrics, while the field's core promise — helping humans find model defects — is almost never measured as task performance.
- **Core Hypothesis:** On a planted-defect detection task, attribution-equipped practitioners perform no better (accuracy, time) than baseline-information practitioners, with attribution sometimes inducing overconfidence in wrong hypotheses — the tools' value being narrative, not diagnostic.
- **Why Important:** Explanation tooling shapes regulatory and engineering practice; a rigorous human-utility null would force the field to design for measured debugging outcomes.
- **Why Possibly Novel:** Human-grounded evaluations exist but are small and dated; a preregistered, planted-defect study with modern tools and adequate power is missing.
- **Minimal Experiment:** Preregister a 60-participant study; plant 3 defect types in models; compare defect-finding across {baseline, attribution, attribution+training} conditions.
- **Main Risk:** User-study logistics and the dependence of results on participant expertise; requires careful power analysis.
- **Cluster:** NEG-HYP

### C-0267 · Object-centric representations don't pay off downstream
- **One-sentence idea:** Test the null that slot-based object-centric representation learning, at matched pretraining compute, provides no advantage over plain patch-based features for the downstream reasoning and prediction tasks it was designed to enable.
- **Problem:** Object-centric learning is motivated by anticipated benefits for relational reasoning and systematic generalization that are demonstrated mainly on synthetic toy environments, while patch-based baselines improve relentlessly.
- **Core Hypothesis:** On real-world relational tasks (visual relation prediction, physical dynamics forecasting, compositional VQA), frozen slot representations lose to compute-matched patch features under identical readouts, because slot bottlenecks discard information without delivering usable symbolic structure.
- **Why Important:** The object-centric agenda consumes significant research energy on a promissory note; a rigorous audit either cashes it or refocuses the agenda on where slots genuinely help.
- **Why Possibly Novel:** Matched-compute downstream audits of slot models against modern patch baselines on real (non-synthetic) tasks are rare and never comprehensive.
- **Minimal Experiment:** Pretrain slot and patch models at matched budgets; evaluate frozen representations on 5 real relational/dynamics tasks with identical probes.
- **Main Risk:** Slot methods may be under-scaled relative to their potential, inviting "not fair at this scale" objections that scale-trend analysis must address.
- **Cluster:** NEG-HYP

### C-0268 · Intermediate-task transfer is noise in vision
- **One-sentence idea:** Test the null that inserting an intermediate fine-tuning task between pretraining and target fine-tuning ("stepping-stone transfer") provides no reliable benefit for vision tasks, with published positive cases being selection effects over a distribution centered at zero.
- **Problem:** Intermediate-task recipes circulate as practical wisdom, but the vision version of the known-unstable NLP phenomenon (STILTs) has never been audited at distribution level — papers report chosen wins, not the win-rate.
- **Core Hypothesis:** Across a random sample of (intermediate, target) task pairs, the intermediate-task effect distribution is centered at zero with heavy tails in both directions, unpredictable by task-similarity heuristics — making the practice net-neutral and the literature a tail sample.
- **Why Important:** Prevents wasted adaptation compute and demonstrates, on a concrete practice, how selective reporting manufactures folklore.
- **Why Possibly Novel:** Distribution-level (not case-level) evaluation of intermediate-task transfer in vision has not been done.
- **Minimal Experiment:** Evaluate a 10×10 intermediate×target task grid with matched budgets and 3 seeds; report the full effect distribution and test similarity-heuristic predictors.
- **Main Risk:** Compute cost of the grid; effects may be regime-dependent (small target data), requiring at least two data scales.
- **Cluster:** NEG-HYP

### C-0269 · The ImageNet-transfer correlation has broken down at the frontier
- **One-sentence idea:** Test whether the historical correlation between ImageNet accuracy and downstream transfer quality — the field's core model-selection heuristic — has broken down for post-2021 high-accuracy models, predicting near-zero rank correlation within the modern frontier cohort.
- **Problem:** "Better ImageNet model = better backbone" guided a decade of choices; as top-1 saturates and training recipes overfit benchmark idiosyncrasies, the heuristic may now be dead weight, yet it still drives model selection.
- **Core Hypothesis:** Within the cohort of models above ~85% top-1, ImageNet rank predicts transfer rank at near-chance levels across diverse downstream tasks, with transfer better predicted by pretraining data composition than by benchmark accuracy — the heuristic's validity was a low-accuracy-era artifact.
- **Why Important:** Model selection affects every practitioner; certifying the heuristic's death (and replacing it) has field-wide operational value.
- **Why Possibly Novel:** The classic transfer-correlation studies predate the current frontier; a cohort-restricted re-analysis is overdue and absent.
- **Minimal Experiment:** Fine-tune 20 frontier models on 12 diverse tasks with per-model tuned recipes; compute within-cohort rank correlations; regress transfer on data-composition covariates.
- **Main Risk:** Per-model tuning fairness at this scale is laborious; correlation attenuation from restriction-of-range must be handled statistically.
- **Cluster:** NEG-HYP

### C-0270 · Confidence thresholding of pseudo-labels is no better than random keeping
- **One-sentence idea:** Test the null that the universal practice of filtering pseudo-labels by confidence threshold selects no better than randomly keeping the same volume of pseudo-labels, because confidence correlates with easiness in ways that make retained labels redundant rather than informative.
- **Problem:** Confidence filtering is the load-bearing component of self-training pipelines, assumed to trade volume for quality; but if high-confidence labels are precisely the ones the student would learn anyway, the filter adds nothing — an untested possibility.
- **Core Hypothesis:** At matched retained volume, confidence-filtered and randomly-filtered pseudo-label sets produce statistically indistinguishable students on standard semi-supervised benchmarks, with filtering's real effect being volume reduction; informativeness-aware selection (disagreement, margin-near items with verification) beats both.
- **Why Important:** The result would redirect self-training design from confidence thresholds — tuned in every pipeline — toward selection criteria that actually add information.
- **Why Possibly Novel:** The random-at-matched-volume control is conspicuously missing from self-training literature.
- **Minimal Experiment:** Run self-training on 3 benchmarks with {confidence, random, margin-based, disagreement-based} selection at matched volumes; compare student accuracy with seeds.
- **Main Risk:** The null may hold only above certain pseudo-label accuracy levels, requiring noise-regime-resolved conclusions.
- **Cluster:** NEG-HYP
## Sub-cluster EVAL-FAIL — Evaluation Protocol Failures (C-0271 – C-0300)

### C-0271 · mIoU hides boundary progress: the size-stratified re-ranking
- **One-sentence idea:** Show that mIoU is so dominated by large-region interiors that method rankings on popular segmentation benchmarks change substantially under size-stratified and boundary-weighted decompositions — meaning the field's headline metric cannot see much of what methods differ in.
- **Problem:** Methods with very different boundary behavior, small-object performance, and error structure receive nearly identical mIoU, and the community optimizes what the metric measures.
- **Core Hypothesis:** Re-scoring published-class methods with {small-object mIoU, boundary-F, interior-mIoU} produces rank reversals in a substantial fraction of closely-ranked pairs, and several "SOTA" advances are pure interior gains invisible to applications needing boundaries.
- **Why Important:** Metric myopia silently steers architecture evolution; a decomposition standard would realign optimization with application needs.
- **Why Possibly Novel:** Boundary metrics exist, but a systematic re-ranking audit of the recent literature under decomposed metrics has not been assembled.
- **Minimal Experiment:** Re-evaluate 15 public segmentation checkpoints on ADE20K/Cityscapes under 4 decomposed metrics; report rank correlation with mIoU and reversal cases.
- **Main Risk:** Checkpoint availability and reproduction fidelity for older methods.
- **Cluster:** EVAL-FAIL

### C-0272 · Preprocessing variance exceeds claimed improvements
- **One-sentence idea:** Audit the silent variation in test-time preprocessing (resize kernels, crop protocols, normalization constants, padding) across segmentation/detection codebases, quantifying how much of cross-paper "improvement" is reproducible preprocessing artifact.
- **Problem:** Papers compare numbers produced under different resize interpolations and evaluation resolutions as if protocol-equivalent, and the aggregate magnitude of this noise is unknown.
- **Core Hypothesis:** For a fixed checkpoint, legitimate preprocessing variants (bilinear-vs-bicubic, whole-image-vs-sliding-window, ±resolution rounding) span an accuracy range comparable to typical claimed SOTA margins, and specific popular codebases embed systematically favorable choices.
- **Why Important:** Establishes the field's protocol-noise floor and motivates standardized evaluation containers — cheap fixes with large validity payoff.
- **Why Possibly Novel:** Preprocessing sensitivity is folklore; its systematic quantification against the distribution of claimed margins is missing.
- **Minimal Experiment:** Evaluate 5 checkpoints under a factorial grid of 24 legitimate preprocessing variants; compare the spread against margins claimed in 30 recent papers.
- **Main Risk:** Codebase archaeology is tedious; some variants may be judged "illegitimate" contentiously, requiring transparent variant taxonomies.
- **Cluster:** EVAL-FAIL

### C-0273 · A decade of COCO AP progress: recognition or localization?
- **One-sentence idea:** Decompose the last decade of COCO detection AP improvements into localization-quality gains versus classification/recognition gains, testing the hypothesis that recent progress is almost entirely localization refinement — a much narrower achievement than "better object understanding."
- **Problem:** AP conflates whether a detector recognizes objects better or draws boxes tighter, so the field's progress narrative rests on an unexamined mixture.
- **Core Hypothesis:** Using localization-insensitive scoring (AP at IoU 0.3) and classification-error decomposition tools, most post-2019 AP gains come from tighter localization and duplicate suppression, while category-recognition errors have barely moved — implying claimed understanding progress is largely geometric polish.
- **Why Important:** Correct progress attribution redirects research toward the stagnant component and recalibrates claims about detection being "solved."
- **Why Possibly Novel:** Error-decomposition tools exist (TIDE-style) but have not been applied longitudinally to audit the decade's progress narrative.
- **Minimal Experiment:** Run error decomposition on 12 detectors spanning 2015–2025 at matched backbones where possible; plot component-wise error trajectories over time.
- **Main Risk:** Backbone/data confounds across eras require careful matched subsets to isolate detector-head progress.
- **Cluster:** EVAL-FAIL

### C-0274 · Exact-name matching punishes correct open-vocabulary predictions
- **One-sentence idea:** Quantify how much open-vocabulary segmentation/detection evaluation, which requires predicting the benchmark's exact class-name token, penalizes semantically correct predictions (synonyms, hypernyms), and show that semantic-similarity-aware scoring changes method rankings.
- **Problem:** Open-vocab methods are scored by matching predicted embeddings to a fixed name list, so a model calling a "couch" a "sofa" scores zero — evaluation measures vocabulary-choice alignment, not visual correctness.
- **Core Hypothesis:** A nontrivial fraction of scored "errors" are lexical mismatches (verifiable by human audit), the mismatch rate differs systematically across methods (penalizing models with richer vocabularies), and soft semantic scoring reorders published comparisons.
- **Why Important:** The bias punishes exactly the models open-vocabulary research is trying to build, distorting the subfield's selection pressure.
- **Why Possibly Novel:** Lexical-mismatch audits with rank-impact analysis have not been performed on open-vocab dense benchmarks.
- **Minimal Experiment:** Human-audit 2K "errors" from 4 open-vocab methods for semantic correctness; implement WordNet/embedding-based soft scoring; re-rank methods.
- **Main Risk:** Soft scoring introduces its own contestable similarity choices; must show conclusions robust across similarity sources.
- **Cluster:** EVAL-FAIL

### C-0275 · Center-crop evaluation conceals aspect-ratio brittleness
- **One-sentence idea:** Show that the standard center-crop/resize evaluation protocol hides systematic failures on natural aspect ratios and compositions, and that model rankings shift when evaluation preserves native geometry — the protocol having quietly shaped models toward crop-world statistics.
- **Problem:** Virtually all classification evaluation crops to squares at fixed size, so models are never scored on the geometric diversity of real deployment inputs, and protocol-induced blind spots go unmeasured.
- **Core Hypothesis:** Evaluating with native aspect ratios (padded or variable-size inference) drops accuracy non-uniformly across models — architectures with strong learned center biases and square-position priors degrade most — reordering closely ranked models and revealing a protocol-fitted monoculture.
- **Why Important:** Deployment inputs are not center crops; a protocol that trained the field toward them is a validity failure worth measuring precisely.
- **Why Possibly Novel:** Aspect-ratio-preserving re-evaluation at scale, with ranking impact and bias attribution, has not been published.
- **Minimal Experiment:** Re-evaluate 20 classifiers under {center-crop, full-image padded, native-resolution} protocols on ImageNet and a native-geometry test set; analyze rank shifts and positional-bias correlates.
- **Main Risk:** Models legitimately trained for crops may be unfairly judged; the study must frame results as deployment-validity, not cheating.
- **Cluster:** EVAL-FAIL

### C-0276 · The many ADE20Ks: split drift breaks cross-paper comparability
- **One-sentence idea:** Document how nominally identical benchmarks (ADE20K, Cityscapes, COCO variants) exist in silently divergent versions across codebases — different label mappings, ignored-class conventions, split files, and annotation revisions — and quantify the cross-paper comparability error this creates.
- **Problem:** Papers cite "ADE20K mIoU" as a common currency while inheriting different dataset-loading conventions from different frameworks, making numerical comparison across papers partly meaningless — with unknown magnitude.
- **Core Hypothesis:** Evaluating one fixed checkpoint through 6 popular framework pipelines yields mIoU differences up to several points from convention drift alone (label remapping, void handling, resolution defaults), exceeding many claimed improvements.
- **Why Important:** Establishes the cross-paper noise floor and motivates checksummed benchmark definitions — infrastructure with immediate field-wide value.
- **Why Possibly Novel:** Framework-drift quantification with a fixed-checkpoint methodology has not been published despite widespread suspicion.
- **Minimal Experiment:** Run 3 checkpoints through {mmseg, detectron2, custom-paper repos} evaluation stacks; diff every convention; attribute score differences to specific conventions.
- **Main Risk:** Findings may embarrass specific codebases; requires careful, neutral presentation focused on fixes.
- **Cluster:** EVAL-FAIL

### C-0277 · Boundary-tolerant metrics reward strategic hedging
- **One-sentence idea:** Show that boundary-tolerant evaluation conventions (void bands around ground-truth boundaries, tolerance radii) are gameable: models can gain benchmark points by strategically hedging predictions in tolerance zones without any real boundary improvement.
- **Problem:** Tolerance conventions were designed to absorb annotation noise, but they also define an exploit surface that trained models may already be using — and that explicit optimization could abuse — undermining boundary-quality claims.
- **Core Hypothesis:** A post-processing step that adaptively reshapes predictions within tolerance zones (without new information) improves benchmark boundary scores measurably, and some existing methods' boundary gains shrink substantially under tolerance-zero audited evaluation with uncertainty-aware ground truth.
- **Why Important:** If tolerance zones are exploitable, boundary-progress claims need audited metrics — before leaderboard optimization discovers the exploit at scale.
- **Why Possibly Novel:** Gameability analysis of dense-metric tolerance conventions has not been conducted.
- **Minimal Experiment:** Implement tolerance-zone-aware post-processing; measure score gains across metrics/benchmarks; re-evaluate published methods with multi-annotator boundary uncertainty as reference.
- **Main Risk:** Multi-annotator boundary ground truth is scarce, requiring some new annotation for the audit reference.
- **Cluster:** EVAL-FAIL

### C-0278 · Same mIoU, opposite reliability: dense metrics ignore calibration
- **One-sentence idea:** Demonstrate that segmentation models with indistinguishable mIoU differ drastically in pixelwise confidence reliability (calibration, selective-prediction value), and propose reliability-adjusted dense evaluation that reorders methods for safety-relevant use.
- **Problem:** Dense benchmarks score only argmax masks, so the confidence quality that downstream consumers (fusion, planning, human review) depend on is invisible to the metrics driving model selection.
- **Core Hypothesis:** Among mIoU-matched model pairs, pixel-level selective risk at fixed coverage differs by large factors, rankings under reliability-weighted metrics disagree strongly with mIoU rankings, and popular training tricks (heavy augmentation, OHEM) trade invisible reliability for visible mIoU.
- **Why Important:** Safety-critical adopters currently select models on a metric blind to the property they need most.
- **Why Possibly Novel:** Dense-prediction calibration exists as a topic, but the ranking-disagreement audit and a proposed standard reliability-adjusted protocol do not.
- **Minimal Experiment:** Evaluate 12 mIoU-comparable segmenters on calibration/selective-prediction suites ID and OOD; publish dual-axis rankings and trick-level attributions.
- **Main Risk:** Reliability metrics have design freedom; conclusions must be robust across several formulations.
- **Cluster:** EVAL-FAIL

### C-0279 · How much of SOTA is inference protocol?
- **One-sentence idea:** Quantify the fraction of claimed state-of-the-art margins in segmentation/detection attributable to inference-time protocol choices (multi-scale testing, flipping, sliding-window overlap, threshold tuning) rather than to the proposed methods, via a protocol-normalized re-evaluation of recent leaderboard entries.
- **Problem:** Papers mix single-scale and heavily-ensembled inference in headline tables, and reviewers cannot see how much of each margin is protocol; the aggregate distortion across the literature is unmeasured.
- **Core Hypothesis:** Under protocol-normalized evaluation (fixed single-scale, no TTA, fixed thresholds), a substantial fraction of recent SOTA margins shrink below significance, and protocol contributions are systematically larger for papers with smaller methodological deltas.
- **Why Important:** Separates method progress from evaluation-time compute spending, enabling honest comparisons and better reviewing norms.
- **Why Possibly Novel:** Individual protocol effects are known; the literature-scale accounting of protocol-vs-method contributions is not.
- **Minimal Experiment:** Reproduce 10 recent SOTA results with and without their inference protocols; decompose each margin; correlate protocol share with method-novelty ratings.
- **Main Risk:** Reproduction burden; authors may dispute normalized settings, requiring published per-protocol matrices rather than one verdict.
- **Cluster:** EVAL-FAIL

### C-0280 · VQA string matching fails modern generative answers
- **One-sentence idea:** Measure the "paraphrase penalty" that exact-match and consensus-based VQA metrics impose on modern generative VLMs (correct answers phrased differently), and show metric choice — not capability — explains a meaningful share of cross-model ranking on legacy VQA benchmarks.
- **Problem:** Legacy VQA metrics were designed for short classification-style answers; generative models produce correct long-form answers that score zero, and the field mixes results across scoring eras.
- **Core Hypothesis:** Human-audited correct-but-mismatched answer rates differ systematically across models (penalizing more fluent models), semantic scoring (entailment or LLM-judged with bias controls) changes model rankings, and part of reported "instruction-tuning gains" on VQA is metric-fitting to short answers.
- **Why Important:** Corrects capability comparisons that inform model choices, and cleans up longitudinal progress claims contaminated by metric-fit effects.
- **Why Possibly Novel:** Paraphrase-penalty quantification with rank-impact and metric-fitting analysis has not been done comprehensively for the generative-VLM era.
- **Minimal Experiment:** Human-audit 3K mismatched answers from 6 VLMs on VQAv2/OK-VQA; compare rankings under exact, entailment-based, and audited scoring; measure answer-length vs. penalty correlation.
- **Main Risk:** LLM-based semantic scoring imports its own biases; the audit must anchor on human judgments.
- **Cluster:** EVAL-FAIL

### C-0281 · Judge models prefer confident verbosity — and it reorders leaderboards
- **One-sentence idea:** Quantify verbosity, confidence-phrasing, and style biases of LLM/VLM judges used in multimodal evaluation, and measure how much of current leaderboard ordering is explained by bias-susceptible presentation rather than content correctness.
- **Problem:** Multimodal leaderboards increasingly rely on model judges whose biases are documented anecdotally but not propagated into an accounting of how rankings would change under bias-controlled judging.
- **Core Hypothesis:** Controlled rewrites (same content, varied length/hedging/format) shift judge scores by margins comparable to inter-model gaps; bias-corrected judging (content-extraction before scoring, length-matched comparisons) reorders mid-leaderboard models substantially.
- **Why Important:** Judge-based evaluation is becoming the field's primary instrument; uncorrected style biases let models win by rhetoric.
- **Why Possibly Novel:** Bias existence is known; the rank-impact quantification with a validated correction protocol for multimodal judging is missing.
- **Minimal Experiment:** Build content-matched style-varied response sets; measure judge score sensitivity; apply corrected protocols to a real leaderboard's response data; report ordering changes.
- **Main Risk:** Correction protocols may overcorrect (penalizing legitimately better-communicated answers), requiring human-anchored validation.
- **Cluster:** EVAL-FAIL

### C-0282 · Benchmark images live inside the pretraining corpus
- **One-sentence idea:** Measure the contamination rate of popular multimodal benchmarks (test images or near-duplicates present in public pretraining corpora), and produce decontaminated re-rankings testing whether contamination advantages differ across models.
- **Problem:** Web-pretrained models are evaluated on benchmarks partially embedded in their training distributions, and vision-side contamination accounting (image near-duplicates, not just text) is largely absent.
- **Core Hypothesis:** Contamination rates for several popular benchmarks are substantial, per-item performance on contaminated items is measurably inflated, and models differ in contamination benefit according to their corpus overlap — shifting decontaminated rankings.
- **Why Important:** Contamination-adjusted evaluation is a validity requirement as corpora and benchmarks increasingly share sources.
- **Why Possibly Novel:** Systematic image-level (embedding-based) contamination audits across multimodal benchmarks with re-ranking are missing.
- **Minimal Experiment:** Run scalable near-duplicate detection between 6 benchmarks and LAION-scale indexes; compare per-model performance on contaminated vs. clean partitions; publish clean subsets.
- **Main Risk:** Near-duplicate thresholds are contestable; requires sensitivity analysis and human verification samples.
- **Cluster:** EVAL-FAIL

### C-0283 · Few-shot rankings are episode-sampling noise
- **One-sentence idea:** Perform a power analysis of few-shot evaluation protocols showing that the episode counts standard in the literature yield confidence intervals wider than typical claimed method differences — making a substantial fraction of few-shot leaderboard ordering statistical noise.
- **Problem:** Few-shot results depend on random support-set draws, and papers report means over episode counts chosen by convention, without power calculations tied to the effect sizes they claim.
- **Core Hypothesis:** Reproducing popular few-shot comparisons with 100× episodes shows that many published differences fall within episode-sampling noise; per-episode paired testing reverses some established orderings; support-set composition explains more variance than method identity.
- **Why Important:** The few-shot literature's comparative claims need a noise floor; establishing it cheaply raises reporting standards.
- **Why Possibly Novel:** Variance decomposition (episode vs. seed vs. method) with power-analysis prescriptions has not been standard or published at audit scale.
- **Minimal Experiment:** Re-run 8 few-shot methods on standard benchmarks with massive episode counts and paired-episode statistics; publish variance decompositions and required-episode tables.
- **Main Risk:** Mostly computational; results may be dismissed as "known" despite never being quantified — framing must emphasize the concrete false-positive rate.
- **Cluster:** EVAL-FAIL

### C-0284 · Corruption severity levels are not comparable across corruption types
- **One-sentence idea:** Show that the severity calibration of standard corruption-robustness benchmarks is inconsistent across corruption types (severity 3 fog ≠ severity 3 noise in any perceptual or informational sense), so aggregate robustness scores hide arbitrary weightings and re-normalization changes model rankings.
- **Problem:** Mean corruption error averages over severities whose cross-type equivalence was set heuristically; models optimized for the suite inherit its arbitrary difficulty allocation.
- **Core Hypothesis:** Normalizing severities by human-recognizability or information-theoretic degradation changes per-type weightings enough to reorder robustness leaderboards, and some "robust" methods win primarily on over-weighted corruption types.
- **Why Important:** Robustness rankings guide method adoption; ranking sensitivity to arbitrary calibration constants is a validity flaw with a constructive fix.
- **Why Possibly Novel:** Severity-recalibration audits with human-anchored difficulty equating have not been applied to the corruption-benchmark ecosystem.
- **Minimal Experiment:** Collect human recognition rates across the corruption×severity grid; re-normalize; re-rank 20 models under equated difficulty; identify weighting-sensitive methods.
- **Main Risk:** Human-difficulty anchoring is one of several defensible normalizations; conclusions must be stable across at least two.
- **Cluster:** EVAL-FAIL

### C-0285 · "Zero-shot" cross-dataset evaluation hides target tuning
- **One-sentence idea:** Audit the open secret that "zero-shot" cross-dataset segmentation/detection evaluations use hyperparameters (score thresholds, mask-fusion settings, prompt templates) tuned on the target benchmark, quantifying how much reported zero-shot performance depends on this hidden supervision.
- **Problem:** Cross-dataset transfer results claim no target-domain adaptation while their inference hyperparameters were selected using target-domain scores — an inconsistency of unknown aggregate magnitude.
- **Core Hypothesis:** Choosing inference hyperparameters strictly on source-domain validation drops reported "zero-shot" numbers by several points non-uniformly across methods, reordering comparisons and revealing which methods are genuinely transferable versus threshold-brittle.
- **Why Important:** Honest zero-shot protocols are essential for the field's central claims about open-world readiness.
- **Why Possibly Novel:** The hidden-tuning audit with source-only protocol enforcement has not been performed across the open-vocabulary literature.
- **Minimal Experiment:** Re-evaluate 6 open-vocab methods with source-tuned vs. target-tuned inference settings; report per-method sensitivity and rank changes.
- **Main Risk:** Reconstructing what each paper tuned requires author correspondence or careful code archaeology.
- **Cluster:** EVAL-FAIL

### C-0286 · Benchmarks punish models for being more precise than the ontology
- **One-sentence idea:** Quantify how flat-label evaluation penalizes predictions that are correct at a finer granularity than the benchmark ontology ("oak" scored wrong against "tree"), and show hierarchy-aware scoring changes both rankings and the apparent scaling behavior of open-vocabulary models.
- **Problem:** As models' vocabularies outgrow benchmark ontologies, an increasing share of scored errors are granularity mismatches, systematically penalizing the most knowledgeable models — a bias growing over time and unmeasured.
- **Core Hypothesis:** Granularity-mismatch errors constitute a rising fraction of "errors" for newer models (auditable by humans), hierarchy-aware metrics restore credit non-uniformly across models, and some claimed capability plateaus in scaling curves flatten because of this ceiling artifact rather than capability saturation.
- **Why Important:** Mismeasured scaling behavior misleads the field's core narratives; the fix (hierarchy-aware scoring) is implementable today.
- **Why Possibly Novel:** Hierarchical metrics exist, but the longitudinal bias analysis (newer models punished more) and scaling-curve correction have not been done.
- **Minimal Experiment:** Audit granularity mismatches across model generations on ImageNet/ADE evaluations; implement WordNet-hierarchy scoring; re-plot scaling curves under both metrics.
- **Main Risk:** Hierarchy choice injects its own ontology commitments; requires multi-hierarchy robustness checks.
- **Cluster:** EVAL-FAIL

### C-0287 · Panoptic Quality's arithmetic drives architecture choices
- **One-sentence idea:** Analyze how the specific arithmetic of the Panoptic Quality metric (hard 0.5-IoU matching, equal thing/stuff averaging, small-segment sensitivity) has steered panoptic architecture evolution, and show that defensible alternative formulations reorder methods and would have favored different designs.
- **Problem:** PQ's design choices were pragmatic, but the metric became the selection pressure for a whole subfield without analysis of which methodological "progress" is metric-arithmetic fitting.
- **Core Hypothesis:** Method rankings are unstable across defensible PQ variants (soft matching, area-weighted, boundary-aware), the instability localizes to specific design features (e.g., segment-splitting behavior), and several architectural trends (proposal-free vs. proposal-based) trace to PQ arithmetic rather than task quality.
- **Why Important:** Demonstrates concretely how metric design becomes architecture destiny, and provides a better-grounded evaluation basis for unified segmentation.
- **Why Possibly Novel:** Metric-sensitivity analysis linked to historical architecture selection has not been performed for panoptic segmentation.
- **Minimal Experiment:** Re-score 10 panoptic methods under 5 PQ variants; identify rank instabilities; correlate design features with per-variant advantages.
- **Main Risk:** Counterfactual history claims ("architectures would have differed") must be carefully hedged as selection-pressure analysis.
- **Cluster:** EVAL-FAIL

### C-0288 · Humans disagree with mIoU about which segmentation is better
- **One-sentence idea:** Run controlled human studies comparing perceived segmentation quality against metric rankings, testing whether mIoU-preferred outputs are actually preferred by application-representative human judges — and derive a perceptual segmentation metric from the disagreement structure.
- **Problem:** Dense metrics were chosen for computability, not validated against human quality judgments; if rankings disagree with human preferences, leaderboards optimize away from perceived quality.
- **Core Hypothesis:** Human preferences weight boundary cleanliness, semantic coherence of errors (plausible vs. absurd label choices), and object completeness far more than area-proportional accuracy, producing frequent human-vs-mIoU ranking disagreements that a learned perceptual metric can predict.
- **Why Important:** For human-facing applications (editing, AR, medical review), the current metric provably optimizes the wrong target if the disagreement is confirmed.
- **Why Possibly Novel:** Perceptual-metric validation is standard in image generation but essentially absent for semantic segmentation evaluation.
- **Minimal Experiment:** Collect pairwise human preferences over 2K output pairs (matched mIoU, differing error structure); model preference drivers; test a learned metric's ranking agreement with humans vs. mIoU's.
- **Main Risk:** Preference depends on application framing given to raters; requires multiple framings for generality.
- **Cluster:** EVAL-FAIL

### C-0289 · Meta-benchmark rankings collapse under dataset reweighting
- **One-sentence idea:** Test the stability of multi-dataset meta-benchmark conclusions (VTAB-style suites, multimodal leaderboard aggregates) under defensible reweightings of constituent datasets, hypothesizing that many headline model orderings invert within the space of reasonable weights.
- **Problem:** Aggregate scores implicitly weight datasets (usually uniformly), an arbitrary choice that determines winners without ever being defended or stress-tested.
- **Core Hypothesis:** For current multimodal and transfer meta-benchmarks, the fraction of model pairs whose ordering is weight-invariant is small; published rankings live in a narrow weighting region; and dataset-cluster structure (many near-duplicate datasets) silently multiplies some capabilities' effective weight.
- **Why Important:** Meta-benchmark conclusions drive model selection and narrative ("model X is best overall"); their fragility should be a reported property, not a discovery by users.
- **Why Possibly Novel:** Weight-perturbation stability analysis with duplicate-cluster correction has not been applied to the field's aggregate leaderboards.
- **Minimal Experiment:** For 3 meta-benchmarks, compute ranking stability over weight simplex samples; cluster constituent datasets by score correlation; report effective-capability weights and invariant conclusions.
- **Main Risk:** All-weightings-equal analysis can be attacked as too permissive; needs principled weight-region definitions.
- **Cluster:** EVAL-FAIL

### C-0290 · Measuring leaderboard overfitting with fresh replication sets
- **One-sentence idea:** Construct fresh, protocol-matched replication test sets for detection/segmentation benchmarks and measure the "adaptive overfitting" gap — how much published method rankings and margins shrink on data nobody could have tuned against.
- **Problem:** Years of leaderboard iteration (threshold tuning, ablation selection, architecture search against val/test feedback) may have overfit the community to specific test sets; classification-era replication studies found rank preservation, but dense tasks with their many tunable inference knobs have never been audited.
- **Core Hypothesis:** On replication sets, absolute performance drops uniformly but *margins between methods compress substantially*, with the compression largest for methods whose gains came from inference-knob tuning — dense-task leaderboards carry more adaptive overfitting than classification ones did.
- **Why Important:** Quantifies how much reported progress survives contact with genuinely fresh data — the field's most basic validity question.
- **Why Possibly Novel:** Replication-set methodology has not been applied to detection/segmentation benchmarks.
- **Minimal Experiment:** Collect and annotate 2K-image COCO-protocol and 500-image Cityscapes-protocol replication sets; evaluate 15 public methods; compare margin structures against original test sets.
- **Main Risk:** Annotation cost and distribution-matching fidelity of the replication sets are the hard parts, requiring careful collection protocols.
- **Cluster:** EVAL-FAIL

### C-0291 · How much of referring-expression benchmarks is solvable blind?
- **One-sentence idea:** Quantify the fraction of referring-expression and grounding benchmarks solvable without the image — from expression statistics and dataset priors alone — and publish prior-resistant splits that force genuine visual grounding.
- **Problem:** Grounding benchmarks contain degenerate items ("the man" with one man) whose prevalence sets an un-reported performance floor, inflating both absolute numbers and possibly method differences.
- **Core Hypothesis:** A text-only model with access to dataset statistics (object-location priors, expression-to-box regularities) achieves a substantial fraction of reported grounding performance; filtering prior-solvable items shrinks method gaps and reorders some comparisons.
- **Why Important:** Grounding claims underpin multimodal-understanding narratives; measuring the blind-solvable floor is prerequisite to interpreting any score.
- **Why Possibly Novel:** Blind baselines exist for VQA; the systematic grounding-benchmark version with released prior-resistant splits does not.
- **Minimal Experiment:** Train text+prior-only predictors on RefCOCO-family training sets; measure test performance; release filtered evaluation subsets and re-rank published models.
- **Main Risk:** Aggressive filtering may bias remaining items toward specific phenomena, requiring documentation of the filtered distribution.
- **Cluster:** EVAL-FAIL

### C-0292 · The best-checkpoint convention quietly inflates results
- **One-sentence idea:** Quantify the inflation introduced by reporting the best checkpoint/epoch selected using test (or reused-validation) performance — a widespread quiet practice — and measure its aggregate effect on the field's reported margins.
- **Problem:** Papers rarely state checkpoint-selection protocols; selecting among many checkpoints on evaluation data is multiple testing that inflates scores, with unknown field-level magnitude.
- **Core Hypothesis:** For typical training runs, best-of-N-checkpoints selection on evaluation data inflates results by an amount comparable to seed noise and to many claimed margins, the inflation grows with evaluation-set smallness and checkpoint count, and a survey of released training logs reveals the practice's prevalence.
- **Why Important:** A quantified inflation constant and prevalence estimate convert a suspected bad practice into an actionable reviewing standard.
- **Why Possibly Novel:** Checkpoint-selection inflation has not been measured systematically for vision workloads, nor its prevalence surveyed.
- **Minimal Experiment:** Simulate selection protocols over dense checkpoint grids for 6 tasks; derive inflation curves; audit public repos/logs for selection-protocol evidence.
- **Main Risk:** Prevalence auditing depends on incomplete public information; prevalence claims must be appropriately bounded.
- **Cluster:** EVAL-FAIL

### C-0293 · Rare-class sample sizes make many mIoU gains statistically void
- **One-sentence idea:** Show that per-class IoU estimates for rare classes in standard benchmarks rest on so few test regions that their confidence intervals span several points of mIoU, and a substantial fraction of claimed improvements is attributable to statistically insignificant rare-class fluctuations.
- **Problem:** mIoU averages per-class scores with wildly unequal support (some classes appear in a handful of test images), and papers never propagate this uncertainty into headline comparisons.
- **Core Hypothesis:** Bootstrap confidence intervals on benchmark mIoU are wide enough that many recent SOTA claims are within noise, the noise is dominated by identifiable low-support classes, and reporting support-weighted or CI-aware comparisons changes the set of "significant" improvements substantially.
- **Why Important:** Adds the missing error bars to the field's most-used dense metric, with immediate reviewing implications.
- **Why Possibly Novel:** Class-support uncertainty propagation into benchmark-level comparisons has not been standard or systematically retrofitted onto the literature.
- **Minimal Experiment:** Bootstrap per-class and aggregate mIoU for 10 model pairs on ADE20K/Cityscapes; classify claimed margins by significance; identify the high-variance class sets.
- **Main Risk:** Bootstrap validity over correlated regions needs careful design (image-level resampling).
- **Cluster:** EVAL-FAIL

### C-0294 · Depth metrics have stopped measuring depth quality
- **One-sentence idea:** Demonstrate that saturated threshold-based depth-estimation metrics (δ<1.25 family) no longer discriminate among modern monocular depth models whose errors are structural (planes, boundaries, scale drift), and that structure-sensitive evaluation reorders current methods.
- **Problem:** Depth leaderboards report near-ceiling threshold accuracies while models differ visibly in geometric fidelity — the metrics reward per-pixel closeness and ignore the structured errors that break downstream 3D use.
- **Core Hypothesis:** Under structure-aware metrics (planarity preservation, occlusion-boundary accuracy, metric-scale consistency across depth ranges), current model rankings differ markedly from threshold-metric rankings, and recent "improvements" concentrate in already-saturated components.
- **Why Important:** Depth feeds robotics/AR pipelines whose failures trace to exactly the structural errors current metrics can't see.
- **Why Possibly Novel:** Structure-stratified re-ranking audits of the modern monocular-depth generation have not been consolidated.
- **Minimal Experiment:** Re-evaluate 10 depth models on NYU/KITTI with a structural metric battery; compare rankings; correlate structural scores with downstream task success (novel-view or grasping proxies).
- **Main Risk:** Structural metrics require careful definitions to avoid substituting one arbitrary weighting for another.
- **Cluster:** EVAL-FAIL

### C-0295 · Simulated clicks misrank interactive segmentation methods
- **One-sentence idea:** Test whether the simulated-click protocols used to evaluate interactive segmentation (center-of-error-region clicking) produce method rankings that disagree with rankings under real human clicking behavior, invalidating the simulation as a selection instrument.
- **Problem:** Interactive methods are developed and ranked entirely against idealized click simulators, though human click distributions (near boundaries, hesitant, imprecise) differ systematically — the sim-to-human ranking gap is unmeasured.
- **Core Hypothesis:** Human-user evaluations reorder simulator-ranked methods because some methods overfit simulator click geometry, and a human-calibrated click model (fitted from logged interactions) restores ranking agreement — providing a fixed evaluation instrument.
- **Why Important:** The entire subfield's progress signal depends on simulator fidelity; a demonstrated misranking would redirect both evaluation and method design.
- **Why Possibly Novel:** Sim-vs-human ranking validity for interactive segmentation has not been established despite universal reliance on simulation.
- **Minimal Experiment:** Run 40-participant studies over 6 interactive methods; compare NoC (clicks-to-quality) rankings against simulator rankings; fit and validate a human click model.
- **Main Risk:** Human-study variance requires careful power planning; UI confounds must be standardized across methods.
- **Cluster:** EVAL-FAIL

### C-0296 · Compositionality benchmarks may measure artifact exploitation
- **One-sentence idea:** Audit vision-language compositionality benchmarks (binding, word-order tests) for statistical artifacts (caption plausibility asymmetries, image-quality cues) that allow high scores without compositional understanding, and construct artifact-controlled versions measuring how much reported "compositionality" survives.
- **Problem:** Compositionality scores are interpreted as measuring binding ability, but hard-negative construction pipelines can leak superficial cues (unnatural captions detectable by language priors alone), inflating or deflating scores for reasons unrelated to composition.
- **Core Hypothesis:** Text-only and image-only baselines solve a substantial fraction of items on popular compositionality suites; artifact-controlled item construction (plausibility-matched negatives) reduces model-human gaps and changes cross-model comparisons — revising the field's "VLMs can't compose" narrative in both directions.
- **Why Important:** Compositionality is a headline capability claim; its measurement validity determines a major research agenda's factual basis.
- **Why Possibly Novel:** Artifact audits exist for individual benchmarks; a systematic cross-suite audit with controlled reconstruction and re-ranking does not.
- **Minimal Experiment:** Run modality-ablated baselines on 5 compositionality benchmarks; identify artifact signatures; rebuild 2 suites with plausibility-matched negatives; re-evaluate model panels.
- **Main Risk:** Constructing genuinely artifact-free negatives is hard; the contribution must include validated construction protocols.
- **Cluster:** EVAL-FAIL

### C-0297 · How far out-of-distribution are "OOD" benchmarks, really?
- **One-sentence idea:** Measure the effective distributional distance between training corpora and the benchmarks used to claim OOD robustness, testing whether celebrated "OOD generalization" results actually operate at small effective shifts for web-pretrained models — and recalibrate robustness claims per unit of measured shift.
- **Problem:** OOD benchmarks were defined relative to ImageNet-1k-era training; for web-scale-pretrained models, sketch/rendition styles are abundantly in-distribution, making "OOD robustness" claims incommensurable across model generations.
- **Core Hypothesis:** Embedding-space and density-based shift measures show popular OOD sets lie close to web pretraining distributions, per-unit-shift robustness (slope of accuracy vs. measured shift) reveals much smaller differences between models than raw OOD accuracy suggests, and some robustness "progress" is pure distribution coverage.
- **Why Important:** Distinguishes robustness mechanisms from data coverage — the central confound in the scaling-era robustness literature — with a reusable measurement protocol.
- **Why Possibly Novel:** Shift-magnitude-normalized robustness accounting across model generations has not been operationalized.
- **Minimal Experiment:** Estimate train-test shift measures for 10 models × 8 "OOD" benchmarks; plot accuracy-vs-shift curves; compare slope-based and raw robustness rankings.
- **Main Risk:** Shift measurement itself is model-dependent; requires triangulation across several estimators to be credible.
- **Cluster:** EVAL-FAIL

### C-0298 · First-frame protocols conflate segmentation with tracking
- **One-sentence idea:** Decompose video-object-segmentation evaluation to show that the standard first-frame-mask protocol mixes two abilities — appearance re-identification and mask propagation quality — such that methods ranked identically overall differ drastically per ability, and applications need the decomposed report.
- **Problem:** VOS benchmarks output single scores under which propagation-strong/re-detection-weak methods tie with their opposites, so users cannot select methods for their failure profile (occlusion recovery vs. boundary drift).
- **Core Hypothesis:** An evaluation decomposition using controlled probes (occlusion events, re-entry, appearance change vs. static high-detail segments) reveals orthogonal ability axes across current methods, predicts application-specific performance better than aggregate scores, and shows recent progress concentrated on one axis only.
- **Why Important:** Ability-resolved evaluation changes both method selection and where research effort goes in video segmentation.
- **Why Possibly Novel:** Event-stratified decomposition of VOS scores with orthogonality analysis has not been standardized.
- **Minimal Experiment:** Annotate event types (occlusion, re-entry, deformation) in DAVIS/YouTube-VOS; re-score 10 methods per event class; test orthogonality and re-rank per application profile.
- **Main Risk:** Event annotation is subjective at boundaries; requires clear taxonomies and inter-annotator checks.
- **Cluster:** EVAL-FAIL

### C-0299 · Instance-segmentation AP rewards duplicate-guessing
- **One-sentence idea:** Analyze how mask-AP's handling of ranked predictions rewards strategic duplicate and near-duplicate guessing (confidence-ordered variants of the same object), quantify how much current methods exploit this, and propose duplicate-penalized AP that changes rankings.
- **Problem:** AP evaluates a ranked list where extra low-confidence guesses can only help, so architectures and post-processing evolve toward benchmark-optimal over-prediction that applications (which consume thresholded outputs) never see the benefit of.
- **Core Hypothesis:** Modern instance segmenters emit measurable duplicate-guess mass that inflates AP relative to thresholded-output quality; the inflation differs across method families (query-based vs. NMS-based); and fixed-budget or duplicate-penalized metrics reorder methods toward those with deployable output behavior.
- **Why Important:** The metric-deployment mismatch means leaderboard winners may be practically worse — a concrete, fixable evaluation failure.
- **Why Possibly Novel:** Duplicate-exploitation accounting and its family-differential analysis have not been quantified for the modern query-based era.
- **Minimal Experiment:** Measure AP vs. fixed-threshold F-scores for 10 methods; ablate duplicate-guess mass; evaluate under duplicate-penalized AP variants; report rank changes.
- **Main Risk:** Defining "duplicates" for soft masks requires care; several defensible definitions should agree for a robust conclusion.
- **Cluster:** EVAL-FAIL

### C-0300 · The field's false-discovery rate is measurable
- **One-sentence idea:** Estimate the aggregate false-discovery rate of one year of segmentation/detection SOTA claims by systematically re-running a random sample of published improvements with proper seed statistics, matched tuning, and held-out evaluation — turning meta-scientific criticism into a measured quantity.
- **Problem:** Individual audits find specific fragile claims, but the field lacks an estimate of what fraction of its published improvements are real — the single number that would calibrate how to read the literature.
- **Core Hypothesis:** A meaningful fraction (plausibly 30–60%) of sampled claimed improvements fail to replicate at significance under matched-budget re-evaluation, failure probability is predictable from paper features (margin size, absence of error bars, single-benchmark evaluation), and the predictive model transfers to unsampled papers.
- **Why Important:** A measured FDR with risk predictors changes reviewing standards, replication incentives, and how practitioners triage the literature.
- **Why Possibly Novel:** Sampled-replication FDR estimation has been done in other sciences but never executed for modern computer vision benchmarks.
- **Minimal Experiment:** Randomly sample 20 claimed improvements from one year; preregister replication protocols; re-run each with 5 seeds and matched tuning; report the replication rate and its predictors.
- **Main Risk:** Compute cost and author-relations sensitivity; sampling and protocol fairness must be unimpeachable for the result to be accepted.
- **Cluster:** EVAL-FAIL
## Sub-cluster ROBUST — Robustness and Distribution Shift (C-0301 – C-0330)

### C-0301 · Robustness is not a backbone property: task-level decoupling
- **One-sentence idea:** Show that the same backbone can be corruption-robust for classification while fragile for segmentation (and vice versa), refuting the implicit assumption that robustness rankings transfer across tasks built on one representation.
- **Problem:** Robustness is benchmarked at the classification level and the results are used to select backbones for dense deployments, assuming task-invariance of robustness that has never been verified.
- **Core Hypothesis:** Corruption-robustness rankings of backbones correlate weakly between classification and dense-task heads on the same corrupted images, because dense readouts depend on spatial feature stability that global pooling hides — a dissociation measurable as rank inversions.
- **Why Important:** Backbone selection for safety-relevant dense systems currently relies on the wrong evidence if the decoupling holds.
- **Why Possibly Novel:** Task-resolved robustness comparisons on matched backbones and corruptions have not been systematically reported.
- **Minimal Experiment:** For 10 backbones, train classification and segmentation heads; evaluate both on identically corrupted images; compare per-backbone robustness rankings across tasks.
- **Main Risk:** Head-capacity choices could drive dense-task differences, requiring head-matched controls.
- **Cluster:** ROBUST

### C-0302 · Last-layer group-robustness fixes fail on spatially entangled bias
- **One-sentence idea:** Test whether the celebrated finding that spurious correlations live in the last layer (fixable by last-layer retraining) breaks down for dense prediction, where spurious cues (context textures, co-occurring backgrounds) are spatially entangled with features throughout the network.
- **Problem:** Group-robustness methods validated on classification (DFR-style) are being adopted as general fixes, but dense tasks bind spurious context to every pixel's receptive field, plausibly violating the last-layer-sufficiency premise.
- **Core Hypothesis:** For segmentation with planted contextual bias (class A always on background B), last-layer retraining on balanced data recovers little worst-group accuracy, while the same intervention works for classification on the same images — the bias residing in spatial feature mixing, not the readout.
- **Why Important:** Determines whether cheap debiasing transfers to the dense tasks deployed in high-stakes settings, or whether dense debiasing needs fundamentally different machinery.
- **Why Possibly Novel:** Group-robustness theory has not been stress-tested on dense prediction with controlled spatial confounds.
- **Minimal Experiment:** Construct segmentation datasets with controlled context-class correlations; compare last-layer vs. full retraining on balanced subsets; measure worst-group IoU recovery in both task modes.
- **Main Risk:** Synthetic confound construction may not represent natural bias structure, requiring one natural-bias validation dataset.
- **Cluster:** ROBUST

### C-0303 · Decomposing weather: reflections, not raindrops, break driving segmentation
- **One-sentence idea:** Decompose adverse-weather failures of driving-scene segmentation into physical components (occlusion by drops, wet-surface reflections, contrast loss, color shift), testing the hypothesis that reflective-surface confusion — not the visually salient rain streaks — causes most safety-relevant errors.
- **Problem:** Weather robustness is treated as a monolithic axis with generic augmentation fixes, without knowing which physical component actually breaks models — so augmentation design is untargeted.
- **Core Hypothesis:** Controlled component-wise degradation shows wet-road reflections cause class-critical errors (road/vehicle confusion) at far higher rates than streak occlusion, and reflection-targeted augmentation recovers more safety-relevant accuracy than generic weather augmentation at matched budget.
- **Why Important:** Component-resolved failure attribution converts weather robustness from benchmark-chasing into targeted physical modeling, with direct AD-safety consequences.
- **Why Possibly Novel:** Physically decomposed weather ablations (isolating each component synthetically and in real captures) have not been used to attribute segmentation failures.
- **Minimal Experiment:** Render/composite each weather component separately onto clear-weather Cityscapes-like scenes; measure per-component, per-class degradation; compare targeted vs. generic augmentation training.
- **Main Risk:** Synthetic component realism limits attribution validity; requires a real rain-capture validation subset.
- **Cluster:** ROBUST

### C-0304 · The corruption radius: how far do patch attacks spread?
- **One-sentence idea:** Characterize the spatial propagation law of localized adversarial patches in dense prediction — how far beyond the patch predictions get corrupted — and show the propagation radius is architecture-family-dependent (global attention spreads corruption much farther than convolution).
- **Problem:** Patch attacks on segmentation are demonstrated anecdotally, but the spatial extent of their influence — the quantity determining physical-world risk — has no measurement standard or architectural characterization.
- **Core Hypothesis:** Corruption radius scales with effective receptive-field structure: bounded and local for CNNs, benchmark-spanning for ViT-based segmenters (single patch flips distant pixels), with attention-window architectures in between — yielding an architecture-level safety trade-off invisible in clean accuracy.
- **Why Important:** Physical patch threat models for AD/robotics need the radius law to assess blast-zone risk, and it introduces a concrete robustness cost of global attention.
- **Why Possibly Novel:** Spatial influence measurement of dense attacks with cross-architecture propagation laws has not been formalized.
- **Minimal Experiment:** Optimize fixed-size patches against 6 segmenters; map corrupted-pixel distributions vs. distance; fit propagation laws per architecture family.
- **Main Risk:** Attack-optimization strength differences across architectures could confound radius comparisons; requires attack-budget normalization.
- **Cluster:** ROBUST

### C-0305 · Natural adversarial examples are mostly not model failures
- **One-sentence idea:** Audit "natural adversarial example" benchmarks (ImageNet-A-style) to quantify what fraction of items reflect genuine model failure versus label ambiguity, multi-object scenes, and misleading ground truth — testing whether the benchmark measures robustness or annotation philosophy.
- **Problem:** Failure-mined benchmarks were constructed by keeping images that fooled an era's models, a selection process that concentrates ambiguous and contestable items whose "correct" labels humans also dispute — yet scores are read as pure robustness.
- **Core Hypothesis:** Human multi-annotator re-labeling shows a large fraction of these items have legitimate alternative answers or ambiguous ground truth, models' "errors" often match plausible human labels, and ambiguity-corrected scoring compresses claimed robustness differences between models substantially.
- **Why Important:** These benchmarks influence robustness research priorities; measuring their signal-to-ambiguity ratio recalibrates what progress on them means.
- **Why Possibly Novel:** Systematic multi-label human audits with score correction have not been applied to failure-mined robustness benchmarks.
- **Minimal Experiment:** Collect 10-annotator label distributions for 2K ImageNet-A items; classify failure types; re-score 15 models against label distributions rather than single labels.
- **Main Risk:** Annotator pools disagree with the original labeling protocol in ways that need careful, transparent adjudication rules.
- **Cluster:** ROBUST

### C-0306 · Robustness interventions saturate: an interference law
- **One-sentence idea:** Measure how robustness interventions (augmentation families, adversarial training, ensembling, test-time adaptation) compose when stacked, testing the hypothesis of strongly sub-additive returns — the interventions consume a shared robustness resource rather than adding independent protections.
- **Problem:** Papers evaluate interventions in isolation, and practitioners stack them assuming approximate additivity, but the composition behavior — the quantity deployment actually cares about — is unmapped.
- **Core Hypothesis:** Pairwise and triple-wise stacking shows saturating returns with specific antagonistic pairs (adversarial training negates augmentation diversity benefits), the saturation structure is predicted by overlap in the feature-invariances each intervention induces, and a small subset of combinations dominates the full stack at fraction of cost.
- **Why Important:** A composition map replaces guesswork in building robust systems and reveals whether robustness methods are mechanistically redundant.
- **Why Possibly Novel:** Systematic composition matrices for robustness interventions with mechanistic overlap analysis have not been published.
- **Minimal Experiment:** Train the 16-cell factorial of 4 interventions on one benchmark; evaluate across shift suites; fit additivity deviations and invariance-overlap predictors.
- **Main Risk:** Factorial compute cost; interaction structure may vary across shift types, complicating one clean law.
- **Cluster:** ROBUST

### C-0307 · Test-time adaptation breaks on realistic streams
- **One-sentence idea:** Characterize the failure boundary of test-time adaptation (TTA) methods under realistic non-i.i.d. test streams — temporally correlated inputs, label shift, recurring environments — hypothesizing catastrophic self-reinforcing drift precisely in the deployment conditions TTA is marketed for.
- **Problem:** TTA methods are validated on shuffled corruption benchmarks, but real streams (a car driving through a tunnel; a camera watching one scene) violate the i.i.d. assumptions their entropy-minimization updates rely on.
- **Core Hypothesis:** Under correlated streams, popular TTA methods collapse (feature drift toward dominant classes, irreversible normalization corruption) with damage growing with adaptation rate; the failure boundary is predictable from stream autocorrelation and class-marginal drift statistics, enabling a safety envelope specification.
- **Why Important:** TTA is entering deployed pipelines; its instability envelope under realistic conditions is the key missing safety datum.
- **Why Possibly Novel:** Stream-realism stress-testing with predictive failure boundaries (not just anecdotal failures) has not been consolidated.
- **Minimal Experiment:** Build stream generators with controllable autocorrelation/label-shift; run 6 TTA methods across the stream-parameter grid; map collapse regions and validate the boundary predictor on real driving videos.
- **Main Risk:** Method-specific fixes (episodic resets) partially mitigate; the study must include them to remain decision-relevant.
- **Cluster:** ROBUST

### C-0308 · Certified robustness for segmentation is numerically vacuous
- **One-sentence idea:** Perform an honest accounting of certified-robustness guarantees for dense prediction, testing whether achievable certified radii at deployable accuracy are orders of magnitude below physically meaningful threat sizes — and identify exactly where the certification pipeline loses tightness.
- **Problem:** Certified segmentation papers report radii without translating them into deployment-relevant threat terms, leaving practitioners unable to judge whether the guarantees exclude any realistic attack at all.
- **Core Hypothesis:** Current certification methods certify per-pixel radii corresponding to perturbations far smaller than compression artifacts, the accuracy cost of certification exceeds its guarantee value under any realistic threat model, and the dominant looseness is attributable to specific pipeline steps (smoothing variance, union bounds over pixels) that dictate where theoretical work should focus.
- **Why Important:** Prevents certified-robustness reporting from functioning as safety theater and directs theory at the measured bottlenecks.
- **Why Possibly Novel:** Threat-calibrated vacuousness accounting with looseness attribution has not been done for dense certification.
- **Minimal Experiment:** Evaluate 3 certified segmentation methods; convert radii to physical threat equivalents (JPEG level, printable patch contrast); decompose the certification gap by pipeline stage.
- **Main Risk:** The conclusion may read as purely negative; the looseness-attribution component must carry constructive weight.
- **Cluster:** ROBUST

### C-0309 · Certification and boundary precision are fundamentally at odds
- **One-sentence idea:** Establish a quantitative trade-off law between randomized-smoothing-based certification strength and boundary localization precision in segmentation — smoothing certifies interiors by destroying exactly the high-frequency evidence boundaries need.
- **Problem:** Certified segmentation reports pixel-accuracy-style metrics under smoothing without acknowledging that the smoothing noise scale directly bounds achievable boundary sharpness, hiding a structural cost of the approach.
- **Core Hypothesis:** Boundary-F degrades as a predictable function of smoothing σ (an uncertainty-principle-like relation between certified radius and boundary localization), implying certification budgets should be spatially adaptive — strong on interiors, absent at boundaries — a design current methods cannot express.
- **Why Important:** Makes the hidden cost of certification explicit and motivates spatially heterogeneous certification as a new problem formulation.
- **Why Possibly Novel:** The radius-vs-boundary-precision trade-off has not been formalized or measured as a law.
- **Minimal Experiment:** Sweep smoothing σ for certified segmenters; measure certified radius and boundary-F jointly; fit the trade-off curve; prototype spatially adaptive σ maps.
- **Main Risk:** The relation may be method-specific rather than fundamental, requiring derivation plus multi-method verification.
- **Cluster:** ROBUST

### C-0310 · The camera ISP is a bigger domain axis than the weather
- **One-sentence idea:** Quantify the sensitivity of recognition/segmentation models to camera image-signal-processor (ISP) parameters — demosaicing, tone mapping, sharpening, denoising — by re-rendering RAW captures under controlled ISP variation, testing whether ISP shift causes degradation comparable to or exceeding celebrated environmental shifts.
- **Problem:** Deployment moves models across devices whose ISPs differ radically, yet robustness research is organized around visible environmental axes while the invisible processing axis lacks even a benchmark.
- **Core Hypothesis:** ISP-parameter shifts within realistic device ranges degrade dense-task accuracy on par with moderate weather corruption, the damage concentrates in texture-defined classes, and ISP-randomized training (cheap, via RAW re-rendering) buys more deployment robustness per compute than generic augmentation.
- **Why Important:** Cross-device reliability is a universal deployment problem with, currently, no measurement instrument or targeted training answer.
- **Why Possibly Novel:** ISP-controlled robustness benchmarks built from RAW re-rendering are essentially absent from the literature.
- **Minimal Experiment:** Re-render a RAW dataset under a grid of ISP pipelines; evaluate 8 models; compare ISP-induced degradation against corruption baselines; train with ISP randomization and re-evaluate.
- **Main Risk:** RAW dataset availability with dense labels is limited, possibly requiring new capture or label transfer.
- **Cluster:** ROBUST

### C-0311 · Video models are worse at motion blur than image models
- **One-sentence idea:** Test the counterintuitive hypothesis that video-trained models are *more* fragile to motion blur than image-trained models — because temporal redundancy lets video models avoid learning blur-invariant single-frame features — inverting the natural expectation that video training teaches motion robustness.
- **Problem:** Video pretraining is assumed to confer robustness to temporal artifacts like motion blur, an assumption never tested at the single-frame level where deployment often operates.
- **Core Hypothesis:** At matched architecture and data scale, video-pretrained encoders show larger accuracy drops on motion-blurred single frames than image-pretrained encoders, because clean-neighbor frames let video models externalize deblurring to temporal aggregation — a crutch absent at test time.
- **Why Important:** Corrects a deployment-relevant expectation about when video pretraining helps, and illustrates a general principle: training-time information redundancy can prevent robust feature learning.
- **Why Possibly Novel:** Frame-level robustness comparisons between video- and image-pretrained models are missing; the redundancy-crutch mechanism is untested.
- **Minimal Experiment:** Evaluate matched video/image-pretrained encoders on blur-graded single-frame recognition/segmentation; verify the mechanism by retraining video models with temporally decorrelated sampling.
- **Main Risk:** Matched video/image model pairs are scarce; may require controlled pretraining at moderate scale.
- **Cluster:** ROBUST

### C-0312 · Corruption doesn't just lower accuracy — it biases predictions toward priors
- **One-sentence idea:** Show that distribution shift induces systematic *directional* prediction bias (toward frequent, contextually expected classes) rather than symmetric accuracy loss, meaning rare and safety-critical classes vanish from predictions first — a failure structure aggregate robustness metrics cannot see.
- **Problem:** Robustness is reported as mean accuracy drop, treating errors as unstructured, while deployment risk depends on *which* classes absorb the errors — an unmeasured distributional failure mode.
- **Core Hypothesis:** Under increasing corruption, prediction marginals converge toward training-prior marginals along a predictable trajectory (evidence-weakening reduces likelihood terms faster than prior terms), rare-class recall collapses super-linearly relative to mean accuracy, and prior-correction at inference partially restores rare-class recall under shift.
- **Why Important:** Safety cases for AD/medical systems hinge on rare-class behavior under degradation; the prior-collapse law would be a core input to such cases.
- **Why Possibly Novel:** Directional bias trajectories under corruption and their prior-dynamics explanation have not been characterized.
- **Minimal Experiment:** Track class-marginal and per-class-recall trajectories across corruption severities for 8 models; fit the prior-convergence law; test inference-time prior correction under shift.
- **Main Risk:** The effect may partly reflect benchmark class imbalance idiosyncrasies, requiring multiple datasets with different prior structures.
- **Cluster:** ROBUST

### C-0313 · Augmentation-trained robustness is corruption memorization
- **One-sentence idea:** Test at scale whether robustness gained from corruption-style augmentation generalizes to genuinely held-out corruption families, or whether the field's augmentation recipes amount to memorizing the benchmark's corruption manifold.
- **Problem:** Augmentation pipelines increasingly resemble the evaluation corruptions (directly or through diversity heuristics), making reported robustness gains uninterpretable as generalization — the overlap has never been rigorously quantified with truly disjoint corruption families.
- **Core Hypothesis:** Under a strict corruption-family holdout protocol (perceptually and mathematically disjoint train/test corruption sets), augmentation-trained models retain only a small fraction of their claimed robustness advantage, and the retained fraction is predicted by feature-space (not pixel-space) similarity between train and test corruption effects.
- **Why Important:** Distinguishes robustness *mechanisms* from corruption *coverage* — the central interpretive question for a decade of augmentation-based robustness results.
- **Why Possibly Novel:** Prior holdout attempts used weakly disjoint families; a formalized disjointness criterion with feature-space similarity accounting is new.
- **Minimal Experiment:** Define corruption families with measured pairwise feature-effect similarity; train on subsets, evaluate on disjoint subsets; regress transfer against similarity.
- **Main Risk:** True disjointness is hard to guarantee; the similarity-regression framing turns this weakness into the object of study.
- **Cluster:** ROBUST

### C-0314 · Sensor fusion degrades below the best single sensor under partial corruption
- **One-sentence idea:** Demonstrate that multi-sensor fusion models (RGB+depth, RGB+LiDAR), advertised as robustness solutions, perform *worse* than their best single-modality branch when one sensor degrades — because learned fusion weights are static while sensor reliability is dynamic — and characterize when fusion is a liability.
- **Problem:** Fusion architectures are validated with all sensors nominal; partial-degradation behavior — the scenario motivating fusion in the first place — is rarely evaluated, and the failure structure (over-trusting the corrupted stream) is unquantified.
- **Core Hypothesis:** Under single-sensor corruption, standard fusion models fall below the clean-sensor-only baseline across a wide degradation range, the deficit traces to fusion layers lacking reliability inference, and lightweight per-sample reliability gating restores the fusion advantage — separating the architecture problem from the concept.
- **Why Important:** Fusion-for-robustness is a foundational assumption of AV/robotics stacks; measuring when it inverts is directly safety-relevant.
- **Why Possibly Novel:** Systematic partial-degradation stress matrices for fusion architectures with mechanism attribution have not been standard.
- **Minimal Experiment:** Evaluate 5 fusion architectures on segmentation/detection under per-sensor corruption grids; compare against single-sensor baselines; test reliability-gated variants.
- **Main Risk:** Results may depend on fusion-stage placement (early/late), requiring the comparison across fusion designs to be complete.
- **Cluster:** ROBUST

### C-0315 · A size-robustness law: small objects fail first, predictably
- **One-sentence idea:** Establish a quantitative law relating object pixel size to corruption robustness — how detection/segmentation reliability decays with size under each shift type — providing the missing input for safety analyses that currently assume size-uniform degradation.
- **Problem:** Aggregate robustness numbers average over object scales, but deployment risk concentrates in small objects (distant pedestrians); the size-conditional structure of robustness has not been formalized as a measurable law.
- **Core Hypothesis:** Per-size robustness curves collapse onto a universal form when size is normalized by corruption-specific information-loss scales (blur radius, noise power per object area), enabling prediction of small-object failure onset for unseen corruption levels from a few calibration measurements.
- **Why Important:** A predictive size-robustness law converts robustness evaluation into an engineering tool for setting operational limits (maximum reliable detection distance under conditions).
- **Why Possibly Novel:** Size-stratified robustness has appeared descriptively; the normalized universal-curve formulation with predictive validation is new.
- **Minimal Experiment:** Measure per-size AP/IoU across corruption grids for 6 models; test curve collapse under the proposed normalization; validate predictions on held-out severities.
- **Main Risk:** Universality may fail across corruption types with qualitatively different information loss, fragmenting the law.
- **Cluster:** ROBUST

### C-0316 · Modern models are more compression-fragile than their predecessors
- **One-sentence idea:** Test the hypothesis that web-trained modern models are *more* sensitive to JPEG/codec parameter shifts than ImageNet-era models — because web training data is pre-compressed within a narrow quality band, creating an unrecognized codec-distribution dependence.
- **Problem:** Compression robustness is assumed solved and no longer tracked, while training-data pipelines quietly changed the compression statistics models are adapted to — allowing generation-over-generation regressions to go unnoticed.
- **Core Hypothesis:** Accuracy-vs-quality-factor curves show modern web-pretrained models degrading faster outside the web-typical quality band (both at very high and very low quality) than older models trained on less uniformly compressed data, with sensitivity localized to compression-artifact-tuned features detectable in early layers.
- **Why Important:** Codec settings vary across cameras, platforms, and pipelines; a hidden regression on this axis affects virtually every deployment.
- **Why Possibly Novel:** Longitudinal codec-sensitivity auditing across model generations, tied to training-corpus compression statistics, has not been performed.
- **Minimal Experiment:** Evaluate 20 models spanning eras across quality-factor sweeps (including recompression chains); measure per-generation sensitivity; correlate with training-corpus compression statistics where documented.
- **Main Risk:** Corpus compression statistics are partially undocumented, requiring estimation from corpus samples.
- **Cluster:** ROBUST

### C-0317 · The adversarial-pretraining transfer crossover
- **One-sentence idea:** Resolve the conflicting evidence on whether adversarially trained backbones transfer better or worse by testing a crossover hypothesis: robust features win dense-task transfer at low target-data scale (better priors) but lose at high scale (information ceiling from invariance constraints).
- **Problem:** The literature contains both "robust models transfer better" and "robustness taxes accuracy" results, treated as contradictory rather than as regimes of one law — leaving practitioners without guidance on when to use robust checkpoints.
- **Core Hypothesis:** Transfer performance curves of robust vs. standard backbones cross at a predictable target-data scale that shifts with task granularity (later crossover for boundary-sensitive tasks where robust features' smoothness costs most), unifying the contradictory findings.
- **Why Important:** Converts a confusing literature into a decision rule (use robust checkpoints below data threshold X for task type Y).
- **Why Possibly Novel:** The data-scale crossover framing with task-granularity dependence has not been proposed or mapped.
- **Minimal Experiment:** Fine-tune robust/standard backbone pairs across target-data scales on {classification, segmentation, depth}; locate crossovers; test the granularity prediction.
- **Main Risk:** Robust checkpoint availability confounds (different data/recipes) require training matched pairs for clean claims.
- **Cluster:** ROBUST

### C-0318 · Temporal flicker is a robustness axis orthogonal to accuracy
- **One-sentence idea:** Establish frame-to-frame prediction instability (flicker) of segmentation models on videos as a robustness dimension uncorrelated with mIoU, propose its standardized measurement, and show that accuracy-matched models differ by large factors in stability — with training-procedure causes identifiable.
- **Problem:** Dense models are selected by single-frame accuracy and deployed on video, where instability breaks downstream consumers (tracking, planning, user trust); the field lacks even agreement that stability is a separate quality to report.
- **Core Hypothesis:** Flicker (label-change rate on static regions under natural frame-to-frame variation) varies several-fold among mIoU-matched models, is driven by identifiable training factors (augmentation noise sensitivity, sharp decision boundaries, BN statistics), and cheap interventions (temporal consistency losses on unlabeled video, EMA weights) reduce it without accuracy cost.
- **Why Important:** Makes an invisible deployment-critical property visible, measurable, and optimizable — likely reordering model choices for every video application.
- **Why Possibly Novel:** Temporal stability metrics exist in scattered forms; the accuracy-orthogonality demonstration and causal training-factor analysis do not.
- **Minimal Experiment:** Measure flicker for 12 accuracy-matched segmenters on unlabeled driving/indoor video; regress against training factors; validate intervention effects.
- **Main Risk:** Distinguishing legitimate prediction changes (real motion) from flicker needs careful static-region identification.
- **Cluster:** ROBUST

### C-0319 · CNNs fail locally, ViTs fail globally — different safety profiles
- **One-sentence idea:** Characterize the *topology* of failure under distribution shift — CNN errors clustering in local image regions while ViT errors manifest as global, image-wide label coherence failures — showing architecture choice determines failure geometry, not just failure rate, with distinct safety implications.
- **Problem:** Robustness comparisons report scalar accuracy, but downstream harm depends on error structure: a locally wrong map is recoverable by fusion; a globally incoherent one is not — and this structural dimension is unmeasured across architectures.
- **Core Hypothesis:** Under matched accuracy drops, error spatial autocorrelation and cross-image coherence statistics separate architecture families sharply (attention propagates corruption globally; convolution contains it), and the failure-topology profile predicts downstream system-level harm better than accuracy in fusion/tracking pipelines.
- **Why Important:** Safety engineering needs failure-structure models, not just rates; an architecture-conditioned failure topology would directly inform redundancy design.
- **Why Possibly Novel:** Failure-geometry characterization across architecture families under shift, with downstream-harm validation, is unexplored.
- **Minimal Experiment:** Evaluate matched CNN/ViT segmenters under corruption; compute error-cluster statistics; simulate downstream fusion/tracking consumers; compare harm per unit accuracy loss.
- **Main Risk:** Accuracy matching across architectures under shift requires careful checkpoint selection to avoid confounds.
- **Cluster:** ROBUST

### C-0320 · Mild shifts compound super-linearly
- **One-sentence idea:** Measure robustness under *combinations* of individually mild corruptions (slight blur + slight noise + slight color shift), testing the hypothesis that degradation composes super-linearly — real-world conditions are compositions, and single-axis benchmarks systematically understate deployed risk.
- **Problem:** Robustness benchmarks perturb one axis at a time, while deployment conditions co-vary many mild degradations; the composition behavior of model robustness is essentially uncharacterized.
- **Core Hypothesis:** Accuracy loss under k combined mild corruptions substantially exceeds the sum of individual losses, the super-linearity grows with model reliance on any single fragile feature family (identifiable via frequency analysis), and models ranked robust on single axes reorder under composition — with a compact interaction model predicting compositional loss from pairwise measurements.
- **Why Important:** If composition breaks single-axis extrapolation, the field's robustness evidence doesn't support deployment claims, and benchmark design must change.
- **Why Possibly Novel:** Corruption-interaction studies beyond severity scaling of single types are nearly absent.
- **Minimal Experiment:** Evaluate 10 models on a designed composition grid (all pairs and triples at calibrated mild severities); fit interaction models; compare single-axis and compositional rankings.
- **Main Risk:** Severity calibration for "mild" must be principled (human-matched) for compositions to be interpretable.
- **Cluster:** ROBUST

### C-0321 · Dense prediction is the soft target for backdoors
- **One-sentence idea:** Characterize the backdoor threat surface of segmentation models, testing the hypothesis that dense tasks are substantially easier to backdoor imperceptibly than classification — spatially localized triggers causing spatially localized mislabeling evade all current defenses designed for image-level flips.
- **Problem:** Backdoor research is classification-centric; dense-task attack surfaces (trigger→local mask edits, class-conditional region attacks) and the corresponding defense gaps are unmapped while segmentation deploys in safety-critical settings.
- **Core Hypothesis:** Dense backdoors achieve high attack success at poison rates far below classification-equivalent attacks (per-pixel supervision provides more gradient channels for trigger binding), evade classification-oriented defenses entirely, and produce clean-accuracy footprints below detection thresholds — establishing dense tasks as the highest-risk/lowest-defense quadrant.
- **Why Important:** Threat prioritization for ML security currently ignores the tasks most exposed; measured attack economics would redirect defense research.
- **Why Possibly Novel:** Systematic dense-task backdoor characterization (attack economics, defense evasion, detection signatures) is missing.
- **Minimal Experiment:** Implement trigger→mask attacks across poison rates on Cityscapes training; measure success/stealth curves; run classification-era defenses; propose dense-specific detection statistics.
- **Main Risk:** Dual-use sensitivity requires responsible framing centered on detection contributions.
- **Cluster:** ROBUST

### C-0322 · Promptable segmenters are discontinuous in their prompts
- **One-sentence idea:** Audit the stability of promptable segmentation models (SAM-class) under tiny prompt perturbations — single-pixel point jitter, box edge shifts — documenting discontinuous mask changes and establishing prompt-stability as a reliability metric that current leaderboards ignore.
- **Problem:** Promptable models are evaluated on best-case or simulated prompts, while human prompts vary; if outputs are discontinuous in prompt space, downstream annotation and interactive systems inherit unquantified instability.
- **Core Hypothesis:** A measurable fraction of point prompts sit near decision discontinuities where 1–2 pixel jitter changes the selected object entirely, instability concentrates at ambiguous part-whole hierarchies, and prompt-stability maps predict human annotation disagreement — making instability a usable ambiguity signal as well as a defect.
- **Why Important:** Promptable models are becoming annotation infrastructure; their input-stability properties propagate into every dataset built with them.
- **Why Possibly Novel:** Prompt-space stability analysis with discontinuity mapping and human-disagreement validation has not been published.
- **Minimal Experiment:** Perturb prompts systematically over 5K instances for 3 promptable models; measure mask divergence distributions; correlate instability maps with multi-annotator disagreement data.
- **Main Risk:** Some instability is legitimate ambiguity resolution; the analysis must separate defect from ambiguity via the human-agreement anchor.
- **Cluster:** ROBUST

### C-0323 · Mean robustness conceals worst-case incompetence
- **One-sentence idea:** Show that models with equal mean robustness differ enormously in per-image worst-case behavior across shifts (some images fail under *every* condition), and that mean-based robustness reporting systematically hides the tail structure that determines real-world reliability.
- **Problem:** Robustness suites report averages over images and corruptions; two models with identical means can have completely different tail behavior — one failing gracefully everywhere, one catastrophically somewhere — and the field's metrics cannot tell them apart.
- **Core Hypothesis:** Per-image robustness profiles (accuracy across the full shift battery) reveal a heavy-tailed "universally fragile" image subpopulation that differs across models despite equal means, tail mass is uncorrelated with mean robustness across models, and tail-aware selection identifies different winners than mean-based leaderboards.
- **Why Important:** Reliability engineering is about tails; introducing distributional robustness reporting would realign evaluation with deployment risk.
- **Why Possibly Novel:** Image-level robustness-profile analysis with tail/mean decoupling demonstrations has not been standard.
- **Minimal Experiment:** Compute full image×shift accuracy tensors for 10 models; analyze tail statistics and cross-model tail overlap; propose and evaluate tail-aware summary metrics.
- **Main Risk:** Tail estimates need many shift conditions per image; compute grows quickly and must be budgeted by design.
- **Cluster:** ROBUST

### C-0324 · Style-transfer robustness tests overestimate real-shift robustness
- **One-sentence idea:** Show that stylization-based robustness evaluations (and trainings) preserve scene layout statistics, so they measure only appearance-shift robustness while real domain shifts change layout too — inflating robustness estimates for models that rely on spatial priors.
- **Problem:** Stylized benchmarks are used as proxies for domain shift, but they perturb texture while keeping composition fixed, leaving a whole shift dimension (layout, viewpoint, object-configuration change) untested — and models can pass by leaning harder on the preserved layout.
- **Core Hypothesis:** Models with strong spatial-prior reliance (measurable via position-scrambling sensitivity) score deceptively well on stylized suites but fail layout-shifted real domains; decomposing shift into appearance and layout components shows current benchmarks cover mostly the former, and layout-controlled evaluations reorder robustness rankings.
- **Why Important:** Corrects what a widely used robustness instrument actually measures, and introduces the missing layout-shift axis into evaluation.
- **Why Possibly Novel:** The appearance/layout shift decomposition with prior-reliance interaction analysis has not been formulated.
- **Minimal Experiment:** Construct evaluations factoring appearance shift (stylization) and layout shift (composition-varied captures/synthetics); measure model performance on the 2×2; correlate with spatial-prior reliance metrics.
- **Main Risk:** Constructing layout-shifted evaluations at scale requires synthetic scenes or new collections with careful realism control.
- **Cluster:** ROBUST

### C-0325 · Pixel metrics hide instance-level robustness collapse
- **One-sentence idea:** Demonstrate that segmentation models under shift can maintain respectable mIoU while entire object instances vanish from predictions — pixel- and instance-level robustness decouple — and introduce instance-survival metrics that expose safety-relevant failures aggregate metrics miss.
- **Problem:** Corruption evaluations for segmentation report pixel metrics in which losing a distant pedestrian entirely costs almost nothing, so models optimized and selected under them can be instance-catastrophic while looking robust.
- **Core Hypothesis:** Under increasing shift, instance-survival rate (fraction of ground-truth objects retaining any sufficient prediction mass) degrades much faster than mIoU, the decoupling is model-dependent (some architectures fail by erosion, others by deletion), and instance-survival rankings disagree with mIoU-robustness rankings.
- **Why Important:** For any application that cares about objects (all safety applications), the pixel-metric robustness literature may be measuring the wrong thing entirely.
- **Why Possibly Novel:** Instance-survival-vs-pixel-metric decoupling under shift has not been quantified as a general phenomenon.
- **Minimal Experiment:** Evaluate 10 segmenters across corruption grids with joint pixel and instance-survival metrics; characterize erosion-vs-deletion failure styles; re-rank models.
- **Main Risk:** Instance-survival thresholds introduce metric design freedom needing sensitivity analysis.
- **Cluster:** ROBUST

### C-0326 · The geography-performance law of dense prediction
- **One-sentence idea:** Quantify how dense-prediction performance varies across world regions and income levels, and — beyond documenting the gap — attribute it causally among object-appearance differences, context/layout differences, and photographic-capture differences to determine what data collection would actually fix it.
- **Problem:** Geographic performance disparities are documented for classification, but dense tasks (where infrastructure, vehicles, and street layouts differ radically) lack both measurement and, critically, causal attribution of the gap's components — so mitigation is guesswork.
- **Core Hypothesis:** Dense-task degradation across regions exceeds classification degradation (context reliance amplifies distribution mismatch), and controlled decomposition (object-swap composites, layout-transfer tests, capture-stat normalization) shows layout/context mismatch — not object appearance — dominates, implying targeted scene-level (not object-level) data collection is the efficient fix.
- **Why Important:** Global deployment equity for segmentation-based systems requires knowing what the gap is made of, not just that it exists.
- **Why Possibly Novel:** Component-level causal attribution of geographic performance gaps for dense prediction has not been attempted.
- **Minimal Experiment:** Evaluate segmenters on geographically diverse driving/street datasets; run the attribution battery (composite swaps, capture normalization); rank component contributions per region.
- **Main Risk:** Geographically diverse dense-labeled data is scarce; partial label transfer and human verification will be needed.
- **Cluster:** ROBUST

### C-0327 · Does simulation find real failures? Validating sim-based robustness testing
- **One-sentence idea:** Test the core assumption of simulation-based robustness testing — that failure modes discovered in simulation predict real-world failures — by systematically searching for failures in sim and verifying their transfer rate on matched real captures.
- **Problem:** Industry increasingly certifies perception robustness via simulated adversarial scenario search, without measured evidence about which classes of simulated failures transfer to reality and which are rendering artifacts.
- **Core Hypothesis:** Failure transfer is highly category-dependent — geometry/occlusion-driven failures transfer at high rates while appearance/lighting-driven failures transfer poorly (renderer-specific) — enabling a validated taxonomy of which simulation findings warrant real-world action.
- **Why Important:** Simulation testing is becoming a certification instrument; its predictive validity is the load-bearing question and is essentially unmeasured in public literature.
- **Why Possibly Novel:** Systematic sim-to-real failure-transfer measurement with a predictive taxonomy has not been published openly.
- **Minimal Experiment:** Run scenario search against a segmenter in simulation; physically reconstruct/re-capture 100 failure and 100 non-failure scenarios; measure transfer rates by failure category.
- **Main Risk:** Physical reconstruction fidelity limits scale; careful scenario selection and matched-capture protocols are the hard engineering.
- **Cluster:** ROBUST

### C-0328 · Robust "architectures" are mostly robust data
- **One-sentence idea:** Re-attribute the robustness advantages claimed for architectural innovations by retraining architecture pairs on strictly matched data and recipes, testing the hypothesis that data differences explain most published cross-architecture robustness differences.
- **Problem:** Robustness comparisons across architectures (ViT-vs-CNN robustness claims and successors) almost always compare models trained on different data/recipes, and the architecture-vs-data attribution has been repeatedly raised but never settled with adequate controls across the modern architecture zoo.
- **Core Hypothesis:** Under matched pretraining data, augmentation, and schedule, cross-architecture robustness differences shrink by more than half across shift suites, with the residual concentrated in specific shift types (occlusion robustness genuinely favoring attention), producing a validated decomposition of the robustness literature's claims.
- **Why Important:** The field allocates architectural research effort based on robustness claims that may be data shadows; a decisive attribution changes the agenda.
- **Why Possibly Novel:** Matched-everything retraining across a broad modern architecture panel with shift-type-resolved attribution has not been executed.
- **Minimal Experiment:** Train 6 architectures under one matched recipe at two data scales; evaluate the full shift battery; compare cross-architecture spreads against published unmatched comparisons.
- **Main Risk:** One recipe cannot be simultaneously optimal for all architectures; dual-recipe (per-family tuned) arms are needed to bound fairness effects.
- **Cluster:** ROBUST

### C-0329 · Scale inverts noise-type robustness in fine-tuning
- **One-sentence idea:** Test the hypothesis that large pretrained models are more robust than small models to random (symmetric) label noise during fine-tuning but *less* robust to structured, instance-dependent noise — because their capacity and priors let them internalize systematic error patterns that small models cannot fit.
- **Problem:** Label-noise robustness conclusions come from small models with synthetic symmetric noise, while modern fine-tuning faces machine-generated structured noise on large models — the regime where the classic conclusions may invert, unmeasured.
- **Core Hypothesis:** Across model scales, symmetric-noise tolerance grows with scale (priors override random error), while structured-noise absorption also grows with scale (systematic errors are learnable signal to a big model) — producing a scale-dependent crossover in which noise type is more dangerous, with direct implications for machine-annotated training pipelines.
- **Why Important:** The field's noise-handling toolkit and data-quality thresholds are calibrated to the wrong noise model for the current scale regime if the inversion holds.
- **Why Possibly Novel:** Scale × noise-structure interaction studies are absent; noise robustness is treated as scale-monotone.
- **Minimal Experiment:** Fine-tune model ladder (0.1B–7B) on datasets with matched-rate symmetric vs. structured (annotator-model-generated) noise; measure clean-test degradation and noise-pattern internalization per scale.
- **Main Risk:** Constructing realistic structured noise at controlled rates requires care to avoid confounding noise rate with noise learnability.
- **Cluster:** ROBUST

### C-0330 · Abstention fails exactly when it's needed
- **One-sentence idea:** Show that selective-prediction (abstention) mechanisms tuned in-distribution invert under shift — the model abstains on hard-but-solvable ID-like items while confidently answering the shifted items it gets wrong — and establish shift-robust abstention evaluation as a required reporting standard.
- **Problem:** Selective prediction is the standard safety wrapper for deployed models, validated by ID risk-coverage curves; its behavior under the shifts that motivate abstention in the first place is rarely evaluated and plausibly pathological.
- **Core Hypothesis:** Under distribution shift, risk-coverage curves of standard confidence-based abstention cross the random-abstention baseline (worse than useless) for a substantial range of coverage levels, because shift moves errors into high-confidence regions; shift-exposed abstention training and density-aware scores restore monotonicity — defining what "safe abstention" must mean operationally.
- **Why Important:** If the safety wrapper fails under exactly the conditions it exists for, every deployment relying on confidence-thresholded abstention has an unmeasured hole.
- **Why Possibly Novel:** Risk-coverage inversion under shift has been noted in fragments; its systematic characterization with corrected evaluation protocols and fixes is not established.
- **Minimal Experiment:** Compute risk-coverage curves for 10 models × 6 abstention scores, ID and across shift suites; document inversions; evaluate density-aware and shift-trained alternatives.
- **Main Risk:** Results may vary strongly across abstention scores, requiring comprehensive coverage to support general claims.
- **Cluster:** ROBUST
## Sub-cluster GENERAL — Generalization and Simple Belief-Challenging Hypotheses (C-0331 – C-0360)

### C-0331 · One number predicts fine-tuning generalization: functional distance from init
- **One-sentence idea:** Test whether a single cheap quantity — functional distance from the pretrained initialization (output KL on unlabeled data) — predicts the generalization gap of fine-tuned models better than the classical complexity-measure zoo.
- **Problem:** Generalization prediction for fine-tuning lacks a usable measure; classical norms and sharpness metrics were built (and mostly fail) for from-scratch training, while the fine-tuning regime's obvious anchor — the init — is ignored by that literature.
- **Core Hypothesis:** Across tasks, lrs, and methods, held-out performance degrades predictably with functional distance from init beyond a task-dependent optimum, and this one measure dominates weight-norm, sharpness, and margin measures for rank-predicting generalization among fine-tuned variants.
- **Why Important:** A validated predictor enables unlabeled-data model selection and gives fine-tuning theory a correct starting point (deviation from a strong prior, not absolute complexity).
- **Why Possibly Novel:** Distance-from-init appears in theory bounds but has not been benchmarked head-to-head as a practical predictor across modern fine-tuning regimes.
- **Minimal Experiment:** Fine-tune 100 variants (lr × epochs × method) on 3 tasks; measure functional distance on unlabeled data and 8 complexity measures; compare rank-prediction of held-out accuracy.
- **Main Risk:** The optimum-distance structure may be task-specific enough to prevent a single universal law, yielding task-conditioned predictors instead.
- **Cluster:** GENERAL

### C-0332 · Does "accuracy on the line" survive dense prediction?
- **One-sentence idea:** Test whether the celebrated linear ID-OOD accuracy relationship — which underpins how the field interprets robustness interventions — holds for segmentation and detection, where spatial error structure and per-class coupling could break the law.
- **Problem:** The accuracy-on-the-line phenomenon was established for classification and is implicitly assumed for all tasks, informing claims that "effective robustness" is rare; no one has verified the law's scope for dense prediction.
- **Core Hypothesis:** Dense tasks show systematically weaker ID-OOD linearity with structured off-line residuals (models trading interior robustness against boundary robustness), and genuine effective-robustness interventions — invisible in classification — exist for dense tasks.
- **Why Important:** If the law fails for dense tasks, the field's main tool for judging robustness interventions doesn't apply where robustness matters most.
- **Why Possibly Novel:** The linear-trend literature is classification-only; the dense-task scope test with residual-structure analysis is missing.
- **Minimal Experiment:** Evaluate 30 segmenters/detectors on ID and shifted benchmark pairs; fit linear trends per metric (mIoU, boundary-F, AP); characterize off-line models and their common properties.
- **Main Risk:** Fewer available dense models than classifiers weakens trend estimation; may require training a controlled model panel.
- **Cluster:** GENERAL

### C-0333 · Long-tail generalization requires memorization — the causal test
- **One-sentence idea:** Empirically test the theory that memorizing rare training examples is *necessary* for tail generalization, by estimating per-example memorization scores at modern scale and measuring the causal effect of removing memorized examples on tail-class test accuracy.
- **Problem:** The memorization-for-generalization theory is supported by small-scale and theoretical evidence, while modern practice (dedup, memorization-suppression) implicitly assumes memorization is waste — a live contradiction with data-policy consequences.
- **Core Hypothesis:** Removing the top-memorization-score examples damages test accuracy specifically on visually-similar rare test items far beyond random-removal controls, the effect grows toward the class-frequency tail, and memorization-suppressing regularizers reproduce the same targeted damage — memorization is functional infrastructure for the tail.
- **Why Important:** Directly informs deduplication and privacy-motivated memorization-removal policies, which may be silently destroying tail performance.
- **Why Possibly Novel:** Feldman-style influence estimation has not been scaled to modern vision training with causal removal experiments on realistic long-tail data.
- **Minimal Experiment:** Estimate memorization scores on iNaturalist-scale training via subsampled-retraining ensembles; retrain with targeted vs. random removals; measure frequency-stratified test effects.
- **Main Risk:** Memorization-score estimation is compute-heavy; efficient proxies must be validated against the gold estimator first.
- **Cluster:** GENERAL

### C-0334 · One spectral-bias number behind texture bias, shortcuts, and adversarial fragility
- **One-sentence idea:** Test the parsimony hypothesis that texture bias, shortcut learning, and adversarial vulnerability — treated as three literatures — are manifestations of one measurable quantity (the model's effective spectral/simplicity bias), such that a single intervention moves all three predictably.
- **Problem:** Three research communities build separate explanations and fixes for phenomena that may share one cause, wasting effort and obscuring the underlying law.
- **Core Hypothesis:** A model-level simplicity-bias metric (function-frequency response measured via controlled probes) correlates strongly with all three phenomena across architectures and recipes, and interventions that shift the metric (loss shaping, data curricula) move all three in lockstep — while interventions failing to move the metric fix none robustly.
- **Why Important:** Unification would replace three toolboxes of local fixes with one causal handle, and failure would establish the phenomena as genuinely distinct — either outcome reorganizes the robustness literature.
- **Why Possibly Novel:** The three-way joint measurement with interventional lockstep testing has not been performed.
- **Minimal Experiment:** Measure the spectral-bias metric plus all three phenomena for 15 diverse models; compute the correlation structure; apply 3 bias-shifting interventions and test lockstep movement.
- **Main Risk:** Partial correlations (two of three linked) would complicate but not doom the study — the correlation structure is informative regardless.
- **Cluster:** GENERAL

### C-0335 · Sharpness stops predicting generalization outside one architecture family
- **One-sentence idea:** Replicate and extend the negative result that flatness/sharpness measures fail to predict generalization once architecture varies, at foundation-model scale — testing whether the field's favorite generalization story survives its most basic out-of-family test.
- **Problem:** Flat-minima reasoning motivates optimizers (SAM), analysis tooling, and folklore, based on within-family correlational evidence; if sharpness-generalization correlation is zero across families at scale, the story's explanatory status collapses.
- **Core Hypothesis:** Within an architecture family, sharpness correlates with generalization moderately (confound: lr and regularization); across families (ViT/ConvNeXt/hybrid) at matched accuracy, correlation vanishes or inverts, and reparameterization-invariant sharpness variants do not rescue it — flatness is a within-recipe correlate, not a cause.
- **Why Important:** Cleans the field's causal narratives and redirects optimizer research away from flatness proxies if they fail out-of-family.
- **Why Possibly Novel:** The cross-family test at modern scale with invariant sharpness measures has not been decisive; the literature remains within-family.
- **Minimal Experiment:** Train matched-accuracy model panels across 4 families; measure 5 sharpness variants; correlate with ID generalization gap and OOD accuracy within and across families.
- **Main Risk:** Matched-accuracy panels across families require careful recipe work; conclusions depend on measure implementations being audit-proof.
- **Cluster:** GENERAL

### C-0336 · Open-set and OOD generalization are different muscles
- **One-sentence idea:** Test whether generalization to novel classes (open-set recognition) and generalization to novel domains (distribution shift) — habitually conflated as "generalization ability" — are actually uncorrelated model properties with different data and architectural determinants.
- **Problem:** Model cards and papers speak of generalization as one axis, and methods are transferred between open-set and OOD problems assuming shared structure; the correlation between the two abilities across models has never been measured.
- **Core Hypothesis:** Across a large model panel, novel-class performance and domain-shift robustness correlate weakly; the two abilities respond to different training factors (semantic coverage vs. appearance diversity of pretraining data), and optimizing one leaves the other unchanged — requiring separate reporting and separate methods.
- **Why Important:** Conflation misleads model selection for deployments that face one challenge but not the other, and misleads method development that claims general "generalization" improvements.
- **Why Possibly Novel:** The correlation structure between open-set and shift generalization has not been measured as a primary question.
- **Minimal Experiment:** Evaluate 30 models on matched open-set and shift benchmark suites; compute cross-ability correlations; regress each ability on training-data covariates.
- **Main Risk:** Benchmark difficulty imbalances could suppress correlations artificially; needs difficulty-equated suites.
- **Cluster:** GENERAL

### C-0337 · Human-like confusions predict machine generalization
- **One-sentence idea:** Test whether models whose error patterns match human confusion structure (before any shift) generalize better under distribution shift — making human-alignment of errors a cheap, ID-computable robustness predictor.
- **Problem:** Predicting OOD behavior without OOD data is a core unsolved need; human error structure is an untapped candidate signal on the theory that human-like feature reliance implies human-like (shift-stable) cues.
- **Core Hypothesis:** Error-consistency with human confusion matrices on ID data rank-predicts OOD accuracy across models better than ID accuracy does, the prediction survives controlling for accuracy and scale, and the driver is shared cue reliance (verified by cue-conflict tests).
- **Why Important:** A validated ID-computable robustness predictor changes model selection practice; the human-alignment link also informs the debate on whether human-like processing matters instrumentally.
- **Why Possibly Novel:** Error-consistency metrics exist descriptively; their use and validation as *predictive* robustness instruments does not.
- **Minimal Experiment:** Compute human-error consistency for 25 models on datasets with human confusion data; correlate with OOD suite performance, partialling out ID accuracy; verify the cue-reliance mediator on cue-conflict stimuli.
- **Main Risk:** Human confusion data covers limited datasets, constraining the model panel's evaluation scope.
- **Cluster:** GENERAL

### C-0338 · Visual composition follows the data's co-occurrence statistics — a quantitative law
- **One-sentence idea:** Establish that models compose visual concepts (attribute-object, object-context) exactly as far as the compositional statistics of training data allow — a measurable "visual n-gram" law — reframing compositional failure from an architecture problem to a data-statistics bound.
- **Problem:** Compositional generalization failures are blamed on architectures lacking binding mechanisms, spawning structural innovations, while the null model — performance tracks combination-frequency statistics in training data — has never been quantitatively fitted.
- **Core Hypothesis:** Zero-shot performance on unseen attribute-object combinations is predicted with high accuracy by a smoothed co-occurrence model over training statistics (analogous to language-model n-gram backoff), residuals from the law are small and architecture-independent, and apparent architectural "compositionality gains" vanish once data statistics are controlled.
- **Why Important:** If composition is data-bounded, the fix is data design, not architecture — redirecting a major research agenda with a falsifiable law.
- **Why Possibly Novel:** Quantitative co-occurrence-law fitting with architecture-controlled residual analysis is absent from the visual compositionality literature.
- **Minimal Experiment:** Train matched models on datasets with controlled combination statistics; fit the frequency law; test architectural variants for residual differences beyond the law.
- **Main Risk:** Estimating combination statistics for web-scale pretraining is approximate; controlled-data experiments carry the causal weight.
- **Cluster:** GENERAL

### C-0339 · In-weights knowledge crowds out in-context adaptability
- **One-sentence idea:** Test a conservation-like trade-off in VLMs: models that store more task knowledge in weights (better zero-shot) are systematically worse at in-context adaptation to conflicting or novel information, and vice versa — the two learning modes competing rather than composing.
- **Problem:** Model development pushes zero-shot performance and in-context flexibility simultaneously, assuming they are independent virtues; scattered evidence of prior-override failures suggests they may be structurally opposed.
- **Core Hypothesis:** Across models and checkpoints, zero-shot strength on a domain anti-correlates with the ability to adopt in-context information contradicting that domain's priors (measured by counterfactual in-context tasks), the trade-off strengthens with training duration, and it is mediated by measurable attention allocation between context and parametric pathways.
- **Why Important:** If the trade-off is real, "one model for everything" has a structural cost, and applications needing adaptability should select (or train) differently than applications needing knowledge.
- **Why Possibly Novel:** The in-weights/in-context competition has been studied in small-scale language settings; the multimodal, capability-resolved version with mediation analysis is new.
- **Minimal Experiment:** Build counterfactual in-context benchmarks (context redefines visual categories); evaluate a model panel spanning zero-shot strength; correlate override ability with zero-shot scores, controlling scale.
- **Main Risk:** Constructing counterfactual tasks that are unambiguous yet natural requires careful design to avoid measuring instruction-following instead.
- **Cluster:** GENERAL

### C-0340 · Where do invariances come from: data or architecture? An attribution audit
- **One-sentence idea:** Attribute each of a trained model's invariances (translation, scale, rotation tolerance, illumination) quantitatively to architecture (built-in constraints) versus data statistics (learned exposure), producing an invariance provenance map that tests the belief that data can teach any invariance.
- **Problem:** Invariance is discussed loosely as "learned from data" or "built into architecture" without a measurement framework that decomposes the two sources — leaving augmentation and architecture design decisions unguided.
- **Core Hypothesis:** Provenance is invariance-specific: translation tolerance is mostly architectural (surviving random-data training), scale tolerance is mostly data-driven (vanishing without scale-diverse exposure), and rotation tolerance is unlearnable to full range regardless of data (architectural ceiling) — a structured map contradicting the pure-data view.
- **Why Important:** Tells designers which invariances must be architecturally provided versus cheaply taught, replacing folklore in augmentation and architecture choices.
- **Why Possibly Novel:** Systematic invariance-provenance decomposition (random-data controls, exposure-ablated training, architectural ablations) has not been assembled.
- **Minimal Experiment:** Train matched models on {natural data, exposure-ablated data, random data} across {CNN, ViT, ViT+2D-PE variants}; measure invariance spectra; decompose provenance per invariance.
- **Main Risk:** Interactions (architecture enabling data-learning of invariance) complicate clean additive attribution; factorial design mitigates.
- **Cluster:** GENERAL

### C-0341 · CLIP's robustness miracle is training-set coverage — the causal ablation
- **One-sentence idea:** Causally test the celebrated distribution-robustness of CLIP-style models by retraining on corpora with style-shifted content (sketches, renditions, art) explicitly removed, predicting that the famous effective-robustness collapses to standard levels — closing the debate with an intervention rather than correlation.
- **Problem:** CLIP's flat ID-OOD line spawned competing explanations (language supervision, data scale, data distribution); existing evidence is correlational, and the field still cites the robustness as a paradigm property rather than a data property.
- **Core Hypothesis:** Style-coverage-ablated CLIP loses most effective robustness on rendition-type benchmarks while keeping ID accuracy, matched-coverage supervised models gain similar robustness, and residual paradigm effects are small — data coverage is the mechanism, quantitatively.
- **Why Important:** The result determines whether robustness should be pursued through objectives/architectures or purely through data curation — one of the field's directional questions.
- **Why Possibly Novel:** Coverage-ablation retraining at sufficient scale has not been executed; the debate has run on observational analyses.
- **Minimal Experiment:** Train CLIP-small on LAION subsets with style-content filtered (classifier-based) vs. matched-size random filtering; evaluate effective robustness; run the mirrored supervised-arm comparison.
- **Main Risk:** Style filtering is imperfect; leakage bounds must be measured and reported alongside the effect.
- **Cluster:** GENERAL

### C-0342 · One universal hardness score predicts every model's errors
- **One-sentence idea:** Test whether per-sample difficulty is model-independent enough that a single score — k-NN distance in a fixed pretrained feature space — predicts the errors of arbitrary downstream models (architectures, tasks, training data) at practically useful accuracy.
- **Problem:** Difficulty is treated as model-specific, requiring per-model uncertainty machinery, while the strong cross-model error correlations observed in practice hint at a shared, image-intrinsic hardness factor with one cheap estimator.
- **Core Hypothesis:** A fixed-backbone density score predicts error probability for unseen models with AUC comparable to those models' own confidence, transfers across tasks (classification errors predict segmentation errors on the same images), and its failure cases identify the genuinely model-specific error residual worth studying.
- **Why Important:** A universal hardness oracle enables model-agnostic routing, data triage, and evaluation stratification without touching the deployed model.
- **Why Possibly Novel:** Cross-model, cross-task error prediction from one fixed score has not been validated as a primary claim.
- **Minimal Experiment:** Compute the density score on ImageNet/COCO evaluation data; predict errors of 20 diverse models; compare AUC against model-own confidences; test cross-task transfer.
- **Main Risk:** The score may reduce to "atypicality" and fail on adversarially clean but hard items; residual analysis is part of the contribution.
- **Cluster:** GENERAL

### C-0343 · Neural collapse is an epiphenomenon
- **One-sentence idea:** Test whether the widely studied neural-collapse geometry (simplex ETF structure of last-layer features) has any causal relevance to generalization by training models with collapse explicitly prevented and showing unchanged downstream behavior.
- **Problem:** A sizable theory literature treats neural collapse as explaining or enabling generalization/transfer, but interventional evidence that collapse *matters* — rather than being a terminal-phase symptom — is absent.
- **Core Hypothesis:** Anti-collapse constraints (feature-spread regularizers, fixed non-ETF classifiers) leave ID accuracy, OOD robustness, and transfer statistically unchanged across scales, and collapse degree across recipes fails to correlate with any downstream property — demoting collapse to a descriptive curiosity.
- **Why Important:** Redirects theoretical attention from a possibly irrelevant geometry to properties that causally matter, or (if refuted) finally establishes collapse's functional role.
- **Why Possibly Novel:** Interventional anti-collapse studies with comprehensive downstream endpoints have not been conducted; the literature is observational and theoretical.
- **Minimal Experiment:** Train matched models with {standard, anti-collapse-regularized, fixed-random-classifier} heads at 2 scales; measure collapse metrics and a full downstream battery.
- **Main Risk:** Preventing collapse without side effects on optimization requires careful regularizer design to keep the comparison clean.
- **Cluster:** GENERAL

### C-0344 · Diversity, not size, sets the few-shot slope
- **One-sentence idea:** Show that a measurable diversity statistic of the pretraining corpus — not its raw size — predicts downstream few-shot sample efficiency, by constructing same-size corpora of controlled diversity and measuring adaptation curves.
- **Problem:** Data-scaling discourse is organized around corpus size, while the intuition that "diversity matters more" remains unoperationalized — no accepted diversity metric, no controlled evidence, no predictive law.
- **Core Hypothesis:** At fixed image count and compute, corpora with higher measured diversity (cluster-coverage entropy in a reference feature space) produce models with steeper few-shot learning curves downstream, size-vs-diversity trade-off surfaces show diversity dominating beyond modest sizes, and the diversity statistic predicts few-shot slopes across corpus constructions.
- **Why Important:** Converts data strategy from "collect more" to "collect what," with a computable acquisition criterion — arguably the highest-leverage open question in data-centric ML.
- **Why Possibly Novel:** Controlled same-size diversity manipulations with validated predictive metrics are missing; existing evidence conflates size and diversity.
- **Minimal Experiment:** Build 6 same-size corpora spanning a diversity range from one pool; pretrain matched models; measure few-shot curves on 10 tasks; fit and validate the diversity law.
- **Main Risk:** Diversity metric choice is the crux; several candidate metrics must be compared for predictive power to avoid circularity.
- **Cluster:** GENERAL

### C-0345 · Knowledge learned in language transfers to visual judgment — or doesn't
- **One-sentence idea:** Test whether VLMs apply relational knowledge acquired purely through text (size relations, part structures, physical properties never depicted in training images) to visual tasks — a direct measurement of cross-modal knowledge transfer that the multimodal paradigm presumes but rarely verifies.
- **Problem:** The case for language supervision in vision rests on knowledge transferring across modalities, yet clean tests separating verbally-acquired from visually-acquired knowledge are missing — existing benchmarks confound the two sources.
- **Core Hypothesis:** For facts documented in text but controlled to be visually absent from training (verifiable via corpus audits or controlled fine-tuning injections), VLMs apply the knowledge in text-mode queries but fail matched visual-mode queries — cross-modal transfer is far weaker than assumed, localized to the language pathway.
- **Why Important:** Quantifies what language actually buys visual understanding — the foundational premise of the VLM program — with implications for what must still be taught visually.
- **Why Possibly Novel:** Controlled knowledge-injection studies isolating modality-of-acquisition from modality-of-use have not been run on VLMs.
- **Minimal Experiment:** Inject synthetic relational facts via text-only fine-tuning; test application in visual judgment tasks (relative size selection, anomaly detection) against text-mode controls.
- **Main Risk:** Ensuring injected facts remain visually unobserved requires synthetic concepts, which may limit naturalness.
- **Cluster:** GENERAL

### C-0346 · Learned training components overfit their meta-distribution silently
- **One-sentence idea:** Audit learned pipeline components (learned optimizers, learned augmentation policies, learned loss functions) for catastrophic meta-overfitting — strong performance within their meta-training task distribution and silent failure outside it — with a transferable measurement protocol for "meta-generalization radius."
- **Problem:** Learned components are published with evaluations drawn from distributions resembling their meta-training tasks, and adopted by users whose tasks are not; the meta-generalization boundary is never characterized, making adoption a lottery.
- **Core Hypothesis:** Learned optimizers/policies degrade below hand-designed defaults once task distance (architecture family, data modality, scale) exceeds a measurable radius, the radius is narrow for current methods, and radius-expanding meta-training (task-distribution diversity) trades peak performance for usable generality — a measurable frontier.
- **Why Important:** Establishes the honest operating envelope for a growing class of "learned everything" methods before they embed silently in tools.
- **Why Possibly Novel:** Systematic meta-generalization-radius measurement across learned-component families has not been formalized.
- **Minimal Experiment:** Take 4 published learned components; evaluate across task grids ordered by distance from meta-training; map failure boundaries; test diversity-augmented re-meta-training.
- **Main Risk:** Reproducing learned components faithfully is engineering-heavy; scope may need to prioritize 2 component families.
- **Cluster:** GENERAL

### C-0347 · Aggressive data pruning trades ID accuracy for OOD generality
- **One-sentence idea:** Show that dataset pruning at high ratios does not merely approximate full-data training but *changes the generalization profile* — pruned-trained models losing ID accuracy while gaining OOD robustness — because pruning metrics preferentially remove distribution-core redundancy and retain boundary/rare structure.
- **Problem:** Pruning research optimizes for matching full-data ID accuracy, framing pruning as lossy compression; the possibility that pruning *reshapes* what is learned (a different, sometimes preferable trade-off) is unexamined.
- **Core Hypothesis:** At 70–90% pruning with margin-based metrics, models show measurably better OOD accuracy per unit ID accuracy than full-data models (a different point on the trade-off frontier, not just a worse one), the effect direction depends on the pruning metric's core-vs-edge preference, and pruning can be tuned to target desired ID/OOD profiles.
- **Why Important:** Reframes pruning from a cost-saving approximation into a distribution-shaping tool — a new control surface for generalization.
- **Why Possibly Novel:** ID/OOD profile analysis of pruned-data training is absent; the literature reports ID retention only.
- **Minimal Experiment:** Train on prunings {50–95%} × 3 metrics; evaluate ID and OOD suites; map trade-off frontiers against full-data anchors.
- **Main Risk:** Effects may be small at practical pruning ratios; high-ratio regimes carry the claim but limit direct applicability.
- **Cluster:** GENERAL

### C-0348 · Underspecification grows with scale
- **One-sentence idea:** Measure the "underspecification volume" of modern training pipelines — how differently identically-scoring models can behave OOD — across model scale, testing the uncomfortable hypothesis that scale *increases* the behavioral spread of equivalent models rather than pinning it down.
- **Problem:** Underspecification (equal ID performance, divergent deployment behavior) was documented in the CNN era; the field implicitly assumes better, larger models are more determined by their training criterion, without any scale-resolved measurement.
- **Core Hypothesis:** Across seed/data-order ensembles at each scale, ID performance spread shrinks with scale while OOD behavioral spread (per-slice accuracy variance, disagreement rates on shifted data) grows or stays flat — larger models have more unconstrained capacity in exactly the regions evaluation doesn't reach, making single-run reporting less meaningful with scale.
- **Why Important:** If scale amplifies underspecification, the field's single-checkpoint release-and-evaluate practice becomes increasingly unsound, and stress evaluation must scale with models.
- **Why Possibly Novel:** Scale-resolved underspecification measurement has not been performed; the original studies predate modern scaling.
- **Minimal Experiment:** Train seed ensembles (n=10) at 4 scales on fixed data; measure ID spread and OOD/slice behavioral spread; test the scale trend.
- **Main Risk:** Compute cost of ensembles at the largest scale bounds the trend's reach; careful extrapolation framing needed.
- **Cluster:** GENERAL

### C-0349 · Much of the "domain gap" is an annotation-convention gap
- **One-sentence idea:** Quantify how much of measured cross-dataset performance drops in segmentation/detection stems from annotation-convention differences (boundary placement, class definitions, granularity, void handling) rather than image-distribution shift — by re-annotating image subsets under both conventions.
- **Problem:** Cross-dataset evaluation is interpreted as measuring image-domain generalization, but datasets differ simultaneously in annotation protocols; the two gap sources have never been separated, inflating "domain gap" narratives and misdirecting adaptation research.
- **Core Hypothesis:** Re-annotating target-dataset images under the source dataset's protocol recovers a large fraction (plausibly 30–60%) of the cross-dataset performance drop, the annotation-gap share varies predictably with class-definition distance between protocols, and adaptation methods claimed to bridge "domain gaps" partly learn annotation-style translation.
- **Why Important:** Correct gap decomposition changes what cross-dataset numbers mean and what adaptation methods should optimize — image robustness or convention translation.
- **Why Possibly Novel:** Protocol-controlled re-annotation as a gap-decomposition instrument has not been applied systematically.
- **Minimal Experiment:** Re-annotate 500 images from dataset B under dataset A's guidelines (and vice versa); evaluate A-trained models against both annotation versions; decompose the gap.
- **Main Risk:** Re-annotation cost and guideline-fidelity enforcement are the practical constraints; inter-annotator agreement must be tracked.
- **Cluster:** GENERAL

### C-0350 · Scale buys interpolation, not geometric extrapolation
- **One-sentence idea:** Test whether model scaling improves generalization to genuinely novel geometric conditions (unseen viewpoints, extreme scales, unusual object orientations) or only densifies interpolation within seen conditions — predicting flat or negative scaling curves for true geometric extrapolation.
- **Problem:** Scaling narratives cite broad benchmark gains as evidence of better generalization, without separating interpolative coverage (more data ≈ fewer truly novel test conditions) from extrapolative capability — the distinction that determines behavior in open-world corners.
- **Core Hypothesis:** On controlled geometric extrapolation tests (held-out viewpoint sectors, scale ranges excluded from training via filtering), performance scales far more weakly with model/data size than standard benchmarks suggest, approaching flat for rotation extrapolation — scale improves coverage, not geometric abstraction.
- **Why Important:** Deployment risk lives in extrapolative corners; knowing that scale doesn't buy this capability redirects effort toward explicit geometric structure or targeted data.
- **Why Possibly Novel:** Extrapolation-vs-interpolation decomposition with controlled geometric holdouts across a scale ladder has not been executed.
- **Minimal Experiment:** Construct viewpoint/scale-sector holdout datasets (synthetic + filtered real); evaluate a model scale ladder; compare within-sector vs. extrapolated scaling slopes.
- **Main Risk:** Web pretraining leakage into "held-out" geometric conditions requires strict filtering verification for the real-data arm.
- **Cluster:** GENERAL

### C-0351 · The boundary of task arithmetic: semantic edits compose, spatial ones don't
- **One-sentence idea:** Map when task-vector arithmetic (adding/subtracting fine-tuning weight deltas) works, testing the hypothesis that semantic task edits compose linearly while spatially structured task edits (dense tasks, localization) interfere destructively — a predictable boundary defined by task type.
- **Problem:** Task arithmetic is presented with cherry-picked successes and unexplained failures; without a boundary theory, the technique is unusable in practice and uninformative about weight-space structure.
- **Core Hypothesis:** Composition fidelity is high for classification-style semantic tasks (near-orthogonal deltas in weight space), degrades systematically with the spatial-structure content of tasks (dense deltas overlap in spatial-processing layers, measurable via per-layer delta alignment), and per-layer alignment statistics predict composition success before trying it.
- **Why Important:** A predictive composition rule turns model merging from alchemy into engineering and reveals how task types occupy weight space.
- **Why Possibly Novel:** Task-type-resolved composition analysis with predictive alignment statistics has not been formulated.
- **Minimal Experiment:** Fine-tune one backbone on 12 tasks spanning semantic-to-spatial; evaluate all pairwise compositions; regress composition fidelity on task-type features and delta-alignment metrics.
- **Main Risk:** Results may depend on fine-tuning method (LoRA vs. full) requiring both to establish generality.
- **Cluster:** GENERAL

### C-0352 · The OOD gap decomposes into feature failure vs readout misalignment
- **One-sentence idea:** Decompose out-of-distribution performance drops into feature-space failure (information lost) versus readout misalignment (information present, classifier miscalibrated to shifted geometry), by measuring how much of each gap a small-sample readout refit recovers across many shift types.
- **Problem:** OOD failures are treated monolithically, driving representation-level solutions, while the cheap alternative — the features are fine, the readout is stale — has never been quantified systematically across shift types and models.
- **Core Hypothesis:** Refitting only the readout on ≤100 shifted examples recovers a large, shift-type-dependent fraction of the OOD gap (high for style/corruption shifts, low for semantic shifts), producing a decomposition map that predicts which deployments need representation work versus cheap recalibration.
- **Why Important:** The decomposition determines the correct engineering response to observed OOD failure — a triage tool the field lacks.
- **Why Possibly Novel:** Readout-refit gap decomposition as a general, shift-taxonomy-resolved measurement (rather than isolated observations) has not been assembled.
- **Minimal Experiment:** For 12 models × 10 shift benchmarks, measure zero-shot OOD gap and k-sample readout-refit recovery curves; publish the decomposition atlas.
- **Main Risk:** Refit-sample selection effects require careful sampling protocols and repeated draws.
- **Cluster:** GENERAL

### C-0353 · Degradation-curve shape is a scale signature
- **One-sentence idea:** Characterize the *shape* (not just level) of accuracy-vs-shift-magnitude curves across model scales, testing the hypothesis that small models degrade convexly (graceful) while large models degrade concavely (cliff-like) — better average robustness purchased with sharper failure onset.
- **Problem:** Robustness comparisons report levels at fixed severities; if scale changes curve shape, large models can dominate at benchmark severities while being *more* dangerous near their failure cliffs — a deployment-critical structure invisible in standard reporting.
- **Core Hypothesis:** Normalized degradation curves show systematic convexity change with scale (large models hold performance then collapse rapidly), the cliff location varies unpredictably across shift types (unforecastable failure), and curve-shape metrics differentiate models that levels-based rankings call equivalent.
- **Why Important:** Failure-onset sharpness is a first-order safety property; scale-dependent cliff behavior would temper "bigger is more robust" deployment reasoning.
- **Why Possibly Novel:** Curve-shape (convexity) analysis of robustness as a function of scale has not been formalized.
- **Minimal Experiment:** Measure fine-grained severity sweeps for a model scale ladder across 8 shift types; fit convexity metrics; test the scale-shape relationship.
- **Main Risk:** Severity parameterization affects apparent shape; requires perceptually or informationally calibrated severity axes.
- **Cluster:** GENERAL

### C-0354 · Scene complexity, not category count, drives pretraining transfer
- **One-sentence idea:** Test whether the operative variable in pretraining-data quality is per-image scene complexity (object count, occlusion, layout richness) rather than the corpus-level category diversity the field optimizes, by constructing corpora that decouple the two.
- **Problem:** Data curation targets category/vocabulary coverage, while the possibility that a smaller set of *complex scenes* teaches more transferable features than many simple object-centric images has no controlled evidence — the two properties are conflated in every natural corpus.
- **Core Hypothesis:** At matched image count and category coverage, high-complexity corpora yield better dense-task and relational transfer (with equal classification transfer), complexity effects saturate later than category effects, and a per-image complexity score predicts marginal data value — reshaping acquisition priorities toward scene richness.
- **Why Important:** Data acquisition budgets currently buy category breadth; if complexity dominates for the growing dense/relational workload, collection strategy should invert.
- **Why Possibly Novel:** Complexity-vs-category decoupled corpus construction with transfer endpoints has not been executed.
- **Minimal Experiment:** Build matched corpora {simple-diverse, complex-narrow, complex-diverse} from a large pool via detection-based complexity scoring; pretrain matched models; evaluate stratified transfer.
- **Main Risk:** Complexity correlates with image quality/source confounds requiring careful matching.
- **Cluster:** GENERAL

### C-0355 · Head-class data improves tail-class generalization
- **One-sentence idea:** Test the counterintuitive allocation hypothesis that adding more *head-class* data improves tail-class performance — because tail classes are recognized through compositional reuse of features refined on head classes — inverting the standard rebalancing prescription.
- **Problem:** Long-tail practice assumes tail improvement requires tail data or reweighting; the feature-reuse pathway (head data → better shared features → better tail readouts) is plausible but unmeasured as an allocation option.
- **Core Hypothesis:** At fixed annotation budget, allocating marginal data to head classes improves tail-class few-shot accuracy more than allocating it to the tail itself, up to a measurable crossover; the mechanism is verifiable through feature-attribution overlap between head and tail classes; and the crossover point depends on head-tail feature-sharing statistics computable in advance.
- **Why Important:** Would invert data-collection strategy for every long-tail application, replacing expensive rare-class collection with cheap common-class collection in the identified regime.
- **Why Possibly Novel:** Cross-class data-allocation experiments with feature-reuse mechanism verification have not been performed.
- **Minimal Experiment:** On a long-tail benchmark, train models across marginal-allocation arms {+head, +tail, +balanced} at matched budgets; measure tail accuracy; quantify head-tail feature sharing as the moderator.
- **Main Risk:** The effect plausibly reverses for tail classes with unique features (no reuse pathway), requiring sharing-stratified analysis.
- **Cluster:** GENERAL

### C-0356 · Shortcut removal is whack-a-mole: the cue-hierarchy law
- **One-sentence idea:** Show that removing a shortcut cue from training does not produce robust features but shifts reliance to the next-simplest available cue — a measurable, ordered cue hierarchy — implying shortcut mitigation must address the hierarchy, not individual cues.
- **Problem:** Shortcut-mitigation papers demonstrate removal of one cue and declare victory, without testing what the model uses instead — the sequential structure of shortcut reliance is unmapped.
- **Core Hypothesis:** Under iterative cue removal (texture, then color, then local shape...), models traverse a stable, architecture-consistent cue hierarchy ordered by a measurable simplicity metric; robustness to real shifts improves only marginally per removal step until semantic cues are reached; and the full hierarchy predicts which mitigation combinations are (in)effective.
- **Why Important:** Explains why individual shortcut fixes disappoint on real shifts and provides the map required for effective multi-cue interventions.
- **Why Possibly Novel:** Iterative-removal hierarchy mapping with cross-architecture consistency tests has not been done; shortcut studies are single-cue.
- **Minimal Experiment:** Construct datasets enabling sequential cue ablation; train models at each hierarchy stage; measure cue reliance (cue-conflict probes) and real-shift robustness per stage.
- **Main Risk:** Cue ablations interact (removing texture alters color statistics); careful orthogonalized constructions are needed.
- **Cluster:** GENERAL

### C-0357 · Deduplication hurts small-data training
- **One-sentence idea:** Test the hypothesis that data deduplication — an unquestioned hygiene step — *harms* training in small-data regimes, where natural duplication acts as beneficial importance weighting, making dedup policy scale-dependent rather than universal.
- **Problem:** Dedup is applied uniformly from web-scale wisdom, but duplication frequency in natural collections encodes relevance/typicality information whose removal at small scale may flatten a useful implicit curriculum — an unexamined regime dependence.
- **Core Hypothesis:** Below a dataset-size threshold, deduplicated training underperforms duplication-preserved training on downstream accuracy (duplication ≈ natural importance weights), the effect inverts at scale (dedup prevents memorization waste), and reweighting by duplication counts recovers the small-scale benefit without storage cost — yielding a scale-conditioned dedup policy.
- **Why Important:** Dedup guidance shapes every dataset pipeline; a demonstrated regime inversion would correct blanket policy with a measurable threshold.
- **Why Possibly Novel:** Scale-resolved dedup-value curves with the importance-weighting mechanism test have not been published.
- **Minimal Experiment:** Train across dataset scales {10k..10M} with {raw, deduped, deduped+count-reweighted} variants; map the value curve and locate the inversion.
- **Main Risk:** Natural-duplication structure varies by source (social media vs. curated), requiring multiple corpus types.
- **Cluster:** GENERAL

### C-0358 · Unlabeled invariance metrics beat ID validation for robust checkpoint selection
- **One-sentence idea:** Show that selecting checkpoints/hyperparameters by ID validation accuracy systematically picks less shift-robust models than selecting by cheap unlabeled invariance statistics (prediction consistency under augmentation on unlabeled target-like data) — challenging the universal selection practice.
- **Problem:** Every pipeline selects by ID validation, which cannot see robustness differences among near-tied checkpoints; the field lacks a validated label-free alternative even though robustness is often the deployment priority.
- **Core Hypothesis:** Among ID-accuracy-tied checkpoints from typical runs, OOD performance varies substantially; unlabeled consistency metrics rank-predict this OOD variation well; and consistency-based selection improves deployed robustness at zero ID cost across tasks — ID validation is leaving robustness on the table in every run.
- **Why Important:** A drop-in selection-rule change with field-wide applicability and no labeling cost.
- **Why Possibly Novel:** Consistency metrics exist for OOD estimation; their use and validation as *checkpoint-selection* instruments against the ID-validation default is not established practice.
- **Minimal Experiment:** For 10 training runs, evaluate all checkpoints on ID validation, unlabeled consistency, and OOD suites; compare selection policies' OOD outcomes.
- **Main Risk:** Consistency metrics may be gameable by trivially invariant (over-smoothed) checkpoints, requiring composite selection criteria.
- **Cluster:** GENERAL

### C-0359 · The sim2real gap is mostly low-level statistics
- **One-sentence idea:** Test the hypothesis that most of the synthetic-to-real transfer gap for segmentation is carried by low-level image statistics (color distribution, noise, frequency spectra) fixable with cheap statistical alignment — and that the celebrated "content/semantic gap" is a minor residual.
- **Problem:** Sim2real research invests in photorealistic rendering and sophisticated domain adaptation under the belief that the gap is deep and semantic; the cheap-alignment null hypothesis has never been given a maximal, tuned defense.
- **Core Hypothesis:** Matched-statistics synthetic training (histogram/frequency/noise alignment to target, no semantic changes) closes the majority of the sim2real mIoU gap on driving benchmarks, the residual correlates with layout distribution mismatch (measurable), and expensive photorealism improvements add little beyond statistics alignment — re-ranking where sim2real effort should go.
- **Why Important:** Redirects synthetic-data investment from rendering quality toward cheap statistical post-processing plus layout diversity — an immediate cost lever.
- **Why Possibly Novel:** Maximal low-level-alignment baselines with gap decomposition have not been the centerpiece of a sim2real study.
- **Minimal Experiment:** Train segmenters on GTA-style synthetic data {raw, statistics-aligned, photorealism-enhanced}; evaluate on Cityscapes; decompose remaining gaps against layout-mismatch metrics.
- **Main Risk:** Alignment techniques risk leaking target information; strictly unlabeled-target protocols and leakage audits are required.
- **Cluster:** GENERAL

### C-0360 · A resolution ceiling law for fine-grained transfer
- **One-sentence idea:** Establish that fine-grained downstream capability is bounded by a computable pretraining resolution/patch-size ceiling — features for details smaller than the effective sampling scale cannot exist and are not recoverable by fine-tuning — replacing "more data/capacity will fix it" expectations with a hard law.
- **Problem:** Fine-grained transfer failures are attributed vaguely to data or capacity, and practitioners attempt to fine-tune their way past what may be an information-theoretic ceiling set by pretraining sampling geometry — with no predictive rule for when that works.
- **Core Hypothesis:** Downstream fine-grained accuracy saturates as a function of (task detail scale ÷ pretraining effective sampling scale) with a universal curve across backbones; below ratio 1, no amount of downstream data or head capacity recovers performance without backbone re-exposure to higher resolution; and the law predicts, in advance, which tasks a given checkpoint can serve.
- **Why Important:** A predictive ceiling law prevents wasted adaptation effort and gives checkpoint publishers a principled spec ("serves detail scales above X") — basic infrastructure the ecosystem lacks.
- **Why Possibly Novel:** Sampling-scale ceiling formulation with cross-backbone universal-curve validation has not been established for transfer.
- **Minimal Experiment:** Evaluate backbones spanning patch sizes/training resolutions on fine-grained tasks with controlled detail scales (synthetic + natural); fit the ratio law; test downstream-data-scaling immunity below the ceiling.
- **Main Risk:** Attention may partially integrate sub-patch information via phase effects, softening the hard-ceiling claim into a strong-attenuation law.
- **Cluster:** GENERAL
## Sub-cluster WILDCARD — Meta-Science, Tooling, and Cross-Cutting Bets (C-0361 – C-0372)

### C-0361 · Agent-run replication at literature scale
- **One-sentence idea:** Build and validate an autonomous agent pipeline that re-executes published vision experiments from paper+code artifacts, producing the first literature-scale replication census and a taxonomy of why vision results fail to reproduce.
- **Problem:** Replication in computer vision is anecdotal because human replication cost is prohibitive; agentic execution changes the economics but its reliability as a replication instrument is itself unmeasured.
- **Core Hypothesis:** Agents can faithfully re-execute a substantial fraction of papers-with-code experiments (validated against known-good references), and the resulting census reveals systematic reproducibility predictors (dependency decay, undocumented preprocessing, tuning asymmetries) invisible to case studies.
- **Why Important:** Converts reproducibility from an ethics discussion into a measured, monitorable property of the field, with an instrument others can reuse.
- **Why Possibly Novel:** Agent-based replication has been piloted in ML narrowly; a validated vision-specific census with failure taxonomy does not exist.
- **Minimal Experiment:** Validate the agent on 10 known-reproducible baselines; run it on a random sample of 50 papers-with-code segmentation/classification claims; report replication rates and failure categories.
- **Main Risk:** Agent failures could be misattributed as paper failures; the validation set and human adjudication layer are essential.
- **Cluster:** WILDCARD

### C-0362 · Experts can't predict which results replicate
- **One-sentence idea:** Measure the calibration of computer-vision researchers' beliefs by eliciting forecasts on which published improvements will replicate (before running the replications), testing whether the community's intuition carries any signal — and publishing the calibration curve.
- **Problem:** Research prioritization, reviewing, and citation all rely on expert judgment about which results are real, a judgment whose accuracy has never been measured in this field.
- **Core Hypothesis:** Expert forecasts on replication outcomes are barely better than chance and overconfident, with predictable biases (venue prestige and method elegance inflate belief), while simple observable features (error bars, margin size) outperform expert intuition — mirroring findings from psychology's replication markets.
- **Why Important:** If expert intuition is uncalibrated, the field's informal quality-control mechanisms need replacement by measurable indicators — a structural insight with reviewing-policy consequences.
- **Why Possibly Novel:** Forecasting-based meta-science has not been run for computer vision claims.
- **Minimal Experiment:** Elicit forecasts from 100 researchers on 20 pre-selected claims; run the replications (shared with C-0300 infrastructure); score calibration and compare against feature-based predictors.
- **Main Risk:** Recruiting forecasters and running replications is logistically heavy; piggy-backing on a replication project is the feasible path.
- **Cluster:** WILDCARD

### C-0363 · The half-life of training tricks
- **One-sentence idea:** Measure the decay of published training tricks' effectiveness as base recipes evolve — fitting "half-life curves" for a sample of once-beneficial techniques re-evaluated under successive recipe generations — to quantify how much of the methods literature is transient recipe-interaction.
- **Problem:** Techniques validated against one era's baselines persist in citation and adoption long after recipe evolution has absorbed or inverted their benefit, and the field has no measurement of this decay process.
- **Core Hypothesis:** Most sampled tricks lose the majority of their measured benefit within two recipe generations (their effect having been an interaction with since-fixed weaknesses), a minority are recipe-robust, and robustness is predictable from whether the trick addresses data information content versus optimization mechanics.
- **Why Important:** A measured half-life distribution would recalibrate how the community values incremental method papers and identify the durable-contribution signature worth optimizing for.
- **Why Possibly Novel:** Longitudinal re-evaluation of tricks across recipe eras, framed as decay measurement, has not been done.
- **Minimal Experiment:** Select 15 tricks from 2016–2022; re-evaluate each under {original, mid-era, current} recipes on fixed tasks; fit decay curves and test the durability predictor.
- **Main Risk:** Faithful reconstruction of era recipes requires careful archaeology; disagreements about "current recipe" require multiple modern baselines.
- **Cluster:** WILDCARD

### C-0364 · Citations and production adoption measure different methods
- **One-sentence idea:** Quantify the divergence between academic impact (citations) and real adoption (presence in production configs, framework defaults, competition-winning solutions) for vision methods, characterizing what the two selection processes each reward.
- **Problem:** The field's incentive system optimizes citations, presuming they track usefulness; the adoption record — measurable from public configs, competition write-ups, and framework code — has never been systematically compared against citation rankings.
- **Core Hypothesis:** Citation and adoption rankings correlate weakly beyond a few flagship methods; adoption favors robustness-to-misuse and implementation simplicity (measurable properties) while citations favor novelty framing; and the divergence is growing over time — implying the field's reward signal increasingly decouples from utility.
- **Why Important:** Evidence-based incentive critique with concrete data would inform how methods should be evaluated and what "impact" claims mean.
- **Why Possibly Novel:** Adoption mining from configuration ecosystems (mmdetection/detectron2 configs, Kaggle solutions) as a quantitative counterpart to citations is unexplored.
- **Minimal Experiment:** Mine adoption signals for 200 methods from public config corpora and competition reports; compare against citation trajectories; model what predicts each.
- **Main Risk:** Adoption mining has coverage bias toward open ecosystems; industrial adoption remains partially invisible and must be bounded honestly.
- **Cluster:** WILDCARD

### C-0365 · Which pre-deep-learning ideas revive on foundation features?
- **One-sentence idea:** Systematically re-test the classical segmentation toolbox (CRFs, superpixels, contour grouping, MRF priors) on top of modern foundation features, testing the hypothesis that several "obsolete" structured methods become competitive again once their unary terms are strong — a directed archaeology of discarded ideas.
- **Problem:** Classical methods were abandoned when their feature inputs were weak, not necessarily because their structural priors were wrong; nobody has audited which discarded components add value back on top of modern representations.
- **Core Hypothesis:** Structured inference components encoding priors that current end-to-end models still violate (boundary-region consistency, global topology) provide measurable gains over learned decoders on foundation features — with the revived subset predictable from which priors modern failure analyses show are still unmet.
- **Why Important:** Cheap gains from existing well-understood machinery, plus a methodological lesson about how the field discards ideas for contingent reasons.
- **Why Possibly Novel:** Piecemeal CRF-revival papers exist; the systematic audit across the classical toolbox with failure-mode-matched prediction does not.
- **Minimal Experiment:** Combine 6 classical components with frozen DINOv2/SAM features on 3 segmentation benchmarks; compare against learned-decoder baselines at matched inference cost; map gains to failure-mode categories.
- **Main Risk:** Tuning classical components fairly requires expertise that has partly left the field; implementation quality is the main threat.
- **Cluster:** WILDCARD

### C-0366 · Implementation variance: the same method, five labs, five results
- **One-sentence idea:** Run a controlled multi-team experiment where independent groups implement the same method from its paper description alone, measuring the distribution of results attributable purely to implementation degrees of freedom — the field's unquantified "implementation noise floor."
- **Problem:** Method comparisons across papers implicitly assume papers determine implementations; undocumented choices (initialization details, data pipeline minutiae) may span performance ranges comparable to claimed contributions, but this variance has never been measured directly in vision.
- **Core Hypothesis:** Independent reimplementations of one well-described segmentation method vary by margins comparable to typical SOTA deltas, the variance concentrates in identifiable underdocumented components (augmentation details, schedule interpretation), and a documentation checklist derived from the variance analysis measurably shrinks re-implementation spread.
- **Why Important:** Quantifies the reproducibility value of documentation standards with experimental (not anecdotal) evidence, directly informing venue policies.
- **Why Possibly Novel:** Multi-team controlled reimplementation studies exist in software engineering but not for modern vision methods.
- **Minimal Experiment:** Recruit 5 independent implementers for one method under communication quarantine; compare results; interview-diff implementations; derive and validate the checklist on a second method.
- **Main Risk:** Small-n team samples limit statistical strength; framing as a case study with component attribution keeps it honest.
- **Cluster:** WILDCARD

### C-0367 · Benchmark lifecycle dynamics are predictable
- **One-sentence idea:** Fit lifecycle models to the historical trajectories of vision benchmarks (adoption, discrimination power, saturation, post-saturation misuse) and test whether the fitted dynamics predict — in advance — when current benchmarks will stop discriminating between methods.
- **Problem:** The community discovers benchmark saturation retroactively, after years of publishing indistinguishable "improvements"; a predictive model of benchmark aging would enable proactive evaluation planning.
- **Core Hypothesis:** Benchmark discrimination power (effect-size distribution of year-over-year improvements) follows a common decay law driven by measurable covariates (headroom, leaderboard query volume, method monoculture), and the fitted law predicts remaining useful lifetime of active benchmarks within useful error.
- **Why Important:** Evaluation infrastructure planning — when to build successors, when to distrust deltas — currently runs on intuition; a validated aging model makes it quantitative.
- **Why Possibly Novel:** Benchmark aging has been lamented qualitatively; lifecycle curve-fitting with prospective prediction has not been attempted.
- **Minimal Experiment:** Reconstruct improvement-size time series for 15 retired/mature benchmarks; fit lifecycle models; issue registered predictions for 5 active benchmarks and evaluate after a fixed window.
- **Main Risk:** Historical leaderboard data is incomplete and survivorship-biased, requiring careful corpus construction from papers.
- **Cluster:** WILDCARD

### C-0368 · Measuring the file drawer: the field's unpublished nulls
- **One-sentence idea:** Estimate the volume and content of unpublished negative results in vision research through structured researcher surveys and lab-notebook sampling, quantifying the file-drawer effect's size and identifying which "known-not-to-work" knowledge the community keeps re-purchasing.
- **Problem:** Every lab privately knows methods that don't work, re-discovers others' private nulls at full compute cost, and publishes only positives — but the magnitude of this hidden knowledge and its redundant re-discovery cost has never been estimated.
- **Core Hypothesis:** Surveyed researchers report multiple unpublished substantive nulls each, the nulls cluster heavily on identifiable popular hypotheses (the same failures re-discovered across labs), and the implied aggregate re-discovery compute cost is a large multiple of what a null-results registry would cost to run.
- **Why Important:** Provides the quantitative case (or counter-case) for null-result publication infrastructure with actual numbers instead of rhetoric.
- **Why Possibly Novel:** File-drawer quantification via structured elicitation has been done in psychology/medicine, never for machine learning research practice.
- **Minimal Experiment:** Design and run an anonymized survey of 300 researchers on unpublished negative results; validate a subsample against willing labs' records; estimate cluster structure and redundancy cost.
- **Main Risk:** Self-report bias and definitional fuzziness of a "null result" require careful instrument design and validation.
- **Cluster:** WILDCARD

### C-0369 · Compute-normalized progress curves for a decade of dense prediction
- **One-sentence idea:** Re-plot the last decade of segmentation/detection progress normalized by training compute and data cost, testing whether efficiency-adjusted progress has stalled — separating genuine algorithmic advance from resource escalation.
- **Problem:** Progress narratives cite absolute benchmark gains while training resources grew by orders of magnitude; the field lacks an agreed accounting of how much improvement is algorithmic versus purchased, especially for dense tasks.
- **Core Hypothesis:** Compute-normalized dense-task progress shows distinct eras — genuine algorithmic gains (2015–2019), followed by predominantly resource-driven gains — with recent algorithmic efficiency improving mainly at inference, not training; and the decomposition identifies which innovation classes actually shifted the efficiency frontier.
- **Why Important:** Resource-honest progress accounting informs research investment, hardware policy, and claims about the field's trajectory.
- **Why Possibly Novel:** Compute-normalized progress analyses exist for game-playing and language modeling; the dense-prediction version with innovation-class attribution does not.
- **Minimal Experiment:** Assemble training-cost estimates for 60 milestone dense-prediction models from papers/replications; fit efficiency frontiers over time; attribute frontier shifts to innovation categories.
- **Main Risk:** Training-cost reconstruction for older papers is approximate; conclusions need sensitivity analysis over cost-estimate error.
- **Cluster:** WILDCARD

### C-0370 · Hallucinated citations are propagating into the vision literature
- **One-sentence idea:** Measure the contamination of published vision papers with LLM-artifact errors — hallucinated references, misattributed claims, subtly wrong technical statements matching known LLM failure patterns — and model the propagation dynamics of such errors through subsequent citation.
- **Problem:** LLM writing assistance is now ubiquitous in paper production, and its characteristic errors (plausible fabricated citations, confident misstatements of related work) may be entering the permanent scientific record undetected, with unknown prevalence.
- **Core Hypothesis:** Detectable LLM-artifact errors (nonexistent references, claim-source mismatches verifiable against cited papers) appear at measurable and increasing rates in recent vision papers, cluster in related-work sections, and propagate — later papers repeat misattributed claims citing the intermediate paper — establishing a new form of literature corruption with quantifiable dynamics.
- **Why Important:** Scientific-record integrity is infrastructure; measured prevalence and propagation rates would justify (or dismiss) verification tooling at venues.
- **Why Possibly Novel:** Reference-hallucination audits exist for LLM outputs; measurement of their penetration into the published literature and citation-graph propagation does not.
- **Minimal Experiment:** Automatically verify all references and 200 sampled claim-citation pairs in 500 recent vision papers; compare error rates against a pre-2020 baseline; trace propagation of identified errors forward through citations.
- **Main Risk:** Attribution to LLM use (vs. human sloppiness) is indirect; the study must focus on error prevalence and propagation, using LLM-signature patterns only as secondary evidence.
- **Cluster:** WILDCARD

### C-0371 · The GPU lottery: hardware nondeterminism versus claimed margins
- **One-sentence idea:** Quantify the run-to-run performance variation attributable purely to hardware/software nondeterminism (kernel scheduling, cuDNN algorithm selection, driver versions) at fixed seeds, comparing this irreducible noise floor against the margins claimed in recent dense-prediction papers.
- **Problem:** Papers fix random seeds and believe their results deterministic, but atomics-based kernels and algorithm autotuning introduce nondeterminism whose downstream magnitude — through training's chaotic sensitivity — has never been measured against the scale of published claims.
- **Core Hypothesis:** Bitwise-identical training configurations produce final-metric spreads that are non-negligible (comparable to seed variance) through nondeterministic kernel accumulation orders, the spread grows with training length and model scale, and a measurable fraction of recent claimed improvements falls within this pure-hardware noise envelope.
- **Why Important:** Establishes the true noise floor of the field's measurement instrument — beneath which no claim is meaningful — and motivates deterministic-mode reporting standards.
- **Why Possibly Novel:** Hardware-nondeterminism folklore exists; its quantified propagation to final benchmark metrics at modern scale, compared against literature margins, does not.
- **Minimal Experiment:** Train identical-seed configurations 20× each on {deterministic, default} kernel settings for 3 tasks; measure final-metric spreads; compare against a survey of claimed margins.
- **Main Risk:** Results are hardware/stack-specific and must be replicated across at least two platforms to support general claims.
- **Cluster:** WILDCARD

### C-0372 · Adversarial collaboration as a research protocol for vision disputes
- **One-sentence idea:** Pilot adversarial collaboration — proponents and skeptics of a contested vision claim jointly preregister decisive experiments — on two live controversies (e.g., "language supervision improves dense features" and "attention is necessary at scale"), evaluating the protocol itself as a dispute-resolution instrument for the field.
- **Problem:** Vision controversies persist for years through parallel literatures that never run each other's controls; the field has no institutional mechanism for resolving them, and disputes are settled by fashion rather than decisive tests.
- **Core Hypothesis:** For most contested claims, a jointly-designed experiment acceptable to both sides exists and is affordable; adversarial preregistration produces designs that neither side's solo literature contained (measurably more controls); and outcomes shift participant beliefs more than equivalent solo publications — demonstrating a reusable protocol.
- **Why Important:** A working dispute-resolution mechanism would compress years of parallel contradictory publication into single decisive studies — a structural upgrade to how the field learns.
- **Why Possibly Novel:** Adversarial collaboration is established in psychology but has never been formally piloted for machine learning research disputes.
- **Minimal Experiment:** Recruit opposing researcher pairs for 2 disputes; facilitate joint preregistration; execute the agreed experiments; measure design quality and belief change against matched solo-study controls.
- **Main Risk:** Recruiting genuine opponents willing to precommit is the bottleneck; incentives (co-authorship, venue support) must be arranged in advance.
- **Cluster:** WILDCARD
