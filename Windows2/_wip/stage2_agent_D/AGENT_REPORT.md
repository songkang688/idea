# Agent D Report — Independent Review + Novelty Attack on Batch C

Role: Reviewer + Novelty Assassin (not PI; no final-3 picked).
Inputs: `Windows2/_wip/stage1_agent_C/ideas.jsonl` (345 ideas), Agent C's report/clusters, `Windows2/research_summary.md`.
Outputs: `scores.jsonl` (345 scored), `shortlist.md` (Tier A 79 + Tier B 28), `kills.md` (180), `prior_work_attack.md` (15 mandatory + 4 extra attacks, all citations web-verified).

Headline numbers: **keep 107 (Tier A 79 / Tier B 28) · mutate 58 · kill 180.** Mandatory-15 prior-work verdicts: **SURVIVE 7 / MUTATE 8 / KILL 0.**

---

## 1. Twenty ideas I would bet a PhD year on (from batch C)

Ordered roughly by (decision value × survival probability), not by score average. Bundle references per `shortlist.md`.

1. **W2-C-0302 (+0070)** — Minimum-detectable-effect power tables for popular benchmarks, cross-referenced against 100 papers' claimed deltas. Pure re-analysis; permanent infrastructure; indictment built in.
2. **W2-C-0309 (+0328)** — IRT for detection benchmarks: ability scores, misfit-item audit (cross-checked against COCO-ReM errors), 1k-image short test. Analysis-only, certain informative outcome.
3. **W2-C-0136** — Seed variance vs the distribution of published detection deltas. The missing constant of the field; survives prior-work attack (precedents are classification-only).
4. **W2-C-0311** — Metrology-grade combined uncertainty budget for COCO AP. Umbrella paper composing annotation noise, bootstrap, framework variance, nondeterminism.
5. **W2-C-0344** — Instruction A/B experiment: labeling-protocol effects exceed inter-annotator noise. 300-image budget, foundational reframing of "annotation quality."
6. **W2-C-0338** — The small-object ceiling is human: locate the size floor beneath which progress claims are unfalsifiable. Cheap, epistemically fundamental.
7. **W2-C-0260** — Benchmark monoculture: stratified cross-dataset rank correlation of 15 modern detectors on 10 datasets. The reusable audit artifact of the batch.
8. **W2-C-0276** — Tail-progress illusion: per-class delta distributions of long-tail methods; is AP-rare progress a few easy classes? Days of re-analysis, narrative-changing.
9. **W2-C-0256** — Size-frequency confound in long-tail gains. Same cached predictions, orthogonal decisive cut.
10. **W2-C-0306** — Conformal coverage destroyed by NMS + coverage-preserving suppression. Formal novelty verified (existing conformal-OD papers bracket NMS out). Urgent: field moving.
11. **W2-C-0057** — Missing annotations punish better detectors: controlled-deletion law of leaderboard distortion. COCO-ReM de-risks the premise.
12. **W2-C-0011** — Prompt-template variance vs architecture deltas on OVD leaderboards. Inference-only; urgent (2026 arXiv activity nearby).
13. **W2-C-0326** — Powered adjudication of a SOTA model's residual COCO errors (share that is GT problems, not model failure). TIDE showed the phenomenon in 2020; the citable number is unclaimed.
14. **W2-C-0327** — 2015 architecture + 2026 recipe: attribute a decade of detection progress. ResNet-strikes-back precedent makes a big effect likely; either outcome is a field-level number.
15. **W2-C-0283** — Stale-baselines audit under papers' own tuning budgets. Genre proven in metric learning/recsys; detection open.
16. **W2-C-0285** — Shadow tuning: give the baseline the method's search budget. Sharpest of the rigor family; pre-registration mandatory.
17. **W2-C-0226 (mutated, hosts 0248/0230/0227)** — GT-controlled accounting of SR for detection: recovered information vs hallucination. The SR-helps literature never had HR ground truth in the loop.
18. **W2-C-0150** — Detection UDA vs 50 labeled target images. Cheap kill-shot with budget consequences for a large subfield.
19. **W2-C-0287** — Ablation sign-flip rates under reseeding. Bounded compute, wholesale consequence for component-level claims.
20. **W2-C-0259** — Dense "label everything nameable" re-annotation: salience bias and the false-positive population. 200 images, foundational.

## 2. Ten ideas I almost killed, then revived — and why

1. **W2-C-0326** — TIDE (ECCV 2020) already showed most-confident errors are often misannotations; nearly killed as done. Revived: no powered, stratified, two-annotator share estimate for a modern SOTA model exists; the quotable number is still up for grabs.
2. **W2-C-0032** — LVIS's own paper plus Dave et al. 2021 document AP-rare instability; nearly killed as textbook-known. Revived as mutation: the significance audit of *published claims* against bootstrap MDEs converts known instability into a literature verdict.
3. **W2-C-0081** — Battle of the Backbones (NeurIPS 2023) runs almost exactly this rank-correlation and finds ρ>0.8; killed on first pass. Revived as mutation: BoB is cross-family; the within-family compute-matched version is the causal question BoB can't answer.
4. **W2-C-0082** — SAM failure catalogues are abundant (concealed scenes, SAM-2 CD-concept evaluation); nearly killed. Revived as mutation: a validated *failure-prediction law* from computable image properties is a different and open contribution.
5. **W2-C-0116** — The Elephant in the Room owns context-induced detection weirdness; nearly killed as derivative. Revived: object *removal* with ghost-rate measurement is the inverse experiment nobody ran; artifact controls make or break it.
6. **W2-C-0298** — Most likely outcome (all benchmark copies identical) is boring; nearly killed on expected value. Revived under cheap-to-falsify protection: hours of hashing, scandal-grade tail if circulating COCO/VOC variants differ.
7. **W2-C-0331** — Hoiem-style diagnostics and TIDE already decompose localization vs classification error; nearly killed as re-run. Revived to mutate: as the framing device of a modern decomposition refresh (DETR/open-vocab era), it still earns its slot.
8. **W2-C-0334** — DETR-line papers report NMS ablations, so "NMS-free wins are tuning artifacts" looked pre-refuted. Revived: their ablations tune the proposed model, not the classical baseline's post-processing; the adversarial-tuning audit is intact and disagreement-prone in a productive way.
9. **W2-C-0303** — Disclosed search budgets are unreliable and pair-matching is confounded; nearly killed on soundness. Revived under high-risk high-reward protection: inference-only cost, and even a noisy tuning-tax correlation would matter.
10. **W2-C-0265** — Demographic annotation on dense-crowd imagery nearly killed it on ethics/feasibility. Revived as mutation using datasets with existing demographic metadata or proxy strata; the density×subgroup interaction hypothesis is genuinely novel.

## 3. Bias audit — is this batch too "meta"/eval-science vs method papers?

**Yes, materially.** My keep-set makes the skew explicit rather than hiding it:

- **Composition (EVIDENCE from my own verdicts):** of 107 keeps, roughly 70% are evaluation science, re-analysis, audits, or reproducibility studies; under 10% propose anything a reviewer would call a method. The mutate list leans the same way. Batch C's mandate (cheap, decisive, falsifiable) structurally favors audits — measuring is cheaper than building, and "X is broken" is easier to state crisply than "Y fixes it."
- **Portfolio risks this creates:** (a) *venue concentration* — many keeps compete for the same NeurIPS D&B / analysis-track slots and cite each other's turf; the field can absorb only a few "your benchmark is broken" papers per year before reviewer fatigue; (b) *reputational monotone* — a lab shipping 15 debunks and no constructive artifact reads as adversarial; (c) *stacking fragility* — several audits share one enabling assumption (public cached predictions of many models), so one infrastructure failure kills a whole family.
- **Counterweights already inside the batch:** the constructive artifacts (0260 cross-dataset harness, 0309 IRT machinery, 0311 uncertainty budget, 0302 power tables, 0252 geo-stratified set, 0310 design-based sampling) should be led with as *contributions*, not attacks. 0306 (coverage-preserving suppression) and 0321 (behavioral contracts) are the closest things to methods and deserve protection for that reason alone.
- **Blind spots of the batch itself (HYPOTHESIS):** almost everything is 2D, COCO/LVIS-centric, English-metadata, static-image detection. MICCAI-facing ideas are thin (0043 and little else). Nothing engages 3D, tracking, or the SAM/VFM wave that other Stage-1 agents are generating — good for dedup, bad for coverage. If the final 200 inherits batch C's mix unchecked, the portfolio will be an evaluation-science monoculture; I recommend the PI cap Tier-A eval-audits at ~60% of C's contribution to the 200.

## 4. What information would most change my ranking next

1. **Cached-prediction availability census.** A dozen top keeps (0276, 0256, 0261, 0264, 0255, 0271, 0253, 0309, 0328, 0302, 0331) assume per-instance predictions of many public models exist or are cheaply regenerable. A one-day audit of model zoos would re-rank the whole re-analysis family: if predictions must be regenerated at scale, "analysis-only" ROI claims deflate.
2. **The other agents' SAM/VFM batches.** Overlap/dedup against batches still being generated could kill or merge several C ideas (0082's mutation especially) and will determine whether C's eval-science skew gets balanced or amplified.
3. **Actual compute and annotation budgets.** The training-run family (0283, 0285, 0292, 0299, 0327, 0281) and the annotation-bounded family (0046, 0252, 0258, 0259, 0267, 0310, 0326, 0338, 0344) sit on opposite sides of a budget line whose position I had to guess. A concrete GPU-month and annotation-dollar figure would move ~25 rankings.
4. **Fresh arXiv sweeps on the fast-moving collisions.** Conformal OD (two papers in the last year), OVD prompt sensitivity (2026 activity), SR hallucination, and SAM evaluation are the four fronts where a 6–12-month-old SURVIVE can silently become a KILL. Re-run the attack on 0306, 0011, 0226, 0082 immediately before proposal writing.
5. **Whether double-annotated COCO subsets are accessible** (the LVIS double-annotation subset, COCO-ReM's verification data, the 2171-image multi-group re-annotations referenced in the ObjectLab line). 0046, 0338, 0344, 0311 all get dramatically cheaper if yes — that would push the GT-epistemology bundle to the very top of my board.

## 5. Process notes and epistemic status

- Scoring was single-pass but calibrated against explicit anchors (re-analysis ideas: feasibility/compute 5; training-grid ideas: compute ≤2 unless bounded; "already published" inverted scale used aggressively after each web collision).
- All prior-work claims in `prior_work_attack.md` are labeled KNOWN/EVIDENCE/HYPOTHESIS; every cited paper was retrieved via web search this session except two flagged in place (Picard 2021, Rodriguez et al. 2021 — cited from memory with identifiers, flagged as not re-verified).
- I did not read other agents' folders beyond Agent C's listed inputs, and wrote only under `Windows2/_wip/stage2_agent_D/`.
