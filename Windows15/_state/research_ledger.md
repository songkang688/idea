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

## Stage 1 — batch_001（P1 Wave A 生成 + Wave B 评审/合并，2026-08-28）

**输入（KNOWN FACT，分支 head 已记录于 decision.json）：**

- gen_A：T01 SAM / Foundation Model adaptation / PEFT，100 条（`origin/cursor/p1-wave-a-gen-a-f6f6` @ `5b770eb`）
- gen_B：T02 Medical segmentation，100 条（`origin/cursor/p1-wave-a-batch001-gen-b-9ddf` @ `5889021`）
- gen_C：T03 Smoke / fire / ambiguous segmentation，100 条（`origin/cursor/p1-wave-a-batch001-gen-c-65da` @ `046bd2c`）
- judge_A（聚类/合并）：keep 275 / merge 21 / drop 4（`origin/cursor/p1-wave-b-batch001-judge-a-1cf8`）
- judge_B（permutation/可证伪性）：keep 294 / mutate 6 / drop 0（`origin/cursor/p1-wave-b-batch001-judge-b-5493`）
- judge_C（对抗性查重）：keep 284 / duplicate_of 16 / drop 0（`origin/cursor/p1-wave-b-batch001-judge-c-4e6d`）

**Consolidator 冲突解决规则（完整定义见 `tasks/p1/batch_001/decision.json` R1–R7）：**

1. 查重取并集（judge_A merge ∪ judge_C duplicate_of）：重复关系可由语料内两段文本直接验证（consolidator 抽查 12 对，含全部单评委跨 shard 案例，逐对核对原文），且合并无损——被并入者记录在锚点的 `absorbed_duplicates`。两评委同时标记的 8 条目标全部一致。
2. 质量性 drop 需 ≥2/3 多数：本批 4 条 drop 均为 judge_A 单票，且其理由依赖未经引文核实的先验工作判断（judge_A 自标 advisory）。按证据政策"子 Agent 结论不是事实"，2:1 多数保留，打 `stage2_priorart_check_required` 标记。
3. judge_B 的 6 条 mutate（均 falsifiable=true）接受入库但带 `mutation_required=true` + salvage 说明，Stage 2 晋级前必须改写。

**结果（KNOWN FACT）：** 300 生成 → **271 accepted**（gen_A 93 / gen_B 89 / gen_C 89），29 条并入锚点，0 条质量性删除。`ideas_master.jsonl` 从 0 字节追加至 271 行。未虚构任何引文、基准数或实验结果；全部 idea 均为 HYPOTHESIS 等级。

**产物：** `tasks/p1/batch_001/decision.json`、`accepted.jsonl`、`consolidator/report.md`、`consolidator/next_task_queue.json`、`consolidator/done.json`；gen/judge 原始产物已并入本分支存档。

**下一步：** accepted=271 < 1000 → 继续 batch_002 生成（T04 Object detection / T05 VLM-dense prediction / T06 failure mining）。271 已越过 100–200 的 Diversity Audit 触发窗口（单批产出即超窗），按字面规则本轮不排 audit，但已在 next_task_queue.json 中建议父代理在 batch_002 dedup 时执行 checkpoint_1。

## Stage 1 — Diversity Audit 1（P1 多样性审计合并，2026-08-28）

**输入（KNOWN FACT，head 已记录于 `tasks/p1/diversity_audit_1/decision.json`）：** 对 271 条 accepted（@ `b8d60bc`）的三路独立审计——auditor_A（模式坍缩/簇拥挤，`fc9c24f`）、auditor_B（SAM+X/LoRA+X permutation 伪创新，`829c476`）、auditor_C（反直觉/立场方向/schema 强迫/盲区，`e106a3b`）。三分支路径互斥，git 合并无冲突；语义冲突按 decision.json 的 DR1–DR9 规则裁决。

**canonical 结论（EVIDENCE 级启发式统计，非 KNOWN FACT）：**

1. 无簇级模式坍缩（40 簇、有效簇数 32.1、Gini 0.275）；但约 39–40% 的语料共享同一 deflationary 骨架（"被信任的信号 X 其实是 artifact Y"），三个 generator 均匀出现 → 管线/schema 性质，根因是强制的 `community_default_belief` + `why_that_may_be_wrong` 字段（300/300 填写、0 条肯定默认信念）。
2. permutation 伪创新占比低：tier1 仅 6/271（2.2%），且全部已在 batch_001 带 `mutation_required` 入库，生成期可证伪性闸门有效。
3. 立场方向严重失衡：deflation:rehabilitation ≈ 25:1；anti-pessimism ~1.5%、null/equivalence 2.6%、affirmative 0%、对批判工具的元批判 0%。
4. 共识盲区：视频/时序（烟雾域之外）、交互式分割/人因、安全/对抗/记忆化/数据谱系、理论/形式极限、scale 作为实验变量、test-time compute、效率/scaling law、公平性、跨域合成（60% 单 shard 簇）。

**裁决（decision.json）：** 删除需 3/3 审计一致要求，实际 0/3 → **271 条全部保留，`ideas_master.jsonl` 未改动**。审计旗标取并集记录于 decision.json（不改写 canonical master）：batch_001 的 6 条 mutation_required 与 4 条 stage2_priorart_check_required 延续；auditor_B 新增 5 条 tier1.5（Stage 2 前须把诊断升为主张）与 6 条 permutation 观察名单；auditor_C 的 15 条 singleton 反直觉 idea 受保护（Stage 2 不得仅按簇规模裁掉）。

**领地命名冲突（DR1）：** auditor_C 自拟的 advisory T07–T16 命名被否决——锁定 registry（state_reader queue v1，父代理复确认）的 T07 benchmark/dataset weaknesses、T08 uncertainty/calibration、T09 synthetic data、T10 domain shift、T11 negative results、T12 contrarian hypotheses、T13 SR/restoration、T14 diffusion/generation、T15 LLM/agent、T16 cross-field transfer 为 canonical；auditor_C 的十项 charter 作为内容映射入 canonical 领地与 batch_006 两个 second-pass shard。

**生成合同 v2（batch_003 起生效，batch_002 judge 需执行骨架冻结）：** 每 100 条 shard 配额——deflationary ≤25、constructive ≥20、rehabilitation ≥10、quant-law ≥10、null/equivalence ≥5、affirm-default-with-boundary ≥3（anti-debunk 合计 ≥18：必须有 idea 肯定社区默认并画出成立边界、或提出 null/等价结论、或为被报道的失败翻案）；`claim_direction` 枚举强制、belief 字段改为可选+出处标注、新增 `who_would_disagree`；单一 claim 骨架每 shard ≤5 条；负控制与机制签名必填；HC-23/HC-36/HC-02/HC-30 与 metric-reranking 骨架冻结（仅收竞争机制或跨实例定量律）。

**产物：** `tasks/p1/diversity_audit_1/decision.json`（canonical 裁决）、`next_task_queue.json`（queue v3：batch_003 T07/T08/T09 ready；batch_004 T10/T11/T12；batch_005 T13/T14/T15；batch_006 T16 + 视频/交互与安全/理论两个补洞 shard）、`consolidator/report.md`、`consolidator/done.json`。

**下一步：** 派发 batch_003 三个 generator（`p1_wave_a_batch003_gen_A/B/C`）。目标推算：batch_002 合并后约 510–535 条，batch_005 dedup 期间预计越过 1000；checkpoint_2（500 条时触发）负责核查合同 v2 是否真正改变了立场分布。

## Stage 1 — Batch 002 合并（P1 Wave B Consolidator，2026-08-28）

**git 基线（KNOWN FACT）：** 从 `origin/cursor/p1-wave-b-batch001-consolidator-7c96`（`b8d60bc`，ideas_master 271 行）出发，fast-forward 合并 `origin/cursor/p1-diversity-audit-1-consolidator-ea44`（`0fad002`，为前者直接后代，无冲突；audit 未改动 ideas_master），再从六个 shard 分支按路径检出 batch_002 产物（各分支只触及自身 shard 目录，机械无冲突）。分支 head 全部记录于 `tasks/p1/batch_002/decision.json`。

**输入（KNOWN FACT）：** 300 条新想法（gen_A T04 Object detection / gen_B T05 VLM-dense / gen_C T06 failure mining，各 100）；judge_A（聚类+查重）keep 278 / merge 16 / drop 6（其中 5 为对 master 的重复、1 为 prior-art 风险）；judge_B（permutation/可行性）keep 286 / mutate 12 / drop 2；judge_C（对抗性查重）keep 280 / duplicate_of 20 / drop 0。

**裁决规则（decision.json R1–R8）：** 沿用 batch_001 的 R1–R7（查重取并集、链式跟随至存活锚点、质量性 drop 需 ≥2/3 多数、mutate 直通带标记、查重优先于 mutate/drop、不虚构证据）；新增 **R8 方向冲突规则**：当 A、C 两评委认定同一对为重复但幸存者相反（X→Y vs Y→X）时，以专职查重评委 judge_C 的幸存者为准（三对冲突其 confidence 均为 high）：(B-017,B-087)→B-017 存活、(B-085,C-046)→C-046 存活、(C-053,C-092)→C-053 存活；judge_A 指向被淘汰者的边按 R3 链式改写（B-022→B-087→B-017；B-030→B-024→C-045，双评委路径全部收敛）。

**结果（KNOWN FACT）：** 300 生成 → **272 accepted**，28 条并入锚点（23 条批内、5 条并入 batch_001 master 锚点：B-072→W15-B001-B-076、B-083→W15-B001-A-016、C-001→W15-B001-A-003、C-064→W15-B001-C-033、C-070→W15-B001-A-005），0 条质量性删除（3 张 drop 票均为单票——judge_A: C-038，judge_B: A-012/B-079——2:1 保留并打 `stage2_priorart_check_required`）；11 条带 `mutation_required`（judge_B 12 条 mutate 中 B-083 被查重吸收，R6 优先）；一致 keep 255 条。`ideas_master.jsonl` 从 271 行追加至 **543 行**（本次对 batch_001 旧行只追加不改写，5 条 master 吸收关系记录于 decision.json）。未虚构任何引文、基准数或实验结果；全部新想法均为 HYPOTHESIS 等级。

**advisory 延续：** judge_A 的 38 条 master 近重复观察名单与 9 条 prior-art 风险旗标、4 对内部矛盾（各需一个裁决实验矩阵）、judge_C 的 45 个近重复家族与 12 对受保护竞争假设——全部作为 Stage-2 审查指针记录于 accepted.jsonl consolidation 块与 judge 原始产物，不作删除依据。

**产物：** `tasks/p1/batch_002/decision.json`、`accepted.jsonl`、`consolidator/report.md`、`consolidator/done.json`；gen/judge 原始产物已并入本分支存档；`research_state.json` 更新（total 600 / survivors 543 / batches[2]）。

**下一步：** accepted=543 < 1000 → 继续 generator。按 diversity_audit_1 的 queue v3 派发 batch_003 三个 generator（`p1_wave_a_batch003_gen_A/B/C`，T07 benchmark weaknesses / T08 uncertainty-calibration / T09 synthetic data），生成合同 v2（立场配额+骨架冻结）自 batch_003 起强制执行；checkpoint_2 已到触发线（543 > 500），建议父代理在 batch_003 dedup 时执行。
