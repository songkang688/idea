"""Self-checks for src/alphasmoke on synthetic arrays.

These are CODE-CORRECTNESS unit tests (identity inputs, constructed reversals,
known-alpha composites). They are NOT experiments and produce no reportable results.

Run:  python -m pytest tests/ -q     (from Windows4/Idea_03, with src on sys.path)
  or: python tests/test_selfchecks.py
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from alphasmoke.metrics import (  # noqa: E402
    alpha_metric_report,
    binary_metric_report,
    boundary_f,
    bootstrap_tau,
    connectivity_error,
    dice,
    f_beta,
    gradient_error,
    iou,
    kendall_tau,
    mae,
    mmse_per_image,
    mse,
    sad,
    tau_matrix,
    top_k_reversals,
)
from alphasmoke.baselines import (  # noqa: E402
    hsv_smoke_score,
    rgb_to_hsv,
    smoke_alpha_dark_channel,
    transmission,
)
from alphasmoke.alpha_recovery import recover_alpha, estimate_background  # noqa: E402
from alphasmoke.rater import (  # noqa: E402
    ceiling_summary,
    confront_with_published_deltas,
    pairwise_iou_ceiling,
    pairwise_mae_ceiling,
)

RNG = np.random.default_rng(7)


# ---------------------------------------------------------------- alpha metrics

def test_alpha_metrics_perfect_prediction_is_zero_error():
    a = np.clip(RNG.random((32, 32)), 0, 1)
    assert mae(a, a) == 0.0
    assert sad(a, a) == 0.0
    assert mse(a, a) == 0.0
    assert gradient_error(a, a) == 0.0
    assert connectivity_error(a, a) == 0.0


def test_alpha_metrics_worst_case_orderings():
    gt = np.zeros((16, 16))
    good = np.full_like(gt, 0.1)
    bad = np.ones_like(gt)
    assert mae(good, gt) < mae(bad, gt)
    assert mse(good, gt) < mse(bad, gt)
    assert sad(good, gt) < sad(bad, gt)


def test_gradient_error_detects_blur():
    gt = np.zeros((40, 40))
    gt[:, 20:] = 1.0  # sharp vertical edge
    ramp = np.tile(np.clip((np.arange(40) - 12) / 16.0, 0, 1), (40, 1))  # blurred edge
    assert gradient_error(ramp, gt) > gradient_error(gt, gt)


def test_connectivity_penalizes_disconnected_prediction():
    gt = np.zeros((30, 30))
    gt[5:25, 5:25] = 1.0
    connected = gt.copy()
    disconnected = gt.copy()
    disconnected[14:16, :] = 0.0  # cut the blob in two
    assert connectivity_error(disconnected, gt) > connectivity_error(connected, gt)


def test_mmse_requires_binary_gt_and_matches_mse():
    pred = np.clip(RNG.random((8, 8)), 0, 1)
    gt_bin = (RNG.random((8, 8)) > 0.5).astype(int)
    assert mmse_per_image(pred, gt_bin) == mse(pred, gt_bin.astype(float))
    try:
        mmse_per_image(pred, np.full((8, 8), 0.5))
        raised = False
    except ValueError:
        raised = True
    assert raised, "mmse must reject non-binary GT"


def test_alpha_report_keys():
    a = np.clip(RNG.random((16, 16)), 0, 1)
    g = (RNG.random((16, 16)) > 0.5).astype(int)
    rep = alpha_metric_report(a, a, gt_binary=g)
    assert set(rep) == {"mae", "sad", "mse", "grad", "conn", "mmse"}


# ---------------------------------------------------------------- binary metrics

def test_binary_identity_and_disjoint():
    m = np.zeros((20, 20), bool)
    m[4:12, 4:12] = True
    other = np.zeros_like(m)
    other[14:18, 14:18] = True
    assert iou(m, m) == 1.0 and dice(m, m) == 1.0 and f_beta(m, m) == 1.0
    assert iou(m, other) == 0.0 and dice(m, other) == 0.0 and f_beta(m, other) == 0.0
    assert boundary_f(m, m) == 1.0


def test_empty_empty_convention():
    e = np.zeros((10, 10), bool)
    assert iou(e, e) == 1.0 and dice(e, e) == 1.0
    assert f_beta(e, e) == 1.0 and boundary_f(e, e) == 1.0


def test_boundary_f_tolerance_behaviour():
    gt = np.zeros((40, 40), bool)
    gt[10:30, 10:30] = True
    shifted = np.zeros_like(gt)
    shifted[12:32, 10:30] = True  # 2 px shift
    assert boundary_f(shifted, gt, tolerance_px=2.0) > boundary_f(shifted, gt, tolerance_px=1.0)


def test_binary_report_keys():
    m = np.zeros((12, 12), bool)
    m[2:9, 3:8] = True
    rep = binary_metric_report(m, m)
    assert set(rep) == {"iou", "dice", "f_beta", "boundary_f"}
    assert all(v == 1.0 for v in rep.values())


# ---------------------------------------------------------------- rank agreement

def test_tau_sign_alignment_same_quality_order():
    # 5 checkpoints; iou (higher better) and mae (lower better) agree on quality.
    iou_scores = np.array([0.9, 0.8, 0.7, 0.6, 0.5])
    mae_scores = np.array([0.05, 0.10, 0.15, 0.20, 0.25])
    assert abs(kendall_tau(iou_scores, mae_scores, "iou", "mae") - 1.0) < 1e-9


def test_tau_detects_constructed_reversal():
    # mae reverses the iou quality order entirely -> tau = -1.
    iou_scores = np.array([0.9, 0.8, 0.7, 0.6, 0.5])
    mae_reversed = np.array([0.25, 0.20, 0.15, 0.10, 0.05])
    assert abs(kendall_tau(iou_scores, mae_reversed, "iou", "mae") - (-1.0)) < 1e-9


def test_tau_matrix_and_topk_reversals():
    names = [f"ckpt{i}" for i in range(5)]
    scores = {
        "iou": np.array([0.9, 0.8, 0.7, 0.6, 0.5]),
        "mae": np.array([0.25, 0.20, 0.15, 0.10, 0.05]),  # fully reversed order
        "dice": np.array([0.91, 0.81, 0.71, 0.61, 0.51]),  # agrees with iou
    }
    metrics, m = tau_matrix(scores)
    i, j = metrics.index("iou"), metrics.index("dice")
    assert abs(m[i, j] - 1.0) < 1e-9
    k = metrics.index("mae")
    assert abs(m[i, k] - (-1.0)) < 1e-9
    # Fully reversed order of 5: ckpt2 is rank 3 under BOTH metrics, so only
    # ckpt0 (1 -> 5) and ckpt1 (2 -> 4) leave the top-3.
    revs = top_k_reversals(scores, names, "iou", "mae", k=3)
    assert {r.checkpoint for r in revs} == {"ckpt0", "ckpt1"}
    assert all(r.rank_a <= 3 < r.rank_b for r in revs)


def test_bootstrap_tau_ci_contains_point_for_stable_ranking():
    n_ckpt, n_img = 5, 60
    base_quality = np.linspace(0.9, 0.5, n_ckpt)[:, None]
    per_img_iou = np.clip(base_quality + 0.01 * RNG.standard_normal((n_ckpt, n_img)), 0, 1)
    per_img_mae = np.clip((1 - base_quality) / 4 + 0.005 * RNG.standard_normal((n_ckpt, n_img)), 0, 1)
    out = bootstrap_tau({"iou": per_img_iou, "mae": per_img_mae}, "iou", "mae", n_boot=200)
    assert out["ci"][0] <= out["tau"] <= out["ci"][1]
    assert out["tau"] > 0.8  # constructed to agree


# ---------------------------------------------------------------- baselines

def test_rgb_to_hsv_known_colors():
    img = np.zeros((1, 3, 3))
    img[0, 0] = [1.0, 0.0, 0.0]   # red
    img[0, 1] = [0.5, 0.5, 0.5]   # gray
    img[0, 2] = [0.0, 0.0, 0.0]   # black
    hsv = rgb_to_hsv(img)
    assert hsv[0, 0, 1] == 1.0 and hsv[0, 0, 2] == 1.0        # red: S=1, V=1
    assert hsv[0, 1, 1] == 0.0 and abs(hsv[0, 1, 2] - 0.5) < 1e-12  # gray: S=0
    assert hsv[0, 2, 2] == 0.0                                 # black: V=0


def test_hsv_smoke_score_prefers_gray_over_saturated():
    img = np.zeros((10, 20, 3))
    img[:, :10] = [0.6, 0.6, 0.6]   # smoke-like gray
    img[:, 10:] = [0.9, 0.1, 0.1]   # saturated red
    score = hsv_smoke_score(img)
    assert score[:, :10].mean() > 0.9
    assert score[:, 10:].mean() < 0.1


def test_dark_channel_floor_orders_hazy_above_clear():
    # Clear scene: dark, colorful blocks -> low alpha. Hazy: washed towards white.
    clear = np.zeros((30, 30, 3))
    clear[:15, :, 0] = 0.6   # red-ish half
    clear[15:, :, 2] = 0.6   # blue-ish half
    veil = 0.7
    hazy = np.clip(clear * (1 - veil) + veil, 0, 1)  # white veil composite
    a_clear = smoke_alpha_dark_channel(clear, patch=5)
    a_hazy = smoke_alpha_dark_channel(hazy, patch=5)
    assert a_hazy.mean() > a_clear.mean()
    t = transmission(hazy, patch=5)
    assert t.min() >= 0.0 and t.max() <= 1.0


# ---------------------------------------------------------------- alpha recovery

def test_background_inversion_recovers_known_alpha():
    # Build a synthetic composite with KNOWN alpha, then invert it. This validates
    # the recovery code path; on real data F is estimated/calibrated (protocol §4).
    h, w = 40, 40
    background = np.stack(
        [0.2 + 0.3 * RNG.random((h, w)), 0.3 + 0.3 * RNG.random((h, w)), 0.25 + 0.3 * RNG.random((h, w))],
        axis=2,
    )
    smoke_f = np.array([0.85, 0.85, 0.85])
    yy, xx = np.mgrid[0:h, 0:w]
    alpha_true = np.clip(1.2 * np.exp(-(((yy - 20) ** 2 + (xx - 20) ** 2) / 150.0)), 0, 1)
    frame = alpha_true[..., None] * smoke_f[None, None, :] + (1 - alpha_true[..., None]) * background

    rec = recover_alpha(frame, background, smoke_color=smoke_f)
    assert rec.valid.mean() > 0.5, "most pixels should pass QC on this synthetic scene"
    err = np.abs(rec.alpha[rec.valid] - alpha_true[rec.valid])
    assert err.max() < 1e-6, "exact inversion expected on noiseless synthetic composite"
    assert rec.exclusion_counts["valid"] == int(rec.valid.sum())


def test_background_inversion_masks_ill_conditioned_pixels():
    h, w = 20, 20
    background = np.full((h, w, 3), 0.5)
    background[:5] = 0.84  # nearly equals smoke color -> unidentifiable region
    smoke_f = np.array([0.85, 0.85, 0.85])
    alpha_true = np.full((h, w), 0.4)
    frame = alpha_true[..., None] * smoke_f + (1 - alpha_true[..., None]) * background
    rec = recover_alpha(frame, background, smoke_color=smoke_f, conditioning_min=0.08)
    assert not rec.valid[:5].any(), "F ~= B region must be excluded"
    assert rec.valid[10:].all()
    assert np.isnan(rec.alpha[:5]).all()


def test_estimate_background_median_suppresses_transients():
    frames = [np.full((8, 8, 3), 0.4) for _ in range(9)]
    frames[0] = np.full((8, 8, 3), 1.0)  # one transient bright frame
    bg = estimate_background(frames)
    assert np.allclose(bg, 0.4)


# ---------------------------------------------------------------- rater ceiling

def test_rater_ceiling_identical_masks_is_one():
    m = np.zeros((15, 15), bool)
    m[3:10, 3:10] = True
    res = pairwise_iou_ceiling([m, m.copy(), m.copy()])
    assert res["mean"] == 1.0 and res["min"] == 1.0


def test_rater_ceiling_detects_disagreement_and_soft_mae():
    a = np.zeros((15, 15), bool)
    a[3:10, 3:10] = True
    b = np.zeros_like(a)
    b[5:12, 5:12] = True
    res = pairwise_iou_ceiling([a, b])
    assert 0.0 < res["mean"] < 1.0
    soft = [a.astype(float), b.astype(float)]
    res_soft = pairwise_mae_ceiling(soft)
    assert res_soft["mean"] > 0.0


def test_ceiling_summary_and_confrontation():
    vals = [0.6, 0.7, 0.8, 0.65, 0.75, 0.7]
    summ = ceiling_summary(vals, strata=[0, 0, 1, 1, 2, 2])
    assert summ["pooled"]["n"] == 6 and 0 in summ["per_stratum"]
    rows = confront_with_published_deltas(
        ceiling_median_iou=0.7,
        published_deltas=[
            {"benchmark": "toy", "method_pair": "A-B", "delta_iou": 0.02, "source": "unit-test-row"},
            {"benchmark": "toy", "method_pair": "B-C", "delta_iou": 0.40, "source": "unit-test-row"},
        ],
    )
    assert rows[0]["sub_ceiling"] is True   # 0.02 < 0.30 gap
    assert rows[1]["sub_ceiling"] is False  # 0.40 > 0.30 gap


# ---------------------------------------------------------------- probe stub

def test_probe_registry_stub_raises_with_instructions():
    from alphasmoke.probes.encoder_linear_probe import ENCODER_REGISTRY, load_encoder

    assert {"matting_vitb", "cocoseg_vitb", "imagenet_vitb"} <= set(ENCODER_REGISTRY)
    try:
        load_encoder("matting_vitb")
        raised = False
    except NotImplementedError as e:
        raised = "runbook step R2" in str(e)
    assert raised, "stub must raise with actionable instructions"


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS {name}")
            except AssertionError as exc:
                failures += 1
                print(f"FAIL {name}: {exc}")
            except Exception as exc:  # noqa: BLE001
                failures += 1
                print(f"ERROR {name}: {type(exc).__name__}: {exc}")
    print(f"\n{'ALL SELF-CHECKS PASSED' if failures == 0 else f'{failures} FAILURES'}")
    sys.exit(1 if failures else 0)
