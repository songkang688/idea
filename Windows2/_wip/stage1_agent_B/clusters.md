# Windows2 Stage 1 — Agent B Cluster Map

Agent B's exclusive angle territory: vision foundation models (VFM), multimodal/VLM dense
failure, fine-tuning instability, PEFT limits, forgetting, prompt sensitivity, representation
mismatch, frozen-vs-tuned transfer, synthetic adaptation data, medical VFM science,
language-geometry alignment, and hypothesis-driven agentic vision. Agent A covers
SAM/medical/smoke segmentation; Agent C covers detection/eval/assumptions — no overlap intended.

Total: 345 ideas, IDs `W2-B-0001` … `W2-B-0345`.

| # | Cluster key | ID range | Count | Theme |
|---|-------------|----------|-------|-------|
| 1 | `vfm_failure` | 0001–0035 | 35 | Failure modes of CLIP/DINOv2-v3/SigLIP/MAE/LVLM features: outlier tokens, spectral deficits, resolution extrapolation, inverse scaling, aliasing, seed/curation confounds |
| 2 | `vlm_dense_failure` | 0036–0070 | 35 | Referring/open-vocab segmentation and grounding: spatial-prior answering, negation blindness, hallucinated grounding, synonym instability, compositional and pragmatic failures |
| 3 | `finetune_instability` | 0071–0100 | 30 | Loss spikes, warmup and LN transients, seed/order variance, modality-gap collapse, sharpness transfer, inverse stability scaling, hardware noise floors |
| 4 | `peft_limits` | 0101–0135 | 35 | When PEFT is the wrong tool: intrinsic-rank shortfall, wrong-invariance preservation, calibration and fairness costs, shift crossovers, privacy inversion, placement dissociations |
| 5 | `catastrophic_forgetting` | 0136–0165 | 30 | Rotation-vs-erasure, beneficial forgetting, forgetting chronologies and cascades, decoder-capacity law, measurement biases, savings paradigm, layerwise fingerprints |
| 6 | `prompt_sensitivity` | 0166–0195 | 30 | Prompt jitter/order/negatives, calibration by prompt modality, policy-artifact evaluations, prompt attacks, granularity pragmatics, prompt-free default masks |
| 7 | `representation_mismatch` | 0196–0225 | 30 | Global contrastive geometry vs pixel needs: equivariance spectra, spectral dissociation, upsampling bottleneck, subspace splits, cosine-vs-metric geometry, sufficiency bounds |
| 8 | `crossdomain_frozen_vs_tuned` | 0226–0253 | 28 | Shift budgets, style/content double dissociation, phase boundaries, convention gaps, aging profiles, input-only adaptation sufficiency, equity effects of tuning |
| 9 | `synthetic_adaptation` | 0254–0278 | 25 | Generated data for adaptation: calibration costs, fingerprints, circularity/inbreeding, mixing laws, nameability limits, collapse canaries, spectral-coverage sign prediction |
| 10 | `medical_vfm_science` | 0279–0303 | 25 | Scientific questions about medical VFMs (not "train MedFM"): sufficiency maps, invariance-vs-findings conflicts, site invariance, prevalence shift, leakage, metric-utility divergence |
| 11 | `language_geometry_alignment` | 0304–0328 | 25 | How language supervision shapes/distorts dense geometry: categorical quantization, boundary-vocabulary poverty, MIL identifiability, mentioned bias, style-controlled supervision |
| 12 | `agentic_vision_hypotheses` | 0329–0345 | 17 | Agents/tools only where a vision hypothesis is testable: broken uncertainty chains, verification independence, CoT faithfulness, contamination, agent-vs-scale frontiers |

## Cross-cluster threads (mutation lineages)

Ideas marked `mutate_from` form lineages that the supervisor can treat as evolvable families:

- **Outlier/register tokens:** 0001 → 0027 (norm as uncertainty), 0031 (register ablation),
  0076 (bf16 instability locus), 0114 (VPT-as-registers), 0224 (registers improve patch purity).
- **Invariance as liability:** 0019 (color augmentation) → 0034, 0104 (PEFT preserves wrong
  invariance), 0201 (per-augmentation information cost), 0280/0282/0289 (medical invariance
  conflicts), 0196 (equivariance deficit spectrum).
- **Nameability boundary:** 0026 (unnameable regions) → 0243 (text-steered adaptation),
  0271 (generation-based adaptation), 0306/0309/0321/0323 (vocabulary poverty family).
- **Calibration as leading indicator:** 0053 → 0087 (post-spike scars), 0108 (PEFT calibration),
  0145 (calibration forgotten first), 0180/0194 (prompt-conditional calibration), 0246
  (calibration transfer), 0254/0272 (synthetic-data calibration), 0285/0303 (medical prevalence
  and ROC tails), 0340 (calibration dies at tool boundaries).
- **Frozen-vs-tuned regime theory:** 0112 → 0226 (shift budgets) → 0234 (phase diagram) →
  0241 (style/content dissociation) → 0249 (aging) → 0297 (scanner updates).
- **Mechanism attribution for PEFT:** 0095 → 0098 (LoRA = rescaled LR?) → 0126 (divergence
  onset), 0111 (dropout = interpolation), 0106 (BitFit = moment matching), 0121 (linearity).
- **Forgetting measurement reform:** 0136 (rotation vs erasure) → 0157 (template staleness),
  0163 (OOD probes), 0164 (savings paradigm), 0165 (layerwise fingerprints) → 0252
  (interpolation frontier kinks).
- **Self-referential data loops:** 0262 (self-filtering) → 0269 (closed-loop prompts),
  0275 (dense collapse canary) → 0277 (pseudo-label heredity) → 0343 (agent self-training).

## Counter-intuitive flagship hypotheses (per mission brief)

- More parameters can hurt OOD/dense: 0013 (small-object inverse scaling), 0092 (inverse
  stability scaling), 0182 (scale increases prompt sensitivity on rare classes).
- Language supervision may worsen dense geometry: 0307 (depth), 0304 (shape quantization),
  0209 (regression vs classification), 0321 (texture boundaries).
- PEFT may preserve the wrong invariance: 0104, plus 0102 (intruder dimensions), 0122
  (readout-dependent forgetting claims), 0133 (privacy inversion).
- Forgetting can be desirable: 0137 (typographic vulnerability shed), 0151 (OCR loss
  consequences), 0158 (positive backward transfer).

## Verification discipline

Prior-work claims that could not be verified from memory are tagged
`UNVERIFIED — needs lit search` inside the relevant idea fields (68 of 345 ideas carry the tag).
No citations, numbers, or paper names were fabricated; named phenomena (registers, modality
gap, WiSE-FT-style interpolation, LP-FT feature distortion, POPE-style hallucination) are
used as widely-known reference points and still require citation checks at Stage 2.
