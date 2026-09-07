# Laxman Ultimate AI Edge Gallery Skill

One AI Edge Gallery Agent Skill that bundles practical search, news, weather, Wikipedia, web-page extraction, calculations, conversions, developer utilities, generators, productivity helpers, maps and safe communication links.

## Main capabilities

Search • News • Weather • Wikipedia • Page reader • Calculator • Currency • Units • Time zones • QR • Hash • Base64 • JSON • Regex • Colors • Passwords • Random • IP • URLs • Maps • Notes • Pomodoro • Countdown • Tip • BMI • Percentages • Date difference • Text statistics • URI encoding • UUID.

Most local functions need no API key. Network features use public endpoints and depend on network/CORS availability.

## Install

Google AI Edge Gallery requires a JS skill to expose `window['ai_edge_gallery_get_result']`, and its documentation recommends true web hosting such as GitHub Pages for JS assets plus `.nojekyll` so `SKILL.md` remains directly readable.

After GitHub Pages is enabled, the intended skill URL is:

`https://laxmannepal.github.io/Ambition/`

In AI Edge Gallery: Agent Skills → + → Load skill from URL → paste the URL above.

If Pages is not enabled yet, use the local folder import method instead.

## Design

This is deliberately one skill, but internally it routes requests by an `action` JSON field. It does not silently send SMS/email/WhatsApp; it returns safe links where applicable.
