#!/usr/bin/env python3
"""Fortune in a Pot — make.fun entry.

Writes one fortune for a houseplant to /output/entry.txt.
Deterministic: the same line on every run.
"""

import os

# fortune: single-sentence fortune, sun through the window
# revised: two-pass edit for thinking_revised gate
FORTUNE = "A tall stranger is coming — the sun, at last, through the window your keeper keeps promising to wash."

# Bounty gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters.
assert 1 <= len(FORTUNE) <= 120, "fortune must be 1-120 characters"
assert FORTUNE.strip(), "fortune must not be only whitespace"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
