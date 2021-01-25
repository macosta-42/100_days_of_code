import requests
from datetime import datetime

APP_ID = #YOUR NUTITIONIX APP ID HERE
API_KEY = #YOUR NUTITIONIX API KEY HERE
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

TOKEN = #YOUR SHEETY TOKEN HERE
SHEET = #YOUR SHEETY API HERE

GENDER = "male"
WEIGHT = 85
HEIGHT = 175
AGE = 35

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

r = requests.post(url=ENDPOINT, headers=headers, json=params)
result = r.json()


today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

headers = {"Authorization": f"Bearer {TOKEN}"}

for exercise in result["exercises"]:
    sheet_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": str(round(exercise["duration_min"])) + " min",
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEET, headers=headers, json=sheet_params)

    print(sheet_response.text)
