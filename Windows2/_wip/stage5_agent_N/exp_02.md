# exp_02 — B-0001: register-norm map — uncertainty channel or saliency prior? (+ dissociation plan from B-0114)

**ID:** W2-B-0001 (H's mutated framing is mandatory: stratified audit, not free-lunch pitch).
**Pipeline status:** E bet #2 → G LOCK (mission-protected) → H SURVIVE-IF-EXPERIMENT → L: window open (H's "no paper sells the norm map as per-pixel uncertainty" independently reproduced by L's search) but same micro-field as B-0114 — counts as one bet unless dissociated (PI binding).

## Research question

Is the high-norm artifact-token map in frozen ViTs a genuine **per-pixel error-prediction channel** — beating free baselines *within foreground and near boundaries* — or merely a background/saliency prior that inflates aggregate AUROC?

## Falsifiable hypothesis

H1: On register-free DINOv2, the token-norm map predicts per-pixel linear-probe segmentation error with AUROC/AUPRC exceeding all five free baselines **within foreground strata and within distance-to-boundary bands**, not just overall.
Falsified if: the norm map loses to softmax entropy or distance-to-boundary within foreground strata (then it is a saliency/background prior — Darcet et al. KNOWN result that high-norm tokens sit in low-informative background predicts exactly this failure).

## Prediction

HYPOTHESIS: overall AUROC will look strong but stratified AUROC will collapse toward baseline parity — we assign the deflationary branch ≥50% prior probability and pre-commit to publishing it (H: "a weak/negative result is publishable only as a short deflationary note"; we structure the program so that note has a home — see Dissociation).

## Method sketch

No new model. Pipeline: (1) frozen backbones: DINOv2 (no registers), DINOv2-reg, and test-time-register-patched DINOv2 (arXiv:2506.08010); (2) linear probe per backbone on each dataset; (3) predictor maps computed per image: (a) token-norm map (patch-level, upsampled), (b) probe softmax entropy, (c) distance-to-predicted-boundary, (d) local edge density, (e) feature distance to train-class prototypes; (4) stratified evaluator: fg/bg strata × distance-to-boundary bands × dataset; (5) register-regime comparator: does the signal survive on register-equipped/patched models at all?

## Data

ADE20K + Cityscapes (per H's specification). Optionally one shifted set (e.g., ACDC-style adverse conditions) only if the primary result is positive.

## Baselines

Predictors (b)–(e) above — all free, all mandatory (H names them as the "embarrassing baselines"). PH-Reg (2505.21501) caveat handled by reporting low-norm-artifact prevalence; SINDER (2407.16826) cited for weight-determined artifact direction.

## Metrics

Per-stratum AUROC/AUPRC of per-pixel error prediction; risk-coverage curves for selective prediction; norm-vs-error monotonicity within foreground (H's hidden assumption 1, tested directly).

## Killer Experiment

Exactly H's specified audit: **3 backbone regimes × 2 datasets × 5 predictors, stratified fg/bg and by boundary distance.** One pass of probe training + inference; the entire paper's fate is decided by one table (foreground-stratified AUROC ranking).

## GPU/VRAM/time estimate

**~1 GPU-week on one 24–40GB GPU** (probe training is hours per dataset-backbone; inference and analysis dominated by disk I/O). Cheapest of the B-batch protocols after A-0028.

## Stop / pivot / kill criteria

- **Kill standalone paper** if norm map fails within-foreground superiority on register-free models → fold the deflationary note into the merged registers paper (below).
- **Pivot** to selective-prediction/deployment framing only if it wins the strata AND survives ≥ partially on register-equipped models; if the signal exists only on register-free models, scope claims to legacy backbones explicitly.
- **Stop** immediately and re-search if any paper selling norm-as-uncertainty appears before execution (H and L both verified absence as of their sessions; this is the fastest-moving check in the batch).

## Dissociation plan from B-0114 (mandated)

The two ideas share one literature and one confound family (PI binding: one bet in two costumes). Plan:

- **Claim-level dissociation:** exp_01 answers a *mechanism attribution* question about a PEFT method (where do VPT gains come from); exp_02 answers a *consequence/utility* question about frozen-backbone artifacts (is the artifact map usable signal). Neither result implies the other: VPT could be pure learning while norm maps still predict error, and vice versa.
- **Operational dissociation:** exp_02 contains **no PEFT anywhere** (linear probes only); exp_01 makes **no uncertainty claims**. No shared headline term beyond "registers".
- **Decision rule (pre-registered):** run exp_02's killer first (1 GPU-week, cheapest). If deflationary → **merge**: one registers paper, two experiments — mechanism (exp_01 4-arm) + consequence audit (exp_02) — satisfying L's "cap the register micro-field at one slot". If exp_02 wins its strata → two dissociated papers are justified, but they still may not both enter the Top-3 (AGENT_REPORT constraint).

## Reviewer-2 leftover

Even a within-foreground win leaves "the population of register-free models is shrinking quarterly" (H) — the paper must state plainly what happens on register-equipped backbones, and the honest answer may be "the channel is dying". Sparse artifact coverage (few tokens/image) may cap achievable AUPRC regardless of signal quality.

## Expected result (HYPOTHESIZED, not measured)

Norm map wins unstratified AUROC, loses or ties entropy within foreground; signal absent on register-equipped models. Merged-paper branch is the modal outcome.

## Negative-result interpretation

A clean deflationary result is field-useful: it stops a plausible free-lunch meme before deployment papers adopt it, and it completes the registers story (mechanism + non-consequence) in the merged paper. It also frees a Top-5 slot from the register micro-field — the portfolio-level reading L's audit asked the PI to price.
