# Windows2

- **Windows ID:** Windows2
- **Created:** 2026-08-28
- **Supervisor:** Windows2
- **Status:** COMPLETE — final 3 research packages archived.

## This round's three ideas

| Rank | Seat | ID | One-liner |
| --- | --- | --- | --- |
| **#1** | `Idea_01/` | **C-0306** | NMS silently destroys conformal coverage; coverage-preserving suppression restores it. |
| **#2** | `Idea_02/` | **A-0028** | Teleport probes measure SAM2/SAM3 appearance-vs-location arbitration that fix-papers presuppose. |
| **#3** | `Idea_03/` | **B-0114** | 4-arm dense-task VPT-as-registers (not the original VPT frozen-prompt ablation). |

## Most recommended

**C-0306.** It is the only constructive method in the set, ranked #1 independently by Stage-5 ROI and three consecutive battles, and the first experiment is analysis-only (2–4 GPU-days) on cached pre-NMS candidates.

## Next experiment to run

**C-0306 H1 gate:** harvest pre-NMS candidate boxes from a small detector zoo on COCO val; measure the **blind-spot rate** (GT objects whose only covering candidates NMS removes), stratified by crowding and NMS IoU.

Same week: A-0028 1-GPU-day SAM2-L teleport battery; B-0114 only after its exp_02 gate on a real frozen backbone.

Synthetic prototype numbers are **not** COCO / SAM2 / ADE20K results.

## Project status

| Project | Path | Prototype tests (CPU) |
| --- | --- | --- |
| Idea_01 C-0306 | `Windows2/Idea_01/` | 27 passed |
| Idea_02 A-0028 | `Windows2/Idea_02/` | 23 passed |
| Idea_03 B-0114 | `Windows2/Idea_03/` | 39 passed |

Evolution trail: `Windows2/selection_history/` and `Windows2/_wip/`.

## Git safety

This tree is **Windows2/** only.
