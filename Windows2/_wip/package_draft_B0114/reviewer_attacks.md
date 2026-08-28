# Reviewer Attacks — B-0114: Prompts as Registers

Sections §22–§23. §22 ingests the strongest attack the idea has faced (Agent H, Stage-4 Reviewer-2
pass, `stage4_agent_H/reviewer2_attacks.md` §W2-B-0114) and records how each point is answered *in the
design*, not in rebuttal prose. §23 pre-drafts the attacks the package expects at submission time.

---

## §22 The Stage-4 Reviewer-2 record (H) and how the design answers it

H's opening verdict on the original form was **REJECTION**; the 4-arm redesign earned
**SURVIVE-IF-EXPERIMENT** ("still the best risk-adjusted bet in the batch — but only in the 4-arm form
with DA-VPT cited up front. The 2-arm version E scored is no longer publishable alone."). Point by point:

| # | H's attack (substance) | Status in this package |
|---|---|---|
| A1 | **"The connection is in print."** DA-VPT (arXiv:2505.23694) already observes register-style artifacts in VPT prompt attention, cites Darcet, calls registers "analogous to learnable prompts" — you would merely be first to *quantify* it | Adopted as the novelty boundary. DA-VPT is cited up front in every outward document (§12, §13); the claim is scoped to quantification + dissociation + H2 boundary law — none of which DA-VPT contains, and DA-VPT's own text defers exactly this to "future investigation" |
| A2 | **Known competitor mechanism.** Test-time registers (arXiv:2506.08010) shows register function is reproducible by a pure attention bias — "VPT tokens absorb global aggregation" must be disaggregated from it | Arm (c) *is* the 2506.08010 construction, promoted from threat to instrument; the (b)/(c)/(e) triad is the disaggregation (§8, §21.1) |
| A3 | **Frozen-token control is confounded as designed.** Any inserted token changes every softmax denominator (temperature effect) | Answered structurally: arm (c) has no sequence-length change; arm (e) `sink_only` isolates the denominator shift; K-sweep E3 separates saturating absorption from K-scaling smoothing. Residual stated in print (§21.1) |
| A4 | **The likely outcome is mush** (partial reproduction 20–40%: "VPT partly works by learning — nobody doubted it") | Pre-registered interpretation table (§18) gives every cell a named consequence; the mush region itself has a pre-registered handling (degrade to merged-note mechanism half; B-0194 activates). The kill cell K1 is crisp: <5% each AND H2 < 2× sd |
| A5 | **A paper about the past.** Register-equipped backbones (DINOv2-reg, DINOv3) are becoming default | The H2 arm converts the decay into the paper's own prediction: if register function is real, VPT should gain less where registers are built in — a boundary law that stays relevant *after* the transition. Plus the binding calendar clock (§26 R3) |
| A6 | Hidden assumption: frozen-random tokens isolate "register function" rather than generic capacity | Conceded and re-scoped: arm (b) is labeled *insertion*, never *register function*; register function is claimed only from arm (c) + signatures (§17) |
| A7 | Hidden assumption: VPT benchmark gains may be head-tuning artifacts | Two head classes for every arm, both reported (§21.2) |
| A8 | Hidden assumption: high-norm signature = register function (PH-Reg low-norm counterexample) | Norms demoted to secondary; NOP/broadcast diagnostics (arXiv:2606.08105) are the primary signature axis — made mandatory by L's audit (§8, §21.3) |
| A9 | Hidden assumption: shallow results transfer to VPT-deep | E4 covers deep before any "VPT in general" wording (§16, §21.5) |

L's audit (Finding 1) added the sharpest attack of all — **the original pilot was already run by VPT's
own Fig. 11 in 2022** — and it is answered by construction: the classification Fig. 11 setting is this
project's *bug-detector control* (E0), the dense-task replica of Fig. 11 is a *pre-registered stopping
outcome with a pre-drafted title* (§18 K1, §19), and the naive form is struck from the package entirely
(PI binding).

## §23 Anticipated fresh attacks & pre-drafted answers

**R2-1: "Three seeds is not statistics."**
Conceded for the killer grid and said in print: with n=3 the H2 readout is a directional check with a
2×-sd declaration threshold (§17); unstable cells get pre-approved +2 seeds only (§18 X2); E5/E6 carry
generalization. The 24-run grid is a *decision instrument* for the program, and the paper's claims are
worded to what survives the full matrix.

**R2-2: "Your bias arm is one implementation; register function ≠ 2506.08010's construction."**
The claim is scoped to "attention-geometry function as instantiated by the test-time-registers
construction," with arm (e) as a second, independent geometry-only implementation. If the two geometry
arms disagree, that disagreement is reported (cell M2/X1 territory), not averaged away.

**R2-3: "DINOv2 vs DINOv2-reg are different training runs — your H2 contrast is confounded by run
variance."**
E6's patched-sibling pair (identical weights, registers added post hoc) is the within-run control; H2
must agree in direction across both pair types before the boundary law is claimed (§21.4).

**R2-4: "Fig. 11 already told us the answer; this is a delta paper."**
Fig. 11 is classification-only and two-armed. The register literature's core finding is that artifact
damage is a *dense-task* phenomenon invisible to classification metrics — which is precisely why the
2022 ablation cannot settle the dense question, and why our E0 expects to *reproduce* Fig. 11 on
classification while the dense grid is free to land anywhere (§10, §14). If the dense grid also
reproduces it, we stop and say so (§19) — the question was still worth closing, per DA-VPT's own
"future investigation" deferral.

**R2-5: "The retrofit pivot (title §1.3) would just be test-time registers applied to dense tasks."**
The retrofit branch's contribution is not the construction but the *substitution claim*: matched-budget
evidence that a training-free bias replaces a *trained PEFT method* on dense prediction, plus the
failure boundary (where learned content is irreplaceable). 2506.08010 never benchmarks against VPT.

**R2-6: "You planned a negative-result escape hatch to guarantee publishability — deflationary notes
are not papers."**
The deflationary branch is not a hedge; it closes a question a CVPR 2025 paper explicitly opened
(DA-VPT §Artifact Consideration), completes a canonical ablation where its authors did not run it, and
retires a motivation link (B-0001) the micro-field is actively building on. Short, yes; note-shaped,
yes; and pre-registered as such (§18 K1, §27).

**R2-7: "Why should anyone care once every backbone ships registers?"**
Because the H2 boundary law is exactly the *transition guidance*: it tells practitioners what happens
to token-based PEFT when they move to register-equipped backbones (gain shrinkage or not), and it
explains retroactively which historical VPT wins were register-function in disguise. The claim's value
survives the population shift; the *measurement window* is what expires — hence the quarter clock
(§26 R3).

**R2-8 (internal, PI-level): "The sandbox already told you the answer is content-dominant — why fund
the grid?"**
Because the sandbox cannot exhibit the scale-emergent artifact phenomenon the hypothesis rides on
(§20): a toy without high-norm artifacts finding no register component is consistent with *both* K1
and M1 on real backbones. The sandbox's job was instrument validation; it raised K1's credence (logged,
§26 R1) and the grid's price (1–1.5 GPU-weeks, exp_02-gated) was set with that credence in view — this
is the portfolio's priced ceiling bet, seated 5–2–1 with that risk on the record.
