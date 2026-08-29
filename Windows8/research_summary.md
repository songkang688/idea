# Windows8 研究总结

**日期：** 2026-08-28  
**Supervisor：** Windows8  
**原始想法数：** 2766（≥1000）  
**Final 3：** Idea_01 Objectness-not-features；Idea_02 Spectral PEFT；Idea_03 Selective IoU tokens

## 首推

**Idea_01 — Objectness, Not Features。**

killer 实验最便宜，改变"人们把 PEFT 参数花在*哪里*"的机会最大，而且它没有以 Med-SA / fire-box 评测 / CD-concept 评测的形式被发表过。它带有一个精确的交互假设（在无定形目标上赢、在 COCO 上输）。

## 第一个要跑的实验

`Idea_01` E0：缓存冻结的 SAM embedding；在一个无定形数据集加一个 COCO 对照上，训练一个 1×1 密度头去对比用 GT 框提示的 SAM。toy 回路：`Idea_01/src/train_density_head.py`（用 FakeEncoder，**不是**科学结果）。

## 三者的状态

| ID | 科学内容 | 代码 | 图 | 文献攻击 |
|----|---------|------|---------|-------------------|
| 01 | 完整 package | 可运行原型 | mermaid | 有 |
| 02 | 完整 package | FFT toy | mermaid | 有 |
| 03 | 完整 package | reliability toy | mermaid | 有 |

## 未解风险

- 云端子 Agent 失败或挂起；池子是 Supervisor 用 52 个 core × 变异生成的（有记录），外加 10 条手工 idea。
- 烟雾数据集的许可与 SAM checkpoint 都不在这台 VM 上。
- 如果省掉 COCO 交互对照，Idea_01 会被当成 probe paper 直接拒（desk-reject）。
- Idea_02 可能被说"不算 CV"。
- 如果 E0 显示没有校准域差，Idea_03 就直接死。
