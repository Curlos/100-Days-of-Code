import requests
from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
trial_number = os.getenv("TRIAL_NUMBER")
verified_number = os.getenv("VERIFIED_NUMBER")

weather_params = {
    "lat": 47.751076,
    "lon": -120.740135,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params=weather_params)

print(response.status_code)
first_12_hourly = response.json()["hourly"][:12]
will_rain = False

for i in range(len(first_12_hourly)):
    weather_condition_code = first_12_hourly[i]["weather"][0]["id"]

    if weather_condition_code < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umbrella ☔️🌧",
        from_=trial_number,
        to=verified_number
    )

    print(message.status)
