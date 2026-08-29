# Idea_03 — Literature

**Verification tags.** `[S5-verified]` confirmed in Stage-5 searches (2026-08-28) · `[S6-verified]`
surfaced or re-checked in Stage 6 (2026-08-28) · `[S6-abstract]` abstract read, full text not ·
`[inherited]` carried from Stage 3/4 without re-verification.

`KNOWN FACT` No number in this package was measured by us. Where a paper's reported figure appears,
it is tagged `EVIDENCE` and attributed, and it motivates rather than baselines.

---

## 1. The direct dispute we arbitrate

**`arXiv:2603.14493`** `[S6-verified]`
Argues multimodal linguistic forgetting is **overstated**, and that the operative variable is *task
diversity*, explicitly not data volume.

This is the most important entry in the file, for two opposite reasons.

- It is a **content-side claim made observationally**, with no content-free control and no gradient
  matching. Our `A2`/`A3`/`A4` arms are precisely the controls it lacks, which upgrades this project
  from "testing folklore" to "the decisive experiment for a live, named disagreement."
- It also raises our most likely failure mode. If forgetting really is small under a well-tuned
  recipe, the `A1 − A0` gap may not clear the power gate at 7B. That is why P0 exists and why it is
  evaluated before the other nine runs.

It further predicts the shape of the middle outcome — `A4 < A2 < A1` — which is the mushy P3 branch
we most expect.

---

## 2. The closest prior work (scaffold, not scoop)

**Srivastava et al., PMLR v330 / `arXiv:2410.19925` (CoLLAs)** `[S6-verified]`
Benchmarks five continual-learning methods, rehearsal among them, on LLaVA linguistic forgetting.
**Real data only** — no content-free control, no gradient matching.

We reuse its task splits and cite it as the study our grid subsumes. Its existence is net positive:
it establishes that the phenomenon is worth measuring, and that no one has yet asked *why* rehearsal
works.

---

## 3. Mechanism-side work (the scoop clock)

**Dynamic Gradient Guidance, `arXiv:2511.15164`** (Nov 2025) `[S6-verified]`
Recasts multimodal forgetting as **missing-gradient approximation** on LLaVA, and proposes a method.
Approaches "it's optimization, not data" from the *method* side; we test the same proposition
*causally*, with data ablation. Nearest thing to a competitor and the main reason the residual window
is measured in months.

**MoDE, NeurIPS 2025 / `arXiv:2512.03125`** `[S6-verified]`
Formalises **modality gradient conflict** (Def. 1). Supplies the theoretical vocabulary a positive
result would be written in. Runs no rehearsal-content experiment.

**Pareto LoRA, `arXiv:2606.17296`** `[S6-verified]`
`EVIDENCE` Reports modality-specific gradients differing "by orders of magnitude across various
layers and tasks."

This is load-bearing for a design decision, not just background: it is why **per-layer matching is
the pre-registered primary convention**. A single global-norm scalar can report a clean match while
individual transformer blocks remain badly mismatched, and the demo in `src/` reproduces that gap.

---

## 4. The framing ancestor

**Robins (1995), pseudo-rehearsal** `[inherited]`
Rehearsal on *generated*, content-free patterns mitigates catastrophic forgetting in small networks.

A reviewer will say this predicted our result. The honest response is that our `A2`–`A4` arms are the
multimodal, capability-stratified, gradient-matched version — and that if `A2` fails, we are the
first controlled refutation of the pseudo-rehearsal account in this regime. `KNOWN FACT` Stage 6
recorded this as a framing battle that cannot be resolved before the data exist.

---

## 5. Infrastructure

| Artifact | Role | Tag |
|---|---|---|
| `haotian-liu/LLaVA` | training harness; deepspeed configs shipped | `[S5-verified]` |
| `TRI-ML/prismatic-vlms` | fallback harness + cross-family replication (E5); the trainer used by the closest prior | `[S5-verified]` |
| `EleutherAI/lm-evaluation-harness` | language strata | `[S5-verified]` |
| `EvolvingLMMs-Lab/lmms-eval` | vision-language sanity strata | `[S5-verified]` |
| `allenai/c4` (ODC-BY) | `A2`/`A3`/`A4` source corpus | `[S5-verified]` |
| `llava_v1_5_mix665k` | base mix — **contains a text-only ShareGPT slice** | `[S6-verified]` |
| Vicuna-7B | base model; LLaMA-2 community licence | `[S5-verified]` |

`KNOWN FACT` The LLaVA repo is in maintenance mode; deepspeed configs need version pinning. Known
ecosystem friction — days, not weeks.

`KNOWN FACT` The ShareGPT slice inside `mix665k` is what forces the text-stripped base. It is also
the reason A1 would otherwise partially duplicate what the published recipe already does natively.

---

## 6. Verification debt — clear before submission

| Item | Status | Missing |
|---|---|---|
| `arXiv:2603.14493` | `[S6-verified]` | full-text read of the diversity analysis; its exact task-diversity operationalisation determines how directly our arms arbitrate it |
| `arXiv:2511.15164` | `[S6-verified]` | full text; check whether its evaluation already contains a de-facto content-free arm |
| Robins 1995 | `[inherited]` | primary source not re-read in Windows7 |
| ShareGPT slice size (~40K conversations) | `[S6-verified]` | exact token count must be measured at E0, since it sets every arm's budget |

## Standing rules

1. No citation enters this project that was not found in a Windows7 session and logged here.
2. `EVIDENCE`-tagged figures from other groups (e.g. Pareto LoRA's "orders of magnitude") motivate
   design choices. They are never reused as baselines or compared against our results.
3. Every number in `README.md` and the `src/` demo output is **simulated** and exists to validate the
   decision rule.
