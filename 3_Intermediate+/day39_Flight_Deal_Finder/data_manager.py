import requests


SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/915b3413695fd88038ef76c940882466/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        r = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = r.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            r = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
