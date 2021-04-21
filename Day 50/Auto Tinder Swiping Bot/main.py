from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv()

FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")
TINDER_LOGIN_URL = os.getenv("TINDER_LOGIN_URL")

chrome_driver_path = "/Users/curlos/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")
time.sleep(5)

login = driver.find_element_by_css_selector('a[href="/app/login"]')
login.click()
time.sleep(5)

login_with_facebook = driver.find_element_by_css_selector('button[aria-label="Log in with Facebook"]')
login_with_facebook.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

driver.get(TINDER_LOGIN_URL)
email = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
email.send_keys(FACEBOOK_EMAIL)
password.send_keys(FACEBOOK_PASSWORD)
password.send_keys(Keys.ENTER)

