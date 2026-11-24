#!/usr/bin/env python3
"""Write the alien field note line to /output/entry.txt."""

import os

TEXT = "Field note, day two: they keep their dead in stone gardens and their living in small boxes, and visit both on Sundays. Three stars. The soup alone justifies the trip."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
