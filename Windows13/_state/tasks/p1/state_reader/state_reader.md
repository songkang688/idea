# P1 State Reader Report — Windows13

- **Task**: `p1_state_reader`
- **Role**: state_reader (read-only with respect to canonical window state)
- **Read at**: 2026-08-28T17:45:00Z (UTC)
- **This report's branch**: `cursor/p1-state-reader-cc05` (independent output branch; canonical files untouched)

## 1. Locked window identity (read, not inferred)

Read from `Windows13/_state/window.lock.json` on
`origin/cursor/windows13-p0-init-implementation-d93f`
(remote tip `7b37f37808f891a32708331518dad6ec299c0180`):

| Field | Value |
|---|---|
| windows_id | `Windows13` |
| windows_number | `13` |
| windows_path | `Windows13` |
| repository | `https://github.com/songkang688/idea` |
| branch | `cursor/windows13-p0-init-implementation-d93f` |
| locked | `true` |
| defined_by | `P0` |
| definition_status | `canonical` |

`Windows13/_state/research_state.json` on the same branch agrees on every identity
field and carries `window_locked: true`, `current_stage: "Stage 1"`,
`total_ideas: 0`, `survivors: 0`, `final_target: 3`, `status: "initialized"`,
pipeline `1000+ -> 200 -> 50 -> 20 -> 5 -> 3`. No conflict between lock and
research state was found, so this task is **complete**, not blocked.

The lock says `windows_path = Windows13`; these outputs are therefore written under
`Windows13/_state/tasks/p1/state_reader/` exactly as the lock dictates. No path was invented.

## 2. Cross-check against P0 verification report

Read from `origin/cursor/p0-wave-c-verification-5e24`
(`_p0_dispatch/tasks/p0_init/done_verification.json` and `verification.json`):

- `p0_complete: true`, all verification checks `pass`, zero failures.
- Verified identity matches the lock exactly: `Windows13` / number 13 / path `Windows13`,
  init commit `38641a7a5813ed06b9b80c560e227ef382f76502`, push `verified_success`.
- `recommended_next_task_type: p1_start` — consistent with dispatching P1 now.

## 3. Idea inventory

`Windows13/_state/ideas_master.jsonl` on the P0 implementation branch tip is empty:
**0 lines, 0 bytes → idea_count = 0**. Stage 1 generation has not started.

## 4. P1 exploration task queue (for the parent dispatcher)

This state reader does not generate ideas. The parent should dispatch generators
against the following queue; each generator writes only to its own `shard_path`
and never touches `window.lock.json` or canonical `research_state.json`.

### Next 3 generator tasks

1. **`p1_gen_a_sam_foundation_peft`** — SAM / foundation model adaptation / PEFT /
   failure modes of promptable segmentation.
   Shard: `Windows13/_state/tasks/p1/generators/gen_a_sam_foundation_peft/ideas_shard.jsonl`
2. **`p1_gen_b_hard_domain_dense_prediction`** — Medical / smoke-fire / transparent /
   ambiguous dense prediction failure modes.
   Shard: `Windows13/_state/tasks/p1/generators/gen_b_hard_domain_dense_prediction/ideas_shard.jsonl`
3. **`p1_gen_c_contrarian_eval`** — Contrarian evaluation: calibration, uncertainty,
   benchmark/dataset weaknesses, negative results.
   Shard: `Windows13/_state/tasks/p1/generators/gen_c_contrarian_eval/ideas_shard.jsonl`

### Backlog territories (rotate after the first wave)

| Backlog task_id | Territory |
|---|---|
| `p1_gen_d_object_detection` | Object detection: open-vocabulary, small/dense objects, long-tail, detection-segmentation interplay |
| `p1_gen_e_vlm_dense_prediction` | VLM dense prediction: language-grounded segmentation, referring expressions, open-set pixel labeling |
| `p1_gen_f_synthetic_data` | Synthetic data: generation for dense tasks, sim-to-real, label noise, data-centric curation |
| `p1_gen_g_domain_shift` | Domain shift: unsupervised/test-time adaptation, domain generalization, distribution-shift robustness |
| `p1_gen_h_sr_restoration` | Super-resolution / restoration: degradation modeling, real-world blind restoration, perceptual-fidelity trade-offs |
| `p1_gen_i_diffusion_generation` | Diffusion / generation: controllable generation, generative priors for perception, editing, distillation |
| `p1_gen_j_llm_agent` | LLM / agent: tool use, agentic vision pipelines, reasoning for perception, evaluation of agents |
| `p1_gen_k_cross_field_transfer` | Cross-field transfer: importing methods/insights from NLP, audio, graphics, robotics, or science domains into vision |

## 5. Rules honored

- No new Windows number created or inferred; identity read verbatim from the P0 lock.
- `window.lock.json` not modified.
- `windows_id` / `windows_number` / `windows_path` unchanged.
- Canonical `research_state.json` not updated; all outputs are new files under
  `Windows13/_state/tasks/p1/state_reader/` on this task's own branch.

## 6. Recommendation

**`recommended_next_task_type: p1_wave_a_generators`** — dispatch the three queued
generator tasks above.
