from dotenv import load_dotenv
import requests
import json
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, tequila_locations_url, FLIGHT_SEARCH_API_KEY, headers, put_headers):
        load_dotenv()
        self.FLIGHT_SEARCH_API_KEY = FLIGHT_SEARCH_API_KEY
        self.tequila_locations_url = tequila_locations_url
        self.headers = headers
        self.put_headers = put_headers
        self.prices = self.get_all_rows()
        pass

    def get_all_rows(self):
        SHEET_ENDPOINT_GET = os.getenv("SHEET_ENDPOINT_GET")
        response = requests.get(url=SHEET_ENDPOINT_GET)
        return response.json()['prices']

    def update_lowest_price(self, price, lowestFlightPriceInUSD):
        params = {
            "term": price['city']
        }

        response = requests.get(url=self.tequila_locations_url, headers=self.headers, params=params)

        price_data = {
            "price": {
                "lowestPrice": lowestFlightPriceInUSD,
            }
        }

        price_json = json.dumps(price_data)
        prices_url = f"https://api.sheety.co/4ed76cf9f0e4ec1f5172f38af2e3c4f4/flightDeals/prices/{price['id']}"

        prices_response = requests.put(url=prices_url, data=price_json, headers=self.put_headers)
        print(prices_response.json())

    def update_iata_codes(self):

        for price in self.prices:
            params = {
                "term": price['city']
            }

            response = requests.get(url=self.tequila_locations_url, headers=self.headers, params=params)
            iata_code = response.json()["locations"][0]["code"]

            price_data = {
                "price": {
                    "iataCode": iata_code,
                }
            }

            price_json = json.dumps(price_data)
            prices_url = f"https://api.sheety.co/4ed76cf9f0e4ec1f5172f38af2e3c4f4/flightDeals/prices/{price['id']}"

            prices_response = requests.put(url=prices_url, data=price_json, headers=self.put_headers)
            print(prices_response.json())