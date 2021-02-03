#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import smtplib


AMAZON_URL = "https://www.amazon.fr/Blue-Yeti-Nano-Premium-Microphone/dp/B07DTTGZ7M/ref=sr_1_3?__mk_fr_" \
      "FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=22LW70KOZKVR1&dchild=1&keywords=yeti+x&qid=1612341233&" \
      "quartzVehicle=106-1303&replacementKeywords=x&sprefix=yeti%2Caps%2C163&sr=8-3"

CAMEL_URL = "https://fr.camelcamelcamel.com/product/"

HEADERS = (
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
     'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'}
)

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = ""             # YOUR EMAIL HERE
MY_PASSWORD = ""# YOUR PASSWORD HERE
MAIL_TO = ""


def send_emails(title, price, best):
    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MAIL_TO,
                msg=f"Subject:Amazon Price Alert!\n\n"
                    f"{title}\n"
                    f"Is now: {price}€, Best price was: {best}€\n"
                    f"{AMAZON_URL}".encode('utf-8')
            )


# Scraping Amazon product page
response = requests.get(url=AMAZON_URL, headers=HEADERS)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
web_price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
web_product_title = soup.find(name="span", class_="a-size-large product-title-word-break")
web_asin = soup.find(id="ASIN")
actual_price = float(web_price.getText().split()[0].replace(',', '.'))
product_title = web_product_title.getText().strip()
asin = web_asin.get('value')

# Scraping Camel product page
response = requests.get(url=f"{CAMEL_URL}{asin}", headers=HEADERS)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
camel_price = soup.find(name="tr", class_="lowest_price").find(name="td").find_next_sibling(name="td").getText()
best_price = float(camel_price[:-1].replace(',', '.'))

if actual_price <= best_price:
    send_emails(product_title, actual_price, best_price)
