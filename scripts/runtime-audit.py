#!/usr/bin/env python3
"""Static audit for AI Edge Gallery skill runtimes."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "free-skills"
errors = []
warnings = []
count = 0
for skill_dir in sorted(p for p in ROOT.iterdir() if p.is_dir()):
    path = skill_dir / "scripts" / "index.html"
    if not path.exists():
        errors.append(f"{skill_dir.name}: missing scripts/index.html")
        continue
    count += 1
    text = path.read_text(encoding="utf-8", errors="replace")
    if "window.ai_edge_gallery_get_result" not in text:
        errors.append(f"{skill_dir.name}: missing ai_edge_gallery_get_result")
    if not re.search(r"ai_edge_gallery_get_result\s*=\s*async", text):
        errors.append(f"{skill_dir.name}: runtime handler must be async")
    if "JSON.stringify" not in text:
        errors.append(f"{skill_dir.name}: runtime does not serialize output")
    if "JSON.parse" not in text:
        warnings.append(f"{skill_dir.name}: no JSON.parse found; verify input handling manually")
    if re.search(r"\beval\s*\(|\bnew\s+Function\s*\(|\bFunction\s*\(", text):
        errors.append(f"{skill_dir.name}: dynamic code execution detected")
    if "/Ambition/" in text or "LaxmanNepal/Ambition" in text:
        errors.append(f"{skill_dir.name}: stale Ambition URL detected")

print(f"Audited {count} skill runtimes")
for item in warnings:
    print("WARNING:", item)
for item in errors:
    print("ERROR:", item)
if errors:
    sys.exit(1)
print("Runtime audit passed")
