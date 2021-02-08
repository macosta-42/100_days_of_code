from selenium import webdriver
import time

PROMISED_DOWN = 400
PROMISED_UP = 300
CHROME_DRIVER_PATH = "/Users/matt/Documents/Development/chromedriver"
TWITTER_EMAIL = "" #YOUR TWITTER EMAIL HERE
TWITTER_PASSWORD = "" #YOUR TWITTER PASS HERE


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        consent = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        consent.click()
        time.sleep(2)
        test = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'
        )
        test.click()
        in_progress = True
        while in_progress:
            progress = self.driver.find_element_by_css_selector(".overall-progress").text
            if progress.startswith("Your speed test has completed"):
                self.down = float(self.driver.find_element_by_css_selector(".download-speed").text)
                self.up = float(self.driver.find_element_by_css_selector(".upload-speed").text)
                print(f"down: {self.down}")
                print(f"up: {self.up}")
                in_progress = False
            else:
                time.sleep(5)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(5)
        login = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span'
        )
        login.click()
        time.sleep(2)
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
        )
        email.send_keys(TWITTER_EMAIL)
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
        )
        password.send_keys(TWITTER_PASSWORD)
        login = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span'
        )
        login.click()
        time.sleep(2)
        msg = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/'
            'div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div'
        )
        msg.click()
        msg.send_keys(f"Hey Orange, why is my internet speed {self.down}down/{self.up}up "
                      f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
            'div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]'
        )
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    bot.tweet_at_provider()
