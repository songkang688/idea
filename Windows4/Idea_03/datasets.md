# AlphaSmoke — 数据集与 Checkpoint 资源清单

状态说明：INVENTORY。在运行手册步骤 R0 执行之前，获取/许可状态列均标记为 **UNVERIFIED**；以下内容均不代表下载已成功。本项目包不重新分发任何第三方数据集。

## 1. 烟雾 — 目标领域

| 数据集 | 角色与用途 | GT 类型 | 来源文献（标签） | 获取状态 |
|---|---|---|---|---|
| DS01–DS03（Yuan et al. 合成烟雾） | Part A 次要终点；Part B 合成 alpha τ 分支 | **alpha**（合成图像） | arXiv:1809.00774 / Neurocomputing 2019 `[S3]` | UNVERIFIED（作者主页 / 依申请获取） |
| SMOKE5K | Part A 主要终点（真实划分）；Part B 模型池评分；标注员研究 | 二值（+ 带有透射率引导的生成来源） | Yan et al., AAAI 2022 `[S3]` | UNVERIFIED（依据 Stage-3 记录为公开可用） |
| SSD（Stage-3 标注上限计划中所用烟雾分割数据集） | 标注员研究；上限对抗对照 | 二值 | 依据 `stage3_kill_medical_smoke.md` §8 `[S3]` | UNVERIFIED |
| AusSmoke / MultiNatSmoke | 主要终点（若许可通过）；上限对抗对照性能差距（1–3 个 IoU 点） | 二值 | arXiv:2604.23542 `[V]` | UNVERIFIED |
| FIgLib（固定铁塔野火监控序列） | 实测 alpha 采集数据源（烟雾发生前的背景帧） | 序列，事件级标注 | Dewangan et al., Remote Sensing 14(4):1007, 2022 `[S3]` | UNVERIFIED（依据 Stage-3 记录为公开可用） |
| **AlphaSmoke-Measured（自建新数据集）** | Part B 支柱 2；Part A 第三终点 | 通过背景反演获取的**实测 alpha** + 有效性/敏感性掩码 | 本项目包，`configs/alpha_capture.yaml` | 待实测采集（实验室 + 基于 FIgLib 衍生） |

## 2. 抠图 — 预训练端（分支 M / MB）

| 数据集 | 角色与用途 | 备注说明 | 获取状态 |
|---|---|---|---|
| P3M-10k | 抠图预训练语料 | 人像抠图；隐私保护人脸；必须核查预训练用途的许可条款 | UNVERIFIED `[M — 待核验数据集卡片]` |
| AIM-500 | 抠图预训练语料 | 自然物体抠图 | UNVERIFIED `[M]` |
| Composition-1k / Adobe DIM | 抠图预训练语料（可选） | **受许可限制（依申请获取）**；若无法获取则舍弃并如实报告语料构成 | UNVERIFIED `[M]` |
| Distinctions-646 | 抠图预训练语料（可选） | 注意事项同上 | UNVERIFIED `[M]` |

分支 MB 使用**完全相同**的图像集，仅将 alpha 在 0.5 处进行二值化阈值处理（B1）。实际使用的语料库将在论文中冻结并完整列出；若有任何语料库未通过许可审核，M 与 MB 将同步缩减，以保持 M/MB 对比实验的严格一致性。

## 3. 分割 — 预训练端（分支 S / S+cal）

| 数据源 | 角色与用途 | 备注说明 | 获取状态 |
|---|---|---|---|
| COCO（实例/语义） | 分支 S 受控预训练 + 样本量匹配子集（B8） | 标准开源条款 | UNVERIFIED |
| 匹配骨干网络的公开分割 checkpoint（例如 SAM ViT-B 图像编码器 `[M]`, ViTDet-COCO `[M]`） | 分支 S 公开 checkpoint 单元格；探针编码器 (b) | 承认存在规模混淆因素；以受控单元格承载核心主张 | UNVERIFIED |
| 用于 S+cal 预测头校准的通用（非烟雾）合成图像 | B7 对照实验 | 由分割语料图像 + 随机软掩码合成构建；配方见 `configs/pretrain_arms.yaml` | 本地生成，无需下载 |

## 4. Part-B 模型池 Checkpoint 候选（目标 8–12 个；最终列表在 R3 冻结）

| 候选模型 | 入选原因 | 标签 |
|---|---|---|
| Yan et al. AAAI 2022 模型 (SMOKE5K 系列) | 领域经典基线，评测协议发源 | `[S3]` |
| FoSp (AAAI 2024) | 当前 SMOKE5K 评测协议保持者 (mMse+Fβ) | `[V]` — 权重可用性 UNVERIFIED |
| SFMattingNet (Remote Sensing 2025) | **B9 强制项** — 抠图转向代表模型 | `[V]` — 权重可用性 UNVERIFIED |
| Yuan et al. 系列 (DS0x) | 合成 alpha 时代代表模型 | `[S3]` — 可复现性 UNVERIFIED |
| MAM (Matting Anything) | 冻结 SAM 上的抠图基础大模型预测头 | `[S3]` |
| SAM (自动模式 / 网格点模式，经阈值输出) | 通用分割代表模型 — **B10: 严禁检测器提示** | `[M]` 代码公开 |
| CoSW (NeurIPS 2024) | 标签噪声感知烟雾模型 | `[S3]` — 权重 UNVERIFIED |
| Part-A 各分支 (M, MB, S, S+cal, 0) + 物理底线模型 (DC, HSV) | 内部模型池成员 | 本文构建 |

模型池入选规则（预注册）：任何无法在 R3 之前获取官方开源权重或复现的候选模型，均在论文中列为“尝试获取但不可用” —— 严禁隐瞒舍弃。

## 5. 已发表性能差距总账（用于标注员上限正面对照，B5）

将在 R0 阶段通过按基准整理各连续 SOTA 主张之间所报告的指标差值进行填报（起始集合：AusSmoke/MultiNatSmoke 表格 `[V]`，来自 FoSp `[V]` 的 SMOKE5K 排行榜条目）。保存为 `configs/eval_protocol.yaml → published_deltas`，每行对应一条可验证的文献引用。**绝不凭空编造任何性能增量；每行必须附带可核查的来源，否则不予收录。**
