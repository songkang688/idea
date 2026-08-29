# Windows8 — 自主研究想法演化（Autonomous Research Idea Evolution）

- **Windows ID：** Windows8
- **创建日期：** 2026-08-28（UTC）
- **Supervisor：** Windows8（PI）
- **仓库：** `github.com/songkang688/idea`

本目录树专属于这一轮。兄弟分支上的其他 Windows 目录未被改动。

## 本轮的三个 Idea

1. **Idea_01 — Objectness, Not Features**（推荐）：在无定形目标上，用冻结的 SAM embedding + 密度／排除区对比带提示的 SAM，并配一个 COCO 对照。
2. **Idea_02 — Spectral Locality of Dense PEFT：** 假设 LoRA 的特征差在空间上是低通的；检验高频残差与增加 rank 的效果对比。
3. **Idea_03 — Selective SAM via IoU-token Recalibration：** 假设 SAM 的 IoU token 在无定形域上是反校准（anti-calibrated）的；用风险-覆盖率曲线对比 adapter。

## 最推荐

**Idea_01。** 它是推翻"微调编码器"这一默认做法的最便宜的证伪手段，而 prior work 已经占据了"仅评测"和"adapter SOTA"这两个位置。

## 理由

- 不是 Med-SA / LoRA-MedSAM（那些是方法，但没有"失效位点"检验）。
- 不是"SAM 在火焰／玻璃上失效"（已经有人评测过了）。
- killer 实验只需一个 GPU-day，而且能诚实地把整个项目杀掉。

## 项目状态

| Package | 状态 |
|---------|--------|
| Idea_01 | 可以开跑 E0（要做科学需要真实 SAM 权重；toy 训练回路可运行） |
| Idea_02 | 可以开跑 FFT 审计 |
| Idea_03 | 可以开跑 reliability dump |

## 下一个要跑的实验

Idea_01 E0（见 `Idea_01/experiments.md`）。不要把 FakeEncoder 的数字当作结果报告（Do not report FakeEncoder numbers as results）。

## 候选标题

- Objectness, Not Features: Where Segment Anything Actually Fails on Amorphous Targets
- LoRA Is a Low-Pass Adapter: Spectral Locality of PEFT for Dense Prediction
- When SAM Is Sure and Wrong: Selective Segmentation via IoU-Token Recalibration
