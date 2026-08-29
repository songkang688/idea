# Windows4 — 自主研究想法演化（Autonomous Research Idea Evolution）

- **Windows ID：** Windows4
- **创建日期：** 2026-08-28（UTC）
- **Supervisor：** Windows4
- **仓库：** `github.com/songkang688/idea`
- **状态：** Top-3 packages 归档已 COMPLETE（本次运行没有实测任何实验数字）

## 本轮的三个 Idea

| # | 目录 | 代号 | 科学问题 |
|---|--------|----------|---------------------|
| 1 | `Idea_01/` | **SeeingInside** | SAM 究竟是否用到了紧致框*内部*的图像证据，还是说它只是一个"框→掩码"的插值器？ |
| 2 | `Idea_02/` | **PromptAmnesia** | 在域内 Dice 被调平的前提下，领域 PEFT 是否毁掉了提示类型技能（点／负点／multimask）？ |
| 3 | `Idea_03/` | **AlphaSmoke** | 在*真实烟雾*上，matting 预训练是否优于分割预训练；以及在 alpha/matting 指标下，二值 Dice 的排名是否会翻转？ |

## 最推荐

**Idea_01 SeeingInside。** 它是唯一一个核心新颖性在 prior-work 刺杀中存活下来、*并且* Reviewer #2 的攻击能被一个便宜的 on-manifold 反事实实验封住嘴的旗舰项目。它不需要医学微调的算力，不与 MedSAM/ProFSAM/Gu et al. 竞争，而且即使得到 null 结果，作为关于 SAM 的一条机制性事实也仍然可发表。

## 为什么另外两个不是首推

- Idea_02 的影响半径（blast radius）更大，但它被 P082 卡住（"遗忘"可能只是一个阈值假象），而且除非把混合提示那一列做成论文主体，否则会被 CA-SAM/Gu et al. 挤占。
- Idea_03 是那篇该做的烟雾论文，但 R2 要求必须有一条实测 alpha 的实验臂、且以真实烟雾为主实验；数据与标注风险更高。

## 状态

三个项目均为：**可以开始 killer 实验**。Idea_01 的 `artifacts/e0_smoke/` 是一次**桩后端（stub-backend）的流程自检**（在合成数据上跑 boxfill/oracle 桩），**不是** SAM/COCO 的结果。Idea_02 的代码在没有提供真实权重时只会输出 NaN 骨架。

## 本周要跑的下一个实验

**Idea_01 的 killer：** 当权重就位时，用冻结的 SAM-ViT-B 执行 `python -m src.eval`（见 `Idea_01/README.md`）；否则桩 e0 路径只能检查决策逻辑本身。

然后是 Idea_02 在一个公开 MedSAM checkpoint 上做 P082 阈值扫描。再然后是 Idea_03 在一个公开烟雾数据集上做 HSV + 冻结编码器探针。
