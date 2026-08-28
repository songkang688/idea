# AlphaSmoke — Dataset & Checkpoint Inventory

Status: INVENTORY. Access/license columns are marked **UNVERIFIED** until runbook step
R0 executes; nothing below asserts that a download succeeded. No dataset is
redistributed by this package.

## 1. Smoke — target domain

| Dataset | Role | GT type | Source citation (tag) | Access status |
|---|---|---|---|---|
| DS01–DS03 (Yuan et al. synthetic smoke) | Part A secondary endpoint; Part B synthetic-alpha τ arm | **alpha** (synthetic composites) | arXiv:1809.00774 / Neurocomputing 2019 `[S3]` | UNVERIFIED (author site / on request) |
| SMOKE5K | Part A primary (real split); Part B pool scoring; rater study | binary (+ transmission-guided provenance) | Yan et al., AAAI 2022 `[S3]` | UNVERIFIED (public per Stage-3 notes) |
| SSD (smoke segmentation dataset used in Stage-3 ceiling plan) | rater study; ceiling confrontation | binary | per `stage3_kill_medical_smoke.md` §8 `[S3]` | UNVERIFIED |
| AusSmoke / MultiNatSmoke | primary endpoint (if licensed); ceiling confrontation deltas (1–3 IoU pts) | binary | arXiv:2604.23542 `[V]` | UNVERIFIED |
| FIgLib (fixed-tower wildfire sequences) | measured-alpha capture source (pre-smoke background frames) | sequences, event-labelled | Dewangan et al., Remote Sensing 14(4):1007, 2022 `[S3]` | UNVERIFIED (public per Stage-3 notes) |
| **AlphaSmoke-Measured (new, ours)** | Part B pillar 2; Part A tertiary endpoint | **measured alpha** via background inversion + validity/sensitivity masks | this package, `configs/alpha_capture.yaml` | to be captured (lab + FIgLib-derived) |

## 2. Matting — pretraining side (arms M / MB)

| Dataset | Role | Notes | Access status |
|---|---|---|---|
| P3M-10k | matting pretrain corpus | portrait matting; privacy-preserving faces; license terms must be checked for pretraining use | UNVERIFIED `[M — verify dataset card]` |
| AIM-500 | matting pretrain corpus | natural-object mattes | UNVERIFIED `[M]` |
| Composition-1k / Adobe DIM | matting pretrain corpus (optional) | **license-restricted (request-based)**; if unavailable, drop and report corpus composition honestly | UNVERIFIED `[M]` |
| Distinctions-646 | matting pretrain corpus (optional) | same caveat | UNVERIFIED `[M]` |

Arm MB uses the **identical** image set with alpha thresholded at 0.5 (B1). The corpus
actually used is frozen and listed in the paper; if any corpus fails licensing, both M
and MB shrink together, keeping the M/MB contrast exact.

## 3. Segmentation — pretraining side (arms S / S+cal)

| Source | Role | Notes | Access status |
|---|---|---|---|
| COCO (instance/semantic) | arm S controlled pretrain + matched-count subsample (B8) | standard terms | UNVERIFIED |
| Public seg checkpoint at matched backbone (e.g., SAM ViT-B image encoder `[M]`, ViTDet-COCO `[M]`) | arm S public-checkpoint cell; probe encoder (b) | scale confound acknowledged; controlled cells carry the claim | UNVERIFIED |
| Generic (non-smoke) synthetic composites for S+cal head calibration | B7 control | built from seg-corpus images + random soft masks; recipe in `configs/pretrain_arms.yaml` | generated, not downloaded |

## 4. Part-B checkpoint pool (target 8–12; final list frozen at R3)

| Candidate | Why | Tag |
|---|---|---|
| Yan et al. AAAI 2022 model (SMOKE5K line) | field baseline, protocol origin | `[S3]` |
| FoSp (AAAI 2024) | current SMOKE5K protocol holder (mMse+Fβ) | `[V]` — weights availability UNVERIFIED |
| SFMattingNet (Remote Sensing 2025) | **B9 mandatory** — the matting turn's representative | `[V]` — weights availability UNVERIFIED |
| Yuan et al. line (DS0x) | synthetic-alpha era representative | `[S3]` — reproducibility UNVERIFIED |
| MAM (Matting Anything) | matting foundation head on frozen SAM | `[S3]` |
| SAM (automatic / grid-point mode, thresholded) | generic-segmentation representative — **B10: no detector prompting** | `[M]` code public |
| CoSW (NeurIPS 2024) | label-noise-aware smoke model | `[S3]` — weights UNVERIFIED |
| Part-A arms (M, MB, S, S+cal, 0) + floors (DC, HSV) | internal pool members | ours |

Pool inclusion rule (pre-registered): any candidate whose released weights cannot be
obtained or reproduced by R3 is listed in the paper as "attempted, unavailable" — no
silent drops.

## 5. Published-delta ledger (for the ceiling confrontation, B5)

To be filled at R0 by tabulating, per benchmark, the reported metric deltas between
consecutive SOTA claims (starting set: AusSmoke/MultiNatSmoke table `[V]`, SMOKE5K
leaderboard entries from FoSp `[V]`). Stored as
`configs/eval_protocol.yaml → published_deltas` with one citation per row. **No delta
is invented; every row must carry a verifiable source or it stays out.**
