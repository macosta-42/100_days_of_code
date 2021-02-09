from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
import time

CHROME_DRIVER_PATH = "/Users/matt/Documents/Development/chromedriver"
SIMILAR_ACCOUNT = "python.hub"# TARGET ACCOUNT HERE
USERNAME = ""# YOUR USERNAME HERE
PASSWORD = ""# YOUR PASSWORD HERE

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        consent = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        consent.click()
        username = self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
        username.send_keys(USERNAME)
        password = self.driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
        password.send_keys(PASSWORD)
        login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(5)
        notifications = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notifications.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        popup = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
        time.sleep(2)
        self.driver.quit()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
