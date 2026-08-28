# Experiments — C-0306 (full protocol)

Companion to `proposal.md` §§12–18. Everything here is **pre-registered**: decision thresholds,
strata, seeds, and interpretation rules are fixed before any real-data run. Labels: KNOWN /
EVIDENCE / HYPOTHESIS / MEASURED (synthetic) as defined in `proposal.md`. **No experiment below has
produced a real-data number yet.** The only MEASURED results in this package are synthetic
(E0), from the committed prototype in `src/`.

Global constants (all experiments unless stated): covering threshold τ = 0.5 (τ = 0.75 robustness
arm); α ∈ {0.05, 0.1, 0.2} with α = 0.1 primary; image-level calibration/test split 50/50; ≥5 split
seeds; Clopper–Pearson 95% CIs on all rates plus image-level cluster bootstrap (objects within an
image are correlated — the bootstrap unit is the image).

---

## E0 — Prototype validation (DONE; MEASURED, synthetic)

**Status: complete and reproducible from this package.**

- 27/27 CPU tests pass (`python -m pytest src/tests/ -q`), including brute-force checks of IoU and
  greedy NMS, +∞-quantile behaviour of the conformal layer, and an **exact per-scene check of the
  CPS coverage-transfer theorem** (`test_suppression.py::test_theorem_coverage_transfer_exact`).
- Both committed configs run end-to-end (`python src/run_synthetic.py --config configs/default.yaml`,
  `--config configs/crowded_aggressive.yaml`); results tables in `proposal.md` §18.
- Purpose and limit: validates the machinery and demonstrates both K-regimes (footnote vs
  destruction) are *representable*. The generator was tuned to make both visible — E0 is evidence
  about code, not about the world.

## E1 — The killer experiment: blind-spot gate (GO/NO-GO)

**Question (H1).** What fraction of GT objects lose ALL covering candidates to standard NMS, and how
does it scale with crowdedness and NMS aggressiveness?

**Procedure.**
1. Freeze detector zoo (5–8 checkpoints: Faster R-CNN, RetinaNet, FCOS, one YOLO-family, ≥2
   DETR-family as no-NMS controls; exact checkpoints recorded in a frozen config on Day 1).
2. Cache pre-NMS candidate sets (boxes, scores, class logits; score floor as an axis, {0.01, 0.05})
   for COCO val2017, LVIS v1 val, CrowdHuman val. Validate the cache format on 1 detector × COCO
   first.
3. For every (detector × dataset × θ ∈ {0.3,0.4,0.5,0.6,0.7} × floor × stratum): compute per-GT
   {miss, blind} flags with `conformal_nms.blind_spot` logic (already tested); aggregate to the
   blind-spot table with CIs. Strata: per-image crowdedness (GT count / max pairwise GT IoU /
   same-class density, quartile bins, definitions frozen Day 1) and per-object size (COCO S/M/L) and
   LVIS frequency bins.
4. DETR-family arm: same table with their native top-k output as the "surviving pool" — the
   suppression-free control.

**Decision rule (pre-registered; from N/Q):**

| Worst deployed-plausible stratum blind rate | Decision |
|---|---|
| ≥ 5% | GATE OPENS → E2–E6 |
| 2–5% (crowded strata only) | SCOPE-STOP → E2–E6 restricted to crowded regime |
| < 1–2% everywhere (incl. crowded) | GATE FAILS → measurement note; program ends (proposal §20) |

"Deployed-plausible" = θ ∈ [0.3, 0.5] with standard score floors, on any real dataset stratum. The
conditional rate blind|detected is the tie-breaker when GT quality is contested (see E1-S below).

**Cost.** 2–4 GPU-days (caching) + CPU-days (analysis). **Prediction (HYPOTHESIS, no magnitude
claimed):** small on sparse COCO; materially larger in crowded strata at aggressive θ. The magnitude
IS the gate.

**E1-S — GT-quality sensitivity (runs with E1).** Recompute the table (a) excluding
ignore/crowd-flagged regions, (b) on the conditional blind|detected form, (c) on LVIS
exhaustive-annotation categories only. If any gate cell crosses the materiality boundary between
variants, the conditional table governs and the discrepancy is reported (proposal §25 tripwire).

## E2 — Coverage destruction on real caches (pipelines A and B)

**Question.** Does a split-conformal guarantee calibrated pre-NMS hold at nominal after deploy-NMS,
and does the gap track the blind rate?

**Procedure.** Per detector × dataset × stratum: calibrate pipeline A (keep-all) at α; evaluate
coverage on test split. Pipeline B: same q̂, pool = NMS survivors at deploy θ ∈ {0.3, 0.5}. Report
coverage gap vs nominal, z-scores, blind-stratum coverage (0 by construction — verified, not
assumed), and the per-stratum relation gap ≈ blind rate (the deterministic dominance bound of
proposal §10 makes this a consistency check, not a discovery).

**Falsifier for the framing:** if pipeline B holds nominal in all strata where E1 reported material
blind rates, the caches/analysis disagree internally → halt and debug before any claim.

## E3 — Calibrate-after-NMS and the achievability certificate (pipeline C)

**Question.** Where does SeqCRC-style post-NMS calibration silently condition away the loss, and
where does it certify unachievability (q̂ = +∞)?

**Procedure.** Calibrate on post-NMS pools; record q̂ finiteness, achievability cap
(1 − miss − blind on calibration split), marginal coverage, and blind-stratum coverage per stratum.
Then the full SeqCRC construction (their sequential risk-control form, reimplemented per paper) as
the honest version of the baseline — current pipeline C is its skeleton (EVIDENCE: labeled so in the
prototype).
**Expected (HYPOTHESIS):** q̂ = +∞ (or coverage pinned at cap) exactly in strata where
blind + miss > α; marginal coverage may look acceptable while blind-stratum coverage is 0 —
the "whose objects" table that anchors the paper's Act 2.

## E4 — CPS and the frontier (pipeline D vs everything; H2)

**Question.** Does CPS restore nominal coverage at set sizes/duplicate rates that beat
calibrate-after-NMS on the suppressed stratum and no-NMS IoU-aware calibration on size at matched
coverage?

**Arms.** D (CPS: grid κ ∈ {0.6, 0.7, 0.75, 0.8, 0.9} × r ∈ {1, 2, 3}); baselines: A (keep-all),
full SeqCRC (E3), WACV-2024 IoU-aware calibration no-NMS (reimplementation; K-MANDATED), soft-NMS
and class-aware NMS arms (as deploy suppressors under pipeline-B-style calibration AND as suppression
operators inside the prediction set), DETR-native top-k, trivial anchors (top-k per image; global
threshold sweep).

**Readouts.** Coverage (marginal + blind-stratum) vs mean set size vs duplicates-per-covered-GT, per
stratum and α; full frontier curves; the matched-coverage set-size comparison CPS vs WACV-2024 is the
H2 headline. **Success criterion (pre-registered, H2):** CPS ≥ nominal everywhere (theorem says it
must be — violation means a bug, since the guarantee is marginal over calibration randomness this is
checked in expectation across the ≥5 splits) AND strictly better than post-NMS calibration on
blind-stratum coverage AND smaller sets than WACV-2024 at matched coverage in ≥1 crowded stratum.
**Pivot trigger:** WACV-2024 dominates the whole frontier → characterization pivot (proposal §25).

## E5 — Consumability study (Reviewer-2 leftover)

**Question.** Is CPS output usable as *detections* rather than sets?
**Procedure.** At r = 1 and matched coverage: duplicates/GT, set size per image, and per-image excess
boxes vs (a) NMS output, (b) WACV-2024 output; qualitative panels of crowded scenes. Deliverable: the
drop-in `cps_nms()` artifact (proposal §26.7).

## E6 — Ablations (proposal §16, executed on the E4 substrate)

κ sweep; r budget; score floor; class-agnostic vs class-aware; calibration-set size (incl. q̂ = +∞
frequency near the cap); exchangeable unit (object-pooled vs image-level scene-max — if they disagree
materially, image-level becomes primary, pre-registered); suppression operator inside CPS (greedy-IoU
vs in-set soft decay); τ = 0.75 envelope (where τ_cal = τ + 1 − κ approaches 1 and CPS honestly
degrades); crowdedness-definition robustness (count vs IoU-based vs density strata).

## Statistical discipline (all experiments)

- Rates: Clopper–Pearson 95% CIs; comparisons across pipelines on identical test objects (paired).
- Correlation: image-level cluster bootstrap (1,000 resamples) for every headline number; both
  object-pooled and image-level units reported (proposal §10 caveat).
- Splits: image-level, ≥5 seeds; seed list frozen Day 1; per-seed tables in the appendix.
- Multiplicity: gate decision uses the pre-registered worst-stratum rule only — no post-hoc stratum
  shopping; all 1,440 gate cells are published regardless of outcome.
- No number from E0 (synthetic) may appear in any results section of the paper — mechanism figures
  only, labeled synthetic.

## Reporting map (experiment → paper asset)

| Experiment | Paper asset |
|---|---|
| E1 (+E1-S) | Table 1 blind-spot matrix; Fig. 1 blind rate vs θ per stratum — the gate figure |
| E2 | Fig. 2 coverage destruction vs blind rate (the dominance line) |
| E3 | Table 2 achievability caps + q̂ = +∞ map; blind-stratum coverage ("whose guarantee?") |
| E4 | Fig. 3 coverage/set-size frontier; Table 3 matched-coverage comparison (H2 headline) |
| E5 | Fig. 4 consumability; released `cps_nms()` artifact |
| E6 | Appendix ablation suite; τ = 0.75 envelope figure |
| E0 | Mechanism/schematic figures only (labeled SYNTHETIC), + released code |
