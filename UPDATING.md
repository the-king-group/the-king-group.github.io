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

Every Monday (and on every push) a GitHub Action checks your Google Scholar
profile and adds any paper or preprint that isn't in
`content/publications.yml` yet to the top of that file, then rebuilds and
publishes the site. Existing entries are never touched, so co-first-author
marks, Editor's Suggestion badges and journal links are safe. The "Recent
publications" box on the Research page follows the same list.

**One-time setup** (about two minutes):
1. Create a free key at <https://serpapi.com/> (sign up, then copy your API key).
2. In this repo: **Settings → Secrets and variables → Actions → New repository
   secret**. Name it `SERPAPI_KEY`, paste the key, save.

Until you add the key, the site simply keeps the current list - nothing breaks.

- Scholar gives abbreviated authors ("EM King, …") and links to its own page.
  A new paper shows up that way first; tidy the entry in `publications.yml`
  whenever you like:
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
- Meeting abstracts (APS, AIChE) are skipped automatically, by venue; the list
  is `scholar_exclude_venues:` in `content/site.yml`.
- To keep anything else on Scholar off the site (a thesis, a duplicate), add
  its title to `scholar_exclude:` in `content/site.yml`. Deleting it from
  `publications.yml` alone isn't enough; it would be added back.
- To run the sync right now: **Actions → Update site → Run workflow**.
- The number of papers shown on the Research page is `recent_count:` in
  `content/site.yml` (currently 4).

**Don't edit the `.html` files directly.** They are rebuilt from `content/`
on every run, so a change made only in the HTML is lost.

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
