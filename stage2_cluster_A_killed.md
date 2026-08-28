# Stage 2 — Cluster A Kill Summary

**288 of 372 ideas killed.** This file summarizes *why*, by primary kill reason. Per-idea reasons are in `stage2_cluster_A_scores.csv`. Counts are primary-reason assignments; many ideas fail on multiple axes. "Likely already published" is reviewer judgment, not a literature-search result.

## Kill-reason breakdown

### 1. Likely already published / crowded area with no compelling remaining question (~70 ideas)
The largest bucket. Stage 1 generated many hypotheses whose core phenomenon or method sits in well-mined literature: prompt-template sensitivity (A-0033), learned click policies (A-0015), pseudo-rehearsal (A-0110), task-vector arithmetic (A-0115), conformal segmentation (A-0124), density-based failure prediction (A-0129), crop-and-zoom for small objects (A-0138), positional-embedding interpolation (A-0168), model stitching (A-0171), TTA entropy collapse (A-0253), randomized-smoothing certificates for masks (A-0255), context co-occurrence bias (A-0277), CoTTA-style drift handling (A-0287, A-0288, A-0290), scanner/site effects (A-0050), uncertainty-vs-reader-disagreement (A-0057), PEFT-vs-nnU-Net crossovers (A-0052). Also A-0026, where SAM2 already pins the prompted frame in memory, making the proposal largely moot.

### 2. Confounded design / definition-driven or unfalsifiable claims (~45 ideas)
The proposed minimal experiment cannot isolate the claimed cause, or the headline result is determined by a contestable definition: reversed-video physics (A-0021), "correct behavior at splits" undefined (A-0028), decodability≠use in causal patching (A-0037), morph continua off-distribution (A-0042), intensity-vs-shape synthetics (A-0046), era/content/resolution entanglement (A-0278), curation-vs-world homogenization unidentifiable (A-0279), inpainting artifacts driving "nonlocality" (A-0343), "exhausted prompt optimization" undefined (A-0362), 2-iteration decoders too shallow for "optimization dynamics" (A-0306).

### 3. Data, annotation, or human-study cost disproportionate to upside (~45 ideas)
Requires production logs, expert traces, multi-annotator campaigns, eyetracking, staged photography, or field capture that a small lab cannot fund relative to the expected result: A-0001, A-0020, A-0075, A-0125, A-0161, A-0163, A-0217, A-0218, A-0223, A-0224, A-0234, A-0235, A-0264, A-0266, A-0268, A-0324, A-0339, A-0340, A-0351, A-0354, A-0359, A-0360, A-0363, A-0365.

### 4. Module stacking / "apply X to Y" engineering without a scientific question (~40 ideas)
Auxiliary heads, gates, retrofits, dashboards, and MLOps tooling: error-prediction heads (A-0072), distillation-loss variants (A-0083), gradient taps (A-0097), calibration losses (A-0126), gated TTA (A-0147), locality-constrained decoding (A-0215), task-conditioned selection heads (A-0233), prompt-path retrofits (A-0248), SfM-consistency training (A-0322), constrained-decoding retrofits (A-0332, A-0341), output contracts (A-0349), canary diffing (A-0350), behavior pinning (A-0355), API monitoring (A-0371), dashboards (A-0372). Several HCI-shaped studies (A-0127, A-0219, A-0358) also land here for venue mismatch.

### 5. Infeasible compute for a small lab (14 ideas)
Any design requiring pretraining, matched twin training, or training grids: A-0076, A-0081, A-0088, A-0105, A-0173, A-0180, A-0199, A-0203, A-0204, A-0209, A-0210, A-0285, A-0311, A-0368.

### 6. Redundant with a stronger kept/protected idea (~22 ideas)
Killed to avoid double-funding one insight: A-0012→A-0002/A-0003; A-0041, A-0192→A-0134; A-0044→A-0330; A-0063→A-0317; A-0065→A-0271; A-0101, A-0108, A-0116→A-0107 program; A-0109→A-0092; A-0153, A-0156, A-0158→A-0151/A-0152/A-0237; A-0163→A-0194; A-0186→A-0181; A-0197→A-0196; A-0229→A-0334; A-0267→A-0034; A-0304→A-0178; A-0327→A-0314; A-0333→A-0031/A-0262.

### 7. Low upside / likely-null audits / vague novelty (~25 ideas)
Sound but boring or thin: likely-null implementation audits (A-0308, A-0310, A-0312), boring-null interference test (A-0019), definitional decompositions with no consequence (A-0029, A-0067), niche metrology (A-0143), vague "law" claims (A-0008), aging relevance (A-0144).

### 8. Sound but outcompeted at the budget line (~27 ideas)
Explicitly flagged **near-keep / near-protect** in the CSV — the first ideas to revive if the survivor pool needs widening: A-0028, A-0037, A-0042, A-0046, A-0071, A-0096, A-0108, A-0114, A-0116, A-0123, A-0125, A-0131, A-0148, A-0153, A-0156, A-0166, A-0177, A-0185, A-0189, A-0205, A-0213, A-0234, A-0236, A-0245, A-0251, A-0263, A-0266, A-0270, A-0281, A-0295, A-0303, A-0325, A-0335, A-0337, A-0342, A-0343, A-0362, A-0365, A-0370.

## Notes for Stage 3
- The kill of A-0026 assumes SAM2's default memory retains conditioning frames; if a Stage 3 literature check contradicts this, revisit.
- Bucket 1 kills are judgment calls: any idea there whose literature check comes back empty is automatically interesting again (the judged-published prior was the only disqualifier for several, e.g., A-0124, A-0138, A-0253).
- High-mean kills (A-0189 anchoring coefficient, A-0236 granularity dial, A-0116 prompt-space forgetting) died on redundancy/fragility, not quality — cheap add-ons if an adjacent kept project spins up.
