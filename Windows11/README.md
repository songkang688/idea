# Windows11 — Autonomous Research Idea Evolution

- **Windows 编号:** Windows11
- **创建日期:** 2026-08-28 (UTC)
- **Supervisor / PI:** Windows11
- **仓库:** `github.com/songkang688/idea`
- **Branch:** `cursor/windows11-p0-init-c0c1`
- **当前状态:** initialized（Stage 1 尚未开始产出 Idea）

本轮只写入 `Windows11/`。扫描确认：当前工作区 `main` 顶层无历史 Windows 目录；远程 heads / PR 上已有 Windows2、Windows3、Windows4、Windows6、Windows8、Windows9、Windows10。最大编号 **N=10**。本轮新建 `Windows11`，未覆盖任何旧 Windows。用户指定本窗口身份为 Windows11，与 `Windows{N+1}` 一致。后续阶段必须保持该编号，不得中途切换。

## 本轮目标

从大规模 Idea 探索中，经可证伪筛选，得到 **3** 个可执行研究包（Research Packages）。优先新 observation / 可证伪假说 / failure mode，禁止架构拼装式伪创新。

## 研究方向

**第一优先级:** Vision Foundation Models；Multimodal / Vision-Language Large Models；大模型微调；PEFT / LoRA / Adapter；SAM 系列及其微调、适配、改进；Image Segmentation；Medical Image Segmentation；Smoke / Fire / Transparent or Ambiguous Object Segmentation；Object Detection。

**第二优先级:** Medical VFM；Domain Adaptation；Few-shot / Zero-shot Segmentation；Prompt Learning；Weak / Semi / Self-Supervised Learning；Synthetic Data；Representation Learning；VLM for Dense Prediction；Robustness / Calibration / Uncertainty；Cross-domain Transfer。

允许扩展到超分、修复、扩散/生成、LLM/Agent，但禁止为迎合方向制造伪创新。

## Pipeline

`1000+ -> 200 -> 50 -> 20 -> 5 -> 3`

## 当前状态

| 项 | 值 |
|----|----|
| Stage | Stage 1（目录已初始化，Idea 计数 = 0） |
| total_ideas | 0 |
| survivors | 0 |
| final_target | 3 |
| status | initialized |

## 下一步

运行 **P1**：Stage 1 大规模 Idea 探索（独立检索、失败模式、可证伪假说）。不得把本 README 中的占位写成已完成研究。

P1 子 Agent 仍应使用 `claude-fable-5-thinking-xhigh`。P0 派发因 Fable 数据保留政策未确认而失败；需在 Cursor Dashboard 批准该政策后再派生云端子 Agent。
