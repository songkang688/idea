# Idea_03 — Experiment cards

> **STATUS OF EVERY CARD: NOT RUN**, except E0, which runs on a synthetic pair
> and can only validate the decision logic. **No VLM has been run and no
> checkpoint loaded** (`Windows6/README.md`: *"no VLM eval"*). Windows6 has
> **zero ACTUAL RESULTS**. Budgets are **HYPOTHESIS**; predicted trends are
> **EXPECTED RESULT**.
>
> **E-B blocks everything.** GATE-B is open: no base/chat pair has been
> verified to share a vision encoder and coordinate tokenization — this file's
> own long-standing wording is *"Hard gate"*.

## Card index and execution order

| Card | Name | Gate it decides | Budget (HYPOTHESIS) | Status |
|---|---|---|---|---|
| **E-B** | **GATE-B: checkpoint pair verification** | Is stage isolation available? | **0 — no GPU** | **NOT RUN — BLOCKING** |
| **E0** | Harness validation + O1/O2/O3 round trip | Is the decision logic sound? | ~0, CPU seconds | **RUN — PASS** |
| **E1** | **KILLER**: pair 1, three eval modes + probe | H1, H2 | ≤8 GPU-h | NOT RUN |
| **E2** | Pair 2 replication | generality; releases the STOP rule | ≤8 GPU-h | NOT RUN |
| **E3** | Probe layer sweep + capacity ablation | robustness of H2 | ≈2 GPU-h | NOT RUN |
| **E4** | **H3**: text-only DPO LoRA | RQ4 causality | 1–2 × 24 GB, days | NOT RUN |

Order: **E-B → E0 → E1 → E2 → E4**, with **E3 parallel to E2**. E4 is gated
behind E1 *and* E2 by the STOP rule below.

---

## E-B — GATE-B: checkpoint pair verification — STATUS: NOT RUN, BLOCKING

**Purpose.** Establish that stage isolation is possible at all. Without a
matched pair, any gap could be an encoder or tokenizer difference, and the
paper's central claim is unavailable.

**Input.** Published model cards, configs and licences for candidate pairs:
LLaVA / LLaVA-RLHF (**VERIFIED PRIOR WORK**, listed in `literature.md`),
Qwen-VL / Qwen-VL-Chat (`CITATION NEEDED — 待人工核验`).

**Three checks, all required.**

1. **Shared vision encoder.** Same architecture *and* same weights at the
   vision tower, confirmed from the config, not inferred from the name.
2. **Shared coordinate tokenization.** The two checkpoints must represent
   coordinates identically — same normalisation, same special tokens, same
   digit handling. A differing scheme silently makes the comparison a tokenizer
   study.
3. **Licences permit the comparison and publication of derived metrics.**

**Decision thresholds.**

| Observation | Action |
|---|---|
| All three hold for ≥1 pair | **GATE-B CLOSES** → E0/E1 |
| Encoder or tokenization differs | **Stage isolation unavailable.** Descope to a format-artifact study — a much smaller paper. Re-argue the Final-3 slot before spending GPU |
| Licences block it | Find another pair, or descope |

**Cost.** Hours of reading. **No GPU.**

**Write the finding into this card.** The written verification *is* the artifact
that closes GATE-B. `data.verify_checkpoint_pair` raises `NotImplementedError`
with these three checks spelled out, so the code cannot proceed on an unverified
pair by accident.

---

## E0 — Harness validation and O1/O2/O3 round trip — STATUS: RUN, PASS

**Purpose.** Confirm the decision logic recovers the right answer on data whose
answer is known. `classify_outcome` is the function that converts measurements
into the paper's claim, so it is the one piece that must be right before any
real number exists.

**Input.** `data.make_pair` — a synthetic base/chat pair whose degradation mode
is **chosen by config**: `none`, `format`, `policy`, or `representation`.

**Run.**

```bash
python Idea_03/src/run_smoke.py --seed 0
python -m unittest discover -s Idea_03/tests
```

**Procedure.** Plant each of the four modes in turn; measure free-form,
constrained, likelihood and probe gaps; ask `classify_outcome` for a verdict;
check it matches what was planted.

**Decision threshold.** `run_smoke.py` exits non-zero unless all four modes
round-trip. A decision function that cannot recover a planted answer must not be
pointed at a real one.

**Two properties this card pins.**

1. **The classifier refuses without the likelihood mode.** `classify_outcome`
   raises when `likelihood_gap is None`. That is the kill rule in code — a
   free-form gap alone cannot be separated from the format confound, and
   skipping mode 3 is the easiest way to publish a wrong result here.
2. **Parse failures are reported separately from IoU.** `mean_iou` offers both
   `count_failures=True` and `False`, and a self-check pins the difference. A
   chat model that answers *"The cat is at [12, 30, 44, 80]"* has localised
   correctly; scoring it zero measures prose, not vision.

**What E0 does NOT show.** Nothing about any real VLM. The base and chat models
are simulators whose failure mode we chose. `run_smoke.py` says so before every
number.

---

## E1 — KILLER: pair 1, three eval modes + probe — STATUS: NOT RUN

**Requires GATE-B closed.**

**Input.** One verified pair; ~2k RefCOCO-style referring expressions
(`CITATION NEEDED — 待人工核验`). Same prompts, same images, same shared
distractor sets for both checkpoints.

**The three eval modes**, in order of increasing format immunity:

| Mode | What it measures | What it still leaves in |
|---|---|---|
| **1. Free-form** | Generation as deployed | The whole format confound |
| **2. Grammar-constrained** | `x1,y1,x2,y2` only, no prose | The decoding policy — the model can still emit worse coordinates |
| **3. Likelihood rank** | Score the gold box string against ≤16 **shared** distractor boxes | Nothing generative. **This is the decisive number** |

The distractors are shared between checkpoints on purpose. If each model ranked
against its own candidate set, a likelihood gap could come from an easier set
rather than a better model.

**The probe (H2).** Linear probe on **frozen** visual tokens → box (or region
centre), fit on a small train split, evaluated held out, for both checkpoints.
Ridge-regularised: with a small train split and correlated token dimensions, an
unregularised fit can recover a box from noise and would report "representation
intact" for a checkpoint whose representation was destroyed.

**Reported per checkpoint:** IoU (failures counted and not counted),
**parse-failure rate as its own number**, acc@IoU 0.5, rank acc@1, probe MAE.

**Decision thresholds** (`gap_tolerance` pre-registered at 0.02):

| Observation | Outcome | Action |
|---|---|---|
| No gap under constrained decoding | — | **KILL** — formatting confound, as pre-registered |
| Likelihood gap ≈ 0 | **O1** | Provisional format artifact → confirm on pair 2, then write the negative |
| Likelihood gap > 0, probe intact | **O2** | Decoding-policy tax → E2 |
| Likelihood gap > 0, probe drops | **O3** | Representation tax → E2. The most consequential outcome |
| Likelihood mode not run | — | **No verdict.** The code raises rather than guessing |

**Budget.** ≤8 GPU-h (**HYPOTHESIS**). Eval-only; no training.

---

## E2 — Pair 2 replication — STATUS: NOT RUN

**Purpose.** One pair is one draw. E2 is also what releases (or fires) the STOP
rule guarding the expensive card.

**Procedure.** Repeat E1 on a second GATE-B-verified pair.

**Decision thresholds.**

| Observation | Action |
|---|---|
| Same outcome class on both pairs | **CONTINUE** — E4 unlocked if the gap survived format control |
| **Likelihood gap ≈ 0 on pair 1 AND pair 2** | **STOP.** Write O1 as a negative result. **Do not run DPO** |
| Outcome reverses across pairs | **KILL the general claim**; report as pair-specific and name the pairs in the title |
| Only one pair passes GATE-B | Honest scope — the title names that pair. E4 stays locked; a causal claim from a single pair is not defensible |

**FACT, verbatim, this file's long-standing rule:** *"**STOP** if likelihood gap
~0 on pair 1 and pair 2. Do not run DPO unless observational gap survives format
control."*

**Budget.** ≤8 GPU-h (**HYPOTHESIS**).

---

## E3 — Probe layer sweep and capacity ablation — STATUS: NOT RUN

**Purpose.** Pre-empt the two obvious attacks on H2: *"you probed the wrong
layer"* and *"a linear probe is too weak"*.

**Procedure.** Repeat the H2 probe at several depths of the vision tower.
Additionally fit a small MLP probe alongside the linear one.

**Decision thresholds.**

| Observation | Interpretation |
|---|---|
| The base/chat probe gap is consistent across layers | H2 is robust; report the sweep as a figure |
| The gap exists at one layer only | **DOWNGRADE** — report the sweep, not a headline |
| Linear probe drops but MLP probe does not | The information is **present but not linearly accessible** — a distinct, reportable finding, and a real refinement of "representation tax" |

**Budget.** ≈2 GPU-h (**HYPOTHESIS**). Parallelisable with E2.

---

## E4 — H3: text-only DPO LoRA — STATUS: NOT RUN, GATED

**LOCKED behind the E2 STOP rule.** Do not run unless the observational gap
survived format control on **both** pairs.

**Purpose.** RQ4: is the tax caused by the alignment **objective**, or by the
image data mix used during alignment? Observational comparison cannot separate
them, which is why Reviewer #2's residual names this arm explicitly.

**Procedure.** Apply a small LoRA DPO (`CITATION NEEDED — 待人工核验`) to the
**base** checkpoint using **text-only** preference data — no images. Re-run E1's
three modes and the probe.

**Decision thresholds.**

| Observation | Interpretation |
|---|---|
| The localization gap reproduces after text-only DPO | Strong support for **objective**, not image data mix. The causal claim is available |
| No effect | Text-only preference optimisation does not reproduce it. **Report as such** and drop the causal framing; H1+H2 stand alone |
| Effect present but tiny | Report the effect size; do not upgrade it to a causal headline |

**FACT.** `reviewer_attacks.md`: *"Unmatched data mixes: **do not claim causal
RLHF without H3**."* Without E4, §23 of `proposal.md` forbids the causal claim
entirely.

**Budget.** 1–2 × 24 GB GPUs, days (**HYPOTHESIS**, from `proposal.md`). By far
the most expensive card in the package, which is why it is gated twice.

---

## Cross-cutting rules

1. **GATE-B before any GPU.** An unmatched pair makes this a tokenizer study.
2. **Always run all three eval modes.** The progression *is* the argument, and
   the decision function refuses to return a verdict without mode 3.
3. **Distractors are shared** between checkpoints.
4. **Parse-failure rate is always its own number**, never folded into IoU.
5. **Thresholds are pre-registered** (`gap_tolerance = 0.02`) and applied by
   released code, so a reader can apply our rule to their own measurements.
6. **Cite MDGD as an attack, not as background.** The generic-forgetting
   headline is published and was killed at Stage 3.
7. **Re-check the adjacent literature immediately before writing.** The novelty
   is absence-defined at confidence ~0.5 and `README.md` marks this the highest
   concurrent-work risk in Windows6 (`proposal.md` §26.1).
8. **Budgets stay HYPOTHESIS.** The ≈8 GPU-h figure is an estimate from
   `evolution_summary.md`, never a measurement.
