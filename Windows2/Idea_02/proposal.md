# A-0028 — Stage-7 Research Package: Proposal (Sections 1–10 of 28)

**Package:** Windows2 / Idea_02 (PI final ranking #2) — DRAFT under `_wip/`, to be copied to
`Windows2/Idea_02/` by the PI.
**Idea ID:** W2-A-0028 — the SAM2/SAM3 teleport probe (appearance-vs-location arbitration).
**Genre seat:** capability instrument (SAM/video seat of the final 3).
**Seat record:** seated 8–0 (four kill attempts failed across three battles), ranked #2 (6–2).
**Upstream sources (binding):** `Windows2/_wip/stage5_agent_N/exp_07.md` (protocol),
`Windows2/_wip/stage6_agent_Q/top5.md` (battle-locked form), `Windows2/_wip/stage6_agent_S/final3.md`
(#2 section + packager handoff), `Windows2/_wip/stage7_proto_A0028/` (runnable synthetic prototype),
`Windows2/_wip/PI_BINDING.md` (revive mandate).

This package is written per the Stage-6 handoff to **absorb an already-completed week-one killer
result**: every results table in `experiments.md` carries an explicit RESULT SLOT, and the paper body
(Section 27) is structured around the multi-model extension (SAM3 generational comparison,
DAM4SAM-as-instrument), not around the single SAM2-L battery.

---

## Section 1 — Candidate titles

Ranked; 1–3 are the Stage-6 battle-locked seeds, 4–5 are packager additions.

1. **"Teleport: Does SAM2 Memory Follow the Object or the Place?"** — leads with the probe; best if
   the SAM2-L battery lands the monotone arbitration curve.
2. **"An Arbitration Law for Video Memory: Appearance versus Location in SAM2 and SAM3"** — leads
   with the law + generational comparison; best if the full multi-model study runs to completion.
3. **"Measuring What the Distractor-Memory Fixes Presuppose: A Psychophysics Probe for Segmentation
   Trackers"** — leads with the wedge against the fix-paper line; best for a rebuttal-heavy venue.
4. "Follow the Object or Follow the Place? Teleport Probes for Memory-Based Video Segmentation" —
   neutral fallback covering both pre-registered outcomes.
5. "The Teleport Test: Psychometric Curves for Appearance–Location Arbitration in SAM-Family Memory"
   — instrument-first framing if the appearance-dominance branch fires (SAM2 never follows the place).

Title selection rule: decided **after** the killer battery, by which branch of the Section-7
interpretation table fired. Titles 1–2 presume the location-prior branch; title 5 presumes the
appearance-dominance branch; titles 3–4 are branch-neutral.

## Section 2 — Battle-locked claim and provenance

**Claim (battle-locked at Stage 6, citation set updated; verbatim from `final3.md`):**

> The distractor-fix papers (DAM4SAM arXiv:2509.13864; SAMURAI arXiv:2411.11922; SAM2/SAM3
> memory-design line arXiv:2512.22624) presuppose an appearance-vs-location arbitration nobody has
> measured — teleport probes measure it directly on SAM2 AND SAM3.

Provenance chain: Agent A original (C02 cluster) → Agent F keep ("among the best of C02": ROI 5,
feasibility 5, cheap-falsify, counter-intuitive) → missed F's top-20 → Agent L revive #3 (only
surviving SAM2-video candidate; PI_BINDING mandated a slot) → Agent N exp_07 (protocol + fresh
scoop-check that produced the "fix-papers presuppose" reframing) → Agent O top20 #6 → Agent Q top5 #3
(third kill attempt failed) → Agent S final3 #2 (fourth kill attempt — SAMURAI — failed; week-one
execution upgraded to load-bearing) → PI ranking: **Idea_02**.

Binding conditions this package must encode (Agent S handoff, all honored):

- Written to absorb an already-completed week-one killer result. ✅ (RESULT SLOTS throughout.)
- SAM3 and DAM4SAM as subject models; the probe doubles as a memory-design evaluation instrument. ✅
  (`experiments.md` Section 17, E5/E6.)
- SAMURAI joins the presupposing-fix-papers citation set. ✅ (`literature.md` Section 12.)
- Placebo-paste validity arm and natural-cut external-validity arm are **non-optional**. ✅
  (`experiments.md` Sections 16, 21 — E4 and E7 are gates, not options.)
- Scoop re-search at experiment freeze. ✅ (`roadmap.md` Section 26, clock C2.)

## Section 3 — Executive summary

When a tracked object and a look-alike distractor exchange positions between frames — a "teleport" —
a memory-based video segmenter must decide: follow the appearance to the new place, or follow the
place and adopt the impostor? Every SAM2-era distractor fix (DAM4SAM's distractor-resolving memory,
SAMURAI's motion-aware memory selection, the SAM3-era unified memory framework) is an intervention on
exactly this arbitration — yet no paper has measured the arbitration itself. The fixes are evaluated
by benchmark deltas, which confound the arbitration with everything else in the pipeline.

We propose the **teleport probe**: a controlled behavioral battery that measures
P(follow-place | displacement d, temporal gap g, distractor similarity s) as a psychometric function,
per model. Composite clips built from real image crops (Poisson-blended cut-paste) sweep the
(d, g, s) grid; a paste-without-teleport **placebo arm** controls for compositing artifacts; a
curated **natural hard-cut arm** (~100 clips) controls external validity. Prompt on frame 0; at the
swap frame, score the predicted mask against object-at-new-location vs occupant-of-old-location →
per-trial trichotomy (follow-object / follow-place / other-or-lost); fit the psychometric surface and
summarize each model with a scalar **location-prior index**.

The killer experiment is **one GPU-day**: SAM2-L on the full synthetic battery (~10⁴ short clips).
Both outcomes are pre-registered findings: a monotone location-prior law (the arbitration law the fix
papers presuppose) or near-ceiling appearance-following (a controlled corrective to the drift
folklore the fix-paper line is built on). The full study (3–5 GPU-days) extends to SAM2 sizes, SAM3
(generational comparison), and DAM4SAM/SAMURAI as fixed-memory comparators — converting the diagnosis
into an evaluation instrument for memory designs.

A runnable CPU-only prototype (mirrored in `src/`) already validates the instrument end-to-end on a
surrogate tracker with *known* arbitration: the probe recovers the ground-truth arbitration parameter
with Spearman ρ = 1.000, demonstrates the memory-pollution failure mechanism, and shows a 0.000
placebo disruption rate. **No SAM2 number exists anywhere in this package** (Section 10).

## Section 4 — Background and motivation

**KNOWN.** SAM2 ([Ravi et al., 2024, arXiv:2408.00714](https://arxiv.org/abs/2408.00714)) made
memory-based tracking the default architecture for promptable video segmentation: a FIFO memory bank
of recent frame embeddings + mask features, attended by the current frame. SAM3
([Carion et al., 2025, arXiv:2511.16719](https://arxiv.org/abs/2511.16719)) keeps a memory-based
video tracker at its core while adding concept prompting. The tracking community immediately found
the soft spot: **distractors**. DAM4SAM ([Videnović et al., CVPR 2025, arXiv:2411.17576](https://arxiv.org/abs/2411.17576);
extended version [arXiv:2509.13864](https://arxiv.org/abs/2509.13864)) documents drift toward
visually similar distractors and splits the memory into recent-appearance and distractor-resolving
parts; SAMURAI ([Yang et al., 2024, arXiv:2411.11922](https://arxiv.org/abs/2411.11922)) states that
"SAM 2 tends to prioritize appearance similarity over spatial and temporal consistency" and bolts on
a Kalman motion prior; the memory-design study
([Alansari et al., 2025, arXiv:2512.22624](https://arxiv.org/abs/2512.22624)) re-implements the
SAM2-era memory designs on SAM3 and evaluates all of them — on ten benchmarks, by aggregate deltas.

**The gap (KNOWN by absence; scoop-checked at Stage 5, Stage 6 ×2, and re-verified this session).**
All three fix-papers *presuppose* that the memory arbitrates between appearance evidence and
location/temporal continuity, and each intervenes on that arbitration in a different direction
(DAM4SAM: curate what appearance memory stores; SAMURAI: add an explicit location prior at selection
time; the memory-design study: partition by function). None of them measures the arbitration.
SAMURAI's sentence is supported by two qualitative failure cases, not a measurement. There is no
displacement–gap–similarity curve for any SAM-family model anywhere in the literature. That is the
entire wedge: **the field is A/B-testing fixes to a mechanism it has never characterized.**

**Why it matters beyond the wedge.** (i) Cut-heavy deployments — edited footage, multi-camera
switching, surveillance handoff, medical cine loops — hit the teleport regime constantly; whether the
memory follows appearance or place there is a deployment-safety fact. (ii) A measured arbitration
curve converts memory design from benchmark-delta engineering into instrument-guided engineering: a
fix should *move the curve*, and we can say by how much and where. (iii) The SAM2→SAM3 generational
comparison asks whether a stronger backbone changed the arbitration at all — a question benchmark
deltas cannot answer because the backbones differ in everything simultaneously.

## Section 5 — Research questions

- **RQ1 (arbitration law).** When target and distractor exchange positions, does SAM2's memory follow
  appearance or location — and how does P(follow-place) vary with inter-frame displacement d,
  temporal gap g, and distractor similarity s?
- **RQ2 (generational).** Does SAM3's arbitration differ from SAM2's under the identical battery —
  i.e., did the next generation move the curve, and in which direction?
- **RQ3 (instrument).** Do the shipped fixes (DAM4SAM; SAMURAI) shift the arbitration curve in the
  direction their mechanism predicts (toward appearance), and by a measurable margin — i.e., does the
  probe work as an evaluation instrument for memory designs?
- **RQ4 (mechanism).** After a wrong pick, does the wrong identity persist because the memory bank
  *rebinds* to the distractor (memory pollution), and does freezing/clearing memory restore recovery?
- **RQ5 (external validity).** Do synthetic-cut arbitration measurements predict behavior on natural
  hard cuts?

## Section 6 — Falsifiable hypotheses

- **H1 (location-prior law — the original Agent-A hypothesis).** P(follow-place) increases
  monotonically with displacement d and with temporal gap g: memory attention degrades toward a
  location prior under temporal sparsity.
  *Falsified if:* SAM2 follows appearance at near-ceiling rates across all (d, g) cells, or behavior
  is unsystematic (no monotone structure on either axis).
- **H2 (similarity modulation).** Higher distractor similarity s shifts the curve left (more
  follow-place at equal d, g) — consistent with, and quantifying, DAM4SAM's drift observations.
  *Falsified if:* the curve is s-invariant.
- **H3 (memory pollution).** Given a wrong pick at the swap frame, the wrong identity persists in
  subsequent frames at a rate far above the model's spontaneous re-detection rate, because the memory
  bank absorbs distractor appearance. *Falsified if:* recovery after a wrong pick is rapid and common
  with normal memory updating.
- **H4 (fix direction).** Each shipped fix moves the arbitration curve in the direction its own
  mechanism predicts. The two fix philosophies predict *different* directions: DAM4SAM
  (appearance-memory curation) should shift toward **appearance** (lower location-prior index);
  SAMURAI (explicit Kalman motion prior at selection time) should *reject* the teleported appearance
  — on teleport trials, higher follow-place and/or higher lost rate. The probe distinguishes these
  two philosophies behaviorally, which benchmark deltas cannot.
  *Falsified if:* the fixes leave the curve unmoved relative to vanilla SAM2.1.
- **H5 (external validity).** Natural-hard-cut follow-place rates agree in rank with
  synthetic-battery predictions across matched (d, g, s) bins. *Falsified if:* rank agreement is at
  chance — which fires the pre-registered PIVOT (Section 26).

All five are HYPOTHESES. None is supported by any measurement in this package (Section 10).

## Section 7 — Pre-registered predictions and either-outcome interpretation

**Prediction under H1/H2 (HYPOTHESIS):** monotone P(follow-place) in d and g for SAM2-L, curve
shifted left by s; SAM3 and DAM4SAM curves shifted toward appearance relative to SAM2.1.

**The either-outcome table (pre-registered at Stage 5, binding).** The killer battery has no
deflationary branch:

| SAM2-L battery outcome | Finding | Paper framing |
|---|---|---|
| Monotone location-prior curve (H1 supported) | The arbitration law the fix-papers presuppose, measured | Titles 1/2: the law + the instrument |
| Appearance-following at near-ceiling everywhere (H1 falsified cleanly) | Controlled refutation of the location-prior worry; trust-positive for cut-heavy deployments; directly contradicts the drift folklore the distractor-memory line motivates with | Title 5: the corrective + the instrument |
| Unsystematic (neither monotone nor ceiling) | The instability itself is the report | STOP branch: short note, multi-model extension not funded (Section 26) |

RESULT SLOT (to be filled at day 5 of week one): which branch fired, marginal curves, location-prior
index with CI. Until filled, every statement about SAM2 behavior in this package is HYPOTHESIS.

## Section 8 — Genre and positioning

**Genre: capability instrument** (the portfolio's certainty anchor; the final-3 mix is constructive
method C-0306 + capability instrument A-0028 + mechanism dissociation B-0114 — zero audit-genre
seats). Positioning rules, binding on the paper:

1. **Not a complaint.** The claim is NOT "SAM2 fails on jumps" — the drift phenomenon is documented
   and actively being fixed. The claim is the *measurement instrument* the fix-papers lack.
2. **Instrument, then findings.** The probe is the contribution; the SAM2 curve, the SAM3
   generational comparison, and the fix-paper evaluations are the instrument's first three outputs.
3. **Diagnosis-to-evaluation conversion.** DAM4SAM/SAMURAI enter as *subject models*, not competitors
   — their curves are the demonstration that the instrument discriminates memory designs.
4. **Fix-papers are armor, not threat.** Three fix-papers presupposing the unmeasured arbitration is
   the motivation section writing itself; each new one strengthens the wedge (and tightens the clock
   — Section 26).

## Section 9 — Contributions (as they will appear in the paper)

1. **The teleport probe**: a controlled, placebo-armed behavioral battery measuring
   appearance-vs-location arbitration in memory-based video segmenters as a psychometric function of
   (d, g, s) — with released stimulus generator, scoring harness, and curated natural-cut set.
2. **The first arbitration measurements** for SAM2 (sizes), SAM3, DAM4SAM, and SAMURAI — including
   the first controlled SAM2→SAM3 generational comparison of memory behavior isolated from backbone
   strength confounds. [RESULT SLOT — findings enumerated after the batteries run.]
3. **A mechanism readout**: memory-pollution persistence and recovery after wrong picks, with
   frozen-memory ablation (prototype-validated readout design; real-model numbers pending).
4. **A validated-instrument methodology**: the probe is validated on a surrogate tracker with known
   arbitration before touching any subject model (MEASURED-synthetic: ρ = 1.000 recovery, 0.000
   placebo disruption) — a template for behavioral probing of video models generally.

## Section 10 — Evidence-labeling rule (BINDING on every document in this package)

Three labels, used everywhere, no exceptions:

- **KNOWN** — published literature (with URL) or arithmetic. Example: DAM4SAM partitions memory into
  recent-appearance and distractor-resolving parts (arXiv:2509.13864).
- **HYPOTHESIS** — any statement about SAM2/SAM3/DAM4SAM/SAMURAI behavior under the probe. No SAM2
  number appears anywhere in this package, and none is implied. H1–H5 are all HYPOTHESIS.
- **MEASURED (synthetic surrogate)** — numbers produced by `src/run_synthetic.py` on the surrogate
  memory tracker whose arbitration parameter λ_loc is a known ground truth. These validate the
  *instrument*, never the hypotheses about real models. Canonical committed run:
  `src/results_synthetic/report.md` (mirror of `Windows2/_wip/stage7_proto_A0028/results/report.md`).

The Stage-7 prototype results are a **SYNTHETIC SURROGATE** demonstration. The surrogate is a
functional model of a memory tracker (recency-decayed appearance template + spatial prior, explicit
λ_loc arbitration) — no image encoder, no mask decoder, no learned memory attention, **not SAM2**.
What it proves: the probe pipeline runs end-to-end; the probe recovers a known arbitration
(instrument validity); the trichotomy + persistence readouts track a real mechanism; the placebo arm
can come back clean. What it cannot prove: anything about SAM2 — including H1's monotone gap
prediction, which the surrogate's ~flat gap axis pointedly does **not** prefabricate.
