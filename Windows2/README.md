# Windows2

- **Windows ID:** Windows2
- **Created:** 2026-08-28
- **Supervisor:** Windows2
- **Status:** Final 3 selected. Full packages and remaining prototypes in flight.

## This round's three ideas

| Rank | Seat | ID | One-liner |
| --- | --- | --- | --- |
| **#1** | Idea_01 | **C-0306** | NMS silently destroys conformal coverage; coverage-preserving suppression restores it. |
| **#2** | Idea_02 | **A-0028** | Teleport probes measure SAM2/SAM3 appearance-vs-location arbitration that fix-papers presuppose. |
| **#3** | Idea_03 | **B-0114** | 4-arm dense-task VPT-as-registers (not the original VPT frozen-prompt ablation). |

## Most recommended

**C-0306.** It is the only constructive method in the final set, ranked #1 independently by the Stage-5 ROI ranking and three consecutive battles, and its killer experiment is analysis-only (2–4 GPU-days) on cached pre-NMS candidates.

## Next experiment to run

C-0306 H1 gate: harvest **pre-NMS** candidate boxes from a small detector zoo on COCO val, measure the **blind-spot rate** (GT objects whose only covering candidates NMS removes), stratified by crowding and NMS IoU. A CPU synthetic prototype already exists at `Windows2/_wip/stage7_proto_C0306/` (not a COCO result).

Same week, co-schedule A-0028's 1-GPU-day SAM2-L teleport battery (`Windows2/_wip/stage7_proto_A0028/` is the instrument, not the SAM2 measurement).

## Project status

| Project | Package | Prototype |
| --- | --- | --- |
| Idea_01 C-0306 | **`Windows2/Idea_01/`** | complete (synthetic; 27 tests) |
| Idea_02 A-0028 | **`Windows2/Idea_02/`** | complete (synthetic; 23 tests) |
| Idea_03 B-0114 | drafting under `_wip/package_draft_B0114/` | complete (synthetic) |

Do not treat `_wip` synthetic numbers as COCO/SAM2 benchmark results.

## Git safety

This tree is **Windows2/** only.
