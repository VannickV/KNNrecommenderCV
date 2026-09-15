#!/usr/bin/env python3
"""Bouwt het merkblad en zet elke SVG inline, zodat het bestand op zichzelf werkt."""
import base64, os
def png(path):
    return "data:image/png;base64," + base64.b64encode(open(path,"rb").read()).decode()

def inl(path, cls="", style=""):
    s = open(path).read()
    s = s[s.index("<svg"):]
    s = s.replace('<svg ', f'<svg class="{cls}" style="{style}" preserveAspectRatio="xMidYMid meet" ', 1)
    import re
    s = re.sub(r'\swidth="[\d.]+"\s', ' ', s, count=1)
    s = re.sub(r'\sheight="[\d.]+"\s', ' ', s, count=1)
    return s

HTML = f"""<!doctype html>
<html lang="nl-BE"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Veskana · merkblad</title>
<style>
*,*::before,*::after{{box-sizing:border-box}}
:root{{--ink:#0D2A33;--aqua:#0F8F9E;--paper:#F6F4EF;--steel:#8FA3A8;--line:#dfe6e8;--mist:#EEF5F6}}
body{{margin:0;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;color:var(--ink);background:#fff}}
.wrap{{max-width:1000px;margin:0 auto;padding-inline:24px}}
section{{padding-block:clamp(40px,6vw,72px)}}
h1,h2,h3{{line-height:1.1;letter-spacing:-.02em;margin:0 0 .5em}}
h2{{font-size:clamp(1.4rem,3.4vw,2rem)}}
h3{{font-size:1.05rem;margin-bottom:.3em}}
p{{margin:0 0 1em;max-width:70ch}}
.eyebrow{{font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;font-weight:800;color:var(--aqua);margin-bottom:12px}}
.hero{{background:var(--ink);color:#fff;text-align:center;padding-block:clamp(56px,9vw,104px)}}
.hero svg{{width:min(560px,80%);height:auto}}
.hero p{{color:#a9c6cb;margin:26px auto 0;font-size:.95rem;max-width:52ch}}
.grid{{display:grid;gap:20px}}
@media(min-width:720px){{.grid.c2{{grid-template-columns:1fr 1fr}}.grid.c3{{grid-template-columns:repeat(3,1fr)}}}}
.card{{border:1px solid var(--line);border-radius:14px;padding:26px;background:#fff}}
.card p{{font-size:.94rem;color:#41565f;margin:0}}
.plate{{border:1px solid var(--line);border-radius:14px;padding:34px;display:grid;place-items:center;min-height:170px;background:var(--paper)}}
.plate.dark{{background:var(--ink);border-color:var(--ink)}}
.plate.white{{background:#fff}}
.plate svg{{width:100%;height:auto;max-height:120px}}
.cap{{font-size:.78rem;color:#6b8288;margin-top:10px;text-align:center}}
.swatches{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(150px,1fr))}}
.sw{{border:1px solid var(--line);border-radius:12px;overflow:hidden}}
.sw .chip{{height:88px}}
.sw .meta{{padding:12px 14px;font-size:.82rem}}
.sw b{{display:block;font-size:.9rem}}
.sw code{{color:#6b8288}}
.sizes{{display:flex;flex-wrap:wrap;align-items:flex-end;gap:28px}}
.sizes figure{{margin:0;text-align:center}}
.sizes img{{display:block;image-rendering:auto;margin:0 auto 8px}}
.sizes figcaption{{font-size:.74rem;color:#6b8288}}
ul.rules{{margin:0;padding-left:20px}}
ul.rules li{{margin-bottom:.5em;font-size:.95rem;color:#41565f}}
.bad b{{color:#a33}}
.good b{{color:#1f7a4d}}
table{{width:100%;border-collapse:collapse;font-size:.9rem}}
td,th{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}}
th{{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:#6b8288}}
code{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.86em}}
.mist{{background:var(--mist)}}
footer{{background:var(--ink);color:#9fc0c6;font-size:.85rem;padding-block:30px}}
</style></head><body>

<div class="hero">
  {inl("veskana-logo-horizontal-inverse.svg")}
  <p>Merkteken, wordmark en toepassingsregels. Eén bestand, alles vector.</p>
</div>

<section><div class="wrap">
  <p class="eyebrow">Waarom dit logo en geen pootafdruk</p>
  <h2>Het merkteken is het mechanisme</h2>
  <p>De druppel is doormidden gesneden. Boven de snede het water dat binnenkomt, onder de snede de gesloten kamer.
  Dat is letterlijk <b>eerst de filter, dan de pomp</b>: de enige zin die je klant moet kunnen navertellen. Een logo dat
  het mechanisme draagt werkt in een advertentie als een tweede hook, niet als decoratie.</p>
  <div class="grid c3" style="margin-top:28px">
    <div class="card"><h3>Geen pootje, geen hondenkopje</h3><p>Deze koper is trots op onderscheidingsvermogen, niet op uitgeven: "I don't have a physiotherapist, neither do my dogs". Schattig leest als speelgoed, en speelgoed gaat stuk.</p></div>
    <div class="card"><h3>Staal, geen pet-tech</h3><p>Strakke geometrie in de visuele grammatica van Framework en iFixit. Premium omdat het niet faalt, niet premium omdat het duur is.</p></div>
    <div class="card"><h3>Leesbaar op 16 pixels</h3><p>Twee vormen, één spleet. Werkt als favicon, als Meta-profielfoto en als gravure op roestvrij staal, zonder aanpassing.</p></div>
  </div>
</div></section>

<section class="mist"><div class="wrap">
  <p class="eyebrow">Varianten</p>
  <h2>Vier bestanden dekken alles</h2>
  <div class="grid c2" style="margin-top:24px">
    <div><div class="plate">{inl("veskana-logo-horizontal-colour.svg")}</div><div class="cap">Horizontaal · standaard, voor header en briefpapier</div></div>
    <div><div class="plate dark">{inl("veskana-logo-horizontal-inverse.svg")}</div><div class="cap">Omgekeerd · op ink, foto of donkere sectie</div></div>
    <div><div class="plate">{inl("veskana-logo-stacked-colour.svg", style="max-height:190px")}</div><div class="cap">Gestapeld · vierkante plekken, verpakking, sticker</div></div>
    <div><div class="plate white">{inl("veskana-wordmark.svg", style="max-height:52px")}</div><div class="cap">Wordmark los · waar het merkteken al elders staat</div></div>
  </div>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">Klein formaat</p>
  <h2>App-icoon en favicon</h2>
  <div class="sizes" style="margin-top:22px">
    <figure><img src="{png("veskana-app-icon-180.png")}" width="180" height="180" alt=""><figcaption>180 px · touch icon</figcaption></figure>
    <figure><img src="{png("veskana-app-icon-180.png")}" width="64" height="64" alt=""><figcaption>64 px</figcaption></figure>
    <figure><img src="{png("veskana-favicon-32.png")}" width="32" height="32" alt=""><figcaption>32 px · favicon</figcaption></figure>
    <figure><img src="{png("veskana-favicon-16.png")}" width="16" height="16" alt=""><figcaption>16 px</figcaption></figure>
  </div>
  <p style="margin-top:20px;font-size:.88rem;color:#6b8288">Onder 24 px vervalt de aqua driehoek naar wit: twee kleuren
  op die grootte wordt modder. Het bestand <code>veskana-favicon.svg</code> doet dat nog niet automatisch; zet de
  driehoek op <code>#FFFFFF</code> als je een 16 px versie apart exporteert.</p>
</div></section>

<section class="mist"><div class="wrap">
  <p class="eyebrow">Kleur</p>
  <h2>Drie kleuren, en dat is het</h2>
  <div class="swatches" style="margin-top:22px">
    <div class="sw"><div class="chip" style="background:#0D2A33"></div><div class="meta"><b>Steel Ink</b><code>#0D2A33</code><br><code>rgb(13,42,51)</code></div></div>
    <div class="sw"><div class="chip" style="background:#0F8F9E"></div><div class="meta"><b>Veskana Aqua</b><code>#0F8F9E</code><br><code>rgb(15,143,158)</code></div></div>
    <div class="sw"><div class="chip" style="background:#F6F4EF"></div><div class="meta"><b>Paper</b><code>#F6F4EF</code><br><code>rgb(246,244,239)</code></div></div>
    <div class="sw"><div class="chip" style="background:#8FA3A8"></div><div class="meta"><b>Steel (support)</b><code>#8FA3A8</code><br><code>alleen voor lijnen</code></div></div>
  </div>
  <p style="margin-top:18px">Aqua is een accent, geen vlakvulling: knoppen, de driehoek, één lijn. Zodra aqua het vlak
  vult, kantelt het merk van staal naar plastic. Dat is precies de associatie die deze markt afstraft.</p>
</div></section>

<section><div class="wrap">
  <p class="eyebrow">Regels</p>
  <h2>Vijf dingen wel, vijf dingen niet</h2>
  <div class="grid c2" style="margin-top:24px">
    <div class="card good"><b>Wel</b>
      <ul class="rules" style="margin-top:10px">
        <li>Vrije ruimte rondom = de hoogte van het merkteken gedeeld door drie.</li>
        <li>Minimum breedte horizontaal logo: 120 px digitaal, 28 mm in druk.</li>
        <li>Op foto's altijd de omgekeerde versie, nooit het logo met een schaduw.</li>
        <li>SVG gebruiken waar het kan; de PNG's zijn er voor Meta, marktplaatsen en print.</li>
        <li>Op de fontein zelf: alleen het merkteken, gegraveerd of gelaserd, geen sticker.</li>
      </ul></div>
    <div class="card bad"><b>Niet</b>
      <ul class="rules" style="margin-top:10px">
        <li>De spleet dichtmaken of de driehoek laten raken aan de kom: dan is het mechanisme weg.</li>
        <li>Verhoudingen, tracking of kleuren aanpassen, of het logo op een hoek zetten.</li>
        <li>Een verloop, glans of waterreflectie toevoegen.</li>
        <li>Een pootafdruk, hondensilhouet of waterstraaltje ernaast plaatsen.</li>
        <li>Het logo op aqua zetten: ink op paper of wit op ink, verder niets.</li>
      </ul></div>
  </div>
</div></section>

<section class="mist"><div class="wrap">
  <p class="eyebrow">Bestanden</p>
  <h2>Wat er in de map zit</h2>
  <table style="margin-top:18px">
    <tr><th>Bestand</th><th>Waarvoor</th></tr>
    <tr><td><code>veskana-logo-horizontal.svg</code></td><td>Standaard, neemt de kleur van je CSS over (<code>currentColor</code>)</td></tr>
    <tr><td><code>veskana-logo-horizontal-colour.svg</code> / <code>-inverse.svg</code></td><td>Vaste kleuren, licht en donker</td></tr>
    <tr><td><code>veskana-logo-stacked.svg</code> / <code>-colour.svg</code></td><td>Gestapeld</td></tr>
    <tr><td><code>veskana-wordmark.svg</code> · <code>veskana-mark.svg</code></td><td>Los woordbeeld en los merkteken</td></tr>
    <tr><td><code>veskana-app-icon.svg</code> + PNG 1024/512/180</td><td>App-icoon, socialprofiel, marktplaatsen</td></tr>
    <tr><td><code>veskana-favicon.svg</code> + PNG 32/16</td><td>Browsertab</td></tr>
    <tr><td><code>build_logo.py</code></td><td>Genereert alles opnieuw; letters zijn geometrie, geen font, dus er is geen licentie aan verbonden</td></tr>
  </table>
</div></section>

<footer><div class="wrap">Veskana merkblad · alle vormen zijn vector en fontvrij opgebouwd, dus vrij te gebruiken en te wijzigen.</div></footer>
</body></html>
"""
open("veskana-brand.html","w").write(HTML)
print("veskana-brand.html", len(HTML), "bytes")
