# P1 Wave A - Generator G Shard: Domain Shift (Windows13)

- **task_id**: `p1_gen_g_domain_shift`
- **role**: generator (candidate ideas only; NO verified-novelty claims)
- **windows_id**: Windows13 (locked; canonical state untouched)
- **territory**: Domain shift - unsupervised/test-time adaptation, domain generalization, distribution-shift robustness, ignored i.i.d. assumptions in vision foundation models
- **idea_count**: 100 (id_seed range `W13-P1-G-001` .. `W13-P1-G-100`)
- **evidence policy**: every record labels its claims with [KNOWN FACT] / [HYPOTHESIS] / [EXPECTED RESULT] / [MODEL SPECULATION]. No fabricated papers, numbers, datasets, or experimental results. All predictions are EXPECTED, none were run.
- **novelty status**: `why_possibly_novel` fields are UNVERIFIED model speculation; Wave B dedup + novelty verification must treat all of them as unchecked.

## Cluster overview

| cluster | count | ids |
|---|---|---|
| test-time-adaptation | 14 | 001-014 |
| unsupervised-domain-adaptation | 10 | 015-024 |
| domain-generalization | 12 | 025-036 |
| shift-detection-monitoring | 10 | 037-046 |
| iid-assumption-violations | 10 | 047-056 |
| fm-robustness-scaling | 12 | 057-068 |
| shift-benchmark-critique | 10 | 069-078 |
| continual-online-shift | 8 | 079-086 |
| shift-theory-measurement | 8 | 087-094 |
| vlm-multimodal-shift | 6 | 095-100 |

## Candidate ideas (one-liners)

### test-time-adaptation (14)

- **W13-P1-G-001** - Entropy-minimization test-time adaptation gains are specialized to synthetic corruption-style shifts and vanish or reverse on natural distribution shifts.
- **W13-P1-G-002** - Most published test-time adaptation gains are batch-statistics artifacts that disappear at batch size one, the realistic streaming regime.
- **W13-P1-G-003** - Test-time adaptation hyperparameters are implicitly tuned on the test distribution, making reported gains circular; shift-blind hyperparameter selection erases most of them.
- **W13-P1-G-004** - Core test-time adaptation conclusions were formed on batch-normalized convolutional networks and do not transfer to layer-normalized transformer foundation models.
- **W13-P1-G-005** - Under long unlabeled streams, most self-supervised test-time adaptation methods eventually collapse to trivial predictions, and collapse frequency is a hidden but decisive metric.
- **W13-P1-G-006** - A frozen foundation model with a test-time nearest-neighbor or retrieval-augmented classifier matches gradient-based test-time adaptation at far lower risk.
- **W13-P1-G-007** - Most of what test-time adaptation improves is calibration and decision thresholds, not representation quality, and a post-hoc output correction recovers the bulk of its accuracy gain.
- **W13-P1-G-008** - Test-time adaptation methods are doing implicit label-shift estimation, and explicit unlabeled class-prior correction matches them whenever the shift includes a prior change.
- **W13-P1-G-009** - Single-sample adaptation methods built on augmentation consistency mostly repackage test-time augmentation ensembling, and the learning component adds little.
- **W13-P1-G-010** - No current test-time adaptation method knows when not to adapt; a simple do-no-harm gate based on stream statistics prevents most catastrophic adaptation failures.
- **W13-P1-G-011** - Periodic hard reset to source weights beats sophisticated anti-forgetting machinery in continual test-time adaptation over long horizons.
- **W13-P1-G-012** - Episodic reset-per-shift evaluation protocols overstate test-time adaptation practicality, and realistic recurring mixed-shift streams reverse published method rankings.
- **W13-P1-G-013** - Test-time prompt tuning gains for vision-language models are mostly attributable to augmentation ensembling and confident-view selection rather than to learned prompt updates.
- **W13-P1-G-014** - Matching test images to the pretraining input-statistics envelope, a trivial input-space normalization, is a stronger and safer baseline than most parameter-updating test-time adaptation.

### unsupervised-domain-adaptation (10)

- **W13-P1-G-015** - Classical unsupervised domain adaptation methods built for weak backbones add approximately nothing on top of modern foundation-model features.
- **W13-P1-G-016** - Marginal feature-alignment objectives actively hurt adaptation when source and target label distributions differ, and popular benchmarks hide this by having nearly matched label marginals.
- **W13-P1-G-017** - Given a foundation-model backbone, plain confidence-thresholded self-training beats every sophisticated alignment-based adaptation method across the standard benchmark suite.
- **W13-P1-G-018** - Zero-shot vision-language models have effectively saturated office-style adaptation benchmarks, making continued method development on them uninformative.
- **W13-P1-G-019** - Unsupervised model selection, not adaptation method choice, is the dominant source of variance in domain adaptation outcomes, and reported method gains are smaller than selection-induced spread.
- **W13-P1-G-020** - Source data hurts more than it helps once a strong foundation initialization exists: source-free adaptation matches or beats joint source-plus-target training.
- **W13-P1-G-021** - A cheap a-priori adaptability score computed from foundation-model feature geometry predicts whether unsupervised adaptation will help, do nothing, or hurt on a given domain pair.
- **W13-P1-G-022** - Domain invariance is the wrong objective: methods that succeed do so through implicit class-conditional alignment, and enforcing pure marginal invariance strictly removes target-discriminative information.
- **W13-P1-G-023** - In dense-prediction domain adaptation, a large share of reported gains comes from resolution, crop, and class-frequency handling rather than from distribution-alignment machinery.
- **W13-P1-G-024** - Adaptation methods developed on synthetic-to-real style gaps systematically fail on real-to-real shifts such as geography and time, because the two gap types have different structure.

### domain-generalization (12)

- **W13-P1-G-025** - With foundation-model backbones, the gap between domain-generalization algorithms and empirical risk minimization shrinks to zero, making algorithm-centric generalization research empirically unmotivated in the current regime.
- **W13-P1-G-026** - Domain-generalization benchmarks primarily rank pretrained backbones rather than generalization algorithms, and published algorithm rankings are noise around a backbone-determined score.
- **W13-P1-G-027** - Invariance-penalty methods fail on vision benchmarks because the annotated environments are not causally meaningful, and with environments constructed from capture metadata the same methods start working.
- **W13-P1-G-028** - Weight-averaging and flat-minima methods improve domain-generalization scores through generic variance reduction that helps in-distribution equally, not through any shift-specific mechanism.
- **W13-P1-G-029** - A leakage audit of the domain-generalization literature: quantifying how much of reported progress evaporates under strictly source-only model selection.
- **W13-P1-G-030** - Pretraining data diversity, not model scale, is the dominant controllable factor for out-of-domain generalization at fixed compute.
- **W13-P1-G-031** - Gains from style-based augmentation on stylized benchmarks anti-correlate with performance on real geographic and temporal shifts, revealing style benchmarks as a misleading target.
- **W13-P1-G-032** - Per unit of in-distribution accuracy, frozen-feature linear probes generalize across domains better than end-to-end fine-tuned models, and the gap widens with shift severity.
- **W13-P1-G-033** - Compositional shift, where familiar attributes and objects appear in novel combinations, is a distinct failure axis of vision foundation models that standard domain-generalization metrics never measure.
- **W13-P1-G-034** - Leave-one-domain-out evaluation has such high variance across the choice of held-out domain that most published domain-generalization comparisons are statistically undecidable.
- **W13-P1-G-035** - Textual descriptions of a target domain, used to steer a vision-language model, recover a large fraction of the benefit that unsupervised adaptation obtains from actual target images.
- **W13-P1-G-036** - Latent domain discovery from foundation-model features produces better environment partitions for invariance-based training than human-annotated domain labels.

### shift-detection-monitoring (10)

- **W13-P1-G-037** - Frozen foundation-model embeddings with classical two-sample tests detect deployment distribution shift better than dedicated learned shift detectors.
- **W13-P1-G-038** - Most distribution shifts flagged by monitoring systems do not harm accuracy, and harm-calibrated detection, not shift detection, is the correct monitoring objective.
- **W13-P1-G-039** - Unlabeled accuracy-estimation methods fail precisely on the shift types where monitoring needs them most, and a failure taxonomy predicts when their estimates can be trusted.
- **W13-P1-G-040** - The accuracy-on-the-line phenomenon is a property of shared pretraining lineages, and it breaks for adapted, fine-tuned, or intervention-modified models, undermining its use for monitoring.
- **W13-P1-G-041** - Embedding-space shift detection is dominated by low-level image statistics, masking semantic shifts; band-separated tests are needed to see what actually changed.
- **W13-P1-G-042** - Anytime-valid sequential tests on foundation-model embeddings give deployment shift alarms with controlled false-alarm rates, which matters more in practice than the detection-power race.
- **W13-P1-G-043** - Predicting per-sample correctness under shift is more tractable than predicting aggregate accuracy, and selective prediction transfers across shifts better than accuracy estimation does.
- **W13-P1-G-044** - Rankings from out-of-distribution detection benchmarks do not predict which methods detect harmful natural shift in deployment-like monitoring, revealing a benchmark-objective mismatch.
- **W13-P1-G-045** - Label-shift estimators silently return confident nonsense when class-conditional distributions also shift, and a cheap self-diagnostic can flag when their assumption is violated.
- **W13-P1-G-046** - Drift root-cause attribution, assigning a detected shift to interpretable factors via counterfactual reweighting in foundation-feature space, is more valuable and more tractable than drift detection itself.

### iid-assumption-violations (10)

- **W13-P1-G-047** - Hidden batch effects inside single-domain vision test sets shrink effective sample size so much that standard error bars in evaluation papers are systematically overconfident.
- **W13-P1-G-048** - Data augmentation is an unacknowledged train-time distribution shift, and its interaction with test-time shift explains part of why augmentation-trained models respond unpredictably to deployment drift.
- **W13-P1-G-049** - Dataset curation filters make benchmark test sets systematically easier than deployment data, and the curation-induced optimism is quantifiable by reconstructing the rejected data.
- **W13-P1-G-050** - Deployed vision models reshape the future data they receive, and this feedback loop breaks i.i.d. evaluation in a way measurable only through simulation-based protocols.
- **W13-P1-G-051** - Shuffling time-stamped datasets hides temporal drift; time-respecting splits materially change both absolute accuracy and model rankings on the same data.
- **W13-P1-G-052** - Near-duplicate structure in web-scale pretraining data inflates measured robustness because shifted test sets contain look-alikes of pretraining images.
- **W13-P1-G-053** - Realistic dependence structure in deployment streams breaks conformal prediction coverage for vision models, and the realized coverage gap is large enough to matter operationally.
- **W13-P1-G-054** - Photographer intent biases class-conditional distributions toward prototypical views, and models inherit a prototype bias that surfaces as viewpoint and context fragility under deployment shift.
- **W13-P1-G-055** - A measurable share of reported distribution-shift degradation is actually annotation-standard shift, where label conventions rather than images changed between source and target.
- **W13-P1-G-056** - Shared-source structure within single datasets violates i.i.d. assumptions enough that cluster-aware resampling changes benchmark conclusions, not just error bars.

### fm-robustness-scaling (12)

- **W13-P1-G-057** - Foundation-model robustness gains on shift benchmarks are largely pretraining-coverage effects, and an explicit coverage audit deflates claimed robustness to genuine novelty.
- **W13-P1-G-058** - A time-travel evaluation using only imagery created after a model's data cutoff provides the first clean measurement of foundation-model robustness to genuine novelty.
- **W13-P1-G-059** - Robustness loss under downstream fine-tuning is a smooth function of parameter movement from the pretrained point, giving a practical dial for the accuracy-robustness tradeoff.
- **W13-P1-G-060** - Out-of-distribution performance saturates with model scale earlier than in-distribution performance, indicating that robustness is data-limited rather than capacity-limited.
- **W13-P1-G-061** - Foundation models are relatively less robust to low-level sensor and compression shifts than smaller supervised models, and their celebrated robustness advantage is semantic-only.
- **W13-P1-G-062** - Measured robustness differences between zero-shot and probed versions of the same backbone show that the classification head, not the representation, drives much of the foundation-model robustness story.
- **W13-P1-G-063** - At matched pretraining data, contrastive, captioning, and self-supervised objectives yield similar distribution-shift robustness, showing that the objective is incidental and data is the whole story.
- **W13-P1-G-064** - Robustness-intervention effects measured on small models predict their effects on foundation-scale models, enabling cheap screening before expensive integration.
- **W13-P1-G-065** - Background and texture shortcut reliance survives foundation-model scale essentially unchanged; scale reduces failure frequency but not the failure mechanism.
- **W13-P1-G-066** - Retrieval and classification robustness of the same vision-language model diverge under identical shifts, so single-task robustness certification is misleading for multi-use foundation models.
- **W13-P1-G-067** - Instruction tuning and preference alignment of vision-language assistants degrade the distribution-shift robustness of their underlying visual competence, an unmeasured robustness tax.
- **W13-P1-G-068** - Averaging weights of independently fine-tuned models recovers more of the robustness lost to fine-tuning than any specialized robust-training objective, at zero inference cost.

### shift-benchmark-critique (10)

- **W13-P1-G-069** - Method rankings from synthetic corruption benchmarks do not transfer to natural distribution shifts, and continued use of corruptions as the primary robustness certification is quantitatively unjustified.
- **W13-P1-G-070** - Benchmark domains are confounded bundles of style, content, and class-balance factors, and factorized shift benchmarks would reattribute much of what the field calls domain gap.
- **W13-P1-G-071** - Popular web-scraped shift test sets are inside foundation-model pretraining distributions, and a decontamination protocol is required before any foundation-model robustness number on them is meaningful.
- **W13-P1-G-072** - As in-distribution accuracy saturates, effective-robustness slopes become statistically unidentifiable, and the field needs harder in-distribution benchmarks merely to keep measuring robustness.
- **W13-P1-G-073** - Static shift benchmarks cannot rank methods for real gradual drift; stream benchmarks with controlled drift dynamics reverse adaptation-method rankings.
- **W13-P1-G-074** - Geographic-shift benchmark degradation conflates image-distribution change with label-taxonomy mismatch across regions, and region-relabeled evaluation would separate the two.
- **W13-P1-G-075** - No robustness method Pareto-dominates across shift types, and shift-type profiles should replace single-number robustness leaderboards.
- **W13-P1-G-076** - Subpopulation-shift benchmarks overstate the availability of group labels, and under realistic group-label-free conditions the reported superiority of group-robust methods over plain training shrinks or vanishes.
- **W13-P1-G-077** - Adversarially-filtered hard test sets measure disagreement with the filter model rather than distribution shift, and robustness conclusions drawn from them are filter-relative artifacts.
- **W13-P1-G-078** - Robustness benchmark numbers are unstable to preprocessing details at magnitudes comparable to published method gains, and a preprocessing-sensitivity audit is a missing requirement.

### continual-online-shift (8)

- **W13-P1-G-079** - Caching and re-using per-condition adapters, a domain memory, beats continual gradient updating under recurring shift conditions and eliminates catastrophic forgetting by construction.
- **W13-P1-G-080** - The optimal adaptation learning rate under gradual drift is a function of measurable drift speed, and an adaptive-rate law derived from it beats every fixed-rate configuration.
- **W13-P1-G-081** - Long-horizon stability of online adaptation is governed by the dimensionality of the updated parameter subspace, and full-parameter online updating diverges with probability approaching one.
- **W13-P1-G-082** - A divergence anchor to the frozen source model replaces stored source data in online adaptation, giving replay-level stability at zero storage and no privacy cost.
- **W13-P1-G-083** - Test-time adaptation methods silently assume covariate shift, and under label-conditional drift they confidently adapt in the wrong direction, making things worse than no adaptation.
- **W13-P1-G-084** - Self-supervised test-time training helps only when the auxiliary task is statistically coupled to the shift, and a computable coupling diagnostic predicts its sign of effect.
- **W13-P1-G-085** - Online adaptation methods are broken by realistic non-uniform arrival processes such as class bursts, and arrival-robustness should be a first-class evaluation axis.
- **W13-P1-G-086** - Under matched compute budgets, simple adaptation baselines beat sophisticated methods, and a compute-normalized leaderboard would invert much of the field's perceived ranking.

### shift-theory-measurement (8)

- **W13-P1-G-087** - Generic distribution-divergence measures do not predict transfer performance drop across domains, while cheap hypothesis-disagreement measures do, and the field keeps reporting the wrong quantity.
- **W13-P1-G-088** - Classical domain-adaptation generalization bounds are numerically vacuous at foundation scale yet ordinally predictive, and quantifying this rescues theory as a ranking tool.
- **W13-P1-G-089** - Most accuracy degradation of foundation models under natural shift is captured by a two-parameter description, class-prior change plus uniform margin erosion, enabling label-free degradation forecasting.
- **W13-P1-G-090** - Shift magnitude should be measured in the model's decision-relevant subspace, not in input or generic feature space, and a decision-aware shift norm predicts harm where existing measures fail.
- **W13-P1-G-091** - Effective-robustness conclusions flip under alternative link functions for the in-distribution-to-shift accuracy relationship, revealing that which models count as robust is partly an artifact of curve-fitting convention.
- **W13-P1-G-092** - Transferability-estimation metrics fail exactly when the probe data is shifted from deployment data, and a shift-aware correction term restores their usefulness for model selection.
- **W13-P1-G-093** - Enforcing invariance to a nuisance factor provably trades away robustness to shifts correlated with that factor, and the tradeoff is measurable and large in controlled vision experiments.
- **W13-P1-G-094** - Importance weighting for covariate shift, long dismissed as hopeless in high dimensions, becomes practical when density ratios are estimated in foundation-model embedding space.

### vlm-multimodal-shift (6)

- **W13-P1-G-095** - Language is an adaptation surface: systematic per-domain prompt construction matches gradient-based adaptation of vision-language models at a tiny fraction of the cost and risk.
- **W13-P1-G-096** - The text tower has its own distribution-shift problem: class-name register, dialect, and terminology shifts degrade vision-language classification as much as image shifts, and no benchmark measures this axis.
- **W13-P1-G-097** - Under image distribution shift, vision-language assistants lean harder on language priors, so their accuracy degrades gracefully while their visual grounding collapses, and accuracy-only evaluation hides the swap.
- **W13-P1-G-098** - The caption-style provenance of pretraining data determines which visual shifts a vision-language model is robust to, giving each model a predictable robustness fingerprint.
- **W13-P1-G-099** - Cross-modal agreement between image and text pathways is a label-free estimator of shift harm specific to vision-language models, outperforming confidence-based estimators.
- **W13-P1-G-100** - Generative vision models used as classifiers have a qualitatively different distribution-shift robustness profile than discriminative foundation models, defining an unexplored complementary paradigm.
