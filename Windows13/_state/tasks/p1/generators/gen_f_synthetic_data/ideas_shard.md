# P1 Wave A - Generator F Shard: Synthetic Data (Windows13)

- **task_id**: `p1_gen_f_synthetic_data`
- **role**: generator (candidate ideas only; NO verified-novelty claims)
- **windows_id**: Windows13 (locked; canonical state untouched)
- **territory**: Synthetic data - generation for dense tasks, sim-to-real, label noise, data-centric curation, foundation-model training on synthetic vs real, ignored assumptions
- **idea_count**: 102 (id_seed range `W13-P1-F-001` .. `W13-P1-F-102`)
- **evidence policy**: every record labels its claims with [KNOWN FACT] / [HYPOTHESIS] / [EXPECTED RESULT] / [MODEL SPECULATION]. No fabricated papers, numbers, datasets, or experimental results. All predictions are EXPECTED, none were run.
- **novelty status**: `why_possibly_novel` fields are UNVERIFIED model speculation; Wave B dedup + novelty verification must treat all of them as unchecked.

## Cluster overview

| cluster | count | ids |
|---|---|---|
| dense-task-generation | 14 | 001-014 |
| sim-to-real | 12 | 015-026 |
| label-noise | 12 | 027-038 |
| data-centric-curation | 12 | 039-050 |
| synthetic-vs-real-pretraining | 12 | 051-062 |
| generative-data-engines | 10 | 063-072 |
| procedural-and-graphics | 8 | 073-080 |
| evaluation-of-synthetic-data | 8 | 081-088 |
| ignored-assumptions | 8 | 089-096 |
| scaling-and-economics | 6 | 097-102 |

## Candidate ideas (one-liners)

### dense-task-generation (14)

- **W13-P1-F-001** - Synthetic-data gains in semantic segmentation concentrate on boundary and thin-structure pixels, so pixel-perfect labels rather than scene realism are the active ingredient.
- **W13-P1-F-002** - Mixing pixel-perfect synthetic labels with convention-noisy human labels creates conflicting supervision that caps segmentation performance, and harmonizing label conventions recovers the loss.
- **W13-P1-F-003** - Optical flow transfer from synthetic training data is governed by motion statistics rather than photorealism, so matching real motion distributions with crude rendering beats photorealistic data with mismatched motion.
- **W13-P1-F-004** - Metric depth transfer from synthetic data fails primarily because of scene-scale and layout distribution mismatch, not appearance gap, and layout matching closes more of the gap than image translation.
- **W13-P1-F-005** - For object detection, cut-and-paste composition with mediocre blending matches full 3D rendering pipelines once a low realism threshold is passed, making blending quality an over-optimized axis.
- **W13-P1-F-006** - Generative model internals can supply dense correspondence and grouping pseudo-labels for real images, and a student distilled from them can beat students trained on graphics-rendered ground truth.
- **W13-P1-F-007** - The value of synthetic data per task is predicted by the cost of acquiring real labels for that task, not by the size of the domain gap, revealing label scarcity rather than realism as the binding constraint.
- **W13-P1-F-008** - Synthetic scene generators systematically under-produce heavy-occlusion configurations, and matching real occlusion statistics yields more detection and segmentation transfer than improving textures.
- **W13-P1-F-009** - For human pose estimation, sampling synthetic poses approximately uniformly over kinematically valid space transfers better than sampling from realistic motion-capture distributions.
- **W13-P1-F-010** - Synthetic stuff classes transfer nearly for free while thing classes carry most of the sim-to-real gap, motivating hybrid pipelines that render backgrounds and paste real object instances.
- **W13-P1-F-011** - A measurable share of the sim-to-real segmentation gap is ontology mismatch between asset-derived synthetic classes and visually defined real classes, fixable by remapping rather than rendering.
- **W13-P1-F-012** - Synthetic video with perfectly coherent frames teaches temporal over-smoothness, so video models trained on it degrade on real footage with cuts, jitter, and exposure changes.
- **W13-P1-F-013** - For depth-sensor tasks, faithful sensor-noise simulation matters more than scene realism, and a cheap noise-model calibration step beats expensive content upgrades.
- **W13-P1-F-014** - Reconstructing real scenes into neural 3D representations and re-rendering them with perturbed cameras yields dense supervision with real appearance, and this real2sim2real data beats graphics rendering for dense tasks.

### sim-to-real (12)

- **W13-P1-F-015** - Domain randomization mostly re-implements strong 2D augmentation, and equally aggressive augmentation of a small real set matches heavy randomization in simulation for many perception tasks.
- **W13-P1-F-016** - Reported sim-to-real gaps are inflated by label-convention mismatch, and convention-harmonized re-evaluation shrinks the gap across published setups.
- **W13-P1-F-017** - Foundation-model backbones have made photorealism largely obsolete for sim-to-real: with frozen pretrained features, low-fidelity rendering transfers as well as high-fidelity rendering.
- **W13-P1-F-018** - The direction and size of the sim-real transfer asymmetry (sim-to-real versus real-to-sim) is a cheap diagnostic that identifies whether a gap is appearance-driven or content-driven.
- **W13-P1-F-019** - Models exploit renderer-specific spectral and noise signatures as shortcuts, and matching low-level image statistics between synthetic and real data removes a large, cheap-to-fix share of the sim-to-real gap.
- **W13-P1-F-020** - Sim-to-real adaptation method rankings established on driving benchmarks do not transfer to other target domains, making the canonical leaderboard a domain artifact.
- **W13-P1-F-021** - Adapting label-space statistics (class frequencies, object size and count distributions) via resampling beats image-space adaptation for sim-to-real transfer at a fraction of the cost.
- **W13-P1-F-022** - For contact-rich robotic perception, physics fidelity dominates visual fidelity in sim-to-real transfer, inverting the effort allocation of typical simulation pipelines.
- **W13-P1-F-023** - A large share of the sim-to-real gap lives in normalization statistics, and recalibrating them with a handful of unlabeled real images recovers it without touching any weights.
- **W13-P1-F-024** - Generative image translation of synthetic frames corrupts dense labels by hallucinating and deleting content, so translation-based sim-to-real gains are overstated for dense tasks and label-corruption audits should be mandatory.
- **W13-P1-F-025** - The sim-to-real gap follows its own scaling law with synthetic dataset size, and the exponent difference against real-data scaling predicts crossover budgets where adding synthetic stops helping.
- **W13-P1-F-026** - Weather and lighting randomization in driving simulation covers a thin manifold of real conditions, and a nearest-neighbor coverage audit predicts per-condition transfer failure before any training.

### label-noise (12)

- **W13-P1-F-027** - Pixel-perfect synthetic labels can transfer worse than convention-matched noisy labels because evaluation rewards agreement with human annotator behavior, not with geometric truth.
- **W13-P1-F-028** - Foundation-model pseudo-labels carry attribute-correlated structured noise, so noise-robust learning methods validated on uniform synthetic noise fail on the auto-label noise that actually matters now.
- **W13-P1-F-029** - Synthetic recaptioning of image-text data injects the captioner's systematic biases, and students trained on recaptioned corpora inherit a measurable error fingerprint from the captioning model.
- **W13-P1-F-030** - Boundary-localized label noise damages segmentation training far more per pixel than interior noise, and a boundary-weighted noise metric predicts downstream harm where raw noise rate fails.
- **W13-P1-F-031** - Auto-label noise correlates with example difficulty, so confidence-based label cleaning preferentially deletes hard examples and produces models that score better on clean averages but worse on hard tails.
- **W13-P1-F-032** - The learning-with-noisy-labels leaderboard is a simulation artifact: method rankings under injected noise do not survive on datasets whose noise arose organically from real annotation processes.
- **W13-P1-F-033** - Ensembling multiple foundation-model teachers barely reduces auto-label noise because their errors are correlated through shared pretraining data, violating the independence assumption behind ensemble labeling.
- **W13-P1-F-034** - Beyond a threshold noise level, a small verified-clean validation set is worth more per annotation dollar than any quantity of additional noisy training labels, and the exchange rate is measurable.
- **W13-P1-F-035** - Confidence-based label cleaning entrenches the teacher's biases in the student: samples where the teacher is confidently wrong survive cleaning, creating a measurable self-confirmation loop.
- **W13-P1-F-036** - The soft-versus-hard pseudo-label debate reduces to teacher calibration: soft labels win with calibrated teachers and lose with miscalibrated ones, and a calibration measurement predicts the winner per setup.
- **W13-P1-F-037** - Most of what is booked as label noise in dense annotation is actually irreducible instruction ambiguity, and synthetic data with a single rendering convention trains models to be confidently wrong about genuinely ambiguous pixels.
- **W13-P1-F-038** - Missing-annotation noise (unlabeled true objects treated as background) dominates wrong-label noise in detection training, and exhaustively labeled synthetic data makes the resulting precision-recall distortion worse, not better.

### data-centric-curation (12)

- **W13-P1-F-039** - Most reported gains from sophisticated data-pruning scores on synthetic pools are semantic deduplication in disguise, and after dedup the residual value of pruning scores is marginal.
- **W13-P1-F-040** - Synthetic-data quality filters are task-anticorrelated: filters tuned for classification-style aesthetics remove exactly the cluttered, occluded, hard scenes that dense tasks need most.
- **W13-P1-F-041** - The training value of a synthetic sample is predictable at generation time from generator-internal signals, enabling curation before rendering and saving most of the generation compute that post-hoc filtering wastes.
- **W13-P1-F-042** - Embedding-coverage diversity metrics saturate long before task utility does, and compositional attribute diversity keeps paying after coverage metrics flatline, exposing a blind spot in curation dashboards.
- **W13-P1-F-043** - For low-resource target domains, curating real web data to match a synthetic reference distribution beats curating synthetic data to match limited real samples, reversing the standard curation direction.
- **W13-P1-F-044** - Difficulty-based hard-example mining on synthetic pools preferentially selects generator failure artifacts rather than genuinely hard content, actively injecting shortcut features into training.
- **W13-P1-F-045** - Data-pruning conclusions invert with scale on synthetic pools: pruning helps at small training budgets and hurts at large ones, with a predictable crossover that current papers ignore by evaluating at single scales.
- **W13-P1-F-046** - The optimal real-to-synthetic mixing ratio is predictable from gradient alignment between real and synthetic mini-batches measured early in training, eliminating expensive mixing-ratio sweeps.
- **W13-P1-F-047** - Cross-boundary deduplication between synthetic pools and real train and test sets is a missing pipeline stage: synthetic near-duplicates of test data inflate benchmarks and near-duplicates of train data add nothing.
- **W13-P1-F-048** - Source-level scheduling (synthetic-then-real annealing) dominates example-level curriculum within synthetic data, so curation effort spent ordering synthetic examples is largely wasted.
- **W13-P1-F-049** - Influence-style valuation against a real validation set reveals that most of a typical synthetic pool has near-zero or negative training value, with the positive value concentrated in a small identifiable slice.
- **W13-P1-F-050** - Generative synthetic-data utility scales with distinct-prompt count, not image count: images-per-prompt beyond a small number is nearly wasted compute, making prompt engineering the real dataset-size lever.

### synthetic-vs-real-pretraining (12)

- **W13-P1-F-051** - Procedural and abstract-image pretraining works by installing generic early-layer filters, so its benefit saturates at small scale and vanishes for foundation-scale models with long real-data training.
- **W13-P1-F-052** - Training students on generator-produced data is distillation, not discovery: it accelerates learning toward the generator's knowledge but cannot exceed it, and the ceiling is measurable.
- **W13-P1-F-053** - Model-collapse fears are overstated for the practical vision regime: accumulating synthetic data alongside a fixed real anchor avoids degradation that only replacement-style training exhibits.
- **W13-P1-F-054** - Synthetic data helps foundation models where real data is thin: a density-targeted synthesis policy that generates in low-density regions of the real distribution beats uniform synthesis at equal budget.
- **W13-P1-F-055** - Synthetic captions improve benchmark retrieval scores while quietly degrading robustness under distribution shift because they homogenize the text distribution that contrastive training consumes.
- **W13-P1-F-056** - Rendering-based synthetic pretraining transfers to geometry-loaded tasks and not to semantics-loaded ones, and a task's geometry-semantics loading predicts its synthetic-pretraining benefit.
- **W13-P1-F-057** - The real-data fraction needed to anchor mostly-synthetic pretraining shrinks with model scale, opening a path where foundation models train predominantly on synthetic data with small real anchors.
- **W13-P1-F-058** - Self-supervised objectives differ systematically in synthetic-data tolerance: reconstruction-style objectives degrade less on synthetic pretraining data than contrastive ones, so data provenance should drive objective choice.
- **W13-P1-F-059** - Tagging synthetic samples with a provenance token during pretraining recovers most of the performance lost to synthetic contamination, versus silently mixing, at essentially zero cost.
- **W13-P1-F-060** - Students inherit generator fingerprints from synthetic training data strongly enough that the generator identity is recoverable from student behavior, enabling training-data supply-chain forensics.
- **W13-P1-F-061** - Generating training data with a large generator to train a small task model beats direct real-data training only inside a predictable regime boundary defined by the task's distance from the generator's training distribution.
- **W13-P1-F-062** - Synthetic-pretraining effects survive full fine-tuning for dense tasks but wash out for classification, contradicting the belief that ample fine-tuning erases pretraining data differences uniformly.

### generative-data-engines (10)

- **W13-P1-F-063** - Self-training loops plateau because of diversity collapse in what gets auto-labeled, not noise accumulation, and an entropy audit of accepted pseudo-labels predicts the plateau before it arrives.
- **W13-P1-F-064** - Text-to-image augmentation gains are bounded by the generator's within-class diversity, which is far below real data, and a generator-side recall measurement predicts the augmentation ceiling per class.
- **W13-P1-F-065** - Editing real images beats generating from scratch for augmentation at equal budget because edits preserve real image statistics while still adding controlled variation, especially for dense tasks.
- **W13-P1-F-066** - The best use of generative models for dense tasks is generating labels for real images rather than images for synthetic labels, inverting the standard generation pipeline.
- **W13-P1-F-067** - Published diffusion-augmentation gains shrink dramatically against modern strong-augmentation baselines, surviving mainly in low-data regimes, and a reproduction matrix would recalibrate the field's expectations.
- **W13-P1-F-068** - Students inherit compositional failure modes of their generative teachers: training on diffusion data measurably degrades counting and structural accuracy relative to matched real-data training.
- **W13-P1-F-069** - Web-crawl vintages carry rising synthetic fractions, and models pretrained on different crawl vintages show behavior drift attributable to synthetic contamination, making vintage a measurable data-quality variable.
- **W13-P1-F-070** - Bilevel-optimal data generation (generate to directly maximize student validation improvement) is approximable by first-order gradient matching at a tiny fraction of the cost, capturing most of its gain.
- **W13-P1-F-071** - Deliberately generating realistic near-miss hard negatives improves fine-grained discrimination more than generating additional positives, making negative synthesis the underused half of generative augmentation.
- **W13-P1-F-072** - Generated video is a poor training source for temporal representations because its artifacts are temporal, and hybrid data (generated appearance with real motion) beats end-to-end video generation for training video models.

### procedural-and-graphics (8)

- **W13-P1-F-073** - Transfer from graphics data scales with distinct 3D asset count without saturating, while realism knobs saturate early, so generation budgets should buy assets, not rendering quality.
- **W13-P1-F-074** - A procedurally infinite stream of moderate-quality scenes beats any fixed-size high-quality synthetic dataset for dense tasks, because non-repetition eliminates the synthetic-overfitting failure mode.
- **W13-P1-F-075** - Renderer identity leaves shortcut fingerprints that models exploit, and mixing multiple renderers is a near-free domain-randomization axis stronger than texture randomization.
- **W13-P1-F-076** - Tasks defined only through synthetic supervision, like intrinsic decomposition, may have models that learned renderer conventions rather than physics, and a real-light-transport audit would expose the gap.
- **W13-P1-F-077** - Layout realism (object co-occurrence and physical support relations) transfers more than appearance realism, so scene-grammar investment beats shading investment at equal cost.
- **W13-P1-F-078** - Procedural generation parameters can be optimized directly against downstream validation performance with black-box methods, because the loss over generation parameters is smoother than assumed.
- **W13-P1-F-079** - Camera and ISP simulation parameters matter more for geometric-task transfer than scene content, and calibrating the virtual camera to the target device closes more depth-estimation gap than content matching.
- **W13-P1-F-080** - Rendered-human training data shows an uncanny-valley non-monotonicity: mid-realism renders transfer worse than either stylized or high-realism renders for person-centric tasks.

### evaluation-of-synthetic-data (8)

- **W13-P1-F-081** - Generator quality metrics like distribution-distance scores are nearly uncorrelated with the training utility of generated data, and the field needs utility-specific metrics rather than borrowed perceptual ones.
- **W13-P1-F-082** - Train-on-synthetic-test-on-real rankings of synthetic datasets flip across student architectures, so dataset-superiority claims made with one architecture are architecture-conditional statements in disguise.
- **W13-P1-F-083** - A cheap probe suite over frozen foundation features can predict the full-training utility of a synthetic dataset, replacing most train-to-evaluate cycles in curation loops.
- **W13-P1-F-084** - Synthetic test sets systematically compress model rankings because generators regress toward typical instances, making synthetic evaluation optimistically biased and rank-unstable for model comparison.
- **W13-P1-F-085** - Synthetic data quality is two independent axes, fidelity and coverage, that trade off differently per task, and single-scalar quality reporting systematically misleads adoption decisions.
- **W13-P1-F-086** - Generators have seen the benchmarks: synthetic training data leaks evaluation content through generator memorization, inflating synthetic-data results in ways standard contamination checks never audit.
- **W13-P1-F-087** - Reported synthetic-data gains are confounded by asymmetric tuning effort, and equal-tuning-budget re-evaluation would deflate a measurable share of published improvements.
- **W13-P1-F-088** - Per-image accounting hides the cost of synthetic data: under per-FLOP accounting that includes generation compute, many synthetic-data results are net-negative versus simply training longer on real data.

### ignored-assumptions (8)

- **W13-P1-F-089** - Batch-generated synthetic data violates the i.i.d. assumption through shared seeds, prompts, and scheduler state, and decorrelating generation batches yields free training gains.
- **W13-P1-F-090** - Renderer labels are not ground truth for the evaluation convention: anti-aliased boundaries, transparency, and reflections are labeled by renderer logic that systematically disagrees with human annotation guidelines.
- **W13-P1-F-091** - More realism is not monotonically better: past a threshold, realistic synthesis re-imports the real world's spurious correlations that cruder randomized data had removed, hurting robustness.
- **W13-P1-F-092** - Synthetic data optimized to match today's distribution is optimized for the wrong target when deployment shifts the distribution, and shift-anticipating synthesis beats distribution-matching synthesis.
- **W13-P1-F-093** - Synthetic data is assumed privacy-safe by construction, but generator memorization leaks training individuals, and the utility cost of verified non-memorization is unknown and possibly severe.
- **W13-P1-F-094** - The domain gap is treated as a scalar when it is a decomposable vector over appearance, content, sensor, and label-convention factors, and interventions are systematically misattributed as a result.
- **W13-P1-F-095** - Generation vintage is a hidden curriculum: synthetic corpora accumulate quality drift as pipelines improve, and ordering training by vintage versus shuffling changes outcomes, an unexamined degree of freedom.
- **W13-P1-F-096** - The student-cannot-exceed-teacher assumption fails for dense geometry: averaging noisy generator-derived labels across many views or samples lets students surpass their labeling teacher measurably.

### scaling-and-economics (6)

- **W13-P1-F-097** - Real and synthetic data follow different scaling exponents that interact, and a two-term joint scaling law fitted from pilot runs predicts the optimal real-synthetic mix at any budget.
- **W13-P1-F-098** - Synthetic-data returns plateau when the student saturates the generator's effective support, and the intrinsic dimension of the generated set predicts the plateau point before training reaches it.
- **W13-P1-F-099** - The true unit cost of synthetic data is dominated by curation, validation, and integration rather than generation, and total-cost accounting reverses several published cost-benefit claims.
- **W13-P1-F-100** - Small domain-specialized generators beat giant general generators as training-data engines at equal generation compute, contradicting the bigger-generator-is-better default.
- **W13-P1-F-101** - When real data is exhausted, repeating real epochs beats adding synthetic data up to a predictable repetition count, and the repetition-versus-synthesis crossover is a fittable law.
- **W13-P1-F-102** - Synthetic datasets depreciate faster than real datasets as deployment distributions and conventions drift, and measuring dataset half-life reveals different amortization economics for the two data types.
