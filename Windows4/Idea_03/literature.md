# Literature — AlphaSmoke (narrative notes)

Full register with verification tags (`[V]`/`[S3]`/`[M]`): **`CITATIONS.md`**.
Why each line matters to the design: `proposal.md` §3. This file is the short
narrative map.

## The three literatures this paper sits between

1. **Smoke segmentation with binary protocols.** Yan et al. AAAI 2022 (SMOKE5K)
   `[S3]` set the protocol; FoSp AAAI 2024 `[V]` holds it and already reports
   **mMse + Fβ** — which is why those two metrics are first-class columns in our τ
   matrix (B4), not strawmanned. AusSmoke/MultiNatSmoke `[V]` shows current SOTA
   deltas are 1–3 IoU points — the number the rater ceiling confronts (B5).
2. **Smoke as density/alpha.** Yuan et al. 2019/2020 `[S3]` built synthetic alpha GT
   (DS01–03) and density regression; SFMattingNet 2025 `[V]` is the field's matting
   turn, taken **without** the validity evidence this paper supplies. Matting
   Anything `[S3]` makes alpha heads trivial — which is why Stage 3 killed the
   architecture idea (A1-046) and only the *pretraining-provenance* question (S-103)
   survived.
3. **Label noise / rater disagreement.** Hyperspectral 3-rater smoke statistics
   (arXiv:2602.10858 `[S3]`) and CoSW NeurIPS 2024 `[S3]` establish the phenomenon;
   the NOT-FOUND gap is the ceiling *on the standard RGB benchmarks confronted with
   their own leaderboard deltas* (Stage-3 NOT-FOUND #6).

## Explicit differencing (what we do NOT claim)

- **ProFSAM** (arXiv:2510.21782 `[S3]`): detector-prompted fire SAM2 — out of scope
  by binding obligation B10; no detector prompts anywhere in this project.
- **Matting Anything / Matte Anything** `[S3]`: no new alpha head is claimed; MAM is
  a pool member and an engineering substrate.
- **Density-aware SAM-background smoke segmentation** (Pattern Recognition, per
  `selection_history/literature_anchors.md`): SAM-as-prior is taken; we do not build
  a smoke segmenter around SAM.
- **Dark channel** (He et al. CVPR 2009 `[S3]`): imported as the training-free floor
  (B6), not as a contribution.

## Where the novelty lives (Stage-3 NOT-FOUND register)

- #5: Dice-vs-alpha model-ranking reversal study on smoke → Part B pillar 1.
- #6: RGB-benchmark rater ceiling vs published deltas → Part B pillar 3.
- #7: matting-pretrain vs segmentation-pretrain controlled transfer on smoke →
  Part A.
