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

## Stage 6 — the two dropped from the locked Top 5

Neither was killed on validity, and both keep funded footholds.

### A-0061 — Boundary Nyquist

A second pure-measurement paper, with the **lowest ceiling in the Top 5**: its strongest possible
outcome is negative design advice. It also had the weakest cross-cluster legitimacy under the
auditor's asymmetric-standards finding.

**Cut on genre and ceiling, not validity.** Kept as an **idle-cycle rider** (~15–20 GPU-h), so it
runs whenever the node is otherwise free.

### B-0212 — blending-artifact transfer-gap law

Lost the slot on **portfolio arithmetic, not merit**. Only one Cluster-B slot existed, and B-0121
dominates it roughly **9× on cost-to-decision** while covering the same evaluation-validity axis.

**Compensation, already funded:** B-0212's **3-arm MVE (~6 A100-days, including the probe sanity
gate) runs now**, making it the immediately promotable second alternate and preserving the
intervention-law lane. It is the designated successor on **two** separate rungs of the fallback
ladder.

---

## What was actually revived

Two revivals, both driven by the meta-auditor's finding that the locked Top 5 was
**measurement-tilted**.

### A-0017's method arm — from optional to mandatory

Not a new idea but a **restored scope**: the training-free memory-surgery wrapper, benchmarked
head-to-head against SAMURAI and DAM4SAM, was elevated from optional secondary analysis to a required
deliverable. The audit was explicit that this is a real scope change and the package must budget the
comparison runs — it is now E9 in `Idea_02/experiments.md`.

This is why the Final 3 is not three measurement papers.

### C-0028 — decision triple, revived to funded first alternate

Its **zero-GPU offline dry-run gate** (H-arm constructibility: KS < 0.05 similarity matching plus
noun-rate checks on 10K generated batches) runs immediately, so a fully de-risked training-recipe
flagship is on the shelf before it is needed.

**Deliberately not co-picked with C-0090:** two VLM-training studies sharing eval infrastructure
would recreate monoculture in the opposite direction. C-0090 won the single training slot on being
2.2× cheaper with zero feasibility gates remaining.

**Promotion condition:** C-0090 dying at its power gate — the outcome we consider most likely. By
then C-0028's offline gate has already passed, and the E1 failure is itself *evidence about* C-0028's
premise, so the promotion starts better informed than the original nomination.

---

## The bias that was flagged and not fully fixed

`KNOWN FACT` The audit documented that **no METHOD-genre paper reached nominee grade anywhere in the
funnel** — an extinction, not a close call. Interim exposure is A-0017's mandatory method arm plus
the B-0112+M4 Leg-1 rider.

The recommendation attached to it: **re-instruct the Stage-1 generators for the next window** so this
does not become a three-peat. Seeding method-side ideas deliberately is a better fix than hoping
selection pressure produces one.
