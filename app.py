"""
Entry point for the submodule demo.

math_lib and log_lib are git submodules inside this repo (flat packages).
This script imports them and runs a tiny workflow.
"""

from __future__ import annotations

import sys
from pathlib import Path

# This directory must be on sys.path so that
# `import math_lib` / `import log_lib` resolve to ./math_lib and ./log_lib.
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main() -> int:
    """Run a short demo that uses both libraries when available."""
    try:
        from math_lib import add, average, clamp
        from log_lib import LogLevel, get_logger
    except ImportError as exc:
        print("Libraries are not available as submodules yet.")
        print(f"Import error: {exc}")
        print()
        print("Expected layout:")
        print("  main_module/math_lib/   (submodule)")
        print("  main_module/log_lib/    (submodule)")
        print("Run: git submodule update --init --recursive")
        return 1

    log = get_logger("main_module", LogLevel.DEBUG)
    log.info("Submodule demo starting")

    values = [2, 4, 6, 8]
    mean = average(values)
    total = add(mean, 10)
    bounded = clamp(total, 0, 12)

    log.debug(f"values={values}")
    log.info(f"average={mean}, average+10={total}, clamped={bounded}")
    log.warning("This is only a demo warning — everything is fine.")
    log.info("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
