# 演化总结（Evolution summary）—— Windows8

日期：2026-08-28。Supervisor：Windows8。

## 流水线

| Stage | 目标 | 实际 | 备注 |
|-------|--------|--------|-------|
| 1 原始生成 | ≥1000 | **2766 条网格 + 3×350 条手工批次** | 网格在 `pool.jsonl` 与 `*_prior.md` 中。手工清单：`batch_A.md` / `batch_B.md` / `batch_C.md`（各 350 条）。Final 3 未变：A/B/C 手工清单强化了 objectness、PEFT 谱、IoU／评测校准这三条方向，而不是取代它们。 |
| 2 评审 | 约 200 | **200** | 优先级：因果性检验、便宜的证伪手段、高风险高回报、评审意见分歧大者。 |
| 3 Prior-work 攻击 | 约 50 | **50** | 默认判定：已被发表过。杀掉了纯指标类的 Dice 排名（CC-Dice AAAI 2025）。杀掉了"把 LoRA/Med-SA 当方法论文写"。 |
| 4 Reviewer #2 | 约 20 | **19–20** | 若没有实验能让攻击闭嘴就杀掉。杀掉了不可证伪的 SA-1B 成员推断，以及纯语言学层面的 SAM2-CD。 |
| 5 工程化 | 约 5 | **5** | ROI = 每 GPU-hour 能换到的信息量。 |
| 6 Battle | 3 | **3** | 不制造虚假共识；余留分歧列于下方。 |
| 7 打包 | 3 | **3** | Idea_01..03 |

## Stage 5 Top 5（按 ROI 排序）

1. IDEA-X-0004 Spectral LoRA audit（→ Idea_02）
2. IDEA-X-0001 排除区／objectness 提示（→ Idea_01）
3. IDEA-X-0003 IoU-token 选择性预测（→ Idea_03）
4. IDEA-X-0007 用 replay 保持可提示性
5. IDEA-X-0002 冻结 SAM embedding 上的密度解码器（已并入 Idea_01 的方法）

## Stage 6 未解决的分歧

- Idea_01 究竟是"只是提示／评测"（Skeptical PI 的看法），还是一次针对 objectness 的因果干预（分割专家的看法）。
- Idea_02 算是视觉领域的贡献，还是一份 PEFT 诊断（方法学评审的质疑）。决定：保留，因为如果谱的主张成立，它会预测出一个*新的 adapter*（高频残差）。
- Idea_03 是否只是经典的选择性分类。决定：只有在我们能证明 SAM 的 IoU 在无定形目标上是*反校准*（而不仅仅是弱校准）的情况下才保留。

## Final 3

| Package | 工作标题 | 起源 ID |
|---------|---------------|------------|
| Idea_01 | Objectness, Not Features | X-0001 + X-0002 + SAM-OBJECTNESS + LINEAR-PROBE |
| Idea_02 | Spectral Locality of Dense PEFT | X-0004 + PEFT-SPECTRAL |
| Idea_03 | Selective SAM via IoU-token Recalibration | X-0003 + SAM-IOU-CAL + SELECTIVE |

## 全程使用的认知等级标签

KNOWN FACT / EVIDENCE（有引用）/ HYPOTHESIS / MODEL SPECULATION / EXPECTED（未经测量）。
本轮没有产出任何真实的实验数字。
