# Reviewer summary — Windows8

## Independent review dimensions (Stage 2)

Novelty, significance, scientific question, soundness, feasibility, compute, datasets, baselines, already-published risk, experimental clarity, venue potential, risk, upside, ROI.

Scoring was **not** a mean-rank. Protected: high-risk/high-reward, cheap-to-kill, reviewer-divergent, anti-modular.

## Prior-work kills (Stage 3) — EVIDENCE

| Claim we might have made | Closest work | Decision |
|--------------------------|--------------|----------|
| Adapt SAM to medical with adapters/LoRA | Med-SA (Wu et al., arXiv:2304.12620, MedIA 2025); SAMed; LoRA-MedSAM | **Kill as a method paper.** Keep only *mechanism* questions PEFT does not answer. |
| SAM fails on context-dependent / fire / transparent | arXiv:2412.01240 (CD concepts); arXiv:2510.21782 (fire + boxes); Trans10K + SAM evals | **Kill as an evaluation-only paper.** Mutate to causal intervention (exclusion/density, frozen linear probe). |
| Failures are texture / tree-likeness | arXiv:2412.04243 | Do not repeat their metric. Test a *competing* mechanism: objectness decoder vs texture encoder. |
| Dice ranking ≠ boundary/small-lesion ranking | CC-Dice, AAAI 2025 | **Kill metric-only.** Use NSD/CC-Dice as *tools*, not the contribution. |
| Box prompts beat points on fire | 2510.21782 | **Kill.** Mutate to tightness-matched confounder study (X-0006, not in final 3). |

## Reviewer #2 attacks that survived only if a killer experiment exists

- “Linear probe is not CVPR.” Shut up by: probe vs prompted SAM vs Med-SA on *same frozen encoder*; if probe wins on smoke and loses on COCO, the story is causal.
- “LoRA is low-rank by definition so spectrum is obvious.” Shut up by: comparing rank-64 LoRA vs rank-4 + high-frequency residual; prediction is NSD gap not Dice gap.
- “Everyone already thresholds SAM IoU.” Shut up by: reliability diagrams showing **anti-calibration** (higher IoU token → higher error) on amorphous sets.

## Echo-chamber audit (Supervisor self-check)

Bias risk: over-weighting SAM. Mitigation: equal-annotation bakeoff and nnU-Net remain in Idea_01 controls. Bias risk: over-weighting smoke. Mitigation: Trans10K + infiltrative tumor as required generalization axes.
