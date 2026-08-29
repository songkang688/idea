# Idea_02 experiments

## Killer

Train three PEFT variants on a toy or Synapse-like subset. Save encoder feature maps frozen vs adapted. Radial FFT energy.

## Ablation

HP kernel: Laplacian vs Sobel vs random 3×3. Predicted: random 3×3 ≈ LoRA extra rank (no NSD gain).

## Negative

If r64 already high-pass: kill HP method; maybe still publish the audit as a short note.

## Metrics

Dice, NSD, HD95, energy fraction < kc, parameter count, train time.
