# AlphaSmoke — Reviewer-#2 Attack Ledger → Design Answers

Every attack mounted against P103 (`stage4_r2_setA.md`) and P096 (`stage4_r2_setC.md`)
with the design element that answers it. Attacks are quoted by substance, not
paraphrased into weaker forms. Residual risks that no design removes are listed last —
they stay in the paper as limitations, not footnotes.

## P103 attacks (R2 Set A)

| # | Attack | Design answer | Where |
|---|---|---|---|
| A1 | **Synthetic-alpha circularity**: DS0x alpha GT is produced by the compositing op matting models invert; winning alpha-MAE there shows benchmark-process alignment, not transfer | Synthetic alpha demoted to SECONDARY with the caveat printed verbatim; PRIMARY endpoint is real-smoke binary (B2); soft-boundary mechanism tested on **measured** real alpha (B3) instead | proposal §4.3, §5.2 |
| A2 | **Real labels binary+noisy** ⇒ mechanism untestable where the claim matters | Measured-alpha real arm gives a soft real endpoint without annotators; rater study bounds what binary labels can certify | proposal §5.2–5.3 |
| A3 | **Pretrain scale/diversity confound** (matting corpora 10³–10⁴ vs seg 10⁵–10⁷) | Controlled pretrains from common ImageNet init; matched-image-count seg subsample cell (B8); public-ckpt cells demoted to supporting evidence | proposal §4.1 |
| A4 | **Head-alignment confound** (matting arm arrives with alpha-head warm start) | Arm S+cal: seg pretrain + generic-composite alpha-head calibration (B7); kill K-A3 if S+cal ≈ M | proposal §4.1; plan §2 |
| A5 | **Mechanism unisolated**: "matting wins" could be data provenance, not soft labels | Arm MB: same images, same budget, binarized labels (B1); kill K-A2 if M ≈ MB | proposal §4.1; plan §2 |
| A6 | **Significance**: "pretrain A beats B on niche C" is a data point, not a law | The claim is the *ordering* M > MB > S (mechanism), the budget-dependence (gap grows as N shrinks), and the Part-B protocol that generalizes beyond smoke; practitioner line ("start from matting ckpt") is a corollary, not the headline | proposal §1 |
| A7 | Hidden assumption: portrait/hair boundary statistics ≠ volumetric-media ramps | Acknowledged as the *content* of the bet: if boundary-statistics mismatch dominates, K-A1/K-A4 fire and the negative is reported; the probe tests it in week 1 for ~1 GPU-day | proposal §4.4 |

## P096 attacks (R2 Set C)

| # | Attack | Design answer | Where |
|---|---|---|---|
| C1 | **Strawman on the field's metrics**: SMOKE5K already reports mMse+Fβ (FoSp `[V]`); AusSmoke reports IoU/F1/MSE | mMse and Fβ are first-class τ-matrix columns (B4); pre-registered kill K-B1: if mMse-on-binary rankings already agree with alpha-MAE rankings (τ>0.8), pillar 1 dies and we print that the field's metric suffices; if not, FoSp's table is motivation, not refutation | plan §2; metrics_protocol §2.2–2.3, §3 |
| C2 | **The matting turn already happened** (SFMattingNet `[V]`) | SFMattingNet scored inside the pool (B9); the paper is framed as the validity audit the turn skipped — no published evidence yet shows binary leaderboards mis-rank; we supply or refute it | proposal §5.1; datasets §4 |
| C3 | **Alpha-GT circularity / real alpha unobservable** (the strongest vector; verdict-flipping) | Measured-alpha arm (B3): compositing inversion against known pre-smoke backgrounds; exposure lock, saturation & conditioning exclusions, F-sensitivity maps; reversal claim survives only if synthetic and measured rankings agree against binary (K-B3 otherwise converts the finding into "synthetic alpha mis-ranks") | proposal §5.2; metrics_protocol §4; `src/alphasmoke/alpha_recovery/` |
| C4 | **Ceiling half is second** (disagreement already measured elsewhere) | Ceiling pillar is a *confrontation*, not a discovery claim: pairwise ceilings on the RGB benchmarks the field actually ranks on, overlaid with that field's own published deltas; pre-registered demotion K-B4 (>0.85 → appendix) | proposal §5.3; plan §2 |

## Cross-cutting scope attack (Stage-3 §10, stage6)

| # | Attack | Design answer |
|---|---|---|
| X1 | Drift into detector-prompted fire SAM (S-126 territory, folded elsewhere; ProFSAM exists `[S3]`) | Hard scope guard B10: no detector produces prompts anywhere; SAM only as auto-mode scored checkpoint; any prompt-quality result is cut. Enforced in `configs/eval_protocol.yaml` (pool spec has no detector field) and experiments.md §6 |

## Skeleton-package attacks (carried from the supervisor's initial Idea_03 sketch)

| # | Attack | Design answer |
|---|---|---|
| S1 | "Matting Anything already put an alpha head on SAM" | We claim no architecture. A1-046 was KILLED at Stage 3 for exactly this reason; the claim here is *pretraining-data provenance* (M vs MB vs S arms), and MAM itself sits in the Part-B pool as a scored checkpoint |
| S2 | "The HSV/physics floor is already enough on white smoke" | Then that **is** the paper: pre-registered outcome K-A5 reports floor-dominated budgets, and a floors-beat-foundation-models result is a publishable negative about learned transfer, printed as such |

## Residual risks (no design removes them — printed as limitations)

1. **Scoop velocity** around MAM applications and the matting turn (Stage-3 Medium
   confidence on S-103). Mitigation is ordering, not design: week-1 probe and eval-only
   Part B front-load the publishable core; backup slots (P063/P079) exist per
   `stage4_top20.md`.
2. **Measured-alpha model validity**: locally-uniform smoke color and single
   scattering are approximations; violations are masked/priced (sensitivity maps), not
   eliminated. A reviewer can still argue recovered α is model-laden; the answer in
   the paper is that it is *differently* model-laden than synthetic GT and annotator
   masks, and agreement across the three is exactly what the protocol measures.
3. **Venue ceiling**: evaluation science for a small field (Set C's own note). The
   package accepts this; the τ protocol and measured-alpha tooling are the durable
   artifacts either way.
4. **Checkpoint availability**: pillar 1 needs 8–12 scored checkpoints; if several are
   unobtainable, the τ matrix loses power. Pre-registered floor: publish pool size and
   the "attempted, unavailable" list; if pool < 6, the τ matrix is reported as
   underpowered and the reversal claim is not made.
