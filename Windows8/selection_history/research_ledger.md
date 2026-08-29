# Windows8 研究总账（final）

**Stage：** 7–8 已完成归档。实验未在真实 SAM 上跑过。

**池子：** `selection_history/raw/pool.jsonl` 中有 2766 条原始 ID

**头部候选：** 已打包的 Idea_01、Idea_02、Idea_03。

## 新颖性状态

- Idea_01：剩余新颖性 = 因果部位（编码器 vs objectness 接口）。信心中等。
- Idea_02：剩余新颖性 = PEFT 特征差的谱 + HP vs rank。信心中偏低（主要是会议契合度问题）。
- Idea_03：剩余新颖性 = SAM IoU 头的反校准现象。信心中等；E0 一出结果就可能死。

## 主要风险

云端 agent 失败；数据集／checkpoint 缺失；probe 类与校准类论文被 desk-reject。

## 存活理由

见 `evolution_summary.md` 与 `eliminated_ideas_summary.md`。
