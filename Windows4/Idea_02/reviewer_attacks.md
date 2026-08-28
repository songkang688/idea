# PromptAmnesia — Reviewer Attack Ledger (Windows4 / Idea_02)

**Epistemic status:** REVIEW JUDGMENT. Part I reproduces the binding Stage-4 Reviewer #2 attacks
(`selection_history/stage4_r2_setB.md`) with the design elements that answer them. Part II contains
**new anticipated attacks** raised at Stage 7 against our own design, each with its silencing experiment
or an honest concession. No experimental result is claimed.

Rule in force: a WEAK ACCEPT is conditional — dropping any listed obligation reverts the verdict to REJECT.

---

## Part I — Inherited Stage-4 attacks and contracted answers

### A1. "Coverage, not forgetting" (P065 core attack)

> *"Models degrade on the prompt modes they were not fine-tuned with. That is train/test
> prompt-distribution mismatch — a data-coverage statement, not forgetting — and MedSAM already
> demonstrates it."*

**Contracted answer.** The FT-prompt-mix factorial (box-only / point-only / mixed). All forgetting claims
are licensed **only by the mixed column**, where every evaluated prompt type appeared during fine-tuning.
Box-only and point-only columns quantify the coverage effect as a separate deliverable (RQ5).
**Status if the ordering vanishes in the mixed column:** the forgetting claim dies; the coverage map is
the salvage report (proposal §23 Branch C). No re-framing permitted.

### A2. "Diversity collapse is a loss-aggregation artifact" (C1-061 attack)

> *"Standard recipes disable multimask or backprop only the min-loss mask; post-FT diversity collapse is a
> mechanical consequence of the loss-aggregation choice."*

**Contracted answer.** All-mask-loss + multimask-enabled FT arms in the mixed column; the oracle-best-of-3
vs argmax decomposition (binding). If oracle survives and only argmax moves → the finding transfers to
P031 and is withdrawn here. If collapse appears only under min-loss-mask → reported as a recipe artifact.

### A3. "Threshold artifact masquerading as forgetting" (C1-082)

**Contracted answer.** P082 runs first; symmetric per-domain threshold tuning on a shared calibration
split for frozen and fine-tuned models alike; every headline delta compared against the pre-registered
noise-floor envelope. Asymmetric threshold access is treated as leakage on either side.

### A4. "Matched gain is under-specified and a single point of failure"

**Contracted answer.** One pre-registered rule (proposal §14), used verbatim by P065/P031/P082-plasticity/
P177; tolerance sensitivity (±0.25 / ±0.5 / ±1.0) pre-registered; excluded arms enumerated.

### A5. "Seed and prompt-sampling variance swamp the claimed ordering gaps" (C1-060)

**Contracted answer.** ≥3 seeds per cell (≥5 headline if the envelope is wide); hierarchical bootstrap
over images and seeds; Holm correction over the pre-registered contrast family O1–O5; the envelope
condition is conjunctive with significance.

### A6. "The splice conflates forgetting locus with interface incompatibility" (P177 core attack)

> *"If interfaces drift, a failed splice does not mean forgetting is distributed and a successful splice
> does not mean it is localized; chimera behavior is dominated by representational mismatch (Bansal et
> al.)."*

**Contracted answer (binding since P177 is included).** Every swap cell run with and without a trained
affine stitch; stitch-only calibration cells; both swap directions; per-module α-interpolation as the
continuous baseline. The locus claim requires module-separable restoration **beyond** what stitches and
α-curves explain.

### A7. "Locus is a recipe tautology — the decoder got the update, so the decoder 'forgot'"

**Contracted answer.** Per-module update-norm logging across the grid + one update-norm-matched
fine-tuning arm. Locus statements are conditioned on the norm accounting.

### A8. "Reimplementation strawman (banned pattern F8)" (P082 attack)

**Contracted answer.** Named indictments use released checkpoints only (MedSAM, SAM-Med2D at minimum),
re-run under their published protocols first, symmetric protocol second, both reported.
Re-implementations appear only as unnamed sensitivity checks.

### A9. "SAM-Med2D already published the prompt-mode table"

**Contracted answer.** Their table lacks: matched gain, mixed-vs-box-only factorial, negative clicks,
click-depth curves, diversity decomposition, seeds/CIs, threshold symmetry, and a noise floor. The delta
is the *structure* of the comparison, not the existence of a table. This must be stated with the table
reproduced in related work — not hidden.

### A10. "If the audit finds forgetting exceeds the floor, P082 is a confirmation note"

**Contracted answer (accepted, by design).** P082 is a gate, not a standalone paper, in that branch: its
envelope becomes the reference band of every P065 figure, and the deflation framing is dropped. Only in
the PIVOT branch does P082 become the paper.

---

## Part II — New Stage-7 attacks against our own design (anticipated), with answers

### B1. "Your mixed-FT distribution is arbitrary; a different mix yields a different ordering"

**Threat.** The 1/3-1/3-1/3 mixed distribution is a free parameter; reviewers can claim the observed
mixed-column ordering is an artifact of the chosen mix.

**Silencing experiment.** One perturbed-mix replication cell (e.g., 50/25/25) on the headline domain ×
recipe × 3 seeds. If the ordering's sign is stable across the two mixes, the attack is silenced; if not,
the claim is scoped to "mix-dependent" honestly. ESTIMATE +2–3 GPU-days. Pre-registered as a robustness
cell in `configs/shared_grid.yaml`.

### B2. "COCO is not zero-shot for SAM-family models"

**Threat.** SA-1B-era models may have seen COCO-like imagery; "zero-shot retention" is contaminated.

**Answer (concession + design).** All retention deltas are **relative to frozen SAM under the identical
protocol** — the floor absorbs any absolute contamination. We never claim absolute zero-shot performance;
we claim *change* relative to the frozen floor. Stated as an explicit scope limitation.

### B3. "Ambiguity probes mined from COCO/LVIS encode annotation conventions, not real ambiguity"

**Threat.** Nested-pair mining may select annotation quirks; oracle-vs-GT IoU then measures convention
matching.

**Silencing experiment.** (a) Human spot-audit of a random probe subsample (accept/reject each probe as
genuinely ambiguous; report acceptance rate); (b) replication of the O4 contrast on the probe subset that
passed audit. If O4 holds on the audited subset, silenced. Cheap (annotation-hours, not GPU).

### B4. "Your click simulator choice determines the iterative-column results" (RClicks-class attack)

**Answer (contracted in E3).** Dual-simulator duplicate of every headline contrast; simulator-dependent
contrasts demoted to limitations. Additionally the simulator code is pre-registered and frozen at E0.

### B5. "Two medical FT domains cannot support 'promptable segmenters forget non-uniformly' in general"

**Answer (scope control).** Claims are scoped to "SAM-class models fine-tuned on medical 2D domains" —
the setting where the fix literature lives. The natural→natural fine-tuning generalization is listed as
explicit non-claimed territory. If budget allows, one natural-domain FT cell (e.g., a COCO-subset
fine-tune) is a pre-registered optional extension, not a promise.

### B6. "Envelope built on frozen-model variance understates fine-tuned-model variance"

**Threat.** Fine-tuned checkpoints may have higher eval variance than the frozen model; an envelope from
frozen-model replicates is too narrow, biasing toward PROCEED.

**Silencing experiment.** Compute the same variance decomposition on ≥2 fine-tuned released checkpoints
(prompt-seed and split replicates are eval-only); take the per-cell max of the two envelopes as the
operative band. Pre-registered in `configs/p082_gate.yaml` (`envelope: max_of_frozen_and_ft`).

### B7. "Matched-gain excludes the most aggressive arms — survivorship bias"

**Threat.** Arms that overshoot G\* quickly might be exactly the arms with the worst forgetting; excluding
never-reaching arms could bias the other direction.

**Answer.** The rule never excludes overshooting arms (first checkpoint within band exists for them); only
arms that never reach G\*−0.5 are excluded, and these are enumerated with their full retention curves in
the appendix, plus the tolerance sensitivity re-runs. Concession: if a whole recipe class is excluded in a
stratum, matched comparisons for that stratum are labeled partial.

### B8. "Stitch capacity is a tunable knob; you can make either locus verdict happen"

**Threat.** Affine-vs-1×1-linear stitch choice changes restoration fractions; garden of forking paths.

**Answer.** Stitch family and capacity are fixed at E0 (per-channel affine primary; 1×1 linear as the
single pre-registered secondary); stitch-only calibration cells quantify stitch power; verdicts require
the module separation to hold under **both** stitch families.

### B9. "This is four papers stapled together"

**Answer.** The gate and mechanism arms are not stapled — they are epistemically load-bearing: without the
envelope, orderings are uninterpretable (A3/A5); without the splice, the ordering has no causal anchor
(A6). P031 is explicitly a *separate* sibling paper consuming the same grid. The paper's single thesis is
the four-way disambiguation of "zero-shot Dice dropped" (proposal §4).

### B10. "You will be scooped between freeze and submission"

**Answer.** Scoop-watch queries (`literature.md` §6) run at E0 and pre-submission; fallback branches
(deflation; mechanism-led) are pre-registered so a partial scoop re-scopes rather than kills. Residual
risk accepted and stated.

---

## Verdict discipline

This package inherits: **P065 WEAK ACCEPT · P177 WEAK ACCEPT · P082 WEAK ACCEPT (run first) — all
conditional.** Part I obligations are contract; Part II items B1, B3, B6, B8 are additionally adopted as
pre-registered design elements at Stage 7. Any future drop of an obligation must be logged in
`roadmap.md` with the corresponding claim withdrawn, per the reversion rule.
