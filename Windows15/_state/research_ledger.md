# Windows15 Research Ledger

- **windows_id:** Windows15
- **created_at:** 2026-08-28T17:50:30Z
- **repository:** https://github.com/songkang688/idea
- **branch:** `cursor/windows15-p0-init-implementation-4708`
- **current_stage:** Stage 1
- **status:** initialized
- **total_ideas:** 0
- **survivors:** 0
- **final_target:** 3
- **pipeline:** `1000+ -> 200 -> 50 -> 20 -> 5 -> 3`

## 本轮研究范围

Vision Foundation Models、多模态 / 视觉-语言大模型、大模型微调与 PEFT（LoRA / Adapter）、SAM 系列及其微调与适配、图像分割（含医学、烟雾/火、透明或歧义目标）、目标检测。第二优先级包括医学 VFM、域适应、少/零样本分割、Prompt Learning、弱/半/自监督、合成数据、表征学习、稠密预测 VLM、鲁棒性/校准/不确定性、跨域迁移。允许扩展到超分、修复、扩散/生成、LLM，但禁止为迎合方向制造伪创新。

本轮只写入 `Windows15/`，不得覆盖或改写其他 Windows。

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

## 科研价值观

**优先寻找：** 新 observation；新 scientific question；新 falsifiable hypothesis；新 failure mode；新 empirical phenomenon；被忽略的 assumption；counter-intuitive result；foundation model 的系统性缺陷；评价协议或数据集揭示的新问题；简单但能挑战社区共识的实验。

**主动降权：** Module A + Module B；Transformer + CNN；单纯增加 attention；单纯换 loss / backbone；单纯把已有方法搬到医学或烟雾数据；仅通过更多参数/数据/计算获得提升；没有 scientific hypothesis 的 architecture engineering；novelty 只存在于措辞中的 Idea。

**始终追问：**

1. 社区目前默认什么是真的？
2. 为什么这个假设可能是错的？
3. 什么实验可以最快把它证伪？

## Evidence Rules

始终严格区分：KNOWN FACT / VERIFIED PRIOR WORK / EVIDENCE / HYPOTHESIS / MODEL SPECULATION / EXPECTED RESULT / ACTUAL EXPERIMENTAL RESULT。

绝对禁止虚构：paper / citation、benchmark number、dataset information、已运行的实验、实验结果、Git / Push 成功状态。

没有实际运行实验，就绝对不能写成 ACTUAL EXPERIMENTAL RESULT。涉及 novelty 的结论必须优先验证。子 Agent 结论不是事实。

## 编号决策（canonical，P0 锁定）

| 项 | 标签 | 内容 |
|----|------|------|
| 工作区顶层 | KNOWN FACT | 分支基点 `origin/main` @ `1cf3304`：`README.md`、`Windows1/`、`research_ledger/`；无 Windows15 |
| 远程已有 | KNOWN FACT | Windows1(main)、2、4、6、8、9、10、11、12、13(locked)、14(locked)、16(locked)；Windows3 仅嵌套 `staging/Windows3_supervisor/` |
| max N | KNOWN FACT | 16（本 Agent 自扫 74 origin refs @ 2026-08-28T17:48:58Z） |
| Windows15 是否存在 | KNOWN FACT | 否——任意大小写/嵌套路径、分支名、window.lock.json 声明、research_state windows_id 声明均无 |
| 本轮编号 | DECISION | Windows15 |
| 决策来源 | KNOWN FACT | `_dispatcher/p0/wave_b/decision.json`（Wave B Consolidator，3/3 judge 一致；父 dispatcher 身份 Windows15） |
| 原因 | — | 15 为本 pipeline 预留编号；姊妹 pipelines 已取 13/14/16 并把 15 记为 never_take/本 pipeline 所有；两阶段锁定复扫（mkdir 前 + 写锁前）均确认 15 缺席；创建不会覆盖任何历史研究 |
| 永不复用 | KNOWN FACT | 1、5、7（never gap-fill）；13、14 永不夺取；所有已占用编号不复用 |

`ideas_master.jsonl` 每行 schema（后续 Stage 追加，初始化时保持 0 字节、无表头）：`{idea_id, title, cluster, stage, status: keep|kill|mutate|revive, score, evidence_label, source_agent, created_at}`

## 当前 Stage

Stage 1 目录与状态文件已初始化。`ideas_master.jsonl` 为空（0 字节）。尚无 Keep / Kill / Mutate / Revive 的 Idea 决策。

## 下一阶段要做什么

运行 **P1**：Stage 1 大规模独立 Idea 生成与检索（独立检索、失败模式、可证伪假说），逐步推进 `1000+ -> 200 -> 50 -> 20 -> 5 -> 3`。重要判断必须独立验证或对抗。不得把初始化文档写成已完成研究。
