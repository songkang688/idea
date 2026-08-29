# Idea_01 — 文献验证日志（Literature Verification Log）

`literature.md` 和 `proposal.md` 中引用的所有文献来源的验证状态。建立本文件是为了确保没有任何内容仅仅凭借一连串摘要总结就进入投稿论文的参考文献列表中。

## 标签定义

| 标签 | 含义 |
|---|---|
| `[S5-verified]` | 经 Stage-5 工程师于 2026-08-28 通过网络搜索确认存在 |
| `[S6-verified]` | 在 Stage-6 对抗性审查中发现或重新核实，2026-08-28 |
| `[S6-abstract]` | 已阅读摘要；**未**阅读全文 |
| `[inherited]` | 继承自 Stage-3/4 账本；**未**在 Stage 5/6 中独立重新核实 |

## 验证债务 — 必须在投稿前结清

| 来源 | 当前标签 | 缺失内容 |
|---|---|---|
| TBS, AAAI 2024 | `[inherited]` | 会议、年份与实际内容在 Stage 5/6 中未经核验 |
| AENet, ECCV 2024 | `[inherited]` | 同上 |
| Iterative modulation, CVPR 2024 | `[inherited]` | 同上 |
| `arXiv:2501.13529` (support dilution) | `[S6-abstract]` | 未阅读全文 |
| `arXiv:2607.24706` (SADe) | `[S6-abstract]` | 未阅读全文 |
| Open-V / X2 "37 points" | `[S6-verified]`, 数字为该研究组报告的 `EVIDENCE` | 引用该数字前必须重新阅读原始文献 |

## 已结清项

| 来源 | 标签 | 备注 |
|---|---|---|
| BAM, Lang et al., CVPR 2022 Oral | `[S5-verified]` | 已定位仓库和 checkpoint；也是评测面板成员之一 |
| SAM3, `arXiv:2511.16719`, Nov 2025 | `[S6-verified]` | 促成了 A1 的重新立意定调 |
| SAM 3.1, Mar 2026 | `[S6-verified]` | |
| 评测面板各代码仓库 (PFENet, HSNet, Matcher, PerSAM, FSSAM, SegGPT, SAM/SAM2) | `[S5-verified]` | 仅验证存在性 —— 适用性由 E0 解决 |

## 既定规则

本项目绝不添加任何未在 Windows7 会话中检索并在此记录的引用。如果需要某篇论文且其未在此表中，必须先进行检索并记录。`KNOWN FACT` 本方案包中的任何基准数字均非由我们亲自测得。
