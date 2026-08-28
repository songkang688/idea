# Proposal — AlphaSmoke (P103 + P096 protocol)

## 1. Executive Summary

Smoke is density, but leaderboards are binary Dice. We test a **transfer hypothesis** (matting pretrain → smoke) and a **metric hypothesis** (rank reversal). Not detector+SAM2 (ProFSAM). Not SAM-alpha head (Matting Anything).

## 2. Motivation

Fire/smoke safety cares about thin plumes. Dice rewards fat masks (S-112).

## 3. Problem

Given RGB x, predict binary smoke and/or alpha α∈[0,1]. Compare encoders and metrics.

## 4. Hypotheses

**H-transfer:** Matting-pretrained encoder + linear probe beats COCO-seg-pretrained encoder on real-smoke mIoU at matched probe data.

**H-metric:** Kendall τ between Dice ranking and mMse/SAD ranking is < 0.5 on a model zoo.

## 5. Insight

The missing supervision is **transparency**, not another SAM adapter.

## 6. Novelty

DenSiSeg uses SAM as background prior (crowded). Matting Anything puts a matte head on SAM. We: **pretrain domain transfer** + **evaluation protocol**, with HSV baseline.

## 7. Literature

FoSp AAAI 2024 (mMse/Fβ); SFMattingNet 2025; Matting Anything CVPRW 2024; ProFSAM fire+SAM2 (difference: we do not do detector-prompted fire); Yuan TIP 2020 density.

## 8. Method

Encoders frozen; 1×1 conv or linear on tokens; optional light decoder. Color baseline: HSV + Otsu in a smoke hue band.

## 9. Diagram

`diagrams/architecture.md`

## 10. Math

Probe: \(\min \|W\phi(x)-y\|^2\). Metrics: Dice, mIoU, mMse, SAD if alpha GT exists.

## 11. Implementation

`src/metrics_alpha.py`, `src/hsv_baseline.py`, `src/probe.py`

## 12. Data

Public smoke (e.g. SMOKE5K if licensed). **Do not commit images.** Synthetic alpha composites only as a diagnostic split.

## 13. Baselines

HSV; DeepLab-style if user has weights; frozen SAM everything (likely fails on stuff).

## 14. Metrics

Primary: real-smoke mIoU/Fβ. Secondary: mMse on synthetic or measured-alpha subset.

## 15–17. Matrix / killer

See `experiments.md`. Killer = HSV vs two frozen probes on n small.

## 18. Expected

**EXPECTED:** matting encoder wins thin-smoke Fβ; Dice ranking disagrees. **ACTUAL:** none.

## 19–20. Failures

If HSV wins, deep transfer is unnecessary (publish that). If no rank reversal, P096 dies; keep transfer if H-transfer holds.

## 21–22. R2

Synthetic-alpha circularity → real-smoke primary. Binarized-matting arm: train matting encoder on binarized mattes (control).

## 23. Compute

1×12GB, 1–2 days probes.

## 24. Roadmap

Day 1: HSV + metrics. Day 2–3: linear probes. Week 1: rank matrix on 4 models. Week 2: measured-alpha subset if camera-static data exists.

## 25. Stop

Kill transfer if HSV ≥ both probes. Kill metric paper if τ>0.8. Continue if either H holds.

## 26. Extensions

SAM2 video flicker as turbulence (A1-049) — not this paper.

## 27. Story

“Smoke papers optimize Dice on fat plumes; matting pretraining and matting metrics tell a different story.”

## 28. Titles

- From Mattes to Plumes: Does Transparency Pretraining Transfer?
- When Dice Lies: Metric Reversal in Smoke Segmentation
- Color, Mattes, and Smoke: An Honest Baseline Study
