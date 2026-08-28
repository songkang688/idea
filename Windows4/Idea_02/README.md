# Idea_02 — PromptAmnesia

**One-liner:** At matched in-domain Dice, does single-protocol PEFT erase other prompt skills (points, negatives, multimask diversity)?

**Gate (must run first):** P082 threshold/plasticity noise floor on a *released* MedSAM/SAM-FT checkpoint. If “forgetting” is only a binarization artifact, **pivot**.

**Killer after gate:** Fine-tune decoder LoRA on boxes-only vs mixed prompts; eval zero-shot points/negatives/diversity on held-out natural images (COCO).
