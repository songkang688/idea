# Idea_02 —— Spectral Locality of Dense PEFT

状态：HYPOTHESIS。没有任何实测的 FFT 结果。

## 摘要

**一句话：** 用于分割任务、加在 SAM/ViT 编码器上的 LoRA（及相关 PEFT）本质上是一个**空间低通适配器**：增加 rank 买到的是大器官上的 Dice，而不是边界处的高频——因此在参数量对齐的条件下，一个极小的高频残差适配器在 NSD 上应当胜过更大 rank 的 LoRA。

## 动机

KNOWN FACT：LoRA（Hu et al., ICLR 2022）被 SAMed / LoRA-MedSAM 用在医学 SAM 上。EVIDENCE：那些论文报告的是 Dice／耗时，而不是对适配器特征差（adapter delta）做谱分解。

社区的默认假设：rank 更高 ≈ 容量更大 ≈ 分割更好。

## 问题

设 \(W\) 为一个冻结的权重，\(\Delta = BA\) 为 LoRA。在某个选定的特征图上定义 \(\delta(x) = f_{W+\Delta}(x) - f_W(x)\)。分析 \(\delta\) 的二维功率谱。

## 假设

**H1：** 对器官／病灶而言，\(\|\delta\|_2^2\) 中 \(\geq 80\%\) 的能量落在一个截止频率 \(k_c\) 以下，而该截止频率对于 1 像素级的边界来说过于粗糙（截止频率依 patch size 选定；\(k_c\) 需预先注册）。

**H2：** rank 64 与 rank 4 相比，并不会把能量搬到 \(k_c\) 之上（rank ≠ 频率）。

**H3：** 加一个 depthwise 的高通残差（DoG / Laplacian 卷积，仅几千参数），在相同参数预算下对 NSD 的提升大于提高 LoRA rank。Dice 可能没有变化。

## 新颖性

| 最接近的工作 | 差别 |
|---------|------------|
| LoRA-MedSAM / SAMed | 关注效率 + Dice，没有谱分析 |
| Med-SA | 关注 adapter 设计，不是频率诊断 |
| Fourier / FNet / 谱域 CNN 类论文 | 讨论的不是 SAM 上的 PEFT 特征差 |

确切差别：**研究对象是 \(\delta(x)\)，而不是一个新的 SOTA adapter**——除非 H3 成立。

## 方法

1. 在一个小规模器官数据集（Synapse/AMOS 子集）上微调 LoRA。
2. 在 64 张图像上缓存 \(\delta\)。
3. 计算径向功率谱；统计 \(<k_c\) 的能量占比。
4. 若 H1–H2 成立：训练 HighPassResidual（depthwise 3×3 Laplacian + 1×1），并与 LoRA rank 4、LoRA rank 64 对比。

\[\Delta W = BA, \quad y = W x + \alpha BA x + \gamma \mathrm{HP}(x)\]

## Killer 实验

一张 GPU：在 64 张图像上比较 LoRA-r4 vs LoRA-r64 vs r4+HP。同时报告 Dice **和** NSD **和**谱能量。若 H1 为假（LoRA 本来就是高通的）则停止。

## 预期（未经测量）

Dice：r64 ≈ r4+HP > r4。NSD：r4+HP > r64 ≥ r4。谱：r64 仍然是低通的。

## Reviewer #2

"低秩就意味着低频"在一般意义上是错的（rank 和空间频率是两回事）。论文必须给出这种经验性耦合的证据，并说明 HP 不只是"又加了一个卷积模块"。对照实验：若这套叙事真的关于频率，那么参数量相同的**低通**残差应当**损害** NSD。

## 算力

Killer 实验 < 1 GPU-day。完整的 Synapse/AMOS 需 3–5 天。
