# VIA Italian Table: spec redesign

An unsolicited redesign proposal for [viaitaliantable.com](https://viaitaliantable.com/) (VIA Italian Table, 89 Shrewsbury Street, Worcester, MA), by Jeremy Anderson. Not affiliated with or approved by VIA or Worcester Restaurant Group.

**The idea: Affissioni.** VIA becomes a billposting wall on Shrewsbury Street. Every offer and event is a dated, colour-drenched Italian poster that goes up while it's on and comes down the day after it ends.

## Pages

The built site sits at the repository root, so it deploys straight from `main`.

| Page | What |
| --- | --- |
| `index.html` | Home: lead poster with live open/closed status and the Resy booking strip, then the poster wall, menu preview, private rooms, awards, hours. |
| `menu.html` | Dinner, lunch, dessert, PigFest and family-style menus with prices. |
| `events.html` | Wine dinners, PigFest, the suckling pig dinner, the turkey kit, past dinners. |
| `private-dining.html` | Rooms by headcount and the event request form. |
| `visit.html` | Hours, parking, directions, about, awards. |
| `brand.html` | The brand book: idea, logo options A and B, colour, type, shapes, posters, photography, voice. |

## Repository layout

| Path | What |
| --- | --- |
| `src/` | Page sources, plus the shared `_header.html` and `_footer.html`. Edit pages here. |
| `data/menus.json` | Every menu with prices, as published Oct 20, 2026. Edit dishes here. |
| `build.py` | Rebuilds the root `*.html` pages from `src/` and `data/`: `python3 build.py`. Commit the rebuilt pages. |
| `assets/` | `via.css`, `via.js`, and self-hosted Archivo and Cinzel fonts (SIL Open Font License, license files included). |
| `design-system/` | The design system: `tokens.json`, a usage `README.md`, component previews and guidelines, the B wordmark in four colourways, 15 icons, fonts. |
| `PRODUCT.md` | Product facts the design is built on: users, jobs, providers, constraints, what must not be invented. |
| `DESIGN.md` | The visual system as built: tokens, components, rules. `.impeccable/design.json` is its machine-readable twin. |
| `.impeccable/` | Design-process records: the homepage direction contract (`surfaces/index-html.md`) and the direction roll. |
| `tools/artifact_page.py` | Makes a copy of a page for publishing as a Claude artifact. |

## How the site works

- **Posters expire on their own.** Any element with `data-end="YYYY-MM-DD"` disappears the day after that date (Worcester time). An expired poster can leave a remnant that the next poster is pasted over.
- **Live open/closed status** from the published hours in `assets/via.js` (`HOURS`).
- **Booking strip** hands party size and date to Resy (`?date=&seats=`); 9+ goes to private dining; Sundays show as closed.
- **Tear-off tabs** on posters tear on press, then follow the link.
- **Logo A/B switch** in the top bar swaps VIA's existing mark (A, refresh) and the new cut-paper wordmark (B, rebrand). It's remembered per browser.
- **Event request form** validates on the page. On a live site it would post to VIA's Tripleseat lead form; in this proposal nothing is sent.

## Before this could go live

- Replace every `.photo-slot` with VIA's photography (each slot names the shot and ratio it wants).
- Replace the Option A stand-in (set in Cinzel) with VIA's master logo file, if VIA picks the refresh.
- Confirm Resy deep-link parameters, the Tripleseat form endpoint, and the wine-dinner registration link.
- Port the drink, gluten-free and kids' menus from PDF into `data/menus.json`.
- Confirm details VIA hasn't published (suckling pig pricing and notice, the $25 entrée end date).

## Credits

Typefaces: [Archivo](https://github.com/Omnibus-Type/Archivo) by Omnibus-Type and [Cinzel](https://github.com/NDISCOVER/Cinzel) by Natanael Gama, both under the SIL Open Font License 1.1. Menu content, hours, awards and event listings are VIA's, from viaitaliantable.com.
