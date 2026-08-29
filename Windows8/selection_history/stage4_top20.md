# stage4_top20.md
count=19

- IDEA-X-0001 | IDEA-X-0001 | hand | mixed | 排除区提示（Exclusion-region prompting）：无定形目标需要的提示，是指明"什么不是目标"。
- IDEA-X-0002 | IDEA-X-0002 | hand | mixed | 冻结 SAM 上的密度解码器：在冻结 embedding 上用密度回归头替换二值 mask decoder。
- IDEA-X-0003 | IDEA-X-0003 | hand | mixed | IoU-token 拒答选项：把 SAM 的 IoU 头当作选择性预测的门控。
- IDEA-X-0004 | IDEA-X-0004 | hand | mixed | Spectral LoRA audit：对（LoRA 适配后 − 冻结）特征图做 FFT。
- IDEA-X-0005 | IDEA-X-0005 | hand | mixed | 同等标注工时横向比拼：在固定标注分钟数下比较 nnU-Net vs SAM-PEFT vs 线性探针。
- IDEA-X-0006 | IDEA-X-0006 | hand | mixed | 提示紧致度混淆因素：把 SAM 提示类论文用抖动到同等紧致度的框重跑一遍。
- IDEA-X-0007 | IDEA-X-0007 | hand | mixed | 用 replay 保持可提示性：在医学 PEFT 过程中混入 1% 的合成点击分割数据。
- IDEA-X-0008 | IDEA-X-0008 | hand | mixed | 把标注者当模型：在标注者 A 上训练，在标注者 B 上测试。
- IDEA-X-0009 | IDEA-X-0009 | hand | mixed | patch／病灶直径尺度律：失败概率 ~ f(病灶直径 / patch 尺寸)。
- IDEA-X-0010 | IDEA-X-0010 | hand | mixed | 语言不做像素分组：当视觉 grouper 被冻结时，CLIP/VLM 的文本特征只提升类别存在性 AUC，不提升掩码 NSD。
- IDEA-A-0001 | SAM-OBJECTNESS | invert | natural-COCO-objects | SAM-OBJECTNESS on natural-COCO-objects：SAM 系列在无定形目标上失败，是因为它编码了 objectness 先验，而不是因为编码器缺少特征。
- IDEA-A-0022 | SAM-TEXTURE | invert | natural-COCO-objects | SAM-TEXTURE on natural-COCO-objects：SFM 在血管／烟雾上的失败是由"把纹理当物体"的混淆造成的，不是容量不足。
- IDEA-A-0043 | SAM-PROMPT-GEOM | invert | natural-COCO-objects | SAM-PROMPT-GEOM on natural-COCO-objects：点／框／掩码提示之间的性能差距，应由空间支撑与目标拓扑的不匹配来解释，而不是把"框更好"当成一条普适规[原文在此处被截断：`not 'box is better' as a unive`]
- IDEA-A-0064 | SAM-IOU-CAL | invert | natural-COCO-objects | SAM-IOU-CAL on natural-COCO-objects：SAM 的 IoU token 在 SA-1B 物体上是良好校准的，在低对比度／无定形掩码上则系统性误校准。
- IDEA-A-0085 | SAM-NEGCLICK | invert | natural-COCO-objects | SAM-NEGCLICK on natural-COCO-objects：负点击对物体有帮助，但会在密度场（烟雾／浸润性肿瘤）的支撑区上"打洞"从而造成损害。
- IDEA-A-0106 | SAM-MULTIMASK | invert | natural-COCO-objects | SAM-MULTIMASK on natural-COCO-objects：多掩码歧义排序在医学／无定形图像上相对 COCO 是反过来的。
- IDEA-A-0127 | SAM2-MEMORY | invert | natural-COCO-objects | SAM2-MEMORY on natural-COCO-objects：SAM2 的记忆机制对视频物体有帮助，但会在各自独立运动的火焰／烟雾羽流之间泄漏身份。
- IDEA-A-0169 | HQ-BOUNDARY | invert | natural-COCO-objects | HQ-BOUNDARY on natural-COCO-objects：HQ-SAM 的 high-quality token 改善自然物体边缘，但改善不了折射／透明边界。
- IDEA-A-0190 | FT-FORGET | invert | natural-COCO-objects | FT-FORGET on natural-COCO-objects：MedSAM 式的全量微调对可提示 zero-shot 能力的破坏比 PEFT 更严重，但 PEFT 在其他模态上同样会破坏它。
