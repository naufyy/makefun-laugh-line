#!/usr/bin/env python3
"""The Monthly Plant - one funny line for make.fun (u-email-baru-make-the-judge-laugh-in-one-line-791ccb21).

Writes the entry to /output/entry.txt. Gate: 1-200 UTF-8 characters.
"""
from pathlib import Path

ENTRY = "I bought a plant that only needs water once a month. It died in three weeks, and the care card now sits on my desk as a tiny obituary I wrote myself."


def main():
    # Write exactly the judged text, no trailing newline: the gate counts
    # characters, so the file must hold the entry and nothing else.
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
