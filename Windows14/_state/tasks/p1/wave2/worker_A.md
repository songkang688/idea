# P1 Wave 2 - worker_A: Synthetic data + domain shift

- **task_id**: p1_gen_w2_a
- **role**: worker_A (generator, wave 2)
- **windows_path**: Windows14 (lock verified: `_state/window.lock.json`, locked=true)
- **territory**: Synthetic data + domain shift (generation-for-segmentation, sim-to-real, distribution shift science)
- **output**: `Windows14/_state/tasks/p1/wave2/worker_A.ideas.jsonl` (133 ideas)
- **id_seed prefix**: `w14w2a-` (per queue shard rule JC-QA-01)

## Coverage by cluster (133 total)

| cluster | count | scope |
|---|---|---|
| synthetic_scaling_laws | 12 | scaling/saturation of synthetic data value, mixing ratios, contamination via generators, stopping rules |
| sim2real_gap_anatomy | 12 | decomposition of the gap: frequency bands, layout vs appearance, ISP, shadows, occlusion statistics, camera pose |
| generative_pair_fidelity | 12 | generation-for-segmentation: mask-image alignment bias, filtering pathologies, layout provenance, self-generation collapse |
| renderer_fingerprints | 10 | shortcut learning from renderer/generator artifacts, leakage probes, artifact-randomization critical periods |
| sar_remote_sensing_shift | 12 | speckle, incidence angle, DEM-based simulation, phenology, PSF, geographic transfer, calibration drift (queue sub-hint JC-MT-01) |
| lidar_driving_shift | 11 | ray-drop/intensity, beam patterns, weather clustering, rolling shutter, behavior-model signatures, night bimodality (JC-MT-02) |
| vertical_domains | 11 | underwater optics/biofouling, industrial defects/specular/belt drift, agriculture soil/phenology/orchards, livestock, construction (JC-MT-04) |
| shift_measurement_science | 12 | metrics that predict transfer, aggregation form, transferability-estimator failures, early-warning metrics, entropy-delta regimes |
| adaptation_training_dynamics | 11 | critical periods, boundary-first forgetting, norm-recalibration null model, self-training/adversarial mechanism decompositions |
| synthetic_data_harms | 10 | harm attribution and pruning, prior mismatch, uncanny-valley harm, poison tails, shape contraction, benchmark contamination, distillation inheritance |
| domain_randomization_science | 10 | what DR actually confers, sub-additivity, invariance overdraft, on-manifold sampling, active DR, TTA-equivalence audits |
| shift_theory_taxonomy | 10 | tiered shift taxonomy, error propagation, label-convention artifacts, composition laws, granularity amplification, gap locus |

## Constraints observed

- All ideas `evidence_status="HYPOTHESIS"`; no novelty claims stated as verified fact (novelty framed as "appears untested/unmeasured" per JC-QA-02); no fabricated papers, numbers, or results.
- Avoided SAM+X / LoRA+X / loss+X mashup formulas; ideas are mechanism/measurement/decomposition claims with falsifiable predictions and minimal experiments.
- Uncertainty/calibration territory is capped per queue: only touched incidentally where central to a synthetic-data mechanism (e.g., w14w2a-035, w14w2a-092), not as a cluster.
- Did not write `ideas_master.jsonl`, did not touch the window lock, `research_state.json`, or any wave-1 or sibling shard files (no worker_D/worker_E files existed; none created).

## Unresolved items

- Duplicate-risk zones for Wave B dedup: within-shard neighbors flagged for judge attention — (w14w2a-013 vs w14w2a-022: both spectral/boundary-geometry accounts of the residual gap), (w14w2a-041 vs w14w2a-126: label-convention artifact measured from model side vs relabeling side), (w14w2a-006 vs w14w2a-094: boundary-metric scaling vs boundary-first forgetting), (w14w2a-003 vs w14w2a-111: U-shape mechanism vs cool-down remedy). Kept separate because falsification designs differ.
- Cross-shard overlap possible with worker_C (negative results/contrarian): w14w2a-096, w14w2a-097, w14w2a-098 (null-model / mechanism-decomposition claims) have contrarian character; dedup pass should check worker_C shard.
- No literature verification performed (per task constraints); all "why_possibly_novel" fields are hypotheses about the literature, not search-backed claims.
