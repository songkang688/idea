# Idea_01 — Reviewer #2 Attacks and Responses

Compiled from `stage4_cluster_B_attacks.md` (Reviewer #2 pass) and `stage6_attack_brief.md`
(skeptical PI pass), with the Stage-6 mandatory conditions folded into the design rather than
appended as promises.

**The standard applied.** The question is never "can we argue back?" It is **"what experiment makes
the objection unanswerable?"** Attacks with no such experiment are recorded as accepted risk, not
defended away.

---

## A1 — "Post-SAM3, auditing PFENet/HSNet/BAM indicts a museum" · severity HIGH

`EVIDENCE` SAM3 (Nov 2025, `arXiv:2511.16719`) does exemplar-prompted concept segmentation, and an
image exemplar *is* a support. A panel built around 2020–2022 specialists answers a question nobody
is asking in 2026.

**Response — reframe, and pay for it with one checkpoint.** Add a SAM3-exemplar arm and make
foundation-era retention the **co-headline**; specialists become the historical control that shows
how the property changed across generations. Cost: one HF-gated checkpoint, inside the existing
budget. Day-1 task is requesting access.

This does not kill the audit — the validity methodology and the foundation-matcher numbers stand
either way — but the emphasis was wrong and it was cheap to fix.

---

## A2 — "Leg (b) is hostage to the floor you grant" · severity HIGH

SAM's automatic mask generator is a very strong class-agnostic segmenter. A weak classical saliency
floor could flip leg (b)'s verdict on identical data, so "few-shot learning is fully accounted for
by the prior" would be an artifact of which prior we granted.

**Response — refuse to pick.** Both floors are pre-registered and **every floor-dependent claim is
reported under both, never pooled** (`src/support_audit/stats.py::StratumResult.fails_floor`). A
conclusion that survives the strong Floor-A is unattackable. One that holds only under the weak
Floor-B is reported as exactly that, in those words. The attack is answered by making the
dependence a published axis instead of a hidden choice.

---

## A3 — "Wrong-class supports are not exchangeable across queries" · severity MEDIUM

Which classes are available as "wrong" correlates with query content through co-occurrence
structure, and ±50% area matching is loose. Stratum differences could partly be sampling artifacts.

**Response — three concrete changes, all promoted from ablation into the main design.**
1. **Fixed per-fold wrong-class pools**, shipped as static lists rather than regenerated from a seed
   (`counterfactual.py::write_lists`). A seed plus a code version is not reproducible.
2. **Near/far supercategory split** (2 near + 3 far per episode), with retention reported separately
   for each. If near and far agree, the sampling worry is empirically dead.
3. **Per-episode logging of area-matching relaxations**, so the reader can see how often the
   tolerance had to be widened.

---

## A4 — "Retention is unstable and `τ` is an analyst degree of freedom" · severity MEDIUM

`R = a_wrong / a_corr` blows up when `a_corr` is small, and the episode filter threshold `τ` is
chosen by us.

**Response.** `τ` is frozen at 0.2 in the pre-registration, and the **τ-sensitivity curve over
{0.1, 0.2, 0.3} is published regardless of what it shows.** If the conclusion moves with `τ`, we
say so in the abstract.

`KNOWN FACT` A related instability was found and fixed while building the prototype: the Stage-5
design aggregated per-episode ratios with a **median**, and the per-episode distribution turns out
to be bimodal (a method either lands on the right object under a wrong support or it does not). In
the harness run the fully support-driven control scored median retention 1.000 — identical to a
support-blind method — while its ratio of means was 0.762 [0.651, 0.871]. The median would have
made the killer experiment blind to the effect it exists to measure. Primary statistic is now the
**ratio of means**; the median is retained as a secondary robust statistic and a large gap between
them is flagged as a finding. See `proposal.md` §10.

---

## A5 — "Per-repo protocol differences make the panel incomparable" · severity MEDIUM

Each repository has its own preprocessing, resizing and evaluation code.

**Response — turn it into the second headline.** We must re-run every checkpoint anyway, so we run
**both** each repo's native evaluator and one shared evaluator, and publish the per-method
discrepancy table (E5, ~0.5 A100-day). `EVIDENCE` An unrelated group has reported FSS shifts of up
to 37 points from preprocessing-space mismatch (Open-V / X2). Two independent validity failures in
one paper is a materially stronger submission than either alone.

This is also why the adapters deliberately preserve per-repo preprocessing instead of unifying it
(`src/support_audit/adapters.py`): unifying would destroy the measurement.

---

## A6 — "Foreground bias is known — BAM, TBS, AENet" · severity MEDIUM (framing)

**Response — the measurement/treatment distinction, stated once and hard.** Every cited work is a
*treatment*: it proposes a fix and measures the fix on its own model. None reports the size of the
support-independent share across a panel, against a null model, stratified by whether the benchmark
even permits the prior to help. The mitigation literature is our **motivation section**, and its
density is evidence the community believes the premise. The deliverable is an assay, a
sensitivity-adjusted leaderboard, and a released split.

---

## A7 — "The certification branch is a workshop note, not a paper" · severity OPEN

If everything collapses appropriately (`R < 0.2` everywhere), we publish a certification: the
field's validity confirmed by the first counterfactual audit run on it.

**Response — none. This one is honestly unresolved.** Stage 5 asserted this branch is top-venue;
the Stage-6 attack pass was unconvinced, and we side with the attacker. There is no experiment that
settles a venue judgement.

What we do instead of arguing: **price it.** The certification is the weakest of the three outcome
branches, it costs ~5 A100-days to find out which branch we are in, and the distractor-enriched
split plus the pinned harness are artifacts that survive regardless. Recorded as an accepted risk
in `proposal.md` §20, not defended away.

---

## Attacks we expect but consider already dead

| Attack | Why it does not land |
|---|---|
| "Your method is a hack / the architecture is unmotivated" | There is no architecture. The intervention is on the input. |
| "Unfair comparison — extra parameters/data/compute" | Zero training, zero extra data, released checkpoints, published protocols. |
| "Cherry-picked episodes" | Episode lists and wrong-support lists ship as static files, frozen before inference. |
| "Not reproducible" | Public checkpoints + fixed lists + released split + SHA-256 manifest. Lowest reproducibility risk of the five Stage-6 candidates. |
| "You cannot reproduce the published numbers" | The primary statistic is a within-method ratio and does not require it. Divergences are reported as E5 results. |

---

## Residual risks, owned

1. **Checkpoint link rot** (BAM/OneDrive, HSNet/Google Drive) — the #1 practical risk. Mitigated by
   the day-1 E0 archival gate. If a checkpoint is unobtainable the panel shrinks and we say so; we
   do not silently substitute.
2. **Thin `S3` on PASCAL-5i** — COCO and LVIS carry the primary stratum; per-stratum counts are
   published before any inferential claim.
3. **Novelty perception (A6)** remains the most likely reason a reviewer scores this down even after
   every experiment lands. Positioning is the only lever, and positioning is not a guarantee.
