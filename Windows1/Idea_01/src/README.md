# RetainSAM 源码

```bash
cd Windows1/Idea_01
pip install -r requirements.txt
PYTHONPATH=src python src/train_retain.py --config configs/killer_kvasir.yaml
```

这会在虚拟张量上打印 WiSE-FT 演示。在进行任何真实运行前，请在 `train_retain.py` 中接入 `segment_anything.sam_model_registry` 以及你自己的数据加载器。

不要提交 SAM 的 `.pth` checkpoint。
