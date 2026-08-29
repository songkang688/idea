# Windows6 研究总结

## 实际执行的流水线

**FACT.** 原定阶梯是 `1000→200→50→20→5→3`。Windows6 没有按它执行。实际跑的是：

| 层级 | 标准 | Windows6 实际 |
|---|---|---|
| 原始池 | 1000+ | **1080 原始 / 1062 有效**（S 系列 600 + A–F 480） |
| → 200 | 200 | **约 142** 个打分存活者（78 个 ABCF + 64 个 DE，出自被评审的 480 条） |
| → 50 | 50 | *从未产生* |
| → 20 | 20 | *从未产生* |
| → 5 | 20 → 5 | 10 条 DE 裁决 ‖ 12 条 cheap-cluster 裁决 → **cheap-5** |
| → 3 | 5 → 3 | Reviewer #2 → **3 个存活** |

有两处偏差不能被含糊掩过：**不存在 200 档、不存在 50 档、也不存在真正的 20 档**，而且 **600 条 S 系列想法从未被 Stage-2 打分**——原始池的 55% 从未进入打分环节。第一波超时打断了漏斗，最后是通过一条狭窄的"cheap"通道草草收尾的。带逐条核验的完整偏差表：[`selection_history/stage5_top5.md`](selection_history/stage5_top5.md) §1。

## Final 3 —— **PROVISIONAL，尚未锁定**

裁决与锁定结论：[`selection_history/stage6_battle.md`](selection_history/stage6_battle.md)。有三道门禁尚未关闭——**GATE-A**（公开烟雾数据集上的相机元数据未核实）、**GATE-B**（尚无一对 base/chat checkpoint 被核实为共享视觉编码器与坐标 tokenization）、**GATE-C**（存活者从未与被搁置的扩展项 `D-008`/`D-060`/`E-025` 在同一尺度上排名）。**GATE-D**（状态一致性 + package 深度）已由 W6-T3 关闭。

这三个是（见 `Idea_01`–`Idea_03`）：

1. SAM AMG 作为强度聚类（机制性）
2. 烟雾／火焰数据的相机 ID 泄漏量化
3. VLM 定位能力上的对齐税（已变异，格式控制 + 探针）

Reviewer #2 之后被杀掉的：空切片 FPR–Dice"无相关性"审计；atlas 质心 vs CLIP 文本替换。

各 package 中的所有定量主张，除另有标注外均为 **EXPECTED/HYPOTHESIS**。原型都是合成的。**整轮的 ACTUAL RESULT 计数：零。** W6-T3 把三个 package 加厚到可执行深度，并让每个 `src/` 都能配合 smoke tests 跑起来；它没有产出任何测量结果，而且每个脚本在打印数字之前都会先输出一条"合成输出"的横幅提示。
