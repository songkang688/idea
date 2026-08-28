# Stage 4 — Cluster A Keep List (7 survivors)

**Reviewer #2 (Cloud Sub-Agent J) → Supervisor Windows7.**
17 Stage-3 keeps attacked as submitted papers → **7 survive**, 10 killed. Full attack+defense in `stage4_cluster_A_attacks.md`. Survival rule: an idea lives only if a concrete, realistic experiment refutes its strongest attack.

Each entry: one-liner, the strongest reviewer attack, and the experiment that shuts the reviewer up.

---

## 1. A-0002 — Positional-encoding aliasing causes point-prompt instability
- **One-liner:** Test whether SAM's sub-pixel click-flip instability is spectrally attributable to the prompt encoder's positional Fourier features, via white-box inference-time spectral surgery.
- **Strongest attack:** Attribution ambiguity — SAM's prompt encoder uses continuous random Fourier features, not a grid; any flip-map periodicity is equally consistent with the 16-px patch grid or the 64×64 dense PE, so the headline mechanism can't be isolated as proposed. Secondary: sub-8-px flips are below real click noise, so who cares.
- **Shutting-up experiment:** Path-specific, training-free spectral surgery — bandlimit only the point-path RFF matrix at inference (equal-energy random-row control), compare measured flip-map spectra against the *exactly known* RFF spectrum vs the 16-px grid prediction; then show AMG's 32×32 prompt grid changes recall under half-period phase shifts (machine prompting cares even if humans don't).

## 2. A-0017 — Causal memory surgery for SAM2 (upper-bound diagnostic)
- **One-liner:** Measure how much organic SAM2 tracking failure is reversible by targeted deletion of post-error memory entries — a validated upper bound that prevention methods can be scored against. (Absorbs A-0016's memory-attention analysis as a secondary arm.)
- **Strongest attack:** Trivial alternative — "memory surgery" is operationally a tracker reset, a decades-old heuristic; SAMURAI/DAM4SAM gains already bound the memory-borne share.
- **Shutting-up experiment:** Three-arm comparison on ≥200 protocol-harvested organic failures: targeted deletion vs full reset-to-conditioning-frame vs no-op; then the preregistered kill-shot — per-sequence reversible fraction must predict per-sequence SAMURAI and DAM4SAM gains (r>0.6), proving the surgery is a decomposition instrument, not a repair heuristic. If it doesn't predict, the paper reports the diagnostic dead.

## 3. A-0061 — Boundary Nyquist limit set by decoder resolution
- **One-liner:** Measure where in contour-frequency space segmentation error concentrates and whether the empirical cutoff sits at, or well below, the decoder's theoretical sampling limit.
- **Strongest attack:** Triviality — Nyquist is a theorem; a band-limited decoder is band-limited, no experiment needed. Secondary: polygonal GT contours make high-frequency "error" an annotation artifact.
- **Shutting-up experiment:** Synthetic parametric contour suite (controlled curvature spectra, exact GT) + DIS-5K fine masks, across decoders at ≥3 output resolutions (SAM, HQ-SAM path, SAM2, Mask2Former): locate the empirical cutoff vs the theoretical limit. Cutoff at the limit = sampling-limited (raise resolution, gain); cutoff far below = training-limited (resolution increases wasted — falsifies the field's default fix). The theorem fixes the bound, not the operating point; either outcome changes decoder-design decisions.

## 4. A-0062 — HQ-boundary gains vs. soft multi-annotator ground truth
- **One-liner:** Re-score SAM vs HQ-SAM and successors against 5-annotator soft boundaries; determine whether HQ gains live below the human boundary-resolution floor.
- **Strongest attack:** Statistical artifact — soft references add reference noise, which attenuates every method's measured gain; observed "shrinkage" would be lost metric power, not detected metric gaming.
- **Shutting-up experiment:** Sigma-stratified decomposition — partition boundary arcs by local inter-annotator sigma and compare SAM-vs-HQ gains *within* strata (conditioning on reference precision equalizes attenuation): gains concentrated in high-sigma arcs = unverifiable-in-principle (gaming shown); gains persisting in annotator-consensus arcs = real (audit validates HQ). Plus injected-known-improvement control calibrating the pipeline's detection power, and an NSD-tolerance comparison arm.

## 5. A-0107 — PEFT forgetting is a readout phenomenon, recoverable by decoder reset
- **One-liner:** Four-way {original, tuned} × {encoder-adapters, decoder} swap matrix after domain PEFT on 5 domains; measure the decoder-reset-recoverable fraction of zero-shot loss and the dual-decoder serving win.
- **Strongest attack:** Pseudo-problem + instantiation — LoRA adapters toggle off, so the base model is preserved by construction; and LP-FT (Kumar et al.) already gave the feature-vs-head account.
- **Shutting-up experiment:** The swap matrix with serving-cost teeth: SAM's encoder is >95% of inference FLOPs, so adapter-toggling serves the two capabilities alternately at 2× encoder cost — the matrix tests whether ONE adapted encoder pass feeds TWO 4M-param decoders (tuned = domain, original = zero-shot) simultaneously at ~1× cost. Positive = deployment result "keep both models" doesn't give; negative (swap incoherence) = falsifies the LP-FT account for prompt-conditioned decoders. Content either way.

## 6. A-0178 — Artifact tokens cause prompt-localized segmentation failures
- **One-liner:** Compare click-prompt failure rates on vs. off high-norm artifact patches, with causality from a test-time register-retrofit toggle rather than location matching.
- **Strongest attack:** Unverified premise — MAE-lineage encoders (SAM's ancestry) may lack artifact tokens entirely, voiding the study; and artifact locations confound with boring-background regions where clicks fail anyway.
- **Shutting-up experiment:** (1) Preregistered day-1 norm audit across the deployed promptable fleet (SAM B/L/H, SAM2 Hiera, EfficientSAM, MobileSAM, DINOv2-based pipelines) — cheap go/no-go, and the audit table is itself new. (2) On artifact-positive models: paired within-location design — same images, same pixels, test-time registers toggled on/off (no retraining, no new trained params); on-artifact excess failure that vanishes under the toggle needs no matching argument. Dose-response vs artifact-norm percentile.

## 7. A-0271 — SA-1B pipeline fingerprints and their inheritance
- **One-liner:** Tie each SA-1B mask-statistic signature causally to a documented filter stage by same-image filter-ablated relabeling, then measure which signatures matched students inherit — including complexity ceilings under prompts exceeding training support.
- **Strongest attack:** Circularity + content confound — "students copy label statistics" is definitional, and SA-1B-vs-human statistic gaps reflect documented ontology choices (multi-granularity masks), not hidden pipeline artifacts.
- **Shutting-up experiment:** Same-image, filter-ablated relabeling: five label arms on identical COCO/LVIS images (human; full public SAM auto-label stack; −stability; −IoU≥0.88; −NMS); train matched ViT-S promptable students per arm. Content/ontology confounds vanish by construction; each signature statistic is attributed to a specific filter stage; the ceiling test (students pinned to training-complexity ceilings when prompted on high-complexity held-out objects) shows an extrapolation failure that mere label-copying doesn't predict.

---

## Coverage
Prompt-mechanism 1 · SAM2 memory 1 · boundary 2 (architecture law + evaluation validity) · PEFT-forgetting 1 · representation-internals 1 · data-centric 1.

## Cross-cluster adjacency notes (no overlaps)
- A-0062 ↔ B-0112 / C-0276: three distinct evaluation-validity instruments (annotation softness vs convention shift vs protocol drift).
- A-0107 ↔ C-0068/M4: component-resolved vs optimizer-transient forgetting; different mechanisms and model classes.
- A-0271 ↔ B-0230: auto-*labels* vs synthetic-*images*; complementary decompositions.
