# Idea_02 — PromptAmnesia (Windows4, Stage 7 项目包)

**一句话概述（HYPOTHESIS）：** 微调可提示分割器会按 prompt 类型非均匀地侵蚀其 zero-shot 交互能力 —— 这种性能下降顺序在混合 prompt 微调分布下依然存在（因此属于遗忘而非覆盖率不足），超出了阈值/随机种子/prompt 采样的噪声底线，包含了多掩码歧义消解能力的真实丧失（oracle best-of-3，而不仅仅是 IoU 预测头排序问题），并且在受控拼接（stitch-controlled）的模块移植实验中具有因果局部化特征。

- **捆绑论文项目：** P065（C1-065 + C1-061，旗舰论文）· P082（C1-082 + S-183，准入关卡 — **最优先运行**）· P177（S-177 + C1-062，机制分支 — **必须包含拼接对照**）。
- **继承的 Stage-4 结论：** 三个项目均为有条件 WEAK ACCEPT；P110 REJECT → 转化为报告面板附录；P108 REJECT → 表征漂移仅作为免费协变量记录。详见 `selection_history/stage4_r2_setB.md`。
- **Stage-6 锁定：** `selection_history/stage6_battle.md` — 最终 3 个项目中的 Idea_02。

**全包认识论状态说明：** PROPOSAL。**尚未运行任何实验；本目录下的任何指标均非实测数据。** 所有数字均为设计参数、预注册阈值或计算量 ESTIMATES。原型在 `--dry-run` 模式下生成的结果文件按设计规范包含 NaN 占位符。

## 具有约束力的既定义务（契约 — 放弃任何一项将导致 Stage-4 结论回退为 REJECT）

1. **混合 prompt 微调列（Mixed-prompt FT column）**是所有关于“遗忘”主张的唯一依据；仅边界框微调列仅用于绘制覆盖率图谱。
2. **Oracle best-of-3 与 argmax 分解**承载关于多样性丧失的主张；若仅为排序损失结果则转交至姊妹论文 P031。
3. **P177 拼接对照（Stitching controls）**：训练仿射拼接层、双向移植、仅拼接校准单元、逐模块 α 插值、更新范数核算。
4. **P082 最优先运行**：对称阈值协议、针对具名被质疑模型仅使用官方公开发布的 checkpoint、预注册目标列表、包络线关卡决定 PROCEED 还是 PIVOT。
5. 实验网格配方 + 匹配增益规则（matched-gain rule）单次预注册，在进行任何分析前冻结（标签 `idea02-prereg-v1`）。

## 项目包内容清单

| 路径 | 内容 |
|---|---|
| `proposal.md` | 完整的 28 节研究提案 |
| `literature.md` | 文献综述 — 引用继承自 Stage-3/4 验证，保留 `[V]`/`[M]` 标签；绝无新增/伪造引用 |
| `experiments.md` | 协议级实验设计 E0–E5（关卡、网格、测试集、多样性、模块移植） |
| `reviewer_attacks.md` | 继承的 Stage-4 评审攻击 + 新的 Stage-7 攻击，每项均配有消解实验或诚实让步 |
| `roadmap.md` | 依依赖关系排序的阶段、退出关卡、GPU-day 估算、转向分支 |
| `mermaid.md` | 流水线、析因设计、多样性决策树、模块移植网格、项目组合关系图 |
| `configs/` | 机器可读的预注册草案：`shared_grid.yaml`, `p082_gate.yaml`, `p065_eval_battery.yaml`, `p177_splice.yaml` |
| `src/` | 原型代码：LoRA 训练存根、prompt 类型评测矩阵、阈值扫描关卡、prompt 采样器、oracle 差距计算、模块移植/拼接、匹配增益规则 |
| `requirements.txt` | 原型运行所需的 Python 环境配置 |

## 执行顺序（具约束力）

`P082 关卡 → 网格冻结 → P065 测试集 → (P031 姊妹项目) → P177 机制分支` — 详见 `roadmap.md`。
关卡 PIVOT 转向分支：通缩型论文（包络线 + 对称重评估 + 验证性耦合回归），约 5–8 GPU-days。

## 快速入门（原型）

```bash
# 在 Windows4/Idea_02/ 目录下运行
pip install -r requirements.txt
cd src
python -m promptamnesia.threshold_gate --config ../configs/p082_gate.yaml --self-test
python -m promptamnesia.eval_prompt_matrix --config ../configs/p065_eval_battery.yaml --dry-run
python -m promptamnesia.train_lora_stub --config ../configs/shared_grid.yaml --print-plan
```

关于哪些已实现与哪些为存根，请参阅 `src/README.md`。自测输出为带有明确标签的合成数据；dry-run 矩阵包含 NaN 占位符（遵守绝不伪造指标的契约）。
