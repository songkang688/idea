# AlphaSmoke — 文献引用总账

标签规范（继承自 Stage 3/4）：
- `[V]` — 由 Stage-3/4 评审在 2026-08-28 检索并完整阅读（依据 `stage4_r2_setC.md`）；标识符与其中记录一致。
- `[S3]` — 继承自 Stage-3 文件（`stage3_kill_medical_smoke.md`），该文件在其评审阶段宣称已完成网络验证。
- `[M]` — 凭记忆引用的经典文献或数据集卡片；**在任何草案引用之前必须重新核验标识符**。

以下任何引用均非为本包凭空编造；每一项均存在于 Windows4 筛选历史文件中，或是标记为 `[M]` 待验证的数据集/代码产物。

## 烟雾分割 / 密度估计

| 参考文献 | 标识符 / 来源 | 用于何处 | 标签 |
|---|---|---|---|
| Yuan et al., Deep Smoke Segmentation | Neurocomputing 2019 / arXiv:1809.00774 | DS01–03 alpha GT；合成 alpha 时代基准 | `[S3]` |
| Yuan et al., Wave-Shaped DNN for Smoke Density Estimation | IEEE TIP 2020 | 密度回归先例（否定本体论全新主张） | `[S3]` |
| Yan et al., Transmission-Guided Bayesian Generative Smoke Segmentation | AAAI 2022 | SMOKE5K 数据集；透射率引导机制；mMse 协议发源 | `[S3]` |
| FoSp | AAAI 2024, doi:10.1609/aaai.v38i7.28484 | SMOKE5K 上的 mMse+Fβ 评测协议（B4） | `[V]` |
| AusSmoke / MultiNatSmoke | arXiv:2604.23542 | 二值基准；1–3 个 IoU 点的 SOTA 差距供上限正面对照 | `[V]` |
| SFMattingNet | Remote Sensing 17(13):2259, 2025, doi:10.3390/rs17132259 | 该领域的抠图转向；模型池强制成员（B9） | `[V]` |
| CoSW | NeurIPS 2024 | 将烟雾标签噪声确立为已知问题 | `[S3]` |
| 高光谱烟雾数据集 (3 名标注员) | arXiv:2602.10858 | 标注员间分歧的实证证据 | `[S3]` |
| 浓度加权森林烟雾分割 (Concentration-weighted forest smoke) | Electronics 2021, doi:10.3390/electronics10212675 | 半透明度歧义研究动机 | `[S3]` |
| Dewangan et al., FIgLib & SmokeyNet | Remote Sensing 14(4):1007, 2022, doi:10.3390/rs14041007 | 用于实测 alpha 采集的固定铁塔视频序列 | `[S3]` |
| ProFSAM (Ugwu & Zhang) | arXiv:2510.21782 | 超出范围约束 B10（我们明确**不**做的工作） | `[S3]` |
| 基于 SAM 背景先验的密度感知渐进式烟雾分割 | Pattern Recognition (依据 `literature_anchors.md`) | SAM 作为先验已被探索；范围约束边界 | `[S3]` |

## 图像抠图（Matting）

| 参考文献 | 标识符 / 来源 | 用于何处 | 标签 |
|---|---|---|---|
| Li et al., Matting Anything (MAM) | CVPRW 2024 / arXiv:2306.05399 | 轻量 alpha 预测头；模型池成员；A1-046 淘汰先例 | `[S3]` |
| Yao et al., Matte Anything | arXiv:2306.04121 | 相邻技术领域 | `[S3]` |
| Rhemann et al., Perceptually Motivated Matting Benchmark | CVPR 2009 | SAD/MSE/Grad/Conn 评估指标套件 | `[S3]` |
| Medical Matting | arXiv:2106.09887 | 标注员掩码→alpha 先例 (QUBIQ) | `[S3]` |
| P3M-10k / AIM-500 / Composition-1k / Distinctions-646 | 数据集卡片 | 预训练语料库（分支 M/MB） | `[M]` |

## 物理先验 / 经典基线

| 参考文献 | 标识符 / 来源 | 用于何处 | 标签 |
|---|---|---|---|
| He, Sun & Tang, Dark Channel Prior | CVPR 2009 / TPAMI 2011 | 免训练的透射率物理底线模型（B6） | `[S3]` |
| 经典颜色规则烟雾检测家族 | — | HSV 低饱和度对照作为规则实现，核实前不引用具体论文 | `[M]` |

## 通用分割端

| 参考文献 | 标识符 / 来源 | 用于何处 | 标签 |
|---|---|---|---|
| Kirillov et al., Segment Anything | ICCV 2023 | SAM 自动模式模型池成员；分割预训练编码器选项 | `[M]`（经典文献；待核验具体格式） |
| COCO | 数据集卡片 | 分支 S 预训练语料库 | `[M]` |
| ViTDet-COCO / SAM ViT-B 编码器 checkpoint | 代码开源发布 | 探针编码器 (b)；分支 S 公开单元格 | `[M]` |

## Windows4 流程档案（内部参考）

- `Windows4/selection_history/stage3_kill_medical_smoke.md` — §7 (S-096/S-097/A1-046), §8 (S-102/A1-054), §9 (S-103), §10 (S-126), NOT-FOUND 登记册 #5–7。
- `Windows4/selection_history/stage4_r2_setA.md` — P103 评审意见（约束性条件 B1, B2, B7, B8）。
- `Windows4/selection_history/stage4_r2_setC.md` — P096 评审意见（约束性条件 B3, B4, B5; 新证据登记项 2–4）。
- `Windows4/selection_history/stage4_top20.md` — 最终 3 强锁定（Idea_03 = AlphaSmoke）。
- `Windows4/selection_history/stage6_battle.md` — 第 3 槽位决议、决定性实验 #3（线性探针）、顺序纪律。
