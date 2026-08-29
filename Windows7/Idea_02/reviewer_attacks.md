# Idea_02 — Reviewer #2 Attacks and Responses

From `stage4_cluster_A_attacks.md`, `stage6_attack_brief.md` (verdict: **PIVOT**) and
`stage6_defense_brief.md` (panel vote: FM ADVANCE · SEG ADVANCE · MED BORDERLINE · METH ADVANCE).

Stage 6 changed this design more than any other in Windows7. Every mandatory condition below is
**funded as an experiment**, not promised in prose.

---

## A1 — "The predictive-validity leg passes for a trivial reason" · **FATAL as originally specified**

The strongest attack in the round. P3 originally required per-sequence reversible fraction to
predict SAMURAI/DAM4SAM gains at `r > 0.6`. But reversible fraction and prevention gains are **both**
downstream of generic sequence difficulty — distractor density, occlusion count, failure count,
natural recovery rate. A raw `r > 0.6` is exactly what a shared-difficulty confound produces with
**no instrument validity at all**. The pre-registered statistic could not distinguish "this measures
the memory-borne share" from "hard sequences are hard for everyone."

**Response — change the statistic, not the story.**

1. **Partial correlation.** Regress the difficulty covariates out of both sides first. Pre-registered
   bar: `partial r > 0.4` (lower than 0.6 precisely *because* partialling removes the inflation).
2. **Minimum over a frozen comparator set.** The set is named before any comparator runs, and the
   reported statistic is the minimum across it — not "SAMURAI *and* DAM4SAM", which permits choosing
   the comparator that carries the headline.
3. **Nested-model ΔR²** reported alongside: does adding `ρ` improve on a difficulty-only model?

`KNOWN FACT` The prototype makes this concrete on data where the confound is injected by
construction: naive correlations of 0.952 / 0.918 / 0.859 become partial correlations of 0.682 /
0.397 / **0.028**. The minimum-over-set rule is what stops that third comparator from being quietly
dropped. Run `src/run_pilot.py` to reproduce.

---

## A2 — "Targeted deletion is not the clean intervention you assume" · HIGH

SAM2's memory attention consumes recent non-conditioning frames with **recency-indexed temporal
position encodings**. Deleting post-error entries forces pre-error entries into recency slots they
never occupied during training, so the surgered configuration is off-distribution *independently of
the content* of what was deleted. Part of any targeted-vs-reset gap could be an encoding artifact,
in either direction. The random-deletion control does not isolate this.

**Response — add the sham arm, and get its definition right.**

`sham` deletes a **count-matched number of pre-error (uncorrupted) entries** while leaving every
post-error entry in place: same incision, nothing therapeutic removed. If `targeted` does not beat
it, the benefit comes from the mechanical consequences of deleting entries and the instrument is
dead — for about 10 GPU-h at pilot scale.

> **Definition correction, recorded.** Stage 6 worded the sham as "delete post-error entries but
> re-insert count-matched pre-error duplicates at the same recency slots." Implemented literally that
> arm *still removes the corruption* — it performs the therapeutic action — so it would match
> `targeted` even when the instrument is perfectly valid, making P3 unpassable by construction. The
> literal version is retained as a separate arm, `slot_control`, which answers the different question
> of whether slot occupancy matters once content is gone.

`KNOWN FACT` The prototype demonstrates the control firing: in a simulated world with **zero**
memory-borne failure where the tracker merely prefers emptier banks, `targeted` beats `no_op` by
+0.397 and the gate correctly refuses.

---

## A3 — "SAM3 shipped; this is archaeology" · HIGH

`EVIDENCE` SAM3 (Nov 2025, `arXiv:2511.16719`), SAM 3.1 (Mar 2026); the SAM3 tracker inherits the
SAM2 memory architecture. `arXiv:2512.22624` (Dec 2025) already restudies memory mechanisms inside
SAM3 and ships a public tracking zoo.

**Response — fund E7 and change what the paper is about.** Running the identical protocol on SAM2.1
*and* SAM3 converts the deliverable from "SAM2 has this much memory-borne failure" into **"here is
how much memory-borne failure a model-generation change actually removed, and how much it did
not."** That is a materially larger paper. The released SAM3 zoo makes the ports cheap. ~30 GPU-h.

---

## A4 — "Surgery is a decades-old reset heuristic" · MEDIUM

Now backed by a citable fix paper: CL-MC (`arXiv:2602.19380`), detector-triggered memory overwrite
for SAM2 drift.

**Response.** P2 *is* this test, pre-registered at ≥10 points with a bootstrap CI excluding 0.
`KNOWN FACT` A structural caveat found while prototyping and reported rather than buried: `targeted`
and `reset` are the **same operation** whenever the failure outlasted the memory horizon, because
FIFO has already flushed every pre-error entry. Only 23 of 50 simulated failures retained pre-error
memory. The real harvest reports this share at E1, before any P2 claim, and **P2 is evaluated on
that subset** — pooling the coincident failures dilutes a real gap toward zero rather than measuring
a smaller one (+0.130 became +0.040 in the prototype).

---

## A5 — "Cherry-picked failures" · MEDIUM

**Response.** Fixed harvest protocol with **zero curation** — every failure meeting the definition
enters. Ambiguous-reappearance events are pre-registered as a stratum and reported separately rather
than dropped. The `(IoU threshold, k)` pair that defines the corpus is swept, and the corpus itself
is released.

---

## A6 — "An oracle-timed ceiling is decision-irrelevant" · MEDIUM, partly unresolvable

No deployment has an oracle telling it when the object reappears.

**Response — two moves, and honesty about the residue.**

1. **Promote the `t_r ± δ` timing dose–response from ablation to a main result** (METH's condition,
   effectively resolved in METH's favour). The reader sees how the ceiling degrades as the oracle
   weakens, and the term "oracle-timed ceiling" is used throughout instead of "upper bound".
2. **Cross-validate against SAM2RL's ceiling**, which is derived by optimisation rather than oracle
   timing. Two independently derived ceilings agreeing is worth far more than a framing argument.

Residue: a deployment-minded reviewer may still object that the ceiling is not reachable. That is
the point of a ceiling, but the objection is not experimentally answerable, and the follow-up paper
(replace the oracle with a learned detector) is named in `proposal.md` §26 rather than promised here.

---

## Expert disagreements from Stage 6

### D1 — Is a SAM2.1-only paper viable? · UNRESOLVED at Stage 6

FM: the SAM3 arm must be **core**, or the paper reads retrospective at submission.
SEG: adding SAM3 doubles harvest cost and risks a two-model survey instead of one decisive
decomposition; the protocol's value is method-independent.

**Resolution here:** funded as E7 with a pilot, not promised as future work. If the SAM3 pilot shows
the port is expensive, the paper ships SAM2.1-first with the SAM3 arm as a reported secondary — and
says so explicitly rather than omitting it.

### D2 — Natural video only, in a portfolio with a declared medical axis · RECORDED AS A CONDITION

MED: echocardiography, endoscopy and surgical-tool tracking are where SAM2 memory failure is
clinically load-bearing, and none of it appears.

**Resolution here:** **E8, one medical-video arm, ~10 GPU-h.** Cheap. If the memory-borne share is
larger there than in natural video, that becomes the more interesting venue and a natural
follow-up (`proposal.md` §26).

### D3 — Framing encroachment vs scooping · UNRESOLVED

All four experts agree `arXiv:2512.22624` has not run oracle surgery or a reversibility
decomposition. FM: the "systematic memory-centric study" real estate is occupied, so the pitch must
be decomposition-first. METH: the distinction is clean enough to survive review on the pre-registered
legs alone. **We adopt FM's framing and METH's confidence** — decomposition-first pitch, legs
unchanged.

---

## Residual risks, owned

1. **Scoop risk is the portfolio's single highest.** `KNOWN FACT` This subfield published at least
   six memory policies in two years plus a systematic study with a SAM3 zoo in Dec 2025. Mitigation:
   pre-register and release the protocol early; sequence this project first. The harvested corpus,
   surgery toolkit and validity methodology remain publishable if the headline is scooped.
2. **DiDi access** — academic distribution, no mirror. Day-1 hard dependency.
3. **Harvest yield**, and the tighter H2-testable yield (A4).
4. **Replay determinism** — E0 gates on it; unfixable non-determinism kills the project.
5. **Protocol sensitivity** — the failure definition has free parameters that determine the whole
   corpus. Swept and released; the headline number will still be parameter-sensitive and is reported
   with the sweep beside it.
