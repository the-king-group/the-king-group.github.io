#!/usr/bin/env python3
"""Refresh content/publications.yml from Google Scholar (via SerpApi).

This runs in GitHub Actions. It needs:
  - a free SerpApi key in the SERPAPI_KEY environment variable, and
  - the author's Scholar id in content/site.yml (scholar_id:).

If the key is missing or the request fails for any reason, the existing
content/publications.yml is left exactly as-is, so the website never breaks.
You can always curate the list by hand instead - just remove the "Sync" step
from .github/workflows/deploy.yml.
"""
import os, sys, json, urllib.parse, urllib.request, yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = yaml.safe_load(open(os.path.join(HERE, "content", "site.yml")))
OUT  = os.path.join(HERE, "content", "publications.yml")

key       = os.environ.get("SERPAPI_KEY", "").strip()
author_id = str(SITE.get("scholar_id", "")).strip()

if not key:
    print("SERPAPI_KEY not set - keeping the existing publications.yml.")
    sys.exit(0)
if not author_id:
    print("scholar_id not set in site.yml - keeping the existing publications.yml.")
    sys.exit(0)

def fetch(start):
    params = {
        "engine": "google_scholar_author",
        "author_id": author_id,
        "api_key": key,
        "num": 100,
        "start": start,
        "sort": "pubdate",
    }
    url = "https://serpapi.com/search.json?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)

def year_of(a):
    try:
        return int(str(a.get("year", "")).strip()[:4])
    except Exception:
        return 0

articles = []
try:
    start = 0
    while True:
        data = fetch(start)
        if data.get("error"):
            raise RuntimeError(data["error"])
        batch = data.get("articles", []) or []
        articles.extend(batch)
        if len(batch) < 100:
            break
        start += 100
except Exception as e:
    print(f"Scholar fetch failed ({e}) - keeping the existing publications.yml.")
    sys.exit(0)

if not articles:
    print("No articles returned - keeping the existing publications.yml.")
    sys.exit(0)

articles.sort(key=year_of, reverse=True)

pubs = []
for a in articles:
    entry = {
        "authors": (a.get("authors") or "").strip(),
        "title":   (a.get("title") or "").strip(),
        "venue":   (a.get("publication") or "").strip(),
        "year":    year_of(a) or "",
    }
    if a.get("link"):
        entry["link"] = a["link"]
    pubs.append(entry)

header = (
    "# Auto-generated from Google Scholar by scholar_sync.py.\n"
    "# Edits here are overwritten on the next sync. To curate by hand instead,\n"
    "# delete the 'Sync publications' step in .github/workflows/deploy.yml.\n"
)
with open(OUT, "w") as fh:
    fh.write(header)
    yaml.safe_dump(pubs, fh, sort_keys=False, allow_unicode=True,
                   default_flow_style=False, width=10000)
print(f"Wrote {len(pubs)} publications to publications.yml.")
