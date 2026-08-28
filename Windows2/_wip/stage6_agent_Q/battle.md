# Stage-6 Battle, Rounds 3–4 (Agent Q) — Top 20 → Top 5

Agent Q (Stage-6 continuation; **not the PI — no final-3 picked, no full research packages written**).
Date: 2026-08-28. Input: Agent O's `top20.md` (battle-locked forms are what fight here, not Stage-1 claims).
O's rounds 1–2 are the record of how the 20 were seated; these are rounds 3–4 of the same battle.
Voices unchanged: Skeptical PI (SP), Engineer (ENG), Reviewer #2 (R2), Segmentation expert (SEG),
Foundation-model expert (FM), Medical (MED), Fatal-flaw hunter (FF), Hidden-upside advocate (HU).

## Entering constraints (binding, read into the record)

    10|1. B-0114 and B-0001 cannot both be full seats — B-0001 stays a named arm of B-0114 (already O's topology).
2. A-0061 and A-0206 cannot both be in the 5.
3. At most ONE of {A-0061, A-0206, C-0338} in the 5 (audit-genre cap), absent an explicit boxed override for C-0338.
4. The 5 MUST include a constructive/method package; C-0306 is the default.
5. A-0028 is included unless killed with a NEW fatal flaw + citation.
6. Diversity target: method + SAM/video + PEFT/registers + one medical/safety-or-interactive + one eval audit
   with a silencing experiment. Not five eval audits.
7. The named disputed set — **C-0338 vs C-0057 vs A-0061 vs A-0206 vs B-0194** — is where O's battle-ready five
   and N's ROI five disagree. That set decides seats 4 and 5.

    20|## Note on Agent M's top50 (landed after O's battle; O's Top20 is the input)

`stage3_agent_M/top50.md` now exists on the branch (it did not when O and N ran). Checked for conflicts:
all 20 of O's seats appear in M's 50 in compatible battle-locked forms. Two real discrepancies, neither
touching the Top-5 fight: (a) the detection rigor program is hosted by **C-0311-flagship** in O but by
**C-0136+0287+0302 with C-0311 cut** in M — a host-naming conflict the Stage-7 packager must reconcile if
that program ever advances (it does not advance here); (b) M enforces GT-epistemology ≤ 2 (C-0338, C-0057)
and files A-0163 under annotation metrology, while O carries three GT-epistemology seats as one declared
program bet. At Top-5 granularity at most one GT-epistemology seat survives anyway, so both accountings are
satisfied by this cut. No seat of O's 20 is contradicted by M in a way that changes the input.
    30|
---

## Round 3 — from 20 to a provisional 5

### Part A — the three near-fixed seats earn their passes (no free rides)

**Fight 1: C-0306 (conformal coverage vs NMS) — constructive default, re-attacked anyway.**
**FF:** The gate can return "the fraction of GT objects whose only covering candidates NMS suppresses is
immaterial" — then there is no method, only a negative note, and the constructive quota is unfilled.
**R2:** And K expects a third conformal-OD paper within months; if it prints coverage-preserving suppression
    40|first, the seat converts to a citation. **ENG:** Both risks are priced: the gate is 2–4 GPU-days,
analysis-only, and N's exp_05 has it specified to the threshold sweep — this is the cheapest way in the
entire 20 to find out whether the portfolio's method bet exists. A seat whose fatal risk costs four GPU-days
to resolve is exactly what a Top-5 slot is for. **SP:** Binding constraint 4 names it the default; nobody has
produced a competing constructive package that is battle-ready (A-0206's constructive branch needs the
corpus; B-0114's retrofit branch needs the 4-arm result first). **Seat holds, unanimous.** Condition carried
from O: per-quarter scoop re-search; execution must start within the quarter or the seat converts to a kill.

**Fight 2: A-0028 (teleport probe) — FF given the floor to hunt the new fatal flaw.**
**FF:** I attempted the kill as mandated. Candidate flaws: (i) paste-artifact confound — already neutralized
    50|by the placebo-paste arm (paste-without-teleport) in N's exp_07; (ii) "the memory-design line will print it
first" — DAM4SAM (arXiv:2509.13864) and the SAM2/SAM3 memory-design study (arXiv:2512.22624) document the
distractor phenomenon but N's fresh scoop-check confirmed **no controlled teleport dissociation probe
exists**; that is a freshness risk, not a flaw; (iii) "off-manifold toy" — answered in Round 2 by the curated
real-cut arm (R2 moved on the record). I have **no new fatal flaw and no new citation**. The kill fails.
**R2:** Concur — this battle was its second Reviewer-2 pass; the either-outcome pre-registration (appearance-
tracking vs location-prior are both findings) is the cleanest in the 20. **Seat holds.** ENG note: 1 GPU-day
core; schedule it inside the first week regardless of everything else in this document.

**Fight 3: the register/PEFT slot — B-0114 (4-arm, +B-0001 arm) vs B-0104.**
    60|**FM:** Two B-mechanism seats cannot both enter a 5; pick one. B-0104's premise is fragile in a specific,
dated way: ONE high-rank-plus-tuned-LR ablation closing the dense gap guts the family, and that ablation is
cheap for any PEFT group to run by accident. B-0114's mush risk, by contrast, is bounded by design — the
2-backbone axis makes even partial reproduction directional, and the interpretation table is pre-registered.
**HU (for B-0104):** The invariance-inheritance ceiling is the deeper claim; B-0114 is a mechanism
explanation of one method's gains. **ENG:** B-0114 is execution-grade today (H's grid, NOP/broadcast
diagnostics adopted, no external dependency) and N's exp_02 gives the register micro-field a 1-GPU-week
decision experiment that must run before the full 4-arm study is committed — the slot comes with its own
gate. B-0104 has no equivalent cheap gate; its killer experiment IS the expensive grid. **R2:** B-0114's
population (register-free backbones) shrinks every quarter — that is an argument for seating it NOW or
    70|never; B-0104 keeps. **Vote: B-0114 seats, 7–1 (HU against).** Condition attached: exp_02 runs first; if the
norm-map arm dies on register-free models, the B-0001 arm is dropped without ceremony and the 4-arm study
proceeds as a pure mechanism paper.

### Part B — the disputed set, part 1: the medical/safety/interactive slot

Candidates: **B-0194+B-0169** (interactive/safety program) vs **A-0331** (Dice gradient starvation) vs
**A-0061** (topology at checkpoint selection, gated).

**MED (opening, for A-0331 or A-0061):** This cut is about to do to medical what O's round 2 did to
medical-FM science: zero seats. A-0331 is instrument-level science on the loss the whole field uses; A-0061
    80|has the strongest either-outcome value in the medical pair and counts toward the quota in gated form (I
moved on that in Round 2 and stand by it).

**R2 (against A-0331):** J's verdict is literal: "pursue first or drop." Freshness-fragile means a Top-5
seat for A-0331 is a commitment to execute it FIRST — ahead of C-0306, whose clock the whole room just
agreed is the hottest. The 5 cannot carry two execute-first-or-die seats plus A-0028's week-one run and
C-0338's census gate. Seating A-0331 is scheduling perjury: we would be seating it to feel covered, knowing
it executes third at best, which is the same as dropping it — with a seat wasted.

**FF (against A-0061):** Three compounding problems. (i) The trio-cap arithmetic: A-0061 spends the one
    90|{A-0061, A-0206, C-0338} token on the seat with the WEAKEST headline of the three — its wedge is
quantification of a phenomenon whose existence 2601.06067 already demonstrated and is already prototyping
selection rules against. (ii) Spending the token here forces the eval slot to C-0057 — the seat O's own
round 2 pre-agreed is first-to-vacate (B-0286 desk-pilot trigger). The pair {A-0061, C-0057} is dominated by
the pair {B-0194, C-0338} on payoff (M-H+M-H vs M-H+H), on cost (2–3 GPU-weeks + inference vs ~2 GPU-weeks +
~2 GPU-days), and on coverage (loses safety/interactive entirely). (iii) The EMA null branch is
pre-registered as informative, but "informative null against a one-line fix" is a workshop paper if the
divergence is small — the H-payoff branch is conditional on modern schedules NOT having already fixed it.

**SEG (for B-0194):** The randomized-dose design is the best-engineered protocol in the 20 — randomization
   100|kills the selection-bias objection structurally, the RClicks-hostage tripwire is pre-registered (if policy
variance dominates, both readouts are declared artifacts and the program stops — that is what a stop
criterion is supposed to look like), and it is the ONLY seat in the 20 that covers interactive behavior AND
safety at once. Binding constraint 6 asks for exactly one of medical/safety-or-interactive: B-0194 satisfies
it with the strongest protocol; the medical candidates satisfy it with the weakest schedules.

**HU (probing):** Is B-0194's ceiling too low for a 5? M-H, not H. **FM:** Its ceiling is understated:
"SAM-family confidence grows while accuracy stagnates under randomized dose" is a safety headline with
cross-model generality (≥4 families), and sycophancy language travels — the interactive-segmentation
community and the FM-evaluation community both cite it. The anti-monotone negative-click law is a second
   110|headline in the same compute. **ENG:** ~2 weeks compute, fully specified, no prerequisite. Battle-ready.

**MED (closing, dissent forming):** I register that "the schedules don't fit" is this round's version of
"a weak seat is worse than an honest gap" — true, and it still leaves the portfolio answering every medical
question with nothing this cycle. If the 5 seats B-0194, I want it on the record that A-0331's window closes
by calendar, not by refutation, and that the PI co-signs a portfolio with zero medical seats going into the
5→3 fight.

**Vote on the slot: B-0194+B-0169 — 6 for (SP, ENG, R2, SEG, FM, HU) · 1 against (MED, for A-0061) ·
FF abstains** (wants the slot's genre-token spent nowhere, concurs with outcome). **B-0194+B-0169 seats.**
**MED dissent standing** (carried to the ledger and AGENT_REPORT).
   120|
### Part C — the disputed set, part 2: the eval-audit slot

Candidates: **C-0338** (size-resolved human ceiling) vs **C-0057** (missing-annotation tax) vs **A-0206**
(SAM fingerprint + inheritance). Trio cap: at most one of {C-0338, A-0206} can even be considered
(A-0061 already spent nothing — the token is free).

**C-0057 heard first.**
**SEG (for):** Cheapest seat on the board, inference-only, battle-ready — it is IN O's battle-ready five.
The differential (anti-quality) effect is unclaimed. **FF (against):** It is also the seat O's majority
pre-agreed to vacate first if B-0286's desk pilot returns positive — a Top-5 built on a seat with a
   130|pre-signed eviction notice hands the 5→3 fight a lame duck. And its fatal risk is the dullest in the 20:
no crossover → slope table. Against C-0338 for the same slot it loses on payoff (M-H vs H), on decisiveness
(slope table vs one-figure crossing point), and on clock (no ⏰ vs ⏰). **R2:** N did not even rank it — it
was not in the mandated ten. Its case is cheapness, and cheapness alone is how portfolios fill with slope
tables. **Vote: eliminate C-0057 from the slot, 7–1 (SEG against, accepts under protest).**

**A-0206 vs C-0338 — the real fight.**
**HU (for A-0206):** Highest flagship ceiling in the twenty. N's exp_04 note is explicit: the corpus is
calendar-bound, not GPU-bound, and commissioning starts at SELECTION — meaning a Top-5 seat is precisely the
mechanism by which the corpus gets funded and the data-genetics program stays alive. Cutting it here does
   140|not bench it, it kills the flagship for the cycle. The either-outcome argument that moved FF in Round 2
stands: fingerprint-is-dialect is still a publishable genre-retirement note.

**FF (for C-0338):** Round 2 moved me to "seat, corpus-first" — at Top-20 granularity. At Top-5 granularity
the same facts argue the other way. (i) The corpus is the costliest prerequisite in the 20 ($$); every other
seat in the provisional 5 starts its killer experiment within two weeks for ≤2 GPU-weeks; A-0206 alone
cannot start at all without a spend decision that belongs to the PI, not to a Top-5 list. (ii) The downside
branch is asymmetric in the wrong direction for a flagship: C-0338's null (no crossing) is itself a
field-moving figure ("human ceiling does not bind at deployed sizes — AP-small progress is real"), while
A-0206's null (fingerprint = dialect) demotes the flagship to a note. (iii) The trio-cap token should buy
   150|the highest headline-per-GPU-day in the trio: C-0338 is ¢/H with a 1-day census gate; A-0206 is $$/H with a
weeks-long calendar gate.

**FM:** Agree with FF, with one addition: C-0338's silencing experiment is the best in the portfolio — the
pre-registered per-size-bin crossing point (model-GT AP vs human-human agreement AP) doesn't argue with the
"AP-small progress is meaningful" default, it makes the default unstateable below the measured bin. That is
what binding constraint 6 means by "an eval with a silencing experiment."

**SEG:** C-0338's remaining risk is real — the crossing point may sit below deployed size bins, muting the
headline — but that outcome is knowable at the census gate (1 day, before any annotation spend). A-0206's
   160|equivalent gate costs a corpus.

**SP (procedural):** Is anyone moving to override the trio cap by arguing C-0338 is not audit-genre?
**R2:** No. C-0338 is exactly the genre — "your evaluation practice is unfalsifiable below X" is a
diagnosis-without-fix audit with a constructive boundary as a corollary. It takes the token; no boxed
override is claimed; the cap binds and is satisfied.

**Vote on the slot: C-0338 — 7 for · 1 against (HU, for A-0206).** **C-0338 seats. HU dissent standing**,
with a re-entry trigger the room accepts unanimously: if C-0338's census gate returns "crossing point below
deployed size bins" (headline muted), A-0206 is the named replacement in any subsequent re-cut, and the PI
   170|should decide the corpus-commissioning question on its own merits THIS QUARTER regardless of Top-5
membership — seating decisions must not be the only channel by which calendar-critical spends get decided.

### Round 3 close — provisional 5

**C-0306 · B-0114(4-arm, +B-0001 arm) · A-0028 · B-0194(+B-0169) · C-0338.**
Mix check: method (C-0306) + registers/PEFT (B-0114) + SAM/video (A-0028) + interactive/safety (B-0194) +
one eval audit with a silencing experiment (C-0338). One audit-genre token spent (C-0338). Zero medical
seats (MED dissent standing). Not five eval audits — audit count is 1 of 5 (C-0306 and B-0114 are
mechanism/method, A-0028 is capability science, B-0194 is behavioral safety science).

   180|---

## Round 4 — re-attacks on the provisional 5, renewed motions, final seating

### Part A — one hostile pass per seat, new attacker each

**R2 on the WHOLE 5 (portfolio-level attack):** This 5 has no $$ flagship. Every seat is ≤2 GPU-weeks. Where
is the career paper? **FM (response):** Three of five are H-payoff (C-0306, B-0114, C-0338) and the flagship
ceiling lives in the conditional branches: C-0306's coverage-preserving suppression rule is a method paper
with a formal-novelty moat if the gate opens; B-0114 rewrites the mechanism story of the most-used PEFT
method on dense tasks. The $$ flagships (A-0206 corpus, C-0311 replication ensemble) were cut precisely
   190|because a 5 heading into a 5→3 fight must be resolvable on the group's own budget this quarter. The answer
to "where is the career paper" is "wherever the gates say it is, four GPU-weeks from now" — that is the
design, not an accident. **R2 accepts with a reservation for the record:** if all five gates return their
deflationary branches, the portfolio ships five competent notes and no flagship; the PI should know the 5
trades ceiling for resolution speed.

**FF on C-0306:** Renewing with a sharper number: if the gate fraction is material only in crowded scenes
(COCO-crowd, not COCO), the method's market shrinks to a niche. **ENG:** The gate protocol already stratifies
by crowdedness (N's exp_05); a crowded-only result is a scoped method, not a dead one. **Holds.**

   200|**SEG on A-0028:** The curated real-cut arm needs cuts where an object genuinely relocates across a shot
boundary — curation cost is nonzero and the arm is load-bearing against the off-manifold objection.
**ENG:** Curation is bounded (dozens of clips suffice for the dissociation, not thousands); placebo-paste
arm carries the confound control; 1 GPU-day core stands. **Holds.**

**MED on B-0194 (adversarial by assignment):** If RClicks' clickability model fails to transfer to the
medical-imaging click distributions, the "whole click-policy envelope" claim quietly shrinks to natural
images — and the safety framing oversells. **FM:** The claim is scoped to the policy envelope actually
tested (≥4 policies, ≥4 model families); medical click behavior is out of scope by pre-registration, and
saying so in the limitations section is honest, not fatal. **Holds**, with MED's scope note adopted into
   210|the protocol text.

**HU on C-0338:** Renewing the muted-headline risk as an attack: if the LVIS double-annotation census shows
thin small-bin coverage, the human-human AP estimate has wide CIs exactly where the claim lives.
**SEG:** That is what the census gate is FOR — it runs in one day, before annotation spend, and a
thin-census result triggers the contingent small-strata labeling N priced, or stops the seat. Stop
criterion, not fatal risk. **Holds.**

**FF on B-0114:** The register-equipped-backbone population keeps growing; by the time the 4-arm grid
finishes, reviewers may ask why anyone still adapts register-free backbones. **R2:** The 2-backbone axis IS
   220|the answer — the paper's claim is about the mechanism dissociation, and register-equipped siblings are half
the design, not a threat to it. The obsolescence clock is real but priced (it is why the seat must start
this quarter). **Holds.**

### Part B — renewed motions (the honest losers get their second vote)

**MED moves: swap C-0338 → A-0061** (restores medical, keeps the trio cap satisfied — token moves from
C-0338 to A-0061). **Debate:** FF repeats the dominance argument (weakest headline of the trio takes the
token; C-0338's silencing experiment is lost; constraint-6 eval slot then unfilled by anything with H
payoff). SP adds: constraint 6's eval-with-silencing-experiment slot would be EMPTY — A-0061 is an audit
   230|but its experiment persuades, it does not silence; the swap fails the mix on its face.
**Vote: fails 1–7 (MED alone).** Dissent stands.

**HU moves: swap B-0194 → A-0206** (ceiling argument, corpus-commissioning-at-selection argument).
**Debate:** ENG repeats: the 5 must be executable this quarter; A-0206 cannot be. FM adds: the swap would
put TWO audit-genre trio members in the 5 (A-0206 + C-0338), violating the cap outright — the motion is
unconstitutional as drafted; HU would have to also drop C-0338, i.e., re-litigate Part C, which just closed
7–1. **Vote: fails 1–7 (HU alone).** Dissent stands; re-entry trigger from Round 3 Part C reaffirmed
unanimously (census-gate-muted → A-0206 named replacement; PI decides corpus this quarter regardless).

   240|**SEG moves (small): C-0057 named first alternate** for the eval slot should C-0338 stop at the census gate
AND A-0206's corpus remain unfunded. **Vote: passes 8–0** (alternate list, costs nothing, prevents a
re-litigated round later).

### Part C — constraint audit of the final 5

| Constraint | Status |
|---|---|
| Exactly 5 | C-0306, B-0114(+B-0001 arm), A-0028, B-0194(+B-0169), C-0338 ✓ |
| B-0114 × B-0001 | One seat; B-0001 is a named arm; exp_02 gates the merge decision ✓ |
| A-0061 × A-0206 both in 5 | Neither is in the 5 ✓ |
   250|| ≤1 of {A-0061, A-0206, C-0338} | Exactly one (C-0338); no override claimed; cap binds ✓ |
| Constructive/method package present | C-0306 (default honored) ✓ |
| A-0028 included | Yes; FF's mandated kill attempt failed for want of a new flaw + citation ✓ |
| Diversity mix | method + registers + SAM/video + interactive/safety + 1 eval-with-silencing ✓ |
| Not 5 eval audits | 1 audit-genre seat of 5 ✓ |
| Battle-locked forms only | All five carry O's top20.md forms verbatim; naive/original forms barred ✓ |

### Part D — belief-update ledger (rounds 3–4)

   260|- **FF** on A-0206: "seat, corpus-first" (Round 2) → "cut at Top-5 granularity, named re-entry trigger"
  (asymmetric-null + cannot-start-this-quarter arguments; the Round-2 either-outcome argument conceded as
  true but insufficient at 5-seat granularity).
- **R2** on the portfolio: "where is the career paper" → accepts resolution-speed design with a recorded
  reservation (all-deflationary-branches scenario).
- **SEG** on C-0057: "cheapest seat, battle-ready" → accepts elimination under protest; wins named-first-
  alternate status 8–0.
- **MED**: no movement — dissent on zero-medical-seats carried out of the battle intact (as in Round 2's
  B-0286 fight, this is a PI-level scope decision, not a resolvable disagreement).
- **HU**: no movement on A-0206's value; movement on mechanism — accepts that seating decisions must not be
   270|  the corpus-funding channel, and banks the unanimous re-entry trigger instead.
- **Nobody moved** on: C-0306 (unanimous twice), A-0028 (kill attempt failed), B-0114 vs B-0104 (7–1 stable).

### Part E — final seating (votes)

| Seat | Vote |
|---|---|
| C-0306 | 8–0 |
| B-0114 (4-arm, +B-0001 arm) | 7–1 (HU for B-0104) |
| A-0028 | 8–0 (FF's kill attempt failed on the record) |
| B-0194 (+B-0169) | 6–1–1 (MED against; FF abstains) |
   280|| C-0338 | 7–1 (HU for A-0206) |

**Standing dissents carried out:** MED (zero medical seats — PI must co-sign the scope hole);
HU (A-0206 flagship killed for the cycle unless the PI funds the corpus outside the Top-5 channel);
R2 reservation (no-$$-flagship portfolio ships notes if all gates deflate);
SEG protest (C-0057 eliminated while battle-ready; named first alternate).
No fake consensus: four of eight voices leave this battle with something on the record.
