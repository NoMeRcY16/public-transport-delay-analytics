import time
import csv
import requests

URL = "https://nominatim.openstreetmap.org/search"
HEADERS = {"User-Agent": "transport-delay-college-project/0.1 (student project)"}

with open("data/routes/route_01_stops.csv", newline="", encoding="utf-8") as f:
    stops = list(csv.DictReader(f))

out = []
for s in stops:
    params = {"q": s["search_query"], "format": "json", "limit": 1, "countrycodes": "in"}
    r = requests.get(URL, params=params, headers=HEADERS, timeout=20).json()
    if r:
        lat, lon, name = r[0]["lat"], r[0]["lon"], r[0]["display_name"][:70]
    else:
        lat, lon, name = "", "", "NOT FOUND"
    print(s["stop_order"], s["stop_name"], "|", lat, lon, "|", name)
    out.append([s["stop_order"], s["stop_name"], lat, lon, name])
    time.sleep(2)

with open("data/routes/route_01_stops_geocoded.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["stop_order", "stop_name", "latitude", "longitude", "matched_name"])
    w.writerows(out)
print("Saved data/routes/route_01_stops_geocoded.csv")
