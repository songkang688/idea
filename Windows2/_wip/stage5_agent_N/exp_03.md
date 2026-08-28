# exp_03 — A-0061: topology is lost at checkpoint-selection time (vs arXiv 2601.06067 residual)

**ID:** W2-A-0061.
**Pipeline status:** F keep (counter-intuitive + cheap-falsify) → J's only bare SURVIVE → L Finding 2 + PI binding: **SURVIVE-IF-EXPERIMENT vs arXiv:2601.06067** (HyperTopo-Adapters: min-PD-within-top-K-Dice checkpoint selection already published, Jan 2026, single-author, one Kaggle leaf-lesion dataset) and arXiv:2412.14619 (metric guidance: Betti matching, no dimension aggregation). Must state the exact residual.

## Exact residual claimed (mandated)

arXiv:2601.06067 *presupposes* the phenomenon and ships a selection rule on one small 2D dataset; it does not establish that the phenomenon exists systematically. The residual is: **the systematic, multi-seed, multi-architecture, multi-benchmark quantification of Dice-vs-topology checkpoint divergence, with a selection-noise null model, on standard medical tubular benchmarks — plus the Dice-topology Pareto frontier of a single training run.** 2412.14619 supplies the measurement discipline; 2601.06067 is cited as proof of appetite, not competitor for the quantification.

## Research question

For tubular-structure segmentation (vessels, airways), how much topological quality is discarded by Dice-based checkpoint selection — systematically, beyond selection noise, across seeds, architectures, and datasets — and is it recoverable for free by topology-aware selection?

## Falsifiable hypothesis

H1: Near convergence, per-run checkpoints selected by validation Betti-matching error dominate Dice-selected checkpoints on **test** topology (Betti matching error reduced) at a Dice cost below a pre-registered ε (e.g., ≤0.5 Dice points), and this dominance exceeds a selection-on-noise null in ≥2/3 architectures × ≥2/3 datasets.
Falsified if: divergence between Dice- and topology-selected checkpoints is within the bootstrap selection-noise band — meaning topology is genuinely lost during training, which validates the topology-loss literature (TopoSculpt 2509.03938, SDF-TopoNet 2503.14523, AC2RUNet 2606.12319 — all cited by J as the field still paying training-time costs).

## Prediction

HYPOTHESIS: divergence exists and is architecture-dependent; EMA/cosine-restart schedules (J's objection) reduce but do not eliminate it. No published number exists for the multi-seed magnitude — that number is the paper.

## Method sketch

Measurement study, no new model. Modules: (1) training harness logging **all** checkpoints (or every k steps near convergence) for standard pipelines; (2) topology evaluator implementing Betti-matching error per 2412.14619 (explicitly NOT raw Betti numbers; no dimension aggregation); (3) selection simulator: Dice-select, topology-select, min-PD-within-top-K-Dice (2601.06067's rule, run as a *baseline*), oracle; (4) noise-control: bootstrap val-set subsamples → distribution of selected checkpoints under resampling → null band for "dominance"; (5) val-size/SNR sensitivity analysis (J hidden assumption 2).

## Data

2D: DRIVE-class retinal vessel benchmarks. 3D: one public airway and one public vessel benchmark (final choice at execution after a data-access check; 3D is required — vessels/airways are where a 1-voxel break destroys downstream use). 2 datasets minimum, 3 preferred.

## Baselines

Dice-selected checkpoint (standard practice), last-epoch, EMA weights (the schedule that might erase the effect — must be an explicit arm, not an objection), 2601.06067's min-PD rule, and a topology-loss-trained run (one arm, to show what training-time cost buys relative to free selection).

## Metrics

Betti-matching error (primary), broken-branch count, clDice (reported for comparability, not primary), Dice; dominance rate across runs with bootstrap CIs; "free-gain" summary: median test-topology improvement at ≤ε Dice cost.

## Killer Experiment

**3 architectures × 2 datasets × 5 seeds = 30 runs with full checkpoint logging, plus the selection simulator and noise null.** One number decides everything: the fraction of runs where topology-selection dominance exceeds the noise band. Either outcome publishes (J): dominance → free gains + field-level embarrassment; no dominance → first rigorous evidence that topology loss is a training-time phenomenon.

## GPU/VRAM/time estimate

2D runs: minutes–hours each; 3D runs: ~6–12 h each on a 24GB GPU (patch-based). Total ≈ **2–3 GPU-weeks on one GPU**, checkpoint storage ~1–2 TB (prunable to near-convergence window). No annotation cost.

## Stop / pivot / kill criteria

- **Kill** the headline if dominance is inside the noise band in ≥2/3 of settings → pivot to the negative paper ("topology is lost in training, not selection: a multi-seed audit"), which is pre-committed as publishable.
- **Pivot** if divergence exists but val-topology SNR is too low to select on (val-size analysis) → the paper becomes "the divergence is real but unexploitable without larger val sets" — a sharper, more useful claim than the fix-paper 2601.06067 shipped.
- **Stop/re-scope** if a systematic multi-benchmark version of 2601.06067 appears before execution (this-cycle window per L; freshness re-check at experiment freeze mandatory).

## Reviewer-2 leftover

"The practical payoff is a one-line fix — engineering" (J's harshest line) survives a positive result; the defense is the Pareto-frontier characterization and the noise-null methodology, which 2601.06067 lacks. Also: results may not transfer beyond tubular classes; scope claims accordingly.

## Expected result (HYPOTHESIZED, not measured)

Dominance beyond noise in most non-EMA settings; EMA arm shows reduced divergence. Magnitude unknown — no fabricated number offered.

## Negative-result interpretation

A within-noise result is the strongest possible justification for the topology-loss literature and kills a plausible "free-lunch" meme before the field adopts selection rules on noise (2601.06067's rule would then be shown to select on noise — a correction with its own value). Either way the Betti-matching selection harness is a releasable artifact.
