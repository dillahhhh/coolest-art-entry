"""Coolest-art-01 entry (Python 3.13, standard library only).

The art is entry.jpg beside this file: an AI-generated anime-style image
of a samurai facing the full moon and Mt. Fuji under cherry blossoms,
with a pagoda, a torii gate and lanterns. The program copies it to
/output/entry.png.

The gate accepts a PNG or a JPEG at /output/entry.png, told apart by its
first bytes; the name stays entry.png either way. The file is a whole JPEG of 365912 bytes and 1024 by 576 pixels, inside
the 1 MiB and 1024 by 1024 limits.

Deterministic: no network, no randomness, no clock. It copies the same
bytes every run, so two runs write byte-identical output.

Local run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.jpg"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DST = OUT_DIR / "entry.png"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
