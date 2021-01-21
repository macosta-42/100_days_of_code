import requests
from datetime import datetime


USERNAME = 'macosta'
TOKEN = '4iVuS9NuOKEy#vwv*ERsSZxH'
GRAPH = 'graph1'

PIXELA_ENDPOINT = "https://pixe.la/v1/users"


user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# Register a new user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    'id': GRAPH,
    'name': "Cycling Graph",
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now().strftime("%Y%m%d")

pixel_params = {
    'date': today,
    'quantity': input("How many kilometers did you cycle today ? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
