import json
import os
import sys
import urllib.request
#links https://gist.github.com/philshem/0812d610f11d26a042bbd3e617fa8d22?short_path=bb4816a
#file = 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-niederschlag-10min/ch.meteoschweiz.messwerte-niederschlag-10min_en.json'

location_code = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("METEOSWISS_STATION")
if not location_code:
    sys.exit("Usage: precipitation.py <station_code>  (or set METEOSWISS_STATION)")

with urllib.request.urlopen('https://data.geo.admin.ch/ch.meteoschweiz.messwerte-niederschlag-10min/ch.meteoschweiz.messwerte-niederschlag-10min_en.json') as url:
        json_data = json.loads(url.read().decode())

locations = json_data["features"]

for location in locations:
        if location["id"] == location_code:
                data = location["properties"]["description"]
                Precipitation_data = data.split("Precipitation</strong></td><td>")[1].split("</td>")[0]
                print(Precipitation_data)