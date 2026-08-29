"""Register-signature and invariance instrumentation for the B-0114 arms.

These are the *mechanism* metrics of this prototype. They quantify the three
hypothesis axes (all HYPOTHESES, none claimed as fact):

1. **Location / register geometry** — do injected slots behave like
   attention sinks? Measured as ``sink_mass``: the mean attention mass that
   patch-token *queries* place on prompt slots (and, separately, on register
   slots), per layer. A token can have high sink mass with zero content
   (see the sink_only arm), so this is a geometry statistic, not a content
   statistic.

2. **Learned embedding** — token output-norm statistics
   (``token_norm_stats``): prompt-slot output norms vs patch-token norms,
   plus the fraction of patch tokens whose norm exceeds mean + 3 sd
   ("outlier fraction", the classic register-artifact signature shape).
   NOTE: these norms are reported as *signatures of register-like behavior
   only*. Whether patch-norm maps predict per-pixel error is B-0001's
   question and lives exclusively in ``b0001_hook.py`` (see the dissociation
   plan in exp_02); nothing in this module compares norms to errors.

3. **Dense-task invariance breaking** — ``nuisance_sensitivity``: mean
   relative displacement of patch-token features when *only* the scene-global
   illumination g is resampled (paired renders of identical layouts). A
   perfectly local (invariant) feature would move only via its own pixel
   values' change under g; a feature contaminated by global aggregation
   moves more. Comparing this across arms asks: do injected tokens absorb
   the global computation and leave patch features more local?
"""

from __future__ import annotations

import torch

from .config import ExperimentConfig
from .synthetic_data import SceneBatch
from .tiny_vit import TinyViT


@torch.no_grad()
def sink_mass(
    backbone: TinyViT,
    prompt: torch.Tensor | None,
    prompt_is_sink: bool,
    images: torch.Tensor,
) -> dict:
    """Mean attention mass from patch queries onto prompt / register slots,
    per layer (averaged over heads, batch, and patch queries)."""
    out = backbone(images, prompt=prompt, prompt_is_sink=prompt_is_sink, capture_attn=True)
    layout = out["layout"]
    per_layer_prompt, per_layer_register = [], []
    for attn in out["attn"]:  # (B, H, T, T)
        patch_q = attn[:, :, layout["patch"], :]  # queries from patch slots
        p = layout["prompt"]
        r = layout["register"]
        prompt_mass = (
            patch_q[:, :, :, p].sum(dim=-1).mean().item() if p.stop > p.start else 0.0
        )
        reg_mass = (
            patch_q[:, :, :, r].sum(dim=-1).mean().item() if r.stop > r.start else 0.0
        )
        per_layer_prompt.append(prompt_mass)
        per_layer_register.append(reg_mass)
    return {
        "prompt_sink_mass_per_layer": per_layer_prompt,
        "register_sink_mass_per_layer": per_layer_register,
        "prompt_sink_mass_mean": float(sum(per_layer_prompt) / len(per_layer_prompt)),
        "register_sink_mass_mean": float(sum(per_layer_register) / len(per_layer_register)),
    }


@torch.no_grad()
def token_norm_stats(
    backbone: TinyViT,
    prompt: torch.Tensor | None,
    prompt_is_sink: bool,
    images: torch.Tensor,
) -> dict:
    """Output-norm statistics. Signatures only — no error comparison here
    (that is B-0001 territory, see b0001_hook.py)."""
    out = backbone(images, prompt=prompt, prompt_is_sink=prompt_is_sink)
    patch_norms = out["patch_tokens"].norm(dim=-1)  # (B, N)
    mean, sd = patch_norms.mean(), patch_norms.std()
    outlier_frac = (patch_norms > mean + 3 * sd).float().mean().item()
    stats = {
        "patch_norm_mean": float(mean),
        "patch_norm_sd": float(sd),
        "patch_norm_outlier_frac": float(outlier_frac),
    }
    if out["prompt_tokens"] is not None:
        pn = out["prompt_tokens"].norm(dim=-1)
        stats["prompt_norm_mean"] = float(pn.mean())
        stats["prompt_to_patch_norm_ratio"] = float(pn.mean() / (mean + 1e-8))
    return stats


@torch.no_grad()
def nuisance_sensitivity(
    backbone: TinyViT,
    prompt: torch.Tensor | None,
    prompt_is_sink: bool,
    paired: SceneBatch,
    cfg: ExperimentConfig,
) -> dict:
    """Relative patch-feature displacement under a global-nuisance swap.

    paired must come from generate_batch(..., paired_g=True): identical
    layouts, independent illumination g. Lower = patch features more
    invariant to the global nuisance (more purely local).
    """
    assert paired.images_alt is not None, "need paired_g batch"
    bs = cfg.train.batch_size
    disps, scales = [], []
    for i in range(0, paired.images.shape[0], bs):
        f1 = backbone(
            paired.images[i : i + bs], prompt=prompt, prompt_is_sink=prompt_is_sink
        )["patch_tokens"]
        f2 = backbone(
            paired.images_alt[i : i + bs], prompt=prompt, prompt_is_sink=prompt_is_sink
        )["patch_tokens"]
        disps.append((f1 - f2).norm(dim=-1))
        scales.append(0.5 * (f1.norm(dim=-1) + f2.norm(dim=-1)))
    disp = torch.cat(disps).flatten()
    scale = torch.cat(scales).flatten()
    rel = (disp / (scale + 1e-8)).mean().item()
    return {"nuisance_rel_displacement": float(rel)}


@torch.no_grad()
def collect_signatures(
    backbone: TinyViT,
    prompt: torch.Tensor | None,
    prompt_is_sink: bool,
    val: SceneBatch,
    paired: SceneBatch,
    cfg: ExperimentConfig,
) -> dict:
    imgs = val.images[: cfg.train.batch_size]
    return {
        **sink_mass(backbone, prompt, prompt_is_sink, imgs),
        **token_norm_stats(backbone, prompt, prompt_is_sink, imgs),
        **nuisance_sensitivity(backbone, prompt, prompt_is_sink, paired, cfg),
    }
