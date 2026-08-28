"""Hook for real SAM. Fill checkpoint path when weights exist. Do not commit weights."""

def load_sam_encoder(checkpoint: str | None = None):
    raise NotImplementedError(
        "Load official segment-anything or sam2 image encoder, freeze parameters, "
        "return embeddings at 1/16 or 1/4 scale. Checkpoint must stay off git."
    )
