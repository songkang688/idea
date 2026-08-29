# 漏斗偏差 —— 标准链路 vs Windows1 实际执行路径

状态：**事后审计。** 不重新打开任何选题决策，不修改 `Windows1/README.md` 或 `Windows1/research_summary.md` 中的任何结论。凡本审计发现与那两份文档存在冲突之处，均列在 §4 中供人工裁决并予以保留。

认知标签依据 `Windows1/README.md`：KNOWN FACT, EVIDENCE, HYPOTHESIS, MODEL SPECULATION,
EXPECTED RESULT, ACTUAL EXPERIMENTAL RESULT。

**本轮中不存在 ACTUAL EXPERIMENTAL RESULT。** `Windows1/research_summary.md` 写道
"We have **not** trained models or measured Dice/mIoU/τ in this round"；`README.md` 写道
"No numbers in this archive are measured by us."。本文件中的每个计数均为*想法或决策*的计数，
绝非测量值。每个计数均有来源。

---

## 1. 核心要点：链路真实存在但形态不符

标准链路为 **1000+ → 200 → 50 → 20 → 5 → 3**。
Windows1 实际执行了 **1065 → ~84 → ~20 → 12 → 8 → 5 → 3**。

由此引出两项结构性事实，均记录于此而非予以抹平：

- **Windows1 执行了七个级别，而非六个。** `research_summary.md` 将 Stage 5 标注为 "8 engineered, then 5" —— 这是在 Stage 5 *内部* 进行的 8 → 5 收缩。标准链路上无此步骤；其 Stage 5 *即为* 5。
- **漏斗中部在各个级别上比标准狭窄 2–4 倍。** Stage 2 保留了约 84 条（标准为 200 条）；Stage 3 保留了约 20 条（标准为 50 条）；Stage 4 保留了 12 条（标准为 20 条）。漏斗过早收窄，导致后续几乎没有可供裁减的余地。

**MODEL SPECULATION，如实标注：** 过早收窄与 §3 描述的 Stage-1 云端失败相吻合，后者导致实际*可评审*的池子小于原始生成的计数。总账中未陈述该因果链，因此不作为 EVIDENCE 断言。

---

## 2. 逐级对比

| 级别 | 标准 | Windows1 实际 | 实际计数的来源文件 | 可从仓库独立复现？ |
|---|---|---|---|---|
| Stage 1 原始 | 1000+ | **≥1065**（SEG 365 + 本地 VFM 350 + 本地 ASM 350 + VFM-A 180 + ASM-A 180，存在重合） | `research_summary.md`；`research_ledger/stage1_*` 中的池 | **部分可复现。** `350 + 350` 可通过统计两个本地池文件的 ID 完全核实。`365 + 180 + 180` 由摘要断言，其完整想法文本不在本仓库中。`365+350+350 = 1065` 精确复现了 "≥1065" 的底线。 |
| Stage 2 | 200 | **约 84 SEG 保留** + 未指定的 VFM/ASM 保留项 | `research_summary.md`；`research_ledger/stage2_seg_review.md` | **否。** 总账记录了 48 条命名决策 + 15 条提升项 = **59** 个保留侧单元。约 84 无法重构。见 §4-D。 |
| Stage 3 | 50 | **约 20 条被攻击** | `research_summary.md`；`research_ledger/stage3_priorwork_kill.md`, `stage3_vfm_kills.md` | **对 SEG 为是。** SEG 表恰好包含 5 KILL + 4 SURVIVE + 11 MUTATE = **20 个决策单元**，与"约 20"完全吻合。VFM 表另外增加了 13 个单元（4 KILL + 8 MUTATE + 1 WEAK SURVIVE），"约 20"似乎未将其计入。见 `stage3_survivors.md`。 |
| Stage 4 | 20 | **12 个变异形态**，无无条件 KEEP，1 个 KILL | `research_summary.md`；`research_ledger/stage4_reviewer2.md` + 找回的完整评审组记录 | **是。** 找回的评审组记录恰好包含 12 个提案 P1–P12，1 个 KILL（P10 = SEG-0193-M），其余皆为 KEEP-IF-EXPERIMENT。见 `stage4_candidates.md`。 |
| — *(额外级别)* | *无* | **8 个工程化** | `research_ledger/meta_audit.md` "Updated working Top-8" | **是。** Top-8 清单在 `meta_audit.md` 中枚举为 1–8。 |
| Stage 5 | 5 | **随后为 5** | `research_summary.md`；`research_ledger/stage5_killers.md` | **否。** 工程师的 Top-5 进行了枚举，但 supervisor 的修正重新加回了第 6 个，且记录从未陈述最终的五个。见 §4-E 与 `stage5_top5.md`。 |
| Stage 6 | 3 | **Final 3**（A RetainSAM, B LesionSuppress, D DisagreeShift） | `research_summary.md`, `README.md` | **结果为是，流程为否。** 三位胜出者明确无误。**从未写过 Stage-6 总账文件。** 回填为 `stage6_battle.md`。 |

### 关于胜出者代号字母的说明

`research_summary.md` 将 Final 3 标注为 "**A** RetainSAM, **B** LesionSuppress, **D** DisagreeShift" ——
A, B, D 无 C。字母是 Stage-6 候选名单标签，而非目录名；交付的目录分别为 `Idea_01`、`Idea_02`、`Idea_03`。
**没有任何关于 "C" 是什么或为何被去掉的记录。** 登记为 §4-F。

---

## 3. 记录在案的偏差原因

抄录自 `Windows1/selection_history/evolution_summary.md` 与 `Windows1/research_summary.md`。
这是该轮写下的*唯一*原因。

### 3a. 两次 Stage-1 云端超时（EVIDENCE，陈述了两次）

`evolution_summary.md`："自主 PI 带领 ≤3 个云端子 agent（`claude-fable-5-thinking-xhigh`）。
**两次 Stage-1 350 想法云端运行超时**；supervisor 编写了本地 VFM/ASM 池并重新派发了 180 想法批次。"

`research_summary.md` Stage 1 行："**云端 350 想法运行超时两次**；本地池 + 紧凑批次完成了 ≥1000 的要求。"

对漏斗的影响：≥1000 的要求是通过*替代*满足的，而非通过原定途径。本仓库中的两个本地 350 想法池在其标题中明确标有"supervisor backup"，而紧凑的 180 想法批次（VFM-A, ASM-A）仅以约 1 KB 的保留项摘要留存。因此五个 Stage-1 池中有三个在本仓库中没有可供评审的想法文本。

### 3b. Stage-2 评审员受阻后重启（EVIDENCE）

`evolution_summary.md`："**Stage-2 评审员最初受阻（云端工作区缺少想法文本）**，随后载入完整的 SEG 清单得以恢复。"

对漏斗的影响：实际完成的 Stage-2 评审**仅涵盖 SEG 切片**。`stage2_seg_review.md` 结尾附有 supervisor 自己的说明 "Global 1000 not yet complete: waiting VFM + ASM pools."。**总账中不存在针对 VFM 或 ASM 池的等价 Stage-2 评审表。** VFM/ASM 素材直接从 Stage-1 保留项摘要跳跃至 Stage-3 击杀表。这是漏斗中最大的单一结构性漏洞，也是 Stage 2 显示约 84 而非 200 的最可能原因。

### 3c. 廉价 killer 规则压缩了 Stage 4（EVIDENCE）

`stage4_reviewer2.md` 记录了四个提案："按廉价 killer 规则淘汰：0252（需要真实标注者生成）、0275（仅限随机词试点）、0240 析因设计、0103-M workshop。" 依据*证伪成本*而非科学价值进行筛选使该级别比标准链路预期收缩得更快，也是 Stage 4 产出 12 个而非 20 个的原因。

### 3d. 合并而非仅仅击杀（EVIDENCE）

若干级别是通过*合并*单元而非淘汰单元来实现收缩的，这使得标题计数变小而未伴随相应想法的损失：

- `meta_audit.md`："将 0275 与污染合并；将最坏情况点击与 oracle 点击泄漏合并"。
- `stage3_priorwork_kill.md` 将合并对作为单一单元承载：`0103/0125`。
- `meta_audit.md` Top-8 #7 与 #8 本身就是合并项（"最坏情况/oracle 点击交互式评测合并", "0275 + 评测污染合并（一个评测席位）"）。

---

## 4. 缺失的环节与内部不一致

每项均为*记录*层面的缺陷，并非断言决策错误。此处不单方面解决任何问题。

**A. 完全没有 Stage 6 记录。** `README.md` 断言 "Stage 6 locked method + medical-safety characterization + medical uncertainty method"，`reviewer_summary.md` 列出了三项 Stage-6 分歧，证明 Stage 6 确实发生过。总账中未有文件记录。事后回填为 `stage6_battle.md`，明确标为事后补记，依据 `README.md`、`reviewer_summary.md`、`evolution_summary.md`、`stage5_0276.md` 与 `meta_audit.md` 重建。

**B. VFM/ASM 池无 Stage-2 评审。** 见 §3b。两个本地池中的约 700 条想法有 Stage-1 保留项标记和 Stage-3 击杀决策，但无 Stage-2 打分表。无法从本仓库中找回。

**C. 五个 Stage-1 池中有三个缺少完整想法文本。** SEG-0001…0365, VFM-A 180, ASM-A 180。`eliminated_ideas_summary.md` 指向 `/workspace/research_ledger/`，那是一个云端工作树路径，并非本仓库。此处仅提交了两个本地 350 想法池。

**D. Stage-2 计数无法调和。** `Windows1/selection_history/reviewer_summary.md` 写道 "31 KEEP200 / 8 PROTECT-HRHR / 14 MUTATE / 4 KILL"。统计 `research_ledger/stage2_seg_review.md` 中的 ID 列表得到：

| 分类 | `reviewer_summary.md` 声称 | `stage2_seg_review.md` 实际列出的 ID | 是否吻合？ |
|---|---|---|---|
| KEEP200 | 31 | **23** | 否 |
| PROTECT-HRHR | 8 | **6**（0019, 0054, 0074, 0252, 0355, 0276） | 否 |
| MUTATE | 14 | **15** | 否 |
| KILL | 4 | **4**（0048, 0061, 0170, 0274） | **是** |
| *(单独列表)* 被低估提升项 | 未给出 | 15 | — |

总账的四个分类相加为 23+6+15+4 = **48**，与其自身表头 "## Named-48 decisions" 完全吻合，因此 `stage2_seg_review.md` 内部是一致的。`reviewer_summary.md` 中的 31/8/14 数字因而属于离群值。**此处不予修正** —— `reviewer_summary.md` 是既有的 Windows1 结论文档。提交人工裁决。

**E. Stage-5 的五个从未被指明。** `stage5_killers.md` 枚举了一个 "Engineer Top-5"，随后将其推翻："SUPERVISOR CORRECTION: 0276-M shape-prior field was omitted from this Stage-5 prompt (R2 ranked it #1, inference-only killer). **Must add back before locking Top-5.**"。随后该文件给出了一个包含五项的 "Likely final-3 pool"，那*不是*工程师的 Top-5。没有任何文件说明哪五个进入了 Stage 6。`stage5_top5.md` 重建了候选集并明确标出歧义，而非擅自挑选五个。

**F. 字母 "C" 下落不明。** 见 §2。Final 3 被标为 A/B/D。无 C 的记录。

**G. Stage-4/5 边界上的两份排序列表不一致，且彼此未相互取代。**
`stage4_reviewer2.md` 中的 R2 Top-7 将 `0276-M` 排在第一，且不包含 `Frozen/tuned n*`、`0046-M`、`0074-M` 或交互式评测合并项。`meta_audit.md` 中的 Top-8 包含上述全部四项，且**完全遗漏了 0276**（将其降为 "Protect 0276 … as benches"）。`stage5_killers.md` 展示了其后果：工程师依据 Top-8 开展工作，导致 0276-M 掉出，必须由 supervisor 修正重新加入。记录于 `stage4_candidates.md` §5 与 `stage5_top5.md` §2。

**H. 命名空间错误：`A0263`。** `stage3_vfm_kills.md` 将 `A0263 constrained SAM-FT` 列在 MUTATE 下。`A` 命名空间为 VFM-A/ASM-A，`stage1_vfma_asma_keepers.md` 将其各自限制在 180 条想法内，因此 `A0263` 不可能存在于其中。其指代对象应为 `stage1_vfm_local_pool.md` 中的 `VFM-0263`（"Constrained FT: maximize target Dice s.t. SA-1B drop < ε"），`stage4_reviewer2.md` 正确将其引用为 `VFM-0263/0274`。在总账中**未悄悄修正**；在此予以标记。

**I. `stage4_reviewer2.md` 错述了其自身评审组记录的存放位置。** 它声称完整评审组位于 "on branch cursor/reviewer2-stage4-kill-panel-5733 (cloud worktree, **not this repo**)"。该分支*就在*本仓库中，且评审组记录已从中找回。见 `stage4_candidates.md` §1。括号内的陈述事实性错误；予以标记而非编辑原文。

**J. 五个 Stage-3 SEG 存活者与七个 Stage-3 VFM 存活者在 Stage 4 之前无故消失。** 枚举于 `stage3_survivors.md`，均标有 `NO RECORDED REASON — 需人工确认`。

---

## 5. 与 `README.md` / `research_summary.md` 的冲突

依据本任务的约束，上述两份文档具有权威性且未被修改。本节的存在是为了让任何张力显性化，而非掩埋它们。

| 项目 | `README.md` / `research_summary.md` 的陈述 | 本审计发现 | 处置 |
|---|---|---|---|
| Stage-1 池规模 | "local VFM ~350 + local ASM ~350" | 恰好 350 与 350 | **无冲突** —— "~" 仅代表保守估计。记录为精确化而非更正。 |
| Stage-1 完备性 | "local pools + compact batches completed the ≥1000 requirement" | 要求在*数量*上得到满足；总计 1425 条毛想法中 725 条的可评审*文本*不在本仓库中 | **存在张力，非直接矛盾。** 主张针对的是生成而非归档。予以保留；缺口记录于 §4-C。 |
| Stage-2 广度 | "~84 SEG keep + VFM/ASM keepers" | 仅存在 SEG 评审表；无 VFM/ASM Stage-2 表，且约 84 无法重构 | **提交裁决。** §4-B, §4-D。 |
| Stage-6 存在性 | "Stage 6 locked method + medical-safety characterization + medical uncertainty method" | 由 `reviewer_summary.md` 中的三项独立分歧佐证；无原始记录 | **作为 KNOWN FACT 接受 Stage 6 曾发生过**；其内容经重建并标为事后补记。§4-A。 |
| Final-3 标签 | "A RetainSAM, B LesionSuppress, D DisagreeShift" | 归档中任何地方均无 "C" | **提交裁决。** §4-F。 |

---

## 6. 本审计*不做*的事情

- 它不重新选题。Final 3 已锁定且超出本任务范围。
- 它不把任何 Stage-2 打分当作事实。`stage2_seg_review.md` 写道 "Scores are REVIEWER JUDGMENT not facts" 与 "Do not treat Pub=L as verified novelty"；回填文件中均遵守了这两项约束，记录决策及其成文理由而未将打分重申为科学发现。
- 它不触碰 `research_ledger/`。那 12 个文件的任何一个字节都未被修改、移动或重命名。理由见 `LEDGER_INDEX.md` §4。
- 它不编造理由。每个重建的行要么引用总账文件，要么盖戳 `NO RECORDED REASON — 需人工确认`。
