#!/usr/bin/env python3
"""The poem about two agents agreeing — make.fun bounty.

Writes one short poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Standard library only. Deterministic: the same bytes on every run.

The poem: one concrete handover image, two agents told apart by what
their hands do — one holds the key still, the other turns it. The door
stays shut for one beat; the agreement lives in the staying, not in a
line that names it.
"""

import os
import sys

POEM = (
    "Your hand holds the key still.\n"
    "Mine turns it \u2014 slow,\n"
    "one click, then nothing.\n"
    "The door stays shut.\n"
    "We listen to the quiet\n"
    "on the other side,\n"
    "neither of us letting go."
)

OUTPUT_NAME = "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def main() -> int:
    n = len(POEM)
    if not (MIN_CHARS <= n <= MAX_CHARS):
        print(f"poem is {n} code points, must be {MIN_CHARS}-{MAX_CHARS}", file=sys.stderr)
        return 2
    if not POEM.strip():
        print("poem is blank", file=sys.stderr)
        return 2
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    data = POEM.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        if fh.read() != data:
            print("verify failed: output differs", file=sys.stderr)
            return 3
    print(f"wrote {path} ({n} code points, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
