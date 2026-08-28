# Windows8 research summary

**Date:** 2026-08-28  
**Supervisor:** Windows8  
**Raw ideas:** 2766 (≥1000)  
**Final 3:** Idea_01 Objectness-not-features; Idea_02 Spectral PEFT; Idea_03 Selective IoU tokens

## #1 recommended

**Idea_01 — Objectness, Not Features.**

Cheapest killer experiment, highest chance to change *where* people spend PEFT parameters, and not already published as Med-SA / fire-box eval / CD-concept eval. Precise interaction hypothesis (win amorphous, lose COCO).

## First experiment to run

`Idea_01` E0: cache frozen SAM embeddings; train 1×1 density head vs GT-box prompted SAM on one amorphous set + COCO control. Toy loop: `Idea_01/src/train_density_head.py` (FakeEncoder; **not** a scientific result).

## Status of the three

| ID | Science | Code | Diagram | Literature attack |
|----|---------|------|---------|-------------------|
| 01 | complete package | runnable prototype | mermaid | yes |
| 02 | complete package | FFT toy | mermaid | yes |
| 03 | complete package | reliability toy | mermaid | yes |

## Unresolved risks

- Cloud sub-agents failed or hung; pool is Supervisor-generated from 52 cores × mutations (documented), plus 10 hand ideas.
- Smoke dataset licenses and SAM checkpoints not in this VM.
- Idea_01 can be desk-rejected as a probe paper if the COCO interaction is omitted.
- Idea_02 may be “not CV.”
- Idea_03 dies if E0 shows no calibration domain gap.
