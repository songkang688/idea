# Stage 5 → Top-5 (Windows4)

Date: 2026-08-29 (UTC). **Backfilled record** — see §0.

Epistemic status: **BOOKKEEPING / REVIEW JUDGMENT.** This file adjudicates nothing. It transcribes
the 20 → 5 step from records that already exist in this directory.

Evidence labels used below:
**FACT** (verifiable in a file in this repo, or in released code/dataset cards) ·
**VERIFIED PRIOR WORK** (citation carried from `stage3_kill_*.md` / `stage4_r2_set*.md`, verified there, not
re-verified this pass) · **HYPOTHESIS** · **SPECULATION** · **EXPECTED RESULT** · **ACTUAL RESULT**.
These map onto `supervisor_log.md § Epistemic labels in force` as
KNOWN FACT → FACT, EVIDENCE → VERIFIED PRIOR WORK, MODEL SPECULATION → SPECULATION,
ACTUAL EXPERIMENTAL RESULT → ACTUAL RESULT; HYPOTHESIS and EXPECTED RESULT are unchanged.

> **No ACTUAL RESULT appears anywhere in this file.** `README.md` states this run's status as
> "no experimental numbers were measured in this run", and that `Idea_01/artifacts/e0_smoke/` is a
> "**stub-backend harness check** (boxfill/oracle stubs on synthetic data), **not** a SAM/COCO result".
> Every number quoted below is a *pre-registered threshold or budget estimate* copied from a Stage-4
> file, never a measurement. (FACT)

Anything not traceable to a file is tagged **INFERRED** with the sentence it rests on.

---

## 0. Why this file exists (provenance)

**FACT.** The funnel recorded in `evolution_summary.md` is 1080+ → 200 → 50 → 20 → 5 → 3
("Stage 5–6: Top 5 then battle notes → lock 3"). Every level had a standalone file except Stage 5:
the Top-5 was written *inside* `stage4_top20.md` as the subsection `## Top 5 (Stage 5)`.

This file extracts that subsection into its own auditable record and attaches, for each of the 20
Stage-4 seats, the obligation and the disposition already on record. **It changes no verdict.**
`stage4_top20.md` and `stage6_battle.md` were not edited; the Final 3 and `Idea_0{1,2,3}/` are untouched.
Where the existing files disagree with each other, the disagreement is listed in §6 for human
adjudication rather than resolved here.

---

## 1. Input and output counts

| | Count | Source |
|---|---|---|
| **Input** | **20 seats** | `stage4_top20.md`, heading: "WEAK ACCEPT / SILENCED (20 slots; 19 unique + P082 as gate not a paper)" |
| **Output** | **5 entries** | `stage4_top20.md`, `## Top 5 (Stage 5)` |

**FACT — seat arithmetic.** The 5 output entries consume **6** of the 20 input seats, because Top-5
entry 3 is a merge: "P103+P096 AlphaSmoke (transfer + metric protocol)", and P103 and P096 hold
Top-20 ranks 6 and 4 respectively. Therefore **14 seats did not advance as independent Top-5 entries**,
not 15. §4 enumerates all 14. (The naive subtraction 20 − 5 = 15 double-counts the P103/P096 merge.)

**FACT — P082 is not a paper seat.** `stage4_top20.md` labels it "P082 as gate not a paper" and its
binding obligation is "Run first on released ckpts". It is carried inside Top-5 entry 2 as the gate
("P065 PromptAmnesia (gated by P082)"), so of the 20 seats, 19 are candidate papers and 1 is a gate.

---

## 2. Top-5

Order and content are copied verbatim from `stage4_top20.md § Top 5 (Stage 5)`. (FACT)

| # | ID(s) | Codename | Scientific question (one line) | Binding obligation inherited from `stage4_top20.md` | Unresolved risk carried into Stage 6 |
|---|-------|----------|--------------------------------|-----------------------------------------------------|--------------------------------------|
| 1 | P14 | **SeeingInside** | Does SAM actually use image evidence *inside* a tight box, or is it a box→mask interpolator? | "On-manifold inpaint/swap + box→mask nulls" | Off-manifold/positional-leakage attack is answered only if the counterfactuals stay on-manifold; the "null everyone already believes" payoff asymmetry |
| 2 | P065 (+ P082 gate, + P177 absorbed) | **PromptAmnesia** | Does domain PEFT destroy prompt-type skills (points/negatives/multimask) at matched in-domain Dice? | "Mixed-prompt FT column"; gate P082 "Run first on released ckpts" | P082 may deflate the whole thread; coverage-vs-forgetting confound; shared-grid poisoning; "matched gain" is one under-specified convention |
| 3 | P103 + P096 | **AlphaSmoke** | Does matting pretraining beat segmentation pretraining on *real smoke*, and do binary rankings reverse under alpha metrics? | P103: "Binarized-matting arm; real-smoke primary". P096: "Measured-alpha real arm" | Synthetic-alpha circularity; matting ≈ matting-binarized would kill the mechanism; mMse column could kill the reversal; measured-alpha capture is a data/annotation risk |
| 4 | P063 | **RefractionFeatures** | Does frozen-ViT feature displacement through glass track optically predicted refraction warp? | "A1-067 first; IOR=1 twins" | Sub-patch blindness vs. pixel-correspondence null; Trans10K/GDD are single-image so new capture is required; heavier rendering cost |
| 5 | P079 | **MemoryProbe** | Does SAM2's memory encode position/order rather than appearance? | "Subtract explicit time encodings" | Live scoop risk on the SAM2-analysis line; position–appearance correlation is intrinsic to natural volumes; the *delta* at the memory stage is the claim, not raw decodability |

> **Naming caution (FACT).** `P079` (S-079, SAM2 memory probe, Set A) and `P079f` (B1-079, FSS
> background-swap, Set C) are different projects. P079 advances; P079f does not (§4).

### 2.1 Per-entry detail

Each block gives the obligation with its source, then the risk with its source. Scientific-question
wording is taken from `README.md § This round's three Ideas` where a Final-3 codename exists, and from
`stage3_top50.md § Stage-4 attack list` for P063/P079. (FACT)

**1 — P14 SeeingInside.** *Obligation:* `stage4_top20.md` rank 1 — "On-manifold inpaint/swap + box→mask
nulls". `stage4_r2_setA.md § P14` spells out the four parts: "(a) make **on-manifold natural
counterfactuals** the primary intervention — diffusion-inpaint the object out (or swap in a different
object) with the box held fixed; (b) demote embedding-zeroing / S-604 patch-shuffle to secondary
convergence checks; (c) add the prompt-only and learned box→mask nulls, matched per instance on
convexity; (d) make low-contrast medical the primary endpoint". Set A also records that the original
instrument alone fails: "The original S-014 embedding-zeroing instrument alone: REJECT." (FACT)
*Risk:* Set A's asymmetric-payoff attack — "if Dice collapses, the result is the null everyone already
believes ('SAM sees')" — is a ceiling that no redesign removes. (FACT) Set A's WEAK ACCEPT was
"conditional on the redesign **and the P107v merge**"; the merge half was overruled downstream
(`stage4_top20.md` REJECTs "P107v-as-flagship (HalluSegBench scoop)"; `stage6_battle.md`: "Supervisor:
**do not merge**"). **INFERRED:** P14 therefore enters Stage 6 with one clause of its Stage-4 survival
condition deliberately unsatisfiable as written; this rests on the two quoted sentences and is a
bookkeeping observation, not a re-judgement. Additionally, Set A obligation (d) makes low-contrast
medical the *primary* endpoint while `README.md § Most recommended` credits Idea_01 with "does not
require medical FT compute" — **INFERRED** these are compatible only if the medical endpoint is
evaluation-only (no fine-tuning); flagged in §6.

**2 — P065 PromptAmnesia, gated by P082.** *Obligation:* `stage4_top20.md` rank 2 — "Mixed-prompt FT
column"; rank 8 P082 — "Run first on released ckpts". `stage4_r2_setB.md § P065`: "The forgetting claim
survives **only if the prompt-type ordering persists inside the mixed-prompt column** — that column
isolates forgetting from coverage; the box-only column alone proves nothing", and "Verdict: WEAK
ACCEPT. Flagship of the thread, but the paper is the mixed-prompt column and the oracle-gap
decomposition; without them it is SAM-Med2D's table re-plotted." (FACT)
*Risk:* `stage6_battle.md § Decisive experiments` item 1 — "P082 noise-floor envelope (1–2 GPU-days) —
if 'forgetting' is thresholding, **pivot Idea_02**". (FACT) Set B's cross-paper attacks 1 and 2 remain
open against this entry: "**Shared-grid poisoning.** P065, P177, P031, P082 all reuse one fine-tuning
checkpoint grid … a single recipe flaw … contaminates four papers at once", and "**'Matched gain' is a
single point of failure.**" (FACT) `README.md` adds the crowding ceiling: "crowded by CA-SAM/Gu et al.
unless the mixed-prompt column is the paper". (FACT / VERIFIED PRIOR WORK for the citations)

**3 — P103 + P096 AlphaSmoke.** *Obligation:* `stage4_top20.md` rank 6 P103 — "Binarized-matting arm;
real-smoke primary"; rank 4 P096 — "Measured-alpha real arm". `stage4_r2_setA.md § P103` fixes the
four-arm design "{COCO-seg, matting, matting-binarized, scratch} at matched fine-tune budgets …
**primary endpoint on real smoke**", and `stage4_r2_setC.md § P096` makes both the measured-alpha arm
and the mMse column "**binding**": "Without the measured-alpha arm, attack 3 stands and the verdict
flips to REJECT." (FACT)
*Risk:* two pre-registered kill conditions travel with this entry. Set A: "If matting ≈
matting-binarized, the soft-boundary mechanism is dead even if the transfer helps — report that and
stop." Set C: "show whether mMse against *binary* GT rank-correlates with alpha-MAE against *alpha* GT.
If it does (τ > 0.8) … pillar 1 dies — pre-registered kill condition." (FACT — thresholds are
pre-registered, **not** measurements.) `README.md`: "R2 requires a measured-alpha arm and real-smoke
primary; data/annotation risk is higher". (FACT) Set A's residual circularity attack also survives by
design: alpha GT "exists only where smoke was synthetically composited … or subjectively annotated"
(Set C attack 3). (FACT)

**4 — P063 RefractionFeatures.** *Obligation:* `stage4_top20.md` rank 3 — "A1-067 first; IOR=1 twins".
`stage4_r2_setA.md § P063`: "**Can an experiment shut me up? YES — if the program is reordered.** …
Mitsuba scenes with an IOR sweep including IOR = 1.0 twins … regress per-patch feature displacement on
predicted optical warp **with pixel-correspondence R² as the printed null**", and "A1-063 as standalone
flagship: REJECT." (FACT)
*Risk:* the sub-patch squeeze is unresolved — "refraction warps through common glassware are frequently
sub-patch (<16 px), invisible to patch-quantized ViT features, so R²≈0 there is a resolution artifact,
not absent physics; supra-patch warps are trackable by raw pixel correspondence". Plus a data risk:
"Trans10K/GDD are single-image benchmarks, so the two-frame method needs re-shot or newly captured
data". (FACT) `stage6_battle.md` records the cost/ceiling trade that made it a backup: "glass physics
has higher ceiling and heavier rendering cost". (FACT)

**5 — P079 MemoryProbe.** *Obligation:* `stage4_top20.md` rank 5 — "Subtract explicit time encodings".
`stage4_r2_setA.md § P079`: "**Verdict: WEAK ACCEPT**, conditional on (a) and (b) being mandatory",
where (a) is "regress out the known temporal encodings, probe the residual" and (b) "report the
position:appearance information ratio at encoder vs memory — the *delta* is the claim". "The headline as
originally designed: REJECT." (FACT)
*Risk:* Set A flags an open scoop — "Scoop risk is live (the SAM2-analysis line, arXiv:2503.00042)"
(VERIFIED PRIOR WORK, per Set A's citation policy; not re-verified this pass) — and an
identification problem that no probe removes on natural data: "in videos and volumes, position and
appearance are strongly correlated … linear probes on correlated nuisances identify nothing without
decorrelation". (FACT)

---

## 3. Rule basis for advancement

**FACT.** `evaluation_rubric.md` forbids ranking by mean score ("Do **not** rank by mean score. Use a
decision rule.") and supplies the two lists the Stage-4 files argue from:

- *Survival rules:* "High-risk, high-upside with a cheap Killer Experiment"; "Simple counter-intuitive
  hypothesis"; "Extreme reviewer disagreement"; "Can be killed in <1 GPU-day".
- *Kill rules:* "Core novelty is 'new module'"; "Hypothesis is not falsifiable"; "Killer experiment
  requires a new foundation-model pretrain"; "Closest prior work already ran the same experiment
  (Stage 3)"; "Reviewer #2 attack cannot be answered by an experiment (Stage 4)".
- *ROI:* dimension 14, "Research ROI = (upside × falsifiability) / (compute × calendar friction)".

**FACT.** No seat entering Stage 5 was cut by a *kill rule* — all 20 had already cleared Stage 4's
"survival iff a realistic experiment would silence the attack" bar. The 20 → 5 step is therefore a
**quota/ROI ranking**, and the reasons in §4 are correspondingly of three recorded kinds:
(a) an explicit cut or de-prioritisation instruction in a Stage-4 file; (b) an explicit
ceiling/downgrade statement in a Stage-4 file ("not a flagship", "demotes to a note", "one figure");
(c) a Stage-6 adjudication that folded the seat into a survivor. Each row in §4 is tagged with which
kind applies, so a reader can see where an explicit cut note exists and where only a ceiling does.

---

## 4. 20 → 5: disposition of the 14 non-advancing seats

Ranks are `stage4_top20.md` Top-20 ranks. **Disposition** distinguishes *absorbed* (still funded inside
a Final-3 package), *gate* (runs, but is not a paper), *demoted* (kept as arm/appendix/companion), and
*deferred* (survived Stage 4, no Stage-5 seat). **Basis kind** is (a)/(b)/(c) per §3.

| Rank | ID | Disposition | Recorded reason | Basis |
|------|-----|-------------|-----------------|-------|
| 7 | P177 | **Absorbed** into Top-5 entry 2 | `stage6_battle.md` locks "**Idea_02 PromptAmnesia (P065/P082/P177)**" — P177 is funded inside the PromptAmnesia package, not cut. `stage4_r2_setB.md § P177` had already denied it standalone status: "The freeze ablation alone (S-177) is one figure and remains REJECT as a standalone; it lives only as an arm inside this design", and placed it last in the eval-reuse chain: "P082 first … then P065 → P031 → P177". | (c) + (b) |
| 8 | P082 | **Gate**, not a paper seat | The status is fixed in `stage4_top20.md`'s own section heading — "20 slots; 19 unique + **P082 as gate not a paper**" — and its rank-8 obligation is "Run first on released ckpts". `stage4_r2_setB.md § P082`: "**WEAK ACCEPT — and it must run FIRST** … it is the gatekeeper that decides whether P065/P177 are measuring signal", and records the self-defeating branch: "if the audit finds forgetting *does* exceed the noise floor, this 'paper' is a confirmation note." Carried into Top-5 entry 2 as "gated by P082" and into `stage6_battle.md § Decisive experiments` item 1. | (a) |
| 9 | P107 | **Demoted** to an ablation chapter of entry 2 | `stage6_battle.md § Unresolved disagreements`: "P065 vs P107 for PEFT slot: P107 is more 'constructive mechanism' but smaller blast radius. **P065 is the PEFT paper**; P107 is an ablation chapter." `stage4_r2_setB.md § P107` adds the non-negotiable condition it would have had to carry alone: "the decoupled-metric requirement is non-negotiable — with raw boundary-F this is unpublishable regardless of outcome." | (c) |
| 10 | P044 | **Deferred** — explicitly budget-capped | `stage4_r2_setB.md § P044`: "The significance attack stands as a ceiling: this is a strong short paper or workshop headliner, not a main-track flagship; **Stage 5 should budget it accordingly and must not let it absorb resources from P065/P082.**" This is a direct Stage-5 instruction not to spend a flagship slot on it. | (a) |
| 11 | P042 | **Deferred** | **NO RECORDED REASON — 需要人工确认.** P042 carries `stage4_r2_setC.md`'s strongest verdict class ("SILENCED", confidence Med-High, "Nothing structural" under *What no experiment can fix*) and is listed **first** in Set C's "Compute ranking of survivors (cheapest first): P042, P096, P079f, P228, P040". Under `evaluation_rubric.md` ROI it therefore reads as a strong candidate, yet no file in `selection_history/` states why it did not take a Top-5 seat; `stage6_battle.md` does not mention it at all. Attacks that remain *on record but were answered* (so they are context, **not** a cut reason): "Hygiene-as-paper" and "'Fraction of the gap' is ill-posed". | none |
| 12 | P031 | **Demoted** to a cell/appendix of entry 2 | `stage4_r2_setB.md § P031`: "**WEAK ACCEPT**, with the explicit warning that **the modal outcome is a recipe footnote**", surviving "only in the cell {IoU-loss on, zero-shot, recalibrated}", and "If the easy fix kills the desync, report the kill inside P082's deflation frame; **do not stretch it into a paper.**" It is also mid-chain in the shared-grid eval order ("P065 → P031 → P177"), so it cannot be scheduled ahead of entry 2. `stage4_r2_setB.md § P110` additionally routes P110's panel into "P065/P031 appendices". | (a) + (b) |
| 13 | P079f | **Deferred** | `stage4_r2_setC.md § P079f`, *What no experiment can fix*: "If the effect exists but is fully absorbed by the 2024 fixes, the paper **demotes to a benchmark-hygiene note**. Acceptable risk." The prior-work pressure is on record as near-miss on the Stage-3 kill rule: Zhu et al. CVPR 2024 and TBS AAAI 2024 mean "the 'shortcut' you reveal is the motivation section of two 2024 method papers" (VERIFIED PRIOR WORK). Set C survived it only by narrowing the deliverable, and four controls are binding. | (b) |
| 14 | P051 | **Deferred** — explicitly not funded | `stage4_r2_setC.md § Notes for the supervisor` 3: "**The two training-heavy survivors should not both be funded; P051's shelf-life risk makes P061u the safer of the two if forced to choose.**" Cost on record: "~40–80 training runs … **borderline against the rubric's 'weeks not years'**" — i.e. against `evaluation_rubric.md` dim. 5/6 and the ROI rule. *What no experiment can fix:* "Shelf life." | (a) |
| 15 | P040 | **Deferred** | `stage4_r2_setC.md § P040`, *What no experiment can fix*: "If the two-factor sweep shows width effects are fully absorbed by contrast, no framing rescues a standalone paper — that outcome is **one figure inside the medical-eval thread**. The submission must be built so that this demotion path is explicit." Verdict is conditional ("SILENCED-IF-MUTATED") and the core attack is "**'Quantified lore'**" against a published GLM (VERIFIED PRIOR WORK). | (b) |
| 16 | P052 | **Deferred** — re-scoped | `stage4_r2_setB.md § P052`: "**WEAK ACCEPT — re-scoped.** Mandatory: retitle the claim to the measurable interaction … '**objectness prior**' may appear as interpretation, **never as the result**", kept above the line only "despite the fragile chain". A seat whose headline word was struck cannot carry a Top-5 entry. | (b) |
| 17 | P228 | **Deferred** — companion role | `stage4_r2_setC.md § P228`: "SILENCED-IF-MUTATED — within-model prompt-manipulation design binding; cross-model 'vision-only vs VLM' comparisons excluded from the headline", and "**Pairs naturally with the demoted P107v residue**". Its Top-20 obligation already narrows it to one target: "BiomedParse; not B1-107". Residual risk on record: "If the prompt-causal share is ~0 … it re-enters Udandarao's shadow." | (b) |
| 18 | P101 | **Deferred** — first to cut | Strongest explicit cut note in the corpus. `stage4_r2_setA.md § P101`: "**WEAK ACCEPT** — lowest tier; **first to cut if the 20-slot quota binds.** Without the matched-area baseline table: REJECT." And § *Consequences for the pool* 1: "cut my accepts in this order: **P101 first**, P103 second". Core attack: the headline is "close to guaranteed by construction" (attention temperature, not a granularity code). | (a) |
| 19 | P061u | **Deferred** — flagship status denied | `stage4_r2_setC.md § P061u`, *What no experiment can fix*: "**This can never be a flagship** — the ceiling is a solid, well-controlled attribution study at a second-tier venue or a strong workshop-to-main pipeline." Cost: "~50–80 GPU-days total. Heavy but within one-lab feasibility" — against ROI it loses to the eval-only survivors. | (a) + (b) |
| 20 | P177-arm | **Demoted** — never standalone | The seat is defined as non-standalone in `stage4_top20.md` itself: its rank-20 one-liner is "Freeze-encoder figure only" and its binding obligation is the single phrase "**Not standalone**". Concurring: `stage4_r2_setB.md § P177` — "The freeze ablation alone (S-177) is one figure and remains REJECT as a standalone." | (a) |

### 4.1 Counts

**FACT.** 14 rows above + 6 seats consumed by the 5 Top-5 entries = 20 input seats. By disposition:
absorbed 1 (P177), gate 1 (P082), demoted 3 (P107, P031, P177-arm), deferred 9 (P044, P042, P079f,
P051, P040, P052, P228, P101, P061u). Exactly **one** row has no recorded reason: **P042** (rank 11).

### 4.2 Seats that never reached Stage 5

**FACT**, for funnel completeness: `stage4_top20.md § REJECT (out)` lists "P060, P001, P004, P007, P110,
P108, P107v-as-flagship (HalluSegBench scoop)". These were cut at Stage 4, are not part of the 20, and
are not re-litigated here. `stage4_r2_setA.md` retains P001 "as hygiene gate"; `stage4_r2_setB.md`
routes P110's reporting panel into "P065/P031 appendices" and logs P108's drift statistic "as a free
covariate in the grid".

---

## 5. Interface to Stage 6

Transcription only. Stage 6 is adjudicated in `stage6_battle.md`; nothing here re-decides it.

**FACT.** Of the Top-5, three became the Final 3 and two are backups:

| Top-5 # | ID(s) | Outcome | Package |
|---|---|---|---|
| 1 | P14 | **Final 3** — recommended #1 | `Idea_01/` SeeingInside |
| 2 | P065 (+P082 gate, +P177) | **Final 3** | `Idea_02/` PromptAmnesia |
| 3 | P103 + P096 | **Final 3** | `Idea_03/` AlphaSmoke |
| 4 | P063 | **Backup** | — |
| 5 | P079 | **Backup** | — |

`stage4_top20.md § Final 3` states the lock and the backup condition: "See `stage6_battle.md`. Locked:
… **Idea_01 SeeingInside (P14)** — recommended #1 · **Idea_02 PromptAmnesia (P065/P082/P177)** ·
**Idea_03 AlphaSmoke (P103/P096)**" and "P063/P079 are first backups if a killer experiment dies in
week 1." `README.md § This round's three Ideas` matches. (FACT)

**FACT.** `stage6_battle.md` records the two rulings that decided the third slot and the PEFT slot:
"**Third slot = AlphaSmoke.** P063 is backup" and "**P065 is the PEFT paper**; P107 is an ablation
chapter" — and keeps one disagreement explicitly open: Set A "wants P14 merged with P107v; Set C
**scooped P107v** (HalluSegBench). Supervisor: **do not merge**."

**FACT.** Execution order for the Final 3 is fixed in `stage6_battle.md § Decisive experiments that
remain (must run in this order)`: P082 noise-floor envelope, then P14 on-manifold inpaint, then P103
linear-probe / tiny-head. `README.md § Next experiment to run (this week)` is consistent with it.

**FACT.** All three packages are "**ready to start killer experiments**" per `README.md`; no killer
experiment has been run. Backup activation is conditioned on failure "in week 1", which has not
occurred and cannot be recorded here.

---

## 6. Consistency with `stage4_top20.md`

**Claim of this section (FACT).** This file is an extraction, not a revision: membership, ordering, IDs,
codenames and merge structure are the same five entries as `stage4_top20.md § Top 5 (Stage 5)`, in the
same order. The table below diffs them entry by entry.

| # | `stage4_top20.md § Top 5 (Stage 5)` | This file §2 | Identical? |
|---|---|---|---|
| 1 | "P14 SeeingInside" | P14 SeeingInside | yes |
| 2 | "P065 PromptAmnesia (gated by P082)" | P065 PromptAmnesia, P082 gate | yes |
| 3 | "P103+P096 AlphaSmoke (transfer + metric protocol)" | P103 + P096 AlphaSmoke | yes |
| 4 | "P063 RefractionFeatures" | P063 RefractionFeatures | yes |
| 5 | "P079 MemoryProbe" | P079 MemoryProbe | yes |

**No differences in Top-5 content.** The items below are *observations about the existing corpus*,
surfaced by writing this file. They are listed for human adjudication and **none of them was acted on**:
no existing file was edited, no verdict changed, and `Idea_0{1,2,3}/` were not touched.

1. **Seat arithmetic, 15 vs 14.** Subtracting 5 from 20 suggests 15 non-advancing seats; the true
   number is 14 because Top-5 entry 3 merges two seats (P103 rank 6 + P096 rank 4). Recorded in §1
   and §4.1. No file is wrong; the merge is just easy to miscount. (FACT)
2. **Top-5 order ≠ Top-20 rank order.** `stage4_top20.md` ranks P063 at 3, P096 at 4, P079 at 5,
   P103 at 6, but its Top-5 subsection orders them P14, P065, P103+P096, P063, P079 — AlphaSmoke moves
   from ranks 4/6 up to 3rd. `stage6_battle.md` supplies the rationale ("smoke transfer has public data
   and a one-week killer. **Third slot = AlphaSmoke.**"), so this is a documented re-ordering rather
   than an inconsistency, but the two orderings are not the same list and a reader diffing them will
   notice. (FACT)
3. **Set A's cut order vs the outcome for P103.** `stage4_r2_setA.md` instructed "cut my accepts in
   this order: P101 first, **P103 second**", yet P103 advanced to Top-5 and into the Final 3 as
   `Idea_03/`. Set A's instruction was scoped to "if the global 20-slot quota binds", and
   `stage6_battle.md` overrides it for the third slot with a stated reason, so the two are reconcilable
   — but the reconciliation is nowhere written down. **Flagged for human confirmation.** (FACT for the
   quotes; the reconciliation is **INFERRED** from "if the global 20-slot quota binds" plus
   "Third slot = AlphaSmoke".)
4. **P042 has no recorded Stage-5 reason.** See §4 rank 11. It holds Set C's top verdict class and its
   cheapest-compute rank, so its absence from the Top-5 is unexplained by any file in
   `selection_history/`. **Needs human confirmation** — either a reason exists off-record, or the seat
   was dropped by oversight. (FACT that no reason is on record.)
5. **An outstanding Stage-5 obligation appears not to have been discharged.**
   `stage4_r2_setC.md § Notes for the supervisor` 1 states: "The stage3_top50 flagship list needs the
   corresponding edit at Stage 5" — because P107v's flagship status was revoked. `stage3_top50.md`
   still lists "10. **P107v** B1-107 — Inpaint-object-out; phantom dense masks (VLM hallucination)"
   under "### SURVIVE (flagship)". `stage4_top20.md` and `reviewer_summary.md` do record the
   revocation, so the conclusion is not in doubt anywhere else; only the Stage-3 file is stale.
   **Not edited here** (this task is limited to creating this file). **Flagged for human action.** (FACT)
6. **P14's medical-endpoint obligation vs the README's compute claim.**
   `stage4_r2_setA.md § P14` obligation (d) is "make low-contrast medical the primary endpoint", while
   `README.md § Why not the others as #1` credits Idea_01 with "does not require medical FT compute".
   **INFERRED:** compatible if and only if the medical endpoint is evaluation-only; the two sentences
   never say so explicitly. **Flagged for human confirmation.** (INFERRED, resting on those two quotes.)
7. **P14's Set-A survival condition is only partially satisfiable as written.**
   Set A's WEAK ACCEPT was "conditional on the redesign **and the P107v merge**"; the merge was
   subsequently forbidden (`stage6_battle.md`: "Supervisor: **do not merge**") after P107v was rejected
   as a flagship. The redesign clause stands and is what `stage4_top20.md` rank 1 encodes; the merge
   clause is void. Recorded so that a later reader does not treat the void clause as an unmet
   obligation. (FACT for the quotes; **INFERRED** that the clause is void rather than outstanding.)

**Funnel completeness after this file (FACT).** 1080+ → `stage1_*.md` · 200 → `stage2_top200.md` +
`stage2_top200_ids.txt` · 50 → `stage3_top50.md` · 20 → `stage4_top20.md` · **5 → this file** ·
3 → `stage6_battle.md`. Every level of the funnel in `evolution_summary.md` now has a standalone record.
