# Proposal — SeeingInside (P14)

## 1. Executive Summary

**One-liner.** SAM with a tight box may be a geometric interpolator, not an appearance segmenter.

**Abstract.** We intervene on *image evidence inside the prompted box* while holding the prompt fixed. If Dice is invariant to on-manifold interior replacement, SAM is not “seeing” the object. Distinct from prompt-jitter (RClicks, FNPC) and from VLM hallucination benches (HalluSegBench).

## 2. Research Motivation

Foundation-model papers credit the image encoder. If tight-box Dice is explained by box geometry, those credits are wrong, and GT-box tables are not segmentation evaluations.

## 3. Problem Definition

Let \(I\) be an image, \(b\) a box prompt, \(M=f(I,b)\) SAM’s mask. Construct \(I'\) that equals \(I\) outside \(b\) and replaces the interior with (i) constant fill, (ii) on-manifold inpaint, (iii) a swapped other-object crop. Measure \(\mathrm{Dice}(M',GT)\) vs \(\mathrm{Dice}(M,GT)\).

## 4. Core Hypothesis

**H1 (interpolator):** For compact COCO “things,” mean-fill inside \(b\) drops Dice by \(<0.05\) relative to \(I\).

**H2 (appearance):** On-manifold inpaint that removes the object drops Dice by \(>0.15\).

Falsifiable: both can fail.

## 5. Key Insight

Intervene on the **image**, not the prompt. Prior robustness work perturbs clicks/boxes.

## 6. Novelty

RClicks/BREPS: realistic *prompts*. Stable-SAM: prompt stability. We: *image* ablation with prompt frozen. HalluSegBench: VLMs and language; we stay class-agnostic SAM.

## 7. Literature

See `literature.md`.

## 8. Proposed Method

No new architecture. Protocol: frozen SAM; interventions; null models (ellipse-in-box, learned 3-layer conv box→mask). Optional: mask image tokens whose centers fall in \(b\) if using official SAM internals.

## 9. Architecture Diagram

See `diagrams/architecture.md`.

## 10. Mathematical Formulation

\[
\Delta_{\text{fill}} = \mathbb{E}[\mathrm{Dice}(f(I,b),GT)-\mathrm{Dice}(f(I_{\text{fill}},b),GT)]
\]
Interpolator hypothesis: \(\Delta_{\text{fill}}\approx 0\). Appearance hypothesis: \(\Delta_{\text{inpaint}}\gg 0\).

## 11. Implementation

`src/` — interventions, metrics, SAM wrapper, box-fill baseline.

## 12. Dataset Plan

COCO val2017 things, area > 32² px, one instance/image sample. Secondary: a 2D organ set with GT boxes (if license allows). **No patient data in this repo.**

## 13. Baselines

Ellipse-in-box; GrabCut inside box; box-fill SAM; official SAM on \(I\).

## 14. Metrics

Dice, IoU, Boundary-F (tolerance 3px). Report by area decile and by compactness.

## 15. Experimental Matrix

See `experiments.md`.

## 16. Ablation

Fill color (mean vs median vs noise); inpaint model choice; box tightness {0,+4,+16} px (BREPS-aware: do not claim tightness novelty).

## 17. Killer Experiment

64–200 COCO instances, ViT-B if available else baseline-only. Pre-register: interpolator if median \(\Delta_{\text{fill}}<0.05\).

## 18. Expected Results

**EXPECTED (not measured):** mean-fill hurts concave objects more; inpaint hurts textured objects more. **ACTUAL:** none.

## 19. Failure Cases

Holes, occlusion, stuff-like regions, mirrors.

## 20. Negative Results

If all interventions match \(I\), encoder is unused under tight boxes — still a paper. If only noise-fill hurts, SAM uses any interior statistic, not identity.

## 21. Reviewer #2 Attack

Off-manifold fill; SAM uses positional tokens; task degenerates to “fill the box.”

## 22. Response Strategy

Mandatory on-manifold inpaint/swap; ellipse and learned box→mask nulls; medical/smoke slice only as stress test, not headline if N small.

## 23. Compute Plan

1×12GB GPU, <4h for 200 images SAM-B. CPU OK for baselines.

## 24. Implementation Roadmap

Day 1: this killer. Day 2–3: inpaint + swap. Week 1: size/compactness strata. Week 2: token-ablation if code internals available. Full paper: +2 datasets, human examples.

## 25. Stop / Continue

Kill project if ellipse-null matches SAM on \(I\) (SAM unused). Pivot if only fill works but inpaint doesn’t (low-level stats). Continue if inpaint Δ ≫ fill Δ.

## 26. Extensions

SAM2 memory; medical nested tumor-in-organ (not the paper core).

## 27. Paper Story

“We thought SAM segments objects; under the evaluation protocol everyone uses, it may complete the box.”

## 28. Candidate Titles

- Seeing Inside the Box: Does SAM Use Interior Appearance?
- Box Completers: An Intervention Study of Promptable Segmentation
- The Image Encoder’s Missing Credit under Tight-Box Evaluation
