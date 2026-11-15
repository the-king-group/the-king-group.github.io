# King Group website

Static website for the King Group, Northwestern University. Content lives in
`content/` as Markdown/YAML and is built into a static site by `build.py`.

- `content/` - everything editable (see `UPDATING.md`)
- `assets/` - CSS, JS, images, CV
- `build.py` - regenerates the pages at the repo root
- `*.html` - generated pages (rebuilt by `build.py`)
- `scholar_sync.py` - adds new papers from Google Scholar
- `.github/workflows/update.yml` - syncs, rebuilds and commits every Monday
  and on every push; GitHub Pages then publishes the result

To edit the site, see **`UPDATING.md`**.
