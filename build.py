#!/usr/bin/env python3
"""
Build the EMM website into ./site

Usage:  python3 build.py
Needs:  Python 3.9+ and Jinja2  (pip install jinja2)

How the project is laid out
  templates/base.html          shared layout (header, footer, language switch)
  templates/partials/          small pieces reused by several pages
  templates/es/*.html          Spanish pages  (one file per page)
  templates/en/*.html          English pages  (one file per page)
  content/data.py              lists used by several pages (affiliates, videos, documents, articles)
  content/articles/*.html      article bodies (kept in their original language)
  static/                      CSS, fonts, images, PDFs - copied as-is
  site/                        the finished website. Upload this folder; never edit it by hand.
"""
import datetime
import json
import math
import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).parent
OUT = ROOT / "site"
sys.path.insert(0, str(ROOT / "content"))
import data  # noqa: E402

SITE_URL = "https://nccmn.org"

# key: (spanish path, english path)
ROUTES = {
    "home":        ("/", "/en/"),
    "about":       ("/nosotros/", "/en/about/"),
    "churches":    ("/servicios/iglesias/", "/en/services/churches/"),
    "ministers":   ("/servicios/ministros/", "/en/services/ministers/"),
    "exemption":   ("/exencion-contributiva/", "/en/tax-exemption/"),
    "retirement":  ("/plan-de-retiro/", "/en/retirement-plan/"),
    "join":        ("/unase/", "/en/join/"),
    "affiliates":  ("/organizaciones-afiliadas/", "/en/affiliates/"),
    "resources":   ("/recursos/", "/en/resources/"),
    "training":    ("/formacion/", "/en/training/"),
    "reflections": ("/reflexiones/", "/en/reflections/"),
    "give":        ("/donar/", "/en/give/"),
    "prayer":      ("/oracion/", "/en/prayer/"),
    "contact":     ("/contacto/", "/en/contact/"),
    "privacy":     ("/privacidad/", "/en/privacy/"),
    "thanks":      ("/gracias/", "/en/thanks/"),
}
NOINDEX = {"thanks"}


def url(key, lang):
    es, en = ROUTES[key]
    return es if lang == "es" else en


def article_url(slug, lang):
    return url("reflections", lang) + slug + "/"


# ---------------------------------------------------------------- network map
def network_map():
    """Place the affiliated-church dots, the curved lines to the main office and the state labels
    on the same map projection as the state outlines (content/geo.py, content/map_shapes.json)."""
    from geo import project
    shapes = json.loads((ROOT / "content" / "map_shapes.json").read_text(encoding="utf-8"))
    hx, hy = project(*data.HQ["lonlat"])
    nodes = []
    for p in data.MAP_PLACES:
        x, y = project(*p["lonlat"])
        # curved line from HQ to the place
        mx, my = (hx + x) / 2, (hy + y) / 2
        dx, dy = x - hx, y - hy
        dist = math.hypot(dx, dy) or 1
        bend = min(60, dist * 0.18)
        cx, cy = mx - dy / dist * bend, my + dx / dist * bend
        nodes.append({**p, "label_en": p.get("label_en", p["label"]), "x": x, "y": y,
                      "r": 4 + 2.2 * math.sqrt(p["count"]),
                      "path": f"M{hx},{hy} Q{cx:.1f},{cy:.1f} {x},{y}",
                      "len": round(dist * 1.15)})
    states = [{"code": code, "x": project(lon, lat)[0], "y": project(lon, lat)[1]}
              for code, lon, lat in data.MAP_STATES]
    return {"hq": {"x": hx, "y": hy, **data.HQ}, "nodes": nodes, "states": states,
            "land": shapes["land"], "state_shapes": shapes["states"]}


# ---------------------------------------------------------------- build
def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT)

    env = Environment(loader=FileSystemLoader(ROOT / "templates"),
                      autoescape=True, undefined=StrictUndefined,
                      trim_blocks=True, lstrip_blocks=True)
    year = datetime.date.today().year
    articles = data.load_articles(ROOT / "content" / "articles")
    common = dict(data=data, url=url, article_url=article_url, year=year,
                  site_url=SITE_URL, articles=articles, netmap=network_map())

    sitemap = []

    def render(template, out_path, lang, key, alt_path, **extra):
        tpl = env.get_template(template)
        html = tpl.render(lang=lang, page=key, path=out_path, alt_path=alt_path,
                          noindex=key in NOINDEX, **common, **extra)
        dest = OUT / out_path.lstrip("/") / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html, encoding="utf-8")
        if key not in NOINDEX:
            sitemap.append(out_path)

    for key, (es, en) in ROUTES.items():
        render(f"es/{key}.html", es, "es", key, en)
        render(f"en/{key}.html", en, "en", key, es)

    for a in articles:
        for lang in ("es", "en"):
            other = "en" if lang == "es" else "es"
            render("partials/article.html", article_url(a["slug"], lang), lang,
                   "reflections", article_url(a["slug"], other), article=a)

    # 404 page (Netlify serves /404.html automatically)
    (OUT / "404.html").write_text(
        env.get_template("partials/404.html").render(
            lang="es", page="404", path="/404.html", alt_path="/en/",
            noindex=True, **common), encoding="utf-8")

    # robots + sitemap
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    today = datetime.date.today().isoformat()
    items = "\n".join(f"  <url><loc>{SITE_URL}{p}</loc><lastmod>{today}</lastmod></url>"
                      for p in sitemap)
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{items}\n</urlset>\n", encoding="utf-8")

    # hosting config files live at the site root
    for f in ("_headers", "_redirects"):
        shutil.copy(ROOT / "deploy" / f, OUT / f)

    # check every internal link points at a real file
    broken = check_links()
    pages = len(list(OUT.rglob("*.html")))
    print(f"Built {pages} pages into {OUT}")
    if broken:
        print("Broken internal links:")
        for b in broken:
            print("  ", b)
        sys.exit(1)


LINK_ATTRS = r'(href|src|srcset|action)="([^"]*)"'


def link_targets(attr, value):
    """The URLs inside one attribute (srcset can hold several, separated by commas)."""
    if attr == "srcset":
        return [part.strip().split()[0] for part in value.split(",") if part.strip()]
    return [value]


def make_relative(dest_dir: Path):
    """Copy ./site to dest_dir with every root link (/x/) rewritten as a relative link,
    so the site can be previewed from a sub-folder (GitHub Pages) or opened straight from disk."""
    import os
    import re
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    shutil.copytree(OUT, dest_dir)
    for page in dest_dir.rglob("*.html"):
        rel = os.path.relpath(dest_dir, page.parent).replace(os.sep, "/")
        prefix = "" if rel == "." else rel + "/"

        def to_relative(url):
            if not url.startswith("/") or url.startswith("//"):
                return url
            path, _, frag = url.lstrip("/").partition("#")
            if path == "" or path.endswith("/"):
                path += "index.html"
            return prefix + path + ("#" + frag if frag else "")

        def fix(m):
            attr, value = m.group(1), m.group(2)
            if attr == "srcset":
                parts = []
                for part in value.split(","):
                    bits = part.strip().split()
                    if bits:
                        bits[0] = to_relative(bits[0])
                        parts.append(" ".join(bits))
                return f'{attr}="{", ".join(parts)}"'
            return f'{attr}="{to_relative(value)}"'

        html = re.sub(LINK_ATTRS, fix, page.read_text(encoding="utf-8"))
        # a preview copy must never compete with the real site in search results
        if '<meta name="robots"' not in html:
            html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">', 1)
        page.write_text(html, encoding="utf-8")

    # every relative link in the preview must reach a real file, and none may stay root-absolute
    problems = []
    for page in dest_dir.rglob("*.html"):
        for attr, value in re.findall(LINK_ATTRS, page.read_text(encoding="utf-8")):
            for url in link_targets(attr, value):
                if url.startswith(("http:", "https:", "mailto:", "tel:", "data:", "#", "//")) or url == "":
                    continue
                if url.startswith("/"):
                    problems.append(f"{page.relative_to(dest_dir)}: still root-absolute -> {url}")
                    continue
                target = (page.parent / url.split("#")[0].split("?")[0]).resolve()
                if not target.exists():
                    problems.append(f"{page.relative_to(dest_dir)}: missing -> {url}")
    if problems:
        print("Preview link problems:")
        for p_ in sorted(set(problems))[:50]:
            print("  ", p_)
        sys.exit(1)


def check_links():
    import re
    broken = []
    for page in OUT.rglob("*.html"):
        html = page.read_text(encoding="utf-8")
        for attr, value in re.findall(LINK_ATTRS, html):
            for href in link_targets(attr, value):
                if not href.startswith("/") or href.startswith("//"):
                    continue
                href = href.split("#")[0].split("?")[0]
                target = OUT / href.lstrip("/")
                if href.endswith("/"):
                    target = target / "index.html"
                if not target.exists():
                    broken.append(f"{page.relative_to(OUT)} -> {href}")
    return sorted(set(broken))


if __name__ == "__main__":
    main()
    if "--preview" in sys.argv:
        make_relative(ROOT / "preview")
        print("Relative-link preview written to", ROOT / "preview")
