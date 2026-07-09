"""Unlike the other modules, this file will not use additional API requests
I decided to do this because it is quite easy to simply use formulas to calculate the moon phases
that way the user does not have to worry as much about API limits and other memory related issues"""

from datetime import datetime, timezone
import math

oldNewMoon = datetime(2000, 1, 6, 18, 14, tzinfo=timezone.utc)
today = datetime.now(timezone.utc)

daysSince = (today - oldNewMoon).total_seconds() / 86400

moonAge = daysSince % 29.53058

if moonAge < 1.84566:
    phase = "New Moon"

elif moonAge < 5.53699:
    phase = "Waxing Crescent"

elif moonAge < 9.22831:
    phase = "First Quarter"

elif moonAge < 12.91963:
    phase = "Waxing Gibbous"

elif moonAge < 16.61096:
    phase = "Full Moon"

elif moonAge < 20.30228:
    phase = "Waning Gibbous"

elif moonAge < 23.99361:
    phase = "Third Quarter"

elif moonAge < 27.68493:
    phase = "Waning Crescent"

else:
    phase = "New Moon"


illumination = (1 - math.cos(2 * math.pi - moonAge / 29.53058)) / 2
print(illumination)

moonInfo = {
    "Phase" : phase,
    "Age" : round(moonAge, 2),
    "Illumination" : f"{round(illumination * 100, 1)}%"
}

