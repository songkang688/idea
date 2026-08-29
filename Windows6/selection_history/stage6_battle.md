# Stage 6 — Research group battle & Final-3 lock verdict (RETROSPECTIVE RECONSTRUCTION)

- **Windows ID:** Windows6
- **Branch:** `cursor/windows6-research-idea-evolution-b55d`
- **Reconstructed on:** 2026-08-29 (UTC)
- **Base commit:** `0c25df6` (immediately after W6-T1 landed `stage5_top5.md`)
- **Task:** W6-T2 (second of three Windows6 close-out tasks: T1 → T2 → T3)
- **Document type:** **RETROSPECTIVE / 补记.**

## 0. What this file closes, and what it is not

**FACT.** `Windows6/README.md` carries an open status line: *"Provisional Final 3 packaged; **Stage 5/6 still confirming** against DE-top10 assassin + auditor."* This file exists to terminate that dangling "still confirming" by issuing an explicit 5 → 3 adjudication and an explicit **locked / provisional** verdict (§5).

**FACT — and this is the most important disclaimer in the file.** **No Stage-6 battle event ever took place in Windows6.** There is no artifact recording a debate, a vote, or a panel. What Windows6 actually has is **four independent rejector passes**, each with a recorded source:

| Rejector pass | Artifact | Scope |
|---|---|---|
| Stage-3 cheap-killer prior-work assassin | `stage3_prior_work_kill_cheap.jsonl` (12 verdicts) | A–F cheap cluster |
| Stage-3 DE top-10 assassin | `stage3_DE_top10.json.md` (10 verdicts) | D+E medical/VLM branch |
| Stage-4 Reviewer #2 | `stage4_reviewer2_cheap5.jsonl` (5 verdicts) | the cheap-5 |
| Meta-auditor (Stage 2 vs Stage 3 reconciliation) | `auditor_overlay.md` | collisions between bands |

This file **adjudicates from those four recorded passes**. It does not invent a fifth reviewer, a panel, a vote count, or any role that the artifacts do not name. Where the four passes conflict, the conflict is preserved in §4 rather than smoothed into a consensus.

**Scope boundaries (hard):**

- Does **not** modify `Idea_01/`, `Idea_02/`, `Idea_03/` — package thickening is **W6-T3**.
- Does **not** modify any `stage1_pool/` / `stage2*` / `stage3*` / `stage4*` file, nor `stage5_top5.md`.
- Does **not** modify `README.md`, `research_summary.md`, or `supervisor_log.md` — status reconciliation is **W6-T3**.
- Does **not** re-review the two Reviewer #2 kills. Their reasons are transcribed, not re-litigated.

### Evidence grading legend

Same scale as `stage5_top5.md`: **FACT** (present in a Windows6 artifact) · **VERIFIED PRIOR WORK** (external paper web-searched by a Stage-3/4 agent and used to kill/mutate; tables not re-run) · **HYPOTHESIS** (claim to be tested) · **SPECULATION** (inference made by *this* document) · **EXPECTED RESULT** (pre-registered predicted trend) · **ACTUAL RESULT** (a number actually produced by running something).

**FACT.** Windows6 has **zero ACTUAL RESULTS**. `README.md` labels the packages *"no real SAM numbers" / "no smoke mAP" / "no VLM eval"*; `Idea_02/proposal.md` states *"We have not trained a detector here."* Every cost figure in §6 is **HYPOTHESIS**.

**Citation rule enforced in this file:** external papers may be cited **only** if they already appear in `literature_anchors.md` or in an `Idea_0*/literature.md`. No new references were added.

---

## 1. The 5 → 3 adjudication

**FACT.** Input is the Top-5 reconstructed in `stage5_top5.md` §2, which is itself a verbatim reading of `stage4_reviewer2_cheap5.jsonl`.

| # | Stage-4 id | Original numbering | Verdict carried forward | Basis | Outcome |
|---|---|---|---|---|---|
| 1 | `AMG-HU-clustering` | F-067 | **survive**, `advance: true` | R2 + Stage-3 keep (0.6) + auditor protected keep | → **`Idea_01`**, §2.1 |
| 2 | `camera-ID-smoke` | F-043 | **survive**, `advance: true` | R2 + Stage-3 keep (0.55) + auditor protected keep | → **`Idea_02`**, §2.2 |
| 3 | `empty-slice-FPR-Dice` | F-022 (+F-074 dup) | **KILL** | Reviewer #2 | thread ended, §1.1 |
| 4 | `alignment-tax-localization` | F-031 / E-009 (+F-039) | **survive (mutated)**, `advance: true` | R2 + Stage-3 mutate (0.5) + DE keep E-009 (0.55) + auditor protected keep | → **`Idea_03`**, §2.3 |
| 5 | `atlas-vs-CLIP-text` | F-036 / F-037 | **KILL** | Reviewer #2 | thread ended, §1.1 |

Count: **3 survive / 2 killed.**

### 1.1 Fatal flaws that ended threads (transcribed, not re-reviewed)

**`empty-slice-FPR-Dice` (F-022 / F-074) — KILL.** Reviewer #2 reason, verbatim from `stage4_reviewer2_cheap5.jsonl`:

> `Near-definitional Dice property; Metrics Reloaded; no leaderboard preds`

Three distinct defeaters in one line: the effect is close to a definitional property of Dice rather than an empirical finding; **VERIFIED PRIOR WORK** Metrics Reloaded (Nature Methods 2024, `literature_anchors.md`) already covers the metric-selection ground; and the audit is unrunnable because leaderboard predictions are not obtainable. **FACT:** the record carries `reason` only — **no `residual` and no `advance` field** — i.e. Reviewer #2 offered this idea no rescue path. That is what distinguishes a kill from a mutate here.

**`atlas-vs-CLIP-text` (F-036 / F-037) — KILL.** Reviewer #2 reason, verbatim:

> `CLIP-Driven Universal Model ICCV 2023 one-hot ablation; substitution unidentifiable`

**VERIFIED PRIOR WORK:** CLIP-Driven Universal Model, ICCV 2023 — the proposed one-hot substitution ablation already exists in that paper, and the atlas-vs-text substitution is not identifiable as posed. **FACT:** again `reason` only, no `residual`, no `advance`.

**FACT — the auditor did not save either one.** `auditor_overlay.md` had protected neither into the Final 3 and states the precedence rule outright: *"Reviewer #2 later **killed** F-022 empty-FPR audit and F-036/037 atlas-vs-text… Those auditor 'keeps' do **not** enter Final 3."* The disagreement that this rule papers over is preserved in §4.1.

---

## 2. The three survivors, examined

### 2.1 `Idea_01` — SAM AMG ≈ HU clustering on CT (F-067)

**Scientific question.** Is SAM's Automatic Mask Generation on CT performing semantic objectness, or is it approximately clustering in HU space after windowing?

**Falsifiable hypotheses (HYPOTHESIS, from `Idea_01/proposal.md`).**
- **H1:** After a fixed clinical window, Hungarian-matched mean IoU(AMG, k-means) > IoU(AMG, SLIC) on a pre-registered CT subset.
- **H2 (causal):** An edge-preserving intensity remap changes AMG more than an intensity-preserving texture shuffle with the same edge map.
- **H3:** The H1 gap is stable across an AMG hyperparameter grid and 2–3 windows; if not, the finding is a **setting artifact** → kill or mutate.

**Residual obligation (FACT, verbatim from `stage4_reviewer2_cheap5.jsonl`):**

> `Must earn mechanistic via intensity vs texture counterfactuals; else evaluation note`

**Downgrade path if the residual is not met — this is the one case the source text specifies explicitly.** The clause *"else evaluation note"* is the downgrade: without the causal arm the contribution stops being a mechanistic claim about what AMG computes and becomes an evaluation note reporting an agreement correlation. **FACT:** `Idea_01/reviewer_attacks.md` states a stricter local rule — *"If we cannot run the causal arm, **do not submit**."* So the two artifacts disagree on severity (downgrade vs withhold); recorded in §4.4, not resolved here.

**Closest prior work (VERIFIED PRIOR WORK; only from `literature_anchors.md` / `Idea_01/literature.md`).**
- Segment Anything, ICCV 2023 — supplies the AMG definition being tested.
- SAM2 CT review, arXiv 2408.11210 — black-box CT evaluation; listed in `literature_anchors.md` under *"Remaining-novelty targets"* precisely because it is **not** an AMG-vs-k-means test.
- SAM/SAM2 low-contrast CT, arXiv 2408.04212 — intensity/window dependence; cited by Reviewer #2.
- HQ-SAM, NeurIPS 2023, arXiv 2306.01567 — used to kill the adjacent F-012 filter claim; `Idea_01/literature.md` records *"we do **not** claim filter=HQ"*.
- MedSAM-related CT notes, arXiv 2408.03322 — benchmark context.

**FACT (the gap, as recorded):** `Idea_01/literature.md` states *"**Gap:** no AMG vs k-means Hungarian/ARI study with texture-vs-intensity counterfactuals."* Stage-3 novelty confidence **0.6** — the highest in the round.

**Biggest reviewer attack and the evidence that shuts it.** *"Windowing manufactures the result"* (`Idea_01/reviewer_attacks.md` attack #1): since windowing is a monotone intensity map, running one window can fabricate the AMG≈clustering agreement through preprocessing alone. Shut-up evidence: **sweep 3 clinical windows and report all of them** (abdomen 400/40, bone 2000/400, lung −600/1500 or documented equivalents), and require H1 to hold on ≥2. `Idea_01/proposal.md` concedes the point directly: *"The paper is the **counterfactual**, not the correlation."* Secondary attacks, all with stated answers: agreement ≠ mechanism → the H2 arm; k-means is one cheap baseline among many → also run Otsu, GMM, SLIC; metric shopping → pre-register Hungarian IoU + ARI + boundary-F; *"SAM is bad on CT is already known"* → the paper is mechanism, not Dice tables; hyperparameter brittleness → AMG `points_per_side` grid.

**Death conditions (FACT, from `Idea_01/experiments.md` "Stop").**
- **KILL** if SLIC ≥ k-means in agreement with AMG **on all windows**.
- **KILL** if the texture shuffle moves AMG about as much as the intensity remap (H2 fails — the mechanistic claim is dead by the residual's own terms).
- **KILL** (Stage-5 gate) if AMG is closer to ground truth than to k-means **and** texture shuffle moves AMG a lot.
- **PIVOT** if only one window shows clustering equivalence (H3 fails → setting artifact).
- **KILL the CT-specificity claim** if the COCO control shows the same clustering equivalence — the effect would not be CT-specific.
- **CONTINUE** only if H1 and H2 hold on ≥2 windows and ≥2 AMG settings.

### 2.2 `Idea_02` — Camera-ID vs event-disjoint leakage on smoke/fire (F-043)

**Scientific question.** How much of published smoke/fire detection performance is camera familiarity rather than plume detection — and is *event-disjoint* splitting (the current best practice) actually sufficient?

**Falsifiable hypotheses (HYPOTHESIS, from `Idea_02/proposal.md`).**
- **H1:** camera-disjoint mAP < random-split mAP by more than seed std.
- **H2:** event-disjoint mAP ≠ camera-disjoint mAP (residual same-camera different-event leakage).
- **H3:** a linear probe on frozen backbone features predicts camera ID above chance on a held-out time split.
- **H4:** empty (no-smoke) frames from **train** cameras draw higher FP rate or confidence than empty frames from unseen cameras.

**Residual obligation (FACT, verbatim):**

> `Need event-disjoint vs camera-disjoint gap plus empty-frame memorization probe`

**Downgrade path if the residual is not met.** The source gives **no** explicit downgrade clause for this one — unlike Idea_01, there is no *"else …"*. What the artifacts do give is a two-step fallback ladder, which this file reads off them rather than inventing:
1. **Documented pivot (FACT, `Idea_02/experiments.md`):** *"**Pivot** to event-disjoint only if cameras < 10 (underpowered)."* That pivot forfeits H2 — the very claim that distinguishes this work from PYRONEAR's existing practice.
2. **SPECULATION (inference by this document, flagged as such):** if the H2 gap is delivered but H4 is not, the paper cannot separate geography shift from background memorization, and it collapses back onto the Voxel51 blog diagnosis. `Idea_02/proposal.md` states the equivalent gate as *"Fatal if we only report camera-disjoint drop without H4"* — "fatal", not "downgrade". No artifact describes a surviving reduced form. The honest reading is that **Idea_02 has no recorded soft landing**: it is a full paper or a kill.

**Closest prior work (VERIFIED PRIOR WORK; only from `literature_anchors.md` / `Idea_02/literature.md`).**
- PYRONEAR-2025, arXiv 2402.05349 — event-disjoint splits + pHash. This is simultaneously the closest work and the target: the contribution is that event-disjoint ≠ camera-disjoint.
- Voxel51 Pyro-SDIS audit, 2026 blog — recorded as *"diagnosis, **no** retrained mAP"*. **FACT:** `Idea_02/literature.md` carries the standing instruction *"Do not cite a peer-reviewed mAP inflation number we did not compute."* This file complies: no inflation number is stated anywhere.
- SmokeFrames / Nemo — prior sets, flagged *"check camera IDs before use"*.

**Biggest reviewer attack and the evidence that shuts it.** *"Camera identity is just geography; you have re-measured domain shift, which is not news"* (`Idea_02/reviewer_attacks.md`: *"Confounder: camera = geography"*). Shut-up evidence: the **empty-frame memorization probe** (H4). Empty frames contain no plume, so a seen-vs-unseen camera gap on negatives cannot be explained by plume-appearance domain shift; it is background memorization. Supporting controls already specified in `Idea_02/experiments.md`: an ImageNet-pretrained backbone never trained on smoke as the probe control, cluster bootstrap over **events**, equal-N class-ratio-matched splits, and a pHash dedup rerun that separates duplicate-frame leakage from camera signature. Secondary attacks with stated answers: novelty vs the blog → we retrain and quantify; tiny camera N → multiple folds + CIs; noisy mAP → 3 seeds and report FAR.

**Death conditions (FACT, from `Idea_02/proposal.md` and `experiments.md`).**
- **KILL** if there is no camera metadata on any usable public set (this is a **precondition**, see §5 GATE-A).
- **KILL** if the camera-disjoint drop vanishes once event-disjoint is applied (H2 dead → PYRONEAR already solved it).
- **KILL** if the camera-ID probe is at chance (H3 dead).
- **KILL** if only one tiny camera set is available.
- **PIVOT** to event-disjoint only if cameras < 10.
- **STOP** (Stage-5 gate) if random ≈ camera-disjoint within seed noise **and** probe ≈ chance **and** no seen/unseen empty-FPR gap — confirm with 2 more seeds before stopping.
- **CONTINUE** if H1 and H4 hold on ≥2 datasets.

### 2.3 `Idea_03` — Alignment tax on localization (F-031 / E-009, + F-039)

**Scientific question.** Does alignment (SFT → RLHF) cost a VLM its localization ability, and if so, *at which stage* and *in which component* — the decoding policy or the visual representation?

**Falsifiable hypotheses (HYPOTHESIS, from `Idea_03/proposal.md`).**
- **H1:** constrained box metrics drop from base → chat on ≥1 public checkpoint pair.
- **H2:** a linear probe on **frozen** visual tokens does **not** drop (tax is decoding/format) **or does** drop (tax is representation) — the branch itself is the result.
- **H3 (optional, causal):** LoRA DPO on **text-only** preferences still hurts H1 → the objective, not the image data mix.

**Residual obligation (FACT, verbatim):**

> `Format-controlled eval + representation probe + small text-only DPO control`

**FACT:** this is the only residual in the round with **three** conjuncts, and each maps to a different hypothesis (H1 / H2 / H3). It is the heaviest residual of the three survivors.

**Downgrade path if the residual is not met.** Here the artifacts are unusually clear, because `Idea_03/experiments.md` pre-registers three outcomes:
- **O1** — the gap dies under likelihood scoring → the tax was a **format artifact**; the recorded instruction is *"write negative"*. That is the downgrade: a negative result on formatting, not an alignment-tax paper.
- **O2** — the gap survives in likelihood but the probe holds → **policy tax**.
- **O3** — the probe also drops → **representation tax**.
- If the format-controlled eval is not run at all, `Idea_03/proposal.md` is explicit: *"**Kill** if H1 fails under constrained decoding (formatting confound)"* — and the DPO arm is expressly gated behind it: *"Do not run DPO unless observational gap survives format control."* So the degradation ladder is O3 → O2 → O1(negative) → kill, and the DPO conjunct is **conditional**, not unconditional.

**Closest prior work (VERIFIED PRIOR WORK; only from `literature_anchors.md` / `Idea_03/literature.md`).**
- MDGD, EMNLP Findings 2025 — visual forgetting under instruction tuning. `Idea_03/proposal.md`: *"Visual forgetting under instruction tuning is **published**… Reviewer #2 killed the generic headline."*
- TWIST & SCOUT, ICCV 2025 — grounding / forget-free tuning; recorded as closest, *"we must cite them as attacks."*
- RL-finetuned VLM robustness, 2026, arXiv 2602.12506.
- LLaVA / LLaVA-RLHF families, 2023–24 — *"checkpoint pairs if licenses allow"*.
- **FACT (the surviving gap):** `Idea_03/literature.md` records *"Stage 3: stage-isolated localization curve was NOT FOUND as a standalone paper (EVIDENCE GAP, conf ~0.5)."*

#### 2.3.1 Concurrent-work risk — handled separately, as required

**FACT.** `README.md` rates Idea_03 *"Highest impact, highest concurrent-work risk."* **FACT.** `stage3_DE_top10.json.md` keeps `E-009` at confidence **0.55** with the note *"matched checkpoint localization tax still open"*. **FACT.** The cheap-cluster assassin independently scored the same idea at **0.5** with remaining novelty narrowed to *"Stage-isolated base vs SFT vs RLHF localization curve only"*.

Reading those three together: **the generic headline is already gone, and what remains is a narrow residual slice.** 0.55 is not a comfortable margin — it is the assassin saying the question is *still* open, i.e. open **as of the search date**, not open by construction. Two structural aggravators:

1. **SPECULATION (this document).** The residual novelty is defined by an *absence* ("NOT FOUND as a standalone paper"). Absence-defined novelty decays monotonically with time and is the failure mode most likely to be scooped between now and submission. Compare Idea_01, whose 0.6 rests on a *positive* structural gap (nobody has run the counterfactual arms), and Idea_02, whose 0.55 rests on a *methodological* gap (the blog never retrained). Idea_03's gap is the most fragile of the three even though its confidence number sits mid-range.
2. **FACT.** The one number a scooper would need is cheap to produce. `Idea_03/proposal.md` puts the whole thing at *"Eval-only: 1 GPU, 1–2 days"*, and `experiments.md` at *"≤8 GPU-h"*. Low cost to us is also low cost to everyone else.

**Mitigations already in the package (FACT).** The hard gate — *"identical vision encoder + coordinate tokenization"* — is what turns this from "chat model scores lower" into a stage-isolated claim, and it is also the strongest defence against a scoop, since a concurrent paper without matched checkpoints does not answer the same question. Reviewer #2's recorded instructions reinforce this: *"cite MDGD; we only claim stage+format isolation"*, *"do not claim causal RLHF without H3"*, *"box parsing ≠ localization: constrained decoding + probe"*, and *"Small N families: honest scope."*

**Risk verdict.** Idea_03 stays in the Final 3, but it is the **most likely of the three to be lost to concurrent work**, and it is the member whose feasibility precondition is least verified (§5 GATE-B). Its priority in the execution order (§6) is placed accordingly: last by dependency, but its cheap precondition check is placed early precisely because a failed gate should surface before the GPU spend, not after.

**Death conditions (FACT).**
- **KILL** if H1 fails under constrained decoding (the drop was a formatting confound).
- **STOP** if the likelihood gap is ~0 on pair 1 **and** pair 2.
- **HARD GATE:** no checkpoint pair with identical vision encoder and identical coordinate tokenization → the stage-isolation claim is not available at all.
- **DO NOT RUN** the DPO arm unless the observational gap survives format control.
- **DOWNGRADE to negative result** on O1.

---

## 3. Cross-cutting evidence state of the three survivors

**FACT.** All three residual obligations are **unmet**. Nothing has been run: `Idea_01` has a synthetic CPU prototype (`src/amg_intensity_equiv.py`), `Idea_02` a split-simulator plus camera-ID probe on synthetic features (`src/camera_split_audit.py`), `Idea_03` a synthetic constrained-eval harness (`src/format_controlled_box.py`). **ACTUAL RESULT count across all three: zero.**

**FACT (package depth, measured at base commit `0c25df6`).** Windows6 `proposal.md` sizes are **2781 / 1330 / 987 bytes** for Idea_01 / 02 / 03. The same files on branch `cursor/windows4-research-idea-evolution-2962` are **29870 / 35997 / 24385 bytes** — a factor of roughly **11× / 27× / 25×**. Windows6's `Idea_01/proposal.md` even jumps from a numbered "§7–28" heading straight to a pointer list, i.e. sections 7 through 28 are declared but absent. **This is a packaging deficit, not a science deficit** — the underlying hypotheses, gates and stop rules are all present and specific. Thickening is **W6-T3**; its bearing on the lock verdict is stated in §5 GATE-D.

---

## 4. Unresolved disagreements kept explicit

Recorded conflicts only. No debate is reconstructed that the artifacts do not evidence.

### 4.1 Auditor keeps vs Reviewer #2 kills — F-022, F-036/037

**FACT.** `auditor_overlay.md` opens with the precedence rule *"Stage-3 named papers win collisions"* and lists protected keeps, then records that **Reviewer #2 subsequently killed F-022 empty-FPR audit and F-036/037 atlas-vs-text**, concluding *"Those auditor 'keeps' do **not** enter Final 3."*

**The disagreement is real and is only resolved by ordering, not by argument.** The auditor's Stage-2/3 reconciliation had reasons to keep those threads; Reviewer #2 killed them later. The overlay resolves the clash by recency/authority ("R2 came last, R2 wins"), not by rebutting the auditor's grounds — which are never restated. **SPECULATION:** had Reviewer #2 run *before* the auditor, the overlay's own precedence rule would not obviously have produced the same outcome. **Kept open. Not re-litigated here** — §0 forbids re-reviewing the kills, and this file abides.

### 4.2 Stage-3 extensions vs Final 3 — D-008, D-060, E-025 were never ranked against the survivors

**FACT.** `stage3_DE_top10.json.md` ends: *"Held as **extensions**, not Final 3: D-008, D-060, E-025."* **FACT.** None appears in `stage4_reviewer2_cheap5.jsonl` — **Reviewer #2 never saw them.**

**FACT.** On the Stage-3 confidence figures as literally written, `D-008` sits at **0.60**, which equals Idea_01's 0.6 and exceeds Idea_02's 0.55 and Idea_03's 0.5/0.55. `D-060` sits at **0.55**, level with Idea_02.

**SPECULATION — and an important caveat against over-reading the line above.** Those confidences come from **two different assassin runs** (the DE top-10 pass and the cheap-cluster pass) with no evidence that the scales were calibrated against each other. So the comparison is *suggestive, not valid*. That is precisely the problem: **the artifacts do not contain a common scale on which the Final 3 beat the extensions**, because — per `stage5_top5.md` §1 — there was never a 20-band where the two Stage-3 branches met. This is the single largest input to the §5 verdict.

### 4.3 The same idea drew two different Stage-3 verdict labels

**FACT.** The alignment-tax thread was judged twice: the cheap-cluster assassin returned `mutate` at 0.5 (`alignment-tax-vlm-localization`); the DE assassin returned `keep` at 0.55 (`E-009`). Same underlying question, two labels, two confidences, no artifact reconciling them. `auditor_overlay.md` merges the IDs (*"F-031/E-009"*) without addressing the verdict divergence. Directionally compatible — both let it live — but the round never produced a single authoritative Stage-3 verdict for its highest-impact idea.

### 4.4 How hard is Idea_01's residual — downgrade or withhold?

**FACT.** `stage4_reviewer2_cheap5.jsonl` says the failure mode is *"else evaluation note"* — a downgrade. **FACT.** `Idea_01/reviewer_attacks.md` says *"If we cannot run the causal arm, **do not submit**."* — a withhold. These are different instructions for the same contingency, and no artifact says which governs. Consequential: it decides whether a failed H2 yields a shorter paper or no paper.

### 4.5 Stage-2 keeps overturned by Stage-3

**FACT.** `auditor_overlay.md` records *"Killed despite Stage-2 keep: F-001/002/003 jitter-UQ, F-014 LN≈LoRA, F-051 AdaLoRA-rank, F-074 dup of F-022."* Stage 2 had scored these as keeps; Stage 3 named prior work against them. Resolved by the stated rule *"Stage-3 named papers win collisions"* — recorded here as a resolved-by-policy disagreement rather than an argued one.

### 4.6 F-012 was dropped from the cheap-5 with no recorded reason

**FACT.** The cheap-cluster pass issued 4 mutates; only 3 reached Reviewer #2. `F-012-samhq-vs-filter` (mutate, 0.35) was dropped. **FACT.** The only related instruction is `stage2_ABCF_summary.md`'s *"Do not treat F-012 as 'filter matches HQ-SAM' (mutate to gain-stratification)"* — a scoping note, not an elimination. Carried over from `stage5_top5.md` §1.2; still unexplained.

### 4.7 Day-1 sample size for Idea_01: 50 slices or 100?

**FACT.** `README.md` says *"then **50** real CT slices with SAM AMG vs k-means/SLIC"*; `Idea_01/experiments.md` killer step 3 says *"On **50** MSD/TotalSegmentator slices"*; the Stage-5 engineering block in the same file says *"Day-1: **100** TotalSegmentator slices"*. Minor, but it is an unreconciled number inside the one experiment everything else depends on. §6 resolves it operationally by taking the larger figure and saying so.

### 4.8 Bookkeeping conflicts already logged elsewhere

`stage5_top5.md` §5 records INCONSISTENCY-01 through -04 (README provisional / supervisor_log stuck at Stage 1 / evolution_summary claiming Stage 5 done / cheap-cluster verdict counts 11 vs 12). Those are status and arithmetic defects rather than scientific disagreements, and they remain **W6-T3**'s to fix. Not duplicated here.

---

## 5. Lock verdict — **Final 3 remain PROVISIONAL**

### Verdict

> **The Windows6 Final 3 CANNOT be locked at commit `0c25df6`. They remain PROVISIONAL.**

The idea set is almost certainly right, and this verdict should not be read as doubt about the science. It is a statement that **two of the three members can still be killed by lookups that have not been performed**, and that **the selection was never run against a comparison set**. Locking now would record a decision the evidence does not yet support.

### Why not locked — three independent grounds

**Ground 1 (decisive) — two of three survivors have unverified feasibility preconditions, and each is a *kill* condition in its own package, not a risk.**

- **`Idea_02`:** `experiments.md` step 1 is *"Inventory camera IDs on one public set (PYRONEAR or FIgLib **if IDs exist**)"*, and the first stop rule is *"**Kill** if no camera metadata."* **FACT:** no artifact in Windows6 records that camera IDs were ever confirmed to exist, nor how many cameras. The entire idea rests on an unchecked assumption. `literature.md` even carries the warning *"check camera IDs before use."*
- **`Idea_03`:** `experiments.md` imposes a *"**Hard gate:** identical vision encoder + coordinate tokenization"*, and `literature.md` lists checkpoint pairs only as *"if licenses allow."* **FACT:** no artifact names a concrete pair verified to satisfy the gate. `experiments.md` offers *"e.g. Qwen-VL vs Chat"* — an example, not a verification.

Both checks are cheap, need no GPU, and would take hours. Locking a Final 3 in which two members are one negative lookup away from death is not a defensible record.

**Ground 2 — the Final 3 was never ranked against a comparison set.** Per §4.2 and `stage5_top5.md` §1: there was no 50-band and no 20-band; the two Stage-3 branches never met on a common scale; `D-008` (0.60) and `D-060` (0.55) were parked as extensions without ever being compared head-to-head with the survivors; and Reviewer #2 never saw them. A lock asserts *"these three beat the field."* Windows6 can support *"these three survived the one channel that ran."* Those are different claims and only the second is true.

**Ground 3 — the round's status record still contradicts itself.** Four artifacts state four different stages (README: Stage 5/6 confirming; `supervisor_log.md`: Stage 1; `evolution_summary.md`: Stage 5 done; `Idea_01/README.md`: Stage 5 in flight). A lock declared on top of an incoherent status field is not auditable — a reader cannot tell what was locked or when. This is **W6-T3**'s to fix, and it is why the lock decision must follow T3 rather than precede it.

### Grounds deliberately **rejected** as reasons not to lock

Two tempting arguments are wrong, and the record should say so:

- **"The three residual obligations are unmet."** Not a blocker. Residuals are the research to be *done*; they gate **publication**, not **selection**. If unmet residuals blocked locking, no Final 3 could ever be locked before the papers were written. `stage5_top5.md` and §2 above both treat them as forward obligations.
- **"Zero ACTUAL RESULTS / synthetic prototypes only."** Also not a blocker, for the same reason. `README.md` and `research_summary.md` already label this honestly; a Final 3 is a bet on questions, not a report of findings.

The real blockers are Grounds 1–3: unverified *preconditions*, a missing *comparison set*, and an incoherent *status record*.

### Unlock gates — what must be true, and who does it

| Gate | Requirement | Owner | Standard that closes it |
|---|---|---|---|
| **GATE-A** | Confirm camera metadata exists on ≥1 public smoke/fire set | Idea_02 executor, before any training | A written camera inventory with a camera **count**. ≥10 cameras → gate passes. <10 → the documented pivot to event-disjoint-only fires, which forfeits H2, and Idea_02 must be **re-argued or replaced** before lock. Zero → Idea_02 is **killed** by its own stop rule. No GPU. |
| **GATE-B** | Name one base/chat checkpoint pair verified to have identical vision encoder **and** identical coordinate tokenization, under a usable license | Idea_03 executor, before any GPU spend | A named pair with both properties confirmed from model cards/configs. Fails → the stage-isolation claim is unavailable and Idea_03 must be descoped to a format-artifact study or replaced. No GPU. |
| **GATE-C** | Retro-fit the missing comparison step: rank the 3 survivors against `D-008`, `D-060`, `E-025` on **one** common rubric | Supervisor (a Stage-6 pass proper) | One artifact, one scale, all six scored, with an explicit statement of whether any extension outranks a survivor. Closes §4.2. No GPU. |
| **GATE-D** | Reconcile the status record and bring the packages to a depth where the Final 3 is reviewable | **W6-T3** | INCONSISTENCY-01…04 resolved into one status line; packages no longer 11–27× thinner than the Windows4 reference; `Idea_01/proposal.md`'s absent "§7–28" either written or removed. |

**Lock condition (all four).** When GATE-A, GATE-B, GATE-C and GATE-D are all closed, the Final 3 may be declared **LOCKED**, and the declaration should be written into the reconciled status line rather than into this file.

**Deliberately not a gate:** running the experiments in §6. Those decide whether the papers exist, not whether the selection is sound.

### Conditional note on the likely outcome

**SPECULATION.** GATE-A and GATE-B are each a few hours of desk work, GATE-C is one scoring pass, GATE-D is already scheduled as W6-T3. The likely outcome is that all four close and the Final 3 locks essentially as-is — Idea_01 is well-founded, and Idea_02/Idea_03 are more likely to pass their preconditions than fail them. This note is a forecast, not a verdict; **the verdict above is PROVISIONAL and no downstream document should cite Windows6 as having a locked Final 3 until the gates are closed and recorded.**

---

## 6. Decisive experiments that remain (must run in this order)

All cost figures are **HYPOTHESIS** (budget estimates transcribed from `Idea_0*/experiments.md` and `evolution_summary.md`). None has been run. Steps 0a and 0b are the §5 gates and come first because they are free and can kill two of the three members.

**Step 0a — GATE-A: camera-ID inventory (no GPU, hours).**
Inventory camera IDs on PYRONEAR-2025 or FIgLib.
→ **≥10 cameras:** continue to step 4. · **1–9 cameras:** pivot to event-disjoint-only, forfeit H2, re-argue Idea_02's Final-3 slot. · **No camera metadata anywhere:** **KILL Idea_02** by its own stop rule and promote a replacement via GATE-C.

**Step 0b — GATE-B: checkpoint-pair verification (no GPU, hours).**
Confirm one base/chat pair with identical vision encoder and identical coordinate tokenization, license usable.
→ **Pass:** continue to step 6. · **Fail:** **DESCOPE Idea_03** to a format-artifact study (the O1 branch as a standalone negative result) or replace it. Do not spend the ≤8 GPU-h before this resolves.

**Step 1 — Idea_01 synthetic sanity check (CPU, minutes). ~0 GPU-h.**
Run `Idea_01/src/amg_intensity_equiv.py` on synthetic piecewise-constant "CT".
→ **Threshold (FACT, from `experiments.md`):** if the AMG-mock (threshold connected components) does **not** beat SLIC even on synthetic blobs, *"the **implementation** is wrong — fix before real SAM."*
→ **Fix-and-repeat**, not kill. This step cannot validate the science; it can only invalidate the harness.

**Step 2 — Idea_01 correlation arm on real CT (≈2 GPU-h, HYPOTHESIS).**
SAM ViT-B AMG vs k-means (k ∈ {8,16,32}) vs SLIC vs multi-Otsu vs GMM, on **100 TotalSegmentator/MSD slices** — taking the larger of the two recorded figures (see §4.7; README and the killer list say 50, the Stage-5 block says 100; the larger is used and the discrepancy flagged rather than silently averaged). Three clinical windows. Pre-registered metrics: Hungarian mean IoU, ARI, boundary-F — all three reported, no metric shopping.
→ **CONTINUE** if IoU(AMG,k-means) > IoU(AMG,SLIC) on ≥2 windows. · **PIVOT** if only 1 of 3 windows shows it (H3 fails → setting artifact). · **KILL** if SLIC ≥ k-means on **all** windows.

**Step 3 — Idea_01 counterfactual arm + COCO control (the decisive experiment of the round; ~2 GPU-h incremental, HYPOTHESIS).**
Arm (i) monotone HU remap inside tissue with Sobel edges frozen; arm (ii) permute the high-frequency residual with per-superpixel HU mean preserved. Then the same protocol on COCO.
→ **CONTINUE as a mechanistic paper** if the intensity remap moves AMG substantially more than the texture shuffle, on ≥2 windows and ≥2 AMG settings. · **DOWNGRADE to evaluation note** if the two arms move AMG comparably — this is the residual's own *"else evaluation note"*; note §4.4 records that `Idea_01/reviewer_attacks.md` reads the same contingency as *do not submit*, and that conflict must be settled before writing. · **KILL the CT-specificity claim** if the COCO control reproduces the clustering equivalence. · **KILL** (Stage-5 gate) if AMG is closer to ground truth than to k-means **and** the texture shuffle moves AMG a lot.

*Steps 1–3 come first because Idea_01 is the cheapest, has no unverified data precondition, and is the round's `#1 start here`. Its counterfactual arm is the only experiment in Windows6 that can convert a residual obligation into a finished claim without acquiring anything new.*

**Step 4 — Idea_02 pilot: 1 seed × 3 split protocols (~10 GPU-h, HYPOTHESIS). Requires GATE-A passed.**
Pyronear-2025 subsample, YOLOv8n, splits {random, event-disjoint, camera-disjoint}, equal-N and class-ratio matched. Report image-level AP and FAR@recall. Plus camera-ID linear probe and empty-frame FPR seen vs unseen, with the ImageNet-pretrained control backbone and cluster bootstrap over events.
→ **CONTINUE to 3 seeds + second dataset** if camera-disjoint < random beyond seed std **and** the seen/unseen empty-frame gap is present. · **STOP** if random ≈ camera-disjoint within seed noise **and** probe ≈ chance **and** no empty-FPR gap — confirm with 2 more seeds before declaring. · **KILL** if the camera-disjoint drop vanishes under event-disjoint (H2 dead).

**Step 5 — Idea_02 pHash dedup rerun (incremental, HYPOTHESIS). Only if step 4 continues.**
Separates duplicate-frame leakage from camera signature.
→ **CONTINUE** if the gap survives dedup. · **DOWNGRADE** to a near-duplicate audit if the gap is fully explained by duplicates — at which point it restates the Voxel51 blog with numbers, which `Idea_02/proposal.md` treats as fatal to the framing.

**Step 6 — Idea_03 three-mode eval (≤8 GPU-h, HYPOTHESIS). Requires GATE-B passed.**
One verified pair, 2k RefCOCO, modes: free-form / grammar-constrained / likelihood rank of GT against ≤16 shared distractor boxes. Then the frozen-visual-token linear probe.
→ **O3 — representation tax** (likelihood gap present, probe drops): strongest outcome, continue. · **O2 — policy tax** (likelihood gap present, probe holds): continue. · **O1 — format artifact** (gap dies under likelihood): **write the negative result**; do not proceed to DPO. · **STOP** if the likelihood gap is ~0 on pair 1 **and** pair 2.

**Step 7 — Idea_03 text-only DPO control (1–2 × 24GB, days, HYPOTHESIS). Gated: only on O2 or O3.**
`Idea_03/experiments.md` is explicit — *"Do not run DPO unless observational gap survives format control."*
→ **CONTINUE to the causal claim** if text-only preference tuning still degrades localization (objective, not data mix). · **Restrict to the observational claim** otherwise; per `reviewer_attacks.md`, *"do not claim causal RLHF without H3."*

### Battle stop condition

**FACT.** No new fatal prior work was raised against the three survivors after Stage 4. The two kills (§1.1) absorbed the two fatal collisions the round found — Metrics Reloaded against F-022, CLIP-Driven Universal Model against F-036/037. The threat that remains is not a known paper but the **absence-defined novelty** of Idea_03 (§2.3.1), which no further reading can retire and only execution speed can protect.

---

## 7. Provenance

**Artifacts read to build this file:** `Windows6/README.md`, `Windows6/research_summary.md`; `selection_history/` — `stage5_top5.md`, `stage3_DE_top10.json.md`, `stage3_prior_work_kill_cheap.jsonl`, `stage4_reviewer2_cheap5.jsonl`, `auditor_overlay.md`, `reviewer_attacks.md`, `reviewer_summary.md`, `literature_anchors.md`, `evolution_summary.md`, `supervisor_log.md`, `stage2_ABCF_summary.md`, `stage2_DE_summary.md`; `Idea_01/` — `README.md`, `proposal.md`, `experiments.md`, `reviewer_attacks.md`, `roadmap.md`, `literature.md`, `references/math.md`; `Idea_02/` and `Idea_03/` — same set less `references/math.md`.

**Format reference (structure only, no content reused):** `Windows4/selection_history/stage6_battle.md` on branch `cursor/windows4-research-idea-evolution-2962` — source of the *"Unresolved disagreements kept explicit"*, *"Fatal flaws that ended threads"*, *"Decisive experiments that remain (must run in this order)"* and *"Battle stop"* section pattern. The Windows4 package sizes quoted in §3 were read from that branch's tree listing.

**Files written by W6-T2:** this file only. No existing file was modified.

**Left to W6-T3:** INCONSISTENCY-01…04 from `stage5_top5.md` §5; the status line in `README.md` / `research_summary.md` / `supervisor_log.md`; package thickening (GATE-D). **W6-T3 must not record the Final 3 as locked** — per §5 it is PROVISIONAL until GATE-A…D are closed.
