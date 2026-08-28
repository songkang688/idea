# Windows14 P1 Wave 2 - Judge A: cross-shard dedup + hypothesis clustering

## Scope and inputs
Fetched and read from origin (not chat):
- `origin/cursor/windows14-p1-wave2-worker-a-cc54` -> `worker_A.ideas.jsonl` (133 ideas, synthetic data + domain shift)
- `origin/cursor/windows14-p1-wave2-worker-b-8795` -> `worker_B.ideas.jsonl` (126 ideas, super-resolution / restoration + diffusion)
- `origin/cursor/windows14-p1-wave2-worker-c-9388` -> `worker_C.ideas.jsonl` (130 ideas, negative results + contrarian)
- `origin/cursor/windows14-p1-wave2-worker-d-a7e5` -> `worker_D.ideas.jsonl` (124 ideas, object detection failure modes)
- `origin/cursor/windows14-p1-wave2-worker-e-e584` -> `worker_E.ideas.jsonl` (125 ideas, VLM / dense prediction)

Cross-wave context (read-only, NOT modified): `origin/cursor/windows14-p1-wave1-consolidator-13bd` -> `Windows14/_state/ideas_master.jsonl` (366 canonical wave1 ideas), used only for cross-wave near-duplicate flags.

Total input ideas: **638**. All `id_seed` values are unique across shards. All ideas are `evidence_status=HYPOTHESIS`; nothing here verifies novelty or adds citations.

## Method
Same protocol as wave1 judge_A. Clustering is at the **hypothesis level** (core mechanism / causal claim), not wording or domain. Candidate pairs were surfaced by a TF-IDF cosine scan over `one_line + core_hypothesis + falsifiable_prediction` (threshold 0.18, 262 pairs, 105 cross-shard) plus a targeted manual sweep of the three collision zones (worker_C contrarian restatements vs B/D/E; D-vs-E open-vocab; A-vs-B synthetic contamination). Every duplicate/near-duplicate call below is a judgment call on hypothesis text, not a similarity score.

Member roles in `judge_A.clusters.jsonl`:
- `primary` - recommended anchor for the cluster (keep).
- `near_duplicate` - same core hypothesis as another member; **kept** but flagged as a merge candidate (keep).
- `variant` - same hypothesis family, distinct falsifiable prediction (keep).
- `drop_duplicate` - hypothesis-level duplicate of a kept member; recommend **drop** and fold into the noted target.
- `distinct` - unique hypothesis inside a theme group (keep).

Wave2 shards have far more disjoint territories than wave1's, so overlap density is lower: most duplication is worker_C (negative/contrarian) independently re-deriving claims that B/D/E state in their home territory, plus the built-in D (detection) vs E (VLM dense) open-vocab overlap.

## Results
| stat | value |
|---|---|
| input ideas (A/B/C/D/E/total) | 133 / 126 / 130 / 124 / 125 / 638 |
| clusters emitted | 110 (44 hypothesis-overlap, 66 distinct-theme groups) |
| cross-shard overlap clusters | 38 |
| duplicate marks total | 56 (15 drop_duplicate + 41 near_duplicate kept) |
| keep / drop recommendations | 623 keep / 15 drop |
| drops by shard (A/B/C/D/E) | 2 / 1 / 8 / 2 / 2 |

Theme groups (`TG2-*`) partition the 441 remaining ideas by their worker-assigned cluster labels for consolidator navigation; those members are NOT duplicates.

## Drop recommendations (fold, do not discard content)
Every `drop_duplicate` is a hypothesis-level duplicate of a kept idea; its shard-specific prediction should be folded into the primary as an experimental arm, per the member note.

| id_seed | cluster | fold into / reason |
|---|---|---|
| `w14w2c-038` | XW2-01 corruption_suite_external_validity | fold into w14w2b-116: identical corruption-suites-do-not-predict-real-robustness claim, bare form |
| `w14w2c-110` | XW2-02 crawl_contamination_of_benchmarks | fold into w14E-101: identical crawl-contamination + post-cutoff-imagery hypothesis, zero-shot segmentation arm |
| `w14w2c-113` | XW2-03 word_frequency_determines_openvocab | fold into w14E-106: identical frequency-beats-visual-difficulty claim, contrarian phrasing |
| `w14w2c-117` | XW2-04 caption_salience_alignment_cap | fold into w14E-107: identical rarely-named-regions-cannot-align claim (nameability vs segmentability) |
| `w14w2c-108` | XW2-05 annotation_noise_floor | fold into w14D2-047 as segmentation arm: identical below-threshold-GT-noise-exceeds-model-differences claim |
| `w14w2c-116` | XW2-08 bagofwords_compositional_blindness | fold into w14D2-082: identical relational-blindness relation-swap claim, referring-segmentation arm |
| `w14D2-026` | XW2-09 query_list_interference | fold into w14D2-081: same vocabulary-size-tax measurement of the same interference effect |
| `w14D2-028` | XW2-10 part_whole_query_default | fold into w14E-110 as detection arm: identical part-query-returns-whole claim with object-centric-alignment mechanism |
| `w14E-057` | XW2-11 openvocab_nearest_neighbor_retrieval | fold into w14E-063: 'ocelot yields cat-shaped masks' is the same neighbor-regression claim, rare-word arm |
| `w14w2a-112` | XW2-19 generated_image_contamination | fold into w14w2b-077: same benchmarks-drifting-synthetic-ward claim; keep its synthetic-trained-model-flattering readout as an arm |
| `w14w2a-036` | XW2-20 self_consuming_loop_collapse | fold into w14w2b-079: same boundary-entropy-per-cycle collapse law stated as a rate prediction |
| `w14w2b-080` | XW2-22 synthetic_occlusion_gap | fold into w14w2a-024: identical simpler-occlusion-topology-predicts-failure claim |
| `w14w2c-087` | XW2-23 temporal_consistency_tradeoff | fold into w14D2-118: identical consistency-loss-trades-accuracy-for-smoothness claim, segmentation arm |
| `w14w2c-111` | XW2-27 taxonomy_convention_artifacts | fold into w14D2-059: identical taxonomy-mapping-dominates-generalization-tables claim |
| `w14E-076` | XW2-43 lexical_vagueness_uncalibrated | fold into w14E-079: identical confidence-ignores-lexical-vagueness claim, phenomenon form |

## Strongest cross-shard duplicate signals
- **XW2-03/XW2-04 caption/word statistics determine open-vocab performance**: `w14E-106` + `w14w2c-113` + `w14D2-022` + `w14E-010`, and `w14E-060` + `w14D2-087` + `w14E-107` + `w14w2c-117` - three shards independently claim language-frequency statistics, not visual difficulty, set dense performance.
- **XW2-05 annotation noise floor**: `w14D2-047` + `w14w2c-108` + `w14D2-061` - small/rare-object leaderboards bounded by annotation agreement, det + seg arms.
- **XW2-08 bag-of-words compositional blindness**: `w14D2-082` + `w14w2c-116` + `w14D2-024` + `w14E-043` - relation/modifier/attribute-binding blindness converging from three shards.
- **XW2-09 query-list interference**: `w14D2-081` + `w14D2-026` + `w14E-089` (+ hierarchical/synonym variants `w14E-090`, `w14E-088`).
- **XW2-19/XW2-20 synthetic contamination and loop collapse**: `w14w2b-077` + `w14w2a-112`, `w14w2b-079` + `w14w2a-036` - A and B mirror each other on generated-data contamination and self-consuming-loop collapse.
- **XW2-23 temporal-consistency tradeoff**: `w14D2-118` + `w14w2c-087` + four B/D variants - smoothness-vs-accuracy exchange claimed identically for detection and segmentation.

## Tension pairs (kept deliberately; consolidator should pair each into one decisive experiment)
- **XW2-24**: `w14w2b-104` (temporal memory saturates; long memory buys persistence, not accuracy) vs `w14w2c-088` (memory anti-scales: more stored frames = more drift).
- **XW2-44**: `w14w2c-024` (SSL-vs-supervised advantage vanishes under full fine-tuning) vs `w14D2-086` (SSL-vs-supervised failure profiles persist through identical fine-tuning).
- **XW2-42**: `w14w2a-059` (match LiDAR intensity physics per material) vs `w14w2a-066` (drop the intensity channel entirely; geometry-only transfers better).
- **XW2-09**: `w14D2-025` (adding confusable negative vocabulary cuts false positives) vs `w14E-034` (semantically dense vocabularies self-poison with false positives).
- **XW2-41**: `w14w2c-118` (prompt-template gains are dataset-specific noise) vs `w14E-011`/`w14E-012` (dense-specific templates and ensembling effects are real and structured).
- **XW2-40**: `w14w2c-115` (grounding bottleneck is the vision encoder) vs `w14E-064` (small-object grounding fails at the fusion stage, not the vision stage).
- **XW2-36**: `w14w2b-015` (seed-instability detects hallucination) vs `w14w2b-019` (deterministic samplers make hallucination reproducible, defeating exactly that detector) - a validity dependency, not a contradiction.
- **XW2-17**: `w14w2b-028`/`w14w2a-015` (model the ISP to close the gap) vs `w14w2c-067` (strong photometric augmentation narrows models to the benchmark pipeline and backfires).

## Cross-wave near-duplicate flags (vs wave1 ideas_master.jsonl; flags only, all wave2 members kept)
- **STRONG**: `w14D2-012` (per-object-size temperature scaling fixes what global temperature cannot) vs wave1 `w14-0202` (size-conditional recalibration beats global temperature scaling). Nearly the same hypothesis; wave2 adds the detection arm and the reliability-curve mechanism. Consolidator must dedup or explicitly mark as detection extension of w14-0202.
- **MODERATE**: `w14w2b-037` (8-bit export destroys sub-quantization gradients annotators saw in windowed views; train-label mismatch) vs wave1 `w14-0153` (8-bit conversion erases low-contrast lesions; input recall ceiling). Same physical cause, different locus (label mismatch vs input ceiling).
- **MODERATE**: `w14w2c-125` / `w14w2a-113` (distillation transfers teacher failure map / synthetic biases) vs wave1 `w14-0068` (distilled students inherit accuracy but lose the correction loop). Same inheritance family, distinct claims.
- **WEAK**: `w14w2b-108` (models silently correct rolling-shutter distortion toward canonical shapes) vs wave1 `w14-0366` (rolling-shutter banding as spurious fire cue). Shared physics only.

## Caveats / unresolved
- All clustering is judgment-based on hypothesis text; TF-IDF was used only to surface candidates (threshold 0.18), so paraphrase duplicates with fully disjoint vocabulary could be missed. The three high-collision zones were manually swept in full; low-collision zones (A intra-shard, B intra-shard technique clusters) rely on the scan plus worker cluster labels.
- Near-duplicate members are kept, not merged; the consolidator decides final merges per cluster.
- No novelty verification was performed; all clustering is over unverified HYPOTHESIS-status ideas. Never treat cluster primaries as validated.
- Cross-wave flags are advisory: this judge does not modify wave1 canonical state and did not dedup against it beyond flagging.
- Theme groups (`TG2-*`) inherit worker-assigned cluster labels; borderline members were not re-assigned across theme groups since theme groups carry no dedup semantics.

## Recommended next task
`p1_wave2_consolidator`: merge fold-targets into primaries, resolve the tension pairs, apply the cross-wave flags against `ideas_master.jsonl`, and select per-cluster champions.
