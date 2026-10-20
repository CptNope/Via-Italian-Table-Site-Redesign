#!/usr/bin/env python3
"""Assemble site/*.html from src/pages/*.html + shared header/footer.

Each page starts with a front-matter block:
---
title: Page title
desc: Meta description
active: menu|events|private|visit|home|brand
---
"""
import html, json, pathlib, re

ROOT = pathlib.Path(__file__).parent
SRC, OUT = ROOT / "src", ROOT / "site"
HEADER = (SRC / "_header.html").read_text()
FOOTER = (SRC / "_footer.html").read_text()
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
    body = re.sub(r"\{\{menu:(\w+)\}\}", lambda mm: menu_html(mm.group(1)), body)
    head = HEADER.replace("{{title}}", meta["title"]).replace("{{desc}}", meta["desc"])
    for key in ("menu", "events", "private", "visit"):
        head = head.replace("{{cur:%s}}" % key, ' aria-current="page"' if meta.get("active") == key else "")
    return head + body + FOOTER


for page in sorted((SRC / "pages").glob("*.html")):
    (OUT / page.name).write_text(render(page))
    print("built", page.name)
