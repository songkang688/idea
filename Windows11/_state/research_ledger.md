# Windows11 Research Ledger

## Round identity

- **windows_id:** Windows11
- **windows_path:** `Windows11/`
- **repository:** https://github.com/songkang688/idea
- **branch:** `cursor/windows11-p0-init-c0c1`
- **created_at:** 2026-08-28T16:56:40Z
- **supervisor:** Windows11（用户指定；且扫描得到 max N=10，故本轮为 Windows11）

## 本轮研究范围

Vision / Multimodal foundation models、分割与检测、PEFT、SAM 适配，以及可迁移到医学/烟雾/透明或歧义目标的**科学问题**（不是把已有方法搬到新数据）。允许在证据支持下扩展到 restoration、generation、LLM，但不得为迎合优先级制造伪创新。

Pipeline: `1000+ -> 200 -> 50 -> 20 -> 5 -> 3`。最终目标 3 个 Research Packages。

## 研究优先级

### 第一优先级

- Vision Foundation Models
- Multimodal / Vision-Language Large Models
- 大模型微调
- Parameter-Efficient Fine-Tuning / LoRA / Adapter
- SAM / Segment Anything 系列及其微调、适配、改进
- Image Segmentation
- Medical Image Segmentation
- Smoke / Fire / Transparent or Ambiguous Object Segmentation
- Object Detection

### 第二优先级

- Medical Vision Foundation Models
- Domain Adaptation
- Few-shot / Zero-shot Segmentation
- Prompt Learning
- Weak / Semi / Self-Supervised Learning
- Synthetic Data
- Representation Learning
- Vision-Language Models for Dense Prediction
- Robustness / Calibration / Uncertainty
- Cross-domain Transfer

### 允许扩展（不得伪创新）

- Super Resolution / Image Restoration
- Diffusion Models / Image Generation / Multimodal Generation
- Large Language Models / Fine-tuning / Alignment / Agents

## 科研价值观

**优先寻找：** 新 observation；新 scientific question；新 falsifiable hypothesis；新 failure mode；新 empirical phenomenon；被忽略的 assumption；counter-intuitive result；foundation model 的系统性缺陷；评价协议或数据集揭示的新问题；简单但能挑战社区共识的实验。

**主动降权：** Module A + Module B；Transformer + CNN；单纯增加 attention；单纯换 loss / backbone；单纯把已有方法搬到医学或烟雾数据；仅靠更多参数/数据/计算；没有 scientific hypothesis 的 architecture engineering；novelty 只存在于措辞中的 Idea。

**始终追问：**

1. 社区目前默认什么是真的？
2. 为什么这个假设可能是错的？
3. 什么实验可以最快把它证伪？

## Evidence Rules

严格区分：KNOWN FACT / VERIFIED PRIOR WORK / EVIDENCE / HYPOTHESIS / MODEL SPECULATION / EXPECTED RESULT / ACTUAL EXPERIMENTAL RESULT。

绝对禁止虚构：paper / citation；benchmark number；dataset information；未运行的实验及其结果；Git / Push 成功状态。

没有实际运行实验，就不得写成 ACTUAL EXPERIMENTAL RESULT。涉及 novelty 的结论必须优先验证。子 Agent 结论不是事实。

## 编号扫描（P0）

| 类型 | 内容 |
|------|------|
| KNOWN FACT | 工作区 `main` 仅有根 `README.md`（`# fnyuan`）与 `.git`；无顶层 Windows 目录 |
| KNOWN FACT | `origin/main` = `990f3eb` Initial commit，与本地一致 |
| KNOWN FACT | 远程存在顶层目录 Windows2, Windows4, Windows6, Windows8, Windows9, Windows10 |
| KNOWN FACT | Windows3 出现在 PR #1 分支（staging 布局） |
| KNOWN FACT | 未发现 Windows1、Windows5、Windows7、Windows11 顶层目录 |
| KNOWN FACT | 观察到的编号集合 {2,3,4,6,8,9,10}；max N = 10 |
| DECISION | 创建 `Windows11/`，不覆盖任何已有 Windows |

未把 Windows1/5/7 的缺失当成“这些轮不存在于其他机器”；只记录本仓库 remote heads 上未见其顶层目录。

## 当前 Stage

**Stage 1**（目录初始化完成；`total_ideas = 0`）。status = `initialized`。

尚无 Idea 记录。`ideas_master.jsonl` 为空。无 Keep / Kill / Mutate / Revive 决策。

## 下一阶段（P1）

Stage 1 大规模 Idea 探索：独立检索、记录失败模式与可证伪假说、对抗式 novelty 检查。保持最多 3 个云端子 Agent 并行，模型 slug `claude-fable-5-thinking-xhigh`。

**P0 阻塞记录（不影响目录初始化）：** Task 工具拒绝该模型，错误为必须先 acknowledge Claude Fable 5 data retention policy。已通过 environment setup action 请求用户在 Dashboard 确认。确认前不得假装子 Agent 已运行。

## Idea record schema（jsonl，每行一条）

```text
idea_id, stage, status, cluster, core_hypothesis, scores,
closest_prior_work, novelty_status, reviewer_opinions, major_risks,
unresolved_questions, required_experiments, survival_elimination_reason,
current_ranking, agent_assignments, completed_tasks
```

P0 不写入任何 Idea 行。
