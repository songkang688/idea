# gen_q_inference_time_compute - shard summary

- task_id: p1_gen_q_inference_time_compute
- generator_id: gen_q_inference_time_compute
- windows: Windows13 (window_locked true)
- wave: p1_wave_a_w5
- branch: cursor/p1-gen-q-inference-time-f1b9
- idea_count: 100 (W13-P1-Q-001 .. W13-P1-Q-100, sequential, no gaps)
- schema: gen_j canonical (family_fingerprint + structured evidence_label dict + genre + needs_special_resources + seg_metric_dependent; numeric kill threshold inside every falsifiable_prediction; every fastest experiment states time/cost and names >= 1 public dataset AND >= 1 public model, or sets needs_special_resources=true)
- novelty_status: unverified on all 100 records

## Dispatch condition and queue provenance

Commissioned by the w2 diversity-audit decision (origin/cursor/p1-diversity-audit-consolidator-w2-942c, priority 5) with dispatch condition "only after gen_g is judged". Condition verified met: wave_b_w3 judged gen_g (canonical master at origin/cursor/p1-wave-b-consolidator-w4-e8e2 = 934 records includes accepted G ids; wave_b_w3_gate5/remaining_remand.jsonl enumerates the remanded remainder). No gen_q shard or done.json existed on any origin branch before this task (verified via git ls-remote + ls-tree scan).

## Territory covered (10 clusters, max share 12%)

| cluster | count |
|---|---|
| inference-compute-scaling-laws | 12 |
| ensembling-mechanisms | 10 |
| detection-search-decoding | 9 |
| verifier-guided-search | 10 |
| test-time-training-dense | 10 |
| anytime-early-exit | 9 |
| compute-allocation | 8 |
| retrieval-incontext-testtime | 8 |
| active-learning-folklore | 12 |
| psychophysics-contrast | 12 |

Fold-ins delivered as mandated: active-learning/data-acquisition folklore (12 records) and psychophysics-style human-model contrast designs (12 records).

## Genre and metric mix

- constructive_capability: 38 (38%) - meets >= 25% constructive quota
- audit_debunk: 10 (10%) - under the <= 40% pure-audit cap
- characterization_law: 52
- seg_metric_dependent: 39 true / 61 false - 61% of falsifications are NOT segmentation/mask-metric-bound (quota >= 30% non-seg)
- needs_special_resources: 3 (Q-090, Q-097, Q-100 - each requires new human psychophysics data; cost estimates stated in-record; all other 97 records run on public data + one GPU with stated time/cost)

## Guard self-audit

- HARD ANTI-OVERLAP (TTA-method critique banned as primary; gen_g owns G-001..G-014 plus remanded TTA ids): PASS. Zero records take entropy-minimization, batch-statistics adaptation, TTA hyperparameter circularity, stream collapse, do-no-harm gating, reset policies, episodic-protocol critique, or test-time prompt tuning as subject. The test-time-training cluster is constructive/characterization (aux-task selection laws, stopping rules, parameter-subset dissociations, teacher-anchored objectives, capacity cliffs, representation dynamics); records adjacent to gen_g claims carry explicit in-record scope notes (Q-009 vs G-009, Q-037 vs G-009, Q-042/Q-043 vs G-010, Q-044 vs G-004, Q-046 vs G-005, Q-049 vs G-005/G-011, Q-051 vs G-017).
- ANTI-OVERLAP gen_l (LLM/agent loops): PASS. All mechanisms are non-LLM (detectors, dense predictors, ensembles, retrieval memories, psychophysics probes). Records nearest to gen_l territory carry differentiation notes: Q-008/Q-017 vs L-025, Q-061 vs L-026. No agent orchestration, tool calls, or VLM reasoning loops anywhere.
- SAM cap (<= 5%): PASS. 1/100 records mention SAM (Q-076, a one-line differentiation note against accepted W13-P1-A-091; SAM is not the subject of any record).
- Calibration/uncertainty primary BAN: PASS. No cluster or record has calibration/uncertainty estimation as subject; no calibration metrics appear in any falsification. The word "uncertainty" appears only inside the active-learning cluster where uncertainty-sampling is the audited acquisition baseline (the commissioned folklore territory), plus two incidental phrase usages (Q-013, Q-063).
- HARD BAN smoke/fire/fog/transparent/amorphous-scattering: PASS (0 mentions; shift examples use synthetic-to-real, night, cross-dataset - never weather/scattering media).
- HARD BAN annotation/convention/label-noise as primary: PASS. AL records are framed entirely as acquisition value under matched budgets; zero label-noise/convention-pathology subjects (0 regex matches after cleanup).
- F1-F5 template ban: PASS (no PEFT-factorial-on-SAM, no SAM-component probes, no internal-score-as-free-detector framing - Q-055 explicitly avoids it via a trained behavioral gate, no cue-ablation-on-organisms, no published-deltas-are-noise primary framing - Q-058/Q-082 make specific mechanism-attributed protocol claims instead).
- Structure quota (>= 8 subclusters, none > 15%): PASS (10 clusters, max 12%).
- Cheap-predictor cap (<= 3): PASS at 3 (Q-042 gradient-alignment predicts TTT sign; Q-060 human speeded errors predict exit depth; Q-100 human RT tracks machine iterations - the latter two are primarily shared-difficulty laws and self-declare the cap note in-record).
- Equalization/matched-budget-null cap (<= 3): PASS at 3 (Q-016 TTA-vs-ensemble redundancy; Q-077 uncertainty-vs-random under strong backbones; Q-080 coreset-vs-cluster-sample). Other matched-budget records (Q-010, Q-021, Q-030, Q-037, Q-073) claim directional differences or crossover laws, not nulls.
- Counting-primary cap (<= 5): PASS (0 records with counting as primary subject).
- Realism-not-active-ingredient ban: PASS (0 records).
- Wave1-template-port rule: PASS - every eval-adjacent record (Q-053, Q-058, Q-065, Q-068, Q-082, Q-087) names a subject-native mechanism (class-prior amplification, exit-head decoder duplication, gain concentration, aliasing, composition-sensitivity of scratch retraining, duplicate avoidance).
- Avoided territories: no diffusion-internals science (gen_j; Q-004 uses a diffusion depth model only as a stochastic predictor whose sample count is the variable), no 3D/geometry/video modeling (gen_k; depth/flow appear only as dense tasks for test-time mechanisms, with in-record differentiation from K-019/K-026; Q-067 uses adjacent frames only as a density signal), no training-compute scaling/memorization/data-composition laws (gen_n), no hard-domain subjects (gen_o), no eval-repair protocol proposals (gen_p; Q-094/Q-099 build new psychophysics-native instruments instead), no adversarial/security/fairness (gen_u), no training-dynamics (gen_m; Q-018 consumes checkpoints at test time only).
- No fake citations: PASS. No bibliographic citation strings anywhere. Public datasets/models are named plainly (COCO, LVIS, CrowdHuman, Cityscapes, ADE20K, PASCAL VOC/5i, COCO-20i, FSS-1000, Mapillary Vistas, BDD100K, GTA5, NYUv2, DIODE, ETH3D, Sintel, KITTI, ImageNet(-C/-R), ObjectNet, CIFAR, Food-101, DTD, DomainNet, iNaturalist, PANDA, Argoverse-HD, AMASS; YOLOv8/YOLOX, RT-DETR, DINO-DETR, Faster/Mask/Cascade R-CNN, FreeSOLO, Pix2Seq, SegFormer, Mask2Former, UPerNet, DeepLabv3+, ViT/DeiT/ConvNeXt/ResNet/EfficientNet/Swin, DPT, MiDaS, Depth Anything v2, Marigold, RAFT, ViTPose, SegGPT, Painter, OWL-ViT, CLIP, DINOv2). Psychophysics reference values (Bouma constant, search slopes, channel bandwidths, human efficiency and psychometric-slope ranges) are labeled as model-recall KNOWN FACTS, unverified here, with no invented sources; the Geirhos model-vs-human public data release is referenced by name as a public resource.

## Kill-threshold and experiment gates

- 100/100 falsifiable_prediction fields contain a pre-registered numeric kill threshold with explicit "kill the idea if" language (GATE-1).
- 100/100 records carry the full structured evidence_label dict incl. prior_work_basis (GATE-2) and family_fingerprint (subject_system / manipulated_variable / measurement_family).
- 100/100 fastest_falsification_experiment fields state a time/cost bound; 97 run on public data + a single GPU; 3 set needs_special_resources=true with explicit human-data cost estimates (GATE-3).
- 100/100 fastest experiments name at least one public dataset and at least one public model (GATE-4).
