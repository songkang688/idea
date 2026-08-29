# Idea_01 experiments

## Datasets (plan, not downloaded here)

- Smoke/fire: public wildfire / smoke segmentation sets used in 2510.21782 (Khan et al. fire datasets as cited there). If licenses block, use a 200-frame hand-split from a CC-licensed smoke video — document provenance.
- Transparent: Trans10K.
- Medical amorphous: infiltrative glioma subset (BraTS) as *optional* Week 2, not Day 1.
- Object control: COCO 2017 val, 100 random “thing” instances with GT boxes.

Splits: image-level, no video leakage. Report scanner/video-id held-out when applicable.

## Preprocess

- SAM official resize/normalize.
- No extra color jitter in killer exp (confounder).
- Density GT: binary masks unless multi-rater exists.

## Baselines

1. Prompted SAM ViT-B, GT box (official).
2. Prompted SAM2.
3. Automatic mask generator (negative control).
4. nnU-Net or a 5-level U-Net trained on the **same 200 images** (equal data, not equal history).
5. Med-SA **only after** killer exp (do not let adapter training contaminate H1).

## Metrics

NSD (τ=2px or 2mm), Dice, HD95, soft-AP on density, ECE if using IoU (Idea_03). Size-quartile breakdown.

## Experimental matrix

| ID | Question | Conditions |
|----|----------|------------|
| E0 | Killer | A/B/C above |
| E1 | Prompt tightness matched | jitter boxes to IoU∈{0.5,0.7,0.9} |
| E2 | Head depth | linear vs 1×1 vs 3×3 vs 2-layer |
| E3 | SAM vs SAM2 frozen E |
| E4 | Equal annotation minutes vs nnU-Net |
| E5 | Trans10K transfer of smoke-trained head (expect fail if density is domain-specific) |

## Ablation

Exclusion channel on/off; TV loss on/off; freeze vs unfreeze last encoder block (should be **worse science** if it helps — contaminates H1).

## Controls

COCO object split. Random-features encoder (break \(E\)): **EXPECTED** collapse if H1 uses real SAM features.

## Robustness / generalization

JPEG q=50; prompt jitter; video-id holdout.

## Failure analysis

If B wins on smoke by predicting “whole sky”: check precision. If C only helps because the ring leaks GT: ablate ring width independently of GT.

## Negative result interpretation

H1 false + random-features also fails → encoder limit (align 2412.04243).  
H1 false + random-features works → data leakage in our head (implementation bug).

## Compute

Killer: 1×12–24GB GPU, <8h including embedding cache. Full: 2–3 days.
