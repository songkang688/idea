# Agent E Report — Stage-2 Review & Prior-Work Attack on Batch B

**Role:** Independent Reviewer + Novelty Assassin for batch B (VFM / VLM / PEFT / forgetting).
Not the PI; no final-3 selection made. Batch C untouched (Agent D's territory).

**Deliverables (all under `Windows2/_wip/stage2_agent_E/`):**

| File | Contents |
|---|---|
| `scores.jsonl` | All 345 ideas, 14 dimensions each, verdict + protection tag + note |
| `shortlist.md` | 77 keeps (31 protected), top tier, protected exceptions |
| `kills.md` | 268 kills with per-idea justification and kill taxonomy |
| `prior_work_attack.md` | 26 adversarial literature attacks (15 mandated + 11 self-ranked-high) |
| `AGENT_REPORT.md` | this file |

**Headline numbers:** 77 keep / 268 kill. Attack outcomes on the mandated 15:
6 SURVIVE (0001, 0074, 0104, 0293, 0307, 0332), 7 MUTATE (0042, 0098, 0154, 0200, 0203, 0226, 0254),
2 KILL (0136 — Davari et al. CVPR'22; 0175 — RClicks NeurIPS'24). Among my 11 extras:
4 SURVIVE (0114, 0304, 0323, 0268), 6 MUTATE (0101, 0145, 0163, 0172, 0213, 0339), 1 KILL (0279 — DINOv3 medical benchmark).

---

## 1. Twenty PhD-year bets from batch B

Ideas I would stake a PhD year on, given one strong student, a few hundred GPU-hours to a few
thousand (flagged where more), and today's literature. Ordered roughly by conviction × feasibility,
not by mean score. Mutated forms are the bet where noted.

1. **W2-B-0114** — VPT tokens as trainable registers. The frozen-random-token control is an afternoon; every outcome (full, partial, no reproduction of VPT gains) is publishable. Best risk-adjusted bet in the batch.
2. **W2-B-0001** — Register-norm maps as free per-pixel uncertainty. Cheap, decisive, deployment-relevant; survived direct attack on the hottest artifact literature.
3. **W2-B-0304** — Language quantizes shape space. Psychophysics-grade paradigm nobody occupies; multi-pipeline morph controls make it rigorous.
4. **W2-B-0074** — Modality-gap collapse dynamics predict zero-shot loss. Gap statics are crowded, dynamics are empty; early-warning signal has practical teeth.
5. **W2-B-0323** — Mention bias imprint on feature decodability, SSL-normalized, with small-scale caption-intervention causal check.
6. **W2-B-0104** — Invariance-inheritance ceiling of PEFT on dense tasks. Mechanism + failure predictor; must be positioned against intruder-dimensions and LoRA-learns-less.
7. **W2-B-0307** — Causal matched-data test of language-alignment cost to metric depth. Needs moderate pretraining compute; highest scientific ceiling of the geometry family.
8. **W2-B-0332** — Artifact-swap causal test of visual CoT faithfulness. Execute early; fastest-decaying novelty among survivors.
9. **W2-B-0268** — Benchmark contamination by generated imagery + ranking distortion. Urgency bet: the clean-baseline window is closing.
10. **W2-B-0213 (mutated, merged with 0200)** — Resolution × probe-capacity confound audit; which published VFM-ranking conclusions invert under corrected protocol.
11. **W2-B-0226 (mutated)** — Shift-budget curves frozen-vs-tuned for dense prediction; functional-form stability across shift families.
12. **W2-B-0101 (mutated)** — Task-indexed required-rank law: LoRA accuracy vs captured spectral mass, validated cross-task.
13. **W2-B-0145 (mutated)** — Spatial calibration decay precedes accuracy decay in dense adaptation; region-level early warning.
14. **W2-B-0194** — Segmentation sycophancy: confidence rises with prompt count while accuracy doesn't. Cheap, catchy, safety-adjacent.
15. **W2-B-0169** — Negative-click dose-response: more negative points hurt beyond 2–3. Clean response-surface design; practitioners feel this daily and nobody measured it.
16. **W2-B-0164** — Relearning-speed (savings) paradigm for VFM forgetting: memory that retention probes miss. Near-free on existing checkpoints.
17. **W2-B-0227** — Cleaner labels transfer worse (label-noise paradox) via controlled noise ladders. Contrarian, cheap, decisive either way.
18. **W2-B-0263** — Procedural corruptions beat realistic generated ones for robustness training; structure-preservation mechanism.
19. **W2-B-0286** — Site-of-origin decodability: natural VFMs more site-invariant than medical FMs. Cheap, provocative, pairs with 0293's program.
20. **W2-B-0042 (mutated)** — The synonym-variance ledger: is name noise bigger than published OVS effect sizes? Field-hygiene result with guaranteed citations.

Deliberately excluded despite conviction: **0293** and **0317** — both top-quality science, but 0293 needs
matched-budget pretraining runs (compute partner, not a solo PhD-year) and 0317's identifiability theory
needs a theory collaborator; both belong in the portfolio only with those resources secured.

## 2. Ten almost-killed-then-revived

Ideas that were one keystroke from the kill file, and what saved them.

1. **W2-B-0025** (attention maps epiphenomenal?) — nearly killed for fragile intervention design; revived because either outcome splits the interpretability community (DP protection is for exactly this).
2. **W2-B-0033** (seed variance vs published VFM gaps) — nearly killed for pretraining cost; revived as the field's missing error bar — reproducibility science that changes how every comparison paper is read.
3. **W2-B-0092** (inverse stability scaling) — nearly killed as probably-false; revived because a 3-point model ladder bounds the cost of checking a claim that, if true, breaks default scaling intuitions.
4. **W2-B-0133** (LoRA memorizes more per-parameter) — nearly killed fearing PEFT-privacy prior work; search found membership-inference-on-PEFT work but not the per-parameter inversion claim; revived with a mandatory pre-execution literature re-check.
5. **W2-B-0157** (prompt-template staleness inflates forgetting estimates) — nearly killed as a measurement nitpick; revived because it invalidates numbers in a live literature — small work, outsized correction value.
6. **W2-B-0164** (savings/relearning paradigm) — nearly killed as a psychology-import gimmick; revived because relearning speed measures retained structure that all current retention probes miss, at near-zero cost.
7. **W2-B-0215** (text-aligned subspace vs complement for dense info) — nearly killed as post-hoc geometry; revived because the decomposition makes a testable prediction about *which* dense tasks text-aligned features fail.
8. **W2-B-0252** (interpolation-frontier kinks) — nearly killed as a likely null; revived under HRHR protection: kinks reproducing across model pairs would be evidence of discrete mechanism transitions — cheap enough to gamble.
9. **W2-B-0325** (text-only counterfactual decomposition of spatial errors) — nearly killed because blind/language-prior baselines are standard in VQA; revived because the *decomposition* (inherited-linguistic vs visual error mass) is not in the dense/spatial literature.
10. **W2-B-0338** (web-agent benchmark contamination via retrieval) — nearly killed as 0268's shadow; revived because the blinding experiment (answers reachable via retrieval vs not) is decisive and the agent-eval community has not run it.

## 3. Bias audit

Honest accounting of where my judgment is likely skewed:

- **"Dynamics/causal beats statics/observational" hammer.** My single most-used revival move (0074, 0145, 0163, 0293, 0307) is upgrading a published observational finding to its trajectory/causal version. It is a sound heuristic in this literature, but applied five times it becomes a monoculture: if reviewers start treating "controlled rerun of a known correlation" as incremental, several of my survivors weaken together. Correlated-bet risk, not just taste.
- **PEFT-theoretical vs empirical: mildly over-theoretical, contained.** peft_limits (8) + finetune_instability (7) = 15/77 keeps, and the 0095/0098/0101/0104 mechanics family is internally correlated — one adverse result (e.g., intruder dimensions replicating strongly on vision backbones) damages four keeps at once. I partially hedged by keeping deployment-empirical PEFT ideas (0108, 0112, 0118), but a PI wanting a purely empirical portfolio should trim this family to two.
- **Anti-benchmark prejudice.** Kill taxonomy category 3 ("engineering, not science") did a lot of work — I killed dataset/benchmark proposals aggressively. Batch B's history says that is where citations live (RClicks, FeatUp are exactly such papers). My mandate is scientific-question quality, but the PI should know the portfolio is deliberately light on artifact-contribution papers.
- **Search-coverage ceiling.** 26 ideas got live adversarial search; the other 319 verdicts rest on my prior knowledge of 2023–2026 literature. Kill notes citing specific papers (MaskCLIP, LEEP/LogME, Davari) are solid; kills reasoned from "this cluster is crowded" are softer. Unpublished-likelihood scores for non-attacked ideas should be read as ±1.
- **Cheap-experiment favoritism.** CF protection rewarded decisiveness-per-dollar, which systematically favors dissociation/response-curve designs over integrative or theory-building work. 0317 (identifiability theory) nearly died to this bias before HRHR protection caught it.
- **Recency/venue bias in the attack itself.** My searches over-sample arXiv 2024–2026 and English venues. A scooping paper in a journal, a non-English venue, or pre-2020 psychology/psychophysics (relevant to 0304, 0326) could exist below my search floor.

## 4. Next information that would change my ranking

Ordered by how much of the board it would move:

1. **A frozen-random-token VPT pilot (one afternoon).** If random tokens reproduce ≥30% of VPT's gain, 0114 becomes the batch's flagship and several PEFT-mechanics keeps gain support; if 0%, 0114 drops to mid-list. Cheapest high-leverage measurement available.
2. **One arXiv hit on visual-evidence interventions for VLM CoT.** Would flip 0332 SURVIVE→KILL overnight. This is the survivor with the shortest shelf life; re-search immediately before any execution decision.
3. **A controlled matched-data language-alignment pretraining study appearing.** Kills 0307 (and weakens 0304/0323's framing) — or, if none appears in 6 months, upgrades 0307's urgency. Same watch applies to any "register norms as uncertainty" paper for 0001.
4. **Vision-backbone replication of intruder dimensions.** Shuttleworth et al. is LLM-centric; a strong vision replication reshapes the whole 0095/0098/0101/0104 family — strengthening 0104's premise while further constraining 0098's mutated boundary question.
5. **Agent D's batch-C scores.** If C's top ideas dominate B's on the same dimensions, cross-batch calibration matters more than my within-B ordering; my protected-class quotas were set batch-internally.
6. **Compute-partner reality check.** 0293 and 0307 assume pretraining-scale resources. Confirmed access moves both up; no access converts 0293 into a kill (its observational fallback is published — see 0279's fate) and forces 0307 into a smaller matched-finetuning design.
7. **Replication of ITACLIP's definition gains on more dense benchmarks.** If auxiliary-text gains are robust, 0172's mutated version narrows further; if they prove dataset-fragile, the original dissociation claim partially revives.
8. **Contamination-detector validation data.** 0268 hinges on generated-image detectors being calibratable on benchmark-like distributions; a validation study either de-risks the idea or kills its measurement basis.

## 5. Compliance notes

- All writes confined to `Windows2/_wip/stage2_agent_E/`.
- No batch-C idea was scored or re-ranked.
- No final-3 selected; top tier in `shortlist.md` is explicitly non-binding input to the PI.
- All papers cited in `prior_work_attack.md` were found via live web search during this review;
  URL-verification status is flagged per citation. No invented citations.
