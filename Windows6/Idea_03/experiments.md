# Idea_03 experiments

## Killer

1. Pick **one** model family with base and chat weights.
2. RefCOCO-style or synthetic referring: always output `x1,y1,x2,y2` via constrained decoding.
3. Also score the **likelihood** of the gold box string (format-immune-ish).
4. Fit linear probe: visual tokens → box (or region center) on a small train split; eval both checkpoints with **frozen** encoder.
5. Report: generated-box IoU vs probe error. **EXPECTED split:** if gen drops and probe holds → format; both drop → representation.

## Stage 5 engineering

Eval modes: (1) free-form (2) grammar-constrained (3) likelihood rank of GT vs ≤16 shared distractor boxes.

Outcomes: **O1** gap dies under likelihood → format artifact (write negative). **O2** gap in likelihood, probe OK → policy tax. **O3** probe also drops → representation tax.

Day-1: one pair (e.g. Qwen-VL vs Chat), 2k RefCOCO, three modes. ≤8 GPU-h. **Hard gate:** identical vision encoder + coordinate tokenization.

**STOP** if likelihood gap ~0 on pair 1 and pair 2. Do not run DPO unless observational gap survives format control.
