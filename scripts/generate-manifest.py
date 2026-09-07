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
    required = {"schema_version", "name", "repository", "pages_base", "skills"}
    missing = required - set(data)
    if missing:
        print("Manifest missing fields:", sorted(missing))
        return 1
    if not isinstance(data["schema_version"], int) or data["schema_version"] < 1:
        print("Invalid schema_version")
        return 1
    if not isinstance(data["skills"], list):
        print("skills must be an array")
        return 1
    actual = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    listed = sorted(item.get("id", "") for item in data["skills"])
    if actual != listed:
        print("Manifest mismatch")
        print("Missing from manifest:", sorted(set(actual) - set(listed)))
        print("Stale in manifest:", sorted(set(listed) - set(actual)))
        return 1
    seen_names = set()
    for item in data["skills"]:
        for field in ("id", "name", "description", "category", "path"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                print(f"Missing/invalid {field} for skill {item.get('id', '<unknown>')}")
                return 1
        if item["id"] in seen_names:
            print(f"Duplicate skill ID: {item['id']}")
            return 1
        seen_names.add(item["id"])
        expected = f"{item['id']}/"
        if item["path"] != expected:
            print(f"Invalid path for {item['id']}: {item['path']}")
            return 1
        if not (SKILLS / item["id"] / "SKILL.md").is_file():
            print(f"Missing SKILL.md: {item['id']}")
            return 1
    print(f"Manifest is consistent: {len(listed)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
