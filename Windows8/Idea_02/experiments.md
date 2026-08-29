# Idea_02 实验设计

## Killer

在一个 toy 或类 Synapse 的子集上训练三种 PEFT 变体。分别保存冻结与适配后的编码器特征图。计算径向 FFT 能量。

## 消融

HP 卷积核：Laplacian vs Sobel vs 随机 3×3。预测：随机 3×3 ≈ 增加 LoRA rank（都没有 NSD 增益）。

## 负结果

若 r64 本来就是高通的：杀掉 HP 方法；不过这份审计本身也许仍可作为一篇 short note 发表。

## 指标

Dice、NSD、HD95、\(<k_c\) 的能量占比、参数量、训练耗时。
