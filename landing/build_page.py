#!/usr/bin/env python3
"""Zet logo en productbeeld inline in de template, zodat de pagina één bestand is."""
import re, pathlib
B = pathlib.Path("../brand/veskana")

def inline(path, strip_size=True):
    s = pathlib.Path(path).read_text()
    s = s[s.index("<svg"):]
    if strip_size:
        s = re.sub(r'\swidth="[\d.]+"', '', s, count=1)
        s = re.sub(r'\sheight="[\d.]+"', '', s, count=1)
    return s.strip()

html = pathlib.Path("veskana-template.html").read_text()
html = html.replace("{{LOGO}}",     inline(B/"veskana-logo-horizontal-colour.svg"))
html = html.replace("{{LOGO_INV}}", inline(B/"veskana-logo-horizontal-inverse.svg"))
html = html.replace("{{PRODUCT}}",  inline("product-fountain.svg", strip_size=False))
pathlib.Path("veskana-fontein.html").write_text(html)
print("veskana-fontein.html", len(html), "bytes")
