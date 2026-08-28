# Architecture — B-0114 4-arm dense-task prototype

## Dataflow

```mermaid
flowchart TB
    subgraph DATA["synthetic_data.py"]
        GEN["scene generator<br/>rectangles of C classes<br/>+ global illumination g"]
        GEN --> TRAINSET["train / val scenes<br/>(per seed, deterministic)"]
        GEN --> PAIRED["paired scenes<br/>same layout, resampled g"]
    end

    subgraph PRETRAIN["train.py :: pretrain_backbone (per backbone variant, per seed)"]
        OBJ["GLOBAL-ONLY objectives:<br/>g regression + class presence"]
        POOLFREE["register_free:<br/>pool over PATCH tokens<br/>(global leak built in)"]
        POOLREG["register_equipped:<br/>pool over REGISTER slots<br/>(patch tokens stay clean)"]
        OBJ --- POOLFREE
        OBJ --- POOLREG
        POOLFREE --> FREEZE["freeze backbone"]
        POOLREG --> FREEZE
    end

    TRAINSET --> PRETRAIN

    subgraph ARMS["train.py :: train_arm (x4 mandated + optional sink_only)"]
        A1["arm 1 frozen_random<br/>K random tokens, never trained"]
        A2["arm 2 learned<br/>tokens + head trained (VPT-shallow)"]
        A3["arm 3 learned_frozen<br/>arm-2 tokens frozen, fresh head"]
        A4["arm 4 no_token<br/>dense readout baseline"]
        A5["(extra) sink_only<br/>keys trainable, values = 0"]
        A2 -- "tokens copied verbatim" --> A3
    end

    FREEZE --> VIT

    subgraph MODEL["tiny_vit.py"]
        VIT["TinyViT (frozen)<br/>seq = [prompt | register | patch]"]
        HEAD["DenseHead (shared class)<br/>linear per-patch or conv decoder<br/>reads PATCH tokens only"]
        VIT --> HEAD
    end

    ARMS -- "prompt params owned by arm" --> VIT
    TRAINSET --> ARMS
    HEAD --> LOGITS["per-pixel logits -> mIoU"]

    subgraph READOUT["metrics.py — the paper's main table"]
        DEC["gain decomposition (seed-wise, telescoping):<br/>insertion = arm1 - arm4<br/>content = arm3 - arm1<br/>co-adapt = arm2 - arm3<br/>total = arm2 - arm4<br/>sink geometry = arm5 - arm4"]
        H2["H2 directional readout:<br/>gain(free) vs gain(equipped)"]
    end
    LOGITS --> DEC
    LOGITS --> H2

    subgraph SIG["signatures.py — mechanism axes (HYPOTHESES)"]
        S1["geometry: sink mass of<br/>patch queries on prompt/register slots"]
        S2["embedding: token norm ratios,<br/>patch-norm outlier fraction<br/>(signatures ONLY, no error link)"]
        S3["invariance breaking:<br/>patch-feature displacement<br/>under paired g-swap"]
    end
    VIT -- "captured attention" --> S1
    VIT --> S2
    PAIRED --> S3

    subgraph B0001["b0001_hook.py — QUARANTINED"]
        HK["norm-map vs per-patch error AUROC<br/>flag-gated: --with-b0001-hook<br/>no B-0114 module imports it"]
    end
    LOGITS -. "only if flag passed" .-> HK
```

## Module map

| module | role | key invariants (tested) |
|---|---|---|
| `synthetic_data.py` | scenes + global nuisance g; paired-g renders | deterministic per (seed, split); paired renders share layout; g moves pixels |
| `tiny_vit.py` | ViT-tiny, slot layout `[prompt\|register\|patch]`, sink mode, dense heads | value-zeroing matches reference impl; linear head strictly per-patch; forward never mutates backbone params |
| `train.py` | global-only pretraining; per-arm training | backbone frozen & bit-identical across arms; `frozen_random` tokens equal their init; `learned_frozen` reuses arm-2 tokens verbatim |
| `metrics.py` | mIoU, decomposition, H2 | decomposition telescopes exactly seed-wise; H2 needs both backbones |
| `signatures.py` | sink mass, norm signatures, nuisance sensitivity | sink mass 0 without tokens, bounded by 1; sensitivity 0 on identical renders |
| `b0001_hook.py` | quarantined B-0001 seam | AUROC correct on known cases; import isolation + flag gating enforced by AST tests |
| `config.py` | YAML + validation | `learned_frozen` requires `learned`; geometry synced data↔model |
| `run_synthetic.py` | orchestration, EXPECTED vs MEASURED report | arm order guarantees `learned` before `learned_frozen`; JSON dump reproducible |

## Design invariants

1. **The backbone is arm-independent.** Prompt parameters are owned by the
   arm; `train_arm` never touches backbone weights (asserted per state-dict
   key in tests). The decomposition is meaningless without this.
2. **One head class for every arm** (linear or conv, per config) so head
   capacity cannot masquerade as a token effect; the head reads patch
   tokens only — prompt/register slots are never visible to the readout.
3. **The decomposition telescopes by construction**:
   insertion + content_transfer + co_adaptation = total VPT gain, seed-wise.
4. **Hypotheses stay hypotheses.** The runner prints EXPECTED (pre-registered
   from exp_01) and MEASURED (synthetic) in separate blocks; H2 confirmation
   lines are tagged as sandbox mechanism checks.
5. **B-0001 quarantine** (PI binding): no import path from B-0114 modules to
   `b0001_hook.py`; hook output only under an explicit flag and banner.
