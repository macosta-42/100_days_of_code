from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

USERNAME = ""
PASSWORD = ""

chrome_driver_path = "/Users/matt/Documents/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2326238225&f_L=%C3%8Ele-de-France%2C%20France&geoId="
           "104246759&keywords=pentester&location=%C3%8Ele-de-France%2C%20France")

# Sign in
time.sleep(5)
sign = driver.find_element_by_xpath("/html/body/header/nav/div/a[2]")
sign.click()
time.sleep(5)
username = driver.find_element_by_css_selector("input#username")
username.send_keys(USERNAME)

password = driver.find_element_by_css_selector("input#password")
password.send_keys(PASSWORD)

sign = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
sign.click()
time.sleep(5)

messenger = driver.find_element_by_css_selector(".msg-overlay-bubble-header")
messenger.click()

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Register job and follow company
    job_register = driver.find_element_by_css_selector(".jobs-save-button")
    job_register.click()
    time.sleep(3)

    close_button = driver.find_element_by_xpath('/html/body/div[1]/section/ul/li/button')
    close_button.click()
