from bs4 import BeautifulSoup
from twilio.rest import Client
import smtplib
from dotenv import load_dotenv
import os
import requests

class StockTracker():
    def __init__(self):
        load_dotenv()

    def scrape_page(self):
        HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
                    'Accept-Language': 'en-US, en;q=0.5'})
        URL = "https://www.amazon.com/Apple-MWP22AM-A-AirPods-Pro/dp/B07ZPC9QD4"
        response = requests.get(URL, headers=HEADERS)
        product_html = response.text

        return product_html, URL

    def check_in_stock(self):
        notify_by = int(input("How would you like to be notified when the item is back in stock?"
                              " Enter a number from 1-3 from the following options: "
                              "\n1. Text"
                              "\n2. Email"
                              "\n3. Both Text and Email\n"))

        product_html, URL = self.scrape_page()
        soup = BeautifulSoup(product_html, "html.parser")
        product_name = soup.select_one("#productTitle").getText().replace('\n', '').strip('')
        product_price = float(soup.select_one('#priceblock_ourprice').getText()[1:])
        in_stock_text = soup.select_one("#availability").getText().replace('\n', '').strip()
        in_stock = 'in stock' in in_stock_text.lower()

        if notify_by == 1:
            self.send_text(product_name, product_price, in_stock)
        elif notify_by == 2:
            self.send_email(product_name, product_price, in_stock, URL)
        elif notify_by == 3:
            self.send_text(product_name, product_price, in_stock)
            self.send_email(product_name, product_price, in_stock, URL)

    def send_text(self, product_name, product_price, in_stock):
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        trial_number = os.getenv("TRIAL_NUMBER")
        verified_number = os.getenv("VERIFIED_NUMBER")

        product_price_formatted = "{:.2f}".format(product_price)

        if in_stock:
            client = Client(account_sid, auth_token)
            messageBody = f"🚨BREAKING NEWS! '{product_name}' on Amazon for ${product_price_formatted} is IN STOCK!"
            message = client.messages \
                .create(
                body=messageBody,
                from_=trial_number,
                to=verified_number
            )

            print(message.status)

    def send_email(self, product_name, product_price, in_stock, URL):
        if in_stock:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                my_email = os.getenv("EMAIL")
                my_password = os.getenv("PASSWORD")
                to_email = os.getenv("TO_EMAIL")
                connection.starttls()
                connection.login(user=my_email, password=my_password)

                product_price_formatted = "{:.2f}".format(product_price)
                connection.sendmail(from_addr=my_email, to_addrs=to_email,
                                    msg=f"Subject:BREAKING NEWS! '{product_name}' on Amazon on "
                                        f"sale for ${product_price_formatted} is IN STOCK!"
                                        f"\n\nClick here to buy {product_name} for {product_price_formatted}: {URL}")
                print("Email sent!")
                connection.close()

    def check_price(self):
        notify_by, product_name, product_price, user_price, URL = self.scrape_product_price()

        if notify_by == 1:
            self.send_text(product_name, product_price, user_price)
        elif notify_by == 2:
            self.send_email(product_name, product_price, user_price, URL)
        elif notify_by == 3:
            self.send_text(product_name, product_price, user_price)
            self.send_email(product_name, product_price, user_price, URL)