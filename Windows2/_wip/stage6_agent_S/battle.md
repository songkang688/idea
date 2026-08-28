# Stage-6 Battle, Rounds 5–6 (Agent S) — Top 5 → Final 3

Agent S (Stage-6 final cut; **picks the final 3; does NOT write the 28-section Stage-7 packages**).
Date: 2026-08-28. Input: Agent Q's `top5.md` (battle-locked forms are what fight; arms are binding).
O ran rounds 1–2, Q ran rounds 3–4; these are **rounds 5–6** of the same battle.
Voices unchanged: Skeptical PI (SP), Engineer (ENG), Reviewer #2 (R2), Segmentation expert (SEG),
Foundation-model expert (FM), Medical (MED), Fatal-flaw hunter (FF), Hidden-upside advocate (HU).

## Entering constraints (binding, read into the record)

1. **C-0306 stays** unless a NEW fatal scoop is found (mandated fresh search: 2025–2026 conformal OD + NMS).
2. **A-0028 stays** unless a new fatal flaw with URL is produced.
3. Exclusion pairs still apply (B-0114 × B-0001 one seat with arm; A-0061 × A-0206; trio cap on
   {A-0061, A-0206, C-0338}).
4. The 3 must NOT be three audits and MUST include C-0306's constructive method.
5. Medical-zero is a standing dissent. C-0338 OR B-0194 may be replaced by a medical idea from M's top50 /
   Q's alternates (A-0074 volume CI, A-0331 Dice starvation) ONLY IF that idea has a **cheaper silencing
   experiment** AND does not violate audit caps.
6. PI lean (recorded as lean, not command): C-0306, A-0028, one of {B-0114, B-0194}. C-0338 noted as best
   eval leftover with "complaint paper" AC-risk if paired with another audit.
7. Stage-7 prototype directories (`stage7_proto_C0306`, `stage7_proto_A0028`) do **not exist on the
   branch** — checked this session. No prototype evidence enters the record.

---

## Round 5 — evidence into the record, protected seats re-attacked, medical motions heard

### Part A — the mandated C-0306 scoop search (fresh, this session)

**FF (reporting the hunt):** Live search, 2025–2026 conformal OD + NMS. Four findings, none a scoop:

- **SeqCRC** (arXiv:2505.24038, "Conformal Object Detection by Sequential Risk Control") — the paper's own
  text: NMS "is considered as part of the OD model itself." It calibrates **after** suppression, on the
  post-NMS list. It neither measures the coverage NMS destroys nor modifies suppression. It remains the
  baseline N's exp_05 already names, not a scoop.
- **arXiv:2605.07549** ("Probabilistic Object Detection with Conformal Prediction", 2026) — the newest
  conformal-OD entry; conformalizes detector heads (coordinate-wise CP, Bonferroni, aleatoric scaling).
  Grepped the full text: **zero mentions of NMS**. Confirms K's "third conformal-OD paper within months"
  prediction landed — and it landed on a different square.
- **arXiv:2606.03568** ("Learned Non-Maximum Suppression for 3D Object Detection", 2026) — learned
  suppression optimizing mAP/NDS; it even cites NMS suppressing valid detections in crowds as motivation,
  but carries **no coverage guarantee and no conformal layer**. Adjacent evidence that the blind spot is
  real; not a coverage-preserving suppression rule.
- **arXiv:2505.16740** (conformal runway detection) and the railway-signals CP paper — applications of
  conformal-after-NMS; nothing structural.

**FF verdict:** No coverage-preserving suppression rule has printed; nobody has quantified the blind spot.
The wedge is intact and the clock is confirmed hot (2605.07549 proves the field is publishing quarterly).
**SP:** Binding condition 1 resolves: **C-0306 stays.** **R2:** One sharpening for the packager —
2605.07549 must join the mandatory citation set; its silence on NMS is itself the motivating sentence of
the intro. **Seat confirmed 8–0 (third consecutive unanimous).**

### Part B — A-0028: the fourth kill attempt

**FF:** Fresh search. One genuinely new adjacent item: **SAMURAI** (arXiv:2411.11922) states in print that
"SAM 2 tends to prioritize appearance similarity over spatial and temporal consistency" in crowded scenes.
If that sentence were a measurement, the probe's headline is half-claimed. Attack lodged.

**FM (response):** Read SAMURAI's evidence base: the claim is an *anecdotal characterization of failure
patterns* (their Fig. 1: two qualitative failure cases) motivating a motion-prior bolt-on. There is no
controlled dissociation, no displacement/gap/similarity grid, no arbitration curve, no placebo arm — and
the claim is about distractor confusion in crowds, not about the appearance-vs-location arbitration law
under temporal sparsity. It is a THIRD fix-paper presupposing the arbitration nobody measured — it
strengthens exp_07's framing ("the fix papers presuppose what nobody measured") and joins DAM4SAM
(arXiv:2509.13864) and the memory-design study (arXiv:2512.22624) in the related-work armor.

**R2:** Concur, with a cost: three fix-papers presupposing the arbitration means the absorb-risk (a busy
ablation table elsewhere prints a teleport-shaped row) is climbing every quarter. The 1-GPU-day core is
only cheap if it actually runs. **ENG:** Adopted as a binding schedule note: killer battery in week one,
no exceptions — it was already Q's condition; it is now load-bearing.

**FF verdict:** SAMURAI is a citation obligation, not a fatal flaw. **No new fatal flaw + URL exists.
The kill fails — fourth attempt.** **Seat confirmed 8–0**, condition attached: SAMURAI enters the
mandatory citation set; week-one execution is binding.

### Part C — the medical motions (binding condition 5 tested on the merits)

**MED (moving):** Two motions, taken separately, per the binding's explicit invitation.

**Motion 1: replace C-0338 with A-0074 (volume-CI coverage audit).**
**MED:** Clinically consequential, checkable, and the conformal-segmentation line answered the method
question without ever auditing deployed practice. **FF (against, on the binding's own test):** The
binding requires a *cheaper silencing experiment*. A-0074's killer experiment is a mandatory
deployed-pipeline survey — calendar-bound, human-subjects-of-a-sort, weeks — followed by a synthetic-GT
coverage audit. C-0338's silencing experiment is a 1-day census gate plus 1–2 GPU-days. A-0074 is
**strictly more expensive** on the axis the binding names. **R2:** And it fails the second test too:
A-0074 is an audit ("your deployed CIs are invalid") — swapping audit-for-audit does not reduce audit-cap
exposure; it trades the portfolio's best silencing experiment for a survey. **Vote: fails 1–7 (MED alone).**

**Motion 2: replace B-0194 with A-0331 (Dice gradient starvation, instrumented).**
**MED:** Instrument-level science on the loss the entire medical field uses; the CC-DiceCE line is closing
the niche; this is the last cycle the window is open. **ENG (against, on the binding's own test):**
A-0331's silencing experiment is instrumented training on two multi-lesion datasets, ~2 GPU-weeks —
**not cheaper** than B-0194's ~2 GPU-weeks; the binding's condition fails on arithmetic. **R2:** And the
Round-3 scheduling-perjury argument is *worse* at 3 seats than at 5: J's verdict is "pursue first or
drop," and this portfolio's execute-first budget is already committed to C-0306 (hottest clock, must
start within the quarter) and A-0028 (week one, binding). A-0331 in the 3 would execute third — that is
"drop" wearing a seat. **Vote: fails 1–7 (MED alone).**

**MED (closing, dissent for the record — third consecutive battle):** Both motions failed on conditions
the PI wrote, so I lose on the merits and say so. The consequence stands regardless: **zero medical
projects receive Stage-7 packages this cycle**; A-0331's window closes by calendar, not refutation. The
off-portfolio recommendation (Q's ledger: A-0331 instrumentation ~2 GPU-weeks if spare compute exists)
is re-affirmed 8–0 — but an off-portfolio recommendation is not a package, and the PI co-signs that gap
by accepting this cut. **Dissent standing.**

### Round 5 close

C-0306 and A-0028 hold their seats on the merits (not only by binding). Both medical swaps fail the
binding's own tests. The final seat is a three-way fight: **B-0114 vs B-0194 vs C-0338.**

---

## Round 6 — the seat-3 fight, the ranking, the audit

### Part A — three cases, heard in full

**HU (for C-0338):** The cheapest H-payoff item in the entire pipeline: a 1-day census gate plus 1–2
GPU-days buys a one-figure claim that makes "AP-small progress is meaningful" *unstateable* below the
measured bin. N ROI #2. Its null is field-moving in the other direction. Evicting the best silencing
experiment from the package list to fund a 1.5-GPU-week mechanism study is buying ceiling with certainty.

**SEG + MED (for B-0194):** The best-engineered protocol in the surviving set — randomization kills
selection bias structurally, the RClicks-hostage tripwire is the best stop criterion on the board, and it
is the ONLY candidate covering safety AND interactive behavior. Cut it and the Top-3 covers neither.
Two headlines in one ~2-GPU-week run. O's battle-ready #3.

**FM + ENG (for B-0114):** The highest-ceiling mechanism bet left alive (H): it rewrites the mechanism
story of the most-used PEFT method on dense tasks, and its arm (c) branch doubles as a training-free
constructive recipe (attention-bias injection as a VPT substitute) — the portfolio's only *second*
constructive shot if C-0306's gate disappoints. Execution-grade today, no external dependency, and it
arrives with its own decision gate: exp_02 (~1 GPU-week) runs before the 24-run grid is committed — the
binding ordering condition makes the seat self-de-risking. And it is the only candidate with a
**now-or-never clock**: the register-free backbone population decays every quarter.

### Part B — the arguments that decided it

**R2 (the package-scarcity argument, against C-0338):** A Stage-7 package is 28 sections of program
infrastructure. C-0338's entire resolution costs ≈2 GPU-days. **A project that resolves for the price of
a long weekend does not need a package to happen — it needs a calendar slot.** Adopt what Q already
recommended: the census gate runs off-portfolio in week one regardless of seating (1 CPU-day). If the
crossing-point fires, the PI re-opens with a measured branch in hand and C-0338's full trigger lattice
(C-0057 first alternate 8–0; A-0206 re-entry claim) is preserved on the record. Seating it would spend
the scarcest resource on the least package-hungry item. **SP:** Also the AC-risk accounting: with C-0338
out, the Top-3 carries **zero audit-genre seats** — C-0306's headline already opens with "NMS destroys
coverage" and the safest way to keep that reading constructive rather than adversarial is to make its
neighbors a capability instrument and a mechanism dissociation, not a second complaint.

**FM (the correlation argument, against B-0194):** With A-0028 protected, seating B-0194 makes **two of
three packages SAM-family behavioral probes** — two seats exposed to the same relevance risk (SAM-family
attention cooling), the same reviewer pool, and partially the same rebuttal ("probing a model you didn't
train"). C-0306 + A-0028 + B-0114 spans three communities (detection/UQ, video memory, PEFT/backbone
mechanism) with zero shared infrastructure and uncorrelated failure modes. At 3 seats, decorrelation is
worth more than at 5.

**ENG (the perishability argument, B-0114 over B-0194):** B-0194's niche is verifiably slow — Q's record:
"the SAM-UQ literature cites the phenomenon but does not own the randomized dose-response law"; no scoop
clock beyond routine re-search. B-0114's window is verifiably closing — register-equipped backbones become
default; both H and L flagged it; Q's record: "seat it NOW or never." **When two bets are close, seat the
one that expires.** B-0194 survives a quarter on the bench intact; B-0114 does not.

**FF (hostile pass on B-0114 before it wins anything):** The mush branch is real: if the 4-arm table lands
in an uninterpretable cell, the H-payoff seat degrades to the mechanism half of a merged exp_02 note.
**R2 (answer):** The kill criterion is crisp and pre-registered (arms b and c each <5% of VPT's dense gain
AND H2 gap < 2× seed sd → honest death), the classification control is a built-in bug detector, and the
2-backbone axis makes even partial results directional. The risk is priced, bounded, and — decisive here —
**gated**: exp_02 fires before the grid is funded. **Attack holds no new ground.**

**HU (last word for C-0338):** Then let the record say it plainly: the group is declining a package for
the portfolio's cheapest H-payoff figure, and if the census gate fires material the PI will wish the
package existed. **SP:** Noted verbatim, and the off-portfolio week-one census run is adopted **8–0** —
the figure is not being declined; the *package* is.

### Part C — the vote on seat 3

| Candidate | Votes |
|---|---|
| **B-0114** (4-arm, +B-0001 arm, exp_02-gated) | **5 — SP, ENG, R2, FM, FF** |
| B-0194 (+B-0169) | 2 — SEG, MED |
| C-0338 (+C-0007 arm) | 1 — HU |

**B-0114 takes seat 3, 5–2–1.** Dissents standing: SEG/MED (safety-and-interactive coverage falls to zero
in the Top-3; B-0194 remains battle-ready and unscooped); HU (cheapest-H figure has no package owner;
census gate adopted off-portfolio as partial remedy).

### Part D — ranking the 3

**#1 C-0306 — 8–0.** Constructive requirement, both pipelines' independent #1 (N ROI #1, O battle-ready
#1), hottest clock (2605.07549 confirms the field prints quarterly), unanimous in every round it has ever
fought (three battles running).

**#2 — A-0028 vs B-0114.** **FM/HU (for B-0114 at #2):** rank by ceiling; H beats M-H. **R2/ENG (for
A-0028 at #2):** rank by certainty-per-package: four failed kill attempts across three battles, either
outcome pre-registered as a finding, 1-GPU-day core already scheduled for week one, and the freshest
evidence (SAMURAI) *increased* its motivation. B-0114's H ceiling carries the portfolio's widest
deflationary branch and its package cannot even commit its main grid until exp_02 returns. A completed,
certain finding outranks a gated bet at package time. **Vote: A-0028 #2, 6–2 (FM, HU for B-0114).**
**B-0114 is #3.**

### Part E — constraint audit of the final 3

| Constraint | Status |
|---|---|
| Exactly 3 | C-0306 · A-0028 · B-0114(+B-0001 arm) ✓ |
| C-0306 kept (no new fatal scoop) | Fresh 2025–2026 search: SeqCRC calibrates post-NMS; 2605.07549 never mentions NMS; no coverage-preserving suppression printed ✓ |
| A-0028 kept (no new fatal flaw + URL) | SAMURAI = citation obligation, not flaw; fourth kill attempt failed ✓ |
| B-0114 × B-0001 | One seat; B-0001 is a named arm; exp_02 runs before the 4-arm grid (binding ordering) ✓ |
| A-0061 × A-0206 | Neither in the 3 ✓ |
| Trio cap {A-0061, A-0206, C-0338} | Zero seated ✓ |
| Not three audits | Zero audit-genre seats (method + capability instrument + mechanism dissociation) ✓ |
| C-0306 constructive method included | Yes, seat #1 ✓ |
| Medical swap conditions | Both motions heard and failed on the binding's own tests (neither alternate has a cheaper silencing experiment; A-0074 is audit-for-audit) ✓ |
| Battle-locked forms only | All three carry Q's top5.md forms verbatim ✓ |

### Part F — belief-update ledger (rounds 5–6)

- **FF** on A-0028: lodged the SAMURAI attack in good faith, withdrew it on reading the evidence base —
  moved from "possible half-claim" to "third presupposing fix-paper; cite it." Fourth kill attempt, fourth
  failure, on the record.
- **R2** on C-0338: moved from "best eval leftover" to "package-scarcity argument" — a ≈2-GPU-day project
  needs a calendar slot, not 28 sections. Authored the off-portfolio census adoption (8–0).
- **MED**: no movement — lost both motions on the binding's own conditions and said so; medical-zero
  dissent carried out for the third consecutive battle, now attached to the *package* list, which is the
  strongest form it has taken.
- **SEG**: moved from C-0057 advocacy (spent, rounds 3–4) to B-0194 advocacy; loses; carries the
  coverage-hole dissent (no safety/interactive package) and wins B-0194's named-first-replacement status.
- **HU**: no movement on C-0338's value; banked the unanimous off-portfolio census run and the preserved
  trigger lattice instead of the seat.
- **Nobody moved** on: C-0306 (unanimous three battles running), B-0114 vs B-0194 head-to-head (the
  perishability + decorrelation arguments were not answered by the losing side).

**Standing dissents carried out:** MED (zero medical packages — PI co-signs by accepting the cut);
SEG (zero safety/interactive coverage in the 3; B-0194 named first replacement); HU (cheapest-H figure
unowned by any package; census gate runs anyway). No fake consensus: three of eight voices leave with
something on the record.
