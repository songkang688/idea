# Idea_03 experiments

## Killer

Model: 2D U-Net, 3 seeds.
Train: LIDC slices with ≥2 raters; f = mean vote.
Splits: leave-one-scanner-out if scanner IDs usable; else intensity/noise shift as declared proxy.
Methods: hard CE; hard CE+TS (T on source val); soft BCE to f; optional ensemble.
Metric: sparsification AURC on target domain, plus Dice.
Kill: soft AURC not better than hard+TS by a pre-registered margin (e.g. 5% relative) with overlapping CIs.

## Full

QUBIQ; stain perturbation; annotator-id model; risk-coverage.
