"""scripts/figures/ にある図のスクリプトをすべて実行する。

    uv run scripts/figures/build_all.py           # すべて
    uv run scripts/figures/build_all.py sample    # 名前に sample を含むものだけ
"""

import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

pattern = sys.argv[1] if len(sys.argv) > 1 else ""
for script in sorted(HERE.glob("*.py")):
    if script.name in {"figstyle.py", "build_all.py"} or pattern not in script.stem:
        continue
    print(f"run: {script.name}")
    runpy.run_path(str(script), run_name="__main__")
