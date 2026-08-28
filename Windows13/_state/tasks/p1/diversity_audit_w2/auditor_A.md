# P1 Diversity Audit round 2 — Auditor A (mode collapse / crowding / permutation)

- **Windows**: Windows13 (locked, `windows_path: Windows13`) — identity untouched.
- **Role**: `auditor_A_mode_collapse`, independent, read-only against canonical state. This audit modified **nothing** in `ideas_master.jsonl`, `research_state.json`, `research_ledger.md`, or `window.lock.json`.
- **Audited set**: `Windows13/_state/ideas_master.jsonl`, **494 records**, from `origin/cursor/p1-wave-b-consolidator-w2-3111` (commit `929445dd130fa6b094024e7b00df42b7af6b04c6`). Shards: gen_a 94, gen_b 85, gen_c 69 (wave1, 248) + gen_d 79, gen_e 79, gen_f 88 (wave2, 246).
- **Method**: deterministic regex/count analysis over all idea text fields of all 494 records (judge metadata read separately, never counted as idea text), full pairwise token-Jaccard over one-liners (121,771 pairs), plus tallies of judge A permutation flags and judge C template-family fingerprints already attached to the records. Reproducible; no records modified. Prior w1 audit read for baseline deltas only, not copied.
- **Audited at**: 2026-08-28T20:40:40Z.

## 1. Mode-collapse verdict at 494

| Axis | w1 verdict (248) | w2 verdict (494) | Evidence |
|---|---|---|---|
| Lexical/surface | LOW | **LOW** | EVIDENCE: max pairwise one-liner token-Jaccard 0.282 (`W13-P1-E-034` vs `W13-P1-E-047`); **0** pairs >= 0.33 across all 121,771 pairs |
| Structural/territory | HIGH | **MEDIUM (improved)** | EVIDENCE: SAM subject-share fell 35.1% -> **17.6%** (below the 25% target already; wave2 added ~0 SAM-subject records); eval/measurement cluster-share fell 43.5% -> **31.4%**; 65 clusters, largest = 13/494 (2.6%). BUT annotation/convention pathology rose to **39.3%** mention-share and new wave2-born template families crowd (section 3) |
| Genre | HIGH | **HIGH (persisting, slightly worse in wave2)** | EVIDENCE: 494/494 records carry the contrarian schema (`community_default_belief` + `why_it_might_be_wrong`); constructive-phrased one-liners 1/494 by strict regex; wave2 loose-constructive **12/246 (4.9%)** vs wave1's loose 46/248 (18.5%, auditor B w1 hand-label). Debunk monoculture persisted because gen_d/e/f were generated BEFORE the w1 guards existed |

KNOWN FACT (timeline): wave2 shards D–F were dispatched before the w1 diversity audit, so w1 anti-crowding guards could not have shaped them; guard compliance is only enforceable from gen_h onward. This audit therefore separates "guard violated" from "guard predates shard".

## 2. Crowded / overcrowded clusters (action-ordered)

1. **annotation_convention_pathology** — cross-shard, 6/6 shards. EVIDENCE: 194/494 (**39.3%**) mention annotation/rater/label-noise/ground-truth/pseudo-label (w1: 38.3%; wave2 added 92 more: gen_d 35, gen_e 31, gen_f 26); direct clusters `label-noise` 9, `annotation-label-noise` 7, `human-baselines-annotation` 7, `medical_ambiguity_ground_truth` 8, `data_and_annotation_protocols` 6; judge C family `annotation_ceiling_conventions` = **13**, the largest fingerprint cell in master (cap is 6). w1 said stop_feeding; wave2 kept feeding (pre-guard). **Action: ESCALATE to HARD BAN as primary subject/cluster in gen_m..gen_p and all later shards.**
2. **eval_measurement_super_cluster** — portfolio macro-genre. EVIDENCE: 155/494 (**31.4%**) by cluster-name classification (was 43.5%); wave2 still added 40 (gen_d 13, gen_f 25, gen_e 2); 356/494 (72.1%) mention benchmark/eval/metric somewhere. Improving but still the largest macro-territory. **Action: keep no-new-eval-critique-generator rule; <= 20% eval-critique per shard.**
3. **detection subject** — NEW saturation (expected: gen_d's mandate). EVIDENCE: 151/494 (30.6%) mention detection; 76/79 of gen_d is detection-subject; `small-dense-objects` 13 + `fm-failure-modes` 13 are the joint-largest clusters in master. **Action: detection-primary territory is now saturated; no more detection generators.**
4. **open-vocab / VLM dense** — NEW shard-level saturation. EVIDENCE: 111/494 (22.5%) mention open-vocab/VLM/vision-language; 70/79 of gen_e. **Action: saturated; in-flight gen_l must keep its guard (target the LLM/agent loop, not the VLM itself).**
5. **synthetic-data engines** — gen_f fixation contained to its mandate. EVIDENCE: 121/494 (24.5%) mention synthetic; 74/88 in gen_f; gen_f clusters `synthetic-vs-real-pretraining` 11 + `sim-to-real` 10 + `data-centric-curation` 10 + `generative-data-engines` 10; judge C family `realism_not_the_active_ingredient` = **12** (cap 6 exceeded). **Action: territory owned-and-closed by gen_f; gen_n's anti-overlap guard is now critical; ban "realism/fidelity is not the active ingredient" framing outside gen_f.**
6. **calibration_uncertainty** — still crowded, 6/6 shards. EVIDENCE: 102/494 (20.6%) mention calibration/uncertainty/abstention (wave2 added 36: gen_d 14, gen_e 13, gen_f 9 — pre-guard); 31 direct wave1 cluster ideas unchanged. **Action: keep the w1 BAN (primary-cluster level).**
7. **small/dense/crowded/counting** — NEW cross-shard convergence. EVIDENCE: 68/494 (13.8%) across all 6 shards (gen_d 27, gen_e 13, gen_f 12); judge C family `density_crowding_counting` = 7. **Action: WATCH; cap as primary cluster at <= 5 per new shard.**
8. **"X is a free/cheap predictor of Y" genre** — NEW cross-shard template (successor of w1's F3 internal-score-as-free-detector). EVIDENCE: 27/494 (5.5%) match free/cheap/zero-cost-predictor phrasing, present in ALL 6 shards (E 7, A 6, D 5, F 5, B 3, C 1); judge A permutation family `proximity_predicts_performance` 7; judge C `cheap_predictor_of_outcome` 7. **Action: WATCH; cap <= 3 per new shard.**
9. **equalization / matched-budget-null family** — NEW, judge-fingerprinted. EVIDENCE: judge C `equalization_null_hidden_budget` 9 + `tf10_hidden_variance_term` 7 (both exceed the 6-cap); my stricter regex catches only 2, so the crowding is at template level, not phrasing level. **Action: cap "gains vanish under matched budget X" as primary framing at <= 3 per new shard.**

Fingerprint-cap status: **14 judge-C template families already exceed the <= 6 accepted-per-cell cap** (top: annotation_ceiling_conventions 13, realism_not_the_active_ingredient 12, tf03_silent_capability_erosion 10, tf04_sam_plus_x_ports 10, equalization_null_hidden_budget 9). The cap was defined at w1 but wave2 records predate it; enforce it at judge time from gen_g/h onward AND as a selection-time cap at the 200->50 cut.

## 3. SAM+X / LoRA+X / permutation axes

- **SAM+X: FROZEN.** EVIDENCE: 87/494 (17.6%) mention SAM/SAM2 — the identical 87 records from wave1 (86 gen_a + 1 gen_b); wave2 added **zero** SAM-subject records. Judge C `tf04_sam_plus_x_ports` = 10 accepted, all gen_a legacy; judge A `sam_plus_x_ports` flags = 9, all `W13-P1-A-*`. Running master SAM share is already below the w1 25% target. **Keep the <= 5% per-shard cap (10% for in-flight gen_k only). Flag: guard_held.**
- **LoRA+X: CONTAINED.** EVIDENCE: 25/494 (5.1%) mention LoRA, all gen_a; zero wave2 growth. PEFT/adapter/fine-tuning mentions 87/494 (17.6%), mostly incidental outside gen_a. **Flag: contained_no_action.**
- **loss+X: STILL CLEAR.** EVIDENCE: 4 accepted records carry judge A `loss_plus_x_family` flags (`W13-P1-A-101`, `B-003`, `B-018`, `B-034`), all wave1; no wave2 growth. Objective-function science remains open for queued gen_m under its HARD ban on add-loss-term-X-to-task-Y permutations.
- **NEW permutation axis — wave1-template ports.** EVIDENCE: judge A flagged **73/246 (29.7%)** of accepted wave2 records with `permutation_family:*` flags and **39/246 (15.9%)** as `wave1_family_adjacent` (wave1 critique templates re-instantiated on detection/VLM/synthetic subjects, e.g. `convention_scoring_template` 9, `teacher_bias_inheritance` 6, `oracle_decomposition_template` 6, `hidden_budget_confound` 5, `scaling_law_template` 5). These were accepted as distinct hypotheses, but they are the top prior-art/novelty risk. **Action: (a) novelty gate prioritizes these 73; (b) new-shard guard: porting a wave1 critique template to a new subject requires a subject-native mechanism claim, else judges kill as permutation.**

## 4. Missing contrarian vs missing constructive

**Missing constructive is the larger deficit and it worsened in wave2.** EVIDENCE: strict constructive-phrased one-liners 1/494 (regex); wave2 loose-constructive 12/246 (**4.9%**) vs wave1's loose 46/248 (18.5%); 494/494 remain contrarian-schema; 57/494 carry judge dissents concentrated in the adversary judge, consistent with genre monotony. The w1 genre quota (>= 25% constructive per shard) never applied to D–F. **Consequence: queued gen_p (>= 80% constructive mandate) is the single highest-leverage remaining shard — elevate it from priority 8 to first dispatch of the remaining queue.** If the wave3 audit still shows < 10% loose-constructive at master level, commission a second constructive shard (see gen_q-reserve note below).

**Missing contrarian belief-targets still unchallenged at 494** (HYPOTHESIS: these community defaults remain untested in-portfolio; counts are EVIDENCE):

| Unchallenged belief target | Coverage at 494 | Owned by |
|---|---|---|
| Scaling orthodoxy (bigger models/data always help) | 0.6% | queued gen_n |
| Emergence claims in vision FMs | 0.4% | queued gen_n (add explicitly) |
| Optimizer/schedule/training folklore | 2.8% mentions, no dedicated cluster | queued gen_m |
| Memorization/privacy | 1.2% | queued gen_n |
| 3D-consistency of 2D foundation features | 0.8% | in-flight gen_k |
| Human-vision / psychophysics contrasts | 1.6% | **unowned** (fold into gen_q or gen_r below) |
| Test-time compute/adaptation orthodoxy | 0.2% | **unowned** -> proposed gen_q |
| Active-learning / data-acquisition folklore | 0.6% | **unowned** (fold into gen_q) |
| Cross-field transfer claims (audio/time-series/graphs) | 0.0% | **unowned** -> proposed gen_r (w1 deferral rule triggers) |
| Underwater/sonar 0.0%, microscopy 0.4%, document/OCR 0.2%, remote sensing 1.8% | near-zero | queued gen_o |

## 5. Recommended next territories (no reuse of in-flight letters gen_h, gen_j, gen_k, gen_l; gen_i stays deferred since gen_h filled restoration)

Re-prioritized remaining w1 queue (letters unchanged, content confirmed still-valid at 494):

1. **gen_p_constructive_capability** — elevate to priority 1 (was 8). Genre deficit is the dominant collapse axis (4.9% loose-constructive in wave2). Guards unchanged (>= 80% constructive, 0% pure-audit, <= 10% SAM).
2. **gen_o_hard_domain_diversifier** — priority 2. Underwater/sonar 0.0%, microscopy 0.4%, document/OCR 0.2%, remote sensing 1.8%, agriculture ~0.2% at 494; medical is 11.1% so the <= 25% medical cap has headroom. Add explicit document/OCR emphasis. Smoke/fire/transparent HARD BAN stands.
3. **gen_m_training_dynamics_objectives** — priority 3. Training-dynamics coverage 4.0%; loss+X permutation volume still zero, so the territory is both empty and guard-protected.
4. **gen_n_scaling_memorization_data_laws** — priority 4. Scaling laws 0.8%, memorization 1.2%; STRENGTHEN the anti-overlap guard: gen_f now owns 60 synthetic-engine records and the `realism_not_the_active_ingredient` + `scaling-and-economics` clusters; gen_n must frame data/scale-level interventions, never generation pipelines; add emergence-claims audit to its mandate.

Proposed ADDITIONAL generators toward 1000 (fresh letters; a–p all burned/in-flight/queued/deferred):

5. **gen_q_test_time_compute_adaptation** (NEW, priority 5) — test-time training/adaptation/augmentation laws, inference-time compute scaling for perception, test-time search/ensembling, TTA failure modes under real shift; fold in active-learning folklore and psychophysics-style human-model contrast designs. Coverage today: 0.2%/0.6%/1.6%. ANTI-OVERLAP guard: in-flight gen_l owns LLM/agent-orchestrated loops; gen_q owns non-LLM test-time mechanisms for dense/detection models; <= 5% SAM; annotation-pathology hard ban applies.
6. **gen_r_cross_field_transfer** (NEW, priority 6) — vision <-> audio/time-series/graphs/scientific-imaging transfer science. The w1 deferral rule said revisit "if wave3 leaves cross-field coverage at ~0" — it is 0.0% at 494, and both wave3 in-flight shards (h/j/k/l) leave it untouched, so the trigger condition is effectively met early. Guards from w1 deferral apply verbatim: each idea names both fields AND the transferred invariance/structure; hard ban on bare apply-architecture-X-to-field-Y permutations.
7. **gen_s_embodied_interactive_perception** (RESERVE, priority 7) — embodied/robotic/active perception + interactive human-in-the-loop vision (w1-deferred `embodied_robotics`; 3.2% loose mentions, no dedicated cluster; `interaction_loops_human_factors` has only 5). Commission after gen_q/gen_r if the acceptance rate holds.
8. **gen_t_efficiency_deployment_science** (RESERVE, priority 8) — quantization/pruning/distillation/latency laws as science, non-SAM (w1-deferred; only ~5 dedicated records despite 9.7% loose mentions). Commission only if the 1000-margin erodes (see capacity math).

Capacity math toward 1000 (HYPOTHESIS — arithmetic on EVIDENCE inputs): master 494. In-flight raw ~500 (gen_g 100 generated + gen_h, gen_j, gen_k, gen_l ~100 each) at the observed blended acceptance 494/604 = 81.8% -> ~409 -> **~903**. Remaining queue gen_m..gen_p ~400 raw -> ~327 -> **~1230**, clearing 1000 with ~230 margin. gen_q + gen_r add ~164 more (~1394) and close the remaining blind spots. Conclusion: the 1000 target is reachable with the existing queue alone; gen_q/gen_r are recommended for diversity margin, gen_s/gen_t held in reserve against acceptance-rate dips below ~70%.

## 6. Guard updates for gen_m..gen_p and beyond (delta to w1 guard set)

- **ESCALATE**: annotation/convention/label-noise pathology from stop_feeding to HARD BAN as primary subject (39.3% mention-share; largest fingerprint cell 13/6-cap).
- **ADD**: cap "X-is-a-free/cheap-predictor-of-Y" ideas at <= 3 per shard (27 already, all 6 shards).
- **ADD**: cap equalization/matched-budget-null primary framing at <= 3 per shard (fingerprint cells at 9 and 7).
- **ADD**: ban "realism/fidelity is not the active ingredient" framing outside gen_f (cell at 12).
- **ADD**: wave1-template-port rule — re-instantiating a wave1 critique template on a new subject requires a subject-native mechanism claim (73/246 wave2 accepts are permutation-flagged; 39 wave1-adjacent).
- **KEEP**: SAM <= 5% (10% gen_k), calibration primary-cluster ban, smoke/fire/transparent hard ban, >= 8 sub-clusters/none > 15% (note: gen_d's largest cluster hit 16.5% — pre-guard, flagged not sanctioned), >= 25% constructive floor, <= 40% pure-debunk ceiling, fingerprint cap <= 6 now ALSO enforced at Stage-2 selection.
- **QUALITY GATES still unmet in wave2 (pre-guard)**: numeric kill thresholds ~0/246 (8 records contain any digit in `falsifiable_prediction`, none a clean threshold); structured `evidence_label` dict 0/246 (wave1: 94/248, gen_a only). gen_h onward must comply; wave2 records need schema backfill before Stage 2 ranking.

## 7. Citation integrity

EVIDENCE: 13 citation-like strings in the 494-record master, all in wave1 gen_a `prior_work_basis` fields, all real well-known papers (verified at w1: SAM, SAM2, LoRA, VPT, MAE, BitFit, model soups, task arithmetic, DETR, texture-bias, registers, SAM-HQ, CKA). **Wave2 added zero citation strings. Zero fake citations found. This audit adds no citations.**

## 8. Scope compliance

- Canonical files untouched: `ideas_master.jsonl`, `research_state.json`, `research_ledger.md`, `window.lock.json`.
- Files written: only `Windows13/_state/tasks/p1/diversity_audit_w2/auditor_A.{md,json}` and `done_auditor_A.json`.
- Own branch `cursor/p1-diversity-audit-w2-auditor-a-7ef7`; no force-push; Windows13 identity unchanged.
