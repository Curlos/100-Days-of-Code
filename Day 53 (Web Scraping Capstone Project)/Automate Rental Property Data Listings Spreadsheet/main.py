from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import time
import os


class RentalPropertyData():
    def __init__(self):
        load_dotenv()
        chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.ZILLOW_RENTAL_URL = os.getenv("ZILLOW_RENTAL_URL")
        self.GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")
        self.prices = []
        self.addresses = []
        self.links = []

    def get_rental_listings(self):
        # TODO: Use BeautifulSoup and requests to scrape all the listings from the web address
        HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
                    'Accept-Language': 'en-US, en;q=0.5'})
        URL = self.ZILLOW_RENTAL_URL
        response = requests.get(URL, headers=HEADERS)
        listings_html = response.text

        self.driver.get(self.ZILLOW_RENTAL_URL)
        self.driver.maximize_window()

        soup = BeautifulSoup(listings_html, "html.parser")

        prices = soup.select(".list-card-price")
        addresses = soup.select(".list-card-addr")
        links = soup.select(".list-card-link")

        self.prices = [price.getText() for price in prices]
        self.addresses = [address.getText() for address in addresses]

        for a in links:
            if a['href'].startswith("https://www.zillow.com/"):
                self.links.append(a['href'])
            else:
                print(a['href'])
                print('https://www.zillow.com' + a['href'])
                self.links.append('https://www.zillow.com' + a['href'])

    def get_rental_listings_multiple_pages(self):
        # TODO: Scrape the info from several pages instead of just one to see all the available options

        pass

    def fill_in_form(self):
        # TODO: Use selenium to fill in the google form with the info from self.listings
        for i in range(len(self.prices)):
            self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfPVSzHcZLQPlKr-kBKZenjZR9S6hFMIBHCnOZomqTiHQaNGA"
                            "/viewform")

            time.sleep(3)

            inputs = self.driver.find_elements_by_css_selector("input.quantumWizTextinputPaperinputInput.exportInput")
            address = inputs[0]
            price = inputs[1]
            link = inputs[2]
            submit = self.driver.find_element_by_css_selector("span.appsMaterialWizButtonPaperbuttonLabel"
                                                              ".quantumWizButtonPaperbuttonLabel.exportLabel")

            address.send_keys(self.addresses[i])
            price.send_keys(self.prices[i])
            link.send_keys(self.links[i])
            submit.click()


rent = RentalPropertyData()
rent.get_rental_listings()
rent.fill_in_form()
