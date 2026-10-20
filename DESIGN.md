---
name: VIA Italian Table
description: Affissioni, the poster wall. Every offer at VIA is a dated, colour-drenched Italian poster pasted on the wall and pasted over when its date passes.
colors:
  mattone: "#a8381f"
  mattone-deep: "#7c2715"
  oliva: "#4f5b23"
  oliva-deep: "#3a4419"
  zafferano: "#eaa42a"
  zafferano-pale: "#f6d58e"
  prugna: "#3e1a33"
  prugna-soft: "#5b2a4b"
  inchiostro: "#1c1512"
  bianco: "#f3efe7"
  muro: "#d8cfc0"
  muro-deep: "#b9ad99"
  oro: "#d9a640"
  on-dark: "#fbf6ee"
typography:
  poster:
    fontFamily: "Archivo, Archivo Black, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(4.5rem, 3rem + 9vw, 6rem)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: "-0.035em"
    fontVariation: "'wdth' 125"
  headline-lg:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.6rem, 1.8rem + 3.6vw, 4.5rem)"
    fontWeight: 900
    lineHeight: 1.02
    letterSpacing: "-0.03em"
    fontVariation: "'wdth' 112"
  headline:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2rem, 1.5rem + 2.2vw, 3.25rem)"
    fontWeight: 900
    lineHeight: 1.02
    letterSpacing: "-0.03em"
    fontVariation: "'wdth' 112"
  title:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.35rem, 1.15rem + .8vw, 1.75rem)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-0.015em"
  lead:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.1rem, 1rem + .4vw, 1.3rem)"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
    fontVariation: "'wdth' 100"
  label:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "0.05em"
    fontVariation: "'wdth' 85"
  condensed:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontWeight: 700
    letterSpacing: "0.02em"
    fontVariation: "'wdth' 70"
  small:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.9rem"
  micro:
    fontFamily: "Archivo, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.78rem"
  mark-a:
    fontFamily: "Cinzel, Trajan Pro, Georgia, serif"
    fontSize: "1.7rem"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.06em"
rounded:
  none: "0"
  focus: "2px"
  circle: "50%"
  arc: "999px"
spacing:
  s-1: "0.25rem"
  s-2: "0.5rem"
  s-3: "0.75rem"
  s-4: "1rem"
  s-5: "1.5rem"
  s-6: "2rem"
  s-7: "3rem"
  s-8: "4.5rem"
  s-9: "7rem"
  gutter: "16px"
  seam: "3px"
  wrap: "82rem"
components:
  button-primary:
    backgroundColor: "{colors.mattone}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.7rem 1.25rem"
    height: "3rem"
  button-sun:
    backgroundColor: "{colors.zafferano}"
    textColor: "{colors.inchiostro}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.7rem 1.25rem"
    height: "3rem"
  button-paper:
    backgroundColor: "{colors.bianco}"
    textColor: "{colors.inchiostro}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.7rem 1.25rem"
    height: "3rem"
  button-plum:
    backgroundColor: "{colors.prugna}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.7rem 1.25rem"
    height: "3rem"
  button-ink:
    backgroundColor: "{colors.inchiostro}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.7rem 1.25rem"
    height: "3rem"
  button-ghost:
    backgroundColor: "transparent"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.7rem 1.25rem"
    height: "3rem"
  poster:
    backgroundColor: "{colors.mattone}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    padding: "1.5rem 1.5rem 0"
  poster-sun:
    backgroundColor: "{colors.zafferano}"
    textColor: "{colors.inchiostro}"
  poster-paper:
    backgroundColor: "{colors.bianco}"
    textColor: "{colors.inchiostro}"
  tear-off-tab:
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.6rem 0.5rem"
    height: "3.25rem"
  booking-strip:
    backgroundColor: "{colors.mattone-deep}"
    padding: "2px"
    width: "40rem"
  booking-field:
    backgroundColor: "{colors.bianco}"
    textColor: "{colors.inchiostro}"
    padding: "0.5rem 0.75rem 0.45rem"
  input-field:
    backgroundColor: "{colors.bianco}"
    textColor: "{colors.inchiostro}"
    rounded: "{rounded.none}"
    padding: "0.7rem 0.8rem"
    height: "3rem"
  menu-sheet:
    backgroundColor: "{colors.bianco}"
    textColor: "{colors.inchiostro}"
    rounded: "{rounded.none}"
  masthead:
    backgroundColor: "{colors.bianco}"
    textColor: "{colors.inchiostro}"
    height: "4.25rem"
  actionbar-link:
    backgroundColor: "{colors.bianco}"
    textColor: "{colors.inchiostro}"
    height: "3.6rem"
  actionbar-link-primary:
    backgroundColor: "{colors.mattone}"
    textColor: "{colors.on-dark}"
    height: "3.6rem"
  room-card:
    backgroundColor: "{colors.prugna-soft}"
    textColor: "{colors.on-dark}"
    padding: "1.5rem"
  room-card-patio:
    backgroundColor: "{colors.oliva}"
    textColor: "{colors.on-dark}"
    padding: "1.5rem"
  footer:
    backgroundColor: "{colors.inchiostro}"
    textColor: "{colors.on-dark}"
---

# Design System: VIA Italian Table

## Overview

**Creative North Star: "Affissioni, the Poster Wall on Shrewsbury Street"**

VIA's site is an Italian billposting wall. The page background is plaster (muro); every offer, event, menu and room is a sheet of drenched poster stock pasted onto it, edge to edge or slightly askew, with a seam of wall showing between sheets. The craft reference is mid-century Italian poster work (Depero, Olivetti, Pirelli): flat fields of brick, olive, saffron and Super Tuscan plum, huge expanded black type, and a small vocabulary of cut-paper shapes that each stand for something real at VIA (the fire, the plate, the spit, the glass, the deal, the table).

The wall is honest about time. Every poster carries its dates first, and the code takes a poster down the day after its `data-end` date (Worcester time). An expired poster can leave a muro-deep remnant ("Was Tue, Jun 16 · pasted over"). Actions are not floating buttons but tear-off tabs cut along the poster's bottom edge, like a street flyer; pressing one tears it before the link follows. Photography is pasted on like a clipping, tilted, never full-bleed behind type; until VIA supplies photos, every photo is a labelled, hatched slot naming the shot and ratio.

Density is poster-scale: few words, very large, set in one family (Archivo) used across its width axis the way a printer uses wood type. The system deliberately refuses the restaurant category default it replaces (the old viaitaliantable.com look and its peers): a dark full-bleed food photo, a gold serif, and a lone "Reserve" button. Gold survives only inside Logo Option A.

**Key Characteristics:**
- Whole fields of colour, never thin accents; colour is what a poster is made of.
- One typeface, Archivo, across widths: 125 to shout, 112 for headlines, 70 to 85 for labels and dates, 100 to read.
- Square-cut rectangles and whole cut-paper curves; nothing in between.
- Depth is paper on plaster: a paste shadow and a hair of rotation, no cards, no glass.
- Dates lead, expired content disappears, and the three doors (book, order, plan an event) are one tap from anywhere.
- Two switchable identities (A: existing gold mark; B: cut-paper VIA wordmark) inside the same poster world.

## Colors

Four poster stocks, an ink, a paper and the wall; every stock is flat and fully saturated for its hue, and each owns whole fields.

### Primary
- **Mattone, Brick Red** (#a8381f): the lead poster on the home page, the Book a table button, the active nav underline, the menu tab underline, the primary phone action, focus outline inside booking fields, invalid-field borders and error text on paper. The colour of the exposed brick room.
- **Mattone Scuro, Shadow Brick** (#7c2715): the booking strip's frame, the brick variant poster (Thanksgiving kit), default photo-slot ground, pressed/shadow states.

### Secondary
- **Oliva, Olive** (#4f5b23): menus and the kitchen; the $25 entrées poster, the patio room, menu dish tags, the form confirmation panel, and the bullets of positive brand-book rules.
- **Oliva Scura, Deep Olive** (#3a4419): olive photo-slot ground only.

### Tertiary
- **Zafferano, Saffron** (#eaa42a): the sun. Dates and highlights, the PigFest poster, the "Find a table" button inside the booking strip, the open-now status dot, today's row in the hours table, seat dots in room maps, global focus outline (3px), text selection, and the sun inside Logo B.
- **Zafferano Chiaro, Pale Saffron** (#f6d58e): links inside the ink pitch bar only.
- **Prugna, Super Tuscan Plum** (#3e1a33): wine, evenings and rooms; the Cakebread wine-dinner poster, the "Plan an event" door, the plate disc in the lead composition, the Wine Spectator column in the award bill, and the focus outline on saffron, paper and wall fields.
- **Prugna Chiara, Soft Plum** (#5b2a4b): room cards, the wine-glass shape, plum photo slots.

### Neutral
- **Inchiostro, Ink** (#1c1512): all type on light fields, the masthead's bottom seam, the footer, the pitch bar, the ink poster (suckling pig), the spit stripe, and the ground for Logo A.
- **Bianco, Poster Paper** (#f3efe7): set-text surfaces only: masthead, menu sheet, forms, booking-strip fields, paper buttons, the wall heading slip, the phone action bar.
- **Muro, Plaster Wall** (#d8cfc0): the body background behind everything, and the seam colour between pasted fields.
- **Muro Scuro, Old Plaster** (#b9ad99): the torn remnant of an expired poster.
- **Oro, Incumbent Gold** (#d9a640): Logo Option A only.
- **On-dark Paper Type** (#fbf6ee): type on mattone, oliva, prugna and ink. A softened version (88% mixed toward transparent) carries secondary text on dark fields; on paper, secondary text is ink mixed 74% toward bianco.

### Named Rules

**The Drenched Field Rule.** Colour comes as whole poster fields, never as a thin accent stripe or tinted card. A typical page by area runs roughly mattone 24%, muro 20%, oliva 16%, prugna 14%, ink 14%, zafferano 12%.

**The Ink-or-Paper Rule.** Text on mattone, oliva and prugna is paper (#fbf6ee); text on zafferano, bianco and muro is ink. Paper on saffron (2.0:1) and ink on brick (2.8:1) fail and are never used for text. Measured pairs: paper on mattone 6.0:1, paper on oliva 6.8:1, paper on prugna 13.9:1, ink on saffron 8.4:1, mattone on bianco 5.6:1.

**The Gold Belongs to A Rule.** Oro appears only inside Logo Option A, always on an ink or plum ground. The new world never borrows gold.

## Typography

**Display Font:** Archivo variable (weights 100 to 900, width 62% to 125%), self-hosted, with Archivo Black, Helvetica Neue, Arial fallbacks
**Body Font:** Archivo (same file) at width 100
**Logo A stand-in:** Cinzel 700 (with Trajan Pro, Georgia), used only to redraw VIA's existing Roman-capital mark until master artwork arrives

**Character:** One grotesque played like a case of wood type: expanded black caps shout the name of the thing, narrow bold caps carry dates, prices and actions, and the regular width reads quietly underneath. Width, not a second family, makes the contrast.

### Hierarchy
- **Poster** (900, width 125, uppercase, clamp(4.5rem, 3rem + 9vw, 6rem), line-height 0.86, letter-spacing -0.035em): page titles ("What's on", "Menus", "Visit") and poster titles (PigFest, Cakebread Cellars). Poster titles size per poster from clamp(2rem, 1.4rem + 2.4vw, 3.4rem) up to clamp(2.6rem, 1.6rem + 3.4vw, 4.8rem) on wide posters; room capacities ("36 guests") use it too. Manual soft hyphens only.
- **Headline** (900, width 112, sentence case, h1 clamp(2.6rem, 1.8rem + 3.6vw, 4.5rem) / h2 clamp(2rem, 1.5rem + 2.2vw, 3.25rem), line-height 1.02, -0.03em): section heads such as "On the wall this week", "Three rooms for a party". Balanced wrapping.
- **Title** (800, clamp(1.35rem, 1.15rem + .8vw, 1.75rem), line-height 1.1, -0.015em): facts, room names, the wall heading slip. Menu section heads use 900 / width 112 / 1.6rem uppercase over a 2px ink rule.
- **Lead** (400, clamp(1.1rem, 1rem + .4vw, 1.3rem), line-height 1.5, max 38ch): the one-paragraph introduction under a lead poster or page title.
- **Body** (400, width 100, 1.0625rem / 17px, line-height 1.55, measure 66ch): all reading text. Poster body text caps at 46ch.
- **Label** (700 to 800, width 70 to 85, uppercase, +0.02em to +0.05em): buttons (800 / 85 / .95rem), tear-off tabs (800 / 78 / .86rem), nav (700 / 80 / .92rem), dates and condensed lines (700 / 70). Field labels inside the booking strip use micro size with +0.08em.
- **Small / Micro** (.9rem / .78rem): poster date lines, notes, captions, pitch bar.
- **Prices** (800, tabular figures, no wrap): every price and phone number on the site.

### Named Rules

**The One Family Rule.** Archivo is the only typeface of the world. Contrast comes from the width axis (125 / 112 / 100 / 85 / 70) and weight, never from a second display face. Cinzel exists only as Logo A's placeholder.

**The Date Leads Rule.** On any poster the bold date (start or end) is the first line of text, then the kind of thing it is, in small type: "Tuesday, Dec 8 · 6:30 pm · Wine dinner". A poster with no end date says so ("For a limited time", "Any night").

**The Name, Not a Slogan Rule.** Poster type sets the name of the thing (PigFest, Whole suckling pig, $25 entrées), never a tagline.

## Layout

The page is a vertical stack of full-bleed **fields**, each one poster sheet, padded 4.5rem top and bottom (3rem under 620px) with a 16px minimum side gutter that respects safe-area insets. Consecutive fields are separated by a 3px seam of muro, so the wall shows between sheets. Content sits in an 82rem centred wrap.

The home page opens with a full-bleed mattone **lead poster**: a two-column grid (1.15fr / .85fr, bottom-aligned). Left: Logo B (or A) at poster scale as the h1, a lead paragraph, the live open/closed status chip, the booking strip, a one-line booking note, and the two sibling doors (Order takeout, Delivery) plus Plan an event. Right: a cut-paper composition (saffron half-sun bleeding off the bottom right, plum plate disc, ink spit stripe at -24deg) with a pasted 4:5 photo slot rotated 2.2deg. The next field (the wall) is pulled up 2.25rem so its heading slip overlaps the lead poster's bottom edge, already pasted.

**The wall** is a 12-column dense grid (gap 1.5rem by 1rem) of posters spanning 4, 5, 6, 7, 8 or 12 columns. Posters align to the top, each carries its own tilt between -0.9deg and +0.7deg, and one may overlap its neighbour (-3rem right margin on wide screens). Remnants of expired posters take 3 columns.

Inner pages open with a **page head** field: poster-type title, lead, and a saffron sun clamp(16rem, 10rem + 24vw, 34rem) bleeding off the bottom right behind it.

**Breakpoints:** at 1060px the wall drops to 6 columns (4/5/6-span posters become 3; 7/8/12 go full width) and rooms go 2-up with the patio full width. At 860px the masthead wraps, the nav becomes a horizontally scrolling row under the logo, the lead poster stacks to one column, the masthead Book button hides, and a fixed three-door **phone action bar** appears at the bottom (body gains matching bottom padding). At 620px the wall is one column, the booking strip goes 2-up with a full-width button, and menu tabs scroll horizontally. At 400px awards go single column.

**The Three Doors Rule.** Book (Resy), order (Toast / DoorDash) and plan an event (private dining / Tripleseat) are reachable in one tap from every page: masthead Book button and nav on wide screens, the fixed action bar on phones, and the lead poster's strip and doors on home.

## Elevation & Depth

Depth is paper pasted on plaster. There are no floating cards, no glass, no blur, and no hard offset shadows. A poster, button, room card or photo slot sits on the wall with a single soft **paste** shadow: a hairline lip plus a short, tight drop below. The other depth cues are physical: a fraction of a degree of rotation, overlapping edges, the muro seam between fields, and dashed tear lines. Larger sheets that sit further off the wall (the menu sheet, the booking strip) get a longer, softer drop.

### Shadow Vocabulary
- **Paste** (`box-shadow: 0 1px 0 rgba(0,0,0,.06), 0 10px 24px -14px rgba(28,21,18,.55)`): the default for every pasted sheet: posters, buttons, room cards, photo slots, remnants, brand-book cards.
- **Paste lift** (`box-shadow: 0 1px 0 rgba(0,0,0,.06), 0 16px 26px -14px rgba(28,21,18,.6)`): button hover, paired with a 2px rise.
- **Strip** (`box-shadow: 0 18px 40px -22px rgba(0,0,0,.6)`): the booking strip inside the lead poster.
- **Sheet** (`box-shadow: 0 30px 60px -36px rgba(0,0,0,.7)`): the menu sheet.
- **Ghost edge** (`box-shadow: inset 0 0 0 2px currentColor`, 3px on hover): ghost buttons; a printed outline, not a shadow.

### Named Rules

**The Pasted, Not Floating Rule.** Every raised element uses the paste shadow and stays square to the wall or tilted by under 1deg (photo clippings up to about 2.2deg). Nothing hovers with a large diffuse glow.

## Shapes

Rectangles are square-cut: posters, buttons, tabs, fields, inputs, room cards and sheets all have 0 radius. Curves appear only as whole cut-paper shapes: full circles (the plate, the coins, seat dots, the status dot) and half-discs cut with a 999px radius on two corners (the sun, the glass bowl, the table). The 2px radius on focus rings and the pill segmented control in the pitch bar are interface apparatus, not part of the poster world.

### The six cut-paper shapes
Each shape is cut from a poster colour and stands for something real at VIA. They live in a poster's art band (the top strip, bled to the poster's edges, 4.5 to 9.5rem tall) or in a lead/page-head composition, never behind running text. Flat fills only; they may overlap and bleed off the edge like paper trimmed after pasting; one composition per poster, two or three shapes at most.

1. **The sun, the fire**: a half-disc (top corners 999px) rising from a bottom edge, usually mattone on saffron or saffron on mattone. The spit's fire; the arch of a street; also the sun inside Logo B's A.
2. **The plate**: a full plum disc.
3. **The spit**: a long ink stripe (10 to 14px) crossing the field at a shallow angle (-4deg to -24deg), sometimes skewering a plate disc.
4. **The glass**: a soft-plum bowl (bottom corners 999px) on an 8px stem; wine dinners.
5. **The coins, a deal**: three equal circles in a row (saffron, mattone, bianco), half sunk below the art band; the $25 entrées.
6. **The table set**: a bianco plate disc or half-disc flanked by two 6px saffron uprights (knife and fork); the Thanksgiving kit and other at-home tables.

## Components

### Buttons
Character: a printed label slapped on the wall: square, condensed bold caps, pasted.
- **Shape:** square-cut (0 radius), minimum 3rem tall (2.75rem in the masthead).
- **Primary:** mattone with paper type, padding .7rem 1.25rem, Archivo 800 width 85, uppercase, .95rem, +0.05em, with an optional 1.15em leading icon.
- **Hover / Focus:** rises 2px with the paste-lift shadow over .25s on the house ease-out; returns flat on press. Focus is a 3px saffron outline offset 3px (plum on saffron, paper and wall fields).
- **Variants:** sun (saffron, ink type; the booking strip's "Find a table"), paper (bianco, ink; Order takeout, Delivery), plum (prugna, paper; Plan an event), ink, and ghost (transparent with a 2px inset edge in the current colour, 3px on hover). Disabled is 50% opacity, no rise.
- **Arrow link:** condensed 800 uppercase text with a trailing arrow that slides 3px on hover.

### Booking strip (signature)
The working action inside the lead poster: a shadow-brick frame (2px padding, 2px gaps) holding two paper fields (Party, Date) and a saffron "Find a table" button, max 40rem wide. Field labels are micro, uppercase, +0.08em, in soft ink; values are 700 at 1.05rem. The date list is generated for the next 21 days with Sundays shown as "closed" and disabled; there is no time field because Resy's link takes only date and party size. Submitting hands `?date=&seats=` to Resy; "9 or more" routes to private dining.

### Poster (signature)
Every offer, event and special is one poster built the same way, top to bottom:
1. **Art band**: the cut-paper composition, bled to the top and side edges, clear of text.
2. **Dates**: bold start or end date first, then what kind of thing it is (small type, soft colour).
3. **Title**: poster type, the name of the thing.
4. **Body**: one or two plain sentences, and real dishes with real prices when there are any (an item list with 1px rules in the poster's own type colour at 22%, prices in tabular 800).
5. **Tear-off tabs**: one to three actions.

Posters are square-cut, padded 1.5rem (0 at the bottom, where the tabs sit), carry the paste shadow and a per-poster tilt (`--tilt`, -0.9deg to +0.7deg). Stocks: mattone (default), olive, plum, sun (saffron with ink type), paper, brick (shadow brick), ink. A poster with `data-end` is removed the day after its date; one with `data-start` stays down until then.

### Tear-off tabs (signature)
The poster's actions, cut like an Italian street flyer. A row of equal tabs across the poster's full width, separated from the body and from each other by 2px dashed lines in the poster's type colour at 45%. Each tab is at least 3.25rem tall, Archivo 800 width 78, uppercase, .86rem, on the poster stock darkened 18% toward black (10% on saffron), darkening further (32%, or 16% on saffron) on hover. On press the tab tears: it drops 14px and rotates a random -5deg to +5deg over .45s, and the link follows after 320ms. Phone and anchor links tear and spring back. Reduced motion and modified clicks skip the tear.

### Remnant
The pasted-over trace of an expired poster: muro-deep, ink type, 1.4deg tilt, paste shadow, condensed line "Was Tue, Jun 16 · pasted over" and the event's title. It only appears once its poster's date has passed.

### Photo slots
Labelled frames for VIA's own photography: a hatched ground (135deg ink hairlines every 14px over shadow brick, soft plum, deep olive, warm ink or pale paper), an inset dashed frame at 45%, a camera icon top right, and a caption naming the shot and ratio. Pasted like a clipping with the paste shadow and a small tilt. Never full-bleed, never behind type.

### Status chip
Live open/closed from the published hours (Worcester time): a translucent ink chip on the lead poster with a saffron dot and 3px saffron halo when open ("Open now · dinner until 9pm"), a paper dot at 70% when closed ("Closed now · opens tomorrow at 11:30am").

### Navigation
- **Pitch bar:** an ink strip above everything at micro size, stating the spec proposal, with a pill segmented control (A · Refresh / B · Rebrand) whose pressed option is saffron with ink type, and a Brand book link in pale saffron. Proposal apparatus; it goes away on a live site.
- **Masthead:** sticky bianco bar, min 4.25rem, 3px ink bottom seam; logo left, four links (Menu, What's on, Private dining, Visit) in Archivo 700 width 80 uppercase .92rem, a 3px mattone underline on hover and on the current page, and the Book a table button.
- **Phone (under 860px):** nav becomes a scrolling row under the logo; a fixed bottom action bar holds three doors (paper, paper, and mattone for the primary), 3.6rem tall with icon over micro caps.
- **Menu tabs:** a real tablist on the menu sheet; condensed 800 uppercase tabs with a 5px mattone underline on the selected tab, over a 3px ink seam; arrow, Home and End keys move between tabs; a hash opens a menu directly.

### Inputs / Fields
- **Style:** bianco ground, 2px ink border, 0 radius, padding .7rem .8rem, min 3rem; labels above in small uppercase 700 +0.06em; hints in soft ink.
- **Focus:** the global 3px focus outline.
- **Error:** border thickens to 3px mattone with a bold mattone message below; the first invalid field takes focus. Success replaces the form with an olive confirmation panel that names the room that fits the headcount.

### Menu sheet
A bianco sheet with the sheet shadow, holding the tablist and panels. Panels set sections in two columns (min 22rem), each headed by a 900 width-112 uppercase title over a 2px ink rule; dishes are a name / price grid with a description row beneath, 1px ink-14% rules, and olive micro tags (e.g. GF).

### Rooms
Seat-map cards for the three private spaces: soft plum (patio: olive), padded 1.5rem, capacity in poster type ("36 guests"), and a grid of saffron seat dots (paper dots on the patio), one dot per guest.

### Award bill
The awards set as one poster: three publication columns, each a small uppercase 800 head over a 2px ink rule, then award titles in 900 uppercase at clamp(1.4rem, 1rem + 1.6vw, 2.4rem), alternating width 112 and 72 like a printed bill; the Wine Spectator column in plum.

### Footer
Ink field with soft paper type: logo, address, phone with a Copy button, small uppercase column heads, social links as 2.75rem square outlined tiles (saffron on hover), and the Worcester Restaurant Group family links above a faint rule.

### Logo, two options
The site ships both and switches between them from the pitch bar (`data-logo` on the root, remembered per browser; B is the default). Never mix A and B in one piece.
- **Option A · Refresh (keep the gold mark):** VIA's existing Roman-capital mark, redrawn in Cinzel 700 as a stand-in (1.7rem, +0.06em, oro) over "Italian Table" (.5rem, +0.32em, uppercase, oro), on an ink block padded .35rem .8rem .4rem. Always on ink or plum; final artwork comes from VIA's master file.
- **Option B · Rebrand (the cut-paper VIA):** an SVG symbol (`#mark-b`, viewBox 294 by 120) of three letters cut from straight lines and one arc: a V, an I bar, and a flat-topped A whose counter is a notch, with a half-disc sun (radius 20 units) rising at the base of the A. Letters take the current colour; the sun takes `--sun-fill` (saffron by default, brick on a saffron ground). Lockup: the mark at 2.1rem high beside "Italian / Table" in 700 width 75, .72rem, +0.14em caps. On the home lead poster it is the h1 at up to 26rem wide. Clear space equals the sun's height on every side; minimum 64px wide on screen (18mm in print), below which "VIA" is set in Archivo Black. Works in ink, paper or any poster colour at 4.5:1 or better.

### Motion
One ease, `cubic-bezier(.16, 1, .3, 1)`, an expo-like ease-out. Posters arrive already visible and **settle** onto the wall (.9s, from triple tilt, 10px low and 1.5% large), staggered 90ms each, while a faint **paste brush** sheen sweeps across once (1.1s, 120ms behind). Buttons rise 2px over .25s; arrow links slide 3px; tabs tear over .45s. `prefers-reduced-motion: reduce` removes all of it and the JS skips the tear.

## Do's and Don'ts

### Do:
- **Do** build every offer, event and special as a poster with the five-part anatomy: art band, dates, title, body, tear-off tabs.
- **Do** give every time-limited poster a `data-end` date so it comes down by itself, and say "For a limited time" or "Any night" when there is no end date.
- **Do** fill whole fields with a poster stock (mattone, oliva, zafferano, prugna, ink) and keep bianco for set-text surfaces: masthead, menus, forms, booking fields.
- **Do** set paper type (#fbf6ee) on mattone, oliva, prugna and ink, and ink type on zafferano, bianco and muro.
- **Do** use Archivo only, varying width: 125 for poster type, 112 for headlines, 70 to 85 for labels, dates and actions, 100 for reading.
- **Do** keep rectangles square-cut and use curves only as whole cut-paper circles and half-discs from the six shapes.
- **Do** paste sheets with the paste shadow (`0 1px 0 rgba(0,0,0,.06), 0 10px 24px -14px rgba(28,21,18,.55)`) and a tilt under 1deg.
- **Do** keep book, order and plan-an-event one tap away on every page.
- **Do** put photos in labelled slots, pasted like clippings, with the shot and ratio named.

### Don't:
- **Don't** fall back to the category default this world replaces: a dark full-bleed food photo with a gold serif and a lone "Reserve" button.
- **Don't** set text over a photo or a cut-paper shape; shapes live in the art band, photos in slots.
- **Don't** use gold (oro) or Cinzel anywhere outside Logo Option A.
- **Don't** put paper type on saffron (2.0:1) or ink type on brick (2.8:1).
- **Don't** add gradients, outlines or textures to cut-paper shapes, or put more than three shapes in one poster.
- **Don't** round the corners of posters, buttons, tabs or fields.
- **Don't** stretch, outline or shadow Logo B, recolour its sun beyond saffron (or brick on saffron), or mix Options A and B in one piece.
- **Don't** let a promotion linger past its date or show a poster before its start date.
