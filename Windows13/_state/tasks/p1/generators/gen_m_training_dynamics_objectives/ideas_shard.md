# gen_m_training_dynamics_objectives — ideas shard (W13, P1 Wave A w3)

- **windows_id / path:** Windows13 (window_locked: true)
- **task_id:** p1_gen_m_training_dynamics_objectives
- **id range:** W13-P1-M-001..W13-P1-M-100 (100 ideas)
- **wave:** p1_wave_a_w3 | **novelty_status:** unverified (Wave B dedup + novelty verification pending)
- **retry note:** this is the retry of the gen_m dispatch that was interrupted (billing) with no origin shard; an all-origin-branch scan before generation confirmed no prior `gen_m_training_dynamics_objectives/done.json` anywhere on origin.

## Territory
Within-run training dynamics, fine-tuning dynamics, optimizer/schedule folklore, and objective-function science for dense prediction beyond focal+dice. The mechanism class of B-057/B-080/B-024 (target parameterization as gradient-conditioning device) is generalized onto depth, optical flow, surface normals, keypoint heatmaps, distance fields, and output-distribution coupling — none of those three ids is cloned and no scattering-media example appears anywhere. Model-lifecycle/version-drift content is deliberately absent (reserved for gen_v); every idea is about dynamics inside a single training run (multi-stage fine-tuning pipelines appear only where the mechanism claim is about within-run conditioning).

## Clusters (11; max share 10%)
| cluster | n |
|---|---|
| target-parameterization-geometry | 10 |
| objective-gradient-geometry | 10 |
| optimizer-mechanism-science | 10 |
| schedule-warmup-folklore | 10 |
| finetuning-trajectory-dynamics | 10 |
| acquisition-order-phase-transitions | 10 |
| gradient-interference-multiobjective | 10 |
| normalization-precision-dynamics | 8 |
| batch-sampling-dynamics | 8 |
| augmentation-as-optimization | 8 |
| instability-spike-science | 6 |

## Genre mix
characterization_law 58 / constructive_capability 26 / audit_debunk 16 (constructive 26% >= 25%; pure audit/debunk 16% <= 40%).

## Guard self-audit (see done.json for the full numeric block)
- HARD ban add-loss-term-X-to-task-Y: no record proposes adding a loss term to a task; every objective-related idea states a WHEN/WHY mechanism with a numeric kill threshold. Loss-combination records (e.g., M-017) are meta-laws about when combinations work, not combination proposals.
- SAM/SAM2: 0 records (0% <= 5%).
- Calibration/uncertainty: not a cluster; the single occurrence of the word "calibration" is a differentiation reference to occupied W13-P1-D-031.
- Smoke/fire/fog/transparent/amorphous-scattering examples: 0.
- F1–F5 template families (PEFT-factorial-on-SAM, SAM-component probes, internal-score-as-free-detector, cue-ablation-collapse on scattering organisms, published-deltas-are-noise): 0 records; run-variance/delta-noise framing avoided entirely (M-048 audits the informativeness of early transients, not delta noise).
- Annotation/convention/label-noise as primary subject: 0 (label smoothing in M-090 is an objective modification, not annotation noise).
- cheap-predictor-of-Y: 3 (M-017, M-064, M-097) at the cap.
- equalization/matched-budget-null: 3 (M-015, M-032, M-058) at the cap; mechanism-substitution designs (matched-ingredient recovery, e.g. M-002/M-007/M-013/M-063) are a different falsification family and are spread across clusters with distinct fingerprints.
- small/dense/crowded/counting as primary: 2 (M-055 thin-structure critical period, M-005 thin-class gradient concentration) <= 5; no counting/crowd records.
- realism-not-active-ingredient framing (gen_f): 0; no synthetic-data records at all.
- Colonization check: no diffusion, no SR/restoration, no 3D/geometry/video-primary (flow appears only as a dense-regression target for parameterization science), no LLM/agent, no security/fairness, no scaling-law/memorization-privacy/data-composition, no domain-shift/TTA, no hard-domain diversification, no eval-protocol critique. Occupied ids (D-031, D-050, E-075, E-076, F-036, F-048, F-058, F-089, F-095) are not restated; where adjacent (M-016 vs D-031, M-008 vs D-050, M-018/M-085 vs E-075, M-065/M-069 vs F-036) the record carries an explicit differentiation note.
- Numeric kill + falsified-if: 100/100 records carry a numeric threshold and an explicit kill condition inside `falsifiable_prediction`.
- Fastest experiments: 99/100 name >= 1 public dataset AND >= 1 public model with a time/cost bound on one GPU; M-030 sets `needs_special_resources: true` (multi-GPU batch ladder) and still names public data/models.
- seg/mask-metric-bound falsifications: 61%; 39% of records have kill branches evaluable without segmentation/mask metrics (>= 30% required). `seg_metric_dependent=true` was assigned only when every kill branch requires a segmentation/mask metric.
- No citations are fabricated: no reference strings appear anywhere; prior-work claims are labeled as unverified model recall inside `evidence_label.prior_work_basis`. Novelty is never claimed as verified.

## Files
- `ideas_shard.jsonl` (100 records, gen_j-compatible schema incl. `family_fingerprint` + `evidence_label`)
- `ideas_shard.md` (this file)
- `done.json`
