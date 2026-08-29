"""Original Idea_01 prototype entry point, kept because README.md points here.

The implementation moved into the `amgclust` package (W6-T3) so that the
metrics have one source of truth and are unit-tested. This file is now a thin
shim; `python src/run_smoke.py` is the same run with more output.

Run: python amg_intensity_equiv.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run_smoke import main

if __name__ == "__main__":
    raise SystemExit(main([]))
