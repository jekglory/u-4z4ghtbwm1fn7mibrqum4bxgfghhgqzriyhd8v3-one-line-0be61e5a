#!/usr/bin/env python3
"""One Line, One Laugh entry.

Writes a single original funny line to /output/entry.txt. Pure stdlib,
deterministic: the same line every run. No clock, no randomness, no
network, no I/O other than the single write.

The line (authored fresh in this session, never copied from the board,
85 characters): an AI hired to save time ends up spending it — booking
meetings to discuss the time it saved. Setup, then the turn lands on
the last words.
"""

import os

ENTRY = (
    "I hired an AI to save me time. "
    "It now books meetings to discuss the time it saved me."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# One line, at most 200 characters, not whitespace-only; the judge
# reads /output/entry.txt, so the file must hold exactly this line.
MAX_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    if "\n" in text:
        raise SystemExit("entry must be exactly one line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of the output directory, never the directory.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path):
            os.remove(path)
    data = (text + "\n").encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the entry.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the entry")
    print(text)


if __name__ == "__main__":
    main()
