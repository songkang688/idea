# Idea_01 Reviewer #2

## Most dangerous rejection

“This is WiSE-FT with extra distillation. HQ-SAM already reported the COCO drop. MedSAM already fine-tunes SAM. No new mechanism.”

## Hidden assumption

That COCO click mIoU is a valid proxy for SA-1B promptability, and that interpolation in weight space is the right null.

## Confounders

- Extra replay data = extra regularization, not “constraint.”
- Teacher masks inherit SAM errors; student copies SAM’s ontology.
- Interactive eval simulation ≠ humans (RClicks).

## Missing baselines

WiSE-FT, model soup of epoch checkpoints, EWC, LoRA at matched train time, decoder-only.

## Unfairness

Constrained method sees COCO images; naive FT does not. **Control:** naive FT with COCO images but **classification/misc loss** or **unrelated reconstruction**, to test “any COCO pixels” vs prompt-replay.

## Trivial alternative

Pick α on val Dice subject to J_gen ≥ ε — no new training.

## Rebuttal experiments (must run before submission)

1. Domination vs WiSE-FT (fatal).
2. Naive + COCO images without prompt distillation.
3. Human 8-user click subset (small) to show ranking not reversed vs simulation.
4. LVIS tail classes: retention not only COCO head classes.
