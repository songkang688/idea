# Idea_02 —— LesionSuppress

**候选标题**

1. When Enhancement Erases the Finding: A Lesion-Suppression Safety Spec
2. Size–Contrast–Strength Curves for Silent Lesion Loss under Denoising and SR
3. Do Not Trust the Clean Image: Measuring Suppression of Small Findings

## 1. 摘要

深度去噪与超分辨率（SR）可能**消除或幻觉出**微小的临床病灶。我们**不**主张跨所有管线的普适定律（该主张在评审中已被杀）。我们主张一份**安全规范**：针对指定的管线族，估计

P(suppress | size, CNR, strength)

并检验各分组的**排名顺序**是否与 LIDC-IDRI 上的**真实**小结节敏感度相匹配。若合成排名无法迁移，项目死亡。

## 2. 动机

KNOWN：医学物理中的基于任务的图像质量；厂商 DLR/SR 后的读者研究；深度学习图像恢复的幻觉指标。HYPOTHESIS："先去噪后分割"的论文低估了**真实病灶删除**（抑制）相对于虚假结构插入（幻觉）的发生率。监管／安全受众关注微小、低对比度病灶的抑制。

## 3. 问题定义

设 x 为体积／切片，ℓ 为带有属性（尺寸，对比度噪声比 CNR）的病灶。设 T_s 为强度为 s 的增强算子（降噪等级、SR 尺度、GAN 权重）。冻结的检测器 D（在**未增强**数据上训练的 nnU-Net / nnDetection）若在 T_s 后的检测命中 ℓ，则产生一次 hit。

抑制事件：ℓ 在 x 上被检测到，但在 T_s(x) 上未被检测到，或检测得分跌破预先注册的工作点。

## 4. 核心假设

**H1（迁移性）：** 在匹配的 (size, CNR) 分组中，合成病灶抑制率与真实 LIDC 小结节漏诊率增量之间的 Kendall τ > 0，且置信区间排除 0。

**H2（剂量响应）：** 对每个管线族分别而言，P(suppress) 随 s 增大而增大，随 size 和 CNR 增大而减小。

**H3（普适性）—— 可选，默认关闭：** 将 s 缩放到公共轴后，各管线族坍缩为同一曲线。我们**不需要** H3 即可发表。

若 H1 在主要管线族（CNN 去噪器）上失败，则 kill 项目。若 CHO 与 nnU-Net 产生极大分歧，则转向"插入假象"分析。

## 5. 关键洞察

抑制率是一条**心理测量学曲线**，而非 mIoU 脚注。排名顺序的迁移是科学门禁；绝对 P 值 EXPECTED 取决于病灶插入模型。

## 6. 新颖性

特定产品已有读者研究。类 sFRC 指标（UNSURE 2026 arXiv —— 待复核）针对幻觉。**空缺：** 公开的、基于检测器的**抑制曲线**，且在 LIDC 上附带**合成到真实的排名检验**，放弃了普适性主张。

信心：中等（Medium）。

## 7. 文献

见 `literature.md`。

## 8–10. 方法 / 架构图 / 数学形式

将已知尺寸／CNR 的病灶插入 Mayo 式 LDCT 或 LIDC 背景中（注意：LIDC 已有结节 —— 使用无结节切片或做减法）。施加 T_s。用冻结的 D 打分。

每个管线族的逻辑回归模型：

\[
\mathrm{logit}\, P(\mathrm{suppress}) = \beta_0 + \beta_{\mathrm{size}}\log \mathrm{size} + \beta_{\mathrm{CNR}}\mathrm{CNR} + \beta_s s
\]

用 AIC 比较逐家族拟合 vs 联合拟合（H3）。

## 11. 实现

`src/lesion_suppress/` 中的插入、指标、曲线拟合。原型在合成 2D 高斯上运行，无需临床数据。

## 12. 数据

LIDC-IDRI（真实结节，尺寸）。Mayo/AAPM LDCT（若可用）。在 CT H1 通过**之后**将 fastMRI 作为第二模态。killer 实验无需新的人类读者。

## 13. 基线

未处理；BM3D 家族；DnCNN 类；一种 SR（例如残差 CNN）。不主张 SOTA 去噪器。

## 14. 指标

病灶级敏感度；抑制率；对比真实的 Kendall τ；可选 CHO。

## 15–17.

见 `experiments.md`。Killer = H1 的 τ。

## 18. 预期（未经测量）

EXPECTED：微小低 CNR 病灶首先被抑制；在匹配的视觉平滑度下生成式 SR 弱于 BM3D；若插入合理，τ 为中等（约 0.4–0.8）。

## 19–20. 失效 / 负结果

若 τ ~ 0：插入模型是论文的混淆因素 —— 停止声称安全规范。若 CHO ≠ 检测器：测量无效。

## 21–22. R2

"合成病灶不是真的。" → H1 就是答案或死亡。
"没有新方法。" → 同意：这是一篇**规范／表征**论文；立足点在于影响力和安全性，而非架构新颖性。Stage 6 接受了这一点。

## 23. 算力

Killer 约 2 GPU-days（推理）。完整方案约 10。

## 24–28.

见 `roadmap.md`。立意：一份可以放进部署卡片中的测得的 P(suppress|·)。
