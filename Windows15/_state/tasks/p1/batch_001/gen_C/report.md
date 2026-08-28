# P1 Wave A Generator C Report — Windows15 / batch_001

- Task: `p1_wave_a_batch001_gen_C`
- Role: generator (Wave A)
- Parent: Windows15 dispatcher
- Territory: **T03 Smoke / fire / transparent or ambiguous object segmentation** (ambiguous / transparent / volumetric / boundary-undefined objects)
- Base branch: `origin/cursor/windows15-p1-state-reader-a5fa`
- Output dir: `Windows15/_state/tasks/p1/batch_001/gen_C/` (only location written)
- Idea count: **100** (`W15-B001-C-001` … `W15-B001-C-100`), within the contract range 80–120.

## What was generated

100 distinct scientific hypotheses about objects whose boundaries are physically undefined
(smoke, fire, fog, steam, dust, spray), transparent/refractive (glass, liquids), or volumetric.
Per the scientific bar, these are observations, falsifiable hypotheses, failure modes,
ignored assumptions, counterintuitive-result candidates, metric critiques, and
foundation-model systematic-defect claims — **not** "apply method X to smoke" transfers,
module combinations, attention/loss swaps, or scale-up proposals.

Each idea record contains: `idea_id`, `one_line`, `cluster`, `problem`, `core_hypothesis`,
`falsifiable_prediction`, `why_important`, `why_possibly_novel`,
`minimal_falsification_experiment`, `main_risk`, `community_default_belief`,
`why_that_may_be_wrong`, `fastest_falsification`, `evidence_class` (tags).

## Cluster coverage (100 ideas)

| Cluster | Count | Focus |
|---|---|---|
| ontology_problem_formulation | 10 | What is the "object"? Threshold artifacts, exposure-defined flame extent, ill-posedness of 2D labels for volumes, fractal boundaries, media as a third ontology category. |
| annotation_epistemology | 8 | Disagreement as density signal, motion-resolved labels, tool signatures, trimap economics, downwind truncation bias, consensus-vs-sample labels, layer counting, negative-evidence labels. |
| image_formation_physics | 10 | Beer–Lambert decomposition, detectability limits, emitter-vs-surface fire, refraction warp fields, specular viewpoint dependence, chromatic neutrality, smoke shadows, haze convergence at distance, polarization, motion-sparsity dichotomy. |
| foundation_model_defects | 10 | Boundary snapping to background gradients, prompt fall-through as an opacity probe, cross-model disagreement as a glass detector, context-grounded open-vocab responses, topology deficits, prompt-jitter ambiguity meter, transmittance linear probes, interactive-click oscillation, day/night bimodality, tracker decorrelation half-life. |
| evaluation_metrics | 10 | Metric-relative SOTA, resolution-unstable boundary metrics, human-preference divergence, detectability weighting, protocol-swap domain gap, distractor decorrelation, temporal-consistency conflicts, instance-convention variance, construct validity, category leakage in glass. |
| temporal_dynamics | 8 | Tiny temporal-statistics models, turbulence spectra, flow divergence as emission state, flicker as camera artifact, gravity alignment, adaptive frame averaging, camera micro-motion for glass, propagated-label half-life. |
| multimodal_sensing | 7 | Thermal–visible disagreement, cool-smoke thermal null, VIS/NIR particle sizing, depth-dropout signatures, audio-supervised flame, flash/no-flash densitometry, rolling-shutter flicker recovery. |
| shortcut_learning_failure_modes | 10 | Color-reliance index, skyline shortcut, context-dependence ratio, compression cliff, fire-context hallucination coupling, rim reliance, white-blob representational collapse, night glare masks, curation-induced latency, natural-adversarial taxonomy. |
| representation_output_space | 10 | Log-transmittance additivity, nested level sets, boundary distributions, layered glass decomposition, joint spectral factorization, turbulent-parallax 3D, layer counting, presence-vs-evidence dual masks, amodal dissociation, multi-hypothesis ambiguity atlas. |
| contrarian_counterintuitive | 10 | Scale hurts, downsampling helps, blur as diagnostic, matting pretraining wins, noise beats architecture, mask quality delays alarms, novices beat models, clutter helps glass, unrealistic-but-correct synthetic wins, boundary precision is wasted budget. |
| datasets_synthetic | 7 | Compositing shortcut dynamics, metered physical-alpha capture protocol, physics-predicted transfer matrix, flame-chemistry OOD axis, viral-footage leakage, generated-smoke spoofing, transparent-liquid dynamics gap. |

## Compliance notes

- **Novelty is hypothesized, never claimed as verified.** Every `why_possibly_novel` field is
  phrased as an unverified belief and explicitly marked "(not verified)". Wave B dedup and any
  later literature verification remain responsible for actual novelty checks.
- **No invented citations, papers, benchmark names, datasets, or numeric results.** References to
  real, well-known artifacts are generic (e.g. "promptable segmenters", "self-supervised ViT
  features", Beer–Lambert law, Kolmogorov turbulence) and no quantitative claims are asserted as
  established facts; all numbers appear only inside predictions to be tested.
- **Distinctness:** ideas were generated cluster-first with one hypothesis/mechanism per record;
  where two ideas touch the same phenomenon (e.g. C-010 fractal boundaries and C-040 metric
  instability), one is the observation/measurement and the other the metric/benchmark consequence,
  and they cross-reference rather than duplicate.
- **Locked window respected:** wrote only inside `Windows15/_state/tasks/p1/batch_001/gen_C/`;
  did not touch `window.lock.json`, `research_state.json`, `ideas_master.jsonl`,
  `research_ledger.md`, or any other `gen_*` directory.

## Validation performed

- `ideas.jsonl`: 100 lines, every line parses as JSON, all 14 required fields present and
  non-empty on every record, `evidence_class` is a list on every record.
- IDs are exactly `W15-B001-C-001` through `W15-B001-C-100`, unique, in order.

## Unresolved items (for the parent / Wave B)

1. Novelty of all 100 ideas is unverified by construction; Wave B dedup should collapse
   near-neighbors across gen_A/B/C shards and any later literature-check stage should audit the
   `why_possibly_novel` claims.
2. Several ideas share experimental infrastructure (controlled fog-machine captures with
   physical instrumentation: C-011, C-015, C-019, C-020, C-047, C-081, C-095). If any advance
   past Stage 1, they should be batched around a single capture campaign.
3. Intra-shard thematic overlap flagged for the dedup consolidator: C-001/C-043/C-075
   (annotator-threshold family), C-010/C-040 (fractal boundary family), C-030/C-034
   (prompt-perturbation family), C-017/C-080 (layer-counting family). All are distinct
   hypotheses but are the closest pairs in this shard.

## Recommended next task

`p1_wave_b_dedup` — batch_001 dedup consolidation across gen_A, gen_B, gen_C shards.
