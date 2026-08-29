# Idea_01 — Checkpoint 清单（E0, Day 1）

**状态：模板（TEMPLATE）。以下内容尚未进行下载或哈希计算。**

本文件是实验 E0（第 1 天门禁）的输出成果。2020–2022 年代论文 checkpoint 的链接失效（link rot）是本项目最大的单一实际风险，因此归档工作优先于其他一切事务进行。

## 规则

1. 按照"先下载，再计算 SHA-256，最后镜像备份至内部存储"的顺序执行。
2. 通过 **commit SHA** 锁定代码仓库，绝不使用分支名称。
3. 若某个 checkpoint 无法获取，评测面板直接缩减并在论文中如实声明。**绝不使用重新实现的代码替代** —— 重新实现属于不同的模型，会悄然改变审计所测量的对象。
4. `KNOWN FACT` Stage 5 于 2026-08-28 将这些仓库标记为"存在性已验证"。存在性已验证并不等同于适用性已验证。本门禁正是解决该区分的地方。

## 评测面板

| 方法 | 模型家族 | 来源 | 失效风险 | 已下载 | SHA-256 | 仓库 commit | 前向传播测试 OK |
|---|---|---|---|---|---|---|---|
| BAM | specialist | OneDrive (`chunbolang/BAM`) | **HIGH** | ☐ | | | ☐ |
| HSNet | specialist | Google Drive (`juhongm999/hsnet`) | **HIGH** | ☐ | | | ☐ |
| PFENet | specialist | `dvlab-research/PFENet` (8 个模型) | low | ☐ | | | ☐ |
| Matcher | foundation | `aim-uofa/Matcher` | low | ☐ | | | ☐ |
| PerSAM | foundation | `ZrrSkywalker/Personalize-SAM` | low | ☐ | | | ☐ |
| FSSAM | foundation | `Sam1224/FSSAM` | low | ☐ | | | ☐ |
| SegGPT | foundation | HF `SegGptForImageSegmentation` | low | ☐ | | | ☐ |
| SAM / SAM2 | floor | facebookresearch 官方 | low | ☐ | | | ☐ |
| **SAM3-exemplar** | foundation | 官方, **HF-gated** | 访问审批周期 | ☐ | | | ☐ |

## SAM3 访问权限

申请日期：______
获批日期：______

此处的风险在于访问权限的审批周期，而非下载体积。即使该分支直到第 2 周才需要，也应在第 1 天立即提交申请。若未能获得访问权限，论文将使用 FSSAM/Matcher/SegGPT 维持基础模型时代的并列头条结论，并明确说明 SAM3 的缺失，而非悄然略过。

## 门禁判定结果

- 拥有已验证 checkpoint 的方法数：____ / 9
- 若 ≥ 4 则**继续推进（Continue）**。若 < 4 则**终止项目（Kill）**（开源测试工具，不发表任何内容）。
- 决策结论：______  日期：______
