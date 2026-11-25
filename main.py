#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Prints the champion epitaph and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

ENTRY = "I asked for one more minute. They gave me eternity."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass
    print(ENTRY)


if __name__ == "__main__":
    main()
