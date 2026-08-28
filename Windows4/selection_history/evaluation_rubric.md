# Stage 2+ Evaluation Rubric (Windows4)

Do **not** rank by mean score. Use a decision rule.

## Dimensions (1–5 unless noted)

1. Novelty (scientific, not architectural)
2. Significance (who is wrong if we are right?)
3. Scientific question clarity
4. Technical soundness
5. Feasibility (one lab, weeks not years)
6. Compute (lower is better for ROI)
7. Dataset availability
8. Baseline availability
9. Likelihood already published (higher = worse)
10. Experimental clarity / falsifiability
11. Venue potential (CVPR/ICCV/ECCV/MICCAI) as *story quality*, not prestige chasing
12. Risk
13. Upside
14. Research ROI = (upside × falsifiability) / (compute × calendar friction)

## Survival rules (protect from mean-score death)

- High-risk, high-upside with a cheap Killer Experiment
- Simple counter-intuitive hypothesis
- Extreme reviewer disagreement
- Can be killed in <1 GPU-day

## Kill rules

- Core novelty is “new module”
- Hypothesis is not falsifiable
- Killer experiment requires a new foundation-model pretrain
- Closest prior work already ran the same experiment (Stage 3)
- Reviewer #2 attack cannot be answered by an experiment (Stage 4)

## Stage 3 stance

Default: **this idea has already been done.** Agents hunt to kill novelty, not to praise it.
If partial overlap: **mutate**, do not auto-kill.

## Stage 4 stance

Default: **reject the paper.** Survival iff a realistic experiment would silence the attack.
