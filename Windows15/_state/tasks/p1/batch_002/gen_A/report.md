# P1 Wave A Generator Report - batch_002 gen_A

- **task_id:** `p1_wave_a_batch002_gen_A`
- **windows_id / windows_path:** `Windows15` / `Windows15` (lock respected; no canonical files touched)
- **territory:** T04 Object detection
- **idea_count:** 100 (target 100, min 80 - met)
- **id range:** `W15-B002-A-001` … `W15-B002-A-100`
- **output files:** `ideas.jsonl` (this dir), `report.md`, `done.json`

## Scope and constraints followed

- All 100 entries are falsifiable hypotheses about detection mechanisms, evaluation, data, and deployment behavior - no backbone-swap ideas and no "architecture X + module Y" combination ideas.
- `why_possibly_novel` is explicitly marked "Unverified:" in every entry; novelty is a hypothesis label, not a verified claim (per generator contract in `state_reader/task_queue.json`).
- No invented papers, citations, benchmark numbers, named datasets-as-results, or claimed experimental results. Dataset references are generic ("a COCO-style benchmark", "a long-tail detection dataset").
- Wrote only inside `Windows15/_state/tasks/p1/batch_002/gen_A/`. Did not modify `ideas_master.jsonl`, `research_state.json`, `research_ledger.md`, or `window.lock.json`.

## Cluster coverage (10 ideas each, 10 clusters)

| Cluster | Ideas | Focus |
|---|---|---|
| `label_assignment` | 001-010 | assignment entropy/churn, curriculum effects, conflict masking, gradient-mass accounting, shape/occlusion-conditioned sampling |
| `duplicate_suppression_nms` | 011-020 | box voting vs annotation variance, density-adaptive thresholds, suppression circuits in end-to-end models, duplicate-derived uncertainty, vocabulary-scaling of cross-class suppression |
| `box_regression_loss_geometry` | 021-030 | IoU-loss shrinkage bias, parameterization error structure, stride quantization floor, cls-reg Pareto front, cascade-as-affine-correction, loss-vs-feature attribution for elongated objects |
| `small_objects_scale` | 031-040 | label-noise ceiling, aliasing/phase effects, FPN oversmoothing, context-vs-appearance crossover, per-class resolution optima, scale-dependent forgetting, sub-stride information audits |
| `confidence_calibration` | 041-050 | score-semantics decomposition, frequency-scaling calibration law, background-shift threshold recalibration, jitter-based OOD signal, image-level vs box-level calibration, corruption-dose universality |
| `training_dynamics_optimization` | 051-060 | head under-training, per-task checkpoint optima, background overfit vs transfer, assignment-frozen validation loss, positives-based LR scaling, oversampling placement, EMA decomposition, warmup attribution, swing-image seed variance |
| `annotation_noise_gt_ambiguity` | 061-070 | modal/amodal inconsistency, ignore-region blind spots, structured missing labels, mid-training label auditing, score-mass splitting, dataset tightness bias, duplicate-GT paradigm sensitivity, contrast-snapping bias, jitter-averaging law, verified negatives |
| `evaluation_metrics` | 071-080 | mAP-vs-operating-point inversions, score-tail gaming, instance-weighted AP, continuous localization power, class-mapping sensitivity, error-profile decomposition, out-of-context reliance scalar, size-bucket artifacts, resolution-robustness curves, rank-based selection metrics |
| `context_background_cooccurrence` | 081-090 | background prototypes, context-reliance bimodality, head-localized priors, negative-context dominance, part-whole FP filter, artifact-FP direction, count priors, positional priors, size-asymmetric interference, entropy-adaptive thresholds |
| `test_time_robustness_deployment` | 091-100 | TTA redundancy law, flicker decomposition, branch-asymmetric quantization, BN batch-1 shifts, interference radius, resolution stair-steps, blur convention mismatch, difficulty routing, ensemble-gain prediction, latency jitter |

## Evidence-class distribution (tags, multi-tag per idea)

Heavy weighting toward cheap falsification: `inference_only_probe` and `public_checkpoint_reanalysis` dominate, followed by `small_scale_training`, `metric_reanalysis`, `ablation_study`, `synthetic_or_paste_intervention`, `annotation_audit`, `training_dynamics_logging`, `cross_architecture_comparison`. Every idea carries a `fastest_falsification` route, and roughly half can be first-pass falsified with inference-only or re-analysis work (no training).

## Notes for Wave B dedup (p1_wave_b_dedup_batch002)

- Nearest intra-shard neighbors to watch: 018 vs 030 (both elongated objects; 018 is NMS-operator geometry, 030 is loss-vs-feature attribution); 032 vs 037 (both grid-phase effects; 032 is aliasing/score oscillation, 037 is FN recovery via shifted inference); 077 (metric-side context reliance) vs 082/084 (mechanism-side context reliance); 095 vs 089 (both interference; 089 is object-to-object, 95 is background-to-object).
- Cross-shard collision risk with batch_001 (segmentation territories) should be low, but ideas 031, 061-070 (annotation noise) and 041-050 (calibration) have territory-agnostic analogues - dedup should compare on mechanism, not just topic words.
