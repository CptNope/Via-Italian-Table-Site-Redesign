#!/usr/bin/env python3
"""Assemble site/*.html from src/pages/*.html + shared header/footer.

Each page starts with a front-matter block:
---
title: Page title
desc: Meta description
active: menu|events|private|visit|home|brand
---
"""
import html, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).parent
SRC, OUT = ROOT / "src", ROOT  # built pages live at the repo root, which GitHub Pages serves from main
HEADER = (SRC / "_header.html").read_text()
FOOTER = (SRC / "_footer.html").read_text()
sys.path.insert(0, str(ROOT / "tools"))
import logos  # noqa: E402  (wordmark concepts, tools/logos.py)

MENUS = json.loads((ROOT / "data" / "menus.json").read_text())


def menu_html(key: str) -> str:
    """Render one menu from data/menus.json as menu sections."""
    out = []
    for sec in MENUS[key]:
        out.append('<div class="menu-section">\n<h3>%s</h3>' % html.escape(sec["title"]))
        if sec.get("note"):
            out.append('<p class="note">%s</p>' % html.escape(sec["note"]))
        for d in sec["items"]:
            tag = ' <span class="tag">%s</span>' % html.escape(d["tag"]) if d.get("tag") else ""
            desc = "<p>%s%s</p>" % (html.escape(d.get("desc", "")), tag) if (d.get("desc") or tag) else ""
            out.append('<div class="dish"><h4>%s</h4><span class="price">%s</span>%s</div>'
                       % (html.escape(d["name"]), html.escape(d["price"]), desc))
        out.append("</div>")
    return "\n".join(out)


def render(path: pathlib.Path) -> str:
    raw = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n", raw, re.S)
    meta = dict(line.split(": ", 1) for line in m.group(1).splitlines())
    body = raw[m.end():]
    # {{include:name}} -> src/_partials/name.html (shared page sections)
    for _ in range(3):  # partials may include partials
        body = re.sub(r"\{\{include:([\w-]+)\}\}", lambda mm: (SRC / "_partials" / (mm.group(1) + ".html")).read_text(), body)
    body = re.sub(r"\{\{menu:(\w+)\}\}", lambda mm: menu_html(mm.group(1)), body)
    # {{logo:concept:ink:accent:ground}} -> inline SVG from tools/logos.py ("-" = no ground)
    body = re.sub(r"\{\{logo:(\w+):(\w+):(\w+):([\w-]+)\}\}",
                  lambda mm: logos.make(mm.group(1), mm.group(2), mm.group(3), None if mm.group(4) == "-" else mm.group(4)), body)
    head = HEADER.replace("{{marks}}", logos.symbols_html()).replace("{{title}}", meta["title"]).replace("{{desc}}", meta["desc"])
    for key in ("menu", "events", "private", "visit"):
        head = head.replace("{{cur:%s}}" % key, ' aria-current="page"' if meta.get("active") == key else "")
    if meta.get("base"):  # pages served from any path (404.html) resolve links from the site root
        head = head.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<base href="%s">' % meta["base"], 1)
    return head + body + FOOTER


for page in sorted((SRC / "pages").glob("*.html")):
    (OUT / page.name).write_text(render(page))
    print("built", page.name)
