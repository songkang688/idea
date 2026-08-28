# Windows15 — Autonomous Research Idea Evolution

- **Windows 编号:** Windows15
- **创建日期:** 2026-08-28 (UTC)
- **Supervisor / PI:** Windows15
- **仓库:** `github.com/songkang688/idea`
- **Branch:** `cursor/windows15-p0-init-implementation-4708`
- **当前状态:** initialized（Stage 1 尚未开始产出 Idea）

本轮只写入 `Windows15/`。身份指令：本窗口固定为 **Windows15**，后续阶段不得改号；window_defined_by = P0，window_definition_status = canonical。

**KNOWN FACT（编号扫描，本实现 Agent 自扫，git fetch origin --prune @ 2026-08-28T17:48:58Z，74 origin refs）：**

- 当前 `main` 顶层：`README.md`、`Windows1/`（已合并的 Windows 1 最终成果）、`research_ledger/`。
- 远程 origin heads 上已有顶层 Windows 目录：Windows1（main）、Windows2、Windows4、Windows6、Windows8、Windows9、Windows10、Windows11、Windows12、Windows13、Windows14、Windows16。
- Windows3 仅以嵌套 `staging/Windows3_supervisor/` 存在（`origin/cursor/idea-evolution-windows3-b534`、`origin/cursor/w3s1-cluster-b-7ea7`），编号已烧毁；另有嵌套 `research_ledger/windows1/`（main 与 `origin/cursor/seg-0276-m-stage5-f84d`）。
- Windows13 / Windows14 / Windows16 均已由并行姊妹 pipeline 实现并写入 `window.lock.json`（分别声明 13 / 14 / 16）。
- 全部 origin heads（任意大小写/嵌套路径、分支名、window.lock.json 声明、research_state.json windows_id 声明）均未发现 **Windows15**。
- 缺号：Windows5、Windows7（从未在任何 ref 上以任何拼写存在；惯例严格单调递增，永不回填）；Windows1/5/7 永不复用。
- 已存在最大编号 **max_n = 16**。本轮编号 **Windows15** 由本 pipeline 的 canonical 决策文件 `_dispatcher/p0/wave_b/decision.json`（Wave B，3/3 judge 一致同意）指定：15 是本 pipeline（父 dispatcher 身份 Windows15）预留的编号，姊妹 pipelines 已分别取走 13/14/16 并在其锁文件中把 15 记为本 pipeline 所有（never_take: 15）。Windows15 不存在于任何 ref，创建不会覆盖历史研究。
- 锁定协议：mkdir 前与写 `window.lock.json` 前各执行一次 `git fetch origin --prune` 并全量复扫（两阶段均通过，Windows15 始终缺席）。

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
