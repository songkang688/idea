# Idea_01 Reviewer #2

## Most dangerous rejection

“This is a linear probe / prompt trick on known SAM failure cases (smoke, glass). CD-concept and fire-prompt papers already showed SAM is weak; Med-SA already fixes medical. Incremental.”

## Hidden assumptions they will name

- Density GT is well-defined for smoke.
- Frozen official preprocessing matches training.
- GT boxes for SAM are an upper bound (they are not: tightness confound).

## Confounders

- Extra parameters in \(h_\theta\) vs decoder (keep \(h_\theta\) tiny).
- Train data for B/C vs zero-shot A (the point is adaptation locus, not zero-shot fairness — say this in the intro or die).
- Threshold tuning on test.

## Experiments that shut this up

1. **Interaction plot:** amorphous gain × COCO loss (H2).
2. **Parameter-matched** tiny U-Net vs \(h_\theta\) on frozen \(z\).
3. **Random encoder** control.
4. Tightness-matched boxes (E1).
5. Show Med-SA on the same 200 smoke images: if Med-SA wins Dice but loses the COCO-preservation story, different paper (forgetting) — do not hide it.

## Reproducibility attacks

Release embedding-cache script, seeds, exact SAM checkpoint hash, prompt rasterization code (this repo `src/`).
