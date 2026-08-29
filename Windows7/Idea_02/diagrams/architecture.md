# Idea_02 — Surgery, Arms, and the Decision Rule

No weights are modified anywhere in this project. The "architecture" is a wrapper over SAM2's
inference-state memory bank plus the experimental design around it.

---

## 1. Where the surgeon sits

```mermaid
flowchart LR
    subgraph SAM2["SAM2.1 video predictor (frozen)"]
        ENC["image encoder"] --> MA["memory attention"]
        MA --> DEC["mask decoder"]
        BANK[("memory bank<br/>conditioning frame m0 (permanent)<br/>recent FIFO entries (recency-encoded)<br/>object pointers")]
        BANK <--> MA
        DEC --> W["memory encoder writes new entry"]
        W --> BANK
    end
    SURG["MemorySurgeon<br/>delete / keep / reinsert<br/>NO weights touched"] -.operates on.-> BANK
```

---

## 2. The six arms

```mermaid
flowchart TD
    F["failure state at t_r<br/>bank = m0 + pre-error entries + post-error (corrupted) entries"]

    F --> N["no_op<br/>nothing"]
    F --> T["targeted<br/>drop entries written in [t_f, t_r)<br/>keep m0 + pre-error"]
    F --> R["reset<br/>keep m0 only"]
    F --> S["sham<br/>drop count-matched PRE-ERROR entries<br/>leave corruption in place"]
    F --> SC["slot_control<br/>targeted, then refill vacated<br/>recency slots with pre-error duplicates"]
    F --> RK["random_k<br/>count-matched random deletion"]

    T -.->|"beats?"| N
    T -.->|"H2: pre-error memory is load-bearing"| R
    T -.->|"H3: it is the content, not the motions"| S
    SC -.->|"does slot occupancy still matter?"| T
    RK -.->|"does it matter WHICH entries?"| T
```

`sham` is the vacuous control — same incision, nothing therapeutic removed. Implementing the
Stage-6 wording literally would have produced an arm that also removes the corruption, making
"targeted beats sham" unpassable by construction; that version is kept separately as `slot_control`.

---

## 3. The structural bound on H2

```mermaid
flowchart LR
    A["failure lasts t_r - t_f frames"] --> B{"t_r - t_f < bank capacity?"}
    B -- yes --> C["pre-error entries survive in the bank<br/>targeted ≠ reset<br/>H2 IS testable"]
    B -- no --> D["FIFO already flushed everything pre-error<br/>targeted == reset (same operation)<br/>H2 is NOT testable on this failure"]
```

The share of the corpus on the left branch bounds how much of the harvest can speak to H2 at all. It
is reported at E1, before any P2 claim. In the prototype run it was 23 of 50 simulated failures.

**P2 is read on the left branch only.** Right-branch failures contribute an exact zero to the
`targeted − reset` gap, so pooling them dilutes a real effect rather than measuring a smaller one: in
the prototype a genuine +0.130 subset gap pooled to +0.040, below the pre-registered 0.10 bar, in the
world where the decomposition is real. The pooled figure is reported alongside and labelled diluted.

---

## 4. Decision rule

```mermaid
flowchart TD
    E0["E0 replay-determinism gate<br/>no_op must reproduce the original failure bit-for-bit"]
    E0 -- fail --> KILL0["KILL. Arm differences would be harness noise."]
    E0 -- pass --> E1["E1 harvest (fixed protocol, zero curation)<br/>report total yield AND H2-testable yield"]
    E1 --> E2["E2 pilot: 50 failures x 6 arms<br/>+ partialled regression  (~10 GPU-h)"]

    E2 --> G1{"targeted ≈ sham?"}
    G1 -- yes --> KILL1["KILL. Effect is deletion mechanics,<br/>not memory content."]
    G1 -- no --> G2{"targeted - reset < 3 pts<br/>AND pilot partial r < 0.2?"}
    G2 -- yes --> KILL2["STOP before comparator passes.<br/>Release corpus + toolkit as tech note."]
    G2 -- no --> E3["E3/E4 killer experiment (~60 GPU-h)"]

    E3 --> K1{"P1 ≥30 vs no_op<br/>P2 ≥10 vs reset<br/>P3 ≥10 vs sham"}
    E3 --> K2{"min over frozen comparator set<br/>partial r > 0.4"}
    K1 -- fail --> NEG["Pre-registered negative.<br/>Corpus + toolkit still published."]
    K2 -- fail --> NEG
    K1 -- pass --> WIN
    K2 -- pass --> WIN["Headroom table:<br/>how much failure is memory-borne, and<br/>what share each policy actually captures"]
```

---

## 5. The validity design (attack A1)

```mermaid
flowchart LR
    D["sequence difficulty<br/>distractor density, occlusion,<br/>failure count, no-op recovery"]
    D --> RHO["reversible fraction ρ"]
    D --> G["prevention-method gain g_c"]
    RHO -.->|"the claim we want to test"| G

    RHO --> P1["residual of ρ after regressing on X"]
    G --> P2["residual of g_c after regressing on X"]
    P1 --> PC["partial r = corr(residuals)"]
    P2 --> PC
    PC --> MIN["min over FROZEN comparator set C<br/>threshold 0.4"]
```

Difficulty drives **both** `ρ` and `g_c`, so the naive correlation is inflated by a path that has
nothing to do with instrument validity. In the prototype, naive correlations of 0.952 / 0.918 /
0.859 became partial correlations of 0.682 / 0.397 / 0.028. Freezing `C` and reporting the minimum is
what prevents the 0.028 comparator from being dropped after the fact.
