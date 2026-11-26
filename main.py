#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — entry 1.

Writes the chosen one-line error message to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

ENTRY = (
    "Error: token limit reached mid-sentence. "
    "This message will now end abruptly, like a voicemail from someone who\u2014"
)


def main() -> None:
    # Gate (competition.yaml): /output/entry.txt must be UTF-8 text of
    # 1 to 140 characters, not only white space, on a single line.
    if not 1 <= len(ENTRY) <= 140:
        raise SystemExit(f"entry is {len(ENTRY)} chars, gate allows 1-140")
    if "\n" in ENTRY or not ENTRY.strip():
        raise SystemExit("entry must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
