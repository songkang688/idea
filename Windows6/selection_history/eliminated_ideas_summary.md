# 被淘汰的想法（概览）

这不是 1000 个 ID 的全量转储。反复出现的杀掉理由：

- 模块堆叠 / 把 PEFT 用在医学上但没有机制
- 用提示抖动做 SAM 不确定性（SAM-U / UR-SAM / SAIF）
- LoRA 有效秩 ≪ r（Illusion of Equivalence 2024）
- 把直方图匹配当域适应（KiTS23, RHM）
- LN-affine vs LoRA 的测试时适配（2025–26 已经很拥挤）
- 把非单调点击当作发现（RITM, Stable-SAM）
- 把 Dice vs CE 的校准差异当作发现（TMI 2020）
- 空切片 FPR 与 Dice 排行榜（属于定义问题 + Metrics Reloaded）
- Atlas 与 CLIP 器官文本的替换（Universal Model ICCV 2023）

见 `stage3_prior_work_kill_cheap.jsonl`、`stage4_reviewer2_cheap5.jsonl`，以及 Stage 2 的各个 JSONL 文件。
