# Stage 5 → Top-5 (Windows1) — reconstructed, with the five NOT pinned by the record

Status: **retrospective reconstruction.**

`Windows1/research_summary.md` describes Stage 5 as "**8 engineered, then 5**". The 8 is enumerated in
the ledger and is reproduced exactly below. **The 5 is not.** No file in this archive states which
five candidates entered Stage 6.

This file therefore does two separate things, and keeps them separate:

- §1–§3 record what *is* written down: the Top-8, the engineer's Top-5, the supervisor's correction,
  and the cheap-killer designs.
- §4 reconciles them into a candidate set for Stage 6 and **marks every row that the record does not
  pin as `AMBIGUOUS — 需人工确认`**, rather than choosing a five and presenting it as the five.

Sources: `research_ledger/meta_audit.md`, `research_ledger/stage5_killers.md`,
`research_ledger/stage5_0276.md`, `research_ledger/cheap_killers_0252_0046.md`,
`Windows1/selection_history/eliminated_ideas_summary.md`,
`Windows1/selection_history/reviewer_summary.md`, `Windows1/selection_history/evolution_summary.md`.

Epistemic labels per `Windows1/README.md`. All costs and gates below are HYPOTHESIS or design
specification. **No ACTUAL EXPERIMENTAL RESULT exists in this round** — `research_summary.md`:
"We have **not** trained models or measured Dice/mIoU/τ in this round."

---

## 1. The 8 — "Updated working Top-8" from `meta_audit.md`

Verbatim membership and order, with the file's own header caveat "(not final 3)".

| # | Candidate | Provenance | Advanced past Stage 5? |
|---|---|---|---|
| 1 | Constrained SAM-FT dual objective (method) | VFM-0263/0274, panel P12 | **Yes → Idea_01 RetainSAM** |
| 2 | Frozen/tuned crossover law | A0121, Stage-3 MUTATE; never in the R2 panel | **No** — cut, reason recorded |
| 3 | 0046-M transmittance vs binary for transparent classes | Stage-3 KILL, revived by this audit | **No** — cut, reason recorded |
| 4 | 0085-M lesion suppression law | panel P8 | **Yes → Idea_02 LesionSuppress** |
| 5 | 0074-M inter-observer calibration transfer vs accuracy transfer | Stage-3 KILL, revived by this audit as a narrowed mutation | **Yes → Idea_03 DisagreeShift** |
| 6 | 0252 label ecology + intervention | panel P1, dropped by R2's cheap-killer rule, restored by this audit | **No** — Stage-6 cut |
| 7 | Worst-case/oracle-click interactive eval merge | A0022 + A0168, both Stage-3 KILLs, merged by this audit | **No** — Stage-6 cut |
| 8 | 0275 + eval contamination merge (one eval slot) | panel P3 + salvage of the killed P10 | **No** — cut |

Plus a standing instruction in the same file: "**Protect 0276 shape-prior law and 0240 context
sampling as benches.**" Note that this *protects* 0276 without giving it a Top-8 slot — the omission
that §3 shows had to be corrected.

### Why the Top-8 looks unlike the R2 Top-7

`meta_audit.md` is an audit of the *portfolio*, not a re-review of proposals, and it deliberately
reversed several earlier verdicts. Its recorded rulings:

- **ACCEPTS**: "eval over-indexing; 0285 cut from SURVIVE; merge 0275 with contamination; merge
  worst-case clicks with oracle-click leak; revive 0046 as transmittance-vs-binary hypothesis (not
  'framing paper'); revive 0074 only as cross-stain calibration of disagreement fields (Stage3 killed
  original histo-prob maps); 0113 only as spatial error-structure prediction."
- **REJECTS**: "treating 0074 original as wrongly killed — original form **IS** published
  (RAPSODI/calibration). **Only mutation survives.**"
- **PARTIAL**: "constrained SAM-FT dual objective is method-shaped but **may lack novelty**; needs
  Stage3 of VFM keepers."

Three of the eight are therefore *resurrections* of Stage-3 kills (0046-M, 0074-M, and the A0022+A0168
merge), and one of the eight is the eventual #1 recommendation carrying an explicit novelty doubt.
The list-vs-list conflict with Reviewer #2 is itemised in `stage4_candidates.md` §5b.

---

## 2. The engineer's Top-5 — `stage5_killers.md`

Verbatim: "Engineer Top-5: (1) Constrained SAM-FT (2) Frozen/tuned n\* (3) 0085-M lesion suppression
(4) 0074-M calibration-under-shift (5) Interactive eval merge."

Cut by the engineer, with reasons as written: "0046-M (**GT scarcity**), 0252 (**soft kill in sim**),
0275 contamination (**engineering/confound**)."

So the engineer reduced the Top-8 to five by cutting #3, #6 and #8 — and, because he was working from
the Top-8, never saw SEG-0276-M at all.

---

## 3. The supervisor correction — 0276-M was missing

Verbatim from `stage5_killers.md`: "**SUPERVISOR CORRECTION: 0276-M shape-prior field was omitted from
this Stage-5 prompt** (R2 ranked it #1, inference-only killer). **Must add back before locking
Top-5.**"

The same file then gives a five-entry "Likely final-3 pool" that is **not** the engineer's Top-5:

1. Constrained SAM-FT
2. 0085-M lesion suppression
3. 0276-M prior-shape interpolation (pending design)
4. 0252 if cheap killer exists
5. Interactive eval only if not "just a benchmark paper" for the archival packages

**KNOWN FACT — these two five-entry lists conflict.** The engineer's Top-5 contains
`Frozen/tuned n*` and `0074-M` and omits `0276-M` and `0252`; the "likely final-3 pool" omits
`Frozen/tuned n*` and `0074-M` and contains `0276-M` and `0252`. Since `0074-M` became **Idea_03**, the
"likely final-3 pool" cannot be the operative Stage-5 five either. Neither list is the five.
This is the core reason the Stage-5 set is unrecoverable, and it is logged at
`FUNNEL_DEVIATION.md` §4-E.

### 3a. SEG-0276-M killer design (the design the correction called for)

From `stage5_0276.md`, the only per-candidate Stage-5 design that was written down:

- **Definition of α:** "projection of (pred − instance GT SDF) onto (GT → class-prior) in canonical
  frame."
- **Control:** SSA control against wrong-class / global / morphology.
- **Causal test:** "Causal shut-up: wrong-class prompt redirects attraction."
- **Pre-registered gates (HYPOTHESIS, none measured):** monotonicity; Δα ≥ 0.10; SSA > 0;
  median ρ ≤ 0.5.
- **Cost (HYPOTHESIS):** "~3 A100-days **inference-only**."
- **Designer's recommendation:** "INCLUDE, displace Constrained SAM-FT, keep 0085-M."
- **Supervisor's ruling:** "wait Stage 6 lock; 0276 is strong HRHR; SAM-FT only if it beats WiSE-FT."

That designer-vs-supervisor split is unresolved at Stage 5 by design, and is carried into
`stage6_battle.md` §3.

### 3b. Cheap-killer designs — `cheap_killers_0252_0046.md`

**SEG-0252.** Amplification `g ≈ ρ_H · ρ_M`. `ρ_M` measured with 0 humans in a synthetic loop;
`ρ_H` from a one-generation injected-convention human study (N = 12 × 60). Recorded limit:
"Human-free kills K1–K3. **Cannot cheaply CONFIRM multi-gen human pipelines.**" Supervisor ruling in
the same file: "0252 remains in final-3 contention over 0285."

The asymmetry matters and is the ground of the Stage-6 cut: the cheap instrument could *falsify* but
never *confirm*, so 0252 could enter Stage 6 but could not win a slot on external validity.

**SEG-0046-M.** A 3-day SegFormer-B0 A/B/C comparison (binary / alpha / entropy-matched soft) on
Transparent-460, Composition-1k, AIM-500, Foggy Cityscapes, transferring to Trans10K/GDD/SMOKE5K.
Gate: "promote only if scaling law holds AND not explained by soft labels."
Recorded prior-art risk: "SMOKE5K already transmission-guided (Yan et al. AAAI 2022) — **high
prior-art risk**." Treat that citation as EVIDENCE-FROM-AGENT.

---

## 4. Reconciled Stage-5 candidate set entering Stage 6

Seven distinct candidates are documented as live at some point during Stage 5. **Five of them
entered Stage 6 and the record does not say which five.** Rows are ordered by how firmly the record
places them in Stage 6.

| Candidate | One-sentence hypothesis | Stage-5 verdict as recorded | Rationale source | Entered Stage 6? |
|---|---|---|---|---|
| **Constrained SAM-FT** (VFM-0263/0274) | Promptability-constrained SAM fine-tuning strictly dominates the WiSE-FT interpolation Pareto front. | Engineer Top-5 **#1**; also "likely final-3 pool" #1; `meta_audit.md` PARTIAL flag "may lack novelty" | `stage5_killers.md`, `meta_audit.md`, panel P12 | **Yes — certain.** Became Idea_01, and `README.md` names it "#1 recommendation" |
| **SEG-0085-M** lesion suppression | P(suppress) is a function of size, contrast and enhancement strength; rank order must transfer to real LIDC nodules. | Engineer Top-5 **#3**; "likely final-3 pool" #2; R2 required softening "universal" | `stage5_killers.md`, panel P8 | **Yes — certain.** Became Idea_02 |
| **SEG-0074-M** calibration under shift | Disagreement-trained uncertainty fields retain ordering-sensitive meaning under scanner/stain shift where hard labels + TS cannot. | Engineer Top-5 **#4**; revived by `meta_audit.md` #5 as a *narrowed* mutation only | `stage5_killers.md`, `meta_audit.md`, `reviewer_summary.md` | **Yes — certain.** Became Idea_03 |
| **SEG-0276-M** prior-shape interpolation | A per-category prior-shape field has a transferable evidence/prior coefficient α, testable inference-only. | Not in the engineer's Top-5; **reinstated by supervisor correction**; "likely final-3 pool" #3; full design written | `stage5_killers.md`, `stage5_0276.md` | **Yes — certain.** `README.md` names it "Runner-up", so it was live at the Stage-6 lock |
| **SEG-0252** label ecology | Model-in-the-loop labelling amplifies conventions with `g ≈ ρ_H·ρ_M`. | Engineer **cut** it ("soft kill in sim"); `cheap_killers_0252_0046.md` overrode: "remains in final-3 contention over 0285"; "likely final-3 pool" #4 | `stage5_killers.md`, `cheap_killers_0252_0046.md` | **Yes — near-certain.** `eliminated_ideas_summary.md` records it as a **Stage 6** cut: "Cheap killer exists; **Stage 6 cut on external-validity circularity**" |
| **SEG-0250** rare states vs rare classes | At matched frequency, rare object states cost more accuracy than rare classes. | **Not named in any Stage-5 list** — absent from the Top-8, the engineer's Top-5, and the "likely final-3 pool" | `eliminated_ideas_summary.md`, panel P2 | **AMBIGUOUS — 需人工确认.** `eliminated_ideas_summary.md` says "SEG-0250 \| Strong but **Stage 6 cut (eval slot)**", which implies it reached Stage 6, yet no Stage-5 file carries it. Either it was promoted without a record, or "Stage 6 cut" is being used loosely. |
| **Frozen/tuned n\*** (A0121) | A frozen-vs-tuned data-scale crossover point n\* exists and is predictable a priori. | Engineer Top-5 **#2**; `meta_audit.md` Top-8 #2 | `stage5_killers.md`, `meta_audit.md` | **AMBIGUOUS — 需人工确认.** It held a Stage-5 slot, so it plausibly entered Stage 6, but `eliminated_ideas_summary.md` gives a reason without a stage: "Frozen/tuned n\* \| Selector circularity; worst cost-to-kill". |
| **Interactive eval merge** (A0022 + A0168) | Worst-case valid clicks and oracle-click leakage combine into one interactive-evaluation program. | Engineer Top-5 **#5**; "likely final-3 pool" #5, conditional on not being "just a benchmark paper" | `stage5_killers.md`, `meta_audit.md` | **AMBIGUOUS — 需人工确认.** Held a Stage-5 slot. Final reason recorded without a stage: `eliminated_ideas_summary.md` "Interactive eval merge \| Occupied by TETRIS + RClicks". `stage3_vfm_kills.md` had already predicted "Stage-5 'interactive eval merge' is DEAD as stated." |
| **SEG-0046-M** transmittance | Transmittance regression beats binary masks for transparent/translucent classes, as a scaling law not explained by soft labels. | **Cut by the engineer** — "0046-M (GT scarcity)" | `stage5_killers.md`, `cheap_killers_0252_0046.md` | **No.** But `reviewer_summary.md` records a Stage-6 dissent about it: "Engineer wanted 0046-M as cheap insurance" — so it was still argued for at Stage 6 without holding a slot |
| **SEG-0275 + contamination merge** | Post-cutoff names plus contamination audit occupy one evaluation slot. | **Cut by the engineer** — "0275 contamination (engineering/confound)" | `stage5_killers.md`, `meta_audit.md` #8 | **No** |
| **SEG-0285** typographic masks | In-image text redirects masks through the text-reading pathway. | Cut from SURVIVE by `meta_audit.md`; survived only on the condition of showing dissociation from CLIP typographic attacks | `meta_audit.md`, `stage4_reviewer2.md` | **No** — lost the 0252-vs-0285 contest at Stage 4/5; see `stage4_candidates.md` §5a |

### The honest count

- **4 certain** Stage-6 entrants: Constrained SAM-FT, 0085-M, 0074-M, 0276-M.
- **1 near-certain**: 0252, on the strength of an explicit "Stage 6 cut" attribution.
- **3 candidates for the remaining slots** if the five is to be read strictly: 0250,
  Frozen/tuned n\*, Interactive eval merge — and only two of those three can fit if 0252 is counted,
  which already fills the fifth.

Since 4 certain + 1 near-certain = 5, the most defensible reading is that the Stage-5 five was
**Constrained SAM-FT, 0085-M, 0074-M, 0276-M, 0252**, and that 0250, Frozen/tuned n\* and the
interactive eval merge died at or just before the Stage-5 lock. **This reading is offered as a
reading, not as the record**, because `eliminated_ideas_summary.md` attributes 0250's death to
"Stage 6" in the same breath, which the reading cannot accommodate. Flagged
`AMBIGUOUS — 需人工确认` and referred for human adjudication.

---

## 5. What Stage 5 actually produced

Independently of the membership question, Stage 5's deliverable is unambiguous and is the part that
carried into the packages: **each survivor got a named killer experiment with a pre-registered
falsifier.** `research_summary.md` describes the stage as "Killer experiments specified", and the
three surviving falsifiers are stated in that file as locked hypotheses:

1. **RetainSAM** — falsified if WiSE-FT interpolation matches or beats constrained FT.
2. **LesionSuppress** — falsified if Kendall τ is low or sign-flips on LIDC-matched bins.
3. **DisagreeShift** — falsified if temperature scaling matches on ordering-sensitive metrics.

Plus, for the runner-up, the four gates in `stage5_0276.md` (monotonicity, Δα ≥ 0.10, SSA > 0,
median ρ ≤ 0.5).

All four are HYPOTHESIS with pre-registered thresholds. None has been run. Costs quoted anywhere in
this file (~3 A100-days for 0276-M; ~4–6 GPU-days for the RetainSAM killer per
`Windows1/Idea_01/README.md`; ~2 for Idea_02, ~4 for Idea_03) are **HYPOTHESIS estimates, not
measurements**.
