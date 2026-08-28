# Idea_01 literature

Status: KNOWN unless marked UNSURE. URLs are canonical where possible.

## Foundation

- Kirillov et al., *Segment Anything*, ICCV 2023. https://arxiv.org/abs/2304.02643
- Ravi et al., *SAM 2: Segment Anything in Images and Video*, 2024. https://arxiv.org/abs/2408.00714
- Ke et al., *Segment Anything in High Quality* (HQ-SAM), NeurIPS 2023. https://arxiv.org/abs/2306.01567
- Ma et al., *Segment Anything in Medical Images* (MedSAM), Nature Communications 2024. https://arxiv.org/abs/2304.12306

## Adaptation / interpolation / PEFT

- Wortsman et al., *Robust fine-tuning of zero-shot models* (WiSE-FT), CVPR 2022. https://arxiv.org/abs/2109.01903
- Wortsman et al., *Model soups*, ICML 2022. https://arxiv.org/abs/2203.05482
- Hu et al., *LoRA*, ICLR 2022. https://arxiv.org/abs/2106.09685
- Kirkpatrick et al., *EWC*, PNAS 2017. https://arxiv.org/abs/1612.00796
- Kim et al., *R-Adapter* (WiSE-style ensemble inside PEFT; CLIP, not SAM), ECCV 2024. https://arxiv.org/abs/2408.05749
- Mai et al., *Lessons and Insights from a Unifying Study of PEFT in Visual Recognition* (WiSE-for-PEFT), CVPR 2025. https://arxiv.org/abs/2409.16434
- Chen et al., *RobustSAM*, CVPR 2024. https://arxiv.org/abs/2406.09627 — consistency vs frozen SAM on degraded images; **architectural**, not a COCO-interactive constraint
- Zhong et al., *Conv-LoRA*, ICLR 2024. https://arxiv.org/abs/2401.17868 — PEFT forgetting mitigation by freezing, not a performance constraint

## Interactive evaluation (also used as attacks on naive click-sim)

- Benenson et al. interactive annotation scale, 2019 (UNSURE exact title in this file — confirm before camera-ready)
- RClicks, 2024. https://arxiv.org/abs/2410.11722 — real vs simulated clicks
- TETRIS, AAAI 2024. https://arxiv.org/abs/2402.06132 — adversarial valid clicks

## Datasets

- SA-1B (Kirillov et al. 2023)
- COCO 2017
- LVIS
- ADE20K
- Kvasir-SEG
- ISIC 2018
- COD10K (camouflaged objects)

## Relation

HQ-SAM/MedSAM/RobustSAM/Conv-LoRA = **neighbors** (freeze or extra modules, not a J_gen constraint). WiSE-FT / R-Adapter = **kill-switch / PEFT-interpolation** baselines. RClicks/TETRIS = **eval protocol constraints**.

Lit-verify (2026-08-28): **NOT FOUND** an explicit paper that fine-tunes SAM subject to a constraint that COCO interactive performance not degrade. The combination remains OPEN as of that search (EVIDENCE = search miss, not proof of unpublished status).
