# Stage 4 — Cluster C KILLED List (Reviewer #2)

**11 of 18 Stage-3 survivors killed.** One paragraph per kill: the fatal attack and why no realistic experiment rescues it. Full transcripts in `stage4_cluster_C_attacks.md`.

The instructed extra-harsh criteria did the most damage: six of the eleven are pure audits or analysis-only papers with no causal lever (C-0093, C-0276, C-0320, C-0332, M1/C-0002, M5/C-0099).

---

## C-0093 — Dimensional collapse doesn't hurt transfer *(was Stage-3 KEEP)*

Analysis-only with no downstream decision. RankMe claims prediction, not causation — and prediction is what practitioners use it for; VICReg-family regularizers are justified by end-task gains, not rank metrics. So even a flawless interventional result (flat transfer across an order of magnitude of rank) retires no method, no metric, no workflow. Worse, the intervention acts on projector rank while transfer is read from backbone features (wrong-variable objection), and "except at extreme collapse" is a built-in unfalsifiable escape hatch. The only rescue — showing RankMe-guided selection actively misleads — is expected to fail against RankMe's own validation.

## C-0276 — The many ADE20Ks: split drift breaks cross-paper comparability *(was Stage-3 KEEP)*

The purest "we ran an audit" in the batch: no hypothesis at risk (everyone believes drift exists; only its size is unknown), no causal lever, no decision that changes — "the field should standardize" is a call to action, not a finding. Attribution of drift to specific conventions requires a within-framework factorial that dissolves the six-framework headline into piecemeal protocol ablations papers already run. Execution is easy and the result certain to be nonzero, which is exactly the problem: no experimental risk means no experiment can save it. **Salvage:** build the fixed-checkpoint protocol harness as shared evaluation infrastructure for the surviving C-0310/C-0302 experiments.

## C-0320 — Mild shifts compound super-linearly *(was Stage-3 KEEP)*

"Super-linear" is a units artifact until proven otherwise: bounded metrics cannot compose additively by arithmetic, and the same data can look sub-linear, additive, or super-linear in error-rate vs. log-odds vs. independent-failure space — the classic additive-vs-multiplicative interaction trap, which epidemiology never resolved. The likely outcome (approximately independent-multiplicative composition) is a worthless null; the exciting outcome yields only "benchmarks should compose" — an audit conclusion with no lever on any model. The rescue (pre-registered functional form + mechanistic training interventions) converts it into a different, training-heavy paper nobody proposed.

## C-0332 — Does "accuracy on the line" survive dense prediction? *(was Stage-3 KEEP)*

A scope-test audit with no lever, on a model panel that can't support the fit (a few dozen backbone-sharing segmenters vs. Miller et al.'s hundreds of diverse classifiers). If the law holds, nothing changes; if it breaks, the deviation is plausibly Jensen's-inequality arithmetic (mIoU is a nonlinear aggregate of per-class ratios), not a robustness phenomenon. The operational use case — predicting segmentation performance under shift without labels — is already served per-image by Reverse Classification Accuracy (Valindria et al., IEEE TMI 2017) and successors. The only rescue is a working corrected OOD-mIoU estimator, which is a different paper of unknown feasibility.

## C-0002 / M1 — Orthogonal-classifier + resolution-matched audit of OV-seg text towers on seen classes

The target claim is not load-bearing: OV-seg papers use text towers as an open-set interface, not a seen-class booster, and the careful ones already separate seen/unseen tables. Both outcomes are nulls — collapse confirms the field's implicit assumption (the mutation's own kill condition concedes it); recovery is answered by "a new class costs one text embedding; your random-orthogonal control can't even be applied to an unseen class." Underneath, it's a Hoffer et al. (2018) control transplanted to pixel-softmax. No experiment fixes a non-load-bearing target.

## C-0014 / M2 — Budget-matched post-hoc filter equivalence audit of attention surgery

Kill on stakes: training-free CLIP segmentation is a benchmark micro-genre with no deployment surface, and NACLIP already publishes the Gaussian prior as a method — "post-hoc vs. in-attention" is a distinction reviewers will collapse. Equivalence claims need pre-registered TOST margins that underpowered per-benchmark differences will not sustain, and the mutation's own risk note concedes boundary metrics likely break the equivalence — turning the headline into "the surgery papers were right where it matters." A clean, cheap design in service of a hygiene result for a niche.

## C-0047 / M3 — Directional asymmetry in VLM spatial reasoning tracks raster serialization *(closest call)*

The frozen audit can't control text-prior and image-statistics confounds for closed-data models (and Kamath et al.'s per-relation tables may already contain the asymmetry); the causal retrain arm carries a permanent escape hatch ("scale too small") that voids its kill condition; and the lever is aging out — Qwen2-VL-class 2D RoPE and tiled encodings make raster-order locality a receding architecture cohort. The elegant cheap version (frozen LLM + projector-only retrains under raster/column/Hilbert orders on synthetic scenes) is real, but its payoff caps at a footnote for last year's architectures. Revive only if free evidence (a large, replicated asymmetry in existing per-relation benchmark tables that survives synthetic-scene controls) surfaces first.

## C-0068 / M4 — Adam-moment transplant isolates optimizer transients from update rank in forgetting

Plausibly LR hygiene in disguise: transplanted second moments shrink early effective steps, and the design's own preconditioner-mimicking LR arm *is* the transplant by another name — if those arms coincide, the finding reduces to "smaller early steps forget less," i.e., tuned warmup, which Biderman et al. already controlled for. The zone is instructed-harsh and actively mined (continual-pretraining optimizer-state work, quarterly LoRA-forgetting updates), the expected result is a mushy fraction that changes no one's method choice (LoRA is used for memory anyway), and the proposal's own kill condition is an unpublishable null. The one control that would prove a real mechanism (shuffled-transplant arm: structured ≫ permuted moments at matched global scale) still leaves a best case of revising a narrative's decomposition inside someone else's fast-moving literature.

## C-0099 / M5 — Post-hoc whitening audit across published SSL checkpoints *(easiest kill)*

The checkpoint zoo cannot support the conclusion: published checkpoints differ in data, epochs, architecture, and augmentation, so whatever spread whitening removes is unattributable to "method family" — the controlled version (matched recipes) is solo-learn's published territory, which already found small gaps. Both outcomes are dead ends (spread shrinks → probe-protocol sensitivity is known; spread survives → null), whitening estimated on transfer data is a quiet distribution leak, and SSL methods justify themselves by fine-tuning, where frozen-probe whitening is irrelevant. No experimental path leads to a decision-changing claim.

## C-0355 / M7 — Annotation-budget crossover predicted by a feature-sharing score

The crossover, if it exists, lives where nobody operates: at benchmark scales head classes sit deep in diminishing returns, so the marginal head label's value for tail performance is ≈0 outside contrived tiny-budget corners. The idea is stranded between eras — allocation economics matter for from-scratch training (rare), while the feature-sharing predictor presumes a foundation backbone that turns tail recognition into a few-shot problem and voids the question. Simulated label markets on subsampled benchmarks map to no real annotation decision, and crossover-point estimation demands an expensive run grid for a fragile quantity. The transfer science underneath is owned (OLTR, Kang et al.); the economics layer has no viable habitat.

## C-0365 / M8 — Failure-mode-matched revival: unmet classical priors predict which components help which model

A 3×4 grid cannot establish a principle — scoring ~8/12 qualitative matches by common sense (CRF helps where boundaries are bad) is near-guaranteed, with the authors grading their own rubric. The effect budget is inside evaluation noise: post-CRF-decline, classical post-processing gains on strong models are fractions of an mIoU point, so the paper predicts the sign of effects smaller than its own error bars, with implementation fairness (expert tuning of 2009-era components) as the dominant nuisance. And practice has a dominating alternative — fine-tune or distill a better decoder. Scaling the grid fixes the statistics but not the effect sizes; no realistic experiment makes small effects large.

---

## Tally

| Verdict | Count | IDs |
|---|---|---|
| SURVIVE | 7 | C-0028, C-0090, C-0128, C-0158(M6), C-0229, C-0302, C-0310 |
| KILL | 11 | C-0002(M1), C-0014(M2), C-0047(M3), C-0068(M4), C-0093, C-0099(M5), C-0276, C-0320, C-0332, C-0355(M7), C-0365(M8) |

Stage-3 KEEPs killed: 4 of 10 (C-0093, C-0276, C-0320, C-0332 — all on the analysis-only / audit-without-lever criteria).
Stage-3 MUTATEs killed: 7 of 8 (only M6/C-0158 survived — the only mutation with both a mechanism and a fix).
