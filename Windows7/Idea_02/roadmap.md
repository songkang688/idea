# Idea_02 — Implementation Roadmap

Zero training, single A100. **Sequence this project first among the three** — its novelty decays
with the calendar in a way the other two do not.

---

## Day 1 — hard dependencies and the gate

- [ ] **Confirm DiDi access** at `go.vicos.si/didi` (academic distribution, linked from DAM4SAM).
      There is no mirror. This is a hard dependency, not a nice-to-have.
- [ ] Clone and pin by commit: `facebookresearch/sam2`, `yangchris11/samurai`,
      `jovanavidenovic/DAM4SAM`, `Mark12Ding/SAM2Long`, `LingyiHongfd/lvos-evaluation`.
- [ ] Request SAM3 tracking-zoo access (gated; lead time is the risk).
- [ ] Verify one SAM2.1 VOS pass end to end on LVOS v2.

---

## Day 2–3 — the surgeon and E0

- [ ] `MemorySurgeon` hooks over the video predictor's inference-state memory dict: delete, keep,
      reinsert, with recency slots made explicit.
- [ ] All six arms.
- [ ] **E0 replay-determinism gate.** The `no-op` arm must reproduce the original failure
      bit-for-bit across repeats. `check_replay_determinism` raises rather than warns.

**Nothing else runs until E0 passes.** If replay is non-deterministic and unfixable, the project is
dead and this is where it should die.

---

## Week 1 — harvest, freeze, pilot

- [ ] **E1 harvest** (~12 GPU-h): LVOS v2 val + DiDi, Hiera-B+ and Hiera-L, fixed protocol, zero
      curation.
- [ ] Report **both** yields: total usable failures, and the H2-testable share (failures shorter
      than the memory horizon). If the second is small, P2 is descoped and the paper says so.
- [ ] **Freeze `configs/preregistration.yaml`**, including the comparator set `C`. This happens
      *before* any comparator runs.
- [ ] **E2 pilot** (~10 GPU-h): 50 failures × 6 arms + partialled regression.

**Gate.** `targeted ≈ sham` ⇒ stop, the instrument is dead. `targeted − reset < 3 pts` **and** pilot
partial `r < 0.2` ⇒ stop before the comparator passes; release corpus and toolkit as a tech note.

---

## Week 2 — full surgery

- [ ] **E3** (~25 GPU-h): ≥200 failures × 6 arms, both backbones, ambiguity strata.
- [ ] **E5** memory-attention logging → interference vs competition taxonomy.
- [ ] **E6** (~15 GPU-h) deletion scope + `t_r ± δ` timing dose–response. This is a **main result**,
      not an ablation.

---

## Week 3 — validity and the headroom table

- [ ] **E4** (~35 GPU-h): comparator passes over the frozen set.
- [ ] Partialled validity: `min_{c ∈ C} partial r`, nested-model ΔR², bootstrap CIs.
- [ ] Cross-ceiling check against SAM2RL's optimisation-derived bound on shared sequences.
- [ ] **The headroom table** — the paper's central artifact: share of the oracle-timed ceiling each
      published memory policy captures.
- [ ] **E8** medical-video arm (~10 GPU-h).

---

## Week 4 — generational arm and release

- [ ] **E7** SAM3 arm (~30 GPU-h): identical protocol on SAM2.1 and SAM3.
- [ ] Release the organic-failure corpus and the surgery toolkit.
- [ ] Paper draft, decomposition-first framing.

---

## Scoop-clock discipline

`KNOWN FACT` This is the fastest-decaying novelty in Windows7.

- **Pre-register and post the protocol early** — before the full results exist. It is the only real
  defence.
- If scooped mid-flight, pivot to the corpus + toolkit + validity methodology, all of which survive
  independently.
- Do not wait for the SAM3 arm to start writing.

---

## Branch points

| Observation | Action |
|---|---|
| E0 non-deterministic and unfixable | **kill** |
| DiDi inaccessible | descope to LVOS v2 + SA-V; report the distractor-density gap |
| <80 usable failures even with SA-V | descope to a bounded pilot report |
| H2-testable share very small | keep P1/P3, descope P2 explicitly |
| `targeted ≈ sham` | **kill the instrument claim**; publish deletion-mechanics note |
| `targeted ≈ reset` | publish as a bounded diagnostic post-mortem |
| partial `r < 0.2` | pre-registered negative + corpus + toolkit |
| all pass | headroom table becomes the subfield's reference artifact |
