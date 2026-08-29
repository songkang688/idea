# Idea_03 — Selective SAM via IoU-token Recalibration

Status: HYPOTHESIS. No reliability diagrams measured.

## Executive summary

**One sentence:** SAM/SAM2 IoU tokens are calibrated on SA-1B-like objects and **anti-calibrated** on amorphous/low-contrast masks; a reject option + isotonic recalibration raises risk-coverage Dice more than Med-SA-sized adapters.

## Motivation

KNOWN FACT: SAM2 exposes `iou_predictions`. EVIDENCE: engineering notes tell practitioners to threshold ~0.5. Papers almost never report **reliability diagrams** on smoke/Trans10K/medical.

## Hypotheses

**H1:** On COCO objects, IoU-token vs true IoU has positive Spearman ρ and ECE below a pre-registered bound.

**H2:** On amorphous sets, ρ drops and may go **negative** (anti-calibration): high token, low true IoU.

**H3:** Selective prediction (cover 80% of pixels/images) using recalibrated scores beats a parameter-matched adapter on covered Dice, and is honest about the rejected tail.

## Novelty

Not “use the confidence score.” The claim is **domain-dependent miscalibration of the IoU head** and a method that is a **reject option**, not another mask decoder.

Closest: selective classification (Geifman & El-Yaniv); SAM2 API. Difference: dense prediction + demonstrated anti-calibration.

## Method

Map IoU token \(s\) through isotonic regression on a val split. Reject if \(\hat{\mathrm{IoU}} < \tau\). Report risk-coverage curves.

Optional: train a 1×1 calibrator on frozen decoder features (Idea_01-compatible).

## Killer

Zero training: dump SAM2 IoU tokens vs GT IoU on 100 COCO vs 100 Trans10K/smoke. Plot reliability. **Kill H2** if ρ stays high on amorphous.

## Expected

H1 true, H2 true, coverage 80% recovers most of the “SAM is bad on glass” gap by abstaining.

## Reviewer #2

“Trivial thresholding.” Shut up with anti-calibration + risk-coverage vs adapter at equal extra params. If only weakly calibrated, kill and merge into Idea_01 analysis figure.
