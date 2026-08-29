# Idea_01 —— 在 CT 上 SAM AMG 算不算强度聚类？（Windows6 / F-067）

> **整份文档的认知状态。** 其中没有任何实验被执行过。每个量都是
> **HYPOTHESIS** 或 **EXPECTED RESULT**。Windows6 **没有产出任何 ACTUAL RESULTS**；
> `Windows6/README.md` 记录了 *"no real SAM numbers"*。引用仅在它们已出现于
> `selection_history/literature_anchors.md` 或 `literature.md` 时才属于
> **VERIFIED PRIOR WORK**；其他任何内容均标为 `CITATION NEEDED — 待人工核验`。

## 1. 标题与标识符

| 字段 | 取值 |
|---|---|
| 工作标题 | *Is SAM's Automatic Mask Generation Just Intensity Clustering on CT?* |
| Windows6 ID | `Idea_01` |
| Stage-1 来源 | `F-067`（`stage1_pool/F_001_080.jsonl`，种子 `amg`，变异 `cheaper`） |
| Stage-3 记录 | `sam-amg-intensity-clustering`，`continue: keep`，`novelty_confidence: 0.6` |
| Stage-4 记录 | `AMG-HU-clustering`，`continue: survive`，`advance: true` |
| 审计员 | 受保护的保留项（`auditor_overlay.md`） |
| 选题状态 | Final 3，**PROVISIONAL** —— 见 `selection_history/stage6_battle.md` §5 |
| 论文类型 | 分析型／短文 —— **不是**一个新的 decoder |

## 2. 一句话主张

**HYPOTHESIS。** 在做过窗宽窗位处理的 CT 上，SAM 的 Automatic Mask Generation
（AMG）返回的掩码清单近似于 Hounsfield 强度聚类，而这一点可以通过因果而非相关性
方式来确立：展示 AMG 能够追踪纯强度的干预，同时对保持强度的纹理干预保持不变。

## 3. 摘要

**HYPOTHESIS，未经测量。** 基础提示分割器常被当作 CT 上的自动候选区域生成器。
既有评测表明 SAM/SAM2 对窗宽窗位敏感，且在低对比度 CT 上较弱（**VERIFIED PRIOR
WORK**，arXiv 2408.04212，arXiv 2408.11210）。该观察*与*以下更强的主张相一致 ——
但并没有确立它：即 AMG 的掩码清单近似等价于 HU（或做过窗宽窗位的 8 位）空间中的聚类。
我们给出了一份预先注册的等价性检验，加上 Reviewer #2 强制要求的因果反事实实验：
保持边缘的强度重映射 vs 保持强度的纹理随机化。论文的贡献在于**反事实实验**，
而不是相关性。**不主张任何实验数字。**

## 4. 背景与动机

AMG 的用法就好像它产出的是语义物体候选一样。在自然图像上这种表述至少是可以讨论的。
在 CT 上它可能更接近于一个阈值操作：CT 是一种经过物理标定的单通道模态，其"物体"
很大程度上是由窗宽窗位映射后的 HU 平台值定义的，而一个没有解剖先验的分割器
可能除了这些平台值之外别无依凭。

若该等价性成立，将引出三项后果（**SPECULATION** —— 这些是利害关系，不是发现）：

1. 在 CT 上使用 AMG 作为语义伪标签的论文，实质是在注入强度超像素并将其称为 objectness。
2. MedSAM 式的微调可能在应对错误的失效模式 —— 在改善一个在 CT 上的行为完全由输入直方图主导的 decoder。
3. 任何 SAM-on-CT 的表格中都应包含一行经典的基线（标量 HU 上的 k-means），缺少它属于审稿失职。

**为什么是现在。** 廉价 killer 环节（`stage3_prior_work_kill_cheap.jsonl`）将
新颖性信心评为 **0.6** —— Windows6 中最高 —— 剩余新颖性为
*"Mechanistic AMG vs HU k-means equivalence on CT not found"*。

## 5. 问题陈述与研究问题

设 \(I\) 为 HU 下的 CT 切片，\(W\) 为有记录的窗宽窗位映射。AMG 在 \(W(I)\) 上产出
掩码清单 \(\mathcal{M}_{\mathrm{AMG}}\)。强度聚类器 \(C\)（k-means、multi-Otsu、GMM）
产出 \(\mathcal{M}_C\)；空间／纹理超像素方法 \(S\)（SLIC）产出 \(\mathcal{M}_S\)。

- **RQ1（相关性）。** \(\mathcal{M}_{\mathrm{AMG}}\) 是否比 \(\mathcal{M}_S\) 更接近 \(\mathcal{M}_C\)？
- **RQ2（因果性）。** \(\mathcal{M}_{\mathrm{AMG}}\) 是否*追踪*纯强度的干预，并忽略纯纹理的干预？
- **RQ3（范围）。** 任何 RQ1 的效应是跨窗宽窗位与 AMG 超参数稳定的，还是由单一预处理选择人为制造的？
- **RQ4（特异性）。** 该效应是 CT 特异的，还是在自然图像上也出现同样的等价性（若是后者，则关于 CT 什么都说明不了）？

## 6. 假设（预先注册）

- **H1。** 在固定临床窗之后，在预先注册的 CT 子集上，在 §15 的**全部三个**指标上，
  匹配的平均 IoU(\(\mathcal{M}_{\mathrm{AMG}}, \mathcal{M}_{k\text{-means}}\)) >
  IoU(\(\mathcal{M}_{\mathrm{AMG}}, \mathcal{M}_{\mathrm{SLIC}}\))。
- **H2（因果）。** 保持边缘的强度重映射对 AMG 的改变量，**大于**具有相同边缘图、保持强度的纹理置乱。
- **H3（范围）。** H1 的差距跨越 AMG 超参数网格并在 3 个窗中的 ≥2 个成立。若仅在恰好 1 个窗上成立，
  则该发现属于**设置假象** → 转向或 kill。
- **H4（特异性，Reviewer #2 先手防范）。** 在完全相同的协议下，H1 的差距在 COCO 上**不存在或小得多**。
  若 COCO 复现了它，则该主张是关于一般意义上的 AMG，而不是关于 CT，论文失去了研究对象。

## 7. 核心洞察

窗宽窗位是一个**单调强度映射**。单调映射不能创造或摧毁边缘的*位置*，但它会重新分配对比度 ——
因此如果研究只跑一个窗，"AMG ≈ 聚类"可以通过预处理本身人为制造出来。这正是 H2 存在的全部原因。

互补的洞察在于两条臂的设计。AMG 与 k-means 之间的相关性很容易获得，也很容易被打发。
不易被打发的是一次**双重解离**：一种干预在冻结边缘的同时改变强度，另一种在冻结局部平均强度的同时改变纹理。
若 AMG 跟随前者并忽略后者，"AMG 在读取强度"就从一种解释变成了测量结果。

## 8. 新颖性陈述

**VERIFIED PRIOR WORK。** 最接近的工作是在 CT 上*评测* SAM —— 针对器官的 Dice、窗宽窗位敏感性、
提示敏感性（arXiv 2408.11210，arXiv 2408.04212）。`literature_anchors.md` 明确将 SAM2 CT 评测
归入 *"Remaining-novelty targets"*，正因为它是一项黑箱评测，而**不是** AMG 对比聚类的检验。

**空缺（FACT，引自 `literature.md`）：** *"no AMG vs k-means Hungarian/ARI
study with texture-vs-intensity counterfactuals."*

因此新颖性不是"SAM 在 CT 上表现差" —— 那是已知的，本论文绝不能这样主张。新颖性在于
**机制 + 预先注册的多指标一致性 + 因果测量工具**。

## 9. 与既有工作的关系（差异化）

| 既有工作 | 状态 | 它确立了什么 | 为什么它不构成抢先 |
|---|---|---|---|
| Segment Anything, ICCV 2023 | **VERIFIED PRIOR WORK** | 定义了 AMG | 定义了研究对象；未对 CT 机制做任何主张 |
| SAM2 CT review, arXiv 2408.11210 | **VERIFIED PRIOR WORK** | 黑箱 CT 评测 | 报告性能存在差异，而不是 AMG 在*计算*什么 |
| SAM/SAM2 low-contrast CT, arXiv 2408.04212 | **VERIFIED PRIOR WORK** | 强度／窗宽窗位依赖性 | 最强的邻近工作。展示了对强度的敏感性；未检验与聚类器的等价性，也未做纹理对照 |
| HQ-SAM, NeurIPS 2023, arXiv 2306.01567 | **VERIFIED PRIOR WORK** | 掩码质量精修 | 在 Stage 3 用于杀掉邻近的 `F-012` 滤波主张。`literature.md` 记录了长期约束：*"we do not claim filter=HQ"* |
| SAMRefiner, arXiv 2502.06756 | **VERIFIED PRIOR WORK** | 掩码精修 | 与上方同族；精修不是机制 |
| MedSAM CT notes, arXiv 2408.03322 | **VERIFIED PRIOR WORK** | 基准背景 | 被 Reviewer #2 作为背景引用 |
| Metrics Reloaded, Nature Methods 2024 | **VERIFIED PRIOR WORK** | 指标选择指导 | 约束*我们*的指标选择；它杀掉了同胞想法 `F-022`，我们绝不能通过报告定义性性质重蹈覆辙 |
| SLIC superpixels | `CITATION NEEDED — 待人工核验` | 空间超像素 | 我们的纹理／空间对照 |
| Multi-Otsu, GMM, k-means, ARI, Hungarian matching | `CITATION NEEDED — 待人工核验` | 经典基线与指标 | 标准工具；正式引用必须在投稿前核实 |

## 10. 重要性 —— 如果我们对了，谁错了

- **若 H1 + H2 成立：** 每一篇把 CT 上的 AMG 输出当作语义候选区域的论文都欠缺一个 k-means 基线。审稿人获得了一项一行代码级的检查手段。
- **若 H1 成立但 H2 失败：** 诚实的产出是一篇 **evaluation note**（§20）—— 有一致性而无机制。这是 Reviewer #2 的残余要求所明确预料到的结局。
- **若 H1 失败：** AMG 在 CT 上做的事情超越了纯强度，这比我们原本寻找的结论是一个更有趣的正面发现，值得作为针对我们自身假设的负结果来报告。

诚实地指出回报的不对称性："AMG 算聚类"这一方向是许多评审本就半信半疑的，因此必须因果性地交付，否则会被读成对传闻的印证。

## 11. 方法概览

1. 用有记录的 W/L 对 \(I\) 进行窗宽窗位处理。三个临床窗。
2. 在超参数网格上运行 AMG。
3. 运行强度聚类器与空间对照。
4. 为每个（AMG 设置 × 基线 × 窗）单元格计算全部三个一致性指标加两个基数诊断量（§15）。
5. 施加两种干预，重跑 AMG，测量自一致度。
6. 在 COCO 上重复整个协议作为特异性对照。

实现位于 `src/amgclust/`。`pipeline.agreement_profile` 回答 H1，`pipeline.counterfactual_profile`
回答 H2。两者都不返回裁决 —— 阈值写在 `experiments.md` 中并由调用方施加，因此分析代码内部
无法悄悄调参。

## 12. 干预措施（因果工具）

| 臂 | 改变什么 | 固定什么 | 有效性检查（必须通过，否则该臂不构成证据） |
|---|---|---|---|
| **强度重映射** | HU 值（通过严格单调映射） | 边缘位置（Sobel 支撑） | `check_remap_is_monotone` —— 像素值次序保持 |
| **纹理置乱** | 每个小块内部的高频残差 | 每块的平均强度 | `check_shuffle_preserves_tile_means` —— 块均值误差在 1e-9 内 |

**为什么单调性是承重的。** 非单调重映射会创造或摧毁边缘，从而使强度臂与它本应固定的边缘结构发生混淆。
`intensity_remap` 在 `gamma <= 0` 时抛异常，而不是静默产生非单调映射。

**为什么均值保持是承重的。** 若纹理臂改变了局部 HU 水平，任何 AMG 响应都可归因于强度，解离就会瓦解。
块均值检查正是允许使用"保持强度"一词的前提。

当任一检查失败时 `pipeline.counterfactual_profile` 抛出 `RuntimeError`。损坏的测量工具不产出任何数字，
而不是产出一个看起来可发表的数字。

## 13. 空模型与基线

| 角色 | 方法 | 目的 |
|---|---|---|
| 强度聚类器 | 标量 HU 上的 k-means，k ∈ {8,16,32} | 假设的正对照 |
| 强度聚类器 | multi-Otsu | 阈值族对照；防范"k-means 具有特殊性"的质疑 |
| 强度聚类器 | 一维 GMM | 软分配对照 |
| 空间／纹理 | SLIC | **具有区分力的基线。** 聚类必须胜过*超像素*，而不只是胜过随机 |
| 特异性 | COCO 上的全套协议 | H4 |
| 健全性 | 合成分段常数 phantom | 卡片 E0；仅用于检验测试台 |

**Reviewer #2 的第三条攻击在这里得到回应：** "k-means 是众多廉价基线之一" —— 因此 Otsu、GMM 和 SLIC
全部运行，聚类必须胜过超像素，而不仅仅是与 AMG 相关。

## 14. 数据集

| 数据 | 角色 | 状态 |
|---|---|---|
| TotalSegmentator 或 MSD CT 切片，n = 100 | 主要数据 | 见 `experiments.md`。数据集论文标为 `CITATION NEEDED — 待人工核验` |
| COCO 子集 | H4 特异性对照 | `CITATION NEEDED — 待人工核验` |
| 合成 phantom（`data.synthetic_ct`） | 仅用于测试台验证 | 随本 package 提供 |

**FACT。** 记录中的 `n` 曾不一致：`README.md` 与 killer 清单写 50，Stage-5 工程化区块写 100。
`stage6_battle.md` §4.7 记录了它，§6 裁定为 **100**。本 package 全文使用 100。

不重新分发患者数据；仅分发公开数据集标识符与派生指标。

## 15. 指标与统计分析

**预先注册，全部三个永远同时报告。** 报告迎合假设的子集属于指标挑选攻击（`reviewer_attacks.md` A4），
因此代码没有"选最优指标"的辅助函数，`run_smoke.py` 并排打印全部三个裁决。

| 指标 | 对什么敏感 |
|---|---|
| **Hungarian IoU** | 掩码集合间最优的一对一匹配质量 |
| 像素标签图上的 **ARI** | 划分一致性，已做随机校正 |
| ±2 px 处的 **Boundary-F** | 轮廓放置位置，而非区域重叠 |

加上两项**诊断量**（仅报告，不承载假设）：

- **`coverage_iou`** —— 来自 `references/math.md` 的有向公式 \((1/|A|)\sum_A \max_B \mathrm{IoU}\)。
  追问"每个 AMG 掩码是否都能被*某个*聚类解释？"。
- **`cardinality_ratio`** —— \(|A|/|B|\)。

**为什么归一化方式发生了改变（W6-T3，至关重要）。** Hungarian IoU 按 \(\min(|A|,|B|)\) 归一化，
而不是 \(|A|\)。AMG 返回数十个嵌套掩码构成的清单，而聚类器返回 \(k\) 类划分；除以 \(|A|\) 大部分是在测量
基数差异，即便子集完美匹配也会报告接近零的一致度。基数*确实*是真实的差异 —— 正因如此它被显式报告，
而不是被静默折进一致性数字中。

**统计方法。** 逐切片配对比较（每张切片都经过每个基线），切片上的 bootstrap 置信区间，
且 H1 的裁决要求在全部三个指标上符号一致。**未预先注册 p 值阈值**；§20 中的决策规则是跨条件的效应方向规则，
这比单一显著性检验更难被操纵。

## 16. Killer 实验（首跑）

`experiments.md` 卡片 **E1**。100 张 CT 切片、软组织窗、SAM ViT-B AMG 对比 k-means / multi-Otsu /
GMM / SLIC，全部三个指标。预算 **约 2 GPU-h（HYPOTHESIS**，抄录自 `evolution_summary.md`；非测量值）。

称其为 killer，是因为它便宜、不需要训练、不需要罕见 checkpoint，且其失效模式（§20）直接终结项目，
而不是引发打补丁。

## 17. 完整实验方案

| 卡片 | 内容 | 预算（HYPOTHESIS） |
|---|---|---|
| E0 | 合成测试台验证，CPU | 约 0 |
| E1 | Killer：相关性臂，单个窗 | 约 2 GPU-h |
| E2 | 窗扫描 × AMG 网格（H3） | 约 8–20 GPU-h |
| E3 | **反事实各臂（H2）** | 约 2–4 GPU-h |
| E4 | COCO 特异性对照（H4） | 约 2 GPU-h |
| E5 | SAM2 泛化性（可选） | 约 4–8 GPU-h |
| E6 | 失败案例定性检查（金属、对比剂） | 约 1 GPU-h |

**FACT。** `experiments.md` 将完整矩阵记录为 *"~40–80 GPU-h (windows × SAM variants × counterfactuals)"*。
那是上限；§28 中的决策树旨在确保大部分预算永远无需花销。

## 18. 消融与对照

- **窗宽窗位消融：** 3 个临床窗 —— 这*就是* H3，不是可有可无的补充。
- **k 消融：** k ∈ {8,16,32}；H1 的差距绝不能依赖某一个好运的 k。
- **AMG 网格：** `points_per_side` ∈ {16,32}。
- **指标消融：** 全部三个指标，永远同时报告。
- **基数控制：** 报告 `|A|/|B|`，防止有人声称一致度是计数假象。
- **测量工具消融：** 改变 `remap_gamma` 与 `shuffle_tile`；若 H2 的方向随 tile 尺寸翻转，则纹理臂测的是 tile 尺寸。
- **领域对照：** COCO（H4）。

## 19. 预期结果（全部为 EXPECTED RESULT —— 未经任何测量）

- **EXPECTED。** 在主要窗下，Hungarian IoU 与 ARI 将强度聚类器排在 SLIC 之上；boundary-F 在三者中区分力最弱，
  因为两个家族都把边缘放在高梯度位置。
- **EXPECTED。** 肺窗下的差距收窄，那里空气／组织对比度使得几乎任何方法都能达成一致。
- **EXPECTED。** H2 的解离效应若为真，其幅度小于 H1 的差距 —— 因果效应通常如此 —— 因此 E3 需要比 E1 更多的切片，而不是更少。
- **SPECULATION。** COCO 显示出弱得多的差距。若非如此，见 §20。

以上均未被实际观测到。`run_smoke.py` 中的合成运行属于测试台自检，其数字不承载证据效力。

## 20. 可证伪性与 Kill 条件

| 触发条件 | 动作 |
|---|---|
| 在**全部**窗下 SLIC 一致度 ≥ k-means | **KILL** |
| 纹理置乱对 AMG 的扰动幅度与强度重映射大致相当 | **KILL 机制性主张** → §20.1 |
| H1 仅在 3 个窗中的恰好 1 个成立 | **PIVOT** —— 报告为窗宽窗位假象 |
| AMG 相比 k-means 更接近真值 **且** 纹理置乱大幅扰动 AMG | **KILL**（Stage-5 门禁） |
| COCO 复现了等价性 | **KILL CT 特异性主张**；最多写一篇通用 AMG 注记 |
| 某条臂未通过有效性检查 | **无结果**；修测量工具，不予报告 |

### 20.1 降级路径，以及记录中尚未解决的冲突

**FACT。** Reviewer #2 的残余要求原文为：*"Must earn mechanistic via intensity vs
texture counterfactuals; **else evaluation note**"* —— 一次降级。

**FACT。** 本 package 中的 `reviewer_attacks.md` 写道：*"If we cannot run the
causal arm, **do not submit**."* —— 扣下不发。

针对同一情况存在两种不同指令，没有产物指明以何者为准。`stage6_battle.md` §4.4 将该冲突登记为未解决。
**必须在动笔前定夺，而不是在写作期间。** 两处读法在 H2 失败时决定的是产出一篇更短的论文还是完全不发。

## 21. 混淆因素与缓解措施

| 混淆因素 | 缓解措施 |
|---|---|
| 窗宽窗位制造出一致度 | 3 窗扫描；将 H3 作为 kill 条件 |
| AMG 过分割虚高任何匹配分数 | Hungarian 一对一 + 显式 `cardinality_ratio` |
| 纹理置乱改变局部强度 | 块均值有效性检查，代码强制 |
| 强度重映射移动边缘 | 单调性检查，代码强制 |
| Tile 尺寸驱动 H2 结论 | 变化 `shuffle_tile`（§18） |
| 指标挑选 | 三个预先注册的指标全部报告 |
| 切片选择偏向简单解剖结构 | 运行前预先注册切片清单 |
| 该效应是一般性 AMG 规律而非 CT 特性 | COCO 对照（H4） |

## 22. Reviewer #2 合规矩阵（有约束力）

| # | 攻击（`reviewer_attacks.md`） | 约束性义务 | 在何处满足 |
|---|---|---|---|
| 1 | 窗宽窗位制造出结论 | 扫描 3 个窗，全部报告 | E2 / H3 |
| 2 | 一致度 ≠ 机制 | 强度重映射 vs 纹理置乱 | E3 / H2 / §12 |
| 3 | k-means 只是众多廉价基线之一 | 增加 Otsu、GMM、SLIC；必须胜过超像素 | §13 |
| 4 | 指标挑选 | 预先注册 IoU + ARI + boundary-F | §15 |
| 5 | "SAM 在 CT 上不行"已知 | 交付机制，而非 Dice 表格 | §8, §10 |
| 6 | 超参数脆弱性 | AMG 网格 | §18 |

**残余义务（FACT，原文）：** *"Must earn mechanistic via intensity vs texture
counterfactuals; else evaluation note."* 卡片 **E3** 是其全部所在，这正是 §28 在 E3
出结论前拒绝投稿的原因。

## 23. 范围边界

- **不是**新的 decoder、损失函数或 adapter。
- **不是**关于 SAM 在 CT 上表现差的主张。
- **不是**关于引导滤波能追平 HQ-SAM 的主张 —— 那属于邻近的 `F-012`，`stage2_ABCF_summary.md` 明确禁止这种表述。
- **不是** 3D。仅限单张切片；体积一致性不在讨论范围内。
- **不是**与 MedSAM 的横向比拼。适配方法属于背景，不是研究对象。

## 24. 算力与资源预算

**全部为 HYPOTHESIS。** Day-1 约 2 GPU-h（`evolution_summary.md`）。通向完整论文的决策树路径
约 15–35 GPU-h。完整矩阵上限 40–80 GPU-h（`experiments.md`）。卡片 E0 为 CPU 数秒，完全不需 GPU。

无训练。不需要 checkpoint 三元组。这是 Windows6 Final 3 中最便宜的一个，也是 `README.md`
将其标为 *"#1 start here"* 的原因。

## 25. 可复现性与发布计划

- 随机种子通过 `config.set_seed` 固定，返回显式 `Generator`，函数从不读取全局 RNG 状态。
- 配置即数据（`configs/*.yaml`）；未知键抛异常而非被忽略，防止静默漏字段。
- `tests/test_smoke.py` 纯基于 numpy 运行 —— 无需 scipy、PyYAML 或权重。
- 发布：代码、配置、预先注册的切片清单以及逐切片指标 CSV。仅限派生指标；不重新分发患者数据。

## 26. 风险与缓解

| 风险 | 严重度 | 缓解措施 |
|---|---|---|
| H2 失败 → 降级为 evaluation note | 高 | 接受该结局，但必须先解决 §20.1 |
| 并行工作发表了等价性 | 中 | 协议便宜；尽早跑 E1+E3。暴露面低于 Idea_03，因为我们的空缺是结构性的而非由缺席定义的 |
| AMG 掩码数量导致匹配不稳定 | 中 | 基数诊断量；对 `min_area` 的敏感性分析 |
| 仅单一窗显示效应 | 中 | 预先声明的转向（§20） |
| 评审将其读为"SAM 在 CT 上不行" | 中 | §8、§23 中的表述纪律 |

## 27. 伦理与数据考量

基于各自许可下的公开去标识化 CT 数据集。不尝试重新识别，不重新分发患者影像。
不作任何临床主张：这是一项关于模型行为的研究，而非关于诊断。若结论成立，其实践信息是给
方法开发者的告诫，而非给临床医生的。

## 28. 交付物与决策树

**交付物。** 短篇分析论文；测试台；预先注册的切片清单；逐切片指标表格。

```
E0 测试台  ──失败──> 修实现（绝非科学结论）
   │通过
E1 killer   ──全部窗下 SLIC ≥ 强度──> KILL
   │H1 成立
E2 窗扫描   ──仅 1/3 窗成立──> PIVOT: 窗宽窗位假象
   │≥2/3 窗成立
E3 因果     ──置乱 ≈ 重映射──> 降级为 evaluation note（先定夺 §20.1）
   │解离成立
E4 COCO     ──COCO 复现了该效应──> KILL CT 特异性；最多为通用 AMG 注记
   │CT 特异
   └─> 机制性论文。E5/E6 为可选加强项。
```

**候选标题。** *Is SAM AMG Just Intensity Clustering on CT?* ·
*Windowing, Superpixels, and the Objectness of Foundation Models* ·
*A Causal Test of SAM's CT Objectness*
