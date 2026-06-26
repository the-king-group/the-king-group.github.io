# King Group — website

Static website for the King Group, Northwestern University.
Built as plain HTML/CSS/JS — no build step required to deploy.

## Structure
- `index.html`, `research.html`, `publications.html`, `people.html`,
  `news.html`, `join.html` — the pages
- `assets/css/style.css` — design system
- `assets/js/site.js` — self-assembly hero animation + mobile nav
- `assets/img/` — headshot images
- `assets/king-cv-2026.pdf` — downloadable CV
- `build.py` — regenerates the HTML pages from shared header/footer +
  content (optional; run `python3 build.py` after editing content there)

## Deploy (GitHub Pages)
This repo is named `kinggroup.github.io`, so GitHub Pages serves it from
the repository root on the `main` branch automatically. Push the files to
`main` and the site goes live at https://kinggroup.github.io.

## Editing
- People, talks, news, and publications are defined as lists in `build.py`.
  Edit there and re-run `python3 build.py`, or edit the generated `.html`
  files directly.
