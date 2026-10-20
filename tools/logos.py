#!/usr/bin/env python3
"""VIA wordmark concepts, defined once.

Every mark is built from the same three cut-paper letters (straight cuts only)
plus one VIA-specific device. `svg(name, ink, accent, ground)` returns markup;
run this file to write assets/logos/*.svg.
"""
import pathlib

PAL = {
    "mattone": "#a8381f", "oliva": "#4f5b23", "zafferano": "#eaa42a",
    "prugna": "#3e1a33", "inchiostro": "#1c1512", "bianco": "#f3efe7", "paper": "#fbf6ee",
}

V = '<polygon points="0,0 34,0 60,82 86,0 120,0 79,120 41,120"/>'
I = '<rect x="132" y="0" width="34" height="120"/>'
A = '<polygon points="178,120 216,0 256,0 294,120 260,120 236,44 212,120"/>'
LETTERS = V + I + A


def _wrap(vb, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{title}">'
            f"<title>{title}</title>{body}</svg>")


def sole(ink, accent, ground=None):
    """B1 · Sole: a sun rises inside the A (the fire under the spit)."""
    g = f'<rect x="-12" y="-12" width="318" height="144" fill="{ground}"/>' if ground else ""
    return _wrap("-12 -12 318 144", g + f'<g fill="{ink}">{LETTERS}</g>'
                 f'<path fill="{accent}" d="M216,120 A20,20 0 0 1 256,120 Z"/>', "VIA")


def spiedo(ink, accent, ground=None):
    """B2 · Spiedo: the spit runs through all three letters, a disc turning on the I."""
    gfill = ground or "none"
    g = f'<rect x="-12" y="-12" width="318" height="144" fill="{ground}"/>' if ground else ""
    cut = ('<mask id="spit-cut"><rect x="-20" y="-20" width="340" height="170" fill="#fff"/>'
           '<rect x="-30" y="52" width="360" height="10" fill="#000" transform="rotate(-5 149 57)"/></mask>')
    return _wrap("-12 -12 318 144", g + f'<defs>{cut}</defs><g fill="{ink}" mask="url(#spit-cut)">{LETTERS}</g>'
                 f'<circle cx="149" cy="57" r="19" fill="{accent}"/>', "VIA")


def arco(ink, accent, ground=None):
    """B3 · Arco: the wordmark stands in front of a half-sun, a sunrise down the street."""
    g = f'<rect x="-12" y="-36" width="318" height="168" fill="{ground}"/>' if ground else ""
    return _wrap("-12 -36 318 168", g + f'<path fill="{accent}" d="M27,120 A120,120 0 0 1 267,120 Z"/>'
                 f'<g fill="{ink}">{LETTERS}</g>', "VIA")


def targa(ink, accent, ground=None):
    """B4 · Targa: an Italian street plate. VIA is a street, and the plate names it."""
    plate = ground or PAL["bianco"]
    return _wrap("0 0 380 200",
                 f'<rect x="0" y="0" width="380" height="200" rx="14" fill="{accent}"/>'
                 f'<rect x="12" y="12" width="356" height="176" rx="6" fill="{plate}"/>'
                 f'<rect x="24" y="24" width="332" height="152" rx="2" fill="none" stroke="{accent}" stroke-width="3"/>'
                 f'<g fill="{ink}" transform="translate(43 40)">{LETTERS}</g>', "VIA")


def tondo(ink, accent, ground):
    """B5 · Tondo: a round stamp: plate, sun and letters. Stickers, app icon, wax-seal size."""
    return _wrap("0 0 300 300",
                 f'<defs><clipPath id="tondo-clip"><circle cx="150" cy="150" r="150"/></clipPath></defs>'
                 f'<circle cx="150" cy="150" r="150" fill="{ground}"/>'
                 f'<g clip-path="url(#tondo-clip)"><path fill="{accent}" d="M40,300 A110,110 0 0 1 260,300 Z"/></g>'
                 f'<g fill="{ink}" transform="translate(48 70) scale(.694)">{LETTERS}</g>', "VIA")


def biglietto(ink, accent, ground):
    """B6 · Biglietto: the wordmark as a poster with its own tear-off tabs."""
    tabs = "".join(f'<rect x="{18 + i * 95}" y="170" width="89" height="40" fill="{accent}"/>' for i in range(3))
    dash = f'<line x1="12" y1="160" x2="312" y2="160" stroke="{ink}" stroke-width="3" stroke-dasharray="9 7"/>'
    return _wrap("0 0 324 222",
                 f'<rect x="0" y="0" width="324" height="222" fill="{ground}"/>'
                 f'<g fill="{ink}" transform="translate(30 22) scale(.894)">{LETTERS}</g>{dash}{tabs}', "VIA")


def monogramma(ink, accent, ground=None):
    """B7 · Monogramma: the V alone with the sun in its valley. Favicon and avatar."""
    g = f'<rect x="-10" y="-10" width="140" height="140" fill="{ground}"/>' if ground else ""
    return _wrap("-10 -10 140 140", g + f'<g fill="{ink}">{V}</g><circle cx="60" cy="27" r="15" fill="{accent}"/>', "VIA")


CONCEPTS = {
    "sole": sole, "spiedo": spiedo, "arco": arco, "targa": targa,
    "tondo": tondo, "biglietto": biglietto, "monogramma": monogramma,
}

# Colourways written to disk: (file suffix, ink, accent, ground)
WAYS = {
    "sole": [("ink", "inchiostro", "zafferano", None), ("paper", "paper", "zafferano", None), ("on-mattone", "paper", "zafferano", "mattone"), ("mono", "inchiostro", "inchiostro", None)],
    "spiedo": [("ink", "inchiostro", "mattone", None), ("paper", "paper", "zafferano", None), ("on-zafferano", "inchiostro", "mattone", "zafferano"), ("mono", "inchiostro", "inchiostro", None)],
    "arco": [("ink", "inchiostro", "zafferano", None), ("paper", "paper", "zafferano", None), ("on-prugna", "paper", "mattone", "prugna"), ("on-oliva", "paper", "zafferano", "oliva")],
    "targa": [("classic", "inchiostro", "mattone", "bianco"), ("night", "paper", "zafferano", "prugna"), ("mono", "inchiostro", "inchiostro", "bianco")],
    "tondo": [("mattone", "paper", "zafferano", "mattone"), ("oliva", "paper", "zafferano", "oliva"), ("prugna", "paper", "mattone", "prugna"), ("ink", "paper", "zafferano", "inchiostro")],
    "biglietto": [("zafferano", "inchiostro", "mattone", "zafferano"), ("mattone", "paper", "zafferano", "mattone"), ("oliva", "paper", "zafferano", "oliva")],
    "monogramma": [("ink", "inchiostro", "zafferano", None), ("on-mattone", "paper", "zafferano", "mattone"), ("on-zafferano", "inchiostro", "mattone", "zafferano")],
}


def make(name, ink, accent, ground):
    c = lambda k: PAL[k] if k else None
    return CONCEPTS[name](c(ink), c(accent), c(ground))


if __name__ == "__main__":
    out = pathlib.Path(__file__).resolve().parent.parent / "assets" / "logos"
    out.mkdir(parents=True, exist_ok=True)
    n = 0
    for name, ways in WAYS.items():
        for suffix, ink, accent, ground in ways:
            # unique mask/clip ids per file are not needed: each file is standalone
            (out / f"via-{name}-{suffix}.svg").write_text(make(name, ink, accent, ground) + "\n")
            n += 1
    print(f"wrote {n} files to {out}")
