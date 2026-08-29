"""Original Idea_03 prototype entry point, kept for the path already in use.

The implementation moved into the `aligntax` package (W6-T3) so the three eval
modes, the probe and the O1/O2/O3 decision function have one source of truth and
are unit-tested. This file is now a thin shim; `python src/run_smoke.py` is the
same run with more output.

Run: python format_controlled_box.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run_smoke import main

if __name__ == "__main__":
    raise SystemExit(main([]))
