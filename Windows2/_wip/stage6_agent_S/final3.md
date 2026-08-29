# Final 3 — Stage-6 Close (Agent S, Top 5 → Final 3)

These three receive full Stage-7 packages (28 sections, written by the next agents — not here).
Battle-locked forms from Q's `top5.md` are what advance; arms and ordering conditions are binding on the
packagers. Ranked 1–3 by the Round-6 votes (`battle.md` Part D).

---

## #1 — C-0306: conformal coverage vs NMS (constructive/method seat) — seated 8–0, ranked #1 8–0

**Mutated claim (battle-locked):** Conformal coverage guarantees are destroyed by NMS, and a
coverage-preserving suppression rule restores them at competitive set size.

**Why it beat the other two:** It is the reason the other two are allowed to exist — the binding requires
the constructive method, and the fresh 2025–2026 scoop search *strengthened* the seat instead of killing
it: SeqCRC (arXiv:2505.24038) still treats NMS "as part of the OD model itself"; the newest conformal-OD
paper (arXiv:2605.07549, 2026) never mentions NMS at all; the learned-NMS line (arXiv:2606.03568)
optimizes mAP with no coverage guarantee. The field is publishing quarterly around the exact hole this
project fills, which simultaneously confirms the wedge and the urgency. Both upstream pipelines ranked it
#1 independently (N ROI #1, O battle-ready #1); it is unanimous across three consecutive battles; and its
fatal risk costs 2–4 GPU-days of analysis to resolve — the cheapest decisive gate in the portfolio.

**Killer experiment (N exp_05):** Gate first — cache pre-NMS candidate sets from 5–8 detectors
(anchor-based / anchor-free / DETR-family) on COCO val + LVIS + one dense-crowd benchmark; measure the
blind-spot rate: the fraction of GT objects whose *only* covering candidates NMS suppresses, stratified by
detector × NMS-IoU threshold × score threshold × crowdedness (2–4 GPU-days, analysis-only). If material,
build the coverage-preserving suppression module (greedy suppression that never removes the last
calibrated-set representative of a spatial cluster, with a provable candidate-set coverage bound) and
benchmark on the risk/set-size frontier vs SeqCRC-post-NMS, WACV-2024 no-NMS IoU-aware calibration,
soft-NMS, and DETR-family no-suppression controls.

**First-week plan:**
- Days 1–2: candidate-cache harvester (post-processing disabled) validated on two detectors + COCO val;
  score-floor pruning to control the 200–500 GB cache.
- Days 3–4: extend to the full detector zoo, LVIS, and the crowd benchmark; conformal layer (split
  calibration on pre-suppression candidate sets) stood up on cached data.
- Day 5: first blind-spot table across the threshold sweep and crowdedness strata; log the freshness
  re-search at proposal freeze (2605.07549 and 2606.03568 join the mandatory citation set).
- Gate verdict target: end of week 2. Method leg is built ONLY if the gate opens.

**Remaining risk:** The blind spot may be material only in crowded strata (→ pre-registered SCOPE-STOP to
a crowded-scenes method) or immaterial everywhere (→ ship the measurement as a short note; the constructive
quota crisis goes to the PI with B-0194 as named replacement seat — see `why_not_the_other_two.md`). The
scoop clock is real and confirmed hot: per-quarter re-search is mandatory and the seat converts to a kill
if execution has not started within the quarter.

**Paper title seeds:**
1. "Suppressed but True: Non-Maximum Suppression Silently Destroys Conformal Coverage in Object Detection"
2. "Coverage-Preserving Suppression: Reconciling NMS with Distribution-Free Guarantees"
3. "The NMS Blind Spot: Measuring — and Repairing — What Suppression Costs Conformal Object Detection"

---

## #2 — A-0028: SAM2/SAM3 teleport probe (SAM/video capability seat) — seated 8–0, ranked #2 6–2

**Mutated claim (battle-locked, citation set updated this session):** The distractor-fix papers (DAM4SAM
arXiv:2509.13864; SAMURAI arXiv:2411.11922; SAM2/SAM3 memory-design line arXiv:2512.22624) presuppose an
appearance-vs-location arbitration nobody has measured — teleport probes measure it directly on SAM2 AND
SAM3.

**Why it beat the other two:** It is the portfolio's certainty anchor. Four kill attempts across three
battles have now failed — this round's SAMURAI attack ("SAM 2 tends to prioritize appearance similarity")
dissolved on inspection into a third fix-paper presupposing the unmeasured arbitration, i.e., more
motivation, not a flaw. Either outcome is pre-registered as a finding (monotone location-prior law vs
appearance-dominance corrective), the placebo-paste arm controls the probe's own validity, and the core
costs one GPU-day. Highest information-per-GPU-day in the surviving set. At package time, a near-certain
finding with a week-one result outranks a gated H-ceiling bet — that is the 6–2 ranking vote.

**Killer experiment (N exp_07):** Prompt SAM2-L on frame 0; synthetic swap battery across the
(displacement d, temporal gap g, distractor similarity) grid — cut-paste with Poisson blending, plus
paste-without-teleport placebo; at the swap frame score mask IoU against object-at-old-location vs
object-at-new-location → per-trial trichotomy (follow-object / follow-place / neither); fit
P(follow-place) as a psychometric function of (d, g, similarity). 1 GPU-day core; full study (SAM2 sizes +
SAM3 + DAM4SAM as fixed-memory comparator + ~100 curated natural hard-cut clips) 3–5 GPU-days.

**First-week plan (binding — the killer core runs in week one, no exceptions):**
- Days 1–3: stimulus generator over the (d, g, similarity) grid + placebo-paste arm; scoring harness
  (trichotomy + psychometric fit) on a smoke batch.
- Day 4: SAM2-L killer battery (~10⁴ short clips, one GPU-day).
- Day 5: first arbitration curves with CIs; natural-cut curation starts in parallel; scoop re-search
  logged at experiment freeze (mandatory — fastest-moving niche of the three).
- Package note for Stage-7: the package must be written to absorb an already-completed killer result and
  carry the multi-model extension (SAM3 generational comparison, DAM4SAM-as-instrument) as its body.

**Remaining risk:** Absorb-risk is climbing — three fix-papers now touch the phenomenon, and a busy
ablation table elsewhere could print a teleport-shaped row (kill criterion if it happens before
execution; the week-one run is the mitigation). Synthetic-cut → natural-cut external validity is the
scientific risk; the pivot (re-scope to natural-cut-only with a smaller grid) is pre-registered.

**Paper title seeds:**
1. "Teleport: Does SAM2 Memory Follow the Object or the Place?"
2. "An Arbitration Law for Video Memory: Appearance versus Location in SAM2 and SAM3"
3. "Measuring What the Distractor-Memory Fixes Presuppose: A Psychophysics Probe for Segmentation Trackers"

---

## #3 — B-0114: VPT-as-registers, 4-arm dense-task form (+B-0001 artifact-map arm) — seated 5–2–1, ranked #3

**Mutated claim (battle-locked):** VPT's dense-task gains are partly register function — token arms
dissociate register absorption from added capacity, and the norm-map arm tests artifact maps as free
uncertainty.

**Why it beat the other two (B-0194 and C-0338, the seat-3 losers):** Three arguments carried the 5–2–1
vote. (i) **Perishability:** B-0114 is the only candidate with a now-or-never clock — the register-free
backbone population decays every quarter, while B-0194's niche is verifiably slow (nobody owns the
randomized dose-response law) and keeps on the bench intact. When bets are close, seat the one that
expires. (ii) **Decorrelation:** with A-0028 protected, seating B-0194 would make two of three packages
SAM-family behavioral probes — same relevance risk, same reviewer pool; B-0114 gives the Top-3 three
communities (detection/UQ, video memory, PEFT/mechanism) with zero shared infrastructure. (iii) **Ceiling
with a gate:** it is the highest-ceiling mechanism bet alive (H vs B-0194's M-H), it doubles as the
portfolio's only second constructive shot (the arm-(c) ≥50% branch converts to a training-free VPT
substitute — a retrofit recipe), and its main risk is bounded by its own binding ordering condition:
exp_02 runs before the 24-run grid is committed. Against C-0338 the argument was package scarcity, not
merit: a ≈2-GPU-day audit doesn't need 28 sections — its census gate runs off-portfolio in week one
regardless (adopted 8–0), with its full trigger lattice preserved.

**Killer experiment (N exp_01, gated by exp_02 — ordering is BINDING):** H's 4-arm × 2-backbone grid on
ADE20K: full VPT vs frozen-random tokens vs attention-bias-only vs no-token, on DINOv2 vs
DINOv2-with-registers, 3 seeds (24 runs, 1–1.5 GPU-weeks), with NOP/broadcast diagnostics
(arXiv:2606.08105) as readout axes, a pre-registered interpretation table, the gain-decomposition readout
(learned = a−max(b,c); register/bias = c−d; insertion = b−d), and the H2 directional test
(gain on register-free > gain on register-equipped). B-0001 arm: stratified AUROC of the register-norm map
vs entropy / distance-to-boundary / edge-density baselines — decided by exp_02 (~1 GPU-week) BEFORE the
grid is funded.

**First-week plan:**
- Days 1–2: launch N's exp_02 (register-norm UQ audit) — the binding ordering condition; it is the
  dissociation/merge decision for the register micro-field and the B-0001 arm's live-or-die test.
- Days 1–5 in parallel: token-injection wrapper + attention-bias module (test-time-registers construction,
  arXiv:2506.08010); verify the classification control reproduces Prompt-Fixed ≈ Linear (VPT Fig. 11) on a
  small run — the built-in implementation-bug detector.
- Commit the 24-run killer grid only after exp_02 returns; if the norm-map fails cheap baselines
  within-foreground on register-free models, drop the B-0001 arm without ceremony and proceed as a pure
  mechanism paper.

**Remaining risk:** The mush branch — a 4-arm table landing outside the pre-registered interpretation
table degrades the seat to the mechanism half of a merged exp_02 note (crisp kill criterion: arms b and c
each <5% of VPT's dense gain AND H2 gap < 2× seed sd). The obsolescence clock is why the seat must start
this quarter. The softmax-denominator confound is bounded by the token-count sweep, not eliminated —
a known Reviewer-2 leftover the package must answer in print.

**Paper title seeds:**
1. "Prompts as Registers: Dissociating Register Function from Learned Content in Visual Prompt Tuning"
2. "What Do Prompt Tokens Actually Do on Dense Tasks? A Four-Arm, Two-Backbone Dissociation"
3. "Free Registers: Attention-Bias Injection as a Training-Free Substitute for VPT on Dense Prediction"

---

## Portfolio shape (for the Stage-7 packagers)

- **Genres:** constructive method + capability instrument + mechanism dissociation. Zero audit-genre
  seats — the "complaint paper" AC-risk named in the PI lean is structurally closed.
- **Communities:** detection/UQ, video memory, PEFT/backbones — no shared infrastructure, uncorrelated
  failure modes, three distinct reviewer pools.
- **Budget:** all three killer experiments start within two weeks on group compute; total to full
  resolution ≈ 3–4 GPU-weeks plus exp_02's 1 GPU-week gate.
- **Week-one co-schedule (nothing waits on anything):** C-0306 cache harvest → gate table; A-0028 killer
  battery (day 4); B-0114's exp_02 launch; PLUS the off-portfolio C-0338 census gate (1 CPU-day, adopted
  8–0 — the figure is not declined, the package is).
- **Clocks:** C-0306 per-quarter scoop re-search, seat converts to kill if execution slips the quarter;
  A-0028 re-search at experiment freeze; B-0114 must start this quarter (obsolescence).
