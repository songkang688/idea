# Idea_01 文献

状态：除标明 UNSURE 外均为 KNOWN。URL 尽可能采用规范地址。

## 基础工作

- Kirillov et al., *Segment Anything*, ICCV 2023. https://arxiv.org/abs/2304.02643
- Ravi et al., *SAM 2: Segment Anything in Images and Video*, 2024. https://arxiv.org/abs/2408.00714
- Ke et al., *Segment Anything in High Quality* (HQ-SAM), NeurIPS 2023. https://arxiv.org/abs/2306.01567
- Ma et al., *Segment Anything in Medical Images* (MedSAM), Nature Communications 2024. https://arxiv.org/abs/2304.12306

## 适配 / 插值 / PEFT

- Wortsman et al., *Robust fine-tuning of zero-shot models* (WiSE-FT), CVPR 2022. https://arxiv.org/abs/2109.01903
- Wortsman et al., *Model soups*, ICML 2022. https://arxiv.org/abs/2203.05482
- Hu et al., *LoRA*, ICLR 2022. https://arxiv.org/abs/2106.09685
- Kirkpatrick et al., *EWC*, PNAS 2017. https://arxiv.org/abs/1612.00796
- Kim et al., *R-Adapter*（PEFT 内部的 WiSE 风格集成；针对 CLIP，非 SAM）, ECCV 2024. https://arxiv.org/abs/2408.05749
- Mai et al., *Lessons and Insights from a Unifying Study of PEFT in Visual Recognition* (WiSE-for-PEFT), CVPR 2025. https://arxiv.org/abs/2409.16434
- Chen et al., *RobustSAM*, CVPR 2024. https://arxiv.org/abs/2406.09627 —— 在退化图像上对比冻结 SAM 的一致性；属于**架构层面**，非 COCO 交互约束
- Zhong et al., *Conv-LoRA*, ICLR 2024. https://arxiv.org/abs/2401.17868 —— 通过冻结缓解 PEFT 遗忘，非性能约束

## 交互式评测（亦用作对朴素点击模拟的攻击）

- Benenson et al. interactive annotation scale, 2019（UNSURE 本文件中的确切标题 —— 在终稿前确认）
- RClicks, 2024. https://arxiv.org/abs/2410.11722 —— 真实 vs 模拟点击
- TETRIS, AAAI 2024. https://arxiv.org/abs/2402.06132 —— 对抗性有效点击

## 数据集

- SA-1B (Kirillov et al. 2023)
- COCO 2017
- LVIS
- ADE20K
- Kvasir-SEG
- ISIC 2018
- COD10K（伪装目标）

## 关系定位

HQ-SAM/MedSAM/RobustSAM/Conv-LoRA = **邻近工作**（冻结或额外模块，非 J_gen 约束）。WiSE-FT / R-Adapter = **kill 开关 / PEFT 插值**基线。RClicks/TETRIS = **评测协议约束**。

文献核验（2026-08-28）：在"保持 COCO 交互性能不退化"这一显式约束下微调 SAM 的论文 **NOT FOUND**。截至该次检索，该组合依然属于 OPEN（EVIDENCE = 检索未命中，非未发表之证明）。
