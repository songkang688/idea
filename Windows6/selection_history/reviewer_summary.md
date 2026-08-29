# Stage 3 —— Prior-work 刺客（廉价 killer 簇）

来源：[Stage3 prior-work kill cheap](bc-adbcd019-2528-5e6f-b9dc-8942aabc525b)。引用是通过网页检索得到的，不要当作穷尽的。

## Continue = 保留

- 在 CT 上 SAM AMG ≈ HU 聚类（novelty_conf 0.6）
- 烟雾／火焰上的相机 ID 泄漏导致指标虚高（0.55）

## Continue = 变异

- 空切片 FPR 与 Dice 排行榜的去相关（放弃那个门控方法）
- 把 VLM 对齐税做成阶段隔离的定位曲线
- Atlas 质心 vs CLIP 器官文本（机制：文本充当空间先验）

## Continue = 杀掉

- LN-affine ≈ LoRA；直方图匹配做域适应；LoRA 有效秩；提示抖动做不确定性量化；非单调点击；Dice vs CE 校准

完整 JSONL：`stage3_prior_work_kill_cheap.jsonl`
