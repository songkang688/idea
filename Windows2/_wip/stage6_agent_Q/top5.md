# Top 5 — Stage-6 Cut (Agent Q, Top 20 → Top 5)

Not the final 3 — the 5→3 fight comes later. Seats carry O's battle-locked mutated forms; arms are binding.
Killer experiments reference Agent N's Stage-5 protocols where they exist (exp_01–exp_10); B-0194+B-0169 has
no N protocol and carries O's battle-locked design. Order below is NOT a ranking except where stated in
AGENT_REPORT (first-GPU-day recommendation).

Constraint compliance: exactly one of {A-0061, A-0206, C-0338} seated (C-0338; no genre override claimed);
A-0061 and A-0206 both out; B-0001 remains a named arm of B-0114; C-0306 fills the constructive/method
requirement; A-0028 included (mandated kill attempt failed — no new fatal flaw + citation found); mix is
    10|method + registers + SAM/video + interactive/safety + one eval audit with a silencing experiment.

---

## 1. C-0306 — conformal coverage vs NMS (constructive/method seat)

- **Mutated one-liner:** Conformal coverage guarantees are destroyed by NMS, and a coverage-preserving
  suppression rule restores them at competitive set size.
- **Killer experiment (N exp_05):** Gate first — measure the fraction of GT objects whose only covering
  candidates NMS suppresses, across detectors, thresholds, and crowdedness strata (2–4 GPU-days,
  analysis-only). If material, build coverage-preserving suppression and benchmark vs SeqCRC-post-NMS and
    20|  no-NMS IoU-aware calibration on the risk/set-size frontier.
- **Stop/kill criteria:** KILL if the gate fraction is below the pre-registered materiality threshold across
  all crowdedness strata (ship the gate as a short note). KILL if a third conformal-OD paper prints a
  coverage-preserving suppression rule before execution starts (per-quarter scoop re-search mandatory;
  months-scale clock per K). SCOPE-STOP to a crowded-scenes method if the fraction is material only in
  crowded strata. Seat converts to a kill if execution has not started within the quarter (⏰).
- **Why it beat the other 15:** Only battle-ready constructive package in the 20 (A-0206's constructive
  branch needs a corpus; B-0114's retrofit branch needs the 4-arm result first) — binding constraint made it
  the default and nobody displaced it. Cheapest decisive gate in the portfolio (N's ROI #1, O's
  battle-ready #1); unanimous in every round it has fought.
    30|- **Remaining risk:** The gate fraction may be small outside crowded scenes; the conformal-OD field is
  moving on a months-scale clock and can print first.

## 2. B-0114 — VPT-as-registers, 4-arm dense-task form (+B-0001 artifact-map arm) (registers/PEFT mechanism seat)

- **Mutated one-liner:** VPT's dense-task gains are partly register function — token arms dissociate
  register absorption from added capacity, and the norm-map arm tests artifact maps as free uncertainty.
- **Killer experiment (N exp_01, gated by exp_02):** H's 4-arm × 2-backbone grid — full VPT vs frozen-random
  vs attention-bias-only vs no-token, on register-free AND register-equipped siblings, ≥3 dense tasks, with
  NOP/broadcast diagnostics (arXiv 2606.08105) as readout axes and a pre-registered interpretation table
    40|  (1–1.5 GPU-weeks). B-0001 arm: stratified AUROC of the register-norm map vs entropy /
  distance-to-boundary / edge-density baselines. **Ordering condition (binding from Round 3):** N's exp_02
  (~1 GPU-week) runs BEFORE the full 4-arm study is committed — it is the dissociation/merge decision
  experiment for the register micro-field.
- **Stop/kill criteria:** DROP the B-0001 arm if exp_02 shows the norm-map signal fails cheap baselines
  within-foreground on register-free models (4-arm study proceeds as pure mechanism paper). KILL the seat if
  a register-mechanism paper with dense-task token arms prints first. STOP if the 4-arm result is
  non-directional mush even under the pre-registered interpretation table (i.e., effects neither vanish on
  register-equipped siblings nor persist cleanly). Obsolescence clock: start this quarter — the register-free
  backbone population shrinks every quarter.
    50|- **Why it beat the other 15:** Won the register/PEFT slot over B-0104 7–1: B-0104's premise dies to any
  single high-rank + tuned-LR ablation (cheap for others to run by accident), while B-0114's mush risk is
  bounded by the 2-backbone design; execution-grade today with no external dependency; best mechanism bet in
  the 20 per H and N (ROI #5 despite costing more than the gates above it).
- **Remaining risk:** Partial-reproduction "mush" if the interpretation table doesn't cover the observed
  cell; register-equipped backbones shrink the relevant population (window, not flaw).

## 3. A-0028 — SAM2/SAM3 teleport probe (SAM/video capability seat)

- **Mutated one-liner:** The distractor-fix papers (DAM4SAM arXiv:2509.13864; SAM2/SAM3 memory-design line
  arXiv:2512.22624) presuppose an appearance-vs-location arbitration nobody has measured — teleport probes
    60|  measure it directly on SAM2 AND SAM3.
- **Killer experiment (N exp_07):** Prompt on frame 0, teleport the object (cut-paste + curated real cuts +
  paste-without-teleport placebo), measure whether the mask follows appearance or location as a function of
  temporal sparsity; either outcome pre-registered as a finding (appearance-tracking vs location-prior).
  1 GPU-day core + bounded curation.
- **Stop/kill criteria:** KILL if the placebo-paste arm shows the probe measures paste artifacts rather than
  arbitration (probe invalid). KILL if a memory-design ablation prints a teleport-shaped probe before
  execution (fastest-moving niche in the 5 — scoop re-search at proposal freeze AND experiment freeze).
  No deflationary stop exists: both outcomes are findings by pre-registration.
- **Why it beat the other 15:** Binding inclusion — and the mandated kill attempt failed on the merits: FF
    70|  found no new fatal flaw with a citation (paste confound already controlled; off-manifold objection
  answered in Round 2 by the curated real-cut arm; the moving memory-design field is a freshness risk, not a
  flaw). Highest information-per-GPU-day in the 20 (N ROI #4, discounted only for review-pass history — it
  has now had two). Only surviving video-memory coverage after A-0026's arm narrowed.
- **Remaining risk:** The memory-design field is verifiably moving; a busy ablation table elsewhere could
  absorb the headline. Run it week one — it costs one GPU-day.

## 4. B-0194 — segmentation sycophancy under randomized prompt dose (+B-0169 negative-click arm; one interactive-behavior program) (interactive/safety seat)

- **Mutated one-liner:** Under randomized prompt dose, SAM-family confidence grows while accuracy stagnates
  (sycophancy), and negative clicks turn anti-monotone beyond k across the whole click-policy envelope.
    80|- **Killer experiment (O battle-locked design; no N protocol exists):** Randomized-dose protocol —
  difficulty-stratified images, dose 1–10 assigned randomly, ≥4 click policies including RClicks'
  human-derived model, ≥4 model families; factorial positive × negative click sweep; effects must hold
  within difficulty strata and across the policy envelope (~2 GPU-weeks). Scope note adopted in Round 4:
  claims are pre-registered as scoped to the tested policy envelope (natural-image click distributions);
  medical click behavior explicitly out of scope.
- **Stop/kill criteria:** KILL (pre-registered tripwire) if click-policy variance dominates dose effects
  within strata — both readouts are then declared artifacts of policy choice and the program stops.
  SCOPE-STOP to a single-policy note if the anti-monotone negative-click effect holds under some policies
  but not across the envelope. No scoop clock beyond normal re-search: the SAM-UQ literature cites the
    90|  phenomenon but does not own the randomized dose-response law.
- **Why it beat the other 15:** Won the medical/safety/interactive slot 6–1–1 over A-0331 and A-0061:
  A-0331's "pursue first or drop" (J) cannot be honored inside a 5 whose execute-first budget is spent on
  C-0306/A-0028/C-0338 — seating it would be scheduling perjury; A-0061 would have spent the audit-genre
  token on the weakest headline of the trio and forced pre-agreed-lame-duck C-0057 into the eval slot.
  B-0194 is battle-ready (O's #3), covers safety AND interactive at once, and its tripwire is the
  best-formed stop criterion in the 20.
- **Remaining risk:** The RClicks-hostage scenario (policy variance dominating) kills both headlines at
  once; payoff bucket is M-H, the lowest ceiling in this 5.

   100|## 5. C-0338 — the size-resolved human ceiling (+C-0007 arm) (eval-audit seat; the one {A-0061, A-0206, C-0338} token)

- **Mutated one-liner:** Below a per-size crossing point, AP-small progress is unfalsifiable — model-GT AP
  exceeds human-human agreement AP in the smallest bins.
- **Killer experiment (N exp_06) — this is the portfolio's silencing experiment:** 1-day census gate on the
  LVIS double annotations (size distribution of double-annotated instances), then per-size-bin human-human
  agreement AP vs model-GT AP with a PRE-REGISTERED crossing point (1–2 GPU-days). The figure does not argue
  with "AP-small progress is meaningful" — it makes the claim unstateable below the measured bin.
  Arms per O/I fold: C-0007/A-0164 tiny-object noise floor + jitter propagation; A-0071 consensus-referenced
  ceiling correction.
   110|- **Stop/kill criteria:** STOP at the census gate (before any annotation spend) if small-bin
  double-annotation coverage is too thin for usable CIs — triggers either the contingent small-strata
  labeling N priced, or the seat stops and C-0057 (named first alternate, 8–0) takes the slot.
  DEMOTE the headline to a bounded claim if the crossing point sits below deployed size bins — this outcome
  also triggers A-0206's named re-entry claim in any later re-cut. KILL if the annotation-noise-race
  adjacency (Label Convergence / Noise-Aware Evaluation line) prints a size-stratified ceiling first
  (⏰ — wedges decay in months; scoop re-search at proposal freeze).
- **Why it beat the other 15:** Won the eval slot 7–1 over A-0206 and 7–1 over C-0057 (Round 3 Part C):
  vs C-0057 — higher payoff (H vs M-H), one-figure decisiveness vs slope-table risk, and C-0057 carries a
  pre-signed eviction notice (B-0286 desk-pilot trigger from O's round 2); vs A-0206 — its null is
   120|  field-moving ("the ceiling does not bind — AP-small progress is real") where A-0206's null demotes the
  flagship to a genre-retirement note, and its gate costs one day where A-0206's costs a corpus the group
  cannot commission from inside a seat list. N ROI #2; cheapest H-payoff item in the 20.
- **Remaining risk:** Crossing point below deployed size bins mutes the headline (knowable at the census
  gate); annotation-noise race adjacency is the liveliest scoop front among the five.

---

## Named alternates and triggers (binding on the 5→3 stage)

1. **C-0057** is first alternate for the eval slot (8–0) if C-0338 stops at the census gate and A-0206's
   130|   corpus remains unfunded.
2. **A-0206** holds a named re-entry claim if C-0338's census gate returns a muted headline; independently,
   the PI should decide the corpus-commissioning question this quarter on its own merits — the Top-5 list
   must not be the only channel for calendar-critical spend decisions (unanimous, Round 3 Part C).
3. **exp_02 before exp_01** (B-0001 dissociation before the full 4-arm commitment) is a binding ordering
   condition on seat 2.
