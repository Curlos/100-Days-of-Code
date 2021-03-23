from dotenv import load_dotenv
import smtplib
import os
import requests
from datetime import datetime
import time

load_dotenv()
MY_LAT = -50.76  # Your latitude
MY_LONG = -127.528  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


def iss_close(iss_latitude, iss_longitude):
    if iss_latitude >= MY_LAT - 5 and iss_latitude <= MY_LAT + 5:
        if iss_longitude >= MY_LONG - 5 and iss_longitude <= MY_LONG + 5:
            return True
    return False


def is_dark():
    if time_now.hour >= sunset:
        return True


def send_email():
    if iss_close(iss_latitude, iss_longitude) and is_dark():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            my_email = os.getenv("EMAIL")
            my_password = os.getenv("PASSWORD")
            to_email = os.getenv("TO_EMAIL")
            connection.starttls()
            connection.login(user=my_email, password=my_password)

            connection.sendmail(from_addr=my_email, to_addrs=to_email,
                                msg=f"Subject:Look up!\n\nThe ISS is currently above your position at the coordinates: {iss_latitude}, {iss_longitude}")
            print("Email sent!")
            connection.close()


while True:
    print(iss_latitude, iss_longitude)
    send_email()
    time.sleep(5)


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
