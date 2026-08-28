# Stage 1 — Cluster B: Massive Original Research Idea Catalog

**Agent:** Cloud Sub-Agent B (for Supervisor Windows7) · **Repo:** github.com/songkang688/idea
**Stage:** 1 (mass generation, NOT filtered) · **Total ideas:** 366 (B-0001 … B-0366)

**Scope:** Medical image segmentation · Medical vision foundation models · Smoke/fire/transparent/ambiguous segmentation · Domain adaptation & domain shift · Few-shot/zero-shot segmentation · Prompt learning · Weak/semi/self-supervised learning · Synthetic data · Annotation efficiency · Long-tail · Cross-domain transfer · Multimodal supervision for dense prediction.

**Quality contract per idea:** explicit failure mode of current methods, falsifiable core hypothesis, and a cheap "killer experiment" that could refute the idea quickly. No fabricated papers or measured results are cited anywhere; named methods (SAM, nnU-Net, DINO, CLIP, etc.) are referenced only as well-known method families.

## Section map

| Section | IDs | Cluster tag |
|---|---|---|
| 1. Medical Image Segmentation (core) | B-0001–B-0030 | MedSeg |
| 2. Medical Vision Foundation Models | B-0031–B-0060 | MedFM |
| 3. Smoke/Fire/Transparent/Ambiguous Segmentation | B-0061–B-0090 | AmbigSeg |
| 4. Domain Adaptation & Domain Shift | B-0091–B-0120 | DomainAdapt |
| 5. Few-shot / Zero-shot Segmentation | B-0121–B-0150 | FewZero |
| 6. Prompt Learning | B-0151–B-0180 | PromptLearn |
| 7. Weak / Semi / Self-supervised Learning | B-0181–B-0210 | WSSL |
| 8. Synthetic Data | B-0211–B-0240 | Synth |
| 9. Annotation Efficiency | B-0241–B-0270 | AnnotEff |
| 10. Long-tail Recognition & Segmentation | B-0271–B-0300 | LongTail |
| 11. Cross-domain Transfer | B-0301–B-0330 | CrossDom |
| 12. Multimodal Supervision for Dense Prediction | B-0331–B-0360 | MultiSup |
| 13. Cross-cutting Wildcards | B-0361–B-0366 | (mixed) |

---
## Section 1 — Medical Image Segmentation (core) [B-0001–B-0030]

### B-0001
- **One-sentence idea:** Condition segmentation networks directly on physical voxel spacing via FiLM-style metadata injection instead of resampling every volume to a canonical grid.
- **Problem:** Current pipelines (nnU-Net-style) resample to a fixed spacing, destroying information in high-res axes and interpolating artifacts into low-res axes; performance drops sharply on spacings unseen at training time.
- **Core Hypothesis:** A single network that receives per-axis physical spacing as a conditioning signal will outperform resample-to-canonical pipelines on held-out spacings, because it can learn spacing-dependent receptive-field usage rather than relying on interpolated voxels.
- **Why Important:** Slice thickness and in-plane resolution vary enormously across hospitals; spacing shift is one of the largest silent generalization failures in deployment.
- **Why Possibly Novel:** Spacing is almost universally "normalized away" as preprocessing; treating it as a first-class model input with learned modulation, rather than a nuisance, is rarely explored systematically.
- **Minimal Experiment:** Train one abdominal CT model on 3 native spacings with/without spacing-FiLM; evaluate on 2 held-out spacings (real thick-slice scans, not synthetic downsampling). Falsified if conditioning gives no gain over resampling.
- **Main Risk:** Spacing effects may be absorbable by heavy resampling augmentation, making conditioning redundant.
- **Cluster:** MedSeg

### B-0002
- **One-sentence idea:** Replace mask prediction for vessels/airways with prediction of a centerline flow field (direction + radius) from which the mask is reconstructed, to make connectivity the primary learned quantity.
- **Problem:** Overlap-loss-trained networks break tubular structures at low-contrast segments; a 1-voxel gap barely changes Dice but destroys downstream graph analysis.
- **Core Hypothesis:** Networks that regress a locally smooth vector field along vessels will produce fewer topological breaks than mask classifiers at matched voxel accuracy, because the output parameterization makes discontinuities expensive.
- **Why Important:** Vascular/airway trees feed surgery planning and CFD; connectivity, not Dice, is the clinically binding metric.
- **Why Possibly Novel:** Flow-field output parameterizations exist for instance segmentation of cells (Cellpose-style) but are not established as a topology mechanism for 3D tubular trees with radius recovery.
- **Minimal Experiment:** On one public airway or coronary dataset, train mask baseline vs. flow-field head on the same backbone; compare Betti-error/#broken-branches at matched Dice. Falsified if breaks are unchanged.
- **Main Risk:** Reconstruction from noisy fields may introduce its own failure modes (hallucinated bridges).
- **Cluster:** MedSeg

### B-0003
- **One-sentence idea:** Train segmentation models to predict the full inter-rater mask distribution and evaluate them against a fresh, unseen rater rather than a majority-vote consensus.
- **Problem:** Single-GT training treats rater disagreement as noise; models trained on consensus systematically over-smooth ambiguous boundaries and cannot express legitimate ambiguity.
- **Core Hypothesis:** A model trained to match the rater distribution (e.g., via a stochastic decoder scored by generalized energy distance) will match a held-out human rater better than any consensus-trained model, measurably in rater-vs-model agreement statistics.
- **Why Important:** Regulatory and clinical acceptance depends on being "within inter-rater variability"; today's evaluation cannot even measure that claim properly.
- **Why Possibly Novel:** Probabilistic segmentation exists, but evaluation against a strictly held-out rater as the primary success criterion (not GED on the same raters) is rarely done and changes conclusions.
- **Minimal Experiment:** Use any multi-rater dataset (e.g., lung nodules with 4 raters): train on 3 raters, test agreement with the 4th; compare consensus-trained vs. distribution-trained. Falsified if consensus training matches the held-out rater equally well.
- **Main Risk:** Few public datasets have enough raters for statistically meaningful held-out-rater evaluation.
- **Cluster:** MedSeg

### B-0004
- **One-sentence idea:** Optimize segmentation networks directly for downstream biomarker error (volume, diameter, ejection fraction) with the biomarker computed differentiably from the soft mask.
- **Problem:** Dice-optimal models can carry systematic volumetric bias (small structures inflated, large deflated), which corrupts longitudinal biomarker trends even when Dice looks excellent.
- **Core Hypothesis:** Adding a differentiable biomarker-error term produces models with substantially lower biomarker bias at negligible Dice cost, and biomarker bias is largely independent of Dice above a threshold.
- **Why Important:** Clinicians consume measurements, not masks; a 5% consistent volume bias can flip treatment-response decisions.
- **Why Possibly Novel:** The claim that Dice and biomarker fidelity decouple, and that biomarker terms fix it, is a falsifiable, rarely tested proposition; most work stops at overlap metrics.
- **Minimal Experiment:** Take a trained cardiac or tumor model; fine-tune 1 epoch with a soft-volume error term; measure volume bias and Bland-Altman limits on held-out data. Cheap and decisive.
- **Main Risk:** Biomarker terms may trade bias for variance, worsening per-case reliability.
- **Cluster:** MedSeg

### B-0005
- **One-sentence idea:** Derive physically correct soft boundary labels from partial-volume modeling (fraction of tissue per voxel) instead of hard binary labels at object borders.
- **Problem:** Binary boundary labels are physically wrong wherever a voxel straddles a tissue interface; networks are forced to fit label noise that is structured, not random.
- **Core Hypothesis:** Training on partial-volume-derived soft targets at boundary voxels improves sub-voxel surface metrics (ASSD, surface Dice at tight tolerances) without hurting volumetric Dice.
- **Why Important:** Sub-voxel surface accuracy drives radiotherapy margins and small-structure volumetry, where every boundary voxel is a large relative error.
- **Why Possibly Novel:** Label smoothing is common but uniform; boundary softening derived from an explicit partial-volume forward model (using spacing and PSF) is a mechanism, not a heuristic.
- **Minimal Experiment:** Generate soft labels by rasterizing existing high-res contours at acquisition resolution with a PSF model; retrain same architecture; compare surface Dice@1mm. Falsified if no surface gain.
- **Main Risk:** Contour GT itself may be too imprecise for the PSF model to add signal.
- **Cluster:** MedSeg

### B-0006
- **One-sentence idea:** Quantify and eliminate sliding-window seam inconsistency by adding a shifted-crop prediction-consistency loss during training.
- **Problem:** Patch-based 3D inference produces predictions that depend on arbitrary patch placement; Gaussian blending hides but does not remove disagreement at seams, causing unstable lesion counts between runs.
- **Core Hypothesis:** Networks trained with explicit consistency between overlapping shifted crops will show near-zero placement variance at inference and modest whole-volume accuracy gains, indicating that placement variance is learned instability rather than irreducible.
- **Why Important:** Placement-dependent outputs undermine reproducibility claims in clinical software; nobody currently reports this variance.
- **Why Possibly Novel:** Consistency regularization is used across augmentations, but crop-placement consistency as a measured deployment failure with a targeted fix is largely undocumented.
- **Minimal Experiment:** For 3 public models, re-run inference with 8 shifted grids and report per-case Dice variance and lesion-count variance; then retrain one model with shift-consistency loss. Falsified if variance is already negligible.
- **Main Risk:** The variance may be small for organs and only matter for tiny lesions, narrowing the contribution.
- **Cluster:** MedSeg

### B-0007
- **One-sentence idea:** Replace naive left-right flip augmentation with laterality-aware flipping that swaps paired labels, and audit how much silent damage naive flipping causes.
- **Problem:** Flip augmentation is default in most pipelines, but for laterality-labeled structures (left/right kidney, hippocampus) naive flipping teaches the network anatomically false statistics or is disabled entirely, losing a strong augmentation.
- **Core Hypothesis:** Label-swapping flips recover the full augmentation benefit while eliminating laterality confusions, and naive flipping measurably increases left/right confusion errors in low-data regimes.
- **Why Important:** Laterality errors are among the most consequential clinical mistakes (wrong-side reporting), and the fix is nearly free.
- **Why Possibly Novel:** This is a widely ignored correctness bug in standard pipelines; a careful audit plus fix would be a small but influential empirical contribution.
- **Minimal Experiment:** Train hippocampus/kidney segmentation at 10/50/100% data with (a) no flip, (b) naive flip, (c) swap-flip; count laterality confusions. One GPU-week total.
- **Main Risk:** Modern high-capacity models may already resolve laterality from context, nullifying the effect at scale.
- **Cluster:** MedSeg

### B-0008
- **One-sentence idea:** Feed acquisition metadata (reconstruction kernel, kVp, MRI sequence parameters) into the segmentation network as conditioning tokens instead of discarding DICOM headers.
- **Problem:** Networks must infer acquisition physics from pixels alone; cross-protocol degradation is treated as "domain shift" although the causal variable is recorded in the header for free.
- **Core Hypothesis:** Metadata conditioning recovers a large fraction of cross-protocol performance drop without any target-domain images, because the model can index protocol-specific appearance priors explicitly.
- **Why Important:** Protocol diversity is the dominant deployment shift in radiology; using free metadata is cheaper than any adaptation method.
- **Why Possibly Novel:** Metadata is used for stratification/harmonization offline, but rarely as an in-network conditioning signal with controlled ablations against image-only inference.
- **Minimal Experiment:** Train on multi-kernel CT with kernel token vs. without; test on held-out kernel with correct vs. shuffled tokens (shuffling must hurt if the mechanism is real). Falsified if shuffled ≈ correct.
- **Main Risk:** Metadata may be too coarse a proxy for actual appearance variation, or headers unreliable in the wild.
- **Cluster:** MedSeg

### B-0009
- **One-sentence idea:** Use an implicit (coordinate-based) decoder queried at physical world coordinates so one model trains on and predicts at arbitrary anisotropic resolutions without resampling.
- **Problem:** Grid decoders tie output resolution to input grid; anisotropic clinical volumes force lossy resampling, and inter-slice interpolation invents boundaries where no data exists.
- **Core Hypothesis:** An INR-style decoder over a CNN/transformer feature volume, trained across mixed native spacings, will beat resampling pipelines specifically on through-plane surface accuracy, with the gap growing with anisotropy.
- **Why Important:** Thick-slice imaging is the norm outside research hospitals; through-plane behavior is where current tools fail hardest.
- **Why Possibly Novel:** INR decoders exist for super-resolution and shape completion, but "train once across heterogeneous native spacings, evaluate through-plane surfaces" is an untested specific claim.
- **Minimal Experiment:** Mixed-spacing training on one organ; compare through-plane surface Dice vs. isotropic-resample baseline on thick-slice test scans with thin-slice GT. Falsified if equal.
- **Main Risk:** INR decoders may underfit fine in-plane detail, trading one failure for another.
- **Cluster:** MedSeg

### B-0010
- **One-sentence idea:** Train a segmentation quality-control head that predicts per-case Dice/surface error without ground truth, supervised on the model's own historical errors, to gate deployment.
- **Problem:** Deployed models fail silently; softmax confidence is miscalibrated under shift and correlates poorly with case-level quality, so failures reach clinicians unflagged.
- **Core Hypothesis:** A separately trained error-predictor using intermediate features + prediction geometry estimates case-level Dice with enough fidelity (rank correlation) to catch the worst decile of cases, transferring across sites better than confidence baselines.
- **Why Important:** Automatic QC is the single biggest blocker for autonomous deployment of segmentation in clinics.
- **Why Possibly Novel:** Reverse-testing and confidence baselines exist; a systematic study of what QC signals survive cross-site shift, with a deployment-gating protocol, does not.
- **Minimal Experiment:** Train QC head on site A errors, evaluate worst-decile recall on site B for an existing public model. Falsified if it cannot beat entropy-based ranking.
- **Main Risk:** QC heads may inherit the same blind spots as the segmenter (correlated failures).
- **Cluster:** MedSeg

### B-0011
- **One-sentence idea:** Build a physics-based metal artifact simulator (beam hardening, photon starvation on inserted implant shapes) as targeted augmentation for CT segmentation around implants.
- **Problem:** Models collapse near hip/dental implants; generic corruption augmentation (noise, blur) does not resemble streak artifacts, and paired clean/artifact clinical data is essentially unobtainable.
- **Core Hypothesis:** Physically simulated artifacts transfer to real implant cases far better than generic corruptions, and the gain correlates with simulator physical fidelity (a dose-response relationship, which is falsifiable).
- **Why Important:** Implant patients are common in the elderly population that dominates imaging, and are silently excluded from most benchmark performance claims.
- **Why Possibly Novel:** Artifact simulation exists for artifact-reduction research; using it as a controlled robustness-training variable for segmentation, with fidelity ablations, is unexplored.
- **Minimal Experiment:** Insert virtual implants into public CT, forward-project/reconstruct to create artifacts, retrain, evaluate on a small real implant test set annotated for this purpose (~30 cases). Falsified if generic corruptions match.
- **Main Risk:** Simulator-real gap in artifact texture may cap transfer.
- **Cluster:** MedSeg

### B-0012
- **One-sentence idea:** Train one backbone across datasets with contradictory labeling protocols by attaching per-dataset "protocol heads" that model each dataset's definition (e.g., liver ± vessels) explicitly.
- **Problem:** Naively pooling datasets with conflicting label conventions injects contradiction into training; current practice either drops datasets or accepts the noise, and "universal" models silently average over incompatible definitions.
- **Core Hypothesis:** Protocol-conditioned heads over a shared representation outperform both per-dataset models and naive pooling, and the learned protocol embeddings will cluster by annotation convention rather than by scanner.
- **Why Important:** The field is moving to multi-dataset "universal" segmentation; protocol contradiction is its unaddressed confounder.
- **Why Possibly Novel:** Label-space heterogeneity is acknowledged, but modeling annotation protocol as an explicit conditioning variable with testable embedding structure is new territory.
- **Minimal Experiment:** Pick two public datasets with known definitional conflict for the same organ; train pooled vs. protocol-head models; evaluate on each dataset's own convention. Falsified if pooling matches.
- **Main Risk:** Insufficient per-protocol data to fit heads; protocol differences may be too subtle to matter.
- **Cluster:** MedSeg

### B-0013
- **One-sentence idea:** Segment longitudinal change directly from image pairs (change mask as output) instead of segmenting each timepoint and subtracting after registration.
- **Problem:** Segment-then-register pipelines compound two error sources; subtraction of independently noisy masks yields spurious "growth" on stable patients, poisoning response assessment.
- **Core Hypothesis:** A pairwise network trained to output change regions will show near-zero false change on test-retest (same-day repeat) scans, where the pipeline approach shows substantial false change.
- **Why Important:** Longitudinal decisions (progression vs. stable) are the highest-stakes use of segmentation in oncology and neurology.
- **Why Possibly Novel:** Change detection is standard in remote sensing but rarely formulated end-to-end for medical volumes with test-retest as the falsifying benchmark.
- **Minimal Experiment:** Use any test-retest dataset (e.g., repeat brain MRI): compare false-change volume of pipeline vs. pairwise model trained with synthetic longitudinal pairs. Falsified if pipeline is already clean.
- **Main Risk:** Synthetic change used for training may not cover real growth patterns.
- **Cluster:** MedSeg

### B-0014
- **One-sentence idea:** Exploit unlabeled test-retest repeat scans as a free training signal by penalizing prediction disagreement between same-patient repeats.
- **Problem:** Segmentation reproducibility (scan-rescan variability) is rarely optimized or even measured; models optimized on single scans have unknown and often poor test-retest stability, limiting biomarker use.
- **Core Hypothesis:** Adding a repeat-consistency loss on unlabeled repeat pairs reduces scan-rescan volume variability substantially without reducing accuracy, because variability is dominated by model sensitivity to acquisition noise, which is learnable.
- **Why Important:** Biomarker qualification (FDA/EMA) hinges on repeatability coefficients, not Dice.
- **Why Possibly Novel:** Repeat scans are abundant in trials but essentially unused as a supervision signal for segmentation stability.
- **Minimal Experiment:** Fine-tune an existing model with consistency on public repeat-scan data; report repeatability coefficient before/after and accuracy on labeled test. Falsified if variability is unchanged or accuracy drops.
- **Main Risk:** Consistency may be achieved by degenerate over-smoothing (must monitor accuracy).
- **Cluster:** MedSeg

### B-0015
- **One-sentence idea:** Learn an end-to-end differentiable zoom policy that selects where to run high-resolution segmentation for tiny structures (optic chiasm, cranial nerves) instead of fixed two-stage cropping.
- **Problem:** Tiny structures vanish at the downsampled resolution most 3D networks require; hand-tuned cascade pipelines use fixed ROIs that fail on anatomical variants and cannot be trained jointly.
- **Core Hypothesis:** A jointly trained soft-attention zoom (differentiable cropping) recovers small-structure recall on anatomical variants where fixed cascades fail, because localization errors can be corrected by gradient feedback from the segmentation loss.
- **Why Important:** Small organs-at-risk dominate radiotherapy planning failures; variants are exactly where automation must not fail.
- **Why Possibly Novel:** Differentiable cropping exists in 2D vision; a 3D medical variant evaluated specifically on variant-anatomy stress cases is a concrete gap.
- **Minimal Experiment:** Compare fixed cascade vs. differentiable zoom on head-and-neck OARs, with a curated variant-anatomy test subset. Falsified if fixed ROIs never miss.
- **Main Risk:** Memory cost of joint training; variants may be too rare in training data for the policy to learn them.
- **Cluster:** MedSeg

### B-0016
- **One-sentence idea:** Output an explicit third "uncertain band" class calibrated to inter-rater variability so downstream users review only the band, not the whole mask.
- **Problem:** Binary masks force decisions in regions where human experts genuinely disagree; clinicians must review entire contours because they cannot see where the model is guessing.
- **Core Hypothesis:** A band-producing model can be calibrated such that a target fraction (e.g., 90%) of true boundary errors fall inside a band occupying a small fraction of the surface, dramatically cutting review effort — and this coverage transfers across sites.
- **Why Important:** Human review time, not model accuracy, is the current bottleneck in contouring workflows.
- **Why Possibly Novel:** Uncertainty maps exist, but formulating and validating a coverage-vs-review-area operating curve as the primary deliverable is a workflow-grounded reframing.
- **Minimal Experiment:** Post-hoc: derive bands from ensemble variance on an existing model; measure error coverage vs. band area on multi-rater data; check cross-site coverage stability. No training needed for the falsification.
- **Main Risk:** Coverage calibration may not survive domain shift, which is where it is most needed.
- **Cluster:** MedSeg

### B-0017
- **One-sentence idea:** Replace fixed 0.5 thresholding of soft masks with a decision-theoretic per-case threshold chosen to maximize expected Dice/minimize expected volume error under the model's own predictive distribution.
- **Problem:** Argmax/0.5 thresholding is provably suboptimal for Dice and induces size-dependent volume bias (small objects systematically shrunken), yet is the universal default.
- **Core Hypothesis:** Expected-metric decision rules computed from the softmax field improve small-structure Dice and remove most size-dependent volume bias at zero training cost, with gains largest for small/low-confidence structures.
- **Why Important:** A free, retraining-free improvement applicable to every deployed model is maximal impact per unit effort.
- **Why Possibly Novel:** Decision-theoretic post-processing is known in theory; a systematic empirical demonstration across organs/sizes with a practical estimator would fill a real gap between theory and practice.
- **Minimal Experiment:** Apply expected-Dice thresholding to 3 existing public model outputs; stratify gains by structure size. A weekend of compute; falsified if gains vanish outside toy settings.
- **Main Risk:** Requires reasonably calibrated probabilities; badly calibrated models may not benefit without recalibration.
- **Cluster:** MedSeg

### B-0018
- **One-sentence idea:** For airway/vessel trees, deliberately oversegment with a high-recall network, then prune with a learned graph classifier operating on branch-level features.
- **Problem:** Single-shot networks balance leakage vs. omission pixel-wise; they cannot reason at branch level, so they both leak into parenchyma and drop distal branches — errors that are trivially separable in graph space.
- **Core Hypothesis:** Recall-tuned proposal + graph pruning strictly dominates the single-network operating curve on tree-length-detected vs. leakage-volume axes, because branch-level features (length, radius profile, direction coherence) separate true branches from leaks better than voxel evidence.
- **Why Important:** Distal airway/vessel quantification is the clinically informative part (e.g., in COPD), and is exactly what current methods drop.
- **Why Possibly Novel:** Two-stage propose-and-prune is standard in detection but rarely instantiated with explicit graph-topological features for 3D trees with a falsifiable dominance claim.
- **Minimal Experiment:** On a public airway benchmark, tune baseline to high recall, extract branch graph, train a small GBM/GNN pruner; plot both operating curves. Falsified if curves cross.
- **Main Risk:** Proposal stage may miss branches unrecoverably, capping the ceiling.
- **Cluster:** MedSeg

### B-0019
- **One-sentence idea:** Test whether topological loss benefits survive being computed on 4×–8× downsampled probability maps, making persistent-homology training affordable for 3D.
- **Problem:** Topology-aware losses are near-unusable in 3D due to computational cost, so practitioners skip them; whether topology must be enforced at full resolution is an untested assumption.
- **Core Hypothesis:** Most topological errors (merges, splits, holes) are visible at coarse scale, so coarse-scale topological loss recovers the majority of the topology benefit at a small fraction of the cost — a quantifiable cost/benefit curve.
- **Why Important:** If true, topology supervision becomes practical for every 3D pipeline overnight.
- **Why Possibly Novel:** The scale-dependence of topological supervision has not been characterized; this is a cheap, decisive empirical question nobody has answered.
- **Minimal Experiment:** Train with PH loss at full/2×/4×/8× downsampling on a 2D→small-3D benchmark; plot Betti error vs. compute. Falsified if benefits vanish below full resolution.
- **Main Risk:** Fine-scale topology errors (thin bridges) may be exactly the ones that matter and the ones lost at coarse scale.
- **Cluster:** MedSeg

### B-0020
- **One-sentence idea:** Constrain organ segmentation outputs to a learned discrete codebook of plausible shapes (VQ shape prior) so the network cannot emit anatomically impossible masks.
- **Problem:** Networks produce disconnected fragments, holes, and impossible shapes under shift; post-hoc largest-component heuristics are crude and fail for naturally multi-part structures.
- **Core Hypothesis:** Decoding through a vector-quantized shape latent (trained on masks only, which are abundant) reduces the anatomically-implausible-output rate to near zero under domain shift while matching baseline Dice in-domain.
- **Why Important:** Implausible outputs destroy clinician trust disproportionately; guaranteed plausibility is a qualitatively different product claim.
- **Why Possibly Novel:** Shape priors are classic, but a quantized shape codebook as a hard bottleneck with an implausibility-rate metric under deliberate shift stress-testing is a fresh, falsifiable packaging.
- **Minimal Experiment:** Train mask-VQ on public organ masks; bolt decoder onto existing backbone; count implausible outputs (automated rules: components, holes, size bounds) on corrupted/OOD inputs vs. baseline. Falsified if implausibility persists or in-domain Dice drops meaningfully.
- **Main Risk:** Codebook may fail on genuine pathology-induced shape outliers — precisely the important cases.
- **Cluster:** MedSeg

### B-0021
- **One-sentence idea:** Segment directly from undersampled k-space (jointly with implicit reconstruction) instead of segmenting DL-reconstructed images, to avoid committing to reconstruction errors.
- **Problem:** Accelerated MRI reconstructions hallucinate or smooth exactly the fine structures segmentation needs; the two-stage pipeline optimizes image appearance, not downstream mask fidelity.
- **Core Hypothesis:** At high acceleration factors, joint k-space-to-mask training beats segmenting state-of-the-art reconstructions, with the gap growing with acceleration — because the network can preserve task-relevant frequency content that recon losses discard.
- **Why Important:** Determines whether "recon then analyze" is the right architecture for accelerated MRI, a foundational pipeline question.
- **Why Possibly Novel:** Joint recon-seg has been touched, but a clean acceleration-sweep with matched backbones and a "gap grows with acceleration" prediction is a crisp uncontested claim to test.
- **Minimal Experiment:** fastMRI knee/brain with public masks: sweep 4×/8×/16×, two-stage vs. joint. Falsified if the gap is flat or negative.
- **Main Risk:** Requires raw k-space with segmentation labels — limited public overlap.
- **Cluster:** MedSeg

### B-0022
- **One-sentence idea:** Give MRI segmentation networks per-scan self-calibration tokens that predict intensity landmarks (CSF/GM/WM modes) and normalize features internally, replacing offline histogram standardization.
- **Problem:** MRI intensities are non-quantitative; offline histogram matching breaks on pathology (lesions shift histograms) and on unseen protocols, and errors propagate irreversibly into the network.
- **Core Hypothesis:** Learning normalization inside the network, anchored on predicted anatomical intensity landmarks, is more robust to pathology-distorted histograms than any fixed preprocessing, measurable as smaller cross-protocol drop on lesion-heavy cases.
- **Why Important:** Intensity nonstandardization is the root cause of a large share of MRI generalization failures.
- **Why Possibly Novel:** Learnable normalization exists generically; anchoring it to anatomically meaningful predicted landmarks (interpretable + auditable) is a specific new mechanism.
- **Minimal Experiment:** Train on protocol A, test on protocol B, stratified by lesion load: fixed standardization vs. landmark tokens. Falsified if fixed preprocessing matches on high-lesion cases.
- **Main Risk:** Landmark prediction itself may fail under the same shifts it is meant to fix (circularity).
- **Cluster:** MedSeg

### B-0023
- **One-sentence idea:** Replace foreground-oversampled patch training with dual-stream training (whole-volume low-res context + local high-res patch) to fix false positives far from the target organ.
- **Problem:** Foreground oversampling — used everywhere to fight class imbalance — starves the model of distal negative context, producing absurd false positives (kidney predicted in shoulder) that patch-level metrics never reveal.
- **Core Hypothesis:** Models trained with a global-context stream will show an order-of-magnitude fewer distal false positives at equal organ Dice, and the distal-FP rate is a hidden variable explaining much cross-dataset variance in reported performance.
- **Why Important:** Distal FPs are the most embarrassing and trust-destroying deployment failures, and current benchmarks are blind to them.
- **Why Possibly Novel:** The diagnosis (sampling-induced context starvation) and a distal-FP metric are both unarticulated in the literature.
- **Minimal Experiment:** Evaluate 3 public patch-trained models on whole-body scans; quantify distal FPs; retrain one with context stream. Falsified if distal FPs are already rare.
- **Main Risk:** Whole-body data may be needed at training time, which some datasets lack.
- **Cluster:** MedSeg

### B-0024
- **One-sentence idea:** Train multiple-lesion segmentation with a lesion-instance detection objective (per-lesion F1) alongside voxel loss, because semantic Dice hides missed small lesions.
- **Problem:** In multi-lesion diseases (MS, metastases), one large lesion dominates Dice; models can miss half the small lesions with negligible Dice penalty, corrupting lesion counts that drive diagnosis.
- **Core Hypothesis:** Directly optimizing a differentiable surrogate of lesion-level F1 (blob-matching-based) shifts models toward small-lesion recall with minimal Dice loss, and the Dice-vs-lesion-F1 tradeoff curve is steep (i.e., large F1 gains are cheap).
- **Why Important:** New-lesion counts are the primary endpoint in MS trials; the metric-objective mismatch has direct trial-outcome consequences.
- **Why Possibly Novel:** blob loss-style ideas exist; mapping the full tradeoff curve and tying it to counting endpoints as the falsifiable claim is a sharper contribution.
- **Minimal Experiment:** Retrain a public MS-lesion model with instance-weighted loss sweeps; plot Dice vs. lesion-F1 frontier. Falsified if the frontier is flat.
- **Main Risk:** Instance surrogates may be unstable for touching/confluent lesions.
- **Cluster:** MedSeg

### B-0025
- **One-sentence idea:** Enforce cyclic temporal consistency across the cardiac cycle in cine MRI segmentation using unlabeled frames, with labeled end-diastole/end-systole only.
- **Problem:** Cine segmentation is trained on 2 labeled phases; predictions on intermediate frames jitter non-physiologically, and derived ejection-fraction curves are noisy, but temporal labels are prohibitively expensive.
- **Core Hypothesis:** A cyclic-consistency loss (segmentation must return to itself over one cycle, and volumes must vary smoothly) reduces EF estimation error and frame-to-frame jitter without any new labels.
- **Why Important:** EF is among the most-used measurements in medicine; frame jitter directly inflates its variance.
- **Why Possibly Novel:** Temporal consistency is common in video; exploiting cardiac cyclicity specifically (a hard physiological constraint, not generic smoothness) is a domain-structured version with a clear metric (EF error).
- **Minimal Experiment:** Public cine dataset: add cycle-consistency to a per-frame baseline; measure EF error vs. per-frame baseline and temporal-smoothing post-hoc. Falsified if post-hoc smoothing matches.
- **Main Risk:** Arrhythmic patients violate cyclicity — must detect and exempt them.
- **Cluster:** MedSeg

### B-0026
- **One-sentence idea:** Jointly predict per-slice motion-corruption scores and use them to reweight inter-slice feature fusion for fetal/neonatal MRI segmentation.
- **Problem:** Fetal MRI stacks contain unpredictable motion-ruined slices; networks average corrupted and clean slices indiscriminately, and slice-outlier rejection is currently a separate brittle preprocessing step.
- **Core Hypothesis:** Learning corruption scores end-to-end (self-supervised via synthetic slice motion) and gating fusion on them beats both no-gating and external outlier rejection, because the gating can be feature-level and partial rather than binary.
- **Why Important:** Fetal imaging is the fastest-growing MRI application with the worst motion problem; robust automation is blocked on exactly this.
- **Why Possibly Novel:** Outlier rejection exists in reconstruction literature; integrating it as a differentiable gating mechanism inside segmentation is a concrete architectural gap.
- **Minimal Experiment:** Synthesize slice-level motion on clean stacks, train gated vs. ungated; test on genuinely motion-corrupted stacks with expert labels. Falsified if gating gains don't transfer to real motion.
- **Main Risk:** Real motion artifacts differ from simulated ones in structured ways.
- **Cluster:** MedSeg

### B-0027
- **One-sentence idea:** Formulate 3D interactive correction as a conditional update network: one corrected slice (or scribble) plus current prediction in, corrected volume out — optimizing clicks-to-acceptable, not Dice.
- **Problem:** Editing tools propagate corrections geometrically (interpolation), ignoring image evidence; learned interactive models are trained for from-scratch segmentation, not for minimal-effort repair of an existing near-miss prediction.
- **Core Hypothesis:** A network trained specifically on (prediction, correction) → (repaired volume) pairs, with errors sampled from real model failure modes, halves the interactions needed to reach clinical acceptability versus scribble-based from-scratch interactive baselines.
- **Why Important:** In practice every clinical mask is human-verified; total edit effort is the real cost function of the field, and almost nobody optimizes it.
- **Why Possibly Novel:** The training distribution (repairing realistic model errors rather than segmenting from scratch) is the novel, testable ingredient.
- **Minimal Experiment:** Generate failure cases from a frozen model; train repair net; measure simulated clicks-to-95%-Dice vs. interactive baselines. Falsified if repair-specific training doesn't beat generic interactive models.
- **Main Risk:** Simulated click behavior may not match real annotators (needs small user study eventually).
- **Cluster:** MedSeg

### B-0028
- **One-sentence idea:** Characterize and correct structure-size-dependent miscalibration: fit size-conditional temperature/threshold corrections so small structures stop being systematically mis-confident.
- **Problem:** Calibration is evaluated globally; segmentation confidence is systematically size-dependent (tiny structures often overconfidently missed or underconfidently found), which global temperature scaling cannot fix.
- **Core Hypothesis:** A simple size-conditional recalibration (temperature as a monotone function of predicted component size) yields large calibration gains for small structures at zero accuracy cost, and the size-miscalibration pattern is consistent across architectures.
- **Why Important:** Downstream consumers (uncertainty gating, active learning, QC) all assume calibrated confidence; size-dependence silently breaks all of them for small lesions.
- **Why Possibly Novel:** Size-stratified calibration analysis of segmentation models appears to be an unfilled, easily testable empirical niche.
- **Minimal Experiment:** Post-hoc analysis of 3 public models: ECE stratified by component size, then fit size-conditional temperature on val, test on held-out. Days of work, no training.
- **Main Risk:** Effect may be dataset-idiosyncratic rather than a general law.
- **Cluster:** MedSeg

### B-0029
- **One-sentence idea:** Make multi-sequence MRI tumor models robust to missing sequences by conditioning on an explicit presence mask and training with structured sequence dropout, instead of zero-filling absent channels.
- **Problem:** Deployed brain-tumor models assume fixed four-sequence input; real referrals routinely lack sequences, and zero-imputation silently shifts feature statistics, causing degraded, unflagged predictions.
- **Core Hypothesis:** Presence-conditioned models degrade gracefully (performance falls proportionally to information lost, not catastrophically), and explicit conditioning beats zero-fill and beats learned imputation, especially for the sequence-combinations rarest in training.
- **Why Important:** Missing sequences are the norm in real-world neuro-oncology referrals; graceful degradation determines usability.
- **Why Possibly Novel:** Modality dropout is known; the specific claims about conditioning-vs-imputation ordering and rare-combination behavior are untested and decision-relevant.
- **Minimal Experiment:** Public brain tumor data: train the three variants, evaluate all 15 sequence subsets. Falsified if zero-fill with dropout training is already optimal.
- **Main Risk:** Combinatorial evaluation cost; conclusions may vary by tumor sub-region.
- **Cluster:** MedSeg

### B-0030
- **One-sentence idea:** Detect and exploit "anatomical addressability": predict each voxel's coordinates in a canonical body atlas as an auxiliary task, giving the network an explicit positional prior for organ layout.
- **Problem:** Networks relearn "the liver is under the right lung" implicitly from limited data and forget it under shift; positional priors are strong in medicine but unused as explicit supervision.
- **Core Hypothesis:** Jointly regressing canonical atlas coordinates (trainable from cheap coarse registrations) improves organ segmentation most under domain shift and in low-data regimes, because layout knowledge transfers even when appearance does not.
- **Why Important:** A cheap, label-free auxiliary signal that specifically targets the shift/low-data regimes where medical segmentation actually struggles.
- **Why Possibly Novel:** Atlas coordinates as auxiliary dense regression for segmentation robustness — with the specific prediction that gains concentrate under shift — is a testable, mechanism-level idea rather than generic multi-task learning.
- **Minimal Experiment:** Generate pseudo-coordinates via affine registration to one template; train with/without the auxiliary head; compare in-domain vs. cross-site gaps. Falsified if gains are uniform or absent.
- **Main Risk:** Coarse registration noise may cap the value of the auxiliary signal.
- **Cluster:** MedSeg
## Section 2 — Medical Vision Foundation Models [B-0031–B-0060]

### B-0031
- **One-sentence idea:** Replace uniform random masking in medical masked-image-modeling with anatomy-weighted masking that allocates mask budget by local anatomical information density.
- **Problem:** In CT/MRI, a large fraction of voxels are air, couch, or homogeneous tissue; uniform MIM spends most of its pretraining signal reconstructing trivially predictable content, starving rare informative regions.
- **Core Hypothesis:** Masking proportional to local information (entropy/edge density/atlas-derived organ maps) yields better frozen features for boundary-sensitive downstream tasks at equal pretraining compute, with the largest gains for small-structure segmentation.
- **Why Important:** Pretraining compute for 3D is the binding constraint on medical FMs; better sample efficiency compounds across the whole field.
- **Why Possibly Novel:** Content-aware masking exists in natural images, but exploiting the extreme, quantifiable background redundancy of medical volumes with anatomical priors is a distinct, testable mechanism.
- **Minimal Experiment:** Pretrain two small ViTs (uniform vs. anatomy-weighted masking) on the same corpus for equal steps; linear-probe on 3 segmentation tasks. Falsified if downstream parity.
- **Main Risk:** Weighted masking may just replicate what longer uniform training achieves (a constant-factor, not qualitative, gain).
- **Cluster:** MedFM

### B-0032
- **One-sentence idea:** Run a controlled scaling-law study for 3D medical foundation models that separates the axes of dataset size, voxel resolution, and patient diversity.
- **Problem:** Medical FM efforts scale "data" blindly; nobody knows whether adding more patients, more scans per patient, or higher resolution buys more downstream segmentation accuracy, so compute is allocated by folklore.
- **Core Hypothesis:** Patient diversity dominates raw scan count (heavily correlated repeat scans add little), and resolution scaling shows task-dependent exponents — quantifiable as separable power laws.
- **Why Important:** The next generation of medical FMs will cost millions in compute; knowing the exponents changes what data consortia should collect.
- **Why Possibly Novel:** Scaling laws exist for natural-image/LLM domains; the medical-specific axes (patients vs. scans vs. resolution) have never been disentangled.
- **Minimal Experiment:** Grid of small-scale pretrainings on subsets controlling each axis independently (fixable at ~modest GPU budget with small ViTs); fit power laws; check extrapolation on one mid-scale run. Falsified if curves are indistinguishable across axes.
- **Main Risk:** Small-scale exponents may not extrapolate; conclusions could be architecture-specific.
- **Cluster:** MedFM

### B-0033
- **One-sentence idea:** Tokenize medical volumes with content-adaptive supervoxels instead of fixed cubic patches, so token boundaries align with anatomical boundaries.
- **Problem:** Fixed-grid patches split organs and merge unrelated tissues into single tokens; the model wastes capacity undoing an arbitrary discretization that ignores anatomy.
- **Core Hypothesis:** Supervoxel tokenization (with token-count matched to grid baseline) improves dense downstream performance, particularly boundary metrics, because token-internal homogeneity increases and boundary information is preserved at token edges.
- **Why Important:** Tokenization is the foundational design choice of every volumetric transformer; a better default lifts all downstream work.
- **Why Possibly Novel:** Superpixel tokenization is explored in 2D vision; a rigorous 3D medical instantiation with boundary-metric-focused evaluation and matched compute is missing.
- **Minimal Experiment:** Pretrain/finetune same transformer with grid vs. supervoxel tokens (equal token count) on 2 organ tasks; compare surface Dice. Falsified if boundary metrics don't improve.
- **Main Risk:** Irregular tokens complicate positional encoding and efficient batching; engineering overhead may eat the gains.
- **Cluster:** MedFM

### B-0034
- **One-sentence idea:** Build CT foundation models that treat Hounsfield units as calibrated physical measurements — enforcing quantitative-intensity equivariance instead of normalizing intensities away.
- **Problem:** Standard pipelines window/normalize CT, discarding the fact that HU is an absolute physical scale; models then confuse tissues that are trivially separable by calibrated density and fail on out-of-window structures.
- **Core Hypothesis:** A model with an intensity-faithful input pathway (multi-window plus raw-HU channel with physically meaningful encodings) will beat single-window baselines on tasks spanning wide density ranges, and will transfer across protocols better because HU semantics are protocol-stable.
- **Why Important:** CT is the highest-volume modality; throwing away its calibrated physics is a systematic self-inflicted handicap.
- **Why Possibly Novel:** Windowing choices are treated as hyperparameters; framing HU as a physical invariant with an equivariance objective is a mechanism-level rethink.
- **Minimal Experiment:** Train matched models with windowed vs. physics-faithful input encodings on a multi-tissue task (e.g., simultaneous bone+soft-tissue+lung); compare in- and cross-protocol. Falsified if window ensembles already saturate.
- **Main Risk:** HU calibration is imperfect in practice (kernel/kVp dependence), weakening the invariance.
- **Cluster:** MedFM

### B-0035
- **One-sentence idea:** Systematically audit train-test contamination between medical FM pretraining corpora and popular benchmarks via near-duplicate patient/scan detection, and publish decontaminated benchmark splits.
- **Problem:** Medical FMs are pretrained on aggregated public corpora that silently overlap the benchmarks used to certify them (same patients across dataset releases, re-hosted subsets), inflating reported zero/few-shot performance.
- **Core Hypothesis:** A meaningful fraction of standard benchmark cases are near-duplicates of pretraining data for at least some widely used FMs, and decontaminated evaluation measurably reorders published model rankings.
- **Why Important:** If contamination is real, part of the field's perceived FM progress is an artifact — this is foundational hygiene work.
- **Why Possibly Novel:** Contamination auditing is established for LLMs but essentially absent for medical imaging FMs, where patient-level overlap is subtler than exact duplication.
- **Minimal Experiment:** Build embedding-based near-duplicate detector; run across 3 public corpora × 5 benchmarks; re-evaluate 2 public FMs on clean vs. full splits. No training required.
- **Main Risk:** Duplicate detection thresholds are contestable; overlap may turn out negligible (a null result, though still publishable hygiene).
- **Cluster:** MedFM

### B-0036
- **One-sentence idea:** Retrieval-augmented segmentation: retrieve the most similar labeled cases from a reference library at inference and condition the decoder on their image-mask pairs.
- **Problem:** Parametric models cannot exploit the growing archives of labeled cases at inference; rare anatomies fail even when a nearly identical labeled case exists in the archive.
- **Core Hypothesis:** Conditioning on retrieved (image, mask) neighbors improves performance specifically on tail cases (rare variants, rare pathologies), with gains monotone in retrieval quality — while head cases are unaffected.
- **Why Important:** Hospitals own exactly this asset (archives); retrieval turns data governance into direct inference-time value without retraining.
- **Why Possibly Novel:** Retrieval augmentation is mature in NLP; a dense-prediction medical variant with a tail-case-stratified falsifiable claim is largely unexplored.
- **Minimal Experiment:** Train retrieval-conditioned decoder on public organ data; evaluate stratified by nearest-neighbor distance (proxy for rarity); ablate with random retrieval (must hurt). Falsified if random ≈ true retrieval.
- **Main Risk:** Retrieval may leak benchmark near-duplicates, faking gains (ties to B-0035 audit).
- **Cluster:** MedFM

### B-0037
- **One-sentence idea:** Train a medical in-context segmentation model (prompt with k example image-mask pairs, segment the query) and measure how in-context ability scales with pretraining task diversity, not data volume.
- **Problem:** Every new structure currently requires fine-tuning; existing in-context vision models are trained on natural images and transfer poorly to volumetric medicine, and nobody knows what drives emergence of dense in-context ability.
- **Core Hypothesis:** In-context segmentation quality scales primarily with the number of distinct labeled tasks (structures × protocols) seen in pretraining, following a task-diversity law, and saturates quickly with per-task volume.
- **Why Important:** If task diversity is the binding variable, the field should invest in many small labeled tasks rather than a few giant datasets — a strategic redirection.
- **Why Possibly Novel:** Task-diversity scaling for dense in-context learning is unmeasured; the medical setting uniquely provides hundreds of well-defined structures to test it.
- **Minimal Experiment:** Assemble N tasks from public label sets; train in-context learner on {10, 30, 100} tasks with volume held fixed; evaluate on held-out structures. Falsified if volume, not diversity, drives held-out performance.
- **Main Risk:** Compute-hungry; conclusions may be capacity-dependent.
- **Cluster:** MedFM

### B-0038
- **One-sentence idea:** Map where parameter-efficient adaptation must be placed in volumetric transformers: test the hypothesis that appearance shift requires early-layer adapters while label/task shift requires late-layer adapters.
- **Problem:** LoRA/adapter placement for 3D medical models is copied from NLP recipes; when adaptation fails, practitioners cannot tell whether the placement or the budget was wrong.
- **Core Hypothesis:** There is a systematic layer-shift correspondence — scanner/protocol shifts are corrected by early-block adaptation, new-structure learning by late-block adaptation — and mismatched placement wastes most of the parameter budget.
- **Why Important:** A placement law would turn adapter configuration from trial-and-error into a principled decision, saving compute across all medical FM fine-tuning.
- **Why Possibly Novel:** Layer-wise adaptation analyses exist for classification; a controlled shift-type × placement factorial for dense 3D prediction does not.
- **Minimal Experiment:** One FM, two shift types (cross-scanner same task; same scanner new structure), adapters at early/mid/late/all; full factorial is ~12 cheap fine-tunes. Falsified if placement is irrelevant.
- **Main Risk:** Findings may not generalize across FM architectures.
- **Cluster:** MedFM

### B-0039
- **One-sentence idea:** Prevent catastrophic forgetting when fine-tuning medical FMs on narrow tasks by rehearsing on self-generated pseudo-labeled diverse anatomy instead of stored data.
- **Problem:** Fine-tuning an FM for one organ measurably destroys its broad capabilities, but data-retention constraints (privacy) forbid classic rehearsal buffers of original pretraining data.
- **Core Hypothesis:** Rehearsal with the FM's own pseudo-labels on public/synthetic diverse anatomy preserves generalist performance nearly as well as true-data rehearsal, because what must be preserved is the function, not the data.
- **Why Important:** Hospitals will fine-tune shared FMs locally; without privacy-compatible forgetting mitigation, every local model silently narrows.
- **Why Possibly Novel:** Data-free/pseudo-rehearsal is studied in classification; quantifying dense-prediction forgetting in medical FMs and testing pseudo-rehearsal there is open.
- **Minimal Experiment:** Fine-tune a public medical FM on one organ; measure degradation on 5 other tasks; compare no-rehearsal vs. pseudo-rehearsal vs. true rehearsal. Falsified if pseudo-rehearsal fails to close the gap.
- **Main Risk:** Pseudo-label errors may reinforce and amplify existing FM biases.
- **Cluster:** MedFM

### B-0040
- **One-sentence idea:** Measure whether medical FMs memorize rare patients — via membership-inference and near-copy reconstruction attacks on MIM-pretrained models — and identify which pretraining choices modulate it.
- **Problem:** Medical FM pretraining is presumed privacy-safe because "only features are learned," but MIM explicitly optimizes reconstruction, and rare cases (unusual anatomy, implants) are plausibly memorized verbatim; no one has quantified this for volumetric FMs.
- **Core Hypothesis:** Membership inference succeeds well above chance for outlier patients in MIM-pretrained medical FMs, and memorization concentrates on the rare cases that are also the most re-identifiable — with masking ratio and deduplication as the strongest mitigating knobs.
- **Why Important:** A positive result changes the legal calculus of every data-sharing consortium; a strong negative result unblocks data sharing.
- **Why Possibly Novel:** Memorization science exists for LLMs/diffusion; volumetric medical MIM has unique structure (3D, small corpora, extreme outliers) and zero published measurements.
- **Minimal Experiment:** Pretrain small MIM models with known member/non-member splits including planted outliers; run standard MI attacks; ablate masking ratio and dedup. Fully controlled and cheap.
- **Main Risk:** Small-model results may understate or overstate large-model memorization.
- **Cluster:** MedFM

### B-0041
- **One-sentence idea:** Federated pretraining of a multi-modality medical FM using locally routed modality experts over a shared anatomical trunk, so sites never share raw data or modality-specific experts.
- **Problem:** No single institution has all modalities at scale; naive federated averaging across sites with disjoint modalities (CT-only site, MR-only site) destroys modality-specific features and converges poorly.
- **Core Hypothesis:** Architecturally separating modality-expert parameters (updated only locally by sites owning that modality) from a shared trunk (federated) matches centralized multimodal pretraining within a small margin, whereas plain FedAvg degrades severely as modality skew grows.
- **Why Important:** This is the realistic path to a broad medical FM given data-governance reality; the field needs to know whether it works.
- **Why Possibly Novel:** Federated learning with systematically disjoint modalities per client (not just non-IID labels) is an understudied regime with a clean architectural answer to test.
- **Minimal Experiment:** Simulate 6 clients with skewed modality ownership on public CT/MR corpora; compare FedAvg vs. expert-trunk splitting vs. centralized. Falsified if FedAvg is fine.
- **Main Risk:** Simulated federation understates real-world heterogeneity (compute, dropout, protocol drift).
- **Cluster:** MedFM

### B-0042
- **One-sentence idea:** Characterize the frequency-response bias of medical FMs (which spatial-frequency bands their features preserve) and correct it with band-balanced pretraining perturbations.
- **Problem:** Downstream failures on fine structures (trabeculae, small vessels, GGO texture) suggest FM features are low-frequency dominated, but no one measures a model's frequency response, so fixes are blind guesses.
- **Core Hypothesis:** A frequency-probing suite (linear decoding of band-filtered targets) will reveal systematic high-frequency information loss in MIM-pretrained medical FMs, and pretraining with band-balanced reconstruction targets recovers it, improving exactly the fine-structure downstream tasks.
- **Why Important:** A measurable "frequency fingerprint" per FM would let practitioners match models to tasks and diagnose failures mechanistically.
- **Why Possibly Novel:** Frequency analyses exist for GANs/classifiers; a standardized frequency-response probe for dense medical FMs plus a corrective objective is new.
- **Minimal Experiment:** Probe 3 public medical FMs for band-wise decodability; correlate with fine-structure task performance; retrain one small FM with band-balanced targets. Falsified if no frequency deficit exists or correction doesn't transfer.
- **Main Risk:** Frequency deficits may be dataset artifacts (reconstruction kernels) rather than model properties.
- **Cluster:** MedFM

### B-0043
- **One-sentence idea:** Entropy-adaptive token merging for whole-body volumes: aggressively merge tokens in homogeneous regions while preserving full resolution in complex regions, to make whole-body transformers tractable.
- **Problem:** Whole-body scans exceed transformer context budgets; uniform downsampling or fixed token merging destroys small lesions, while cropping destroys global context — both failure modes are documented pain points.
- **Core Hypothesis:** Local-complexity-adaptive merging retains organ-level performance at 5–10× token reduction while uniform merging at the same budget measurably loses small-lesion sensitivity — i.e., where tokens are spent matters more than how many.
- **Why Important:** Whole-body reasoning (staging, metastasis screening) is the flagship FM use case and is currently compute-blocked.
- **Why Possibly Novel:** Token merging (ToMe-style) exists for 2D classification; a content-adaptive 3D version evaluated on lesion sensitivity vs. token budget curves is unexplored.
- **Minimal Experiment:** Fixed backbone, sweep uniform vs. adaptive merging budgets on a whole-body dataset with small-lesion annotations; plot sensitivity-vs-tokens curves. Falsified if curves coincide.
- **Main Risk:** Complexity estimator itself may miss subtle lesions (chicken-and-egg).
- **Cluster:** MedFM

### B-0044
- **One-sentence idea:** Define an "acquisition-sensitivity fingerprint" benchmark: measure every medical FM's output sensitivity to controlled acquisition-parameter perturbations (kernel, dose, sequence, spacing) as a standard model card entry.
- **Problem:** FMs are compared on accuracy leaderboards while their sensitivity to acquisition parameters — the property that determines deployment safety — is unmeasured and unreported.
- **Core Hypothesis:** FMs differ dramatically and consistently in parameter sensitivity even at matched accuracy, and the fingerprint predicts cross-site performance drop better than in-domain accuracy does.
- **Why Important:** Would give hospitals a rational basis for model selection and shift regulators toward measurable robustness claims.
- **Why Possibly Novel:** Robustness benchmarks exist for natural corruptions; physically grounded acquisition-parameter sweeps (via simulation and paired-protocol data) for medical FMs do not.
- **Minimal Experiment:** Build perturbation suite from public paired-protocol data + physics simulation; fingerprint 4 public FMs; correlate fingerprints with known cross-site gaps. No training needed.
- **Main Risk:** Simulated perturbations may not span real protocol variation.
- **Cluster:** MedFM

### B-0045
- **One-sentence idea:** Localize where demographic performance bias enters medical FMs by swapping pretraining and fine-tuning populations factorially and measuring per-group segmentation quality.
- **Problem:** Segmentation quality differences across demographic groups are reported anecdotally, but nobody knows whether bias is inherited from pretraining corpora or induced during fine-tuning, so mitigation is misdirected.
- **Core Hypothesis:** A factorial swap (pretrain on group-skewed corpus A/B × fine-tune on A/B) will show that most per-group boundary-quality disparity traces to the fine-tuning distribution, not pretraining — a decision-relevant, falsifiable attribution.
- **Why Important:** Determines whether fair medical AI requires rebalancing billion-image pretraining sets (very costly) or just fine-tuning sets (cheap).
- **Why Possibly Novel:** Bias attribution via factorial pretrain/finetune swaps has not been done for dense medical prediction.
- **Minimal Experiment:** Use public datasets with demographic metadata; 2×2 factorial with small FMs; per-group surface metrics. Falsified if pretraining dominates.
- **Main Risk:** Confounding between demographics and scanners/sites in available data.
- **Cluster:** MedFM

### B-0046
- **One-sentence idea:** Open-vocabulary medical segmentation where class queries are embeddings of ontology graph nodes (RadLex/SNOMED), enabling zero-shot segmentation of unseen structures via graph proximity.
- **Problem:** Universal medical segmenters use flat class lists; a structure absent from training is unaddressable even when it is an obvious ontological neighbor of trained structures (e.g., a specific muscle in a trained muscle group).
- **Core Hypothesis:** Conditioning the decoder on ontology-graph embeddings lets zero-shot performance on held-out structures scale with graph proximity to trained structures — a testable monotone relationship that flat-label models cannot exhibit.
- **Why Important:** Medicine has thousands of nameable structures; per-structure annotation will never cover them, but ontologies already encode their relationships for free.
- **Why Possibly Novel:** Open-vocabulary segmentation uses free-text embeddings; using curated medical ontology graph structure as the query space, with proximity-scaling as the falsifiable claim, is distinct.
- **Minimal Experiment:** Train on N structures with ontology queries, hold out structures at graded graph distances; test the proximity-performance correlation. Falsified if performance is flat in graph distance.
- **Main Risk:** Ontology distance may correlate poorly with visual similarity for some organ families.
- **Cluster:** MedFM

### B-0047
- **One-sentence idea:** Continual (streaming) pretraining of medical FMs across sequentially arriving sites, using generative replay of synthetic exemplars instead of stored patient data.
- **Problem:** Medical FMs are frozen artifacts; the data distribution drifts (new scanners, protocols), but retraining from scratch is prohibitive and storing old site data for replay is legally impossible.
- **Core Hypothesis:** Streaming pretraining with a lightweight generative-replay memory maintains within-a-margin performance on early sites while capturing new sites, whereas naive continued pretraining measurably forgets early-site protocols.
- **Why Important:** Real deployment is a stream, not a snapshot; the field has no validated recipe for keeping FMs current.
- **Why Possibly Novel:** Continual SSL with privacy-compatible replay for volumetric medical data is an unoccupied intersection of continual learning and medical FM work.
- **Minimal Experiment:** Sequence 4 public datasets as "sites"; compare joint training vs. naive sequential vs. generative-replay sequential on per-site probes. Falsified if naive sequential doesn't forget.
- **Main Risk:** Generative replay quality for 3D may be insufficient to preserve protocol-specific features.
- **Cluster:** MedFM

### B-0048
- **One-sentence idea:** Distill 3D FMs into 2.5D slice-wise students with cross-slice consistency distillation, simultaneously quantifying how much genuinely 3D information the teacher actually uses.
- **Problem:** 3D FMs are undeployable on clinical edge hardware, and — separately — the field has never cleanly measured how much of "3D model superiority" is true volumetric reasoning versus better effective capacity.
- **Core Hypothesis:** A 2.5D student distilled with inter-slice feature-consistency targets recovers most of the 3D teacher's performance, and the residual gap (the "irreducible 3D value") is task-dependent and small for organs but large for tortuous structures — making the gap itself a measurable scientific quantity.
- **Why Important:** Answers both a deployment need and a foundational architecture question with one set of experiments.
- **Why Possibly Novel:** Distillation is routine; using the distillation residual as an instrument to quantify intrinsic 3D task requirements is a new framing.
- **Minimal Experiment:** Distill one public 3D model into 2.5D on 3 tasks of varying "3D-ness"; report residual gaps. Falsified if gaps are uniform (no task structure).
- **Main Risk:** Distillation losses may confound the measurement (student capacity limits mistaken for 3D value).
- **Cluster:** MedFM

### B-0049
- **One-sentence idea:** Probe whether medical FM embedding geometry preserves anatomical topology (adjacency, containment) and use the topology-preservation score to predict transfer performance.
- **Problem:** FM selection for a new task is done by leaderboard rank, which predicts transfer poorly; we lack intrinsic, task-free measurements of what anatomical structure an FM has internalized.
- **Core Hypothesis:** The degree to which an FM's patch-embedding space preserves anatomical adjacency relations (measured against atlas-derived ground truth graphs) predicts its downstream segmentation transfer better than in-domain benchmark scores.
- **Why Important:** A cheap intrinsic probe that predicts transfer would save enormous fine-tuning compute across the community.
- **Why Possibly Novel:** Representation-geometry probes exist in NLP (analogies, structure); anatomical-topology probing of medical FMs is unattempted.
- **Minimal Experiment:** Compute topology-preservation scores for 5 public FMs; correlate with fine-tuned performance on 6 tasks (many results already public). Nearly free.
- **Main Risk:** Correlation may exist but be driven by a confounder (model scale).
- **Cluster:** MedFM

### B-0050
- **One-sentence idea:** Establish a frozen-feature dense-probing benchmark for medical FMs and test whether FM rankings flip between linear probing and full fine-tuning.
- **Problem:** Medical FM papers evaluate with full fine-tuning, which mostly measures architecture + data, not representation quality; rankings may be artifacts of fine-tuning recipes, and cheap probing evaluations are nonstandard.
- **Core Hypothesis:** FM rankings under frozen dense probes disagree substantially with full-fine-tuning rankings, and the frozen ranking predicts low-data-regime performance better — meaning current leaderboards mislead exactly the users (low-data clinics) who need FMs most.
- **Why Important:** Would redefine how the field measures medical FM progress, separating representation from recipe.
- **Why Possibly Novel:** Dense frozen probing suites exist in natural imaging research; the ranking-flip hypothesis for medical FMs is untested and consequential.
- **Minimal Experiment:** Frozen linear/light-decoder probes for 5 public FMs × 6 tasks; compare orderings against published fine-tuned results and against 10-shot fine-tuning. Falsified if orderings agree everywhere.
- **Main Risk:** Probe design choices (decoder capacity) could themselves determine rankings.
- **Cluster:** MedFM

### B-0051
- **One-sentence idea:** Pretrain medical FMs by solving dense multi-scale registration between unlabeled scan pairs, on the hypothesis that correspondence is a better dense pretext than reconstruction.
- **Problem:** MIM optimizes pixel reconstruction, which rewards texture memory more than spatial precision; downstream boundary tasks need exactly the correspondence precision that reconstruction pretexts don't enforce.
- **Core Hypothesis:** Registration-pretrained features beat reconstruction-pretrained features on boundary-sensitive downstream tasks at matched compute, with the advantage concentrated in surface metrics rather than region metrics.
- **Why Important:** Identifies the right dense pretext for medical pretraining — a foundational, compounding choice.
- **Why Possibly Novel:** Registration as a self-supervised task exists, but a head-to-head pretext comparison isolating boundary-metric outcomes at matched compute has not been run.
- **Minimal Experiment:** Pretrain small twins (MIM vs. registration pretext) on the same corpus; probe on 3 segmentation tasks with region and surface metrics separated. Falsified if surface metrics show no differential gain.
- **Main Risk:** Registration pretext may collapse on non-alignable pairs (different body regions) without careful pair mining.
- **Cluster:** MedFM

### B-0052
- **One-sentence idea:** Characterize test-time compute scaling for segmentation FMs: does quality scale with inference-time sampling (multiple stochastic decodes + agreement-based selection/merging), and where does it saturate?
- **Problem:** LLMs gain from test-time compute; segmentation inference is one-shot by convention, and nobody knows whether medical FMs have exploitable inference-time headroom or how to harvest it beyond crude TTA averaging.
- **Core Hypothesis:** Diverse stochastic decoding with learned agreement-based merging yields a monotone quality-vs-compute curve that beats TTA averaging at matched compute, with the largest gains on ambiguous/OOD cases.
- **Why Important:** Inference compute is cheap and elastic in clinics (non-real-time reads); a validated scaling knob converts idle compute into accuracy.
- **Why Possibly Novel:** Test-time scaling laws are unexplored for dense prediction; the ambiguity-stratified prediction makes it falsifiable rather than a bag of tricks.
- **Minimal Experiment:** Take a stochastic-decoder segmentation model; sweep samples 1→64 with merging strategies; plot quality vs. compute stratified by case difficulty. Falsified if the curve is flat beyond trivial averaging.
- **Main Risk:** Existing models may lack enough output diversity for selection to help (would require diversity-trained decoders).
- **Cluster:** MedFM

### B-0053
- **One-sentence idea:** Pretrain a modality-agnostic FM with aggressive cross-modality dropout (CT/MR/US of overlapping anatomy) to force a shared anatomical latent, then test zero-shot cross-modality segmentation transfer.
- **Problem:** Per-modality FMs cannot transfer labels across modalities; a structure labeled richly in CT must be re-annotated from scratch in ultrasound, though the underlying anatomy is identical.
- **Core Hypothesis:** If a shared anatomical latent exists, a decoder trained on CT labels alone will produce above-chance (and usefully warm-start-able) segmentations on MR/US of the same anatomy — with transfer quality tracking the modality overlap in pretraining.
- **Why Important:** Cross-modality label reuse would multiply the value of every existing annotation several-fold.
- **Why Possibly Novel:** Cross-modality synthesis and adaptation exist pairwise; testing for an emergent shared anatomical latent in a jointly pretrained FM, with zero-shot decoding as the probe, is a distinct question.
- **Minimal Experiment:** Pretrain a small joint model on unpaired multi-modality abdominal data; train decoder on CT labels; evaluate zero-shot on MR. Falsified if zero-shot is at chance.
- **Main Risk:** Without paired data, the latent may align coarse anatomy only, failing at boundary precision.
- **Cluster:** MedFM

### B-0054
- **One-sentence idea:** Measure resolution/patch-size transfer curves for medical FMs and fix scale brittleness with scale-randomized pretraining.
- **Problem:** FMs pretrained at one patch size and resolution degrade when fine-tuned or run at another — a routine mismatch (pretraining corpora are downsampled; clinical use is native-resolution) whose cost has never been quantified for dense medical tasks.
- **Core Hypothesis:** Scale mismatch causes a large, previously unattributed share of "FM underperformance vs. specialized models," and scale-randomized pretraining eliminates most of it at negligible pretraining cost.
- **Why Important:** Would explain a persistent puzzle (why FMs sometimes lose to small task-specific models) with an actionable, cheap fix.
- **Why Possibly Novel:** Resolution transfer is studied for classification ViTs; systematic dense-task transfer curves and the attribution claim for medical FMs are new.
- **Minimal Experiment:** Evaluate 3 public FMs across an inference-resolution sweep on fixed tasks; pretrain one small FM with/without scale randomization. Falsified if transfer curves are already flat.
- **Main Risk:** Scale randomization may dilute pretraining signal, trading peak for robustness.
- **Cluster:** MedFM

### B-0055
- **One-sentence idea:** Replace learned positional embeddings with body-coordinate embeddings derived from scout/localizer registration, so FM tokens know where in the body they are.
- **Problem:** Crop-based training gives FMs no notion of absolute anatomical position; models confuse look-alike structures from different body regions and behave erratically on unusual fields-of-view.
- **Core Hypothesis:** Injecting approximate canonical body coordinates (cheaply obtained from localizers or coarse whole-scan registration) improves whole-body tasks and dramatically improves robustness to unusual FOV crops, with negligible cost in-domain.
- **Why Important:** FOV variation is a mundane, ubiquitous deployment shift with no current mechanism addressing it.
- **Why Possibly Novel:** Anatomical positional priors as replacement/augmentation for learned positional embeddings in FMs is a concrete architectural gap (relates to B-0030 but at pretraining scale and in the embedding, not as auxiliary task).
- **Minimal Experiment:** Fine-tune matched models ± body-coordinate embeddings; evaluate on aggressively cropped test volumes. Falsified if crop robustness is unchanged.
- **Main Risk:** Coordinate estimation fails exactly on unusual scans where it is most needed.
- **Cluster:** MedFM

### B-0056
- **One-sentence idea:** Use the FM's own pretraining signal (e.g., masked-reconstruction error maps) as a free, training-free spatial error predictor for downstream segmentation QC.
- **Problem:** Downstream QC systems (like B-0010) need training on failure examples; but the FM already computes a self-supervised difficulty signal that might localize likely segmentation errors for free — a hypothesis nobody has checked.
- **Core Hypothesis:** Spatial MIM-reconstruction error correlates with downstream segmentation error location well enough to flag error regions with useful precision, especially under domain shift where supervised QC breaks.
- **Why Important:** A zero-training universal QC signal would be immediately deployable with every FM-based pipeline.
- **Why Possibly Novel:** Reconstruction error is used for anomaly detection; its use as a segmentation-error localizer with quantified precision/recall is an untested, cheap-to-check claim.
- **Minimal Experiment:** For one FM-based segmenter, compute voxelwise correlation between masked-reconstruction error and segmentation error on in-domain and shifted test sets. A few days, no training. Falsified if correlation is negligible.
- **Main Risk:** Reconstruction difficulty may track texture complexity, not semantic error.
- **Cluster:** MedFM

### B-0057
- **One-sentence idea:** Test whether aggressive dedup + diversity-pruning of medical pretraining corpora (removing near-identical slices/series) lets a 10× smaller corpus match full-corpus FM quality.
- **Problem:** Medical corpora are extraordinarily redundant (adjacent slices, repeat scans, protocol clones); pretraining cost scales with tokens while information may scale far slower — but nobody has measured the redundancy discount.
- **Core Hypothesis:** Information-based pruning retains downstream performance within noise at ≤10–20% of the original corpus, and the pruning score (embedding-space density) transfers across corpora — establishing a data-curation law for medical pretraining.
- **Why Important:** Would cut medical FM pretraining costs by an order of magnitude and redirect effort from hoarding to curating.
- **Why Possibly Novel:** Data pruning science exists for natural images/LLMs; the extreme structured redundancy of volumetric medical data makes both the opportunity and the measurement different, and it is unmeasured.
- **Minimal Experiment:** Prune one public corpus at {100, 30, 10, 3}% by density score vs. random; pretrain small FMs; probe downstream. Falsified if random pruning matches density pruning.
- **Main Risk:** Rare-case removal by overzealous pruning could hurt exactly the tail robustness that matters.
- **Cluster:** MedFM

### B-0058
- **One-sentence idea:** Train mixture-of-experts medical FMs and test whether unsupervised expert routing spontaneously discovers pathology (routing as a free abnormality detector).
- **Problem:** MoE routing in vision is treated as a pure efficiency trick; whether routing decisions carry clinically meaningful structure (normal vs. abnormal tissue) is unknown — if they do, MoE FMs ship a free anomaly signal.
- **Core Hypothesis:** In MoE FMs pretrained on mixed normal/pathological data, a small subset of experts specializes on abnormal tissue, and routing statistics alone achieve non-trivial abnormality localization without any labels.
- **Why Important:** Free unsupervised pathology localization from an architecture already adopted for efficiency would be a significant emergent capability.
- **Why Possibly Novel:** Emergent expert semantics have been observed in NLP; the pathology-specialization hypothesis for medical vision MoE is specific, cheap to test, and unexamined.
- **Minimal Experiment:** Pretrain a small MoE on a corpus with known lesion annotations held out; measure AUROC of routing-derived abnormality maps. Falsified if routing is semantically random.
- **Main Risk:** Experts may specialize on acquisition parameters (scanner) rather than pathology.
- **Cluster:** MedFM

### B-0059
- **One-sentence idea:** Add a cross-scale feature-consistency objective to medical FM pretraining so that structures produce stable features across the resolution pyramid, targeting lesions visible only at particular scales.
- **Problem:** Feature pyramids of current FMs represent the same structure inconsistently across scales; small lesions are represented at fine scales but contextualized at coarse scales, and the mismatch produces scale-dependent misses.
- **Core Hypothesis:** Enforcing cross-scale consistency (fine features, pooled, must predict coarse features and vice versa) improves detection/segmentation of scale-marginal structures — those near the visibility threshold — more than it affects large structures, a testable size-stratified prediction.
- **Why Important:** Scale-marginal lesions (small mets, early GGO) are where screening value concentrates and where models are least reliable.
- **Why Possibly Novel:** Multi-scale architectures abound, but an explicit cross-scale consistency pretraining loss with size-stratified evaluation is a specific untested mechanism.
- **Minimal Experiment:** Pretrain small twins ± the objective; evaluate lesion sensitivity stratified by lesion size. Falsified if gains are size-uniform or absent.
- **Main Risk:** Consistency may over-smooth scale-specific information that is genuinely scale-local.
- **Cluster:** MedFM

### B-0060
- **One-sentence idea:** Cross-patient anatomical contrastive pretraining: use registration-derived correspondence to make "same anatomical location, different patient" the positive pair, instead of augmentation-based positives.
- **Problem:** Augmentation-based contrastive learning defines positives as views of the same image, teaching instance identity rather than anatomical semantics; features cluster by patient/scan, not by anatomy — the opposite of what segmentation needs.
- **Core Hypothesis:** Cross-patient positives (same atlas location) produce features whose linear separability of anatomical classes is markedly higher, translating into better few-shot segmentation than instance-contrastive or MIM baselines at matched compute.
- **Why Important:** Aligns the pretext directly with the downstream invariance actually needed (patient-invariant, anatomy-specific features).
- **Why Possibly Novel:** Position-based positives have been touched in limited settings; a rigorous comparison against MIM with atlas-graded correspondence quality as a controlled variable is missing.
- **Minimal Experiment:** Pretrain small twins (instance-positive vs. cross-patient-positive) using cheap affine correspondences; few-shot probe on 3 structures. Falsified if anatomical positives don't beat instance positives.
- **Main Risk:** Registration errors inject label noise into positives; pathology violates cross-patient correspondence.
- **Cluster:** MedFM
## Section 3 — Smoke/Fire/Transparent/Ambiguous Segmentation [B-0061–B-0090]

### B-0061
- **One-sentence idea:** Reformulate smoke segmentation as alpha-matte/optical-density regression instead of binary masking, because smoke physically has no boundary.
- **Problem:** Binary smoke masks are ill-posed — annotators draw arbitrary contours through a continuous density field — so models trained on them learn annotator whim, and IoU rewards reproducing that whim rather than perceiving smoke.
- **Core Hypothesis:** Models trained to regress per-pixel opacity (supervised via composited data with known alpha) will beat binary-mask models on downstream tasks (early detection, density estimation) and will generalize across annotation conventions that break binary models.
- **Why Important:** Smoke detection is a life-safety application whose evaluation currently measures agreement with an arbitrary line, not perception of smoke.
- **Why Possibly Novel:** Matting is mature for hair/fur; establishing opacity regression as the correct problem statement for smoke, with a convention-transfer experiment as evidence, is a reframing contribution.
- **Minimal Experiment:** Composite real smoke plumes (chroma-keyed captures) onto scenes with exact alpha; train binary vs. opacity models; evaluate both on two differently-conventioned public smoke datasets. Falsified if binary transfers equally well.
- **Main Risk:** Composited training data may not span real in-the-wild smoke/illumination interactions.
- **Cluster:** AmbigSeg

### B-0062
- **One-sentence idea:** Create physically grounded smoke ground truth by capturing smoke in front of calibrated patterned backgrounds, recovering true per-pixel transmittance analytically.
- **Problem:** All existing smoke datasets rely on hand-drawn masks with no physical meaning; there is no ground truth against which density/opacity predictions can even be validated, blocking the entire measurement chain.
- **Core Hypothesis:** Transmittance recovered from known-background attenuation (light-transport inversion over checkerboard/LED panels) provides label quality sufficient to train and — critically — to benchmark opacity models that then transfer to natural backgrounds.
- **Why Important:** Gives the field its first physically meaningful benchmark; every subsequent smoke-perception claim becomes testable.
- **Why Possibly Novel:** Controlled-background matting capture exists for hair/objects; nobody has built the smoke/participating-media analog with radiometric calibration.
- **Minimal Experiment:** Lab capture with a fog machine, LED panel background, and radiometric calibration; verify recovered transmittance against a transmissometer at a few points; train a small model and test on natural-background captures of the same plume (turntable setup). Falsified if recovered alpha disagrees with physical measurement.
- **Main Risk:** Lab smoke (glycol fog) may differ optically from combustion smoke; needs at least one real-smoke validation session.
- **Cluster:** AmbigSeg

### B-0063
- **One-sentence idea:** Use turbulence statistics of motion (temporal power spectra of local flow) as a self-supervised signature separating smoke from fog, clouds, and dust.
- **Problem:** Appearance-based smoke detectors confuse smoke with fog banks, low clouds, and dust — the dominant false-alarm sources in wildfire camera networks — because single-frame appearance genuinely overlaps.
- **Core Hypothesis:** Buoyant combustion plumes have characteristic spatiotemporal spectral signatures (rising, turbulent cascade statistics) that are measurably distinct from advected fog/cloud motion, and a temporal-spectrum head reduces false alarms at fixed sensitivity.
- **Why Important:** False alarms are the operational killer of wildfire camera networks; a physics-motivated discriminative cue attacks the exact failure.
- **Why Possibly Novel:** Turbulence-statistics features have been used descriptively in fluid imaging; as a discriminative, self-supervised training signal for smoke-vs-lookalike classification they are unexplored.
- **Minimal Experiment:** From public wildfire-camera footage plus fog/cloud footage, compute local temporal spectra; test a shallow classifier on spectra alone vs. appearance-only CNN on confuser-heavy splits. Falsified if spectra carry no discriminative power.
- **Main Risk:** Requires sufficient frame rate and resolution; distant plumes may be too small for reliable spectral estimation.
- **Cluster:** AmbigSeg

### B-0064
- **One-sentence idea:** Exploit flame flicker frequency structure (via high-fps or event cameras) as a near-invariant fire signature to kill sunset/brake-light/reflection false positives.
- **Problem:** RGB fire segmentation relies on color and glow, which sunsets, sodium lamps, and reflections replicate; static appearance cannot separate them, and standard 30fps video aliases the discriminative flicker band.
- **Core Hypothesis:** Combustion flicker occupies a characteristic low-frequency band with broadband turbulence harmonics that man-made lights and sunlight lack; sampling that band (event camera or ≥120fps) provides a feature that removes most classic false positives at negligible sensitivity cost.
- **Why Important:** Fire alarm systems' credibility hinges on false-positive rates; a physical invariant is more durable than dataset patching.
- **Why Possibly Novel:** Flicker analysis appears in old handcrafted fire detection; a modern event-camera/high-fps learned pipeline with a curated false-positive stress benchmark would reset the field's evaluation standard.
- **Minimal Experiment:** Capture a small paired dataset (real flames, sunsets, lamps, reflective surfaces) with an event camera or 240fps phone; test flicker-band features vs. RGB CNN on the confuser set. Falsified if flicker adds nothing over color+texture.
- **Main Risk:** Wind-driven distant flames and near-smoldering fires may lack detectable flicker.
- **Cluster:** AmbigSeg

### B-0065
- **One-sentence idea:** Use polarization imaging as the primary cue for transparent-object segmentation, with a controlled study of when polarization is necessary versus when RGB context suffices.
- **Problem:** RGB transparent-object segmentation leans on contextual priors (glasses sit on tables) and fails on textureless, contextless glass; depth sensors return garbage on glass; the field lacks a principled account of which physical cue is actually needed when.
- **Core Hypothesis:** Specular polarization signatures at glass surfaces provide segmentation signal that is complementary and, in context-poor scenes, strictly necessary — such that a pol-RGB model beats RGB models by a margin that grows as contextual cues are experimentally removed.
- **Why Important:** Robot manipulation and cleaning in homes/labs fails on glassware; knowing the minimal sensor suite is a hardware-level design answer.
- **Why Possibly Novel:** Polarization datasets exist; the context-ablation methodology (systematically removing contextual cues to isolate physical necessity) is a new experimental design for this question.
- **Minimal Experiment:** Capture glassware on turntables with/without contextual surroundings using a polarization camera; train matched models; measure the RGB-vs-pol gap as a function of context richness. Falsified if RGB holds up context-free.
- **Main Risk:** Polarization cues degrade outdoors/under diffuse lighting; conclusions may be lighting-regime-specific.
- **Cluster:** AmbigSeg

### B-0066
- **One-sentence idea:** Mine LiDAR/ToF dropout and range-anomaly regions from robot logs as free weak labels for training RGB-only transparent-surface segmentation.
- **Problem:** Transparent surfaces require expensive manual annotation precisely because they are hard to see; meanwhile robots continuously generate depth-sensor failure patterns on those exact surfaces, a free label source nobody harvests systematically.
- **Core Hypothesis:** Depth-dropout-derived pseudo-labels (filtered by geometric consistency across viewpoints) suffice to train RGB transparent-region segmentation to a useful level without any human masks, and multi-view aggregation removes most dropout-noise false positives.
- **Why Important:** Converts an abundant deployment byproduct into supervision for one of the most annotation-hostile categories.
- **Why Possibly Novel:** Individual works have noted depth failure on glass; a systematic pipeline treating sensor failure as a weak-label channel with multi-view purification, evaluated against human-labeled benchmarks, is missing.
- **Minimal Experiment:** Use an existing RGB-D dataset containing glass; derive dropout pseudo-labels; train RGB model; evaluate on a human-labeled transparent-object benchmark. Falsified if pseudo-label noise caps performance far below few-shot supervised.
- **Main Risk:** Dropout also occurs on dark/absorptive and distant surfaces — confounders that filtering may not fully remove.
- **Cluster:** AmbigSeg

### B-0067
- **One-sentence idea:** Segment transparent objects by predicting the background-distortion (refraction) field and deriving the object mask from where distortion is non-zero.
- **Problem:** Direct appearance classification of transparent pixels is nearly information-free (the pixels show the background); current models therefore overfit to contours and context and miss unfamiliar transparent shapes.
- **Core Hypothesis:** The refraction-induced warp field between observed background and inferred undistorted background is a stronger, shape-generalizing signal: a warp-field model will generalize to unseen transparent object categories where appearance models collapse.
- **Why Important:** Category-level generalization is the practical requirement (robots meet novel glassware constantly).
- **Why Possibly Novel:** Refractive flow has been used for reconstruction in controlled setups; as the central representation for in-the-wild transparent segmentation with category-transfer evaluation, it is untested.
- **Minimal Experiment:** Train on ray-traced synthetic scenes (exact warp GT available) for a set of shapes; evaluate category-held-out on synthetic and on a small real benchmark; compare against appearance baseline under the same category split. Falsified if warp features don't improve category transfer.
- **Main Risk:** Estimating the undistorted background in cluttered real scenes may be too ill-posed without multi-view input.
- **Cluster:** AmbigSeg

### B-0068
- **One-sentence idea:** Replace masks with two-layer scene decomposition (foreground alpha + occluded background estimate) as the standard output for semi-transparent categories, with an evaluation protocol built on composited ground truth.
- **Problem:** For smoke, glass, dirty windows, and spray, a mask answers the wrong question — downstream consumers need what is behind and how much is in front, and no benchmark measures either.
- **Core Hypothesis:** Models trained for layered decomposition on composited data recover background content and alpha accurately enough to improve a concrete downstream task (e.g., detection of objects behind smoke/glass) versus mask-then-inpaint pipelines.
- **Why Important:** Defines the correct API for an entire object family; downstream perception through participating media is a real robotics/surveillance need.
- **Why Possibly Novel:** Layered representations exist in vision (reflections, matting); establishing them with a downstream-task-grounded benchmark for the ambiguous-object family is an unclaimed synthesis.
- **Minimal Experiment:** Composite objects behind synthetic smoke/glass over real scenes; compare detection-behind-occluder accuracy for layered model vs. mask+inpaint. Falsified if the pipeline matches end-to-end decomposition.
- **Main Risk:** Two-layer assumption breaks for multiple stacked transparent media.
- **Cluster:** AmbigSeg

### B-0069
- **One-sentence idea:** Develop and validate soft-boundary evaluation metrics for fuzzy objects by measuring which candidate metrics best predict human quality judgments of smoke/fire masks.
- **Problem:** IoU/Dice on fuzzy-boundary objects saturate on the easy interior and are dominated by arbitrary annotation width at the boundary; method rankings on smoke benchmarks may be measurement noise, but nobody has checked metrics against human judgment.
- **Core Hypothesis:** Human experts' preference orderings over predicted smoke masks disagree substantially with IoU orderings, and a boundary-uncertainty-weighted metric can be constructed that matches human preference significantly better — changing published method rankings.
- **Why Important:** If the metric is broken, the literature's conclusions are unreliable; metric science is upstream of all method work.
- **Why Possibly Novel:** Metric-vs-human-judgment validation is established in image quality and matting, but has never been applied to ambiguous-object segmentation benchmarks.
- **Minimal Experiment:** Collect pairwise human preferences over ~500 prediction pairs from existing public models on smoke data; compute metric-human agreement for IoU, boundary-F, matting metrics, and new candidates. No model training. Falsified if IoU already agrees with humans.
- **Main Risk:** Human judgments may be task-dependent (alarm vs. quantification), requiring multiple protocols.
- **Cluster:** AmbigSeg

### B-0070
- **One-sentence idea:** Collect multi-annotator labels on smoke/transparent boundaries and train ambiguity-calibrated models that predict the annotator distribution, testing whether model uncertainty can match human disagreement geography.
- **Problem:** Fuzzy-object datasets ship single-annotator masks, so ambiguity is baked in as noise; models are confidently wrong exactly where humans would disagree, and there is no data to even diagnose this.
- **Core Hypothesis:** Human disagreement on fuzzy boundaries is spatially systematic (predictable from image content), and a model trained on multi-annotator data can predict the disagreement map with high fidelity — enabling honest confidence output for alarms.
- **Why Important:** Alarm thresholds tuned on single-annotator data inherit one person's boundary taste; calibrated ambiguity enables principled operating points.
- **Why Possibly Novel:** Multi-rater modeling is developed in medical imaging (B-0003) but absent for smoke/fire/transparency, where ambiguity is arguably even larger.
- **Minimal Experiment:** Re-annotate 300 images from a public smoke dataset with 5 annotators; train disagreement-prediction head; evaluate on held-out annotators. Falsified if disagreement is idiosyncratic (unpredictable).
- **Main Risk:** Annotation cost; disagreement may partly reflect tool/interface artifacts.
- **Cluster:** AmbigSeg

### B-0071
- **One-sentence idea:** Run a controlled physics-fidelity ablation for synthetic smoke training data: which simulation components (scattering order, illumination model, turbulence resolution) actually matter for sim-to-real transfer.
- **Problem:** Synthetic smoke is widely used for training, but rendering choices are ad hoc; teams pay for expensive volumetric path tracing without evidence of which fidelity axes buy real-world performance.
- **Core Hypothesis:** Sim-to-real transfer is highly sensitive to a small subset of fidelity axes (plausibly multiple scattering and correct illumination coupling) and insensitive to others (fine turbulence detail) — yielding a cost-effective rendering recipe.
- **Why Important:** Gives every group a validated, minimal-cost synthesis recipe; kills cargo-cult rendering.
- **Why Possibly Novel:** Fidelity ablations exist for driving simulators; nothing comparable exists for participating media, whose rendering axes are unique.
- **Minimal Experiment:** Factorial rendering ablation (2^4 configurations) with fixed downstream architecture; evaluate all on the same real smoke test set. Falsified if transfer is fidelity-insensitive (then cheap rendering suffices — also useful).
- **Main Risk:** Interactions between axes may defeat the factorial budget; conclusions may depend on the real-domain lighting.
- **Cluster:** AmbigSeg

### B-0072
- **One-sentence idea:** Separate steam/water vapor from smoke using condensation dynamics — the characteristic dissipation, buoyancy, and boundary-evolution differences over seconds-scale windows.
- **Problem:** Industrial and kitchen deployments drown in steam false alarms; single-frame appearance of steam and light smoke is genuinely near-identical, and current systems either alarm on both or are detuned into uselessness.
- **Core Hypothesis:** Steam exhibits faster edge dissipation and different buoyant-plume evolution than combustion smoke, and a temporal model on seconds-scale clips separates them with high accuracy where frame-based models are at chance.
- **Why Important:** Steam confusion is the top practical complaint about vision-based smoke detection in industrial settings.
- **Why Possibly Novel:** Steam-vs-smoke is mentioned as a failure mode everywhere but has never been made a dedicated benchmark with a physics-motivated temporal solution.
- **Minimal Experiment:** Capture paired steam (kettles, showers, vents) and smoke (controlled burns, incense) clips across distances; test frame vs. clip models; report the temporal gain. Falsified if frame models already separate them.
- **Main Risk:** Distance/resolution limits temporal cues; mixed steam+smoke scenes remain hard.
- **Cluster:** AmbigSeg

### B-0073
- **One-sentence idea:** For static cameras, learn a background radiance model and detect smoke as the residual consistent with a scattering forward model — self-supervised, no smoke masks needed.
- **Problem:** Supervised smoke segmentation needs annotation that is ill-posed (see B-0061); meanwhile fixed surveillance cameras observe their own smoke-free background for thousands of hours — an unexploited self-supervision source.
- **Core Hypothesis:** Modeling observed frames as background attenuated and airlight-shifted per a single-scattering model (I = B·t + A·(1−t)) allows recovering transmittance t without labels, and this zero-annotation detector approaches supervised performance on static-camera benchmarks.
- **Why Important:** Static cameras are the deployment reality (wildfire towers, industrial CCTV); annotation-free onboarding per camera is the scalable path.
- **Why Possibly Novel:** Background subtraction and dehazing exist separately; welding them into a per-camera self-supervised smoke transmittance estimator with a falsifiable comparison to supervised models is new.
- **Minimal Experiment:** On public static-camera smoke videos, fit background model from clean footage, invert scattering model; compare to a supervised baseline on the same clips. Falsified if the inversion is far below supervised.
- **Main Risk:** Illumination changes and moving objects violate the background model; airlight A estimation is fragile at night.
- **Cluster:** AmbigSeg

### B-0074
- **One-sentence idea:** Repurpose pretrained dehazing networks' transmission-map estimators as zero-shot smoke segmenters, testing whether dehazing is secretly the strongest smoke prior available.
- **Problem:** Smoke segmentation and dehazing communities are disjoint; dehazing models are trained on vast haze data to estimate exactly the quantity (transmittance) that smoke segmentation needs, yet are never evaluated as smoke perceivers.
- **Core Hypothesis:** Transmission maps from off-the-shelf dehazing models, thresholded/calibrated on a handful of images, rival dedicated supervised smoke segmenters on thin-smoke regimes — and fusing both wins overall.
- **Why Important:** If true, the smoke field inherits years of dehazing progress for free; if false, it establishes that smoke ≠ haze in a measurable way.
- **Why Possibly Novel:** This cross-field transfer evaluation appears never to have been run; it is a genuinely cheap, decisive experiment either way.
- **Minimal Experiment:** Run 3 public dehazing models on 2 smoke segmentation benchmarks; calibrate threshold on 10 images; compare against published supervised results. Days of work, zero training.
- **Main Risk:** Dehazing models assume global atmospheric haze and may fail structurally on localized plumes.
- **Cluster:** AmbigSeg

### B-0075
- **One-sentence idea:** Supervise smoke density estimation using visibility of fiducial landmarks at known distances (industrial sites, fire ranges), converting landmark contrast loss into calibrated optical-depth labels.
- **Problem:** No in-the-wild ground truth for smoke density exists; safety decisions (evacuation visibility thresholds) need calibrated optical depth, which hand-drawn masks cannot provide.
- **Core Hypothesis:** Contrast attenuation of known high-contrast fiducials (via Koschmieder-type relations) yields per-sightline optical-depth labels accurate enough to train a dense density regressor that interpolates between sightlines.
- **Why Important:** Moves smoke perception from "is there smoke" to "how bad is it" — the question fire-safety engineering actually asks.
- **Why Possibly Novel:** Visibility meters and fiducials are standard in fire engineering; nobody has closed the loop into dense-prediction training labels.
- **Minimal Experiment:** Instrument a controlled burn or fog chamber with printed fiducials at surveyed distances; derive labels; train and validate against transmissometer readings on held-out sightlines. Falsified if fiducial-derived labels disagree with instruments.
- **Main Risk:** Sparse sightlines may under-constrain dense interpolation; illumination variation contaminates contrast measurements.
- **Cluster:** AmbigSeg

### B-0076
- **One-sentence idea:** Inject buoyant-plume physics (rise, bend-over under wind, entrainment growth rates) as a structured shape prior for aerial/tower wildfire smoke segmentation.
- **Problem:** Distant wildfire plumes occupy few pixels with cloud-like texture; appearance models confuse them with clouds and haze, ignoring that plume geometry obeys well-characterized fluid-dynamics scaling laws that clouds do not.
- **Core Hypothesis:** Constraining or scoring detections against plume-shape families (parameterized by buoyancy flux and wind) reduces cloud false positives substantially at fixed sensitivity, especially for small distant plumes where texture is uninformative.
- **Why Important:** Early wildfire detection at maximum range is exactly the small-plume regime where current systems fail.
- **Why Possibly Novel:** Plume-rise models are standard in atmospheric science; their use as a generative prior or verification stage in learned smoke detection is essentially untried.
- **Minimal Experiment:** Fit plume-geometry likelihood as a post-hoc re-scorer on an existing detector's outputs over public wildfire camera data; measure the FP/sensitivity tradeoff shift. No retraining. Falsified if geometry scoring doesn't move the ROC.
- **Main Risk:** Terrain-driven plume distortion and multiple merged plumes break the parametric families.
- **Cluster:** AmbigSeg

### B-0077
- **One-sentence idea:** Distill thermal-camera supervision (which sees through smoke and sees fire directly) into RGB-only fire/smoke models via co-mounted capture rigs.
- **Problem:** Thermal cameras solve much of fire perception but are too expensive for mass deployment; RGB models lack any supervision about what is actually burning behind the smoke they see.
- **Core Hypothesis:** Cross-modal distillation from co-registered thermal to RGB (thermal-derived fire masks and through-smoke structure as targets) yields RGB models that localize fire cores and occluded structure measurably better than RGB-label-trained models, at zero deployment cost.
- **Why Important:** Multiplies the value of a few instrumented capture campaigns into fleet-wide cheap-camera improvements.
- **Why Possibly Novel:** Cross-modal distillation is standard for depth; the thermal→RGB fire/smoke instance with through-occlusion targets is an open, high-value application.
- **Minimal Experiment:** One co-mounted RGB+thermal capture campaign at controlled burns; distill; evaluate RGB-only model on held-out burns against RGB-supervised baseline. Falsified if distillation adds nothing an RGB label couldn't.
- **Main Risk:** Registration errors between modalities; thermal supervision may teach cues absent in RGB (unlearnable targets).
- **Cluster:** AmbigSeg

### B-0078
- **One-sentence idea:** Build a hard-negative stress benchmark for fire segmentation (sunsets, sodium lights, reflections, red foliage, welding) and show that radiometric cues from HDR/raw capture separate what tone-mapped RGB cannot.
- **Problem:** Published fire segmentation numbers come from benchmarks nearly devoid of the confusers that dominate real false alarms; models compete on saturated positives while the deployment-limiting negatives are unmeasured.
- **Core Hypothesis:** State-of-the-art fire models collapse on a curated confuser set (large FP rates), and much of the gap is recoverable from radiometric information (absolute radiance, saturation structure) that tone mapping destroys.
- **Why Important:** Re-anchors the field's evaluation to the actual deployment failure mode; the radiometric claim points to a concrete sensor-pipeline fix.
- **Why Possibly Novel:** Confuser-focused benchmarks exist in face anti-spoofing and elsewhere; fire/smoke lacks one, and the tone-mapping-destroys-evidence hypothesis is untested.
- **Minimal Experiment:** Assemble ~2k confuser images/clips (public footage + captures); evaluate 3 public fire models; capture a raw/HDR subset to test the radiometric-recovery claim. Falsified if models already handle confusers or raw adds nothing.
- **Main Risk:** Licensing/collection effort for diverse confusers; raw capture subset is small.
- **Cluster:** AmbigSeg

### B-0079
- **One-sentence idea:** Train fire/smoke perception directly on raw sensor data (pre-ISP), hypothesizing that ISP processing (white balance, tone mapping, denoising) destroys the radiometric signatures of combustion.
- **Problem:** Camera ISPs optimize for human viewing, normalizing away absolute intensity and color ratios; fire's distinguishing physics (blackbody-like spectrum, extreme radiance) is partially erased before the model ever sees the pixels.
- **Core Hypothesis:** Raw-domain models will show better fire/no-fire discrimination on radiance-critical confusers (reflections, lit windows, sunsets) than sRGB models trained on the same scenes, and the gap will localize to ISP stages identifiable by ablating the ISP pipeline stage by stage.
- **Why Important:** If ISP is the bottleneck, the fix is a firmware/data-pipeline change, not endless data collection.
- **Why Possibly Novel:** Raw-domain vision is studied for low-light and detection generally; the ISP-ablation methodology applied to combustion signatures is specific and new.
- **Minimal Experiment:** Capture paired raw+sRGB of flames and confusers with one camera; train matched small models; run the ISP-stage ablation. Falsified if sRGB models match raw.
- **Main Risk:** Raw data availability at scale; cross-sensor raw generalization is poor.
- **Cluster:** AmbigSeg

### B-0080
- **One-sentence idea:** Detect glass surfaces from the parallax behavior of specular highlights under small camera motion — highlights move against the background flow — as a self-supervised video cue.
- **Problem:** Static appearance of clean glass is nearly nonexistent; models depend on frames and context. Yet any moving camera generates a physical signature (highlight motion inconsistent with scene flow) that current methods ignore.
- **Core Hypothesis:** A two-frame model fed optical flow + image will learn to localize glass from flow anomalies of specularities and transmitted-layer motion differences, trained purely with self-supervised photometric-consistency violations as pseudo-labels, approaching supervised single-frame accuracy without labels.
- **Why Important:** Robots and AR devices always have small camera motion available; exploiting it makes glass perception label-free.
- **Why Possibly Novel:** Reflection removal uses layer-motion differences; converting the same physics into a self-supervised glass segmenter with quantitative benchmark comparison is an open construction.
- **Minimal Experiment:** On existing video/RGB-D datasets containing glass, derive flow-anomaly pseudo-labels, train, and evaluate against a labeled glass benchmark. Falsified if flow anomalies are too sparse/noisy to train from.
- **Main Risk:** Textureless backgrounds give no flow to be anomalous against; motion blur corrupts the cue.
- **Cluster:** AmbigSeg

### B-0081
- **One-sentence idea:** Segment glass scenes into transmitted vs. reflected content (what is behind the glass vs. mirrored) as a three-way dense decomposition, since downstream tasks need the distinction, not just "glass here."
- **Problem:** Existing glass segmentation stops at the pane; robots looking through windows treat reflections as real obstacles and transmitted objects as unreachable — both errors stem from collapsing physically distinct layers into one label.
- **Core Hypothesis:** A model trained on composited (transmitted, reflected, direct) decompositions transfers to real windows well enough to cut reflection-induced false obstacles in a downstream navigation-style evaluation by a large factor.
- **Why Important:** Windows and glass doors are ubiquitous in indoor robotics; the transmitted/reflected confusion is a concrete safety failure.
- **Why Possibly Novel:** Reflection separation exists as image restoration; recasting it as a labeled dense decomposition tied to a downstream robotics metric is an unoccupied framing.
- **Minimal Experiment:** Composite training data from paired scenes (capture behind-glass and reflected-scene separately, blend physically); test on real windows with manually verified layer labels; measure downstream false-obstacle rate. Falsified if compositing doesn't transfer.
- **Main Risk:** Real glass has spatially varying reflectance and dirt; two-layer compositing may undershoot complexity.
- **Cluster:** AmbigSeg

### B-0082
- **One-sentence idea:** Recover 3D smoke occupancy from sparse multi-view cameras (differentiable volumetric rendering with a scattering model), making segmentation a 2D projection of an estimated 3D medium.
- **Problem:** Per-view 2D smoke masks are viewpoint-inconsistent and cannot support 3D-grounded decisions (where is the smoke, is the corridor passable); multi-camera sites have the views but no method fuses them physically.
- **Core Hypothesis:** Joint estimation of a low-resolution emission/extinction volume from ≥3 calibrated views, via differentiable single-scatter rendering, produces per-view segmentations that are more accurate and more temporally stable than independent 2D models, and yields usable 3D plume localization.
- **Why Important:** Industrial sites and buildings already have multi-camera coverage; 3D smoke maps are what evacuation and HVAC control actually need.
- **Why Possibly Novel:** NeRF-style media reconstruction exists offline for graphics; a coarse, fast, safety-oriented version with quantitative 2D/3D evaluation against staged releases is unbuilt.
- **Minimal Experiment:** Fog-machine releases in a room with 4 calibrated cameras and a few in-room density sensors; compare per-view masks and 3D localization against sensors and per-view baselines. Falsified if fusion doesn't beat per-view models.
- **Main Risk:** Calibration drift and highly dynamic media may break slow volumetric optimization; needs a fast amortized variant.
- **Cluster:** AmbigSeg

### B-0083
- **One-sentence idea:** Transfer fuzzy-media segmentation machinery (opacity regression, soft-boundary metrics) to ground-glass opacities in lung CT, treating GGO as "smoke inside the body."
- **Problem:** GGO delineation suffers exactly the binary-mask ill-posedness of smoke — graded density with no true edge — yet the medical community uses hard masks and Dice, with notorious inter-rater chaos on GGO extent.
- **Core Hypothesis:** Density-regression formulations (predicting attenuation deviation from expected parenchyma rather than a mask) will show higher inter-rater-consistent evaluation and better longitudinal sensitivity to change than binary GGO masks.
- **Why Important:** GGO burden drives ILD and infection severity scoring; a formulation matched to the physics could change clinical quantification.
- **Why Possibly Novel:** The explicit methodological bridge between participating-media vision and GGO quantification, with a formulation-comparison experiment, appears unmade.
- **Minimal Experiment:** On public ILD/pneumonia CT with multi-rater masks, compare binary training vs. density regression on held-out-rater agreement and on synthetic longitudinal change detection. Falsified if binary masks are equally consistent.
- **Main Risk:** Attenuation baselines vary with inspiration level and scanner, confounding density labels.
- **Cluster:** AmbigSeg

### B-0084
- **One-sentence idea:** Model ultrasound acoustic shadows as first-class ambiguous regions: jointly predict shadow maps (from attenuation physics) and shadow-aware anatomy segmentation with explicit "no-evidence" outputs.
- **Problem:** Ultrasound networks confidently hallucinate anatomy inside acoustic shadows where there is physically no signal; standard training punishes honest abstention because labels exist everywhere.
- **Core Hypothesis:** Jointly estimating shadow probability (self-supervised from beam-direction attenuation modeling) and gating segmentation confidence on it reduces hallucinated-structure errors inside shadows while leaving unshadowed performance intact — measurable via shadow-stratified evaluation.
- **Why Important:** Shadow hallucination is a silent, clinically dangerous ultrasound failure that current benchmarks average away.
- **Why Possibly Novel:** Shadow detection exists as a niche task; coupling it into segmentation as a physics-derived evidence gate with shadow-stratified metrics is an untested mechanism.
- **Minimal Experiment:** Annotate shadow regions on a public ultrasound set (cheap — shadows are easy to label); evaluate existing models shadow-stratified; train gated model. Falsified if models don't actually hallucinate in shadows.
- **Main Risk:** Distinguishing shadow from genuinely hypoechoic tissue is itself uncertain.
- **Cluster:** AmbigSeg

### B-0085
- **One-sentence idea:** Harvest free supervision from surveillance timelapses that capture the same static scene with and without smoke, using the clean frame as the known background in a compositing model.
- **Problem:** In-the-wild smoke annotation is scarce and ill-posed, yet wildfire and industrial cameras record millions of before/during pairs of identical scenes — a physically exploitable pairing that current training pipelines ignore.
- **Core Hypothesis:** Given a co-registered clean background frame, per-pixel transmittance can be estimated analytically (up to airlight), yielding pseudo-labels at scale whose quality is sufficient to train models that beat those trained on hand-drawn masks from the same footage.
- **Why Important:** Turns existing camera archives into a self-labeling smoke corpus orders of magnitude larger than any annotated dataset.
- **Why Possibly Novel:** Paired-scene supervision is used in shadow/reflection research; the smoke instantiation with a hand-label-vs-derived-label showdown is new.
- **Minimal Experiment:** From public wildfire-camera archives, auto-mine before/during pairs; derive transmittance labels; train and compare against mask-trained baselines on a held-out annotated set. Falsified if derived labels underperform hand masks.
- **Main Risk:** Illumination differences between before/during frames corrupt the derivation; needs illumination normalization.
- **Cluster:** AmbigSeg

### B-0086
- **One-sentence idea:** Build a diagnostic taxonomy-benchmark that decomposes "hard segmentation" by boundary-evidence type (transparent, translucent-media, camouflage, shadow, motion-blur) and tests whether methods fail differently per type.
- **Problem:** Transparent, smoke, camouflage, and shadow segmentation are studied by separate communities with separate benchmarks; whether their difficulties are one phenomenon or several is unknown, so methods claiming "hard-case robustness" are unfalsifiable.
- **Core Hypothesis:** Failure modes cluster by evidence type, not by dataset — models strong on camouflage will not transfer to translucency — implying the field needs evidence-type-specific mechanisms rather than general "hard-case" methods.
- **Why Important:** A diagnostic axis would organize a fragmented literature and expose which "general" methods are actually general.
- **Why Possibly Novel:** Cross-benchmark meta-evaluations exist elsewhere; an evidence-type-controlled diagnostic suite for ambiguous segmentation is unbuilt.
- **Minimal Experiment:** Assemble type-pure subsets from existing public benchmarks; evaluate 6 published methods in a full crossover; test the failure-clustering hypothesis statistically. No training required.
- **Main Risk:** Type purity is hard to guarantee; datasets confound type with domain (indoor/outdoor).
- **Cluster:** AmbigSeg

### B-0087
- **One-sentence idea:** Output nested core/extent masks for fuzzy objects — a certain inner core and a maximal outer extent — and annotate datasets this way, which is cheaper and better-posed than single-contour annotation.
- **Problem:** Single-contour annotation of smoke/flames forces annotators to make an arbitrary call, is slow because of that deliberation, and hides the information downstream users need (both "definitely smoke" and "possibly smoke" regions).
- **Core Hypothesis:** Nested-mask annotation is faster per image (less deliberation) and more inter-annotator-consistent than single contours, and models trained on nested targets provide operating-point flexibility that improves both high-precision and high-recall deployment modes.
- **Why Important:** Cheaper, more consistent annotation plus better deployment semantics — a Pareto improvement in the data pipeline itself.
- **Why Possibly Novel:** Interval/band-style annotation has precedent in other fields (e.g., ordinal bounds) but has not been proposed or validated for fuzzy-object vision annotation.
- **Minimal Experiment:** Timed annotation study (n=6 annotators, 200 images) comparing single vs. nested protocols on speed and cross-annotator agreement; train on both and compare deployment operating curves. Falsified if nested is slower or no more consistent.
- **Main Risk:** Two boundaries could be slower in practice; tooling must support it.
- **Cluster:** AmbigSeg

### B-0088
- **One-sentence idea:** Solve occlusion ordering through transparency — instance segmentation of stacked/nested glassware with correct depth ordering — using ray-traced synthetic training and real lab-glassware evaluation.
- **Problem:** Instance segmentation assumes opaque occlusion (front object hides back); with glassware, all instances are simultaneously visible and intertwined, breaking the assumptions of every mask-based instance framework, and lab-automation robots need exactly this.
- **Core Hypothesis:** An instance representation with per-pixel multi-instance membership (a pixel can belong to several transparent instances with depth order) can be trained on ray-traced scenes and transfer to real glassware, whereas standard instance heads structurally cannot express the ground truth.
- **Why Important:** Laboratory automation (pipetting, sorting glassware) is a growing robotics market blocked by this exact perception gap.
- **Why Possibly Novel:** Amodal and layered instance segmentation exist; multi-membership through transparency with depth ordering, plus a physical benchmark, is a distinct unsolved formulation.
- **Minimal Experiment:** Ray-trace nested-glassware scenes; train multi-membership head vs. standard instance head; evaluate on 100 photographed and manually layer-labeled real scenes. Falsified if standard heads cope after fine-tuning.
- **Main Risk:** Real-world dirt, liquids, and labels on glass may dominate the difficulty rather than the formulation.
- **Cluster:** AmbigSeg

### B-0089
- **One-sentence idea:** Disentangle intrinsic smoke density from illumination/background context by training on multi-illumination captures of identical plumes, forcing appearance-invariant density estimates.
- **Problem:** The same smoke looks white on dark backgrounds and dark on bright ones; models entangle background context into "smokeness," causing systematic errors when illumination geometry changes (e.g., backlit vs. frontlit plumes).
- **Core Hypothesis:** Training with same-plume multi-illumination pairs (turntable/lighting-rig captures, or timelapse sun movement) with a density-consistency loss yields estimates invariant to illumination direction, fixing the documented backlit-plume failure mode without extra labels.
- **Why Important:** Illumination-dependent failure is systematic and time-of-day-correlated — a dangerous property for safety systems that must work at all hours.
- **Why Possibly Novel:** Multi-illumination intrinsic decomposition is established for surfaces; its application to participating media with a consistency-training scheme is unexplored.
- **Minimal Experiment:** Capture plumes under controlled lighting sweeps; train with/without cross-illumination consistency; test on held-out lighting directions and real dawn/dusk footage. Falsified if standard training is already illumination-stable.
- **Main Risk:** Capturing identical plumes under multiple illuminations is physically tricky (plumes evolve); needs fast lighting switching.
- **Cluster:** AmbigSeg

### B-0090
- **One-sentence idea:** Formulate early smoke detection as sequential evidence accumulation with an explicit detection-latency-vs-false-alarm operating curve, instead of per-frame segmentation.
- **Problem:** Nascent smoke is invisible in single frames but integrates to visibility over tens of seconds; per-frame models are structurally blind to it, and the field's metrics (per-frame IoU) cannot even express "detected 40 seconds earlier."
- **Core Hypothesis:** A recurrent accumulator over stabilized frames detects staged fire onsets significantly earlier than the best per-frame model at matched false-alarm rate, and the latency-FA tradeoff curve is the correct headline metric for the field.
- **Why Important:** Every minute of earlier wildfire detection has quantifiable suppression value; latency is the true objective, currently unmeasured.
- **Why Possibly Novel:** Sequential detection theory (CUSUM-style) is classic; wiring it into learned smoke perception with onset-timestamped benchmark data would establish a new evaluation standard.
- **Minimal Experiment:** Use onset-known controlled burns and public wildfire-camera archives with first-visibility annotations; compare accumulator vs. per-frame detectors on latency at fixed FA/day. Falsified if temporal integration buys no latency.
- **Main Risk:** Camera vibration and compression artifacts may dominate the weak temporal signal at long range.
- **Cluster:** AmbigSeg
## Section 4 — Domain Adaptation & Domain Shift [B-0091–B-0120]

### B-0091
- **One-sentence idea:** Solve the test-time-adaptation model-selection problem with a label-free surrogate validation signal (cross-augmentation prediction agreement) validated against oracle selection.
- **Problem:** TTA methods have hyperparameters (learning rate, steps, momentum) that in papers are tuned with labeled target data — unavailable by definition in deployment — so reported TTA gains may be unrealizable in practice.
- **Core Hypothesis:** Agreement between predictions under semantically neutral augmentations correlates strongly with target accuracy across TTA hyperparameter settings, allowing label-free selection that retains most of the oracle-selected gain.
- **Why Important:** Without a selection mechanism, TTA is not deployable at all; this is the field's unglamorous but binding bottleneck.
- **Why Possibly Novel:** Surrogate validation is studied for UDA checkpoint selection; a systematic instrument for TTA hyperparameter selection with retained-gain quantification is missing.
- **Minimal Experiment:** For 3 TTA methods × 4 segmentation shift benchmarks, sweep hyperparameters, compute surrogate-accuracy correlation, and report gain retained under surrogate vs. oracle selection. No new methods needed. Falsified if correlation is weak.
- **Main Risk:** Surrogate may fail exactly under large shift, where selection matters most.
- **Cluster:** DomainAdapt

### B-0092
- **One-sentence idea:** Characterize the conditions under which entropy-minimization TTA collapses (class imbalance, small batches, long streams) and build a cheap online diagnostic that switches adaptation off before collapse.
- **Problem:** Entropy-based TTA can catastrophically collapse to predicting dominant classes, and practitioners discover this only after silent failure; the collapse conditions are anecdotal, not characterized.
- **Core Hypothesis:** Collapse onset is preceded by measurable early-warning signals (entropy variance shrinkage, prediction-distribution drift rate) that a monitor can detect with enough lead time to freeze adaptation, and the collapse boundary is a reproducible function of batch size and class skew.
- **Why Important:** Deployment safety of the entire TTA family hinges on knowing when it is unsafe.
- **Why Possibly Novel:** Collapse is mentioned as a caveat everywhere but has no systematic phase-diagram study or validated early-warning monitor for dense prediction.
- **Minimal Experiment:** Grid over batch size × class skew × stream length on a segmentation shift benchmark; map collapse frequency; train monitor on half the grid, test lead time on the other half. Falsified if collapse is unpredictable.
- **Main Risk:** Early-warning signals may be method-specific, limiting generality.
- **Cluster:** DomainAdapt

### B-0093
- **One-sentence idea:** Disentangle covariate shift from label-distribution shift in BN-statistic adaptation: recalibrating BN on target batches silently conflates the two and mis-adapts when class prevalence differs.
- **Problem:** BN-stat recalibration — the cheapest, most-used adaptation — assumes feature-statistic changes reflect appearance shift; when the target simply contains more pathology (label shift), recalibration "corrects" statistics that were right, degrading exactly the abnormal cases.
- **Core Hypothesis:** Decomposing target-batch statistics into class-conditional components (via the model's own posteriors) and recalibrating only the class-conditional means/variances beats naive BN adaptation whenever label shift co-occurs with covariate shift, with the gap growing in prevalence difference.
- **Why Important:** Real clinical sites differ in both scanner and case-mix simultaneously — the exact regime where the standard trick backfires.
- **Why Possibly Novel:** BN adaptation and label-shift correction are separate literatures; their interaction in dense prediction is undiagnosed.
- **Minimal Experiment:** Construct target sets with controlled prevalence (resampling public data) × scanner shift; compare naive vs. class-conditional BN recalibration. Falsified if naive BN is robust to prevalence.
- **Main Risk:** Class-conditional statistics estimated from wrong posteriors may self-reinforce errors.
- **Cluster:** DomainAdapt

### B-0094
- **One-sentence idea:** Measure the drift half-life of continual test-time adaptation on long realistic streams and fix accumulation with source-statistic anchoring plus stochastic parameter restoration.
- **Problem:** Continual TTA accumulates errors over hours/days of deployment streams; papers evaluate on short shuffled sequences, hiding the drift that kills real systems.
- **Core Hypothesis:** Adaptation quality decays with a characteristic half-life determined by update magnitude and stream autocorrelation, and anchoring (penalizing deviation from source statistics) plus random partial weight restoration extends the half-life by an order of magnitude at negligible peak cost.
- **Why Important:** The gap between benchmark TTA and deployable TTA is precisely long-horizon stability.
- **Why Possibly Novel:** Some works add restoration heuristics; a quantitative drift-kinetics framing (half-life as a function of stream statistics) with predictive power is new.
- **Minimal Experiment:** Build day-long realistic streams (ordered by acquisition time from public multi-site data); measure decay curves for 3 continual-TTA methods ± anchoring. Falsified if no systematic decay exists.
- **Main Risk:** Realistic long streams with ground truth are scarce; may need semi-synthetic stream construction.
- **Cluster:** DomainAdapt

### B-0095
- **One-sentence idea:** Empirically decompose cross-site medical performance drop into scanner, protocol, and population components using matched-cohort counterfactual datasets.
- **Problem:** "Domain shift" is treated as one blob; sites differ simultaneously in hardware, acquisition protocol, and patient population, and no one knows which component dominates — so mitigation investment (harmonization vs. rebalancing vs. adaptation) is blind.
- **Core Hypothesis:** The decomposition is measurable using natural experiments (same scanner model at different sites, protocol changes within a site, traveling-subject data), and scanner/protocol effects will dominate population effects for segmentation (unlike for classification) — a falsifiable, decision-guiding claim.
- **Why Important:** Directs the entire field's robustness effort toward the component that actually matters.
- **Why Possibly Novel:** Harmonization literature measures scanner effects on features; a causal decomposition of segmentation performance drop with matched cohorts has not been assembled.
- **Minimal Experiment:** Curate matched pairs from public multi-site datasets (same-scanner/different-site, same-site/protocol-change); evaluate fixed models across the grid; variance-decompose. No training. Falsified if components are inseparable in available data.
- **Main Risk:** Public data may not contain enough matched structure; confounding may be irreducible.
- **Cluster:** DomainAdapt

### B-0096
- **One-sentence idea:** Establish a "shift-type → adaptation-locus" law: appearance shifts are correctable by normalization-layer adaptation alone, while geometric shifts require spatial-module adaptation, tested via controlled factorial shifts.
- **Problem:** Practitioners choose what to adapt (norm layers, adapters, full model) by habit; failures are attributed to methods when the real issue is adapting the wrong parameter subset for the shift type.
- **Core Hypothesis:** There is a reproducible correspondence between shift type and minimal sufficient adaptation locus, such that a cheap shift-type classifier can route to the right locus and match full-model adaptation at a fraction of the risk and compute.
- **Why Important:** Converts adaptation configuration from folklore into a decision rule, and reduces overfitting risk by adapting fewer parameters.
- **Why Possibly Novel:** Parameter-subset adaptation studies exist piecemeal; the factorial shift-type × locus experiment and the routing rule are not established.
- **Minimal Experiment:** Construct pure appearance shifts (intensity/kernel simulation) and pure geometric shifts (spacing/FOV changes) on one dataset; adapt each locus; build the correspondence table. Falsified if locus doesn't interact with shift type.
- **Main Risk:** Real shifts are mixtures; the routing rule must handle composition.
- **Cluster:** DomainAdapt

### B-0097
- **One-sentence idea:** Show that global Fourier-amplitude-swap adaptation fails on spatially localized domain differences (artifacts, coils, shading) and replace it with spatially windowed frequency alignment.
- **Problem:** Fourier-based domain alignment assumes domain style is a global spectral property; MRI bias fields, CT ring artifacts, and vignetting are local, so global amplitude swapping both under-corrects locally and corrupts clean regions.
- **Core Hypothesis:** A windowed (patch-wise) spectral alignment with spatial regularization outperforms global swapping specifically on datasets whose shift is localized, and the local-vs-global gap predicts which real datasets have localized shift — making the method also a diagnostic.
- **Why Important:** Fourier adaptation is popular for its simplicity; knowing its failure boundary and having an equally simple fix keeps the simplicity while removing the blind spot.
- **Why Possibly Novel:** The localized-shift failure mode of spectral methods is unarticulated; the windowed variant with diagnostic interpretation is a concrete step beyond.
- **Minimal Experiment:** Synthesize localized shifts (bias fields, rings) vs. global shifts; compare global and windowed spectral alignment; then apply to 3 real cross-site pairs. Falsified if global swapping handles local shifts fine.
- **Main Risk:** Windowing introduces seam artifacts and more hyperparameters.
- **Cluster:** DomainAdapt

### B-0098
- **One-sentence idea:** Separate geometric domain shift (field-of-view, patient positioning, spacing) from appearance shift in DA benchmarks, and develop adaptation that re-estimates spatial priors rather than restyling intensities.
- **Problem:** Virtually all segmentation DA methods restyle appearance; when the true shift is geometric (different FOV cropping, prone vs. supine positioning), style methods do nothing, yet benchmarks never isolate this axis, so the blind spot is invisible.
- **Core Hypothesis:** On geometry-dominant shifts, appearance-DA methods provide ≈zero gain while a spatial-prior re-estimation approach (re-fitting expected organ layout via coarse target-side registration statistics) recovers most of the drop — demonstrating the field has been solving only half the problem.
- **Why Important:** Geometric shift is pervasive in practice (protocol FOV differences are universal) and completely unaddressed.
- **Why Possibly Novel:** The appearance/geometry axis decomposition of segmentation DA, with a geometry-specific mechanism, is essentially virgin territory.
- **Minimal Experiment:** Build geometry-shift-only splits (recrop/reposition public data realistically); run 4 popular DA methods; implement spatial-prior re-estimation. Falsified if appearance methods handle geometric shift anyway.
- **Main Risk:** Realistic geometric shift simulation must avoid trivial artifacts models could exploit.
- **Cluster:** DomainAdapt

### B-0099
- **One-sentence idea:** Mask pseudo-labels near predicted boundaries during self-training DA, since pseudo-label errors concentrate in boundary bands and drive error accumulation.
- **Problem:** Self-training UDA treats pseudo-label confidence pixel-independently; boundary pixels are systematically wrong under shift, get confidently pseudo-labeled anyway, and imprint the source model's boundary bias irreversibly onto the target model.
- **Core Hypothesis:** Excluding a distance-to-boundary band from pseudo-label supervision (band width set by shift magnitude) improves final target boundary accuracy, because interiors carry enough signal to adapt and boundaries are re-learned from adapted features rather than copied errors.
- **Why Important:** Boundary quality is exactly what segmentation is for; current self-training quietly sacrifices it.
- **Why Possibly Novel:** Confidence thresholding is standard; the spatial-structure-of-error insight (band exclusion, width as a function of shift) is a specific untested mechanism.
- **Minimal Experiment:** On one synthetic-to-real and one cross-site benchmark, sweep band widths in self-training; compare boundary-F and Dice against confidence-threshold baselines at matched supervision volume. Falsified if band masking underperforms confidence masking.
- **Main Risk:** For thin structures the band may swallow the whole object, requiring size-adaptive bands.
- **Cluster:** DomainAdapt

### B-0100
- **One-sentence idea:** Open-set domain adaptation for segmentation: detect and abstain on target-domain regions belonging to classes absent from the source label space, rather than force-labeling them.
- **Problem:** UDA methods assume identical label spaces; real target domains contain novel classes (new pathology, new objects) that current methods confidently mislabel as their nearest source class — an error mode benchmarks are designed not to see.
- **Core Hypothesis:** Joint adaptation + novelty estimation (novelty scored against adapted features, not source features) can maintain closed-set accuracy while flagging most novel-class pixels, whereas post-hoc OOD detectors on adapted models fail because adaptation itself warps novelty scores.
- **Why Important:** Silent mislabeling of never-seen classes is a safety-critical failure in both driving and medical deployment.
- **Why Possibly Novel:** Open-set DA exists for classification; the dense version with the "adaptation warps novelty" interaction is unexplored.
- **Minimal Experiment:** Remove classes from source label space on a driving benchmark; run UDA; measure novel-class mislabeling with and without joint novelty estimation. Falsified if post-hoc OOD on adapted models suffices.
- **Main Risk:** Novelty vs. shifted-known-class distinction may be fundamentally ambiguous at the pixel level.
- **Cluster:** DomainAdapt

### B-0101
- **One-sentence idea:** Active domain adaptation for segmentation that selects target regions (not images) to annotate, scored by the product of domain-discrepancy and decision-uncertainty.
- **Problem:** A tiny target-annotation budget usually beats elaborate UDA, but current active-DA selects whole images, wasting budget on regions the source model already handles; region-level selection under domain shift lacks a principled score.
- **Core Hypothesis:** Regions that are simultaneously domain-atypical (high feature-space discrepancy from source) and decision-uncertain contribute most per annotated pixel; the product score beats uncertainty-only and discrepancy-only selection at every budget, with the advantage largest at small budgets.
- **Why Important:** In practice every deployment has a small labeling budget; per-pixel efficiency of that budget is the real currency.
- **Why Possibly Novel:** Active DA exists at image level; the region-level product-scoring hypothesis with budget curves is a concrete, testable refinement.
- **Minimal Experiment:** On two cross-domain segmentation pairs, simulate region-annotation budgets {0.1%, 1%, 5%}; compare selection scores. Falsified if uncertainty-only matches the product score.
- **Main Risk:** Region-level annotation cost models may not reflect real annotator time (context switching costs).
- **Cluster:** DomainAdapt

### B-0102
- **One-sentence idea:** Train a "shift meter" that predicts, per case, whether test-time adaptation will improve or harm the prediction — before running it — enabling selective adaptation.
- **Problem:** TTA helps on some cases and actively harms others; deployments must currently choose all-or-nothing, and the harmed cases are unpredictable, making TTA a liability in regulated settings.
- **Core Hypothesis:** The sign of TTA's effect is predictable from pre-adaptation observables (feature-statistic distance, prediction entropy profile, augmentation disagreement) with enough accuracy that selective adaptation dominates both always-adapt and never-adapt policies.
- **Why Important:** Converts TTA from a gamble into a controlled intervention — likely the difference between research technique and deployed tool.
- **Why Possibly Novel:** Predicting adaptation benefit per-case is essentially unstudied; existing work predicts accuracy, not the delta from adaptation.
- **Minimal Experiment:** On multi-site medical data, run TTA per case, record deltas, train delta-sign predictor on half the sites, test on held-out sites. Falsified if the delta is unpredictable across sites.
- **Main Risk:** Delta-sign may depend on TTA method specifics, requiring per-method meters.
- **Cluster:** DomainAdapt

### B-0103
- **One-sentence idea:** Audit which self-supervised auxiliary losses actually correlate with segmentation improvement in single-image test-time training, across shift types — and expose anti-correlated ones.
- **Problem:** Test-time training assumes minimizing an auxiliary self-supervised loss (rotation, contrastive, reconstruction) improves the main task on the test sample, but this coupling is an article of faith; for dense prediction under some shifts it may be zero or negative.
- **Core Hypothesis:** Auxiliary-main coupling is shift-type-dependent and auxiliary-task-dependent, with reconstruction-type losses anti-correlated under artifact-driven shifts (the model "fixes" the artifact instead of the segmentation); a coupling-map would tell practitioners which auxiliary to trust when.
- **Why Important:** TTT is widely used for single-sample medical adaptation where its failure is invisible; a coupling map prevents silent harm.
- **Why Possibly Novel:** Individual TTT papers report successes; a systematic coupling audit across auxiliary tasks × shift types for segmentation does not exist.
- **Minimal Experiment:** For one model, 4 auxiliary heads, 5 controlled shift types: per-case scatter of auxiliary-loss improvement vs. Dice change. Pure measurement. Falsified if coupling is uniformly positive.
- **Main Risk:** Findings may be architecture-specific; needs at least two backbones.
- **Cluster:** DomainAdapt

### B-0104
- **One-sentence idea:** Quantify lesion erasure/hallucination in GAN-based cross-domain image translation for segmentation DA, and prevent it with patch-level content-preservation contrastive constraints evaluated on lesion recall.
- **Problem:** Translation-based DA (CycleGAN-style) is known anecdotally to delete or invent small lesions — the content that matters most — but the field lacks a lesion-preservation metric and keeps publishing translation DA validated only on organ-level Dice.
- **Core Hypothesis:** Standard translation loses a substantial fraction of small lesions (measurable by lesion-matched recall through the translation), and a lesion-scale contrastive preservation term restores most of it with minor style-fidelity cost.
- **Why Important:** If translation silently erases pathology, translation-based DA pipelines are clinically dangerous regardless of their Dice.
- **Why Possibly Novel:** Content preservation is discussed generically; a lesion-recall-through-translation metric and targeted fix make it concrete and falsifiable.
- **Minimal Experiment:** Translate lesion-annotated volumes across a public cross-modality pair; measure lesion visibility before/after via a fixed detector; add preservation term and re-measure. Falsified if lesions survive translation fine.
- **Main Risk:** The fixed detector used for measurement may itself be domain-sensitive (needs careful control).
- **Cluster:** DomainAdapt

### B-0105
- **One-sentence idea:** Replace learned style transfer with physics-derived acquisition mappings (e.g., CT kernel changes as measurable convolution kernels) for adaptation across reconstruction protocols.
- **Problem:** Learned translation can hallucinate; yet for many protocol shifts the transformation is not unknown — it is physics with estimable parameters (kernel PSFs, dose noise models) — and the field uses GANs where a deterministic operator exists.
- **Core Hypothesis:** For kernel/dose/sequence-parameter shifts, physics-estimated mappings (fit from phantom or paired-reconstruction data) beat learned translation in downstream segmentation while being invertible and hallucination-free, and the residual gap identifies which shifts are genuinely non-physical.
- **Why Important:** Deterministic, auditable adaptation is qualitatively safer for regulated deployment than generative translation.
- **Why Possibly Novel:** Physics harmonization exists in radiomics; wiring estimated acquisition operators into segmentation DA with a head-to-head against GAN translation is untested.
- **Minimal Experiment:** Use paired-kernel public CT reconstructions: fit kernel mapping, compare against CycleGAN-style translation on segmentation transfer. Falsified if learned translation wins even on pure kernel shift.
- **Main Risk:** Many real shifts mix physical and non-physical components; scope must be honestly bounded.
- **Cluster:** DomainAdapt

### B-0106
- **One-sentence idea:** Adapt label-shift correction (prevalence reweighting via confusion-matrix EM) to dense segmentation outputs, correcting for sites whose pathology prevalence differs from the training distribution.
- **Problem:** A model trained where 30% of cases have tumors is miscalibrated at a screening site with 2% prevalence; classification has established label-shift corrections, but pixels are not IID samples and no dense analog exists — so deployed models carry systematic prevalence bias.
- **Core Hypothesis:** A region-level (connected-component) formulation of label-shift EM — estimating target prevalence from aggregated component-level posteriors — reduces false-positive burden at low-prevalence sites without retraining, outperforming naive global threshold tuning.
- **Why Important:** Prevalence mismatch between development and deployment is universal in screening applications and currently handled by ad-hoc threshold fiddling.
- **Why Possibly Novel:** Dense-prediction label-shift correction with a component-level likelihood model appears to be an open formalization.
- **Minimal Experiment:** Resample a public lesion dataset into prevalence-shifted "sites"; apply component-level EM vs. threshold tuning; measure FP/FN balance recovery. Falsified if global threshold tuning is already optimal.
- **Main Risk:** Component-level independence assumptions may be too wrong for clustered pathology.
- **Cluster:** DomainAdapt

### B-0107
- **One-sentence idea:** Benchmark TTA under honest single-patient streaming (batch=1, no shuffling, no test-set reuse) and expose how much published gain depends on unrealistic batch composition.
- **Problem:** TTA evaluations use large shuffled target batches; clinical and embedded deployments see one case at a time in temporal order, and BN-based methods behave completely differently in that regime — the literature's numbers may not survive the protocol change.
- **Core Hypothesis:** A substantial fraction of published segmentation-TTA gains disappear or invert under honest streaming, and the survivors share identifiable properties (normalization-free updates, episodic resets) — yielding a practitioner's shortlist of deployment-valid methods.
- **Why Important:** Prevents the field from optimizing a fictional protocol; identifies which techniques are actually usable.
- **Why Possibly Novel:** Streaming caveats are known for classification TTA; a rigorous segmentation-specific streaming audit with a survivors' analysis has not been published.
- **Minimal Experiment:** Re-run 6 public TTA methods under batch-1 streaming on 3 shift benchmarks; compare against reported protocols. Pure re-evaluation. Falsified if gains survive streaming broadly.
- **Main Risk:** Faithful reimplementation burden; authors may dispute protocol choices (mitigate by releasing harness).
- **Cluster:** DomainAdapt

### B-0108
- **One-sentence idea:** Constrain test-time adaptation with an anatomical shape prior so that adaptation can change appearance processing but cannot push outputs off the manifold of plausible anatomy.
- **Problem:** Unconstrained TTA objectives (entropy, consistency) can be satisfied by anatomically absurd segmentations; under strong shift, adaptation drifts toward degenerate shapes with no mechanism pulling it back.
- **Core Hypothesis:** Adding a shape-plausibility term (log-likelihood under a mask autoencoder trained source-side on labels only) to the TTA objective prevents degenerate drift and converts TTA failures into graceful degradation, with the plausibility term acting as an automatic brake exactly when shift is large.
- **Why Important:** Bounded-failure adaptation is the requirement for using TTA in safety-relevant systems.
- **Why Possibly Novel:** Shape priors and TTA both exist; using the prior as a drift brake with a "failure-boundedness" evaluation criterion (worst-case, not mean, performance) is a fresh combination and metric.
- **Minimal Experiment:** On increasing synthetic shift severity, run entropy-TTA ± shape term; report worst-decile Dice trajectories. Falsified if the brake doesn't lift the worst decile.
- **Main Risk:** The prior may block legitimate adaptation on genuinely unusual anatomy.
- **Cluster:** DomainAdapt

### B-0109
- **One-sentence idea:** Restrict test-time adaptation of dense transformers to a small set of learned tokens (adaptation-by-prompt), trading peak adaptation capacity for stability and revertibility.
- **Problem:** Full-model or norm-layer TTA on transformers risks unbounded drift and cannot be instantly reverted or audited; regulators and MLOps teams need adaptation with a small, inspectable, resettable state.
- **Core Hypothesis:** Token-constrained adaptation achieves a large fraction of full-TTA gains on appearance shifts while exhibiting order-of-magnitude lower catastrophic-failure rates on long streams, and its state (a few vectors) can be cached per scanner and reused (domain memory) — a stability-capacity tradeoff worth mapping.
- **Why Important:** Provides the missing "safe mode" for adaptation in production systems.
- **Why Possibly Novel:** Prompt-based TTA exists for classification; the stability/failure-rate framing and per-scanner token caching for dense medical streams are unexplored.
- **Minimal Experiment:** Compare token-TTA vs. norm-TTA vs. full-TTA on long streams: mean gain, worst-case, failure rate, revert cost. Falsified if token adaptation is both weaker and no safer.
- **Main Risk:** Token capacity may be insufficient for geometry-flavored shifts (consistent with B-0096's law).
- **Cluster:** DomainAdapt

### B-0110
- **One-sentence idea:** Domain versioning for streaming adaptation: detect when the input distribution reverts to a previously seen state (scanner switched back, protocol restored) and reload the cached adapted state instead of re-adapting.
- **Problem:** Real deployment streams alternate among a small set of recurring conditions (scanners, protocols, day/night); continual TTA treats every change as novel, wastefully re-adapting and accumulating drift each cycle.
- **Core Hypothesis:** Lightweight domain fingerprinting (feature-statistic signatures) can match incoming data to cached adaptation states with high precision, and a version-switching policy outperforms continual adaptation on recurring-domain streams both in accuracy and in total update count (less drift exposure).
- **Why Important:** Recurrence is the actual structure of deployment streams; exploiting it is both cheaper and safer than perpetual adaptation.
- **Why Possibly Novel:** Continual TTA work assumes forward-moving domain sequences; the recurrence-and-caching formulation with fingerprint matching is a distinct systems-flavored contribution.
- **Minimal Experiment:** Build recurring-domain streams from multi-scanner public data (A-B-A-C-A…); compare continual TTA vs. fingerprint-cached switching. Falsified if continual adaptation handles recurrence gracefully already.
- **Main Risk:** Fingerprint collisions between similar domains could load wrong states (needs confidence thresholds).
- **Cluster:** DomainAdapt

### B-0111
- **One-sentence idea:** Gradient-free feature adaptation via optimal-transport mapping of intermediate feature distributions at multiple depths, handling multimodal feature shifts that mean/variance alignment cannot express.
- **Problem:** BN-style alignment matches only first and second moments; when target features are multimodally shifted (e.g., two scanner subpopulations in one stream), moment matching aligns to a fictional average domain and degrades both modes.
- **Core Hypothesis:** Closed-form or Sinkhorn OT maps between source and target feature distributions (estimated on small target buffers, applied as fixed transforms) beat moment alignment precisely when target feature distributions are multimodal — with a bimodality statistic predicting the gap.
- **Why Important:** Gradient-free adaptation is deployable on frozen, certified models where backprop is prohibited — a common regulatory constraint.
- **Why Possibly Novel:** OT for domain alignment exists at training time; inference-time layered OT transforms for frozen dense models with the multimodality-predicts-gain claim are untested.
- **Minimal Experiment:** Construct unimodal vs. bimodal target mixtures from public multi-scanner data; compare moment vs. OT alignment on frozen models. Falsified if OT never beats moments.
- **Main Risk:** OT estimation on small buffers is noisy; per-layer maps may compound errors.
- **Cluster:** DomainAdapt

### B-0112
- **One-sentence idea:** Build a taxonomy and detector for label-consistent shift — cases where appearance is in-distribution but the label convention differs — where any feature-level adaptation is guaranteed harmful.
- **Problem:** Some cross-site "domain gaps" are actually annotation-convention gaps (different contouring guidelines); adaptation methods interpret the resulting error signal as covariate shift and warp features, making predictions worse while metrics on the adapting site improve misleadingly.
- **Core Hypothesis:** Convention shift is detectable without labels by its signature — feature statistics match source while output-space disagreement concentrates systematically at boundaries with a consistent bias direction — and a detector for it prevents categorically futile adaptation attempts.
- **Why Important:** Distinguishing "the images differ" from "the definitions differ" determines whether the fix is adaptation or protocol harmonization — completely different investments.
- **Why Possibly Novel:** Annotation-convention shift as a formal shift category with a label-free detector is unformulated in the DA literature.
- **Minimal Experiment:** Create convention-shifted labels (systematic margin erosion/dilation per guideline differences) on one dataset; verify adaptation methods harm it; test the detector's separation of convention vs. covariate shift. Falsified if signatures are indistinguishable.
- **Main Risk:** Real convention differences are subtler than simulated margin changes.
- **Cluster:** DomainAdapt

### B-0113
- **One-sentence idea:** Identify contrast inversion (structures flipping from bright to dark) as the dominant failure variable in cross-modality adaptation, and design sign-invariant edge representations that survive it.
- **Problem:** CT→MR adaptation fails much harder for some structures than others; the pattern tracks whether tissue contrast inverts between modalities, but methods treat cross-modality gaps as generic style differences and miss this structure entirely.
- **Core Hypothesis:** Per-structure adaptation difficulty is predictable from a contrast-inversion index computed on paired atlases, and features built on contrast-sign-invariant primitives (gradient orientation without polarity, phase congruency) close a disproportionate share of the gap on inverted structures.
- **Why Important:** Explains and predicts where cross-modality methods fail, replacing blanket claims with structure-level understanding.
- **Why Possibly Novel:** Cross-modality DA is a crowded field, but the inversion-index analysis and polarity-invariant feature pathway are a specific untested mechanism.
- **Minimal Experiment:** Compute inversion indices from a paired CT/MR atlas; correlate with published per-structure UDA gaps; add polarity-invariant input branch and evaluate on high-inversion structures. Falsified if difficulty doesn't track inversion.
- **Main Risk:** Inversion may be confounded with structure size/boundary strength.
- **Cluster:** DomainAdapt

### B-0114
- **One-sentence idea:** Adapt driving segmentation to adverse weather by first estimating physical weather parameters (fog density, rain rate) and conditioning the network on them, instead of treating weather as an unstructured domain.
- **Problem:** Weather adaptation lumps "fog" into one domain; fog obeys a parametric scattering model whose single parameter (density) smoothly indexes the shift, but methods neither estimate nor exploit this — every density is a new domain to them.
- **Core Hypothesis:** A weather-parameter estimator plus parameter-conditioned segmentation generalizes across the full density continuum after training on a few discrete simulated levels, beating unconditioned DA especially at held-out intermediate densities (interpolation) and beyond-training densities (extrapolation).
- **Why Important:** Weather robustness for autonomy needs guarantees across a continuum, not performance at sampled benchmark levels.
- **Why Possibly Novel:** Physics-parameterized domain indexing with interpolation/extrapolation evaluation is a structured alternative to the domain-as-category dogma.
- **Minimal Experiment:** Train on 3 simulated fog densities with/without conditioning; test across a dense sweep plus real fog data. Falsified if unconditioned training interpolates equally well.
- **Main Risk:** Real weather deviates from the scattering model (heterogeneous fog, spray), limiting the parametrization.
- **Cluster:** DomainAdapt

### B-0115
- **One-sentence idea:** Ship "source sketches" — a few hundred privacy-cleared synthetic exemplars distilled from the source model — alongside deployed models to close most of the source-free adaptation gap.
- **Problem:** Source-free DA discards source data for privacy, paying a large adaptation-quality cost; but the binary choice (all source data vs. none) is false — a tiny, privacy-auditable synthetic summary might retain most of the adaptation value.
- **Core Hypothesis:** Dataset-distillation-style synthetic exemplars (optimized so training on them reproduces source gradients) recover a large fraction of source-present adaptation performance at a size where formal privacy auditing (memorization checks per exemplar) is feasible — mapping a privacy-utility frontier the field hasn't drawn.
- **Why Important:** Makes a principled middle ground between privacy absolutism and adaptation quality, with an auditable artifact.
- **Why Possibly Novel:** Dataset distillation exists for classification efficiency; its use as a privacy-bounded adaptation aid for dense prediction, with per-exemplar privacy auditing, is new.
- **Minimal Experiment:** Distill 200 exemplars from a source segmentation task; run adaptation with none/sketches/full-source; run membership-style audits on the sketches. Falsified if sketches add nothing over source-free.
- **Main Risk:** Dense-prediction dataset distillation is technically immature; exemplars may leak more than audits detect.
- **Cluster:** DomainAdapt

### B-0116
- **One-sentence idea:** Adapt the input instead of the model: learn a per-case input-space transformation (frozen network, trainable preprocessing) so the deployed, certified model itself never changes.
- **Problem:** Regulated deployments cannot modify certified model weights, ruling out standard TTA entirely; adaptation research ignores this constraint, leaving regulated users with nothing.
- **Core Hypothesis:** Optimizing a constrained input transform (smooth intensity remapping + mild spatial warp) against self-supervised objectives recovers a meaningful fraction of weight-space TTA gains, and its constrained function class makes catastrophic failure geometrically bounded (the transform cannot create structures).
- **Why Important:** The only adaptation form compatible with locked-model regulation — a large, underserved user base.
- **Why Possibly Novel:** Input-space adaptation appears sporadically for classification robustness; a systematic dense-prediction study with failure-boundedness analysis is missing.
- **Minimal Experiment:** Compare input-TTA vs. weight-TTA on cross-site medical shifts: mean gain, worst-case, and formal transform-capacity analysis. Falsified if input space is too weak to matter.
- **Main Risk:** Appearance-only transforms cannot address geometry or semantic shift (consistent with B-0096).
- **Cluster:** DomainAdapt

### B-0117
- **One-sentence idea:** Order target-domain data easy-to-hard (by estimated shift magnitude) during self-training UDA, testing whether curriculum prevents early pseudo-label poisoning.
- **Problem:** Self-training bootstraps from pseudo-labels whose initial quality varies wildly across target samples; training order is random, so early exposure to hard samples injects errors that compound — yet curriculum over the target domain is rarely controlled or studied.
- **Core Hypothesis:** At matched total steps, easy-to-hard target curricula (ranked by source-model confidence calibrated with augmentation agreement) reach higher final accuracy and lower variance than random or hard-first orders, with the effect size growing with total shift magnitude.
- **Why Important:** A zero-cost training-schedule change that could improve every self-training pipeline is maximal return on simplicity.
- **Why Possibly Novel:** Curriculum ideas float around; a controlled order-manipulation study isolating schedule from all other factors in segmentation UDA is absent.
- **Minimal Experiment:** Fix everything except sample order on two UDA benchmarks; run 3 orders × 3 seeds. Cheap and decisive. Falsified if order doesn't matter.
- **Main Risk:** Effect may be small relative to other pipeline noise; needs adequate seeds for power.
- **Cluster:** DomainAdapt

### B-0118
- **One-sentence idea:** Per-case source routing in multi-source adaptation: pick which source model (or mixture) to adapt from for each target case via fast embedding-space matching, instead of pooling all sources.
- **Problem:** Multi-source DA pools sources into one model, averaging away source-specific expertise; a target case nearly identical to source B's distribution is served by a compromise model dragged toward sources A and C.
- **Core Hypothesis:** Per-case routing to the nearest source expert (or a sparse mixture) beats pooled multi-source training whenever inter-source diversity is high, with the pooled-vs-routed gap predictable from a source-dispersion statistic — telling practitioners when to bother with routing.
- **Why Important:** Institutions increasingly hold zoos of site-specific models; routing exploits the zoo instead of demanding expensive joint retraining.
- **Why Possibly Novel:** Source selection exists at dataset level; per-case dense-prediction routing with a dispersion-based applicability criterion is a concrete refinement.
- **Minimal Experiment:** Train 4 single-source models + 1 pooled on public multi-site data; evaluate routing vs. pooling on held-out sites; correlate gap with dispersion. Falsified if pooling always wins.
- **Main Risk:** Routing errors on truly novel targets could underperform the pooled model's safety-in-averaging.
- **Cluster:** DomainAdapt

### B-0119
- **One-sentence idea:** Session-level online adaptation of interactive segmentation models from the user's own corrections: every click is a free labeled pixel, so the model should get better within a reading session.
- **Problem:** Interactive models (SAM-style) treat each case independently; a radiologist correcting the same systematic error 40 times in a session generates dense supervision that the model discards, wasting the most authoritative adaptation signal available.
- **Core Hypothesis:** Lightweight online updates (token/prompt-space, per B-0109) from within-session corrections reduce clicks-per-case with case index — a measurable learning curve within sessions — without cross-session drift, since session state resets.
- **Why Important:** Click reduction is the direct productivity metric of interactive tools; session-bounded adaptation avoids the safety issues of persistent adaptation.
- **Why Possibly Novel:** Online learning from interaction exists in niche tools; a modern formulation on foundation-model-based interactive segmentation with within-session learning curves as the primary metric is open.
- **Minimal Experiment:** Simulate sessions of 30 same-distribution cases with a click simulator; measure clicks-per-case trajectory with/without online updates. Falsified if the curve is flat.
- **Main Risk:** Click simulators may overstate real-user consistency; adaptation could overfit to one user's style (feature or bug).
- **Cluster:** DomainAdapt

### B-0120
- **One-sentence idea:** A sealed, streaming, no-oracle benchmark harness for segmentation TTA that forbids target-label peeking, batch shuffling, and test-set reuse — with a public leaderboard re-running published methods.
- **Problem:** TTA papers self-report under inconsistent, often leaky protocols (oracle hyperparameters per B-0091, shuffled batches per B-0107, multiple passes over test data); results are mutually incomparable and likely inflated, but no infrastructure enforces honesty.
- **Core Hypothesis:** Under a sealed harness, the published ranking of segmentation TTA methods reorders substantially, absolute gains shrink by a large fraction, and simple baselines (BN recalibration with episodic reset) climb the ranking — quantifying the field's protocol inflation.
- **Why Important:** Benchmarks define fields; a sealed harness would redirect TTA research toward deployment-valid contributions.
- **Why Possibly Novel:** Sealed-evaluation infrastructure exists in other subfields; segmentation TTA has nothing comparable, and the inflation quantification itself is a publishable finding.
- **Minimal Experiment:** Implement the harness; port 8 methods; compare sealed vs. reported numbers. Engineering-heavy but conceptually cheap; falsified if reported numbers replicate under sealing.
- **Main Risk:** Faithful ports are laborious; authors may contest configurations (mitigated by accepting author-submitted configs).
- **Cluster:** DomainAdapt
## Section 5 — Few-shot / Zero-shot Segmentation [B-0121–B-0150]

### B-0121
- **One-sentence idea:** Audit and quantify "foreground bias" in few-shot segmentation — models segmenting the salient object regardless of what the support actually shows — via wrong-support counterfactual testing.
- **Problem:** FSS benchmarks contain mostly one salient object per query, so a model can score well by ignoring the support entirely and segmenting whatever is salient; reported progress may partially measure saliency, not few-shot learning.
- **Core Hypothesis:** Feeding deliberately mismatched supports (wrong class) leaves predictions largely unchanged for a substantial share of current methods — a "support-sensitivity score" — and methods reranked by this score reorder the leaderboard.
- **Why Important:** If the field's metric can be gamed by class-blind saliency, method comparisons are meaningless until the bias is measured and designed out.
- **Why Possibly Novel:** Saliency bias is occasionally mentioned, but a standardized counterfactual-support sensitivity audit across published methods does not exist.
- **Minimal Experiment:** Run 8 public FSS methods with correct vs. shuffled-class supports on standard benchmarks; report prediction-change rates. Pure evaluation, days of work. Falsified if all methods collapse appropriately under wrong supports.
- **Main Risk:** Some benchmarks may legitimately lack distractor objects, making the audit less informative there.
- **Cluster:** FewZero

### B-0122
- **One-sentence idea:** Suppress base-class leakage in novel-class segmentation by allocating novel classes an orthogonal feature subspace at episode time, rather than letting them compete inside base-class geometry.
- **Problem:** Novel-class predictions systematically leak toward visually similar base classes (novel "wolf" labeled as base "dog") because the frozen feature space was shaped by base-class discrimination; fine-tuning fixes it but destroys base performance.
- **Core Hypothesis:** Projecting novel-class prototypes into the null space of base-class discriminants reduces base-leakage errors substantially at fixed base-class accuracy, with the gain proportional to base-novel similarity — a measurable, mechanism-level prediction.
- **Why Important:** Base-novel confusion is the dominant error type in generalized few-shot settings that mirror real deployments (existing system + new class).
- **Why Possibly Novel:** Null-space and orthogonality tricks exist in continual learning; their application to episodic prototype construction with similarity-stratified evaluation is untried.
- **Minimal Experiment:** On a generalized-FSS benchmark, stratify novel classes by feature similarity to bases; compare standard vs. null-space prototypes on leakage rate. Falsified if leakage is unaffected.
- **Main Risk:** Orthogonalization may discard features the novel class genuinely needs.
- **Cluster:** FewZero

### B-0123
- **One-sentence idea:** Construct a genuinely-novel-class benchmark (classes verifiably absent from web-scale pretraining) and measure how much "zero-shot segmentation" performance evaporates on it.
- **Problem:** "Novel" classes in current benchmarks (buses, dogs) saturate web-scale pretraining corpora; zero/few-shot claims are measured on classes the backbone has effectively seen thousands of times, inflating the apparent generalization.
- **Core Hypothesis:** On verifiably unseen categories (new industrial parts, rare biological specimens, synthetic objects with controlled novelty), zero-shot performance drops far more than few-shot performance, revealing that current "zero-shot" is largely retrieval of pretrained concepts, not compositional generalization.
- **Why Important:** Deployment novel classes (a factory's new component) are truly novel; the field needs numbers that predict that setting.
- **Why Possibly Novel:** Contamination-controlled benchmarks exist in NLP; a verifiable-novelty dense benchmark with a zero-vs-few-shot decomposition is unbuilt.
- **Minimal Experiment:** Assemble 30 verifiably novel categories (custom-fabricated objects, post-pretraining-cutoff products); evaluate 5 open-vocab and 5 FSS methods; compare against standard-benchmark deltas. Falsified if performance transfers intact.
- **Main Risk:** Verifying absence from closed pretraining corpora is hard; fabricated objects may be unrepresentatively simple.
- **Cluster:** FewZero

### B-0124
- **One-sentence idea:** Show that support-set selection explains more performance variance than method choice in FSS, and build active support selection (choosing which k examples to label) as the highest-leverage intervention.
- **Problem:** FSS papers average over random support draws, hiding enormous per-draw variance; practitioners choosing supports in deployment get no guidance, though their choice may matter more than which SOTA method they install.
- **Core Hypothesis:** Variance decomposition will show support-draw variance rivals or exceeds inter-method variance at k≤5, and support selection by coverage criteria (diversity in pose/scale/context of the target class) recovers most of the oracle-support gain.
- **Why Important:** Redirects effort from method leaderboards to the data decision users actually control.
- **Why Possibly Novel:** Support-variance is reported as error bars, never analyzed as the object of study with an actionable selection procedure validated across methods.
- **Minimal Experiment:** For 4 methods × 2 benchmarks, evaluate 50 support draws per class; decompose variance; test coverage-based selection vs. random. Falsified if method variance dominates.
- **Main Risk:** Coverage criteria that work on benchmarks may need class-specific tuning in the wild.
- **Cluster:** FewZero

### B-0125
- **One-sentence idea:** Replace prototype averaging in k-shot segmentation with per-mode matching that preserves intra-class multimodality (a class with visually distinct sub-types keeps multiple prototypes).
- **Problem:** Averaging k support features into one prototype destroys multimodal class structure (e.g., "chair" spanning office chairs and armchairs); queries matching one mode are scored against a fictional average that matches nothing.
- **Core Hypothesis:** Clustering support features into adaptive modes and matching queries to the nearest mode improves precisely on multimodal classes (quantified by support-feature dispersion), with no cost on unimodal classes — a dispersion-stratified prediction.
- **Why Important:** Real deployment classes are almost always multimodal; the averaging assumption is a silent ceiling on k-shot scaling.
- **Why Possibly Novel:** Multi-prototype ideas exist; the dispersion-stratified falsifiable claim and adaptive mode count tied to a measurable class property sharpen it into science.
- **Minimal Experiment:** Stratify benchmark classes by support dispersion; compare mean-prototype vs. mode-matching across strata at k=10. Falsified if gains don't concentrate on high-dispersion classes.
- **Main Risk:** With small k, mode estimation is noisy; adaptive mode-count selection may be fragile.
- **Cluster:** FewZero

### B-0126
- **One-sentence idea:** Fix support-query geometric mismatch (pose, viewpoint, scale) with lightweight test-time geometric alignment before feature correlation, instead of hoping correlation layers absorb it.
- **Problem:** Correlation-based FSS degrades sharply when the query object's pose/scale differs from supports — a failure invisible in benchmarks whose photos share canonical viewpoints, but dominant in robotics/industrial use.
- **Core Hypothesis:** Optimizing a small geometric transform of support features (rotation/scale/affine in feature space) to maximize correlation peak sharpness before matching recovers most of the pose-mismatch loss, and the benefit is predictable from a pose-difference estimate.
- **Why Important:** Deployment queries do not respect canonical viewpoints; robustness to geometric mismatch decides practical usability.
- **Why Possibly Novel:** Alignment modules exist inside architectures; a test-time optimization formulation with pose-mismatch-stratified evaluation isolates and addresses the specific failure.
- **Minimal Experiment:** Build a pose-mismatch-controlled test split (rendered turntable objects or viewpoint-annotated data); measure degradation curves ± test-time alignment. Falsified if correlation is already pose-robust.
- **Main Risk:** Feature-space transforms may not correspond cleanly to image-space geometry for deep features.
- **Cluster:** FewZero

### B-0127
- **One-sentence idea:** Add negative supports ("this is NOT the class") as a first-class input to few-shot segmentation, formalized as contrastive prototype construction.
- **Problem:** Real annotators can cheaply supply negatives (confusable objects, background look-alikes), but FSS interfaces accept only positive masks; models therefore cannot be told about a specific confusion even when the user knows it.
- **Core Hypothesis:** k positive + m negative supports outperform k+m positives whenever the negative is drawn from the model's actual confusion set, with the gain proportional to the confuser's baseline false-positive contribution — making negatives the cheaper marginal annotation.
- **Why Important:** Changes the annotation interface of few-shot systems toward how humans naturally teach (contrast pairs).
- **Why Possibly Novel:** Negative prompts exist in interactive segmentation clicks; episodic negative supports with a confusion-targeted value analysis are unformalized in FSS.
- **Minimal Experiment:** On standard benchmarks, identify per-class top confusers from baseline errors; compare positive-only vs. positive+targeted-negative episodes at matched annotation budget. Falsified if negatives never beat extra positives.
- **Main Risk:** Untargeted negatives (random) may dilute rather than help — interface must guide negative choice.
- **Cluster:** FewZero

### B-0128
- **One-sentence idea:** Disentangle recognition from delineation in FSS evaluation: measure separately whether the model found the right object and how well it drew the boundary, since these have different failure causes and cures.
- **Problem:** IoU conflates "segmented the wrong object" with "sloppy boundary on the right object"; methods are tuned blindly against the mixture, and it is unknown which failure dominates — though the fixes (better matching vs. better decoding) are entirely different.
- **Core Hypothesis:** Decomposed evaluation will show most FSS error mass is recognition (wrong/partial object selection), implying class-agnostic boundary decoders are already sufficient and research should refocus on matching; the decomposition also predicts which method improvements transfer across benchmarks.
- **Why Important:** Redirects an entire subfield's optimization target based on measurement rather than intuition.
- **Why Possibly Novel:** Decomposition analyses exist for object detection (TIDE-style); no equivalent diagnostic exists for few-shot dense prediction.
- **Minimal Experiment:** Build the decomposition tool (object-level assignment then boundary scoring); run on 8 public methods' predictions. Pure analysis of existing outputs. Falsified if boundary error dominates instead — equally informative.
- **Main Risk:** Decomposition requires instance-level GT which some FSS benchmarks lack (fixable on PASCAL/COCO-derived ones).
- **Cluster:** FewZero

### B-0129
- **One-sentence idea:** Establish training-free FSS (frozen self-supervised features + correspondence + test-time optimization) as a mandatory baseline, quantifying exactly what episodic meta-training adds.
- **Problem:** FSS methods entangle episodic training machinery with pretrained-feature quality; as SSL backbones (DINO-family) improved, it became unclear whether meta-training contributes anything beyond what frozen correspondence already provides — but no rigorous accounting exists.
- **Core Hypothesis:** A carefully engineered training-free pipeline matches or exceeds a majority of published episodic methods on standard benchmarks, and the residual advantage of meta-training concentrates in specific conditions (low-quality supports, cluttered queries) that can be named and measured.
- **Why Important:** Would recalibrate the field's understanding of where its progress actually came from and where meta-learning genuinely pays.
- **Why Possibly Novel:** Strong training-free baselines have appeared, but the systematic residual-attribution analysis (what exactly does episodic training buy, and when) is missing.
- **Minimal Experiment:** Build the frozen-feature pipeline; evaluate against 10 published numbers; stratify the gap by support quality and query clutter. Falsified if meta-training wins broadly and uniformly.
- **Main Risk:** Engineering effort in the baseline could be criticized as its own form of tuning (mitigate with ablations).
- **Cluster:** FewZero

### B-0130
- **One-sentence idea:** Add novel classes to a deployed segmenter via null-space parameter updates that provably leave base-class outputs unchanged on a calibration set.
- **Problem:** Generalized FSS methods report base-class degradation as an averaged metric, but deployments need a guarantee — regression on existing classes is contractually unacceptable — and no current method offers even an empirical near-guarantee.
- **Core Hypothesis:** Constraining novel-class weight updates to the null space of base-class feature activations (computed on a stored calibration set) achieves useful novel-class accuracy with base-class output drift below measurement noise, trading a bounded novel-class penalty for a hard stability property.
- **Why Important:** Reframes generalized FSS around the deployment contract (no regressions) rather than an average metric.
- **Why Possibly Novel:** Null-space updates appear in continual learning for classification; the dense-prediction formulation with drift-guarantee evaluation is unexplored.
- **Minimal Experiment:** Implement null-space novel-class addition on a semantic segmentation model; measure base drift (per-pixel output change) and novel accuracy vs. standard fine-tuning and frozen-feature baselines. Falsified if the null space is too restrictive to learn novel classes.
- **Main Risk:** Calibration-set null space may not cover the true base distribution; drift could appear off-calibration.
- **Cluster:** FewZero

### B-0131
- **One-sentence idea:** Factor cross-domain FSS failure (natural-image supports/training → medical/industrial queries) into feature-transfer failure vs. matching-mechanism failure with swap experiments.
- **Problem:** FSS trained on natural images collapses on medical/industrial targets, but nobody knows whether the features stop transferring or the matching/decoding machinery breaks — the two explanations demand opposite remedies (re-pretraining vs. matcher redesign).
- **Core Hypothesis:** Swap experiments (natural features + in-domain matcher, in-domain features + natural matcher, etc.) will attribute most of the cross-domain drop to feature transfer for modality-shifted targets (CT, thermal) but to the matcher for style-shifted targets (sketches, industrial photos) — a two-regime law.
- **Why Important:** Cross-domain FSS is the actual industrial use case; knowing which component to fix saves the community years of misdirected work.
- **Why Possibly Novel:** Cross-domain FSS benchmarks exist; the component-attribution methodology via factorial swaps does not.
- **Minimal Experiment:** 2×2 (feature source × matcher source) on two target domains with small in-domain training sets for the in-domain variants. Falsified if attribution is uniform across target types.
- **Main Risk:** In-domain components trained on small data may understate their ceiling, biasing attribution.
- **Cluster:** FewZero

### B-0132
- **One-sentence idea:** Break the k-shot saturation of in-context segmentation (performance plateauing beyond ~5 shots) by replacing prompt concatenation with retrieval plus non-parametric decoding over all shots.
- **Problem:** In-context segmentation models plateau quickly with added examples — suspicious, since more labeled examples should monotonically help; the bottleneck is plausibly the fixed-capacity aggregation (context window, prototype pooling), not information exhaustion.
- **Core Hypothesis:** A non-parametric route (per-pixel k-NN over all support features with learned distance) continues improving to k=100+ where in-context aggregation saturates, demonstrating the plateau is architectural, not informational.
- **Why Important:** Determines whether scaling labeled examples at inference is worthwhile — a basic economics question for deployment.
- **Why Possibly Novel:** Saturation is visible in published curves but unexplained; the architectural-vs-informational decomposition with a non-parametric probe is a clean unanswered question.
- **Minimal Experiment:** On one benchmark, extend shot curves to k=100 for an in-context model vs. non-parametric matching over identical features. Falsified if both saturate together (information exhaustion).
- **Main Risk:** Non-parametric decoding may be too slow for practical inference (though fine for the scientific question).
- **Cluster:** FewZero

### B-0133
- **One-sentence idea:** Few-shot segmentation of relationally defined targets ("the handle of any tool", "the damaged part") where the class is a role, not an appearance category.
- **Problem:** FSS assumes appearance-coherent classes; many real requests are functional/relational roles whose instances look nothing alike, and current matching-by-appearance methods are structurally incapable of them — the failure isn't measured because benchmarks exclude such classes.
- **Core Hypothesis:** Role classes require relational context features (object-part structure, damage-vs-intact contrast), and a method combining part decomposition with support-derived relational rules will vastly outperform appearance matching on a purpose-built role-class benchmark, while appearance methods sit near chance.
- **Why Important:** Industrial inspection and maintenance queries are predominantly role-based ("worn area", "connector pins"); this is a large unserved query class.
- **Why Possibly Novel:** Compositional/relational few-shot exists in VQA; a dense-prediction role-class benchmark and method family is essentially unclaimed.
- **Minimal Experiment:** Build a 15-role benchmark from existing part-annotated datasets (roles spanning appearance-diverse objects); run 5 FSS baselines to establish the failure; prototype the relational method. Falsified if appearance FSS already handles roles.
- **Main Risk:** Role definitions can be ambiguous; annotation consistency needs care.
- **Cluster:** FewZero

### B-0134
- **One-sentence idea:** Characterize the extreme-minimal-supervision limit: one positive pixel (not a mask) per novel class, combined with strong class-agnostic segment priors.
- **Problem:** The cost-quality frontier of few-shot supervision is unmapped at its cheap extreme; if one click on one image bought most of one full mask's value (given modern segment-anything-style priors), annotation economics would change, but nobody has measured this frontier.
- **Core Hypothesis:** With current class-agnostic mask priors, single-pixel supports recover a large fraction (falsifiably: >70%) of full-mask one-shot performance on well-delineated classes, and the residual gap concentrates on classes whose extent is convention-dependent (where the mask carries boundary-convention information a point cannot).
- **Why Important:** Establishes the actual marginal value of mask annotation in the foundation-model era — a number every annotation budget needs.
- **Why Possibly Novel:** Point-supervised segmentation exists in weak supervision; the support-side minimal-supervision frontier for FSS, with the convention-information interpretation, is unmeasured.
- **Minimal Experiment:** On two benchmarks, sweep support supervision {1 pixel, 10 pixels, box, mask} × k; plot the frontier. Pure evaluation with existing components. Falsified if points are far below masks everywhere.
- **Main Risk:** Results hinge on the quality of the class-agnostic prior, requiring multi-prior replication.
- **Cluster:** FewZero

### B-0135
- **One-sentence idea:** Delineate the regimes where classical registration-based one-shot segmentation beats learned FSS in medical imaging (and vice versa), producing a decision rule instead of another method.
- **Problem:** For anatomy, propagating one labeled atlas by registration is a decades-old one-shot method that modern medical FSS papers often exclude from comparison; practitioners have no evidence-based rule for which paradigm to use for which structure.
- **Core Hypothesis:** Registration dominates for spatially stable anatomy and loses catastrophically on pathology and topology-variable structures, with the crossover predictable from an inter-subject deformation-variability statistic — yielding a simple, validated router between paradigms.
- **Why Important:** Prevents both communities from overclaiming; gives clinical developers an immediate decision procedure.
- **Why Possibly Novel:** Head-to-head studies are scattered and small; a systematic regime map with a predictive routing statistic is missing.
- **Minimal Experiment:** Evaluate registration one-shot vs. 3 FSS methods across ~15 structures spanning stability regimes; fit the routing statistic; validate on held-out structures. Falsified if no stable regime structure exists.
- **Main Risk:** Registration implementation quality strongly affects conclusions; must use strong, tuned baselines.
- **Cluster:** FewZero

### B-0136
- **One-sentence idea:** Test whether diffusion-generated variations of support images (synthetic extra shots) improve FSS beyond classical augmentation, with generation conditioned to preserve the support mask.
- **Problem:** k is small by definition; generative models could in principle multiply supports, but naive generation breaks mask alignment and may only replay the generator's priors — whether synthetic shots add information beyond geometric/photometric augmentation is an open empirical question.
- **Core Hypothesis:** Mask-preserving generative augmentation helps only when the generator injects genuine appearance diversity absent from the support (measurable via feature-space coverage gain), and otherwise matches classical augmentation — making coverage gain a usable predictor of when to bother generating.
- **Why Important:** Teams are already doing this blindly; a predictive criterion converts guesswork into policy.
- **Why Possibly Novel:** Generative augmentation is studied for classification; the mask-preservation constraint and the coverage-gain predictor for dense few-shot are specific new pieces.
- **Minimal Experiment:** For 20 classes, generate mask-conditioned support variants; measure feature-coverage gain and FSS delta vs. classical augmentation; test the predictor's correlation. Falsified if deltas are uncorrelated with coverage gain.
- **Main Risk:** Mask-conditioned generation quality varies wildly across classes, confounding the analysis.
- **Cluster:** FewZero

### B-0137
- **One-sentence idea:** Correct support-query appearance mismatch at test time by restyling support images into the query's domain (statistics-matched, mask-preserving) before matching.
- **Problem:** Deployed FSS often uses web/catalog supports against in-the-wild queries (different lighting, sensor, context); matching degrades from pure appearance mismatch even when the class is identical — a gap distinct from class-level generalization and unhandled by episodic training.
- **Core Hypothesis:** Cheap statistical restyling of supports toward the query (feature-statistic matching, no generative model) recovers a large share of the domain-mismatch loss, and the recovery correlates with a support-query feature distance, making the correction self-triggering.
- **Why Important:** The support-domain problem is ubiquitous in practice (nobody photographs supports with the deployment camera) and absent from benchmarks.
- **Why Possibly Novel:** Style alignment is standard in UDA; applying it per-episode on the support side, with a self-triggering criterion, is a distinct and easily testable mechanism.
- **Minimal Experiment:** Construct cross-domain support-query pairs (catalog→wild) from existing datasets; measure FSS drop and restyling recovery. Falsified if mismatch loss is negligible or unrecoverable by restyling.
- **Main Risk:** Restyling may corrupt fine-grained class evidence for texture-defined classes.
- **Cluster:** FewZero

### B-0138
- **One-sentence idea:** Give few-shot/zero-shot segmenters a semantic-hierarchy fallback: when novel-class evidence is insufficient, output the most specific confident ancestor class ("vehicle" instead of a wrong "trailer").
- **Problem:** Current systems emit a full-confidence mask for the requested class or nothing; under insufficient evidence they silently guess, and downstream consumers cannot distinguish confident identification from coin-flips — a failure of output semantics, not accuracy.
- **Core Hypothesis:** Hierarchical prediction with calibrated specificity selection strictly improves a utility metric that scores partial credit for correct ancestors (and penalizes wrong specifics), and users in a small study prefer and act better on hierarchical outputs.
- **Why Important:** Wrong-but-confident specific labels are worse than honest general ones in every safety-relevant application.
- **Why Possibly Novel:** Hierarchical classification is classic; hierarchy-aware output semantics for open-vocabulary dense prediction with calibrated specificity is unbuilt.
- **Minimal Experiment:** Wrap an open-vocab segmenter with hierarchy + specificity calibration; evaluate under the partial-credit metric on classes at varied evidence levels. Falsified if flat prediction matches under the honest metric.
- **Main Risk:** Hierarchy choice is contestable; partial-credit metric design needs care to avoid gaming.
- **Cluster:** FewZero

### B-0139
- **One-sentence idea:** Transferable threshold calibration for open-vocabulary segmentation: learn how to set per-class confidence thresholds from base classes so novel classes get correct thresholds without any labels.
- **Problem:** Open-vocab segmenters need a per-class score threshold to binarize masks; for novel classes there is no validation data to tune it, and a global threshold is badly wrong for classes with atypical score distributions — a mundane blocker that silently dominates real accuracy.
- **Core Hypothesis:** The optimal threshold is predictable from label-free class properties (text-embedding geometry, score-distribution shape on unlabeled data), and a threshold-regressor trained on base classes transfers to novel ones, recovering most of the oracle-threshold gap.
- **Why Important:** Every deployment hits this problem immediately; solving it is unglamorous but unblocks the entire open-vocabulary paradigm in practice.
- **Why Possibly Novel:** Calibration transfer across classes is essentially unstudied for dense open-vocabulary models.
- **Minimal Experiment:** On open-vocab benchmarks, compute oracle thresholds per class; train threshold-regressor on half the classes, test threshold quality on the rest. Falsified if optimal thresholds are unpredictable from class properties.
- **Main Risk:** Threshold predictability may vary by score head design, requiring per-architecture regressors.
- **Cluster:** FewZero

### B-0140
- **One-sentence idea:** Make referring segmentation ambiguity-aware: when an expression matches multiple objects, output the candidate set plus a minimal clarifying question, instead of arbitrarily picking one.
- **Problem:** Referring segmentation models resolve genuinely ambiguous expressions ("the cup on the table" with three cups) by silent arbitrary choice; benchmarks contain little ambiguity, so this behavior is unmeasured and unpenalized while being the dominant real-interaction failure.
- **Core Hypothesis:** An ambiguity-detection head (predicting match-set cardinality) plus set-output achieves near-perfect ambiguity recognition on a purpose-built ambiguous benchmark, and in simulated dialogues, one clarifying question raises final accuracy above the best single-guess model by a wide margin.
- **Why Important:** Interactive robots and assistive tools live on referring expressions; graceful ambiguity handling is the difference between usable and infuriating.
- **Why Possibly Novel:** Ambiguity in referring expressions is studied in NLP dialogue; the dense-prediction instantiation with set outputs and question policies is open.
- **Minimal Experiment:** Build ambiguous-expression evaluation by programmatically underspecifying existing referring annotations; measure silent-failure rates of current models; train the cardinality head. Falsified if models already signal ambiguity via calibrated scores.
- **Main Risk:** Constructed ambiguity may differ from natural ambiguity distributions.
- **Cluster:** FewZero

### B-0141
- **One-sentence idea:** Use a learned part vocabulary as the transfer substrate for few-shot segmentation: novel objects are segmented by recognizing shared parts (legs, handles, wheels) plus a support-derived part composition.
- **Problem:** Whole-object matching fails when the novel class shares no global appearance with anything seen, yet is trivially composed of familiar parts; current FSS has no mechanism to exploit part reuse, which is how humans handle novel objects.
- **Core Hypothesis:** A part-vocabulary model (parts learned self-supervised across base data) with support-fitted part composition outperforms whole-object matching specifically on structurally novel classes, with the gain predicted by a part-overlap statistic between novel class and base vocabulary.
- **Why Important:** Part reuse is the plausible mechanism for genuine (non-retrieval) generalization — the capability B-0123 shows is missing.
- **Why Possibly Novel:** Part-based recognition is classic; a quantitative part-overlap-predicts-transfer law for dense few-shot prediction has never been established.
- **Minimal Experiment:** Learn parts on base classes; evaluate on novel classes stratified by part overlap; compare against whole-object FSS. Falsified if gains don't track part overlap.
- **Main Risk:** Unsupervised part discovery quality is the load-bearing dependency.
- **Cluster:** FewZero

### B-0142
- **One-sentence idea:** Diagnose and fix support-query scale mismatch with a scale-searched matching pyramid whose scale posterior is output explicitly (the model reports at what scale it found the object).
- **Problem:** FSS correlation degrades when the query instance is much larger/smaller than supports; feature pyramids partially help but scale robustness is never isolated as an evaluation axis, hiding a systematic failure for close-up/far-away deployments.
- **Core Hypothesis:** Explicit scale search with soft scale voting removes most of the scale-mismatch degradation (measured on a scale-controlled split), and the emitted scale posterior is itself useful (flagging suspicious matches when the posterior is diffuse).
- **Why Important:** Scale variation between enrollment and deployment images is guaranteed in practice (different cameras, distances).
- **Why Possibly Novel:** Scale handling is folklore inside architectures; making it explicit, measured, and reported (with the diagnostic posterior) converts a hidden failure into a controlled variable.
- **Minimal Experiment:** Build scale-controlled evaluation via re-rendered/re-cropped instances; measure degradation curves for 5 methods; add scale search to one. Falsified if modern pyramids are already scale-flat.
- **Main Risk:** Extreme scale differences change effective appearance (texture visibility), beyond what search can fix.
- **Cluster:** FewZero

### B-0143
- **One-sentence idea:** Settle when test-time fine-tuning on the support set helps versus hurts FSS, as a function of shot count, support-query domain gap, and parameter subset — producing a practitioner's decision table.
- **Problem:** Half the field freezes everything at test time fearing k-shot overfitting; the other half fine-tunes and reports gains; both cite anecdotes, and no controlled study maps the actual regime boundaries — practitioners inherit superstition.
- **Core Hypothesis:** Test-time fine-tuning benefit is positive above a shot threshold that decreases with domain gap (more gap → fine-tuning pays sooner) and depends strongly on the parameter subset (final-layer vs. prompt vs. full), with regime boundaries stable enough across datasets to tabulate.
- **Why Important:** This is the most common configuration decision in applied few-shot work, currently made blind.
- **Why Possibly Novel:** Scattered ablations exist; the systematic three-factor regime map with cross-dataset stability validation does not.
- **Minimal Experiment:** Grid over k × domain gap (3 target domains) × parameter subset on one strong backbone; validate boundary stability on a fourth domain. Falsified if regimes are dataset-idiosyncratic.
- **Main Risk:** Conclusions may shift with backbone scale, requiring at least two model sizes.
- **Cluster:** FewZero

### B-0144
- **One-sentence idea:** Measure prototype interference in multi-way few-shot segmentation (N novel classes simultaneously) and correct it with joint prototype whitening/orthogonalization.
- **Problem:** FSS research is overwhelmingly 1-way; deployments enroll many novel classes at once, and per-class independent prototypes interfere (confusion among simultaneously enrolled classes) in ways 1-way benchmarks structurally cannot reveal.
- **Core Hypothesis:** Accuracy decays super-linearly with N under independent prototype construction, driven by inter-prototype similarity, and joint whitening of the prototype set restores most of the loss — with the N-decay curve as the headline diagnostic the field should adopt.
- **Why Important:** The gap between 1-way benchmarks and N-way reality silently invalidates method rankings for practical use.
- **Why Possibly Novel:** N-way FSS exists in scattered evaluations; interference as the object of study, with a spectral fix and decay-curve methodology, is unclaimed.
- **Minimal Experiment:** Sweep N from 1 to 20 on a many-class benchmark for 4 methods; fit decay curves; apply joint whitening. Falsified if decay is negligible or whitening doesn't help.
- **Main Risk:** Benchmarks with enough co-occurring classes per image are limited.
- **Cluster:** FewZero

### B-0145
- **One-sentence idea:** Text-plus-shots division of labor: use language to solve recognition (which object) and the few shots only to define the boundary convention (how to delineate it).
- **Problem:** Text prompts identify objects well but cannot convey delineation conventions (include the stem? the shadow? the liquid in the glass?); shots convey conventions but are wasted on re-teaching recognition the VLM already has — current hybrids don't exploit this complementarity explicitly.
- **Core Hypothesis:** An architecture that routes recognition to text matching and learns only a convention transform from shots achieves full-hybrid accuracy with far fewer shots (conventions are low-dimensional), measurable by shots-to-target-accuracy on convention-sensitive classes.
- **Why Important:** Reduces the few-shot burden to the part of the problem that genuinely needs examples, making enrollment near-instant.
- **Why Possibly Novel:** The recognition/convention decomposition (linked to B-0128's diagnosis) as an architectural principle for text-shot hybrids is unformulated.
- **Minimal Experiment:** Construct convention-variant labels (same objects, different delineation rules) on existing data; compare shots-to-accuracy for the routed hybrid vs. standard few-shot. Falsified if conventions require as many shots as full classes.
- **Main Risk:** Some conventions may be spatially complex (not low-dimensional), breaking the premise.
- **Cluster:** FewZero

### B-0146
- **One-sentence idea:** Replace research-convention episode sampling with deployment-realistic episode construction (supports chosen by non-experts, queries from operational distributions) and measure how method rankings change.
- **Problem:** Benchmark episodes are sampled IID from curated datasets — supports are always clean, canonical, and correctly labeled; deployment episodes have amateur supports and operational query distributions, and there is no evidence that benchmark rankings survive the change.
- **Core Hypothesis:** Under realistic episodes (support noise, non-canonical viewpoints, label errors at documented human rates), absolute performance drops sharply and method rankings reorder, with robustness-oriented methods overtaking benchmark leaders — quantifying a validity gap the field ignores.
- **Why Important:** If rankings don't transfer to realistic episodes, the community's selection signal is broken exactly where it matters.
- **Why Possibly Novel:** Realistic-conditions audits exist in other areas (face recognition); episodic-benchmark validity for FSS is unexamined.
- **Minimal Experiment:** Build a realistic-episode generator (documented noise models); re-evaluate 8 methods; compare rankings. Falsified if rankings are preserved.
- **Main Risk:** Choice of noise models is contestable; needs grounding in a small real user study.
- **Cluster:** FewZero

### B-0147
- **One-sentence idea:** Continual few-shot segmentation: enroll novel classes sequentially over months without storing past supports, using consolidated prototype memory with interference-aware placement.
- **Problem:** Real systems accumulate classes over time; re-enrolling everything is impossible when past supports are deleted (privacy/storage), and naive sequential prototype addition degrades old classes through representation drift and interference — a setting benchmarks don't model.
- **Core Hypothesis:** Prototype consolidation (storing distributional summaries, placing new prototypes under an interference penalty against stored summaries) maintains old-class accuracy within a small band over 100+ sequential enrollments where naive addition degrades steadily — with degradation predictable from cumulative prototype-space crowding.
- **Why Important:** Matches the actual lifecycle of deployed recognition systems; crowding analysis gives capacity planning.
- **Why Possibly Novel:** Continual learning and FSS intersect only in a few classification works; the dense, long-horizon, no-replay setting with crowding diagnostics is open.
- **Minimal Experiment:** Simulate 100-class sequential enrollment on a many-class benchmark; compare naive vs. consolidated memory; fit crowding-degradation curve. Falsified if naive accumulation doesn't degrade.
- **Main Risk:** Long-horizon simulation may miss real temporal distribution drift.
- **Cluster:** FewZero

### B-0148
- **One-sentence idea:** Map the support-annotation cost-quality frontier (points vs. boxes vs. polygons vs. precise masks per shot) to find the cost-optimal support labeling policy for a target accuracy.
- **Problem:** FSS assumes pixel-perfect support masks; in reality every support must be annotated by someone, and whether 5 box-supports beat 2 mask-supports at equal cost is unknown — annotation policy is set by convention, not evidence.
- **Core Hypothesis:** For most classes, coarse supports (boxes + a click) reach within a few points of mask supports at equal count, so at equal cost coarse-many dominates precise-few; exceptions are convention-sensitive classes (per B-0145), which are identifiable in advance.
- **Why Important:** Directly optimizes the human cost of every few-shot deployment — the metric users actually pay in.
- **Why Possibly Novel:** Weak supervision literatures exist for training; the support-side cost-frontier analysis with timed annotation costs is unmeasured.
- **Minimal Experiment:** Timed annotation study for cost constants; sweep support type × count across 2 benchmarks; plot iso-cost accuracy curves. Falsified if precise-few dominates everywhere.
- **Main Risk:** Cost constants vary across tools/annotators; report sensitivity analysis.
- **Cluster:** FewZero

### B-0149
- **One-sentence idea:** Pretrain episodic segmentation ability entirely from unlabeled data by constructing pseudo-episodes from self-supervised clusters and mask proposals — no class labels ever.
- **Problem:** Episodic training needs many labeled classes (the diversity B-0037 shows is binding); labels are the scarce resource, yet unlabeled data contains abundant repeated visual concepts that could form pseudo-classes for episode construction.
- **Core Hypothesis:** Pseudo-episodes built from SSL feature clusters + class-agnostic mask proposals train an in-context segmenter matching label-trained episodic models on held-out real classes, demonstrating that episodic skill (matching + decoding) is learnable without semantic labels.
- **Why Important:** Removes the labeled-class-diversity bottleneck from few-shot pretraining entirely.
- **Why Possibly Novel:** Unsupervised meta-learning exists for classification; the dense version with mask-proposal-based pseudo-classes and a labels-vs-none showdown is unbuilt.
- **Minimal Experiment:** Build pseudo-episodes from an unlabeled corpus; train matched architectures on pseudo vs. real episodes; evaluate both on standard FSS benchmarks. Falsified if pseudo-episodes trail badly.
- **Main Risk:** Cluster granularity may mismatch human class granularity, teaching wrong invariances.
- **Cluster:** FewZero

### B-0150
- **One-sentence idea:** Support-sufficiency prediction: the model outputs, before segmenting, whether the provided supports are adequate for the query — enabling "ask for a better example" behavior.
- **Problem:** Few-shot systems fail silently when supports are inadequate (wrong scale, occluded, atypical); users cannot tell whether to fix the supports or distrust the model, and no method quantifies support adequacy per query.
- **Core Hypothesis:** A sufficiency head trained on episodes with known outcome quality predicts per-episode performance well enough to route low-sufficiency cases to "request another support," and the requested-support loop beats fixed-k operation at equal total annotation.
- **Why Important:** Transforms few-shot tools from silent guessers into interactive systems that manage their own evidence — the missing usability layer.
- **Why Possibly Novel:** Performance prediction exists for classification; episode-level sufficiency prediction with a closed-loop support-request policy for dense prediction is new.
- **Minimal Experiment:** Train sufficiency predictor on episode outcomes; evaluate routing policy in simulation (oracle provides requested supports). Falsified if episode outcome is unpredictable from support-query features.
- **Main Risk:** Sufficiency predictor may just learn query difficulty, not support-specific inadequacy (needs careful controls).
- **Cluster:** FewZero
## Section 6 — Prompt Learning [B-0151–B-0180]

### B-0151
- **One-sentence idea:** Determine what learned soft prompts actually encode — class semantics or dataset-specific bias — via nearest-text projection and cross-dataset prompt-transplant experiments.
- **Problem:** Soft prompt tuning improves in-distribution scores, but nobody knows what the learned vectors represent; if they encode dataset statistics rather than class meaning, their celebrated gains are overfitting in disguise, which would explain their known fragility under shift.
- **Core Hypothesis:** Transplanting learned prompts across datasets of identical classes will show large performance drops correlated with dataset-statistic distance (not class distance), and prompt vectors will project closer to dataset-style directions than to class-name embeddings — evidence of bias encoding.
- **Why Important:** Reframes how the field should regularize and interpret prompt tuning; affects thousands of derivative works.
- **Why Possibly Novel:** Prompt interpretability studies exist for NLP; the semantics-vs-bias decomposition with transplant methodology for vision prompt tuning is unexecuted.
- **Minimal Experiment:** Tune prompts on dataset A, transplant to dataset B with same classes; decompose the drop; project prompts against text-embedding anchors. Days of compute. Falsified if prompts transfer intact.
- **Main Risk:** Projection-based interpretation of continuous vectors is inherently contestable; needs multiple probes.
- **Cluster:** PromptLearn

### B-0152
- **One-sentence idea:** Prevent prompt-tuning's characteristic collapse under distribution shift by regularizing learned prompts to stay on the natural-language embedding manifold.
- **Problem:** Tuned prompts beat hand-crafted prompts in-distribution but fall below them under shift — the tuned vectors leave the region of language space where the VLM's alignment is trustworthy, so the model's behavior becomes undefined off-manifold.
- **Core Hypothesis:** Constraining prompt updates to the span/neighborhood of real text embeddings (projection or penalty) sacrifices a little in-distribution gain but eliminates the below-handcrafted collapse under shift, with the tradeoff controllable by the constraint radius.
- **Why Important:** Makes prompt tuning safe-by-default for deployment, where shift is guaranteed.
- **Why Possibly Novel:** Regularized prompt tuning exists in various forms; the manifold-departure explanation of shift collapse, tested via constraint-radius sweeps, is a mechanism-level claim not yet established.
- **Minimal Experiment:** Tune prompts with constraint radii {0, small, large} on one dataset; evaluate across 4 shifted variants; plot in-distribution vs. shifted performance against radius. Falsified if collapse persists at all radii or never occurs.
- **Main Risk:** The text manifold may be poorly approximated by available anchors, weakening the constraint.
- **Cluster:** PromptLearn

### B-0153
- **One-sentence idea:** Learn an automatic geometric-prompt policy (where to place points/boxes) for promptable segmenters, replacing grid prompting with a trained proposal agent optimized for downstream mask quality.
- **Problem:** Automated use of promptable models relies on dense grid prompting (wasteful, produces duplicates and fragments) or detector-generated boxes (inherits detector failures); prompt placement is a decision problem nobody optimizes directly.
- **Core Hypothesis:** A lightweight policy trained with mask-quality reward places an order of magnitude fewer prompts than grids at equal coverage, and the policy transfers across image domains better than detector-based prompting because it learns model-specific prompt sensitivity rather than object appearance.
- **Why Important:** Prompt efficiency determines the cost of running promptable models at scale (video, whole-slide images, volumes).
- **Why Possibly Novel:** Prompt-placement as a learned sequential policy with model-in-the-loop reward, and the transfer claim versus detectors, is largely unexplored.
- **Minimal Experiment:** Train the policy on one dataset with a frozen promptable model; compare prompts-per-image vs. coverage curves against grid and detector baselines on two unseen domains. Falsified if grids/detectors are already Pareto-optimal.
- **Main Risk:** Policy may overfit the specific promptable model version, requiring retraining per model release.
- **Cluster:** PromptLearn

### B-0154
- **One-sentence idea:** Quantify prompt-position sensitivity of promptable segmenters (output variance across equivalent clicks inside the same object) and use that variance as a per-case failure predictor.
- **Problem:** Two clicks a few pixels apart inside the same object can yield different masks; this instability is undocumented, unmeasured, and invisible in benchmarks that use fixed prompt protocols — yet it determines real-user experience and reproducibility.
- **Core Hypothesis:** Prompt-position variance is large for a substantial minority of cases, is spatially structured (predictable from image content), and correlates strongly with mask error — making cheap multi-prompt variance a calibration-free quality signal that beats confidence scores.
- **Why Important:** Provides both a missing reliability metric for promptable models and a free QC signal for automated pipelines.
- **Why Possibly Novel:** TTA-style variance is used for classification uncertainty; prompt-space variance as a measured property and validated error predictor for interactive segmentation is new.
- **Minimal Experiment:** For a public promptable model, sample 20 interior clicks per object across two datasets; measure mask variance and its correlation with error. Zero training. Falsified if variance is negligible or uninformative.
- **Main Risk:** Variance may conflate genuine ambiguity (multiple valid granularities) with instability; needs granularity-controlled analysis.
- **Cluster:** PromptLearn

### B-0155
- **One-sentence idea:** Learn a mapping from acquisition/scene metadata (scanner tags, camera EXIF, weather) to prompt vectors, so a frozen dense model is domain-conditioned by free metadata instead of adapted on images.
- **Problem:** Domain conditioning currently requires image-based adaptation (risky, data-hungry); metadata that directly identifies the domain is discarded, and prompts — the natural injection point for conditioning frozen models — are never driven by it.
- **Core Hypothesis:** A metadata-to-prompt network trained across many domains lets a frozen segmenter match per-domain-tuned prompts on held-out domains whose metadata is interpolable, and degrades gracefully (to the unconditioned prompt) when metadata is novel — a safe conditioning channel.
- **Why Important:** Zero-image-adaptation domain conditioning is deployable in regulated settings where model and data must not change (complements B-0116).
- **Why Possibly Novel:** Metadata conditioning (B-0008) meets prompt learning: the composition — metadata-driven prompt generation for frozen dense models with held-out-domain interpolation tests — is unexplored.
- **Minimal Experiment:** Train the mapper on multi-site data with metadata; evaluate on held-out sites vs. unconditioned and per-site-tuned prompts. Falsified if metadata carries no prompt-space signal.
- **Main Risk:** Metadata quality/completeness in the wild; mapper may shortcut on site identity rather than physical parameters.
- **Cluster:** PromptLearn

### B-0156
- **One-sentence idea:** Prompt banks with per-input retrieval: maintain a library of specialized prompts (per condition/domain/subtask) and route each input to its nearest prompt by image content.
- **Problem:** A single tuned prompt must average over heterogeneous conditions (day/night, contrast/non-contrast); performance on minority conditions is silently sacrificed, and monolithic prompts cannot be extended without retraining everything.
- **Core Hypothesis:** A retrieval-routed prompt bank beats the single-prompt optimum whenever intra-domain heterogeneity is high (quantified by feature-cluster separation), matches it otherwise, and supports incremental extension (add a prompt, no retraining) with zero interference by construction.
- **Why Important:** Modular, extensible conditioning is the operational requirement for long-lived deployed systems.
- **Why Possibly Novel:** Prompt pools exist in continual learning for classification; the dense-prediction instantiation with heterogeneity-predicts-gain analysis and extension protocol is untested.
- **Minimal Experiment:** On a day/night + weather segmentation dataset, compare single prompt vs. clustered prompt bank with routing; correlate gain with cluster separation. Falsified if a single prompt suffices at all heterogeneity levels.
- **Main Risk:** Routing errors on boundary cases; bank growth management over time.
- **Cluster:** PromptLearn

### B-0157
- **One-sentence idea:** Formalize negative prompting for dense prediction — "suppress X" prompts with a principled subtraction geometry in embedding space — to kill specific recurring false positives without retraining.
- **Problem:** Deployed segmenters exhibit known recurring false positives (shadows as smoke, reflections as fire); the only current remedies are retraining or post-hoc filtering, though VLM-based models have an embedding space where the confuser is nameable.
- **Core Hypothesis:** Constructed suppression directions (projecting class queries away from confuser embeddings, with magnitude calibrated on a handful of examples) remove a large fraction of the named false positives at bounded true-positive cost, and the tradeoff curve is stable across images — a controllable knob, not a gamble.
- **Why Important:** Field-fixable false positives without retraining would change operations for every deployed open-vocab system.
- **Why Possibly Novel:** Negative prompts exist in generative models; a calibrated, evaluated suppression mechanism for dense discriminative predictions is unbuilt.
- **Minimal Experiment:** On open-vocab segmentation with known confuser pairs, sweep suppression magnitude; plot FP-removal vs. TP-cost curves. Falsified if suppression is uncontrollable or ineffective.
- **Main Risk:** Embedding arithmetic may not localize: suppressing "shadow" might damage semantically adjacent legitimate classes.
- **Cluster:** PromptLearn

### B-0158
- **One-sentence idea:** Chain-of-prompts for nested structures: segment coarse-to-fine (organ → substructure → lesion) by conditioning each stage's prompt on the previous stage's output, with an explicit error-propagation study.
- **Problem:** Hierarchically nested targets are segmented either flat (ignoring containment constraints) or by rigid cascades (errors propagate uncorrectably); promptable models enable conditional chaining, but its error dynamics are unknown — does chaining amplify or dampen upstream errors?
- **Core Hypothesis:** Prompt chaining with soft (probabilistic) upstream conditioning dampens error propagation relative to hard cropping cascades (downstream stages can recover from upstream misses), yielding better leaf-level accuracy and guaranteed containment consistency.
- **Why Important:** Nested outputs with consistency guarantees are what clinical and industrial reporting actually requires (lesion counts per organ segment).
- **Why Possibly Novel:** Cascades are old; the soft-conditioning-dampens-errors hypothesis, tested with controlled upstream corruption, is a specific unanswered dynamics question.
- **Minimal Experiment:** Build 3-level chains on a hierarchically labeled dataset; inject controlled upstream errors; measure downstream recovery for soft vs. hard conditioning. Falsified if hard cascades are equally robust.
- **Main Risk:** Soft conditioning may blur stage responsibilities, making failures harder to attribute.
- **Cluster:** PromptLearn

### B-0159
- **One-sentence idea:** Convention tokens: train one segmenter on multiple datasets with conflicting delineation conventions, exposing the convention as a switchable prompt, so one model serves all conventions on demand.
- **Problem:** The same structure is delineated differently across guidelines and datasets (tumor with/without edema, road with/without shoulder); models either average conventions into a mush or fragment into per-convention models — and users cannot ask for the convention they need.
- **Core Hypothesis:** Convention-token conditioning learns clean, switchable delineation styles (validated by convention-classification of outputs), improves per-convention accuracy over pooled training, and — the falsifiable surprise — interpolated tokens produce coherent intermediate conventions, evidencing a low-dimensional convention manifold.
- **Why Important:** Convention mismatch is a huge hidden component of "domain gap" (see B-0112); making it explicit and controllable dissolves it.
- **Why Possibly Novel:** Dataset tokens exist for multi-dataset detection; treating annotation convention as an interpolable controlled variable with manifold analysis is a fresh, testable framing.
- **Minimal Experiment:** Train on 3 convention-conflicting datasets with tokens; test switching (correct vs. swapped tokens must differ appropriately) and interpolation coherence. Falsified if tokens fail to separate conventions.
- **Main Risk:** Convention differences may be entangled with appearance differences between the datasets (needs controlled relabeling for a clean subset).
- **Cluster:** PromptLearn

### B-0160
- **One-sentence idea:** Replace entropy-based test-time prompt tuning objectives with cross-augmentation agreement objectives, and characterize when each collapses.
- **Problem:** Test-time prompt tuning typically minimizes prediction entropy on the test sample, inheriting entropy minimization's degenerate optima (confidently wrong predictions); for dense outputs the collapse is spatially structured (backgrounds swallow objects) and undiagnosed.
- **Core Hypothesis:** Agreement-across-augmentations objectives have strictly better failure modes than entropy for dense test-time prompt adaptation (collapse requires coordinated errors across views, which is rarer), measurable as lower catastrophic-failure rates at matched average gains.
- **Why Important:** Test-time prompt tuning is the lightest-weight adaptation available; making it safe determines whether it can be used unattended.
- **Why Possibly Novel:** Objective comparisons exist for classification TTA; the dense-prediction, prompt-space version with failure-rate (not mean) as the primary metric is new.
- **Minimal Experiment:** On shifted segmentation benchmarks, run both objectives across seeds/cases; report mean gain and worst-decile outcomes. Falsified if entropy is equally safe.
- **Main Risk:** Augmentation choice becomes the new hidden hyperparameter (must be reported honestly).
- **Cluster:** PromptLearn

### B-0161
- **One-sentence idea:** Prompt distillation: compress an ensemble of specialized prompts (or the prompting behavior of a large model) into a single compact prompt, quantifying what is lost.
- **Problem:** Prompt ensembles and per-condition prompt banks (B-0156) improve accuracy but multiply inference cost and complexity; whether their benefits are compressible into one vector — and what structurally cannot be compressed — is unknown.
- **Core Hypothesis:** Distillation (training one prompt to match the ensemble's output distribution) retains most average-case gains but systematically loses condition-specific tail performance, with the incompressible residue localized to conditions requiring contradictory feature weightings — an information-theoretic limit made measurable.
- **Why Important:** Determines the true deployment cost of prompt-based specialization and when banks are irreducible.
- **Why Possibly Novel:** Model distillation is standard; prompt-space distillation with a compressibility analysis for dense tasks is unexamined.
- **Minimal Experiment:** Distill a 10-prompt ensemble into 1 prompt on a heterogeneous dataset; stratify retained performance by condition; identify incompressible strata. Falsified if a single prompt captures everything (banks pointless) or nothing (distillation pointless).
- **Main Risk:** Results depend on prompt capacity (length), requiring a capacity sweep.
- **Cluster:** PromptLearn

### B-0162
- **One-sentence idea:** Measure whether learned prompts transfer across backbone architectures, and if not, learn cheap prompt-translation adapters — establishing a science of prompt universality.
- **Problem:** Every backbone upgrade orphans all previously learned prompts (retuning everything from scratch); whether prompts encode backbone-independent task information that could be translated, rather than relearned, is untested.
- **Core Hypothesis:** Direct prompt transplants across backbones fail, but a small translation network trained once on paired prompt sets (same tasks tuned on both backbones) transfers new prompts with most of their performance — implying prompts encode largely backbone-independent content in backbone-specific coordinates.
- **Why Important:** Would make prompt libraries durable assets across model generations — a big operational win for prompt-based ecosystems.
- **Why Possibly Novel:** Representation translation (stitching) exists between networks; prompt-space translation with a task-transfer protocol is unexplored.
- **Minimal Experiment:** Tune 30 task prompts on backbones A and B; train translator on 20 pairs, test on 10 held-out tasks. Falsified if translated prompts perform at transplant (chance) level.
- **Main Risk:** Translation may only work between architecturally similar backbones.
- **Cluster:** PromptLearn

### B-0163
- **One-sentence idea:** Instance-conditional prompts: a hypernetwork generates a per-input prompt from the image itself, tested against static prompts specifically under high intra-domain heterogeneity.
- **Problem:** A static prompt is a single operating point; when one domain contains heterogeneous sub-conditions, the static optimum underserves all of them, and current conditional-prompt work reports averages that hide whether gains come from heterogeneity handling or extra capacity.
- **Core Hypothesis:** Instance-conditional prompts beat static prompts by a margin that scales with measured input heterogeneity, and — the capacity control — beat parameter-matched longer static prompts only under heterogeneity, isolating conditionality (not capacity) as the active ingredient.
- **Why Important:** Clarifies a muddled literature with a controlled attribution, guiding when conditional prompting is worth its complexity.
- **Why Possibly Novel:** Conditional prompting exists; the heterogeneity-stratified, capacity-controlled attribution experiment for dense tasks does not.
- **Minimal Experiment:** Datasets ordered by heterogeneity; compare static vs. long-static vs. conditional prompts; plot gain vs. heterogeneity. Falsified if gains are heterogeneity-independent (pure capacity effect).
- **Main Risk:** Heterogeneity measurement itself requires care to avoid circularity.
- **Cluster:** PromptLearn

### B-0164
- **One-sentence idea:** Uncertainty-eliciting prompts: learn prompts whose output channel is a calibrated per-pixel confidence for a frozen dense model, extracting reliability information the model has but does not express.
- **Problem:** Frozen deployed models produce miscalibrated confidences and cannot be retrained for calibration; prompt channels can inject new behavior without touching weights, but whether calibration is "promptable" — i.e., latent in the frozen model and extractable by conditioning — is unknown.
- **Core Hypothesis:** Prompts optimized for calibration objectives on a small labeled set produce substantially better-calibrated dense confidence than temperature scaling of the same frozen model, and the calibration transfers across mild shifts because it reads internal evidence rather than fitting output statistics.
- **Why Important:** Calibration retrofitting for frozen, certified models is a deployment requirement no current tool meets well.
- **Why Possibly Novel:** Prompting for auxiliary output behaviors (not accuracy) is essentially unstudied for dense vision models.
- **Minimal Experiment:** Learn calibration prompts on 200 labeled images; compare ECE/reliability curves against temperature scaling in-domain and under shift. Falsified if prompts can't beat temperature scaling.
- **Main Risk:** The frozen model may genuinely lack the latent evidence, capping all conditioning approaches equally.
- **Cluster:** PromptLearn

### B-0165
- **One-sentence idea:** Compare the adversarial and corruption robustness of prompt-tuned versus fully fine-tuned dense models at matched clean accuracy, testing whether the small prompt parameterization is a robustness feature.
- **Problem:** Prompt tuning changes orders of magnitude fewer parameters than fine-tuning, plausibly preserving the pretrained model's robustness properties; but robustness comparisons between adaptation paradigms are absent, so the security implications of the paradigm choice are unknown.
- **Core Hypothesis:** At matched clean accuracy, prompt-tuned models retain more of the base model's corruption robustness (they cannot unlearn robust features) but are not more adversarially robust (attacks transfer through the frozen backbone) — a dissociation that clarifies what the frozen backbone protects.
- **Why Important:** Adaptation paradigm choices are being made at scale with zero robustness evidence; the dissociation would inform both deployment and theory.
- **Why Possibly Novel:** Robustness of PEFT methods is beginning to be studied for classification; the dense-prediction version with the corruption/adversarial dissociation hypothesis is open.
- **Minimal Experiment:** Match clean accuracy between paradigms on one benchmark; run corruption suites and standard attacks on both. Falsified if paradigms are robustness-equivalent.
- **Main Risk:** Matching clean accuracy exactly is fiddly; conclusions may depend on tuning budgets.
- **Cluster:** PromptLearn

### B-0166
- **One-sentence idea:** Show that the training order of tasks/classes during multi-task prompt learning determines interference patterns, and derive an interference-minimizing prompt curriculum.
- **Problem:** Multi-task prompt sets are trained in arbitrary order; anecdotal instability across runs suggests order effects, but prompt-learning curricula are unstudied — practitioners re-roll seeds without understanding why results vary.
- **Core Hypothesis:** Prompt interference is asymmetric (learning task A before B differs from B before A) and predictable from task-gradient alignment, so an alignment-based ordering reduces final-variance and improves the worst task's performance at identical total compute.
- **Why Important:** Free (schedule-only) improvement and variance reduction for every multi-task prompt system.
- **Why Possibly Novel:** Curriculum and gradient-conflict research exists for full training; the prompt-subspace version — where interference dynamics may differ qualitatively because the backbone is frozen — is unexplored.
- **Minimal Experiment:** Train 5-task prompt sets under 10 random orders + alignment-derived order; compare variance and worst-task outcomes. Falsified if order effects are noise.
- **Main Risk:** Effects may be small in the frozen-backbone regime precisely because interference passes only through prompts.
- **Cluster:** PromptLearn

### B-0167
- **One-sentence idea:** Textual inversion for domain jargon: learn pseudo-word embeddings for concepts VLMs don't know ("GGO", "slag inclusion", "delamination") from a few masked examples, enabling open-vocabulary segmentation of specialist vocabularies.
- **Problem:** Open-vocabulary segmentation fails on specialist terms absent from web text-image training; the standard remedy is full fine-tuning per domain, discarding the open-vocabulary interface exactly where it would be most valuable.
- **Core Hypothesis:** Pseudo-words learned from ≤10 masked examples per concept slot into existing prompt syntax compositionally (usable in spatial and attribute constructions: "small ⟨GGO⟩ near pleura"), achieving segmentation quality between zero-shot-known-class and fine-tuned levels — with compositionality as the falsifiable differentiator from classifier heads.
- **Why Important:** Extends the open-vocabulary paradigm to the specialist domains (medicine, manufacturing) that need it most.
- **Why Possibly Novel:** Textual inversion is established in generative models; its systematic transplantation to discriminative dense prediction with compositionality evaluation is largely unclaimed.
- **Minimal Experiment:** Learn 15 specialist pseudo-words on a medical/industrial dataset; test standalone and compositional queries vs. linear-probe baselines. Falsified if pseudo-words don't compose.
- **Main Risk:** Discriminative embedding spaces may be less compositional than generative ones.
- **Cluster:** PromptLearn

### B-0168
- **One-sentence idea:** Pixel-space visual prompts (learnable border/frame perturbations) versus token-space prompts for adapting frozen dense models: map which adaptation regimes each can and cannot express.
- **Problem:** Visual prompting (learned input-space perturbations) works surprisingly well for classification, but for dense prediction its capabilities are unmapped — it could be a deployment-friendly adaptation channel (works on black-box models) or fundamentally too weak.
- **Core Hypothesis:** Pixel prompts can implement global appearance adaptations (style, illumination) but structurally cannot implement spatial-semantic adaptations (new class conventions), while token prompts can do both — an expressivity hierarchy testable with controlled shift types (reusing B-0096's factorial design).
- **Why Important:** Black-box adaptation (no model access beyond inputs) is the only option for API-served vision models — knowing its limits is immediately practical.
- **Why Possibly Novel:** Visual prompting for dense prediction, with an expressivity-hierarchy experiment against token prompts, is essentially unstudied.
- **Minimal Experiment:** Factorial: {pixel, token} prompts × {appearance, geometric, convention} shifts on one frozen segmenter. Falsified if pixel prompts match token prompts everywhere or nowhere.
- **Main Risk:** Optimization difficulty of pixel prompts may masquerade as expressivity limits (needs careful tuning).
- **Cluster:** PromptLearn

### B-0169
- **One-sentence idea:** Systematize prompt ensembling for dense prediction: compare embedding-averaging, output-averaging, and learned aggregation, with a variance-decomposition explaining when each wins.
- **Problem:** Prompt ensembling is used as folkloric seasoning ("average 80 templates") inherited from classification; for dense tasks the aggregation point (embedding vs. output) changes boundary behavior, and no analysis guides the choice.
- **Core Hypothesis:** Embedding averaging smooths class semantics (helping recognition, harming boundary sharpness) while output averaging preserves boundary detail at higher cost, and a decomposition of prompt-induced variance into semantic vs. spatial components predicts the optimal aggregation per task.
- **Why Important:** A default-setting question affecting every open-vocabulary dense deployment, currently answered by copy-paste.
- **Why Possibly Novel:** Ensembling analyses exist for classification; the dense-specific aggregation-point analysis with variance decomposition is new.
- **Minimal Experiment:** On two open-vocab segmentation benchmarks, run all aggregation schemes over a fixed template set; decompose variance; test the predictor. Cheap, no training. Falsified if aggregation point is inconsequential.
- **Main Risk:** Findings may be model-family-specific.
- **Cluster:** PromptLearn

### B-0170
- **One-sentence idea:** Domain-incremental segmentation via prompt pools with key-based routing: each new domain adds a prompt, keys route inputs, and the frozen backbone guarantees zero interference on old domains.
- **Problem:** Domain-incremental learning for segmentation suffers the stability-plasticity dilemma because weights are shared; prompt pools solved this elegantly for classification, but dense prediction poses harder routing (per-image? per-region?) and the transfer is unvalidated.
- **Core Hypothesis:** Per-region routing (different image parts may match different domain prompts — e.g., mixed lighting) beats per-image routing on realistic mixed-condition inputs, and the pool approach matches joint training on all domains while provably never regressing old domains.
- **Why Important:** Never-regress guarantees (impossible with weight updates) are exactly what long-lived deployed systems need for domain growth.
- **Why Possibly Novel:** L2P-style pools are classification-only so far; the per-region routing question is genuinely new and dense-specific.
- **Minimal Experiment:** Sequential domains (clear→fog→night) with pool vs. fine-tuning vs. joint; include mixed-condition test images for the routing comparison. Falsified if per-image routing suffices and pools trail joint training badly.
- **Main Risk:** Key matching may fail on domains not seen by the (frozen) key encoder.
- **Cluster:** PromptLearn

### B-0171
- **One-sentence idea:** Factorial study of prompt injection depth for dense tasks: establish where in the network prompts must enter to implement appearance conditioning versus semantic/task conditioning.
- **Problem:** Prompt injection depth is treated as an implementation detail (usually input-only or all-layers); if different conditioning types require different depths, single-depth designs silently cap what prompting can do for dense models — and failures get blamed on "prompting" generally.
- **Core Hypothesis:** Appearance conditioning is only effective when injected in early blocks and semantic/task conditioning in late blocks (mirroring B-0038's adapter law in the prompt channel), and mixed-depth injection achieves both simultaneously where any single depth fails.
- **Why Important:** A depth-placement law would upgrade prompt design from convention to engineering for every dense prompting system.
- **Why Possibly Novel:** Depth ablations exist scattershot for classification; the conditioning-type × depth factorial for dense prediction is unexecuted.
- **Minimal Experiment:** One frozen backbone; prompts injected at {early, mid, late, all}; tasks requiring appearance vs. semantic conditioning (from B-0096/B-0159 setups). Falsified if depth doesn't interact with conditioning type.
- **Main Risk:** Interactions with backbone architecture family (conv-hybrid vs. pure attention).
- **Cluster:** PromptLearn

### B-0172
- **One-sentence idea:** Establish prompt-length scaling laws for dense tasks: performance and overfitting-onset as functions of token count and tuning-set size, yielding a practical sizing rule.
- **Problem:** Prompt length is picked by superstition (often 4–16 tokens); for dense tasks with small tuning sets, too-long prompts overfit invisibly (no validation data to detect it), and no quantitative sizing guidance exists.
- **Core Hypothesis:** Dense-task prompt performance follows a predictable curve in (length, data size) with an overfitting boundary at a stable data-per-token ratio, so optimal length is computable from tuning-set size alone — a one-line rule replacing guesswork.
- **Why Important:** Prompt sizing is a universal decision made thousands of times a day with zero evidence.
- **Why Possibly Novel:** Scaling analyses of prompt capacity exist minimally for NLP; the dense-vision version with the data-per-token boundary claim is unmeasured.
- **Minimal Experiment:** Grid over length {1..256} × data {10..10k images} on two dense tasks; map the boundary; validate the rule on a third task. Falsified if no stable ratio exists.
- **Main Risk:** The ratio may vary with task complexity, requiring a task-difficulty correction term.
- **Cluster:** PromptLearn

### B-0173
- **One-sentence idea:** Gradient-free discrete prompt search for dense models (evolutionary/LLM-proposed hard prompts) as an interpretable, API-compatible alternative to soft prompts.
- **Problem:** Soft prompts require gradient access (impossible for API-served models) and are uninterpretable (unauditable in regulated settings); whether discrete prompt search can approach soft-prompt performance for dense tasks is unknown.
- **Core Hypothesis:** LLM-guided iterative hard-prompt search (propose, evaluate on small labeled set, refine) reaches a substantial fraction of soft-prompt gains for open-vocabulary segmentation, and its outputs transfer across model versions far better than soft prompts (they encode semantics, not coordinates — connecting to B-0151).
- **Why Important:** Black-box and auditable adaptation channels are required by API economics and regulation, respectively.
- **Why Possibly Novel:** Hard-prompt search exists for classification/generation; dense-prediction search with the cross-version transfer comparison is untested.
- **Minimal Experiment:** Run the search loop on two segmentation tasks; compare against soft prompts on performance and cross-model-version transfer. Falsified if hard prompts are hopelessly behind.
- **Main Risk:** Search cost (many evaluations); small labeled sets may overfit the search itself.
- **Cluster:** PromptLearn

### B-0174
- **One-sentence idea:** Measure and improve compositional generalization of prompt-driven segmentation over attribute conjunctions ("cracked AND red region") via explicit prompt algebra.
- **Problem:** Open-vocab segmenters handle single attributes but degrade unpredictably on conjunctions/negations; downstream users compose queries naturally, and the failure is undocumented because benchmarks test atomic classes only.
- **Core Hypothesis:** Naive text conjunction fails systematically compared to an explicit prompt algebra (set operations on per-attribute mask distributions), and the gap grows with the number of conjuncts — establishing both the failure and a working alternative.
- **Why Important:** Query composition is the natural user interface for inspection/search tasks; supporting it correctly unlocks real applications.
- **Why Possibly Novel:** Compositionality is studied for VQA/retrieval; a controlled conjunction benchmark and algebraic remedy for dense prediction is unbuilt.
- **Minimal Experiment:** Build conjunction queries from attribute-annotated datasets; compare naive text vs. algebraic composition across conjunct counts. Falsified if text composition just works.
- **Main Risk:** Attribute independence assumptions in the algebra fail for correlated attributes.
- **Cluster:** PromptLearn

### B-0175
- **One-sentence idea:** One dense model, prompt-switchable across output tasks (semantic masks, instance boundaries, depth, normals) — measuring cross-task interference and synergy in the prompt regime.
- **Problem:** Multi-task dense models fix their task set at training; prompt-switchable task specification promises open task sets, but whether tasks interfere through the shared frozen backbone or synergize (task prompts transferring structure to each other) is unmeasured.
- **Core Hypothesis:** In the frozen-backbone prompt regime, task interference is near zero (unlike jointly trained heads) while synergy persists (adding a depth prompt improves boundary quality of the segmentation prompt via shared calibration data), yielding strictly better scaling of task count than joint training.
- **Why Important:** Open-ended task extensibility without retraining would change how dense-prediction systems are built and shipped.
- **Why Possibly Novel:** Task prompting exists in unified models; the interference/synergy measurement specifically attributable to the prompt regime is an open scientific question.
- **Minimal Experiment:** Train task prompts sequentially vs. jointly on a frozen backbone; measure per-task deltas as tasks accumulate. Falsified if interference matches jointly trained heads.
- **Main Risk:** Frozen backbones may cap per-task ceilings below practical requirements.
- **Cluster:** PromptLearn

### B-0176
- **One-sentence idea:** Region-conditioned prompting: combine spatial prompts ("in this region") with semantic prompts so reviewers can direct open-vocabulary segmentation to specific areas of interest.
- **Problem:** Guided-review workflows (radiology second reads, industrial re-inspection) need "look for X here" queries; current models accept either geometry (points/boxes → class-agnostic masks) or semantics (text → whole-image masks) but not their conjunction with correct semantics-in-region behavior.
- **Core Hypothesis:** Joint spatial-semantic prompting trained with region-restricted supervision outperforms the compositional baseline (text-driven mask ∩ region) specifically when the region contains distractors of similar classes, because attention restriction changes feature computation, not just output masking.
- **Why Important:** Matches the actual interaction pattern of expert review workflows — the highest-value deployment context for interactive segmentation.
- **Why Possibly Novel:** Point/box and text prompting exist separately in promptable models; their principled conjunction with the distractor-stratified claim is untested.
- **Minimal Experiment:** Construct region+class queries on densely annotated data (with distractor-controlled splits); compare joint model vs. intersection baseline. Falsified if intersection suffices everywhere.
- **Main Risk:** Training data for region-restricted supervision must be synthesized carefully to avoid shortcuts.
- **Cluster:** PromptLearn

### B-0177
- **One-sentence idea:** Validation-free prompt overfitting detection: predict from prompt-space geometry (distance traveled from initialization, alignment with text manifold) whether a tuned prompt has overfit — no held-out data required.
- **Problem:** Prompt tuning is used precisely when labeled data is too scarce for a validation split; overfitting is thus undetectable at the moment it is most likely, and users deploy overfit prompts unknowingly.
- **Core Hypothesis:** Overfitting leaves geometric signatures (excessive displacement, off-manifold drift per B-0152, sharpening of the loss landscape) that predict the generalization gap with useful accuracy across tasks — enabling early stopping without validation data.
- **Why Important:** Data-free reliability diagnostics are the missing piece for low-shot adaptation in practice.
- **Why Possibly Novel:** Generalization prediction from weight-space geometry exists for full training; the prompt-subspace version — where geometry is low-dimensional and cheap to analyze — is unexplored and much more tractable.
- **Minimal Experiment:** Tune prompts across many (task, data-size) configurations; record geometry trajectories and true generalization gaps; test predictive power on held-out tasks. Falsified if geometry is uninformative.
- **Main Risk:** Signatures may be optimizer-dependent (learning rate confound).
- **Cluster:** PromptLearn

### B-0178
- **One-sentence idea:** Quantify and close the cross-lingual gap in prompt-driven segmentation: do non-English class names (clinical Latin, German industrial terms) degrade dense predictions, and can multilingual prompt alignment fix it without retraining the VLM?
- **Problem:** Deployment vocabularies are frequently non-English, but vision-language segmenters are trained predominantly on English text; the dense-prediction cost of querying in other languages is unmeasured, and per-language fine-tuning defeats the open-vocabulary purpose.
- **Core Hypothesis:** Non-English queries suffer a measurable, language-dependent segmentation penalty concentrated on rare terms, and a lightweight alignment layer (mapping non-English embeddings onto their English-anchor geometry, trained on translation pairs only — no images) recovers most of it.
- **Why Important:** Language should not gate access to vision tools; the fix requires no image data, making it deployable everywhere.
- **Why Possibly Novel:** Multilingual gaps are documented for retrieval/classification; dense-prediction quantification plus the text-only alignment remedy is open.
- **Minimal Experiment:** Evaluate open-vocab segmentation with translated class names across 5 languages; train the text-only alignment; re-evaluate. Falsified if the gap is negligible or unfixable without images.
- **Main Risk:** Translation ambiguity of technical terms confounds measurement (needs curated term lists).
- **Cluster:** PromptLearn

### B-0179
- **One-sentence idea:** Federated prompt personalization: sites share a frozen backbone and exchange only learned site-prompts, whose structure is then analyzed as an interpretable map of inter-site variation.
- **Problem:** Federated fine-tuning of dense models is bandwidth-heavy and privacy-questionable (weights leak data); prompts are tiny and inspectable, but federated prompt learning for dense tasks — and what shared prompt geometry reveals about site variation — is unstudied.
- **Core Hypothesis:** Federated averaging over prompts (with local prompt residuals for personalization) approaches per-site tuning quality at a fraction of communication, and the learned site-prompt geometry clusters by scanner/protocol (not by site identity), providing a free, privacy-preserving map of the federation's domain structure.
- **Why Important:** A practical federation mechanism plus an interpretability dividend (knowing which sites are domain-alike guides data governance).
- **Why Possibly Novel:** Federated prompt tuning is nascent in NLP/classification; the dense-prediction version with domain-cartography analysis of prompt space is new.
- **Minimal Experiment:** Simulate 8 sites from multi-scanner public data; federated prompts vs. per-site vs. global; cluster analysis of site prompts against scanner metadata. Falsified if prompt geometry is uninformative or federation fails.
- **Main Risk:** Prompt averaging across genuinely incompatible domains may need mixture, not mean.
- **Cluster:** PromptLearn

### B-0180
- **One-sentence idea:** Self-refinement loops for dense prediction: the model critiques its own segmentation (via a learned critique prompt) and emits a refined prompt for a second pass, with a learned stopping criterion.
- **Problem:** Dense models get one forward pass by convention; language models improved substantially through self-critique loops, but whether segmentation quality is improvable by iterated prompt refinement — and when iteration diverges — is unknown.
- **Core Hypothesis:** Critique-conditioned second passes correct a meaningful fraction of first-pass errors (particularly boundary and omission errors identifiable from the prediction's internal inconsistencies), improvement saturates within ~3 iterations, and a learned stop-rule avoids the degradation cases — net positive at 2–3× inference cost.
- **Why Important:** An inference-time quality knob (per B-0052) with an interpretable mechanism; useful wherever compute is cheaper than errors.
- **Why Possibly Novel:** Iterative refinement exists architecturally (recurrent decoders); prompt-mediated self-critique with divergence analysis and learned stopping for dense prediction is a fresh construction.
- **Minimal Experiment:** Train critique+refine prompts on one benchmark; measure per-iteration deltas, divergence rate, and stop-rule effectiveness. Falsified if iteration is flat or divergent on balance.
- **Main Risk:** The critique may only see errors the model can already represent — blind spots persist through iterations.
- **Cluster:** PromptLearn
## Section 7 — Weak / Semi / Self-supervised Learning [B-0181–B-0210]

### B-0181
- **One-sentence idea:** Measure the damage caused by out-of-distribution contamination in the unlabeled pool of semi-supervised segmentation, and build contamination-robust pseudo-labeling that filters by dual (feature + prediction-stability) criteria.
- **Problem:** Semi-supervised methods assume the unlabeled pool matches the labeled distribution; real unlabeled hospital/web dumps contain wrong body parts, corrupted scans, and other modalities, which current methods confidently pseudo-label and learn from — the harm is unquantified.
- **Core Hypothesis:** Even modest contamination (10–20%) measurably degrades or destabilizes semi-supervised gains, harm concentrates in classes visually similar to contaminants, and a dual-filter pool curator restores near-clean performance — establishing contamination-robustness as a required evaluation axis.
- **Why Important:** The unlabeled pool is never curated in practice (curation defeats the purpose); robustness to dirty pools decides real-world viability.
- **Why Possibly Novel:** Open-set semi-supervised learning exists for classification; the dense-prediction damage quantification and pool-curation remedy are unestablished.
- **Minimal Experiment:** Inject controlled contamination fractions/types into unlabeled pools on two benchmarks; run 3 SSL methods ± the filter; map damage curves. Falsified if methods are naturally contamination-robust.
- **Main Risk:** Contamination taxonomy choices may not represent real dumps (mitigate with one genuinely raw hospital-style pool).
- **Cluster:** WSSL

### B-0182
- **One-sentence idea:** Quantify pseudo-label error heritability across self-training generations (which errors persist, amplify, or die out) and design error-decorrelated co-training informed by the heritability map.
- **Problem:** Confirmation bias in self-training is universally invoked but never dissected: nobody knows which error types are heritable (boundary bias? false positives near confusers?) versus self-correcting, so anti-bias mechanisms are designed blind.
- **Core Hypothesis:** Error heritability is strongly structured — systematic boundary displacements are near-perfectly inherited while sporadic interior errors wash out — implying targeted decorrelation (differing boundary inductive biases between co-trained models) beats generic model-diversity tricks.
- **Why Important:** Converts confirmation bias from a slogan into a measured mechanism with a targeted cure.
- **Why Possibly Novel:** Self-training analyses report aggregate metrics; a generational error-lineage study for dense prediction is unperformed.
- **Minimal Experiment:** Run 5 self-training generations, tracking per-pixel error lineages on validation volumes; classify error types by survival rate; test the targeted co-training. Falsified if heritability is unstructured.
- **Main Risk:** Lineage tracking requires careful bookkeeping; conclusions may vary with threshold policies.
- **Cluster:** WSSL

### B-0183
- **One-sentence idea:** Audit which consistency-regularization augmentations are label-semantics-preserving for medical images, and publish a validity-tested augmentation suite for anatomical data.
- **Problem:** Consistency regularization imports natural-image augmentations (flips, large rotations, color jitter) into medical semi-supervised pipelines where several are semantically invalid (laterality flips, orientation-breaking rotations, modality-meaningless color shifts) — models are trained to be invariant to transformations that should change the answer.
- **Core Hypothesis:** A validity audit will show standard suites contain harmful invariances whose removal improves semi-supervised medical segmentation, with the harm concentrated in laterality-sensitive and orientation-sensitive structures — and a physics/anatomy-validated suite will beat both full and minimal augmentation.
- **Why Important:** Nearly every medical SSL paper copies these suites; a validated replacement improves the whole line of work at zero method complexity.
- **Why Possibly Novel:** Augmentation validity is folk knowledge (related supervised issue in B-0007); a systematic invariance-validity audit for consistency training is missing.
- **Minimal Experiment:** Ablate augmentation families in a fixed SSL pipeline across 3 anatomies; stratify by laterality/orientation sensitivity. Falsified if invalid augmentations are harmless.
- **Main Risk:** Effects may be small at large labeled fractions (must test the low-label regime where SSL matters).
- **Cluster:** WSSL

### B-0184
- **One-sentence idea:** Replace the fixed pseudo-label confidence threshold with per-class dynamic quantile thresholds matched to the labeled-set class distribution, rescuing rare classes from threshold starvation.
- **Problem:** A single high threshold (e.g., 0.95) admits abundant easy-class pseudo-labels while rare/hard classes never clear it, so semi-supervised training amplifies class imbalance — rare-class recall stagnates or degrades while headline mIoU improves.
- **Core Hypothesis:** Setting thresholds as per-class confidence quantiles calibrated to match expected class frequencies yields large rare-class recall gains at minor precision cost, and the improvement grows with class-imbalance severity — a monotone, testable relationship.
- **Why Important:** Rare classes (small lesions, rare objects) are typically the point of the application; current SSL silently sacrifices them.
- **Why Possibly Novel:** Dynamic thresholding exists in classification SSL; the dense version with frequency-matched quantiles and imbalance-stratified evaluation is a concrete gap.
- **Minimal Experiment:** On one natural and one medical benchmark with long-tailed classes, swap fixed for quantile thresholds in a fixed pipeline; report per-class deltas vs. imbalance ratio. Falsified if fixed thresholds are rare-class-neutral.
- **Main Risk:** Expected class frequencies estimated from small labeled sets are noisy; needs smoothing.
- **Cluster:** WSSL

### B-0185
- **One-sentence idea:** Determine whether consistency regularization should operate in feature space or output space for dense prediction, with boundary quality as the discriminating metric.
- **Problem:** Semi-supervised segmentation methods apply consistency at whatever level is convenient; output-space consistency arguably over-smooths boundaries (penalizing legitimate boundary sensitivity to perturbations) while feature-space consistency may under-constrain semantics — the choice is never isolated experimentally.
- **Core Hypothesis:** Output-space consistency improves region metrics but degrades boundary sharpness relative to feature-space consistency at matched settings, and a boundary-exempt output consistency (masking the consistency loss near predicted boundaries) captures both benefits.
- **Why Important:** A default-choice question embedded in hundreds of pipelines, with a boundary cost nobody measures because evaluations emphasize region overlap.
- **Why Possibly Novel:** Consistency-level comparisons exist scattered in classification; the boundary-stratified dense analysis and the boundary-exempt variant are new.
- **Minimal Experiment:** Fixed pipeline; vary only consistency level (output/feature/hybrid/boundary-exempt); report region and boundary metrics separately on 2 datasets. Falsified if level doesn't matter or boundary effects are absent.
- **Main Risk:** Interactions with augmentation strength could confound (control by factorial sub-design).
- **Cluster:** WSSL

### B-0186
- **One-sentence idea:** Safe semi-supervised segmentation: pseudo-label inclusion governed by a statistical certificate ensuring the semi-supervised model is (with high confidence) no worse than the supervised-only baseline.
- **Problem:** Semi-supervised methods sometimes underperform supervised baselines (bad pools, mismatched assumptions), and practitioners cannot know in advance; in regulated domains an uncertain gain with possible regression is unusable, so SSL is simply avoided.
- **Core Hypothesis:** A held-out-risk-gated inclusion rule (admit pseudo-label batches only while a sequential test confirms non-inferiority on a small validation set) preserves most SSL upside while bounding downside at a chosen confidence — making SSL adoptable under risk constraints.
- **Why Important:** "Never worse" guarantees are the adoption threshold for clinical and safety-critical training pipelines.
- **Why Possibly Novel:** Safe SSL theory exists for classification with strong assumptions; a practical sequential-testing formulation for dense prediction is unbuilt.
- **Minimal Experiment:** On benchmarks where SSL is known to help and hurt (contaminated pools per B-0181), run gated vs. ungated SSL; verify the bound empirically across seeds. Falsified if gating destroys the upside or fails to bound downside.
- **Main Risk:** Small validation sets make the sequential test conservative; the theory-practice gap in the certificate.
- **Cluster:** WSSL

### B-0187
- **One-sentence idea:** Train segmentation from radiologists' eye-gaze recorded during routine reading, with a fixation-to-extent calibration model bridging the gap between where experts look and where lesions are.
- **Problem:** Expert gaze is a free byproduct of every read (with eye trackers), densely correlated with pathology location — but fixations mark points of interest, not extents, and naive gaze-heatmap supervision teaches blob-shaped lesions; the fixation-extent link is the unsolved piece.
- **Core Hypothesis:** A calibration model (learned on a small mask-annotated subset, mapping gaze dynamics + image evidence to extent) turns gaze into supervision worth a large fraction of full masks — quantifiable as masks-equivalent value per gaze-recorded case.
- **Why Important:** Converts routine clinical work into training data at zero marginal annotation cost — the ultimate annotation-efficiency play.
- **Why Possibly Novel:** Gaze-supervised localization has been probed; the fixation-to-extent calibration formulation with masks-equivalent accounting is a concrete missing mechanism.
- **Minimal Experiment:** Use a public gaze+image dataset (chest X-ray gaze corpora exist): train gaze-only, calibrated-gaze, and mask-supervised models; place calibrated gaze on the masks-equivalent scale. Falsified if calibration can't beat raw heatmap supervision.
- **Main Risk:** Gaze is contaminated by search behavior (looking at normal regions to rule things out).
- **Cluster:** WSSL

### B-0188
- **One-sentence idea:** Mine weak 3D localization labels from the synchronization between dictation audio timestamps and image scroll/zoom positions during clinical reading.
- **Problem:** When a radiologist says "8mm nodule right lower lobe" they are almost always displaying the relevant slice; this time-alignment between speech and viewport is recorded by PACS but discarded, leaving a massive weak-label stream unused.
- **Core Hypothesis:** Dictation-viewport alignment yields slice-level (and zoom-derived region-level) localization labels with quantifiable noise, sufficient to train detection-grade localization that transfers to segmentation warm-starting — at zero annotation cost beyond logging.
- **Why Important:** Unlocks supervision that scales with routine clinical throughput rather than annotation budgets.
- **Why Possibly Novel:** Report-text weak supervision is studied; the temporal viewport-speech alignment channel is essentially untouched (requires only logging infrastructure, no new labels).
- **Minimal Experiment:** Instrument a reading-simulation study (or use research PACS logs): quantify alignment precision between mention time and displayed slice; train slice-level localizer from alignment labels. Falsified if alignment noise swamps signal.
- **Main Risk:** Reading styles vary (some dictate after scrolling away); requires per-reader noise modeling.
- **Cluster:** WSSL

### B-0189
- **One-sentence idea:** Re-measure the scribble-supervision cost curve in the foundation-model era: how few scribbles suffice when combined with strong class-agnostic mask priors, and where does scribble information still matter?
- **Problem:** Scribble-supervised segmentation methods (and their reported label savings) predate strong promptable mask priors; the entire cost-benefit landscape has shifted, and current annotation-planning decisions rely on obsolete numbers.
- **Core Hypothesis:** With modern mask priors, scribble requirements drop by an order of magnitude for well-delineated classes, and residual scribble value concentrates on boundary-convention and low-contrast cases — reshaping optimal annotation policy from "scribble everything lightly" to "scribble only ambiguous structures."
- **Why Important:** Annotation budgets are allocated today using pre-foundation-model evidence; updated curves change real spending.
- **Why Possibly Novel:** Individual combinations exist (scribbles + SAM-style models); the systematic re-measurement of the cost curve with policy conclusions is missing.
- **Minimal Experiment:** Sweep scribble density × prior usage on 2 medical + 1 natural dataset; identify where the prior saturates scribble value. Falsified if priors don't shift the curve.
- **Main Risk:** Results tied to specific prior models; needs 2+ priors for robustness.
- **Cluster:** WSSL

### B-0190
- **One-sentence idea:** Centroid-only 3D lesion annotation: train segmentation from single center-point clicks per lesion with an expected-size prior and a count-preserving loss.
- **Problem:** Full 3D lesion masks cost minutes each; a centroid click costs a second, but naive point supervision collapses to tiny blobs or misses lesion multiplicity — and no method treats lesion count (which points give exactly) as the supervision to preserve.
- **Core Hypothesis:** Combining point supervision with (a) a size-distribution prior estimated from a small fully-masked subset and (b) a differentiable count-matching loss achieves lesion-level detection F1 near full-mask training, with volumetric accuracy trailing at a quantifiable cost — an explicit cost-fidelity tradeoff for annotation planning.
- **Why Important:** Multi-lesion diseases need counting more than exact volumes (B-0024); matching supervision to the clinically binding metric slashes cost.
- **Why Possibly Novel:** Point supervision exists in 2D natural images; the 3D lesion setting with count-preservation as the design principle is specific and open.
- **Minimal Experiment:** On a public multi-lesion dataset, train {points, points+size, points+size+count} vs. full masks; report lesion F1 and volume error separately. Falsified if points can't approach mask-level F1.
- **Main Risk:** Size priors mislead on atypical lesions; touching lesions break counting.
- **Cluster:** WSSL

### B-0191
- **One-sentence idea:** Treat incompletely annotated datasets (only some lesions masked per scan) as positive-unlabeled learning, jointly estimating per-image annotation completeness and training an unbiased dense classifier.
- **Problem:** Real lesion datasets are systematically incomplete (annotators mark index lesions, skip the rest); standard training treats unmarked lesions as negatives, actively teaching the model to suppress true positives — a pervasive, rarely corrected label pathology.
- **Core Hypothesis:** Dense PU-learning with a per-image completeness estimate (inferred from prediction-annotation discrepancy statistics) recovers most of the sensitivity lost to incomplete labels, and the estimated completeness maps flag which dataset portions are untrustworthy — audited against deliberately decimated full annotations.
- **Why Important:** Incomplete annotation is the norm, not the exception, in clinical datasets; correcting it improves everything trained downstream.
- **Why Possibly Novel:** PU learning is mature for classification; dense PU with completeness estimation and a decimation-based validation protocol is underdeveloped.
- **Minimal Experiment:** Take a fully annotated lesion dataset; randomly decimate annotations at known rates; compare standard vs. PU training against ground truth; check completeness-estimate accuracy. Fully controlled. Falsified if standard training is robust to decimation.
- **Main Risk:** Real incompleteness is non-random (small/faint lesions skipped), harder than random decimation — needs a biased-decimation condition too.
- **Cluster:** WSSL

### B-0192
- **One-sentence idea:** Sparse-slice 3D annotation with registration-guided label completion: annotate 3–5 optimally spaced slices per volume and complete labels via patient-specific deformable interpolation, training on completion-confidence-weighted targets.
- **Problem:** Full-volume annotation is the dominant cost in 3D; naive interpolation between sparse slices fails on curved/branching structures, and training pipelines cannot express "labeled here, inferred there" — so sparse annotation stays underexploited.
- **Core Hypothesis:** Deformable-registration-based completion (registering neighboring annotated slices through the volume) plus confidence-weighted training recovers ≥90% of dense-annotation performance at ≤20% cost for smooth organs, with the failure boundary (tubular/branching structures) predictable from inter-slice registration residuals.
- **Why Important:** Puts a validated number on the most natural 3D annotation shortcut and tells annotators when it is safe.
- **Why Possibly Novel:** Slice interpolation exists; the confidence-weighted training integration and the predictive failure boundary are the missing scientific pieces.
- **Minimal Experiment:** Simulate sparse annotation from dense public labels across organ types; sweep slice budgets; compare completion strategies; validate the failure predictor. Falsified if naive interpolation matches registration-guided completion.
- **Main Risk:** Registration quality varies with anatomy and pathology; the confidence model must be honest.
- **Cluster:** WSSL

### B-0193
- **One-sentence idea:** Speckle-native self-supervised pretraining for ultrasound: pretext tasks built on speckle statistics (decorrelation prediction, statistics-map estimation) instead of natural-image SSL recipes that treat speckle as noise.
- **Problem:** SSL recipes imported from natural images (color/blur augmentations, denoising pretexts) treat ultrasound speckle as nuisance noise, but speckle is a deterministic tissue signature carrying microstructure information — current pretraining destroys exactly the modality's information channel.
- **Core Hypothesis:** Pretexts that predict speckle statistics and their spatial evolution produce features that transfer better to ultrasound segmentation (especially of tissue-texture-defined boundaries) than natural-image SSL at matched compute — with the advantage vanishing on boundary types defined by macroscopic edges (a discriminating prediction).
- **Why Important:** Ultrasound is the world's most accessible modality and the worst-served by current pretraining conventions.
- **Why Possibly Novel:** Speckle physics is well studied in acoustics; its use as an SSL pretext design principle for deep features is essentially untouched.
- **Minimal Experiment:** Pretrain small twins (standard SSL vs. speckle-native) on unlabeled ultrasound; probe on 2 segmentation tasks with texture- vs. edge-defined boundaries. Falsified if speckle pretexts show no differential gain.
- **Main Risk:** Scanner post-processing (speckle reduction filters) may have already destroyed the statistics in available data.
- **Cluster:** WSSL

### B-0194
- **One-sentence idea:** Confidence-gated temporal label propagation for medical video (ultrasound sweeps, endoscopy): quantify propagation error accumulation and admit propagated labels into training only where multi-cue gates agree.
- **Problem:** Labeling one frame and tracking to neighbors is the obvious cheap supervision for medical video, but propagation errors accumulate silently (drift, occlusion, deformation), and training on drifted labels can be worse than training on fewer clean ones — the admit/reject decision has no principled solution.
- **Core Hypothesis:** Propagation error grows with measurable per-step signals (flow inconsistency, appearance change rate), and a gate trained on these signals admits a large fraction of propagated frames at near-clean label quality — beating both frame-only and ungated propagation at fixed annotation budget.
- **Why Important:** Medical video annotation is drastically underexploited because everyone fears drift; a validated gate unlocks it.
- **Why Possibly Novel:** Label propagation is old; the gate-centric formulation with drift forecasting and budget-matched comparison is the unclaimed practical core.
- **Minimal Experiment:** On a labeled ultrasound video dataset, propagate from sparse keyframes, measure true drift vs. gate signals, train with gated/ungated/frame-only labels. Falsified if drift is unpredictable or gating doesn't help.
- **Main Risk:** Gate signals may fail exactly during rapid probe motion where drift is worst.
- **Cluster:** WSSL

### B-0195
- **One-sentence idea:** Value-based curation of the unlabeled pool: estimate each unlabeled sample's marginal value to semi-supervised training and show that curated subsets beat the full pool.
- **Problem:** SSL folklore says more unlabeled data is better; but redundant, contaminated (B-0181), or distributionally skewed unlabeled samples can dilute or bias training — the per-sample value question is unasked, and pools are used wholesale.
- **Core Hypothesis:** Unlabeled-sample value is predictable from coverage statistics (novelty relative to labeled set, density in unlabeled pool, prediction instability), and a value-ranked 25% subset matches or beats the full pool while cutting compute proportionally — data curation beats data volume in SSL too.
- **Why Important:** Unlabeled data is free but training on it isn't; value-based curation converts SSL from a compute sink into a targeted tool.
- **Why Possibly Novel:** Data valuation exists for labeled data (influence functions, Shapley); unlabeled-pool valuation for dense SSL is unstudied.
- **Minimal Experiment:** Rank a pool by candidate value scores; train SSL on {random, top, bottom} quartiles; compare against full pool. Falsified if random subsets match value-ranked ones.
- **Main Risk:** Value scores may be method-dependent, requiring per-method calibration.
- **Cluster:** WSSL

### B-0196
- **One-sentence idea:** Expose labeled-split variance in semi-supervised segmentation benchmarks: re-run standard protocols across many labeled-subset draws and test whether published method gaps exceed split noise.
- **Problem:** SSL benchmarks fix one (or few) labeled subsets; at 1–5% label fractions, which specific images are labeled plausibly changes results more than method choice, meaning the literature's comparisons may be statistically vacuous — nobody has run the power analysis.
- **Core Hypothesis:** Across ≥20 labeled-split draws, within-method variance at low label fractions rivals or exceeds between-method gaps for a substantial share of published comparisons, and a variance-aware protocol (fixed split families + reporting standards) restores meaningful comparison.
- **Why Important:** If the field's evaluation can't statistically distinguish its methods, that's the single most important fact to publish about it.
- **Why Possibly Novel:** Split-variance concerns are whispered; the systematic power analysis with protocol prescription for dense SSL is undone.
- **Minimal Experiment:** 3 methods × 2 benchmarks × 20 splits at 1% and 5% labels; variance decomposition and significance testing of published-size gaps. Compute-heavy but conceptually trivial. Falsified if split variance is negligible.
- **Main Risk:** Compute cost; authors of affected methods will contest configurations.
- **Cluster:** WSSL

### B-0197
- **One-sentence idea:** Test whether anatomically impossible mixing augmentations (CutMix/CopyPaste across patients) help or hurt medical semi-supervised segmentation, against the assumption that unrealistic mixes are harmless regularization.
- **Problem:** Mixing augmentations are imported into medical SSL because they help on natural images; they produce anatomically impossible training inputs (a liver patch in a brain), and whether medical models pay a realism penalty — or benefit anyway — is asserted in both directions without controlled evidence.
- **Core Hypothesis:** Mixing benefits persist for texture-driven decisions but corrupt learned anatomical-layout priors (measurable via distal false positives per B-0023 and layout-probing), so anatomy-aware mixing (mixes restricted to plausible spatial contexts) retains the regularization while preserving layout knowledge.
- **Why Important:** Resolves a live methodological dispute with direct consequences for every medical SSL pipeline.
- **Why Possibly Novel:** Mixing ablations exist for accuracy only; the layout-prior corruption mechanism and anatomy-aware variant are untested.
- **Minimal Experiment:** Fixed SSL pipeline ± mixing ± anatomy-aware mixing; evaluate accuracy plus layout-probe metrics and distal FP rates. Falsified if impossible mixes are fully harmless.
- **Main Risk:** Layout corruption may only appear under distribution shift, requiring cross-site test sets.
- **Cluster:** WSSL

### B-0198
- **One-sentence idea:** Correct unlabeled-pool class skew in semi-supervised segmentation by distribution-aligned crop sampling — sampling unlabeled crops to match the labeled class geography rather than uniformly.
- **Problem:** Uniform crop sampling from unlabeled volumes/scenes oversamples dominant classes (background, large organs); pseudo-label training then reinforces the head, compounding the threshold starvation of B-0184 — the sampling layer itself is a hidden imbalance amplifier no one tunes.
- **Core Hypothesis:** Guiding unlabeled crop sampling with the current model's class-location predictions (oversampling probable-rare-class regions) improves rare-class semi-supervised gains substantially over uniform sampling at identical compute, with a self-correcting dynamic (as rare-class predictions improve, sampling improves).
- **Why Important:** A free, method-agnostic lever on the imbalance problem that plagues every dense SSL application.
- **Why Possibly Novel:** Class-balanced sampling exists for labeled data; model-guided unlabeled crop sampling with the feedback-dynamics analysis is unexplored.
- **Minimal Experiment:** Swap uniform for model-guided sampling in a fixed pipeline on an imbalanced benchmark; track per-class gains and the sampling-accuracy feedback over training. Falsified if sampling geography doesn't matter.
- **Main Risk:** Early bad predictions could lock in wrong sampling (needs exploration floor).
- **Cluster:** WSSL

### B-0199
- **One-sentence idea:** A stopping criterion for self-training rounds: predict the marginal gain of the next round from label-agreement statistics, ending the ritual of running a fixed number of rounds.
- **Problem:** Self-training pipelines run 2–3 rounds by convention; sometimes the second round helps, sometimes it quietly hurts, and there is no signal telling practitioners to continue or stop — wasted compute at best, degradation at worst.
- **Core Hypothesis:** Marginal round gain is predictable (sign and rough magnitude) from cheap statistics of consecutive-round pseudo-label agreement (volume of changed labels, direction of changes relative to model confidence), enabling a stop-rule that captures most achievable gain while avoiding degradation rounds.
- **Why Important:** Self-training is ubiquitous; a validated stop-rule improves reliability and saves compute across the board.
- **Why Possibly Novel:** Round-count is treated as a hyperparameter everywhere; the marginal-gain-forecasting formulation appears unstudied.
- **Minimal Experiment:** Run 6-round self-training across 8 dataset×method configurations; regress round-k+1 gains on round-k statistics; validate the stop-rule on held-out configurations. Falsified if gains are unforecastable.
- **Main Risk:** The forecast may not transfer across method families without recalibration.
- **Cluster:** WSSL

### B-0200
- **One-sentence idea:** Rigorously compare soft uncertainty-weighted consistency against hard confidence thresholding in dense SSL — a widely assumed superiority that has never been cleanly isolated.
- **Problem:** Papers adopt either hard thresholding or soft weighting of pseudo-supervision with cursory justification; the two interact differently with calibration error (weights inherit miscalibration continuously; thresholds only at the cutoff), and no controlled comparison isolates the choice across calibration regimes.
- **Core Hypothesis:** Soft weighting outperforms thresholding only when the model is reasonably calibrated (per B-0028, rarely true for small structures); under realistic miscalibration, thresholding is more robust — so the right choice is calibration-dependent and a recalibrate-then-weight scheme dominates both.
- **Why Important:** A foundational design choice in every dense SSL method, currently made by fashion.
- **Why Possibly Novel:** The calibration-dependence hypothesis and the recalibrate-then-weight resolution are specific and untested.
- **Minimal Experiment:** Fixed pipeline; {hard, soft, recalibrated-soft} × {well/poorly calibrated models (controlled via training length)}; 2 datasets. Falsified if the choice is calibration-independent.
- **Main Risk:** Calibration manipulation may covary with accuracy, confounding attribution.
- **Cluster:** WSSL

### B-0201
- **One-sentence idea:** Co-training on genuinely independent views (frontal/lateral X-rays, multi-parametric MRI sequences) versus artificially augmented views, quantifying how much real view independence is worth.
- **Problem:** Co-training theory requires conditionally independent views, but practice fakes them with augmentations of one image; medical imaging uniquely offers true independent views of the same anatomy, yet nobody has measured the real-vs-fake independence gap that theory says should exist.
- **Core Hypothesis:** Co-training across physically independent views yields larger and more robust semi-supervised gains than augmentation-based view pairs at matched settings, with the gap growing as label fraction shrinks — empirically vindicating (or refuting) the independence assumption's practical value.
- **Why Important:** Either validates a theoretically principled route to better medical SSL or shows the celebrated independence assumption doesn't matter — both change practice.
- **Why Possibly Novel:** Multi-view medical co-training exists in instances; the controlled real-vs-augmented independence comparison is the untested scientific core.
- **Minimal Experiment:** On paired-view datasets (multi-sequence MRI), co-train with {true second view, augmented first view} at several label fractions. Falsified if fake views match real ones.
- **Main Risk:** True views also differ in information content (not just independence), needing information-matched controls.
- **Cluster:** WSSL

### B-0202
- **One-sentence idea:** Map how far single-atlas semi-supervision can go: one labeled volume + registration-propagated labels + modern self-training, benchmarked honestly against 10%-labeled baselines.
- **Problem:** The "barely supervised" regime (one labeled case) is served by either classical atlas propagation or modern SSL, never their disciplined combination; claims about minimum-label requirements for new structures rest on no systematic evidence.
- **Core Hypothesis:** The combination (atlas propagation for initialization, uncertainty-gated self-training for refinement) achieves within-striking-distance performance of 10%-labeled training for spatially regular structures, with the single-case choice (which case to label) mattering enormously — measurable as case-selection variance.
- **Why Important:** Defines the true lower bound of annotation for new segmentation tasks — the first question every new project asks.
- **Why Possibly Novel:** Both components are old; the honest combined benchmark with case-selection analysis and structure-type stratification is missing.
- **Minimal Experiment:** For 5 structures, run the combination from each of 10 different single labeled cases; compare to 1%/10% baselines; quantify selection variance. Falsified if the combination stalls far below 10% baselines.
- **Main Risk:** Results heavily structure-dependent; must resist overgeneralizing from easy organs.
- **Cluster:** WSSL

### B-0203
- **One-sentence idea:** Weakly supervised lesion localization by counterfactual comparison against a patient-matched normal appearance model, using only image-level "pathology present" labels.
- **Problem:** Image-level weak supervision via CAMs highlights discriminative (not complete) regions and fails for diffuse pathology; but medicine has a structure natural images lack — a well-defined "normal" appearance per anatomical location — that CAM-style methods never exploit.
- **Core Hypothesis:** Training a normal-appearance model (on healthy-labeled scans) and localizing pathology as calibrated deviation-from-normal, gated by the image-level label, yields more complete lesion extents than CAM derivatives — with the advantage largest for diffuse/multi-focal disease where CAMs are worst.
- **Why Important:** Image-level labels exist at population scale (billing codes, report conclusions); completeness of weak localization is the blocker to using them for segmentation.
- **Why Possibly Novel:** Anomaly detection and weak supervision are separate literatures; their principled fusion with completeness-focused evaluation (not just pointing accuracy) is underexplored.
- **Minimal Experiment:** On a dataset with image labels + hidden masks, compare CAM-family vs. counterfactual-deviation localization on completeness metrics, stratified by lesion diffuseness. Falsified if CAMs match on diffuse disease.
- **Main Risk:** Normal-model quality varies across anatomy; deviation maps flag artifacts as pathology.
- **Cluster:** WSSL

### B-0204
- **One-sentence idea:** Boundary-segment annotation: annotators trace only the boundary segments the model is uncertain about, with interiors and confident boundaries auto-completed — training on heterogeneous-density supervision.
- **Problem:** Full-contour annotation wastes most effort on boundary segments any model gets right; there is no annotation protocol or training formulation for "supervise only the hard 20% of the boundary," though uncertainty maps make the hard segments identifiable in advance.
- **Core Hypothesis:** Uncertainty-targeted boundary annotation achieves full-annotation boundary quality at a fraction of tracing length, and a mixed-density training loss (strong on annotated segments, weak elsewhere) avoids the degenerate solutions naive partial supervision produces — establishing per-segment marginal annotation value.
- **Why Important:** Boundary tracing is the most time-consuming annotation primitive; targeting it where it matters is the most direct efficiency lever.
- **Why Possibly Novel:** Partial annotation exists at image/region level; boundary-segment-level targeting with marginal-value accounting appears unformulated.
- **Minimal Experiment:** Simulate partial boundary annotation from dense labels (keep segments where a baseline is uncertain); train mixed-density models across kept-fractions; plot the quality-vs-tracing-length curve. Falsified if random segment selection matches uncertainty-targeted selection.
- **Main Risk:** Real annotator time may not scale with tracing length as assumed (context acquisition overhead).
- **Cluster:** WSSL

### B-0205
- **One-sentence idea:** Quantify patch-grid artifacts in ViT self-supervised features as a dense-prediction bottleneck and remove them via sub-patch offset-ensembled distillation.
- **Problem:** SSL ViT features exhibit patch-grid quantization artifacts (features constant within patches, discontinuous at patch borders); dense downstream tasks inherit blocky boundaries, and the artifact's cost is confounded with everything else — never isolated or systematically removed.
- **Core Hypothesis:** Grid artifacts account for a measurable fraction of boundary error in frozen-feature segmentation (isolable by evaluating boundaries at patch-border vs. patch-interior positions), and distilling an offset-ensembled teacher (features averaged over sub-patch shifts) into a student removes most of it cheaply.
- **Why Important:** Frozen SSL features are becoming the universal substrate for dense tasks (see B-0129); a systematic artifact and its removal affect everything built on them.
- **Why Possibly Novel:** Grid artifacts are informally known; the border-position-stratified quantification and the offset-distillation fix are concrete and unpublished.
- **Minimal Experiment:** Evaluate frozen-feature segmentation boundary error stratified by position relative to patch grid; distill offset-ensembled features; re-evaluate. Falsified if boundary error is grid-position-independent.
- **Main Risk:** Distillation may smooth away genuine high-frequency features along with artifacts.
- **Cluster:** WSSL

### B-0206
- **One-sentence idea:** Physics-based acquisition augmentation (simulated kernel, dose, sequence changes) as the consistency perturbation for medical semi-supervised learning, replacing photometric jitter.
- **Problem:** Consistency training teaches invariance to whatever perturbations it uses; photometric jitter teaches invariance to transformations that never occur clinically while missing the acquisition variations that do — the perturbation set is misaligned with the deployment shift set.
- **Core Hypothesis:** Consistency over physics-simulated acquisition perturbations yields models with substantially smaller cross-protocol degradation than photometric consistency at equal in-domain performance — semi-supervised learning and robustness training unified through perturbation choice.
- **Why Important:** Aligns SSL's implicit invariance curriculum with the actual deployment threat model, at no extra labeled cost.
- **Why Possibly Novel:** Physics augmentation exists for supervised robustness (B-0011); as the consistency mechanism in SSL with cross-protocol evaluation, it is untested.
- **Minimal Experiment:** Fixed SSL pipeline; swap perturbation sets; evaluate in-domain and cross-protocol on public multi-protocol data. Falsified if perturbation choice doesn't shape robustness.
- **Main Risk:** Simulation realism limits (see B-0011); some acquisition effects can't be simulated post hoc from images.
- **Cluster:** WSSL

### B-0207
- **One-sentence idea:** Factorial dissection of noise types in noisy-student self-training for segmentation: which perturbation channel (input noise, feature dropout, label perturbation, depth/stochastic path) actually drives the dense-prediction gains.
- **Problem:** Noisy-student recipes bundle multiple noise sources; for dense prediction, each channel plausibly acts differently (input noise → invariance, feature dropout → capacity, label perturbation → decision-boundary smoothing), but the bundle is adopted wholesale and its active ingredients for segmentation are unknown.
- **Core Hypothesis:** The channels are far from interchangeable — a factorial will show most segmentation gain comes from one or two channels (predicted: feature-level noise), and channel-specific effects differ for region vs. boundary metrics — enabling leaner, better-targeted recipes.
- **Why Important:** Recipe dissection reduces compute and reveals mechanism; bundled recipes propagate superstition.
- **Why Possibly Novel:** Noisy-student ablations exist for classification; the dense-metric-stratified factorial is unrun.
- **Minimal Experiment:** 2^4 factorial over noise channels in a fixed self-training pipeline on 2 datasets; region/boundary metrics separately. Falsified if channels are additive and interchangeable.
- **Main Risk:** Interactions may require fractional-factorial extension; conclusions could be dataset-scale-dependent.
- **Cluster:** WSSL

### B-0208
- **One-sentence idea:** Human verification (1-second accept/reject of pseudo-labels) as the supervision channel: quantify the value-per-second of verification versus annotation in dense SSL.
- **Problem:** The human effort spectrum between "no labels" and "full masks" contains an almost-free primitive — glancing at a pseudo-label and accepting/rejecting it — whose supervision value for dense training has never been measured against the annotation it displaces.
- **Core Hypothesis:** Verification-filtered pseudo-labels (rejects discarded or down-weighted) buy more final accuracy per human-second than spending the same seconds on fewer full annotations, in the regime where the base pseudo-labeler is decent — with the crossover point (when to switch from verifying to annotating) measurable and practically usable.
- **Why Important:** Optimal allocation of human seconds is the real objective of all label-efficient learning; verification is its cheapest unstudied instrument.
- **Why Possibly Novel:** Verification appears inside annotation tools; as a formally evaluated supervision primitive with value-per-second accounting for dense SSL, it is unstudied.
- **Minimal Experiment:** Timed study: annotators either verify pseudo-labels or annotate from scratch under equal time budgets; train on both outputs; compare. Falsified if verification-time converts to less accuracy than annotation-time everywhere.
- **Main Risk:** Verification quality depends on display/UX; rejects may correlate with exactly the hard cases training needs.
- **Cluster:** WSSL

### B-0209
- **One-sentence idea:** Longitudinal self-supervision from clinical archives: enforce prediction consistency on anatomy that a learned stability-detector deems unchanged between a patient's successive scans.
- **Problem:** Archives hold millions of longitudinal scan pairs where most anatomy is unchanged; unlike controlled test-retest pairs (B-0014), real intervals include genuine change, so naive consistency would penalize correct change detection — the stable/changed decomposition is the missing piece that makes archive-scale consistency usable.
- **Core Hypothesis:** A jointly learned stability detector (identifying unchanged regions from image evidence) plus consistency only on stable regions extracts robust supervision from raw archives, improving segmentation stability and cross-protocol robustness (longitudinal pairs often span protocol changes — free paired-shift data).
- **Why Important:** Converts the largest existing unlabeled resource (hospital archives) into targeted supervision using its unique longitudinal structure.
- **Why Possibly Novel:** Longitudinal consistency exists in specific pipelines; the stability-gated formulation for general archive-scale self-supervision is open.
- **Minimal Experiment:** On public longitudinal data, train ± stability-gated consistency; evaluate accuracy, scan-rescan stability, and cross-protocol transfer; verify the gate against annotated change. Falsified if gating can't separate change from noise.
- **Main Risk:** Stability detector errors leak change into consistency targets, suppressing sensitivity to real change.
- **Cluster:** WSSL

### B-0210
- **One-sentence idea:** Map the label-budget boundary where semi-supervised segmentation stops paying: a multi-task empirical law for when unlabeled data adds nothing over the labeled set alone.
- **Problem:** SSL papers evaluate at 1–10% label fractions where gains are large; practitioners with moderate budgets (say 500 labeled volumes) have no evidence whether SSL is worth its complexity — the gain-vs-labeled-size decay curve is unmapped across tasks.
- **Core Hypothesis:** SSL gain decays with labeled-set size following a task-dependent but shape-consistent curve whose decay constant is predictable from task properties (class rarity, boundary ambiguity), yielding a practical rule for whether a given project should bother with SSL.
- **Why Important:** Saves enormous practitioner effort by replacing "SSL always helps" folklore with a quantitative applicability boundary.
- **Why Possibly Novel:** Individual papers show a few label fractions; the cross-task decay-law synthesis with property-based prediction is missing.
- **Minimal Experiment:** For 5 tasks, sweep labeled size across 2 orders of magnitude with a fixed strong SSL method; fit decay curves; test the property-based prediction on a sixth task. Falsified if decay shapes are inconsistent.
- **Main Risk:** Conclusions tied to the chosen SSL method's strength; needs a second method for robustness.
- **Cluster:** WSSL
## Section 8 — Synthetic Data [B-0211–B-0240]

### B-0211
- **One-sentence idea:** Audit mask-image misalignment in diffusion-generated segmentation training data and show that alignment-aware filtering beats generating more data.
- **Problem:** Mask-conditioned diffusion produces images that deviate from their conditioning masks (objects extending past, missing, or displaced); training pipelines consume these pairs as if perfectly labeled, injecting systematic boundary noise that is worse than random label noise because it is generator-structured.
- **Core Hypothesis:** Measured misalignment (via an independent segmenter's disagreement with the conditioning mask) is substantial and class-dependent, its inclusion measurably degrades boundary learning, and filtering the worst-aligned fraction beats doubling the generation volume — quality dominates quantity through the alignment channel.
- **Why Important:** Mask-conditioned generation is becoming a default data-augmentation tool; unmeasured label corruption at the source poisons everything downstream.
- **Why Possibly Novel:** Generation quality is assessed by realism metrics, not by conditioning fidelity; the alignment audit and the filter-vs-volume comparison are unperformed.
- **Minimal Experiment:** Generate a mask-conditioned synthetic set; score alignment with an independent model; train on {all, filtered, 2× all}; compare boundary metrics. Falsified if misalignment is negligible or harmless.
- **Main Risk:** The alignment scorer's own biases could drive the filtering (use two independent scorers).
- **Cluster:** Synth

### B-0212
- **One-sentence idea:** Demonstrate and defeat the blending-artifact shortcut: models trained on lesions inpainted into healthy scans learn to detect inpainting boundaries, not lesions.
- **Problem:** Inpainting lesions into healthy backgrounds is a popular augmentation, but the composite boundary carries subtle generator artifacts; a model can achieve high synthetic-set accuracy by keying on artifacts and then fail on real lesions — a shortcut nobody routinely tests for.
- **Core Hypothesis:** A classifier trained to distinguish inpainted from real patches will succeed far above chance (the artifact exists), lesion models trained on inpainted data will show inflated synthetic-set and depressed real-set performance proportional to that artifact detectability, and artifact-suppressed generation (adversarial blending against the artifact classifier) closes most of the real-set gap.
- **Why Important:** The shortcut silently invalidates a widely used medical augmentation strategy; the detectability score gives the field a routine hygiene check.
- **Why Possibly Novel:** Shortcut learning is documented generally; the inpainting-boundary instance with a quantitative detectability-predicts-transfer-gap law is specific and untested.
- **Minimal Experiment:** Train the artifact classifier on one public inpainting pipeline; correlate its AUROC with the synth-to-real generalization gap across generation settings. Falsified if artifacts are undetectable or uncorrelated with the gap.
- **Main Risk:** Artifact detectability varies enormously across inpainting methods; needs several.
- **Cluster:** Synth

### B-0213
- **One-sentence idea:** Estimate the real-synthetic exchange rate — how many synthetic samples substitute for one real labeled sample — as a measurable function of generator, task, and domain.
- **Problem:** Synthetic data decisions (generate vs. annotate) are made without a currency: the marginal value of a synthetic sample relative to a real one is unknown, unmeasured, and assumed constant, though it plainly varies by task and generator.
- **Core Hypothesis:** The exchange rate is well-defined via matched learning curves (real-only vs. mixed), varies by an order of magnitude across tasks/generators, degrades with synthetic volume (diminishing exchange), and is predictable from cheap proxies (distributional distance, alignment per B-0211) — enabling annotate-vs-generate budget decisions.
- **Why Important:** Puts synthetic data on an economic footing; every data-strategy meeting needs this number.
- **Why Possibly Novel:** Scattered comparisons exist; the formal exchange-rate methodology with proxy-based prediction is unestablished.
- **Minimal Experiment:** For 3 tasks × 2 generators, fit learning curves over real/synthetic mixing grids; extract exchange rates; test proxy predictions. Falsified if exchange rates are unstable or unpredictable.
- **Main Risk:** Exchange rates may depend on the real-data regime (helpful only below some real-data size), complicating the summary.
- **Cluster:** Synth

### B-0214
- **One-sentence idea:** Build a utility-predictive quality metric for synthetic segmentation data, benchmarked by correlation with actual downstream training gains — replacing FID, which predicts nothing about dense-task utility.
- **Problem:** Synthetic data is graded by realism metrics (FID-family) that ignore label alignment, coverage of decision-relevant variation, and class balance; teams optimize generators against metrics uncorrelated with what they actually need — downstream segmentation improvement.
- **Core Hypothesis:** Downstream utility is predicted far better by a composite of task-anchored measures (feature-space coverage gain over the real training set, mask-alignment score, boundary-frequency content match) than by FID, with correlation strong enough to steer generator selection without training downstream models.
- **Why Important:** A valid quality signal redirects the entire synthetic-data-for-vision pipeline from beauty contests to utility.
- **Why Possibly Novel:** FID's inadequacy is suspected widely; a validated dense-task utility metric with a public correlation benchmark does not exist.
- **Minimal Experiment:** Assemble 20 synthetic sets (varying generators/settings); train downstream on each; correlate candidate metrics with observed gains. Falsified if nothing beats FID (itself informative).
- **Main Risk:** Metric validity may not transfer across task families; needs held-out task validation.
- **Cluster:** Synth

### B-0215
- **One-sentence idea:** Label-first pathology synthesis: sample plausible label maps from anatomical+disease shape models, then render images conditioned on them — extending SynthSeg-style generation from anatomy to lesions with controllable rare-configuration coverage.
- **Problem:** Image-first generation inherits the training distribution's gaps (rare lesion locations/sizes/multiplicities stay rare); label-first generation can deliberately enumerate rare configurations, but principled generative models of pathological label geometry (where lesions can plausibly occur, how they deform anatomy) are missing.
- **Core Hypothesis:** A label-geometry model built from epidemiological priors (location/size distributions) plus mechanical plausibility rules, feeding a label-conditioned renderer, improves rare-configuration segmentation (unusual locations, multiplicity extremes) far more than image-first generation at matched volume — because coverage, not realism, is the binding constraint.
- **Why Important:** Rare configurations are where models fail and where real data can never be dense; deliberate coverage is the only scalable answer.
- **Why Possibly Novel:** SynthSeg established label-first for anatomy; the pathological-geometry extension with coverage-targeted evaluation is open.
- **Minimal Experiment:** Build a simple lesion-geometry sampler for one organ; train on label-first vs. image-first synthetic sets; evaluate on a rare-configuration-enriched real test set. Falsified if realism-first matches coverage-first on rare cases.
- **Main Risk:** Renderer quality on out-of-distribution label maps may degrade exactly where coverage is extended.
- **Cluster:** Synth

### B-0216
- **One-sentence idea:** Audit generative memorization leakage in synthetic medical datasets — near-copies of real patients surfacing in released synthetic sets — and its double harm: privacy breach and benchmark contamination.
- **Problem:** Institutions release "privacy-safe" synthetic datasets from generators trained on private data; diffusion memorization means some samples are near-copies of real patients, simultaneously violating the privacy claim and contaminating any benchmark whose test patients were in generator training — neither harm is being measured at release time.
- **Core Hypothesis:** Standard released synthetic sets contain detectable near-duplicates of generator-training patients at non-negligible rates (findable via embedding-space nearest-neighbor auditing against the training pool), and their removal measurably changes downstream benchmark results — establishing mandatory release-time auditing.
- **Why Important:** One demonstrated leak would reshape synthetic-data-release governance; the audit tool is the deliverable either way.
- **Why Possibly Novel:** Diffusion memorization is documented for natural images; the medical synthetic-release audit with the dual privacy/contamination framing is unperformed.
- **Minimal Experiment:** Train a generator on a known corpus; audit its synthetic output for near-copies at several training-set sizes and duplication levels; validate the audit's detection power. Fully controlled. Falsified if memorization is absent under realistic settings.
- **Main Risk:** Embedding-based duplicate detection has contestable thresholds (mitigate with human verification of flagged pairs).
- **Cluster:** Synth

### B-0217
- **One-sentence idea:** Map the domain-randomization-versus-realism frontier for dense prediction: randomization wins when the target domain is unknown, realism when it is known — quantified as a function of target-domain knowledge.
- **Problem:** The synthetic-data community splits into randomization (vary everything) and realism (match the target) camps, both supported by anecdotes; the obvious reconciliation — the answer depends on how much you know about the target — has never been formalized or measured for segmentation.
- **Core Hypothesis:** With target-domain knowledge parameterized (none / distributional statistics / a few images), optimal generation interpolates from full randomization to matched realism along a measurable frontier, and mis-matching strategy to knowledge level costs a predictable performance penalty.
- **Why Important:** Converts a sterile ideological dispute into a lookup rule practitioners can apply.
- **Why Possibly Novel:** Both strategies are studied separately; the knowledge-conditional frontier with controlled information levels is an unclaimed synthesis.
- **Minimal Experiment:** One rendering pipeline with a randomization-realism dial; three target-knowledge conditions; evaluate on two real target domains. Falsified if one strategy dominates at all knowledge levels.
- **Main Risk:** The dial's parameterization may not span the strategies fairly.
- **Cluster:** Synth

### B-0218
- **One-sentence idea:** Determine where synthetic data belongs in the training pipeline — pretraining, joint mixing, or fine-tuning stage — and whether the common "synthetic-then-real" curriculum is actually optimal.
- **Problem:** Synthetic data is inserted into pipelines at arbitrary stages by habit; stage placement changes what the model retains (early synthetic may be overwritten; late synthetic may dominate), and no controlled study isolates placement from volume for dense tasks.
- **Core Hypothesis:** Placement effects are large and systematic: synthetic-first pretraining contributes robust low-level features that survive real-data fine-tuning, while late-stage synthetic injection distorts decision boundaries — so synthetic-early/real-late dominates, except for rare-class synthesis (B-0231) which must appear late to avoid being overwritten.
- **Why Important:** A placement rule multiplies the value of every synthetic dataset at zero generation cost.
- **Why Possibly Novel:** Curriculum research and synthetic data intersect only anecdotally; the stage-placement factorial with retention analysis (what survives fine-tuning) is unrun.
- **Minimal Experiment:** Fixed synthetic+real budgets; permute placement schedules; measure final performance plus feature-retention probes. Falsified if placement is irrelevant at matched volumes.
- **Main Risk:** Conclusions may depend on relative volumes (needs a volume-ratio sweep).
- **Cluster:** Synth

### B-0219
- **One-sentence idea:** Counterfactual patient pairs — the same anatomy rendered with and without a lesion — as causal supervision that breaks co-occurrence shortcuts in lesion segmentation.
- **Problem:** Real datasets confound lesions with their contexts (disease co-occurs with age-related changes, certain scanners, treatment artifacts); models learn these shortcuts and fail on lesions in unfamiliar contexts, and real data can never provide the counterfactual (same patient, no lesion) needed to break the confound.
- **Core Hypothesis:** Training with generated counterfactual pairs (enforcing identical predictions outside the lesion and correct delineation inside) measurably reduces context-shortcut reliance — quantified by performance on context-swapped test cases (lesions transplanted into atypical contexts) where standard-trained models fail.
- **Why Important:** Shortcut dependence is a primary cause of clinical-deployment brittleness; counterfactual supervision is the direct causal remedy.
- **Why Possibly Novel:** Counterfactual generation exists for explanation and classification-bias work; its use as paired training supervision for dense prediction with context-swap evaluation is largely untested.
- **Minimal Experiment:** Build counterfactual pairs via lesion inpainting/removal (with B-0212's artifact control); train paired vs. standard; evaluate on context-swapped tests. Falsified if paired training doesn't reduce context sensitivity.
- **Main Risk:** Generation artifacts could introduce a new shortcut replacing the old one.
- **Cluster:** Synth

### B-0220
- **One-sentence idea:** Procedural (simulation-grown, generative-model-free) vascular and airway trees as topology-rich pretraining data for tubular-structure segmentation.
- **Problem:** Tubular segmentation fails on topology (B-0002), partly because real annotated trees are few and topologically undersampled; learned generative models reproduce the same undersampling, whereas procedural growth models (angiogenesis simulations, L-systems with physiological constraints) can produce unlimited topologically diverse, perfectly labeled trees — an option the deep-learning era has largely ignored.
- **Core Hypothesis:** Pretraining on procedurally grown trees rendered with simple appearance models transfers topological competence (connectivity, branching statistics) to real vessel/airway tasks, beating both no-pretraining and generic-image pretraining specifically on topology metrics — because topology, unlike appearance, transfers from procedural data intact.
- **Why Important:** Topology is the clinically binding property of trees and the hardest to learn from scarce real data.
- **Why Possibly Novel:** Procedural anatomy appears in isolated works; the topology-transfer hypothesis with topology-stratified evaluation is a clean untested claim.
- **Minimal Experiment:** Grow 10k procedural trees; pretrain; fine-tune on small real sets; compare Betti/connectivity errors vs. baselines. Falsified if topological gains don't transfer.
- **Main Risk:** Appearance gap may prevent transfer despite topological validity (test with appearance randomization).
- **Cluster:** Synth

### B-0221
- **One-sentence idea:** Confusion-conditioned hard-negative synthesis: generate near-miss negatives targeted at the model's current false-positive modes, as an adversarial curriculum for dense prediction.
- **Problem:** False positives cluster on specific look-alikes (vessels mistaken for lesions, shadows for smoke); real data contains too few borderline negatives to teach the distinction, and untargeted generation reproduces the easy majority rather than the informative boundary cases.
- **Core Hypothesis:** Generating negatives conditioned on the model's own FP embeddings ("more things like what fools it, verified lesion-free") reduces the targeted FP mode several times faster per training sample than untargeted synthetic negatives — and iterating this loop drives FP modes down sequentially without inflating FN rates.
- **Why Important:** FP reduction is the deployment bottleneck for screening systems; sample-efficient targeted synthesis attacks it directly.
- **Why Possibly Novel:** Hard-negative mining is classic on real data; closed-loop generative hard-negative synthesis for dense prediction with per-mode tracking is largely unexplored.
- **Minimal Experiment:** Identify top-3 FP modes of a lesion detector; generate targeted vs. untargeted negatives at equal volume; retrain and compare per-mode FP reduction. Falsified if targeting doesn't beat volume.
- **Main Risk:** The verified-negative requirement (generated negatives must truly lack lesions) needs careful QC; loop may oscillate.
- **Cluster:** Synth

### B-0222
- **One-sentence idea:** Measure the thin-structure fidelity floor of latent diffusion (structures below which latent compression destroys them) and establish when pixel-space generation is required for training data.
- **Problem:** Latent diffusion dominates synthesis for cost reasons, but its autoencoder compresses away structures near or below the latent grid scale (thin vessels, hairline cracks, fine membranes); synthetic sets silently lack exactly the structures many segmentation tasks target, and nobody publishes the fidelity floor.
- **Core Hypothesis:** There is a sharp, measurable width threshold (in pixels, generator-specific) below which structures are absent or corrupted in latent-generated images, models trained on such data show a corresponding blind spot on real thin structures, and pixel-space or cascaded generation removes it — making the floor a required datasheet property for any generator used in dense tasks.
- **Why Important:** Prevents a whole category of silent dataset defects in the fastest-growing data source.
- **Why Possibly Novel:** Latent compression artifacts are known qualitatively; the quantitative floor measurement linked to downstream blind spots is unpublished.
- **Minimal Experiment:** Generate images containing calibrated-width structures via conditioning; measure survival vs. width across generators; train on latent- vs. pixel-generated data and compare thin-structure recall. Falsified if no floor exists within task-relevant widths.
- **Main Risk:** Conditioning may itself fail at thin widths, confounding generation vs. conditioning limits.
- **Cluster:** Synth

### B-0223
- **One-sentence idea:** Quantify when synthetic validation sets can be trusted for model selection: measure rank correlation between synthetic-val and real-val decisions across realistic model pools.
- **Problem:** Teams short on labeled data use synthetic sets not just for training but for validation and model selection — a far more dangerous use, since selection errors are silent and systematic (synthetic val favors models that fit the generator's biases); the practice spreads with zero validity evidence.
- **Core Hypothesis:** Synthetic-val rank correlation with real-val is high for coarse decisions (architecture family) but collapses for fine decisions (checkpoint selection, hyperparameters near optimum), and correlates with generator-real distributional distance — yielding concrete rules for what synthetic validation may and may not decide.
- **Why Important:** Bad model selection silently caps every project; validity boundaries for a spreading practice are urgent hygiene.
- **Why Possibly Novel:** Synthetic training is studied extensively; synthetic evaluation validity for dense prediction has almost no literature.
- **Minimal Experiment:** Pool 50 model variants on 2 tasks; rank by synthetic and real validation; compute correlation by decision granularity. Falsified if correlations are uniformly high (practice vindicated) — also valuable.
- **Main Risk:** Results depend on generator quality; needs a generator-quality sweep for the distance claim.
- **Cluster:** Synth

### B-0224
- **One-sentence idea:** Map the differential-privacy-versus-utility frontier for synthetic medical segmentation data: how much downstream Dice survives at meaningful privacy budgets.
- **Problem:** DP-trained generators promise provably private synthetic data, but DP noise degrades exactly the fine structures segmentation needs; the epsilon-vs-downstream-utility curve for dense tasks is unmeasured, so institutions cannot make informed privacy-utility choices and either over-share or refuse to share.
- **Core Hypothesis:** The frontier is strongly task-dependent — organ-scale segmentation survives strict budgets while small-lesion tasks collapse early — and hybrid schemes (DP for rare identifying features, non-DP for common anatomy statistics) dominate uniform DP at matched formal guarantees.
- **Why Important:** Data-sharing policy decisions worth millions of patient records hinge on this unmeasured curve.
- **Why Possibly Novel:** DP generative modeling is studied for classification utility; the dense-prediction frontier with the task-stratification and hybrid-mechanism claims is open.
- **Minimal Experiment:** Train DP generators at several epsilon values on one corpus; train segmenters on each synthetic set; plot utility-vs-epsilon for organ and lesion tasks. Falsified if utility is epsilon-flat or uniformly destroyed.
- **Main Risk:** DP generative training is finicky; failures may reflect optimization rather than fundamental limits.
- **Cluster:** Synth

### B-0225
- **One-sentence idea:** Determine the minimum replay fidelity for generative replay in continual segmentation: how good must replayed synthetic data be to prevent forgetting of old tasks/domains?
- **Problem:** Generative replay (synthesizing old-task data instead of storing it) is the privacy-compatible answer to continual learning, but it inherits an unquantified assumption — that the generator is good enough — and nobody knows the fidelity threshold below which replay fails, so systems discover failure only in production.
- **Core Hypothesis:** Forgetting prevention depends on replay fidelity through a measurable threshold curve, the binding fidelity dimension is label-conditional structure (right classes in right places) rather than photorealism, and a cheap fidelity probe predicts replay adequacy before deployment.
- **Why Important:** Gives continual-learning practitioners a pre-deployment adequacy test instead of faith.
- **Why Possibly Novel:** Generative replay papers report end metrics; the fidelity-threshold decomposition (what aspect of replay quality matters) is unstudied for dense tasks.
- **Minimal Experiment:** Degrade replay data along controlled axes (photorealism, label alignment, class balance); measure forgetting for each axis; validate the adequacy probe. Falsified if forgetting is insensitive to fidelity axes.
- **Main Risk:** Axis degradations may not decompose cleanly (interactions).
- **Cluster:** Synth

### B-0226
- **One-sentence idea:** Factorial dissection of copy-paste augmentation harmonization: which components (lighting match, noise match, boundary blending, geometric plausibility) actually drive dense-prediction gains, and which merely hide detectable paste artifacts.
- **Problem:** Copy-paste is among the most effective segmentation augmentations, decorated with harmonization steps of untested value; simultaneously, paste artifacts risk shortcut learning (models detecting pastedness, cf. B-0212) — the component-wise cost-benefit is unknown.
- **Core Hypothesis:** A factorial will show most of copy-paste's gain survives with zero harmonization (the gain is from layout diversity, not realism), harmonization's main effect is reducing artifact detectability rather than improving accuracy, and geometric plausibility (paste location priors) is the one component with real accuracy impact.
- **Why Important:** Simplifies a ubiquitous augmentation to its active ingredients and installs an artifact-hygiene check.
- **Why Possibly Novel:** Copy-paste is used everywhere but dissected nowhere; the realism-vs-layout attribution is a clean open question.
- **Minimal Experiment:** 2^4 factorial over harmonization components on 2 benchmarks, plus artifact-detectability measurement per cell. Falsified if all components matter equally.
- **Main Risk:** Component effects may differ between natural and medical domains (run one of each).
- **Cluster:** Synth

### B-0227
- **One-sentence idea:** Class-wise utility prediction for text-to-image synthetic segmentation data: predict, per class, whether generation+cross-attention masks will help before training on them.
- **Problem:** Text-to-image models with attention-derived masks promise free training data for arbitrary classes, but per-class quality varies wildly (great for "dog," garbage for "catheter"), and teams discover which classes worked only after expensive training runs.
- **Core Hypothesis:** Per-class synthetic utility is predictable from pre-training-computable signals (attention-mask coherence, generation diversity, text-embedding familiarity of the class term), enabling a go/no-go decision per class that recovers most of the oracle selection's benefit.
- **Why Important:** Converts a hit-or-miss free-data source into a managed one; especially valuable for long-tail class extension.
- **Why Possibly Novel:** Text-to-image training data works exist; the per-class utility-prediction layer with validated go/no-go decisions is missing.
- **Minimal Experiment:** Generate data for 40 classes; train per-class additions; correlate observed gains with the candidate predictors. Falsified if per-class utility is unpredictable.
- **Main Risk:** Predictors may be model-version-specific, needing recalibration per generator release.
- **Cluster:** Synth

### B-0228
- **One-sentence idea:** Physics-based ultrasound simulation from CT/MRI-derived anatomy (with segmentation labels carried through) as a training source for ultrasound segmentation where real labeled data is scarce.
- **Problem:** Ultrasound segmentation lacks labeled data because annotation is hard and archives are unstructured; meanwhile labeled CT/MRI define 3D anatomy from which ultrasound physics (acoustic impedance, speckle, shadowing) can be simulated — a cross-modality label-transfer route that bypasses annotation entirely but whose viability is unquantified.
- **Core Hypothesis:** Simulated ultrasound from CT-derived tissue maps, plus light appearance adaptation on unlabeled real ultrasound, trains segmenters to a usable fraction of real-data performance, with the residual gap concentrated in probe-interaction effects the simulator misses (measurable via effect-specific test stratification).
- **Why Important:** Would unlock supervised ultrasound learning at CT/MRI annotation prices — a large economic arbitrage.
- **Why Possibly Novel:** Ultrasound simulators exist for training clinicians; their systematic use as dense-supervision factories with gap decomposition is underexplored.
- **Minimal Experiment:** Simulate cardiac or abdominal US from labeled CT; train; evaluate on real labeled US vs. small-real-data baselines. Falsified if the simulated-to-real gap is unusably large even with adaptation.
- **Main Risk:** Speckle and probe artifacts are notoriously hard to simulate faithfully (connects to B-0193's physics).
- **Cluster:** Synth

### B-0229
- **One-sentence idea:** Generate interpolated domains between training sources (synthetic domain bridging) and test whether filling the inter-domain gaps improves unseen-domain generalization more than adding same-domain volume.
- **Problem:** Domain generalization trains on a few discrete source domains; the space between and around them is empty, and models may fail on unseen domains simply because no training signal covers the connecting regions — yet generation could fill those gaps deliberately, a use distinct from generic augmentation.
- **Core Hypothesis:** Training with generated bridge domains (style/physics interpolations between sources) improves unseen-target performance more than equal volumes of additional source-domain data, with the gain largest for targets geometrically between sources and persisting (smaller) for extrapolated targets.
- **Why Important:** Reframes generation's role in robustness from "more data" to "topological completion of domain coverage" — a testable, more efficient use.
- **Why Possibly Novel:** Style mixing exists as augmentation; the explicit interpolation-vs-volume controlled comparison with target-position analysis is unrun.
- **Minimal Experiment:** Multi-site medical or multi-weather driving data: train {sources, sources+volume, sources+bridges}; evaluate on held-out domains positioned between and beyond sources. Falsified if bridges match plain volume.
- **Main Risk:** Interpolated domains may be off-manifold (unrealistic mixtures) and teach nothing relevant.
- **Cluster:** Synth

### B-0230
- **One-sentence idea:** Decompose synthetic data's advantage into label cleanliness versus image distribution: how much of the benefit is just that synthetic labels are perfect?
- **Problem:** Synthetic data differs from real data in two entangled ways — image realism (worse) and label quality (perfect) — and all comparisons confound them; if much of synthetic data's value is label cleanliness, the field should invest in label cleaning rather than generation, but the decomposition has never been run.
- **Core Hypothesis:** Injecting realistic label noise (matched to measured human annotation-error statistics) into synthetic labels erases a large fraction of the synthetic-real performance difference in low-data regimes — demonstrating that label perfection, not image content, drives much of the observed benefit.
- **Why Important:** Redirects investment between generation and annotation QC based on measurement rather than assumption.
- **Why Possibly Novel:** The clean-label confound is unremarked in synthetic-data comparisons; the noise-injection decomposition is simple and undone.
- **Minimal Experiment:** Train on {real, synth, synth+human-matched label noise, real+cleaned labels} at several data sizes. Falsified if noise injection doesn't move synthetic utility.
- **Main Risk:** Modeling "human-matched" label noise realistically requires multi-annotator data for calibration.
- **Cluster:** Synth

### B-0231
- **One-sentence idea:** Tail-targeted conditional generation for long-tail segmentation, with per-class gain accounting and identification of the class properties that make generation fail.
- **Problem:** Generators are trained on the same long-tailed data as segmenters, so naive generation reproduces the head; conditioning can force tail-class output, but tail conditioning quality is exactly where generators are weakest — whether tail synthesis helps, and for which classes, is empirically unresolved.
- **Core Hypothesis:** Tail-class generation yields real per-class gains for structure-defined classes (recognizable geometry) but fails for texture/context-defined tail classes (generator lacks the concept), with the divide predictable from generation-consistency metrics — so tail synthesis should be deployed selectively, not universally.
- **Why Important:** Long-tail is the standing excuse for deployment failures; knowing where generation genuinely helps prevents wasted effort and false confidence.
- **Why Possibly Novel:** Tail-class generation is attempted broadly; the class-property-stratified success analysis with a selective-deployment rule is missing.
- **Minimal Experiment:** Generate for 20 tail classes on a long-tailed benchmark; train with tail-augmentation; regress per-class gains on class-property features. Falsified if gains are property-independent.
- **Main Risk:** Per-class gains at the tail are statistically noisy (see B-0277's power concern) — needs repeated runs.
- **Cluster:** Synth

### B-0232
- **One-sentence idea:** Pretrain a dense-prediction foundation model on 100% synthetic/procedural imagery (zero real data) and measure the real-data gap — a privacy-free, license-free FM baseline.
- **Problem:** FM pretraining is entangled with data-governance liabilities (privacy, copyright, consent); fully synthetic pretraining would eliminate them, and small-scale evidence hints learned features transfer from procedural imagery, but the dense-task gap at meaningful scale is unmeasured.
- **Core Hypothesis:** A procedurally pretrained FM (fractal/graphics/procedural anatomy mixtures) reaches within a modest, quantifiable gap of real-data pretraining on segmentation transfer, the gap shrinks with procedural diversity (not volume), and the residue concentrates in high-level semantics rather than boundary features — mapping exactly what real data is still needed for.
- **Why Important:** A viable synthetic FM changes the legal and economic structure of foundation-model building.
- **Why Possibly Novel:** Formula/fractal pretraining exists for classification at modest scales; the dense-transfer measurement with the diversity-vs-volume and semantics-vs-boundary decompositions is open.
- **Minimal Experiment:** Pretrain matched small FMs (procedural vs. real corpus); probe dense transfer on 4 tasks; run the diversity ablation. Falsified if the gap is catastrophic and diversity-insensitive.
- **Main Risk:** Small-scale conclusions may not extrapolate to FM scale (same risk as B-0032; report as scaling trend).
- **Cluster:** Synth

### B-0233
- **One-sentence idea:** Simulate arbitrary MRI contrasts from quantitative tissue maps (qMRI) to train sequence-invariant segmentation, with physics-exact augmentation replacing style-transfer approximations.
- **Problem:** MRI appearance depends on acquisition sequence through known physics (signal equations over T1/T2/PD maps); models fail across sequences, and the field patches this with learned style transfer when exact forward simulation from quantitative maps is available and ignored.
- **Core Hypothesis:** Training with physics-simulated contrast sweeps (all achievable sequence parameters from a modest qMRI corpus) produces sequence-invariant segmenters that generalize to held-out real sequences better than style-augmented baselines — and the failure cases isolate the non-Bloch effects (artifacts, B1 inhomogeneity) that simulation misses.
- **Why Important:** Sequence diversity is the single largest MRI deployment variable; an exact-physics answer is more durable than learned approximations.
- **Why Possibly Novel:** Contrast simulation exists in physics literature and SynthSeg uses random contrasts; systematic physics-exact sequence-sweep training with held-out-sequence evaluation against style baselines is not established.
- **Minimal Experiment:** Use public qMRI data; simulate 20 sequences; train; test on real scans of sequences excluded from simulation. Falsified if style augmentation matches physics simulation.
- **Main Risk:** qMRI corpora are small and their own acquisition biases propagate into everything.
- **Cluster:** Synth

### B-0234
- **One-sentence idea:** Depth-consistent weather compositing for driving data: insert fog/rain with transmission computed from scene depth, and test whether physical consistency (vs. flat alpha overlays) matters for segmentation robustness transfer.
- **Problem:** Synthetic weather augmentation mostly overlays depth-ignorant haze; real fog attenuates with distance, so depth-inconsistent training fog teaches physically wrong cues (near objects hazed, far objects clear), potentially harming rather than helping real-fog performance — an unverified suspicion.
- **Core Hypothesis:** Depth-consistent fog compositing transfers to real foggy-scene segmentation markedly better than depth-ignorant compositing at matched visual severity, and depth-ignorant training measurably mis-calibrates the model's distance-visibility relationship (testable via depth-stratified error analysis).
- **Why Important:** Weather robustness training is standard practice in autonomy; if the standard recipe is physically wrong, everyone inherits the flaw.
- **Why Possibly Novel:** Depth-aware fog synthesis exists in a few datasets; the controlled consistency-vs-ignorance comparison with the miscalibration analysis is unrun.
- **Minimal Experiment:** Composite both fog types on one driving dataset (depth available); train matched models; evaluate on real fog benchmarks with depth-stratified errors. Falsified if flat overlays transfer equally.
- **Main Risk:** Real-fog test sets are small; depth estimates in training data carry their own errors.
- **Cluster:** Synth

### B-0235
- **One-sentence idea:** Build generator blind-spot maps — a systematic catalog of visual phenomena a given generator cannot produce — and use them to predict where synthetic-trained models will fail and what real data to collect.
- **Problem:** Every generator has systematic incapabilities (specular highlights, thin structures per B-0222, rare textures); models trained on its output inherit matching blind spots, but the incapability→downstream-failure link is never mapped, so failures surprise everyone and real-data collection is untargeted.
- **Core Hypothesis:** Generator incapabilities are enumerable via probing (conditioning on phenomena and measuring production fidelity), downstream failure geography of synthetic-trained models aligns with the blind-spot map far above chance, and blind-spot-targeted real-data collection repairs failures several times more efficiently than random collection.
- **Why Important:** Converts synthetic-data risk from unknown-unknowns to a managed checklist, and optimizes the real-data budget that remains.
- **Why Possibly Novel:** Generator evaluation measures average quality; capability cartography linked predictively to downstream failure and collection policy is a new construction.
- **Minimal Experiment:** Probe one generator across a phenomenon battery; train downstream on its data; test failure-map alignment; run targeted vs. random collection repair. Falsified if failures don't align with blind spots.
- **Main Risk:** Phenomenon battery completeness; blind spots may interact (compositional incapabilities).
- **Cluster:** Synth

### B-0236
- **One-sentence idea:** Measure synthetic-data scaling laws for dense prediction: the exponent and saturation point of performance versus synthetic volume, compared against real-data scaling on the same tasks.
- **Problem:** Synthetic data is treated as if more is monotonically better; theory and scattered evidence suggest earlier saturation (limited generator entropy) and possibly degradation (distribution takeover), but the scaling curves have never been fit and compared for segmentation — so generation budgets are set blind.
- **Core Hypothesis:** Synthetic scaling shows a systematically smaller exponent and earlier saturation than real-data scaling, the saturation point is predictable from generator diversity metrics, and beyond saturation additional synthetic volume actively hurts mixed training (measurable takeover effect) — giving generation budgets a principled stopping rule.
- **Why Important:** Prevents both under-generation and the costlier failure of drowning real data in saturated synthetic volume.
- **Why Possibly Novel:** Data scaling laws exist for real corpora; the synthetic-specific exponents, saturation prediction, and takeover characterization are unmeasured.
- **Minimal Experiment:** For 2 tasks × 2 generators, sweep synthetic volume across 3 orders of magnitude at fixed real volume; fit curves. Falsified if synthetic scaling matches real scaling.
- **Main Risk:** Compute cost of the sweep; exponents may vary with the real/synthetic ratio (add one ratio sweep).
- **Cluster:** Synth

### B-0237
- **One-sentence idea:** Condition generation on distance transforms instead of binary masks, hypothesizing sharper mask-image boundary agreement in synthetic segmentation data.
- **Problem:** Binary-mask conditioning gives the generator no gradient of "how close to the boundary am I," producing exactly the boundary-zone misalignment measured in B-0211; the conditioning representation itself — never the target of study — may be the cause.
- **Core Hypothesis:** Distance-transform (or soft-boundary) conditioning reduces boundary misalignment between generated images and labels substantially at identical generator capacity, and models trained on the resulting data show boundary-metric gains that binary-conditioned data cannot match at any volume.
- **Why Important:** A representation-level fix at the source of the pipeline is cheaper than all downstream filtering; boundary fidelity is dense prediction's scarcest resource.
- **Why Possibly Novel:** Conditioning representations are chosen by convention; the misalignment-attribution to binary conditioning and the distance-transform remedy are untested.
- **Minimal Experiment:** Train matched conditional generators (binary vs. distance conditioning); measure alignment (per B-0211's audit) and downstream boundary metrics. Falsified if conditioning representation doesn't move alignment.
- **Main Risk:** Distance conditioning may trade boundary fidelity for interior realism.
- **Cluster:** Synth

### B-0238
- **One-sentence idea:** Decompose the sim-to-real gap into appearance versus content (layout/geometry) components via style-bridging experiments, to allocate generation-improvement effort where the gap actually lives.
- **Problem:** "Sim-to-real gap" is treated as one number; simulators may fail on appearance (textures, sensor noise) or on content (object layouts, co-occurrence statistics), which demand entirely different fixes (better rendering vs. better scene generation) — and the decomposition is never measured before investing.
- **Core Hypothesis:** Style-transferring synthetic images to real appearance (holding layout fixed) closes a measurable fraction of the gap — that fraction is the appearance component — and across popular simulators the content component dominates for segmentation (layouts are the harder deficiency), contradicting the field's rendering-centric investment.
- **Why Important:** Simulator development budgets are large and currently allocated by intuition; the decomposition is a direct investment guide.
- **Why Possibly Novel:** Style bridging is used as a method; as a measurement instrument for gap decomposition across simulators, it is unexploited.
- **Minimal Experiment:** For 2 simulators × 1 real target each: baseline gap, style-bridged gap, and (reverse) real-stylized-as-sim controls; decompose. Falsified if appearance explains nearly everything.
- **Main Risk:** Style transfer imperfections blur the decomposition (bound them with the reverse control).
- **Cluster:** Synth

### B-0239
- **One-sentence idea:** Closed-loop self-improving synthesis: segmentation-model errors steer the next generation round, with an explicit study of convergence versus mode-collapse dynamics of the loop.
- **Problem:** Static synthetic sets fix their coverage at generation time; looping model errors back into generation (make more of what the model fails on) is the obvious upgrade, but such loops can also collapse (generating ever-narrower hard cases, overfitting the model to generator quirks) — the dynamics are unstudied for dense prediction.
- **Core Hypothesis:** Error-steered loops outperform static generation at matched total volume for the first few iterations, then exhibit measurable degeneration (diversity collapse in generated batches, real-set performance plateau or decline), and a diversity-floor constraint on each round stabilizes the loop into sustained gains.
- **Why Important:** Establishes whether the appealing "self-improving data engine" narrative actually works for segmentation, and how to engineer it safely.
- **Why Possibly Novel:** Active generation appears in fragments; the loop-dynamics characterization (convergence, collapse, stabilization) is the missing science.
- **Minimal Experiment:** Run 6-round loops ± diversity floor on one task; track real-set performance and generated-batch diversity per round. Falsified if loops neither help nor collapse (dynamics-free).
- **Main Risk:** Compute-intensive; conclusions may depend on error-to-conditioning translation quality.
- **Cluster:** Synth

### B-0240
- **One-sentence idea:** Validate generation-based stress testing: are controlled synthetic perturbation suites (same scene ± rain, occlusion sweeps) faithful proxies for real-perturbation robustness?
- **Problem:** Generated counterfactual test suites are increasingly used to certify robustness ("model survives synthetic rain sweep"), but if generated perturbations miss real perturbations' hard components, such certificates are false comfort — the meta-validity question is unasked while the practice spreads into safety cases.
- **Core Hypothesis:** Rank correlation between synthetic-perturbation robustness and matched real-perturbation robustness across a model pool is high for geometric perturbations (occlusion, scale) but substantially lower for atmospheric/photometric ones (rain, fog, low light), where generators smooth away the hardest physical effects — defining which synthetic certificates are admissible.
- **Why Important:** Robustness certification methodology is becoming regulatory currency; its validity boundaries must be measured before it hardens into standards.
- **Why Possibly Novel:** Synthetic corruptions (corruption benchmarks) are compared to real shifts occasionally for classification; the dense-prediction, perturbation-type-stratified validity study is missing.
- **Minimal Experiment:** For 15 models: robustness under synthetic perturbation sweeps vs. matched real-condition test sets (existing rain/fog/occlusion data); correlate by perturbation type. Falsified if correlations are uniformly high.
- **Main Risk:** "Matched" real conditions are hard to align in severity with synthetic sweeps (use ordinal matching).
- **Cluster:** Synth
## Section 9 — Annotation Efficiency [B-0241–B-0270]

### B-0241
- **One-sentence idea:** A sealed, cost-honest benchmark for active learning in segmentation — realistic batch sizes, cold starts, and time-based (not image-count) budgets — testing whether published AL gains survive.
- **Problem:** AL papers compare against random sampling under idealized protocols (warm starts, oracle-tuned budgets, per-image cost units); practitioners repeatedly find random sampling hard to beat, suggesting the literature's gains partly reflect protocol artifacts — but no rigorous audit exists for dense prediction.
- **Core Hypothesis:** Under realistic conditions (cold start, batch acquisition, time-costed annotation, no test-set peeking for hyperparameters), a substantial fraction of published segmentation-AL gains shrink to insignificance, and the survivors share identifiable traits (diversity components, region-level granularity) — yielding an evidence-based practitioner shortlist.
- **Why Important:** AL adoption decisions are being made on potentially inflated evidence; the audit either restores confidence or redirects the field.
- **Why Possibly Novel:** AL skepticism exists as scattered negative results; a systematic sealed re-evaluation with survivor analysis for segmentation is unperformed.
- **Minimal Experiment:** Re-run 8 published AL methods under the sealed protocol on 3 datasets with timed-cost models. Pure re-evaluation. Falsified if gains broadly survive.
- **Main Risk:** Cost-model choices are contestable (publish sensitivity analyses across cost models).
- **Cluster:** AnnotEff

### B-0242
- **One-sentence idea:** Region-level active learning with a context-acquisition cost model: selecting small scattered regions is not cheap once the annotator must re-orient in each new image.
- **Problem:** Region-level AL assumes cost proportional to region area, but human annotators pay a fixed context cost per image visited (loading, orienting, understanding anatomy); ignoring it makes scattered-region selection look artificially efficient, and real deployments discover the overhead too late.
- **Core Hypothesis:** Under a validated two-part cost model (per-image context cost + per-area tracing cost), optimal selection shifts from scattered maximal-information regions toward spatially clustered acquisitions, and cost-model-aware selection beats area-costed selection by a meaningful margin in real annotator-time experiments.
- **Why Important:** Aligns AL's objective with what budgets actually pay for — human minutes, not pixels.
- **Why Possibly Novel:** Cost-sensitive AL exists abstractly; the context-cost structure for dense annotation, empirically calibrated with timed studies, is unmodeled.
- **Minimal Experiment:** Timed annotation study to fit the cost model; simulate AL under area-only vs. two-part costs; validate the top policies with a second timed study. Falsified if context costs are negligible.
- **Main Risk:** Cost parameters vary across tools and annotator experience levels.
- **Cluster:** AnnotEff

### B-0243
- **One-sentence idea:** Solve the active-learning cold-start problem for segmentation with self-supervised-feature coverage sampling — principled selection before any task model exists.
- **Problem:** AL methods need a trained model to score informativeness, but the first (often largest) annotation batch is chosen with no model at all; random selection at round zero can dominate the entire campaign's outcome, and the cold-start decision is unstudied for dense tasks.
- **Core Hypothesis:** Coverage-maximizing selection in self-supervised feature space (facility-location over frozen SSL embeddings, with slice/patient de-duplication) beats random first batches consistently, with the advantage largest in heterogeneous datasets and persisting through subsequent AL rounds (good foundations compound).
- **Why Important:** The first batch is the highest-leverage, least-informed decision in every annotation campaign.
- **Why Possibly Novel:** Cold-start selection has minor classification literature; dense-prediction cold-start with volumetric redundancy handling (adjacent slices are near-duplicates) is a distinct unsolved instance.
- **Minimal Experiment:** Compare first-batch strategies (random, coverage, diversity variants) at 3 budget sizes on 3 datasets; track downstream rounds. Falsified if random is unbeatable at round zero.
- **Main Risk:** SSL feature quality on the target domain gates everything (test with 2 feature sources).
- **Cluster:** AnnotEff

### B-0244
- **One-sentence idea:** Measure automation-bias contamination in model-assisted annotation — annotators anchoring on pre-segmentations — and design blind-review protocols that keep the speed without inheriting the model's errors.
- **Problem:** Model-assisted annotation (pre-segmentation + human correction) is now standard for speed, but annotators demonstrably under-correct plausible-looking model errors; datasets built this way inherit the assisting model's systematic biases, which then get "validated" when similar models are evaluated on them — a circularity nobody quantifies.
- **Core Hypothesis:** Anchored annotation reproduces a measurable fraction of assisting-model errors (versus from-scratch annotation of the same cases), the effect grows with model plausibility, and interleaving blind cases (no pre-segmentation, unannounced) both measures per-annotator anchoring live and reduces it via awareness — an implementable QA protocol.
- **Why Important:** If assisted datasets are model-biased, the field's data flywheel is quietly converging on its own errors; measurement and protocol are urgent.
- **Why Possibly Novel:** Automation bias is documented in radiology decision support; its dataset-contamination consequence for segmentation ground truth is unmeasured.
- **Minimal Experiment:** Cross-over study: annotators label overlapping case sets with/without pre-segmentation from a model with known planted errors; measure error inheritance rates. Falsified if annotators reliably catch the planted errors.
- **Main Risk:** Study effects (annotators behaving better when observed); needs naturalistic logging validation.
- **Cluster:** AnnotEff

### B-0245
- **One-sentence idea:** Learn per-case annotation-time predictors and switch active learning from accuracy-per-image to accuracy-per-minute optimization.
- **Problem:** AL selects the most informative samples, which are systematically the hardest and slowest to annotate; informativeness and annotation cost are positively correlated, so per-image-optimal selection can be per-minute-suboptimal — but time is what budgets buy, and per-case time is never predicted or used.
- **Core Hypothesis:** Annotation time is predictable per case from image features (boundary complexity, instance count, ambiguity proxies) with useful accuracy, and time-normalized acquisition (information ÷ predicted minutes) yields more final accuracy per annotation-hour than count-based acquisition — with the gap widening as case difficulty varies more.
- **Why Important:** Makes label-efficiency research optimize the actual scarce resource; immediately deployable in labeling platforms.
- **Why Possibly Novel:** Cost-aware AL is theorized; learned time predictors calibrated on real logged annotation sessions for dense tasks are essentially absent.
- **Minimal Experiment:** Fit time predictors on logged annotation sessions (or a timed study); run simulated AL under time budgets with both acquisition rules; validate the top rule in a small live campaign. Falsified if time is unpredictable or the correction doesn't matter.
- **Main Risk:** Time predictors may not transfer across annotators/tools without recalibration.
- **Cluster:** AnnotEff

### B-0246
- **One-sentence idea:** Contestability prediction for annotation QA: train a model to predict which annotations a second expert would dispute, and route only those to re-review.
- **Problem:** Double-reading everything for quality assurance doubles cost, so most datasets QA a random sample — wasting reviews on uncontroversial cases while systematic errors in ambiguous regions sail through; the review budget is spent without targeting.
- **Core Hypothesis:** Inter-rater contestability is predictable per annotation (from image ambiguity features and annotation geometry) well enough that reviewing the top-scored 20% catches the majority of would-be disputes — matching near-full double-reading quality at a fraction of cost, verifiable on existing multi-rater corpora.
- **Why Important:** QA targeting is a direct multiplier on every annotation budget in every domain.
- **Why Possibly Novel:** Disagreement modeling exists descriptively (B-0070, B-0003); its operationalization as a QA routing system with catch-rate accounting is unbuilt.
- **Minimal Experiment:** Train contestability predictor on multi-rater data (label = raters disagreed here); evaluate dispute catch-rate vs. review fraction on held-out raters. Falsified if disputes are unpredictable.
- **Main Risk:** Predictor may capture only generic ambiguity, missing annotator-specific lapses (complement with B-0268).
- **Cluster:** AnnotEff

### B-0247
- **One-sentence idea:** Show that consensus label fusion (STAPLE-style) fails when raters share training lineage (correlated biases), and build lineage-aware fusion that models rater covariance.
- **Problem:** Label-fusion algorithms assume conditionally independent raters, but real annotation teams are trained by the same instructor with the same guideline examples — their errors correlate, consensus confidently converges on shared bias, and the "ground truth" inherits it invisibly.
- **Core Hypothesis:** On teams with documented shared training, fused labels deviate systematically from external-expert reference in the direction of the shared curriculum's exemplars, and fusion that estimates a rater covariance structure (from agreement patterns) recovers a less biased consensus — measurable wherever an independent reference rater exists.
- **Why Important:** Consensus ground truth anchors every evaluation; correlated-bias contamination undermines the field's reference standard itself.
- **Why Possibly Novel:** Correlated annotators are acknowledged in crowdsourcing theory; the segmentation-fusion instance with lineage as the measured correlate is unexamined.
- **Minimal Experiment:** Recruit two annotator cohorts trained via different curricula on the same cases plus one external expert; compare within/between-cohort agreement and fusion outcomes. Falsified if lineage doesn't structure errors.
- **Main Risk:** Recruiting lineage-controlled cohorts takes organization; effect may be structure-dependent.
- **Cluster:** AnnotEff

### B-0248
- **One-sentence idea:** Learned slice-selection policies for 3D annotation: choose which slices a human should label (per volume, adaptively) to maximize full-volume label quality after completion.
- **Problem:** Sparse-slice annotation (B-0192) defaults to uniform slice spacing, but information is nonuniform — anatomy changes fast in some regions and slowly in others — and the selection decision, made thousands of times per campaign, has no learned policy behind it.
- **Core Hypothesis:** A policy that selects slices adaptively (conditioned on the volume and previously labeled slices, trained to minimize completion error) beats uniform and heuristic (curvature-based) selection by a margin that compounds over annotation rounds, and the policy transfers across organs with similar geometric statistics.
- **Why Important:** Same annotation budget, better labels, at pure software cost — multiplied across all 3D annotation worldwide.
- **Why Possibly Novel:** Slice selection is handled by rules of thumb; a learned sequential-selection policy with completion-error training signal appears unbuilt.
- **Minimal Experiment:** Simulate on densely labeled volumes: uniform vs. curvature vs. learned selection at budgets of 3–7 slices; measure completed-label fidelity. Falsified if uniform is near-optimal (possible for smooth organs).
- **Main Risk:** Policy training needs diverse dense-labeled volumes; gains may be organ-specific.
- **Cluster:** AnnotEff

### B-0249
- **One-sentence idea:** Optimal coarse-to-fine annotation staging: label everything cheaply first, then spend refinement passes only where a model trained on coarse labels remains uncertain.
- **Problem:** Campaigns choose one annotation precision upfront; precision beyond what training needs is wasted everywhere, precision below it is wasted entirely — yet the staged alternative (coarse pass → train → targeted fine pass) has no validated policy for what "coarse" should be or where refinement pays.
- **Core Hypothesis:** Two-stage campaigns dominate single-stage at equal total time across realistic budgets, the optimal first-stage coarseness is predictable from task boundary-sensitivity, and refinement targeting by coarse-model uncertainty beats random refinement substantially — a complete, validated staging recipe.
- **Why Important:** Campaign architecture (not selection tweaks) is the biggest untouched lever in annotation economics.
- **Why Possibly Novel:** Coarse-to-fine exists informally in industry practice; its formalization with policy optimization and controlled total-time evaluation is missing from the literature.
- **Minimal Experiment:** Simulate staging from dense labels with timed cost constants (coarse = boxes/low-vertex polygons); validate the winning policy in a small live timed campaign. Falsified if single-stage matches staged at equal time.
- **Main Risk:** Simulation-to-live gap in cost constants; stage-switching overhead.
- **Cluster:** AnnotEff

### B-0250
- **One-sentence idea:** Establish when low-resolution annotation is safe: annotate at 4×-downsampled display, restore boundary precision with learned label super-resolution, and map the fidelity boundary by structure type.
- **Problem:** Annotating on downsampled images is dramatically faster (less panning, fewer vertices), but nobody knows how much boundary truth is lost, whether learned upsampling (conditioned on the full-res image) recovers it, and for which structures the shortcut is disqualifying — so the practice is either banned or used blindly.
- **Core Hypothesis:** Image-conditioned label super-resolution recovers most boundary fidelity for structures whose full-res boundaries follow image gradients (organs, vehicles), while convention-defined boundaries (tumor margins including edema) lose irrecoverable information — a structure-type rule that annotation planners can apply directly.
- **Why Important:** A potential 2–3× throughput gain on the most expensive annotation category, with validated safety limits.
- **Why Possibly Novel:** Label super-resolution exists as a technique; the annotation-protocol question (when is coarse display safe, with human-in-the-loop timing) is unstudied.
- **Minimal Experiment:** Annotators label the same cases at full and 4× reduced resolution (timed); super-resolve the coarse labels; compare fidelity and time by structure type. Falsified if recovery fails even for gradient-following boundaries.
- **Main Risk:** Annotator behavior at low resolution may change qualitatively (skipping small objects entirely).
- **Cluster:** AnnotEff

### B-0251
- **One-sentence idea:** Unlock legacy datasets via learned ontology mapping: train converters between label protocols (different class definitions and granularities) so old annotations supervise new tasks with quantified fidelity.
- **Problem:** Decades of annotated datasets are stranded by incompatible label protocols (classes split/merged/defined differently); naive class-name matching silently corrupts training, so the archives — collectively larger than any new campaign — go unused.
- **Core Hypothesis:** Protocol conversion is learnable from small overlap sets (cases labeled under both protocols) as a conditional relabeling model, converted legacy data provides supervision worth a large, quantifiable fraction of native annotation, and conversion confidence maps identify the class regions where protocols are genuinely incommensurable.
- **Why Important:** The cheapest large annotation source is the annotation that already exists; conversion tooling multiplies the world's labeled-data stock.
- **Why Possibly Novel:** Label-space heterogeneity is handled by heads (B-0012) or dropped; explicit learned conversion with fidelity accounting and incommensurability detection is a distinct, unbuilt tool.
- **Minimal Experiment:** Take two datasets with protocol conflicts and a creatable overlap set (~50 dual-labeled cases); train converter; measure converted-data supervision value vs. native labels. Falsified if conversion value is negligible.
- **Main Risk:** Some protocol differences depend on information absent from images (clinical context), capping conversion.
- **Cluster:** AnnotEff

### B-0252
- **One-sentence idea:** Validate learning-curve extrapolation as a budgeting instrument for dense tasks: from a small pilot annotation, predict the accuracy-versus-N curve before committing the campaign budget.
- **Problem:** Annotation budgets are committed before anyone knows the task's data hunger; learning-curve extrapolation from pilots is the obvious instrument, but its reliability for segmentation (where per-class curves differ and pilot noise is high) is unvalidated — so budgets are set by analogy and negotiation.
- **Core Hypothesis:** Power-law extrapolation from a 10% pilot predicts full-campaign accuracy within useful tolerance for region metrics but systematically over-predicts boundary-metric and rare-class saturation, and a corrected extrapolator (fitting per-class curves with hierarchical shrinkage) restores calibrated prediction intervals usable for budget decisions.
- **Why Important:** A validated budgeting instrument would rationalize annotation spending across the entire field.
- **Why Possibly Novel:** Learning-curve literature exists for classification; the dense-task validation with per-class hierarchical correction and decision-calibrated intervals is missing.
- **Minimal Experiment:** On 5 fully annotated datasets, simulate pilots, extrapolate, compare against realized curves; quantify interval calibration. No new annotation. Falsified if extrapolation is hopeless at pilot sizes.
- **Main Risk:** Extrapolation may fail exactly for the novel tasks where budgeting matters most (report domain-transfer validity).
- **Cluster:** AnnotEff

### B-0253
- **One-sentence idea:** Quantify the deployment bias created by "interesting-case" annotation (skipping easy/normal cases) and correct it with importance weighting plus a mandatory random floor.
- **Problem:** Annotation naturally concentrates on hard, abnormal, or interesting cases (they seem more valuable, and normals feel wasteful); the resulting dataset misrepresents deployment case-mix, models miscalibrate on normals (false positives on healthy anatomy), and the induced bias is neither measured nor corrected in standard practice.
- **Core Hypothesis:** Enrichment-biased training measurably inflates false-positive rates on unenriched test streams in proportion to the enrichment factor, and a two-part fix (importance reweighting from a logged selection model + a small random-sample floor) restores calibration at a few percent of budget — turning selection bias into a managed quantity.
- **Why Important:** Nearly all clinical datasets are enriched; the induced miscalibration lands directly on deployed screening performance.
- **Why Possibly Novel:** Sampling bias is classical statistics; its specific quantification and budgeted correction protocol for dense-prediction datasets is not established practice.
- **Minimal Experiment:** From a population-representative dataset, construct enriched training subsets at known factors; measure FP inflation and the correction's recovery. Fully controlled. Falsified if enrichment is harmless.
- **Main Risk:** Real selection processes are less documented than simulated ones (the selection model must be estimated).
- **Cluster:** AnnotEff

### B-0254
- **One-sentence idea:** Sequential stopping rules for annotation campaigns: monitor marginal model improvement per label batch and stop when the campaign's remaining value drops below its cost, with statistical guarantees.
- **Problem:** Campaigns run to budget exhaustion, not to sufficiency; nobody applies sequential-analysis machinery to decide "we have enough labels," so money is spent past saturation on some tasks while others stop short — both errors invisible without a monitored stopping framework.
- **Core Hypothesis:** A sequential monitor (periodic held-out evaluation with drift-corrected improvement estimation) can call saturation within a small error of the oracle stopping point across tasks, saving a meaningful fraction of budget on saturating tasks — and the monitor's variance requirements set a principled evaluation-set size for campaigns.
- **Why Important:** Applies to every annotation campaign ever run; savings compound field-wide.
- **Why Possibly Novel:** Optimal stopping is mature theory; its practical instantiation and validation for dense-annotation campaigns (with the eval-set sizing corollary) is absent.
- **Minimal Experiment:** Replay 5 completed datasets as simulated campaigns; run the monitor; compare stop points and realized losses vs. oracle. Falsified if saturation is undetectable at feasible eval-set sizes.
- **Main Risk:** Non-stationary campaigns (annotator mix changes over time) violate monitor assumptions.
- **Cluster:** AnnotEff

### B-0255
- **One-sentence idea:** Measure the gap between simulated and real users in interactive-segmentation evaluation, then build empirically calibrated user models — because current click simulators may be crowning the wrong methods.
- **Problem:** Interactive segmentation methods are ranked by simulated users (center-of-largest-error clicking), but real users click differently (perceptual salience, motor noise, impatience, strategy switching); if rankings flip under real behavior, the field is optimizing an artifact — and no one has run the comparison.
- **Core Hypothesis:** Method rankings under logged real-user interaction differ meaningfully from simulator rankings (especially between methods tuned to simulator idioms), and a behavioral user model fitted to interaction logs (click placement distributions, correction strategies) reproduces real rankings, giving the field a valid cheap evaluator.
- **Why Important:** Interactive tools are the near-term deployment path for segmentation; their evaluation must reflect actual humans.
- **Why Possibly Novel:** Click simulators are universal; their behavioral validity has never been established or refuted with a controlled human study.
- **Minimal Experiment:** User study (12 annotators × 4 methods × shared cases) with full logging; compare real vs. simulated rankings; fit and validate the behavioral model. Falsified if simulator rankings hold.
- **Main Risk:** User-study variance requires careful within-subject design; tool-UX confounds method comparison.
- **Cluster:** AnnotEff

### B-0256
- **One-sentence idea:** Optimize the propagate-verify economics of video annotation: find the keyframe density and verification policy that minimize total human time for target label quality.
- **Problem:** Video annotation pipelines (label keyframes, track between, verify/fix) involve coupled choices — keyframe spacing, tracker choice, verification thoroughness — currently set by intuition; the joint optimization for actual human minutes has not been formulated or measured, though video is the fastest-growing annotation category.
- **Core Hypothesis:** Total-time-optimal policies use sparser keyframes plus targeted verification (gated by tracker-confidence signals, cf. B-0194) rather than dense keyframes, cutting human time substantially at matched quality — with the optimal policy predictable from clip motion statistics.
- **Why Important:** Video annotation cost is the bottleneck for temporal-model development everywhere (surgery, driving, surveillance).
- **Why Possibly Novel:** Components all exist; the joint policy optimization validated in timed human experiments is missing.
- **Minimal Experiment:** Grid over keyframe density × verification policy in a timed annotation study on 2 video domains; fit the policy predictor on motion statistics. Falsified if dense keyframing is unavoidable.
- **Main Risk:** Results depend on tracker generation; must report against 2 trackers.
- **Cluster:** AnnotEff

### B-0257
- **One-sentence idea:** Speech-first annotation: the annotator describes the target verbally ("the darker nodule under the pleura, not the vessel"), a grounding model proposes the mask, and the human verifies — replacing tracing with talking.
- **Problem:** Tracing is slow and ergonomically costly; speech is 5–10× faster than drawing and can express negations and disambiguations, but no annotation pipeline treats language grounding plus verification as the primary mask-creation mechanism, and its accuracy-throughput profile is unmeasured.
- **Core Hypothesis:** For distinctive structures, speech+grounding+verify produces accepted masks several times faster than tracing at matched quality, with failures concentrated where language cannot discriminate (multiple similar instances) — predictable in advance, enabling hybrid routing (speak when distinctive, trace when not).
- **Why Important:** Could change the dominant annotation interface, with accessibility benefits (annotators with motor limitations) as a side effect.
- **Why Possibly Novel:** Referring segmentation exists as a task; its inversion into an annotation-production tool with timed throughput studies and routing rules is unexplored.
- **Minimal Experiment:** Timed within-subject study: speech-first vs. tracing on cases stratified by distinctiveness; measure accepted-mask quality and time. Falsified if verification overhead eats the speech advantage.
- **Main Risk:** Grounding-model errors on specialist vocabulary (mitigable via B-0167's pseudo-words).
- **Cluster:** AnnotEff

### B-0258
- **One-sentence idea:** Difficulty-based annotator routing: predict per-case difficulty and route cases between crowd workers and experts to hit target quality at minimum cost.
- **Problem:** Datasets are annotated by a single tier (all-expert = expensive; all-crowd = noisy on hard cases); per-case difficulty varies by orders of magnitude, so uniform tiering wastes expert time on easy cases and crowd accuracy on hard ones — routing is standard in industrial QA but absent from dataset construction methodology.
- **Core Hypothesis:** A difficulty predictor (trained on a small dual-annotated calibration set where crowd-expert disagreement defines difficulty) enables routing that achieves expert-tier dataset quality at a large cost reduction, with the residual quality gap concentrated in cases the predictor flags as uncertain — which get expert review anyway under the policy.
- **Why Important:** Directly reduces the price of expert-grade datasets, the binding constraint in medical and scientific imaging.
- **Why Possibly Novel:** Task routing exists in crowdsourcing for classification labels; calibrated dense-annotation routing with quality guarantees is unestablished.
- **Minimal Experiment:** Dual-annotate a calibration set; train the router; simulate routed campaigns against all-expert and all-crowd baselines on held-out dual-annotated cases. Falsified if difficulty is unpredictable pre-annotation.
- **Main Risk:** Crowd availability/ethics for medical images; difficulty predictor drift across case-mix changes.
- **Cluster:** AnnotEff

### B-0259
- **One-sentence idea:** Estimate the per-class marginal value of the next annotation and allocate labeling budgets across classes by marginal return, not by prevalence or uniformity.
- **Problem:** Multi-class campaigns allocate effort implicitly (annotate whatever appears); classes saturate at wildly different rates (common organs early, rare lesions never), so the last thousand labels of a saturated class are worthless while a starving class stays data-limited — no tooling estimates or acts on per-class marginal value.
- **Core Hypothesis:** Per-class marginal value is estimable online from class-wise learning-curve slopes (with hierarchical smoothing across classes), and slope-proportional allocation achieves the same minimum per-class accuracy at substantially lower total budget than proportional or uniform allocation — validated by replayed campaigns.
- **Why Important:** Class-level allocation is a budget lever larger than any selection heuristic, and it currently has no owner.
- **Why Possibly Novel:** Learning curves are studied per-dataset; the per-class marginal-value allocation framework with online estimation is unbuilt.
- **Minimal Experiment:** Replay 3 multi-class datasets as campaigns under allocation policies; compare budget-to-target-accuracy. Falsified if allocation policy doesn't matter (classes saturate together).
- **Main Risk:** Per-class slope estimation is noisy early, when allocation matters most (hence the hierarchical smoothing).
- **Cluster:** AnnotEff

### B-0260
- **One-sentence idea:** Statistical process control for annotation quality: continuously double-annotate a small hidden audit stream to track dataset error rate live, with control-chart triggers for intervention.
- **Problem:** Annotation quality drifts (fatigue, guideline drift, annotator turnover), but campaigns measure quality — if ever — once at the end; drift discovered post hoc means re-annotation or silent dataset defects, and no live monitoring methodology exists for dense labels.
- **Core Hypothesis:** A 3–5% hidden audit stream (cases dual-annotated without annotators knowing which) suffices to detect realistic quality-drift events within days via control charts on agreement metrics, and early intervention (targeted retraining of drifting annotators) prevents measurable end-dataset quality loss — SPC transplanted to dense annotation.
- **Why Important:** Every long campaign has drift; live detection converts irrecoverable defects into managed incidents.
- **Why Possibly Novel:** SPC is a mature industrial method; its calibrated adaptation to segmentation annotation (which agreement metrics, what audit fraction, which control limits) is undeveloped.
- **Minimal Experiment:** Inject controlled drift (guideline change, simulated fatigue) into an annotation study with the audit stream; measure detection latency vs. audit fraction. Falsified if realistic drift hides below feasible audit rates.
- **Main Risk:** Hidden auditing raises consent/ethics questions in some annotator arrangements.
- **Cluster:** AnnotEff

### B-0261
- **One-sentence idea:** Validate micro-verification as a supervision channel: 3-second binary questions ("is the boundary correct in this circle?") aggregated across many viewers into training-grade boundary supervision.
- **Problem:** The atomic unit of annotation is assumed to be drawing; but binary judgments are 100× faster, parallelize across casual annotators, and could in principle localize errors precisely if the questions are placed well — the aggregation of micro-judgments into dense supervision is unformalized and unvalidated.
- **Core Hypothesis:** Adaptively placed micro-questions (targeting model-uncertain boundary segments per B-0204) aggregated with an item-response model yield boundary-error localization with quality sufficient to drive training corrections, at a per-error cost far below tracing-based correction — with diminishing returns quantified per additional judgment.
- **Why Important:** Opens dense-annotation to the enormous casual-labor pool that can judge but not trace.
- **Why Possibly Novel:** Binary QA exists inside tools; its formalization as a primary supervision channel with aggregation theory and training integration is new.
- **Minimal Experiment:** Place micro-questions on predictions with known errors; collect judgments (crowd); measure error-localization accuracy vs. judgments-per-site; retrain with corrections. Falsified if judgments are too noisy to localize errors.
- **Main Risk:** Question placement is a chicken-and-egg with model uncertainty quality.
- **Cluster:** AnnotEff

### B-0262
- **One-sentence idea:** Train on imperfect labels by modeling each annotator's error process (systematic over/under-segmentation, boundary style) and inverting it — annotator-ID-conditioned training instead of label cleaning.
- **Problem:** Label noise handling either cleans labels (expensive) or treats noise as random (wrong — annotator errors are systematic and personal); datasets discard the annotator identity metadata that would let models learn and invert each annotator's bias, effectively wasting a free noise-structure signal.
- **Core Hypothesis:** Jointly learning a per-annotator label-transformation model (small, e.g., boundary offset fields + class confusion) with the segmentation network recovers a consensus closer to expert reference than training on raw or majority-fused labels — with the learned annotator parameters independently validated against their measured styles on multi-rater subsets.
- **Why Important:** Extracts more truth from existing noisy datasets at zero annotation cost; makes annotator metadata valuable, encouraging its retention.
- **Why Possibly Novel:** Annotator confusion matrices exist for classification crowdsourcing; the dense version with spatial boundary-style modeling and style validation is underdeveloped.
- **Minimal Experiment:** On a multi-rater dataset, train annotator-conditioned models using single-rater labels; compare recovered consensus vs. raw/fused training against held-out expert reference. Falsified if annotator styles are unlearnable.
- **Main Risk:** Requires several annotations per annotator; identifiability issues if annotators saw disjoint case types.
- **Cluster:** AnnotEff

### B-0263
- **One-sentence idea:** Measure how annotation-tool interaction latency and rendering quality causally affect label accuracy — the tool as an uncontrolled variable in every dataset.
- **Problem:** Datasets are treated as tool-independent, but annotators on laggy or low-quality viewers demonstrably cut corners (fewer polygon vertices, less zooming); tool-induced label degradation is plausibly comparable to inter-annotator variance yet has never been isolated — making cross-dataset label quality comparisons subtly confounded.
- **Core Hypothesis:** Controlled latency injection (0/100/300ms interaction delay) and rendering degradation cause measurable, systematic boundary-quality loss (vertex density drops, small-object omissions rise), with effects large enough that tool specification belongs in dataset documentation standards.
- **Why Important:** If tools shape labels, dataset datasheets, benchmark comparisons, and annotation-cost models all need a tooling axis.
- **Why Possibly Novel:** HCI studies latency generally; its causal effect on dense-label quality is unmeasured in the vision-dataset literature.
- **Minimal Experiment:** Within-subject study: same cases annotated under randomized latency/rendering conditions; measure boundary fidelity against reference. Falsified if labels are tool-robust.
- **Main Risk:** Lab conditions may understate long-session effects (fatigue-latency interactions).
- **Cluster:** AnnotEff

### B-0264
- **One-sentence idea:** Find the pre-annotation quality threshold: below what model quality does showing pre-segmentations slow annotators down or corrupt labels, versus starting blank?
- **Problem:** Model-assisted annotation is assumed beneficial whenever a model exists, but correcting a bad pre-segmentation can cost more than drawing from scratch (deletion overhead, anchoring per B-0244); the quality threshold where assistance flips from help to harm is unknown, so teams deploy assistance indiscriminately.
- **Core Hypothesis:** There is a measurable per-structure quality threshold (in boundary-F terms) below which pre-annotation increases total time and inherited-error rate, the threshold is higher for complex boundaries, and a per-case gating rule (show assistance only when predicted quality clears the threshold, via B-0010's QC) beats always-on assistance in total campaign time and quality.
- **Why Important:** Assistance deployment is universal; a validated gating rule improves every assisted campaign immediately.
- **Why Possibly Novel:** Assistance benefits are reported at aggregate level; the threshold mapping and gated-assistance policy are unmeasured.
- **Minimal Experiment:** Timed study with pre-segmentations at controlled quality levels (degraded model outputs); measure time and final quality vs. blank-start. Falsified if assistance always helps regardless of quality.
- **Main Risk:** Threshold likely varies across annotator skill (stratify by experience).
- **Cluster:** AnnotEff

### B-0265
- **One-sentence idea:** Test whether many cheap coarse masks aggregate to expert precision: crowd consensus of low-effort annotations versus single expert masks, evaluated boundary-wise.
- **Problem:** The "wisdom of crowds" is assumed transferable to dense labels, but boundary errors of casual annotators may be correlated (everyone rounds off the same concavities), in which case aggregation converges to a systematically smoothed shape rather than the truth — the aggregation-validity question for dense geometry is open.
- **Core Hypothesis:** Crowd-mask aggregation matches expert precision on convex, high-contrast boundaries but exhibits irreducible correlated bias on concavities, thin protrusions, and low-contrast segments — quantifiable as a residual bias floor that no crowd size crosses, defining exactly where experts remain necessary.
- **Why Important:** Determines the geometric limits of crowd-sourced dense annotation — a foundational fact for annotation economics.
- **Why Possibly Novel:** Crowd aggregation is studied via IoU averages; the boundary-geometry-stratified bias-floor analysis is unperformed.
- **Minimal Experiment:** Collect 15 casual masks per case on structures with expert reference; plot aggregate error vs. crowd size stratified by boundary geometry. Falsified if aggregation converges to expert level everywhere.
- **Main Risk:** Crowd platform quality variance; instructions confound (fix via single protocol).
- **Cluster:** AnnotEff

### B-0266
- **One-sentence idea:** Correspondence-based label transfer to new datasets: match unlabeled images to labeled-archive neighbors via dense correspondence, warp their labels across, and have humans verify — annotation as retrieval-plus-verification.
- **Problem:** New datasets are annotated from scratch even when visually near-identical labeled examples exist in public archives; dense-correspondence models can warp archive labels onto new images, but nobody has built or costed the retrieval-warp-verify pipeline against fresh annotation.
- **Core Hypothesis:** For domains with archive coverage (common anatomy, street scenes), retrieval-warp-verify produces accepted labels at a fraction of fresh-annotation cost, with the acceptance rate predictable from correspondence confidence — so the pipeline self-triages between transfer and fresh annotation per case.
- **Why Important:** Every past dataset becomes a discount on every future one; compounding returns on the field's accumulated labeling.
- **Why Possibly Novel:** Label warping exists within-dataset (video, atlases); the cross-dataset retrieval formulation with verification economics is unassembled.
- **Minimal Experiment:** For a "new" dataset (held-out public set), run the pipeline against an archive; measure accepted-label quality, human verify/fix time vs. from-scratch time. Falsified if verification cost erases the transfer saving.
- **Main Risk:** Archive-target license and distribution mismatches; correspondence fails exactly on novel content (by design, triaged out).
- **Cluster:** AnnotEff

### B-0267
- **One-sentence idea:** Systematically detect and correct label errors in legacy segmentation benchmarks, then re-rank state-of-the-art methods on the cleaned versions.
- **Problem:** Classic benchmarks contain uncorrected label errors (missed objects, sloppy boundaries, wrong classes); at current performance levels, top methods may differ mostly in how they fit label errors, and "progress" near the ceiling may be noise-fitting — the cleaning-and-reranking exercise done for image classification has no dense-prediction equivalent.
- **Core Hypothesis:** Model-committee disagreement plus targeted human review will find label errors affecting a non-trivial fraction of pixels/instances in standard benchmarks, and cleaned-benchmark re-evaluation will compress or reorder top-method rankings — revealing how much recent progress is real.
- **Why Important:** Benchmark integrity underwrites every empirical claim in the field; the cleaning also produces better benchmarks as an artifact.
- **Why Possibly Novel:** Label-error studies exist for classification datasets; rigorous dense-benchmark cleaning with SOTA re-ranking is largely undone.
- **Minimal Experiment:** Run committee-based error mining on one benchmark's validation set; human-verify flagged errors; re-evaluate 10 published models. Falsified if error rates are negligible or rankings are stable.
- **Main Risk:** Corrections themselves embed judgment calls (publish both versions with provenance).
- **Cluster:** AnnotEff

### B-0268
- **One-sentence idea:** Estimate per-annotator reliability without any gold standard, purely from the structure of the agreement graph across overlapping assignments, and weight label fusion accordingly.
- **Problem:** Campaigns either trust all annotators equally or maintain expensive gold-standard test items; agreement-graph methods (who agrees with whom, on what case types) could estimate reliability for free, but their validity for dense labels — where agreement is a continuous spatial quantity, not a binary match — is unestablished.
- **Core Hypothesis:** Spectral/EM-style reliability estimation extended to spatial agreement kernels recovers per-annotator quality rankings that match hidden-gold rankings closely, and reliability-weighted fusion beats majority fusion measurably — with case-type-conditional reliability (annotators good at organs, bad at lesions) as a bonus output.
- **Why Important:** Free, continuous annotator QC for every multi-annotator campaign, with no gold-item overhead.
- **Why Possibly Novel:** Gold-free reliability estimation is developed for categorical crowdsourcing; the spatial-kernel extension with case-type conditioning is open methodology.
- **Minimal Experiment:** On multi-rater data with a hidden expert reference, estimate reliabilities gold-free; compare rankings and fusion quality against gold-informed weighting. Falsified if graph structure carries no reliability signal.
- **Main Risk:** Requires overlap structure in assignments (design constraint on campaigns).
- **Cluster:** AnnotEff

### B-0269
- **One-sentence idea:** Treat annotation-guideline wording as an experimental variable: controlled guideline A/B tests measuring how phrasing and example choice shift the resulting labels.
- **Problem:** Guidelines are written once, by intuition, and never validated; different phrasings of the same intent ("include the wall" vs. diagrams vs. worked examples) plausibly shift boundaries systematically across the whole dataset — a guideline-induced bias potentially larger than annotator variance, and entirely unmeasured.
- **Core Hypothesis:** Guideline variants produce systematic, directional label shifts (not just added variance) detectable with modest annotator cohorts, worked-example-heavy guidelines reduce inter-annotator variance more than prose precision does, and guideline-induced variance is comparable in magnitude to annotator-induced variance — making guideline validation a required campaign step.
- **Why Important:** The guideline is the cheapest, most-copied artifact in annotation; validating it fixes bias at the source for entire datasets.
- **Why Possibly Novel:** Guideline effects are folklore in annotation practice; controlled measurement with variance decomposition is essentially unpublished for dense labels.
- **Minimal Experiment:** 3 guideline variants × 6 annotators × shared cases on one ambiguous structure; decompose variance into guideline/annotator/case components. Falsified if guideline variants are interchangeable.
- **Main Risk:** Effects may be structure-specific; needs replication on 2–3 structures.
- **Cluster:** AnnotEff

### B-0270
- **One-sentence idea:** Solve the annotation-portfolio problem: given a fixed budget, optimize the mix of expert masks, crowd coarse labels, verification passes, and synthetic data against a validated end-to-end model-quality objective.
- **Problem:** Annotation budgets buy a portfolio of supervision types, but each type is studied in isolation; nobody optimizes the mix jointly, and interactions (verification multiplies crowd value; synthetic data changes how many real masks are needed) mean isolated conclusions don't compose — the actual decision practitioners face has no framework.
- **Core Hypothesis:** A portfolio model built from measured component value functions (from B-0208/B-0213/B-0258-style experiments) plus estimated interaction terms predicts end-model quality across mixes well enough to optimize, and optimized portfolios beat single-type spending and naive mixes by a meaningful margin at equal cost — validated in a real end-to-end campaign.
- **Why Important:** This is the decision every data-budget owner actually makes; a validated optimizer converts label-efficiency research into practice.
- **Why Possibly Novel:** Individual supervision-type comparisons exist; the joint portfolio formulation with interaction estimation and end-to-end validation is unattempted.
- **Minimal Experiment:** Measure component value functions on one task; fit portfolio model; run three portfolios (optimized, naive, single-type) at equal budget; compare end models. Falsified if the portfolio model mispredicts badly.
- **Main Risk:** Interaction terms may be strong and task-specific, limiting transferability of the optimizer.
- **Cluster:** AnnotEff
## Section 10 — Long-tail Recognition & Segmentation [B-0271–B-0300]

### B-0271
- **One-sentence idea:** Disentangle the three conflated imbalance axes in long-tail segmentation — image frequency, instance frequency, and pixel area — and show each requires a different remedy.
- **Problem:** "Long-tail segmentation" lumps together classes that are rare across images, rare in instance count, or merely small in area; methods are compared on datasets mixing all three, so a fix for pixel scarcity (e.g., area reweighting) gets credited or blamed for image-rarity effects it cannot touch.
- **Core Hypothesis:** Controlled datasets isolating each axis will show existing long-tail methods have axis-specific effect profiles (reweighting fixes area imbalance, resampling fixes image rarity, neither fixes instance rarity), and axis-specific diagnosis of a real dataset predicts which method will help — turning method choice from lottery into decision.
- **Why Important:** The long-tail segmentation literature is uninterpretable without this decomposition; every practitioner inherits the confusion.
- **Why Possibly Novel:** The three-axis distinction is occasionally noted in passing; the controlled isolation experiment and the diagnostic-predicts-remedy validation are unperformed.
- **Minimal Experiment:** Construct axis-isolated variants by subsampling a large dataset; run 5 long-tail methods on each; verify the predicted effect profiles. Falsified if methods are axis-agnostic.
- **Main Risk:** Perfect axis isolation is impossible (correlations remain); report achieved decorrelation.
- **Cluster:** LongTail

### B-0272
- **One-sentence idea:** Demonstrate that image-level resampling — the standard long-tail remedy — barely changes pixel-level class exposure in segmentation, and replace it with crop-level rebalancing.
- **Problem:** Oversampling images containing rare classes still trains mostly on those images' abundant head-class pixels (a rare-class image is 99% background); the field imports image-level resampling from classification without noticing that dense prediction's unit of exposure is the pixel, not the image.
- **Core Hypothesis:** Measured per-class gradient exposure under image resampling shifts far less than nominal sampling ratios suggest, explaining its weak segmentation results, and crop-level rebalancing (sampling training crops centered on rare classes with controlled context) achieves the intended exposure shift and correspondingly larger tail gains at matched compute.
- **Why Important:** Corrects a silently ineffective default inherited by nearly every long-tail segmentation pipeline.
- **Why Possibly Novel:** Crop-based sampling exists ad hoc; the exposure-accounting analysis that explains why image resampling fails for dense tasks is the missing piece.
- **Minimal Experiment:** Instrument per-class pixel/gradient exposure under both schemes; correlate exposure shift with per-class accuracy gains. Falsified if image resampling already shifts exposure effectively.
- **Main Risk:** Aggressive crop rebalancing distorts context statistics (interacts with B-0276; control context in crops).
- **Cluster:** LongTail

### B-0273
- **One-sentence idea:** Measure the collateral damage of loss reweighting on head-class boundary quality and calibration, and fix it with interior-only reweighting that spares boundary pixels.
- **Problem:** Class reweighting boosts tail recall but its costs are reported only as small mIoU dips; the damage plausibly concentrates in head-class boundary precision and calibration (upweighted tail gradients push decision boundaries into head regions) — a structured cost invisible to region metrics that everyone uses.
- **Core Hypothesis:** Reweighting degrades head boundary-F and inflates head-class confidence miscalibration disproportionately to its Dice cost, and applying weights only to interior pixels (boundary pixels keep neutral weights) retains most tail gains while eliminating most boundary damage — a strictly better operating point.
- **Why Important:** Boundary quality is dense prediction's raison d'être; hidden boundary costs mean the field's tail-vs-head tradeoff is mischaracterized.
- **Why Possibly Novel:** Reweighting side effects are studied via aggregate accuracy; the boundary/calibration-stratified cost analysis and the spatial weighting fix appear new.
- **Minimal Experiment:** Sweep reweighting strength; report head boundary-F, ECE, and tail recall; test interior-only weighting. Cheap, one benchmark. Falsified if damage is boundary-uniform.
- **Main Risk:** Interior/boundary partition adds a hyperparameter (band width); results may vary with class geometry.
- **Cluster:** LongTail

### B-0274
- **One-sentence idea:** Run the statistical power analysis of long-tail benchmarks: with a handful of test instances per tail class, published per-class improvements may be statistically meaningless — quantify and fix the reporting.
- **Problem:** Tail classes have few test instances by definition (sometimes <10); per-class IoU differences of several points lie within resampling noise, yet papers claim tail improvements without confidence intervals — the field may be ranking methods on evaluation noise exactly where it claims to help.
- **Core Hypothesis:** Bootstrap analysis of standard long-tail benchmarks will show tail-class metric confidence intervals wide enough that a substantial fraction of published pairwise "improvements" are non-significant, and a corrected protocol (aggregated tail strata, reported CIs, minimum-instance thresholds) changes the literature's apparent conclusions.
- **Why Important:** Statistical validity of the field's core claims; costs nothing to fix once demonstrated.
- **Why Possibly Novel:** Power problems are generic knowledge; the concrete audit of long-tail segmentation benchmarks with re-analysis of published comparisons is undone.
- **Minimal Experiment:** Bootstrap per-class metrics on 3 benchmarks; recompute significance of 20 published method-pair tail claims. Pure analysis. Falsified if tail CIs are tight.
- **Main Risk:** Authors may dispute bootstrap assumptions for structured outputs (use block bootstrap over images).
- **Cluster:** LongTail

### B-0275
- **One-sentence idea:** Test whether the decoupling result from long-tail classification (representations are fine, only the classifier needs rebalancing) transfers to dense prediction, where the "classifier" is a spatial decoder.
- **Problem:** Long-tail classification's most influential finding — retrain only the final classifier on balanced data — is imported into segmentation by analogy, but a dense decoder does far more than classify (it localizes, shapes boundaries, integrates context), and whether tail failure lives in the representation or the decoder is unknown for dense tasks.
- **Core Hypothesis:** Decoupled retraining recovers much less of the tail gap in segmentation than in classification because tail failure is partly representational (tail features are poorly localized, not just poorly classified) — testable by probing frozen features for tail-class localizability before and after balanced decoder retraining.
- **Why Important:** Determines whether the field's cheapest long-tail fix works for dense tasks, and where the failure actually lives.
- **Why Possibly Novel:** The decoupling hypothesis has not been rigorously tested for segmentation with representational-vs-decoder attribution.
- **Minimal Experiment:** Freeze backbone, retrain decoder balanced; compare against full balanced training; probe frozen tail-feature localizability. Falsified if decoder retraining closes the gap (classification result transfers).
- **Main Risk:** Results may depend on decoder capacity (sweep two decoder sizes).
- **Cluster:** LongTail

### B-0276
- **One-sentence idea:** Quantify contextual imprisonment of tail classes — rare classes recognized only in their most typical context — and break it with context-decorrelation training.
- **Problem:** Tail classes appear in few contexts in training data, so models bind them to context (a rare traffic sign only on poles, a rare lesion only in one organ region); in novel contexts the class becomes invisible, an error mode invisible to standard evaluation because test sets share the training context distribution.
- **Core Hypothesis:** Context-swap evaluation (tail objects composited into atypical-but-plausible contexts) will show tail recall collapsing far more than head recall, the collapse magnitude will track training context diversity per class, and context-decorrelation training (context-varied compositing per B-0281) will restore much of it — establishing context diversity, not instance count, as the binding tail variable.
- **Why Important:** Redefines what "more tail data" should mean for collection and synthesis: diverse contexts, not more copies.
- **Why Possibly Novel:** Context bias is studied for head classes; the frequency-stratified analysis with the context-diversity-is-binding claim is untested.
- **Minimal Experiment:** Build context-swap tests for 15 tail + 15 head classes; measure collapse vs. training context diversity. Falsified if tail and head degrade equally.
- **Main Risk:** Compositing artifacts confound (use B-0226's artifact controls).
- **Cluster:** LongTail

### B-0277
- **One-sentence idea:** Transfer intra-class variation from head to tail: learn variation modes (pose, lighting, style deformations) on head classes and apply them as feature-space augmentation to tail classes.
- **Problem:** Tail classes have too few samples to span their own appearance variation, but much of that variation (viewpoint, illumination, imaging effects) is class-generic and richly observable on head classes — current tail augmentation ignores this transferable structure and just reweights or duplicates.
- **Core Hypothesis:** Variation directions extracted from head-class feature distributions transfer to tail classes (applying them to tail features generates plausible, label-preserving variants), improving tail segmentation more than duplication or noise augmentation at matched budgets, with gains proportional to how class-generic the learned variation modes are.
- **Why Important:** Converts head-class abundance — the very thing that defines the problem — into the tail's resource.
- **Why Possibly Novel:** Feature-space variation transfer exists in few-shot classification; the dense-prediction instantiation with mode-genericity analysis is open.
- **Minimal Experiment:** Extract head variation modes (PCA/flows on aligned features); augment tail features during decoder training; compare against duplication baselines. Falsified if transferred variation is label-destroying or useless.
- **Main Risk:** Class-specific variation (deformations unique to the tail class) is not covered — bounds the achievable gain.
- **Cluster:** LongTail

### B-0278
- **One-sentence idea:** Label borrowing through class hierarchies: supervise tail classes jointly with abundant superclass labels (every "rare terrier" is also a "dog"), quantifying how much hierarchy-mediated supervision closes the tail gap.
- **Problem:** Tail classes are trained only on their own scarce labels, though massive supervision exists one level up the hierarchy; flat label spaces structurally waste this containment relation, and hierarchy-based training in segmentation lacks a controlled accounting of what superclass supervision is worth to the tail.
- **Core Hypothesis:** Joint hierarchical training (tail logits constrained to sum into superclass predictions supervised by abundant data) improves tail localization and boundary quality substantially — the superclass teaches where-and-how-to-segment, leaving only the fine discrimination to scarce tail labels — with the gain largest for tails whose superclass is visually coherent.
- **Why Important:** A supervision multiplier for the tail that uses existing labels, no new data.
- **Why Possibly Novel:** Hierarchical classification is classic; the quantitative supervision-borrowing analysis for dense tail prediction, with coherence-stratified predictions, is unestablished.
- **Minimal Experiment:** Train flat vs. hierarchical on a hierarchy-labeled benchmark; report tail deltas stratified by superclass visual coherence. Falsified if hierarchy adds nothing to tails.
- **Main Risk:** Incoherent superclasses ("miscellaneous") could actively hurt (the stratification tests this).
- **Cluster:** LongTail

### B-0279
- **One-sentence idea:** Map when mixture-of-experts beats unified models for long-tail segmentation: dedicated tail experts with learned routing versus one shared model, as a function of tail-head feature conflict.
- **Problem:** Tail and head classes compete for shared parameters (gradient conflict), motivating tail experts — but experts fragment training data and add routing failure; the literature offers both success and failure anecdotes with no characterization of which regime a given dataset is in.
- **Core Hypothesis:** The expert-vs-unified outcome is predicted by measurable tail-head gradient conflict: high conflict (visually similar head/tail pairs competing) favors experts, low conflict favors unified capacity — and a conflict-based router design (experts only for conflicted tail groups) dominates both extremes.
- **Why Important:** Architecture choice for long-tail systems currently has no evidence-based guidance.
- **Why Possibly Novel:** MoE for long-tail exists; the conflict-metric-predicts-regime analysis and selective expert allocation are untested.
- **Minimal Experiment:** Measure per-class-pair gradient conflict on 2 benchmarks; train unified/full-expert/selective-expert variants; test the prediction. Falsified if outcomes don't track conflict.
- **Main Risk:** Gradient-conflict metrics are noisy and training-stage-dependent.
- **Cluster:** LongTail

### B-0280
- **One-sentence idea:** Hybrid parametric/non-parametric prediction: head classes served by the trained decoder, tail classes by k-NN retrieval over a labeled feature memory — because parametric compression is exactly what scarce classes can't afford.
- **Problem:** Parametric models must compress each class into shared weights, which fails when a class has 20 examples; non-parametric retrieval uses every example directly but is inefficient for abundant classes — yet segmentation systems are forced into one paradigm for all classes regardless of frequency.
- **Core Hypothesis:** A frequency-based hybrid (parametric head, retrieval tail, learned blending in the uncertain middle) beats both pure paradigms on long-tail benchmarks, with the crossover frequency measurable and stable across datasets — and tail memory can be updated instantly (new tail examples improve predictions without retraining).
- **Why Important:** The instant-update property solves the operational tail problem (new rare cases arrive continuously) that retraining-based methods structurally cannot.
- **Why Possibly Novel:** Retrieval-augmented segmentation (B-0036) meets long-tail: the frequency-crossover analysis and per-class paradigm assignment are the new science.
- **Minimal Experiment:** Implement the hybrid on one long-tail benchmark; sweep the crossover threshold; test instant-update by adding tail examples post-training. Falsified if a single paradigm dominates all frequencies.
- **Main Risk:** Retrieval latency at inference; memory feature drift if the backbone is later updated.
- **Cluster:** LongTail

### B-0281
- **One-sentence idea:** Context-matched copy-paste for tail classes: paste rare objects into contexts sampled from a learned plausibility model, testing the claim that context diversity (not paste count) drives tail gains.
- **Problem:** Copy-paste augmentation for tail classes uses random placement, which both creates implausible scenes and — per B-0276's contextual imprisonment — fails to systematically expand the context distribution that actually binds tail recognition; placement is treated as a nuisance, not the mechanism.
- **Core Hypothesis:** At matched paste volume, context-diversified plausible placement improves tail performance substantially more than random placement, and the gain per paste correlates with the novelty of the pasted context relative to the class's training contexts — directly validating context diversity as the active ingredient.
- **Why Important:** Turns copy-paste from a volume knob into a targeted mechanism against the tail's real deficit.
- **Why Possibly Novel:** Copy-paste and context bias are separate literatures; the placement-as-mechanism experiment with per-paste novelty accounting connects them testably.
- **Minimal Experiment:** Fixed paste budget: random vs. plausibility-sampled vs. novelty-maximized placement; per-class gains vs. context-novelty. Falsified if placement is irrelevant.
- **Main Risk:** Plausibility model errors create harmful implausible composites (monitor with a plausibility-quality sweep).
- **Cluster:** LongTail

### B-0282
- **One-sentence idea:** Characterize calibration as a function of class frequency in segmentation and deploy frequency-conditional recalibration — because a single temperature cannot fix a frequency-structured miscalibration.
- **Problem:** Calibration is evaluated and corrected globally, but tail classes are plausibly systematically miscalibrated in a different direction than head classes (overconfident-wrong on tails from decision-boundary crowding, underconfident-right from reweighting); downstream consumers (fusion, QC, active learning) inherit frequency-dependent confidence distortion nobody has mapped.
- **Core Hypothesis:** Per-class calibration error follows a systematic frequency trend consistent across architectures, global temperature scaling leaves the trend intact, and frequency-binned (or frequency-regressed) temperature correction removes most of it at zero accuracy cost — a drop-in fix for every long-tail model.
- **Why Important:** Every confidence-consuming pipeline behaves worse on exactly the rare classes that matter; the fix is nearly free.
- **Why Possibly Novel:** Extends B-0028's size-stratified insight to the frequency axis, which is unexamined for dense prediction calibration.
- **Minimal Experiment:** Post-hoc analysis of 4 public long-tail segmentation models: ECE vs. class frequency; fit and validate frequency-conditional temperatures. Days of work. Falsified if miscalibration is frequency-flat.
- **Main Risk:** Tail calibration estimates are noisy (same power problem as B-0274; use aggregated frequency bins).
- **Cluster:** LongTail

### B-0283
- **One-sentence idea:** Measure the tension between long-tail recognition and open-set detection: methods that boost rare-known-class confidence plausibly destroy the ability to flag never-seen classes.
- **Problem:** Long-tail methods teach models to predict rare classes confidently despite weak evidence; open-set detection needs weak evidence to trigger "unknown" — the same evidence regime pushed in opposite directions, yet the two lines of research are evaluated separately and their interaction is unmeasured in segmentation.
- **Core Hypothesis:** Applying standard long-tail remedies (reweighting, logit adjustment, tail experts) measurably degrades open-set pixel detection (unknown classes absorbed into tail predictions), the degradation scales with remedy strength, and joint objectives (tail-boosting constrained by unknown-detection floors) can recover most of both — mapping an unavoidable but optimizable tradeoff frontier.
- **Why Important:** Real deployments face rare-known and unknown classes simultaneously; optimizing one blindly sacrifices the other.
- **Why Possibly Novel:** The long-tail/open-set interaction is nearly unstudied for dense prediction; the frontier mapping would be foundational.
- **Minimal Experiment:** On a benchmark with held-out unknown classes, sweep long-tail remedy strength; plot tail accuracy vs. unknown-detection AUROC. Falsified if the axes are independent.
- **Main Risk:** Unknown-class choice affects the frontier's shape (use multiple unknown splits).
- **Cluster:** LongTail

### B-0284
- **One-sentence idea:** Federated long-tail segmentation: when every site has a different tail, federated averaging erases all of them — fix with shared trunk plus site-personalized tail heads and cross-site tail-knowledge exchange.
- **Problem:** In federations (hospitals, fleets), classes rare at one site may be common at another; FedAvg's parameter averaging cancels site-specific tail learning (small gradients drowned by the consensus), so the federation is collectively worse on tails than its best-informed member — an unmeasured, structural failure.
- **Core Hypothesis:** Tail-class knowledge measurably localizes in identifiable parameters, FedAvg demonstrably erases it (site-tail accuracy drops after aggregation rounds), and an architecture exchanging tail knowledge through feature-space exemplar sharing (privacy-compatible) instead of parameter averaging lets each site inherit others' tail competence — the federation exceeding every member.
- **Why Important:** The federation's whole premise is pooling rare experience; if aggregation destroys exactly that, the field needs to know and fix it.
- **Why Possibly Novel:** Federated learning and long-tail intersect only in early classification studies; the dense, complementary-tails setting with knowledge-localization analysis is open.
- **Minimal Experiment:** Simulate 5 sites with complementary tails from one dataset; track per-site tail accuracy through FedAvg rounds; test the exchange architecture. Falsified if FedAvg preserves tails.
- **Main Risk:** Feature-exemplar sharing needs its own privacy audit (connects to B-0115/B-0040).
- **Cluster:** LongTail

### B-0285
- **One-sentence idea:** Rare anatomical variants as medical long-tail: build a variant-enriched evaluation (situs inversus, accessory organs, post-surgical anatomy) and a variant-detection safety layer that flags when standard models should not be trusted.
- **Problem:** Segmentation models internalize modal anatomy; on variants (organ mirroring, missing/extra structures, surgical rearrangement) they confidently impose the standard layout — dangerous exactly because variants are rare enough to be absent from test sets, so the failure is certified-invisible.
- **Core Hypothesis:** Standard models fail on variants at rates far exceeding their benchmark error (measurable on a curated variant set), the failures are confidently wrong (miscalibrated), and a variant detector (layout-consistency scoring against atlas statistics) flags most variant cases for human routing — a deployable safety layer independent of fixing the models.
- **Why Important:** Variant patients exist in every population; confident wrong anatomy is among the most harmful possible outputs.
- **Why Possibly Novel:** Anatomical variants are a clinical commonplace but essentially unaddressed as a dataset/evaluation/safety problem in the segmentation literature.
- **Minimal Experiment:** Curate ~100 variant cases from public data and case repositories; evaluate 3 public models; build the layout-consistency flagger. Falsified if models handle variants gracefully.
- **Main Risk:** Variant case collection is laborious; some variants are individually so rare that even the safety evaluation is underpowered.
- **Cluster:** LongTail

### B-0286
- **One-sentence idea:** Extend post-hoc logit adjustment to structured dense outputs: frequency-corrected decision rules for segmentation applied at inference, no retraining.
- **Problem:** Logit adjustment (subtracting log class priors) is theoretically grounded and free for classification, but pixels are not IID — spatial correlation, within-image class co-occurrence, and evaluation metrics like mIoU break the theory's assumptions — and the correct structured-output analog is neither derived nor tested, so the field's cheapest fix has no dense-prediction counterpart.
- **Core Hypothesis:** A structured logit adjustment (priors computed at the appropriate unit — component-level for detection-like metrics, pixel-level for area metrics — with image-level prior updating) yields consistent tail improvements post hoc, approaching a useful fraction of trained-rebalancing gains at zero training cost, and the unit-of-adjustment choice is metric-dependent in the predicted direction.
- **Why Important:** A free tail improvement applicable retroactively to every deployed segmentation model.
- **Why Possibly Novel:** Logit adjustment for dense structured outputs, with the unit-of-adjustment analysis, is an unclaimed theoretical-empirical gap.
- **Minimal Experiment:** Apply adjustment variants to 4 public models' logits; report per-frequency-stratum deltas under multiple metrics. Pure inference. Falsified if adjustments don't transfer to dense outputs.
- **Main Risk:** Image-level prior estimation errors could hurt individual images (bound with conservative priors).
- **Cluster:** LongTail

### B-0287
- **One-sentence idea:** Determine the effective sample-size law for dense tasks: which quantity — instance count, pixel area, or context/appearance diversity — actually predicts tail-class learnability.
- **Problem:** "This class has too little data" conflates incomparable quantities: 50 instances of a large-area class may outteach 500 of a tiny one, and 20 diverse examples may beat 200 clones; collection budgets and long-tail method design both need to know what the binding quantity is, and no regression across classes has established it.
- **Core Hypothesis:** Across many classes and datasets, per-class accuracy is predicted far better by a composite effective-sample measure dominated by appearance-context diversity (feature-space coverage) than by instance count or pixel area — making diversity the collection target and count-based long-tail definitions obsolete.
- **Why Important:** Redefines the field's core variable; changes both dataset construction and how "long-tail" is measured.
- **Why Possibly Novel:** Effective-number-of-samples heuristics exist for classification reweighting; the empirical determination of the binding quantity for dense tasks is missing.
- **Minimal Experiment:** Regress per-class performance on {count, area, diversity} across 3 datasets × 2 architectures; validate the winning predictor on subsampled controlled classes. Falsified if count dominates.
- **Main Risk:** Diversity measures are feature-space-dependent (replicate with two feature sources).
- **Cluster:** LongTail

### B-0288
- **One-sentence idea:** Isolate tail boundary quality: rare classes suffer disproportionately worse boundaries even when recognized, and class-agnostic boundary transfer from head classes can fix it.
- **Problem:** Long-tail analysis stops at recognition metrics; conditional on correct recognition, tail boundaries may still be much worse (too few examples to learn class-specific boundary statistics), but this second-order deficit is unmeasured and its remedy — boundary knowledge is largely class-agnostic and abundant — is unexploited.
- **Core Hypothesis:** Recognition-conditioned boundary quality degrades with class frequency (measurable via matched-recognition comparisons), and routing tail boundary refinement through a class-agnostic boundary module trained on all classes eliminates most of the deficit — because boundary delineation, unlike recognition, transfers across classes nearly for free.
- **Why Important:** For measurement applications (sizes, areas), boundary quality is the deliverable; a tail that is found but mis-measured is still a failure.
- **Why Possibly Novel:** The recognition/boundary decomposition (B-0128) has not been applied along the frequency axis, and the class-agnostic-transfer remedy is untested there.
- **Minimal Experiment:** Compute recognition-conditioned boundary-F vs. class frequency on 2 benchmarks; attach a shared boundary-refinement head; re-measure. Falsified if boundary quality is frequency-independent.
- **Main Risk:** Confounding between class frequency and intrinsic boundary difficulty (control with matched-geometry class pairs).
- **Cluster:** LongTail

### B-0289
- **One-sentence idea:** Zero-frequency classes via compositional description — segmenting classes with zero training instances from attribute compositions — with hallucination rate as a first-class reported metric.
- **Problem:** Beyond the tail lies frequency zero: classes known to exist but absent from training; compositional description ("orange, cone-shaped, roadside") could reach them, but open-vocabulary systems are never evaluated on their false-positive behavior when the described class is truly absent — the hallucination side of zero-shot is unmeasured.
- **Core Hypothesis:** Compositional queries achieve meaningful zero-instance segmentation for attribute-decomposable classes, but current systems hallucinate the described class in a large fraction of images where it is absent, and hallucination is reducible by explicit absence calibration (per-query score floors learned from verified-absent images, extending B-0139) — making the recall-hallucination frontier the honest evaluation.
- **Why Important:** Zero-frequency handling is the boundary of what learned systems can claim; unmeasured hallucination makes current claims unsafe.
- **Why Possibly Novel:** Zero-shot segmentation reports recall-type metrics; the absence-calibrated hallucination evaluation is essentially missing.
- **Minimal Experiment:** Build present/absent query-image pairs for 20 compositional classes; measure the frontier for 3 open-vocab systems; test absence calibration. Falsified if hallucination is already negligible.
- **Main Risk:** Verifying true absence in evaluation images requires careful curation.
- **Cluster:** LongTail

### B-0290
- **One-sentence idea:** Targeted tail collection via retrieval: mine unlabeled archives/web for probable tail-class instances with open-vocabulary detectors, route to verification, and compare cost-per-useful-tail-sample against annotating random data.
- **Problem:** The tail's defining property is that random collection almost never encounters it — annotating random data costs hundreds of images per tail instance found; retrieval-directed collection could change the economics by orders of magnitude, but the pipeline's yield, verification cost, and induced bias are unquantified.
- **Core Hypothesis:** Retrieval-directed collection reduces cost-per-verified-tail-sample by 10–100× versus random annotation for retrievable classes, the retrieved distribution is measurably biased toward prototypical instances (a quantifiable diversity penalty per B-0287), and a diversity-constrained retrieval variant recovers most of the diversity at modest yield cost.
- **Why Important:** Collection, not modeling, is often the cheapest fix for the tail; this prices the fix and its hidden bias.
- **Why Possibly Novel:** Data hunting is industrial folklore; the yield/bias/diversity accounting as a reproducible methodology is unpublished.
- **Minimal Experiment:** For 10 tail classes, run retrieval-directed vs. random collection against a fixed archive; measure yield, verification cost, diversity, and downstream per-class gains. Falsified if yield gains are erased by bias.
- **Main Risk:** Retrieval works precisely for classes the detector already knows — the hardest tails stay hard (report the retrievability boundary).
- **Cluster:** LongTail

### B-0291
- **One-sentence idea:** Controlled study of sampling-temperature schedules for long-tail segmentation: does annealing from natural to balanced distribution beat any static mixture, and why?
- **Problem:** Whether to train on natural, balanced, or scheduled class distributions is decided by convention per subfield (detection uses repeat-factor sampling, classification uses two-stage); for segmentation, static-vs-scheduled has never been isolated, and the mechanism claims (early natural training builds features, late balanced training fixes decision rules) are untested folklore.
- **Core Hypothesis:** Scheduled sampling (natural→balanced annealing) beats every static mixture at matched compute, the gain comes specifically from late-stage rebalancing acting on mature features (testable by probing feature quality at the switch point), and the optimal switch point is predictable from feature-convergence diagnostics rather than fixed epochs.
- **Why Important:** A pure schedule change — free to adopt — affecting every long-tail training run.
- **Why Possibly Novel:** Two-stage training exists; the continuous-schedule comparison with mechanism probing and adaptive switch-point prediction is unrun for dense tasks.
- **Minimal Experiment:** Sweep static mixtures and schedules on one benchmark; probe features at candidate switch points; validate the adaptive rule. Falsified if a static mixture matches the best schedule.
- **Main Risk:** Interactions with learning-rate schedules confound (factorial sub-design needed).
- **Cluster:** LongTail

### B-0292
- **One-sentence idea:** Compositional long-tail: build evaluation and methods for rare class-attribute combinations (rusty car, flooded road) that class-level long-tail analysis cannot see.
- **Problem:** A class can be head-frequency while specific states of it are vanishingly rare — and those states (damaged, occluded, weathered variants) are often exactly the deployment-critical cases; benchmarks index rarity by class only, so compositional tails are invisible in both evaluation and method design.
- **Core Hypothesis:** Per-combination performance on a compositional-tail benchmark (mined from attribute-annotated data) will show failures at head-class/rare-attribute cells rivaling classic tail-class failures, standard long-tail methods (indexed on class frequency) will not help these cells, and attribute-aware rebalancing will — establishing composition as a required second axis of the long-tail problem.
- **Why Important:** Safety-critical rare states of common objects are arguably more consequential than rare object classes.
- **Why Possibly Novel:** Compositional generalization is studied in classification/VQA; the dense-prediction compositional-tail benchmark and rebalancing axis are unbuilt.
- **Minimal Experiment:** Assemble the benchmark from existing attribute-annotated segmentation data; evaluate 5 models per cell; test attribute-aware vs. class-aware rebalancing. Falsified if class-level methods already fix compositional cells.
- **Main Risk:** Attribute annotation sparsity limits cell coverage (supplement with targeted annotation).
- **Cluster:** LongTail

### B-0293
- **One-sentence idea:** Measure per-class effective capacity usage in segmentation networks and test whether explicitly reallocating capacity (wider tail-specific pathways) beats loss-based rebalancing.
- **Problem:** Loss reweighting changes gradient pressure but not architecture; if tail classes are capacity-starved (their features entangled in dimensions dominated by head classes), no reweighting can help — but per-class capacity usage has never been measured, so the field cannot distinguish optimization failure from capacity failure.
- **Core Hypothesis:** Capacity probes (per-class feature-subspace dimensionality, pruning sensitivity per class) will show tail classes occupy disproportionately shared, low-dimensional feature subspaces, and architectural reallocation (dedicated tail feature dimensions) yields gains that loss reweighting cannot reach at any strength — separating and solving the capacity component.
- **Why Important:** Distinguishes two fundamentally different failure causes that the field currently treats with one (possibly wrong) remedy.
- **Why Possibly Novel:** Capacity analysis exists for pruning research; its class-stratified application to the long-tail question is unmade.
- **Minimal Experiment:** Run capacity probes on trained long-tail models; correlate with per-class accuracy; test dedicated-dimension variants against reweighting sweeps. Falsified if tail classes show no capacity signature.
- **Main Risk:** Capacity metrics are indirect; architectural interventions change more than capacity (control carefully).
- **Cluster:** LongTail

### B-0294
- **One-sentence idea:** Quantify the label-noise/long-tail interaction: a fixed label-error rate destroys tail classes disproportionately, and noise-robust methods must be evaluated per frequency stratum.
- **Problem:** Label noise and class imbalance are studied separately, but their interaction is multiplicative for tails — 5% mislabeling of a 40-instance class corrupts a meaningful fraction of its entire supervision — and noise-robust methods (loss truncation, sample filtering) may systematically discard exactly the atypical-looking-but-correct tail samples, making them tail-hostile.
- **Core Hypothesis:** Controlled noise injection will show per-class damage scaling inversely with frequency, standard noise-robust methods will amplify (not mitigate) tail damage by filtering atypical tail samples as noise, and frequency-aware noise handling (per-class noise-rate estimation with tail-protective thresholds) fixes the amplification.
- **Why Important:** Real datasets have both problems simultaneously; methods validated on each alone may be jointly harmful.
- **Why Possibly Novel:** The interaction study and the tail-hostility hypothesis about noise-robust methods are specific, untested, and consequential.
- **Minimal Experiment:** Inject controlled label noise on a long-tail benchmark; train with/without noise-robust methods; report per-frequency-stratum damage. Falsified if noise-robust methods are tail-neutral.
- **Main Risk:** Synthetic noise may differ from real annotation errors (add one real-noise condition via B-0267's error mining).
- **Cluster:** LongTail

### B-0295
- **One-sentence idea:** Tail discovery in unlabeled pools: use open-set/novelty scoring to surface probable rare-class instances from unlabeled data for human confirmation, growing the tail's labeled set at minimum verification cost.
- **Problem:** Semi-supervised learning propagates the labeled distribution — it cannot label what annotators never labeled — so unlabeled pools full of tail instances contribute nothing to the tail; the missing primitive is discovery: finding the unlabeled tail instances so cheap human confirmation can convert them to supervision.
- **Core Hypothesis:** Ranking unlabeled regions by combined novelty (far from labeled distribution) and coherence (consistent with some labeled tail class's neighborhood) surfaces true tail instances at precision sufficient for economical verification, and each verified batch measurably lifts tail performance — a compounding discovery-verify-retrain loop that plain semi-supervised learning cannot replicate.
- **Why Important:** Unlabeled data is the only abundant resource; making it serve the tail (its blind spot) changes long-tail economics.
- **Why Possibly Novel:** Novelty detection and semi-supervised learning exist separately; the discovery-for-verification loop with precision/lift accounting for dense tail classes is unassembled.
- **Minimal Experiment:** Hide tail labels from a benchmark's training pool; run discovery ranking; measure precision@k and downstream lift per verified batch vs. random verification. Falsified if discovery precision is near base rate.
- **Main Risk:** Discovery favors prototypical tail instances (same diversity penalty as B-0290 — measure it).
- **Cluster:** LongTail

### B-0296
- **One-sentence idea:** Replace frequency-blind mIoU with deployment-utility-weighted evaluation for long-tail segmentation, and show that method rankings depend strongly on the utility model.
- **Problem:** Equal-weight class averaging (mIoU) implicitly assigns identical importance to every class — an arbitrary utility model that matches no deployment; safety-critical rare classes and cosmetic common ones count the same, and methods are ranked (and designed) against this fiction.
- **Core Hypothesis:** Under explicit utility models derived from real applications (e.g., safety-weighted for driving, measurement-weighted for medical), published method rankings reorder substantially, and some celebrated long-tail methods optimize exactly the classes real utilities down-weight — demonstrating the field has been optimizing an unexamined objective.
- **Why Important:** Metrics are the field's steering wheel; making the utility model explicit and varied is prerequisite to meaningful progress claims.
- **Why Possibly Novel:** Utility-weighted evaluation is discussed abstractly; the concrete re-ranking study with application-derived utility models for long-tail segmentation is undone.
- **Minimal Experiment:** Define 3 application utility models; re-rank 10 published methods' results under each. Pure re-analysis. Falsified if rankings are utility-invariant.
- **Main Risk:** Utility models are contestable (publish them as replaceable modules, report sensitivity).
- **Cluster:** LongTail

### B-0297
- **One-sentence idea:** Measure the order of forgetting during fine-tuning — tail classes are erased first — and build tail-protective fine-tuning that shields frequency-critical parameters.
- **Problem:** Every fine-tune (new site, new data, continual updates) redistributes capacity; if forgetting follows reverse-frequency order (tails die first, heads persist), then routine model maintenance systematically destroys exactly the classes hardest to restore — a dynamic the continual-learning literature hasn't examined through the frequency lens.
- **Core Hypothesis:** Forgetting curves during standard fine-tuning are strongly frequency-ordered, the effect is driven by parameter sharing (tail-critical parameters identified via B-0293-style probes get overwritten by head-dominated gradients), and selective protection of tail-critical parameters (frequency-weighted EWC-style penalties) preserves tails at minor cost to adaptation speed.
- **Why Important:** Model maintenance is continuous in deployment; unprotected fine-tuning quietly undoes all long-tail investment.
- **Why Possibly Novel:** Catastrophic forgetting is studied task-wise; the within-task frequency-ordered forgetting law and its targeted mitigation are unexamined.
- **Minimal Experiment:** Fine-tune long-tail-trained models on shifted data; track per-frequency forgetting curves; test frequency-weighted protection. Falsified if forgetting is frequency-flat.
- **Main Risk:** Frequency confounds with learnability (control by matching initial per-class accuracy).
- **Cluster:** LongTail

### B-0298
- **One-sentence idea:** Intra-class tails: discover rare sub-modes within head classes (unusual poses, rare sub-types) via feature clustering, and rebalance at sub-mode level — long-tail treatment below the label granularity.
- **Problem:** Class labels hide internal distributions: a head class contains rare sub-modes that fail like tail classes but are invisible to any class-indexed analysis or remedy; the effective tail is defined by the data's modes, not the ontology's labels, and no methodology addresses imbalance below label granularity.
- **Core Hypothesis:** Unsupervised sub-mode discovery within head classes will reveal sub-modes whose error rates rival tail classes, sub-mode-level rebalancing will fix them without any new labels, and total error reduction from sub-mode treatment will exceed class-level long-tail treatment on ostensibly balanced datasets — the tail was hiding inside the head all along.
- **Why Important:** Extends long-tail methodology to the datasets that believe they don't have the problem.
- **Why Possibly Novel:** Hidden-stratification is documented in medical classification; the dense-prediction sub-mode rebalancing methodology with the head-hides-tail quantification is open.
- **Minimal Experiment:** Cluster within-class features on 2 benchmarks; measure per-cluster error dispersion; rebalance at cluster level and re-measure. Falsified if within-class error is mode-uniform.
- **Main Risk:** Clusters may capture nuisance factors (background) rather than meaningful sub-modes.
- **Cluster:** LongTail

### B-0299
- **One-sentence idea:** Decompose per-tail-class failure into detectability versus delineability — some rare classes are found-but-mistraced, others missed-entirely — and route each to its matching remedy.
- **Problem:** Tail improvements are pursued with a single toolbox, but a class failing because the model never proposes it needs recognition-side fixes (rebalancing, retrieval per B-0280), while a class found but badly traced needs boundary-side fixes (per B-0288); without per-class failure typing, remedies are misallocated and their evaluations muddied.
- **Core Hypothesis:** A per-class decomposition (detection recall vs. recognition-conditioned boundary quality, extending B-0128 to the frequency axis) will reveal a bimodal failure typology among tail classes predictable from class properties (size, context-dependence, boundary complexity), and remedy-to-type matching will outperform uniform application of any single remedy at equal effort.
- **Why Important:** Turns long-tail improvement from blanket method application into diagnosis-driven treatment.
- **Why Possibly Novel:** The failure-typology-with-routing methodology for tail classes has not been formulated.
- **Minimal Experiment:** Run the decomposition on 30 tail classes across 2 benchmarks; cluster failure types; apply matched vs. mismatched remedies to type exemplars. Falsified if failure types don't separate or remedies aren't type-specific.
- **Main Risk:** Small per-class test counts limit typing confidence (aggregate by predicted type, per B-0274).
- **Cluster:** LongTail

### B-0300
- **One-sentence idea:** Fit the collection scaling law for tail classes: marginal accuracy per additional labeled sample as a function of current class frequency, enabling principled collection budgets per class.
- **Problem:** Collection budgeting for tails asks "how many more samples until this class works," and the field has no curve to consult; the marginal value of the next tail sample (plausibly enormous at n=20, unknown when it fades) has never been fit across classes, so budgets are guesses.
- **Core Hypothesis:** Per-class accuracy follows a shared parametric curve in effective sample size (per B-0287's measure) with class-specific difficulty offsets estimable from a few points, so a target accuracy translates into a predicted collection requirement with calibrated uncertainty — validated by held-out collection simulations.
- **Why Important:** Converts tail data collection from faith-based to quantitative — the budgeting instrument (B-0252) specialized where budgets are hardest to set.
- **Why Possibly Novel:** Learning curves exist per dataset; the per-class frequency-indexed law with difficulty decomposition and collection-decision validation is unbuilt.
- **Minimal Experiment:** Subsample classes across frequency ranges on 3 datasets; fit the shared curve; validate predictions on held-out classes' subsampling trajectories. Falsified if per-class curves share no structure.
- **Main Risk:** Difficulty offsets may dominate the shared structure, leaving predictions too loose to guide budgets.
- **Cluster:** LongTail
## Section 11 — Cross-domain Transfer [B-0301–B-0330]

### B-0301
- **One-sentence idea:** Decompose exactly what transfers from natural-image pretraining to medical segmentation — low-level edge machinery versus semantic organization — via layer-wise transplant-and-freeze experiments.
- **Problem:** Natural-image pretraining helps medical tasks, but the field doesn't know why: if only early-layer edge/texture machinery transfers, then the enormous investment in semantically richer natural pretraining is wasted on medicine, and lighter alternatives would suffice — the attribution has never been cleanly measured.
- **Core Hypothesis:** Layer-wise transplantation (freeze natural-pretrained layers k..K, reinitialize the rest) will show medical transfer value concentrating overwhelmingly in early layers, with late-layer semantic features contributing near zero or negatively — implying cheap edge-oriented pretraining could replace web-scale pretraining for medical dense tasks.
- **Why Important:** Redirects pretraining investment for an entire application domain based on measurement.
- **Why Possibly Novel:** Feature-transferability studies exist for classification circa early CNNs; the dense-task, modern-architecture, medical-target version with the cheap-pretraining implication is missing.
- **Minimal Experiment:** Layer-block transplant grid on 2 medical tasks × 2 backbones; compare against edge-task-pretrained lightweight baselines. Falsified if late layers carry substantial value.
- **Main Risk:** Layer-wise attribution is entangled with optimization effects (control with multiple learning-rate regimes).
- **Cluster:** CrossDom

### B-0302
- **One-sentence idea:** Establish the science of 2D→3D weight inflation: which inflation strategy wins, when inflation beats native 3D pretraining, and what property of the 2D source predicts inflated performance.
- **Problem:** 3D medical models routinely initialize from inflated 2D weights (copied/averaged along the new axis) chosen by convention; strategies are never compared controlled, and the field doesn't know when inflation is a crutch that native (but data-poorer) 3D pretraining would beat.
- **Core Hypothesis:** Inflation strategy matters measurably (axis-aware initialization preserving 2D filter statistics beats naive copying), inflated-2D beats native-3D pretraining below a quantifiable 3D-data threshold and loses above it, and the crossover is predictable from the target task's through-plane information content.
- **Why Important:** Every 3D medical project makes this decision; a validated rule replaces folklore at zero cost.
- **Why Possibly Novel:** Inflation is used everywhere and studied almost nowhere; the crossover law is an obvious, unclaimed measurement.
- **Minimal Experiment:** Inflation-strategy grid × 3D-pretraining-data sweep on 2 tasks; locate crossovers; test the through-plane predictor. Falsified if strategies tie and no crossover exists.
- **Main Risk:** Conclusions may shift with architecture family (test conv and transformer variants).
- **Cluster:** CrossDom

### B-0303
- **One-sentence idea:** Transfer video models to volumes: treat the through-plane axis as time and test whether temporal inductive biases (motion smoothness, tracking) map onto anatomical continuity.
- **Problem:** Video pretraining is abundant and 3D medical pretraining scarce; slices through anatomy resemble frames through time (smooth deformation of structures), suggesting video-pretrained temporal machinery could transfer — but the analogy's validity has never been tested, and it might fail on the ways anatomy is unlike motion (bidirectionality, no causality).
- **Core Hypothesis:** Video-pretrained models fine-tuned on volumes (z-as-time) outperform image-pretrained 2D and inflated baselines specifically on through-plane consistency metrics, with the gain tracking how "motion-like" the anatomy's slice-to-slice change statistics are — validating (and bounding) the analogy quantitatively.
- **Why Important:** Would unlock the largest pretrained-model ecosystem (video) for volumetric medicine.
- **Why Possibly Novel:** Scattered attempts exist; the systematic test with slice-statistics-predicts-transfer analysis is missing.
- **Minimal Experiment:** Fine-tune matched video/image/inflated backbones on 3 volumetric tasks; report through-plane surface metrics; correlate gains with slice-change statistics. Falsified if video pretraining offers nothing beyond image pretraining.
- **Main Risk:** Video models' frame-rate assumptions may mismatch slice spacing (test spacing-conditioned variants per B-0001).
- **Cluster:** CrossDom

### B-0304
- **One-sentence idea:** Cross-spectral transfer surgery: identify which pretrained-feature channels break under RGB→thermal/NIR transfer and repair them with channel-statistics reinitialization rather than full fine-tuning.
- **Problem:** RGB-pretrained models transfer poorly to thermal/NIR imagery, and the failure is treated as generic domain gap; but the cause is plausibly localized — color-opponent and spectral-specific channels become meaningless while structure channels remain valid — and localized repair has never been tried in place of blanket fine-tuning.
- **Core Hypothesis:** A channel-level diagnostic (activation-statistics divergence between RGB and thermal inputs) will identify a minority of broken channels, and reinitializing only those (keeping structural channels frozen) will match or beat full fine-tuning in low-data thermal regimes — because it preserves transferable structure that full fine-tuning destroys.
- **Why Important:** Thermal/NIR segmentation (fire per B-0077, surveillance, agriculture) always has scarce labels; surgical transfer is the right tool for that regime.
- **Why Possibly Novel:** Cross-spectral transfer is handled by fine-tuning or paired translation; channel-level diagnosis-and-repair is an untested mechanism.
- **Minimal Experiment:** Compute channel diagnostics on paired RGB/thermal scenes; repair vs. full fine-tune vs. freeze on a thermal segmentation task at several label budgets. Falsified if breakage isn't channel-localized.
- **Main Risk:** Channel entanglement in modern backbones may blur the broken/intact distinction.
- **Cluster:** CrossDom

### B-0305
- **One-sentence idea:** Settle stain transfer versus stain-invariant training in histopathology with a controlled same-tissue comparison, and decompose the residual gap after each.
- **Problem:** Two incompatible schools handle stain variation — normalize images to a reference stain versus train invariance via stain augmentation — and both claim superiority on incomparable setups; labs pick by lineage, and the residual failures of each approach are never characterized side by side.
- **Core Hypothesis:** On a controlled benchmark (same tissue blocks, multiple stains/scanners), stain augmentation dominates normalization for segmentation (normalization errors are irreversible preprocessing damage), the residual gap after augmentation is dominated by morphology-affecting variation (section thickness) rather than color — redirecting effort from color handling to the actual residual.
- **Why Important:** Digital pathology deployment is blocked on cross-lab robustness; resolving the schools' dispute with decomposition guides the whole field.
- **Why Possibly Novel:** Comparisons exist piecemeal; the same-tissue controlled design with residual-gap decomposition is unexecuted.
- **Minimal Experiment:** Use re-stained/re-scanned public sets; matched training under each school; stratify residual errors by variation source. Falsified if normalization wins or residuals are color-dominated.
- **Main Risk:** Same-tissue multi-stain data is limited (may need one collaborating lab).
- **Cluster:** CrossDom

### B-0306
- **One-sentence idea:** Attribute the histopathology scanner gap to its physical components — optics (PSF, focus), color pipeline, and compression — via component-wise simulation, enabling targeted physics-informed calibration transfer.
- **Problem:** "Scanner shift" in pathology bundles optical, chromatic, and compression differences; adaptation methods attack the bundle blindly, though each component has a cheap targeted fix (PSF matching, color calibration from a scanned target, recompression) if only the field knew which dominates.
- **Core Hypothesis:** Component-wise forward simulation (apply scanner B's estimated PSF/color/compression to scanner A images) will decompose the performance gap into additive component contributions, with color-pipeline differences dominating for most scanner pairs — meaning a scanned calibration slide plus color-transform is most of the answer, no learning required.
- **Why Important:** Replaces heavy adaptation machinery with cheap metrology where the physics permits — the right engineering economics.
- **Why Possibly Novel:** Scanner variability is documented descriptively; the causal component decomposition with targeted-fix validation is missing.
- **Minimal Experiment:** Estimate per-scanner component parameters from calibration slides; simulate component swaps; measure gap decomposition on 3 scanner pairs. Falsified if components don't compose additively.
- **Main Risk:** Component interactions (focus × compression) may break additivity.
- **Cluster:** CrossDom

### B-0307
- **One-sentence idea:** Human→animal medical transfer along anatomical homology: use evolutionary homology maps as the transfer prior and test whether transfer quality tracks homology distance.
- **Problem:** Veterinary imaging has almost no labeled data while human medical models abound; naive transfer fails unpredictably across species and organs, and no framework predicts which human-trained capabilities port to which species — though comparative anatomy provides exactly such a structure map for free.
- **Core Hypothesis:** Transfer performance from human models to animal targets correlates strongly with anatomical homology/conservation measures per organ, homology-guided label mapping (transferring to the homologous structure, not the visually similar one) beats naive class matching, and the correlation enables zero-annotation triage of which veterinary tasks inherit human models.
- **Why Important:** Multiplies medical AI's reach into veterinary and comparative research at near-zero data cost, with a principled applicability map.
- **Why Possibly Novel:** Cross-species transfer happens ad hoc; homology as a quantitative transfer prior appears untested.
- **Minimal Experiment:** Evaluate human-trained organ models on annotated veterinary sets (dogs/pigs available publicly) across organs; correlate with homology scores. Falsified if transfer is homology-independent.
- **Main Risk:** Species differences in imaging protocols confound anatomy effects (control by protocol matching).
- **Cluster:** CrossDom

### B-0308
- **One-sentence idea:** Build the dense-task transfer matrix: measure pairwise transfer value among segmentation, depth, normals, and boundary tasks across domains, testing whether geometric-task pretraining specifically improves segmentation boundaries.
- **Problem:** Auxiliary and pretraining task choices for dense prediction are made by intuition ("depth probably helps"); the pairwise task-transfer structure — which dense task teaches what to which — has been mapped for natural-image classification eras but not for modern dense prediction across domain gaps.
- **Core Hypothesis:** The transfer matrix is strongly asymmetric and structured: geometric tasks (depth/normals) transfer boundary precision to segmentation but not semantics, segmentation transfers little back to geometry, and the structure is stable across domains — so the matrix, measured once, becomes a reusable design table for auxiliary-task selection.
- **Why Important:** Converts multi-task/pretraining design from folklore to lookup; boundary-precision transfer would be immediately exploited (per B-0288).
- **Why Possibly Novel:** Task-transfer atlases exist for classification-era representation learning; the dense-to-dense matrix with region/boundary metric separation is unbuilt.
- **Minimal Experiment:** Pretrain on each source task, probe on each target with metrics separated; 4×4 matrix × 2 domains. Falsified if the matrix is symmetric/unstructured.
- **Main Risk:** Matrix entries may depend on pretraining scale (report at two scales).
- **Cluster:** CrossDom

### B-0309
- **One-sentence idea:** Measure inter-domain gradient conflict in multi-domain segmentation training and fix it with conflict-aware batch composition, rather than architectural separation.
- **Problem:** Joint training across domains sometimes underperforms per-domain training ("domain interference"), and the field responds with domain-specific parameters; but interference plausibly arises transiently from conflicting gradients in mixed batches — a scheduling problem, not an architectural one — and batch composition is never treated as the control variable.
- **Core Hypothesis:** Per-domain gradient conflict is measurable, batch-composition-dependent, and predictive of final interference; conflict-aware scheduling (grouping compatible domains within batches, alternating conflicting ones with appropriate momentum handling) recovers most per-domain performance without any added parameters — beating domain-specific-parameter solutions at matched capacity.
- **Why Important:** If scheduling solves interference, the field's move toward parameter fragmentation is unnecessary complexity.
- **Why Possibly Novel:** Gradient conflict is studied for multi-task; the multi-domain dense-prediction version with batch composition as the intervention is unexplored.
- **Minimal Experiment:** Train on 4 domains with instrumented gradient conflict; compare mixed vs. conflict-aware batching vs. domain-specific BN at matched capacity. Falsified if interference is batch-composition-independent.
- **Main Risk:** Conflict metrics fluctuate through training; scheduling gains may not survive learning-rate interactions.
- **Cluster:** CrossDom

### B-0310
- **One-sentence idea:** Adapter arithmetic for unseen domains: compose adapters trained on multiple seen domains (weighted combinations) to handle novel domains, testing whether domain adaptation is compositional in adapter space.
- **Problem:** A new domain currently requires new adaptation data and training; if a foggy-night domain could be served by combining a fog adapter and a night adapter, unseen-domain coverage would follow combinatorially from linear training investment — but adapter compositionality for dense prediction is an untested conjecture.
- **Core Hypothesis:** For factorizable domain shifts (weather × time × sensor), linear adapter combinations achieve a large fraction of oracle (jointly trained) performance on held-out factor combinations, composition weights are predictable from the target's feature statistics, and non-factorizable shifts fail identifiably — mapping where compositionality holds.
- **Why Important:** Combinatorial domain coverage from linear training cost would change robustness economics for autonomy and surveillance.
- **Why Possibly Novel:** Task arithmetic exists for classification/LLMs; domain-factor arithmetic for dense prediction with a factorizability boundary is open.
- **Minimal Experiment:** Train single-factor adapters on a driving dataset with factor annotations; evaluate combinations on held-out factor pairs vs. oracle joint adapters. Falsified if compositions perform at single-adapter level.
- **Main Risk:** Factor interactions in image formation (fog at night ≠ fog + night) may dominate.
- **Cluster:** CrossDom

### B-0311
- **One-sentence idea:** Determine when weight-space merging of domain-expert segmentation models works: the feature-alignment precondition for model soups across domains.
- **Problem:** Weight averaging of fine-tuned models ("soups") works surprisingly often for classification, offering free multi-domain models without joint training; for dense prediction across domains it sometimes works and sometimes catastrophically fails, and no diagnostic predicts which — so a potentially free capability sits unused for lack of a precondition theory.
- **Core Hypothesis:** Merging succeeds iff the experts remain in the same loss basin (measurable via weight-space distance and mode-connectivity probes), the precondition is controllable (shared warmup schedules keep experts mergeable), and a pre-merge diagnostic predicts merged performance accurately — turning merging into a reliable tool with a go/no-go test.
- **Why Important:** Free multi-domain models from independently trained experts would simplify every multi-site development workflow.
- **Why Possibly Novel:** Soup research is classification-centric; the dense-prediction failure modes, controllable precondition, and validated diagnostic are missing.
- **Minimal Experiment:** Fine-tune domain experts under varying shared-initialization regimes; merge; correlate merged performance with basin diagnostics. Falsified if mergability is unpredictable.
- **Main Risk:** Dense decoders may be less linearly connected than classifiers, making the useful regime narrow.
- **Cluster:** CrossDom

### B-0312
- **One-sentence idea:** Language as the alignment bridge for cross-domain dense transfer when no paired or even unpaired image correspondence exists — align both domains' features to shared text anchors.
- **Problem:** Feature-alignment adaptation needs target images resembling source structure; for extreme gaps (sketch↔photo, map↔satellite, diagram↔radiograph) no image-space correspondence exists, but both domains' contents are describable in the same language — an alignment substrate current dense-transfer methods ignore.
- **Core Hypothesis:** Anchoring both domains' region features to a shared text-embedding space (via per-domain lightweight projection heads trained on domain-local text pairs) enables label transfer across gaps where image-space UDA fails completely, with transfer quality tracking the domains' shared describability (measurable via caption-overlap statistics).
- **Why Important:** Extends transfer to domain pairs currently considered unbridgeable, using ubiquitous weak text supervision.
- **Why Possibly Novel:** Language-guided adaptation exists in early forms for classification; the dense-prediction, extreme-gap formulation with describability analysis is unclaimed.
- **Minimal Experiment:** Transfer segmentation across one extreme pair (e.g., photo→schematic/sketch data) via text anchoring vs. image-space UDA baselines. Falsified if text anchoring adds nothing over UDA.
- **Main Risk:** Text anchors are coarse (region-level), possibly capping boundary quality (combine with class-agnostic boundary modules per B-0288).
- **Cluster:** CrossDom

### B-0313
- **One-sentence idea:** Benchmark domain-distance metrics as transfer predictors: which cheap measurement between source and target best predicts realized fine-tuning gain across many domain pairs — building a validated "transferability oracle" for dense tasks.
- **Problem:** Practitioners choose sources and predict porting effort with unvalidated intuitions; candidate distances (feature-space OT/FID-type, label-statistics divergence, frequency signatures) have never been raced against realized dense-task transfer outcomes at scale, so no number can be trusted for planning.
- **Core Hypothesis:** Predictive power varies enormously across candidate metrics, a supervised combination predicts transfer gain and required-fine-tuning-data within planning-useful tolerance, and the best predictors differ for region versus boundary outcomes — yielding the first validated planning instrument for cross-domain dense transfer.
- **Why Important:** Transfer decisions allocate large budgets on guesswork; even coarse validated prediction changes planning.
- **Why Possibly Novel:** Transferability estimation exists for classification checkpoints; the cross-domain dense-task version with dual-metric outcomes is unbuilt.
- **Minimal Experiment:** Assemble 30 source→target dense transfer pairs from public data; measure all candidate distances; fine-tune all pairs; fit and validate the predictor on held-out pairs. Falsified if nothing predicts transfer.
- **Main Risk:** The pair sample may under-represent extreme gaps; predictor may overfit dataset families.
- **Cluster:** CrossDom

### B-0314
- **One-sentence idea:** Detect negative transfer before paying for it: build predictors for when pretrained initialization hurts dense-task training relative to from-scratch, and characterize the negative-transfer regime.
- **Problem:** Pretraining is assumed universally beneficial, but from-scratch training occasionally wins (very different domains, large target data, geometry-heavy tasks); the negative-transfer regime for dense prediction is uncharacterized, so no one knows when the default is wrong — and discovering it costs a full training run.
- **Core Hypothesis:** Negative transfer occupies a predictable regime (large target data × large domain distance × geometry-dominated tasks), is detectable early in training from relative loss-curve dynamics (allowing cheap abort-and-restart), and its mechanism is feature-reuse lock-in (pretrained features occupy dimensions the task needs for different content — probeable via B-0293-style capacity analysis).
- **Why Important:** Prevents both silent underperformance from bad defaults and wasted pretraining engineering where it can't help.
- **Why Possibly Novel:** Negative transfer is documented anecdotally; the regime map, early detector, and mechanism probe for dense tasks are unassembled.
- **Minimal Experiment:** Grid of {pretrained, scratch} across target-data sizes × domain distances on 6 tasks; fit the regime boundary; validate the early detector. Falsified if pretraining never loses.
- **Main Risk:** Regime boundaries may shift with optimization recipes (report across two recipes).
- **Cluster:** CrossDom

### B-0315
- **One-sentence idea:** Validated checkpoint selection from model zoos for dense tasks: race cheap proxies (frozen-feature probing, gradient measures) against exhaustive fine-tuning as selection oracles.
- **Problem:** Zoos hold hundreds of candidate checkpoints; teams pick by fame or by fine-tuning a few, and cheap selection proxies validated for classification are unvalidated for dense prediction, where decoder interactions may break their assumptions — so the selection decision is unprincipled exactly where fine-tuning is most expensive.
- **Core Hypothesis:** Frozen-feature dense probing (light decoder, few epochs) ranks checkpoints in near-perfect agreement with full fine-tuning at 1–2% of the cost, cheaper gradient/energy proxies degrade gracefully but usefully, and proxy validity varies systematically with target-domain distance — yielding a costed selection protocol.
- **Why Important:** Multiplies effective zoo value and saves community-scale fine-tuning compute.
- **Why Possibly Novel:** Transferability proxies are classification-validated; the dense-prediction validation with cost-tiered protocol is missing (complements B-0050's ranking-flip question).
- **Minimal Experiment:** 20 checkpoints × 4 dense targets: full fine-tune (reference) vs. proxy rankings; report rank correlations by cost tier. Falsified if proxies fail for dense tasks.
- **Main Risk:** Reference fine-tuning quality itself varies with budget (fix budgets carefully).
- **Cluster:** CrossDom

### B-0316
- **One-sentence idea:** Test whether generative (diffusion) model features are more domain-robust dense representations than discriminative features — and localize where each wins across the shift spectrum.
- **Problem:** Diffusion models trained for generation encode dense correspondences that transfer surprisingly well, but claims of their superiority over discriminative SSL features are anecdotal and shift-unstratified; the field lacks a controlled comparison isolating feature source from everything else across domain gaps.
- **Core Hypothesis:** Generative features degrade more slowly with domain distance for boundary/correspondence tasks (generation requires modeling all appearance, not just discriminative cues) but trail in-domain semantic accuracy, with the crossover point measurable — so feature-source choice should be a function of expected deployment shift, not fashion.
- **Why Important:** Feature-substrate choice is upstream of everything; a shift-conditional answer would rationalize it.
- **Why Possibly Novel:** Diffusion-feature papers show isolated wins; the shift-stratified controlled race with crossover measurement is unrun.
- **Minimal Experiment:** Frozen features from matched-scale generative/discriminative models; probe on tasks at graded domain distances; locate crossovers per metric type. Falsified if one substrate dominates everywhere.
- **Main Risk:** Matching model scale/data across paradigms is hard; conclusions may be scale-dependent.
- **Cluster:** CrossDom

### B-0317
- **One-sentence idea:** Characteristic-scale mismatch in cross-domain transfer (satellite→drone→ground): measure the transfer cost of object-scale distribution shifts and fix it with scale-canonicalizing input pyramids rather than fine-tuning.
- **Problem:** Domains often differ primarily in characteristic object scale (a car is 20 pixels from satellite, 2000 from ground); scale mismatch masquerades as semantic domain gap and gets treated with heavy adaptation, though it may be correctable by explicit scale normalization — the scale component of cross-domain gaps has not been isolated.
- **Core Hypothesis:** A scale-decomposition experiment (resampling targets to match source characteristic scale) will show scale mismatch explains a large fraction of cross-viewpoint transfer gaps, and a scale-canonicalizing front end (estimate per-region GSD/object scale, resample to canonical) recovers that fraction without touching model weights — cheaper and safer than adaptation.
- **Why Important:** Aerial-to-ground ecosystems (mapping, agriculture, inspection) constantly port models across viewpoint scales with unnecessary machinery.
- **Why Possibly Novel:** Scale augmentation is standard; scale as the measured, separable component of cross-domain gaps with a canonicalization fix is unframed.
- **Minimal Experiment:** Cross-viewpoint transfer with/without scale canonicalization on public aerial/drone/ground segmentation sets; decompose gaps. Falsified if scale explains little.
- **Main Risk:** Scale estimation errors on heterogeneous scenes; residual appearance gaps still need handling.
- **Cluster:** CrossDom

### B-0318
- **One-sentence idea:** Cross-domain distillation without paired data: transfer a teacher's dense knowledge to a student in a different domain via relational (feature-geometry) targets instead of per-pixel matching.
- **Problem:** Distillation assumes teacher and student see the same inputs; when the target domain differs (teacher on natural images, student on thermal/medical), per-pixel distillation is undefined and current practice falls back to weight transfer — discarding the teacher's relational knowledge (which classes/parts relate how) that is domain-invariant and distillable in principle.
- **Core Hypothesis:** Distilling relation structures (inter-class feature distances, part-whole co-activation patterns, boundary-response statistics) from teacher-domain batches to student-domain batches improves student segmentation beyond weight-initialization transfer, with gains concentrated in semantic organization (recognition) rather than boundary precision — a testable signature of what relational knowledge carries.
- **Why Important:** Unlocks the knowledge of large single-domain teachers for every unpaired target domain.
- **Why Possibly Novel:** Relational distillation exists within-domain; the cross-domain unpaired formulation with the semantic-vs-boundary signature prediction is open.
- **Minimal Experiment:** Distill a strong natural-image teacher into thermal/medical students via relational targets vs. init-only; separate metric reporting. Falsified if relational targets add nothing over initialization.
- **Main Risk:** Relation structures may be domain-contingent (class co-occurrence differs), teaching wrong priors.
- **Cluster:** CrossDom

### B-0319
- **One-sentence idea:** Test the anomaly-segmentation universality hypothesis: joint training on industrial defects and medical lesions improves both, because both tasks share a "deviation from learned normality" core.
- **Problem:** Industrial defect segmentation and medical lesion segmentation evolved as separate literatures with parallel method development; if their shared structure (subtle deviations from a strong normal prior) dominates their domain differences, the fields are wastefully duplicating effort — a cross-pollination experiment neither field has run.
- **Core Hypothesis:** A jointly trained anomaly-segmentation model (shared deviation-detection machinery, domain-specific normal priors) outperforms same-capacity domain-specific models on both sides, transfer is asymmetric in an informative direction (industrial's texture regularity teaches medical more than vice versa, or the reverse), and the shared component is identifiable via ablation.
- **Why Important:** Positive results would merge two method communities and their datasets; negative results would falsify a popular latent assumption.
- **Why Possibly Novel:** The cross-field joint-training experiment with shared/specific decomposition appears unattempted despite the obvious analogy.
- **Minimal Experiment:** Joint vs. separate training on one industrial (defect) and one medical (lesion) benchmark at matched capacity; ablate the shared trunk. Falsified if joint training helps neither.
- **Main Risk:** Domain interference (per B-0309) could mask genuine shared structure (control batch composition).
- **Cluster:** CrossDom

### B-0320
- **One-sentence idea:** Layout canonicalization for viewpoint transfer: correct the layout-statistics rotation between overhead and ground views (sky-above priors vs. map-like priors) before transfer, isolating layout from appearance in viewpoint gaps.
- **Problem:** Aerial↔ground transfer fails partly because learned spatial priors (classes' absolute/relative positions) are viewpoint-specific — road-below-sky versus road-as-network — and appearance-focused adaptation cannot touch this layout component, which has never been separated from appearance in viewpoint-transfer analysis.
- **Core Hypothesis:** Layout priors are extractable and swappable (measurable via position-conditional prediction probes), a layout-reprior intervention (retrain only position-encoding/late-layout layers on sparse target data) recovers a large share of the viewpoint gap at a fraction of full fine-tuning, and the layout component's size explains why viewpoint gaps resist appearance-based UDA (per B-0098's geometry blind spot).
- **Why Important:** Names and fixes the component that makes viewpoint transfer anomalously hard for standard adaptation.
- **Why Possibly Novel:** Spatial-prior analysis exists in-domain; its role in cross-viewpoint transfer failure, with the targeted-relayering fix, is unmeasured.
- **Minimal Experiment:** Probe layout priors of aerial- and ground-trained models; run layout-only vs. appearance-only vs. full adaptation across the viewpoint pair. Falsified if layout retraining adds nothing.
- **Main Risk:** Layout and appearance layers may not separate cleanly in modern architectures.
- **Cluster:** CrossDom

### B-0321
- **One-sentence idea:** Decompose the dermoscopy↔clinical-photo gap within the same disease: which acquisition component (optics/magnification, illumination geometry, framing/distance, calibration) dominates transfer failure for skin lesion segmentation.
- **Problem:** Models trained on dermoscopy fail on smartphone photos of the same lesions and vice versa; the gap spans several simultaneously varying acquisition factors, and teleodermatology deployment (photos in, dermoscopy-grade analysis out) is blocked without knowing which factor to correct — no factorized measurement exists.
- **Core Hypothesis:** Using paired captures (same lesion, both modalities, available in public datasets and easily extended), component-wise bridging (simulate each factor's transform separately) will show illumination geometry and magnification dominate over color calibration, and a two-factor correction front end recovers most cross-modality transfer — a deployable, learning-light fix.
- **Why Important:** Teledermatology is a high-volume, access-critical application blocked precisely on this gap.
- **Why Possibly Novel:** Dermoscopy-vs-photo differences are acknowledged clinically; the paired factor decomposition for dense-model transfer is unrun.
- **Minimal Experiment:** On paired lesion captures, apply factor-wise transforms; measure per-factor transfer recovery for a fixed segmenter. Falsified if the gap resists factorization.
- **Main Risk:** Paired data volume is modest; factor simulations approximate reality imperfectly.
- **Cluster:** CrossDom

### B-0322
- **One-sentence idea:** Exploit patient-paired multi-modal datasets (fundus + OCT of the same eyes) for supervised cross-modal representation alignment, enabling label transfer between modalities without any target-modality annotation.
- **Problem:** Fundus photography has abundant labels; OCT (and OCT-A) label coverage is thin; the same patients routinely receive both exams, creating natural cross-modal pairs — but this pairing is used for diagnosis fusion, not for transferring dense supervision between modalities, leaving a supervised alignment channel unexploited.
- **Core Hypothesis:** Patient-paired alignment (training modality encoders so paired exams map to consistent anatomical latents, using vessel/disc structure as anchors) enables fundus-label-supervised training of OCT-projection segmenters at useful accuracy with zero OCT annotations, with quality tracking the anatomical overlap of the modality pair.
- **Why Important:** A template for the many paired-modality situations in medicine (mammography/tomosynthesis, CT/PET) where one modality's labels could bootstrap the other's.
- **Why Possibly Novel:** Cross-modal medical alignment exists for registration/fusion; patient-pairing as a dense label-transfer mechanism with zero-target-annotation evaluation is underexplored.
- **Minimal Experiment:** On public paired fundus/OCT data, train paired alignment; evaluate zero-annotation transfer of vessel/lesion segmentation against small supervised OCT baselines. Falsified if pairing adds nothing over unpaired alignment.
- **Main Risk:** Geometric correspondence between modalities is partial (2D fundus vs. 3D OCT), bounding transferable structures.
- **Cluster:** CrossDom

### B-0323
- **One-sentence idea:** Factorial sim-to-real for surgical scenes: determine which simulator deficiencies (specular wetness, tissue deformation, smoke/irrigation, texture realism) actually block simulator-trained surgical segmentation.
- **Problem:** Surgical video annotation is severely restricted (privacy, expertise), making simulators the natural training source — but surgical simulators fail sim-to-real badly, upgrade priorities are set by visual intuition, and the deficiency-impact ranking (what to fix first: wet specularity? deformation? instruments?) has never been measured.
- **Core Hypothesis:** A factorial fidelity study (toggling specular rendering, deformation physics, particulate effects, texture source) will show sim-to-real transfer for instrument-and-anatomy segmentation is dominated by one or two factors (predicted: specular/wetness rendering), enabling an evidence-ranked simulator-improvement roadmap that gets most of real-data performance at a fraction of maximal-fidelity cost.
- **Why Important:** Surgical autonomy and analytics are data-blocked; making simulators sufficient is the only scalable unblocking, and it needs a priority list.
- **Why Possibly Novel:** Sim-to-real fidelity ablations exist for driving (B-0071 does smoke); the surgical instantiation with its unique factors is unrun.
- **Minimal Experiment:** Factorial rendering configurations in an open surgical simulator; fixed downstream model; evaluate all on real annotated laparoscopy. Falsified if transfer is factor-insensitive.
- **Main Risk:** Factor interactions; real-data evaluation sets are small (use multiple).
- **Cluster:** CrossDom

### B-0324
- **One-sentence idea:** Stepwise transfer through constructed intermediate domains: test when a bridging-domain curriculum (photo→edge-map→sketch) beats direct fine-tuning across large gaps, and how to choose the path.
- **Problem:** Direct fine-tuning across extreme gaps loses source knowledge before target competence forms (catastrophic transition); intermediate domains could smooth the path, but bridging is applied anecdotally with no evidence on when it beats direct transfer or how to construct/select bridges — the "domain geodesic" question is unformalized for dense tasks.
- **Core Hypothesis:** Bridged transfer beats direct transfer only above a measurable gap threshold (below it, bridges waste budget), synthetic bridges (style/physics interpolations per B-0229) work as well as natural ones, and the optimal number of steps grows slowly (2–3 suffices) — a complete usage rule for the technique.
- **Why Important:** Gives practitioners a decision rule for a technique currently applied by faith, and connects to generative bridging (B-0229) as the bridge factory.
- **Why Possibly Novel:** Intermediate-domain ideas float in curriculum and UDA literature; the threshold law and bridge-construction comparison for dense tasks are unmeasured.
- **Minimal Experiment:** Transfer across 4 pairs of graded gap sizes, direct vs. 1/2/3-step bridges (synthetic and natural); locate the threshold. Falsified if direct transfer always matches bridging.
- **Main Risk:** Bridge quality confounds step-count effects (control bridge construction method).
- **Cluster:** CrossDom

### B-0325
- **One-sentence idea:** Map where domain gaps live in frequency space across many domain pairs, and use each pair's band-signature as a transfer diagnostic that selects the appropriate adaptation method.
- **Problem:** Different domain pairs have gaps in different spatial-frequency bands (sensor noise: high; illumination/style: low; structural content: mid), and adaptation methods implicitly specialize by band (style transfer fixes low, denoising-like methods high) — but no diagnostic measures a pair's band-signature, so method choice ignores the gap's actual location.
- **Core Hypothesis:** Band-wise gap analysis (transfer performance after swapping/matching individual frequency bands between domains) yields stable signatures per pair, signatures cluster into a small taxonomy, and signature-matched method selection outperforms any single method applied uniformly across pairs — adaptation prescribed by measurement.
- **Why Important:** A cheap pre-adaptation diagnostic that routes to the right method family would raise the floor of every cross-domain project.
- **Why Possibly Novel:** Frequency analyses exist for single methods (B-0097) and FMs (B-0042); the cross-pair signature taxonomy with method routing is the new layer.
- **Minimal Experiment:** Compute band signatures for 15 domain pairs; cluster; validate routing on held-out pairs against uniform method application. Falsified if signatures don't predict method effectiveness.
- **Main Risk:** Band swapping introduces artifacts that contaminate the measurement (use soft band interpolation).
- **Cluster:** CrossDom

### B-0326
- **One-sentence idea:** Derive the freeze-depth law for cross-domain fine-tuning: how many backbone layers to unfreeze as a function of measured domain distance and target data size, validated as a practitioner's rule.
- **Problem:** The freeze/unfreeze decision is made per project by trial and error; intuitions exist (more distance → unfreeze deeper) but no quantitative rule has been fit and validated for dense prediction, so every team re-runs the same expensive sweep or defaults to full fine-tuning with overfitting risk at small data.
- **Core Hypothesis:** Optimal unfreezing depth is a smooth, learnable function of (domain distance per B-0313, target data size), the fitted rule transfers across backbone families with a calibration constant, and following it recovers ≥95% of oracle-sweep performance at one training run instead of many.
- **Why Important:** One of the most-made decisions in applied transfer learning, currently made blind; even approximate rules save community-scale compute.
- **Why Possibly Novel:** Freeze-depth folklore is ubiquitous; the fitted, validated, distance-indexed law for dense tasks is unpublished.
- **Minimal Experiment:** Sweep freeze depths across (distance × data-size) grid on 6 transfer pairs; fit the rule; validate on 3 held-out pairs. Falsified if optimal depth is unpredictable.
- **Main Risk:** Interaction with adapter-style alternatives (report against PEFT baselines per B-0038).
- **Cluster:** CrossDom

### B-0327
- **One-sentence idea:** Audit "universal" segmentation models on verifiably held-out domains and publish domain-coverage cartography: where universality claims actually hold.
- **Problem:** Models marketed as universal segmenters are evaluated on benchmark collections overlapping their training distributions; their behavior on genuinely unrepresented domains (industrial radiography, microscopy variants, artistic imagery) is unknown, and users deploy them on the strength of universality claims no evaluation supports.
- **Core Hypothesis:** Universal models' performance stratifies sharply by proximity to training-domain clusters (measurable via B-0313 distances), with cliff-like degradation beyond coverage — and a published coverage map (performance as a function of domain-space position) predicts per-domain reliability better than any aggregate benchmark score.
- **Why Important:** Converts universality from marketing into a measurable, falsifiable, user-actionable property.
- **Why Possibly Novel:** Individual OOD evaluations exist; systematic domain-space cartography of universal segmenters with predictive coverage maps is unbuilt.
- **Minimal Experiment:** Evaluate 3 universal models on 20 domains spanning measured distances from their training clusters; fit coverage maps; validate predictions on 5 more domains. Pure evaluation. Falsified if performance is distance-flat (true universality).
- **Main Risk:** Training-distribution details of closed models are opaque (estimate proximity via behavioral probes).
- **Cluster:** CrossDom

### B-0328
- **One-sentence idea:** Fit the annotation-versus-distance law for porting: the minimum target annotation needed to close a cross-domain gap as a function of measured domain distance — pricing every port in labels.
- **Problem:** Porting a model to a new domain always ends with "annotate some target data," but how much is never predictable; the relationship between domain distance and required annotation has not been fit, so porting budgets oscillate between wasteful over-annotation and failed under-annotation.
- **Core Hypothesis:** Required annotation (to reach a target accuracy) grows predictably with domain distance with method-dependent slopes (better adaptation methods flatten the curve), the law transfers across task types after normalization, and it enables the first quantitative cost comparison between adaptation research and annotation spending — how many labels each method is "worth."
- **Why Important:** Expresses adaptation methods' value in the universal currency (labels), rationalizing both research priorities and project budgets; completes B-0313's oracle with a cost axis.
- **Why Possibly Novel:** Label-budget curves exist in-domain; the distance-indexed porting law with method-worth accounting is unassembled.
- **Minimal Experiment:** For 8 transfer pairs at measured distances, sweep target annotation with 2 adaptation methods + plain fine-tuning; fit and validate the law. Falsified if annotation requirements are distance-independent.
- **Main Risk:** Target-accuracy choice affects the law's shape (report at multiple thresholds).
- **Cluster:** CrossDom

### B-0329
- **One-sentence idea:** Quantify the cost of shared normalization statistics in multi-domain training and establish when domain-conditional normalization is necessary versus wasteful.
- **Problem:** Multi-domain segmentation training usually shares normalization layers whose statistics average incompatible domain distributions (CT intensities vs. photograph statistics), silently degrading all domains; domain-specific normalization fixes it but fragments the model and fails on unseen domains — and the decision has no quantitative criterion.
- **Core Hypothesis:** The shared-norm penalty grows with a measurable inter-domain feature-statistics divergence, becomes negligible below a threshold (making conditional norms wasteful there), and at high divergence a hybrid (shared affine, domain-conditional statistics with an unseen-domain fallback estimator) captures the benefits of both — a complete normalization policy for multi-domain training.
- **Why Important:** Normalization design is in every multi-domain system; a validated criterion ends a recurring architecture debate (training-time complement to B-0093's test-time analysis).
- **Why Possibly Novel:** Domain-specific BN exists as a trick; the divergence-threshold criterion and the unseen-domain fallback design are unmeasured.
- **Minimal Experiment:** Train shared/conditional/hybrid normalization across domain sets of graded divergence; locate the threshold; test unseen-domain behavior. Falsified if shared norms are always fine or always bad.
- **Main Risk:** Threshold may depend on normalization type (BN/LN/GN — test all three).
- **Cluster:** CrossDom

### B-0330
- **One-sentence idea:** Test whether robustness transfers independently of accuracy: does corruption/adversarial tolerance acquired in a source domain survive fine-tuning into a target domain, or must robustness be re-trained per domain?
- **Problem:** Robustness is expensive (adversarial training, corruption augmentation) and is currently re-established per domain from scratch; whether robustness is a transferable representation property (surviving fine-tuning like accuracy does) or a fragile decision-boundary property (destroyed by any fine-tuning) is a basic unknown that determines where robustness investment belongs in the pipeline.
- **Core Hypothesis:** Corruption robustness transfers substantially through fine-tuning (it lives in feature-level invariances), while adversarial robustness largely does not (it lives in decision-boundary geometry the fine-tuning rewrites) — a dissociation (parallel to B-0165's) that dictates robustness training placement: corruption robustness at pretraining, adversarial robustness per deployment.
- **Why Important:** Robustness budgeting across the transfer pipeline is currently uninformed; the dissociation would set the policy.
- **Why Possibly Novel:** Robustness transfer through fine-tuning is scarcely measured for dense prediction; the mechanism-level dissociation claim is untested.
- **Minimal Experiment:** Robustify source models both ways; fine-tune into 3 target domains; measure retained robustness of each type vs. per-domain re-training. Falsified if both types transfer equally (or neither transfers).
- **Main Risk:** Robustness metrics across domains need careful severity matching.
- **Cluster:** CrossDom
## Section 12 — Multimodal Supervision for Dense Prediction [B-0331–B-0360]

### B-0331
- **One-sentence idea:** Mine negations from radiology reports ("no pneumothorax", "unremarkable liver") into certified-negative spatial supervision — the report's most reliable content, currently discarded.
- **Problem:** Report-supervised learning focuses on positive findings, but positive mentions are noisy (hedged, mislocalized) while negations are the report's most trustworthy statements; nobody converts "no X" into the spatial statement it implies (the atlas region of X is X-free), wasting the cleanest supervision channel reports offer.
- **Core Hypothesis:** Negation-derived negative supervision (parsed negations → atlas-grounded negative regions) measurably reduces false positives of report-supervised dense models — with the gain concentrated in exactly the finding classes most often negated — and negation supervision is complementary to positive-mention supervision, not redundant with it.
- **Why Important:** False positives are the deployment killer for screening; a free, high-precision negative-label stream at archive scale directly attacks them.
- **Why Possibly Novel:** Negation detection exists in clinical NLP; its systematic conversion to spatial negative supervision for dense training is essentially unexploited.
- **Minimal Experiment:** Parse negations from a public report corpus; add atlas-grounded negative losses to a report-supervised baseline; measure FP changes per finding class. Falsified if negatives add nothing over positives alone.
- **Main Risk:** Atlas grounding errors turn good negations into wrong negative labels (bound with conservative region margins).
- **Cluster:** MultiSup

### B-0332
- **One-sentence idea:** Use size measurements quoted in reports ("2.3 cm nodule") as metric supervision: the predicted lesion's differentiable diameter must match the reported number.
- **Problem:** Reports contain millions of quantitative size statements tied to findings, but weak-supervision pipelines reduce reports to class labels or coarse locations; the numbers — which directly constrain the mask geometry that segmentation must produce — are thrown away because no training formulation consumes them.
- **Core Hypothesis:** A differentiable size-extraction head (predicted mask → longest-axis diameter) supervised by report measurements trains lesion segmenters with substantially better size fidelity than mention-only supervision, and combined with even 5% full masks, closes much of the gap to fully supervised training — because size constrains the solution space more than any class label.
- **Why Important:** Size is the clinically consumed output (RECIST staging); supervision aligned to it is both abundant and maximally relevant.
- **Why Possibly Novel:** Report-mining stops at categories/locations; the quantitative-measurement-as-loss formulation appears untested at scale.
- **Minimal Experiment:** On a dataset with reports and hidden masks, train mention-only vs. mention+size supervision; compare size error and Dice. Falsified if size terms don't improve geometry.
- **Main Risk:** Report measurements have their own error/rounding conventions; matching measured lesion to predicted instance is nontrivial in multi-lesion cases.
- **Cluster:** MultiSup

### B-0333
- **One-sentence idea:** Ground anatomical location phrases ("left lower lobe", "segment VII") into atlas-defined spatial priors as coarse but abundant localization supervision for dense models.
- **Problem:** Nearly every reported finding carries an anatomical locator that maps deterministically onto atlas regions, yet report supervision typically treats location words as classification tokens rather than as the spatial constraints they are — leaving archive-scale coarse localization unused.
- **Core Hypothesis:** Locator-phrase grounding (parse → atlas region → "finding lies within region" constraint) provides supervision worth a quantifiable fraction of point annotations (per B-0134's frontier), stacks additively with negation (B-0331) and size (B-0332) channels, and its value scales with locator granularity (segment-level ≫ organ-level) — an accounting that tells health systems what report detail is worth.
- **Why Important:** Establishes the exchange rate between routine reporting language and annotation, potentially redirecting how radiologists are asked to phrase reports.
- **Why Possibly Novel:** Location phrases feed retrieval and classification work; their atlas-constrained dense-supervision value has not been measured or stacked with other report channels.
- **Minimal Experiment:** Train with locator constraints at two granularities on a report+mask dataset; place on the annotation-equivalent scale; test channel additivity. Falsified if locators add nothing at any granularity.
- **Main Risk:** Atlas registration errors on abnormal anatomy (exactly where findings are) weaken constraints.
- **Cluster:** MultiSup

### B-0334
- **One-sentence idea:** Convert report hedging language ("possibly", "cannot exclude", "likely") into calibrated uncertainty labels, training segmentation models whose confidence mirrors the radiologist's expressed certainty.
- **Problem:** Weak supervision treats every mentioned finding as equally true, but radiologists systematically encode confidence in hedging vocabulary; ignoring it means training on "cannot exclude a nodule" as if it were "definite nodule" — injecting graded uncertainty as label noise instead of using it as the calibration signal it is.
- **Core Hypothesis:** Hedge-weighted supervision (mention certainty parsed to a probability scale validated against radiologist surveys) produces models with markedly better-calibrated finding probabilities than binary-mention training at equal detection accuracy, and the learned probability scale recovers the field's implicit hedging-to-probability mapping — a clinically interpretable by-product.
- **Why Important:** Calibrated confidence is what triage and prioritization systems consume; hedges are the only archive-scale uncertainty labels in existence.
- **Why Possibly Novel:** Hedge detection exists in clinical NLP; its use as a training-time calibration target for dense/detection models is essentially unstudied.
- **Minimal Experiment:** Map hedge terms to probabilities via a small reader survey; train hedge-weighted vs. binary on a report-supervised task; compare calibration on expert-adjudicated test cases. Falsified if hedging carries no calibration signal.
- **Main Risk:** Hedging conventions vary across radiologists/institutions (model reader effects per B-0262's philosophy).
- **Cluster:** MultiSup

### B-0335
- **One-sentence idea:** Mine temporal comparison statements ("increased from prior", "stable") into ordinal longitudinal supervision linking study pairs — training change-aware segmentation without any change masks.
- **Problem:** Longitudinal change is the highest-value clinical quantity (B-0013), but change masks are essentially never annotated; meanwhile reports explicitly state the change direction for millions of study pairs, a paired ordinal label stream that no segmentation training formulation currently consumes.
- **Core Hypothesis:** Ordinal change supervision (predicted volumes across the pair must order consistently with the report's comparative statement) trains models with substantially lower longitudinal noise (per B-0014's metrics) and better change-direction accuracy than independently trained per-study models — because the ordinal constraint suppresses exactly the inter-study measurement noise that plagues pipelines.
- **Why Important:** Unlocks archive-scale longitudinal supervision for the task clinical oncology actually cares about.
- **Why Possibly Novel:** Comparative-statement parsing exists in NLP; its conversion to paired ordinal training constraints for dense prediction is unexploited.
- **Minimal Experiment:** Parse comparatives from a longitudinal corpus; add pairwise ordinal loss; evaluate change-direction accuracy against radiologist-adjudicated pairs. Falsified if ordinal constraints don't reduce longitudinal noise.
- **Main Risk:** Comparatives sometimes reference different lesions than the model tracks (instance-matching ambiguity).
- **Cluster:** MultiSup

### B-0336
- **One-sentence idea:** Measure and de-bias template leakage in report-supervised models: models shortcut on institutional boilerplate ("PORTABLE study; lines and tubes...") instead of learning image-grounded semantics.
- **Problem:** Reports contain massive institution-specific templating correlated with acquisition context and case-mix; contrastively trained image-text models can satisfy their objective by matching template style to scanner appearance — a shortcut producing inflated within-institution results and collapse across institutions, undiagnosed because evaluations stay in-distribution.
- **Core Hypothesis:** A template-signal audit (training text-only classifiers to predict institution/scanner from reports; measuring image-text alignment attributable to boilerplate) will reveal substantial shortcut capacity, cross-institution transfer of report-supervised dense models will track boilerplate divergence, and template-ablated training (style-normalized or finding-extracted text) will improve cross-institution transfer at slight in-domain cost.
- **Why Important:** Report supervision is the foundation of medical VLMs; a documented shortcut at its core affects everything downstream.
- **Why Possibly Novel:** Shortcut learning is studied for images; the report-text-side shortcut in multimodal medical training is unquantified.
- **Minimal Experiment:** Run the audit on a public report corpus; train with raw vs. finding-extracted text; compare cross-institution dense probes. Falsified if boilerplate carries no alignment signal.
- **Main Risk:** Finding extraction may discard genuinely useful context along with boilerplate.
- **Cluster:** MultiSup

### B-0337
- **One-sentence idea:** Word-region alignment via optimal transport for report-supervised dense training, with phrase grounding as the audited intermediate rather than an emergent hope.
- **Problem:** Image-report contrastive training aligns global embeddings and hopes region-word correspondence emerges; it emerges poorly (findings are small, reports mention many things), and because grounding is never measured as an intermediate objective, failures are invisible until downstream — the alignment mechanism is an unaudited black box.
- **Core Hypothesis:** Explicit OT-based alignment between report phrases and image regions (with anatomical priors per B-0333 as transport costs) yields measurably better phrase grounding, and grounding quality is the mediating variable for downstream dense performance — establishable by showing downstream gains are predicted by grounding gains across training variants.
- **Why Important:** Identifies and instruments the causal bottleneck inside the field's dominant medical pretraining recipe.
- **Why Possibly Novel:** OT alignment appears in vision-language research; the mediation analysis (grounding as the measured causal intermediate) for medical dense tasks is missing.
- **Minimal Experiment:** Train contrastive vs. OT-aligned variants; measure phrase grounding (on a grounded subset) and downstream segmentation; test mediation. Falsified if downstream gains don't track grounding.
- **Main Risk:** Grounded evaluation subsets are small; OT costs need anatomical priors to avoid degenerate couplings.
- **Cluster:** MultiSup

### B-0338
- **One-sentence idea:** Extract lesion counts from reports ("three hepatic metastases") as instance-count constraints for multi-lesion segmentation training.
- **Problem:** Counting statements are among the most concrete report contents and directly constrain instance structure, yet weak supervision collapses them into presence labels; count-constrained dense training (the natural companion to B-0190's click counts) has no text-supervised formulation despite archive-scale availability.
- **Core Hypothesis:** A differentiable counting head (predicted instances → expected count) supervised by parsed report counts improves lesion-level F1 (per B-0024's metric) over presence-only supervision, with the gain largest in the 2–5 lesion range where counts are most reliably reported and models most often merge/split incorrectly.
- **Why Important:** Lesion counts drive staging; count supervision targets the instance-structure errors that voxel losses ignore.
- **Why Possibly Novel:** Count supervision exists for crowd counting from point labels; report-count-derived constraints for medical instance segmentation are untested.
- **Minimal Experiment:** Parse counts from reports of a lesion dataset; add count loss; evaluate lesion F1 stratified by count. Falsified if counts don't improve instance structure.
- **Main Risk:** Reports count what radiologists deem reportable (size thresholds), a systematic bias needing a threshold model.
- **Cluster:** MultiSup

### B-0339
- **One-sentence idea:** Diagnose exactly why CLIP-style patch tokens are poor at dense tasks — training-objective-induced global pooling artifacts versus data-induced deficits — and repair them by dense-alignment self-distillation with the diagnosis as the guide.
- **Problem:** Contrastive VLM features power open-vocabulary segmentation, but their patch tokens are known to be spatially messy (attention sinks, global-information smearing); fixes are proposed ad hoc without establishing which pathology (objective, architecture, or data) causes which spatial artifact — so remedies are trial-and-error.
- **Core Hypothesis:** A causal decomposition (retraining small VLMs with objective/architecture/data factors varied) will attribute specific spatial artifacts to specific causes (predicted: global-pooling objective causes token-smearing; register-free architecture causes sink tokens), and cause-matched repairs will each fix their artifact — a mechanistic account replacing the current patch-fix folklore.
- **Why Important:** All open-vocabulary dense prediction inherits these tokens; a mechanistic understanding upgrades every downstream system.
- **Why Possibly Novel:** Patch-token pathologies are documented descriptively; the factorial causal attribution with matched repairs is unrun.
- **Minimal Experiment:** Train small contrastive VLMs varying the factors; measure artifact signatures; apply matched repairs; verify artifact-specific fixes. Falsified if artifacts don't attribute to factors.
- **Main Risk:** Small-scale VLM findings may not extrapolate to production-scale models (validate signatures on public large models).
- **Cluster:** MultiSup

### B-0340
- **One-sentence idea:** Exploit depth-boundary coincidence as free supervision: depth discontinuities from RGB-D or stereo mark object boundaries, refining segmentation boundaries without any mask labels.
- **Problem:** Object boundaries are the most expensive annotation content and the weakest part of weakly supervised segmentation; depth sensors deliver boundary evidence (occlusion discontinuities) for free at capture time, but this channel is used as an input feature rather than as a supervision signal for RGB-only models — conflating deployment sensing with training supervision.
- **Core Hypothesis:** Depth-discontinuity supervision (boundary-alignment losses only where depth edges are reliable) sharpens weakly supervised RGB segmentation boundaries substantially, the improvement survives deploying without depth (supervision-only usage), and failure regions (depth-smooth semantic boundaries: pictures on walls, road markings) are identifiable and maskable in advance.
- **Why Important:** Free boundary supervision at capture time attacks weak supervision's characteristic weakness (per B-0128's decomposition, delineation) with zero annotation.
- **Why Possibly Novel:** Depth as input is standard; depth as training-only boundary supervision with reliability gating and RGB-only deployment is a distinct, cheaply testable framing.
- **Minimal Experiment:** Add gated depth-edge losses to a weakly supervised baseline on an RGB-D dataset; evaluate RGB-only inference boundary metrics. Falsified if depth edges don't transfer to RGB-only boundaries.
- **Main Risk:** Depth edges mark occlusions, not semantic boundaries — the divergence cases need the gating to work.
- **Cluster:** MultiSup

### B-0341
- **One-sentence idea:** Alignment-robust cross-modal distillation: characterize how much spatial misregistration between teacher modality (thermal/depth) and student modality (RGB) distillation can tolerate, and design losses that degrade gracefully.
- **Problem:** Cross-modal distillation (B-0077, B-0340) assumes co-registered modalities, but real rigs have parallax, rolling-shutter offsets, and calibration drift; per-pixel distillation losses turn small misregistration into systematic supervision error, and the tolerance envelope — the engineering number every rig designer needs — has never been measured.
- **Core Hypothesis:** Standard per-pixel distillation degrades sharply beyond a few pixels of misregistration while correlation-window and distribution-level losses tolerate an order of magnitude more at modest peak cost, and the optimal loss choice is predictable from the rig's measured registration error — a design chart for cross-modal supervision systems.
- **Why Important:** Determines whether cheap uncalibrated capture rigs can produce useful cross-modal supervision — a gating question for scaling this supervision family.
- **Why Possibly Novel:** Distillation losses are compared on aligned data; the misregistration-tolerance characterization is unstudied.
- **Minimal Experiment:** Inject controlled misregistration into an aligned RGB+thermal dataset; sweep loss families; map the tolerance envelope. Falsified if all losses degrade identically.
- **Main Risk:** Synthetic misregistration may miss real error structure (validate on one genuinely uncalibrated rig).
- **Cluster:** MultiSup

### B-0342
- **One-sentence idea:** Establish the modality-dropout curriculum: how the schedule of missing-modality simulation during training (constant rate, annealed, blockwise) shapes robustness to missing inputs at deployment.
- **Problem:** Multimodal dense models train with modality dropout to survive missing inputs (B-0029), but the dropout schedule is an unexamined hyperparameter: constant-rate dropout may prevent deep fusion from forming, while late dropout may be too little — the schedule-robustness relationship is unmapped though every multimodal system needs it.
- **Core Hypothesis:** Schedule shape has large, systematic effects: full-modality warmup followed by annealed dropout yields both better full-modality peaks and better missing-modality floors than constant-rate dropout (fusion must form before being stressed), and the optimal anneal point is detectable from fusion-layer diagnostics — a recipe replacing the current arbitrary constants.
- **Why Important:** A free (schedule-only) improvement to every multimodal dense system, plus mechanistic insight into fusion formation.
- **Why Possibly Novel:** Modality dropout is universal, its curriculum unstudied; the fusion-formation mechanism claim makes it science rather than tuning.
- **Minimal Experiment:** Schedule grid on one multimodal segmentation task; evaluate all modality subsets; probe fusion layers across training. Falsified if schedules are equivalent.
- **Main Risk:** Optimal schedules may vary with modality count/redundancy (test two modality sets).
- **Cluster:** MultiSup

### B-0343
- **One-sentence idea:** Surgeon commentary as supervision: align intraoperative speech ("now dividing the cystic duct") with surgical video to weakly supervise instrument and anatomy segmentation.
- **Problem:** Surgical video annotation requires surgeon time (the scarcest annotation resource in existence), while teaching hospitals record thousands of narrated procedures whose speech names exactly the structures and actions on screen with rough temporal alignment — a supervision stream currently used only for workflow classification, never for dense prediction.
- **Core Hypothesis:** Speech-video alignment (utterance time → frame window; named entities → weakly localized masks via class-agnostic proposals) yields dense supervision sufficient to train usable anatomy/instrument segmenters with zero manual masks, with quality tracking narration density — and combined with tiny mask sets, matching much larger fully supervised baselines.
- **Why Important:** Unlocks the only annotation source (expert narration) that scales with surgical volume rather than against it.
- **Why Possibly Novel:** Narrated-video learning exists for instructional web video; the surgical instantiation with anatomical entity grounding and safety-relevant evaluation is essentially open.
- **Minimal Experiment:** Use public narrated surgical datasets (or lecture recordings); build the alignment pipeline; evaluate against annotated benchmarks. Falsified if narration alignment is too coarse for dense supervision.
- **Main Risk:** Narration is sparse and anticipatory/retrospective (speech precedes or follows the visible act) — temporal offset modeling required.
- **Cluster:** MultiSup

### B-0344
- **One-sentence idea:** Mine historical radiotherapy dose maps and plans as free dense supervision: clinically approved dose distributions encode organ-at-risk and target geometry with life-critical precision.
- **Problem:** Radiotherapy archives hold decades of treatment plans in which dose gradients were shaped around exactly the anatomical boundaries segmentation models need — each plan is a physician-approved dense annotation surrogate — but this archive is only mined for dose prediction, never inverted into segmentation supervision.
- **Core Hypothesis:** Inverting plans (steep dose gradients + plan constraints → organ boundary evidence; prescription regions → target evidence) yields supervision that trains OAR segmentation to within a small gap of contour-supervised models, effectively converting every archived plan into a validated annotation — with plan-era and protocol effects quantifiable as noise terms.
- **Why Important:** Radiotherapy structures are among the most expensive annotations in medicine; their historical archive is enormous and (unlike contours) always clinically validated by physicists and physicians.
- **Why Possibly Novel:** Dose prediction from contours is a whole field; the inverse direction (plans as segmentation supervision) appears essentially unexplored.
- **Minimal Experiment:** On public plan+contour datasets, derive boundary evidence from dose maps alone; train and compare against contour supervision. Falsified if dose gradients under-determine anatomy.
- **Main Risk:** Dose shaping reflects planning trade-offs, not pure anatomy (margins, sparing priorities) — requires a plan-convention model.
- **Cluster:** MultiSup

### B-0345
- **One-sentence idea:** Use PET uptake (SUV maps) as soft supervision for CT tumor segmentation in paired PET/CT — metabolic evidence teaching anatomical delineation.
- **Problem:** CT tumor boundaries are ambiguous (soft-tissue contrast limits) while co-acquired PET provides functional tumor evidence at coarse resolution; PET is used as an input channel at inference, but many deployments have CT only — the paired-acquisition archive as a training-only supervision source for CT-only models is underexploited.
- **Core Hypothesis:** SUV-weighted training targets (calibrated from PET with resolution and uptake-specificity modeling) train CT-only segmenters that outperform CT-mask-supervised models of equal annotation budget — because PET resolves precisely the ambiguous-boundary cases where human CT annotation is worst — with the gain concentrated in low-contrast tumor interfaces.
- **Why Important:** Converts every archived PET/CT into a boundary-teaching example for the CT-only models most of the world runs.
- **Why Possibly Novel:** PET/CT fusion at inference is standard; PET-as-training-only-supervision with uptake-calibration modeling and CT-only deployment evaluation is a distinct unexplored channel (the medical sibling of B-0077).
- **Minimal Experiment:** On public PET/CT tumor data, train CT-only models with mask vs. SUV-derived supervision at matched budgets; stratify by boundary contrast. Falsified if SUV supervision trails masks everywhere.
- **Main Risk:** Uptake is not coextensive with tumor (necrotic cores, inflammation) — the calibration model carries the burden.
- **Cluster:** MultiSup

### B-0346
- **One-sentence idea:** Quantify how LLM parsing errors propagate into dense supervision: the noise budget of the increasingly universal reports-to-structured-tuples-to-labels pipeline.
- **Problem:** Everyone now parses free-text reports with LLMs into (finding, location, size, certainty) tuples for supervision (feeding B-0331–B-0338 style channels), but LLM extraction has structured error modes (hallucinated findings, wrong laterality, unit confusion); how much parsing noise the downstream dense training tolerates — and which error types are fatal versus benign — is unmeasured, so pipeline QC has no target.
- **Core Hypothesis:** Downstream dense-model quality degrades with parsing error non-uniformly by error type (laterality flips are fatal, size rounding benign), the tolerance thresholds are measurable via controlled error injection, and targeted verification of the fatal error types only (cheap human QC on a small fraction) restores near-clean performance — a costed QC policy for the whole report-supervision family.
- **Why Important:** The reports-to-labels pipeline is becoming infrastructure; its error propagation must be characterized before the field builds on sand.
- **Why Possibly Novel:** LLM extraction accuracy is benchmarked intrinsically; the downstream propagation study with type-stratified tolerance is missing.
- **Minimal Experiment:** Inject typed parsing errors at controlled rates into a clean parsed corpus; train dense models per condition; map type-tolerance curves. Falsified if all error types degrade equally.
- **Main Risk:** Real LLM errors correlate with report difficulty (validate injection realism against measured LLM error distributions).
- **Cluster:** MultiSup

### B-0347
- **One-sentence idea:** Build an instruction-following benchmark for dense medical prediction: do "segment anything you describe" models actually execute clinical instructions (modifiers, exclusions, conditionals), or only class names?
- **Problem:** Instruction-tuned segmentation models are evaluated on simple referring expressions; clinical instructions are compositional ("segment the enhancing tumor excluding necrosis, only in the left lobe") and the models' compliance with modifiers, negations, and conditionals is unmeasured — capability claims outrun evaluation exactly where errors are consequential.
- **Core Hypothesis:** Current instruction-tuned dense models satisfy the head noun and ignore modifiers at high rates (measurable by modifier-controlled instruction pairs whose correct outputs differ), failure is systematic by construction type (negation worst, per B-0331's theme), and modifier-supervised fine-tuning on programmatically generated instruction-mask pairs closes most of the gap — a capability audit plus the training recipe it implies.
- **Why Important:** Instruction interfaces are the deployment path for clinical dense AI; silent modifier-dropping is a safety defect that standard metrics cannot see.
- **Why Possibly Novel:** Instruction-following audits exist for LLMs; the dense-prediction compositional-compliance benchmark is unbuilt.
- **Minimal Experiment:** Generate modifier-controlled instruction pairs from richly annotated data; measure output divergence and correctness for 4 public models. Falsified if models already comply with modifiers.
- **Main Risk:** Programmatic instruction generation may not match clinical phrasing (validate with clinician-written instructions).
- **Cluster:** MultiSup

### B-0348
- **One-sentence idea:** Condition lesion segmentation on patient covariates (labs, demographics, history) as prior-shifting context — and rigorously separate legitimate prior use from harmful shortcut dependence.
- **Problem:** Radiologists read images with the chart open (a PSA level changes what a prostate reader expects), while models read blind; naive covariate conditioning risks shortcut learning (predicting findings from labs regardless of pixels), and the field lacks a framework for capturing the prior benefit while bounding the shortcut harm — so covariates stay unused.
- **Core Hypothesis:** Covariate conditioning improves lesion detection/segmentation in genuinely ambiguous cases (measurable on reader-disagreement subsets), the shortcut component is isolable via covariate-permutation testing (performance on covariate-swapped cases must not degrade beyond the prior's legitimate contribution), and a shortcut-penalized training scheme retains most benefit with bounded covariate reliance — a template for safe context use in dense prediction.
- **Why Important:** Context is a genuine part of expert reading; making it usable safely is both a performance and a safety contribution.
- **Why Possibly Novel:** Multimodal fusion with tabular data exists for classification; the shortcut-bounded framework for dense prediction with permutation-based auditing is unformulated.
- **Minimal Experiment:** Train ± covariates on a dataset with labs; evaluate on ambiguity-stratified and covariate-permuted test sets. Falsified if benefits exist only via shortcuts.
- **Main Risk:** Covariate-outcome correlations in retrospective data may be irreducibly confounded (choose covariates with known mechanistic relevance).
- **Cluster:** MultiSup

### B-0349
- **One-sentence idea:** A principled fusion framework for multiple weak supervision modalities (gaze, report text, clicks, dose maps) with unknown, correlated error structures — measuring complementarity instead of assuming it.
- **Problem:** Weak supervision channels are studied one at a time (B-0187, B-0331–B-0345); real archives offer several simultaneously, but naive loss-summing assumes independent errors, while the channels plausibly share failure modes (all derived from the same reading session) — the fusion problem, including estimating inter-channel error correlation without ground truth, is unsolved.
- **Core Hypothesis:** Inter-channel error correlation is estimable from agreement statistics on unlabeled data (extending B-0268's gold-free machinery across modalities), correlation-aware fusion weights beat naive summing measurably, and measured channel complementarity predicts fusion gains — so channel-portfolio decisions (which supervision streams to engineer next) become quantitative.
- **Why Important:** The archive-supervision program (this section's theme) succeeds or fails on principled fusion; complementarity accounting also prioritizes future channel engineering.
- **Why Possibly Novel:** Multi-source weak supervision theory exists for classification (labeling-function frameworks); the dense-prediction version with spatial error correlation is unbuilt.
- **Minimal Experiment:** On a dataset with 3 derivable channels + hidden masks, estimate error correlations gold-free; compare fusion schemes; validate the complementarity predictor. Falsified if naive summing is unbeatable.
- **Main Risk:** Spatial error correlation estimation may need more channel overlap than archives provide.
- **Cluster:** MultiSup

### B-0350
- **One-sentence idea:** Audit suggestion-induced hallucination in text-conditioned medical segmentation: does asking for a finding make the model draw one that isn't there?
- **Problem:** Text-conditioned segmenters are deployed in query workflows ("segment the pneumothorax"); when the queried finding is absent, a model trained mostly on positive query-image pairs may hallucinate plausible masks — a leading-question vulnerability with obvious clinical harm, unmeasured because benchmarks only pose queries for present findings (the medical, workflow-critical sharpening of B-0289).
- **Core Hypothesis:** Current medical text-conditioned segmenters produce confident masks for absent queried findings at high rates, hallucination rate correlates inversely with the finding's training-set query-absent exposure, and absence-balanced training (explicit "not present" supervision from negation mining per B-0331) cuts hallucination dramatically at minor sensitivity cost — the recall-hallucination frontier as the mandatory reporting standard.
- **Why Important:** Query-driven workflows are the immediate deployment mode; leading-question hallucination is their characteristic silent failure.
- **Why Possibly Novel:** VLM hallucination is studied for captioning; the query-conditioned dense-output audit in the medical safety context is undone.
- **Minimal Experiment:** Query 3 public medical text-segmenters for verified-absent findings across a curated set; measure hallucination rates; test absence-balanced fine-tuning. Falsified if models already abstain correctly.
- **Main Risk:** Verifying absence requires careful adjudication (reuse negation-verified cases).
- **Cluster:** MultiSup

### B-0351
- **One-sentence idea:** Free-text acquisition context ("portable AP view, patient rotated, limited study") as conditioning input for dense models — the unstructured sibling of DICOM metadata conditioning.
- **Problem:** Technologist and report-header comments describe acquisition compromises that change how images should be interpreted (rotation, poor inspiration, motion), information that structured DICOM tags don't capture; models interpret compromised images as if pristine, producing errors a human reader forewarned by the comment would avoid.
- **Core Hypothesis:** Encoding acquisition free-text as conditioning (via a text encoder into prompt/FiLM channels, extending B-0008/B-0155 to unstructured text) improves dense-prediction robustness specifically on flagged-compromise studies — with correct-vs-shuffled-comment controls proving the mechanism — and the learned conditioning generalizes to unseen comment phrasings.
- **Why Important:** Compromised acquisitions are overrepresented among clinical errors; the warning text already exists in every archive.
- **Why Possibly Novel:** Structured metadata conditioning is emerging; unstructured acquisition-commentary conditioning appears untouched.
- **Minimal Experiment:** Train ± comment conditioning on a chest X-ray task with technologist comments; evaluate on flagged studies with shuffle controls. Falsified if comments carry no exploitable signal.
- **Main Risk:** Comments correlate with case difficulty (condition may just learn "be uncertain" — distinguish via calibration analysis).
- **Cluster:** MultiSup

### B-0352
- **One-sentence idea:** Sentence-to-region contrastive pretraining: align individual report sentences with image regions (instead of whole reports with whole images) and measure the dense-task value of alignment granularity.
- **Problem:** Medical image-text pretraining aligns at global granularity, but reports are sets of sentence-level statements about distinct regions; global alignment blends them, plausibly explaining weak dense transfer — yet granularity has never been isolated as the variable (models differing in granularity also differ in everything else).
- **Core Hypothesis:** At matched data and compute, sentence-region alignment (regions proposed class-agnostically, sentence-region pairs learned jointly) beats report-image alignment on dense downstream tasks by a wide margin while matching it on classification — establishing granularity as the binding variable for dense transfer and quantifying its exchange rate.
- **Why Important:** Directs the next generation of medical VLM pretraining with a controlled fact rather than architecture fashion.
- **Why Possibly Novel:** Local alignment ideas circulate; the granularity-isolated controlled comparison with dense-vs-classification dissociation is unrun.
- **Minimal Experiment:** Pretrain matched models at {report-image, sentence-image, sentence-region} granularity on one public corpus; probe dense and classification transfer. Falsified if granularity doesn't matter for dense tasks.
- **Main Risk:** Sentence-region pairing without ground truth is itself noisy (the OT machinery of B-0337 is the pairing engine).
- **Cluster:** MultiSup

### B-0353
- **One-sentence idea:** Doppler audio as vessel supervision: the audio stream of Doppler ultrasound encodes flow presence and velocity — use it as free supervision for vessel segmentation in B-mode images.
- **Problem:** Vessel annotation in ultrasound is scarce, but every Doppler exam pairs B-mode imagery with audio whose spectral content certifies flowing blood at the interrogation site; this physiological label stream is discarded at capture, and no training pipeline consumes exam audio as supervision.
- **Core Hypothesis:** Doppler-audio-derived flow labels (interrogation-gate locations with flow-positive/negative audio classification) provide point-supervision at scale sufficient to train B-mode vessel segmenters approaching point-annotation-supervised baselines — with the audio channel's error structure (angle dependence, wall filters) modeled as label noise.
- **Why Important:** Vascular ultrasound is ubiquitous and operator-dependent; automated vessel identification from B-mode alone would broaden access, and the supervision is already being generated daily.
- **Why Possibly Novel:** Audio-visual learning is a natural-video field; physiological instrument audio as dense-supervision for medical imaging appears unexplored.
- **Minimal Experiment:** Collect paired B-mode + Doppler-gate data (standard exam output); derive point labels; train and compare against manual point supervision. Falsified if audio-derived points are too sparse/noisy.
- **Main Risk:** Gate positions sample vessels sparsely and non-randomly (operators interrogate where they already see vessels).
- **Cluster:** MultiSup

### B-0354
- **One-sentence idea:** Quantify the supervision value of structured reporting: how much more dense-training signal per report does structured reporting (organ/finding/segment fields) yield versus free text — evidence to inform reporting policy.
- **Problem:** Hospitals are deciding whether to mandate structured reporting for clinical reasons; its side effect — dramatically cleaner supervision for image models (deterministic field-to-atlas mapping versus noisy NLP parsing) — is never quantified, so the AI-value argument is absent from a policy debate it should inform.
- **Core Hypothesis:** Supervision derived from structured fields trains dense models to a given performance with several-fold fewer reports than free-text parsing (the parsing-noise tax of B-0346 avoided at the source), and the gap widens for spatial detail (segment-level fields) — yielding a concrete supervision-value coefficient per structured field to weigh in reporting-policy decisions.
- **Why Important:** A rare chance for the vision community to inform upstream data-generation policy with numbers before conventions harden.
- **Why Possibly Novel:** Structured-vs-free-text comparisons exist for clinical retrieval; the dense-supervision value comparison is unmeasured.
- **Minimal Experiment:** On a corpus with both structured fields and free text for the same studies, derive supervision from each; train matched models; compare report-efficiency curves. Falsified if parsing closes the gap.
- **Main Risk:** Corpora with parallel structured/free-text reporting are limited (some registries qualify).
- **Cluster:** MultiSup

### B-0355
- **One-sentence idea:** Multimodal consistency as a deployment QC loop: disagreement between report-derived expectations and image-derived segmentation flags errors in either the model or the report — one signal auditing both.
- **Problem:** Deployed segmentation lacks ground truth for monitoring (B-0010's problem), and reports lack systematic verification against images; yet each is an independent observation of the same patient — their disagreement is computable per study and currently computed nowhere, wasting a free bidirectional error detector.
- **Core Hypothesis:** Text-image disagreement (parsed findings vs. model outputs, with calibrated tolerance per finding type) flags model failures with useful precision on studies where reports are reliable, flags report errors (missed findings) where the model is reliable, and the two error sources are separable by disagreement pattern — enabling a deployed loop that improves both model monitoring and reporting quality from the same signal.
- **Why Important:** Solves deployment monitoring (the blocker of B-0010) using data every hospital already produces, while adding report QA as a by-product.
- **Why Possibly Novel:** Report-image consistency appears in dataset-cleaning contexts; the deployed bidirectional QC loop with source attribution is undesigned.
- **Minimal Experiment:** On a corpus with adjudicated errors of both kinds, compute disagreement signals; measure flagging precision/recall per error source; test attribution. Falsified if disagreement can't separate error sources.
- **Main Risk:** Correlated failures (model trained on similar reports misses what reports miss — B-0336's shortcut) blind the loop exactly where both err.
- **Cluster:** MultiSup

### B-0356
- **One-sentence idea:** Let a physically grounded modality define the boundary convention for an ambiguous one: elastography stiffness maps as the training-time arbiter of tumor boundaries in B-mode ultrasound and MRI.
- **Problem:** Tumor boundaries in B-mode/MR are partly conventional (B-0159's problem) because the visible interface is ambiguous; elastography measures the mechanically distinct region — a physical quantity closer to the surgical margin question — but is used diagnostically, not as the boundary-defining supervision for models on the ambiguous modality.
- **Core Hypothesis:** Training B-mode/MR segmenters against elastography-derived boundaries (co-acquired, registered) produces delineations that predict surgical/pathological margins better than radiologist-contour-supervised models — replacing an aesthetic convention with a physical one, testable wherever resection specimens provide ground truth.
- **Why Important:** Anchors segmentation conventions to physical/clinical reality rather than annotation habit — the deepest version of the convention problem this catalog repeatedly meets.
- **Why Possibly Novel:** Multi-modal fusion for diagnosis exists; cross-modal boundary-convention supervision with pathology-anchored evaluation appears unattempted.
- **Minimal Experiment:** On paired B-mode+elastography lesion data (with any pathology-correlated outcome), train contour- vs. stiffness-supervised models; compare against margin-related endpoints. Falsified if stiffness boundaries predict outcomes no better.
- **Main Risk:** Elastography has its own artifacts and limited penetration; registration between modalities on deformable tissue is hard.
- **Cluster:** MultiSup

### B-0357
- **One-sentence idea:** Mine RECIST caliper annotations — the diameter lines radiologists draw on millions of oncology studies — as sparse geometric supervision for lesion segmentation at archive scale.
- **Problem:** Every oncology trial and routine follow-up generates caliper measurements (endpoints of the longest lesion axis, stored in PACS/DICOM), constituting the largest existing corpus of expert lesion geometry — yet segmentation training uses only the rare fully contoured datasets, ignoring an annotation archive orders of magnitude larger because no formulation consumes two-point diameter labels.
- **Core Hypothesis:** Caliper supervision (endpoints constrain the mask's extremal axis; the line's interior is lesion-positive; perpendicular extent is softly bounded by RECIST convention) trains lesion segmenters to within a modest gap of contour-supervised models, and combining archive-scale calipers with few contours beats contour-only training at any realistic contour budget — the strongest available instance of the archive-supervision thesis.
- **Why Important:** Converts decades of routine oncology workflow into training data; immediately actionable in any hospital system.
- **Why Possibly Novel:** RECIST data feeds response assessment research; its systematic use as dense-supervision (with the axis-constraint formulation) is strikingly underexplored.
- **Minimal Experiment:** On a lesion dataset with masks, simulate caliper labels; train caliper-only and caliper+few-masks models; place on the annotation-value scale (per B-0333). Falsified if two-point supervision is geometrically insufficient.
- **Main Risk:** Real calipers have selection bias (target lesions only per RECIST rules) — the PU machinery of B-0191 handles the unmeasured lesions.
- **Cluster:** MultiSup

### B-0358
- **One-sentence idea:** Settle whether report generation as an auxiliary task improves dense-prediction representations — the transfer direction the medical VLM field assumes but has not isolated.
- **Problem:** Joint segmentation+report-generation models are built on the assumption that generation pressure enriches spatial representations; but generation may instead siphon capacity toward language fluency, and the assumed positive transfer to dense tasks has never been isolated from data and scale confounds — the field's architectural direction rests on an untested premise.
- **Core Hypothesis:** At controlled data/capacity, adding report generation to segmentation training helps dense performance only when generation is grounded (attention constrained to image evidence, per B-0337) and hurts when ungrounded (fluency learned from report priors drains capacity) — a conditional answer explaining the mixed anecdotes and prescribing when to co-train.
- **Why Important:** Multi-task medical VLM architectures are proliferating; knowing when generation helps dense tasks prevents systematic capacity waste.
- **Why Possibly Novel:** Joint models exist in numbers; the isolated, grounding-conditioned transfer measurement is unrun.
- **Minimal Experiment:** Matched models: segmentation-only, +grounded generation, +ungrounded generation; dense metrics at fixed capacity/data. Falsified if generation's effect is unconditional (always helps or always hurts).
- **Main Risk:** Grounding enforcement mechanisms themselves add supervision (control by grounding-without-generation arm).
- **Cluster:** MultiSup

### B-0359
- **One-sentence idea:** Pathology-outcome-anchored supervision: use downstream ground truth (biopsy results, resected-specimen measurements) as delayed, sparse, but definitionally correct labels correcting segmentation trained on imaging conventions.
- **Problem:** Segmentation "ground truth" is radiologist opinion; for oncology, the actual truth arrives later — pathology reports, specimen volumetrics — and systematically disagrees with imaging contours (imaging over/underestimates by tissue type); models inherit imaging convention errors that outcome data could correct, but no training formulation consumes delayed outcome labels.
- **Core Hypothesis:** Outcome-anchored calibration (training-time constraints tying predicted volumes/margins to specimen measurements for the resected subset) systematically shifts model predictions toward pathological truth (validatable on held-out resected cases), quantifying and correcting the imaging-convention bias per tumor type — segmentation calibrated to reality rather than to readers.
- **Why Important:** For surgical planning and response assessment, pathological truth is the deliverable; convention-calibrated models have measurably wrong scale today.
- **Why Possibly Novel:** Radiology-pathology correlation is a research field; its inversion into a training signal for dense prediction is unexploited.
- **Minimal Experiment:** On a cohort with imaging + specimen volumetrics, measure imaging-convention bias; train with outcome anchoring on half the resected cases; validate bias correction on the rest. Falsified if outcome constraints can't shift the bias.
- **Main Risk:** Resection cohorts are selected (operable cases), and specimen processing changes geometry (shrinkage models required).
- **Cluster:** MultiSup

### B-0360
- **One-sentence idea:** A grounding-capability taxonomy for medical vision-language segmenters: systematically measure what current models actually ground — anatomy terms, finding terms, spatial modifiers, quantities — as the diagnostic foundation for the report-supervision program.
- **Problem:** The channels proposed across this section (B-0331–B-0357) all assume models can be taught to ground specific language types, but the current grounding capability profile of medical VLM segmenters is unmapped — which term categories ground reliably, which fail, and whether failures are data gaps or architectural limits is unknown, leaving the whole program without a baseline diagnostic.
- **Core Hypothesis:** Grounding capability is sharply stratified by term category (anatomy ≫ common findings ≫ rare findings ≫ spatial modifiers ≫ quantities), the strata correlate with term frequency-in-pretraining and visual definability, and category-targeted fine-tuning lifts individual strata independently — establishing that the failures are data gaps, not architectural limits, and prioritizing the supervision channels accordingly.
- **Why Important:** Provides the capability map that sequences the entire multimodal-supervision agenda by expected yield.
- **Why Possibly Novel:** Grounding evaluations exist for natural-image VLMs; the category-stratified medical audit with the data-vs-architecture attribution is unbuilt.
- **Minimal Experiment:** Build category-balanced grounding probes from richly annotated data; audit 4 public medical VLM segmenters; run one category-targeted fine-tune. Falsified if grounding is category-uniform.
- **Main Risk:** Category boundaries are fuzzy (publish the taxonomy with the benchmark for community iteration).
- **Cluster:** MultiSup
## Section 13 — Cross-cutting Wildcards [B-0361–B-0366]

### B-0361
- **One-sentence idea:** Test whether ambiguity handling is one transferable skill: does a model trained to express uncertainty on multi-rater medical boundaries transfer that competence to smoke boundaries and camouflage, or is ambiguity handling domain-bound?
- **Problem:** Ambiguity-aware methods are developed independently per domain (medical multi-rater, smoke, camouflage, shadow — per B-0003/B-0070/B-0086); if ambiguity expression is a domain-general capability, the fields are quadruplicating work, and cross-domain ambiguity pretraining would lift all of them — but the transfer question has never been posed.
- **Core Hypothesis:** Uncertainty-expression competence (calibrated boundary distributions) transfers across ambiguity domains substantially better than segmentation accuracy itself transfers — because expressing "the boundary is uncertain here" relies on domain-general evidence-weighing — measurable by cross-domain calibration transfer with frozen uncertainty heads.
- **Why Important:** A positive result would found "ambiguity pretraining" as a shared resource across four currently disjoint communities.
- **Why Possibly Novel:** Cross-domain transfer of uncertainty competence (as distinct from task accuracy) appears never to have been measured.
- **Minimal Experiment:** Train ambiguity-aware models on multi-rater medical data; evaluate uncertainty calibration zero-shot on smoke/camouflage multi-rater sets (and reverse); compare against accuracy transfer. Falsified if uncertainty transfers no better than accuracy.
- **Main Risk:** Requires multi-rater data in several domains (B-0070's collection feeds this).
- **Cluster:** AmbigSeg / MedSeg (cross-cutting)

### B-0362
- **One-sentence idea:** Measure the metric-decision correlation: which segmentation metric improvements actually change downstream decisions (treatment choice, alarm raised, robot action), and how much published "progress" is decision-invisible.
- **Problem:** The field optimizes Dice/mIoU deltas of 1–2 points; whether such deltas ever flip a downstream decision (the only thing that matters in deployment) is unknown — progress may be real but decision-irrelevant, or metrics may miss decision-critical differences entirely, and no study has connected the metric layer to the decision layer quantitatively.
- **Core Hypothesis:** Decision-flip analysis (feeding model-pair outputs through real decision rules: RECIST response categories, alarm thresholds, dose constraints) will show many published metric gaps produce near-zero decision changes while some metric-invisible differences (boundary bias, per B-0004) produce many — motivating decision-weighted evaluation as the field's missing outcome layer.
- **Why Important:** Aligns the field's optimization target with its actual value function; likely reorders what counts as progress.
- **Why Possibly Novel:** Clinical-utility discussions are common in prose; the systematic metric-to-decision-flip measurement across method pairs is unexecuted.
- **Minimal Experiment:** For 10 published model pairs on public data, compute decision outputs under 3 real decision rules; tabulate metric-delta vs. decision-flip rates. Pure analysis. Falsified if decision flips track metric deltas faithfully.
- **Main Risk:** Decision rules vary across institutions (use several; report sensitivity).
- **Cluster:** MedSeg / LongTail (cross-cutting)

### B-0363
- **One-sentence idea:** Efficiency-normalized progress audit: re-rank recent dense-prediction state of the art under matched inference compute/energy budgets and measure how much claimed progress survives.
- **Problem:** SOTA claims conflate algorithmic progress with compute growth; deployment operates under fixed budgets (edge devices, per-study cost caps), and whether the field's recent gains persist at matched compute — or are purchased entirely by scale — is unmeasured for dense prediction, distorting both research incentives and deployment expectations.
- **Core Hypothesis:** Under matched-budget evaluation (parameter/FLOP/latency-normalized), a substantial fraction of headline segmentation progress over recent years compresses or vanishes, the survivors identify genuinely algorithmic advances, and efficiency-frontier reporting (accuracy-vs-compute curves, not points) changes which methods practitioners should adopt at each budget.
- **Why Important:** Separates knowledge from expenditure in the field's progress narrative; directly serves budget-constrained deployment.
- **Why Possibly Novel:** Efficiency audits exist for LLMs/classification; the dense-prediction frontier audit with survivor attribution is undone.
- **Minimal Experiment:** Re-evaluate 12 published models across 3 benchmarks with measured FLOPs/latency/energy; fit frontiers by publication year. Pure evaluation. Falsified if frontiers advance as fast as headline numbers.
- **Main Risk:** Faithful re-implementation and measurement standardization burden (publish the harness).
- **Cluster:** MedFM / CrossDom (cross-cutting)

### B-0364
- **One-sentence idea:** Reproducibility audit of dense-prediction SOTA: quantify how much of published method-over-baseline gaps survives independent reimplementation, seed variance, and tuned baselines.
- **Problem:** Segmentation papers report gains over baselines they configure themselves; seed variance, baseline under-tuning, and implementation details plausibly account for a large fraction of claimed gaps (as documented in other ML subfields), but dense prediction — with its expensive runs discouraging replication — has never had a systematic audit, so the literature's effective signal-to-noise is unknown.
- **Core Hypothesis:** Independent reimplementation with equal tuning budgets for methods and baselines will show a substantial fraction of published gaps shrinking below seed-level noise, shrinkage will correlate with identifiable paper properties (missing variance reporting, baseline age), and the audit will yield a checkable "reliability prior" for reading future claims.
- **Why Important:** Field-level error bars determine how much cumulative knowledge the literature actually contains; every methods researcher builds on these claims.
- **Why Possibly Novel:** Replication studies exist for RL/recommendation/optimizers; dense prediction lacks one entirely.
- **Minimal Experiment:** Select 10 influential recent methods; reimplement with matched tuning; run 5 seeds each on original benchmarks. Compute-heavy, conceptually simple. Falsified if published gaps replicate broadly.
- **Main Risk:** Reimplementation fidelity disputes (mitigate with author-reviewed configurations and released code).
- **Cluster:** WSSL / DomainAdapt (cross-cutting)

### B-0365
- **One-sentence idea:** A standardized uncertainty-evaluation protocol for dense prediction — calibration, spatial structure, and downstream utility measured jointly — adopted as a reporting standard across all task families in this catalog.
- **Problem:** Uncertainty outputs are evaluated inconsistently (ECE here, sparsification there, nothing usually), and never for spatial structure (is uncertainty in the right places?) or downstream utility (does it actually help triage/review per B-0016?); methods claiming "uncertainty-aware" cannot be compared, and consumers cannot select — the measurement layer is missing for a capability every deployment needs.
- **Core Hypothesis:** A three-axis protocol (probabilistic calibration, spatial error-coverage, and task-utility under fixed review budgets) will show current methods excel on at most one axis (calibrated but spatially wrong, or useful but miscalibrated), that the axes are empirically separable (low inter-axis correlation across methods), and that axis profiles predict deployment usefulness better than any single score — justifying the protocol as a community standard.
- **Why Important:** Uncertainty quality gates QC (B-0010), annotation targeting (B-0204), safe adaptation (B-0102), and clinical review (B-0016) — a shared measurement standard multiplies all of them.
- **Why Possibly Novel:** Individual uncertainty metrics exist; the joint three-axis protocol with the axis-separability finding and cross-family adoption is unassembled.
- **Minimal Experiment:** Evaluate 8 uncertainty methods on 3 tasks under all three axes; measure inter-axis correlations; validate utility-axis predictions in one simulated review workflow. Falsified if a single existing metric captures all axes.
- **Main Risk:** Utility-axis design requires workflow assumptions (publish as configurable modules).
- **Cluster:** MedSeg / AnnotEff (cross-cutting)

### B-0366
- **One-sentence idea:** Simulate the multi-generation dataset ecosystem: models assist annotation, the resulting datasets train the next models, which assist the next annotation — measuring whether dense-prediction data ecosystems drift toward model-error fixation ("annotation collapse").
- **Problem:** B-0244 shows single-generation anchoring; the field is now entering its third or fourth generation of model-assisted dataset construction, and the ecosystem-level dynamics — do systematic model errors amplify across generations, homogenize datasets, and become unfalsifiable as evaluation sets inherit them too? — have never been studied, though analogous "model collapse" is documented for generative-text ecosystems.
- **Core Hypothesis:** Multi-generation simulation (model → assisted annotation with measured anchoring rates → retrain → repeat) will show systematic error fixation growing per generation, boundary conventions homogenizing toward model-preferred geometry, and — critically — standard benchmarks becoming blind to the drift because they evolve within the same loop; blind-annotation injection at a measurable minimum rate (per generation) stabilizes the ecosystem.
- **Why Important:** If the field's data flywheel fixates errors, everything downstream inherits them invisibly; the stabilization rate is the actionable deliverable for every dataset-producing organization.
- **Why Possibly Novel:** Model collapse is studied for generative training on generated data; the human-in-the-loop annotation-ecosystem version with anchoring dynamics and stabilization policy is unexplored.
- **Minimal Experiment:** Simulate 5 generations using B-0244's measured anchoring rates on one dataset; track error fixation and convention drift; sweep blind-injection rates. Falsified if human correction naturally damps drift.
- **Main Risk:** Simulation fidelity to real annotator behavior (anchor parameters must come from real studies, hence the dependency on B-0244).
- **Cluster:** AnnotEff / WSSL (cross-cutting)

---

*End of catalog: 366 ideas (B-0001–B-0366). Stage 1 output — unfiltered by design; filtering and Windows archival packaging are later-stage tasks.*
