# Windows7 — Eliminated Ideas

What died, at which stage, and which ones deserve to come back.

---

## Where the losses happened

| Stage | In | Out | Killed | Dominant cause |
|---|---|---|---|---|
| 2 | 1,110 | 255 | 855 | no scientific question — "add a module", "apply X to Y" |
| **3** | 255 | 52 | **203** | **prior work already covers the mechanism** |
| 4 | 52 | 21 | 31 | central attack has no affordable experimental answer |
| 5 | 21 | 5 | 16 | cost-per-decision too high |
| 6 | 5 | 3 | 2 | portfolio overlap and confound |

**Stage 3 is where research ideas actually die.** Four out of five survivors of independent review
turned out to have their core mechanism already published — usually under a different name, often in
an adjacent subfield that the originating agent had not searched.

---

## Stage 2 — the 855

Almost entirely ideas with no falsifiable claim. The recurring shapes:

- **Module stacking.** "SAM + Mamba", "cross-attention between the two branches", "add a boundary
  refinement head." No hypothesis, so no possible negative result.
- **Transplants.** "Apply method X to medical images." A paper only if the transplant fails
  informatively, and none of these said what failure would look like.
- **Loss and backbone swaps.** An ablation, not a project.
- **Underspecified ambition.** "Make segmentation robust to domain shift." Not a question.

The filter: *what result would prove this wrong?* An idea that cannot answer that in one sentence did
not advance.

---

## Stage 3 — the 203 · representative kills

| Idea | Killed by |
|---|---|
| Uncertainty-aware SAM prompting for ambiguous boundaries | Multiple published prompt-uncertainty methods; the proposed mechanism was one of them |
| PEFT rank allocation by layer sensitivity | AdaLoRA and successors; the "insight" was the published method |
| Synthetic smoke data with physically-based rendering | Existing synthetic smoke corpora, same rationale |
| Cross-modal distillation for transparent objects | Adjacent-field work under a different name |
| Test-time adaptation for medical segmentation shift | Crowded; no remaining differentiator |

**Mutated rather than killed** — the productive path, and the one both top finalists took:

- A method idea about *fixing* SAM2 memory → **A-0017**, which measures whether memory is the problem
  at all. The fix was taken; the measurement was not.
- A method idea about *improving* few-shot support encoding → **B-0121**, which asks whether the
  support is being used. Same move.

The pattern is worth naming: **when the method is taken, check whether the measurement is.** It
usually is not, because measuring is less rewarding to publish than proposing.

---

## Stage 4 — the 31

Killed by attacks with no affordable experimental answer:

- **Unremovable confounds.** Most often extra parameters, extra data, or extra compute doing the work
  the proposed mechanism claimed.
- **Nonexistent baselines.** The honest comparison required a model nobody released.
- **Metrics that cannot separate the hypothesis from the trivial alternative.** If the proposed
  mechanism and "the model got slightly better at everything" produce the same numbers, there is no
  experiment.

---

## Stage 5 — the 16

All scientifically defensible; all too expensive per decision. Typical: a full pre-training run
required before *any* signal, or a labelling effort with no public substitute.

`KNOWN FACT` Several of these become viable at a different budget. They are cost casualties, not
scientific ones, and the distinction should be preserved if this pool is revisited.

---

## Stage 6 — the final two

### C-0028 — the decision triple

Well-designed and genuinely interesting. Cut for **territory overlap with C-0090 at higher cost**:
both probe multimodal fine-tuning dynamics, and C-0090's content-free grid was judged the sharper
instrument for a similar budget.

**Revival condition:** if C-0090 fails its power gate at E1 — the outcome we consider most likely —
C-0028 is the natural successor and inherits the harness, the eval configs and the pre-registration
discipline. The E1 failure would also be *evidence about* C-0028's premise, so the revival would
start better informed than the original.

### A-0044 — temporal calibration

Cut because the calibration claim could not be separated from a difficulty confound within budget.
The partial-correlation machinery built for A-0017's validity test is exactly what it needed, and did
not have.

**Revival condition:** after A-0017 completes. The comparator infrastructure and the partialled
validity design transfer directly, which changes the cost calculation that killed it.

---

## Ideas considered for revival and not revived

The meta-auditor reviewed the Stage-3 kill list for high-risk / high-reward ideas eliminated too
readily, and revived none.

**Reasoning:** the Stage-3 kills were mechanism-level rather than framing-level. When only the framing
was dead, the idea was **mutated in place** rather than eliminated — which is how both B-0121 and
A-0017 reached the final. There was no residual pool of wrongly-killed ideas to draw from.

**Caveat, recorded honestly.** The auditor also flagged a convergence bias: reviewers increasingly
favoured measurement projects as the round progressed, and all three finalists are measurement
projects. The audit could not name a specific method idea that was wrongly killed, so no revival
followed — but the bias is real, and a future round should seed at least one method-side idea into
Stage 5 deliberately rather than letting selection pressure decide.
