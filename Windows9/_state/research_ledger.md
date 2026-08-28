# Windows9 Research Ledger

- **windows_id:** Windows9
- **created_at:** 2026-08-28T16:49:21Z
- **current_stage:** Stage 1
- **status:** initialized
- **evidence_class of this file's historical claims:** VERIFIED PRIOR WORK for remote Windows dirs listed below; KNOWN FACT for this worktree init.

## 本轮研究范围

Ming 仓库 `songkang688/idea` 的独立研究窗口。只新增 `Windows9/`。禁止覆盖 Windows2/3/4/6/8 及其他历史产物。

编号决策（KNOWN FACT from `git ls-remote` + `git ls-tree`）:

| ID | 位置 | 状态 |
|----|------|------|
| Windows2 | 远程分支 `cursor/research-idea-evolution-windows2-c2c9` 等 | 存在，未检出到本工作区 |
| Windows3 | 远程 `staging/Windows3_supervisor` | 存在，未覆盖 |
| Windows4 | 远程 `cursor/windows4-research-idea-evolution-2962` | 存在，未覆盖 |
| Windows6 | 远程 `cursor/windows6-research-idea-evolution-b55d` | 存在，未覆盖 |
| Windows8 | 远程 `cursor/windows8-research-idea-evolution-cd91` | 存在，未覆盖 |
| Windows1/5/7/9 | 远程 heads 扫描 | 本工作区创建前无 Windows9 |

**决策:** max N = 8 → 本轮 `Windows9`。Keep 该编号，后续阶段不得切换。

## 研究优先级

第一优先级：VFM；Multimodal / VLM；大模型微调；PEFT / LoRA / Adapter；SAM 系列；Image / Medical / Smoke-Fire / Transparent-Ambiguous Segmentation；Object Detection。

第二优先级：Medical VFM；DA；Few/Zero-shot Seg；Prompt Learning；Weak/Semi/Self-Supervised；Synthetic Data；Representation Learning；VLM Dense Prediction；Robustness / Calibration / Uncertainty；Cross-domain Transfer。

允许扩展：SR / Restoration / Diffusion / Multimodal Generation / LLM / Alignment / Agents。不得伪创新迎合。

## 科研价值观

优先：新 observation / scientific question / falsifiable hypothesis / failure mode / empirical phenomenon / 被忽略 assumption / counter-intuitive result / foundation model 系统性缺陷 / 评价协议问题 / 能挑战共识的简单实验。

降权：Module A+B、Transformer+CNN、加 attention、换 loss/backbone、把方法搬到医学或烟雾、堆参数数据算力、无假说的架构工程、措辞 novelty。

追问：社区默认什么为真？为何可能错？最快证伪实验是什么？

## Evidence Rules

严格区分：KNOWN FACT / VERIFIED PRIOR WORK / EVIDENCE / HYPOTHESIS / MODEL SPECULATION / EXPECTED RESULT / ACTUAL EXPERIMENTAL RESULT。

禁止虚构：paper、citation、benchmark、dataset 信息、未跑实验、实验结果、Git/Push 成功状态。

未实际跑实验，不得写 ACTUAL EXPERIMENTAL RESULT。

## Idea 登记字段（后续每条必须有）

Idea ID, Stage, Status, Cluster, Core Hypothesis, Scores, Closest Prior Work, Novelty Status, Reviewer Opinions, Major Risks, Unresolved Questions, Required Experiments, Survival / Elimination Reason, Current Ranking, Agent assignments.

当前 `ideas_master.jsonl` 为空。total_ideas = 0。尚无 Keep/Kill/Mutate/Revive。

## Keep / Kill / Mutate / Revive 日志

- 2026-08-28: **Keep Windows9 as this-round id.** Reason: remote max N=8; creating Windows9 does not overwrite existing trees. (KNOWN FACT)

## 当前 Stage

Stage 1 — 已完成 P0 工作区初始化。Idea 生成未开始。

## 下一阶段要做什么

**P1 — Stage 1 Massive Idea Exploration**

- 保持最多 3 个云端子代理并行，模型 `claude-fable-5-thinking-xhigh`。
- 优先降低最大不确定性：foundation model / SAM / PEFT / 分割评价协议的失败模式与可证伪假说。
- 独立验证 novelty；对抗 Supervisor 偏见。
- 在未达到 Stage 1 完成条件前不得停止。
