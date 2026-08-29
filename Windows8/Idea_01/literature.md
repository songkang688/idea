# Idea_01 文献

只列真实、可核查的条目。访问日期 2026-08-28。

| 论文 | 年份 | 会议／ID | 与本课题的关系 |
|-------|------|------------|----------|
| Kirillov et al., Segment Anything | 2023 | ICCV / arXiv:2304.02643 | 基础模型；objectness 接口 |
| Ravi et al., SAM 2 | 2024 | arXiv:2408.00714 | 视频记忆；必需的泛化性验证 |
| Ma et al., MedSAM | 2024 | Nature Communications / arXiv:2304.12306 | 医学全量微调；遗忘问题的对照 |
| Wu et al., Medical SAM Adapter | 2023/2025 | arXiv:2304.12620, MedIA 2025 | adapter 的 SOTA，我们必须在 killer 实验中*不更新编码器*的前提下胜过它 |
| SAMed | 2023 | arXiv:2304.13785 | 在 SAM 编码器上做 LoRA |
| LoRA-MedSAM | 约 2025 | Springer 书章 | 效率导向的 LoRA；以 Dice 为中心 |
| HQ-SAM, Ke et al. | 2023 | arXiv:2306.01567 | high-quality token；物体边缘 |
| CD-concept SAM eval | 2024 | arXiv:2412.01240 | 对烟雾／透明这类 CD 概念的评测 |
| Tree-like / low-contrast SFM limits | 2024 | arXiv:2412.04243 | 竞争性的纹理机制解释 |
| Promptable fire segmentation | 2025 | arXiv:2510.21782 | 火焰上的框提示 |
| Trans10K | 2020 | 透明物体数据集 | 泛化性验证集 |
| nnU-Net, Isensee et al. | 2021 | Nature Methods | 同等标注量／专用模型对照 |
| LoRA, Hu et al. | 2022 | ICLR | PEFT 的基本构件（Idea_02 中使用） |
| Connected-component metrics | 2025 | AAAI | 作为指标使用，不作为贡献点 |

不要把未经核实的 clawrxiv 式条目当作证据引用。
