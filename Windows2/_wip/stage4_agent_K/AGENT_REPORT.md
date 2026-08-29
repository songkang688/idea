# Agent K Report — Stage-4 Reviewer-2 Attack + Freshness Assassination (Batch C LOCK)

**Role:** Reviewer #2 and freshness assassin for batch-C eval-science LOCK ideas. Not the PI; no
final-3 selected. Read-only on all other agents' directories; all writes confined to
`Windows2/_wip/stage4_agent_K/`.

**Deliverables:**

| File | Contents |
|---|---|
| `reviewer2_attacks.md` | 38 full attacks: harshest rejection, hidden assumptions, killer experiment or NONE, verdict, mutation, fresh URLs |
| `verdicts.jsonl` | 38 machine-readable verdict records |
| `AGENT_REPORT.md` | this file |

**Coverage:** all 32 C LOCK IDs from Agent G's `provisional_200_partial.md` (0302, 0309, 0136,
0311, 0344, 0338, 0260, 0276, 0256, 0306, 0057, 0011, 0326, 0327, 0283, 0285, 0226, 0150, 0287,
0259, 0046, 0007, 0279, 0159, 0122, 0298, 0158, 0308, 0135, 0341, 0055, 0043) plus 6 of Agent D's
next-best bets that G placed in FLEX (0345, 0303, 0119, 0321, 0193, 0277) = **38 ideas**. All 20
of D's explicit "PhD-year bets" were already inside the LOCK set. Mandatory nearby literature was
re-searched live (Label Convergence, COCO-ReM, TIDE-adjacent error work, BoB-adjacent
cross-dataset work, tinyBenchmarks-adjacent IRT work, conformal OD 2024–26, Hosang/NMS
calibration, Elephant-in-the-Room descendants, metric-learning/recsys stale-baseline genre) plus
~20 additional 2024–2026 sweeps; every cited URL was returned by live search this session or is
explicitly flagged as inherited from D/G's verified lists.

## Headline numbers

| Verdict | Count | IDs |
|---|---|---|
| SURVIVE | 0 | — (matching Agent H's calibration: no bare SURVIVE granted) |
| SURVIVE-IF-EXPERIMENT | 23 | 0338, 0326, 0259, 0057, 0136, 0311, 0283, 0285, 0287, 0298, 0260, 0276, 0256, 0279, 0345, 0011, 0159, 0306, 0308, 0135, 0226, 0193, 0321 |
| MUTATE | 10 | 0344, 0007, 0043, 0302, 0309, 0327, 0122, 0150, 0158, 0277 |
| KILL | 5 | **0046, 0119, 0341** (freshness) · **0303, 0055** (methodological/portfolio) |

## 1. Ideas that died at this stage (5 kills)

**Freshness kills — the literature got there first (3):**

1. **W2-C-0046** (annotation-noise band CIs). Two WACV 2025 papers occupy the move: *Label
   Convergence* (arXiv 2409.09412) builds the noise-derived mAP band from the exact LVIS
   double-annotation artifact G's census assigned to this idea, and *Noise-Aware Evaluation of
   Object Detectors* (Llerena & Jung) builds noise-aware AP upper/lower bounds on COCO. D's
   Stage-2 MUTATE verdict anticipated the risk; the mutation target has now itself been
   published. Residuals reassigned: claims-audit → 0302, tightness-drift arm (0080) → 0311.
   **This is the mission's "one strong annotation-noise paper scoops the family" scenario,
   realized — twice, at the same venue, in the same year.**
2. **W2-C-0119** (rank stability predicts AP without labels). *PCR — Automated Model Evaluation
   for Object Detection* is an **ICCV 2025 oral** (arXiv 2508.12082) doing label-free mAP
   estimation for detectors with a corruption meta-dataset, and it already beats the
   perturbation-stability method that is this idea's mechanism. Any resubmission is a
   method-increment entry in someone else's benchmark table.
3. **W2-C-0341** (batch cross-talk exploit). The 2025–2026 determinism literature (NeurIPS 2025
   arXiv 2506.09501, Thinking Machines batch-invariant kernels, TBIK, CoRun) fully explains and
   fixes batch-composition dependence; no content-dependent channel exists to pre-register in a
   correctly configured detector. Residual: a batch-sensitivity paragraph inside FLEX C-0290.

**Methodological/portfolio kills — no affordable experiment silences the reviewer (2):**

4. **W2-C-0303** (tuning-on-benchmark generalization tax). The flagship precedent (Recht et al.,
   ImageNetV2) found **no adaptive overfitting**, COCO-O already ran the shift version on 100+
   detectors, and the observational design is unfixably confounded (era × family × compute ×
   selective disclosure). The clean randomized-budget design is unfundable against a published
   null prior. Kill by the same standard H applied to B-0033/B-0252.
5. **W2-C-0055** (fresh i.i.d. COCO test set). Unfundable without a partner, and — worse — the
   2013–2014 Flickr pool is not resamplable, so the adaptivity-vs-distribution confound would be
   *worse* than ImageNetV2's, against the same null prior. Recorded as conditionally revivable
   if an industrial annotation partner appears (preserving D's HRHR rationale).

**Freshness-forced mutations (headline dead, narrower claim survives, 10):** 0344 (Nature MI 2023
ran the instruction A/B at 864-annotator scale; survives only as the leaderboard-yardstick
version), 0327 (torchvision's own `fasterrcnn_resnet50_fpn_v2` published the +9.7 AP
recipe-on-2015-architecture number in 2022; survives as itemized attribution), 0302 (MDE/power
frameworks fully built for LLM evals, arXiv 2411.00640 + 2605.30315; survives as
detection-variance-components + claims audit), 0309 (IRT with misfit-error-detection and tiny
subsets done on 91 vision models, arXiv 2409.04041; survives as detection-item IRT with
convention-stability), 0158 (WACV 2024 IoU-aware calibration + IJCV 2024 own the "NMS biases
confidences" empirics; survives as winner's-curse selection theory), 0150 (the field is
self-retiring — arXiv 2503.23220, Foundational FSOD; survives as the exchange-rate instrument),
0122 (D-LeDe published the pHash leakage audit + KITTI scandal number; survives as
tail/cross-benchmark leakage), 0007 (→ arm of 0338), 0043 (→ size-stratified MDE claims audit),
0277 (→ single-bias matched-pretraining intervention, compute-partner-conditional).

## 2. The 8 most paper-shaped C ideas (post-attack)

"Paper-shaped" = sharp post-attack claim, affordable decisive killer experiment, visible venue
slot. Ordered by conviction:

1. **C-0306 (conformal coverage destroyed by NMS).** Freshness re-verified: SeqCRC still
   calibrates after NMS; the blind-spot magnitude (GT objects whose only covering candidates get
   suppressed) is a cheap decisive gate, and the coverage-preserving suppression method has a
   formal-novelty moat. Must now beat the no-NMS IoU-aware-calibration baseline. Urgent.
2. **C-0338 (size-resolved human ceiling).** With Label Convergence supplying the aggregate
   ceiling and the artifact, the size-stratified crossing-point experiment ("below s pixels,
   AP-small progress is unfalsifiable") is cheap, sharp, and takes the family's strongest slot.
   Absorbs 0007 and shares infrastructure with 0344-mutated and 0259.
3. **C-0057 (missing-annotation tax law).** The differential (anti-quality) effect remains
   unclaimed; ReM/MJ-COCO de-risk the premise and supply the salience-matched deletion model
   that makes the design non-toy. Inference-only.
4. **C-0011 (prompt variance vs leaderboard margins).** Still unclaimed for 2D OVD leaderboards;
   TG-OverLoCK shows method papers are starting to report template robustness — the window is
   closing, but a two-GPU-week inference grid ships the one number the field lacks.
5. **C-0326 (powered adjudication of residual COCO errors).** The corrections-as-evaluees arm
   (human adjudication vs ReM vs MJ-COCO agreement) turns the crowding into content and yields
   the quotable share. Must move before the next corrected-COCO release.
6. **C-0136 (seed variance vs published deltas, scale-matched).** The detection census is still
   open (confirmed this session); with the flagship extrapolation disclaimed and the claims audit
   restricted to same-scale deltas, it is fundable and decisive. Shares its seed grid with 0287.
7. **C-0309-mutated (detection-item IRT).** The convention-stability question ("is the IRT fit an
   artifact of the matching rule?") is genuinely new content, the misfit↔ReM lift is
   pre-registrable, and the 1k short test validated on held-out model families is a usable
   artifact. Positioning against arXiv 2409.04041 is mandatory and survivable.
8. **C-0226 (GT-controlled SR accounting).** The detection-metric hallucination decomposition is
   confirmed unclaimed; the Hallucination Score paper supplies a perceptual comparator, not a
   competitor. Needs the real-LR validation arm.

Just below the line: 0279 (residual-structure version is strong but lives entirely in Udandarao's
shadow), 0345 and 0159 (both strong but on hard execution clocks), 0285+0283 (best run as one
pre-registered audit), 0311 (flagship-grade only if the PI lets it absorb 0136/0302 rather than
compete with them).

## 3. Which eval-audits should be capped out of the 200

G's C-side eval-audit share was 57.9% against D's ~60% cap. After this round the arithmetic and
the venue-fatigue argument both say the cap should tighten. Concrete recommendations:

**Remove from slot accounting (verdict-driven, 5):** C-0046, C-0119, C-0341, C-0303, C-0055
(kills). This alone drops C's eval-audit count by four [E] slots and one [A] slot.

**Convert to arms — no standalone slots (5):**
- **C-0007 → 0338** (same conclusion, same infrastructure).
- **C-0256 → 0276** as one merged long-tail forensics paper with the prediction-release artifact
  (two slots → one; salami-slicing defense).
- **C-0298 → 0122-mutated** as a side audit inside one leakage program (expected-null long-shot
  should not hold a slot in a portfolio already heavy with audits).
- **C-0043 → the 0302/0338 noise-floor program** as its MICCAI-facing arm.
- **C-0283 + C-0285 → one pre-registered tuning-fairness audit** with two budget conventions
  (any reviewer treats them as one paper; the portfolio should too).

**Hard caps on family co-submission (venue-fatigue control):**
- **GT-epistemology family:** at most **3 concurrent submissions** from {0338, 0344-mutated,
  0326, 0259, 0057, 0311} — recommend 0338 + 0057 + 0326 first wave; 0344-mutated and 0259
  second wave sharing annotation infrastructure; 0311 only in its absorb-0136/0302 flagship form.
- **Rigor/training-audit family:** at most **2 executed** from {0136+0287 (shared grid),
  0283+0285 (merged), 0327-mutated} — recommend 0136+0287 and the 0283/0285 merger; 0327-mutated
  only if a compute partner covers the ~15-run ladder.
- **Leaderboard-integrity re-analysis family:** 0260's inversion census and 0122-mutated should
  not both ship as standalone D&B submissions in the same cycle as 0345; stagger or bundle.

**Net effect if adopted:** C's eval-audit slot count falls from 33 to ~24–26 (roughly 45–50% of
C's contribution), the family collision surface shrinks, and the freed slots go to batch A or to
the C mechanism ideas (0306, 0308, 0135, 0158-mutated) that this round left healthier than the
audits.

## 4. Correlated-failure warnings for the PI

1. **The annotation-noise front is no longer empty — it is a race.** Five artifacts/papers
   published 2024–2026 (COCO-ReM, Label Convergence, Noise-Aware Evaluation, MJ-COCO,
   label-error-correction benchmark 2508.06556) already occupy overlapping shares of the
   GT-epistemology thesis, and one LOCK idea (0046) died to them this round. Every surviving
   family member holds a *wedge*, not a territory; wedges decay in months. Execute 0338/0326/0057
   first or expect two more kills at the next freshness pass.
2. **The "port LLM-eval statistics to detection" pattern (0302, 0309, and partially 0136) has
   the same ~12-month shelf life H diagnosed for B's "dynamics/causal upgrade" heuristic.**
   2411.00640 → 2605.30315 took ~14 months; the detection port is an obvious next step for those
   authors' communities. First-mover advantage only.
3. **Checkpoint-dependence cluster (0276+0256, 0260, partially 0159):** all require third-party
   retraining whose reimplementation fidelity is the reviewers' first attack. The
   prediction-release artifact (per-class predictions for the retrained grid) is the shared
   shield and should be budgeted once, centrally.
4. **Urgency-clock cluster (0306, 0011, 0279, 0345):** each sits on a front with verified
   2025–2026 movement (conformal OD, template-robustness reporting, exposure-law extensions,
   contamination tooling). Same rule H set for B: two-quarter execution or drop; portfolio
   storage converts these to kills.

## 5. Compliance

- All writes confined to `Windows2/_wip/stage4_agent_K/`; no other agent's directory modified.
- No final-3 selected; verdicts are inputs to the PI.
- No invented citations: every URL was returned by live web search this session or is flagged
  [inherited from D/G's verified lists]; memory-only or non-re-verified citations are flagged in
  place (Metrics Reloaded, arXiv 2605.07549, Yan et al. 2021).
- Calibration matched to Agent H: zero bare SURVIVEs; every survival is conditional on a named
  experiment/control absent from the Stage-1/Stage-2 form.
