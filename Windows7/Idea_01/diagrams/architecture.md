# Idea_01 — Protocol and Data Flow

There is no model architecture in this project. The "architecture" is the measurement apparatus,
so these diagrams show the intervention and the decision rule instead of a network.

---

## 1. The counterfactual, per episode

```mermaid
flowchart LR
    subgraph IN["Episode (frozen before inference)"]
        S["Correct support<br/>(I_s, M_s) of class c"]
        Q["Query I_q<br/>GT mask M_q"]
        W["Wrong supports S'<br/>2 near + 3 far<br/>classes verified ABSENT from Q<br/>area matched ±50%"]
    end

    S --> F1["f(S, Q)"]
    W --> F2["f(S', Q)"]
    Q --> F1
    Q --> F2
    Q --> G["Support-free floor g(Q)<br/>Floor-A: SAM AMG (strong)<br/>Floor-B: saliency (weak)"]

    F1 --> A1["a_corr = IoU(pred, M_q)"]
    F2 --> A2["a_wrong = median over S'"]
    F1 --> V["insensitivity<br/>IoU(pred_wrong, pred_corr)"]
    F2 --> V
    G --> A3["a_floor"]

    A1 --> R["retention R = a_wrong / a_corr"]
    A2 --> R
    R --> SSS["SSS = 1 - R"]
    A1 --> FT["floor test:<br/>CI overlap of a_corr and a_floor"]
    A3 --> FT
```

The floor is computed **once per query image** and reused across every method in the panel, which is
where most of the compute saving comes from.

---

## 2. Stratification — the part that separates two different indictments

```mermaid
flowchart TD
    E["Episode with query Q, class c"] --> D{"Degenerate benchmark?<br/>(FSS-1000)"}
    D -- yes --> S4["S4 degenerate control<br/>high retention here indicts the BENCHMARK"]
    D -- no --> C{"Any annotated instance<br/>of a class ≠ c in Q?"}
    C -- yes --> S3["S3 distractor present<br/>PRIMARY STRATUM<br/>high retention here indicts the MODEL"]
    C -- no --> M{"≥2 instances of class c?"}
    M -- yes --> S2["S2 multi-object same class"]
    M -- no --> S1["S1 single object<br/>saliency prior cannot be wrong here"]
```

`S3` is primary because it is the only stratum where "segment the salient thing" and "segment the
class the support names" are forced to disagree. Every prior discussion of foreground bias conflates
`S1` and `S3`; this design does not.

---

## 3. Decision rule

```mermaid
flowchart TD
    MVE["MVE (~1 A100-day)<br/>PFENet + BAM + Matcher + 1 foundation-era method<br/>PASCAL-5i f0, COCO-20i f0"]
    MVE --> GATE{"any R > 0.35 on any stratum<br/>OR family gap > 15 pts?"}
    GATE -- no --> DIE["No-go. Idea dies for 1 A100-day.<br/>Release harness."]
    GATE -- yes --> KILLER["Killer experiment (~2 A100-days)<br/>on stratum S3"]

    KILLER --> LA{"leg (a)<br/>≥ half of specialists retain R > 0.5"}
    KILLER --> LB{"leg (b)<br/>a_corr indistinguishable from floor<br/>reported per floor, never pooled"}

    LA -- pass --> H["HEADLINE:<br/>sensitivity-adjusted leaderboard reorders"]
    LB -- pass --> H
    LA -- fail --> BOTH{"both legs failed?"}
    LB -- fail --> BOTH
    BOTH -- yes --> CERT["CERTIFICATION result published instead<br/>(weakest branch, priced as such)"]

    H --> S4C{"S4 high but S3 low?"}
    S4C -- yes --> BENCH["PIVOT: benchmark paper.<br/>Distractor-enriched split is the deliverable."]
    S4C -- no --> PAPER["Model-level indictment"]
```

---

## 4. Statistics pipeline

```mermaid
flowchart LR
    EP["per-episode measurements"] --> TAU["pre-registered filter<br/>a_corr ≥ τ (τ=0.2 frozen)"]
    TAU --> P["PRIMARY estimator<br/>ratio of means<br/>Σ a_wrong / Σ a_corr"]
    TAU --> M["SECONDARY estimator<br/>median of per-episode ratios"]
    P --> B["episode bootstrap B=10,000<br/>numerator and denominator resampled<br/>on identical indices"]
    M --> B
    B --> FLAG{"|primary - secondary| > 0.2?"}
    FLAG -- yes --> BI["flag: bimodal episodes<br/>= hard failure mode, reported as a finding"]
    FLAG -- no --> OK["graceful degradation"]
```

**Why the primary estimator is not a median.** Per-episode retention is bimodal: under a wrong
support a method either lands on the correct object or it does not, so `R(e)` piles up near 0 and
near 1. A median over that distribution is a coin flip on which pile is larger. In the prototype run
the fully support-driven control scored median retention 1.000 — identical to a support-blind
method — while its ratio of means was 0.762 [0.651, 0.871]. See `proposal.md` §10.
