"""
International Space Station (ISS) Location Tracker Module
Simply fetches the current ISS coordinates
In the future will display location on world map
"""

import requests


url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url).json()


if "iss_position" in response:

    latitude = response["iss_position"]["latitude"]
    longitude = response["iss_position"]["longitude"]

    issDetails = {
        "lat": latitude,
        "long": longitude
    }

else:

    issDetails = {
        "lat": "N/A",
        "long": "N/A"
    }