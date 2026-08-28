# Idea_02 proposal

## Executive summary

Smoke/fire CCTV datasets often share cameras across train/val. A Voxel51 audit of Pyro-SDIS reported massive near-duplicates as **shared-camera familiarity** (KNOWN as a blog diagnosis, not a peer-reviewed mAP delta). PYRONEAR-2025 uses **event-disjoint** splits (https://arxiv.org/abs/2402.05349). Reviewer #2: survive iff we measure **random vs event-disjoint vs camera-disjoint** with CIs and a **background-memorization probe**.

**We have not trained a detector here.** Code is a split-simulator + camera-ID linear probe on synthetic features.

## Hypothesis

**H1:** Camera-disjoint mAP < random-split mAP by more than seed std.

**H2:** Event-disjoint mAP ≠ camera-disjoint mAP (residual same-camera different-event leakage).

**H3:** A linear probe on backbone features predicts camera ID above chance on a held-out time split.

**H4:** Empty (no-smoke) frames from train cameras have higher FP or confidence than empty frames from unseen cameras.

## Novelty

Not “datasets leak.” The paper is **quantified inflation + confounder split** (geography vs memorization). Fatal if we only report camera-disjoint drop without H4.

## Kill

If camera-disjoint drop vanishes after event-disjoint; or camera-ID probe is chance; or only one tiny camera set.
