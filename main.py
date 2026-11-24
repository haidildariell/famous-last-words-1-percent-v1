#!/usr/bin/env python3
"""Famous last words of a phone at 1% battery.

Writes a single line to /output/entry.txt, with no trailing newline.
Standard library only; no network, no external files.
"""

import os

LINE = "If anyone asks, I died at 100%. I have a reputation to protect."

MIN_CHARS = 1
MAX_CHARS = 199


def validate(text):
    length = len(text)
    if not MIN_CHARS <= length <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, length)
        )


def main():
    validate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
