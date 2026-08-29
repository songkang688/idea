# Windows1 研究总结

## 漏斗（去重后的近似值）

| 阶段 | 数量 | 说明 |
|---|---|---|
| Stage 1 原始 | ≥1065（SEG 365 + 本地 VFM ~350 + 本地 ASM ~350 + VFM-A 180 + ASM-A 180；有重叠） | 云端 350 条想法的任务两次超时；靠本地池加紧凑批次补足了 ≥1000 的要求 |
| Stage 2 | SEG 保留约 84 条 + VFM/ASM 的入选者 | 独立打分；HRHR（高风险高回报）受保护 |
| Stage 3 | 约 20 条被攻击 | 默认判定为"已发表"；有若干条与 2024–2026 年的工作精确撞车 |
| Stage 4 | 12 条变异形态 | 无一条无条件 KEEP；有 1 条 KILL（replica-spiking 通胀曲线） |
| Stage 5 | 先工程化到 8 条，再收到 5 条 | killer 实验已明确指定 |
| Stage 6 | **Final 3** | A RetainSAM、B LesionSuppress、D DisagreeShift |

## 已锁定的假设（可证伪）

1. **RetainSAM（HYPOTHESIS）：** 带可提示性约束的 SAM 微调，在（目标域 Dice，通用 k 次点击 mIoU）这一 Pareto 前沿上严格优于 WiSE-FT 插值。若插值打平或反超，则假设被证伪。
2. **LesionSuppress（HYPOTHESIS）：** 由合成插入病灶得到的"抑制率 vs（尺寸，CNR）"秩序，与 LIDC 上按同样分箱匹配的真实小结节敏感度一致（Kendall τ 显著大于 0）。若 τ 偏低或符号翻转，则被证伪。
3. **DisagreeShift（HYPOTHESIS）：** 在扫描仪或染色偏移下，用分歧训练出的不确定性场在**稀疏化曲线／逐像素 AURC** 上优于硬标签 + temperature scaling，即使 ECE 可以被调平也是如此。若 TS 在这些对排序敏感的指标上打平，则被证伪。

## 明确不主张的内容

- 本轮我们**没有**训练任何模型，也**没有**实测任何 Dice/mIoU/τ。
- 新颖性的信心度是**对抗式检索之后的后验判断**，不构成"尚未被发表"的证明。
- 已有若干相邻论文占据了附近的位置（HQ-SAM 的权衡表格、WiSE-FT、多评分者概率分割、去噪读片者研究）。
