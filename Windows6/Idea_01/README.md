# Idea_01 — SAM AMG as intensity clustering on CT

**Selection status:** Final 3, **PROVISIONAL — not locked.** Stages 1–6 are
recorded; the lock verdict and its open gates are in
[`../selection_history/stage6_battle.md`](../selection_history/stage6_battle.md) §5.
Idea_01 is the one member of the Final 3 with **no unverified data or
checkpoint precondition**, which is why `Windows6/README.md` marks it
*"#1 start here"*.

**Evidence status:** **no real SAM numbers, no real CT.** Everything in this
package is HYPOTHESIS or EXPECTED RESULT. The scripts run, but on a synthetic
phantom with a threshold connected-component stand-in for AMG, and they print a
placeholder banner saying so before every number.

**Hypothesis (falsifiable).** On windowed CT, SAM Automatic Mask Generation
(AMG) mask sets agree with intensity clustering (k-means / multi-Otsu / GMM)
more than with texture-based superpixels (SLIC), and AMG tracks **intensity
remaps** while remaining **invariant to intensity-preserving texture shuffles**.

If the texture-shuffle arm moves AMG as much as the intensity remap, the
mechanistic claim is **dead** — see the downgrade path below.

## One-liner

SAM's "objectness" on CT is mostly HU clustering after windowing — unless the
counterfactuals say otherwise.

## Run it now (CPU, no weights, no data, seconds)

```bash
python Idea_01/src/run_smoke.py --seed 0        # E0 harness gate
python -m unittest discover -s Idea_01/tests    # 22 self-checks
```

Requires **numpy only**. scipy and PyYAML are optional accelerants; everything
runs and passes without them. `run_smoke.py` exits non-zero if the harness
fails its own E0 gate.

## Killer experiment (Day 1)

Card **E1** in [`experiments.md`](experiments.md): **100** pre-registered
TotalSegmentator/MSD slices, abdomen window, SAM ViT-B AMG versus k-means /
multi-Otsu / GMM / SLIC. Three pre-registered metrics — Hungarian IoU, ARI,
boundary-F — all reported. ≈2 GPU-h (**HYPOTHESIS**).

> The sample size was inconsistent in the record (50 in some places, 100 in
> others). `stage6_battle.md` §4.7 logged it and §6 resolved it to **100**.

Then card **E3**, the counterfactual arms. E3 is the one that decides whether
this is a mechanistic paper.

## The obligation that decides what this paper is

Reviewer #2 let this idea through **conditionally**. Verbatim from
`stage4_reviewer2_cheap5.jsonl`:

> `Must earn mechanistic via intensity vs texture counterfactuals; else evaluation note`

Card E3 is the whole of that obligation. If it fails, the contribution
downgrades to an evaluation note — and note the unresolved conflict recorded in
`stage6_battle.md` §4.4: this package's `reviewer_attacks.md` reads the same
contingency as *"do not submit"* rather than *"downgrade"*. **Settle which
governs before writing.**

## Package map

| File | What it holds |
|---|---|
| [`proposal.md`](proposal.md) | 28 sections: hypotheses, method, interventions, baselines, metrics, kill conditions, decision tree |
| [`experiments.md`](experiments.md) | Cards E0–E6 with inputs, thresholds, branches and budgets |
| [`reviewer_attacks.md`](reviewer_attacks.md) | Stage-4 attacks + our red team, each with the evidence that answers it |
| [`roadmap.md`](roadmap.md) | Phases, what runs in parallel, what runs last |
| [`literature.md`](literature.md) | Verified entries only; unverifiable slots left as `CITATION NEEDED` |
| [`references/math.md`](references/math.md) | Metric definitions, including why the IoU normalisation changed |
| [`diagrams/system.md`](diagrams/system.md) | Pipeline diagram |
| [`configs/`](configs/) | `default.yaml` (synthetic smoke) and `e1_killer.yaml` (the real protocol) |
| [`src/amgclust/`](src/amgclust/) | Metrics, segmenters, interventions, pipeline, config/seed control |
| [`tests/test_smoke.py`](tests/test_smoke.py) | 22 self-checks, numpy-only |

## What the code deliberately refuses to do

`segmenters.sam_amg` and `data.load_real_ct_slices` raise `NotImplementedError`
with instructions rather than returning plausible fake output. A package that
silently substitutes a mock for the real thing is how EXPECTED becomes ACTUAL by
accident.
