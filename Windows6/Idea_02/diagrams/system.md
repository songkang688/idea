```mermaid
flowchart TB
  D[烟雾帧 + 相机 ID] --> R[随机划分]
  D --> E[按事件划分]
  D --> C[按相机划分]
  R --> T[训练小检测器]
  E --> T
  C --> T
  T --> M[mAP / FAR]
  T --> P[相机 ID 线性探针]
  T --> F[空帧 见过 vs 未见过]
```
