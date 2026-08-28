# Idea_01 — SAM AMG as intensity clustering on CT

**Status:** Stage 4 survived Reviewer #2; Stage 5 in flight.  
**Hypothesis (falsifiable):** On windowed CT, SAM Automatic Mask Generation (AMG) mask sets agree with intensity clustering (k-means / multi-Otsu / GMM) more than with texture-based superpixels (SLIC), and AMG tracks **intensity remaps** while remaining **invariant to intensity-preserving texture shuffles**.

If the texture-shuffle arm moves AMG as much as intensity remap, **kill** the mechanistic claim.

## One-liner

SAM’s “objectness” on CT is mostly HU clustering after windowing — unless counterfactuals say otherwise.

## Killer experiment (Day 1)

See `experiments.md`. Synthetic + 50–200 public CT slices. No need for SA-1B. Pre-register three agreement metrics: Hungarian IoU, ARI, boundary-F.
