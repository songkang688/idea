# SeeingInside — Stage-7 Research Proposal (P14 / S-014 / S-604)

Windows4 · Idea_01 · Date: 2026-08-28 · Status: pre-experimental (no ACTUAL scientific results)

Epistemic labels used throughout:
`KNOWN FACT` (verifiable in code/paper/dataset card) · `EVIDENCE` (published measurement, Stage-3-verified) ·
`HYPOTHESIS` (ours, falsifiable) · `MODEL SPECULATION` (mechanistic guess) ·
`EXPECTED RESULT` (pre-registered prediction, not measured) · `ACTUAL EXPERIMENTAL RESULT` (measured by us; smoke tests only so far).

---

## 1. Title & Identifiers

**SeeingInside: How Much Image Evidence Does a Promptable Segmenter Use Inside a Tight Box?**
A null-calibrated, on-manifold counterfactual audit of box-prompted SAM.

- Project: P14 (Stage-4 Top-20 rank 1; Stage-6 lock Idea_01)
- Lineage: S-014 (ablate image evidence inside box, prompt fixed) + S-604 (patch-shuffle mutation)
- Process record: `Windows4/selection_history/` — stage3_kill_sam_eval.md Cluster 2 (SURVIVE),
  stage4_r2_setA.md P14 (WEAK ACCEPT conditional), stage4_top20.md rank 1, stage6_battle.md lock.

## 2. One-Sentence Claim

HYPOTHESIS: In the tight-box prompting regime — and most strongly in low-contrast medical
images evaluated under the MedSAM protocol — a substantial fraction of SAM's reported Dice
is reachable by mechanisms that use **no image evidence at all**, and SAM's own masks change
far less than they should when the image content inside the box is counterfactually replaced.

## 3. Abstract

Box prompts are the strongest prompt SAM accepts, and tight ground-truth boxes are the
standard protocol in medical SAM evaluation (KNOWN FACT: MedSAM-class evaluation uses
GT-derived boxes; Ma et al. 2024). A tight box is also, by itself, a powerful predictor of
the mask: it fixes location, scale, and extent. This proposal asks the causal question that
the prompt-perturbation literature (Stable-SAM; BREPS; RoBox-SAM — all perturb the *prompt*
with the image fixed) leaves open: **with the prompt held fixed, how much does the output
mask depend on the image evidence inside the box?** We answer it with on-manifold
counterfactuals — diffusion inpainting that removes the object, and object swaps that
replace it — so that every input we score is a natural image, immune to the off-manifold
ablation fallacy. We calibrate every number against three no-image-evidence nulls:
(i) a per-instance convexity-matched box-fill shape, (ii) prompt-only SAM (image embedding
replaced by a dataset-mean embedding), and (iii) a small learned box→mask regressor trained
without any image input. Primary endpoint: the fraction of MedSAM-protocol box-prompt Dice
reachable by the best no-image null, and the counterfactual sensitivity gap of SAM in the
low-contrast regime. Pre-registered kill condition: if intact-vs-counterfactual Dice gaps
exceed 15 points in every stratum, SAM "sees" everywhere, the interpolator claim dies, and
we publish nothing beyond a negative-result note.

## 4. Background & Motivation

- KNOWN FACT — SAM's promptable design: image encoder (ViT), prompt encoder, and a light
  mask decoder in which prompt tokens cross-attend to image embeddings; positional encodings
  are re-injected into the image-embedding side of cross-attention at every decoder layer
  (Kirillov et al. 2023, paper + released code). Consequence: even with degraded image
  features, the decoder retains a full positional scaffold — a reason to *expect* competent
  box-shaped masks without image evidence, and a reason off-manifold ablations alone cannot
  settle the question (this architectural point was Reviewer #2's attack (iii) and is now a
  design constraint).
- EVIDENCE — the prompt side is thoroughly studied: Stable-SAM analyzes which image features
  the decoder attends to under low-quality prompts (arXiv:2311.15776); BREPS shows output is
  a steep function of box coordinates with ~30% IoU drops under realistic boxes
  (arXiv:2601.15123); RoBox-SAM sweeps 0–30% box shifts across 5 medical modalities
  (arXiv:2407.21284); Cheng et al. document jitter-scale degradation (arXiv:2305.00035).
  **All of these perturb the prompt with the image fixed.** Nobody intervenes on the image
  evidence with the prompt fixed (Stage-3 assassination, Cluster 2: gap verified, verdict
  SURVIVE).
- EVIDENCE — box-geometry priors are real in fine-tuned models: box-fine-tuned MedSAM
  decoders "learned to expect" box geometry, imposing rigid rectangular constraints on
  irregular lesions (arXiv:2606.04705).
- EVIDENCE — tight-box medical evaluation is the deployed protocol, and medical images are
  the low-contrast regime where SAM is weakest (Ma et al. 2024; Mazurowski et al. 2023;
  Huang et al. 2024, arXiv:2304.14660; He et al., arXiv:2304.09324: relative target size and
  contrast dominate SAM Dice).
- HYPOTHESIS — if a tight box on a convex, low-contrast object is a near-sufficient
  statistic for the mask, then reported box-prompt Dice conflates "the model segments" with
  "the prompt already encodes the answer." No published number currently separates the two.

## 5. Problem Statement & Research Questions

Let `f(I, b)` be a promptable segmenter (frozen SAM), `I` an image, `b` a tight box prompt,
`m = f(I, b)` the output mask, `g` the GT mask.

- **RQ1 (reliance):** How much does `m` change under counterfactual replacement of the image
  content inside `b`, with `b` fixed? (Counterfactual Sensitivity Gap, §15)
- **RQ2 (null calibration):** What fraction of `Dice(m, g)` is reachable by mechanisms with
  no access to `I`? (Null-Reachable Fraction, §15)
- **RQ3 (regime map):** How do RQ1/RQ2 vary with object contrast, convexity, size, and box
  padding — natural (COCO) vs low-contrast medical (MedSAM protocol)?
- **RQ4 (tracking):** When a different object is swapped into the box, does the mask track
  the new evidence, or persist as a box-shaped prior?

## 6. Hypotheses (pre-registered)

- **H0 (SAM sees):** Removing/replacing in-box evidence collapses or redirects the mask;
  intact-vs-counterfactual Dice gap > 15 points in all strata; no-image nulls sit far below
  intact Dice. → Interpolator claim dead (pre-registered kill, §20).
- **H1 (regime-dependent interpolation — our primary bet):** In low-contrast medical
  instances with tight boxes, SAM behaves as a box→mask interpolator: counterfactual gap
  ≤ 5 Dice points, learned no-image null reaches ≥ 90% of intact Dice, and swap masks fail
  to track swapped-in content — while high-contrast natural instances show H0 behavior.
- **H2 (global interpolation):** Interpolator behavior everywhere, including COCO.
  MODEL SPECULATION: unlikely given SAM's demonstrated point-prompt ability; we do not bet
  on H2, but the design detects it.

Verdict logic per stratum requires **conjunction** (all four): small counterfactual gap ∧
swap-tracking failure ∧ null reaches intact Dice ∧ secondary off-manifold checks agree (§15).

## 7. Key Insight

Prior work asks "how wrong can the prompt be before the mask breaks?" We ask the inverse
causal question: "with a perfect prompt, does the image matter?" The instrument that makes
the question answerable — and survived Reviewer #2 — is **on-manifold counterfactuals**:
inpaint the object out or swap another object in, so the decoder only ever sees natural
inputs, and the comparison is *evidence-present vs evidence-absent*, not
*natural vs corrupted*. The interpolator claim is then not an interpretation of an ablation;
it is a measured equivalence: SAM-on-counterfactual ≈ SAM-on-intact ≈ learned-no-image-null,
plus a demonstrated failure to track swapped-in evidence.

## 8. Novelty Statement

EVIDENCE (Stage-3, web-verified 2026-08-28): all published perturbation studies of box-prompted
SAM perturb the prompt (Stable-SAM, BREPS, RoBox-SAM, Cheng et al., FNPC) or document
box-geometry artifacts post-fine-tuning (arXiv:2606.04705). The direct causal intervention on
image evidence with prompt fixed is unrun ("Exact remaining difference … That is a different
experiment and a different claim" — stage3_kill_sam_eval.md, Cluster 2). The null-calibration
methodology (per-instance convexity-matched nulls + prompt-only forward + learned no-image
regressor) is likewise absent from the SAM-eval literature (Stage-3 Cluster 12 found the
box-fill-null figure missing even in size-floor studies). Novelty confidence 4/5 per Stage 3.

## 9. Relation to Prior Work (differentiation)

| Prior work | What it did | What it did NOT do (us) |
|---|---|---|
| Stable-SAM (arXiv:2311.15776) | Decoder attention analysis under degraded prompts | No intervention on image evidence; prompt-side only |
| BREPS (arXiv:2601.15123) | Realistic-box distributions; worst-case box search; IoU heatmaps over box placement | Image fixed always; no null models |
| RoBox-SAM (arXiv:2407.21284) | 0–30% box-shift sweeps, 5 modalities; attention drift under bad boxes | Same: prompt perturbation only |
| MedSAM box-predictor note (arXiv:2606.04705) | Documents box-shaped-mask artifacts in box-fine-tuned decoders | Observational; no counterfactual; fine-tuned models only |
| He et al. (arXiv:2304.09324), Mazurowski et al. (MedIA 2023), Huang et al. (arXiv:2304.14660) | Size/contrast-stratified SAM medical evals under GT-box protocol | No no-image null; Dice reported as if all of it were "segmentation" |
| FNPC (arXiv:2308.10382) | Box sensitivity on ultrasound + multi-box augmentation | Remedy work, prompt-side |
| Kirillov et al. (arXiv:2304.02643) | SAM design; positional re-injection in decoder | States design; never measures image-evidence reliance |
| P107v / HalluSegBench lineage | Counterfactual *hallucination* benchmark for VLM-driven segmentation | Different model class, different claim; see §23 — explicitly not merged |

## 10. Significance — who is wrong if we are right

If H1 holds: (a) every MedSAM-protocol evaluation number (EVIDENCE: the dominant medical-SAM
evaluation convention) overstates *segmentation* ability by the null-reachable fraction —
the papers are not wrong about Dice, they are wrong about what Dice measures; (b) tight-box
medical benchmarks need a mandatory no-image-null reporting arm (we provide the tool);
(c) "SAM adapts to modality X with boxes" claims must show gains *above the null line*, not
above zero. If H0 holds everywhere: the field gets a pre-registered, null-calibrated
demonstration that SAM genuinely consults image evidence even in its weakest regime — a
clean negative worth one short note, not a flagship (per Stage-3 kill condition). The
asymmetric-payoff attack (Reviewer #2 point iv) is answered by making the medical regime
primary: there, *either* branch changes how published numbers are read, because the protocol
under audit is the deployed one.

## 11. Method Overview

Framework: **null-calibrated counterfactual evaluation**, entirely frozen-model, eval-only.

For each instance (I, g, b) with b the tight GT box (+ padding sweep):

1. **Intact forward:** m_intact = f(I, b).
2. **Primary counterfactuals (on-manifold, §12):** object-out inpainting I_out; object-swap
   I_swap (with the inserted object's mask s_new known by construction). Forward with the
   SAME b: m_out = f(I_out, b), m_swap = f(I_swap, b).
3. **No-image nulls (§13):** box-fill rectangle; per-instance convexity-matched fill;
   prompt-only SAM (dataset-mean image embedding); learned box→mask regressor.
4. **Secondary convergence checks (off-manifold, demoted per R2):** patch-shuffle inside box
   (S-604); embedding-mean replacement inside box (S-014 softened from zeroing);
   luminance-matched noise interior.
5. **Readouts (§15):** counterfactual sensitivity, persistence, swap tracking,
   null-reachable fraction — stratified by contrast × convexity × size × padding.

Everything is a forward pass or a tiny regressor: no SAM training, no pretrain (rubric-compliant).

## 12. Interventions (counterfactual instruments)

**Primary (on-manifold; the claim rests on these):**

- **Object-out inpaint:** mask the GT object region (dilated by d px, d pre-registered),
  inpaint with an off-the-shelf diffusion inpainter conditioned on "background continuation";
  reject-and-resample any counterfactual whose in-box region is flagged non-natural by a
  quality screen (LPIPS-to-context + human spot check on 10%). Box b unchanged.
  NOTE on tooling: the specific inpainting model is chosen at run time; under Windows4
  citation policy (§25 of `literature.md`) we do not cite an inpainting paper here because
  none appears in the Stage-3 verified list — the tool citation will be added when selected.
- **Object-swap:** paste a different object (from another instance of a different class,
  geometry-fit to the box; alpha-blended, then the same inpainting model harmonizes the
  seam) into the box; s_new recorded. Box b unchanged.
- **Fallback instrument (prototype + robustness check):** classical inpainting
  (Telea / Navier–Stokes via OpenCV) — cheaper, less natural; used in the prototype and as a
  sensitivity check that conclusions do not depend on one generative model.

**Secondary (off-manifold; convergence checks only — never headline):**

- **Patch-shuffle inside box** (S-604): permute 16-px-aligned patches within the box.
- **Embedding-mean inside box** (S-014, softened): replace image-embedding vectors whose
  receptive centers fall inside b with the dataset-mean embedding (not zeros — zeros are
  maximally off-manifold; Reviewer #2 point ii).
- **Luminance-matched noise interior:** matched mean/variance noise inside b.

Padding sweep {0, 4, 8, 16 px} runs on all conditions. R2's confound note (padding conflates
prompt informativeness with ablated area) is answered by **decoupling**: the ablated region
is always the GT-object region (fixed), while padding varies only the *prompt*; a separate
arm varies ablated-region dilation at fixed padding (§18).

## 13. Null Models & Baselines

| Null / baseline | Uses image? | Purpose |
|---|---|---|
| Box-fill rectangle | No | Literal interpolator floor (Stage-3 Cluster 12 obligation) |
| **Convexity-matched fill** (per instance: fill = box ∩ scaled convex prior matched to instance solidity) | No | Removes the convexity confound: compares SAM to the best *shape-prior* guess for that instance class, not to a global rectangle (R2 missing-baseline 3) |
| **Prompt-only SAM**: f(Ī, b) with Ī the dataset-mean image embedding | No (mean only) | "The interpolator claim in one number" — what does SAM's decoder emit from box + positional scaffold alone? (R2 missing-baseline 1) |
| **Learned box→mask null**: tiny regressor (box geometry + dataset id → 64×64 mask logits, upsampled), trained on the same split, never sees pixels | No | If this matches ablated-SAM, "interpolation" is a property of label statistics, not of SAM (R2 missing-baseline 2) |
| Oracle-threshold stub (prototype only) | Yes | Positive control for the decision logic: a model that genuinely "sees" must be classified as seeing |
| SAM point-prompt arm | Yes | Cross-prompt control: point prompts carry far less geometry; reliance should be visibly higher if the framework is sound |

## 14. Datasets

- **Natural:** 500 COCO val2017 instances, stratified sample over (convexity/solidity
  quartile × relative-size quartile × in-box RMS contrast quartile). KNOWN FACT: COCO masks
  are polygon-based with documented quality issues (COCO-ReM, arXiv:2403.18819) — boundary-F
  is therefore secondary on COCO.
- **Medical (PRIMARY endpoint):** 500 low-contrast instances drawn from public datasets used
  in MedSAM-protocol evaluations (Ma et al. 2024; Mazurowski et al. 2023; Huang et al.
  arXiv:2304.14660 cohorts guide the selection — e.g., abdominal CT organs/lesions and
  breast ultrasound; final list fixed and frozen before any SAM forward pass, recorded in
  `configs/`). Selection criterion is pre-registered: in-box RMS contrast in the lowest two
  deciles of the source dataset.
- **Synthetic (prototype + E0 logic validation only):** controllable shapes dataset
  (`src/dataset.py`): ellipses/blobs/polygons with parametric convexity, contrast, size;
  never used for scientific claims.
- Medical inpainting caveat → §21 (naturalness screening is harder on CT/US; the fallback
  instrument and the swap arm carry more weight there).

## 15. Metrics & Statistical Analysis

Per instance, Dice D(·,·) primary; IoU and boundary-F secondary.

- **CSG (Counterfactual Sensitivity Gap):** D(m_intact, g) − D(m_out, g)... reported
  alongside **Persistence** P = D(m_out, m_intact): high P with the object absent = the mask
  survives without its evidence. (CSG alone is confounded when g ≈ box; P is not.)
- **Swap-Tracking Score:** T = D(m_swap, s_new) vs T_null = D(null shape, s_new). Tracking
  failure ⇔ T − T_null ≤ τ2.
- **NRF (Null-Reachable Fraction):** max over no-image nulls of D(null, g) / D(m_intact, g),
  per instance; medical primary endpoint = median NRF under the MedSAM protocol.
- **Prompt-only gap:** D(m_intact, g) − D(f(Ī, b), g).
- **Interpolator verdict (per stratum), pre-registered conjunction:**
  median CSG ≤ τ1 (5 Dice pts) ∧ median (T − T_null) ≤ τ2 (5 pts) ∧ median NRF ≥ τ3 (0.90)
  ∧ secondary checks directionally consistent (sign agreement on CSG).
- **Statistics:** paired per-instance design; BCa bootstrap 95% CIs (10k resamples);
  Wilcoxon signed-rank for paired condition contrasts; Holm correction across strata;
  pre-registered regression of CSG on {contrast, solidity, log size, padding} with dataset
  fixed effects. Thresholds τ1–τ3 are frozen in `configs/default.yaml` before any real-SAM run.

## 16. Killer Experiment (pre-registered; run first)

**E1 — "Inpaint-out vs nulls, medical-first"** (full card in `experiments.md`):
500 medical + 500 COCO instances × conditions {intact, object-out, object-swap, box-fill,
convexity-matched, prompt-only, learned-null} × padding {0,4,8,16 px}, frozen SAM ViT-H
(replicate key cells with ViT-B). Compute: forward passes + one tiny-regressor training —
single GPU, ≈ 2–3 GPU-days including the diffusion inpainting.
**Kill condition (Stage-3, binding):** if intact-vs-counterfactual Dice gap > 15 points in
*every* stratum, SAM sees; the interpolator claim dies; publish the null-calibrated
sensitivity curve only if the low-contrast regime shows interpolator behavior — otherwise a
negative-result note and stop.
**Success condition:** H1 conjunction (§15) holds in the low-contrast medical stratum.

## 17. Full Experimental Program

E0 pipeline-logic validation (stubs, synthetic; ACTUAL, non-scientific) → E1 killer
(above) → E2 secondary convergence checks (patch-shuffle, embedding-mean, noise) →
E3 regime map (contrast × convexity × size surfaces) → E4 prompt decoupling (padding vs
ablation-dilation; point-prompt arm) → E5 model generality (ViT-B/L/H; MedSAM checkpoint;
SAM-2 image mode if time permits) → E6 instrument robustness (diffusion vs classical
inpainting; inpainter swap) → E7 evidence-tracking deep dive (swap-content gradient:
same-class vs other-class vs texture-only swaps). Cards with per-experiment kill conditions:
`experiments.md`.

## 18. Ablations & Controls

- Inpainting-quality control: reject-and-resample screen + report results with/without
  screening; 10% human audit.
- Ablation-extent control: dilate the ablated region {0, 8, 16 px} at fixed padding —
  separates "how much was changed" from "how informative is the prompt" (answers R2
  confound on the padding sweep).
- Convexity control: all null comparisons per-instance matched; global box-fill reported
  only as the floor.
- Seam-artifact control: sham-inpaint arm — inpaint a *background* region of equal area
  outside the box, object untouched; any Dice movement bounds the artifact contribution.
- Multimask control: single-mask output head fixed; multimask + IoU-head selection reported
  as a sensitivity row (head selection is a known confound; cf. Stage-4 P101 review).
- Checkpoint control: ViT-B vs ViT-H; box-fine-tuned MedSAM (EVIDENCE: box-geometry priors
  are stronger post-fine-tuning, arXiv:2606.04705 — EXPECTED: NRF higher for MedSAM).

## 19. Expected Results (all EXPECTED RESULT — no measurements exist)

- EXPECTED: COCO high-contrast stratum shows H0 behavior — CSG large (>15 pts), swap masks
  track content. This is the sanity stratum; failure here indicts the instrument, not SAM.
- EXPECTED (primary bet): low-contrast medical stratum shows median NRF ≥ 0.9 and small CSG;
  learned null approaches intact Dice within a few points; prompt-only SAM emits box-shaped
  masks with surprisingly competitive Dice.
- EXPECTED: NRF increases monotonically as in-box contrast decreases and solidity increases;
  padding 0→16 px lowers null Dice faster than intact Dice (prompt informativeness decays).
- EXPECTED: box-fine-tuned MedSAM shows higher NRF than base SAM at matched instances.
- MODEL SPECULATION: secondary off-manifold probes will *overstate* reliance relative to
  on-manifold counterfactuals (off-manifold inputs push the decoder toward its positional
  prior), which is precisely why they are demoted.
- ACTUAL EXPERIMENTAL RESULT (smoke test only, synthetic data, stub models — no scientific
  content): the E0 harness classifies the BoxFillBaseline stub as "interpolator" and the
  OracleThreshold stub as "seeing" — decision logic verified end-to-end. See
  `experiments.md` §E0 for the recorded output.

## 20. Falsifiability & Kill Conditions

- **Global kill (binding, Stage-3):** intact-vs-counterfactual gap > 15 Dice points in every
  stratum → claim dead; negative note; stop. Detectable within E1 (week-1 scale).
- **Instrument kill:** if the sham-inpaint control moves Dice by more than τ1/2, the
  inpainting instrument is confounded → fall back to swap-only + classical-inpaint
  convergence; if those disagree, report instrument failure and stop.
- **Null-model kill:** if the learned box→mask null beats intact SAM on medical (NRF > 1
  broadly), the *benchmark protocol* is degenerate beyond SAM — pivot the paper to a
  protocol audit (still publishable; smaller claim; pre-registered as pivot-1).
- **Conjunction discipline:** no single small gap is ever reported as "interpolation";
  the four-way conjunction (§15) is the only licensed verdict.

## 21. Confounders & Mitigations

| Confounder (source) | Mitigation |
|---|---|
| Object convexity drives both null and intact scores (R2) | Per-instance convexity-matched nulls; solidity as regression covariate; stratified reporting |
| Global ViT attention leaks in-box corruption everywhere (R2 point ii) | Primary interventions are natural images — global influence is then *legitimate evidence flow*, not artifact; off-manifold probes demoted |
| Positional-scaffold degeneracy (R2 point iii) | Prompt-only null makes the scaffold's contribution an explicit measured number instead of a hidden artifact |
| Padding conflates prompt info and ablated area (R2) | Decoupled sweeps (§18) |
| Inpainting seams / distribution shift | Quality screen + sham-inpaint control + two inpainting instruments |
| Task degeneracy alternative ("tight boxes are near-sufficient statistics") (R2 hidden assumption) | That alternative is *measured*, not denied: it is exactly what NRF quantifies; the claim is rephrased as "the protocol's information content", licensed by the learned null |
| COCO GT noise | Boundary-F secondary on COCO; medical primary |
| Multimask head selection | Fixed head primary; selection as sensitivity row |

## 22. Reviewer #2 Compliance Matrix (binding obligations → design)

| R2 requirement (stage4_r2_setA.md, P14) | Where satisfied |
|---|---|
| (a) On-manifold counterfactuals primary (inpaint-out / swap-in, box fixed) | §12 primary instruments; E1 |
| (b) Embedding-zeroing / patch-shuffle demoted to secondary convergence checks | §12 secondary; E2 only; never headline |
| (c) Prompt-only null + learned box→mask null, convexity-matched per instance | §13; `src/model_sam.py`, `src/train.py` |
| (d) Low-contrast medical as primary endpoint; report fraction of MedSAM-protocol Dice reachable by no-image null | §14, §15 NRF; E1 medical-first |
| Swap arm: masks must fail to track swapped-in content for the claim to stand | §15 Swap-Tracking; E7 |
| Per-instance convexity-matched box-fill null (not global) | §13 |
| Coordination with P107v | **Superseded by Stage-6 supervisor ruling: no merge** — see §23 |

## 23. Scope Boundaries (non-merge with P107v / HalluSegBench)

Stage-6 ruling (KNOWN FACT, `stage6_battle.md`): Set-A R2 suggested merging P14 with P107v
(inpaint-object-out shared instrument); Set-C found P107v **scooped by HalluSegBench**; the
supervisor ruled **do not merge**. Boundary enforced in this package: SeeingInside intervenes
on *pixels inside a box prompt* to measure *evidence reliance of a promptable segmenter's
mask decoder*. It makes **no** claim about vision-language grounding, hallucination,
counterfactual *benchmarking* of VLM segmenters, or language-conditioned behavior; it
introduces no text prompts; it does not evaluate on, compare to, or extend HalluSegBench.
Shared machinery (a diffusion inpainter) is a tool, not a thesis. Any reviewer mapping this
to HalluSegBench is answered by the claim object: reliance measurement with nulls for
box-prompted SAM vs hallucination benchmark for language-driven segmentation.

## 24. Compute & Resource Budget

- E0: CPU, minutes (runs in this repo today).
- E1: ~1000 instances × ~28 condition-cells, forward-only ≈ 30k SAM forwards (≤ 1 GPU-day
  ViT-H on one A100/4090) + diffusion inpainting ≈ 2000 images (≈ 1 GPU-day) + learned null
  training (< 1 GPU-hour). Total ≈ 2–3 GPU-days.
- E2–E7: ≈ 4–6 additional GPU-days. Whole program ≤ 10 GPU-days, single-GPU lab scale
  (rubric: feasibility 5/5, compute cost low; killable in < 1 GPU-week).
- Storage: < 50 GB (counterfactual image cache).

## 25. Reproducibility & Release Plan

- All thresholds, strata, dataset freezes, and seeds in version-controlled configs
  (`configs/default.yaml`) committed **before** the first real-SAM forward (this commit).
- Deterministic seeding throughout (`src/utils.py`); per-instance results emitted as
  CSV + JSON; figures regenerable from artifacts.
- Release: code (this `src/`), counterfactual generation scripts, frozen instance lists,
  per-instance raw Dice tables, and the null-model checkpoints. Inpainted medical images
  released as deltas/scripts if license forbids redistribution (§27).
- The prototype's stub backend guarantees the harness is runnable by any reviewer with no
  GPU and no weights.

## 26. Risks & Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Diffusion inpainting unnatural on CT/US | Medium-high | Modality-specific inpainters at run time; classical-inpaint convergence arm; swap arm weighted higher on medical; sham-inpaint bound |
| Result is H0 everywhere (claim dies) | Real (Stage-3 conceded) | Pre-registered kill = cheap, fast exit (< 1 week); backup projects P063/P079 named in `roadmap.md` |
| "Priced-in" objection: BREPS already discredited tight boxes on natural images | Certain to be raised | Medical-primary framing: the audited protocol is the deployed one (R2 accepted this answer); natural stratum is the control, not the claim |
| Scoop risk on the counterfactual instrument | Medium (HalluSegBench adjacency) | Different claim object (§23); move fast: E1 is week-1 |
| GT-box leakage debate (GT-derived boxes are themselves oracle prompts) | Known critique (Stage-3 Cluster 1 killed oracle-protocol *papers*) | We do not propose an eval protocol; we audit the existing one — orthogonal claim |
| Learned null overfits tiny medical splits | Medium | Cross-validated training; capacity cap (<100k params); report train/val gap |

## 27. Ethical & Data Considerations

- All datasets public and licensed for research (COCO; public MedSAM-suite medical sets);
  no PHI beyond what dataset releases already de-identified; no new human data collected.
- Counterfactual medical images are synthetic edits: released only as scripts + hashes where
  redistribution is restricted; clearly watermarked "synthetic — not for clinical use".
- Dual-use: low. The result, if positive, *increases* safety by exposing inflated clinical
  segmentation numbers.
- Compute footprint ≤ 10 GPU-days — negligible.

## 28. Deliverables, Publication Plan & Decision Tree

- **Deliverables:** (1) null-calibrated reliance audit paper (target: CVPR/ICCV-class or
  MICCAI if medical-led story dominates); (2) open-source auditing harness (this repo) with
  a drop-in "no-image-null reporting arm" any benchmark can adopt; (3) frozen counterfactual
  instance lists as a reusable probe set.
- **Decision tree:**
  1. Run E0 (done, stub-level) → E1 medical-first.
  2. E1 shows H1 conjunction in medical → full program E2–E7 → flagship paper.
  3. E1 shows H0 everywhere → binding kill: negative note; escalate backups
     (P063 RefractionFeatures / P079 MemoryProbe per `stage4_top20.md`).
  4. Instrument kill triggers → swap-only fallback; if still confounded, report and stop.
  5. NRF > 1 broadly → pivot-1: protocol-degeneracy audit paper.
- **Authorship/effort split** (single-lab): counterfactual generation; SAM harness + nulls;
  medical data curation; statistics + writing. All four workstreams are independent until E1
  integration.

---
*Process lineage: Stage-3 SURVIVE → Stage-4 WEAK ACCEPT (rank 1) with binding redesign →
Stage-6 lock as Idea_01 (no P107v merge) → this Stage-7 package. No fabricated citations;
no fabricated numbers; all forward-looking statements tagged EXPECTED or HYPOTHESIS.*
