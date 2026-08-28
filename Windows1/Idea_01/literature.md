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

HQ-SAM/MedSAM = **neighbors**. WiSE-FT = **kill-switch baseline**. RClicks/TETRIS = **eval protocol constraints**, not competitors.
