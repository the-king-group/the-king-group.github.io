#!/usr/bin/env python3
"""Static-site generator for the King Group website."""
import os, html

OUT = "/home/claude/site"
SITE = "King Group"
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

def head(title, desc, active, depth_css="assets/css/style.css"):
    nav = "\n".join(
        f'        <li><a href="{f}"{" class=\"active\"" if name==active else ""}>{name}</a></li>'
        for f, name in [(f, n) for f, n in PAGES]
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
{FONTS}
<link rel="stylesheet" href="{depth_css}">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32x32.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<nav class="nav"><div class="nav-in">
  <a class="brand" href="index.html"><span class="dot"></span>King Group</a>
  <button class="nav-toggle" aria-expanded="false" aria-controls="navlinks">menu</button>
  <ul class="nav-links" id="navlinks">
{nav}
  </ul>
</div></nav>
<main id="main">
"""

FOOTER = """</main>
<footer class="footer"><div class="wrap"><div class="footer-in">
  <div>
    <div class="brand"><span class="dot"></span>King Group</div>
    <p>Designing materials that are dynamic, responsive, and able to correct
       their own errors.</p>
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
    <a href="assets/king-cv-2026.pdf">Curriculum vitae (PDF)</a>
    <p style="margin-top:.6rem">2145 Sheridan Rd<br>Evanston, IL 60208</p>
  </div>
</div>
<div class="colophon">
  <span>Northwestern University — Chemical &amp; Biological Engineering · Materials Science &amp; Engineering</span>
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
    <p class="eyebrow">King Group · Northwestern University</p>
    <h1>Materials that <em>correct</em><br>their own errors.</h1>
    <p class="lead">The King group studies and designs materials that are dynamic,
      responsive, and robust — emphasizing both fundamental science and applications
      to biology and sustainability.</p>
    <div class="btn-row">
      <a class="btn" href="research.html">Explore the research <span class="arr">&rarr;</span></a>
      <a class="btn ghost" href="join.html">Join the group</a>
    </div>
    <p class="affil" style="margin-top:1.8rem">
      Chemical &amp; Biological Engineering · Materials Science &amp; Engineering<br>
      Affiliated with Applied Physics &amp; the NSF–Simons NITMB
    </p>
  </div>
  <div class="lattice-wrap">
    <canvas id="lattice" role="img"
      aria-label="Particles assembling from disorder into an ordered lattice"></canvas>
    <span class="lattice-cap">self-assembly,<br>error-corrected</span>
  </div>
</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head">
    <p class="eyebrow">The question</p>
    <h2>How do we design error-correcting materials without billions of years of evolution?</h2>
  </div>
  <div class="prose">
    <p>Unlike human-made materials, biological systems are strikingly robust to
      errors in dynamic, out-of-equilibrium environments. Living matter corrects
      errors across six orders of magnitude — from nanometer-scale kinetic
      proofreading that drives replication far below its equilibrium error rate,
      to millimeter-scale vasculature that remodels in response to blood flow.</p>
    <p>Because so many biological systems correct their own errors, it should be
      possible to design synthetic materials with the same ability. Doing so will
      take both fundamental discoveries about the physical and biological laws
      governing these dynamic interactions, and new computational and
      inverse-design methods to engineer them.</p>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Focus areas</p>
    <h2>What we work on</h2></div>
  <div class="focus-grid">
    <div class="focus"><span class="n">01</span>
      <h3>Inverse &amp; differentiable design</h3>
      <p>Using automatic differentiation to design particle shapes, interactions,
         and assembly kinetics directly from the properties we want.</p></div>
    <div class="focus"><span class="n">02</span>
      <h3>Self-assembly &amp; colloids</h3>
      <p>Programmable patchy particles, open lattices, and self-limited
         structures — and the reactions that build and disassemble them.</p></div>
    <div class="focus"><span class="n">03</span>
      <h3>Non-equilibrium &amp; active matter</h3>
      <p>Emergent activity from wave-mediated interactions, and the statistical
         mechanics of systems driven far from equilibrium.</p></div>
    <div class="focus"><span class="n">04</span>
      <h3>Error correction &amp; inference</h3>
      <p>Kinetic proofreading in synthetic systems, and inferring interaction
         potentials from stochastic particle trajectories.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="callout">
    <div>
      <h2>We're recruiting.</h2>
      <p>The group is looking for curious students and postdocs across chemical
         engineering, materials science, applied physics, and computation.</p>
    </div>
    <div><a class="btn" href="join.html">How to join <span class="arr">&rarr;</span></a></div>
  </div>
</div></section>
"""
page("index.html", "King Group — Northwestern University",
     "The King group at Northwestern designs materials that are dynamic, responsive, "
     "and able to correct their own errors, bridging fundamental science with "
     "applications to biology and sustainability.", "Home", home)

# ---------------------------------------------------------------- RESEARCH
highlights = [
    ("2024", "Programmable patchy particles for materials design",
     "Computational design of anisotropic particle shapes that stabilize complex "
     "open lattices and enable self-limited assembly, using automatic differentiation.",
     "https://www.pnas.org/doi/full/10.1073/pnas.2311891121"),
    ("2024", "Tuning colloidal reactions",
     "Inverse-designed components give control over complex colloidal reactions — "
     "including the controlled disassembly of virus-like shells and drug-delivery-"
     "inspired release of trapped particles.",
     "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.133.228201"),
    ("2025", "Inferring interaction potentials from stochastic trajectories",
     "A method for extracting interactions from particle trajectories in and out of "
     "equilibrium, validated on experimental colloids interacting via depletion forces.",
     "https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.7.023075"),
    ("2025", "Scattered waves fuel emergent activity",
     "Nonreciprocal wave-mediated interactions reveal a new form of activity that "
     "emerges as a collective property of the system.",
     "https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.7.013055"),
    ("2021", "Designing self-assembling kinetics with differentiable models",
     "Inverse design of the kinetic properties of self-assembled structures, from "
     "transition rates between small clusters to bulk crystallization rates.",
     "https://www.pnas.org/doi/abs/10.1073/pnas.2024083118"),
]
hl_html = "\n".join(
    f'    <a class="hl-item" href="{u}"><span class="yr">{y}</span>'
    f'<span><h4>{html.escape(t)}</h4><p>{html.escape(d)}</p></span></a>'
    for y, t, d, u in highlights)

research = f"""
<section class="page-head"><div class="wrap">
  <p class="eyebrow">Research</p>
  <h1>Order, on purpose.</h1>
  <p class="lead">We work to understand and design materials that are dynamic,
    responsive, and can correct their own errors — emphasizing both fundamental
    science and applications to biology and sustainability.</p>
</div></section>

<section class="section tight"><div class="wrap"><div class="prose">
  <p>Unlike human-made materials, biological systems are strikingly robust to errors
     in the face of dynamic, out-of-equilibrium environments. Living matter corrects
     errors across six orders of magnitude: nanometer-scale kinetic proofreading
     achieves exponentially lower error rates in DNA replication than can be reached
     at equilibrium, and millimeter-scale vasculature rapidly remodels in response
     to changes in blood flow. Because many biological systems are capable of robust
     error correction, it should be possible to design synthetic materials with
     similar functions.</p>
  <p>Error-correcting materials would reshape modern technology — from artificial
     joints revitalized by synthetic enzymes to last a lifetime instead of a decade,
     to phone screens that repair themselves while charging overnight. Building them
     will require both fundamental discoveries about the physical and biological laws
     that govern these complex, dynamic interactions, and new methods in computational
     and inverse design. So how do we design error-correcting materials without the
     luxury of billions of years of evolution?</p>
</div></div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Selected work</p>
    <h2>Recent publications</h2></div>
  <div class="hl">
{hl_html}
  </div>
  <p class="legend" style="margin-top:1.6rem">
    See the <a href="publications.html">full publication list &rarr;</a></p>
</div></section>
"""
page("research.html", "Research — King Group",
     "The King group designs dynamic, error-correcting materials, bridging "
     "self-assembly, non-equilibrium statistical mechanics, and inverse design.",
     "Research", research)

# ---------------------------------------------------------------- PUBLICATIONS
# (authors, title, venue_html, year, links[(label,url)], editor_suggestion, note)
ME = "King, E. M."
def auth(s):
    return s.replace(ME, f'<span class="me">{ME}</span>')

pubs = [
 (auth("King, E. M.*, Engel, M. C.*, Martin, C. S., Schoenholz, S. S., Manoharan, V. N., Brenner, M. P."),
  "Inferring interaction potentials from stochastic particle trajectories",
  '<span class="j">Physical Review Research</span> 7, 023075', "2025",
  [("Journal","https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.7.023075")], True, ""),
 (auth("King, E. M.*, Morrell, M. C.*, Sustiel, J. B., Gronert, M., Pastor, H., Grier, D. G."),
  "Scattered waves fuel emergent activity",
  '<span class="j">Physical Review Research</span> 7, 013055', "2025",
  [("Journal","https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.7.013055")], False, ""),
 (auth("Krueger, R. K.*, King, E. M.*, Brenner, M. P."),
  "Tuning colloidal reactions",
  '<span class="j">Physical Review Letters</span> 133, 228201', "2024",
  [("Journal","https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.133.228201")], True, ""),
 (auth("King, E. M.*, Du, C. X.*, Zhu, Q. Z., Schoenholz, S. S., Brenner, M. P."),
  "Programmable patchy particles for materials design",
  '<span class="j">Proceedings of the National Academy of Sciences</span> 121, e2311891121', "2024",
  [("Journal","https://www.pnas.org/doi/full/10.1073/pnas.2311891121")], False, ""),
 (auth("Zhu, Q. Z., Du, C. X., King, E. M., Brenner, M. P."),
  "Proofreading mechanism for colloidal self-assembly",
  '<span class="j">Physical Review Research</span> 6, L042057', "2024",
  [("Journal","https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.6.L042057")], False, ""),
 (auth("Grier, D. G., King, E. M., Morrell, M. C."),
  "Thunder and lightning: a revolution in wave-matter interactions",
  '<span class="j">Preprint</span>', "2024",
  [], False, ""),
 (auth("Kimchi, O., King, E. M., Brenner, M. P."),
  "Uncovering the mechanism for aggregation in repeat expanded RNA reveals a reentrant transition",
  '<span class="j">Nature Communications</span> 14, 332', "2023",
  [("Journal","https://www.nature.com/articles/s41467-022-35803-3")], False, ""),
 (auth("King, E. M.\u2020, Wang, W., Weitz, D. A., Spaepen, F., Brenner, M. P."),
  "Correlation tracking: using simulations to interpolate highly correlated particle tracks",
  '<span class="j">Physical Review E</span> 105, 044608', "2022",
  [("Journal","https://journals.aps.org/pre/abstract/10.1103/PhysRevE.105.044608")], False, "corr"),
 (auth("Goodrich, C. P.*, King, E. M.*, Schoenholz, S. S., Cubuk, E. D., Brenner, M. P."),
  "Designing self-assembling kinetics with differentiable statistical physics models",
  '<span class="j">Proceedings of the National Academy of Sciences</span> 118, e2024083118', "2021",
  [("Journal","https://www.pnas.org/doi/abs/10.1073/pnas.2024083118")], False, ""),
 (auth("King, E. M., Gebbie, M. A., Melosh, N. A."),
  "Impact of rigidity on molecular self-assembly",
  '<span class="j">Langmuir</span> 35, 16062\u201316069', "2019",
  [], False, ""),
]

def pub_html(p):
    authors, title, venue, year, links, ed, note = p
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
  <p class="eyebrow">Publications &amp; preprints</p>
  <h1>Publications</h1>
  <p class="lead">Peer-reviewed articles and preprints. A full record is available
     on the <a href="assets/king-cv-2026.pdf">curriculum vitae</a>.</p>
</div></section>

<section class="section tight"><div class="wrap">
  <ul class="pub-list">
{pubs_html}
  </ul>
  <p class="legend">* co-first author&nbsp;&nbsp;·&nbsp;&nbsp;&dagger; corresponding author</p>
</div></section>
"""
page("publications.html", "Publications — King Group",
     "Publications and preprints from Ella King and the King Group, spanning "
     "self-assembly, non-equilibrium physics, and inverse design.",
     "Publications", publications)

# ---------------------------------------------------------------- PEOPLE
people = """
<section class="page-head"><div class="wrap">
  <p class="eyebrow">People</p>
  <h1>The group</h1>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="pi">
    <div class="pi-photo">
      <img src="assets/img/ella-king.jpg"
           alt="Ella King, Principal Investigator" width="760" height="1140">
    </div>
    <div class="pi-body">
      <p class="eyebrow">Principal Investigator</p>
      <h2>Ella King</h2>
      <p class="pi-role">
        Assistant Professor of Chemical &amp; Biological Engineering<br>
        Assistant Professor of Materials Science &amp; Engineering<br>
        Affiliated: Applied Physics Graduate Program · NITMB
      </p>
      <p class="pi-meta">
        Ella joins Northwestern in September 2026. Her research designs dynamic,
        error-correcting materials by combining non-equilibrium statistical
        mechanics with computational inverse design. She was previously a Simons
        Junior Fellow at the NYU Center for Soft Matter Research and the Flatiron
        Institute Center for Computational Biology, and earned her physics Ph.D.
        at Harvard as an NSF Graduate Research Fellow.
      </p>
      <p class="pi-meta">
        <strong>Email:</strong>
        <a href="mailto:ella.king@northwestern.edu">ella.king@northwestern.edu</a><br>
        <strong>Office:</strong> 2145 Sheridan Rd, Evanston, IL 60208
      </p>
      <div class="pi-links">
        <a class="btn ghost" href="assets/king-cv-2026.pdf">Curriculum vitae</a>
        <a class="btn ghost" href="https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/king-ella.html">Faculty profile</a>
        <a class="btn ghost" href="https://ellaking.org/">Personal site</a>
      </div>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">Graduate students</p>
    <h2>Researchers</h2></div>
  <div class="members">
    <div class="member">
      <div class="av">K</div>
      <h3>Katherine Ellis</h3>
      <p class="r">Graduate Student<br>Chemical &amp; Biological Engineering</p>
      <a class="e" href="mailto:KatherineEllis2030@u.northwestern.edu">KatherineEllis2030@u.northwestern.edu</a>
    </div>
    <div class="member" style="display:flex;flex-direction:column;justify-content:center">
      <h3 style="font-family:var(--f-display);font-weight:500;font-size:1.3rem">Your name here</h3>
      <p class="r" style="margin-bottom:.9rem">The group is recruiting students and postdocs.</p>
      <a class="e" href="join.html" style="font-family:var(--f-mono);font-size:.8rem">How to join &rarr;</a>
    </div>
  </div>
</div></section>
"""
page("people.html", "People — King Group",
     "Meet the King Group: principal investigator Ella King and group members at "
     "Northwestern University.", "People", people)

# ---------------------------------------------------------------- NEWS
news_items = [
    ("Jan 2026", "Welcome to the group, Kate Ellis, our first graduate student!"),
    ("Sep 2026", "The King Group opens at Northwestern University."),
]
news_html = "\n".join(
    f'    <li><span class="d">{d}</span><span class="t">{html.escape(t)}</span></li>'
    for d, t in news_items)
news = f"""
<section class="page-head"><div class="wrap">
  <p class="eyebrow">News</p>
  <h1>News &amp; updates</h1>
</div></section>

<section class="section tight"><div class="wrap">
  <ul class="news">
{news_html}
  </ul>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="eyebrow">On the road</p>
    <h2>Selected talks</h2></div>
  <ul class="talks">
{{talks}}
  </ul>
</div></section>
"""
talks_data = [
 ("Designing dynamic and non-equilibrium materials", "Center for Soft &amp; Living Matter, University of Pennsylvania", "Invited Talk", "Mar 2026"),
 ("Controlling dynamic and non-equilibrium materials", "Institute for Fundamental Science, University of Oregon", "Invited Talk", "Mar 2026"),
 ("Kinetic proofreading", "Course in Molecular Biophysics, Calgary", "Guest Lecture", "Mar 2026"),
 ("Emergent activity", "Levitated Matter Conference, Chicago", "Invited Talk", "Oct 2025"),
 ("Designing dynamic and non-equilibrium materials", "Frontiers in Applied &amp; Computational Mathematics, Newark", "Invited Talk", "Jun 2025"),
 ("Emergent activity arises from wave scattering", "APS March Meeting, Anaheim", "Award Session Talk", "Mar 2025"),
 ("Designing dynamic and non-equilibrium materials", "APS March Meeting, Anaheim", "Invited Talk", "Mar 2025"),
 ("Inverse design of bio-inspired materials", "Statistical Mechanics &amp; Molecular Simulation Seminar", "Invited Talk", "Oct 2024"),
 ("Designing bio-inspired properties in self-assembled materials", "UW Distinguished Young Scholars Seminar", "Invited Talk", "Jul 2024"),
 ("Inverse design with differentiable patchy particles", "SIAM Mathematical Aspects of Materials Science", "Invited Talk", "May 2024"),
 ("Emergent activity in wave-mediated interactions", "UPenn Soft Matter Theory Seminar", "Invited Talk", "Apr 2024"),
 ("Inverse design of functional materials", "NYU Courant Modeling &amp; Simulation Group Seminar", "Talk", "Nov 2023"),
 ("Inferring interaction potentials from particle trajectories", "APS March Meeting, Las Vegas", "Award Session Talk", "Mar 2023"),
 ("End-to-end differentiable atomistic simulations with JAX&nbsp;MD", "MRS Meeting, Boston", "Tutorial", "Nov 2022"),
]
talks_html = "\n".join(
    f'    <li class="talk"><span><span class="tt">{t}</span><br>'
    f'<span class="tv">{v}</span></span>'
    f'<span class="tm"><span class="kind">{k}</span><br>{d}</span></li>'
    for t, v, k, d in talks_data)
news = news.replace("{talks}", talks_html)
page("news.html", "News — King Group",
     "Latest news and selected talks from the King Group at Northwestern University.",
     "News", news)

# ---------------------------------------------------------------- JOIN
join = """
<section class="page-head"><div class="wrap">
  <p class="eyebrow">Join us</p>
  <h1>Build error-correcting materials with us.</h1>
  <p class="lead">The King group brings together chemical engineering, materials
     science, applied physics, and scientific computation. If designing dynamic,
     responsive materials excites you, we'd love to hear from you.</p>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="join-card">
    <h2 style="font-size:1.5rem;margin-bottom:.6rem">Prospective students &amp; postdocs</h2>
    <p style="max-width:60ch;color:var(--ink-soft)">
      Current Northwestern students and prospective postdoc candidates are warmly
      welcome to <a href="mailto:ella.king@northwestern.edu">email Ella</a> directly.
      Prospective graduate students should apply to one of the PhD programs the
      group is affiliated with — your application reaches us through any of them.
    </p>
    <div class="join-grid">
      <div class="prog">
        <h3>Chemical &amp; Biological Engineering</h3>
        <p>Soft materials, transport, and design at the chemical-engineering core of the group.</p>
        <a href="https://www.mccormick.northwestern.edu/chemical-biological/academics/graduate/chemical-biological-engineering-phd/">Program &rarr;</a>
      </div>
      <div class="prog">
        <h3>Materials Science &amp; Engineering</h3>
        <p>Structure, assembly, and the design of new functional materials.</p>
        <a href="https://www.mccormick.northwestern.edu/materials-science/academics/graduate/phd/">Program &rarr;</a>
      </div>
      <div class="prog">
        <h3>Applied Physics</h3>
        <p>Non-equilibrium statistical mechanics, active matter, and theory.</p>
        <a href="https://appliedphysics.northwestern.edu/">Program &rarr;</a>
      </div>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="callout">
    <div>
      <h2>Reach out.</h2>
      <p>Tell us what you're curious about — and what you'd want to build.</p>
    </div>
    <div><a class="btn" href="mailto:ella.king@northwestern.edu">Email Ella <span class="arr">&rarr;</span></a></div>
  </div>
</div></section>
"""
page("join.html", "Join Us — King Group",
     "Join the King Group at Northwestern. Information for prospective graduate "
     "students and postdocs in chemical engineering, materials science, and applied physics.",
     "Join", join)

print("Built:", ", ".join(f for f, _ in PAGES))

# ---------------------------------------------------------------- 404
four04 = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found — King Group</title>
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
  <a class="brand" href="/"><span class="dot"></span>King Group</a>
</div></nav>
<main class="nf">
  <p class="code">404 — page not found</p>
  <h1>This page didn't self-assemble.</h1>
  <p>The link may be broken or the page may have moved. Here are a few places
     that definitely exist.</p>
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
