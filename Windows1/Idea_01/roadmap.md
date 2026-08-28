# Idea_01 roadmap

| When | Work | Stop check |
|---|---|---|
| Day 1 | Install SAM; WiSE-FT interpolation on **one already-FT public MedSAM-class checkpoint if available**, else start naive FT overnight; implement prompt suite | Suite reproduces ballpark zero-shot SAM COCO clicks |
| Day 2–3 | Finish naive FT; 11-α curve; implement constrained loss | If naive already within ε on COCO, switch target to farther domain |
| Week 1 | Constrained λ sweep; domination test | **Kill method if no domination** |
| Week 2 | LoRA/EWC/COCO-pixels controls; 2nd domain | |
| Full paper | ViT-H, 3 seeds, human click micro-study, SAM2 variant | |

Code entry: `src/train_retain.py` (prototype).
