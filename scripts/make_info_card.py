from pathlib import Path
from xml.sax.saxutils import escape
rows = [("USER","Luis Lutchi"),("ROLE","Developer / Digital Creator"),("ORG","LES - Lutchi Enterprise Systems"),("FOCUS","Software, AI & Automation"),("BUILDING","CodeLES / VibePay / LutchiCash"),("BASED","Angola"),("GITHUB","github.com/luislutchii")]
items = []
for i, (key, value) in enumerate(rows):
    y = 72 + i*45
    items.append('<g opacity="0"><text x="24" y="%s" fill="#1685FF" font-family="monospace" font-size="12">%s</text><text x="126" y="%s" fill="#F4F7FB" font-family="monospace" font-size="12">%s</text><animate attributeName="opacity" from="0" to="1" begin="%.2fs" dur=".3s" fill="freeze"/></g>' % (y, escape(key), y, escape(value), .25+i*.14))
svg = '<svg xmlns="http://www.w3.org/2000/svg" width="650" height="480" viewBox="0 0 650 480"><rect width="650" height="480" rx="12" fill="#080B12" stroke="#1C2B45"/><rect width="650" height="34" rx="12" fill="#101827"/><circle cx="18" cy="17" r="5" fill="#FF5F57"/><circle cx="35" cy="17" r="5" fill="#FEBC2E"/><circle cx="52" cy="17" r="5" fill="#28C840"/><text x="325" y="21" text-anchor="middle" fill="#8B95A7" font-family="monospace" font-size="11">luis@github: ~</text><text x="24" y="56" fill="#F4F7FB" font-family="monospace" font-size="13" font-weight="700">LUIS LUTCHI <tspan fill="#1685FF">/ PROFILE</tspan></text>' + "".join(items) + '<path d="M24 407 H626" stroke="#1C2B45"/><text x="24" y="435" fill="#1685FF" font-family="monospace" font-size="11">BUILD. AUTOMATE. ITERATE. SCALE.</text><text x="24" y="457" fill="#8B95A7" font-family="monospace" font-size="10">LES - LUTCHI ENTERPRISE SYSTEMS</text></svg>'
Path("info-card.svg").write_text(svg, encoding="utf-8")
print("Wrote info-card.svg")
