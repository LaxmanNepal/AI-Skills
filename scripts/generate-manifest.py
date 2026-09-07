#!/usr/bin/env python3
"""Validate the committed skill manifest against free-skills directories."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "free-skills"
MANIFEST = SKILLS / "manifest.json"


def main():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    actual = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    listed = sorted(item["id"] for item in data.get("skills", []))
    if actual != listed:
        print("Manifest mismatch")
        print("Missing from manifest:", sorted(set(actual) - set(listed)))
        print("Stale in manifest:", sorted(set(listed) - set(actual)))
        return 1
    for item in data["skills"]:
        expected = f"{item['id']}/"
        if item.get("path") != expected:
            print(f"Invalid path for {item['id']}: {item.get('path')}")
            return 1
        if not (SKILLS / item["id"] / "SKILL.md").is_file():
            print(f"Missing SKILL.md: {item['id']}")
            return 1
    if len(listed) != len(set(listed)):
        print("Duplicate skill IDs in manifest")
        return 1
    print(f"Manifest is consistent: {len(listed)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
