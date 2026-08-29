"""amgclust — Is SAM AMG intensity clustering on CT?

Windows6 / Idea_01. Every number this package can currently produce is
SYNTHETIC. There are no real SAM measurements anywhere in Windows6.

Hard dependency: numpy. scipy and PyYAML are optional accelerants; the
package runs and the smoke tests pass without them.
"""

from .config import Config, load_config, set_seed
from .metrics import (
    adjusted_rand_index,
    boundary_f,
    cardinality_ratio,
    coverage_iou,
    hungarian_iou,
    label_boundaries,
    masks_to_label_map,
)
from .interventions import (
    intensity_remap,
    sobel_magnitude,
    texture_shuffle,
    check_remap_is_monotone,
    check_shuffle_preserves_tile_means,
)
from .segmenters import (
    amg_mock,
    connected_components,
    gmm_1d,
    kmeans_1d,
    multi_otsu,
    sam_amg,
    slic_lite,
)
from .data import load_real_ct_slices, synthetic_ct
from .pipeline import AgreementProfile, agreement_profile, counterfactual_profile

PLACEHOLDER_BANNER = (
    "=" * 72
    + "\nSYNTHETIC / PLACEHOLDER OUTPUT — NOT A SCIENTIFIC RESULT.\n"
    + "No SAM weights and no real CT data were used. The 'AMG' here is a\n"
    + "multi-threshold connected-component stand-in. These numbers test the\n"
    + "harness, not the hypothesis. Label them HYPOTHESIS, never ACTUAL RESULT.\n"
    + "=" * 72
)

__all__ = [
    "Config",
    "load_config",
    "set_seed",
    "hungarian_iou",
    "coverage_iou",
    "cardinality_ratio",
    "adjusted_rand_index",
    "boundary_f",
    "label_boundaries",
    "masks_to_label_map",
    "intensity_remap",
    "texture_shuffle",
    "sobel_magnitude",
    "check_remap_is_monotone",
    "check_shuffle_preserves_tile_means",
    "kmeans_1d",
    "multi_otsu",
    "gmm_1d",
    "slic_lite",
    "amg_mock",
    "sam_amg",
    "connected_components",
    "synthetic_ct",
    "load_real_ct_slices",
    "agreement_profile",
    "counterfactual_profile",
    "AgreementProfile",
    "PLACEHOLDER_BANNER",
]
