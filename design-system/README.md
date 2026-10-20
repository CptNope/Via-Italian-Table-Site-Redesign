VIA Italian Table looks like a billposting wall on Shrewsbury Street: flat, colour-drenched Italian posters (Depero, Olivetti, Pirelli), each one dated, pasted up when something is on and pasted over when it ends. Build every surface as posters on that wall.

> This system is a **spec proposal** by Jeremy Anderson, not yet approved by VIA. Two logo options are open (A keep the gold mark, B the new cut-paper VIA). Photography is placeholder until VIA supplies its own.

## Content fundamentals

- Write like a server who knows the menu: warm, plain, specific. Name the dish, the date, the price, the room size.
- Second person, present tense. "Nine or more? See the private rooms." Never "please contact our team for more information."
- Dates read the way people say them, bold, first: **Tuesday, Dec 8 · 6:30 pm**. Ranges: **Through Friday, Oct 31**. An offer with no end says so: "For a limited time", "Any night, by arrangement".
- Buttons and tear-off tabs name what happens: Book a table, Order takeout, Call to arrange, Register, See the menu.
- Use Italian only where VIA's own menu does (porchetta, arancini, affogato, Michelangelato). No faux-Italian flourishes, no "mangia!".
- Never invent claims: no testimonials, award years, chef names, seat counts or prices VIA hasn't published.
- No emoji. No exclamation marks on the site.

Real copy to follow:
- "Through Friday, Oct 31: porchetta, wild boar ragù, a one-pound Berkshire chop."
- "After 4 pm, park in any open space, whatever the sign says."
- "Specials and dinners go up with their dates and come down when they end."

## Visual foundations

### Colour
- Colour owns whole fields, never thin accents. Each section is one poster field: `mattone`, `oliva`, `prugna`, `zafferano`, `inchiostro`, `bianco` or `muro`.
- Lead with `mattone` (the first viewport, primary actions). Use `oliva` for menus and the kitchen, `prugna` for wine, rooms and evenings, `zafferano` for the sun, dates and awards, `inchiostro` for hours and the footer.
- `muro` is the plaster wall behind posters; `bianco` is paper for set text only (menus, forms, masthead).
- Text: `on-dark` on mattone, mattone-deep, oliva, prugna and inchiostro; `inchiostro` on zafferano, bianco and muro. Never `on-dark` on `zafferano` (2.0:1) or `inchiostro` on `mattone` (2.8:1).
- Secondary text: `on-dark-soft` on dark fields, `on-light-soft` on paper.
- `oro` belongs to logo Option A only.
- Rough share of a page: mattone 24%, muro 20%, oliva 16%, prugna 14%, ink 14%, zafferano 12%.

### Type
- One family: Archivo (variable width 62–125, weight 100–900), self-hosted from `fonts/archivo-var.woff`. Use the width axis like wood type.
- `poster-xl` / `poster-m`: width 125, weight 900, uppercase, tracking −0.035em, leading 0.86. Titles of things (PigFest, Cakebread Cellars), never slogans. Max 6rem.
- `h1`–`h2`: width 112, weight 900, sentence case. `h3`: weight 800.
- `label`: width 80–85, weight 800, uppercase, +0.05em. Buttons, tabs, nav, dates.
- `body` and `lead`: width 100, weight 400. Body measure 66ch, lead 38ch.
- `price`: weight 800 with tabular figures (`font-variant-numeric: tabular-nums`).
- Never put an eyebrow or kicker above a heading. Never use Inter, Playfair or a system display face.

### Cut-paper shapes
- Six shapes, flat fills from the poster colours: the sun (half-disc, the fire), the plate (disc), the spit (a 10px ink bar crossing at an angle), the glass (half-round cup + stem), the coins (three discs, a deal), the table set (half-disc between two saffron bars).
- Shapes live in a poster's **art band** at its top (`.poster-art`), clipped, and may bleed off the edge. Never behind running text.
- Two or three shapes per poster. Corners: `radius-square` or `radius-disc`, nothing between.

### Layout
- Full-bleed fields stacked like pasted sheets, separated by a `seam` of `muro`.
- Content max width 82rem; side gutter at least `space-4` (16px) plus safe-area insets.
- The wall: a 12-column grid with posters spanning 4–8 columns, tilted −1° to +1°, `align-items: start` so heights vary like real posters.
- Section padding `space-8` desktop, `space-7` phone. More space above a heading than below.

### Depth, borders, motion
- One shadow: `paste` (posters, buttons, photo slots); `lift` on button hover. No glows, no hard offset shadows.
- Borders: 2px solid `inchiostro` for paper rules and inputs; 2px dashed (45% of the poster's ink) for tear-off lines.
- Motion: on load, posters settle onto the wall (rotation eases to rest, a brush-sheen sweeps once), staggered 90ms. Content is visible from the first frame. Tear-off tabs drop and rotate 5–7° for 320ms before navigating. Ease `cubic-bezier(.16, 1, .3, 1)`. All of it off under `prefers-reduced-motion`.
- Focus: 3px solid `zafferano` ring, offset 3px; `prugna` on zafferano, bianco and muro fields.

### Photography
- Photos are clippings pasted on a poster (tilt 1–2°, `paste` shadow), never full-bleed behind type.
- Shoot real service: the spit turning, hands, steam, the gelato case, the exposed-brick room full. 4:5 for posters, 3:2 for rooms.
- Until VIA's photos arrive, use `PhotoSlot`, which names the shot it wants.

## Iconography
- The `Icons` group: 15 authored line icons on a 24px grid, 2px stroke, square caps, single ink `inchiostro`. In code, draw them inline with `currentColor` so they take the text colour.
- Icons sit beside a label (buttons, tabs, the phone action bar); an icon alone needs an `aria-label`.
- No emoji or Unicode glyphs as icons.

## Logo
- **Option B (proposed):** the cut-paper VIA, assets in `Logos`. The sun inside the A is always `zafferano`, or `mattone` on a zafferano field, or the ink colour in one-colour print. Clear space = the sun's height. Minimum 64px wide; smaller, set "VIA" in Archivo Black.
- **Option A (refresh):** VIA's existing gold Roman-capital mark. Its master file is not in this system; the `mark-a` style is a type stand-in only. Use on `inchiostro` or `prugna`.
- Never mix A and B in one piece. Never set the mark over a photo; give it a poster field.

## The poster (core pattern)
Every offer, event and special is a `Poster`: art band → dates (bold first) → title (`poster-m`) → one or two plain sentences or a priced list → 1–3 tear-off tabs. Every poster carries an end date in its markup (`data-end="YYYY-MM-DD"`) so it comes down the day after; a past one may leave a `Remnant`.

## Integrations
Reservations: Resy (`resy.com/cities/worcester-ma/venues/via-italian-table`, `?date=&seats=`). Takeout: Toast. Delivery: DoorDash. Events: Tripleseat lead form. Gift cards: Worcester Restaurant Group. Link out; never rebuild these flows.
