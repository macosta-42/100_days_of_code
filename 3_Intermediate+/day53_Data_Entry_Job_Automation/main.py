import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

CHROME_DRIVER_PATH = "/Users/matt/Documents/Development/chromedriver"

GOOGLE_DOC = "" #YOUR GOOGLEDOC URL HERE

ZILLOW = "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22" \
         "usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.5517753500" \
         "9766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694" \
         "487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isM" \
         "apVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22" \
         "value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C" \
         "%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22va" \
         "lue%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22" \
         "mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A" \
         "1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


class EstateDataScraping:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.all_links = []
        self.all_addresses = []
        self.all_prices = []

    def zillow_scraping(self):
        response = requests.get(ZILLOW, headers=HEADER)
        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        all_link_elements = soup.select(".list-card-top a")

        for link in all_link_elements:
            href = link["href"]
            print(href)
            if "http" not in href:
                self.all_links.append(f"https://www.zillow.com{href}")
            else:
                self.all_links.append(href)

        all_address_elements = soup.select(".list-card-info address")
        self.all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

        all_price_elements = soup.select(".list-card-heading")
        price = ""
        for element in all_price_elements:
            try:
                price = element.select(".list-card-price")[0].contents[0]
            except IndexError:
                print('Multiple listings for the card')
                price = element.select(".list-card-details li")[0].contents[0]
            finally:
                self.all_prices.append(price)

    def filling_google_doc(self):

        for n in range(len(self.all_links)):
            self.driver.get(GOOGLE_DOC)

            time.sleep(2)
            address = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

            address.send_keys(self.all_addresses[n])
            price.send_keys(self.all_prices[n])
            link.send_keys(self.all_links[n])
            submit_button.click()


bot = EstateDataScraping()
bot.zillow_scraping()
bot.filling_google_doc()
