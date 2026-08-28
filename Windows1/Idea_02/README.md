# Idea_02 — LesionSuppress

**Candidate titles**

1. When Enhancement Erases the Finding: A Lesion-Suppression Safety Spec
2. Size–Contrast–Strength Curves for Silent Lesion Loss under Denoising and SR
3. Do Not Trust the Clean Image: Measuring Suppression of Small Findings

## 1. Executive summary

Deep denoisers and super-resolution (SR) can **remove or hallucinate** small clinical findings. We do **not** claim a universal law across all pipelines (that claim was killed in review). We claim a **safety specification**: for a named pipeline family, estimate

P(suppress | size, CNR, strength)

and test whether the **rank order** of bins matches **real** small-nodule sensitivity on LIDC-IDRI. If synthetic rank fails to transfer, the project dies.

## 2. Motivation

KNOWN: task-based image quality in medical physics; reader studies after vendor DLR/SR; DL restoration hallucination metrics. HYPOTHESIS: papers that “denoise then segment” under-report **true-lesion deletion** (suppression) vs fake-structure insertion (hallucination). Regulatory/safety audience cares about suppression of small, low-contrast lesions.

## 3. Problem definition

Let x be a volume/slice, ℓ a lesion with attributes (size, contrast-to-noise ratio CNR). Let T_s be an enhancement operator at strength s (noise reduction level, SR scale, GAN weight). A frozen detector D (nnU-Net / nnDetection trained on **unenhanced** data) produces a hit if a detection matches ℓ after T_s.

Suppression event: ℓ is detected on x but not on T_s(x), or detection score falls below a pre-registered operating point.

## 4. Core hypothesis

**H1 (transfer):** Kendall τ between synthetic-bin suppression rates and real LIDC small-nodule miss-rate deltas, across matched (size, CNR) bins, is > 0 with CI excluding 0.

**H2 (dose-response):** For each pipeline family separately, P(suppress) increases with s and decreases with size and CNR.

**H3 (universality) — optional, default OFF:** after rescaling s to a common axis, families collapse. We do **not** need H3 to ship.

Kill the project if H1 fails on the primary family (CNN denoiser). Pivot to “insertion artifacts” analysis if CHO and nnU-Net disagree wildly.

## 5. Key insight

Suppression is a **psychometric curve**, not an mIoU footnote. Rank-order transfer is the scientific gate; absolute P values are EXPECTED to be insertion-model dependent.

## 6. Novelty

Reader studies exist for specific products. sFRC-like metrics (UNSURE 2026 arXiv — re-verify) target hallucination. **Gap:** public, detector-based **suppression curves** with a **synthetic-to-real rank test** on LIDC, dropping universality.

Confidence: Medium.

## 7. Literature

See `literature.md`.

## 8–10. Method / diagram / math

Insert lesions with known size/CNR into Mayo-style LDCT or LIDC backgrounds (careful: LIDC already has nodules — use nodule-free slices or subtract). Apply T_s. Score with frozen D.

Logistic model per family:

\[
\mathrm{logit}\, P(\mathrm{suppress}) = \beta_0 + \beta_{\mathrm{size}}\log \mathrm{size} + \beta_{\mathrm{CNR}}\mathrm{CNR} + \beta_s s
\]

Compare per-family vs pooled fit with AIC (H3).

## 11. Implementation

`src/lesion_suppress/` insertion, metrics, curve fit. Prototype runs on synthetic 2D Gaussians without clinical data.

## 12. Data

LIDC-IDRI (real nodules, size). Mayo/AAPM LDCT if available. fastMRI for a second modality **after** CT H1 passes. Do not require new readers for killer.

## 13. Baselines

Unprocessed; BM3D family; DnCNN-class; one SR (e.g. residual CNN). Not claiming SOTA denoisers.

## 14. Metrics

Lesion-level sensitivity; suppression rate; Kendall τ vs real; CHO optional.

## 15–17.

See `experiments.md`. Killer = H1 τ.

## 18. Expected (not measured)

EXPECTED: small low-CNR lesions suppressed first; generative SR worse than BM3D at matched visual smoothness; τ moderate (~0.4–0.8) if insertion is reasonable.

## 19–20. Failures / negatives

If τ~0: insertion model is the paper’s confounder — stop claiming safety spec. If CHO≠detector: measurement invalid.

## 21–22. R2

“Synthetic lesions aren’t real.” → H1 is the answer or the death.
“No method.” → agree: this is a **spec/characterization** paper; Impact is the defense, not architectural novelty. Stage 6 accepted that.

## 23. Compute

Killer ~2 GPU-days (inference). Full ~10.

## 24–28.

See `roadmap.md`. Story: a measured P(suppress|·) you can put in a deployment card.
