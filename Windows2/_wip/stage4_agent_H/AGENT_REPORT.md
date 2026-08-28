# Agent H Report — Stage-4 Reviewer-2 Attack + Freshness Assassination (Batch B survivors)

**Role:** Reviewer #2 and freshness assassin for batch-B survivors only. Not the PI; no final-3
selected. Agents F/G not waited on; D/E score files untouched; `stage2_agent_G/` untouched
(does not exist at time of writing).

**Deliverables (all under `Windows2/_wip/stage4_agent_H/`):**

| File | Contents |
|---|---|
| `reviewer2_attacks.md` | 29 full attacks: harshest rejection, hidden assumptions, killer experiment, verdict, mutation, fresh prior-work URLs |
| `verdicts.jsonl` | one machine-readable verdict record per attacked idea (29 lines) |
| `AGENT_REPORT.md` | this file |

**Coverage:** all 20 of Agent E's "PhD-year bets" (0114, 0001, 0304, 0074, 0323, 0104, 0307,
0332, 0268, 0213, 0226, 0101, 0145, 0194, 0169, 0164, 0227, 0263, 0286, 0042) plus 9 fragile
protected keeps (0025, 0033, 0092, 0133, 0252, 0264, 0278, 0305, 0317) = 29 ideas, exceeding the
20-idea minimum. Mandatory freshness re-search executed on all five flagged IDs and extended to
13 more; ~16 live web searches over 2024–2026 arXiv/venues; every cited URL was returned by live
search this session or inherited from E's verified list; memory-only citations are flagged
[not re-verified] in the attacks file.

## Headline numbers

| Verdict | Count | IDs |
|---|---|---|
| SURVIVE | 0 | — |
| SURVIVE-IF-EXPERIMENT | 14 | 0001, 0092, 0101, 0104, 0114, 0145, 0169, 0194, 0213, 0226, 0227, 0263, 0268, 0317 |
| MUTATE | 9 | 0074, 0164, 0264, 0278, 0286, 0304, 0305, 0307, 0323 |
| KILL | 6 | 0025, 0033, 0042, 0133, 0252, 0332 |

No unconditional SURVIVE was granted: under Reviewer-2 posture, every idea's survival is
conditional on a named control/experiment that its Stage-1 form lacked. Those named experiments
are the operational output of this stage.

## 1. Ideas that died at this stage (6 kills)

**Freshness kills — the literature got there first (3):**

1. **W2-B-0332** (visual CoT post-hoc theater). E's own tripwire fired: *On the Faithfulness of
   Visual Thinking* (arXiv 2510.23482) corrupts the visual thoughts, finds predictions nearly
   unchanged under visual intervention, and ships a training fix; Evidence-RL (2608.08021) and the
   2024–2026 counterfactual-visual-intervention line take the rest. E ranked this bet #8 and said
   "execute early"; it is now unexecutable. **This is the single largest casualty of this round.**
2. **W2-B-0133** (LoRA memorizes more per-parameter). The 2025–2026 privacy literature answers in
   the opposite direction at scale (55× lower MIA success for LoRA, arXiv 2601.12104; up to 10×
   less memorization, 2502.05087; memorization *rises* with rank, 2507.21009). The per-parameter
   normalization is metric engineering; no mechanism for a sign flip in vision. E's CI protection
   was explicitly conditional on a pre-execution re-check; the re-check failed.
3. **W2-B-0042** (synonym-variance ledger). RENOVATE (NeurIPS 2024) documented and fixed name
   imprecision, open metrics (2311.03352) reformed scoring, and SynCLIP (CVPR 2026) both
   quantifies synonym-substitution sensitivity and trains it away. Micro-literature complete.
   Residual (name choice as a protocol axis) folded into 0213.

**Methodological kills — no affordable experiment silences the reviewer (3):**

4. **W2-B-0025** (attention maps epiphenomenal). Construct failure: attention weights ARE the
   computation, so "destroy alignment, preserve statistics" has no coherent null family; every
   outcome has a prepared deflationary reading (off-manifold vs too-weak). The community would
   split over the method, not the finding — that is not the productive kind of DP.
5. **W2-B-0033** (seed variance vs published gaps). The affordable experiment (ViT-S scale) cannot
   license the flagship-scale indictment; variance does not extrapolate across 3 orders of
   magnitude, and the decisive multi-seed flagship run has no funder. By E's own compute-partner
   criterion (applied to 0293), this converts to a kill.
6. **W2-B-0252** (interpolation kinks). Published interpolation paths in exactly this regime are
   smooth (Neyshabur et al. 2020; five years of WiSE-FT plots); thresholded metrics manufacture
   kinks; and even seed-stable kinks would not license "discrete mechanism transitions." The HRHR
   prize is unclaimable even on a win.

**Freshness-forced mutations (headline dead, narrower claim survives):** 0074 (MG-CLIP/GNSP
publish gap-dynamics-as-indicator), 0304 (categorical perception along morphs is 2021 prior;
supervised-classifier control now mandatory), 0307 (matched CLIP-vs-DINO pretraining exists,
arXiv 2510.11835), 0323 (caption gap measured in 2406.09067; causal caption intervention in
2404.07983), 0164 (relearning-as-probe is ICML 2026's framework), 0264 (transitive MIA via
synthetic training data run on clinical notes, Sci. Reports 2024), 0286 (site-decodability audit
exists for pathology, 2501.18055), 0305 (COMFORT banks the behavioral Whorfian result).

## 2. The 8 most paper-shaped survivors

"Paper-shaped" = post-attack claim is sharp, the killer experiment is affordable and decisive,
and the field has a visible slot for the result. Ordered by my conviction:

1. **W2-B-0114 (VPT as registers, 4-arm form).** Still the best risk-adjusted bet in the batch,
   but only in the upgraded design: VPT vs frozen-random tokens vs attention-bias-only vs no-token,
   on register-free AND register-equipped backbones, DA-VPT cited up front. Every cell of the
   outcome table is publishable; the attention-bias arm converts analogy into mechanism.
2. **W2-B-0194 (segmentation sycophancy, randomized-dose form).** One week of compute; the
   randomized prompt-dose protocol cleanly kills the selection-bias objection that sinks the
   observational version. Safety-adjacent, catchy, and the SAM-UQ literature (UncertainSAM, RUAC)
   provides the citation slot without owning the dose-response law.
3. **W2-B-0001 (artifact map: uncertainty channel or saliency prior?).** Honest stratified audit
   against cheap baselines across register regimes. The reframing survives its own negative
   outcome (a deflationary note), and no one has run the specific measurement.
4. **W2-B-0104 (invariance-dissociation grid).** The only member of the PEFT-mechanics family
   whose killer experiment separates mechanism from tautology; must include the high-rank arm.
5. **W2-B-0268 (contamination audit with placebo/injection calibration).** The urgency is real and
   nobody has done the generated-image (as opposed to duplicate-leakage) version; the calibration
   arms are the difference between science and a scare.
6. **W2-B-0213+0200 (robust-inversion protocol audit).** Survives as the all-matchings version:
   published conclusions that invert under every defensible resolution/probe convention. Expect
   fights; that is the DP value.
7. **W2-B-0304 (mutated: supervision taxonomy predicts quantization boundaries).** The three-way
   model contrast with naming-boundary alignment is still an unoccupied psychophysics-grade
   paradigm — smaller than the original pitch, but clean and genuinely new.
8. **W2-B-0169 (negative-click dose-response across the policy envelope).** Cheap, decisive
   either way if run across click policies including RClicks' human-derived model; pairs naturally
   with 0194 as one interactive-behavior paper program.

Just below the line: 0145 (lives or dies on the temperature arm), 0307-mutated (strong but now
staged behind a cheap probe of existing matched checkpoints), 0226 (honest expected outcome is
the negative branch), 0317 (needs the theory collaborator before it is anyone's Year-1 bet).

## 3. Correlated-failure clusters

Where one adverse event takes out multiple survivors at once — the PI should not stack bets
within a cluster.

1. **The "dynamics/causal upgrade" cluster (0074, 0145, 0163-legacy, 0307, 0323) — already
   failing together.** E flagged this monoculture in the Stage-2 bias audit; this round confirmed
   it empirically: 3 of the 5 took direct freshness hits (0074 via MG-CLIP/GNSP, 0307 via
   2510.11835, 0323 via 2406.09067 + 2404.07983). The upgrade heuristic ("statics published →
   measure the trajectory / run the controlled version") has a ~12-month shelf life because it is
   the same heuristic everyone else's reviewers are teaching them. Any surviving member should be
   executed first or dropped.
2. **PEFT-mechanics family (0092, 0101, 0104, 0114).** Shared exposure: one strong vision-side
   replication of intruder dimensions, or a mechanistic VPT paper, re-prices all four. Also shared
   hidden assumption: dense-task PEFT deficits are structural rather than hyperparameter/rank
   artifacts — a single "high rank + tuned LR closes the dense gap" result guts 0101 and 0104
   simultaneously. Recommend at most two from this family, one mechanism (0114) + one
   deployment-empirical.
3. **Eval-integrity / measurement-reform cluster (0042-dead, 0213, 0226, 0268, 0033-dead).**
   Fastest-aging cluster in the batch: RClicks, RENOVATE, SynCLIP, Kerssies, and the ICCVW-2025
   leakage audit show NeurIPS-D&B-style teams industrialize exactly these papers. Survivors here
   (0213, 0268) must be executed on a two-quarter clock or not at all. Shared failure mode:
   "the correction is itself a convention" — mitigated only by the multi-convention/placebo
   designs specified in the attacks.
4. **Calibration/uncertainty cluster (0001, 0145, 0194).** Shared dependency: cheap baselines
   (entropy, temperature, randomized dose) must lose for the headline to stand; a single strong
   "trivial baselines suffice for dense uncertainty" paper deflates all three. Also all
   week-scale-cheap, hence high scoop hazard — same property that just killed 0332/0133/0042.
5. **Language-imprint geometry family (0304, 0305, 0307, 0317, 0323).** Shared hidden assumption:
   supervision-modality effects are attributable to *language* rather than to data distribution
   or supervision density. The matched-pretraining tooling that now exists (2510.11835) both
   enables and threatens the whole family: one strong "it's the data, not the language" result at
   matched pretraining damages all five framings at once. The supervised-classifier control
   (0304) and dose-response designs (0307, 0323) are the family's only insurance.
6. **Interactive-behavior pair (0169, 0194).** Both live inside RClicks' hostage situation: if
   click/prompt-policy variance dominates the effects, both curves are artifacts. Cheap to hedge:
   run both under the shared randomized-dose + policy-envelope protocol as one program.

## 4. Notes for the PI

- E's top tier is now materially re-priced: of E's twelve top-tier items, 0332 is dead, 0074/0323/
  0307/0304 are mutated (each lost its headline to 2025–2026 literature), and 0001/0104/0114/0213/
  0226/0101/0268 survive only with named controls. The batch's center of gravity has shifted from
  "discovery claims" to "quantification-with-controls claims"; that should inform venue targeting.
- Freshness half-life observed in this round: ideas whose killer experiment costs under ~2 GPU-weeks
  had roughly a 1-in-3 chance of having been executed by someone else within ~12 months of E's
  review. Cheap-to-falsify protection should be paired with immediate execution, not portfolio
  storage.
- I did not re-verify Agent E's scores or rewrite any Stage-2 files; all E-verdict references above
  are read-only citations.

## 5. Compliance

- All writes confined to `Windows2/_wip/stage4_agent_H/`.
- Did not wait on Agents F or G; `stage2_agent_G/` untouched (absent).
- No final-3 selection; verdicts are inputs to the PI.
- No invented citations: every URL was returned by live web search during this review or inherited
  from Agent E's verified list; memory-only citations flagged [not re-verified].
