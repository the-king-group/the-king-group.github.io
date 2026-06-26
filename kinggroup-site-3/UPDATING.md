# Updating the King Group website

You don't need to touch any HTML. Everything on the site is generated from the
plain-text files in the **`content/`** folder. Edit those on GitHub, commit, and
the site rebuilds and republishes itself automatically (usually within a minute).

## Where things live

| To change… | Edit this file |
|---|---|
| Homepage intro, headline, departments, affiliations, contact info, PhD program links | `content/site.yml` |
| The Research page write-up | `content/research.md` |
| Featured papers on the Research page | `content/highlights.yml` |
| The full publication list | `content/publications.yml` |
| People (you + group members) | `content/people.yml` |
| News items | `content/news.yml` |
| The Join page intro text | `content/join.md` |

Images (headshots, the research figure, logo) live in `assets/img/`.

## Common tasks

**Add a news item** — open `content/news.yml` and add a line at the top:
```yaml
- date: Mar 3, 2026
  text: Our paper on colloidal reactions was featured as an Editor's Suggestion.
```

**Add a publication** — open `content/publications.yml` and add an entry at the
top (newest first):
```yaml
- authors: "King, E. M., Coauthor, A. B."
  title: The title of the paper
  venue: Journal Name 1, 234567
  year: 2026
  editor_suggestion: true        # optional, adds the badge
  link: https://doi.org/...       # optional
```
Mark co-first authors with `*` and the corresponding author with `†` right after
the name. Your own name (`King, E. M.`) is bolded automatically.

**Add a group member** — open `content/people.yml`, add under `members:`:
```yaml
  - name: New Person
    role: Graduate Student in Materials Science & Engineering
    email: person@u.northwestern.edu
    photo: assets/img/new-person.jpg   # upload the photo to assets/img/ first
```
Leave out `photo:` to show a letter monogram instead.

**Change the homepage intro or your departments** — edit `content/site.yml`.

## Previewing locally (optional)

If you have Python installed:
```bash
pip install pyyaml markdown
python build.py
```
Then open `public/index.html` in a browser. (`public/` is generated; you never
edit it by hand and it isn't committed to the repo.)
