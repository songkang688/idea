# Windows4 research summary

**KNOWN:** SAM is a promptable segmenter (Kirillov et al., ICCV 2023); medical/smoke/fire adaptations are crowded; Gu et al. (arXiv:2404.09957) already ran decoder-only vs encoder PEFT on medical SAM; RClicks/BREPS already attacked oracle prompts; HalluSegBench scooped the VLM inpaint-hallucination flagship.

**HYPOTHESIS (Idea_01):** Interior image evidence inside a tight box is *not* necessary for high SAM Dice on thing-like objects.

**HYPOTHESIS (Idea_02):** At matched in-domain Dice, mixed-prompt fine-tuning retains zero-shot prompt skills that single-protocol FT loses.

**HYPOTHESIS (Idea_03):** An encoder trained for alpha matting transfers to real smoke better than one trained for binary COCO-style masks, and model ranking reverses under matting metrics.

All numbers in Idea_*/experiments.md are **EXPECTED**, never measured here.
