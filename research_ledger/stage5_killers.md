# Stage 5 — Killer experiments (auditor Top-8)

Source: bc-41b96f8f-f888-5f68-a593-4fca1505017f
Engineer Top-5: (1) Constrained SAM-FT (2) Frozen/tuned n* (3) 0085-M lesion suppression (4) 0074-M calibration-under-shift (5) Interactive eval merge.

Cut by engineer: 0046-M (GT scarcity), 0252 (soft kill in sim), 0275 contamination (engineering/confound).

SUPERVISOR CORRECTION: 0276-M shape-prior field was omitted from this Stage-5 prompt (R2 ranked it #1, inference-only killer). Must add back before locking Top-5.

Likely final-3 pool:
- Constrained SAM-FT
- 0085-M lesion suppression
- 0276-M prior-shape interpolation (pending design)
- 0252 if cheap killer exists
- Interactive eval only if not "just a benchmark paper" for the archival packages
