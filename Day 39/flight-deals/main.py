from dotenv import load_dotenv
from flight.data_manager import DataManager
from flight.flight_search import FlightSearch
from flight.notification_manager import NotificationManager
import os

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager flight_utils to achieve the program requirements.
load_dotenv()
tequila_kiwi_base_url = "https://tequila-api.kiwi.com"
tequila_locations_url = tequila_kiwi_base_url + "/locations/query"
tequila_search_url = tequila_kiwi_base_url + "/v2/search/"
FLIGHT_SEARCH_API_KEY = os.getenv("FLIGHT_SEARCH_API_KEY")
SHEET_ENDPOINT_GET = os.getenv("SHEET_ENDPOINT_GET")

headers = {
    "apikey": FLIGHT_SEARCH_API_KEY
}

put_headers = {
    "Content-Type": "application/json"
}
sheet = DataManager(tequila_locations_url, FLIGHT_SEARCH_API_KEY, headers, put_headers)
prices = sheet.get_all_rows()

search = FlightSearch(tequila_locations_url, tequila_search_url, FLIGHT_SEARCH_API_KEY, headers, put_headers)
cheapest_flights = search.search_for_flights(prices)

notify = NotificationManager(cheapest_flights)
notify.send_notification()
