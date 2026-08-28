# Stage 6 — Final-3 Recommendation

**Meta-Reviewer / Auditor / Deputy Supervisor (Cloud Sub-Agent R) → Supervisor Windows7.**
Basis: full-funnel bias audit in `stage6_audit.md`. Selection universe: Supervisor-locked Top 5 (A-0017, B-0121, A-0061, B-0212, C-0090) + alternates (A-0002, M5, C-0028, A-0178, C-0302, B-0230, A-0107).

## THE FINAL 3

| # | ID | Title | Genre | Cluster | Core cost | Pre-registered kill rule |
|---|----|-------|-------|---------|-----------|--------------------------|
| 1 | **B-0121** | Wrong-support counterfactual audit of few-shot segmentation | Evaluation-validity audit (input-interventional) | B | ~5 A100-days, zero training | ≥50% IoU retention for ≥half of specialist methods on distractor-present strata AND indistinguishable from support-free objectness floor; both legs failing publishes the certification negative |
| 2 | **A-0017** | Causal memory surgery for SAM2 — validated decomposition **+ mandatory training-free tracker arm** | Causal mechanism tool with method upside | A | ~80–120 GPU-h, zero training | Targeted deletion ≥30 pts over no-op AND ≥10 pts over full reset; per-sequence reversible fraction predicts SAMURAI *and* DAM4SAM gains at r>0.6, else the instrument is reported dead |
| 3 | **C-0090** | Text-batch rehearsal works by gradient rebalancing, not content | Training-mechanism causal test → training recipe | C | ~2,450 A100-h | Balance-effect ≥80% of curated effect on ≥3/4 language capabilities under BOTH gradient-matching conventions = mechanism; Ret(A2)≈Ret(A0) everywhere = refuted; divergence across conventions is itself the finding |

Total core budget ≈ **3,050 A100-h** (+ ~15 A100-days of riders per the audit) — inside a single 8×A100 node for the cycle. One idea per cluster, which also decorrelates the three independent Stage-2→5 reviewer lineages (no single reviewer chain's blind spot touches more than one pick).

---

## Justifications (one paragraph each)

**B-0121 — Wrong-support counterfactual FSS audit.** The funnel's consensus best buy (ROI 9, the only unanimous #1 in any cluster) and the portfolio's single audit slot, taken on merit: it is the cheapest decisive experiment in the entire pool (~5 A100-days, zero training, all seven method checkpoints public and verified this session), every outcome branch publishes (leaderboard reorder, validity certification, or benchmark-degeneracy indictment — each against a pre-registered support-free objectness floor), and its "audit" is actually an input-space intervention (counterfactual wrong-class supports, stratified by query complexity), which is why it survived a genuine Reviewer-#2 round rather than a lenient one. Startable next week: Day 1–2 support-injection wrappers for PFENet/BAM/Matcher, Day 3 MVE on PASCAL-5i/COCO-20i fold 0, go/no-go before week 2. Its one soft spot — thin novelty margin over the documented foreground-bias literature — is handled by positioning the instrument and the sensitivity-adjusted leaderboard as the contribution, with the 2024 mitigation wave cited as motivation.

**A-0017 — SAM2 causal memory surgery, with the intervention arm made mandatory (this is the revival).** Picked over its Top-5 clustermate A-0061 and over B-0212 because it is the only Top-5 idea that can graduate from measurement to method inside one budget: the audit elevates the previously-secondary arm to a required deliverable — if targeted post-error memory deletion beats full reset by the preregistered ≥10-pt margin, the paper must ship it as a training-free SAM2 wrapper benchmarked head-to-head against SAMURAI and DAM4SAM, converting the "upper-bound diagnostic" into a candidate tracker improvement. The design is falsifiable twice over (the margin test kills the "it's just a reset heuristic" attack; the r>0.6 predictive-validity bar kills the instrument honestly if it measures nothing prevention methods exploit), costs ~100 GPU-h with zero training on the hottest model family in the pool, and is startable next week (failure harvesting on public LVOS v2 + DiDi via the written protocol; all comparators are public SAM2.1 wrappers). Residual scoop risk in the fast-moving SAM2-memory subfield is priced in: preregister and post the protocol early — the harvested-failure corpus and validity methodology survive even if another memory heuristic lands first.

**C-0090 — rehearsal-content mechanism test.** The portfolio's deliberate expensive pick and the direct counterweight to the funnel's documented cheapness bias: it is the only Top-5 idea whose every outcome branch changes how people *train* (mechanism confirmed → rehearsal-curation budgets across the field are wasted, a gradient-balance term suffices; mushy middle → the first per-capability rehearsal dosing recipe with a minimal-real-text fraction sweep; refuted → the first controlled multimodal refutation of the 30-year-old pseudo-rehearsal account). The design is fully specified and startable next week on the published LLaVA-1.5 recipe (15 fine-tunes, 3 seeds × 5 arms including the shuffled-token and single-document controls that make any outcome interpretable), has a convention-invariance requirement that defuses the gradient-matching dispute by construction, was scoop-checked this session (arXiv:2410.19925 is scaffold, not scoop — no content-free controls), and carries an honest abort gate (seed-variance power check at 6 runs, kill at <1K A100-h spent). Chosen over C-0028 as the single training slot: 2.2× cheaper, zero feasibility gates left, and its own cluster ranked it #1 on ROI.

---

## What was revived, what was dropped, and the fallback ladder

**Revived (per the audit's mandatory clause — the Top 5 was measurement-tilted):**
- **A-0017's method arm** — elevated from optional secondary analysis to mandatory deliverable (training-free memory-surgery wrapper vs SAMURAI/DAM4SAM). This is a real scope change, not relabeling: the Research Package must budget the head-to-head comparison runs.
- **C-0028** — revived to *funded first alternate*: its zero-GPU offline dry-run gate (H-arm constructibility: KS<0.05 similarity matching + noun-rate checks on 10K generated batches) runs immediately, so a fully de-risked training-recipe flagship is on the shelf if C-0090 dies at its power gate — or for next cycle. Not co-picked with C-0090: two VLM-training studies sharing eval infrastructure would recreate monoculture in the opposite direction.

**Dropped from the locked Top 5, with compensation:**
- **A-0061** (Boundary Nyquist) — second pure-measurement paper; lowest ceiling in the Top 5 (its strongest outcome is negative design advice); weakest cross-cluster legitimacy per the asymmetric-standards finding. Kept as an idle-cycle rider (~15–20 GPU-h) — cut on genre and ceiling, not validity.
- **B-0212** (blending-artifact transfer-gap law) — loses the slot on portfolio arithmetic, not merit: one Cluster-B slot existed, and B-0121 dominates it 9× on cost-to-decision ratio while covering the eval-validity axis. Compensation: **B-0212's 3-arm MVE (~6 A100-days, including the probe sanity gate) is funded now**, making it the immediately promotable second alternate and preserving the intervention-law lane.

**Fallback ladder (pre-committed, no re-litigation needed):**
1. If **C-0090** dies at its power gate → promote **C-0028** (offline gate already passed by then; decision triple alone, 9 runs ≈ 3,600 A100-h, settles it).
2. If **B-0121** proves infeasible (benchmark degeneracy so total that even the certification branch is vacuous) → promote **M5** if its $0 desk survey found ≥15 auditable pairs; else promote **B-0212** off its passed MVE.
3. If **A-0017** is scooped before the margin test runs → promote **B-0212** off its passed MVE; **A-0002** (same cluster, ~30 GPU-h killer battery, cleanest causal design in A) is the cheap stopgap if B-0212's MVE failed.

---

## Residual risks (owned, not hidden)

1. **A-0017 scoop risk** — the SAM2-memory subfield moves quarterly. Mitigation: preregistration + early protocol release; the decomposition instrument and failure corpus remain novel contributions regardless. This is the portfolio's highest single risk.
2. **B-0121 novelty perception** — a reviewer can say "foreground bias is known." Mitigation is positioning (instrument + mandatory reported number + sensitivity-adjusted leaderboard); the certification branch is the hedge. Accepted because the cost of finding out is 5 A100-days.
3. **C-0090 mushy-middle outcome** — the most likely single result is the stratified middle, which is the weakest of its three branches (a dosing recipe, not a headline kill). Accepted: the branch is still a training-practice change, and the abort gate caps the downside at <1K A100-h.
4. **No METHOD-genre paper in the Final 3** — the funnel offered none at nominee grade (extinction documented in the audit §1, §8). Interim exposure is A-0017's mandatory method arm; the B-0112+M4 Leg-1 rider keeps the lane alive; Stage-1 generator re-instruction recommended for the next window so this is not a three-peat.
5. **Frozen-checkpoint dependency** — B-0121 and A-0017 both audit public checkpoints; availability was verified this session, but a pulled checkpoint or license change would force substitutions (low probability, low impact — panels are 7 and 3+ methods deep respectively).
6. **Process debt flagged upstream** — the asymmetric anti-audit enforcement (Cluster C harsh, Cluster B lenient) and the 12× cross-cluster cost-bar inconsistency (A-0107 dropped at 450 GPU-h while C-0028 was nominated at 5,300) are uncorrected at their source; both Final-3-relevant consequences were neutralized here, but the next window should issue uniform Stage-4/5 criteria.

---

## Portfolio diversity check (the constraint that drove the audit)

- **Genres:** 1 evaluation-validity audit · 1 causal-mechanism tool with a mandatory method arm · 1 training-mechanism/recipe test. Not three measurement papers.
- **Domains/model families:** few-shot segmentation benchmarks (natural images) · SAM2 video tracking · multimodal LLM fine-tuning. No shared datasets, checkpoints, or killer-experiment infrastructure (spot-verified against all three engineers' dedup tables).
- **Risk correlation:** primary risks are scooping (A-0017), benchmark degeneracy (B-0121), and seed-variance power (C-0090) — mutually independent.
- **Budget shape:** two cheap-decisive (≈10 A100-days combined) + one deliberate expensive training program — the cheapness bias is exploited where it is a feature and overridden where it was a bug.

**Branch:** `cursor/stage6-meta-review-final3-4fc5` (contains `stage6_audit.md` + this file).
