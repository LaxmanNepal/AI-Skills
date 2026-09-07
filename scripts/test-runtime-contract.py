#!/usr/bin/env python3
"""Fast static smoke tests for every packaged skill runtime."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "free-skills"
errors = []
for skill in sorted(p for p in ROOT.iterdir() if p.is_dir()):
    html = skill / "scripts" / "index.html"
    if not html.exists():
        continue
    text = html.read_text(encoding="utf-8", errors="replace")
    checks = [
        ("handler", r"window\.ai_edge_gallery_get_result\s*=\s*async"),
        ("JSON output", r"JSON\.stringify"),
        ("error path", r"error|catch"),
    ]
    for label, pattern in checks:
        if not re.search(pattern, text, re.I):
            errors.append(f"{skill.name}: missing {label} contract")

if errors:
    print("Runtime contract failures:")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"Runtime contract smoke tests passed for {len(list(ROOT.glob('*/scripts/index.html')))} skills")
