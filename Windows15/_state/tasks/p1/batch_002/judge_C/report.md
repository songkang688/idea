# P1 Wave B Judge C Report - batch_002 (adversarial duplicates)

- **task_id:** `p1_wave_b_batch002_judge_C`
- **windows:** `Windows15` (locked; no canonical files touched - writes confined to `Windows15/_state/tasks/p1/batch_002/judge_C/`)
- **role:** hard-duplicate audit within batch_002 (intra-shard and cross-shard) and against the accepted batch_001 master, with explicit protection of competing pairs
- **verdict scheme:** `keep | duplicate_of | drop`

## Inputs

| shard | branch | territory | ideas |
|---|---|---|---|
| gen_A | `origin/cursor/p1-wave-a-batch002-gen-a-83d7` | T04 Object detection | 100 (`W15-B002-A-001..100`) |
| gen_B | `origin/cursor/p1-wave-a-batch002-gen-b-0edc` | T05 VLM / dense prediction | 100 (`W15-B002-B-001..100`) |
| gen_C | `origin/cursor/p1-wave-a-batch002-gen-c-86e2` | T06 Failure mining | 100 (`W15-B002-C-001..100`) |
| master | `origin/cursor/p1-wave-b-batch001-consolidator-7c96` | T01/T02/T03 accepted | 271 (`Windows15/_state/ideas_master.jsonl`) |

Sibling judge branch `origin/cursor/p1-wave-b-batch002-judge-a-f0d4` was NOT read for judgments;
this audit is independent.

Input integrity checks (scripted): all three shards have exactly 100 sequential, unique IDs;
all 13 contract fields present in every record; a regex sweep for fabricated-citation patterns
(`et al.`, arXiv IDs, bracketed references, year-parenthesized citations, claimed numeric
benchmark results) found zero hits in 300 records. No `drop` verdicts were warranted on
integrity grounds.

## Dedup standard (inherited from batch_001 judge_C, extended for master audit)

Two ideas are hard duplicates when they assert the same core scientific claim such that
decisively falsifying/verifying one substantially falsifies/verifies the other. A domain
re-instantiation counts as distinct only if the domain changes the mechanism or the
prediction, not merely the dataset. Entailment, nested claims, and competing mechanisms
over one observable are NOT duplicates - they are flagged and protected. New for batch_002:
every idea was additionally screened against the 271 accepted master entries; an idea that
re-instantiates an accepted master claim without changing mechanism or prediction is marked
`duplicate_of` the master ID (master entries are never modified from this task).

Borderline calls were decided on full `core_hypothesis` / `falsifiable_prediction` text,
not one-liners. Two calls were reversed by full-text reading: `A-096` (FPN level-assignment
cohort steps - a genuinely different mechanism from `C-002`'s patch-count quantization; kept)
and `B-030` (initially misread as a competing "no-op" claim; its 'not red' = 'red' prediction
is the same negation-as-affirmative claim as `C-045`/`B-024`; merged).

## Verdict counts

- ideas reviewed: **300** (plus 271 master entries screened)
- keep: **280**
- duplicate_of: **20** (gen_A 3, gen_B 13, gen_C 4)
- drop: **0**
- hard duplicates by scope: intra-shard **8**, cross-shard **10**, vs master **2**

## Hard duplicates (duplicate -> canonical)

| duplicate | canonical | scope | conf | one-line rationale |
|---|---|---|---|---|
| A-037 | A-032 | intra_A | high | detection outcome periodic in sampling-grid phase; mitigation differs, claim identical |
| A-066 | C-017 | cross_A_C | medium | learned per-dataset annotation tightness/offset conventions confound cross-dataset localization |
| A-088 | C-022 | cross_A_C | medium | object-position-in-frame priors from framing statistics |
| B-014 | B-008 | intra_B | high | anisotropy/whitening vs prompt ensembling - same 2x2 ablation twice |
| B-024 | C-045 | cross_B_C | high | negation processed as affirmative mention (noun behavioral arm) |
| B-026 | C-021 | cross_B_C | medium | co-occurrence statistics predict hallucination - same regression |
| B-030 | C-045 | cross_B_C | medium | negation-as-affirmative, attribute instantiation |
| B-041 | C-003 | cross_B_C | medium | square-resize policy breaks extreme-aspect inputs |
| B-046 | B-049 | intra_B | medium | autoregressive serialization-position error growth |
| B-064 | C-025 | cross_B_C | high | pretraining/eval near-duplicate contamination stratification |
| B-068 | A-031 | cross_A_B | medium | small-object gaps inside the inter-annotator noise band - same measurement |
| B-072 | **W15-B001-B-076** | vs_master | high | boundary-distance-structured miscalibration + distance-conditioned recalibration |
| B-085 | C-046 | cross_B_C | high | binding-error capacity scaling with attributed-instance count |
| B-087 | B-017 | intra_B | high | relations unprocessed; conjunction-equivalence and inversion-invariance are one claim |
| B-092 | B-034 | intra_B | medium | caption-frequent renaming recovers open-vocab dense performance |
| B-099 | B-018 | intra_B | medium | grounding locked to camera frame regardless of requested reference frame |
| C-032 | C-029 | intra_C | medium | bimodal failure persistence under scale/generation change |
| C-057 | A-034 | cross_A_C | high | small-object detection is context-driven; context-ablation experiment identical |
| C-070 | **W15-B001-A-005** | vs_master | high | interactive correction oscillation/divergence restates accepted master claim |
| C-092 | C-053 | intra_C | high | visual lost-in-the-middle: multi-image and video-frame forms are one claim |

Every merge carries a `salvage_in_merge` note in `duplicates.json` so the consolidator
loses no experimental arm (e.g. A-037's half-stride double-inference recovery, B-064's
crawl-index stratification, C-070's early-warning divergence predictor).

All IDs above are `W15-B002-*` unless marked as master (`W15-B001-*`).

## Protected competing pairs (NOT duplicates - do not merge)

Intra-batch (12, including one quartet):

1. **B-001 vs B-002** - outlier tokens vs distributed gist leakage as the cause of bad similarity maps.
2. **B-017 vs B-023** - relations unprocessed vs relation accuracy frequency-predicted.
3. **B-045 vs B-048** - coordinate-vocabulary quantization vs round-number digit priors.
4. **B-054 vs B-057** - text conditioning in depth: no-op vs causal metric-scale shift.
5. **A-020 vs C-060** - pair-recall collapse: training-data statistics vs architecture signature.
6. **A-061 vs C-018** - convention mixing: per-class noise correlation vs policy blending.
7. **A-063 vs C-062** - border misses: missing labels (eval artifact) vs trained truncation suppression.
8. **C-027 vs C-033** - failure correlation: shared web data vs shared frozen backbones.
9. **C-080 vs C-085** - repair collateral: loss-landscape sharpness vs feature-space locality.
10. **C-081 vs C-030** - jitter instability marks failures vs consistent-wrongness blind spot.
11. **C-035 vs C-082** - error-population dichotomy vs mining selection bias (nested pair; each load-bearing).
12. **A-009 / A-018 / A-030 / C-059** - four competing mechanisms for elongated-object failure (assignment geometry, NMS overlap, loss extraction, box-prior cliffs).

Competing with master (5) - kept precisely because they contest an accepted master claim:

1. **C-006 vs W15-B001-A-035** - thin-structure failure: orientation-to-grid vs width threshold.
2. **C-036 vs W15-B001-B-076** - severity anti-alignment vs boundary-overconfidence calibration (different quantities).
3. **C-064 vs W15-B001-C-033** - genus deficit: data-attributable vs architecture-attributable.
4. **C-065 vs W15-B001-A-001** - granularity: intrinsic instability vs deterministic click-geometry dial.
5. **A-068 vs W15-B001-A-034** - contrast-edge snapping: annotation-inherited vs model prior.

Additionally, 12 kept ideas are flagged `protect:master_adjacent` (nested claims or
generalizations of accepted master entries, e.g. C-025 generalizing W15-B001-C-098, C-079
generalizing W15-B001-A-042, A-087 kept per the master's own precedent of retaining
per-domain count-prior instantiations). Details in `duplicates.json`.

## Near-duplicate families

45 families flagged in `verdict.jsonl` (`family:FXX_*` flags) to give the consolidator
collision-aware clustering without forcing merges - e.g. `F02_size_grid_cliffs`
(C-002, A-096, B-040, A-023, A-040), `F12_caption_frequency_law` (11 members),
`F26_calibration_structure`, `F33_pipeline_artifacts`. Family membership never overrides a
keep verdict.

## Compliance

- Novelty verification NOT performed (out of scope); `why_possibly_novel` treated as unverified labels throughout.
- No citations invented; no benchmark numbers asserted; rationales reference only the ideas' own texts and master IDs.
- Locked/canonical state files (`ideas_master.jsonl`, `research_state.json`, `research_ledger.md`, `window.lock.json`) untouched.
- Sibling judge output not copied or consulted.

## Outputs

- `report.md` (this file)
- `duplicates.json` - hard duplicates with rationales and salvage notes, protected pairs, families
- `verdict.jsonl` - 300 verdicts (`keep`=280 / `duplicate_of`=20 / `drop`=0)
- `done.json`

**recommended_next_task_type:** `p1_wave_b_batch002_consolidator`
