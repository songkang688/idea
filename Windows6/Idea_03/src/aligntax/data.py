"""Synthetic base/chat pair, and the GATE-B refusal for real checkpoints.

The simulator is built so that the four possible answers to the research
question can each be planted deliberately:

    none            neither generation nor representation degrades
    format          only free-form generation degrades (chatty wrapper)
    policy          generation AND likelihood degrade; visual tokens intact
    representation  visual tokens themselves degrade, so the probe drops too

`pipeline.classify_outcome` must recover the planted mode from the
measurements alone. That round trip is the only thing the smoke run tests.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class SyntheticPair:
    """One synthetic evaluation set plus 'base' and 'chat' internal states.

    `tokens_base` / `tokens_chat` stand in for frozen visual-token activations.
    They are identical unless the planted mode is `representation` — which is
    exactly the distinction H2 is trying to detect in real models.
    """

    boxes: np.ndarray  # (n, 4) gold boxes
    distractors: np.ndarray  # (n, k, 4) shared distractor boxes for ranking
    tokens_base: np.ndarray  # (n, d)
    tokens_chat: np.ndarray  # (n, d)
    decode_noise_base: float
    decode_noise_chat: float
    chatty_rate_base: float
    chatty_rate_chat: float
    tax_mode: str

    def __len__(self) -> int:
        return len(self.boxes)


def make_pair(cfg, rng: np.random.Generator) -> SyntheticPair:
    """Build a synthetic pair with the degradation named by `cfg.tax_mode`."""
    n, d, s = cfg.n_examples, cfg.token_dim, cfg.image_size

    corner = rng.uniform(0, s * 0.6, size=(n, 2))
    extent = rng.uniform(s * 0.1, s * 0.35, size=(n, 2))
    boxes = np.concatenate([corner, corner + extent], axis=1)

    tokens = rng.normal(size=(n, d))
    tokens[:, :4] = boxes / s + 0.01 * rng.normal(size=(n, 4))

    # Distractors are SHARED between checkpoints so the ranking task is
    # identical for both — otherwise a likelihood gap could come from an easier
    # candidate set rather than from the model.
    jitter = rng.normal(scale=s * 0.15, size=(n, cfg.n_distractors, 4))
    distractors = np.clip(boxes[:, None, :] + jitter, 0, s)

    mode = cfg.tax_mode
    tokens_chat = tokens.copy()
    decode_noise_chat = 0.0
    chatty_chat = 0.0

    if mode == "format":
        chatty_chat = cfg.chatty_rate
    elif mode == "policy":
        chatty_chat = cfg.chatty_rate
        decode_noise_chat = cfg.policy_noise
    elif mode == "representation":
        chatty_chat = cfg.chatty_rate
        decode_noise_chat = cfg.policy_noise
        tokens_chat = tokens + cfg.representation_noise * rng.normal(size=(n, d))

    return SyntheticPair(
        boxes=boxes,
        distractors=distractors,
        tokens_base=tokens,
        tokens_chat=tokens_chat,
        decode_noise_base=0.0,
        decode_noise_chat=decode_noise_chat,
        chatty_rate_base=0.0,
        chatty_rate_chat=chatty_chat,
        tax_mode=mode,
    )


def verify_checkpoint_pair(*_args, **_kwargs) -> None:
    """GATE-B. Not implemented here on purpose."""
    raise NotImplementedError(
        "GATE-B (stage6_battle.md 5) is OPEN. Idea_03's own experiments.md calls "
        "it a 'Hard gate: identical vision encoder + coordinate tokenization', and "
        "no Windows6 artifact records that any base/chat pair was ever checked "
        "for it. Card E-B must confirm, from published model cards and configs: "
        "(1) the two checkpoints share a vision encoder, (2) they share coordinate "
        "tokenization, (3) the licences permit the comparison. Without all three "
        "the stage-isolation claim is unavailable and Idea_03 descopes to a "
        "format-artifact study. Windows6 has run NO VLM eval."
    )
