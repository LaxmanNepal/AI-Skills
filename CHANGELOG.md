# Changelog

## 2.0.0 — Runtime Contract v2

- Hardened the calculator runtime by replacing dynamic `Function()` evaluation with an explicit expression parser.
- Added runtime static auditing for all packaged skills.
- Added deterministic runtime contract smoke tests.
- Added a consolidated GitHub Actions quality gate.
- Added a reusable skill documentation template.
- Added scalable architecture guidance for 100+ skills.
- Added a project `VERSION` marker.

The 30 existing installable skills remain independently packaged under `free-skills/`.
