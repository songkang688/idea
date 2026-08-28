# Stage 3 — Cluster A Keep List (17 survivors)

**Sub-Agent G (Prior-Work Hunter) → Supervisor Windows7.**
84 Cluster A survivors → **17 kept** (12 KEEP + 5 MUTATE), 67 killed. Full adversarial analysis in `stage3_cluster_A_priorwork.md`; mutations detailed in `stage3_cluster_A_mutations.md`.

Each entry: one-liner, closest prior work found by real search, and the precise novelty remainder that experiments can isolate.

---

## KEEP (12)

### 1. A-0002 — Positional-encoding aliasing causes point-prompt instability
- **One-liner:** Test whether SAM's sub-pixel click-flip instability is spatially periodic at the prompt encoder's positional-embedding frequency grid, and whether anti-aliased re-encoding removes it.
- **Closest prior:** Stable Segment Anything Model (Fan et al., 2023, arXiv:2311.15776) — attributes instability to decoder attention drift, never tests the encoder-side aliasing mechanism.
- **Remainder:** Fourier analysis of flip maps vs. PE grid period + causal low-pass PE intervention. Confidence: medium.

### 2. A-0003 — Prompt-order sensitivity of multi-click prompting
- **One-liner:** Fixed click *sets*, permuted click *orders*: measure IoU spread and test mediation by the inter-step low-res mask prior.
- **Closest prior:** TETRIS (Moskalenko et al., 2024, arXiv:2402.06132) — perturbs click positions, never order. SEARCH NOTE: no order-invariance study found.
- **Remainder:** Order-invariance as a measurable property + benchmark-validity implication. Confidence: medium.

### 3. A-0016 — Forgetting curve of SAM2's memory bank
- **One-liner:** Parametric occlusion-length sweeps to identify the functional form of re-ID decay (exponential interference vs. slot-eviction steps), aligned with logged memory contents.
- **Closest prior:** SAM2Long (Ding et al., 2024, arXiv:2410.16268) — fixes memory error accumulation without characterizing the decay law.
- **Remainder:** Mechanism decomposition in a method-dominated literature. Confidence: medium-high.

### 4. A-0032 — Exhaustivity misses concentrate far from the concept prototype
- **One-liner:** Analyze the *structure* (not rate) of instance misses under concept prompts: distance-from-prototype in the model's own embedding space, controlling size/occlusion.
- **Closest prior:** SAM 3 / SA-Co (Meta AI, 2025) — measures how much is missed, never where misses live in embedding space.
- **Remainder:** A priori predictability of misses → targeted verification and honest recall bounds. Confidence: medium.

### 5. A-0061 — Boundary Nyquist limit set by decoder resolution
- **One-liner:** Measure where in contour-frequency space segmentation error concentrates and whether the cutoff is predictable from decoder feature-map resolution across models.
- **Closest prior:** FourierLoss (2023, arXiv:2309.12106) — same math as a loss function, not as a measurement of an architectural constant.
- **Remainder:** A design-guiding "boundary Nyquist constant". SEARCH NOTE: no direct hit. Confidence: medium-high.

### 6. A-0062 — HQ-boundary gains vs. soft multi-annotator ground truth
- **One-liner:** Re-score SAM vs. HQ-SAM and successors against 5-annotator soft boundaries; quantify how much "high-quality boundary" progress is hard-label metric gaming.
- **Closest prior:** Metrics Reloaded (Maier-Hein et al., Nature Methods 2024) — recommends tolerance metrics but never re-evaluates the HQ line against multi-annotator references.
- **Remainder:** Validity audit of a celebrated improvement line. Confidence: medium.

### 7. A-0078 — Do distilled students inherit teacher click-fragility maps?
- **One-liner:** Correlate spatial fragility maps across SAM / MobileSAM / EfficientSAM vs. independently trained controls, controlling shared-data confounds.
- **Closest prior:** Born-Again Networks (Furlanello et al., ICML 2018, arXiv:1805.04770) — student-teacher effects for classification accuracy, not failure-mode inheritance. SEARCH NOTE: no inheritance study found for segmentation.
- **Remainder:** Pathology inheritance as a property of the distillation signal. Confidence: medium-high.

### 8. A-0107 — PEFT forgetting is a readout phenomenon, recoverable by decoder reset
- **One-liner:** Four-way {original, tuned} × {encoder-adapters, decoder} swap matrix after domain PEFT on 5 domains; measure the decoder-reset-recoverable fraction of zero-shot loss.
- **Closest prior:** Kumar et al. (ICLR 2022, arXiv:2202.10054) — feature-distortion vs. head account for classification; CA-SAM (CVPR 2026) prevents SAM forgetting without locating it.
- **Remainder:** Component-resolved forgetting for promptable models + the dual-decoder deployment implication. Confidence: medium.

### 9. A-0136 — Token-occupancy law for small-object failure
- **One-liner:** Vary input resolution to decouple token occupancy from pixel area; test whether quality collapse pins to the <1-token threshold.
- **Closest prior:** SOHES ablations (ICLR 2024, arXiv:2404.12386) — patch size correlates with mask quality, aggregate only, never object-aligned or occupancy-decoupled.
- **Remainder:** Tokens (not pixels) as the mechanistic unit of small-object failure. Confidence: medium.

### 10. A-0178 — Artifact tokens cause prompt-localized segmentation failures
- **One-liner:** Compare click-prompt failure rates on vs. off high-norm artifact patches (location-matched), then show register retrofitting removes the excess.
- **Closest prior:** Vision Transformers Need Registers (Darcet et al., ICLR 2024, arXiv:2309.16588) — representation-level anomaly + aggregate dense gains, no prompt-conditioned causal tracing.
- **Remainder:** Causal chain from a known representation anomaly to user-visible promptable failure. Confidence: medium-high.

### 11. A-0227 — Is SAM's multimask diversity calibrated to ambiguity, or a template?
- **One-liner:** Correlate inter-hypothesis spread with human-interpretation entropy; test cross-image template similarity of the 3-mask structure.
- **Closest prior:** A-SAM (NeurIPS 2024) — replaces SAM's ambiguity handling with a CVAE, never audits the deployed model's diversity calibration.
- **Remainder:** Validity of using multimask spread as uncertainty in downstream pipelines. Confidence: medium.

### 12. A-0271 — SA-1B pipeline fingerprints and their inheritance
- **One-liner:** Define generator-signature statistics (curvature spectra, complexity ceilings) distinguishing SA-1B from human datasets; train matched models on each; test signature reproduction on new images.
- **Closest prior:** Segment Anything (Kirillov et al., 2023, arXiv:2304.02643) — documents the filter stack (IoU≥0.88, stability, NMS) but never analyzes its distributional imprint or inheritance. SEARCH NOTE: no fingerprint-inheritance analysis found.
- **Remainder:** First quantitative inheritance measurement for the auto-labeling era's flagship dataset. Confidence: medium-high.

---

## MUTATE (5) — see `stage3_cluster_A_mutations.md` for full mutations

### 13. A-0017 → Causal memory surgery for SAM2
- **Mutated one-liner:** Measure how much organic SAM2 tracking failure is reversible by targeted deletion of post-error memory entries — an upper-bound diagnostic that prevention methods (SAMURAI, DAM4SAM) can be scored against.
- **Closest prior:** SAMURAI (2024, arXiv:2411.11922) — prevents distractor lock-in; never quantifies the reversible share post hoc.

### 14. A-0068 → Training-free audit of latent alpha-matte information in binary-trained logits
- **Mutated one-liner:** Rank-correlate raw SAM logits with ground-truth alpha in translucent regions (distance-to-boundary partialled out) + boundary-placement variance on translucency.
- **Closest prior:** Matting Anything (2023, arXiv:2306.05399) — proves matting works *after training a head*; never measures the free signal in the logits.

### 15. A-0128 → Trajectory calibration of interactive confidence
- **Mutated one-liner:** Does self-reported confidence inflate with click count independent of accuracy, and is the inflation a correctable model constant that repairs stopping rules?
- **Closest prior:** On Calibrating Semantic Segmentation Models (NeurIPS 2023, arXiv:2212.12053) — static calibration only; no interaction-indexed analysis exists.

### 16. A-0134 → The absence option: emptiness calibration for geometric prompts (absorbs A-0047)
- **Mutated one-liner:** Benchmark null-detection AUROC of existing SAM signals across empty-prompt families (background clicks, texture boxes, wrong boxes) and fix with a trained null token — scoped to point/box prompting, which SAM3's concept-level presence head does not cover.
- **Closest prior:** SAM 3 presence head (2025) — concept prompts only; Huang et al. (Medical Image Analysis 2024, arXiv:2304.14660) — documents confident wrong-box masks without a rejection benchmark.

### 17. A-0314 → Linear property axes in mask decoders (activation steering as measurement)
- **Mutated one-liner:** Extract steering directions for interpretable mask properties from contrastive activation pairs; evaluate cross-image generalization, dose-response linearity, and compositionality — a mechanistic map of the decoder's property geometry.
- **Closest prior:** Inference-Time Intervention (NeurIPS 2023, arXiv:2306.03341) / Activation Steering Decoding (ACL 2025) — token-generation steering; SEARCH NOTE: no steering of dense mask outputs found.

---

## Coverage
Survivor spread: prompt-sensitivity 2, SAM2-memory 2, SAM3-concepts 1, boundary 3, distillation 1, PEFT-forgetting 1, calibration/uncertainty 2, small-objects 1, evaluation 1, representation-internals 2, ambiguity 1, data-centric 1.
