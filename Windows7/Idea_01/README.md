# Idea_01 — SupportAudit

**Wrong-support counterfactual audit of few-shot segmentation.**
Internal ID `B-0121` · Windows7 · **Recommended #1 of this round.**

> Feed a few-shot segmenter a support image of a class that is provably absent from the query, and
> measure how much of its reported accuracy survives.

## Why this one is ranked first

| Property | Value |
|---|---|
| Compute to a decision | **~2 A100-days** (killer); ~5 A100-days full |
| Training | **none** — inference only |
| Data/checkpoints | all public |
| Outcome branches that publish | **all three** (reorder / certify / indict the benchmark) |
| Primary statistic | a *within-method ratio*, so it does not depend on reproducing anyone's absolute number |

It was the only unanimous #1 in any Stage-2 cluster, and it survived a genuine Reviewer #2 round
rather than a lenient one — there is no architecture to attack, because the intervention is on the
input.

## Files

| File | What is in it |
|---|---|
| `proposal.md` | The full 28-section research package. Start here. |
| `literature.md` | Prior work, what each paper actually did, and our exact difference |
| `experiments.md` | Experiment matrix E0–E7, ablations, controls, decision rules |
| `reviewer_attacks.md` | Attacks A1–A7 and the experiment that answers each |
| `roadmap.md` | Day 1 → Week 4 |
| `diagrams/architecture.md` | Mermaid protocol and data-flow diagrams |
| `src/` | Runnable harness + the statistics, validated against mock controls |
| `configs/` | Pre-registration artifacts (frozen before any inference) |
| `references/` | Checkpoint manifest template, literature verification log |

## Run the harness now

```bash
cd src
pip install -r ../requirements.txt
python run_mve.py --episodes 200 --seed 0
```

No checkpoints and no GPU required. The script builds a synthetic benchmark, runs the whole audit
pipeline, and applies the pre-registered decision rule.

### What the harness run demonstrates

`MockSegmenter` is a test fixture with a tunable `support_reliance`, giving the harness a positive
and a negative control:

```
method                stratum                      n  retention (ratio of means)    med    SSS
mock_support_blind    S1_single_object            60         1.000 [1.000,1.000]  1.000  0.000
mock_support_blind    S3_distractor_present       60         1.000 [1.000,1.000]  1.000  0.000
mock_support_driven   S1_single_object            60         1.000 [1.000,1.000]  1.000  0.000
mock_support_driven   S3_distractor_present       60         0.762 [0.651,0.871]  1.000  0.238 *
  * primary and median estimators disagree by >0.2 (bimodal episodes)
```

Three things to read off it, and all three are properties of the *instrument*, not results about any
published method:

1. **The controls separate on `S3`.** A support-blind method retains everything (1.000); a
   support-driven one loses a measurable share (0.762, CI excluding 1.0). The audit can detect what
   it is built to detect.
2. **Nothing separates on `S1`.** With a single object in the query there is only one thing to
   segment, so destroying the support cannot change the answer. This is benchmark degeneracy
   (hypothesis H3) reproduced in miniature, and it is the whole reason `S3` is the pre-registered
   primary stratum.
3. **The `*` flag matters.** The median-of-ratios estimator reports 1.000 for the support-driven
   control — it would have missed the effect entirely. Per-episode retention is bimodal, so the
   primary statistic is the ratio of means. This correction was found by running the prototype and
   is written up in `proposal.md` §10.

**No number in this repository is an experimental result about a published method.** Everything
above comes from mock fixtures and exists to validate the measurement apparatus.

## First experiment to run (Day 1)

Not the MVE — the **checkpoint archival gate** (E0). Download and SHA-256 every checkpoint in the
panel, BAM (OneDrive) and HSNet (Google Drive) first, because link rot is the project's single
biggest practical risk. Record hashes in `references/checkpoint_manifest.md`. Then freeze the
pre-registration (`configs/preregistration.yaml`) before a single inference runs.

## Killer experiment

On the pre-registered `S3` distractor-present stratum: (a) do ≥ half of specialist methods retain
`R > 0.5` under wrong-class supports, and (b) is their correct-support accuracy statistically
indistinguishable from a support-free objectness floor — reported separately under a strong floor
(SAM AMG) and a weak floor (classical saliency)? Both legs failing kills the headline and we
publish the certification result instead.

## Status

Design complete, harness runs, statistics validated against controls. Not yet run against any real
checkpoint.
