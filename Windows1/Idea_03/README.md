# Idea_03 —— DisagreeShift

**候选标题**

1. Disagreement Fields that Travel: Pixelwise Rater Variability under Scanner and Stain Shift
2. Temperature Scaling Cannot Reorder Pixels: Why Soft Multi-Rater Training Matters OOD
3. Calibration that Means Something: Sparsification of Segmentation Uncertainty under Shift

## 1. 摘要

在**标注者间分布上训练分割概率场**（而非多数投票的硬标签）。在**扫描仪或染色偏移**下用**对次序敏感的指标**（稀疏化 / 逐像素 AURC）进行评测。用于击杀的基线是硬标签训练 + 温度缩放（Temperature Scaling, Guo et al., 2017）。TS 是**单一标量**，无法重新对像素排序；若它依然能匹敌 AURC，说明我们的训练没有产生更好的误差**排序**，项目死亡。

最初的 SEG-0074（经病理学验证的浸润图）被现有的 MRI–病理学管线 **kill** 掉了。这项变异是一个不同的问题：**当准确率无法迁移时，以分歧形态呈现的不确定性能否迁移？**

## 2. 动机

KNOWN：Probabilistic U-Net、随机分割网络、LIDC 4 位标注者、QUBIQ。社区默认做法：报告共识上的 Dice，可能加上 ECE。HYPOTHESIS：即便在 OOD 场景下 ECE 也可通过 TS 修复，而模型**在何处**不确定（标注者冲突区域 vs 随机边界）除非在分歧上训练，否则无法迁移。

## 3. 问题定义

对于图像 x，标注者 {y^{(r)}} 给出逐像素频率 f(x)_i ∈ [0,1]。学习 p_θ(x)_i。在领域偏移 T(x) 下，对比：

- 对比多数投票的 Dice
- 对比 f 的 ECE / NLL
- **稀疏化（Sparsification）：** 移除前 k% 最不确定的像素，测量剩余的 Dice/误差；AURC

## 4. 核心假设

**H1：** 在留出扫描仪（LIDC）或染色／中心（病理学）下，在匹配的 Dice 水平下，在分歧上训练的 p_θ 相比硬标签 + TS 具有**更低的稀疏化误差／更好的 AURC**。

**H2：** 在高标注者熵的分组中该差距更大。

若 TS 在主偏移上匹敌 AURC 则 kill。若校准可迁移但 Dice 叙事模糊，则转向选择性预测／弃答。

## 5. 关键洞察

TS 无法实现空间层面的分歧。若我们依然落败，要么说明标注者的空间冲突无法从当前数据集规模学到，要么说明分布偏移破坏了编码它的特征。

## 6. 新颖性

Prob U-Net 预测的是**域内**分布。多标注者论文已有。**空缺：** 在**对次序敏感的指标**上，针对**结构上不具备该能力**的基线（标量 TS）进行偏移评测。信心：逻辑空缺上中偏高；实证取胜上中等。

## 7–10.

见文献、架构图、数学形式：

\[
\mathcal{L}_{\mathrm{soft}} = \mathrm{KL}\big(f \,\|\, \sigma(z_\theta)\big)
\quad\text{或}\quad
\mathrm{BCE}(\sigma(z_\theta), f)
\]

对比多数类上的硬 CE + logit 上的 TS。

标注者专属头（Tanno 式）作为可选消融。

## 11–17.

`src/disagree_shift/` 指标 + 虚拟训练器。Killer 实验：若元数据允许则采用 LIDC 留一扫描仪；否则采用 LIDC 上的合成染色／噪声偏移作为**代理**（声明代理性质）。

## 18. 预期

EXPECTED：硬标签 vs 软标签在偏移下具有相似的 Dice 下降；AURC 差距偏向软标签，尤其在高熵像素上。未经测量。

## 19–22.

致命风险：扫描仪太少；在偏移后验证集上调 TS 作为偷偷使用的 oracle。预先注册：TS **仅**在源域验证集上拟合。

R2："QUBIQ 已经做过了。" 应答：QUBIQ 是域内的多标注者研究；我们增加了**偏移 + TS kill 检验**。

## 23. 算力

Killer 约 4 GPU-days（2D U-Net）。完整方案约 16。

## 25. 停止条件

H1 失败则 kill。若在 2 个偏移上 AURC 取胜则继续。

## 27. 立意

一旦更换扫描仪，硬标签加温度计无法将不确定性放置在医生存在分歧的位置；在分歧上训练可以做到 —— 或者它也做不到，而我们应当停止假装 ECE 是部署时关心的量。
