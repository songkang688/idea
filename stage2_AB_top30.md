# Stage 2 — A+B Top 30 + 15 Protected Wildcards (partial merge; Batch C pending)

**Basis:** 130-idea unique pool (`stage2_AB_merged_pool.md`). Ranking weighs: cross-batch convergence (two independent reviewers generated the same idea — the strongest available signal), reviewer flagship designations, falsifiability sharpness, cost-to-verdict ratio, and field-level consequence. Scores from both batch score sheets consulted; no experimental results are assumed or invented.

Top 30 and wildcards are **disjoint** (45 protected entries total). All selections remain subject to Stage 3 prior-art search — see the uncertainty note at the end.

---

## Part 1 — Top 30 strongest unique candidates (ranked)

### Tier 1 — The contamination & evaluation flagships (1–11)

1. **MERGE-01** (A-0029 + B-0019) — Model-in-the-loop annotation corrupts its own ground truth: crossover anchoring study + student inheritance test.
   *Why:* Both batches independently invented this and both called it flagship-tier. Field-level stakes (the community's future GT), a controlled within-annotator design, and compounding importance as model-assisted annotation grows.

2. **A-0007** — SAM masks imprint the SA-1B annotation protocol, not image statistics.
   *Why:* The mechanism paper of the contamination program; clean same-images design; "segment anything" reframed as "replicate one annotation policy."

3. **MERGE-09** (A-0267 + B-0329) — Weak-to-strong dense distillation: students inherit bias-type errors, surpass variance-type errors.
   *Why:* Determines the ceiling of the field's dominant dataset-construction strategy; merges A's signature instrument with B's bias/variance theory; HRHR·DM protected.

4. **B-0191** — Error amplification in self-consuming segmentation pipelines.
   *Why:* The stability conditions of the data flywheel become design rules for every auto-labeling pipeline; the dense analogue of model-collapse theory, built empirically.

5. **A-0245** — A 2015 U-Net with a 2026 recipe: what fraction of a decade's progress is recipe?
   *Why:* Batch A's flagship falsification study; the attribution number becomes field infrastructure whichever way it lands.

6. **MERGE-15** (A-0091 + B-0082) — Label-noise-aware leaderboards: inter-annotator floors + relabeling bootstrap → rank-flip probabilities.
   *Why:* Converts "progress within label noise" from suspicion to instrument; one annotation budget serves both halves; flagship-tier for medical evaluation.

7. **A-0340** — Bootstrap the leaderboards: the fiction fraction.
   *Why:* Cheapest headline number in the pool — released predictions plus a week of analysis reframes how every leaderboard is read.

8. **A-0336** — Human floors and ceilings for segmentation benchmarks.
   *Why:* The missing anchor of dense evaluation; no model training required; cited by every headroom discussion for years.

9. **A-0337** — Annotation instructions as an experimental treatment.
   *Why:* Genuinely new experimental methodology; "GT is instruction-contingent at SOTA-gap scale" forces benchmark practice changes.

10. **MERGE-14** (A-0166 + B-0037) — The annotation-tolerance ceiling: closed-form + empirical, with annotator-identity residual test.
    *Why:* Analytic ceiling everyone evaluating small structures needs, plus the sharpest style-fitting proof in the pool (residuals predict the annotator).

11. **B-0012** — Near-duplicate inflation of annotation-efficiency claims.
    *Why:* Cheap, decisive, attacks numbers driving clinical adoption now; recalibrates how the whole program reads the few-shot literature — run early.

### Tier 2 — Deployment-critical safety & validity audits (12–18)

12. **MERGE-02** (A-0185 + B-0241) — The absent-target hallucination benchmark with refusal protocols.
    *Why:* Text-driven monitoring and OV segmentation are productizing now; makes refusal a first-class metric before deployment norms solidify; cross-batch convergence.

13. **A-0118** — Models hallucinate surgically removed organs.
    *Why:* The most quotable patient-safety silent failure available, with a mechanism (positional-consistency prior) and a benchmark deliverable.

14. **B-0185** — Knowledge conflict: dense VLMs regress to textbook priors on abnormal cases.
    *Why:* The worst conceivable medical-VLM failure mode, untested; NLP knowledge-conflict methodology ports directly; HRHR·DM protected.

15. **A-0187** — Negation anti-accuracy: worse than chance, located as a fusion failure.
    *Why:* Systematically inverted behavior is qualitatively scarier than "ignores negation"; encoding-vs-fusion attribution makes it repairable.

16. **A-0041** — Does chain-of-thought causally change grounding?
    *Why:* A causal intervention with a mask endpoint that crowns or kills the reasoning-segmentation subfield; both outcomes consequential.

17. **A-0103** — Uncertainty maps ≠ clinician disagreement (boundary-band-excluded test).
    *Why:* A stringent validity instrument that may empty the clinical value proposition of an entire UQ literature.

18. **B-0084** — Out-of-domain calibration of SAM's predicted-IoU head.
    *Why:* Highest ratio of affected systems to experimental cost in either batch — an afternoon of compute against a dependency thousands of pipelines share.

### Tier 3 — Adaptation science with cross-batch convergence (19–24)

19. **MERGE-07** (A-0076 + B-0248) — The gain/retention frontier: forgetting as unforced error.
    *Why:* The infrastructure spine of adaptation science; matched-target selection discipline plus frontier estimation answers the folklore on both sides.

20. **A-0078** — Forgetting is mostly readout drift.
    *Why:* If lost capabilities remain linearly decodable, continual learning's objective changes entirely; simple design, big reframe.

21. **MERGE-08** (A-0058 + B-0260) — Low-rank adaptation amplifies shortcuts.
    *Why:* Cross-batch convergence on a safety-critical inversion of PEFT folklore, with synthetic and natural evidence and a rank-sweep mechanism test.

22. **A-0055** — LLRD explains most of the PEFT advantage.
    *Why:* One cheap baseline potentially deflating a literature; the tuning-fairness fight it provokes is the point.

23. **MERGE-05** (A-0296 + B-0064) — The UDA reality audit.
    *Why:* Ranking transfer + marginal-value-over-foundation-baselines in one matched-compute grid; decision-grade for everyone doing segmentation DA after 2026.

24. **MERGE-06** (A-0303 + B-0057) — Statistics recalibration: TTA method + shift-tier diagnostic.
    *Why:* Both batch reviewers independently rated this family highest-adoption-probability; fills the post-BN vacuum and routes all other adaptation work.

### Tier 4 — Mechanism laws and program anchors (25–30)

25. **MERGE-04** (A-0161 + B-0129) — The small-structure bottleneck: information-absent vs decoder-limited.
    *Why:* The compass for all small-structure investment; probe stage is cheap, intervention grid is decisive; several other survivors get their interpretation from it.

26. **MERGE-03** (A-0006 + B-0226) — One boundary-contrast law across hard-target literatures.
    *Why:* A single-variable law that would unify three failure literatures and decide preprocess-vs-retrain per domain; cross-batch convergence.

27. **A-0121** — Binary smoke masks are ill-posed ground truth.
    *Why:* Task-redefinition anchor of the entire amorphous program; everything downstream (contrast law, latency metric, primitives) depends on this measurement being done carefully.

28. **A-0093** — Why nnU-Net still wins: causal component-swap decomposition.
    *Why:* The strategic fork of medical VFM investment, attacked with component swaps rather than another bake-off; expensive, contentious, and exactly why nobody has done it properly.

29. **MERGE-10** (A-0141 + B-0126) — What frozen features know about layered scenes.
    *Why:* Three-way verdict (pretraining fix / format fix / decoder fix) from linear probes on frozen features — field-redirecting conclusions at probing cost.

30. **A-0154** — Camouflage failure: attentional or perceptual?
    *Why:* One oracle-prompt experiment could redirect an entire subfield's investment from features to search; near-free.

**First alternates (31–34, in order):** A-0031 (paraphrase variance) · B-0083 (protocol sensitivity — run-first candidate on cost grounds) · B-0114 (PEFT seed variance) · A-0242 (publication-bias z-curve).

---

## Part 2 — 15 protected wildcards

High-risk/high-reward and counter-intuitive bets that would not win a consensus vote today but must survive Stage 3 attrition. Each carries explicit protection; kill only on direct prior-art hits or hard feasibility walls, not on mean scores.

1. **B-0009** [HRHR] — Geometric-stratum census of SA-1B: frequency-capability curves separating data limits from architecture limits. *The study that tells the field where scaling stops working; feasibility drags its mean, upside is field-redirecting.*
2. **MERGE-16** (A-0142 + B-0159) [CI/HRHR] — Depth failure as transparency signal: invalidity as feature and as the largest free transparency corpus. *If confounder filtering works, transparency data economics change permanently.*
3. **B-0075** [HRHR·CI] — Reflection-swap cue attribution for glass. *The rare physical intervention yielding a causal statement about what a foundation model uses.*
4. **B-0162** [HRHR] — Polarization-privileged training: what fraction transfers to plain RGB? *Clean dichotomy either way; capture-once-deploy-everywhere upside.*
5. **B-0078** [HRHR] — Language as a domain coordinate: zero-image adaptation from text descriptions. *Either opens a zero-data channel or measures the limit of language-vision domain alignment; permutation control is mandatory.*
6. **B-0294** [HRHR] — Bimodal loss residuals as a corpus-free contamination detector. *High failure probability; success creates an instrument the whole field needs and cannot currently buy. Pre-registered kill criterion.*
7. **B-0318** [HRHR] — Differentiable scattering: 2D smoke masks supervise 3D density. *The one physics-first bet; binary-mask parity is the cheap early kill test.*
8. **A-0122** [HR] — Beer–Lambert transmittance as smoke ground truth. *Physics-grounded labels for a safety domain — outlives model generations if the illumination problem is tractable.*
9. **A-0125** [HR] — Turbulence spectra as label-free smoke signal. *Appearance-free pretext robust to exactly the shifts that break appearance models; distance-regime gate first.*
10. **A-0089** [HR] — Forgetting hysteresis: suppression time-constants and refresh schedules. *A genuinely new phenomenon to name, with an immediately adoptable maintenance policy.*
11. **A-0067** [HR+RM] — The encoder/decoder LR-ratio dial: R²>0.7 or bust. *Radical-simplification claim; messy middle is a real risk, collapsing the recipe zoo justifies protection.*
12. **A-0203** [HR+CI] — SSL object emergence as a crop-statistics artifact. *A causal intervention on one of SSL's most celebrated narratives; compute-heavy, theory-relevant. A-0266 gates it.*
13. **A-0254** [RM] — A provably-novel synthetic zero-shot benchmark. *Construction-heavy, but it is the reusable contamination-proof instrument three killed audits pointed at.*
14. **A-0207** [RM] — Data vs method: variance decomposition over open-corpus VFMs. *Fragile pool, contestable kernels — but "data explains more than method" would force re-reading of the comparison literature.*
15. **B-0285** [CI·CF] — Compression that helps: JPEG as a matched filter for smoke. *The pool's surprise bet: beneficial degradation inverts preprocessing dogma and falsifies the monotone-degradation assumption; nearly free to test.*

**Wildcard alternates:** A-0305 (night information floor) · B-0338 (noise as signal) · A-0157 (human glass floor) · B-0128 (Lipschitz prompt geometry).

---

## Stage 3 handoff notes

- **Prior-art priority:** Tier 1 first — the contamination/annotation-noise program (MERGE-01, A-0007, MERGE-09, MERGE-15, A-0336) sits in fast-moving audit territory (model-assisted annotation bias in HCI/medical imaging, 2023–2026 SAM audit literature, psychology-imported meta-science). A single existing paper could kill or force re-scoping of the pool's top entries. Merged ideas must be searched per-constituent *and* per-merged-framing.
- **Conflict-aware sequencing:** see `stage2_AB_duplicates.md` §3 (14 flags) and the dependency map in `stage2_AB_clusters.md` — instruments before audits (CONF-10), smoke GT before smoke claims (CONF-3), compression confounder before tokenization-floor headlines (CONF-4).
- **Batch C integration:** rankings are provisional; C survivors may join clusters, force new merges (MERGE-19+), or displace Tier 3–4 entries. Tier 1 is unlikely to move except by prior-art kill.

*End of Top 30 + wildcards (A+B partial).*
