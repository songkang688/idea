# A-0028 — Literature Review, Novelty, and Scoop Analysis (Sections 11–14 of 28)

Labeling per `proposal.md` Section 10: everything in this file is **KNOWN** (published, with URL)
unless explicitly tagged otherwise. Full BibTeX in `references/references.bib`; annotated one-liners
in `references/references.md`. Citation verification date: 2026-08-28 (this session, live search).

---

## Section 11 — The subject models: SAM2, SAM3, and memory-based tracking

**SAM2** — Ravi et al., "SAM 2: Segment Anything in Images and Videos," 2024.
[arXiv:2408.00714](https://arxiv.org/abs/2408.00714) · [code](https://github.com/facebookresearch/sam2).
Streaming architecture: image encoder per frame; a **memory bank** of recent frames' features +
predicted masks (FIFO, plus the prompted frame); **memory attention** conditions the current frame on
the bank; mask decoder outputs the masklet. The memory is the locus of the arbitration this project
measures: what the bank stores and how attention weighs stale appearance against recent location is
implicit, learned, and — before this project — uncharacterized. Sizes: Tiny/Small/Base+/Large
(SAM2.1 checkpoints). The killer battery runs on **SAM2.1-L** (`sam2.1_hiera_large`).

**SAM3** — Carion et al., "SAM 3: Segment Anything with Concepts," 2025.
[arXiv:2511.16719](https://arxiv.org/abs/2511.16719) · [code](https://github.com/facebookresearch/sam3).
Unified detector + **memory-based video tracker** sharing one backbone; adds promptable concept
segmentation, retains SAM2-style visual prompting (points/boxes/masks) for video. Because the tracker
remains memory-based, the identical probe applies — enabling the first controlled generational
comparison of memory *behavior* (RQ2). KNOWN: SAM3 inherits "all the capabilities of SAM 2"
including point-prompted video segmentation, so the frame-0-prompt protocol transfers unchanged.

**Memory lineage (pre-SAM context).** XMem — Cheng & Schwing, ECCV 2022,
[arXiv:2207.01578](https://arxiv.org/abs/2207.01578) (Atkinson–Shiffrin multi-store memory for VOS);
Cutie — Cheng et al., CVPR 2024, [arXiv:2310.12982](https://arxiv.org/abs/2310.12982)
(object-level memory reading, explicitly motivated by distractor robustness); KeepTrack — Mayer et
al., ICCV 2021, [arXiv:2103.16556](https://arxiv.org/abs/2103.16556) (learned association to "keep
track of what not to track" — distractor awareness predates SAM2). The appearance-vs-location tension
is a decade-old design axis in tracking; SAM2 made one implicit choice at scale, and nobody has
measured what that choice is.

**Long-video memory variants** (the design space the instrument would serve): SAM2Long — Ding et al.,
ICCV 2025, [arXiv:2410.16268](https://arxiv.org/abs/2410.16268) (training-free memory tree);
HiM2SAM — [arXiv:2507.07603](https://arxiv.org/abs/2507.07603) (hierarchical memory); SAMITE —
[arXiv:2507.21732](https://arxiv.org/abs/2507.21732) (temporal memory mechanism); EfficientTAM —
[arXiv:2411.18933](https://arxiv.org/abs/2411.18933) and EdgeTAM —
[arXiv:2501.07256](https://arxiv.org/abs/2501.07256) (efficiency-focused SAM2 variants that DAM4SAM's
extended paper shows also benefit from memory redesign). Every one of these modifies memory policy
and evaluates by benchmark delta. None measures arbitration.

## Section 12 — The distractor-fix line and what it presupposes (the mandatory citation set)

The three papers named in the battle-locked claim, plus what each one measures vs presupposes:

**1. DAM4SAM** — Videnović, Lukežič, Kristan, "A Distractor-Aware Memory for Visual Object Tracking
with SAM2," **CVPR 2025**. [arXiv:2411.17576](https://arxiv.org/abs/2411.17576) ·
[CVPR open access](https://openaccess.thecvf.com/content/CVPR2025/papers/Videnovic_A_Distractor-Aware_Memory_for_Visual_Object_Tracking_with_SAM2_CVPR_2025_paper.pdf) ·
[project](https://jovanavidenovic.github.io/dam-4-sam/) · [code + DiDi dataset](https://github.com/jovanavidenovic/DAM4SAM).
Extended journal-style version: "Distractor-Aware Memory-Based Visual Object Tracking,"
[arXiv:2509.13864](https://arxiv.org/abs/2509.13864) — **this is the arXiv ID carried in the
battle-locked claim**; both IDs refer to the same DAM4SAM line and both are cited.
*What it measures:* benchmark quality/robustness deltas on 7 (v1) / 13 (extended) benchmarks; ships
the distractor-distilled **DiDi** dataset. *What it presupposes:* that SAM2's failure is storing the
wrong appearances — the fix partitions memory into recent-appearances (RAM) and distractor-resolving
(DRM) stores with introspection-gated updates. That is an intervention on appearance-memory *content*
justified by drift anecdotes, with no measurement of the appearance-vs-location arbitration it aims
to repair.

**2. SAMURAI** — Yang, Huang, Chai, Jiang, Hwang, "SAMURAI: Adapting Segment Anything Model for
Zero-Shot Visual Tracking with Motion-Aware Memory," 2024.
[arXiv:2411.11922](https://arxiv.org/abs/2411.11922) · [code](https://github.com/yangchris11/samurai).
*What it claims:* "SAM 2 tends to prioritize appearance similarity over spatial and temporal
consistency" (crowded scenes). *Evidence base for that sentence:* qualitative failure cases (their
Fig. 1) motivating a Kalman-filter motion prior + threshold-gated memory selection. Ruled at Stage-6
(fourth kill attempt, `stage6_agent_S/battle.md` Round 5 Part B): **an anecdotal characterization,
not a measurement — the third fix-paper presupposing the unmeasured arbitration**; a citation
obligation, not a scoop. Note the direction: if SAMURAI's sentence were quantitatively right
(appearance-dominance), the location-prior branch of H1 is falsified — which is the *other*
pre-registered finding. The probe adjudicates a disagreement the fix-papers don't know they have.

**3. The SAM2/SAM3 memory-design study** — Alansari, Naseer, Al Marzouqi, Javed, Werghi, "Rethinking
Memory Design in SAM-Based Visual Object Tracking," 2025.
[arXiv:2512.22624](https://arxiv.org/abs/2512.22624) · [code (SAM3 Tracking Zoo)](https://github.com/HamadYA/SAM3_Tracking_Zoo).
*What it does:* re-implements SAM2-era memory designs (DAM4SAM, SAMURAI, HiM2SAM, SAMITE, SAM2Long)
on the SAM3 backbone; ten-benchmark evaluation; proposes a hybrid short-term-appearance +
long-term-distractor-resolving memory. *Why it matters here:* (i) it is the closest thing to a
systematic memory study, and its instrument is still the aggregate benchmark delta — it varies memory
designs but never isolates the arbitration variable; (ii) it confirms SAM3 must be a subject model
(the memory-design conversation has already moved to SAM3); (iii) its zoo is infrastructure this
project reuses for the comparator arms (E6). It is simultaneously the strongest motivation and the
fastest-moving absorb-risk (Section 24 / `reviewer_attacks.md`).

**The presupposition, stated precisely.** All three fixes are interventions on the same latent
quantity — how memory attention weighs stale appearance evidence against location/temporal
continuity — from three different philosophies (curate appearance content / add explicit location
prior / partition by function). An intervention on an unmeasured quantity can only be evaluated by
end-to-end deltas, which is what all three do. The teleport probe measures the quantity.

*Packaging-session addendum (2026-08-28, live-verified):* SAMITE
([arXiv:2507.21732](https://arxiv.org/abs/2507.21732)) turns out to be a **fourth** fix-paper in the
same shape — it selects memories via a "position-wise anchor (a frame whose target is nearby to the
current)" alongside a feature-wise anchor, and injects "explicit positional clues" as pseudo mask
prompts to suppress distractors. A fourth independent intervention on the unmeasured arbitration; it
joins the presupposing-fix-papers citation set (and Section 24's absorb-risk trend line: the shape
now prints roughly quarterly). Still no controlled dissociation measurement anywhere in it.

## Section 13 — Adjacent methodology: behavioral probes and model psychophysics

- **Psychometric methodology.** Wichmann & Hill, "The psychometric function: I. Fitting, sampling,
  and goodness of fit," *Perception & Psychophysics* 63:1293–1313, 2001.
  [DOI:10.3758/BF03194544](https://doi.org/10.3758/BF03194544). The fitting-and-CI discipline for
  P(response | stimulus intensity) curves; the probe's P(follow-place | d, g, s) surfaces are
  psychometric functions and are analyzed as such (logistic GLM + clustered bootstrap; `experiments.md`
  Section 19).
- **Wilson intervals for per-cell rates.** Wilson, *JASA* 22:209–212, 1927.
  [DOI:10.1080/01621459.1927.10502953](https://doi.org/10.1080/01621459.1927.10502953). Used
  throughout the prototype and the real batteries.
- **Object permanence probing.** Shamsian et al., "Learning Object Permanence from Video," ECCV 2020,
  [arXiv:2003.10469](https://arxiv.org/abs/2003.10469) — precedent for controlled location-continuity
  probes of trackers, in the learning (not measurement) direction.
- **Compositing.** Pérez, Gangnet, Blake, "Poisson Image Editing," SIGGRAPH 2003,
  [DOI:10.1145/1201775.882269](https://dl.acm.org/doi/10.1145/1201775.882269) — the blending used by
  the stimulus generator; the placebo arm exists precisely because compositing is an intervention.
- **Benchmarks anchoring the stimuli/validation** (KNOWN, standard): COCO
  [arXiv:1405.0312](https://arxiv.org/abs/1405.0312); LVIS
  [arXiv:1908.03195](https://arxiv.org/abs/1908.03195); DAVIS 2017
  [arXiv:1704.00675](https://arxiv.org/abs/1704.00675); MOSE
  [arXiv:2302.01872](https://arxiv.org/abs/2302.01872); LVOS
  [arXiv:2211.10181](https://arxiv.org/abs/2211.10181); DiDi
  ([DAM4SAM repo](https://github.com/jovanavidenovic/DAM4SAM)) as the external distractor-heavy anchor.

## Section 14 — Novelty statement and scoop analysis

**Novelty claim (scoop-checked four times: Stage-5 N, Stage-6 Q, Stage-6 S, and this packaging
session).** No published or preprinted work measures appearance-vs-location arbitration in
memory-based video segmenters as a controlled function of displacement, temporal gap, and distractor
similarity. Specifically, none of the following contains a teleport/swap causal probe, an arbitration
curve, a placebo-controlled displacement grid, or any psychometric characterization of memory
behavior: SAM2 (2408.00714), SAM3 (2511.16719), DAM4SAM (2411.17576 / 2509.13864), SAMURAI
(2411.11922), memory-design study (2512.22624), SAM2Long (2410.16268), HiM2SAM (2507.07603), SAMITE
(2507.21732), EfficientTAM (2411.18933), EdgeTAM (2501.07256), Cutie (2310.12982), XMem (2207.01578),
KeepTrack (2103.16556).

**What DOES exist (and is therefore not claimable as novel):**

- The drift-toward-distractors *phenomenon* — documented (DAM4SAM, SAMURAI, DiDi). The paper must not
  claim discovery of the phenomenon.
- Distractor-heavy *evaluation data* — DiDi exists; our synthetic battery is a controlled instrument,
  not a benchmark competitor, and DiDi is used as an external anchor.
- Memory-design *comparison at benchmark level* — 2512.22624 owns that; we own the per-mechanism
  arbitration axis it lacks.

**Scoop-risk statement (KNOWN trend, HYPOTHESIS on timing).** Three fix-papers touch the phenomenon;
the niche prints quarterly; the highest-probability scoop shape is not a dedicated probe paper but a
**teleport-shaped row in someone's ablation table** (absorb risk). Standing obligations, binding
(clocks consolidated in `roadmap.md` Section 26): (i) killer battery runs in week one, no exceptions
— execution is the only real mitigation; (ii) mandatory scoop re-search at experiment freeze and
again at submission freeze, logged in the repo; (iii) if a controlled teleport-style dissociation
probe appears before our execution, the pre-registered response is KILL (not "differentiate") — per
`stage5_agent_N/exp_07.md`; a benchmark-delta ablation row that merely *gestures* at displacement
sensitivity without a controlled (d, g, s) design does NOT trigger the kill (it becomes a citation),
and the PI adjudicates borderline cases against the written criterion in `roadmap.md` Section 26.
