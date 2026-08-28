# Portfolio Risk — What a CVPR AC Would Say About a Top-3 Drawn From Current Gravity

Agent L, Stage 6. The supervisor's ledger names four gravity wells: **A-0061** (topology at checkpoint selection),
**A-0206** (SAM fingerprint), **B-0114** (VPT-as-registers), **B-0001** (register-norm uncertainty), with the measurement
cluster capped. If the Top-3 were drawn from these today, here is the adversarial read.

## 1. The AC simulation

Assume Top-3 = {A-0061, A-0206, B-0114} (the ledger's current ordering), submitted as three CVPR papers from one lab.

**AC meta-review, composite (HYPOTHESIS, grounded in the EVIDENCE cited in audit.md):**

> Paper 1 (topology/checkpoint): careful measurement study; reviewers noted a Jan-2026 arXiv already proposes
> topology-aware checkpoint selection [2601.06067] and a MICCAI-line paper prescribes the metrics [2412.14619].
> Novelty is in the systematic quantification, not the phenomenon. R2 asks: "where is the selection rule you propose
> instead?" — the paper measures a problem others are already fixing.
>
> Paper 2 (SAM mask fingerprints): most original of the three; R1 likes it. R2 asks why mask-space attribution is not a
> straightforward port of image-attribution fingerprinting [ManiFPT-line; 2608.15652] and whether the "fingerprint" is
> just annotation-guideline dialect (the authors' own confound). Accept hinges entirely on the controlled-provenance
> corpus — which is also the paper's main cost.
>
> Paper 3 (VPT registers): R2 opens with the original VPT paper's Prompt-Fixed ablation and DA-VPT's printed observation
> that prompts are register-analogous; the contribution reduces to a careful 4-arm disaggregation of a connection already
> in print, on a backbone population (register-free ViTs) that is shrinking. Borderline.
>
> Cross-cutting: all three papers diagnose defects in standard practice; none ships a fix, a method, or an artifact the
> community will *use* (the fingerprint corpus is the exception if released). The lab's identity risk: "the group that
> tells you your pipeline is broken." Reviewer fatigue with this genre is documented inside your own pipeline (D's
> venue-concentration warning; H's note that NeurIPS-D&B-style teams industrialize these papers within quarters).

**If B-0001 replaces any of the three**, the portfolio gets worse, not better: B-0001 and B-0114 sit in the same
register/token-artifact micro-field — same literature, same confound family (norm/background entanglement), same
obsolescence event (register-equipped backbones by default; test-time registers already remove artifacts post hoc,
per H's verified citations). Two of three papers would rise or fall on one micro-field's fashion cycle. **They are one
bet in two costumes.**

## 2. Correlation matrix of the four gravity wells

| Pair | Shared failure mode | Severity |
|---|---|---|
| B-0114 × B-0001 | Register literature moves (registers default / artifacts fixed post hoc / "norms are background detectors") | HIGH — same micro-field |
| A-0061 × A-0206 | "Audit of standard practice" genre fatigue; both are diagnosis-without-fix | MEDIUM — genre-level |
| A-0061 × measurement cluster | Multi-seed training grids + metric-choice statistics infrastructure | MEDIUM — infrastructure |
| A-0206 × contamination cluster (B-0268, C-0122, C-0298, C-0345, A-0100) | "Your dataset is polluted" reviewer fatigue; 6 papers wide already | MEDIUM — must displace, not add |
| All four | ≤2 GPU-week experiments → H's measured ~1/3-per-12-months scoop hazard each; ≈70% that at least one of three is scooped in a year if execution is portfolio-paced rather than immediate | HIGH — timing |

Effective independent bets in the current gravity: **~2** (one token-artifact bet, one practice-audit bet), not 4.
G estimated ~90 effective bets in the 121-slot portfolio; the compression at the very top is far more severe than in
the portfolio at large — the funnel is concentrating correlation, which is backwards.

## 3. What a defensible Top-3 shape looks like (recommendation, not selection)

I do not pick the three. Structurally, a Top-3 that survives an AC contains at most ONE from each row:

1. **One audit flagship** — best-shaped candidates: A-0061 (with mandatory repositioning per audit Finding 2) or A-0206
   (if the provenance-corpus pilot lands). Not both.
2. **One constructive/method package** — candidates already in LOCK: **C-0306** (conformal coverage under NMS + a
   coverage-preserving suppression method — formal novelty, ships an algorithm), **C-0309** (IRT machinery + 1k short
   test — ships an artifact), **A-0163** (transition-band atlas + band-aware evaluation — ships a metric + dataset),
   or B-0114 executed so that the attention-bias arm yields a *register retrofit recipe* (the constructive reading of H's
   4-arm design).
3. **One mechanism/discovery bet** — candidates: B-0104 (invariance-dissociation grid), B-0304-mut (supervision taxonomy
   predicts quantization boundaries), B-0074 (gap-collapse dynamics, executed first per H's cluster warning), or a revived
   A-0199-mut dose-response (revive.md #2).

Portfolio constraints the PI should enforce at the lock, in writing:
- **≤1 slot per micro-field** (register/token-artifact; SAM forensics; annotation-noise metrology).
- **≥1 of Top 3 must ship a usable artifact or method**; "we release our audit code" does not count.
- **Every ≤2-GPU-week finalist gets an execution-start deadline inside one quarter**, or loses the slot to the next
  candidate — cheapness decays; H measured the rate.
- **The six-idea annotation-taxonomy dependency (J's cluster) counts as one slot** until the taxonomy exists. If two of
  the Top 5 need it, the taxonomy paper *is* the real Top-5 member and should be named as such.
- **Re-run freshness attacks at two gates** (proposal freeze, experiment freeze) for A-0061, A-0206, B-0114, B-0001,
  C-0306, C-0011, B-0268 — the fronts J/H/G/L identified as moving per-quarter.

## 4. The venue-honesty question the supervisor has been avoiding

**HYPOTHESIS with EVIDENCE base:** F said it directly ("if the PI optimizes MICCAI, promote 0074/0075/0061/0331/0315; if
CVPR/ICCV method tracks, promote the constructive Tier C"), D said it ("venue concentration... NeurIPS D&B / analysis
tracks"), and the supervisor's ledger has never stated a venue target. Three of four gravity wells are analysis papers
whose natural homes are NeurIPS D&B/analysis tracks or TMLR, not CVPR main. Locking a Top 5 without a venue decision
means the portfolio will be re-litigated at writing time — the most expensive possible moment. Decide the venue mix
first; the Top 5 follows almost mechanically from it.
