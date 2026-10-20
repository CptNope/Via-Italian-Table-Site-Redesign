# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS (plus light vanilla JS where needed) in a GitHub repo, deployable to any static host. Chosen by Jeremy for easy demo and hand-off.

## Users

- **Diners deciding where to eat tonight or this weekend** (Worcester / Central Mass locals, Shrewsbury Street regulars, date-night couples, business lunchers). Usually on a phone. Job: see the menu, check hours, book a table on Resy or call.
- **Takeout and delivery customers.** Job: get to Toast (takeout) or DoorDash (delivery) in one tap, ideally after glancing at the menu.
- **Event planners** (office lunches, rehearsal dinners, birthdays, showers). Job: learn which room fits their headcount, then send a Tripleseat request or call the event coordinator.
- **Regulars following what's on** (PigFest, wine & beer dinners, suckling pig dinners, holiday kits, $25 entrées). Job: see the current promotion and its dates.
- Secondary: gift-card buyers, job seekers (routed to Worcester Restaurant Group).

## Product Purpose

The website for VIA Italian Table, a chef-driven Italian restaurant at 89 Shrewsbury Street, Worcester, MA 01604 (508-754-4842), part of Worcester Restaurant Group alongside The Sole and 111 Chophouse. It exists to turn interest into a booked table, a takeout/delivery order, or an event inquiry, with balanced weight across all three (no single funnel dominates). Success: fewer taps from landing to Resy / Toast / DoorDash / Tripleseat, current menus and hours always findable, and seasonal events promoted without going stale.

**This build is an unsolicited spec pitch** to VIA / Worcester Restaurant Group by Jeremy Anderson (jeremyanderson.tech). No client sign-off exists. Use only publicly available facts; anything VIA has not published is a placeholder, labeled as such.

## Positioning

"Italian with a modern twist": an urban, exposed-brick room with an open kitchen where guests watch the chefs, spit-roasted meats and poultry, house-made gelato, a large pasta list drawing on Tuscan, Neapolitan and Sicilian recipes, and a cellar with Super Tuscans (Wine Spectator Award of Excellence). Event formats like PigFest and the whole suckling pig dinner are its own; the year-round patio on Shrewsbury Street's restaurant row is part of the pitch.

## Operating Context

- Reservations: **Resy**, or by phone 508-754-4842.
- Takeout: **Toast**. Delivery: **DoorDash**. Family-style to-go menu.
- Private dining: **Tripleseat** event request form, phone 508-798-3474, coordinator Maria Hawley, downloadable PDF brochure. Rooms: large private room (36), small semi-private room (16), year-round patio (36). Private luncheons/dinners Mon–Fri. Regular or custom menu; complimentary A/V.
- Hours (as published Oct 2026): Mon–Thu lunch 11:30–4, dinner 4–9; Fri lunch 11:30–4, dinner 4–10; Sat dinner 4–10; Sun closed.
- Parking: 111 Chophouse lot during lunch hours (11:30–4) only; after 4 pm any open space regardless of signage.
- Menus: dinner, lunch, dessert, drinks (PDF), gluten-free (PDF), kids (PDF), family-style to-go, seasonal (PigFest through Oct 31).
- Gift cards bought via Worcester Restaurant Group; balance checked via Toast. Careers on WRG site.
- Recurring promotions: PigFest, wine & beer/spirit dinners, suckling pig dinner, $25 entrées, holiday turkey kits (via WRG, phone 508-799-4111).
- Social: Facebook, Instagram, Twitter/X; reviews on Google and Tripadvisor; photos on Flickr; videos on YouTube.
- Staff update the site themselves today (WordPress on WP Engine); promotions must be easy to swap and must expire cleanly.

## Capabilities and Constraints

- External providers stay external: the site links to (or embeds) Resy, Toast, DoorDash, Tripleseat; it does not replace them.
- Menus must be readable HTML (not PDF-only) and mobile-first; PDFs may remain as downloads.
- Time-limited promotions carry explicit end dates and must not linger past them.
- Fix current-site defects: staging-domain links (viaitalian.wpengine.com), broken Tripadvisor URL, http links, "Dine In" pointing to a menu instead of reservations, unlabeled icon links, ~20-item nav.
- **Undecided:** final menu content and prices (use current published menus, marked as sample), real photography (placeholders until VIA supplies), whether to keep or replace the logo (see Brand Commitments).

## Brand Commitments

- Name: **VIA Italian Table** (short form "VIA"). Name stays.
- Identity direction is open: present **two options side by side**: (A) a refresh that keeps the existing VIA logo and builds a new system around it, and (B) a full rebrand with a new wordmark. VIA chooses.
- Voice (from existing copy): warm, inviting, celebratory, sensory; food, wine and gathering with family and friends as "a celebration of life."
- Family relationship: sits within Worcester Restaurant Group with The Sole and 111 Chophouse; footer cross-links remain.

## Evidence on Hand

- Awards (no years published): Telegram & Gazette / Worcester Living: Best Italian, Best Romantic Dinner, Best Outdoor Dining, Best Business Lunch. Worcester Magazine: Best Italian, Best Restaurant, Best High-Heeled Dinner Date. Wine Spectator: Award of Excellence.
- Existing site copy, menus and hours at viaitaliantable.com (fetched Oct 20, 2026).
- Existing logo file VIA-Italian-Table.png and a patio photo; no other assets in hand.
- **Absent, do not fabricate:** testimonials/review quotes, chef or owner names, opening year, award years, seat counts beyond private rooms, prices not published, press quotes.

## Product Principles

1. **Three doors, one tap each.** Book, order, or plan an event should each be reachable from any page without hunting.
2. **The menu is the product.** Menus are first-class HTML pages, fast on a phone, not buried PDFs.
3. **Show the kitchen.** The open kitchen, the spit, the gelato, the cellar are the proof; lead with them over generic "Italian" cues.
4. **Always current.** Hours, promotions and dates must be true today; expired content disappears.
5. **Easy for staff to keep alive.** Content changes (specials, events, hours) shouldn't require a designer.

## Accessibility & Inclusion

WCAG 2.2 AA. Labeled icon links, real text for menus, sufficient contrast over photography, gluten-free and kids options findable from the main menu page.
