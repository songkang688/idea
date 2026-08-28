# P1 Diversity Audit — Wave 2 — Auditor B (hypothesis quality / blind spots)

- **task_id:** `p1_diversity_audit_w2`
- **role:** `auditor_B_quality_blindspots`
- **windows_id / windows_path:** Windows13 / Windows13 (window_locked: true)
- **branch:** `cursor/p1-diversity-audit-w2-auditor-b-0688`
- **audited set:** `Windows13/_state/ideas_master.jsonl` @ `origin/cursor/p1-wave-b-consolidator-w2-3111` (commit `929445dd130fa6b094024e7b00df42b7af6b04c6`), **494 records** (wave1 248: gen_a 94, gen_b 85, gen_c 69; wave2 246: gen_d 79, gen_e 79, gen_f 88)
- **audited_at_utc:** 2026-08-28T20:50:27Z
- **independence:** Auditor A wave2 output was fetched-for (`git fetch origin` + tree scan of every origin branch for `Windows13/_state/tasks/p1/diversity_audit_w2/done_auditor_A.json`) and was **not present at audit time**; this audit is fully independent of Auditor A w2.
- **method:** deterministic regex/count analysis over all fields of all 494 records; manual read of all 246 wave2 one-liners with hand-labeled genre classification; judge-meta aggregation (feasibility tiers, duplicate groups, template families); off-master tree inspection of in-flight shards gen_g/h/j/k on their origin branches. No canonical state files modified. No citations invented.

---

## 1. Falsifiability quality (wave2 vs wave1)

| metric | wave1 (248) | wave2 D/E/F (246) | verdict |
|---|---|---|---|
| all 11 prose fields present & substantive | 248/248 | 246/246 | PASS |
| hedge words (might/may/could) in prediction | 0 | 0 | PASS |
| explicit "falsified if / fails if" clause in prediction or minimal experiment | 149/248 (60%) | **0/246 (0%)** | **REGRESSION** |
| numeric kill threshold in falsifiable_prediction | 2–4/248 (~1.6%) | 4/246 (1.6%) | UNCHANGED (bad) |
| vague-magnitude-only predictions ("substantially", "large", "strong" with no number) | 87/248 (35%) | 89/246 (36%) | UNCHANGED (bad) |
| structured `evidence_label` dict | 94/248 (gen_a only) | **0/246** | **REGRESSION** |
| inline bracket evidence tags | gen_b/c partial | 246/246, uniformly on exactly 5 fields (problem, core_hypothesis, falsifiable_prediction, why_possibly_novel, community_default_belief) | consistent but wrong schema |

**Finding B1 (top falsifiability defect, wave2): the kill condition went implicit.**
Wave1 records (91 of them) wrote "falsified if X" into the minimal experiment; wave2 predictions are directional `[EXPECTED RESULT]` statements ("will show a strong monotone relationship") that never state what outcome kills the idea. Only 4/246 (`W13-P1-D-026`, `W13-P1-E-058`, `W13-P1-F-020`, `W13-P1-F-082`) carry any numeric threshold. Kill adjudication of "strong/large/most" is left to future judges' taste, exactly the failure the w1 audit gate ("every falsifiable_prediction must carry a numeric kill threshold") was written to prevent. Wave2 D/E/F were **generated before** that gate existed (shards were on origin before the w1 audit closed), but the wave2 judges/consolidator did **not retrofit** thresholds either.

**Finding B2: evidence-label schema is now fragmented four ways** — gen_a structured dict, gen_b/c sparse inline tags, wave2 uniform 5-field inline tags, and in-flight gen_j (structured dict + `genre` + `family_fingerprint` + `needs_special_resources` + `seg_metric_dependent`) vs gen_k (`evidence_labels` + separate `kill_threshold` field). Programmatic Stage-2 readers currently see 400/494 master records as schema-less. Wave2's inline tags map 1:1 to the dict (5 tagged fields, all 246 records) and can be normalized mechanically by a consolidator.

**Finding B3: experiments are runnable-but-underspecified.** Judge B marked 244/246 `runnable_as_stated`, yet wave2 experiment fields name almost no concrete model or dataset (1 named-system mention in all 492 experiment fields; wave1 gen_a named SAM/COCO-class systems freely). "A standard open-vocabulary benchmark" leaves dataset choice as a hidden degree of freedom — a benchmark-shopping risk when these are actually run. Zero fake-citation risk is the flip side: **0 citation-like strings in all 246 wave2 records; 0 fake citations found in master** (wave1 finding of 13 real citations in gen_a unchanged).

## 2. Cheap-kill quality

- Explicit time/cost bound in fastest_falsification_experiment: wave2 **129/246 (52%)** vs wave1 144/248 (58%). Per shard: gen_d 54/79, gen_e 57/79, **gen_f 18/88 (20%) — worst in portfolio**; gen_f fastest tests routinely require training runs whose cost is never stated.
- Feasibility tiers (judge B): wave2 is cheaper than wave1 — T1 (inference/analysis-only) 167/246 = 68% (wave1: 39%), T2 78, T3 (gated/expensive) 1 (wave1: 6). `runnable_as_stated` 244/246.
- Special-resource fastest tests (raters/clinicians/exotic sensors): wave2 **0/246** (wave1: 32) — real improvement, partly a side effect of domain-generic phrasing.
- Redundancy hygiene: 0 judge-A duplicate groups with ≥3 accepted members; max pairwise near-duplication not re-measured here (w1: LOW) but one-liner read found no near-duplicates.
- **Finding B4:** cheap-kill is structurally good (cheap tiers, no gated resources) but **adjudication-poor** (B1): a T1 test without a pre-registered kill threshold produces a plot, not a verdict.

## 3. Constructive vs debunk balance after adding D/E/F

Hand-labeled genre of all 246 wave2 one-liners (labels are auditor judgment — HYPOTHESIS; counts over those labels — EVIDENCE):

| shard | clear constructive (capability/fix/recipe/decision-rule payload) | borderline | clear % | w1-audit ≥25% floor* |
|---|---|---|---|---|
| gen_d | 13/79 (D-018/024/045/046/050/054/065/072/074/078/079/082/083) | 9 | 16.5% | fail |
| gen_e | 17/79 (E-004/009/029/033/039/040/046/048/049/050/058/072/074/075/080/081/086) | 8 | 21.5% | marginal fail |
| gen_f | 32/88 (F-003/005/008/009/010/014/019/021/023/034/036/041/043/046/054/059/060/065/066/070/071/072/073/074/075/077/078/083/089/092/096/100) | 14 | 36.4% | pass |
| **wave2 total** | **62/246 (25.2%)** | 31 (upper bound 93 = 37.8%) | | |

\* the floor postdates D/E/F generation; recorded as calibration, not as a violation.

Strict-constructive (auditor C's w1 criterion — capability is the primary contribution, not a fix bolted onto a debunk): ≈ **22/246 (8.9%)**: D-045, D-050, D-054, D-072, D-078, D-079, D-082, D-083, E-009, E-074, E-080, F-014, F-041, F-046, F-054, F-059, F-066, F-070, F-071, F-078, F-083, F-096.

Portfolio after wave2: strict-constructive ≈ 29–33/494 (**6–7%**, up from 3–4%); loose ≈ 108/494 (**21.9%**, up from 18.5%); debunk/audit genre ≈ 58–62% of wave2 (wave1: ~60%). In-flight shards self-report better balance (gen_j `genre`: 37/104 constructive, 10 audit_debunk; gen_k: 34/105 constructive, 27 debunk_audit) — the genre quota is working where it was applied.

**Finding B5: the debunk skew is improving but the portfolio is still ~3:1 debunk-vs-strict-constructive; gen_p (≥80% constructive mandate) remains justified. The 62-id wave2 clear-constructive list above should be protected from genre-blind culling in Stage 2, extending the w1-protected 46-id list to 108 ids.**

Guard compliance snapshot (w1 global guards, measured on wave2 accepted): SAM-subject 0/246 → master SAM share fell 31.9% → **16.0%** (below-25% target met); calibration/uncertainty one-liners 8/246 (3.3%, ban respected); seg/mask-metric-bound falsifications 14% of wave2 (30%-independence guard met; note 15% is detection-AP-bound — expected for gen_d); structure quota met for gen_e (11 clusters, max 13%) and gen_f (10, max 12%), marginal for gen_d (9 clusters; small-dense-objects and fm-failure-modes at 16% vs 15% cap).

**Finding B6: the w1 family-fingerprint guard (≤6 accepted per fingerprint cell) was never operationalized — 0/246 wave2 records carry fingerprint tags.** Judges tracked informal template families instead, and several exceed the cap across shards: judge_C `template_families` — annotation_ceiling_conventions 13, realism_not_the_active_ingredient 12, equalization_null_hidden_budget 9, pseudo_label_bias_inheritance 8, input_geometry_artifacts 7, density_crowding_counting 7, cheap_predictor_of_outcome 7; judge_A permutation families — convention_scoring_template 11, content_over_realism_factorial 10, proximity_predicts_performance 7, hidden_budget_confound 7, teacher_bias_inheritance 7, oracle_decomposition_template 6, consistency_self_audit 6. These are wave2's analog of wave1's F1–F5 template families. Proposed Stage-2 selection-time caps (T6–T11): T6 cheap-predictor-of-outcome/proximity-predicts-performance keep ≤5; T7 teacher/pseudo-label bias-inheritance keep ≤4; T8 realism-not-the-active-ingredient/content-over-realism keep ≤5; T9 annotation/convention-ceiling scoring keep ≤5; T10 equalization-null/hidden-budget keep ≤4; T11 oracle-decomposition keep ≤3 (cap values HYPOTHESIS — consolidator/Stage-2 to tune).

## 4. Missing territories vs remaining queue gen_m/n/o/p

Off-master awareness applied: gen_g (domain shift, 100, incl. 15 TTA-primary), gen_h (SR/restoration, 100), gen_j (diffusion science, 104), gen_k (3D/geometry/video, 105) verified present on origin branches; gen_l (LLM/agent vision) in flight per dispatcher. None re-recommended here.

- **gen_m (training dynamics / objective science): mandate INTACT.** Core territory (optimizer/schedule folklore, fine-tuning dynamics, loss-landscape science, objective design with mechanism) still ~empty. Wave2 added only adjacent records requiring an anti-overlap guard: D-031 (loss-reweighting = calibration), D-050 (mask-derived objectives), E-075 (boundary-aware assignment), E-076 (tower-freezing asymmetry), F-036 (soft-vs-hard labels = teacher calibration), F-048 (source-level scheduling), F-058 (objective choice vs data provenance), F-089 (batch decorrelation), F-095 (vintage ordering).
- **gen_n (scaling/memorization/data laws): mandate PARTIALLY COLONIZED by accepted gen_f — tighten guards before dispatch.** Data-scaling corner taken: F-045 (pruning inverts with scale), F-051 (procedural pretraining saturates), F-057 (real-anchor fraction shrinks with scale), F-097 (joint real-synthetic scaling law; absorbed F-025), F-098 (support-saturation plateau), F-101 (repetition-vs-synthesis crossover). Memorization corner taken: F-060 (generator fingerprints), F-086 (generator memorization leaks benchmarks), F-093 (privacy leakage of generators). **Residual gen_n territory (still empty): model/compute scaling laws of vision FMs, dense-task transfer scaling, emergence claims, memorization in discriminative/dense models, membership inference on vision FMs, privacy of dense features, real-data composition laws.** Add the 9 ids above to gen_n's anti-overlap ban list.
- **gen_o (hard-domain diversifier): mandate FULLY INTACT — highest-value remaining queue item.** Wave2 is domain-generic; domain-native records ≈ 6 (D-026 aerial/microscopy scale statistics, F-020/F-026 driving, F-022 robotics, F-009/F-080 human-centric). Underwater/sonar 0, microscopy/histology-primary 0, remote-sensing-primary 0, agriculture 0, document/OCR-primary 0, industrial-inspection 0. Medical-primary in wave2 ≈ 0, so portfolio medical share fell to ~12% — the ≤25% medical cap is easily satisfiable.
- **gen_p (constructive rebalancer): STILL JUSTIFIED, urgency reduced.** Portfolio strict-constructive is 6–7%; but wave2 (25% clear) and in-flight gen_j/k (32–36%) show organic improvement. Keep ≥80% constructive mandate; consider pointing gen_p at the debunk-heaviest clusters (detection-eval pathology, annotation conventions) for debunk-to-repair conversion.

**Recommended dispatch order: gen_o → gen_m → gen_n (with updated guards) → gen_p.**

## 5. Remaining blind spots (near-zero across 494 + all off-master/in-flight shards)

1. **Efficiency/deployment science** (quantization, pruning, distillation-as-science, latency/accuracy laws for dense prediction): 2 wave2 primary (F-045, F-052), deferred at w1, owned by no in-flight shard.
2. **Model lifecycle / continual updating** (version drift, regression testing across model updates, continual learning, dataset/model half-life): 1 primary (F-102; F-069 adjacent).
3. **Security** (adversarial robustness of dense/open-vocab systems, backdoors, data poisoning incl. synthetic-data supply-chain attacks): ~1 primary (D-059 typographic transfer; F-044 shortcut-injection adjacent).
4. **Fairness / geographic-demographic performance disparity** for dense prediction: 0 primary, ~3 incidental mentions in 494.
5. **Human-vision/psychophysics alignment** as mechanism (crowding, subitizing, perceptual metrics vs model behavior): ~2 seeds (D-018, D-081, D-080, D-096 adjacencies).
6. **Cross-field transfer** (vision ↔ audio/time-series/graphs/scientific imaging): still 0 — w1 deferral condition ("revisit if wave3 leaves it ~0") not yet triggered since wave3 (gen_h/j/k/l) is unjudged; keep deferred, re-check at audit w3.
7. **Embodied/robotic perception:** 1 primary (F-022); w1 deferral stands.

Suggested fresh letters (no collision with a–p; letters q+ are free on all origin branches as of this audit): **gen_q_efficiency_deployment_science** (priority 1 of the new set; anti-overlap: F-052 distillation ceiling, teacher-student block F-028/F-031/F-035/F-036), **gen_r_model_lifecycle_updating** (priority 2; seeds F-102/F-069; distinct from gen_m's within-run dynamics), **gen_s_security_dense_prediction** (priority 3; includes constructive forensics angle extending F-060), then gen_t_fairness_geographic and gen_u_human_vision_psychophysics as bench candidates for the next audit. Commission after (or interleaved with) gen_m/n/o/p — the queue plus in-flight shards already add ~800–900 gross ideas toward the 1000+ target.

## 6. Process findings for the consolidator

- **Gate adoption is inconsistent across in-flight wave3 shards** (checked on their origin branches): gen_j complies fully (98/104 numeric thresholds, 104/104 structured evidence_label + genre + family_fingerprint + needs_special_resources + seg_metric_dependent); gen_k complies via divergent schema (105/105 separate `kill_threshold` field, `evidence_labels`, genre, fingerprint); **gen_h: 0/100 on every gate** (no thresholds, no structured labels, 2/100 time bounds); gen_g (pre-audit): 0/100 gates, 69/100 time bounds. Wave3 judges must either retrofit kill thresholds for gen_g/gen_h at judge time or grade them under the wave2 (gateless) standard explicitly.
- **Adopt gen_j's record schema as canonical** going forward; mechanically backfill wave2's uniform inline tags into structured dicts at the next consolidation; declare per-record `kill_threshold` (gen_k style) acceptable iff mirrored into falsifiable_prediction.
- **Novelty debt:** 494/494 accepted ideas remain `novelty_status=unverified`; only 2 surviving records carry judge prior-art-risk flags (D-001, E-031) and 2 known-result restatements were killed (E-035, F-053). Judge instinct is the only prior-art filter so far. Recommend a prior-art triage lane (sample ~10% per shard, verify against real literature, no invented citations) before Stage 2 ranking.

## 7. Compliance

- Files written: only `Windows13/_state/tasks/p1/diversity_audit_w2/auditor_B.{md,json}` + `done_auditor_B.json`.
- NOT touched: `ideas_master.jsonl`, `research_state.json`, `window.lock.json`, ledger, any generator/judge file.
- No fake citations in this audit; all prior-art remarks are judge/auditor HYPOTHESES and labeled as such.
- Own unique branch, no force-push.
- recommended_next_task_type: `p1_diversity_audit_w2_C_or_consolidator`.
