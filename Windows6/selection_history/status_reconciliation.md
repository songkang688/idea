# 状态调和总账（W6-T3）

- **Windows ID：** Windows6
- **分支：** `cursor/windows6-research-idea-evolution-b55d`
- **执行日期：** 2026-08-29（UTC）
- **基线提交：** `cf3ac70`（W6-T2 落地 `stage6_battle.md` 之后紧接的那次提交）
- **任务：** W6-T3（Windows6 三个收尾任务中的最后一个：T1 → T2 → T3）

## 本文件为什么存在

在本任务之前，同一轮里有四个文件各自声称四个不同的阶段。W6-T1 已把这处冲突登记为 [`stage5_top5.md`](stage5_top5.md) §5 中的 INCONSISTENCY-01…04，但有意没有去修；W6-T2 则把这份不自洽的状态记录点名为拒绝锁定 Final 3 的 **Ground 3**。本总账就是这次修复的前后对照记录，好让人工评审无需 diff 就能逐条核对每处编辑与其依据。

**下文每一条状态陈述的依据都是 [`stage6_battle.md`](stage6_battle.md) §5。** W6-T3 没有重新裁决任何事情。它传播的结论就是 W6-T2 当初给出的那一个：**Final 3 是 PROVISIONAL，尚未锁定。**

## 现在各处统一使用的那一条状态语句

> Stage 1–6 已记录。Final 3 **PROVISIONAL —— 尚未锁定**。GATE-A / GATE-B / GATE-C 未关闭；GATE-D 已由 W6-T3 关闭。

## 逐条编辑

### 1. `selection_history/supervisor_log.md` —— "Current stage" 字段（INCONSISTENCY-02）

| | |
|---|---|
| **改前** | `Current stage: **Stage 1 — Massive Idea Exploration** (retry wave)` |
| **改后** | `Current stage: **Stage 6 — adjudicated and recorded.** Final 3 remain **PROVISIONAL**, not locked, pending GATE-A/B/C in stage6_battle.md §5.` |
| **依据** | `stage6_battle.md` §5（结论），以及 `stage5_top5.md` + `stage6_battle.md` 的存在本身。 |
| **备注** | 这个字段不仅仅是相对其他文件过时——它与**自己下方第四行的派发日志**相矛盾，那里早已记录了 *"Stage3 assassin done"* 以及 Reviewer #2 环节。`Last updated` 由 2026-08-28 改为 2026-08-29。 |
| **保留** | 四条原始派发行一字未动；它们是历史。另**追加**了三行（W6-T1、W6-T2、W6-T3）。`## Numbering` 与 `## Policy` 两节未改——特别是 `1000→200→50→20→5→3` 那条政策行被原样留下，因为它记录的是当初*意图*要做什么，而 `stage5_top5.md` §1 已经记录了它并未被执行。 |

### 2. `README.md` —— Status 行（INCONSISTENCY-01）

| | |
|---|---|
| **改前** | `- **Status:** Provisional Final 3 packaged; Stage 5/6 still confirming against DE-top10 assassin + auditor.` |
| **改后** | `- **Status:** Stages 1–6 recorded. Final 3 are **PROVISIONAL — not locked.**`，并新增一节 **"Final 3 能被锁定之前还缺什么"**，其中带 GATE-A/B/C 表格以及"GATE-D 已关闭"的说明。 |
| **依据** | `stage6_battle.md` §5，包括门禁表格及其结尾指令 *"no downstream document should cite Windows6 as having a locked Final 3 until the gates are closed and recorded."* |
| **为什么措辞要改** | 旧那行是一个*没有出口*的状态："still confirming against DE-top10 assassin + auditor" 没有给出任何完成判据，而且它被写下时，被点名的两个产物（`stage3_DE_top10.json.md`、`auditor_overlay.md`）其实早就已经存在了。读者根本看不出"确认"什么时候才算结束。替换后的版本保留了 `provisional`，但写明了退出条件。 |

### 3. `research_summary.md` —— 流水线那一行（漏斗偏差）

| | |
|---|---|
| **改前** | `Pipeline executed: 1000+ ideas → scoring → prior-work kill → Reviewer #2.` |
| **改后** | 一张 `## Pipeline actually executed` 表格，给出 `1080 raw / 1062 live → ≈142 scored → (10 DE ‖ 12 cheap) → cheap-5 → 3 survive`，把缺失的 200 / 50 / 20 档标为 *never produced*，点出 600 条未打分的 S 系列，并给出指向 `stage5_top5.md` §1 的链接。随后是一节 `## Final 3 — PROVISIONAL, not locked`，点名各未关闭的门禁。 |
| **依据** | `stage5_top5.md` §1 与 §1.1（已逐条与 JSONL 记录数核验）；锁定状态依据 `stage6_battle.md` §5。 |
| **为什么** | 旧那行只在"形状"层面为真。它暗示了一条已完成的收缩流水线，同时掩盖了缺失的档位以及从未被打分的那 55% 池子。 |
| **同时还改了** | 结尾那条认知性声明现在还额外写明 `ACTUAL RESULT count for the whole round: zero`，并记录 W6-T3 没有产出任何测量结果。 |

### 4. `selection_history/evolution_summary.md` —— Stage 5 那一行（INCONSISTENCY-03、-04）

| | |
|---|---|
| **改前** | `- Stage 5 cloud engineering + DE assassin + auditor: **done**. Day-1 budgets ~2 / ~10 / ~8 GPU-h. …` |
| **改后** | 同一条，修正为 `**done as work, but never landed as a file at the time** — retrospectively reconstructed by W6-T1 as stage5_top5.md`，并把那几个 GPU-hour 数字明确重标为 **HYPOTHESIS（预算估计），不是实测运行时间**。 |
| **新增** | 一条 **Stage 6** 条目（由 W6-T2 裁决，结论为 PROVISIONAL，并披露当时从未发生过 Stage-6 辩论事件——该裁决是从四次有记录的 rejector 环节重建的）。 |
| **新增** | 一条针对 INCONSISTENCY-04 的**裁决计数更正**：该文件自己写的 *"Keep 2, mutate 3, kill 6"* 合计 11，而 `stage3_prior_work_kill_cheap.jsonl` 里有 12 条记录（保留 2、**变异 4**、杀掉 6）。原句被留在原处、在其下方更正，而不是被悄悄改写，这样那处算术错误就仍然留在记录中可见。 |
| **依据** | `stage5_top5.md` §0 与 §5；`stage6_battle.md` §0 与 §5。 |

## 四处已登记不一致的处置

| ID | 登记在 `stage5_top5.md` §5 中的内容 | 处置 |
|---|---|---|
| **INCONSISTENCY-01** | README 说 Stage 5/6 仍在确认中 | **已解决** —— 见编辑 2。同时也解决了它标记的第四处措辞：`Idea_01/README.md` 里的 *"Stage 5 in flight"* 已在 Part-B 加厚过程中更新。 |
| **INCONSISTENCY-02** | `supervisor_log.md` 卡在 Stage 1 | **已解决** —— 见编辑 1。 |
| **INCONSISTENCY-03** | `evolution_summary.md` 声称 Stage 5 完成却没有产物 | **已解决** —— 见编辑 4，而且产物本身现在已经存在（`stage5_top5.md`）。同一条目中标记的 GPU-hour 误标问题也已修正。 |
| **INCONSISTENCY-04** | 廉价簇的裁决计数 11 vs 12 | **以更正而非改写的方式解决** —— 见编辑 4。错误的计数被保留并加注，而不是被删除。 |

## W6-T3 之后的门禁状态

| 门禁 | 责任方 | 本任务之后的状态 |
|---|---|---|
| **GATE-A** —— 在至少 1 个公开烟雾／火焰数据集上确认相机元数据 | Idea_02 执行者 | **未关闭。** 需要真去查一个真实数据集；超出文档类任务的范围。`Idea_02/experiments.md` 的 E-A 现在已精确规定"关闭它"长什么样。 |
| **GATE-B** —— 核实一对共享视觉编码器 + 坐标 tokenization 的 base/chat checkpoint | Idea_03 执行者 | **未关闭。** 需要真去读模型卡／配置文件；超出范围。`Idea_03/experiments.md` 的 E-B 现在已规定该项检查。 |
| **GATE-C** —— 存活者与 `D-008`/`D-060`/`E-025` 在同一套评分标准上排名 | Supervisor | **未关闭。** 这是一项选题判断；W6-T3 被明确禁止改动 Final 3 或重新裁决，因此它无法关闭这道门禁。 |
| **GATE-D** —— 状态一致性 + package 深度 | W6-T3 | **已关闭。** 状态已调和（即本文件）；`Idea_01`–`Idea_03` 已加厚到可执行深度，`src/` 可运行且 smoke tests 通过；`Idea_01/proposal.md` 此前缺失的 §7–28 已补齐。 |

**后果。** 由于 GATE-A、GATE-B、GATE-C 仍未关闭，**Final 3 保持 PROVISIONAL。** W6-T3 无权锁定它们，也确实没有锁定。

## W6-T3 *没有*触碰的东西

- **Final 3 的构成** —— 未变。
- **任何 Stage 1–4 产物** —— `stage1_pool/*.jsonl`、`stage2_*`、`stage3_*`、`stage4_reviewer2_cheap5.jsonl` 逐字节一致。
- **W6-T1 与 W6-T2 的产物** —— `stage5_top5.md` 与 `stage6_battle.md` 逐字节一致。本总账说某处不一致"已解决"时，解决动作发生在*目标*文件里；`stage5_top5.md` §5 中的登记条目保持原样，因为它是该缺陷的历史记录。
- **任何测量** —— 一次都没有做。本轮的 ACTUAL RESULTS 仍然为零。
