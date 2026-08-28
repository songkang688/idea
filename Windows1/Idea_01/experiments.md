# Idea_01 experiments

All outcomes below are EXPECTED unless labeled ACTUAL (none are ACTUAL).

## Killer experiment (Week 1)

| Item | Spec |
|---|---|
| Backbone | SAM ViT-B official |
| Target | Kvasir-SEG, official split |
| Naive FT | decoder + encoder last 2 blocks, AdamW, 20 epochs, lr 1e-4/1e-5 |
| Constrained | same + replay 50% batch from COCO train, λ∈{0.3,1,3} |
| WiSE-FT | 11-point interpolation naive↔θ₀ |
| Generic eval | COCO val 500-image subset; random 1/3 clicks; center-of-error 1/3; GT-box |
| Seeds | 2 for killer, 3 for paper |
| Kill | constrained does not dominate interpolation at ≥2 λ-matched operating points |

## Full matrix

Domains: Kvasir-SEG, ISIC, COD10K.
Methods: zero-shot, decoder-only, LoRA-r8, full FT, EWC, constrained, WiSE-FT on each naive run.
Prompt types: click, box, mixed.
Report Pareto plots, not only best Dice.

## Ablations

λ, replay buffer size, freeze encoder vs not, LoRA vs full under same L_ret, teacher = θ₀ vs EMA student.

## Controls

Equal steps, equal peak LR grid (unfair LR is the classic confound), identical prompt sampler for eval.

## Robustness

JPEG 50, spatial shift of clicks ±4px, unseen object categories on LVIS.

## Generalization

Train medical, eval generic; train COD10K, eval generic; never tune on generic eval split.

## Failure analysis

Per-class COCO drop; thin structures; holes; multi-mask IoU token calibration.

## Stop conditions

See README §25.
