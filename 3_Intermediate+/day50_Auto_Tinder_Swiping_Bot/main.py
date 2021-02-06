from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium import webdriver
import random
import time

EMAIL = ""
PASSWORD = ""

chrome_driver_path = "/Users/matt/Documents/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/")

time.sleep(2)
tinder_login = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
tinder_login.click()
time.sleep(2)
facebook = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
facebook.click()
time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_id('email')
email.send_keys(EMAIL)
password = driver.find_element_by_id('pass')
password.send_keys(PASSWORD)
fb_login = driver.find_element_by_id('loginbutton')
fb_login.click()
time.sleep(5)
driver.switch_to.window(base_window)

location = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
location.click()
time.sleep(2)
notifications = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications.click()
time.sleep(2)
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()
time.sleep(2)

for n in range(100):

    time.sleep(random.randint(1,10))

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)
        try:
            star_profile = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]/span')
            star_profile.click()

        except NoSuchElementException:
            time.sleep(2)

        try:
            front_page = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]/span')
            front_page.click()

        except NoSuchElementException:
            time.sleep(2)

driver.quit()
