# PromptAmnesia — Execution Roadmap (Windows4 / Idea_02)

**Epistemic status:** PLAN. Phases are dependency-ordered with GPU-day ESTIMATES; no calendar dates.
Binding order (Stage 4/6): **P082 gate first → grid freeze → P065 → (P031 sibling) → P177.**

---

## Phase 0 — Environment + pre-registration freeze (E0)

Blocks everything downstream.

- [ ] Reproduce environment from `requirements.txt`; smoke-test `src/promptamnesia/` CLIs (`--dry-run`).
- [ ] Download + hash-pin assets: SAM ViT-B/H, MedSAM, SAM-Med2D checkpoints; COCO val2017, LVIS-rare
      index, BUSI, MSD Task09, TN3K. Record hashes in `configs/` (amendment commit).
- [ ] Scoop-watch searches (`literature.md` §6); update related-work deltas if hits.
- [ ] **Release blocker:** re-verify every `[M]`-tagged citation quoted in the pre-registration text.
- [ ] Build + freeze ambiguity-probe mining protocol and both click simulators.
- [ ] Tag **`idea02-prereg-v1`** (freezes: grid recipe, matched-gain rule, contrast family O1–O5, gate
      target list, envelope definition, stitch families).

**Exit gate G0:** tag exists; all assets hashed; dry-run matrices generate.
Compute: CPU + download bandwidth only.

## Phase 1 — P082 gate (E1) — ESTIMATE 1–2 GPU-days

- [ ] Frozen-model variance decomposition → envelope per (domain × prompt type)
      (`threshold_gate.py::build_envelope`).
- [ ] B6 control: eval-only variance replicates on released fine-tuned checkpoints; operative envelope =
      per-cell max.
- [ ] Re-evaluate MedSAM / SAM-Med2D under (a) their published protocols, (b) the symmetric protocol.
- [ ] Compare pre-registered target deltas vs envelope → `gate_decision`.

**Exit gate G1 (decision point):**
- **PROCEED** (≥1 checkpoint outside envelope on ≥2 domains, ≥1 prompt type) → Phase 2.
- **PIVOT** → Phase 2', deflation branch: paper = envelope + symmetric re-evaluations + Biderman-coupling
  confirmatory regression on a minimal grid (ESTIMATE 5–8 GPU-days total). Idea_02 re-scopes; supervisor
  notified per `stage6_battle.md` decisive-experiment list item 1.

## Phase 2 — Shared checkpoint grid (E2) — ESTIMATE 25–45 GPU-days (≈204 short runs)

- [ ] Launch grid per `configs/shared_grid.yaml` (domains × mixes × recipes × seeds; covariate logging on).
- [ ] Mid-grid audit after first domain completes: verify matched-gain bands are reachable per arm; if an
      arm never reaches band, log per A7/B7 (no recipe changes — grid is frozen).
- [ ] B1 robustness cell (perturbed mixed distribution) on headline domain (+2–3 GPU-days).
- [ ] Update-norm-matched arm for P177 (added only on PROCEED).
- [ ] Hand checkpoint manifest to sibling P031.

**Exit gate G2:** all cells trained or explicitly logged as failed; manifest committed (hashes, seeds,
configs); matched-gain selections computed and committed.

## Phase 3 — Battery + diversity evaluation (E3 + E4) — ESTIMATE 3–6 GPU-days

- [ ] Full prompt-type eval matrix over matched-gain checkpoints (4 columns × retention suites ×
      symmetric thresholds), `eval_prompt_matrix.py`.
- [ ] Dual-simulator duplicates of headline contrasts.
- [ ] Ambiguity probes: oracle-vs-argmax per checkpoint (`diversity.py`); B3 human spot-audit of probe
      subsample.
- [ ] Statistics: hierarchical bootstrap, Holm over O1–O5, envelope conjunction; RQ5 coverage map from
      off-diagonal + box-only column.

**Exit gate G3 (claim triage):**
- H2/H3 survive in mixed column → flagship branch continues.
- Mixed column null → Branch C (coverage paper) locked; Phase 4 becomes optional descriptive appendix.
- O4 resolves to ranking-loss → diversity claim transferred to P031 (log the transfer).

## Phase 4 — P177 mechanism arm (E5) — ESTIMATE 2–4 GPU-days

- [ ] Train stitches (both families, capacity-capped) per swap cell; stitch-only calibration cells.
- [ ] Both-direction swap grid × {stitch, no-stitch}; α-interpolation curves per module group.
- [ ] Restoration fractions per prompt type with CIs; verdict per pre-registered rule (H5).

**Exit gate G4:** locus verdict (stands / withdrawn-descriptive) logged with artifacts.

## Phase 5 — Analysis, writing, release

- [ ] Assemble reporting panel (P110 residue) as appendix: per-prompt-type retention, gain-vs-retention
      frontier per arm, model-card rows.
- [ ] Exploratory-only appendix: drift-covariate lead-time glance (P108 residue; resurrection criteria per
      proposal §28).
- [ ] Failure enumeration appendix (excluded arms, rejected probes, simulator-flipped contrasts).
- [ ] **Release blockers:** every quoted `[M]` citation re-verified; every reported number traceable to a
      run artifact (config hash + seed + commit); obligations checklist (reviewer_attacks Part I) signed
      off item-by-item.
- [ ] Venue: main-track CV venue (MICCAI variant if medical story dominates); deflation branch may target
      an earlier deadline given its 5–8 GPU-day footprint.

---

## Standing rules across phases

1. Commit + push after every phase exit gate (this branch: `cursor/windows4-research-idea-evolution-2962`).
2. Any dropped obligation → logged amendment here + corresponding claim withdrawn (reversion rule).
3. No number leaves the repo without an epistemic label; EXPECTED RESULT never silently becomes
   ACTUAL EXPERIMENTAL RESULT.
4. Backup ideas if a killer experiment dies at G1–G3 with no salvageable branch: P063 RefractionFeatures,
   P079 MemoryProbe (per `stage4_top20.md`).

## Budget summary (ESTIMATES, single A100-class GPU)

| Phase | GPU-days |
|---|---|
| 1 (gate) | 1–2 |
| 2 (grid) | 25–45 (robustness cells included) |
| 3 (battery) | 3–6 |
| 4 (mechanism) | 2–4 |
| **Total flagship branch** | **≈ 35–55** |
| Pivot branch total | 5–8 |
