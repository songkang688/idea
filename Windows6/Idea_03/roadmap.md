# Idea_03 — Roadmap

All budgets are **HYPOTHESIS** (estimates from
`selection_history/evolution_summary.md` and `experiments.md`). None is a
measured runtime. **No VLM has been run**; `Windows6/README.md` records *"no VLM
eval"*.

Ordering principle: **the clock is the constraint.** Unlike Idea_01 and Idea_02,
Idea_03's dominant risk is not cost or feasibility — it is that the gap closes
while we work. The novelty is defined by an absence at confidence ~0.5, and
`README.md` marks this the highest concurrent-work risk in Windows6. Everything
below is arranged to reach a defensible result quickly, not to minimise compute.

> **Scheduling note that cuts across the whole round.** `Windows6/README.md`
> ranks Idea_01 as *"#1 start here"* on tractability, and that ranking is right
> for tractability. But **GATE-B and E1 here should not wait for Idea_01 to
> finish.** They are cheap, they are eval-only, and their value decays. Running
> Idea_03's gate check in parallel with Idea_01's Phase 0 costs almost nothing.

## Phase 0 — GATE-B: checkpoint pair verification (no GPU, hours) — **BLOCKING**

| | |
|---|---|
| **Work** | Card E-B. For each candidate pair, confirm from configs and model cards: (1) shared vision encoder weights, (2) shared coordinate tokenization, (3) licences permit the comparison |
| **Cost** | Hours of reading. **No GPU** |
| **Status** | **NOT RUN. This is GATE-B from `stage6_battle.md` §5, and it is why the Final 3 remain PROVISIONAL** |
| **Branch** | All three hold → Phase 1 · encoder or tokenization differs → **descope** to a format-artifact study and re-argue the Final-3 slot · licences block → find another pair |

**There is no downstream mitigation for failing this gate.** An unmatched pair
turns the whole study into a tokenizer comparison, and no amount of careful
evaluation repairs it.

## Phase 1 — Harness validation (CPU, done in this package)

| | |
|---|---|
| **Work** | Card E0. `python Idea_03/src/run_smoke.py`, `python -m unittest discover -s Idea_03/tests` |
| **Cost** | CPU seconds |
| **Exit** | All four planted degradation modes round-trip through `classify_outcome`, and 27 self-checks pass |
| **Status** | **DONE.** The decision function recovers `none` / `format` / `policy` / `representation` from measurements alone, and refuses to return a verdict when the likelihood mode is missing |

## Phase 2 — Bring-up (first GPU session)

| | |
|---|---|
| **Work** | Load the verified pair; implement the three eval modes against it; build and **freeze** the shared distractor sets; fix the prompt templates |
| **Cost** | ≈1 GPU-h (**HYPOTHESIS**) |
| **Exit** | Both checkpoints produce parseable output under constrained decoding on a 50-example subset, and the shared distractor sets are identical across arms |

## Phase 3 — E1 killer (H1 + H2)

| | |
|---|---|
| **Work** | Card E1: pair 1, ~2k referring expressions, three eval modes, frozen-feature probe. Report parse-failure rate as its own number |
| **Cost** | ≤8 GPU-h (**HYPOTHESIS**). Eval-only, no training |
| **Kill if** | No gap survives constrained decoding — formatting confound, pre-registered |
| **Provisional O1 if** | Likelihood gap ≈ 0 → confirm on pair 2, then write the negative |
| **Continue if** | Likelihood gap survives → O2 (probe intact) or O3 (probe drops) |
| **No verdict if** | The likelihood mode was skipped. The code raises |

**This is the decision point.** ≤8 GPU-h to a defensible three-way answer is why
this idea survived Stage 4 despite the scoop risk.

## Phase 4 — E2 replication ‖ E3 probe robustness

Parallel. E3 needs no second checkpoint pair and is cheap.

| Card | Work | Cost (**HYPOTHESIS**) | Branch |
|---|---|---|---|
| **E2** | Repeat E1 on a second GATE-B-verified pair | ≤8 GPU-h | same outcome on both → continue · **likelihood gap ≈ 0 on both → STOP, write O1** · outcome reverses → **kill the general claim**, report pair-specific |
| **E3** | Probe layer sweep + linear-vs-MLP capacity ablation | ≈2 GPU-h | consistent across layers → H2 robust · one layer only → **downgrade** to a sweep report · linear drops but MLP does not → *"present but not linearly accessible"*, a distinct finding |

## Phase 5 — E4 text-only DPO (H3) — **double-gated**

| | |
|---|---|
| **Work** | Small LoRA DPO on the base checkpoint using **text-only** preference data, then re-run E1's modes and probe |
| **Cost** | 1–2 × 24 GB GPUs, days (**HYPOTHESIS**). By far the most expensive card |
| **Unlock condition** | The observational gap survived format control on **both** pairs. FACT, verbatim: *"Do not run DPO unless observational gap survives format control."* |
| **Branch** | Gap reproduces → the **objective** is implicated, causal claim available · no effect → report it and **drop the causal framing**; H1+H2 stand alone · tiny effect → report the effect size, do not upgrade it |

Without E4, `proposal.md` §23 forbids the causal claim entirely. That is a
constraint on what may be written, not a reason to run E4 prematurely.

## Phase 6 — Paper & release

Analysis paper. Release the eval harness, the prompt templates, the shared
distractor sets, the probe code, per-example scores, and — most importantly —
the **pre-registered `classify_outcome` decision function**, so a reader can
apply our rule to their own numbers.

**Immediately before writing:** re-check MDGD, TWIST & SCOUT and
arXiv 2602.12506 for updates. The last is recent enough that a v2 could contain
this result.

**Candidate titles.** *Which Stage Costs the Box?* · *Format-Controlled
Localization Tax in Aligned VLMs* · *The Box Is Still There: Probing
Localization After Alignment*

## Budget summary

| Path | Total (**HYPOTHESIS**) |
|---|---|
| Descope at GATE-B | **0 GPU-h** |
| Kill at E1 | ≈9 GPU-h |
| Through E2 + E3 | ≈19 GPU-h |
| With the DPO arm | +1–2 × 24 GB for days |

Day-1 is ≈8 GPU-h, the figure recorded in `evolution_summary.md` — an estimate,
not a measurement. Eval-only was originally recorded as *"1 GPU, 1–2 days"*.

## Standing rules

1. **GATE-B before any GPU.**
2. **Speed matters more here than compute.** Do not queue this behind Idea_01.
3. Always run all three eval modes; the verdict function refuses without mode 3.
4. Distractors shared between checkpoints; freeze them before Phase 3.
5. Parse-failure rate is always its own number.
6. No causal claim without E4.
7. Re-check the adjacent literature immediately before writing.
8. Budgets stay labelled **HYPOTHESIS** wherever quoted.

## Dependency graph

```
Phase 0 (GATE-B, no GPU)  --encoder/tokenizer differ--> DESCOPE to format study
   |verified pair
Phase 1 (E0 harness, CPU, DONE)
   |
Phase 2 (bring-up; freeze shared distractors + templates)
   |
Phase 3 (E1 killer) --no gap under constrained decoding--> KILL
   |                 --likelihood gap ~0--> provisional O1
   |gap survives
   +----------------+
   |                |
Phase 4a (E2 pair 2)  Phase 4b (E3 probe sweep)   <-- parallel
   |                |
   |  E2: gap ~0 on both pairs --> STOP, write O1 as a negative
   |      outcome reverses     --> KILL the general claim
   +--------+-------+
            |gap replicates
      Phase 5 (E4 text-only DPO)  <-- unlocked only here
            |
      Phase 6 (paper + release the decision function)
```
