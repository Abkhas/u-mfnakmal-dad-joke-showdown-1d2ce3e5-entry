#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Writes one dad joke, at most 200 characters, to /output/entry.txt.
Stdlib only. The joke is a single line; the punchline lands at the end.
"""

import os
import sys

LINE = "My daughter asked where the water goes when it drains away. I said, 'Down to see the world,' and she said, 'Dad, that's the deepest thing you've ever said.'"

MAX_CHARS = 200


def main() -> int:
    line = LINE.strip()
    if not line or len(line) > MAX_CHARS:
        print(f"invalid entry: {len(line)} chars (must be 1..{MAX_CHARS})",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("invalid entry: must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = "out"
        os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    # Verify what we wrote: UTF-8, single line, 1..200 chars.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n" or len(line) > MAX_CHARS:
        print("verification failed", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
