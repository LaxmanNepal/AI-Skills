# Free AI Edge Gallery Skills

A collection of independent, installable AI Edge Gallery skills. Every skill has its own `SKILL.md` and JavaScript runtime under `scripts/index.html`.

## Skills

1. `ultimate-assistant` — all-in-one toolbox
2. `calculator`
3. `weather`
4. `wikipedia`
5. `news-search`
6. `web-search`
7. `currency`
8. `unit-converter`
9. `timezone`
10. `qr-code`
11. `hash`
12. `base64`
13. `json-formatter`
14. `regex-tester`
15. `color-tools`
16. `password-generator`
17. `random-generator`
18. `ip-lookup`
19. `url`
20. `maps`
21. `notes`
22. `pomodoro`
23. `countdown`
24. `tip-calculator`
25. `bmi`
26. `percentage`
27. `date-difference`
28. `text-statistics`
29. `uri-tools`
30. `uuid`

## API key policy

These skills do not require a paid API key. Network-backed skills require internet access and can fail if the device or endpoint blocks requests.

## AI Edge Gallery compatibility

Each JavaScript skill follows the official Agent Skills structure: a root `SKILL.md` and `scripts/index.html` exposing `window['ai_edge_gallery_get_result']`. AI Edge Gallery recommends serving JavaScript skills through a real web host such as GitHub Pages rather than raw GitHub URLs.
