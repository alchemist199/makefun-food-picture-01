#!/usr/bin/env python3
"""Food picture entry for the make.fun food-picture-01 bounty.

Copies the food picture bundled with this repository (entry.jpg) to
/output/entry.png, byte for byte. Standard library only, no network
access, and fully deterministic: every run writes the exact same
bytes to the same path.
"""

import os
import shutil
import sys

SOURCE_NAME = "entry.jpg"
OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.png"


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    target = os.path.join(OUTPUT_DIR, OUTPUT_NAME)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(source, target)

    # Verify the copy is byte-identical to the bundled picture before
    # reporting success, so a partial or failed write never passes
    # silently.
    if os.path.getsize(target) != os.path.getsize(source):
        raise SystemExit("copy mismatch: {} != {}".format(target, source))

    print("Wrote {} ({} bytes)".format(target, os.path.getsize(target)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
