"""Training-free physics/color floors (binding obligation B6).

Every learned arm in Part A is compared against these floors under the identical
scoring protocol; cells that do not beat both floors are reported as
"below physics floor" (proposal.md section 4.2, kill condition K-A5).
"""

from .color_hsv import hsv_smoke_score, hsv_smoke_mask, rgb_to_hsv
from .dark_channel import (
    dark_channel,
    estimate_atmospheric_light,
    transmission,
    smoke_alpha_dark_channel,
)

__all__ = [
    "hsv_smoke_score",
    "hsv_smoke_mask",
    "rgb_to_hsv",
    "dark_channel",
    "estimate_atmospheric_light",
    "transmission",
    "smoke_alpha_dark_channel",
]
