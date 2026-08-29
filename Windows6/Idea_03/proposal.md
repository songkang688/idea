# Idea_03 — Stage-isolated localization tax in aligned VLMs (Windows6 / F-031 · E-009)

> **Epistemic status of this entire document.** Nothing here has been run.
> Every quantity is **HYPOTHESIS** or **EXPECTED RESULT**. `Windows6/README.md`
> records *"no VLM eval"*; no checkpoint has been loaded. Citations are
> **VERIFIED PRIOR WORK** only where they already appear in `literature.md` or
> `selection_history/literature_anchors.md`; every other slot reads
> `CITATION NEEDED — 待人工核验`.
>
> **Two things make this the riskiest member of the Final 3.** GATE-B is open —
> no base/chat checkpoint pair has been verified to share a vision encoder and
> coordinate tokenization, which this package's own `experiments.md` calls a
> *"Hard gate"*. And `README.md` marks it *"highest concurrent-work risk"*; §26
> treats that as a scheduling constraint, not a caveat.

## 1. Title & identifiers

| Field | Value |
|---|---|
| Working title | *Which Stage Costs the Box? Format-Controlled Localization Tax in Aligned VLMs* |
| Windows6 ID | `Idea_03` |
| Stage-1 origin | `F-031` / `E-009`, mutated via `F-039` |
| Stage-3 record | `E-009`, `continue: keep`, `novelty_confidence: **0.55**`, note *"matched checkpoint localization tax still open"* |
| Stage-4 record | `alignment-tax-localization`, `continue: survive`, `advance: true` |
| Auditor | protected keep, **stage-isolated** (`auditor_overlay.md`) |
| Selection status | Final 3, **PROVISIONAL** — `stage6_battle.md` §5, blocked on GATE-B |
| Paper type | analysis / diagnosis |

## 2. One-sentence claim

**HYPOTHESIS.** The localization degradation observed in chat-aligned VLMs is
**not** primarily an output-format artifact, and it can be attributed to a
specific stage by combining format-controlled evaluation with a frozen-feature
probe — separating a *decoding-policy* tax from a *representation* tax.

## 3. Abstract

**HYPOTHESIS, not measured.** Visual forgetting under instruction tuning is
already published (MDGD, EMNLP Findings 2025 — **VERIFIED PRIOR WORK**), and
Reviewer #2 killed the generic headline outright. What survives is narrower and
harder: **which stage** pays the cost, and **whether the visual backbone still
contains the box** even when the model cannot say it. We evaluate a base/chat
pair under three modes of increasing format immunity — free-form,
grammar-constrained, and likelihood ranking of the gold box against shared
distractors — and pair that with a linear probe on frozen visual tokens. The
three-way outcome (**O1** format artifact / **O2** policy tax / **O3**
representation tax) is decided by a pre-registered function of the
measurements. **No VLM has been run.**

## 4. Background & motivation

Aligned chat models are widely reported to be worse at emitting coordinates
than their base counterparts. Two very different things could be true:

1. **The model still knows where the object is** and has been aligned into
   answering in prose, so a strict parser scores it zero.
2. **Alignment moved the representation**, and the localization information is
   genuinely degraded.

These call for opposite responses — a decoding fix versus a training fix — and
the literature does not currently separate them. The instrument that separates
them is cheap: a probe on frozen features asks whether the box is still *in*
the model, independently of whether the model can *say* it.

**Why the framing must stay narrow.** *"Alignment hurts vision"* is published
and was killed at Stage 3. This paper is **stage isolation plus format
control**, or it is nothing.

## 5. Problem statement & research questions

- **RQ1.** Does a localization gap between base and chat survive
  grammar-constrained decoding?
- **RQ2.** Does it survive generation entirely, i.e. under likelihood ranking?
- **RQ3.** Do frozen visual tokens still linearly encode the box in the chat
  checkpoint?
- **RQ4 (causal).** Does text-only preference optimisation reproduce the gap —
  implicating the objective rather than the image data mix?

## 6. Hypotheses (pre-registered)

Carried forward verbatim in substance from the original proposal:

- **H1.** Constrained box metrics drop from base → chat on ≥1 public pair.
- **H2.** The linear probe on frozen visual tokens **does not** drop (the tax is
  decoding/format) **or does** drop (the tax is representation). H2 is
  deliberately two-sided: both answers are publishable, and only *not measuring*
  is a failure.
- **H3 (optional, causal).** LoRA DPO on **text-only** preferences still hurts
  H1 → the objective, not the image data mix.

**Kill** if H1 fails under constrained decoding (formatting confound).

## 7. Key insight

**Likelihood ranking is the format-immune measurement.** Under it the model
never generates; it only scores candidates. A gap that survives cannot be an
artifact of how the model talks. Together with the probe, this yields a clean
2×2:

| | Probe intact | Probe drops |
|---|---|---|
| **Likelihood gap ≈ 0** | O1 — format artifact, write the negative | (incoherent; investigate the instrument) |
| **Likelihood gap > 0** | **O2** — decoding-policy tax | **O3** — representation tax |

The second insight is that the **distractors must be shared** between the two
checkpoints. If each model ranks against its own candidate set, a likelihood
gap can come from an easier set rather than a better model. `make_pair` shares
them by construction.

## 8. Novelty statement

**VERIFIED PRIOR WORK.** MDGD (EMNLP Findings 2025) reports visual forgetting
under instruction tuning. TWIST & SCOUT (ICCV 2025) addresses grounding under
forget-free tuning. Both are close, and both must be cited as attacks rather
than as background.

**Gap (FACT, verbatim from `literature.md`):** *"Stage 3: stage-isolated
localization curve was NOT FOUND as a standalone paper (EVIDENCE GAP, conf
~0.5)."*

**This is an absence-defined novelty claim, and that matters.** The evidence is
that a search did not find the paper — confidence ~0.5, the lowest of the Final
3 — not that the paper cannot exist. `stage3_DE_top10.json.md` records E-009 at
**0.55** with the note *"matched checkpoint localization tax still open"*. An
absence claim decays: every week it is more likely someone else has filled it.
§26 treats this as the primary risk.

## 9. Relation to prior work (differentiation)

| Prior work | Status | What it establishes | Why it does not pre-empt us |
|---|---|---|---|
| MDGD | **VERIFIED PRIOR WORK**, EMNLP Findings 2025 | Visual forgetting under instruction tuning | Reports the phenomenon; does not isolate the stage, and does not control for output format. **Cite as an attack** |
| TWIST & SCOUT | **VERIFIED PRIOR WORK**, ICCV 2025 | Grounding under forget-free tuning | Proposes a *fix*. We diagnose *where the cost is*. A fix that works does not tell you which stage paid |
| RL-finetuned VLM robustness | **VERIFIED PRIOR WORK**, arXiv 2602.12506 | RL-tuning effects on VLM robustness | Adjacent and recent. Must be checked for scoop before writing |
| LLaVA / LLaVA-RLHF families | **VERIFIED PRIOR WORK**, 2023–24 | Candidate checkpoint pairs | Subject to GATE-B and licence review |
| Qwen-VL / Qwen-VL-Chat | `CITATION NEEDED — 待人工核验` | Candidate pair named in the experiment plan | Subject to GATE-B |
| RefCOCO | `CITATION NEEDED — 待人工核验` | Referring-expression benchmark | Evaluation data |
| DPO | `CITATION NEEDED — 待人工核验` | The H3 instrument | Method, not a claim |
| Grammar-constrained decoding | `CITATION NEEDED — 待人工核验` | Eval mode 2 | Tooling |
| Linear probing of frozen representations | `CITATION NEEDED — 待人工核验` | The H2 instrument | Standard method; formal citation unverified |

## 10. Significance — who is wrong if we are right

- **O2 (policy tax).** The capability survives alignment and is being suppressed
  at decoding. The fix is cheap — constrained decoding — and every paper
  reporting "aligned models are worse at grounding" from free-form generation
  has measured the wrong thing.
- **O3 (representation tax).** Alignment genuinely damages spatial features.
  The fix is expensive and belongs in training, and this is the more consequential
  finding.
- **O1 (format artifact).** The reported degradation is largely parsing. This is
  a **negative result and it should be written**, because the field is currently
  drawing training-time conclusions from a decoding-time problem.

Note the unusual property: **all three outcomes are publishable.** That is a
strength for the science and a weakness for prioritisation — it means the
project has no cheap kill, and the only real gate is GATE-B.

## 11. Method overview

1. **GATE-B**: verify a base/chat pair shares vision encoder and coordinate
   tokenization, with usable licences. No pair, no stage isolation.
2. Evaluate both checkpoints on referring expressions in three modes:
   free-form, grammar-constrained, likelihood rank against ≤16 **shared**
   distractors.
3. Fit a linear probe on **frozen** visual tokens → box, on a small train split,
   evaluated held-out, for both checkpoints.
4. Report parse-failure rate **separately** from IoU.
5. Classify O1/O2/O3 with the pre-registered decision function.
6. Only if the observational gap survives format control: the text-only DPO arm
   (H3).

Implementation: `src/aligntax/`. `pipeline.classify_outcome` is a pure function
of measurements with no model access, so it is unit-testable — and the smoke run
plants each of the four possible answers in turn and checks the function
recovers them.

## 12. Instruments

| Instrument | What it isolates | Guard |
|---|---|---|
| **Grammar-constrained decoding** | Removes the prose wrapper | Output always parses; verified by a self-check |
| **Likelihood ranking** | Removes generation entirely | Distractors **shared** across checkpoints |
| **Frozen-feature linear probe** | Whether the box survives in the representation | Ridge-regularised; an unregularised fit can recover a box from noise and would report "intact" for a destroyed representation |
| **Separate parse-failure reporting** | Talking too much vs. failing to localise | `mean_iou` offers both `count_failures=True` and `False`; the difference *is* the format tax, quantified |
| **Text-only DPO** (H3) | Objective vs. image data mix | Optional; gated on the observational gap surviving |

**The decision function refuses to classify without the likelihood mode.** That
is the kill rule expressed in code: a free-form gap alone cannot be separated
from the format confound, and the easiest way to publish a wrong result here
would be to skip mode 3 and report the gap anyway.

## 13. Null models & baselines

| Role | Method | Purpose |
|---|---|---|
| Reference | Base checkpoint, all three modes | The un-aligned comparison |
| Subject | Chat checkpoint, all three modes | |
| Format control | Same checkpoint, free-form vs constrained | Isolates the wrapper cost within one model |
| Representation control | Probe on both checkpoints, frozen | H2 |
| Causal control | Text-only DPO LoRA | H3 |
| Negative control | `tax_mode = "none"` in the harness | Everything downstream must come out null |

## 14. Datasets & checkpoints — and the gate that blocks everything

| Resource | Role | Status |
|---|---|---|
| A base/chat pair sharing vision encoder + coordinate tokenization | **Required** | **UNVERIFIED — GATE-B** |
| RefCOCO-style referring expressions, ~2k | Primary eval | `CITATION NEEDED — 待人工核验` |
| Synthetic pair (`data.make_pair`) | Harness validation only | Ships here |

> ### GATE-B — the precondition that keeps Idea_03 provisional
>
> **FACT.** `experiments.md` has always read *"**Hard gate:** identical vision
> encoder + coordinate tokenization"*. No Windows6 artifact records that any
> pair was ever checked.
>
> | Outcome | Consequence |
> |---|---|
> | A pair verified on all three counts (shared encoder, shared coordinate tokenization, usable licence) | Gate closes; proceed |
> | Encoder or tokenization differs | **Stage isolation is unavailable.** Any gap could be an encoder or tokenizer difference. Idea_03 descopes to a format-artifact study — a much smaller paper |
> | No usable pair at all | Idea_03 cannot run as specified |
>
> This costs hours reading model cards and configs, and no GPU. It is card
> **E-B** and it runs first.

## 15. Metrics & statistical analysis

**Primary:** IoU and accuracy@IoU 0.5 under each of the three modes; **top-1
rank accuracy** for the likelihood mode; **probe MAE** in pixels.

**Parse-failure rate is always reported separately.** Folding unparseable
outputs into the IoU mean as zeros is precisely what makes a chat model look
unable to localise when it is merely talking. The two failures need different
fixes and support different conclusions, so the package reports IoU both ways
and treats the difference as a measurement in its own right.

**The distractor set is shared** between checkpoints. Otherwise a likelihood gap
could reflect an easier candidate set.

**Thresholds.** `gap_tolerance` is pre-registered at 0.02 and applied by
`classify_outcome`, not chosen after seeing results. Bootstrap CIs over examples.

## 16. Killer experiment (run first)

Card **E-B** (GATE-B, no GPU), then card **E1**: one verified pair, ~2k
referring expressions, three eval modes, plus the probe. **≤8 GPU-h
(HYPOTHESIS**, from `experiments.md`; `evolution_summary.md` records ≈8 GPU-h
day-1). Eval-only — no training.

## 17. Full experimental program

| Card | Content | Budget (HYPOTHESIS) |
|---|---|---|
| E0 | Harness validation, O1/O2/O3 round trip, CPU | ~0 |
| **E-B** | **GATE-B checkpoint verification** | 0 — no GPU |
| E1 | Killer: pair 1, three modes + probe | ≤8 GPU-h |
| E2 | Pair 2 (replication) | ≤8 GPU-h |
| E3 | Probe-layer sweep and probe-capacity ablation | ≈2 GPU-h |
| E4 | **H3**: text-only DPO LoRA | 1–2 × 24 GB, days |

**STOP rule (FACT, verbatim):** *"STOP if likelihood gap ~0 on pair 1 and pair
2. Do not run DPO unless observational gap survives format control."* E4 is by
far the most expensive card and is gated behind E1 **and** E2.

## 18. Ablations & controls

- **Eval-mode ablation:** all three modes, always. The progression is the
  argument.
- **Parse-failure ablation:** IoU with and without failures counted.
- **Probe layer sweep:** the box may be recoverable at one depth and not
  another; reporting a single layer invites the "you probed the wrong layer"
  attack.
- **Probe capacity ablation:** linear versus a small MLP. If only the MLP
  recovers the box, the information is present but not linearly accessible —
  a distinct and reportable finding.
- **Distractor-count sweep:** 4, 8, 16. A gap that only appears at one set size
  is a property of the set.
- **Prompt-template ablation:** several templates. Alignment changes prompt
  sensitivity, and one template is one draw.

## 19. Expected results (all EXPECTED RESULT — nothing measured)

- **EXPECTED.** The free-form gap is the largest of the three; the constrained
  gap is smaller; the likelihood gap is smallest. That ordering is close to
  mechanical, which is why only the *third* number is decisive.
- **EXPECTED.** Parse-failure rate is substantially higher for the chat
  checkpoint — the most robust prediction here and the least interesting.
- **SPECULATION.** **O2** is the most likely outcome: the box survives in
  frozen features while the decoding policy has shifted. No evidence supports
  this beyond plausibility, and it is recorded so it can be shown wrong.
- **EXPECTED.** H3 is the hardest to obtain and the most attackable, since a
  small text-only LoRA may simply be too weak to reproduce anything.

## 20. Falsifiability & kill conditions

| Trigger | Action |
|---|---|
| No verified checkpoint pair | **Cannot run as specified** (GATE-B) — descope to a format-artifact study |
| H1 fails under constrained decoding | **KILL** — formatting confound, as pre-registered |
| Likelihood gap ≈ 0 on pair 1 **and** pair 2 | **STOP.** Write O1 as a negative result. Do **not** run DPO |
| Likelihood mode not run | **No verdict.** The decision function raises |
| Gap present but reverses across pairs | **KILL** the general claim; report as pair-specific |
| Probe result depends entirely on layer choice | **DOWNGRADE** — report the layer sweep, not a headline |
| MDGD or a concurrent paper already reports the stage isolation | **KILL or reposition** — see §26 |

### 20.1 What "kill" means here, and what it does not

O1 is a **kill of the hypothesis** but not of the output: `experiments.md` says
*"write negative"*. Reporting that a widely cited degradation is largely a
parsing artifact is a service to the field. What is **not** acceptable is
running only free-form evaluation, observing a gap, and reporting a tax.

## 21. Confounders & mitigations

| Confounder | Mitigation |
|---|---|
| Output format (the big one) | Three eval modes; likelihood is generation-free |
| Different vision encoders between checkpoints | **GATE-B.** No mitigation exists downstream — this is why it is a hard gate |
| Different coordinate tokenization | GATE-B |
| Unmatched instruction-tuning data mixes | Cannot be fixed observationally. **Do not claim causal RLHF without H3** |
| Probe capacity or layer choice | Layer sweep + capacity ablation |
| Distractor set difficulty | Shared distractors, plus a count sweep |
| Prompt template | Template ablation |
| Probe overfitting on a small train split | Ridge regularisation; held-out evaluation |

## 22. Reviewer #2 compliance matrix (binding)

| Attack (from `reviewer_attacks.md`) | Binding obligation | Where satisfied |
|---|---|---|
| Novelty of generic forgetting | **Cite MDGD**; claim only stage + format isolation | §8, §9 |
| Unmatched data mixes | **Do not claim causal RLHF without H3** | §21, E4 |
| Box parsing ≠ localization | Constrained decoding **and** probe | §12, E1 |
| Small N families | Honest scope; name the pairs in the title if only one | §23 |

**Residual obligation (FACT, verbatim from `stage4_reviewer2_cheap5.jsonl`):**
*"Needs format-controlled eval + representation probe + small text-only DPO
control."* Three conjuncts: cards E1 (first two) and E4 (the third).

## 23. Scope boundaries

- **Not** "alignment hurts vision" — published, and killed at Stage 3.
- **Not** a fix. TWIST & SCOUT proposes fixes; we diagnose.
- **Not** a claim about RLHF causality without H3.
- **Not** a broad multi-family survey. If one pair passes GATE-B, the title
  names that pair.
- **Not** a benchmark contribution.

## 24. Compute & resource budget

**All HYPOTHESIS.** Day-1 ≈8 GPU-h (`evolution_summary.md`); `proposal.md`
originally recorded eval-only as *"1 GPU, 1–2 days"*. The optional DPO arm is
*"1–2 × 24 GB, days"* and is the only expensive item — which is exactly why the
STOP rule gates it behind two pairs.

GATE-B and E0 need no GPU.

## 25. Reproducibility & release plan

- Seeds fixed via `config.set_seed`, returning an explicit `Generator`.
- **The decision function is pre-registered and released as code.**
  `classify_outcome` takes measurements and returns O1/O2/O3 with no model
  access, so a reader can apply our rule to their own numbers.
- `Config` rejects unknown keys and validates `tax_mode`.
- `tests/test_smoke.py`: 27 self-checks, numpy only.
- Release: eval harness, prompt templates, the shared distractor sets, probe
  code, per-example scores.

## 26. Risks & mitigations — concurrent work first

| Risk | Severity | Mitigation |
|---|---|---|
| **Concurrent work** | **Highest in Windows6** | See below |
| GATE-B fails | High | Check first; costs hours |
| Data-mix confound blocks causal claims | High | H3, or drop the causal framing |
| Probe result is layer-dependent | Medium | Layer sweep; downgrade to a sweep report |
| DPO arm too weak to show anything | Medium | Pre-declare it as optional; H1+H2 stand alone |
| Licences block the comparison | Medium | Part of GATE-B |

### 26.1 The concurrent-work risk, treated as a schedule constraint

**FACT, three independent records point the same way:**

1. `stage3_DE_top10.json.md`: E-009 keep confidence **0.55** — the lowest of the
   Final 3 — with the note *"matched checkpoint localization tax still open"*.
   *Still open* is a statement about the field, and it has a shelf life.
2. `literature.md`: the gap is an **EVIDENCE GAP at confidence ~0.5** — a search
   that did not find the paper, not proof it does not exist.
3. `Windows6/README.md`: *"Highest impact, highest concurrent-work risk."*

**Why the exposure is structurally high.** The experiment is cheap
(eval-only, ≤8 GPU-h), needs no new data, needs no training, and uses public
checkpoints. Everything that makes it attractive to us makes it attractive to
everyone else. The novelty is defined by an absence, and absences close.

**Mitigations, in order:**

- **Run E-B and E1 first.** The gap is only defensible while it is open. This is
  the reason Idea_03 should not be scheduled after Idea_01 and Idea_02 despite
  being ranked third for tractability.
- **Re-check MDGD, TWIST & SCOUT and arXiv 2602.12506 for updates immediately
  before writing.** The last is recent enough that a v2 could contain this.
- **Preserve a fallback contribution.** If the stage-isolation claim is scooped,
  the pre-registered O1/O2/O3 decision procedure and the format-controlled
  protocol remain a methods contribution — *how to measure this correctly* —
  which is not scooped by someone reporting a number.

**Honest limit.** None of these reduce the probability of being scooped. They
reduce the cost of it. There is no mitigation for an absence-defined claim other
than speed.

## 27. Ethical & data considerations

Public checkpoints under their own licences; licence compatibility is part of
GATE-B. No new data is collected. The finding concerns model capability
measurement, not deployment safety, and must not be presented as evidence that
alignment is harmful in general — the scope is coordinate emission on referring
expressions, and nothing broader.

## 28. Deliverables & decision tree

**Deliverables.** Analysis paper; the format-controlled eval harness; the
pre-registered O1/O2/O3 decision function; shared distractor sets.

```
E-B GATE-B  ──no verified pair──> descope to a format-artifact study
   │pair verified
E0 harness  ──round trip fails──> fix the decision logic (never a conclusion)
   │pass
E1 pair 1   ──H1 fails under constrained decoding──> KILL (format confound)
   │         ──likelihood gap ~0──> provisional O1
   │gap survives
E2 pair 2   ──likelihood gap ~0 here too──> STOP. Write O1 as a negative.
   │         ──gap reverses across pairs──> KILL the general claim
   │gap replicates
   ├─ probe intact ──> O2 policy tax
   └─ probe drops  ──> O3 representation tax
   │
E4 DPO      (only if the gap survived format control on BOTH pairs)
   └─> causal claim about the objective, or H3 dropped and O2/O3 stands alone
```

**Candidate titles.** *Which Stage Costs the Box?* · *Format-Controlled
Localization Tax in Aligned VLMs* · *The Box Is Still There: Probing Localization
After Alignment*
