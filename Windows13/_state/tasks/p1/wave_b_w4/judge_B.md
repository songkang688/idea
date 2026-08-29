# P1 Wave B w4_KLM — Judge B (feasibility) — Windows13

- **Role:** judge_B_feasibility | **Wave:** w4_KLM | **Branch:** `cursor/p1-wave-b-w4-judge-b-feasibility-331c`
- **Inputs (raw shards, judged independently of Judge A, which was not on origin at judging time):**
  - gen_k `origin/cursor/p1-gen-k-3d-geometry-video-dc89` — 105 ideas (3D geometry / video)
  - gen_l `origin/cursor/p1-gen-l-llm-agent-vision-c11e` — 100 ideas (LLM-agent vision)
  - gen_m `origin/cursor/p1-gen-m-training-dynamics-d8f7` — 100 ideas (training dynamics / objectives)
- **Canonical master:** READ ONLY, 592 records on `origin/cursor/p1-wave-b-consolidator-w3-bf20` (this branch's base); used for collision checks only, untouched. `ideas_master.jsonl` not written. Lock identity unchanged.
- **Exclusions honored:** gen_n / gen_o / gen_p not read; nothing from them merged into `accepted_shard_B`.

## Headline verdicts

| | K | L | M | total |
|---|---|---|---|---|
| input | 105 | 100 | 100 | **305** |
| keep | 103 | 98 | 100 | **301** |
| merge | 2 | 2 | 0 | **4** |
| kill | 0 | 0 | 0 | **0** |

- Tiers over keeps: **T1 (inference/analysis only) 152**, **T2 (small trainings, GPU-days) 149**, **T3 (gated) 0**.
- **159 keeps score 5** (killable in ≤1 GPU-day on public assets by the generator's own stated bound).
- Zero kills: this wave is uniformly cheap and falsification-first; even known-result-adjacent entries carry distinct experimental designs worth the marginal arm on a shared rig.

## Merges (4)

| absorbed | into | scope | basis |
|---|---|---|---|
| K-043 | K-037 | in-wave | same matched-budget GS densification ablation grid; overcomplete-then-prune becomes one arm; keep K-043's cross-seed variance readout |
| L-011 | L-015 | in-wave | L-011 (text-vs-raw probe gap) is stage one of L-015's latent-handoff adapter protocol |
| L-069 | L-097 | in-wave | identical variance-decomposition-and-freeze design, same ≥50%-share / ≥40%-cut thresholds; active viewing kept as one task family |
| K-100 | **C-023 (master)** | cross-wave | depth-specific instance of the master semantic-duplicate contamination program (C-023/C-024/C-028 family, which already absorbed w3 routings). Master untouched; routing recommendation for w4 consolidator |

## Schema drift (commissioned flag) — three mutually inconsistent schemas

- **gen_k:** kill threshold in a **separate `kill_threshold` field** (105/105), **plural `evidence_labels`**, no `needs_special_resources` field.
- **gen_l:** inline `KILL:` clause in `falsifiable_prediction`, singular `evidence_label`, `needs_special_resources` present (all false).
- **gen_m:** inline `KILL:` clause, singular `evidence_label`, plus extra fields `source_shard` / `wave` / `novelty_status` / `seg_metric_dependent`; the **`wave` field is mislabeled `p1_wave_a_w3` on all 100 records** (actual wave w4_KLM) — consolidator must correct on append.
- Genre vocabulary also drifts per shard (`debunk_audit` vs `debunk`/`eval-critique` vs `audit_debunk`).

## Gate compliance

- **GATE-1 (numeric kill threshold):** K 100/105 — **5 qualitative** (K-035, K-039, K-065, K-083, K-094), flagged for generator retrofit, **no numbers invented by this judge**. L 100/100, M 100/100.
- **GATE-2 (evidence label):** present 305/305; gen_k's plural field name is drift, not a content gap.
- **GATE-3 (time/cost bound):** 305/305 fastest experiments carry explicit time/device bounds (K/L mostly hours-to-one-GPU-day; M mostly 1–5 days on one A100/RTX 4090).
- **GATE-4 (named public dataset AND model in the experiment): bimodal.** gen_m **100/100** (torchvision ResNet-50, DeepLabv3+, NYU Depth v2, Cityscapes, ImageNet-100, …). gen_k **0/105** full compliance (K-001 dataset-only, K-068 model-only) and gen_l **0/100** — both write generically ("public backbones", "one RGB-D dataset", "open agent framework", "public vision tools"). Verified by manual spot-reads: a generator style choice, not a detector artifact. **205 records need asset-naming retrofit before Stage-2** (schema-only remand recommended, not content rejection).
- **GATE-5 (retrofit duty):** taken by recommendation only — judges don't rewrite records. Retrofit list in `judge_B.json`.
- **GATE-6 (genre audit):** K 44 characterization / 27 debunk_audit / 34 constructive; L 48 / 47 constructive / **only 3 debunk + 2 eval-critique (thin debunk lane)**; M 58 characterization_law / 26 constructive / 16 audit_debunk.
- **GATE-7 (no fake citations): PASS** — zero citation-like strings in all 305 records by mechanical scan; this judge cites nothing.
- **GATE-8 (prior art):** 3 unverified `prior_art_risk` flags (L-074, M-023, M-031); needs the triage lane, no citations asserted.

## Resources & anomalies

- **Only one `needs_special_resources=true` in the wave: M-030** (8-GPU node for the full batch-size ladder; stated single-GPU fallback tests a reduced range → stays T2, score 3).
- **8 gen_k ideas require fresh physical captures** (K-021, K-045, K-050, K-058, K-088, K-089, K-094, K-103) — runnable, but capture labor is invisible in GPU-time bounds; scores discounted one point.
- Anomaly ids (6): the 5 qualitative-kill gen_k ids + M-030.
- `seg_metric_dependent=true` on 61/100 gen_m records is consistent with their dense-prediction readouts; not a defect.

## Co-run economics

19 co-run rigs identified (full membership in `judge_B.json`): the wave's real cost is far below 305 × per-idea cost because clusters share harnesses — e.g. `gs_matched_budget_rig` (11 GS ablation arms on one training rig), `open_agent_harness` + per-cluster L rigs (one agent framework, frozen tools, fixed query suites), `dense_finetune_trajectory_rig` / `spike_telemetry_rig` (one instrumented training run feeds many analyses).

## Family-cap pressure (escalated, not force-merged)

- `shared_percept_decorrelation` (L): L-024, L-036, L-071, L-072, L-078, L-086 — 6 at cap across 4 clusters; all instances of "verification/ensemble value = error decorrelation".
- `head_backbone_interface` (M): M-031, M-041, M-044, M-049, M-050, M-098 at cap (M-023, M-047 adjacent).
- `bn_norm_statistics_mechanics` (M): M-071..M-078 — 8, over cap; the whole normalization cluster is one fingerprint family.

Recommendation: Stage-2 slot caps at consolidation rather than judge-time forced merges — members target distinct systems and share rigs, so keeping them is nearly free.

## Deliberate tensions kept (4)

1. **L-024 vs L-036** — is same-model self-verification unrescuable, or does consequence-question phrasing decorrelate percepts enough?
2. **L-072 vs L-078** — encoder diversity vs tool-set diversity: which buys decorrelation cheapest at matched cost?
3. **L-074 vs L-075** — debate as compute repackaging vs adversarial falsification-seeking adding real value at iso-compute.
4. **M-044 vs M-049** — head-init scale vs head-LR timescale ratio as the operative interface knob.

## Cross-wave adjacencies (no merge)

- M-071..M-078 ↔ master F-023 (sim-to-real normalization statistics): adjacent measurement family, different mechanism.
- L-024/L-036 ↔ master D-065 (MLLM verifier-role deployment): adjacent theme, different question.

## Handoff

Judge A w4 was not on origin at judging time. Consolidator should diff this shard against Judge A when it lands; expected friction points are the 4 merges and the 5 qualitative kill thresholds. Recommended next: `p1_wave_b_w4_judge_C_or_consolidator`.
