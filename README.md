# King Group website

Static website for the King Group, Northwestern University. Content lives in
`content/` as Markdown/YAML and is built into a static site by `build.py`.

- `content/` — everything editable (see `UPDATING.md`)
- `assets/` — CSS, JS, images, CV
- `build.py` — regenerates the pages at the repo root
- `*.html` — generated pages (rebuilt by `build.py`)
- `.github/workflows/deploy.yml` — builds and deploys to GitHub Pages on push

## Deploying
This repo deploys via GitHub Actions. One-time setup: **Settings → Pages → Build
and deployment → Source: "GitHub Actions"**. After that, every push to `main`
rebuilds and publishes the site.

To edit the site, see **`UPDATING.md`**.
