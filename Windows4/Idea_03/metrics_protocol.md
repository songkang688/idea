# AlphaSmoke — Metrics & Measurement Protocol

Status: PROTOCOL SPECIFICATION. Definitions below are what `src/alphasmoke` implements;
every formula is standard and attributed. Before any paper-bound number is produced,
implementations must be cross-checked against released evaluation code of the cited
protocols (runbook step R1) — noted per metric as **verify-against**.

Notation: prediction `p ∈ [0,1]^{H×W}` (soft map), alpha GT `a ∈ [0,1]^{H×W}`, binary
GT `g ∈ {0,1}^{H×W}`, binarized prediction `p̂ = 1[p ≥ τ_op]` under the frozen
operating rule (experiments.md §1.1).

---

## 1. Alpha-error family (Rhemann et al., CVPR 2009 suite `[S3]`)

Implemented in `src/alphasmoke/metrics/alpha_metrics.py`.

| Metric | Definition | Notes |
|---|---|---|
| MAE | mean(&#124;p − a&#124;) over evaluation region | headline alpha metric for Part A tertiary endpoint |
| SAD | Σ&#124;p − a&#124; (reported ÷1000 by matting convention) | scale-dependent; report with resolution |
| MSE | mean((p − a)²) | per-image; dataset aggregate = mean over images |
| Gradient (Grad) | Σ(‖∇σ p‖ − ‖∇σ a‖)² with ∇σ = first-order Gaussian derivative, σ=1.4 | verify-against: matting-benchmark ports differ in σ and normalization |
| Connectivity (Conn) | Rhemann connectivity with threshold ladder step 0.1, θ=0.15 | uses largest connected component of thresholded p∧a per level; verify-against: community Python ports |

Evaluation region: full frame for smoke (no trimap exists); where a benchmark defines
an unknown-region trimap, both full-frame and trimap-region variants are reported.

## 2. Binary-overlap family

Implemented in `src/alphasmoke/metrics/binary_metrics.py`.

### 2.1 IoU / Dice

Standard set overlap of `p̂` vs `g`; per-image, then dataset mean (mIoU). Empty-∪-empty
convention: score 1.0 when both prediction and GT are empty (convention printed in the
paper; smoke test sets contain no-smoke frames).

### 2.2 Fβ (B4 column)

Fβ = (1+β²)·P·R / (β²·P + R) with **β² = 0.3** (saliency/smoke convention used by the
SMOKE5K line — FoSp AAAI 2024 `[V]`). **verify-against:** FoSp released eval code —
whether P/R are computed from a per-image adaptive threshold (2×mean saliency
convention) or a fixed threshold, and whether the dataset aggregate is mean-of-Fβ or
Fβ-of-means. The choice found in the released code is frozen as `τ_op` for all arms.

### 2.3 mMse (B4 column)

Per-image MSE between the *soft* prediction and the **binary** GT, averaged over the
dataset — the SMOKE5K protocol's mMse (Yan et al. AAAI 2022 `[S3]`; FoSp `[V]`).
**verify-against:** released SMOKE5K/FoSp eval code (scaling ×100 vs raw; soft-vs-
binarized prediction input). This column is load-bearing: pre-registered kill K-B1
compares rankings under mMse-on-binary-GT with alpha-MAE-on-alpha-GT.

### 2.4 Boundary-F (primary-endpoint component)

BF-style boundary F1: boundary pixels of `p̂` and `g` matched within distance tolerance
θ_d = 2 px via distance transforms; precision/recall over matched boundary pixels;
report also at θ_d ∈ {1, 5} px in the appendix. verify-against: BSDS/DAVIS-style
implementations differ in boundary extraction (4- vs 8-neighborhood).

## 3. Rank agreement (Part B pillar 1)

Implemented in `src/alphasmoke/metrics/rank_agreement.py`.

1. For each metric m and checkpoint c: per-image scores → dataset score S_m(c).
2. **Sign alignment:** each metric declares a direction (higher-better: IoU, Dice, Fβ,
   boundary-F; lower-better: MAE, SAD, MSE, mMse, Grad, Conn). Lower-better scores are
   negated before ranking so τ = +1 always means "same ordering of model quality."
3. Kendall τ (τ-b, tie-aware) for every metric pair → symmetric τ matrix.
4. **Reversal enumeration:** for every metric pair, the set of checkpoints in the
   top-3 under one metric but not the other, with rank displacements — the qualitative
   payload Stage 3 asked for ("reversal cases among top-3 ranks").
5. **Uncertainty:** bootstrap over images (resample image set with replacement,
   recompute S_m(c), recompute τ; 10⁴ resamples; percentile CIs).

## 4. Measured-alpha recovery (Part B pillar 2, B3)

Implemented in `src/alphasmoke/alpha_recovery/background_inversion.py`.

### 4.1 Model

Single-scattering compositing on a static, exposure-locked camera:

    I(x) = α(x)·F + (1 − α(x))·B(x)

- `B(x)`: per-pixel clean background, estimated as the temporal median of ≥ K pre-smoke
  frames (default K=10; median suppresses transient motion).
- `F`: smoke color, assumed locally uniform per frame; estimated from the densest
  smoke region (pixels with largest ‖I−B‖, top quantile q=0.02) or supplied from a
  calibrated lab target.
- Per-pixel least squares across channels:

    α(x) = ⟨I(x)−B(x), F−B(x)⟩ / ‖F−B(x)‖² , clipped to [0,1].

### 4.2 Validity mask (all exclusions binding, from the Set-C verdict)

A pixel enters evaluation only if **all** hold:

1. not saturated in I or B (any channel outside [ε, 1−ε], default ε = 2/255);
2. conditioning: ‖F − B(x)‖ ≥ δ (default δ = 0.08 in [0,1] units) — where smoke color
   ≈ background color, α is unidentifiable;
3. sensitivity: std of α(x) under F perturbed by ±Δ (default Δ = 0.05 per channel,
   8 perturbations) ≤ s_max (default 0.10). Sensitivity maps are released with the
   dataset.

Frame-level QC: exposure lock verified from EXIF/camera log; frames with global
illumination change vs background (median |I−B| on smoke-free border region > 0.02)
are dropped; backlit/plume-shadow scenes excluded by protocol
(`configs/alpha_capture.yaml`).

### 4.3 What this does and does not claim

- **KNOWN FACT:** the compositing identity is exact for a single non-emissive
  scattering layer with locally uniform effective color; it is the same model that
  generated DS0x synthetic GT — but here α is *measured from real smoke optics*, not
  authored, which is precisely what breaks the circularity attack.
- **MODEL SPECULATION (bounded):** real smoke violates local-uniform-F under strong
  multiple scattering / self-shadowing; the sensitivity mask converts this from a
  silent bias into an explicit exclusion + released uncertainty map.

## 5. Rater ceiling (Part B pillar 3, B5)

Implemented in `src/alphasmoke/rater/ceiling.py`.

- Sampling: 150 images per dataset (SMOKE5K-real, SSD), stratified by smoke-density
  tercile (density proxy: mean HSV smoke score of the GT region, so stratification
  does not use any model under test).
- Raters: 3–5, instructed with the dataset's own original annotation guideline (no
  new definition of "smoke boundary" — the ceiling must reflect the benchmark as
  used).
- Statistics: pairwise IoU over all rater pairs per image (binary task); pairwise MAE
  on the soft-annotation subset; report distribution (median, IQR) per stratum and
  pooled — a mean alone hides the bimodality the hyperspectral study found
  (arXiv:2602.10858 `[S3]`).
- Confrontation table: per benchmark, ceiling (1 − median pairwise IoU) vs the
  published method deltas collected in `datasets.md` (e.g., AusSmoke's 1–3 IoU-point
  SOTA gaps `[V]`); a delta is flagged "sub-ceiling" if smaller than the ceiling gap.
- Pre-registered demotion K-B4 (ceiling > 0.85 → appendix).

## 6. Physics floors (B6)

Implemented in `src/alphasmoke/baselines/`.

- **Dark channel** (He, Sun & Tang CVPR 2009 `[S3]`): dark = min-filter over channels
  and patch (default 15 px); atmospheric light A from top 0.1% dark-channel pixels;
  transmission t = 1 − ω·dark(I/A), ω = 0.95; smoke alpha floor α_DC = 1 − t. Optional
  edge-aware smoothing; no training.
- **HSV low-chroma rule**: smoke score = w_s·(1−S) ⊙ band(V) ⊙ (1−spread(RGB)), where
  spread = (max−min channel); weights fixed a priori in
  `configs/eval_protocol.yaml` and **never tuned on any test set** (tuning allowed
  only on a held-out train split, logged). Classical color-rule smoke detection is a
  decades-old family; we implement the rule as a control, and any specific historical
  citation used in the draft is `[M]` until re-verified.

Both floors emit soft maps in [0,1] and are scored under the identical protocol as
every learned arm (same τ_op, same metrics), entering every Part-A results table and
the Part-B pool.

## 7. Linear probe protocol (Part A week-1 killer)

Implemented in `src/alphasmoke/probes/encoder_linear_probe.py`.

- Encoders: (a) matting-pretrained (MAM/ViTMatte-class public checkpoint — exact
  checkpoint recorded in `configs/linear_probe.yaml` at run time), (b) COCO-seg /
  SAM-class encoder at matched backbone size, (c) ImageNet-only control.
- Probe: single 1×1 conv from frozen patch features → logit map, bilinear upsample to
  input; no decoder, no adapter — the probe measures *linearly available* smoke
  evidence in the frozen representation.
- Training: N ∈ {25, 50, 100, 250} real-smoke images × 3 seeds; AdamW; early stop on
  held-out probe-val split; identical schedule for all encoders.
- Endpoint: real-smoke test mIoU (+ Fβ, mMse for continuity), CI over seeds ×
  image-bootstrap.
- Decision rule K-A1 (experiments.md §2).
