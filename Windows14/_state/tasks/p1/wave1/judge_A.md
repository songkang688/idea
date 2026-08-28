# Windows14 P1 Wave B - Judge A: cross-shard dedup + hypothesis clustering

## Scope and inputs
Fetched and read from origin (not chat):
- `origin/cursor/windows14-p1-wave-a-worker-a-e978` -> `worker_A.ideas.jsonl` (132 ideas, SAM/foundation-model adaptation/PEFT)
- `origin/cursor/windows14-p1-wave-a-worker-b-c6ba` -> `worker_B.ideas.jsonl` (126 ideas, medical segmentation)
- `origin/cursor/windows14-p1-wave-a-worker-c-4be5` -> `worker_C.ideas.jsonl` (124 ideas, smoke/fire/transparent/ambiguous + failure mining)

Total input ideas: **382**. All ideas are `evidence_status=HYPOTHESIS`; nothing here verifies novelty or adds citations.

## Method
Clustering was done at the **hypothesis level** (core mechanism/causal claim), not wording or domain. Two ideas
are near-duplicates when they assert the same underlying mechanism even if instantiated in different territories
(e.g. tokenization size floor in medical lesions vs smoke wisps). Ideas that share a mechanism family but make
distinct falsifiable predictions are kept as `variant`. Ideas with no hypothesis-level overlap are grouped into
distinct-theme groups (`distinct_theme_group`) purely for consolidator navigation; those members are NOT duplicates.

Member roles in `judge_A.clusters.jsonl`:
- `primary` - recommended anchor for the cluster (keep).
- `near_duplicate` - same core hypothesis as another member; **kept** but flagged as a merge candidate (keep).
- `variant` - same hypothesis family, distinct falsifiable prediction (keep).
- `drop_duplicate` - hypothesis-level duplicate of a kept member; recommend **drop** and fold into the noted target.
- `distinct` - unique hypothesis inside a theme group (keep).

## Results
| stat | value |
|---|---|
| input ideas (A/B/C/total) | 132 / 126 / 124 / 382 |
| clusters emitted | 81 (52 hypothesis-overlap, 29 distinct-theme groups) |
| cross-shard clusters | 46 |
| duplicate marks total | 78 (15 drop_duplicate + 63 near_duplicate kept) |
| keep / drop recommendations | 367 keep / 15 drop |

## Drop recommendations (fold, do not discard content)
Every `drop_duplicate` is a hypothesis-level duplicate of a kept idea; its domain-specific prediction should be
folded into the primary as an experimental arm, per the member note.

| id_seed | cluster | fold into / reason |
|---|---|---|
| `w14p1c-105` | XD-01 | fold into w14A-021/w14_p1b_061 as amorphous thin-wisp arm; identical tokenization-bottleneck claim |
| `w14p1c-061` | XD-02 | fold into w14_p1b_005: identical instability-matches-human-disagreement hypothesis, smoke arm |
| `w14p1c-083` | XD-02 | fold into w14p1c-001/w14A-010: minimal-flip-displacement fragility score is the same signal repackaged |
| `w14p1c-065` | XD-03 | fold into w14_p1b_008: identical fringe-confidence inversion, smoke arm |
| `w14p1c-060` | XD-06 | fold into w14A-020/w14p1c-002: predicted-minus-actual IoU gap is the same signal used as detector |
| `w14p1c-063` | XD-07 | fold into w14_p1b_075 as density-shift arm; same coverage-breakage hypothesis |
| `w14p1c-008` | XD-08 | fold into w14_p1b_044 as smoke arm; identical AMG-blindness hypothesis |
| `w14p1c-109` | XD-11 | fold into w14_p1b_035 as smoke arm; identical hypothesis. Note tension with w14A-073 (pruning as helpful regularizer) |
| `w14p1c-076` | XD-14 | fold into w14p1c-072 as cross-dataset train/test matrix arm; same conventions-exceed-models hypothesis |
| `w14p1c-039` | XD-14 | fold into w14p1c-072: fire-definition disagreement arm of the same hypothesis |
| `w14p1c-057` | XD-15 | fold into w14p1c-071 as alarm-latency arm; same IoU-vs-alarm-utility hypothesis |
| `w14p1c-073` | XD-17 | fold into w14_p1b_100 as event-level (same-fire frames) arm; identical leakage hypothesis |
| `w14p1c-092` | XD-20 | fold into w14_p1b_122 as open-vocabulary arm; same negation-blindness hypothesis (locus differs: fusion vs text encoder - note in consolidation) |
| `w14p1c-111` | XD-27 | fold into w14p1c-043 as vs-diffusion-generated comparison arm; same physically-grounded-synthesis hypothesis |
| `w14p1c-045` | XD-40 | fold into w14p1c-075 as region-level soft-IoU arm; same opacity-aware-metric hypothesis |

## Strongest cross-shard duplicate signals (all three territories collide)
- **XD-01 tokenization size floor**: `w14A-021` + `w14_p1b_061` + `w14p1c-105` - same architectural-floor hypothesis, three domains.
- **XD-02 prompt-jitter instability as signal**: `w14_p1b_005` + `w14A-010` + `w14p1c-001/061/083`.
- **XD-06 internal quality-signal miscalibration**: `w14A-020/012/056/082` + `w14p1c-002/060/064` + `w14_p1b_076`.
- **XD-15 metric/objective decoupling** and **XD-16 undertuned-baseline artifacts**: the two shards' evaluation-science
  clusters largely mirror each other (`w14_p1b_107` ~ `w14p1c-071`; `w14A-071` ~ `w14p1c-070`).
- **XD-22 latent unread signals**: `w14A-091` + `w14_p1b_011` + `w14p1c-110` (soft boundary/opacity recoverable without retraining).

## Tension pairs (kept deliberately; consolidator should pair them into single decisive experiments)
- **XD-06**: w14A-082 vs w14p1c-002: IoU head transfers well vs is anti-informative OOD
- **XD-04/XD-02**: w14_p1b_073 (model uncertainty decorrelates from raters, controlled) vs w14_p1b_005/w14p1c-061 (jitter instability matches rater disagreement)
- **XD-29**: w14A-028 (register-like tokens clean transfer) vs w14p1c-104 (register tokens drain amorphous evidence)
- **XD-52**: w14_p1b_079 (feature distance predicts error) vs w14p1c-067 (smoke is feature-space in-distribution, error OOD-grade)
- **DG-24**: w14p1c-026 (depth input hurts transparent objects) vs w14p1c-102 (depth conditioning degrades gracefully)
- **XD-11 vs DG-10**: w14_p1b_035/w14p1c-109 (token reduction discards rare targets) vs w14A-073 (token pruning as helpful regularizer)
- **XD-19**: w14_p1b_093 (too much contextual shape prior: hallucination) vs w14_p1b_029 (too little: no completion beyond FOV)

## Caveats / unresolved
- All clustering is judgment-based on hypothesis text; no embedding or literature search was used. No novelty is claimed or verified for any idea.
- Near-duplicate calls between a general (worker_A) and a domain (worker_B/C) instantiation keep both when the domain version adds a distinct measurable law or intervention; the consolidator may merge more aggressively.
- Worker_C flagged intra-shard near-neighbors in `worker_C.md`; those judged genuinely duplicative are in the drop list, the rest are marked `near_duplicate` and kept.
- Shared-infrastructure observations from worker done.json files (multi-annotator smoke labels, alpha-composite pipeline) are consolidation opportunities, not duplicates.

## Recommended next task
`p1_wave1_consolidator`: merge fold-targets into primaries, resolve the tension pairs, and select per-cluster champions.
