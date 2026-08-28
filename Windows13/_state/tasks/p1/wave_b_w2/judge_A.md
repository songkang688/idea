# P1 Wave B — Judge A: Hypothesis-Level Dedup (Wave 2: Generators D+E+F)

- **task_id:** `p1_wave_b_w2` | **role:** `judge_A_dedup` | **windows_id:** `Windows13` (locked)
- **branch:** `cursor/p1-wave-b-w2-judge-a-dedup-13e5`
- **Scope:** cross-shard dedup at the hypothesis level for the SECOND generator wave (D+E+F only), near-duplicate clustering, permutation/template flagging, cross-wave collision flagging against the already-accepted wave-1 master, accepted-candidate list for THIS wave only. Canonical state (`ideas_master.jsonl`, `research_state.json`, `window.lock.json`) untouched — the wave-1 master was read for collision flagging and NOT rewritten.
- **Epistemic status:** NO novelty is verified for any kept idea. Every "prior-art risk" and "known result" remark below is the judge's unverified HYPOTHESIS. No citations were invented.

## 1. Inputs

| Shard | Branch | Ideas | done.json status |
|---|---|---|---|
| gen_d_object_detection | `cursor/p1-gen-d-object-detection-07a3` | 100 (W13-P1-D-001..100) | done |
| gen_e_vlm_dense_prediction | `cursor/w13-p1-gen-e-vlm-dense-9412` | 100 (W13-P1-E-001..100) | done |
| gen_f_synthetic_data | `cursor/w13-p1-gen-f-synthetic-data-3a94` | 102 (W13-P1-F-001..102) | done |
| **Total wave-2 input** | | **302** | |
| (reference, read-only) wave-1 accepted master | `cursor/p1-wave-b-consolidator-w1-7a58` | 248 accepted ids (A/B/C) | consolidated |

All 302 lines parsed; IDs contiguous per shard; no cross-shard ID collisions; no ideas invented or renumbered by this judge.

## 2. Method

Each idea was compared on its `core_hypothesis` content (mechanism + falsifiable claim), not title strings — first within and across D/E/F, then against the 248 wave-1 accepted ideas. Two ideas were treated as duplicates when they assert the same mechanism with the same falsification design, differing only in substrate (task, modality, metric, or the "X" slot of a template). Ideas sharing a premise but making distinct falsifiable claims were clustered, not merged.

This wave's analog of wave-1's SAM+X permutation problem is **template instantiation across substrates**: the same schema stamped onto detection, dense prediction, and synthetic data. Twelve template families were flagged (Section 5). Cross-wave, near-verbatim ports of already-accepted wave-1 ideas were killed with the wave-1 id as merge target; family-adjacent ideas were kept but carry explicit wave-1 flags for the novelty judge. High-value non-template ideas were protected as anomalies.

## 3. Verdict Counts

| Quantity | Value |
|---|---|
| Input total | 302 (D: 100, E: 100, F: 102) |
| **Keep (accepted candidates this wave)** | **248** (D: 80, E: 80, F: 88) |
| Kill or merge | 54 (D: 20, E: 20, F: 14) |
| Duplicate groups | 36 (44 of the 54 kills are merges inside these groups) |
| Standalone kills (wave-1 ports / known-result restatement) | 10 |
| Cross-wave collision kills (merge target is an accepted wave-1 id) | 12 |
| Kept ideas carrying wave-1 collision/prior-art flags | 40 |
| Flagged template/permutation ids (kept and killed combined) | 99 |
| High-value anomalies (protected) | 18 |
| Judge clusters (every one of the 302 ids assigned exactly once) | 32 |

Shard F is the strongest per-idea shard but the most template-driven: 14 near-isomorphic instantiations of "factor X beats photorealism, shown by a 2x2 factorial". Shard E is heavily paired with D (the same hypothesis written once for boxes and once for pixels): 10 of the 36 duplicate groups are exact D≡E substrate pairs. Shard D contributed most of the cross-wave collisions, re-deriving wave-1 shard-C evaluation critiques on the detection substrate.

## 4. Duplicate Groups (the ones that matter most)

Cross-shard hypothesis collisions — exactly what this judge exists to catch. Full list with members, primaries, and merge reasons: `judge_A.json → duplicate_groups`.

**D≡E substrate pairs (same hypothesis, boxes vs pixels):** dg01 caption-frequency-governs-open-vocab (keep D-001, merge E-005); dg02 distractor-vocabulary collapse (keep D-002, merge E-025); dg03 no-abstention/nearest-concept relabeling (keep D-003, merge E-026); dg05 text-geometry-predicts-confusions (keep E-047, merge D-005); dg07 attribute binding (keep D-057, merge D-007); dg08 part-queries-return-wholes (keep E-079, merge D-008); dg19 boundary-weighted reranking (keep D-047, merge E-067); dg25 cross-lingual inconsistency (keep E-054, merge D-012); dg12 hierarchy-granularity credit (keep D-038 + E-028, merge D-014); dg13 vocabulary forgetting (keep D-068, merge E-071).

**D≡F / E≡F pairs:** dg32 correlated teacher/foundation errors defeat ensembling (keep D-060, merge F-033); dg35 captioner-fingerprint inheritance (keep F-060 + E-077, merge F-029); dg34 labels-for-real-images beat images-with-labels (keep F-066, merge F-006).

**Within-shard consolidations:** dg04 recognition-dominates (D-071 ⊃ D-004); dg22 easy-regime referring (E-013 ⊃ E-014, E-015, E-020 — the largest single consolidation: skyline baseline, distractor decay, blind prior, and bimodality are one hypothesis); dg16 annotation ceiling (D-096 ⊃ D-017, E-065); dg28 sim-to-real convention/ontology (F-090 ⊃ F-011, F-016); dg30 camera/sensor pipeline (F-019 ⊃ F-013, F-079); dg29 layout-over-appearance (F-077 ⊃ F-004); dg36 joint scaling law (F-097 ⊃ F-025); dg31 injected-noise leaderboard artifact (F-028 ⊃ F-032); dg23 negation (E-052 ⊃ E-016); dg24 missing comparison operation (E-085 ⊃ E-089); dg26 proposal stage dominates (E-002 ⊃ E-064); plus dg06, dg09, dg10, dg11, dg14, dg15, dg17, dg18, dg20, dg21, dg27, dg33.

## 5. Flagged Template / Permutation Families (wave-2's SAM+X)

- **content_over_realism_factorial (14 ids, shard F):** "factor X beats photorealism via 2x2 factorial" stamped over motion (F-003), blending (F-005), occlusion (F-008), sensor noise (F-013, killed), camera pipeline (F-019), label-space (F-021), physics (F-022), assets (F-073), layout (F-077, absorbs F-004), device ISP (F-079, killed), backbone interaction (F-017), umbrella (F-094). Kept members each carry a distinct factor and mechanism; F-094 is the umbrella that makes the family coherent rather than redundant.
- **wave1_critique_ports (13 ids):** accepted wave-1 evaluation critiques re-derived on new substrates. Killed where near-verbatim: D-006→C-052, D-035→C-047, D-087→C-077, D-092→C-028, D-100→C-069, E-021→C-020, E-037→B-046, E-066→C-045, E-070→C-024, F-039→C-058, F-016→B-085 (partial), D-056→A-102. Kept-with-flags: D-059, D-088, D-012 (merged in-wave), F-023.
- **consistency_self_audit (7 ids):** "self-consistency under transform T as free audit/fix" — paraphrase (E-021, killed), synonym (E-029), language (E-054), round-trip (E-022), format (E-096), jitter (D-054), containment (E-081). Wave-1 C-020 is the ancestor; each kept member uses a genuinely different T.
- **hidden_budget_confound (8 ids):** resolution (D-022), inference compute (D-091), preprocessing (E-044), prompt tuning (E-066, killed), augmentation strength (F-015), baseline strength (F-067), tuning effort (F-087), generation compute (F-088). Wave-1 C-045 is the ancestor.
- **missing_operation_wrapper (5 ids, shard E):** ordinal (E-085), complement (E-087), comparative (E-089, killed), connectives (E-090), metric quantities (E-091).
- **proximity_predicts_performance (8 ids):** caption frequency (D-001), web-frequency tail relocation (D-034), lexical rarity (E-030), visual distance (E-031), condition coverage (F-026), generator support distance (F-061), support plateau (F-098).
- **teacher_bias_inheritance (10 ids):** D-056 (killed→A-102), D-100 (killed→C-069), E-072, E-077, F-029 (killed), F-031, F-035, F-055, F-060, F-068.
- **convention_scoring_template (15 ids):** conventions/ontology as hidden error component across D-049/D-053/D-075/D-084/D-094/D-095/E-043/E-068/E-083/F-002/F-011/F-016/F-027/F-037/F-090. Wave-1 ancestors: C-067, B-085, B-075, A-079.
- Also flagged: **rank_transfer_instability** (6), **scaling_law_template** (7), **oracle_decomposition_template** (8), **blind_trivial_baseline** (3).

99 unique ids carry at least one family flag; each kept flagged idea has a mandatory prior-art search note for the novelty judge.

## 6. Cross-Wave Collisions Against the Wave-1 Master (flag only — master untouched)

12 wave-2 ideas were killed as near-verbatim ports of accepted wave-1 ideas (list in Section 5, `wave1_critique_ports`). 40 kept ideas carry explicit wave-1 family or prior-art flags — the highest-risk keeps are E-035 (vs A-039 + registers literature), D-054 (vs B-026/A-005), E-084 (vs B-030), F-040 (vs C-102), E-043 (vs A-079), D-096 (vs C-025/C-066/B-091), F-086 (vs C-023/C-064), E-072 (vs A-102/A-091), and E-074 (vs A-041/A-014). Full map: `judge_A.json → wave1_collision_flags_on_keeps`.

One standalone kill was made on known-result grounds rather than wave-1 grounds: F-053 (accumulate-vs-replace resolves model collapse) restates a result the judge assesses (UNVERIFIED) as established; the consolidator may resurrect it if the novelty judge disagrees.

## 7. High-Value Anomalies (protected, 18)

D-029 (pattern completion in packed layouts), D-051 (nested-instance structural blind spot), D-069 (state-space is the generalization frontier), D-083 (paradigm disagreement finds annotation errors), D-097 (detectors out-localize their training labels), D-099 (contextual self-censorship from sparse annotation), E-010 (masks persist after object inpainted away), E-041 (probes beat the model's own verbalized dense outputs), E-055 (viewer-centric frame-of-reference shared by models and annotators), E-084 (countability grammar controls mask topology), E-095 (reasoning tax on grounding), E-099 (prompt overlays contaminate unmarked predictions), F-027 (pixel-perfect labels transfer worse than convention-matched noisy labels), F-040 (quality filters anti-select dense value), F-060 (generator supply-chain forensics), F-069 (crawl-vintage contamination drift), F-091 (non-monotone realism re-imports spurious correlations), F-096 (students exceed teachers via multi-view fusion).

## 8. Deliberate Tensions Kept (head-to-heads, not redundancy)

1. **D-063 vs E-074** — frozen features lack sub-patch precision (no head closes the high-IoU gap) vs a shallow decoder recovers most of the frozen-vs-fine-tuned dense gap.
2. **F-005 vs D-039** — cut-and-paste sufficiency past a realism threshold vs paste artifacts inflate measured gains.
3. **F-052 vs F-096** — distillation ceiling (exceedance needs an external signal) vs multi-view consistency fusion supplying exactly that signal; a regime-mapping pair.
4. **D-071/D-004 vs D-044** — naming dominates residual error vs proposal recall binds for geometrically atypical classes.
5. **D-077 vs D-020/D-055** — pretraining compute should go to recognition (objectness saturates) vs dense/objectness pretraining wins for small-object transfer.
6. **F-074 vs F-064/F-098** — infinite procedural streams beat fixed datasets vs generator-support ceilings.

## 9. Accepted-Candidate List (this wave)

248 kept ids with cluster assignments, duplicate-group membership, family flags, wave-1 notes, anomaly/tension notes, and copied core fields are in `accepted_shard_A.jsonl`. Machine-readable dispositions (keep_ids[], kill_or_merge_ids[] with targets and reasons, clusters, duplicate_groups, flagged_permutation, wave1_collision_flags_on_keeps, anomaly_ids[], deliberate_tensions) are in `judge_A.json`.

Keep counts by judge cluster (kept/total; 32 clusters cover all 302 ids exactly once): openvocab_vocabulary_dependence 9/11, absence_abstention_scope 5/6, recognition_vs_localization 8/10, text_embedding_geometry 7/8, name_phrasing_multilinguality 3/7, compositional_binding_attributes 4/5, granularity_parts_extent 9/11, context_reliance_cooccurrence 8/10, score_calibration_thresholds 4/5, small_dense_object_mechanics 10/11, counting_density_suppression 9/10, longtail_evaluation_training 3/5, detection_segmentation_pipelines 9/9, foundation_detector_priors_forgetting 8/10, mllm_dense_interfaces 12/12, eval_protocol_statistics 6/10, annotation_limits_conventions 8/13, dense_feature_mechanics 8/10, language_seg_pipelines_training 6/7, referring_relational_grounding 12/16, negation_logic_set_queries 3/5, dense_eval_protocols 3/5, sim2real_content_factors 13/17, sim2real_adaptation_methods 6/6, label_convention_synthetic 6/10, label_noise_learning 6/8, teacher_bias_inheritance 4/7, data_curation_valuation 11/12, synthetic_scaling_economics 9/10, synthetic_pretraining_provenance 10/11, generative_data_engines 15/16, synthetic_eval_contamination 8/9.

## 10. Caveats / handoff to later judges & Consolidator

1. **Novelty unverified everywhere.** This pass removed internal redundancy and cross-wave near-verbatim ports only. The 40 kept-but-flagged ids and every "prior-art check required" note should be first in line for the novelty gate.
2. **kill_or_merge ≠ bad idea.** Merge targets say where content folds (including 12 targets in the wave-1 master); the Consolidator may resurrect any merged id if it disagrees with a grouping — E-073 (training attribution), E-064 (oracle protocols), F-016 (sim-to-real convention re-evaluation), and D-100 (dual-protocol annotation design) are the likeliest candidates for resurrection as experiments attached to their targets.
3. **Deliberate tensions** (Section 8) need adjudication by experiment, not dedup.
4. **Not judged here:** feasibility/compute triage, impact ranking, Stage-2 selection, and any change to canonical state. The wave-1 master remains exactly as the wave-1 Consolidator wrote it.
