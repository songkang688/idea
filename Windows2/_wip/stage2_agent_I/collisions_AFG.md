# A vs B∪C Portfolio Collisions — Resolutions (Agent I)

Agent I (merger + novelty assassin; **not PI, no final-3**). Date: 2026-08-28.
Resolves G's six predicted collision fronts plus four additional collisions found during the fold. Notation: **host ← parasite** (parasite = named arm, no slot). G files untouched; all resolutions live in my `provisional_200.md`.

## 1. Prompt-jitter cluster (G predicted: A jitter vs B-0169/B-0194; RClicks killed B-0175)

- **No A jitter-duplicate admitted.** F's shortlist contained no direct click-jitter robustness idea (RClicks territory); tier-2 candidates in that space (A-0008 click-order path dependence, A-0106 prompt-through-glass) stay **cut**.
- **B-0169** (negative-click dose-response) and **B-0194** (segmentation sycophancy) keep their LOCK slots unchallenged.
- **New collision found: A-0341 vs B-0182** ("scale increases prompt sensitivity" — A on ambiguous objects/visual prompts, B on rare classes/text prompts). **KEEP BOTH** with a hard modality split: A-0341 owns visual-prompt granularity-hypothesis flipping (mini-SAM series), B-0182 owns text-template sensitivity on rare classes. Mandatory mutual citation; if the PI wants one slot, A-0341 is the more sophisticated claim and would host.
- **A-0065** (clinician-click sim2real gap, rescue) admitted only as the medical port of RClicks — the clinician corpus and method-reordering claim are the paper; RClicks cited as the instrument.

## 2. SA-1B/SAM fingerprint & contamination cluster (cap: 5 slots)

Members before merge would have been 6+ slots. After merge, exactly **5**:

| Slot | Idea | Arms absorbed |
|---|---|---|
| 1 | **A-0206** SAM-fingerprint detection (LOCK) | ← A-0264 (SAM pseudo-label error anatomy) |
| 2 | **A-0205** verification bias / correlated accepted errors (LOCK) | — |
| 3 | **A-0301** SA-1B swallowed the test sets (FLEX) | ← **C-0345** (foundation-model test-set exposure; ⏰ urgency inherited) |
| 4 | **B-0268** generated-image contamination (LOCK, ⏰) | — |
| 5 | **C-0122** train-test duplication census (LOCK) | ← C-0264 (G's merge), ← **A-0100** (smoke/fire video-provenance dedup), ← **C-0298** (hash-audit of benchmark variants) |

- **C-0298 → C-0122** is the cap-enforcing merge: the hash-audit is a sub-instrument of the duplication census (same forensic infrastructure, same deliverable format). Its (P) protection is honored as a named arm.
- **Kept outside the cap** (different lineage/target, mandatory cross-citation): A-0312 (dataset-dialect classification — sociology, not SAM provenance), A-0315 (patient-level leakage — medical hygiene), C-0269 (CLIP curation bias), A-0025 (topology-bias mechanism).

## 3. Annotation-noise / seed-churn / boundary-raster vs C-0311 (GT-epistemology host)

- **A-0198 (seed-churn maps) → arm of C-0311.** Churn is the model-variance axis of C-0311's metrology budget (which already hosts bootstrap, noise-derived IoU threshold, framework variance). The gains-concentrate-on-churn-pixels audit rides inside.
- **A-0164 (tiny-object noise floor) → arm of C-0007** (same instrument, near-duplicate across batches; A's jitter-propagation derivation becomes the method).
- **A-0151 (three-way boundary error decomposition) KEEPS its own FLEX slot**: C-0311 budgets COCO AP (detection); A-0151 budgets boundary metrics for segmentation. Shared metrology tooling, different metric family and audience. Cross-referenced.
- Boundary-raster mechanics: **A-0003 → arm of B-0018** (patch-grid aliasing phase-sweep inside the thin-structure Nyquist law) and **A-0153 → arm of B-0203** (analytic bilinear sharpness floor inside the post-upsampler decomposition).

## 4. A-0245 UDA rank-correlation vs C-0150 / B-0226

- **A-0245 → arm of C-0150** (UDA reckoning host): cross-pair rank-stability with frozen hyperparameters becomes C-0150's third instrument (after 50-labeled-images and foundation-backbone gap-closure).
- **B-0226** (shift-budget curves frozen-vs-tuned) is a different object (functional form of shift response, not method-ranking reproducibility) — untouched.
- Rescue **A-0226 was NOT admitted** (tier-2 gap-decomposition idea) — too adjacent to this cluster; stays cut.

## 5. Medical rebalance vs B-0293

- **B-0293 → folded into B-0286** (site-of-origin decodability), exercising G's own recorded fallback ("compute-partner-conditional, else fold residual into B-0286"). No compute partner exists at merge time, and batch A supplies cheaper instruments that cover the medical-science need.
- A's medical slate after the fold (11 slots): A-0074 (volume-CI validity audit), A-0058 (directional tumor uncertainty), A-0061 (Dice-topology checkpoint claim), A-0071 (inter-rater ceiling audit), A-0075 (STAPLE minority erasure), A-0063 (annotation-fatigue forensics), plus rescues A-0046 (ultrasound speckle vs SAM2 memory), A-0062 (2D→3D spacing crossover law), A-0065 (clinician-click gap), A-0068 (extreme-imbalance phase transition), A-0315 (patient-leakage audit).
- Note: these answer *measurement/annotation/deployment* questions, not B-0293's pretraining-attribution question — that question survives as the named residual arm inside B-0286, revivable if a compute partner appears.

## 6. SAM-failure atlas: C-0082 re-entry

- As G predicted, the mutated **C-0082 failure-scaling law re-enters via A's slot**: it becomes a named arm of the **A-0026 unit** (masklet-drift-predictability, F-protected slot), forming one SAM-failure-prediction paper: static first-frame ambiguity → drift forecast (A-0026) + failure-law fitting (C-0082-mut). Cut tier-2 ideas A-0029 (erosion bias) and A-0043 (absorbing-state failure) are flagged as optional third arms if the unit needs more observables — no slots.

## 7. Additional collisions found during the fold (not predicted by G)

| Collision | Resolution |
|---|---|
| **A-0334 vs C-0333** ("mask shape leaks semantics" vs "silhouettes are almost enough") | **A-0334 hosts ← C-0333.** Same shape-sufficiency territory; A-0334 carries the larger claim set. Post-reconciliation caveat: J found **BareBones (arXiv:2604.10528)** — a silhouette-only recognition benchmark — which scoops much of C-0333's capability measurement and demotes the host to FLEX [mut] (documented-practice privacy audit is the surviving leg). |
| **A-0237 vs C-0208** (label conventions masquerade as domain shift vs "label conventions are a domain" hosting 0014/0134) | **A-0237 hosts ← C-0208 (incl. its 0014/0134 arms) ← A-0249.** A's version has the falsifiable >25%-of-gap figure and the UDA credit-assignment stakes; C-0208's framing and arms survive inside. |
| **A-0337 vs C-0078** (mask metrics vs downstream, segmentation vs detection) | **A-0337 hosts ← C-0078.** One metric→downstream validity program with instrumented consumers; detection (AP) is an arm. Also carries A-0352's residual decision-rule framing. |
| **A-0300 vs A-0290** (ensemble-gain collapse vs shared blind spots) | **A-0290 hosts ← A-0300** (temporal-trend arm; same model-zoo infrastructure, same monoculture thesis). |
| **A-0076 vs A-0091/A-0082** (smoke metric audits, internal to A) | **A-0076 hosts ← A-0091 (human-judgment vs IoU rankings) ← A-0082 (annotator alpha-threshold distribution).** One smoke-metrology paper: binary-mask rankings vs density labels, with the human-preference and alpha-cutoff arms. |

## 8. PI directive (`_wip/PI_TO_I.md`) — applied after F/H/J completion

- **B kills mandated by Agent H:** B-0332 (LOCK; arXiv:2510.23482 scooped visual-thought corruption), B-0133 (opposite-direction LoRA-memorization results), B-0025, B-0252 — all dropped, no arms. **B-0042 residual relocated** from C-0011 to B-0213 (SynCLIP).
- **Re-annotation-arbiter cluster consolidated** (J risk #1: 0237, 0249, 0151, 0150, 0163, 0071 all use better-annotations-as-referee and share one unbuilt noise/convention/quality/ambiguity taxonomy): 0237+0249 merge already mandatory; additionally **A-0151 → arm of A-0163** and **A-0071 → arm of C-0043**. Remaining slots: A-0237, A-0150, A-0163 — declared one GT-epistemology program with a single shared taxonomy + multi-rater pool.
- F's mutated forms preferred throughout for 0001, 0060, 0076, 0107, 0181, 0198, 0245, 0301, 0326, 0074, 0331, 0300, 0352 (0001/0060 were never in the keep set; all others carry the mutation in `provisional_200.md`).
- Flagship protections honored: 0206, 0163, 0150, 0121, 0175, 0145 all hold slots; 0151 survives as a named arm.

## 9. Agent K (Reviewer-2 on batch C) — verdicts ingested

- **K kills applied (5 C slots):** C-0046 (Label Convergence + Noise-Aware Evaluation, WACV 2025, own the LVIS/COCO noise-band artifact — 0080 tightness-drift arm relocated to C-0311, claims-audit residual to C-0302) · C-0341 (2025–26 determinism/batch-invariant-kernel literature explains and fixes batch cross-talk — residual paragraph in C-0290) · C-0303 (Recht adaptivity null + COCO-O; observational design un-deconfoundable) · C-0119 (PCR, ICCV 2025 oral, owns label-free mAP-from-consistency) · C-0055 (unfundable without industrial partner; conditional revival recorded).
- **Slot backfill:** tier-2 A-0043 (VOS absorbing-state analysis) promoted from optional-arm status to a FLEX slot, holding the portfolio at the 190 floor.
- K's MUTATE/SURVIVE-IF-EXPERIMENT gates on C hosts (0302, 0309, 0344, 0007, 0043, 0122, 0150, 0158, 0277, 0327 and the SURVIVE-IF set) do not change slot structure; they are flagged inline in `provisional_200.md` and live in `stage4_agent_K/`.

## Cross-batch balance effects

- G FLEX displaced into arms of A hosts: **C-0208, C-0345, C-0078, C-0333** (4 slots, content preserved).
- G LOCK merged within G: **C-0298 → C-0122** (cap enforcement).
- G FLEX folded within G: **B-0293 → B-0286** (G's own conditional).
- H/PI kills in B (no arms): **B-0332, B-0025, B-0133, B-0252**.
- A ideas merged into G hosts (content preserved, no A slot): **A-0245→C-0150 · A-0164→C-0007 · A-0313→C-0302 · A-0322→C-0300 · A-0228→C-0212 · A-0305→C-0326 · A-0100→C-0122 · A-0323→C-0338 · A-0198→C-0311 · A-0071→C-0043 · A-0003→B-0018 · A-0153→B-0203 · A-0220→C-0115** (13).
- A-internal merges: **A-0249→A-0237 · A-0264→A-0206 · A-0300→A-0290 · A-0091→A-0076 · A-0082→A-0076 · A-0151→A-0163** (6), plus **C-0082-mut→A-0026** re-entry.

All merges are reversible; every parasite is named at its host in `provisional_200.md`.
