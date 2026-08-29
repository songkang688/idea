# Stage 6 — Research group battle (Windows8)

**This is a RETROSPECTIVE RECORD, not a live transcript.**

- **Written:** 2026-08-29 (UTC+8), by the Stage-6 recorder pass.
- **Round executed:** 2026-08-28 (per `README.md`, `research_summary.md`, `supervisor_log.md`).
- **Status of this document:** reconstructed after the fact from artifacts that already existed in this tree. No Stage-6 file was produced at the time the round ran. Every adjudication below is *transcribed or derived from a recorded artifact*, and each row cites where it comes from. Where a decision's rationale was never written down, that is stated instead of filled in.
- **What this file does not do:** it does not re-open the Final 3, does not modify `Idea_01/`, `Idea_02/`, `Idea_03/`, and does not modify `stage2_top200.md` / `stage3_top50.md` / `stage4_top20.md` / `stage5_top5.md`.

**Why the retrospective label is load-bearing (FACT).** `supervisor_log.md` contains exactly three sections — "Git numbering decision", "Stage 1 dispatch (t0)", "Stage 1 recovery (t1)". There is no Stage-6 dispatch entry, no vote tally, and no sub-agent id associated with any Stage-6 rejector. The only sub-agents this round ever recorded were the three Stage-1 batch generators, and all three failed on first dispatch (`request is required and could not be loaded from cloud agent state`). So no independent Stage-6 review process is evidenced, and this file does not claim one. See §5.

## Participating roles (as recorded, with their evidentiary status)

| Role | Where it is recorded | Independence evidenced? |
|------|----------------------|-------------------------|
| Supervisor / PI "Windows8" | `README.md` ("Supervisor: Windows8 (PI)"), `supervisor_log.md`, `research_summary.md` | N/A — sole decision-maker of record |
| "Skeptical PI" | `evolution_summary.md` → "Stage 6 unresolved disagreements", bullet 1 | **No.** Named as a position, no separate agent id or log |
| "Segmentation expert" | `evolution_summary.md` → same bullet 1 | **No.** Same |
| "Methodology reviewer" | `evolution_summary.md` → same section, bullet 2 | **No.** Same |
| "Reviewer #2" | `reviewer_summary.md` → "Reviewer #2 attacks that survived only if a killer experiment exists"; per-package `reviewer_attacks.md` in all three Idea dirs | **No.** A persona applied by the Supervisor as an adversarial checklist |
| Echo-chamber auditor | `reviewer_summary.md` → "Echo-chamber audit (Supervisor self-check)" — explicitly labelled a *self*-check | **No, by its own wording** |

**FACT.** The comparison round `Windows4` opens its `stage6_battle.md` with "Role cycle covered by Stage 3 assassins + Stage 4 R2 (**three independent rejectors**). No false consensus." Windows8 has no equivalent record and this file makes no equivalent claim.

## 1. Input to Stage 6

**FACT.** Five candidates, from `stage5_top5.md` (`count=5`, ROI order as recorded in `evolution_summary.md` → "Stage 5 Top 5 (ROI order)"):

| Stage-5 rank | ID | Codename |
|---|----|----------|
| 1 | `IDEA-X-0004` | Spectral LoRA audit |
| 2 | `IDEA-X-0001` | Exclusion-region prompting |
| 3 | `IDEA-X-0003` | IoU-token reject option |
| 4 | `IDEA-X-0007` | Replay for promptability |
| 5 | `IDEA-X-0002` | Density decoder on frozen SAM |

Output: three packages, locked in `README.md` and `research_summary.md` before this file existed.

## 2. Battle matrix, 5 → 3

### 2.0 Where the six criteria come from (no new dimensions were invented)

| Criterion used below | Recorded origin |
|---------------------|-----------------|
| Falsifiability of the scientific question | `reviewer_summary.md` Stage-2 dimension list ("scientific question", "soundness"); Stage-4 rule in `evolution_summary.md`: "Kill if no experiment can shut the attack"; every `proposal.md` states numbered falsifiable H1/H2/H3 plus a kill line |
| Killer-experiment cost, "one GPU-day" calibre | `README.md` → "Killer experiment is one GPU-day and can kill the project honestly"; Stage-5 rule in `evolution_summary.md` → "ROI = information per GPU-hour"; `reviewer_summary.md` Stage-2 dimensions "feasibility", "compute", "ROI" |
| Prior-work occupancy | `reviewer_summary.md` → "Prior-work kills (Stage 3) — EVIDENCE" table; `README.md` → "prior work already occupied the eval-only and adapter-SOTA slots"; `reviewer_summary.md` dimension "already-published risk" |
| Publishable if the result is null | `reviewer_summary.md` dimensions "risk"/"upside"; per-package negative-result clauses (`Idea_01/proposal.md`, `Idea_02/experiments.md` → "Negative", `Idea_03/proposal.md`) |
| Blast radius (if we are right, who was wrong) | `reviewer_summary.md` dimensions "significance"/"upside"; `research_summary.md` → "highest chance to change *where* people spend PEFT parameters". **Wording note:** "blast radius" is the phrase used in `Windows4/selection_history/stage6_battle.md`; it is adopted here as a label for the significance/upside axis Windows8 already scored, not as a new criterion |
| Data & checkpoint availability | `reviewer_summary.md` dimension "datasets"; `research_summary.md` → "Smoke dataset licenses and SAM checkpoints not in this VM"; `README.md` project-status table → Idea_01 "needs real SAM weights for science; toy loop runs"; `Idea_01/experiments.md` → "Datasets (plan, not downloaded here)" |

### 2.1 The matrix

All cells are **HYPOTHESIS**-grade judgements about unrun work, except where a cell states what a file says (**FACT**) or restates a prior-work attack recorded in `reviewer_summary.md` (**VERIFIED PRIOR WORK (as recorded)** — transcribed, not re-verified against the literature by this pass).

| Criterion | `X-0004` Spectral LoRA | `X-0001` Exclusion prompting | `X-0003` IoU reject | `X-0007` Replay promptability | `X-0002` Density head |
|---|---|---|---|---|---|
| **Falsifiable?** | **Yes, numerically.** Only candidate with a pre-registerable numeric threshold in its own proposal: "≥80% of energy below cutoff \(k_c\)", "pre-register \(k_c\)" (`Idea_02/proposal.md`) | **Yes**, H3 in `Idea_01/proposal.md`, but the decision boundary is qualitative ("do not help COCO") | **Yes**, and the sign of the effect is the test: ρ must go **negative**, not merely small (`Idea_03/proposal.md` H2) | **Yes**, with a stated numeric target: "<1 Dice drop on the medical target" (`raw/batch_X_hand.md`) | **Yes**, H1 in `Idea_01/proposal.md`, but stated as "higher NSD" without a margin |
| **Killer cost** (recorded estimate) | "Killer < 1 GPU-day" (`Idea_02/proposal.md`); Day-1 form can run on "any LoRA checkpoint or the toy trainer in `src/`" (`Idea_02/roadmap.md`) | Shares Idea_01 E0: "1×12–24GB GPU, <8h including embedding cache" (`Idea_01/experiments.md`) | **Cheapest of the five: "Zero training"** — dump SAM2 IoU tokens vs GT IoU on 100 COCO vs 100 Trans10K/smoke (`Idea_03/proposal.md`) | "COCO-proxy 200 images + LoRA" (`raw/batch_X_hand.md`) — requires an actual PEFT training run, so strictly more than the other four | Shares Idea_01 E0, same <8h budget |
| **Prior-work occupancy** | Open. "LoRA-MedSAM / SAMed: efficiency + Dice, **no spectrum**"; "Med-SA: adapter design, not frequency diagnosis" (`Idea_02/proposal.md`). Adjacent-but-not-same: spectral-bias work (Rahaman et al. 2019) marked "**adjacent**, not PEFT-delta" in `Idea_02/literature.md` | Open only as a *causal intervention*. The two neighbouring slots are taken: eval-only killed (arXiv:2412.01240; arXiv:2510.21782; Trans10K+SAM evals) and adapter-SOTA killed (Med-SA arXiv:2304.12620 / MedIA 2025, SAMed, LoRA-MedSAM) — `reviewer_summary.md` | Contested. `reviewer_summary.md` records the attack verbatim: "Everyone already thresholds SAM IoU." Survives **only** via anti-calibration evidence | Partly occupied. "Med-SA claims PEFT avoids forgetting **without measuring** promptable zero-shot" (`raw/batch_X_hand.md`) — the gap is real but is a measurement gap on someone else's claim | Same slot as `X-0001`; `Idea_01/proposal.md` novelty table lists it against 2412.04243 as the **competing mechanism** (objectness in \(D,p\) vs texture in \(E\)) |
| **Null still publishable?** | **Yes, explicitly.** "If r64 already high-pass: kill HP method; **maybe still publish the audit as a short note**" (`Idea_02/experiments.md`) | Yes. "If H1 is false: … publish the negative as support for 2412.04243-style encoder limits" (`Idea_01/proposal.md`); "If only H1: still a useful negative on encoder-adaptation narrative" (`Idea_01/roadmap.md`) | **No, as a lead.** "If only weakly calibrated, **kill and merge into Idea_01 analysis figure**" (`Idea_03/proposal.md`) | Not recorded either way. No negative-result clause exists for `X-0007` anywhere in the tree | Folded into Idea_01's negative clause; no separate publishable null |
| **Blast radius** | Wide but indirect: hits every dense-PEFT rank-tuning practice. `research_summary.md` frames Idea_01, not this, as "highest chance to change *where* people spend PEFT parameters", yet `evolution_summary.md` still ranks `X-0004` first on ROI — an unreconciled tension, see §5.2 | **Widest of the five.** If right, the "fine-tune / adapt the encoder" default is misdirected — `README.md`: "the cheapest falsifier of the 'fine-tune the encoder' default" | Narrower: changes deployment and reporting practice (abstention, risk-coverage) more than model design | Narrow: corrects one under-measured claim about PEFT and forgetting | Same blast radius as `X-0001` — they are two arms of one causal claim, which is why they merged (§4.1) |
| **Data / checkpoint availability** | **Least blocked.** Needs a LoRA checkpoint or the in-repo toy trainer; organ sets (Synapse/AMOS subset) are public research sets, no smoke licence involved | **Most blocked.** Needs real SAM weights ("needs real SAM weights for science", `README.md`) **and** a licence-clear amorphous set. Recorded fallback: "If licenses block, use a 200-frame hand-split from a CC-licensed smoke video — document provenance" (`Idea_01/experiments.md`) | Partly blocked: needs a SAM/SAM2 checkpoint, but its killer can run on COCO + Trans10K alone, so it **does not depend on the smoke licence** | Blocked on a PEFT training setup plus a COCO proxy | Same blockers as `X-0001` |
| **Stage-6 outcome** | **→ Idea_02** | **→ Idea_01 (lead arm)** | **→ Idea_03** | **Backup, not killed** (§4.2) | **Absorbed into Idea_01 (§4.1)** |

**FACT — cross-cutting constraint that applies to all five.** `research_summary.md` → "Unresolved risks": "Smoke dataset licenses and SAM checkpoints not in this VM." `README.md` project status marks all three packages as *ready to start*, none as started. Consequently **no candidate was eliminated at Stage 6 on measured evidence**, because there is no measured evidence: `evolution_summary.md` states "No actual experimental numbers were produced in this round."

## 3. The three winners: lock-in rationale, binding obligation, death condition

### 3.1 Idea_01 — Objectness, Not Features (`IDEA-X-0001` + `IDEA-X-0002`, lead package, #1 recommended)

**Won on: blast radius × killer cost, plus an open prior-work slot.** The recorded rationale is `README.md` → "Most recommended … **Idea_01.** It is the cheapest falsifier of the 'fine-tune the encoder' default, and prior work already occupied the eval-only and adapter-SOTA slots." `research_summary.md` adds the discriminating property: "Precise interaction hypothesis (win amorphous, lose COCO)." It is the only one of the five whose claim, if true, invalidates a *current spending pattern* rather than a *reporting habit*.

**Binding obligation — the COCO interaction control (H2). Not optional.**

- **FACT.** `research_summary.md` → "Unresolved risks": "Idea_01 can be **desk-rejected as a probe paper if the COCO interaction is omitted**."
- Operationally this is the two-sided continue rule already in `Idea_01/proposal.md`: continue only if NSD(B or C) > NSD(A) on amorphous **and** NSD(B) < NSD(A) on COCO. A one-sided amorphous win is *not* a pass.
- `Idea_01/reviewer_attacks.md` names the required artifact: "**Interaction plot:** amorphous gain × COCO loss (H2)", together with three further obligations that the same file marks as the things that "shut this up": parameter-matched tiny U-Net on frozen \(z\), a random-encoder control, and tightness-matched boxes (E1).
- One further non-negotiable from `Idea_01/reviewer_attacks.md`, quoted because its own wording is absolute: the train-data asymmetry between conditions B/C and zero-shot A must be declared as being about adaptation locus, "**say this in the intro or die**".

**Death / pivot conditions (all recorded).**

| Trigger | Action | Source |
|---|---|---|
| B ≪ A on amorphous | **Kill.** Encoder is the bottleneck; explicitly forbidden to "add adapters to 'fix' without new science" | `Idea_01/proposal.md` |
| B ≈ A everywhere | **Pivot**, possibly to a calibration paper | `Idea_01/proposal.md` |
| IoU tokens separate success/failure better than our head | **Pivot to Idea_03** | `Idea_01/roadmap.md` |
| H1 false after SAM2 + tightness controls | **Kill** | `Idea_01/roadmap.md` |
| H1 false **and** random-features encoder also fails | Read as encoder limit, align with 2412.04243, publish negative | `Idea_01/experiments.md`, `Idea_01/proposal.md` |
| H1 false **and** random-features encoder *works* | Not a result — treat as data leakage / implementation bug in our head | `Idea_01/experiments.md` |

### 3.2 Idea_02 — Spectral Locality of Dense PEFT (`IDEA-X-0004`)

**Won on: falsifiability precision and null-result value.** It is the only candidate carrying a numeric, pre-registerable threshold in its own proposal (≥80% of \(\|\delta\|_2^2\) below \(k_c\), with \(k_c\) pre-registered from patch size), and the only one whose failure mode still yields a publishable artifact ("maybe still publish the audit as a short note", `Idea_02/experiments.md`). `evolution_summary.md` ranks it #1 on Stage-5 ROI. It is also the least blocked by this VM's missing assets.

**It won despite being the weakest on venue fit, and that was recorded, not glossed.** `research_summary.md` risk: "Idea_02 may be 'not CV.'" `research_ledger.md`: "Confidence **medium-low (venue fit)**." `Idea_02/reviewer_attacks.md` attack: "not a vision paper; LoRA math already low-rank; HP is just a conv." The recorded reason for keeping it anyway is `evolution_summary.md`: "Decision: keep because it **predicts a *new adapter*** (high-frequency residual) if the spectrum claim holds" — i.e. it was kept as a *constructive* claim, not as a diagnostic.

**Binding obligation — the parameter-matched LOW-pass control must HURT.** This is the specific arm that converts "HP is just another conv" into a frequency claim:

- `Idea_02/proposal.md` → "Control: low-pass residual with same param count should **hurt** NSD if the story is frequency."
- `Idea_02/reviewer_attacks.md` lists it as obligation (2), and states the consequence of not running it in absolute terms: "**If we cannot run (2), kill the method half and keep audit-only (weaker).**"
- Two further obligations from the same file: (1) a rank-vs-frequency scatter plot, and (3) COCO promptability after PEFT as a second axis — which is the hook that keeps `X-0007` alive as a backup (§4.2).
- `reviewer_summary.md` states the reviewer-facing form: against "LoRA is low-rank by definition so spectrum is obvious", the answer must be rank-64 LoRA vs rank-4 + high-frequency residual, and "the prediction is **NSD gap not Dice gap**".

**Death / pivot conditions (all recorded).**

| Trigger | Action | Source |
|---|---|---|
| H1 false on **two** backbones | **Kill** | `Idea_02/roadmap.md` |
| r64 already high-pass | **Kill the HP method half**, keep the audit as a short note | `Idea_02/experiments.md` |
| Low-pass control cannot be run at all | **Kill the method half**, audit-only | `Idea_02/reviewer_attacks.md` |
| Killer is negative and forgetting is the remaining story | Activates `X-0007` (§4.2) | `eliminated_ideas_summary.md` |

### 3.3 Idea_03 — Selective SAM via IoU-token Recalibration (`IDEA-X-0003` + `IDEA-A-0064`)

**Won on: killer cost, and on being the only candidate whose killer needs no training and no smoke licence.** `Idea_03/proposal.md`: "**Zero training**: dump SAM2 IoU tokens vs GT IoU on 100 COCO vs 100 Trans10K/smoke. Plot reliability." Against the criterion "ROI = information per GPU-hour", it is the extreme point of the five.

**Binding obligation — demonstrate ANTI-calibration, not weak calibration.** The distinction is the entire paper:

- **FACT.** `evolution_summary.md` → Stage-6 disagreements: "Decision: keep **if** we show SAM IoU is *anti-calibrated* on amorphous targets (**not merely weakly calibrated**)."
- `reviewer_summary.md`: against "Everyone already thresholds SAM IoU", the answer must be "reliability diagrams showing **anti-calibration** (higher IoU token → higher error) on amorphous sets".
- `Idea_03/reviewer_attacks.md` adds two further obligations: "anti-calibration (**not just ECE>0**); coverage curves; reject **images** vs **pixels** (two protocols, **pre-registered**)".
- Formally this is H2 in `Idea_03/proposal.md`: on amorphous sets Spearman ρ "drops and may go **negative**". A positive-but-small ρ does not satisfy the obligation.

**Death condition — E0 with no calibration domain gap kills it. This is the hardest kill line of the three.**

| Trigger | Action | Source |
|---|---|---|
| E0 shows no calibration domain gap | **Kill** | `research_summary.md` ("Idea_03 dies if E0 shows no calibration domain gap"); `Idea_03/roadmap.md` ("Kill if no domain gap in E0"); `research_ledger.md` ("Confidence medium; **dies on E0**") |
| ρ stays high on amorphous | **Kill H2** — the central hypothesis | `Idea_03/proposal.md` |
| Only weakly calibrated (gap exists but no sign reversal) | **Kill as a lead** and merge into Idea_01 as an analysis figure | `Idea_03/proposal.md` |

## 4. The two candidates that did not become packages

**FACT, stated plainly because it matters for how much weight this Stage 6 can bear: neither was killed.** Of the five Stage-5 entries, four are inside the Final 3 and the fifth is parked. Nothing died at Stage 6. A battle stage in which no candidate is eliminated is a weak battle stage; that is recorded here as an observation, not excused. It also means the "5 → 3" reduction is arithmetically a **merge plus a park**, not a three-way win over two losers.

### 4.1 `IDEA-X-0002` Density decoder on frozen SAM — **ABSORBED** (neither backup nor kill)

**FACT.** `evolution_summary.md` → "Stage 5 Top 5 (ROI order)", item 5, states the disposition inline: "IDEA-X-0002 Density decoder on frozen SAM embeddings **(merged into Idea_01 method)**."

Corroborated by the package itself: the density head *is* Idea_01's method, not an option beside it. `Idea_01/proposal.md` step 2 is "**Density head** \(h_\theta(z)\)"; E0 condition B is "Frozen linear/density head"; the code artifact is `Idea_01/src/train_density_head.py`; the toy checkpoint is `Idea_01/outputs/idea01_e0/density_head.pt`. `IDEA-X-0001`'s exclusion region enters as condition C, "B + exclusion channel". So `X-0001` and `X-0002` are the two arms of a single interaction test, which is why they occupy one package rather than two.

**No activation condition applies** — it is already active as part of Idea_01. If Idea_01 dies, `X-0002` dies with it; there is no recorded path by which `X-0002` survives Idea_01's kill.

### 4.2 `IDEA-X-0007` Replay for promptability — **BACKUP**, with a recorded activation condition

**FACT.** `eliminated_ideas_summary.md` → "Parked high-ROI (not final 3)": "`X-0007 Replay promptability` | Why parked: **Strong**; overlaps Idea_02 forgetting subplot | **Revive if: Idea_02 killer is negative and forgetting is the remaining story**."

So the activation condition is explicit and it is gated on **Idea_02**, not on Idea_01 or Idea_03: if Idea_02's spectral killer comes back negative and the surviving story is forgetting of the promptable interface, `X-0007` is promoted.

**It is already partially wired in as a sub-axis, short of promotion.** `Idea_02/reviewer_attacks.md` obligation (3) is "COCO promptability after PEFT (**link X-0007**) as a second axis". So `X-0007` contributes an experimental axis to Idea_02 today, and becomes the lead only under the revive condition above.

**Gap, recorded not filled.** `X-0007` has no negative-result clause anywhere in the tree, so if it were promoted it would enter as the only one of the five without a written "what if this is null" answer. The generic funnel rule in `eliminated_ideas_summary.md` — "A killed idea is revived only if a new experiment would change the final-3 ranking" — governs the promotion, but says nothing about what happens after.

## 5. Unresolved disagreements kept explicit

Three disagreements were recorded at the time and are transcribed verbatim-in-substance. Two more were found by this retrospective pass and are labelled as such. **No consensus is manufactured for any of them.**

### 5.1 Recorded at the time (source: `evolution_summary.md` → "Stage 6 unresolved disagreements")

1. **Is Idea_01 "just prompting/eval" or a causal intervention on objectness?** Positions recorded as *Skeptical PI* vs *Segmentation expert*. **No resolution recorded** — `evolution_summary.md` lists it and stops. This is the disagreement that the §3.1 binding obligation exists to settle empirically: the COCO interaction is what separates "probe paper" from "causal locus".
2. **Is Idea_02 a vision contribution or a PEFT diagnostic?** Position recorded as *Methodology reviewer*. **Resolved in favour of keeping**, with the reason recorded: "keep because it predicts a *new adapter* (high-frequency residual) if the spectrum claim holds." The disagreement is not thereby dissolved — `research_summary.md` still carries "Idea_02 may be 'not CV'" as a live risk and `research_ledger.md` still rates venue-fit confidence "medium-low".
3. **Is Idea_03 just classical selective classification?** **Resolved conditionally**: "keep if we show SAM IoU is *anti-calibrated* … (not merely weakly calibrated)." The condition is unmet as of this writing, so the disagreement is open in practice.

### 5.2 Found by this retrospective pass — execution-order contradiction

**FACT.** Two recorded orderings disagree about what runs first.

- `evolution_summary.md` Stage-5 ROI order puts `IDEA-X-0004` (Idea_02) at rank 1, ahead of Idea_01's arms.
- `README.md` → "Next experiment to run: **Idea_01 E0**", and `research_summary.md` → "First experiment to run: `Idea_01` E0".

Two files say Idea_01 first, one ordering says Idea_02 first. §6 follows the two-file majority (Idea_01 E0 first) because it is the more explicit instruction, and flags the contradiction rather than silently picking. **Human adjudication requested.**

There is also a third position that no file states, so it is not adopted: on a pure gating argument Idea_03's E0 is the only killer that needs zero training and no smoke licence, so it is the cheapest way to remove one of three packages. Labelling this honestly — **SPECULATION** by this auditor, not a recorded Windows8 decision, and deliberately not used to reorder §6.

### 5.3 Found by this retrospective pass — the methodological defect of this round

**FACT.** Windows8's Stage 6 had **no independent rejector.** Evidence, all from existing files:

- `supervisor_log.md` records no Stage-6 dispatch, no rejector agent id, and no vote.
- The three roles named in the disagreement list have no agent ids, unlike the Stage-1 batch agents, which do (`bc-c89434d9-…`, `bc-3afc797e-…`, `bc-4a5961ff-…`, plus retries `bc-7a636a75-…`, `bc-fb91c4d2-…`).
- All three original Stage-1 cloud sub-agents ERRORed, and two batches were recovered by **local** file-writers — so this round never successfully ran an independent adversarial agent at any stage.
- `reviewer_summary.md`'s adversarial section is a "Reviewer #2" persona and its bias check is explicitly a "Supervisor **self**-check".
- The self-check names its own exposure: "Bias risk: over-weighting SAM… Bias risk: over-weighting smoke." Both risks are visible in the outcome — all three packages are SAM-family, and two of the three depend on amorphous/smoke-type targets.

**Consequence for how much this Stage 6 proves.** The three disagreements in §5.1 are real records, but they are positions articulated by one Supervisor, not the output of independent rejectors. Windows4's Stage-6 claim of "three independent rejectors" does not transfer to Windows8. This is logged as a **methodological defect of the Windows8 round**, and is the honest answer in place of a fabricated multi-agent debate.

**Related, and already documented elsewhere — do not re-litigate here.** `stage5_top5.md` §4 and §5 (added by the Stage-5 audit pass, 2026-08-29) record that `stage2_top200.md` is a mechanical prefix of the idea grid covering only 10 of 52 cores, that 30 of the 50 IDs in `stage3_top50.md` never appear in `stage2_top200.md`, and that three lineage tokens cited for the Final 3 (`LINEAR-PROBE` = `IDEA-A-0316`, `PEFT-SPECTRAL` = `IDEA-A-0211`, `SELECTIVE` ≈ `IDEA-A-1051`) cannot be traced through Stage 4. Those defects sit upstream of Stage 6 and are already routed for human adjudication in that file.

## 6. Decisive experiments — mandatory execution order

Order below follows `README.md` and `research_summary.md` (see §5.2 for the contradiction with the ROI ordering). **All costs are recorded estimates; the estimates themselves are HYPOTHESIS, since nothing has been run.** Thresholds are quoted from the packages; where a package leaves a threshold qualitative, that is flagged as a pre-registration gap to close *before* the run, not during it.

### Step 1 — Idea_01 E0 (the objectness killer)

- **Setup (FACT, as recorded):** cache frozen SAM embeddings on 200 amorphous + 100 COCO; train `DensityHead`; conditions A = prompted SAM with GT box, B = frozen density head, C = B + exclusion channel. `Idea_01/experiments.md`, `Idea_01/roadmap.md` ("Day 1 … **Stop criteria applied the same evening**").
- **Cost estimate (HYPOTHESIS):** 1 × 12–24 GB GPU, < 8 h including the embedding cache.
- **Prerequisite that is currently unmet (FACT):** real SAM weights, plus a licence-clear amorphous set; recorded fallback is a 200-frame hand-split from a CC-licensed smoke video with documented provenance.
- **Decision rule (FACT, from `Idea_01/proposal.md`):**

| Outcome | Action |
|---|---|
| NSD(B or C) > NSD(A) on amorphous **AND** NSD(B) < NSD(A) on COCO | **Continue** to Step 1b |
| B ≈ A everywhere | **Pivot** (candidate: calibration paper) |
| B ≪ A on amorphous | **Kill** Idea_01; do not patch with adapters |
| Amorphous win but **no** COCO loss | **Do not proceed as-is** — this is the desk-reject shape named in `research_summary.md`; the interaction claim, not the win, is the paper |

- **Pre-registration gap (flagged):** "≈" and "≪" carry no numeric margin in any file, and no seed count or significance test is specified. **HYPOTHESIS:** without a pre-registered margin and repeat count, Step 1's own stop rule is not decidable. Fix before running.
- **Step 1b, same gate, before any claim leaves the room (FACT, from `Idea_01/reviewer_attacks.md` and `experiments.md` E1–E3):** tightness-matched boxes, random-encoder control, SAM2 frozen encoder, parameter-matched tiny U-Net. `Idea_01/roadmap.md` places these at Day 2–3. Note the recorded reading of the random-encoder control: if H1 fails *and* random features also fail → encoder limit (a real negative result); if H1 fails *and* random features **work** → treat as our own leakage/bug, not a finding.

### Step 2 — Idea_02 FFT audit (the spectral killer)

- **Setup (FACT):** LoRA on a small organ set (Synapse/AMOS subset); cache \(\delta\) on 64 images; radial power spectrum; energy fraction below \(k_c\). Day-1 fallback explicitly permits "any LoRA checkpoint or the toy trainer in `src/`" (`Idea_02/roadmap.md`).
- **Cost estimate (HYPOTHESIS):** killer < 1 GPU-day; full Synapse/AMOS 3–5 days.
- **Decision rule (FACT, from `Idea_02/proposal.md`, `experiments.md`, `roadmap.md`):**

| Outcome | Action |
|---|---|
| ≥ 80% of \(\|\delta\|_2^2\) below pre-registered \(k_c\) **and** r64 does not move energy above \(k_c\) | **Continue** to the r4 vs r64 vs r4+HP arm |
| r4+HP > r64 on **NSD** at matched parameters (Dice may be flat) | **Continue** — the constructive claim holds |
| Param-matched **low-pass** residual does *not* hurt NSD | **Kill the method half**, keep audit-only — the frequency story is unsupported |
| Low-pass control cannot be run at all | **Kill the method half**, audit-only |
| r64 already high-pass (H1 false) | **Kill the HP method**; the audit may still stand as a short note |
| H1 false on **two** backbones | **Kill Idea_02**, and evaluate promoting `X-0007` per §4.2 |

- **Pre-registration gap (flagged):** \(k_c\) must be fixed from patch size *and written down* before the first FFT. The 80% figure is pre-registered; \(k_c\) itself is not yet a number in any file.

### Step 3 — Idea_03 E0 (the calibration killer)

- **Setup (FACT):** zero training; dump SAM/SAM2 IoU tokens vs GT IoU on 100 COCO vs 100 Trans10K/smoke; reliability diagrams; then isotonic on val and risk-coverage on test (Day 2–3).
- **Cost estimate (HYPOTHESIS):** inference only, no training; the smallest budget of the three. No figure is recorded, so none is asserted.
- **Decision rule (FACT, from `Idea_03/proposal.md`, `roadmap.md`, `research_summary.md`, `evolution_summary.md`):**

| Outcome | Action |
|---|---|
| ρ positive on COCO with ECE under the pre-registered bound, **and** ρ drops to ≈0 or **negative** on amorphous | **Continue** to isotonic + risk-coverage |
| Domain gap exists but **no sign reversal** (weak calibration only) | **Kill as a lead**; merge into Idea_01 as an analysis figure |
| ρ stays high on amorphous | **Kill** H2, and with it Idea_03 |
| No calibration domain gap at all | **Kill Idea_03** — the single hardest kill line in this round |

- **Pre-registration gap (flagged):** `Idea_03/proposal.md` requires "ECE below a **pre-registered bound**" but no bound is written anywhere; likewise the H3 coverage target appears as "cover 80%" in the proposal and "coverage 80%" in the expectations, but the image-level vs pixel-level protocol split that `reviewer_attacks.md` demands be pre-registered is not yet specified. Both must be fixed before E0, or E0 cannot kill anything.

### Cross-step interactions (recorded, not invented)

- Step 1 → Step 3: if Idea_01's E0 shows IoU tokens separate success from failure better than the density head, `Idea_01/roadmap.md` says **pivot to Idea_03**. So a Step-1 failure can *strengthen* Step 3 rather than being wasted.
- Step 3 → Step 1: a weak-calibration-only outcome sends Idea_03's content into Idea_01 as an analysis figure (`Idea_03/proposal.md`).
- Step 2 → `X-0007`: a negative spectral killer with forgetting as the surviving story promotes the backup (`eliminated_ideas_summary.md`).
- **Consequence worth naming (HYPOTHESIS):** these three packages are not independent bets. Idea_01 and Idea_03 can each absorb the other's failure, and Idea_02 hands off to a backup. Correlated failure is therefore plausible: a common-cause failure — no SAM checkpoint, or no licence-clear amorphous data — takes out Steps 1 and 3 together, since both need real SAM weights. `research_summary.md` already lists that exposure.

## 7. Battle stop

**FACT.** No candidate in the Stage-5 five was eliminated at Stage 6 on evidence, because no experiment had been run. `evolution_summary.md`: "6 Battle | 3 | **3** | No false consensus; remaining disagreements listed below" and "No actual experimental numbers were produced in this round." The Final 3 were locked on recorded *a priori* judgement — cost, falsifiability, prior-work occupancy, blast radius — not on measurement. This file records that as the state of affairs rather than dressing it up as an adjudicated contest.

## 8. Funnel completeness index

| Level | Target | File of record | Recorded count |
|---|---|---|---|
| 1 Raw | ≥ 1000 | `raw/pool.jsonl` (+ `raw/batch_A|B|C.md`, `raw/batch_A|B|C_prior.md`, `raw/batch_X_hand.md`) | 2766 |
| 2 Review | ~200 | `stage2_top200.md` | 200 |
| 3 Prior-work attack | ~50 | `stage3_top50.md` | 50 |
| 4 Reviewer #2 | ~20 | `stage4_top20.md` | 19 |
| 5 Engineering / ROI | ~5 | `stage5_top5.md` | 5 |
| 6 Battle | 3 | **`stage6_battle.md` (this file)** + `Idea_01/`, `Idea_02/`, `Idea_03/` | 3 |

Every level now has a file. **That is not the same as every level being auditable** — the Stage-2 and Stage-2→3 defects recorded in `stage5_top5.md` §4 remain open, as do the three lineage tokens in `stage5_top5.md` §5.

## 9. Evidence-grade statement for this file

- **FACT** — what a file in this tree says, and the absence of things verified absent (no Stage-6 dispatch in `supervisor_log.md`; no agent ids for the Stage-6 roles; no Stage-6 file before this one).
- **VERIFIED PRIOR WORK (as recorded)** — prior-work attacks and identifiers (Med-SA arXiv:2304.12620 / MedIA 2025; SAMed arXiv:2304.13785; LoRA-MedSAM; MedSAM arXiv:2304.12306; SAM arXiv:2304.02643; SAM 2 arXiv:2408.00714; HQ-SAM arXiv:2306.01567; arXiv:2412.01240; arXiv:2412.04243; arXiv:2510.21782; Trans10K; nnU-Net Nature Methods 2021; LoRA ICLR 2022; Rahaman et al. 2019; Geifman & El-Yaniv; Guo et al.; CC-Dice AAAI 2025) are transcribed from `reviewer_summary.md`, `eliminated_ideas_summary.md` and the three `literature.md` files. **This pass did not re-verify any of them against the literature, and added no paper, citation, venue or author.**
- **HYPOTHESIS** — every criterion judgement in §2.1, every cost estimate in §6, and every claim about how an unrun experiment will behave.
- **SPECULATION** — marked inline, used exactly once (§5.2, the gating argument for running Idea_03 first) and explicitly not acted on.
- **EXPECTED RESULT** — only where a package already frames a prediction, e.g. `Idea_01/proposal.md` "Amorphous NSD: C ≥ B > A; COCO: A > B"; `Idea_02/proposal.md` "Dice: r64 ≈ r4+HP > r4. NSD: r4+HP > r64 ≥ r4"; `Idea_02/experiments.md` "Predicted: random 3×3 ≈ LoRA extra rank (no NSD gain)"; `Idea_03/proposal.md` "H1 true, H2 true, coverage 80%".
- **ACTUAL RESULT — none.** The label is applied to nothing in this file; this bullet is its only appearance. The only numeric artifacts in the tree are toy or synthetic and self-labelled: `Idea_01/outputs/idea01_e0/toy_report.txt` ("TOY RUN (FakeEncoder). NOT a scientific result."), its companion `density_head.pt`, `Idea_02/outputs/idea02_fft/toy_report.txt` ("TOY LoRA on random tensors. NOT a scientific result."), `Idea_03/outputs/idea03_e0/toy_report.txt` ("SYNTHETIC illustration of H1/H2. NOT measured on SAM."). Per `README.md`, "Do not report FakeEncoder numbers as results" — no value from those files is reproduced here as evidence for or against any hypothesis, and no such value influenced any adjudication above.
- **No fabricated process.** No reviewer agent, vote, score, ranking session or debate is asserted that is not already recorded in `evolution_summary.md`, `reviewer_summary.md` or the per-package `reviewer_attacks.md`. Where the record is silent, §5.3 says so.
