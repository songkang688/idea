# Idea_01 — Checkpoint Manifest (E0, Day 1)

**Status: TEMPLATE. Nothing below has been downloaded or hashed yet.**

This file is the output of experiment E0, the day-1 gate. Link rot on 2020–2022 checkpoints is this
project's single biggest practical risk, so archival happens before anything else.

## Rules

1. Download, then SHA-256, then mirror to internal storage. In that order.
2. Pin the repository by **commit SHA**, not by branch.
3. If a checkpoint is unobtainable, the panel shrinks and the paper says so. **Do not substitute a
   re-implementation** — a re-implementation is a different model and would silently change what the
   audit measures.
4. `KNOWN FACT` Stage-5 tagged these repos "existence-verified" on 2026-08-28. Existence-verified is
   not fitness-verified. This gate is where that distinction gets resolved.

## Panel

| Method | Family | Source | Rot risk | Downloaded | SHA-256 | Repo commit | Forward pass OK |
|---|---|---|---|---|---|---|---|
| BAM | specialist | OneDrive (`chunbolang/BAM`) | **HIGH** | ☐ | | | ☐ |
| HSNet | specialist | Google Drive (`juhongm999/hsnet`) | **HIGH** | ☐ | | | ☐ |
| PFENet | specialist | `dvlab-research/PFENet` (8 models) | low | ☐ | | | ☐ |
| Matcher | foundation | `aim-uofa/Matcher` | low | ☐ | | | ☐ |
| PerSAM | foundation | `ZrrSkywalker/Personalize-SAM` | low | ☐ | | | ☐ |
| FSSAM | foundation | `Sam1224/FSSAM` | low | ☐ | | | ☐ |
| SegGPT | foundation | HF `SegGptForImageSegmentation` | low | ☐ | | | ☐ |
| SAM / SAM2 | floor | facebookresearch official | low | ☐ | | | ☐ |
| **SAM3-exemplar** | foundation | official, **HF-gated** | access lead time | ☐ | | | ☐ |

## SAM3 access

Requested on: ______
Granted on: ______

Access lead time, not download size, is the risk here. Request on day 1 even though the arm is not
needed until week 2. If access does not land, the paper keeps the foundation-era co-headline using
FSSAM/Matcher/SegGPT and states the SAM3 gap explicitly rather than quietly omitting it.

## Gate outcome

- Methods with verified checkpoints: ____ / 9
- **Continue** if ≥ 4. **Kill** if < 4 (release the harness, publish nothing).
- Decision: ______  Date: ______
