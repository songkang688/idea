# Stage 3 → survivors (Windows1) — reconstructed

Status: **retrospective reconstruction.** Windows1 kept two Stage-3 *kill* sheets but never wrote a
Stage-3 survivor list. This file derives the survivor set by inversion from those two sheets.

Sources, and nothing else:
- `research_ledger/stage3_priorwork_kill.md` — SEG slice (5 KILL / 4 SURVIVE / 11 MUTATE)
- `research_ledger/stage3_vfm_kills.md` — VFM slice (4 KILL / 8 MUTATE / 1 WEAK SURVIVE)
- one-line hypotheses from `research_ledger/stage1_seg_keepers.md`,
  `research_ledger/stage1_vfma_asma_keepers.md`, `research_ledger/stage1_vfm_local_pool.md`
- "advanced?" column verified against the recovered Stage-4 panel (see `stage4_candidates.md`)

Epistemic labels per `Windows1/README.md`. Every row is a *decision record*, never a measurement.
`stage3_priorwork_kill.md` carries its own caveat, which applies to every citation-based kill below:
"citations claimed web-verified; still treat 2025–2026 items as **EVIDENCE-FROM-AGENT** until
re-checked in final packages."

Rows with no supporting text in any ledger file are stamped **`NO RECORDED REASON — 需人工确认`**.
No verdict rationale in this file is invented.

---

## 1. Scoreboard

| Slice | KILL | MUTATE | SURVIVE | WEAK SURVIVE | Decision units | Survivors |
|---|---|---|---|---|---|---|
| SEG (`stage3_priorwork_kill.md`) | 5 | 11 | 4 | 0 | **20** | **15** |
| VFM/ASM (`stage3_vfm_kills.md`) | 4 | 8 | 0 | 1 | **13** | **9** |
| Total | 9 | 19 | 4 | 1 | **33** | **24** |

**KNOWN FACT.** The SEG slice contains exactly 20 decision units, which reproduces the
"Stage 3 | ~20 attacked" row of `Windows1/research_summary.md` exactly. The 13 VFM/ASM units appear
**not** to be counted in that "~20". Recorded in `FUNNEL_DEVIATION.md` §2.

**KNOWN FACT.** 24 survivors entered the Stage-4 boundary but the Stage-4 panel attacked only 12.
The 12 dropped units are itemised in §4; most have no recorded reason.

---

## 2. SEG slice — survivors

Verdict values are exactly as written in `stage3_priorwork_kill.md`. "Territory rank" is that file's
own ranked list "## Current top scientific territory" (1–10); a dash means the ID is absent from it.

| ID | One-sentence hypothesis | Stage-3 verdict | Territory rank | Rationale source | Advanced to Stage 4? |
|---|---|---|---|---|---|
| **SEG-0252** | Model-in-the-loop labelling amplifies annotation conventions across generations (label ecology). | SURVIVE | 1 | `stage3_priorwork_kill.md`; hypothesis from `stage1_seg_keepers.md` Top-30 | **Yes** — panel P1 |
| **SEG-0250** | At matched frequency, rare *object states* cost more accuracy than rare *classes*. | SURVIVE | 2 | `stage3_priorwork_kill.md` territory #2 "matched-frequency state-tail vs class-tail" | **Yes** — panel P2 |
| **SEG-0275** | Post-cutoff concept names test open-vocabulary grounding without contamination (temporal holdout). | SURVIVE | 3 | `stage3_priorwork_kill.md`; `stage1_seg_keepers.md` Top-30 | **Yes** — panel P3 |
| **SEG-0285** | In-image printed text physically redirects masks, not just captions. | SURVIVE **(weak)** | 9 | `stage3_priorwork_kill.md` marks it `0285(weak)` and territory #9 "physical typographic injection moving masks" | **Yes** — panel P9 |
| **SEG-0276** | A per-category prior-shape field interpolates against local evidence with a transferable coefficient α, interacting with SAM prompt sensitivity. | MUTATE | 4 | `stage3_priorwork_kill.md` territory #4 | **Yes** — panel P4 |
| **SEG-0355** | "Undefined" and "uncertain" are conflated: no monotone score on existing heads separates them. | MUTATE | 5 | `stage3_priorwork_kill.md` territory #5 | **Yes** — panel P5 |
| **SEG-0002** | Human boundary jitter sets a noise floor; subtracting it re-ranks reported SOTA. | MUTATE | 6 | `stage3_priorwork_kill.md` territory #6; `stage1_seg_keepers.md` Top-30 | **Yes** — panel P6 |
| **SEG-0240** | The sampling-vs-reweighting gap is a context-statistics mechanism, not an optimisation artifact. | MUTATE | 7 | `stage3_priorwork_kill.md` territory #7 | **Yes** — panel P7 |
| **SEG-0085** | Denoising/SR pipelines suppress small low-contrast lesions as a function of enhancement strength. | MUTATE | 8 | `stage3_priorwork_kill.md` territory #8; `stage1_seg_keepers.md` Top-30 | **Yes** — panel P8 → **Idea_02** |
| **SEG-0193** | Test-set replica injection yields a causal ΔmIoU inflation curve. | MUTATE | 10 | `stage3_priorwork_kill.md` territory #10 | **Yes** — panel P10 (then the round's only Stage-4 KILL) |
| **SEG-0103 / SEG-0125** *(one merged unit)* | 0103: a go/no-go statistic for unsupervised domain adaptation. 0125: a self-training error-amplification law readable from round 1. | MUTATE | — | Recorded as the single unit `0103/0125` in `stage3_priorwork_kill.md`; both one-liners from `stage1_seg_keepers.md` Top-30 | **Yes** — panel P11 ("UDA amplification exponent vs GDA theory; churn stopping rule") carries both halves |
| **SEG-0019** | Boundary hallucination is evidence-free: masking local evidence still yields confident contours. | MUTATE | — | Verdict is recorded; **no rationale for its later disappearance** | **No** — `NO RECORDED REASON — 需人工确认` |
| **SEG-0054** | Pre-visibility smoke is detectable from temporal flicker spectra. | MUTATE | — | Verdict is recorded; **no rationale for its later disappearance** | **No** — `NO RECORDED REASON — 需人工确认` |
| **SEG-0031** | `NO RECORDED HYPOTHESIS` — 0031 is absent from the `stage1_seg_keepers.md` Top-30 and appears only as `0031(P)` in the Stage-2 promotions list. | MUTATE | — | Verdict is recorded; hypothesis text and later disposition both absent | **No** — `NO RECORDED REASON — 需人工确认` |
| **SEG-0122** | `NO RECORDED HYPOTHESIS` — 0122 appears only in the Stage-2 under-ranked promotions list. | MUTATE | — | Verdict is recorded; hypothesis text and later disposition both absent | **No** — `NO RECORDED REASON — 需人工确认` |

### SEG slice — killed at Stage 3 (for completeness)

All five have a recorded prior-work reason, and all five are independently confirmed in
`Windows1/selection_history/eliminated_ideas_summary.md`. Treat the citations as EVIDENCE-FROM-AGENT
per the source file's own caveat.

| ID | One-sentence hypothesis | Recorded kill reason | Confirmed in eliminated_ideas_summary? |
|---|---|---|---|
| SEG-0074 | Infiltration probability fields instead of hard contours. | Prior work: MRI–histo probability maps + patient-level calibration already exist | Yes — "SEG-0074 original" |
| SEG-0206 | Watermark/logo learnability as a dataset pathology. | ImageNet-W; watermark learning is often the *design goal* | Yes |
| SEG-0185 | Frozen dense probes predict fine-tune rank at ~1% compute. | LogME / OTCE-seg | Yes |
| SEG-0046 | Smoke as optical-density regression, not a binary mask. | SMOKE+ / dehazing / AAAI 2022 transmission-guided smoke | Yes — "SEG-0046 framing" |
| SEG-0113 | Predict deployment mIoU from an unlabeled stream. | Bar CVPRW 2022 / AutoEval / SPE | Yes |

**Note on partial resurrection (EVIDENCE).** Two of these five were later revived in *mutated* form by
`research_ledger/meta_audit.md`: "revive 0046 as transmittance-vs-binary hypothesis (not 'framing
paper')" and "revive 0074 only as cross-stain calibration of disagreement fields". `meta_audit.md`
also records the supervisor **rejecting** the broader claim: "REJECTS: treating 0074 original as
wrongly killed — original form IS published (RAPSODI/calibration). Only mutation survives."
SEG-0074-M went on to become **Idea_03 DisagreeShift**. So a Stage-3 kill produced a finalist through
an explicitly narrowed mutation, and the ledger is unusually clear about the limits of that revival.

---

## 3. VFM / ASM slice — survivors

Verdicts exactly as written in `stage3_vfm_kills.md`. One-liners from
`stage1_vfma_asma_keepers.md` (A-namespace) and `stage1_vfm_local_pool.md` (VFM-namespace).

| ID | One-sentence hypothesis | Stage-3 verdict | Recorded mutation direction | Advanced to Stage 4? |
|---|---|---|---|---|
| **VFM-0263 / VFM-0274** | 0263: maximise target Dice subject to an SA-1B promptability drop < ε. 0274: retain SA-1B AMG quality and COCO fine-tuning as a dual objective. | MUTATE *(written as `A0263` — namespace error, see below)* | "HQ-SAM Table 9 already measured drop; WiSE-FT is the α dial; need retention BENCHMARK + method that beats WiSE-FT" | **Yes** — panel P12 → **Idea_01** |
| A0051 | Encoder/decoder probe gap in promptable segmenters. | MUTATE | "prompt-conditioned credit assignment" | **No** — `NO RECORDED REASON — 需人工确认` |
| A0028 | Cross-prompt disagreement predicts error. | MUTATE | "cross-modality (not within-type) disagreement" | **No** — `NO RECORDED REASON — 需人工确认` |
| A0166 | SA-1B / eval near-duplicate leakage. | MUTATE | "SA-1B stats as audit not hypothesis" | **No** — `NO RECORDED REASON — 需人工确认` |
| A0121 | A frozen-vs-tuned data-scale crossover point n\*. | MUTATE | "crossover + a priori selector" | **No panel slot, but it did continue.** See §5 — it reappears as "Frozen/tuned crossover law" in `meta_audit.md` Top-8 #2 and "Frozen/tuned n\*" in the Stage-5 engineer Top-5 #2. Recorded reason for its eventual death: `eliminated_ideas_summary.md` "Frozen/tuned n\* \| Selector circularity; worst cost-to-kill". |
| A0153 | A linear map aligns CLIP patch features to DINOv2 spatial correspondence. | MUTATE — flagged "**BEST VFM crack**" | "linear CLIP-patch→DINOv2 correspondence" | **No.** Recorded reason exists: killed by prior work — `eliminated_ideas_summary.md` "VFM-A0153 \| CLIP-DINOiser / ProxyCLIP / Platonic Representation Hypothesis", and `evolution_summary.md` lists "linear CLIP→DINOv2 as lead (Platonic / CLIP-DINOiser)" among kills. Note the reversal: Stage 3's highest-rated VFM item died without ever reaching Reviewer #2. |
| A0073 | Prompt-tuning vs LoRA under distribution shift. | MUTATE | "vision instantiation" | **No** — `NO RECORDED REASON — 需人工确认` |
| A0021 | Overtrained-small vs Chinchilla-optimal for dense prediction. | MUTATE | "ride public grids only" | **No** — `NO RECORDED REASON — 需人工确认` |
| A0109 | Seed and split variance exceeds published method deltas. | **WEAK SURVIVE** | (none recorded) | **No** — `NO RECORDED REASON — 需人工确认`. Note the topic overlaps SEG-0002-M (panel P6), whose panel text lists "training-seed variance" as a required baseline; whether A0109 was absorbed there is **not recorded**. |

### VFM slice — killed at Stage 3

| ID | One-sentence hypothesis | Recorded kill reason | Confirmed in eliminated_ideas_summary? |
|---|---|---|---|
| A0022 | Worst-case *valid* click sequences for interactive segmentation. | TETRIS | Yes — "VFM-A0022 \| TETRIS AAAI 2024" |
| A0168 | Oracle-click simulation leaks relative to human clicks. | RClicks | Yes — "VFM-A0168 \| RClicks 2024" |
| A0077 | Effective LoRA rank via SVD truncation. | PARA | Yes — "VFM-A0077 \| PARA / AdaLoRA" |
| A0148 | Outlier / high-norm token renormalisation in ViTs. | Registers | Yes — "VFM-A0148 \| DINOv2 registers" |

**Recorded resurrection as a merge (EVIDENCE).** A0022 and A0168 were killed individually here, then
recombined: `meta_audit.md` instructs "merge worst-case clicks with oracle-click leak" and lists the
result as Top-8 #7 "Worst-case/oracle-click interactive eval merge". It reached the Stage-5 engineer
Top-5 (#5, "Interactive eval merge") before dying at Stage 6 —
`eliminated_ideas_summary.md`: "Interactive eval merge \| Occupied by TETRIS + RClicks", i.e. it was
finally killed by the same two papers that killed its two parents.

`stage3_vfm_kills.md` anticipated exactly this: "**IMPLICATION:** Stage-5 'interactive eval merge' is
DEAD as stated."

---

## 4. The 24 → 12 narrowing at the Stage-4 boundary

**KNOWN FACT.** 24 units survived Stage 3; the recovered Stage-4 panel attacked 12. No ledger file
documents the selection of those 12.

| Disposition | Count | Units |
|---|---|---|
| Advanced to the Stage-4 R2 panel | 11 SEG units (12 SEG IDs, since `0103/0125` is one merged unit) + 1 VFM unit = **12 panel proposals** | P1–P12 |
| Dropped with a recorded reason found elsewhere | 2 | A0153 (prior work), A0121 (continued outside the panel, later killed on selector circularity) |
| Dropped with **no** recorded reason | 10 | SEG-0019, SEG-0054, SEG-0031, SEG-0122, A0051, A0028, A0166, A0073, A0021, A0109 |

**MODEL SPECULATION, flagged as such and not to be cited as a reason:** the 12 panel proposals are
exactly the 10 entries of the `stage3_priorwork_kill.md` "top scientific territory" list, plus the
`0103/0125` unit, plus the constrained SAM-FT unit. That is consistent with the territory ranking
having been used as the Stage-4 shortlist. The ledger never says so, so it is not asserted.

---

## 5. Two structural findings about the survivor set

**A. Idea_01's ancestor never passed a Stage-2 review (KNOWN FACT).**
`VFM-0263` and `VFM-0274` come from `stage1_vfm_local_pool.md`, the 350-idea supervisor-backup pool.
The only Stage-2 review sheet in the ledger is `stage2_seg_review.md`, which covers the **SEG** slice
and closes with "Global 1000 not yet complete: waiting VFM + ASM pools." No VFM/ASM Stage-2 sheet was
ever written. So the eventual **#1 recommendation** entered the funnel at Stage 3, straight from
Stage-1 generation, with no independent Stage-2 scoring. Recorded in `FUNNEL_DEVIATION.md` §3b/§4-B.
This is a gap in the *process record*; it is not a claim that Idea_01 is unsound, and `stage4_reviewer2.md`
plus the recovered panel show it was attacked hard at Stage 4.

**B. Two namespace hazards a future auditor will trip over (KNOWN FACT).**

1. `stage3_vfm_kills.md` writes **`A0263`**. The A-namespace (VFM-A / ASM-A) holds 180 ideas per
   `stage1_vfma_asma_keepers.md`, so `A0263` cannot exist there. The referent is `VFM-0263` in the
   local 350-idea pool, which `stage4_reviewer2.md` cites correctly as `VFM-0263/0274`.
   Flagged, not corrected — the ledger is not modified by this backfill.
2. **`0274` is two different ideas.** `SEG-0274` was KILLed at Stage 2
   (`stage2_seg_review.md`: `KILL: 0048, 0061, 0170, 0274`, and it also appears in that file's
   "Over-ranked (eval-only / known genre)" list). `VFM-0274` is "Retain SA-1B AMG quality + COCO FT
   as the dual objective" and is a direct ancestor of **Idea_01**. A bare "0274" in this archive is
   ambiguous; always carry the `SEG-` or `VFM-` prefix.
