"""
Space Weather Module

Fetches recent space weather data
makes use of NASA's DONKI API
weather data includes solar flares, coronal mass ejections, and geomagnetic storms
"""

import requests
from datetime import datetime, timedelta

apiKey = "DEMO_KEY"

startDate = (datetime.utcnow() - timedelta(days=30)).strftime("%Y-%m-%d")
baseURL = "https://api.nasa.gov/DONKI"

flareResponse = requests.get(
    f"{baseURL}/FLR?startDate={startDate}&api_key={apiKey}"
).json()

cmeResponse = requests.get(
    f"{baseURL}/CME?startDate={startDate}&api_key={apiKey}"
).json()

stormResponse = requests.get(
    f"{baseURL}/GST?startDate={startDate}&api_key={apiKey}"
).json()

if isinstance(flareResponse, list) and flareResponse:

    flare = flareResponse[-1]

    flareDetails = {
        "Class": flare.get("classType", "N/A"),
        "Peak Time": flare.get("peakTime", "N/A"),
        "Source": flare.get("sourceLocation", "N/A"),
        "Active Region": flare.get("activeRegionNum", "N/A"),
        "Instruments": ", ".join(
            instrument["displayName"]
            for instrument in flare.get("instruments", [])
        ) or "N/A"
    }

else:
    flareDetails = {
        "Class": "N/A",
        "Peak Time": "N/A",
        "Source": "N/A",
        "Active Region": "N/A",
        "Instruments": "N/A"
    }



if isinstance(cmeResponse, list) and cmeResponse:

    cme = cmeResponse[-1]

    cmeDetails = {
        "Start Time": cme.get("startTime", "N/A"),
        "Source": cme.get("sourceLocation", "N/A"),
        "Active Region": cme.get("activeRegionNum", "N/A")
    }

else:
    cmeDetails = {
        "Start Time": "N/A",
        "Source": "N/A",
        "Active Region": "N/A"
    }



if isinstance(stormResponse, list) and stormResponse:

    storm = stormResponse[-1]

    stormDetails = {
        "Start Time": storm.get("startTime", "N/A"),
        "Kp Index": (
            storm["allKpIndex"][-1].get("kpIndex", "N/A")
            if storm.get("allKpIndex")
            else "N/A"
        )
    }

else:
    stormDetails = {
        "Start Time": "N/A",
        "Kp Index": "N/A"
    }



weatherDetails = {
    "Flare": flareDetails,
    "CME": cmeDetails,
    "Storm": stormDetails
}