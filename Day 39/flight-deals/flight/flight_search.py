from dotenv import load_dotenv
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from currency_converter import CurrencyConverter
from .data_manager import DataManager
import requests
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, tequila_locations_url, tequila_search_url, FLIGHT_SEARCH_API_KEY, headers, put_headers):
        load_dotenv()
        self.FLIGHT_SEARCH_API_KEY = FLIGHT_SEARCH_API_KEY
        self.tequila_locations_url = tequila_locations_url
        self.tequila_search_url = tequila_search_url
        self.headers = headers
        self.put_headers = put_headers
        self.cheapest_flights = []

    def search_for_flights(self, prices):
        sheet_data = DataManager(self.tequila_locations_url, self.FLIGHT_SEARCH_API_KEY, self.headers, self.put_headers)

        for price in prices:
            today = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
            date_six_months_later = (datetime.now() + relativedelta(months=+6)).strftime("%d/%m/%Y")

            params = {
                "fly_from": price['iataCode'],
                "date_from": today,
                "date_to": date_six_months_later
            }

            response = requests.get(url=self.tequila_search_url, headers=self.headers, params=params)
            flights = response.json()[
                'data']  # The Tequila API seems to sort the prices of each flight from lowest to greatest
            lowestFlightPrice = flights[0]['price']

            currency = list(flights[0]['conversion'].keys())[0]
            c = CurrencyConverter()
            lowestFlightPriceInUSD = c.convert(lowestFlightPrice, currency, 'USD')

            if lowestFlightPriceInUSD < price['lowestPrice']:
                cheapestFlightInfo = {}
                cheapestFlightInfo['lowestFlightPriceInUSD'] = lowestFlightPriceInUSD
                cheapestFlightInfo['flight_from'] = f"{flights[0]['cityFrom']}-{flights[0]['flyFrom']}"
                cheapestFlightInfo['flight_to'] = f"{flights[0]['cityTo']}-{flights[0]['flyTo']}"
                cheapestFlightInfo['date_from'] = flights[0]["route"][0]['utc_departure'][:10]
                cheapestFlightInfo['date_to'] = flights[0]["route"][0]['utc_arrival'][:10]
                self.cheapest_flights.append(cheapestFlightInfo)

                # Update the lowest price on the sheet
                sheet_data.update_lowest_price(price, round(lowestFlightPriceInUSD))

        return self.cheapest_flights