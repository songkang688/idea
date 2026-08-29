# Idea_03 — RehearsalGrid: Text-Batch Rehearsal Works by Gradient Rebalancing, Not by Content

**Internal ID:** C-0090 (Cluster C)
**Window:** Windows7 · **Package written:** 2026-08-29
**Status:** Ready to start. ~2,450 A100-h — the deliberate expensive pick of the round.

> **Epistemic contract.** `KNOWN FACT` = checkable property of a public artifact. `EVIDENCE` = a
> finding reported by a cited paper. `HYPOTHESIS` / `EXPECTED` = our prediction. **No `ACTUAL
> RESULT` appears in this file.**

---

## 1. Executive Summary

**One sentence.** Interleaving text-only batches during multimodal fine-tuning prevents language
forgetting — we test whether it works because of *what the text says* or merely because it puts a
matched-scale gradient on the language pathway.

**Abstract.** The field curates rehearsal corpora on the assumption that rehearsal content matters.
We run the control nobody has run: at a fixed token budget, we progressively destroy the content of
the rehearsal stream while holding the gradient scale matched, and measure capability-stratified
language retention. Five arms — none, curated, random web, **token-shuffled**, and **one document
repeated** — dissect diversity from lexical statistics from syntax. If retention survives to the
degenerate arms, rehearsal-data curation budgets across the field are misdirected and a
gradient-balance term suffices. If it collapses, we have the first controlled refutation of the
pseudo-rehearsal account in the multimodal regime. The middle outcome is a per-capability dosing
recipe. All three change how people train.

**Why it is #3 and not lower.** It is the only project in Windows7 that changes what large labs
*do* rather than how they *measure*, and the only one whose subject is a frontier model class. It is
also the most expensive by an order of magnitude and the most likely to die on statistical power.

---

## 2. Research Motivation

Multimodal fine-tuning degrades a base LLM's language ability. The standard mitigation is to
interleave text-only batches, and the standard practice is to *curate* what goes in them. That
practice encodes an untested causal assumption: that the rehearsal text's content is what does the
work.

There is an alternative explanation that no one has ruled out. Multimodal fine-tuning shifts the
gradient distribution on the language tower; a text batch — any text batch — restores a
language-shaped gradient of the right scale. Under that account, content is irrelevant and the field
is paying for curation that a scaling coefficient would buy.

`EVIDENCE` The mechanism vocabulary now exists and points the same way. Modality gradient conflict
is formally defined (`arXiv:2512.03125`, Def. 1) `[S6-verified]`, and Pareto LoRA
(`arXiv:2606.17296`) `[S6-verified]` reports modality-specific gradients differing "by orders of
magnitude across various tasks and layers." Dynamic Gradient Guidance (`arXiv:2511.15164`,
Nov 2025) `[S6-verified]` recasts forgetting as missing-gradient approximation on LLaVA.

`EVIDENCE` And there is a live, named disagreement to arbitrate: `arXiv:2603.14493`
`[S6-verified]` argues forgetting is overstated and that the operative variable is *task diversity*,
explicitly not volume — an observational, content-side claim **with no content-free control and no
gradient matching.** Our A2/A3/A4 arms are exactly the controls that claim lacks.

Being the decisive experiment for a stated dispute is a substantially better position than testing
folklore.

---

## 3. Problem Definition

Fine-tune a base LLM `θ_0` into a VLM on a multimodal instruction mix, interleaving text-only
batches at a fixed fraction of the total token budget. Let arm `a` determine the rehearsal stream's
content, holding tokens, schedule and gradient scale fixed.

For language capability `c`, define

```
Ret(c, a) = score(c, θ_a) / score(c, θ_0)        (ratio, secondary)
Abs(c, a) = score(c, θ_a) − score(c, θ_0)        (absolute delta, CO-PRIMARY)
```

**Arms (rehearsal = 10% of total training tokens, 1 text batch per 9 multimodal batches):**

| Arm | Rehearsal stream | Destroys |
|---|---|---|
| `A0` none | — | forgetting floor |
| `A1` curated | instruction/text mix of the kind the field curates | — |
| `A2` random-web | C4 documents, no curation | curation |
| `A3` shuffled-token | the *same* C4 sample, tokens permuted within documents | syntax and content; **preserves unigram statistics and length** |
| `A4` single-doc | one fixed ~2K-token document repeated for the whole budget | diversity |

**Effects:**
```
content-effect(c) = Ret(A1) − Ret(A2)
balance-effect(c) = Ret(A2) − Ret(A0)
total-effect(c)   = Ret(A1) − Ret(A0)
```

`A3` vs `A2` separates lexical statistics from syntax. `A4` vs `A2` separates diversity from content.
These two contrasts are what keep every outcome from being a shrug.

---

## 4. Core Hypothesis

> **H1.** Rehearsal's protective effect on language capabilities is produced primarily by placing a
> matched-scale gradient on the language pathway, not by the semantic content of the rehearsal text.
>
> **H2.** The effect is capability-stratified: fluency is rescued by any text-shaped gradient, while
> knowledge-dependent capabilities require real content.
>
> **H3.** The conclusion is invariant to the gradient-matching convention. If it is not, the
> convention-dependence is itself the finding — but only under a **pre-registered primary
> convention**, so that "divergence is a finding" cannot absorb every outcome.

---

## 5. Falsifiable Prediction (pre-registered)

**P0 (power gate, evaluated first).** The `A1 − A0` gap on knowledge and fluency strata must exceed
**2× seed σ**, against a **minimum detectable effect declared before the 15 arms run**. If not, the
phenomenon is too small at this scale and the program stops for <1K A100-h.

**P1 (mechanism confirmed).** `balance-effect ≥ 0.8 × total-effect` on ≥3 of 4 language capabilities,
under the **primary per-layer matching convention**.

**P2 (content camp confirmed).** `Ret(A2) ≤ Ret(A0)` on all capabilities.

**P3 (stratified recipe).** Knowledge shows `content-effect > 50%` of total while fluency shows
`< 20%`.

**Falsification of H1** is P2. Anything between P1 and P2 lands on P3, which is the honest middle and
is published as a dosing recipe with the minimal-real-text fraction sweep.

---

## 6. Key Insight

**The degenerate arms are the contribution.** `A2` (random web) is the obvious control and would on
its own produce an ambiguous result. `A3` (token-shuffled) and `A4` (single repeated document) are
what make the experiment dissective: they destroy syntax and diversity respectively while preserving
the property that the batch is still *text-shaped gradient*. No adjacent paper runs them.

Two structural corrections, both forced at Stage 6, are what make the design interpretable at all:

1. **The base is not the published recipe.** `EVIDENCE` LLaVA-1.5's `llava_v1_5_mix665k` already
   contains a text-only ShareGPT slice (~40K conversations). So "reproduce the published recipe" and
   "A0 = no rehearsal" **cannot both hold**: A0 requires stripping ShareGPT, which is a recipe
   deviation, and A1 partially duplicates what the recipe already does natively. The base is
   therefore a **pre-registered text-stripped mix with token-budget re-matching across arms**, and
   the published-recipe run is reported as a *reference point, not an arm*. This narrows the claim's
   direct applicability and we state that narrowing rather than eliding it.

2. **Ratios with near-zero denominators are noise amplifiers.** `EVIDENCE` Vicuna-7B is near-floor on
   GSM8K and weak on IFEval. `Ret = score/score(base)` on those strata can flip the decision rule on
   noise alone, and the original abort gate watched only seed variance on A0/A1 — it never checked
   per-stratum denominator adequacy. **Absolute deltas are now co-primary with ratios**, and strata
   failing a denominator-adequacy check are replaced before the arms run, not after.

---

## 7. Novelty — exact difference from closest prior work

| Closest prior | What it actually did | Our exact difference |
|---|---|---|
| Srivastava et al., PMLR v330 / `arXiv:2410.19925` (CoLLAs) `[S6-verified]` | 5 continual-learning methods on LLaVA linguistic forgetting; rehearsal among them. **Real data only.** | No content-free controls, no gradient matching. Scaffold, not scoop: we cite it, reuse its task splits, and subsume it. |
| `arXiv:2603.14493` `[S6-verified]` | Argues forgetting is overstated; operative variable is *task diversity*, not volume. Observational. | It is a **content-side claim with no content-free control**. We are the decisive experiment for it. |
| Dynamic Gradient Guidance `arXiv:2511.15164` `[S6-verified]` | Recasts forgetting as missing-gradient approximation on LLaVA; proposes a method. | Approaches "it's optimization" from the *method* side. We test it causally with data ablation. |
| MoDE (NeurIPS 2025) / `arXiv:2512.03125` `[S6-verified]` | Formalises modality gradient conflict. | Gives us the theoretical frame for a positive result; runs no rehearsal-content experiment. |
| Robins 1995, pseudo-rehearsal `[inherited]` | Rehearsal on generated (content-free) patterns works in small nets. | Our A2–A4 arms are the multimodal, capability-stratified version. If A2 fails, this is the first controlled refutation in this regime. |

**Remaining novelty (confidence: medium-high, decaying).** `KNOWN FACT` As of the Stage-6 sweep,
**no content-free-control study exists** in this setting — A2/A3/A4 are unclaimed. But the "it's
optimization balance, not data" conclusion is being approached from the gradient-methods side, and
the residual window is plausibly months.

---

## 8. Proposed Method

### 8.1 Base and arms

Base run: LLaVA-1.5-7B (Vicuna-7B + CLIP ViT-L/336) on a **text-stripped** 665K-derived mix, 1 epoch,
published hyperparameters, via `haotian-liu/LLaVA`. Fallback harness: `TRI-ML/prismatic-vlms` (the
trainer used by the closest prior). Rehearsal is 10% of total training tokens, interleaved 1:9.

**Token-budget re-matching** across arms is explicit and logged: stripping ShareGPT removes tokens
from the base mix, so each arm's total token count is equalised before any comparison.

### 8.2 Gradient-matching conventions

- **Primary: per-layer matching** — per-transformer-block gradient-norm matching on the LLM tower.
  `EVIDENCE` Chosen as primary because per-layer disparity is documented (`arXiv:2606.17296`), so a
  global-norm match can leave individual blocks badly mismatched. Stage 5 left the two symmetric;
  Stage 6 required a single pre-registered primary so that "divergence is the finding" cannot absorb
  every outcome.
- **Secondary: global-norm matching.**

Telemetry: per-module gradient norms logged every 50 steps via hooks (~0 cost).

### 8.3 Stratified evaluation

| Stratum | Benchmarks |
|---|---|
| Fluency | WikiText perplexity, LAMBADA |
| Knowledge | MMLU, NaturalQuestions closed-book |
| Reasoning | ARC-Challenge (+ GSM8K **only if it clears the denominator gate**) |
| Instruction-following | IFEval (**denominator-gated**) |
| Vision-language (sanity, must not regress) | VQAv2, GQA, TextVQA |

Via `EleutherAI/lm-evaluation-harness` and `EvolvingLMMs-Lab/lmms-eval`. Eval YAMLs are frozen and
committed **before any arm runs**.

---

## 9. Architecture Diagram

See `diagrams/architecture.md`. Inline summary:

```
text-stripped 665K mix ──┐
                         ├─► LLaVA-1.5-7B fine-tune ──► θ_a ──► stratified eval
rehearsal stream (10%) ──┘        (1 text batch per 9 multimodal)
   A0 none                          ▲
   A1 curated                       │ gradient-norm matching
   A2 random web (C4)               │  primary: per-layer
   A3 shuffled tokens               │  secondary: global norm
   A4 single repeated doc           │
                                    └── per-module grad norms logged every 50 steps
```

---

## 10. Mathematical Formulation

**Gradient matching.** For a text batch `B_txt` at step `t`, scale its loss by `λ_t` so that the
language-tower gradient norm matches the reference arm's:

*Per-layer (primary):* for each transformer block `l`,
```
λ_t^{(l)} = ‖ ∇_{θ^{(l)}} L_ref ‖ / ( ‖ ∇_{θ^{(l)}} L_txt ‖ + ε )
```
applied as a per-block scaling of the text-batch contribution.

*Global (secondary):* one `λ_t` from the whole-tower norm ratio.

`KNOWN FACT` Scaling text losses to match reference gradient norms changes the effective learning
rate on the language tower. That is a real risk to training stability and is monitored, not assumed
away.

**Decision statistics.** For capability `c` and arm `a`, with `S` seeds:
```
Abs(c,a) = mean_s score(c, θ_{a,s}) − score(c, θ_0)         [CO-PRIMARY]
Ret(c,a) = mean_s score(c, θ_{a,s}) / score(c, θ_0)         [secondary]
σ(c,a)   = seed standard deviation
```

**P0 power gate**, evaluated on the first 6 runs, against an MDE declared in advance:
```
Abs(c,A1) − Abs(c,A0)  >  2 σ(c,A0∪A1)     for knowledge and fluency
```

**P1 mechanism rule** (only interpreted if P0 passes):
```
[Ret(c,A2) − Ret(c,A0)]  ≥  0.8 · [Ret(c,A1) − Ret(c,A0)]     on ≥3 of 4 capabilities
```
`KNOWN FACT` This is a ratio of differences and is unstable when the denominator is small — which is
exactly what `arXiv:2603.14493` predicts. **The ratio is left uninterpreted below the declared
MDE**, and the absolute-delta version is reported alongside in every case.

---

## 11. Implementation

`src/` implements the parts that can be validated without a GPU: the interleaved rehearsal sampler,
the four content-destruction transforms, both gradient-matching conventions, the token-budget
accounting, the denominator-adequacy gate, and the full decision rule with power analysis.

```
src/
  rehearsal_grid/
    __init__.py
    arms.py         # A0-A4 content-destruction transforms; A3 tokenizer-validity check
    sampler.py      # interleaved 1:9 text/multimodal sampler + token-budget accounting
    matching.py     # per-layer (primary) and global-norm (secondary) scaling
    power.py        # MDE, denominator-adequacy gate, seed-variance power analysis
    decision.py     # P0-P3 pre-registered rule, absolute deltas co-primary
  run_decision_demo.py  # exercises the whole rule on synthetic eval scores
```

### 11.1 Reusable public codebases (existence-verified Stage 5, 2026-08-28)

| Component | Repo / dataset |
|---|---|
| Training | `github.com/haotian-liu/LLaVA` (deepspeed configs shipped) |
| Training fallback | `github.com/TRI-ML/prismatic-vlms` |
| Text eval | `github.com/EleutherAI/lm-evaluation-harness` |
| VL eval | `github.com/EvolvingLMMs-Lab/lmms-eval` |
| Rehearsal corpora | `allenai/c4` (HF), ShareGPT / OpenOrca slices |
| Telemetry | torch hooks + wandb |

`KNOWN FACT` The LLaVA repo is in maintenance mode; deepspeed configs need version pinning. Known
ecosystem friction — days, not weeks.

---

## 12. Dataset Plan

| Data | Role | Licence note |
|---|---|---|
| LLaVA 665K mix, **text-stripped** | base multimodal training | ShareGPT provenance is legally murky (scraped conversations). It is in the published recipe so use is defensible by precedent; a careful group notes it. We **strip** it from the base, which incidentally reduces exposure. |
| C4 (`allenai/c4`) | A2, A3, A4 source | ODC-BY |
| ShareGPT / OpenOrca text slice | A1 curated | as above |
| Vicuna-7B | base model | LLaMA-2 community licence, research use |

No annotation, no API spend.

---

## 13. Baselines

`A0` (forgetting floor) is the baseline that matters. The **published-recipe run** is a reference
point reported once, explicitly *not* an arm, because its mix contains native text rehearsal.
Cross-family replication on `prismatic-vlms` (A0/A1/A2 × 1 seed) is promoted into the core design.

---

## 14. Metrics

Per-capability absolute deltas (co-primary) and retention ratios (secondary); seed σ; per-module
gradient norms; content-effect / balance-effect / total-effect decomposition; VL sanity scores;
training-stability traces (loss curves, effective LR on the language tower).

---

## 15. Experimental Matrix

| # | Experiment | Runs | Cost | Decides |
|---|---|---|---|---|
| E0 | Recipe reproduction + text-stripped base construction + token accounting | 1 | ~100 A100-h | harness validity |
| E0b | **A3 tokenizer-validity pilot** (1 run) | 1 | ~100 A100-h | do permuted tokens give the intended control, or degenerate attention? |
| **E1** | **Power gate: A0/A1/A2 × 2 seeds** | 6 | ~600 A100-h | **go / no-go (P0)** |
| E2 | Full grid: A0–A4 × 3 seeds | 15 (9 more) | ~900 A100-h | P1, P2, P3 |
| E3 | Second convention (global-norm) on the decision arms | 3 | ~300 A100-h | H3 |
| E4 | Mixture sweep A2/A1 at {1, 5, 10}% real × 2 seeds | 6 | ~600 A100-h | P3 dosing recipe |
| E5 | Cross-family replication (prismatic, A0/A1/A2 × 1 seed) | 3 | ~300 A100-h | generality |
| E6 | Evaluation | — | ~150 A100-h | — |

**Full program ≈2,450–3,000 A100-h** on 8×A100-80GB. `KNOWN FACT` One full LLaVA-1.5-7B fine-tune is
roughly 100 A100-h. **The program can die at E1 for under 1,000 A100-h.**

---

## 16. Ablation Plan

- Rehearsal fraction: 5% / 10% / 20% of token budget.
- Interleave granularity: 1:9 batch-level vs within-batch mixing.
- Matching convention: per-layer (primary) vs global (secondary) vs **none** (a third arm that
  isolates how much of everything is just gradient scale).
- Mixture sweep (E4): the minimal real-text fraction, per capability.
- Model scale: 13B escalation **only if** E1 shows the effect is real but underpowered at 7B.

---

## 17. Killer Experiment

> **The content-free rehearsal grid.** Five arms at fixed token budget on a text-stripped
> LLaVA-1.5-7B base, capability-stratified retention with absolute deltas co-primary, under the
> pre-registered per-layer matching convention.
>
> **Mechanism confirmed** iff `balance-effect ≥ 0.8 × total-effect` on ≥3 of 4 language capabilities
> ⇒ the field's rehearsal-curation budgets are misdirected; a gradient-balance term suffices.
> **Content camp confirmed** iff `Ret(A2) ≤ Ret(A0)` everywhere ⇒ first controlled refutation of the
> pseudo-rehearsal account in the multimodal regime.
> **Stratified recipe** otherwise ⇒ the first per-capability rehearsal dosing recipe.
>
> `A3` vs `A2` separates lexical statistics from syntax; `A4` vs `A2` separates diversity from
> content. **Decision-arm cost ≈900 A100-h after the power gate.**

**Gate before it: E1 (~600 A100-h).** A0/A1/A2 × 2 seeds with per-stratum power analysis against a
pre-declared MDE. If the `A1 − A0` gap on knowledge + fluency is below 2× seed σ, the phenomenon is
too small at this scale: stop, publish the power analysis, and reallocate.

---

## 18. Expected Results

**All `EXPECTED` / `HYPOTHESIZED`.**

| Quantity | Expected |
|---|---|
| `A1 − A0` on fluency | measurable; the stratum most likely to clear the power gate |
| `A1 − A0` on knowledge | smaller; the stratum most likely to fail it |
| balance-effect share, fluency | high — any text-shaped gradient should rescue fluency |
| balance-effect share, knowledge | low — content should matter here |
| `A3` vs `A2` | `HYPOTHESIS` the least predictable contrast, and the most informative |
| Most likely landing branch | **P3, the stratified recipe** |

`EVIDENCE` Stage 6 was explicit that the mushy middle is now the *predicted* outcome rather than a
risk, because `arXiv:2603.14493`'s diversity claim implies `A4 < A2 < A1`. We price that honestly:
P3 is the weakest headline of the three branches, and it is the one we most expect.

---

## 19. Failure Cases

- **Underpowered at 7B** — the single most likely ending. `EVIDENCE` If forgetting is largely
  avoidable through regularisation and low learning rates, the `A1 − A0` gap may be small. Ends the
  program for <1K A100-h.
- **`A3` degenerate.** Permuted tokens may produce degenerate attention rather than the intended
  unigram-preserving control. E0b pilots this with one run before three seeds are committed.
- **Matching destabilises training.** Scaling text losses changes the effective LR on the language
  tower. Monitored via loss curves and per-module norms; a stability failure is reported, not tuned
  away.
- **Base-model currency.** `KNOWN FACT` LLaVA-1.5-7B is an old base for 2026. Whether the result
  holds for a current MLLM is unknown and unaffordable here. Stated as a limitation.
- **Cost.** 2,450 A100-h is ~20× Idea_02 and ~500× Idea_01's killer. Worst cost-per-decision in the
  round.

---

## 20. Negative Results

| Outcome | What we publish |
|---|---|
| P0 fails | Power analysis + the measured effect size at this scale. Useful: it bounds how large multimodal linguistic forgetting actually is under a well-tuned recipe, which the field asserts loosely. |
| P2 (content camp) | First controlled refutation of pseudo-rehearsal in the multimodal regime, with the gradient-matched controls that make it interpretable. |
| Conventions diverge | Reported under the **pre-registered primary**, with the secondary as a stated sensitivity. `KNOWN FACT` Stage 6 flagged "divergence is the finding" as unfalsifiable-adjacent; naming the primary in advance is what stops every outcome from becoming a result. |
| P3 | Per-capability dosing recipe + minimal-real-text fraction. Weakest headline; still a training-practice change. |

---

## 21. Reviewer #2 Attack

| # | Attack | Severity |
|---|---|---|
| **A1** | *"Your control arm contradicts your premise."* LLaVA-1.5's mix already contains text-only ShareGPT, so "reproduce the published recipe" and "A0 = no rehearsal" cannot both hold. | **Fatal as originally specified** |
| **A2** | *"Two of four strata have unusable denominators."* Vicuna-7B is near-floor on GSM8K and weak on IFEval; ratios there amplify noise and can flip the ≥3-of-4 rule. | High |
| **A3** | *"'If conventions diverge, the divergence is the finding' is unfalsifiable-adjacent."* Every outcome becomes a result. | High |
| **A4** | *"The 80%-of-gap rule is a ratio of differences with a small denominator."* | High |
| **A5** | *"One model family, one scale — you cannot say 'stop paying for curation'."* | Medium |
| **A6** | *"Robins 1995 predicted this."* | Medium, framing |
| **A7** | *"This is a language-retention study in a segmentation portfolio."* (SEG's Stage-6 dissent) | Portfolio-level |
| **A8** | *"The mechanism space is being colonised in real time."* | Scoop clock |

---

## 22. Response Strategy

| # | Response | Where |
|---|---|---|
| **A1** | **Redefine the base.** Pre-registered **text-stripped mix with explicit token-budget re-matching** across arms; the published-recipe run becomes a reported *reference point*, not an arm. We also state plainly that this narrows direct applicability from "the published recipe" to "a controlled variant of it." | §3, §8.1, E0 |
| **A2** | **Absolute deltas co-primary with ratios**, plus a **denominator-adequacy gate applied before the arms run**. GSM8K and IFEval are replaced (e.g. ARC-C + a knowledge split) if the pilot shows floor effects. The original abort gate watched only seed variance; this one watches per-stratum denominators. | §6, §10, `src/rehearsal_grid/power.py` |
| **A3** | **Name a single pre-registered primary convention: per-layer.** `EVIDENCE` Justified by documented per-layer gradient disparity (`arXiv:2606.17296`). Global-norm becomes a stated sensitivity analysis. Divergence is then a *qualified* finding, not a catch-all. | §8.2, E3 |
| **A4** | **Declare the minimum detectable effect before the 15 arms**, and leave the ratio uninterpreted below it. Report the absolute-delta version in every case. | §10, E1 |
| **A5** | **Promote a 3-run cross-family replication** (prismatic-vlms, A0/A1/A2 × 1 seed) from optional into the core design. | E5 |
| **A6** | Robins is small-net pseudo-rehearsal. The multimodal, capability-stratified, gradient-matched version is the contribution — and if A2 fails, we are the first controlled refutation of that account in this regime. `KNOWN FACT` Stage 6 recorded this as a framing battle unresolvable pre-data. | §7 |
| **A7** | No experiment answers a portfolio-fit objection. Recorded honestly: this was a **deliberate diversification decision** by the Stage-6 panel, over SEG's dissent, to avoid a Final 3 composed entirely of inference-only diagnostics. | §25, Windows7 README |
| **A8** | **Start soon.** The design is 15 fine-tunes from done; the mitigation is execution, not argument. | §24 |

---

## 23. Compute Plan

`KNOWN FACT` 8×A100-80GB. One full LLaVA-1.5-7B fine-tune ≈100 A100-h (~12 h wall-clock).

| Phase | Runs | A100-h | Cumulative |
|---|---|---|---|
| E0 reproduction + stripped base | 1 | 100 | 100 |
| E0b A3 tokenizer pilot | 1 | 100 | 200 |
| **E1 power gate** | 6 | 600 | **800 ← kill point** |
| E2 remaining grid arms | 9 | 900 | 1,700 |
| E3 second convention | 3 | 300 | 2,000 |
| E5 cross-family | 3 | 300 | 2,300 |
| E6 evaluation | — | 150 | 2,450 |
| E4 mixture sweep (P3 branch only) | 6 | 600 | 3,050 |

**The program dies for under 1,000 A100-h if the phenomenon is not there.** That asymmetry is the
only thing that makes a 2,450 A100-h project responsible.

No annotation, no API spend.

---

## 24. Implementation Roadmap

**Day 1.** Clone LLaVA; pin deepspeed configs; download the 665K mix and the LLaVA-1.5 projector.
Build the **text-stripped** mix and compute token-budget re-matching for all five arms.

**Day 2–3.** Interleaved text-batch sampler (~100-line change in the LLaVA data module, following its
existing multi-source sampler pattern). Per-module gradient-norm hooks. Both matching conventions.

**Day 4–5.** Verify the published recipe reproduces LLaVA-1.5 evals within noise (E0, one run).
**Freeze the eval YAMLs, the MDE, the primary convention and the strata list — commit the
pre-registration artifact before any arm runs.**

**Week 2.** E0b `A3` tokenizer-validity pilot (1 run). Denominator-adequacy gate on all strata;
replace failing strata *now*, not later.

**Week 3.** **E1 power gate**: A0/A1/A2 × 2 seeds. Evaluate P0 against the declared MDE. **Go/no-go.**

**Week 4–6.** E2 full grid; E3 second convention; E5 cross-family replication.

**Week 7+.** E4 mixture sweep if the result lands on P3.

---

## 25. Stop / Continue Criteria

| Condition | Action |
|---|---|
| E0 cannot reproduce LLaVA-1.5 within noise | **stop**; the harness is not trustworthy |
| `A3` produces degenerate attention (E0b) | drop `A3`, report why; `A4` still separates diversity |
| **P0 fails at E1** | **stop for <1K A100-h.** Publish the power analysis. Do **not** escalate to 13B unless the effect is real-but-underpowered rather than absent. |
| P0 passes | run the full grid |
| Conventions diverge | report under the pre-registered primary; secondary as sensitivity |
| Lands on P3 | fund E4 mixture sweep — without it, P3 is a shrug with a table |
| Scooped | the content-free grid is unclaimed as of Stage 6; if that changes mid-flight, pivot to the cross-family replication and the power analysis |

`EVIDENCE` Stage 6 recorded an open portfolio-level disagreement: whether 2,450 A100-h here beats the
same budget on C-0028's decision triple. If the group holds only one node, that fight reopens.

---

## 26. Possible Extensions

- **The gradient-balance term itself.** If P1 lands, replace the rehearsal corpus with an explicit
  regulariser and show it matches — turning a measurement into a method, and deleting a recurring
  data-curation cost line.
- **Current-generation base model** — the honest limitation in §19 is also the obvious follow-up.
- **Other modalities.** Audio-language and video-language fine-tuning have the same folklore.
- **Cross-link to Idea_02.** Both projects ask whether an intervention's *content* or its *mechanical
  side effects* do the work, and both answer it with a vacuous control arm. The design pattern
  transfers.

---

## 27. Paper Story

> Everyone curates rehearsal data to stop multimodal fine-tuning from damaging a model's language
> ability. We destroyed the data and kept the gradient. At a fixed token budget and matched per-layer
> gradient norms, we replace curated rehearsal text with random web text, then with the same text
> token-shuffled, then with a single document repeated thousands of times — and measure which
> language capabilities notice. [`EXPECTED`: fluency does not; knowledge does.] The consequence is a
> per-capability answer to a question the field has been answering with a budget line.

---

## 28. Candidate Titles

1. *Rehearsal Without Content: Is Text-Batch Rehearsal Gradient Rebalancing in Disguise?*
2. *What Does Rehearsal Data Actually Do? A Content-Free Grid for Multimodal Fine-Tuning*
3. *Shuffled, Repeated, Random: Destroying Rehearsal Content at Matched Gradient Scale*
4. *Capability-Stratified Rehearsal: Which Language Abilities Need Real Text?*
5. *You Are Paying for Curation You May Not Need*

---

## Provenance

Windows7 Stage 1–6 artifacts on `songkang688/idea`: `cursor/stage1-cluster-c-ideas-8c7f` →
`cursor/stage2-cluster-c-scoring-70d5` → `cursor/stage3-cluster-c-priorwork-f96e` →
`cursor/stage4-cluster-c-reviewer2-c1be` → `cursor/stage5-cluster-c-engineering-2eff` →
`cursor/stage6-attack-pass-top5-cca8` / `cursor/stage6-defense-top5-2995` /
`cursor/stage6-meta-review-final3-4fc5`.

Stage-6 mandatory conditions — text-stripped base with token re-matching (A1), per-stratum
denominator gates with absolute deltas co-primary (A2), a single pre-registered primary convention
(A3), a declared MDE before the arms (A4), and a funded cross-family replication (A5) — are folded
into §3, §6, §8, §10 and §15 rather than appended.
