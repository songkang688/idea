# Eliminated ideas (compressed)

Raw pool: 2766. This file records **classes** of kills, not every ID.

## Pseudo-innovation (never entered Stage 2)

Module stacking, backbone swaps, “SAM + attention”, “apply Transformer to medical” — forbidden at generation.

## Exact or conceptual duplicates of prior work (Stage 3)

- Medical SAM Adapter / SAMed / LoRA-MedSAM as the paper.
- “Evaluate SAM2 on fire with boxes.”
- “SAM struggles with CD concepts / transparency” without a new mechanism.
- “Propose CC-Dice / size-stratified Dice” as the contribution.

## Reviewer #2 unsound (Stage 4)

- SA-1B membership leakage as a main claim (cannot audit cheaply).
- SAM2-CD “language vs vision” without an interface.
- Open-vocab VLM dense papers that cannot freeze the grouper fairly (X-0010 parked).

## Parked high-ROI (not final 3)

| ID | Why parked | Revive if |
|----|------------|-----------|
| X-0007 Replay promptability | Strong; overlaps Idea_02 forgetting subplot | Idea_02 killer is negative and forgetting is the remaining story |
| X-0005 Equal annotation minutes | Important control, not a method | Use inside Idea_01 Week 2 |
| X-0006 Box tightness confound | Cheap workshop paper | After Idea_01 prompt experiments |
| X-0008 Rater-as-model | Needs LIDC multi-rater discipline | Medical-only pivot |
| X-0009 Diameter/patch law | Maybe too simple; still a killer plot | Add as Idea_01 analysis figure |

## Revive rule

A killed idea is revived only if a new experiment would change the final-3 ranking. Metric papers stay dead as lead ideas.
