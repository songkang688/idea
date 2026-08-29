# Idea_03 — RehearsalGrid

**Does text-batch rehearsal work because of what the text says, or because it puts a
matched-scale gradient on the language pathway?**

Internal ID `C-0090` · Windows7 · ~2,450 A100-h (dies at the gate for <1,000)

---

## The question

Multimodal fine-tuning degrades a base LLM's language ability. Everyone mitigates it by interleaving
text-only batches, and everyone *curates* what goes in them. That practice assumes the rehearsal
text's content is doing the work — an assumption nobody has tested against a content-free control.

So we destroy the content and keep the gradient. At a fixed token budget with matched per-layer
gradient norms, curated rehearsal text is replaced by random web text, then by the *same* text with
tokens shuffled, then by a single document repeated for the entire budget. Then we ask which
language capabilities notice.

| Arm | Rehearsal stream | Destroys |
|---|---|---|
| `A0` | none | — (forgetting floor) |
| `A1` | curated instruction/text mix | — |
| `A2` | random C4 documents | curation |
| `A3` | the same C4 sample, tokens permuted within documents | syntax and content; **keeps unigram statistics and length** |
| `A4` | one ~2K-token document, repeated | diversity |

`A3` vs `A2` separates lexical statistics from syntax. `A4` vs `A2` separates diversity from content.
Those two contrasts are what stop every outcome from being a shrug, and no adjacent paper runs them.

---

## Why every branch is publishable

| Result | Meaning |
|---|---|
| `balance-effect ≥ 0.8 × total` on ≥3 of 4 capabilities | Rehearsal is gradient rebalancing. The field's curation budgets are misdirected; a balance term suffices. |
| `Ret(A2) ≤ Ret(A0)` everywhere | Content really is load-bearing — the first controlled refutation of the pseudo-rehearsal account in the multimodal regime. |
| Anything between | The first **per-capability rehearsal dosing recipe**: how much real text each ability actually needs. |
| The gap is too small to measure | A power analysis bounding how large multimodal linguistic forgetting is under a well-tuned recipe — something the field currently asserts loosely. |

We expect the third. It is the weakest headline and we price it as such.

---

## Run the decision rule now

```bash
pip install -r requirements.txt
python src/run_decision_demo.py
```

No GPU, no model, no training. **Every number it prints is simulated.** It validates the decision
rule, not any claim about rehearsal — the point is that the parts of this project that can be
*wrong* are testable before 2,450 A100-hours are committed.

### What the demo shows

**The rule fires correctly where an effect exists, and refuses where it does not.**

```
--- World 3: stratified -- fluency runs on gradient, knowledge needs content ---
capability            total  balance  content    bal%   cont%
fluency             +0.1212  +0.1192  +0.0019    0.98    0.02
knowledge           +0.0870  +0.0278  +0.0591    0.32    0.68
P3 -- STRATIFIED. Fund the mixture sweep (E4) for the dosing recipe.

--- World 4: forgetting is tiny at this scale ---
knowledge   +0.0040   2 x seed sd 0.0043   FAIL
fluency     +0.0012   2 x seed sd 0.0095   FAIL
NO POWER -- every total effect is below the declared MDE (0.020). The rule declines
to answer. Stop for <1K A100-h and publish the power analysis.
```

World 4 is the one worth staring at. It is the **most likely real outcome**, and a rule that reported
"MIXED, inconclusive" there would invite one more seed and one more arm until something crossed a
threshold. Declining to answer is a decision, and it is cheap.

**Three things the demo also establishes, each of which was a live reviewer attack:**

```
arm                      total    multimodal    rehearsal
A0_none            688,888,889   688,888,889            0
A1_curated         688,888,889   620,000,000   68,888,889
all arms on an identical total budget: True
```
`A0` has no rehearsal stream, so it must draw *more* multimodal tokens to reach the same total.
Skipping that step makes `A0` the shortest run and hands the grid a training-length confound dressed
up as a rehearsal effect.

```
global scale (one scalar for the whole tower) : 3.245
residual per-layer mismatch under the global rule: 0.237 .. 3.233
effective-LR multiplier on the language tower : 4.28x
```
The global convention reports a clean match while individual blocks are off by up to 4.2×. That is
why per-layer is the pre-registered **primary**. The LR multiplier is logged because matching changes
the step size on the language tower — a training-stability risk, not a free operation.

```
stratum                  base  chance  headroom     snr  verdict
reasoning_gsm8k          0.03    0.00     0.030     4.3  FLOOR
instruction_ifeval       0.28    0.22     0.060     2.9  FLOOR
```
Vicuna-7B is near-floor on GSM8K and weak on IFEval. Retention is `score/score(base)`, so those two
strata would let noise flip the ≥3-of-4 rule. They are replaced **before** the arms run.

```
large effect (gap +0.130)  balance share = 0.86  [0.85, 0.87]
small effect (gap +0.030)  balance share = 1.18  [0.66, 1.81]
```
Same underlying 0.85 share, two very different intervals. The 0.8 threshold means something only on
the top row — which is why P0 gates P1.

---

## Three design corrections found while building this

1. **The base cannot be the published recipe.** `EVIDENCE` LLaVA-1.5's `llava_v1_5_mix665k` already
   contains a text-only ShareGPT slice, so "reproduce the published recipe" and "`A0` = no rehearsal"
   cannot both hold. The base is a pre-registered **text-stripped** mix with token-budget
   re-matching; the published-recipe run is a reported reference point, not an arm. This narrows the
   claim's direct applicability, and §3 says so rather than eliding it.
2. **Ratios need usable denominators.** Absolute deltas are now **co-primary** with retention ratios,
   with a denominator-adequacy gate applied before the arms. The Stage-5 abort gate watched only seed
   variance; it never asked whether a stratum could support a ratio at all.
3. **"Divergence between conventions is the finding" is unfalsifiable-adjacent.** With no declared
   primary, every outcome becomes a result. Per-layer matching is now the pre-registered primary
   (justified by documented per-layer gradient disparity); global-norm is a stated sensitivity.

---

## Cost, and the asymmetry that justifies it

| Phase | A100-h | Cumulative |
|---|---|---|
| E0 reproduction + stripped base | 100 | 100 |
| E0b `A3` tokenizer pilot | 100 | 200 |
| **E1 power gate** (A0/A1/A2 × 2 seeds) | 600 | **800 ← kill point** |
| E2 remaining grid arms | 900 | 1,700 |
| E3 second convention | 300 | 2,000 |
| E5 cross-family replication | 300 | 2,300 |
| E6 evaluation | 150 | 2,450 |

`KNOWN FACT` One full LLaVA-1.5-7B fine-tune is roughly 100 A100-h on 8×A100-80GB. **The program
dies for under 1,000 A100-h if the phenomenon is not there.** That asymmetry is the only thing that
makes a 2,450 A100-h project responsible, and it is why E1 is a hard gate rather than a checkpoint.

---

## Files

| Path | Contents |
|---|---|
| `proposal.md` | the full 28-section package |
| `literature.md` | verified sources and their exact relation to this project |
| `experiments.md` | E0–E6 with costs and decision points |
| `reviewer_attacks.md` | A1–A8 and the experiment that answers each |
| `roadmap.md` | day 1 → week 7 |
| `diagrams/architecture.md` | arms, matching, and the decision rule |
| `configs/preregistration.yaml` | frozen before E1 — MDE, strata, primary convention |
| `src/` | runnable prototype of the entire decision rule |
| `references/access_checklist.md` | day-1 dependencies, none confirmed yet |

---

## Honest risks

- **Underpowered at 7B** is the single most likely ending. That is priced in, and it ends cheaply.
- **`A3` may be degenerate** — permuted tokens might give degenerate attention rather than the
  intended unigram-preserving control. E0b pilots this with one run before three seeds are committed.
- **The base model is old.** `KNOWN FACT` LLaVA-1.5-7B is not a 2026 frontier MLLM. Whether the
  result transfers to a current model is unknown and unaffordable here; it is stated as a limitation,
  not hedged.
- **The mechanism space is being colonised in real time** by gradient-side methods papers. The
  mitigation is execution speed, not argument.
- **Portfolio fit.** This is a language-retention study in a mostly-segmentation round. `EVIDENCE`
  That was a deliberate diversification decision by the Stage-6 panel over the segmentation
  reviewer's dissent, recorded in `selection_history/`. No experiment settles it.
