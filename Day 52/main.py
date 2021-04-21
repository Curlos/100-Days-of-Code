from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
import time
import os

class InstagramFollowerBot():
    def __init__(self):
        load_dotenv()
        chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
        self.INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

    def login_to_instagram(self):
        '''
        Logins to the user's Instagram account
        '''
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(self.INSTAGRAM_USERNAME)
        password.send_keys(self.INSTAGRAM_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def follow_account_followers(self, account_url="https://www.instagram.com/nba/"):
        '''
        Follows the followers of another person's Instagram account.
        Note: Instagram will automatically place a cooldown on the bot account
        if it detects an unusual amount of following activity in a short amount of time (like this bot)
        '''
        self.driver.get(account_url)
        people_following_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header'
                                                                    '/section/ul/li[2]/a')
        people_following_button.click()
        time.sleep(5)

        start_time = time.time()

        # Scrolls infinitely for 25 seconds and then all the account elements with the follow
        # button will have loaded in the html which can then be selected
        while True:
            if time.time() - start_time >= 25:
                break

            # If there are any accounts that I am not following in the window
            elem_in_popup = self.driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
            elem_in_popup.send_keys(Keys.END)

        accounts_to_follow = self.driver.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")

        for account in accounts_to_follow:
            print(account.text)
            account.click()

    def unfollow_everyone(self, account_url="https://www.instagram.com/real_goat_23_james"):
        self.driver.get(account_url)
        following_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        following_button.click()
        time.sleep(5)

        start_time = time.time()

        while True:
            # TODO: Instead of using a 25-second timer, need to change it to detect when the scroll has reached the end
            if time.time() - start_time >= 25:
                break

            try:
                elem_in_popup = self.driver.find_element_by_css_selector("button.sqdOP.L3NKy._8A5w5")
                elem_in_popup.send_keys(Keys.END)
            except:
                elem_in_popup = self.driver.find_element_by_css_selector("button.sqdOP.L3NKy._8A5w5")
                elem_in_popup.send_keys(Keys.END)

        accounts_to_unfollow = self.driver.find_elements_by_css_selector("button.sqdOP.L3NKy._8A5w5")

        for account in accounts_to_unfollow:
            print(account.text)
            account.click()
            time.sleep(1)

            unfollow_button = self.driver.find_element_by_css_selector("button.aOOlW.-Cab_")
            unfollow_button.click()

bot = InstagramFollowerBot()
bot.login_to_instagram()
bot.follow_account_followers()
#bot.unfollow_everyone()