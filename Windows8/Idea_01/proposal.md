# Idea_01 — Objectness, Not Features

**Recommended #1 for this Windows round.**

Status: HYPOTHESIS-level research package. No actual experimental results.

## Executive summary

**One sentence:** SAM-family failures on smoke, fire, glass, and infiltrative lesions are caused by an **objectness decoder/prompt prior**, not by missing encoder features — and a frozen-encoder linear/density head plus exclusion-region prompts should beat prompted SAM on amorphous targets while losing on COCO objects.

If this is false, the encoder really lacks the features (aligns with texture-separability accounts) and we **kill** the project in one GPU-day.

## Research motivation

KNOWN FACT: SAM (Kirillov et al., ICCV 2023) and SAM 2 (Ravi et al., 2024) are trained to output instance masks from points/boxes. EVIDENCE: they underperform on context-dependent and low-contrast concepts (arXiv:2412.01240; arXiv:2412.04243) and fire is typically rescued with tight boxes (arXiv:2510.21782).

The community default (MODEL SPECULATION in papers, treated as fact) is: “need medical/fire adaptation of the encoder.” Med-SA, SAMed, LoRA-MedSAM all spend parameters on the encoder/adapters.

**Why this might not be true:** object-like targets share a topological prior (closed boundary, interior vs exterior) that smoke/infiltrative tumor/glass do not. That prior can live entirely in the **prompt + mask decoder**. Encoder embeddings might already be linearly informative.

## Problem definition

Let \(x\) be an image, \(z = E(x)\) frozen SAM image embeddings, \(p\) a prompt, \(D\) the SAM mask decoder.

- **Object-like** targets: COCO things.
- **Amorphous** targets: smoke, fire plumes, transparent objects, infiltrative tumors.

**Question:** Does \(D(\cdot, p)\) destroy information that is still present in \(z\)?

## Core hypothesis (falsifiable)

**H1:** A linear or 1×1-conv head on frozen \(z\) trained with a density/BCE loss for 200–2000 amorphous images achieves **higher NSD** (and not merely Dice) than official prompted SAM/SAM2 with GT boxes on the same images.

**H2:** The same frozen head is **worse** than prompted SAM on COCO val object subsets (so we did not train a generic better segmenter).

**H3:** Exclusion-region prompts (a negative ring / “not-object” mask) improve prompted SAM on amorphous targets **without** encoder FT, and do not help COCO.

If H1 is false: encoder features are insufficient → stop Idea_01 as a method; publish the negative as support for 2412.04243-style encoder limits.

## Key insight

The scientific object is **where the failure lives** (encoder vs objectness interface), not a new backbone.

## Novelty (precise)

| Closest work | What they did | Exact difference |
|---------------|---------------|------------------|
| 2412.01240 | Evaluate SAM/SAM2 on CD concepts | Evaluation; no frozen linear probe, no exclusion-region intervention |
| 2412.04243 | Texture / tree-likeness metrics | Competing mechanism (texture in \(E\)) vs ours (objectness in \(D,p\)) |
| 2510.21782 | Box prompts for fire | Boxes still assume an object extent; we test exclusion/density |
| Med-SA / LoRA-MedSAM | Train adapters/LoRA for medical Dice | We forbid encoder updates in the killer experiment |

Remaining novelty confidence: **medium**. A probe paper is easy to desk-reject; the **interaction** (win on amorphous, lose on COCO) is the paper.

## Proposed method

1. Extract \(z = E(x)\) from frozen SAM ViT-B/L (and SAM2 Hiera-B+ as a required generalization).
2. **Density head** \(h_\theta(z) \in [0,1]^{H' \times W'}\), bilinear upsample.
3. Optional **exclusion prompt**: rasterize a negative band outside a loose box; feed as mask prompt to \(D\) for the prompted baseline and as extra channels to \(h_\theta\).
4. Train \(\theta\) only.

### Data flow

Image → frozen encoder → \(z\) → \(h_\theta\) → upsample → density → threshold for binary metrics (report also continuous ranking).

## Mathematical formulation

\[
\mathcal{L} = \lambda_{\mathrm{bce}} \mathrm{BCE}(\hat{y}, y) + \lambda_{\mathrm{dice}} \mathrm{Dice}(\hat{y}, y) + \lambda_{\mathrm{tv}} \mathrm{TV}(\hat{y})
\]

For smoke, \(y\) may be soft (rater frequency). **HYPOTHESIS:** TV on density beats CRF-style postprocess.

Do not threshold before the loss.

## Killer experiment (Day 1)

On a public smoke or fire set **and** a 100-image COCO subset:

| Condition | Trainable | Prompt |
|-----------|-----------|--------|
| A Prompted SAM GT-box | none | GT box |
| B Frozen linear/density head | \(h_\theta\) only | none |
| C B + exclusion channel | \(h_\theta\) | loose box + negative ring |

**Continue** if NSD(B or C) > NSD(A) on amorphous **and** NSD(B) < NSD(A) on COCO.  
**Pivot** if B≈A everywhere (method not interesting; maybe calibration paper).  
**Kill** if B << A on amorphous (encoder is the bottleneck; do not add adapters to “fix” without new science).

## Expected results (HYPOTHESIS, not measured)

- Amorphous NSD: C ≥ B > A
- COCO: A > B
- Dice gaps smaller than NSD gaps

## Stop / continue

See `roadmap.md`.
