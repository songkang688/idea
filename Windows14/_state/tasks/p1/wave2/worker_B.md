# Windows14 P1 Wave 2 — worker_B shard report

- task_id: p1_gen_w2_b
- role: worker_B
- windows_id / windows_path: Windows14
- territory: Super-resolution / restoration + diffusion models (restoration-segmentation coupling, generative priors, diffusion segmentation science)
- sub-domain hints used: microscopy/gigapixel WSI (JC-MT-03), video/streaming segmentation (JC-MT-05)
- output shard: `Windows14/_state/tasks/p1/wave2/worker_B.ideas.jsonl`
- idea_count: 126
- id_seed range: `w14w2b-001` .. `w14w2b-126` (shard-unique prefix `w14w2b-` per JC-QA-01)

## Method

Each idea is a single JSONL line with the 15 fields used by wave-1 shards
(`id_seed`, `one_line`, `cluster`, `problem`, `core_hypothesis`,
`falsifiable_prediction`, `why_important`, `why_possibly_novel`,
`minimal_falsification_experiment`, `main_risk`, `territory`,
`evidence_status`, `default_community_belief`, `why_it_might_be_wrong`,
`fastest_falsification`).

Every idea answers the three required questions:
1. what the community currently treats as true (`default_community_belief`),
2. why it might be wrong (`core_hypothesis` states the challenge; `why_it_might_be_wrong` is the honest self-skeptical caveat against the hypothesis, following the wave-1 field convention),
3. the fastest falsifying experiment (`fastest_falsification`, with `minimal_falsification_experiment` as the fuller design).

Generation avoided: module-A+B glue, pure attention/loss/backbone swaps, mechanical
method-to-domain transplants, scaling-only claims, and architecture engineering
without a scientific hypothesis. Uncertainty/calibration was NOT used as a primary
territory (capped per queue); the few ideas touching confidence or variance
(w14w2b-009, w14w2b-063) are framed as restoration-information-routing and
diffusion-methodology defects respectively, not as calibration contributions.

## Cluster map (126 ideas)

| cluster | count | ids | scope |
|---|---|---|---|
| restoration_segmentation_coupling | 14 | 001–014 | does SR/denoising/deblurring help or hurt segmentation; directional biases; covert channels |
| hallucination_fabrication | 12 | 015–026 | where generative restoration invents content; detectability; compounding |
| degradation_physics | 12 | 027–038 | noise models, ISP, demosaicing, compression, bit depth, exposure as physical laws |
| diffusion_priors_features | 14 | 039–052 | diffusion internals as segmentation signal; timestep/score/attention/latent-space science |
| diffusion_segmentation_models | 14 | 053–066 | mask-diffusion posterior fidelity, stochasticity collapse, decoding, guidance, self-conditioning |
| perception_distortion_downstream | 10 | 067–076 | task utility as third axis; metric-utility divergence; codecs and IQA blind spots |
| synthetic_loops_contamination | 10 | 077–086 | generated data in benchmarks/training; fingerprints, watermarks, self-consuming loops |
| microscopy_wsi | 14 | 087–100 | JC-MT-03: denoiser count bias, stain normalization, seams, focus, virtual staining, scanner leakage |
| video_streaming | 14 | 101–114 | JC-MT-05: codec structure, persistence bias, memory drift, interpolation, permanence hallucination |
| evaluation_science | 12 | 115–126 | how restoration/diffusion segmentation claims are (mis)measured; contamination, metric gaming |

## Epistemic status

- ALL 126 ideas carry `evidence_status: HYPOTHESIS`. No literature search was
  performed in this task; every `why_possibly_novel` field is explicitly marked
  HYPOTHESIS / unverified and phrased as "appears less explored / pending
  literature check", never as an absence-of-prior-work fact (JC-QA-02).
- No papers, citations, datasets, numeric results, or experimental outcomes were
  invented. Where prior-art families are gestured at (e.g. steganographic
  collusion in image translation, diffusion memorization, Noise2X denoisers,
  perception-distortion tradeoff), they are referenced as known research areas
  without fabricated specifics; each idea's claim remains a new falsifiable
  hypothesis to be checked against literature in the dedup/verification wave.

## Validation performed

- 126/126 lines parse as JSON; all 15 required fields present and non-empty on
  every line; no extra fields.
- `id_seed` unique and sequential `w14w2b-001..126`; prefix correct on all lines.
- `territory` and `evidence_status` uniform across the shard.

## Files written (this shard only)

- `Windows14/_state/tasks/p1/wave2/worker_B.ideas.jsonl`
- `Windows14/_state/tasks/p1/wave2/worker_B.md`
- `Windows14/_state/tasks/p1/wave2/worker_B.done.json`

Did NOT touch: `Windows14/_state/ideas_master.jsonl`,
`Windows14/_state/research_state.json`, `Windows14/_state/window.lock.json`,
or any `worker_A` / `worker_C` / `worker_D` / `worker_E` files under wave2.
