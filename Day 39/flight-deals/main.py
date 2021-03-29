from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from dateutil import tz
from currency_converter import CurrencyConverter
import requests
import json
import os

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
load_dotenv()
tequila_kiwi_base_url = "https://tequila-api.kiwi.com"
tequila_locations_url = tequila_kiwi_base_url + "/locations/query"
tequila_search_url = tequila_kiwi_base_url + "/v2/search/"
FLIGHT_SEARCH_API_KEY = os.getenv("FLIGHT_SEARCH_API_KEY")
SHEET_ENDPOINT_GET = os.getenv("SHEET_ENDPOINT_GET")

# Twilio API Information
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
trial_number = os.getenv("TRIAL_NUMBER")
verified_number = os.getenv("VERIFIED_NUMBER")

headers = {
    "apikey": FLIGHT_SEARCH_API_KEY
}

response = requests.get(url=SHEET_ENDPOINT_GET)
prices = response.json()['prices']

"""put_headers = {
    "Content-Type": "application/json"
}

for price in prices:
    params = {
        "term": price['city']
    }

    response = requests.get(url=tequila_locations_url, headers=headers, params=params)
    iata_code = response.json()["locations"][0]["code"]

    price_data = {
        "price": {
            "iataCode": iata_code,
        }
    }

    price_json = json.dumps(price_data)
    prices_url = f"https://api.sheety.co/4ed76cf9f0e4ec1f5172f38af2e3c4f4/flightDeals/prices/{price['id']}"

    prices_response = requests.put(url=prices_url, data=price_json, headers=put_headers)
    print(prices_response.json())"""

for price in prices:
    today = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
    date_six_months_later = (datetime.now() + relativedelta(months=+6)).strftime("%d/%m/%Y")
    print
    params = {
        "fly_from": price['iataCode'],
        "date_from": today,
        "date_to": date_six_months_later
    }

    response = requests.get(url=tequila_search_url, headers=headers, params=params)
    flights = response.json()['data']  # The Tequila API seems to sort the prices of each flight from lowest to greatest
    lowestFlightPrice = flights[0]['price']

    currency = list(flights[0]['conversion'].keys())[0]
    c = CurrencyConverter()
    currency_USD = c.convert(lowestFlightPrice, currency ,'USD')

    # Creating message body
    flight_from = f"{flights[0]['cityFrom']}-{flights[0]['flyFrom']}"
    flight_to = f"{flights[0]['cityTo']}-{flights[0]['flyTo']}"
    date_from = flights[0]["route"][0]['utc_departure'][:10]
    date_to = flights[0]["route"][0]['utc_arrival'][:10]

    messageBody = f"Only ${round(currency_USD)} to fly from {flight_from} to {flight_to}, from {date_from} to {date_to}."


    if lowestFlightPrice < price['lowestPrice']:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=messageBody,
            from_=trial_number,
            to=verified_number
        )

        print(message.status)

