# Windows7 — Research Summary

**2026-08-29** · 1,110 raw ideas → 3 executable research packages.

---

## The shape of the round

The Final 3 are **one evaluation-validity audit, one causal-mechanism tool with a mandatory method
arm, and one training-mechanism test**. That composition was not the plan; it is what survived, plus
one deliberate correction.

Every "new architecture" idea that entered Stage 3 died there or at Stage 4, for the same reason each
time: the closest prior work had already done the thing, or Reviewer #2 could name a confound that no
affordable experiment could remove. `KNOWN FACT` The Stage-6 audit recorded this as an **extinction,
not a close call** — no METHOD-genre paper reached nominee grade anywhere in the funnel — and
responded by making Idea_02's method arm a required deliverable rather than an optional extension.
It also recommended re-instructing the Stage-1 generators next window so this does not repeat.

What the three share is that each attacks a *load-bearing assumption the field currently acts on
without evidence*:

| Idea | The assumption it attacks |
|---|---|
| **SupportAudit** | that few-shot segmentation benchmarks measure few-shot segmentation |
| **MemorySurgeon** | that memory corruption is what makes SAM2 lose objects |
| **RehearsalGrid** | that rehearsal-data *content* is what prevents multimodal forgetting |

Each has a control arm that no adjacent paper runs: a wrong support, a vacuous sham, a token-shuffled
corpus. That is the round's signature — in each case the contribution is the control.

---

## Idea_01 — SupportAudit (B-0121) · **recommended first**

**Question.** When a few-shot segmentation method is given the *wrong* support image, how much of its
accuracy survives?

**Statistic.** Retention `= a_wrong / a_correct` per stratum; support-sensitivity `SSS = 1 − R`.
Primary estimator is the **ratio of means**, with episode-level bootstrap.

**Why it matters.** If retention is high on the distractor-present stratum, the field has been
scoring a saliency prior and calling it few-shot segmentation. If it is low, the benchmarks are
certified and a new statistic enters the toolbox. If the two strata split, that is benchmark
degeneracy, measured for the first time.

**Killer experiment.** ~5 GPU-h. Two methods, one benchmark, the distractor-present stratum.

**What the prototype changed.** The pre-registered statistic was the median of per-episode ratios.
Running the harness against controls showed per-episode retention is strongly **bimodal** — under a
wrong support a method either lands on the right object or it does not — so the median is a coin flip
on which pile is larger. The fully support-driven control scored a median of 1.000, identical to a
support-blind method, while its ratio of means was 0.762 [0.651, 0.871]. The killer experiment would
have been blind to the very effect it exists to detect. Now: ratio of means primary, median secondary
and flagged when they disagree, because a bimodal split is a finding about the failure mode.

---

## Idea_02 — MemorySurgeon (A-0017)

**Question.** When SAM2 loses an object, how much of the failure is *memory-borne* — recoverable by
deleting corrupted memory entries — versus perception-borne?

**Design.** Harvest organic failures with a fixed protocol and zero curation. At the recovery point,
run six arms: `no_op`, `targeted`, `reset`, `sham`, `slot_control`, `random_k`. No weights are ever
modified.

**Why it matters.** Every memory-policy paper (SAMURAI, DAM4SAM, SAM2Long) implicitly claims a
headroom it never measures. This produces the headroom table: what share of the oracle-timed ceiling
each published policy actually captures.

**And it has to graduate.** `KNOWN FACT` The Stage-6 audit found the Top 5 measurement-tilted and made
the method arm a **required deliverable**: if targeted deletion clears the ≥10-point margin over a
full reset, the paper must ship the surgery as a training-free wrapper benchmarked head-to-head
against SAMURAI and DAM4SAM (E9, ~40 GPU-h, conditional). The honest wrinkle, stated in the package
rather than discovered later: the measurement is **oracle-timed** and a wrapper is not, so E9 needs a
failure trigger and its gain will land strictly below the measured ceiling.

**What the prototype changed, twice.**

The **sham arm was specified backwards**. Stage 6 asked for "delete post-error entries but re-insert
count-matched pre-error duplicates at the same recency slots." Implemented literally, that arm still
removes the corruption — it performs the therapeutic action — so "targeted must beat sham" was
unpassable by construction. A sham operation makes the incision and removes nothing.

**H2 is structurally untestable on long failures, and pooling them dilutes the test.** `targeted` and
`reset` are the same operation once FIFO has flushed every pre-error entry, so those failures
contribute an exact zero to the arm gap. Only 23 of 50 simulated failures were testable, and pooling
turned a genuine +0.130 gap into +0.040 — below the pre-registered bar, in the world where the
decomposition is real. P2 is now read on the testable subset, and the failure-duration distribution
became a reported property of the corpus rather than a nuisance parameter.

The simulator also demonstrated why the controls are not optional. In a world with **no memory-borne
failure at all** — a tracker that simply does better with an emptier bank — the naive test
(`targeted` vs `no_op`) reported +0.360 and passed, **and so did P3**. Only P2 caught it. Neither
control alone is sufficient.

**Validity.** Naive correlations of 0.952 / 0.918 / 0.859 between reversible fraction and
prevention-method gain became partial correlations of 0.682 / 0.397 / **0.028** after partialling out
difficulty. The pre-registered statistic is the **minimum over a comparator set frozen before any
comparator runs**, so one strong comparator cannot carry the headline.

---

## Idea_03 — RehearsalGrid (C-0090)

**Question.** Does interleaved text rehearsal prevent language forgetting because of what the text
*says*, or because it puts a matched-scale gradient on the language pathway?

**Design.** Five arms at fixed token budget and matched per-layer gradient norms: none, curated,
random web, **token-shuffled**, **one document repeated**. Capability-stratified retention.

**Why it matters.** It is the only project in this round that changes what large labs *do* rather
than how they measure. It is also the decisive experiment for a live dispute: `arXiv:2603.14493`
argues the operative variable is task diversity — a content-side claim made observationally, with no
content-free control and no gradient matching.

**What the prototype changed.** Three things, all pre-registration rather than compute. The base
cannot be the published recipe, because LLaVA-1.5's mix already contains text-only ShareGPT — so
`A0` requires a text-stripped base with token-budget re-matching. Retention ratios need usable
denominators, and Vicuna-7B is near-floor on GSM8K and weak on IFEval, so absolute deltas are
co-primary and a denominator gate runs before the arms. And "if the matching conventions diverge, the
divergence is the finding" makes every outcome a result, so per-layer is now the declared primary.

**Cost discipline.** ~2,450 A100-h total, but **the program dies at its power gate for under 1,000**.
That asymmetry is the only thing that makes it responsible, and the demo shows the rule correctly
*refusing to answer* in the low-effect world rather than reporting an inconclusive result that would
invite one more seed and one more arm.

---

## What is genuinely uncertain

- **Idea_02's novelty window is months, not years.** Memory-policy work on SAM2 is crowded, and
  someone else may run the surgery.
- **Idea_03 will probably end at its gate.** If forgetting really is small under a well-tuned recipe,
  there is nothing to decompose at 7B.
- **Idea_01 is the safest and the least ambitious.** Its worst case is a clean, useful, unexciting
  paper — which is exactly why it is the one to run first.
- **All three have literature-verification debt.** Several sources are known only through secondary
  citation and must be read directly before any submission. Logged per idea.
- **Idea_02's method arm is the least-specified part of the round.** E9 requires a failure trigger
  that does not yet exist, and its design is sketched (attention collapse, confidence, mask-area) but
  not chosen. It is conditional on P2 and runs last, which is the right sequencing, but it is the
  place where a reader should expect the package to be thinnest.

---

## The honest bottom line

Nothing in Windows7 has been measured. What exists is three research packages whose decision rules
have been executed against synthetic controls and, in every case, found to contain at least one error
that would have compromised the real experiment. That is the deliverable: not results, but three
experiments that are now more likely to produce interpretable ones.

**Run Idea_01 E1 first. It costs five GPU-hours.**
