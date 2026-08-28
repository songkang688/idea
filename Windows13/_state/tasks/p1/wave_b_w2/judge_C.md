# P1 Wave B — Judge C (Adversary), Wave 2 (Generators D+E+F)

- **task_id:** `p1_wave_b_w2` · **role:** `judge_C_adversary` · **windows:** Windows13 (locked)
- **branch:** `cursor/p1-wave-b-w2-judge-c-adversary-46ac`
- **mandate:** attack mode collapse, template families, architecture permutation, wave1 collisions; independent keep/merge/kill; protect anomalies; no verified novelty claims; no fabricated citations.

## Inputs

| shard | branch | ideas |
|---|---|---|
| gen_d_object_detection | `origin/cursor/p1-gen-d-object-detection-07a3` | 100 |
| gen_e_vlm_dense_prediction | `origin/cursor/w13-p1-gen-e-vlm-dense-9412` | 100 |
| gen_f_synthetic_data | `origin/cursor/w13-p1-gen-f-synthetic-data-3a94` | 102 |

Wave1 master (248 accepted ideas) read **read-only** from `origin/cursor/p1-wave-b-consolidator-w1-7a58` for collision auditing. Wave2 Judge A (`origin/cursor/p1-wave-b-w2-judge-a-dedup-13e5`) was consulted **after** dispositions were drafted; wave2 Judge B (`done_judge_B.json`) did **not exist** on the remote at judging time (searched all refs; only wave1 `wave_b_w1` Judge B exists for Windows13). Canonical state files (`ideas_master.jsonl`, `research_state.json`, `window.lock.json`) untouched.

## Verdict summary

| | gen_d | gen_e | gen_f | total |
|---|---|---|---|---|
| input | 100 | 100 | 102 | **302** |
| keep | 68 | 78 | 77 | **223** |
| merge | 31 | 21 | 24 | **76** (59 within wave2, 17 into wave1 master) |
| kill | 1 | 1 | 1 | **3** |

Checksum: 223 + 76 + 3 = 302. Template families named: 28. Anomalies protected: 33. Deliberate tensions kept: 8. Cross-shard attractors: 13.

## Hygiene audit (pass 1)

All 302 records carry the uniform 13-field schema including `community_default_belief`, `why_it_might_be_wrong`, and `fastest_falsification_experiment`. A pattern scan for citation-like strings (`et al.`, `arXiv`, venue acronyms, year-parentheses) returned **zero** hits across all three shards — no fabricated citations. Hedging (`[HYPOTHESIS]`, `[MODEL SPECULATION / unverified]`, `[EXPECTED RESULT]`) is intact on every record spot-checked, including all kill candidates. Generator discipline in wave2 is materially better than a typical shard; the problems are structural (repetition), not epistemic (overclaiming).

## Mode collapse findings (pass 2)

- **gen_d** restates *"the bottleneck is naming, not finding"* four times (D-004, D-038, D-044-as-antithesis, D-071), runs the *bootstrap-noise* audit twice (D-032, D-085), the *context-reliance* probe four times (D-010, D-023, D-037, D-062), and the *abstention* deficit three times (D-003, D-016, D-070).
- **gen_e** runs the *referring-benchmarks-are-shortcut-solvable* audit three times (E-013, E-015, E-020), *consistency-as-free-signal* three times (E-021, E-029, E-096), and duplicates gen_d ideas wholesale at the dense substrate (distractor vocabulary, part-whole, hierarchy scoring, boundary-weighted eval, caption frequency).
- **gen_f** is the heaviest collapser: *"realism is not the active ingredient — axis X matters more"* appears **13 times** with X ∈ {motion stats, layout, occlusion stats, sensor noise, physics, assets, scene grammar, camera params, …}, *"cheap signal predicts expensive outcome"* seven times, and the real+synthetic scaling law is re-derived in four separate records (F-025, F-046→adjacent, F-057, F-097, F-101).

Treatment: closest same-hypothesis pairs merged to one primary; the rest of each family kept but **flagged** with `template:<family>` so the consolidator and novelty gate see the correlation structure. Merging an entire family into one idea would have destroyed genuinely independent falsification targets; leaving it unflagged would have hidden generator monoculture. Both errors are avoided.

## Architecture/task permutation attack (pass 4)

Cross-shard ports of one hypothesis merged to a single primary (detection ↔ segmentation ↔ dense ↔ MLLM is a substrate swap, not a new hypothesis): part-queries-return-wholes (D-008→E-079), distractor-vocabulary collapse (E-025→D-002), caption-frequency law (E-005→D-001), text-geometry forecast (D-005→E-047), boundary-weighted eval (E-067→D-047), hierarchy scoring (D-014, D-038→E-028), vocabulary narrowing (E-071→D-068), state grounding (E-092→D-069), interface-not-perception (E-093→E-041), correlated-teacher-errors (F-033→D-060), captioner fingerprints (F-029→E-077), context-without-object counterfactuals (E-073→E-010).

Ports of **published results** were killed, not merged (see kills): typographic attacks → OVD (D-059), register/outlier tokens → VLM dense (E-035), accumulate-vs-replace model collapse → vision (F-053).

## Wave1 collision audit (pass 5)

17 wave2 records restate accepted wave1 ideas closely enough that one experimental design covers both; each is merged into the wave1 master id (`wave1:` prefix in the merge map) so content attaches to the accepted program instead of duplicating it:

| wave2 id | wave1 target | collision |
|---|---|---|
| D-006, D-042, E-063 | C-052 | synonym-substitution ranking instability (detection / tail / cross-dataset ports) |
| D-035 | C-047 | few-shot support-set variance exceeds method gaps (near-verbatim) |
| D-054 | B-026 | prompt-jitter output variance as free quality signal |
| D-056 | A-102 | pseudo-label bias amplification (convexity/anti-thin) |
| D-067 | A-059 | photographic-composition prior (salience/centrality recall bias) |
| D-087 | C-077 | evaluation-harness variance flips comparisons |
| D-092 | C-028 | corruption suites don't predict natural shift |
| D-100 | C-069 | model-in-the-loop annotation contamination (adopted post-consultation, see below) |
| E-021 | C-020 | paraphrase inconsistency as error detector |
| E-037 | B-046 | dense/boundary texture-bias cue-conflict |
| E-065 | C-025 | leaderboard gaps within annotation noise (referring port) |
| E-066 | C-045 | hidden prompt-tuning budget against test benchmarks |
| E-070 | C-024 | zero-shot is seen-shot; contamination stratification |
| F-039 | C-058 | curation/pruning ≈ dedup in disguise |
| F-040 | C-102 | quality filters help some tasks, hurt others |

A further ~20 keeps carry explicit `wave1_adjacent` flags (see `judge_C.json → wave1_collision_audit.adjacency_flags_on_keeps`) where the wave2 idea shares a family with an accepted wave1 idea but asserts a genuinely different mechanism or instrument (e.g., D-012 vs C-103, E-84 vs B-030, E-95 vs C-060, F-86 vs C-023).

## Kills (3)

1. **D-059** (typographic attacks transfer to OVD) — expected-yes permutation of an established image-level phenomenon onto encoders the detectors literally reuse; the "community belief" it attacks is not genuinely held; residual content is measurement detail. Wave1 precedent: mirrored idea A-077 unanimously killed. *(Prior-art assessment unverified, stated as such.)*
2. **E-035** (high-norm outlier tokens hurt dense prediction; filter for free gains) — restates the documented register-token result including its dense-cost and remedy; the belief it attacks ("patch tokens are spatially faithful") is the one that literature already overturned; third across-wave instantiation of the outlier-token template. Judge A kept it but flagged it their #1 prior-art risk; this judge concludes kill. *(Unverified.)*
3. **F-053** (model collapse overstated; accumulation avoids it) — restates the accumulate-vs-replace boundary condition that is already the mainstream caveat to the collapse narrative; its `community_default_belief` is a strawman post that literature; residual is an ablation. Independent convergence: Judge A killed it too. *(Unverified.)*

All three kills are recoverable by the consolidator if the novelty gate overturns the prior-art assessments.

## Anomalies protected (33)

Non-template, contrarian, or tension-bearing ideas explicitly shielded from consolidation pressure. Highlights: D-029 (pattern-completion hallucination in regular layouts), D-097 (models out-localize their own training labels), D-044/D-072 (anti-theses to the shard's own naming-vs-finding consensus), E-055 (frame-of-reference bias shared with annotators), E-084 (grammar→mask-topology coupling), E-087 (complement queries fail with zero perceptual excuse), E-095 (chain-of-thought actively harms grounding), F-080 (uncanny-valley non-monotonicity), F-089 (batch-generation i.i.d. violation), F-091 (realism re-imports spurious correlations), F-096 (students exceed teachers via averaging), F-060 (generator supply-chain forensics), F-043 (reversed curation direction). Full list with notes in `judge_C.json → anomaly_notes`.

## Deliberate tensions kept (8)

Experiment-adjudicable disagreements preserved rather than deduplicated, e.g. D-071 vs D-044 vs D-072 (what actually bottlenecks detection), F-052 vs F-096 (generator ceiling vs student surpassing), D-039 vs F-005 (opposite signs on copy-paste blending), F-017 vs F-019 (is photorealism obsolete or are low-level render statistics load-bearing), F-073 vs F-091 (does more synthetic diversity always help). Full list in `judge_C.json → deliberate_tensions_kept`.

## Post-hoc comparison with Judge A (dedup)

Read only after this judge's dispositions were drafted. Strong independent convergence on ~30 merge groups and on the F-053 kill. Recorded divergences: E-035 (A keeps/flags, C kills); the E-013/E-014/E-020 group (A collapses to one primary, C keeps two); primary-direction flips on D-021/D-079 and the F-027/F-090 convention cluster; routing of the synonym-instability ports (A → wave2 E-029, C → wave1 C-052). One objective adoption: **D-100 → wave1 C-069**, a collision this judge missed in the independent pass and verified against the master before adopting — recorded transparently, not deference. Details in `judge_C.json → judge_A_divergence_post_hoc`.

## Epistemic status

No novelty verified for any kept idea. All prior-art-risk statements (20-entry watchlist in `judge_C.json → watchlists.high_prior_art_risk_keeps`) are this judge's unverified hypotheses for the novelty gate to check first. No citations invented anywhere in this report or the JSON.

## Outputs

- `Windows13/_state/tasks/p1/wave_b_w2/judge_C.md` (this file)
- `Windows13/_state/tasks/p1/wave_b_w2/judge_C.json` (full verdicts: keep_ids, merge_map with reasons, kill_reasons, families, anomalies, tensions, watchlists)
- `Windows13/_state/tasks/p1/wave_b_w2/accepted_shard_C.jsonl` (223 keep records with flags)
- `Windows13/_state/tasks/p1/wave_b_w2/done_judge_C.json`

**recommended_next_task_type:** `p1_wave_b_w2_consolidator`
