# Idea_02 — MemorySurgeon

**Causal memory surgery as a validated decomposition instrument for SAM2.**
Internal ID `A-0017` · Windows7 · **Highest ceiling of the round, and the highest single risk.**

> Eight memory policies compete to fix SAM2's tracking failures. None of them can say how much there
> was to fix. This supplies the denominator.

## The one-paragraph version

When SAM2 loses an object in a long video, delete the memory entries written after the failure
began, replay from the ground-truth recovery opportunity, and measure how much of the failure was
*memory-borne* rather than representation-borne. Three pre-registered controls turn that from a
repair heuristic into a decomposition instrument: it must beat a full reset, it must beat a vacuous
sham, and the per-sequence reversible fraction must predict independent prevention methods' gains
**after generic sequence difficulty is partialled out**.

## Files

| File | What is in it |
|---|---|
| `proposal.md` | The full 28-section research package. Start here. |
| `literature.md` | The crowded 2025–2026 SAM-memory lane, and our exact remaining difference |
| `experiments.md` | E0–E8, arms, ablations, decision rules |
| `reviewer_attacks.md` | A1–A6 and expert disagreements D1–D2, with the experiment answering each |
| `roadmap.md` | Day 1 → Week 4 |
| `diagrams/architecture.md` | Mermaid: surgery arms, decision flow, validity design |
| `src/` | Runnable prototype: memory bank, six arms, replay gate, partialled validity |
| `configs/preregistration.yaml` | Frozen before any run — including the comparator set |
| `references/` | Access checklist, literature verification log |

## Run the prototype now

```bash
cd src
pip install -r ../requirements.txt
python run_pilot.py --failures 400 --sequences 60 --seed 0
```

No GPU, no checkpoints. It runs the pilot decision rule against a simulator whose failure
attribution is known by construction, which is the only way to check that the decision rule can
tell a real effect from an artifact.

### What the prototype run demonstrates

Two scenarios, and the second is the important one.

**Scenario A — memory-borne failure is real.**

```
H2-testable failures (pre-error memory survived FIFO): 23/50
recovery rate by arm: no_op=0.08 targeted=0.52 reset=0.48 sham=0.04 slot_control=0.54
targeted-no_op          +0.440  [+0.280, +0.580]   P1 PASS
targeted-sham           +0.480  [+0.340, +0.620]   P3 PASS
targeted-reset (all)    +0.040  [-0.160, +0.240]   <-- diluted, NOT the test
targeted-reset (H2 set) +0.130  [-0.130, +0.391]   <-- P2 is read here, PASS
VERDICT: decomposition survives all three arms at pilot scale.
```

**Scenario B — no memory-borne failure at all; the tracker simply does better with an emptier bank.**

```
recovery rate by arm: no_op=0.58 targeted=0.94 reset=1.00 sham=0.64 slot_control=0.70
targeted-no_op          +0.360  [+0.200, +0.500]   P1 PASS   <-- the naive test is fooled
targeted-sham           +0.300  [+0.140, +0.460]   P3 PASS   <-- and so is this control
targeted-reset (H2 set) -0.130  [-0.304, +0.000]   P2 FAIL   <-- only P2 fires
slot_control-targeted   -0.240  [-0.380, -0.100]
VERDICT: targeted is no better than a restart. Publishable as a bounded diagnostic
post-mortem, not as a decomposition.
```

Scenario B is the whole reason the control arms exist. A design that only tested "does targeted
deletion beat doing nothing" would have reported a +0.360 effect and called it a causal
decomposition — and note that **P3 passes here too**. Only P2 catches this particular artifact. The
two controls are complementary and neither alone is sufficient.

**Predictive validity, on data where the confound is present by construction:**

```
comparator     naive r   partial r
SAMURAI          0.952       0.682
DAM4SAM          0.918       0.397
SAM2Long         0.859       0.028
min partial r = 0.028 (threshold 0.4) -> FAIL
```

This is reviewer attack A1 made concrete. Raw correlations near 0.9 look like overwhelming
validation; after partialling out no-op recovery, failure count and distractor density, one
comparator drops to 0.03. The pre-registered statistic is the **minimum over a comparator set frozen
before any comparator runs**, so a single strong comparator cannot carry the headline.

**Every number above is simulated.** It validates the decision rule, not SAM2.

## Two design corrections found by building this

1. **The sham arm was specified backwards.** Stage 6 asked for "delete post-error entries but
   re-insert count-matched pre-error duplicates." Implemented literally, that arm still removes the
   corruption — it performs the therapeutic action — so "targeted must beat sham" would be
   unpassable by construction. A sham operation makes the incision and removes nothing. The vacuous
   version is now `sham`; the literal Stage-6 version is kept as `slot_control`, answering a
   different question. See `proposal.md` §3.
2. **`targeted` and `reset` are the same operation when the failure outlasts the memory horizon.**
   FIFO has already flushed every pre-error entry, so H2 is untestable on those failures — and
   including them does not measure a smaller effect, it **dilutes a real one toward zero** by a
   factor set by the corpus's failure-duration distribution. In the prototype only 23 of 50 failures
   were H2-testable, and pooling turned a genuine +0.130 reset gap into +0.040, which would have
   failed P2 in the world where the decomposition is real. **P2 is therefore read on the H2-testable
   subset**, and the real harvest must report that share at E1 before any P2 claim. See
   `proposal.md` §3 and §19.
3. **The pilot is underpowered for P2 specifically.** Scenario A's H2-subset gap is +0.130 with a CI
   of [-0.130, +0.391] at n = 23. The 50-failure pilot gate is adequate for P1 and P3 and is *not*
   adequate for P2 — so a P2 failure at pilot scale is a signal to enlarge the H2 subset, not to
   kill the project. Only a P3 failure kills at pilot scale.

## First experiment to run (Day 1)

**E0, the replay-determinism gate.** The `no-op` arm must reproduce the original failure
bit-for-bit; SAM2's video-predictor caches make this a real risk, not a formality. If replay is not
deterministic, every arm difference is partly harness noise and nothing downstream is interpretable.
Also on day 1: confirm DiDi access (`go.vicos.si/didi` — no mirror exists).

## Killer experiment

≥200 organic failures. `targeted` must beat `no_op` by ≥30 points, `reset` by ≥10, and `sham` by
≥10; and `min_{c ∈ frozen} partial r > 0.4`. Either miss kills the instrument claim. ≈60 GPU-h.

## Biggest risk

**The scoop clock.** `EVIDENCE` The SAM-memory subfield published at least six memory policies in
two years and a systematic memory-design study with a SAM3 zoo in Dec 2025. This is the
fastest-decaying novelty in Windows7 and should be sequenced first if only one project can start.

## Status

Design complete, prototype runs, decision rule validated against known-artifact scenarios. Not yet
run against SAM2.
