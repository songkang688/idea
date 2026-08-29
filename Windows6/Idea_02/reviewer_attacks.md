# Idea_02 — Reviewer attacks & answers

A-series from the Stage-4 pass recorded in `stage4_reviewer2_cheap5.jsonl` and
`reviewer_summary.md`. B- and C-series are our own red team. **No attack is
listed without the evidence that answers it**, and where an attack is only
partly mitigated it says so.

---

## A. The Stage-4 attacks (binding)

### A1. "The blog already diagnosed this"

**The attack.** The Voxel51 Pyro-SDIS audit already reported shared-camera
near-duplicates. You are writing up a known problem.

**Evidence that shuts it.** **VERIFIED PRIOR WORK**, and the record is precise
about what it is: `literature.md` files it as *"2026 blog — diagnosis, **no**
retrained mAP"*. We **retrain under three protocols and quantify the deltas with
event-clustered CIs**, and we add the confounder split (H4) that the blog does
not attempt. A diagnosis and a measured inflation with a mechanism are different
contributions.

**Standing constraint (FACT).** *"Do not cite a peer-reviewed mAP inflation
number we did not compute."* No such number appears anywhere in this package.

### A2. "Camera identity is just geography" — the fatal one

**The attack.** Different cameras are different places: different terrain,
vegetation, haze, sun angle. Camera-disjoint scoring lower is ordinary domain
shift. You have re-measured a known phenomenon and called it leakage.

**Why it is dangerous.** Because it is the default reading, and if it stands the
paper has no finding.

**Evidence that shuts it.** The **empty-frame memorisation probe (H4)**. Empty
frames contain **no plume**. A seen-versus-unseen camera gap on negatives cannot
be a plume-appearance domain shift — there is no plume to shift. It has to be
the background, i.e. memorisation.

Supporting controls: the detector trains on non-empty frames only, so both sides
of the comparison are held out under identical conditions; the ImageNet control
backbone (E3) distinguishes "the detector learned it" from "any backbone
encodes scene identity".

**FACT.** `proposal.md` is blunt: *"Fatal if we only report camera-disjoint drop
without H4."* H4 is not a robustness check. It is the paper.

### A3. "Tiny camera N"

**The attack.** With a handful of towers, the camera-disjoint estimate is one
draw from a tiny population and the CI is meaningless.

**Evidence that shuts it.** Multiple folds; 3 seeds; **event-clustered**
bootstrap CIs; a camera-count sensitivity ablation showing the gap is not driven
by one unusual tower. And a hard pre-declared floor: **<10 cameras triggers the
pivot to event-disjoint only**, which forfeits H2 and sends the idea back for
re-argument rather than shipping an underpowered claim.

### A4. "PYRONEAR already fixed splits"

**The attack.** Event-disjoint splitting is deployed. The problem is solved.

**Evidence that shuts it.** This is exactly H2, and the code makes it checkable
rather than assertable. `splits.camera_overlap` and `splits.event_overlap`
report per-protocol counts, and the self-checks assert the structure:
event-disjoint shares **0 events but >0 cameras**; camera-disjoint shares
neither. If event-disjoint turned out camera-disjoint on a real dataset, H2
would be unfalsifiable there and the pivot fires — stated in advance, not after
seeing the numbers.

### A5. "mAP is noisy"

**Evidence that shuts it.** 3 seeds; H1 requires a gap exceeding seed std; FAR
at fixed recall reported alongside AP because it is the operationally meaningful
number; and the CI method resamples events rather than frames.

---

## B. The attacks that decide whether this is a paper

### B1. "You cannot separate memorisation from domain shift at all"

**The attack.** Even empty frames from a seen camera differ from empty frames
from an unseen camera in terrain and lighting. The gap could still be shift.

**Why it is dangerous.** It is the sophisticated version of A2 and it partly
lands.

**Evidence that shuts it — and its limit.** The ImageNet control backbone (E3)
separates "generic scene identity, available to any model" from "identity this
detector learned". A gap present in the detector backbone and absent in the
ImageNet backbone is hard to explain as terrain.

**Honest limitation.** This does not fully close the attack. A complete answer
would need empty frames from the *same* camera under different conditions, or a
matched-terrain camera pairing, neither of which is specified. **Recorded as
partly mitigated.**

### B2. "The whole gap is duplicate frames"

**The attack.** Near-duplicate frames across the split, not camera signature.
The blog already said so.

**Evidence that shuts it.** Card **E4**: pHash dedup, rebuild all splits, rerun.
Pre-declared branches — survives dedup → camera signature; disappears → downgrade
to a near-duplicate audit; shrinks → report both numbers and attribute the share.
The outcome is pre-committed, so it cannot be spun afterwards.

### B3. "There is no reduced version of this paper"

Not a reviewer attack — a planning fact, recorded because it changes how the
work should be scheduled.

**FACT.** The Stage-4 record gives Idea_02 **no downgrade clause**. Its residual
is a requirement, not an *"else …"* — unlike Idea_01, which was explicitly
allowed to become an evaluation note. The only documented fallback is the
<10-camera pivot, which forfeits H2. `stage6_battle.md` §2.2 recorded the
reading: **Idea_02 is a full paper or a kill.** Do not plan on salvaging a
partial result.

---

## C. Our own red team

### C1. "Your camera-ID probe is memorising fire episodes, not cameras"

**This is a real defect that was present and is now fixed.** On a random split
the probe can name the camera by recognising the *episode* shared across the
split. **Measured during W6-T3:** with the camera signature switched off
entirely, a random-split probe still beat chance by ≈0.17 — pure event leakage.

**Answer.** H3 is evaluated **event-disjoint**, always. Two self-checks pin it:
one asserts the event-disjoint control sits near chance, the other asserts the
random-split version *is* confounded, so the rule cannot be silently dropped by
a later refactor.

### C2. "Your equal-N matching hides the effect"

Subsampling the test side to match size and class ratio could remove real
signal. **Answer:** report matched and unmatched side by side. And
`match_equal_n` **raises** rather than shipping a comparison whose positive
ratio it could not match — an unmatched comparison produces no number instead of
a misleading one.

### C3. "Image-level AP is not detection"

**Answer.** Deliberate, and stated in `proposal.md` §15: the operational
question for a tower is false alarms at a required recall, not box tightness.
IoU is secondary. If a reviewer insists, box metrics are an addition, not a
replacement.

### C4. "Empty frames are not representative negatives"

Frames with no fire anywhere may be trivially easy, making the FPR comparison
uninformative. **Answer:** report the absolute FPRs alongside the gap, so a
reader can see whether either side is near the floor. If both are ≈0 the probe
is uninformative and must be reported as such rather than as a null result for
H4. **Not fully mitigated** — a harder negative pool (dawn fog, dust, cloud
shadow) would be a better instrument and is not currently specified.

### C5. "One dataset is not a benchmark claim"

**Answer.** E5 adds a second corpus; `proposal.md` §20 requires H1 and H4 on ≥2
datasets to CONTINUE. If only one dataset has camera IDs, the title names that
dataset. Honest scope over implied generality.

### C6. "Your synthetic harness proves nothing"

Correct, and the package says so at runtime. The camera signature was planted by
`make_corpus`; `run_smoke.py` prints that before any number. E0 checks that H2 is
*expressible* in code, and nothing else.

### C7. "Publishing camera IDs exposes tower locations"

**Answer.** Camera IDs are released as **opaque indices**, never coordinates.
No imagery is redistributed — only split indices and derived metrics.

---

## Standing discipline

1. Never cite an inflation number we did not compute. The Voxel51 audit is a
   blog diagnosis with no retrained mAP, and must be described that way.
2. The probe is always evaluated event-disjoint.
3. Empty frames are never trained on.
4. CIs cluster over events, never frames.
5. Report camera-shared and event-shared counts in every table.
6. GATE-A before any GPU.
7. Never relabel EXPECTED as ACTUAL. There is no smoke mAP in Windows6.
