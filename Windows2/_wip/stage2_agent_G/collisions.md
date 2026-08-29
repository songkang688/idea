# Cross-Batch Collision Map — B ∪ C (Agent G)

Agent G (merger + feasibility auditor; not PI). Date: 2026-08-28.
Inputs: Agent D outputs (batch C), Agent E outputs (batch B), stage-1 idea text where needed.
Scope: only ideas that survived D/E review (D 107 keeps, E 77 keeps = 184 units). Batch A not read; Agent F not waited for.

Resolution vocabulary:
- **MERGE (host ← parasite)** — one ID keeps the slot; the parasite survives only as a *named mutation/arm* of the host and consumes no slot.
- **KEEP BOTH** — scientifically distinct; both hold slots; flagged as a correlated-bet cluster where relevant.
- Intra-batch merges D/E already made (e.g., B-0200→B-0213, C-0328→C-0309-as-recommended) are formalized here so the slot accounting in `provisional_200_partial.md` is exact.

---

## 1. PI-flagged collisions

### 1.1 B-0042 (mut) ↔ C-0011 — name/prompt variance vs published deltas
- B-0042 (mutated by E): synonym-variance ledger for open-vocab **segmentation** — is synonym-induced ranking variance bigger than published OVS effect sizes?
- C-0011 (survived D's attack, urgency flag): prompt-template variance vs architecture deltas on open-vocab **detection** leaderboards.
- Same inferential move ("vocabulary-side noise exceeds the effect sizes papers claim"), same instrument class (inference-only perturbation of the text side), different task and perturbation axis (synonyms vs templates).
- **Resolution: MERGE — host C-0011, parasite B-0042** as the named "synonym-variance ledger (OVS arm)". One *vocabulary-noise vs leaderboard-margins* paper covering OVD templates + OVS synonyms is stronger than two, and halves the reviewer-fatigue exposure of the "your eval is noise" genre. C-0011 hosts because the leaderboard-margin framing is sharper and D flagged execution urgency (2026 arXiv activity nearby).
- Related but NOT merged: B-0157 (prompt-template staleness inflates *forgetting* estimates) — different measurement object (retention audits, not leaderboards); B-0168 (template gains are calibration) — mechanism decomposition, not variance accounting. Both keep own slots.

### 1.2 B-0226 (mut) ↔ C-0081 (mut) — shift / pretrain transfer
- B-0226 (mutated by E): shift-budget curves — functional form of frozen-vs-tuned degradation under continuous shift for dense prediction; crossover-point stability.
- C-0081 (mutated by D): within-family compute-matched test of whether classification-checkpoint quality still orders dense-task performance (post-Battle-of-the-Backbones residual).
- Different scientific objects: B measures *robustness curves under shift* (frozen vs tuned as treatment); C measures *transfer-ordering* of pretraining quality (checkpoint rank as treatment). The overlap is thematic (pretraining vs dense downstream), not experimental.
- **Resolution: KEEP BOTH.** Note: C-0081-mut was a D *mutate* verdict, not in D's keep-set — it holds no slot in this portfolio; it remains available as a mutation if the PI wants it. B-0226 keeps its slot (E top tier). Flagged in the **frozen-vs-tuned correlated cluster** (with B-0234, B-0241, C-0150, C-0193).

### 1.3 B-0268 ↔ C-0298 — contamination / benchmark copies
- B-0268: AI-generated-image contamination of web-collected benchmarks + induced method-ranking distortion (eval-integrity, closing clean-baseline window).
- C-0298: hash-audit of circulating benchmark file variants (silent mutations of annotations/images across mirrors and years).
- Both are "benchmark forensics," but the mechanisms are disjoint (generated imagery entering data vs version drift of dataset artifacts), the instruments are disjoint (generated-image detectors vs cryptographic hashing), and the failure narratives are different.
- **Resolution: KEEP BOTH.** Additionally: **MERGE C-0264 → C-0122** (duplicate-concentration-in-the-tail becomes a stratified arm of the train-test duplication census — identical duplicate-detection infrastructure, and the tail stratification is one analysis cut, not a paper). B-0338 (web-agent benchmark contamination via retrieval) also stays separate — different contamination channel (retrieval reachability), decisive blinding design. All four (B-0268, B-0338, C-0122+0264, C-0298, plus C-0345) form the **benchmark-integrity correlated cluster**; the PI should treat them as one thematic bet at most 4–5 slots wide, which this portfolio respects.

### 1.4 B-0033 ↔ C-0136 — seed variance
- B-0033 (E keep, DP-protected): *pretraining*-seed variance of SSL VFMs vs published cross-model dense gaps (expensive; ViT-S scale pilot).
- C-0136 (D keep, survived attack, D bet #3): *detection-training* seed variance vs the distribution of published detection deltas (30 short/medium runs).
- Same scientific question — "is the leaderboard inside seed noise?" — at two pipeline stages with a >10× cost gap. Running them as separate papers invites the "salami" critique and duplicates the delta-census infrastructure.
- **Resolution: MERGE — host C-0136, parasite B-0033** as the named "pretraining-stage arm (execute only with a compute partner; ViT-S/ImageNet-100 pilot first)". E's DP protection is preserved: the arm is explicitly listed and cannot be silently dropped without PI sign-off. The delta-census (curated list of published deltas) is shared infrastructure across both arms.
- Related, not merged: C-0284 (seed-count power standard) is folded into C-0302 (see §2.6); C-0287 (ablation sign-flips) keeps its own slot (different object: component claims, not leaderboard deltas).

---

## 2. Additional collisions found by G

### 2.1 C-0001 ↔ C-0279 (intra-C, formalized) + cross-batch novelty transfer from E's kill of B-0037
- C-0001 (rare-class AP predicted by text-prior frequency) and C-0279 (rarity should be measured against pretraining exposure) are one exposure-vs-rarity paper; D already said "merge with 0001 at proposal time".
- **New cross-batch evidence:** E killed B-0037 citing *Udandarao et al. 2024* ("concept frequency predicts zero-shot performance" — the "No Zero-Shot Without Exponential Data" line). That kill evidence transfers: the frequency→performance headline is published for zero-shot classification, so C-0001/C-0279's remaining novelty is the **detection/LVIS-AP instantiation with visual-difficulty covariates partialled out**, and it must position against Udandarao et al. explicitly. D's attack did not check this collision.
- **Resolution: MERGE — host C-0279, parasite C-0001** (per-class frequency-regression arm) **and parasite C-0020** (invented-names / caption-leakage probe becomes the causal arm of the same exposure program; same corpora, same models, same conclusion space). Downgraded from "SURVIVE clean" to "SURVIVE with mandatory Udandarao positioning".

### 2.2 B-0023 ↔ C-0308 — machine psychophysics transplants
- B-0023: Landolt-C-style acuity battery for LVLMs; C-0308: adaptive staircase thresholds for detectors.
- Same methodological import (psychophysics → model evaluation), different model families, communities, and endpoints.
- **Resolution: KEEP BOTH**, flagged as a correlated *methodological* bet — if reviewers reject the transplant genre, both die together. Recommend shared stimulus/staircase tooling to amortize cost. C-0308 is the stronger host (D protected, novelty 5); B-0023 is FLEX.

### 2.3 B-0323 / B-0026 / B-0326 / B-0243 ↔ C-0279(+0001/0020) / C-0269 — supervision-statistics imprint
- All measure how language/corpus statistics (mention probability, nameability, name frequency, curation filtering) imprint on model competence.
- Instruments differ: feature decodability (B-0323), psycholinguistic norms (B-0026), granularity defaults (B-0326), adaptation boundary (B-0243), per-class AP regression (C-0279), dataset-composition tracing (C-0269).
- **Resolution: KEEP ALL, one correlated cluster.** If the general "corpus statistics predict per-class competence" premise fails, six bets weaken together. The causal arms (B-0323's caption-intervention retraining; C-0020's invented names inside C-0279) are the cluster's insurance and should be prioritized in execution order.

### 2.4 B-0208 / B-0018 / B-0013 / B-0284 ↔ C-0007 / C-0338 / C-0340 — size / sampling-floor laws
- Six size-law instruments: patch-occupancy recall law (B-0208), thin-structure Nyquist law (B-0018), sub-patch inverse scaling (B-0013), lesion-size/stride law (B-0284), tiny-object annotation-noise floor (C-0007), human small-object ceiling (C-0338), pixel-count causal isolation (C-0340).
- Distinct mechanisms (architecture sampling vs annotation noise vs human perception) — **KEEP**, but the PI should know these compete for the same "small objects are different" narrative slot at venues. C-0007 and C-0338 share annotation infrastructure with C-0344/C-0046 (see census).

### 2.5 B-0227 ↔ C-0115 / C-0344 — label-quality economics
- B-0227 (cleaner labels transfer worse — noise-ladder paradox), C-0115 (quality-vs-quantity exchange rate at fixed budget), C-0344 (instructions exceed inter-annotator noise).
- Distinct claims (paradox vs exchange rate vs protocol effect). **KEEP ALL**; cluster-flag only.

### 2.6 Intra-batch merges formalized for slot accounting
These follow D's/E's own recommendations; G formalizes them so each consumes one slot:
- **C-0302 ← C-0070, C-0065, C-0284** — one power/significance infrastructure paper: MDE tables (0302/0070) + claims re-analysis (0065) + seed-count standard (0284). D's own bundling note proposed exactly this rigor bundle.
- **C-0311 ← C-0064, C-0042, C-0282** — the metrology uncertainty budget hosts its own components: bootstrap-axis choice (0064), noise-derived IoU threshold (0042), framework variance (0282; D's top-20 entry for 0311 already lists framework variance as a budget component).
- **C-0309 ← C-0328** — D's attack verdict (tinyBenchmarks collision): the 1k-subset result is the application half of the IRT paper.
- **C-0226 ← C-0248, C-0231** — GT-controlled SR accounting hosts the asymmetry analysis (0248, per D's mutation note which already folds 0248) and the object-destruction rate (0231) as arms of one SR-truthfulness paper.
- **C-0338 ← C-0071** — forced partly by a *fresh prior-work hit found during the census*: **Label Convergence (arXiv 2409.09412)** already estimates an upper performance bound from contradictory annotations using the LVIS doubly-annotated subset and bootstrapped mAP, with Co-DETR near the bound. C-0071's standalone headline ("is SOTA above the human ceiling?") is partially occupied; it survives as the size-stratified arm of C-0338, which must cite Label Convergence in the first paragraph.
- **C-0150 ← C-0221** — one "UDA reckoning" paper, two instruments: 50-labeled-images comparison + foundation-backbone gap-closure audit. Both are cheap; together they are decisive.
- **C-0122 ← C-0264** — see §1.3.
- **C-0046 ← C-0080** — intra-dataset tightness drift becomes a measured component of the annotation-noise band (same double-annotation infrastructure now confirmed public; see census).
- **C-0279 ← C-0001, C-0020** — see §2.1.
- **C-0290 ← C-0296** — pretrained-weight provenance joins the silent-variables/determinism audit, per D's own note ("bundles naturally").
- **B-0213 ← B-0200** — already merged by E (probe-capacity × resolution protocol-confound audit). Recorded here; one slot.
- **B-0098 ← B-0095** — E's attack verdict on 0098 already prescribed "merge with 0095's displacement-budget control". One slot.
- **B-0234 ← B-0112** — E's note on 0234: "unifies 0112/0127/0226 family"; the LoRA-vs-full-FT shift crossover (0112) is one axis of the 2D phase boundary (0234). B-0226 stays separate (top-tier; the budget-curve functional form is its own object).
- **C-0136 ← B-0033** — see §1.4.
- **C-0011 ← B-0042** — see §1.1.

### 2.7 Checked and explicitly NOT merged (scientifically distinct)
- B-0001 (register-norm uncertainty) ↔ C-0190 (flicker as free uncertainty) ↔ C-0119 (transform rank-stability predicts AP): three "free signal" ideas with disjoint mechanisms (artifact geometry / temporal inconsistency / perturbation stability). Keep; cluster-flag ("free uncertainty signals").
- B-0268 ↔ C-0122: generated-image contamination vs near-duplicate contamination — disjoint mechanisms, keep both (§1.3).
- B-0145-mut (dense calibration decays before accuracy) ↔ C-0158 (NMS destroys calibration): both calibration, disjoint pipelines (adaptation dynamics vs detection post-processing). B-0145 was independently dropped on prior-work grounds (E demoted it after the LLM/CL ordering papers), not on this collision.
- B-0213-mut (probe/resolution confound in VFM rankings) ↔ C-0260 (benchmark monoculture) / C-0253 (granularity knob): different measurement objects (probing protocol vs cross-dataset generality). Keep B-0213 and C-0260.
- B-0286/B-0293 (medical FM science) ↔ C-0043 (Dice on small structures): complementary, no overlap.
- B-0164 (savings/relearning) ↔ nothing in C. B-0304 (morph quantization) ↔ nothing in C.
- C-0116 (ghost rate) ↔ B-0039 (killed co-occurrence hallucination): C hosts; B-0039 stays dead (POPE lineage).

---

## 3. Summary table

| # | Collision | Resolution | Slot effect |
|---|---|---|---|
| 1 | B-0042 ↔ C-0011 | MERGE: C-0011 hosts | −1 |
| 2 | B-0226 ↔ C-0081-mut | KEEP B-0226 (C-0081 was already only a mutation, no slot) | 0 |
| 3 | B-0268 ↔ C-0298 (+C-0122, B-0338, C-0345) | KEEP BOTH; C-0264→C-0122 | −1 |
| 4 | B-0033 ↔ C-0136 | MERGE: C-0136 hosts | −1 |
| 5 | C-0001/C-0020 ↔ C-0279 (+ Udandarao transfer from B-0037 kill) | MERGE: C-0279 hosts | −2 |
| 6 | B-0023 ↔ C-0308 | KEEP BOTH (correlated methodological bet) | 0 |
| 7 | C-0071 ↔ C-0338 (+ Label Convergence 2409.09412) | MERGE: C-0338 hosts | −1 |
| 8 | Intra-batch formalizations (§2.6) | 12 further parasites | −12 |

Total parasites (merged, no slot): **23** — C-side 18 (0001, 0020, 0042, 0064, 0065, 0070, 0071, 0080, 0221, 0231, 0248, 0255*, 0261*, 0264, 0282, 0284, 0296, 0328), B-side 5 (0033, 0042, 0095, 0112, 0200).

*0255→0276 (head-class utility arm) and 0261→0256 (tail-definition arm) are census-driven demotions of the long-tail re-analysis family — see `feasibility_census.md` §3 — following D's own bundling note (long-tail forensics bundle).

All merges are reversible: every parasite is named at its host and can be re-promoted by the PI or after Agent F reports.
