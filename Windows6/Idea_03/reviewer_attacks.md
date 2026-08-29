# Idea_03 — Reviewer attacks & answers

A-series from the Stage-4 pass recorded in `stage4_reviewer2_cheap5.jsonl`.
B-series covers the two attacks that could end the project. C-series is our own
red team. **No attack is listed without the evidence that answers it**, and
where an attack is only partly mitigated it says so.

---

## A. The Stage-4 attacks (binding)

### A1. "Generic visual forgetting is already published"

**The attack.** MDGD (EMNLP Findings 2025, **VERIFIED PRIOR WORK**) reports
visual forgetting under instruction tuning. TWIST & SCOUT (ICCV 2025,
**VERIFIED PRIOR WORK**) addresses grounding under forget-free tuning. The
headline is taken.

**Status.** Correct, and Reviewer #2 **killed the generic headline outright**.
The idea survives only in a narrower form.

**Evidence that shuts it.** Framing discipline, enforced in `proposal.md` §8 and
§23: the claim is **stage isolation + format control**, never *"alignment hurts
vision"*. **Cite MDGD as an attack, not as background** — a related-work mention
reads as ignorance; an explicit "MDGD establishes the phenomenon, we ask which
stage pays and whether the backbone still contains the box" reads as
positioning. TWIST & SCOUT proposes a *fix*; a fix that works does not tell you
which stage paid.

### A2. "Unmatched data mixes — you cannot claim RLHF causality"

**The attack.** Base and chat checkpoints differ in far more than the alignment
objective. Any gap could come from the instruction-tuning data mix.

**Why it is dangerous.** Purely observational comparison genuinely cannot
separate these.

**Evidence that shuts it.** Card **E4**: text-only DPO LoRA applied to the base
checkpoint, with **no images**. If the localization gap reproduces from
text-only preferences, the objective is implicated rather than the image data
mix.

**Binding constraint (FACT, verbatim from the original file):** *"do not claim
causal RLHF without H3."* Until E4 runs, `proposal.md` §23 forbids the causal
framing entirely — H1 and H2 stand on their own as a diagnosis without it.

### A3. "Box parsing is not localization"

**The attack.** A chat model that answers *"Sure! The cat is at [12, 30, 44,
80]"* has localised correctly and been scored zero by a strict parser. You are
measuring prose.

**Why it is dangerous.** It is the most likely true explanation of the reported
phenomenon, and if unaddressed the paper measures the wrong thing.

**Evidence that shuts it.** Three layers, in increasing strength:

1. **Permissive parsing.** `parse_box` strips prose, brackets and separators, so
   a parse failure means "no four numbers", not "unexpected wrapper".
2. **Parse-failure rate reported as its own number**, never folded into the IoU
   mean as zeros. The difference between IoU-with-failures and
   IoU-on-parseable-only **is the format tax, quantified**.
3. **Likelihood ranking** — generation-free, so prose cannot touch it. A gap
   that survives mode 3 is not a parsing artifact.

And the pre-registered kill rule: **if H1 fails under constrained decoding, the
project dies.** `classify_outcome` raises rather than returning a verdict when
the likelihood mode was not run, so the shortcut is unavailable in code.

### A4. "Small N of model families"

**Evidence that shuts it.** Honest scope. E2 replicates on a second pair; if
only one pair passes GATE-B, the title names that pair rather than implying
generality, and E4 stays locked because a causal claim from a single pair is not
defensible.

---

## B. The two attacks that could end the project

### B1. Concurrent work — **the highest-risk attack in Windows6**

**The attack.** *"This appeared three months ago."*

**Why it is dangerous, from three independent records (all FACT):**

| Source | Evidence |
|---|---|
| `stage3_DE_top10.json.md` | E-009 keep confidence **0.55** — lowest of the Final 3 — note: *"matched checkpoint localization tax **still open**"* |
| `literature.md` | The gap is an **EVIDENCE GAP at confidence ~0.5** — a search that did not find the paper, not proof it does not exist |
| `Windows6/README.md` | *"Highest impact, **highest concurrent-work risk**"* |

**Why the exposure is structurally high, not just unlucky.** The experiment is
eval-only (≤8 GPU-h), needs no new data, needs no training, and uses public
checkpoints. Everything that makes it attractive to us makes it attractive to
everyone else. And the novelty is **defined by an absence** — absences close on
their own, without anyone doing anything wrong.

**Evidence that shuts it — partially:**

- **Speed.** Run E-B and E1 first. `roadmap.md` schedules Idea_03's gate check
  ahead of its tractability ranking for this reason alone.
- **Re-check before writing.** MDGD, TWIST & SCOUT and especially
  arXiv 2602.12506 (recent enough that a v2 could contain this) must be
  re-checked immediately before writing, not at submission.
- **A fallback contribution that cannot be scooped the same way.** The
  pre-registered O1/O2/O3 decision procedure and the format-controlled protocol
  are a **methods** contribution — *how to measure this correctly*. Someone
  reporting a number does not scoop a released decision rule.

**Honest limit.** None of this reduces the probability of being scooped. It
reduces the cost. For an absence-defined claim there is no mitigation other than
speed, and this file should not pretend otherwise.

### B2. "Your two checkpoints are not comparable" — GATE-B

**The attack.** If the base and chat checkpoints differ in vision encoder or
coordinate tokenization, the measured gap is an encoder or tokenizer difference
wearing an alignment costume.

**Why it is dangerous.** There is **no downstream mitigation**. No amount of
careful evaluation repairs an unmatched pair.

**Evidence that shuts it.** Card **E-B**, which this package's own
`experiments.md` has always called a *"Hard gate"*: shared vision encoder
confirmed from the config (not the name), shared coordinate tokenization,
compatible licences. `data.verify_checkpoint_pair` raises with those three
checks spelled out, so the code cannot proceed on an unverified pair by
accident.

**If it fails:** stage isolation is unavailable and Idea_03 descopes to a
format-artifact study — a much smaller paper that must be re-argued for its
Final-3 slot. This is why GATE-B keeps Idea_03 PROVISIONAL in
`stage6_battle.md` §5.

---

## C. Our own red team

### C1. "You probed the wrong layer"

A linear probe at one depth is one measurement. **Answer:** card E3 sweeps
layers, and the pre-declared branch is a downgrade — if the gap exists at one
layer only, report the sweep rather than a headline.

### C2. "A linear probe is too weak to show the box is gone"

Absence of linear decodability is not absence of information. **Answer:** E3
adds an MLP probe. If the linear probe drops and the MLP does not, the finding
becomes *"present but not linearly accessible"* — a distinct and more precise
result than "representation tax", and it should be reported that way rather
than folded into O3.

### C3. "Your ridge penalty is doing the work"

**Answer:** ridge is there for a stated reason — with a small train split and
correlated token dimensions, an *unregularised* fit can recover a box from noise
and would report "representation intact" for a destroyed representation, i.e.
it biases towards O2. Report probe error across a penalty sweep so the
conclusion is visibly not a function of one hyperparameter.

### C4. "The distractor sets differ between checkpoints"

**Answer:** they are shared by construction (`make_pair` builds one set per
example, used by both arms). A likelihood gap therefore cannot come from an
easier candidate set. The distractor **count** is also swept (4/8/16), because a
gap that appears at one set size is a property of the set.

### C5. "One prompt template is one draw"

Alignment changes prompt sensitivity, so a single template could produce the gap
by itself. **Answer:** template ablation in `proposal.md` §18. **Only partly
mitigated** — a full prompt-robustness study is a paper of its own, and the
ablation shows sensitivity rather than eliminating it.

### C6. "O1 means you have nothing"

**Answer:** no. `experiments.md` says *"write negative"*. Establishing that a
widely cited degradation is largely a parsing artifact is a service, given the
field is drawing training-time conclusions from a decoding-time problem. What is
**not** acceptable is running only free-form evaluation, seeing a gap, and
reporting a tax — which is why `classify_outcome` refuses to return a verdict
without mode 3.

### C7. "Your synthetic harness proves nothing"

Correct, and the package says so at runtime. E0 checks that the O1/O2/O3
decision logic recovers a planted answer. The base and chat "models" are
simulators whose failure mode we chose. It validates the ruler, not the object.

### C8. "You are measuring RefCOCO, not localization"

**Answer:** honest scope. The claim is about coordinate emission on referring
expressions, and `proposal.md` §27 forbids generalising it to "alignment is
harmful". Extending to other grounding formats is future work, not an implied
claim.

---

## Standing discipline

1. Never claim "alignment hurts vision" — published, killed at Stage 3.
2. Never claim RLHF causality without H3 (card E4).
3. Always run all three eval modes; the verdict function refuses without mode 3.
4. Always report parse-failure rate as its own number.
5. Distractors are shared between checkpoints.
6. GATE-B before any GPU.
7. Re-check the adjacent literature immediately before writing — the novelty is
   absence-defined at confidence ~0.5 and decays with time.
8. Never relabel EXPECTED as ACTUAL. Windows6 has run no VLM eval.
