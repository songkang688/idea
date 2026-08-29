# Idea_01 —— RetainSAM

**候选标题**

1. RetainSAM: Fine-Tuning SAM under a Promptability-Retention Constraint
2. Dominating the WiSE-FT Front: Constrained Adaptation of Promptable Segmenters
3. Keep the Clicks: Domain Adaptation of SAM without Destroying Interactivity

## 1. 摘要

在**目标稠密预测领域**上微调 SAM（或 SAM2 图像编码器 + 提示解码器），同时**显式约束通用可提示性**（在留出的自然图像上的点击／框）。科学主张不是"又一个 adapter"。它是：**在微调期间对提示行为指标施加约束，可以严格支配基础 checkpoint 与简单微调 checkpoint 之间由 WiSE-FT 权重插值所描绘出的 Pareto 前沿**。

若权重插值本就已经描绘了该前沿，则该*方法*死亡；该*评测协议*仍可作为负结果／基准注记发布。

## 2. 动机

KNOWN：SAM 被用作基础权重文件，随后在医学或伪装目标数据集上做全量微调。社区默认做法：目标域 Dice 是唯一目标；SA-1B/COCO 上的交互性被假定为要么已保持、要么无关紧要。

HYPOTHESIS：无约束微调静默地将 SAM 转化为了一个小模型专才，而论文依然称其结果为"SAM"。HQ-SAM 风格的表格已经暗示了在某些 PEFT 放置方式下 COCO AP 的下降（来自 prior-work agent 的 EVIDENCE：HQ-SAM 的权衡表）。WiSE-FT（Wortsman et al., 2022）是遍历该权衡的简单方式。还没有人（截至文献核验 NOT FOUND）将可提示性视为一项**约束**，并附带针对插值的 **kill 测试**。

## 3. 问题定义

设 θ₀ 为官方 SAM 权重。设 D_tgt 为有标签的目标分割数据集。设 D_gen 为冻结的通用可提示性测试套件（图像 + 点击／框协议，**无梯度**）。

寻找在以下目标上达到 Pareto 最优的 θ：

- J_tgt(θ) = D_tgt 验证集上的 Dice/mIoU
- J_gen(θ) = 协议向量：{1-click mIoU, 3-click mIoU, box mIoU, NoC@90}

**约束形式（训练）：** 最小化 L_tgt(θ; D_tgt) + λ L_ret(θ; D_gen^replay)

其中 L_ret 是可微代理损失（在采样提示下相对于 SAM-θ₀ 伪标签的掩码 CE/Dice），而非评测协议本身。

**成功不是 D_tgt 上的一个数字。** 成功是对插值曲线 θ(α)=(1−α)θ₀+α θ_naive 的严格支配。

## 4. 核心假设（可证伪）

**H1：** 存在若干工作点，在 ≥2 个点上，约束微调在匹配的 J_gen 下取得比 WiSE-FT 更高的 J_tgt，**且**在匹配的 J_tgt 下取得更高的 J_gen。

**H2：** 在匹配的 D_tgt 训练预算下，简单全量微调违反了预先注册的 ε（例如在 COCO val 上 3-click mIoU 下降 > 2 点），而约束微调没有。

若插值折线未被严格支配，则 **Kill H1**。

若简单微调本就保持在 ε 之内，则 **Kill H2** —— 该问题对于该领域并不存在（在 kill 项目前尝试更远的领域）。

## 5. 关键洞察

可提示性是一种**行为**，而非单一精度。插值混合权重得到标量融合；它无法优先保护**点击到掩码的几何关系**，同时允许**解码器类别先验**发生改变。对提示采样掩码施加 replay 约束能正中该子空间。

这是关于参数空间几何特性的 HYPOTHESIS，而非既成事实。

## 6. 新颖性（确切差别）

| 邻近工作 | 他们做了什么 | 我们做什么 |
|---|---|---|
| HQ-SAM | 额外解码器 token 用于边界；报告部分 COCO 权衡 | 约束 + **必须胜过插值** |
| MedSAM | 在医学数据上微调 SAM；关注目标 Dice | 双重评测；保留通用点击能力 |
| WiSE-FT | 插值零样本与微调 CLIP | 同样的基线**作为 kill 开关**，而非作为我们的方法 |
| LoRA / adapters | 更少参数，隐式正则化 | 显式 J_gen 约束；在匹配参数量下对比 |
| 持续学习 / EWC | 保护旧任务 Fisher 信息 | 旧任务是**可提示分割**，通过点击协议而非 ImageNet 测量 |

剩余新颖性**以胜过 WiSE-FT 为前提**。信心：中等（Medium）。

## 7. 文献

见 `literature.md`。仅引用我们视为 KNOWN 的论文。

## 8–10. 方法、架构图、数学形式

见 `diagrams/architecture.md` 以及下方数学形式。

### 训练

1. 采样目标批次（图像，GT 掩码）。可选：从 GT 采样点／框以保持在 SAM 提示接口内。
2. 从 COCO train（或有许可的 SA-1B 子集）采样 replay 图像。从冻结的 θ₀（无梯度）生成提示（随机内部点击、带噪框）与**教师**掩码。
3. 学生模型 θ 同时预测目标掩码与 replay 掩码。
4. 损失函数：

\[
\mathcal{L} = \mathcal{L}_{\mathrm{DiceCE}}(p_{\mathrm{tgt}}, y_{\mathrm{tgt}}) + \lambda \, \mathcal{L}_{\mathrm{DiceCE}}(p_{\mathrm{replay}}, y_{\theta_0}) + \gamma \|\theta_{\mathrm{enc}} - \theta_{0,\mathrm{enc}}\|_2^2
\]

可选拉格朗日方式：当 J_gen 的低成本滑动估计值跌破 ε 时增大 λ。

### WiSE-FT 基线

\[
\theta(\alpha)=(1-\alpha)\theta_0 + \alpha \theta_{\mathrm{naive}}, \quad \alpha\in[0,1]
\]

在 11 个 α 点上评测双轴。约束运行必须实现支配。

## 11. 实现

`src/` 中的可运行原型（插值、损失、提示采样、评测钩子）。完整 SAM 训练需要官方 `segment-anything` checkpoint（未打包在仓库中）。

## 12. 数据

- 目标域（killer 选一个）：Kvasir-SEG 或 ISIC 2018 或 COD10K。
- 通用套件：COCO 2017 val（things）、LVIS 稀有类别子集、可选 ADE20K stuff（预期更难）。
- **不要**在 COCO val 上训练。

## 13. 基线

Zero-shot SAM；仅微调解码器；编码器 LoRA；全量微调；WiSE-FT；可选编码器 EWC。

## 14. 指标

目标域：Dice、NSD/Boundary IoU。通用套件：1/3/5 次点击下的 mIoU（误差中心模拟**与**随机内部点击 —— RClicks 证明了模拟存在偏差；我们两者都报）。框 mIoU。NoC@90。相对于 θ₀ 的保留 Δ。

## 15–17. 实验矩阵 / 消融 / Killer

见 `experiments.md`。

## 18. 预期结果（未经测量）

EXPECTED：简单微调在医学数据上比零样本提升 8–20 Dice，但损失数点 COCO 3-click mIoU。WiSE-FT 描绘出平滑前沿。约束微调 EXPECTED 位于前沿之上（若 replay 与插值互补）；若不互补则 EXPECTED 坍缩到前沿上。

## 19. 失效案例

编码器必须剧烈变动的远端医学领域；stuff 类别；微小物体；SAM2 视频记忆提示（超出 v1 范围）。

## 20. 负结果

若 WiSE-FT 表现持平：发布**可提示性保留套件**与负结果（"插值就足够了"）。那依然是一篇论文，但不是*这篇*方法论文。转向 Idea_03 作为 #1。

## 21–22. Reviewer #2 / 应答

攻击："HQ-SAM Table X 已经展示了权衡；WiSE-FT 已经能遍历它。"
应答实验：**支配图（domination plot）**。若无支配，他们是对的 —— 停止。

攻击："Replay 只是蒸馏，不是约束。"
应答：对比 λ=0 关蒸馏 vs λ>0 vs 插值；展示 replay ≠ 插值。

攻击："COCO 不是 SA-1B。"
应答：记录代理数据集性质；可用时可选 SA-1B 子集。

## 23. 算力

Killer：约 4–6 GPU-days（A100）。完整方案：约 20 GPU-days，3 个领域，先 ViT-B 后 ViT-H，3 个随机种子。

## 24. 路线图

见 `roadmap.md`。

## 25. 停止 / 继续

- **Kill 方法：** 在 2/2 个目标领域上均无 Pareto 支配。
- **转向（Pivot）：** 纯 replay 与约束等价 → 持续学习短文。
- **继续（Continue）：** 在医学 + 一个非医学（COD10K）上实现支配。

## 26. 扩展

SAM2 视频可提示性；MedSAM 权重作为 θ₀；逐层插值 vs 我们的约束。

## 27. 论文立意

"大家都在做插值。我们证明保护*点击行为*不等同于混合权重 —— 或者我们证明它们是一回事，并不再把无约束医学微调称为'SAM'。"

## 28. 标题

列于文首。
