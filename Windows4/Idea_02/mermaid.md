# PromptAmnesia — Diagrams (Windows4 / Idea_02)

Epistemic status: DESIGN DIAGRAMS. No results are encoded here.

## 1. Study pipeline with gate decision

```mermaid
flowchart TD
    E0["E0 Pre-registration freeze<br/>grid recipe · matched-gain rule · contrasts O1–O5<br/>gate targets · probe protocol · click simulators<br/>tag: idea02-prereg-v1"]
    E1["E1 P082 GATE (runs FIRST, eval-only)<br/>frozen-model variance decomposition<br/>symmetric threshold protocol<br/>released checkpoints only (MedSAM, SAM-Med2D)"]
    DEC{"Gate decision:<br/>any reproduced delta outside<br/>envelope on ≥2 domains?"}
    PIV["PIVOT — Branch A (deflation paper)<br/>envelope + symmetric re-evals<br/>+ confirmatory coupling regression<br/>(≈5–8 GPU-days total)"]
    E2["E2 Shared FT checkpoint grid (only training)<br/>2 domains × 3 prompt mixes × 4 recipes × ≥3 seeds<br/>+ loss-aggregation cells + covariate logging"]
    MG["Matched-gain selection (§14, single rule)<br/>first checkpoint within ±0.5 Dice of weakest arm's best"]
    E3["E3 P065 battery<br/>box · 1-click · iterative-5 (+neg clicks) · ambiguity<br/>symmetric thresholds · dual click simulators"]
    E4["E4 Diversity arm (C1-061)<br/>oracle best-of-3 vs IoU-head argmax"]
    E5["E5 P177 mechanism arm<br/>module splice × trained stitch × both directions<br/>+ per-module α-interpolation"]
    P5["Phase 5 Analysis + paper<br/>reporting panel appendix (P110 residue)<br/>drift covariate exploratory (P108 residue)"]

    E0 --> E1 --> DEC
    DEC -- "no (all inside envelope)" --> PIV
    DEC -- "yes" --> E2 --> MG --> E3 --> E4 --> E5 --> P5
    E3 --> P5
    PIV --> P5
```

## 2. P065 factorial — coverage vs forgetting separation

```mermaid
flowchart LR
    subgraph FTMIX["FT prompt mix (columns)"]
        BO["box-only<br/>(coverage column)"]
        PO["point-only<br/>(coverage column)"]
        MX["MIXED<br/>(licensing column —<br/>all claims live here)"]
    end
    subgraph BATTERY["Eval battery (rows)"]
        B1["box (jittered)"]
        B2["1-click"]
        B3["iterative-5 incl. negative clicks"]
        B4["multimask ambiguity<br/>(oracle vs argmax)"]
    end
    FTMIX -->|"× recipes {full-FT ×3 LR, decoder-FT, LoRA e+d, VeRA ctrl}<br/>× ≥3 seeds × 2 domains, at matched gain"| BATTERY
    BATTERY --> DELTA["Δ(prompt type) vs frozen-SAM floor<br/>at symmetric tuned thresholds"]
    DELTA --> CVG["box-only / point-only orderings<br/>= COVERAGE MAP (RQ5)"]
    DELTA --> FGT["mixed-column orderings O1–O3, O5<br/>+ envelope + Holm = FORGETTING (H2/H3)"]
```

## 3. Diversity decomposition decision tree (C1-061)

```mermaid
flowchart TD
    P["Ambiguity probe: 3 candidates + IoU-head scores<br/>≥2 valid GT masks per prompt"]
    Q1{"Oracle best-of-3<br/>drops after FT?<br/>(all-mask-loss cells included)"}
    Q2{"Argmax drops?"}
    Q3{"Drop only in<br/>min-loss-mask cells?"}
    CAP["CAPABILITY LOSS<br/>diversity-forgetting claim stands (H4)"]
    RNK["RANKING LOSS<br/>transfer to P031 (IoU-head desync);<br/>withdrawn from this paper"]
    ART["LOSS-AGGREGATION ARTIFACT<br/>reported as recipe finding, not forgetting"]
    NUL["No diversity effect —<br/>reported as null"]

    P --> Q1
    Q1 -- yes --> Q3
    Q3 -- yes --> ART
    Q3 -- no --> CAP
    Q1 -- no --> Q2
    Q2 -- yes --> RNK
    Q2 -- no --> NUL
```

## 4. P177 splice/stitch grid

```mermaid
flowchart TD
    subgraph MODULES["Module groups (swapped one at a time)"]
        M1["image encoder"]
        M2["prompt encoder"]
        M3["decoder cross-attention"]
        M4["decoder-rest + heads"]
    end
    subgraph CONTROLS["Controls per cell"]
        C1["both swap directions<br/>(pre-FT→FT and FT→pre-FT)"]
        C2["± trained affine stitch<br/>(capacity-capped, 2 pre-registered families)"]
        C3["stitch-only calibration cells"]
        C4["α-interpolation per group<br/>α ∈ {0,.25,.5,.75,1}"]
        C5["update-norm accounting +<br/>norm-matched FT arm"]
    end
    MODULES --> R["Restoration fraction R per cell, per prompt type<br/>R = (chimera − FT) / (frozen − FT), bootstrap CIs"]
    CONTROLS --> R
    R --> V{"cross-attn+stitch ≫ encoder+stitch,<br/>both directions, beyond α-curve?"}
    V -- yes --> H5Y["H5 stands: locus at mechanism grade"]
    V -- no --> H5N["Locus claim withdrawn;<br/>grid + α-curves reported descriptively"]
```

## 5. Portfolio interfaces and execution order

```mermaid
flowchart LR
    P082["P082 gate<br/>(this package, runs first)"]
    GRID["Shared checkpoint grid<br/>(pre-registered, frozen)"]
    P065["P065 battery + C1-061 diversity<br/>(this package, flagship)"]
    P031["P031 IoU-head desync / calibration<br/>(sibling paper)"]
    P177["P177 mechanism arm<br/>(this package)"]
    P110["P110 residue:<br/>reporting panel appendix"]
    P108["P108 residue:<br/>drift covariate log (free)"]

    P082 --> GRID --> P065 --> P177
    GRID --> P031
    P065 -- "ranking-loss branch of O4" --> P031
    P065 --- P110
    GRID --- P108
```
