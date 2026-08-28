# Stage 5 — Cluster B Experimental Engineering (7 Stage-4 survivors)

**Experimental Engineer (Cloud Sub-Agent N) → Supervisor Windows7.**
Designed as if work starts next week: every design names real datasets, real public codebases
(verified by search this session or inherited from Stage-3/4 session searches — marked), concrete
GPU budgets in A100-days, a minimal viable experiment (MVE) with a go/no-go gate, and one
pre-registered Killer Experiment whose failure kills the idea.

Inputs: `stage4_cluster_B_keep.md` / `stage4_cluster_B_attacks.md` (branch
`cursor/stage4-cluster-b-reviewer2-b25a`), `stage3_cluster_B_*` (branch
`cursor/stage3-cluster-b-priorwork-5dcc`), `stage1_cluster_B_ideas.md` (branch
`cursor/stage1-cluster-b-ideas-6596`). Cross-checked against `stage4_cluster_A_keep.md` and
`stage4_cluster_C_keep.md` for killer-experiment collisions (§ Cross-cluster dedup, end of file).

**All numeric outcomes under "Expected results" are HYPOTHESIZED — predictions to be tested, not
measured facts. No paper or result is cited that was not found in this session's searches or
inherited from the Stage-1/3/4 documents (marked "inherited").**

Provenance convention: [verified this session] = found by this Stage-5 engineer's web searches;
[inherited] = carried from Stage-3/4 session documents.

---

## E1. B-0121 (PROTECTED) — Wrong-support counterfactual audit of few-shot segmentation

### RQ
What fraction of reported few-shot segmentation (FSS) accuracy is support-independent — i.e.
recoverable with a deliberately wrong-class support — measured per method, per benchmark, and per
query-complexity stratum; and does ranking methods by support sensitivity reorder the published
leaderboard?

### Hypothesis
A substantial share of FSS accuracy on standard benchmarks is produced by a class-blind
foreground/saliency prior, not by use of the support; the share differs systematically between
specialist meta-learners (PFENet/HSNet/BAM era) and foundation-model matchers (Matcher, PerSAM,
SegGPT, FSSAM), and is largest on single-salient-object queries.

### Falsifiable prediction (pre-registered)
On distractor-present, multi-object query strata of COCO-20i / LVIS-92i, at least half of the
audited specialist methods retain > 50% of their correct-support IoU when fed a wrong-class
support. Falsified if all audited methods retain < 20% IoU on those strata (models collapse
appropriately → field certified; publishable negative).

### Method
1. For each method f and episode (S, Q): predict with the correct support, then with K=5
   wrong-class supports (classes verified absent from Q, support-mask area matched within ±50% to
   the correct support). Score: (a) **retention** = IoU_wrong/IoU_correct against GT; (b)
   **insensitivity** = IoU(M_wrong, M_correct) between the two predictions; (c) episode-level
   flip rate (insensitivity > 0.9).
2. Stratify every number by query complexity: single- vs multi-object query, distractor of a
   different class present/absent (computable from benchmark instance annotations). This
   separates benchmark degeneracy from model insensitivity — the Stage-4 defense.
3. Support-free floor: score a support-free objectness baseline (SAM automatic mask generation,
   largest/most-central mask; plus a classical salient-object detector) on identical episodes.
   A method whose correct-support accuracy ≈ its wrong-support accuracy ≈ the support-free floor
   has its "few-shot learning" fully accounted for by the prior.
4. Sensitivity-adjusted leaderboard: rerank methods by (IoU_correct − IoU_wrong) and by
   IoU_correct on the distractor-present stratum only; release the stratum definition as a fixed
   distractor-enriched evaluation split.

### Data
- PASCAL-5i (VOC2012+SBD) and COCO-20i (COCO 2014) — standard FSS splits, public.
- LVIS-92i episodes (used by Matcher [verified this session]) for higher multi-object density.
- FSS-1000 as the near-degenerate control benchmark (single centered object by construction).

### Baselines
- Support-free objectness floor (SAM AMG largest-mask; salient-object detector).
- Random-support (correct class, different instance) as the upper anchor for benign support
  variation.
- Published correct-support numbers of each checkpoint (reproduced, not copied).

### Metrics
Retention, insensitivity, flip rate (all stratified); support-sensitivity score
SSS = 1 − retention; Kendall τ between original and sensitivity-adjusted leaderboards;
bootstrap CIs over episodes; per-fold seeds for episode sampling (3 seeds).

### Real reusable codebases (all with public checkpoints)
- PFENet — github.com/dvlab-research/PFENet (8 pretrained models, PASCAL-5i + COCO-20i)
  [verified this session].
- HSNet — github.com/juhongm999/hsnet (Google Drive checkpoints) [verified this session].
- BAM — github.com/chunbolang/BAM (OneDrive checkpoints, VGG16/ResNet50, both benchmarks; CVPR
  2022 Oral, the Lang et al. base-class-bias paper itself) [verified this session].
- Matcher — github.com/aim-uofa/Matcher (ICLR 2024; training-free DINOv2+SAM) [verified this
  session].
- PerSAM — github.com/ZrrSkywalker/Personalize-SAM (training-free + 2-param variant) [verified
  this session].
- FSSAM — github.com/Sam1224/FSSAM (ICML 2025; SAM2-based, uses official SAM2 checkpoints)
  [verified this session].
- SegGPT — available in HuggingFace Transformers (`SegGptForImageSegmentation`) [verified this
  session].
- SAM / SAM2 official checkpoints (facebookresearch) for the support-free floor [verified this
  session via FSSAM/Matcher dependencies].

### GPU/time budget
Inference-only. ~8–10 methods × 2 benchmarks × 4 folds × 1,000 episodes × 6 support conditions
(1 correct + 5 wrong) ≈ 500k forward passes; at 0.3–3 s each → **≤ 5 A100-days** total including
strata, floors, and 3 episode-sampling seeds. Zero training. Engineering: one adapter per repo to
inject controlled supports (~7 small wrappers).

### MVE (go/no-go)
PFENet + BAM + Matcher on PASCAL-5i fold 0 and COCO-20i fold 0 (1,000 episodes each), correct vs
wrong supports, single stratification pass. **~1 A100-day.**
Go if any method retains > 35% IoU under wrong supports on any stratum, or if specialist-vs-
foundation retention differs by > 15 points. No-go (idea dies cheaply) if all retentions < 20%
everywhere including PASCAL single-object strata.

### Experiment ladder
- **Full:** all methods × both benchmarks × all folds × all strata × 3 seeds; sensitivity-adjusted
  leaderboard; distractor-enriched split release.
- **Ablations:** wrong-support similarity (near-class vs far-class wrong supports, e.g. cat→dog vs
  cat→airplane); support-mask area matching on/off; K = 1 vs 5 wrong draws; 1-shot vs 5-shot
  (all-wrong and mixed 4-correct+1-wrong supports — dose-response in the support set).
- **Controls:** random correct-class support (benign variation anchor); support-free floor;
  blank-support input (degenerate control, methods permitting).
- **Robustness:** repeat retention on FSS-1000 (degenerate benchmark — retention here measures
  benchmark, not model); verify conclusions are unchanged when scoring with the official
  per-repo evaluation code vs one shared evaluator.
- **Generalization:** medical transfer probe — one-shot organ episodes assembled from a public
  abdominal CT dataset (e.g. MSD/AMOS slices) run through the training-free methods (Matcher,
  PerSAM, SegGPT) only; tests whether the saliency-prior finding transfers out of natural images.

### Expected results (HYPOTHESIZED)
Specialist meta-learners retain 40–70% IoU under wrong supports on PASCAL-5i single-object
strata and 20–40% on COCO distractor strata; training-free foundation matchers retain less
(10–30%) because matching is explicitly support-driven; the sensitivity-adjusted leaderboard
reorders ≥ 3 of 8 positions; FSS-1000 retention is high for everything (benchmark degeneracy
indicted separately from models).

### Negative interpretation
If every method collapses appropriately (< 20% retention everywhere): the field's validity is
certified; publish the certification + the stratified protocol as a short evaluation paper —
informative negative that only this audit provides. If retention is high only where benchmarks
are degenerate: the indictment moves from models to benchmarks; the distractor-enriched split
becomes the main deliverable.

### Stop criteria
- Stop after MVE if no-go gate fires AND the COCO distractor stratum also shows < 20% retention.
- Stop before any method development: this is an audit; the fixed split is the only artifact.
- Hard cap: 8 A100-days and the audit ships with whatever methods ran.

### Killer Experiment
**The stratified wrong-support counterfactual with support-free floor:** on the pre-registered
distractor-present stratum, (a) ≥ half of specialist methods retain > 50% IoU with wrong-class
supports, and (b) their correct-support accuracy on that stratum is statistically
indistinguishable (bootstrap CI overlap) from the support-free objectness floor. If (a) and (b)
both fail — methods collapse under wrong supports and beat the floor — the headline claim is dead
and the certification result is published instead. Cost of the killer alone: ~2 A100-days.

### ROI: **9/10.** Days of compute, zero training, headline number, informative in every branch,
and no published counterfactual audit exists (Stage-4 search: only mitigation methods — TBS AAAI
2024, AENet ECCV 2024 [inherited]).

---

## E2. B-0212 — Blending-artifact detectability → synthetic-to-real transfer-gap law

### RQ
At fixed generator and fixed image content, does the detectability of compositing artifacts (probe
classifier AUROC on composite-vs-real patches) predict the synthetic-to-real transfer gap of
lesion segmenters trained on the composites — and do trained models causally use the artifact
shortcut?

### Hypothesis
The compositing boundary is an exploitable shortcut: models trained on detectably composited
lesions key on the seam, inflating synthetic-set accuracy and depressing real-set accuracy in
proportion to probe-measured artifact detectability; suppressing or injecting the artifact at
fixed content moves the gap causally.

### Falsifiable prediction (pre-registered)
Across a ≥ 5-rung compositing ladder at fixed content, Spearman ρ between probe AUROC and
real-set DSC is ≤ −0.8 (higher detectability → worse real performance); and re-injecting
artifacts into the best-blended arm reopens ≥ 50% of the ladder's real-DSC spread. Falsified if
|ρ| < 0.5 or injection moves real DSC by < 2 DSC points.

### Method
1. **Fixed-content compositing ladder.** Lesion source fixed: procedural tumor synthesis from
   SyntheticTumors (shape+texture generation, CVPR 2023) [verified this session] — same lesions,
   same target healthy CTs, same locations across arms. Arms vary only the compositing step:
   (i) hard cut-paste; (ii) Gaussian-feathered paste; (iii) Poisson blending; (iv) learned
   harmonization (PCTNet); (v) probe-adversarial anti-artifact blending (fine-tune the
   compositor against the frozen probe). Arms (i)–(iv) run through libcom's `get_composite_image`
   (`none`/`gaussian`/`poisson`) and `ImageHarmonizationModel` (PCTNet) [verified this session].
2. **Probe.** Patch classifier (ResNet-50, boundary-centered patches, composite vs real lesion
   boundary patches from the real-lesion training split) per arm → AUROC_a. Also report libcom's
   `HarmonyScoreModel` (BargainNet) and `InharmoniousLocalizationModel` (MadisNet) scores as
   off-the-shelf detectability proxies [verified this session].
3. **Downstream.** Train an identical segmenter per arm on synthetic-only data (DiffTumor STEP3
   MONAI U-Net recipe, 96³ patches [verified this session]); evaluate on real lesions (LiTS/MSD
   Task03 held-out). Gap_a = synthetic-val DSC − real-test DSC.
4. **Causal arms.** (a) Injection: add the measured seam residual (high-frequency boundary
   signature extracted as the mean difference between arm-(i) and arm-(iv) boundary patches) into
   arm-(iv) composites; prediction: real DSC drops toward arm-(i). (b) Usage attribution at
   inference: paste the seam signature along GT lesion boundaries vs random background curves in
   *real* test images; a shortcut-using model's predictions should follow injected seams.
5. **Law + audit deliverable:** AUROC-vs-gap curve at fixed content; probe-AUROC reported as a
   hygiene number for existing public synthesis pipelines (SyntheticTumors, DiffTumor).

### Data
- MSD Task03 Liver (public; mirrored via DiffTumor's HuggingFace assets [verified this session]);
  LiTS real tumors for real-set evaluation; DiffTumor HealthyCT collection for healthy target
  scans [verified this session].
- Second organ for generalization: kidney (KiTS23) or pancreas (MSD Task07) using DiffTumor's
  released per-organ assets [verified this session].

### Baselines
- Real-lesion-trained segmenter (upper anchor); DiffTumor released segmentation checkpoints
  (U-Net/nnU-Net/SwinUNETR trained on synthetic tumors, HuggingFace) [verified this session] as
  external reference points; generative in-fill arm (DiffTumor diffusion checkpoints) appended to
  the ladder as a sixth, generator-confounded rung reported separately (kept out of the
  fixed-content law).

### Metrics
Probe AUROC per arm; synthetic-val DSC, real-test DSC + NSD; gap; Spearman ρ across arms
(3 seeds → 15+ points); injection effect size (ΔDSC); seam-following rate in the attribution
test; per-lesion-size stratification.

### Real reusable codebases
- github.com/MrGiovanni/SyntheticTumors (CVPR 2023, procedural lesion synthesis) [verified].
- github.com/MrGiovanni/DiffTumor (CVPR 2024; STEP3 segmentation training pipeline; HF
  checkpoints for autoencoder/diffusion/segmenters) [verified].
- github.com/bcmi/libcom (compositing: none/gaussian/poisson; PCTNet harmonization; BargainNet
  harmony score; MadisNet inharmonious localization) [verified].
- MONAI + nnU-Net for training/eval [verified]; timm/torchvision for probes.

### GPU/time budget
Probes: < 1 A100-day total. Segmenters: 5 arms × 3 seeds × 2 organs ≈ 30 runs at 1–1.5
A100-days each (DiffTumor U-Net recipe, shortened to a pre-registered 1,000-epoch schedule after
MVE calibration) → **~40–45 A100-days full program**; causal arms +4; attribution inference
negligible.

### MVE (go/no-go)
Liver only, arms (i)/(iii)/(iv), 1 seed, probe per arm. **~6 A100-days.**
Go if probe AUROC ordering matches real-DSC ordering (3 points, monotone) and the arm-(i)-vs-(iv)
real-DSC spread ≥ 3 DSC points. No-go if real DSC is flat (< 1.5 points spread) across
compositing at fixed content — the folklore is wrong, publish the null cheaply.
Pre-MVE sanity gate (< 0.5 A100-day): probe on arm (i) must reach AUROC > 0.9, else the pipeline
is buggy or the artifact premise fails; debug before spending.

### Experiment ladder
- **Full:** 5-rung ladder × 2 organs × 3 seeds; law curve; injection + attribution causal arms;
  hygiene-number audit of public pipelines.
- **Ablations:** probe architecture (ResNet-50 vs ConvNeXt-T vs frequency-domain probe); patch
  size; boundary-only vs whole-lesion patches; segmenter backbone (U-Net vs SwinUNETR).
- **Controls:** fixed-content requirement enforced by construction (same lesions/locations across
  arms); real-trained segmenter anchor; a "content-varied" ladder replicated once to show the
  confound the fixed-content design removes (the Stage-4 attack, demonstrated then dismissed).
- **Robustness:** repeat law with NSD instead of DSC; lesion-size strata; probe trained on one
  arm evaluated on others (transferable artifact signature).
- **Generalization:** second organ; sixth generative-in-fill rung (reported as
  generator-confounded, outside the law); one 2D natural-image replicate (COCO-object cut-paste
  with libcom, small scale) to test domain-independence of the law's direction.

### Expected results (HYPOTHESIZED)
Probe AUROC spans ~0.98 (cut-paste) → ~0.65 (harmonized/adversarial); real DSC spans 10–25 DSC
points across the ladder at fixed content; ρ ≈ −0.9; injection reopens ≥ 60% of the spread;
attribution shows seam-following in high-AUROC arms only.

### Negative interpretation
If real DSC is insensitive to compositing at fixed content: blending folklore is quantified as
overrated — content, not compositing, drives the gap; publish as a corrective measurement (the
2017 Cut-Paste-and-Learn blending claim [inherited] fails to transfer to medical volumes). If
detectability varies but the gap doesn't: detectable ≠ used, an equally citable boundary on
shortcut-learning claims (arXiv 2403.06748 [inherited] documents other medical shortcuts).

### Stop criteria
- Stop at sanity gate if cut-paste artifacts are unprobeable (AUROC < 0.6).
- Stop after MVE on no-go; publish null with the 3-arm evidence.
- Stop the ladder (skip arm v) if arms (i)–(iv) already span < 3 DSC points.
- Hard cap 55 A100-days.

### Killer Experiment
**Fixed-content ladder + reverse injection:** the ρ ≤ −0.8 law across ≥ 5 arms AND artifact
injection into best-blended composites reopening ≥ 50% of the spread. Both must hold; either
failing kills the "law" (the correlation attack and the detectable-≠-used attack from Stage 4 are
exactly these two legs). Cost of the killer alone: ~15 A100-days (subset: 5 arms × 1 organ ×
2 seeds + injection).

### ROI: **8/10.** Moderate cost, fully public data/code, causal design that answers both Stage-4
attacks, and a hygiene number (pipeline probe-AUROC) the synthesis community can adopt
immediately.

---

## E3. M5 (from B-0362) — Decision-flip-rate audit of published SOTA deltas

### RQ
What fraction of published segmentation SOTA deltas, when recomputed case-by-case under
pre-registered decision rules drawn verbatim from clinical/operational guidelines, produce (a)
near-zero decision change (decision-invisible progress) or (b) a reversed winner under at least
one legitimate rule family?

### Hypothesis
Metric deltas of the size that earns SOTA claims (~1–3 DSC points) frequently do not survive
translation through real decision rules: many published gains are decision-invisible, and a
non-trivial fraction reverse under at least one guideline-derived rule, because case-level
decision disagreement concentrates in cases the mean metric down-weights.

### Falsifiable prediction (pre-registered)
Among auditable published pairs with |ΔDSC| ≤ 3 points, ≥ 30% are decision-null (bootstrap CI of
the decision-accuracy delta crosses zero under every rule family) or winner-reversing under ≥ 1
rule family. Falsified if < 10% flip anywhere on the rule surface — metric progress is certified
decision-faithful (informative negative).

### Method
1. **Pre-registration first.** Decision-rule families frozen before any flip is computed, drawn
   verbatim from guidelines: (a) RECIST 1.1 response categories computed from predicted masks
   (longest axial diameter; ±20%/+5mm category boundaries — Eisenhauer et al. 2009, the standard
   guideline); (b) dose-volume constraint satisfaction on radiotherapy structures (OpenKBP
   evaluation stack [inherited, Stage-3]); (c) detection/alarm rules at fixed operating points
   (lesion-count and minimum-size triggers as used in screening challenge protocols, e.g.
   LUNA16-style FROC operating points on LIDC nodules). Each family carries a pre-registered
   ±10% threshold-perturbation grid → the flip-rate **surface**, not one number.
2. **Auditable-pair collection.** Systematic sweep of recent segmentation papers claiming SOTA
   deltas on public 3D benchmarks (BraTS, KiTS, LiTS/MSD, AMOS); a pair is auditable iff both
   models' checkpoints or per-case predictions are public. Anchor set available today: DiffTumor's
   released real-vs-synthetic-trained segmenters (3 organs × 3 backbones, HuggingFace) [verified
   this session]; nnU-Net (MIC-DKFZ/nnUNet) vs MedNeXt (MIC-DKFZ/MedNeXt) [verified this
   session]; TotalSegmentator version pairs (public weights). The **auditable fraction** of the
   swept claims is itself a headline reproducibility finding.
3. **Flip computation.** Per pair × rule × case: decision(model A), decision(model B),
   decision(GT). Report: case-level flip rate; decision-accuracy delta vs GT decisions;
   winner-consistency between the published metric delta and each rule; surface over the
   threshold grid; sensitivity analysis over rule families.
4. **Metric layer.** All mask metrics recomputed with the Metrics Reloaded reference
   implementation (github.com/Project-MONAI/MetricsReloaded; framework inherited from Stage 3 —
   Maier-Hein et al., Nature Methods 2024) so metric-computation variance is not confounded with
   decision variance.

### Data
Public test/val splits with GT: MSD Task03/Task07, KiTS23, BraTS 2021, AMOS22, LIDC (via pylidc
[verified this session]); OpenKBP data for the dose-constraint family [inherited].

### Baselines
- Null model pair (same model, two seeds / two folds): the flip-rate floor from training noise —
  every published-pair flip rate is reported as excess over this floor (crucial control).
- Metric-delta-matched synthetic pairs (perturb one model's masks to produce a controlled ΔDSC):
  calibration curve linking ΔDSC to expected flip rate under each rule.

### Metrics
Case-level flip rate (excess over null floor); decision-accuracy delta + bootstrap CI;
fraction decision-null; fraction winner-reversing; auditable fraction; flip-rate surface over
threshold grid; agreement (κ) between model-derived and GT-derived RECIST categories (comparable
to the κ 0.67–0.81 automated-vs-manual RECIST range found in Stage-4's searches [inherited]).

### Real reusable codebases
- github.com/MIC-DKFZ/nnUNet; github.com/MIC-DKFZ/MedNeXt (nnU-Net-v1-based trainers, public)
  [verified this session].
- MONAI nnU-Net bundle conversion utilities (`monai.apps.nnunet`) for uniform checkpoint handling
  [verified this session].
- DiffTumor HuggingFace segmentation checkpoints (9 models) [verified this session].
- TotalSegmentator public weights (wasserth/TotalSegmentator).
- github.com/Project-MONAI/MetricsReloaded for metric recomputation.
- pylidc + FLamby fed_lidc_idri loaders for LIDC masks [verified this session].
- OpenKBP evaluation code (ababier/open-kbp) [inherited, Stage-3].
- RECIST longest-diameter extraction: ~200 lines on top of scikit-image (no external dependency
  needed; protocol cross-checked against the automated-RECIST literature found in Stage 4
  [inherited]).

### GPU/time budget
Inference-only: ~20 model-pair × benchmark combinations × 100–500 cases of 3D inference →
**~8–10 A100-days**; the dominant cost is engineering (pair collection, per-repo inference
harnesses, rule implementations) — CPU-bound analysis thereafter.

### MVE (go/no-go)
Zero-GPU desk survey first: sweep ~50 recent SOTA-claiming segmentation papers; count auditable
pairs. Go only if ≥ 15 auditable pairs exist (else publish the reproducibility finding alone).
Then: DiffTumor's 9 released pairs + nnU-Net baseline on MSD Task03 under the RECIST family only.
**~2 A100-days.** Go if case-level excess flip rate > 5% for at least 3 pairs.

### Experiment ladder
- **Full:** all auditable pairs × 3 rule families × threshold surface × null-floor control ×
  calibration curve.
- **Ablations:** per-case vs per-lesion decision granularity; 2D-slice vs 3D diameter extraction
  for RECIST; consensus-GT vs single-rater GT where LIDC multi-rater masks allow.
- **Controls:** null pair floor (seeds/folds of the same method); synthetic ΔDSC calibration
  pairs; rule-grid sensitivity (the Stage-4 "cherry-picked rules" attack is answered by the
  pre-registered surface).
- **Robustness:** repeat headline with NSD-ranked pairs; stratify pairs by whether models were
  trained only on the evaluation benchmark's training split vs with external data (contamination
  stratification).
- **Generalization:** one non-medical replicate — deployed-threshold alarm rules on a public
  driving benchmark pair (e.g. two public Cityscapes checkpoints from mmsegmentation with a
  pedestrian-within-corridor alarm rule) to show the audit template is not oncology-specific.

### Expected results (HYPOTHESIZED)
Given automated-vs-manual RECIST category agreement of only κ 0.67–0.81 at DSC ≈ 0.85 and up to
37.5% reader-score shifts under AI assistance (evidence found in Stage-4 session [inherited]):
expect 25–50% of small published deltas decision-null, 10–25% winner-reversing under ≥ 1 family,
auditable fraction 20–40% of swept claims, and null-floor flip rates of 2–5% (making excess flips
interpretable).

### Negative interpretation
If flips ≈ null floor everywhere: published metric progress is decision-faithful at current delta
sizes — a certification the field can cite against metric-nihilism; the calibration curve
(ΔDSC → expected flips) remains a standing deliverable either way. If the auditable fraction is
tiny: the reproducibility finding becomes the paper (published deltas cannot be decision-audited).

### Stop criteria
- Stop after desk survey if < 15 auditable pairs (publish reproducibility note).
- Stop a rule family if GT-derived decisions are degenerate on a benchmark (> 95% one category —
  no discriminative power).
- Hard cap 12 A100-days + pre-registered analysis plan (no post-hoc rule additions).

### Killer Experiment
**The pre-registered flip surface with null-floor control:** compute the flip-rate surface for
all auditable pairs under the frozen rule families; the claim survives only if excess-over-floor
flips ≥ 30% of small-delta pairs somewhere on the pre-registered surface AND the effect is not
explained by the ΔDSC calibration curve (i.e. flips concentrate beyond what the metric delta
predicts). Both legs falsifiable; failure of both = certified decision-faithfulness, published as
the negative. Cost of the killer alone: ~4 A100-days after pair collection.

### ROI: **8/10.** Near-zero GPU cost, evidence-backed non-vacuity (Stage-4 RECIST findings), a
headline number for the whole field; discounted from 9 by the pair-collection engineering burden
and the desk-survey sample risk.

---

## E4. B-0222 — Thin-structure fidelity floor of latent autoencoders + downstream penalty

### RQ
At what structure width (in pixels, as a function of autoencoder downsampling factor) does the
latent-autoencoder round-trip destroy thin structures; and does the measured round-trip floor
predict the width-stratified recall deficit of segmenters trained on latent-generated data versus
matched-compute pixel-space generation?

### Hypothesis
Autoencoder compression imposes a measurable, autoencoder-specific survival-vs-width curve on
thin structures (independent of any generator or conditioning), and this curve — not conditioning
or diffusion failure — is the operative mechanism behind thin-structure blind spots in models
trained on latent-generated data.

### Falsifiable prediction (pre-registered)
For each autoencoder, structure survival drops below 90% at a width w* that scales approximately
linearly with the spatial downsampling factor f (w* within [0.5f, 2f] pixels); and the
width-stratified recall deficit of the latent-arm-trained segmenter tracks the round-trip
survival curve pointwise within ±10% recall. Falsified if survival > 95% at all widths ≥ 2 px for
modern f8 autoencoders (no floor exists), or if the downstream deficit is uncorrelated with the
round-trip curve.

### Method
1. **Arm A — round-trip protocol (no generation, no conditioning; kills the Stage-4 confound
   attack by construction).** Encode-decode real and phantom images through k autoencoders ×
   downsampling factors. Inputs: (a) calibrated phantom battery — anti-aliased curves/lines at
   widths 1–16 px, controlled contrast, curvature, spacing, background texture; (b) real
   width-annotated structures — retinal vessels (DRIVE, CHASE_DB1, FIVES) with per-pixel vessel
   width from the GT distance transform; road cracks (DeepCrack). Measures per width bin:
   structure survival (frozen oracle segmenter trained on originals, applied to decoded images),
   contrast attenuation, centerline displacement.
2. **Autoencoder panel.** Stable Diffusion v1.5 VAE (f8) and SDXL VAE (f8); CompVis
   latent-diffusion first-stage KL-f4 and KL-f8 models [inherited lineage, verified via MedVAE's
   documented CompVis/Stability ancestry this session]; MedVAE 2D X-ray autoencoders at total
   compression 16 (4× spatial) and 64 (8× spatial) with public HuggingFace weights and
   encode/decode CLI [verified this session]; one MONAI AutoencoderKL trained in-domain at f4/f8
   (MONAI generative components) as the trained-from-scratch control.
3. **Arm B — downstream causal test (matched compute).** One domain: retinal fundus at 512².
   Train mask-conditioned latent LDM (on a panel autoencoder) vs pixel-space diffusion at matched
   GPU-hours (MONAI generative recipes); generate equal-size synthetic sets from identical
   held-out vessel masks; train identical segmenters per arm; report vessel recall stratified by
   GT width.
4. **Deliverable:** the protocol + per-autoencoder datasheet (survival curves, w*), and the
   when-to-use-pixel-space decision rule keyed to task-relevant structure width — the
   protocol-not-constant framing that survives autoencoder turnover (Stage-4 defense; the
   engineering fix wave — MedVAE, VAEsselSparse, VesselSDF [inherited] — is the customer, not the
   competitor).

### Data
DRIVE, CHASE_DB1, FIVES (retinal vessels, public); DeepCrack (cracks, public); phantom battery
(generated, released); optionally DIS-5K fine structures as a natural-image spot check.

### Baselines
Identity (no round-trip) upper anchor; classical downsample-upsample (bicubic at factor f)
lower anchor — separates "any resampling at f" from "this learned autoencoder"; real-data-trained
segmenter for Arm B.

### Metrics
Survival-vs-width curves + w* per autoencoder; contrast attenuation ratio; downstream per-width
recall/Dice; pointwise curve-vs-deficit agreement (the killer statistic); matched-compute
accounting (GPU-hours, params, steps) reported side by side.

### Real reusable codebases
- github.com/StanfordMIMI/MedVAE (six 2D/3D VAEs, HF weights, encode/decode CLI) [verified this
  session].
- CompVis/latent-diffusion + Stability AI VAE checkpoints (sd-vae-ft-mse et al., HF) [verified
  lineage this session].
- MONAI generative components (AutoencoderKL, LDM training recipes; Project-MONAI) [verified
  MONAI tooling this session].
- nnU-Net / MONAI segmentation for oracle + downstream segmenters [verified this session].
- scikit-image distance transforms for width maps (standard).

### GPU/time budget
Arm A: **< 2 A100-days** (pure inference + one oracle segmenter per dataset) — plus ~3 A100-days
if the in-domain MONAI AutoencoderKL pair is trained rather than reused. Arm B: 2 diffusion
trainings at a pre-registered matched budget (cap 12 A100-days each) + sampling + 2×3-seed
segmenter trainings (~4) → **~35 A100-days full program**.

### MVE (go/no-go)
Phantom battery + DRIVE through SD-1.5 VAE, SDXL VAE, MedVAE-4×, MedVAE-8× (all public weights,
no training; oracle segmenter = published DRIVE U-Net recipe retrained once).
**~1 A100-day.** Go if any modern autoencoder shows survival < 90% for widths ≥ 2 px with the
bicubic control surviving (learned compression is the cause). No-go: no floor in task-relevant
widths → the community belief is corrected; publish the short datasheet note, skip Arm B.

### Experiment ladder
- **Full:** k ≥ 6 autoencoders × 2 factors × phantom+2 real datasets; Arm B matched-compute
  causal test; datasheet release.
- **Ablations:** phantom contrast/curvature/spacing; decoder-only vs full round-trip (encode-
  decode vs decode-from-projected-latent); fine-tuned vs stock VAE decoder.
- **Controls:** bicubic resampling anchor (isolates *learned* compression); identity;
  oracle-segmenter error floor measured on originals.
- **Robustness:** oracle-free survival scoring via matched filtering (removes oracle bias);
  survival measured with a second segmenter architecture.
- **Generalization:** cracks (DeepCrack) and one 3D probe (MedVAE 3D on a CT vessel subset,
  round-trip only) to show the protocol ports across dimensionality.

### Expected results (HYPOTHESIZED)
f8 VAEs: survival < 50% at 1–2 px, < 90% at 3–5 px (w* ≈ 4–8 px); f4: w* ≈ 2–4 px; MedVAE
(medically trained) modestly better at matched factor; bicubic control survives 2 px+ (learned
compression, not sampling theory, is the binding constraint); Arm B latent-arm recall deficit
concentrated below measured w*, matching the curve within ±10%.

### Negative interpretation
No floor → belief-correcting datasheet note ("modern f8 VAEs preserve 2-px structures"), modest
but citable; floor exists but downstream deficit doesn't track it → conditioning/generation
dominates, the datasheet remains valid as an upper bound and the downstream claim dies — report
both curves so the field sees where the loss actually enters.

### Stop criteria
- Stop after MVE if no floor (skip Arm B entirely — the expensive arm is gated on the cheap one).
- Arm B capped at the pre-registered matched budget; no rebalancing after results are seen.
- Hard cap 40 A100-days.

### Killer Experiment
**Round-trip-predicts-downstream:** the pointwise match (±10% recall) between the no-generation
round-trip survival curve and the latent-arm width-stratified recall deficit at matched compute.
This is the only experiment that ties the floor causally to the training-data penalty while
excluding conditioning by construction. If the match fails, the floor paper survives only as a
datasheet; the causal claim dies. Cost of the killer: Arm A (2 A100-days) + Arm B (~33
A100-days).

### ROI: **7/10.** The MVE is nearly free and decisive for the floor's existence; the full causal
claim is mid-cost; ceiling is a protocol/datasheet contribution — durable but rarely
headline-grabbing.

---

## E5. B-0230 (PROTECTED) — Label-cleanliness vs image-distribution decomposition of synthetic data

### RQ
For rendering/simulation pipelines whose labels are clean by construction, what fraction of the
synthetic-vs-real utility difference is attributable to label cleanliness rather than image
distribution, as a function of data scale?

### Hypothesis
A material fraction of rendered data's measured utility in low-data regimes comes from its
perfect labels; injecting label noise calibrated to *measured* human annotation error into
synthetic labels erases that fraction, and cleaning real labels recovers a comparable amount from
the other side.

### Falsifiable prediction (pre-registered)
At 5–25% data scales, injecting measured-calibration noise into synthetic labels closes ≥ 40% of
the synth-vs-real utility gap in both tasks under at least one of three pre-registered calibrated
noise models. Falsified if < 10% of the gap moves under all calibrated noise models at all scales
— "it's the images", equally decision-relevant (invest in generation, not annotation QC).

### Method
1. **Scope (Stage-4 condition):** rendered/simulated pipelines only — labels clean by
   construction. Task 1: GTA5 → Cityscapes semantic segmentation (driving). Task 2: Hypersim →
   NYUv2-40 indoor semantic segmentation (Hypersim: 77,400 rendered images with full GT
   [verified this session]).
2. **Measured noise calibration (Stage-4 condition — no parametric guessing).** Three calibrated
   noise models, each fit to real measured disagreement: (a) boundary jitter with magnitude
   distribution fit to Cityscapes fine-vs-coarse annotation discrepancies on the same images
   (a *measured* human annotation-quality axis that ships inside Cityscapes); (b) polygon
   simplification fit to the same statistics; (c) class-confusion/instance-omission fit to
   multi-rater disagreement statistics from QUBIQ (3–7 raters/task [verified this session]) and
   LIDC-IDRI (4 raters, via pylidc/FLamby [verified this session]) transported as rates, with
   transport sensitivity reported.
3. **Pre-registered 4-arm grid:** {real+own labels; real+consensus-cleaned labels (Cityscapes
   fine as the "cleaned" arm for the coarse-label variant); synth+clean labels;
   synth+injected-noise labels} × scales {5, 10, 25, 50, 100%} × 2 tasks × 3 seeds. Fixed
   architecture + schedule (SegFormer-B2 via mmsegmentation standard configs).
4. **Decomposition readout:** cleanliness share = [U(synth,clean) − U(synth,noisy)] /
   [U(synth,clean) − U(real,own)], per scale/task/noise model, with the noise-model sensitivity
   reported as a first-class result (Stage-4 condition).

### Data
GTA5, SYNTHIA (secondary), Cityscapes fine+coarse (all public); Hypersim (apple/ml-hypersim)
[verified this session]; NYUv2-40; QUBIQ + LIDC-IDRI for noise-rate calibration [verified this
session].

### Baselines
Mixed real+synth arm at each scale (the practitioner's default); label-noise-robust loss arm
(e.g. symmetric CE) to test whether cheap robustness tricks recover the injected loss.

### Metrics
mIoU (+ boundary F-score, since label noise is boundary-concentrated); cleanliness share with
bootstrap CIs; share-vs-scale curves; noise-model sensitivity band.

### Real reusable codebases
- mmsegmentation (standard GTA5/Cityscapes/NYUv2 configs, SegFormer/DeepLabv3+).
- github.com/apple/ml-hypersim (dataset + tooling) [verified this session].
- Cityscapes scripts (official label tooling).
- github.com/hongweilibran/qubiq + pylidc + owkin/FLamby (fed_lidc_idri) for rater-disagreement
  statistics [verified this session].

### GPU/time budget
4 arms × 5 scales × 2 tasks × 3 seeds = 120 runs, cost-weighted by scale (low-scale runs are
short): ≈ 55 full-run-equivalents at ~0.7 A100-day each → **~40 A100-days**, plus noise-model
fitting (CPU) and +15 A100-days for the mixed-arm baseline and noise-robust-loss arm →
**~55–70 A100-days full program**.

### MVE (go/no-go)
GTA5→Cityscapes, 10% scale, 4 arms × 1 seed × noise models (a)+(c). **~4–6 A100-days.**
Go if noise injection moves synthetic utility by ≥ 2 mIoU under either calibrated model. No-go
if < 1 mIoU: label cleanliness is second-order at this scale — check the 5% scale once (cheap)
before declaring the negative.

### Experiment ladder
- **Full:** grid above + share-vs-scale curves + sensitivity band.
- **Ablations:** noise magnitude dose-response (0.5×/1×/2× calibrated level — links share to
  measured noise level continuously); architecture swap (DeepLabv3+); boundary-weighted loss.
- **Controls:** real+consensus-cleaned arm (the decomposition's other side); noise injected into
  *real* labels at matched calibration (symmetry check: does noise hurt real and synth labels
  equally? If not, image distribution interacts with label noise — reported, not hidden).
- **Robustness:** three noise models as first-class sensitivity; seeds; scale replication.
- **Generalization:** second task (Hypersim→NYUv2); SYNTHIA swap-in for GTA5 (renderer
  independence).

### Expected results (HYPOTHESIZED)
Cleanliness share 30–60% at 5–25% scales, declining below 20% at 100% scale (perfect labels
matter most when data is scarce); noise-robust losses recover only part of the injected loss;
boundary F-score shows larger shares than mIoU (noise is boundary-concentrated).

### Negative interpretation
"< 10% under all calibrated models" → the synthetic advantage is the images; annotation-QC
investment does not substitute for generation; the calibrated-noise toolkit and fine-vs-coarse
calibration method remain reusable artifacts. Either branch prices the generation-vs-QC
investment question — the reason this survived Stage 4.

### Stop criteria
- Stop after MVE (+5% check) on no-go.
- Drop the second task if Task-1 share CI is narrower than ±10% and both noise models agree
  (diminishing returns); otherwise second task is mandatory before any claim.
- Hard cap 75 A100-days.

### Killer Experiment
**The calibrated-noise erasure test:** pre-registered ≥ 40% gap closure at low scales under
measured-calibration noise, with the noise-model sensitivity band published alongside. The
Stage-4 "noise model determines the answer" attack is defused only if the share is stable across
the three measured calibrations — instability itself falsifies the headline (and is reported).
Cost of the killer alone: ~12 A100-days (one task, 3 scales, 4 arms, 2 noise models, 2 seeds).

### ROI: **7/10.** Clean falsification and direct investment guidance, but the costliest grid in
this cluster and a share-type headline that is easier to argue with than a flip rate or a
leaderboard reorder. Distinct by design from A-0271 (auto-label filter attribution on real
images) and C-0229 (task-vs-data decomposition): this prices the *label-noise* axis of
*synthetic images* (see dedup section).

---

## E6. B-0331 — Report negations as spatially grounded negative supervision

### RQ
Do negations parsed from radiology reports, grounded to anatomical regions, carry per-patient
spatial information that reduces false positives of report-supervised chest-X-ray models beyond
(a) a matched class-prior baseline and (b) permuted-report negatives?

### Hypothesis
"No pneumothorax" grounded to the pleural/apical regions of *this* patient is worth more than the
population prior, because negation prevalence and location co-vary with patient context; training
with atlas-grounded negative losses reduces FPs concentrated in frequently negated finding
classes, and the gain survives both information-content controls.

### Falsifiable prediction (pre-registered)
On held-out gold-annotated data, the negation arm reduces per-class FPs at matched sensitivity by
≥ 5% relative over the matched class-prior control for at least half of the frequently negated
finding classes, with permuted-report negatives landing between prior-control and true-negation
arms. Falsified if negation ≤ class-prior control across classes — negations are just priors;
the idea is dead (Stage-4 concession).

### Method
1. **Parsing.** Extract negations per report from MIMIC-CXR free text with the CheXpert labeler
   (stanfordmlgroup/chexpert-labeler [inherited, Stage-3]) cross-checked with NegBio; RadGraph
   (PhysioNet) relations for finding-anatomy links where present.
2. **Grounding.** Map each negated finding to anatomical regions via Chest ImaGenome (242,072
   scene graphs; 29 anatomical bounding-box locations per frontal image; atlas-based extraction
   with 1,071 manually validated bbox images available for misgrounding audit) [verified this
   session]. Conservative margins: erode region boxes; drop images flagged for devices/support
   hardware; CheXmask anatomical masks (676,803 masks with per-mask RCA quality scores) [verified
   this session] refine lung-field negatives.
3. **Training arms (identical architecture/schedule).** Multi-label per-region finding model
   (region features from ImaGenome boxes; per-region per-finding logits) and a dense per-pixel
   variant (U-Net multi-head): (a) positives only (report-supervised baseline); (b) + negation
   negatives (region-grounded); (c) + matched class-prior negatives — same total negative mass
   per class, assigned by population frequency without reading the patient's report; (d) +
   permuted-report negatives — negations transplanted from a different patient (marginals
   preserved, per-patient information destroyed). Arms (c) and (d) are the killer's controls.
4. **Evaluation.** Gold spatial GT, all public: VinDr-CXR radiologist boxes; SIIM-ACR
   pneumothorax masks (Kaggle); MS-CXR phrase-grounding gold boxes (PhysioNet). Note: CANDID-PTX
   is now access-restricted (Health New Zealand internal) [verified this session] — excluded
   from the plan. Report per-finding FP at matched sensitivity, stratified by the finding's
   negation frequency; the pre-registered interaction test: gain(b over c) increases with
   negation frequency.
5. **Poisoning bound.** Misgrounding rate audited on ImaGenome's manually validated subset;
   margin-erosion sensitivity sweep (0/5/10% erosion); per-arm performance on anatomically
   deviant cases (device-present, effusion-distorted) reported separately.

### Data
MIMIC-CXR-JPG + reports (PhysioNet, credentialed); Chest ImaGenome; CheXmask; VinDr-CXR;
SIIM-ACR; MS-CXR. All public/credentialed-public.

### Baselines
Arm (a); class-frequency thresholding on arm (a) outputs (zero-training prior baseline);
CheXpert-labeler image-level negative supervision without spatial grounding (image-level vs
region-level value of the same negation).

### Metrics
Per-finding FP rate at matched sensitivity (primary); AUROC per region-finding; localization
FROC on VinDr/MS-CXR; Dice on SIIM-ACR pneumothorax; negation-frequency interaction coefficient;
misgrounding rate + sensitivity band.

### Real reusable codebases
- stanfordmlgroup/chexpert-labeler [inherited]; ncbi-nlp/NegBio; RadGraph (PhysioNet).
- Chest ImaGenome loaders (PhysioNet distribution includes scene-graph JSONs keyed to MIMIC-CXR
  DICOM ids) [verified this session].
- CheXmask (PhysioNet) [verified this session].
- mlmed/torchxrayvision (CXR model zoo + dataset loaders); MONAI for the dense variant.

### GPU/time budget
Parsing/grounding: CPU, ~1 week of pipeline engineering. Training: 4 arms × 3 seeds × 2 model
variants at ~1–1.5 A100-days per run (224–512 px, ~240k images, mixed precision) →
**~25–30 A100-days full program**; evaluation inference negligible.

### MVE (go/no-go)
Three findings (pneumothorax, pleural effusion, consolidation), 50k-image subset, arms (a)–(d),
region-level model only, 1 seed. **~4 A100-days.** Go if arm (b) beats arm (c) on FP at matched
sensitivity for ≥ 2 of 3 findings with CI separation. No-go if (b) ≤ (c) everywhere → negations
are priors; publish the negative with the controls (cheap, clean, still citable as the first
information-content measurement of report negations).

### Experiment ladder
- **Full:** all frequently negated findings (~10 classes) × 4 arms × 3 seeds × both model
  variants; interaction test; poisoning bound.
- **Ablations:** grounding granularity (whole-lung vs ImaGenome region vs CheXmask-refined);
  negative-loss weight; parser (CheXpert-labeler vs NegBio agreement subset only).
- **Controls:** arms (c) and (d) (the design's core); image-level-negation arm (spatial grounding
  value isolated).
- **Robustness:** margin-erosion sweep; device/deviant-anatomy strata; label-shift check across
  evaluation datasets (MIMIC→VinDr transfer).
- **Generalization:** one non-CXR probe if cheap — abdominal CT reports with "no X" statements
  mapped to TotalSegmentator organ masks on a public reports+CT subset; exploratory only,
  dropped without prejudice if data access stalls.

### Expected results (HYPOTHESIZED)
Negation arm: 5–15% relative FP reduction over the class-prior control in frequently negated
classes (pneumothorax, effusion); permuted arm intermediate; gains concentrated in
high-negation-frequency classes (positive interaction); misgrounding ≤ 10% on validated subset
with margins.

### Negative interpretation
(b) ≤ (c): the report's cleanest channel is informationally empty at organ scale — a decisive,
control-backed negative that stops a plausible archive-mining program before the field wastes
effort; the parsing+grounding pipeline still ships as reusable infrastructure. (b) > (c) but no
interaction: negations help but not via per-class frequency — mechanism revision, still
publishable.

### Stop criteria
- Stop after MVE on no-go (the two controls make the negative airtight).
- Stop the dense variant if the region-level model shows no signal (dense is strictly harder).
- Hard cap 35 A100-days.

### Killer Experiment
**The two-control information test:** negation negatives must beat BOTH the matched class-prior
control and the permuted-report control at matched sensitivity, with the pre-registered
negation-frequency interaction. This is exactly the quantity the Stage-4 "information-free"
attack denies; no cheaper experiment answers it, and its failure is fatal by design. Cost of the
killer alone: the MVE + 2 seeds ≈ 8 A100-days.

### ROI: **6/10.** Decisive controls and archive-scale relevance, but CXR-scoped payoff, heavier
data engineering (credentialed access, parsing, grounding), an expected effect size in the
5–15% relative range, and gold evaluation thinned by the CANDID-PTX restriction.

---

## E7. B-0112 (+ M4/B-0159 merged) — Convention-shift program: formalization, audit detector, convention tokens

### RQ
Is annotation-convention shift (identical images, different label conventions) a formally
distinct, detectable, and controllable shift class? Three registered sub-questions: (1) do
adaptation methods harm under pure convention shift while helping under pure covariate shift?
(2) can a dataset-audit detector separate the two regimes without target-convention
re-annotation? (3) do convention tokens trained on controlled relabelings recover and
interpolate the convention axis?

### Hypothesis
Convention shift produces a signature — matched image-feature distributions with systematic,
direction-consistent, boundary-concentrated label disagreement — that (1) makes feature-level
adaptation categorically harmful, (2) is detectable in the audit setting, and (3) is
low-dimensional enough to expose as a switchable, interpolable token.

### Falsifiable predictions (pre-registered, one per leg)
(1) TENT/BN-recalibration/self-training change true target-convention error by ≤ 0 (no help or
harm) under pure convention shift while improving ≥ +2 Dice under matched covariate shift —
falsified if adaptation helps equally in both regimes. (2) Detector AUROC ≥ 0.85 separating
convention-pair from covariate-pair panels, held-out datasets — falsified below 0.7.
(3) Token interpolation produces monotone mask sequences (volume and boundary offset monotone in
interpolation coefficient) and blinded raters place interpolated masks between endpoint
conventions ≥ 80% of the time — falsified at chance.

### Method
1. **Zero-annotation real conventions (Stage-4 defense).** Nested label hierarchies on identical
   images: BraTS 2021 enhancing-tumor ⊂ tumor-core ⊂ whole-tumor; KiTS23 tumor ⊂ tumor+cyst ⊂
   whole-kidney; LiTS lesion vs lesion+liver. Each nesting level = a written convention applied
   to the same voxels; appearance confound removed by construction.
2. **One bounded controlled relabeling.** ~200 images (single 2D slice each, budget-bounded)
   relabeled under two written guidelines by 2 annotators each (e.g. lesion boundary with/without
   perilesional margin on a public CT/MR subset); this is the only human-annotation cost and the
   ground truth no prior token work has [inherited, Stage-3 verification].
3. **Leg 1 — direction-of-harm.** Train nnU-Net source models per convention; "deploy" onto
   (a) same images, other convention (pure convention shift) and (b) other-site images, same
   convention — multi-site prostate T2 (NCI-ISBI 2013 / PROMISE12 / PROSTATEx, the standard
   public multi-site trio) as the covariate comparator. Run TENT (github.com/DequanWang/tent
   [inherited tooling; standard]), BN-recalibration, and pseudo-label self-training; measure true
   error against the target convention's labels vs the apparent (unsupervised) adaptation
   objective — the pre-registered dissociation: apparent objective improves while true error
   worsens under convention shift.
4. **Leg 2 — audit detector.** Inputs computable in the audit setting (both datasets with their
   own labels; no re-annotation): image-feature distributional distance (encoder MMD) crossed
   with model-vs-target-label disagreement structure (boundary concentration, signed bias
   consistency, volume-ratio systematicity). Train/freeze the detector on a construction panel
   (nested-hierarchy pairs + cross-site pairs from public multi-site collections); test on
   held-out pairs incl. the controlled relabeling. Claim scoped to dataset audits (Stage-4
   honesty condition).
5. **Leg 3 — convention tokens.** One segmenter conditioned by a convention token (FiLM/prompt
   token on a nnU-Net-class or SAM-based backbone), trained jointly on conventions of identical
   images (nested hierarchies + relabeled subset). Tests: switching (correct-token Dice ≈
   per-convention specialist; swapped-token Dice drops in the predicted direction);
   interpolation (automatic monotonicity + 3 blinded raters × ~100 samples).

### Data
BraTS 2021 (1,251 cases), KiTS23, LiTS (all public); NCI-ISBI-2013/PROMISE12/PROSTATEx
(public multi-site prostate); ~200-image relabeling (annotation budget: 2 annotators × ~15 h);
LIDC-IDRI multi-rater masks as auxiliary rater-variability contrast (variance vs systematic
convention) [verified this session].

### Baselines
No-adaptation source model; oracle per-convention supervised model (ceiling); for the detector:
feature-distance-only and disagreement-only single-signal detectors (shows both signals are
needed); for tokens: separate per-convention models (parameter-matched) and dataset-token
baseline without convention-controlled training data (the M4 attack's strawman, included to be
beaten).

### Metrics
Leg 1: Δtrue-Dice under adaptation per regime + apparent-objective trajectory (the dissociation
plot). Leg 2: AUROC/AUPRC on held-out pairs. Leg 3: switching Dice matrix, monotonicity rate,
blinded-rater ordering accuracy, convention-classification of outputs.

### Real reusable codebases
- MIC-DKFZ/nnUNet [verified this session]; MONAI.
- github.com/DequanWang/tent (TENT, ICLR 2021) [standard public implementation].
- BraTS/KiTS/LiTS loaders in MONAI/nnU-Net ecosystems [verified this session].
- pylidc for LIDC rater masks [verified this session].
- SAM fine-tuning stacks (facebookresearch/segment-anything) if the token backbone is promptable
  [verified this session].

### GPU/time budget
Leg 1: ~8 source trainings + cheap TTA runs ≈ 10 A100-days. Leg 2: panel of ~15 pair models
(many reuse Leg-1 models) + detector (CPU/light) ≈ 8 A100-days. Leg 3: 3–5 token-model trainings
+ specialists ≈ 10 A100-days. **~30–40 A100-days full program** + annotation budget (2 × ~15 h
annotator time) + 3 raters × ~2 h for blinded judgment.

### MVE (go/no-go)
Leg 1 only, BraTS: source trained on tumor-core, deployed on whole-tumor labels of the *same*
images (pure convention shift) vs a cross-site BraTS split at fixed convention (covariate
proxy); TENT + BN-recalib. **~3 A100-days.** Go if the dissociation appears (apparent objective
improves, true error flat/worse under convention shift; true error improves under covariate
shift). No-go if adaptation is equally helpful/harmless in both regimes — the program's
motivating premise fails and all three legs die together (cheap kill).

### Experiment ladder
- **Full:** all three legs across the three nested-hierarchy datasets + prostate covariate panel
  + controlled relabeling + blinded rater study.
- **Ablations:** adaptation method family (entropy vs BN-stats vs pseudo-label); detector input
  ablation (feature-only / disagreement-only / joint); token injection point and dimension;
  token training with vs without controlled-relabeling data (isolates M4's added value).
- **Controls:** identical-image construction (appearance confound removed by design); LIDC
  rater-variance contrast (unsystematic noise must NOT trigger the detector — specificity
  control); label-permutation null for the detector.
- **Robustness:** convention-pair severity sweep (ET-vs-TC subtler than ET-vs-WT); cross-dataset
  detector transfer (train BraTS/KiTS panels → test LiTS + relabeling).
- **Generalization:** natural-image spot check — road with/without shoulder or sidewalk
  convention synthesized from Cityscapes label hierarchy (identical images, two written
  conventions from the official label spec) to show the phenomenon is not medical-only.

### Expected results (HYPOTHESIZED)
Leg 1: TENT/self-training worsen true error by 2–8 Dice under convention shift while their
objectives improve (the dissociation); BN-recalib ≈ no-op; covariate arm gains +2–5 Dice.
Leg 2: joint detector AUROC 0.85–0.95; single-signal detectors ≤ 0.75. Leg 3: switching within
2 Dice of specialists; monotone interpolation ≥ 90% of cases; rater ordering ≥ 80%.

### Negative interpretation
Leg-1 failure: adaptation methods are convention-robust in practice — surprising, publishable as
a corrective to the harm narrative, but kills the program's urgency. Leg-2 failure with Leg-1
success: harm is real but undetectable without labels — narrows the contribution to the
formalization + harm demonstration (still a paper). Leg-3 failure: conventions are not
low-dimensional/token-controllable — the M4 merge dies, B-0112's audit half stands alone.

### Stop criteria
- Stop everything after MVE if Leg 1's dissociation is absent.
- Legs are severable: pre-registered decision points after each leg; Leg 3 requires Leg 1 pass
  (tokens without demonstrated harm have no motivation).
- Annotation spend gated on Leg-1 pass (no relabeling budget before the premise survives).
- Hard cap 45 A100-days + 40 annotator-hours.

### Killer Experiment
**The direction-of-harm dissociation on identical images (Leg 1 + specificity control):**
adaptation's unsupervised objective improves while true target-convention error worsens on the
same voxels — with LIDC rater-noise pairs showing no such systematic signature (specificity).
This kills or validates the formalization premise for ~3 A100-days; Legs 2–3 are staged behind
it. Full-program falsification requires all three pre-registered predictions.

### ROI: **6/10.** Highest ceiling in the cluster (formalization + detector + method in one
program; the only methods-flavored survivor) but the most failure points, the only human
annotation budget, and a three-leg structure where the payoff requires at least two legs to land.
The severable staging protects the investment.

---

# Cross-cluster killer-experiment dedup (A/C Stage-4 keeps read this session)

Checked against `stage4_cluster_A_keep.md` (A-0002, A-0017, A-0061, A-0062, A-0107, A-0178,
A-0271) and `stage4_cluster_C_keep.md` (C-0028, C-0090, C-0128, C-0158, C-0229, C-0302, C-0310).
No B killer duplicates an A/C killer; four adjacencies are noted and held disjoint by design:

1. **B-0112 vs A-0062 (soft multi-annotator boundaries).** A-0062's killer is sigma-stratified
   gain decomposition against *unsystematic* rater noise; B-0112's killer is the
   direction-of-harm dissociation on *systematic written-guideline* conventions built from nested
   hierarchies — different instruments, and B-0112's LIDC specificity control explicitly verifies
   the detector ignores A-0062's phenomenon.
2. **B-0212 vs C-0128 (edit artifacts).** C-0128 calibrates evaluation-time edit artifacts
   (null-edit noise floor) to measure context reliance of frozen models; B-0212 manipulates
   training-data compositing artifacts and measures trained-model transfer. Different lever
   (train-time vs eval-time), different claim (shortcut law vs context score). No shared arm.
3. **B-0230 vs A-0271 (identical-images, vary-labels template) and vs C-0229 (decomposition
   template).** A-0271 attributes auto-label *filter-stage* signatures on real images; C-0229
   decomposes task-vs-data value with exact multi-label controls; B-0230 prices the *label-noise*
   axis of *rendered images* via calibrated noise injection. Shared design vocabulary, disjoint
   measured quantities; no shared datasets in the killer arms.
4. **M5 vs killed C-0276 (protocol-drift harness, salvaged as infra).** Inherited Stage-4
   scoping preserved: C-0276 measures implementation variance of the same model; M5 measures
   decision-rule invariance of published deltas *between* models. If the C-cluster builds the
   fixed-checkpoint harness, M5 reuses it for inference reproducibility, not as a claim.

B-0121, B-0222, B-0331 have no killer-experiment analog anywhere in the A/C keep lists
(wrong-support counterfactual, round-trip compression phantoms, and two-control negation
information test are unique to Cluster B).
