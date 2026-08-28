# Windows2 Research Summary (live ledger)

## Pipeline

1000+ ideas → 200 → 50 → 20 → 5 → 3 executable research packages.

## Current stage

**Stage 1 still open** (Agents A, B running). **Stage 2/3 started early on batch C only** — independent scoring + adversarial prior-work kill on C high-ROI set. Global 1000→200 ranking waits until A+B catalogs land.

| Agent | Focus | Status | Count |
| --- | --- | --- | --- |
| A | SAM / medical / ambiguous-object segmentation | RUNNING | pending |
| B | VFM / VLM / PEFT / forgetting | RUNNING | pending |
| C | Detection / evaluation / unproven assumptions | COMPLETE | 345 (`W2-C-0001`–`0345`) |
| D (next) | Independent reviewer + novelty assassin on C high-ROI | DISPATCHING | — |

Catalog C lives at `Windows2/_wip/stage1_agent_C/` (imported from `57db2bc` on `cursor/windows2-stage1-agent-c-70ca`).

## Provisional watchlist (NOT Stage-2 survivors yet)

From C's self-nominated high-ROI set, protect until adversarial literature returns:

- Evaluation-science cluster: annotation-noise AP bands, seed-variance decomposition, stale-baseline decay, stratified cheap eval, LVIS AP-rare bootstrap, missing-annotation tax
- Assumption-kill cluster: SAM zero-shot domain atlas, classification-pretrain ≠ dense transfer, prompt-template variance vs architecture delta
- Mechanism cluster: NMS vs detection in crowds, pre-NMS vs post-NMS calibration, context-ghost detections, SR hallucination vs information
- Recipe-vs-architecture: 2015 detector under 2026 recipe; AL vs random at realistic batches

These may be **high significance / medium novelty**. Several are "metaresearch" and will be attacked as "not a CV method paper." Keep them if a killer experiment is cheap and the claim would change how papers are accepted.

## Top candidates (post Stage 2)

*Empty until Agent D returns scores.*

## Unresolved questions

- Are C's evaluation-science ideas already published as dataset-quality / ranking-robustness papers (2023–2026)?
- Which of C's 15 high-ROI items survive exact-prior-work search?
- Agents A/B catalogs still missing — global dedup not possible yet.

## Git safety

This round owns **Windows2/** only. Do not touch other Windows* trees (other concurrent supervisors exist on this repo).
