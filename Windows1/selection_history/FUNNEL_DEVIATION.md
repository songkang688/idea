# Funnel deviation — standard chain vs what Windows1 actually executed

Status: **retrospective audit.** No selection decision is re-opened and no conclusion in
`Windows1/README.md` or `Windows1/research_summary.md` is altered. Where this audit finds a
contradiction with those two documents, it is listed in §4 for human adjudication and left in place.

Epistemic labels per `Windows1/README.md`: KNOWN FACT, EVIDENCE, HYPOTHESIS, MODEL SPECULATION,
EXPECTED RESULT, ACTUAL EXPERIMENTAL RESULT.

**No ACTUAL EXPERIMENTAL RESULT exists in this round.** `Windows1/research_summary.md` states
"We have **not** trained models or measured Dice/mIoU/τ in this round"; `README.md` states
"No numbers in this archive are measured by us." Every count in this file is a count of *ideas or
decisions*, never a measurement. Every count is sourced.

---

## 1. Headline: the chain is real but the shape is wrong

The standard chain is **1000+ → 200 → 50 → 20 → 5 → 3**.
Windows1 executed **1065 → ~84 → ~20 → 12 → 8 → 5 → 3**.

Two structural facts follow, and both are recorded here rather than smoothed over:

- **Windows1 ran seven levels, not six.** `research_summary.md` labels Stage 5 as "8 engineered,
  then 5" — a 8 → 5 narrowing *inside* Stage 5. The standard chain has no such step; its Stage 5
  *is* the 5.
- **The middle of the funnel is 2–4× narrower than standard at every level.** Stage 2 kept ~84 where
  the standard keeps 200; Stage 3 kept ~20 where the standard keeps 50; Stage 4 kept 12 where the
  standard keeps 20. The funnel narrowed early and then had little left to cut.

**MODEL SPECULATION, flagged as such:** the early narrowing is consistent with the Stage-1 cloud
failures described in §3 leaving a smaller *reviewable* pool than the raw generated count suggests.
The ledger does not state this causal link, so it is not asserted as EVIDENCE.

---

## 2. Level-by-level comparison

| Level | Standard | Windows1 actual | Source file for the actual count | Independently reproducible from the repo? |
|---|---|---|---|---|
| Stage 1 raw | 1000+ | **≥1065** (SEG 365 + local VFM 350 + local ASM 350 + VFM-A 180 + ASM-A 180, with overlap) | `research_summary.md`; pools in `research_ledger/stage1_*` | **Partly.** `350 + 350` is exactly verifiable by counting IDs in the two local pool files. `365 + 180 + 180` is asserted by digests whose full idea text is not in this repo. `365+350+350 = 1065` reproduces the "≥1065" floor exactly. |
| Stage 2 | 200 | **~84 SEG keep** + unspecified VFM/ASM keepers | `research_summary.md`; `research_ledger/stage2_seg_review.md` | **No.** The ledger documents 48 named decisions + 15 promotions = **59** keep-side units. ~84 is not reconstructible. See §4-D. |
| Stage 3 | 50 | **~20 attacked** | `research_summary.md`; `research_ledger/stage3_priorwork_kill.md`, `stage3_vfm_kills.md` | **Yes for SEG.** The SEG sheet contains exactly 5 KILL + 4 SURVIVE + 11 MUTATE = **20 decision units**, matching "~20" exactly. The VFM sheet adds 13 more units (4 KILL + 8 MUTATE + 1 WEAK SURVIVE) that the "~20" figure does not appear to include. See `stage3_survivors.md`. |
| Stage 4 | 20 | **12 mutated forms**, no unconditional KEEP, one KILL | `research_summary.md`; `research_ledger/stage4_reviewer2.md` + recovered full panel | **Yes.** The recovered panel contains exactly 12 proposals P1–P12, one KILL (P10 = SEG-0193-M), and all others KEEP-IF-EXPERIMENT. See `stage4_candidates.md`. |
| — *(extra level)* | *none* | **8 engineered** | `research_ledger/meta_audit.md` "Updated working Top-8" | **Yes.** The Top-8 list is enumerated 1–8 in `meta_audit.md`. |
| Stage 5 | 5 | **then 5** | `research_summary.md`; `research_ledger/stage5_killers.md` | **No.** The engineer's Top-5 is enumerated, but a supervisor correction re-added a 6th, and the record never states the final five. See §4-E and `stage5_top5.md`. |
| Stage 6 | 3 | **Final 3** (A RetainSAM, B LesionSuppress, D DisagreeShift) | `research_summary.md`, `README.md` | **Outcome yes, process no.** The three winners are unambiguous. **No Stage-6 ledger file was ever written.** Backfilled as `stage6_battle.md`. |

### Note on the winner letters

`research_summary.md` labels the Final 3 "**A** RetainSAM, **B** LesionSuppress, **D** DisagreeShift" —
A, B, D with no C. The letters are Stage-6 slate labels, not directory names; the delivered
directories are `Idea_01`, `Idea_02`, `Idea_03` respectively. **There is no record of what "C" was**
or why it was dropped. Logged as §4-F.

---

## 3. Recorded causes of the deviation

These are transcribed from `Windows1/selection_history/evolution_summary.md` and
`Windows1/research_summary.md`. They are the *only* causes the round wrote down.

### 3a. Two Stage-1 cloud timeouts (EVIDENCE, stated twice)

`evolution_summary.md`: "Autonomous PI with ≤3 cloud sub-agents (`claude-fable-5-thinking-xhigh`).
**Two Stage-1 350-idea cloud runs timed out**; supervisor wrote local VFM/ASM pools and re-dispatched
180-idea batches."

`research_summary.md`, Stage 1 row: "**Cloud 350-idea runs timed out twice**; local pools + compact
batches completed the ≥1000 requirement."

Effect on the funnel: the ≥1000 requirement was met by *substitution*, not by the originally intended
route. The two local 350-idea pools in this repo are explicitly labelled "supervisor backup" in their
own titles, and the compact 180-idea batches (VFM-A, ASM-A) survive only as a ~1 KB keeper digest.
So three of the five Stage-1 pools have no reviewable idea text in this repository.

### 3b. Stage-2 reviewer blocked, then restarted (EVIDENCE)

`evolution_summary.md`: "**Stage-2 reviewer initially blocked (cloud workspace had no idea text)** and
was resumed with the full SEG list."

Effect on the funnel: the Stage-2 review that did complete covers the **SEG slice only**.
`stage2_seg_review.md` closes with the supervisor's own note "Global 1000 not yet complete: waiting
VFM + ASM pools." **No equivalent Stage-2 review sheet for the VFM or ASM pools exists in the
ledger.** The VFM/ASM material jumps straight from Stage-1 keeper digests to the Stage-3 kill sheet.
This is the single largest structural hole in the funnel and the most likely reason Stage 2 reads ~84
instead of 200.

### 3c. The cheap-killer rule compressed Stage 4 (EVIDENCE)

`stage4_reviewer2.md` records four proposals "Dropped by cheap-killer rule: 0252 (needs real annotator
generations), 0275 (nonce-word pilot only), 0240 factorial, 0103-M workshop." Selecting on
*cost-to-falsify* rather than on scientific merit narrows a level faster than the standard chain
expects, and it is why Stage 4 produced 12 rather than 20.

### 3d. Merges, not just kills (EVIDENCE)

Several levels shrank by *merging* units rather than eliminating them, which makes the headline counts
smaller without a corresponding loss of ideas:

- `meta_audit.md`: "merge 0275 with contamination; merge worst-case clicks with oracle-click leak".
- `stage3_priorwork_kill.md` carries a merged pair as one unit: `0103/0125`.
- `meta_audit.md` Top-8 #7 and #8 are themselves merges ("Worst-case/oracle-click interactive eval
  merge", "0275 + eval contamination merge (one eval slot)").

---

## 4. Missing links and internal discrepancies

Each item is a defect in the *record*, not a claim that a decision was wrong. Nothing here is
resolved unilaterally.

**A. No Stage 6 record at all.** `README.md` asserts "Stage 6 locked method + medical-safety
characterization + medical uncertainty method", and `reviewer_summary.md` lists three Stage-6 dissents,
so Stage 6 demonstrably happened. No ledger file documents it. Backfilled as `stage6_battle.md`,
which is explicitly labelled retrospective and reconstructed from `README.md`,
`reviewer_summary.md`, `evolution_summary.md`, `stage5_0276.md` and `meta_audit.md`.

**B. No Stage-2 review of the VFM/ASM pools.** See §3b. The ~700 ideas in the two local pools have
Stage-1 keeper marks and Stage-3 kill decisions but no Stage-2 scoring sheet. Unrecoverable from this
repository.

**C. Full idea text missing for three of five Stage-1 pools.** SEG-0001…0365, VFM-A 180, ASM-A 180.
`eliminated_ideas_summary.md` points at `/workspace/research_ledger/`, a cloud worktree path that is
not this repository. Only the two local 350-idea pools were committed.

**D. Stage-2 counts do not reconcile.** `Windows1/selection_history/reviewer_summary.md` states
"31 KEEP200 / 8 PROTECT-HRHR / 14 MUTATE / 4 KILL". Counting the ID lists in
`research_ledger/stage2_seg_review.md` gives:

| Bucket | `reviewer_summary.md` claims | IDs actually listed in `stage2_seg_review.md` | Match? |
|---|---|---|---|
| KEEP200 | 31 | **23** | no |
| PROTECT-HRHR | 8 | **6** (0019, 0054, 0074, 0252, 0355, 0276) | no |
| MUTATE | 14 | **15** | no |
| KILL | 4 | **4** (0048, 0061, 0170, 0274) | **yes** |
| *(separate list)* Under-ranked promotions | not given | 15 | — |

The ledger's four buckets sum to 23+6+15+4 = **48**, which matches its own header "## Named-48
decisions" exactly, so `stage2_seg_review.md` is internally consistent. The 31/8/14 figures in
`reviewer_summary.md` are therefore the outlier. **Not corrected here** — `reviewer_summary.md` is an
existing Windows1 conclusion document. Referred for human adjudication.

**E. The Stage-5 five is never stated.** `stage5_killers.md` enumerates an "Engineer Top-5", then
overrides it: "SUPERVISOR CORRECTION: 0276-M shape-prior field was omitted from this Stage-5 prompt
(R2 ranked it #1, inference-only killer). **Must add back before locking Top-5.**" The file then
gives a five-entry "Likely final-3 pool" that is *not* the engineer's Top-5. No file states which
five entered Stage 6. `stage5_top5.md` reconstructs the candidate set and marks the ambiguity
explicitly instead of picking a five.

**F. Slate letter "C" is unaccounted for.** See §2. Final 3 is labelled A/B/D. No record of C.

**G. Two ranked lists at the Stage-4/5 boundary disagree, and neither supersedes the other.**
The R2 Top-7 in `stage4_reviewer2.md` ranks `0276-M` first and does not contain
`Frozen/tuned n*`, `0046-M`, `0074-M` or the interactive-eval merge. The Top-8 in `meta_audit.md`
contains all four of those and **omits 0276 entirely** (relegating it to "Protect 0276 … as benches").
`stage5_killers.md` shows the consequence: the engineer worked from the Top-8, so 0276-M fell out and
had to be reinstated by supervisor correction. Recorded in `stage4_candidates.md` §5 and
`stage5_top5.md` §2.

**H. Namespace error: `A0263`.** `stage3_vfm_kills.md` lists `A0263 constrained SAM-FT` under MUTATE.
The `A` namespace is VFM-A/ASM-A, which `stage1_vfma_asma_keepers.md` caps at 180 ideas each, so
`A0263` cannot exist in it. The intended referent is `VFM-0263` in `stage1_vfm_local_pool.md`
("Constrained FT: maximize target Dice s.t. SA-1B drop < ε"), which `stage4_reviewer2.md` cites
correctly as `VFM-0263/0274`. **Not silently corrected** in the ledger; flagged here.

**I. `stage4_reviewer2.md` misstates where its own panel lives.** It says the full panel is
"on branch cursor/reviewer2-stage4-kill-panel-5733 (cloud worktree, **not this repo**)". That branch
*is* in this repository and the panel was recovered from it. See `stage4_candidates.md` §1.
The parenthetical is factually wrong; flagged rather than edited.

**J. Five Stage-3 SEG survivors and seven Stage-3 VFM survivors vanish before Stage 4 with no
recorded reason.** Enumerated in `stage3_survivors.md`, each marked
`NO RECORDED REASON — 需人工确认`.

---

## 5. Contradictions with `README.md` / `research_summary.md`

Per the constraints on this task, the two documents above are authoritative and unmodified. This
section exists so that any tension is visible rather than buried.

| Item | `README.md` / `research_summary.md` says | This audit finds | Disposition |
|---|---|---|---|
| Stage-1 pool sizes | "local VFM ~350 + local ASM ~350" | exactly 350 and 350 | **No conflict** — "~" is simply conservative. Recorded as a tightening, not a correction. |
| Stage-1 completeness | "local pools + compact batches completed the ≥1000 requirement" | The requirement was met as a *count*; the reviewable *text* for 725 of the 1425 gross ideas is not in this repo | **Tension, not contradiction.** The claim is about generation, not archival. Left standing; gap logged at §4-C. |
| Stage-2 breadth | "~84 SEG keep + VFM/ASM keepers" | Only a SEG review sheet exists; no VFM/ASM Stage-2 sheet, and ~84 is not reconstructible | **Referred.** §4-B, §4-D. |
| Stage-6 existence | "Stage 6 locked method + medical-safety characterization + medical uncertainty method" | Corroborated by three independent dissents in `reviewer_summary.md`; no primary record | **Accepted as KNOWN FACT that Stage 6 occurred**; its content is reconstructed and labelled retrospective. §4-A. |
| Final-3 labels | "A RetainSAM, B LesionSuppress, D DisagreeShift" | No "C" anywhere in the archive | **Referred.** §4-F. |

---

## 6. What this audit does *not* do

- It does not re-select. Final 3 is locked and out of scope.
- It does not treat any Stage-2 score as fact. `stage2_seg_review.md` states "Scores are REVIEWER
  JUDGMENT not facts" and "Do not treat Pub=L as verified novelty"; both constraints are honoured in
  the backfilled files, which report decisions and their stated rationales without re-asserting the
  scores as findings.
- It does not touch `research_ledger/`. Not one byte of those 12 files is modified, moved or renamed.
  Rationale in `LEDGER_INDEX.md` §4.
- It does not invent reasons. Every reconstructed row either cites a ledger file or is stamped
  `NO RECORDED REASON — 需人工确认`.
