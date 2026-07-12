"""
Astronomy Picture of the Day (APOD) module
for fetching and displaying the Astronomy Picture of the Day.
"""

import requests

apiKey = "DEMO_KEY" # The demo key works but has a slower request rate. you can easily get your own api key from https://api.nasa.gov/

url = f"https://api.nasa.gov/planetary/apod?api_key={apiKey}"
response = requests.get(url).json()
# print(response.status_code)  # use if the website isn't working, it shows the success (200) or error code

apodDetails = {
    "Title": response.get("title", "N/A"),
    "Date": response.get("date", "N/A"),
    "Explanation": response.get("explanation", "N/A"),
    "Image URL": response.get("url", ""),
    "Media Type": response.get("media_type", "N/A"),
    "Copyright": response.get("copyright", "Public Domain")
}

if apodDetails["Media Type"] == "image":
    image = requests.get(apodDetails["Image URL"]).content

    with open("apod.jpg", "wb") as f:
        f.write(image)