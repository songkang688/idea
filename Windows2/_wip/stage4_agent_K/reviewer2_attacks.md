# Agent K — Reviewer-2 Attacks + Freshness Assassination: Batch C LOCK (+ D's next bets)

**Role:** Reviewer #2 / freshness assassin for batch-C eval-science LOCK ideas. Not the PI; no final-3.
**Posture:** every idea is treated as a *submitted paper*; the default belief is "already done, or no experiment can silence the reviewer." Calibration bar taken from Agent H: **zero bare SURVIVEs were granted**.
**Coverage:** all 32 C LOCK IDs from Agent G's `provisional_200_partial.md`, plus 6 of Agent D's next-best bets that G placed in FLEX (C-0345, C-0303, C-0119, C-0321, C-0193, C-0277). All 20 of D's explicit "PhD-year bets" are already inside the LOCK set. **Total: 38 attacks.**
**Verification hygiene:** every URL below was returned by live web search this session, or is explicitly marked [inherited from D/G's verified lists]. No invented citations. Epistemic labels: KNOWN (retrieved), EVIDENCE (supports, doesn't settle), HYPOTHESIS (my inference).

**Three structural attacks applied to every "re-analysis given zoo checkpoints" idea** (G already repriced #1):

- **S1 — prediction-cache:** no public per-instance prediction bundles exist; "analysis-only" = "inference + analysis" (GPU-days). Confirmed by G's census; not fatal, but every abstract claiming "pure re-analysis" is now overclaiming.
- **S2 — venue:** "this is not a method paper." NeurIPS D&B / analysis tracks absorb only a few "your benchmark is broken" papers per cycle; the C LOCK set alone contains ~20 competitors for those slots, many citing each other's turf. Any single idea's acceptance probability is coupled to how many siblings the lab also submits.
- **S3 — annotation-noise scoop:** the GT-epistemology family shares one thesis ("test labels are too noisy to support current claims"). **This scoop is no longer hypothetical:** Label Convergence (WACV 2025), Noise-Aware Evaluation of Object Detectors (WACV 2025), COCO-ReM (ECCV 2024), MJ-COCO-2025, and a label-error detection/correction benchmark (arXiv 2508.06556) have already published overlapping shares of it. Each family member must now say what it adds *beyond five existing papers*, not beyond zero.

Verdict vocabulary: **SURVIVE** (unconditional — not granted), **SURVIVE-IF-EXPERIMENT** (survives only with the named control/experiment), **MUTATE** (headline dead; narrower claim named), **KILL**.

---

## PART 1 — GT-epistemology family (S3 exposure maximal)

### 1. W2-C-0344 — Instructions beat annotators (labeling-protocol A/B experiment)

**Fresh prior work (searched this session):**
- *Labelling instructions matter in biomedical image analysis*, Rädsch et al., **Nature Machine Intelligence 2023**. https://doi.org/10.1038/s42256-023-00625-5 — KNOWN: systematic study of labeling instructions on annotation quality; 14,040 images, 156 professional annotators + 708 MTurk workers, instruction arms with different information density; exemplary images boost quality, text extension does not; measured on Dice.
- *Improving Task Instructions for Data Annotators*, arXiv:2312.14565 — KNOWN: 307-annotator experiment; rules beat vague standards by 14% accuracy.
- Murrugarra-Llerena et al., CVPRW 2022 [inherited from D] — sub-pixel box discrepancies distort AP.

**Harshest rejection:** "The flagship claim — labeling instructions materially change the labels — was published in Nature Machine Intelligence in 2023 with an A/B design two orders of magnitude larger than your 300-image budget. Your contribution is porting a known effect to boxes."
**Hidden assumptions:** (a) instruction effects on *boxes* behave like segmentation/instance masks; (b) 300 images × 2 arms has power to separate between-arm effect from within-arm annotator noise (no power analysis was ever run for this design); (c) downstream model-AP deltas from instruction-induced label shifts exceed AP measurement noise on 300 images — at n=300, bootstrap AP noise is huge, likely swamping the effect.
**Killer experiment:** exists but is NOT the current design. Two-arm instruction A/B on ≥1k images with pre-registered power analysis, endpoints = (i) between-arm GT divergence in AP-equivalent units vs within-arm inter-annotator divergence, (ii) the induced spread on a *fixed leaderboard*: score 10 public detectors against both GT arms and count rank inversions. The leaderboard-margin comparison is what Rädsch et al. do not have.
**Verdict: MUTATE.**
**Mutated one-liner:** *The instruction term in detection ground truth: an A/B protocol experiment showing labeling-instruction choice moves benchmark AP and model rankings by more than inter-annotator noise — and by more than typical published deltas.*
**Structural notes:** S3 direct hit (this is the family's most-scooped member). S2 applies. Cheap enough to survive S2 if executed as the quantitative-yardstick version.

### 2. W2-C-0338 — The small-object ceiling is human (hosts 0071 arm)

**Fresh prior work:**
- *Label Convergence*, Tschirschwitz & Rodehorst, WACV 2025, arXiv:2409.09412. https://arxiv.org/abs/2409.09412 — KNOWN (re-verified): LVIS doubly-annotated subset + bootstrap gives an upper bound of 62.6–67.5 mAP; Co-DETR at 66.8 sits at the bound; explicitly concludes "model capacity is sufficient" and calls for multi-annotated data.
- *Noise-Aware Evaluation of Object Detectors*, Murrugarra-Llerena & Jung, WACV 2025. https://openaccess.thecvf.com/content/WACV2025/html/Llerena_Noise-Aware_Evaluation_of_Object_Detectors_WACV_2025_paper.html — KNOWN: quantifies corner-wise annotation noise on COCO, proposes noise-aware upper/lower AP bounds, shows AP is most distorted **for small objects** and strict IoU thresholds.
- *Noise-Robust Tiny Object Localization with Flows* (TOLF), arXiv:2601.00617 — KNOWN: manual review finds ~34.2% of AI-TOD test boxes noisy; 2-pixel shift = >20% IoU drop at 10×10 px.
**Harshest rejection:** "Label Convergence already established the human-consistency ceiling and that SOTA sits at it; Noise-Aware Evaluation already showed AP is most corrupted for small objects. Your 'size floor' is the intersection of two published results."
**Hidden assumptions:** (a) the *size-resolved* ceiling curve differs enough from the aggregate ceiling to be interesting; (b) fresh human re-annotation at small sizes is feasible at claimed budget (TOLF's 34% noise rate suggests annotators may simply be unable to do the task — which is the thesis, but also means the "human ceiling" estimate itself will have huge error bars exactly where the claim lives); (c) LVIS double annotations have enough sub-16px instances for size stratification (unverified — HYPOTHESIS).
**Killer experiment:** yes — the one neither WACV paper ran: per-size-bin human-human agreement AP vs model-GT AP on the same instances, with a pre-registered crossing-point estimate ("below s pixels, human-GT agreement ≤ model-GT agreement, so claimed AP-small progress below s is unfalsifiable"), plus a check of published AP-small deltas against the bin noise. Requires the LVIS double-annotation size census *first* (one day) — if sub-16px counts are too low, budget fresh double annotation of small-object strata only.
**Verdict: SURVIVE-IF-EXPERIMENT** (the size-resolved crossing-point experiment with the census precondition; Label Convergence + Noise-Aware Eval must be paragraph-one citations).

### 3. W2-C-0046 — Annotation-noise band CIs for COCO AP (+0080 tightness-drift arm)

**Fresh prior work:** Label Convergence (above) — KNOWN: this IS a noise-derived performance band on detection mAP, built from the same LVIS double-annotation artifact G's census assigned to this idea, with bootstrap CIs. Noise-Aware Evaluation (above) — KNOWN: noise-aware upper/lower bounds around AP for COCO, per stratum. COCO-ReM, arXiv:2403.18819 — KNOWN: ranking changes under corrected GT.
**Harshest rejection:** "Two WACV 2025 papers already propagate annotation disagreement into detection-AP bounds — one from double annotations (Label Convergence), one from corner-wise noise models (Noise-Aware Evaluation). Your 'annotation-noise band' is their union. The only unclaimed piece is auditing published deltas against the band — which is a table, not a paper, and it is the same table your companion submission (0302) already promises."
**Hidden assumptions:** (a) the band construction differs meaningfully from the two published constructions (it does not — the input artifact and the bootstrap are identical to Label Convergence's); (b) the claims-audit constitutes a standalone contribution (it duplicates 0302's claims re-analysis arm).
**Killer experiment:** NONE that rescues standalone status. Any experiment worth running (the claims audit) lives more naturally inside 0302 (MDE tables) or 0311 (uncertainty budget).
**Verdict: KILL** (freshness kill; D's own MUTATE verdict in `prior_work_attack.md` §1 anticipated this — the mutation target has now itself been published). Residual: the 0080 intra-dataset tightness-drift arm transfers to 0311 as one budget component; the claims-audit transfers to 0302.

### 4. W2-C-0326 — Half the remaining COCO errors are not model errors

**Fresh prior work:** TIDE, arXiv:2008.08115 [inherited from D]; COCO-ReM (above); MJ-COCO-2025, https://github.com/MJCOCO-2025/MJ-COCO-2025-Dataset + Neurocomputing 2026 paper (arXiv:2506.00997 per repo) — KNOWN: fully automated re-annotation fixing missing/duplicate/group errors on COCO; *From Label Error Detection to Correction*, arXiv:2508.06556 — KNOWN: modular framework + benchmark for label-error detection AND correction in OD datasets, with human-in-the-loop correction studies.
**Harshest rejection:** "TIDE showed it in 2020; COCO-ReM corrected it in 2024; MJ-COCO automated it in 2025; 2508.06556 built the correction benchmark. The 'share of residual errors that are GT problems' is now derivable from existing artifacts — diff any SOTA model's FPs against COCO-ReM/MJ-COCO corrections and you have the number without any new annotation."
**Hidden assumptions:** (a) ReM/MJ-COCO corrections are not themselves the arbiter — but if they are treated as truth, the study is a diff script; if they are not, the study needs its own adjudication, and then reviewers ask why the existing corrections weren't good enough; (b) "deployment thresholds" is a well-defined operating point (it is not; must be pre-registered).
**Killer experiment:** yes — the version that beats the diff-script objection: stratified sample of residual errors of 3 SOTA detectors, *independent two-annotator adjudication with disagreement resolution*, reporting (i) the GT-problem share with CIs, (ii) agreement between the human adjudication and ReM/MJ-COCO automated corrections — the last arm converts the two competitor artifacts into evaluees and yields the quotable "even the corrected sets disagree with humans X% of the time."
**Verdict: SURVIVE-IF-EXPERIMENT** (two-annotator powered adjudication including the corrections-as-evaluees arm; urgency high — each new corrected-COCO release shrinks the open share).

### 5. W2-C-0007 — Annotation-noise floor for tiny objects

**Fresh prior work:** TOLF arXiv:2601.00617 (34.2% noisy boxes on AI-TOD; scale-resolved noise-sensitivity analysis); Noise-Aware Evaluation WACV 2025 (AP distortion largest for small objects).
**Harshest rejection:** "The tiny-object noise floor is now published twice: a WACV 2025 paper says AP-small is the most noise-corrupted stratum, and a 2026 method paper measured a 34% bad-box rate on the leading tiny-object benchmark and even characterized IoU sensitivity by scale. Whether 'sub-16px AP is meaningful' is answered: mostly not."
**Hidden assumptions:** that a dedicated floor paper adds anything beyond 0338's size-resolved ceiling — it does not; the two ideas share both infrastructure and conclusion.
**Killer experiment:** none standalone; the decisive experiment is 0338's crossing-point design.
**Verdict: MUTATE** — fold into 0338 as its benchmark-facing arm (AI-TOD/COCO AP-small floor tables). No portfolio slot.

### 6. W2-C-0259 — Dense "label everything nameable" re-annotation (salience bias)

**Fresh prior work:** LVIS federated design, arXiv:1908.03195 [inherited]; COCO-ReM non-exhaustiveness findings (above); 2508.06556 (missing-label detection). No paper found this session that measures *annotator salience bias* by exhaustive re-annotation of a benchmark subset — the specific instrument appears unclaimed.
**Harshest rejection:** "That benchmarks under-annotate non-salient objects is why LVIS went federated in 2019 — you are re-measuring the design rationale of an existing dataset. And your 'FP population' result is confounded: models flag objects your own annotators will also miss, so the exhaustive set inherits its own salience bias."
**Hidden assumptions:** (a) "everything nameable" is operationalizable — annotation stopping rule dominates the result and must be pre-registered; (b) 200 images support class-level salience conclusions (power analysis needed); (c) second-pass model-assisted mining doesn't circularly define the FP population.
**Killer experiment:** yes — two-protocol exhaustive re-annotation (free recall vs checklist-prompted) on the same images; salience bias = the checklist-minus-recall increment, by size/class/position; then re-score public detectors against both to bound the "penalized-for-being-right" share. The two-protocol design also feeds 0344.
**Verdict: SURVIVE-IF-EXPERIMENT** (two-protocol design with pre-registered stopping rule; bundle with 0344/0338 infrastructure or S2 will kill all three separately).

### 7. W2-C-0043 — Dice on small structures is a coin flip

**Fresh prior work:** *Structure Size as Confounder in Uncertainty-Based Segmentation Quality Prediction*, MIDL/Lübeck 2024, https://www.mic.uni-luebeck.de/fileadmin/mic/publications/2024/246_Structure_Size_as_Confound.pdf — KNOWN: Dice-size dependence treated as confounder. *Sex-based Bias Inherent in the Dice Similarity Coefficient*, arXiv:2509.19778 — KNOWN: model-independent synthetic-error analysis quantifying DSC differences by structure size (0.03–0.06 for small structures at 1–3 mm error). *Do We Really Need Dice?*, arXiv:2104.08717 — KNOWN: region-size bias analysis. Metrics Reloaded (Nature Methods 2024) [not re-verified this session; flagged] owns metric-selection guidance.
**Harshest rejection:** "Dice-size pathology is quantified (2509.19778 gives the analytical curves), size-stratified reporting is already the recommendation of multiple 2024–2026 papers, and Metrics Reloaded governs metric choice. The multi-annotator angle adds LIDC/QUBIQ data to a settled point."
**Hidden assumptions:** (a) LIDC/QUBIQ re-verification (G's census left this PARTIAL); (b) MICCAI reviewers will see "annotator-vs-annotator Dice as the noise floor" as new rather than as Label-Convergence-for-medicine.
**Killer experiment:** the salvageable one: size-stratified *claims audit* — annotator-vs-annotator Dice per size bin as MDE, then audit published MICCAI segmentation deltas per size bin against it ("X% of small-structure improvements are sub-noise"). Analysis-only given LIDC/QUBIQ.
**Verdict: MUTATE.**
**Mutated one-liner:** *The size-stratified noise floor of medical segmentation claims: annotator-disagreement Dice as the minimum detectable effect, audited against published deltas.* (This makes it the MICCAI-facing sibling of 0302, not a standalone metric critique.)

### 8. W2-C-0057 — Missing annotations punish better detectors

**Fresh prior work:** COCO-ReM (above); PU detection, arXiv:2002.04672 [inherited]; MJ-COCO (adds missing labels at scale — the artifact now exists on both sides); 2508.06556.
**Harshest rejection:** "COCO-ReM showed sharper models were penalized by bad GT and rankings change; MJ-COCO quantifies added missing labels per class. The 'law' you fit is a synthetic-deletion curve whose real-world anchor points are already published."
**Hidden assumptions:** (a) synthetic random deletion mimics real missingness (real missing labels are salience-biased — small/occluded/background objects — so the uniform-deletion law may not transfer; must delete by a fitted salience model, not uniformly); (b) "better models" is one-dimensional (confidence calibration differences confound the differential effect).
**Killer experiment:** yes — controlled deletion at rates r with *two deletion processes* (uniform and salience-matched, fitted from ReM/MJ-COCO's recovered-label statistics), across ≥15 detectors spanning quality; report distortion-vs-quality slopes and the crossover where leaderboard order inverts. Cheap (inference + eval loops).
**Verdict: SURVIVE-IF-EXPERIMENT** (salience-matched deletion arm mandatory; uniform-only would be rejected as toy).

---

## PART 2 — Rigor/metrology family

### 9. W2-C-0302 — MDE power tables + claims re-analysis (hosts 0070/0065/0284)

**Fresh prior work:**
- *Adding Error Bars to Evals*, arXiv:2411.00640 — KNOWN: full statistical framework for benchmark comparisons including power analysis and **the inverted MDE formula at fixed N**; recommends paired analysis, clustered SEs.
- *Resolution Diagnostics for Paired LLM Evaluation*, arXiv:2605.30315 — KNOWN: MDE at current N, required-N, resolution ratio q=N/N*, applied to real leaderboards; flags displayed rankings as unresolved.
**Harshest rejection:** "Power tables for benchmarks exist — 2411.00640 derived them, 2605.30315 shipped the leaderboard re-analysis with prospective validation. You are porting a published protocol to COCO and changing the noise model."
**Hidden assumptions:** (a) detection's variance structure (correlated instances within images, AP's non-decomposability, seed variance entering through training not just sampling) genuinely requires new machinery, not a design-effect correction to the LLM formulas; (b) the 100-paper delta census is extractable (papers rarely report val-set AP for the exact checkpoint pairs); (c) S1: the bootstrap inputs require regenerating predictions for the model population — priced, fine.
**Killer experiment:** yes — the detection-specific part 2411.00640 cannot do: empirical MDE decomposition into {instance-sampling, image-sampling, seed, framework} components via nested bootstrap over G's zoo + a ≥5-seed training grid on 2 architectures, validated by a prospective prediction (train two fresh seeds, check the interval). Then the claims table.
**Verdict: MUTATE** (framing, not substance): *Resolution diagnostics for detection benchmarks: the variance components LLM-eval statistics cannot see, plus the claims audit.* Must cite 2411.00640/2605.30315 in paragraph one or the "power tables" pitch reads as parallel invention. S2 mitigated by leading with the reusable tables as infrastructure.

### 10. W2-C-0309 — IRT for detection benchmarks (hosts 0328)

**Fresh prior work:**
- *On Evaluation of Vision Datasets and Models using Human Competency Frameworks*, arXiv:2409.04041 — KNOWN: IRT on **91 vision models** (ImageNet): ability/difficulty/discriminability/guessing; overconfidence-vs-IRT deviations flag label errors; **10-image subsets rank 91 models at Kendall 0.85**.
- IRT for vision robustness with annotation-error detection via feasibility parameter (finds up to 40% of errors on CIFAR/ImageNet), OpenReview https://openreview.net/pdf?id=e8Eletuo1hk — KNOWN.
- tinyBenchmarks, arXiv:2402.14992 [inherited from D].
**Harshest rejection:** "IRT-for-vision-benchmarks exists with all three of your contributions — ability scores, misfit↔annotation-error auditing, and tiny ranking subsets — on 91 models (2409.04041). You changed the task from classification to detection."
**Hidden assumptions:** (a) the detection "item" is definable — per-instance TP/FN across models requires fixing a matching convention, and the IRT fit may be an artifact of that convention (must show fit stability across IoU thresholds/matching rules — this is genuinely new content but also a new failure mode); (b) S1: 30+ models × COCO val inference, priced; (c) misfit↔ReM cross-check assumes ReM is truth (see attack 4).
**Killer experiment:** yes — fit 2PL/3PL IRT to per-instance outcome matrices across ≥30 detectors under ≥3 matching conventions; pre-register that (i) misfit items enrich for ReM-corrected instances (quantified lift), (ii) the 1k short test preserves rank (r>0.95) on held-out models *including OVD models not in the fit population*. The held-out-family generalization is what makes it more than a port.
**Verdict: MUTATE** (positioning-forced): *What is an item in a detection benchmark? IRT over instance-outcome matrices, convention-stability, misfit↔annotation-error lift, and a 1k short test.* 2409.04041 in paragraph one. Absorbs 0328 as before.

### 11. W2-C-0136 — Seed variance vs published deltas (hosts B-0033 arm)

**Fresh prior work:** *Evaluating Variance in VQA Benchmarks*, arXiv:2508.02645 — KNOWN: training-seed/framework variance across 14 VQA benchmarks; variance-aware evaluation advocacy. *On the Extreme Variance of Certified Local Robustness Across Model Seeds*, arXiv:2601.13303 — KNOWN: seed stddev exceeds published robustness margins. Bouthillier MLSys 2021, Picard 2109.08203 [inherited from D]. No detection-specific seed-variance census found this session — the gap D identified still holds.
**Harshest rejection:** "A fourth 'seed variance exceeds published deltas' paper (after classification, AL, robustness, VQA) — the genre's marginal information is near zero; everyone already believes it. And your variance estimates at trainable scale (ResNet-50 class) don't license claims about the flagship models whose deltas you audit." (This is the exact argument H used to kill B-0033 — it applies to this idea's *extrapolation*, not its core.)
**Hidden assumptions:** (a) the published-delta census is a fair comparison population if variance is only measured on mid-scale pipelines — must restrict the audited claims to the same scale class, which shrinks the headline; (b) detection-specific variance sources (BN, loader order, NMS ties) are separable within budget; (c) ~40–60 training runs are fundable (bounded, but not "cheap").
**Killer experiment:** yes — ≥7 seeds × {Faster R-CNN, DINO-DETR, YOLO-class} × 2 schedules on COCO; variance decomposition; then audit *only same-scale published deltas* (pre-registered inclusion rule) against the measured distribution. Report the fraction of deltas within seed noise, by year.
**Verdict: SURVIVE-IF-EXPERIMENT** (scale-matched claims audit; the flagship-scale extrapolation must be explicitly disclaimed or the B-0033 kill argument applies here too).

### 12. W2-C-0311 — Metrology-grade uncertainty budget for COCO AP (hosts 0064/0042/0282)

**Fresh prior work:** Label Convergence + Noise-Aware Evaluation (the annotation-noise component is now published twice); 2411.00640 (sampling/paired components for LLM evals); Bouthillier 2021 [inherited]; VQA variance 2508.02645 (framework nondeterminism component, different task).
**Harshest rejection:** "An umbrella that composes other people's measurements: the noise band is Label Convergence's, the bootstrap axis is commodity, the seed component is 0136's, the framework component is a table. GUM-style formalism on top of borrowed numbers is packaging, not measurement science. Also: your own portfolio submits the components as separate papers (0136, 0302) — the umbrella double-counts them." (S2 at its sharpest; also the intra-portfolio cannibalism problem.)
**Hidden assumptions:** (a) components are independent enough for a combined budget (annotation noise interacts with IoU-threshold choice — the 0042 arm — so the budget needs cross terms nobody has estimated); (b) a combined interval is more useful to practitioners than the max of components (must be argued, not assumed).
**Killer experiment:** yes — the one thing composition cannot fake: an *empirical validation of the combined budget* — predict the AP spread of a replication ensemble (same method re-trained/re-evaluated under resampled conditions: seeds × frameworks × GT variants × bootstrap), then run the ensemble and show the predicted interval covers. A budget that predicts is metrology; one that doesn't is a spreadsheet.
**Verdict: SURVIVE-IF-EXPERIMENT** (the coverage-validation ensemble is mandatory; also requires a portfolio decision: either 0311 is the flagship and 0136/0302 fold in as sections, or 0311 is cut — submitting all three invites the double-counting rejection. Recommend the fold-in.)

### 13. W2-C-0283 — Stale baselines under papers' own budgets

**Fresh prior work:** Musgrave et al. ECCV 2020, arXiv:2003.08505 [inherited, re-confirmed]; Dacrema et al. RecSys 2019 [inherited]; **detrex**, arXiv:2306.07265 — KNOWN: re-tuning hyperparameters of DETR-family baselines yields +0.4 to +1.1 AP over original implementations — direct EVIDENCE that baseline decay ≥ typical claimed deltas in detection, published as a byproduct of a benchmarking codebase.
**Harshest rejection:** "The genre is famous (metric learning, recsys), and detection's own infrastructure papers (detrex) already show retuned baselines gain ~1 AP — your audit will confirm a number the community can already read off a GitHub README. Twenty retrainings of old baselines is a lot of compute for a foregone conclusion."
**Hidden assumptions:** (a) "papers' own tuning budgets" are recoverable from papers (they are mostly undisclosed — the audit must define a budget convention, which reviewers will attack as arbitrary); (b) per-paper re-implementations are faithful (the Musgrave critique cuts both ways: a sloppy audit is worse than none).
**Killer experiment:** yes — pre-registered selection of 12–20 method-vs-baseline pairs (2018–2025) with a *fixed, published budget protocol* (equal trials of a declared search space per side); headline = distribution of "claimed delta minus fair-budget delta" over time (the decay-rate model). detrex numbers cited as the motivating observation.
**Verdict: SURVIVE-IF-EXPERIMENT** (pre-registration + the decay-over-time model are the only things separating it from 'detrex, but slower'; if the compute partner does not materialize, cap it out — see AGENT_REPORT).

### 14. W2-C-0285 — Shadow tuning (budget-asymmetry manufactures SOTA)

**Fresh prior work:** NH-Fair, arXiv:2602.03895 — KNOWN: tuning-aware benchmark showing carefully tuned ERM rivals specialized fairness methods; explicit "fixing parameters across baselines yields biased comparisons" finding — the shadow-tuning thesis, executed in fairness. Musgrave (above). No detection instantiation found.
**Harshest rejection:** "This is 0283 with the budget knob turned the other way — the same audit family, same compute, same confounds; and NH-Fair just published the 'tuned baseline rivals the method' result in vision-adjacent territory. Also unfalsifiable in the direction you want: if the baseline fails to catch up, defenders say your search space was wrong."
**Hidden assumptions:** (a) the method's search budget is knowable (papers under-report; must be estimated, attackable); (b) search-space choice for the baseline is neutral (it never is — pre-registration is the only defense, as D said).
**Killer experiment:** yes — pre-registered: pick 6–8 recent SOTA claims with disclosed ablation counts; give the *baseline* exactly that trial count over a pre-declared space; report delta shrinkage with CIs. Bounded to 6–8 pairs to stay fundable.
**Verdict: SURVIVE-IF-EXPERIMENT** (pre-registration filed before any run; merge consideration: 0283+0285 are one paper to any reviewer — recommend running as one pre-registered audit with two budget conventions, freeing a slot).

### 15. W2-C-0287 — Ablation sign-flip rates under reseeding

**Fresh prior work:** 2601.13303 (certified robustness: seed stddev > published margins — the nearest published sign-flip-style result); VQA variance 2508.02645; no detection ablation-reseeding study found.
**Harshest rejection:** "A corollary of 0136: if seed variance ~ delta size, ablation sign flips follow arithmetically. You're spending a grid of retrainings to confirm an implication of your own companion paper."
**Hidden assumptions:** (a) published ablations are re-runnable (configs incomplete); (b) sign-flip rate is the right statistic (a flip on a 0.1-AP component is noise, not news — must weight by claimed importance); (c) bounded compute holds only if components are cheap (many ablations require full re-training).
**Killer experiment:** yes — 5 seeds × 10 published ablation tables (pre-registered selection, components re-run in original codebases); report P(sign flip | claimed delta size) — the *curve*, not the anecdote count. The curve is the reusable artifact 0136 doesn't produce.
**Verdict: SURVIVE-IF-EXPERIMENT** (must be co-planned with 0136 to share the seed grid; standalone it fails the S2 cost-benefit test).

### 16. W2-C-0327 — 2015 architecture + 2026 recipe

**Fresh prior work (searched this session — direct hit):**
- **torchvision `fasterrcnn_resnet50_fpn_v2`**, PR https://github.com/pytorch/vision/pull/5763 — KNOWN: modern recipe + minor head/FPN changes on the 2015 Faster R-CNN yields **37.0 → 46.7 AP (+9.7)** on COCO, shipped in torchvision 1.12 (2022), following *Benchmarking Detection Transfer Learning with Vision Transformers*, arXiv:2111.11429.
- RetinaNet v2 +5.1, Mask R-CNN v2 +9.5/+7.2 (same release, https://pytorch.org/blog/pytorch-1-12-new-library-releases/).
**Harshest rejection:** "The headline number exists in the torchvision model zoo since 2022: a 2015 architecture with a modernized recipe gains ~10 AP. Everyone who calls `fasterrcnn_resnet50_fpn_v2(weights='DEFAULT')` already knows your conclusion."
**Hidden assumptions:** (a) that nobody has itemized the recipe — true, the torchvision PR bundles recipe + small architectural edits (heavier RPN/heads, no FrozenBN), so the *attribution* between recipe and architecture is genuinely unresolved; (b) "matched compute vs modern architecture" comparisons are fundable (400-epoch schedules — the v2 recipe — are expensive).
**Killer experiment:** yes — the decomposition torchvision didn't do: factorized recipe ladder (schedule length, LSJ augmentation, init provenance, BN policy, head capacity) on the frozen 2015 architecture + matched-compute modern architecture reference, yielding "X of the 10 AP is recipe, Y is architecture, per component." Expensive but bounded (~15 training runs).
**Verdict: MUTATE.**
**Mutated one-liner:** *Decomposing the decade: itemized attribution of Faster R-CNN's +10 AP recipe gain, against a compute-matched modern reference.* The demonstration is dead; the decomposition and the field-level attribution number survive.

### 17. W2-C-0298 — Hash-audit of circulating benchmark variants

**Fresh prior work:** no direct competitor found this session. Nearest: D-LeDe (attack 22, integrity-adjacent); MM-Detect (contamination, different question).
**Harshest rejection:** "Expected outcome: all mirrors identical; a null result with no consequence. Even a positive (variant annotation files circulating) is a blog post unless you show it moved published numbers."
**Hidden assumptions:** (a) mirrors are enumerable (HF, Kaggle, academic torrents, framework auto-downloads — tractable); (b) a found variant is attributable to specific papers (almost never provable — the consequential claim is out of reach).
**Killer experiment:** partial — hash census + *if* variants found, re-evaluate 5 public models on variant-vs-canonical annotations to bound the AP impact. The consequence arm is the difference between forensics and trivia; but its precondition (variants exist) is outside the author's control.
**Verdict: SURVIVE-IF-EXPERIMENT** — strictly as a protected cheap long-shot *executed as a side audit inside 0122's leakage program, not as a portfolio slot* (see AGENT_REPORT cap list). The verdict is conditional on the consequence arm being pre-planned.

---

## PART 3 — Leaderboard-integrity / re-analysis family

### 18. W2-C-0260 — Benchmark monoculture (cross-dataset rank study)

**Fresh prior work:** Battle of the Backbones, arXiv:2310.19909 [inherited, cross-task ρ>0.8]; **COCO-O**, arXiv:2307.12730 — KNOWN: 100+ detectors, "are improvements credible or overfitting to COCO test set", natural-shift版; CD-FSOD arXiv:2210.05311 + NTIRE 2025 challenge (https://github.com/lovelyqian/NTIRE2025_CDFSOD) — KNOWN: COCO-source cross-domain transfer rankings; COUNTS CVPR 2025 (OOD benchmark, https://openaccess.thecvf.com/content/CVPR2025/html/Li_COUNTS_Benchmarking_Object_Detectors_and_Multimodal_Large_Language_Models_under_CVPR_2025_paper.html); COCO Generalization Benchmark inside arXiv:2506.21042 (11 target datasets).
**Harshest rejection:** "Between COCO-O (100+ detectors, credibility question asked verbatim), BoB (cross-task rank correlations), COUNTS, and the CD-FSOD line, the 'does COCO rank transfer' question has been answered from four directions: mostly yes within distribution, decreasingly under shift. A fifth correlation table is reviewer fatigue."
**Hidden assumptions:** (a) that in-distribution *within-task* cross-dataset rank transfer of standard (closed-vocab) detectors — the one cell those four papers don't cover — is where interesting inversions live (untested; may be as boring as ρ>0.9); (b) S1: needs retrained heads per dataset for closed-vocab models (not just inference) — costlier than G's repricing assumed; the "reusable audit harness" is a real engineering artifact but S2 says harnesses aren't papers.
**Killer experiment:** yes, but must be the stratified version: 15 modern detectors × 8–10 detection datasets (fine-tuned per dataset under a fixed protocol), reporting rank correlation *stratified by size/density/domain distance* and the specific published-claim inversions ("method A>B on COCO reverses on 4/9 datasets"). The inversion census, not the aggregate ρ, is the paper.
**Verdict: SURVIVE-IF-EXPERIMENT** (inversion-census framing; mandatory positioning vs COCO-O/BoB/COUNTS; if aggregate ρ comes back >0.9 with no notable inversions, the paper must be pre-committed to publishing the null with the harness).

### 19. W2-C-0276 — Tail-progress illusion (hosts 0255)  &  20. W2-C-0256 — Size-frequency confound (hosts 0261)

(Attacked jointly; same artifact dependence, same rejection surface.)
**Fresh prior work:** Dave et al., arXiv:2102.01066 [inherited, re-verified this session] — KNOWN: +2.9 AP-rare from a ranking-policy change alone, "roughly the magnitude of a typical CVPR method"; AP-Fixed/AP-Pool proposed. LVIS paper (per-category AP withheld as unstable). SimLTD CVPR 2025 and the 2024–2026 long-tail method stream (arXiv:2401.15885, 2310.12152, 2511.16619) still report APr as headline — EVIDENCE the audit remains needed *and* that per-class predictions of these methods are not routinely released (S1 bites hard: G's census downgraded exactly this family; MMDetection ships only Seesaw±RFS).
**Harshest rejection (0276):** "Dave et al. told the field five years ago that AP-rare gains can be evaluation artifacts and gave corrected metrics; the field ignored it. Your per-class decomposition of methods you had to *retrain yourself* (because checkpoints don't exist) shows... that reimplementations differ. Every surprising finding will be attributed to your reimplementation, not the method."
**Harshest rejection (0256):** "Size and frequency are correlated in LVIS — known from the dataset paper's own statistics; a decorrelation analysis is a weekend of pandas on per-class tables that papers don't publish, so you retrain, and the reimplementation objection above applies."
**Hidden assumptions (both):** (a) retrain-fallback fidelity — the entire evidentiary weight rests on faithful reproductions of ~8 methods (G's fallback priced this as 'bounded' but the *credibility* cost was not priced); (b) per-class AP at LVIS-rare sample sizes is meaningful at all (LVIS's own authors say it isn't — the analysis must be bootstrap-banded per class, which will erase many "concentrated gains" findings into noise).
**Killer experiment:** yes, shared — retrain 6–8 long-tail methods in ONE codebase (MMDetection) under authors' configs, release per-class predictions as the artifact (fixing S1 for everyone downstream), and report: (i) per-class delta concentration (Gini/top-k share) with bootstrap bands [0276], (ii) frequency-vs-size partial-effect decomposition [0256], (iii) the 0255 head-class-utility arm. One paper, not two.
**Verdict (both): SURVIVE-IF-EXPERIMENT** — *as a single merged paper with the prediction-release artifact as the S2 shield*. Two separate slots would be killed for salami-slicing; recommend the PI convert 0256 to an arm of 0276 (stronger host), freeing one slot.

### 21. W2-C-0279 — Exposure vs rarity (hosts 0001/0020)

**Fresh prior work:** *No "Zero-Shot" Without Exponential Data*, Udandarao et al., arXiv:2404.04125 — KNOWN (re-verified): 34 models, 5 pretraining corpora, log-linear concept-frequency→zero-shot-performance law, "Let it Wag!" long-tail benchmark; their frequency pipeline already uses an open-set tagger over pretraining *images*, not just captions.
**Harshest rejection:** "Udandarao et al. established the exposure law across 34 multimodal models including retrieval; running RAM++ over Grounding DINO's pretraining mix and regressing APr on frequency is their pipeline pointed at a new task head. The 'invented names' causal arm is the only piece they don't have — and it's one figure."
**Hidden assumptions:** (a) OVD pretraining corpora are enumerable (Grounding DINO's mix — O365, GoldG, Cap4M — is public in composition but not fully downloadable at counting scale; the frequency estimates will carry corpus-reconstruction error the reviewer will attack); (b) exposure explains *detection-specific* failure (localization of rare classes) beyond classification-style recognition — the interesting deviation from Udandarao's law, currently HYPOTHESIS.
**Killer experiment:** yes — the residual test: regress LVIS-rare per-class AP on estimated exposure; the paper lives in the *residual structure* (which rare classes beat/undershoot their exposure prediction, and does localization error, not classification error, explain the gap) + the invented-names intervention arm (classes with zero possible exposure). Inference-only.
**Verdict: SURVIVE-IF-EXPERIMENT** (residual-structure framing; Udandarao paragraph-one; urgent — this is a fast lane).

### 22. W2-C-0122 — Train-test duplication census (hosts 0264)

**Fresh prior work (direct hit):** *D-LeDe: A Data Leakage Detection Method for Automotive Perception Systems*, 2025, https://www.scitepress.org/Papers/2025/134767/134767.pdf — KNOWN: pHash-based train-test near-duplicate audit for OD datasets; **KITTI: 851 exact-hash pairs, >27,000 pairs at pHash distance ≤10**; follow-up robustness study (SN Computer Science 2026, https://link.springer.com/article/10.1007/s42979-026-05289-7) extends to SODA10M with duplicate-removal ablations.
**Harshest rejection:** "D-LeDe published the method AND the scandal number (KITTI's 27k near-duplicate pairs) in 2025, with a 2026 follow-up. Your census extends the table to COCO/VOC/LVIS — incremental dataset coverage of a published audit."
**Hidden assumptions:** (a) COCO/LVIS have nontrivial duplication (unlike KITTI's video frames, COCO was curated from distinct Flickr photos — the expected answer is 'little', a null; the tail-duplicate arm (0264) is where non-null findings plausibly live); (b) per-image causal check (does removing dupes change AP?) needs retraining — priced beyond "cheapest in portfolio."
**Killer experiment:** yes — the arms D-LeDe lacks: (i) LVIS-rare duplicate concentration (0264 arm: are rare-class instances duplicated across train/test at higher rates? directly attacks APr credibility), (ii) AP inflation bound via test-side dedup re-scoring (no retraining needed), (iii) cross-*benchmark* duplication (COCO-val images inside other benchmarks' train sets — feeds 0345).
**Verdict: MUTATE.**
**Mutated one-liner:** *Duplication where it hurts: tail-duplicate concentration and cross-benchmark leakage in detection evaluation* (D-LeDe cited as the method precedent; generic census demoted to an appendix).

### 23. W2-C-0345 — Foundation-model detection advantage as test-set exposure

**Fresh prior work:** MM-Detect, https://github.com/MLLM-Data-Contamination/MM-Detect (EMNLP 2025 Findings) — KNOWN: multimodal contamination detection framework covering COCO-Caption among benchmarks; benchleak (PyPI) — KNOWN: LLM contamination detectors productized; D-LeDe (above). No audit found that measures COCO/LVIS *val-image* presence in OVD/foundation-detector pretraining corpora and links it to per-image performance.
**Harshest rejection:** "Contamination auditing is industrialized (MM-Detect, benchleak); OVD papers already claim to dedup their pretraining data against benchmarks; and your effect estimate is confounded — foundation detectors are better on benchmark-like images for a hundred reasons besides having seen them."
**Hidden assumptions:** (a) access to pretraining corpora at matching scale (only partially public — Cap4M etc.; incomplete corpora bias exposure estimates downward, which actually helps a lower-bound claim); (b) the per-image exposure→performance link needs a matched-pair design (exposed vs unexposed images matched on difficulty), or it's correlational.
**Killer experiment:** yes — matched-pair contrast: find near-duplicates of val images inside public OVD pretraining corpora (pHash + embedding), match each exposed val image to unexposed val images by difficulty covariates, compare per-image detection quality; plus the H-mandated placebo/injection calibration (deliberately inject known val images into a small fine-tune to calibrate the detector-of-exposure's sensitivity). Two-quarter clock — same urgency class as H's B-0268 verdict.
**Verdict: SURVIVE-IF-EXPERIMENT** (matched-pair + injection calibration mandatory; execute early or drop — this front industrializes fast).

### 24. W2-C-0011 — Prompt variance vs architecture deltas (hosts B-0042 residual)

**Fresh prior work (re-searched as mandated):** arXiv:2604.17126 — KNOWN (re-verified): prompt instability in DETR+CLIP grounding, 263 images, structured variability; OV3D-Bench arXiv:2608.17110 — KNOWN: CV% across 15 templates for OV *3D* detection, overdetailed prompts hurt all encoders; **TG-OverLoCK, Sci Rep 2026** (https://www.nature.com/articles/s41598-026-50117-w) — KNOWN: a *method paper* now routinely reporting mean±std LVIS AP across 4 templates and worst-case template drop — EVIDENCE the field is beginning to routinize template-variance reporting.
**Harshest rejection:** "Prompt sensitivity is documented (2604.17126), benchmarked in 3D (OV3D-Bench), and method papers have started reporting template robustness tables (TG-OverLoCK). By the time this is reviewed, template-std reporting may be standard practice and your leaderboard comparison will describe last year's sins."
**Hidden assumptions:** (a) template variance on OV-COCO/OV-LVIS 2D leaderboards is of the same order as published architecture deltas (plausible from OV3D-Bench's 3D numbers, but 2D magnitudes are unmeasured — the paper's entire value is this one number); (b) the method population's *official* prompts are recoverable (they are, from repos).
**Killer experiment:** yes — 10–15 OVD checkpoints × ~30 defensible template/synonym sets on OV-COCO + OV-LVIS; report the induced AP-novel spread against the distribution of published pairwise deltas, plus rank-inversion counts under template resampling. Inference-only; two GPU-weeks.
**Verdict: SURVIVE-IF-EXPERIMENT** (unchanged core, hard two-quarter execution clock; the B-0042 synonym residual folds in as one axis of the template grid).

### 25. W2-C-0150 — UDA reckoning (hosts 0221)

**Fresh prior work (direct hits):** *Large Self-Supervised Models Bridge the Gap in DAOD*, arXiv:2503.23220 — KNOWN: states "the current Mean Teacher paradigm for DAOD is outdated," uses VFMs as label sources; *Revisiting Few-Shot Object Detection with VLMs*, arXiv:2312.14494 — KNOWN: GroundingDINO zero-shot beats FSOD SOTA 48.3 vs 33.1 AP; Foundational FSOD benchmark proposed; VG-DETR, arXiv:2508.11167 — KNOWN: 1% labeled target data + VFM guidance in source-free detection, with a leaderboard.
**Harshest rejection:** "The field is already retiring itself: DAOD papers now open by calling Mean Teacher outdated, and the few-labels-beat-UDA observation is the founding premise of Foundational FSOD (2023) and the VFM-guided semi-supervised line. Your kill-shot fires at a corpse."
**Hidden assumptions:** (a) that no one has stated the *budget equivalence* ("method X = N labeled images") — true as a quantitative instrument, but the qualitative conclusion is community property; (b) 50 labeled images is the right unit (labeling cost varies wildly by density).
**Killer experiment:** the surviving one — the exchange-rate curve: for each of 6–8 published UDA methods on standard benchmark pairs, find N* = labeled-target-images needed for plain fine-tuning (2025 backbone and 2019 backbone) to match it; publish the N* table as the decision instrument, with annotation-cost (boxes, not images) on the x-axis.
**Verdict: MUTATE.**
**Mutated one-liner:** *The exchange rate of adaptation: how many labeled target boxes buys each published UDA-for-detection method, under old and new backbones.* (Instrument survives; "reckoning" framing dead — mandatory citations 2503.23220 / 2312.14494.)

### 26. W2-C-0159 — Detection AL replication at realistic batch sizes

**Fresh prior work:** ALBench, arXiv:2207.13339 — KNOWN: AL-for-detection benchmark platform motivated by "random performs similarly" and "contradictory conclusions across setups"; *Box-Level Class-Balanced Sampling*, arXiv:2508.17849 — KNOWN: shows SOTA image-level AL methods **fail to beat random when cost is measured in boxes**; *Streamlining AL in Real-World OD*, arXiv:2508.19906 — KNOWN: AL rankings flip across validation sets (τ from −0.6 to 1.0); *Evaluating Zero-cost AL*, arXiv:2212.04211 — KNOWN: pretrained-weight provenance flips AL-vs-random conclusions.
**Harshest rejection:** "The indictment already exists in pieces: a benchmark platform built because conclusions contradict (ALBench), a published can't-beat-random-under-box-cost result (2508.17849), and ranking instability across val sets (2508.19906). A replication study assembles known shrapnel."
**Hidden assumptions:** (a) that no one has run the *systematic multi-method multi-codebase* version with honest random baselines (true — the pieces are anecdotal, Lüth-style systematics remain classification-only); (b) "realistic batch sizes" is definable (needs an industry-anchored survey arm, or the choice is attacked as arbitrary).
**Killer experiment:** yes — Lüth-et-al.-for-detection: 6–8 published detection-AL methods × 2 codebases × box-cost accounting × tuned-random baselines × ≥5 seeds, batch sizes from paper-typical to deployment-typical; pre-registered. Expensive but bounded; the WACV/NeurIPS-D&B slot for it demonstrably exists (classification precedent).
**Verdict: SURVIVE-IF-EXPERIMENT** (box-cost + tuned-random arms mandatory; ALBench/2508.17849 in paragraph one).

---

## PART 4 — Mechanism / probe / method-adjacent ideas

### 27. W2-C-0306 — Conformal coverage destroyed by NMS (+ coverage-preserving suppression)

**Fresh prior work (mandated re-search):** SeqCRC, arXiv:2505.24038 (v2 current) — KNOWN (re-verified): defines COD, calibrates *after* NMS, treats NMS as part of the model; *Probabilistic OD with CP*, arXiv:2605.07549 [inherited from D, not re-retrieved this session — flagged]; **new adjacent hit:** *Do We Still Need NMS? IoU-Aware Calibration*, WACV 2024, https://doi.org/10.1109/wacv57701.2024.00478 — KNOWN: replaces NMS with a calibration that "implicitly accounts for the likelihood of each detection being a duplicate" — a suppression-free pipeline that a reviewer will call the practical answer to coverage destruction.
**Harshest rejection:** "Two conformal-OD papers give guarantees despite NMS, and IoU-aware calibration removes NMS entirely — so the step you attack is either already handled downstream (SeqCRC) or deletable (WACV 2024). Who needs coverage-preserving *suppression*?"
**Hidden assumptions:** (a) that post-NMS guarantees are practically vacuous for suppressed objects (true formally — SeqCRC's guarantee conditions on the post-NMS list — but the *magnitude* of destroyed coverage is unmeasured; if it's 1%, the paper is a footnote); (b) that a coverage-aware suppression rule can beat "no suppression + calibration" (WACV 2024) on the coverage/set-size frontier — now the mandatory comparison.
**Killer experiment:** yes — first measure the blind spot: fraction of GT objects whose only covering candidates are suppressed by standard NMS, across detectors/thresholds/crowdedness (cheap, decisive — if large, everything downstream matters); then the method: suppression rule with provable candidate-set coverage, evaluated against SeqCRC-post-NMS AND IoU-aware-calibration-no-NMS on the risk/set-size frontier.
**Verdict: SURVIVE-IF-EXPERIMENT** (the blind-spot magnitude measurement is the gate; WACV 2024 baseline mandatory; urgency confirmed — third conformal-OD paper likely within months).

### 28. W2-C-0158 — NMS as calibration destroyer (winner's curse)

**Fresh prior work (direct hits):** *Do We Still Need NMS? IoU-Aware Calibration*, WACV 2024 (above) — KNOWN: frames classic NMS as producing "biased confidence estimates" and builds the fix; *Systematic Evaluation of Uncertainty Calibration in Pretrained Object Detectors*, IJCV 2024, https://link.springer.com/article/10.1007/s11263-024-02219-z — KNOWN: explicitly evaluates calibration on raw pre-NMS outputs vs post-processed pipelines and warns that post-processing "might bias the evaluation, especially when evaluating uncertainties"; Küppers et al. 2020/2022 [inherited].
**Harshest rejection:** "WACV 2024 already says NMS biases confidences and ships the replacement; IJCV 2024 already benchmarks pre-vs-post-NMS calibration. Your 'nobody isolates NMS as the calibration destroyer' framing was true in 2023."
**Hidden assumptions:** (a) the *mechanism* (survivor selection = winner's curse, formalizable as a selection-bias estimator) still adds explanatory content beyond the two 2024 papers (yes, marginally: neither derives the selection-bias form or predicts miscalibration magnitude from candidate-cluster statistics); (b) pre-NMS scores are accessible (yes, code-level, per G).
**Killer experiment:** yes — the theory-plus-validation version only: derive expected post-NMS overconfidence under a winner's-curse selection model from candidate-cluster size/correlation; verify the predicted miscalibration curve across detectors/NMS variants (soft-NMS, class-agnostic); show the correction implied by the theory matches or beats IoU-aware calibration where it applies.
**Verdict: MUTATE.**
**Mutated one-liner:** *The winner's curse in detection confidences: a selection-bias theory of post-NMS miscalibration, with predictions the 2024 empirical papers can't make.* (Empirical demonstration alone is dead; only the predictive mechanism survives.)

### 29. W2-C-0308 — Machine psychophysics staircases for detectors

**Fresh prior work:** adaptive-staircase methodology is mature and moving (NEST, Vision Research 2025, https://doi.org/10.1016/j.visres.2025.108710; QUEST+ line; AEPsych arXiv:2104.09549) — all *for human observers*. No paper found this session applying adaptive staircases to measure detector psychometric thresholds (contrast/size/occlusion) as a benchmark alternative.
**Harshest rejection:** "Models aren't observers with trial budgets — you can evaluate on every stimulus level, so adaptive staircases solve a problem detectors don't have. Full psychometric curves via grid sweep are trivial; the transplant is methodological cosplay."
**Hidden assumptions:** (a) the stimulus dimensions are the right ones and synthetic degradations produce thresholds predictive of natural-image failure (the entire external validity of the instrument — must be shown, or it's a toy); (b) thresholds add information beyond AP-by-stratum curves the benchmark already yields.
**Killer experiment:** yes — the validity gate: measure detector thresholds (size, contrast, occlusion) via staircases on controlled stimuli; show they (i) predict per-stratum benchmark AP better than model-family/AP-overall baselines, and (ii) dissociate models with equal COCO AP. If thresholds don't out-predict cheap baselines, the instrument dies honestly — the reviewer objection ("grid sweep suffices") is answered by *cost per bit* only in large stimulus spaces, so the design must use a high-dimensional stimulus space where grids are infeasible (occlusion×size×contrast×clutter jointly) — this is where staircases genuinely pay.
**Verdict: SURVIVE-IF-EXPERIMENT** (high-dimensional joint-threshold design + predictive-validity gate; low collision risk, high construct risk).

### 30. W2-C-0135 — Co-occurrence overrides appearance

**Fresh prior work:** Elephant in the Room, arXiv:1808.03305 [inherited]; *Quantifying Context Bias in DAOD*, arXiv:2409.14679 — KNOWN: FG-BG association quantification; *Mitigating Context Bias with Mask Pooling*, arXiv:2505.18446 — KNOWN: causal (SCM/intervention) treatment of context bias, random-background stress benchmark; *Zero-Shot Detection of Out-of-Context Objects*, WACV 2025 — KNOWN: OOC detection with FMs; UFR CVPR 2024, arXiv:2405.15225 (SCM for detection bias).
**Harshest rejection:** "Context reliance in detectors is a 2018 result now with its own causal-intervention literature (Mask Pooling line, UFR) and an OOC-detection subfield. 'Keyboard fires beside monitor-shaped blobs' is a demo of a mechanism that has been quantified, modeled with SCMs, and mitigated."
**Hidden assumptions:** (a) the *arbitration curve* (at what appearance-degradation level does context take over, per class) is genuinely absent from that literature (it is — existing work measures average context effects, not the appearance-context tradeoff function); (b) synthetic blob/degradation stimuli don't introduce their own artifacts (needs matched-degradation controls à la D's 0116 verdict).
**Killer experiment:** yes — psychometric arbitration curves: parametrically degrade object appearance (morph to blob) in-context vs out-of-context; per-class curves of P(detected) vs appearance evidence × context strength; validate context-strength axis against training-set co-occurrence statistics. Naturally shares machinery with 0308 — run as one program.
**Verdict: SURVIVE-IF-EXPERIMENT** (arbitration-curve design with degradation controls; position against Mask Pooling/2409.14679 as "they measure that context matters; we measure when it wins").

### 31. W2-C-0341 — Batch cross-talk exploit

**Fresh prior work (direct hits):** *Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference*, NeurIPS 2025 / arXiv:2506.09501 — KNOWN: batch composition changes outputs via kernel selection and FP non-associativity; the Thinking Machines batch-invariance study and batch-invariant kernels — KNOWN (cited within 2506.09501 and arXiv:2511.00025); TBIK arXiv:2511.17826, CoRun arXiv:2608.14376 — KNOWN: determinism engineering now a subfield.
**Harshest rejection:** "Batch-composition dependence is a fully explained numerical phenomenon with a 2025–2026 engineering literature and shipped fixes (batch-invariant kernels). For detectors, either your cross-talk is this known FP/kernel effect (a port of a solved diagnosis) or it's a misconfigured BatchNorm in eval mode (a bug report). An 'exploit' needs an information channel; FP noise carries ~no adversary-controllable signal, and you present no mechanism by which batchmate *content* steers another image's detections in a correctly configured pipeline."
**Hidden assumptions:** (a) a content-dependent channel exists in correctly-configured detectors — no mechanism identified beyond test-time BN (a configuration error) and FP noise (content-independent for practical purposes); (b) deployment systems batch heterogeneous users' images through shared BN-style statistics (modern serving does not).
**Killer experiment:** NONE that rescues the exploit claim. The only honest outcomes are (i) "effect is FP-noise-sized" — a footnote to 2506.09501; (ii) "effect is large because BN was left in train mode" — a bug report; (iii) a genuine content channel — no candidate mechanism exists to pre-register.
**Verdict: KILL** (freshness + mechanism kill; the determinism literature owns the phenomenon and the fix). Residual: a one-paragraph batch-sensitivity check belongs inside the FLEX determinism audit C-0290, not in any slot.

### 32. W2-C-0226 — GT-controlled SR accounting (hosts 0248/0231)

**Fresh prior work (mandated re-search):** Task-driven SR arXiv:1803.11316, FDSR arXiv:2004.00554 [both re-verified] — SR-helps-detection genre, no HR-GT hallucination accounting; **Hallucination Score for generative SR**, arXiv:2507.14367 — KNOWN: MLLM-based hallucination measurement for GSR, hallucination framed as orthogonal to fidelity/quality, plus mitigation via reward fine-tuning.
**Harshest rejection:** "Hallucination in generative SR is now measured (HS, 2507.14367) and mitigated; the SR-for-detection literature already knows PSNR doesn't predict detection utility (FDSR). Your decomposition is HS with AP instead of MLLM judgments."
**Hidden assumptions:** (a) the *detection-metric* accounting (which AP gains come from detections unsupported by the true HR image) is distinct from perceptual hallucination scoring — true, HS never touches detection metrics or GT-controlled downsampling, but the reviewer will demand the HS comparison; (b) downsample→SR→detect protocols represent real LR deployment (synthetic downsampling ≠ real degradation — a known objection; needs one real-LR arm, e.g., paired zoom imagery).
**Killer experiment:** yes — the protocol as designed (HR GT, downsample, SR back, score against HR GT; decompose ΔAP into recovered-vs-hallucinated by checking support in the true HR image), with (i) classical-vs-generative SR contrast, (ii) HS correlation arm, (iii) one real-LR validation arm.
**Verdict: SURVIVE-IF-EXPERIMENT** (real-LR arm + HS positioning now mandatory; the detection accounting remains unclaimed — confirmed this session).

### 33. W2-C-0193 — Threshold drift under mild shift

**Fresh prior work:** D3M, arXiv:2506.05047 — KNOWN: label-free deployment deterioration monitoring; *Monitoring Risks in TTA*, arXiv:2507.08721 — KNOWN: sequential risk monitoring; Podkopaev & Ramdas line cited therein. None isolates the *fixed-confidence-threshold operating-point drift* of detectors as the object of study.
**Harshest rejection:** "Deployment monitoring is a maturing field with statistical guarantees (D3M, sequential testing); 'thresholds go stale under shift' is the folk knowledge that motivates that entire field. A descriptive drift study without a monitoring/correction contribution is the related-work section of those papers."
**Hidden assumptions:** (a) precision/recall at fixed threshold decays much faster than AP under mild shift (plausible, unmeasured — the paper's one number); (b) "mild shift" is definable and reproducible (needs a shift ladder: compression, ISP, time-of-day, sensor swap).
**Killer experiment:** yes — the decoupling measurement: across a shift ladder × 10 detectors, plot ΔAP vs Δ(precision@fixed-τ); headline = regimes where AP moves <1 point while deployed precision collapses >10 points; plus a label-free threshold-recalibration baseline (using D3M-style signals) to show the failure is cheaply correctable — which converts the descriptive study into an actionable one.
**Verdict: SURVIVE-IF-EXPERIMENT** (decoupling-curve design + recalibration arm; position as the detection-specific gap in the monitoring literature).

### 34. W2-C-0321 — Behavioral contracts for detector updates

**Fresh prior work:** negative-flip literature — *Regression Bugs Are In Your Model!*, arXiv:2105.03048 (NLP), MUSCLE arXiv:2407.09435 (LLM updates, −40% negative flips), FlipGuard arXiv:2410.00508; positive-congruent training (Yan et al. 2021, vision classification — cited inside MUSCLE) [not independently re-verified this session — flagged]. No detection-specific negative-flip/contract study found.
**Harshest rejection:** "Backward-compatibility and negative flips are established (classification, NLP, LLMs) with mitigation methods; 'contracts' is a rebranding of regression test suites, and D&B reviewers will ask for the method contribution your audit lacks."
**Hidden assumptions:** (a) detection negative flips are structurally different (plausibly yes: a flip can be a localization regression at equal AP — classification metrics can't see this; this is the idea's real wedge); (b) practitioners will adopt contract suites without a standard body (adoption risk irrelevant to acceptance but relevant to impact claims).
**Killer experiment:** yes — measure instance-level negative-flip rates across public detector version ladders (YOLOv5→v8→v11, torchvision v1→v2, MMDet upgrades) at matched or improved AP; taxonomy of flip types (lost detection, class swap, localization regression, confidence collapse at fixed τ — ties to 0193); ship the contract test-suite artifact + one mitigation baseline (Yan-style positive-congruent distillation ported to detection).
**Verdict: SURVIVE-IF-EXPERIMENT** (the mitigation baseline arm is what buys it a venue beyond D&B; without it, MUTATE into 0193's deployment paper).

### 35. W2-C-0303 — Tuning-on-benchmark generalization tax

**Fresh prior work:** *Do ImageNet Classifiers Generalize to ImageNet?*, arXiv:1902.10811 — KNOWN (re-verified): the canonical adaptive-overfitting study found **no evidence of adaptivity-driven overfitting** on CIFAR/ImageNet — gains on old test sets translated to *larger* gains on new ones; COCO-O arXiv:2307.12730 — KNOWN: robustness-vs-COCO-progress correlations measured for 100+ detectors (their "credibility" analysis is a version of this idea's question under shift).
**Harshest rejection:** "The best-executed study of this question (Recht et al.) found the opposite sign for classification, and COCO-O already ran the shift version for 100+ detectors. Your observational design — regressing generalization gaps on disclosed tuning intensity — is confounded by era, method family, compute, and the fact that disclosed budgets are fiction. D flagged the confounds and protected it anyway; as a submitted paper it has no defensible identification strategy."
**Hidden assumptions:** (a) disclosed tuning budgets carry signal (they don't — selective disclosure is itself correlated with method culture); (b) a "simplicity dividend" is separable from age-of-method (older = simpler = more externally validated — perfectly collinear).
**Killer experiment:** NONE affordable. The clean design (randomize tuning budgets across matched methods, measure OOD gap) is a huge training study nobody will fund for an expected null (per Recht/COCO-O base rates); every observational version dies to confounding at review.
**Verdict: KILL** (methodological kill by H's B-0033/B-0252 standard: the affordable version cannot license the claim, the fundable-in-principle version has a strong published null prior). Residual: COCO-O citation belongs in 0260's related work.

### 36. W2-C-0119 — Rank stability under benign transforms predicts AP

**Fresh prior work (direct hit):** **PCR — Automated Model Evaluation for OD via Prediction Consistency and Reliability, ICCV 2025 ORAL**, arXiv:2508.12082, code https://github.com/YonseiML/autoeval-det — KNOWN: label-free mAP estimation for detectors from pre/post-NMS box consistency + confidence reliability, with a corruption meta-dataset, beating prior AutoEval methods *including* the earlier bounding-box-stability-under-perturbation method (Yang et al., MC-dropout perturbations) which is itself this idea's mechanism.
**Harshest rejection:** "AutoEval-for-detection is an ICCV 2025 oral; your transform-stability signal is the weaker cousin of the perturbation-stability baseline PCR already beats. This submission is a new entry in an established benchmark table, and not the leading one."
**Hidden assumptions:** none rescue it — the target quantity (label-free AP), the evaluation protocol (corruption meta-datasets), and the family of stability signals are all published, with a leaderboard.
**Killer experiment:** NONE that changes the verdict — beating PCR by a margin would be a method-increment paper, exactly what batch C exists to avoid.
**Verdict: KILL** (freshness kill; the census-flagged "regenerate predictions" cost is moot).

### 37. W2-C-0055 — Fresh i.i.d. COCO test set

**Fresh prior work:** ImageNetV2/Recht et al. (above) — KNOWN: the genre's flagship found **no adaptive overfitting**, and reports that replicating a test-set distribution is "astonishingly hard"; COCO-O — KNOWN: the shifted version exists with 100+ detectors and already concludes much detector progress is COCO-specific.
**Harshest rejection:** "A six-figure annotation project whose most probable outcome — per the best precedent — is 'no adaptive overfitting, but we can't fully rule out distribution mismatch,' i.e., the Recht et al. ambiguity reproduced at higher cost in a harder-to-replicate collection pipeline (2014 Flickr is not resamplable in 2026). COCO-O already supplies the field's working answer under shift."
**Hidden assumptions:** (a) the COCO collection distribution is re-creatable (it is not — Flickr's 2013–2014 content pool is gone; the adaptivity-vs-distribution confound will be *worse* than ImageNetV2's); (b) a funder exists for the annotation budget (none identified; same criterion H used to kill B-0033).
**Killer experiment:** exists in principle (the artifact IS the experiment) but is unfundable and un-deconfoundable as scoped. Cheaper probes (evaluating on held-back COCO test-dev vs val differences, or on ReM) do not answer the adaptivity question.
**Verdict: KILL** (portfolio kill: cost × null-prior × confound; explicitly reversible if an industrial annotation partner materializes — record as conditional revival, per D's protection rationale).

### 38. W2-C-0277 — End-to-end bias tracing (pretraining statistics → detection errors)

**Fresh prior work:** Udandarao 2404.04125 (pretraining-frequency → downstream performance, the correlational spine already published); context-bias causal line (2409.14679, 2505.18446) covering the detection-error end; no end-to-end single-bias trace found.
**Harshest rejection:** "Both ends of your pipeline are published — exposure→performance (Udandarao) and context-bias→detection-errors (Mask Pooling line). The 'end-to-end trace' adds a middle (representation-level mediation) that requires instrumentation at every stage; any gap becomes 'correlation chain', and D's own review conceded the instrumentation could eat the project."
**Hidden assumptions:** (a) one bias is traceable through pretraining→features→detections without controlled pretraining (it isn't — mediation without intervention is storytelling); (b) controlled pretraining at even small scale is affordable for a detection-relevant bias (borderline; ~CLIP-small scale).
**Killer experiment:** the only defensible one — a *single-bias intervention study*: choose one measurable bias (e.g., co-occurrence of a class pair), construct matched pretraining corpora differing only in that statistic (counterfactual caption/image filtering at small scale), pretrain matched encoders, measure the downstream detection-error signature predicted in advance. Small-scale but causal.
**Verdict: MUTATE.**
**Mutated one-liner:** *One bias, controlled: a matched-pretraining intervention tracing a single co-occurrence statistic to a predicted detection failure.* (HRHR retained but converted from observational tracing to a small controlled intervention; if the compute partner for matched pretraining is absent, this converts to KILL by the B-0293/B-0033 criterion.)

---

## Verdict summary table

| # | ID | Verdict | One-line disposition |
|---|----|---------|----------------------|
| 1 | C-0344 | MUTATE | Nature MI 2023 owns "instructions matter"; survive as leaderboard-yardstick version |
| 2 | C-0338 | SURVIVE-IF-EXPERIMENT | size-resolved crossing-point design; Label Convergence ¶1 |
| 3 | C-0046 | **KILL** | Label Convergence + Noise-Aware Eval (both WACV 2025) occupy the band; audit folds into 0302/0311 |
| 4 | C-0326 | SURVIVE-IF-EXPERIMENT | two-annotator adjudication incl. corrections-as-evaluees arm |
| 5 | C-0007 | MUTATE | fold into 0338 (TOLF + Noise-Aware own the pieces) |
| 6 | C-0259 | SURVIVE-IF-EXPERIMENT | two-protocol (recall vs checklist) salience design |
| 7 | C-0043 | MUTATE | size-stratified MDE claims-audit for MICCAI; not a metric critique |
| 8 | C-0057 | SURVIVE-IF-EXPERIMENT | salience-matched deletion arm mandatory |
| 9 | C-0302 | MUTATE | detection variance components + claims audit; 2411.00640/2605.30315 ¶1 |
| 10 | C-0309 | MUTATE | detection-item IRT; 2409.04041 ¶1; convention-stability arm |
| 11 | C-0136 | SURVIVE-IF-EXPERIMENT | scale-matched claims audit; no flagship extrapolation |
| 12 | C-0311 | SURVIVE-IF-EXPERIMENT | coverage-validation ensemble; absorb 0136/0302 or cut |
| 13 | C-0283 | SURVIVE-IF-EXPERIMENT | pre-registered pairs + decay model; else cap out |
| 14 | C-0285 | SURVIVE-IF-EXPERIMENT | pre-registered; merge with 0283 recommended |
| 15 | C-0287 | SURVIVE-IF-EXPERIMENT | P(flip|delta) curve; share 0136's seed grid |
| 16 | C-0327 | MUTATE | torchvision v2 owns the headline (+9.7); survive as itemized attribution |
| 17 | C-0298 | SURVIVE-IF-EXPERIMENT | consequence arm; run inside 0122 program, no slot |
| 18 | C-0260 | SURVIVE-IF-EXPERIMENT | inversion census; COCO-O/BoB/COUNTS positioning |
| 19 | C-0276 | SURVIVE-IF-EXPERIMENT | merged 0276+0256 single paper + prediction-release artifact |
| 20 | C-0256 | SURVIVE-IF-EXPERIMENT | as arm of merged paper (see 19) |
| 21 | C-0279 | SURVIVE-IF-EXPERIMENT | residual-structure framing; Udandarao ¶1; urgent |
| 22 | C-0122 | MUTATE | D-LeDe owns method+number; survive as tail/cross-benchmark leakage |
| 23 | C-0345 | SURVIVE-IF-EXPERIMENT | matched-pair + injection calibration; two-quarter clock |
| 24 | C-0011 | SURVIVE-IF-EXPERIMENT | variance-vs-margins grid; two-quarter clock |
| 25 | C-0150 | MUTATE | field self-retired; survive as exchange-rate instrument |
| 26 | C-0159 | SURVIVE-IF-EXPERIMENT | Lüth-for-detection with box-cost + tuned random |
| 27 | C-0306 | SURVIVE-IF-EXPERIMENT | blind-spot magnitude gate; IoU-aware-calibration baseline |
| 28 | C-0158 | MUTATE | WACV/IJCV 2024 own the empirics; survive as winner's-curse theory |
| 29 | C-0308 | SURVIVE-IF-EXPERIMENT | high-dim joint thresholds + predictive-validity gate |
| 30 | C-0135 | SURVIVE-IF-EXPERIMENT | arbitration-curve design; Mask-Pooling positioning |
| 31 | C-0341 | **KILL** | 2025–26 determinism literature owns mechanism + fix; no content channel |
| 32 | C-0226 | SURVIVE-IF-EXPERIMENT | + real-LR arm + Hallucination-Score positioning |
| 33 | C-0193 | SURVIVE-IF-EXPERIMENT | AP-vs-operating-point decoupling + recalibration arm |
| 34 | C-0321 | SURVIVE-IF-EXPERIMENT | detection flip taxonomy + mitigation baseline |
| 35 | C-0303 | **KILL** | Recht-null prior + unfixable confounds; no affordable identification |
| 36 | C-0119 | **KILL** | PCR (ICCV 2025 oral) owns label-free detection AutoEval |
| 37 | C-0055 | **KILL** | unfundable, un-deconfoundable, null-prior; revive only with partner |
| 38 | C-0277 | MUTATE | observational trace dead; single-bias matched-pretraining intervention |

**Totals: SURVIVE 0 · SURVIVE-IF-EXPERIMENT 23 · MUTATE 10 · KILL 5.**
Freshness kills (literature got there): C-0046, C-0119, C-0341. Methodological/portfolio kills: C-0303, C-0055.
