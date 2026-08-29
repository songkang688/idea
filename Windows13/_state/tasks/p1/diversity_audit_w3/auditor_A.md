# P1 Diversity Audit round 3 — Auditor A (mode collapse / crowding / permutation)

- **Windows**: Windows13 (locked, `windows_path: Windows13`) — identity untouched.
- **Role**: `auditor_A_mode_collapse`, independent of auditors B/C, read-only against canonical state. Nothing in `ideas_master.jsonl`, `research_state.json`, `research_ledger.md`, or `window.lock.json` was modified.
- **Audited set**: `Windows13/_state/ideas_master.jsonl`, **934 records**, from `origin/cursor/p1-wave-b-consolidator-w4-e8e2` (commit `2411f9307030b8de4e445d0972a0b624cc451130`). Shards: gen_a 94, gen_b 85, gen_c 69 (w1, 248) + gen_d 79, gen_e 79, gen_f 88 (w2, 246) + gen_g 30, gen_h 16 (gate5-repaired subsets), gen_j 98 (w3, 144) + gen_k 102, gen_l 96, gen_m 98 (w4, 296). **440 records added since the last audit at 494** — cadence (+100–200) was overdue; this audit covers the double increment.
- **Method**: deterministic regex/count analysis over the 12 idea-text fields of all 934 records (judge metadata and `family_fingerprint` read separately, never counted as idea text); full pairwise one-liner token-Jaccard (435,711 pairs); tallies of judge_C `template:*` fingerprint flags, judge_A flags/duplicate groups, and judge genre labels; off-master gen_n/o/p enumerated **read-only** for ownership checks. Instrument note: my tokenizer differs slightly from the w2 auditor's (their top pair E-034/E-047 = 0.282 measures 0.250 here), so cross-audit Jaccard deltas are indicative, not exact.
- **Audited at**: 2026-08-29T01:18:41Z. Novelty of all audited ideas remains **UNVERIFIED**; no citations added.

## 1. Mode-collapse verdict at 934

| Axis | w2 verdict (494) | w3 verdict (934) | Evidence |
|---|---|---|---|
| Lexical/surface | LOW | **LOW** | EVIDENCE: max pairwise one-liner Jaccard 0.258 (`W13-P1-L-019` vs `L-040`, shared framing not shared claim); **0** pairs >= 0.33 of 435,711; 124 clusters, largest 14/934 (1.5%) |
| Structural/territory | MEDIUM improved | **MEDIUM (still improving)** | EVIDENCE: every w2 crowded subject diluted — SAM 17.6% -> **9.6%**, annotation pathology 39.3% -> **29.6%**, detection 30.6% -> 22.2%, VLM 22.5% -> 11.9%, synthetic 24.5% -> 17.1%, calibration 20.6% -> 16.5%. Eval/benchmark background stable at 71.7%. New masses (3D/video, training dynamics, LLM-agent, diffusion) sit inside their mandated shards with internal spread within guard (J/K/L/M largest cluster 10.2–13.7%) |
| **Template/fingerprint** | (subsumed under structural) | **MEDIUM-HIGH — NEW dominant axis** | EVIDENCE: 10 judge_C cells over the <=6 cap in the w3/w4 vocabulary alone (section 3); crowding migrated from *subjects* to *single-shard template families* |
| Genre | HIGH persisting | **HIGH, improving but unresolved** | EVIDENCE: 934/934 contrarian schema; strict-constructive 0/934; loose-constructive 101/934 (**10.8%**) — but w3/w4 additions run 13.4% vs 8.5% for the pre-existing 494, and judge_C labels ~28% of w4 constructive; resolution rides on in-flight gen_p |

## 2. Crowded clusters / template families (action-ordered)

1. **gen_m internal template monoculture** — NEW, the headline finding. EVIDENCE: four over-cap cells inside one shard: `ritual_is_mechanism_in_disguise` **19** (largest single-shard cell ever in this portfolio: M-006/007/011/013/014/019/023/024/026/027/031/032/034/047/063/071/076/089/091), `boundary_interior_decomposition` 10, `acquisition_order_phase` 10 (M-051..M-060, a *contiguous id block* — generation-order fixation), `bn_statistics_mechanics` 7. That is 46/98 of gen_m in four templates. **Action: Stage-2 slot caps; future shards hard-cap "celebrated ritual X is mechanism Y in disguise" at <=3.**
2. **cheap/free-predictor-of-outcome** — cross-shard, compounding. EVIDENCE: judge_C cell doubled 7 -> **14** (J 4, G 2, K 2, L 3, M 3); the w2 <=3/shard guard was near-respected per shard (gen_j at 4 violates) yet the portfolio total doubled anyway. **Action: ESCALATE to portfolio freeze — a new instance must displace an existing member at Stage 2.**
3. **annotation/convention pathology** — improving but leaking through a new substrate. EVIDENCE: mention-share fell 39.3% -> 29.6% and gen_m added only 4; BUT gen_l re-fed the banned territory via agent-generated annotation: `agent_annotation_loop` 8/8 (L-051..L-060) + 25 mentions; judge-time hard-ban enforcement fired once (L-054 merged into L-059). **Action: keep HARD BAN; extend its text to name agent/model-generated-annotation substrates explicitly.**
4. **eval/measurement background** — stable at 71.7% mention (was 72.1%). gen_k is the most eval-critique-shaped new shard (96/102 mention; `stratified_eval_hidden_failure` 10/10). **Action: keep no-new-eval-critique-generator + <=20%/shard.**
5. **video/3D memory** — gen_k mandate, now owned: `video-understanding-memory` 14 is the largest cluster in master; `feature-3d-consistency` 12, `gaussian-splatting-science` 11. **Action: territory owned-and-closed; no more 3D/video generators.**
6. **calibration/uncertainty** — 16.5% (down from 20.6%) but `dispersion_as_uncertainty` sits at exactly cap 6 with remand-adjacent members. **Action: keep primary-cluster ban; merge trigger armed for w5_NPO.**
7. **counting/density** — 9.2% (was 13.8%), moved sideways into agent-counting via gen_l. **Action: keep watch, <=5 primary per shard.**

## 3. Fingerprint cells over cap (<=6) — w3/w4 judge vocabulary

`ritual_is_mechanism_in_disguise` 19 (M) · `cheap_predictor_of_outcome` 14 (J/G/K/L/M) · `stratified_eval_hidden_failure` 10 (K) · `boundary_interior_decomposition` 10 (M) · `acquisition_order_phase` 10 (M) · `generator_memorization` 8 (J7+H1) · `agent_annotation_loop` 8 (L) · `hidden_distribution_prior` 7 (K) · `text_interface_lossiness` 7 (L-013..L-019 contiguous) · `bn_statistics_mechanics` 7 (M). At-cap watch: `binding_conditioning_pathologies`, `dispersion_as_uncertainty`, `gradient_conflict_localization`, `decorrelation_active_ingredient` (6 each).

Two caveats. (a) The 14 over-cap **w1/w2-era** cells found at 494 (`annotation_ceiling_conventions` 13, `realism_not_the_active_ingredient` 12, tf03 10, tf04 10, `equalization_null` 9, …) were never consolidated and remain open Stage-2 debt — the two flag vocabularies do not share cell ids, so the true census is 10–24 cells depending on vocabulary merging. (b) The w4 consolidator's own list says 7 still-over-cap cells; my raw master-flag tally says 10 — instrument difference (master flags only vs family definitions incl. remand context), same headline members. Enforcement point stays **Stage-2 slot caps + judge-time merge triggers** — forced merges would override two-judge keep majorities (w4 precedent).

## 4. SAM+X / LoRA+X / loss+X / template ports

- **SAM+X: FROZEN, second consecutive audit.** EVIDENCE: 90/934 (9.6%) — the frozen 87 wave1 records + 3 gen_k (K-068, K-073, K-079: SAM2-memory subjects, within gen_k's 10% allowance). **Keep <=5% default cap.**
- **LoRA+X: CONTAINED.** 31/934 (3.3%): 25 gen_a legacy + 6 incidental (1 J, 5 L).
- **loss+X: BAN HELD through maximum exposure.** gen_m (the objective-function shard) produced zero judge_A `loss_plus_x_family` flags; its pathology is template-level (section 2.1), not add-loss-term permutation.
- **Template ports / novelty debt: OVERDUE.** The w2 novelty priority list (73 permutation-flagged wave2 accepts) was never processed; w4 added 3 outvoted judge_C kills preserved as dissent (K-020, K-069, L-012) plus a 20-id prior-art watchlist; **105/934 records now carry judge_dissent**. The subject-native-mechanism rule is working at judge time (K-079 -> A-052 dissent; K-104 merged to C-077), but GATE-8 is the oldest unpaid debt in the pipeline.

## 5. Missing territories at 934 (and who owns them)

| Territory | Coverage on master | Owner |
|---|---|---|
| Cross-field transfer (audio/time-series/graphs) | **0.0%** — third consecutive audit at zero | **NOBODY** -> gen_r, priority 1 |
| Non-LLM test-time adaptation/compute | strict TTA 1.2%; gen_l owns only the LLM side (`test-time-compute-perception` 10) | UNOWNED -> gen_q |
| Adversarial/security/fairness | 4.3% incidental / 1.1%, zero dedicated clusters | **ORPHANED** (gen_u policy-blocked) -> gen_w |
| Model lifecycle/continual | 7.5% loose, no primary cluster | w2 reserve gen_v |
| Embodied/interactive | 4.5% strict, passive-only adjacency in gen_k | w2 reserve gen_s |
| Efficiency/deployment | 7.4% strict; distillation now part-owned by gen_j/gen_m (`distillation_lossmap` 11) | gen_t, mandate shrunk to non-distillation |
| Psychophysics 1.2% / active learning 0.7% | thin | fold into gen_q (w2 map) |
| Underwater 0.0% / sonar 0.0% / microscopy 0.2% / document-OCR 0.5% / remote sensing 1.1% / agriculture 1.0% | near-zero on master, but **off-master gen_o covers all of these** (12/12/13/12+9/10+9/2 cluster records, enumerated read-only) | in-flight gen_o — do NOT duplicate |
| Scaling 1.0% / memorization-privacy 4.2% / emergence | off-master gen_n covers (22/31/9 cluster records) | in-flight gen_n |

## 6. Recommended next generator letters

Letters unavailable: a–p burned (i retired permanently; **n/o/p in-flight in w5_NPO judging — do not reuse**), u blocked by policy. Free: **q, r, s, t, v, w, x, y, z**.

1. **gen_r_cross_field_transfer** (priority 1, elevated from w2's 6) — the only genuinely zero-coverage territory left. Guards: both fields + transferred invariance named per idea; hard ban on bare apply-X-to-field-Y.
2. **gen_q_test_time_compute_adaptation** (priority 2) — anti-overlap sharpened with evidence: gen_l owns the LLM loop *including* its test-time-compute cluster and iso-budget-null family; gen_q owns non-LLM TTA/TTT/test-time-augmentation laws for dense/detection/geometry models. Folds in psychophysics + active-learning folklore.
3. **gen_w_adversarial_security_fairness** (priority 3, NEW letter) — inherits the mandate of policy-blocked gen_u under a fresh letter (u itself never used). Occupied-ground check vs accepted H-090 mandatory at commissioning.
4. **gen_v_model_lifecycle_continual** (priority 4) — w2 reserve mapping preserved (reserved letters are never re-mapped). Anti-overlap: gen_n owns data-scale laws; gen_v owns the deployed-model time axis.
5. **gen_s_embodied_interactive_perception** (priority 5, reserve) — after q/r/w if w5 acceptance holds.
6. **gen_t_efficiency_deployment_science** (priority 6, reserve, mandate SHRUNK) — exclude distillation (now owned); commission only if the 1000-margin erodes.
7. **gen_x_constructive_capability_2** (CONTINGENT, do not commission now) — only if the post-w5 audit measures master loose-constructive < 15% *after* gen_p merges. At 10.8% pre-merge, the w2 <10% trigger did not fire.

**Capacity math** (HYPOTHESIS on EVIDENCE inputs): master 934; w5_NPO raw 304 at blended acceptance 77.0% (934/1213) -> **~1168**, clearing 1000 on the in-flight wave alone; remand lane adds 0–127 more (extract-only pass yielded 46/173; the 127 need invasive retrofit). gen_q/r/w -> ~1400. All recommended letters are **diversity margin, not capacity necessity** — commission in coverage-hole order (r, q, w), not volume order.

## 7. Guard updates (delta to the w2 set)

- **ADD**: within-shard template cap — no single judge_C family >4 accepted per shard (gen_m hit 19/10/10/7; gen_k 10/7; gen_l 8/7). Enforce at judge time from w5_NPO onward.
- **ESCALATE**: cheap-predictor-of-outcome to **portfolio freeze** at 14 — new instances displace, never add.
- **ADD**: hard-cap "ritual is mechanism in disguise" framing at <=3/shard outside gen_m.
- **EXTEND**: annotation-pathology hard ban to explicitly name agent/model-generated-annotation substrates.
- **KEEP**: SAM <=5% (held at 9.6%), calibration primary-cluster ban (dispersion at exact cap — trigger armed), equalization-null <=3/shard (fired correctly in w4: L-074 merged), eval-critique <=20%/shard, >=8 clusters none >15%, >=25% constructive floor, <=40% pure-debunk ceiling, subject-native-mechanism rule.
- **ENFORCE**: GATE-8 novelty lane — 105 dissent-carrying records, the w2 73-id list, w4's 3 outvoted kills + 20-id watchlist.

## 8. Quality gates on w3/w4 additions

EVIDENCE: 420/440 carry a digit in `falsifiable_prediction` (the 20 without are all tracked: 13 gate5-repaired verbal-exact bounds + 7 gen_k `gate1_qualitative_threshold`); 440/440 carry `evidence_label` dicts; 198 gen_k/gen_l carry `gate4_deferred`. Wave2 (D/E/F) schema backfill remains the outstanding debt; one Stage-2 retrofit lane should take wave2 backfill + GATE-4 pinning + the 7 gen_k numeric retrofits together.

## 9. Citation integrity

EVIDENCE: 14 records carry citation-like strings, all wave1 gen_a, the same well-known-paper set verified at w1/w2 (SAM, SAM2, LoRA, VPT, MAE, BitFit, model soups, task arithmetic, DETR, texture-bias, registers, SAM-HQ, CKA). Instrument note: w2 counted 13 citation-*strings*; I count 14 *records* carrying them — same underlying set. **Zero citation strings added by waves 3/4. Zero fake citations found. This audit adds no citations. Novelty of all ideas remains unverified.**

## 10. Off-master enumeration (READ-ONLY — nothing merged)

- gen_n 100 ideas @ `origin/cursor/p1-gen-n-scaling-memorization-4814` — w5_NPO judging.
- gen_o 100 ideas @ `origin/cursor/p1-gen-o-hard-domain-acc5` — w5_NPO judging.
- gen_p 104 ideas @ `origin/cursor/p1-gen-p-constructive-6c3b` — w5_NPO judging.
- w5 judge progress: judge B pushed (`origin/cursor/p1-wave-b-w5-judge-b-feasibility-7e74`); judges A/C pending at audit time.
- 127 remaining gen_g/gen_h remands at `Windows13/_state/tasks/p1/wave_b_w3_gate5/remaining_remand.jsonl` — accepted-on-content, awaiting invasive threshold retrofit; a repair lane, not a generator slot.

## 11. Scope compliance

- Canonical files untouched: `ideas_master.jsonl`, `research_state.json`, `research_ledger.md`, `window.lock.json` (branch created *from* the canonical tip `2411f93`, files carried verbatim).
- Files written: only `Windows13/_state/tasks/p1/diversity_audit_w3/auditor_A.{md,json}` and `done_auditor_A.json`.
- Own branch `cursor/p1-diversity-audit-w3-auditor-a-9a11`; no force-push; Windows13 identity unchanged; independent of auditors B/C.
