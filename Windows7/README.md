# Windows7 — Research Idea Evolution

**Created:** 2026-08-29 · **Branch of record:** `main` · **Predecessor on `main`:** `Windows1`

> `KNOWN FACT` `main` currently contains only `Windows1`. Branches exist for other Windows numbers
> but were never merged into `main`. `Windows7` is created per explicit instruction, is a fresh
> directory, and overwrites nothing.

---

## The three final ideas

| # | Codename | ID | One sentence | Cost |
|---|---|---|---|---|
| **01** | **SupportAudit** | B-0121 | Feed few-shot segmentation methods the *wrong* support image and measure how much accuracy survives. | **~5 GPU-h** |
| 02 | MemorySurgeon | A-0017 | Delete SAM2's corrupted memory entries mid-failure and measure how much tracking failure is memory-borne rather than perception-borne. | ~140–180 GPU-h |
| 03 | RehearsalGrid | C-0090 | Destroy the *content* of rehearsal text while matching its gradient scale, and find out whether rehearsal curation buys anything. | ~2,450 A100-h |

All three are **measurement projects**. None proposes a new module, and that is deliberate: each one
tests a load-bearing assumption the field currently acts on without evidence.

---

## #1 recommendation: **Idea_01, SupportAudit**

**Run it first, and run it this week.**

The recommendation is not about which idea is most interesting — Idea_02 probably is. It is about
cost-per-decision, and the gap is not close:

| | Killer experiment | What a negative result costs |
|---|---|---|
| **Idea_01** | **~5 GPU-h** | five hours |
| Idea_02 | ~60 GPU-h behind a ~22 GPU-h gate | a week |
| Idea_03 | ~900 A100-h behind an ~800 A100-h gate | most of a month |

Three further reasons:

1. **Every outcome is publishable, and they are different papers.** High retention indicts the
   benchmarks. Low retention certifies them and validates a new statistic. A split between strata is
   benchmark degeneracy, measured. The audit's object of study is the *evaluation*, so there is no
   branch where the result is "nothing happened."
2. **It has no external dependencies that can block day 1.** Public checkpoints, public benchmarks,
   no gated data, no access request. Idea_02 has a hard dependency on DiDi with no mirror; Idea_03
   needs an 8×A100 allocation that can absorb 800 hours before a go/no-go.
3. **The prototype already caught a design error.** Building the harness showed that the
   pre-registered statistic — median of per-episode retention ratios — was the wrong estimator,
   because per-episode retention is bimodal. The support-driven control scored a median of 1.000
   (indistinguishable from a support-blind method) while its ratio of means was 0.714. Had that gone
   unnoticed, the killer experiment would have been unable to detect the effect it exists to detect.
(The current harness run gives a ratio of means of 0.762 against a median of 1.000.)

**The first experiment to run:** E1 in `Idea_01/experiments.md` — the two-method, one-benchmark,
distractor-present-stratum wrong-support pass. About 5 GPU-h, and it decides whether the full audit
is worth building.

---

## Status

| | Idea_01 | Idea_02 | Idea_03 |
|---|---|---|---|
| 28-section proposal | ✅ | ✅ | ✅ |
| Runnable prototype | ✅ `run_mve.py` | ✅ `run_pilot.py` | ✅ `run_decision_demo.py` |
| Prototype exercised end to end | ✅ | ✅ | ✅ |
| Architecture diagrams | ✅ | ✅ | ✅ |
| Pre-registration frozen | ✅ committed | ✅ committed | ✅ committed |
| Literature verified & debt logged | ✅ | ✅ | ✅ |
| Reviewer #2 attacks + responses | ✅ 8 | ✅ 6 | ✅ 8 |
| External access confirmed | ❌ not yet | ❌ **DiDi is a hard blocker** | ❌ not yet |
| Any real experiment run | **❌ no** | **❌ no** | **❌ no** |

**Every number in this directory is either cited from a published paper (`EVIDENCE`) or produced by a
synthetic prototype (`SIMULATED`). Nothing here was measured on a real model or a real benchmark.**
The prototypes exist to validate decision rules before compute is spent, and they are labelled as
such in every file that reports their output.

---

## What building the prototypes changed

This is the part that would not exist if the packages had been written without running anything.

**Idea_01 — the primary statistic was wrong.** Per-episode retention is bimodal: under a wrong
support, a method either lands on the right object or it does not, so the ratio piles up near 0 and
near 1. A median over that distribution is a coin flip on which pile is larger. Switched to ratio of
means, with the median retained as a secondary robust statistic and a flag when the two disagree —
because a bimodal split is itself a finding about the method's failure mode.

**Idea_02 — the sham arm was specified backwards.** Stage 6 asked for "delete post-error entries but
re-insert count-matched pre-error duplicates." Implemented literally, that arm *still removes the
corruption*, so it performs the therapeutic action and would match `targeted` even when the
instrument is perfectly valid. A sham operation makes the incision and removes nothing. The vacuous
version is now `sham`; the literal version survives as `slot_control`, answering a different
question.

**Idea_02 — H2 is structurally untestable on long failures, and pooling them is worse than useless.**
`targeted` and `reset` are the *same operation* once FIFO has flushed every pre-error entry, which
happens whenever the failure outlasts the memory horizon. Those failures contribute an exact zero to
the arm gap, so including them does not measure a smaller effect — it dilutes a real one. Only 23 of
50 simulated failures were testable, and pooling turned a genuine +0.130 gap into +0.040, which would
have failed the pre-registered bar in the world where the decomposition is real. P2 is now read on
the testable subset, with the pooled figure reported and labelled diluted.

**Idea_03 — the control arm contradicted the premise.** LLaVA-1.5's published mix already contains a
text-only ShareGPT slice, so "reproduce the published recipe" and "`A0` = no rehearsal" cannot both
hold. The base is now a pre-registered text-stripped mix with token-budget re-matching, and the
published-recipe run is a reference point rather than an arm. This narrows the claim, and the
proposal says so.

---

## Directory

```
Windows7/
├── README.md                  ← you are here
├── research_summary.md        the round in one document
├── selection_history/
│   ├── evolution_summary.md   1110 → 255 → 52 → 21 → 5 → 3
│   ├── reviewer_summary.md    what the reviewers actually changed
│   └── eliminated_ideas_summary.md   what died, and why it might come back
├── Idea_01/  SupportAudit    (B-0121)
├── Idea_02/  MemorySurgeon   (A-0017)
└── Idea_03/  RehearsalGrid   (C-0090)
```

Each idea directory carries `README.md`, `proposal.md` (28 sections), `literature.md`,
`experiments.md`, `reviewer_attacks.md`, `roadmap.md`, `diagrams/`, `src/`, `configs/`, `references/`.

---

## Next actions, in order

1. **Run Idea_01 E1** (~5 GPU-h). It is the cheapest decision available and it gates everything else
   in that project.
2. **Request DiDi access for Idea_02 today.** It is a hard dependency with no mirror, and the request
   has lead time regardless of when the project starts.
3. **Request SAM3 tracking-zoo access** (gated, slow) even though Idea_02's E7 does not run for weeks.
4. **Do not start Idea_03** until an allocation is confirmed that can absorb 800 A100-h before a
   go/no-go.

---

## Unresolved risks

- **Idea_02 has the fastest-decaying novelty in this round.** Memory-policy work on SAM2 is an active
  area, and the mitigation is execution speed plus early public pre-registration, not argument.
- **Idea_02's DiDi dependency has no fallback.** Losing it means descoping to LVOS v2 + SA-V and
  reporting the distractor-density gap honestly.
- **Idea_03 will most likely end at its power gate.** `arXiv:2603.14493` argues multimodal linguistic
  forgetting is overstated; if it is right, the effect may not clear 2× seed σ at 7B. That ending is
  priced in and costs under 1,000 A100-h.
- **Idea_03's portfolio fit is contested.** It is a language-retention study in a mostly-segmentation
  round. `EVIDENCE` The Stage-6 panel included it as a deliberate diversification decision over the
  segmentation reviewer's dissent; no experiment settles that disagreement, and it is recorded in
  `selection_history/reviewer_summary.md` rather than smoothed over.
- **All three packages carry literature-verification debt**, logged per idea in `references/`. Some
  sources are known only through secondary citation and must be read directly before submission.
