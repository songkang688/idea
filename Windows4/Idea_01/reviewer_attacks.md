# SeeingInside — Reviewer Attacks & Answers

Source of record: `Windows4/selection_history/stage4_r2_setA.md` (P14 review, WEAK ACCEPT
conditional). Each attack below is quoted/condensed from that review or anticipated for the
next round. Status column: **ANSWERED-BY-DESIGN** (the redesigned protocol removes the
attack), **MEASURED** (the attack's alternative hypothesis is quantified rather than
denied), **OPEN** (residual risk we accept and disclose).

---

## A. The four attacks from the Stage-4 rejection paragraph

### A1. Off-manifold ablation fallacy
*"Zeroed/mean image embeddings and patch-shuffled interiors are inputs no natural image
produces; decoder behavior under them licenses no conclusion about natural inputs."*

**Status: ANSWERED-BY-DESIGN.** The headline interventions are now on-manifold: diffusion
inpaint-out and object-swap produce natural images; the box is unchanged; every scored
forward pass sees a plausible photograph/scan. Embedding-mean (S-014, softened from zeroing)
and patch-shuffle (S-604) survive only as *secondary convergence checks* (E2) and are never
used to state the claim. If secondary and primary disagree, primary wins and the
disagreement is reported as a finding about off-manifold probing itself.

### A2. Non-localized intervention (global ViT attention)
*"Pixel corruption inside the box changes embeddings everywhere via attention; 'image
evidence inside the box' is not a manipulable variable."*

**Status: ANSWERED-BY-DESIGN.** For natural counterfactuals this ceases to be a confound:
when the object is genuinely absent from the scene, whatever global influence propagates is
*legitimate evidence flow from a changed scene*, exactly the causal variable of interest.
We manipulate "evidence of the object" (a scene-level fact), not "pixels inside a crop box"
(an implementation detail). The sham-inpaint control (equal-area background edit outside the
box) bounds seam/global side effects numerically.

### A3. Positional-scaffold degeneracy
*"The decoder re-injects positional encodings at every layer; emitting a clean box-shaped
mask from positions alone is what the machinery should do — no discovered 'prior'."*

**Status: MEASURED.** The prompt-only null (dataset-mean image embedding, real box, real
positional scaffold) turns this from an interpretive objection into a reported number: the
Dice the scaffold alone achieves. If prompt-only SAM already reaches intact Dice in a
stratum, we report precisely that — which *is* the interpolator finding, correctly
attributed to the positional pathway (KNOWN FACT, architecture: Kirillov et al.,
arXiv:2304.02643) rather than to a mystified "prior".

### A4. Asymmetric payoff ("if Dice collapses you proved the null everyone believes")
**Status: ANSWERED-BY-DESIGN.** Medical-first framing. On natural images BREPS
(arXiv:2601.15123) has already discredited tight-box protocols, so the COCO stratum is a
*control*, not the claim. In the MedSAM-protocol regime the tight box is the deployed
standard (arXiv:2304.12306), so both branches move something real: H1 → published medical
Dice conflates protocol information with segmentation; H0 → a null-calibrated defense of the
protocol. The Stage-3 kill condition still applies (gap > 15 pts everywhere → stop), so the
downside is cheap, not reframed.

## B. Hidden assumption & confounders from the review

### B1. Task degeneracy alternative
*"Tight boxes on convex objects are near-sufficient statistics; ANY mechanism scores high."*

**Status: MEASURED.** This is not an alternative to rule out — it is the quantity NRF
estimates. The learned box→mask null (no pixels ever) is the direct estimate of "what the
label statistics + box geometry alone support." The paper's claim is worded accordingly:
not "SAM ignores images" but "X% of protocol Dice is reachable with zero image evidence,
and SAM's counterfactual sensitivity is indistinguishable from such a mechanism in
stratum S." SAM-specificity comes from the conjunction with CSG/persistence/swap-tracking.

### B2. Convexity confound
**Status: ANSWERED-BY-DESIGN.** Per-instance convexity-matched nulls (solidity-matched fill,
not global rectangle); solidity as a covariate in the pre-registered regression; stratified
reporting.

### B3. Padding sweep conflates prompt informativeness with ablated area
**Status: ANSWERED-BY-DESIGN.** Decoupled: padding varies only the prompt (ablation region
fixed to GT object); a separate arm varies ablation-region dilation at fixed padding (E4).

## C. Anticipated next-round attacks (our own red team)

### C1. "Your inpainter leaks the object" / seam artifacts
The inpainter might leave low-level traces (frequency signatures, seams) that SAM reads.
**Status: MEASURED + OPEN.** Mitigations: quality screen with reject-and-resample; 10%
human audit; sham-inpaint arm bounds the artifact effect; classical-inpaint convergence arm
(different artifact family — agreement across instruments argues against artifact-driven
conclusions). Residual risk disclosed: no screen is perfect; this is the main OPEN item on
medical modalities (CT/US inpainting realism), and the reason the swap arm — whose inserted
content is real image material — carries extra weight there.

### C2. "This is HalluSegBench for SAM" (scoop adjacency)
**Status: ANSWERED-BY-DESIGN.** Stage-6 supervisor ruling: no merge with P107v;
HalluSegBench benchmarks *hallucination in language-driven segmentation*; SeeingInside
measures *evidence reliance of a box-prompted mask decoder against no-image nulls*.
No text prompts, no VLM, no hallucination taxonomy, different readouts (NRF/CSG/persistence
vs hallucination rates). Proposal §23 states the boundary; the related-work section will
state it in the paper explicitly rather than hoping reviewers miss the adjacency.

### C3. "GT-derived boxes are oracle prompts; your audit inherits the discredited protocol"
**Status: ANSWERED-BY-DESIGN.** We audit the protocol *as deployed* (MedSAM-class
evaluation); the finding is about what its numbers mean. An oracle prompt makes our case
harder, not easier: the tighter the box, the more information the prompt carries, which is
exactly what NRF quantifies. A realistic-box arm (BREPS-style loose boxes) is a planned
sensitivity row (E4), expected to *lower* NRF — EXPECTED, monotonicity pre-registered.

### C4. "Dice on a counterfactual image against the original GT is meaningless"
Correct if used alone — after object removal there is no true object. **Status:
ANSWERED-BY-DESIGN.** Persistence P = Dice(m_out, m_intact) is the primary counterfactual
readout (mask-to-mask, GT-free); CSG vs GT is reported alongside for continuity with the
protocol being audited; swap-tracking uses the *known* inserted mask s_new as its reference.

### C5. "Multimask head selection hides the effect"
**Status: ANSWERED-BY-DESIGN.** Single-head primary; multimask+IoU-head-selection as a
sensitivity row. (Confound family documented in the Stage-4 P101 review; multimask design is
a KNOWN FACT of the SAM paper.)

### C6. "Frozen SAM only — maybe fine-tuned models differ"
**Status: MEASURED.** MedSAM checkpoint arm (E5). EXPECTED direction: fine-tuned-with-boxes
decoders show *higher* NRF (box-geometry prior evidence: arXiv:2606.04705). Either outcome
is informative; neither is assumed.

### C7. "n=1000 instances is small"
**Status: OPEN (accepted).** Power: paired per-instance design with bootstrap CIs on median
gaps; 500 per domain stratified 4×4×4 gives ~8 instances/cell at full crossing, so claims
are made at marginal-stratum level (per contrast quartile, etc.), never per cell. If CIs on
the primary endpoint straddle τ thresholds, we scale the medical cohort before publishing —
compute cost is forward-passes only.

---

## Standing discipline

- No verdict is stated from a single metric; the four-way conjunction (proposal §15) is the
  only licensed "interpolator" statement.
- Any experiment that dies takes its branch of the decision tree with it (roadmap.md);
  there is no post-hoc threshold motion — τ1–τ3 are frozen in `configs/default.yaml`.
- All numbers in the eventual paper carry EXPECTED/ACTUAL provenance tags in the repo.
