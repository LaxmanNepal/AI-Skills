# AI-Skills Architecture

## Runtime contract v2
Every installable skill is a self-contained directory under `free-skills/<skill-id>/` with:

- `SKILL.md` — agent-facing metadata and invocation instructions.
- `scripts/index.html` — sandbox runtime exposing `window.ai_edge_gallery_get_result`.
- JSON input/output — successful calls return `{result: ...}` and failures return `{error: ...}`.

Runtimes should be deterministic, dependency-light, and avoid dynamic code execution such as `eval` and `Function`.

## Marketplace contract
`free-skills/manifest.json` is the catalog source. Stable skill IDs are folder names. Marketplace URLs are derived from the GitHub Pages base plus the skill path. Descriptions should be short, accurate, and installation-oriented.

## CI layers
1. Metadata validation checks frontmatter, names, descriptions, duplicate IDs, and stale repository URLs.
2. Runtime audit checks the JS bridge, JSON serialization, async contract, and dangerous dynamic execution.
3. Runtime smoke tests enforce the common output/error contract.
4. Manifest validation checks the catalog against the physical skill folders.

## Scaling from 30 to 100+
Use stable IDs, one folder per skill, category metadata, deterministic local utilities where possible, and explicit network/privacy documentation for web-backed skills. New skills should not require changes to the marketplace UI: add the folder, update the manifest, and let CI validate it.

Recommended categories include search, productivity, developer, data, finance, communication, media, education, utilities, and device automation.

## Security model
Treat skill runtimes as untrusted inputs. Do not embed credentials. Validate all user-provided strings. Prefer explicit parsers over dynamic evaluation. Network-backed skills should clearly disclose external requests. CI must fail on obvious dynamic code execution or stale repository references.
