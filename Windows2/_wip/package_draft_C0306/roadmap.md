# Roadmap — C-0306

Execution plan keyed to the pre-registered gate (experiments.md E1). Binding process constraints
carried from the pipeline: **execution must start within the quarter or the seat converts to a kill
(Q, ⏰); two-quarter total execution clock (K); freshness re-search at proposal freeze AND experiment
freeze AND quarterly.** No training anywhere; the only GPU phase is detector inference for caching.

## Day 1 — freeze and validate

- [ ] **Pre-registration commit:** detector zoo (exact checkpoints), crowdedness stratum definitions,
      gate decision thresholds (≥5% open / 2–5% scope / <1–2% fail), α levels, τ levels, split seeds.
      One commit; nothing in it changes afterwards without a logged amendment.
- [ ] **Freshness re-search #1 (proposal freeze):** run the six query families in `literature.md` §7;
      resolve the U1–U4 UNVERIFIED citations; log results. Kill trigger: printed blind-spot
      measurement or coverage-preserving suppression rule.
- [ ] Cache-format validation: 1 detector × COCO val with post-processing disabled; confirm the
      `(gt_boxes, cand_boxes, cand_scores)` triple drops into this package's loaders; measure
      per-image cache size to recalibrate the storage estimate.
- [ ] CI green on this package (27 tests) in the execution environment.

## Day 2–3 — cache and first real table

- [ ] Launch full caching: 5–8 detectors × {COCO val, LVIS val, CrowdHuman val} (2–4 GPU-days
      wall-clock; overlaps analysis work).
- [ ] Point `blind_spot` analysis at the validated real cache (loader swap — no analysis-code
      changes by design).
- [ ] **First real blind-spot table** on the validation detector; E1-S sensitivity variants wired.

## Week 1 — the gate

- [ ] Complete E1 gate matrix (~1,440 cells) over the zoo with CIs + image-level bootstrap.
- [ ] E1-S GT-quality sensitivity (ignore regions, LVIS exhaustive-only, conditional form).
- [ ] E2 coverage-destruction run (pipelines A/B) — consistency check against the dominance bound.
- [ ] **GATE DECISION against the pre-registered table.**
  - FAIL → write the measurement note from Week-1 assets (skeleton: proposal §20 + §27 closing);
    release cache + code; stop. Named consequence (Q): the conformal slot is freed.
  - SCOPE → continue, crowded strata only; retitle per proposal §28 candidates.
  - OPEN → continue, full program.

## Week 2 — method leg first pass

- [ ] E3: pipeline C + achievability-certificate map (q̂ = +∞ cells); begin full SeqCRC
      reimplementation.
- [ ] E4 first pass: CPS (κ, r) grid on gate-open strata; trivial anchors (top-k, threshold sweep);
      soft-NMS / class-aware arms.
- [ ] WACV-2024 IoU-aware-calibration reimplementation started (K-mandated baseline).
- [ ] DETR-native control arm.
- [ ] First frontier plots; H2 preliminary read.
- [ ] **Freshness re-search #2 (experiment freeze).**

## Weeks 3–6 (full paper push; contingent on gate)

- [ ] Complete E4 (all baselines incl. full SeqCRC + WACV-2024), E5 consumability, E6 ablations
      (incl. τ = 0.75 envelope, exchangeable-unit arm, crowdedness-definition robustness).
- [ ] Optional half-day manual audit of ~100 blind-flagged objects (A9 insurance + Fig. 1 panels).
- [ ] Characterization section (conditions for coverage-safe suppression) — this is also the
      pre-registered pivot destination if WACV-2024 dominates the frontier.
- [ ] `cps_nms()` release artifact + cache release prep.
- [ ] Paper per proposal §27; venue: CVPR/ICCV/ECCV-line main conference; TMLR fallback if the scoop
      clock demands speed; measurement-note fallback stays pre-written regardless.

## Standing clocks and stop rules (mirror of proposal §25)

| Clock/rule | Trigger | Action |
|---|---|---|
| Seat start clock (Q, ⏰) | execution not started within the quarter | seat converts to kill |
| Total execution clock (K) | two quarters elapsed | stop-loss: ship strongest completed asset |
| Scoop re-search | proposal freeze, experiment freeze, quarterly | kill matching leg if printed |
| Gate | E1 table vs pre-registered thresholds | open / scope / note per table |
| Frontier pivot | WACV-2024 dominates everywhere | characterization paper |
| GT-integrity tripwire | gate cell flips across boundary in E1-S | conditional table governs; report |

## Dependencies and risks to the schedule

- Storage (200–500 GB estimate) and pre-NMS hooks per detector are the only Day-1..3 technical risks;
  both have fallbacks (score-floor pruning; drop to 5 detectors) — proposal §19.5.
- WACV-2024 reimplementation is the longest engineering item on the method leg; started Week 2 so it
  cannot block the gate.
- Nothing in the plan waits on training, annotation, or external data collection.
