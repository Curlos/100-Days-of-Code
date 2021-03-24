from dotenv import load_dotenv
import requests
import os

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
query = {
    "query": "I ran 3 miles and walked 2 miles"
}

response = requests.post(url=exercise_endpoint, data=query, headers=headers)
print(response.json())