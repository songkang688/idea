# Idea_02 — MemorySurgeon: Causal Memory Surgery as a Validated Decomposition Instrument for SAM2

**Internal ID:** A-0017 (Cluster A)
**Window:** Windows7 · **Package written:** 2026-08-29
**Status:** Ready to start. Zero training. ~80–120 GPU-h core, +~60 GPU-h for the Stage-6 mandatory arms.

> **Epistemic contract.** `KNOWN FACT` = checkable property of a public artifact. `EVIDENCE` = a
> finding reported by a cited paper. `HYPOTHESIS` / `EXPECTED` = our prediction. **No `ACTUAL
> RESULT` appears in this file.** Nothing here has been run.

---

## 1. Executive Summary

**One sentence.** When SAM2 loses an object in a long video, delete the memory entries written
after the failure began, replay, and measure how much of the failure was *memory-borne* rather than
representation-borne — then validate that this measurement predicts what independent prevention
methods actually gain.

**Abstract.** SAM2-family trackers accumulate corrupted memory after a tracking error, and the
subfield has produced roughly eight competing memory policies in two years (SAMURAI, SAM2Long,
DAM4SAM, SAMITE, HiM2SAM, SENTRY, …) with **no common yardstick for how much headroom any of them
captures**. We build that yardstick. On organic failures harvested by a fixed protocol from LVOS v2
and DiDi, we perform oracle-timed **targeted deletion** of post-error memory entries — keeping the
conditioning-frame memory and all pre-error object memories — and replay. Three things make this a
decomposition instrument rather than a repair heuristic, and all three are pre-registered: targeted
deletion must beat **full reset**, it must beat a **temporal-encoding sham**, and the per-sequence
reversible fraction must predict the per-sequence gains of independent training-free prevention
methods **after partialling out generic sequence difficulty**. The deliverable is a headroom table:
how much of remaining SAM2-family tracking failure is memory-borne, and what share each published
memory policy actually captures.

**Why it is #2 and not #1.** Highest ceiling in the round, and the highest single risk: this
subfield moves quarterly and the scoop clock is running.

---

## 2. Research Motivation

`EVIDENCE` At least six papers assert that FIFO or confidence-driven memory writes cause error
accumulation in SAM2 (SAMURAI, SAM2Long, DAM4SAM, SAMITE, HiM2SAM, SENTRY — per `arXiv:2512.22624`
and `arXiv:2606.24449`, both `[S6-verified]`). `EVIDENCE` `arXiv:2512.22624` ("Rethinking Memory
Design in SAM-Based Visual Object Tracking", Dec 2025) states in print that the field is
"bottlenecked by memory design", and ships a SAM3 tracking zoo.

`EVIDENCE` SAM2RL (`arXiv:2507.08548`) RL-overfits a *per-video* memory policy, reports +4.91%
tracking quality over SAM2 — beating SAMURAI and DAM4SAM in their setup — and then observes that
even the overfit policy "still fails to achieve optimal performance, suggesting the limit of the
memory bank capacity."

Read those together and the field is asking, in print, a question nobody has answered: **of the
performance still missing, how much is memory-borne and how much is representational?** Eight
policies compete on a leaderboard with no denominator. A policy that captures 90% of the available
memory headroom and one that captures 30% look identical if the headroom is unknown.

---

## 3. Problem Definition

Let SAM2 track object `o` through frames `1..T`, maintaining memory bank `M_t` = conditioning-frame
memory `m_0` (permanently retained) ∪ recent non-conditioning memories ∪ object pointers.

**Failure event (pre-registered protocol, zero curation).** A failure begins at frame `t_f` if
per-frame IoU falls below 0.1 for `k` consecutive annotated frames after having been ≥0.5 earlier.
`t_r` = the ground-truth *recovery-opportunity* frame (the object is annotated visible again).

**Surgery arms at `t_r`:**

| Arm | Operation | Answers |
|---|---|---|
| `no_op` | nothing | natural recovery baseline |
| `targeted` | delete entries written in `[t_f, t_r)`; keep `m_0` and all pre-`t_f` entries | the claim |
| `reset` | keep `m_0` only | is it just a restart? (H2) |
| **`sham`** | delete a **count-matched number of pre-error (uncorrupted) entries**, leaving every post-error entry in place | do the *motions* alone help? (H3) |
| **`slot_control`** | `targeted`, then refill the vacated recency slots with count-matched pre-error duplicates | once content is removed, does slot occupancy matter? |
| `random_k` | delete `k` entries at random, count-matched | does it matter *which* entries? |

> **Definition note on the sham, recorded because it departs from the Stage-6 one-liner.** Stage 6
> specified the sham as "delete post-error entries but re-insert count-matched pre-error duplicates
> at the same recency slots." Implemented literally, that arm *still removes the corrupted entries* —
> it performs the therapeutic action — so it would be expected to match `targeted` even when the
> instrument is perfectly valid, making "targeted must beat sham" unpassable by construction. The
> medical analogy settles it: a sham operation makes the incision and removes nothing. So `sham` here
> deletes the same **number** of entries while leaving the corruption in place, and the literal
> Stage-6 arm is retained separately as `slot_control`, which answers a different and also worthwhile
> question. Both run in the pilot.

> **Structural bound discovered while building the prototype (2026-08-29).** `targeted` and `reset`
> are **the same operation** whenever the failure lasted longer than the memory bank's horizon,
> because FIFO has already flushed every pre-error entry by `t_r`. Hypothesis H2 is therefore
> untestable on those failures, and the share of the corpus with `t_r − t_f` shorter than the
> capacity bounds how much of the harvest can speak to H2 at all. In the prototype run only 23 of
> 50 simulated failures retained any pre-error memory. **The real harvest must report this share
> before any H2 claim**, and the failure-duration distribution becomes a reported property of the
> corpus rather than a nuisance parameter. Correspondingly, the same limit applies to the `sham`
> arm: it can only be exactly count-matched when enough pre-error entries survive to delete.
>
> **The consequence for P2, which is sharper than it first appears.** Failures where `targeted` and
> `reset` coincide contribute an exact zero to the arm gap. Pooling them does not measure a smaller
> effect — it *dilutes a real one* by a factor set by the benchmark's failure-duration distribution,
> which is a property of the data rather than of SAM2. In the prototype, a genuine +0.130 gap on the
> H2-testable subset became +0.040 when pooled, which fails the pre-registered 0.10 bar in the very
> world where the decomposition is real. **P2 is therefore evaluated on the H2-testable subset**,
> with the pooled figure reported alongside and labelled as diluted.
>
> This also re-sizes the pilot. At 23 testable failures the subset gap carries a CI of
> [−0.130, +0.391] — adequate for P1 and P3, **not** adequate for P2. A P2 failure at pilot scale is
> therefore a signal to enlarge the H2 subset, not to kill the project; only a P3 failure kills at
> pilot scale.

**Recovery.** IoU ≥ 0.5 within `w` frames of `t_r`, sustained.

**Reversible fraction** `ρ(s)` for sequence `s` = share of its failures recovered under `targeted`
but not under `no-op`.

The problem: estimate `ρ`, establish that it is a *decomposition* (targeted > reset **and** targeted
> sham), and validate it externally (`ρ` predicts prevention-method gains after difficulty
controls).

---

## 4. Core Hypothesis

> **H1.** A large fraction of organic long-video tracking failure is reversible under oracle-timed
> targeted deletion of post-error memory entries.
>
> **H2 (decomposition).** Targeted deletion beats full reset, because pre-error memories are
> load-bearing. Without H2, "surgery" collapses into "restart the tracker".
>
> **H3 (not an artifact).** Targeted deletion beats the temporal-encoding sham, so the gain is
> attributable to the *content* of the deleted entries rather than to the recency slots freed.
>
> **H4 (validity).** The per-sequence reversible fraction predicts per-sequence J&F gains of
> independent training-free prevention methods, **after controlling for generic sequence
> difficulty**.

---

## 5. Falsifiable Prediction (pre-registered)

**P1.** `targeted` recovery rate exceeds `no-op` by ≥30 points on protocol-harvested failures.

**P2.** `targeted` beats `reset` by ≥10 points of recovery.

**P3 (added Stage 6).** `targeted` beats `sham` by ≥10 points of recovery.

**P4 (kill-shot, revised at Stage 6).** Reversible fraction predicts per-sequence J&F gains with
**partial `r > 0.4`** after partialling out no-op recovery rate, failure count, and distractor
density — and the pre-registered statistic is the **minimum partial `r` across a named comparator
set fixed before any comparator is run**, not the maximum over comparators.

**Falsification.** `targeted ≈ sham` ⇒ the instrument story collapses to memory-recency mechanics;
report and stop. `targeted ≈ reset` ⇒ the decomposition collapses to "reset works"; publish as a
bounded diagnostic post-mortem. Partial `r < 0.2` ⇒ the instrument does not measure what prevention
methods exploit; publish the pre-registered negative with the corpus and toolkit.

---

## 6. Key Insight

**The field has a numerator and no denominator.** Every memory policy reports how much it gains.
None reports how much was available to gain. An oracle-timed ceiling supplies the denominator — but
only if it is validated, which is what separates this from "resetting the tracker helps".

Three design moves carry the whole project, and two of them were forced by Stage 6:

1. **Targeted vs reset** distinguishes decomposition from restart. `EVIDENCE` This is now
   load-bearing rather than decorative: reset-style repair is being independently published (CL-MC,
   `arXiv:2602.19380`, detector-triggered memory overwrite for SAM2 drift `[S6-verified]`).
2. **The temporal-encoding sham** is the arm the original design lacked. SAM2's memory attention
   consumes recent non-conditioning frames with **recency-indexed temporal position encodings**.
   Deleting post-error entries forces pre-error entries into recency slots they never occupied
   during training, so the surgered configuration is off-distribution *independently of the content*
   of what was deleted. Without the sham, part of any targeted-vs-reset gap could be an encoding
   artifact in either direction. The random-deletion control does not isolate this.
3. **Difficulty-partialled validity.** Reversible fraction and prevention-method gains are both
   downstream of generic sequence difficulty. A raw `r > 0.6` is exactly what a shared-difficulty
   confound produces with no instrument validity at all. Partialling is not a statistical nicety
   here; it is the difference between a validated instrument and a tautology.

---

## 7. Novelty — exact difference from closest prior work

| Closest prior | What it actually did | Our exact difference |
|---|---|---|
| `arXiv:2512.22624` — Rethinking Memory Design in SAM-Based VOT, Dec 2025 `[S6-verified]` | Systematically analyses SAM2-era memory mechanisms, reimplements them inside SAM3, evaluates on ten benchmarks, proposes a hybrid short/long-term memory. **A design study.** | No oracle surgery, no reversibility decomposition, no external validity test. It occupies the "systematic memory-centric study" real estate, which is why our pitch must be decomposition-first. |
| SAMURAI, DAM4SAM, SAM2Long, SAMITE, HiM2SAM, SENTRY | Each proposes a memory *policy* and reports its gain. | We are the denominator those gains are missing. They become our comparators, not our competitors. |
| SAM2RL (`arXiv:2507.08548`) `[S6-verified]` | Per-video RL-optimised memory policy; an upper bound obtained by **optimisation**. | We obtain a ceiling by **oracle timing**. Two independently derived ceilings that agree would neutralise the oracle-dependence objection far better than any framing argument. This is upside, not overlap. |
| CL-MC (`arXiv:2602.19380`) `[S6-verified]` | Detector-triggered memory overwrite for SAM2 drift — a fix. | Makes P2 load-bearing: a citable reset-style fix now exists, so "targeted > reset" must be measured, not asserted. |

**Remaining novelty (confidence: medium-high, decaying).** `KNOWN FACT` As of the Stage-6 sweep, no
published work performs oracle-timed causal memory surgery with a reversibility decomposition and an
external predictive-validity test. **`KNOWN FACT` This is the fastest-decaying novelty in Windows7.**

---

## 8. Proposed Method

### 8.1 Failure harvesting (fixed protocol, zero curation)

Run SAM2.1 (Hiera-B+ and Hiera-L) semi-supervised VOS over LVOS v2 val (140 videos) and DiDi. Every
failure meeting the definition enters the corpus. Ambiguous-reappearance cases form a
**pre-registered stratum reported separately** — this is what kills the cherry-picking attack.

### 8.2 The surgeon

`MemorySurgeon` wraps the video predictor's inference state and exposes delete/keep/reinsert over
per-frame memory entries and object pointers. **No weights are touched.** Replay determinism is
verified before any arm is scored: the `no-op` arm must reproduce the original failure bit-for-bit,
or the harness is invalid.

### 8.3 Memory-attention analysis

Log cross-attention mass from current-frame queries to each memory entry, before and after surgery.
This distinguishes two irreversibility mechanisms: **interference** (conditioning-frame attention
collapses) vs **competition** (it persists but is outvoted by a locked distractor).

### 8.4 Predictive validity

Run the comparator set on the same sequences and regress their per-sequence J&F gains on `ρ`,
controlling for no-op recovery, failure count and distractor density. The comparator set is **named
and frozen before any comparator runs**, and the reported statistic is the **minimum** partial `r`
across it.

---

## 9. Architecture Diagram

See `diagrams/architecture.md`. Inline summary:

```
video ──► SAM2.1 VOS ──► per-frame IoU ──► failure detector (IoU<0.1 for k frames after ≥0.5)
                                             │
                              t_f ───────────┴──────────── t_r (GT recovery opportunity)
                                                            │
                        ┌───────────────────────────────────┼───────────────────────────┐
                     no-op          targeted            reset            sham        random-k
                        │        (drop [t_f,t_r))    (keep m_0 only)  (drop + refill    │
                        │         keep m_0 + pre       recency slots)                   │
                        └───────────────► replay from t_r ◄────────────────────────────┘
                                                │
                        recovery rate ──► ρ per sequence ──► partial-r vs comparator gains
```

---

## 10. Mathematical Formulation

No loss. The estimands:

**Recovery indicator** for failure `i` under arm `a`:
`R_a(i) = 1[ IoU ≥ 0.5 within w frames of t_r, sustained ]`

**Arm recovery rate:** `π_a = (1/N) Σ_i R_a(i)`, bootstrap CI over failures.

**Reversible fraction** for sequence `s`:
```
ρ(s) = |{i ∈ s : R_targeted(i) = 1 ∧ R_no-op(i) = 0}| / |{i ∈ s}|
```

**Decomposition tests:** `π_targeted − π_reset ≥ 0.10` and `π_targeted − π_sham ≥ 0.10`, both with
bootstrap CIs excluding 0.

**Predictive validity (the revision that matters).** For comparator `c` with per-sequence gain
`g_c(s)` and difficulty covariates `X(s) = [no-op recovery, failure count, distractor density]`:

```
r_partial(c) = corr( ρ − ρ̂(X) ,  g_c − ĝ_c(X) )       where ·̂(X) are OLS fits on X
```

Pre-registered pass condition:
```
min_{c ∈ C_frozen} r_partial(c) > 0.4
```

`C_frozen` is named before any comparator runs. Using the minimum rather than "SAMURAI *and*
DAM4SAM at r > 0.6" removes the post-hoc comparator-selection freedom that Stage 6 flagged; with
five or six comparators available it also converts the claim from an anecdote about two wrappers
into a claim about the mechanism class.

**Nested-model check** reported alongside: does adding `ρ` to a model of `g_c` on `X` alone
significantly improve fit?

---

## 11. Implementation

`src/` contains a runnable prototype of the core innovation: the memory-bank abstraction, all five
surgery arms including the sham, the replay-determinism check, and the difficulty-partialled
validity statistics — driven by a simulated tracker so the entire decision pipeline executes with no
GPU and no checkpoints.

```
src/
  memory_surgery/
    __init__.py
    bank.py        # MemoryBank: entries, recency slots, conditioning frame, object pointers
    surgeon.py     # the five arms; recency re-indexing made explicit (that is the sham's target)
    harvest.py     # failure-event detection from an IoU trace, per the fixed protocol
    replay.py      # replay harness + determinism check
    validity.py    # partial correlation, min-over-comparators rule, nested-model comparison
    simulate.py    # a toy memory-driven tracker with controllable memory-borne failure share
  run_pilot.py     # the 50-failure pilot decision rule (section 17), end to end
```

**Real run:** fork `facebookresearch/sam2`, implement the same operations over the video predictor's
inference-state memory dict. `KNOWN FACT` Stage 5 estimated ~300 LOC for the hooks; Stage 6 noted the
sham arm adds modest extra engineering for recency re-indexing.

### 11.1 Reusable public codebases (all existence-verified Stage 5, 2026-08-28)

| Repo | Role |
|---|---|
| `github.com/facebookresearch/sam2` | video predictor, memory bank |
| `github.com/yangchris11/samurai` | comparator — motion-aware memory selection, training-free |
| `github.com/jovanavidenovic/DAM4SAM` | comparator + **DiDi dataset** |
| `github.com/Mark12Ding/SAM2Long` | comparator — training-free memory tree |
| `github.com/LingyiHongfd/LVOS` + `lvos-evaluation` | data + J&F scoring |
| SAM3 tracking zoo (via `arXiv:2512.22624`) `[S6-verified]` | generational arm |

---

## 12. Dataset Plan

| Dataset | Role | Note |
|---|---|---|
| LVOS v2 val (140 videos) | primary harvest | dense GT, long-term, public |
| DiDi | distractor-distilled harvest | `go.vicos.si/didi`, linked from DAM4SAM. **No mirror — confirm access day 1** |
| SA-V val | optional scale-out | if yield is short |
| **one medical video set** | MED dissent (§21 D2) | echo / endoscopy / surgical-tool tracking |

**Preprocessing.** Standard SAM2 VOS protocol; LVOS uses the
`--track_object_appearing_later_in_video` convention. GT reappearance frames come from dense
annotations.

---

## 13. Baselines

`no-op` (natural recovery) · `reset` (the "decades-old heuristic" arm) · **`sham`** (temporal-encoding
control) · `random-k` (count-matched, tests *which* entries matter) · SAMURAI / DAM4SAM / SAM2Long
and further training-free wrappers as **comparators for validity, not competitors**.

---

## 14. Metrics

Recovery rate per arm; time-to-recovery; post-recovery J&F (lvos-evaluation toolkit); per-sequence
reversible fraction `ρ`; **partial** `r` (Pearson + Spearman, bootstrap CIs, minimum over the frozen
comparator set); attention-mass shift pre/post surgery; headroom table (share of the oracle-timed
ceiling each prevention method captures). Everything stratified by the ambiguity stratum.

---

## 15. Experimental Matrix

| # | Experiment | Cost | Decides |
|---|---|---|---|
| E0 | DiDi access + replay-determinism check | ~2 GPU-h | feasibility |
| E1 | Failure harvest, LVOS v2 + DiDi, both backbones | ~12 GPU-h | corpus yield |
| **E2** | **Pilot: 50 failures × 5 arms** | ~10 GPU-h | **go/no-go** |
| E3 | Full surgery: ≥200 failures × 5 arms | ~25 GPU-h | P1, P2, P3 |
| E4 | Comparator passes (frozen set) | ~35 GPU-h | P4 |
| E5 | Memory-attention logging | +20% | failure taxonomy |
| E6 | Deletion-scope + timing dose–response `t_r ± δ` | ~15 GPU-h | oracle-strength sensitivity |
| E7 | SAM3 generational arm | ~30 GPU-h | significance / A3 |
| E8 | Medical-video arm | ~10 GPU-h | portfolio fit (D2) |

**Core ≈80–120 GPU-h; with the Stage-6 mandatory arms ≈140–180 GPU-h.** Zero training. 1× A100-40GB,
peak VRAM ≈16–24 GB.

---

## 16. Ablation Plan

- **Deletion scope:** all post-error vs recent-`k` vs object-pointers-only vs spatial-features-only.
- **Surgery timing `t_r ± δ`** — *promoted from ablation to a main result* (§21 D4): it shows how the
  ceiling degrades as the oracle weakens, which is the honest answer to "no deployment has an oracle".
- Recovery window `w`; failure definition sweep (IoU < 0.1 vs < 0.3; `k`).
- Backbone size (Hiera-B+ vs Hiera-L); SAM2 vs SAM2.1 checkpoints.
- With / without the ambiguous-reappearance stratum.

---

## 17. Killer Experiment

> **Two-part pre-registered shot on ≥200 organic failures.**
>
> **(1) Four-arm surgery.** `targeted` must beat `no-op` by ≥30 points, `reset` by ≥10 points, **and
> `sham` by ≥10 points.**
>
> **(2) Difficulty-partialled predictive validity.** `min_{c ∈ C_frozen} r_partial(c) > 0.4` after
> partialling out no-op recovery, failure count and distractor density, with the comparator set named
> before any comparator runs.
>
> Either miss kills the instrument claim. Both passing makes it the reference diagnostic for the
> SAM2-memory subfield. **≈60 GPU-h.**

**Pilot gate first (E2, ~10 GPU-h, 50 failures).** All five arms plus the partialled regression at
pilot scale. `targeted ≈ sham` ⇒ **stop**, the instrument story is dead and the honest report is
recency mechanics. `targeted − reset < 3 points` **and** pilot partial `r < 0.2` ⇒ stop before the
comparator passes; release corpus and tooling as a tech note.

---

## 18. Expected Results

**All `EXPECTED` / `HYPOTHESIZED`. Nothing measured.**

| Quantity | Expected |
|---|---|
| Reversible fraction | 40–70% |
| `targeted − reset` | ≥10 points |
| `targeted − sham` | **unknown — this is the arm we are least able to predict, which is why it exists** |
| Partial `r` (min over comparators) | 0.4–0.6 (note: *lower* than Stage 5's raw `r ≥ 0.6–0.75`, because partialling removes the shared-difficulty component) |
| Prevention methods' share of the ceiling | 50–80% |

`HYPOTHESIS` The most likely way this project ends badly is not P1 or P2 — it is P3. If the
targeted-vs-reset gap turns out to be substantially a recency-slot artifact, the sham arm will say
so, and it will say so at pilot scale for ~10 GPU-h.

---

## 19. Failure Cases

- **Harvest yield short.** LVOS v2 (140 videos) + DiDi may not yield 200 *usable* organic failures
  with GT reappearance frames; the ambiguous stratum could dominate. Mitigation: SA-V val scale-out;
  yield is reported before any claim.
- **H2-testable yield is a second, tighter budget.** Only failures shorter than the memory horizon
  can distinguish `targeted` from `reset` (§3). If most organic failures outlast the bank, the
  corpus supports P1 and P3 but not P2, and the paper must say so rather than pooling. Reported as a
  corpus property at E1, before any arm is scored.
- **Replay non-determinism.** SAM2's video predictor caches must be handled carefully or the `no-op`
  arm will not reproduce the original failure. E0 gates on this.
- **DiDi access.** Academic distribution at `go.vicos.si`, no mirror.
- **Failure-definition sensitivity.** The `(IoU threshold, k)` pair determines the entire corpus.
  Swept, and the corpus is released.

---

## 20. Negative Results

| Outcome | What we publish |
|---|---|
| `targeted ≈ sham` | The gap is recency mechanics, not memory content. Instrument story dead; report honestly with the toolkit. Cheapest possible ending (~10 GPU-h). |
| `targeted ≈ reset` | Decomposition collapses to "reset works"; still bounds the memory-borne share. Diagnostic post-mortem. |
| partial `r < 0.2` | The instrument does not measure what prevention methods exploit. Pre-registered negative + harvested corpus + surgery toolkit, both reusable. |
| high `no-op` recovery | SAM2.1's natural recovery is underrated — a benchmark finding in its own right. |

---

## 21. Reviewer #2 Attack

| # | Attack | Severity |
|---|---|---|
| **A1** | *"P3 passes for a trivial reason."* Reversible fraction and prevention gains are both downstream of sequence difficulty. Raw `r > 0.6` is what a shared-difficulty confound produces with **no instrument validity at all**. | **Fatal as originally specified** |
| **A2** | *"Targeted deletion is not the clean intervention you think."* Recency-indexed temporal position encodings mean surgered configurations are off-distribution regardless of content. | High |
| **A3** | *"SAM3 shipped — this is archaeology."* SAM3 (Nov 2025) inherits the SAM2 memory architecture; `arXiv:2512.22624` already restudies memory inside SAM3 with a public zoo. | High |
| **A4** | *"Surgery is a decades-old reset heuristic."* Now backed by a citable fix paper (CL-MC). | Medium |
| **A5** | *"Cherry-picked failures."* | Medium |
| **A6** | *"An oracle-timed ceiling is decision-irrelevant — no deployment has the oracle."* | Medium, partly unresolvable |
| **D1** | *(expert disagreement)* Is a SAM2.1-only paper viable, or must SAM3 be core? | Unresolved at Stage 6 |
| **D2** | *(expert disagreement)* Every dataset is natural video, in a portfolio with a declared medical axis. | Recorded as a design condition |

---

## 22. Response Strategy

| # | Response | Where |
|---|---|---|
| **A1** | **Redefine the pass condition.** Partial `r > 0.4` after partialling out no-op recovery, failure count and distractor density; statistic is the **minimum over a frozen comparator set**, not the max; nested-model comparison reported alongside. This is the single most important change Stage 6 forced. | §10, E4 |
| **A2** | **Add the temporal-encoding sham arm** — delete post-error entries, re-insert count-matched pre-error duplicates into the same recency slots. It bounds the encoding artifact directly, and it runs at pilot scale for ~10 GPU-h. | §3, E2, E3 |
| **A3** | **Add the SAM3 generational arm (E7).** This converts the deliverable from "SAM2 has this much memory-borne failure" into "here is how much a model-generation change actually removed, and how much it did not" — a materially larger paper. `EVIDENCE` The `arXiv:2512.22624` SAM3 tracking zoo makes the comparator ports cheap. | E7 |
| **A4** | P2 is exactly this test, and it is pre-registered at ≥10 points with a CI excluding 0. | E3 |
| **A5** | Fixed harvest protocol, zero curation, **all** failures enter, ambiguous stratum pre-registered and reported separately, corpus released. | E1 |
| **A6** | **Promote the `t_r ± δ` dose–response from ablation to a main result** so the reader sees how the ceiling degrades as the oracle weakens. Plus cross-validate against SAM2RL's independently-derived optimisation ceiling: two ceilings from different principles agreeing is worth more than any framing argument. | §16, E6 |
| **D1** | Resolved in favour of including SAM3 as a **funded arm (E7)**, not a promise. | E7 |
| **D2** | Add **one medical-video arm (E8, ~10 GPU-h)**. Cheap, and it is where SAM2 memory failure is clinically load-bearing. | E8 |

---

## 23. Compute Plan

`KNOWN FACT` Zero training, zero annotation, 1× A100-40GB, peak VRAM ≈16–24 GB.

| Item | GPU-h |
|---|---|
| Harvest (≈320 videos, Hiera-L) | ~12 |
| Surgery replays (≥200 failures × 5 arms, partial) | ~25 |
| Comparator passes (frozen set) | ~35 |
| Attention logging | +20% |
| **Core subtotal** | **~80–120** |
| SAM3 arm (E7) | ~30 |
| Medical arm (E8) | ~10 |
| Timing dose–response (E6) | ~15 |
| **Total with mandatory arms** | **~140–180** |

---

## 24. Implementation Roadmap

**Day 1.** Confirm DiDi access (no mirror — this is a hard dependency). Clone sam2, samurai,
DAM4SAM, SAM2Long, lvos-evaluation. Request SAM3 zoo access.

**Day 2–3.** `MemorySurgeon` hooks over the inference-state memory dict. **Replay-determinism check
(E0): the `no-op` arm must reproduce the original failure bit-for-bit.** Nothing else runs until it
does.

**Week 1.** E1 harvest; report yield and the ambiguous-stratum share. Freeze the comparator set `C`
in the pre-registration **before** any comparator runs. Then E2, the 50-failure five-arm pilot with
the partialled regression.

**Week 2.** E3 full surgery; E5 attention logging; E6 timing dose–response.

**Week 3.** E4 comparator passes; the headroom table; E8 medical arm.

**Week 4.** E7 SAM3 generational arm; corpus + toolkit release; paper draft.

**Pre-registration and early protocol release are scheduled deliberately early** — they are the only
real defence against the scoop clock (§25).

---

## 25. Stop / Continue Criteria

| Condition | Action |
|---|---|
| Replay non-deterministic and unfixable | **kill** at E0 |
| Harvest yields <80 usable failures even with SA-V | descope to a bounded pilot report |
| `targeted ≈ sham` at pilot | **kill the instrument claim**; publish recency-mechanics note |
| `targeted − reset < 3 pts` **and** pilot partial `r < 0.2` | **stop before comparator passes**; release corpus + tooling |
| Scooped mid-flight | the harvested corpus, the surgery toolkit and the validity methodology remain publishable; pivot to those |
| Everything passes | headroom table becomes the subfield's reference artifact |

`KNOWN FACT` **This project's value decays with the calendar.** It should be sequenced first among
the three if only one can start immediately.

---

## 26. Possible Extensions

- **Generational headroom law.** Run the identical protocol across SAM2.1 → SAM3 → whatever is next;
  the deliverable becomes a law about what generation changes remove.
- **Two-ceiling cross-validation** with SAM2RL's optimisation-derived bound.
- **Medical video as the main venue** if E8 shows a larger memory-borne share than natural video —
  clinically load-bearing and less crowded.
- **Non-oracle approximation.** Replace the oracle `t_r` with a learned detector and measure how much
  of the ceiling a deployable system could reach. That is the natural follow-up paper.

---

## 27. Paper Story

> Eight memory policies compete to fix SAM2's tracking failures, and none of them can say how much
> there was to fix. We supply the denominator. On organic failures harvested by a fixed protocol, we
> delete post-error memory entries and replay — and we validate that the resulting reversible
> fraction is a real measurement, not a restart, by beating a full reset, beating a recency-matched
> sham, and predicting the per-sequence gains of independent prevention methods after difficulty is
> partialled out. The result is a headroom table: how much of remaining failure is memory-borne, and
> what share each published policy actually captures.

---

## 28. Candidate Titles

1. *How Much of SAM2's Tracking Failure Is Memory? A Validated Causal Decomposition*
2. *Memory Surgery: An Oracle-Timed Ceiling for SAM-Family Video Object Segmentation*
3. *The Missing Denominator: Measuring Headroom for Memory Policies in SAM2*
4. *Reversible and Irreversible Failure in Promptable Video Segmentation*
5. *Deleting the Past: Targeted Memory Deletion as a Decomposition Instrument, Not a Reset*

---

## Provenance

Windows7 Stage 1–6 artifacts on `songkang688/idea`: `cursor/stage1-cluster-a-ideas-e2b2` →
`cursor/stage2-cluster-a-scoring-0234` → `cursor/stage3-cluster-a-priorwork-b0e5` →
`cursor/stage4-cluster-a-reviewer2-f1fa` → `cursor/stage5-cluster-a-engineering-ed30` →
`cursor/stage6-attack-pass-top5-cca8` / `cursor/stage6-defense-top5-2995` /
`cursor/stage6-meta-review-final3-4fc5`.

Stage-6 changed this design more than any other in the round. The PIVOT verdict is honoured here:
partialled validity with a min-over-comparators rule (A1), the sham arm (A2), the SAM3 arm (A3), the
timing dose–response promoted to a main result (A6), and the medical arm (D2) are all **funded**, not
promised.
