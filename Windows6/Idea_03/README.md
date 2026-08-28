# Idea_03 — Alignment tax on VLM localization (mutated)

**Hypothesis:** After controlling **output format**, chat/RLHF checkpoints localize worse than matched **base** (or SFT) models on referring/box tasks; if the drop is **only** in generated coordinates and **not** in a frozen visual-token probe, the tax is formatting, not perception.

## Killer

Constrained decoding + likelihood-based box scoring on existing checkpoint pairs; linear probe on visual tokens; optional tiny text-only DPO.
