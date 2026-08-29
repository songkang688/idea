# Idea_01 README

**Objectness, Not Features** —— 用冻结的 SAM embedding + 密度／排除区对比带提示的 SAM。

## 快速开始

```bash
pip install -r ../../requirements.txt
python src/train_density_head.py --config configs/killer_e0.yaml
python src/eval_killer.py --config configs/killer_e0.yaml
```

在没有 SAM 权重的情况下，脚本会改用 **FakeEncoder**，使训练回路仍然可以跑通。等 checkpoint 到位后换成 `sam_encoder.py`。

## 假设等级标注

本代码在 FakeEncoder 上产出的所有数字都是 **toy 机制自检**，不是科学结果。
