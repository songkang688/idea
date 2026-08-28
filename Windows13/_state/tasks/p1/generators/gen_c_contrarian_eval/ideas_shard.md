# P1 Wave A - Generator C Shard: Contrarian Evaluation (Windows13)

- **task_id**: `p1_gen_c_contrarian_eval`
- **role**: generator (candidate ideas only; NO verified-novelty claims)
- **windows_id**: Windows13 (locked; canonical state untouched)
- **territory**: Contrarian evaluation - calibration, uncertainty, benchmark/dataset weaknesses, negative results, ignored assumptions in vision foundation model evaluation
- **idea_count**: 104 (id_seed range `W13-P1-C-001` .. `W13-P1-C-104`)
- **evidence policy**: every record labels its claims with [KNOWN FACT] / [HYPOTHESIS] / [EXPECTED RESULT] / [MODEL SPECULATION]. No fabricated papers, numbers, datasets, or experimental results. All predictions are EXPECTED, none were run.
- **novelty status**: `why_possibly_novel` fields are UNVERIFIED model speculation; Wave B dedup + novelty verification must treat all of them as unchecked.

## Cluster overview

| cluster | count | ids |
|---|---|---|
| calibration | 12 | 001-012 |
| uncertainty | 10 | 013-022 |
| benchmark-contamination | 12 | 023-034 |
| metric-validity | 10 | 035-044 |
| protocol-assumptions | 10 | 045-054 |
| negative-results | 10 | 055-064 |
| human-baselines-annotation | 8 | 065-072 |
| statistics-reproducibility | 8 | 073-080 |
| robustness-shift-critique | 8 | 081-088 |
| vlm-eval-weaknesses | 10 | 089-098 |
| ignored-assumptions | 6 | 099-104 |

## Candidate ideas (one-liners)

### calibration (12)

- **W13-P1-C-001** - Zero-shot vision-language classifier calibration is dominated by prompt template choice rather than model quality, making calibration leaderboards prompt artifacts.
- **W13-P1-C-002** - Fixed-bin expected calibration error systematically misranks vision foundation models compared to debiased or binning-free calibration estimators.
- **W13-P1-C-003** - In-distribution calibration of vision foundation models carries near-zero information about their calibration under distribution shift.
- **W13-P1-C-004** - Full fine-tuning of vision foundation models improves in-distribution accuracy while systematically destroying calibration transferability relative to linear probing.
- **W13-P1-C-005** - Softmax-confidence-based selective prediction for vision foundation models is beaten by a plain nearest-neighbor distance in frozen feature space.
- **W13-P1-C-006** - Verbalized confidence from multimodal vision-language models is systematically less reliable than their own token-level log-probabilities on visual questions, contradicting the intuition that self-reports add information.
- **W13-P1-C-007** - Most published calibration differences between vision foundation models are within test-set resampling noise and would not survive a paired bootstrap.
- **W13-P1-C-008** - Aggregate calibration hides severe tail-class miscalibration: vision foundation models that look calibrated on average are strongly overconfident exactly on rare classes.
- **W13-P1-C-009** - Post-hoc calibration methods evaluated on held-out splits of the same distribution overstate their value because the fitted correction does not transfer across datasets.
- **W13-P1-C-010** - A measurable share of apparent overconfidence in vision foundation models is actually test-label error, and models are better calibrated with respect to corrected labels.
- **W13-P1-C-011** - Calibration evaluation for detection and segmentation is ill-defined as currently practiced because the confidence scores are ranking scores, not probabilities of any explicit event.
- **W13-P1-C-012** - Ensembles of vision foundation models improve calibration mostly by uniformly shrinking confidence rather than by improving the ranking of which inputs are risky.

### uncertainty (10)

- **W13-P1-C-013** - The epistemic-aleatoric uncertainty decomposition reported for vision models is not identifiable in practice: interventions designed to change one component move both estimates.
- **W13-P1-C-014** - Monte-Carlo dropout applied to heads on frozen foundation-model features yields uncertainty essentially uncorrelated with error, despite remaining a common default.
- **W13-P1-C-015** - Marginal coverage claims of conformal prediction on vision benchmarks conceal severe conditional coverage failures under realistic covariate shift.
- **W13-P1-C-016** - Standard out-of-distribution detection benchmarks are largely solvable by trivial low-level statistics, so reported method rankings measure benchmark artifacts.
- **W13-P1-C-017** - The embedding norm of a single deterministic forward pass predicts errors about as well as a deep ensemble for frozen vision foundation models.
- **W13-P1-C-018** - Uncertainty-method rankings established on small networks and datasets invert at foundation scale, so the field's canonical conclusions may not transfer to the models people actually deploy.
- **W13-P1-C-019** - Test-time-augmentation-based uncertainty mostly measures a model's augmentation sensitivity, not its predictive uncertainty, and the two decouple under simple interventions.
- **W13-P1-C-020** - For multimodal models, answer instability across paraphrased visual prompts predicts errors better than the model's own internal confidence signals.
- **W13-P1-C-021** - Error-detection AUROC as the standard uncertainty metric structurally favors accurate models, so uncertainty leaderboards partly re-measure accuracy.
- **W13-P1-C-022** - Conformal prediction sets on large-label-space vision tasks become so large under distribution shift that they are decision-theoretically worthless, and utility-based reporting would reveal this.

### benchmark-contamination (12)

- **W13-P1-C-023** - Contamination of vision benchmarks by web-scale pretraining is systematically underestimated because deduplication tools detect pixel duplicates but not semantic duplicates of the same scene.
- **W13-P1-C-024** - Zero-shot performance of vision foundation models is mostly seen-shot: accuracy stratified by similarity to pretraining data reveals the claimed generalization is concentrated where near-training content exists.
- **W13-P1-C-025** - Annotation error rates in flagship vision test sets exceed the score gaps separating leading foundation models, so leaderboard order among top models is not measurable with current labels.
- **W13-P1-C-026** - Perceptual-hash deduplication pipelines are blind to generative re-renderings, so benchmarks are increasingly contaminated by synthetic derivatives of their own test images.
- **W13-P1-C-027** - Val and test splits of legacy vision benchmarks are non-iid due to photographer, session, and source-page leakage, inflating scores relative to honest disjoint splits.
- **W13-P1-C-028** - Synthetic corruption benchmarks poorly predict degradation on real-world image quality problems, so corruption-robustness scores are a misleading proxy for deployment robustness.
- **W13-P1-C-029** - Benchmark aging is real: category semantics and visual distributions drift over time, so accuracy on decade-old test sets overstates accuracy on the same nominal task today.
- **W13-P1-C-030** - A large fraction of multiple-choice visual-question benchmarks remains solvable by language-only priors, and blind baselines are still not routinely reported for new benchmarks.
- **W13-P1-C-031** - Cross-model benchmark comparisons are silently invalidated by preprocessing mismatches, with resize interpolation and crop conventions contributing gaps comparable to claimed modeling advances.
- **W13-P1-C-032** - Adaptive overfitting to reused test sets is measurable in the foundation-model era: models released later gain more on the canonical test set than on fresh replicas, controlling for capability.
- **W13-P1-C-033** - Image-retrieval benchmark scores are inflated by near-duplicate galleries, and deduplicating the gallery reranks retrieval models.
- **W13-P1-C-034** - General-purpose vision benchmarks embed demographic and geographic confounds that make aggregate scores unrepresentative and cross-model comparisons unstable across subpopulations.

### metric-validity (10)

- **W13-P1-C-035** - Top-1 accuracy on multi-object images is an ill-posed metric that penalizes correct perception, and multi-label re-evaluation changes foundation-model rankings.
- **W13-P1-C-036** - Mean intersection-over-union hides boundary quality: segmenters with equal mIoU differ drastically in boundary fidelity, which dominates downstream utility in editing and medical use.
- **W13-P1-C-037** - Any fixed-feature-space distance metric for generative image evaluation is structurally gameable, and an adversarial-sensitivity audit should accompany every reported score.
- **W13-P1-C-038** - Averaging accuracy uniformly over corruption types assumes all corruptions are equally likely, and deployment-weighted robustness scores flip model rankings.
- **W13-P1-C-039** - Zero-shot retrieval recall correlates poorly with the end-task utility of embeddings inside retrieval-augmented multimodal pipelines.
- **W13-P1-C-040** - Model-based image-caption metrics are circular: they systematically favor captions stylistically similar to the judge's own training distribution, penalizing accurate but differently phrased descriptions.
- **W13-P1-C-041** - AUROC-based out-of-distribution detection rankings do not survive at deployment-relevant operating points, and FPR-at-high-TPR reorders published methods.
- **W13-P1-C-042** - Multi-task benchmark suite rankings are unstable under reasonable task reweighting, so suite-level leaderboards encode arbitrary editorial weight choices.
- **W13-P1-C-043** - Repeated-sampling metrics for multimodal generation conflate output diversity with capability, crediting models for stochastic variety rather than reliability.
- **W13-P1-C-044** - Micro-averaged accuracy hides that foundation-model progress is concentrated on frequent classes, and macro-averaged evaluation shows much flatter progress curves.

### protocol-assumptions (10)

- **W13-P1-C-045** - Uncontrolled prompt-engineering budgets act as hidden compute in zero-shot comparisons, and equalizing prompt-search effort shrinks or reverses claimed model gaps.
- **W13-P1-C-046** - Linear-probe evaluation encodes a linearity assumption about representation quality, and shallow nonlinear probes rerank vision backbones, undermining probe-based pretraining conclusions.
- **W13-P1-C-047** - Few-shot evaluation variance across support-set draws exceeds the model gaps typically reported, making single-draw few-shot comparisons close to meaningless.
- **W13-P1-C-048** - Frozen-backbone comparisons are confounded by head architecture and head-training recipes, and standardizing heads changes which backbone wins.
- **W13-P1-C-049** - Silent normalization-statistics adaptation at test time is inconsistently applied across robustness studies, contaminating a fraction of reported robustness gains.
- **W13-P1-C-050** - Image decoding and interpolation library differences alone shift benchmark scores enough to matter, making bit-level evaluation reproducibility a fiction across the field.
- **W13-P1-C-051** - Single-resolution evaluation systematically biases cross-model comparisons because models are trained at different native resolutions, and resolution-sweep reporting changes conclusions.
- **W13-P1-C-052** - Zero-shot classification rankings are unstable under synonym substitution of class names, revealing that benchmark-specific wording quietly advantages some models.
- **W13-P1-C-053** - Inconsistent, often unreported use of test-time augmentation across published results contaminates cross-paper comparisons by an amount comparable to claimed method gains.
- **W13-P1-C-054** - Random-seed variance in fine-tuning is large enough that many claimed state-of-the-art improvements at foundation scale are single-seed lottery wins.

### negative-results (10)

- **W13-P1-C-055** - Attention maps of vision transformers fail causal faithfulness tests: regions highlighted as evidence are often not the regions whose removal changes the prediction.
- **W13-P1-C-056** - Reported advantages of self-supervised pretraining over supervised pretraining shrink or vanish on several downstream tasks once augmentation pipelines and compute are strictly equalized.
- **W13-P1-C-057** - Scaling up vision models does not improve calibration under distribution shift beyond what improved accuracy mechanically implies: a negative result about scale as an uncertainty cure.
- **W13-P1-C-058** - Sophisticated data-curation pipelines for vision pretraining add little beyond simple deduplication plus basic quality filtering: a controlled negative result on curation complexity.
- **W13-P1-C-059** - Claimed emergent visual abilities in multimodal models are largely artifacts of discontinuous metrics, and smooth scoring reveals smooth scaling: a metric-artifact negative result.
- **W13-P1-C-060** - Chain-of-thought prompting yields no genuine gain on visual reasoning benchmarks once answer-format effects and extra-token compute are controlled: a null result behind a popular technique.
- **W13-P1-C-061** - Knowledge distillation from large vision foundation models transfers little beyond what label smoothing and better targets provide: a dark-knowledge null at foundation scale.
- **W13-P1-C-062** - Adversarial robustness gains do not transfer across threat models: a systematic cross-threat evaluation matrix showing mostly empty off-diagonals for modern vision defenses.
- **W13-P1-C-063** - Feature-space augmentation and mixing methods that helped small-scale training deliver no measurable benefit when fine-tuning foundation backbones: a scale-dependent null.
- **W13-P1-C-064** - Synthetic training images from generative models improve downstream benchmarks mainly when the test set shares the generator's stylistic biases, and gains evaporate on independently sourced test data.

### human-baselines-annotation (8)

- **W13-P1-C-065** - Human-level performance claims in vision rest on weak human baselines, and expert or incentive-aligned human evaluation reopens the human-machine gap on several solved tasks.
- **W13-P1-C-066** - Models beating human accuracy on benchmarks are often just out-predicting annotator disagreement: agreement-ceiling analysis reframes superhuman claims as majority-vote overfitting.
- **W13-P1-C-067** - Ground truth is instruction-dependent: re-annotating the same images under different but equally reasonable instructions shifts model rankings, exposing benchmark truth as one convention among several.
- **W13-P1-C-068** - Evaluating against annotator label distributions instead of hard labels reranks vision foundation models, revealing that some models are better at truth and others at convention.
- **W13-P1-C-069** - Model-assisted annotation has quietly contaminated ground truth: benchmarks labeled with model-in-the-loop pipelines are biased toward the model families used, inflating those families' measured performance.
- **W13-P1-C-070** - Quality-control gold questions bias test sets toward the unambiguous, so benchmarks systematically exclude the hard cases and overstate deployable accuracy.
- **W13-P1-C-071** - Vision-language models used as judges of visual outputs exhibit self-preference and family-preference biases large enough to corrupt model comparisons that rely on them.
- **W13-P1-C-072** - Annotation-vendor ecosystems create test-set leakage paths that deduplication cannot see: the same worker pools and internal guideline documents touch both training-data production and benchmark creation.

### statistics-reproducibility (8)

- **W13-P1-C-073** - A field-wide bootstrap audit of vision benchmark deltas: a large fraction of published improvements are within test-set resampling noise once paired item-level uncertainty is computed.
- **W13-P1-C-074** - Leaderboards inflate apparent state-of-the-art through selection: the expected maximum over many noisy submissions exceeds true best performance, and the bias is quantifiable from submission statistics.
- **W13-P1-C-075** - The vision benchmark ecosystem has low effective dimensionality: most benchmarks rank models nearly identically, so new benchmarks add publication events but little measurement information.
- **W13-P1-C-076** - Aggregate benchmark rankings conceal reproducible task-specific reversals, and per-deployment model selection based on the aggregate is measurably worse than stratified selection.
- **W13-P1-C-077** - The same checkpoint scores materially differently across popular evaluation harnesses, and harness variance is an unbudgeted error term in every cross-paper comparison.
- **W13-P1-C-078** - Benchmark test sets are underpowered for the effect sizes the field now studies: a power-analysis audit showing that current test sizes cannot resolve current frontier gaps.
- **W13-P1-C-079** - Silent test-informed model selection is endemic: development practices leak test-set signal into checkpoint choice, and a leakage-audit protocol can measure the resulting inflation.
- **W13-P1-C-080** - Published ablation tables systematically overstate component importance because ablations are run once, at one scale, on one seed: a variance-aware re-ablation study.

### robustness-shift-critique (8)

- **W13-P1-C-081** - Effective-robustness analysis via linear fits on accuracy scatter plots breaks down near the accuracy ceiling, and conclusions about which interventions confer robustness flip under ceiling-aware models.
- **W13-P1-C-082** - Distribution-shift benchmarks conflate multiple shift types into single scores, and factorizing shifts reveals that models robust on the benchmark are robust to only some factors deployments care about.
- **W13-P1-C-083** - Fixed-epsilon adversarial evaluation is incomparable across models with different preprocessing and native resolutions, making cross-model robustness tables silently inconsistent.
- **W13-P1-C-084** - Corruption-robustness gains from augmentation research are substantially overfitting to the benchmark's corruption menu, and generalization to held-out corruption families is much weaker than reported averages suggest.
- **W13-P1-C-085** - Vision models certified robust by standard suites fail on temporal shift: robustness leaderboard leaders lose their advantage on data collected years after their training cutoffs.
- **W13-P1-C-086** - Spurious-correlation benchmarks contain their own meta-spurious cues: models can score well on debiasing tests by exploiting artifacts of how the tests were constructed.
- **W13-P1-C-087** - Out-of-distribution generalization scores confound representation robustness with classifier-head robustness, and separating the two shows most model differences live in the head.
- **W13-P1-C-088** - Certified-robustness guarantees do not predict empirical security under realistic attacks: certification radius and practical attack success are weakly related across defended models.

### vlm-eval-weaknesses (10)

- **W13-P1-C-089** - Object-hallucination benchmarks for captioning models measure language co-occurrence priors more than visual grounding, and a blind-model control quantifies exactly how much.
- **W13-P1-C-090** - Visual-grounding scores of multimodal models collapse under image-swap consistency tests: models answer identically when the image is replaced, exposing text-shortcut reliance the benchmarks never check.
- **W13-P1-C-091** - Referring-expression benchmarks are substantially solvable by object-size and position priors without reading the expression, deflating claimed spatial-language grounding.
- **W13-P1-C-092** - Reported multimodal reasoning gains on text-rich benchmarks are mostly optical-character-recognition gains in disguise, separable by transcribed-input ablations.
- **W13-P1-C-093** - Chart and diagram question-answering benchmarks are contaminated by template reuse: finite generator templates make test items predictable from training exposure, inflating scores.
- **W13-P1-C-094** - Multi-image reasoning benchmarks are largely answerable from a single image, and single-image ablations expose that the multi-image capability being marketed is untested by them.
- **W13-P1-C-095** - Video-understanding benchmarks remain largely solvable from one or a few frames even for the newest foundation models, so temporal-understanding claims are still uncertified.
- **W13-P1-C-096** - Counting benchmarks are gamed by dataset count priors: models predict the modal count for an object category rather than counting, and prior-decorrelated items collapse performance.
- **W13-P1-C-097** - Safety evaluations of multimodal models measure refusal-style pattern matching rather than harm-relevant capability, and style-normalized re-evaluation reorders safety leaderboards.
- **W13-P1-C-098** - Instruction-following evaluations for multimodal models conflate formatting compliance with visual understanding: parsing-tolerant re-grading changes model rankings.

### ignored-assumptions (6)

- **W13-P1-C-099** - Temporal collection order inside benchmarks violates the iid assumption invisibly: items collected later differ systematically, and train-test splits inherit hidden temporal structure.
- **W13-P1-C-100** - Benchmark category weighting reflects collection accidents rather than deployment frequency, and usage-weighted evaluation changes which vision models look best.
- **W13-P1-C-101** - The single-ground-truth assumption fails on a measurable fraction of benchmark images, and ambiguity-aware evaluation that accepts answer sets changes both scores and rankings.
- **W13-P1-C-102** - The assumption that higher pretraining data quality uniformly improves downstream performance is wrong: quality filtering helps some downstream tasks while measurably hurting others, and the trade-off is hidden by suite averages.
- **W13-P1-C-103** - English-centric class names and prompts are an ignored evaluation assumption: multilingual re-evaluation of zero-shot vision models changes rankings and reveals language-dependent capability profiles.
- **W13-P1-C-104** - Static test sets cannot detect interaction brittleness: adaptive human-in-the-loop evaluation finds failure modes in vision foundation models that static benchmarks structurally miss, at measurable rates.

## Notes for Wave B (dedup)

- Ideas within a cluster intentionally probe adjacent angles (e.g. several calibration-estimator critiques); dedup should merge where the falsification experiment is effectively identical.
- Several ideas are cross-cutting audits (harness variance, preprocessing sensitivity, seed variance) that may overlap with shards from other generators; check against other generator territories.
- Full structured fields (problem, core_hypothesis, falsifiable_prediction, why_important, why_possibly_novel, minimal_falsification_experiment, main_risk, community_default_belief, why_it_might_be_wrong, fastest_falsification_experiment) are in `ideas_shard.jsonl`.
