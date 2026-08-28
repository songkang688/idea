# Stage 5 — Cluster C Top Nominees

**Experimental Engineer (Cloud Sub-Agent O) → Supervisor Windows7.**
7 Stage-4 survivors engineered against real codebases (`stage5_cluster_C_engineering.md`); ranked by (decision value per GPU-hour) × (does it change how people **train/evaluate** models, per Supervisor preference). Costs in `stage5_cluster_C_roi.csv`.

**KEEP: C-0090 (rank 1) and C-0028 (rank 2). Optional 3rd slot: evaluated and declined** — C-0158's killer measurement is exceptional *and* cheap, but its paper-level claim is neither; its Phase-1 probe is recommended as a ~$2K rider (details below).

---

## NOMINEE 1 — C-0090: Text-batch rehearsal works by gradient rebalancing, not by content

**One-liner:** Five rehearsal arms {none, curated, random web text, shuffled tokens, single repeated document} at fixed token budget on a LLaVA-1.5-7B fine-tune decide whether rehearsal-data *content* does anything that a matched-scale gradient on the language pathway doesn't.

**Killer experiment:** 15 fine-tunes (5 arms × 3 seeds) on the exact published LLaVA-1.5 recipe (`haotian-liu/LLaVA`), capability-stratified retention (fluency / knowledge / reasoning / instruction-following via `lm-evaluation-harness`; VL sanity via `lmms-eval`), reported under two pre-registered gradient-matching conventions (global-norm, per-layer). Pre-registered rule: gradient-balance mechanism confirmed iff random-web-text retention ≥ 80% of curated retention on ≥3 of 4 language capabilities under both conventions. The shuffled-token and single-doc arms dissect *what* about content matters if anything does.

**Why rank 1:**
- **Cheapest decisive design in the cluster** (~2.3K A100-h, no annotation, no API spend) with the highest branch-coverage: mechanism confirmed → the field stops paying for rehearsal curation; mushy middle → first per-capability rehearsal dosing recipe ("X% real text, only for knowledge"); refuted → first controlled multimodal refutation of the pseudo-rehearsal account. All three are training-practice changes.
- No scale escape hatch: the phenomenon lives at fine-tuning scale, which is exactly where we run.
- Scoop check done this session: the closest prior (arXiv:2410.19925, continual learning for LLaVA) uses real-data rehearsal only — no content-free controls, no gradient-matching analysis. Scaffold, not scoop.
- Fifteen fine-tunes from done; every component is a verified public codebase.

**Kill condition honored:** if seed variance swamps the curated-vs-none gap after 6 runs and a 13B escalation doesn't fix power, report the power analysis and kill at <1K A100-h spent.

---

## NOMINEE 2 — C-0028: In-batch concept co-occurrence, not loss design, creates dense alignment

**One-liner:** The hardness-matched decision triple — random vs noun-overlap-curated vs hardness-matched-without-co-occurrence batches at CLIP-B/32 on a frozen 20M-pair corpus — isolates whether batch *co-occurrence structure* causally creates patch-level alignment, or whether it's generic hard-negative pressure.

**Killer experiment:** 13 pretraining runs in `mlfoundations/open_clip` (decision triple × 3 seeds + 4 dose-curve runs), batch curation implemented as the maintainer-documented webdataset `compose()` iterator; H-arm batches quantile-matched to N-arm in-batch similarity histograms (KS < 0.05, verified offline before any GPU spend) under a no-shared-noun constraint. Dense metrics via two independent training-free protocols (SCLIP, NACLIP) + a raw patch-alignment score; retrieval via CLIP_benchmark, reported jointly. Pre-registered rule: mechanism isolated iff ΔmIoU(N−R) > 2σ, ΔmIoU(N−H) ≥ 0.5·ΔmIoU(N−R) under both protocols, and the dose curve is monotone.

**Why rank 2:**
- **Largest practice-change surface if it lands:** batch composition becomes a documented, nearly-free pretraining dial for dense ability — a recipe change for anyone training contrastive VLMs, no new objective needed.
- Every Reviewer-#2 attack has a design answer: hardness-matched control (attacks 1/2/4), monotone dose curve (attack 3's vacuous-null), dual dense protocols (protocol artifact).
- The JEST-reframe outcome (N tracks H) is still a publishable controlled refutation with the first dense-task accounting of batch hardness — JEST never measured dense grounding (Stage-3 search).
- The offline dry-run gate (similarity-histogram matching + noun-rate checks on 10K generated batches) de-risks the full 5.2K A100-h program at zero GPU cost.

**Kill condition honored:** if the H arm is unconstructible at curation strength ≥ 0.25 on this corpus, kill before the first pretraining run.

---

## Optional 3rd — evaluated, DECLINED: C-0158 (uncertainty sampling × LLM-annotator error)

The bar was "exceptional + cheap." Its Phase-1 killer *measurement* clears both: ~$1.5K API + ~120 GPU-h to put a number (item-level Spearman between learner uncertainty and annotator error, on four ground-truthed pools × two annotators) on a mechanism the field currently argues about with folklore. But the *nomination unit is the paper*, and the paper needs Phase 2: matched-total-cost acquisition arms in binding-budget settings (VLM dense annotation, frontier-annotator at scale) including the annotate-everything + noise-robust baseline — real spend, and a deliverable that is pipeline advice rather than a training-recipe change of the top two's magnitude.

**Recommendation:** fund Phase 1 as a rider during the nominees' programs; promote to full nomination next cycle iff ρ ≥ 0.3 with a working self-consistency error-predictor (AUROC ≥ 0.7). If ρ ≤ 0.1 everywhere, publish the cheap null and close the thread permanently.

---

## Drop reasons (ranks 4–7)

| Rank | ID | Drop reason (one line) |
|---|---|---|
| 3 | C-0158 | Killer measurement cheap+exceptional, paper is neither; deliverable is pipeline advice → rider, not nominee |
| 4 | C-0310 | Clean label-invariant intervention, but headline is a magnitude-comparison audit; dense labels need new annotation money; training arm contends with Rawgment (no public code — reimplementation dependency). Revival trigger: public RAW+dense-label driving set (RAWDet-7 shows the ecosystem moving) |
| 5 | C-0302 | Cheap, genuinely open dissociation — but the payoff (diagnosis + debiasing-depth knob) serves a narrow subcommunity; outranked on practice-change breadth. First-call fallback if a nominee dies at Stage 6 |
| 6 | C-0128 | Best validation design in the cluster, but the deliverable is an instrument+score; the training implication is downstream work the paper motivates, not performs — loses under the anti-audit preference |
| 7 | C-0229 | Right control, worst ROI: 6–9K A100-h for a decomposition whose deflation targets live 100× above affordable scale; likely outcome is the known middle, pricing an investment without changing a recipe |

## Portfolio note

Both nominees are training-mechanism causal tests (the Stage-4 portfolio's strongest axis) and share nothing but the eval-harness infrastructure — no correlated kill risk: C-0090 lives at fine-tuning scale on public recipes; C-0028 at small-pretraining scale with an offline-verifiable treatment. Combined program ≈ 7.5K A100-h + $0 annotation, inside a single 8×A100 node's budget for the cycle.
