# Proposal — PromptAmnesia (P065, gated by P082)

## 1. Executive Summary

Document **prompt-type-resolved retention** of SAM under PEFT, not “SAM forgets” (already CA-SAM/Gu). Mixed-prompt FT is the load-bearing column.

## 2. Motivation

Medical SAM papers report in-domain Dice. Deployed users still click. If clicks die while Dice lives, the literature is measuring the wrong skill.

## 3. Problem

Train on dataset D with protocol π∈{box, point, mixed}. Evaluate skills Σ = {box, point, negative, multimask entropy} on D and on COCO zero-shot.

## 4. Hypothesis

**H1:** Boxes-only LoRA at matched D-Dice drops COCO point Dice more than mixed-prompt LoRA.

**H2 (gate):** A val-tuned threshold recovers ≥50% of the apparent drop → forgetting is miscalibration (P082); then the paper becomes the gatekeeper audit.

## 5. Insight

Forgetting is a **behavior battery**, not a dataset mIoU.

## 6. Novelty vs Gu et al. / CA-SAM / EvoSAM

They measure OOD Dice or propose a method. We measure **cross-protocol skill** with mixed-prompt control and multimask diversity (C1-061).

## 7. Literature

Gu et al. arXiv:2404.09957; CA-SAM arXiv:2511.17201; EvoSAM arXiv:2503.06236; InfLoRA (cls, not this); SAM paper multimask design.

## 8. Method

Frozen encoder default; LoRA on decoder (and optional prompt encoder). Three train recipes: box, point, mixed. No new blocks.

## 9. Diagram

See `diagrams/architecture.md`.

## 10. Math

Retention \(R(\sigma)=s_{\text{FT}}(\sigma)/s_{0}(\sigma)\). Matched-gain constraint: \(|s_{\text{FT}}(D)-s_{\text{ref}}(D)|<\epsilon\).

Diversity: mean pairwise IoU among 3 masks (lower = more diverse).

## 11. Implementation

`src/gate_threshold.py`, `src/eval_prompts.py`, training stub.

## 12. Data

Public organ 2D (e.g. a Kaggle-license set the user already has) + COCO val. **Do not commit medical images.**

## 13. Baselines

Frozen SAM; decoder-full-FT small LR (C1-076 confound); mixed-prompt; WiSE-FT interpolation as arm not paper (P110 dead).

## 14. Metrics

Dice/IoU per prompt type; multimask pairwise IoU; ECE of IoU-head (P031 arm).

## 15–16. Matrix / ablation

See `experiments.md`. Stitching controls if running P177 chapter.

## 17. Killer

P082 on one public ckpt (hours). Then 1-epoch LoRA box vs mixed, n small.

## 18. Expected

**EXPECTED:** mixed retains points better. **ACTUAL:** none.

## 19–20. Failures / negatives

If mixed = box, protocol coverage was the whole story. If gate recovers the drop, publish P082 and kill P065 method claims.

## 21–22. R2

Coverage-vs-forgetting: mixed column **mandatory**. Oracle best-of-3 for diversity claim.

## 23. Compute

1×24GB, 1–3 days for LoRA grids.

## 24. Roadmap

Day 1: gate. Day 2–3: LoRA box vs mixed. Week 1: COCO zero-shot battery. Week 2: P177 stitch if gate fails to kill the thread.

## 25. Stop

Kill P065 if gate explains ≥50% drop. Pivot to calibration paper (P031). Continue if mixed ≫ box on points at matched D-Dice.

## 26. Extensions

SAM2; multi-hospital.

## 27. Story

“We fine-tuned SAM for Dice and accidentally untaught it to take a click.”

## 28. Titles

- Prompt Amnesia: Protocol-Resolved Forgetting in Adapted SAM
- Mixed Prompts as Retention Insurance
- When Dice Lives and Clicks Die
