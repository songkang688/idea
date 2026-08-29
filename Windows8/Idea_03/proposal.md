# Idea_03 —— Selective SAM via IoU-token Recalibration

状态：HYPOTHESIS。没有实测过任何可靠性图（reliability diagram）。

## 摘要

**一句话：** SAM/SAM2 的 IoU token 在类 SA-1B 的物体上是良好校准的，而在无定形／低对比度掩码上是**反校准（anti-calibrated）**的；因此"拒答选项 + isotonic 重校准"在 risk-coverage 意义下提升 Dice 的幅度，会大于 Med-SA 量级的 adapter。

## 动机

KNOWN FACT：SAM2 暴露了 `iou_predictions`。EVIDENCE：工程实践文档告诉使用者按约 0.5 做阈值。而论文里几乎从不在烟雾／Trans10K／医学数据上报告**可靠性图**。

## 假设

**H1：** 在 COCO 物体上，IoU token 与真实 IoU 之间的 Spearman ρ 为正，且 ECE 低于一个预先注册的界。

**H2：** 在无定形数据集上，ρ 会下降，甚至可能变为**负值**（反校准）：token 高，真实 IoU 低。

**H3：** 使用重校准后的分数做选择性预测（覆盖 80% 的像素／图像），在被覆盖部分的 Dice 上胜过参数量对齐的 adapter，并且对被拒的尾部保持诚实披露。

## 新颖性

这不是"用一下置信度分数"。主张在于 **IoU 头存在依赖领域的误校准**，而方法本身是一个**拒答选项（reject option）**，不是又一个 mask decoder。

最接近的工作：选择性分类（Geifman & El-Yaniv）；SAM2 API。差别：这里是稠密预测 + 已被证实的反校准现象。

## 方法

在一个 val 划分上用 isotonic regression 映射 IoU token \(s\)。若 \(\hat{\mathrm{IoU}} < \tau\) 则拒答。报告 risk-coverage 曲线。

可选：在冻结的 decoder 特征上训练一个 1×1 校准器（与 Idea_01 兼容）。

## Killer 实验

零训练：在 100 张 COCO 与 100 张 Trans10K／烟雾图像上，导出 SAM2 的 IoU token 与真实 GT IoU。绘制可靠性图。若在无定形数据上 ρ 仍然很高，则 **kill H2**。

## 预期

H1 成立、H2 成立，且在 80% 覆盖率下，通过弃答就能收回"SAM 在玻璃上很差"这一差距的大部分。

## Reviewer #2

"这只是平凡的阈值化。"让他闭嘴的做法：拿出反校准的证据（不只是 ECE>0）；给出覆盖率曲线；在额外参数量相同的条件下与 adapter 对比 risk-coverage。如果只是弱校准，就 kill 掉本 Idea，并把它并入 Idea_01 的分析图。
