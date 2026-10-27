import json
from pathlib import Path
from xml.sax.saxutils import escape

data_path = Path("data/contributions.json")
if not data_path.exists():
    raise SystemExit("Run scripts/fetch_contributions.py first.")
data = json.loads(data_path.read_text(encoding="utf-8"))
days = data.get("days", [])[-371:]
if not days:
    raise SystemExit("No real contribution data available.")
days = [{"date": "", "level": 0, "count": 0}] * (371 - len(days)) + days
palette = ["#172033", "#123A72", "#0758C7", "#1685FF", "#6AB7FF"]
rects = []
for i, day in enumerate(days):
    week, dow = divmod(i, 7)
    x, y = 20 + week * 14, 43 + dow * 14
    date, count = escape(day.get("date", "")), int(day.get("count", 0))
    level = max(0, min(4, int(day.get("level", 0))))
    delay = min(week * 0.035 + dow * 0.012, 1.8)
    rects.append(
        f'<rect x="{x}" y="{y}" width="10" height="10" rx="2" fill="{palette[level]}" opacity="0">'
        f'<title>{date}: {count} contribution(s)</title>'
        f'<animate attributeName="opacity" from="0" to="1" begin="{delay:.3f}s" dur=".35s" fill="freeze"/></rect>'
    )
total = int(data.get("total_contributions", 0))
total_fmt = format(total, ",")
head = (
    f'<svg xmlns="http://www.w3.org/2000/svg" width="860" height="154" viewBox="0 0 860 154">'
    f'<rect width="100%" height="100%" rx="12" fill="#080B12"/>'
    f'<text x="20" y="25" fill="#F4F7FB" font-family="monospace" font-size="13">luislutchii / CONTRIBUTION LOG</text>'
    f'<text x="840" y="25" text-anchor="end" fill="#8B95A7" font-family="monospace" font-size="11">{total_fmt} contributions</text>'
)
legend_parts = ['<text x="20" y="143" fill="#8B95A7" font-family="monospace" font-size="10">LESS</text>']
for i, c in enumerate(palette):
    legend_parts.append(f'<rect x="{62 + i * 18}" y="133" width="11" height="11" rx="2" fill="{c}"/>')
legend_parts.append('<text x="162" y="143" fill="#8B95A7" font-family="monospace" font-size="10">MORE</text>')
legend_parts.append('<text x="840" y="143" text-anchor="end" fill="#8B95A7" font-family="monospace" font-size="10">PUBLIC GITHUB CONTRIBUTIONS</text>')
legend_parts.append('</svg>')
legend = "".join(legend_parts)
Path("contrib-heatmap.svg").write_text(head + "".join(rects) + legend, encoding="utf-8")
print("Wrote contrib-heatmap.svg")