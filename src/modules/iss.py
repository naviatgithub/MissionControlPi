"""
International Space Station (ISS) Location Tracker Module
Simply fetches the current ISS coordinates
In the future will display location on world map
"""

import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url).json()

latitude = response["iss_position"]["latitude"]
longitude = response["iss_position"]["longitude"]

# print("lat:", latitude)
# print("long:", longitude)

issData = {
    "lat": latitude,
    "long": longitude
}