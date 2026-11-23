#!/usr/bin/env python3
"""Copy the bundled world-news image to /output/entry.png.

Deterministic and offline: the same bundled bytes are written on every
run, so repeated runs produce byte-identical output.
"""
import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(script_dir, "entry.png")
target_path = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
shutil.copyfile(source_path, target_path)
os.chmod(target_path, 0o644)
if os.path.getsize(target_path) != os.path.getsize(source_path):
    raise RuntimeError("entry.png copy is incomplete: size mismatch")
print("wrote", target_path)
