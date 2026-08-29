# Idea_03 — Stage-isolated localization tax in aligned VLMs

**Selection status:** Final 3, **PROVISIONAL — not locked.** Idea_03 is blocked
by **GATE-B**: no base/chat checkpoint pair has been verified to share a vision
encoder and coordinate tokenization, which this package's own `experiments.md`
has always called a *"Hard gate"*. See
[`../selection_history/stage6_battle.md`](../selection_history/stage6_battle.md) §5.

**Evidence status:** **no VLM eval, no checkpoint loaded.** Everything is
HYPOTHESIS or EXPECTED RESULT. The scripts run, but on simulated "base" and
"chat" models whose failure mode is chosen by the config, and they say so before
every number.

**Hypothesis.** The localization degradation in chat-aligned VLMs is **not**
primarily an output-format artifact, and the stage responsible can be identified
by combining format-controlled evaluation with a frozen-feature probe.

## The three-way answer

| | Probe intact | Probe drops |
|---|---|---|
| **Likelihood gap ≈ 0** | **O1** — format artifact. Write the negative | (incoherent — check the instrument) |
| **Likelihood gap > 0** | **O2** — decoding-policy tax | **O3** — representation tax |

All three outcomes are publishable. That is a strength for the science and a
weakness for prioritisation: this project has no cheap kill, so the only real
gate is GATE-B, and the only real pressure is the clock.

## Run it now (CPU, no VLM, no checkpoint, seconds)

```bash
python Idea_03/src/run_smoke.py --seed 0        # O1/O2/O3 round-trip gate
python -m unittest discover -s Idea_03/tests    # 27 self-checks
```

Requires **numpy only**. The gate plants each of the four possible answers —
`none`, `format`, `policy`, `representation` — and checks that
`classify_outcome` recovers it from the measurements alone. A decision function
that cannot recover a planted answer must not be pointed at a real one.

## The rule the code will not let you break

`classify_outcome` **raises** when the likelihood-rank mode is missing. A
free-form gap alone cannot be separated from the format confound, and skipping
mode 3 is the easiest way to publish a wrong result here. The kill rule —
*"Kill if H1 fails under constrained decoding"* — is enforced in code, not just
documented.

Likewise, `mean_iou` reports IoU with and without parse failures counted. The
difference between those two numbers **is the format tax, quantified.** A chat
model answering *"Sure! The cat is at [12, 30, 44, 80]"* has localised
correctly; scoring it zero measures prose.

## Killer experiment

Card **E-B** first (GATE-B, no GPU), then card **E1**: one verified pair, ~2k
referring expressions, three eval modes (free-form / grammar-constrained /
likelihood rank against ≤16 **shared** distractors) plus the frozen-feature
probe. ≤8 GPU-h (**HYPOTHESIS**), eval-only. See [`experiments.md`](experiments.md).

**STOP rule, verbatim:** *"STOP if likelihood gap ~0 on pair 1 and pair 2. Do
not run DPO unless observational gap survives format control."*

## The obligation Reviewer #2 attached

Verbatim from `stage4_reviewer2_cheap5.jsonl`:

> `Needs format-controlled eval + representation probe + small text-only DPO control`

Three conjuncts. The first two are card E1; the third is card E4, and without it
`proposal.md` §23 forbids any causal claim about the alignment objective.

## Highest concurrent-work risk in Windows6 — read before scheduling

Three independent records agree: Stage-3 keep confidence **0.55** (lowest of the
Final 3, note *"matched checkpoint localization tax still open"*), an
**EVIDENCE GAP at confidence ~0.5** in `literature.md`, and `Windows6/README.md`'s
own *"highest concurrent-work risk"*.

The novelty is **defined by an absence**, and the experiment is cheap,
eval-only, needs no new data and uses public checkpoints — everything that makes
it attractive to us makes it attractive to everyone else.

**Consequence for scheduling:** GATE-B and E1 should **not** be queued behind
Idea_01 despite Idea_01 being ranked *"#1 start here"* on tractability. They
cost hours and their value decays. Details in `proposal.md` §26.1.

## Package map

| File | What it holds |
|---|---|
| [`proposal.md`](proposal.md) | 28 sections: hypotheses, the 2×2, GATE-B, metrics, kill conditions, concurrent-work analysis, decision tree |
| [`experiments.md`](experiments.md) | Cards E-B, E0–E4 with thresholds and branches |
| [`reviewer_attacks.md`](reviewer_attacks.md) | Stage-4 attacks + red team, including the two only *partly* mitigated |
| [`roadmap.md`](roadmap.md) | Phases; why speed outranks compute here |
| [`literature.md`](literature.md) | Verified entries only; MDGD cited as an attack |
| [`diagrams/system.md`](diagrams/system.md) | Pipeline diagram |
| [`configs/`](configs/) | `default.yaml` (synthetic) and `e1_killer.yaml` (real protocol) |
| [`src/aligntax/`](src/aligntax/) | Boxes, three decode modes, probe, metrics, the O1/O2/O3 decision function |
| [`tests/test_smoke.py`](tests/test_smoke.py) | 27 self-checks, numpy-only |

## What the code deliberately refuses to do

`data.verify_checkpoint_pair` raises `NotImplementedError` spelling out GATE-B's
three checks, so the code cannot proceed on an unverified pair by accident.
`classify_outcome` raises without the likelihood mode. `Config` rejects unknown
keys and invalid `tax_mode` values. Silence is the failure mode that turns
EXPECTED into ACTUAL.
