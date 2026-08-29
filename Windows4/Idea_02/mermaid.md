# PromptAmnesia — 架构图（Windows4 / Idea_02）

认识论状态说明：DESIGN DIAGRAMS。此处未包含任何实验结果。

## 1. 带有准入关卡决策的研究流水线

```mermaid
flowchart TD
    E0["E0 预注册冻结<br/>网格配方 · 匹配增益规则 · 对比族 O1–O5<br/>关卡目标 · 探针协议 · 点击模拟器<br/>标签: idea02-prereg-v1"]
    E1["E1 P082 准入关卡 (最优先运行，仅评测)<br/>冻结模型方差分解<br/>对称阈值协议<br/>仅使用公开发布的 checkpoint (MedSAM, SAM-Med2D)"]
    DEC{"关卡决策：<br/>在 ≥2 个领域上是否有可复现的差值<br/>超出噪声包络线？"}
    PIV["PIVOT — Branch A (通缩型论文)<br/>包络线 + 对称重评估<br/>+ 验证性耦合回归<br/>(共约 5–8 GPU-days)"]
    E2["E2 共享微调 Checkpoint 网格 (唯一训练阶段)<br/>2 领域 × 3 prompt 混合 × 4 配方 × ≥3 种子<br/>+ 损失聚合单元格 + 协变量记录"]
    MG["匹配增益筛选 (§14，单一规则)<br/>首个处于最弱分支最佳值 ±0.5 Dice 内的 checkpoint"]
    E3["E3 P065 测试集<br/>边界框 · 1点 · 迭代5点(含负点) · 歧义<br/>对称阈值 · 双点击模拟器"]
    E4["E4 多样性分支 (C1-061)<br/>oracle best-of-3 vs IoU 预测头 argmax"]
    E5["E5 P177 机制分支<br/>模块移植 × 训练拼接 × 双向<br/>+ 逐模块 α 插值"]
    P5["Phase 5 综合分析与论文撰写<br/>报告面板附录 (P110 残留)<br/>表征漂移协变量探索 (P108 残留)"]

    E0 --> E1 --> DEC
    DEC -- "否 (均在包络线内)" --> PIV
    DEC -- "是" --> E2 --> MG --> E3 --> E4 --> E5 --> P5
    E3 --> P5
    PIV --> P5
```

## 2. P065 析因设计 — 覆盖率与遗忘的解耦分离

```mermaid
flowchart LR
    subgraph FTMIX["微调 prompt 混合 (列)"]
    BO["仅边界框 box-only<br/>(覆盖率列)"]
    PO["仅点 point-only<br/>(覆盖率列)"]
    MX["混合 MIXED<br/>(授权列 —<br/>所有主张均在此确立)"]
    end
    subgraph BATTERY["评测测试集 (行)"]
    B1["边界框 (带抖动)"]
    B2["1 次点击"]
    B3["迭代 5 次点击 (含负点击)"]
    B4["多掩码歧义<br/>(oracle vs argmax)"]
    end
    FTMIX -->|"× 配方 {全量微调 ×3 LR, 仅解码器微调, LoRA 编+解, VeRA 对照}<br/>× ≥3 种子 × 2 领域，在匹配增益下"| BATTERY
    BATTERY --> DELTA["对称微调阈值下<br/>相对于冻结 SAM 底线的 Δ(prompt 类型)"]
    DELTA --> CVG["仅边界框 / 仅点列的排序<br/>= 覆盖率图谱 (RQ5)"]
    DELTA --> FGT["混合列排序 O1–O3, O5<br/>+ 包络线 + Holm 校正 = 遗忘 (H2/H3)"]
```

## 3. 多样性分解决策树 (C1-061)

```mermaid
flowchart TD
    P["歧义探针: 3 个候选掩码 + IoU 预测头得分<br/>每个 prompt 包含 ≥2 个有效 GT 掩码"]
    Q1{"微调后 Oracle best-of-3<br/>是否下降？<br/>(包含 all-mask-loss 单元格)"}
    Q2{"Argmax 是否下降？"}
    Q3{"是否仅在<br/>min-loss-mask 单元格中下降？"}
    CAP["能力丧失 (CAPABILITY LOSS)<br/>多样性遗忘主张成立 (H4)"]
    RNK["排序损失 (RANKING LOSS)<br/>转交至 P031 (IoU 预测头失步)；<br/>从本文中撤回"]
    ART["损失聚合人工伪影 (LOSS-AGGREGATION ARTIFACT)<br/>作为配方发现报告，非遗忘"]
    NUL["无多样性效应 —<br/>作为零假设报告"]

    P --> Q1
    Q1 -- 是 --> Q3
    Q3 -- 是 --> ART
    Q3 -- 否 --> CAP
    Q1 -- 否 --> Q2
    Q2 -- 是 --> RNK
    Q2 -- 否 --> NUL
```

## 4. P177 移植 / 拼接网格

```mermaid
flowchart TD
    subgraph MODULES["模块组 (每次替换一个)"]
    M1["图像编码器"]
    M2["Prompt 编码器"]
    M3["解码器交叉注意力"]
    M4["解码器其余部分 + 各预测头"]
    end
    subgraph CONTROLS["每单元格对照设置"]
    C1["双向移植<br/>(微调前→微调后 及 微调后→微调前)"]
    C2["有/无训练仿射拼接<br/>(严格限制容量，2 种预注册类型)"]
    C3["仅拼接校准单元格"]
    C4["逐组 α 插值<br/>α ∈ {0, .25, .5, .75, 1}"]
    C5["更新范数核算 +<br/>范数匹配微调分支"]
    end
    MODULES --> R["每单元格、每 prompt 类型的恢复比例 R<br/>R = (嵌合体 − 微调后) / (冻结 − 微调后)，Bootstrap 置信区间"]
    CONTROLS --> R
    R --> V{"cross-attn+stitch ≫ encoder+stitch，<br/>双向均成立且超出 α 曲线？"}
    V -- 是 --> H5Y["H5 成立：机制级定位确立"]
    V -- 否 --> H5N["定位主张撤回；<br/>描述性报告网格与 α 曲线"]
```

## 5. 项目组合接口与执行顺序

```mermaid
flowchart LR
    P082["P082 准入关卡<br/>(本包，优先运行)"]
    GRID["共享 Checkpoint 网格<br/>(预注册，冻结)"]
    P065["P065 测试集 + C1-061 多样性<br/>(本包，旗舰项目)"]
    P031["P031 IoU 预测头失步 / 校准<br/>(姊妹论文)"]
    P177["P177 机制分支<br/>(本包)"]
    P110["P110 残留：<br/>报告面板附录"]
    P108["P108 残留：<br/>表征漂移协变量日志 (免费)"]

    P082 --> GRID --> P065 --> P177
    GRID --> P031
    P065 -- "O4 的排序损失分支" --> P031
    P065 --- P110
    GRID --- P108
```
