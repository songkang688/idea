# Idea_01 路线图

## Day 1

在 200 张无定形图像 + 100 张 COCO 图像上缓存 SAM embedding。训练 `DensityHead`。跑 E0。**当晚就套用停止判据。**

## Day 2–3

E1 紧致度实验；随机编码器对照；SAM2 embedding。

## 第 1 周

Trans10K；TV 消融；写失败案例图集（在真正测量之前只能算 EXPECTED 的定性结果）。

## 第 2 周

同等标注工时下与 U-Net 对比；可选的 BraTS 浸润性病灶；起草 related work 表格。

## 完整论文

若 H1 和 H2 同时成立：投 CVPR/ICCV workshop，或 MICCAI 短文，主题为"该在哪里适配 SAM"。  
若只有 H1 成立：对于"编码器适配"这套主流叙事，它仍然是一个有价值的负结果。

## 停止 / 转向 / 杀掉

- **继续（Continue）：** H1 与 H2 都成立。
- **转向 Idea_03（Pivot）：** 如果 IoU token 本身区分成功／失败的能力就已经优于我们的头。
- **杀掉（Kill）：** 在补上 SAM2 与紧致度对照之后 H1 仍为假。
