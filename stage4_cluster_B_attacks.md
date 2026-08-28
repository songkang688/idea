# Stage 4 — Cluster B: Reviewer #2 Attack Round

**Cloud Sub-Agent K (Reviewer #2) → Supervisor Windows7.**

Mandate: assume each Stage-3 Cluster B survivor is a submitted paper. Reject as hard as possible on every axis —
novelty, feasibility, confounds, identifiability, effect size, data availability, evaluation circularity,
"so what". **Keep only if a realistic experiment can shut the reviewer up.**

Input: 20 decision units from `stage3_cluster_B_keep.md` (14 KEEP) + `stage3_cluster_B_mutations.md` (6 mutations,
of which M2/B-0069 was already folded into B-0062). Cross-checked against Cluster A keeps
(`stage3_cluster_A_keep.md`) and Cluster C keeps (`stage3_cluster_C_keep.md`).

**Verdict totals: 7 SURVIVE (6 KEEP + 1 mutation KEEP, with M4 merged into B-0112 and counted once) /
12 KILL (incl. M2, which dies with its host B-0062) / 1 MERGE (M4 → B-0112).**

Protected status was not honored where the attack is fatal: B-0058 (P) and B-0353 (P) are killed;
B-0121 (P) and B-0230 (P) survive on merit.

## Fresh searches run this session (Reviewer #2's own literature check)

New attacks cite only work actually found in this session's searches; everything else is inherited from the
Stage-3 killsheet and marked as such.

1. FSS wrong-support / foreground-bias audit → found only bias-*mitigation* methods (TBS AAAI 2024, AENet
   ECCV 2024, CVPR 2024 background-context-bias modulation). No counterfactual audit paper. B-0121 stands.
2. Text-prompted medical segmentation hallucination → **direct hit on B-0350**: MedVeriSeg + MedVeriSeg-Bench
   (arXiv 2604.10242) and HEAL-MedVQA (arXiv 2505.00744, IJCAI 2025).
3. Inpainting-artifact shortcut → adjacent only: Shortcut Learning in Medical Image Segmentation
   (arXiv 2403.06748; padding/center-crop/caliper shortcuts). No detectability→transfer-gap law. B-0212 stands.
4. Latent-compression thin structures → adjacent only: VAEsselSparse (arXiv 2605.01382), VesselSDF
   (arXiv 2506.16556) — mask-space representation fixes, not a generated-image fidelity floor. B-0222 stands.
5. Label-cleanliness decomposition → SENSE (arXiv 2605.19289) confirmed adjacent (generative labels not clean;
   OT reassignment fix); the confound-breaking decomposition remains unrun. B-0230 stands.
6. Doppler audio supervision → **kill ammunition for B-0353**: Doppler *image*-based weakly-supervised vascular
   segmentation exists (ISBI 2023, DOI 10.1109/ISBI53787.2023.10230548); DopUS-Net (arXiv 2305.08938) fuses
   Doppler for vessel segmentation. No paired audio+B-mode dataset found.
7. MoE routing as pathology detector → engineered MoE-AD wave is crowding fast: AnomalyMoE (arXiv 2508.06203),
   MoECLIP (arXiv 2603.03101), ReMoE (arXiv 2607.29039), REN (IEEE TMI 2026). Emergence question itself still
   unclaimed, but see B-0058 attack.
8. Decision-flip audit → automated-vs-manual RECIST reader studies (Cancers 16(23):4009: κ 0.67–0.81 category
   agreement at DSC ≈0.85; Cancers 18(5):808 systematic review; EJR 2026 iRECIST feasibility: AI assistance
   shifted reader scores across progression boundaries in up to 37.5% of cases) show decision-level disagreement
   is large — but **no audit of published SOTA deltas exists**. M5 stands and gains supporting evidence.

---

# SURVIVORS (7)

## S1. B-0112 (+ M4/B-0159 merged) — Convention-shift program: formalization, detector, convention tokens

**Claim under review:** label-consistent convention shift is a distinct shift class; it is detectable without
target-convention knowledge; convention tokens with interpolation + controlled-relabeling validation make the
convention axis explicit and switchable.

**Reviewer #2 attacks:**
1. *"Label-free" is false advertising.* The detector's signature (feature statistics match source, output-space
   disagreement concentrates at boundaries with consistent bias) requires target-side annotations to compute
   disagreement. Without target labels there is nothing to disagree with. You detect convention shift only in
   the dataset-audit setting, not at deployment.
2. *Strawman simulation.* Systematic margin erosion/dilation is a cartoon of real guideline differences; real
   convention pairs are entangled with site appearance shift, so the detector will misfire exactly where it
   matters. Castro et al. (Nature Comms 2020, inherited) already named the phenomenon — you add a toy.
3. *Token semantics unproven.* Dataset-conditioning tokens exist (inherited); nothing guarantees your tokens
   encode convention rather than residual site appearance.
4. *Two half-papers stapled together.* The taxonomy/detector and the token method each look thin alone.

**Can a realistic experiment shut me up? YES — which is why it survives, as one merged program:**
- Zero-cost real conventions: nested label hierarchies on identical images (e.g., BraTS-style enhancing-tumor
  vs tumor-core vs whole-tumor definitions) give *actual* convention variants with no appearance confound and no
  new annotation — this defeats the strawman attack directly.
- One bounded re-annotation arm: same images labeled under two written guidelines (the controlled-relabeling
  ground truth no prior token work has — inherited Stage-3 verification).
- Pre-registered three-way test on identical images: (a) adaptation methods *harm* under pure convention shift
  and help under pure covariate shift; (b) detector separates the regimes at stated AUROC in the audit setting
  (scope the claim honestly to audits); (c) tokens trained on controlled relabelings recover the convention axis
  and interpolate monotonically under blinded rater judgment.
- Merged because neither half survives review alone (attack 4); together the validation chain is closed.

**Verdict: KEEP (M4 merged in).**

## S2. B-0121 (PROTECTED) — Wrong-support counterfactual audit of few-shot segmentation

**Claim under review:** a substantial share of reported FSS accuracy is support-independent foreground prior,
measurable by feeding deliberately mismatched supports; a support-sensitivity score reorders the leaderboard.

**Reviewer #2 attacks:**
1. *Old news.* Foreground/base-class bias is documented (Learning What Not to Segment, CVPR 2022, inherited);
   the 2024 method wave (TBS AAAI 2024, AENet ECCV 2024, CVPR 2024 iterative modulation — searched this session)
   exists *because* everyone knows about background/foreground bias. Your audit quantifies the known.
2. *The audit measures the benchmark, not the models.* On single-salient-object queries (most of PASCAL-5i),
   a wrong support is uninformative — there is nothing else to segment, so "prediction unchanged" conflates
   model pathology with benchmark degeneracy.
3. *Evaluation-only, workshop scale.* No method contribution; the falsification branch ("all methods collapse
   appropriately") leaves you with a null.

**Can a realistic experiment shut me up? YES:**
- Days of compute, zero training: N public FSS checkpoints, matched wrong-class supports, prediction-change
  rates. Nobody publishes this number (searched: mitigation methods exist, the counterfactual audit does not).
- Attack 2 is answered inside the design: stratify by query complexity (single- vs multi-object, distractor
  present/absent) so benchmark degeneracy is measured *separately* from model insensitivity — the stratified
  audit indicts benchmark and models on separate counts, which is strictly more damning.
- Attack 3 is answered by the headline number: if support-sensitivity reorders the leaderboard, every future
  FSS paper must report it; the audit + fixed distractor-enriched evaluation split is a full contribution.
  If instead everything collapses appropriately, the field's validity is certified — an informative negative
  the audit uniquely provides.

**Verdict: KEEP.**

## S3. B-0212 — Blending-artifact detectability → synthetic-to-real transfer-gap law

**Claim under review:** artifact detectability (probe classifier AUROC on inpainted vs real patches) predicts
the synth-to-real gap of lesion models; artifact-suppressed compositing closes most of the gap.

**Reviewer #2 attacks:**
1. *Confounded law.* Across generation settings, better generators improve realism and blending together —
   your detectability↔gap correlation may just re-measure "better generators are better." The "law" is
   generator quality in a trench coat.
2. *Detectable ≠ used.* A dedicated probe finding artifacts does not prove the lesion model keys on them;
   shortcut usage requires a causal test, not a correlation.
3. *Known since 2017.* Cut-Paste-and-Learn (inherited) showed blending matters; medical shortcut learning is
   documented (arXiv 2403.06748, searched — padding/caliper shortcuts). You quantify folklore.

**Can a realistic experiment shut me up? YES — the causal arm is the paper:**
- Hold generator and content *fixed*; vary only compositing (cut-paste, Poisson, harmonization, adversarial
  anti-artifact blending). If probe-AUROC ordering predicts real-set performance ordering at fixed content,
  the artifact channel is isolated from generator quality (kills attack 1).
- Reverse intervention: inject artifacts into otherwise-identical composites and watch the gap reopen —
  direct evidence the segmenter *uses* the shortcut (kills attack 2).
- Attack 3 concedes the motivation: known-qualitatively + never-quantified + a routine hygiene check
  (report probe-AUROC of your synthesis pipeline) is exactly a measurement paper the field adopts.

**Verdict: KEEP.**

## S4. B-0222 — Thin-structure fidelity floor of latent diffusion + downstream penalty

**Claim under review:** a measurable width threshold below which latent-generated structures are absent or
corrupted; models trained on such data inherit a thin-structure blind spot; pixel-space generation removes it.

**Reviewer #2 attacks:**
1. *The field already believes this and is fixing it.* MedVAE, FA-VAE (inherited); and now sparsity-preserving
   vessel autoencoders exist precisely because dense latent compression destroys thin structures (VAEsselSparse,
   arXiv 2605.01382; VesselSDF, arXiv 2506.16556 — searched). Your measurement arrives after the fix wave.
2. *A number for a moving target.* Each new autoencoder shifts the floor; the paper is obsolete on release.
3. *Conditioning confound.* Your own risk statement: at thin widths you cannot tell whether generation fails
   or conditioning fails — the headline curve is uninterpretable as stated.

**Can a realistic experiment shut me up? YES — by shipping a protocol, not a constant:**
- Autoencoder round-trip arm (encode-decode real images with calibrated-width structures, no generation)
  isolates compression fidelity from conditioning cleanly — kills attack 3 with one cheap experiment.
- Calibrated-width phantom battery + survival-vs-width curves across k autoencoders × downsampling factors:
  the *protocol* is the contribution and survives generator turnover (kills attack 2 — every new autoencoder
  gets a datasheet number, which is the point).
- Attack 1 concedes the premise and strengthens the need: the fix wave is engineering against an unmeasured
  quantity; matched-compute pixel- vs latent-space training on a real vessel task, with recall deficit tracking
  the measured floor, converts belief into a decision rule (when is pixel-space generation mandatory).

**Verdict: KEEP.**

## S5. B-0230 (PROTECTED) — Label-cleanliness vs image-distribution decomposition of synthetic data

**Claim under review:** injecting human-matched label noise into synthetic labels erases a large fraction of
the synthetic-real difference — pricing label perfection separately from image realism.

**Reviewer #2 attacks:**
1. *False premise for the dominant pipeline.* Generative synthetic labels are NOT clean — SENSE (arXiv
   2605.19289, searched) documents generative instability and builds OT label reassignment because of it.
   You are pricing a perfection that doesn't exist.
2. *The noise model determines the answer.* "Human-matched" noise is a modeling choice; parametric boundary
   jitter vs structured rater bias give different headlines. Garbage calibration in, garbage decomposition out.
3. *Four-arm training grids are cheap to run and cheap to dismiss* — one dataset, one task, and reviewers call
   it anecdote.

**Can a realistic experiment shut me up? YES:**
- Scope to pipelines where labels ARE clean by construction — rendered/simulated data — and state that scope in
  the title if needed (kills attack 1; the Stage-3 rebuttal stands: SENSE's finding makes the label-quality
  axis *more* worth isolating, and rendered pipelines are a huge real segment).
- Calibrate noise injection from measured multi-annotator disagreement (public multi-rater segmentation data),
  not parametric assumptions, and report decomposition-vs-noise-model sensitivity as a first-class result
  (kills attack 2 by making the dependence explicit rather than hidden).
- Pre-registered 4-arm grid {real, synth, synth+matched-noise labels, real+consensus-cleaned labels} across
  data scales × ≥2 tasks (kills attack 3). Falsification is clean: if noise injection doesn't move synthetic
  utility, the answer is "it's the images," which is equally decision-relevant for investment.

**Verdict: KEEP.**

## S6. B-0331 — Report negations as spatially grounded negative supervision

**Claim under review:** parsing "no X" into atlas-grounded negative regions reduces false positives of
report-supervised dense models, concentrated in frequently negated finding classes.

**Reviewer #2 attacks:**
1. *Near-zero information content.* Organ-scale negatives from "no pneumothorax" teach what any trained model
   already knows — most pixels are negative. Your FP reduction is trivial prior-tightening obtainable from a
   class-frequency prior without reading a single report.
2. *Grounding poison.* Atlas misgrounding converts good negations into wrong negative labels exactly in the
   pathological/variant cases where anatomy deviates from atlas.
3. *The hallucination motivation just died.* The absent-query problem is being solved training-free at
   inference (MedVeriSeg, searched — see B-0350 kill); why train?

**Can a realistic experiment shut me up? YES — because the controls that answer attack 1 are cheap and decisive:**
- Information-content controls on public report+image data (MIMIC-CXR-scale): compare negation negatives against
  (a) a matched class-prior baseline (same total negative mass, no per-patient reports) and (b) permuted-report
  negatives (negations drawn from other patients). Any gain over both controls is per-patient information —
  the exact quantity attack 1 denies. If it doesn't beat the matched-prior control, the idea is dead; clean
  falsification either way.
- Attack 2 is bounded, not fatal: conservative region margins + a poisoning-rate sensitivity sweep quantify it.
- Attack 3 misses the scope: B-0331 is training supervision at archive scale for any dense/report-supervised
  model (FP reduction in screening), not an inference-time verifier for LISA-like MLLMs; the mechanism and the
  deliverable are disjoint from MedVeriSeg.

**Verdict: KEEP.**

## S7. M5 (from B-0362) — Decision-flip-rate audit of published SOTA deltas

**Claim under review:** recompute N published segmentation SOTA deltas under distinct legitimate decision-rule
families; report the fraction of published claims that flip. One headline number for the field's fragility.

**Reviewer #2 attacks:**
1. *Cherry-picked rules, unanswerable accusation.* Choose thresholds near the operating point and everything
   flips; choose lax rules and nothing does. The headline number is an artifact of rule selection.
2. *You can't get the checkpoints.* Most published deltas aren't reproducible; your auditable sample is biased
   toward well-engineered public pipelines, underestimating (or misestimating) fragility.
3. *Meta-science is unpublishable at method venues,* and Metrics Reloaded (inherited) already gives guidance.

**Can a realistic experiment shut me up? YES:**
- Pre-register decision-rule families drawn verbatim from clinical/operational guidelines (RECIST 1.1 response
  categories, dose-volume constraints, deployed alarm thresholds) *before* computing any flip — rule selection
  is then external, not the authors' (kills attack 1); report the flip rate as a surface over the rule grid
  with sensitivity analysis, not a single cherry-pickable number.
- Audit only pairs with public checkpoints/predictions and report the auditable fraction as a finding in itself
  (turns attack 2 into a result about reproducibility).
- Attack 3 is contradicted by evidence found this session: automated-vs-manual RECIST reader studies show
  category agreement of only κ 0.67–0.81 even at DSC ≈0.85, and AI assistance shifted reader scores across
  progression boundaries in up to 37.5% of cases (Cancers 16(23):4009; EJR 2026 feasibility study) — decision-
  level disagreement is demonstrably large, so the audit will not be vacuous, and no published-delta flip audit
  exists (searched). Metrics Reloaded gives guidance, not an audit of the literature's published claims.

**Verdict: KEEP.**

---

# KILLS (12)

## X1. B-0058 (PROTECTED) — MoE routing as free pathology detector — KILL

**The dilemma no experiment escapes:** the interesting claim is emergence in *foundation-scale* medical MoE
models; the affordable experiment is pretraining a *small* MoE. A null at small scale says nothing about
emergence at scale (emergent capabilities are scale-dependent by definition — the claim's own framing).
A positive at small scale is confounded by the idea's own stated risk: experts specialize on acquisition
(scanner, site, protocol), which correlates with pathology prevalence across sources — separating "routing
detects pathology" from "routing detects the scanner that pathological cases came from" requires acquisition-
stratified corpora that public medical data mostly cannot supply.
**Second front:** to matter, the routing signal must beat cheap unsupervised anomaly-detection baselines AND
the engineered MoE-AD wave found this session (AnomalyMoE arXiv 2508.06203; MoECLIP arXiv 2603.03101; ReMoE
arXiv 2607.29039; REN, IEEE TMI 2026). "Free but worse than the trained router" is not a paper, and the wave
will have saturated the message by submission time.
**No realistic experiment simultaneously answers the scale objection and the acquisition confound. KILL.**

## X2. B-0062 (+M2/B-0069 arm) — Physically calibrated per-pixel smoke transmittance GT — KILL (closest call)

**Benchmark-validity circularity:** the paper's load-bearing claim is that lab-recovered dense transmittance
validates *field* smoke perception. Verifying that claim requires field-scale dense physical GT — exactly the
thing whose nonexistence motivates the dataset. Field transmissometer point-checks (the A2I2 move, inherited)
validate a few pixels; all the benchmark's discriminative power lives in the fuzzy boundary where no point
sensor will sit.
**Physics regime attacks:** the known-background inversion assumes attenuation + airlight over a calibrated
pattern; combustion smoke at deployment distances adds multiple scattering, self-emission, and path radiance —
a different regime from a glycol fog machine at 3 meters (the glycol-vs-combustion gap is the idea's own
unresolved risk). **Effort asymmetry:** a physical capture rig, radiometric calibration, and real-smoke
sessions buy a benchmark whose external validity cannot be established from inside the lab.
**M2 (metric-validation arm) dies with its host.**
**Closest call on this list** — revive at a later stage *only if* rescoped honestly as a lab-physics benchmark
(controlled-conditions opacity estimation) without the field-transfer claim. As submitted: **KILL.**

## X3. B-0193 — Speckle-native self-supervised pretraining for ultrasound — KILL

**The signal is destroyed in the data you can get:** clinical B-mode archives are speckle-filtered,
log-compressed, and scan-converted (the idea's own risk statement); genuine speckle statistics live in RF/IQ
data, and public RF datasets are orders of magnitude too small to support "SSL at matched compute" claims.
**The pretext is self-defeating:** predicting Nakagami/decorrelation statistics — deterministic, locally
computable functions of the input — is solvable by a shallow filter bank; nothing forces the encoder to learn
anatomy. The pretext reduces to distilling a classical estimator, and features that encode local moments will
probe well on texture tasks for reasons that have nothing to do with transferable structure — making even a
"positive" result uninterpretable.
**No realistic experiment fixes both the data pipeline and the triviality objection at once. KILL.**

## X4. B-0285 — Rare anatomical variants as long-tail benchmark — KILL

**The collection is the bottleneck, and it cannot ship:** variant cases curated from case reports and clinical
archives face licensing/privacy walls — a benchmark that cannot be released is not a benchmark. Public
segmentation corpora contain variants at population rates (situs inversus ~1/10⁴), so "curate ~100 cases"
means radiologist review of enormous archives: the curation is the unsolved research cost, not a preliminary.
**Power:** ~100 cases across ~10 variant types is n≈10 per variant; per-variant failure claims are anecdotes.
**Predictability:** "models trained on modal anatomy fail confidently on situs inversus" — every reviewer
already believes the headline; and the safety layer reduces to atlas-consistency checking, established
machinery (MOOD-adjacent, inherited).
**A realistic experiment produces an underpowered confirmation of the expected on data nobody else can use.
KILL.**

## X5. B-0344 — Radiotherapy dose maps as inverse contour supervision — KILL

**Structural identifiability failure, unfixable by experiment design:** dose gradients live where the optimizer
put them — at PTV margins, beam apertures, and OAR constraint surfaces that bind only near targets:
1. PTV = CTV + safety margin (typically 5–10 mm, protocol-specific): the "target evidence" is offset from true
   anatomy *by design*, by more than the accuracy gap separating modern segmenters. The supervision teaches the
   margin, not the organ, and no noise model fixes a systematic protocol-dependent bias.
2. Distal organs sit in flat low-dose regions carrying zero boundary signal — supervision is spatially confined
   to the treated region, so the trained model is silently untrained exactly where dose says nothing.
3. Where constraints do bind, dose conforms to the *planner's* contour of that era/protocol — inheriting
   inter-protocol convention variance as label noise (compounding attack 1).
**The minimal experiment (OpenKBP inversion, inherited citation) would "succeed" only where constraints bind,
and the resulting margin bias is undetectable by the experiment itself — the shutting-up experiment cannot
distinguish the paper's success from its failure mode. KILL.**

## X6. B-0350 — Suggestion-induced hallucination in medical segmentation — KILL

**Direct prior-work hit, found this session:** MedVeriSeg (arXiv 2604.10242) constructs MedVeriSeg-Bench —
false/absent-target queries for text-prompted (LISA-like) medical segmentation across 24 modalities and 151
entities with a clinician-in-the-loop pipeline — and ships a training-free query-verification mitigation that
rejects hallucinated segmentation while preserving valid-query utility. HEAL-MedVQA (arXiv 2505.00744,
IJCAI 2025) covers the VQA-side hallucination protocol with doctor-annotated masks and textual/visual shortcut
tests. The idea's exact core — "segment the tumor" when none exists, measure conjured masks, mitigate — is
published, benchmark and mitigation included.
**Remaining deltas** (hallucination-rate vs training-exposure correlation; negation-mined absence-supervision
training as an alternative mitigation) are follow-up experiments to someone else's benchmark, not a program.
The negation-supervision substance survives independently as B-0331. **KILL.**

## X7. B-0353 (PROTECTED) — Doppler audio as vessel supervision — KILL

**Dominated by published work, found this session:** Doppler *image*-based weakly-supervised vascular
ultrasound segmentation exists (ISBI 2023, DOI 10.1109/ISBI53787.2023.10230548 — color-Doppler pseudo-labels
train B-mode vessel segmenters, generalizing to images without Doppler), and DopUS-Net (arXiv 2305.08938)
fuses Doppler and B-mode for vessel segmentation with public code. The audio stream at a single interrogation
gate is a strict information subset of the dense color-Doppler flow map that the same machine produces in the
same exam — the proposal is to use strictly less information through a strictly harder pipeline.
**Feasibility (the Stage-3 flagged risk, now decisive):** no paired audio+B-mode dataset exists (searched —
Doppler "audio" datasets are underwater hydrophone/maritime data); DICOM archives do not routinely store the
audio; prospective collection inherits operator selection bias (gates placed where vessels are already seen).
**Any realistic experiment is dominated by the published color-Doppler-image baseline by construction. KILL.**

## X8. B-0361 — Ambiguity handling as a transferable skill — KILL

**The experiment cannot exist:** cross-domain calibration transfer requires multi-rater ground truth in several
ambiguity domains (medical, smoke, camouflage); the multi-rater smoke/camouflage collections it depends on were
part of killed ideas (B-0070 line), so the dependency chain is dead and no public substitute exists.
**Confound that no available control removes:** cross-domain "uncertainty transfer" is predicted by boundary-
width statistics alone — fuzzy boundaries have wider rater disagreement everywhere, so a model that maps local
gradient structure to uncertainty will "transfer" without any domain-general evidence-weighing. Separating the
two requires matched-width cross-domain stimuli that don't exist.
**Stage 3 already flagged medium-low novelty confidence (terminology-mismatch risk on the search). Weakest
epistemic position on the list + infeasible decisive experiment. KILL.**

## X9. M1 (from B-0007, was PROTECTED) — Mirror-Cost flipping audit — KILL

**Conceded ceiling:** Stage 3's own entry says "low ceiling as a full paper." The outcome is folklore
confirmation ("don't mirror lateralized structures" — confirmed); the when-to-flip decision rule is one table.
**Vanishing effect size:** the idea's own risk — high-capacity models resolve laterality from context — predicts
the measured damage shrinks toward zero exactly at the model scale reviewers care about, leaving an audit of
small models' pathologies. A cheap experiment that can only confirm folklore or measure a vanishing effect is a
workshop note, not a keep slot. **KILL.**

## X10. M3 (from B-0078) — Tone-mapping destroys fire evidence — KILL

**The decisive experiment is not realistic:** the hypothesis requires paired RAW/HDR + tone-mapped captures of
*real fires* and matched confusers (sunsets, fog, sodium lights, welding) at benchmark diversity. Controlled
burns are regulated, capture campaigns are expensive, and the achievable n is a demo, not a benchmark — the
exact "small raw subset" weakness Stage 1 already flagged, now load-bearing.
**Attribution confound survives even a positive result:** fire-vs-confuser separation may ride on temporal
flicker and plume dynamics rather than the radiometric channel; a RAW-domain gain does not isolate tone-mapping
as the destroyed evidence without temporal controls that multiply the capture burden. **KILL.**

## X11. M6 (from B-0366) — Calibrated annotation-collapse simulation — KILL

**Calibration theater:** the published anchoring measurements (OSAIRIS 72–88% catch rates, inherited) are one
or two scalars; the simulation's qualitative conclusions — drift regimes, the stabilizing blind-case ratio —
are determined by the annotator behavior model those scalars do not constrain (spatial error correlation,
error-type mix, attention drift across generations, catch-rate dependence on error salience).
**Unfalsifiable deliverable:** the actionable output (minimum blind-annotation rate per generation) is a
prediction about multi-generation dynamics for which no validation data exists or can be created in scope —
real generation-2+ clinical annotation ecosystems aren't observable, and crowdworker toy loops don't transfer
to clinical annotation behavior. A simulation whose headline number cannot be checked by any realistic
experiment is exactly what this stage exists to kill. **KILL.**

## X12. M2 (from B-0069) — Metric-validation arm of B-0062 — KILL (with host)

Folded into B-0062 at Stage 3; B-0062 is killed above (X2), and the arm has no standalone existence —
Stage 3 itself judged it "too thin standalone" with the physical anchor gone. **KILL.**

---

# Cross-cluster notes

- No survivor collides with Cluster A keeps (SAM/promptable-model internals, memory, distillation) or
  Cluster C keeps (training dynamics, ISP/shift axes, comparability audits).
- M5 (decision-flip audit) stays disjoint from C-0276 (framework/protocol drift with fixed checkpoints):
  C-0276 measures implementation variance of the *same* model; M5 measures decision-rule invariance of
  *published deltas between* models. Scoping inherited from Stage 3 and preserved.
- B-0230's rendered-pipeline scoping keeps it disjoint from C-cluster synthetic/curation entries.

# Survivor portfolio (7)

| # | ID | Program | Cheapest decisive experiment |
|---|----|---------|------------------------------|
| 1 | B-0112 (+M4) | Convention-shift formalization + detector + convention tokens | Nested-label-hierarchy conventions on identical images + one controlled relabeling; three-way pre-registered test |
| 2 | B-0121 (P) | Wrong-support counterfactual FSS audit | N public checkpoints × shuffled supports, stratified by query complexity; days of compute |
| 3 | B-0212 | Blending-artifact detectability → transfer-gap law | Fixed-content compositing ladder + artifact injection/suppression causal arms |
| 4 | B-0222 | Thin-structure fidelity floor protocol | AE round-trip on calibrated-width phantoms (no generation) + matched-compute pixel-vs-latent training |
| 5 | B-0230 (P) | Label-cleanliness vs image-distribution decomposition | Pre-registered 4-arm grid, measured-noise calibration, rendered-pipeline scope |
| 6 | B-0331 | Negation mining → spatial negative supervision | Matched class-prior + permuted-report controls on public report+image data |
| 7 | M5 (B-0362) | Decision-flip-rate audit of published SOTA deltas | Pre-registered guideline-derived rule families × public checkpoints; flip-rate surface |
