# C-0306 Research Package — Conformal Coverage vs NMS + Coverage-Preserving Suppression

**Status: DRAFT in `_wip/` — awaiting final Idea_* numbering by Agent S. Copy this directory to
`Windows2/Idea_XX/` unchanged once numbering is decided; nothing in it depends on its current path.**

- **Idea ID:** W2-C-0306
- **One-liner:** Conformal coverage guarantees are silently destroyed by NMS (the *blind spot*:
  GT objects whose every covering candidate gets suppressed — unrecoverable by any threshold), and a
  coverage-preserving suppression rule (CPS) with a provable Jaccard-triangle-inequality transfer
  restores them at competitive set size.
- **Design:** gate-first. The killer experiment is a 2–4-GPU-day, analysis-only measurement of the
  blind-spot rate across detectors × datasets × NMS thresholds × crowdedness. The method leg is built
  only if the pre-registered gate opens. Both outcomes publish.
- **Prototype:** included and runnable (`src/`, CPU-only, 27 tests, no data/weights needed).

```
NO NUMBER IN THIS PACKAGE IS A COCO / LVIS / CROWDHUMAN RESULT.
All measured numbers are synthetic mechanism demos, labeled MEASURED (synthetic).
Real-data magnitudes are exactly what the killer experiment exists to measure.
Epistemic labels used throughout: KNOWN / EVIDENCE / HYPOTHESIS / MEASURED (synthetic).
```

## Package layout

| Path | Contents |
|---|---|
| `proposal.md` | the full proposal — all 28 required sections (executive summary → candidate titles) |
| `literature.md` | survey with per-citation verification tags + freshness-search protocol |
| `experiments.md` | pre-registered protocol E0–E6: gate, decision table, baselines, statistics |
| `reviewer_attacks.md` | 10 strongest attacks (incl. Stage-4 K's) with responses + residual risks |
| `roadmap.md` | Day 1 / Day 2–3 / Week 1 / Week 2 / full-paper plan + standing clocks |
| `diagrams/` | mermaid sources: architecture, four pipelines, gate/stop/pivot logic |
| `src/` | **runnable prototype** (copied from `stage7_proto_C0306`, path-adjusted; see `src/README.md`) |
| `configs/` | committed synthetic operating points (fixed seeds; copied from the prototype) |
| `references/` | `references.md` (tagged link table) + `refs.bib` (verified entries only) |

## Quickstart (prototype)

```bash
pip install -r src/requirements.txt
python src/run_synthetic.py                                        # 3 strata, deploy NMS IoU 0.5
python src/run_synthetic.py --config configs/crowded_aggressive.yaml
python -m pytest src/tests/ -q                                     # 27 tests, ~5 s
```

## Provenance chain (pipeline-internal)

Stage-2 D bet #10 SURVIVE (`stage2_agent_D/prior_work_attack.md` §E1) → G LOCK / M
mission-protected (`stage3_agent_M/top50.md` #31) → Stage-4 K **SURVIVE-IF-EXPERIMENT**
(`stage4_agent_K/reviewer2_attacks.md` §27: blind-spot magnitude is the gate; WACV-2024 baseline
mandatory; third conformal-OD paper expected within months) → Stage-5 N killer-experiment protocol
(`stage5_agent_N/exp_05.md`) → Stage-6 O top-20 #1 / Q top-5 #1, constructive/method seat,
execute-first (`stage6_agent_Q/top5.md`) → Stage-7 P synthetic prototype (`stage7_proto_C0306/`) →
this package (Stage-7 Agent U). PI binding: gravity MUST include ≥1 C idea (this and/or C-0338).

## The two headline claims (both falsifiable, neither yet measured on real data)

- **H1 (gate):** a non-trivial fraction of GT objects lose ALL covering candidates to standard NMS,
  growing with crowdedness and NMS aggressiveness. Pre-registered materiality: ≥5% opens the gate;
  <1–2% everywhere kills the method leg (measurement note ships instead).
- **H2 (method):** CPS achieves nominal coverage with smaller sets than no-NMS IoU-aware calibration
  (WACV 2024) and strictly better suppressed-stratum coverage than SeqCRC-style post-NMS calibration,
  in at least the crowded regime.

## Binding constraints carried into execution

- Execution starts within the quarter or the seat converts to a kill (Q, ⏰).
- Two-quarter total execution clock (K).
- Freshness re-search at proposal freeze + experiment freeze + quarterly (queries in
  `literature.md` §7); printed scoop kills the matching leg.
- WACV-2024 no-NMS baseline is mandatory (K); full SeqCRC construction must be implemented for the
  paper (current pipeline C is its skeleton and is labeled as such).
