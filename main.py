"""Aica Time Machine Warning - make.fun entry.

Writes a single one-line warning label for a time machine
(120 characters or fewer) to /output/entry.txt.
Python standard library only.
"""

import os

ENTRY = (
    "WARNING: If you arrive before you departed, remain calm. "
    "You already panicked about this yesterday."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 120


def validate(text: str) -> None:
    """Check the entry before writing: non-empty, one line, <= 120 chars."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
