# P1 Wave A Generator Report - batch_002 gen_C (T06 failure mining)

- **task_id:** `p1_wave_a_batch002_gen_C`
- **windows:** Windows15 (locked; lock verified against `Windows15/_state/window.lock.json` and the P1 state reader's `state.json`, both untouched)
- **territory:** T06 failure mining
- **idea_count:** 100 (target 100, min 80)
- **id range:** `W15-B002-C-001` .. `W15-B002-C-100` (sequential, no gaps, validated by script)
- **output:** `Windows15/_state/tasks/p1/batch_002/gen_C/ideas.jsonl` (one JSON object per line)

## Scope and interpretation

Per the task queue's generator contract, all entries are scientific hypotheses about
systematic failure modes of vision foundation models, VLMs, segmenters, and detectors —
proposed failure laws, ignored assumptions, and measurement blind spots. None of them
are "add a failure-mining module" engineering proposals. Every idea carries the 13
required fields including `community_default_belief`, `why_that_may_be_wrong`, and
`fastest_falsification` in addition to the base contract fields.

## Hard-rule compliance

- `why_possibly_novel` is phrased as a hypothesis in every entry and each one explicitly
  carries a "(not verified)" marker; no verified-novelty claims are made.
- No invented citations, no fabricated benchmark numbers, no claimed experimental results.
  Where public artifacts are named (SAM, DINOv2, CLIP, COCO, LVIS, ADE20K, Swin, DETR,
  ToMe-style merging, LAION-scale corpora), they are used only as well-known experiment
  substrates, never with attributed quantitative results.
- Writes confined to `Windows15/_state/tasks/p1/batch_002/gen_C/`. Canonical ledgers
  (`ideas_master.jsonl`, `research_state.json`, `research_ledger.md`, `window.lock.json`)
  untouched. No new Windows directories created.

## Cluster composition (12 clusters, 100 ideas)

| Cluster | Count | Angle |
|---|---|---|
| vlm-failure-modes | 14 | language-prior override thresholds, counting psychophysics, chirality, negation geometry, binding capacity laws, token-compression hallucination, OCR crutch, caption-style likelihood, yes-bias, sycophancy exchange rate, chart tick quantization, multi-image serial position, viewpoint frequency forecasting |
| annotation-convention-leakage | 9 | boundary convention offsets, amodal/modal blending, crowd-ignore suppression, watermark shortcuts, co-occurrence hallucination law, center bias fingerprints, polygon curvature ceilings, GT false-negative echo, white-composite shortcut |
| meta-assumptions-eval-blindspots | 9 | near-duplicate contamination, failure burst autocorrelation, human adjudication boundary, failure-mass conservation under benchmark targeting, anthropomorphic cause misattribution, contested ground truth, objective-function fossils, auto-label amplification law, literature aesthetic curation |
| tokenization-grid-artifacts | 8 | patch-phase periodicity, patches-per-object cliffs, aspect distortion, pos-embed interpolation zones, artifact/register tokens, orientation aliasing, window seams, token-merging damage concentration |
| cross-model-failure-correlation | 8 | shared-data failure floor, distillation phylogeny, failure persistence bimodality, TTA confident-wrong blind spot, natural-adversarial subspace overlap, scale transfer asymmetry, backbone monoculture, low-rank failure geometry |
| detector-failure-modes | 8 | pre-NMS stage attribution, DETR query niches, small-object context reliance, threshold portability, aspect-ratio cliffs, pair-recall collapse signatures, label-space vs perception decomposition, border truncation policy |
| segmentation-failure-modes | 8 | topology censoring by IoU, genus prior / hole filling, SAM granularity instability, stuff-thing fragmentation threshold, reflection/transparency taxonomy, shadow convention floor, scale-anchoring class flips, interactive click divergence |
| distribution-shift-microstructure | 8 | per-instance failure cliffs, interaction-dominated failure budgets, robustness anisotropy, camera ISP fingerprints, metadata-dominated mined clusters, transition-regime failures, clipping leakage law, sim-real asymmetry diagnostics |
| failure-prediction-self-knowledge | 8 | linear feature legibility of failures, sharpness repairability, jitter vs confidence, mining selection bias, post-hoc verbalized confidence, taxonomy instability, repair-damage locality kernel, early-training determination |
| preprocessing-pipeline | 7 | JPEG-absence OOD, interpolation kernel mismatch, metadata mishandling share, gamut clipping, normalization luminance tails, video chroma entrainment, resample-signature reliance |
| confidence-calibration-geometry | 7 | confident/diffident error dichotomy, severity anti-alignment, score-localization decoupling, prior-shift law, style bifurcation, SAM quality-head prompt shift, distance-conditioned temperature |
| temporal-video-failures | 6 | flicker as catastrophe precursor, blur direction dependence, shuffle-test static bias, occlusion memory horizon, motion-per-frame shift, video lost-in-the-middle |

## Notes for Wave B dedup (p1_wave_b_dedup_batch002)

- Nearest-neighbor risk inside this shard was managed deliberately: C-009 (JPEG absence)
  vs C-016 (resample signature) are distinct corruptions with a factorial-separation note in
  C-016; C-030 (TTA agreement) vs C-081 (jitter inconsistency) target different signals
  (augmentation-vote agreement vs sub-pixel stability) and different claims (blind spot vs
  superiority); C-035 (error dichotomy) vs C-082 (mining selection bias) share the
  confident-error concept but make orthogonal claims (mitigation invariance vs sampling bias).
- Likely cross-shard collision surface: batch_002 gen_A (T04 object detection) may overlap
  with the detector-failure-modes cluster (C-055..C-062); gen_B (T05 VLM / dense prediction)
  may overlap with the vlm-failure-modes cluster (C-042..C-054). Dedup should compare on
  core_hypothesis rather than territory labels, since this shard frames everything as
  failure laws rather than methods.
- No entries here were checked against batch_001 shards or other generators' outputs;
  novelty fields are hypotheses only.

## Self-checks performed

- JSONL parse: 100/100 lines valid JSON.
- Required fields: 13/13 present and non-empty on every line.
- ID sequence: exact match to `W15-B002-C-001..100`, no duplicates.
- Grep audit: every `why_possibly_novel` contains a not-verified disclaimer; no numeric
  performance claims presented as results.
