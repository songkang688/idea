"""PromptAmnesia prototype (Windows4/Idea_02).

Prompt-type-resolved behavioral forgetting in fine-tuned promptable segmenters:
P082 noise-floor gate, P065 prompt-type battery + C1-061 oracle-gap diversity
decomposition, P177 splice/stitch mechanism arm.

This package contains protocol logic only. It generates no experimental results;
model weights and datasets are external assets pinned at pre-registration time.
"""

__version__ = "0.1.0"

EPISTEMIC_NOTICE = (
    "PROTOTYPE: no output of this package is an experimental result unless it "
    "carries a RunArtifact {config_hash, seed, commit} produced from real assets."
)
