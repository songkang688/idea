# Windows8 — Autonomous Research Idea Evolution

- **Windows ID:** Windows8
- **Created:** 2026-08-28 (UTC)
- **Supervisor:** Windows8 (PI)
- **Repo:** `github.com/songkang688/idea`

This tree is exclusive to this round. Other Windows directories on sibling branches were not modified.

## This round’s three Ideas

1. **Idea_01 — Objectness, Not Features** (recommended): frozen SAM embeddings + density/exclusion vs prompted SAM on amorphous targets, with a COCO control.
2. **Idea_02 — Spectral Locality of Dense PEFT:** LoRA feature deltas are hypothesized to be spatially low-pass; test high-frequency residual vs extra rank.
3. **Idea_03 — Selective SAM via IoU-token Recalibration:** SAM IoU tokens hypothesized anti-calibrated on amorphous domains; risk-coverage vs adapters.

## Most recommended

**Idea_01.** It is the cheapest falsifier of the “fine-tune the encoder” default, and prior work already occupied the eval-only and adapter-SOTA slots.

## Why

- Not Med-SA / LoRA-MedSAM (those are methods without a locus-of-failure test).
- Not “SAM fails on fire/glass” (already evaluated).
- Killer experiment is one GPU-day and can kill the project honestly.

## Project status

| Package | Status |
|---------|--------|
| Idea_01 | Ready to start E0 (needs real SAM weights for science; toy loop runs) |
| Idea_02 | Ready to start FFT audit |
| Idea_03 | Ready to start reliability dump |

## Next experiment to run

Idea_01 E0 (see `Idea_01/experiments.md`). Do not report FakeEncoder numbers as results.

## Candidate titles

- Objectness, Not Features: Where Segment Anything Actually Fails on Amorphous Targets
- LoRA Is a Low-Pass Adapter: Spectral Locality of PEFT for Dense Prediction
- When SAM Is Sure and Wrong: Selective Segmentation via IoU-Token Recalibration
