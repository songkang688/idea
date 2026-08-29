# Stage 4 → Top-20 (Windows4)

日期：2026-08-28。Reviewer #2 存活条件 = 实验能够平息质疑。

## REJECT (淘汰项)

P060, P001, P004, P007, P110, P108, P107v-as-flagship (因 HalluSegBench 抢先发表而被淘汰)

## WEAK ACCEPT / SILENCED (20 个席位；19 个独立设想 + P082 作为把关项而非独立论文)

| Rank | ID | One-liner | Binding obligation |
|------|-----|-----------|-------------------|
| 1 | P14 | SAM 视觉感知 vs 框到掩码插值 | On-manifold inpaint/swap + box→mask nulls |
| 2 | P065 | 提示类型遗忘测试套件 | Mixed-prompt FT column |
| 3 | P063 | 特征空间折射 | A1-067 first; IOR=1 twins |
| 4 | P096 | 烟雾指标反转 | Measured-alpha real arm |
| 5 | P079 | SAM2 记忆内容探测 | Subtract explicit time encodings |
| 6 | P103 | 抠图→烟雾迁移 | Binarized-matting arm; real-smoke primary |
| 7 | P177 | 解码器位点遗忘 | Stitching controls |
| 8 | P082 | 遗忘噪声下限把关 | Run first on released ckpts |
| 9 | P107 | LoRA 放置位置 vs 错误类型 | Matched-param + decoupled metrics |
| 10 | P044 | 预处理 vs PEFT | Pre-registered ≥50% recovery |
| 11 | P042 | 各向异性混淆因素 | Slice-decimation not interpolation |
| 12 | P031 | IoU 头部失步 | Recalibration cell mandatory |
| 13 | P079f | FSS 背景置换 | Sham-swap + BAM control |
| 14 | P051 | Copy-paste vs 扩散模型 | Amortization frontier |
| 15 | P040 | 边界扩散性 | Width×contrast two-factor |
| 16 | P052 | 目标特性 (Stuff-ness) × 小样本初始化 | 关注交互效应，而非 “FM hurts” |
| 17 | P228 | 模型内非典型提示 | BiomedParse; not B1-107 |
| 18 | P101 | 嵌入范数粒度 | Matched-area vs threshold/3-head |
| 19 | P061u | 风格 × 自训练交互效应 | Fixed backbone 2×2 |
| 20 | P177-arm | 仅作为冻结编码器插图 | Not standalone |

## Top 5 (Stage 5)

1. P14 SeeingInside
2. P065 PromptAmnesia (gated by P082)
3. P103+P096 AlphaSmoke (transfer + metric protocol)
4. P063 RefractionFeatures
5. P079 MemoryProbe

## 最终 3 项 (经 R2 + ROI 评估，无虚假共识)

参见 `stage6_battle.md`。锁定项：

- **Idea_01 SeeingInside (P14)** — 推荐 #1
- **Idea_02 PromptAmnesia (P065/P082/P177)**
- **Idea_03 AlphaSmoke (P103/P096)**

若第 1 周内有 Killer Experiment 证伪/淘汰了某个主选设想，P063/P079 作为首选备选方案。
