# Windows6 — 自主研究想法演化（Autonomous Research Idea Evolution）

- **Windows ID：** Windows6
- **创建日期：** 2026-08-28（UTC）
- **Supervisor：** Windows6
- **分支：** `cursor/windows6-research-idea-evolution-b55d`
- **状态：** Stage 1–6 已记录。Final 3 为 **PROVISIONAL —— 尚未锁定。** 裁决与锁定结论见 [`selection_history/stage6_battle.md`](selection_history/stage6_battle.md)。

### Final 3 能被锁定之前还缺什么

`stage6_battle.md` §5 里有三道门禁尚未关闭。三者都不需要 GPU，全部是数小时的案头工作。

| 门禁 | 必须成立的条件 | 失败后果 |
|------|-------------------|----------|
| **GATE-A** | 确认至少 1 个公开烟雾／火焰数据集存在相机元数据，并给出相机**数量** | 少于 10 台相机就只能被迫转向"仅按事件划分"的方案并放弃 H2；完全没有元数据则按 Idea_02 自己的停止规则**杀掉 Idea_02** |
| **GATE-B** | 核实至少一对 base/chat checkpoint 共享视觉编码器**且**共享坐标 tokenization，许可可用 | Idea_03 的阶段隔离（stage-isolation）主张将无法成立，降级为一项格式假象研究 |
| **GATE-C** | 三个存活者与 `D-008` / `D-060` / `E-025` 在同一套评分标准上排过名 | 没有这一步，这一轮只能声称"这三个在唯一跑起来的通道里存活了"，而不能声称"这三个胜过了全场" |

**GATE-D（状态一致性 + package 深度）已由 W6-T3 关闭** —— 见 [`selection_history/status_reconciliation.md`](selection_history/status_reconciliation.md)。

当 A、B、C 三道门禁关闭时，Final 3 方可宣布为 **LOCKED**，并更新本行。在那之前，任何下游文档都不应引用 Windows6 为"已锁定 Final 3"。

## 本轮的三个 Idea（暂定 —— 见上方门禁）

| # | 目录 | Idea | 推荐度 |
|---|--------|------|----------------|
| 1 | `Idea_01/` | 在 CT 上，SAM AMG ≈ HU 强度聚类（机制性 + 反事实） | **#1 从这里开始** —— 最便宜、可证伪、不需要庞大的预训练 |
| 2 | `Idea_02/` | 烟雾／火焰数据上"相机 ID 划分 vs 事件划分"的泄漏问题 | 如果能拿到两个数据集，就是一篇有力的审计论文 |
| 3 | `Idea_03/` | 定位能力上的对齐税（alignment tax，做了格式控制 + 探针） | 影响最大，同时被并行工作抢先的风险也最大 |

## 最推荐

**Idea_01。** Reviewer #2 的各条攻击都有便宜的封嘴实验；CPU 原型已存在；不依赖罕见的 checkpoint 三元组。

## 下一个实验

先跑 `Idea_01/src/amg_intensity_equiv.py`（CPU、合成数据、数秒），然后用 **100 张真实 CT 切片**做 SAM AMG vs k-means / multi-Otsu / GMM / SLIC 的对比（见 `Idea_01/experiments.md`，卡片 E0 → E1 → E2）。

本行此前写的是 *50* 张切片。`Idea_01/experiments.md` 里同时出现过 50（killer 清单）和 100（Stage-5 工程化区块）两个数字；`stage6_battle.md` §4.7 记录了这处矛盾，§6 通过取较大值予以裁定。现已统一使用 **100**。

## 项目状态

| Idea | 状态 |
|------|--------|
| Idea_01 | 可执行深度的 package + 合成原型 + smoke tests；**没有任何真实 SAM 数字** |
| Idea_02 | 可执行深度的 package + 合成划分探针 + smoke tests；**没有烟雾 mAP** |
| Idea_03 | 可执行深度的 package + 格式-vs-探针 demo + smoke tests；**没有 VLM 评测** |

W6-T3 加厚了文档，并让每个 `src/` 都能跑起来。**它没有产出任何测量结果。** 本轮任何脚本打印出的每一个数字都是合成的，并在运行时如实标注。Windows6 中的 **ACTUAL RESULTS 数量为零**。

## 实际执行的漏斗（不是标准阶梯）

`selection_history/supervisor_log.md` 里的政策是 `1000→200→50→20→5→3`。实际跑的**不是**这个：

`1080 原始 / 1062 有效` → **约 142 个打分存活者**（78 个 ABCF + 64 个 DE）→ Stage-3 以两条未合并的分支运行（10 条 DE 裁决 ‖ 12 条 cheap-cluster 裁决）→ **cheap-5** → Reviewer #2 → **3 个存活**。

**不存在 200 档、不存在 50 档、也不存在真正的 20 档**，而且 600 条 S 系列想法从未被 Stage-2 打分。完整偏差表：[`selection_history/stage5_top5.md`](selection_history/stage5_top5.md) §1。
