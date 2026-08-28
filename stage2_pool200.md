# Stage 2 — Windows5 Official Unique Idea Pool (stage2_pool200)

**Role:** Stage-2 closer. **Inputs:** `stage2_AB_merged_pool.md` (130 unique, branch `cursor/stage2-ab-merge-80a1`), `stage2_batch_C_survivors.md` (74, branch `cursor/stage2-batch-c-review-0cdb`), `stage2_audit.md` revive list (12, branch `cursor/stage2-meta-audit-dbae`).
**Arithmetic:** 130 + 74 + 12 = 216 candidates → 16 cross-batch dedup merges → **200 unique ideas**.
**Merges this pass:** MERGE-19…29 (11 new) + 5 extensions of existing merges (MERGE-04, -09, -14, -15, -18, marked ‡). Full log in `stage2_pool200_index.md`.
**Revives:** all 12 auditor revives executed; B-0081 merged with survivor C-0177 (same program) as MERGE-24 — none of the other 11 duplicates a survivor.
**Novelty status:** every entry is **UNVERIFIED** pending the Stage-3 prior-art sweep (`stage3_attack_queue.md`); entries with documented overlap carry an explicit risk note.
**Protection legend:** HR/HRHR high-risk-high-reward · CI counter-intuitive · RM/DM disagreement magnet · CF cheap-to-falsify · REV auditor revive · M merit (unprotected). Merged entries carry the union of constituent flags.
**Balance:** evaluation-genre entries are capped per the auditor (§6.1): 30/200 = 15% core eval (marked [E]); constructive/method ideas ≈ 38 (19%); HRHR/HR wildcards 30 (15%).

---

## P1 — Auto-labeling ecology & ground-truth contamination (9)

### W5-001 — Model-in-the-loop annotation corrupts its own ground truth
- **CanonicalID:** W5-001  ·  **Cluster:** P1 — Auto-labeling ecology & ground-truth contamination
- **SourceIDs:** IDEA-A-0029 + IDEA-B-0019  (= MERGE-01)
- **One-liner:** Within-annotator crossover (scratch / SAM-assisted / correct-the-proposal) measuring anchoring and agreement-with-SAM inflation, plus student training on each corpus to test error-signature inheritance.
- **Problem:** SAM is now embedded in annotation tools; if annotators accept SAM proposals preferentially where SAM is good, new datasets inherit SAM's competence profile — an ecosystem-level circularity nobody has quantified.
- **Hypothesis:** Datasets built with SAM-assisted pipelines show measurably higher agreement-with-SAM (by >10 IoU) than scratch-annotated datasets on matched content, and models trained on the former overestimate their real-world boundary quality by a corresponding margin.
- **Novelty:** UNVERIFIED
- **Protect:** HR+RM / HRHR·DM
- **Why kept:** Strongest cross-batch convergence in the pool: both reviewers independently generated the model-in-the-loop GT-corruption claim; one within-annotator crossover plus a student inheritance test answers both. Maximum protection.

### W5-002 — SAM masks imprint the SA-1B annotation protocol
- **CanonicalID:** W5-002  ·  **Cluster:** P1 — Auto-labeling ecology & ground-truth contamination
- **SourceIDs:** IDEA-A-0007
- **One-liner:** Determine how much of SAM's mask granularity behavior is an imprint of the SA-1B annotation *protocol* rather than a property of images.
- **Problem:** SA-1B was built with a specific interactive annotation pipeline; SAM's notion of "a mask" may encode that pipeline's policy (e.g., preferred granularity, hole handling) rather than natural object statistics.
- **Hypothesis:** SAM's everything-mode mask-size and mask-count distributions match SA-1B's distributions far more closely than those of independently annotated datasets (ADE20K, LVIS) on the *same images*, indicating protocol imprinting.
- **Novelty:** UNVERIFIED
- **Protect:** RM
- **Why kept:** Ecosystem-level claim with a clean same-images design: "segment anything" reframed as "replicate SA-1B's annotation policy." A reviewer-disagreement magnet — some will call it obvious, others field-critical — which is exactly the protected profile.

### W5-003 — Weak-to-strong dense distillation: inherit vs surpass (incl. the soft-label channel)
- **CanonicalID:** W5-003  ·  **Cluster:** P1 — Auto-labeling ecology & ground-truth contamination
- **SourceIDs:** IDEA-A-0267 + IDEA-B-0329 + IDEA-C-0310  (= MERGE-09‡)
- **One-liner:** Students trained on weak-teacher/SAM labels (hard or soft) inherit spatially correlated bias-type errors and surpass variance-type errors; bias-breaking perturbations and mixing-dilution curves define auto-labeling's ceiling.
- **Problem:** Training students on foundation-model labels — pseudo-masks or soft distillation targets — is the field's dominant dataset-construction strategy, but which teacher errors students inherit versus correct, and thus the strategy's ceiling, is unmeasured.
- **Hypothesis:** Students inherit bias-type teacher errors (error-signature match above chance, transferred through hard labels and through soft-label 'dark knowledge') while surpassing variance-type errors; bias-breaking label perturbations and fresh-data mixing shift the inheritance predictably — falsified if students' errors decorrelate from their teachers'.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR·DM
- **Why kept:** Capstone of the contamination program; A supplies the signature instrument, B the bias/variance theory and surpassing test, and C-0310 adds the soft-label distillation channel — one error-decomposition harness covers pseudo-labeling and distillation.

### W5-004 — Structured (non-i.i.d.) noise in SAM pseudo-labels breaks noise-robust learning theory
- **CanonicalID:** W5-004  ·  **Cluster:** P1 — Auto-labeling ecology & ground-truth contamination
- **SourceIDs:** IDEA-B-0001
- **One-liner:** Characterize SAM-generated pseudo-label noise as spatially structured (boundary-biased, systematically dilated/eroded per texture class) and test whether noise-robust losses designed for i.i.d. label noise fail on it.
- **Problem:** SAM is widely used as an auto-labeler, but downstream training methods assume label noise is random, while SAM's errors are systematic and correlated with image content.
- **Hypothesis:** Noise-robust training methods that provably help under symmetric/asymmetric i.i.d. pixel noise give near-zero or negative gains when the noise source is SAM pseudo-labels, because the noise is low-entropy and learnable as a bias.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Measures the noise model of the field's default auto-labeler.

### W5-005 — Error amplification in self-consuming segmentation pipelines
- **CanonicalID:** W5-005  ·  **Cluster:** P1 — Auto-labeling ecology & ground-truth contamination
- **SourceIDs:** IDEA-B-0191
- **One-liner:** Measure the generational dynamics of pipelines where models pseudo-label data used to train successor models (the standard auto-labeling loop), quantifying which error types amplify, stay stable, or self-correct across generations.
- **Problem:** Foundation-model auto-labeling has made recursive training loops ubiquitous in dense prediction, while the collapse dynamics studied for generative models have no dense-task analogue to guide practice.
- **Hypothesis:** Boundary biases amplify geometrically across generations (each student sharpens its teacher's systematic offsets) while random errors wash out, so multi-generation loops drift toward confident, consistent, wrong boundaries—detectable early via generational bias-trend monitoring and preventable with small fresh-label injections whose required rate is measurable.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Defines the stability conditions of the data flywheel everyone is now building on.

### W5-006 — Positive-unlabeled statistics for everything-mode auto-labeling
- **CanonicalID:** W5-006  ·  **Cluster:** P1 — Auto-labeling ecology & ground-truth contamination
- **SourceIDs:** IDEA-B-0320
- **One-liner:** Treat SAM everything-mode outputs as what they statistically are—high-precision positives over an unknown-recall support—and develop positive-unlabeled estimation for training detectors/segmenters from them, replacing the false closed-world assumption of current auto-labeling.
- **Problem:** Models trained on everything-mode pseudo-labels systematically suppress object classes and strata the proposal engine under-recalls, inheriting and hardening its blind spots.
- **Hypothesis:** PU-corrected training (with per-stratum class priors estimated from small audits) recovers a substantial fraction of the recall lost to naive training (largest on low-contrast and small-object strata where everything-mode recall is worst), and the required audit budget for prior estimation is tiny relative to the gains—making the correction nearly free.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Repairs a foundational statistical flaw in the field's dominant auto-labeling pattern using the theory built for exactly this data shape.

### W5-007 — A geometric-stratum census of SA-1B that predicts fine-tuning gains
- **CanonicalID:** W5-007  ·  **Cluster:** P1 — Auto-labeling ecology & ground-truth contamination
- **SourceIDs:** IDEA-B-0009
- **One-liner:** Audit web-scale segmentation pretraining data (SA-1B) for the frequency of hard strata—transparent, wiry, camouflaged, low-contrast, tiny—and test whether stratum frequency predicts where fine-tuning helps most.
- **Problem:** We know SAM fails on transparent and thin objects, but we lack a quantitative account tying failures to pretraining-data frequency versus architectural limits.
- **Hypothesis:** Per-stratum zero-shot IoU and per-stratum fine-tuning gain are both log-linear in the stratum's estimated pretraining frequency; strata that deviate from this line indicate architectural (not data) limits.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR — protected
- **Why kept:** The most consequential distinction in foundation-model planning: strata on the frequency-capability line need data; deviating strata need new architecture.

### W5-008 — Label-convention averaging: systematic boundary bias from multi-dataset fine-tuning
- **CanonicalID:** W5-008  ·  **Cluster:** P1 — Auto-labeling ecology & ground-truth contamination
- **SourceIDs:** IDEA-B-0006
- **One-liner:** Show that fine-tuning one model on multiple datasets with different annotation conventions (e.g., "organ+capsule" vs "organ only") produces a predictable averaged boundary bias rather than dataset-conditional behavior.
- **Problem:** Merged medical datasets silently disagree about where boundaries are by convention, and models trained on the union may learn a compromise that matches no convention.
- **Hypothesis:** A model fine-tuned on merged conventions exhibits a systematic boundary offset approximating a weighted average of source conventions, measurable as bias (not variance), and a one-token convention indicator removes most of it.
- **Novelty:** UNVERIFIED
- **Protect:** DM
- **Why kept:** Attacks the field's default scaling recipe (pool everything) with a measurable bias term and a nearly free fix.

### W5-009 — Ontology shift disguised as appearance shift across endoscopy datasets
- **CanonicalID:** W5-009  ·  **Cluster:** P1 — Auto-labeling ecology & ground-truth contamination
- **SourceIDs:** IDEA-B-0053
- **One-liner:** Estimate what fraction of cross-dataset performance drop between endoscopy benchmarks is due to differing label definitions ("polyp" boundaries, inclusion rules) rather than appearance shift, using a small bridge re-annotation.
- **Problem:** Cross-dataset drops are cited as evidence of appearance domain gaps, motivating adaptation methods, but part of the drop may be that the datasets define the target differently.
- **Hypothesis:** Re-annotating a bridge set of images from dataset B under dataset A's written protocol recovers a substantial fraction of the cross-dataset drop, bounding the true appearance gap well below the reported gap.
- **Novelty:** UNVERIFIED
- **Protect:** DM
- **Why kept:** Could show a chunk of the domain-adaptation literature has been fitting a label-definition gap with appearance machinery.

## P2 — Benchmark validity & evaluation instruments (13)

### W5-010 — Label-noise-aware leaderboards with rank-flip probabilities [E]
- **CanonicalID:** W5-010  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-A-0091 + IDEA-B-0082 + IDEA-C-0321  (= MERGE-15‡)
- **One-liner:** Multi-rater re-annotation (3 raters × 50–100 cases × ~5 benchmarks) measures inter-annotator floors and fits noise models; a relabeling bootstrap converts them into rank-flip probabilities and per-benchmark verdicts.
- **Problem:** Leaderboard gains of 0.5–1 Dice are celebrated on benchmarks whose annotator disagreement may be several Dice points, meaning models are being fit to one annotator's style, not anatomy.
- **Hypothesis:** For ≥half of widely used benchmarks, the top-10 leaderboard spread is smaller than the measured inter-annotator Dice spread on a re-annotated subset — recent "progress" is within label noise.
- **Novelty:** UNVERIFIED — partial overlap: Maier-Hein 2018 / Wiesenfarth toolkit rank-stability line (audit §3.1)
- **Protect:** RM / CF·DM
- **Why kept:** Flagship medical-evaluation instrument; B's bootstrap consumes exactly the multi-rater data A collects, and C-0321 (independently generated 3-rater pilot) folds in as the entry-point study. Novelty at risk: must reposition against Maier-Hein 2018 / Wiesenfarth challenge-rank bootstraps (audit §3).

### W5-011 — The annotation-tolerance ceiling + tolerance-band metrics [E]
- **CanonicalID:** W5-011  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-A-0166 + IDEA-B-0037 + IDEA-C-0245  (= MERGE-14‡)
- **One-liner:** Closed-form max-IoU from boundary tolerance and object size, empirically anchored by multi-rater jitter; annotator-identity prediction from residuals proves style-fitting; tolerance-band metrics test how rankings change when within-ambiguity errors stop counting.
- **Problem:** Benchmarks reward sub-jitter boundary matching that no human rater could reproduce; the field lacks the analytic ceiling, empirical tolerance estimates, and metrics that stop scoring 'progress' inside the ambiguity band.
- **Hypothesis:** Per-stratum max-IoU follows a closed form in tolerance and object size; on small structures, leaderboard gaps sit at or above this ceiling (style-fitting, provable by predicting annotator identity from model residuals), and tolerance-band re-scoring materially changes method rankings.
- **Novelty:** UNVERIFIED
- **Protect:** CI / CF
- **Why kept:** One tolerance program: A's empirical jitter floor, B's closed form, and C-0245's tolerance-aware metric (independently generated) are three parts of one paper — an evaluation instrument with a constructive metric deliverable.

### W5-012 — Bootstrap the leaderboards: the fiction fraction [E]
- **CanonicalID:** W5-012  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-A-0340
- **One-liner:** Apply bootstrap resampling over test sets to published segmentation rankings and measure what fraction of leaderboard orderings are statistically indistinguishable under test-set sampling variation alone.
- **Problem:** Leaderboards present point-estimate orderings with no test-set-sampling uncertainty; two models differing by 0.4 mIoU on a 2k-image test set may be statistically tied, but the field has never computed ranking confidence at scale — the leaderboard's implied precision is unexamined.
- **Hypothesis:** Under image-level bootstrap, >50% of adjacent-pair orderings on major segmentation leaderboards are within sampling noise (overlapping 95% intervals), and the fraction grows near the top where gaps compress — most fine-grained leaderboard structure is statistically fictional, falsified if orderings are robust under resampling.
- **Novelty:** UNVERIFIED — known overlap: Maier-Hein et al. 2018 bootstrapped biomedical challenge rankings; must reposition (audit §3.1)
- **Protect:** CF
- **Why kept:** The cheapest idea in the batch that produces a headline number: near-zero model runs (released predictions suffice), a week of analysis, and a "fiction fraction" that reframes how leaderboards are read.

### W5-013 — Human floors and ceilings for segmentation benchmarks [E]
- **CanonicalID:** W5-013  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-A-0336
- **One-liner:** Measure human segmentation performance (time-budgeted and unlimited) on standard benchmarks to establish the human floors and ceilings that segmentation evaluation has always lacked.
- **Problem:** Unlike classification (where human baselines anchored progress narratives), segmentation benchmarks have no published human performance — so "superhuman" claims, headroom estimates, and difficulty comparisons across benchmarks all float without an anchor.
- **Hypothesis:** Human mIoU on standard benchmarks is substantially below 100 (HYPOTHESIS: 75–90 depending on benchmark, driven by class-definition ambiguity rather than perceptual failure), and current top models already exceed time-budgeted human performance on ≥2 benchmarks while trailing unlimited-time humans everywhere — the human anchor reorders our sense of which benchmarks are "hard."
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** The missing anchor of dense-prediction evaluation — the fact that no systematic human baseline exists for major segmentation benchmarks is itself the surprising finding.

### W5-014 — Annotation instructions as an experimental treatment [E]
- **CanonicalID:** W5-014  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-A-0337
- **One-liner:** Treat annotation instructions as an experimental variable: annotate the same images under different (all-reasonable) instruction documents and measure how much benchmark ground truth — and resulting model rankings — depend on instruction wording.
- **Problem:** Instructions define what ground truth *is* (occlusion handling, boundary conventions, class edge cases), yet they are unpublished, unversioned, and never varied experimentally; the GT variance induced by instruction choice is a hidden hyperparameter of every benchmark.
- **Hypothesis:** Two reasonable instruction variants produce GT differing by >5 IoU-equivalent on ambiguity-prone classes, sufficient to invert model rankings whose gaps are below that scale — benchmark conclusions are instruction-contingent at the scale of typical SOTA gaps.
- **Novelty:** UNVERIFIED
- **Protect:** RM
- **Why kept:** The most methodologically novel idea in the evaluation cluster (Nov 5): instructions-as-treatment is genuinely new experimental methodology, and "GT is instruction-contingent at SOTA-gap scale" would be a finding every benchmark paper must cite.

### W5-015 — Near-duplicate contamination and the inflation of efficiency claims [E]
- **CanonicalID:** W5-015  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-B-0012 + IDEA-C-0328  (= MERGE-28)
- **One-liner:** Embedding-based train/test near-duplicate audits of popular benchmarks, plus the predictable shrinkage of few-shot and annotation-efficiency claims under dedup-aware splits.
- **Problem:** Near-duplicates (adjacent frames, same-patient slices, re-posted web images) sit across train/test boundaries and inside few-shot splits, inflating efficiency and generalization numbers that now drive clinical adoption decisions.
- **Hypothesis:** Duplicate-cluster structure predicts the inflation: dedup-aware re-splits shrink few-shot/annotation-efficiency gains by a dataset-predictable factor, and popular benchmarks contain enough train/test near-duplicates to move headline numbers — falsified if dedup leaves claims intact.
- **Novelty:** UNVERIFIED — adjacent: established patient-leakage/dedup literature; few-shot quantification is the residual (audit §3.6)
- **Protect:** CF·DM
- **Why kept:** Merged the general contamination audit (C-0328, which absorbed C-0170) with its sharpest consequence (B-0012's few-shot inflation); one duplicate-detection pass serves both. Run early — it recalibrates how the program reads the efficiency literature.

### W5-016 — The missing-negative problem in transparent-object benchmarks [E]
- **CanonicalID:** W5-016  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-B-0017
- **One-liner:** Show that transparent-object segmentation benchmarks contain almost no target-absent images, leaving false-positive behavior unmeasured, and build a negative-inclusive evaluation that changes method rankings.
- **Problem:** Benchmarks like glass/transparent-object suites evaluate only images containing glass, so models are never penalized for hallucinating transparency on glossy or reflective non-glass surfaces.
- **Hypothesis:** Method rankings on positives are weakly correlated with false-positive rates on curated hard negatives (mirrors, water, gloss), and some top methods are among the worst on negatives.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Deployment harm is FP-dominated (hallucinated glass in robotics), yet the benchmarks penalize only misses.

### W5-017 — Honest zero-shot: quantifying hidden adaptation through validation-set prompt search [E]
- **CanonicalID:** W5-017  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-B-0108
- **One-liner:** Measure how much of reported "zero-shot" segmentation performance is attributable to prompt-template and hyperparameter search on validation data from the target distribution, establishing corrected zero-shot bounds.
- **Problem:** Papers tune prompt templates, thresholds, and post-processing on target-domain validation splits and still call the result zero-shot, conflating adaptation-free capability with search-based adaptation.
- **Hypothesis:** Validation-informed prompt/hyperparameter search accounts for a substantial fraction of claimed zero-shot performance, and truly search-free evaluation (fixed universal settings) reorders zero-shot leaderboards.
- **Novelty:** UNVERIFIED
- **Protect:** DM
- **Why kept:** Zero-shot claims drive deployment planning; this is the cheapest way to find out what they are worth.

### W5-018 — Efficient false-positive-rate estimation for rare-event monitoring via importance-sampled negatives [E]
- **CanonicalID:** W5-018  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-B-0110
- **One-liner:** Develop and validate an importance-sampling estimator for extremely low false-positive rates (FP/day) of fire/smoke systems, replacing infeasible exhaustive negative evaluation with stratified sampling over scene-condition space.
- **Problem:** Deployment requires certifying FP rates on the order of one per camera-week, but test sets contain thousands—not billions—of negative frames, so reported FP rates are statistically meaningless at the certification scale.
- **Hypothesis:** Negative-frame risk is concentrated in identifiable strata (sunsets, fog banks, steam, headlights), and stratified importance sampling with learned proposal distributions estimates deployment FP rates with orders-of-magnitude fewer labeled negatives than uniform sampling, validated against long-duration field logs.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The gap between "demo" and "deployable" for rare-event systems is exactly this estimator.

### W5-019 — Bimodal test losses: detecting pretraining contamination from loss distributions alone [E]
- **CanonicalID:** W5-019  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-B-0294
- **One-liner:** Test whether per-image loss distributions on evaluation sets exhibit mixture structure (a memorized low-loss mode and a genuine-generalization mode) that reveals pretraining contamination without any access to the pretraining corpus.
- **Problem:** Contamination auditing requires corpus access nobody has, but if memorized images betray themselves through anomalously low loss relative to their difficulty, contamination becomes statistically detectable from model behavior alone—turning an intractable provenance problem into a mixture-modeling problem.
- **Hypothesis:** Evaluation-set loss residuals (after regressing out measurable difficulty) are bimodal for contaminated benchmarks and unimodal for verified-clean ones, the low-residual mode's images disproportionately have web-visible duplicates (external validation), and mode-membership provides per-image contamination probabilities that materially change benchmark conclusions when used as weights.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR — protected
- **Why kept:** Contamination auditing currently requires corpus access nobody has; a behavioral detector would be applied to every existing benchmark and model.

### W5-020 — A provably-novel synthetic zero-shot benchmark [E]
- **CanonicalID:** W5-020  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-A-0254
- **One-liner:** Construct a true-zero-shot benchmark from procedurally synthesized never-seen categories to measure how much of "zero-shot segmentation" survives when pretraining exposure is provably zero.
- **Problem:** Zero-shot claims are untestable on natural categories (everything is in web data somewhere, cf. IDEA-A-0194); provably novel synthetic categories with controllable structure would give the first clean zero-shot measurement.
- **Hypothesis:** On procedurally generated novel object categories (parametric shape-texture grammars, verified absent from training corpora), OV segmentation performance drops >40% relative to matched-difficulty natural categories — a large share of "zero-shot" is memory, falsified if synthetic-novel performance matches natural.
- **Novelty:** UNVERIFIED
- **Protect:** RM
- **Why kept:** The contamination-proof instrument the zero-shot literature lacks; absorbs 0194's accounting question and 0333's adjusted-scores agenda into one clean construction.

### W5-021 — FSS scores are base-class proximity in disguise [E]
- **CanonicalID:** W5-021  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-A-0246
- **One-liner:** Audit base-class leakage in few-shot segmentation benchmarks: how much of reported FSS performance comes from novel classes resembling base classes seen during episodic training?
- **Problem:** FSS protocols split classes into base/novel, but visual similarity between splits (novel "sheep" after base "cow") means "few-shot" performance partly measures base-class generalization — the leakage magnitude has never been quantified.
- **Hypothesis:** Per-novel-class FSS performance correlates strongly (ρ > 0.7) with feature-space proximity to the nearest base class, and re-splitting benchmarks to maximize base-novel distance drops reported SOTA by >15 IoU — much of "few-shot learning" is near-class transfer.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Cheap, decisive audit of the FSS protocol itself; the max-distance re-split is a constructive deliverable, not just criticism.

### W5-022 — Evaluate methods against 1-pixel morphological perturbations of ground truth: if rankings… [E]
- **CanonicalID:** W5-022  ·  **Cluster:** P2 — Benchmark validity & evaluation instruments
- **SourceIDs:** IDEA-C-0339
- **One-liner:** Evaluate methods against 1-pixel morphological perturbations of ground truth: if rankings flip, benchmarks measure annotation-style matching, not accuracy.
- **Problem:** If dilating or eroding all test masks by one pixel reorders method rankings, methods differ mainly in their systematic offset relative to an arbitrary annotation convention — a possibility never checked.
- **Hypothesis:** On boundary-sensitive metrics, single-pixel ground-truth morphology changes flip a substantial fraction of pairwise method rankings on popular benchmarks — published boundary superiority claims are largely claims about matching the annotation convention's tightness, and offset-calibrated evaluation removes the flips.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** PROTECTED (cheap-to-falsify). Re-scoring against ±1-pixel morphological perturbations of ground truth tests whether boundary leaderboards measure delineation skill or annotation-convention matching — an afternoon-scale experiment with field-level consequences.

## P3 — Meta-science, replication & attribution (7)

### W5-023 — A 2015 U-Net with a 2026 recipe [E]
- **CanonicalID:** W5-023  ·  **Cluster:** P3 — Meta-science, replication & attribution
- **SourceIDs:** IDEA-A-0245
- **One-liner:** Re-train decade-old architectures (original U-Net, DeepLab-era models) with fully modern recipes to measure what fraction of a decade's reported segmentation progress is recipe rather than architecture.
- **Problem:** Progress narratives credit architectures, but recipes (augmentation, schedules, normalization, pretraining) improved simultaneously; the attribution has never been settled for segmentation, distorting where the field believes value comes from.
- **Hypothesis:** Modern-recipe U-Net (2015 architecture) closes >60% of the reported gap to modern architectures on standard benchmarks — most of a decade's progress is recipe, falsified if the architecture gap survives recipe equalization.
- **Novelty:** UNVERIFIED — known overlap: nnU-Net Revisited (arXiv:2404.09556) settles the medical-3D arm; natural-image decade arm open (audit §3.2)
- **Protect:** RM
- **Why kept:** The batch flagship falsification study: index surprising-#1, deservedly.

### W5-024 — Powered compute-matched replication: the field's inflation factor [E]
- **CanonicalID:** W5-024  ·  **Cluster:** P3 — Meta-science, replication & attribution
- **SourceIDs:** IDEA-A-0226 + IDEA-C-0340  (= MERGE-29)
- **One-liner:** Re-run a sample of published gains (attention-U-Net genre and beyond) giving baselines the proposed method's full compute including hyperparameter search, with ≥5 seeds — how much of the literature survives?
- **Problem:** The field's most common paper template claims gains over under-tuned baselines with unreported search budgets; how much of the genre survives tuned baselines, matched total compute, and multi-seed statistics is unknown.
- **Hypothesis:** Under tuned baselines at matched total compute (including hyperparameter search) and 5 seeds, a majority of sampled module-contribution claims lose statistical significance; the surviving fraction defines a field-level inflation coefficient — falsified if most published gains replicate.
- **Novelty:** UNVERIFIED — adjacent: nnU-Net Revisited and tuned-baseline replication genre
- **Protect:** RM
- **Why kept:** Merged A's genre-specific powered replication with C-0340's general compute-matching protocol: one replication program, one inflation estimate; ground-truths A-0242's publication-bias z-curve.

### W5-025 — Publication bias: the z-curve for segmentation deltas [E]
- **CanonicalID:** W5-025  ·  **Cluster:** P3 — Meta-science, replication & attribution
- **SourceIDs:** IDEA-A-0242
- **One-liner:** Estimate publication bias in segmentation literature by comparing the distribution of reported improvements against the expected null distribution from seed noise (z-curve/caliper analysis of reported deltas).
- **Problem:** If many reported gains cluster just above significance/noise thresholds, the literature's aggregate evidential value is inflated by selection; segmentation-specific quantification of this bias does not exist.
- **Hypothesis:** Reported improvement distributions show a discontinuity at the informal ~0.5–1.0 point "publishability threshold" (excess mass just above, deficit just below) inconsistent with any smooth true-effect distribution — quantifiable selection bias, falsified if the distribution is smooth.
- **Novelty:** UNVERIFIED
- **Protect:** RM
- **Why kept:** A field-level selection-bias coefficient — one number that contextualizes every small reported gain.

### W5-026 — Deflationary baselines for few-shot segmentation [E]
- **CanonicalID:** W5-026  ·  **Cluster:** P3 — Meta-science, replication & attribution
- **SourceIDs:** IDEA-A-0250 + IDEA-B-0024  (= MERGE-11)
- **One-liner:** Shot-ladder grid: episodic meta-learning vs direct PEFT fine-tuning vs retrieval + dense-correspondence transfer, cross-domain; locate the crossovers and deliver the honest-baseline table the FSS literature never reports.
- **Problem:** Few-shot fine-tuning is the default even at n=3–5, where optimization is unstable; a retrieval-plus-correspondence baseline is rarely reported.
- **Hypothesis:** For anatomies with consistent topology, correspondence-based mask transfer dominates fine-tuning below a crossover n, and the crossover is predictable from registration residuals.
- **Novelty:** UNVERIFIED
- **Protect:** CF / DM·CF
- **Why kept:** A's third arm is B's method — identical shot budgets, targets, and honesty constraints; one study retires two literature gaps.

### W5-027 — WSSS's residual gap is structural extent error [E]
- **CanonicalID:** W5-027  ·  **Cluster:** P3 — Meta-science, replication & attribution
- **SourceIDs:** IDEA-A-0261
- **One-liner:** Decompose the remaining gap in image-label-only weakly supervised semantic segmentation (WSSS) into localization, extent, and boundary components to test whether the CAM paradigm has hit a structural ceiling.
- **Problem:** WSSS progress has slowed near a performance plateau; without knowing whether the residual gap is in finding objects, estimating their extent, or delineating boundaries, the field cannot tell if the CAM-seed paradigm is exhausted or under-optimized.
- **Hypothesis:** ≥70% of the residual gap to full supervision is extent error (systematic under/over-coverage of discriminative regions), which is *structural* to classification-derived localization — oracle boundary refinement barely helps, and no CAM-family method can close it, falsified if boundary refinement recovers most of the gap.
- **Novelty:** UNVERIFIED
- **Protect:** RM
- **Why kept:** Oracle-substitution ceiling analysis that could end a subfield's optimization race with evidence; the paradigm-exhaustion verdict is RM-protected territory.

### W5-028 — Run a seed-variance meta-analysis of prompt-learning literature: how many reported gains… [E]
- **CanonicalID:** W5-028  ·  **Cluster:** P3 — Meta-science, replication & attribution
- **SourceIDs:** IDEA-C-0094
- **One-liner:** Run a seed-variance meta-analysis of prompt-learning literature: how many reported gains exceed seed noise?
- **Problem:** Prompt tuning has few parameters but high optimization variance; papers report single-seed or best-seed numbers on few-shot splits.
- **Hypothesis:** Re-running representative prompt-learning methods with ≥10 seeds and multiple few-shot draws shows that a substantial fraction of published between-method gaps fall inside the joint seed+split noise band.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Seed/split variance meta-analysis of the prompt-learning canon; measurement repair with immediate field-wide consequences for how few-shot claims are read.

### W5-029 — Run the scramble test on published "global context" modules: shuffle distant image… [E]
- **CanonicalID:** W5-029  ·  **Cluster:** P3 — Meta-science, replication & attribution
- **SourceIDs:** IDEA-C-0315
- **One-liner:** Run the scramble test on published "global context" modules: shuffle distant image regions and see if the module's benefit survives.
- **Problem:** Many papers attribute gains to long-range context aggregation; if performance is unchanged when distant content is scrambled, the module's stated mechanism is not what it does.
- **Hypothesis:** For a substantial fraction of published context modules, the accuracy gain over local baselines persists under distant-region scrambling — the gains come from added capacity/regularization, not from the long-range information the papers credit.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** PROTECTED (cheap-to-falsify). The scramble test is a universal, inference-only mechanism-verification instrument for "global context" claims — a reusable audit, not a one-off.

## P4 — PEFT & fine-tuning recipe science (17)

### W5-030 — LLRD explains most of the PEFT advantage
- **CanonicalID:** W5-030  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-A-0055
- **One-liner:** Test the hypothesis that layer-wise learning-rate decay (LLRD) alone accounts for most of the reported benefit of sophisticated PEFT schemes in dense-prediction fine-tuning.
- **Problem:** Many adapter papers compare against naive full FT with uniform LR; LLRD is a strong, cheap baseline that is often missing, potentially inflating PEFT novelty claims.
- **Hypothesis:** Full FT with tuned LLRD comes within 0.5 mIoU of the best PEFT method on ≥70% of standard adaptation benchmarks, at equal compute.
- **Novelty:** UNVERIFIED
- **Protect:** CI+RM
- **Why kept:** Protected CI+RM: one cheap baseline potentially deflating a whole literature.

### W5-031 — One dial: the encoder/decoder LR ratio
- **CanonicalID:** W5-031  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-A-0067
- **One-liner:** Test whether a single scalar — the encoder/decoder learning-rate ratio — explains most variance among PEFT/fine-tuning recipes for promptable segmentation ("the stability–plasticity dial").
- **Problem:** The recipe zoo (freeze this, adapt that) may collapse onto one underlying control variable; if so, the field is over-parameterizing a one-dimensional choice.
- **Hypothesis:** Across recipes, final target-task and retained-generality metrics are predicted (R² > 0.7) by the effective encoder:decoder LR ratio alone, with recipe identity adding <5% explained variance.
- **Novelty:** UNVERIFIED
- **Protect:** HR+RM
- **Why kept:** Protected HR+RM: a radical-simplification claim (R²>0.7 or bust) that reviewers will fight about.

### W5-032 — Strong augmentation + frozen features vs LoRA, matched compute
- **CanonicalID:** W5-032  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-A-0072
- **One-liner:** Run the controlled comparison the field skipped: strong augmentation + frozen features + linear/light decoder vs weak augmentation + LoRA, at matched compute, for dense adaptation.
- **Problem:** Augmentation strength and adaptation method are always co-varied in papers; we don't know how much of PEFT's benefit is reproducible by augmentation with a frozen backbone.
- **Hypothesis:** On ≥50% of small-data segmentation tasks, strong-aug + frozen features matches LoRA + default-aug within 1 mIoU at equal compute, implying much of "adaptation" is invariance injection, not representation change.
- **Novelty:** UNVERIFIED
- **Protect:** RM
- **Why kept:** The controlled factorial the field skipped; verdict reframes "adaptation" as invariance-injection vs representation change.

### W5-033 — Seed variance of PEFT fine-tuning versus reported effect sizes
- **CanonicalID:** W5-033  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-B-0114
- **One-liner:** Measure the cross-seed variance of LoRA/adapter fine-tuning results for segmentation and compare it against the effect sizes typically reported when proposing new PEFT variants.
- **Problem:** PEFT papers report single-seed comparisons on small medical datasets; if seed variance rivals reported gaps, much of the PEFT-variant literature is statistically unsupported.
- **Hypothesis:** Cross-seed standard deviation of standard PEFT fine-tuning on small dense-prediction datasets is of comparable magnitude to typical claimed inter-method differences, and variance grows as dataset size shrinks—exactly where most comparisons are made.
- **Novelty:** UNVERIFIED
- **Protect:** DM
- **Why kept:** A fast-growing literature reports single-seed comparisons on small datasets; the variance audit with minimum-detectable-effect tables sets reporting standards with numbers, not exhortation.

### W5-034 — Attention adapts "where", MLP adapts "what": a causal placement test
- **CanonicalID:** W5-034  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-B-0253
- **One-liner:** Causally test the hypothesis that adapting attention weights primarily corrects spatial-relational errors (grouping, extent) while adapting MLP weights corrects appearance-semantic errors (what counts as target texture), by targeted-placement fine-tuning with error-type-stratified evaluation.
- **Problem:** LoRA placement on attention versus MLP layers is debated with aggregate metrics that cannot see whether the two placements fix different errors—leaving the design question unresolved because it is asked with the wrong instrument.
- **Hypothesis:** Attention-only adaptation disproportionately reduces grouping/extent errors while MLP-only adaptation disproportionately reduces appearance-classification errors (a double dissociation), and the domain's error-type profile therefore predicts optimal placement—explaining contradictory placement findings across prior tasks.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The placement debate is unresolved because it is asked with aggregate metrics — the wrong instrument.

### W5-035 — The boundary tax of parameter efficiency
- **CanonicalID:** W5-035  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-B-0257
- **One-liner:** Test whether PEFT methods that match full fine-tuning on region-level metrics systematically underperform on boundary-localized metrics—a hidden "boundary tax" of constrained adaptation—and identify which constraint geometries avoid it.
- **Problem:** PEFT equivalence claims rest on region-dominated metrics (mIoU, Dice); if constrained updates preferentially sacrifice high-frequency boundary corrections (which plausibly require higher-rank changes), the equivalence is an artifact of metric choice with clinical consequences.
- **Hypothesis:** At matched region metrics, standard low-rank adaptation shows measurable boundary-metric deficits versus full fine-tuning, the deficit scales with boundary-correction spatial frequency (mechanistic link to rank constraints), and boundary-targeted PEFT variants (higher rank in early/high-resolution pathways) eliminate the tax at small parameter cost.
- **Novelty:** UNVERIFIED
- **Protect:** CI·DM
- **Why kept:** Boundary precision is what medical and industrial users pay for; if the tax exists, PEFT equivalence claims systematically overpromise for exactly those users.

### W5-036 — Adapting the choice, not the masks: selection-head-only adaptation for granularity conventions
- **CanonicalID:** W5-036  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-B-0269
- **One-liner:** Test whether adapting only the multimask selection head—which candidate mask to prefer—captures most of the benefit of full adaptation for domains whose conventions differ mainly in granularity (whole-organ versus sub-structure), at near-zero parameter cost.
- **Problem:** Many "domain gaps" in prompted segmentation may actually be convention gaps: the model already generates the right candidate but selects the wrong granularity, and full adaptation wastefully retrains generation to fix a selection problem.
- **Hypothesis:** For convention-type domain gaps (identified by high oracle-candidate performance), selection-head adaptation on tiny label budgets (tens of examples) recovers the majority of the full-adaptation gain, while appearance-type gaps show near-zero selection-only recovery—yielding a cheap diagnostic (oracle-candidate audit) that routes each domain to the right adaptation depth.
- **Novelty:** UNVERIFIED
- **Protect:** CI·CF
- **Why kept:** The oracle-candidate audit is nearly free and could reclassify part of the medical-SAM adaptation literature as selection problems solved with generation-sized tools.

### W5-037 — The input-stem hypothesis for cross-modality transfer
- **CanonicalID:** W5-037  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-B-0270 + IDEA-C-0020  (= MERGE-19)
- **One-liner:** Trainable patch-embedding/stem plus standard PEFT reaches near-full-FT performance for cross-modality transfer; omitting the stem caps performance regardless of adapter rank.
- **Problem:** RGB-pretrained backbones transferred to ultrasound/OCT/X-ray/multispectral may fail primarily at the first nonlinearity rather than in deep semantics, yet stem retraining is scattered folklore with no controlled multi-modality validation.
- **Hypothesis:** For semantics-preserving modality shift, full fine-tuning of only the stem (≤1% of parameters) plus LoRA reaches ≥95% of full-FT performance, while stem-frozen adaptation shows a rank-independent ceiling; a factorial {stem trainable} × {LoRA rank} across ≥4 modality transfers tests the predicted ceiling effect.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Two batches converged on the same folklore-to-law claim (B-0270's interface-vs-semantics split; C-0020's ceiling-effect design); one factorial answers both, with immediate recipe value for the hardest medical transfer setting.

### W5-038 — Capacity as regularization: are small adapters implicitly noise-robust?
- **CanonicalID:** W5-038  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-B-0272
- **One-liner:** Test whether low-capacity PEFT confers implicit robustness to label noise in fine-tuning data—the constrained update cannot fit structured annotation errors—making PEFT strictly preferable to full fine-tuning for noisy medical labels beyond its efficiency benefits.
- **Problem:** Medical fine-tuning data is systematically noisy (rushed annotations, convention mixtures), noise-robust training methods add complexity, and an implicit regularization already present in PEFT would change the cost-benefit of both.
- **Hypothesis:** Under controlled label-noise injection, the PEFT-versus-full-FT performance gap reverses sign as noise increases (full FT fits the noise, low-rank cannot), the protection scales inversely with adapter capacity in a lawful way, and the effect is strongest for spatially structured noise (boundary offsets) that low-rank updates are geometrically unable to express.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Inverts how practitioners frame the efficiency-quality tradeoff exactly where medical labels are noisiest.

### W5-039 — Less rank, more accuracy: the low-rank advantage on tiny datasets
- **CanonicalID:** W5-039  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-B-0306
- **One-liner:** Test the counterintuitive observation that very low LoRA ranks (1–2) sometimes outperform standard ranks (8–16) on tiny fine-tuning datasets, characterizing the capacity-data-size interaction and its implication that rank should scale with data.
- **Problem:** Rank defaults are data-size-agnostic, tiny-dataset fine-tuning is the modal medical scenario, and if minimal-rank updates act as strong implicit regularizers precisely where overfitting risk peaks, current defaults are systematically wrong for the most common regime—but the interaction has never been mapped.
- **Hypothesis:** The optimal-rank-versus-data-size relationship is monotone with a measurable slope (approximately logarithmic), rank-1 dominance below ~20 samples reflects genuine generalization advantage rather than optimization artifact (verifiable by extensive tuning of higher ranks), and a simple rank-selection rule (rank as a function of sample count and shift magnitude) removes the need for per-project search in the low-data regime.
- **Novelty:** UNVERIFIED
- **Protect:** CI·CF
- **Why kept:** Rank defaults are data-size-agnostic while tiny-n fine-tuning is the most common real scenario; a rank-vs-n rule upgrades thousands of projects nearly for free.

### W5-040 — Five percent of elsewhere: out-of-domain data as a superior regularizer
- **CanonicalID:** W5-040  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-B-0315
- **One-liner:** Test the phenomenon that mixing a small fraction (~5%) of unrelated out-of-domain data into fine-tuning outperforms optimally tuned conventional regularization (weight decay, dropout, early stopping) at preventing overfitting on small target datasets.
- **Problem:** Small-data fine-tuning fights overfitting with parameter-space regularizers whose strength is hard to tune, while data-space anchoring (keeping a trickle of diverse data in the mix) may regularize in exactly the directions that matter—preserving general features—yet it is unstudied as a first-class regularization alternative.
- **Hypothesis:** Anchor-data mixing dominates tuned parameter-space regularization on small-target fine-tuning (measured on target and transfer metrics jointly), the mechanism is gradient-subspace anchoring (target gradients are projected against directions that damage general features—verifiable by update-subspace analysis), and the optimal anchor fraction follows a predictable schedule in target-data size—making the method turnkey.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** A simple, turnkey, mechanism-backed regularizer for the modal fine-tuning scenario, with a dominance claim that is cheap to falsify against exhaustively tuned conventional baselines.

### W5-041 — Depth auxiliary vs semantically-empty auxiliary
- **CanonicalID:** W5-041  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-A-0238
- **One-liner:** Test whether auxiliary depth estimation genuinely improves segmentation or whether the reported multi-task benefit is explained by the extra supervision acting as a regularizer replaceable by label-free alternatives.
- **Problem:** Depth-auxiliary gains for segmentation are cited as evidence of geometric synergy; but any auxiliary target correlated with image structure might regularize equally well, and the synergy-vs-regularization question determines whether depth labels are worth acquiring.
- **Hypothesis:** Replacing depth supervision with structurally similar but semantically empty auxiliaries (predicting blurred luminance, or *shuffled-pair* depth) recovers >70% of the multi-task gain — the benefit is generic regularization, falsified if true depth outperforms matched pseudo-auxiliaries.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** The semantically-empty-auxiliary control is a genuinely new instrument applicable to every multi-task synergy claim; depth is just the first target.

### W5-042 — Predict PEFT failure from the spectral structure of the weight update that full…
- **CanonicalID:** W5-042  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-C-0001
- **One-liner:** Predict PEFT failure from the spectral structure of the weight update that full fine-tuning would make.
- **Problem:** LoRA-style methods sometimes match full fine-tuning (FT) and sometimes fail badly, with no accepted pre-hoc predictor of which regime a task falls into.
- **Hypothesis:** PEFT underperforms full FT precisely when the singular-value spectrum of (W_FT − W_pre) is heavy-tailed (effective rank above the adapter rank); tasks with rapidly decaying spectra show no gap.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Turns the PEFT-vs-full-FT choice into a measurable pre-hoc decision rule; a clear falsifiable spectral criterion with broad practical reach across every adaptation deployment.

### W5-043 — Adjudicate whether PEFT failures are capacity failures or optimization failures by giving…
- **CanonicalID:** W5-043  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-C-0011
- **One-liner:** Adjudicate whether PEFT failures are capacity failures or optimization failures by giving PEFT unbounded compute.
- **Problem:** When LoRA lags full FT, papers conclude "insufficient capacity", but LoRA also changes optimization geometry.
- **Hypothesis:** For a substantial fraction of "PEFT-hard" tasks, LoRA at fixed rank closes the gap given 5–10× training length with tuned schedules — implying optimization, not capacity, is the binding constraint.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Clean mechanism adjudication (capacity vs optimization) that changes the remedy for PEFT failures; rare because compute-unbounded PEFT training defeats PEFT's selling point, so nobody runs it.

### W5-044 — Test whether PEFT specifically fails at small-lesion sensitivity because the required…
- **CanonicalID:** W5-044  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-C-0016
- **One-liner:** Test whether PEFT specifically fails at small-lesion sensitivity because the required update lives in high-frequency spatial features.
- **Problem:** Aggregate Dice hides that adaptation methods may differ most on the smallest, most clinically important structures.
- **Hypothesis:** The LoRA-vs-FT sensitivity gap grows as lesion size shrinks (log-linear in lesion diameter), and injecting adapters into the patch-embedding/early conv stem removes the size dependence.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Size-stratified PEFT sensitivity targets the highest-stakes clinical regime (small lesions) with a concrete frequency-localization mechanism and an actionable stem-adapter fix.

### W5-045 — Test the hypothesis that PEFT cannot *unlearn* — tasks requiring suppression of…
- **CanonicalID:** W5-045  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-C-0023
- **One-liner:** Test the hypothesis that PEFT cannot *unlearn* — tasks requiring suppression of misleading pretrained features need full FT.
- **Problem:** Some transfers require actively removing a pretrained cue (e.g., texture bias harmful for modality X); additive low-rank updates may be poor at suppression.
- **Hypothesis:** On tasks constructed so that a known pretrained cue is anti-correlated with the target label, the LoRA-vs-FT gap is large and grows with the cue's pretrained salience, while on cue-neutral controls the gap vanishes.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR
- **Why kept:** PROTECTED (high-risk/high-reward). The add-vs-suppress asymmetry would define a principled "must-full-FT" task class; counter-intuitive, theory-adjacent, and directly relevant to shortcut-ridden medical datasets.

### W5-046 — Bias-variance decomposition of PEFT vs full fine-tuning
- **CanonicalID:** W5-046  ·  **Cluster:** P4 — PEFT & fine-tuning recipe science
- **SourceIDs:** IDEA-A-0052
- **One-liner:** Quantify the bias-variance decomposition of PEFT vs full fine-tuning across random seeds: is PEFT's advantage on small data mostly variance reduction?
- **Problem:** PEFT beats full FT on small datasets, attributed vaguely to "regularization"; a formal seed-level bias-variance decomposition would identify the mechanism.
- **Hypothesis:** Across 20 seeds, PEFT shows ≥3× lower seed variance but *higher* bias (worse best-seed performance) than full FT; the mean gap is explained primarily by the variance term at n<500 images and flips sign as n grows.
- **Novelty:** UNVERIFIED
- **Protect:** REV · M
- **Why kept:** Auditor revive (stage2_audit.md §5): Revive at reduced scope (2 datasets × 3 sizes × 10 seeds ≈ 120 runs) and **share the grid with B-0114** (PEFT seed variance, survivor), which already budgets 10 seeds × 4 methods × 4 sizes — the marginal cost of the decomposition on top of B-0114's runs is near zero.

## P5 — Forgetting, retention & update geometry (9)

### W5-047 — The gain/retention frontier: is forgetting unforced error?
- **CanonicalID:** W5-047  ·  **Cluster:** P5 — Forgetting, retention & update geometry
- **SourceIDs:** IDEA-A-0076 + IDEA-B-0248  (= MERGE-07)
- **One-liner:** One LR × components × steps × rank sweep with matched-target checkpoint selection traces the gain/retention Pareto frontier, places published recipes inside it, and fits retention-vs-effective-rank laws.
- **Problem:** SAM fine-tunes report target gains without measuring generality loss; the community lacks even a descriptive account of the trade-off's shape, let alone whether existing recipes are efficient.
- **Hypothesis:** The gain/retention frontier is strongly concave (large retention is nearly free up to a knee), and ≥70% of common recipes (full FT, decoder-only, LoRA at default LR) sit >10 retention points inside the frontier — i.e., forgetting in practice is mostly unforced error.
- **Novelty:** UNVERIFIED
- **Protect:** RM / DM
- **Why kept:** Same frontier, same infrastructure; B's matched-target checkpoint selection is exactly the confound control A's frontier estimate needs. Infrastructure spine of the adaptation-science program.

### W5-048 — Forgetting is mostly readout drift
- **CanonicalID:** W5-048  ·  **Cluster:** P5 — Forgetting, retention & update geometry
- **SourceIDs:** IDEA-A-0078 + IDEA-C-0034  (= MERGE-20)
- **One-liner:** Probe frozen features of 'forgotten' models to decompose catastrophic forgetting into feature loss vs readout loss; linear re-probing may recover most 'lost' zero-shot dense performance.
- **Problem:** Continual-learning methods assume fine-tuning destroys representations, but the lost capability may remain linearly decodable — the field has not separated feature erasure from readout misalignment for dense tasks.
- **Hypothesis:** Lightweight re-probing of fine-tuned encoders recovers most of the zero-shot dense performance lost to fine-tuning; the recoverable fraction is large for short adaptations and shrinks with update depth — falsified if features are truly erased and re-probing recovers little.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Cross-batch convergence (A's re-probing claim; C-0034's feature-vs-readout decomposition); if capabilities remain decodable, continual learning's objective changes from preserving weights to preserving readouts.

### W5-049 — Forgetting hysteresis: suppression, not erasure
- **CanonicalID:** W5-049  ·  **Cluster:** P5 — Forgetting, retention & update geometry
- **SourceIDs:** IDEA-A-0089 + IDEA-C-0040  (= MERGE-21)
- **One-liner:** 'Forgotten' capabilities are suppressed, not erased: tiny rewinding/re-exposure sets restore them at a few percent of original cost, with measurable time-constants that define cheap refresh schedules.
- **Problem:** If forgetting is retrieval failure rather than erasure, expensive continual-learning machinery could be replaced by scheduled refreshes — but restoration-cost curves and their time-constants have never been mapped for dense models.
- **Hypothesis:** Brief re-exposure to a small fraction of old data restores most suppressed performance at ~5% of original training cost, with restoration cost growing along a measurable hysteresis curve in time-since-forgetting — falsified if restoration requires near-full retraining.
- **Novelty:** UNVERIFIED
- **Protect:** HR
- **Why kept:** Cross-batch convergence on suppression-vs-erasure (A's hysteresis time-constants; C-0040's rewinding-set test); HR-protected — a positive result replaces CL machinery with refresh schedules.

### W5-050 — Low-rank adaptation amplifies shortcuts
- **CanonicalID:** W5-050  ·  **Cluster:** P5 — Forgetting, retention & update geometry
- **SourceIDs:** IDEA-A-0058 + IDEA-B-0260  (= MERGE-08)
- **One-liner:** Low-rank updates can only reweight existing (often spurious) directions: worst-group degradation on constructed spurious correlations plus sharper site-fingerprint encoding on natural hospital shifts, rank sweep as the mechanism test.
- **Problem:** Low-rank updates can only reweight existing feature directions; if the strongest existing directions are spurious (backgrounds, textures), LoRA may amplify shortcut reliance — an unexamined safety issue.
- **Hypothesis:** On datasets with known spurious correlations (backgrounds correlated with class), LoRA-adapted segmenters show larger worst-group degradation than full FT at matched in-distribution accuracy.
- **Novelty:** UNVERIFIED
- **Protect:** HR+CI / CI·DM
- **Why kept:** Identical claim and mechanism generated in both batches, with synthetic and natural instantiations; a safety-critical inversion of PEFT folklore. In productive tension with B-0272 (CONF-1).

### W5-051 — Predicting adapter-merging success from task-vector geometry
- **CanonicalID:** W5-051  ·  **Cluster:** P5 — Forgetting, retention & update geometry
- **SourceIDs:** IDEA-B-0251
- **One-liner:** Test whether the success of merging multiple dataset-specific LoRAs into one (versus training jointly) is predictable from the geometry of their updates (subspace angles, task-vector cosines), enabling merge-or-retrain decisions without trial training.
- **Problem:** Organizations accumulate per-dataset adapters and want consolidated models, but merging sometimes works and sometimes collapses—with no predictive theory, every consolidation is a gamble.
- **Hypothesis:** Merge degradation correlates strongly with inter-adapter subspace interference (principal angles between update subspaces weighted by singular values), the predictor computed from adapter weights alone forecasts merge quality within useful tolerance, and interference-guided merging (orthogonalization before averaging) recovers most losses in the risky regime.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Adapter consolidation is a routine operational need currently decided by trial and error; a validated weight-space predictor makes it a calculation.

### W5-052 — Benchmark sequential-checkpoint weight averaging as a nearly-free anti-forgetting…
- **CanonicalID:** W5-052  ·  **Cluster:** P5 — Forgetting, retention & update geometry
- **SourceIDs:** IDEA-C-0050
- **One-liner:** Benchmark sequential-checkpoint weight averaging as a nearly-free anti-forgetting baseline that may beat dedicated CL methods.
- **Problem:** CL literature compares against weak naive baselines; simple weight averaging across domain checkpoints is rarely in the comparison set.
- **Hypothesis:** Uniform or Fisher-weighted averaging of per-domain fine-tuned checkpoints attains lower average forgetting than EWC and matches modest replay on cross-site medical segmentation — at zero training-time overhead.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** PROTECTED (simple counter-intuitive). Checkpoint weight averaging as a continual-learning baseline: if a trivial zero-overhead method beats EWC and matches replay, the field's method complexity is unjustified.

### W5-053 — Quantify cumulative "TTA drift": continuously running test-time adaptation in deployment…
- **CanonicalID:** W5-053  ·  **Cluster:** P5 — Forgetting, retention & update geometry
- **SourceIDs:** IDEA-C-0056
- **One-liner:** Quantify cumulative "TTA drift": continuously running test-time adaptation in deployment causes progressive forgetting.
- **Problem:** TTA methods (entropy minimization, statistics updates) are evaluated per-batch; deployed continuously, their updates compound without any consolidation mechanism.
- **Hypothesis:** Under a realistic stream (site mixture with rare-case bursts), continuous TTA degrades monotonically on a frozen reference set, with drift rate proportional to stream non-stationarity; periodic parameter resets trade recent-gain for drift elimination at a measurable exchange rate.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** PROTECTED (counter-intuitive, deployment-critical). Continuous test-time adaptation as a "slow poison" is a quantitative drift law the field urgently needs as TTA moves into deployed systems.

### W5-054 — Disentangle true representational forgetting from annotation-protocol mismatch when… [E]
- **CanonicalID:** W5-054  ·  **Cluster:** P5 — Forgetting, retention & update geometry
- **SourceIDs:** IDEA-C-0057
- **One-liner:** Disentangle true representational forgetting from annotation-protocol mismatch when measuring cross-site "forgetting".
- **Problem:** Old-site performance drops after adaptation may partly reflect that the new site's *label style* was learned — a labeling artifact, not knowledge loss.
- **Hypothesis:** Re-annotating a small old-site subset under the new site's protocol reduces measured "forgetting" by a substantial fraction (>30%) in protocol-divergent dataset pairs, and by ~0% in protocol-matched pairs.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Separates annotation-protocol artifact from true representational forgetting — measurement repair that could shrink the field's headline phenomenon by a third.

### W5-055 — Subgroup regression under fine-tuning: who loses when the average improves?
- **CanonicalID:** W5-055  ·  **Cluster:** P5 — Forgetting, retention & update geometry
- **SourceIDs:** IDEA-B-0286
- **One-liner:** Systematically test whether fine-tuning that improves average performance regresses identifiable subgroups (rare acquisition settings, atypical anatomy, minority demographics) below the zero-shot baseline—making the pre-fine-tuning model strictly better for some patients.
- **Problem:** Fine-tuning decisions are made on aggregate metrics, subgroup regressions would be clinically and ethically material, and the zero-shot-versus-fine-tuned comparison at subgroup granularity is simply not part of current adaptation practice.
- **Hypothesis:** Fine-tuning on realistically skewed target data produces measurable subgroup regressions relative to zero-shot in a substantial fraction of adaptation runs (the adapted model trades tail robustness inherited from web-scale pretraining for target-majority fit), regressions concentrate in subgroups underrepresented in fine-tuning data relative to pretraining, and lightweight interpolation between base and adapted weights recovers most subgroup loss at minor average cost.
- **Novelty:** UNVERIFIED
- **Protect:** REV · M
- **Why kept:** Auditor revive (stage2_audit.md §5): Killed because the mechanism "is documented for classification" — but the dense/medical instantiation with the do-no-harm framing is precisely the kind of consequential port the pool keeps elsewhere (e.g., A-0242 ports z-curves from psychology).

## P6 — Domain shift, TTA & continual deployment (11)

### W5-056 — The UDA reality audit
- **CanonicalID:** W5-056  ·  **Cluster:** P6 — Domain shift, TTA & continual deployment
- **SourceIDs:** IDEA-A-0296 + IDEA-B-0064  (= MERGE-05)
- **One-liner:** Published UDA methods on fresh adaptation pairs (frozen + bounded-retuning) against source-only and frozen-foundation baselines at matched compute; ranking transfer and marginal value per shift regime.
- **Problem:** UDA method development has iterated on the same few pairs for years; the methods' hyperparameters and design choices may be benchmark-pair-specific, making the literature's reported ordering meaningless for new deployments — the overfitting-to-the-pair magnitude is unmeasured.
- **Hypothesis:** On 4 novel adaptation pairs, the published UDA method ranking scrambles (rank correlation < 0.4 with GTA→Cityscapes ordering) and the average gain over source-only baselines shrinks by >50% — the field has been fitting the benchmark, falsified if rankings and gains transfer.
- **Novelty:** UNVERIFIED
- **Protect:** RM / DM
- **Why kept:** Two deflationary UDA audits with ~80% identical experimental grids; strictly stronger run together — ranking transfer plus marginal value over foundation baselines in one matched-compute grid. Decision-grade for post-2026 segmentation DA.

### W5-057 — Token/norm-statistics recalibration: TTA method + shift-tier diagnostic
- **CanonicalID:** W5-057  ·  **Cluster:** P6 — Domain shift, TTA & continual deployment
- **SourceIDs:** IDEA-A-0303 + IDEA-B-0057  (= MERGE-06)
- **One-liner:** Per-layer token-statistics matching for ViTs evaluated twice: as an optimization-free TTA method and as a minutes-cheap instrument whose recovery fraction routes shifts to norm-stats / PEFT / full-UDA tiers.
- **Problem:** The most reliable classic TTA trick—updating BN statistics—has no ViT equivalent, since LayerNorm carries no cross-sample statistics; ViT-era dense TTA lacks a comparably simple mechanism.
- **Hypothesis:** Domain shift manifests as measurable drift in token-population statistics at specific layers, and matching those statistics to source values via affine token corrections recovers a meaningful fraction of the shift loss without labels.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** A-0303 explicitly asks for the LayerNorm-era analog of BN-statistics TTA; B-0057 is that analog — one measurement operation, two readouts (method + diagnostic). Highest immediate-adoption probability in the pool.

### W5-058 — Which domain-distance metric actually predicts fine-tuning gain?
- **CanonicalID:** W5-058  ·  **Cluster:** P6 — Domain shift, TTA & continual deployment
- **SourceIDs:** IDEA-B-0054
- **One-liner:** Benchmark candidate domain-distance measures (FID in various feature spaces, MMD, spectral divergences, token-distribution shifts) as predictors of how much a foundation segmenter will gain from fine-tuning on a target domain.
- **Problem:** Practitioners need to predict, before annotating, whether fine-tuning will pay off; distance metrics are used informally without validation against realized gains.
- **Hypothesis:** Distances computed in the segmenter's own mid-layer token space predict fine-tuning gain markedly better than generic FID/MMD, because gain depends on mismatch as seen by this model, not any model.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Turns adaptation planning into a pre-annotation measurement, validated against realized gains rather than proxy shift labels.

### W5-059 — Amplitude-only adaptation: testing the "shift is style" hypothesis with Fourier-space adapters
- **CanonicalID:** W5-059  ·  **Cluster:** P6 — Domain shift, TTA & continual deployment
- **SourceIDs:** IDEA-B-0072
- **One-liner:** Constrain all trainable adaptation to a global Fourier amplitude filter and measure how much of various domain gaps this single interpretable component can close, upper-bounding the "style" content of each shift.
- **Problem:** The folk claim that scanner/site shifts are mostly "style" has never been operationalized as a capacity-constrained, interpretable test.
- **Hypothesis:** For scanner and site shifts, an amplitude-only adapter closes the majority of the gap, while for cross-modality or cross-anatomy shifts it closes little, yielding a quantitative style-fraction per shift type.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Turns folklore ("site shift is style") into a cheap standard diagnostic with a number attached.

### W5-060 — Language as a domain coordinate: text-described domains for zero-shot adaptation
- **CanonicalID:** W5-060  ·  **Cluster:** P6 — Domain shift, TTA & continual deployment
- **SourceIDs:** IDEA-B-0078
- **One-liner:** Test whether natural-language descriptions of a target domain ("underwater, greenish turbidity, particulate backscatter") can condition a segmenter's adaptation—via text-derived feature modulation—without any target images.
- **Problem:** Some deployment domains have no data at all before launch (new camera sites, rare modalities), leaving no adaptation signal except human knowledge of the domain.
- **Hypothesis:** Domains occupy a partially language-describable manifold: text-conditioned modulation recovers a meaningful fraction of the gap that image-conditioned adaptation achieves, and the recoverable fraction correlates with how "describable" the shift is (style vs content).
- **Novelty:** UNVERIFIED
- **Protect:** HRHR — protected
- **Why kept:** Either opens a zero-data adaptation channel or measures the limit of language-vision domain alignment — both outcomes are valuable, and the question is basic science about VLM geometry, not a product pitch.

### W5-061 — Label-free PEFT: distilling prompt-ensemble consensus into adapters
- **CanonicalID:** W5-061  ·  **Cluster:** P6 — Domain shift, TTA & continual deployment
- **SourceIDs:** IDEA-B-0279
- **One-liner:** Adapt segmentation models to new domains without any labels by distilling the consensus of prompt-perturbation ensembles (the base model's own agreement structure on unlabeled target data) into a lightweight adapter, and measure how close label-free PEFT gets to supervised PEFT.
- **Problem:** Most deployment domains have unlabeled data in abundance and labels not at all; existing unsupervised adaptation either drifts (self-training) or under-delivers (feature alignment), while promptable models contain an internal consistency signal that has not been harnessed for weight adaptation.
- **Hypothesis:** Prompt-consensus pseudo-labels are systematically more reliable than confidence-filtered standard pseudo-labels on shifted data (agreement across prompts filters shift-induced instability), so consensus-distilled adapters recover a meaningful fraction of supervised-PEFT gains with near-zero collapse risk, quantifiable as a fraction-of-supervised-gain metric across shift types.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The consistency anchor is structurally harder to game than entropy, addressing TTA's collapse problem at its root.

### W5-062 — Entropy TTA silently collapses rare classes
- **CanonicalID:** W5-062  ·  **Cluster:** P6 — Domain shift, TTA & continual deployment
- **SourceIDs:** IDEA-A-0239
- **One-liner:** Audit entropy-minimization test-time adaptation (TENT-class) on segmentation for silent class collapse, and characterize the conditions (class imbalance, shift type) that trigger it.
- **Problem:** TTA methods validated on classification are applied to segmentation, where entropy minimization can collapse rare classes into dominant ones while *improving* average metrics — a dangerous failure whose triggering conditions are unmapped.
- **Hypothesis:** On class-imbalanced segmentation under shift, entropy-based TTA improves mIoU while reducing rare-class IoU by >30% relative in a predictable fraction of cases, with collapse probability rising with batch-level class skew — average metrics actively hide the harm, falsified if rare-class performance tracks average gains.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Safety-relevant hidden harm (averages improve while rare classes die) with predictive triggers; inference-scale cost.

### W5-063 — Style leaks through skips: do skip connections undermine cross-domain robustness?
- **CanonicalID:** W5-063  ·  **Cluster:** P6 — Domain shift, TTA & continual deployment
- **SourceIDs:** IDEA-B-0304
- **One-liner:** Test the phenomenon that removing or bottlenecking encoder-decoder skip connections sometimes improves cross-domain segmentation—evaluating whether skips pipe domain-specific low-level statistics (style) directly into predictions, bypassing the domain-invariant deep pathway.
- **Problem:** Skip connections are unquestioned dense-architecture dogma for boundary precision, but they structurally exempt low-level features from the abstraction that confers invariance—if style leaks through skips, the field's default architecture trades robustness for sharpness without anyone measuring the exchange rate.
- **Hypothesis:** Skip-carried features encode domain identity far more strongly than bottleneck features (probeable), cross-domain degradation is disproportionately attributable to skip pathways (verifiable by skip-ablation and skip-swap interventions), and style-normalized skips (instance-normalized or spectrally filtered) retain boundary precision while removing most of the leaked fragility—breaking the assumed tradeoff.
- **Novelty:** UNVERIFIED
- **Protect:** CI·DM
- **Why kept:** Indicts the most standard dense-architecture component with a three-step causal design (pathway probing, ablation/swap, normalized-skip rescue).

### W5-064 — Night vision: adaptation gap or information deficit
- **CanonicalID:** W5-064  ·  **Cluster:** P6 — Domain shift, TTA & continual deployment
- **SourceIDs:** IDEA-A-0305
- **One-liner:** Determine whether night-time segmentation is a domain-adaptation problem or an information-deficit problem, by measuring the human ceiling on the same night imagery models fail on.
- **Problem:** Night segmentation is framed as domain shift (fixable by adaptation), but low-light imagery may simply lack the information — in which case adaptation research chases an impossible target and sensor-side solutions (exposure, NIR) are the answer; the framing has never been tested against a human ceiling.
- **Hypothesis:** On standard night benchmarks, human segmentation (with unlimited time, contrast tools allowed) exceeds the best adapted models by >15 mIoU on structure-rich classes but matches models on severely underexposed regions — the gap decomposes into a recoverable adaptation component and a hard information floor, mapped per region, falsified if humans match models everywhere (pure information deficit) or exceed everywhere (pure adaptation gap).
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Counter-intuitive framing flip: the field assumes night is an adaptation problem; this measures whether the target is even achievable.

### W5-065 — Test histogram matching as a domain-adaptation baseline: if intensity alignment closes…
- **CanonicalID:** W5-065  ·  **Cluster:** P6 — Domain shift, TTA & continual deployment
- **SourceIDs:** IDEA-C-0325
- **One-liner:** Test histogram matching as a domain-adaptation baseline: if intensity alignment closes most of the cross-site gap, complex DA methods are solving an already-solved problem.
- **Problem:** Domain-adaptation papers for medical imaging rarely include the cheapest classical baseline — per-image intensity histogram alignment — leaving their headroom claims unanchored.
- **Hypothesis:** Histogram matching (plus nothing) recovers a majority of the cross-site performance drop on standard medical DA benchmarks, and published DA methods' gains shrink to marginal once applied on top of it — the benchmarks primarily measure intensity shift.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** PROTECTED (cheap-to-falsify). Histogram matching as the missing classical domain-adaptation baseline: an hour of preprocessing that could reframe the difficulty claims of a benchmark literature.

### W5-066 — Continual adaptation under cyclically returning domains
- **CanonicalID:** W5-066  ·  **Cluster:** P6 — Domain shift, TTA & continual deployment
- **SourceIDs:** IDEA-A-0301
- **One-liner:** Study continual adaptation under *cyclically returning* domains (day/night, seasons, weather) and test whether current continual-DA methods oscillate — repeatedly re-learning and forgetting each phase — instead of consolidating a cycle-covering solution.
- **Problem:** Real deployment shift is largely cyclic, not a linear sequence of novel domains, but continual-DA is evaluated on linear sequences; whether methods exploit recurrence (consolidate) or thrash (re-adapt every cycle, accumulating damage) is unknown.
- **Hypothesis:** Standard continual-DA methods show non-decreasing re-adaptation cost across repeated cycles (no consolidation), while an explicit phase-memory design converges to near-zero re-adaptation by cycle 3 — current methods waste the structure of recurrence, falsified if standard methods naturally consolidate.
- **Novelty:** UNVERIFIED
- **Protect:** REV · M
- **Why kept:** Auditor revive (stage2_audit.md §5): Killed on data-assembly weight, but day/night/weather cycles are recoverable from existing time-stamped driving corpora (BDD100k-class) plus the synthetic-cycle control the idea itself proposes.

## P7 — Language–vision grounding & dense-VLM failure modes (19)

### W5-067 — Does chain-of-thought causally change grounding?
- **CanonicalID:** W5-067  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-A-0041
- **One-liner:** Test whether chain-of-thought style reasoning text actually changes *where* VLMs ground (attention/mask placement) or only changes the verbal rationale while grounding stays fixed.
- **Problem:** Reasoning-segmentation systems assume intermediate reasoning improves localization, but reasoning could be post-hoc rationalization with grounding determined by the visual pathway alone.
- **Hypothesis:** For referring segmentation with reasoning-capable VLMs, forcing incorrect-but-plausible reasoning chains changes final masks in <15% of cases — grounding is causally insensitive to the reasoning text.
- **Novelty:** UNVERIFIED
- **Protect:** HR+CI
- **Why kept:** Protected HR+CI: a causal intervention with a mask endpoint that either crowns or kills "reasoning segmentation" — a growing subfield betting on the assumption this idea tests.

### W5-068 — Negation: worse than chance, a fusion failure
- **CanonicalID:** W5-068  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-A-0187
- **One-liner:** Measure whether referring segmentation models process negation ("the cup that is not red") above chance, and whether failures are text-encoding or vision-grounding failures.
- **Problem:** Negation is frequent in natural instructions but suspected to be ignored by VLMs; for segmentation, negation failure produces exactly-wrong outputs (the negated object), which is worse than random — the failure severity and locus are unmeasured.
- **Hypothesis:** On negated referring expressions with two-candidate scenes, models select the *negated* (wrong) object above 50% (systematic anti-accuracy, worse than chance), and text-embedding probes show negation is representable but unused by the grounding head — a fusion failure, not an encoding failure.
- **Novelty:** UNVERIFIED
- **Protect:** CI+CF
- **Why kept:** Anti-accuracy (worse than random) is a qualitatively different and scarier claim than "models ignore negation"; the encoding-vs-fusion attribution gives it a locatable cause.

### W5-069 — Spatial-relation minimal pairs near chance
- **CanonicalID:** W5-069  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-A-0183
- **One-liner:** Isolate spatial-relation reasoning ("left of", "behind", "between") as the failure locus in referring expression segmentation via minimal-pair expressions that differ only in the relation.
- **Problem:** Referring segmentation errors conflate category recognition, attribute binding, and spatial reasoning; without isolation, methods "improve" without knowing which capability moved — and spatial relations are suspected to be near-chance.
- **Hypothesis:** On minimal pairs where only the spatial relation disambiguates the target, current referring-segmentation models perform <15 points above chance, with egocentric relations ("left of") worse than intrinsic ones ("on top of") — spatial language is largely unused by the grounding pathway.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Tests the core value proposition of language-guided segmentation with minimal pairs — the cleanest isolation design available.

### W5-070 — The absent-target hallucination benchmark
- **CanonicalID:** W5-070  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-A-0185 + IDEA-B-0241  (= MERGE-02)
- **One-liner:** One benchmark crossing {present / absent-plausible / absent-implausible} targets with a prompt-assertiveness ladder; mask-emission rates, confidence, spatial targeting of hallucinated masks, and refusal protocols at fixed sensitivity.
- **Problem:** Text-prompted segmenters are rarely tested with prompts for absent objects; deployment (e.g., "segment the tumor", "find the pedestrian") requires calibrated refusal, and hallucinated masks are the silent worst case.
- **Hypothesis:** Current OV/referring segmenters produce above-threshold masks for absent-but-scene-plausible objects in >40% of cases (vs <10% for implausible ones), with hallucination targeting the most co-occurrence-typical scene regions — hallucination is a scene-prior readout, predictable from context.
- **Novelty:** UNVERIFIED
- **Protect:** CF+RM / CI·CF
- **Why kept:** Identical dependent variable (mask emission on certified-absent images) generated in both batches; the plausibility gradient and assertiveness ladder are two axes of one design; makes refusal a first-class metric before deployment norms solidify.

### W5-071 — Scene text hijacks grounding
- **CanonicalID:** W5-071  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-A-0199
- **One-liner:** Measure interference from scene text (signs, labels, watermarks) on VLM grounding: does written text in images hijack text-prompted segmentation toward regions containing matching words?
- **Problem:** VLMs read scene text; a prompt for "stop" may ground to a stop sign's *text* rather than the requested object concept, and adversarial or incidental text may hijack masks — an interference channel unquantified for dense prediction.
- **Hypothesis:** Planting prompt-matching scene text shifts grounding to the text region in >30% of cases for OCR-capable VLMs (and near 0% for CLIP-class models without strong OCR), with hijack probability scaling with text size — grounding inherits typographic-attack vulnerability in proportion to OCR capability.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Extends typographic attacks to masks with a capability-scaling law (hijack ∝ OCR ability) — a predictive, not merely demonstrative, security result.

### W5-072 — CLIP dense misalignment is co-occurrence-structured
- **CanonicalID:** W5-072  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-A-0181
- **One-liner:** Audit patch-level image-text alignment in CLIP-style models to establish *why* global contrastive training produces spatially misaligned dense features, and quantify the misalignment's structure.
- **Problem:** CLIP features are repurposed for segmentation despite training only for global alignment; the known "noisy dense features" problem lacks a structural characterization (is misalignment random, object-boundary-concentrated, or background-leaking?), which any fix implicitly assumes.
- **Hypothesis:** CLIP patch-text similarity systematically leaks object scores into co-occurring background regions (measurable as background-context activation exceeding object activation for >20% of classes), and the leak strength per class correlates with caption co-occurrence statistics — misalignment is co-occurrence-structured, not random noise.
- **Novelty:** UNVERIFIED
- **Protect:** — (merit)
- **Why kept:** Structural characterization that every OV-segmentation fix implicitly assumes; the co-occurrence regression gives it a mechanism and per-class failure predictions.

### W5-073 — Text-space collinearity predicts open-vocabulary confusion for amorphous classes
- **CanonicalID:** W5-073  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-B-0124
- **One-liner:** Test whether the near-collinearity of related concept embeddings in CLIP text space ("smoke", "steam", "fog", "haze") predicts—and upper-bounds—visual discrimination performance of open-vocabulary segmenters on those classes.
- **Problem:** Open-vocab models fail to separate visually distinct but linguistically adjacent phenomena, and it is unknown whether the bottleneck is the visual encoder or the text anchor geometry.
- **Hypothesis:** Per-class-pair confusion rates correlate strongly with text-embedding cosine similarity even after controlling for visual similarity, and replacing text anchors with visually derived anchors breaks the ceiling—localizing the failure to text-space geometry.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Localizes a safety-critical confusion to a specific, fixable component (text anchors vs visual encoder), redirecting effort from data collection to anchor engineering.

### W5-074 — Prompt paraphrase variance and prompt-averaged leaderboards [E]
- **CanonicalID:** W5-074  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-A-0031 + IDEA-C-0067  (= MERGE-22)
- **One-liner:** Paraphrase variance in open-vocabulary segmentation exceeds reported SOTA gaps; re-estimate leaderboards with prompt-resampled confidence intervals and ranking-stability statistics.
- **Problem:** Open-vocab results are reported under a single prompt phrasing per class although reasonable paraphrases shift scores at SOTA-gap scale — leaderboard orderings may be prompt-sampling noise.
- **Hypothesis:** Across reasonable paraphrase sets, per-method score variance exceeds the median inter-method gap on standard benchmarks, and prompt-averaged confidence intervals reorder published rankings — falsified if rankings are stable under prompt resampling.
- **Novelty:** UNVERIFIED
- **Protect:** CF+RM
- **Why kept:** Cross-batch convergence (A's paraphrase-variance claim; C-0067's prompt-averaged CI repair); an inference-only statistical repair of an entire leaderboard genre.

### W5-075 — Prompt-specificity inverse-U (basic-level optimum)
- **CanonicalID:** W5-075  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-A-0033
- **One-liner:** Map the relationship between lexical specificity of the prompt ("vehicle" → "car" → "sedan" → "2012 Toyota Camry") and segmentation quality, testing for a non-monotonic optimum.
- **Problem:** Users assume more specific prompts are better; but rare specific terms are poorly represented in text encoders, suggesting an interior optimum of specificity.
- **Hypothesis:** Segmentation IoU vs specificity level is inverse-U shaped, with the optimum at basic-level categories (in the Rosch sense), and the drop for over-specific prompts correlates with term frequency in pretraining corpora.
- **Novelty:** UNVERIFIED
- **Protect:** CI+CF
- **Why kept:** Counter-intuitive (more specific ≠ better), theory-connected (Rosch basic-level), mechanism-bearing (frequency mediation), and inference-only.

### W5-076 — Lay vs expert terminology for medical grounding
- **CanonicalID:** W5-076  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-A-0049
- **One-liner:** Test whether expert medical terminology or lay descriptions prompt medical VLM segmentation better — the "vocabulary register mismatch" question.
- **Problem:** Medical VLMs are prompted with expert terms ("pneumothorax") though their web-scale pretraining likely contains far more lay language ("collapsed lung"); the optimal register is unknown.
- **Hypothesis:** For general-domain VLMs applied to medical grounding, lay-term prompts outperform expert terms by >5 IoU on average, and the gap reverses for models pretrained on biomedical literature (PubMed-scale corpora).
- **Novelty:** UNVERIFIED
- **Protect:** CI+CF
- **Why kept:** Free performance lever plus a text-tower diagnostic, with a predicted interaction (general vs biomedical pretraining) that makes the design self-controlling.

### W5-077 — Where do VLMs lose spatial detail? Layer-wise localization decay in vision-language models
- **CanonicalID:** W5-077  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-B-0132
- **One-liner:** Trace the layer-by-layer decay of pixel-localizable information in LLaVA-style VLMs to identify precisely where dense-prediction capacity is destroyed by token pooling and language-alignment stages.
- **Problem:** VLMs are being asked to ground, point, and segment, but their architecture compresses spatial detail at unidentified stages—without a decay map, dense-VLM design is guesswork.
- **Hypothesis:** Localization information (probed per layer as boundary recovery) collapses sharply at identifiable bottlenecks (projector, resampler) rather than gradually through the language model, implying that dense capability can be restored with taps at pre-collapse layers rather than architectural overhauls.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Dense-capable VLMs are being built now on intuition; this replaces it with a decay map and validated tap points.

### W5-078 — Does text supervision smooth away boundary precision? The semantic-blur hypothesis
- **CanonicalID:** W5-078  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-B-0174
- **One-liner:** Test whether adding language supervision to segmentation training systematically degrades boundary precision (language groups pixels semantically, not photometrically), quantifying a boundary-semantics tradeoff in multimodal training.
- **Problem:** Language-supervised dense models are celebrated for semantic flexibility, but language never specifies boundaries, and its training pressure may actively blur them—an unmeasured cost side of the multimodal ledger.
- **Hypothesis:** At matched region-level accuracy, models with heavier language supervision show measurably worse boundary-localized metrics, the degradation grows with text-loss weight in a dose-dependent way, and boundary-specific auxiliary supervision eliminates the tradeoff—demonstrating it is an objective-design artifact, not an inherent cost.
- **Novelty:** UNVERIFIED
- **Protect:** CI·DM
- **Why kept:** Names the unmeasured cost side of the rush toward language-native dense models, with a falsifiable dose-response and a proposed remedy (boundary auxiliaries) that turns critique into design guidance.

### W5-079 — Knowledge conflict in VLM segmenters: when text priors contradict image evidence
- **CanonicalID:** W5-079  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-B-0185
- **One-liner:** Construct controlled conflicts between linguistic anatomical priors ("the liver is homogeneous") and image evidence (nodular cirrhotic liver) to measure which source dense VLMs trust, and whether the arbitration is calibrated to evidence strength.
- **Problem:** Language-supervised dense models import textual world knowledge whose priors can contradict individual images—the arbitration behavior is unknown but determines safety on atypical (i.e., diseased) cases, which are exactly the cases that matter.
- **Hypothesis:** Dense VLMs systematically over-trust text priors when image evidence is degraded (noise, low contrast), producing prior-conforming segmentations of atypical anatomy, and the over-trust is measurable as miscalibrated evidence weighting that worsens with language-model scale.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR·DM — protected
- **Why kept:** "Prior-conforming segmentation of abnormal anatomy" is the worst conceivable medical-VLM failure mode and is untested.

### W5-080 — Quantify "global leakage": how much of each CLIP patch token's content is image-level…
- **CanonicalID:** W5-080  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-C-0061
- **One-liner:** Quantify "global leakage": how much of each CLIP patch token's content is image-level semantics rather than local content.
- **Problem:** Contrastive image-text training optimizes a global objective; patch tokens may become carriers of global information, corrupting their use for dense prediction.
- **Hypothesis:** Mutual information between a patch token and the image-level label exceeds that between the token and its own receptive-field content in late CLIP layers, and the leakage ratio predicts zero-shot segmentation failure per layer.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Information-theoretic measurement of "global leakage" supplies the mechanism behind naive CLIP dense-readout failure plus a practical per-layer readout-selection instrument.

### W5-081 — Build a text-only baseline audit for referring segmentation: how often is the mask…
- **CanonicalID:** W5-081  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-C-0072
- **One-liner:** Build a text-only baseline audit for referring segmentation: how often is the mask predictable without looking at the image?
- **Problem:** Referring-expression datasets contain language priors ("the sky", "the left man") that let models score without genuine cross-modal grounding.
- **Hypothesis:** A model given only the text (plus dataset-level mask statistics) achieves a nontrivial fraction of reported referring-segmentation performance, and per-sample text-predictability correlates with where published models succeed — indicating prior exploitation rather than grounding.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR
- **Why kept:** PROTECTED (high-risk/high-reward). The text-only referring-segmentation baseline audits the central grounding claim of an entire subfield; the VQA language-prior audit transplanted to dense prediction, overdue and cheap.

### W5-082 — Show that report-supervised medical VLMs align to reporting style — including pervasive…
- **CanonicalID:** W5-082  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-C-0076
- **One-liner:** Show that report-supervised medical VLMs align to reporting style — including pervasive negations — and that negation breaks their dense grounding.
- **Problem:** Radiology reports frequently assert absence ("no consolidation"); contrastive alignment on such text may create pathological associations between absence-words and normal anatomy.
- **Hypothesis:** In report-pretrained medical VLMs, similarity maps for "no X" prompts activate the same regions as "X" prompts (negation blindness), and the degree of blindness predicts failure of the model's pseudo-mask quality on pathology classes with high negation frequency in reports.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Negation blindness in report-trained medical VLM dense grounding, tied quantitatively to report negation statistics — clinically pressing, measurable, and specific to the medical supervision pipeline.

### W5-083 — Test whether decoders trained on frozen CLIP features learn to *invert* the alignment…
- **CanonicalID:** W5-083  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-C-0078
- **One-liner:** Test whether decoders trained on frozen CLIP features learn to *invert* the alignment direction — actively removing text-aligned components to recover spatial detail.
- **Problem:** Frozen-VLM segmentation pipelines work better than raw similarity readouts; what the trained decoder actually does to the features is unknown.
- **Hypothesis:** The decoder's learned input transformation systematically down-projects the directions most aligned with text embeddings (measurable via projection analysis), and constraining the decoder to preserve those directions reproduces the raw-readout failures — proving decoders succeed by undoing alignment.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR
- **Why kept:** PROTECTED (high-risk/high-reward). "Decoders succeed by undoing alignment" would expose the standard frozen-CLIP segmentation pipeline as self-contradictory — a mechanistic result with large design consequences.

### W5-084 — Replace the VLM text encoder's output with class-mean image embeddings: if open-vocab…
- **CanonicalID:** W5-084  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-C-0329
- **One-liner:** Replace the VLM text encoder's output with class-mean image embeddings: if open-vocab segmentation is unchanged, "language" contributes nothing beyond class indexing.
- **Problem:** Open-vocabulary methods credit language understanding; the null — text embeddings function merely as arbitrary class anchors learnable from images alone — is never tested.
- **Hypothesis:** Substituting text embeddings with image-derived class prototypes (mean embeddings of a handful of examples) preserves most open-vocab segmentation performance on seen-vocabulary classes, with genuine language value confined to zero-example classes — bounding the linguistic contribution precisely.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** PROTECTED (cheap counter-intuitive). Replacing the text encoder with class-mean image prototypes bounds the linguistic contribution of "language-driven" segmentation with a single embedding swap.

### W5-085 — Tail open-vocabulary failure is linguistic, not visual
- **CanonicalID:** W5-085  ·  **Cluster:** P7 — Language–vision grounding & dense-VLM failure modes
- **SourceIDs:** IDEA-B-0033
- **One-liner:** Decompose open-vocabulary segmentation failures on tail classes into linguistic causes (polysemous or obscure class names) versus visual causes (rare appearance), by intervening on the text side only.
- **Problem:** Open-vocab models fail on rare classes, and everyone assumes the cause is visual rarity, but tail class names are also rarer and more ambiguous in the text encoder's training distribution.
- **Hypothesis:** For a meaningful fraction of tail classes, replacing the class name with a disambiguated description (or a name that is frequent in text corpora) recovers a large share of the gap, holding the image pathway fixed.
- **Novelty:** UNVERIFIED
- **Protect:** REV · M
- **Why kept:** Auditor revive (stage2_audit.md §5): Killed as duplicate of B-0124, but 0124 covers only amorphous-class text-anchor collinearity; 0033 is the general long-tail version, and it mechanistically connects to A-0033 (specificity inverse-U) and A-0049 (register mismatch) — three surviving ideas would share its frequency-regression machinery.

## P8 — Interactive segmentation & the prompt interface (6)

### W5-086 — The human-prompt distribution gap [E]
- **CanonicalID:** W5-086  ·  **Cluster:** P8 — Interactive segmentation & the prompt interface
- **SourceIDs:** IDEA-B-0089 + IDEA-B-0193  (= MERGE-17)
- **One-liner:** Collect human prompt logs once: measure the oracle-prompt inflation factor of GT-derived evaluation prompts, and the training-side gain from human-modeled prompt sampling — evaluation and training halves of one gap.
- **Problem:** Benchmark prompts are computed from the GT mask (centroid, tight box), information a real user does not have; reported numbers therefore bound deployment performance from above by an unknown margin.
- **Hypothesis:** The oracle inflation factor is large and task-dependent (worst for low-contrast and ambiguous-extent targets) and is itself predictable from target visibility statistics, enabling corrected reporting without user studies for every paper.
- **Novelty:** UNVERIFIED
- **Protect:** DM
- **Why kept:** B's reviewer prescribed shared prompt-log collection; the merged framing (the interaction channel has a domain gap; measure it at eval, close it at training) is strictly stronger. Shares logs with revived A-0328.

### W5-087 — Prompt-protocol sensitivity: how much do medical-SAM rankings depend on the click recipe? [E]
- **CanonicalID:** W5-087  ·  **Cluster:** P8 — Interactive segmentation & the prompt interface
- **SourceIDs:** IDEA-B-0083
- **One-liner:** Quantify how method rankings among medical SAM variants change across published prompt protocols (center click, random-in-mask, box-with-jitter, iterative), and propose reporting a protocol-sensitivity index.
- **Problem:** Each paper evaluates under its own prompt recipe; cross-paper comparisons implicitly assume protocol invariance that has never been verified.
- **Hypothesis:** Rankings among top methods are materially protocol-dependent (rank correlations well below 1 across protocols), and some methods' claimed superiority exists only under their own protocol.
- **Novelty:** UNVERIFIED — adjacent: medical-SAM protocol-variation papers; rank-correlation index is the residual (audit §3.7)
- **Protect:** CF·DM
- **Why kept:** Pure evaluation on public checkpoints; if rankings move materially, cross-paper comparison in this subfield is broken and a protocol-sensitivity index becomes mandatory reporting.

### W5-088 — Wrong-prompt behavior: does SAM fail loudly or silently under semantic prompt errors?
- **CanonicalID:** W5-088  ·  **Cluster:** P8 — Interactive segmentation & the prompt interface
- **SourceIDs:** IDEA-B-0104
- **One-liner:** Characterize what promptable segmenters output when prompts are semantically wrong (clicked on the wrong organ, box around the wrong object), and whether any internal signal flags the mismatch.
- **Problem:** Real users make semantic errors, and a model that returns a confident well-formed mask of the wrong structure is more dangerous than one that visibly fails.
- **Hypothesis:** Under wrong-target prompts, output confidence and mask-quality predictions remain high (silent failure) because the decoder's job is conditional delineation, and detecting the mismatch requires an external image-mask-intent consistency signal, which a small auxiliary model can supply.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Defines and measures a safety property nobody reports; one evaluation pass produces the answer, and the auxiliary mismatch-detector gives a constructive follow-up.

### W5-089 — Is the prompt-to-mask map continuous? Lipschitz geometry of interactive segmentation
- **CanonicalID:** W5-089  ·  **Cluster:** P8 — Interactive segmentation & the prompt interface
- **SourceIDs:** IDEA-B-0128
- **One-liner:** Measure the continuity structure of the click-position-to-output-mask mapping—identifying discontinuity manifolds where millimeter click changes flip the output—and test whether discontinuity density predicts interactive failure rates.
- **Problem:** Users assume nearby clicks give similar masks; if the prompt-response map has dense discontinuities (mode switches between competing objects), interaction becomes unpredictable in ways average metrics never reveal.
- **Hypothesis:** The prompt space is partitioned into basins separated by discontinuity boundaries that concentrate near object-part junctions and ambiguous regions; per-image discontinuity density is measurable, varies across domains, and predicts human interaction time better than one-shot IoU.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Defines a geometric usability property of promptable models that training could optimize but nobody measures.

### W5-090 — Non-monotonic interactive refinement: when more clicks make masks worse
- **CanonicalID:** W5-090  ·  **Cluster:** P8 — Interactive segmentation & the prompt interface
- **SourceIDs:** IDEA-B-0282
- **One-liner:** Quantify how often adding a correction click degrades SAM-family mask quality (non-monotonic refinement), characterize the conditions triggering it, and identify the decoder mechanism responsible.
- **Problem:** Interactive pipelines assume monotone improvement with user effort, but practitioners observe occasional regressions after corrections—if regressions are common, click-efficiency metrics and user trust are both built on a false monotonicity assumption.
- **Hypothesis:** Click-induced regressions occur at a measurable, non-trivial rate concentrated in identifiable conditions (corrections near ambiguity boundaries triggering candidate-mask mode switches), the mechanism is decoder mode competition rather than noise (verifiable by candidate-trajectory logging), and a mode-stabilized decoding rule eliminates most regressions without harming normal refinement.
- **Novelty:** UNVERIFIED
- **Protect:** CI·CF
- **Why kept:** Breaks the monotone-improvement contract that click-efficiency metrics and user trust are built on.

### W5-091 — Simulated-click protocol validity for interactive segmentation [E]
- **CanonicalID:** W5-091  ·  **Cluster:** P8 — Interactive segmentation & the prompt interface
- **SourceIDs:** IDEA-A-0328
- **One-liner:** Validate (or invalidate) simulated-click protocols for interactive segmentation by measuring ranking agreement with real-user evaluations across the current model generation.
- **Problem:** Interactive segmentation progress is measured almost entirely through click simulators (cf. IDEA-A-0048); if simulator rankings diverge from human-user rankings for modern models, the subfield's leaderboard is measuring the wrong thing — the protocol validity check is overdue.
- **Hypothesis:** Simulator-based and real-user rankings agree on coarse model tiers but disagree on adjacent pairs in >30% of cases, with disagreement concentrated where models differ in error *placement* (which simulators respond to differently than humans) — simulators are valid for screening, invalid for fine ranking.
- **Novelty:** UNVERIFIED
- **Protect:** REV · M
- **Why kept:** Auditor revive (stage2_audit.md §5): Killed on user-study cost — but Batch B *funded* the same data collection twice (B-0089 oracle-inflation and B-0193 prompt-log collection, which the B reviewer explicitly ordered to "run as one user-study effort").

## P9 — Transparency, camouflage & layered scenes (6)

### W5-092 — What frozen features know about layered scenes
- **CanonicalID:** W5-092  ·  **Cluster:** P9 — Transparency, camouflage & layered scenes
- **SourceIDs:** IDEA-A-0141 + IDEA-B-0126  (= MERGE-10)
- **One-liner:** Probes on frozen VFM features over glass regions decode {glass presence, background class, both layers}; the three-way verdict routes transparency work to pretraining, output-format, or decoder fixes.
- **Problem:** Transparent objects violate the assumption that pixel appearance belongs to the surface at that pixel; whether backbone features on glass regions represent "glass" or "the background behind glass" is unmeasured and determines what any downstream head can do.
- **Hypothesis:** Linear probes on patch features within glass regions decode the *background* class with >70% accuracy but "glass present" with <55% (near chance for hard cases) across major VFMs — the representation itself is transparent to transparency.
- **Novelty:** UNVERIFIED
- **Protect:** HR+CI / CI
- **Why kept:** Same probing substrate generated twice; B's positive case presupposes A's measurement, and the three-way verdict is stronger than either alone. Flagship of the transparency cluster.

### W5-093 — Depth failure as transparency signal
- **CanonicalID:** W5-093  ·  **Cluster:** P9 — Transparency, camouflage & layered scenes
- **SourceIDs:** IDEA-A-0142 + IDEA-B-0159  (= MERGE-16)
- **One-liner:** Depth sensors fail on glass — exploited on both sides of the pipeline: {RGB, naive RGB-D, RGB+validity-mask} inference triads, and invalid-depth masks harvested from public RGB-D corpora as potentially the largest free transparency corpus.
- **Problem:** RGB-D models are assumed superior, but on transparent surfaces depth is systematically wrong (returns background depth or dropout), potentially teaching models an anti-glass shortcut; the sign of depth's contribution on transparency is unestablished.
- **Hypothesis:** RGB-D models underperform RGB-only models on transparent-object IoU by >5 points when depth is naively fused, but *depth-invalidity* (the dropout/mismatch pattern itself) used as an explicit feature outperforms both — the sensor's failure is the best transparency cue.
- **Novelty:** UNVERIFIED — adjacent: ClearGrasp-lineage depth-invalidity exploitation (audit §3.5)
- **Protect:** CI / HRHR
- **Why kept:** One discovery claim ('depth invalidity is the strongest transparency cue'), two exploitation arms; HRHR wildcard — if confounder filtering works, transparency data economics change permanently. Novelty at risk: ClearGrasp-lineage robotics work exploits depth invalidity (audit §3).

### W5-094 — Does SAM segment glass by its reflections? A reflection-swap diagnostic
- **CanonicalID:** W5-094  ·  **Cluster:** P9 — Transparency, camouflage & layered scenes
- **SourceIDs:** IDEA-B-0075
- **One-liner:** Determine whether foundation segmenters localize transparent objects via boundary/refraction cues (domain-stable) or via reflected environmental content (domain-fragile), by swapping reflections between environments in controlled captures.
- **Problem:** Transparent-object performance varies wildly across environments, and without knowing which cue the model uses, indoor-trained systems cannot be safely deployed outdoors.
- **Hypothesis:** Segmentation quality tracks the familiarity of reflected content rather than the physical boundary cues—demonstrable when reflection-swapped objects (same glass, alien reflections) lose performance while boundary cues are held fixed.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR·CI — protected
- **Why kept:** Identifies the true generalization bottleneck for transparency perception; the answer redirects data collection (reflection diversity vs boundary diversity).

### W5-095 — Polarization-taught transparency: can physics-privileged training transfer to plain RGB?
- **CanonicalID:** W5-095  ·  **Cluster:** P9 — Transparency, camouflage & layered scenes
- **SourceIDs:** IDEA-B-0162
- **One-liner:** Train transparency segmenters with polarization imagery as privileged supervision (available only at training time) and measure how much of the polarization advantage transfers to RGB-only inference.
- **Problem:** Polarization cameras see glass through physical cues (polarized specular reflection) but will never be ubiquitous; whether their signal can be internalized by RGB models via privileged learning is untested.
- **Hypothesis:** Polarization-privileged training transfers a substantial fraction of the polarization advantage to RGB inference—because polarization labels teach the model which subtle RGB cues (reflection gradients, boundary distortions) are transparency-diagnostic—outperforming RGB-only training at matched labels.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR — protected
- **Why kept:** Either yields a capture-once-deploy-everywhere recipe or proves the polarization cue has no RGB correlate — a clean, valuable dichotomy either way.

### W5-096 — The human floor on near-invisible glass
- **CanonicalID:** W5-096  ·  **Cluster:** P9 — Transparency, camouflage & layered scenes
- **SourceIDs:** IDEA-A-0157
- **One-liner:** Measure the human-vision floor for near-invisible glass (clean, anti-reflective, well-lit) and test whether current models are above or below human performance on the hardest transparency regime.
- **Problem:** Some glass is nearly invisible even to humans (people walk into doors); without a human floor, we cannot say whether model failures reflect missing information or missing competence.
- **Hypothesis:** On a hardest-regime glass set, human detection (brief-presentation) exceeds the best models by >30 points — humans exploit weak cues (frames, context, subtle reflections) that models don't, proving competence (not information) is the bottleneck.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** The competence-vs-information verdict decides whether transparency research should invest in modeling or sensing — a rare experiment that prices a whole research direction.

### W5-097 — Camouflage failure: attentional or perceptual?
- **CanonicalID:** W5-097  ·  **Cluster:** P9 — Transparency, camouflage & layered scenes
- **SourceIDs:** IDEA-A-0154
- **One-liner:** Determine whether camouflaged object detection failures are perceptual (features don't separate figure from ground) or attentional (features suffice but saliency/prompting never looks there), using oracle-prompt interventions.
- **Problem:** COD is treated as one problem, but the two failure sources demand opposite fixes (representation learning vs search/prompting); no work cleanly separates them.
- **Hypothesis:** Given an oracle point prompt, promptable models recover >70% of the COD performance gap versus specialized COD models — most camouflage failure is attentional (not finding the object), not perceptual (not being able to delineate it).
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** One oracle-prompt experiment could redirect an entire subfield's investment from features to search.

## P10 — Amorphous matter full stack: smoke, fire, wildfire (12)

### W5-098 — Binary smoke masks are ill-posed ground truth
- **CanonicalID:** W5-098  ·  **Cluster:** P10 — Amorphous matter full stack: smoke, fire, wildfire
- **SourceIDs:** IDEA-A-0121
- **One-liner:** Demonstrate that binary smoke masks are ill-posed ground truth by measuring annotator threshold inconsistency, and propose density-graded ground truth as the corrected task definition.
- **Problem:** Smoke has no boundary — annotators binarize a continuous density field at arbitrary personal thresholds, so smoke-segmentation benchmarks may largely measure threshold mimicry, capping and distorting all reported progress.
- **Hypothesis:** Inter-annotator disagreement on smoke masks concentrates in low-density regions and corresponds to annotators applying different implicit density thresholds (recoverable as a per-annotator scalar), such that a single density map explains >80% of inter-annotator mask variance.
- **Novelty:** UNVERIFIED
- **Protect:** RM
- **Why kept:** Task-redefinition with a measurable decomposition test (per-annotator scalar thresholds); anchors the entire smoke program (0122, 0128, 0126, 0319).

### W5-099 — Beer–Lambert transmittance as smoke ground truth
- **CanonicalID:** W5-099  ·  **Cluster:** P10 — Amorphous matter full stack: smoke, fire, wildfire
- **SourceIDs:** IDEA-A-0122
- **One-liner:** Use atmospheric transmission physics (Beer–Lambert attenuation) to derive alpha-matte smoke ground truth from smoke/no-smoke image pairs, creating physically defined labels without human thresholding.
- **Problem:** Human smoke labels are threshold-arbitrary (IDEA-A-0121); paired imagery (fixed cameras before/during smoke) permits computing per-pixel transmittance as physically meaningful ground truth, which nobody has operationalized into a benchmark.
- **Hypothesis:** Transmittance maps computed from pairs are reproducible across illumination-matched pairs (correlation >0.9), and models trained to regress transmittance transfer better to unseen scenes (>10% relative error reduction) than binary-mask-trained models thresholded post hoc.
- **Novelty:** UNVERIFIED
- **Protect:** HR
- **Why kept:** Protected HR: the first physically defined supervision for smoke — a benchmark-construction idea whose success would obsolete threshold-mimicry training (0121's diagnosis) and enable 0126's latency metric on principled labels.

### W5-100 — One boundary-contrast law across hard-target literatures
- **CanonicalID:** W5-100  ·  **Cluster:** P10 — Amorphous matter full stack: smoke, fire, wildfire
- **SourceIDs:** IDEA-A-0006 + IDEA-B-0226  (= MERGE-03)
- **One-liner:** A single standardized integrated-boundary-contrast measure may predict IoU and detection recall across amorphous matter, camouflage, transparency, and low-contrast lesions; causal contrast-enhancement arm included.
- **Problem:** SAM fails on smoke/fire, but we don't know if this is a continuous physics-driven failure (no boundary → no mask) or a semantic gap (never saw the category).
- **Hypothesis:** Across amorphous and solid objects alike, SAM IoU is monotonically predicted by a single scalar — integrated boundary contrast — and amorphous categories lie on the *same* curve as solid objects (falsified if amorphous classes fall systematically below the curve).
- **Novelty:** UNVERIFIED
- **Protect:** CI / DM
- **Why kept:** Same single-variable law (failure as a continuous function of boundary contrast, not category membership) generated twice; curve collapse would unify three failure literatures. Depends on A-0121's GT critique for the smoke y-axis (CONF-3).

### W5-101 — No prompt strategy rescues SAM on smoke
- **CanonicalID:** W5-101  ·  **Cluster:** P10 — Amorphous matter full stack: smoke, fire, wildfire
- **SourceIDs:** IDEA-A-0128
- **One-liner:** Systematically quantify SAM/SAM2's failure on smoke across prompt strategies, testing whether *any* prompting scheme (multi-point, box, dense grid, video propagation) recovers usable smoke masks.
- **Problem:** SAM is being wired into wildfire pipelines as a zero-shot labeler, but its edge-driven mask prior (cf. IDEA-A-0006) is maximally mismatched to boundary-free smoke — the practical recoverability question is unanswered.
- **Hypothesis:** No prompt strategy raises SAM's smoke IoU above 0.5× a small supervised baseline's; failures are shrinkage-to-dense-core (predictable from the density field), meaning SAM masks systematically under-cover exactly the low-density smoke that matters for early detection.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Protected CF: a definitive cheap negative with a quantified shrinkage law that blocks a specific bad practice (SAM auto-labeling of smoke) before it propagates into datasets.

### W5-102 — Detection latency as the wildfire metric
- **CanonicalID:** W5-102  ·  **Cluster:** P10 — Amorphous matter full stack: smoke, fire, wildfire
- **SourceIDs:** IDEA-A-0126
- **One-liner:** Replace IoU with detection-latency (time from first visible smoke to first correct alarm-grade mask) as the primary metric for wildfire smoke systems, and test whether IoU-optimal models are latency-suboptimal.
- **Problem:** Wildfire response cares about minutes-to-detection of faint early smoke, but the field optimizes IoU on developed plumes; the two objectives may rank models differently, misdirecting research.
- **Hypothesis:** On time-stamped ignition sequences, model rankings by median detection latency disagree with IoU rankings (rank correlation <0.5), and latency winners share high recall on low-density smoke rather than high boundary accuracy.
- **Novelty:** UNVERIFIED
- **Protect:** RM
- **Why kept:** Mission-aligned metric with a testable ranking-disagreement claim; the evaluation-science layer of the smoke program.

### W5-103 — Fire segmenters are color detectors
- **CanonicalID:** W5-103  ·  **Cluster:** P10 — Amorphous matter full stack: smoke, fire, wildfire
- **SourceIDs:** IDEA-A-0123
- **One-liner:** Test whether fire segmentation models are mostly color detectors, via hue-manipulation stress tests and colored-distractor benchmarks (sunsets, neon, brake lights).
- **Problem:** Fire has a distinctive color signature, inviting a spectral shortcut; if models are ~color thresholds with extra steps, they will fail on atypical flames (methanol, gas burners) and false-alarm on red/orange distractors — unquantified in current benchmarks.
- **Hypothesis:** State-of-the-art fire segmenters lose >50% IoU on hue-shifted flames while confidently segmenting >30% of matched colored distractors — performance is explained predominantly by chromatic features, not structure or motion.
- **Novelty:** UNVERIFIED
- **Protect:** CI+CF
- **Why kept:** Safety-critical shortcut audit with specific, checkable predictions (blue flames missed, sunsets flagged); cheap; the fire-side complement of 0021's achromaticity test.

### W5-104 — Turbulence spectra as a label-free smoke signal
- **CanonicalID:** W5-104  ·  **Cluster:** P10 — Amorphous matter full stack: smoke, fire, wildfire
- **SourceIDs:** IDEA-A-0125
- **One-liner:** Test whether the turbulence statistics of smoke motion (spectral signatures of buoyant plumes) provide a self-supervision signal that separates smoke from all rigid-world motion without labels.
- **Problem:** Smoke's defining property is its dynamics (buoyancy-driven turbulence), yet self-supervised smoke detection from motion statistics — rather than appearance — remains untested as a primary signal.
- **Hypothesis:** A classifier over local spatiotemporal spectra (no appearance features) achieves >0.9 AUC separating smoke regions from moving rigid objects, vegetation, and camera shake, and pretraining on this signal improves downstream smoke segmentation with 10× fewer labels.
- **Novelty:** UNVERIFIED
- **Protect:** HR
- **Why kept:** Protected HR: physics-grounded, appearance-free pretext that would be robust to exactly the shifts that break appearance models; genuinely novel formulation.

### W5-105 — Differentiable scattering: a physics head for volumetric smoke from single images
- **CanonicalID:** W5-105  ·  **Cluster:** P10 — Amorphous matter full stack: smoke, fire, wildfire
- **SourceIDs:** IDEA-B-0318
- **One-liner:** Attach a differentiable single-scattering radiative-transfer head to a segmentation backbone so smoke predictions are expressed as volumetric density fields rendered into 2D—making the physical quantity the output and the 2D mask merely its projection.
- **Problem:** 2D smoke masks conflate optically thin and thick smoke, cannot support downstream physics (dispersion, visibility), and force models to make arbitrary threshold decisions at soft boundaries.
- **Hypothesis:** Training a density-field head through a differentiable scattering renderer against ordinary 2D masks yields (a) binary segmentation at least matching direct mask prediction, (b) density estimates that correlate with independent physical measurements (transmissometers, paired-view consistency) despite never being directly supervised—demonstrating that physics structure extracts 3D information from 2D labels.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR — protected
- **Why kept:** Resolves the dimensional mismatch (2D labels, 3D medium) that pure segmentation cannot, and its validation (paired-view consistency, transmissometer correlation) is independent of the training labels.

### W5-106 — Fog as a negative domain: does adapting to fog worsen smoke detection?
- **CanonicalID:** W5-106  ·  **Cluster:** P10 — Amorphous matter full stack: smoke, fire, wildfire
- **SourceIDs:** IDEA-B-0055
- **One-liner:** Test whether robustness-oriented adaptation toward foggy conditions increases false positives on smoke (and vice versa), revealing an adversarial coupling between a nuisance domain and a target class that look alike.
- **Problem:** Weather robustness and smoke detection are pursued independently; because fog and smoke are near-identical scattering phenomena, adapting to tolerate one may suppress or hallucinate the other.
- **Hypothesis:** Models adapted for fog invariance show a measurable increase in smoke false negatives (fog-invariance transfers to smoke-invariance), quantifiable as a robustness-specificity tradeoff curve.
- **Novelty:** UNVERIFIED
- **Protect:** CI·DM
- **Why kept:** Formalizes a class of shift ("negative domain") the robustness literature has no name for, in a safety-critical setting.

### W5-107 — Boxes are the wrong primitive for amorphous targets
- **CanonicalID:** W5-107  ·  **Cluster:** P10 — Amorphous matter full stack: smoke, fire, wildfire
- **SourceIDs:** IDEA-A-0319
- **One-liner:** Test whether bounding boxes are the wrong output primitive for amorphous phenomena (smoke, fire, spills, dust) by comparing box-based against blob/level-set-based detection formulations on downstream decision quality.
- **Problem:** Detection pipelines force amorphous phenomena into boxes whose corners are meaningless (a smoke box is mostly non-smoke); the primitive mismatch plausibly harms both learning and downstream use, but no controlled formulation comparison exists.
- **Hypothesis:** For amorphous targets, blob-primitive detectors (center + soft extent) beat box detectors on downstream decision metrics (alarm localization error, extent-tracking stability) by >20% relative at matched compute, while boxes remain superior for rigid objects — the optimal primitive is phenomenology-dependent, falsified if boxes suffice everywhere.
- **Novelty:** UNVERIFIED
- **Protect:** — (merit)
- **Why kept:** Output-primitive science — a representational question the field treats as settled by convention, judged on downstream decisions rather than proxy AP. Completes the amorphous-phenomena program (0121, 0122, 0141, 0287).

### W5-108 — Is duplicate suppression the binding constraint for amorphous-target detection?
- **CanonicalID:** W5-108  ·  **Cluster:** P10 — Amorphous matter full stack: smoke, fire, wildfire
- **SourceIDs:** IDEA-B-0219
- **One-liner:** Test whether non-maximum suppression and its query-based equivalents systematically destroy correct detections of amorphous, fragmenting targets (smoke plumes splitting and merging), by comparing suppression-free architectures at matched capacity on plume-dense scenes.
- **Problem:** NMS assumes one box per discrete object, but plumes are non-discrete—overlapping detections of one plume and separate detections of split plumes are both correct answers that suppression logic cannot represent.
- **Hypothesis:** A measurable fraction of missed detections on multi-plume scenes occurs at the suppression stage (recoverable by oracle suppression), the loss grows with plume fragmentation degree, and set-prediction architectures without hard suppression recover most of it—reframing amorphous detection as a suppression-design problem.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Attributes a chronic failure to a specific replaceable pipeline stage rather than to feature quality where effort currently goes.

### W5-109 — The smoke/fog/steam/cloud/dust confusion benchmark
- **CanonicalID:** W5-109  ·  **Cluster:** P10 — Amorphous matter full stack: smoke, fire, wildfire
- **SourceIDs:** IDEA-A-0124
- **One-liner:** Build the smoke/fog/steam/cloud/dust confusion benchmark and test whether any visual model can separate these physically distinct but visually similar aerosols from single frames.
- **Problem:** Wildfire systems must distinguish smoke from look-alike aerosols, but no benchmark isolates this five-way confusion, and it is unknown whether single-frame separation is even information-theoretically feasible.
- **Hypothesis:** Single-frame human expert accuracy on the five-way task is barely above chance for distant plumes (<45% vs 20% chance), while short temporal clips restore human accuracy to >80% — the discrimination is fundamentally temporal, and single-frame models are structurally capped.
- **Novelty:** UNVERIFIED
- **Protect:** REV · HRHR-data
- **Why kept:** Auditor revive (stage2_audit.md §5): This is the information-theoretic ceiling under three survivors (B-0055 fog-negative-domain, B-0124 text-anchor confusion, A-0126 latency metric) and the only killed idea that restores a *temporal* question to the smoke program.

## P11 — Small structures & token-lattice artifacts (11)

### W5-110 — The small-structure bottleneck: information-absent vs decoder-limited vs destroyed-at-tokenization
- **CanonicalID:** W5-110  ·  **Cluster:** P11 — Small structures & token-lattice artifacts
- **SourceIDs:** IDEA-A-0161 + IDEA-B-0129 + IDEA-C-0264  (= MERGE-04‡)
- **One-liner:** Probe frozen features to locate the decodability crossover for small/thin structures, attribute the loss layer-by-layer to patch embedding, and test tokenization irreversibility with decoder-capacity × patch-size grids.
- **Problem:** Small/thin-structure failure is loosely attributed to 'resolution'; whether the information is absent from tokens (irreversible) or present but decoder-limited (recoverable) decides where the field's small-structure investment should go.
- **Hypothesis:** Overparameterized probes on frozen features locate a size crossover below which structure information is absent at the token level; the crossover tracks patch size rather than decoder capacity, and layer-wise audits localize the destruction to the patch-embedding stage — falsified if larger decoders recover small-structure performance.
- **Novelty:** UNVERIFIED
- **Protect:** RM
- **Why kept:** Three independent generations of one question (A patch-grid intervention, B oracle probes, C-0264 layer-of-loss attribution) merged into one program; the compass for all small-structure investment.

### W5-111 — IoU-vs-size failure law with a patch-size knee
- **CanonicalID:** W5-111  ·  **Cluster:** P11 — Small structures & token-lattice artifacts
- **SourceIDs:** IDEA-A-0003
- **One-liner:** Establish an empirical "failure law" relating object pixel size to SAM IoU and test whether the breakpoint is set by the ViT patch size (16 px).
- **Problem:** "SAM is bad at small objects" is folklore without a quantitative form; if the failure is patch-quantization-driven, it predicts a specific breakpoint and scaling.
- **Hypothesis:** SAM's mean IoU vs object diameter follows a saturating curve with a sharp knee at ~2–3 patch widths (32–48 px at 1024 input), and re-running with a hypothetical smaller-patch encoder (or higher-res tiling) shifts the knee proportionally — if the knee does not track patch size, the hypothesis is falsified.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Cheap-to-falsify with a sharp quantitative prediction (curve collapse in patch units); directly complements the training-side version (0161) at near-zero compute.

### W5-112 — Resolution beats small-object architecture remedies
- **CanonicalID:** W5-112  ·  **Cluster:** P11 — Small structures & token-lattice artifacts
- **SourceIDs:** IDEA-A-0313
- **One-liner:** Test whether raw input resolution beats all architectural small-object remedies at matched compute — the compute-matched showdown the small-object detection literature has skipped.
- **Problem:** Dozens of architectural fixes target small-object detection, each compared at fixed resolution; if simply spending the same extra compute on resolution dominates them, the literature's recommendations are misordered for practitioners.
- **Hypothesis:** At matched inference FLOPs, resolution scaling exceeds ≥80% of published architectural small-object remedies on their own benchmarks, with architecture wins confined to memory-bound regimes where resolution cannot be raised — resolution is the dominant currency, falsified if architectures win at matched compute.
- **Novelty:** UNVERIFIED
- **Protect:** RM
- **Why kept:** A compute-matched confrontation that could re-baseline an entire subfield with six reproductions — enormous verdict-per-GPU-hour, and a guaranteed disagreement magnet among small-object-method authors.

### W5-113 — Bigger models, smaller structures: an inverse scaling pocket for dense prediction?
- **CanonicalID:** W5-113  ·  **Cluster:** P11 — Small structures & token-lattice artifacts
- **SourceIDs:** IDEA-B-0288
- **One-liner:** Test whether larger foundation-segmenter variants perform relatively worse on very small structures than smaller variants—an inverse-scaling pocket where capacity is allocated to global coherence at the expense of tiny-target fidelity.
- **Problem:** Scaling is assumed monotone-beneficial across all strata, procurement defaults to the largest affordable model, but if scale redistributes capacity away from small-structure precision, the default is wrong for exactly the medical and early-detection tasks where small things matter most.
- **Hypothesis:** Size-stratified evaluation reveals a crossing: larger variants dominate on medium/large structures while smaller variants match or beat them on structures below a threshold size (mechanism: deeper attention integrates global context that overrides weak local evidence, verifiable via attention-rollout analysis), and the crossing replicates across model families—establishing stratum-conditional model selection.
- **Novelty:** UNVERIFIED
- **Protect:** CI·DM
- **Why kept:** A verified crossing overturns scale-is-all procurement exactly for small-structure-critical deployments (early detection, lesions).

### W5-114 — Benchmark JPEG already deleted the small objects
- **CanonicalID:** W5-114  ·  **Cluster:** P11 — Small structures & token-lattice artifacts
- **SourceIDs:** IDEA-A-0176
- **One-liner:** Audit dataset-level JPEG compression as a hidden confounder for small-object and boundary research: are benchmark small objects already destroyed by compression before models ever see them?
- **Problem:** Popular benchmarks were collected as compressed JPEGs; compression disproportionately destroys small-object texture and boundary detail, so measured "model limits" may partly be data limits — never audited.
- **Hypothesis:** On losslessly captured evaluation sets, model small-object performance is >15% higher than on JPEG-matched versions of the same scenes, and cross-benchmark differences in reported small-object difficulty correlate with dataset compression statistics — part of "small objects are hard" is "small objects were deleted."
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Benchmark-construction confounder that reframes "small objects are hard" — a data-provenance insight nobody has audited.

### W5-115 — Register-token artifacts blind small objects
- **CanonicalID:** W5-115  ·  **Cluster:** P11 — Small structures & token-lattice artifacts
- **SourceIDs:** IDEA-A-0174
- **One-liner:** Measure the effect of ViT attention artifacts (high-norm "register" tokens appearing in feature maps) on small-object localization, testing whether artifact positions systematically mask small instances.
- **Problem:** DINOv2-class models exhibit high-norm artifact tokens in low-information regions (motivating register tokens); whether these artifacts collide with and suppress small objects in dense prediction is an open, checkable question.
- **Hypothesis:** Small-object recall drops significantly (>10%) for instances whose spatial location coincides with artifact tokens compared to matched non-artifact locations, and register-token models show no such positional recall deficit — artifacts cause localized dense-prediction blindness.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Ties a hot ViT mechanism (register tokens) to a concrete dense harm with a pure inference study; the register/no-register model pair is a natural experiment.

### W5-116 — Angular aliasing: patch-grid anisotropy against thin oblique structures
- **CanonicalID:** W5-116  ·  **Cluster:** P11 — Small structures & token-lattice artifacts
- **SourceIDs:** IDEA-B-0122
- **One-liner:** Measure how segmentation quality of thin structures varies with their orientation relative to the ViT patch grid, and determine whether the effect stems from patch embedding, positional encoding, or attention locality.
- **Problem:** Patch tokenization imposes a square lattice on images; thin structures crossing patches obliquely are fragmented across tokens in orientation-dependent ways, a potential systematic bias no one has quantified.
- **Hypothesis:** Thin-structure IoU exhibits measurable periodic dependence on orientation (worst near 45° at widths below patch size), the effect persists after rotation augmentation, and it localizes to the patch-embedding stage via layer-wise interventions.
- **Novelty:** UNVERIFIED
- **Protect:** CI·CF
- **Why kept:** A lattice-induced bias would touch every ViT dense predictor on safety-critical thin targets (vessels, wires, catheters); synthetic controls make it cheap to establish or kill.

### W5-117 — Patch-lattice aliasing: performance is periodic in input size and grid phase
- **CanonicalID:** W5-117  ·  **Cluster:** P11 — Small structures & token-lattice artifacts
- **SourceIDs:** IDEA-B-0305 + IDEA-C-0261  (= MERGE-25)
- **One-liner:** Dense quality oscillates with input size at the patch-grid period and with sub-patch translation phase of object boundaries — an unmeasured variance term contaminating cross-paper comparisons; anti-aliased resizing removes it.
- **Problem:** Dense scores are treated as smooth functions of input resolution and framing, but ViT patch grids induce periodic aliasing in both input size and boundary-to-grid alignment — a systematic variance source no benchmark controls.
- **Hypothesis:** Segmentation quality oscillates measurably (a) with input size at the patch-grid period and (b) with sub-patch translation offsets of object boundaries; the amplitude is architecture-predictable and shrinks under anti-aliased resizing — falsified if phase and size sweeps show no periodicity beyond noise.
- **Novelty:** UNVERIFIED
- **Protect:** CI·CF
- **Why kept:** Merged the two phase axes of one aliasing phenomenon (B's resolution periodicity; C-0261's translation grid-phase); one sweep instrument serves both, co-scheduled with B-0122's orientation axis.

### W5-118 — Recovered or hallucinated? Synthetic-truth audit of learned upsampling detail
- **CanonicalID:** W5-118  ·  **Cluster:** P11 — Small structures & token-lattice artifacts
- **SourceIDs:** IDEA-A-0170 + IDEA-C-0276  (= MERGE-26)
- **One-liner:** Do INR decoders and learned feature upsamplers recover image information or impose metric-pleasing priors? Synthetic scenes with exact sub-pixel truth dissociate recovered from fabricated boundary detail.
- **Problem:** INR decoders and learned upsamplers output sub-pixel-smooth boundaries that improve metrics, but whether the detail is grounded in image evidence or imposed by a learned prior is unmeasured — a fabrication risk wherever outputs feed measurements.
- **Hypothesis:** On synthetic scenes with exact sub-pixel ground truth, a large fraction of the boundary-metric gain from learned upsampling/INR decoding survives image-content randomization — i.e., is prior-imposed rather than recovered — and the fabrication concentrates exactly where downstream measurement decisions are most sensitive.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** The same fabrication-vs-information question with the same synthetic-truth instrument, generated independently in A (INR decoders) and C (feature upsamplers); merged as one adjudication spanning both method families.

### W5-119 — Test whether anti-aliased patchification (strided-conv tokenizers violate Nyquist)…
- **CanonicalID:** W5-119  ·  **Cluster:** P11 — Small structures & token-lattice artifacts
- **SourceIDs:** IDEA-C-0269
- **One-liner:** Test whether anti-aliased patchification (strided-conv tokenizers violate Nyquist) changes ViT texture bias and dense robustness.
- **Problem:** Patch embedding is a stride-16 convolution — a textbook aliasing operation — yet aliasing's contribution to ViT behavior (texture sensitivity, shift instability) has not been isolated at the tokenizer.
- **Hypothesis:** Adding proper low-pass filtering before patch sampling (fixed, non-learned) reduces measured shift inconsistency and high-frequency texture reliance of ViT features at equal accuracy, with the largest dense-task gains on high-frequency-content domains (pathology, bone) — aliasing at tokenization is a causal contributor to known ViT pathologies.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Anti-aliased patchification tests a principled causal account (Nyquist violation at the tokenizer) of several documented ViT pathologies simultaneously — one fixed low-pass layer against shift instability and texture bias.

### W5-120 — Quantify numerics as a benchmark variance source: low-precision attention implementations… [E]
- **CanonicalID:** W5-120  ·  **Cluster:** P11 — Small structures & token-lattice artifacts
- **SourceIDs:** IDEA-C-0287
- **One-liner:** Quantify numerics as a benchmark variance source: low-precision attention implementations change dense outputs near boundaries at rates comparable to reported method gains.
- **Problem:** FlashAttention variants, bf16/fp16 choices, and kernel fusion alter floating-point summation orders; dense predictions near decision boundaries can flip, yet numerics is never reported or controlled in benchmarks.
- **Hypothesis:** Across numerics configurations (kernels, precisions, batch nondeterminism), per-pixel prediction flips concentrate near boundaries and accumulate to metric differences overlapping the magnitude of typical published improvements on fine-grained boundary metrics — numerics is an unacknowledged term in the field's error budget.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR
- **Why kept:** PROTECTED (high-risk/high-reward). Numerics (attention kernels, precision, batch nondeterminism) as an unacknowledged variance term rivaling published method gains would force reporting-standards changes across dense-prediction benchmarking.

## P12 — Uncertainty, calibration & confidence validity (7)

### W5-121 — Uncertainty maps ≠ clinician disagreement
- **CanonicalID:** W5-121  ·  **Cluster:** P12 — Uncertainty, calibration & confidence validity
- **SourceIDs:** IDEA-A-0103
- **One-liner:** Test whether model uncertainty maps (entropy, MC-dropout, ensembles) actually correlate with *clinician disagreement* regions, which is the operational meaning of "useful uncertainty" in medical segmentation.
- **Problem:** Uncertainty methods are validated against model error, but their clinical use case is flagging regions where experts would disagree or want review — an alignment nobody measures.
- **Hypothesis:** Pixel-wise correlation between model uncertainty and multi-annotator disagreement is weak (ρ < 0.4) for standard methods, and is dominated by trivial boundary-band effects — after excluding boundary bands, correlation approaches zero.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** The boundary-band-excluded test is a stringent new instrument that may empty the clinical value proposition of an entire uncertainty-quantification literature.

### W5-122 — Are free uncertainty sources valid posteriors?
- **CanonicalID:** W5-122  ·  **Cluster:** P12 — Uncertainty, calibration & confidence validity
- **SourceIDs:** IDEA-B-0120 + IDEA-B-0337 + IDEA-C-0253  (= MERGE-18‡)
- **One-liner:** One coverage-testing methodology (held-out-rater reference distributions, in- and out-of-domain) applied to the three 'free' uncertainty sources practitioners consume: SAM multimask spread, mask-diffusion samples, and TTA disagreement.
- **Problem:** Practitioners consume free ensembles — SAM's multimask outputs, diffusion samples, TTA disagreement — as uncertainty, with no evidence any of them match the distribution of human raters, the reference uncertainty actually consumed clinically.
- **Hypothesis:** Under distributional coverage tests against held-out rater panels, free uncertainty sources are miscalibrated (multimask spread collapses OOD; TTA disagreement only partially tracks human ambiguity), and post-hoc recalibration recovers a measurable fraction per unit compute.
- **Novelty:** UNVERIFIED
- **Protect:** CF / CF·DM
- **Why kept:** One instrument, three free uncertainty sources: B's pair plus C-0253's TTA surrogate (independently generated). Shares multi-rater reference data with MERGE-15 and A-0103.

### W5-123 — Out-of-domain calibration of SAM's mask-quality head
- **CanonicalID:** W5-123  ·  **Cluster:** P12 — Uncertainty, calibration & confidence validity
- **SourceIDs:** IDEA-B-0084
- **One-liner:** Audit whether SAM's predicted-IoU head remains calibrated under domain shift, characterize its failure structure, and test whether a tiny recalibration head fitted on one shifted domain transfers to others.
- **Problem:** Pipelines use SAM's self-reported mask quality to filter pseudo-labels and route human review, but its reliability outside natural images is unverified.
- **Hypothesis:** The quality head systematically overestimates on out-of-domain inputs with an error that grows smoothly with shift magnitude and shares structure across domains—making a single lightweight recalibration broadly transferable.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** Load-bearing infrastructure with zero published calibration analysis.

### W5-124 — Dice loss destroys calibration, imbalance-scaled
- **CanonicalID:** W5-124  ·  **Cluster:** P12 — Uncertainty, calibration & confidence validity
- **SourceIDs:** IDEA-A-0097
- **One-liner:** Test at scale whether Dice loss — the medical default — systematically destroys probability calibration relative to cross-entropy, and whether the harm scales with class imbalance.
- **Problem:** Dice loss is near-universal in medical segmentation, yet its miscalibration side effect (known in isolated studies) has never been quantified across tasks or connected to imbalance level, leaving practitioners without a usage rule.
- **Hypothesis:** Dice-trained models show ECE ≥3× cross-entropy-trained models at matched Dice score, with miscalibration growing monotonically with foreground sparsity; a two-phase (CE→Dice) schedule retains Dice's accuracy without the calibration penalty.
- **Novelty:** UNVERIFIED — phenomenon documented in isolated medical studies; scaling law + schedule fix are the open parts (audit §3.4)
- **Protect:** RM
- **Why kept:** Settles a folklore dispute about the single most-used loss in medical imaging, with an imbalance-conditioned usage rule as the deliverable.

### W5-125 — Confidence inversion: why soft-label training can produce harder predictions
- **CanonicalID:** W5-125  ·  **Cluster:** P12 — Uncertainty, calibration & confidence validity
- **SourceIDs:** IDEA-B-0310
- **One-liner:** Investigate the paradoxical observation that models trained on soft labels (matting-style, multi-rater averages) sometimes output more extreme confidences than hard-label-trained models, characterizing when and why softness in, sharpness out.
- **Problem:** Soft labels are used specifically to convey uncertainty to models, the inversion—if real—means the mechanism backfires (models resolve soft supervision into confident interpolation rather than calibrated doubt), and downstream consumers reading confidence as uncertainty are then systematically misled.
- **Hypothesis:** Soft-label training with standard losses teaches models to predict the label-generating process's mean rather than its uncertainty (the loss is minimized by confident mean prediction), producing sharpened outputs in ambiguous zones unless the loss explicitly separates value and confidence channels—a loss-structure account testable by comparing distribution-matching versus mean-regression objectives on identical soft labels.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Corrects a widespread misunderstanding about what soft supervision achieves, with a loss-structure account testable by comparing mean-regression vs distribution-matching objectives on identical labels.

### W5-126 — Uncertainty routes labels to the wrong pixels
- **CanonicalID:** W5-126  ·  **Cluster:** P12 — Uncertainty, calibration & confidence validity
- **SourceIDs:** IDEA-A-0280
- **One-liner:** Test whether model uncertainty actually targets the pixels humans most need to label — auditing the core assumption of uncertainty-routed annotation (the model asks for labels where it is uncertain) for dense tasks.
- **Problem:** Uncertainty-guided labeling assumes uncertain pixels are the valuable ones, but uncertainty concentrates on trivial boundary bands (cf. IDEA-A-0103) while systematic errors are often *confident*; the assumption's validity for dense annotation routing is unverified.
- **Hypothesis:** Labeling budget spent on high-uncertainty regions yields less downstream improvement per pixel than budget spent on confident-but-wrong regions identified by cross-model disagreement — uncertainty routes labels to already-known ambiguity, missing the valuable systematic errors, falsified if uncertainty-routed labeling wins.
- **Novelty:** UNVERIFIED
- **Protect:** CI+CF
- **Why kept:** Attacks a productized assumption with a cheap, fully simulatable design; the confident-error-vs-uncertainty dissociation is the fresh instrument.

### W5-127 — Independent verifier vs self-confidence for failure prediction
- **CanonicalID:** W5-127  ·  **Cluster:** P12 — Uncertainty, calibration & confidence validity
- **SourceIDs:** IDEA-B-0098
- **One-liner:** Train small independent verifier networks that predict a frozen segmenter's per-case failure (IoU below threshold) from the image and predicted mask, and benchmark them against the model's own confidence outputs.
- **Problem:** Silent failure is the key deployment risk; self-reported confidence is entangled with the very representations that caused the failure.
- **Hypothesis:** An independent verifier trained on diverse failure examples detects out-of-domain failures with substantially higher AUROC than self-confidence, because it can key on inconsistency cues (mask-image disagreement) the primary model is blind to.
- **Novelty:** UNVERIFIED
- **Protect:** REV · M
- **Why kept:** Auditor revive (stage2_audit.md §5): The B reviewer's kill note conceded the science "stays implicit" — so make it explicit as the revival condition: the deliverable is the *attribution* (what do verifiers see that self-confidence structurally cannot — mask-image consistency cues vs representation-entangled confidence), with held-out-model and held-out-domain generalization as the falsifiable claims.

## P13 — Representation & pretraining science of VFMs (13)

### W5-128 — SAM follows edges, not objects
- **CanonicalID:** W5-128  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-A-0001
- **One-liner:** Test whether SAM segments *visual boundaries* rather than *semantic objects* by dissociating the two on camouflage and texture-boundary stimuli.
- **Problem:** SAM's zero-shot masks are widely treated as "object" masks, but its training signal (SA-1B) rewards boundary-consistent regions, and nobody has cleanly dissociated edge-following from objecthood.
- **Hypothesis:** SAM's mask agreement with ground truth is predicted almost entirely by local boundary gradient strength, not by object semantics; on stimuli where a strong texture edge crosses an object (or a camouflaged object has no edge), SAM will follow the edge, not the object, in >80% of cases.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** The cleanest mechanistic question in the cluster: a 2×2 dissociation design that converts scattered "SAM fails on X" anecdotes into a single testable mechanism claim, at inference-only cost.

### W5-129 — SAM2 worse than SAM1 on static fine boundaries
- **CanonicalID:** W5-129  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-A-0013
- **One-liner:** Test whether SAM2's video-trained image encoder *lost* single-image segmentation quality relative to SAM1 — a modality trade-off audit.
- **Problem:** SAM2 is assumed to strictly supersede SAM1, but video training may have traded static-image boundary precision for temporal stability.
- **Hypothesis:** On a boundary-quality-weighted static benchmark (high-res, fine structures), SAM1 outperforms SAM2 by a measurable margin (>2 boundary-F points) despite SAM2's parity or superiority on region IoU.
- **Novelty:** UNVERIFIED — known overlap: 2024 SAM2-vs-SAM medical/2D papers (arXiv:2408.04212, 2408.00756); carve is narrow (audit §3.3)
- **Protect:** CI+CF
- **Why kept:** Newest-isn't-better is a counter-intuitive, immediately actionable claim; a week of inference falsifies it.

### W5-130 — Functional achromaticity of dense models
- **CanonicalID:** W5-130  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-A-0021 + IDEA-B-0136  (= MERGE-13)
- **One-liner:** A common color-intervention battery {original, grayscale, hue-rotated, equiluminant, chroma-only} applied to SAM-class models and smoke segmenters: which dense capabilities are colorblind, with FP-stratified smoke reporting as the deployment payoff.
- **Problem:** For domains that are effectively monochrome (IR, many medical modalities), it matters whether SAM's competence depends on color statistics; this basic invariance is unmeasured.
- **Hypothesis:** SAM's IoU drops <2 points under full hue rotation and grayscale conversion on natural images, i.e., SAM is functionally achromatic — falsified if color-defined boundaries (equiluminant color edges) segment well, which would prove chromatic sensitivity.
- **Novelty:** UNVERIFIED
- **Protect:** CI+CF / CI·CF
- **Why kept:** Same instrument (channel/hue interventions), same question (is the boundary signal achromatic?), general + applied instantiations. Framed jointly with A-0123's opposite-direction fire finding (CONF-9).

### W5-131 — The task×backbone matrix for frozen dense features
- **CanonicalID:** W5-131  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-A-0202
- **One-liner:** Build the definitive task×backbone matrix for frozen dense features (DINOv2, CLIP, SAM, MAE-class) under matched probing protocols, testing whether any single "best dense backbone" exists or dominance is task-structured.
- **Problem:** Backbone choice for dense tasks is driven by fashion and scattered single-task probes with inconsistent protocols; the community lacks a controlled dominance map and a theory of *which* pretraining objective wins *where*.
- **Hypothesis:** No backbone dominates: objective type predicts the winner per task family (contrastive→semantics, MIM→texture/depth, segmentation-supervised→boundaries), with the pattern stable across probe capacities — falsified if one backbone Pareto-dominates.
- **Novelty:** UNVERIFIED
- **Protect:** — (merit)
- **Why kept:** Community-resource value: the matched-protocol matrix that absorbs killed 0012/0023 and grounds a dozen other survivors' backbone choices.

### W5-132 — SSL "object emergence" is a crop-statistics artifact
- **CanonicalID:** W5-132  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-A-0203
- **One-liner:** Test whether "emergent segmentation" in self-supervised ViT attention maps is a genuine objecthood representation or an artifact of the cropping-based augmentation statistics used in pretraining.
- **Problem:** Attention-based object emergence (DINO-style) is celebrated as evidence SSL learns objects; but random-crop augmentation makes centered, large objects statistically special, so the "emergence" may be an augmentation echo — the causal driver is untested.
- **Hypothesis:** Retraining with object-decentered cropping statistics substantially degrades attention-object alignment (>40% relative) without harming downstream classification — object emergence is largely an augmentation artifact, falsified if emergence survives decentered training.
- **Novelty:** UNVERIFIED
- **Protect:** HR+CI
- **Why kept:** Protected HR+CI: a causal intervention on one of SSL's most celebrated narratives.

### W5-133 — Object discovery or texture grouping?
- **CanonicalID:** W5-133  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-A-0266
- **One-liner:** Test whether unsupervised segmentation via SSL-feature clustering discovers *objects* or merely *contiguous texture regions*, using scenes where objecthood and texture segmentation disagree.
- **Problem:** Unsupervised segmentation methods report improving object metrics, but their clustering substrate may be texture coherence that only correlates with objects in curated benchmarks — on texture-object dissociated scenes the methods' true nature would show.
- **Hypothesis:** On dissociation scenes (multi-texture single objects, uniform-texture multi-object groups), SSL-clustering methods track texture boundaries in >70% of conflicts — "unsupervised object discovery" is largely texture grouping, falsified if methods follow objecthood cues (closure, continuity) over texture.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Perception-science dissociation methodology applied to a celebrated claim; the cheap correlational prelude to 0203's causal intervention.

### W5-134 — Texture-vs-shape verdict inverts for dense readouts
- **CanonicalID:** W5-134  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-A-0211
- **One-liner:** Re-measure texture-vs-shape bias in modern VFMs (DINOv2, CLIP, SAM-class) with dense-prediction-relevant stimuli, testing whether the CNN-era texture bias actually disappeared or merely moved.
- **Problem:** "Transformers are shape-biased" is now folklore based on classification-oriented cue-conflict tests; whether dense predictions (masks) follow shape or texture under conflict — the version that matters for segmentation — has not been measured.
- **Hypothesis:** Under texture-shape cue-conflict for segmentation (shape of A textured as B), modern VFM-based segmenters follow *texture boundaries* in >40% of cases despite classifying by shape — the bias verdict inverts between classification and dense readouts of the same backbone.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Within-model dissociation (same backbone, opposite bias verdicts by readout) would invalidate a folklore claim exactly where it is applied.

### W5-135 — In-context segmentation: abstraction or copying?
- **CanonicalID:** W5-135  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-A-0223
- **One-liner:** Determine whether in-context segmentation (SegGPT/Painter-style visual prompting) performs abstraction or sophisticated nearest-neighbor copying, via support-query relationship manipulations.
- **Problem:** In-context dense models appear to "understand" tasks from one example, but the mechanism — abstract task inference vs feature-matched label transfer — is undetermined, and the two predict different generalization limits.
- **Hypothesis:** Performance collapses (>50% relative) when support and query share task semantics but differ in low-level statistics (style-shifted supports), while remaining high for semantically-different but visually-similar supports — behavior tracks visual similarity, not task abstraction; falsified if the opposite pattern holds.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Mechanism dissociation with a 2×2 design (semantic-match × visual-match) that predicts generalization limits either way; the strongest of the several allegiance-dissociation ideas in the batch (kills 0257 by covering the sharper target).

### W5-136 — Platonic convergence is semantics-only at patch level
- **CanonicalID:** W5-136  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-A-0225
- **One-liner:** Test the "platonic convergence" claim at the *patch* level: are different VFMs' dense feature spaces converging to affinely equivalent representations, or does convergence hold only for global semantics?
- **Problem:** Evidence suggests foundation models converge toward shared representations at the global level; if dense/spatial features do not converge equivalently, model interchangeability assumptions (feature swapping, cross-model distillation, universal decoders) fail in unmapped ways.
- **Hypothesis:** Cross-model affine alignment of patch features achieves high fidelity for semantic content (class decodability preserved >90%) but low fidelity for geometric content (boundary/position decodability <50% preserved) — convergence is semantics-only, falsified if geometric content aligns equally well.
- **Novelty:** UNVERIFIED
- **Protect:** RM
- **Why kept:** Tests a fashionable theory (platonic representation hypothesis) exactly at the level where it should break; the semantic/geometric decomposition is a new instrument.

### W5-137 — Data vs method: the variance decomposition
- **CanonicalID:** W5-137  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-A-0207
- **One-liner:** Quantify how much of inter-VFM downstream variance is explained by training *data* overlap versus objective and architecture, using models with disclosed corpora.
- **Problem:** The community attributes model differences to objectives and architectures, but training-data composition is a massive uncontrolled variable; without decomposition, method-level conclusions drawn from model comparisons are unreliable.
- **Hypothesis:** For models with known corpora, a data-overlap kernel predicts pairwise downstream-behavior similarity (error correlation across a dense-task suite) better than objective or architecture indicators — data explains more variance than method, falsified if method indicators dominate.
- **Novelty:** UNVERIFIED
- **Protect:** RM
- **Why kept:** RM-protected: "data explains more than method" would force re-reading of the comparison literature, and the kernel-regression methodology will be fought over — the productive kind of controversy.

### W5-138 — Test non-monotonicity of pretraining scale for medical transfer: curated small…
- **CanonicalID:** W5-138  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-C-0289
- **One-liner:** Test non-monotonicity of pretraining scale for medical transfer: curated small pretraining can beat web-scale for specific modalities.
- **Problem:** "More pretraining data always helps downstream medical tasks" guides model selection, but distribution mismatch may make web-scale pretraining actively dilutive for some modalities.
- **Hypothesis:** For at least some modality/task pairs (e.g., ultrasound, OCT), models pretrained on smaller curated in-domain-adjacent corpora outperform web-scale-pretrained models of matched architecture after identical fine-tuning — and the crossover is predicted by a measurable domain-distance statistic.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Curation-beats-scale crossovers with a pre-hoc domain-distance predictor attack the "take the biggest checkpoint" default at its evidence base, for the modalities where mismatch is most plausible.

### W5-139 — Measure the true frozen-backbone ceiling for dense prediction with properly engineered…
- **CanonicalID:** W5-139  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-C-0301
- **One-liner:** Measure the true frozen-backbone ceiling for dense prediction with properly engineered multi-layer readouts.
- **Problem:** "Frozen backbones can't do dense prediction well" justifies universal fine-tuning; the claim is largely tested with naive single-layer readouts.
- **Hypothesis:** With multi-layer feature aggregation and modest decoders, frozen modern backbones close most of the gap to full fine-tuning on standard segmentation benchmarks — the believed necessity of fine-tuning reflects readout under-engineering, with the residual gap concentrated in domain-shifted settings.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The frozen-backbone ceiling with properly engineered multi-layer readouts tests the universal fine-tuning assumption; frozen deployment has large certification and serving implications.

### W5-140 — Objectness erosion: when continued SSL pretraining hurts promptable segmentation
- **CanonicalID:** W5-140  ·  **Cluster:** P13 — Representation & pretraining science of VFMs
- **SourceIDs:** IDEA-B-0300
- **One-liner:** Investigate the phenomenon that continued self-supervised pretraining (MAE-style) on target-domain data before supervised fine-tuning sometimes degrades promptable segmentation, testing whether reconstruction objectives erode the objectness/grouping structure that prompt decoding depends on.
- **Problem:** The domain-adaptive-pretraining recipe (SSL on target, then fine-tune) is standard advice inherited from NLP and classification, but promptable segmentation relies on representational properties (grouping, boundary salience) that reconstruction objectives do not preserve and may actively trade away—an unexamined recipe conflict.
- **Hypothesis:** MAE-style continued pretraining measurably degrades frozen-feature grouping quality (probeable before any fine-tuning) while improving pixel-reconstruction-aligned properties, the degradation propagates to prompted-segmentation performance in low-label fine-tuning regimes (insufficient supervision to rebuild grouping), and grouping-preserving SSL variants (contrastive or distillation-anchored) avoid the trap—defining which SSL is safe for promptable models.
- **Novelty:** UNVERIFIED
- **Protect:** REV · M
- **Why kept:** Auditor revive (stage2_audit.md §5): Killed on "instrument softness" (no settled grouping probe) — but survivors B-0129/B-0132 are building exactly that probe infrastructure; the reviewer's own almost-survived note says "if a robust grouping probe emerges from 0129/0132's work, rerun this." That condition is already funded.

## P14 — Composed pipelines & preprocessing skepticism (7)

### W5-141 — The box-to-mask error transfer function
- **CanonicalID:** W5-141  ·  **Cluster:** P14 — Composed pipelines & preprocessing skepticism
- **SourceIDs:** IDEA-B-0217
- **One-liner:** Characterize how upstream box-localization errors transform into downstream mask errors in detect-then-segment pipelines, and test whether training the segmenter under the detector's actual error distribution (rather than clean boxes) hardens the pipeline.
- **Problem:** Detectors and promptable segmenters are developed and evaluated separately; the coupling—how box jitter, scale error, and drift propagate through prompt conditioning into mask failure—is the unmodeled interface where pipelines actually break.
- **Hypothesis:** Mask degradation as a function of box perturbation is non-linear with a target-geometry-dependent cliff (small targets tolerate almost no box error), and matching the segmenter's training-time box-noise distribution to the deployed detector's measured error distribution recovers most of the pipeline loss at zero inference cost.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Detect-then-segment is the dominant production architecture and its interface is unmodeled.

### W5-142 — Assigner-induced bias against elongated objects
- **CanonicalID:** W5-142  ·  **Cluster:** P14 — Composed pipelines & preprocessing skepticism
- **SourceIDs:** IDEA-B-0223
- **One-liner:** Isolate how label-assignment rules in detector training (IoU thresholds, center sampling) systematically under-train on extreme-aspect-ratio objects (catheters, tubes, wires), separately from feature or anchor limitations.
- **Problem:** Elongated-object detection failures are attributed to features or anchors, but the training-time assigner silently discards or mislabels candidate-to-GT matches for thin objects (center points miss thin diagonal structures; IoU thresholds are unreachable), starving them of gradient signal.
- **Hypothesis:** Gradient-flow accounting shows elongated objects receive disproportionately few positive assignments under standard assigners, aspect-ratio-conditional assignment restores training signal and recovers a large share of the performance gap without any architectural change, and the effect explains cross-detector consistency of elongated-object failure.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** A training-logic fix, universal across detectors, for a safety-critical object family (catheters, wires) — and cheap to instrument via gradient-flow accounting.

### W5-143 — What does a detector add over change detection for static-camera monitoring?
- **CanonicalID:** W5-143  ·  **Cluster:** P14 — Composed pipelines & preprocessing skepticism
- **SourceIDs:** IDEA-B-0233
- **One-liner:** Rigorously measure the marginal value of learned object detection over classical background-model change detection for static-camera fire/smoke monitoring at matched false-positive budgets, identifying which detections genuinely require semantics.
- **Problem:** Static cameras permit strong background modeling that flags any appearance change; the expensive learned detector may only be needed to classify changes, not find them—but deployments run full-frame detection anyway, and nobody has cleanly decomposed the roles.
- **Hypothesis:** At matched FP budgets, change detection recovers the large majority of true events on static cameras (finding is cheap), learned semantics matter mainly for change triage (rejecting benign changes), and a change-gated detector architecture achieves equal recall at a fraction of the compute—with the residual detector-only detections concentrated in slow-onset events that defeat background models.
- **Novelty:** UNVERIFIED
- **Protect:** DM·CI
- **Why kept:** A deflationary question with large compute stakes that the monitoring literature has never asked cleanly.

### W5-144 — The hallucination-utility frontier of super-resolution for downstream dense prediction
- **CanonicalID:** W5-144  ·  **Cluster:** P14 — Composed pipelines & preprocessing skepticism
- **SourceIDs:** IDEA-B-0331
- **One-liner:** Using SR models with controllable generative strength (guidance/hallucination knobs), map the frontier between detail hallucination and downstream segmentation utility on gigapixel pathology and low-res monitoring—establishing when generative SR is a legitimate preprocessing stage versus a boundary-fabrication hazard.
- **Problem:** Generative SR is entering medical and monitoring pipelines on visual-quality evidence, while its effect on downstream boundary fidelity—the property those pipelines actually need—is uncharacterized as a function of generative strength.
- **Hypothesis:** Downstream segmentation quality is non-monotonic in SR generative strength (mild strength recovers resolvable structure; high strength fabricates confident boundaries that segmenters trace), the optimum differs systematically between texture-driven and boundary-driven tasks, and hallucinated-boundary harm is detectable without ground truth via SR-seed ensembling (fabricated details vary across seeds, real details don't)—yielding a deployable safety check.
- **Novelty:** UNVERIFIED
- **Protect:** DM
- **Why kept:** Generative SR is entering medical and monitoring pipelines on visual-quality evidence; this supplies the boundary-fidelity evidence and a deployable audit before the practice embeds silently.

### W5-145 — Noise as signal: does restoration destroy the forensic cues tiny-target detection relies on?
- **CanonicalID:** W5-145  ·  **Cluster:** P14 — Composed pipelines & preprocessing skepticism
- **SourceIDs:** IDEA-B-0338
- **One-liner:** Test whether denoising preprocessing harms detection of near-resolution-limit targets (distant smoke plumes, micro-calcifications) because sensor-noise interaction statistics around real structures carry discriminative information that restoration removes along with the noise.
- **Problem:** Denoising is applied universally on the assumption that noise only obscures, but at the resolution limit, how a faint structure perturbs the local noise field may be a genuine detection cue—one that cleaner-looking restored images no longer contain.
- **Hypothesis:** Detection performance for sub-5-pixel targets is measurably higher on raw than denoised inputs for detectors trained on each respectively (the noise-interaction cue is real and learnable), the effect reverses above a target-size crossover (noise becomes pure nuisance), and the crossover is predictable from target-contrast-to-noise ratios—yielding a size-conditional preprocessing rule that contradicts uniform-restoration practice.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** If restoration deletes the earliest detectable signal, uniform preprocessing practice is harming exactly the systems built for early detection (wildfire, screening).

### W5-146 — Compression that helps: does JPEG act as a matched filter for smoke?
- **CanonicalID:** W5-146  ·  **Cluster:** P14 — Composed pipelines & preprocessing skepticism
- **SourceIDs:** IDEA-B-0285
- **One-liner:** Test the counterintuitive observation that mild lossy compression sometimes improves smoke segmentation, evaluating the hypothesis that compression's frequency truncation suppresses exactly the high-frequency background clutter that generates smoke false positives.
- **Problem:** Preprocessing dogma treats compression purely as degradation, but if amorphous low-frequency targets like smoke gain discriminability when high-frequency distractors are removed, deployment pipelines are leaving free accuracy on the table—and the robustness literature's monotone-degradation assumption is wrong for a target class.
- **Hypothesis:** Segmentation quality for low-frequency amorphous targets is non-monotonic in compression strength with a measurable optimum at mild compression (the effect absent for high-frequency targets), the mechanism is spectral overlap between target and clutter (predictable per class from their power-spectra separation), and a learned band-suppression filter beats JPEG at the same principle—confirming the matched-filter account.
- **Novelty:** UNVERIFIED
- **Protect:** CI·CF
- **Why kept:** Beneficial degradation inverts preprocessing dogma and falsifies the robustness literature's monotone-degradation assumption for a target class.

### W5-147 — Audit window-position bias in sliding-window inference: prediction quality varies…
- **CanonicalID:** W5-147  ·  **Cluster:** P14 — Composed pipelines & preprocessing skepticism
- **SourceIDs:** IDEA-C-0273
- **One-liner:** Audit window-position bias in sliding-window inference: prediction quality varies systematically between window centers and edges, hidden by overlap blending.
- **Problem:** 3D/high-res pipelines predict in overlapping windows and blend; the blend obscures whether voxels near window edges receive systematically worse predictions — and whether blending weights are anywhere near optimal.
- **Hypothesis:** Per-voxel error conditioned on within-window position shows a reproducible center-to-edge quality gradient (context truncation effect), Gaussian blending under-corrects it, and empirically fitted position-dependent weights improve final accuracy at zero model change — a free, measurable pipeline win.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Window-position error profiling of sliding-window inference exposes a potential free accuracy win in a universally used pipeline; near-zero risk and immediate utility.

## P15 — Medical FM capabilities & deployment safety (16)

### W5-148 — Models hallucinate surgically removed organs
- **CanonicalID:** W5-148  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-A-0118
- **One-liner:** Test how segmentation models fail on post-surgical and anatomically variant patients, quantifying the "atlas prior" dependence of modern learned models.
- **Problem:** Learned models may implicitly encode normal-anatomy atlases; post-surgical absence (resected organs), transplants, and congenital variants then trigger hallucinated structures — a patient-safety failure mode without a benchmark.
- **Hypothesis:** On post-resection cases, models hallucinate the absent organ (predict >20% of its typical volume) in ≥40% of cases, and hallucination rate correlates with the organ's positional consistency in training data — models segment "where organs usually are."
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Patient-safety silent failure with a mechanism (positional-consistency prior) and a benchmark deliverable; the medical twin of 0185's absence benchmark.

### W5-149 — Why nnU-Net still wins: causal component attribution
- **CanonicalID:** W5-149  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-A-0093 + IDEA-C-0300  (= MERGE-27)
- **One-liner:** Matched-budget component swaps (3D context handling, augmentation policy, resolution/preprocessing-normalization stack) causally decompose the nnU-Net-vs-foundation-model gap.
- **Problem:** nnU-Net-class specialists still beat adapted foundation models on medical benchmarks, but which components carry the advantage is unknown — the attribution that decides where medical-segmentation investment should go.
- **Hypothesis:** A small number of transferable components (3D context, augmentation policy, preprocessing/normalization) explain most of the nnU-Net-vs-VFM gap under matched budgets, and grafting them onto VFM pipelines closes most of it — falsified if the advantage is irreducibly architectural.
- **Novelty:** UNVERIFIED
- **Protect:** HR+RM
- **Why kept:** Cross-batch convergence (A's component swaps vs VFMs; C-0300's architecture-vs-preprocessing attribution); the strategic fork of medical segmentation attacked with causal decomposition rather than another bake-off. Coordinate with A-0245 (CONF-12).

### W5-150 — Laterality blindness: invalid flip invariance and the left/right capability probe
- **CanonicalID:** W5-150  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-A-0100 + IDEA-C-0149  (= MERGE-23)
- **One-liner:** Flip-TTA imposes an anatomically invalid invariance inside standard pipelines, and medical FMs may be unable to represent left vs right at all — a never-event-grade safety audit from flipped-input probes.
- **Problem:** Horizontal-flip augmentation/TTA is standard in medical pipelines and challenge winners although anatomy is lateralized, and nobody has audited whether medical foundation models can reliably encode laterality — the capability wrong-side interventions depend on.
- **Hypothesis:** Flip-TTA measurably degrades performance on lateralized structures while helping symmetric ones, and flip-consistency probes show medical FMs mis-encode left/right at rates far above never-event tolerances; both effects trace to flip-symmetric training practice.
- **Novelty:** UNVERIFIED
- **Protect:** CI+CF
- **Why kept:** Merged pipeline-level (A-0100) and capability-level (C-0149) laterality audits: same stimuli, same clinical never-event stake, one cheap decisive paper.

### W5-151 — The exchange rate between radiology reports and pixel labels
- **CanonicalID:** W5-151  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-B-0156
- **One-liner:** Measure how many report-supervised images (spatial constraints parsed from routine radiology text) equal one expert pixel-labeled image for training lesion segmenters, establishing a supervision exchange rate.
- **Problem:** Hospitals hold millions of image-report pairs and few masks, but the quantitative value of report text as segmentation supervision has never been priced against pixel labels.
- **Hypothesis:** Report-derived constraints (laterality, lobe, size mentions) provide supervision worth a stable, measurable fraction of a pixel label—with the exchange rate varying predictably by finding type (focal high, diffuse low)—so optimal budgets mix both sources according to the measured rate.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Prices an idle hospital-scale data asset with a clean experimental design; directly changes annotation budget decisions.

### W5-152 — Absence statements as supervision: teaching models what is not there
- **CanonicalID:** W5-152  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-B-0182
- **One-liner:** Exploit explicit negative findings in radiology reports ("no pneumothorax", "no focal lesion") as verified-absence supervision, testing whether absence-aware training reduces hallucinated segmentations more effectively than positive-only training augmented with generic negatives.
- **Problem:** Reports certify absence with expert authority—information no image-only pipeline possesses—yet current text-mining pipelines discard negative findings, and models hallucinate exactly the findings experts explicitly ruled out.
- **Hypothesis:** Absence-supervised training reduces false-positive segmentation of the certified-absent classes substantially more than equal volumes of unlabeled or randomly negative data, because certified absence provides class-specific hard negative supervision at the image level.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Report negations are free, expert-authored, and aimed precisely at the hallucinations that cause alarm fatigue.

### W5-153 — Contrast-enhancement differencing as automatic vessel ground truth—and its hidden bias
- **CanonicalID:** W5-153  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-B-0184
- **One-liner:** Use registered pre/post-contrast CT differencing to generate automatic vessel labels at scale, and characterize the systematic bias this induces (only perfused vessels enhance) on models trained from such labels.
- **Problem:** Contrast physics offers free, precise vessel labels, but the labeling mechanism is physiologically selective—occluded and hypo-perfused vessels never enhance—creating a training signal whose bias directly opposes key clinical use cases (finding occlusions).
- **Hypothesis:** Models trained on enhancement-derived labels inherit measurable blindness to non-enhancing vessel segments (quantified on occlusion-annotated test sets) even while excelling on healthy vasculature, and mixing a small fraction of expert-labeled pathological cases disproportionately corrects the bias.
- **Novelty:** UNVERIFIED
- **Protect:** CI·DM
- **Why kept:** A paradigm case of physically generated labels whose bias directly opposes the clinical use, with the correction (fraction of expert pathological labels) priced by the same experiment.

### W5-154 — Measure the pairwise-reasoning gap: FMs cannot compare two scans (change detection) even…
- **CanonicalID:** W5-154  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-C-0150
- **One-liner:** Measure the pairwise-reasoning gap: FMs cannot compare two scans (change detection) even when they analyze each well individually.
- **Problem:** Longitudinal comparison is a core radiology act; FM architectures and pretraining see single images, and their comparison ability is untested.
- **Hypothesis:** On controlled change-detection tasks (synthetic and registered-pair real data), FM-based pipelines perform near chance for changes below a large magnitude, while trivially trained siamese baselines succeed — a structural, not scale, deficiency.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Change detection (pairwise reasoning) is the modal clinical act and a plausibly structural blind spot of single-image FMs; the change-magnitude-ladder design is clean and decisive.

### W5-155 — Test whether FMs lost metric scale: physical-size estimation fails because pretraining…
- **CanonicalID:** W5-155  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-C-0151
- **One-liner:** Test whether FMs lost metric scale: physical-size estimation fails because pretraining pipelines discard pixel spacing.
- **Problem:** Clinical decisions hinge on millimeters, but FM preprocessing resizes images, destroying the mapping between pixels and physical units.
- **Hypothesis:** FM features cannot support size estimation beyond relative-within-image judgments (probes fail to predict physical size across images with varying spacing), and injecting spacing as a side input at probe time restores accuracy — the information is destroyed, not unused.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Metric-scale destruction (pixel spacing discarded by preprocessing) is a crisp information-availability audit with a definitive spacing-injection test; measurement is half of radiology.

### W5-156 — Test whether report-supervised FMs learn the distribution of *reported* findings,…
- **CanonicalID:** W5-156  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-C-0162
- **One-liner:** Test whether report-supervised FMs learn the distribution of *reported* findings, systematically missing unreported incidentals.
- **Problem:** Reports document what radiologists chose to mention; findings outside the clinical question (incidentals) are under-reported, biasing FM supervision.
- **Hypothesis:** On images with expert re-reads that recover unreported findings, report-trained FMs detect reported-type findings well but miss unreported-type ones at rates predicted by reporting-frequency statistics — the model inherits the reporting policy, not the visual truth.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR
- **Why kept:** PROTECTED (high-risk/high-reward). "Models learn the reporting policy, not the visual truth" is a supervision-bias account of FM blind spots that only a re-read study can verify — expensive, but no cheaper design answers it.

### W5-157 — Determine the effective resolution ceiling of medical FMs: which subtle findings live…
- **CanonicalID:** W5-157  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-C-0164
- **One-liner:** Determine the effective resolution ceiling of medical FMs: which subtle findings live below what the representation can carry?
- **Problem:** Micro-findings (microcalcifications, early interstitial change) may fall below FM effective spatial bandwidth after tokenization and pooling — the field lacks a frequency-resolved capability map.
- **Hypothesis:** FM feature sensitivity to controlled high-frequency perturbations cuts off at a measurable spatial frequency per model, and clinical findings whose discriminative energy lies above the cutoff show near-chance FM performance regardless of fine-tuning — a physics-style capability bound.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** A frequency-response capability bound for medical FMs — a physics-style spec sheet telling users which findings are unreachable at any fine-tuning budget.

### W5-158 — Measure salience suppression: FMs detect the most prominent lesion and systematically…
- **CanonicalID:** W5-158  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-C-0173
- **One-liner:** Measure salience suppression: FMs detect the most prominent lesion and systematically under-report additional ones.
- **Problem:** Multi-lesion sensitivity is clinically vital (staging, metastasis counts); representation-level "winner-take-most" behavior would cap it independent of thresholds.
- **Hypothesis:** Per-lesion detection probability conditioned on lesion properties drops significantly when a more salient lesion is present in the same image (versus matched single-lesion controls), the suppression strengthens with salience gap, and it persists across detection thresholds — a representational, not calibration, effect.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR
- **Why kept:** PROTECTED (high-risk/high-reward). Salience suppression — the presence of a prominent lesion lowering detection of others — is a representational multi-lesion failure invisible to aggregate sensitivity, with severe staging consequences if real.

### W5-159 — Clinical-measurement validity of mask metrics [E]
- **CanonicalID:** W5-159  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-B-0081 + IDEA-C-0177  (= MERGE-24)
- **One-liner:** Which segmentation metric predicts errors in the quantities clinicians consume (volumes, diameters, growth rates, boundary-derived indices) — and do FM-vs-specialist Dice-parity claims survive on those measures?
- **Problem:** Papers optimize and rank by Dice/IoU while clinicians consume derived measurements; the metric-to-utility mapping is assumed rather than measured, and Dice-parity adoption claims may hide clinical-measure failure.
- **Hypothesis:** For thin and small structures, boundary-localized metrics predict downstream clinical-measurement error far better than region metrics; metric-induced method rankings materially disagree with utility-induced rankings, and generalist FMs that match specialists on Dice lose on the clinically consumed measures.
- **Novelty:** UNVERIFIED
- **Protect:** REV · M
- **Why kept:** Auditor revive R3 (B-0081, 'the missing root-validity question of the medical program') merged with Batch C's highest-scoring survivor (C-0177, avg 4.46; C-0232 already folded into it): identical machinery — derive clinical measurements from public-model predictions and regress errors on mask metrics. The one eval-genre addition, admitted because it is outcome-anchored.

### W5-160 — Run the slice-order checkerboard test on "3D" models: feed volumes with permuted slice…
- **CanonicalID:** W5-160  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-C-0326
- **One-liner:** Run the slice-order checkerboard test on "3D" models: feed volumes with permuted slice order and see whether claimed volumetric reasoning notices.
- **Problem:** 3D architectures claim volumetric context use; if predictions are unchanged under slice permutation, the models are functionally 2.5D and the papers' mechanism claims fail.
- **Hypothesis:** A measurable fraction of published 3D models show near-identical performance under local slice permutations — their receptive fields or learned features do not exploit inter-slice order, contradicting the stated rationale for their 3D design.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** PROTECTED (cheap-to-falsify). Slice-order permutation testing of "3D reasoning" claims is zero-training mechanism verification for an architecture class; absorbs 0153's benchmark-partitioning framing into one paper.

### W5-161 — Apply the mask-the-lesion test systematically to medical detection papers: does the…
- **CanonicalID:** W5-161  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-C-0332
- **One-liner:** Apply the mask-the-lesion test systematically to medical detection papers: does the detector still fire on surrounding context when the finding itself is erased?
- **Problem:** Reported detection performance may ride on contextual shortcuts (position, co-occurring devices, patient habitus); the direct occlusion control is quick and rarely reported.
- **Hypothesis:** For a measurable fraction of published-style medical detectors, inpainting the lesion region leaves detection confidence above the decision threshold on many cases — a context-shortcut prevalence estimate per model and dataset that reframes their claimed sensitivity.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** PROTECTED (cheap-to-falsify). The mask-the-lesion occlusion audit yields a per-model context-shortcut prevalence number that belongs next to every reported medical-detection AUC.

### W5-162 — The small-lesion sensitivity law: foundation models vs specialists
- **CanonicalID:** W5-162  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-A-0096
- **One-liner:** Establish the sensitivity-vs-lesion-size law for medical VFMs versus specialized detectors, testing whether foundation models have a systematically worse small-lesion exponent.
- **Problem:** Missing small lesions is the clinically catastrophic failure; whether VFM adaptation sacrifices small-lesion sensitivity relative to purpose-built models is unquantified as a scaling relationship.
- **Hypothesis:** Detection sensitivity vs lesion diameter follows a sigmoid whose midpoint is ≥30% larger (worse) for adapted VFMs than for specialized 3D models at matched overall Dice — aggregate parity hides small-lesion inferiority.
- **Novelty:** UNVERIFIED
- **Protect:** REV · M
- **Why kept:** Auditor revive (stage2_audit.md §5): The kill rationale ("survivor 0161 carries the general size-law science") conflates two different laws: 0161 is about *tokenization* floors in natural images; 0096 is about *sensitivity* (detection, not delineation) at matched aggregate Dice in 3D clinical data — the number regulators and radiology procurement actually need.

### W5-163 — Restain-and-register IHC as molecular ground truth for H&E
- **CanonicalID:** W5-163  ·  **Cluster:** P15 — Medical FM capabilities & deployment safety
- **SourceIDs:** IDEA-B-0177
- **One-liner:** Generate automatic cell/structure labels for H&E histology by restaining the same physical slides with IHC markers and registering the pair, then characterize and correct the registration-induced label noise for training.
- **Problem:** Histology annotation demands pathologist time and suffers known inter-rater problems, while chemistry can produce molecularly defined labels—if the registration noise between stains can be handled.
- **Hypothesis:** Restain-registered IHC labels train H&E segmenters that match or exceed pathologist-annotation-trained models on molecularly verifiable targets, provided training explicitly models the spatially structured registration noise (which naive training does not tolerate).
- **Novelty:** UNVERIFIED
- **Protect:** REV · HRHR-gated
- **Why kept:** Auditor revive (stage2_audit.md §5): Revive **conditionally**: hold as a partnership-gated HRHR slot with a hard go/no-go (existing public restain-registered pairs, e.g.

## P16 — Synthetic data & derived supervision resources (7)

### W5-164 — Does generative augmentation actually cover the tail it promises to fix?
- **CanonicalID:** W5-164  ·  **Cluster:** P16 — Synthetic data & derived supervision resources
- **SourceIDs:** IDEA-B-0186
- **One-liner:** Measure the mode coverage of diffusion-generated medical images against the true long tail of pathology presentations, testing whether synthesis concentrates near dataset modes precisely where data was never scarce.
- **Problem:** Synthetic data is prescribed as the cure for rare presentations, but generators are trained on the same skewed distributions and may reproduce the skew—delivering volume without coverage.
- **Hypothesis:** Synthetic pathology images occupy a measurably narrower support than real data (quantified by coverage metrics on curated rare-presentation references), and segmentation gains from synthetic augmentation concentrate on already-common presentations while rare-presentation performance is unchanged or harmed.
- **Novelty:** UNVERIFIED
- **Protect:** DM
- **Why kept:** If synthesis reproduces the skew it is prescribed to fix, the field's main scarcity remedy is a placebo.

### W5-165 — Synthetic-fraction dose-response thresholds
- **CanonicalID:** W5-165  ·  **Cluster:** P16 — Synthetic data & derived supervision resources
- **SourceIDs:** IDEA-A-0285 + IDEA-B-0190  (= MERGE-12)
- **One-liner:** Sweep within-class and global synthetic fractions across two generator families; endpoints: rare-class real-instance recall inversion, silent OOD-robustness decay, and a label-free probe detector — dose rules for the field's main scarcity remedy.
- **Problem:** The obvious long-tail fix — synthesize the rare classes — has a specific failure mode: if rare-class training data is predominantly synthetic, models may learn "rare class = synthetic-looking," failing on real rare instances precisely where the fix was aimed; this coupling is untested.
- **Hypothesis:** When synthetic fraction within a class exceeds ~70%, real-instance recall for that class *decreases* relative to no-augmentation baselines (artifact-shortcut regime), while below it augmentation helps — a within-class mixing threshold that current practice routinely violates for the rarest classes.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Same fraction-ladder machinery generated twice; two failure modes (rare-class inversion, robustness poisoning) of one dose-response curve.

### W5-166 — The inpainting fingerprint: do models learn the lesion or the paste?
- **CanonicalID:** W5-166  ·  **Cluster:** P16 — Synthetic data & derived supervision resources
- **SourceIDs:** IDEA-B-0189
- **One-liner:** Test whether segmentation models trained on lesions synthetically inpainted into healthy images learn to detect the generative fingerprint (boundary statistics, noise discontinuities) rather than lesion appearance, by evaluating on fingerprint-free presentations.
- **Problem:** Inpainting-based augmentation reports strong in-benchmark gains, but if models key on synthesis artifacts, the gains are circular—the model detects the augmentation, not the disease.
- **Hypothesis:** A detector can distinguish inpainted from real lesions at high accuracy using local statistics (proving a fingerprint exists), models trained on inpainted data degrade disproportionately on real-only test sets versus inpainted test sets, and artifact-suppressed synthesis (noise-matched blending) closes part of the circularity gap.
- **Novelty:** UNVERIFIED
- **Protect:** CI·CF
- **Why kept:** A circularity flaw in a fast-spreading augmentation practice, detectable with a cheap classifier.

### W5-167 — Too-clean ground truth: when perfect synthetic labels teach the wrong tolerance
- **CanonicalID:** W5-167  ·  **Cluster:** P16 — Synthetic data & derived supervision resources
- **SourceIDs:** IDEA-B-0200
- **One-liner:** Test whether the pixel-perfect labels of rendered data teach segmentation models boundary-tolerance expectations that mismatch real-world annotation conventions, and whether deliberately degrading synthetic labels toward realistic annotator statistics improves real-data performance.
- **Problem:** Synthetic pipelines celebrate their perfect geometric labels, but models fine-tuned or evaluated against human-annotated data face systematically looser, convention-laden boundaries—a mismatch in the label-generating process itself.
- **Hypothesis:** Models trained on geometrically perfect synthetic labels develop over-sharp boundary posteriors that are miscalibrated against human-annotated evaluations, and injecting realistic annotator-noise models into synthetic labels (matched to target-dataset conventions) improves both accuracy and calibration on real benchmarks.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** Inverts a data-quality intuition and prescribes deliberately degrading labels — cheap to run, hard to ignore, and connects synthetic-data practice to the annotation-noise literature (0037, 0082).

### W5-168 — Which realism factor buys sim-to-real transfer
- **CanonicalID:** W5-168  ·  **Cluster:** P16 — Synthetic data & derived supervision resources
- **SourceIDs:** IDEA-A-0283
- **One-liner:** Run factor-controlled sim-to-real for segmentation — independently making geometry, texture, lighting, and sensor-model real versus synthetic — to identify which realism factor actually buys transfer for dense tasks.
- **Problem:** "Realism" in synthetic data is treated as one axis, but rendering budgets must be allocated across factors; dense prediction may need geometric realism far more than photometric realism (or vice versa) — the factor attribution has not been done for segmentation.
- **Hypothesis:** Sensor-model realism (noise, optics, compression) and geometric layout realism dominate transfer for segmentation (together >70% of the sim-to-real gap closure), while texture photorealism — where most rendering effort goes — contributes <15% — falsified if photorealism dominates.
- **Novelty:** UNVERIFIED
- **Protect:** — (merit)
- **Why kept:** Honest 2⁴ factorial causal design answering the budget question every synthetic-data team faces; absorbs killed 0281/0290's fidelity questions into one framework.

### W5-169 — Procedural beats diffusion on web-sparse phenomena
- **CanonicalID:** W5-169  ·  **Cluster:** P16 — Synthetic data & derived supervision resources
- **SourceIDs:** IDEA-A-0287
- **One-liner:** Compare procedural (physics/graphics) generation against diffusion-model generation for training data on *out-of-web-distribution* phenomena (smoke, transparency, medical), testing whether generative models can synthesize what they never saw well enough to teach it.
- **Problem:** Diffusion generators are trained on web data, so their coverage of exactly the phenomena that need synthetic data (rare, hard-to-photograph) is suspect; procedural generation has no such circularity — but the comparison for segmentation training value has not been run.
- **Hypothesis:** For web-underrepresented phenomena, procedural data beats diffusion-generated data as training material (>5 IoU downstream) despite lower photorealism, with diffusion data exhibiting mode-collapse toward web-typical instances (measurable as lower coverage of the phenomenon's physical parameter space) — falsified if diffusion data wins on these domains.
- **Novelty:** UNVERIFIED
- **Protect:** — (merit)
- **Why kept:** Exposes the circularity limit of generative augmentation with a measurable mechanism (parameter-space coverage); supplies the data strategy for the smoke and transparency programs (0122, 0141).

### W5-170 — Mask-MAE prior from unpaired mask archives
- **CanonicalID:** W5-170  ·  **Cluster:** P16 — Synthetic data & derived supervision resources
- **SourceIDs:** IDEA-A-0278
- **One-liner:** Learn label-space priors by masked autoencoding on *unpaired* segmentation masks (no images), and test whether such shape/layout priors improve label-efficient segmentation when injected as a regularizer.
- **Problem:** Massive mask archives exist without usable images (privacy-stripped medical, licensing-orphaned datasets); whether label-space structure alone — shapes, adjacencies, layouts — carries transferable value has not been tested.
- **Hypothesis:** A mask-MAE prior trained on unpaired masks, used to regularize low-label training (penalizing unlikely label configurations), improves 10-label-regime performance by >3 mIoU on structurally regular domains (anatomy, streets) and ~0 on unstructured ones — label-space structure is real, transferable, and domain-regularity-dependent.
- **Novelty:** UNVERIFIED
- **Protect:** REV · HRHR-build
- **Why kept:** Auditor revive (stage2_audit.md §5): The kill reason ("builds a thing rather than tests a claim") is wrong on its face — the structured-vs-unstructured interaction *is* the falsifiable claim, and the convention-encoding risk is a feature: it makes this the constructive twin of survivor A-0007. Highest-priority revive.

## P17 — Detection–segmentation interface & instance science (6)

### W5-171 — Measure the equivariance conflict: box regression rewards translation-sensitive features…
- **CanonicalID:** W5-171  ·  **Cluster:** P17 — Detection–segmentation interface & instance science
- **SourceIDs:** IDEA-C-0179
- **One-liner:** Measure the equivariance conflict: box regression rewards translation-sensitive features while mask prediction demands equivariance, and shared backbones must compromise.
- **Problem:** Multi-task det+seg models share features between objectives with opposing symmetry requirements; the compromise has never been measured as such.
- **Hypothesis:** Backbone feature equivariance (response shift under input shift) in jointly trained models sits between the values of detection-only and segmentation-only twins, and its position on that axis predicts which task the joint model sacrifices — equivariance is the contested resource.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Equivariance as the contested resource in det+seg multi-task learning replaces loss-weight folklore with a measurable, designable quantity.

### W5-172 — Test the amodal-modal conflict: detectors learn amodal object extent while segmentation…
- **CanonicalID:** W5-172  ·  **Cluster:** P17 — Detection–segmentation interface & instance science
- **SourceIDs:** IDEA-C-0187
- **One-liner:** Test the amodal-modal conflict: detectors learn amodal object extent while segmentation learns visible (modal) extent, corrupting shared features under occlusion.
- **Problem:** Boxes routinely cover occluded object parts, masks never do; joint training feeds features contradictory supervision precisely on occluded regions.
- **Hypothesis:** In occlusion-stratified evaluation, joint det+seg models show a characteristic error signature absent in single-task twins — mask over-extension into occluded regions and box under-coverage — with magnitude proportional to occlusion rate in training data.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The amodal-modal supervision contradiction is a precise, occlusion-conditioned account of a known-but-unattributed error pattern, with a strong synthetic control arm.

### W5-173 — Show that competing instance-segmentation paradigms differ almost entirely on boundary…
- **CanonicalID:** W5-173  ·  **Cluster:** P17 — Detection–segmentation interface & instance science
- **SourceIDs:** IDEA-C-0190
- **One-liner:** Show that competing instance-segmentation paradigms differ almost entirely on boundary pixels — and agree elsewhere.
- **Problem:** Paradigm debates (top-down vs bottom-up vs query-based) cite aggregate AP, obscuring where the paradigms actually behave differently.
- **Hypothesis:** Per-pixel agreement analysis shows inter-paradigm disagreement concentrates within a thin boundary band (with interior agreement near ceiling), implying paradigm choice is a boundary-handling choice — and boundary-band metrics reorder the paradigm ranking relative to AP.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Per-pixel agreement decomposition showing paradigms differ almost only at boundaries would reframe paradigm debates as boundary-handling choices — cheap, clarifying, and probably true.

### W5-174 — Show mask-classification architectures secretly perform detection: their queries have…
- **CanonicalID:** W5-174  ·  **Cluster:** P17 — Detection–segmentation interface & instance science
- **SourceIDs:** IDEA-C-0192
- **One-liner:** Show mask-classification architectures secretly perform detection: their queries have box-like receptive behavior, inheriting detection's failure modes.
- **Problem:** Mask-classification (query-decoder) segmentation is presented as a departure from detection, but its queries may functionally re-implement boxes — importing crowding and duplicate pathologies unacknowledged.
- **Hypothesis:** Query attention footprints in mask-classification models are compact and box-approximable (high IoU between attention support and fitted boxes), and the models exhibit detection-typical failures (crowding misses, duplicate-merge errors) at rates predicted by the box-approximability score.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** PROTECTED (counter-intuitive). Mask-classification queries functioning as boxes explains inherited detection failures and prevents the field rediscovering detection fixes under new names — a lineage audit with predictive content.

### W5-175 — Show that deriving lesion detection from segmentation post-processing destroys calibrated…
- **CanonicalID:** W5-175  ·  **Cluster:** P17 — Detection–segmentation interface & instance science
- **SourceIDs:** IDEA-C-0196
- **One-liner:** Show that deriving lesion detection from segmentation post-processing destroys calibrated lesion-level confidence, and quantify the decision cost.
- **Problem:** Medical pipelines often segment then extract lesions by connected components, assigning ad-hoc confidences (max/mean pixel score) whose decision-theoretic quality is unexamined.
- **Hypothesis:** Lesion-level confidences derived from pixel scores are systematically miscalibrated (size-dependent bias: large lesions overconfident) and rank lesions worse than detection-native confidence at matched localization quality, measurably degrading downstream triage decisions at fixed review budgets.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The pixel-to-lesion confidence conversion problem is unformalized yet sits directly under clinical triage workflows; the size-dependent miscalibration hypothesis is specific and checkable.

### W5-176 — Test whether sliding-window 3D segmentation loses whole-object evidence that…
- **CanonicalID:** W5-176  ·  **Cluster:** P17 — Detection–segmentation interface & instance science
- **SourceIDs:** IDEA-C-0204
- **One-liner:** Test whether sliding-window 3D segmentation loses whole-object evidence that detection-style global context retains — on large lesions exceeding window size.
- **Problem:** 3D medical segmentation processes fixed windows for memory reasons; objects larger than the window are never seen whole, unlike in detection-style whole-volume approaches.
- **Hypothesis:** Segmentation error on lesions larger than the inference window grows discontinuously at the window-size threshold (controlling for lesion size effects below it), and providing coarse whole-volume context (low-res global pass) removes the discontinuity — proving a window-induced, not size-induced, failure.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The window-size discontinuity on large lesions is a hidden systematic failure of universal sliding-window practice, testable with a clean regression-discontinuity design and a cheap global-context intervention.

## P18 — Boundary error science & loss metrology (9)

### W5-177 — Decompose segmentation boundary error into image-aleatoric, annotation-protocol, and…
- **CanonicalID:** W5-177  ·  **Cluster:** P18 — Boundary error science & loss metrology
- **SourceIDs:** IDEA-C-0205
- **One-liner:** Decompose segmentation boundary error into image-aleatoric, annotation-protocol, and model-bias components with a reusable methodology.
- **Problem:** Boundary error is reported as one number, conflating irreducible image ambiguity, labeling convention, and actual model deficiency — making cross-paper progress claims uninterpretable.
- **Hypothesis:** The three components are separable using (a) multi-rater data for protocol variance, (b) local image-gradient statistics for aleatoric floor, and (c) residual for model bias — and across modern models, the model-bias component is a minority share of total boundary error on standard benchmarks.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The boundary error budget (image-aleatoric / annotation-protocol / model-bias) is the foundational accounting that the rest of C8 consumes; if model bias is a minority share, boundary-method research needs redirection.

### W5-178 — Measure the physics floor: partial-volume effects and slice thickness define a computable…
- **CanonicalID:** W5-178  ·  **Cluster:** P18 — Boundary error science & loss metrology
- **SourceIDs:** IDEA-C-0206
- **One-liner:** Measure the physics floor: partial-volume effects and slice thickness define a computable lower bound on boundary error in medical imaging.
- **Problem:** Boundary metrics are compared to zero as the implicit ideal, though imaging physics makes sub-PSF boundary localization information-theoretically limited.
- **Hypothesis:** A floor computed from point-spread function and voxel anisotropy predicts the plateau of boundary accuracy across models and datasets; models at the floor cannot be distinguished by boundary metrics, and reported "improvements" below the floor are noise.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Physics-derived boundary-metric floors (PSF, voxel anisotropy) calibrate when boundary "progress" is metrological illusion — a missing yardstick for an entire evaluation culture.

### W5-179 — Derive and verify the systematic inward/outward boundary bias induced by cross-entropy…
- **CanonicalID:** W5-179  ·  **Cluster:** P18 — Boundary error science & loss metrology
- **SourceIDs:** IDEA-C-0208
- **One-liner:** Derive and verify the systematic inward/outward boundary bias induced by cross-entropy training under class imbalance.
- **Problem:** Boundary placement bias is observed anecdotally (models "shrink" rare structures) but lacks an analytic account tied to the loss.
- **Hypothesis:** The stationary decision boundary under pixel-wise CE sits at a posterior threshold displaced from the true boundary by a computable function of local class prior and label noise — predicting per-structure signed bias that matches measured displacement fields across datasets.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** A closed-form displacement-bias prediction from cross-entropy under class imbalance is rare theory-with-verification, and it predicts a correctable systematic error in clinical volumetry.

### W5-180 — Redo method comparison statistics accounting for spatial autocorrelation of boundary… [E]
- **CanonicalID:** W5-180  ·  **Cluster:** P18 — Boundary error science & loss metrology
- **SourceIDs:** IDEA-C-0210
- **One-liner:** Redo method comparison statistics accounting for spatial autocorrelation of boundary errors — standard tests overstate significance.
- **Problem:** Boundary-error comparisons treat per-pixel or per-case errors as independent; boundary errors are strongly spatially autocorrelated, shrinking effective sample sizes.
- **Hypothesis:** Applying autocorrelation-corrected inference (effective-N adjustment, block bootstrap along boundaries) to published-style comparisons removes statistical significance from a substantial fraction of boundary-metric "wins" while leaving region-metric conclusions largely intact.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Spatial-autocorrelation-corrected inference could remove statistical significance from a substantial fraction of boundary-metric "wins" — statistics repair with real teeth, imported from a mature discipline.

### W5-181 — Detect annotation-tool fingerprints in ground-truth boundaries and quantify their effect… [E]
- **CanonicalID:** W5-181  ·  **Cluster:** P18 — Boundary error science & loss metrology
- **SourceIDs:** IDEA-C-0212
- **One-liner:** Detect annotation-tool fingerprints in ground-truth boundaries and quantify their effect on benchmark comparisons.
- **Problem:** Polygon tools, brushes, and level-set-assisted tools each impose characteristic boundary statistics (vertex spacing, curvature spectra, smoothness) that become part of "ground truth" invisibly.
- **Hypothesis:** The annotation tool is identifiable from boundary statistics alone at high accuracy, models trained on one tool's labels score systematically higher against same-tool test labels (tool-matching bonus), and part of cross-dataset "generalization gaps" is tool mismatch rather than image-domain shift.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** PROTECTED (counter-intuitive). Annotation-tool forensics — ground truth carrying identifiable tool fingerprints that confer tool-matching score bonuses — is a wholly unexplored confound in every cross-dataset boundary comparison.

### W5-182 — Extract sub-pixel boundary estimates from logit gradients: models know boundary positions…
- **CanonicalID:** W5-182  ·  **Cluster:** P18 — Boundary error science & loss metrology
- **SourceIDs:** IDEA-C-0214
- **One-liner:** Extract sub-pixel boundary estimates from logit gradients: models know boundary positions more precisely than their argmax masks express.
- **Problem:** Standard mask extraction discretizes at pixel resolution, discarding the continuous structure of the network's output field around boundaries.
- **Hypothesis:** Sub-pixel boundary localization derived from the logit field's zero-crossing interpolation beats argmax-mask boundaries against high-resolution reference truth by a consistent margin — demonstrating recoverable precision that standard evaluation and deployment throw away.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** PROTECTED (cheap counter-intuitive). Sub-pixel boundary readout from logit zero-crossings — free precision that standard argmax evaluation discards, reframing boundary quality as partly a readout problem.

### W5-183 — Perform bias-variance decomposition of boundary displacement fields: model boundary…
- **CanonicalID:** W5-183  ·  **Cluster:** P18 — Boundary error science & loss metrology
- **SourceIDs:** IDEA-C-0218
- **One-liner:** Perform bias-variance decomposition of boundary displacement fields: model boundary errors are directional and consistent, not random.
- **Problem:** Boundary error metrics are unsigned magnitudes, hiding whether models systematically displace boundaries (bias) or scatter around truth (variance) — different problems with different fixes.
- **Hypothesis:** Across seeds, per-location mean displacement (bias field) accounts for the majority of squared boundary error in trained segmenters, bias fields are reproducible across architectures (image-driven), and simple post-hoc bias-field correction improves boundaries more than typical loss innovations.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Signed bias/variance decomposition of boundary displacement: if reproducible bias dominates, a cheap post-hoc correction beats years of loss innovation — a high-leverage reframing with reusable machinery.

### W5-184 — Test whether Dice loss is actually necessary for imbalanced segmentation, or whether…
- **CanonicalID:** W5-184  ·  **Cluster:** P18 — Boundary error science & loss metrology
- **SourceIDs:** IDEA-C-0290
- **One-liner:** Test whether Dice loss is actually necessary for imbalanced segmentation, or whether tuned weighted cross-entropy matches it.
- **Problem:** "Use Dice loss for imbalance" is near-universal advice, potentially established against under-tuned CE baselines and perpetuated by citation.
- **Hypothesis:** With properly tuned class weights and learning-rate schedules, weighted CE matches Dice-family losses on region metrics across imbalance levels, while showing different (sometimes better) boundary and calibration behavior — the belief reflects tuning asymmetry, not loss superiority.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The Dice-vs-properly-tuned-weighted-CE adjudication targets the field's most-repeated loss advice with a tuning-equalized, pre-registered design; CE's superior probabilistic properties raise the stakes.

### W5-185 — Test whether early stopping on validation Dice silently sacrifices boundary quality that…
- **CanonicalID:** W5-185  ·  **Cluster:** P18 — Boundary error science & loss metrology
- **SourceIDs:** IDEA-C-0311
- **One-liner:** Test whether early stopping on validation Dice silently sacrifices boundary quality that continues improving after Dice plateaus.
- **Problem:** Standard practice stops training when val-Dice plateaus; if metric families converge at different speeds (cf. 0207), the convention systematically truncates boundary learning.
- **Hypothesis:** Boundary metrics continue improving significantly after val-Dice plateau in a substantial fraction of training runs, so Dice-based stopping leaves consistent boundary performance unbanked — and multi-metric stopping criteria capture it at negligible cost.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** PROTECTED (cheap-to-falsify). Early stopping on validation Dice truncating still-improving boundary learning is a universal-convention audit costing almost nothing, with an immediate multi-metric stopping-rule remedy.

## P19 — Multi-rater disagreement & ambiguity science (5)

### W5-186 — Validate inter-rater disagreement maps as a free error oracle: where raters disagree…
- **CanonicalID:** W5-186  ·  **Cluster:** P19 — Multi-rater disagreement & ambiguity science
- **SourceIDs:** IDEA-C-0233
- **One-liner:** Validate inter-rater disagreement maps as a free error oracle: where raters disagree predicts where models fail.
- **Problem:** Model error prediction (quality control) is built from model internals; the annotation process itself may already contain the best error predictor, unused.
- **Hypothesis:** Spatial rater-disagreement maps predict held-out model error maps with accuracy exceeding model-confidence-based error predictors, across architectures — implying model errors are dominated by intrinsic case ambiguity rather than model idiosyncrasy.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Rater-disagreement maps as a model-free error oracle, benchmarked head-to-head against confidence-based error predictors — reframes quality control around case ambiguity rather than model internals.

### W5-187 — Quantify consensus harm: training on majority-vote/STAPLE labels destroys clinically…
- **CanonicalID:** W5-187  ·  **Cluster:** P19 — Multi-rater disagreement & ambiguity science
- **SourceIDs:** IDEA-C-0234
- **One-liner:** Quantify consensus harm: training on majority-vote/STAPLE labels destroys clinically relevant ambiguity information relative to training on raw rater sets.
- **Problem:** Consensus fusion is the default preprocessing for multi-rater data, presumed harmless noise reduction; it may erase exactly the distributional signal risk-aware applications need.
- **Hypothesis:** Models trained on raw multi-rater labels (as distributions) match consensus-trained models on consensus metrics while being substantially better calibrated to the rater distribution on ambiguous regions — the consensus step is where ambiguity information dies, measurably.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** PROTECTED (counter-intuitive). Consensus fusion as the point where ambiguity information dies indicts the default preprocessing of nearly all multi-rater medical data, with a direct twin-training test.

### W5-188 — Decompose rater disagreement into systematic style offsets versus genuine ambiguity using…
- **CanonicalID:** W5-188  ·  **Cluster:** P19 — Multi-rater disagreement & ambiguity science
- **SourceIDs:** IDEA-C-0235
- **One-liner:** Decompose rater disagreement into systematic style offsets versus genuine ambiguity using mixed-effects modeling — recovering hidden agreement.
- **Problem:** All disagreement is treated as ambiguity; but raters may agree on the structure while differing by consistent personal offsets (tight vs generous delineation), a separable component.
- **Hypothesis:** A mixed-effects model (rater-specific boundary offset fields + shared ambiguity term) explains a majority of inter-rater variance on typical datasets, and style-corrected labels show substantially higher effective agreement — most "ambiguity" is removable style.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The style-offset vs genuine-ambiguity mixed-effects decomposition could reveal that most "ambiguity" is removable style — changing variance budgets, performance ceilings, and fusion practice everywhere.

### W5-189 — Stress-test losses under multimodal ground truth: standard objectives assume unimodal…
- **CanonicalID:** W5-189  ·  **Cluster:** P19 — Multi-rater disagreement & ambiguity science
- **SourceIDs:** IDEA-C-0249
- **One-liner:** Stress-test losses under multimodal ground truth: standard objectives assume unimodal truth and fail predictably when raters split between discrete hypotheses.
- **Problem:** When ambiguity is discrete (vessel branches left or right; lesion is one structure or two), the rater distribution is multimodal — and pixel-wise losses trained on it converge to averages that match no rater.
- **Hypothesis:** On constructed and natural multimodal-truth cases, models trained with standard losses produce anatomically invalid averaged solutions at high rates, while distribution-aware training preserves modes — with the invalid-average rate predictable from the modes' spatial separation.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR
- **Why kept:** PROTECTED (high-risk/high-reward). Standard losses producing anatomically invalid "averaged" solutions under multimodal rater truth is a dangerous, characterizable pathology — silent absurdities like blended vessel branches deserve a predictive account.

### W5-190 — Show that self-training converges toward a single annotator style, collapsing the…
- **CanonicalID:** W5-190  ·  **Cluster:** P19 — Multi-rater disagreement & ambiguity science
- **SourceIDs:** IDEA-C-0124
- **One-liner:** Show that self-training converges toward a single annotator style, collapsing the inter-rater variance present in the initial labels.
- **Problem:** Pseudo-labels are generated by a model trained on multi-rater-influenced data; iterating may systematically homogenize label style, losing calibrated ambiguity.
- **Hypothesis:** Across self-training rounds, the distributional spread of predictions on ambiguous regions (where raters disagree) shrinks monotonically toward one mode, and the final model's rater-likelihood is high for one rater and low for others — measurable style collapse absent in the supervised baseline.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR
- **Why kept:** PROTECTED (high-risk/high-reward). Self-training as an ambiguity destroyer connects semi-supervised practice to the multi-rater agenda (C9); medically, the discarded distributional signal is exactly what risk-aware deployment needs.

## P20 — Prompt-learning pathologies (5)

### W5-191 — Show that learned soft prompts are dataset fingerprints: the training dataset is…
- **CanonicalID:** W5-191  ·  **Cluster:** P20 — Prompt-learning pathologies
- **SourceIDs:** IDEA-C-0091
- **One-liner:** Show that learned soft prompts are dataset fingerprints: the training dataset is identifiable from the prompt vector alone.
- **Problem:** CoOp-style prompts are interpreted as "task semantics", but they may primarily encode dataset-specific statistics (style, class priors, acquisition quirks).
- **Hypothesis:** A classifier over learned prompt vectors identifies the source dataset with high accuracy even across matched-task datasets (same classes, different collection), and the fingerprint strength anti-correlates with the prompt's cross-dataset transfer.
- **Novelty:** UNVERIFIED
- **Protect:** HRHR
- **Why kept:** PROTECTED (high-risk/high-reward). Prompts as dataset fingerprints reframes prompt reuse as a safety/leakage issue and prompt vectors as auditable artifacts — a genuinely new lens on a ubiquitous method.

### W5-192 — Test whether the celebrated base-new class trade-off in prompt learning is a…
- **CanonicalID:** W5-192  ·  **Cluster:** P20 — Prompt-learning pathologies
- **SourceIDs:** IDEA-C-0095
- **One-liner:** Test whether the celebrated base-new class trade-off in prompt learning is a regularization artifact rather than a generalization property.
- **Problem:** Base-class gains vs new-class drops are theorized as overfitting-to-seen-classes; but simple regularization knobs (early stopping, weight decay to zero-shot) may trace the same trade-off curve.
- **Hypothesis:** The base-new frontier of specialized methods is matched by vanilla CoOp with a single regularization strength swept — implying published "solutions" move along, not above, an easily accessible curve.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The one-knob frontier-equivalence test could deflate an entire branch of base-new prompt methods; decisive in either direction and cheap relative to its consequence.

### W5-193 — Test whether test-time prompt tuning is functionally equivalent to entropy minimization…
- **CanonicalID:** W5-193  ·  **Cluster:** P20 — Prompt-learning pathologies
- **SourceIDs:** IDEA-C-0101
- **One-liner:** Test whether test-time prompt tuning is functionally equivalent to entropy minimization plus temperature calibration.
- **Problem:** TPT-style methods report zero-shot gains, but their objective (confidence maximization over augmentations) may reduce to well-known calibration adjustments.
- **Hypothesis:** A closed-form per-sample temperature/prior adjustment fitted to the same augmentation ensemble reproduces the bulk of TPT's gains at a fraction of compute; TPT's residual advantage concentrates on samples where it changes the argmax, which are disproportionately errors.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Reduces test-time prompt tuning to closed-form calibration if the hypothesis holds; the argmax-changing residual analysis doubles as a harm probe for an expensive deployed technique.

### W5-194 — Document "prompt collapse": class prompts converging toward each other during long…
- **CanonicalID:** W5-194  ·  **Cluster:** P20 — Prompt-learning pathologies
- **SourceIDs:** IDEA-C-0113
- **One-liner:** Document "prompt collapse": class prompts converging toward each other during long training, silently destroying fine-grained discrimination.
- **Problem:** Prompt training monitors accuracy, not the geometry of the prompt set; converging prompts would degrade exactly the confusable classes while aggregate metrics look stable.
- **Hypothesis:** Pairwise similarity among class-prompt embeddings increases with training beyond a task-dependent point, and its rise predicts (precedes) the decline of confusable-pair accuracy — establishing collapse as a monitorable pathology with an early-warning signal.
- **Novelty:** UNVERIFIED
- **Protect:** CI
- **Why kept:** PROTECTED (counter-intuitive). Prompt collapse as a monitorable training pathology with a lead-lag early-warning signal; nobody currently tracks prompt-set geometry during training.

### W5-195 — Replace learned prompts with random-but-frozen vectors of matched norm: if accuracy…
- **CanonicalID:** W5-195  ·  **Cluster:** P20 — Prompt-learning pathologies
- **SourceIDs:** IDEA-C-0316
- **One-liner:** Replace learned prompts with random-but-frozen vectors of matched norm: if accuracy holds, prompt "learning" is mostly capacity, not semantics.
- **Problem:** Prompt-tuning papers imply prompts encode task semantics; the null hypothesis — any extra trainable-then-frozen directions plus the head recalibration suffice — is never run.
- **Hypothesis:** Freezing prompts at random initialization while training only the same lightweight components the method trains recovers a large fraction of reported gains on standard benchmarks — bounding the semantic content of learned prompts from above.
- **Novelty:** UNVERIFIED
- **Protect:** CF
- **Why kept:** PROTECTED (cheap-to-falsify). Random-frozen prompts of matched norm upper-bound the semantic content of prompt learning — the conspicuously missing null control for an entire method family.

## P21 — Label-efficient learning validity (5)

### W5-196 — Test whether consistency regularization works via implicit boundary smoothing rather than…
- **CanonicalID:** W5-196  ·  **Cluster:** P21 — Label-efficient learning validity
- **SourceIDs:** IDEA-C-0121
- **One-liner:** Test whether consistency regularization works via implicit boundary smoothing rather than the cluster assumption it cites.
- **Problem:** The mechanism of consistency training in segmentation is asserted (decision boundaries in low-density regions) but never separated from a mundane alternative: averaging over perturbations smooths predicted boundaries.
- **Hypothesis:** Replacing consistency training with explicit boundary-smoothing regularization (no unlabeled data) reproduces a large fraction of its gains on standard benchmarks; the residual unlabeled-data benefit concentrates on images whose appearance is far from labeled examples — separating smoothing from information gain.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The smoothing-equivalence control for consistency regularization is a first-order mechanism question for all of semi-supervised segmentation — the control experiment is conspicuously absent from the literature.

### W5-197 — Show that the "low-data regime" simulated by subsampling big datasets misrepresents true… [E]
- **CanonicalID:** W5-197  ·  **Cluster:** P21 — Label-efficient learning validity
- **SourceIDs:** IDEA-C-0127
- **One-liner:** Show that the "low-data regime" simulated by subsampling big datasets misrepresents true small-cohort learning, breaking method rankings.
- **Problem:** Papers simulate scarcity as 5% of a large dataset — preserving class coverage and appearance diversity that genuine small cohorts lack.
- **Hypothesis:** Method rankings established on subsampled-scarcity benchmarks reorder significantly on true small cohorts (single-site, consecutive patients), because subsampling preserves diversity that specific methods exploit — measurable as a ranking-correlation breakdown.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The subsampled-scarcity vs genuine-small-cohort audit touches every low-data claim in medical segmentation; if rankings reorder, the field has been optimizing for the wrong users.

### W5-198 — Quantify the positional shortcut in pixel-level contrastive SSL on spatially registered…
- **CanonicalID:** W5-198  ·  **Cluster:** P21 — Label-efficient learning validity
- **SourceIDs:** IDEA-C-0132
- **One-liner:** Quantify the positional shortcut in pixel-level contrastive SSL on spatially registered medical images.
- **Problem:** Medical volumes are roughly aligned; pixel contrastive objectives can minimize loss by encoding position rather than appearance semantics.
- **Hypothesis:** Features from pixel-contrastive SSL on registered data predict spatial coordinates far better than appearance-matched controls, and their downstream transfer drops disproportionately on unregistered/abnormal cases — with registration-breaking augmentation closing both gaps.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The positional shortcut in pixel-contrastive SSL on registered medical images is a plausible silent failure of the standard recipe, and the graded registration-breaking design gives it a proper dose-response test.

### W5-199 — Show that "barely-supervised" (one labeled volume) segmentation success is carried by…
- **CanonicalID:** W5-199  ·  **Cluster:** P21 — Label-efficient learning validity
- **SourceIDs:** IDEA-C-0137
- **One-liner:** Show that "barely-supervised" (one labeled volume) segmentation success is carried by implicit registration, and collapses on unregistered anatomy.
- **Problem:** Single-volume supervision methods report strong results on well-aligned datasets (cardiac, abdominal atlases); the role of implicit spatial alignment is unacknowledged.
- **Hypothesis:** Performance of barely-supervised methods degrades toward failure as test-time anatomical alignment with the labeled volume decreases (measured by registration residual), while many-label baselines degrade far less — alignment, not method ingenuity, is the active ingredient.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** Alignment-stratified evaluation of barely-supervised segmentation directly tests whether implicit registration, not method ingenuity, is the active ingredient — a sharp, checkable deflation.

### W5-200 — Test whether label-efficient methods change the slope or only the intercept of the…
- **CanonicalID:** W5-200  ·  **Cluster:** P21 — Label-efficient learning validity
- **SourceIDs:** IDEA-C-0143
- **One-liner:** Test whether label-efficient methods change the slope or only the intercept of the labeled-data learning curve.
- **Problem:** Methods claim to "reduce annotation needs by N×", implying slope changes, but most evaluations report isolated points, not curves.
- **Hypothesis:** Fitting power-law learning curves across label fractions shows that semi/weak/self-supervised methods shift the intercept (constant multiplier) but leave the exponent statistically unchanged — implying their advantage shrinks at scale and "N× savings" claims are point-estimate artifacts.
- **Novelty:** UNVERIFIED
- **Protect:** M
- **Why kept:** The slope-vs-intercept learning-curve analysis converts "N× annotation savings" marketing into a testable scaling claim — one of the batch's best methodological ideas with consequences for funding-level decisions.

---

*End of pool: 200 unique ideas across 21 clusters. Authoritative full texts remain in the batch survivor files and `stage2_audit.md` §5; merge rationales in `stage2_AB_duplicates.md` and `stage2_pool200_index.md`.*
