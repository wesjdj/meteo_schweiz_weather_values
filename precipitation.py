import json
import urllib.request
#links https://gist.github.com/philshem/0812d610f11d26a042bbd3e617fa8d22?short_path=bb4816a
#file = 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-niederschlag-10min/ch.meteoschweiz.messwerte-niederschlag-10min_en.json'

location_code = ""

with urllib.request.urlopen('https://data.geo.admin.ch/ch.meteoschweiz.messwerte-niederschlag-10min/ch.meteoschweiz.messwerte-niederschlag-10min_en.json') as url:
        json_data = json.loads(url.read().decode())

locations = json_data["features"]

for location in locations:
        if location["id"] == location_code:
                data = location["properties"]["description"]
                Precipitation = data.split("Precipitation</strong></td><td>")[1]
                Precipitation_data = Precipitation[0] + Precipitation[1] + Precipitation[2]
                print(Precipitation_data)