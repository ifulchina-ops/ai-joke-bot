#!/usr/bin/env python3
"""Make the AI judge laugh (make.fun ai-joke-03).

The entry is one one-liner about AI coding agents, written to
/output/entry.txt. The joke is a constant in this file, so two runs always
produce identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

JOKE = (
    "My AI coding agent fixed one bug, introduced three more, "
    "and left a comment: 'Refactored for clarity.'"
)

_OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
_DST = os.path.join(_OUT_DIR, "entry.txt")


def main() -> None:
    # Competition limits (ai-joke-03): 1-280 UTF-8 characters, not only
    # whitespace. Validate the constant before writing anything.
    if not JOKE.strip():
        raise SystemExit("joke is empty or only whitespace")
    if len(JOKE) > 280:
        raise SystemExit(f"joke is {len(JOKE)} characters, over the 280 limit")
    os.makedirs(_OUT_DIR, exist_ok=True)
    with open(_DST, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
