# Contributing to Laxman AI Skills

Thanks for helping improve the collection.

## Add a skill

Create a new folder under `free-skills/<skill-id>/` with:

```text
free-skills/<skill-id>/
├── SKILL.md
└── scripts/
    └── index.html
```

### SKILL.md requirements

- Use YAML frontmatter with `name` and `description`.
- Explain what the skill does.
- Tell the model when and how to call `run_js`.
- Document the expected JSON input and JSON output.
- Document errors and network/API requirements.
- Keep secrets out of the skill and repository.

### JavaScript runtime requirements

For executable skills, expose:

```js
window.ai_edge_gallery_get_result = async input => {
  // parse input, perform the operation, return a JSON string
};
```

Return a JSON string with a predictable shape such as `{ "result": ... }` or `{ "error": "..." }`.

## Manifest

Add the skill to `free-skills/manifest.json`. The CI manifest check must pass.

## Local validation

Run:

```bash
python3 scripts/validate-skills.py
python3 scripts/generate-manifest.py
```

## Pull requests

Keep changes focused, describe how the skill was tested, and do not commit API keys, tokens, passwords, private URLs, or personal data.
