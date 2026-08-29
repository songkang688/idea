# Stage 6 — final battle, 5 → 3 (Windows1)

## THIS IS A RETROSPECTIVE RECONSTRUCTION

**No Stage-6 record was written when Stage 6 happened.** This file was authored *after* the Final 3
were locked, packaged, and merged into `main`. It is assembled from documents that survived, not from
a transcript of the session.

**KNOWN FACT — Stage 6 occurred.** Three independent attestations:

1. `Windows1/README.md`: "**Stage 6 locked** method + medical-safety characterization + medical
   uncertainty method."
2. `Windows1/research_summary.md` funnel table: "Stage 6 \| **Final 3** \| A RetainSAM,
   B LesionSuppress, D DisagreeShift."
3. `Windows1/selection_history/reviewer_summary.md` records three named Stage-6 dissents, which could
   not exist without a Stage-6 session.

**KNOWN FACT — no primary Stage-6 record exists.** `research_ledger/` contains no `stage6_*` file,
and neither did `Windows1/selection_history/` before this backfill. Every kill sheet from Stages 1–5
was kept; the 5 → 3 adjudication was not.

**What this file is and is not.** The *outcome* (which three won, and their locked falsifiers) is
KNOWN FACT, taken verbatim from `README.md` and `research_summary.md`. The *reasoning* is reconstructed
from `reviewer_summary.md`, `evolution_summary.md`, `eliminated_ideas_summary.md`,
`research_ledger/meta_audit.md`, `research_ledger/stage4_reviewer2.md`,
`research_ledger/stage5_0276.md` and `research_ledger/cheap_killers_0252_0046.md`. Where those
documents are silent, this file says so instead of filling the gap.

Epistemic labels per `Windows1/README.md`: KNOWN FACT, EVIDENCE, HYPOTHESIS, MODEL SPECULATION,
EXPECTED RESULT, ACTUAL EXPERIMENTAL RESULT.

**Nothing here is an ACTUAL EXPERIMENTAL RESULT.** `research_summary.md`: "We have **not** trained
models or measured Dice/mIoU/τ in this round." `README.md`: "**No numbers in this archive are measured
by us.**" Every threshold, gate and cost below is a pre-registered HYPOTHESIS or a HYPOTHESIS estimate.

**Input set caveat.** Which five candidates entered Stage 6 is not pinned by the record; see
`stage5_top5.md` §4. The most defensible reading is Constrained SAM-FT, 0085-M, 0074-M, 0276-M and
0252, with 0250 / Frozen-tuned n\* / interactive-eval-merge dying at or just before the lock. This
file adjudicates the winners and the runner-up, which *are* documented, and does not assert the
membership of the losing pair.

---

## 1. The locked portfolio and the reason for its shape

**KNOWN FACT.** `README.md` states the composition rule directly: "Stage 6 locked **method +
medical-safety characterization + medical uncertainty method**."

| Slate letter | Directory | Name | Portfolio role |
|---|---|---|---|
| **A** | `Idea_01` | RetainSAM | the **method** paper — and the #1 recommendation |
| **B** | `Idea_02` | LesionSuppress | the **medical-safety characterization** |
| **D** | `Idea_03` | DisagreeShift | the **medical uncertainty method** |

`evolution_summary.md` gives the reason the slate is shaped this way: "**Meta-audit:** portfolio was
over-indexed on eval science; medical/physics ideas had been over-killed by adjacency. **Final 3
restores method + two medical.**" See §4b — this was a deliberate correction, not a preference.

`reviewer_summary.md` states the supervisor's own summary of the lock: "Supervisor locked A/B/D to
keep **one method, one safety spec, one uncertainty method**, and because RetainSAM's kill test is the
**cheapest portfolio de-risk**."

**Slate letter C is unaccounted for.** The slate runs A, B, D with no C anywhere in the archive.
`NO RECORDED REASON — 需人工确认`; also logged at `FUNNEL_DEVIATION.md` §4-F.

**A structural fact about the whole slate (KNOWN FACT).** `reviewer_summary.md`: "Stage-4: **no idea
earned unconditional KEEP**. All finalists are **KEEP-IF-EXPERIMENT**." The Final 3 are therefore not
three approved projects; they are three conditional bets, each with a pre-registered way to die. That
is why §2 is organised around death conditions rather than strengths.

---

## 2. The three winners

Each entry gives the locked reason, the binding obligation the idea must honour, and the condition
under which it dies. **All three sets of conditions are transcribed from `README.md`,
`research_summary.md` and the per-Idea `README.md` files rather than restated in new words**, because
these are the round's locked commitments and paraphrase would weaken them.

---

### 2a. Idea_01 — RetainSAM (slate A, #1 recommendation)

Ancestry: `VFM-0263` + `VFM-0274` → Stage-3 MUTATE → panel P12 → Stage-5 engineer Top-5 #1.

**One-sentence hypothesis** (from `README.md`): "Fine-tune SAM on a target domain **subject to a
promptability-retention constraint**, and require the method to **strictly dominate WiSE-FT
interpolation** on a prompt-behavior Pareto front."

**Locked reason** — `README.md`, verbatim: "It is the only method-building project in the final three,
it has the cheapest decisive falsifier (WiSE-FT must be beaten), and a failure still leaves a reusable
promptability-retention benchmark."

**Binding obligation.** Must strictly dominate the WiSE-FT interpolation front — not match it, not
tie. `research_summary.md` locked hypothesis 1: "A promptability-constrained SAM fine-tune **strictly
dominates** the WiSE-FT interpolation Pareto on (target Dice, generic k-click mIoU). **Falsified if
interpolation matches or beats it.**" Domination must hold at **≥ 2 operating points**
(`README.md` step 5; `Idea_01/README.md` H1).

**Death condition (the kill switch).** `README.md`: "**Kill Idea_01** if constrained FT does not
strictly dominate interpolation at **≥2 operating points**" — and, per the recommendation section,
"If WiSE-FT already traces the Pareto front, **kill Idea_01 in week 1** and **promote Idea_03 to #1**."

`Idea_01/README.md` adds a second, separate falsifier and a required response to each:
- "**Kill H1** if the interpolation polyline is not strictly dominated."
- "**Kill H2** if naive FT already stays within ε — the problem does not exist for that domain (then
  try a farther domain before killing the project)."
- Stop/continue rule: "**Kill method:** no Pareto domination on 2/2 target domains."

**Inherited doubt, on the record.** Two independent reviewers flagged novelty fragility *before* the
lock, and the lock proceeded anyway with the kill switch as the mitigation:
- `meta_audit.md` **PARTIAL**: "constrained SAM-FT dual objective is method-shaped but **may lack
  novelty**; needs Stage3 of VFM keepers."
- Panel P12 remaining fatal flaw: "**High probability the interpolation baseline matches, leaving no
  paper.**"
- `stage3_vfm_kills.md`: "Constrained SAM-FT only survives if it beats WiSE-FT interpolation and ships
  a retention protocol."

**Salvage if it dies.** `Idea_01/README.md` §20: "If WiSE-FT matches: publish the
**promptability-retention suite** and the negative result ('interpolation is enough'). That is still a
paper, but not *this* method paper. **Pivot to Idea_03 as #1.**"

---

### 2b. Idea_02 — LesionSuppress (slate B)

Ancestry: `SEG-0085` → Stage-3 MUTATE ("lesion suppression law vs enhancement strength") → panel P8 →
`meta_audit.md` Top-8 #4 → Stage-5 engineer Top-5 #3.

**One-sentence hypothesis** (from `README.md`): "Measure **lesion-suppression probability** as a
function of size, contrast, and enhancement strength; validate rank-order against real LIDC small
nodules; **drop any 'universal law' claim** unless it survives."

**Locked reason.** It is the medical-safety slot. `evolution_summary.md` places it in the cluster
"Medical safety of enhancement pipelines (SEG-0085-M)", and `reviewer_summary.md` records that the
lock accepted its non-method character: from `Idea_02/README.md` §21–22, "'No method.' → agree: this
is a **spec/characterization** paper; Impact is the defense, not architectural novelty. **Stage 6
accepted that.**"

**Binding obligation — abandon "universal".** This was imposed at Stage 4 and is non-negotiable.
Panel P8 verdict: "KEEP-IF-EXPERIMENT — clinically important; **soften 'universal' to 'conditional
law'**." `evolution_summary.md` lists it under "Mutated and kept": "lesion suppression drops
'universal'". `Idea_02/README.md` §1 complies explicitly: "We do **not** claim a universal law across
all pipelines (**that claim was killed in review**). We claim a **safety specification**."
The universality hypothesis is retained only as an opt-out: `Idea_02/README.md` H3 is
"**optional, default OFF** … We do **not** need H3 to ship."

**Death condition — Kendall τ on LIDC small nodules.** `research_summary.md` locked hypothesis 2:
"Rank-order of suppression vs (size, CNR) from synthetic insertions matches real small-nodule
sensitivity on LIDC-matched bins (**Kendall τ significantly > 0**). **Falsified if τ low or
sign-flips.**" `Idea_02/README.md` H1 requires "τ … > 0 with **CI excluding 0**", and its stop rule is
"**Kill the project if H1 fails on the primary family (CNN denoiser).**"

Two further recorded failure modes, from `Idea_02/README.md` §19–20: "If τ~0: insertion model is the
paper's confounder — **stop claiming safety spec.** If CHO≠detector: **measurement invalid.**"

**Why τ and not an absolute number.** `Idea_02/README.md` §5: "Suppression is a **psychometric curve**,
not an mIoU footnote. **Rank-order transfer is the scientific gate**; absolute P values are EXPECTED to
be insertion-model dependent." This is what makes panel P8's "suppression is a pipeline config, not a
model property" attack survivable — the claim was narrowed to a rank order within a named family.

---

### 2c. Idea_03 — DisagreeShift (slate D)

Ancestry: `SEG-0074` → **Stage-3 KILL** → revived by `meta_audit.md` as a narrowed mutation only →
Top-8 #5 → Stage-5 engineer Top-5 #4. The only finalist that entered as a resurrected kill.

**One-sentence hypothesis** (from `README.md`): "Train **pixelwise uncertainty fields on inter-rater
disagreement** and test whether they keep **ordering-sensitive** meaning under scanner/stain shift,
where hard labels + temperature scaling structurally cannot."

**Locked reason.** The medical-uncertainty-method slot, and the recorded beneficiary of the portfolio
rebalance. `reviewer_summary.md`: "0074 original killed, mutation to disagreement-calibration
**revived by auditor + Stage 6**." It is also the designated successor if Idea_01 dies —
`README.md`: "**promote Idea_03 to #1**."

**Binding obligation — ordering-sensitive metrics, not ECE.** `research_summary.md` locked
hypothesis 3: "Disagreement-trained fields beat hard-label + temperature scaling on
**sparsification / pixelwise AURC** under scanner or stain shift, **even when ECE can be matched**."
`evolution_summary.md` under "Mutated and kept": "disagreement fields evaluated with
ordering-sensitive metrics **not ECE**."

**Second binding obligation — the revival is narrow.** `meta_audit.md` permits the revival only in
one form: "revive 0074 **only** as cross-stain calibration of disagreement fields (Stage3 killed
original histo-prob maps)", and explicitly **REJECTS** the wider claim: "treating 0074 original as
wrongly killed — original form **IS** published (RAPSODI/calibration). **Only mutation survives.**"
Reverting toward MRI–histo probability maps re-enters killed territory.
`Idea_03/README.md` §1 complies: "Original SEG-0074 (histo-validated infiltration maps) was
**killed** by existing MRI–histo pipelines. This mutation is a different question."

**Death condition — temperature scaling catching up.** `research_summary.md`: "**Falsified if TS
matches on ordering-sensitive metrics.**" `Idea_03/README.md`: "**Kill if TS matches AURC on the
primary shift.** Pivot to selective prediction / deferral if calibration transfers but Dice story is
muddy", and "Kill H1 fail. Continue if AURC wins on **2 shifts**."

**Anti-cheat condition, pre-registered.** `Idea_03/README.md` §19–22: "Fatal: too few scanners;
**TS-on-shifted-val as sneaky oracle. Pre-register: TS fitted only on source val.**" A TS baseline
tuned on shifted data would be an unfair win and is barred in advance.

**The logical basis of the bet (HYPOTHESIS, not fact).** `Idea_03/README.md` §5: "TS cannot implement
spatial disagreement. If we still lose, either raters' spatial conflict is not learnable from the
dataset size, or shift destroys the features that encode it." Its own confidence statement is
calibrated rather than promotional: "Confidence: **Medium-High on the logical gap; Medium on empirical
win**."

---

## 3. The runner-up: SEG-0276-M, and the disagreement about it

**KNOWN FACT — status.** `README.md`: "Runner-up **SEG-0276-M** (prior-shape interpolation α) is
**HRHR and inference-only**; revive it if **Idea_01 dies to WiSE-FT** *and* **Idea_03's TS baseline
unexpectedly matches**."

**Revival condition — conjunctive, not disjunctive.** Both clauses must hold. One finalist dying is
not enough: 0276-M returns only if the method slot *and* the uncertainty slot both fail. This is a
deliberately high bar and it is recorded as such.

`eliminated_ideas_summary.md` independently names it the first thing to bring back:
"**Revive first if a finalist dies:** SEG-0276-M (inference-only α, SSA controls, ~3 GPU-days)" — and
gives the Stage-6 cut reason: "SEG-0276-M \| **Strongest runner-up; cut to avoid three-eval-ish
portfolio and to keep medical B/D.**"

So 0276-M was not cut on quality. It was cut on **portfolio composition**, which is the same rule that
promoted Idea_02 and Idea_03. Stated plainly: it lost to a constraint, not to an argument.

**Design and gates, ready to execute** (from `stage5_0276.md`; all HYPOTHESIS): α = "projection of
(pred − instance GT SDF) onto (GT → class-prior) in canonical frame"; SSA control against wrong-class
/ global / morphology; causal test "wrong-class prompt redirects attraction"; gates = monotonicity,
Δα ≥ 0.10, SSA > 0, median ρ ≤ 0.5; cost "~3 A100-days **inference-only**".

### 3a. The designer/supervisor split — recorded, not smoothed

**This disagreement was never resolved by argument. It was resolved by the Stage-6 lock, against the
designer.**

- **The designer's position** — `stage5_0276.md`, verbatim: "Recommendation from designer: **INCLUDE,
  displace Constrained SAM-FT, keep 0085-M.**" The designer wanted 0276-M to take Idea_01's slot.
- **The supervisor's deferral** — same file, verbatim: "Supervisor: **wait Stage 6 lock**; 0276 is
  strong HRHR; **SAM-FT only if it beats WiSE-FT.**" The supervisor declined to decide at Stage 5 and
  postponed it to Stage 6.
- **Reviewer #2 agreed with the designer on ranking** — the recovered panel ranks P4 (0276-M) **#1**
  and constrained SAM-FT **#6** of 7, with 0276-M's rationale being that its "killer experiment is
  inference-only and decisively falsifiable". See `stage4_candidates.md` §4.
- **A third dissent, independently logged** — `reviewer_summary.md`: "Reviewer #2 preferred **0276-M
  over LesionSuppress** (characterization vs geometry law)", and separately "**0276 designer
  recommended displacing RetainSAM.**"

So at the Stage-6 lock, the two candidates the supervisor chose for slots A and B were each opposed by
a named reviewer in favour of 0276-M, and 0276-M had been Reviewer #2's #1 overall. It still lost.

**The recorded basis for overruling** is `reviewer_summary.md`: the lock was made "to keep one method,
one safety spec, one uncertainty method, and because **RetainSAM's kill test is the cheapest portfolio
de-risk**" — a portfolio-shape and cost-of-falsification argument, not a claim that 0276-M was weaker
science. `eliminated_ideas_summary.md` says the same thing from the other side: cut "to avoid
three-eval-ish portfolio".

**An unresolved tension worth flagging.** 0276-M was cut partly to avoid an "eval-ish" portfolio, yet
its killer experiment was the cheapest of the four (~3 A100-days, inference-only) — cheaper than
Idea_01's (~4–6 GPU-days per `Idea_01/README.md`), and Idea_01 was justified partly on cheapness of
falsification. The record does not reconcile these two cost arguments.
`NO RECORDED REASON — 需人工确认`.

### 3b. Other Stage-6 dissents on record

From `reviewer_summary.md`, "Stage-6 dissent on record":

- "Reviewer #2 preferred 0276-M over LesionSuppress (characterization vs geometry law)."
- "**Engineer wanted 0046-M as cheap insurance.**" — note this is the same 0046-M the engineer himself
  had cut at Stage 5 for "GT scarcity" (`stage5_killers.md`), and which carries a recorded
  "high prior-art risk" against SMOKE5K / Yan et al. AAAI 2022
  (`cheap_killers_0252_0046.md`). It did not get a slot.
- "0276 designer recommended displacing RetainSAM."

Three dissents, three rejections, all logged. `Windows4/selection_history/stage6_battle.md` uses the
phrase "No false consensus" for the same practice; Windows1 kept the dissents but did not keep the
session, which is the specific gap this file closes.

---

## 4. Recorded conflicts carried into Stage 6

Real disagreements between named reviewers, transcribed from the ledger. **No consensus is
manufactured for any of them.**

### 4a. Conflict 1 — SEG-0285 vs SEG-0252: the auditor and Reviewer #2 inverted each other

| Party | Verdict on 0285 | Verdict on 0252 | Source |
|---|---|---|---|
| **Reviewer #2** | **Promote** — Top-7 rank 2, "cheapest to execute" | **Drop** — cheap-killer rule, "needs real annotator generations" | `stage4_reviewer2.md`, recovered panel |
| **Meta-auditor** | **Cut** — "0285 cut from SURVIVE" | **Promote** — Top-8 #6 | `meta_audit.md` |

`stage4_reviewer2.md` names the clash and records the ruling, verbatim: "**CONFLICT with meta-audit:
auditor cut 0285 and promoted 0252.** Supervisor: **keep 0252 via cheaper proxy** (synthetic multi-gen
teacher→student loops + one small human study); **0285 only if dissociation from CLIP typographic
attacks is shown**; 0276 and constrained SAM-FT and 0085-M remain central."

`cheap_killers_0252_0046.md` confirms the direction: "Supervisor: **0252 remains in final-3 contention
over 0285.**"

**Both then lost anyway, and for the reasons each side had predicted.**

- **0252** was cut at Stage 6 — `eliminated_ideas_summary.md`: "Cheap killer exists; **Stage 6 cut on
  external-validity circularity**"; `evolution_summary.md`: "SEG-0252 label ecology (cheap ρ_H·ρ_M
  design exists; **external-validity circularity**)." The cheap proxy that rescued it was exactly what
  doomed it: `cheap_killers_0252_0046.md` states "Human-free kills K1–K3. **Cannot cheaply CONFIRM
  multi-gen human pipelines.**" An instrument that can only falsify cannot carry a positive claim, and
  Reviewer #2's original objection — that simulated annotators "would gut the claim" — was vindicated.
- **0285** never satisfied its condition. `eliminated_ideas_summary.md`: "Typographic injection
  established for VLMs (FigStep / multimodal neurons); **incremental at mask level**";
  `evolution_summary.md` lists "typographic mask injection as a lead idea" among kills. The required
  dissociation from CLIP typographic attacks was never shown, so the auditor's cut stood.

**Net effect on the record:** the supervisor split the difference at Stage 4 — rescuing 0252 on a
downgraded instrument and keeping 0285 alive on an unmet condition — and by Stage 6 both compromises
had collapsed. Neither reviewer was vindicated over the other; both were right about the candidate
they attacked.

### 4b. Conflict 2 — the portfolio was over-indexed on eval science

**This conflict is between the meta-auditor and the funnel's own accumulated output**, and it is the
reason the Final 3 look the way they do.

`meta_audit.md` opens with the supervisor conceding it: "Supervisor **ACCEPTS: eval over-indexing**;
…". `evolution_summary.md` states the finding and the remedy together: "**Meta-audit:** portfolio was
**over-indexed on eval science**; **medical/physics ideas had been over-killed by adjacency.** Final 3
restores method + two medical."

The mechanism named is **adjacency over-killing** — medical and physics ideas were being killed for
being *near* existing work rather than for being wrong. The evidence in the funnel supports that
reading: SEG-0074 was killed on MRI–histo adjacency, SEG-0046 on SMOKE5K / dehazing adjacency, and
both were then revived by the audit in narrowed form. `reviewer_summary.md` records the same movement:
"medical 0085-M mutated to a suppression *law/spec*; 0074 original killed, mutation to
disagreement-calibration revived by auditor + Stage 6."

**Consequence, stated plainly.** Two of the three finalists (Idea_02 and Idea_03) hold their slots
partly because of a **portfolio-balance correction**, and Idea_03's ancestor had been killed outright
at Stage 3. The Final 3 is a corrected slate, not the funnel's unmodified output. Recording this is
the point: a reader who assumes the three winners simply out-competed the field would be wrong.

**The correction had a cost, and it is also on the record.** The eval-science candidates that lost
slots to the rebalance were not judged worthless — `eliminated_ideas_summary.md` calls SEG-0250
"**Strong** but Stage 6 cut (**eval slot**)" and SEG-0276-M the "**Strongest runner-up**", both cut on
composition rather than on merit. `meta_audit.md` simultaneously instructed "Protect 0276 shape-prior
law and 0240 context sampling **as benches**", i.e. preserve them as benchmarks even while denying
them slots. So the rebalance traded away acknowledged quality for portfolio shape, deliberately.

### 4c. Conflict 3 — the two ranked lists that never reconciled

Recorded in full at `stage4_candidates.md` §5b and `stage5_top5.md` §3; summarised here because it
directly affected who was in the room at Stage 6.

The R2 Top-7 (`stage4_reviewer2.md`) ranked 0276-M **#1**. The Top-8 (`meta_audit.md`) **omitted
0276 entirely**. The Stage-5 engineer worked from the Top-8, so Reviewer #2's top-ranked candidate
silently fell out of the funnel and had to be restored by hand —
`stage5_killers.md`: "**SUPERVISOR CORRECTION: 0276-M shape-prior field was omitted from this Stage-5
prompt** (R2 ranked it #1, inference-only killer). **Must add back before locking Top-5.**"

**MODEL SPECULATION, flagged and not to be relied on:** had that omission gone uncaught, 0276-M would
not have been the runner-up and `README.md` would carry no revival path for a double finalist failure.
The record does not comment on this counterfactual.

---

## 5. Execution order and the branch points

`README.md` designates the first experiment; the ordering below is that designation plus the "Next
experiments" line from the same file. **Every cost is HYPOTHESIS. Every predicted outcome is
EXPECTED RESULT at most. Nothing has been run.**

### Step 1 (Week 1, gating) — RetainSAM kill test

The decisive experiment for the whole portfolio, transcribed from `README.md` "First experiment to
run":

1. "Fine-tune **SAM ViT-B** on one medical set (**Kvasir-SEG or ISIC**) with a standard recipe."
2. "Interpolate `θ(α) = (1−α) θ_SAM + α θ_FT` for **α ∈ {0, 0.1, …, 1}** (WiSE-FT)."
3. "Evaluate **target Dice** *and* a **frozen promptability suite** (**1/3/5-click mIoU, box prompt,
   iterative NoC**) on **COCO/LVIS held-out** images."
4. "Train the constrained objective once."
5. "**Kill Idea_01** if constrained FT does not strictly dominate interpolation at **≥2 operating
   points**."

The promptability suite is **frozen and gradient-free** — `Idea_01/README.md` §3: "Let D_gen be a
frozen generic promptability suite (images + click/box protocols, **no gradient**)." Its §14 also
requires reporting clicks **both** ways, "center-of-error simulation **and** random-interior clicks —
**RClicks showed simulation bias**; we report both" — a direct inheritance from the Stage-3 kill of
A0168.

Cost: **HYPOTHESIS**, "~4–6 GPU-days (A100)" for the killer, "~20 GPU-days" for the full study
(`Idea_01/README.md` §23).
Expected outcome: **EXPECTED RESULT only** — `Idea_01/README.md` §18 predicts naive FT gains and a
smooth WiSE-FT front, and explicitly labels the prediction "**(NOT measured)**".

**Branch actions after Step 1**

| Outcome | Action | Source |
|---|---|---|
| Constrained FT dominates at ≥2 points on ≥2 domains | **Continue**; Idea_01 stays #1 | `README.md`; `Idea_01/README.md` §25 "Continue: domination on medical + one non-medical (COD10K)" |
| Interpolation traces the front | **Kill Idea_01 in week 1. Promote Idea_03 to #1.** Publish the retention suite as a negative result / benchmark note | `README.md` §"#1 recommendation"; `Idea_01/README.md` §20 |
| Naive FT never violates ε | Do **not** kill yet — "**try a farther domain before killing the project**" | `Idea_01/README.md` "Kill H2" |
| Replay-only equals constrained | **Pivot** to a continual-learning short paper | `Idea_01/README.md` §25 |

### Step 2 (in parallel, low GPU) — the two medical killers

`README.md`: "In parallel (low GPU): **Idea_02** synthetic-vs-LIDC rank correlation on one lesion
family; **Idea_03** LIDC sparsification vs hard-label+TS on a held-out scanner."

| | Idea_02 | Idea_03 |
|---|---|---|
| Falsifier | Kendall τ vs real LIDC bins; kill if τ low or sign-flips | Sparsification / pixelwise AURC vs hard-label + TS; kill if TS matches |
| Pre-registered guard | primary family = CNN denoiser; CHO≠detector ⇒ measurement invalid | **TS fitted only on source val** (no shifted-val oracle) |
| Cost (**HYPOTHESIS**) | "~2 GPU-days (inference)", full "~10" | "~4 GPU-days (2D U-Net)", full "~16" |
| Continue rule | H2 dose-response per family; H3 universality stays OFF | "Continue if AURC wins on **2 shifts**" |
| Declared proxy risk | insertion realism is the confounder | if scanner metadata is insufficient, synthetic stain/noise shift is used and must be "**declare[d] proxy**" |

Both are run in parallel with Step 1 rather than after it, because neither depends on Idea_01's
outcome and Idea_03 must be ready to take #1 if Step 1 kills Idea_01.

### Step 3 (conditional, currently blocked) — revive SEG-0276-M

Trigger, both clauses required: **Idea_01 dies to WiSE-FT** *and* **Idea_03's TS baseline unexpectedly
matches**. Then run the design in `stage5_0276.md` against its four pre-registered gates
(monotonicity, Δα ≥ 0.10, SSA > 0, median ρ ≤ 0.5). Cost **HYPOTHESIS**: ~3 A100-days, inference-only.

If only Idea_01 dies, the recorded action is promotion of Idea_03, not revival of 0276-M.

---

## 6. What this reconstruction could not recover

- **The Stage-6 session itself.** No transcript, no vote, no per-candidate scoring. The three
  dissents in `reviewer_summary.md` are the only surviving trace of the deliberation.
- **Which five candidates were in the room.** See `stage5_top5.md` §4. Four are certain
  (Constrained SAM-FT, 0085-M, 0074-M, 0276-M), 0252 is near-certain, and 0250 / Frozen-tuned n\* /
  interactive-eval-merge cannot be placed. `AMBIGUOUS — 需人工确认`.
- **Slate letter C.** `NO RECORDED REASON — 需人工确认`.
- **Why the cheapest falsifier (0276-M, ~3 A100-days, inference-only) lost a slot to a costlier one
  (Idea_01, ~4–6 GPU-days) when cheapness of falsification was a stated reason for Idea_01's
  selection.** `NO RECORDED REASON — 需人工确认`. See §3a.
- **Whether SEG-0250 was cut at Stage 5 or Stage 6.** `eliminated_ideas_summary.md` says "Stage 6 cut
  (eval slot)" but no Stage-5 list contains it. `AMBIGUOUS — 需人工确认`.
