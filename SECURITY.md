# Security Policy

## Scope

This repository contains Agent Skills and small JavaScript runtimes intended for AI Edge Gallery. Skills should minimize permissions, avoid unnecessary data collection, and never embed secrets.

## Reporting a vulnerability

Please do not publish sensitive exploit details in a public issue. Report security problems privately through the repository's available GitHub security reporting channel, when enabled, or contact the repository maintainer through their GitHub profile.

Include:

- affected skill and file
- impact
- reproduction steps
- suggested mitigation, if known

## Security principles

- Never commit API keys, tokens, passwords, cookies, or private credentials.
- Validate and constrain untrusted input.
- Prefer local computation when network access is unnecessary.
- Clearly document network-backed behavior.
- Do not request permissions that are not required for the skill.
- Avoid dynamic code execution from untrusted input.
- Return controlled JSON errors instead of leaking sensitive runtime details.
