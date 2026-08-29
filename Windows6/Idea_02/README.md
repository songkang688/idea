# Idea_02 — Camera-ID leakage inflation on smoke/fire benchmarks

**Selection status:** Final 3, **PROVISIONAL — not locked.** Idea_02 is the
member blocked by **GATE-A**: it has never been verified that camera metadata
exists on any public smoke/fire set, and this package's own first stop rule is
*"Kill if no camera metadata."* See
[`../selection_history/stage6_battle.md`](../selection_history/stage6_battle.md) §5.

**Evidence status:** **no smoke mAP, no detector trained.** `proposal.md` states
*"We have not trained a detector here."* Everything is HYPOTHESIS or EXPECTED
RESULT. The scripts run, but on a synthetic corpus whose camera signature was
planted on purpose, and they say so before every number.

**Hypothesis.** Random splits inflate detector performance relative to
**camera-disjoint** splits; **event-disjoint** (PYRONEAR-style) is *not* the
same as camera-disjoint; and empty frames from **seen** cameras score
differently from unseen ones — memorisation, not only geographic shift.

## Why the empty frames are the whole paper

Camera-disjoint scoring lower is easy to dismiss as ordinary domain shift.
Empty frames contain **no plume**, so a seen-versus-unseen gap on negatives
cannot be a plume-appearance effect — it has to be the background. That is what
turns a domain-shift observation into a memorisation claim.

`proposal.md`: *"Fatal if we only report camera-disjoint drop without H4."*

## Run it now (CPU, no dataset, no detector, seconds)

```bash
python Idea_02/src/run_smoke.py --seed 0        # split-structure gate
python -m unittest discover -s Idea_02/tests    # 24 self-checks
```

Requires **numpy only**. The gate checks the property H2 depends on:

| protocol | cameras shared | events shared |
|---|---|---|
| random | > 0 | > 0 |
| **event_disjoint** | **> 0** | **0** |
| camera_disjoint | 0 | 0 |

That middle row is the hypothesis in one line — holding out episodes leaves the
towers behind. If the code could not produce that structure, H2 would not be
expressible and no real run would be worth starting.

## Killer experiment

Card **E-A** first (GATE-A camera inventory, no GPU), then card **E1**:
PYRONEAR subsample, YOLOv8n, 1 seed × 3 protocols, camera-ID probe, empty-frame
FPR. ≈10 GPU-h (**HYPOTHESIS**). See [`experiments.md`](experiments.md).

## The obligation Reviewer #2 attached

Verbatim from `stage4_reviewer2_cheap5.jsonl`:

> `Need event-disjoint vs camera-disjoint gap plus empty-frame memorization probe`

Both conjuncts, not either. **And note there is no recorded downgrade clause** —
unlike Idea_01, this idea was given no *"else …"*. The only documented fallback
is the <10-camera pivot, which forfeits H2. `stage6_battle.md` §2.2 recorded the
honest reading: **full paper or kill.**

## Two protocol defects the harness caught

Both would have produced a publishable-looking but wrong result, and both are
now pinned by self-checks:

1. **The camera-ID probe was evaluated on a random split.** With the camera
   signature switched off entirely it still beat chance by ≈0.17 — it was naming
   the camera by recognising the fire *episode*, not the tower. The probe is now
   always evaluated **event-disjoint**.
2. **The empty-frame comparison had no seen-camera side.** Restricting empties
   to the test split puts them all on the unseen side under camera-disjoint, and
   the seen FPR came out `nan`. The detector now trains on non-empty frames
   only, so every empty frame is held out and can be partitioned purely by
   whether its camera was seen.

## Package map

| File | What it holds |
|---|---|
| [`proposal.md`](proposal.md) | 28 sections: hypotheses, instruments, GATE-A, metrics, kill conditions, decision tree |
| [`experiments.md`](experiments.md) | Cards E-A, E0–E5 with thresholds and branches |
| [`reviewer_attacks.md`](reviewer_attacks.md) | Stage-4 attacks + red team, including the two only *partly* mitigated |
| [`roadmap.md`](roadmap.md) | Phases; what is parallel; what never runs before GATE-A |
| [`literature.md`](literature.md) | Verified entries only; the "no inflation number we did not compute" rule |
| [`diagrams/system.md`](diagrams/system.md) | Pipeline diagram |
| [`configs/`](configs/) | `default.yaml` (synthetic) and `e1_killer.yaml` (real protocol) |
| [`src/camsplit/`](src/camsplit/) | Splits + overlap accounting, metrics, probe, detector stand-in, pipeline |
| [`tests/test_smoke.py`](tests/test_smoke.py) | 24 self-checks, numpy-only |

## What the code deliberately refuses to do

`data.load_real_corpus` and `detector.train_real_detector` raise
`NotImplementedError` with instructions rather than returning plausible fake
output. `match_equal_n` raises rather than shipping a comparison whose class
ratio it could not match. `Split` raises on overlapping train/test indices.
Silence is the failure mode that turns EXPECTED into ACTUAL by accident.
