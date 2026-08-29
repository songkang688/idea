# A-0028 — Roadmap, Stop/Continue Criteria, Paper Plan, Release (Sections 25–28 of 28)

Labeling per `proposal.md` Section 10. The week-one schedule is **binding** (Stage-6 S, Round 5:
"killer battery in week one, no exceptions — it was already Q's condition; it is now load-bearing").

---

## Section 25 — Roadmap and schedule

### Week one (BINDING — verbatim from `stage6_agent_S/final3.md`, expanded)

- **Days 1–3 — instrument build-out (real stimuli).** Stimulus generator over the (d, g, s) grid on
  real crops (COCO/LVIS donors, DAVIS/SA-V backgrounds, Poisson blending) + the placebo-paste arm;
  scoring harness (trichotomy + psychometric fit) validated on a smoke batch. The synthetic mirror in
  `src/` is the reference implementation for grid iteration, seeding discipline, trichotomy scoring,
  and Wilson/index/ρ analysis — the real generator replaces `world.py`'s abstract candidates with
  rendered composites; `sam2_wrapper.py` is the adapter seam (env-gated stub already present:
  `A0028_USE_REAL_SAM2=1` + checkpoint + config; `render_trial_frames` is its input path).
- **Day 4 — THE KILLER BATTERY.** SAM2.1-L, full grid, ~10⁴ clips, placebo arm first, one GPU-day
  (`experiments.md` Section 20; spec `configs/killer_sam2l.yaml`).
- **Day 5 — first curves + freeze log.** Arbitration curves with CIs; gate verdict (V then A/B/C);
  fill the RESULT SLOTS in `experiments.md`; natural-cut curation starts in parallel; **scoop
  re-search executed and logged at experiment freeze** (mandatory — fastest-moving niche of the
  final 3).

### Weeks 2–3 — fan-out (conditional on gate A or B)

- E3 size scaling (SAM2.1-T/S/B+), E5 SAM3 generational battery, E6 DAM4SAM + SAMURAI comparators,
  E8 frozen-memory pollution ablation — ~3 GPU-days total, single 24 GB GPU, order-independent.
- Natural-cut annotation completes; E7 runs (~0.5 GPU-day); H5 rank-agreement verdict.

### Week 4 — analysis freeze and preprint

- Threshold-sensitivity appendix; psychometric surfaces per model; generational and fix-evaluation
  figures; second scoop re-search; **arXiv preprint immediately** (absorb-risk mitigation M3) — the
  preprint carries the killer + whatever fan-out is complete; the venue submission follows.

### Milestones

| M | Deliverable | Gate |
|---|---|---|
| M0 (done) | synthetic prototype: instrument validated on known-λ surrogate, 23 tests, committed run | — (MEASURED, surrogate) |
| M1 (day 3) | real stimulus generator + smoke batch through SAM2.1-L adapter | smoke trichotomy rates populated, placebo seams QA'd |
| M2 (day 5) | killer battery result + gate verdict + freeze log | V, then A/B/C |
| M3 (week 4) | arXiv preprint (instrument + SAM2 law/corrective + available fan-out) | H5 verdict in hand or natural-cut arm explicitly flagged in-progress |
| M4 | venue submission (Section 27) | full battery + threshold appendix + final scoop re-search |

## Section 26 — Stop / pivot / kill / continue criteria (pre-registered, consolidated)

**Kill criteria:**

- **K1 (scooped).** A controlled teleport/swap-style dissociation probe — a designed (displacement ×
  gap × similarity)-style manipulation with per-condition behavioral scoring on a SAM-family tracker —
  appears in the literature before our execution. Verdict: KILL, not "differentiate"
  (`stage5_agent_N/exp_07.md`). NOT a kill: a benchmark-delta ablation row gesturing at displacement
  sensitivity without controlled manipulation → citation obligation. Borderline → PI adjudicates
  against this written criterion.
- **K2 (probe invalid).** Placebo gate V fails (real-model placebo disruption Wilson-upper ≥ 0.05)
  after a bounded compositing-fix iteration (one re-run). Verdict: KILL — the probe measures paste
  artifacts, and we say so rather than shipping a confounded instrument.

**Pivot criterion:**

- **P1 (external validity).** Synthetic curves fail to predict natural-cut behavior — pre-registered
  test: Spearman rank agreement between synthetic-predicted and natural-cut-measured P(follow-place)
  across matched bins < 0.4, or sign disagreement on the d-marginal direction. Verdict: re-scope to
  **natural-cut-only** with a smaller factorial grid (larger curation budget replaces the synthetic
  battery; the instrument claim narrows to natural discontinuities; the paper survives smaller).

**Stop criterion:**

- **S1 (unsystematic).** Killer gate C fires: SAM2-L shows neither monotone structure nor
  appearance-ceiling. Verdict: STOP the multi-model extension; report the instability itself
  (per-cell variance decomposition + seeds) as one short note. No further GPU spend.

**Continue criteria:**

- **C1.** Gate A or B fires → fund the fan-out (E3/E5/E6/E7/E8; 3–4 further GPU-days) and the full
  paper. Both branches are findings by pre-registration; neither is a deflationary outcome.
- **C2 (freshness clock).** Scoop re-search at experiment freeze (day 5) and at submission freeze
  (M4), logged in-repo (`references/` gets a dated addendum each time). Between M3 and M4, a monthly
  literature sweep of the SAM-memory niche (arXiv cs.CV, "SAM2/SAM3 memory", "distractor", "tracking
  drift") — the niche printed DAM4SAM→extended→SAMURAI→zoo within ~13 months.
- **C3 (portfolio clock, Stage-6).** The week-one battery is the seat's execution condition; if
  week-one does not happen, the seat reverts to the PI with the absorb-risk memo and B-0194 as the
  named replacement (see `reviewer_attacks.md` Section 24).

## Section 27 — Paper plan: skeleton, figures, venues

**Skeleton (8 pages + supplement), written to absorb the completed killer result as Section 4:**

1. Introduction — the fix-papers presuppose an unmeasured arbitration (three citations, three
   philosophies, zero measurements); the teleport probe measures it.
2. Related work — `literature.md` Sections 11–13 compressed; the "what exists / what doesn't" table.
3. The probe — stimuli, placebo arm, trichotomy, psychometric analysis; **instrument validation on
   the known-λ surrogate** (ρ = 1.000; the methodological contribution stands independent of any
   subject-model result).
4. The SAM2 arbitration law [RESULT SLOT — killer battery + size scaling].
5. Generational comparison: SAM3 vs SAM2 [RESULT SLOT — E5].
6. The probe as a memory-design instrument: DAM4SAM and SAMURAI curves [RESULT SLOT — E6]; memory
   pollution and the frozen-memory ablation [RESULT SLOT — E8].
7. External validity: natural cuts + DiDi anchoring [RESULT SLOT — E7].
8. Limitations (observation-sparsity scope of g; categorical similarity tiers; subject-model
   training-data overlap disclosure) & conclusion.

**Figure plan:** F1 probe schematic (from `diagrams/probe_pipeline.mmd`); F2 SAM2-L arbitration
curves — the three marginals with CIs; F3 psychometric surface + location-prior index per model
(the one-glance instrument figure); F4 generational overlay (SAM2 sizes + SAM3); F5 fix-evaluation
overlay (vanilla vs DAM4SAM vs SAMURAI — H4's two predicted directions); F6 synthetic-vs-natural
agreement scatter (H5); F7 memory-pollution persistence + frozen-memory recovery bars.

**Venues (in order):** CVPR 2027 (primary — the DAM4SAM/SAMURAI/zoo reviewer pool lives there;
submission window fits M4 after a week-one killer battery); ICCV 2027 (fallback); NeurIPS 2027
Datasets & Benchmarks track (alternative framing: probe battery + curated natural-cut set as the
released artifact). Workshop hedge only if M3 slips: a VOT/video-understanding workshop carrying the
preprint while the full battery completes.

## Section 28 — Reproducibility, release, and ethics/licensing

**Reproducibility discipline (already enforced in the mirror `src/`):** every battery is a pure
function of (config, seed) — per-cell crc32-derived streams; byte-identical stimuli across subjects
(clips rendered once, cached, hashed); per-trial provenance (donor IDs, paste coords, blend seed,
grid cell) in the results JSON; configs and result hashes committed alongside figures. The synthetic
run in this package regenerates with one command (`README.md`); 23 unit tests cover world, tracker,
probe, and the env-gate.

**Release plan:** code (stimulus generator, adapters, scoring, analysis) under Apache-2.0; the
synthetic surrogate + validation suite released as the instrument-validation artifact; natural-cut
annotations released; the clips themselves distributed as source-URL + timestamp + processing script
where redistribution licenses don't permit direct hosting (CC-licensed sources preferred at curation
time to keep this rare). DiDi is consumed under its own license from the DAM4SAM repo, never
redistributed.

**Ethics.** No human subjects, no personal data collection; natural-cut curation excludes clips
centering identifiable private individuals (broadcast/sports/produced footage preferred). Dual-use
surface: an arbitration map could, in principle, inform evasion of tracking systems (where and when a
tracker loses identity); assessed as low marginal risk — distractor drift is already publicly
documented and actively published on (DAM4SAM, SAMURAI, DiDi); the probe adds characterization, not
an attack tool; findings are equally useful for hardening (the fix-evaluation arm exists for exactly
that). Compute footprint is deliberately small (≤ 5 GPU-days total, inference-only) — the cheapest
protocol in the Stage-5 set.

**Model/data licenses.** SAM2/SAM3 code+weights under their Meta releases (Apache-2.0 code;
checkpoint licenses honored); DAM4SAM and SAMURAI from official repos with pinned commits; COCO/LVIS/
DAVIS/MOSE/SA-V under their respective research licenses — all standard research use, no
redistribution of model weights or benchmark images in the release.
