import requests
import os
from twilio.rest import Client


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
# Change OWN API key HERE
API_KEY = ""
LAT = 48.926559
LON = 2.859430
EXCLUDE = ("current", "minutely", "daily", "alerts")
# Change Twilio information HERE
account_sid = ""
auth_token = ""
# Or use environment variables HERE
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']


parameters = {
    "lat": LAT,
    "lon": LON,
    "exclude": EXCLUDE,
    "appid": API_KEY,
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()['hourly']
condition_codes = [data[hour]['weather'][0]['id'] for hour in range(0, 12)]

take_umbrella = False
for code in condition_codes:
    if int(code) < 700:
        take_umbrella = True

print(take_umbrella)

if take_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        # Change Twilio phone numbers HERE
        from_='',
        to=''
    )
    print(message.status)
