# Idea_03 experiments

## Killer

1. Pick **one** model family with base and chat weights.
2. RefCOCO-style or synthetic referring: always output `x1,y1,x2,y2` via constrained decoding.
3. Also score the **likelihood** of the gold box string (format-immune-ish).
4. Fit linear probe: visual tokens → box (or region center) on a small train split; eval both checkpoints with **frozen** encoder.
5. Report: generated-box IoU vs probe error. **EXPECTED split:** if gen drops and probe holds → format; both drop → representation.

## Stop

- **Kill** if no matched checkpoints or H1 is null under constraints.
- **Pivot** to SFT-only vs base if RLHF weights unavailable.
- **Continue** if H1 holds and H2 discriminates mechanism.
