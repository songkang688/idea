# RetainSAM architecture

```mermaid
flowchart LR
  subgraph train [Train step]
    Xt[Target image + GT] --> SAM_S[Student SAM θ]
    Xr[COCO replay image] --> SAM_S
    Xr --> SAM_T[Frozen teacher θ0]
    SAM_T -->|prompted pseudo-mask| Lret[Retention DiceCE]
    Xt -->|GT mask| Ltgt[Target DiceCE]
    Ltgt --> L[L = Ltgt + λ Lret]
    Lret --> L
  end
  subgraph eval [Eval — no grad]
    SAM_S --> Jt[Target Dice]
    SAM_S --> Jg[Click/box suite on COCO/LVIS]
    Theta0[θ0] --> Wise[WiSE-FT α-grid]
    Naive[θ_naive] --> Wise
    Wise --> Pareto[Pareto plot Jt vs Jg]
    Jt --> Pareto
    Jg --> Pareto
  end
```

```
Weight interpolation (kill-switch baseline):
  θ(α) = (1-α) θ_SAM + α θ_naive

Constraint (what we claim is not equivalent):
  min_θ  L_tgt(θ)  s.t.  J_gen(θ) ≥ J_gen(θ0) - ε
  implemented as replay distillation + optional λ ramp.
```
