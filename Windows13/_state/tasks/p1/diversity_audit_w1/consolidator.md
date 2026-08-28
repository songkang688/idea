# P1 Diversity Audit w1 — Consolidator Report

- **Task**: `p1_diversity_audit_w1` / role `consolidator`
- **Window**: Windows13 (locked; identity untouched)
- **Branch**: `cursor/p1-diversity-audit-consolidator-w1-25a0`
- **Canonical base**: `origin/cursor/p1-wave-b-consolidator-w1-7a58` @ `936670f` (248 accepted ideas; NOT modified by this task)
- **Decided at**: 2026-08-28T19:44:04Z
- **Status**: ok (no irreconcilable conflicts; meta-judge not required)

## Inputs

| Auditor | Branch | Focus |
|---|---|---|
| A (mode collapse) | `origin/cursor/p1-diversity-auditor-a-mode-collapse-3ef2` @ `bf47c66` | crowding, permutation flags, blind spots |
| B (quality/blindspots) | `origin/cursor/p1-diversity-auditor-b-quality-blindspots-0826` @ `75beb1e` | hypothesis quality, citations, constructive census |
| C (adversary) | `origin/cursor/p1-diversity-auditor-c-adversary-c2b5` @ `286b4f7` | template families F1–F5, off-master shard discovery |

## Where the auditors agree (adopted as consensus, EVIDENCE)

1. Surface/lexical duplication in the 248 is LOW; the collapse is structural (genre and model-organism level).
2. SATURATED, stop feeding: SAM/SAM2 internals (~34–35% subject share), PEFT-on-SAM, calibration/uncertainty (all three wave-1 generators independently converged), annotation-pathology, generic eval critique (~43.5% super-cluster).
3. gen_b fixated on smoke/fire/fog/transparent media (~72–73% of shard) → hard ban on those running examples going forward.
4. Blind spots at ~0%: restoration/low-level, diffusion model science, LLM/agent-vision, 3D/geometry/video-beyond-SAM2, scaling laws, memorization/privacy, training-dynamics/objective science.
5. No fake citations anywhere in master or in the audits (13 citation strings, all in gen_a `prior_work_basis`, all real well-known papers).

## Disagreements and how they were reconciled

### 1. Constructive count: A=0, B=46 (18.5%), C=7–11 (~3–4%)
Different operationalizations, not conflicting facts. A ran a crude method-primary regex; B hand-labeled all 248 one-liners with a loose criterion; C applied a strict enabling-capability criterion and explicitly noted B's looser one. **Resolution**: C's strict count is the headline scarcity metric; B's 46-id list is kept as the loose upper bound and as a *protected list* for Stage 2 (those ids must not be culled on genre grounds); A's regex stands as evidence that nothing is method-primary in framing. All three converge on the action: constructive rebalance (dedicated gen_p + ≥25% per-shard constructive quota). Not escalated.

### 2. Letter collisions with existing gen_d–gen_g shards (+ reserved gen_h)
Auditor A recommended new territories under letters `gen_d..gen_i`, but wave2 shards `gen_d` (object detection, 100), `gen_e` (VLM dense, 100), `gen_f` (synthetic data, 102), `gen_g` (domain shift, 100) already exist on origin with different mandates — verified by this consolidator via `git ls-tree` across all origin branches. Auditor C caught the collision and used `gen_h..gen_m`, but `gen_h` is itself reserved/in flight per the parent dispatcher. **Resolution**: every recommendation remapped to fresh letters **gen_i..gen_p**; full mapping in `decision.json.letter_registry.remap`. Territory content from A survives; only the letters were rejected.

### 3. Territory overlap with in-flight wave2 shards
Dropped from the queue: detection science (in-flight `gen_d` owns it), VLM dense/language-vision interface (in-flight `gen_e` owns it). Narrowed A's data-centric-scaling to the residual `gen_f` does not cover (scaling-law science, memorization/privacy) → `gen_n`, with an explicit anti-overlap guard.

### 4. Guard strictness (SAM cap 5% vs 10%; constructive quota 25% vs 50%)
Adopted the stricter 5% SAM cap (C) everywhere except `gen_k` (10%, SAM2-video contrast baselines are legitimate there). Adopted C's ≥25% constructive floor + ≤40% debunk ceiling globally rather than B's 50% (which would distort characterization-law territories), and compensated with `gen_p` at ≥80% constructive. B's three quality gates (numeric kill thresholds, structured evidence_label dict, cost-bounded fastest tests) adopted verbatim.

### 5. Cross-field transfer (C only)
Deferred — single-auditor support and the highest permutation risk. Recorded in `deferred_territories` with C's guards so the signal is not lost.

## Next generator queue (8 tasks, letters gen_i..gen_p)

| # | task_id | territory (short) | fills |
|---|---|---|---|
| 1 | `p1_gen_i_restoration_lowlevel` | SR/denoise/deblur/low-light/ISP science | 0% blind spot (B#1, C#1) |
| 2 | `p1_gen_j_diffusion_model_science` | diffusion/generative models as subject | model-science gap (B#2, C#2) |
| 3 | `p1_gen_k_3d_geometry_video` | 3D/point-cloud/NeRF/depth/flow + video beyond SAM2 | 3D≈0, flow 0.4% (A#2, C#4–5) |
| 4 | `p1_gen_l_llm_agent_vision` | LLM/agent loops around vision | agent gap (C#3, B#8) |
| 5 | `p1_gen_m_training_dynamics_objectives` | training dynamics + objective science | 1.2% coverage (A#5, B#6, C#6) |
| 6 | `p1_gen_n_scaling_memorization_data_laws` | scaling laws, memorization/privacy, data composition | 0%/0.4% (A#1 residual) |
| 7 | `p1_gen_o_hard_domain_diversifier` | underwater/microscopy/remote sensing/industrial/agri/docs + medical-beyond-ambiguity | gen_b blind spots (A#3, B#7+9) |
| 8 | `p1_gen_p_constructive_capability` | enabling-capability rebalancer incl. constructive eval-repair | genre skew (A#6, C#6, B#5) |

Each queue item in `decision.json` carries `task_id`, `role=generator`, `territory`, `shard_path` (`Windows13/_state/tasks/p1/generators/<gen_id>/ideas_shard.jsonl`), id seed range, and per-shard `anti_crowding_guards`; nine global anti-crowding guards and four quality gates apply to all shards.

## Wave2 status note (no action by this task)

Wave2 shards **D–G (402 ideas) are off-master and stay off-master** until Wave B judges + the Wave2 Consolidator process them — that append is the Wave2 Consolidator's job, not this task's. Progress at consolidation time: wave2 judge A (dedup) is DONE (`origin/cursor/p1-wave-b-w2-judge-a-dedup-13e5`); judges B/C and the consolidator are pending. Recommendation: run `p1_wave_b_w2_continue` in parallel with dispatching `gen_i..gen_p`.

## Evidence and citation policy

All counts above are labeled EVIDENCE where reproducible from repo contents (auditor JSONs, `git ls-tree`, shard line counts re-verified locally by this consolidator) and HYPOTHESIS where judgment-based (e.g. freed-slot estimate). **This report makes no literature claims and adds zero citations; no fake citations.**

## Scope compliance

- `window.lock.json`: untouched. `windows_id` Windows13 unchanged. `ideas_master.jsonl`: untouched (accepted_count_canonical stays **248**).
- `research_state.json`: only exploration/diversity-audit fields added; `windows_id` Windows13, `window_locked` true, Stage 1 preserved; JSON validated.
- `research_ledger.md`: append-only audit section.
- Own branch, no force-push.
