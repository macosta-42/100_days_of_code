from datetime import datetime
import requests
import smtplib
import time

# Change the receiver email HERE
EMAIL_TO = ""

# Change your email and password HERE
EMAIL_FROM = ""
PASSWORD = ""

# Change your Latitude an Longitude HERE
MY_LAT = 48.926560
MY_LONG = 2.859430

# Checking ISS API and compare with my position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

iss_is_overhead = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5

# Checking sunrise-sunset API and compare with my time
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

is_night = sunset < time_now < sunrise

# Check every 60sec if ISS is over my position and if it's currently the night. If so, send me an email
while True:
    time.sleep(60)
    if iss_is_overhead and is_night:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_FROM, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_FROM,
                to_addrs=EMAIL_TO,
                msg="Subject:Look up\n\nThe ISS is above you in the sky."
            )
