# Idea_01 —— Objectness, Not Features

**本轮 Windows 的 #1 推荐。**

状态：HYPOTHESIS 级别的研究 package。没有任何真实实验结果。

## 摘要

**一句话：** SAM 系列在烟雾、火焰、玻璃以及浸润性病灶上的失败，是由 **objectness 解码器／提示先验（decoder/prompt prior）** 造成的，而不是因为编码器缺少特征——因此在冻结编码器上加一个线性／密度头，再配合排除区（exclusion-region）提示，应当能在无定形目标上胜过带提示的 SAM，同时在 COCO 物体上落败。

如果这是错的，那就说明编码器确实缺少这些特征（与"纹理可分性"那一派解释一致），我们就在一个 GPU-day 内 **kill** 掉这个项目。

## 研究动机

KNOWN FACT：SAM（Kirillov et al., ICCV 2023）和 SAM 2（Ravi et al., 2024）是被训练成"从点／框输出实例掩码"的。EVIDENCE：它们在依赖上下文的、低对比度的概念上表现不佳（arXiv:2412.01240；arXiv:2412.04243），而火焰通常要靠紧致框（tight boxes）才能救回来（arXiv:2510.21782）。

社区的默认判断（论文里属于 MODEL SPECULATION，却被当成事实）是："需要对编码器做医学／火焰领域适配。" Med-SA、SAMed、LoRA-MedSAM 都把参数花在编码器／adapter 上。

**为什么这可能不成立：** 类物体（object-like）目标共享一个拓扑先验（闭合边界、内部 vs 外部），而烟雾／浸润性肿瘤／玻璃并不具备这个先验。这个先验完全可以只存在于 **prompt + mask decoder** 里。编码器 embedding 也许本身就已经是线性可用的信息。

## 问题定义

设 \(x\) 为图像，\(z = E(x)\) 为冻结的 SAM 图像 embedding，\(p\) 为提示，\(D\) 为 SAM mask decoder。

- **Object-like** 目标：COCO 的 things。
- **Amorphous**（无定形）目标：烟雾、火焰羽流、透明物体、浸润性肿瘤。

**问题：** \(D(\cdot, p)\) 是否销毁了在 \(z\) 中仍然存在的信息？

## 核心假设（可证伪）

**H1：** 在冻结的 \(z\) 上用密度／BCE 损失训练一个线性或 1×1 卷积头，训练数据为 200–2000 张无定形图像，其 **NSD 更高**（而不只是 Dice 更高）——高于在同一批图像上用 GT 框提示的官方 SAM/SAM2。

**H2：** 同一个冻结头在 COCO val 的物体子集上**比**带提示的 SAM **更差**（说明我们并没有训出一个通用意义上更好的分割器）。

**H3：** 排除区提示（一个负向环带／"not-object" 掩码）能在**不做**编码器微调的情况下提升带提示 SAM 在无定形目标上的表现，而对 COCO 没有帮助。

若 H1 为假：编码器特征不足 → 停止把 Idea_01 当作一种方法；把这个负结果发表出来，作为对 2412.04243 那类"编码器能力上限"论述的支持。

## 关键洞察

科学对象是**失败发生在哪里**（编码器 vs objectness 接口），而不是一个新 backbone。

## 新颖性（精确界定）

| 最接近的工作 | 他们做了什么 | 确切差别 |
|---------------|---------------|------------------|
| 2412.01240 | 在 CD（context-dependent）概念上评测 SAM/SAM2 | 只是评测；没有冻结线性探针，也没有排除区干预 |
| 2412.04243 | 纹理 / tree-likeness 指标 | 是**竞争性机制解释**（纹理在 \(E\) 里）vs 我们的（objectness 在 \(D,p\) 里） |
| 2510.21782 | 用框提示做火焰分割 | 框仍然预设了物体范围；我们检验的是排除区／密度 |
| Med-SA / LoRA-MedSAM | 训练 adapter/LoRA 提升医学 Dice | 我们在 killer 实验中**禁止**更新编码器 |

剩余的新颖性信心：**中等**。一篇纯 probe 论文很容易被 desk-reject；真正构成论文的是那个**交互效应**（在无定形上赢、在 COCO 上输）。

## 提议方法

1. 从冻结的 SAM ViT-B/L 提取 \(z = E(x)\)（并把 SAM2 Hiera-B+ 作为必需的泛化性验证）。
2. **密度头** \(h_\theta(z) \in [0,1]^{H' \times W'}\)，双线性上采样。
3. 可选的**排除提示**：在一个宽松框（loose box）之外栅格化出一条负向带；对带提示的 baseline 作为 mask prompt 喂给 \(D\)，对 \(h_\theta\) 则作为额外通道输入。
4. 只训练 \(\theta\)。

### 数据流

图像 → 冻结编码器 → \(z\) → \(h_\theta\) → 上采样 → 密度图 → 为二值指标做阈值化（同时也报告连续排序指标）。

## 数学形式

\[
\mathcal{L} = \lambda_{\mathrm{bce}} \mathrm{BCE}(\hat{y}, y) + \lambda_{\mathrm{dice}} \mathrm{Dice}(\hat{y}, y) + \lambda_{\mathrm{tv}} \mathrm{TV}(\hat{y})
\]

对烟雾而言，\(y\) 可以是软标签（多标注者的标注频率）。**HYPOTHESIS：** 在密度上加 TV 优于 CRF 式后处理。

不要在计算损失之前做阈值化。

## Killer 实验（Day 1）

在一个公开烟雾或火焰数据集上**并且**在一个 100 张图的 COCO 子集上：

| 条件 | 可训练部分 | 提示 |
|-----------|-----------|--------|
| A 带 GT 框提示的 SAM | 无 | GT box |
| B 冻结编码器 + 线性／密度头 | 仅 \(h_\theta\) | 无 |
| C B + 排除通道 | \(h_\theta\) | loose box + 负向环带 |

**继续（Continue）：** 若在无定形数据上 NSD(B 或 C) > NSD(A) **且** 在 COCO 上 NSD(B) < NSD(A)。  
**转向（Pivot）：** 若在所有场景下 B≈A（方法不再有趣；也许可以改成一篇校准论文）。  
**杀掉（Kill）：** 若在无定形数据上 B << A（编码器才是瓶颈；不要在没有新科学的前提下加 adapter 去"修"它）。

## 预期结果（HYPOTHESIS，未经测量）

- 无定形 NSD：C ≥ B > A
- COCO：A > B
- Dice 的差距小于 NSD 的差距

## 停止／继续

见 `roadmap.md`。
