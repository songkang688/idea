# AlphaSmoke — Citation Register

Tag convention (inherited from Stage 3/4):
- `[V]` — fetched and read during the Stage-3/4 passes (2026-08-28) per
  `stage4_r2_setC.md`; identifiers as recorded there.
- `[S3]` — carried from a Stage-3 file (`stage3_kill_medical_smoke.md`) that claimed
  web verification during its pass.
- `[M]` — memory-cited classic or dataset card; **re-verify identifier before quoting
  in any draft**.

No citation below was invented for this package; each one appears in the Windows4
selection-history files or is a dataset/code artifact flagged `[M]` for verification.

## Smoke segmentation / density

| Ref | Identifier | Used for | Tag |
|---|---|---|---|
| Yuan et al., Deep Smoke Segmentation | Neurocomputing 2019 / arXiv:1809.00774 | DS01–03 alpha GT; synthetic-alpha era | `[S3]` |
| Yuan et al., Wave-Shaped DNN for Smoke Density Estimation | IEEE TIP 2020 | density-regression precedent (kills ontology claim) | `[S3]` |
| Yan et al., Transmission-Guided Bayesian Generative Smoke Segmentation | AAAI 2022 | SMOKE5K; transmission-as-guide; mMse protocol origin | `[S3]` |
| FoSp | AAAI 2024, doi:10.1609/aaai.v38i7.28484 | mMse+Fβ protocol on SMOKE5K (B4) | `[V]` |
| AusSmoke / MultiNatSmoke | arXiv:2604.23542 | binary benchmark; 1–3 IoU SOTA deltas for ceiling confrontation | `[V]` |
| SFMattingNet | Remote Sensing 17(13):2259, 2025, doi:10.3390/rs17132259 | the matting turn; mandatory pool member (B9) | `[V]` |
| CoSW | NeurIPS 2024 | smoke label noise as established problem | `[S3]` |
| Hyperspectral smoke dataset (3 raters) | arXiv:2602.10858 | inter-annotator disagreement evidence | `[S3]` |
| Concentration-weighted forest smoke | Electronics 2021, doi:10.3390/electronics10212675 | translucency-ambiguity motivation | `[S3]` |
| Dewangan et al., FIgLib & SmokeyNet | Remote Sensing 14(4):1007, 2022, doi:10.3390/rs14041007 | fixed-tower sequences for measured-alpha capture | `[S3]` |
| ProFSAM (Ugwu & Zhang) | arXiv:2510.21782 | out-of-scope guard B10 (what we are NOT doing) | `[S3]` |
| Density-aware progressive smoke seg w/ SAM background priors | Pattern Recognition (per `literature_anchors.md`) | SAM-as-prior is taken; scope guard | `[S3]` |

## Matting

| Ref | Identifier | Used for | Tag |
|---|---|---|---|
| Li et al., Matting Anything (MAM) | CVPRW 2024 / arXiv:2306.05399 | light alpha head; pool member; A1-046 kill precedent | `[S3]` |
| Yao et al., Matte Anything | arXiv:2306.04121 | adjacent territory | `[S3]` |
| Rhemann et al., Perceptually Motivated Matting Benchmark | CVPR 2009 | SAD/MSE/Grad/Conn metric suite | `[S3]` |
| Medical Matting | arXiv:2106.09887 | rater-masks→alpha precedent (QUBIQ) | `[S3]` |
| P3M-10k / AIM-500 / Composition-1k / Distinctions-646 | dataset cards | pretrain corpora (arms M/MB) | `[M]` |

## Physics / classical baselines

| Ref | Identifier | Used for | Tag |
|---|---|---|---|
| He, Sun & Tang, Dark Channel Prior | CVPR 2009 / TPAMI 2011 | training-free transmission floor (B6) | `[S3]` |
| Classical color-rule smoke detection family | — | HSV low-chroma control is implemented as a rule, not cited to a specific paper until verified | `[M]` |

## Segmentation side

| Ref | Identifier | Used for | Tag |
|---|---|---|---|
| Kirillov et al., Segment Anything | ICCV 2023 | SAM auto-mode pool member; seg-pretrain encoder option | `[M]` (classic; verify exact ref format) |
| COCO | dataset card | arm S pretrain corpus | `[M]` |
| ViTDet-COCO / SAM ViT-B encoder checkpoints | code releases | probe encoder (b); arm S public cell | `[M]` |

## Windows4 process documents (internal)

- `Windows4/selection_history/stage3_kill_medical_smoke.md` — §7 (S-096/S-097/A1-046),
  §8 (S-102/A1-054), §9 (S-103), §10 (S-126), NOT-FOUND register #5–7.
- `Windows4/selection_history/stage4_r2_setA.md` — P103 review (binding conditions B1,
  B2, B7, B8).
- `Windows4/selection_history/stage4_r2_setC.md` — P096 review (binding conditions B3,
  B4, B5; NEW EVIDENCE register items 2–4).
- `Windows4/selection_history/stage4_top20.md` — Final-3 lock (Idea_03 = AlphaSmoke).
- `Windows4/selection_history/stage6_battle.md` — third-slot decision, decisive
  experiment #3 (linear probe), ordering discipline.
