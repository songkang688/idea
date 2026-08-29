# Stage 4 → candidates (Windows1) — R2 panel RECOVERED

Status: **retrospective reconstruction. The full Reviewer #2 panel was recovered.**

`research_ledger/stage4_reviewer2.md` is a ~1.1 KB summary and states that the full panel is
"on branch cursor/reviewer2-stage4-kill-panel-5733 (cloud worktree, **not this repo**)".
**That parenthetical is wrong.** The branch is in this repository, and the panel — 21,207 bytes,
all 12 proposals with full attack structure — was recovered from it.

---

## 1. Recovery record

**PANEL RECOVERED.** Provenance:

| Field | Value |
|---|---|
| Branch | `origin/cursor/reviewer2-stage4-kill-panel-5733` |
| Path on that branch | `research_ledger/stage4_reviewer2_kill_panel.md` |
| Blob | `edeaccb6a431c460e93a0e207b378839a82cf7ab` (21,207 bytes) |
| Commit | `c77a907e5d210d768d909b897e5dbdbd46da36a5`, "Add Stage 4 Reviewer #2 kill panel for 12 segmentation/VFM proposals", Fri Aug 28 2026 |
| Title line | `# Stage 4 — Reviewer #2 Kill Panel (Windows1 PI)` |

Attribution to Windows1 is solid on three independent counts: the title says "Windows1 PI"; the
branch suffix `5733` matches the `Source: bc-90c313c0-0076-59a0-a25e-0727cdb45733` line in
`research_ledger/stage4_reviewer2.md`; and the panel's Top-7 list reproduces the summary's R2 Top-7
in the same order with the same seven IDs.

**The branch holds only two files** — `README.md` and the panel — so it is a panel-only branch, never
merged. That is why the panel is missing from `main`. This backfill does **not** merge that branch or
copy the panel into `research_ledger/`; it indexes and summarises it here, leaving
`research_ledger/` untouched.

### Branches searched, and what each actually contains

Four branches were named as possibly holding Stage-4 panel material. **Only one does.**

| Branch | Verdict | What is actually on it |
|---|---|---|
| `cursor/reviewer2-stage4-kill-panel-5733` | **Windows1 panel — RECOVERED** | `research_ledger/stage4_reviewer2_kill_panel.md`, titled "(Windows1 PI)", P1–P12 matching Windows1's SEG-/VFM- IDs |
| `cursor/stage4-cluster-a-reviewer2-f1fa` | **NOT Windows1** | `stage3_cluster_A_*` and `stage4_cluster_A_*` (attacks, decisions.csv, keep, killed) |
| `cursor/stage4-cluster-b-reviewer2-b25a` | **NOT Windows1** | `stage4_cluster_B_*` |
| `cursor/stage4-cluster-c-reviewer2-c1be` | **NOT Windows1** | `stage4_cluster_C_*` |

**The three cluster branches are a different window's Stage 4 and must not be folded into Windows1.**
Evidence, checked file by file:

- `stage4_cluster_A_keep.md` and `stage4_cluster_A_killed.md` both carry the header
  "**Reviewer #2 (Cloud Sub-Agent J) → Supervisor Windows7.**" Cluster B names "Cloud Sub-Agent K".
- Their ID namespaces are `A-0003`, `A-0016`, `B-0058`, `B-0062`, `C-0028`, `C-0090` … — a
  hyphenated cluster-letter scheme with **no overlap** with Windows1's `SEG-0001…0365`,
  `VFM-0001…0350`, `ASM-0001…0350` or `A0001…A0180` namespaces.
- Their subject matter is disjoint from Windows1's funnel (SAM2 memory FIFO eviction, MoE routing as
  pathology detector, Doppler audio supervision, dose maps as contour supervision, dimensional
  collapse, text-batch rehearsal).
- Their counts do not fit Windows1's Stage 4 either: cluster A is 7 survivors of 17, B is 7 of 20,
  C is 7 of 18. Windows1's Stage 4 was 12 proposals with one kill.

These three branches nonetheless carry `Windows1/` and `research_ledger/` in their trees with
**byte-identical blob hashes** to `main` — they simply branched from a commit that already had
Windows1 merged. That inheritance is what makes them look relevant, and it is also the reason
`research_ledger/` must not be relocated (see `LEDGER_INDEX.md` §4).

---

## 2. Panel structure

Every proposal in the recovered panel was assessed on a fixed seven-part schema, which is why the
reconstruction below is uniform rather than impressionistic:

1. **Rejection** — the hostile reviewer's strongest single objection
2. **Hidden assumption**
3. **Confounder**
4. **Missing baseline**
5. **Trivial alternative** — the cheaper explanation that must be excluded
6. **Shut-me-up experiment** — the concrete study that would silence the objection
7. **Decision** + **Remaining fatal flaw**

The panel opens with a role statement: "hostile CVPR/ICCV/MICCAI reviewer. Each proposal rejected,
then assessed for whether a real experiment rescues it."

**Epistemic caveat carried forward.** These are REVIEWER JUDGMENT, consistent with
`research_ledger/stage2_seg_review.md` ("Scores are REVIEWER JUDGMENT not facts"). No attack below is
a demonstrated fact about any method, and no "shut-me-up experiment" has been run — all are
HYPOTHESIS / EXPECTED at most. **No ACTUAL EXPERIMENTAL RESULT exists.**

### Citations claimed by the panel

The panel lists ten citations it claims were "checked against live sources": Kumar/Ma/Liang 2020
(arXiv 2002.11361); Wang et al. 2022 (2204.08200); Li et al. HalluSegBench 2025 (2506.21546);
Byrd & Lipton 2019 (1812.03372); Goh et al. Multimodal Neurons 2021 (distill.pub); Wortsman et al.
WiSE-FT 2022 (2109.01903); Ramanathan et al. PACO 2023 (2301.01795); Pham et al. VAW 2021
(2106.09707); Cheng et al. Boundary IoU 2021 (2103.16562); Liu et al. GRES 2023 (2306.00968).

Treat these as **EVIDENCE-FROM-AGENT**, not as verified by this backfill — `stage3_priorwork_kill.md`
sets that standard for the round and it is not relaxed here.

**The panel flags one of its own citations as unresolved**, verbatim: "The 'ACL Findings 2025
one-generation NLP analog' cited by P1: **UNSURE which paper — must be pinned or dropped.**"
Carried forward as an open item; not resolved here and not to be cited until pinned.

---

## 3. The 12 candidates

`stage4_reviewer2.md` summarises the outcome as "KILL: P10 0193 replica-spiking (no transportable
law). KEEP-IF-EXPERIMENT: all others. **No unconditional KEEP.**" The recovered panel confirms
this exactly: 11 KEEP-IF-EXPERIMENT, 1 KILL, 0 unconditional KEEP.

| # | ID | One-sentence hypothesis | Reviewer #2 verdict | Rationale source | Advanced to Stage 5? |
|---|---|---|---|---|---|
| **P1** | SEG-0252 | Multi-generation model-in-the-loop labelling drifts mask conventions. | KEEP-IF-EXPERIMENT | Panel P1 | **Contested.** Dropped by the cheap-killer rule at Stage 4, then kept in contention — see §5 |
| **P2** | SEG-0250 | Rare object *states* cost more than rare *classes* at matched frequency. | KEEP-IF-EXPERIMENT | Panel P2; R2 Top-7 rank 3 | Yes, then Stage-6 cut |
| **P3** | SEG-0275 | Post-cutoff concept names measure genuine open-vocab grounding. | KEEP-IF-EXPERIMENT | Panel P3 | Reduced to "cheap nonce-word pilot only" |
| **P4** | SEG-0276-M | A per-category prior-shape field has a transferable evidence/prior interpolation coefficient α. | KEEP-IF-EXPERIMENT — "HRHR; killer experiment is inference-only (cheap)" | Panel P4; **R2 Top-7 rank 1** | Yes, but only after a supervisor correction — see §5 |
| **P5** | SEG-0355-M | "Undefined" and "uncertain" are conflated by all existing scores. | KEEP-IF-EXPERIMENT **(borderline KILL at current claim strength)** | Panel P5; R2 Top-7 rank 4 | Not in the Stage-5 engineer Top-5 |
| **P6** | SEG-0002-M | Boundary-jitter noise floor re-ranks reported SOTA. | KEEP-IF-EXPERIMENT — "cheap and useful, but incremental" | Panel P6; R2 Top-7 rank 5 | Not in the Stage-5 engineer Top-5 |
| **P7** | SEG-0240-M | The sampling-vs-reweighting gap is context-statistics, not optimisation. | KEEP-IF-EXPERIMENT — "an ML-theory paper in a CVPR costume" | Panel P7 | **No** — "Dropped by cheap-killer rule: … 0240 factorial" |
| **P8** | SEG-0085-M | Lesion suppression is a function of size, contrast and enhancement strength. | KEEP-IF-EXPERIMENT — "clinically important; **soften 'universal' to 'conditional law'**" | Panel P8; R2 Top-7 rank 7 | **Yes → Idea_02** |
| **P9** | SEG-0285 | In-image text redirects masks via the text-reading pathway. | KEEP-IF-EXPERIMENT — "cheap, likely to work, limited ceiling" | Panel P9; **R2 Top-7 rank 2** | **Contested** — the auditor cut it; see §5 |
| **P10** | SEG-0193-M | Test-replica spiking yields a transportable ΔmIoU inflation curve. | **KILL** as standalone — "salvage as a section of a contamination-audit tool" | Panel P10 | **No** — the round's only Stage-4 kill |
| **P11** | SEG-0103-M | A UDA amplification exponent beats GDA theory; churn gives a stopping rule. | KEEP-IF-EXPERIMENT **(stopping rule only; drop the theory-comparison framing)** | Panel P11 | **No** — "Dropped by cheap-killer rule: … 0103-M workshop" |
| **P12** | VFM-0263 / 0274 | Constrained SAM fine-tuning: maximise target Dice subject to a promptability drop < ε. | KEEP-IF-EXPERIMENT — "engineering-safe, **novelty-fragile**" | Panel P12; R2 Top-7 rank 6 | **Yes → Idea_01** |

### Per-candidate detail

Recorded because the "trivial alternative" and "missing baseline" rows are what actually shaped the
three surviving packages. Condensed from the panel; the panel is the authority.

**P1 SEG-0252** — Rejection: "model-collapse tourism ported to masks"; the proposed statistics measure
tool-UI artifacts because annotators accept SAM's default mask to save clicks. Trivial alternative:
laziness. Missing baseline: a human-only multi-generation arm plus a second-teacher arm.
Shut-me-up: two-generation crossover, teacher A vs B vs none at matched UI/time, a classifier
identifying the teacher from mask statistics, and a student reproducing A's signature.
Remaining fatal flaw: "Real annotator generations are expensive; simulated annotators would gut the
claim."

**P2 SEG-0250** — Rejection: matched frequency is "a mirage"; one covariate of a dozen is controlled
and called causal. Confounder: rare states change mask geometry, so error rises because delineation
is harder for anyone including humans. Missing baseline: boundary-complexity-matched control plus an
oracle-box arm to split recognition from delineation failure.

**P3 SEG-0275** — Rejection: "LiveBench-for-segmentation", and the bottleneck is supply, not the idea.
Trivial alternative: tokenizer fragmentation on any OOV string. Missing baseline: **nonce-word
control** — existing concepts renamed with made-up words. This is the baseline that survived as the
only sanctioned Stage-5 activity for P3.

**P4 SEG-0276-M** — Rejection: "transferable coefficient" presumes a one-dimensional tradeoff between
"prompt-semantic strength" and "local evidence", neither of which has an agreed operationalisation,
"making the law circular". Trivial alternative: "under weak evidence the model emits the category's
average training mask. Memorized mean shape, no field." Missing baseline: Bayesian mean-shape
template. Shut-me-up: fit α on model A / categories X, then predict mask geometry with CIs on
model B / held-out categories / held-out degradations, beating mean-shape.
Remaining fatal flaw: "Operationalizing 'prompt-semantic strength' may never survive review."

**P5 SEG-0355-M** — Rejection: the claim is a universal negative over a nonparametric class and
"cannot be proven empirically". Hidden assumption: a ground-truth undefined/uncertain partition
exists and annotators agree — "report κ or it didn't happen". Repair: an enumerated-scores claim plus
a trained probe that *does* separate them, showing signal exists and scores miss it.

**P6 SEG-0002-M** — Rejection: "statistically incoherent" — GT jitter is **common-mode** across models
scored on the same labels, so paired comparisons cancel it and a 0.5% delta can be significant even
with a 2% floor. Missing baseline: **paired bootstrap on existing leaderboards — free, no
re-annotation.** Remaining fatal flaw: "The paired-evaluation objection may kill the 'gains vanish'
headline outright."

**P7 SEG-0240-M** — Rejection: full-batch training is a different optimisation regime, so "the
'control' changes more than it fixes"; matching scalar gradient-noise variance leaves the covariance
structure unmatched. Confounder: BN/GN statistics under resampling. Missing baseline: a GN/LN-only
arm and a long-vs-short training arm, citing Byrd & Lipton 2019.

**P8 SEG-0085-M** — Rejection: "'Universal across pipelines/modalities' is precisely the claim MICCAI
reviewers distrust"; connected-component filtering deletes small lesions *after* the network, so much
of the suppression probability is "a pipeline config, not a model property". Trivial alternative:
resolution/PSF limit plus the known small-object bias of Dice loss. Missing baseline: a human reader
curve at matched size×contrast, and a postprocessing-ablated arm.
**This is the attack that forced Idea_02 to drop "universal law".**

**P9 SEG-0285** — Rejection: typographic attacks are five years old (Goh et al. 2021); extending them
from captions to masks "replicates the community's null hypothesis". Trivial alternative: any
high-contrast patch attracts mask decoders — nothing about reading. Missing baseline: scrambled /
unreadable text at matched size and contrast, plus a quantified caption-redirect-without-mask-redirect
dissociation. **This dissociation requirement is what the supervisor later made P9's survival
condition.**

**P10 SEG-0193-M (KILLED)** — Rejection: inflation curves are dataset- and capacity-specific, so the
deliverable is "a calibration table nobody else can use"; "replica" is undefined across exact-dup /
near-dup / augmented / same-scene, and the curve differs by orders of magnitude across them.
Trivial alternative: "inflation ≈ duplicate fraction × per-image gain is nearly dimensional
analysis." Remaining fatal flaw, verbatim: "**No transportable law is plausible.**"
This matches `eliminated_ideas_summary.md` "SEG-0193-M \| No transportable inflation law (Stage 4
KILL)" and `research_summary.md` "one KILL (replica-spiking inflation curve)".

**P11 SEG-0103-M** — Rejection: the GDA bound is a known-loose worst-case upper bound (Kumar et al.
2020 exponential-in-T; Wang et al. 2022 improved to additive), so "empirical exponent beats theory"
is "a foregone conclusion … a category error". Hidden assumption: a single power law exists, whereas
self-training failure is often phase-transition-like. Verdict keeps the stopping rule only.

**P12 VFM-0263/0274** — Rejection: "the entire novelty is a constraint formulation the community
implements informally with LoRA, frozen encoders, replay, and weight interpolation"; WiSE-FT "spans a
near-free Pareto front by interpolating checkpoints", so without strict dominance this is "a
reinvention with a Lagrangian". Confounder: ε on SA-1B natural images "can be trivially satisfied
while promptability collapses on other domains — constraint on the wrong distribution".
Shut-me-up: Pareto plot on 3 target domains including medical, constrained vs interpolation vs LoRA
vs replay, promptability measured on SA-1B **and** held-out third domains, showing strict dominance
anywhere on the front. Remaining fatal flaw: "**High probability the interpolation baseline matches,
leaving no paper.**"

**This is the direct origin of Idea_01's kill switch.** `Windows1/README.md` requires domination at
≥2 operating points; `Windows1/Idea_01/README.md` H1 states "≥2 points" and adds "Kill H1 if the
interpolation polyline is not strictly dominated."

---

## 4. R2 Top-7 for Stage 5

Reproduced from the panel's own ranking table, with the rationale it gave.

| Rank | Panel # | Idea | Recorded rationale |
|---|---|---|---|
| 1 | P4 | shape-prior field (SEG-0276-M) | "HRHR protected: killer experiment is inference-only and decisively falsifiable (cross-model, held-out-category prediction vs mean-shape baseline)." |
| 2 | P9 | typographic mask attack (SEG-0285) | "Cheapest to execute; dissociation + patching converts a known effect into a mechanism claim." |
| 3 | P2 | rare states vs rare classes (SEG-0250) | "Counterfactual state-edit pairs feasible with current editing models; strong conceptual payoff if the gap survives complexity matching." |
| 4 | P5 | undefined vs uncertain (SEG-0355-M) | "Repaired constructive framing (probe separates, scores don't) is a real finding; medium cost." |
| 5 | P6 | noise-floor re-rank (SEG-0002-M) | "Near-free triage: paired bootstrap on existing leaderboards first — either outcome informative." |
| 6 | P12 | constrained SAM-FT (VFM-0263/0274) | "Safe engineering with built-in kill switch: run the weight-interpolation baseline first; proceed only if headroom exists." |
| 7 | P8 | lesion suppression (SEG-0085-M) | "MICCAI-valuable after softening 'universal'; gate on a cheap 2-pipeline postprocessing-ablated pilot." |

This is identical in membership and order to the R2 Top-7 line in `stage4_reviewer2.md`, which is the
strongest single confirmation that the recovered panel is Windows1's.

### The panel's own drop list

Verbatim: "Dropped: P1 (HRHR but the killer experiment needs real multi-generation annotator cohorts
— expensive, **so the cheap-killer protection rule doesn't apply**), P3 (run only the cheap nonce-word
pilot; full auto-refreshing bench is a maintenance sink), P7 (factorial compute heavy; elimination
logic never closes), P11 (theory half dead; stopping rule workshop-tier), P10 (killed)."

Note what the P1 clause says about the round's protection policy: HRHR protection was **conditional on
the killer experiment being cheap**, and was withdrawn when it was not. That is the "cheap-killer
rule" named in `stage4_reviewer2.md`, stated here in its own words.

---

## 5. Recorded conflicts at the Stage-4/5 boundary

Reproduced because Windows1's own instruction was to keep dissent on record rather than manufacture
consensus. Both conflicts are load-bearing for Stage 6 and both reappear in `stage6_battle.md`.

### 5a. 0285 vs 0252 — the auditor and Reviewer #2 reached opposite verdicts

- **Reviewer #2** ranked 0285 at Top-7 #2 (cheapest to execute) and **dropped 0252** under the
  cheap-killer rule, because "real annotator generations are expensive".
- **The meta-audit** did the reverse: `meta_audit.md` records "Supervisor ACCEPTS: … **0285 cut from
  SURVIVE**", while `cheap_killers_0252_0046.md` concludes "**0252 remains in final-3 contention over
  0285.**"
- `stage4_reviewer2.md` states the conflict explicitly and records the ruling: "CONFLICT with
  meta-audit: auditor cut 0285 and promoted 0252. **Supervisor: keep 0252 via cheaper proxy**
  (synthetic multi-gen teacher→student loops + one small human study); **0285 only if dissociation
  from CLIP typographic attacks is shown**; 0276 and constrained SAM-FT and 0085-M remain central."
- The cheaper proxy that rescued 0252 is specified in `cheap_killers_0252_0046.md`: amplification
  `g ≈ ρ_H · ρ_M`, with `ρ_M` measured with zero humans in a synthetic loop and `ρ_H` from a
  one-generation injected-convention human study (N = 12 × 60). That file also records the limit of
  the proxy: "Human-free kills K1–K3. **Cannot cheaply CONFIRM multi-gen human pipelines.**"
  So 0252 was rescued for *falsification* only, never for confirmation — which is exactly the
  "external-validity circularity" it was finally cut on at Stage 6.

Neither side was overruled into silence: 0252 survived on a downgraded instrument, 0285 survived on a
condition, and both were ultimately cut at Stage 6.

### 5b. The two ranked lists disagree, and the engineer followed the wrong one

The R2 Top-7 above and the "Updated working Top-8" in `meta_audit.md` are different lists produced by
different reviewers, and neither file declares which supersedes the other:

| | R2 Top-7 (`stage4_reviewer2.md` + panel) | Top-8 (`meta_audit.md`) |
|---|---|---|
| SEG-0276-M | **rank 1** | **absent** from the Top-8; only "Protect 0276 shape-prior law … as benches" |
| Frozen/tuned crossover | absent | #2 |
| SEG-0046-M | absent | #3 |
| SEG-0074-M | absent | #5 |
| Interactive eval merge | absent | #7 |

`stage5_killers.md` records the consequence and the correction, verbatim: "**SUPERVISOR CORRECTION:
0276-M shape-prior field was omitted from this Stage-5 prompt** (R2 ranked it #1, inference-only
killer). **Must add back before locking Top-5.**"

So Reviewer #2's top-ranked candidate was accidentally dropped at the Stage-5 handoff and had to be
reinstated by hand. It went on to become the runner-up. Carried into `stage5_top5.md` §2 and
`FUNNEL_DEVIATION.md` §4-G.

---

## 6. What is still not recoverable

- **How 24 Stage-3 survivors became these 12 proposals.** The panel begins with 12 already selected.
  See `stage3_survivors.md` §4; ten dropped units have no recorded reason.
- **The panel's P1 citation.** "ACL Findings 2025 one-generation NLP analog" is marked UNSURE by the
  panel itself and remains unpinned.
- **Whether A0109 (seed/split variance) was absorbed into P6.** The topics overlap and P6's panel text
  requires a seed-variance baseline, but no file records a merge. `NO RECORDED REASON — 需人工确认`.
- **Any Stage-4 material for the VFM/ASM slice beyond P12.** Eight Stage-3 VFM survivors never reach
  the panel; see `stage3_survivors.md` §3.
