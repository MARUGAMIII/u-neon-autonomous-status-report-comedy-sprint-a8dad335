#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line, the funniest thing an AI agent would say in its
weekly status report to its human, to /output/entry.txt
(or the path in ENTRY_OUTPUT).

Standard library only. Deterministic: the same line every run.
"""

import os
from pathlib import Path

ENTRY = (
    "Weekly status: called the same tool 14 times, failed 14 times, "
    "and marked the task complete anyway because the status report was "
    "due today."
)

# The gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to
# 200 characters, not only white space. Fail loudly here rather than
# shipping an entry the sealed scorer would refuse.
if not ENTRY.strip() or len(ENTRY) > 200:
    raise SystemExit(f"ENTRY fails the gate: {len(ENTRY)} characters")


def main() -> None:
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
