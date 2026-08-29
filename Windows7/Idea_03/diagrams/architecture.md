# Idea_03 — The Grid, the Matching, and the Gate

No new model. The "architecture" is the experimental design: five training streams, one matching
convention, and a decision rule that has to be committed before any of it runs.

---

## 1. The training pipeline

```mermaid
flowchart LR
    MIX["llava_v1_5_mix665k"] --> STRIP["strip the text-only<br/>ShareGPT slice"]
    STRIP --> BASE["text-stripped multimodal mix"]
    BASE --> MATCH["token-budget re-matching<br/>all arms on one total"]

    C4[("C4 / curated text")] --> ARM{"arm"}
    ARM -->|A0| R0["(no rehearsal stream)"]
    ARM -->|A1| R1["curated text"]
    ARM -->|A2| R2["random web docs"]
    ARM -->|A3| R3["same docs, tokens permuted<br/>within each document"]
    ARM -->|A4| R4["one document, repeated"]

    MATCH --> TRAIN["LLaVA-1.5-7B fine-tune<br/>1 text batch per 9 multimodal"]
    R0 --> TRAIN
    R1 --> TRAIN
    R2 --> TRAIN
    R3 --> TRAIN
    R4 --> TRAIN

    TRAIN --> THETA["theta_a"] --> EVAL["stratified eval<br/>fluency / knowledge / reasoning /<br/>instruction + VL sanity"]
```

`A0` carries no rehearsal stream, so it draws **more** multimodal tokens to reach the same total.
Without that re-match, `A0` is simply the shortest run and every arm difference is contaminated by
training length.

---

## 2. What each arm destroys

```mermaid
flowchart TD
    A1["A1 curated<br/>content + syntax + diversity"] -->|"remove curation"| A2["A2 random web<br/>content + syntax + diversity"]
    A2 -->|"permute tokens"| A3["A3 shuffled<br/>keeps unigram stats + length<br/>destroys syntax and content"]
    A2 -->|"collapse to one doc"| A4["A4 single doc<br/>keeps content + syntax<br/>destroys diversity"]
    A1 --- A0["A0 none<br/>forgetting floor"]
```

`A3` vs `A2` isolates syntax from lexical statistics. `A4` vs `A2` isolates diversity from content.
These two contrasts are the contribution; `A2` alone would produce an ambiguous result.

---

## 3. Gradient matching

```mermaid
flowchart LR
    T["text batch"] --> G["per-block gradient norms<br/>on the language tower"]
    REF["reference arm norms"] --> G
    G --> P["PRIMARY: per-layer<br/>lambda_l = ||g_ref_l|| / ||g_txt_l||"]
    G --> S["SECONDARY: global norm<br/>one lambda for the whole tower"]
    P --> LR["log effective-LR multiplier<br/>stability risk, not a free operation"]
    S --> SENS["E3 sensitivity analysis"]
```

Per-layer is primary because modality-specific gradients differ by orders of magnitude across layers
(`arXiv:2606.17296`), so a global scalar can report a clean match while individual blocks remain badly
mismatched. Naming the primary in advance is what stops "the conventions diverged" from being a
result in every possible world.

---

## 4. Gates and the decision rule

```mermaid
flowchart TD
    E0["E0 reproduce published recipe<br/>measure base scores"] -- fail --> K0["stop: harness untrustworthy"]
    E0 --> DEN{"per-stratum denominator adequate?<br/>headroom >= 0.10, snr >= 3"}
    DEN -- no --> REP["replace the stratum NOW,<br/>before any arm runs"]
    DEN -- yes --> FREEZE["FREEZE preregistration:<br/>MDE, strata, primary convention, eval YAMLs"]
    REP --> FREEZE

    FREEZE --> E0B["E0b: is A3 degenerate?"]
    E0B -- degenerate --> DROP["drop A3; A4 still separates diversity"]
    E0B -- ok --> E1
    DROP --> E1["E1 power gate<br/>A0/A1/A2 x 2 seeds"]

    E1 --> P0{"Abs(A1) - Abs(A0) > max(2 sd, MDE)<br/>on knowledge AND fluency?"}
    P0 -- no --> STOP["STOP at ~800 A100-h.<br/>Publish the power analysis:<br/>it bounds how large forgetting really is."]
    P0 -- yes --> E2["E2 full grid, A0-A4 x 3 seeds"]

    E2 --> R{"decompose per capability"}
    R -->|"balance >= 0.8 x total on >=3 of 4"| P1["P1 MECHANISM<br/>curation budgets are misdirected"]
    R -->|"Ret(A2) <= Ret(A0) everywhere"| P2["P2 CONTENT<br/>first controlled refutation of<br/>pseudo-rehearsal in this regime"]
    R -->|"knowledge content>0.5, fluency<0.2"| P3["P3 STRATIFIED<br/>fund E4 dosing sweep"]
```

---

## 5. The effect decomposition

```
total-effect(c)   = Ret(c, A1) - Ret(c, A0)      what rehearsal buys
balance-effect(c) = Ret(c, A2) - Ret(c, A0)      what ANY text-shaped gradient buys
content-effect(c) = Ret(c, A1) - Ret(c, A2)      what the curation buys
```

Reported in absolute score points (co-primary) as well as ratios, with bootstrap CIs over seeds. The
shares `balance/total` and `content/total` are **not computed** for any capability whose total effect
falls below the declared MDE: dividing by a gap the power analysis just called indistinguishable from
zero produces a share that swings on seed noise alone.
