# Provisional 200 — Full A ∪ B ∪ C Portfolio (Agent I)

Agent I (merger + novelty assassin for batch A; **not PI, no final-3**). Date: 2026-08-28.
Built by folding batch A (F's 76 keeps + 28 tier-2 rescue candidates) into G's 121-slot B∪C portfolio, after the prior-work verdicts in `a_prior_work.md` and the collision resolutions in `collisions_AFG.md`. G files untouched; this file supersedes `stage2_agent_G/provisional_200_partial.md` as the working 200.
**Mid-merge reconciliation:** F's `prior_work_attack.md` and Stage-4 Agent J's `verdicts.jsonl` landed while this fold was in flight; both are incorporated (see `a_prior_work.md` Part 5). Net effect: 3 of my literature kills restored as mutations (0331, 0352, 0107), 2 LOCKs demoted to FLEX (0334, 0349).

## Headline accounting

| Category | A | B | C | Total |
|---|---|---|---|---|
| **LOCK** | 6 | 18 | 31 | **55** |
| **FLEX** | 79 | 45 | 21 | **145** |
| **Portfolio slots** | **85** | **63** | **52** | **200** ✓ |

Movement from G's baseline (B 64 / C 57 / A-reserve 79):
- 4 G FLEX absorbed as arms of A hosts (C-0208→A-0237, C-0345→A-0301, C-0078→A-0337, C-0333→A-0334).
- 1 G LOCK merged within G to enforce the contamination cap (C-0298→C-0122).
- 1 G FLEX folded per G's own conditional (B-0293→B-0286, no compute partner).
- A takes 85 slots (79 reserved + 3 freed by absorbing G content into A hosts + 3 slack under the 210 ceiling for F/J-mandated mutation restorations).
- 12 A ideas merged into G hosts and 5 A-internal merges (arms, no slots); 2 A ideas killed by literature.

Tags: (L)=LOCK, (F)=FLEX; [mut]=claim demoted/refocused per `a_prior_work.md`; hosts show ←parasites; (¢)=cheap, ($)=heavy, (⏰)=urgency.

---

## BATCH A — 85 slots

### A LOCK (6)

| ID | Claim | Notes |
|---|---|---|
| A-0121 | Puddle mirrors cause phantom-object segmentation; road-plane mirror-symmetry verification | J-gate: pilot phantom-rate floor first (LiDAR-side phenomenon now published, VehicleSec 2026); camera-side audit unclaimed |
| A-0150 | Boundary GT is scale-relative: correct boundaries drift with viewing resolution | J-gate: signed shift is the claim; interface/resampling controls mandatory |
| A-0163 | Stuff-stuff boundaries are bands, not curves; band-aware GT + scoring | (¢) J-gate: per-pair-d Boundary IoU baseline mandatory |
| A-0175 | Printed calibration shapes → camera-true sub-pixel boundary GT, zero annotation | metrology flagship; feeds A-0276; J-gate: GT error budget (optics/edge-convention) as Table 1 |
| A-0205 | Verification bias: accepted machine-mask errors are correlated with model style and inherited | inbreeding core; dense correlated-contamination legs carry novelty (NLP acceptance bias published) |
| A-0206 ←A-0264 | SAM-fingerprint detection in assisted datasets + pseudo-label error-anatomy arm | data-genetics flagship; cap slot 1/5; J-gate: controlled-provenance dialect control vs A-0312 |

### A FLEX — from F Tier A (9)

| ID | Claim | Notes |
|---|---|---|
| A-0074 [mut] | Coverage audit of segmentation-volume uncertainty pipelines under boundary-correlated errors | J adds mandatory deployed-pipeline survey; COMPASS/CONSIGN/CONSeg as reference bounds |
| A-0148 [mut] | Miscalibrated uncertainty overlays net-hurt human-AI camouflage search; calibration as manipulated moderator | soft-vs-hard highlighting known (F); COD + calibration moderator is the paper; links A-0188 |
| A-0199 [mut] | Rare-context hallucination dose-response on classical segmenters with known training data | J freshness hit: HalluSegBench/HII-DPO own the VLM framing; dense/classical complement survives |
| A-0237 ←A-0249, C-0208(←0014/0134) | Three-way gap decomposition: convention vs quality vs appearance; UDA-credit smoking gun | J: merge mandatory (0249 unidentifiable standalone); NLP re-annotation template cited |
| A-0326 [mut] | Signed, property-resolved context-value crossover law + locality-architecture natural experiments | J: drop the monotonicity-dogma framing |
| A-0331 [mut] | Per-instance gradient-share instrumentation of Dice starvation; data-side vs loss-side remedies | restored per F+J (blob loss owns phenomenon, instrumentation unclaimed); **freshness-fragile — execute first if executed** |
| A-0334 [mut] ←C-0333 | Privacy attack on documented mask-only release practices; silhouette-sufficiency arm | demoted from LOCK: BareBones (arXiv:2604.10528) scooped the mask-only recognition instrument; documented-practice audit survives |
| A-0349 [mut] | Convention-learnability: signed model-vs-own-training-label offsets per junction type | demoted from LOCK per J (training-labels objection); curvature/function dissociation control mandatory |
| A-0352 [mut] | Segmentation-free scalar measurement with physical-GT anchoring (phantoms/harvest/cytometry) | restored per F+J; counting excluded (answered); rides A-0175's physical-GT infrastructure |

### A FLEX — from F Tier B (24)

| ID | Claim |
|---|---|
| A-0058 | Tumor boundary uncertainty is directionally structured (infiltration axes); HRHR |
| A-0061 | Dice-topology Pareto: topology is lost at checkpoint-selection time (¢) |
| A-0071 [mut] | Consensus-referenced ceiling audit: locate SOTA vs rater-vs-consensus ceiling, style-vs-anatomy residuals (J fixed the formalism: pairwise inter-rater Dice is not an upper bound) |
| A-0075 | STAPLE-style consensus erases correct minority experts; outcome-anchored; HRHR; J-gate: LIDC pilot + modern-fusion (RaLMPH/CASC-AI) strawman check |
| A-0076 ←A-0091, A-0082 | Smoke metrology: binary-mask rankings flip under density labels; hosts human-judgment-vs-IoU + alpha-threshold arms; SFMatting-800 as density reference (F) |
| A-0145 [mut] | Findability bias bound via temporal-adjacency verification in camera-trap bursts (J removed the ecology-collaboration wall; claim a bound, not a benchmark correction) |
| A-0151 | Three-way boundary error decomposition (model / annotation / metric); cross-ref C-0311 |
| A-0152 | Size-stratified reporting flips leaderboards; progress never reached the smallest decile (¢) |
| A-0183 | Anomaly-segmentation benchmarks are boundary detectors in disguise (¢) |
| A-0188 | Uncertainty overlays can net-increase clinician misses; human study |
| A-0195 | Sub-10-example classes are retrieval, not generalization (¢) |
| A-0215 [mut] | Protocol-vs-architecture effect size via existing COCO/Sama-COCO dual labels (J: commissioned corpus dead on cost-benefit; zero-annotation-budget version, GPU-week) |
| A-0268 | Does semi-supervised segmentation survive DINOv2-grade features? pre-registered re-baselining |
| A-0276 | Dense scaling laws: boundary quality scales with smaller exponent than region accuracy; pairs with A-0175 |
| A-0278 | Sub-patch detail hides in neighboring tokens; recoverable-sharpness probe; cross-ref B-0013/B-0018 |
| A-0290 ←A-0300 | Shared blind spots across the model zoo = data-ecosystem holes; hosts ensemble-gain-collapse trend arm |
| A-0297 | Causal feature surgery: where promptable models represent each object; HRHR |
| A-0301 [mut] ←C-0345 | SA-1B/dense contamination audit with mask-quality-on-duplicates readout + exposure-tracking arm (⏰); cap slot 3/5; F: Ramos ICCVW 2025 owns the classification-side genre — mask-level memorization is the surviving leg |
| A-0321 | LVIS rare-class claims need CIs; bootstrap fragility audit (¢) |
| A-0329 | Strong frame-independent baseline for VOS; what is temporal machinery for? |
| A-0330 | Do boundary losses improve boundaries? noise-floor-aware reruns |
| A-0339 | 3D's difficulty reputation is a supervision-bit accounting artifact; HRHR |
| A-0341 | Prompt sensitivity increases with scale on ambiguous objects (visual prompts); modality-split vs B-0182 |
| A-0351 | Two-annotator myth: disagreement is multi-modal; dense rater panels; HRHR |

### A FLEX — from F Tier C (15)

| ID | Claim |
|---|---|
| A-0022 | Jacobian of SAM's mask w.r.t. prompt is a label-free structure detector; HRHR |
| A-0042 | Micro-motion segmentation: objects invisible in any single frame; new task |
| A-0097 | Heat-shimmer segmentation as a pre-smoke fire channel; HRHR physics |
| A-0107 [mut] | Supervision purity of LiDAR/ToF invalid-return glass masks + pseudo-label scaling law; restored per F (cue published — GRAR/TOPGN/SILICA — purity taxonomy and scaling unclaimed) |
| A-0110 | Day-night transmission/reflection flip inside fixed scenes; annotate-once |
| A-0136 | Disagreement maps transfer across datasets better than masks |
| A-0143 | Part-level undecidability in camouflage; decision-theoretic annotation |
| A-0173 | Instance merging obeys a crowding law (machine Bouma law) |
| A-0181 [mut] | Abstention cliff as the empirical test of minority-collapse theory in dense prediction (per F) |
| A-0225 | 100-labeled-pixels challenge: extreme-budget phase map of supervision paradigms |
| A-0254 | Does object-centric data cause SSL segmentation emergence? causal de-object-centrification |
| A-0292 | Zero-real-image segmentation foundation: procedural pretraining limit; HRHR |
| A-0312 | Masks reveal their dataset: annotation-dialect classification; outside contamination cap, cross-cite A-0206 |
| A-0337 ←C-0078 | Mask metrics vs task success with instrumented consumers; hosts detection-AP arm |
| A-0345 | Segmentation models are secret amodal completers |

### A FLEX — F Protected exceptions (6)

| ID | Claim |
|---|---|
| A-0026 [mut] ←C-0082-mut | Causal map of VOS failure: variance decomposition (smooth drift vs discrete events) regressed on frame-0 ambiguity, on vanilla + memory-fixed SAM2; hosts failure-scaling-law arm (collision #6 re-entry); J reframed from pure prediction |
| A-0028 | Teleport experiments: does SAM2 track appearance or location? (¢) |
| A-0063 | Annotation fatigue leaves order signatures in public medical datasets |
| A-0085 | Smoke shadows mislabeled as smoke; sun-geometry forensics |
| A-0117 | Caustics as transparent-object shadows; HRHR physics |
| A-0139 | COD models lack inhibition-of-return; multi-instance recall collapse |

### A FLEX — Tier-2 rescues (25)

| ID | Claim |
|---|---|
| A-0010 | Instance Nyquist limit: periodic textures merge below token resolution; cross-ref B-0018 |
| A-0020 | Everything-mode recall geometry vs prompt-grid density |
| A-0025 | Topology bias: holes filled at rates predictable from training statistics; fine-tune causal leg |
| A-0034 | VOS metrics reward temporal smoothness: oracle-smoother audit (¢) |
| A-0046 | Ultrasound speckle decorrelation breaks SAM2 memory; matched-cost duel; medical |
| A-0062 | Through-plane spacing threshold where 3D stops beating 2D; crossover law; medical |
| A-0065 | Clinician-click sim2real prompting gap; RClicks ported to medical |
| A-0068 | Extreme-imbalance phase transition: recall decouples from Dice; medical |
| A-0099 | Auto-exposure dynamics leak global fire evidence; shortcut audit (¢) |
| A-0101 | Glass models are frame detectors in disguise; frameless collapse probe (¢) |
| A-0160 | Per-class signed boundary bias removable by morphological recalibration (¢) |
| A-0170 | Upstream JPEG bounds small-object recall independent of model |
| A-0178 | Instance count vs pixel count as separate supervision currencies |
| A-0200 | Tail errors are label errors: frequency-resolved correction; cite Northcutt line |
| A-0203 | Unpromptable objects: the reachable mask space of frozen interactive models (N5) |
| A-0209 | Shape entropy predicts point-supervision viability; pre-commitment law |
| A-0233 | Weather shifts compose super-additively; interaction matrix |
| A-0239 | Compression asymmetry: models overfit benchmark compression, deployment is rawer (N5, ¢) |
| A-0255 | Unsupervised-seg evaluation is circular: Hungarian-matching granularity luck |
| A-0283 | Resolution-extrapolation failure is radially structured (positional encoding) (¢) |
| A-0286 | How small can a decoder be? capacity localization over frozen foundations; cross-ref B-0213 |
| A-0309 | PQ's 0.5-IoU matching cliff manufactures significance (¢) |
| A-0315 | Patient-level leakage in medical benchmarks via anatomical fingerprinting; cross-cite C-0122 |
| A-0343 | Relational grounding gap in referring segmentation; ARO-style controls |
| A-0348 | Inference-time search vs training-time scale: the compute exchange rate |

---

## BATCH B — 63 slots (G's portfolio, 2 deltas)

### B LOCK (18)

B-0114 (L) VPT tokens as trainable registers · B-0001 (L) register-norm maps as free uncertainty · B-0304 (L) language quantizes shape space · B-0074 (L) modality-gap collapse dynamics · B-0323 (L) mention-bias imprint · B-0104 (L) PEFT invariance-inheritance ceiling · B-0307 (L)($) language-alignment cost to 3D · B-0332 (L)(⏰) visual-CoT faithfulness artifact-swap · **B-0268 (L)(⏰) generated-image contamination — cap slot 4/5** · B-0213←0200 (L) resolution×probe-capacity confound · B-0226 (L) shift-budget curves (untouched by A-0245 merge, see collisions §4) · B-0101 (L) required-rank law · B-0194 (L)(¢) segmentation sycophancy · B-0169 (L)(¢) negative-click dose-response · B-0164 (L)(¢) savings/relearning forgetting · B-0227 (L)(¢) cleaner labels transfer worse · B-0263 (L)(¢) procedural corruptions beat realistic · **B-0286 ←B-0293 (L) site-of-origin decodability, now hosting the medical-pretraining-attribution residual (G's conditional exercised)**.

### B FLEX (45)

vfm_failure (5): B-0013 sub-patch inverse scaling · **B-0018 ←A-0003** thin-structure Nyquist law + patch-grid-aliasing phase-sweep arm · B-0023 LVLM acuity battery · B-0025 attention maps epiphenomenal? · B-0026 nameability predicts dense errors.
vlm_dense_failure (5): B-0036 relation flip-consistency (cross-cite A-0343) · B-0054 multi-hop error law · B-0062 size adjectives read as pixels · B-0064 part-whole containment · B-0068 shadows/holes/reflections grounding.
finetune_instability (3): B-0077 inverted layer-wise LR decay · B-0092 inverse stability scaling · B-0098←0095 LoRA≈rescaled-LR boundary.
peft_limits (3): B-0108 calibration sign flip · B-0118 PEFT hides subgroup gaps · B-0133 LoRA memorizes more per-parameter.
catastrophic_forgetting (4): B-0137 beneficial forgetting · B-0154 head-capacity curve · B-0157 template staleness · B-0163 forgetting-audit bias.
prompt_sensitivity (2): B-0168 template gains are calibration · B-0182 scale increases text-prompt sensitivity on rare classes (modality-split vs A-0341).
representation_mismatch (5): B-0196 equivariance-deficit predictor · **B-0203 ←A-0153** post-upsampler residual decomposition + analytic bilinear-floor arm · B-0208 occupancy-threshold recall law · B-0215 text-aligned subspace · B-0222 video pretraining repairs equivariance.
crossdomain_frozen_vs_tuned (4): B-0234←0112 frozen-vs-tuned phase boundary · B-0241 style-vs-content dissociation · B-0243 nameability boundary · B-0252 interpolation-frontier kinks.
synthetic_adaptation (4): B-0254 generated-data calibration tax · B-0264 synthetic medical privacy laundering · B-0275 boundary-F1 collapse canary · B-0278 spectral-coverage criterion.
medical_vfm_science (3): B-0282 orientation invariance destroys laterality · B-0284 lesion-size/stride law · B-0303 fine-tuning degrades ROC tails. *(B-0293 folded into B-0286.)*
language_geometry (4): B-0305 Whorfian spatial imprint · B-0317 MIL identifiability · B-0325 text-only counterfactual decomposition · B-0326 basic-level naming sets granularity.
agentic (3): B-0329 agent confidence vs tool quality · B-0338 web-agent contamination · B-0342 question-substitution drift.

---

## BATCH C — 52 slots (G's portfolio, 6 deltas)

### C LOCK (31)

C-0302 ←0070,0065,0284, **A-0313** rigor flagship + segmentation power-audit arm · C-0309 ←0328 IRT for benchmarks · C-0136 ←B-0033 seed variance census · C-0311 ←0064,0042,0282, **A-0198** metrology uncertainty budget + seed-churn variance arm · C-0344 instruction-A/B protocol experiment · C-0338 ←0071, **A-0323** human ceiling + general-classes human-mIoU arm · C-0260 monoculture cross-dataset ranks · C-0276 ←0255 tail-progress illusion · C-0256 ←0261 size-frequency confound · C-0306 (⏰) conformal coverage vs NMS · C-0057 missing-annotation tax · C-0011 ←B-0042 (⏰) vocabulary noise vs margins · C-0326 ←**A-0305** residual-error adjudication + multi-benchmark headroom arm · C-0327 2015 architecture + 2026 recipe · C-0283 stale-baselines decay · C-0285 shadow tuning · C-0226 ←0248,0231 SR truthfulness · C-0150 ←0221, **A-0245** UDA reckoning + cross-pair rank-stability arm · C-0287 ablation sign-flip rates · C-0259 label-everything re-annotation · C-0046 ←0080 annotation-noise band CIs · C-0007 ←**A-0164** tiny-object noise floor + jitter-propagation method arm · C-0279 ←0001,0020 exposure-vs-rarity · C-0159 detection AL replication · **C-0122 ←0264, A-0100, C-0298** duplication census + smoke/fire-provenance arm + hash-audit arm — cap slot 5/5 · C-0158 NMS calibration destroyer · C-0308 machine psychophysics staircases · C-0135 co-occurrence overrides appearance · C-0341 batch cross-talk exploit · C-0055 fresh i.i.d. COCO test set · C-0043 size-stratified Dice reliability. *(C-0298 merged into C-0122.)*

### C FLEX (21)

Tier-A survivors (14): C-0193 threshold drift · **C-0115 ←A-0220** quality-vs-quantity exchange + mask-precision-threshold arm · C-0119 transform rank-stability · C-0145 vocabulary interference · C-0178 synthetic vs real corruption · C-0190 flicker as free uncertainty · **C-0212 ←A-0228** night-is-ISP + RAW-evaluation execution arm · C-0258 fairness benchmark · C-0269 CLIP curation bias · C-0277 end-to-end bias tracing · **C-0300 ←0304-C, A-0322** reproduction-gap meta-analysis + literature-mined noise-floor arm · C-0303 tuning tax · C-0319 weak-to-strong dense · C-0321 behavioral contracts. *(C-0078→A-0337 · C-0208→A-0237 · C-0345→A-0301.)*
Tier-B survivors (7): C-0013 small objects from context · C-0116 ghost-rate benchmark · C-0125 stride-grid box snapping · C-0290 ←0288/0289/0296 determinism audit · C-0329 vestigial RPN · C-0332 cropping test · C-0340 resolution is pixel count. *(C-0333→A-0334.)*

---

## MERGED — arms created in this fold (no slots; reversible)

**A→A (5):** 0249→0237 · 0264→0206 · 0300→0290 · 0091→0076 · 0082→0076.
**A→G hosts (12):** 0245→C-0150 · 0164→C-0007 · 0313→C-0302 · 0322→C-0300 · 0228→C-0212 · 0305→C-0326 · 0100→C-0122 · 0323→C-0338 · 0198→C-0311 · 0003→B-0018 · 0153→B-0203 · 0220→C-0115.
**G→A hosts (4):** C-0208(+0014/0134)→A-0237 · C-0345→A-0301 · C-0078→A-0337 · C-0333→A-0334.
**G→G (2):** C-0298→C-0122 · B-0293→B-0286.
**Re-entry (1):** C-0082-mut→A-0026.
(G's pre-existing 23 parasites unchanged; see G's file.)

## LEFTOVER CUTS (batch A)

**Killed by literature (2):** A-0272 (CreativePSD/LICA/OmniPSD own design-layer corpora) · A-0017 (WACV 2026 owns wiry-failure + evidences architectural cause; F concurs — expressivity sliver lives in the rescued A-0203).
**Initially killed, restored as mutations after F/J reconciliation (3):** A-0331, A-0352, A-0107 (see F Tier A / Tier C tables above).
**Tier-2 not rescued (25, slot pressure):** A-0007, 0008, 0015, 0016, 0018, 0021, 0029*, 0036, 0043*, 0045, 0081, 0088, 0090, 0106, 0111, 0118, 0126, 0135, 0155, 0189, 0226, 0252, 0259, 0266, 0310. (*flagged as optional arms of the A-0026 unit.)
F's 51 kills and 172 remaining borderlines stand as F recorded them; G's 40 drops stand as G recorded them. All cuts reversible.

## Cluster-cap compliance

- **Contamination/inbreeding cap (≤5):** A-0206, A-0205, A-0301, B-0268, C-0122 = 5 ✓.
- **C eval-audit cap:** C lost 3 eval-audit FLEX (0078, 0345, 0333-adjacent) and 1 eval-audit LOCK slot (0298 merged) vs 1 mechanism FLEX (0333); C's eval-audit share stays ≤60% of C's 52 slots.
- **Medical rebalance:** 12 A medical slots (incl. restored 0331) + 5 B/C medical slots ≈ 8.5% of portfolio (was ~5% in G's partial), per G's under-coverage note.
