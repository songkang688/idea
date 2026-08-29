"""Killer-experiment runner (E0 with stubs / E1 scaffold with official SAM).

Per instance and model:
  conditions  : intact | object-out (exact bg or inpaint) | object-swap | sham-inpaint |
                patch-shuffle (secondary) | matched-noise (secondary)
  nulls       : box-fill | convexity-matched fill | learned box->mask | (prompt-only, SAM)
  readouts    : Dice/IoU/boundary-F vs GT; persistence; swap-tracking; NRF
  verdict     : pre-registered four-way conjunction per stratum (proposal §15):
                interpolator ⇔ small CSG ∧ high persistence ∧ tracking failure ∧
                NRF ≥ τ3 ∧ secondary probes directionally consistent.

With model.backend=stub this is E0: the harness must classify BoxFillBaseline as
'interpolator' and OracleThresholdBaseline as 'seeing' (≥1 stratum). Outputs are ACTUAL
smoke-test artifacts about the HARNESS, never about SAM.

Usage:
    python -m src.eval --config configs/default.yaml
    python -m src.eval --config configs/default.yaml --override model.backend=sam \
        model.sam_checkpoint=/path/to/sam_vit_b_01ec64.pth dataset.kind=coco
"""

from __future__ import annotations

import argparse
import csv
import os
from collections import defaultdict
from typing import Dict, List, Optional

import numpy as np

from .config import load_config
from .dataset import Instance, build_eval_instances
from .interventions import (
    boxfill_null,
    convexity_matched_mask,
    matched_noise_in_box,
    object_out_inpaint,
    patch_shuffle_in_box,
    sham_inpaint,
)
from .model_sam import (
    LearnedBoxToMaskNull,
    PromptableSegmenter,
    build_eval_models,
)
from .utils import (
    boundary_f,
    dice,
    ensure_dir,
    fill_fraction_in_box,
    iou,
    median,
    pad_box,
    save_json,
    set_seed,
)


# ------------------------------------------------------------- per instance

def evaluate_instance(
    model: PromptableSegmenter,
    inst: Instance,
    learned_null: Optional[LearnedBoxToMaskNull],
    cfg: Dict,
) -> Dict:
    cond = cfg["conditions"]
    paddings = list(cond["paddings_px"])
    p0 = int(cond["primary_padding_px"])
    shape = inst.image.shape[:2]
    g = inst.gt_mask
    b0 = pad_box(inst.box, p0, shape)

    row: Dict = {
        "model": model.name,
        "instance": inst.id,
        "stratum": f"{inst.meta.get('contrast_level','?')}-contrast/"
        f"{inst.meta.get('solidity_level','?')}-solidity",
        "solidity": inst.meta.get("solidity"),
        "contrast": inst.meta.get("contrast_measured"),
        "size_frac": inst.meta.get("size_frac"),
    }

    # --- intact ---
    m_intact = model.predict(inst.image, b0)
    row["dice_intact"] = dice(m_intact, g)
    row["iou_intact"] = iou(m_intact, g)
    row["bf_intact"] = boundary_f(m_intact, g)

    # --- primary counterfactual: object-out (exact bg when the dataset provides it) ---
    dilate = int(cond["ablation_dilate_px"][0])
    method = cond["object_out_inpaint_method"]
    if inst.background is not None:
        out_img = inst.background
        row["object_out_source"] = "exact"
    else:
        out_img = object_out_inpaint(inst.image, g, dilate_px=dilate, method=method)
        row["object_out_source"] = f"inpaint-{method}"
    m_out = model.predict(out_img, b0)
    row["dice_out"] = dice(m_out, g)
    row["csg"] = row["dice_intact"] - row["dice_out"]
    row["persistence"] = dice(m_out, m_intact)

    # inpaint variant always recorded too (instrument-robustness column, E6)
    if cond.get("object_out", True) and inst.background is not None:
        inp_img = object_out_inpaint(inst.image, g, dilate_px=dilate, method=method)
        m_inp = model.predict(inp_img, b0)
        row["dice_out_inpaint"] = dice(m_inp, g)
        row["persistence_inpaint"] = dice(m_inp, m_intact)

    # --- primary counterfactual: object-swap (tracking readout) ---
    if cond.get("object_swap", True) and inst.swap_image is not None:
        m_swap = model.predict(inst.swap_image, b0)
        s_new = inst.swap_mask
        row["track_T"] = dice(m_swap, s_new)
    else:
        m_swap, s_new = None, None
        row["track_T"] = float("nan")

    # --- controls & secondary probes ---
    if cond.get("sham_inpaint", True):
        sham_img = sham_inpaint(inst.image, g, b0, dilate_px=dilate, method=method)
        row["dice_sham"] = (
            dice(model.predict(sham_img, b0), g) if sham_img is not None else float("nan")
        )
    ps = cond.get("patch_shuffle", {})
    if ps.get("enabled", True):
        shuf = patch_shuffle_in_box(
            inst.image, b0, patch_px=int(ps.get("patch_px", 16)), seed=hash(inst.id) % 2**31
        )
        row["dice_shuffle"] = dice(model.predict(shuf, b0), g)
        row["csg_secondary"] = row["dice_intact"] - row["dice_shuffle"]
    if cond.get("matched_noise", True):
        noisy = matched_noise_in_box(inst.image, b0, seed=hash(inst.id) % 2**31)
        row["dice_noise"] = dice(model.predict(noisy, b0), g)

    # --- no-image nulls ---
    nulls: Dict[str, np.ndarray] = {}
    if cfg["nulls"].get("use_boxfill", True):
        nulls["boxfill"] = boxfill_null(b0, shape)
    if cfg["nulls"].get("use_convexity_matched", True):
        nulls["convexity_matched"] = convexity_matched_mask(
            b0, shape, fill_fraction_in_box(g, b0)
        )
    if learned_null is not None:
        nulls["learned"] = learned_null.predict(inst.image, b0)  # reads box only

    best_null_dice = float("-inf")
    for name, nm in nulls.items():
        d = dice(nm, g)
        row[f"dice_null_{name}"] = d
        best_null_dice = max(best_null_dice, d)
    row["nrf"] = (
        best_null_dice / max(row["dice_intact"], 1e-8) if nulls else float("nan")
    )

    # tracking null: best static shape vs the inserted object
    if s_new is not None and nulls:
        row["track_T_null"] = max(dice(nm, s_new) for nm in nulls.values())
        row["track_delta"] = row["track_T"] - row["track_T_null"]
    else:
        row["track_delta"] = float("nan")

    # --- padding sweep (intact + object-out only; full grid is an E1 cost decision) ---
    for pad in paddings:
        if pad == p0:
            continue
        bp = pad_box(inst.box, pad, shape)
        row[f"dice_intact_p{pad}"] = dice(model.predict(inst.image, bp), g)
        row[f"dice_out_p{pad}"] = dice(model.predict(out_img, bp), g)
    return row


# ------------------------------------------------------------- aggregation

def stratum_verdicts(rows: List[Dict], cfg: Dict) -> Dict:
    th = cfg["thresholds"]
    tau1 = float(th["tau1_csg_dice"])
    rho = float(th["rho_persistence"])
    tau2 = float(th["tau2_track_delta"])
    tau3 = float(th["tau3_nrf"])

    grouped: Dict = defaultdict(list)
    for r in rows:
        grouped[(r["model"], r["stratum"])].append(r)

    out: Dict = {}
    for (model, stratum), rs in sorted(grouped.items()):
        med = lambda k: median([r[k] for r in rs if not np.isnan(r.get(k, np.nan))])
        m_csg, m_pers = med("csg"), med("persistence")
        m_track, m_nrf = med("track_delta"), med("nrf")
        m_sec = med("csg_secondary")
        c1 = (m_csg <= tau1) and (m_pers >= rho)
        c2 = m_track <= tau2 if not np.isnan(m_track) else False
        c3 = m_nrf >= tau3 if not np.isnan(m_nrf) else False
        c4 = (
            ((m_sec <= tau1) == (m_csg <= tau1))
            if not np.isnan(m_sec)
            else True
        )
        verdict = "interpolator" if (c1 and c2 and c3 and c4) else "seeing"
        out[f"{model} :: {stratum}"] = {
            "n": len(rs),
            "median_dice_intact": med("dice_intact"),
            "median_csg": m_csg,
            "median_persistence": m_pers,
            "median_track_delta": m_track,
            "median_nrf": m_nrf,
            "median_csg_secondary": m_sec,
            "median_dice_sham": med("dice_sham"),
            "conjunction": {
                "c1_low_csg_high_persistence": bool(c1),
                "c2_tracking_failure": bool(c2),
                "c3_null_reaches_intact": bool(c3),
                "c4_secondary_consistent": bool(c4),
            },
            "verdict": verdict,
        }
    return out


def e0_assertions(verdicts: Dict) -> Dict:
    """E0 pass criteria (experiments.md): boxfill stub -> interpolator in ALL strata;
    oracle stub -> seeing in >=1 stratum."""
    boxfill = [v for k, v in verdicts.items() if k.startswith("boxfill_stub")]
    oracle = [v for k, v in verdicts.items() if k.startswith("oracle_threshold_stub")]
    checks = {}
    if boxfill:
        checks["boxfill_stub_all_interpolator"] = all(
            v["verdict"] == "interpolator" for v in boxfill
        )
    if oracle:
        checks["oracle_stub_seeing_somewhere"] = any(
            v["verdict"] == "seeing" for v in oracle
        )
    checks["E0_PASS"] = bool(checks) and all(checks.values())
    return checks


# ------------------------------------------------------------------ report

def write_outputs(rows: List[Dict], verdicts: Dict, checks: Dict, cfg: Dict) -> str:
    out_dir = ensure_dir(cfg["experiment"]["out_dir"])
    # CSV (per-instance provenance for every reported number, proposal §25)
    keys: List[str] = sorted({k for r in rows for k in r})
    csv_path = os.path.join(out_dir, "results.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(rows)
    save_json({"verdicts": verdicts, "e0_checks": checks}, os.path.join(out_dir, "verdicts.json"))

    lines = [
        f"# {cfg['experiment']['name']} — harness output",
        "",
        "Epistemic tag: **ACTUAL EXPERIMENTAL RESULT (smoke test)** when run with stub",
        "backends on synthetic data — validates the decision logic ONLY; says nothing",
        "about SAM. Real-SAM runs (backend=sam) produce E1 evidence.",
        "",
        "| model :: stratum | n | Dice intact | CSG | persist. | trackΔ | NRF | sec.CSG | verdict |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for k, v in verdicts.items():
        lines.append(
            f"| {k} | {v['n']} | {v['median_dice_intact']:.3f} | {v['median_csg']:.3f} "
            f"| {v['median_persistence']:.3f} | {v['median_track_delta']:.3f} "
            f"| {v['median_nrf']:.3f} | {v['median_csg_secondary']:.3f} | **{v['verdict']}** |"
        )
    if checks:
        lines += ["", "## E0 checks", ""]
        for k, val in checks.items():
            lines.append(f"- {k}: {'PASS' if val else 'FAIL'}")
    md_path = os.path.join(out_dir, "summary.md")
    with open(md_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    return out_dir


# -------------------------------------------------------------------- main

def main(argv=None) -> Dict:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", default="configs/default.yaml")
    ap.add_argument("--override", nargs="*", default=[])
    args = ap.parse_args(argv)
    cfg = load_config(args.config, args.override)
    set_seed(int(cfg["experiment"]["seed"]))

    instances = build_eval_instances(cfg)
    models = build_eval_models(cfg)

    learned_null: Optional[LearnedBoxToMaskNull] = None
    ckpt = cfg["nulls"].get("learned_null_ckpt")
    if ckpt and os.path.exists(ckpt):
        try:
            learned_null = LearnedBoxToMaskNull(ckpt)
            print(f"[eval] learned box->mask null loaded from {ckpt}")
        except Exception as e:  # torch missing etc.
            print(f"[eval] learned null unavailable ({e}); NRF uses shape nulls only")
    else:
        print("[eval] no learned-null checkpoint; NRF uses shape nulls only "
              "(run src.train to add it)")

    rows: List[Dict] = []
    for model in models:
        print(f"[eval] model={model.name} uses_image_evidence={model.uses_image_evidence}")
        for inst in instances:
            rows.append(evaluate_instance(model, inst, learned_null, cfg))

    verdicts = stratum_verdicts(rows, cfg)
    checks = e0_assertions(verdicts) if cfg["model"]["backend"] == "stub" else {}
    out_dir = write_outputs(rows, verdicts, checks, cfg)

    print(f"[eval] wrote {out_dir}/results.csv, verdicts.json, summary.md")
    for k, v in verdicts.items():
        print(f"[eval] {k}: {v['verdict']}  (CSG={v['median_csg']:.3f}, "
              f"persist={v['median_persistence']:.3f}, trackΔ={v['median_track_delta']:.3f}, "
              f"NRF={v['median_nrf']:.3f})")
    if checks:
        print(f"[eval] E0 {'PASS' if checks.get('E0_PASS') else 'FAIL'}: {checks}")
    return {"verdicts": verdicts, "checks": checks}


if __name__ == "__main__":
    main()
