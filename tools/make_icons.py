"""Make the EMM logo files, favicon, app icons and social-sharing image.

Run after changing tools/emm_mark.py:   python3 tools/make_icons.py
Needs: Pillow and Playwright.
"""
import asyncio
import base64
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from emm_mark import mark, svg  # noqa: E402

IMG = ROOT / "static" / "img"
FONTS = ROOT / "static" / "fonts"
SPRUCE, GOLD, GOLD_LIGHT = "#14403C", "#B8862B", "#D9A846"
NAMES = {"en": ("Excellence Ministry", "Management"),
         "es": ("Excelencia en", "Administración Ministerial")}


def font(name):
    return "data:font/woff2;base64," + base64.b64encode((FONTS / name).read_bytes()).decode()


CSS = f"""
@font-face {{ font-family: L; src: url('{font("literata-latin-600-normal.woff2")}'); }}
@font-face {{ font-family: F; src: url('{font("libre-franklin-latin-600-normal.woff2")}'); }}
body {{ margin: 0; }}
.lk {{ display: inline-flex; align-items: center; gap: 22px; padding: 24px 28px; }}
.mk {{ width: 118px; flex: none; line-height: 0; }}
.t1 {{ font: 600 64px/0.9 L; color: {SPRUCE}; letter-spacing: 0.02em; }}
.rule {{ height: 3px; width: 56px; background: {GOLD}; margin: 12px 0 10px; }}
.t2 {{ font: 600 19px/1.25 F; color: {SPRUCE}; letter-spacing: 0.01em; }}
.dark {{ background: {SPRUCE}; }} .dark .t1, .dark .t2 {{ color: #fff; }} .dark .rule {{ background: {GOLD_LIGHT}; }}
"""

MARK = svg(mark())
MARK_LIGHT = svg(mark(arch="#fff", key=GOLD_LIGHT, crossc=SPRUCE, gap=SPRUCE))


def keystone_icon(size_vb=100, radius=20):
    """Small sizes: the keystone and cross alone on a spruce tile (the arch gets lost below 48px)."""
    c = 50
    cross = (f"M{c-4.5} 22 H{c+4.5} V36 H{c+15} V45 H{c+4.5} V76 H{c-4.5} V45 H{c-15} V36 H{c-4.5} Z")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size_vb} {size_vb}">'
            f'<rect width="100" height="100" rx="{radius}" fill="{SPRUCE}"/>'
            f'<path d="M20 12 H80 L68 88 H32 Z" fill="{GOLD_LIGHT}"/>'
            f'<path d="{cross}" fill="{SPRUCE}"/></svg>')


def lockup(lang, dark=False):
    l1, l2 = NAMES[lang]
    return (f'<div class="lk{" dark" if dark else ""}"><div class="mk">{MARK_LIGHT if dark else MARK}</div>'
            f'<div><div class="t1">EMM</div><div class="rule"></div><div class="t2">{l1}<br>{l2}</div></div></div>')


async def main():
    from playwright.async_api import async_playwright
    from PIL import Image
    (IMG / "emm-mark.svg").write_text(MARK + "\n", encoding="utf-8")
    (IMG / "emm-mark-light.svg").write_text(MARK_LIGHT + "\n", encoding="utf-8")
    (IMG / "emm-icon.svg").write_text(keystone_icon() + "\n", encoding="utf-8")
    logos = ROOT / "brand"
    logos.mkdir(exist_ok=True)
    (logos / "emm-mark.svg").write_text(MARK + "\n", encoding="utf-8")
    (logos / "emm-mark-white.svg").write_text(MARK_LIGHT + "\n", encoding="utf-8")
    async with async_playwright() as p:
        b = await p.chromium.launch()

        async def shot(html, out, scale=2, transparent=False, sel=".lk", viewport=None):
            pg = await b.new_page(device_scale_factor=scale, viewport=viewport or {"width": 1400, "height": 800})
            await pg.set_content(f"<style>{CSS}</style>{html}")
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(200)
            if sel:
                await (await pg.query_selector(sel)).screenshot(path=str(out), omit_background=transparent)
            else:
                await pg.screenshot(path=str(out))
            await pg.close()

        # downloadable logo files
        for lang in ("en", "es"):
            await shot(lockup(lang), logos / f"emm-logo-{lang}.png", transparent=True)
            await shot(lockup(lang, True), logos / f"emm-logo-{lang}-dark.png")
        # icons
        icon_png = {}
        for size in (32, 180, 192, 512):
            buf = logos / f"_icon{size}.png"
            await shot(f'<div class="ic" style="width:{size}px;height:{size}px;line-height:0">{keystone_icon(radius=0 if size == 180 else 20)}</div>',
                       buf, scale=1, transparent=True, sel=".ic")
            icon_png[size] = Image.open(buf).convert("RGBA")
            buf.unlink()
        icon_png[32].save(IMG / "favicon-32.png")
        icon_png[192].save(IMG / "icon-192.png")
        icon_png[180].convert("RGB").save(IMG / "apple-touch-icon.png")
        icon_png[512].save(logos / "emm-icon-512.png")
        icon_png[512].save(ROOT / "static" / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
        # social-sharing image
        og = f"""<div class="og" style="width:1200px;height:630px;box-sizing:border-box;display:flex;align-items:center;
            gap:60px;padding:0 90px;background:#fff;border-bottom:16px solid {SPRUCE}">
            <div style="width:300px;flex:none;line-height:0">{MARK}</div>
            <div><div style="font:600 46px/1.12 L;color:{SPRUCE};margin:0 0 22px">Donde la administración está al servicio de la misión</div>
            <div class="rule"></div>
            <div style="font:600 25px/1.35 F;color:#4A5A57">Excellence Ministry Management<br>Excelencia en Administración Ministerial</div></div></div>"""
        await shot(og, IMG / "og.png", scale=1, sel=".og", viewport={"width": 1200, "height": 630})
        await b.close()


if __name__ == "__main__":
    asyncio.run(main())
