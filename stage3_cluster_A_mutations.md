# Stage 3 — Cluster A Mutations (5)

Ideas with real partial overlap where a precise novel remainder could be carved out. Each mutation states what prior work forced the change, the mutated one-liner, and the new falsifiable hypothesis.

---

## M1. A-0017 — "Identity capture" → Causal memory surgery for SAM2

- **What forced the mutation:** SAMURAI (Yang et al., 2024, arXiv:2411.11922) and DAM4SAM (Videnovic et al., 2024, arXiv:2411.17576) already discovered distractor lock-in in SAM2's memory and built prevention methods. "Stale memories block recovery" is their stated premise.
- **What died:** The discovery claim.
- **What survives:** Nobody performs *post-hoc causal surgery* — deleting specific post-error memory entries at ground-truth reappearance and measuring recovery — which separates memory-borne failure from representational failure and upper-bounds what any prevention method can gain.
- **Mutated one-liner:** Causal memory surgery for SAM2: measure how much organic tracking failure is reversible by targeted deletion of post-error memory entries, giving an upper bound that prevention methods can be scored against.
- **New hypothesis:** On ≥200 organic SAM2 failures, oracle-timed deletion of post-error entries restores tracking in >60% of cases, and the per-sequence reversible fraction predicts (r>0.6) the gain achievable by distractor-aware memory methods — establishing memory-editing recovery as an upper-bound diagnostic.

## M2. A-0068 — Translucency limitation → Training-free latent-matte audit

- **What forced the mutation:** Matting Anything (Li et al., 2023, arXiv:2306.05399) and Matte Anything (Yao et al., 2023, arXiv:2306.04121) already extract mattes from SAM — but through *trained* readout modules, proving usable signal exists without measuring what is free.
- **What died:** "SAM features support matting" as a finding.
- **What survives:** Whether alpha information is present in the *raw output logits* (recoverable training-free) vs. created by trained heads — plus the uncharacterized placement policy of the forced hard boundary on translucent matter.
- **Mutated one-liner:** A training-free audit of binary-trained mask logits against ground-truth alpha mattes: how much matting information do promptable models give away for free, and where does the forced hard boundary land on translucent matter?
- **New hypothesis:** After partialling out distance-to-boundary, SAM logit values retain rank correlation ρ>0.3 with true alpha in translucent regions, and hard-boundary placement variance on translucent regions exceeds opaque regions by >5× — quantifying both the free signal and the representational cost of binary supervision.

## M3. A-0128 — Confidence collapse under iterative prompting → Trajectory calibration

- **What forced the mutation:** Static miscalibration of segmentation confidence is documented (On Calibrating Semantic Segmentation Models, NeurIPS 2023, arXiv:2212.12053), and conformal work (arXiv:2602.10045) states SAM's predicted IoUs carry no guarantee. "SAM is miscalibrated" is not a finding.
- **What died:** The static miscalibration claim.
- **What survives:** No one audits confidence *along interaction trajectories* — the quantity stopping rules actually consume — nor tests whether inflation is a stable, correctable model constant.
- **Mutated one-liner:** Trajectory calibration of promptable models: does self-reported mask confidence inflate with interaction count independent of accuracy, and is the inflation a correctable model constant that repairs interactive stopping rules?
- **New hypothesis:** Under RClicks-realistic simulated sessions on ≥2k objects, predicted-IoU inflation beyond true-IoU gain is positive after accuracy plateaus in >40% of objects; a single per-model click-indexed correction reduces wasted post-plateau clicks by >30% at equal final quality.

## M4. A-0134 — Emptiness calibration → The absence option for geometric prompts (absorbs A-0047)

- **What forced the mutation:** SAM 3 (2025) ships a trained presence head for concept-absence rejection — but only for *text/concept* prompts; and Huang et al. (Medical Image Analysis 2024, arXiv:2304.14660) already document confident wrong-box masks without benchmarking rejection. A-0047 (MedSAM wrong-box rejection) overlapped both this idea and Cluster B survivor B-0350.
- **What died:** Concept-level emptiness (SAM3 owns it); the standalone medical wrong-box idea (A-0047, merged here; medical scope ceded to B-0350).
- **What survives:** The entire deployed SAM-1/2 point/box base has no absence channel; the null-detection competence of its existing signals (predicted IoU, stability, logit statistics) is unmeasured and unrepaired for natural-image auto-annotation.
- **Mutated one-liner:** The absence option: benchmark null-detection AUROC of point/box-promptable segmenters across empty-prompt families and fix it with a trained null token — the rejection competence SAM3's concept-level presence head does not provide.
- **New hypothesis:** Existing SAM signals achieve <0.75 AUROC for emptiness detection across empty-prompt families (background clicks, texture boxes, wrong boxes); a null-token fine-tune reaches >0.9 AUROC while preserving mask quality, measurably raising auto-annotation precision at fixed recall.

## M5. A-0314 — Activation steering for mask control → Linear property axes in mask decoders

- **What forced the mutation:** Activation steering is mature for LLMs (Inference-Time Intervention, NeurIPS 2023, arXiv:2306.03341) and LVLMs (Activation Steering Decoding, ACL 2025; Steer2Edit, arXiv:2602.09870). "Port steering to vision" is attackable as pure technique transfer.
- **What died:** The tool-transfer framing.
- **What survives:** All existing steering targets token generation; whether prompt-conditioned *dense* decoders possess linear, compositional axes for geometric mask properties is an unclaimed mechanistic question — with the control interface as a corollary, not the headline.
- **Mutated one-liner:** Do mask decoders have linear property axes? Contrastive activation differences as steering vectors for interpretable mask properties, evaluated by cross-image generalization, dose-response linearity, and composition.
- **New hypothesis:** For ≥3 of 4 tested properties (dilate/erode, attachment inclusion, boundary tightness, granularity), a single direction from 100 contrastive pairs transfers to held-out images with monotone dose-response (Spearman ρ>0.7) and <15% off-target drift — establishing approximately linear, compositional property axes in the decoder.

---

## Near-misses that mutation saved (summary)

1. **A-0017** — killed as discovery, saved as causal upper-bound diagnostic.
2. **A-0068** — killed as "matting from SAM", saved as training-free latent-information audit.
3. **A-0128** — killed as "SAM is miscalibrated", saved as trajectory-indexed calibration + stopping-rule repair.
4. **A-0134** — killed at concept level by SAM3's presence head, saved by scoping to the geometric-prompt rejection gap (absorbing A-0047).
5. **A-0314** — killed as steering-technique port, saved as decoder property-geometry measurement.
