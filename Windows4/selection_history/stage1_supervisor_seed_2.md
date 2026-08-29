# Stage 1 导师种子创意目录续篇 (S-361–S-720)

变异、拆分及邻近领域的创意。依然是假说，而非实验结果。

| ID | OneLiner | Problem | Hypothesis | WhyNovel | MinExp | Risk | Cluster |
|---|---|---|---|---|---|---|---|
| S-361 | SAM 预测 IoU 排名 ≠ 真实 IoU 排名 | 选择 | 医学图像上 Spearman ρ << 1 | 记录现象 | 200 张图像 | 低 | SAM_PROMPT |
| S-362 | 3 个 SAM 掩码的最佳值 vs 预测最佳值 | 解码 | Oracle 多掩码差距是真实的上行空间 | 上限 | 1 个数据集 | 低 | SAM_PROMPT |
| S-363 | 细长结构点击边缘 vs 点击中心 | 协议 | 边缘点击在血管上胜出 | 几何 | 1 | 低 | SAM_PROMPT |
| S-364 | 提示位置编码中的框长宽比惩罚 | 方法？ | 倾向于不做新模块：测量失败 vs 长宽比 | 测量 | 1 | 低 | SAM_PROMPT |
| S-365 | 测试时提示条件化 Dropout | TTA | 随机提示 Dropout 集成 | 低成本 | 1 | 增量改进 | SAM_PROMPT |
| S-366 | 在超分辨率输入上运行 SAM | 超分作为预处理 | 超分对小病灶的帮助大于微调 | 预处理 | 1 | 超分领域拥挤 | SAM_PROMPT |
| S-367 | 在恢复（去噪）后的 CT 上运行 SAM | 恢复 | 去噪 > LoRA | 预处理 | 1 | 增量改进 | SAM_PROMPT |
| S-368 | JPEG 质量作为隐藏领域 | 鲁棒性 | 网络抓取的火灾视频 | 扫描质量 q | 1 | 低 | ROBUST |
| S-369 | 运动模糊 vs SAM2 记忆 | 视频 | 模糊对记忆的破坏超过空间退化 | 切片 | 1 | 低 | SAM2_MEMORY |
| S-370 | 压缩伪影作为“纹理物体” | 失败 | SAM 贴靠到压缩块 | JPEG | 1 | 低 | SAM_PROMPT |
| S-371 | 散焦作为类透明边缘 | 统一 | 散焦物体表现类似于 Alpha | 相机 | 1 | 推测性 | SMOKE_ALPHA |
| S-372 | 雨痕作为线性透明物体 | 邻近领域 |  | 1 | 增量改进 | SMOKE_ALPHA |
| S-373 | 玻璃幕墙分割 vs 烟雾 | 统一 | 相同指标 | Trans10k | 中等 | SMOKE_ALPHA |
| S-374 | 水下焦散现象 | 失败 | 水下 SAM | 1 | 场景细分 | SAM_PROMPT |
| S-375 | 伪装 vs 烟雾：纹理 vs Alpha | 分类学 | 不同的失败模式 | COD + 烟雾 | 中等 | ASSUMPTION |
| S-376 | 阴影 vs 烟雾 | 混杂因素 |  | 1 | 低 | SMOKE_ALPHA |
| S-377 | 蒸汽 vs 烟雾 | 分类学 | 厨房 vs 火灾 | 1 | 数据 | SMOKE_ALPHA |
| S-378 | 灰尘 vs 烟雾 | 分类学 |  | 1 | 数据 | SMOKE_ALPHA |
| S-379 | 镜头冷凝结露 | 传感器 |  | 1 | 场景细分 | ROBUST |
| S-380 | 火焰上的卷帘快门 | 传感器 |  | 1 | 场景细分 | FIRE_CONFOUND |
| S-381 | HDR vs SDR 火焰 | 传感器 |  | 1 | 数据 | FIRE_CONFOUND |
| S-382 | 自动曝光抽吸现象 | 视频 |  | 1 | 低 | FIRE_CONFOUND |
| S-383 | 白平衡作为领域 | 颜色 |  | 1 | 低 | DET_SHIFT |
| S-384 | 手机 vs 单反的 ISP 流水线不匹配 | 领域 |  | 1 | 数据 | DET_SHIFT |
| S-385 | 烟雾密度的超分辨率 | 逆问题 | 病态问题 | 合成 | 高 | SMOKE_ALPHA |
| S-386 | 先盲反卷积再分割 | 流水线 |  | 1 | 传统方法 | SAM_PROMPT |
| S-387 | 带有 Dice 奖励学习 CT 窗位 | 预处理 | vs 固定窗口 | 1 | 增量改进 | SAM_MEDICAL_GAP |
| S-388 | 逐患者窗口作为提示 | 提示 | 窗口向量输入 SAM | 1 | 具新颖性 | SAM_MEDICAL_GAP |
| S-389 | DICOM 标签作为侧向信息 | 元数据 | 切片位置，kVp | 1 | 数据 | SAM_MEDICAL_GAP |
| S-390 | 扫描仪厂商对抗验证 | 领域 |  | 1 | 数据 | SAM_MEDICAL_GAP |
| S-391 | 协议（增强 vs 平扫） | 领域 |  | 1 | 数据 | SAM_MEDICAL_GAP |
| S-392 | 儿科 vs 成人尺度 | 偏移 |  | 1 | 数据 | SAM_MEDICAL_GAP |
| S-393 | 植入设备作为 OOD | 鲁棒性 |  | 1 | 场景细分 | SAM_MEDICAL_GAP |
| S-394 | MRI 运动伪影 | 鲁棒性 |  | 1 | 数据 | SAM_MEDICAL_GAP |
| S-395 | 部分容积效应即为 Alpha 抠图 | 统一 | CT 部分容积 = Alpha | 1 | 有趣 | SMOKE_ALPHA |
| S-396 | 超像素提示 | 提示 | SLIC 区域作为掩码提示 | 1 | 增量改进 | SAM_PROMPT |
| S-397 | 极端学习：单像素提示 | 极限 |  | 1 | 容易 | SAM_PROMPT |
| S-398 | 全图框提示 | 极限 | 等同于显著性 | 1 | 容易 | SAM_PROMPT |
| S-399 | 随机框先验作为 SAM 基线 | 基线 |  | 1 | 容易 | SAM_PROMPT |
| S-400 | 距离变换作为额外通道 | 输入 |  | 1 | 传统方法 | SAM_PROMPT |
| S-401 | 边缘图拼接 | 输入 |  | 1 | 传统方法 | SAM_PROMPT |
| S-402 | 不要拼接：测试 SAM 是否已使用边缘 | 消融 | Sobel 引入 vs 剔除 | 1 | 容易 | ASSUMPTION |
| S-403 | SAM 前的频域滤波 | 预处理 | 高通 vs 低通 | 1 | 容易 | SAM_PROMPT |
| S-404 | 颜色抖动微调 vs 冻结 | 鲁棒性 |  | 1 | 容易 | PEFT_DENSE |
| S-405 | 测试时 MixStyle | TTA |  | 1 | 拥挤 | SYNTH_DA |
| S-406 | 来自目标的 BatchNorm 统计量 | TTA |  | 1 | 传统方法 | SYNTH_DA |
| S-407 | 来自目标的提示统计量（框大小直方图） | TTA |  | 1 | 具新颖性 | SAM_PROMPT |
| S-408 | SAM 在翻转下的自一致性 | TTA | 翻转平均 | 1 | 容易 | SAM_PROMPT |
| S-409 | SAM 的 90 度旋转不变性 | 等变性 |  | 1 | 容易 | SAM_PROMPT |
| S-410 | 尺度金字塔 SAM | TTA |  | 1 | 增量改进 | SAM_PROMPT |
| S-411 | 带有重叠共识的分块 SAM | 大图像 | 病理 | 1 | 工程 | SAM_MEDICAL_GAP |
| S-412 | WSI 十亿像素提示协议 | 问题 |  | 1 | 数据 | SAM_MEDICAL_GAP |
| S-413 | 细胞重叠作为互斥约束 | 问题 |  | 1 | Cellpose 已存在 | SAM_MEDICAL_GAP |
| S-414 | 染色归一化作为提示 | 预处理 |  | 1 | 传统方法 | SAM_MEDICAL_GAP |
| S-415 | IHC vs H&E 领域 | 偏移 |  | 1 | 数据 | SAM_MEDICAL_GAP |
| S-416 | 冻结病理 VFM + SAM 解码器 | 混合 | UNI 特征输入 SAM | 繁重 | 拥挤 | SAM_MEDICAL_GAP |
| S-417 | 不要融合：线性探测 UNI vs SAM | 基线 |  | 1 | 容易 | ASSUMPTION |
| S-418 | 放射学报告转为边界框再输入 SAM | 流水线 |  | 1 | 拥挤 | VLM_DENSE |
| S-419 | 报告否定句处理 | 语言 |  | 1 | 重要 | VLM_DENSE |
| S-420 | VLM-SAM 中的左右侧性错误 | 安全性 |  | 1 | 重要 | VLM_DENSE |
| S-421 | 提示中的测量 token (mm) | 语言 |  | 1 | 有趣 | VLM_DENSE |
| S-422 | 计数问题 vs 掩码 | 任务 |  | 1 | 邻近领域 | VLM_DENSE |
| S-423 | 掩码质量上的视觉问答 | 评估 |  | 1 | 风险大 | VLM_DENSE |
| S-424 | LLM 编写实验配置 | 元实验 | 超出范围（除非是失败研究） | — | 低 ROI | NEG_RESULT |
| S-425 | 智能体标注者 vs 人工时间 | HCI |  | 成本 | 偏软性 | FEWSHOT |
| S-426 | 带有提示分歧的主动学习 | AL |  | 1 | 增量改进 | SAM_PROMPT |
| S-427 | 批量 AL vs 顺序点击 | AL |  | 1 | 拥挤 | FEWSHOT |
| S-428 | SAM 嵌入中的 Core-set 采样 | AL |  | 1 | 拥挤 | FEWSHOT |
| S-429 | 遗忘 OOD 医院的主动学习 | AL |  | 1 | 有趣 | FORGETTING |
| S-430 | 掩码上的标签平滑 | 训练 |  | 1 | 传统方法 | PEFT_DENSE |
| S-431 | 边界加权 Dice vs 均匀 Dice | 损失 | 不是“新损失论文”：测试 SAM 微调是否需要 | 1 | 容易 | ASSUMPTION |
| S-432 | Logit 上的交叉熵 vs SAM 微调上的 Dice | 损失 |  | 1 | 容易 | PEFT_DENSE |
| S-433 | 用于稀薄烟雾的 Focal Loss | 损失 | 仅当使用密度分桶时 | 1 | 增量改进 | SMOKE_ALPHA |
| S-434 | 用于火焰召回率的 Tversky 损失 | 损失 |  | 1 | 传统方法 | FIRE_CONFOUND |
| S-435 | 不要发明损失：重新加权密度分桶 | 数据 |  | 1 | 更好 | SMOKE_ALPHA |
| S-436 | 从厚烟到薄烟的课程学习 | 训练 |  | 1 | 增量改进 | SMOKE_ALPHA |
| S-437 | 从大器官到小器官的课程学习 | 训练 |  | 1 | 传统方法 | SAM_MEDICAL_GAP |
| S-438 | 反向课程学习：困难样本优先 | 训练 |  | 1 | 容易 | ASSUMPTION |
| S-439 | SAM 伪标签作为课程教师 | 蒸馏 | 拥挤 | 搜索 | 拥挤 | SYNTH_DA |
| S-440 | 伪标签的置信度阈值化 | 蒸馏 |  | 1 | 传统方法 | SYNTH_DA |
| S-441 | 协同训练两种提示类型 | 半监督 |  | 1 | 增量改进 | SAM_PROMPT |
| S-442 | SAM 解码器上的 Mean-Teacher | 半监督 |  | 1 | 传统方法 | PEFT_DENSE |
| S-443 | 提示抖动下的一致性作为自监督学习 | SSL |  | 1 | 具新颖性 | SAM_PROMPT |
| S-444 | MAE 预训练编码器 vs UNet 的 SAM 编码器 | 表示 |  | 计算量 | 拥挤 | PEFT_DENSE |
| S-445 | DINOv2 vs SAM 编码器用于密集任务 | 表示 |  | 1 | 拥挤 | PEFT_DENSE |
| S-446 | 极小样本下使用哪个冻结编码器 | 机制 |  | 曲线 | 重要 | ASSUMPTION |
| S-447 | 小病灶上的 Patch 大小 14 vs 16 | 架构 |  | 1 | 增量改进 | SAM_MEDICAL_GAP |
| S-448 | 面向 WSI 的窗口注意力 vs 全局注意力 | 架构 |  | 繁重 | 拥挤 | SAM_MEDICAL_GAP |
| S-449 | Mamba vs ViT：仅在识别出 ViT 失败模式时 | 架构 | 需要先发现失败 | — | 伪风险 | NEG_RESULT |
| S-450 | 不要无科学问题地替换骨干 | 废弃 | — | — | 废弃 | NEG_RESULT |
| S-451 | Token 合并速度 vs 小物体召回率 | 效率 |  | 1 | 工程 | DET_SHIFT |
| S-452 | 剪枝 SAM MLP | 效率 |  | 1 | 工程 | PEFT_DENSE |
| S-453 | 在匹配提示下将 SAM2 蒸馏为用于火灾的 Tiny 模型 | 蒸馏 | 公平 | 1 | 拥挤 | FIRE_CONFOUND |
| S-454 | 端侧窗口处理 + 微型 UNet vs MobileSAM | 部署 |  | 1 | 工程 | FIRE_CONFOUND |
| S-455 | 能耗指标 | 部署 |  | 1 | 偏软性 | EVAL_LEAK |
| S-456 | 延迟百分位数而非均值 | 部署 |  | 1 | 工程 | EVAL_LEAK |
| S-457 | Batch 大小 1 vs 8 的 Dice 差异 | 协议 | BN | 1 | 容易 | EVAL_LEAK |
| S-458 | 混合精度掩码差异 | 复现性 |  | 1 | 工程 | EVAL_LEAK |
| S-459 | SAM CUDA 的非确定性 | 复现性 |  | 1 | 工程 | EVAL_LEAK |
| S-460 | LoRA 检查点平均 | 训练 |  | 1 | 增量改进 | PEFT_DENSE |
| S-461 | 基于校准而非 Dice 的早停 | 训练 |  | 1 | 有趣 | CALIB |
| S-462 | 在 OOD 医院数据上的早停 | 训练 |  | 1 | 重要 | SAM_MEDICAL_GAP |
| S-463 | 提示类型专家模型的模型汤（Model Soups） | 模型汤 |  | 1 | 增量改进 | SAM_PROMPT |
| S-464 | 面向器官的任务向量 | 算术 |  | 1 | 拥挤 | PEFT_DENSE |
| S-465 | 对不良 LoRA 方向取反 | 编辑 |  | 1 | 推测性 | PEFT_DENSE |
| S-466 | 使用旧任务提示修复微调 | 修复 |  | 1 | 增量改进 | FORGETTING |
| S-467 | 仅在提示编码器上使用弹性权重整合（EWC） | EWC |  | 1 | 增量改进 | FORGETTING |
| S-468 | 将多个器官打包为多提示批次 | 训练 |  | 1 | 工程 | SAM_MEDICAL_GAP |
| S-469 | 类别平衡采样 vs 患者平衡采样 | 训练 |  | 1 | 重要 | EVAL_LEAK |
| S-470 | 对稀薄烟雾帧进行过采样 | 训练 |  | 1 | 容易 | SMOKE_ALPHA |
| S-471 | 时间步长（Striding）作为数据增强 | 视频 |  | 1 | 容易 | SAM2_MEMORY |
| S-472 | 倒放视频训练 | 视频 |  | 1 | 容易 | SAM2_MEMORY |
| S-473 | 火灾视频的速度抖动增强 | 视频 |  | 1 | 容易 | FIRE_CONFOUND |
| S-474 | 帧重复作为作弊手段 | 评估 | 检测测试集中的重复帧 | 审计 | 社交阻力 | EVAL_LEAK |
| S-475 | 火灾数据集中的训练/测试片段重叠 | 泄漏 | 哈希 | 1 | 社交阻力 | EVAL_LEAK |
| S-476 | YouTube 火灾数据集许可证 | 社交 |  | — | 偏软性 | EVAL_LEAK |
| S-477 | 野火数据集的地理偏差 | 偏差 |  | 元分析 | 偏软性 | EVAL_LEAK |
| S-478 | 烟雾监控相机中的肤色/场景偏差 | 偏差 |  | 1 | 偏软性 | EVAL_LEAK |
| S-479 | 器官分割中的性别/年龄性能差距 | 公平性 |  | 1 | 重要 | SAM_MEDICAL_GAP |
| S-480 | 扫描仪尺寸与医院的混杂 | 因果 |  | 1 | 困难 | SAM_MEDICAL_GAP |
| S-481 | 捷径：X-ray 中的标尺 | 虚假线索 |  | 1 | 已知类别 | SAM_MEDICAL_GAP |
| S-482 | 捷径：医院覆盖文本 | 虚假线索 |  | 1 | 已知 | VLM_DENSE |
| S-483 | 捷径：胸腔引流管暗示病理 | 虚假线索 |  | 1 | 已知 | SAM_MEDICAL_GAP |
| S-484 | 捷径：红色饱和度暗示火灾 | 虚假线索 |  | 1 | 容易 | FIRE_CONFOUND |
| S-485 | 捷径：天空暗示非火灾 | 虚假线索 |  | 1 | 容易 | FIRE_CONFOUND |
| S-486 | 无火灾的红色反事实覆盖层 | 因果 |  | 1 | 容易 | FIRE_CONFOUND |
| S-487 | 灰度世界火灾图像 | 因果 |  | 1 | 容易 | FIRE_CONFOUND |
| S-488 | 移除颜色：在灰度火灾图像上运行 SAM | 因果 |  | 1 | 容易 | FIRE_CONFOUND |
| S-489 | 灰度烟雾：颜色是不必要的？ | 因果 |  | 1 | 容易 | SMOKE_ALPHA |
| S-490 | 纯光流烟雾检测器 | 基线 |  | 1 | 传统方法 | SMOKE_ALPHA |
| S-491 | 变化检测基线 | 基线 |  | 1 | 传统方法 | SMOKE_ALPHA |
| S-492 | GMM 背景建模 | 基线 |  | 1 | 传统方法 | SMOKE_ALPHA |
| S-493 | 报告传统基线否则予以拒稿 | 社交 |  | — | 社交阻力 | EVAL_LEAK |
| S-494 | nnU-Net 作为强制性医学基线 | 社交 |  | 1 | 社交阻力 | SAM_MEDICAL_GAP |
| S-495 | Cellpose 作为强制性细胞基线 | 社交 |  | 1 | 社交阻力 | SAM_MEDICAL_GAP |
| S-496 | Mask R-CNN 作为火灾基线 | 社交 |  | 1 | 社交阻力 | FIRE_CONFOUND |
| S-497 | DeepLab Stuff 作为烟雾基线 | 社交 |  | 1 | 社交阻力 | SMOKE_ALPHA |
| S-498 | CRF 后处理作为基线 | 社交 |  | 1 | 传统方法 | SAM_PROMPT |
| S-499 | GrabCut 作为交互式基线 | 社交 |  | 1 | 传统方法 | SAM_PROMPT |
| S-500 | SIOX / 分水岭算法 | 社交 |  | 1 | 传统方法 | SAM_PROMPT |
| S-501 | 匹配人工时间的 GrabCut vs SAM | HCI |  | 成本 | 重要 | SAM_PROMPT |
| S-502 | 新手 vs 专家提示 | HCI |  | 成本 | 重要 | SAM_PROMPT |
| S-503 | 提示教程教学效应 | HCI |  | 成本 | 偏软性 | SAM_PROMPT |
| S-504 | 超过 100 例病例的疲劳效应 | HCI |  | 成本 | 偏软性 | SAM_PROMPT |
| S-505 | SAM IoU-token 的信任校准 | HCI |  | 成本 | CALIB | CALIB |
| S-506 | 自动化偏差：接受错误的 SAM 掩码 | HCI |  | 成本 | 安全性 | SAM_MEDICAL_GAP |
| S-507 | 结合 SAM 的第二阅片人 | 临床 |  | 繁重 | 偏软性 | SAM_MEDICAL_GAP |
| S-508 | CAD 试验终点 ≠ Dice | 临床 |  | 偏软性 | 偏软性 | EVAL_LEAK |
| S-509 | 放射治疗中的勾画时间 | 应用 |  | 成本 | 偏软性 | SAM_MEDICAL_GAP |
| S-510 | 观察者内变异性作为目标 | 指标 | 模型落在人类区间内 | 1 | 重要 | EVAL_LEAK |
| S-511 | 表面 Dice 放射治疗默认指标 | 指标 |  | 1 | 已知 | EVAL_LEAK |
| S-512 | 预测 vs GT 上的剂量-体积直方图 | 下游任务 |  | 繁重 | 重要 | SAM_MEDICAL_GAP |
| S-513 | 不改变辐射剂量的分割误差 | 下游任务 |  | 繁重 | 重要 | SAM_MEDICAL_GAP |
| S-514 | 不改变报警状态的检测 mAP | 下游任务 |  | 1 | 重要 | FIRE_CONFOUND |
| S-515 | 跟踪 MOTA vs 火势蔓延估计 | 下游任务 |  | 1 | 有趣 | FIRE_CONFOUND |
| S-516 | 3D 体积误差 vs 切片 Dice | 下游任务 |  | 1 | 已知 | SAM_MEDICAL_GAP |
| S-517 | Hausdorff 95 对单个像素敏感 | 指标 |  | 1 | 已知 | EVAL_LEAK |
| S-518 | 归一化表面 Dice 阈值 2mm | 指标 |  | 1 | 已知 | EVAL_LEAK |
| S-519 | 面向多器官的全景质量（PQ） | 指标 |  | 1 | 已知 | EVAL_LEAK |
| S-520 | 火焰实例的 PQ | 指标 |  | 1 | 增量改进 | FIRE_CONFOUND |
| S-521 | 用于玻璃的 Boundary IoU | 指标 |  | 1 | 已知 | SMOKE_ALPHA |
| S-522 | 用于 Alpha 的 MAD / MSE | 指标 |  | 1 | 已知 | SMOKE_ALPHA |
| S-523 | 用于 Alpha 的梯度误差 | 指标 |  | 1 | 已知 | SMOKE_ALPHA |
| S-524 | 烟雾掩码的连通性 | 指标 |  | 1 | 有趣 | SMOKE_ALPHA |
| S-525 | 血管的拓扑结构（Betti 数） | 指标 |  | 1 | 拥挤 | SAM_MEDICAL_GAP |
| S-526 | 导管的中心线 Dice (clDice) | 指标 |  | 1 | 已知 | SAM_MEDICAL_GAP |
| S-527 | SAM 比 UNet 更易在拓扑上失败 | 主张 |  | 1 | 可测试 | SAM_MEDICAL_GAP |
| S-528 | 事后拓扑修复 vs 额外模块 | 极简 |  | 1 | 传统方法 | SAM_MEDICAL_GAP |
| S-529 | 连通分量过滤作为基线 | 极简 |  | 1 | 容易 | SAM_PROMPT |
| S-530 | 空洞填充破坏嵌套物体 | 失败 |  | 1 | 容易 | SAM_PROMPT |
| S-531 | 嵌套器官内肿瘤协议 | 协议 | 两个提示 | 1 | 重要 | SAM_MEDICAL_GAP |
| S-532 | 层次化 SAM：先器官后病灶 | 流水线 |  | 1 | 增量改进 | SAM_MEDICAL_GAP |
| S-533 | 将病灶提示条件化于器官掩码 | 提示 |  | 1 | 增量改进 | SAM_PROMPT |
| S-534 | 器官与病灶之间的互斥损失 | 训练 | 若微调 | 1 | 传统方法 | PEFT_DENSE |
| S-535 | 图谱先验 vs SAM | 经典 |  | 1 | 传统方法 | SAM_MEDICAL_GAP |
| S-536 | 先配准后图谱 vs 可提示模型 | 对比 |  | 1 | 传统方法 | SAM_MEDICAL_GAP |
| S-537 | SAM 用于初始化水平集（Level-Set） | 混合 |  | 1 | 传统方法 | SAM_PROMPT |
| S-538 | 仅当 SAM 残差为高频时才采用混合模型 | 测试 |  | 1 | 有趣 | SAM_PROMPT |
| S-539 | SAM 误差的残差分析 | 科学 | 误差的频谱特性 | 1 | 重要 | SAM_PROMPT |
| S-540 | 误差模式分类学图谱 | 科学 | 聚类误差 | 1 | 重要 | SAM_PROMPT |
| S-541 | 逐数据集误差指纹 | 科学 |  | 元分析 | 社交阻力 | EVAL_LEAK |
| S-542 | 从图像统计量预测 SAM 失败 | 路由 | 随后发送给专家模型 | 1 | 增量改进 | SAM_PROMPT |
| S-543 | 分流到 nnU-Net vs SAM 的路由器 | 系统 |  | 1 | 工程 | SAM_MEDICAL_GAP |
| S-544 | “Stuff vs Thing” 的低成本检测器 | 路由器 |  | 1 | 有趣 | SMOKE_ALPHA |
| S-545 | 在烟雾上使用 Thing 模型属于范畴错误 | 主张 |  | 1 | 概念性 | SMOKE_ALPHA |
| S-546 | 在器械上使用 Stuff 模型失败 | 对偶 |  | 1 | 容易 | DET_SHIFT |
| S-547 | 联合全景火灾+烟雾分割 | 任务 |  | 数据 | 宏大雄心 | FIRE_CONFOUND |
| S-548 | 共享编码器双头无新颖性（除非展示梯度冲突） | 废弃 | 必须先展示梯度冲突 | 1 | 科学 | PEFT_DENSE |
| S-549 | 火灾 vs 烟雾的梯度冲突 | 测量 |  | 1 | 可测试 | PEFT_DENSE |
| S-550 | 多任务有助于校准 | 主张 |  | 1 | 可测试 | CALIB |
| S-551 | 多任务损害罕见类别 | 主张 |  | 1 | 容易 | DET_SHIFT |
| S-552 | 烟雾的辅助深度信息 | 若有 RGB-D |  | 数据 | 数据 | SMOKE_ALPHA |
| S-553 | 双目立体烟雾 | 传感器 |  | 数据 | 硬件 | SMOKE_ALPHA |
| S-554 | 激光雷达（LiDAR）+ 相机火灾检测 | 传感器 |  | 数据 | 硬件 | FIRE_CONFOUND |
| S-555 | 高光谱烟雾 | 传感器 |  | 数据 | 硬件 | SMOKE_ALPHA |
| S-556 | 低成本纯 RGB vs 专用传感器：投资回报率（ROI） | 问题 | 何时纯 RGB 已足够 | 偏软性 | 偏软性 | ASSUMPTION |
| S-557 | 纯热红外火灾分割 | 传感器 |  | 1 | 数据 | FIRE_CONFOUND |
| S-558 | 将对齐热红外-RGB 作为核心问题 | 域自适应 |  | 1 | 拥挤 | SYNTH_DA |
| S-559 | 非配对热红外-RGB CycleGAN 已过时拥挤 | 废弃 | 需要新问题 | — | 废弃 | SYNTH_DA |
| S-560 | 用于闪烁检测的事件相机 | 传感器 |  | 数据 | 场景细分 | FIRE_CONFOUND |
| S-561 | 音频爆裂声 + 视频 | 多模态 |  | 数据 | 邻近领域 | FIRE_CONFOUND |
| S-562 | 气味传感器超出研究范围 | 废弃 | — | — | 废弃 | NEG_RESULT |
| S-563 | 卫星野火 vs 地面监控相机 | 尺度 | 不同的科学范畴 | 拆分 | 社交阻力 | FIRE_CONFOUND |
| S-564 | 卫星烟羽上的 SAM | 尺度 |  | 1 | 数据 | SMOKE_ALPHA |
| S-565 | 分辨率差距：10m vs 1cm | 问题 |  | 1 | 偏软性 | SMOKE_ALPHA |
| S-566 | 卫星图像中的云 vs 烟雾 | 混杂因素 |  | 1 | 遥感领域已知 | SMOKE_ALPHA |
| S-567 | 若遥感文献已有，不得声称 CV 创新 | 搜索 | 强制性 Stage 3 任务 | — | 流程 | EVAL_LEAK |
| S-568 | 水下烟雾类似物：浑浊度 | 统一 |  | 1 | 推测性 | SMOKE_ALPHA |
| S-569 | 恶劣天气驾驶数据集 vs 野火烟雾 | 迁移 |  | 1 | 可测试 | SMOKE_ALPHA |
| S-570 | BDD 雾天模型用于野火 | 迁移 |  | 1 | 容易 | SMOKE_ALPHA |
| S-571 | 恶劣天气基准遗漏了火灾 | 缺陷 |  | 元分析 | 偏软性 | EVAL_LEAK |
| S-572 | 透明工业产品检测 | 工业 |  | 1 | 数据 | SMOKE_ALPHA |
| S-573 | 食品保鲜膜检测 | 工业 |  | 1 | 场景细分 | SMOKE_ALPHA |
| S-574 | 细胞培养基弯月面 | 科学 |  | 1 | 场景细分 | SAM_MEDICAL_GAP |
| S-575 | 超声耦合剂伪影 | 失败 |  | 1 | 场景细分 | SAM_MEDICAL_GAP |
| S-576 | 镜面高光误报为火灾 | 失败 |  | 1 | 容易 | FIRE_CONFOUND |
| S-577 | 霓虹灯标志误报为火灾 | 失败 |  | 1 | 容易 | FIRE_CONFOUND |
| S-578 | 日落晚霞误报为火灾 | 失败 |  | 1 | 容易 | FIRE_CONFOUND |
| S-579 | 焊接作为超出范围的火灾类型 | 分类学 |  | 1 | 偏软性 | FIRE_CONFOUND |
| S-580 | 生日蜡烛 vs 灾害火灾 | 分类学 |  | 1 | 偏软性 | FIRE_CONFOUND |
| S-581 | 数据集定义本身就是贡献 | 主张 |  | 数据 | 社交阻力 | EVAL_LEAK |
| S-582 | 仅在旧指标失效时才构建新数据集 | 规则 |  | — | 流程 | EVAL_LEAK |
| S-583 | 使用 Alpha 重新标注烟雾 | 数据 | 高价值 | 成本 | 成本 | SMOKE_ALPHA |
| S-584 | 使用患者划分重新标注医学 SAM | 数据 |  | 成本 | 社交阻力 | SAM_MEDICAL_GAP |
| S-585 | 发布多标注者烟雾数据集 | 数据 |  | 成本 | 重要 | SMOKE_ALPHA |
| S-586 | 发布提示跟踪轨迹数据 | 数据 | 记录点击日志 | 成本 | 重要 | SAM_PROMPT |
| S-587 | 失败案例图谱作为独立论文 | 科学 |  | 成本 | 社交阻力 | SAM_PROMPT |
| S-588 | 可复现性套件 > 0.5% Dice 增益 | 社交 |  | — | 社交阻力 | EVAL_LEAK |
| S-589 | 负面结果论文的发表会议策略 | 社交 |  | — | 偏软性 | NEG_RESULT |
| S-590 | 挑战既有假设本身就是一种论文类型 | 社交 |  | — | 偏软性 | ASSUMPTION |
| S-591 | 测量论文：提示敏感性法则 | 科学 | 拟合缩放关系 | 1 | 重要 | SAM_PROMPT |
| S-592 | 微调图像数 vs Dice 的缩放法则 | 科学 |  | 计算量 | 拥挤 | PEFT_DENSE |
| S-593 | LoRA 秩 vs 遗忘程度的缩放法则 | 科学 |  | 2 个任务 | 有趣 | FORGETTING |
| S-594 | 记忆长度 vs 3D Dice 的缩放法则 | 科学 |  | 1 | 容易 | SAM2_MEMORY |
| S-595 | 边界框紧致度 vs Dice 的缩放法则 | 科学 |  | 1 | 容易 | SAM_PROMPT |
| S-596 | 物体面积 vs Dice 的幂律关系 | 科学 |  | 元分析 | 重要 | SAM_PROMPT |
| S-597 | 对比度 vs Dice 的法则 | 科学 |  | 元分析 | 重要 | SAM_MEDICAL_GAP |
| S-598 | 边界长度 vs Dice | 科学 |  | 1 | 容易 | SAM_PROMPT |
| S-599 | 肿瘤分形维数 vs SAM 失败 | 科学 |  | 1 | 推测性 | SAM_MEDICAL_GAP |
| S-600 | 纹理熵 vs 点提示失败 | 科学 |  | 1 | 重复 S-002 | SAM_PROMPT |
| S-601 | 变异 S-002：傅里叶空间中的熵 | 科学 |  | 1 | 增量改进 | SAM_PROMPT |
| S-602 | 变异 S-007：评分器 = SAM IoU-token | 循环论证 | 会导致过拟合 | 1 | 容易 | SAM_PROMPT |
| S-603 | 变异 S-007：评分器 = 放射科医生微型模型 | 蒸馏 |  | 1 | 数据 | SAM_PROMPT |
| S-604 | 变异 S-014：打乱框内 patch | 因果 |  | 1 | 有趣 | SAM_PROMPT |
| S-605 | 变异 S-014：打乱框外 patch | 因果 |  | 1 | 有趣 | SAM_PROMPT |
| S-606 | 变异 S-041：仅微调 50 步解码器 | 极端 |  | 1 | 容易 | SAM_MEDICAL_GAP |
| S-607 | 变异 S-046：顺序模态 vs 混合模态 | 持续学习 |  | 1 | 重要 | FORGETTING |
| S-608 | 变异 S-052：n=10,20,50,100 曲线 | 机制 |  | 1 | 重要 | ASSUMPTION |
| S-609 | 变异 S-058：哪些 COCO 类别发生遗忘 | 切片 |  | 1 | 有趣 | FORGETTING |
| S-610 | 变异 S-073：随机顺序 vs 倒序 | 3D |  | 1 | 容易 | SAM2_MEMORY |
| S-611 | 变异 S-079：探测记忆中的器官 ID | 探测 |  | 1 | 有趣 | SAM2_MEMORY |
| S-612 | 变异 S-096：8 种指标的等级相关性 | 元分析 |  | 1 | 重要 | EVAL_LEAK |
| S-613 | 变异 S-103：人像抠图 → 玻璃迁移 | 迁移 |  | 1 | 可测试 | SMOKE_ALPHA |
| S-614 | 变异 S-141：哪些 COCO 类别在 PEFT 后存活 | 切片 |  | 1 | 重要 | PEFT_DENSE |
| S-615 | 变异 S-148：缩放到相同范数的随机 LoRA | 对照组 |  | 1 | 高风险 | PEFT_DENSE |
| S-616 | 变异 S-164：针对选择性网络风险进行训练 | 目标 |  | 1 | 有趣 | CALIB |
| S-617 | 变异 S-176：顺序先点后框 | 顺序 |  | 1 | 容易 | FORGETTING |
| S-618 | 变异 S-199：包含 HD95, NSD, PQ | 矩阵 |  | 1 | 容易 | EVAL_LEAK |
| S-619 | 变异 S-228：罕见 vs 典型疾病照片 | 切片 |  | 1 | 数据 | VLM_DENSE |
| S-620 | 变异 S-240：合成否定句式 | NLP |  | 1 | 容易 | VLM_DENSE |
| S-621 | 变异 S-288：OOD = 其他器官 | 划分 |  | 1 | 容易 | ASSUMPTION |
| S-622 | 变异 S-288：OOD = 其他医院 | 划分 |  | 1 | 重要 | ASSUMPTION |
| S-623 | 变异 S-292：在单一器官上从头训练 ViT | 繁重 |  | 计算量 | 高风险 | ASSUMPTION |
| S-624 | 变异 S-318：绘制 Dice-ECE 帕累托图 | 权衡 |  | 1 | 重要 | CALIB |
| S-625 | 变异 S-342：关闭记忆 vs 消融遮挡机制 | 消融 |  | 1 | 容易 | SAM2_MEMORY |
| S-626 | 变异 S-347：烟雾上的提示进化 | 领域 |  | 1 | 容易 | SMOKE_ALPHA |
| S-627 | 拆分 S-015：火灾 vs 烟雾 vs 染色 vs 雾霾 | 分类学 |  | 1 | 概念性 | ASSUMPTION |
| S-628 | 拆分 S-054：肿瘤上的点 vs 肿瘤上的框 | 提示 |  | 1 | 容易 | SAM_MEDICAL_GAP |
| S-629 | 拆分 S-099：白烟 vs 黑烟 vs 工业烟雾 | 颜色 |  | 1 | 数据 | SMOKE_ALPHA |
| S-630 | 拆分 S-126：室内火灾 vs 野火 vs 车辆火灾 | 场景 |  | 1 | 数据 | FIRE_CONFOUND |
| S-631 | 合并 S-003+S-060：Oracle 提示协议论文 | 评估 |  | 元分析 | 社交阻力 | EVAL_LEAK |
| S-632 | 合并 S-096+S-199：指标反转论文 | 评估 |  | 元分析 | 重要 | EVAL_LEAK |
| S-633 | 合并 S-141+S-058：PEFT 对 Zero-Shot 的代价 | PEFT |  | 1 | 重要 | PEFT_DENSE |
| S-634 | 合并 S-176+S-006：协议遗忘 | 持续学习 |  | 1 | 重要 | FORGETTING |
| S-635 | 合并 S-079+S-073：记忆内容 vs 时间顺序 | 记忆 |  | 1 | 重要 | SAM2_MEMORY |
| S-636 | 复活“简单颜色模型”作为必要基线 | 社交 |  | 1 | 社交阻力 | SMOKE_ALPHA |
| S-637 | 复活时间匹配的 GrabCut 基线 | 社交 |  | 成本 | 社交阻力 | SAM_PROMPT |
| S-638 | 废弃 S-149 QLoRA（除非以显存为核心故事） | 废弃 | — | — | 废弃 | PEFT_DENSE |
| S-639 | 废弃 S-424 LLM 实验智能体 | 废弃 | — | — | 废弃 | NEG_RESULT |
| S-640 | 废弃 S-449 无失败分析的 Mamba | 废弃 | — | — | 废弃 | NEG_RESULT |
| S-641 | 废弃 S-450 骨干网络替换 | 废弃 | — | — | 废弃 | NEG_RESULT |
| S-642 | 废弃 S-559 非配对 CycleGAN | 废弃 | — | — | 废弃 | SYNTH_DA |
| S-643 | 废弃 S-562 气味传感器 | 废弃 | — | — | 废弃 | NEG_RESULT |
| S-644 | 重点保护 S-014 框内图像消融 | 保护 | — | — | 保护 | SAM_PROMPT |
| S-645 | 重点保护 S-052 小样本 n 下预训练损害 | 保护 | — | — | 保护 | ASSUMPTION |
| S-646 | 重点保护 S-148 随机 LoRA 方向 | 保护 | — | — | 保护 | PEFT_DENSE |
| S-647 | 重点保护 S-183 低可塑性假说 | 保护 | — | — | 保护 | FORGETTING |
| S-648 | 重点保护 S-228 VLM 先验损害 | 保护 | — | — | 保护 | VLM_DENSE |
| S-649 | 重点保护 S-292 从头训练类 SAM 模型 | 保护 | — | — | 保护 | ASSUMPTION |
| S-650 | 重点保护 S-318 微调校准代价 | 保护 | — | — | 保护 | CALIB |
| S-651 | 重点保护 S-347 提示进化损害 | 保护 | — | — | 保护 | SAM_PROMPT |
| S-652 | 重点保护 S-395 部分容积作为 Alpha | 保护 | — | — | 保护 | SMOKE_ALPHA |
| S-653 | 重点保护 S-513 剂量不敏感误差 | 保护 | — | — | 保护 | SAM_MEDICAL_GAP |
| S-654 | 重点保护 S-539 残差频谱分析 | 保护 | — | — | 保护 | SAM_PROMPT |
| S-655 | 重点保护 S-604 打乱 Patch 因果测试 | 保护 | — | — | 保护 | SAM_PROMPT |
| S-656 | 低成本：S-408 翻转一致性 | 低成本 |  | 1 | 低成本 | SAM_PROMPT |
| S-657 | 低成本：S-409 旋转测试 | 低成本 |  | 1 | 低成本 | SAM_PROMPT |
| S-658 | 低成本：S-488 灰度火灾 | 低成本 |  | 1 | 低成本 | FIRE_CONFOUND |
| S-659 | 低成本：S-489 灰度烟雾 | 低成本 |  | 1 | 低成本 | SMOKE_ALPHA |
| S-660 | 低成本：S-293 关闭记忆 | 低成本 |  | 1 | 低成本 | SAM2_MEMORY |
| S-661 | 低成本：S-287 额外点测试 | 低成本 |  | 1 | 低成本 | SAM_PROMPT |
| S-662 | 低成本：S-294 按对比度划分框 vs 点 | 低成本 |  | 1 | 低成本 | SAM_PROMPT |
| S-663 | 低成本：S-298 IoU-token ECE | 低成本 |  | 1 | 低成本 | CALIB |
| S-664 | 低成本：S-356 随机框测试 | 低成本 |  | 1 | 低成本 | SAM_PROMPT |
| S-665 | 低成本：S-353 点击饱和测试 | 低成本 |  | 1 | 低成本 | SAM_PROMPT |
| S-666 | 表示：器官的 SAM token PCA | 表示 |  | 1 | 容易 | SAM_MEDICAL_GAP |
| S-667 | 表示：医学 vs SA-1B 编码器 CKA | 表示 |  | 计算量 | 有趣 | SAM_MEDICAL_GAP |
| S-668 | 表示：解码器交叉注意力图 | 表示 |  | 1 | 容易 | SAM_PROMPT |
| S-669 | 表示：跨患者记忆库 CKA | 表示 |  | 1 | 有趣 | SAM2_MEMORY |
| S-670 | 表示：器官间 LoRA 子空间重叠 | 表示 |  | 1 | 有趣 | PEFT_DENSE |
| S-671 | 表示：CLIP vs SAM 空间对齐 | 表示 |  | 1 | 拥挤 | VLM_DENSE |
| S-672 | 表示：CLIP 中的烟雾 vs 云彩 | 表示 |  | 1 | 容易 | VLM_DENSE |
| S-673 | 表示：CLIP 中的火灾是“橙色” | 表示 |  | 1 | 容易 | VLM_DENSE |
| S-674 | 表示：医学 CLIP 仍按自然图像聚类 | 表示 |  | 1 | 可测试 | VLM_DENSE |
| S-675 | 表示：掩码 token vs 图像 token 的 RSA | 表示 |  | 1 | 有趣 | SAM_PROMPT |
| S-676 | 优化：SAM 微调中的 AdamW vs SGD | 优化 |  | 1 | 容易 | PEFT_DENSE |
| S-677 | 优化：余弦退火 vs 常数学习率 | 优化 |  | 1 | 容易 | PEFT_DENSE |
| S-678 | 优化：预热（Warmup）的必要性 | 优化 |  | 1 | 容易 | PEFT_DENSE |
| S-679 | 优化：解码器上的梯度裁剪 | 优化 |  | 1 | 容易 | PEFT_DENSE |
| S-680 | 优化：fp16 的损失缩放 | 优化 |  | 1 | 工程 | PEFT_DENSE |
| S-681 | 数据：公开集之间的重复患者 | 泄漏 |  | 哈希 | 社交阻力 | EVAL_LEAK |
| S-682 | 数据：MSD vs BTCV 重叠 | 泄漏 |  | 审计 | 社交阻力 | EVAL_LEAK |
| S-683 | 数据：来自同一 YouTube 频道的火灾视频 | 泄漏 |  | 审计 | 社交阻力 | EVAL_LEAK |
| S-684 | 数据：来自同一工厂的烟雾照片 | 泄漏 |  | 审计 | 社交阻力 | EVAL_LEAK |
| S-685 | 数据：对比基础模型训练中包含 SA-1B | 泄漏 |  | 元分析 | 社交阻力 | EVAL_LEAK |
| S-686 | 法律：临床中 SAM 权重的许可证 | 社交 |  | — | 偏软性 | EVAL_LEAK |
| S-687 | 法律：微调中的医学数据合规 | 社交 |  | — | 偏软性 | 偏软性 | EVAL_LEAK |
| S-688 | 隐私：SAM 对罕见纹身特征的记忆 | 安全性 |  | 困难 | 困难 | EVAL_LEAK |
| S-689 | 隐私：医学微调中的成员推断 | 安全性 |  | 1 | 繁重 | EVAL_LEAK |
| S-690 | 安全性：SAM 在对抗 Patch 上——仅评估损坏 | 鲁棒性 | 常见损坏而非漏洞利用 | 1 | 流程 | ROBUST |
| S-691 | 鲁棒性：高斯噪声 | 鲁棒性 |  | 1 | 容易 | ROBUST |
| S-692 | 鲁棒性：对比度 | 鲁棒性 |  | 1 | 容易 | ROBUST |
| S-693 | 鲁棒性：雾天损坏 vs 真实烟雾 | 鲁棒性 |  | 1 | 有趣 | SMOKE_ALPHA |
| S-694 | 鲁棒性：运动模糊 | 鲁棒性 |  | 1 | 容易 | ROBUST |
| S-695 | 鲁棒性：弹性变换 | 鲁棒性 |  | 1 | 容易 | ROBUST |
| S-696 | 鲁棒性：直方图偏移 | 鲁棒性 |  | 1 | 容易 | ROBUST |
| S-697 | 鲁棒性：Tile Dropout | 鲁棒性 |  | 1 | 容易 | ROBUST |
| S-698 | 鲁棒性：提示 Dropout | 鲁棒性 |  | 1 | 容易 | SAM_PROMPT |
| S-699 | 鲁棒性：CT 中缺失切片 | 鲁棒性 |  | 1 | 容易 | SAM2_MEMORY |
| S-700 | 鲁棒性：打乱切片子集 | 鲁棒性 |  | 1 | 容易 | SAM2_MEMORY |
| S-701 | 泛化性：未见器官 | 泛化 |  | 1 | 容易 | SAM_MEDICAL_GAP |
| S-702 | 泛化性：未见模态 | 泛化 |  | 1 | 容易 | SAM_MEDICAL_GAP |
| S-703 | 泛化性：未见火灾场景 | 泛化 |  | 1 | 容易 | FIRE_CONFOUND |
| S-704 | 泛化性：未见相机 | 泛化 |  | 1 | 容易 | DET_SHIFT |
| S-705 | 泛化性：未见密度范围 | 泛化 |  | 1 | 数据 | SMOKE_ALPHA |
| S-706 | 泛化性：未见提示协议 | 泛化 |  | 1 | 容易 | SAM_PROMPT |
| S-707 | 泛化性：未见一天中的时间 | 泛化 |  | 1 | 容易 | FIRE_CONFOUND |
| S-708 | 泛化性：未见季节野火 | 泛化 |  | 1 | 数据 | FIRE_CONFOUND |
| S-709 | 泛化性：未见医院 | 泛化 |  | 1 | 重要 | SAM_MEDICAL_GAP |
| S-710 | 泛化性：未见物种（兽医） | 泛化 |  | 1 | 场景细分 | SAM_MEDICAL_GAP |
| S-711 | 泛化性：未见年龄（儿科） | 泛化 |  | 1 | 数据 | SAM_MEDICAL_GAP |
| S-712 | 失败分析模板：50 张图像定性分析 | 流程 | Stage 5 必填 | — | 流程 | EVAL_LEAK |
| S-713 | 停止条件：若 Oracle 框 SAM 比 UNet 低 0.2 Dice，终结 SAM 微调故事 | 流程 |  | 1 | 流程 | SAM_MEDICAL_GAP |
| S-714 | 停止条件：若指标反转，将论文类型转为评估 | 流程 |  | 1 | 流程 | EVAL_LEAK |
| S-715 | 停止条件：若最相近论文是 MedSAM+适配器，进行变异或废弃 | 流程 |  | — | 流程 | SAM_MEDICAL_GAP |
| S-716 | 停止条件：若 ProFSAM 已经做了检测器+SAM2 火灾分割 | 流程 |  | — | 流程 | FIRE_CONFOUND |
| S-717 | 停止条件：若 InfLoRA 已在分类上做了正交 LoRA，要求密集证据 | 流程 |  | — | 流程 | PEFT_DENSE |
| S-718 | 下一波次应由智能体增加 280+ 独立创意 | 流程 |  | — | 流程 | META |
| S-719 | 审计员应检查围绕 SAM 的信息茧房（Echo Chamber） | 流程 |  | — | 流程 | META |
| S-720 | 导师偏差：相比方法类论文过度偏向评估类论文 | 流程 | 标记给审计员 | — | 流程 | META |
