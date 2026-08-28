# Idea_01 — SeeingInside

**One-liner:** Test whether SAM uses pixels *inside* a tight box or merely interpolates a blob from the box geometry.

**Killer experiment (Day 1):** Frozen SAM-ViT-B, COCO instances, GT boxes. Compare original vs mean-fill vs inpaint-inside-box vs ellipse-null. See `experiments.md`.

**Status:** Design complete. **No ACTUAL numbers.**

```bash
pip install -r requirements.txt
python -m src.eval_killer --images_dir /path/to/coco/val2017 --ann /path/to/instances_val2017.json --limit 64
```

If `segment_anything` / weights are absent, the script still runs **BoxFillBaseline** and records that SAM path was skipped (not a fake SAM score).
