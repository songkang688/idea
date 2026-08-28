# Agent G Report — B∪C Merge + Feasibility Census

Role: merger + feasibility auditor. **Not PI; no final-3; batch A untouched; did not wait for Agent F.**
Inputs: `stage2_agent_D/*` (batch C review), `stage2_agent_E/*` (batch B review), `research_summary.md`, `selection_history/*`, stage-1 jsonl for idea text, live web search for artifacts.
Outputs (all under `Windows2/_wip/stage2_agent_G/`): `collisions.md`, `feasibility_census.md`, `provisional_200_partial.md`, this report.

**Headline numbers:** from 184 D/E keeps → **121 portfolio slots (LOCK 50 / FLEX 71) + 23 merged parasites + 40 drops**. 79 slots reserved for batch A. C's eval-audit share capped at 57.9% (D's ~60% policy). E's cheap mechanism bets (B-0114, 0001, 0074, 0104 + 0304/0323/0164/0169/0194/0227/0263) all LOCK. Census: **6 C analysis ideas downgraded by missing caches/artifacts** (3 dropped: 0253, 0254, 0271; 3 demoted to hosted arms: 0255, 0261, 0264); the rest of the "analysis-only" family repriced from "cached analysis" to "inference + analysis" with no slot change; the GT-epistemology bundle (0046/0338/0344/0311/0057/0326) **upgraded** because COCO-ReM and the LVIS double-annotation subset are confirmed public.

---

## 1. What would change after Agent F (batch A) reports

Batch A is 352 SAM / medical / ambiguous-object-segmentation ideas. Predictable pressure points, in order of expected impact:

1. **SAM-prompt mechanics.** A's point-jitter family (supervisor notes flag A-0001) lands directly on B-0169 (negative clicks) and B-0194 (sycophancy). Precedent: E already killed B-0175 via RClicks (NeurIPS'24) — the same literature will be F's murder weapon. If A has a stronger or broader prompt-perturbation instrument, B-0169/0194 drop from LOCK claims to arms of a merged prompt-robustness program. I kept them LOCK because they are dose-response/causal designs RClicks did not run, but this is the LOCK assignment most likely to be revised.
2. **Contamination/benchmark-integrity.** A-0017/0206/0301 (SA-1B prior + contamination, per supervisor merge notes) will collide with the B-0268 / C-0122 / C-0298 / C-0345 cluster. The cluster has 4 slots + B-0338; after F it should still have at most 5 — any A survivor here must displace, not add.
3. **Annotation-noise / GT epistemology.** A-0151/0198 (seed-churn, boundary rasterization) meet C-0046/0136/0311 and the COCO-ReM-based family. Expect merges where A's ideas are segmentation-side instantiations of the same uncertainty budget — C-0311 is the natural host and was built as an umbrella.
4. **Frozen-vs-tuned / UDA.** A-0245 (UDA rank-correlation across novel shifts) meets C-0150(+0221) and B-0226. If A's version is broader, C-0150's arm structure absorbs it or the FLEX slot flips to A.
5. **Medical rebalance.** This portfolio carries only 6 medical slots (B-0282/0284/0286/0293/0303, C-0043). Batch A is the medical batch; several of the 79 reserved slots should fill there — and B-0293's compute-conditional FLEX status should be resolved by whether A brings a cheaper instrument for the same attribution question.
6. **SAM-failure prediction.** D mutated C-0082 into a failure-prediction law and it is *not* in this portfolio (mutation, not keep). If A carries a SAM-failure atlas idea, the mutated C-0082 law is the right merge target and could re-enter through A's slot, not C's.
7. **Cross-batch calibration.** E flagged that protected-class quotas were set batch-internally. If F's scores run systematically higher/lower, the LOCK/FLEX boundary (not membership of the 121) is what should move first.

## 2. Correlated-bet clusters (portfolio risk map)

One adverse event damages all members; the PI should not read the 121 as 121 independent bets. Effective independent bets ≈ 90.

| Cluster | Members (slots) | Shared failure mode |
|---|---|---|
| Cached-prediction infrastructure | C-0309, 0302, 0136-census arm, 0326, 0276, 0256, 0119 (7) | Zoo checkpoints unusable at scale / eval-protocol drift. Census verified the zoos, so residual risk is engineering, not existence. |
| Benchmark integrity | B-0268, B-0338, C-0122, C-0298, C-0345 (5) | Reviewer fatigue with "your benchmark is contaminated"; detector-calibration validity (B-0268's known weak point). |
| GT epistemology | C-0046, 0338, 0344, 0007, 0259, 0326 (6) + B-0227 | One strong "annotation noise bounds progress" paper (e.g., Label Convergence follow-up) scoops the framing; mitigation: the instruments differ (instructions, size floor, salience, deletion law). |
| Training-rigor compute family | C-0283, 0285, 0287, 0327 (4) | All need training-grid compute; a budget cut kills four at once (already trimmed from 7 by dropping 0292/0299/0330). |
| Supervision-statistics imprint | B-0026, 0323, 0326, 0243, C-0279, C-0269 (6) | If corpus-frequency→competence correlations prove confound-dominated, the family weakens together; causal arms (B-0323 retraining, C-0020 invented names) are the insurance. |
| PEFT mechanics | B-0098, 0101, 0104 (3) | A strong vision replication of intruder dimensions reshapes all three (E's own flag). |
| Registers/token mechanics | B-0001, B-0114 (2) | A single "register norms are meaningless downstream" result hits both. |
| Frozen-vs-tuned under shift | B-0226, 0234, 0241, C-0150, 0193 (5) | If crossover curves prove shift-family-idiosyncratic, the "budget" framing collapses to case studies. |
| Free-uncertainty signals | B-0001, C-0190, C-0119 (3) | Deployment reviewers may demand the same baselines (softmax entropy/ensembles) beat all three. |
| Psychophysics transplants | C-0308, B-0023, B-0304 (3) | Genre rejection ("cute import, not CV science"). |
| Seed/variance metrology | C-0136, 0302, 0311, 0290, 0287 (5) | Shared delta-census + variance-component infrastructure; also venue concentration (D&B/analysis tracks). |

## 3. Remaining novelty risks (ranked)

1. **Fresh hit found this session:** *Label Convergence* (arXiv 2409.09412) — already computes an annotation-consistency performance bound on the LVIS doubly-annotated subset with bootstrap CIs. Forced C-0071→arm-of-0338; is mandatory first-paragraph related work for C-0338, C-0046, C-0311. A deeper read of its appendix ("COCO Reannotated", 80k images × 5 raters, reported as having issues) is required before executing the GT-epistemology bundle — if that artifact is usable, several designs get cheaper; if its "issues" are fatal, nothing changes.
2. **Udandarao et al. transfer:** E's kill of B-0037 (concept frequency predicts zero-shot performance) was never applied to batch C. C-0279(+0001/0020) now carries mandatory positioning; the detection instantiation with visual-difficulty covariates is the surviving claim.
3. **Fast-decay survivors (re-attack immediately before proposal writing):** B-0332 (visual CoT intervention — E's highest scoop risk), C-0306 (conformal-OD field moving, 2 papers/yr), C-0011+B-0042 (prompt/name sensitivity, 2026 activity), B-0268/C-0345 (contamination gold rush), C-0226 (SR hallucination).
4. **Unverified-by-search verdicts:** E attacked 26/77 keeps, D attacked 19/107 with live search; the other ~120 keeps in this portfolio rest on D/E's priors. My census re-verified artifacts, not novelty. A stage-3 sweep should prioritize LOCK ideas that were never live-attacked: C-0260, C-0259, C-0135, C-0341, C-0043, B-0304 got partial coverage, but e.g. C-0122, C-0193, C-0308, B-0164, B-0286 have never faced a dedicated search.
5. **Bundle-size risk:** the merged hosts (C-0302 with 3 arms, C-0311 with 3, C-0279 with 2, C-0226 with 2, C-0338 with 1) are now review-scope risks in the other direction — "too many claims per paper." Fission points are documented; this is a writing-stage decision, not a slot decision.

## 4. Deviations, biases, and epistemic status

- **I merged more aggressively on the C side (18 parasites) than the B side (5).** Justification: D's own bundling notes proposed most of these merges, and the ~60% eval-audit cap is better met by consolidating redundant audits than by killing protected ideas. Consequence: C's slot count (57) understates C's content (75 idea-units live inside it).
- **Protected-idea overrides (require PI sign-off to become final):** dropped despite D protection — C-0251, C-0334, C-0253, C-0271 (protection class preserved via siblings: 0135/0013 keep the counter-intuitive class; 0285/0287 keep the adversarial-retuning class). Demoted despite protection: C-0255, C-0261, C-0264 (census-driven, reversible). No E-protected idea was dropped; B-0033's DP protection survives as a named arm of C-0136.
- **Census scope honesty:** I verified existence, not completeness — e.g., I confirmed MMDetection ships Seesaw/RFS LVIS models but did not enumerate how many *distinct long-tail methods* have usable public checkpoints; that one-day enumeration is the single highest-value follow-up before committing C-0276/0256 to LOCK-final.
- **Numbers not re-scored:** I did not re-score any idea on D/E's 14 dimensions; LOCK/FLEX placement uses their verdicts + census evidence + cluster accounting only.
- All writes confined to `Windows2/_wip/stage2_agent_G/`. No batch A files read. No final-3 selected.
