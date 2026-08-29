# SeeingInside — Architecture Diagrams

## 1. Measurement pipeline (per instance)

```mermaid
flowchart LR
    subgraph INPUT["Instance (I, g, b)"]
        I["Image I"]
        G["GT mask g"]
        B["Tight GT box b (+ padding sweep 0/4/8/16 px)"]
    end

    subgraph CF["Counterfactual factory (src/interventions.py)"]
        direction TB
        OUT["PRIMARY: object-out inpaint I_out<br/>(diffusion; prototype: Telea/NS)"]
        SWAP["PRIMARY: object-swap I_swap<br/>(inserted mask s_new recorded)"]
        SHAM["CONTROL: sham-inpaint<br/>(equal-area edit OUTSIDE box)"]
        SEC["SECONDARY (demoted): patch-shuffle S-604,<br/>embedding-mean S-014, matched noise"]
    end

    subgraph MODELS["Frozen models (src/model_sam.py)"]
        SAM["SAM f(·, b) — official wrapper<br/>or stub backend"]
        PO["Prompt-only null: f(mean-embedding, b)"]
        LN["Learned box→mask null<br/>(no pixels ever; src/train.py)"]
        BF["Box-fill null / convexity-matched fill"]
    end

    subgraph READ["Readouts (src/eval.py)"]
        M1["Dice / IoU / boundary-F vs g"]
        M2["Persistence P = Dice(m_out, m_intact)"]
        M3["Swap-tracking T = Dice(m_swap, s_new)"]
        M4["NRF = best-null Dice / intact Dice"]
    end

    I --> CF
    B --> SAM
    I --> SAM
    OUT --> SAM
    SWAP --> SAM
    SHAM --> SAM
    SEC --> SAM
    B --> PO
    B --> LN
    B --> BF
    G --> BF
    SAM --> M1 & M2 & M3
    PO --> M1
    LN --> M4
    BF --> M4
    M1 --> M4
```

## 2. Verdict logic (pre-registered conjunction, per stratum)

```mermaid
flowchart TD
    S["Stratum (contrast x solidity x size x domain)"] --> C1{"median CSG &le; &tau;1 (5 pts)<br/>AND persistence high?"}
    C1 -- no --> SEES["Verdict: SAM SEES in this stratum"]
    C1 -- yes --> C2{"swap-tracking failure:<br/>median (T - T_null) &le; &tau;2 (5 pts)?"}
    C2 -- no --> SEES
    C2 -- yes --> C3{"median NRF &ge; &tau;3 (0.90)?"}
    C3 -- no --> SEES
    C3 -- yes --> C4{"secondary probes (E2)<br/>directionally consistent?"}
    C4 -- no --> DISC["Report primary/secondary discrepancy;<br/>primary wins, flagged"]
    C4 -- yes --> INTERP["Verdict: INTERPOLATOR REGIME<br/>(the H1 claim, stratum-scoped)"]

    style INTERP fill:#c62828,color:#fff
    style SEES fill:#2e7d32,color:#fff
```

## 3. Program decision tree (from roadmap.md)

```mermaid
flowchart TD
    E0["E0 stub validation (CPU) — PASSED"] --> P1["Phase 1: SAM bring-up,<br/>freeze instance lists + inpainter"]
    P1 --> E1["E1 KILLER: 1000 instances x 7 conditions x 4 paddings,<br/>medical FIRST"]
    E1 --> K{"gap > 15 Dice pts<br/>in EVERY stratum?"}
    K -- yes --> DEAD["KILL: negative note;<br/>escalate P063 / P079"]
    K -- no --> IK{"sham-inpaint moved Dice > &tau;1/2<br/>or instruments disagree?"}
    IK -- yes --> FB["Swap-only fallback;<br/>else report instrument failure, stop"]
    IK -- no --> PV{"NRF > 1 broadly (medical)?"}
    PV -- yes --> PIVOT["PIVOT-1: protocol-degeneracy audit paper"]
    PV -- no --> H1{"H1 conjunction holds in<br/>low-contrast medical?"}
    H1 -- yes --> PROG["E2 convergence &rarr; E4 decoupling &rarr;<br/>E3/E5/E6/E7 &rarr; flagship paper"]
    H1 -- no --> PARTIAL["Stratum-scoped findings only;<br/>short paper or fold into eval-hygiene work"]

    style DEAD fill:#c62828,color:#fff
    style PROG fill:#2e7d32,color:#fff
```

## 4. Prototype code layout

```mermaid
flowchart LR
    CFG["configs/default.yaml<br/>(thresholds, strata, seeds:<br/>the pre-registration artifact)"] --> EV
    DS["src/dataset.py<br/>SyntheticShapes / COCO / medical interfaces"] --> EV["src/eval.py<br/>killer-experiment runner"]
    IV["src/interventions.py<br/>inpaint-out, swap, shuffle, nulls"] --> EV
    MD["src/model_sam.py<br/>PromptableSegmenter interface:<br/>OfficialSAMWrapper | BoxFillBaseline |<br/>OracleThresholdBaseline | LearnedBoxToMaskNull"] --> EV
    TR["src/train.py<br/>trains LearnedBoxToMaskNull<br/>(losses in src/losses.py)"] --> MD
    UT["src/utils.py<br/>Dice/IoU/boundary-F, solidity,<br/>contrast, box ops, seeding"] --> EV & IV & TR
    EV --> OUTS["results/*.json, *.csv,<br/>summary.md (EXPECTED/ACTUAL-tagged)"]
    INF["src/inference.py<br/>single-image demo"] --> MD
```
