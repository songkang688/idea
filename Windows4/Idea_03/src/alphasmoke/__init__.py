"""AlphaSmoke — Windows4 Idea_03 (P103 matting->smoke transfer + P096 metric protocol).

Package status: instrument code for a pre-registered plan. Nothing in this package
produces or contains experimental results; it implements the measurement protocol
specified in ``metrics_protocol.md``.

Subpackages
-----------
metrics         alpha-error suite (MAE/SAD/MSE/mMse/Grad/Conn), binary suite
                (IoU/Dice/F-beta/boundary-F), rank agreement (Kendall tau matrix,
                reversal enumeration, bootstrap CIs).
baselines       training-free physics/color floors (B6): dark-channel transmission,
                HSV low-chroma rule.
alpha_recovery  measured-alpha real arm (B3): compositing inversion against known
                pre-smoke backgrounds with validity and sensitivity masks.
probes          week-1 killer experiment stub: frozen-encoder linear probe (torch).
rater           inter-rater ceiling statistics and confrontation table (B5).
"""

__version__ = "0.1.0"
