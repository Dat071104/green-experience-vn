import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
runpy.run_path(str(ROOT / "test_suite.py"), run_name="__main__")
