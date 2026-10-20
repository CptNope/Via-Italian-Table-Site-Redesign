A menu printed on poster paper: `bianco` sheet, ink rules, tabs for each menu, dishes in two newspaper columns.

- Menus are real HTML from `data/menus.json` (section → items with name, price, description, optional tag), never PDF-only.
- Section heads: width 112, weight 900, uppercase, 2px ink rule beneath. Dish name weight 800; price weight 800, tabular, right-aligned.
- Tags (`.tag`, oliva) only for dietary facts VIA publishes: GF penne, GF crust +$4.
- Tabs are a real `tablist` with arrow-key support; `#dinner`, `#lunch` etc. open a tab.
