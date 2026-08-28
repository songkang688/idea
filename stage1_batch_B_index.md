# Stage 1 — Batch B Index

**PI:** Windows5
**Stage:** 1 (Autonomous Research Idea Evolution)
**Batch:** B
**Ideas file:** `stage1_batch_B_ideas.md`
**Total ideas:** 340 (IDEA-B-0001 … IDEA-B-0340, sequential, no gaps)

All entries are hypotheses with minimal experiments; no empirical results are claimed anywhere in this batch, and no citations are fabricated.

---

## 1. Cluster Map

| # | Cluster (angle) | ID range | Count |
|---|---|---|---|
| 1 | Dataset failure / annotation efficiency / long-tail | IDEA-B-0001 – 0040 | 40 |
| 2 | Domain shift / cross-domain transfer | IDEA-B-0041 – 0080 | 40 |
| 3 | Evaluation weakness / calibration / uncertainty / robustness | IDEA-B-0081 – 0120 | 40 |
| 4 | Representation mismatch | IDEA-B-0121 – 0155 | 35 |
| 5 | Multimodal supervision | IDEA-B-0156 – 0185 | 30 |
| 6 | Synthetic data pitfalls | IDEA-B-0186 – 0215 | 30 |
| 7 | Detection limitations | IDEA-B-0216 – 0245 | 30 |
| 8 | Parameter efficiency vs quality (PEFT) | IDEA-B-0246 – 0280 | 35 |
| 9 | Surprising empirical phenomena worth testing | IDEA-B-0281 – 0315 | 35 |
| 10 | Genuinely motivated combinations | IDEA-B-0316 – 0330 | 15 |
| 11 | SR / restoration / generation / diffusion / LLM agents (dense-prediction questions only) | IDEA-B-0331 – 0340 | 10 |
| | **Total** | | **340** |

Domain coverage inside clusters (recurring threads): SAM/promptable segmentation (throughout, dominant), medical imaging (CT/MRI/ultrasound/endoscopy/histopathology/surgery), smoke/fire/wildfire monitoring, transparent objects, detection pipelines, VLM/open-vocabulary grounding, PEFT/LoRA, domain adaptation and TTA, few/zero-shot, prompt learning, synthetic/generative data, representation probing.

---

## 2. Twenty Most Surprising Ideas

Selected for counterintuitive hypotheses that, if confirmed, would overturn a standard assumption.

1. **IDEA-B-0281** — Slightly off-center clicks may beat centroid clicks; the canonical prompt location may be systematically suboptimal.
2. **IDEA-B-0282** — Adding a correction click can make the mask *worse*; interactive refinement may be non-monotonic via decoder mode-switching.
3. **IDEA-B-0285** — Mild JPEG compression may *improve* smoke segmentation by acting as a matched filter that removes high-frequency clutter.
4. **IDEA-B-0287** — Throwing away color can improve RGB medical segmentation (color as a shortcut carrier, not a signal).
5. **IDEA-B-0288** — Larger SAM variants may be *worse* on tiny structures — an inverse-scaling pocket in dense prediction.
6. **IDEA-B-0293** — Freezing early layers may hurt more for "closer" domains (endoscopy) than "farther" ones (CT), inverting the depth-distance heuristic.
7. **IDEA-B-0304** — Skip connections — dense architecture dogma — may pipe domain style directly into predictions and undermine robustness.
8. **IDEA-B-0306** — Rank-1 LoRA may beat rank-16 on tiny datasets; optimal rank may need to *shrink* with data.
9. **IDEA-B-0310** — Training on *soft* labels can produce *harder* (more overconfident) predictions — soft supervision backfiring.
10. **IDEA-B-0313** — Frozen *random* encoders may nearly match pretrained ones on texture-driven medical tasks, bounding where pretraining actually matters.
11. **IDEA-B-0315** — 5% unrelated out-of-domain data may out-regularize optimally tuned weight decay for small-data fine-tuning.
12. **IDEA-B-0338** — Denoising may *delete* the earliest detectable signal for tiny targets: sensor noise interaction as a forensic detection cue.
13. **IDEA-B-0055** — Adapting a model to tolerate fog may make it *blind to smoke* — a "negative domain" whose invariance harms a confusable target class.
14. **IDEA-B-0017** — Transparent-object benchmarks contain almost no glass-free images, so false-positive behavior of top methods is essentially unmeasured.
15. **IDEA-B-0019** — Humans correcting SAM proposals may anchor to SAM's errors, so model-in-the-loop datasets inherit model-lineage bias.
16. **IDEA-B-0075** — SAM may segment glass by its *reflections* (domain-fragile) rather than its boundaries (domain-stable) — testable by reflection swapping.
17. **IDEA-B-0126** — Transparent-object failure may be an output-format problem, not a feature problem: frozen features may already decode two layers.
18. **IDEA-B-0200** — Pixel-perfect synthetic labels may train *worse* models than deliberately degraded, annotator-noise-matched labels.
19. **IDEA-B-0300** — MAE-style continued pretraining on target data may *erode* the objectness structure promptable decoding depends on.
20. **IDEA-B-0302** — Class labels may be dead weight for prompted models: class-agnostic masks alone may train delineation just as well.

---

## 3. Twenty Cheapest-to-Falsify Ideas

Selected for requiring only public checkpoints, public datasets, and evaluation compute (no or minimal training), so the core hypothesis can be killed quickly.

1. **IDEA-B-0083** — Re-run public medical-SAM checkpoints under 5 prompt protocols; if rankings are protocol-stable, hypothesis dies. Evaluation only.
2. **IDEA-B-0090** — Size-stratified re-scoring of public checkpoints; disagreement with mean-IoU rankings is directly computable.
3. **IDEA-B-0093** — Score multimask outputs under oracle vs self-selection; the generation-vs-selection gap falls out of existing outputs.
4. **IDEA-B-0104** — Feed wrong-organ prompts to SAM and read the confidence distribution; silent-failure behavior is observable immediately.
5. **IDEA-B-0117** — Recompute threshold-sweep metrics for public checkpoints; threshold-artifact share of reported gaps is pure evaluation.
6. **IDEA-B-0120** — Coverage-test SAM's multimask spread as an uncertainty interval in and out of domain; no training required.
7. **IDEA-B-0125** — Paste identical crops at controlled positions and measure SAM's position-response surface; frozen-model evaluation.
8. **IDEA-B-0128** — Dense click-grid mapping of prompt-to-mask discontinuities on a few hundred images; frozen-model evaluation.
9. **IDEA-B-0130** — Probe background regions and correlate with hallucination under forced prompts; probing plus evaluation.
10. **IDEA-B-0136** — Evaluate luminance-only vs RGB smoke segmentation with public models before any retraining; the causal claim dies fast if TP drops.
11. **IDEA-B-0139** — Render parametric shape families and sweep SAM along shape axes; prior-strength curves need no training.
12. **IDEA-B-0153** — Measure quality-vs-click-count saturation with controlled click sequences on frozen models.
13. **IDEA-B-0059** — Fill the prompt-type × shift-type robustness matrix with frozen models across existing shifted datasets.
14. **IDEA-B-0084** — Compare SAM's predicted IoU against actual IoU across domains; the calibration audit is a single evaluation pass.
15. **IDEA-B-0089** — Collect image-only prompts from a handful of users and compute the oracle-prompt inflation factor on existing benchmarks.
16. **IDEA-B-0281** — Dense click grids over object populations directly confirm or kill the off-center-click advantage.
17. **IDEA-B-0282** — Simulated correction sequences on frozen models measure click-regression rates immediately.
18. **IDEA-B-0285** — Sweep JPEG quality on smoke benchmarks with frozen models; non-monotonicity is either there or not.
19. **IDEA-B-0299** — Position-stratified metrics across resolution ladders on public ViT segmenters expose the border penalty without training.
20. **IDEA-B-0305** — Fine-grained resolution sweeps (2–4 px steps) plus a periodicity test on frozen models settle the aliasing claim.

---

## 4. Notes for Stage 2 (selection/evolution)

- Clusters 3 and 9 contain the highest density of evaluation-only experiments — good candidates for early falsification passes at low compute.
- Clusters 5, 6, and 10 contain the highest-variance/highest-payoff bets (new supervision channels, physics-grounded labels, theory imports); most require data collection or partnerships.
- Several ideas form natural chains (e.g., 0084 → 0098 → 0110 on failure detection and certification; 0186 → 0190 → 0191 → 0207 on synthetic-data dynamics; 0246 → 0255 → 0271 → 0306 on rank laws) that could be merged into programs in later stages.
- Forbidden patterns audit: no idea is a pure module-stack, a bare "apply to medical" port, or a loss/backbone swap; combination ideas (0316–0330) each state their scientific motivation explicitly.
