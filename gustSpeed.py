import json
import urllib.request
#links https://gist.github.com/philshem/0812d610f11d26a042bbd3e617fa8d22?short_path=bb4816a
#file = 'https://data.geo.admin.ch/ch.meteoschweiz.messwerte-niederschlag-10min/ch.meteoschweiz.messwerte-niederschlag-10min_en.json'

location = "REH"

with urllib.request.urlopen('https://data.geo.admin.ch/ch.meteoschweiz.messwerte-wind-boeenspitze-kmh-10min/ch.meteoschweiz.messwerte-wind-boeenspitze-kmh-10min_en.json') as url:
        json_data = json.loads(url.read().decode())

locations = json_data["features"]

for location in locations:
    if location["id"] == location:
        data = location["properties"]["description"]
        wind_speed = data.split("Gust peak</strong></td><td>")[1]
        wind_speed_data = wind_speed[0] + wind_speed[1] + wind_speed[2]
        print(wind_speed_data)