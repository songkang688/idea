# References — C-0306

Machine-readable list. Verification tags as in `../literature.md`:
PIPELINE-VERIFIED (checked inside this pipeline, Stage-2 D / Stage-4 K / Stage-7 P),
TEXTBOOK (stable common knowledge), UNVERIFIED (believed real; confirm identifier before any
submission — deliberately no URL given). **No citation here is invented; nothing UNVERIFIED may be
cited in a paper draft until resolved.**

## Core prior work (novelty-defining)

| # | Reference | Year | Venue | Link | Tag |
|---|---|---|---|---|---|
| 1 | Conformal Object Detection by Sequential Risk Control (SeqCRC) | 2025 | arXiv | https://arxiv.org/abs/2505.24038 | PIPELINE-VERIFIED (D; K re-verified v2) |
| 2 | Do We Still Need NMS? IoU-Aware Calibration (short title per K's record) | 2024 | WACV | https://doi.org/10.1109/wacv57701.2024.00478 | PIPELINE-VERIFIED (K; mandated baseline) |
| 3 | Probabilistic Object Detection with Conformal Prediction | 2026 | arXiv | https://arxiv.org/abs/2605.07549 | PIPELINE-VERIFIED (D); K flags re-verify at freeze |
| 4 | A Systematic Evaluation of Uncertainty Calibration in Pretrained Object Detectors | 2024 | IJCV | https://link.springer.com/article/10.1007/s11263-024-02219-z | PIPELINE-VERIFIED (K) |
| 5 | Kosub — A note on the triangle inequality for the Jaccard distance | 2019 | Pattern Recognition Letters | https://arxiv.org/abs/1612.02696 | PIPELINE-VERIFIED (P, used in prototype) |

## Conformal prediction foundations

| # | Reference | Year | Venue | Link | Tag |
|---|---|---|---|---|---|
| 6 | Vovk, Gammerman, Shafer — Algorithmic Learning in a Random World | 2005 | Springer | — (book) | TEXTBOOK |
| 7 | Papadopoulos et al. — Inductive Confidence Machines for Regression | 2002 | ECML | — | TEXTBOOK |
| 8 | Lei et al. — Distribution-Free Predictive Inference for Regression | 2018 | JASA | https://arxiv.org/abs/1604.04173 | TEXTBOOK |
| 9 | Angelopoulos, Bates — A Gentle Introduction to Conformal Prediction | 2021 | arXiv | https://arxiv.org/abs/2107.07511 | TEXTBOOK |
| 10 | Angelopoulos et al. — Conformal Risk Control | 2024 | ICLR | https://arxiv.org/abs/2208.02814 | TEXTBOOK |
| 11 | Angelopoulos et al. — Learn then Test | 2021 | arXiv | https://arxiv.org/abs/2110.01052 | TEXTBOOK |

## Detection / NMS / datasets

| # | Reference | Year | Venue | Link | Tag |
|---|---|---|---|---|---|
| 12 | Bodla et al. — Soft-NMS | 2017 | ICCV | https://arxiv.org/abs/1704.04503 | TEXTBOOK |
| 13 | Hosang et al. — Learning Non-Maximum Suppression | 2017 | CVPR | https://arxiv.org/abs/1705.02950 | TEXTBOOK |
| 14 | Carion et al. — DETR: End-to-End Object Detection with Transformers | 2020 | ECCV | https://arxiv.org/abs/2005.12872 | TEXTBOOK |
| 15 | Zhu et al. — Deformable DETR | 2021 | ICLR | https://arxiv.org/abs/2010.04159 | TEXTBOOK |
| 16 | Ren et al. — Faster R-CNN | 2015 | NeurIPS | https://arxiv.org/abs/1506.01497 | TEXTBOOK |
| 17 | Tian et al. — FCOS: Fully Convolutional One-Stage Object Detection | 2019 | ICCV | https://arxiv.org/abs/1904.01355 | TEXTBOOK |
| 18 | Lin et al. — Microsoft COCO | 2014 | ECCV | https://arxiv.org/abs/1405.0312 | TEXTBOOK |
| 19 | Gupta et al. — LVIS | 2019 | CVPR | https://arxiv.org/abs/1908.03195 | TEXTBOOK |
| 20 | Shao et al. — CrowdHuman | 2018 | arXiv | https://arxiv.org/abs/1805.00123 | TEXTBOOK |

## UNVERIFIED — resolve at proposal freeze (cite nowhere until then)

| # | Believed reference | Believed year/venue | Why it matters | Tag |
|---|---|---|---|---|
| U1 | de Grancey et al. — conformal box-margin guarantees for detection (safety context) | ~2022, SAFECOMP workshop | earlier conformal-OD line, post-NMS — strengthens the survey | UNVERIFIED |
| U2 | Andéol et al. — conformal prediction / risk control for railway-signaling detection | ~2023, COPA (PMLR) | same line, applied | UNVERIFIED |
| U3 | Adaptive-NMS (pedestrian crowding) | ~2019, CVPR | crowded-NMS AP line (K concedes qualitative "old news") | UNVERIFIED |
| U4 | CrowdDet — one proposal, multiple predictions | ~2020, CVPR | crowded-NMS AP line | UNVERIFIED |

## Pipeline-internal evidence (not citable externally)

- `Windows2/_wip/stage2_agent_D/prior_work_attack.md` §E1 — D's novelty verification (SURVIVE).
- `Windows2/_wip/stage4_agent_K/reviewer2_attacks.md` §27 — K's freshness re-search + verdict
  (SURVIVE-IF-EXPERIMENT) + mandated WACV-2024 baseline.
- `Windows2/_wip/stage5_agent_N/exp_05.md` — killer-experiment protocol.
- `Windows2/_wip/stage6_agent_Q/top5.md` #1 — seat, stop/kill criteria.
- `Windows2/_wip/stage7_proto_C0306/` — synthetic prototype (copied into `../src/`).
