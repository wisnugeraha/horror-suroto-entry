#!/usr/bin/env python3
"""Two-Sentence Horror — entry for make.fun u-suroto-two-sentence-horror.

Writes a two-sentence horror story to /output/entry.txt.
Gate: 1..400 chars, non-blank, UTF-8. House judge compares two-sentence
stories pairwise; restraint and implied horror over gore.
"""
import os
import sys

STORY = (
    "The hospital called this morning to say the bed had been emptied out overnight, "
    "which is strange, because I was the only one in it — my sister checked on me "
    "at four, and she has been dead for six years."
)
MAX = 400
OUT = "/output/entry.txt"


def emit(story: str, out: str = OUT) -> None:
    if not (1 <= len(story) <= MAX) or not story.strip():
        sys.exit(f"story failed gate ({len(story)} chars, blank={not story.strip()})")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(story + "\n")


def confirm(out: str = OUT) -> None:
    with open(out, "rb") as f:
        data = f.read()
    text = data.decode("utf-8").rstrip("\n")
    if text != STORY:
        sys.exit(f"confirm failed: disk has {text[:40]!r}, expected {STORY[:40]!r}")


def main() -> None:
    emit(STORY)
    confirm(OUT)


if __name__ == "__main__":
    main()
