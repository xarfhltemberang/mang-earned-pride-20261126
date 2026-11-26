#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride, in one concrete scene, with no
trailing newline.

The line: after nine months of physiotherapy, a father climbs the
porch steps alone, and his child finally keeps both hands in their
pockets instead of hovering at his back. The effort is inside the
scene (nine months of physio, the steps, the hovering), the pride
arrives at the last word, and there is no trophy, podium, or
graduation in sight.
"""

import os

ENTRY = (
    "After nine months of physio, Dad climbed the porch steps alone, "
    "and for the first time my hands stayed in my pockets instead of "
    "hovering at his back."
)


def main() -> None:
    # Gate assertions, matching the kit exactly:
    # 1-240 characters, a single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 240, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
