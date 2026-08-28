# Stage 3 — Cluster B Keep List (14 KEEP)

Survivors of the adversarial prior-work hunt. Each entry: what survives, the closest real prior work, why it does
not kill the idea, and novelty confidence. Six additional mutated ideas live in `stage3_cluster_B_mutations.md`.

| # | ID | Idea (one line) | Closest prior work | Why prior work doesn't kill it | Novelty conf. |
|---|----|-----------------|--------------------|-------------------------------|---------------|
| 1 | B-0058 (P) | Unsupervised MoE routing as a free pathology detector in medical FMs | V-MoE routing analyses (Riquelme et al., NeurIPS 2021); AnomalyMoE (2025) | Prior MoE-AD work *engineers* the router with supervision; the emergent-routing-detects-pathology question is untested | Medium |
| 2 | B-0062 | Physically calibrated per-pixel smoke transmittance ground truth (absorbs B-0069 metric-validation arm) | A2I2-Haze (2022, transmissometer point GT) | A2I2 gives scene-level scalar density, not dense per-pixel transmittance maps; no dataset supports training/validating opacity regression against physics | Medium-high |
| 3 | B-0112 | Label-consistent convention shift: formalization, prevalence audit, label-free detector | Castro et al., Nature Comms 2020 (names annotation-policy shift) | Named in passing, never formalized, measured, or made detectable | Medium-high |
| 4 | B-0121 (P) | Counterfactual wrong-support audit of FSS (how much accuracy is support-independent foreground prior) | Learning What Not to Segment (Lang et al., CVPR 2022) | Base-class bias is known; the wrong-support counterfactual magnitude has never been published | Medium-high |
| 5 | B-0193 | Speckle-statistics-native self-supervised pretraining for ultrasound | USCL (MICCAI 2021); despeckling SSL | Prior work removes speckle as noise; nobody uses speckle statistics as the pretext signal | Medium |
| 6 | B-0212 | Blending-artifact detectability → synthetic-to-real transfer-gap law for pasted/inpainted lesions | Cut, Paste and Learn (Dwibedi et al., ICCV 2017); TumorCP (MICCAI 2021) | Blending known to matter qualitatively; the quantitative detectability→gap law and pipeline audit are missing | Medium-high |
| 7 | B-0222 | Thin-structure fidelity floor of latent diffusion + downstream segmentation penalty | MedVAE (2025); FA-VAE frequency-aware autoencoders | Compression loss is documented qualitatively; the width-vs-downsampling floor curve and causal downstream test are unmeasured | Medium-high |
| 8 | B-0230 (P) | Decompose synthetic-data advantage into label cleanliness vs image distribution (noise-injection experiment) | SENSE / What Makes Synthetic Data Effective (2026); Beyond Real Data (2025) | Adjacent works study the gap or label noise separately; the confound-breaking decomposition has never been run | Medium-high |
| 9 | B-0285 | Rare anatomical variants as a curated long-tail segmentation benchmark | MOOD challenge (medical OOD) | OOD benchmarks target pathology/corruptions; cataloged anatomical variants (in-distribution humans) are unbenchmarked | Medium |
| 10 | B-0331 | Mine report negations into spatially grounded negative supervision for segmentation | CheXpert labeler (Irvin et al., AAAI 2019) | Negation extraction exists for image-level labels only; atlas-grounded spatial negative supervision is unpublished | Medium-high |
| 11 | B-0344 | Radiotherapy dose maps as weak inverse supervision for contours | OpenKBP (Babier et al., 2021) | Forward mapping (contours→dose) is mature; nobody inverts dose→contour supervision | Medium |
| 12 | B-0350 | Suggestion-induced hallucination benchmark for medical segmentation ("segment the tumor" when none exists) | POPE (EMNLP 2023); CARES (NeurIPS 2024) | Hallucination/sycophancy measured at VQA level; dense/grounded medical variant plus negation-based mitigation is open | Medium-high |
| 13 | B-0353 (P) | Doppler audio as free spatial supervision for vessel segmentation | AVSBench (ECCV 2022) | Natural-scene audio-visual segmentation exists; physiologically coupled Doppler-audio supervision is untouched (high feasibility risk, high novelty) | Medium |
| 14 | B-0361 | Is ambiguity handling a transferable skill across dense domains? | Prob U-Net line (NeurIPS 2018) | Ambiguity modeled within domains; cross-domain transfer of the ambiguity machinery untested (search found no direct prior; flagged medium-low) | Medium-low |

(P) = PROTECTED in Stage 2. Protected ideas killed by direct prior-work hits: B-0007 (mutated instead), B-0017,
B-0035, B-0074, B-0107, B-0177, B-0196, B-0272.

## Portfolio notes
- Physical-measurement spine: B-0062 (smoke physics GT) and B-0193 (speckle physics pretext) share a
  "use the sensor physics, don't fight it" thesis.
- Convention axis: B-0112 (KEEP) + B-0159 (mutation) form one coherent program on annotation conventions.
- Medical-VLM safety pair: B-0331 (negative supervision) feeds the mitigation arm of B-0350 (suggestion hallucination).
- Highest-risk slot: B-0353 (Doppler audio) — kept deliberately as the portfolio's long shot.
