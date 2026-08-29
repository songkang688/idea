# Idea_02 — Experiment cards

> **STATUS OF EVERY CARD: NOT RUN**, except E0, which runs on a synthetic
> corpus and can only validate the harness. **No detector has been trained.**
> Windows6 has **zero ACTUAL RESULTS** and no smoke mAP. Budgets are
> **HYPOTHESIS**; predicted trends are **EXPECTED RESULT**.
>
> **E-A blocks everything.** GATE-A (`stage6_battle.md` §5) is open: it has
> never been verified that camera metadata exists on any public smoke set, and
> Idea_02's own first stop rule is *"Kill if no camera metadata."*

## Card index and execution order

| Card | Name | Gate it decides | Budget (HYPOTHESIS) | Status |
|---|---|---|---|---|
| **E-A** | **GATE-A: camera-ID inventory** | Does this project exist? | **0 — no GPU** | **NOT RUN — BLOCKING** |
| **E0** | Harness validation (synthetic, CPU) | Is H2 even expressible in code? | ~0, CPU seconds | **RUN — PASS** |
| **E1** | **KILLER**: 1 seed × 3 protocols + probe + empty-frame FPR | H1, H2, H3, H4 | ≈10 GPU-h | NOT RUN |
| **E2** | 3 seeds, event-clustered CIs | H1/H2 with confidence | ≈30 GPU-h | NOT RUN |
| **E3** | Probe control on an ImageNet backbone | H3 specificity | ≈1 GPU-h | NOT RUN |
| **E4** | pHash dedup rerun | duplicates vs camera signature | ≈10 GPU-h | NOT RUN |
| **E5** | Second dataset | generality | ≈30 GPU-h | NOT RUN |

Order: **E-A → E0 → E1 → E2 → E4**, with **E3 runnable in parallel** with E1
(it needs no detector training, only a frozen ImageNet backbone) and E5 last.

---

## E-A — GATE-A: camera-ID inventory — STATUS: NOT RUN, BLOCKING

**Purpose.** Establish that the project's subject matter exists. Everything
below is void without it.

**Input.** Public metadata for PYRONEAR-2025 (arXiv 2402.05349, **VERIFIED
PRIOR WORK**) and FIgLib (`CITATION NEEDED — 待人工核验`). Dataset cards,
directory structure, filename conventions, any accompanying CSV.

**Procedure.**

1. Determine whether a per-frame camera identifier exists — explicit field,
   derivable from the path, or absent.
2. If derivable rather than explicit, **document the derivation rule** and spot
   check it against at least 20 frames by eye. A guessed camera ID silently
   corrupts every split downstream.
3. Count distinct cameras. Count events per camera. Count empty/no-smoke frames
   per camera — H4 needs negatives from **both** seen and unseen cameras.
4. Write the counts into this card. That written inventory *is* the artifact
   that closes GATE-A.

**Decision thresholds.**

| Observation | Action |
|---|---|
| ≥10 cameras, IDs explicit or reliably derivable, empty frames present on both sides | **GATE-A CLOSES** → E0/E1 |
| ≥10 cameras but no empty-frame pool | **H4 is unrunnable** on this set → find another or accept that the paper collapses to domain shift (§20.1 of `proposal.md` calls that fatal) |
| 1–9 cameras | **PIVOT** to event-disjoint only. This **forfeits H2**, the distinguishing claim; Idea_02 must be re-argued for its Final-3 slot before any GPU is spent |
| No camera metadata on any usable set | **KILL Idea_02** by its own stop rule |

**Cost.** Hours of desk work. **No GPU.**

**Why it is first.** Idea_02 is the most expensive member of the Final 3 per
unit of evidence — it is the only one that requires training. Spending ≈10
GPU-h before confirming the data supports the question is the single most
avoidable failure mode in this package.

---

## E0 — Harness validation (synthetic, CPU) — STATUS: RUN, PASS

**Purpose.** Confirm the three protocols have the overlap structure the
hypothesis requires. If event-disjoint and camera-disjoint were the same thing
in code, H2 would not be expressible and no real run would be worth starting.

**Input.** `data.make_corpus` — a synthetic corpus with camera ⊃ event ⊃ frame
structure, a planted camera signature and an empty-frame pool. Not images, not
embeddings.

**Run.**

```bash
python Idea_02/src/run_smoke.py --seed 0
python -m unittest discover -s Idea_02/tests
```

**Decision threshold.** `run_smoke.py` exits non-zero unless:

| Protocol | Cameras shared | Events shared |
|---|---|---|
| random | > 0 | > 0 |
| event_disjoint | **> 0** | **0** |
| camera_disjoint | **0** | 0 |

The middle row is the whole hypothesis in one line: holding out episodes leaves
the towers behind.

**Two protocol defects this card caught during W6-T3.** Both would have produced
a publishable-looking but wrong result:

1. **The camera-ID probe was evaluated on a random split.** With the camera
   signature switched off entirely, it still beat chance by ≈0.17 — it was
   naming the camera by recognising the fire *episode* shared across the split,
   not the tower. H3 must be evaluated **event-disjoint**. Both directions are
   now pinned by self-checks, so the rule cannot be dropped.
2. **The empty-frame comparison had no seen-camera side.** Restricting empties
   to the test split puts all of them on the unseen side under a camera-disjoint
   protocol, and the seen-camera FPR came out `nan`. Fixed: the detector trains
   on non-empty frames only, so *all* empty frames are held out and can be
   partitioned purely by whether their camera was seen.

**What E0 does NOT show.** Nothing about real smoke data. The camera signature
was planted by `make_corpus`; any leakage it finds is leakage we inserted. The
synthetic H4 gap comes out ≈0, which is a property of a linear stand-in on
planted features and **not** a prediction.

---

## E1 — KILLER: three protocols, one seed — STATUS: NOT RUN

**Requires GATE-A closed.**

**Input.** PYRONEAR-2025 subsample with camera IDs. Equal-N, class-ratio-matched
test sides across all three protocols.

**Arms.** YOLOv8n (`CITATION NEEDED — 待人工核验`), one seed, trained separately
under random / event-disjoint / camera-disjoint.

**Measurements.**

1. Image-level **AP** and **FAR@recall 0.8** per protocol.
2. **Camera-ID linear probe** on frozen backbone features, **evaluated
   event-disjoint**, reported against the majority-class chance level.
3. **Empty-frame FPR**, seen versus unseen cameras. Detector trained on
   non-empty frames only.
4. Camera and event overlap counts per protocol, reported alongside — so a
   reader can verify the protocols are what they claim.

**Decision thresholds.**

| Observation | Action |
|---|---|
| camera-disjoint AP < random AP, gap > seed std | **H1 supported** → E2 |
| event-disjoint AP strictly between random and camera-disjoint | **H2 supported** → E2 |
| event-disjoint ≈ camera-disjoint | **KILL** — PYRONEAR already solved it |
| probe margin over chance ≈ 0 | **KILL H3**; the representation carries no camera identity |
| seen-camera empty FPR > unseen, consistent in direction | **H4 supported** — the key result |
| no empty-frame gap | **Fatal to the framing** (`proposal.md` §20.1) — the paper is domain shift, which is not news |

**Budget.** ≈10 GPU-h (**HYPOTHESIS**, from `evolution_summary.md`).

---

## E2 — Three seeds and honest confidence intervals — STATUS: NOT RUN

**Purpose.** H1 and H2 are gaps between numbers, so they are only as good as
the intervals around them.

**Procedure.** Repeat E1 with 3 seeds per protocol. Report bootstrap CIs
resampled over **events**, never over frames.

**Why the clustering matters.** Consecutive frames of one plume from one tower
are heavily correlated. A frame-level bootstrap treats them as independent and
reports an interval several times too narrow — the specific way an audit like
this overstates its own confidence. `metrics.cluster_bootstrap_ci` only offers
the clustered version; there is no frame-level option to reach for.

**Decision thresholds.**

| Observation | Action |
|---|---|
| H1 and H2 gaps survive with CIs excluding 0 | **CONTINUE** to E4 |
| Gaps inside seed noise **and** probe ≈ chance **and** no empty-FPR gap | **STOP** — confirm with 2 further seeds before declaring |
| Gaps survive but CIs are very wide | Add seeds before adding claims |

**Budget.** ≈30 GPU-h (**HYPOTHESIS**).

---

## E3 — Probe control on an ImageNet backbone — STATUS: NOT RUN

**Purpose.** Decide whether camera identity is something the *smoke detector*
learned, or just generic scene identity that any vision backbone would carry.

**Procedure.** Repeat the H3 probe on a frozen ImageNet-pretrained backbone that
has never seen smoke data. Same event-disjoint evaluation.

**Decision thresholds.**

| Observation | Interpretation |
|---|---|
| Detector backbone probe ≫ ImageNet probe | The detector *learned* camera identity — the strong reading |
| Both probes high and similar | Any backbone encodes scene identity. H3 survives but weakens: it shows the information is *available*, not that the detector exploits it. Report honestly |
| Both at chance | **KILL H3** |

**Budget.** ≈1 GPU-h (**HYPOTHESIS**). Cheap, parallelisable with E1, and it
pre-empts an obvious reviewer question.

---

## E4 — pHash dedup rerun — STATUS: NOT RUN

**Purpose.** Separate near-duplicate frames from camera signature. This is the
confound the Voxel51 blog identified, and if the whole gap is duplicates then
the paper restates the blog with numbers.

**Procedure.** Deduplicate with pHash (`CITATION NEEDED — 待人工核验`), rebuild
all three splits on the deduplicated corpus, rerun E1.

**Decision thresholds.**

| Observation | Action |
|---|---|
| Gap survives dedup | **CONTINUE** — camera signature, not duplicates. The strongest form of the result |
| Gap disappears after dedup | **DOWNGRADE** to a near-duplicate audit |
| Gap shrinks but survives | Report both numbers side by side; attribute the share |

**Budget.** ≈10 GPU-h (**HYPOTHESIS**).

---

## E5 — Second dataset — STATUS: NOT RUN

**CONTINUE** requires H1 and H4 on ≥2 datasets (`proposal.md` §20). Candidates:
FIgLib, SmokeFrames, Nemo — all subject to their own GATE-A inventory first.
If only one dataset has camera IDs, scope the title to that dataset explicitly
rather than implying generality. Budget ≈30 GPU-h (**HYPOTHESIS**).

---

## Cross-cutting rules

1. **GATE-A first.** No GPU spend before the camera inventory is written down.
2. **The probe is always event-disjoint.** A random-split probe measures event
   memorisation; the harness demonstrated this at zero camera signature.
3. **Empty frames are never trained on.** Both sides of H4 must be held out
   under identical conditions.
4. **CIs cluster over events.** Never over frames.
5. **Report the overlap counts.** Every table states cameras-shared and
   events-shared per protocol, so a reader can check the protocols are real.
6. **Never cite an inflation number we did not compute.** Standing instruction
   from `literature.md`: the Voxel51 audit is a blog diagnosis with no retrained
   mAP, and must be described that way.
7. **Budgets stay HYPOTHESIS.** The ≈10 GPU-h figure is an estimate from
   `evolution_summary.md`, never a measurement.
