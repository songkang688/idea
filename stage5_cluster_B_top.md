# Stage 5 — Cluster B Top Nominees

**Experimental Engineer (Cloud Sub-Agent N) → Supervisor Windows7.**
Ranked by ROI (decisiveness per A100-day, headline value, failure-branch informativeness) over
the 7 Stage-4 survivors. Full designs in `stage5_cluster_B_engineering.md`.

## Ranking (all 7)

| Rank | ID | Program | ROI | MVE cost | Full cost | Verdict |
|------|----|---------|-----|----------|-----------|---------|
| 1 | B-0121 (P) | Wrong-support counterfactual FSS audit | 9 | ~1 A100-day | ~5 A100-days | **KEEP — Nominee 1** |
| 2 | B-0212 | Blending-artifact detectability → transfer-gap law | 8 | ~6 A100-days | ~40–45 A100-days | **KEEP — Nominee 2** |
| 3 | M5 (B-0362) | Decision-flip-rate audit of published SOTA deltas | 8 | desk survey + ~2 A100-days | ~8–10 A100-days | **CONDITIONAL 3rd** (exceptional + cheap; gated on desk survey) |
| 4 | B-0222 | Thin-structure fidelity floor protocol | 7 | ~1 A100-day | ~35 A100-days | DROP from Stage-5 slate |
| 5 | B-0230 (P) | Label-cleanliness vs image-distribution decomposition | 7 | ~4–6 A100-days | ~55–70 A100-days | DROP from Stage-5 slate |
| 6 | B-0331 | Negation mining → spatial negative supervision | 6 | ~4 A100-days | ~25–30 A100-days | DROP from Stage-5 slate |
| 7 | B-0112 (+M4) | Convention-shift program (3 legs) | 6 | ~3 A100-days | ~30–40 A100-days + annotation | DROP from Stage-5 slate |

"DROP from Stage-5 slate" = not nominated for immediate execution; designs remain live in the
engineering file and several have cheap MVEs worth running opportunistically (see Salvage notes).

---

## Nominee 1 — B-0121: Wrong-support counterfactual audit of few-shot segmentation (ROI 9)

**Why it wins.** Cheapest decisive experiment in the cluster: zero training, ≤ 5 A100-days total,
all checkpoints public and verified this session (PFENet, HSNet, BAM, Matcher, PerSAM, FSSAM,
SegGPT). Every outcome branch publishes: high retention → the field's headline metric is partly
saliency and the leaderboard reorders; low retention → the field's validity is certified by the
first counterfactual audit; benchmark-degenerate retention → the distractor-enriched split
becomes the mandatory fix. No published counterfactual audit exists (Stage-4 search: only
mitigation methods).

**Killer experiment.** Stratified wrong-support counterfactual with support-free floor: on the
pre-registered distractor-present stratum, ≥ half of specialist methods retain > 50% IoU under
wrong-class supports AND are statistically indistinguishable from the support-free objectness
floor. Both legs failing = certification result published instead. Killer cost: ~2 A100-days.

**Start-next-week plan.** Day 1–2: support-injection wrappers for PFENet/BAM/Matcher. Day 3: MVE
(PASCAL-5i + COCO-20i fold 0). Go/no-go gate. Week 2: full method panel, strata, floors,
sensitivity-adjusted leaderboard.

---

## Nominee 2 — B-0212: Blending-artifact detectability → synthetic-to-real transfer-gap law (ROI 8)

**Why it wins.** The only survivor with a fully causal design answering both of its Stage-4
attacks inside one ladder: fixed-content compositing rungs isolate the artifact channel from
generator quality; reverse artifact-injection converts "detectable" into "used." The entire stack
is public and verified this session (SyntheticTumors lesion synthesis, DiffTumor training
pipeline + healthy-CT assets, libcom compositing/harmonization/inharmony-scoring). Deliverable
the field adopts on day one: probe-AUROC as a hygiene number for any synthesis pipeline. Failure
branches are cheap and citable (compositing-doesn't-matter null, or detectable-≠-used boundary).

**Killer experiment.** Fixed-content ladder + reverse injection: Spearman ρ(probe AUROC,
real DSC) ≤ −0.8 across ≥ 5 compositing arms at fixed generator/content, AND artifact injection
into the best-blended arm reopening ≥ 50% of the real-DSC spread. Either leg failing kills the
law. Killer cost: ~15 A100-days (subset).

**Start-next-week plan.** Day 1–3: compositing ladder generation on MSD Task03 healthy CTs
(libcom arms i–iv). Day 4: probe sanity gate (cut-paste AUROC > 0.9, < 0.5 A100-day). Week 2–3:
MVE (3 arms × 1 seed, ~6 A100-days), then full ladder on go.

---

## Conditional 3rd — M5: Decision-flip-rate audit of published SOTA deltas (ROI 8)

**Why nominated (exceptional + cheap).** Near-zero GPU (~8–10 A100-days, inference only); the
headline is field-level ("X% of published SOTA claims flip under guideline-derived decision
rules"); non-vacuity is already evidenced by Stage-4's RECIST findings (κ 0.67–0.81 category
agreement at DSC ≈ 0.85; up to 37.5% reader-score shifts [inherited]); every branch publishes,
including the reproducibility finding if checkpoints are missing. The null-pair flip-rate floor
and ΔDSC-calibration controls (added in this design) make the number attack-proof against the
rule-selection objection.

**Why conditional, not unconditional.** The one non-engineering risk is sample existence: the
audit needs ≥ 15 auditable published pairs (public checkpoints/predictions). That is checkable
for zero GPU cost. **Condition: run the desk survey (~50 recent SOTA-claiming papers) first; if
≥ 15 auditable pairs, M5 is a full third nominee; if fewer, publish the reproducibility note and
stand down.** DiffTumor's 9 released real-vs-synthetic checkpoint pairs already guarantee the MVE
regardless.

**Killer experiment.** Pre-registered flip surface with null-floor control: excess-over-floor
flips ≥ 30% of small-delta pairs somewhere on the frozen rule surface, concentrating beyond what
the ΔDSC calibration curve predicts. Killer cost: ~4 A100-days after pair collection.

---

## Drop reasons (ranks 4–7)

- **B-0222 (rank 4, ROI 7).** The floor-existence MVE is nearly free and should be run
  opportunistically, but the program's decisive causal arm (matched-compute pixel- vs
  latent-diffusion training) costs ~33 A100-days for a datasheet/protocol payoff — durable, less
  headline-dense per A100-day than the nominees. Dropped on cost-to-ceiling ratio, not validity.
- **B-0230 (rank 5, ROI 7, protected).** Cleanest falsification logic in the cluster, but the
  costliest grid (~55–70 A100-days across 120 runs), and a share-type headline whose
  noise-model sensitivity band — however honestly reported — invites more argument per result
  than a leaderboard reorder or flip rate. Protection honored by keeping the design execution-
  ready; not by a nomination slot.
- **B-0331 (rank 6, ROI 6).** The two-control killer is decisive and the negative branch is
  genuinely valuable, but: credentialed-data engineering is the real cost (parse + ground + audit
  at MIMIC scale), the expected effect is 5–15% relative FP in a CXR-scoped deliverable, and the
  gold evaluation pool thinned this session (CANDID-PTX now access-restricted — verified). Run
  the 4-arm MVE when a credentialed pipeline exists.
- **B-0112+M4 (rank 7, ROI 6).** Highest ceiling and the only methods-flavored survivor, but
  three staged legs, the cluster's only human-annotation budget, and a payoff that requires ≥ 2
  legs to land. Its Leg-1 MVE (direction-of-harm dissociation on BraTS nested labels,
  ~3 A100-days) is the single highest-information cheap experiment among the drops and is the
  first thing to fund if a nominee dies at its gate.

## Salvage notes for the Supervisor

1. If either nominee dies at its MVE gate, promote in order: M5 (if desk survey passed) →
   B-0112 Leg-1 MVE → B-0222 Arm-A MVE. All three gates together cost < 6 A100-days.
2. B-0121's distractor-enriched split and M5's rule-surface harness are shared-infrastructure
   candidates for later stages (evaluation-validity axis of the portfolio).
3. No nominee collides with Cluster A or C killer experiments (dedup table at the end of
   `stage5_cluster_B_engineering.md`).
