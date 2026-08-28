# P1 Wave B — batch_001 — Judge A Report (hypothesis-level clustering)

- **task_id:** `p1_wave_b_batch001_judge_A`
- **role:** judge (hypothesis-level clustering / scientific-structure)
- **windows_path:** `Windows15` (locked)
- **inputs:** `gen_A/ideas.jsonl` (100), `gen_B/ideas.jsonl` (100), `gen_C/ideas.jsonl` (100) — 300 ideas total
- **outputs:** `clusters.json`, `verdict.jsonl` (one line per input idea), `done.json`, this report

## 1. What this judge did and did not do

All 300 ideas were read in full at the hypothesis level. Ideas were clustered by their **falsifiable core claim and mechanism** — what would have to be true of the world for the idea to hold — not by keyword, domain vocabulary, or the generators' own cluster labels. Near-duplicates were marked and merged into a representative; a small number of clearly weak or likely-known ideas were dropped; the rest were kept.

Explicit scope limits, per instructions:

- **No verified novelty claims.** Where a note says "likely-known" or "prior-art risk", that is an advisory judgment from general knowledge, not a literature check. Nothing here certifies that any kept idea is novel.
- **No citations.** None were consulted, and none were invented.
- All keep/merge/drop decisions are **this judge's verdict only**, intended as input to the batch_001 consolidator, which may overrule any of them.

## 2. Corpus shape

The three generator shards occupy three largely disjoint territories, which is why raw cross-shard duplication is low but **template-level duplication** (same scientific claim instantiated in different domains) is common:

| Shard | Territory | n |
|---|---|---|
| gen_A | SAM / promptable-segmenter adaptation science (PEFT/LoRA mechanics, prompt geometry, forgetting, provenance) | 100 |
| gen_B | Medical image segmentation (annotation noise, metrology, shifts, lesions, human-AI workflow, 3D plumbing) | 100 |
| gen_C | Amorphous / boundary-undefined media (smoke, fire, glass, transparency): ontology, physics, temporal dynamics | 100 |

Schema note for the consolidator: gen_B carries `territory` + `evidence_class`, gen_C carries `evidence_class` only, gen_A carries neither. Field harmonization will be needed at consolidation.

## 3. Clustering result: 40 hypothesis-level clusters

Full membership, per-cluster hypothesis statements, shard coverage, merges, drops, and flags are in `clusters.json`. Summary:

| Cluster | Name | Size | Shards | Merges/Drops within |
|---|---|---|---|---|
| HC-01 | eval_statistical_validity | 8 | A,B,C | 3 merges → B-020 |
| HC-02 | task_relevant_metric_decoupling | 14 | A,B,C | 1 merge; 1 drop (B-022) |
| HC-03 | evaluation_protocol_artifacts | 9 | A,B,C | 1 merge → C-010 |
| HC-04 | peft_comparison_validity | 6 | A | 1 merge → A-068 |
| HC-05 | detection_vs_delineation | 6 | B,C | — |
| HC-06 | supervision_definition_gap | 8 | A,B,C | — |
| HC-07 | model_as_disagreement_simulator | 5 | A,B,C | 1 merge → B-007 |
| HC-08 | continuous_latent_thresholding | 9 | B,C | 1 merge → C-003 |
| HC-09 | annotation_protocol_design | 8 | B,C | — |
| HC-10 | annotation_process_imprint | 11 | A,B,C | 1 merge → C-004 |
| HC-11 | adaptation_data_efficiency | 8 | A | 1 drop (A-051) |
| HC-12 | self_training_prior_reinforcement | 2 | A,B | — |
| HC-13 | peft_update_geometry | 10 | A | — |
| HC-14 | minimal_sufficient_adaptation | 8 | A | 1 merge → A-081 |
| HC-15 | geometric_scale_prior_mismatch | 5 | A,B | — |
| HC-16 | capability_erosion | 10 | A | 1 merge → A-023 |
| HC-17 | edge_affinity_prior | 3 | A,B,C | 1 cross-shard merge (C-029 → A-034) |
| HC-18 | sam_perceptual_mechanisms | 6 | A | — |
| HC-19 | gap_localization_readout | 10 | A,B | — |
| HC-20 | prompt_interface_mechanics | 6 | A | 1 merge → A-010 |
| HC-21 | pretraining_provenance_priors | 7 | A | — |
| HC-22 | synthetic_and_physical_data | 8 | C | — |
| HC-23 | shortcut_priors_medical | 16 | B | 1 merge → B-026; 1 drop (B-032) |
| HC-24 | output_pipeline_bottleneck | 4 | A,B,C | — |
| HC-25 | topology_thin_structures | 3 | B | — |
| HC-26 | uncertainty_calibration_safety | 12 | A,B,C | 2 merges (→ A-009, → B-076) |
| HC-27 | label_free_auditing | 3 | A,B | — |
| HC-28 | lifecycle_deployment_ops | 4 | A | — |
| HC-29 | training_dynamics_boundary_memorization | 8 | A,B,C | 1 merge → B-012 |
| HC-30 | media_temporal_dynamics | 14 | C | 1 merge → C-050 |
| HC-31 | multimodal_sensing_media | 8 | C | 1 drop (C-061) |
| HC-32 | image_formation_physics_media | 9 | C | — |
| HC-33 | media_representation_output_space | 8 | C | 1 merge → C-080 |
| HC-34 | interactive_refinement_dynamics | 4 | A,B,C | 1 cross-shard merge (C-036 → A-005) |
| HC-35 | human_ai_workflow | 7 | B | — |
| HC-36 | media_context_shortcuts | 15 | C | — |
| HC-37 | frozen_foundation_signals | 2 | C | — |
| HC-38 | consistency_as_supervision | 2 | A | — |
| HC-39 | distribution_shift_medical | 6 | B | 1 merge → B-046 |
| HC-40 | volumetric_geometry_inference | 8 | B | — |

Every cluster is a **keep** at cluster level; no cluster was judged empty of scientific content.

## 4. Near-duplicates

### 4.1 Merged (21 total; decision = `merge` in verdict.jsonl, with `merge_into`/`duplicate_of` set)

Within-shard merges (19): B-006, B-014, B-024 → B-020 (noise-floor variance sources); B-019 → B-060; C-040 → C-010; A-020 → A-068; B-059 → B-007; C-035 → C-003; C-006 → C-004; A-025 → A-023; A-093 → A-081; B-051 → B-026; B-052 → B-046; B-082 → B-076; A-063 → A-009; B-100 → B-012; A-040 → A-010; C-017 → C-080; C-049 → C-050.

Cross-shard merges (2):

- **C-029 → A-034** (HC-17): both claim segmenter boundaries snap to strong irrelevant image gradients; the smoke measurement becomes a testbed of A-034's local edge-field model.
- **C-036 → A-005** (HC-34): both claim interactive refinement oscillates non-convergently between attractors on ambiguous content; media is the high-ambiguity testbed.

Merges are "same claim, same experiment family" — the absorbed idea's distinctive arm is noted in `verdict.jsonl` so nothing is silently lost.

### 4.2 Retained template twins (kept, flagged in notes; consolidator may still merge)

Same scientific claim instantiated in different domains with genuinely different experiments or instruments. Kept deliberately, recorded in `clusters.json → cross_shard_near_duplicate_relations`:

A-072 ↔ B-020 (noise floor vs claimed deltas) · A-061 ↔ C-083 (model diversity reproduces rater disagreement) · A-036 ↔ C-013 (morphology fingerprints the generation process) · A-062 ↔ B-078 (overconfidence grows with shift) · A-067 ↔ B-077 (model signals audit labels) · A-045 ↔ B-084 (granularity selection is the dominant gap) · A-055 ↔ B-069 (self-training reinforces the prior) · A-092 ↔ C-088 (physics-matched noise dominates content) · A-053 ↔ B-096 ↔ C-093 (boundary noise is filtered, not learned) · B-003 ↔ B-047 ↔ C-043 (sites/annotators are labeling functions) · B-017 ↔ C-046 (bookkeeping conventions permute rankings) · A-080 ↔ B-012 (staged fitting timescales) · C-002 ↔ C-020 (detectability score predicts misses) · C-038 ↔ C-056 (temporal decorrelation half-life).

## 5. High-value / anomalous ideas (14 flags)

Flagged for unusual leverage, inversion of a standard assumption, or safety relevance — **not** verified novel:

| Idea | Why flagged |
|---|---|
| W15-B001-C-030 | Defect-as-sensor: prompt fall-through rate as a calibrated opacity meter |
| W15-B001-A-049 | Oracle low-res-mask experiment could bound/deflate much of the boundary fine-tuning literature |
| W15-B001-B-065 | Non-monotone final contour quality as model accuracy rises (rare errors evade review) — safety-critical |
| W15-B001-B-093 | Bypass segmentation entirely for scalar clinical endpoints |
| W15-B001-A-076 | Random-encoder floor exposes which benchmarks actually test foundation knowledge |
| W15-B001-A-098 | Adapter transport across base models via linear feature map |
| W15-B001-C-055 | Active micro-motion + rigidity violation for refractive surfaces |
| W15-B001-C-063 | Rolling-shutter row spectrum as single-frame flame-dynamics cue |
| W15-B001-C-099 | Synthetic media spoof deployed smoke/fire pipelines — security-relevant |
| W15-B001-C-011 | Annotator disagreement as a physical densitometer |
| W15-B001-B-079 | Abstention-disease coupling: automation equity failure invisible to aggregate metrics |
| W15-B001-A-090 | SA-1B privacy blurring learned as objectness evidence — provenance quirk |
| W15-B001-C-092 | Physical compositing correctness beats visual realism for transfer |
| W15-B001-B-036 | Fractional-membership training: unbiased volumetry hidden from overlap metrics |

## 6. Drops (4)

- **W15-B001-B-032** — effective-locality of trained attention models: likely-known (heavily studied ERF territory); thin marginal content. (Advisory.)
- **W15-B001-A-051** — shared-exponent scaling curve: soft claim, dominated by actionable siblings (A-052, A-057) that produce the same curves as a byproduct.
- **W15-B001-B-022** — normalized-Dice transform: largely anticipated by existing resolution/shape-normalized boundary metrics. (Advisory.)
- **W15-B001-C-061** — audio-visual flame localization: established technique family; the flame-specific increment is thin next to C-062/C-063.

## 7. Verdict summary

| Decision | Count |
|---|---|
| keep | 275 |
| merge | 21 |
| drop | 4 |
| **total** | **300** |

## 8. Notes and tensions worth the consolidator's attention

1. **An informative internal contradiction was kept on purpose:** A-017 (convention changes require encoder rewrites) vs A-045/A-046 (conventions are decoder-level readout policies). One experiment matrix resolves it; both sides are falsifiable as stated.
2. **The strongest cross-shard convergence** is on three claims arrived at independently by all three generators: (a) measurement/label noise rivals claimed effect sizes (HC-01/02/03), (b) a large share of "domain gap" is supervision-definition gap (HC-06/08/10), and (c) model-internal disagreement reproduces human disagreement (HC-07/26/27). Independent triple convergence raises confidence that these are real seams, not generator idiosyncrasy.
3. **Merge direction is conservative:** absorbed ideas retain their distinctive experimental arm in the verdict notes; no content was discarded by merging.
4. gen_B/gen_C carry `evidence_class` (and gen_B `territory`) fields absent from gen_A — schema harmonization needed downstream.
