#!/usr/bin/env python3
"""Bouwt het Veskana-logopakket. Alle lettervormen zijn hier geometrisch
gedefinieerd (geen font-afhankelijkheid), zodat elke SVG overal identiek rendert."""
import math, os

# ---------- kleuren ----------
INK   = "#0D2A33"   # Steel Ink
AQUA  = "#0F8F9E"   # Veskana Aqua
PAPER = "#F6F4EF"   # Paper

# ---------- letters, elk in een vak van 72 x 100, stokdikte 14 ----------
L = {
 "V": {"fills":["M0,0 L14,0 L36,75.9 L58,0 L72,0 L43,100 L29,100 Z"]},
 "E": {"fills":["M0,0 L62,0 L62,14 L14,14 L14,43 L54,43 L54,57 L14,57 L14,86 L62,86 L62,100 L0,100 Z"]},
 "S": {"fills":[], "strokes":["M63,22 C58,11 48,7 36,7 C22,7 8,14 8,27 C8,39 19,44 36,49 C53,54 64,60 64,73 C64,86 50,93 36,93 C24,93 14,89 9,79"]},
 "K": {"fills":["M0,0 L14,0 L14,100 L0,100 Z",
                "M52,0 L72,0 L14,58 L14,38 Z",
                "M14,42 L14,62 L52,100 L72,100 Z"]},
 "A": {"fills":["M0,100 L14,100 L36,24.1 L58,100 L72,100 L43,0 L29,0 Z",
                "M18,62 L54,62 L54,76 L18,76 Z"]},
 "N": {"w":64,
       "fills":["M0,0 L14,0 L14,100 L0,100 Z",
                "M50,0 L64,0 L64,100 L50,100 Z",
                "M0,0 L14,0 L64,74.8 L64,100 L50,100 L0,25.2 Z"]},
}
WORD, TRACK, LW, CAP = "VESKANA", 24, 72, 100
def lw(ch): return L[ch].get("w", LW)
# optische kerning: schuine letters (V, A, K) hebben andere witruimte dan rechte
KERN = {"VE": -8, "ES": 0, "SK": 3, "KA": 10, "AN": 4, "NA": 6}
OFFS, _x = [], 0.0
for _i, _c in enumerate(WORD):
    OFFS.append(_x)
    if _i < len(WORD)-1:
        _x += lw(_c) + TRACK + KERN.get(WORD[_i:_i+2], 0)
WORD_W = OFFS[-1] + lw(WORD[-1])

def wordmark(color="currentColor", x=0, y=0, scale=1.0):
    out = [f'<g transform="translate({x},{y}) scale({scale})" fill="{color}">']
    for i, ch in enumerate(WORD):
        out.append(f'<g transform="translate({OFFS[i]:g},0)">')
        for d in L[ch].get("fills", []):
            out.append(f'<path d="{d}"/>')
        for d in L[ch].get("strokes", []):
            out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="14" stroke-linecap="butt"/>')
        out.append('</g>')
    out.append('</g>')
    return "\n".join(out)

# ---------- merkteken ----------
# Boven de spleet het water dat binnenkomt, onder de spleet de gesloten kamer:
# eerst de filter, dan de pomp. Geometrie staat in mark_geom.py.
from mark_geom import MARK_TRI, MARK_BOWL, MARK_TOP, MARK_BOT, MARK_L, MARK_R
TLx, TRx = MARK_L, MARK_R

def mark(color="currentColor", accent=None, x=0, y=0, scale=1.0):
    a = accent or color
    return (f'<g transform="translate({x},{y}) scale({scale})">'
            f'<path d="{MARK_TRI}" fill="{a}"/>'
            f'<path d="{MARK_BOWL}" fill="{color}"/></g>')

def svg(w, h, body, extra=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" '
            f'width="{w:g}" height="{h:g}" role="img"{extra}>\n{body}\n</svg>\n')

def write(name, content):
    open(name, "w").write(content)
    print(f"  {name}  ({len(content)} bytes)")

# ---------- 1. merkteken los ----------
write("veskana-mark.svg", svg(100, 100,
    '<title>Veskana</title>\n'+mark("currentColor"),
    ' fill="currentColor"'))

# ---------- 2. wordmark los ----------
write("veskana-wordmark.svg", svg(WORD_W, CAP,
    '<title>Veskana</title>\n'+wordmark("currentColor"),
    ' fill="currentColor"'))

# ---------- 3. horizontale lockup ----------
MH    = MARK_BOT-MARK_TOP                     # inkthoogte merkteken
MW    = TRx-TLx                               # inktbreedte merkteken
def lockup(mark_h, gap, color, accent=None):
    sc   = mark_h/MH
    mw   = MW*sc
    toth = max(mark_h, CAP)
    body = ('<title>Veskana</title>\n'
            + mark(color, accent, x=-TLx*sc, y=(toth-mark_h)/2 - MARK_TOP*sc, scale=round(sc,4))
            + "\n" + wordmark(color, x=round(mw+gap,2), y=(toth-CAP)/2))
    return round(mw+gap+WORD_W,1), toth, body

w,h,body = lockup(132, 56, "currentColor")
write("veskana-logo-horizontal.svg", svg(w, h, body, ' fill="currentColor"'))

# ---------- 4. gestapelde lockup ----------
sc2   = 168/MH
mw2   = MW*sc2
gap2  = 44
toth2 = 168+gap2+CAP
body = ('<title>Veskana</title>\n'
        + mark("currentColor", None, x=(WORD_W-mw2)/2-TLx*sc2, y=-MARK_TOP*sc2, scale=round(sc2,4))
        + "\n" + wordmark("currentColor", x=0, y=168+gap2))
write("veskana-logo-stacked.svg", svg(WORD_W, toth2, body, ' fill="currentColor"'))

# ---------- 5. app-tegel ----------
INK_X0, INK_X1 = TLx, TRx                     # werkelijke inktbreedte van het merkteken
def mark_centered(size, target_h, radius, bg=INK):
    s_ = target_h/MH
    cx = (INK_X0+INK_X1)/2
    cy = (MARK_TOP+MARK_BOT)/2
    tx = size/2 - cx*s_
    ty = size/2 - cy*s_
    return (f'<title>Veskana</title>\n<rect width="{size}" height="{size}" rx="{radius}" fill="{bg}"/>\n'
            + mark("#FFFFFF", AQUA, x=round(tx,2), y=round(ty,2), scale=round(s_,4)))

write("veskana-app-icon.svg", svg(512, 512, mark_centered(512, 286, 114)))

# ---------- 6. favicon ----------
write("veskana-favicon.svg", svg(64, 64, mark_centered(64, 40, 14)))

# ---------- 7. horizontaal, twee kleuren, op papier ----------
w,h,body = lockup(132, 56, INK, AQUA)
write("veskana-logo-horizontal-colour.svg", svg(w, h, body))

# ---------- 8. horizontaal, omgekeerd (op donker) ----------
w,h,body = lockup(132, 56, "#FFFFFF", AQUA)
write("veskana-logo-horizontal-inverse.svg", svg(w, h, body))

# ---------- 9. gestapeld, twee kleuren ----------
sc2   = 168/MH; mw2 = MW*sc2; gap2 = 44; toth2 = 168+gap2+CAP
body = ('<title>Veskana</title>\n'
        + mark(INK, AQUA, x=(WORD_W-mw2)/2-TLx*sc2, y=-MARK_TOP*sc2, scale=round(sc2,4))
        + "\n" + wordmark(INK, x=0, y=168+gap2))
write("veskana-logo-stacked-colour.svg", svg(WORD_W, toth2, body))

print("\nmerkteken inkt: %.1f x %.1f  |  wordmark: %.0f x %d" % (MARK_R-MARK_L, MARK_BOT-MARK_TOP, WORD_W, CAP))
