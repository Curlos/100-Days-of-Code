import requests
from pprint import pprint

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

question_data = response.json()["results"]
