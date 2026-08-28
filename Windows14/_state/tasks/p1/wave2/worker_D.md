# P1 Wave 2 - worker_D: Object Detection Ideas

- task_id: `p1_gen_w2_d`
- role: worker_D (Wave 2 generator, filling empty dispatcher slot while Wave 1 Judge A runs)
- windows_path: `Windows14` (window.lock.json verified: `locked: true`, `windows_id: Windows14`)
- territory: **Object Detection** (failure modes of detectors / open-vocab / foundation-model detection; explicitly NOT SAM+detector mashups)
- output: `Windows14/_state/tasks/p1/wave2/worker_D.ideas.jsonl`
- idea_count: **124**
- evidence_status: all `HYPOTHESIS` — no verified novelty claims, no fabricated papers, numbers, or results. `why_possibly_novel` fields are conjectures to be checked by later dedup/novelty phases.

## Cluster breakdown (15 clusters, 124 ideas)

| cluster | count | theme |
|---|---|---|
| confidence_calibration | 11 | score semantics, threshold transfer, deployment gap, hallucination logit forensics |
| open_vocab_semantics | 11 | name-frequency effects, modifier/relation binding, negative vocabulary, vocabulary-size tax, multilingual queries |
| foundation_detectors | 11 | grounding single-referent bias, FP coherence, co-query interference, proposal-stage modality bottleneck, binding-vs-recognition emergence |
| nms_and_duplicates | 10 | density-adaptive suppression, part-whole duplicates, kept-vs-best-box gap, numeric tie instability, TTA geometry |
| localization_vs_classification | 8 | subtask error coupling, aspect-ratio shrinkage, amodal convention mismatch, center drift, per-edge uncertainty |
| small_objects_and_scale | 8 | assignment-vs-feature resolution decomposition, FPN scale cliffs, context parasitism, phase aliasing, annotation noise floor |
| distribution_shift_failures | 8 | subtask-selective corruption, texture-vs-shape in detection, low-light normalization, level-targeted weather adaptation, JPEG grid FPs |
| detr_query_dynamics | 8 | query coverage gaps, Hungarian instability, layer oracles, inert content queries, denoising prior over-trust, effective query capacity |
| evaluation_metrics | 8 | operating-region mAP, IoU threshold vs annotator ceiling, bootstrap CIs, error-taxonomy order dependence, flicker metrics, split overfitting |
| training_dynamics | 8 | assignment as failure-profile lever, focal gamma frontier, copy-paste shortcuts, subtask convergence, EMA decomposition, taxonomy interference |
| context_and_cooccurrence | 7 | co-occurrence FP structure, causal object-removal maps, spatial grammar, camera-height priors |
| dataset_annotation_artifacts | 7 | missing-label suppression, crowd flags, annotator-batch fingerprints, near-duplicate leakage, rare-class label noise |
| occlusion_and_crowding | 7 | pairwise-memorized occlusion, amodal emergence, feature-collision cliffs, fence fragmentation, detection-based counting |
| temporal_video_detection | 6 | flicker as thresholding artifact, aggregation speed threshold, blur-speed prior, re-detection latency, keyframe bias |
| open_world_unknowns | 6 | proposal confound in open-world eval, objectness taxonomy leakage, novelty/OOD trade-off, discard-stream mining |

## Generation discipline

- Every idea carries all 15 required fields including `default_community_belief`, `why_it_might_be_wrong`, and `fastest_falsification` (most falsifiable within hours-to-days on public checkpoints/datasets, no training where avoidable).
- Territory boundary respected: no SAM+detector mashup ideas; SAM-adjacent territory belongs to wave1 worker_A.
- id_seed range: `w14D2-001` … `w14D2-124` (D2 prefix distinguishes wave2 worker_D from wave1 shards).
- Did not touch: `window.lock.json`, `ideas_master.jsonl`, `research_state.json`, any other worker's shard.

## Unresolved items

- Novelty of all 124 ideas is unverified (by design at P1); dedup against wave1 shards A/B/C and any parallel wave2 shards is the consolidator/judge's job.
- Possible thematic overlap with wave1 worker_C (failure mining) on a few failure-analysis-flavored ideas (e.g. error-taxonomy critiques); flagging for the dedup judge rather than self-censoring.
