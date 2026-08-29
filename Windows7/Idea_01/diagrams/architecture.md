# Idea_01 — 协议与数据流（Protocol and Data Flow）

本项目中没有模型架构。此处的"架构"即测量装置本身，因此这些图表展示的是干预流程与决策规则，而非神经网络。

---

## 1. 逐 episode 的反事实干预

```mermaid
flowchart LR
    subgraph IN["Episode（推理前已冻结）"]
        S["正确 support<br/>类别 c 的 (I_s, M_s)"]
        Q["Query I_q<br/>GT 掩码 M_q"]
        W["错误 supports S'<br/>2 个近类 + 3 个远类<br/>类别经核验在 Q 中严格不存在<br/>面积匹配在 ±50% 范围内"]
    end

    S --> F1["f(S, Q)"]
    W --> F2["f(S', Q)"]
    Q --> F1
    Q --> F2
    Q --> G["无 support 的下界 g(Q)<br/>Floor-A: SAM AMG (强)<br/>Floor-B: 显著性 (弱)"]

    F1 --> A1["a_corr = IoU(pred, M_q)"]
    F2 --> A2["a_wrong = S' 上的中位数"]
    F1 --> V["不敏感度<br/>IoU(pred_wrong, pred_corr)"]
    F2 --> V
    G --> A3["a_floor"]

    A1 --> R["保持率 R = a_wrong / a_corr"]
    A2 --> R
    R --> SSS["SSS = 1 - R"]
    A1 --> FT["下界检验：<br/>a_corr 与 a_floor 的 CI 重叠"]
    A3 --> FT
```

下界**针对每张 query 图像仅计算一次**，并在评测面板的所有方法间复用，这也是大部分算力节省的来源。

---

## 2. 分层（Stratification）—— 区分两种不同控诉的核心部分

```mermaid
flowchart TD
    E["Query 为 Q、类别为 c 的 Episode"] --> D{"是否为退化基准？<br/>(FSS-1000)"}
    D -- 是 --> S4["S4 退化对照组<br/>此处高保持率控诉的是基准（BENCHMARK）"]
    D -- 否 --> C{"Q 中是否存在任何<br/>类别 ≠ c 的标注实例？"}
    C -- 是 --> S3["S3 存在干扰物（distractor present）<br/>主要分层（PRIMARY STRATUM）<br/>此处高保持率控诉的是模型（MODEL）"]
    C -- 否 --> M{"类别 c 的实例数是否 ≥2？"}
    M -- 是 --> S2["S2 同类多目标"]
    M -- 否 --> S1["S1 单目标<br/>此处显著性先验不可能出错"]
```

`S3` 是主要分层，因为它是"分割显著物体"与"分割 support 指定的类别"被迫产生冲突的唯一分层。此前关于前景偏差的所有讨论都将 `S1` 与 `S3` 混为一谈；而本设计将其严格区分。

---

## 3. 决策规则

```mermaid
flowchart TD
    MVE["MVE (~1 A100-day)<br/>PFENet + BAM + Matcher + 1 个基础模型时代方法<br/>PASCAL-5i f0, COCO-20i f0"]
    MVE --> GATE{"是否有任何 R > 0.35 在任一分层出现<br/>或者模型家族间差距 > 15 个百分点？"}
    GATE -- 否 --> DIE["终止。想法以 1 A100-day 成本终止。<br/>开源测试工具。"]
    GATE -- 是 --> KILLER["Killer 实验 (~2 A100-days)<br/>在分层 S3 上运行"]

    KILLER --> LA{"检验分支 (a)<br/>≥ 半数专有方法的保持率 R > 0.5"}
    KILLER --> LB{"检验分支 (b)<br/>a_corr 与下界在统计上无法区分<br/>按各下界单独报告，绝不合并"}

    LA -- 通过 --> H["头条结论：<br/>敏感度调整后的排行榜发生重排"]
    LB -- 通过 --> H
    LA -- 失败 --> BOTH{"两个检验分支均失败？"}
    LB -- 失败 --> BOTH
    BOTH -- 是 --> CERT["转而发表认证结果（CERTIFICATION result）<br/>(最弱分支，已按其实际价值定价)"]

    H --> S4C{"S4 表现高但 S3 表现低？"}
    S4C -- 是 --> BENCH["转向：基准批判论文。<br/>富含干扰物的评测划分是主要交付物。"]
    S4C -- 否 --> PAPER["模型层面的有效性控诉"]
```

---

## 4. 统计分析流水线

```mermaid
flowchart LR
    EP["逐 episode 测量数据"] --> TAU["预注册过滤规则<br/>a_corr ≥ τ（τ=0.2 预先冻结）"]
    TAU --> P["主要估计器（PRIMARY estimator）<br/>均值之比（ratio of means）<br/>Σ a_wrong / Σ a_corr"]
    TAU --> M["次要估计器（SECONDARY estimator）<br/>逐 episode 比值的中位数"]
    P --> B["episode 级 bootstrap B=10,000<br/>分子与分母在相同索引上重采样"]
    M --> B
    B --> FLAG{"|主要估计器 - 次要估计器| > 0.2？"}
    FLAG -- 是 --> BI["标记：双峰分布 episode<br/>= 硬性失效模式，作为一项发现报告"]
    FLAG -- 否 --> OK["平缓退化模式"]
```

**为什么主要估计器不能采用中位数。** 逐 episode 的保持率呈双峰分布：在错误 support 下，方法要么精准落在正确物体上，要么完全落空，因此 `R(e)` 会在 0 附近和 1 附近堆积。对这种分布取中位数等于抛硬币赌哪一堆更大。在原型运行中，完全由 support 驱动的对照组给出的中位数保持率为 1.000 —— 与无视 support 的方法完全一致 —— 而其均值之比为 0.762 [0.651, 0.871]。参见 `proposal.md` §10。
