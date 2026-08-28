# P1 Wave 2 — Judge B supplemental pass: worker_C only — Windows14

- **Task:** `p1_wave2_judge_B_worker_C`
- **Role:** `judge_B_permutation_filter` (supplemental shard; independent of Judge A and Judge C, whose verdicts were not consulted)
- **Status:** complete
- **Judged at (UTC):** 2026-08-28T20:55Z

## Scope and inputs (read-only)

| Shard | Branch | Ideas |
|---|---|---|
| `worker_C.ideas.jsonl` (negative results / contrarian / anti-scaling) | `origin/cursor/windows14-p1-wave2-worker-c-9388` | 130 |

This pass covers ONLY worker_C, which the first Judge B pass
(`origin/cursor/windows14-p1-wave2-judge-b-cfb9`, shards A/B/D/E, 508 ideas) did not judge.
The prior pass's `judge_B.flags.jsonl` was read only to confirm ID-space disjointness:
it contains no `w14w2c-*` ids, so there is no coverage overlap and nothing here duplicates
or overwrites the prior three judge_B files. No canonical ledgers touched
(`ideas_master.jsonl`, `research_state.json`, `research_ledger.md`, `window.lock.json`
untouched, per lock). No worker, judge_A, or judge_C files modified.

## Filter mandate and rubric (same protocol as wave1/wave2 judge_B)

Flag ideas that are, at the hypothesis level:

1. **Mere architecture permutations** — swap/rearrange modules or capacity with no mechanism claim.
2. **Module A+B pairings** — bolt module B onto system A where the pairing itself is the contribution.
3. **SAM + loss/backbone swaps** — generalized to any backbone/head/loss swap as the deliverable.
4. **Mechanical transfers** — mechanical port of a known method or known finding into the territory with no territory-specific mechanism.
5. **Parameter-only scaling** — rank/size/hyperparameter sweeps without a mechanism.

Verdicts: **keep** (falsifiable mechanism/behavior claim; method elements are the test
instrument), **mutate** (real hypothesis buried in a permutation-shaped idea; flags file
specifies the salvage), **kill** (the pairing/swap is the whole idea and the insight is
already carried elsewhere).

## Verdict counts

| Shard | keep | mutate | kill | total |
|---|---|---|---|---|
| worker_C (negative/contrarian) | 128 | 2 | 0 | 130 |

The very low mutate rate is consistent with wave2 shards A/B/D/E (508 reviewed, 5 mutate,
0 kill) and is a structural property of the territory: non-replication audits,
confound decompositions, anti-scaling laws, and measurement-validity claims are
hypothesis-first by construction. Where these ideas use head swaps, recipe transplants,
ablations, or matched-budget bake-offs (e.g. w14w2c-012, -013, -077, -079, -114), the swap
is the test instrument for an attribution or equivalence claim, not the contribution —
exactly the keep condition of the rubric. Zero kills: for both mutates the buried
hypothesis is not carried by any other idea in the shard.

## Mutates (2)

- **w14w2c-059** (`data_quantity_myths`) — dense-specific dataset pruning. Importance-scoring
  for dataset pruning is an established classification methodology (record concedes); as
  framed the headline is a new boundary-entropy score winning a two-score pruning bake-off.
  Salvage: the mis-ranking law is the deliverable — measure directly how
  classification-derived importance scores fail to predict measured dense value and what
  drives dense data value (boundary-configuration diversity vs class difficulty); the new
  score becomes the confirmatory exploit.
- **w14w2c-062** (`data_quantity_myths`) — balancing-unit comparison. As framed the
  deliverable is a three-way sampling-recipe bake-off with an established
  online-hard-mining-style method as the headline winner; the unit-mismatch mechanism is
  asserted but only indirectly measured. Salvage: the balancing-unit law is the primary
  claim — which unit of supervision mass (pixels, instances, images) predicts per-class
  learning outcomes, measured via per-class supervision-mass vs IoU curves and
  loss/gradient-mass accounting; the scheme ranking becomes the confirmatory exploit.

## Keep-with-note (9)

Kept, with a mandatory framing/control recorded in the flags file (common thread: a
conceded known finding, known protocol, or bake-off-shaped instrument is present, and a
specific dense-native delta keeps the idea hypothesis-first):

- **w14w2c-005** — emergence-as-metric-artifact: language-side account is conceded prior work; the dense thresholded-metric geometry and which dense abilities remain genuinely discontinuous must lead.
- **w14w2c-006** — specialists vs generalist: the cross-domain interference mechanism must be measured inside the generalist; domain splits pre-registered; else a capacity bake-off.
- **w14w2c-010** — small-ensemble OOD reversal: per-member error-decorrelation (ID vs OOD) must be measured; output-space alignment audited.
- **w14w2c-034** — adaptive-attack re-evaluation: the dense-aware attack mechanisms (gradient dilution over summed per-pixel losses) are the contribution; released checkpoints only.
- **w14w2c-037** — epsilon-budget artifact: the sweep must test the dense-sensitivity calibration mechanism (incl. spatially-weighted budgets) and address operational relevance; else a hyperparameter sweep.
- **w14w2c-050** — DRO amplifies group label noise: dense-specific (boundary-structured, group-conditional mask quality) noise characterization plus a natural-noise arm are mandatory.
- **w14w2c-058** — dedup effective corpus size: dense-vs-classification decoupling on identical checkpoints and multi-threshold dedup are mandatory; else an LM-dedup port.
- **w14w2c-084** — half-resolution + guided upsampling: the upsampler must be off-the-shelf and the content-stratified saturation map must lead; else a module pairing.
- **w14w2c-092** — streaming evaluation for segmentation: detection-side streaming evaluation is conceded prior work; mask-staleness geometry and granularity/latency interaction must lead.

## Notes for the consolidator (dedup NOT done here — out of judge_B scope)

1. **Negation family:** w14w2c-120 overlaps the family the first judge_B pass already
   flagged (wave2 w14E-029/w14E-036; wave1 w14_p1b_122 / w14p1c-092). w14w2c-120 adds a
   distinct scale-invariance + targeted-fine-tune-beats-scale framing; merge into that family.
2. **Wave-3 overlap (self-flagged):** w14w2c-122 (agent pipelines vs end-to-end) belongs to
   the LLM/agent territory scheduled for wave 3; deduplicate against wave-3 shards.
3. **worker_A adjacency (self-flagged in records):** w14w2c-022 (domain generalization vs
   strong augmentation), w14w2c-055 (synthetic minority rebalancing backfire), w14w2c-096
   (shifted unlabeled pools) border wave2 worker_A's synthetic/shift territory but are
   framed as non-replication/backfire claims; check against worker_A entries at merge time.
4. **Wave-1 worker_B medical adjacency (self-flagged):** w14w2c-054 (scanner confounds),
   w14w2c-074 (elastic deformation relic) use medical substrates; framed as measurement or
   non-replication claims, not segmentation methods.
5. **Leakage/contamination family:** w14w2c-064 (session-split leakage), w14w2c-103
   (unlabeled-pool-to-test leakage), w14w2c-110 (pretraining-crawl contamination of
   zero-shot evaluations) are distinct channels of the contamination/leakage families the
   first judge_B pass flagged in shards A/B (w14w2a-008/-112, w14w2b-077/084/085/086/115);
   cross-link, do not collapse — the channels differ.
6. **TTA family (within shard):** w14w2c-013 (FLOP-matched equivalence) and w14w2c-075
   (per-image regression accounting) are complementary claims about the same practice; keep
   both, cross-link.
7. **Resolution family (within shard):** w14w2c-001, -009, -084, -129 all use resolution as
   the operative variable with distinct claims (scaling confound, compute-allocation axis,
   inference redundancy, degradation knee); cross-link, do not merge.
8. **Efficiency-hides-boundary-damage template:** w14w2c-123/124/126/127/128/130 share the
   "aggregate metrics hide boundary/small-object damage" template across different
   compression mechanisms; each carries a distinct mechanism and falsifiable prediction —
   flagging for awareness, not merger.
9. **Mutate verdicts carry an explicit `mutation` field** in
   `judge_B_worker_C.flags.jsonl`; apply the re-framing at merge time rather than dropping.
10. Judge A and Judge C verdicts were not consulted (independence requirement); conflicts
    must be resolved by the consolidator. Novelty remains unverified for all 130 ideas; no
    papers, citations, or numbers were invented or checked here.

## Files written (only)

- `Windows14/_state/tasks/p1/wave2/judge_B_worker_C.md` (this file)
- `Windows14/_state/tasks/p1/wave2/judge_B_worker_C.flags.jsonl` (130 verdict lines, one per idea)
- `Windows14/_state/tasks/p1/wave2/judge_B_worker_C.done.json`

## Recommended next task type

`p1_wave2_consolidator` — with this supplemental pass, judge_B coverage of wave2 is
complete (shards A/B/D/E in `judge_B.flags.jsonl`, worker_C in
`judge_B_worker_C.flags.jsonl`, 638 ideas total); the consolidator can merge all five
shards with Judge A + Judge B (+ Judge C if present) flags.
