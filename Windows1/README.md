# Windows1 — 研究想法演化（Research Idea Evolution）

- **Windows 编号：** 1（本仓库此前没有任何 Windows 目录）
- **创建日期：** 2026-08-28
- **Supervisor 身份：** Windows1
- **仓库：** `songkang688/idea`

## 本轮的三个想法

| ID | 简称 | 一句话概括 | 状态 |
|---|---|---|---|
| **Idea_01** | **RetainSAM** | 在目标域上微调 SAM，但**施加可提示性保持约束（promptability-retention constraint）**，并要求该方法在提示行为的 Pareto 前沿上**严格优于（strictly dominate）WiSE-FT 插值**。 | 可以开跑 killer 实验 |
| **Idea_02** | **LesionSuppress** | 测量**病灶抑制概率（lesion-suppression probability）**随尺寸、对比度、增强强度的变化关系；用 LIDC 真实小结节验证其秩序（rank-order）；除非该结论能存活，否则放弃任何"普适定律"式的主张。 | 可以开跑 killer 实验 |
| **Idea_03** | **DisagreeShift** | 在**评分者间分歧（inter-rater disagreement）上训练逐像素不确定性场**，检验它在扫描仪／染色偏移下是否仍保有**对排序敏感（ordering-sensitive）**的含义——而硬标签 + temperature scaling 在结构上做不到这一点。 | 可以开跑 killer 实验 |

## 首推

**Idea_01 RetainSAM。**

它是最终三个里唯一一个构建方法的项目，拥有最便宜的决定性证伪手段（必须打败 WiSE-FT），而且即使失败也留下一套可复用的可提示性保持基准。如果 WiSE-FT 本身就已经刻画出了整条 Pareto 前沿，则在第 1 周就杀掉 Idea_01，并把 Idea_03 提为首推。

## 第一个要跑的实验

**RetainSAM 判杀测试（第 1 周）：**

1. 用标准配方在一个医学数据集（Kvasir-SEG 或 ISIC）上微调 SAM ViT-B。
2. 对 α ∈ {0, 0.1, …, 1} 做插值 `θ(α) = (1−α) θ_SAM + α θ_FT`（即 WiSE-FT）。
3. 在 COCO/LVIS 留出图像上评估目标域 Dice **以及**一整套冻结的可提示性测试（1/3/5 次点击的 mIoU、框提示、迭代式 NoC）。
4. 把带约束的目标函数训练一次。
5. 若带约束的微调没能在 **≥2 个工作点上严格优于**插值，则**杀掉 Idea_01**。

## 后续实验（无论 Idea_01 存活还是被杀）

- 并行推进（低 GPU 消耗）：Idea_02 在一个病灶族上做合成数据与 LIDC 的秩相关；Idea_03 在一个留出扫描仪上做 LIDC 稀疏化 vs 硬标签+TS。

## 组合构成（为什么不是三篇评测论文）

Stage 6 锁定的是**方法 + 医学安全性刻画 + 医学不确定性方法**这个组合。次席 **SEG-0276-M**（先验形状插值 α）属于高风险高回报（HRHR）且只需推理，若 Idea_01 死于 WiSE-FT *且* Idea_03 的 TS 基线意外地打平，则复活它。

## 本目录使用的认知等级规则

`KNOWN FACT`、`EVIDENCE`、`HYPOTHESIS`、`MODEL SPECULATION`、`EXPECTED RESULT`、`ACTUAL EXPERIMENTAL RESULT` 均有标注。**本存档中没有任何数字是我们实测得到的。** 预测曲线一律只是 `EXPECTED`。
