# SeeingInside — Experiment Cards

All thresholds referenced here are frozen in `configs/default.yaml` (τ1 = 0.05 Dice,
ρ = 0.85 persistence, τ2 = 0.05 tracking delta, τ3 = 0.90 NRF, global kill = 0.15 Dice).
`src/config.py` refuses runtime overrides of any threshold. Tags:
EXPECTED RESULT = pre-registered prediction; ACTUAL EXPERIMENTAL RESULT = measured, with
provenance. **The only ACTUAL results in this file are E0 harness smoke tests (stub models,
synthetic data). No SAM has been run. Nothing here supports a scientific claim about SAM.**

---

## E0 — Decision-logic validation (stubs, synthetic) — STATUS: RUN, PASSED

**Question.** Does the harness classify a known interpolator as "interpolator" and a known
pixel-consulting model as "seeing", using only the pre-registered conjunction?

**Design.** 60 synthetic instances (2×2 strata: contrast {low 0.06, high 0.35} × solidity
{high, low}), two stub models: `BoxFillBaseline` (negative control — a literal box→mask
interpolator) and `OracleThresholdBaseline` (positive control — Otsu inside the box, so it
genuinely consults pixels). Conditions: intact, object-out (exact synthetic background +
Telea-inpaint variant), object-swap, sham-inpaint, patch-shuffle (secondary),
matched-noise (secondary). Nulls: box-fill, convexity-matched fill, learned box→mask
regressor (83k params, trained on a disjoint seed range, `src/train.py`).

**Pass criteria (pre-registered in `src/eval.py::e0_assertions`):**
box-fill stub → "interpolator" in ALL strata; oracle stub → "seeing" in ≥ 1 stratum.

**ACTUAL EXPERIMENTAL RESULT (smoke test; artifacts committed at
`artifacts/e0_smoke/{summary.md,verdicts.json,results.csv}`; reproduce with
`python -m src.train --config configs/default.yaml && python -m src.eval --config configs/default.yaml`):**

| model :: stratum | n | Dice intact | CSG | persist. | trackΔ | NRF | verdict |
|---|---|---|---|---|---|---|---|
| boxfill_stub :: high-contrast/high-solidity | 15 | 0.880 | 0.000 | 1.000 | −0.116 | 1.122 | interpolator |
| boxfill_stub :: high-contrast/low-solidity | 15 | 0.819 | 0.000 | 1.000 | −0.171 | 1.089 | interpolator |
| boxfill_stub :: low-contrast/high-solidity | 15 | 0.870 | 0.000 | 1.000 | −0.121 | 1.133 | interpolator |
| boxfill_stub :: low-contrast/low-solidity | 15 | 0.807 | 0.000 | 1.000 | −0.185 | 1.122 | interpolator |
| oracle_threshold_stub :: high-contrast/high-solidity | 15 | 1.000 | 0.414 | 0.586 | +0.157 | 0.988 | seeing |
| oracle_threshold_stub :: high-contrast/low-solidity | 15 | 1.000 | 0.405 | 0.595 | +0.153 | 0.893 | seeing |
| oracle_threshold_stub :: low-contrast/high-solidity | 15 | 0.746 | 0.177 | 0.664 | −0.199 | 1.324 | seeing |
| oracle_threshold_stub :: low-contrast/low-solidity | 15 | 0.769 | 0.153 | 0.784 | −0.127 | 1.169 | seeing |

E0 checks: `boxfill_stub_all_interpolator = PASS`, `oracle_stub_seeing_somewhere = PASS`,
**E0_PASS = PASS**.

**Reading (about the harness, not about SAM):** the two controls separate exactly as
designed — the interpolator signature is (CSG = 0, persistence = 1, tracking failure,
NRF ≥ 1) and the seeing signature is (large CSG, low persistence, positive tracking at
high contrast). Note the oracle's tracking delta goes negative in low-contrast strata —
an honest preview of why the conjunction, not any single metric, is the verdict. Also
note NRF > 1 for the box-fill stub: the GT-informed convexity-matched null beats a
rectangle, as it must.

**Instructive detail (ACTUAL, smoke test):** the first oracle implementation used a
"foreground = minority side" polarity rule and scored Dice ≈ 0 inside *tight* boxes,
where the object is the majority — fixed to a border-ring background reference. Recorded
here because it is exactly the class of harness bug that could silently corrupt E1;
E0 caught it, which is E0's job.

---

## E1 — KILLER: on-manifold counterfactuals vs no-image nulls, medical-first — STATUS: NOT RUN

**Question.** RQ1/RQ2: with tight boxes fixed, how much does SAM's mask depend on image
evidence, and what fraction of protocol Dice do no-image nulls reach?

**Design (proposal §16).** 500 low-contrast medical (MedSAM-protocol datasets, frozen
list, lowest-two contrast deciles) + 500 COCO instances (stratified) × conditions
{intact, object-out (diffusion inpaint), object-swap, sham-inpaint, box-fill,
convexity-matched, prompt-only, learned-null} × padding {0, 4, 8, 16 px}. Frozen SAM
ViT-H primary, ViT-B replication. Backend: `OfficialSAMWrapper`; prompt-only via
`PromptOnlySAMNull` with a cohort-mean embedding (`compute_mean_embedding`).

**Pre-registered outcomes.**
- GLOBAL KILL (binding, Stage-3): median CSG > 0.15 in EVERY stratum → SAM sees; claim
  dead; negative note; escalate backups (roadmap.md).
- INSTRUMENT KILL: sham-inpaint |ΔDice| > τ1/2 → swap-only fallback; if diffusion and
  classical instruments disagree on verdicts → report instrument failure, stop.
- H1 SUCCESS: interpolator conjunction holds in the low-contrast medical stratum.
- PIVOT-1: NRF > 1 broadly on medical → protocol-degeneracy audit re-scope.

**EXPECTED RESULT (prediction, not evidence):** H1 — interpolator regime in low-contrast
medical; seeing regime on high-contrast COCO. EXPECTED: prompt-only SAM emits box-shaped
masks with non-trivial Dice (the positional-scaffold number, R2 attack iii made
measurable).

**Cost.** ≈ 30k SAM forwards + 2k inpaintings + <1 GPU-h null training ≈ 2–3 GPU-days.

---

## E2 — Secondary convergence checks (off-manifold, demoted) — STATUS: NOT RUN

Patch-shuffle (S-604), interior embedding-mean replacement
(`predict_with_interior_mean_embedding`, S-014 softened), matched-noise interior — same
instances as E1. Role: the c4 consistency row of the verdict conjunction ONLY; never
headline (binding R2 obligation). EXPECTED: off-manifold probes overstate reliance
relative to on-manifold counterfactuals (MODEL SPECULATION, flagged as such in proposal §19).
Kill condition: none — E2 cannot kill the claim, only annotate primary/secondary
discrepancies.

## E3 — Regime map — STATUS: NOT RUN

CSG/persistence/NRF surfaces over contrast × solidity × size; pre-registered regression
(proposal §15) with dataset fixed effects. EXPECTED: NRF rises as contrast falls and
solidity rises (monotonicity pre-registered; failure = reportable surprise, not silence).

## E4 — Prompt/ablation decoupling — STATUS: NOT RUN

(a) padding sweep at fixed ablation; (b) ablation-dilation sweep {4, 8, 16 px} at fixed
padding; (c) loose/realistic-box arm; (d) point-prompt arm. Answers the R2 padding
confound; EXPECTED: NRF decreases with padding and with looser boxes; point-prompt
reliance ≫ box-prompt reliance. Kill condition: if (a) and (b) interact so strongly that
CSG is not interpretable at the primary padding, the E1 verdict is re-derived per padding
and reported as a family.

## E5 — Model generality — STATUS: NOT RUN

ViT-B/L/H, MedSAM checkpoint, (optional) SAM-2 image mode. EXPECTED: box-fine-tuned
MedSAM shows higher NRF than base SAM (direction from arXiv:2606.04705's box-geometry
prior evidence). Either outcome reported.

## E6 — Instrument robustness — STATUS: NOT RUN

Second diffusion inpainter + classical (Telea/NS) arm on the full set; verdict-level
agreement matrix. Kill condition: cross-instrument verdict disagreement → instrument
failure declared (this is the E1 INSTRUMENT-KILL, run at scale).

## E7 — Evidence-tracking gradient — STATUS: NOT RUN

Swap-content gradient: same-class swap / other-class swap / texture-only fill. EXPECTED:
tracking score falls monotonically along the gradient if SAM reads content; flat tracking
at null level across the gradient is the strongest interpolator signature. Feeds the
paper's qualitative figure set.

---

## Provenance rules

1. A number enters `proposal.md` or the paper only if it exists in a committed
   `artifacts/*/results.csv` (per-instance) + `verdicts.json` (aggregate).
2. EXPECTED → ACTUAL tag flips happen in the same commit as the artifact.
3. Stub-backend outputs are permanently quarantined to E0 and never aggregated with
   real-SAM outputs (`model` column + backend field make mixing detectable).
