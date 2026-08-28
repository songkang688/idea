# P1 Wave A — worker_C (Windows14)

- **Task:** `p1_gen_w1_c` (Stage P1 Massive Idea Exploration, Wave A generator)
- **Territory:** Smoke / fire / ambiguous (transparent) object segmentation + failure mining
- **Status:** complete
- **Window lock:** verified before writing — `Windows14/_state/window.lock.json` has `locked: true`, `windows_id: Windows14`, `windows_path: Windows14`. No Windows directories created, no numbering scan performed, no canonical ledgers touched.

## Output

- `Windows14/_state/tasks/p1/wave1/worker_C.ideas.jsonl` — **124 candidate ideas**, one JSON object per line.
- Every object carries: `id_seed`, `one_line`, `cluster`, `problem`, `core_hypothesis`, `falsifiable_prediction`, `why_important`, `why_possibly_novel`, `minimal_falsification_experiment`, `main_risk`, `territory`, `evidence_status="HYPOTHESIS"`, `default_community_belief`, `why_it_might_be_wrong`, `fastest_falsification`.
- All lines validated as parseable JSON with all 15 required fields non-empty; ids `w14p1c-001` … `w14p1c-124`, no duplicates.
- `ideas_master.jsonl` was **not** written (merging is a later consolidator task).

## Generation stance

Falsifiable hypotheses over architecture mashups: each idea names a specific failure mechanism or belief about SAM/VFM behavior on smoke, fire, transparent, low-contrast, or amorphous targets, plus a quantitative prediction and the cheapest experiment that could kill it. Novelty claims are hedged (`why_possibly_novel` states why it *might* be new); **no novelty was verified against literature** — that is downstream work. No papers, benchmarks, or experimental results were fabricated; where experiments need datasets, they are described generically (e.g., "a public smoke set", "multi-annotator subset") rather than by asserted named results.

## Cluster map (14 clusters, 124 ideas)

| cluster | n | focus |
|---|---|---|
| sam_prompt_failure_amorphous | 11 | click jitter instability, see-through capture, multimask collapse, dead zones, everything-mode blindness, prompt-ensemble density, forgetting asymmetry |
| edge_texture_frequency_bias | 9 | frequency-band ablations, fake-contour rescue, chroma vs luminance splits, spectral-slope probes, layer-depth inversion, positional shortcuts |
| transparent_object_failures | 11 | background-content dominance, refraction warp blindness, highlight anchoring, interior-vs-boundary taxonomy, rim supervision, depth negative transfer, mesh topology |
| fire_photometric_failures | 9 | saturation-contour tracking, bloom halos, unused flicker, chroma MLP baseline, reflection FPs, day/night gating, amodal fire, annotation conventions, donut cores |
| soft_mask_matting_density | 10 | alpha-matting reframing, ranking annotation, exact-alpha composites, dehazing transmission reuse, metric validity, unsupervised video alpha, format routing |
| temporal_video_failures | 9 | temporal-variance baseline, memory shrinkage, topology-change failures, flow divergence, hybrid prompting, band-split filters, latency-vs-IoU decoupling, fps cliffs |
| uncertainty_calibration | 8 | calibration-gap as detector, jitter-vs-human disagreement, bias-not-variance ensembles, conformal masks, selective prediction, confidence inversion, familiar-but-incompetent OOD |
| metrics_annotation_ambiguity | 9 | annotation noise floor, ignore-band re-ranking, threshold-offset audits, event-vs-pixel metrics, instruction effects, event leakage, tiny-instance metrics, transfer matrix |
| failure_mining_methodology | 9 | renderer-space failure manifolds, cross-VFM transfer, FP cluster cardinality, source-inpainting counterfactuals, caption slices, corruption fingerprints, prompt-space margins, active-learning inversion, sim2real fidelity axes |
| semantic_confusion_openvocab | 8 | synonym variance, steam/smoke context ceiling, horizon shortcuts, density-gradient vs CLIP, dust temporal priors, caption-frequency ladders, negation blindness, attribute prompts |
| physics_priors_crossmodal | 9 | gravity prior ledger, advection consistency, scattering-color reranking, thermopile fusion, RGB−NIR difference, shadow validation, polarization vs reflections, turbulence spectra, depth-scale disentanglement |
| representation_probing | 8 | attention entropy, register-token contamination, patch-size ceiling, linear haze direction, SSL-vs-supervised reversal, matter-type undersampling, token-merging harm, alpha decodability |
| data_synthesis_supervision | 8 | composite-vs-diffusion data, background-vs-plume diversity, copy-paste shortcuts, temperature-swept flames, dilation asymmetry, motion pseudo-labels, negative-set budgets, fog-augmentation poisoning |
| deployment_robustness | 6 | bitrate cliffs, lens-contamination permanence, auto-exposure self-hiding, pixels-per-plume scaling law, distillation band loss, rolling-shutter shortcut |

## Unresolved items (for downstream waves)

1. **No novelty verification performed** — every `why_possibly_novel` is a hypothesis; Wave B/C must dedup against sibling shards (worker_A SAM/PEFT, worker_B medical) and, later, against literature.
2. **Expected cross-shard overlap:** SAM prompt-behavior and PEFT/forgetting ideas (w14p1c-001…011) may collide with worker_A's SAM territory; uncertainty/ambiguity ideas (w14p1c-060…067) may collide with worker_B's medical inter-observer-variability ideas. Flagged for the dedup pass.
3. **Intra-shard adjacency to watch during dedup:** w14p1c-018 vs -107 (layer/SSL probing), -044 vs -089 (transmission-map reuse), -034 vs -056 (flicker bands), -061 vs -066 (disagreement maps), -016 vs -110 (alpha-parameterized composites).
4. Several minimal experiments assume access to multi-annotator smoke labels or alpha-composite pipelines that may need to be built once and shared across experiments; a consolidator could factor out this shared infrastructure.

## Recommended next task type

`p1_wave_B_dedup` — merge/dedup the three Wave-A shards before any acceptance into `ideas_master.jsonl`.
