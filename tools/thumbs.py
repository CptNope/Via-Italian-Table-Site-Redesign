#!/usr/bin/env python3
"""Regenerate assets/layouts/*.jpg thumbnails (needs: pip install playwright pillow; playwright install chromium)."""
import asyncio
from playwright.async_api import async_playwright
from PIL import Image
OUT=str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'assets' / 'layouts') + '/'
ROOT=str(__import__('pathlib').Path(__file__).resolve().parent.parent)
PAGES=[('index','a'),('home-partenze','b'),('home-manifesto','c'),('home-cucina','d')]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for n,k in PAGES:
            for w,h,t in [(1440,900,'desktop'),(390,844,'phone')]:
                pg=await b.new_page(viewport={'width':w,'height':h}, device_scale_factor=1, reduced_motion='reduce')
                await pg.goto(f'file://{ROOT}/{n}.html'); await pg.wait_for_timeout(500)
                # hide the proposal bar so thumbnails show the site itself
                await pg.add_style_tag(content='.pitch{display:none!important}')
                await pg.wait_for_timeout(100)
                f=f'{OUT}layout-{k}-{t}.png'
                await pg.screenshot(path=f)
                im=Image.open(f).convert('RGB')
                im=im.resize((960,600)) if t=='desktop' else im.resize((300,650))
                im.save(f.replace('.png','.jpg'), quality=82, optimize=True)
                import os; os.remove(f)
                await pg.close()
        await b.close()
asyncio.run(main())
