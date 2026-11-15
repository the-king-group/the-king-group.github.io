#!/usr/bin/env python3
"""Add new papers from Google Scholar to content/publications.yml.

Runs weekly in GitHub Actions (.github/workflows/update.yml). It needs:
  - a free SerpApi key in the SERPAPI_KEY environment variable, and
  - the Scholar author id in content/site.yml (scholar_id:).

It only ever ADDS papers and preprints that are not already in the list, at
the top of the file. Existing entries (with their co-first-author marks,
badges and journal links) are never changed. Conference abstracts (APS, AIChE)
are skipped; see scholar_exclude_venues in content/site.yml. If the key is
missing or the request fails, the file is left exactly as it is, so the
website never breaks.
"""
import difflib, json, os, re, sys, urllib.parse, urllib.request, yaml

HERE = os.path.dirname(os.path.abspath(__file__))
PUBS = os.path.join(HERE, "content", "publications.yml")

# Scholar entries whose venue contains any of these are meeting abstracts,
# not papers. Used when site.yml does not set scholar_exclude_venues.
DEFAULT_EXCLUDE_VENUES = [
    "AIChE Annual Meeting",
    "APS Global Physics Summit",
    "APS March Meeting",
    "Meeting Abstracts",
    "Bulletin of the American Physical Society",
]

def norm(title):
    return re.sub(r"[^a-z0-9]", "", str(title).lower())

def same(a, b):
    a, b = norm(a), norm(b)
    return a == b or difflib.SequenceMatcher(None, a, b).ratio() > 0.8

def year_of(a):
    try:
        return int(str(a.get("year", "")).strip()[:4])
    except ValueError:
        return 0

def is_abstract(article, exclude_venues):
    venue = (article.get("publication") or "").lower()
    return any(v.lower() in venue for v in exclude_venues)

def new_entries(articles, existing_titles, exclude=(), exclude_venues=DEFAULT_EXCLUDE_VENUES):
    """Scholar papers and preprints that are not in the list yet, newest first."""
    known = list(existing_titles) + list(exclude)
    out = []
    for a in sorted(articles, key=year_of, reverse=True):
        title = (a.get("title") or "").strip()
        if not title or is_abstract(a, exclude_venues):
            continue
        if any(same(title, k) for k in known):
            continue
        known.append(title)
        entry = {"authors": (a.get("authors") or "").strip(), "title": title}
        venue = (a.get("publication") or "").strip()
        # Scholar appends ", 2025" to the venue; the year has its own field.
        venue = re.sub(r",\s*(19|20)\d\d$", "", venue)
        if venue:
            entry["venue"] = venue
        entry["year"] = year_of(a) or ""
        if a.get("link"):
            entry["link"] = a["link"]
        out.append(entry)
    return out

def insert(text, entries):
    """Put the new entries above the first existing one, keeping the rest as is."""
    if not entries:
        return text
    block = yaml.safe_dump(entries, sort_keys=False, allow_unicode=True,
                           default_flow_style=False, width=10000)
    block = re.sub(r"(?m)^- ", "\n- ", block).lstrip("\n") + "\n"
    m = re.search(r"(?m)^- ", text)
    if not m:
        return text.rstrip("\n") + "\n" + block
    return text[:m.start()] + block + text[m.start():]

def fetch(author_id, key):
    articles, start = [], 0
    while True:
        params = {"engine": "google_scholar_author", "author_id": author_id,
                  "api_key": key, "num": 100, "start": start, "sort": "pubdate"}
        url = "https://serpapi.com/search.json?" + urllib.parse.urlencode(params)
        with urllib.request.urlopen(url, timeout=60) as r:
            data = json.load(r)
        if data.get("error"):
            raise RuntimeError(data["error"])
        batch = data.get("articles") or []
        articles.extend(batch)
        if len(batch) < 100:
            return articles
        start += 100

def main():
    site = yaml.safe_load(open(os.path.join(HERE, "content", "site.yml"), encoding="utf-8"))
    key = os.environ.get("SERPAPI_KEY", "").strip()
    author_id = str(site.get("scholar_id", "")).strip()
    if not key or not author_id:
        print("SERPAPI_KEY or scholar_id not set - leaving publications.yml as is.")
        return
    try:
        articles = fetch(author_id, key)
    except Exception as e:
        print(f"Scholar fetch failed ({e}) - leaving publications.yml as is.")
        return
    text = open(PUBS, encoding="utf-8").read()
    existing = [p["title"] for p in (yaml.safe_load(text) or [])]
    venues = site.get("scholar_exclude_venues") or DEFAULT_EXCLUDE_VENUES
    skipped = sum(is_abstract(a, venues) for a in articles)
    entries = new_entries(articles, existing, site.get("scholar_exclude") or [], venues)
    print(f"Checked {len(articles)} Scholar entries ({skipped} meeting abstracts skipped).")
    if not entries:
        print("Nothing new.")
        return
    with open(PUBS, "w", encoding="utf-8") as fh:
        fh.write(insert(text, entries))
    for e in entries:
        print("Added:", e["title"])

if __name__ == "__main__":
    sys.exit(main())
