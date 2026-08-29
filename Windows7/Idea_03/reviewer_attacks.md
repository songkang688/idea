# Idea_03 — Reviewer #2 Attacks and Responses

Ordered by severity. A1 was **fatal as originally specified** — the Stage-5 design could not have
survived it — and A2–A4 each had the power to make a 2,450 A100-h result uninterpretable.

---

## A1 — "Your control arm contradicts your premise." **[fatal as specified]**

> LLaVA-1.5's `llava_v1_5_mix665k` already contains a text-only ShareGPT slice (~40K conversations).
> So "reproduce the published recipe" and "`A0` = no rehearsal" cannot both be true. Your `A0` is not
> a no-rehearsal condition, and your `A1` partially duplicates what the recipe already does.

**Response — redefine the base, and say what that costs.**

The base is a **pre-registered text-stripped mix** with explicit **token-budget re-matching** across
all arms. The published-recipe run is reported once as a *reference point*, not as an arm.

Re-matching is not cosmetic. `A0` has no rehearsal stream, so to reach the same total token count it
must draw more multimodal tokens; without that, `A0` is simply the shortest run and the grid contains
a training-length confound dressed as a rehearsal effect. `src/rehearsal_grid/sampler.py` implements
this and `run_decision_demo.py` prints the check.

**What it costs:** the claim narrows from "the published recipe" to "a controlled variant of it." We
state that narrowing in §3 rather than eliding it.

---

## A2 — "Two of your four strata have unusable denominators." **[high]**

> Vicuna-7B is near-floor on GSM8K and weak on IFEval. Retention is `score/score(base)`. A ratio with
> a near-zero denominator is noise, and one unstable stratum can flip your ≥3-of-4 rule.

**Response — absolute deltas co-primary, plus a gate that runs before the arms.**

`Abs(c,a) = score − score(base)` is **co-primary** with the retention ratio everywhere. A
denominator-adequacy gate (headroom over chance ≥ 0.10, headroom/seed-σ ≥ 3) is applied at E0, and
failing strata are **replaced before the 15 arms run**.

`KNOWN FACT` The Stage-5 abort gate watched only seed variance on `A0`/`A1`. It never asked whether a
stratum could support a ratio at all. The demo shows GSM8K and IFEval failing the gate on
illustrative Vicuna-like numbers.

---

## A3 — "'If the conventions diverge, the divergence is the finding' is unfalsifiable-adjacent." **[high]**

> With no declared primary, every possible outcome becomes a result.

**Response — name the primary in advance: per-layer matching.**

`EVIDENCE` Justified rather than arbitrary: Pareto LoRA (`arXiv:2606.17296`) reports modality-specific
gradients differing by orders of magnitude across layers, so a single global scalar can report a
clean match while individual blocks stay badly mismatched. The demo reproduces exactly that — a
global scale of 3.245 leaving per-layer residuals spanning 0.24 to 3.23.

Global-norm becomes a stated **sensitivity analysis** (E3). Divergence is then a qualified finding
about convention-dependence, not a catch-all.

---

## A4 — "Your 80% rule is a ratio of differences with a small denominator." **[high]**

> `balance / total` where `total = A1 − A0` is exactly the quantity your own power analysis says
> might be small. At three seeds that ratio can swing wildly.

**Response — declare the MDE before the arms, and refuse to interpret below it.**

The minimum detectable effect is committed at E0. Below it, `decision.py` reports absolute deltas and
**declines to compute the share**. The demo quantifies the stakes: the same underlying 0.85 share
gives `0.86 [0.85, 0.87]` on a +0.130 gap and `1.18 [0.66, 1.81]` on a +0.030 gap.

Bootstrap CIs over seeds accompany every reported share.

---

## A5 — "One model family, one scale." **[medium]**

> You cannot tell the field to stop paying for curation based on LLaVA-1.5-7B alone.

**Response — fund the replication.** `A0`/`A1`/`A2` × 1 seed on `TRI-ML/prismatic-vlms` (E5, ~300
A100-h), promoted from optional into the core design.

`KNOWN FACT` This does not fully answer the attack — one more family at one more scale is not
generality — and §19 states the base-model-currency limitation directly rather than hedging it.

---

## A6 — "Robins 1995 already predicted this." **[medium, framing]**

> Pseudo-rehearsal showed content-free rehearsal works. Your positive result is 30 years old.

**Response.** Robins is small-network pseudo-rehearsal. The contribution is the multimodal,
capability-stratified, gradient-matched version — and the framing runs both ways: **if `A2` fails, we
are the first controlled refutation of the pseudo-rehearsal account in this regime.**

`KNOWN FACT` Stage 6 recorded this as a framing battle unresolvable before the data exist. We do not
pretend an experiment settles it.

---

## A7 — "This is a language-retention study in a segmentation portfolio." **[portfolio-level]**

**Response.** No experiment answers this, and we do not invent one. `EVIDENCE` It was a **deliberate
diversification decision** by the Stage-6 panel, taken over the segmentation reviewer's dissent, to
avoid a Final 3 composed entirely of inference-only diagnostics. The dissent and the reasoning are
recorded in `selection_history/`.

---

## A8 — "The mechanism space is being colonised in real time." **[scoop clock]**

> Dynamic Gradient Guidance (`arXiv:2511.15164`) already recasts forgetting as missing-gradient
> approximation. Someone will run your control soon.

**Response.** `KNOWN FACT` As of the Stage-6 sweep, no content-free-control study exists in this
setting — `A2`/`A3`/`A4` are unclaimed. But the residual window is plausibly months, and the
mitigation is execution speed, not argument. Post the pre-registration early. If scooped mid-flight,
the power analysis, the cross-family replication and the dosing recipe all survive independently.

---

## What each attack changed

| Attack | Design change |
|---|---|
| A1 | text-stripped base + token re-matching; published recipe demoted to a reference point |
| A2 | absolute deltas co-primary; denominator gate before the arms |
| A3 | per-layer named as pre-registered primary; global demoted to sensitivity |
| A4 | MDE declared before the grid; shares uninterpreted below it |
| A5 | cross-family replication promoted into the core design |
| A6 | reframed around the refutation branch |
| A7 | recorded as a portfolio decision, not defended as science |
| A8 | early pre-registration; sequencing pressure |

Five of eight are answered by pre-registration rather than by extra compute, which is the cheapest
form of defence available to a project this expensive.
