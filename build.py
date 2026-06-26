#!/usr/bin/env python3
"""Static-site generator for the King Group website."""
import os, html

OUT = "/home/claude/site"
SCHOLAR = "https://scholar.google.com/citations?user=tMOOznMAAAAJ&amp;hl=en"
PAGES = [
    ("index.html",        "Home"),
    ("research.html",     "Research"),
    ("publications.html", "Publications"),
    ("people.html",       "People"),
    ("news.html",         "News"),
    ("join.html",         "Join"),
]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?'
         'family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400..500&'
         'family=Hanken+Grotesk:wght@400;500;600;700&'
         'family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')

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
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32x32.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<nav class="nav"><div class="nav-in">
  <a class="brand" href="index.html"><img class="brand-mark" src="assets/img/ek-logo.png" alt="">King Group</a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="navlinks">menu</button>
  <ul class="nav-links" id="navlinks">
{navlinks(active)}
  </ul>
</div></nav>
<main id="main">
"""

FOOTER = f"""</main>
<footer class="footer"><div class="wrap"><div class="footer-in">
  <div>
    <div class="brand"><img class="brand-mark" src="assets/img/ek-logo.png" alt="">King Group</div>
    <p>The King group works to understand and design materials that are
       dynamic, responsive, and can correct their own errors.</p>
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
    <a href="mailto:ella.king@northwestern.edu">ella.king@northwestern.edu</a>
    <a href="https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/king-ella.html">Northwestern profile</a>
    <a href="{SCHOLAR}">Google Scholar</a>
    <p style="margin-top:.6rem">2145 Sheridan Rd<br>Evanston, IL 60208</p>
  </div>
</div>
<div class="colophon">
  <span>Northwestern University &middot; Chemical &amp; Biological Engineering &middot; Materials Science &amp; Engineering</span>
  <span>&copy; 2026 King Group</span>
</div>
</div></footer>
<script src="assets/js/site.js"></script>
</body>
</html>"""

def page(fname, title, desc, active, body):
    with open(os.path.join(OUT, fname), "w") as fh:
        fh.write(head(title, desc, active) + body + FOOTER)

# ---------------------------------------------------------------- HOME
home = """
<section class="hero"><div class="wrap"><div class="hero-grid">
  <div class="hero-copy">
    <p class="eyebrow">King Group &middot; Northwestern University</p>
    <h1>Error&#8209;correcting materials</h1>
    <p class="lead">The King group works to understand and design materials that
      are dynamic, responsive, and can correct their own errors. We emphasize both
      fundamental science and applications to biology and sustainability.</p>
    <div class="btn-row">
      <a class="btn" href="research.html">Research <span class="arr">&rarr;</span></a>
      <a class="btn ghost" href="join.html">Join us</a>
    </div>
    <p class="affil" style="margin-top:1.8rem">
      Chemical &amp; Biological Engineering &middot; Materials Science &amp; Engineering<br>
      Affiliated with: Applied Physics Graduate Program, NITMB
    </p>
  </div>
  <div class="lattice-wrap">
    <canvas id="lattice" role="img"
      aria-label="Particles assembling from disorder into an ordered lattice"></canvas>
  </div>
</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>What we work on</h2></div>
  <div class="figure-wrap">
    <img src="assets/img/error-correcting-materials.jpg" width="1100" height="1099"
      alt="Error-correcting materials: robustness to noise, stimulated healing, and self-healing">
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="callout">
    <div><h2>Come join us!</h2></div>
    <div><a class="btn" href="join.html">Join us <span class="arr">&rarr;</span></a></div>
  </div>
</div></section>
"""
page("index.html", "King Group · Northwestern University",
     "The King group at Northwestern works to understand and design materials that "
     "are dynamic, responsive, and can correct their own errors.", "Home", home)

# ---------------------------------------------------------------- RESEARCH
highlights = [
    ("Programmable patchy particles for materials design",
     "Computational design of anisotropic particle shapes that stabilize complex "
     "open lattices and enable self-limited assembly using automatic differentiation.",
     "https://www.pnas.org/doi/full/10.1073/pnas.2311891121"),
    ("Tuning colloidal reactions",
     "Control over complex colloidal reactions with inverse designed components. "
     "Controlled disassembly of virus-like shells and, inspired by drug delivery "
     "applications, induced release of small particles trapped inside.",
     "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.133.228201"),
    ("Inferring interaction potentials from stochastic particle trajectories",
     "Novel method for extracting interactions from particle trajectories in and "
     "out of equilibrium. Validated on experimental colloidal data interacting via "
     "depletion forces.",
     "https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.7.023075"),
    ("Scattered waves fuel emergent activity",
     "Nonreciprocal wave-mediated interactions reveal a new form of activity that "
     "emerges as a collective property of the system.",
     "https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.7.013055"),
    ("Designing self-assembling kinetics with differentiable statistical physics models",
     "Inverse design of kinetic properties of self-assembled structures, including "
     "transition rates between small clusters and bulk crystallization rates.",
     "https://www.pnas.org/doi/abs/10.1073/pnas.2024083118"),
]
hl_html = "\n".join(
    f'    <a class="hl-item" href="{u}"><span class="yr"></span>'
    f'<span><h4>{html.escape(t)}</h4><p>{html.escape(d)}</p></span></a>'
    for t, d, u in highlights)

research = f"""
<section class="page-head"><div class="wrap">
  <h1>Research</h1>
</div></section>

<section class="section tight"><div class="wrap"><div class="prose">
  <p>The King group works to understand and design materials that are dynamic,
     responsive, and can correct their own errors. Unlike human-made materials,
     biological systems are strikingly robust to errors in the face of dynamic,
     out-of-equilibrium environments. Living matter corrects errors across six
     orders of magnitude: nanometer-scale kinetic proofreading achieves
     exponentially lower error rates in DNA replication than can be reached at
     equilibrium, and millimeter-scale vasculature rapidly remodels in response to
     changes in blood flow. Because many biological systems are capable of robust
     error correction, it should be possible to design synthetic materials with
     similar functions.</p>
  <p>Error-correcting materials would revolutionize modern technologies, ranging
     from artificial joints that could be revitalized with error-correcting
     synthetic enzymes to last a lifetime instead of just a decade, to phone screens
     that repair themselves while recharging overnight. Creating these materials
     will require both fundamental discoveries in the physical and biological laws
     that govern these complex, dynamic interactions and innovations in computational
     and inverse design methods. So how do we design error-correcting materials
     without the luxury of billions of years of evolution?</p>
</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>Recent publications</h2></div>
  <div class="hl">
{hl_html}
  </div>
  <p class="legend" style="margin-top:1.6rem">
    See the <a href="publications.html">full publication list &rarr;</a></p>
</div></section>
"""
page("research.html", "Research · King Group",
     "The King group works to understand and design materials that are dynamic, "
     "responsive, and can correct their own errors.", "Research", research)

# ---------------------------------------------------------------- PUBLICATIONS
ME = "King, E. M."
def auth(s):
    return s.replace(ME, f'<span class="me">{ME}</span>')

pubs = [
 (auth("King, E. M.*, Engel, M. C.*, Martin, C. S., Schoenholz, S. S., Manoharan, V. N., Brenner, M. P."),
  "Inferring interaction potentials from stochastic particle trajectories",
  '<span class="j">Physical Review Research</span> 7, 023075', "2025",
  [("Journal","https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.7.023075")], True),
 (auth("King, E. M.*, Morrell, M. C.*, Sustiel, J. B., Gronert, M., Pastor, H., Grier, D. G."),
  "Scattered waves fuel emergent activity",
  '<span class="j">Physical Review Research</span> 7, 013055', "2025",
  [("Journal","https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.7.013055")], False),
 (auth("Krueger, R. K.*, King, E. M.*, Brenner, M. P."),
  "Tuning colloidal reactions",
  '<span class="j">Physical Review Letters</span> 133, 228201', "2024",
  [("Journal","https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.133.228201")], True),
 (auth("King, E. M.*, Du, C. X.*, Zhu, Q. Z., Schoenholz, S. S., Brenner, M. P."),
  "Programmable patchy particles for materials design",
  '<span class="j">Proceedings of the National Academy of Sciences</span> 121, e2311891121', "2024",
  [("Journal","https://www.pnas.org/doi/full/10.1073/pnas.2311891121")], False),
 (auth("Zhu, Q. Z., Du, C. X., King, E. M., Brenner, M. P."),
  "Proofreading mechanism for colloidal self-assembly",
  '<span class="j">Physical Review Research</span> 6, L042057', "2024",
  [("Journal","https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.6.L042057")], False),
 (auth("Grier, D. G., King, E. M., Morrell, M. C."),
  "Thunder and lightning: a revolution in wave-matter interactions",
  '<span class="j">Preprint</span>', "2024",
  []  , False),
 (auth("Kimchi, O., King, E. M., Brenner, M. P."),
  "Uncovering the mechanism for aggregation in repeat expanded RNA reveals a reentrant transition",
  '<span class="j">Nature Communications</span> 14, 332', "2023",
  [("Journal","https://www.nature.com/articles/s41467-022-35803-3")], False),
 (auth("King, E. M.\u2020, Wang, W., Weitz, D. A., Spaepen, F., Brenner, M. P."),
  "Correlation tracking: using simulations to interpolate highly correlated particle tracks",
  '<span class="j">Physical Review E</span> 105, 044608', "2022",
  [("Journal","https://journals.aps.org/pre/abstract/10.1103/PhysRevE.105.044608")], False),
 (auth("Goodrich, C. P.*, King, E. M.*, Schoenholz, S. S., Cubuk, E. D., Brenner, M. P."),
  "Designing self-assembling kinetics with differentiable statistical physics models",
  '<span class="j">Proceedings of the National Academy of Sciences</span> 118, e2024083118', "2021",
  [("Journal","https://www.pnas.org/doi/abs/10.1073/pnas.2024083118")], False),
 (auth("King, E. M., Gebbie, M. A., Melosh, N. A."),
  "Impact of rigidity on molecular self-assembly",
  '<span class="j">Langmuir</span> 35, 16062-16069', "2019",
  []  , False),
]

def pub_html(p):
    authors, title, venue, year, links, ed = p
    badges = ""
    if ed:
        badges += '<span class="badge ed">Editor\u2019s Suggestion</span>'
    for label, url in links:
        badges += f'<a class="badge link" href="{url}">{label} &rarr;</a>'
    badge_block = f'<div class="badges">{badges}</div>' if badges else ""
    if links:
        title_el = f'<a class="pub-title" href="{links[0][1]}">{html.escape(title)}</a>'
    else:
        title_el = f'<p class="pub-title">{html.escape(title)}</p>'
    return f"""    <li class="pub">
      <div class="meta"><span class="y">{year}</span></div>
      <div>
        {title_el}
        <p class="authors">{authors}</p>
        <p class="venue">{venue}</p>
        {badge_block}
      </div>
    </li>"""

pubs_html = "\n".join(pub_html(p) for p in pubs)
publications = f"""
<section class="page-head"><div class="wrap">
  <h1>Publications</h1>
  <div class="btn-row" style="margin-top:1.2rem">
    <a class="btn ghost" href="{SCHOLAR}">Google Scholar <span class="arr">&rarr;</span></a>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <ul class="pub-list">
{pubs_html}
  </ul>
  <p class="legend">* co-first author&nbsp;&nbsp;&middot;&nbsp;&nbsp;&dagger; corresponding author</p>
</div></section>
"""
page("publications.html", "Publications · King Group",
     "Publications and preprints from Ella King and the King Group.",
     "Publications", publications)

# ---------------------------------------------------------------- PEOPLE
people = f"""
<section class="page-head"><div class="wrap">
  <h1>People</h1>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="pi">
    <div class="pi-photo">
      <img src="assets/img/ella-king.jpg" width="520" height="650"
           alt="Ella King, Principal Investigator">
    </div>
    <div class="pi-body">
      <p class="eyebrow">Principal Investigator</p>
      <h2>Ella King</h2>
      <p class="pi-role">
        Assistant Professor of Chemical &amp; Biological Engineering<br>
        Assistant Professor of Materials Science &amp; Engineering<br>
        Affiliated with: Applied Physics Graduate Program, NITMB
      </p>
      <p class="pi-meta">
        <strong>Email:</strong>
        <a href="mailto:ella.king@northwestern.edu">ella.king@northwestern.edu</a><br>
        <strong>Address:</strong> 2145 Sheridan Rd, Evanston, IL 60208
      </p>
      <div class="pi-links">
        <a class="btn ghost" href="https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/king-ella.html">Faculty profile</a>
        <a class="btn ghost" href="https://ellaking.org/">Personal website</a>
        <a class="btn ghost" href="{SCHOLAR}">Google Scholar</a>
        <a class="btn ghost" href="assets/king-cv-2026.pdf">Curriculum vitae</a>
      </div>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>Graduate students</h2></div>
  <div class="members">
    <div class="member">
      <div class="av">K</div>
      <h3>Katherine Ellis</h3>
      <p class="r">Graduate Student in Chemical &amp; Biological Engineering</p>
      <a class="e" href="mailto:KatherineEllis2030@u.northwestern.edu">KatherineEllis2030@u.northwestern.edu</a>
    </div>
  </div>
</div></section>
"""
page("people.html", "People · King Group",
     "The King Group: principal investigator Ella King and group members at "
     "Northwestern University.", "People", people)

# ---------------------------------------------------------------- NEWS
news_items = [
    ("Jan 20, 2026", "Welcome to the group, Kate Ellis!"),
]
news_html = "\n".join(
    f'    <li><span class="d">{d}</span><span class="t">{html.escape(t)}</span></li>'
    for d, t in news_items)

talks_data = [
 ("Designing dynamic and non-equilibrium materials", "Center for Soft &amp; Living Matter, University of Pennsylvania, Philadelphia PA", "Invited Talk", "Mar 2026"),
 ("Controlling dynamic and non-equilibrium materials", "Institute for Fundamental Science, University of Oregon, Eugene OR", "Invited Talk", "Mar 2026"),
 ("Kinetic Proofreading", "Course in Molecular Biophysics, Calgary, Canada", "Guest Lecture", "Mar 2026"),
 ("Emergent Activity", "Levitated Matter Conference, Chicago IL", "Invited Talk", "Oct 2025"),
 ("Designing dynamic and non-equilibrium materials", "Frontiers in Applied &amp; Computational Mathematics, Newark NJ", "Invited Talk", "Jun 2025"),
 ("Emergent activity arises from wave scattering", "APS March Meeting, Anaheim CA", "Award Session Talk", "Mar 2025"),
 ("Designing dynamic and non-equilibrium materials", "APS March Meeting, Anaheim CA", "Invited Talk", "Mar 2025"),
 ("Inverse design of bio-inspired materials", "Statistical Mechanics and Molecular Simulation Seminar", "Invited Talk", "Oct 2024"),
 ("Designing bio-inspired properties in self-assembled materials", "University of Washington Distinguished Young Scholars Seminar", "Invited Talk", "Jul 2024"),
 ("Inverse design with differentiable patchy particles", "SIAM Mathematical Aspects of Materials Science", "Invited Talk", "May 2024"),
 ("Emergent activity in wave-mediated interactions", "University of Pennsylvania Soft Matter Theory Seminar, Philadelphia PA", "Invited Talk", "Apr 2024"),
 ("Inverse design of functional materials", "NYU Courant Modeling and Simulation Group Seminar, New York NY", "Talk", "Nov 2023"),
 ("Introduction to Automatic Differentiation", "Flatiron Center for Computational Biology, Inference Group, New York NY", "Talk", "Nov 2023"),
 ("Inferring interaction potentials from particle trajectories", "APS March Meeting, Las Vegas NV", "Award Session Talk", "Mar 2023"),
 ("An Introduction to End-to-End Differentiable Atomistic Simulations with JAX MD", "MRS Meeting, Boston MA", "Tutorial Instructor", "Nov 2022"),
]
talks_html = "\n".join(
    f'    <li class="talk"><span><span class="tt">{t}</span><br>'
    f'<span class="tv">{v}</span></span>'
    f'<span class="tm"><span class="kind">{k}</span><br>{d}</span></li>'
    for t, v, k, d in talks_data)

news = f"""
<section class="page-head"><div class="wrap">
  <h1>News</h1>
</div></section>

<section class="section tight"><div class="wrap">
  <ul class="news">
{news_html}
  </ul>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>Selected presentations</h2></div>
  <ul class="talks">
{talks_html}
  </ul>
</div></section>
"""
page("news.html", "News · King Group",
     "News and selected presentations from the King Group at Northwestern University.",
     "News", news)

# ---------------------------------------------------------------- JOIN
join = """
<section class="page-head"><div class="wrap">
  <h1>Join us</h1>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="prose">
    <p>Current Northwestern students and prospective postdoc candidates are welcome
       to <a href="mailto:ella.king@northwestern.edu">email Ella</a>! Prospective
       graduate students are encouraged to apply to one of the PhD programs our group
       is affiliated with
       (<a href="https://www.mccormick.northwestern.edu/chemical-biological/academics/graduate/chemical-biological-engineering-phd/">Chemical and Biological Engineering</a>,
       <a href="https://www.mccormick.northwestern.edu/materials-science/academics/graduate/phd/">Materials Science and Engineering</a>,
       or <a href="https://appliedphysics.northwestern.edu/">Applied Physics</a>).</p>
  </div>
  <div class="btn-row" style="margin-top:1.6rem">
    <a class="btn" href="mailto:ella.king@northwestern.edu">Email Ella <span class="arr">&rarr;</span></a>
  </div>
</div></section>
"""
page("join.html", "Join Us · King Group",
     "Join the King Group at Northwestern. Information for prospective graduate "
     "students and postdocs.", "Join", join)

print("Built:", ", ".join(f for f, _ in PAGES))

# ---------------------------------------------------------------- 404
four04 = """<!DOCTYPE html>
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
  .nf .code{font-family:var(--f-mono);font-size:.8rem;letter-spacing:.18em;
      text-transform:uppercase;color:var(--teal-deep)}
  .nf h1{font-family:var(--f-display);font-size:clamp(2.4rem,6vw,4rem);
      font-weight:500;letter-spacing:-.02em;margin:.8rem 0 1rem}
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
    <a href="/">Home</a>
    <a href="/research.html">Research</a>
    <a href="/publications.html">Publications</a>
    <a href="/people.html">People</a>
    <a href="/join.html">Join</a>
  </div>
</main>
</body>
</html>"""
with open(os.path.join(OUT, "404.html"), "w") as fh:
    fh.write(four04)
print("Built: 404.html")
