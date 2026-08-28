# PromptAmnesia — Full Research Proposal (Stage 7, Windows4 / Idea_02)

**Epistemic status of this document:** RESEARCH PROPOSAL. Every statement is tagged
KNOWN FACT / EVIDENCE / HYPOTHESIS / MODEL SPECULATION / EXPECTED RESULT.
**No section of this package contains an ACTUAL EXPERIMENTAL RESULT. No metric value below is a
measurement; numeric values are design parameters, pre-registered thresholds, or compute ESTIMATES.**

---

## 1. Package identity and lineage

- **Windows:** Windows4 · **Idea slot:** Idea_02 · **Codename:** **PromptAmnesia**
- **Core paper:** P065 = C1-065 (prompt-type-specific forgetting) + C1-061 (multimask ambiguity/diversity
  collapse), absorbing C1-063 (click-depth), C1-071 (negative-click), C1-074 (cross-modal harm), A1-109
  (negative-click-first ordering), S-176 (protocol forgetting boxes→points, mutated per Stage 3).
- **Gate (runs FIRST):** P082 = C1-082 (threshold artifact) + S-183 (low-plasticity noise floor).
- **Mechanism arm:** P177 = S-177 (forgetting locus decoder vs encoder) + C1-062 (cross-attention
  re-splice restoration), **with mandatory stitching controls and α-interpolation baselines**.
- **Stage lineage:** Stage 1 `stage1_C1.md`/`stage1_A1.md`/`stage1_supervisor_seed.md` → Stage 2 keep +
  C1-audit merge ruling (C1-065 umbrella) → Stage 3 `stage3_kill_peft_vlm.md` (C1-065 SURVIVE as cluster
  core; S-176 MUTATE-merged; S-177/C1-062 SURVIVE conditional; C1-082/S-183 SURVIVE as gatekeeper) →
  Stage 4 `stage4_r2_setB.md` (P065 WEAK ACCEPT, P177 WEAK ACCEPT, P082 WEAK ACCEPT run-first;
  P110 REJECT → panel folded into this paper's appendix; P108 REJECT → drift logged as free covariate) →
  Stage 4 `stage4_top20.md` rank 2 → Stage 6 `stage6_battle.md` locked as **Idea_02**.
- **Binding obligations (from Stage 4/6, restated as contract):**
  1. The paper lives in the **mixed-prompt FT column** — the box-only column alone proves nothing.
  2. Diversity claims live in the **oracle-best-of-3 vs IoU-head-argmax decomposition**.
  3. P177 is included ⇒ **stitching controls + per-module α-interpolation are mandatory**, both swap directions.
  4. **P082 runs first** — symmetric threshold tuning, released checkpoints only for named indictments.
  5. Shared checkpoint-grid recipe is **pre-registered once and frozen** before any analysis.
  6. The matched-gain convention is **defined once** (§14) and used verbatim everywhere.

## 2. One-sentence claim

HYPOTHESIS: Fine-tuning a promptable segmenter erodes its zero-shot interactive skills **non-uniformly by
prompt type** — an ordering that persists even when the fine-tuning prompt distribution covers all prompt
types (i.e., it is forgetting, not train/test prompt-coverage mismatch), that exceeds the
threshold/seed/prompt-sampling noise floor, that includes a genuine loss of multimask ambiguity capability
(oracle best-of-3, not just IoU-head ranking), and that localizes causally to identifiable decoder
components under stitch-controlled module splicing.

## 3. Abstract

KNOWN FACT (from verified prior work; see `literature.md`): fine-tuning SAM-class models erodes zero-shot
generality; prompt-mode-resolved tables after fine-tuning exist (SAM-Med2D); collapse under vanilla full
fine-tuning is documented (Gu et al. 2404.09957); "SAM forgets, fix it" methods exist (CA-SAM, EvoSAM).
What is *not* established: (a) whether the erosion is **prompt-type-structured forgetting** or merely
degradation on prompt modes absent from the fine-tuning distribution; (b) whether published "forgetting"
deltas exceed the noise floor implied by binarization-threshold shifts, seed variance, and prompt-sampling
variance; (c) whether the **capability** to propose diverse valid masks under ambiguity is lost, or only the
IoU head's ranking of proposals; (d) **where** in the architecture the lost behavior lives. PromptAmnesia
answers all four with one pre-registered fine-tuning grid and three analysis arms: a noise-floor **gate**
(P082, eval-only, runs first, symmetric threshold protocol on released checkpoints), a **behavioral
battery** crossing fine-tuning prompt-mix {box-only, point-only, mixed} with an evaluation matrix
{box, 1-click, 5-click iterative with negative clicks, multimask-ambiguity} at matched target-domain gain
(P065), and a **mechanism arm** that swaps modules between pre- and post-fine-tuning checkpoints with
trained affine stitches and per-module α-interpolation to separate lost function from interface mismatch
(P177). Every claim has a pre-registered kill criterion. No results are asserted in advance.

## 4. Problem statement

KNOWN FACT: Promptable segmenters (SAM, SAM 2) expose several interaction contracts at once: box→mask,
point(s)→mask, iterative refinement with positive and negative clicks, and multimask output under ambiguity
with an IoU-head ranking. Fine-tuning for a target domain (e.g., medical) is now routine (MedSAM, SAMed,
SAM-Med2D, Medical SAM Adapter and successors).

EVIDENCE (inherited, verified in Stage 3): fine-tuning erodes zero-shot behavior (Gu et al.; CA-SAM's
motivation), and box-only-trained models prompt poorly with points (MedSAM). But the field measures this
erosion as *dataset-level Dice deltas*, usually at one operating point, usually without seed or
prompt-sampling variance, and never separated from the fine-tuning prompt distribution.

The problem: **the community cannot currently distinguish four different phenomena that all present as
"zero-shot Dice dropped after fine-tuning":**
1. train/test **prompt-coverage mismatch** (a data statement, not forgetting);
2. **operating-point drift** (binarization threshold no longer optimal — an artifact, C1-082);
3. **ranking corruption** (IoU head desynchronized; capability intact — P031's object);
4. **behavioral forgetting proper** (the skill is gone even under fair thresholds, full prompt coverage,
   and oracle mask selection).

PromptAmnesia is the instrument that separates them.

## 5. Why now

- EVIDENCE: The 2024–26 SAM-continual wave (Gu et al. 2404.09957; CA-SAM 2511.17201; EvoSAM 2503.06236)
  builds *fixes* on top of an erosion phenomenon whose measurement hygiene has never been audited. If the
  gate (P082) shows a large fraction of measured erosion is threshold/variance artifact, the fix literature
  is recalibrated; if it shows real signal, the field gains its first prompt-type-resolved map of what is lost.
- EVIDENCE: Biderman et al. (2405.09673) quantified the learning–forgetting coupling for LLMs; Soutif et al.
  extended to ViTs. Nobody has used the coupling to *deflate or validate* dense/promptable forgetting claims.
- KNOWN FACT: all required checkpoints (SAM ViT-B/H, MedSAM, SAM-Med2D) and datasets (COCO, LVIS, BUSI,
  MSD, SA-1B subsets) are public — the study is eval-heavy and fine-tune-light, feasible for one lab.

## 6. Scientific questions

- **RQ1 (gate):** Do published and reproduced "zero-shot forgetting" deltas for fine-tuned SAM-class
  checkpoints exceed a noise-floor envelope constructed from symmetric threshold re-tuning, seed variance,
  prompt-sampling variance, and split variance?
- **RQ2 (ordering):** At matched target-domain gain and with a *mixed-prompt* fine-tuning distribution, is
  zero-shot degradation non-uniform across prompt types (box vs single point vs iterative refinement vs
  negative clicks), with a stable ordering across seeds and domains?
- **RQ3 (diversity):** Under ambiguous prompts, does fine-tuning reduce **oracle best-of-3** mask quality
  (capability loss), or only argmax-selected quality (ranking loss), on held-out ambiguity probes?
- **RQ4 (mechanism):** What fraction of the zero-shot drop is causally attributable to identifiable modules
  (prompt cross-attention vs rest of decoder vs encoder), measured by both-direction module splicing **with
  trained affine stitches** and per-module α-interpolation?
- **RQ5 (coverage vs forgetting):** How much of the naive (box-only-FT) degradation ordering is explained by
  prompt-coverage mismatch alone — i.e., how much does the ordering shrink from the box-only column to the
  mixed column?

## 7. Formal hypotheses and falsification conditions

| ID | Statement (HYPOTHESIS) | Falsified if (pre-registered) |
|----|------------------------|-------------------------------|
| H1 | Reproduced forgetting deltas of ≥1 released fine-tuned checkpoint exceed the P082 noise-floor envelope on ≥2 retention domains | All reproduced deltas fall inside the envelope → **pivot** (§28): the deflation result becomes the paper |
| H2 | In the mixed-prompt FT column, prompt-type degradation ordering is non-uniform: at least one pre-registered contrast (O1–O5, §21) is significant after Holm correction and exceeds the envelope | No contrast survives in the mixed column (even if the box-only column shows ordering) → coverage explains the phenomenon; report as negative result |
| H3 | Negative-click handling and click-3+ refinement degrade before box and click-1 performance (A1-109 / C1-063 ordering) | Ordering absent or reversed in the mixed column |
| H4 | Fine-tuning reduces oracle-best-of-3 IoU on ambiguity probes (capability loss), not merely argmax IoU | Oracle-best-of-3 unchanged while argmax drops → phenomenon reassigned to P031 (IoU-head desync); diversity claim withdrawn |
| H5 | Splicing pre-FT decoder cross-attention (with trained stitch) back into the fine-tuned model restores a substantially larger fraction of the zero-shot drop than splicing the pre-FT encoder (with trained stitch) | Restoration fractions are indistinguishable, or stitch-vs-no-stitch differences dominate module differences → locus claim withdrawn; report interpolation curves descriptively |

MODEL SPECULATION (explicitly *not* a claim of this package): that the ordering, if found, reflects
gradient-exposure asymmetries between prompt pathways. This may motivate follow-up work; it is not tested here.

## 8. The trivial rival explanation, and the design that separates it

The Stage-4 Reviewer #2 attack (`stage4_r2_setB.md` §1) is the design's spine: *"models degrade on the
prompt modes they were not fine-tuned with"* is a coverage statement, not forgetting, and MedSAM already
demonstrates it. Therefore:

- The factorial crosses **FT-prompt-mix ∈ {box-only, point-only, mixed}** with the full eval battery.
- **The forgetting claim is licensed only by the mixed-prompt column**, where every evaluated prompt type
  appeared in fine-tuning. The box-only and point-only columns exist to *measure* the coverage effect
  (RQ5), not to prove forgetting.
- Symmetric threshold re-tuning (frozen and fine-tuned models both get per-domain thresholds tuned on the
  same held-out calibration split) removes the C1-082 artifact channel — enforced by the same code path as
  the P082 gate (`src/promptamnesia/threshold_gate.py`).
- The all-mask-loss and multimask-enabled FT arms remove the mechanical explanation of diversity collapse
  (standard recipes backpropagate only the min-loss mask or disable multimask — collapse would then be a
  loss-aggregation consequence, not forgetting).

## 9. Novelty delta vs closest prior work

Full audit in `literature.md`. Summary of the delta (REVIEW JUDGMENT inherited from Stage 3, re-attackable):

| Closest work | What it established | What it does not contain (our delta) |
|---|---|---|
| Gu et al. 2404.09957 | 18 FT combinations × 17 datasets; vanilla FT collapse; PEFT protects | In-domain Dice focus; no per-prompt-type zero-shot retention at matched gain; no coverage/forgetting separation |
| SAM-Med2D 2308.16184 | Bbox/1pt/3pt/5pt table, frozen vs FT | No matched-gain control, no mixed-vs-box-only FT factorial, no negative clicks, no diversity, no noise floor |
| CA-SAM 2511.17201 | OOD retention tables for *their* method | Not a controlled audit; no prompt-type resolution; no mechanism |
| MedSAM 2304.12306 | Box-only FT prompts poorly with points | That is the *coverage* effect — our null model, not our finding |
| Biderman 2405.09673 / Soutif (ViTs) | Learning–forgetting coupling | Not applied to promptable/dense models; not used to deflate published claims |
| Ramasesh 2007.07400 / Davari 2203.13381 / Lee 2210.11466 | Forgetting depth-profiles, probes, surgical FT (classification) | No promptable decoder; no causal splice; prompt cross-attention has no classification analogue (divergence mechanism per Stage-3 F2 rule) |
| Bansal 2106.07682 (stitching) | Stitching compatibility methodology | Used here as *control*, not contribution; no forgetting-locus application to SAM |
| Metrics Reloaded | Threshold/operating-point pitfalls (canon) | Unapplied to forgetting claims — P082's exact gap |

## 10. Significance — who is wrong if we are right

- If **H1 fails** (everything inside the envelope): the "SAM forgets" motivation sections of the
  CL-for-SAM literature (CA-SAM, EvoSAM class) are built on artifact-contaminated measurements; the fix
  literature loses its problem statement at current effect sizes. This is the P082 branch — a deflation
  paper with named, reproducible re-evaluations.
- If **H2 holds**: every "retention" number reported as a single dataset-level Dice delta (the field's
  default) is under-specified — retention is prompt-type-structured, and method rankings that ignore the
  structure are unstable. The P110-derived reporting panel (appendix, §27) becomes the corrective.
- If **H4's oracle branch holds**: fine-tuning erases capability, not just ranking — a qualitatively
  stronger claim than any published erosion table, and P031's recalibration fixes cannot recover it.
- If **H5 holds**: the community's freeze-the-encoder folk practice is causally grounded (or refuted) for
  promptable decoders — actionable for every SAM fine-tuning recipe.

## 11. Structure of the study

Three arms, strictly ordered (see `mermaid.md` for the flow):

1. **GATE — P082** (eval-only; released checkpoints + frozen SAM; no training). Output: noise-floor
  envelope + PROCEED/PIVOT decision. Runs before the grid recipe is frozen so the envelope can size the
  grid's seed count.
2. **GRID + BATTERY — P065** (the only training in the package). One pre-registered fine-tuning grid
  (§13), evaluated by the prompt-type battery (§16) and diversity decomposition (§17).
3. **MECHANISM — P177** (eval-only reuse of grid checkpoints + tiny stitch training). Splice/stitch/
  interpolation grid (§18).

## 12. P082 gate protocol (runs first)

Design (obligations from `stage4_r2_setB.md` §8 in force):

- **Subjects:** released checkpoints only for any named indictment — MedSAM (ViT-B) and SAM-Med2D at
  minimum; frozen SAM ViT-B/ViT-H as reference. Re-implementations may appear only as unlabeled
  sensitivity checks, never as named claims (F8 strawman rule).
- **Noise-floor envelope:** run the **frozen** model under every variance source the fine-tuned models
  face — ≥5 prompt-sampling seeds × ≥3 calibration/eval split draws × full binarization-threshold sweep ×
  (where applicable) checkpoint-quantization jitter — and take the per-domain, per-prompt-type empirical
  95% band of |ΔDice| (and |ΔmIoU|) under the null of "no forgetting". Envelope construction is
  implemented in `src/promptamnesia/threshold_gate.py` (pure computation; runs on real eval records only).
- **Symmetric threshold protocol:** frozen and fine-tuned models both receive per-domain thresholds tuned
  on the **same** held-out calibration split; tuned thresholds are then frozen for the eval split. Any
  "recovered" performance from re-tuning is reported for both sides or neither.
- **Pre-registered target list:** the specific published deltas to be tested against the envelope are
  fixed in `configs/p082_gate.yaml` **before** any evaluation runs; additions after first eval are
  reported as exploratory.
- **Confirmatory coupling check:** Biderman-style gain-vs-retention regression across the (later) P065
  grid — framed as *confirming* the coupling in the promptable regime, not discovering it (Stage-3 order).
- **Gate decision rule (pre-registered):**
  - PROCEED if ≥1 released checkpoint shows a reproduced retention delta outside the envelope on ≥2
    retention domains for ≥1 prompt type.
  - PIVOT otherwise (§28: the deflation finding becomes Idea_02's paper; P065 grid budget is cut to the
    minimum needed to demonstrate the coupling regression).
- ESTIMATE: 1–2 GPU-days (matches `stage6_battle.md` budget line).

## 13. Shared fine-tuning checkpoint grid (pre-registered, frozen before analysis)

Cross-paper structural attack #1 (`stage4_r2_setB.md`) is answered by freezing this recipe once; P031
(calibration sibling) reuses the same grid. Full spec in `configs/shared_grid.yaml`. Summary:

- **Backbone:** SAM ViT-B (official weights). ViT-H replication of the headline cells only, if budget allows.
- **Target domains (fine-tuning tasks):** (a) breast ultrasound (BUSI), (b) CT organ slices (MSD Task09
  Spleen, 2D). Two domains with disjoint modality physics; both public.
- **FT-prompt-mix axis:** {box-only, point-only, mixed}. The mixed distribution is pre-registered:
  1/3 box (jittered), 1/3 single positive point, 1/3 iterative protocol (up to 5 clicks including
  negative clicks on false-positive regions), with multimask enabled and ambiguity handled by all-mask loss
  (below).
- **Recipe axis (per mix, per domain):**
  - full FT, LR swept over 3 values (the Gu-protocol honesty control; C1-076 LR confound);
  - decoder-only FT (known-weak arm; included because the field ships it);
  - LoRA on encoder+decoder attention projections (the honest PEFT arm per Stage-3 ruling);
  - VeRA-style random-direction control at matched rank (mandatory per Stage-3 cluster-2 ruling: any
    trained-PEFT effect must beat frozen random directions + trained scaling).
- **Loss-aggregation axis (mixed column only, for the diversity claim):** {min-loss-mask backprop,
  all-mask loss}; multimask output **enabled** in both. IoU-head loss **on** by default (honest recipe);
  the off-cell exists once, shared with P031.
- **Seeds:** ≥3 per cell (5 for headline cells if the P082 envelope demands it).
- **Checkpointing:** dense enough for matched-gain selection (§14); every checkpoint logs the free
  covariates: step, train loss, per-module update norm, and encoder–decoder interface CKA drift
  (P108 residue — logged, not analyzed as a claim).
- ESTIMATE: ~204 expanded runs (144 recipe×LR base cells = 8 recipe-LR cells × 3 mixes × 3 seeds ×
  2 domains, + 48 all-mask-loss cells in the mixed column, + 12 mix-robustness cells; enumerable via
  `train_lora_stub --print-plan`); ViT-B fine-tunes on 2D medical sets are short; total order
  25–45 GPU-days on a single A100-class GPU, trimmable by shrinking the point-only column's LR sweeps
  if the gate's envelope is wide.

## 14. Matched-gain convention (single point of failure, defined once)

Cross-paper structural attack #2 answered here; this definition is used verbatim by P065, P031, P082's
plasticity measurement, and P177's checkpoint selection.

> **Matched-gain rule (pre-registered):** For each (domain, mix, seed), let G\* be the best
> target-domain validation Dice achieved by the **weakest recipe arm** in that stratum. Every arm
> contributes the **first checkpoint** (in training order) whose target-domain validation Dice is within
> ±0.5 Dice points of G\*. Arms that never reach G\*−0.5 are excluded from matched comparisons in that
> stratum (reported, not silently dropped). Validation Dice is computed at the arm's own
> calibration-split-tuned threshold (symmetric protocol).

Rationale: "first checkpoint within tolerance" pins effective training length to the same *achieved gain*,
the alternative (best checkpoint per arm) confounds retention with longer training. The tolerance
(±0.5 Dice) is a design parameter, not a measured value; sensitivity to it is a pre-registered robustness
check (re-run headline contrasts at ±0.25 and ±1.0).

## 15. P065 factorial design

The core experiment: **FT-prompt-mix {box-only, point-only, mixed} × recipe {full-FT, decoder-FT,
LoRA-enc+dec, VeRA-control} × eval battery (§16), at matched gain (§14), ≥3 seeds, symmetric thresholds.**

Readout structure per cell: retention delta Δ(p) = metric(fine-tuned, prompt-type p on retention suite) −
metric(frozen SAM, same p, same threshold protocol). The claims are about the *structure of Δ across p*:

- **Coverage effect (RQ5):** Δ-ordering in box-only column minus Δ-ordering in mixed column.
- **Forgetting proper (RQ2/H2):** Δ-ordering inside the mixed column, tested against the P082 envelope.
- **Cross-modal harm (C1-074):** off-diagonal cells (point-only FT → box eval, box-only FT → point eval),
  reported as the coverage-mismatch map.

## 16. Evaluation battery specification (prompt-type matrix)

Retention suites (held-out from all fine-tuning): COCO val2017 instances (natural-category zero-shot
suite, frozen SAM as floor), LVIS rare-category subset (frequency stress), plus the two *non-fine-tuned*
medical domains as cross-domain retention probes (e.g., TN3K when BUSI was the FT domain). Battery columns:

1. **Box:** GT-derived box with pre-registered jitter distribution.
2. **1-click:** single positive point (mask-interior sampling rule pre-registered).
3. **Iterative-5:** standard error-region protocol — click k+1 placed at the center of the largest
   error component; **negative clicks** on false-positive regions (this column carries A1-109/C1-071).
   Readout: Dice@k curve and NoC@90 where defined (C1-063's click-depth ordering).
4. **Multimask-ambiguity:** §17.

Protocol hygiene inherited from Stage-3 kills (RClicks/BREPS ate naive click simulation): the click
simulator is fixed and pre-registered, and every headline contrast is re-run under one alternative
click-placement rule as a sensitivity analysis; contrasts that flip under the alternative simulator are
reported as simulator-dependent (limitation), not as findings.

Threshold policy: per-arm, per-domain threshold tuned on the calibration split (same split for all arms,
frozen model included), then frozen. Implemented by the same code as the gate.

## 17. Diversity arm — oracle best-of-3 decomposition (C1-061)

**Binding obligation.** The ambiguity probe set: prompts placed at pre-registered ambiguous locations —
nested-instance pairs mined from COCO/LVIS annotations (e.g., part-vs-whole, object-vs-group), where ≥2
distinct valid ground-truth masks exist per prompt. Construction protocol is pre-registered; C1-061's
known risk ("diversity metric contested") is mitigated by not using any abstract diversity metric:

- For each probe, the model emits 3 candidate masks + IoU-head scores (multimask mode).
- **Oracle best-of-3:** max over candidates of IoU against the *best-matching* valid GT mask.
- **Argmax:** IoU of the IoU-head-selected candidate.
- **Decomposition (pre-registered):**
  - oracle drops after FT → **capability loss** (the diversity-forgetting claim stands);
  - oracle intact, argmax drops → **ranking loss** → the observation is transferred to P031 (IoU-head
    desync) and *withdrawn from this paper's claims*;
  - both intact in all-mask-loss cells but oracle drops in min-loss-mask cells → **loss-aggregation
    artifact** — reported as a recipe finding, not forgetting.

Computation in `src/promptamnesia/diversity.py`.

## 18. P177 mechanism arm — splice, stitch, interpolate

**Included ⇒ stitching controls mandatory** (binding). Design per `stage4_r2_setB.md` §2, on the
matched-gain checkpoints from §13 (no new training except stitches):

- **Module partition:** {image encoder, prompt encoder, decoder cross-attention (token↔image blocks),
  decoder-rest (remaining decoder + output/IoU heads)}. Exact parameter-name partition in
  `configs/p177_splice.yaml` and `src/promptamnesia/splice.py`.
- **Swap grid:** every module group swapped **in both directions** (pre-FT module into fine-tuned model;
  fine-tuned module into pre-FT model).
- **Stitch control:** each swap cell evaluated **with and without** a small trained affine stitch
  (per-channel scale+shift, optionally 1×1 linear) at the swapped interface, trained on the calibration
  split with everything else frozen. The stitch separates *interface mismatch* from *lost function*
  (Bansal et al. warning; also the surviving test of A1-108's interface story after P108's rejection).
- **α-interpolation baseline:** WiSE-FT-style per-module-group weight interpolation, α ∈ {0, .25, .5, .75, 1},
  the continuous superset of the binary splice — the splice must add information beyond these curves.
- **Confounder control:** per-module effective-plasticity accounting (update-norm per module logged during
  the grid) + one update-norm-matched fine-tune arm; without it, "locus" merely re-describes the recipe.
- **Pre-registered readout:** fraction of zero-shot drop recovered per cell, with seed CIs:
  R(cell) = (metric(chimera) − metric(fine-tuned)) / (metric(frozen) − metric(fine-tuned)),
  computed per prompt type (mechanism may be prompt-type-specific — the bridge between P177 and P065).
- **Locus verdict rule:** H5 stands only if cross-attn-splice+stitch recovers a large fraction while
  encoder-splice+stitch recovers approximately none, in both directions, beyond the α-curve's prediction,
  with CIs excluding overlap. Anything weaker → descriptive report.

## 19. Datasets and released checkpoints

KNOWN FACT (public availability to re-verify at execution time; no license text is asserted here):

| Asset | Role | Notes |
|---|---|---|
| SAM ViT-B / ViT-H weights | frozen reference + FT init | official release |
| MedSAM checkpoint | P082 subject | released; box-trained |
| SAM-Med2D checkpoint | P082 subject | released; box+point+mask-trained |
| COCO val2017 | retention suite | held-out natural categories; frozen SAM is the floor, so "zero-shot" is relative, not absolute |
| LVIS (rare subset) | retention stress | frequency-stratified |
| BUSI | FT domain A + retention probe when not FT'd | breast ultrasound |
| MSD Task09 Spleen (2D slices) | FT domain B | CT |
| TN3K | cross-domain medical retention probe | thyroid ultrasound |
| COCO/LVIS nested-instance mining | ambiguity probes (§17) | constructed, protocol pre-registered |

Data governance: no PHI; all sets are established public research datasets; licenses re-checked before
release of any derived annotation lists (we release *index files*, not images).

## 20. Baselines and mandatory controls (consolidated)

From Stage-3/4 obligations — dropping any reverts the Stage-4 verdict to REJECT:

1. Frozen SAM with per-domain re-tuned threshold (the fair floor).
2. Mixed-prompt FT column (the licensing column).
3. LR-swept full-FT and decoder-only arms (Gu-protocol grid).
4. VeRA/random-direction PEFT control at matched rank.
5. All-mask-loss + multimask-enabled FT arm (diversity claim).
6. Symmetric threshold tuning everywhere (P082 protocol).
7. ≥3 seeds and CIs on every ordering statement.
8. P177: stitch controls, both swap directions, α-interpolation, update-norm accounting.
9. Click-simulator sensitivity duplicate of headline contrasts.
10. Matched-gain rule (§14) with tolerance sensitivity check.

## 21. Metrics and statistical analysis plan

- **Primary metric:** Dice (medical convention) and mIoU (natural-image convention), both at
  calibration-tuned thresholds; boundary quality (NSD/boundary-F) as secondary descriptive only (P107 owns
  error-type decomposition).
- **Retention delta:** Δ(p, arm) vs frozen floor per prompt type p (§15).
- **Pre-registered ordering contrasts (family, Holm-corrected):**
  - O1: Δ(1-click) vs Δ(box) — C1-065 core;
  - O2: Δ(negative-click cells of Iterative-5) vs Δ(positive-only cells) — A1-109/C1-071;
  - O3: Δ(Dice@click-5) vs Δ(Dice@click-1) — C1-063 click-depth;
  - O4: Δ(oracle best-of-3) vs Δ(argmax) on ambiguity probes — C1-061 decomposition;
  - O5: off-diagonal coverage asymmetry (point-FT→box eval vs box-FT→point eval) — C1-074.
- **Inference:** hierarchical bootstrap (resample images within domain, seeds within arm); 95% CIs;
  a contrast counts only if (a) Holm-significant, (b) its point estimate lies outside the P082 envelope,
  (c) it holds in the mixed column.
- **Coupling regression (confirmatory):** retention delta vs achieved gain across all cells
  (Biderman-style), reported with the envelope as reference band.
- **Reporting panel (P110 residue, appendix):** per-prompt-type retention table, gain-vs-retention
  frontier plot per arm, and a model-card row per checkpoint. Panel only — no frontier scalar is proposed
  (Stage-4 P110 REJECT is accepted as final).

## 22. Killer experiments and kill criteria

| Arm | Killer experiment | Kill criterion (pre-registered) |
|---|---|---|
| P082 gate | Envelope vs reproduced released-checkpoint deltas | All deltas inside envelope → PIVOT to deflation paper |
| P065 core | Mixed-column ordering contrasts O1–O3, O5 | No contrast survives (b)+(c) of §21 → forgetting claim dies; coverage map (RQ5) is the salvage report |
| C1-061 diversity | Oracle-vs-argmax decomposition in all-mask-loss cells | Oracle intact → claim transferred to P031; min-loss-only collapse → recipe artifact note |
| P177 locus | Stitch-controlled both-direction swap grid vs α-curves | Restoration fraction not module-separable → locus claim withdrawn |

The cheapest kill (gate) precedes all training. This ordering is the package's ROI argument: worst case
spends ~2 GPU-days and produces a publishable deflation audit; the expensive grid runs only when the
envelope licenses it.

## 23. Expected outcome branches

All entries EXPECTED RESULT (design-stage speculation, no measurements exist):

- **Branch A (gate fails → pivot):** deflation paper — "published SAM-forgetting deltas at current effect
  sizes are threshold/variance artifacts" with symmetric-threshold re-evaluations of MedSAM/SAM-Med2D.
- **Branch B (gate passes, mixed-column ordering holds):** flagship result — prompt-type-structured
  forgetting map + coverage/forgetting decomposition + diversity decomposition + locus mechanism.
- **Branch C (gate passes, ordering only in box-only column):** honest negative — "what looks like
  prompt-type forgetting is prompt-coverage mismatch"; the coverage map and the reporting panel are the
  contributions; the CL-for-SAM fix literature keeps its problem but loses the taxonomy.
- **Branch D (oracle intact, argmax broken):** the diversity half migrates to P031 (IoU-head desync);
  P065 ships without C1-061 and P031 gains its decision-damage exhibit.
- Every branch produces a reportable artifact; no branch requires asserting an unmeasured number.

## 24. Reviewer-attack ledger and silencing map

Full inherited attack text + our answers in `reviewer_attacks.md`. Compressed map:

| Attack (Stage 4) | Design answer |
|---|---|
| "Coverage, not forgetting" | Mixed-prompt column licenses all claims (§8, §15) |
| "Diversity collapse is a loss-aggregation artifact" | All-mask-loss + multimask-enabled arms; oracle decomposition (§17) |
| "Threshold artifact (C1-082)" | P082 gate + symmetric threshold protocol everywhere (§12) |
| "Matched gain under-specified" | Single frozen convention (§14) + tolerance sensitivity |
| "Splice conflates locus with interface mismatch" | Trained stitches, both directions, α-interpolation superset (§18) |
| "Locus is a recipe tautology" | Update-norm accounting + norm-matched arm (§18) |
| "Seed/prompt variance swamps ordering" | ≥3 seeds, hierarchical bootstrap, envelope condition (§21) |
| "Reimplementation strawman (F8)" | Released checkpoints only for named claims (§12) |
| "SAM-Med2D already published the table" | Their table is unmatched-gain, coverage-confounded, threshold-naive; the delta is §9 row 2 |

## 25. Risks and mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Gate pivots the whole idea | Medium-high (by design) | Branch A is a protected deliverable; grid budget is not spent before the gate |
| Ambiguity probe construction contested | Medium | Pre-registered mining protocol; oracle-gap needs only per-candidate IoUs, no diversity scalar |
| Click-simulator dependence | Medium | Dual-simulator sensitivity duplicate (§16); simulator-dependent contrasts demoted to limitations |
| Arms fail to reach matched-gain band | Medium | Rule reports exclusions explicitly; tolerance sensitivity pre-registered |
| Stitch training itself restores function (over-powerful control) | Low-medium | Stitch capacity capped (affine); stitch-only cells (no swap) reported as calibration of stitch power |
| ViT-B-only conclusions | Low | Headline cells replicated on ViT-H if budget allows; otherwise scoped claim |
| Compute overrun | Low-medium | Point-only column is first to shrink; P177 and P082 are eval-only |

## 26. Compute budget and feasibility

ESTIMATES (single A100-class GPU; no measured runtimes exist yet):

| Item | Estimate |
|---|---|
| P082 gate (eval-only) | 1–2 GPU-days |
| Shared grid fine-tuning (§13) | 25–40 GPU-days |
| Battery + diversity evaluation | 3–6 GPU-days |
| P177 stitches + swap-grid eval | 2–4 GPU-days |
| Total (worst case) | ≈ 35–50 GPU-days, one GPU, one lab |

Feasibility rubric check: no foundation-model pretraining; all data/checkpoints public; the decisive gate
costs <2 GPU-days (rubric's "can be killed in <1 GPU-day" satisfied in spirit by the gate's first-day
partial readout on one domain).

## 27. Reproducibility, pre-registration, epistemic hygiene

- The grid recipe (`configs/shared_grid.yaml`), matched-gain rule (§14), contrast family (§21), gate
  target list (`configs/p082_gate.yaml`), and ambiguity-probe protocol are **frozen before any analysis**;
  the freeze is a tagged commit on this branch.
- Every released number will carry one of the ledger's labels; EXPECTED RESULT never upgrades to
  ACTUAL EXPERIMENTAL RESULT without a run artifact (config hash + seed + commit) checked into the repo.
- `[M]`-tagged citations (memory-cited classics inherited from Stage 3) must be re-verified against arXiv
  before any manuscript quotes them — tracked as a release blocker in `roadmap.md`.
- Code: `src/promptamnesia/` prototype in this package; all analysis code pure-function where possible;
  eval records serialized (parquet/CSV) so every figure regenerates from committed artifacts.
- The P110-derived reporting panel ships as a mandatory appendix (per Stage-4 disposition).

## 28. Deliverables, venue, portfolio interfaces, backups

- **Primary deliverable:** one main-track paper (CVPR/ICCV/ECCV class; MICCAI variant if the medical
  domains dominate the story) = P065 battery + P082 envelope + P177 mechanism, whichever branch obtains.
- **Portfolio interfaces:**
  - **P031** (IoU-head desync / calibration): consumes this grid's checkpoints; receives the diversity
    claim if H4 resolves to ranking-loss; the IoU-loss-off cell is shared.
  - **P044 / P052:** independent medical-side falsifiers; no shared single point of failure.
  - **P108 residue:** interface-drift statistic logged as a free covariate in the grid; resurrection
    (a prediction paper) only if it incidentally shows striking lead time — pre-registered as exploratory.
  - **P110 residue:** reporting panel appendix (§21); no scalar.
- **Execution order (binding, from Stage 4/6):** P082 → grid freeze → P065 → P031 (sibling) → P177.
- **Backups if a killer experiment dies in week 1** (per `stage4_top20.md`): P063 RefractionFeatures,
  P079 MemoryProbe hold the portfolio slot; inside Idea_02 the internal pivot is Branch A (deflation).
- **Authorship/venue hygiene:** deflation branch names only released checkpoints; all criticism is
  accompanied by runnable re-evaluation code.
