# exp_01 — B-0114: VPT-as-registers, H's 4-arm dense-task mechanism redesign

**ID:** W2-B-0114 (ONLY the 4-arm dense-task form per `PI_BINDING.md`; the original "afternoon frozen-token pilot" is struck — VPT's own Fig. 11 Prompt-Fixed ablation already ran it on classification, EVIDENCE per L audit Finding 1, arXiv:2203.12119).
**Pipeline status:** E bet #1 → G LOCK (mission-protected) → H SURVIVE-IF-EXPERIMENT (4-arm form only) → L demotion of naive form → PI binding: 4-arm dense-task redesign or drop.

## Research question

On **dense prediction tasks**, is part of VPT's gain over linear probing produced by *register function* (prompt tokens absorbing global aggregation / acting as attention biases) rather than by *learned task content* — and does this mechanism predict that VPT gains shrink on register-equipped backbones?

## Falsifiable hypothesis

H1: On register-free ViT backbones and dense tasks, the attention-bias-only arm (no token, test-time-register-style bias injection) reproduces a statistically non-zero fraction of VPT's gain over linear probing, and VPT-trained tokens develop register signatures (classified by the NOP-vs-broadcast diagnostics of arXiv:2606.08105).
H2 (directional, pre-registered): gain(VPT | register-free backbone) > gain(VPT | register-equipped sibling) on dense tasks, at matched trainable parameters.

Falsified if: on register-free backbones, arms (b) frozen-random and (c) attention-bias each reproduce ≈0% of VPT's dense-task gain (all gain is learned content — the dense-task analogue of VPT Fig. 11), AND the register-free vs register-equipped gain difference is within seed noise.

## Prediction

HYPOTHESIS (not measured): dense tasks behave differently from the classification setting where Prompt-Fixed ≈ Linear (KNOWN, VPT Fig. 11), because register artifacts corrupt *spatial* feature maps (KNOWN, Darcet et al. arXiv:2309.16588); we predict a non-trivial register component on dense tasks and a measurable H2 gap. DA-VPT's observation of register-style artifacts in VPT prompt attention (EVIDENCE, arXiv:2505.23694, surfaced by H) makes the mechanism plausible but unquantified.

## Method sketch (modules / dataflow)

1. **Token-injection wrapper** around a frozen ViT: inserts K tokens at chosen depths (VPT-shallow and VPT-deep variants), token params either trainable (arm a) or frozen-random (arm b).
2. **Attention-bias module** (arm c): per-layer additive bias on attention logits mimicking a register's sink function, no token appended — implementation per the test-time-registers construction (KNOWN, arXiv:2506.08010).
3. **Dense heads:** linear probe + light decoder (both reported) trained per arm; backbone always frozen so the decomposition is head-independent.
4. **Signature analyzer:** token-norm distributions, attention-sink mass, and NOP-vs-broadcast classification (arXiv:2606.08105) on learned vs frozen tokens.
5. **Token-count sweep** (K ∈ {1, 4, 16, 64}) to separate register absorption from generic softmax-denominator/temperature effects (H's confound).

Dataflow: image → frozen backbone (+arm-specific injection) → dense head → task metric; token/attention stats logged per layer.

## Data

ADE20K semantic segmentation, Cityscapes segmentation, NYUv2 depth (3 dense tasks); VTAB-style classification triplet as the *control* where we expect to reproduce the published Prompt-Fixed ≈ Linear result (a built-in sanity anchor). Backbone pairs: DINOv2 vs DINOv2-with-registers (census-confirmed available per G), plus one supervised ViT.

## Baselines

Arm (d) no-token linear probe / decoder; arm (b) frozen-random tokens; arm (c) attention-bias-only; published VPT numbers as external anchors. Mandatory citation set up front: VPT (2203.12119), Darcet (2309.16588), DA-VPT (2505.23694), test-time registers (2506.08010), Do-All-ViTs-Need-Registers (2603.25803).

## Metrics

mIoU / RMSE (depth) deltas over arm (d), with 3-seed mean±sd; gain-decomposition table: learned = a−max(b,c); register/bias = c−d; insertion = b−d. Signature metrics: high-norm token fraction, attention-sink mass, NOP/broadcast class shares.

## Killer Experiment

**One dense task (ADE20K), ViT-B backbone pair (DINOv2 / DINOv2-reg), 4 arms × 2 backbones × 3 seeds = 24 cheap runs** (only prompts + head trainable). Read out: the decomposition table plus the H2 directional test. Every cell of the outcome table is interpretable (per H): all-learned → mechanism dies honestly; substantial bias arm → register mechanism confirmed and the attention-bias arm doubles as a *register retrofit recipe* (the constructive reading L asked for).

## GPU/VRAM/time estimate

Killer: 24 runs × ~6–10 h on one A100-40GB (fits in 24GB at ViT-B with frozen backbone) ≈ **1–1.5 GPU-weeks**. Full study (3 dense + 3 classification tasks, token sweep, VPT-shallow/deep): **4–6 GPU-weeks**. No annotation cost.

## Stop / pivot / kill criteria

- **Kill** the mechanism claim if arms (b) and (c) each reproduce <5% of VPT's dense gain on register-free backbones across seeds AND H2 gap < 2× seed sd — write the negative note (merged into exp_02's paper, see dissociation plan there).
- **Pivot** to the retrofit-recipe framing if arm (c) ≥ 50% of VPT gain: the paper becomes "attention-bias injection is a training-free VPT substitute on dense tasks".
- **Stop** the classification arms early if the control fails to reproduce Prompt-Fixed ≈ Linear (implementation bug detector).

## Reviewer-2 leftover

The softmax-denominator confound survives partially even with arm (c) — token insertion changes normalization in a way bias injection does not exactly match; the token-count sweep bounds but does not eliminate it. Obsolescence: register-equipped backbones becoming default (H, L both flag) makes the register-free result historical; the H2 arm is the insurance. PH-Reg's low-norm artifacts (arXiv:2505.21501) mean norm signatures alone cannot define register function — hence the NOP/broadcast diagnostics are mandatory, not optional.

## Expected result (HYPOTHESIZED, not measured)

Decomposition on ADE20K/register-free: learned component dominant, bias arm reproducing a minority-but-nonzero share of the gain; H2 gap positive and outside seed noise. On classification controls: bias/frozen arms ≈ 0, reproducing print.

## Negative-result interpretation

If dense tasks also show ≈0 register component, the VPT-register connection is cosmetic everywhere — this *completes* VPT Fig. 11's classification-only ablation and definitively closes the DA-VPT-opened question. Publishable only as a short analysis note or as the mechanism half of a merged registers paper with exp_02; it would also retire B-0001's motivation link, so the two experiments should be co-scheduled (see exp_02 §Dissociation).
