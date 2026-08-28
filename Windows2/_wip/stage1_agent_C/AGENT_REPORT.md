# AGENT_REPORT - Windows2 Stage 1, Cloud Sub-Agent C

Role: independent idea generator (detection / evaluation / assumptions angle). Stage 1 only. No final-3 selection performed (that is the supervisor's job). `Windows2/README.md` intentionally not written.

## Deliverables

| Path | Contents |
|---|---|
| `Windows2/_wip/stage1_agent_C/ideas.jsonl` | 345 ideas, one JSON object per line (source of truth) |
| `Windows2/_wip/stage1_agent_C/ideas.md` | Same 345 ideas, human-readable, grouped by cluster |
| `Windows2/_wip/stage1_agent_C/clusters.md` | Cluster map: 12 clusters, ID ranges, counts, high-ROI picks |
| `Windows2/_wip/stage1_agent_C/AGENT_REPORT.md` | This report |

## Count

- **345 ideas** (requirement: at least 340), IDs `W2-C-0001` ... `W2-C-0345`, contiguous, unique, all lines valid JSON.
- Every idea has: problem, falsifiable hypothesis, cheapest experiment, ROI estimate.
- Cluster distribution: C1 detection limitations 40; C2 evaluation weakness 40; C3 unproven assumptions 35; C4 surprising phenomena 30; C5 negative results 30; C6 robustness/calibration/UQ 25; C7 domain shift/syn2real 25; C8 SR/restoration/generation tied to dense prediction 25; C9 long-tail/metric fairness/dataset bias 30; C10 reproducibility/compute-fairness 25; C11 motivated combinations 20; C12 belief-challenging simple hypotheses 20.

## Scientific-rule compliance

- No forbidden mashups (no "YOLO + Transformer", no attention-for-detection, no "apply DETR to X", no loss-only or backbone-only ideas).
- No fabricated citations or results anywhere; empirical statements inside hypotheses are predictions to be tested, not claims. A standing header in `ideas.md` marks the novelty of **all** ideas as UNVERIFIED - needs lit search; ideas resting on an additional specific presumption about prior work carry an individual UNVERIFIED note (W2-C-0001, 0014, 0019, 0050, 0055, 0062, 0079, 0117).
- Cluster 11 combinations each state their genuine scientific motivation inline.

## 15 highest-ROI one-liners

1. **W2-C-0046** - Propagate measured annotation noise into COCO AP confidence bands; test whether typical SOTA increments are statistically distinguishable at all.
2. **W2-C-0136** - Train 10 seeds of 3 standard recipes and publish the variance components that decide how much of the detection leaderboard is luck.
3. **W2-C-0283** - Re-run the baselines of 20 recent papers under modern recipes to measure how much "progress" is stale-baseline decay.
4. **W2-C-0328** - Show a stratified 1k-image subset reproduces full-benchmark detector rankings, collapsing evaluation cost for the whole field.
5. **W2-C-0032** - Bootstrap LVIS AP-rare to test whether the long-tail leaderboard is ranking sampling noise.
6. **W2-C-0226** - Ground-truth-controlled test of whether super-resolution recovers detection-relevant information or hallucinates texture that fools metrics.
7. **W2-C-0082** - A falsification atlas mapping exactly which domains SAM-style zero-shot segmentation actually works in, and which descriptors predict failure.
8. **W2-C-0081** - Compute-matched rank-correlation audit of the assumption that better classification pretraining means better dense-task transfer.
9. **W2-C-0003** - Oracle-suppression experiment quantifying how much crowded-scene error is NMS, not detection.
10. **W2-C-0158** - Show temperature scaling fitted pre-NMS leaves post-NMS outputs miscalibrated, relocating where detection calibration must happen.
11. **W2-C-0159** - Preregistered multi-codebase replication testing whether detection active learning beats random sampling at realistic batch sizes.
12. **W2-C-0057** - Human-verify high-confidence "false positives" to measure how missing annotations tax better detectors and invert rankings.
13. **W2-C-0011** - Measure whether prompt-template variance exceeds the architecture deltas that open-vocab detection papers report.
14. **W2-C-0116** - Inpaint objects out of scenes and measure how often detectors still see them: context-driven ghost detections as a safety metric.
15. **W2-C-0327** - Train 2015-era Faster R-CNN under a 2026 recipe to decompose a decade of detection progress into recipe vs architecture.

## Hashes (sha256)

- `ideas.jsonl`: `f85678a5814992431925cedd283b9e540f47a93beb935b987c84b2a0577b2218`
- `ideas.md`: `f86dde3912a4884b070eb118e7ece7c95dd714321c768aececfe5f082058993c`
- `clusters.md`: `5137d580a74182cfe26941bdc746ddcdba717bf83192b1ce88e20902bbc0b61b`

Commit hash and push status: see git history for commit `Windows2 Stage1 Agent C: detection/eval/assumption idea catalog` on branch `cursor/windows2-stage1-agent-c-70ca` (recorded at push time; a file cannot contain its own commit hash).
