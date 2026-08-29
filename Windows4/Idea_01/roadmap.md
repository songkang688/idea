# SeeingInside — Roadmap

Execution is ordered by information-per-GPU-hour, not by calendar. Each step names its
gate: what must be true to proceed. Backups per `stage4_top20.md`: P063 RefractionFeatures,
P079 MemoryProbe.

## Phase 0 — Harness validation (CPU, done in this package)

- [x] Prototype harness: dataset, interventions, nulls, metrics, decision logic (`src/`).
- [x] **E0** stub validation: BoxFillBaseline must be classified "interpolator", OracleThreshold
      stub must be classified "seeing" (ACTUAL smoke-test output recorded in `experiments.md`).
- [x] Thresholds τ1–τ3, strata, seeds frozen in `configs/default.yaml` (this commit predates
      any real-SAM forward pass — that is the pre-registration).
- **Gate:** E0 passes both stub classifications. → PASSED (see experiments.md §E0).

## Phase 1 — Real-model bring-up (first GPU session)

- [ ] Install `segment-anything`, fetch ViT-B + ViT-H checkpoints; wire `OfficialSAMWrapper`
      (interface already in `src/model_sam.py`; no code redesign expected).
- [ ] Golden-set check: 20 COCO instances, intact condition — Dice in the published
      ballpark for GT-box prompting (sanity only, no thresholds).
- [ ] Freeze the two instance lists (500 COCO / 500 medical) and commit them.
      Medical cohort selection per proposal §14 (lowest two contrast deciles,
      MedSAM-protocol datasets).
- [ ] Select + validate diffusion inpainter; run the quality screen; commit the tool
      citation to `literature.md` (deferred-citation slot).
- **Gate:** golden-set sanity passes; counterfactual quality screen rejects < 30% of
  generations (else switch inpainter before spending E1 compute).

## Phase 2 — E1 Killer experiment (≈ 2–3 GPU-days)

- [ ] Generate counterfactual cache (object-out + object-swap, 1000 instances).
- [ ] Train learned box→mask null per domain (`src/train.py`, < 1 GPU-hour).
- [ ] Full condition × padding grid, medical first (`src/eval.py`).
- [ ] Compute CSG, persistence, swap-tracking, NRF + bootstrap CIs; apply the
      pre-registered conjunction per stratum.
- **Gates (pre-registered, binding):**
  - **KILL:** intact-vs-counterfactual gap > 15 Dice pts in *every* stratum →
    write negative-result note; escalate backup P063/P079; stop this project.
  - **INSTRUMENT-KILL:** sham-inpaint moves Dice > τ1/2 → swap-only fallback; if classical
    and diffusion instruments disagree on verdicts → report instrument failure; stop.
  - **PIVOT-1:** NRF > 1 broadly on medical → re-scope to protocol-degeneracy audit.
  - **PROCEED:** H1 conjunction holds in the low-contrast medical stratum → Phase 3.

## Phase 3 — Consolidation program (≈ 4–6 GPU-days)

Order fixed; later items dropped first under compute pressure:

1. **E2** secondary convergence checks (patch-shuffle S-604, embedding-mean S-014, noise) —
   the demoted probes, run for the convergence row of the verdict conjunction.
2. **E4** decoupling: padding vs ablation-dilation; realistic-box (loose) arm; point-prompt arm.
3. **E3** regime map: CSG/NRF surfaces over contrast × solidity × size.
4. **E5** model generality: ViT-B/L/H; MedSAM checkpoint (EXPECTED: higher NRF); SAM-2 image
   mode if trivially wireable.
5. **E6** instrument robustness: second diffusion inpainter; classical arm on full set.
6. **E7** swap-content gradient: same-class / other-class / texture-only swaps.

- **Gate to writing:** E2 convergence row complete and E4 decoupling clean (no reversal of
  the E1 verdict). E3/E5–E7 enrich but cannot reverse the claim as pre-registered.

## Phase 4 — Paper & release

- [ ] Paper: medical-led story (MICCAI-timed) if H1-medical only; vision-venue framing
      (CVPR/ICCV-class) if the regime map is rich across domains.
- [ ] Release: harness + frozen instance lists + counterfactual scripts + per-instance
      tables + null checkpoints (proposal §25); medical counterfactuals as scripts/hashes
      where redistribution is restricted.
- [ ] Repo hygiene: every reported number traceable to a results JSON in the artifact dir;
      EXPECTED→ACTUAL tag flips only via committed result files.

## Standing rules

- No threshold motion after Phase 0 (this commit is the pre-registration).
- Off-manifold probes never headline (R2 obligation).
- No merge with P107v/HalluSegBench under any framing pressure (Stage-6 ruling).
- If two consecutive gates fail for instrument reasons (not hypothesis reasons), the
  project returns to the Windows4 supervisor for a backup swap rather than instrument
  archaeology beyond one replacement attempt.

## Dependency graph

```
Phase 0 (done) ──► Phase 1 bring-up ──► E1 killer ──┬─ KILL ──► negative note + backups
                                                    ├─ PIVOT-1 ──► protocol-degeneracy audit
                                                    └─ PROCEED ──► E2 ─► E4 ─► E3/E5/E6/E7 ─► paper
```
