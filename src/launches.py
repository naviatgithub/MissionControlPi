import requests

url = "https://ll.thespacedevs.com/2.3.0/launches/upcoming/?limit=5"

response = requests.get(url).json()

launchData = response["results"][0]

if launchData["mission"]:
    missionDetails = {
        "Mission": launchData["name"],
        "Provider": launchData["launch_service_provider"]["name"],
        "Rocket": launchData["rocket"]["configuration"]["full_name"],
        "Launch Time": launchData["net"],
        "Mission Type": launchData["mission"]["type"],
        "Orbit": launchData["mission"]["orbit"]["name"],
        "Description": launchData["mission"]["description"],
        "Pad": launchData["pad"]["name"],
        "Location": launchData["pad"]["location"]["name"],
        "Image": launchData["image"]
    }
else:
    missionDetails = {
        "Mission": launchData["name"],
        "Provider": launchData["launch_service_provider"]["name"],
        "Rocket": launchData["rocket"]["configuration"]["full_name"],
        "Launch Time": launchData["net"],
        "Pad": launchData["pad"]["name"],
        "Location": launchData["pad"]["location"]["name"],
        "Image": launchData["image"]
    }

print(missionDetails["Image"])