# Windows2 Stage 1 — Agent A: Cluster Map

352 ideas in 14 clusters. IDs are sequential within clusters. `ideas.jsonl` is the canonical machine-readable file; `ideas.md` is the rendered version (both built by `build_catalog.py` from `parts/c*.jsonl`).

## Cluster index

| Cluster | IDs | Count | Theme |
|---|---|---|---|
| C01-sam-prompt-failure | W2-A-0001..0025 | 25 | SAM image-mode failure science: prompt sensitivity as signal, ambiguity heads, tokenization aliasing, box/negative-prompt semantics, SA-1B-inherited shape/topology priors, IoU-head calibration |
| C02-sam2-video-memory | W2-A-0026..0050 | 25 | SAM2/video: masklet drift laws, memory eviction cliffs, erosion bias, distractor swaps, absorbing failure states, forward-backward asymmetry, ultrasound speckle, fixed-camera pollution |
| C03-medical-limits | W2-A-0051..0075 | 25 | Medical: multi-rater disagreement as signal, windowing/vendor/k-space shift, 2D-vs-3D crossover laws, partial-label poisoning, inter-rater ceilings, clinician click sim2real, consensus erasing minority experts |
| C04-amorphous-smoke-fire | W2-A-0076..0100 | 25 | Smoke/fire/fog/water: no-true-boundary evaluation, alpha regression vs binary, sensor-artifact reliance, flicker/flow physics cues, time-to-detect reformulation, dataset leakage and shadow mislabels |
| C05-transparent-glass-mirror | W2-A-0101..0125 | 25 | Glass/mirror: frame-vs-interior evidence decomposition, parallax and polarization physics, depth-dropout auto-labels, day-night transmission flips, human ceiling, puddles/screens as phantom sources |
| C06-camouflage-ambiguity | W2-A-0126..0150 | 25 | Camouflage/ambiguous boundaries: human-model difficulty dissociation, mechanism taxonomy, findability bias, motion/shadow camouflage breakers, undecidability annotation, scale-relative boundary GT |
| C07-boundary-small-objects | W2-A-0151..0175 | 25 | Boundary/small objects: error decomposition, upsampling sharpness floors, stride aliasing signatures, noise-floor-aware evaluation, crowding law, blob-prior transfer functions, physical (printed) ground truth |
| C08-uncertainty-longtail | W2-A-0176..0200 | 25 | Uncertainty/long-tail: object-level vs pixel uncertainty, calibration as shift canary, class-death phase transitions, conformal usability, seed-churn atlases, hallucination by context prior, tail label noise |
| C09-annotation-interactive | W2-A-0201..0225 | 25 | Annotation economics/interactive: real-click sim2real, unreachable masks, verification bias and SAM fingerprints, scribble placement policy, telemetry as ambiguity GT, quality-quantity frontiers |
| C10-domain-shift | W2-A-0226..0250 | 25 | Domain shift: gap decomposition, ISP/night attribution, TTA harm conditions, weather interaction matrix, UDA reproducibility audit, geometric (height) shifts solvable in closed form |
| C11-weak-semi-self | W2-A-0251..0275 | 25 | Weak/semi/self-supervised: CAM recoverability bounds, error inheritance, emergence causality (object-centric data), pseudo-label dynamics/collapse precursors, new supervision sources (design files, EXIF, gaze, physics) |
| C12-foundation-dense-science | W2-A-0276..0300 | 25 | Foundation dense-prediction science (not fine-tuning): property-resolved scaling laws, probing atlases, sub-patch information, attention-sink damage, in-context retrieval laws, causal object-token surgery, monoculture convergence |
| C13-benchmark-failure-audit | W2-A-0301..0325 | 25 | Dataset/benchmark failure: contamination, label-error repair, polygon ceilings, version drift, statistical power, patient leakage, ignore-region census, human baselines, aesthetics/geography bias |
| C14-assumption-tests | W2-A-0326..0352 | 27 | Counter-intuitive assumption tests: context/resolution/pretraining monotonicity, boundary-loss audit, Dice gradient pathology, TTA tax, mask-semantics leakage, 3D-easier-than-2D, segmentation-free measurement |

## Merge / mutate notes

Duplicates killed during generation (internal dedup decisions):

- A "clinician click realism" idea appeared in both C03 and C09; kept BOTH but split scope deliberately: W2-A-0065 = clinician-specific click habits on anatomy; W2-A-0201 = general crowdworker sim2real click gap. W2-A-0201 carries `mutate_from: W2-A-0065`.
- "Ignore-region abuse" was drafted independently for C08 and C13; merged into two non-overlapping deliverables: W2-A-0194 (behavioral audit of what models emit in ignore zones) and W2-A-0325 (cross-benchmark census + ranking sensitivity), linked by `mutate_from`.
- "Vocabulary size effects in open-vocabulary segmentation" split intentionally: W2-A-0197 (confidence-dilution mechanics/normalization) vs W2-A-0285 (evaluation-protocol reform, rank flips). Linked by `mutate_from`.
- "Interior-vs-frame reliance for glass" (W2-A-0101) and the stronger "interior blindness + open-frame hallucination corollary" (W2-A-0112) were kept as parent/mutation because the corollary (hallucinated glass in empty frames) is a distinct falsifiable prediction with distinct deployment consequences.
- Killed outright before writing: "polarization for camouflage" (too close to W2-A-0105 polarization-for-glass with weaker physics grounding), "gamified annotation reliability" (not falsifiable enough), "glass segmentation via sound" (out of scope for vision), a generic "smoke = fine-tune SAM on smoke dataset" (forbidden pseudo-idea), and ~10 "apply X loss / add attention" drafts that violated the hard rules.

Mutation chains (largest families):

- Ambiguity-as-signal family: W2-A-0001 → 0023, 0026, 0341; and multi-rater line 0051 → 0075, 0136, 0184, 0351.
- SA-1B data-genetics family: W2-A-0017 → 0025, 0206, 0264 (dataset inbreeding / SAM fingerprint / pseudo-label anatomy).
- Resolution/tokenization physics family: W2-A-0003 → 0154, 0165; W2-A-0011 → 0015, 0238, 0278, 0283, 0328.
- Metrology family: W2-A-0151 → 0164, 0175, 0330; churn/noise-floor audits 0198, 0313, 0322.
- Sensor-beats-model family: W2-A-0105 → 0120; 0089; 0308 (polarizer, thermal, HDR, industrial sensors).
- Self-diagnosis family: W2-A-0040 → 0047 → 0211 (cycle-consistency → drift onset → correction timing).
- Physics-as-supervisor family: 0081, 0098, 0122, 0274 (advection, Koschmieder, shadow-alpha, support relations).

Cross-cluster theme threads (useful for Stage-2 clustering):

1. "The reference is part of the system": 0051, 0071, 0118, 0143, 0150, 0151, 0163, 0164, 0200, 0302, 0319, 0323, 0330, 0351 — annotation noise, conventions, and ceilings as first-class scientific objects.
2. "Ecosystem inbreeding": 0017, 0206, 0212, 0264, 0290, 0300, 0301 — foundation-era feedback loops between models and datasets.
3. "Signed, structured bias beats scalar error": 0029, 0085, 0160, 0174, 0185 — bias decompositions that make failures correctable post hoc.
4. "Physics channels orthogonal to appearance": 0079, 0081, 0097, 0104, 0117, 0122, 0144, 0147 — cues no RGB-appearance model uses.
5. "Regime maps instead of method fights": 0062, 0067, 0158, 0220, 0225, 0282, 0327 — crossover laws that answer 'when', not 'whether'.
