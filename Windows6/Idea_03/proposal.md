# Idea_03 proposal

## Executive summary

Visual forgetting under instruction tuning is **published** (e.g. MDGD, EMNLP Findings 2025). Reviewer #2 killed the generic headline. **Remaining:** a **stage-isolated localization curve** with format controls.

**H1:** Constrained box metrics drop from base → chat on ≥1 public pair (e.g. families where both weights exist).

**H2:** Linear probe on frozen visual tokens does **not** drop (tax is decoding/format) **or does** drop (tax is representation).

**H3 (optional, causal):** LoRA DPO on **text-only** preferences still hurts H1 → objective, not image data mix.

**Kill** if H1 fails under constrained decoding (formatting confound).

## Novelty

Not “alignment hurts vision.” The paper is **which stage** and **whether the visual backbone still contains the box**. TWIST&SCOUT / MDGD are closest; we must cite them as attacks.

## Compute

Eval-only: 1 GPU, 1–2 days. Optional DPO: 1–2×24GB, days.
