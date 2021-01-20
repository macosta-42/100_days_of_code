from twilio.rest import Client
import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

TWILIO_SID = ""
AUTH_TOKEN = ""

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday = data_list[0]
yesterday_stock = float(yesterday["4. close"])

day_before = data_list[1]
day_before_stock = float(day_before["4. close"])

diff = round((yesterday_stock - day_before_stock), 2)
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percent = round((diff / day_before_stock) * 100)

if abs(percent) > 5:
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    data = response.json()['articles'][:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in data]

    client = Client(TWILIO_SID, AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            # Change Twilio phone numbers HERE
            from_='+13029564644',
            to=''
        )
        print(message.status)
