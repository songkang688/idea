# P1 Wave A — batch_003 gen_A Report

- **task_id:** p1_wave_a_batch003_gen_A
- **role:** generator (Wave A)
- **windows_path:** Windows15
- **territory:** T07 benchmark/dataset weaknesses
- **base branch:** origin/cursor/windows15-p1-state-reader-a5fa
- **output_dir:** Windows15/_state/tasks/p1/batch_003/gen_A/
- **idea_count:** 100 (target 100, contract range 80–120)
- **id range:** W15-B003-A-001 … W15-B003-A-100 (sequential, unique, machine-verified)

## What was generated

100 distinct scientific hypotheses about benchmark and dataset weaknesses — the science of ML
evaluation instruments: statistical power, contamination, annotation economics, lifecycle and
saturation, composition bias, split/test-set construction, external validity of rankings,
synthetic/LLM-judged evaluation, scoring protocol, provenance and documentation, item-response
psychometrics, human baselines, and benchmark repair. Each JSONL record carries the full required
schema: `idea_id`, `one_line`, `cluster`, `problem`, `core_hypothesis`, `falsifiable_prediction`,
`why_important`, `why_possibly_novel`, `minimal_falsification_experiment`, `main_risk`,
`community_default_belief`, `why_that_may_be_wrong`, `fastest_falsification`, `evidence_class`
(plus `territory` and a new `stance` field for downstream dedup/audit convenience).

## Diversity-audit compliance (checkpoint-1 findings applied)

Findings were fetched from the three diversity-audit branches
(`p1-diversity-auditor-a-d203`, `p1-diversity-audit-1-auditor-b-10e4`,
`p1-diversity-audit-1-auditor-c-79d3`) and applied — not copied — inside this territory:

1. **Deflationary cap (~25% recommended by auditor_A):** an explicit `stance` field was added
   to every idea, machine-tallied:

   | Stance | Count | Notes |
   |---|---|---|
   | constructive | 28 | mechanisms/instruments to build: paired evaluation, canaries, ambiguity certificates, anchor equating, escrows, adaptive testing, repair pipelines |
   | quant_law | 21 | quantitative laws: rank-stability collapse, contamination dose-response, ROI curves, survival curves, benchmark half-life, protocol gradients |
   | debunk | 20 | at the auditor cap of ~25%, aimed at genuinely held beliefs (seed variance, temporal leakage, mega-score redundancy, human-baseline softness, committee blind spots) |
   | null_equivalence | 17 | equivalence hypotheses with pre-registered margins (label noise vs rankings, crowd vs expert, deletion vs relabeling, harness two-regime) |
   | rehabilitation | 10 | affirm/defend criticized defaults: test-set reuse benign, gaming rank-safe, old benchmarks valid, crowd labels adequate, error-aware rescoring restores 'broken' benchmarks, field robust to dataset retraction |
   | mechanism | 4 | causal decompositions (contamination via answer-binding, synthetic tail-smoothing, duplicate weighting, era-drift probes) |

2. **Skeleton cap (max 5 per claim skeleton, auditor_B):** the pure unconditional
   "rankings are unchanged" skeleton is held to 5 instances (A-005, A-018, A-029, A-031, A-052);
   the other null/equivalence ideas carry structured predictions (two-regime thresholds,
   divergence-stratum localization, additivity/interaction tests, non-ranking equivalence objects).
   Instance-enumeration of a single claim over N domains was avoided entirely.

3. **Anti-safe-contrarianism (auditor_C):** `community_default_belief` fields describe
   real community practice or actually argued positions, without absolutist intensifiers; for
   rehabilitation ideas the "default belief" is the popular criticism being tested, so the schema
   no longer forces a debunk direction.

4. **Falsification-design diversity (auditor_A found 22% correlation studies):** experiments
   include randomized/factorial trials (A-021, A-022, A-043, A-092), controlled injection/dosing
   (A-009, A-011, A-013), replicate re-collection (A-006, A-025, A-046, A-090), replay/simulation
   against archives (A-030, A-048, A-082, A-094), judge-swap matrices (A-057, A-059), seeded
   adversarial probes (A-032, A-096, A-097), retrain ablations (A-074), bibliometric survival
   models (A-072, A-076), psychometric fitting (A-078–A-085), live A/B challenge designs (A-066,
   A-070), and equating/escrow protocol validations (A-028, A-099, A-100).

## Cluster distribution (13 clusters, max size 8)

| Cluster | Count | Theme |
|---|---|---|
| benchmark_statistical_power | 8 | Rank-stability laws, seed-variance census, paired evaluation, error-correlation aging, collection-variance CIs, adaptive testing, leaderboard capacity |
| contamination_leakage | 8 | Mechanism dissociation, uniformity equivalence, canary dosimeters, semantic-dup misses, dose-response law, temporal/entity leakage, similarity-stratified scoring, probing-leak bounds |
| annotation_economics_quality | 8 | Depth-vs-breadth allocation law, crowd-label rehabilitation, disagreement-targeted relabeling, noise ceilings, gold-question conformity, guideline-length null, ambiguity certificates, fatigue curves |
| benchmark_lifecycle_saturation | 8 | Reuse-overfitting rehabilitation, lifespan law, disputed-item progress migration, anchor equating, successor-order null, saturation changepoints, gaming rank-safety, trap twins |
| dataset_composition_bias | 8 | Discrimination concentration, collection-interface tail law, difficulty strata, geographic rank stability, balanced-vs-natural null, collector-model imprint, source-diversity exchange rate, slice power cards |
| test_set_construction | 8 | Split-design hierarchy, collection-event inflation, curation-filter additivity, within-test duplicates, minimal pairs, test-retest reliability, procedural-GT equivalence, difficulty escrow |
| ranking_validity_external | 8 | Portability decay law, g-factor rehabilitation, scale confound, ensemble rank-redundancy, mega-score dimensionality, reversal admission test, legacy-benchmark validity, harness two-regime |
| synthetic_llm_eval | 7 | Judge similarity gradients, tail-smoothness mechanism, judge triangulation, tier-vs-rank resolution, circulation-driven judge drift, format-vs-fact decomposition, executable-spec generators |
| benchmark_metric_protocol | 7 | Aggregation flips, convention materiality bound, pre-registered budgets, protocol gradients, optimal split allocation, metric top-invariance, noisy-channel leaderboards |
| data_provenance_documentation | 7 | Silent mutation, decay survival law, content-addressed releases, retraction robustness, documentation-quality null, citation lock-in, version-diff registry |
| difficulty_item_response | 8 | IRT compression, era-invariant difficulty, drift-item probes, discrimination-weighted deltas, frontier refresh, human-RT orthogonality, format psychometrics, ability reporting |
| human_baseline_reference | 7 | Incentive-controlled baselines, realistic-condition rehabilitation, crowd-expert routing, ambiguity-agreement curve, parity as frozen-set property, psychophysical correction, protocol cards |
| benchmark_repair_mechanisms | 8 | Impact-forecast repair, ROI decay law, deletion-vs-relabel null, committee blind spots, immune-system streams, posterior-rescoring rehabilitation, fork equating, sealed replicates |

## Evidence-class tag usage

falsifiable_hypothesis 68 · measurement_critique 44 · new_question 28 · counterintuitive_result 20 ·
new_observation 17 · ignored_assumption 13 · failure_mode 10 (each idea carries 2 tags).

## Hard-rule compliance

- **No verified-novelty claims:** every `why_possibly_novel` field is explicitly hedged
  ("hypothesis; not literature-verified" or equivalent) — machine-checked on all 100 records.
- **No invented citations, papers, benchmark numbers, datasets, or experimental results:** ideas
  reference only generic resource classes ("a long-lived leaderboard with archived per-item
  predictions", "public multi-rater datasets"). No named papers, no asserted results; numbers
  appear only as hypothesis parameters inside predictions.
- **Shard-only writes:** only `Windows15/_state/tasks/p1/batch_003/gen_A/` was written.
  `window.lock.json`, `research_state.json`, `ideas_master.jsonl`, `research_ledger.md`, and other
  task directories were not touched. No Windows directory was created; no lock fields modified.

## Territory-boundary notes for the dedup consolidator

- Batch_001 gen_B (T02) flagged its evaluation-metrology ideas (W15-B001-B-013..024) as potential
  T07 neighbors. This shard deliberately stays at the benchmark-instrument level (leaderboards,
  test-set construction, cross-benchmark validity, provenance) rather than segmentation-metric
  mathematics or medical rater noise. Closest-approach pairs to check anyway: A-005/A-018/A-020
  (label noise vs rankings/ceilings) against gen_B's annotation-metrology block, and A-089
  (convention-encoded labels) against gen_B's protocol-imprint ideas.
- A-057..A-063 (LLM-judge and generated-item evaluation) may neighbor future T15 (LLM/agent)
  shards; they are scoped to evaluation-instrument validity, not LLM capabilities.
- A-016, A-070 (adaptive-overfitting bounds, noisy-channel leaderboards) may neighbor T08
  (uncertainty/calibration) if that shard covers eval-server statistics; flagged for the ledger.
- A-047, A-058, A-060, A-063 (synthetic/procedural test data) may neighbor T09 (synthetic data,
  batch_003 gen_C); they are scoped to evaluation-side validity, not synthetic training data.
  Recommend cross-shard check during batch_003 dedup.

## Unresolved items

1. Novelty is hypothesized only — no literature verification was performed by this generator (per contract).
2. Cross-shard overlap checks recommended: batch_003 gen_C (T09) on A-047/A-058/A-060/A-063; future T15 on A-057..A-063; future T08 on A-016/A-070; batch_001 gen_B metrology block on A-005/A-018/A-020/A-089.
3. Several minimal experiments assume access to archived per-item prediction files or competition submission logs; feasibility triage deferred to later selection stages.
4. The `stance` field is an addition to the schema responding to diversity-audit recommendations; the Wave B consolidator may keep or drop it, but keeping it makes stance quotas auditable corpus-wide.
