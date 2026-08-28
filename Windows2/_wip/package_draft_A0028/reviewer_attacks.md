# A-0028 — Reviewer #2 Attacks and Residual Risks (Sections 23–24 of 28)

This idea has survived **four kill attempts across three battles** (Stage-6 O Round 1–2, Q Round 2,
S Round 5) plus the mandatory built-in Reviewer-2 pass at Stage 5. The attacks below include every
attack actually lodged in the pipeline record (with its adjudication) plus the packager's fresh pass.
Labeling per `proposal.md` Section 10.

---

## Section 23 — Reviewer #2: attacks and answers

### A1 (THE attack): "The fix-papers already exist. DAM4SAM found the drift, built the fix, and won
### benchmarks with it. SAMURAI even states the appearance-priority claim in print. What is left?"

**Status: lodged and defeated three separate times (Stage-5 N, Stage-6 Q Fight 2, Stage-6 S Round 5
Part B). The answer, consolidated:**

1. **They document a phenomenon and ship interventions; none measures the arbitration.** DAM4SAM's
   evidence is benchmark deltas + drift anecdotes; its DiDi dataset makes distractor scenes *frequent*
   but contains no controlled displacement/gap/similarity manipulation. SAMURAI's claim sentence
   ("SAM 2 tends to prioritize appearance similarity over spatial and temporal consistency") is
   supported by two qualitative failure cases (its Fig. 1) — an anecdote motivating a Kalman bolt-on,
   not a measurement (adjudicated at Stage 6: citation obligation, not scoop). The memory-design study
   (arXiv:2512.22624) varies memory designs and reports ten-benchmark aggregates — never isolating the
   arbitration variable.
2. **Three fix-papers presupposing the quantity is the motivation, not the refutation.** Each fix
   intervenes on appearance-vs-location arbitration from a different philosophy (curate appearance
   memory / add explicit motion prior / partition by function). Interventions on an unmeasured
   quantity can only be A/B-tested end-to-end — which is exactly what all three do. We measure the
   quantity. The introduction writes itself from their own presuppositions.
3. **The fixes even disagree with each other about the direction of the failure** — SAMURAI says
   appearance dominates; the location-prior worry (and the folklore DAM4SAM's drift anecdotes feed)
   says place-stickiness pollutes memory. The probe adjudicates a disagreement the fix-papers don't
   know they are having (H4 dissociates the two fix philosophies behaviorally).
4. **The fixes become subjects.** DAM4SAM and SAMURAI enter the study as models under test (E6) — the
   probe is the evaluation instrument their own ablation tables lack. A fix-paper cannot scoop the
   instrument that evaluates fix-papers.

### A2: "Adversarial off-manifold stimuli — you built teleports for a model never trained on cuts.
### Of course it fails."

**Status: lodged at Stage-6 O Round 2 and S Round 4 (SEG); answered; the answer is BINDING on the
package (both arms non-optional).**

- The **natural hard-cut arm** (E7) exists precisely for this: shot cuts where objects genuinely
  relocate are ubiquitous in deployed video (broadcast, multi-camera, edited footage, medical cine).
  If synthetic curves predict natural-cut behavior (H5), the manifold objection is empirically closed;
  if they don't, the pre-registered PIVOT re-scopes to natural-cut-only (`roadmap.md` Section 26) —
  the objection is priced either way.
- The **DiDi anchor** ties the battery to an external, community-built distractor benchmark.
- And note the asymmetry: if the appearance-dominance branch fires, the "of course it fails" premise
  is empirically false — the model *doesn't* fail, which is the pre-registered corrective finding.

### A3: "Your probe measures paste artifacts, not arbitration."

**Status: anticipated at Stage 5; the placebo arm is the control; MEASURED (synthetic surrogate)
evidence that the readout can come back clean: placebo disruption 0.000 in the committed prototype
run.** The real-model placebo is gate V of the killer battery and runs FIRST; Wilson-upper-bound
< 0.05 required before any swap trial is interpreted. If gate V fails and compositing cannot be fixed,
the pre-registered verdict is KILL — the probe's own validity criterion is stated in print
(`experiments.md` Section 20).

### A4: "A synthetic surrogate proves nothing about SAM2."

**Correct, and the package says so everywhere it could possibly be misread** (labeling rule,
`proposal.md` Section 10). The surrogate's role is *instrument validation*, which is standard
measurement methodology: before pointing an instrument at an unknown system, show it recovers ground
truth on a system where ground truth is known (MEASURED: Spearman ρ = 1.000 λ-recovery; dummy
brackets 0.892 / 0.030; placebo 0.000). No SAM2 number exists in this package; H1–H5 are labeled
HYPOTHESIS until E1 lands.

### A5: "This is one ablation row, not a paper. The next memory paper prints a teleport row and
### absorbs you."

**The absorb risk — the real one (Section 24, R1).** Answers: (i) the contribution is a validated
instrument + psychometric law + generational comparison + fix evaluation + mechanism ablation — a row
in someone's table reproduces none of that; (ii) the mitigation is *speed*: killer battery in week
one (binding), arXiv preprint immediately after the natural-cut arm confirms (roadmap M3); (iii) the
pre-registered scoop criterion distinguishes a controlled (d, g, s) probe (KILL) from a gesturing
ablation row (citation) — we do not die to a table row, and we do not pretend a real probe isn't one.

### A6: "Your trichotomy thresholds (0.5/0.1 IoU) are arbitrary."

Pre-registered threshold-sensitivity appendix (`experiments.md` Section 19): full battery re-scored
at 0.3/0.5/0.7; headline claims must be threshold-stable or they are not made. The dummy brackets
also calibrate the scoring geometry per cell (the location dummy's 0.892 — not 1.0 — is itself a
scoring-geometry measurement, MEASURED on the surrogate).

### A7: "Why psychophysics language? It's inference on composited clips, not a psychology study."

The borrowed discipline is methodological, not rhetorical: controlled stimulus grids, placebo
controls, psychometric-function fitting with goodness-of-fit (Wichmann & Hill 2001), bracketing
dummies. Precedent exists for controlled behavioral probing of trackers (object-permanence line,
arXiv:2003.10469). The paper uses the framing exactly as far as the methodology carries it and no
further (no claims about "perception").

### A8: "SAM-family relevance is cooling; by publication this measures last year's model."

SAM3 shipped 2025-11 and the memory-design conversation moved to it within weeks (arXiv:2512.22624);
the probe is architected model-agnostically (any promptable memory tracker is a subject — the
adapter interface is one `track(frames, prompt)` call). The instrument outlives any single subject;
each new memory design is a new row for the instrument, not a threat to it.

### A9: "Frame-dropping for gap g is not 'temporal sparsity'; real low-FPS video has motion blur and
### exposure differences."

Scoped honestly: g is *observation sparsity* (memory staleness), the quantity the memory designs
actually manipulate (memory selection/retention policies), not a camera model. Natural-cut clips
carry real photographic discontinuities and anchor the claim (E7). The limitation is stated in print.

### A10 (Stage-5 leftover, kept on the books): "This diagnoses; DAM4SAM fixes. Constructive gap."

Position as the measurement instrument the fix-papers lack — their ablations report benchmark deltas,
not arbitration mechanisms (Stage-5 adjudication, carried into the battle-locked claim). The
instrument-evaluates-fixes arm (E6) is the constructive payload: it tells the next memory designer
*which direction and how far* their policy moved the arbitration, per condition. The portfolio's
constructive-method quota is carried by C-0306 (Idea_01), by design; this seat is the capability
instrument.

## Section 24 — Residual risks and mitigations

| # | Risk | Class | Likelihood / trend | Mitigation (pre-registered where applicable) |
|---|---|---|---|---|
| R1 | **Absorb**: a busy ablation table elsewhere prints a teleport-shaped row before we execute | scoop | climbing — three fix-papers at battle-lock, a **fourth** (SAMITE, arXiv:2507.21732) found at packaging (`literature.md` §12 addendum); niche prints roughly quarterly | week-one killer battery (BINDING); scoop re-search at experiment freeze + submission; written kill-vs-citation criterion (`roadmap.md` §26 C2/K1) |
| R2 | **External validity**: synthetic-cut behavior fails to predict natural-cut behavior | scientific | genuine unknown — THE scientific risk | PIVOT pre-registered: re-scope to natural-cut-only with smaller factorial grid (§26 P1); curation starts day 5 in parallel, not after |
| R3 | **Unsystematic SAM2-L behavior**: no curve to characterize | scientific | low (some structure near-certain; the surrogate shows the readout has dynamic range) | STOP branch: report the instability itself, one short note (§26 S1) |
| R4 | **Placebo gate fails**: compositing artifacts disrupt tracking | engineering | low-moderate; Poisson blending + seam QA in the generator | placebo runs FIRST; iterate compositing; if unfixable → KILL (§26 K2) — stated in print |
| R5 | SAM3 video-API friction (concept-prompt-first design; visual-prompt video mode integration) | engineering | moderate | SAM3 Tracking Zoo as fallback harness; E5 is fan-out, not gate — killer battery never waits on SAM3 |
| R6 | Comparator repro (DAM4SAM/SAMURAI configs drift from papers) | engineering | low | official repos, pinned commits, config hashes in results JSON; zoo re-implementations cross-checked against official where both exist |
| R7 | Natural-cut curation cost creep | schedule | low — bounded scope (dozens/bin, ~100 clips) | fixed curation budget; DiDi anchor is the zero-cost backstop |
| R8 | Model-relevance cooling (SAM-family attention fades) | positioning | low near-term (SAM3 is months old) | model-agnostic adapter; instrument framing (A8) |

**Named replacement seat** (portfolio-level, from Stage-6): if this seat dies at a gate (K1/K2),
B-0194 (+B-0169) is the first replacement — recorded in `stage6_agent_S/why_not_the_other_two.md`;
that decision belongs to the PI, not this package.
