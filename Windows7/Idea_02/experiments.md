# Idea_02 — Experiment Plan

Zero training. 1× A100-40GB, peak VRAM ≈16–24 GB.
**Core ≈80–120 GPU-h; with the Stage-6 mandatory arms ≈140–180 GPU-h.**

---

## Pre-registration (committed before E2)

Frozen in `configs/preregistration.yaml`:

- failure definition `(IoU < 0.1 for k consecutive frames after ≥ 0.5)`, with `k` fixed and swept
- recovery definition `(IoU ≥ 0.5 within w frames, sustained)`
- the ambiguous-reappearance stratum, reported separately
- all six arms, including both controls
- **the comparator set `C`, named before any comparator runs**
- the validity statistic: `min_{c ∈ C} partial r > 0.4`, covariates fixed
- P1/P2/P3 thresholds verbatim

Freezing `C` is the single most important line in the file. "SAMURAI *and* DAM4SAM at r > 0.6"
silently permits choosing which comparator carries the headline after seeing results.

---

## Experiment matrix

| # | Experiment | Cost | Decides |
|---|---|---|---|
| **E0** | DiDi access + **replay-determinism gate** | ~2 GPU-h | whether anything downstream is interpretable |
| E1 | Failure harvest, LVOS v2 + DiDi, Hiera-B+ and Hiera-L | ~12 GPU-h | corpus yield, ambiguous share, **H2-testable share** |
| **E2** | **Pilot: 50 failures × 6 arms + partialled regression** | ~10 GPU-h | **go / no-go** |
| E3 | Full surgery: ≥200 failures × 6 arms | ~25 GPU-h | P1, P2, P3 |
| E4 | Comparator passes over frozen `C` | ~35 GPU-h | P4 (validity) |
| E5 | Memory-attention logging | +20% | interference vs competition taxonomy |
| E6 | Deletion scope + timing dose–response `t_r ± δ` | ~15 GPU-h | oracle-strength sensitivity (A6) |
| E7 | SAM3 generational arm | ~30 GPU-h | significance (A3) |
| E8 | Medical-video arm | ~10 GPU-h | portfolio fit (D2) |

---

## E0 — the gate that comes before science

Replaying an untouched memory bank from `t_r` must reproduce the original failure **bit-for-bit**.
SAM2's video-predictor caches make this a genuine risk. If the `no-op` arm is not deterministic,
every arm difference is partly harness noise.

`src/memory_surgery/replay.py::check_replay_determinism` raises rather than warning, because a
warning here is something a tired person ignores at 2am.

Also day 1: confirm DiDi access at `go.vicos.si/didi`. There is no mirror.

---

## E1 — harvest, and the two yields that constrain everything

Fixed protocol, **zero curation**: every failure meeting the definition enters. Two numbers are
reported before any arm is scored:

1. **Total usable yield.** Target ≥200 organic failures with GT reappearance frames from LVOS v2
   (140 videos) + DiDi. If short, scale out to SA-V val.
2. **H2-testable yield.** `targeted` and `reset` are *the same operation* whenever the failure
   outlasted the memory horizon, because FIFO has already flushed every pre-error entry. Only
   failures with `t_r − t_f` shorter than the bank capacity can test H2. In the prototype run this
   was 23 of 50 simulated failures. If the organic distribution is worse, the corpus supports P1
   and P3 but not P2, and the paper says so instead of pooling.

   **P2 is read on this subset, not on the pooled corpus.** Failures where the two arms coincide
   contribute an exact zero to the gap, so pooling dilutes a real effect rather than measuring a
   smaller one. In the prototype a genuine +0.130 subset gap pooled to +0.040 — below the
   pre-registered 0.10 bar, in the world where the decomposition is real. The pooled number is
   reported alongside and labelled as diluted.

The ambiguous-reappearance stratum is tagged and reported separately, never dropped.

---

## The six arms

| Arm | Operation | Question |
|---|---|---|
| `no_op` | nothing | natural recovery |
| `targeted` | delete entries written in `[t_f, t_r)`; keep conditioning + pre-error | the claim |
| `reset` | keep conditioning frame only | is it just a restart? |
| `sham` | delete a **count-matched number of pre-error (clean) entries**, leave corruption in place | do the motions alone help? |
| `slot_control` | `targeted`, then refill vacated recency slots with pre-error duplicates | does slot occupancy matter once content is gone? |
| `random_k` | count-matched random deletion | does it matter *which* entries? |

`sham` is the vacuous control — same incision, nothing therapeutic removed. `slot_control` is the
Stage-6 arm as literally worded; it is kept because it answers a real question, but it is not the
arm P3 tests against (rationale in `proposal.md` §3).

**Caveat, reported rather than hidden:** `sham` can only be exactly count-matched when enough
pre-error entries survive to delete. The realised match count is logged per failure.

---

## E2 — the pilot gate (~10 GPU-h)

50 failures, all six arms, plus the difficulty-partialled regression at pilot scale.

| Outcome | Action |
|---|---|
| `targeted ≈ sham` | **stop.** The instrument story is dead; the honest report is deletion mechanics. |
| `targeted − reset < 3 pts` **and** pilot partial `r < 0.2` | **stop before comparator passes.** Release corpus + toolkit as a tech note. |
| otherwise | proceed to E3 |

`KNOWN FACT` The prototype in `src/` demonstrates this gate catching a fabricated artifact: in a
simulated world with *zero* memory-borne failure where the tracker merely prefers emptier banks,
`targeted` beats `no_op` by +0.397 — and the control arms fire, so the gate correctly refuses.

---

## E3/E4 — the killer experiment (~60 GPU-h)

> **(1)** `targeted` beats `no_op` by ≥30 points, `reset` by ≥10, **and `sham` by ≥10**.
> **(2)** `min_{c ∈ C_frozen} partial r > 0.4`, partialling out no-op recovery, failure count and
> distractor density; nested-model ΔR² reported alongside.
>
> Either miss kills the instrument claim.

Why partial rather than raw: reversible fraction and prevention-method gains are both downstream of
sequence difficulty, so a raw `r > 0.6` is exactly what a shared-difficulty confound produces with
no validity at all. In the prototype, naive correlations of 0.93 fell to 0.55 / 0.56 / **0.12** after
partialling — and the minimum-over-set rule is what stops the 0.12 comparator from being quietly
dropped.

---

## Ablations

- **Deletion scope:** all post-error vs recent-`k` vs object-pointers-only vs spatial-features-only.
- **Timing `t_r ± δ`** — **promoted from ablation to a main result** (A6): it shows how the ceiling
  degrades as the oracle weakens, which is the honest answer to "no deployment has an oracle."
- Recovery window `w`; failure definition sweep (IoU < 0.1 vs < 0.3; `k`).
- Backbone size (Hiera-B+ vs Hiera-L); SAM2 vs SAM2.1.
- With / without the ambiguous stratum.

---

## Controls

1. `reset`, `sham`, `slot_control`, `random_k` — four different artifact channels.
2. **Sham surgery at random non-failure times**: must *not* change tracking. Harness validity.
3. Replay determinism (E0).
4. Difficulty covariates in every validity model.
5. **Cross-ceiling check against SAM2RL's optimisation-derived bound** — two ceilings from different
   principles agreeing is worth more than any framing argument.

---

## Failure taxonomy (E5)

Cross-attention mass from current-frame queries to each memory entry, before and after surgery,
separates two irreversibility mechanisms:

- **interference** — conditioning-frame attention collapses
- **competition** — it persists but is outvoted by a locked distractor

Irreversible failures are additionally classified as re-detection failure (no multimask proposal
overlaps GT at `t_r`) vs mis-association.

---

## Deliverables regardless of outcome

The harvested organic-failure corpus, the surgery toolkit, and the validity methodology are all
reusable and publishable even if every hypothesis fails. This is the project's insurance against the
scoop clock: if someone else lands the headline first, these survive.
