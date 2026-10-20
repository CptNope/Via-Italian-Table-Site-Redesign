The core unit of the system: one offer, event or special, built like a street poster.

Anatomy, top to bottom: `.poster-art` (the cut-paper composition, clipped, clear of text) → `.poster-dates` (bold date first, then the kind of thing) → title in `.poster-type` (`poster-m`) → `.poster-body` (one or two sentences, or an `.items` price list) → `.tabs` (1–3 tear-off actions).

Colour by class: `poster--sun` (zafferano, ink text), `poster--olive`, `poster--plum`, `poster--brick` (mattone-deep), `poster--ink`, `poster--paper`; the default is mattone. Width on the wall by class `w-4` … `w-12`; tilt with `--tilt` between −1deg and 1deg.

- Every poster with an end date carries `data-end="YYYY-MM-DD"`; the site script removes it the day after. No end date: say so in the dates line ("For a limited time").
- Tabs tear on press (320ms) before following the link; `tel:` tabs tear and spring back.
- Two or three shapes in the art band, from the six in the README. Never behind text.
- The consumer provides dates, title, body or items, actions, colour and width.
