from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os

class InternetSpeedTwitterBot():
    def __init__(self):
        load_dotenv()
        chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = os.getenv("PROMISED_DOWN")
        self.up = os.getenv("PROMISED_UP")
        self.TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
        self.TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()
        time.sleep(100) # After clicking, my internet speed safely takes under 100 seconds to return the results
        ping_speed = float(self.driver.find_element_by_class_name("ping-speed").text)
        download_speed = float(self.driver.find_element_by_class_name("download-speed").text)
        upload_speed = float(self.driver.find_element_by_class_name("upload-speed").text)

        return download_speed, upload_speed

    def tweet_at_provider(self, download_speed, upload_speed):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        email_input = self.driver.find_element_by_name("session[username_or_email]")
        password_input = self.driver.find_element_by_name("session[password]")

        email_input.send_keys(self.TWITTER_EMAIL)
        password_input.send_keys(self.TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        tweet_button.click()

        tweet_text = f"Hey @comcastcares, why is my internet speed {download_speed}down/{upload_speed}up when I pay for {self.down}down/{self.up}up? " \
                     f"I'm ABSOLUTELY APPALLED at this and will be" \
                     f" switching to @ATT where they know how to provide high speeds."

        compose_tweet = self.driver.find_element_by_class_name("public-DraftStyleDefault-ltr")
        compose_tweet.send_keys(tweet_text)

        send_tweet = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div['
                                                       '4]/div/div/div[2]/div[4]/div/span/span')
        send_tweet.click()

bot = InternetSpeedTwitterBot()
download_speed, upload_speed = bot.get_internet_speed()
bot.tweet_at_provider(download_speed, upload_speed)