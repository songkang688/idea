"""Optional SAM wrapper. Never fabricates scores if weights are missing."""
from __future__ import annotations
from typing import Optional
import numpy as np

class SamOrSkip:
    def __init__(self, checkpoint: Optional[str] = None):
        self.ok = False
        self._predictor = None
        if not checkpoint:
            return
        try:
            from segment_anything import SamPredictor, sam_model_registry
            sam = sam_model_registry["vit_b"](checkpoint=checkpoint)
            self._predictor = SamPredictor(sam)
            self.ok = True
        except Exception:
            self.ok = False

    def predict_box(self, image: np.ndarray, box: tuple[int, int, int, int]) -> Optional[np.ndarray]:
        if not self.ok:
            return None
        self._predictor.set_image(image)
        x0, y0, x1, y1 = box
        masks, _, _ = self._predictor.predict(box=np.array([x0, y0, x1, y1]), multimask_output=False)
        return masks[0].astype(np.uint8)
