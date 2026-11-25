#!/usr/bin/env python3
"""One Line of Earned Pride (make.fun).

Writes the entry -- One line: a quiet, earned moment of pride for someone in a scene --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "After eleven years of night shifts, she watched her daughter cross the graduation stage in the nurse's uniform she had once ironed for her — and finally let herself believe the tired years had added up to something."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
