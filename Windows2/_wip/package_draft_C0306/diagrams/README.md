# Diagrams — C-0306

Mermaid sources (render with any mermaid-compatible viewer; all three are also referenced from
`../proposal.md`):

- `architecture.mmd` — system architecture: modules 1–5, the gate decision, and where the synthetic
  generator stands in for the real candidate-cache harvester (proposal §8–9).
- `pipelines.mmd` — the four internal coverage pipelines A–D side by side, including pipeline B's
  silent-loss path and pipeline C's q̂ = +∞ achievability certificate (proposal §9 table, §10).
- `decision_gate.mmd` — the pre-registered gate/stop/pivot logic with the standing clocks
  (proposal §17, §25; `../roadmap.md`).

The prototype's own module-level diagram (code-accurate, file-by-file) lives with the original
prototype at `Windows2/_wip/stage7_proto_C0306/ARCHITECTURE.md`; the code copied into `../src/`
is identical except for three path adjustments documented in `../src/README.md`.
