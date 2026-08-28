# Idea_03 — AlphaSmoke

**One-liner:** Transfer matting pretraining to real smoke, and show whether binary Dice rankings reverse under alpha/matting metrics.

**Killer:** Frozen encoder + linear head: ImageNet/SAM vs a matting encoder (or portrait-matting fine-tune of the same backbone) on a **public binary smoke set** as primary. HSV/physics color baseline required. Optional synthetic alpha as diagnostic only.
