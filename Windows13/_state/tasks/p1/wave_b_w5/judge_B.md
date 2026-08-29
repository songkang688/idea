# P1 Wave B w5_NPO — Judge B (feasibility) — Windows13

- **Role:** judge_B_feasibility | **Wave:** w5_NPO | **Branch:** `cursor/p1-wave-b-w5-judge-b-feasibility-7e74`
- **Inputs (raw shards, judged independently of Judge A, which was not on origin at judging time):**
  - gen_n `origin/cursor/p1-gen-n-scaling-memorization-4814` — 100 ideas (scaling / memorization / data laws)
  - gen_o `origin/cursor/p1-gen-o-hard-domain-acc5` — 100 ideas (hard-domain diversifier: microscopy, underwater, sonar, histopathology, documents, remote sensing, industrial)
  - gen_p `origin/cursor/p1-gen-p-constructive-6c3b` — 104 ideas (constructive capability: detection eval repair, annotation protocols, benchmarks, weak supervision)
- **Canonical master:** READ ONLY, 638 records on `origin/cursor/p1-wave-b-w3-gate5-repair-f611` (this branch's base); used for collision checks only, untouched. `ideas_master.jsonl` not written. Lock identity unchanged.
- **Exclusions honored:** gen_k / gen_l / gen_m (w4_KLM) not judged; nothing from them merged into `accepted_shard_B`.

## Headline verdicts

| | N | O | P | total |
|---|---|---|---|---|
| input | 100 | 100 | 104 | **304** |
| keep | 99 | 100 | 101 | **300** |
| merge | 1 | 0 | 3 | **4** |
| kill | 0 | 0 | 0 | **0** |

- Tiers over keeps: **T1 (inference/analysis, ≤1 GPU-day, no pretraining) 137**, **T2 (small trainings, ≤14 GPU-days on one GPU) 163**, **T3 (gated) 0**.
- **136 keeps score 5** (killable in ≤1 GPU-day on public assets by the generator's own stated bound); 134 score 4; 29 score 3; 1 score 2.
- **gen_o is the cheapest shard judged in this window so far:** 100/100 ideas within 5–40 GPU-hours on one consumer GPU, each with an explicit dollar figure (~$10–$50).
- Zero kills: every record has a public pilot path and a pre-registered numeric kill condition; even the seven `needs_special_resources=true` records stage a cheap public pilot before the gated confirmation step.

## Merges (4)

| absorbed | into | scope | basis |
|---|---|---|---|
| P-065 | P-061 | in-wave | Procrustes orthogonal head-transplant is the constrained arm of P-061's cross-backbone translator family; same rig (fit map on unlabeled images, transplant frozen head, measure recovery); keep orthogonal-vs-linear-vs-2-layer as arms |
| P-075 | P-072 | in-wave | support-consistency rescoring is literally one energy term of P-072's relational re-decoding; nested ablation arm on the same harness; keep the floating-object false-positive readout as the first ablation |
| N-085 | N-084 | in-wave | N-085's scale × similarity claim is one cell of the (duplication count × similarity × scale) dose-response grid N-084 fits; one controlled-injection grid, two readouts; keep N-085's directional headline as a named secondary endpoint |
| P-010 | **C-048 (master)** | cross-wave | detection-specific two-way head × backbone factorial instance of the master head-confound program (C-048, protocol-assumptions). Master untouched; routing recommendation for the w5 consolidator; preserve P-010's additivity readout as an arm |

## Schema (major improvement over w4) + two consolidator actions

All three shards share **one uniform 21-field schema** (w4 had three mutually inconsistent ones). Remaining actions:

1. **`wave` field mislabeled `p1_wave_a_w3` on ALL 304 records** (actual wave w5_NPO) — same defect as w4 gen_m; consolidator must correct on append.
2. **`evidence_label` is a per-field dict** (each of problem/core_hypothesis/falsifiable_prediction/… individually labeled) versus the master's singular string field — normalization decision needed before append. Richer than w4, not a content gap.
3. Cosmetic: the gen_o branch carries no `ideas_shard.md` companion (jsonl only).

## Gate compliance

- **GATE-1 (numeric kill threshold): 304/304 numeric in substance.** gen_n 100/100 and gen_p 104/104 with digits inline; gen_o 100/100 with one formatting outlier — **O-007 spells its numbers in words** ("factor of two", "one-quarter") — normalization only, **no numbers invented by this judge**.
- **GATE-2 (evidence label):** present 304/304 as per-field dicts, plus inline `[KNOWN FACT]/[HYPOTHESIS]/[EXPECTED RESULT]/[MODEL SPECULATION]` tags in text fields.
- **GATE-3 (time/cost bound):** 304/304 fastest experiments parse to explicit bounds (gen_n 1–10 GPU-days on one A100; gen_o 5–40 GPU-hours on one consumer GPU with dollar figures; gen_p under-a-day zoo re-scoring up to 12 single-A100-day retraining grids).
- **GATE-4 (named public dataset AND model in the experiment): bimodal, inverted relative to w4.** gen_p **104/104** full (COCO/LVIS/ADE20K/PACO/KINS/COCOA + MMDetection/MMSegmentation/DINOv2/timm). gen_o **97/100** (O-072 model unnamed; O-077/O-078 name models but run on simulation-generated data, so a dataset name is arguably N/A). gen_n **3/100 full** (N-001, N-002, N-005; N-009 full by explicit reuse of the N-001 grid) — the shard writes generically ("public corpora", "public checkpoints", "small models"). Verified by manual spot-reads: a generator style choice exactly parallel to w4 gen_k/gen_l, not a detector artifact. **96 gen_n records need asset-naming retrofit before Stage-2** (schema-only remand recommended, not content rejection; id list in `judge_B.json`).
- **GATE-5 (retrofit duty):** taken by recommendation only — judges don't rewrite records.
- **GATE-6 (genre audit):** N 67 characterization_law / 25 constructive / 8 audit_debunk; O 32 / 50 / 18; P 4 / 100 / 0 (constructive lane by commission). Wave-level debunk lane is thin (26/304).
- **GATE-7 (no fake citations): PASS** — zero fabricated citation strings. Six gen_n `why_possibly_novel` fields carry **name-only attributions** (Hernandez et al., Muennighoff et al., Jagielski et al., Maini et al., McKenzie et al., Wei et al.) with no titles/venues/IDs asserted → routed to GATE-8 triage as unverified. O-053's "arXiv-derived corpus" is a descriptor of DocBank, not a citation. This judge cites nothing.
- **GATE-8 (prior art):** unverified attribution ids N-007, N-035, N-058, N-072, N-093, N-094 — need the triage lane before Stage-2.

## Resources & anomalies (14 ids, none fatal)

- **7 `needs_special_resources=true`, all with public pilots first:** N-020 (multi-run mask-supervised pretraining; generator admits the 7-GPU-day 1%-SA-1B pilot is **underpowered** → the wave's only `runnable_as_stated=false`, score 2); O-019 (real-SAS data access), O-036 (lab collaboration), O-075 (custom multi-LED capture rig), O-077 (CT facility access), O-078 (thermography rig) — each stages a 10–24 GPU-hour public/simulated pilot, scores discounted to 4; P-009 (binding cost is ~20 expert-hours or ~$300 crowdsourced annotation, GPU cost trivial — discounted to 4).
- O-007 spelled-out numeric threshold (formatting).
- 6 prior-art attribution ids (above).
- `seg_metric_dependent=true` on 57/104 gen_p and 6/100 gen_o records is consistent with their dense-prediction readouts; not a defect.

## Co-run economics

**27 co-run rigs** identified (full membership in `judge_B.json`); the wave's real cost is far below 304 × per-idea cost. Standouts: `n_small_pretrain_grid_rig` — N-009 explicitly reuses the N-001 iso-compute grid, and most model-compute-scaling / dense-transfer ideas share small-pretrain ladders; `n_contamination_injection_rig` — one injection grid feeds N-084 (post-merge) and the whole contamination-mechanism cluster; `o_*` per-domain rigs — one physics simulator + one small trained head per domain (underwater optics, sonar, microscopy PSF, histopath WSI, document OCR/layout, remote sensing, industrial defect); `p_detection_eval_repair_rig` / `p_benchmark_stats_rig` — one cached-inference pass over the MMDetection/MMSegmentation zoos feeds most of gen_p's T1 ideas.

## Deliberate tensions kept (4)

1. **P-014 vs P-064** — annotation-convention control: input-side convention-token conditioning vs weight-space interpolation between convention-finetuned checkpoints. Same goal, competing mechanisms.
2. **N-053 vs N-071** — privacy-risk direction under scaling: growth with capacity at fixed data vs dilution dominating along the realistic joint-scaling path. One memorization-scaling grid settles both.
3. **N-022 vs master A-041 (cross-wave)** — decoder scaling is dead compute vs decoder depth is the binding constraint for thin structures. Co-run on one dense rig would settle the domain split.
4. **P-004 vs P-027** — the same hierarchical-variance machinery pointed at detection MDD certificates vs segmentation power-tables; kept as rig mates, not merged.

## Cross-wave adjacencies (no merge)

- N-084 ↔ C-023 (contamination family, which already absorbed w4's K-100 routing): quantitative dose-response law vs semantic-duplicate detection claim.
- P-048 ↔ D-027 (assignment-starvation family: occlusion slice vs tiny-object slice).
- N-061 ↔ F-062 (dense fine-tuning reuses spatial features: membership leak vs transfer persistence).
- P-019 ↔ E-083 (convention measurement vs marginalization intervention).
- P-061 ↔ J-009 (linearly-relatable representations: general encoders vs diffusion backbones).
- P-100 ↔ D-050 (masks-improve-boxes: data-side refitting vs loss-side objectives).

## Handoff

Judge A w5 was not on origin at judging time (zero w5 judge branches by `git ls-remote`). Consolidator should diff this shard against Judge A when it lands; expected friction points are the 4 merges, the 96-id gen_n GATE-4 retrofit list, and the wave-wide `wave`-field correction. Recommended next: `p1_wave_b_w5_judge_C_or_consolidator`.
