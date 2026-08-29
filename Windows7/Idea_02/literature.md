# Idea_02 — Literature

**Provenance tags.** `[S5-verified]` = existence-verified by the Stage-5 engineer, 2026-08-28.
`[S6-verified]` = surfaced or re-checked in the Stage-6 adversarial/defence passes, 2026-08-28.
`[S6-abstract]` = abstract only. `[inherited]` = carried from Stage-3/4 without re-verification.

> This is the most crowded lane in Windows7. The honest summary: **no fatal scoop, two fast-moving
> clocks, and a framing land-grab already in progress.**

---

## 1. The memory-policy wave — our comparators, not our competitors

`EVIDENCE` At least six published methods assert that FIFO or confidence-driven memory writes cause
error accumulation in SAM2, per `arXiv:2512.22624` and `arXiv:2606.24449` `[S6-verified]`:

| Method | Repo | Role for us |
|---|---|---|
| SAMURAI | `github.com/yangchris11/samurai` `[S5-verified]` | comparator (motion-aware memory selection, training-free) |
| DAM4SAM | `github.com/jovanavidenovic/DAM4SAM` `[S5-verified]` | comparator + **source of the DiDi dataset** |
| SAM2Long | `github.com/Mark12Ding/SAM2Long` `[S5-verified]` | comparator (training-free memory tree) |
| SAMITE | via `arXiv:2512.22624` `[S6-verified]` | candidate comparator |
| HiM2SAM | via `arXiv:2512.22624` `[S6-verified]` | candidate comparator |
| SENTRY | `arXiv:2606.24449` `[S6-verified]` | candidate comparator |
| AS-SAM2 | TCSVT 2026, code promised `[S6-verified]` | candidate, contingent on release |

**Why this list is an asset.** Stage 5 designed the validity test around two comparators. With five
or six, "reversible fraction predicts prevention gains" stops being an anecdote about two wrappers
and becomes a claim about the mechanism class — *provided* the set is frozen before any comparator
runs and the reported statistic is the minimum, not the maximum. Both conditions are in
`configs/preregistration.yaml`.

---

## 2. The framing land-grab

| Work | What it did | Our exact difference |
|---|---|---|
| **`arXiv:2512.22624`** — *Rethinking Memory Design in SAM-Based Visual Object Tracking*, Dec 2025 `[S6-verified]` | Systematically analyses SAM2-era memory mechanisms; reimplements them inside SAM3; evaluates across ten benchmarks; proposes a unified short/long-term hybrid memory; **ships a public SAM3 tracking zoo**. | A *design study*. No oracle surgery, no reversibility decomposition, no external validity test. But it occupies the "systematic memory-centric study" real estate, so our pitch must be **decomposition-first**, not "we study SAM2 memory". |
| **CL-MC** — `arXiv:2602.19380` `[S6-verified]` | Detector-triggered memory overwrite for SAM2 drift — an applied *fix* in the reset family. | Makes P2 (`targeted > reset`) load-bearing rather than decorative: a citable reset-style fix now exists, so the gap must be measured. |

`EVIDENCE` All four Stage-6 experts agreed `arXiv:2512.22624` has not run oracle surgery or a
reversibility decomposition. They disagreed on how much its existence matters — recorded honestly in
`reviewer_attacks.md` as unresolved disagreement, not resolved by assertion.

---

## 3. The field asking our question in print

Two quotations do more for the motivation section than any argument we could construct.

1. `EVIDENCE` `arXiv:2512.22624` states the subfield is **"bottlenecked by memory design"**
   `[S6-verified]`.
2. `EVIDENCE` **SAM2RL** (`arXiv:2507.08548`) `[S6-verified]` RL-overfits a per-video memory policy,
   reports **+4.91% tracking quality over SAM2** — beating SAMURAI and DAM4SAM in their setup — and
   then observes that even the overfit policy *"still fails to achieve optimal performance,
   suggesting the limit of the memory bank capacity."*

A field that has published eight policies and then writes, in print, that it does not know where the
limit is, is a field missing a denominator.

**SAM2RL is also our best hidden upside.** Its ceiling is derived by *optimisation*; ours by *oracle
timing*. Two independently derived ceilings that agree would neutralise the oracle-dependence
objection (A6) far more convincingly than the framing argument Stage 4 used, and the marginal cost is
one public repo plus a shared sequence list.

---

## 4. SAM3 and the generational question

`EVIDENCE` SAM3 released Nov 2025 (`arXiv:2511.16719`); SAM 3.1 Mar 2026 `[S6-verified]`. The SAM3
tracker **inherits the SAM2 memory-bank architecture**, and its memory policy is reported to be more
conservative.

This is simultaneously the biggest threat (A3: a SAM2.1-only paper reads as archaeology at 2026
submission time) and the biggest upside. Running the identical protocol on SAM2.1 **and** SAM3 turns
the deliverable from "SAM2 has this much memory-borne failure" into *"here is how much memory-borne
failure a model-generation change actually removed, and how much it did not."* That is a materially
larger paper, and `arXiv:2512.22624`'s released zoo makes the comparator ports cheap. It is funded
as E7, not deferred to future work.

---

## 5. Data and tooling

| Resource | Role | Note |
|---|---|---|
| `github.com/facebookresearch/sam2` `[S5-verified]` | the subject; video predictor + memory bank | fork for surgery hooks |
| LVOS v2 — `github.com/LingyiHongfd/LVOS` `[S5-verified]` | primary harvest, 140 val videos | dense GT, long-term |
| `lvos-evaluation` `[S5-verified]` | J&F scoring | |
| **DiDi** — `go.vicos.si/didi`, linked from DAM4SAM `[S5-verified]` | distractor-distilled harvest | **no mirror — confirm access day 1** |
| SA-V val | optional scale-out if yield is short | |
| SAM3 tracking zoo (via `arXiv:2512.22624`) `[S6-verified]` | E7 generational arm | HF-gated |

---

## 6. What a reviewer will cite against us

| Likely citation | The attack | Answer |
|---|---|---|
| `arXiv:2512.22624` | "Memory design in SAM trackers has been systematically studied." | Decomposition-first pitch; no prior work runs oracle surgery with a reversibility split and external validity. `reviewer_attacks.md` A3. |
| CL-MC (`arXiv:2602.19380`) | "Memory reset is already a published fix." | P2 measures exactly this gap, pre-registered at ≥10 points with a CI excluding 0. |
| SAM3 / `arXiv:2511.16719` | "You studied the previous generation." | E7 SAM3 arm, funded. |
| SAM2RL (`arXiv:2507.08548`) | "An upper bound already exists." | Different principle (optimisation vs oracle timing). Agreement between them is corroboration, and we run the cross-check. |
| Any continual-learning reviewer | "Deleting recent state is a decades-old heuristic." | That is the `reset` arm, and beating it is a pre-registered requirement. |

---

## 7. Open verification debt

1. SAMITE, HiM2SAM and AS-SAM2 are known to us **through** `arXiv:2512.22624` and
   `arXiv:2606.24449`. Before any of them enters the frozen comparator set, its primary source and
   code release must be verified directly — a comparator that cannot be run is worse than one that
   was never named.
2. `arXiv:2606.24449` (SENTRY) and `arXiv:2602.19380` (CL-MC) were read at **abstract level**.
3. The SAM2RL "+4.91%" figure is `EVIDENCE` reported by that group in their own setup. It motivates;
   it is not a number we may reuse as a baseline.
4. `KNOWN FACT` **No tracking number anywhere in this package was measured by us.**
