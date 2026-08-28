# P1 Wave B - batch_002 Judge B (permutation-kill / feasibility)

- **task_id:** `p1_wave_b_batch002_judge_B`
- **windows:** Windows15 (locked; wrote only inside `Windows15/_state/tasks/p1/batch_002/judge_B/`; no canonical files touched)
- **inputs (fetched, read-only):**
  - `origin/cursor/p1-wave-a-batch002-gen-a-83d7` -> `gen_A/ideas.jsonl` (100 ideas, T04 object detection)
  - `origin/cursor/p1-wave-a-batch002-gen-b-0edc` -> `gen_B/ideas.jsonl` (100 ideas, T05 VLM / dense prediction)
  - `origin/cursor/p1-wave-a-batch002-gen-c-86e2` -> `gen_C/ideas.jsonl` (100 ideas, T06 failure mining)
- **outputs:** `verdict.jsonl` (300 rows, one per idea), this report, `done.json`
- **citation policy:** no citations are asserted anywhere in this review. Where prior-art risk drove a verdict, it is stated as reviewer knowledge of an established technique family, hedged accordingly, with no specific papers, venues, or numbers invented.

## Verdict summary

| | gen_A (T04) | gen_B (T05) | gen_C (T06) | total |
|---|---|---|---|---|
| keep | 91 | 95 | 100 | **286** |
| mutate | 8 | 4 | 0 | **12** |
| drop | 1 | 1 | 0 | **2** |
| permutation-flagged | 8 | 6 | 0 | **14** |

| feasibility | gen_A | gen_B | gen_C | total |
|---|---|---|---|---|
| cheap (inference/analysis-only, incl. small single-annotator audits) | 77 | 81 | 89 | **247** |
| medium (short/small training runs, multi-annotator or multi-day curation, corpus-index work) | 23 | 19 | 11 | **53** |
| expensive | 0 | 0 | 0 | **0** |
| infeasible | 0 | 0 | 0 | **0** |

Falsifiable: **300 / 300 true**. Verified mechanically that every entry carries a non-empty
`falsifiable_prediction`; verified by reading that each states a concrete observable outcome
(a correlation sign, a curve shape, a stratified gap, a bimodality test, etc.) rather than an
unfalsifiable aspiration. One entry (A-073) is falsifiable only after mutation narrows its
contested "downstream utility" arbitration to the crisp rank-divergence core; it is marked
`falsifiable: true` with that condition recorded in its verdict row.

## Why the kill rate is low (and why that is the honest verdict)

All three generator briefs explicitly banned backbone-swap / "architecture X + module Y" ideas,
and the shards largely comply: the dominant idea form is a mechanism, failure-law, or
measurement-blind-spot hypothesis with a named cheap falsification path. A keyword audit
(SAM+, LoRA, adapter, module, plug/bolt, combine-with, new-loss patterns) over all 300
one-liners produced only two surface hits, both benign on inspection (B-004 argues layer
selection *dominates* adapter design; B-080 uses LoRA as a measuring instrument for an
intrinsic-dimensionality claim). The 14 flags below came from manual review of full records,
not keyword matching: they are entries whose *payload* is a method tweak dressed as a
hypothesis. Judge B's mandate is to kill permutations, not to hit a quota; gen_C in
particular contains no method-graft proposals at all.

## Drops (2)

- **W15-B002-A-012** - pattern: `adaptive-threshold+NMS`. Density-adaptive NMS thresholds for
  crowded scenes are an established engineering direction; the "pre-NMS density is a sufficient
  statistic" reframing does not clear the novelty burden, and the deliverable is a
  threshold-scheduling tweak. Classic threshold+X permutation.
- **W15-B002-B-079** - pattern: `known-technique+task (weight interpolation + dense finetuning)`.
  Weight-space interpolation between a pretrained CLIP-family model and its finetune to trade
  zero-shot breadth against target accuracy is an established robust-finetuning technique;
  porting it to dense finetuning is a technique-task permutation, and the
  Pareto-dominance-over-joint-training comparison does not rescue novelty. The shard's own
  `main_risk` concedes the method breaks once decoders are added.

## Mutations (12) - directive per idea

gen_A (8):

- **A-007** (flag: EMA+assignment): lead with the instrumentation-only churn-to-gradient-interference
  measurement; EMA-smoothed assignment becomes one validation arm.
- **A-010** (flag: training-trick+X): reframe around the curriculum claim (cost-based assignment
  enacts easy-object-first ordering suppressing rare-class AP); the randomized warmup is one arm.
- **A-018** (flag: modified-overlap+NMS): measurement-first (shape-conditioned suppression bias from
  anisotropic IoU decay); any fix claim needs a prior-art sweep of shape-aware NMS variants.
- **A-035** (flag: multi-resolution routing): keep "class-conditional resolution-AP optima diverge
  and are predictable from size statistics"; drop the selection system as the contribution.
- **A-047** (flag: loss-schedule+X): must beat the trivial null - temperature scaling already
  re-anchors final-layer scaling post hoc; surviving claim is advantage over post-hoc
  recalibration under shift, else the idea is dominated.
- **A-051** (flag: head-only retune trick): the idea is the measurable head/backbone convergence
  mismatch under assignment non-stationarity, not the retuning recipe (which resembles decoupled
  classifier-retraining practice).
- **A-073** (no flag): strip the contested downstream-utility arbitration (conceded in
  `main_risk`); keep the crisp core - rankings materially diverge between class-equal and
  instance-weighted AP, driven by rare-class score arbitrage.
- **A-098** (flag: router+detector): keep oracle-headroom + difficulty-predictability measurement,
  which dies cheaply on a null; cut the router deliverable (standard dynamic-resolution engineering).

gen_B (4):

- **B-044** (flag: module-mash): keep the spectral-deficit measurement and cost-matched
  boundary-vs-resolution comparison; the injected high-frequency pathway is a validation
  instrument, not the contribution.
- **B-081** (flag: distillation bake-off): name the mechanism (which alignment structure finetuning
  damages and distillation preserves) and pre-register the matched-compute protocol; otherwise it
  is a permutation comparison with delicate bookkeeping (conceded in `main_risk`).
- **B-083** (flag: norm-adaptation+X): normalization-statistic adaptation under shift is an
  established technique and `main_risk` concedes LayerNorm has no swap-able batch statistics;
  narrow to the quantitative recovery-fraction-vs-activation-divergence law on architectures
  where recomputation is well-defined.
- **B-098** (flag: module fix): lead with the correction-turn statelessness measurement (repeat
  rate under "no, the other one"); the exclusion-memory fix is the expected trivial intervention.

## Keeps carrying a flag or caution

- **B-080** (kept, flagged `LoRA-as-instrument`): surface form is LoRA+X, but the payload is a
  falsifiable intrinsic-dimensionality claim (dense updates saturate at qualitatively higher rank,
  boundary-first degradation). LoRA is the instrument, not the novelty.
- **A-092** (kept, no flag, caution recorded): the flicker decomposition claim is the idea; the
  score-smoothing fix overlaps established temporal post-processing practice and should not be
  presented as the contribution.

## Feasibility notes

- Rubric: **cheap** = inference/analysis on public checkpoints and existing predictions, small
  synthetic/composite sets, single-annotator audits up to a few hundred judgments; **medium** =
  anything needing training (even short single-GPU runs), multi-annotator campaigns, multi-day
  curation, or corpus-index work (e.g., C-025 needs a LAION-scale nearest-neighbor index -
  public indexes make this medium, not expensive); **expensive/infeasible** = none found. No
  idea requires closed data, closed models, or unmeasurable quantities on its stated fastest path.
- Boundary judgment calls recorded in `verdict.jsonl`: C-095's *full* Goodhart-drift law
  (multi-year model panel + continually refreshed wild captures) trends expensive, but its stated
  minimal falsification (fresh never-online photo set vs one saturated benchmark) is medium, and
  feasibility is graded on the fastest stated path.
- Feasibility distribution is a strength of this batch: 82% of ideas are first-pass falsifiable
  without any training.

## Notes for the consolidator (`p1_wave_b_batch002_consolidator`)

- Dedup (Judge A territory, cross-referenced here, no verdicts changed on these grounds):
  watch A-077 / A-082 / A-084 vs C-057 (context reliance), A-016 vs B-027 (vocabulary-scaled
  false positives / suppression), A-032 / A-037 vs C-001 / C-002 (grid-phase and patch-quantization
  effects), B-042 vs C-008 (token merging damage), B-025 vs B-067 (absence handling), A-093 vs
  C-037 (score-localization decoupling), B-038 vs C-004 (positional-embedding interpolation).
- The 12 mutate rows contain concrete rewrite directives in their `reason` fields; mutated forms
  remain cheap or medium.
- Novelty fields across all shards remain unverified hypotheses per generator contract; nothing
  in this review verifies novelty, and the two drops rest on reviewer-known established technique
  families, stated without invented citations.
