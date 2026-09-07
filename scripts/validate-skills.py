#!/usr/bin/env python3
"""Validate Google AI Edge Gallery Agent Skills in free-skills/."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "free-skills"


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None, "missing YAML frontmatter"
    end = text.find("\n---", 4)
    if end == -1:
        return None, "unterminated YAML frontmatter"
    data = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return None, f"invalid frontmatter line: {line}"
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key:
            data[key] = value.strip('"\'')
    return data, None


def validate():
    errors = []
    warnings = []
    dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir()) if SKILLS.exists() else []

    if not dirs:
        errors.append("free-skills/ contains no skill directories")

    names = set()
    for skill in dirs:
        rel = skill.relative_to(ROOT).as_posix()
        md = skill / "SKILL.md"
        if not md.is_file():
            errors.append(f"{rel}: missing SKILL.md")
            continue

        text = md.read_text(encoding="utf-8")
        front, err = parse_frontmatter(text)
        if err:
            errors.append(f"{rel}: {err}")
            continue
        for field in ("name", "description"):
            if not front.get(field, "").strip():
                errors.append(f"{rel}: frontmatter missing {field}")

        skill_name = front.get("name", "").strip()
        if skill_name in names:
            errors.append(f"{rel}: duplicate skill name '{skill_name}'")
        names.add(skill_name)

        js = skill / "scripts" / "index.html"
        if js.exists():
            js_text = js.read_text(encoding="utf-8", errors="replace")
            if "run_js" not in text:
                errors.append(f"{rel}: JS skill SKILL.md does not instruct the model to use run_js")
            if "ai_edge_gallery_get_result" not in js_text:
                errors.append(f"{rel}: scripts/index.html missing ai_edge_gallery_get_result")
            if "JSON.stringify" not in js_text and "JSON.parse" not in js_text:
                warnings.append(f"{rel}: runtime has no obvious JSON serialization/parsing")

        combined = text + (js.read_text(encoding="utf-8", errors="replace") if js.exists() else "")
        if re.search(r"/Ambition(?:/|\\b)", combined, re.IGNORECASE):
            errors.append(f"{rel}: contains stale /Ambition/ repository URL")

    print(f"Validated {len(dirs)} skill directories")
    if warnings:
        print(f"Warnings: {len(warnings)}")
        for item in warnings:
            print(f"  ⚠ {item}")
    if errors:
        print(f"Errors: {len(errors)}")
        for item in errors:
            print(f"  ✗ {item}")
        return 1
    print("All skills passed structural validation.")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
