# SeeingInside — 路线图（Roadmap）

执行顺序按照每 GPU 小时的信息增益（information-per-GPU-hour）排列，而非按日历时间排列。每一步均明确了准入关卡（gate）：即必须满足什么条件才能继续推进。备选方案依据 `stage4_top20.md`：P063 RefractionFeatures，P079 MemoryProbe。

## Phase 0 — 测试脚手架验证（CPU，在本包中完成）

- [x] 原型测试脚手架：数据集、干预手段、零假设模型、评价指标、决策逻辑（`src/`）。
- [x] **E0** 存根验证：BoxFillBaseline 必须被判定为 "interpolator"，OracleThreshold 存根必须被判定为 "seeing"（ACTUAL 冒烟测试输出记录在 `experiments.md` 中）。
- [x] 阈值 τ1–τ3、分层方案、随机种子在 `configs/default.yaml` 中冻结（此 commit 早于任何真实 SAM 前向传播 — 此即预注册）。
- **准入关卡（Gate）：** E0 通过两个存根模型的分类检查。→ PASSED（见 `experiments.md` §E0）。

## Phase 1 — 真实模型接入（首次 GPU 运行会话）

- [ ] 安装 `segment-anything`，获取 ViT-B + ViT-H 权重；接入 `OfficialSAMWrapper`（接口已定义在 `src/model_sam.py` 中；无需重构代码）。
- [ ] 黄金测试集检查：20 个 COCO 实例，完整（intact）条件 — Dice 处于已发表的 GT 边界框 prompt 的合理区间内（仅作合理性检查，不设硬性阈值）。
- [ ] 冻结两个实例列表（500 个 COCO / 500 个医学图像）并提交。医学图像队列选择依据提案 §14（对比度最低的两个十分位数，MedSAM 协议数据集）。
- [ ] 选择并验证扩散 inpainter；运行质量筛选；将工具引用提交至 `literature.md`（延后引用槽位）。
- **准入关卡（Gate）：** 黄金测试集通过合理性检查；反事实质量筛选拒绝率 < 30%（否则在消耗 E1 计算量之前更换 inpainter）。

## Phase 2 — E1 杀手级实验（Killer experiment，约 2–3 GPU-days）

- [ ] 生成反事实缓存（目标去除 + 目标替换，共 1000 个实例）。
- [ ] 为每个领域训练学习型 box→mask 零假设模型（`src/train.py`，< 1 GPU 小时）。
- [ ] 运行完整的 条件 × padding 网格实验，医学图像优先（`src/eval.py`）。
- [ ] 计算 CSG、persistence、swap-tracking、NRF 及 Bootstrap 置信区间；按分层应用预注册的合取判定规则。
- **准入关卡（Gates，预注册且具约束力）：**
  - **KILL：** 若在*每个*分层中 intact 与反事实之间的差距均 > 15 个 Dice 点 → 撰写负面结果简报；升级备用方案 P063/P079；终止本项目。
  - **INSTRUMENT-KILL：** 若 sham-inpaint 导致 Dice 变化 > τ1/2 → 回退为仅使用 swap；若经典工具与扩散工具在判定结论上冲突 → 报告工具失效；终止。
  - **PIVOT-1：** 若在医学图像上普遍出现 NRF > 1 → 重新调整范围为评测协议退化审计论文。
  - **PROCEED：** 若在低对比度医学图像分层中满足 H1 合取条件 → 进入 Phase 3。

## Phase 3 — 巩固与扩展计划（约 4–6 GPU-days）

执行顺序固定；在算力紧张时优先放弃后方项目：

1. **E2** 次要收敛性检验（patch-shuffle S-604，embedding-mean S-014，噪声）— 已降级的探针，用于判定合取条件中的收敛行。
2. **E4** 解耦分析：padding vs 消融膨胀；现实边界框（宽松框）分支；点 prompt 分支。
3. **E3** 机制分布图（Regime map）：对比度 × 实心度 × 尺寸空间上的 CSG/NRF 曲面。
4. **E5** 模型泛化性：ViT-B/L/H；MedSAM checkpoint（EXPECTED：更高的 NRF）；SAM-2 图像模式（若接入简便）。
5. **E6** 实验工具稳健性：第二种扩散 inpainter；在全量数据集上运行经典算法分支。
6. **E7** 替换内容梯度：同类别 / 跨类别 / 纯纹理替换。

- **撰写论文准入关卡（Gate to writing）：** E2 收敛性行完成，且 E4 解耦清晰（未推翻 E1 的判定结论）。E3/E5–E7 用于丰富论据，但不能推翻预注册的主张。

## Phase 4 — 论文撰写与开源发布

- [ ] 论文：若仅在 H1-医学图像成立，则以医学为主线叙事（投往 MICCAI 周期）；若机制分布图在跨领域表现丰富，则采用视觉顶级会议框架（CVPR/ICCV 级别）。
- [ ] 开源发布：测试脚手架 + 冻结的实例列表 + 反事实生成脚本 + 逐实例结果表 + 零假设模型权重（提案 §25）；受版权限制的医学反事实数据以脚本/哈希形式发布。
- [ ] 代码库规范：报告的每个数字均可追溯至产物目录中的结果 JSON；EXPECTED→ACTUAL 标签仅能通过提交的结果文件进行转换。

## 既定常驻规则

- Phase 0 之后严禁变动阈值（此 commit 即为预注册）。
- 流形外探针绝不作为核心宣传点（R2 义务）。
- 无论何种立意压力，严禁与 P107v/HalluSegBench 合并（Stage-6 裁定）。
- 若因工具原因（而非假设原因）连续两个关卡失败，项目将退回 Windows4 主管进行备选方案替换，而不进行超过一次尝试的工具考古。

## 依赖关系图

```
Phase 0 (完成) ──► Phase 1 接入准备 ──► E1 杀手级实验 ──┬─ KILL ──► 负面结果简报 + 备用方案
                                                        ├─ PIVOT-1 ──► 评测协议退化审计
                                                        └─ PROCEED ──► E2 ─► E4 ─► E3/E5/E6/E7 ─► 论文撰写
```
