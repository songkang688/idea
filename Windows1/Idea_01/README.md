# Idea_01 — RetainSAM

**Candidate titles**

1. RetainSAM: Fine-Tuning SAM under a Promptability-Retention Constraint
2. Dominating the WiSE-FT Front: Constrained Adaptation of Promptable Segmenters
3. Keep the Clicks: Domain Adaptation of SAM without Destroying Interactivity

## 1. Executive summary

Fine-tune SAM (or SAM2 image encoder + prompt decoder) on a **target dense-prediction domain** while **explicitly constraining generic promptability** (clicks/boxes on held-out natural images). The scientific claim is not “another adapter.” It is: **a constraint on prompt-behavior metrics during FT can strictly dominate the Pareto front traced by WiSE-FT weight interpolation** between the foundation checkpoint and a naively fine-tuned checkpoint.

If interpolation already traces the front, the *method* is dead; the *evaluation protocol* may still be released as a negative-result / benchmark note.

## 2. Motivation

KNOWN: SAM is used as a foundation weights file and then fully fine-tuned on medical or camouflaged-object sets. Community default: target Dice is the objective; interactivity on SA-1B/COCO is assumed either preserved or irrelevant.

HYPOTHESIS: unconstrained FT silently converts SAM into a smaller specialist, and papers still call the result “SAM.” HQ-SAM-style tables already hint at COCO AP drops under some PEFT placements (EVIDENCE from prior-work agent: HQ-SAM tradeoff table). WiSE-FT (Wortsman et al., 2022) is the trivial way to walk that tradeoff. Nobody (NOT FOUND pending lit-verify) treats promptability as a **constraint** with a **kill test against interpolation**.

## 3. Problem definition

Let θ₀ be official SAM weights. Let D_tgt be a labeled target segmentation set. Let D_gen be a frozen generic promptability suite (images + click/box protocols, **no gradient**).

Find θ that is Pareto-optimal on

- J_tgt(θ) = Dice/mIoU on D_tgt val
- J_gen(θ) = protocol vector: {1-click mIoU, 3-click mIoU, box mIoU, NoC@90}

**Constraint form (training):** minimize L_tgt(θ; D_tgt) + λ L_ret(θ; D_gen^replay)

where L_ret is a differentiable proxy (mask CE/Dice vs SAM-θ₀ pseudo-labels under sampled prompts), not the eval protocol itself.

**Success is not a number on D_tgt.** Success is domination of the interpolation curve θ(α)=(1−α)θ₀+α θ_naive.

## 4. Core hypothesis (falsifiable)

**H1:** There exist operating points where constrained FT achieves higher J_tgt than WiSE-FT at matched J_gen, **and** higher J_gen at matched J_tgt, on ≥2 points.

**H2:** Naive full FT violates a pre-registered ε (e.g., 3-click mIoU drop > 2 points on COCO val) while constrained FT does not, at matched D_tgt train budget.

**Kill H1** if the interpolation polyline is not strictly dominated.

**Kill H2** if naive FT already stays within ε — the problem does not exist for that domain (then try a farther domain before killing the project).

## 5. Key insight

Promptability is a **behavior**, not a single accuracy. Interpolation mixes weights for a scalar blend; it cannot preferentially protect **click-to-mask geometry** while allowing **decoder class-prior** to move. A replay constraint on prompt-sampled masks targets that subspace.

This is a HYPOTHESIS about parameter-space geometry, not a fact.

## 6. Novelty (exact difference)

| Neighbor | They did | We do |
|---|---|---|
| HQ-SAM | Extra decoder tokens for boundaries; report some COCO tradeoff | Constraint + **must beat interpolation** |
| MedSAM | FT SAM on medical; target Dice | Dual eval; retain generic clicks |
| WiSE-FT | Interpolate zero-shot and FT CLIP | Same baseline **as kill switch**, not as our method |
| LoRA / adapters | Fewer params, implicit regularization | Explicit J_gen constraint; compare at matched param count |
| Continual learning / EWC | Protect old-task Fisher | Old task is **promptable segmentation**, measured by click protocols not ImageNet |

Remaining novelty is **conditional** on beating WiSE-FT. Confidence: Medium.

## 7. Literature

See `literature.md`. Only cite papers we treat as KNOWN.

## 8–10. Method, diagram, math

See `diagrams/architecture.md` and math below.

### Training

1. Sample target batch (image, GT mask). Optional: sample a point/box from GT to stay in SAM’s prompt interface.
2. Sample replay images from COCO train (or a SA-1B subset if licensed). Generate prompts (random interior click, noisy box) and **teacher** masks from frozen θ₀ (no grad).
3. Student θ predicts both target and replay masks.
4. Loss:

\[
\mathcal{L} = \mathcal{L}_{\mathrm{DiceCE}}(p_{\mathrm{tgt}}, y_{\mathrm{tgt}}) + \lambda \, \mathcal{L}_{\mathrm{DiceCE}}(p_{\mathrm{replay}}, y_{\theta_0}) + \gamma \|\theta_{\mathrm{enc}} - \theta_{0,\mathrm{enc}}\|_2^2
\]

Optional Lagrangian: increase λ when a cheap running estimate of J_gen drops below ε.

### WiSE-FT baseline

\[
\theta(\alpha)=(1-\alpha)\theta_0 + \alpha \theta_{\mathrm{naive}}, \quad \alpha\in[0,1]
\]

Eval both axes at 11 α. Constrained run must dominate.

## 11. Implementation

Runnable prototype in `src/` (interpolation, losses, prompt sampling, eval hooks). Full SAM training requires the official `segment-anything` checkpoint (not bundled).

## 12. Data

- Target (pick one for killer): Kvasir-SEG or ISIC 2018 or COD10K.
- Generic suite: COCO 2017 val (things), LVIS rare-class subset, optional ADE20K stuff (expected harder).
- Do **not** train on COCO val.

## 13. Baselines

Zero-shot SAM; decoder-only FT; LoRA on encoder; full FT; WiSE-FT; optional EWC on encoder.

## 14. Metrics

Target: Dice, NSD/Boundary IoU. Generic: mIoU @ 1/3/5 clicks (center-of-error simulation **and** random-interior clicks — RClicks showed simulation bias; we report both). Box mIoU. NoC@90. Retention Δ vs θ₀.

## 15–17. Experimental matrix / ablation / killer

See `experiments.md`.

## 18. Expected results (NOT measured)

EXPECTED: naive FT gains 8–20 Dice on medical vs zero-shot, loses several points of COCO 3-click mIoU. WiSE-FT traces a smooth front. Constrained FT EXPECTED to sit above the front if replay is non-redundant with interpolation; EXPECTED to collapse onto the front if not.

## 19. Failure cases

Far-domain medical where encoder must move a lot; stuff classes; tiny objects; SAM2 memory prompts (out of v1 scope).

## 20. Negative results

If WiSE-FT matches: publish the **promptability-retention suite** and the negative result (“interpolation is enough”). That is still a paper, but not *this* method paper. Pivot to Idea_03 as #1.

## 21–22. Reviewer #2 / response

Attack: “HQ-SAM Table X already showed the tradeoff; WiSE-FT already walks it.”
Response experiment: **domination plot**. If no domination, they are correct — stop.

Attack: “Replay is just distillation, not a constraint.”
Response: compare λ=0 distillation-off vs λ>0 vs interpolate; show replay≠interpolation.

Attack: “COCO is not SA-1B.”
Response: document proxy; optional SA-1B subset if available.

## 23. Compute

Killer: ~4–6 GPU-days (A100). Full: ~20 GPU-days, 3 domains, ViT-B then ViT-H, 3 seeds.

## 24. Roadmap

See `roadmap.md`.

## 25. Stop / continue

- **Kill method:** no Pareto domination on 2/2 target domains.
- **Pivot:** replay-only equals constrained → continual-learning short paper.
- **Continue:** domination on medical + one non-medical (COD10K).

## 26. Extensions

SAM2 video promptability; MedSAM weights as θ₀; per-layer interpolation vs our constraint.

## 27. Paper story

“Everyone interpolates. We show that protecting *click behavior* is not the same as mixing weights — or we show that it is, and stop calling unconstrained medical FT ‘SAM’.”

## 28. Titles

Listed at top.
