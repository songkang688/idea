# Idea_02 — 文献验证日志（Literature Verification Log）

## 标签定义

| 标签 | 含义 |
|---|---|
| `[S5-verified]` | 经 Stage-5 检索于 2026-08-28 确认存在 |
| `[S6-verified]` | 在 Stage-6 审查中发现或重新核实，2026-08-28 |
| `[S6-abstract]` | 已阅读摘要；**未**阅读全文 |
| `[inherited]` | 继承自 Stage 3/4，未独立重新核实 |

## 验证债务 — 必须在投稿前结清

| 来源 | 标签 | 缺失内容 |
|---|---|---|
| `arXiv:2606.24449` (SENTRY) | `[S6-abstract]` | 全文内容 |
| `arXiv:2602.19380` (CL-MC) | `[S6-abstract]` | 全文内容 |
| SAMITE, HiM2SAM | **经由** `arXiv:2512.22624` 得知 | 未直接阅读原始文献 |
| AS-SAM2 (TCSVT 2026) | `[S6-verified]`, 承诺开源代码 | 代码是否已公开未获确认 |
| SAM2RL "+4.91%" 数据 | `[S6-verified]` | 为该研究组在自设环境下的 `EVIDENCE`；仅作为研究动机，绝不能直接复用为基线数字 |

## 已结清项

| 来源 | 标签 | 备注 |
|---|---|---|
| `arXiv:2512.22624` — Rethinking Memory Design in SAM-Based VOT, Dec 2025 | `[S6-verified]` | 促成了 A3 的重新立意定调；其 SAM3 zoo 降低了 E7 成本 |
| `arXiv:2507.08548` — SAM2RL | `[S6-verified]` | 第二个独立的理论上限；跨上限交叉验证已获资助 |
| SAM3 `arXiv:2511.16719` (Nov 2025), SAM 3.1 (Mar 2026) | `[S6-verified]` | |
| sam2, samurai, DAM4SAM, SAM2Long, LVOS, lvos-evaluation | `[S5-verified]` | 仅验证存在性；适用性在 E0 解决 |

## 既定规则

1. 本项目绝不录入任何未在 Windows7 会话中检索并在此记录的文献引用。
2. `KNOWN FACT` **本方案包中的任何跟踪指标数字均非由我们亲自测得。** `README.md` 和原型输出中的所有数字均为模拟数据，其唯一目的是验证决策规则。
3. Stage 5 将仓库标记为"存在性已验证"。Stage 6 明确建议将**存在性已验证（existence-verified）**与**适用性已验证（fitness-verified）**严格区分开来；该区分由 E0 实验和访问权限核对清单解决，而非本文件。
