# VIA Italian Table · Site redesign

A redesign proposal for [viaitaliantable.com](https://viaitaliantable.com/): a new website, a design system, a brand book, seven logo concepts and four homepage layouts for VIA Italian Table, 89 Shrewsbury Street, Worcester, MA.

**Live preview:** https://cptnope.github.io/Via-Italian-Table-Site-Redesign/ (GitHub Pages, deployed from `main`)

> **Status: unsolicited spec pitch** by Jeremy Anderson ([jeremyanderson.tech](https://jeremyanderson.tech)). Not affiliated with, commissioned or approved by VIA Italian Table or Worcester Restaurant Group. Menus, hours, awards and events are VIA's own published information as of October 20, 2026. Photography is placeholder.

---

## Contents

1. [The idea](#the-idea)
2. [What's in the proposal](#whats-in-the-proposal)
3. [Logo options](#logo-options)
4. [Layout options](#layout-options)
5. [Design system at a glance](#design-system-at-a-glance)
6. [How the site works](#how-the-site-works)
7. [Editing content](#editing-content)
8. [Build, preview and deploy](#build-preview-and-deploy)
9. [Repository structure](#repository-structure)
10. [Accessibility and performance](#accessibility-and-performance)
11. [Facts, sources and what isn't invented](#facts-sources-and-what-isnt-invented)
12. [Before this could go live](#before-this-could-go-live)
13. [How it was designed](#how-it-was-designed)
14. [Credits](#credits)

---

## The idea

**Affissioni: the poster wall.** VIA's site becomes an Italian billposting wall on Shrewsbury Street. Every special, dinner and offer is a flat, colour-drenched poster in the tradition of mid-century Italian poster craft (Depero, Olivetti, Pirelli). Each poster carries its dates, goes up while it's on, and comes down by itself the day after it ends.

Why it fits VIA:

- **VIA has a calendar worth showing.** PigFest, winemaker dinners, the whole suckling pig, the Thanksgiving kit, the $25 list. Most restaurant sites hide this under "News". Here it *is* the brand.
- **VIA means street.** A billposting wall is street furniture, and VIA sits on Worcester's restaurant row.
- **It stays current on its own.** The current site still lists a June 2026 dinner as "upcoming". On the poster wall, expired posters disappear automatically.
- **It refuses the category default** (dark room, plate on slate, gold serif), which is also roughly what VIA has today.

---

## What's in the proposal

| Page | Path | What it shows |
| --- | --- | --- |
| Home (layout A) | [`index.html`](index.html) | Lead poster with the wordmark, live open/closed status, the Resy booking strip and three doors (takeout, delivery, events). Then the poster wall, a menu preview, private rooms, awards and hours. |
| Menus | [`menu.html`](menu.html) | Dinner, lunch, dessert and after-dinner, PigFest and family-style to-go, with prices, as tabs. Drink, gluten-free and kids' menus link to VIA's PDFs. |
| What's on | [`events.html`](events.html) | Current posters (Cakebread Cellars wine dinner, PigFest, suckling pig, turkey kit) and every past pairing dinner. |
| Private dining | [`private-dining.html`](private-dining.html) | The three rooms shown by headcount (36, 16, 36), an event request form, the coordinator's line. |
| Visit | [`visit.html`](visit.html) | Hours with today highlighted, address, parking rules, gift cards, the story, awards. |
| Brand book | [`brand.html`](brand.html) | The idea, both logo options, colour with contrast pairs, type, the six cut-paper shapes, poster anatomy, photography, voice, applications. |
| Logo variations | [`logos.html`](logos.html) | Seven option-B concepts and three option-A treatments, each on paper, reversed, in one colour and at 64/32/16px, with a comparison table. |
| Layout variations | [`layouts.html`](layouts.html) | Four homepage layouts side by side with desktop and phone thumbnails. |
| Layouts B–D | [`home-partenze.html`](home-partenze.html), [`home-manifesto.html`](home-manifesto.html), [`home-cucina.html`](home-cucina.html) | Full working alternatives to the current homepage. |
| Design system | [`design-system/`](design-system/) | Tokens, usage rules, component previews, wordmark files, icons, fonts. |

A dark **proposal bar** across the top of every page labels the site as a spec, switches between logo options A and B, and links to the brand book, logos and layouts. Remove it (in `src/_header.html`) before anything goes live.

---

## Logo options

VIA chooses between **A, refresh** (keep the existing gold Roman-capital mark) and **B, rebrand** (a new cut-paper wordmark). The logo switch in the proposal bar flips the whole site between them.

All seven B concepts use the same three straight-cut letters, plus one device taken from VIA's own kitchen or street:

| Concept | Device | Best for | Files (`assets/logos/`) |
| --- | --- | --- | --- |
| **B1 Sole** | A saffron sun rising inside the A | Primary mark (the one used on the site) | `via-sole-{ink,paper,on-mattone,mono}.svg` |
| **B2 Spiedo** | The spit cut through all three letters, a disc turning on the I | Alternate primary; PigFest, menus | `via-spiedo-{ink,paper,on-zafferano,mono}.svg` |
| **B3 Arco** | The letters in front of a half-sun, a sunrise down the street | Posters, patio, banners | `via-arco-{ink,paper,on-prugna,on-oliva}.svg` |
| **B4 Targa** | An Italian street plate naming the street | Building sign, door, menu covers | `via-targa-{classic,night,mono}.svg` |
| **B5 Tondo** | Plate, sun and letters in one disc | Stickers, avatar, app icon, gift card | `via-tondo-{mattone,oliva,prugna,ink}.svg` |
| **B6 Biglietto** | The wordmark as a poster with tear-off tabs | Tickets, gift cards, loyalty | `via-biglietto-{zafferano,mattone,oliva}.svg` |
| **B7 Monogramma** | The V alone with the sun in its valley | Favicon (used by this site), embroidery | `via-monogramma-{ink,on-mattone,on-zafferano}.svg` |

A suggested family: **Sole** as the primary, **Tondo** for round jobs, **Monogramma** as the favicon. Ratings for small sizes, one-colour use and distinctiveness are on [`logos.html`](logos.html#compare).

All marks are generated from one file, [`tools/logos.py`](tools/logos.py): change the geometry or colourways there and run `python3 tools/logos.py` to rewrite the SVGs; the logo page picks up the same geometry when you run `build.py`.

**Option A** is shown in Cinzel as a stand-in for VIA's master logo file, which isn't in this repository. Replace the stand-in with the real artwork before VIA reviews A in detail.

---

## Layout options

Every layout keeps the same working actions on its first screen (book on Resy, takeout, delivery, plan an event) and the same sections below it. Only the opening changes.

| Layout | Page | Leads with | Best for | Trade-off |
| --- | --- | --- | --- | --- |
| **A · Lead poster** (current home) | `index.html` | The wordmark, then booking | A first impression that makes the new identity unmistakable | What's on this week sits one scroll down |
| **B · Partenze** | `home-partenze.html` | A split-flap departures board of what's coming up, booking as a ticket | Regulars checking what's next | Darkest and busiest; smaller wordmark |
| **C · Manifesto** | `home-manifesto.html` | One typographic playbill: hours, booking, the two big dates | Launching before new photography exists | Type alone; the bill needs editing as events change |
| **D · Cucina** | `home-cucina.html` | Signature dishes and prices on a paper menu sheet | First-time visitors deciding on tonight | Front-page prices need updating with the menu |

To make B, C or D the homepage, rename its source in `src/pages/` to `index.html` (keep the front matter), and move the current one to another name.

---

## Design system at a glance

Full detail lives in [`DESIGN.md`](DESIGN.md) (human-readable), [`.impeccable/design.json`](.impeccable/design.json) (machine-readable) and [`design-system/`](design-system/) (tokens, components, assets).

### Colour

Colour owns whole fields, never thin accents. Each section is one poster.

| Token | Hex | Role | Text on it |
| --- | --- | --- | --- |
| `mattone` | `#a8381f` | Brick red. Lead poster, Book buttons | `on-dark` (6.0:1) |
| `oliva` | `#4f5b23` | Olive. Menus, the kitchen, the patio | `on-dark` (6.8:1) |
| `zafferano` | `#eaa42a` | Saffron. The sun, dates, awards | `inchiostro` (8.4:1). Never light text |
| `prugna` | `#3e1a33` | Super Tuscan plum. Wine, rooms, evenings | `on-dark` (13.9:1) |
| `inchiostro` | `#1c1512` | Ink. Text, hours, footer | `on-dark` (16.7:1) |
| `bianco` | `#f3efe7` | Poster paper, for set text only | `inchiostro` (15.7:1) |
| `muro` | `#d8cfc0` | The plaster wall behind posters | `inchiostro` (11.7:1) |
| `oro` | `#d9a640` | The incumbent gold. Logo option A only | on ink or plum |

### Type

One family, **Archivo** (variable, width 62–125 and weight 100–900), self-hosted, used across its width axis the way a poster printer used wood type:

| Role | Setting |
| --- | --- |
| Poster titles | Black 900, width 125, uppercase, −3.5% tracking, leading 0.86, max 6rem |
| Headlines | Black 900, width 112, sentence case |
| Labels, buttons, dates | Bold 700–800, width 70–85, uppercase, +5% tracking |
| Reading text | Regular 400, width 100, 17px / 1.55, 66ch measure |
| Prices | ExtraBold 800, tabular figures |

**Cinzel** appears only as the stand-in for logo option A.

### Shapes, depth and motion

- **Six cut-paper shapes**, each meaning something at VIA: the sun (the fire), the plate, the spit, the glass, the coins (a deal), the table set. They live in a poster's art band, never behind text.
- **Square corners** everywhere except discs and half-suns.
- **One shadow**, `paste`: a sheet glued to a wall. Posters tilt up to 1°.
- **One motion moment:** posters settle onto the wall on load with a brush-sheen sweep; tear-off tabs drop as you press them; the departures board (layout B) flips its letters into place once. Everything is off under `prefers-reduced-motion`.

### Components

Poster (with tear-off tabs), Remnant (an expired poster, pasted over), Button (six variants), Booking strip, Phone action bar, Menu sheet, Room card (seat map), Awards bill, Photo slot, Status pill, Hours table. Previews and usage rules for each are in [`design-system/components/`](design-system/components/).

---

## How the site works

Plain HTML, one stylesheet ([`assets/via.css`](assets/via.css)) and one script ([`assets/via.js`](assets/via.js)). No framework, no build step needed to view it.

- **Posters expire on their own.** Any element with `data-end="YYYY-MM-DD"` is removed the day after that date, in Worcester time. `data-start` hides something until its date. A `.remnant` with the same `data-end` appears only once its poster has gone.
- **Live open/closed status** is computed from the published hours in `HOURS` at the top of `via.js` ("Open now · lunch until 4pm", "Opens today at 4pm for dinner").
- **Booking strip** lists the next 21 days (Sundays shown as closed) and hands party size and date to Resy (`?date=YYYY-MM-DD&seats=N`). "9 or more" goes to private dining instead.
- **Tear-off tabs** on posters tear on press (320ms) and then follow the link; phone-number tabs tear and spring back.
- **Today's row** in every hours table is highlighted.
- **Menu tabs** are a real tablist with arrow-key support; `menu.html#lunch`, `#pigfest`, `#family` open a tab directly.
- **Logo switch** (proposal bar) swaps A and B site-wide and is remembered per browser.
- **Event request form** validates on the page and suggests a room for the headcount. In this proposal it sends nothing; on a live site it would post to VIA's Tripleseat lead form.
- **Phone action bar** (Book · Order · Call) is fixed to the bottom of every page under 860px wide.

---

## Editing content

Edit sources in `src/` and `data/`, then run `python3 build.py`. Don't edit the root `*.html` files directly; the build overwrites them.

### Add or change a poster

Posters live in `src/_partials/home-wall.html` (home) and `src/pages/events.html` (What's on). Copy an existing `<article class="poster">` and change:

```html
<article class="poster poster--plum w-5" style="--tilt:.4deg" data-end="2026-12-08" aria-labelledby="p-new">
  <div class="poster-art" aria-hidden="true"> <!-- 2–3 cut-paper shapes --> </div>
  <p class="poster-dates"><b>Tuesday, Dec 8 · 6:30 pm</b><span>Wine dinner</span></p>
  <h3 class="poster-type" id="p-new">Name of the thing</h3>
  <div class="poster-body"><p>One or two plain sentences.</p></div>
  <div class="tabs"><a class="tab" href="…">Register</a></div>
</article>
```

- Colour: `poster--sun`, `poster--olive`, `poster--plum`, `poster--brick`, `poster--ink`, `poster--paper` (default is mattone).
- Width on the 12-column wall: `w-4` to `w-12`.
- Always set `data-end` when there's an end date. No end date? Say so in the dates line ("For a limited time").
- Long single words in titles get a soft hyphen: `Thanks&shy;giving`.

### Edit menus

All menus are in [`data/menus.json`](data/menus.json):

```json
{ "dinner": [ { "title": "House pastas", "note": "optional note",
    "items": [ { "name": "Pappardelle Bolognese", "price": "$32.99",
                 "desc": "Beef, pork and sausage ragù finished with cream.", "tag": "GF penne" } ] } ] }
```

Menus available: `dinner`, `lunch`, `dessert`, `pigfest`, `family`. A page shows one with `{{menu:dinner}}`. The few dishes quoted on the homepage and layout D are written into their partials, so update those too when prices change.

### Change hours

Hours appear in a few places; change all of them together:

- `HOURS` in `assets/via.js` (drives the open/closed status and booking dates)
- `src/_partials/home-visit.html` and `src/pages/visit.html` (hours tables)
- `src/pages/home-partenze.html` and `src/pages/home-manifesto.html` (layout B and C openings)

### Shared pieces

- `src/_header.html`: head, icon sprite, both logos, proposal bar, masthead and nav.
- `src/_footer.html`: footer, phone action bar, script.
- `src/_partials/home-*.html`: the homepage sections every layout reuses (`wall`, `kitchen`, `rooms`, `awards`, `visit`). Include one with `{{include:home-wall}}`.

### Add a page

Create `src/pages/new-page.html` starting with front matter, then run the build:

```
---
title: Page title · VIA Italian Table
desc: One-sentence description for search and sharing.
active: menu
---
<section class="field field--oliva page-head">…</section>
```

`active` underlines a nav item: `menu`, `events`, `private` or `visit`.

---

## Build, preview and deploy

Requirements: Python 3.8+ for the build. Nothing else.

```bash
python3 build.py                 # rebuild the root *.html pages from src/ and data/
python3 tools/logos.py           # rewrite assets/logos/*.svg from the logo definitions
python3 -m http.server 8000      # preview at http://localhost:8000
```

Optional, to refresh the layout thumbnails after changing a layout:

```bash
pip install playwright pillow && playwright install chromium
python3 tools/thumbs.py          # rewrites assets/layouts/*.jpg
```

**Deploy:** GitHub Pages serves this repository's root from `main`. Commit the rebuilt pages and push; Pages publishes in a minute or two. `.nojekyll` keeps Pages from processing the files. Every file in the repository is publicly reachable on the deployed site, including `PRODUCT.md`, `DESIGN.md` and `src/`.

---

## Repository structure

```
.
├── index.html, menu.html, events.html,        built pages (served by GitHub Pages)
│   private-dining.html, visit.html,
│   brand.html, logos.html, layouts.html,
│   home-partenze.html, home-manifesto.html,
│   home-cucina.html
├── assets/
│   ├── via.css                                all styles
│   ├── via.js                                 all behaviour
│   ├── fonts/                                 Archivo + Cinzel (WOFF, SIL OFL, licences included)
│   ├── logos/                                 25 SVG logo files (7 concepts × colourways)
│   └── layouts/                               layout thumbnails for layouts.html
├── src/
│   ├── _header.html, _footer.html             shared chrome
│   ├── _partials/                             homepage sections shared by all layouts
│   └── pages/                                 one source file per page
├── data/menus.json                            every menu, with prices
├── design-system/                             tokens.json, README (usage rules), components, assets, fonts
├── tools/
│   ├── logos.py                               logo geometry and colourways
│   ├── thumbs.py                              layout thumbnails
│   └── artifact_page.py                       copy a page for publishing as a Claude artifact
├── build.py                                   the build
├── PRODUCT.md                                 product facts: users, jobs, providers, constraints
├── DESIGN.md                                  the visual system as built
└── .impeccable/                               design-process records (direction contract, design.json, rolls)
```

---

## Accessibility and performance

- Aims for **WCAG 2.2 AA**. Every text/background pair used is listed with its contrast ratio in the brand book; pairs that fail (light text on saffron, ink on brick) are banned.
- Real headings in order, landmarks, a skip link, labelled icon links, visible saffron focus rings (plum on light grounds), real form labels with specific error messages.
- Menus are HTML, not image or PDF-only. Gluten-free options are tagged in the menus.
- All motion respects `prefers-reduced-motion`; content is visible before any animation.
- Works without JavaScript except for live status, poster expiry, the booking hand-off and menu tabs (all menus still render).
- Fonts are self-hosted and subset to Latin (about 160KB total); no third-party scripts or trackers; total CSS and JS under 70KB uncompressed.

---

## Facts, sources and what isn't invented

Built only from VIA's own published information (viaitaliantable.com, fetched October 20, 2026): menus and prices, hours, address and phone, parking rules, private dining rooms and capacities, the coordinator's name and line, events and past dinners, awards, and the Resy, Toast, DoorDash, Tripleseat and Worcester Restaurant Group links.

**Deliberately absent:** testimonials or review quotes, award years (VIA doesn't publish them), chef or owner names, opening year, suckling-pig pricing, and any claim VIA hasn't made. Prices on the site are labelled as a sample from VIA's published menu.

---

## Before this could go live

- [ ] Replace every `.photo-slot` with VIA's photography. Each slot names the shot and ratio it needs.
- [ ] Choose logo A or B (and a B concept); replace the option A stand-in with VIA's master artwork if A is chosen.
- [ ] Remove the proposal bar from `src/_header.html`.
- [ ] Confirm the Resy deep-link parameters, connect the event form to VIA's Tripleseat lead form, and add the wine-dinner registration link.
- [ ] Port the drink, gluten-free and kids' menus from PDF into `data/menus.json`.
- [ ] Confirm unpublished details: suckling-pig pricing and notice, the $25 entrée list's end date.
- [ ] Add VIA's analytics and Google Business details if wanted, plus structured data (Restaurant, Menu, Event).
- [ ] Decide hosting (this repo deploys as a static site anywhere) and how staff will edit posters and menus.

---

## How it was designed

Designed with Claude using the [Impeccable](https://github.com/pbakaus/impeccable) design workflow:

1. **Product context** first: [`PRODUCT.md`](PRODUCT.md) records users, jobs, providers and constraints from VIA's own site.
2. **Direction:** seven visual worlds were derived from VIA's world (street plates, gold-leaf shop glass, the poster wall, Solari boards, Worcester lunch-car enamel, the gelato shop, bar matchbooks); a seeded roll assigned the poster wall and Jeremy confirmed it. The direction contract is in [`.impeccable/surfaces/index-html.md`](.impeccable/surfaces/index-html.md).
3. **Build** code-first, checked at desktop and phone widths, then a mechanical design-detector pass.
4. **Independent review** by a fresh reviewer that hadn't seen the build. It flagged eight issues (mobile title overflow, a missing phone nav, posters not visible on the first screen, a struck-through rather than pasted-over expired poster, awards as identical cards, unlabelled sample prices); all were fixed and the final verdict was *ship*.
5. **Documentation:** [`DESIGN.md`](DESIGN.md) was written from the built site, not before it.
6. Logo and layout variations were added afterwards; layouts B–D were dealt by a second seeded roll from seven ranked homepage structures.

---

## Credits

- Design and build: Jeremy Anderson, with Claude.
- Typefaces: [Archivo](https://github.com/Omnibus-Type/Archivo) by Omnibus-Type and [Cinzel](https://github.com/NDISCOVER/Cinzel) by Natanael Gama, both under the SIL Open Font License 1.1 (licence files in `assets/fonts/`).
- Restaurant content (menus, hours, events, awards, names) belongs to VIA Italian Table and Worcester Restaurant Group.
- This repository has no open-source licence; all rights to the design and code are reserved by the author unless stated otherwise.
