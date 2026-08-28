# Windows10 Research Ledger

- **windows_id:** Windows10
- **created_at:** 2026-08-28T16:53:57Z
- **current_stage:** Stage 1
- **status:** initialized
- **evidence_class of numbering claims:** VERIFIED PRIOR WORK for remote Windows dirs listed below (from `git ls-remote` + `git ls-tree`); KNOWN FACT for this worktree init.

## 本轮研究范围

Ming 仓库 `songkang688/idea` 的独立研究窗口。只新增 `Windows10/`。禁止覆盖 Windows2/3/4/6/8/9 及其他历史产物。根目录 `README.md` 不修改。

编号决策:

| ID | 位置 | 状态 |
|----|------|------|
| Windows2 | 远程分支 `cursor/research-idea-evolution-windows2-c2c9` 等 | 存在，未检出到本工作区 |
| Windows3 | 远程 `staging/Windows3_supervisor` | 存在，未覆盖 |
| Windows4 | 远程 `cursor/windows4-research-idea-evolution-2962` | 存在，未覆盖 |
| Windows6 | 远程 `cursor/windows6-research-idea-evolution-b55d` | 存在，未覆盖 |
| Windows8 | 远程 `cursor/windows8-research-idea-evolution-cd91` | 存在，未覆盖 |
| Windows9 | 远程 `cursor/windows9-p0-init-3045` | 存在，未覆盖 |
| Windows1 / Windows5 / Windows7 | 远程 heads 扫描 | 未见顶层目录 |
| Windows10 | 本轮创建前 `origin` heads | 不存在 |

**决策:** max N = 9 → 本轮 `Windows10`。Keep 该编号，后续阶段不得切换。

## 研究优先级

第一优先级：Vision Foundation Models；Multimodal / Vision-Language Large Models；大模型微调；PEFT / LoRA / Adapter；SAM / Segment Anything 系列及其微调、适配、改进；Image Segmentation；Medical Image Segmentation；Smoke / Fire / Transparent or Ambiguous Object Segmentation；Object Detection。

第二优先级：Medical Vision Foundation Models；Domain Adaptation；Few-shot / Zero-shot Segmentation；Prompt Learning；Weak / Semi / Self-Supervised Learning；Synthetic Data；Representation Learning；Vision-Language Models for Dense Prediction；Robustness / Calibration / Uncertainty；Cross-domain Transfer。

允许扩展：Super Resolution；Image Restoration；Diffusion / Image Generation；Multimodal Generation；LLM；LLM Fine-tuning / Alignment / Agents。不得伪创新迎合。

## 科研价值观

优先：新 observation / scientific question / falsifiable hypothesis / failure mode / empirical phenomenon / 被忽略的 assumption / counter-intuitive result / foundation model 系统性缺陷 / 评价协议或数据集揭示的新问题 / 简单但能挑战社区共识的实验。

降权：Module A+B、Transformer+CNN、单纯增加 attention、单纯换 loss / backbone、单纯把已有方法搬到医学或烟雾数据、仅靠更多参数/数据/计算、没有 scientific hypothesis 的 architecture engineering、novelty 只存在于措辞中的 Idea。

始终追问：

1. 社区目前默认什么是真的？
2. 为什么这个假设可能是错的？
3. 什么实验可以最快把它证伪？

## Evidence Rules

始终严格区分：KNOWN FACT / VERIFIED PRIOR WORK / EVIDENCE / HYPOTHESIS / MODEL SPECULATION / EXPECTED RESULT / ACTUAL EXPERIMENTAL RESULT。

绝对禁止虚构：paper / citation、benchmark number、dataset information、已运行的实验、实验结果、Git / Push 成功状态。

没有实际运行实验，就绝对不能写成 ACTUAL EXPERIMENTAL RESULT。涉及 novelty 的结论必须优先验证。子 Agent 结论不是事实。

## Idea 登记字段（后续每条必须有）

Idea ID, Stage, Status, Cluster, Core Hypothesis, Scores, Closest Prior Work, Novelty Status, Reviewer Opinions, Major Risks, Unresolved Questions, Required Experiments, Survival / Elimination Reason, Current Ranking, Agent assignments / completed tasks。

当前 `ideas_master.jsonl` 为空。total_ideas = 0。尚无 Keep/Kill/Mutate/Revive Idea。

## Keep / Kill / Mutate / Revive 日志

- 2026-08-28: **Keep Windows10 as this-round id.** Reason: remote max N=9（含 Windows9）；创建 Windows10 不覆盖已有树。Evidence class: KNOWN FACT from remote scan. 无 Idea 可 Kill/Mutate/Revive。

## Git checkpoint

- pre_init HEAD: `990f3ebc75d7ab03a8960cf0d1e5621cbb29194a` on `main` (KNOWN FACT)
- init commit: `0255bd7f47ae66e6e161539782e12f4a49c299ae` (KNOWN FACT)
- push: verified_success — `git ls-remote` SHA equals local HEAD `0255bd7f47ae66e6e161539782e12f4a49c299ae` (KNOWN FACT)
- force_push: not used

## 当前 Stage

Stage 1 — 已完成 P0 工作区初始化。Idea 生成未开始。

## 下一阶段要做什么

**P1 — Stage 1 Massive Idea Exploration**

- 保持最多 3 个云端子代理并行，模型 `claude-fable-5-thinking-xhigh`。
- 优先降低最大不确定性：foundation model / SAM / PEFT / 分割评价协议的失败模式与可证伪假说。
- 独立验证 novelty；对抗 Supervisor 偏见。
- 当前阶段未满足 Completion Condition 时不得停止。
