import requests

AMOUNT = 10
TYPE = "boolean"

PARAMETERS = {
    "amount": AMOUNT,
    "type": TYPE,
}

response = requests.get("https://opentdb.com/api.php", params=PARAMETERS)
response.raise_for_status()
question_data = response.json()['results']
