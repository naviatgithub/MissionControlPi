from flask import Flask, render_template

from modules.apod import apodDetails
from modules.weather import weatherDetails
from modules.iss import issDetails
from modules.moon import moonDetails
from modules.launches import missionDetails


app = Flask(__name__)

@app.route("/")
def main():
    return render_template(
        "index.html",
        apod=apodDetails,
        weather=weatherDetails,
        iss=issDetails,
        moon=moonDetails,
        mission=missionDetails
    )

if __name__ == "__main__":
    app.run(debug=True)