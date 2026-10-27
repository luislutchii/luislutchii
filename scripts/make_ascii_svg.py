from pathlib import Path
from PIL import Image
from xml.sax.saxutils import escape
source = Path("source-prepped.png")
if not source.exists():
    raise SystemExit("Run scripts/prep_photo.py with your own photo first.")
im = Image.open(source).convert("L").resize((82, 48))
ramp, pixels, parts = " .:-=+*#%@", list(im.getdata()), []
for y in range(48):
    line = "".join(ramp[min(len(ramp)-1, int((255-pixels[y*82+x])/256*len(ramp)))] for x in range(82)).rstrip()
    safe = escape(line).replace(" ", "&#160;")
    parts.append('<text x="10" y="%.1f" fill="#F4F7FB" opacity="0">%s<animate attributeName="opacity" from="0" to="1" begin="%.3fs" dur=".12s" fill="freeze"/></text>' % (22+y*9.2, safe, y*.055))
svg = '<svg xmlns="http://www.w3.org/2000/svg" width="650" height="480" viewBox="0 0 650 480"><rect width="100%" height="100%" rx="12" fill="#080B12"/><text x="12" y="14" font-family="monospace" font-size="9" fill="#1685FF">LUTCHI // ASCII PORTRAIT</text><g font-family="monospace" font-size="7.4" xml:space="preserve">' + "".join(parts) + '</g><text x="12" y="468" font-family="monospace" font-size="9" fill="#1685FF">LES / ENGINEERED IN ANGOLA</text></svg>'
Path("lutchi-ascii.svg").write_text(svg, encoding="utf-8")
print("Wrote lutchi-ascii.svg")
