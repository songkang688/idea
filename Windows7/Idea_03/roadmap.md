# Idea_03 — Implementation Roadmap

15 fine-tunes, no novel modelling. The engineering is small; the discipline is the whole project.

**Sequence third**, but start the pre-registration early — five of the eight reviewer attacks are
answered by things committed before any arm runs.

---

## Day 1 — environment

- [ ] Clone `haotian-liu/LLaVA`; **pin deepspeed and transformers versions** (`KNOWN FACT` the repo
      is in maintenance mode; this is known ecosystem friction, days not weeks).
- [ ] Download `llava_v1_5_mix665k`, the LLaVA-1.5 projector, Vicuna-7B.
- [ ] Clone `TRI-ML/prismatic-vlms` (fallback harness + E5).
- [ ] Clone `lm-evaluation-harness` and `lmms-eval`; pin task versions.
- [ ] Confirm 8×A100-80GB allocation and queue policy.

## Day 2–3 — the harness changes

- [ ] **Text-stripped mix**: remove the ShareGPT slice, measure its exact token count.
- [ ] **Token-budget re-matching** across all five arms (`sampler.py` port).
- [ ] Interleaved text-batch sampler — ~100 lines in the LLaVA data module, following its existing
      multi-source sampler pattern.
- [ ] Per-module gradient-norm hooks, logged every 50 steps.
- [ ] Both matching conventions; log the effective-LR multiplier on the language tower every step.

## Day 4–5 — E0 and the freeze

- [ ] Reproduce the published recipe; verify evals within noise.
- [ ] Full stratified eval of the **base model** — this fixes every denominator.
- [ ] **Freeze `configs/preregistration.yaml`**: MDE, strata list, primary convention, eval YAMLs.
      Commit it. Everything after this reads the file; nothing rewrites it.

## Week 2 — pilots and gates

- [ ] E0b `A3` tokenizer-validity pilot (1 run). Degenerate ⇒ drop `A3` and record why.
- [ ] Denominator-adequacy gate on all strata. Replace failures **now**.

## Week 3 — the kill point

- [ ] **E1**: `A0`/`A1`/`A2` × 2 seeds (~600 A100-h).
- [ ] Evaluate P0 against the declared MDE.
- [ ] **Go / no-go.** Fail ⇒ stop at ~800 cumulative A100-h and write the power analysis.

## Week 4–6 — the grid

- [ ] E2 remaining 9 runs under the primary convention.
- [ ] E3 second convention on the decision arms.
- [ ] E5 cross-family replication.
- [ ] E6 evaluation sweep; confirm VL sanity scores have not regressed.

## Week 7+ — only if the result lands on P3

- [ ] E4 mixture sweep at {1, 5, 10}% real text. Without it, P3 is a shrug with a table.

---

## Gate summary

| Gate | When | Fail action |
|---|---|---|
| Reproduction within noise | E0 | stop — harness untrustworthy |
| `A3` non-degenerate | E0b | drop `A3`; `A4` still separates diversity |
| Denominator adequacy | E0 | replace the stratum before the arms |
| **P0 power** | **E1** | **stop at ~800 A100-h; publish the power analysis** |
| VL sanity | E6 | a language gain bought with vision damage is a trade, not a result |

---

## Standing discipline

1. **Nothing is decided after the fact.** MDE, strata, primary convention and eval configs are
   committed before the arms. This is what makes the ≥3-of-4 rule mean something.
2. **Absolute deltas are always reported**, whether or not the ratio is interpretable.
3. **Every branch has a paper**, including the one where the phenomenon is too small to study — but
   only if the power analysis was pre-specified, which is why it is written at E0 and not at E1.
