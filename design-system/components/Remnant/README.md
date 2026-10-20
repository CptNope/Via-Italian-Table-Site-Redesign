What's left of an expired poster: a straight-trimmed `muro-deep` sheet, tilted, that the next live poster is pasted over.

- Use at most one per wall, to show the wall is current. It carries its poster's `data-end` and only appears once that date has passed; label it "Was <date> · pasted over".
- The live poster before it gets `.overlaps-next` (negative right margin and higher z-order, desktop only) so its edge lies over the remnant. On phones it stacks.
- Never link it. No clip-path, no strikethrough.
