import sys
from pathlib import Path

# Package layout: tests/ lives inside src/ next to conformal_nms and
# run_synthetic.py, so parents[1] is the src directory itself.
SRC = Path(__file__).resolve().parents[1]
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
