# PromptAmnesia 原型 (`src/promptamnesia/`)

**状态说明：PROTOTYPE。** 本代码实现了项目包的*逻辑体系*（协议、规则、分解算法），以确保预注册的流程具备可执行性与可审计性。其中**不包含任何实验结果，亦绝不生成伪造指标**：需要模型权重或数据集的路径要么依赖真实资产，要么在 `--dry-run` / `--print-plan` / `--self-test` 模式下运行，其输出均带有明确标识的占位符或合成自测试数据。

## 模块清单

| 模块 | 实现功能 | 状态 |
|---|---|---|
| `prompts.py` | 边界框抖动、点放置、包含负点击的迭代点击协议、混合 prompt 采样器（E2/E3 协议） | 完全实现（numpy） |
| `matched_gain.py` | 单一预注册匹配增益规则（提案 §14） | 完全实现 |
| `threshold_gate.py` | 阈值扫描、对称微调、P082 噪声底线包络线、关卡决策（E1） | 完全实现（可在真实评测记录上运行；`--self-test` 使用带标签的合成数据） |
| `diversity.py` | Oracle best-of-3 与 IoU 预测头 argmax 分解（E4, C1-061） | 完全实现 |
| `eval_prompt_matrix.py` | 测试集调度管理 + 结果矩阵骨架（E3） | 调度管理已实现；模型/数据加载为存根（`--dry-run` 输出 NaN 骨架） |
| `train_lora_stub.py` | LoRA/VeRA 风格适配器、来自 `shared_grid.yaml` 的注入计划、prompt 混合 + 损失聚合连线（E2） | 适配器数学计算 + 计划已实现；训练循环为存根（需要 SAM + 数据集） |
| `splice.py` | 模块划分、双向移植、α 插值、限制容量的拼接层（E5, P177） | state-dict 逻辑已实现；拼接层拟合需要真实 checkpoint |
| `metrics.py` | 二值掩码上的 Dice / IoU 计算 | 完全实现 |

## 快速入门

```bash
# 在 Windows4/Idea_02/ 目录下运行
pip install -r requirements.txt
cd src

# 1) P082 准入关卡机制自测试（合成数据，已明确标注）
python -m promptamnesia.threshold_gate --config ../configs/p082_gate.yaml --self-test

# 2) 测试集骨架生成（NaN 占位符 — 遵守“绝不伪造指标”契约）
python -m promptamnesia.eval_prompt_matrix --config ../configs/p065_eval_battery.yaml --dry-run

# 3) 打印预注册微调网格计划（不触发实际训练）
python -m promptamnesia.train_lora_stub --config ../configs/shared_grid.yaml --print-plan
```

## 刻意**未**包含的内容

- 未下载数据集，未包含 checkpoint 权重（在路线图 Phase 0 进行哈希固定）。
- 未包含结果文件：真实运行必须写入带有 `{config_hash, seed, commit}` 溯源标识的产物，由 `eval_prompt_matrix.RunArtifact` 强制执行。
- 未包含超出预注册范围的统计指标（对比族 O1–O5 存在于配置文件中而非代码常量中，受预注册冻结约束）。
