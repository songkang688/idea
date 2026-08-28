"""WiSE-FT interpolation and RetainSAM losses. Prototype — no trained weights."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple

import torch
import torch.nn.functional as F


def wise_ft_state_dicts(
    theta0: Dict[str, torch.Tensor],
    theta_ft: Dict[str, torch.Tensor],
    alphas: Iterable[float],
) -> List[Tuple[float, Dict[str, torch.Tensor]]]:
    """Linear blend in weight space. Keys must match."""
    out = []
    for a in alphas:
        blended = {}
        for k, v0 in theta0.items():
            if not torch.is_floating_point(v0):
                blended[k] = v0.clone()
                continue
            blended[k] = (1.0 - a) * v0 + a * theta_ft[k]
        out.append((float(a), blended))
    return out


def dice_ce_loss(
    logits: torch.Tensor,
    target: torch.Tensor,
    eps: float = 1e-6,
) -> torch.Tensor:
    """logits: (B,1,H,W), target: (B,1,H,W) in {0,1}."""
    ce = F.binary_cross_entropy_with_logits(logits, target)
    p = torch.sigmoid(logits)
    num = 2.0 * (p * target).sum(dim=(1, 2, 3))
    den = p.sum(dim=(1, 2, 3)) + target.sum(dim=(1, 2, 3)) + eps
    dice = 1.0 - (num / den).mean()
    return ce + dice


def retain_loss(
    student_logits: torch.Tensor,
    teacher_logits: torch.Tensor,
    teacher_as_hard: bool = True,
) -> torch.Tensor:
    """Distill teacher SAM masks on replay prompts."""
    if teacher_as_hard:
        target = (teacher_logits.detach() > 0).float()
        return dice_ce_loss(student_logits, target)
    return F.mse_loss(student_logits, teacher_logits.detach())


@dataclass
class RetainObjective:
    lambda_ret: float = 1.0
    encoder_l2: float = 0.0

    def __call__(
        self,
        tgt_logits: torch.Tensor,
        tgt_mask: torch.Tensor,
        replay_student: torch.Tensor,
        replay_teacher: torch.Tensor,
        student_enc: torch.nn.Module | None = None,
        teacher_enc: torch.nn.Module | None = None,
    ) -> torch.Tensor:
        loss = dice_ce_loss(tgt_logits, tgt_mask)
        loss = loss + self.lambda_ret * retain_loss(replay_student, replay_teacher)
        if self.encoder_l2 > 0 and student_enc is not None and teacher_enc is not None:
            extra = 0.0
            for p, q in zip(student_enc.parameters(), teacher_enc.parameters()):
                extra = extra + torch.sum((p - q.detach()) ** 2)
            loss = loss + self.encoder_l2 * extra
        return loss


def iou(pred_bin: torch.Tensor, target: torch.Tensor, eps: float = 1e-6) -> torch.Tensor:
    inter = (pred_bin * target).sum(dim=(1, 2, 3))
    union = pred_bin.sum(dim=(1, 2, 3)) + target.sum(dim=(1, 2, 3)) - inter
    return (inter + eps) / (union + eps)


def dominates_pareto(
    candidate: List[Tuple[float, float]],
    baseline: List[Tuple[float, float]],
    min_points: int = 2,
) -> bool:
    """Each tuple is (J_tgt, J_gen), higher better.

    A candidate point dominates a baseline point if ≥ in both and > in one.
    We count how many candidate points strictly dominate at least one baseline
    point without being dominated. Crude; for the kill test plot in experiments.md.
    """
    wins = 0
    for ct, cg in candidate:
        if any(ct >= bt and cg >= bg and (ct > bt or cg > bg) for bt, bg in baseline):
            if not any(bt >= ct and bg >= cg and (bt > ct or bg > cg) for bt, bg in baseline):
                wins += 1
    return wins >= min_points
