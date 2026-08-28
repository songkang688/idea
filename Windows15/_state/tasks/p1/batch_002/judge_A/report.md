# P1 Wave B — batch_002 Judge A (hypothesis clustering)

- **task_id:** `p1_wave_b_batch002_judge_A`
- **windows_path:** `Windows15` (LOCKED — this task writes only under `_state/tasks/p1/batch_002/judge_A/`; no canonical files touched)
- **inputs:**
  - `gen_A` — 100 ideas, T04 object detection science (`origin/cursor/p1-wave-a-batch002-gen-a-83d7`)
  - `gen_B` — 100 ideas, T05 VLM dense prediction (`origin/cursor/p1-wave-a-batch002-gen-b-0edc`)
  - `gen_C` — 100 ideas, T06 failure mining (`origin/cursor/p1-wave-a-batch002-gen-c-86e2`)
  - master list — 271 accepted batch-001 hypotheses (`origin/cursor/p1-wave-b-batch001-consolidator-7c96`), used **only** to detect duplicates of already-accepted hypotheses
- **constraints honored:** no verified novelty claims, no citations fabricated, no writes to `ideas_master.jsonl`, `research_state.json`, `research_ledger.md`, or `window.lock.json`.

## Method

Clustering is hypothesis-level: ideas are grouped by their shared falsifiable core claim and mechanism (what would have to be true of the world), not by keyword, shard, or generator-supplied cluster label. Decision policy:

- **merge** — same falsifiable core and substantially the same experiment would test both (true near-duplicates). The `merge_into` target is the canonical survivor; salvageable variant conditions are noted.
- **drop / duplicate_of_master** — the falsifiable core is already accepted in the batch-001 master list; `duplicate_of` names the master idea. Salvageable extensions are noted for the consolidator.
- **drop / prior-art risk** — the core claim is, with high (unverified) confidence, established textbook/classic material rather than an open hypothesis. Used once; consolidator may reinstate.
- **keep** — everything else, including *template twins* (same claim template, different domain/instrument/observable), which are kept and recorded as near-duplicate relations, matching batch-001 judge policy.

## Results

| metric | value |
|---|---|
| input ideas | 300 (100 per shard) |
| clusters | 44 (`B2HC-01` … `B2HC-44`) |
| keep | 278 |
| merge (within batch) | 16 |
| drop | 6 (5 duplicate_of_master + 1 prior-art risk) |

### Within-batch merges (16)

Cross-shard convergence was substantial — 12 of 16 merges cross shard boundaries, which is a good sign the three territories found the same underlying phenomena independently:

| from | into | shared falsifiable core |
|---|---|---|
| B-068 | A-031 | small-object method gains sit within inter-annotator noise |
| C-057 | A-034 | below a size threshold, detection is context-driven with a measurable crossover |
| B-026 | C-021 | hallucination of absent categories follows co-occurrence priors |
| B-040 | C-002 | patches-per-object sets a hard detectability floor with size cliffs |
| B-041 | C-003 | resize-geometry distortion drives extreme-aspect failures |
| A-009 | C-059 | aspect-ratio recall cliffs predictable from architecture prior geometry |
| A-088 | C-022 | learned position-in-frame prior causes position-conditional failures |
| C-008 | B-042 | token-merging damage is concentrated and predictable from token similarity |
| C-046 | B-085 | attribute binding degrades superlinearly with instance count (capacity knee) |
| C-053 | C-092 | visual serial-position ("lost in the middle") effect on evidence position |
| B-064 | C-025 | pretraining near-duplicate contamination inflates results, stratifiable |
| B-030 | B-024 | negation acts as positive evidence (attribute variant of object variant) |
| B-017 | B-087 | relation words unused: inversion invariance is one instrument of conjunction-collapse |
| B-022 | B-087 | relation words unused: proximity-word ablation is another instrument |
| B-014 | B-008 | prompt-ensembling gains are an anisotropy workaround subsumed by whitening |
| A-095 | A-089 | spatial score interference with architecture-characteristic range |

### Duplicates of accepted master hypotheses (5, dropped)

| idea | duplicate of | already-accepted claim |
|---|---|---|
| C-001 | W15-B001-A-003 | mask outputs not shift-stable at sub-patch scale, error periodic in sub-token offset |
| B-072 | W15-B001-B-076 | miscalibration is boundary-localized; distance-to-boundary recalibration fixes it |
| B-083 | W15-B001-A-016 | domain gap lives in channel/normalization statistics (statistic recomputation is an intervention variant) |
| C-064 | W15-B001-C-033 | mask predictors carry a genus-zero / simply-connected topology prior |
| C-070 | W15-B001-A-005 | interactive correction enters oscillatory/limit-cycle dynamics (no correction memory) |

Each carries a salvage note in `verdict.jsonl` (e.g., C-064's data-rarity-vs-architecture attribution experiment could be folded into the master idea's plan).

### Prior-art-risk drop (1)

- **C-038** — analytic prior-shift (Bayes) recalibration under class-prior shift is classical statistics; the residual content is a validation study, not a new hypothesis. Unverified judgment; consolidator may reinstate.

### Master near-duplicates kept (38 flagged)

38 kept ideas share a claim template with an accepted batch-001 hypothesis but add distinct falsifiable content (new domain, instrument, conditioning variable, or quantitative law). They are enumerated in `clusters.json → master_near_duplicate_relations` so the consolidator can either accept them as separate entries or fold their new content into the master ideas. The most consequential: C-079 (generalizes the accepted SAM "segmentability probe" to any FM with a cross-head-transfer claim), C-081 (jitter-instability-beats-confidence generalized beyond SAM prompts), C-025 (contamination stratification generalized from fire/smoke corpora), and C-071 (deployment cliffs made per-instance).

### Internal contradictions retained intentionally (4)

1. **B-054 vs B-057** — text conditioning in depth models: atrophied no-op vs causal metric-scale shifter.
2. **A-092 vs C-087** — temporal smoothing of scores: harmless flicker fix vs destroys a catastrophic-failure early-warning signal.
3. **A-050 vs C-073** — corruption degradation: one-dimensional effective dose vs anisotropic weakly-correlated realizations.
4. **A-023 vs A-040** — sub-stride localization: floor needing new supervision vs information already present, readout-limited.

Each pair needs one resolving experiment matrix, not a verdict; both sides kept.

### Cluster landscape (44 clusters)

Largest clusters: confidence/calibration structure (13), assignment dynamics (12), duplicate suppression (11), VLM patch-representation limits (11), absence/negation/hallucination (11). Strong cross-shard clusters (grid-phase aliasing, contamination, context/position priors, threshold transfer) indicate the three territories converged on shared mechanisms — these are prime candidates for unified research programs at consolidation time. Full membership, shard coverage, and per-cluster merges/drops are in `clusters.json`.

### High-value flags (leverage judgments, not novelty claims)

15 ideas flagged in `clusters.json → high_value_anomalies`, led by: C-055 (pre-suppression audit reattributes crowded-scene misses), A-054 (assignment-frozen validation loss), C-071 (per-instance corruption cliffs), C-082 (confidence-mining composition bias), B-061 (pseudo-novelty audit of open-vocabulary benchmarks), C-079 (near-zero-cost failure prediction).

## Handoff

Recommended next task: `p1_wave_b_batch002_consolidator`. Open items for it are listed in `done.json → unresolved_items`.
