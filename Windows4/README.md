# Windows4 — Autonomous Research Idea Evolution

- **Windows ID:** Windows4
- **Created:** 2026-08-28 (UTC)
- **Supervisor:** Windows4
- **Repo:** `github.com/songkang688/idea`
- **Status:** COMPLETE for archival of Top-3 packages (no experimental numbers were measured in this run)

## This round’s three Ideas

| # | Folder | Codename | Scientific question |
|---|--------|----------|---------------------|
| 1 | `Idea_01/` | **SeeingInside** | Does SAM actually use image evidence *inside* a tight box, or is it a box→mask interpolator? |
| 2 | `Idea_02/` | **PromptAmnesia** | Does domain PEFT destroy prompt-type skills (points/negatives/multimask) at matched in-domain Dice? |
| 3 | `Idea_03/` | **AlphaSmoke** | Does matting pretraining beat segmentation pretraining on *real smoke*, and do binary Dice rankings reverse under alpha/matting metrics? |

## Most recommended

**Idea_01 SeeingInside.** It is the only flagship whose core novelty survived prior-work assassination *and* whose Reviewer #2 attack is silenced by a cheap, on-manifold counterfactual. It does not require medical FT compute, does not compete with MedSAM/ProFSAM/Gu et al., and a null result is still publishable as a mechanistic fact about SAM.

## Why not the others as #1

- Idea_02 is higher blast-radius but is gated by P082 (forgetting may be a threshold artifact) and crowded by CA-SAM/Gu et al. unless the mixed-prompt column is the paper.
- Idea_03 is the right smoke paper, but R2 requires a measured-alpha arm and real-smoke primary; data/annotation risk is higher.

## Status

All three: **ready to start killer experiments**. No ACTUAL experimental results in this archive (EXPECTED only).

## Next experiment to run (this week)

**Idea_01 killer:** frozen SAM (ViT-B), COCO val subset, GT box prompts. Conditions: (A) original image, (B) box-fill with mean color, (C) on-manifold inpaint inside box (any public inpainter), (D) prompt-only / no-image tokens if API allows, (E) ellipse-in-box geometric null. Primary metric: ΔDice(B−A) and ΔDice(C−A). Stop: if (C)≈(A) and (B)≪(A), SAM uses interior appearance; if (B)≈(A), interpolator hypothesis holds.

Then Idea_02 P082 threshold sweep on one public MedSAM checkpoint. Then Idea_03 HSV + frozen-encoder probe on a public smoke set.
