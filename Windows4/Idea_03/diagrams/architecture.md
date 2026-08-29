# AlphaSmoke — architecture-level diagram

Companion diagrams: full experiment overview in `../proposal.md` §6; pre-registered
decision tree in `../experiments.md` §3.

```mermaid
flowchart LR
    subgraph INPUT["Input"]
        RGB["RGB image / sequence"]
        BG["Pre-smoke background frames<br/>(fixed camera, exposure-locked)"]
    end

    subgraph FLOORS["Training-free floors (B6)"]
        HSV["HSV low-chroma rule<br/>baselines/color_hsv.py"]
        DC["Dark-channel transmission<br/>baselines/dark_channel.py"]
    end

    subgraph ENCODERS["Frozen / fine-tuned encoders (one ViT-B, init varies)"]
        EM["init: matting (arm M)"]
        EMB["init: matting-binarized (arm MB, B1)"]
        ES["init: COCO-seg (arm S / S+cal, B7)"]
        E0["init: scratch/ImageNet (arm 0)"]
    end

    HEAD["Shared light alpha head (~2-3M params)<br/>or 1x1-conv linear probe (week-1)"]
    SOFT["Soft map in [0,1]"]
    THR["Frozen operating threshold tau_op<br/>(matched to released eval code)"]

    subgraph SCORING["Scoring (metrics/)"]
        BIN["Binary: IoU, Dice, F-beta, mMse, boundary-F"]
        ALP["Alpha: MAE, SAD, MSE, Grad, Conn"]
        TAUM["tau matrix + top-3 reversals<br/>rank_agreement.py"]
    end

    ALPHAGT["Alpha GT sources:<br/>synthetic DS01-03 (secondary, circular)<br/>MEASURED real alpha (B3):<br/>alpha_recovery/background_inversion.py"]
    RATERS["Rater masks x3-5<br/>rater/ceiling.py (B5)"]

    RGB --> HSV & DC --> SOFT
    RGB --> EM & EMB & ES & E0 --> HEAD --> SOFT
    SOFT --> THR --> BIN
    SOFT --> ALP
    BG --> ALPHAGT
    RGB --> ALPHAGT
    ALPHAGT --> ALP
    BIN --> TAUM
    ALP --> TAUM
    RATERS -->|"ceiling bounds certifiable deltas"| TAUM
```

Scope guard (B10): no fire/smoke detector appears anywhere in this graph — SAM-class
models enter only as scored checkpoints in automatic/grid-point mode.
