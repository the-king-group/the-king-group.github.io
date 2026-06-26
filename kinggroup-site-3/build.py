#!/usr/bin/env python3
"""Build the King Group website from the Markdown/YAML files in content/.

Usage:  python3 build.py        # writes the finished site into public/
Edit the files in content/ to change the site, then run this script.
"""
import os, re, html, shutil, yaml, markdown

ROOT    = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
ASSETS  = os.path.join(ROOT, "assets")
OUT     = os.path.join(ROOT, "public")

def load_yaml(name):
    with open(os.path.join(CONTENT, name)) as fh:
        return yaml.safe_load(fh)

def load_md(name):
    """Return (frontmatter dict, html body) for a Markdown file."""
    with open(os.path.join(CONTENT, name)) as fh:
        text = fh.read()
    meta = {}
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        meta = yaml.safe_load(fm) or {}
    else:
        body = text
    return meta, markdown.markdown(body.strip())

SITE = load_yaml("site.yml")
PAGES = [("index.html","Home"),("research.html","Research"),
         ("publications.html","Publications"),("people.html","People"),
         ("news.html","News"),("join.html","Join")]

def esc(s):      return html.escape(str(s))
def escurl(u):   return html.escape(str(u), quote=True)

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?'
         'family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400..500&'
         'family=Hanken+Grotesk:wght@400;500;600;700&'
         'family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')

def affiliations_html():
    parts = []
    for a in SITE["affiliations"]:
        if a.get("url"):
            parts.append(f'<a href="{escurl(a["url"])}">{esc(a["text"])}</a>')
        else:
            parts.append(esc(a["text"]))
    return ", ".join(parts)

def departments_inline():
    return " &middot; ".join(esc(d) for d in SITE["departments"])

def departments_lines():
    return "<br>".join(esc(d) for d in SITE["departments"])

def navlinks(active):
    out = []
    for f, name in PAGES:
        cls = ' class="active"' if name == active else ""
        out.append(f'        <li><a href="{f}"{cls}>{name}</a></li>')
    return "\n".join(out)

def head(title, desc, active):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32x32.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<nav class="nav"><div class="nav-in">
  <a class="brand" href="index.html"><img class="brand-mark" src="assets/img/ek-logo.png" alt="">{esc(SITE['brand'])}</a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="navlinks">menu</button>
  <ul class="nav-links" id="navlinks">
{navlinks(active)}
  </ul>
</div></nav>
<main id="main">
"""

def footer():
    return f"""</main>
<footer class="footer"><div class="wrap"><div class="footer-in">
  <div>
    <div class="brand"><img class="brand-mark" src="assets/img/ek-logo.png" alt="">{esc(SITE['brand'])}</div>
    <p>{esc(SITE['tagline'].split('.')[0])}.</p>
  </div>
  <div class="fcol">
    <h4>Pages</h4>
    <a href="research.html">Research</a>
    <a href="publications.html">Publications</a>
    <a href="people.html">People</a>
    <a href="news.html">News</a>
    <a href="join.html">Join Us</a>
  </div>
  <div class="fcol">
    <h4>Contact</h4>
    <a href="mailto:{esc(SITE['email'])}">{esc(SITE['email'])}</a>
    <a href="{escurl(SITE['faculty_profile'])}">Northwestern profile</a>
    <a href="{escurl(SITE['scholar'])}">Google Scholar</a>
    <p style="margin-top:.6rem">{esc(SITE['address']).replace(', ', ',<br>', 1)}</p>
  </div>
</div>
<div class="colophon">
  <span>{esc(SITE['institution'])} &middot; {departments_inline()}</span>
  <span>&copy; 2026 {esc(SITE['brand'])}</span>
</div>
</div></footer>
<script src="assets/js/site.js"></script>
</body>
</html>"""

def page(fname, title, desc, active, body):
    with open(os.path.join(OUT, fname), "w") as fh:
        fh.write(head(title, desc, active) + body + footer())

# ---------------------------------------------------------------- HOME
def build_home():
    body = f"""
<section class="hero"><div class="wrap"><div class="hero-grid">
  <div class="hero-copy">
    <p class="eyebrow">{esc(SITE['brand'])} &middot; {esc(SITE['institution'])}</p>
    <h1>{esc(SITE['headline'])}</h1>
    <p class="lead">{esc(SITE['tagline'])}</p>
    <div class="btn-row">
      <a class="btn" href="research.html">Research <span class="arr">&rarr;</span></a>
      <a class="btn ghost" href="join.html">Join us</a>
    </div>
    <p class="affil" style="margin-top:1.8rem">
      {departments_inline()}<br>
      Affiliated with: {affiliations_html()}
    </p>
  </div>
  <div class="lattice-wrap">
    <canvas id="lattice" role="img"
      aria-label="Particles assembling from disorder into an ordered lattice"></canvas>
  </div>
</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>{esc(SITE['work_heading'])}</h2></div>
  <div class="figure-wrap">
    <img src="assets/img/error-correcting-materials.png" width="1100" height="1100"
      alt="Error-correcting materials: robustness to noise, stimulated healing, and self-healing">
  </div>
</div></section>

<section class="section"><div class="wrap">
  <a class="callout-btn" href="join.html">
    <h2>{esc(SITE['callout'])}</h2><span class="arr">&rarr;</span>
  </a>
</div></section>
"""
    page("index.html", f"{SITE['brand']} · {SITE['institution']}",
         SITE['tagline'], "Home", body)

# ---------------------------------------------------------------- RESEARCH
def build_research():
    meta, prose = load_md("research.md")
    hl = load_yaml("highlights.yml")
    items = "\n".join(
        f'    <a class="hl-item" href="{escurl(h["url"])}"><span class="yr"></span>'
        f'<span><h4>{esc(h["title"])}</h4><p>{esc(h["desc"].strip())}</p></span></a>'
        for h in hl)
    body = f"""
<section class="page-head"><div class="wrap"><h1>{esc(meta['title'])}</h1></div></section>

<section class="section tight"><div class="wrap"><div class="prose">{prose}</div></div></section>

<section class="section tight"><div class="wrap">
  <div class="figure-wrap">
    <img src="assets/img/error-correcting-materials.png" width="1100" height="1100"
      alt="Error-correcting materials: robustness to noise, stimulated healing, and self-healing">
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>Recent publications</h2></div>
  <div class="hl">
{items}
  </div>
  <p class="legend" style="margin-top:1.6rem">
    See the <a href="publications.html">full publication list &rarr;</a></p>
</div></section>
"""
    page("research.html", f"Research · {SITE['brand']}", SITE['tagline'],
         "Research", body)

# ---------------------------------------------------------------- PUBLICATIONS
def venue_html(v):
    m = re.match(r"^(\D+?)\s*(\d.*)$", v)
    if m:
        return f'<span class="j">{esc(m.group(1).strip())}</span> {esc(m.group(2))}'
    return f'<span class="j">{esc(v)}</span>'

def build_publications():
    pubs = load_yaml("publications.yml")
    rows = []
    for p in pubs:
        authors = esc(p["authors"]).replace("King, E. M.",
                    '<span class="me">King, E. M.</span>')
        link = p.get("link")
        if link:
            title_el = f'<a class="pub-title" href="{escurl(link)}">{esc(p["title"])}</a>'
        else:
            title_el = f'<p class="pub-title">{esc(p["title"])}</p>'
        badges = ""
        if p.get("editor_suggestion"):
            badges += '<span class="badge ed">Editor\u2019s Suggestion</span>'
        if link:
            badges += f'<a class="badge link" href="{escurl(link)}">Journal &rarr;</a>'
        badge_block = f'<div class="badges">{badges}</div>' if badges else ""
        rows.append(f"""    <li class="pub">
      <div class="meta"><span class="y">{esc(p['year'])}</span></div>
      <div>
        {title_el}
        <p class="authors">{authors}</p>
        <p class="venue">{venue_html(p['venue'])}</p>
        {badge_block}
      </div>
    </li>""")
    body = f"""
<section class="page-head"><div class="wrap">
  <h1>Publications</h1>
  <div class="btn-row" style="margin-top:1.2rem">
    <a class="btn ghost" href="{escurl(SITE['scholar'])}">Google Scholar <span class="arr">&rarr;</span></a>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <ul class="pub-list">
{chr(10).join(rows)}
  </ul>
  <p class="legend">* co-first author&nbsp;&nbsp;&middot;&nbsp;&nbsp;&dagger; corresponding author</p>
</div></section>
"""
    page("publications.html", f"Publications · {SITE['brand']}",
         "Publications and preprints from the King Group.", "Publications", body)

# ---------------------------------------------------------------- PEOPLE
def build_people():
    data = load_yaml("people.yml")
    pi = data["pi"]
    links = "\n        ".join(
        f'<a class="btn ghost" href="{escurl(l["url"])}">{esc(l["name"])}</a>'
        for l in pi["links"])
    members = []
    for m in data.get("members", []):
        if m.get("photo"):
            av = f'<div class="av"><img src="{escurl(m["photo"])}" alt="{esc(m["name"])}" width="72" height="72"></div>'
        else:
            av = f'<div class="av">{esc(m["name"][0])}</div>'
        email = (f'<a class="e" href="mailto:{esc(m["email"])}">{esc(m["email"])}</a>'
                 if m.get("email") else "")
        members.append(f"""    <div class="member">
      {av}
      <h3>{esc(m['name'])}</h3>
      <p class="r">{esc(m['role'])}</p>
      {email}
    </div>""")
    body = f"""
<section class="page-head"><div class="wrap"><h1>People</h1></div></section>

<section class="section tight"><div class="wrap">
  <div class="pi">
    <div class="pi-photo">
      <img src="{escurl(pi['photo'])}" width="440" height="440" alt="{esc(pi['name'])}, Principal Investigator">
    </div>
    <div class="pi-body">
      <p class="eyebrow">{esc(pi['label'])}</p>
      <h2>{esc(pi['name'])}</h2>
      <p class="pi-depts">{departments_lines()}</p>
      <p class="pi-affil">Affiliated with: {affiliations_html()}</p>
      <p class="pi-meta">
        <strong>Email:</strong>
        <a href="mailto:{esc(SITE['email'])}">{esc(SITE['email'])}</a><br>
        <strong>Address:</strong> {esc(SITE['address'])}
      </p>
      <div class="pi-links">
        {links}
      </div>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>Graduate students</h2></div>
  <div class="members">
{chr(10).join(members)}
  </div>
</div></section>
"""
    page("people.html", f"People · {SITE['brand']}",
         "The King Group at Northwestern University.", "People", body)

# ---------------------------------------------------------------- NEWS
def build_news():
    news = load_yaml("news.yml")
    items = "\n".join(
        f'    <li><span class="d">{esc(n["date"])}</span><span class="t">{esc(n["text"])}</span></li>'
        for n in news)
    body = f"""
<section class="page-head"><div class="wrap"><h1>News</h1></div></section>

<section class="section tight"><div class="wrap">
  <ul class="news">
{items}
  </ul>
</div></section>
"""
    page("news.html", f"News · {SITE['brand']}",
         "News from the King Group at Northwestern University.", "News", body)

# ---------------------------------------------------------------- JOIN
def build_join():
    meta, prose = load_md("join.md")
    progs = "\n".join(
        f'    <a class="prog" href="{escurl(p["url"])}"><span class="pn">{esc(p["name"])}</span><span class="arr">&rarr;</span></a>'
        for p in SITE["programs"])
    body = f"""
<section class="page-head"><div class="wrap"><h1>{esc(meta['title'])}</h1></div></section>

<section class="section tight"><div class="wrap">
  <div class="prose">{prose}</div>
  <div class="join-grid">
{progs}
  </div>
  <div class="btn-row" style="margin-top:1.6rem">
    <a class="btn" href="mailto:{esc(SITE['email'])}">Email Ella <span class="arr">&rarr;</span></a>
  </div>
</div></section>
"""
    page("join.html", f"Join Us · {SITE['brand']}",
         "Join the King Group at Northwestern.", "Join", body)

# ---------------------------------------------------------------- 404
def build_404():
    four = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found · King Group</title>
""" + FONTS + """
<link rel="stylesheet" href="/assets/css/style.css">
<link rel="icon" href="/favicon.ico" sizes="any">
<style>
  .nf{min-height:70vh;display:flex;flex-direction:column;justify-content:center;
      align-items:flex-start;max-width:var(--maxw);margin:0 auto;padding:0 var(--gut)}
  .nf .code{font-family:var(--f-mono);font-size:.8rem;letter-spacing:.18em;color:var(--teal-deep)}
  .nf h1{font-family:var(--f-display);font-size:clamp(2.4rem,6vw,4rem);
      font-weight:500;letter-spacing:-.02em;margin:.6rem 0 1rem}
  .nf p{max-width:48ch;color:var(--ink-soft);font-size:1.1rem}
  .nf .links{display:flex;flex-wrap:wrap;gap:1.4rem;margin-top:1.8rem;
      font-family:var(--f-mono);font-size:.9rem}
</style>
</head>
<body>
<nav class="nav"><div class="nav-in">
  <a class="brand" href="/"><img class="brand-mark" src="/assets/img/ek-logo.png" alt="">King Group</a>
</div></nav>
<main class="nf">
  <p class="code">404</p>
  <h1>Page not found</h1>
  <p>This page may have moved, or the link may be broken.</p>
  <div class="links">
    <a href="/">Home</a><a href="/research.html">Research</a>
    <a href="/publications.html">Publications</a><a href="/people.html">People</a>
    <a href="/join.html">Join</a>
  </div>
</main>
</body>
</html>"""
    with open(os.path.join(OUT, "404.html"), "w") as fh:
        fh.write(four)

# ---------------------------------------------------------------- BUILD
def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(ASSETS, os.path.join(OUT, "assets"))
    for f in (".nojekyll", "favicon.ico"):
        src = os.path.join(ROOT, f)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(OUT, f))
    build_home(); build_research(); build_publications()
    build_people(); build_news(); build_join(); build_404()
    print("Built site into public/:", ", ".join(f for f, _ in PAGES), "+ 404.html")

if __name__ == "__main__":
    main()
