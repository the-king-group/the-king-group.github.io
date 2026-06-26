# Updating the King Group website

You don't edit HTML. Everything comes from the plain-text files in **`content/`**.
Edit those (on GitHub or locally), and the site rebuilds and republishes itself.

## Where things live

| To change… | Edit this file |
|---|---|
| Homepage intro, headline, departments + links, affiliations, contacts, PhD program links | `content/site.yml` |
| The Research page write-up | `content/research.md` |
| People (you + group members) | `content/people.yml` |
| News items | `content/news.yml` |
| The Join page intro text | `content/join.md` |
| The publication list | `content/publications.yml` (see below - usually automatic) |

Images live in `assets/img/`.

## Publications - automatic from Google Scholar

The publication list and the "Recent publications" box on the Research page are
kept up to date automatically from your Google Scholar profile. You don't have to
touch `publications.yml`.

**One-time setup** (about two minutes):
1. Create a free key at <https://serpapi.com/> (sign up, then copy your API key).
2. In this repo: **Settings → Secrets and variables → Actions → New repository
   secret**. Name it `SERPAPI_KEY`, paste the key, save.

That's it. Every Monday (and on every push) a GitHub Action pulls your latest
Scholar publications, rebuilds the site, and publishes it. Until you add the key,
the site simply keeps the current list - nothing breaks.

- The number of papers shown on the Research page is `recent_count:` in
  `content/site.yml` (currently 4).
- Your Scholar profile is set by `scholar_id:` in `content/site.yml`.
- **Prefer to manage the list by hand instead?** Delete the "Sync publications"
  step in `.github/workflows/deploy.yml`, then edit `content/publications.yml`
  directly. Each entry looks like:
  ```yaml
  - authors: "King, E. M.*, Coauthor, A. B."
    title: The title of the paper
    venue: Journal Name 1, 234567
    year: 2026
    editor_suggestion: true     # optional badge
    link: https://doi.org/...    # optional
  ```
  (`*` marks co-first authors, `†` corresponding; your name is bolded
  automatically.)

## Common tasks

**Add a news item** - top of `content/news.yml`:
```yaml
- date: Mar 3, 2026
  text: Our paper was featured as an Editor's Suggestion.
```

**Add a group member** - under `members:` in `content/people.yml`:
```yaml
  - name: New Person
    role: Graduate Student in Materials Science & Engineering
    email: person@u.northwestern.edu
    photo: assets/img/new-person.jpg   # upload to assets/img/ first
```
Leave out `photo:` to show a letter monogram instead.

## Previewing locally (optional)

```bash
pip install pyyaml markdown
python build.py        # regenerates the .html pages
```
Then open `index.html` in a browser.
