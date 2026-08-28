# Evolution summary — Windows8

Date: 2026-08-28. Supervisor: Windows8.

## Pipeline

| Stage | Target | Actual | Notes |
|-------|--------|--------|-------|
| 1 Raw | ≥1000 | **2766 grid + 350+350 hand batches** | 52 scientific cores × domains × mutations originally in `pool.jsonl`. Cloud Task agents ERROR'd (`request is required...`). Later, [Stage1 ideas batch C retry](bc-7a636a75-321a-50bf-bd04-7ae953ed578d) landed 350 non-template IDEA-C ideas at `batch_C.md` (grid copy: `batch_C_prior.md`). Local Batch A writer produced 350 non-template IDEA-A ideas (`batch_A.md`; grid: `batch_A_prior.md`). Final 3 packages unchanged: C/A hand lists reinforce the same loci (objectness, PEFT spectrum, IoU calibration) rather than displacing them. |
| 2 Review | ~200 | **200** | Priority: causal tests, cheap falsifiers, high-risk/high-reward, reviewer disagreement. |
| 3 Prior-work attack | ~50 | **50** | Default: already published. Killed metric-only Dice ranking (CC-Dice AAAI 2025). Killed “LoRA/Med-SA as a method paper”. |
| 4 Reviewer #2 | ~20 | **19–20** | Kill if no experiment can shut the attack. Killed unfalsifiable SA-1B membership and purely linguistic SAM2-CD. |
| 5 Engineering | ~5 | **5** | ROI = information per GPU-hour. |
| 6 Battle | 3 | **3** | No false consensus; remaining disagreements listed below. |
| 7 Packages | 3 | **3** | Idea_01..03 |

## Stage 5 Top 5 (ROI order)

1. IDEA-X-0004 Spectral LoRA audit (Idea_02)
2. IDEA-X-0001 Exclusion-region / objectness prompting (Idea_01)
3. IDEA-X-0003 IoU-token selective prediction (Idea_03)
4. IDEA-X-0007 Replay to preserve promptability
5. IDEA-X-0002 Density decoder on frozen SAM embeddings (merged into Idea_01 method)

## Stage 6 unresolved disagreements

- Whether Idea_01 is “just prompting/eval” (Skeptical PI) vs a causal intervention on objectness (Segmentation expert).
- Whether Idea_02 is a vision contribution or a PEFT diagnostic (Methodology reviewer). Decision: keep because it predicts a *new adapter* (high-frequency residual) if the spectrum claim holds.
- Whether Idea_03 is classical selective classification. Decision: keep if we show SAM IoU is *anti-calibrated* on amorphous targets (not merely weakly calibrated).

## Final 3

| Package | Working title | Origin IDs |
|---------|---------------|------------|
| Idea_01 | Objectness, Not Features | X-0001 + X-0002 + SAM-OBJECTNESS + LINEAR-PROBE |
| Idea_02 | Spectral Locality of Dense PEFT | X-0004 + PEFT-SPECTRAL |
| Idea_03 | Selective SAM via IoU-token Recalibration | X-0003 + SAM-IOU-CAL + SELECTIVE |

## Epistemic labels used throughout

KNOWN FACT / EVIDENCE (cited) / HYPOTHESIS / MODEL SPECULATION / EXPECTED (not measured).
No actual experimental numbers were produced in this round.
