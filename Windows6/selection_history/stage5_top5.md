# Stage 5 — Top-5 (RETROSPECTIVE RECONSTRUCTION)

- **Windows ID:** Windows6
- **Branch:** `cursor/windows6-research-idea-evolution-b55d`
- **Reconstructed on:** 2026-08-29 (UTC)
- **Reconstructed from commit:** `69b4b2e` ("Research Idea Evolution - Windows 6 - Close remaining in-flight stage notes")
- **Task:** W6-T1 (first of three Windows6 close-out tasks: T1 → T2 → T3)
- **Document type:** **RETROSPECTIVE / 补记.** This is not a contemporaneous Stage-5 record.

## 0. Why this file exists, and what it is not

**FACT.** `evolution_summary.md` states: *"Stage 5 cloud engineering + DE assassin + auditor: **done**. Day-1 budgets ~2 / ~10 / ~8 GPU-h."* — i.e. the Stage-5 work is **claimed to have been performed**.

**FACT.** At commit `69b4b2e` there was **no `stage5_top5.md`** and **no `stage6_battle.md`** in `Windows6/selection_history/`. The Stage-5 claim was never landed as a file. This document is the after-the-fact reconstruction of that missing rung.

**Scope of this file (hard boundaries):**

- It **does not re-select** anything. Every verdict below is transcribed from an existing artifact.
- It **does not modify** `Idea_01/`, `Idea_02/`, `Idea_03/`, or any existing `stage1_pool/` / `stage2*` / `stage3*` / `stage4*` file.
- It **does not fix** the status contradictions it records in §5. Those are deliberately left for **W6-T3**.
- It reconstructs the Top-5 band **only** from `stage4_reviewer2_cheap5.jsonl`, because that is the only 5-item artifact this round actually produced.

### Evidence grading legend

| Label | Meaning as used in this file |
|---|---|
| **FACT** | Directly present in a Windows6 repository artifact; quotable and line-checkable. |
| **VERIFIED PRIOR WORK** | An external paper that a Stage-3/4 agent web-searched and used to kill or mutate an idea. We did **not** re-run their tables. |
| **HYPOTHESIS** | A scientific claim this round wants to test. Not measured. |
| **SPECULATION** | An inference made by *this* retrospective document that the artifacts do not state outright. |
| **EXPECTED RESULT** | A pre-registered predicted trend. Not measured. |
| **ACTUAL RESULT** | A number actually produced by running something. **There are none in Windows6.** |

**FACT.** Windows6 contains **zero ACTUAL RESULTS**. `Windows6/README.md` labels the three packages **"no real SAM numbers" / "no smoke mAP" / "no VLM eval"**, and `research_summary.md` states *"All quantitative claims in packages are EXPECTED/HYPOTHESIS unless labeled otherwise. Prototypes are synthetic."* The `~2 / ~10 / ~8 GPU-h` figures in `evolution_summary.md` are **budget estimates → HYPOTHESIS**, not measured runtimes.

---

## 1. FUNNEL DEVIATION DECLARATION (read this before the Top-5 table)

`supervisor_log.md` states the intended policy: *"Continue waves until ≥1000 unique ideas, then **1000→200→50→20→5→3**."* Windows6 did not execute that ladder. It was interrupted (Wave-1 timeouts) and closed out through a narrow "cheap" channel.

| Rung | Standard policy | Windows6 actual | Status |
|---|---|---|---|
| Raw pool | 1000+ | **1080 raw / 1062 live** (S-series 600 + A–F 480; "D surplus" per `evolution_summary.md`) | **MET** |
| → 200 | 200 scored survivors | **142** carried forward (78 ABCF + 64 DE) | **UNDER (−58)** |
| → 50 | 50-band | *never produced* | **MISSING** |
| → 20 | 20-band | *never produced* | **MISSING** |
| → 5 | 20 → 5 | **10 DE verdicts + 12 cheap-cluster verdicts → 5** (see §1.2) | **REPLACED, not executed as specified** |
| → 3 | 5 → 3 | **3 survive** (Reviewer #2, `stage4_reviewer2_cheap5.jsonl`) | **MET in count only** |

### 1.1 Line-item verification of the numbers above

**FACT (raw pool = 1080).** Record counts in `stage1_pool/`: `A/B/C/D/E/F_001_080.jsonl` = 80 each (480), `S_001_100.jsonl` = 100, `S_101_250.jsonl` = 150, `S_251_400.jsonl` = 150, `S_401_600.jsonl` = 200 (600). 480 + 600 = **1080**. The `1062 live` figure is asserted by `README.md` and `evolution_summary.md`; this file does not re-derive the 18-item delta.

**FACT (the 142 is not a clean "200 band").** The two Stage-2 artifacts and `README.md` describe this band inconsistently:

- `stage2_ABCF_summary.md`: *"Reviewed 320 (A+B+C+F). **78 survivors.**"* — `stage2_survivors_ABCF.jsonl` has **78** records.
- `stage2_DE_summary.md`: *"Reviewed 160 (D+E). **64 survivors / 96 killed.**"* — `stage2_survivors_DE.jsonl` has **64** records.
- `README.md`: *"Stage 2: **78+64 scored**."*

So 78 + 64 = **142** is described as *survivors* by the stage summaries and as *scored* by the README. Both readings fall short of the 200-band, in different ways:

1. Read as **survivors**: 142 < 200.
2. Read as **scored**: also wrong, because 480 items were actually reviewed (320 + 160), and the 142 are what came out.

**FACT.** Under either reading, **the 600 S-series ideas were never Stage-2 scored.** The supervisor seed catalog was started (per `supervisor_log.md`: *"Supervisor seed catalog started locally (S-series) so the funnel is not blocked by timeouts"*) but Stage 2 only covered A–F. This is the single largest deviation in the round: **55% of the raw pool never entered scoring.**

This file explicitly **refuses** to describe the round as having "completed a 200 band." It did not.

### 1.2 How the "→5" actually happened (reconstructed selection rule)

There was no 20-band to narrow. Instead two independent Stage-3 branches ran, and only one of them fed the 5:

**Branch A — cheap-killer prior-work cluster** (`stage3_prior_work_kill_cheap.jsonl`, **12** verdicts):
- keep ×2: `sam-amg-intensity-clustering` (0.6), `camera-id-leakage-smoke` (0.55)
- mutate ×4: `F-012-samhq-vs-filter` (0.35), `empty-slice-fpr-gate` (0.45), `alignment-tax-vlm-localization` (0.5), `clip-text-unused-organs` (0.5)
- kill ×6: `F-014-S-030-ln-affine-vs-lora`, `histogram-matching-da`, `lora-effective-rank`, `prompt-jitter-uncertainty`, `multiclick-nonmonotonic`, `dice-vs-ce-calibration`

**FACT.** The cheap-5 is exactly `keep ×2 + mutate ×3`, with the `F-012-samhq-vs-filter` mutate dropped:

> `sam-amg-intensity-clustering` + `camera-id-leakage-smoke` + `empty-slice-fpr-gate` + `alignment-tax-vlm-localization` + `clip-text-unused-organs` = **the 5 ids in `stage4_reviewer2_cheap5.jsonl`**

**SPECULATION.** No artifact states *why* `F-012` was excluded from the 5. `stage2_ABCF_summary.md` only warns *"Do not treat F-012 as 'filter matches HQ-SAM' (mutate to gain-stratification)"*. The exclusion is undocumented; this file does not invent a reason.

**Branch B — DE top-10 assassin** (`stage3_DE_top10.json.md`, **10** verdicts). **FACT:** none of the DE-only ideas entered the cheap-5 as their own line item. `E-009` reaches the Top-5 only because `auditor_overlay.md` merges it with `F-031` into one protected keep. `D-008`, `D-060`, `E-025` were parked as extensions (§4).

**Bottom line:** Windows6 went `1080 → 142 → (10 DE ‖ 12 cheap) → 5 → 3`. There was never a 50-band or a 20-band to prune from.

---

## 2. Top-5 (exactly 5, in `stage4_reviewer2_cheap5.jsonl` line order)

**FACT.** The membership of this table is not a Stage-5 judgement. It is a verbatim reading of the only 5-item artifact in the round.

| # | Stage-4 id | Original stage-1/2/3 numbering | Reviewer #2 verdict | `advance` | Into Final 3? |
|---|---|---|---|---|---|
| 1 | `AMG-HU-clustering` | **F-067** | survive | `true` | **Yes → `Idea_01`** |
| 2 | `camera-ID-smoke` | **F-043** | survive | `true` | **Yes → `Idea_02`** |
| 3 | `empty-slice-FPR-Dice` | **F-022** (+ **F-074**, dup) | **kill** | *(field absent)* | No |
| 4 | `alignment-tax-localization` | **F-031 / E-009** (+ **F-039**, format arm) | survive | `true` | **Yes → `Idea_03`** |
| 5 | `atlas-vs-CLIP-text` | **F-036 / F-037** | **kill** | *(field absent)* | No |

**Mapping evidence (all FACT, all locatable):**

- `auditor_overlay.md`: *"Protected keeps: **F-067** AMG clustering, **F-043** camera-ID, **F-031/E-009** alignment tax (stage-isolated)."*
- `auditor_overlay.md`: *"Reviewer #2 later **killed** **F-022** empty-FPR audit and **F-036/037** atlas-vs-text."*
- `stage2_ABCF_summary.md` supervisor overlay: *"Keep/mutate: **F-067** AMG-vs-kmeans, **F-043** camera-ID, **F-022/F-074** empty-FPR audit, **F-031/F-039** alignment tax, **F-036/F-037** atlas vs text."* — this is the one place all five map in a single line.
- `auditor_overlay.md` also records **F-074** as *"dup of F-022"* among the killed-despite-Stage-2-keep set.

---

### 2.1 `AMG-HU-clustering` — F-067

- **Original numbering:** `F-067` (`stage1_pool/F_001_080.jsonl`, seed `amg`, mutation type `cheaper`); Stage-3 record id `sam-amg-intensity-clustering`.
- **Scientific hypothesis (HYPOTHESIS):** On windowed CT, SAM's Automatic Mask Generation output is approximately intensity clustering in HU space rather than semantic objectness — so AMG should agree with k-means/multi-Otsu/GMM more than with texture superpixels (SLIC), and should move under intensity remaps while staying invariant to intensity-preserving texture shuffles.
- **Stage-1 minimal experiment (FACT, quoted):** *"MI(AMG,kmeans-intensity) vs MI(AMG,kmeans-ViTfeat) on 100 images; near-equality proves intensity suffices"*.
- **Stage-3 (FACT):** `continue: keep`, `novelty_confidence: 0.6`, remaining novelty *"Mechanistic AMG vs HU k-means equivalence on CT not found"*.
- **Reviewer #2 verdict (FACT):** `"continue":"survive"`, `"advance":true`.
- **Residual obligation (FACT, verbatim from `stage4_reviewer2_cheap5.jsonl`):**
  > `Must earn mechanistic via intensity vs texture counterfactuals; else evaluation note`
- **Meaning of the residual:** if the causal arm is not run, the contribution downgrades from a mechanistic claim to an evaluation note. `Idea_01/reviewer_attacks.md` states the same gate as *"If we cannot run the causal arm, **do not submit**."*
- **Final 3:** **Yes** — packaged as `Idea_01`. `README.md` marks it *"#1 start here"*.
- **Stage-5 engineering claim (HYPOTHESIS, budget only):** `Idea_01/experiments.md` records a Day-1 plan of 100 TotalSegmentator slices, soft-tissue window, SAM ViT-B AMG vs k-means vs multi-Otsu, then texture shuffle, **≤2 GPU-h**, plus a **COCO control** so clustering equivalence must be CT-specific. Not run. **No ACTUAL RESULT.**

### 2.2 `camera-ID-smoke` — F-043

- **Original numbering:** `F-043` (`stage1_pool/F_001_080.jsonl`, seed `smoke`, mutation type `cheaper`); Stage-3 record id `camera-id-leakage-smoke`.
- **Scientific hypothesis (HYPOTHESIS):** Smoke/fire benchmark scores are inflated by shared cameras across train/test, and *event-disjoint* splits do not remove this — camera-disjoint should score lower than random, and a linear camera-ID probe on frozen backbone features should beat chance.
- **Stage-1 minimal experiment (FACT, quoted):** *"Train linear camera classifier; correlate its accuracy with train/test gap across published splits"*.
- **Stage-3 (FACT):** `continue: keep`, `novelty_confidence: 0.55`, remaining novelty *"Peer-reviewed inflation quantification across smoke/fire benches"*.
- **Reviewer #2 verdict (FACT):** `"continue":"survive"`, `"advance":true`.
- **Residual obligation (FACT, verbatim):**
  > `Need event-disjoint vs camera-disjoint gap plus empty-frame memorization probe`
- **Meaning of the residual:** the camera-disjoint drop alone is not the paper; without separating geography shift from background memorization it collapses into an already-blogged diagnosis.
- **VERIFIED PRIOR WORK (used as the attack surface, not replicated):** PYRONEAR-2025 event-disjoint splits (arXiv 2402.05349); the Voxel51 Pyro-SDIS audit is explicitly logged in `Idea_02/literature.md` as *"2026 blog — diagnosis, **no** retrained mAP"*, with the instruction *"Do not cite a peer-reviewed mAP inflation number we did not compute."*
- **Final 3:** **Yes** — packaged as `Idea_02`.
- **Stage-5 engineering claim (HYPOTHESIS, budget only):** Pyronear-2025 subsample, YOLOv8n, 1 seed × 3 protocols + probe + empty-frame FPR, **~10 GPU-h**; equal-N class-ratio-matched splits, cluster bootstrap over events. Not run. **No ACTUAL RESULT** — `Idea_02/proposal.md` states *"We have not trained a detector here."*

### 2.3 `empty-slice-FPR-Dice` — F-022 (+ F-074)

- **Original numbering:** `F-022` (`stage1_pool/F_001_080.jsonl`, seed `dice-fpr-hist`, mutation type `reverse`), with `F-074` (seed `eval-flips`) recorded as a duplicate; Stage-3 record id `empty-slice-fpr-gate`.
- **Scientific hypothesis as last stated (HYPOTHESIS):** Empty-slice false positives on CT are a calibration failure rather than a representation failure, and empty-slice FPR is decorrelated from Dice across published leaderboards.
- **Stage-3 (FACT):** `continue: mutate`, `novelty_confidence: 0.45`, remaining novelty *"Cross-leaderboard FPR vs Dice decorrelation audit; kill two-stage gate as method"*.
- **Reviewer #2 verdict (FACT):** `"continue":"kill"`. **The record carries no `advance` field and no `residual` field** — only a `reason`.
- **Kill reason (FACT, verbatim from `stage4_reviewer2_cheap5.jsonl`):**
  > `Near-definitional Dice property; Metrics Reloaded; no leaderboard preds`
- **VERIFIED PRIOR WORK:** Metrics Reloaded, Nature Methods 2024 (`literature_anchors.md`).
- **Final 3:** **No.** `auditor_overlay.md` is explicit that the auditor's own keep does not override this: *"Those auditor 'keeps' do **not** enter Final 3."*

### 2.4 `alignment-tax-localization` — F-031 / E-009 (+ F-039)

- **Original numbering:** this is the one **merged** entry.
  - `F-031` (`stage1_pool/F_001_080.jsonl`, seed `vlm-clip`, mutation type `split`): *"Alignment tax on localization confounds RLHF objective with RLHF data distribution"*.
  - `E-009` (`stage1_pool/E_001_080.jsonl`, tag `rlhf-tax`): *"Quantify localization drop from base to RLHF checkpoint pairs"*.
  - `F-039` (seed `vlm-clip`, mutation type `reverse`) supplies the format-artifact arm: *"The tax is an output-format artifact: aligned models hedge on raw coordinates"*. Grouped with F-031 by `stage2_ABCF_summary.md` (*"F-031/F-039 alignment tax"*) but **not** named by `auditor_overlay.md`.
  - `auditor_overlay.md` is the authority for the merge: *"F-031/E-009 alignment tax (stage-isolated)"*.
  - Stage-3 cheap-cluster record id: `alignment-tax-vlm-localization`.
- **Scientific hypothesis (HYPOTHESIS):** After output format is controlled, chat/RLHF checkpoints localize worse than matched base/SFT checkpoints; if the drop appears only in generated coordinates and not in a frozen visual-token probe, the alignment tax is a formatting effect rather than a perceptual one.
- **Two Stage-3 verdicts, both recorded (FACT):**
  - cheap cluster: `continue: mutate`, `novelty_confidence: 0.5`, remaining novelty *"Stage-isolated base vs SFT vs RLHF localization curve only"*.
  - DE top-10 assassin: `E-009` **keep**, conf **0.55**, note *"matched checkpoint localization tax still open"*.
- **Reviewer #2 verdict (FACT):** `"continue":"survive"`, `"advance":true`. `reviewer_summary.md` qualifies it as *"survive (mutated)"*.
- **Residual obligation (FACT, verbatim):**
  > `Format-controlled eval + representation probe + small text-only DPO control`
- **Meaning of the residual:** three separate obligations — grammar-constrained/likelihood eval to kill the formatting confound, a frozen-visual-token probe to locate the tax, and a text-only DPO arm before any causal claim about the RLHF objective.
- **VERIFIED PRIOR WORK (attack surface):** MDGD visual forgetting (EMNLP Findings 2025) and TWIST & SCOUT (ICCV 2025) — `Idea_03/literature.md` records that the *stage-isolated localization curve* was **NOT FOUND** as a standalone paper (EVIDENCE GAP, conf ~0.5).
- **Final 3:** **Yes** — packaged as `Idea_03`. `README.md` calls it *"Highest impact, highest concurrent-work risk"*.
- **Stage-5 engineering claim (HYPOTHESIS, budget only):** one base/chat pair, 2k RefCOCO, three eval modes (free-form / grammar-constrained / likelihood rank vs ≤16 shared distractors), **≤8 GPU-h**, hard gate on identical vision encoder + coordinate tokenization; outcomes pre-registered as O1 format artifact / O2 policy tax / O3 representation tax. Not run. **No ACTUAL RESULT.**

### 2.5 `atlas-vs-CLIP-text` — F-036 / F-037

- **Original numbering:** `F-036` (*"Replacing the CLIP text tower with one-hot class embeddings loses nothing for organ segmentation"*) and `F-037` (*"A registered atlas probability channel subsumes text conditioning for organs"*), both `stage1_pool/F_001_080.jsonl`, seed `vlm-clip`; Stage-3 record id `clip-text-unused-organs`.
- **Scientific hypothesis as last stated (HYPOTHESIS):** In text-conditioned organ segmentation the CLIP text tower functions as a spatial prior, so an atlas centroid should substitute for it with no loss.
- **Stage-3 (FACT):** `continue: mutate`, `novelty_confidence: 0.5`, remaining novelty *"Atlas-centroid substitution proving text is spatial prior"*.
- **Reviewer #2 verdict (FACT):** `"continue":"kill"`. **No `advance` field, no `residual` field** — only a `reason`.
- **Kill reason (FACT, verbatim):**
  > `CLIP-Driven Universal Model ICCV 2023 one-hot ablation; substitution unidentifiable`
- **VERIFIED PRIOR WORK:** CLIP-Driven Universal Model, ICCV 2023 — its existing one-hot ablation is what makes the proposed substitution unidentifiable.
- **Final 3:** **No.** Same auditor override as §2.3.

---

## 3. Top-5 → Final 3 outcome

**FACT.** 3 of 5 survive with `advance: true`; 2 are killed. This is the only place where Windows6's realised counts match the standard funnel, and it matches by coincidence of the cheap channel, not by executing a 5-from-20 selection.

The Final 3 are provisional. `reviewer_summary.md`: *"Provisional **Final 3** pending DE-top10 assassin + auditor overlay."* Both of those have since been recorded (`stage3_DE_top10.json.md`, `auditor_overlay.md`), but no artifact declares the Final 3 confirmed — see §5.

---

## 4. Reserve / extensions (explicitly **not** Top-5 members)

**FACT.** `stage3_DE_top10.json.md` ends with: *"Held as **extensions**, not Final 3: **D-008, D-060, E-025**."* That is the original Stage-3 judgement; this file only transcribes it. None of the three appears in `stage4_reviewer2_cheap5.jsonl`, so **none of them is a Top-5 member** and none was ever seen by Reviewer #2's cheap-5 pass.

| ID | Stage-1 idea (verbatim) | Stage-3 DE verdict | Stage-3 note (verbatim) | Stage-2 DE score signal |
|---|---|---|---|---|
| `D-008` | *"Slice-flicker as uncertainty estimator"* | **keep**, conf 0.60 | *"slice-flicker as **eval** not FP-reduction train"* | keep, `protect_flag: true`, roi 5 |
| `D-060` | *"Volume-weighted per-organ FROC"* | **keep**, conf 0.55 | *"FPs per litre organ volume FROC"* | keep, roi 5 |
| `E-025` | *"Randomize Set-of-Mark numbering; measure answer variance"* | **mutate**, conf 0.50 | *"SoM on-image permutation; ship a fix"* | keep, `protect_flag: true`, roi 5 |

**Note on D-008 (FACT).** The Stage-3 keep is conditional on reframing: it survives as an **evaluation** signal, not as a false-positive-reduction training method. Any later revival must carry that constraint.

**SPECULATION.** These three scored as well as or better than several cheap-5 members on Stage-2 ROI, yet were parked. No artifact records the decision rule that sent the cheap cluster to Reviewer #2 while holding the DE keeps back. This is a consequence of the missing 20-band: with no common 20-item pool, the two Stage-3 branches were never ranked against each other.

**FACT.** The remaining DE top-10 entries were disposed of as follows and are **not** extensions: `E-035` kill (0.15), `E-041` kill (0.05), `E-057` kill (0.20), `D-067` kill (0.25), `D-062` mutate (0.40), `E-001` mutate (0.35). `D-062` and `E-001` are mutates with no recorded destination.

---

## 5. Status inconsistency register — **FOR W6-T3, NOT FIXED HERE**

**This task does not modify any of the files below.** They are recorded so that W6-T3 can reconcile them in one pass.

### INCONSISTENCY-01 — README says Stage 5/6 still open

- **File:** `Windows6/README.md`
- **Text (FACT):** *"Status: Provisional Final 3 packaged; Stage 5/6 still confirming against DE-top10 assassin + auditor."*
- **Conflicts with:** `evolution_summary.md`, which calls Stage 5 done.
- **Also relevant:** `Idea_01/README.md` says *"Status: Stage 4 survived Reviewer #2; **Stage 5 in flight**."* — a fourth phrasing of the same state.

### INCONSISTENCY-02 — supervisor_log still says Stage 1

- **File:** `Windows6/selection_history/supervisor_log.md`
- **Text (FACT):** *"Current stage: **Stage 1 — Massive Idea Exploration** (retry wave)"*, last updated 2026-08-28.
- **Conflicts with:** its own dispatch log, which already records *"Stage3 assassin done"* and the Reviewer #2 pass — i.e. the stage field is internally inconsistent with the same file's body, before any cross-file comparison.

### INCONSISTENCY-03 — evolution_summary says Stage 5 done, with no Stage-5 artifact

- **File:** `Windows6/selection_history/evolution_summary.md`
- **Text (FACT):** *"Stage 5 cloud engineering + DE assassin + auditor: **done**. Day-1 budgets ~2 / ~10 / ~8 GPU-h."*
- **Conflicts with:** the absence of `stage5_top5.md` at commit `69b4b2e` (the gap this file fills) and with INCONSISTENCY-01.
- **Additional flag:** the `~2 / ~10 / ~8 GPU-h` figures read as if measured. They are **HYPOTHESIS** (budget estimates). W6-T3 should label them.

### INCONSISTENCY-04 — Stage-3 cheap-cluster verdict counts do not add up *(newly observed by W6-T1)*

- **File:** `Windows6/selection_history/evolution_summary.md`
- **Text (FACT):** *"Stage 3 cheap-killer prior-work: done. **Keep 2, mutate 3, kill 6.**"* — that totals **11**.
- **Actual (FACT):** `stage3_prior_work_kill_cheap.jsonl` holds **12** records: keep 2, **mutate 4**, kill 6.
- **SPECULATION on cause:** the "mutate 3" appears to count only the mutates that advanced into the cheap-5, silently dropping `F-012-samhq-vs-filter`. If so, the summary is conflating "mutate verdicts issued" with "mutates promoted."
- **Left to W6-T3.** Recording only; not corrected here.

### Non-inconsistency, recorded for completeness

`README.md`'s *"Stage 2: 78+64 scored"* is loose wording rather than a contradiction (see §1.1), but it is the phrase most likely to be misread as "the 200-band was completed." It was not. **480 reviewed → 142 survivors; 600 S-series never scored.**

---

## 6. Provenance

**Artifacts read to build this file:** `Windows6/README.md`, `Windows6/research_summary.md`; `selection_history/` — `stage2_ABCF_summary.md`, `stage2_DE_summary.md`, `stage2_survivors_ABCF.jsonl`, `stage2_survivors_DE.jsonl`, `stage3_DE_top10.json.md`, `stage3_prior_work_kill_cheap.jsonl`, `stage4_reviewer2_cheap5.jsonl`, `auditor_overlay.md`, `reviewer_attacks.md`, `reviewer_summary.md`, `eliminated_ideas_summary.md`, `evolution_summary.md`, `literature_anchors.md`, `supervisor_log.md`, plus targeted ID lookups in `stage1_pool/*.jsonl`; and `Idea_01/`, `Idea_02/`, `Idea_03/` — `README.md`, `proposal.md`, `experiments.md`, `reviewer_attacks.md`, `roadmap.md`, `literature.md`.

**Files written by W6-T1:** this file only. No existing file was modified.

**Not produced by this task:** `stage6_battle.md` (still absent), any correction to INCONSISTENCY-01…04, any change to the Final 3.
