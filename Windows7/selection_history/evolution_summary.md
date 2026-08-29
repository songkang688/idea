# Windows7 — Evolution Summary

```
Stage 1  exploration          1,110 raw ideas    (3 clusters, parallel agents)
Stage 2  independent review     255 survive
Stage 3  adversarial prior work  52 survive      ← the largest kill, by far
Stage 4  Reviewer #2 attack      21 survive
Stage 5  experimental engineering  5 survive
Stage 6  research-group battle     3 final
```

---

## Stage 1 — 1,110 raw ideas

Three clusters explored in parallel, each seeded from a different failure mode rather than from a
topic. The framing matters: "where does X break" generates falsifiable ideas, while "what could we
add to X" generates module stacking.

| Cluster | Territory | Yield |
|---|---|---|
| A | video segmentation, tracking, SAM2 memory, temporal failure | ~370 |
| B | few-shot / zero-shot segmentation, prompt sensitivity, benchmark integrity | ~370 |
| C | multimodal fine-tuning, forgetting, PEFT, representation drift | ~370 |

Generation angles: existing-method failure, dataset failure, foundation-model failure, domain shift,
prompt sensitivity, fine-tuning instability, catastrophic forgetting, small objects, boundary
quality, uncertainty, long tail, annotation efficiency, calibration, robustness, synthetic data,
evaluation weakness, surprising empirical phenomena, unproven community assumptions, negative
results.

**Rejected on sight:** "Module A + Module B", "Transformer + CNN", "apply method X to medical
images", "swap the loss", "swap the backbone", "add attention." These were filtered during generation
rather than at Stage 2, which is why the Stage-2 pass rate looks high.

---

## Stage 2 — 1,110 → 255

Independent reviewers scoring novelty, significance, scientific question, soundness, feasibility,
compute, data availability, baseline availability, likelihood-already-published, experimental
clarity, venue potential, risk, upside, and research ROI.

**Not ranked by mean score.** Four categories were protected from averaging:

1. high-risk / high-reward ideas
2. simple but counter-intuitive ideas
3. ideas where reviewers disagreed sharply
4. ideas falsifiable by a cheap experiment

All three finalists came from category 4. That is not a coincidence — a cheap falsification test is
what lets an idea survive Stage 5's cost scrutiny.

---

## Stage 3 — 255 → 52 · the real filter

The stage ran under the assumption that **every idea has already been done**, and the agents' job was
to kill novelty, not defend it.

This removed 80% of the survivors and eliminated essentially every "new architecture" idea in the
pool. The recurring pattern: the mechanism was already published, usually under a different name in
an adjacent subfield.

Ideas were **mutated rather than killed** when only part of the novelty was gone. Both B-0121 and
A-0017 passed through this: each began as a method proposal and came out as a measurement project,
because the method was taken but the measurement was not.

---

## Stage 4 — 52 → 21

Each idea treated as a submitted paper, attacked for rejection, then defended.

The bar was **not** "can we rebut the reviewer?" but "**can we design an experiment that makes the
objection moot?**" Ideas whose central attack had no affordable experimental answer were eliminated
regardless of how good the rebuttal sounded.

Most common fatal attacks: unremovable confounds, missing baselines that do not exist publicly,
metrics that cannot distinguish the hypothesis from the trivial alternative.

---

## Stage 5 — 21 → 5

Each idea treated as a project starting next week: architecture, data, baselines, metrics, ablations,
GPU estimate, minimal viable experiment, stop conditions.

The killing criterion was **cost-per-decision** — the price of the cheapest experiment that decides
whether to continue. Several scientifically interesting ideas died here purely on cost, which is the
correct outcome for a group that must actually run them.

**Top 5:** B-0121 (SupportAudit), A-0017 (MemorySurgeon), C-0090 (RehearsalGrid), C-0028 (decision
triple), A-0044 (temporal calibration).

---

## Stage 6 — 5 → 3

Multi-round group battle: PI, skeptical PI, domain experts, Reviewer #2, methodology and
reproducibility reviewers, the engineer who has to build it, one researcher hunting fatal flaws and
one hunting hidden upside, plus a meta-auditor.

**Selected:** B-0121, A-0017, C-0090.
**Cut:** C-0028 (overlapped C-0090's territory at higher cost), A-0044 (calibration claim could not
be separated from a difficulty confound within budget).

The panel attached **mandatory conditions** to all three survivors rather than approving them as
written. Those conditions are folded into the proposals' method and experiment sections, not appended
as caveats. See `reviewer_summary.md`.

---

## Stage 7 — the packages

Each final idea written as a 28-section research package with a **runnable prototype**.

Building the prototypes was not a formality. Each of the three surfaced at least one error that would
have compromised the real experiment:

| Idea | Error found by building it |
|---|---|
| B-0121 | primary statistic (median of ratios) was blind to the effect it exists to detect |
| A-0017 | the sham arm was specified backwards; and pooling failures longer than the memory horizon dilutes the H2 test toward zero |
| C-0090 | the control arm contradicted the premise, because the published mix already contains text rehearsal |

That is the argument for writing prototypes at Stage 7 rather than at the start of the project: three
design errors caught for a few CPU-seconds each.

---

## Where the artifacts live

Stage 1–6 outputs are on `songkang688/idea` branches, cited per idea in each `proposal.md`
Provenance section. Representative:

```
cursor/stage1-cluster-{a,b,c}-ideas-*
cursor/stage2-cluster-{a,b,c}-scoring-*
cursor/stage3-cluster-{a,b,c}-priorwork-*
cursor/stage4-cluster-{a,b,c}-reviewer2-*
cursor/stage5-cluster-{a,b,c}-engineering-*
cursor/stage6-attack-pass-top5-cca8
cursor/stage6-defense-top5-2995
cursor/stage6-meta-review-final3-4fc5
```
