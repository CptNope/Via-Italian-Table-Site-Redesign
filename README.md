# VIA Italian Table: spec redesign

An unsolicited redesign proposal for [viaitaliantable.com](https://viaitaliantable.com/) (VIA Italian Table, 89 Shrewsbury Street, Worcester, MA), by Jeremy Anderson. Not affiliated with or approved by VIA or Worcester Restaurant Group.

**The idea: Affissioni.** VIA becomes a billposting wall on Shrewsbury Street. Every offer and event is a dated, colour-drenched Italian poster that is pasted up while it's on and comes down the day after it ends.

## What's here

| Path | What |
| --- | --- |
| `site/` | The built site: `index.html`, `menu.html`, `events.html`, `private-dining.html`, `visit.html`, and the brand book at `brand.html`. Open any file in a browser; no server needed. |
| `src/` | Page sources plus the shared header and footer. |
| `data/menus.json` | Every menu (dinner, lunch, dessert, PigFest, family style) with prices, as published Oct 20, 2026. Edit here. |
| `build.py` | Rebuilds `site/*.html` from `src/` and `data/`. Run `python3 build.py`. |
| `site/assets/via.css`, `via.js` | All styles and behaviour. |
| `site/assets/fonts/` | Archivo and Cinzel, self-hosted (SIL Open Font License, files included). |
| `PRODUCT.md` | Product facts this design is built on. |
| `DESIGN.md` | The design system as built: tokens, components, rules. |

## How the site works

- **Posters expire on their own.** Any element with `data-end="YYYY-MM-DD"` disappears the day after that date (Worcester time). An expired poster can leave a torn remnant (`.remnant`).
- **Live open/closed status** from the published hours in `via.js` (`HOURS`).
- **Booking strip** hands party size and date to Resy (`?date=&seats=`); 9+ goes to private dining; Sundays are shown closed.
- **Tear-off tabs** on posters tear on press, then follow the link.
- **Logo A/B switch** in the top bar swaps VIA's existing mark (A, refresh) and the new cut-paper wordmark (B, rebrand). Remembered per browser.
- **Event request form** validates on the page; on a live site it would post to VIA's Tripleseat lead form. In this proposal nothing is sent.

## To do before this could go live

- Replace every `.photo-slot` with VIA's photography (each slot names the shot and ratio it wants).
- Replace the Option A stand-in (set in Cinzel) with VIA's master logo file if VIA picks the refresh.
- Confirm Resy deep-link parameters, the Tripleseat form endpoint, and the wine-dinner registration link.
- Port the drink, gluten-free and kids' menus from PDF into `data/menus.json`.
- Confirm details not published on the current site (suckling pig pricing and notice, $25 entrée end date).

## Credits

Typefaces: [Archivo](https://github.com/Omnibus-Type/Archivo) by Omnibus-Type, [Cinzel](https://github.com/NDISCOVER/Cinzel) by Natanael Gama, both under the SIL Open Font License 1.1. Menu content, hours, awards and event listings are VIA's, from viaitaliantable.com.
