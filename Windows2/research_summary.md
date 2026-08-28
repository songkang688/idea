# Windows2 Research Summary (live ledger)

## Pipeline

1000+ ideas → 200 → 50 → 20 → 5 → 3 executable research packages.

## Current stage

**Stage 1 still open** (Agent A running). Batches B and C are in. **Stage 2/3 running in parallel** on C (Agent D) and B (Agent E, dispatching). Global 1000→200 ranking waits for Agent A.

| Agent | Focus | Status | Count |
| --- | --- | --- | --- |
| A | SAM / medical / ambiguous-object segmentation | RUNNING | pending |
| B | VFM / VLM / PEFT / forgetting | COMPLETE | 345 (`W2-B-0001`–`0345`) |
| C | Detection / evaluation / unproven assumptions | COMPLETE | 345 (`W2-C-0001`–`0345`) |
| D | Independent reviewer + novelty assassin on batch C | RUNNING | — |
| E | Independent reviewer + novelty assassin on batch B | DISPATCHING | — |

Running total of original ideas: **690 / 1000+**.

Catalogs: `Windows2/_wip/stage1_agent_B/`, `Windows2/_wip/stage1_agent_C/`.

## Provisional watchlist (NOT Stage-2 survivors yet)

**Batch C (eval/detection metaresearch):** annotation-noise AP, seed variance, stale baselines, cheap stratified eval, SAM domain atlas, NMS vs detection, calibration location, SR hallucination.

**Batch B (VFM/PEFT mechanisms):** DINO outlier-token error maps; synonym > architecture variance in open-vocab seg; CLIP modality-gap collapse as robustness predictor; LoRA ≈ rescaled full FT; PEFT invariance-inheritance ceiling; forgetting as rotation not erasure; decoder capacity vs backbone rewrite; linear-probe underestimates dense info; bilinear upsample as frozen-VFM bottleneck; frozen vs tuned shift budget; synthetic data accuracy–calibration trade; medical FM vs natural VFM+readout matched budget; language alignment vs geometric structure; visual CoT as post-hoc theater.

Protect until literature returns: cheap-to-falsify mechanism claims in B often have **higher method-paper fit** than C's metaresearch, but higher "already done in 2024–2026 VFM analysis papers" risk.

## Top candidates (post Stage 2)

*Empty until D/E return.*

## Unresolved questions

- Which B ideas are already DINOv2/CLIP analysis or PEFT theory papers?
- Cross-batch duplicates: C-0081 (pretrain≠dense) vs B frozen/tuned transfer cluster.
- Agent A still missing — medical/SAM-specific novelty unknown.

## Git safety

This round owns **Windows2/** only.
