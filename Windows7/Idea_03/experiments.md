# Idea_03 — Experimental Plan

`KNOWN FACT` 8×A100-80GB. One full LLaVA-1.5-7B fine-tune ≈100 A100-h (~12 h wall-clock).
No annotation cost, no API spend.

**The program is designed to die cheaply.** Everything before E2 exists to find out whether the
phenomenon is large enough to study at this scale, for under 1,000 A100-h.

---

## E0 — Reproduction and base construction (1 run, ~100 A100-h)

- Reproduce LLaVA-1.5-7B with published hyperparameters; verify evals land within noise of the
  reported model.
- **Measure the ShareGPT slice's exact token count.** It sets every arm's budget, so it is measured,
  not estimated.
- Build the **text-stripped** mix and compute token-budget re-matching for all five arms.
- Run the base model through the full stratified eval to fix every denominator.

**Gate:** cannot reproduce within noise ⇒ stop; the harness is not trustworthy and no arm difference
would mean anything.

**Then freeze `configs/preregistration.yaml`:** MDE, strata list, primary matching convention, eval
YAMLs. Committed before any arm runs.

---

## E0b — `A3` tokenizer-validity pilot (1 run, ~100 A100-h)

Does a token-permuted stream produce the intended unigram-preserving control, or degenerate
attention and a useless gradient?

Diagnostics: language-tower gradient norms vs `A2`, attention-entropy traces, loss-curve shape.

**Gate:** degenerate ⇒ drop `A3`, report why. `A4` still separates diversity from content, so the
design survives the loss of one arm.

Running this before committing three seeds to `A3` is the cheapest 100 A100-h in the plan.

---

## E1 — Power gate (6 runs, ~600 A100-h) — **THE KILL POINT**

`A0`, `A1`, `A2` × 2 seeds. Full stratified eval.

**Denominator-adequacy gate** on every stratum: headroom over chance ≥ 0.10 and headroom/seed-σ ≥ 3.
`EVIDENCE` Vicuna-7B is near-floor on GSM8K and weak on IFEval; strata that fail are **replaced
now**, not explained away later.

**P0**, on absolute deltas, against the MDE declared at E0:
```
Abs(c, A1) − Abs(c, A0) > max(2 σ_seed, MDE)     for knowledge and fluency
```

**Fail ⇒ stop at ~800 cumulative A100-h.** Publish the power analysis: it bounds how large
multimodal linguistic forgetting actually is under a well-tuned recipe, which the field currently
asserts loosely. Do **not** escalate to 13B unless the effect looks real-but-underpowered rather than
absent.

---

## E2 — The full grid (9 further runs, ~900 A100-h)

`A0`–`A4` × 3 seeds under the **primary per-layer** convention. This is the killer experiment.

| Contrast | Separates |
|---|---|
| `A1 − A0` | total effect |
| `A2 − A0` | balance effect |
| `A1 − A2` | content effect |
| `A3` vs `A2` | lexical statistics from syntax |
| `A4` vs `A2` | diversity from content |

Decision: **P1** `balance ≥ 0.8 × total` on ≥3 of 4 capabilities · **P2** `Ret(A2) ≤ Ret(A0)`
everywhere · **P3** knowledge `content-share > 0.5` while fluency `< 0.2`.

Shares are reported with bootstrap CIs over seeds and are left **uninterpreted** for any capability
whose total effect is below the MDE.

---

## E3 — Second convention (3 runs, ~300 A100-h)

Decision arms re-run under global-norm matching. H3: does the conclusion survive the convention?

Reported as a **sensitivity analysis** under the pre-registered primary. `KNOWN FACT` Stage 6 flagged
"if they diverge, the divergence is the finding" as unfalsifiable-adjacent; naming the primary in
advance is what prevents every outcome from becoming a result.

---

## E4 — Mixture sweep (6 runs, ~600 A100-h) — **P3 branch only**

`A2`/`A1` mixtures at {1%, 5%, 10%} real text × 2 seeds. Produces the minimal real-text fraction per
capability.

Without this, P3 is a shrug with a table attached. It is funded only if the result lands there, which
is also the outcome we most expect.

---

## E5 — Cross-family replication (3 runs, ~300 A100-h)

`A0`/`A1`/`A2` × 1 seed on `TRI-ML/prismatic-vlms`.

Promoted from optional into the core design at Stage 6: a single-family result cannot support "stop
paying for curation." Three runs is the cheapest available answer to that attack.

---

## E6 — Evaluation (~150 A100-h)

All checkpoints × all strata × VL sanity. Frozen YAMLs. VL scores must not regress — a rehearsal
recipe that protects language by damaging vision is not a result, it is a trade we did not measure.

---

## Ablations

- Rehearsal fraction: 5% / 10% / 20% of token budget.
- Interleave granularity: 1:9 batch-level vs within-batch mixing.
- Matching convention: per-layer / global / **none** — the third isolates how much of everything is
  just gradient scale.
- Model scale: 13B **only** on the real-but-underpowered branch.

---

## Budget

| Phase | Runs | A100-h | Cumulative |
|---|---|---|---|
| E0 | 1 | 100 | 100 |
| E0b | 1 | 100 | 200 |
| **E1 gate** | 6 | 600 | **800** |
| E2 | 9 | 900 | 1,700 |
| E3 | 3 | 300 | 2,000 |
| E5 | 3 | 300 | 2,300 |
| E6 | — | 150 | 2,450 |
| E4 (P3 only) | 6 | 600 | 3,050 |

---

## Decision summary

```
E0 reproduce ──fail──> stop (harness)
   │pass
E0b A3 pilot ──degenerate──> drop A3, continue with A2/A4
   │ok
E1 power gate ──P0 fail──> STOP at ~800 A100-h, publish power analysis
   │pass
E2 full grid ──> P1 mechanism | P2 content | P3 stratified
   │
E3 convention sensitivity · E5 cross-family · E4 dosing (P3 only)
```
