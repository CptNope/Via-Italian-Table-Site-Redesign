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
  on-dark-soft: "color-mix(in oklab, #fbf6ee 88%, transparent)"
  on-light-soft: "color-mix(in oklab, #1c1512 74%, #f3efe7)"
  mattone-tab: "#802915"
  mattone-tab-hover: "#621d0e"
  mattone-deep-tab: "#5e1b0d"
  mattone-deep-tab-hover: "#471308"
  oliva-tab: "#3b4418"
  oliva-tab-hover: "#2b3310"
  zafferano-tab: "#cb8e23"
  zafferano-tab-hover: "#b9811f"
  prugna-tab: "#2d1125"
  prugna-tab-hover: "#210b1a"
  inchiostro-tab: "#130d0b"
  inchiostro-tab-hover: "#0c0806"
  bianco-tab: "#bbb7b1"
  bianco-tab-hover: "#918e89"
typography:
  poster:
    fontFamily: "Archivo, Archivo Black, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(4.5rem, 3rem + 9vw, 6rem)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: "-0.035em"
    fontVariation: "'wdth' 125"
  page-title:
    fontFamily: "Archivo, Archivo Black, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.2rem, 9.6vw, 6rem)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: "-0.035em"
    fontVariation: "'wdth' 125"
  poster-title:
    fontFamily: "Archivo, Archivo Black, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2rem, 1.4rem + 2.4vw, 3.4rem)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: "-0.035em"
    fontVariation: "'wdth' 125"
  poster-title-wide:
    fontFamily: "Archivo, Archivo Black, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(2.6rem, 1.6rem + 3.4vw, 4.8rem)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: "-0.035em"
    fontVariation: "'wdth' 125"
  poster-title-phone:
    fontFamily: "Archivo, Archivo Black, Helvetica Neue, Arial, sans-serif"
    fontSize: "clamp(1.9rem, 9.5vw, 2.6rem)"
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
    fontSize: "0.9rem"
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
    backgroundColor: "{colors.mattone-tab}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.6rem 0.5rem"
    height: "3.25rem"
  tear-off-tab-hover:
    backgroundColor: "{colors.mattone-tab-hover}"
  tear-off-tab-sun:
    backgroundColor: "{colors.zafferano-tab}"
    textColor: "{colors.inchiostro}"
  tear-off-tab-sun-hover:
    backgroundColor: "{colors.zafferano-tab-hover}"
  booking-strip:
    backgroundColor: "{colors.mattone-deep}"
    padding: "2px"
    width: "40rem"
  booking-field:
    backgroundColor: "{colors.bianco}"
    textColor: "{colors.inchiostro}"
    padding: "0.45rem 0.75rem 0.15rem"
  booking-select:
    textColor: "{colors.inchiostro}"
    typography: "{typography.body}"
    height: "2.75rem"
  headcount:
    backgroundColor: "{colors.mattone-deep}"
    padding: "2px"
    width: "40rem"
  headcount-field:
    backgroundColor: "{colors.bianco}"
    textColor: "{colors.inchiostro}"
    padding: "0.5rem 0.75rem 0.45rem"
  chip:
    backgroundColor: "rgba(28,21,18,.24)"
    textColor: "{colors.on-dark}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0.5rem 0.85rem"
    height: "2.75rem"
  chip-hover:
    backgroundColor: "{colors.inchiostro}"
  next-card:
    backgroundColor: "{colors.zafferano}"
    textColor: "{colors.inchiostro}"
    rounded: "{rounded.none}"
    padding: "1rem 1.5rem"
    width: "32rem"
  paste-head:
    backgroundColor: "{colors.bianco}"
    textColor: "{colors.inchiostro}"
    rounded: "{rounded.none}"
    padding: "0.85rem 1.25rem"
  copy-button:
    backgroundColor: "transparent"
    typography: "{typography.micro}"
    rounded: "{rounded.none}"
    padding: "0.3rem 0.85rem"
    height: "2.75rem"
    width: "2.75rem"
  skip-link:
    backgroundColor: "{colors.bianco}"
    textColor: "{colors.inchiostro}"
    rounded: "{rounded.none}"
    padding: "0.6rem 1rem"
    height: "2.75rem"
  logo-picker:
    backgroundColor: "{colors.zafferano}"
    textColor: "{colors.inchiostro}"
    rounded: "{rounded.arc}"
    padding: "0.35rem 1.9rem 0.35rem 0.8rem"
    height: "2.75rem"
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
- Switchable identities inside the same poster world: A (the existing gold mark) or one of seven cut-paper VIA wordmarks (B1 to B7), picked from the proposal bar.
- Every page opens on a lead poster, and the next sheet is pasted over its bottom edge.

## Colors

Four poster stocks, an ink, a paper and the wall; every stock is flat and fully saturated for its hue, and each owns whole fields.

### Primary
- **Mattone, Brick Red** (#a8381f): the lead poster on the home page, private dining and the 404, the Book a table button, the active nav underline, the menu tab underline, the primary phone action, focus outline inside booking and headcount fields, the skip link's outline, invalid-field borders and error text on paper. The colour of the exposed brick room.
- **Mattone Scuro, Shadow Brick** (#7c2715): the booking strip's and headcount finder's frame, the brick variant poster (Thanksgiving kit), default photo-slot ground, pressed/shadow states.

### Secondary
- **Oliva, Olive** (#4f5b23): menus and the kitchen; the menu page's lead poster, the $25 entrées poster, the patio room, menu dish tags, the form confirmation panel, and the bullets of positive brand-book rules.
- **Oliva Scura, Deep Olive** (#3a4419): olive photo-slot ground only.

### Tertiary
- **Zafferano, Saffron** (#eaa42a): the sun. Dates and highlights, the Visit lead poster, the PigFest poster, the next-up card, the logo picker, the "Find a table" and "Request a room" buttons, the open-now status dot, today's row in the hours table, seat dots in room maps, global focus outline (3px), text selection, and the sun inside the B wordmarks (Sole, Arco, Tondo, Monogramma).
- **Zafferano Chiaro, Pale Saffron** (#f6d58e): links inside the ink pitch bar only.
- **Prugna, Super Tuscan Plum** (#3e1a33): wine, evenings and rooms; the What's on lead poster, the Cakebread wine-dinner poster, the "Plan an event" door, the plate disc in the lead composition, the Wine Spectator column in the award bill, and the focus outline on saffron, paper and wall fields.
- **Prugna Chiara, Soft Plum** (#5b2a4b): room cards, the wine-glass shape, plum photo slots.

### Neutral
- **Inchiostro, Ink** (#1c1512): all type on light fields, the masthead's bottom seam, the footer, the pitch bar, the ink poster (suckling pig), the spit stripe, and the ground for Logo A.
- **Bianco, Poster Paper** (#f3efe7): set-text surfaces only: masthead, menu sheet, forms, booking-strip and headcount fields, paper buttons, the wall heading slip and paste heads, the skip link, the phone action bar.
- **Muro, Plaster Wall** (#d8cfc0): the body background behind everything, and the seam colour between pasted fields.
- **Muro Scuro, Old Plaster** (#b9ad99): the torn remnant of an expired poster.
- **Oro, Incumbent Gold** (#d9a640): Logo Option A only.
- **On-dark Paper Type** (#fbf6ee): type on mattone, oliva, prugna and ink.
- **Soft Paper Type** (on-dark-soft: paper at 88%, mixed in oklab toward transparent): secondary text on dark fields: poster date lines and body, the book note, room and award notes, the footer, the pitch bar.
- **Soft Ink** (on-light-soft: ink mixed 74% toward bianco in oklab, about #4d4641): secondary text on paper and wall: field labels, hints, menu notes and descriptions, paste-head sublines, wall-head notes, unselected menu tabs. On saffron posters the soft colour is ink 78% toward saffron instead.

### Tab shades
Each poster stock has a pressed-darker pair for its tear-off tabs, precomputed as tokens (the stock mixed in oklab toward black: 82% for the tab, 68% on hover; saffron uses 90% and 84% so ink type stays legible). A poster picks its pair through `--p-tab` / `--p-tab-hover`.
- **Mattone** tab / hover (#802915 / #621d0e); **Mattone Scuro** (#5e1b0d / #471308); **Oliva** (#3b4418 / #2b3310); **Zafferano** (#cb8e23 / #b9811f); **Prugna** (#2d1125 / #210b1a); **Inchiostro** (#130d0b / #0c0806); **Bianco** (#bbb7b1 / #918e89).
- Tab shades are for tabs only; they never become a field or a text colour.

### Named Rules

**The Drenched Field Rule.** Colour comes as whole poster fields, never as a thin accent stripe or tinted card. A typical page by area runs roughly mattone 24%, muro 20%, oliva 16%, prugna 14%, ink 14%, zafferano 12%.

**The Ink-or-Paper Rule.** Text on mattone, oliva and prugna is paper (#fbf6ee); text on zafferano, bianco and muro is ink. Paper on saffron (2.0:1) and ink on brick (2.8:1) fail and are never used for text. Measured pairs: paper on mattone 6.0:1, paper on oliva 6.8:1, paper on prugna 13.9:1, ink on saffron 8.4:1, mattone on bianco 5.6:1.

**The Gold Belongs to A Rule.** Oro appears only inside Logo Option A, always on an ink or plum ground. The new world never borrows gold.

## Typography

**Display Font:** Archivo variable (weights 100 to 900, width 62% to 125%), self-hosted, with Archivo Black, Helvetica Neue, Arial fallbacks
**Body Font:** Archivo (same file) at width 100
**Logo A stand-in:** Cinzel 700 (with Trajan Pro, Georgia), used only to redraw VIA's existing Roman-capital mark until master artwork arrives

**Loading:** both faces are self-hosted variable fonts served WOFF2 first with a WOFF fallback, `font-display: swap`. Archivo's WOFF2 is preloaded in every page head. Cinzel is never preloaded: its only user, the Logo A block, is `display: none` unless `data-logo="a"`, so the browser fetches Cinzel only when Logo A is actually shown.

**Character:** One grotesque played like a case of wood type: expanded black caps shout the name of the thing, narrow bold caps carry dates, prices and actions, and the regular width reads quietly underneath. Width, not a second family, makes the contrast.

### Hierarchy
- **Poster** (900, width 125, uppercase, line-height 0.86, letter-spacing -0.035em): the name of the thing, at four sizes, each a token. **Page title** clamp(2.2rem, 9.6vw, 6rem) for lead-poster titles on every inner page ("What's on", "Private dining", "Visit"); it never has to split a word at 320px. **Poster title** clamp(2rem, 1.4rem + 2.4vw, 3.4rem) for a poster on the wall; **wide** clamp(2.6rem, 1.6rem + 3.4vw, 4.8rem) on w-7 and wider posters; **phone** clamp(1.9rem, 9.5vw, 2.6rem) for every poster title under 620px. The 6rem ceiling (clamp(4.5rem, 3rem + 9vw, 6rem)) stays for proposal-page titles. Room capacities ("36 guests") use poster type too. Manual soft hyphens only.
- **Headline** (900, width 112, sentence case, h1 clamp(2.6rem, 1.8rem + 3.6vw, 4.5rem) / h2 clamp(2rem, 1.5rem + 2.2vw, 3.25rem), line-height 1.02, -0.03em): section heads such as "On the wall this week", "Three rooms for a party". Balanced wrapping.
- **Title** (800, clamp(1.35rem, 1.15rem + .8vw, 1.75rem), line-height 1.1, -0.015em): facts, room names, the wall heading slip. Menu section heads use 900 / width 112 / 1.6rem uppercase over a 2px ink rule.
- **Lead** (400, clamp(1.1rem, 1rem + .4vw, 1.3rem), line-height 1.5, max 38ch): the one-paragraph introduction under a lead poster or page title.
- **Body** (400, width 100, 1.0625rem / 17px, line-height 1.55, measure 66ch): all reading text. Poster body text caps at 46ch.
- **Label** (700 to 800, width 70 to 85, uppercase, +0.02em to +0.05em, all at the small size .9rem): buttons and chips (800 / 85), tear-off tabs (800 / 78), nav (700 / 80, +0.04em), menu tabs (800 / 80), dates and condensed lines (700 / 70). Field labels inside the booking strip and headcount finder use micro size with +0.08em.
- **Small roles, consolidated:** three sizes only. **Body** (1.0625rem) for reading and form values; **small** (.9rem) for labels, buttons, tabs, nav, and small prose (poster date lines, notes, captions, hints); **micro** (.78rem) for the pitch bar, field labels, photo-slot heads, dish tags, copy buttons and action-bar captions. Don't invent a fourth.
- **Prices** (800, tabular figures, no wrap): every price and phone number on the site.

### Named Rules

**The One Family Rule.** Archivo is the only typeface of the world. Contrast comes from the width axis (125 / 112 / 100 / 85 / 70) and weight, never from a second display face. Cinzel exists only as Logo A's placeholder, and is only downloaded when Logo A is on screen.

**The Date Leads Rule.** On any poster the bold date (start or end) is the first line of text, then the kind of thing it is, in small type: "Tuesday, Dec 8 · 6:30 pm · Wine dinner". A poster with no end date says so ("For a limited time", "Any night").

**The Name, Not a Slogan Rule.** Poster type sets the name of the thing (PigFest, Whole suckling pig, $25 entrées), never a tagline.

## Layout

The page is a vertical stack of full-bleed **fields**, each one poster sheet, padded 4.5rem top and bottom (3rem under 620px) with a 16px minimum side gutter that respects safe-area insets. Consecutive fields are separated by a 3px seam of muro, so the wall shows between sheets. Content sits in an 82rem centred wrap.

The home page opens with a full-bleed mattone **lead poster**: a two-column grid (1.15fr / .85fr, bottom-aligned). Left: the chosen logo at poster scale as the h1, a lead paragraph, the live open/closed status chip, the booking strip, a one-line booking note, and the two sibling doors (Order takeout, Delivery) plus Plan an event. Right: a cut-paper composition (saffron half-sun bleeding off the bottom right, plum plate disc, ink spit stripe at -24deg) with a pasted 4:5 photo slot rotated 2.2deg. The next field (the wall) is pulled up 2.25rem so its heading slip overlaps the lead poster's bottom edge, already pasted.

**The wall** is a 12-column dense grid (gap 1.5rem by 1rem) of posters spanning 4, 5, 6, 7, 8 or 12 columns. Posters align to the top, each carries its own tilt between -0.9deg and +0.7deg, and one may overlap its neighbour (-3rem right margin on wide screens). Remnants of expired posters take 3 columns.

**Inner pages carry layout A through.** Every inner page (Menu, What's on, Private dining, Visit, and the 404) opens on its own full-bleed **inner lead poster** built on the same two-column lead grid: page-title poster type, a lead, the page's working action (menu chips and order doors; the next-up card; the headcount finder; status and directions), and a cut-paper composition with a pasted photo slot on the right. Each page owns a stock: menu oliva, events prugna, private dining mattone, visit zafferano, 404 mattone. The inner lead is padded 3rem on top and 4.5rem + 1rem below (3rem + 1rem under 860px, where the art drops to 18rem and its extra glass, stem and table pieces hide); the art is at least 24rem tall on wide screens.

The field after a lead poster is marked **after-lead**: it loses its top padding and seam, and its first block is pulled 3rem up over the poster's bottom edge (2.25rem under 620px), stacked above it, so the next sheet is visibly pasted over the lead. When that block starts with a heading, the heading is a **paste head**: a bianco label slip (see Components).

The older **page head** field (poster-type title at the 6rem ceiling, lead, and a saffron sun clamp(16rem, 10rem + 24vw, 34rem) bleeding off the bottom right) survives only on the proposal pages (Logos, Layouts).

**Alternate homepages.** Layout A (the lead poster and wall above) is the site's default homepage and the system's reference. Three alternates exist as pages for VIA to compare on the Layouts page, each in the same palette, type and paste language with its own page-local styles: **B · Partenze** (what's coming up as a dark split-flap departures board whose letters flip into place once on arrival, with booking as a paper ticket beside it), **C · Manifesto** (the first screen as one paper playbill on a mattone field, hours, booking strip and the two big dates set in mixed wood-type widths), and **D · Cucina** (an olive field with a tilted paper menu sheet of signature dishes and prices beside the wordmark and booking strip). They are proposals, not system patterns: new surfaces follow layout A.

**Breakpoints:** at 1060px the wall drops to 6 columns (4/5/6-span posters become 3; 7/8/12 go full width) and rooms go 2-up with the patio full width. At 860px the masthead wraps, the nav becomes a horizontally scrolling row under the logo, the lead poster stacks to one column, the masthead Book button hides, and a fixed three-door **phone action bar** appears at the bottom (body gains matching bottom padding). At 620px the wall is one column, the booking strip goes 2-up with a full-width button, and menu tabs scroll horizontally. At 400px awards go single column.

**The Three Doors Rule.** Book (Resy), order (Toast / DoorDash) and plan an event (private dining / Tripleseat) are reachable in one tap from every page: masthead Book button and nav on wide screens, the fixed action bar on phones, and the lead poster's strip and doors on home.

**The Thumb Rule.** Every interactive control is at least 2.75rem (44px) tall: buttons (3rem; 2.75rem in the masthead), copy buttons (2.75rem square minimum), nav links (2.75rem at every width), booking-strip selects, the headcount input, chips, the logo picker, pitch-bar links, footer family and social links (2.75rem square), and the skip link. Tear-off tabs (3.25rem) and the phone action bar (3.6rem) run larger.

## Elevation & Depth

Depth is paper pasted on plaster. There are no floating cards, no glass, no blur, and no hard offset shadows. A poster, button, room card or photo slot sits on the wall with a single soft **paste** shadow: a hairline lip plus a short, tight drop below. The other depth cues are physical: a fraction of a degree of rotation, overlapping edges, the muro seam between fields, and dashed tear lines. Larger sheets that sit further off the wall (the menu sheet, the booking strip) get a longer, softer drop.

### Shadow Vocabulary
- **Paste** (`box-shadow: 0 1px 0 rgba(0,0,0,.06), 0 10px 24px -14px rgba(28,21,18,.55)`): the default for every pasted sheet: posters, buttons, room cards, photo slots, remnants, paste heads, the next-up card, the skip link, brand-book cards.
- **Paste lift** (`box-shadow: 0 1px 0 rgba(0,0,0,.06), 0 16px 26px -14px rgba(28,21,18,.6)`): button hover, paired with a 2px rise.
- **Strip** (`box-shadow: 0 18px 40px -22px rgba(0,0,0,.6)`): the booking strip and the headcount finder inside a lead poster.
- **Sheet** (`box-shadow: 0 30px 60px -36px rgba(0,0,0,.7)`): the menu sheet.
- **Ghost edge** (`box-shadow: inset 0 0 0 2px currentColor`, 3px on hover): ghost buttons; a printed outline, not a shadow.

### Named Rules

**The Pasted, Not Floating Rule.** Every raised element uses the paste shadow and stays square to the wall or tilted by under 1deg (photo clippings up to about 2.2deg). Nothing hovers with a large diffuse glow.

## Shapes

Rectangles are square-cut: posters, buttons, tabs, fields, inputs, room cards and sheets all have 0 radius. Curves appear only as whole cut-paper shapes: full circles (the plate, the coins, seat dots, the status dot) and half-discs cut with a 999px radius on two corners (the sun, the glass bowl, the table). The 2px radius on focus rings and the pill logo picker in the pitch bar are interface apparatus, not part of the poster world. Inside the logo concepts, Targa's street plate has its own small corner radii (14, 6 and 2 units in its 380 by 200 drawing); that belongs to the mark, not to site surfaces.

### The six cut-paper shapes
Each shape is cut from a poster colour and stands for something real at VIA. They live in a poster's art band (the top strip, bled to the poster's edges, 4.5 to 9.5rem tall) or in a lead/page-head composition, never behind running text. Flat fills only; they may overlap and bleed off the edge like paper trimmed after pasting; one composition per poster, two or three shapes at most.

1. **The sun, the fire**: a half-disc (top corners 999px) rising from a bottom edge, usually mattone on saffron or saffron on mattone. The spit's fire; the arch of a street; also the sun inside the A of the Sole wordmark.
2. **The plate**: a full plum disc.
3. **The spit**: a long ink stripe (10 to 14px) crossing the field at a shallow angle (-4deg to -24deg), sometimes skewering a plate disc.
4. **The glass**: a soft-plum bowl (bottom corners 999px) on an 8px stem; wine dinners.
5. **The coins, a deal**: three equal circles in a row (saffron, mattone, bianco), half sunk below the art band; the $25 entrées.
6. **The table set**: a bianco plate disc or half-disc flanked by two 6px saffron uprights (knife and fork); the Thanksgiving kit and other at-home tables.

### Art-band compositions
A poster's art band is one class on the band, with the shapes as empty child spans; geometry is tuned through custom properties, never inline coordinates.
- **Sun and spit** (`art-sunspit`; children sun, optional plate, spit): a half-sun rising from the band's floor with the spit across it. Variables: `--sun` (mattone), `--sun-w` (20rem; the sun is half as tall), `--sun-x` (8% from the right), `--spit` (ink), `--spit-y` (4rem up), `--spit-tilt` (3deg), `--plate` (prugna; the plate is a quarter of the sun's width, sitting just left of it). PigFest, the suckling pig.
- **Coins** (`art-coins`; three coins): 7rem discs, 5.5rem apart, half sunk (bottom -3.5rem), in saffron, mattone, bianco. A deal.
- **Glass** (`art-glass`; a cup, an optional second cup, a stem): an 8rem bowl hanging from the band's top edge 3rem from the right on an 8px, 3rem stem. Variables: `--cup` (8rem), `--glass` (prugna-soft), `--glass-2` (mattone; the second cup sits .8 cup-widths left at 85%). Wine.
- **Table** (`art-table`; a plate and two bars): a 6rem bianco disc half sunk at centre between two 6px, 4rem saffron uprights. Holiday kits.
- **Pair** (`art-pair`; two discs): two 7rem discs sunk 2rem, saffron with olive printed over it (multiply). Takeout and VIA at home.

## Components

### Buttons
Character: a printed label slapped on the wall: square, condensed bold caps, pasted.
- **Shape:** square-cut (0 radius), minimum 3rem tall (2.75rem in the masthead).
- **Primary:** mattone with paper type, padding .7rem 1.25rem, Archivo 800 width 85, uppercase, small (.9rem), +0.05em, with an optional 1.15em leading icon.
- **Hover / Focus:** rises 2px with the paste-lift shadow over .25s on the house ease-out; returns flat on press. Focus is a 3px saffron outline offset 3px (plum on saffron, paper and wall fields).
- **Variants:** sun (saffron, ink type; the booking strip's "Find a table"), paper (bianco, ink; Order takeout, Delivery), plum (prugna, paper; Plan an event), ink, and ghost (transparent with a 2px inset edge in the current colour, 3px on hover). Disabled is 50% opacity, no rise.
- **Arrow link:** condensed 800 uppercase text with a trailing arrow that slides 3px on hover.
- **Copy button:** a printed 1.5px outline in the current colour, micro 700 uppercase +0.06em, padding .3rem .85rem, at least 2.75rem by 2.75rem; reads "Copied" for 1.4s after copying.

### Chips
Quick jumps inside a lead poster (the menu's Dinner, Lunch, Dessert, PigFest, Family style; the 404's way back). A wrapping row with .4rem gaps of square-cut labels: 800 width 85 uppercase, small, +0.05em, padding .5rem .85rem, at least 2.75rem tall, on a translucent ink ground (rgba(28,21,18,.24)) with paper type, going solid ink on hover over .2s. No shadow, no tilt: chips are printed on the poster, not pasted on it. A dated chip carries `data-end` and comes down with its poster.

### Booking strip (signature)
The working action inside the lead poster: a shadow-brick frame (2px padding, 2px gaps) holding two paper fields (Party, Date) and a saffron "Find a table" button, max 40rem wide. Field labels are micro, uppercase, +0.08em, in soft ink; values are 700 at body size (1.0625rem), and each select is at least 2.75rem tall. The date list is generated for the next 21 days with Sundays shown as "closed" and disabled; there is no time field because Resy's link takes only date and party size. Submitting hands `?date=&seats=` to Resy; "9 or more" routes to private dining.

### Headcount finder (private dining)
The booking strip's sibling on the private-dining lead poster, in the same shadow-brick frame (2px padding and gaps, max 40rem, strip shadow). A paper field asks "How many guests?" (micro label; the number in 800 at 1.4rem, tabular, 6.5rem wide), and a paper output beside it names the room as you type: up to 16, the semi-private room; up to 36, the private dining room or the patio; more, a call to Maria. Below, a full-width saffron "Request a room" button jumps to the request form and prefills its guest count. It stacks to one column under 620px. The output is a polite live region.

### Next up (events)
The first live item on the What's on lead poster, shown as a single saffron card pasted at -0.8deg: a condensed date line, the name in 900 width 112 uppercase at title size, and an arrow call ("See the menu", "Register") whose arrow slides 3px on hover. Card padding 1rem 1.5rem, max 32rem, paste shadow, a 2px dashed ink-40% tear line along its bottom. The markup lists several candidates in date order, each dated with `data-end`; expired ones are removed by the script and only the first remaining one shows, so the card always names what is actually next. The last candidate is undated ("Any night, by arrangement") so the card is never empty.

### Paste head
The heading of a block pulled over a lead poster's edge: a bianco slip (padding .85rem 1.25rem, paste shadow, -0.6deg), sized to its content, holding an h2 in 900 width 112 at title size and a one-line subline in small soft ink, wrapping side by side. Same object as the wall's heading slip on home.

### Poster (signature)
Every offer, event and special is one poster built the same way, top to bottom:
1. **Art band**: the cut-paper composition, bled to the top and side edges, clear of text.
2. **Dates**: bold start or end date first, then what kind of thing it is (small type, soft colour).
3. **Title**: poster type, the name of the thing.
4. **Body**: one or two plain sentences, and real dishes with real prices when there are any (an item list with 1px rules in the poster's own type colour at 22%, prices in tabular 800).
5. **Tear-off tabs**: one to three actions.

Posters are square-cut, padded 1.5rem (0 at the bottom, where the tabs sit), carry the paste shadow and a per-poster tilt (`--tilt`, -0.9deg to +0.7deg). Stocks: mattone (default), olive, plum, sun (saffron with ink type), paper, brick (shadow brick), ink. A poster with `data-end` is removed the day after its date; one with `data-start` stays down until then.

### Tear-off tabs (signature)
The poster's actions, cut like an Italian street flyer. A row of equal tabs across the poster's full width, separated from the body and from each other by 2px dashed lines in the poster's type colour at 45%. Each tab is at least 3.25rem tall, Archivo 800 width 78, uppercase, small (.9rem), on the poster's own tab shade token (see Colors: the stock pressed darker), switching to its hover shade on hover. Each poster stock sets `--p-tab` and `--p-tab-hover` to its pair. On press the tab tears: it drops 14px and rotates a random -5deg to +5deg over .45s, and the link follows after 320ms. Phone and anchor links tear and spring back. Reduced motion and modified clicks skip the tear.

### Remnant
The pasted-over trace of an expired poster: muro-deep, ink type, 1.4deg tilt, paste shadow, condensed line "Was Tue, Jun 16 · pasted over" and the event's title. It only appears once its poster's date has passed.

### Page not found (404)
The 404 is the remnant idea at page scale: a mattone inner lead poster titled "This poster came down", a one-line lead, chips back to every section, and the Book and phone doors. Its art is the saffron sun with a large muro-deep remnant pasted at 4deg reading "Was here · pasted over / 404". It resolves links from the site root so it works at any path.

### Photo slots
Labelled frames for VIA's own photography: a hatched ground (135deg ink hairlines every 14px over shadow brick, soft plum, deep olive, warm ink or pale paper), an inset dashed frame at 45%, a camera icon top right, and a caption naming the shot and ratio. Pasted like a clipping with the paste shadow and a small tilt. Never full-bleed, never behind type.

### Status chip
Live open/closed from the published hours (Worcester time): a translucent ink chip on the lead poster with a saffron dot and 3px saffron halo when open ("Open now · dinner until 9pm"), a paper dot at 70% when closed ("Closed now · opens tomorrow at 11:30am").

### Navigation
- **Skip link:** the first focusable element on every page. Hidden off-screen until it receives keyboard focus, then it appears as a paper tab fixed over the masthead (16px from the left, .75rem below the safe area): bianco, ink 800 uppercase +0.05em, padding .6rem 1rem, at least 2.75rem tall, paste shadow, 3px mattone outline offset 2px. It jumps to the main region, which takes focus without an outline.
- **Pitch bar:** an ink strip above everything at micro size in soft paper type, stating the spec proposal, with the **logo picker** (a pill select, saffron with ink 700 type, at least 2.75rem tall, a drawn chevron, pale-saffron focus outline) and links to the Brand book, Logos and Layouts pages in pale saffron, each at least 2.75rem tall. Proposal apparatus; it goes away on a live site.
- **Masthead:** sticky bianco bar, min 4.25rem, 3px ink bottom seam; logo left, four links (Menu, What's on, Private dining, Visit) in Archivo 700 width 80 uppercase small (.9rem) +0.04em, a 3px mattone underline on hover and on the current page, and the Book a table button (2.75rem).
- **Phone (under 860px):** nav becomes a scrolling row under the logo, each link at least 2.75rem by 2.75rem; a fixed bottom action bar holds three doors (paper, paper, and mattone for the primary), 3.6rem tall with icon over micro caps.
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
Ink field with soft paper type: logo (the mark at 2.6rem high), address, phone with a Copy button, small uppercase column heads, social links as 2.75rem square outlined tiles (saffron on hover), and the Worcester Restaurant Group family links (each 2.75rem tall) above a faint rule.

### Logo options and the logo picker
The site ships eight logo options and swaps between them from the logo picker in the pitch bar. Never mix two options in one piece.

**The B family (new cut-paper wordmark).** All seven are built from the same three letters cut from straight lines only: a V, an I bar, and a flat-topped A whose counter is a notch (letters drawn in a 294 by 120 box), plus one VIA-specific device. They are defined once in the logo generator, which writes both the standalone SVG colourways in the logos folder and the recolourable symbols (`mark-sole`, `mark-spiedo`, `mark-arco`, `mark-targa`, `mark-tondo`, `mark-biglietto`, `mark-monogramma`) inlined into every page; `mark-b` remains as an alias of Sole with a `--sun-fill` hook for the brand book.
- **B1 Sole** (viewBox -12 -12 318 144): a half-disc sun (radius 20 units) rises inside the base of the A. The default and primary mark: masthead, signage, menus. Under 32px tall switch to Monogramma.
- **B2 Spiedo** (-12 -12 318 144): a 10-unit spit cut through all three letters at -5deg, a radius-19 disc turning on the I. Alternate primary; needs about 48px of height.
- **B3 Arco** (-12 -36 318 168): the letters stand in front of a large half-sun (radius 120). Posters, banners, the lead poster.
- **B4 Targa** (0 0 380 200): an Italian street plate: frame, paper plate, inset 3-unit rule, letters. Building sign, door, menu covers; does not work small.
- **B5 Tondo** (0 0 300 300): a round stamp: disc ground, sun rising from its bottom, letters at 69%. Stickers, avatar, gift card.
- **B6 Biglietto** (0 0 324 222): the wordmark as a ticket with a dashed tear line and three tear-off tabs. Tickets and gift cards; nothing under 80px wide.
- **B7 Monogramma** (-10 -10 140 140): the V alone with a radius-15 sun in its valley. Favicon (the on-mattone colourway is the site favicon), app icon, embroidery.

**Recolouring.** The symbols take their colours from custom properties, with defaults that suit a light ground: `--m-ink` letters (current colour), `--m-accent` sun, disc or arc (saffron), `--m-ground` Tondo's disc (mattone), `--m-on` letters on that disc (paper), `--m-frame` Targa's frame and rule (mattone), `--m-plate` Targa's plate (bianco), `--m-plate-ink` Targa's letters (ink), `--m-ticket` Biglietto's ticket (saffron), `--m-ticket-ink` its letters and tear line (ink), `--m-tabs` its tabs (mattone). The stylesheet's switchable-marks rules set them per context so no mark vanishes into its field: Spiedo's disc is mattone on light grounds and saffron on mattone, prugna, ink and olive fields and in the footer; Tondo's disc turns prugna on a mattone field; Targa's frame turns saffron on mattone; Biglietto's ticket turns bianco on saffron; Arco's sun turns mattone on saffron. Sizes vary by concept and context too: the compact marks (Tondo, Monogramma, Targa, Biglietto) sit 2.9rem high in the masthead; in the home lead poster the wordmark is up to 26rem wide, Arco 24rem, Targa and Biglietto 22rem, Tondo and Monogramma up to 15rem (70%).

**Option A · Refresh (keep the gold mark):** VIA's existing Roman-capital mark, redrawn in Cinzel 700 as a stand-in (1.7rem, +0.06em, oro) over "Italian Table" (.5rem, +0.32em, uppercase, oro), on an ink block padded .35rem .8rem .4rem. Always on ink or plum; final artwork comes from VIA's master file.

**Switching.** The choice lives in `data-logo` on the root element (`a`, `sole`, `spiedo`, `arco`, `targa`, `tondo`, `biglietto`, `monogramma`; the legacy value `b` means Sole; anything unknown falls back to Sole). A head script sets it before first paint from a `?logo=` link, else from the browser's remembered choice (`via-logo` in local storage). Choosing in the picker points every site mark at the chosen symbol and its viewBox, remembers it, and, when the page was opened from a `?logo=` link, rewrites the URL and every internal link so a shared link keeps its logo as the viewer clicks around. Choosing A hides every B mark and shows the gold block.

**B lockup and use.** In the masthead the mark sits 2.1rem high beside "Italian / Table" in 700 width 75, .72rem, +0.14em caps. On the home lead poster it is the h1. Clear space equals the sun's height on every side; minimum 64px wide on screen (18mm in print), below which "VIA" is set in Archivo Black. Works in ink, paper or any poster colour at 4.5:1 or better.

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
- **Do** open every inner page on its own lead poster and paste the next block over its bottom edge, headed by a paper paste head.
- **Do** compose art bands from the five art classes (sun and spit, coins, glass, table, pair) and tune them with their custom properties, not inline geometry.
- **Do** make every interactive control at least 2.75rem (44px) tall.
- **Do** use the tab shade tokens for tear-off tabs, set through `--p-tab` and `--p-tab-hover`.
- **Do** keep type to three small roles: body 1.0625rem, small .9rem, micro .78rem.

### Don't:
- **Don't** fall back to the category default this world replaces: a dark full-bleed food photo with a gold serif and a lone "Reserve" button.
- **Don't** set text over a photo or a cut-paper shape; shapes live in the art band, photos in slots.
- **Don't** use gold (oro) or Cinzel anywhere outside Logo Option A.
- **Don't** put paper type on saffron (2.0:1) or ink type on brick (2.8:1).
- **Don't** add gradients, outlines or textures to cut-paper shapes, or put more than three shapes in one poster.
- **Don't** round the corners of posters, buttons, tabs or fields.
- **Don't** stretch, outline or shadow a B mark, recolour it outside the poster palette through anything but its `--m-*` properties, or mix two logo options in one piece.
- **Don't** preload Cinzel or load it anywhere Logo A is not shown.
- **Don't** treat the alternate homepages (Partenze, Manifesto, Cucina) as system patterns; layout A is the default.
- **Don't** let a promotion linger past its date or show a poster before its start date.
