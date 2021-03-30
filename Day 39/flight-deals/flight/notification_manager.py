from dotenv import load_dotenv
from twilio.rest import Client
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, cheapest_flights):
        load_dotenv()
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.trial_number = os.getenv("TRIAL_NUMBER")
        self.verified_number = os.getenv("VERIFIED_NUMBER")
        self.cheapest_flights = cheapest_flights
        pass

    def create_message_body(self, cheapest_flight_info):
        """ Create the message body. """

        lowestFlightPriceInUSD = cheapest_flight_info['lowestFlightPriceInUSD']
        flight_from = cheapest_flight_info['flight_from']
        flight_to = cheapest_flight_info['flight_to']
        date_from = cheapest_flight_info['date_from']
        date_to = cheapest_flight_info['date_to']

        messageBody = f"Only ${round(lowestFlightPriceInUSD)} to fly from {flight_from} to {flight_to}, from {date_from} to {date_to}."

        return messageBody

    def send_notification(self):
        """ Send a notification to a specified phone number using the message body. """
        if len(self.cheapest_flights) > 0:

            for cheapest_flight_info in self.cheapest_flights:
                messageBody = self.create_message_body(cheapest_flight_info)

                client = Client(self.account_sid, self.auth_token)

                message = client.messages \
                    .create(
                    body=messageBody,
                    from_=self.trial_number,
                    to=self.verified_number
                )

                print(message.status)