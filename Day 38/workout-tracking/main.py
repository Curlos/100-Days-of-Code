from dotenv import load_dotenv
from datetime import datetime
import requests
import json
import os

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
USER_ID = os.getenv("USER_ID")
AUTHORIZATION_HEADER = os.getenv("AUTHORIZATION_HEADER")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Authorization": AUTHORIZATION_HEADER
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
add_workout_endpoint = SHEET_ENDPOINT
query = {
    "query": "I ran 3 miles and walked 2 miles"
}

response = requests.post(url=exercise_endpoint, data=query, headers=headers)
exercises = response.json()["exercises"]
print(exercises)

post_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
    "Authorization": AUTHORIZATION_HEADER
}

for exercise in exercises:
    workout = {
        "workout": {
            "date": datetime.now().strftime('%x'),
            "time": datetime.now().strftime('%X'),
            "exercise": exercise["name"].title(),
            "duration": round(exercise["duration_min"]),
            "calories": round(exercise["nf_calories"])
        }
    }

    workout_json = json.dumps(workout)

    workout_response = requests.post(url=add_workout_endpoint, data=workout_json, headers=post_headers)
    print(workout_response)
    print(workout_response.json())