# 演化总结

- Stage 1 完成：**1080 原始 / 1062 有效**（S + A–F + D 的富余部分）。
- 第一波超时通过紧凑波次 + supervisor 播种得到补救。
- Stage 3 廉价 killer 的 prior-work 攻击：**已完成**。保留 2、变异 3、杀掉 6。对 5 个存活者做 Reviewer #2：**已完成**。
- Stage 2 DE：**64/160 存活**。Top-10 刺客环节：**已完成**（保留 E-009、D-008、D-060；杀掉 E-035/E-041/E-057/D-067）。
- Stage 4 Reviewer #2（cheap-5）：AMG 聚类、相机 ID、对齐税**存活**；空切片 FPR 审计与 atlas-vs-text 被**杀掉**。
- 暂定 package 位于 `Idea_01`–`Idea_03`（仅有合成原型）。
- Stage 5 云端工程化 + DE 刺客 + 审计员：**工作确实做了，但当时从未落成文件** —— 由 W6-T1 事后重建为 [`stage5_top5.md`](stage5_top5.md)。Day-1 预算约 2 / 约 10 / 约 8 GPU-h —— 这些是 **HYPOTHESIS**（预算估计），**不是实测运行时间**。Idea_01 上做 COCO 对照；Idea_02 上做等 N 划分；Idea_03 上做 O1/O2/O3 的格式 vs 表征对比。
- Stage 6 battle：由 W6-T2 事后裁决，成文为 [`stage6_battle.md`](stage6_battle.md)。5 → 3 已确认（Final 3 未变）。**结论：Final 3 仍为 PROVISIONAL，尚未锁定** —— GATE-A/B/C 未关闭，GATE-D 已由 W6-T3 关闭。当时从未发生过 Stage-6 辩论事件；该裁决是从四次有记录的 rejector 环节（两次 Stage-3 刺客、Reviewer #2、元审计员）重建出来的。
- 裁决计数更正：上面那行写的 *"Keep 2, mutate 3, kill 6"* 合计为 11，但 `stage3_prior_work_kill_cheap.jsonl` 里有 **12** 条记录 —— 应为保留 2、**变异 4**、杀掉 6。那个"3"只数了进入 cheap-5 的变异项，把 `F-012-samhq-vs-filter` 静默漏掉了。已作为 INCONSISTENCY-04 记录在 `stage5_top5.md` §5。
