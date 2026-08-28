"""SeeingInside (Windows4 / Idea_01 / P14): null-calibrated counterfactual audit of
image-evidence reliance in box-prompted promptable segmenters.

Prototype scope: killer-experiment harness (E0/E1 scaffold). Stub backends stand in for
frozen SAM when official weights are unavailable; the OfficialSAMWrapper interface is the
drop-in for real runs. No scientific results are produced by the stub backends — they
validate the decision logic only (see experiments.md, E0).
"""

__version__ = "0.1.0"
