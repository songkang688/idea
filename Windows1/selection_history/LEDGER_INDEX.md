# 总账索引 —— Windows1 按阶段漏斗记录的实际存放位置

状态：**事后索引，撰写于 Final 3 已锁定并合并至 `main` 之后。**
本文件中的任何内容均不重新打开选题决策。它仅记录*归属*与*位置*。

此处使用的认知标签遵循 `Windows1/README.md`：KNOWN FACT, EVIDENCE, HYPOTHESIS,
MODEL SPECULATION, EXPECTED RESULT, ACTUAL EXPERIMENTAL RESULT。
本索引中任何地方均不出现 ACTUAL EXPERIMENTAL RESULT，因为本轮不存在此类数字。

---

## 1. 本文件解决的问题

**KNOWN FACT。** Windows1 交付的三个 Idea package 及其三份总结文档位于
`Windows1/` 目录下。但按阶段的漏斗记录 —— 展示 ≥1065 条想法*如何*变为 3 条的文件 ——
不在 `Windows1/` 目录下。它们是**仓库根目录 `research_ledger/` 中的 12 个文件**。

**KNOWN FACT。** 在本次回填之前，`Windows1/selection_history/` 仅包含三份约 1 KB 的摘要
（`evolution_summary.md`、`eliminated_ideas_summary.md`、`reviewer_summary.md`）。从
`Windows1/` 开始阅读的读者没有指向根目录总账的指针，因此无法审计任何具体阶段。

---

## 2. 归属证明：根目录总账的全部 12 个文件均属于 Windows1

两类独立的证据确立了这一点。其中六个文件在其标题中直接点名；另外六个由仅存在于 Windows1 文档中的内容所钉住。

### 2a. 标题中直接点名窗口的文件（KNOWN FACT，自识别）

| 文件 | 确切标题行 |
|---|---|
| `research_ledger/stage1_seg_keepers.md` | `# Stage 1 ingest — SEG slice (Windows1)` |
| `research_ledger/stage1_vfm_local_pool.md` | `# Local VFM/PEFT/SAM pool (Windows1 supervisor backup)` |
| `research_ledger/stage1_asm_local_pool.md` | `# Local assumption-breaking pool (Windows1 supervisor backup)` |
| `research_ledger/stage2_seg_review.md` | `# Stage 2 — Independent SEG review (Windows1)` |
| `research_ledger/stage4_reviewer2.md` | `# Stage 4 — Reviewer #2 (Windows1)` |
| `research_ledger/meta_audit.md` | `# Meta-audit (Windows1)` |

### 2b. 标题中无窗口标记、通过交叉引用归属的文件（EVIDENCE）

其余六个文件**不**携带 `(Windows1)` 字符串。下方通过与 Windows1 作者文档的具体、可查证重合进行归属。凡用词近乎一字不差之处均予以指出，因为逐字重合远强于主题层面的重合。

| 文件 | 将其钉在 Windows1 的交叉引用 | 强度 |
|---|---|---|
| `stage1_vfma_asma_keepers.md` | 其保留项 ID（`A0022, A0051, A0028, A0077, A0101, A0121, A0148, A0153, A0166, A0168`）恰好是 `stage3_vfm_kills.md` 裁决的 ID 集合，其结尾行 —— "Downweight LLM-only … for **this round's final 3**" —— 是一条 Windows1 supervisor 指令。 | 强 |
| `stage3_priorwork_kill.md` | 其 `SURVIVE: 0252, 0275, 0250, 0285(weak)` 行在 `Windows1/selection_history/reviewer_summary.md` 中重述为 "strongest remaining SEG science was 0252, 0250, 0275, 0276-M"。它裁决了带有 Windows1 标记的 `stage1_seg_keepers.md` 中枚举的 SEG-00xx ID。 | 强 |
| `stage3_vfm_kills.md` | 其四条击杀 —— `A0022 TETRIS; A0168 RClicks; A0077 PARA; A0148 Registers` —— 作为四个独立行出现在 `Windows1/selection_history/eliminated_ideas_summary.md` 中（`VFM-A0022 \| TETRIS AAAI 2024`, `VFM-A0168 \| RClicks 2024`, `VFM-A0077 \| PARA / AdaLoRA`, `VFM-A0148 \| DINOv2 registers`）。四对四，近乎一字不差。 | 极强 |
| `stage4_reviewer2.md` *(亦在 2a)* | 其 `Source: bc-90c313c0-…-45733` 与找回的完整评审组记录标题 `# Stage 4 — Reviewer #2 Kill Panel (**Windows1 PI**)` 吻合。见 `stage4_candidates.md`。 | 极强 |
| `stage5_0276.md` | SEG-0276-M 是 `Windows1/README.md` 中点名的亚军（"Runner-up **SEG-0276-M** (prior-shape interpolation α) is HRHR and inference-only"）。其 "Recommendation from designer: INCLUDE, displace Constrained SAM-FT" 在 `reviewer_summary.md` 中重述为 "0276 designer recommended displacing RetainSAM"。 | 极强 |
| `stage5_killers.md` | 其 "Engineer Top-5" #1 `Constrained SAM-FT` 即为 Windows1 的 `Idea_01` RetainSAM；它引用的 "auditor Top-8" 正是带 Windows1 标记的 `meta_audit.md` 内部的 `Updated working Top-8` 清单。 | 强 |
| `cheap_killers_0252_0046.md` | 其公式 `0252: amplification g ≈ ρ_H · ρ_M` 出现在 `Windows1/selection_history/evolution_summary.md` 中，表述为 "SEG-0252 label ecology (**cheap ρ_H·ρ_M design exists**)"。其第二个对象 `0046-M` 出现在同一 evolution_summary 行中（"0046-M transmittance (matting / SMOKE5K AAAI 2022)"）。 | 极强 |

**对记录的更正说明。** 笼统声称全部 12 个标题均带有 `(Windows1)` 是错误的；
只有 2a 中的六个带有。其余六个是通过内容归属的，如表所示。记录这一区分是为了防止后续审计员去"核查"一个并不存在的标题标记。

### 2c. 额外佐证：池规模完全精准，非约数（KNOWN FACT）

`Windows1/research_summary.md` 将本地池描述为 "local VFM ~350 + local ASM ~350"。
统计根目录两个池文件中带有 ID 的行数：

| 文件 | 找到的 ID 数 | 范围 |
|---|---|---|
| `stage1_vfm_local_pool.md` | 350 | `VFM-0001` … `VFM-0350`，无断缺 |
| `stage1_asm_local_pool.md` | 350 | `ASM-0001` … `ASM-0350`，无断缺 |

因此 `~350` 在两种情况下恰好都是 350，且 `365 + 350 + 350 = 1065` 精确复现了
`research_summary.md` 中的 "≥1065" 数字。这是针对本仓库中文件的算术统计，
不是估计值。

---

## 3. 按阶段总账索引

漏斗级别 → 总账文件。下方每个级别均可从 `Windows1/selection_history/` 通过本表格访问。

| 漏斗级别 | 根目录总账文件 | 大小 | 包含内容 | 本目录下回填的配套文件 |
|---|---|---|---|---|
| **Stage 1** 生成（SEG 切片） | `research_ledger/stage1_seg_keepers.md` | ~2.4 KB | 声称 365 条 SEG 想法；簇计数；Top-30 保留项；13 条受保护 HRHR。**仅限摘要 —— 完整的 SEG-0001…0365 文本不在本仓库中。** | — |
| **Stage 1** 生成（VFM 池） | `research_ledger/stage1_vfm_local_pool.md` | ~43 KB | 完整的 350 条本地 VFM/PEFT/SAM 想法池，每想法一行（`ID \| idea \| hyp \| minExp \| cluster \| risk`）。包含 Idea_01 的祖先 `VFM-0263` 与 `VFM-0274`。 | — |
| **Stage 1** 生成（ASM 池） | `research_ledger/stage1_asm_local_pool.md` | ~34 KB | 完整的 350 条本地打破假说（assumption-breaking）想法池。 | — |
| **Stage 1** 紧凑批次 | `research_ledger/stage1_vfma_asma_keepers.md` | ~1 KB | VFM-A 180 + ASM-A 180。**仅限保留项摘要 —— 360 条想法正文不在本仓库中。** | — |
| **Stage 2** 独立评审 | `research_ledger/stage2_seg_review.md` | ~1 KB | 命名 48 条决策（KEEP200 / PROTECT-HRHR / MUTATE / KILL），15 条被低估提升项，10 条被高估项。携带自身警示："Scores are REVIEWER JUDGMENT not facts." | — |
| **Stage 3** prior-work 击杀（SEG） | `research_ledger/stage3_priorwork_kill.md` | ~1.2 KB | 5 KILL、4 SURVIVE、11 MUTATE，外加包含 10 条的已排序"顶级科学领地"清单。 | `stage3_survivors.md`（新增） |
| **Stage 3** prior-work 击杀（VFM） | `research_ledger/stage3_vfm_kills.md` | ~0.8 KB | 4 KILL、8 MUTATE、1 WEAK SURVIVE。宣布"交互式评测合并"死亡并为约束 SAM-FT 设立 WiSE-FT 条件。 | `stage3_survivors.md`（新增） |
| **Stage 4** Reviewer #2 | `research_ledger/stage4_reviewer2.md` | ~1.1 KB | 总结：1 条 KILL（0193），其余皆为 KEEP-IF-EXPERIMENT，R2 Top-7，廉价 killer 淘汰项，以及 0285/0252 与元审计的冲突。 | `stage4_candidates.md`（新增 —— **包含找回的完整 12 提案评审组记录**） |
| **Stage 5** killer 规范 | `research_ledger/stage5_killers.md` | ~0.8 KB | 工程师 Top-5、工程师裁减项，以及 supervisor 修正（指出 0276-M 被错误遗漏）。 | `stage5_top5.md`（新增） |
| **Stage 5** 单一想法设计 | `research_ledger/stage5_0276.md` | ~0.5 KB | SEG-0276-M 的 α 设计、SSA 对照、四个数值门禁、成本，以及设计者 vs supervisor 的分歧。 | `stage5_top5.md`, `stage6_battle.md`（新增） |
| **Stage 5** 廉价 killer 设计 | `research_ledger/cheap_killers_0252_0046.md` | ~0.7 KB | 针对 0252（`g ≈ ρ_H·ρ_M`）与 0046-M 的廉价证伪方案；0046-M 上的现有技术风险。 | `stage5_top5.md`（新增） |
| **跨领域审计**（输入 Stage 5 与 6） | `research_ledger/meta_audit.md` | ~1.2 KB | Supervisor 对审计员质疑的 ACCEPTS / REJECTS / PARTIAL；"Updated working Top-8"；保护 0276 和 0240 的指令。 | `stage5_top5.md`, `stage6_battle.md`（新增） |
| **Stage 6** 最终 5 → 3 | **不存在总账文件** | — | Stage 6 由 `Windows1/README.md` 断言（"Stage 6 locked method + medical-safety characterization + medical uncertainty method"），但从未落成文字。 | `stage6_battle.md`（新增 —— 事后补记） |

---

## 4. 为什么这些文件保留在仓库根目录

**它们未被本次回填移动、重命名或删除。这是深思熟虑的选择，而非疏忽。**

1. **KNOWN FACT —— 相同的 blob 可从其他分支访问。** 完全相同的 12 个文件、在相同路径下、具有逐字节一致的 git blob 哈希，出现在至少另外三个分支上（`cursor/stage4-cluster-a-reviewer2-f1fa`, `…-b-…-b25a`, `…-c-…-c1be`）。那些分支承载着*另一个*窗口的 Stage-4 工作（`A-`/`B-`/`C-` ID 命名空间，不同的 supervisor），仅是从基线提交继承了 `research_ledger/`。在 `main` 上重定位该目录会在每一个这类分支的合并路径上引入重命名，将文档清理变成跨窗口的合并冲突。
2. **KNOWN FACT —— `research_ledger/` 是共享路径，非 Windows1 独占。** 分支 `cursor/reviewer2-stage4-kill-panel-5733` 在同一目录中写入了一个*新*文件（`research_ledger/stage4_reviewer2_kill_panel.md`）。该目录是 agent 在各窗口间输出的共享投递箱；它不是 Windows1 的私有目录树，因此"将其移至 `Windows1/` 下"本身就不是正确的规范化做法。
3. **建立索引充分且可逆。** 归属与可导航性才是实际的缺陷。这两点通过本文件以及回填的各阶段记录得以解决，对其他分支零风险。

**需接受的后果。** `Windows1/` 因此*不是*完全自包含的。审计 Windows1 亦需要访问仓库根目录。这是知情下的权衡，本文件就是使之可导航的指针。若未来的轮次希望建立每窗口的总账，正确的做法是在今后的 `Windows15/` 式窗口目录下撰写*新*文件，而非事后移动这个共享目录。

---

## 5. 总账中的已知空缺（详情见 `FUNNEL_DEVIATION.md`）

- **无 Stage 6 文件。** 事后补记为 `stage6_battle.md`；原始的 5 → 3 环节从未被记录。
- **五个 Stage-1 池中有三个仅为摘要。** SEG-0001…0365、VFM-A 180 与 ASM-A 180 的完整正文在本仓库中缺席。`Windows1/selection_history/eliminated_ideas_summary.md` 写道 "Full pools live in `/workspace/research_ledger/`" —— 该 `/workspace/` 路径曾是云端工作树，此处仅提交了两个本地 350 想法池。
- **Stage 3、4、5 无独立的存活者清单。** 仅保留了击杀表和片段。在本目录下进行了重建，每条无支撑的行均标有 `NO RECORDED REASON — 需人工确认`。
- **总账内部存在命名空间错误。** `stage3_vfm_kills.md` 写着 `A0263 constrained SAM-FT`，但 `A` 命名空间（VFM-A / ASM-A）仅到 180 条想法。其实际指代为 `stage1_vfm_local_pool.md` 中的 `VFM-0263`（"Constrained FT: maximize target Dice s.t. SA-1B drop < ε"），`stage4_reviewer2.md` 正确将其引用为 `VFM-0263/0274`。记录供人工确认，未悄悄更正。
