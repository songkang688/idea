# Stage 6 — Funnel Bias Audit (pre-Final-3)

**Meta-Reviewer / Auditor / Deputy Supervisor (Cloud Sub-Agent R) → Supervisor Windows7.**

**Inputs read (verbatim, from branches):**
- Stage 5 tops + ROI + engineering: `cursor/stage5-cluster-a-engineering-ed30`, `cursor/stage5-cluster-b-engineering-a00b`, `cursor/stage5-cluster-c-engineering-2eff`
- Stage 4 keeps + kills + attacks: `cursor/stage4-cluster-a-reviewer2-f1fa`, `cursor/stage4-cluster-b-reviewer2-b25a`, `cursor/stage4-cluster-c-reviewer2-c1be`
- Windows1 precedent: `research_ledger/meta_audit.md` (main)

**Under audit:** Supervisor-locked Top 5 = A-0017, B-0121, A-0061, B-0212, C-0090.
Alternates = A-0002, M5, C-0028, A-0178, C-0302, B-0230, A-0107.

---

## 1. Funnel census (what actually survived, by genre)

Genre labels: **AUDIT** = evaluation-validity / measurement of frozen models, no lever on training or deployment. **MEAS+INT** = measurement instrument built around an interventional lever (inference-time or data-pipeline intervention). **TRAIN-MECH** = causal test of a training-recipe mechanism, outcome changes how people train. **METHOD/FIX** = proposes or validates a technique/supervision source/fix.

| Stage | Cluster A (7) | Cluster B (7) | Cluster C (7) | Genre tally (21) |
|---|---|---|---|---|
| Stage-4 survivors | A-0002 MEAS+INT · A-0017 MEAS+INT · A-0061 AUDIT · A-0062 AUDIT · A-0107 TRAIN-MECH/METHOD · A-0178 MEAS+INT · A-0271 MEAS+INT | B-0112+M4 METHOD · B-0121 AUDIT · B-0212 MEAS+INT · B-0222 MEAS+INT · B-0230 MEAS+INT · B-0331 METHOD · M5 AUDIT | C-0028 TRAIN-MECH · C-0090 TRAIN-MECH · C-0128 MEAS+INT · C-0158 METHOD/FIX · C-0229 TRAIN-MECH · C-0302 MEAS+INT/FIX · C-0310 MEAS+INT | 4 AUDIT · 10 MEAS+INT · 4 TRAIN-MECH · 3 METHOD |
| Stage-5 nominations (8) | A-0017 · A-0061 · A-0002 | B-0121 · B-0212 · M5(cond.) | C-0090 · C-0028 | 3 AUDIT-leaning · 3 MEAS+INT · 2 TRAIN-MECH · **0 METHOD** |
| Supervisor Top 5 | A-0017 · A-0061 | B-0121 · B-0212 | C-0090 | 2 AUDIT (B-0121, A-0061) · 2 MEAS+INT (A-0017, B-0212) · 1 TRAIN-MECH (C-0090) · **0 METHOD** |

Headline census facts:

1. **Methods went extinct at Stage 5.** Three METHOD-genre survivors existed after Stage 4 (B-0112+M4 convention tokens, B-0331 negation supervision, C-0158 decorrelated acquisition — plus A-0107 as method-adjacent). Zero were nominated. All died on cost-per-decisiveness, not on validity.
2. **The Top 5 is measurement-tilted but not purely audit.** Strict reading: 2 pure audits (B-0121, A-0061), 2 interventional measurements (A-0017, B-0212), 1 training-mechanism test (C-0090). Loose reading (counting A-0017's diagnostic-instrument deliverable as measurement): 3 of 5 measurement-genre. Either way, **selecting any 3-of-5 subset uniformly at random gives a >50% chance of a Final 3 with ≥2 measurement papers** — the diversity constraint must be enforced deliberately, which is what this audit does (§9).

## 2. Finding — the cheapness criterion, not reviewer laziness, produced the audit tilt

All three Stage-5 engineers ranked by decisiveness-per-A100-day (stated explicitly in all three top files), and all three applied an identical "conditional third only if exceptional AND cheap" rule. That rule structurally excludes training-genre ideas from third slots and systematically promotes inference-only designs, because audits of frozen public checkpoints are the cheapest decisive experiments that exist. The correlation in this funnel is near-perfect: every nominee costing <10 A100-days is measurement-genre; both training-genre nominees are the two most expensive survivors nominated.

This is a repeat offense with documented precedent: the Windows1 meta-audit (`research_ledger/meta_audit.md`) records **"Supervisor ACCEPTS: eval over-indexing"** in the prior window. Same pipeline, same failure mode, second occurrence. The bias is in the objective function, not in any individual reviewer.

**Verdict:** real, structural, and partially self-corrected by the Supervisor (the locked Top 5 does contain C-0090 and B-0212, both from the intervention side). Correction still needed at Final-3 selection: at most one pure-audit slot, and the cost-insensitive pick (C-0090) must not be traded away for a third cheap measurement paper.

## 3. Finding — asymmetric standards across clusters broke cross-cluster comparability

Two concrete asymmetries:

- **Anti-audit enforcement was applied to Cluster C only.** C's Reviewer #2 killed 6 pure audits under "instructed extra-harsh criteria" (C-0093, C-0276, C-0320, C-0332, M1, M5/C-0099 — kill file states "No pure audits survived"). B's Reviewer #2, same round, kept two pure-analysis papers and B's engineer ranked them #1 and #3. Under C's standard ("no causal lever, no decision that changes, result certain to be nonzero"), M5/B-0362 would have been at serious risk (its saving graces — the null-pair flip floor and ΔDSC calibration — were added at Stage 5, after survival). Conversely, under B's gentler standard, C-0128 (an instrument with a three-leg validation design) would plausibly have been nominee-grade. **Consequence: "Stage-4 survivor" does not mean the same thing across clusters, and B's audits reached the Top 5 partly because they never faced C's bar.**
- **The cost bar was inconsistent.** Cluster A's engineer dropped A-0107 as "the only survivor needing a substantial training program (~450 GPU-h)" while Cluster C's engineer nominated C-0028 at ~5,300 GPU-h in the same round. A 12× cost difference in opposite verdicts is not a defensible shared standard; A-0107 was effectively judged by a cluster-local budget, not a portfolio budget.

**Verdict:** the Top 5's audit share is partly an artifact of which cluster an idea happened to be filed under. This does not invalidate B-0121 (it survived a genuine attack round and its counterfactual design is input-interventional, not passive) — but it means the *second* audit slot (A-0061) carries no cross-cluster legitimacy and should not occupy a Final-3 slot. It also means A-0107's Stage-5 drop was procedurally unfair, though on the merits (LP-FT-adjacent novelty — the substantive weakness) the drop outcome is still correct for this cycle.

## 4. Finding — monoculture checks

- **Cluster A is a single-ecosystem monoculture:** 7 of 7 Stage-4 survivors and 3 of 3 nominees are SAM/SAM2-family diagnostics of frozen checkpoints. Nothing in A trains anything. Defensible as cluster scoping, but it means "Cluster A representation" and "inference-only SAM paper" are the same thing — the portfolio should take at most one.
- **Funnel-wide convergence on "diagnose frozen public models":** 6 of 8 Stage-5 nominations operate exclusively on public checkpoints without training. The two exceptions (C-0090, C-0028) are both Cluster C, both VLM-training studies sharing eval infrastructure — so the "diversity" between them is smaller than it looks; the portfolio should take exactly one.
- **Era risk:** the funnel audits yesterday's capability surface. A-0134's own kill note observes SAM3's presence head already ships the rejection signal that idea wanted to study; no surviving idea engages the promptable-concept/SAM3-era surface. Not fixable at Final-3 (nothing in the pool covers it) — logged as a missed direction (§8).

**Idea-level convergence within the Top 5 itself is acceptable:** no two Top-5 members share a killer experiment, model family, or dataset (dedup checks were run and documented by all three engineers; spot-verified here).

## 5. Finding — kill-list review: were high-risk/high-reward ideas wrongly killed?

I re-read all 33 Stage-4 kills. **The Stage-4 kills are sound.** Each names a specific structurally unanswerable attack (circularity, unconstructible control, signal-not-in-obtainable-data, direct prior-work hit). Borderline cases, with my ruling:

| ID | Kill basis | Ruling |
|---|---|---|
| C-0047/M3 (raster-order asymmetry) | Reviewer's own "closest call"; lever aging out (2D-RoPE cohort) | **Kill stands.** The payoff ceiling ("footnote for last year's architectures") is the reviewer's strongest point and it strengthens every month. Revival trigger already written into the kill — adequate. |
| B-0062 (smoke transmittance GT) | Field-transfer circularity | **Kill stands; rescope option noted** (lab-physics benchmark without the field claim). Not this cycle — heavy capture rig, no Final-3 relevance. |
| B-0058 (MoE routing as free pathology detector, PROTECTED) | Scale/confound dilemma | **Kill stands — this is the funnel's genuine high-risk/high-reward casualty, and the kill is still right**: no affordable experiment answers both horns, and the engineered MoE-AD wave must be beaten too. Log revival trigger: an open MoE medical/vision FM with exposed routing at deployment scale. |
| A-0178 (artifact tokens) | Stage-5 drop on a ~1 GPU-h existential gate | **Wrong to shelve the gate.** The nominee decision was right, but the 1 GPU-h fleet norm-audit should run unconditionally (Cluster A's engineer said the same). Funded as a rider (§10). |

**The real wrongly-shelved value is in Stage-5 cost drops, not Stage-4 kills:**

- **A-0271 (SA-1B filter fingerprints)** — Cluster A's own engineer calls it "strategically the biggest question (auto-labeling era)" with a clean same-image causal design, dropped purely on ~1,000 GPU-h. Its 25 GPU-h no-training MVE (label-arm signature deltas) is exactly the kind of option the portfolio should hold. Rider (§10).
- **B-0112+M4 Leg-1 MVE** — "the single highest-information cheap experiment among the drops" (B's engineer, ~3 A100-days), and the only path back to a METHOD-genre paper in the pipeline. Rider (§10).
- **C-0028** — nominated by C, left off the locked Top 5. Its zero-GPU offline dry-run gate (batch-constructibility: KS + noun-rate checks) should run now so that C-0028 is a live, de-risked replacement/next-cycle flagship. Rider + first-alternate designation (§10, and Final-3 file).

## 6. Finding — fake-novelty scan of Top 5 + alternates

Stage-3/4 prior-work searches in this funnel were unusually good (fresh-hit kills like B-0350/MedVeriSeg-Bench prove the searches were real). No outright fake novelty found. Residual novelty risk, ranked:

| ID | Novelty exposure | Risk |
|---|---|---|
| B-0121 | Phenomenon (support/foreground bias) documented since Lang et al. 2022 with a 2024 mitigation wave (TBS, AENet). Novelty = the counterfactual audit instrument + degeneracy/pathology stratification + support-free floor, verified unpublished. | **Moderate — thinnest margin in the Final-3 pool.** Mitigation: position as instrument + mandatory reported number; cite the mitigation wave as motivation, not competition. |
| A-0017 | SAM2-memory heuristics are a fast-moving wave (SAMURAI, DAM4SAM, SAM2Long). Novelty = *validated decomposition instrument* with predictive-validity bar, not another heuristic. | **Moderate scoop risk, low fake-novelty risk.** Mitigation: preregister + publish protocol early; the harvested-failure corpus and validity test survive even if new heuristics land. |
| M5 | Non-vacuity evidence (RECIST κ, reader-shift rates) is inherited from published studies; the flip-rate audit itself is new but synthesis-flavored. | Moderate. Desk-survey gate (≥15 auditable pairs) is the honest control — keep it. |
| C-0028 | The batch-curation lever is JEST-published; novelty rests wholly on the hardness-matched control + dense-metric accounting. | Moderate. The mandatory H-arm is correctly non-negotiable. |
| C-0090 | Robins-1995 pseudo-rehearsal + arXiv:2410.19925 adjacency; delta = content-free controls + convention-invariant gradient matching + capability stratification. Scoop check done this session. | Low-moderate. Being "15 fine-tunes from done" is the mitigation — start immediately. |
| B-0212, A-0061, A-0002, A-0178, C-0302, B-0230, A-0107 | Each carries a named adjacency (libcom/harmonization lit; Nyquist triviality; RFF analyses; Darcet registers; DFR; SENSE; LP-FT) already answered by design elements. | Low. (A-0107's LP-FT adjacency is the exception — the weakest novelty position among alternates, consistent with its drop.) |

## 7. Finding — reviewer echo chamber: where it is and is not

**Where the echo is real:** the *selection criterion*, uniformly inherited across Stages 2–5. All three clusters independently produced the identical output shape (2 nominees + cheap conditional third, ranked by per-dollar decisiveness) — that uniformity reflects shared instructions, not three independent judgments converging. Cheap audits won everywhere the criterion was applied symmetrically.

**Where it is not:** attack quality. Stage-4 reviewers killed protected ideas in two clusters (B-0058, B-0353 — protection explicitly overridden with stated justification), killed 4 of 10 Stage-3 KEEPs in C, and killed 7 of 8 mutations in C. Kill reasoning is specific and checkable. This funnel does not rubber-stamp.

**Net:** the echo chamber operated through the ROI objective, and the Supervisor's lock partially corrected it (C-0090, B-0212 included). The Final 3 completes the correction by construction (§9) rather than by re-running any stage.

## 8. Finding — missed research directions (for next window's Stage 1, not this Final 3)

1. **Data-centric science of auto-labeled corpora at scale** — A-0271's lane; the only surviving idea about the SA-1B-era labeling economy, dropped on cost. The field's center of gravity is here; the funnel's is not.
2. **Method development generally** — after B-0112+M4's drop, the pipeline produces zero new techniques. If two consecutive windows end methods-free, the Stage-1 generators (not the reviewers) need re-instruction, because Stage-4 novelty attacks are structurally harder on methods (methods have baselines; audits get "no published audit exists" for free — a novelty form this audit notes is *weaker*, since absence of a prior audit often reflects low perceived value).
3. **SAM3 / promptable-concept-era capability surface** — nothing in the pool touches presence heads, concept prompting, or the new rejection interface.
4. **Annotation economics with humans in the loop** — C-0158 demoted to rider; nothing else survives.
5. **Text-grounded / report-grounded supervision** — B-0331 dropped; the archive-scale free-supervision direction is unrepresented.

## 9. Corrections this audit applies to the Final-3 selection

1. **At most one pure-audit slot** (the Top 5 offers two: B-0121, A-0061). B-0121 takes it on merit (ROI 9, cheapest decisive experiment in the funnel, input-interventional counterfactual, every branch publishes). **A-0061 is removed from Final-3 contention** — second measurement paper, lowest ceiling in the Top 5 (its strongest outcome is negative design advice), and its cross-cluster legitimacy is weakest (§3). At 15–20 GPU-h it survives as a rider-grade side experiment, not a Research Package.
2. **The training-mechanism slot is non-negotiable** — C-0090 stays despite being the most expensive pick, precisely because the funnel's bias is against expensive training papers. Exactly one VLM-training study (not two): C-0028 becomes the de-risked first alternate, not a co-pick (§4 monoculture point).
3. **The mechanism/intervention revival clause is satisfied twice over**, and one revival is real, not nominal: **A-0017's intervention arm is elevated from secondary analysis to mandatory deliverable** — if targeted deletion beats full reset by the preregistered ≥10-pt margin, the paper must ship it as a training-free SAM2 memory-surgery wrapper benchmarked against SAMURAI/DAM4SAM, making A-0017 a causal tool *plus* a candidate tracker improvement, not a pure diagnostic.
4. **B-0212 is not abandoned** — it loses its Top-5 slot to portfolio arithmetic (one cluster-B slot, and B-0121 dominates it on cost-to-decision ratio 9× while covering the portfolio's eval-validity axis), but its 3-arm MVE (~6 A100-days, including the <0.5 A100-day probe sanity gate) is funded now, making it the immediately promotable second alternate.
5. **Option-value riders funded** (total <15 A100-days + ~$2K, all with written go/no-go gates): see §10.

## 10. Funded riders (not Research Packages; each has a pre-written gate)

| Rider | Cost | Gate / purpose |
|---|---|---|
| C-0028 offline dry-run | 0 GPU | KS<0.05 + noun-rate constructibility of the H-arm at s≥0.25 → first-alternate status confirmed |
| B-0212 MVE (3 compositing arms, 1 seed) | ~6 A100-days | Probe sanity AUROC>0.9 then 3-arm ordering → second-alternate status confirmed |
| M5 desk survey (~50 papers) | 0 GPU | ≥15 auditable public-checkpoint pairs → M5 promotable if an eval-validity slot ever opens |
| A-0178 fleet norm-audit | ~1 GPU-h | Artifact-token existence across SAM B/L/H, SAM2 Hiera, EfficientSAM, MobileSAM — audit table is publishable alone |
| A-0271 label-arm MVE | ~25 GPU-h | Filter-ablation signature deltas without training → preserves the auto-labeling-era option |
| B-0112+M4 Leg-1 MVE | ~3 A100-days | Direction-of-harm dissociation on BraTS nested labels → keeps the only METHOD lane alive |
| A-0061 cutoff-ratio table | ~15–20 GPU-h | Optional; run only if idle cycles exist — it was cut from Final-3 on genre, not validity |

---

*Final-3 recommendation with justifications, fallback ladder, and residual risks: `stage6_final3_recommendation.md`.*
