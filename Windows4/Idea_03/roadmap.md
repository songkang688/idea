# Roadmap — AlphaSmoke (gate-ordered; no step starts before its gate)

Full runbook with dependencies and compute plans: `experiments.md` §4. Order is
binding; calendar estimates are deliberately omitted — gates, not dates.

1. **R0 — license/access audit** (`datasets.md`); freeze the operating threshold
   τ_op against released FoSp/SMOKE5K eval code.
2. **R1 — metric cross-check**: `src/alphasmoke` vs released eval code (mMse/Fβ
   definitional match); self-tests green (`tests/`).
3. **R2 — week-1 killer: frozen-encoder linear probe** (`configs/linear_probe.yaml`).
   **GATE K-A1:** no separation at any budget ⇒ pretrain grid is NOT funded; Part A
   demotes to probe + floors.
4. **R3 — Part B pillar 1 (eval-only)**: checkpoint pool inference + τ matrix on
   synthetic alpha, mMse/Fβ columns included.
5. **R4 — rater study launch** (calendar-parallel; `configs/rater_study.yaml`).
   **GATE K-B4:** ceiling > 0.85 IoU ⇒ pillar demoted to appendix.
6. **R5 — measured-alpha capture + recovery** (`configs/alpha_capture.yaml`).
   **GATE K-B5:** QC fail ⇒ reversal headline withdrawn (fallback per proposal §5.2).
7. **R6 — controlled pretrains M/MB (+ matched-count S subsample)** — only if R2
   passed.
8. **R7 — fine-tune sweep** arms × budgets × seeds, floors scored in every cell
   (**K-A2..K-A5** evaluated here).
9. **R8 — final τ matrix** incl. measured-alpha rankings (**K-B1..K-B3**).
10. **R9 — write-up** along whichever decision-tree branch was taken
    (`experiments.md` §3); failure ledger (§7) reported as-is if hit.
