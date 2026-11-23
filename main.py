#!/usr/bin/env python3
"""Write the 23 Nov 2026 world-news image to /output/entry.png.

Deterministic, no network: copies the bundled entry.png byte-for-byte,
so both runs write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
shutil.copyfile(SRC, DST)
os.chmod(DST, 0o644)
print("wrote", DST)
