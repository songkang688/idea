# Stage 5 → Top-5 (Windows8)

count=5

- **审计日期：** 2026-08-29（UTC+8），由 Stage-5 审计／记录环节重写。
- **输入：** 来自 `stage4_top20.md` 的 19 个候选（该文件自己声明 `count=19`：`IDEA-X-0001..0010` 加 9 条 `IDEA-A` 网格条目）。
- **输出：** 5 个候选。上方 `count` 确实等于 5，下方表格恰好 5 行，因此本文件现在与自己的文件名一致了。
- **Stage-5 判据（按已有记录）：** `evolution_summary.md` → "5 Engineering | ~5 | **5** | ROI = information per GPU-hour."

## 为什么要重写这个文件

**FACT.** 本文件的上一版声明 `count=10`，列出的恰好是那十条手工想法 `IDEA-X-0001..0010`。那其实是把 `stage4_top20.md` 的 X 子集原样抄下来，并不是一次 Stage-5 选择。它还把 `stage4_top20.md` 携带的全部 9 条 `IDEA-A` 条目一次性丢掉，没有留下任何理由，并且从未说明每个打包后的 Idea（`Idea_01/02/03`）是从哪个 stage-4 ID 传承而来。这次重写修正了计数，补上了 19→5 的淘汰记录，并补上了血统映射。**本次重写没有重新做任何选择决策**：下面的 Top-5 是从整个目录树中唯一真正存在五条 Stage-5 清单的位置抄录过来的，即 `evolution_summary.md` → "Stage 5 Top 5 (ROI order)"。`Idea_01/`、`Idea_02/`、`Idea_03/`、`stage2_top200.md`、`stage3_top50.md` 和 `stage4_top20.md` 均未被修改。

## 1. Top-5（按 ROI 排序）

排序来源：`evolution_summary.md` 的 "Stage 5 Top 5 (ROI order)" 一节。
假设、最小实验与风险抄录自 `raw/batch_X_hand.md`（字段 `Hypothesis` / `MinExp` / `Risk`），凡已有对应 package 的，再与该 package 的 `experiments.md` 交叉核对。

| # | ID | 代号 | 科学假设（一句话） | 最小 killer 实验 | 最大风险 | 是否进入 Final 3？ |
|---|----|----------|----------------------------------|---------------------------|--------------|-------------|
| 1 | `IDEA-X-0004` | Spectral LoRA audit | **HYPOTHESIS** （LoRA 适配后 − 冻结）特征差的能量中，超过 80% 落在一个无法表示 1 像素边界的空间频率截止点以下。 | 一张 GPU：在 64 张图像上保存特征差并做 FFT（`batch_X_hand.md`）。package 形态：三种 PEFT 变体、冻结 vs 适配后的编码器特征图、径向 FFT 能量（`Idea_02/experiments.md` → "Killer"）。 | **HYPOTHESIS** 需要谨慎选择层；结果可能只是"探测了哪个 block"带来的假象。 | **是 —— Idea_02** |
| 2 | `IDEA-X-0001` | Exclusion-region prompting | **HYPOTHESIS** 排除区提示能在不微调编码器的情况下提升烟雾／浸润性肿瘤上的 NSD，并且对 COCO 物体**没有**帮助。 | 在烟雾周围画一圈负向环带；与 GT-box SAM 对比（`batch_X_hand.md`）。package 形态：`Idea_01/experiments.md` E0 的条件 C，外加排除通道开／关的消融。 | **HYPOTHESIS** 真实用户不会去画环带（部署有效性问题）。package 又补了第二个风险：如果环带泄漏了 GT，那这个效应就是假象——`Idea_01/experiments.md` 要求独立于 GT 地消融环带宽度。 | **是 —— Idea_01** |
| 3 | `IDEA-X-0003` | IoU-token reject option | **HYPOTHESIS** 在无定形测试上，对 SAM IoU token 做阈值化，其提升 risk-coverage Dice 的幅度大于额外参数量相同的 Med-SA。 | 在 Trans10K 与一个烟雾数据集上绘制 risk-coverage 曲线（`batch_X_hand.md`）。package 形态：`Idea_03/experiments.md` E0，COCO vs 无定形的可靠性图，**无需训练**；"Kill if E0 does not show a domain gap in calibration."。 | **HYPOTHESIS** IoU 头也许干脆就是无信息量的，那样就根本没有可供重校准的选择性预测信号。 | **是 —— Idea_03** |
| 4 | `IDEA-X-0007` | Replay for promptability | **HYPOTHESIS** 在医学 PEFT 过程中混入 1% 的合成点击分割数据，可以保住 COCO 提示 mIoU，而医学目标上的 Dice 下降小于 1。 | COCO 代理数据 200 张 + LoRA（`batch_X_hand.md`）。 | **HYPOTHESIS** 合成点击不是 SA-1B，因此被保住的可提示性未必能迁移到真实的提示分布上。 | **否 —— 备选** |
| 5 | `IDEA-X-0002` | Density decoder on frozen SAM | **HYPOTHESIS** 在标注时间对齐之后，冻结的 SAM token + 1×1 卷积密度头在烟雾 IoU 上胜过带提示的 SAM。 | 在 200 帧烟雾图像上训练一个 1×1 头（`batch_X_hand.md`）。package 形态：`Idea_01/experiments.md` E0 的 A/B/C 三个条件，在一张 12–24 GB GPU 上含 embedding 缓存共 <8 小时。 | **HYPOTHESIS** 密度 GT 本身就是有歧义的；另外"预测整片天空"这类退化解必须靠 precision 抓出来（已记录于 `Idea_01/experiments.md` → Failure analysis）。 | **是 —— Idea_01**（已并入 Idea_01 的方法） |

### 关于这份 Top-5 构成的说明

**FACT.** 已有记录中的 Top-5 是 **4 条 Final-3 血统 + 1 条备选**，而不是 3 + 2。`Idea_01` 一家占掉了五个席位中的两个（`IDEA-X-0001` 排除区 + `IDEA-X-0002` 密度），这与 `README.md` 把 Idea_01 描述为 "frozen SAM embeddings + density/**exclusion** vs prompted SAM" 是一致的。唯一的备选是 `IDEA-X-0007`，其被看重的成文依据是 `eliminated_ideas_summary.md` → "Parked high-ROI (not final 3) | X-0007 Replay promptability | **Strong**; overlaps Idea_02 forgetting subplot | Revive if: Idea_02 killer is negative and forgetting is the remaining story."。我没有为了凑出第二个备选而把第六条提上来。

## 2. 淘汰记录：19 → 5（14 条）

按审计规则，可作为淘汰理由的来源只有：`stage3_top50.md` / `stage4_top20.md` 中已记录的 prior-work 攻击、`reviewer_summary.md`、`eliminated_ideas_summary.md`，或明确的漏斗规则。凡这些来源都覆盖不到的具体 ID，一律标注 `NO RECORDED REASON`，而不是给它编一个理由。

关于引用的注意事项：下文中的 arXiv 编号与会议名称都是**按 `reviewer_summary.md` 中的原样记录**抄录的。本次审计没有独立复核它们。因此它们被标为 **VERIFIED PRIOR WORK (as recorded)**。

### 2a. 被淘汰的手工想法（`IDEA-X`），5 条 —— 全部有成文理由

| ID | 代号 | 已记录的淘汰理由 | 来源 | 标签 |
|----|----------|----------------------|--------|-------|
| `IDEA-X-0005` | Equal-annotation-minute bakeoff | "Important control, not a method."。复活规则："Use inside Idea_01 Week 2."。已确认被吸收：它以 `Idea_01/experiments.md` E4 "Equal annotation minutes vs nnU-Net" 的形式出现，并出现在基线 4 中。 | `eliminated_ideas_summary.md` → "Parked high-ROI (not final 3)"；`Idea_01/experiments.md` | FACT |
| `IDEA-X-0006` | Prompt-tightness confound | 有两处记录。(i) Stage-3 prior-work 攻击："Box prompts beat points on fire" 对上 arXiv:2510.21782 → "**Kill.** Mutate to tightness-matched confounder study (X-0006, **not in final 3**)"。(ii) "Cheap workshop paper"，复活时机 "After Idea_01 prompt experiments."。已确认被吸收为 `Idea_01/experiments.md` E1 "Prompt tightness matched, jitter boxes to IoU∈{0.5,0.7,0.9}"。 | `reviewer_summary.md` → "Prior-work kills (Stage 3) — EVIDENCE"；`eliminated_ideas_summary.md`；`Idea_01/experiments.md` | VERIFIED PRIOR WORK (as recorded) + FACT |
| `IDEA-X-0008` | Rater-as-model | "Needs LIDC multi-rater discipline."。复活规则："Medical-only pivot."。 | `eliminated_ideas_summary.md` → "Parked high-ROI (not final 3)" | FACT |
| `IDEA-X-0009` | Patch/lesion diameter law | "Maybe too simple; still a killer plot."。复活规则："Add as Idea_01 analysis figure."。 | `eliminated_ideas_summary.md` → "Parked high-ROI (not final 3)" | FACT |
| `IDEA-X-0010` | Language does not group pixels | "Open-vocab VLM dense papers that cannot freeze the grouper fairly (**X-0010 parked**)."。这与该想法自己记录的风险 "Hard to freeze fairly"（`raw/batch_X_hand.md`）相吻合。 | `eliminated_ideas_summary.md` → "Reviewer #2 unsound (Stage 4)" | FACT |

**记账不一致，只标记不修正。** `eliminated_ideas_summary.md` 把 `X-0010` 的搁置归档在标题 "Reviewer #2 unsound (**Stage 4**)" 之下，然而 `X-0010` 至今仍然出现在 `stage4_top20.md` 里（`count=19`）。两个文件之间差了一个阶段。`stage4_top20.md` 不在本任务范围内，因此这里只作记录交人工裁决，并把该淘汰按 Stage 5 记账。

### 2b. 被淘汰的网格想法（`IDEA-A`），9 条 —— 逐条交代

这 9 条全部解析到 `raw/pool.jsonl` / `raw/batch_A_prior.md`（关于 ID 命名空间冲突见 §4）。**FACT：** 它们在 `pool.jsonl` 中携带的是完全相同的模板文本 —— `problem` = "Community default explanations for failures in *domain* may be wrong; we test core *CORE*"，`min_exp` = "Two-condition A/B on a public *domain* split; freeze all but the hypothesized component; report Dice/NSD/IoU-cal plus a control metric"，`risk` = "Closest eval papers may already contain the observation without the intervention"。它们没有一条指名任何数据集、预算或具体的测量工具。这一点对于 Stage-5 规则 "ROI = information per GPU-hour" 是相关的，但它是整个 `IDEA-A` 家族的共性，因此本身无法解释为什么偏偏是这 9 条被丢掉而其他条目被保留。它只作为背景记录，不作为逐条理由。

| ID | 代号 | 状态 | 已记录的理由 / 缺口 | 来源 | 标签 |
|----|----------|--------|-----------------------|--------|-------|
| `IDEA-A-0001` | SAM-OBJECTNESS | **是合并，不是杀掉** | 它作为独立的 Stage-5 行被去掉，但作为 Idea_01 的子假设保留了下来：Final-3 表格把 Idea_01 的起源 ID 写为 "X-0001 + X-0002 + **SAM-OBJECTNESS** + LINEAR-PROBE"。其假设文本也与 `README.md` 第 12 行（"frozen SAM embeddings + density/exclusion vs prompted SAM … with a COCO control"）以及标题 "Objectness, Not Features" 相吻合。**缺口：** 这次合并只在 Final-3 层面有记录；没有任何文件记录 Stage-5 当时的合并决策本身。 | `evolution_summary.md` → "Final 3" 表格的 Idea_01 行；`README.md`；`research_summary.md` | FACT（仅部分有记录） |
| `IDEA-A-0064` | SAM-IOU-CAL | **是合并，不是杀掉** | 同样的模式：Final-3 表格把 Idea_03 的起源 ID 写为 "X-0003 + **SAM-IOU-CAL** + SELECTIVE"。它的主张（IoU token 在 SA-1B 物体上校准良好、在低对比度／无定形掩码上误校准）正是 `Idea_03/experiments.md` E0 专门用来击杀的那个领域差前提。**缺口：** 同上，合并只在 Final-3 层面有记录。 | `evolution_summary.md` → "Final 3" 表格的 Idea_03 行；`Idea_03/experiments.md` | FACT（仅部分有记录） |
| `IDEA-A-0022` | SAM-TEXTURE | 在簇层面被杀掉 | Stage-3 prior-work 攻击："Failures are texture / tree-likeness" 对上 arXiv:2412.04243 → "Do not repeat their metric. Test a **competing** mechanism: objectness decoder vs texture encoder."。纹理机制被有意指派为对手假设的角色，而不是主打想法，Idea_01 站的是 objectness 那一边。`Idea_01/experiments.md` → "Negative result interpretation: H1 false + random-features also fails → encoder limit (align 2412.04243)" 进一步强化了这一点。 | `reviewer_summary.md` → "Prior-work kills (Stage 3) — EVIDENCE"；`Idea_01/experiments.md` | VERIFIED PRIOR WORK (as recorded) |
| `IDEA-A-0043` | SAM-PROMPT-GEOM | 在簇层面被杀掉 | Stage-3 prior-work 攻击："Box prompts beat points on fire" 对上 arXiv:2510.21782 → "**Kill.** Mutate to tightness-matched confounder study (X-0006, not in final 3)."。因此提示几何这条线只以 `X-0006` 的形式存活，而后者本身也被搁置（§2a）。原机制与它的变异体双双出局。 | `reviewer_summary.md` → "Prior-work kills (Stage 3) — EVIDENCE" | VERIFIED PRIOR WORK (as recorded) |
| `IDEA-A-0085` | SAM-NEGCLICK | 被淘汰 | **NO RECORDED REASON — dropped silently in the original run，需人工确认。** `reviewer_summary.md`、`eliminated_ideas_summary.md`、`evolution_summary.md`、`research_ledger.md` 中都没有任何一处提到负点击、打洞现象或这个 ID。最接近的相邻条目：`IDEA-X-0001` 排除区提示占据了同一片"负向／排除提示语义"的领地，并被保留在第 2 名。`X-0001` 是否本意就要吞并 `A-0085`，属于本审计员的 **SPECULATION**，因此**不**被用作淘汰理由。 | — | NO RECORDED REASON |
| `IDEA-A-0106` | SAM-MULTIMASK | 被淘汰 | **NO RECORDED REASON — dropped silently in the original run，需人工确认。** 除 `stage2/3/4` 的清单和原始池之外，没有任何文件提到多掩码歧义排序、这个代号或这个 ID。 | — | NO RECORDED REASON |
| `IDEA-A-0127` | SAM2-MEMORY | 被淘汰 | **NO RECORDED REASON — dropped silently in the original run，需人工确认。** 最接近的相邻记录是 `eliminated_ideas_summary.md` → "Exact or conceptual duplicates of prior work (Stage 3): 'Evaluate SAM2 on fire with boxes'"，但那一条讲的是在火焰上做框提示，而不是"视频记忆在各自独立运动的羽流之间泄漏身份"，因此覆盖不到本主张。把它当成重复条目会属于 **SPECULATION**。 | — | NO RECORDED REASON |
| `IDEA-A-0169` | HQ-BOUNDARY | 被淘汰 | **NO RECORDED REASON — dropped silently in the original run，需人工确认。** 最接近的相邻记录是 Stage-3 那一行 "SAM fails on context-dependent / fire / transparent" 对上 "Trans10K + SAM evals" → "**Kill as an evaluation-only paper.**"。那一行既没有点名 HQ-SAM 也没有点名 high-quality token，而 `A-0169` 提出的是一个组件层面的主张而非单纯的评测，因此那一行不足以覆盖它。把它外推过来会属于 **SPECULATION**。 | — | NO RECORDED REASON |
| `IDEA-A-0190` | FT-FORGET | 被淘汰 | **NO RECORDED REASON — dropped silently in the original run，需人工确认。** 最接近的相邻记录：`IDEA-X-0007`（Replay for promptability）以干预的形式问了同一个遗忘问题，并被保留在第 4 名，而 `raw/batch_X_hand.md` 对 `X-0007` 的备注是 "Med-SA claims PEFT avoids forgetting without measuring promptable zero-shot"。没有任何文件说 `X-0007` 取代了 `A-0190`；断言这一点属于 **SPECULATION**。另外要注意，Stage-3 那条杀伤 "Adapt SAM to medical with adapters/LoRA … Kill as a method paper. Keep only *mechanism* questions PEFT does not answer" 如果说明什么，反倒是支持**保留** `A-0190` 的，因为它正是一个机制问题。 | — | NO RECORDED REASON |

### 淘汰记录汇总

| 分类 | 数量 |
|--------|-------|
| 有成文理由（搁置 / prior-work 杀伤 / reviewer 判定不成立） | 7（`X-0005`、`X-0006`、`X-0008`、`X-0009`、`X-0010`、`A-0022`、`A-0043`） |
| 记录为并入某个 Final-3 package 而非杀掉 | 2（`A-0001`、`A-0064`） |
| `NO RECORDED REASON` —— 需人工确认 | 5（`A-0085`、`A-0106`、`A-0127`、`A-0169`、`A-0190`） |
| **淘汰合计** | **14** |

保留 5 条 + 淘汰 14 条 = 输入 19 条，与 `stage4_top20.md` 的 `count=19` 对得上。

## 3. ID 血统映射：Final 3 ← stage-4 ID

下面每一行的合并依据都出自同一句话：`evolution_summary.md` 的 "Final 3" 一节，表格列 "Origin IDs"。三行原文如下：

- `| Idea_01 | Objectness, Not Features | X-0001 + X-0002 + SAM-OBJECTNESS + LINEAR-PROBE |`
- `| Idea_02 | Spectral Locality of Dense PEFT | X-0004 + PEFT-SPECTRAL |`
- `| Idea_03 | Selective SAM via IoU-token Recalibration | X-0003 + SAM-IOU-CAL + SELECTIVE |`

| Package | **能够**追溯到 `stage4_top20.md` 的血统 | 对"到底是 X 还是 A？"的裁定 | **无法**追溯到 stage 4 的血统成分 |
|---------|---------------------------------------------------|-----------------------------------|----------------------------------------------------------|
| `Idea_01` Objectness, Not Features | `IDEA-X-0001`（Top-5 第 2）+ `IDEA-X-0002`（Top-5 第 5）+ `IDEA-A-0001` SAM-OBJECTNESS（stage 4，在 §2b 处合并） | **是合并 —— 三者皆是，不是其中之一。** `IDEA-X-0002` 提供密度解码器，`IDEA-X-0001` 提供排除区，`IDEA-A-0001` 提供"objectness 而非特征"的因果框架。旁证：`README.md` 第 12 行（"frozen SAM embeddings + **density/exclusion** vs prompted SAM on amorphous targets, with a COCO control"），以及 `Idea_01/experiments.md`——其 E0 跑的是密度头、其消融开关的是排除通道、其对照就是 COCO 物体划分。 | `LINEAR-PROBE` = `IDEA-A-0316`：只出现在 `stage3_top50.md`，在 `stage2_top200.md` 和 `stage4_top20.md` 中都不存在。**UNRESOLVED**（§5.1）。 |
| `Idea_02` Spectral Locality of Dense PEFT | `IDEA-X-0004`（Top-5 第 1） | **就是 `IDEA-X-0004`，已确认。** 它是唯一可追溯到 stage 4 的祖先。 | `PEFT-SPECTRAL` = `IDEA-A-0211`：只出现在 `stage3_top50.md`，在 `stage2_top200.md` 和 `stage4_top20.md` 中都不存在。**UNRESOLVED**（§5.2）。 |
| `Idea_03` Selective SAM via IoU-token Recalibration | `IDEA-X-0003`（Top-5 第 3）+ `IDEA-A-0064` SAM-IOU-CAL（stage 4，在 §2b 处合并） | **是合并 —— 两者皆是。** `IDEA-X-0003` 提供拒答选项／risk-coverage 方法；`IDEA-A-0064` 提供反校准的领域差前提——那正是 `Idea_03/experiments.md` E0 存在的目的，也是 `reviewer_summary.md` 所指出的、回应"大家早就在对 SAM 的 IoU 做阈值了"的唯一办法。 | `SELECTIVE` = 一个含 53 条记录的网格 core，代表条目 `IDEA-A-1051`：存在于 `raw/pool.jsonl`，但在 stage 2 / 3 / 4 中**全部**缺席。**UNRESOLVED**（§5.3）。 |

## 4. 想法池的已知缺陷（FACT —— 既有文件中的自述，加上本次审计重新计数的结果）

**FACT（自述）。** `research_summary.md` → "Unresolved risks"："Cloud sub-agents failed or hung; pool is Supervisor-generated from **52 cores × mutations** (documented), plus **10 hand ideas**."。原始数量在 `research_summary.md`（"Raw ideas: 2766 (≥1000)"）和 `research_ledger.md`（"2766 raw IDs in `selection_history/raw/pool.jsonl`"）中都声明为 2766。

**FACT（自述）。** `supervisor_log.md` → "Stage 1 recovery (t1)"：批次 A/B/C 的三个云端子 agent 全部返回 ERROR，"`request is required and could not be loaded from cloud agent state`"。补救办法：批次 C 在云端重试（`bc-7a636a75-321a-50bf-bd04-7ae953ed578d`，成功，350 条想法）；批次 A 由**本地** file-writer 产出（350 条想法）；批次 B 由**本地** file-writer 产出（`bc-fb91c4d2-b3c2-5ef7-bb3f-59ac95cf0894`，350 条想法）。因此三个 Stage-1 生成器之间的独立性，比 "Stage 1 dispatch (t0)" 里原本设计的三云端 agent 方案要弱。

**FACT（本次审计通过计数核实）。** `raw/pool.jsonl` 恰好包含 2766 行 JSON，构成为 `batch` = A 1092、B 1248、C 416，再加 `A-extra` 3 / `B-extra` 3 / `C-extra` 4 = 10。这 10 条 "extra" 记录正是手工想法 `IDEA-X-0001..0010`。不同 `core` 取值共 62 个，即 **52 个网格 core + 10 条手工想法**，与"52 cores"的说法完全吻合。各文件的网格表头也一致：`batch_A_prior.md` `count=1092`、`batch_B_prior.md` `count=1248`、`batch_C_prior.md` `count=416`。

**FACT（本次审计核实）—— ID 命名空间冲突，并且它影响可审计性。** `raw/` 下存在两个互不相交的 `IDEA-A-####` 命名空间：

- **网格（grid）**，位于 `raw/batch_A_prior.md` 与 `raw/pool.jsonl`，其中 `IDEA-A-0001` = "SAM-OBJECTNESS on natural-COCO-objects"，簇为 `SAM-OBJECTNESS`；
- **350 条生成清单**，位于 `raw/batch_A.md`，其表头声明 "exactly 350 ideas, IDEA-A-0001 .. IDEA-A-0350"，而它的 `IDEA-A-0001` 完全是另一个想法——"SAM's mask boundaries systematically snap to the locally strongest image gradient"，簇标签为 `SAM-FAIL`。

`stage2_top200.md` / `stage3_top50.md` / `stage4_top20.md` 中使用的 `IDEA-A` ID 解析到的是**网格**，不是 `batch_A.md`。核实方式：把三个 stage 文件的每一行都拿去与 `pool.jsonl` 对解——200 / 50 / 19 行，**零个无法解析的 ID、零个 `core` 不匹配**，而且额外列（`core | mutation | domain`，例如 `SAM-OBJECTNESS | invert | natural-COCO-objects`）只存在于网格记录中。B 和 C 也存在同样的冲突（`batch_B.md` 的 `IDEA-B-0001..0350` 加 `IDEA-B-M-*` / `IDEA-B-X-*` vs `batch_B_prior.md` 的 `IDEA-B-0001..1248`；`batch_C.md` 的 `IDEA-C-0001..` vs `batch_C_prior.md` 的 `IDEA-C-0001..416`）。**后果：** 那三份 350 条的生成清单——也就是 Stage-1 中唯一不是模板生成的产物——从未以一个可解析的 ID 进入漏斗。这与 `evolution_summary.md` 自己的备注 "A/B/C hand lists **reinforce** objectness, PEFT spectrum, IoU/eval calibration rather than displacing them" 并不矛盾，但那句话是一个断言，不是可追溯的逐 ID 审计。标记交人工复核；`stage2/3/4` 文件均未被触碰。

**FACT（本次审计核实）—— 漏斗在 Stage 2 与 Stage 3 之间不是单调的，而且 `stage2_top200.md` 看起来是机械生成的而非打分得出的。** 两项测量：

- **`stage3_top50.md` 中的 50 个 ID 里有 30 个在 `stage2_top200.md` 中不存在**（`IDEA-A-0211`、`0232`、`0253`、`0274`、`0295`、`0316`、`0337`、`0358`、`0379`、`0400`、`0421`、`0442`、`0463`、`0484`、`0505`、`0526`、`0547`、`0568`、`0589`、`0610`、`0631`、`0652`、`0673`、`0694`、`0715`、`0736`、`0757`、`0778`、`0799`、`0820`）。一个 ID 不可能合法地进了 50 却没进 200。相比之下 `stage4_top20.md` ⊆ `stage3_top50.md` 是干净的（0 条新增），所以断裂只发生在 2→3 这一步。
- **`stage2_top200.md` 是网格的一个前缀，不是一份 top-200。** 它的 200 行是 10 条手工想法加 190 条 `IDEA-A` 行，覆盖 `IDEA-A-0001..0210`，其中 20 处缺口呈完全规则的模式（下标 ≡ 5, 6 mod 21——即从每 21 行的 core 区块中恰好剔除 2 行，得到 10 × 19 = 190）。这 190 行只覆盖了 **52 个 core 中的 10 个**，且全部属于 SAM 家族：SAM-OBJECTNESS、SAM-TEXTURE、SAM-PROMPT-GEOM、SAM-IOU-CAL、SAM-NEGCLICK、SAM-MULTIMASK、SAM2-MEMORY、SAM2-CD、HQ-BOUNDARY、FT-FORGET。剩下 42 个 core——包括 Final-3 血统所依赖的 PEFT-SPECTRAL、LINEAR-PROBE 和 SELECTIVE 这三个——在 Stage 2 完全没有被代表过。

这正是 §5.1–§5.3 三处血统断裂的根本原因，也意味着 `evolution_summary.md` 里记录的那次 "1000 → 200" 评审（"2 Review | ~200 | **200** | Priority: causal tests, cheap falsifiers, high-risk/high-reward, reviewer disagreement"）无法从产物中复现。只作记录；`stage2_top200.md` 不在本任务范围内，未被触碰。

## 5. UNRESOLVED —— 交人工裁决

按审计规则，下面没有任何一项是被单方面决定的，也没有任何一项改动了 `Idea_01/02/03`。

1. **Idea_01 血统里的 `LINEAR-PROBE`（`IDEA-A-0316`）—— 只在恰好一个阶段出现过。** **FACT（本次审计核实）：** `A-0316` 在 `stage2_top200.md` 中缺席，在 `stage3_top50.md` 中存在，在 `stage4_top20.md` 中又缺席。根因见 §4：它属于 Stage 2 从未覆盖的那 42 个 core 之一。两种读法：(a) `stage2_top200.md` 不完整，`A-0316` 确实通过了 Stage 2，然后在 Stage 4 因某个未记录的理由被砍掉；(b) Final-3 表格里的 `LINEAR-PROBE` 只是宽泛地用作对"冻结编码器探针"这一设计的描述，而不是一个漏斗 ID，那么 Idea_01 真正的血统就是 `X-0001 + X-0002 + A-0001`。支持 (b) 的证据：`Idea_01/experiments.md` 把 probe 当作一条基线，而 `reviewer_summary.md` 记录的是 "'Linear probe is not CVPR.' Shut up by: probe vs prompted SAM vs Med-SA on *same frozen encoder*"——也就是把它当对照，不是当主打想法。从文件中无法定论。
2. **Idea_02 血统里的 `PEFT-SPECTRAL`（`IDEA-A-0211`）—— 同一种模式。** **FACT：** 在 `stage2_top200.md` 中缺席，在 `stage3_top50.md` 中存在，在 `stage4_top20.md` 中缺席。它的假设（"LoRA updates for dense tasks are spectrally low-pass; extra rank does not buy boundary frequencies"）几乎就是 `IDEA-X-0004` 的换句话说，因此它可能是被折叠进 `X-0004` 的一个重复条目——但没有任何文件这么说，而且这也解释不了它为什么会在没进 200 的情况下出现在 50 里。
3. **Idea_03 血统里的 `SELECTIVE` —— 从未进入漏斗。** **FACT（本次审计核实）：** `SELECTIVE` 是一个真实存在的网格 core，不是拼写错误。`raw/pool.jsonl` 中有 **53** 条记录的 `core = SELECTIVE`；规范代表条目是 **`IDEA-A-1051`**（`invert` / `natural-COCO-objects`），其一句话表述为 "A reject option on SAM IoU tokens raises effective Dice more than any adapter of equal compute."。但字符串 `SELECTIVE` 和 ID `IDEA-A-1051` 在 `stage2_top200.md`、`stage3_top50.md`、`stage4_top20.md` 中**一处都没有**出现。也就是说，`evolution_summary.md` 把 Idea_03 归功于一个在 Stage 2 就被砍掉（或干脆从未被打分过）且再未重现的祖先。要么 Final-3 表格里的这个词只是散文意义上的"选择性预测"，要么就是有一个真实候选在 Stage 2 之后被从原始池里复活却没有留下记录。需人工裁决；另需注意 `IDEA-A-1051` 的主张与 `IDEA-X-0003` 几乎完全重合，所以无论按哪种解释，科学内容都没有损失——损失的只是审计链条。
4. **那 5 条静默淘汰**（`A-0085`、`A-0106`、`A-0127`、`A-0169`、`A-0190`）各自都需要：要么由当初执行 Stage 5 的人补记一个理由，要么把它们重新放回候选集。本审计员没有替它们编造理由。
5. **`X-0010` 的阶段归属**（§2a）—— `eliminated_ideas_summary.md` 把它记为 Stage-4 杀伤，而 `stage4_top20.md` 仍然列着它。
6. **Final-3 的选择本身没有被重新审视。** 审计规则禁止改动它，而本次审计发现的一切也都不与它矛盾；上述三个未解决的血统标记属于记账缺陷，不是"本应打包另一个想法"的证据。

## 6. 本文件的证据分级声明

- **FACT** —— 关于本目录树中某个文件写了什么的陈述，以及本审计员从 `raw/pool.jsonl` 和 `raw/*_prior.md` 表头重新计算出的计数。
- **VERIFIED PRIOR WORK (as recorded)** —— 那些 prior-work 杀伤及其标识（Med-SA arXiv:2304.12620 / MedIA 2025；SAMed；LoRA-MedSAM；arXiv:2412.01240；arXiv:2510.21782；arXiv:2412.04243；Trans10K + SAM evals；CC-Dice AAAI 2025）都是从 `reviewer_summary.md` 和 `eliminated_ideas_summary.md` 抄录的。本次审计没有拿它们去与文献重新核对，也没有新增任何论文、引用或会议名称。
- **HYPOTHESIS** —— Top-5 表格中假设列、实验列、风险列里的每一条主张。
- **SPECULATION** —— 在行内明确标注，并且从不被用作淘汰理由。
- **EXPECTED RESULT** —— 仅出现在源文件本身已经给出预测的地方，例如 `Idea_02/experiments.md` "Predicted: random 3×3 ≈ LoRA extra rank (no NSD gain)"；`Idea_01/experiments.md` "Random-features encoder (break \(E\)): **EXPECTED** collapse if H1 uses real SAM features"。
- **ACTUAL RESULT —— 无。** 本文件中没有任何一句陈述或任何一个数字被套上这个标签；这一条就是它唯一的出现位置。`evolution_summary.md` 写明 "No actual experimental numbers were produced in this round."。整个目录树里唯一的数值输出都是 toy／合成的，并且都自带标注：`Idea_01/outputs/idea01_e0/toy_report.txt`（"TOY RUN (FakeEncoder). NOT a scientific result."）、`Idea_02/outputs/idea02_fft/toy_report.txt`（"TOY LoRA on random tensors. NOT a scientific result."）、`Idea_03/outputs/idea03_e0/toy_report.txt`（"SYNTHETIC illustration of H1/H2. NOT measured on SAM."）。按 `README.md` 的规定，"Do not report FakeEncoder numbers as results"——因此这些数字一个都没有在本文件中被复述来支持任何假设。
