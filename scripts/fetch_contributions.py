import json, os
from datetime import datetime, timezone
from pathlib import Path
import requests
from bs4 import BeautifulSoup

username = os.getenv("GITHUB_USERNAME", "luislutchii")
url = f"https://github.com/users/{username}/contributions"
response = requests.get(url, headers={"User-Agent": "luislutchii-profile-readme/1.0"}, timeout=30)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
cells = soup.select("td.ContributionCalendar-day[data-date]")
if not cells:
    raise SystemExit("Contribution calendar markup not found. No fabricated data was written.")
days = []
for cell in cells:
    try:
        days.append({"date": cell["data-date"], "level": max(0, min(4, int(cell.get("data-level", 0)))), "count": int(cell.get("data-count", 0))})
    except (KeyError, ValueError):
        continue
days.sort(key=lambda x: x["date"])
if not days:
    raise SystemExit("No contribution days parsed; refusing to generate fake data.")
out = Path("data/contributions.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps({"username": username, "fetched_at": datetime.now(timezone.utc).isoformat(), "total_contributions": sum(d["count"] for d in days), "days": days}, indent=2), encoding="utf-8")
print(f"Saved {len(days)} contribution days to {out}")
