# Generator J shard: diffusion/generative models as scientific subject

- task_id: `p1_gen_j_diffusion_model_science`  |  role: generator  |  wave: P1 Wave A (wave3 queue)
- windows: Windows13 (locked)  |  branch: `cursor/p1-gen-j-diffusion-science-3470`  |  generated_at: 2026-08-28T20:24:11Z
- id_seed range: W13-P1-J-001..W13-P1-J-104  |  idea_count: 104
- novelty: ALL ideas UNVERIFIED (generation only; no literature verification performed in this task).
- evidence labels: inline [KNOWN FACT]/[HYPOTHESIS]/[EXPECTED RESULT]/[MODEL SPECULATION] tags plus structured `evidence_label` dict incl. `prior_work_basis` on every record. No citations are fabricated; prior-work claims are explicitly labeled model recall.

## Anti-crowding self-audit (vs decision.json guards)

- SAM/SAM2 mentions: 0/104 records (0.0%) — cap 5%: PASS
- synthetic-training-data framings: 1/104 (1.0%) — cap 10% (gen_f owns): PASS
- 'generative eval metric is broken' framing (gen_c/F5): 0 records — claims target model/sampler behavior, never metric validity: PASS
- banned scattering-media running examples (gen_b): 0: PASS
- calibration/uncertainty as primary cluster: NOT used; the `diffusion-priors-for-ambiguity` cluster (8 records, 7.7%) studies the generative prior's representation of task ambiguity per the assigned territory, and no record's primary claim is a calibration-metric claim.
- template families F1-F4: no PEFT-factorial, no SAM-component probes, no internal-score-as-free-detector framings (self-consistency/typicality records are characterization laws or model diagnostics with explicit validity-boundary tests, not free-detector claims), no cue-ablation-collapse on organisms.
- structure quota: 12 sub-clusters, largest 10/104 (9.6%) <= 15%: PASS
- genre quota: constructive_capability 37 (35.6%) >= 25%: PASS; audit_debunk 10 (9.6%) <= 40%: PASS; characterization_law 57
- metric independence: 101/104 (97.1%) of falsification experiments do NOT depend on segmentation/mask metrics (>= 30% required): PASS
- numeric kill thresholds: 104/104 falsifiable_predictions carry pre-registered numeric thresholds: PASS
- cost bounds: 103/104 fastest-falsification experiments are public-data single-GPU with stated time bounds; 1 record(s) set needs_special_resources=true (small human study)
- family fingerprints: every record tagged (subject_system, manipulated_variable, measurement_family)

## Cluster map

- `diffusion-representations`: 9 ideas
- `diffusion-for-perception`: 10 ideas
- `guidance-science`: 9 ideas
- `inversion-editing-pathologies`: 9 ideas
- `generator-memorization`: 9 ideas
- `sampling-dynamics`: 9 ideas
- `diffusion-priors-for-ambiguity`: 8 ideas
- `conditioning-binding`: 8 ideas
- `distillation-fewstep-science`: 8 ideas
- `latent-space-vae-effects`: 8 ideas
- `noise-schedule-frequency`: 8 ideas
- `video-temporal-diffusion`: 9 ideas

---


## diffusion-representations (9 ideas)

### W13-P1-J-001 [characterization_law]
**The semantically strongest layer/timestep for diffusion-feature extraction is set by signal-to-noise ratio, not raw timestep index, and therefore transfers across models and noise schedules once re-parameterized in SNR.**

- hypothesis: [HYPOTHESIS] Probe accuracy as a function of noise level collapses onto a single curve across models and schedules when indexed by log-SNR, because the denoising task difficulty (and hence the abstraction level of features) is determined by SNR alone.
- kill test: [EXPECTED RESULT] The log-SNR location of peak linear-probe accuracy will agree across at least three public diffusion checkpoints with different schedules to within 0.5 nats of log-SNR; kill the idea if the peak locations spread by more than 1.5 nats or if raw-timestep indexing aligns them equally well.
- fastest falsification: Feature extraction plus linear probes on a 10k-image public subset (ImageNet-scale classes) for three checkpoints is roughly one day on a single A100; no training of diffusion models required.
- fingerprint: image diffusion denoiser features | noise level indexing (SNR vs timestep) across checkpoints | linear-probe accuracy curves

### W13-P1-J-002 [characterization_law]
**Dense correspondence ability in diffusion features lives in self-attention key/query geometry, not in convolutional value pathways, and the two can be dissociated by targeted feature surgery.**

- hypothesis: [HYPOTHESIS] Correspondence accuracy is carried by the key/query token geometry of self-attention layers, while value/conv pathways mainly carry appearance; matching on key/query subspaces alone preserves correspondence while matching on value subspaces alone collapses it.
- kill test: [EXPECTED RESULT] Key/query-only matching will retain at least 85% of full-feature correspondence accuracy (PCK) while value-only matching retains under 50%; kill the idea if the two subspaces are within 10 PCK points of each other.
- fastest falsification: Correspondence evaluation over ~1k image pairs with four feature variants runs in a few hours on one GPU using public checkpoints and public benchmarks.
- fingerprint: text-to-image diffusion self-attention | feature subspace used for matching (key/query vs value/conv) | correspondence PCK

### W13-P1-J-003 [characterization_law]
**v-prediction and x0-prediction models yield markedly better high-noise semantic features than epsilon-prediction models of matched quality, because their outputs remain image-like where epsilon targets are nearly pure noise.**

- hypothesis: [HYPOTHESIS] At low SNR the learning signal for epsilon-parameterized networks is dominated by noise regression, so their internal features degrade faster with noise level than v- or x0-parameterized networks trained on the same data.
- kill test: [EXPECTED RESULT] At log-SNR below -2, linear-probe accuracy of v-parameterized features will exceed epsilon-parameterized features by at least 5 accuracy points on a fixed probe suite with matched architectures and data; kill if the gap is under 2 points or reverses.
- fastest falsification: Two or three CIFAR-scale diffusion trainings (about 1 GPU-day each on a single consumer GPU) plus probing; total under 4 GPU-days with public data.
- fingerprint: small from-scratch diffusion models | output parameterization (epsilon/v/x0) | linear-probe accuracy vs SNR

### W13-P1-J-004 [characterization_law]
**Diffusion features encode intrinsic scene properties (albedo, shading, material gloss) more linearly than contrastive or masked-image features, because generation requires photometric competence that discriminative objectives can discard.**

- hypothesis: [HYPOTHESIS] Generative pretraining preserves photometric factors as linearly decodable structure, whereas invariance-based objectives explicitly or implicitly suppress them, producing a measurable objective-dependent gap on intrinsics probes.
- kill test: [EXPECTED RESULT] Linear probes for albedo/shading separation on public intrinsics benchmarks will show diffusion features beating a strong contrastive baseline by at least 15% relative error reduction; kill if the gap is under 5% relative or the ordering flips.
- fastest falsification: Frozen-feature probing on public intrinsics data across three public checkpoints is a single-GPU, roughly one-day experiment.
- fingerprint: pretrained vision backbones incl. diffusion | pretraining objective family | intrinsic-decomposition probe error

### W13-P1-J-005 [audit_debunk]
**Depth structure readable from image-diffusion features reflects genuinely 3D-consistent knowledge rather than 2D shading heuristics, testable by randomizing photometric cues and checking cross-view probe consistency.**

- hypothesis: [HYPOTHESIS] A nontrivial fraction of depth information in diffusion features survives photometric-cue randomization and remains consistent across viewpoints of the same scene, indicating internal 3D structure beyond monocular heuristics.
- kill test: [EXPECTED RESULT] Under stylization/relighting perturbations that destroy shading cues, depth-probe accuracy will retain at least 60% of its clean value, and cross-view depth-probe agreement on multi-view public scenes will exceed a chance-matched baseline by 25% or more; kill if either margin is missed.
- fastest falsification: Probing plus perturbation re-evaluation on public RGB-D and multi-view data is about 1-2 days on one GPU with public checkpoints.
- fingerprint: text-to-image diffusion features | photometric cue randomization / viewpoint change | depth-probe accuracy and cross-view agreement

### W13-P1-J-006 [characterization_law]
**Conditional denoisers queried with a null prompt produce semantically richer features than genuinely unconditional models of matched scale, because text conditioning during training organizes the internal representation even when unused at inference.**

- hypothesis: [HYPOTHESIS] Training-time text conditioning acts as an auxiliary supervision signal that structures intermediate features; a truly unconditional model trained on the same images will show systematically weaker semantic probes than the null-prompted conditional model.
- kill test: [EXPECTED RESULT] At matched architecture, data, and training compute, null-prompted conditional features will beat unconditional-model features by at least 4 points on a fixed semantic probe suite; kill if the gap is under 1.5 points.
- fastest falsification: Two paired trainings at CIFAR/CC3M-small scale (roughly 2-4 GPU-days total on a single A100 with public data) plus probing.
- fingerprint: paired conditional/unconditional diffusion models | presence of text conditioning during training | semantic probe accuracy

### W13-P1-J-007 [audit_debunk]
**Multi-timestep diffusion feature ensembles are mostly redundant: the timestep-feature stack has low effective rank, and a single well-chosen timestep plus a linear map recovers nearly all probe performance.**

- hypothesis: [HYPOTHESIS] Across timesteps, features are approximately linear transforms of a shared low-dimensional semantic core, so multi-timestep aggregation adds little beyond noise averaging.
- kill test: [EXPECTED RESULT] A probe on single best-timestep features plus a learned linear projection will come within 2 points of the full multi-timestep ensemble on a fixed probe suite, and CKA between timestep features will exceed 0.8 in the semantic band; kill if the ensemble advantage exceeds 5 points.
- fastest falsification: Feature extraction and probing on a 10k-image public set is a sub-day single-GPU experiment with public checkpoints.
- fingerprint: diffusion feature ensembles | number of aggregated timesteps | probe accuracy and representation-similarity (CKA/rank)

### W13-P1-J-008 [characterization_law]
**Diffusion transformers develop high-norm 'register-like' tokens analogous to those in supervised ViTs, and these tokens store global photometric/style state whose deletion selectively breaks style while sparing layout.**

- hypothesis: [HYPOTHESIS] Generative training also induces high-norm aggregate tokens, but their content differs: they buffer global appearance statistics (palette, illumination, style) needed for globally coherent synthesis, rather than classification-relevant summaries.
- kill test: [EXPECTED RESULT] Ablating the top-norm 1% of tokens mid-generation will change global style metrics (color histograms, texture statistics) by at least 3x more than layout metrics (object placement via off-the-shelf detection on outputs); kill if style and layout degrade proportionally within 1.5x.
- fastest falsification: Norm census plus ablation on a few hundred generations is a sub-day single-GPU experiment on public DiT checkpoints.
- fingerprint: DiT-based generators | outlier-token ablation/transplant | style vs layout statistics of generations

### W13-P1-J-009 [constructive_capability]
**Perception heads trained on one diffusion backbone transfer to a different diffusion backbone through a single linear adapter, indicating a shared 'generative representation geometry' across independently trained models.**

- hypothesis: [HYPOTHESIS] Diffusion models trained on similar data converge to representations that are equivalent up to a linear map, so frozen heads plus a cheap adapter recover most cross-model transfer performance.
- kill test: [EXPECTED RESULT] A linear adapter fit on 1% of task data will recover at least 90% of the target-backbone's native head performance for segmentation/depth probes; kill if recovery is below 70% or requires nonlinear adapters to reach it.
- fastest falsification: Head training plus adapter fitting on public dense benchmarks across two public checkpoints is roughly 1-2 GPU-days on a single GPU.
- fingerprint: pairs of public diffusion backbones | cross-model linear adapter | dense-prediction transfer recovery


## diffusion-for-perception (10 ideas)

### W13-P1-J-010 [characterization_law]
**Generative pretraining specifically resolves symmetric-part ambiguity in semantic correspondence (left/right paws, wheels), predicting a large margin over discriminative features exactly on symmetry-confusable pairs and near-parity elsewhere.**

- hypothesis: [HYPOTHESIS] Because generation requires globally consistent part assignment (a left wheel must stay left across the image), diffusion features carry global side/orientation context that discriminative local features lack; the advantage concentrates on symmetry-confusable keypoints.
- kill test: [EXPECTED RESULT] Stratifying a public correspondence benchmark into symmetry-confusable versus unambiguous keypoints will show diffusion features reducing symmetry-flip errors by at least 30% relative to a matched discriminative baseline, while unambiguous-pair accuracy differs by under 5% relative; kill if the advantage is uniform across strata.
- fastest falsification: Stratified re-evaluation of existing public benchmarks with two feature families is a sub-day single-GPU analysis.
- fingerprint: diffusion vs discriminative features | keypoint symmetry stratum | correspondence flip-error rate

### W13-P1-J-011 [characterization_law]
**Generative depth estimators fine-tuned from image diffusion models inherit a photometric prior that fails predictably on non-photorealistic inputs, locating the boundary of the 'repurpose a generator' recipe.**

- hypothesis: [HYPOTHESIS] The recipe's advantage is a photometric-realism prior; on inputs violating natural image statistics (line drawings, scientific visualizations, flat-shaded renders) generative depth models will degrade more than discriminatively pretrained depth models of matched in-domain accuracy.
- kill test: [EXPECTED RESULT] On a matched-pairs protocol (photo vs non-photorealistic depiction of the same geometry), generative-prior depth error will increase at least 2x more than the discriminative baseline's increase; kill if degradations are within 25% relative of each other.
- fastest falsification: Evaluation-only study on public depth checkpoints plus synthetic scenes: under one day on a single GPU.
- fingerprint: generator-derived dense predictors | input depiction style | depth error degradation ratio

### W13-P1-J-012 [constructive_capability]
**Image generators know occluded shape: diffusion features support amodal (completed-shape) segmentation probes far above discriminative features, because generation requires representing whole objects before occlusion.**

- hypothesis: [HYPOTHESIS] To synthesize plausible occlusion scenes, generative models internally represent complete object shape; linear probes on diffusion features will predict occluded object extent substantially better than probes on discriminative features with identical heads and data.
- kill test: [EXPECTED RESULT] On public amodal benchmarks, diffusion-feature probes will beat matched discriminative-feature probes by at least 8 points amodal IoU on heavily occluded instances; kill if the margin is under 3 points.
- fastest falsification: Frozen-feature head training on a public amodal dataset: about one day on one GPU.
- fingerprint: frozen diffusion features | feature source under matched amodal heads | amodal IoU by occlusion fraction

### W13-P1-J-013 [constructive_capability]
**Diffusion-classifier accuracy is bottlenecked by noise-sample variance rather than model knowledge, so paired-noise variance reduction closes most of the gap to discriminative readouts at a fraction of the usual inference cost.**

- hypothesis: [HYPOTHESIS] The class-conditional loss differences that drive the decision are small relative to per-noise-sample variance; sharing identical noise draws across classes and antithetic sampling shrink the estimator variance enough to reveal substantially higher underlying accuracy.
- kill test: [EXPECTED RESULT] Variance-reduced estimation at a fixed budget of 32 denoiser calls per image will recover at least half of the accuracy gap between a naive 32-call diffusion classifier and its 512-call ceiling; kill if the recovery is under 20% of that gap.
- fastest falsification: A few thousand images with tens of denoiser calls each on one GPU: about one day with public checkpoints and data.
- fingerprint: diffusion classifier | likelihood estimator design (noise pairing) | classification accuracy vs NFE

### W13-P1-J-014 [audit_debunk]
**Cross-attention localization in text-to-image models collapses selectively for relational prompts: attention maps localize single objects well but misassign attributes in two-object scenes at a rate predictable from token co-occurrence statistics.**

- hypothesis: [HYPOTHESIS] Attention-map localization is reliable exactly when prompt tokens map to visually distinctive regions independently, and breaks when attribute binding is required, with error rate rising with training-corpus co-occurrence between the attributes and both objects.
- kill test: [EXPECTED RESULT] On generated two-object scenes with swapped attributes, token-attribution maps will assign the attribute to the wrong object in at least 25% of cases while single-object localization stays above 85% pointing-game accuracy; kill if relational and single-object accuracy differ by under 10 points.
- fastest falsification: A few thousand controlled generations plus automated scoring: under one day on a single GPU.
- fingerprint: cross-attention maps of T2I models | prompt relational complexity | pointing-game/attribution accuracy

### W13-P1-J-015 [constructive_capability]
**Occlusion ordering (which object is in front) is linearly decodable from diffusion self-attention geometry without any depth supervision, and more accurately than from discriminative features.**

- hypothesis: [HYPOTHESIS] Synthesizing correct occlusions forces generators to represent depth ordering as an explicit relational feature, making pairwise front/behind relations linearly separable in attention-derived embeddings.
- kill test: [EXPECTED RESULT] A linear classifier on pooled pairwise attention features will predict occlusion order on public panoptic datasets with at least 80% accuracy, beating the same probe on discriminative features by 8 or more points; kill if below 70% or within 3 points of baseline.
- fastest falsification: Feature pooling plus linear probes on public datasets: a few hours on one GPU.
- fingerprint: diffusion attention features | probe target = pairwise occlusion order | ordering accuracy vs baseline features

### W13-P1-J-016 [characterization_law]
**Diffusion features degrade more gracefully under common corruptions than discriminative features, with a measurable crossover severity beyond which the denoising-adjacent pretraining advantage dominates.**

- hypothesis: [HYPOTHESIS] Because denoising training continuously exposes the network to corrupted inputs, diffusion features retain task-relevant structure deeper into corruption severity, producing a severity-dependent crossover where they overtake stronger clean-condition discriminative features.
- kill test: [EXPECTED RESULT] On corruption-benchmark protocols applied to frozen-feature dense probes, diffusion features' relative degradation from severity 1 to 5 will be at least 30% smaller than discriminative features', with a crossover at or before severity 4 for at least half the corruption types; kill if no crossover occurs anywhere and degradation slopes are within 10% relative.
- fastest falsification: Frozen-feature probing across corruption severities on public data: about one day on a single GPU.
- fingerprint: frozen features across pretraining objectives | corruption type and severity | dense-probe degradation slope

### W13-P1-J-017 [constructive_capability]
**Structured inpainting is a scene-understanding test: masking context-critical regions and scoring semantic plausibility of completions yields a graded measure of what a generator understands about scenes, orthogonal to image-quality scores.**

- hypothesis: [HYPOTHESIS] Completion plausibility under context-selective masking (mask the road but keep the cars; mask the shadow but keep the object) measures relational scene knowledge, and models of similar image quality will separate widely on it.
- kill test: [EXPECTED RESULT] Two public generators within 10% of each other on standard quality metrics will differ by at least 25% relative on context-consistency scores (checked by off-the-shelf detectors/VQA over completions, e.g., shadow direction consistent with object and light); kill if all tested model pairs track quality metrics within 10% relative.
- fastest falsification: A few thousand masked completions across 3 public models plus automated scoring: 1-2 days on one GPU.
- fingerprint: inpainting-capable generators | context-selective mask taxonomy | automated consistency scores on completions

### W13-P1-J-018 [characterization_law]
**Single-image diffusion features carry motion affordances: a linear probe predicts the plausible optical-flow direction field of a static frame, revealing implicit dynamics knowledge in image-only generators.**

- hypothesis: [HYPOTHESIS] Natural images betray their dynamics (poses mid-stride, water direction, traffic orientation), and generative training encodes these cues into features from which coarse expected-motion fields are linearly decodable.
- kill test: [EXPECTED RESULT] A probe from single-frame diffusion features to the next-frame flow direction (quantized to 8 bins, evaluated on public video datasets' first frames) will exceed 45% accuracy on moving pixels against a 12.5% chance floor and beat discriminative-feature probes by at least 5 points; kill if within 2 points of baseline or below 30% accuracy.
- fastest falsification: Probe training on precomputed flow from public video datasets: under one day on one GPU.
- fingerprint: image-diffusion features | probe target = future flow direction | quantized flow-direction accuracy

### W13-P1-J-019 [constructive_capability]
**A one-step distilled diffusion model retains most of the parent's dense-perception feature quality at 1/20th the extraction cost, making diffusion backbones cost-competitive with discriminative ViTs for the first time.**

- hypothesis: [HYPOTHESIS] Distillation to one step preserves the internal representation (which the student must keep to imitate the teacher's output map) even while trajectory information is lost, so probe performance drops far less than generation-diversity metrics do.
- kill test: [EXPECTED RESULT] Frozen features from a public one-step distilled student will retain at least 90% of teacher probe performance on a fixed dense suite (segmentation, depth, correspondence); kill if retention falls below 75% on two or more tasks.
- fastest falsification: Probe-suite evaluation on two public checkpoints: a few hours on a single GPU; the optional controlled distillation replicate is 2-3 GPU-days at small scale.
- fingerprint: distilled one-step generators | teacher-vs-student backbone | dense-probe retention fraction


## guidance-science (9 ideas)

### W13-P1-J-020 [characterization_law]
**Classifier-free guidance sharpens the output distribution with a lawful, measurable exponent: embedding-space sample variance shrinks as a power law in guidance scale, with mode-dropping onset at a critical scale predictable from conditional/unconditional score divergence.**

- hypothesis: [HYPOTHESIS] Guidance acts as a temperature-like sharpening whose variance-reduction exponent is approximately constant across prompts within a model, and modes drop when the sharpened density's local mass falls below a threshold set by the divergence between conditional and unconditional scores.
- kill test: [EXPECTED RESULT] Log embedding-variance versus log guidance scale will be linear (R^2 >= 0.9) over the practical range for at least 80% of tested prompt families, and the estimated critical scale will predict observed mode-count collapse within +/-1 guidance unit; kill if linearity fails (R^2 < 0.7) for most prompts or critical-scale predictions miss by more than 2 units.
- fastest falsification: Tens of thousands of samples across scales for ~20 prompts on one GPU: roughly 1-2 days with public checkpoints.
- fingerprint: classifier-free guidance | guidance scale sweep | embedding variance / mode-count scaling

### W13-P1-J-021 [characterization_law]
**CFG's benefit is confined to a narrow mid-trajectory SNR window, and its artifacts (oversaturation, waxy textures) are produced almost entirely by applying guidance outside that window at low noise.**

- hypothesis: [HYPOTHESIS] Semantic alignment is decided in a mid-SNR window where conditional and unconditional scores disagree about content; at low noise the disagreement is dominated by color/contrast statistics, so late guidance mostly extrapolates off-manifold and produces the saturation artifact family.
- kill test: [EXPECTED RESULT] Guidance applied only in the identified mid-SNR window will retain at least 90% of full-schedule alignment (text-image score) while reducing saturation-artifact measures by at least 50%; kill if window-only guidance loses more than 25% of the alignment gain at any window placement.
- fastest falsification: Window sweeps at ~10 placements times ~2k samples on one GPU: about a day with public models.
- fingerprint: CFG schedule | guidance window placement in SNR | alignment vs artifact metric curves

### W13-P1-J-022 [constructive_capability]
**The null-prompt baseline in CFG is the wrong anchor: replacing the empty-string unconditional branch with a learned corpus-mean prompt embedding yields equal alignment at lower guidance scales with fewer artifacts.**

- hypothesis: [HYPOTHESIS] The empty prompt is itself an off-distribution condition whose score has idiosyncratic biases; anchoring guidance at the corpus-mean condition produces a cleaner contrast direction, achieving the same alignment with smaller extrapolation magnitude.
- kill test: [EXPECTED RESULT] Mean-anchor guidance will match null-anchor alignment at a guidance scale at least 25% lower and reduce artifact measures by at least 20% at matched alignment; kill if required scales differ by under 10% or artifacts do not improve.
- fastest falsification: Pareto sweep with two anchors, ~4k samples per configuration on one GPU: under a day using public checkpoints and caption corpora.
- fingerprint: CFG anchor branch | unconditional-anchor distribution | alignment-artifact Pareto front

### W13-P1-J-023 [characterization_law]
**Negative prompts and positive guidance are mechanistically asymmetric: negation via score subtraction removes appearance features but cannot remove relational or compositional content, predicting a measurable class of un-negatable concepts.**

- hypothesis: [HYPOTHESIS] Score-space subtraction can suppress concepts encoded as roughly linear appearance directions (styles, textures, single objects) but fails for content encoded relationally (spatial arrangements, object counts, interactions), which lacks a subtractable direction.
- kill test: [EXPECTED RESULT] A taxonomy-based test will show appearance-level negative prompts succeeding in over 70% of generations while relational negative prompts (e.g., suppressing 'two objects touching') succeed in under 30%; kill if success rates differ by less than 15 points across the taxonomy.
- fastest falsification: A few thousand generations across the taxonomy with automated scoring: under a day on one GPU.
- fingerprint: negative prompting | concept type in taxonomy | suppression success rate

### W13-P1-J-024 [constructive_capability]
**Guidance direction transfers across model scale: the conditional-minus-unconditional score direction computed by a small cheap model can steer a large model's sampling with most of the alignment benefit at a fraction of the compute.**

- hypothesis: [HYPOTHESIS] The guidance direction is a low-complexity semantic signal that small models estimate nearly as well as large ones, so cross-model guidance (large conditional branch, small model providing the contrast) preserves alignment while cutting the second-branch cost.
- kill test: [EXPECTED RESULT] Cross-scale guidance will retain at least 85% of same-model CFG's alignment gain while cutting guidance-branch FLOPs by at least 4x; kill if retention falls below 60% after affine calibration of the small model's direction.
- fastest falsification: Cross-guidance sampling sweeps on one GPU with public checkpoints of two scales: about a day.
- fingerprint: cross-model CFG | scale of the guidance branch | alignment retention vs FLOPs

### W13-P1-J-025 [characterization_law]
**High guidance scales amplify verbatim training-set recall: for duplication-prone prompts, extraction rates rise superlinearly with guidance scale because guidance sharpens toward memorized attractors.**

- hypothesis: [HYPOTHESIS] Memorized images act as sharp modes of the conditional density; since guidance exponentially reweights toward regions where conditional and unconditional scores disagree most, it preferentially amplifies exactly those attractors.
- kill test: [EXPECTED RESULT] For prompts with known duplicated training content, near-copy generation rate will grow superlinearly in guidance scale (at least 3x from scale 1 to scale 7), while matched non-duplicated prompts stay flat within 1.5x; kill if extraction rates are flat or sublinear in scale.
- fastest falsification: Scale sweeps for ~200 prompt candidates with perceptual retrieval against public corpus subsets: 1-2 days on one GPU.
- fingerprint: open T2I checkpoint with public corpus | guidance scale | near-copy extraction rate

### W13-P1-J-026 [constructive_capability]
**Per-prompt optimal guidance scale is predictable from prompt statistics alone (token rarity, length, specificity), enabling a trained scale-predictor that beats any fixed global scale on the alignment-diversity Pareto front.**

- hypothesis: [HYPOTHESIS] The optimal scale reflects how far the conditional distribution is from the marginal, which is estimable from prompt features (rarity, syntactic specificity, embedding norm), so a lightweight regressor can set scale per prompt.
- kill test: [EXPECTED RESULT] A prompt-conditioned scale predictor will dominate every fixed scale, improving alignment at matched diversity by at least 10% relative (or diversity at matched alignment by 15% relative) on held-out prompts; kill if no adaptive policy beats the best fixed scale by more than 3% relative.
- fastest falsification: Scale sweeps over ~1k prompts with automated metrics on one GPU: about 2 days; the regressor itself is minutes to train.
- fingerprint: guidance scale policy | prompt-conditioned scale prediction | alignment-diversity Pareto dominance

### W13-P1-J-027 [constructive_capability]
**Cross-model CFG (conditional branch from model A, unconditional from model B) works if and only if the two models' score fields agree up to an affine map, giving an operational compatibility test for mixing generative models.**

- hypothesis: [HYPOTHESIS] The CFG contrast is meaningful only when both branches share a score geometry; a cheap pre-test measuring affine alignment of the two models' scores on common inputs predicts whether mixed guidance produces coherent images or artifact soup.
- kill test: [EXPECTED RESULT] An affine-alignment score computed on 500 shared noisy inputs will predict mixed-guidance output quality across model pairs with rank correlation at least 0.7; kill if correlation falls below 0.4.
- fastest falsification: Score-alignment probing plus mixed sampling across ~10 model pairs on one GPU: about 2 days with public checkpoints.
- fingerprint: pairs of generators under mixed guidance | score-field affine alignment | mixed-output quality correlation

### W13-P1-J-028 [characterization_law]
**Perceptual guidance strength is what saturates, not information: past a modest scale, extra guidance stops adding text-relevant image content and only shifts global statistics, measurable as a plateau in mutual-information proxies between prompt tokens and image regions.**

- hypothesis: [HYPOTHESIS] Token-to-region information transfer saturates at moderate guidance; beyond that point alignment-metric gains are driven by saturation/contrast statistics those metrics happen to reward, not by additional semantic binding.
- kill test: [EXPECTED RESULT] Attribution-based token-region correspondence measures will plateau (slope < 10% of initial) beyond a saturation scale while global alignment scores keep rising by 15%+ over the same range; kill if correspondence measures keep growing in step with alignment scores.
- fastest falsification: Scale sweeps with two measurement families over ~1k prompts: about a day on one GPU with public models.
- fingerprint: guidance scale response | measurement family (global alignment vs token-region binding) | saturation-point dissociation


## inversion-editing-pathologies (9 ideas)

### W13-P1-J-029 [characterization_law]
**DDIM inversion error is spectrally lawful: reconstruction error concentrates where local high-frequency energy is high, so a cheap spectral map of an image predicts where subsequent edits will fail before any editing is attempted.**

- hypothesis: [HYPOTHESIS] Inversion error is dominated by the ODE discretization interacting with high-curvature score regions, which co-locate with high local spectral energy; therefore a per-region spectral statistic predicts per-region inversion and editing error.
- kill test: [EXPECTED RESULT] Local spectral energy will predict per-patch inversion reconstruction error with rank correlation at least 0.6 across a diverse public image set, and patches in the top spectral decile will show at least 3x the edit-failure rate of the bottom decile; kill if correlation is below 0.3.
- fastest falsification: Inversion plus analysis over ~2k public images on one GPU: a few hours.
- fingerprint: DDIM inversion | local spectral energy of input | spatially resolved reconstruction/edit error

### W13-P1-J-030 [constructive_capability]
**Inversion failure under classifier-free guidance is a per-timestep bias, not noise: the error grows systematically with guidance scale, and null-text-style fixes work precisely because they absorb this bias term, which can be measured and corrected directly.**

- hypothesis: [HYPOTHESIS] The guided reverse trajectory deviates from the inverted trajectory by a structured per-timestep offset dominated by the guidance term; this offset is low-dimensional and predictable, so a closed-form or cheaply fitted correction recovers most of what per-image optimization does.
- kill test: [EXPECTED RESULT] A globally fitted per-timestep correction (no per-image optimization) will recover at least 70% of the reconstruction-quality gap between naive guided inversion and per-image null-text optimization; kill if recovery is below 40%.
- fastest falsification: Offset measurement and global-correction fitting over ~500 images: under a day on one GPU with public checkpoints.
- fingerprint: guided inversion | per-timestep bias correction | reconstruction recovery fraction

### W13-P1-J-031 [characterization_law]
**Iterated invert-edit cycles converge to model-typical attractor images: identity drifts toward the generator's mean style at a measurable geometric rate, giving a quantitative 'regression to the generative mean' law for sequential editing.**

- hypothesis: [HYPOTHESIS] Each invert-edit round trip contracts the image toward high-density regions of the model distribution; identity distance to the original grows with round count following a contraction-mapping pattern with a model-specific rate.
- kill test: [EXPECTED RESULT] Identity similarity to the original (face-embedding or perceptual metric) will decay approximately geometrically over 10 edit rounds with a stable fitted rate (per-model variance under 20%), and repeated no-op edits will drift measurably (at least 30% of the drift of real edits), proving the pipeline itself contracts; kill if drift is negligible for no-op edits and non-monotonic for real edits.
- fastest falsification: 10-round loops on ~300 images for two public editors: about a day on one GPU.
- fingerprint: invert-edit loops | number of edit rounds | identity-drift decay rate

### W13-P1-J-032 [constructive_capability]
**The inversion-error gap between model-generated and real photographs of matched content is a quantitative measure of the generator's manifold mismatch, usable as a model-diagnostic that tracks training data coverage.**

- hypothesis: [HYPOTHESIS] The real-vs-generated inversion-error gap, computed over content-matched pairs, measures how far the model's learned manifold sits from the real data manifold in each content category, and it varies lawfully across categories with training-data density.
- kill test: [EXPECTED RESULT] The per-category inversion gap will correlate with independent estimates of category frequency in the training corpus at rank correlation 0.5 or better across 30+ categories; kill if correlation is under 0.25.
- fastest falsification: Inversion over ~3k images across categories: a few hours on one GPU; corpus-frequency estimates from existing public analyses.
- fingerprint: inversion reconstruction gap | content category | gap vs training-frequency correlation

### W13-P1-J-033 [audit_debunk]
**No attention-based 'local' editor is actually local: every mainstream inversion-editing method leaks measurable background change, with a floor that current architectures cannot cross, quantified by a background-drift budget protocol.**

- hypothesis: [HYPOTHESIS] Because inversion is imperfect and attention manipulations perturb the whole computation graph, background drift has a nonzero floor across all current inversion-based editors, and the floor is set by inversion error rather than the editing mechanism.
- kill test: [EXPECTED RESULT] Across 4+ public editing methods, masked-background perceptual drift will exceed a nontrivial floor (e.g., LPIPS 0.05-equivalent) on at least 70% of edits, and drift will correlate with per-image inversion error at rank correlation 0.5+; kill if any method achieves near-zero background drift (below the reconstruction noise floor) on most images.
- fastest falsification: Cross-method benchmark on ~500 edits: about a day on one GPU using public implementations.
- fingerprint: inversion-based editors | editing method family | masked background drift

### W13-P1-J-034 [characterization_law]
**Invertibility collapses discontinuously as sampling steps shrink: below a critical step count the inversion round-trip error jumps rather than degrades smoothly, defining a phase boundary for edit-capable fast sampling.**

- hypothesis: [HYPOTHESIS] Inversion error is governed by ODE discretization stability, which has a step-size threshold behavior in high-curvature score regions; below a critical number of steps the round-trip loses content discontinuously rather than gracefully.
- kill test: [EXPECTED RESULT] Round-trip reconstruction error versus step count will show a knee: error changes by more than 50% within a 2x step-count window somewhere below 20 steps, rather than a uniform power-law decline; kill if error follows a smooth power law (local slope varying under 20%) across 4-50 steps.
- fastest falsification: Step sweeps over ~1k images and 3 samplers: a few hours on one GPU.
- fingerprint: inversion round-trip | sampler step count | reconstruction error curve shape

### W13-P1-J-035 [characterization_law]
**Stochastic strength in SDEdit-style editing has a universal sweet spot in SNR terms: the structure-preservation versus realism crossover happens at a similar effective noise level across domains and models, collapsing a per-use hyperparameter to a constant.**

- hypothesis: [HYPOTHESIS] The crossover reflects where content-defining information lives in the corruption hierarchy, which is a property of natural-image statistics rather than the model or domain; in SNR units the optimal strength is approximately universal.
- kill test: [EXPECTED RESULT] Optimal noise strengths (by a fixed structure-realism utility) across 5+ editing domains and 2 models will fall within a 1-nat log-SNR band; kill if optima spread over more than 2.5 nats.
- fastest falsification: Strength grids over ~5 tasks x 2 models x 200 images: about a day on one GPU.
- fingerprint: SDEdit-style editing | stochastic noise strength in SNR units | structure-realism optimum location

### W13-P1-J-036 [audit_debunk]
**Inverted latents carry a prompt fingerprint: inverting an image under the wrong caption embeds recoverable traces of that caption, biasing all downstream edits in measurable, caption-specific directions.**

- hypothesis: [HYPOTHESIS] Because guided inversion bends the trajectory using the caption's score contributions, the resulting latent is caption-contaminated: regenerating under a neutral prompt drifts toward the inversion caption's semantics at a measurable rate.
- kill test: [EXPECTED RESULT] Images inverted under deliberately biased captions and regenerated under neutral prompts will shift toward the biased caption per automated attribute scoring in at least 30% of cases versus under 5% for neutral-caption inversion; kill if the shift rates differ by less than 10 points.
- fastest falsification: Paired-caption inversion on ~300 images with automated scoring: a few hours on one GPU.
- fingerprint: guided inversion | inversion caption content | attribute drift of regenerations

### W13-P1-J-037 [constructive_capability]
**Round-trip consistency (apply an edit, then apply its inverse instruction) is a label-free capability measure for instruction editors, and current editors will fail it at rates that single-edit benchmarks completely hide.**

- hypothesis: [HYPOTHESIS] Editing competence implies approximate invertibility for invertible instructions (add/remove, brighten/darken); measuring identity recovery after instruction round-trips exposes failure structure invisible to one-shot metrics and separates models that one-shot metrics rank as equal.
- kill test: [EXPECTED RESULT] Two public editors within 5% on standard single-edit metrics will differ by at least 20% relative on round-trip identity recovery, and round-trip failure will localize to predictable instruction classes (geometry and count edits worst); kill if round-trip scores track single-edit scores within 5% relative across models.
- fastest falsification: Round trips on ~500 images x 20 instruction pairs x 2 editors: about a day on one GPU.
- fingerprint: instruction-following editors | instruction round-trip protocol | identity-recovery score


## generator-memorization (9 ideas)

### W13-P1-J-038 [characterization_law]
**Verbatim memorization versus duplication count follows a sharp sigmoidal threshold, and the threshold location shifts predictably with model capacity, yielding a quantitative memorization law usable for dataset dedup policy.**

- hypothesis: [HYPOTHESIS] Memorization probability versus log duplication count is sigmoidal with a capacity-dependent midpoint: doubling model parameters shifts the midpoint toward fewer required duplicates by a measurable, roughly constant factor.
- kill test: [EXPECTED RESULT] In controlled small-scale trainings with planted duplicates, the fitted response will be sigmoidal (deviance strongly favoring it over linear) with midpoint shifting at least 1.3x per model-size doubling; kill if the response is linear/concave without threshold structure, or midpoints do not move with capacity.
- fastest falsification: A grid of ~9 small trainings (3 sizes x 3 duplication levels) at CIFAR scale: roughly 4-6 GPU-days total on a single GPU with public data.
- fingerprint: small diffusion models with planted duplicates | duplication count x model capacity | near-copy rate dose-response

### W13-P1-J-039 [constructive_capability]
**Text keys, not image copies, gate verbatim recall in text-to-image models: perturbing the prompt away from the memorized caption collapses extraction rates even for heavily duplicated images, enabling inference-time mitigation without retraining.**

- hypothesis: [HYPOTHESIS] Verbatim recall is retrieved through the conditioning pathway: memorized items are stored as caption-keyed attractors, so caption-space perturbations (paraphrase, token dropout) break retrieval even though the image remains 'stored' in the weights.
- kill test: [EXPECTED RESULT] Light prompt paraphrasing will reduce near-copy rates by at least 80% relative for known-memorized items while leaving prompt-faithfulness for non-memorized prompts within 5% of baseline; kill if paraphrase-resistant recall stays above half its original rate.
- fastest falsification: Prompt-perturbation sweeps on known-memorized items: a few hours on one GPU with an open checkpoint.
- fingerprint: open T2I checkpoint | prompt-key perturbation | near-copy rate change

### W13-P1-J-040 [characterization_law]
**Memorized items sit in measurably sharper score-field attractors: reverse trajectories initialized in a neighborhood converge to memorized images faster and from a wider basin than to novel generations, giving a geometric signature of memorization.**

- hypothesis: [HYPOTHESIS] Memorization corresponds to local over-sharpening of the learned density: around memorized outputs, trajectory convergence rate is higher and sensitivity to initial-noise perturbation is lower than around matched novel outputs.
- kill test: [EXPECTED RESULT] Perturbing initial noise by a fixed budget will change memorized generations at least 3x less (perceptual distance) than matched non-memorized generations, and local convergence-rate estimates will separate the two groups with AUC 0.8+ in a characterization (not deployment-detector) setting; kill if AUC is below 0.65 or perturbation sensitivity is comparable.
- fastest falsification: Perturbation ensembles for ~100 memorized plus 100 control items: a few hours on one GPU.
- fingerprint: score-field geometry | initial-noise perturbation budget | basin sharpness statistics

### W13-P1-J-041 [constructive_capability]
**Prompt-keyed memorization is stored in a localizable sliver of weights (dominantly cross-attention K/V): ablating under 1% of parameters removes specific memorized items with negligible global quality loss, enabling surgical unlearning.**

- hypothesis: [HYPOTHESIS] Caption-keyed recall is implemented as high-influence associations concentrated in cross-attention key/value projections for the trigger tokens, so gradient-attribution can locate and null the responsible weight sliver per item.
- kill test: [EXPECTED RESULT] Attribution-guided editing of at most 1% of weights will cut near-copy rate for targeted items by at least 90% while global quality metrics change by under 2% and non-target prompt fidelity by under 3%; kill if removal requires editing over 5% of weights or global quality drops more than 5%.
- fastest falsification: Attribution plus editing for ~20 memorized items: under a day on one GPU with an open checkpoint.
- fingerprint: open T2I weights | attribution-guided weight ablation budget | targeted extraction rate vs global quality

### W13-P1-J-042 [characterization_law]
**Memorized generations commit early: their trajectories lock onto the final output at higher noise levels than novel generations, so commitment time is a mechanistic covariate of memorization measurable without reference to training data.**

- hypothesis: [HYPOTHESIS] Because memorized attractors are sharp, the reverse trajectory's intermediate x0-predictions converge to the final image earlier (at higher noise) for memorized outputs than for novel outputs of matched content complexity.
- kill test: [EXPECTED RESULT] The noise level at which intermediate x0-predictions reach 90% final-image similarity will be at least 1 log-SNR nat earlier for memorized items than matched controls, separating groups with AUC 0.75+; kill if distributions overlap with AUC under 0.6.
- fastest falsification: Trajectory recording for a few hundred prompts: a few hours on one GPU.
- fingerprint: sampling trajectories | memorized vs control prompts | x0-prediction commitment time

### W13-P1-J-043 [characterization_law]
**Generators memorize compositions far more than pixels: layout-level templates from training data recur in generations at rates vastly exceeding verbatim copying, constituting a second, unmeasured tier of memorization.**

- hypothesis: [HYPOTHESIS] The denoiser stores compositional templates (object arrangement, pose, framing) with much lower storage cost than pixel content, so template recurrence survives dedup and appears at orders-of-magnitude higher rates than verbatim recall.
- kill test: [EXPECTED RESULT] Layout-matching against training-corpus samples (object-arrangement graphs, pose skeletons) will find template near-duplicates at 10x or more the rate of pixel near-duplicates under matched false-positive calibration on shuffled controls; kill if template rates are within 3x of verbatim rates.
- fastest falsification: Layout-descriptor scan of ~50k generations against a public corpus subset: 1-2 days on one GPU.
- fingerprint: generation-vs-corpus comparison | duplicate tier definition (pixel vs layout) | calibrated duplicate rates

### W13-P1-J-044 [characterization_law]
**Personalization fine-tuning (LoRA/DreamBooth-style) memorizes its few training images at rates orders of magnitude above pretraining memorization, with leakage growing superlinearly in fine-tuning steps, making 'private personalization' claims measurable and mostly false.**

- hypothesis: [HYPOTHESIS] With so few targets and many passes, personalization operates deep in the memorization regime: adapters store near-verbatim training images retrievable by prompt probing, with leakage increasing superlinearly in steps and inversely with subject-image count.
- kill test: [EXPECTED RESULT] Prompt-probing personalized adapters will retrieve near-copies (perceptual similarity above a calibrated threshold) of at least 30% of training images under standard recipes, and doubling fine-tune steps will more than double retrieval rate; kill if retrieval stays under 5% across standard recipes.
- fastest falsification: A grid of ~12 personalizations with probing: about 1-2 GPU-days total on a single GPU with public images.
- fingerprint: personalization adapters | fine-tune steps x subject-image count | training-instance retrieval rate

### W13-P1-J-045 [audit_debunk]
**Standard augmentations suppress pixel-tier memorization but leave layout-tier memorization intact, so the field's main training mitigation fixes the audited symptom while preserving the unaudited one.**

- hypothesis: [HYPOTHESIS] Augmentations break pixel alignment, blocking verbatim storage, but compositional templates are augmentation-invariant (crops and flips preserve arrangement structure), so template memorization persists at unchanged rates.
- kill test: [EXPECTED RESULT] In planted-duplicate trainings with and without strong augmentation, verbatim recall will drop by at least 80% relative under augmentation while layout-template recurrence drops by less than 20% relative; kill if augmentation suppresses both tiers proportionally (within 20% of each other).
- fastest falsification: Two paired CIFAR-scale trainings plus tiered audits: about 2-3 GPU-days on one GPU.
- fingerprint: planted-duplicate training | augmentation on/off | tiered memorization suppression ratio

### W13-P1-J-046 [constructive_capability]
**Removing memorized attractors improves the model elsewhere: surgical unlearning of verbatim items increases sample diversity and prompt fidelity in the semantic neighborhood of the removed content, showing memorization actively harms nearby generalization.**

- hypothesis: [HYPOTHESIS] Sharp memorized modes capture probability mass and sampling trajectories from their semantic neighborhood, so nearby prompts under-explore; removing the attractor redistributes mass and measurably increases neighborhood diversity.
- kill test: [EXPECTED RESULT] After targeted unlearning of memorized items, neighborhood prompts (same subject/style family) will show at least 15% relative increase in sample diversity (embedding dispersion) and no loss (within 2%) of prompt fidelity; kill if diversity changes by under 5% relative or fidelity drops more than 5%.
- fastest falsification: Unlearning plus neighborhood sampling for ~10 items: under a day on one GPU with an open checkpoint.
- fingerprint: targeted unlearning | presence of memorized attractor | neighborhood diversity and fidelity


## sampling-dynamics (9 ideas)

### W13-P1-J-047 [characterization_law]
**Semantic layout is decided in a narrow early window of the reverse trajectory: swapping conditioning or noise mid-trajectory localizes a universal 'decision point' in SNR units beyond which content is frozen and only appearance changes.**

- hypothesis: [HYPOTHESIS] Content commitment is concentrated: there exists a narrow SNR band where swapping the prompt or re-drawing noise changes layout with high probability, collapsing to near-zero probability past the band, and the band location in SNR units is stable across models.
- kill test: [EXPECTED RESULT] Layout-change probability versus swap time will drop from over 80% to under 20% within a 1.5-nat log-SNR window, and window centers across two public models will agree within 1 nat; kill if the decline spans more than 4 nats (gradual, no decision point) or models disagree by more than 2 nats.
- fastest falsification: Swap experiments at ~15 time points x 300 prompts x 2 models: about a day on one GPU.
- fingerprint: reverse trajectory | mid-trajectory condition/noise swap | layout-change probability curve

### W13-P1-J-048 [characterization_law]
**ODE and SDE samplers systematically differ in output texture statistics, not just variance: stochastic sampling adds measurable high-frequency power and changes fine-detail rendering, so sampler choice is a content decision, not a numerical one.**

- hypothesis: [HYPOTHESIS] Injected noise during late sampling steps acts as a texture-synthesis mechanism: SDE samplers systematically shift the output power spectrum upward in high-frequency bands relative to ODE samplers from identical initial noise, beyond what resampling variance explains.
- kill test: [EXPECTED RESULT] Paired generations (same seed/prompt) will show SDE outputs carrying at least 10% more relative power in the top frequency octave with high consistency (effect in over 70% of pairs); kill if spectral differences are within noise (under 3% median) once sampler hyperparameters are convergence-matched.
- fastest falsification: Paired generation of ~5k images per sampler on one GPU: a few hours.
- fingerprint: sampler family (ODE vs SDE) | stochasticity injection | output power-spectrum statistics

### W13-P1-J-049 [constructive_capability]
**A model's quality-versus-steps exponent predicts its distillability: generators whose sample quality converges fast in step count distill to few-step students with less loss, giving a cheap pre-test before paying distillation compute.**

- hypothesis: [HYPOTHESIS] Both step-count convergence and distillability are governed by the curvature of the model's probability-flow ODE: low-curvature models need fewer steps and are easier to compress into few-step students, so the convergence exponent is a proxy for distillation loss.
- kill test: [EXPECTED RESULT] Across 6+ public base models, the fitted quality-versus-NFE exponent will predict few-step distillation quality loss with rank correlation at least 0.6; kill if correlation is under 0.3.
- fastest falsification: Exponent fitting is hours; the small-scale distillation grid is the bottleneck at roughly 6-10 GPU-days total on a single GPU.
- fingerprint: base generators | quality-vs-NFE exponent as predictor | distillation loss correlation

### W13-P1-J-050 [audit_debunk]
**Popular samplers do not sample the same distribution: at convergence-equivalent settings, different sampler families produce distributionally distinct outputs (hue, contrast, composition statistics), so sampler choice silently changes every downstream measurement.**

- hypothesis: [HYPOTHESIS] Discretization biases differ by sampler family and persist at practical step counts, producing measurable distribution-level differences (not just per-image noise) that exceed evaluation error bars.
- kill test: [EXPECTED RESULT] Two-sample tests on large generation sets from 3 sampler families at matched compute will reject distributional equality (via classifier two-sample test accuracy above 55% against a 50% null) for at least two family pairs, with interpretable feature shifts; kill if all pairwise tests sit within 52% (indistinguishable).
- fastest falsification: ~60k generations plus classifier tests: about a day on one GPU.
- fingerprint: sampler families at matched compute | sampler choice | two-sample distribution tests

### W13-P1-J-051 [constructive_capability]
**Score-field curvature concentrates in a narrow SNR band, and allocating steps adaptively to that band beats hand-tuned schedules at matched compute, turning schedule design into a measurable-quantity optimization.**

- hypothesis: [HYPOTHESIS] Local truncation error is dominated by trajectory curvature, which is empirically concentrated in a measurable SNR band; measuring curvature once per model and placing steps by curvature mass dominates generic schedules.
- kill test: [EXPECTED RESULT] Curvature-adaptive schedules will match default-schedule quality with at least 25% fewer steps (or improve quality metrics by 10%+ relative at matched steps) across two models; kill if gains are under 5% relative everywhere.
- fastest falsification: Curvature census plus schedule benchmark: under a day on one GPU per model.
- fingerprint: step schedule | curvature-mass step placement | quality at matched NFE

### W13-P1-J-052 [constructive_capability]
**The initial noise seed is a composition genome: under deterministic sampling, seeds impose transferable coarse layouts across prompts, and the seed-layout map is stable enough to build a searchable layout library with no model modification.**

- hypothesis: [HYPOTHESIS] With ODE sampling, initial noise determines coarse composition largely independently of the prompt, so layout similarity between same-seed different-prompt generations far exceeds different-seed baselines, enabling seed-indexed layout control.
- kill test: [EXPECTED RESULT] Same-seed cross-prompt layout similarity (detection-graph overlap) will exceed different-seed similarity by at least 2x on average across prompt families, and a seed library will let users hit target coarse layouts in top-5 retrieval at 60%+ success; kill if same-seed similarity exceeds baseline by under 1.2x.
- fastest falsification: A 100-seed x 50-prompt grid: a few hours on one GPU.
- fingerprint: initial noise seed | seed reuse across prompts | cross-prompt layout similarity

### W13-P1-J-053 [constructive_capability]
**Directions in initial-noise space act as approximate global layout controls: a single linear map from noise-space directions to layout changes explains a large fraction of composition variance, giving training-free steering without attention surgery.**

- hypothesis: [HYPOTHESIS] The ODE map from initial noise to image is smooth enough at coarse scales that principal layout modes correspond to consistent noise-space directions shared across seeds, learnable from a modest paired sample.
- kill test: [EXPECTED RESULT] A linear model from noise perturbation directions to layout deltas will explain at least 30% of coarse layout variance and steer object position with 60%+ success within a tolerance window; kill if explained variance is under 10% or steering success under 30%.
- fastest falsification: Perturbation-pair collection and linear fitting on ~5k generations: under a day on one GPU.
- fingerprint: initial-noise space | linear noise-direction steering | layout steering success rate

### W13-P1-J-054 [characterization_law]
**Repeated renoise-denoise cycles converge to model-typical fixed points, and the convergence rate is a per-region 'manifold attraction' measure that predicts how aggressively a model will rewrite content in any img2img use.**

- hypothesis: [HYPOTHESIS] Iterating moderate-strength renoise-denoise acts as a projection toward the model's manifold; its per-region convergence rate (how fast content stops changing) measures local manifold attraction and predicts single-pass img2img edits' rewriting behavior.
- kill test: [EXPECTED RESULT] Per-region convergence rates from 5-cycle iteration will predict single-pass img2img content change with rank correlation 0.6+ across regions, and atypical content (rare objects, unusual textures) will converge at least 2x slower... [direction: rare content keeps changing longer]; kill if correlation is under 0.3.
- fastest falsification: 5-cycle iterations on ~500 images: a few hours on one GPU.
- fingerprint: renoise-denoise iteration | cycle count | per-region convergence rate

### W13-P1-J-055 [constructive_capability]
**Early-stopping the reverse ODE at a nonzero noise floor is an implicit truncation trick for diffusion: it trades diversity for typicality along a lawful curve, giving a free post-hoc knob equivalent to GAN truncation with a measurable exponent.**

- hypothesis: [HYPOTHESIS] Terminating sampling early (then doing a final x0-prediction) contracts outputs toward high-density regions, producing a diversity-typicality tradeoff curve with a stable exponent that complements guidance and composes with it predictably.
- kill test: [EXPECTED RESULT] Sweeping the stop floor will trace a smooth diversity-typicality frontier where log-diversity declines approximately linearly with stop-level (R^2 >= 0.85), and combining moderate early stop with lower guidance will match the alignment of high guidance with at least 10% relative more diversity; kill if the frontier is non-monotonic or the combination never beats guidance-only.
- fastest falsification: Two-knob sweep with ~10k generations: about a day on one GPU.
- fingerprint: early ODE termination | stop-floor level | diversity-typicality frontier


## diffusion-priors-for-ambiguity (8 ideas)

### W13-P1-J-056 [characterization_law]
**Sample spread of generative depth models localizes at genuinely ill-posed pixels: multi-sample dispersion concentrates at occlusion boundaries and scale-ambiguous regions, matching multi-sensor disagreement rather than being uniform noise.**

- hypothesis: [HYPOTHESIS] Because the generative prior learns the multi-modality of the depth-given-image relationship, per-pixel sample dispersion is not isotropic noise but tracks the physically ill-posed structure: it peaks where the inverse problem genuinely admits multiple answers.
- kill test: [EXPECTED RESULT] Per-pixel sample dispersion will rank-correlate with independent ambiguity ground truth (multi-sensor disagreement or multi-annotator variance on public RGB-D data) at 0.5+ within images, at least 2x the correlation achieved by a softmax-entropy baseline from a matched discriminative model; kill if within-image correlation is below 0.25 or no better than the discriminative baseline.
- fastest falsification: 32 samples per image over ~500 public RGB-D images plus correlation analysis: a few hours on one GPU.
- fingerprint: generative depth predictor | sampling repetition | dispersion-vs-ambiguity correlation

### W13-P1-J-057 [characterization_law]
**Generative segmentation samplers reproduce the distribution of human annotator disagreement, not just its magnitude: sampled mask sets match inter-annotator mask distributions on multi-rater datasets better than any softmax-derived baseline.**

- hypothesis: [HYPOTHESIS] Diffusion mask samplers learn the joint structure of plausible annotations, so their sample sets capture correlated, region-level disagreement modes that per-pixel independence assumptions cannot express.
- kill test: [EXPECTED RESULT] On public multi-rater segmentation data, the generalized energy distance between sampled mask sets and rater mask sets will beat per-pixel-independent baselines by at least 20% relative, specifically on region-level disagreement cases; kill if the improvement is under 5% relative or confined to boundary-width effects.
- fastest falsification: Adaptation plus evaluation on one public multi-rater dataset: roughly 1-2 GPU-days on a single GPU.
- fingerprint: diffusion mask sampler | disagreement component (boundary vs region) | distribution-matching to rater sets

### W13-P1-J-058 [audit_debunk]
**Diffusion posterior samplers for inverse problems systematically under-disperse: sampled posteriors are provably narrower than the true posterior in controlled linear inverse settings, with a measurable contraction factor that practitioners should correct for.**

- hypothesis: [HYPOTHESIS] Approximations in posterior-guidance methods (likelihood linearization, score errors, mode-seeking dynamics) compound into systematic over-concentration: the sampled posterior's variance underestimates the true posterior variance by a large, quantifiable factor that grows with measurement sparsity.
- kill test: [EXPECTED RESULT] In synthetic linear inverse problems where the exact posterior is computable (Gaussian mixtures, small images), diffusion posterior samplers will exhibit variance ratios (sampled/true) below 0.5 in sparse-measurement regimes, worsening as measurements decrease; kill if variance ratios stay within [0.8, 1.2] across regimes.
- fastest falsification: Small synthetic diffusion prior plus exact-posterior comparisons: about 1 GPU-day on a single GPU, all synthetic public-reproducible data.
- fingerprint: diffusion posterior sampling | measurement sparsity | sampled-vs-exact posterior variance ratio

### W13-P1-J-059 [characterization_law]
**Distilling a generative dense predictor into a one-step model destroys ambiguity information in a predictable spatial pattern: the student blurs exactly where the teacher's samples disperse, converting represented multi-modality into averaged error.**

- hypothesis: [HYPOTHESIS] Distillation objectives implicitly average over teacher modes; at pixels where the teacher's posterior is multi-modal the student regresses to the mean, so student blur/error maps will spatially match teacher dispersion maps.
- kill test: [EXPECTED RESULT] Spatial correlation between teacher sample-dispersion maps and student residual-blur maps will exceed 0.5 across public depth benchmarks, and student error at high-dispersion pixels will exceed teacher single-sample error by 30%+ relative; kill if correlation is under 0.2.
- fastest falsification: Small-scale distillation plus map comparison: roughly 2 GPU-days on a single GPU with public models and data.
- fingerprint: distilled dense predictor | teacher multi-modality | spatial blur-dispersion correspondence

### W13-P1-J-060 [characterization_law]
**Generative optical-flow samplers express the aperture problem geometrically: sample spread at motion-ambiguous edges is elongated along the edge direction, matching the theoretical null space of the local motion constraint.**

- hypothesis: [HYPOTHESIS] A generative flow model trained on enough data internalizes the local observability structure of motion: at aperture-limited pixels its samples will disperse anisotropically along the theoretically unobservable direction, not isotropically.
- kill test: [EXPECTED RESULT] At detected aperture-limited pixels, the dominant eigenvector of the per-pixel sample-spread covariance will align with the local edge direction within 20 degrees for at least 60% of pixels (chance ~22%); kill if alignment is at chance or spread is isotropic (eigenvalue ratio under 1.5).
- fastest falsification: 32 samples per pair over ~200 public flow pairs plus geometry analysis: a few hours on one GPU.
- fingerprint: generative flow model | aperture-limited pixel selection | dispersion anisotropy vs edge direction

### W13-P1-J-061 [constructive_capability]
**The learned generative prior dominates conditioning evidence at a lawful, measurable noise threshold: for conditional dense prediction, prior-driven hallucination onsets where the condition's information rate falls below the prior's, predicting exactly where generative predictors invent content.**

- hypothesis: [HYPOTHESIS] Along the sampling trajectory there is a per-region crossover between evidence-dominated and prior-dominated dynamics, measurable by comparing output sensitivity to input perturbations against sensitivity to prior perturbations; hallucination localizes past the crossover.
- kill test: [EXPECTED RESULT] A sensitivity-ratio map (input-sensitivity over prior-sensitivity) will predict hallucination locations (regions where output disagrees with masked-input ground truth) with AUC 0.75+ across occlusion levels; kill if AUC is under 0.6.
- fastest falsification: Sensitivity mapping on ~200 masked images: about a day on one GPU.
- fingerprint: conditional generative predictor | evidence-vs-prior sensitivity ratio | hallucination-location prediction AUC

### W13-P1-J-062 [characterization_law]
**Consensus across diffusion samples predicts correctness in-domain but the coupling collapses under domain shift in a measurable way, defining the validity boundary for using sample agreement as a quality proxy.**

- hypothesis: [HYPOTHESIS] Agreement-accuracy coupling is a property of the training distribution: under distribution shift the model can be confidently wrong in correlated ways across samples, so consensus stays high while accuracy falls, breaking the proxy exactly when it is most needed.
- kill test: [EXPECTED RESULT] Across a shift ladder (same task, increasing domain distance), the consensus-accuracy rank correlation will fall from 0.6+ in-domain to under 0.2 at strong shift while mean consensus itself drops by less than 20%, demonstrating correlated confident errors; kill if the coupling stays above 0.5 at all shift levels (proxy robust) or consensus collapses in step with accuracy (proxy honestly uncertain).
- fastest falsification: Sampling across 4 shift levels x 300 images: a few hours on one GPU with public datasets.
- fingerprint: sampling consensus proxy | domain-shift level | consensus-accuracy coupling curve

### W13-P1-J-063 [characterization_law]
**Generative amodal completion samples span the space of human beliefs about hidden content: the diversity of sampled completions for occluded regions matches the distribution of human guesses, making generators measurable models of shared visual expectation.**

- hypothesis: [HYPOTHESIS] Generative models trained on natural scenes internalize the same statistical regularities humans use, so their completion distributions (object identity, extent, pose behind occluders) will approximate aggregated human predictions well beyond chance and beyond class-prior baselines.
- kill test: [EXPECTED RESULT] On a curated occlusion set with collected human completion judgments, the Jensen-Shannon divergence between model completion distributions and human distributions will beat a class-prior baseline by 30%+ relative and correlate with human entropy per item at 0.4+; kill if the model matches humans no better than the class-prior baseline.
- fastest falsification: Sampling and binning are a few GPU-hours; the bottleneck is a small crowd study (needs_special_resources=true only if human study is unavailable; a pilot with lab annotators suffices).
- fingerprint: amodal completion sampler | occluded-content item | model-vs-human completion distribution divergence


## conditioning-binding (8 ideas)

### W13-P1-J-064 [characterization_law]
**Attribute-binding failures are decided in a narrow early timestep window through cross-attention competition, so timestep-targeted attention intervention fixes most binding errors while leaving the rest of generation untouched.**

- hypothesis: [HYPOTHESIS] Binding is resolved when object regions first individuate (early, high-noise steps); attribute tokens compete for regions only in that window, so interventions confined to it capture the full fixable fraction of binding failures at minimal collateral cost.
- kill test: [EXPECTED RESULT] Attention intervention restricted to the first quarter of steps will recover at least 80% of the binding-accuracy improvement of full-schedule intervention while reducing off-target image change by 50%+; kill if late-window intervention performs within 10% of early-window (no temporal specificity).
- fastest falsification: Window ablations over ~2k prompts: under a day on one GPU with public models.
- fingerprint: cross-attention binding | intervention timestep window | binding accuracy vs off-target change

### W13-P1-J-065 [characterization_law]
**Object-count control fails because count is not linearly represented anywhere in the conditioning pathway beyond small numbers: probing text and image streams will find count decodable up to about four and absent beyond, matching the generation failure boundary.**

- hypothesis: [HYPOTHESIS] The failure is representational: the conditioning pathway encodes numerosity like a subitizing system (distinct up to ~4, log-compressed beyond), so generation cannot execute counts its representation does not distinguish; probe decodability and generation accuracy will share the same breakpoint.
- kill test: [EXPECTED RESULT] Linear probes for requested count on text-encoder and cross-attention representations will show accuracy falling below 60% beyond count 4-5 exactly where generation count-accuracy collapses, with the two breakpoints within 1 unit; kill if representations remain decodable (85%+) at counts where generation fails.
- fastest falsification: Probing plus ~3k generations with automated counting: a few hours on one GPU.
- fingerprint: conditioning pathway | requested object count | probe-vs-generation breakpoint alignment

### W13-P1-J-066 [constructive_capability]
**Prompt token influence follows a lawful positional decay: later tokens in long prompts lose per-token causal effect on the image at a measurable rate, and re-normalizing attention by position recovers late-token content without retraining.**

- hypothesis: [HYPOTHESIS] Softmax attention over many tokens dilutes per-token mass with prompt length and position (compounded by causal text-encoder biases), producing a measurable positional influence decay that a position-corrected attention rescaling can flatten.
- kill test: [EXPECTED RESULT] Causal token-deletion tests will show late-quartile tokens having at least 40% less image effect than early-quartile tokens in 60+ token prompts, and positional rescaling will recover late-token content realization by 25%+ relative without harming early content by more than 5%; kill if positional decay is under 15% (no meaningful effect).
- fastest falsification: Permutation battery over ~1k prompts: a few hours on one GPU.
- fingerprint: prompt token position | position-permuted content units | per-position realization rate

### W13-P1-J-067 [characterization_law]
**The same concept prompted in different languages generates measurably different visual distributions, and the differences are systematic (cultural-visual priors of the training pairs), quantifying language as a hidden conditioning variable in multilingual models.**

- hypothesis: [HYPOTHESIS] The conditioning pathway binds each language's tokens to that language's co-occurring visual statistics, so translation-equivalent prompts yield distribution-level differences (objects, settings, aesthetics) far exceeding sampling noise, predictable from corpus provenance.
- kill test: [EXPECTED RESULT] Classifier two-sample tests between generation sets from translation-equivalent prompts will exceed 60% accuracy (50% null) for at least half of tested concept-language pairs, with shift directions consistent with corpus provenance in blind human ratings; kill if distributions are indistinguishable (under 53%) for most pairs.
- fastest falsification: ~2k generations per language for ~20 concepts plus tests: under a day on one GPU.
- fingerprint: multilingual conditioning | prompt language | cross-language generation distribution divergence

### W13-P1-J-068 [audit_debunk]
**Spatial prepositions are executed by 2D canvas priors, not relational understanding: 'X above Y' succeeds only when the pair's canonical canvas arrangement agrees, and fails at predictable rates under counterfactual arrangements.**

- hypothesis: [HYPOTHESIS] The model resolves spatial prepositions by sampling the most frequent canvas arrangement of the object pair from training statistics; genuine relational control exists only weakly, so accuracy collapses when the requested relation contradicts the canonical arrangement.
- kill test: [EXPECTED RESULT] Accuracy on canonical-relation prompts (bird above fence) will exceed counter-canonical prompts (fence above bird) by at least 30 points across a balanced benchmark; kill if the canonicality gap is under 10 points (real relational control).
- fastest falsification: Balanced benchmark of ~1k prompt pairs with automated scoring: a few hours on one GPU.
- fingerprint: spatial-relation conditioning | canonical vs counter-canonical arrangement | relation accuracy gap

### W13-P1-J-069 [characterization_law]
**Conditioning modalities have a stable dominance hierarchy with measurable exchange rates: when text and structural conditions (edges, pose, depth) conflict, the resolution follows a lawful ordering that predicts multi-condition behavior before running it.**

- hypothesis: [HYPOTHESIS] Each conditioning channel exerts influence proportional to its information rate about pixels and its injection depth; conflicts resolve by a consistent dominance ordering (dense structural > sparse structural > text) with quantifiable exchange rates that are stable across content.
- kill test: [EXPECTED RESULT] In controlled conflict batteries (text says left, pose says right), structural conditions will win at least 75% of conflicts against text at default strengths, and fitted exchange rates (strength units of one condition per unit of another) will predict held-out conflict outcomes within 15%; kill if dominance is content-dependent and unstable (prediction error over 35%).
- fastest falsification: Conflict batteries of ~3k generations: under a day on one GPU with public control adapters.
- fingerprint: multi-condition generation | condition conflict battery | dominance ordering and exchange rates

### W13-P1-J-070 [characterization_law]
**Negation blindness lives in the text encoder, not the denoiser: negated prompts embed nearly identically to their affirmative forms, and embedding-level surgery fixes more negation failures than any sampling-time intervention.**

- hypothesis: [HYPOTHESIS] Contrastively trained text encoders map negated phrases close to affirmative ones (negation words carry little visual-embedding weight), so the denoiser never receives the negation; interventions that re-inject negation at the embedding level will dominate sampling-time fixes.
- kill test: [EXPECTED RESULT] Embedding similarity between negated and affirmative prompt pairs will exceed 0.9 (matched-scale baseline pairs at ~0.7), and embedding-space negation surgery will fix at least 2x more negation failures than tuned negative prompting at matched off-target change; kill if negated pairs are well separated (under 0.8) or embedding surgery underperforms sampling fixes.
- fastest falsification: Embedding analysis is minutes; intervention comparison over ~1k prompts is a few hours on one GPU.
- fingerprint: text-encoder negation handling | embedding-level vs sampling-level intervention | negation success rate

### W13-P1-J-071 [audit_debunk]
**Prompt rewriting by users converges on a folk grammar that works for lawful reasons: quantifying which rewrite operations (reordering, splitting, weighting) causally change generation shows most folk tricks are placebo while a small set has large, consistent effects.**

- hypothesis: [HYPOTHESIS] Only rewrite operations that change the embedding geometry meaningfully (content-word placement, splitting compound clauses) causally affect outputs, while popular decorations (quality tags, emphasis punctuation) have effects indistinguishable from resampling noise on modern models.
- kill test: [EXPECTED RESULT] In seed-controlled paired tests, at least half of the ten most popular folk tricks will show effect sizes below resampling noise (paired distribution shift indistinguishable at n=500), while content-reordering operations show significant effects in 80%+ of prompt families; kill if most folk tricks show robust significant effects (folk wisdom vindicated).
- fastest falsification: Paired generation battery of ~10k images: about a day on one GPU.
- fingerprint: prompt rewrite operations | folk trick vs content operation | paired causal effect size


## distillation-fewstep-science (8 ideas)

### W13-P1-J-072 [characterization_law]
**Distillation eats the tails first: few-step students lose rare modes (uncommon classes, unusual compositions) long before average-quality metrics degrade, following a lawful tail-truncation order predictable from teacher mode mass.**

- hypothesis: [HYPOTHESIS] Distillation objectives weight learning by probability mass, so student coverage shrinks from the tails inward: mode-level recall falls in inverse order of teacher mode mass, with a measurable truncation frontier that advances as steps decrease.
- kill test: [EXPECTED RESULT] In class-conditional settings, rare-class generation recall will drop by 30%+ relative at 4 steps while common-class recall stays within 5%, and the recall-versus-mass curve will shift monotonically with step count; kill if losses are mass-uniform (rare and common classes degrade within 10% of each other).
- fastest falsification: Small class-conditional distillation grid: roughly 3-5 GPU-days on one GPU with public data and models.
- fingerprint: few-step students | sampling step budget | mass-stratified mode recall

### W13-P1-J-073 [characterization_law]
**Few-step students lose input sensitivity, not just diversity: the Jacobian of output with respect to conditioning collapses under distillation, predicting that distilled models are disproportionately worse for editing and control than for prompted generation.**

- hypothesis: [HYPOTHESIS] Compressing an iterative refinement into few steps forces the student toward locally flat input-output maps (small condition-Jacobian), so fine-grained condition changes (prompt tweaks, control-signal deltas) produce weaker, coarser output changes than the teacher's.
- kill test: [EXPECTED RESULT] Condition-perturbation response (output change per unit prompt-embedding change) will be at least 40% lower in 1-4 step students than teachers, and the response deficit will predict editing-benchmark degradation across models at rank correlation 0.5+; kill if response magnitudes are within 15% of teachers.
- fastest falsification: Perturbation-response measurement on public teacher-student pairs: a few hours on one GPU.
- fingerprint: teacher-student pairs | condition perturbation | output-response magnitude and alignment

### W13-P1-J-074 [characterization_law]
**Distillation concentrates memorization: few-step students reproduce the teacher's memorized items at equal or higher rates while losing non-memorized diversity, so the privacy-risk fraction of outputs increases through the very process meant to cheapen deployment.**

- hypothesis: [HYPOTHESIS] Memorized items are sharp high-mass attractors that distillation objectives preserve preferentially, while diffuse novel modes are pruned; the student's output distribution therefore over-represents memorized content relative to the teacher.
- kill test: [EXPECTED RESULT] For known-memorized prompts, student near-copy rates will match or exceed teacher rates (ratio 1.0+), while student output diversity on neutral prompts drops 20%+, raising the memorized fraction of output mass by at least 1.5x; kill if student extraction rates fall by 30%+ alongside diversity (uniform compression).
- fastest falsification: Teacher-student extraction comparison on known items: a few hours on one GPU; the planted replicate adds ~2 GPU-days.
- fingerprint: distillation pipeline | teacher-vs-student comparison | memorized-fraction change

### W13-P1-J-075 [characterization_law]
**Guidance baked into distilled weights freezes the alignment-diversity operating point: no inference-time knob recovers the diversity a guidance-distilled student gave up, proving the tradeoff became structural rather than parametric.**

- hypothesis: [HYPOTHESIS] Post-distillation, the diversity-alignment tradeoff is embedded in the learned map itself: sampling-time interventions (temperature-like noise scaling, early stopping, seed dithering) will fail to recover more than a small fraction of the teacher's accessible diversity range at matched alignment.
- kill test: [EXPECTED RESULT] The area of the alignment-diversity region reachable by knob sweeps on a guidance-distilled student will be under 30% of the teacher's reachable region; kill if any knob combination recovers 60%+ of the teacher's operating range.
- fastest falsification: Knob sweeps of ~20k generations across configurations: about a day on one GPU.
- fingerprint: guidance-distilled students | inference-knob sweep | reachable alignment-diversity region

### W13-P1-J-076 [constructive_capability]
**Distillation error concentrates in a measurable SNR band, so hybrid schedules that spend the few available steps non-uniformly (dense where teacher curvature is high) beat uniform few-step schedules at matched compute.**

- hypothesis: [HYPOTHESIS] The student's disagreement with its teacher is not uniform over noise levels but peaks where the teacher's trajectory curvature is high; allocating student steps by measured disagreement mass recovers a meaningful fraction of the distillation loss for free.
- kill test: [EXPECTED RESULT] Teacher-student disagreement profiles will show 50%+ of total disagreement mass concentrated in under 25% of the SNR range, and disagreement-weighted step placement will improve student quality by 10%+ relative at matched step count; kill if disagreement is flat (no band holds more than 35% of mass) or reallocation gains are under 3%.
- fastest falsification: Disagreement profiling plus schedule benchmark on public teacher-student pairs: about a day on one GPU.
- fingerprint: few-step schedule | disagreement-weighted step placement | student quality at matched steps

### W13-P1-J-077 [constructive_capability]
**Violation of the semigroup property (two 1-step jumps disagreeing with one 2-step jump) is an intrinsic inconsistency measure for few-step models that tracks their distillation quality without any reference images or teacher access.**

- hypothesis: [HYPOTHESIS] An ideal few-step model's jumps compose consistently (the flow-map semigroup property); real students violate it in proportion to how badly distillation compressed the trajectory, so composition error is a reference-free proxy of distillation loss.
- kill test: [EXPECTED RESULT] Across students of varying known quality (different recipes/budgets from the same teacher), mean composition error will rank-correlate with reference-based quality gaps at 0.6+; kill if correlation is under 0.3 (composition error measures something orthogonal to quality).
- fastest falsification: Composition-error computation is minutes per student; the student ladder is the cost, roughly 3-4 GPU-days at small scale.
- fingerprint: few-step student alone | jump composition test | composition error vs external quality

### W13-P1-J-078 [constructive_capability]
**Teacher-student representational alignment early in distillation predicts final student quality: CKA at matched noise levels after a small fraction of training forecasts the outcome, enabling early stopping of doomed distillation runs.**

- hypothesis: [HYPOTHESIS] Successful distillation proceeds by first aligning internal representations and then refining outputs; early representational alignment (CKA between teacher and student features at matched SNR) is therefore a leading indicator of final output quality.
- kill test: [EXPECTED RESULT] CKA measured at 10% of training will predict final quality across a grid of recipes with rank correlation 0.6+, beating early output-loss values as a predictor by a significant margin; kill if early CKA predicts no better than early loss (correlation advantage under 0.1).
- fastest falsification: A grid of ~10 small distillations with periodic CKA logging: roughly 5 GPU-days on one GPU.
- fingerprint: distillation training runs | early CKA signal | final-quality prediction correlation

### W13-P1-J-079 [characterization_law]
**One-step generators are qualitatively different objects from few-step ones: the 1-to-2 step transition shows a discontinuous jump in output-map smoothness and failure structure, while 2-to-8 steps vary smoothly, locating the real boundary of 'diffusion-like' behavior.**

- hypothesis: [HYPOTHESIS] With two or more steps the model retains an intermediate-correction mechanism (see noise, adjust) that a single-step map structurally lacks; measurable properties (input-Jacobian spectra, artifact taxonomy, OOD-prompt behavior) will show a discontinuity between 1 and 2 steps and smooth variation beyond.
- kill test: [EXPECTED RESULT] Across matched students, the 1-to-2 step gap in Jacobian-spectrum statistics and artifact-class distributions will exceed the 2-to-4 and 4-to-8 gaps by at least 2x; kill if all successive gaps are within 30% of each other (smooth family).
- fastest falsification: Using public multi-step student releases where available, the measurement suite is about a day on one GPU; training a controlled ladder adds ~4 GPU-days at small scale.
- fingerprint: step-count ladder | 1-vs-2 step transition | smoothness/artifact discontinuity metrics


## latent-space-vae-effects (8 ideas)

### W13-P1-J-080 [constructive_capability]
**Latent compression sets a hard fidelity floor for small structures: objects below a critical pixel size cannot be faithfully generated by 8x-downsampling latent models regardless of denoiser scale, and the decode(encode(x)) roundtrip bound cleanly attributes such failures to the VAE, not the denoiser.**

- hypothesis: [HYPOTHESIS] The VAE roundtrip decode(encode(x)) is an upper bound on achievable fidelity per structure size; measured roundtrip fidelity will show a critical size below which information is destroyed, and generation failures on small structures will track this bound rather than denoiser capacity.
- kill test: [EXPECTED RESULT] Roundtrip legibility/identity of structures below the critical size (estimated around 8-16 pixels for common 8x VAEs) will fall under 50% while generation failures on matched structures occur at rates within 15 points of the roundtrip bound across two denoiser scales; kill if bigger denoisers beat the roundtrip bound (impossible under the hypothesis) or failures are uncorrelated with roundtrip fidelity.
- fastest falsification: Roundtrip battery plus generation battery: a few hours on one GPU with public checkpoints.
- fingerprint: latent autoencoder | structure size | roundtrip-vs-generation fidelity gap

### W13-P1-J-081 [characterization_law]
**Latent space is perceptually non-uniform: equal latent distances correspond to wildly different perceptual changes across image regions and content types, distorting every latent-space loss, edit magnitude, and interpolation built on it.**

- hypothesis: [HYPOTHESIS] The VAE's compression objective allocates latent resolution by reconstruction difficulty, not perceptual salience, so the local latent-to-perceptual metric ratio varies by an order of magnitude across content (faces versus sky), making latent distances systematically misleading.
- kill test: [EXPECTED RESULT] The measured local metric ratio (perceptual change per unit latent change) will vary by at least 5x between high-salience and low-salience content regions, and latent-distance-based edit strength will misestimate perceptual edit magnitude by 2x+ for at least 30% of images; kill if metric ratios vary under 2x (space approximately uniform).
- fastest falsification: Perturbation-decode battery over ~2k images: a few hours on one GPU.
- fingerprint: VAE latent geometry | latent perturbation location/content | latent-to-perceptual metric ratio

### W13-P1-J-082 [characterization_law]
**VAE decoders hallucinate texture deterministically: the fake high-frequency detail added during decoding is a repeatable function of latent content (not random), meaning latent generators systematically sign their outputs with decoder-specific texture and cannot represent certain true textures at all.**

- hypothesis: [HYPOTHESIS] Decoder texture synthesis is deterministic given the latent: repeated decodes and near-duplicate latents produce near-identical fake texture, implying a fixed texture vocabulary that (a) fingerprints the decoder and (b) excludes textures outside its vocabulary from ever being generated faithfully.
- kill test: [EXPECTED RESULT] Texture patches from decodes of perturbed latents will show self-similarity far above real-texture baselines (feature-space similarity 2x+ the natural-variation baseline), and a held-out texture-classification probe will identify the decoder from output patches at 80%+ accuracy across 4 public VAEs; kill if decoder identification is near chance or texture varies like natural texture.
- fastest falsification: Perturb-decode ensembles plus probes across public VAEs: under a day on one GPU.
- fingerprint: VAE decoder | latent perturbation ensemble | texture determinism and vocabulary census

### W13-P1-J-083 [constructive_capability]
**Latent channels carry stable global roles (luma-like, chroma-like, detail-like) consistent across images, so channel-targeted interventions provide training-free global controls (exposure, palette, detail level) with predictable effects.**

- hypothesis: [HYPOTHESIS] Compression pressure plus image statistics push VAEs toward a decorrelated color-like basis: individual channels (or fixed linear combinations) will have consistent global functions across content, making channel arithmetic a reliable control surface.
- kill test: [EXPECTED RESULT] Fixed channel-space directions will produce the same nameable global effect (e.g., brightness, warmth) on 80%+ of diverse images with off-target structural change below a perceptual threshold, and these directions will transfer across images without per-image search; kill if effects are content-dependent (consistent on under 40%) or structurally destructive.
- fastest falsification: Channel-offset battery over ~1k images and two VAEs: a few hours on one GPU.
- fingerprint: latent channel structure | channel-direction offset | effect consistency and transfer

### W13-P1-J-084 [characterization_law]
**Dense prediction from latent-diffusion features inherits a measurable VAE ceiling: label information destroyed by encode-decode roundtrips bounds what any latent-space feature can support, explaining boundary-precision gaps versus pixel-space backbones.**

- hypothesis: [HYPOTHESIS] Whatever task information the VAE roundtrip destroys (thin-structure identity, precise boundary location) is unavailable to latent features in principle; the roundtrip label-consistency bound will predict the task-performance ceiling of latent-feature probes, especially at boundaries.
- kill test: [EXPECTED RESULT] Boundary-band label consistency after roundtrip (relabeling decoded images with a strong reference model) will fall 10%+ below interior consistency, and latent-feature probe errors will concentrate in the same boundary band with spatial correlation 0.5+ to the roundtrip loss map; kill if probe errors are uncorrelated with roundtrip information loss.
- fastest falsification: Roundtrip relabeling plus probe training on one public benchmark: about a day on one GPU.
- fingerprint: latent bottleneck | roundtrip label consistency | probe-error localization vs information-loss map

### W13-P1-J-085 [constructive_capability]
**Sampled latents sometimes leave the decoder-valid region, producing a distinct artifact family; a cheap latent-typicality projection at the final step removes these artifacts without retraining anything.**

- hypothesis: [HYPOTHESIS] The denoiser can terminate at latents outside the encoder's output distribution (where the decoder was never trained); artifact occurrences will coincide with measurable latent atypicality, and projecting final latents toward the encoder-output manifold will remove the artifact family with minimal content change.
- kill test: [EXPECTED RESULT] Artifact-flagged generations will show latent-typicality scores in the extreme tail (bottom decile) at 3x+ the base rate, and typicality projection will fix 60%+ of flagged cases with content change below an edit-magnitude threshold; kill if artifacts are uncorrelated with typicality (under 1.3x enrichment).
- fastest falsification: Typicality scoring plus projection over ~20k generations: under a day on one GPU.
- fingerprint: final sampled latents | latent-typicality projection | artifact-rate reduction

### W13-P1-J-086 [characterization_law]
**The shared-VAE ecosystem correlates errors across 'independent' models: generators built on the same public autoencoder share failure modes and texture signatures, so ensembling them recovers far less than ensemble theory predicts.**

- hypothesis: [HYPOTHESIS] The shared decoder imposes shared blind spots (texture vocabulary, small-structure floor, color quirks); error correlation between same-VAE model pairs will substantially exceed correlation between different-VAE pairs, and same-VAE ensembles will underperform predicted ensemble gains.
- kill test: [EXPECTED RESULT] On structure-fidelity and texture tasks, same-VAE model pairs will show error correlations at least 0.2 higher than different-VAE pairs, and same-VAE ensembling will realize under half the error-reduction predicted by independence; kill if correlation differences are under 0.05.
- fastest falsification: Error batteries across ~6 public models: about a day on one GPU.
- fingerprint: model ecosystem | shared vs distinct VAE | cross-model error correlation

### W13-P1-J-087 [constructive_capability]
**Decoder swapping is a causal attribution instrument: decoding one model's latents with another compatible decoder cleanly splits every output property (artifact, texture, color bias) into denoiser-caused versus decoder-caused, with percentage attributions.**

- hypothesis: [HYPOTHESIS] For VAEs trained on similar data with compatible latent conventions, cross-decoding is faithful enough that property changes under decoder swap measure the decoder's causal share of each output property, yielding a reusable attribution protocol.
- kill test: [EXPECTED RESULT] Decoder swaps will attribute at least 70% of texture-family signatures to the decoder and at least 70% of layout/content properties to the denoiser (double dissociation), with attribution stable (within 10 points) across image sets; kill if cross-decoding is too lossy to preserve content (making attribution meaningless) or attributions are unstable.
- fastest falsification: Swap battery over ~5k generations and 2-3 decoder pairs: a few hours on one GPU.
- fingerprint: denoiser-decoder stack | decoder swap | per-property attribution shares


## noise-schedule-frequency (8 ideas)

### W13-P1-J-088 [characterization_law]
**Coarse-to-fine generation is an artifact of Gaussian noise schedules, not an intrinsic property of diffusion: alternative corruption operators reorder which image structure is decided when, causing predictable trades between layout errors and texture errors.**

- hypothesis: [HYPOTHESIS] The generation order of spatial frequencies is fully determined by the corruption operator's frequency-versus-time SNR profile; corruptions that destroy low frequencies first will produce fine-to-coarse generation and correspondingly shifted error profiles (more layout errors, fewer texture errors).
- kill test: [EXPECTED RESULT] Models trained with low-frequency-first corruption will decide texture before layout in trajectory-swap probes (reversal of the standard commitment order in 70%+ of cases) and will show at least 20% relative more layout-inconsistency errors with correspondingly fewer texture errors; kill if generation order stays coarse-to-fine regardless of corruption.
- fastest falsification: Three small trainings plus probes at CIFAR scale: about 3-4 GPU-days on one GPU with public data.
- fingerprint: corruption operator | frequency-vs-time SNR profile | commitment order and error taxonomy

### W13-P1-J-089 [characterization_law]
**Diffusion models under-generate high-frequency power with a lawful spectral deficit: the gap between generated and real power spectra has a stable shape per model family, predicting which fine-structure content will systematically look 'smoothed'.**

- hypothesis: [HYPOTHESIS] Training dynamics and finite sampling systematically under-fit the highest frequency octaves; the relative spectral deficit curve (generated over real power versus frequency) is stable across content categories within a model and shifts predictably with sampling steps and model scale.
- kill test: [EXPECTED RESULT] The spectral deficit curve will be reproducible across disjoint content categories within a model (curve correlation 0.8+), with top-octave deficits of 10%+ that shrink monotonically with sampling steps; kill if deficits are content-idiosyncratic (correlation under 0.4) or absent at convergence.
- fastest falsification: Spectral analysis over ~50k generated plus matched real images: a few hours on one GPU.
- fingerprint: generated-image statistics | model/steps configuration | spectral deficit curve

### W13-P1-J-090 [characterization_law]
**Terminal-SNR mismatch produces a quantifiable brightness/mean-shift artifact: the residual signal at the schedule's terminal step leaks into every generation as a predictable global bias, computable in closed form from the schedule and verifiable across public models.**

- hypothesis: [HYPOTHESIS] The terminal residual acts as a fixed prior injected into all generations; its magnitude and direction (mean brightness, low-frequency bias) are computable from the schedule's terminal statistics and will predict measured generation biases model by model.
- kill test: [EXPECTED RESULT] Predicted mean-shift magnitudes from terminal-SNR values will match measured generation mean biases across 5+ public models with rank correlation 0.7+, and zero-terminal-SNR models will show biases below half the nonzero-terminal group's median; kill if predicted and measured biases are uncorrelated (under 0.3).
- fastest falsification: Config analysis plus ~10k generations per model: under a day on one GPU.
- fingerprint: noise schedule terminal behavior | terminal SNR value | predicted-vs-measured global bias

### W13-P1-J-091 [constructive_capability]
**Noise schedules should be resolution-corrected: the optimal schedule shifts lawfully with image resolution because a fixed noise level destroys different fractions of information at different scales, so a resolution-corrected schedule transfers hyperparameters across resolutions for free.**

- hypothesis: [HYPOTHESIS] The information destroyed by noise level sigma depends on the signal's spectral mass, which scales with resolution; equating destroyed-information fractions across resolutions yields a correction rule that keeps generation behavior (commitment order, quality) invariant, making schedule tuning transferable.
- kill test: [EXPECTED RESULT] Models trained with the corrected schedule at 2x resolution will match the reference resolution's commitment-order profile within measurement error and beat naive schedule reuse by 15%+ relative on quality metrics; kill if corrected and naive schedules perform within 3% (correction unnecessary) or correction fails to preserve behavior.
- fastest falsification: Four small trainings at two resolutions: about 4 GPU-days on one GPU with public data.
- fingerprint: noise schedule | resolution-corrected schedule rule | behavior invariance across resolutions

### W13-P1-J-092 [constructive_capability]
**Per-SNR validation loss exposes under-trained noise bands left by the training-time timestep-sampling distribution, and cheap targeted fine-tuning on those bands yields outsized quality gains compared to uniform continued training.**

- hypothesis: [HYPOTHESIS] The timestep distribution leaves fingerprints: noise bands undersampled during training will show elevated per-SNR validation loss, and reallocating a small fine-tuning budget to those bands will improve generation quality more than the same budget spent uniformly.
- kill test: [EXPECTED RESULT] Per-SNR loss profiles will identify bands with 15%+ excess loss in public checkpoints, and band-targeted fine-tuning will beat uniform fine-tuning at matched compute by 10%+ relative on quality metrics; kill if profiles are flat (under 5% variation) or targeted tuning gives no advantage.
- fastest falsification: Loss profiling is hours; the paired fine-tune comparison is roughly 2 GPU-days at small scale on one GPU.
- fingerprint: trained checkpoint | per-SNR loss audit and targeted fine-tune | quality gain at matched compute

### W13-P1-J-093 [constructive_capability]
**Optimal noise schedules are derivable from data power spectra: matching the schedule to the domain's spectral statistics (natural 1/f versus other spectra in specialized domains) beats natural-image-default schedules by a predictable margin in non-natural domains.**

- hypothesis: [HYPOTHESIS] The schedule's job is to spread information destruction evenly over time; given a domain's power spectrum this schedule is computable in closed form, and the mismatch between default and spectrum-derived schedules predicts the achievable improvement per domain.
- kill test: [EXPECTED RESULT] In domains whose spectra deviate strongly from 1/f, spectrum-derived schedules will improve quality metrics by 10%+ relative over defaults at matched compute, with the improvement rank-correlating (0.6+) with a computable spectral-mismatch index across domains; kill if improvements are under 3% everywhere or uncorrelated with the mismatch index.
- fastest falsification: Paired small trainings on ~3 domains: about 5-6 GPU-days total on one GPU with public data.
- fingerprint: noise schedule design | spectrum-derived schedule | quality gain vs spectral-mismatch index

### W13-P1-J-094 [characterization_law]
**The corruption operator determines representation content: models trained with blur-based versus noise-based corruption learn measurably different feature families (shape-biased versus texture-complete), making corruption choice a representation-learning design axis.**

- hypothesis: [HYPOTHESIS] Restoring from different corruptions requires different information: blur-corruption training (which preserves layout, destroys detail) will induce features stronger on shape/layout probes, while noise-corruption training induces more complete texture/appearance features, with consistent probe-profile differences at matched generation quality.
- kill test: [EXPECTED RESULT] At matched sample quality, blur-trained features will beat noise-trained features by 5+ points on shape-biased probes while losing 5+ points on texture-sensitive probes (a crossed double dissociation); kill if probe profiles differ by under 2 points everywhere.
- fastest falsification: Two small trainings plus probe batteries: about 3 GPU-days on one GPU.
- fingerprint: corruption operator family | blur vs noise corruption training | shape/texture probe double dissociation

### W13-P1-J-095 [constructive_capability]
**Remaining uncertainty during sampling is frequency-ordered, enabling a 'spectral progress bar': partial trajectories reveal exactly which frequency bands are already decided, supporting early quality prediction and band-selective compute allocation.**

- hypothesis: [HYPOTHESIS] At any trajectory point, low-frequency content is locked while high-frequency content remains undecided, with the moving boundary computable from the schedule; intermediate x0-predictions therefore contain final low-band content exactly, making band-resolved early readouts faithful.
- kill test: [EXPECTED RESULT] Band-limited agreement between intermediate x0-predictions and final images will exceed 90% for bands below the predicted boundary and fall under 50% above it, with the boundary tracking the schedule-derived prediction within half an octave; kill if band agreement does not separate cleanly (boundary undefined by 2+ octaves).
- fastest falsification: Trajectory recording plus band analysis over ~2k generations: a few hours on one GPU.
- fingerprint: partial sampling trajectory | schedule-derived band boundary | band-limited early-readout fidelity


## video-temporal-diffusion (9 ideas)

### W13-P1-J-096 [characterization_law]
**Video diffusion buys temporal smoothness by suppressing motion diversity: generated videos systematically under-disperse motion statistics relative to real footage, a lawful bias measurable with optical-flow distributions and traceable to temporal-consistency objectives.**

- hypothesis: [HYPOTHESIS] Temporal-attention and consistency losses penalize exactly the high-variance motion that real scenes contain, so generated flow-magnitude and flow-direction distributions will be compressed (lower variance, thinner tails) relative to content-matched real video by a stable factor.
- kill test: [EXPECTED RESULT] Generated video sets will show flow-magnitude distributions with at least 30% lower tail mass (95th-percentile motion) than content-matched real sets across 2+ public video models, and the compression factor will correlate with the models' temporal-consistency scores; kill if motion statistics match real footage within 10% or the compression-consistency link is absent.
- fastest falsification: Flow analysis over a few hundred generated and real clips: under a day on one GPU.
- fingerprint: video diffusion outputs | temporal-consistency optimization | motion-distribution compression

### W13-P1-J-097 [constructive_capability]
**Structured continuation probes measure intuitive physics in video generators as a graded capability profile: object permanence, gravity consistency, and collision plausibility form a reproducible difficulty hierarchy that model scale climbs in a fixed order.**

- hypothesis: [HYPOTHESIS] Physical regularities differ in the temporal range and relational complexity needed to enforce them, producing a stable difficulty ordering (permanence easiest, multi-object dynamics hardest); models will pass them in a consistent order as capability grows rather than uniformly improving.
- kill test: [EXPECTED RESULT] Across 3+ public video models of varying strength, pass rates on a continuation battery will show a consistent ordering (permanence > gravity direction > trajectory continuation > collision response) with rank agreement 0.7+ across models; kill if orderings are model-idiosyncratic (agreement under 0.3).
- fastest falsification: A ~500-stimulus battery across 3 models with automated scoring: about a day on one GPU plus API access where local weights are unavailable.
- fingerprint: video generators | physical-regularity class | continuation pass-rate hierarchy

### W13-P1-J-098 [characterization_law]
**Video generation commits appearance and layout within the first few frames and then propagates: a temporal commitment horizon exists after which conditioning changes can no longer alter scene identity, only motion, measurable by mid-generation condition swaps.**

- hypothesis: [HYPOTHESIS] Video diffusion resolves scene identity (appearance, layout) using early-frame content as an anchor and afterwards operates in a propagation regime; condition swaps after the commitment horizon will change motion continuation but not scene identity, with a sharp measurable boundary.
- kill test: [EXPECTED RESULT] Prompt swaps after the first 20% of frames will change scene-identity metrics in under 15% of generations while motion-description changes still take effect in 60%+, with the identity-change rate dropping steeply (within a 10%-of-clip window); kill if identity remains editable throughout (no horizon) or the boundary spans over 40% of the clip (gradual, no commitment structure).
- fastest falsification: Swap experiments at ~10 offsets x 200 prompts: about a day on one GPU with a public video model.
- fingerprint: video sampling trajectory | mid-generation condition swap | identity-vs-motion commitment curves

### W13-P1-J-099 [constructive_capability]
**Motion and appearance are separably stored in video diffusion internals: temporal-attention states carry motion while spatial pathways carry appearance, enabling training-free motion transfer by attention-state swapping between generations.**

- hypothesis: [HYPOTHESIS] The architectural split (spatial layers versus temporal layers) induces a functional split: swapping temporal-attention states between two generations will transplant motion onto the recipient's appearance with high fidelity, demonstrating separable internal codes.
- kill test: [EXPECTED RESULT] Temporal-state swaps will transfer motion (flow-pattern similarity to donor 0.6+) while preserving recipient appearance (identity metrics within 15% of no-swap baseline) in at least 50% of pairs; kill if swaps either fail to move motion (similarity under 0.3) or destroy appearance in most pairs.
- fastest falsification: Swap battery over ~200 generation pairs: a few hours on one GPU with a public video model.
- fingerprint: video model internals | temporal-attention state swap | motion-transfer vs appearance-preservation scores

### W13-P1-J-100 [characterization_law]
**Video models are interpolators before they are extrapolators: quality degrades sharply and asymmetrically when generation must continue beyond observed context versus fill between anchors, quantifying how far current models are from forward world modeling.**

- hypothesis: [HYPOTHESIS] Training distributions and objectives reward consistency with surrounding context, so constrained-on-both-sides generation is fundamentally easier: at matched content, extrapolation quality will fall off with horizon length much faster than interpolation quality falls with gap length.
- kill test: [EXPECTED RESULT] Matched-content comparisons will show extrapolation quality dropping at least 2x faster per frame of horizon than interpolation per frame of gap, with the asymmetry ratio stable across content classes; kill if the two degradation rates are within 30% (no meaningful asymmetry).
- fastest falsification: Paired tasks over ~300 clips: under a day on one GPU with public models and data.
- fingerprint: video generation modes | interpolation vs extrapolation constraint | degradation-rate asymmetry

### W13-P1-J-101 [constructive_capability]
**Video-diffusion features provide time-consistent correspondence that survives occlusion without any tracking supervision: memory-like matching emerges from generative video training, beating per-frame image-feature chaining exactly on occlusion-heavy tracks.**

- hypothesis: [HYPOTHESIS] To generate coherent video through occlusion events, video diffusion models must internally maintain object identity across gaps; their features will therefore support track-through-occlusion matching that per-frame image features cannot, without any tracking-specific training.
- kill test: [EXPECTED RESULT] On public point-tracking benchmarks stratified by occlusion, video-diffusion features with simple matching will beat image-feature chaining by 15+ points on occluded-point re-association while being within 5 points on never-occluded points; kill if the advantage on occluded points is under 5 points.
- fastest falsification: Feature-based tracking on a public benchmark subset: about a day on one GPU.
- fingerprint: video-diffusion features | occlusion stratum | track re-association accuracy vs chaining

### W13-P1-J-102 [characterization_law]
**Long-horizon autoregressive video generation collapses into periodic attractors: continuation loops with a period set by the model's temporal receptive field, so measuring collapse periodicity reverse-engineers the effective temporal memory of black-box video models.**

- hypothesis: [HYPOTHESIS] Once genuinely novel content exhausts, the conditioning window sees near-repeated states and the model enters a limit cycle; the cycle period will track the effective temporal context length, making periodicity a behavioral measurement of memory span.
- kill test: [EXPECTED RESULT] Detected repetition periods in long continuations will cluster near the models' context lengths (within 30%) across architectures with different windows, and doubling the context window will shift measured periods correspondingly; kill if periods are unrelated to context length (correlation under 0.3).
- fastest falsification: Long continuations plus autocorrelation analysis for 2-3 public models: about a day on one GPU.
- fingerprint: autoregressive continuation | temporal context length | repetition-period distribution

### W13-P1-J-103 [characterization_law]
**Camera motion and object motion are entangled in current video models: no internal direction moves the camera while freezing the scene, and the degree of entanglement is measurable, defining a concrete deficit that 3D-aware conditioning must close.**

- hypothesis: [HYPOTHESIS] Because 2D pixel motion confounds the two sources, video models represent total motion holistically: attempted interventions (prompting, latent steering) that request pure camera motion will produce correlated object motion, with an entanglement index far above what explicit-camera-conditioned models achieve.
- kill test: [EXPECTED RESULT] For camera-motion requests on unconditioned models, induced object-motion artifacts (non-rigid scene deformation measured by flow decomposition) will appear in 60%+ of generations, versus under 20% for camera-conditioned baselines, yielding an entanglement index separating the model families by 2x+; kill if unconditioned models achieve near-baseline separation (entanglement is already low).
- fastest falsification: Steering battery plus flow decomposition over ~300 generations: about a day on one GPU.
- fingerprint: video model motion representation | camera-motion intervention | ego/object motion entanglement index

### W13-P1-J-104 [characterization_law]
**Video models memorize clips at lower duplication thresholds than image models memorize images: temporal redundancy (many near-duplicate frames per clip) acts as built-in duplication, making video memorization lawfully easier and current image-derived privacy intuitions wrong for video.**

- hypothesis: [HYPOTHESIS] Each training clip effectively presents its content many times (across frames and overlapping windows), shifting the memorization dose-response left: video models will reproduce training clips at corpus-duplication levels far below the image-model threshold, with the shift predictable from within-clip redundancy statistics.
- kill test: [EXPECTED RESULT] In controlled small-scale trainings, the clip-duplication count needed for reliable near-copy generation will be at least 3x lower than the image-side threshold measured under matched protocol, and the shift will scale with frame-redundancy measures; kill if video and image thresholds are within 1.5x.
- fastest falsification: Paired small-scale trainings with planted duplicates: roughly 5-6 GPU-days total on one GPU with public datasets.
- fingerprint: video vs image diffusion training | planted clip duplication | cross-modality memorization threshold

