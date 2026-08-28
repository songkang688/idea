# P1 Wave B — Judge A: Hypothesis-Level Dedup (Wave 1: Generators A+B+C)

- **task_id:** `p1_wave_b_w1` | **role:** `judge_A_dedup` | **windows_id:** `Windows13` (locked)
- **branch:** `cursor/p1-wave-b-judge-a-dedup-f906`
- **Scope:** cross-shard dedup at the hypothesis level, near-duplicate clustering, permutation flagging, accepted-candidate list for THIS wave only. Canonical state (`ideas_master.jsonl`, `research_state.json`, `window.lock.json`) untouched. Parent will not merge; a later Consolidator writes canonical state after more judges.
- **Epistemic status:** NO novelty is verified for any kept idea. Every "prior-art risk" remark below is the judge's unverified HYPOTHESIS. No citations were invented.

## 1. Inputs

| Shard | Branch | Ideas | done.json status |
|---|---|---|---|
| gen_a_sam_foundation_peft | `cursor/p1-gen-a-sam-foundation-peft-c8d4` | 102 (W13-P1-A-001..102) | complete |
| gen_b_hard_domain_dense_prediction | `cursor/p1-gen-b-hard-domain-a13a` | 96 (W13-P1-B-001..096) | complete |
| gen_c_contrarian_eval | `cursor/windows13-p0-init-implementation-d93f` | 104 (W13-P1-C-001..104) | done |
| **Total** | | **302** | |

All 302 lines parsed; IDs contiguous per shard; no cross-shard ID collisions. No ideas invented or renumbered by this judge.

## 2. Method

Each idea was compared on its `core_hypothesis` content (mechanism + falsifiable claim), not title strings. Two ideas were treated as duplicates when they assert the same mechanism with the same falsification design, differing only in substrate (domain, task, metric, or the "X" slot of a template). Ideas sharing a premise but making distinct falsifiable claims were clustered, not merged. Template-generated families ("permutation" output: SAM+X, LoRA+X, loss+X, hidden-variable-confound, shortcut-ablation, reweighting-instability, statistical-noise, mask-forensics) were flagged; per family/group, one or two primaries were kept and the rest marked `kill_or_merge` with explicit merge targets. Unusual, non-template, high-upside ideas were protected as anomalies.

## 3. Verdict Counts

| Quantity | Value |
|---|---|
| Input total | 302 (A: 102, B: 96, C: 104) |
| **Keep (accepted candidates this wave)** | **245** (A: 92, B: 85, C: 68) |
| Kill or merge | 57 (A: 10, B: 11, C: 36) |
| Duplicate groups | 33 (50 of the 57 kills are merges inside these groups) |
| Standalone prior-art/permutation kills | 7 (A-085, A-089, C-036, C-055, C-059, C-062, C-104) |
| Flagged permutation-style ids | 63 (kept-but-flagged and killed combined) |
| High-value anomalies | 18 |
| Judge clusters | 32 (every one of the 302 ids assigned exactly once) |

Shard C required the most consolidation: it is the strongest shard conceptually but the most template-driven — 13 near-isomorphic instantiations of "hidden factor X contributes variance comparable to claimed gains," 9 of "benchmark solvable by shortcut Y," 5 of "rankings unstable under reweighting," 5 of "deltas are within noise."

## 4. Cross-Shard Duplicate Groups (the ones that matter most)

These are hypothesis collisions **across** generators — exactly what this judge exists to catch:

1. **dg01 Bimodal failure distributions** — A-071 ≡ B-036 (per-case scores bimodal; means track mixture weight). Keep A-071, merge B-036. One study, two territories.
2. **dg02 Pretraining-overlap inflation** — C-024 ≡ A-070 (zero-shot is partly "seen-shot"; overlap-stratified re-evaluation deflates). Keep C-024, merge A-070 as the SAM/SA-1B case study.
3. **dg03 Non-iid split leakage** — C-027 ⊃ {B-088 (smoke/fire video frames), C-033 (retrieval galleries), C-099 (temporal collection order)}. Keep C-027 as umbrella.
4. **dg04 Single-label evaluation fallacy** — {B-095, C-066} ⊃ {C-068, C-101, C-035}. Distribution/set-matching evaluation reranks models and deflates superhuman claims. Keep the segmentation instantiation (B-095) and the superhuman-reframing (C-066).
5. **dg05 Deterministic signals beat uncertainty machinery** — {C-018 (umbrella), B-050 (dense/hard-domain)} ⊃ {C-005, C-014, C-017}.
6. **dg14/dg10/dg07... (within-shard):** ranking-degrades-before-generation (A-026 ⊃ A-068), threshold-placement leaderboards (B-033 ⊃ B-007), loss-determines-geometry (B-018 ⊃ B-096), layered output spaces (B-073 ⊃ B-013), mask forensics (B-035/B-021 ⊃ B-081), uncertainty-vs-rater-disagreement (B-019 ⊃ B-051), recalibration-not-relearning (A-011/A-018/A-100 ⊃ A-098), ambiguity collapse (A-015/A-080 ⊃ A-064), and the C-internal template families (dg16–dg26).
7. **dg27 Head vs representation** — A-014 (SAM decoder-only sufficiency), B-031 (hard-domain separability audit), C-048 (head-recipe confound) form one cross-shard question with **opposing predictions** (A-014: gap lives in the readout; B-031: for hard domains it lives in features). Kept all three deliberately — this is a designed head-to-head, not redundancy. C-087 merged into C-048.

Full group list with members, primaries, and merge reasons: `judge_A.json → duplicate_groups` and `kill_or_merge_ids`.

## 5. Flagged Permutation Families

- **sam_plus_x_ports (14 ids, shard A):** task-arithmetic/soups (A-021), VPT-vs-LoRA (A-022), cue-conflict (A-035), registers (A-039), scale tokens (A-042), memory-LoRA (A-053), UAP-on-prompts (A-074, killed), typographic attacks (A-077), early exit (A-085, killed), score-router (A-086, killed), subspace angles (A-088), curricula (A-089, killed), click advisor (A-094), TT-norm (A-098, killed). Kept members survive because they carry a falsifiable mechanism beyond the recipe; all carry mandatory prior-art search flags.
- **hidden_variable_confound_template (13 ids, shard C):** consolidated to C-077 (harness umbrella) + C-052 (wording) + C-045 (search budget) + C-047 (draws) + C-054 (seeds) + C-048 (heads) + C-046 (probes).
- **shortcut_ablation_template (9 ids, shard C):** consolidated to C-090 (image-swap), C-089 (prior-decorrelated items), C-092 (OCR separation), C-095 (single-input sufficiency), C-097 (refusal style), C-103 (multilingual).
- **known_critique_restatements (6 ids, shard C):** C-035, C-036, C-055, C-059, C-062, C-104 — killed or merged; each restates a critique the judge assesses (unverified) as well-established.
- Also flagged: reweighting_instability (5), statistical_noise (5), mask_forensics (3), loss_plus_x (5), paradigm_ports_hard_domains (3).

## 6. High-Value Anomalies (protected, 18)

A-044 (relational regions unreachable by prompt-as-locator), A-063 (guideline archaeology / policy memorization), A-065 (SA-1B grid fingerprint), A-079 (modal/amodal instability law), A-087 (catastrophic remembering — adaptation moves models backward along training history), B-016 (human-model gap on glass is an evaluation-regime artifact), B-029 (ontological, not statistical, scaling asymptote), B-030 (mass-noun linguistic penalty), B-054 (representation-ambiguity matching law), B-069 (predict the spread-rate derivative, not the state), B-071 (event-camera combustion microdynamics), B-083 (sparse physical sensor labels beat dense human labels), B-090 (ambiguity-type transfer beats domain transfer), B-093 (human-model complementarity largest on hard domains), C-069 (model-assisted annotation self-preference loops), C-072 (annotation-vendor convention leakage), C-074 (leaderboard winner's curse), C-075 (benchmark ecosystem low effective dimensionality).

## 7. Accepted-Candidate List (this wave)

245 kept ids with cluster assignments, flags, duplicate-group membership, judge notes, and copied core fields are in `accepted_shard_A.jsonl`. Machine-readable dispositions (keep_ids[], kill_or_merge_ids[] with merge targets and reasons, clusters, duplicate_groups, flagged_permutation, anomaly_ids[]) are in `judge_A.json`.

Keep counts by judge cluster (kept/total; 32 clusters cover all 302 ids exactly once): prompt_geometry_and_interaction 17/18, peft_mechanism_recalibration 11/13, capability_collapse_forgetting 8/9, sam_scores_selection_calibration 8/10, encoder_representation_artifacts 10/10, decoder_output_space_mechanics 16/17, sam2_video_memory 9/9, data_provenance_priors 11/12, dense_metric_pathologies 7/10, eval_protocol_confounds 7/15, robustness_attacks_shift 12/13, distillation_compression 5/6, adapter_ecosystem_composition 3/4, loss_objective_bias 4/6, contamination_leakage 5/12, soft_boundary_ontology 8/8, transparency_physics 7/8, medical_rater_ambiguity 9/9, hard_domain_foundation_failures 6/6, shortcut_cue_reliance 10/10, dense_uncertainty_calibration 8/9, physics_image_formation 6/6, temporal_process_dynamics 6/6, statistics_reproducibility 5/8, label_ceilings_human_eval 9/14, unifying_failure_structure 3/4, calibration_estimators 8/8, uncertainty_methods_foundation_scale 7/12, ranking_instability_reweighting 2/5, negative_results_nulls 8/10, metric_validity_general 4/5, vlm_evaluation_shortcuts 6/10.

## 8. Caveats / handoff to later judges & Consolidator

1. **Novelty unverified everywhere.** This pass removed internal redundancy only. Prior-art search is the next gate; the kept-but-flagged permutation ids and every "verify prior art" note should be first in line.
2. **kill_or_merge ≠ bad idea.** Merge targets say where content folds; the Consolidator may resurrect a merged id if it disagrees with the grouping.
3. **Deliberate tensions kept:** dg27 (A-014 vs B-031) and the A-076/B-033 threshold pair are complementary-opposing claims kept as designed head-to-heads.
4. **Not judged here:** feasibility/compute triage (gen A flagged A-032, A-102 as compute-heavy; A-089 killed partly on that basis), impact ranking, and Stage-2 selection.
