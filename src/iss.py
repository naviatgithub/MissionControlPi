import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url).json()

latitude = response["iss_position"]["latitude"]
longitude = response["iss_position"]["longitude"]

print("lat:", latitude)
print("long:", longitude)