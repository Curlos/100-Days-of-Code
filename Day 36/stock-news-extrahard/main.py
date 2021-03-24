from alpha_vantage.timeseries import TimeSeries
from twilio.rest import Client
from dotenv import load_dotenv
import requests
import os

load_dotenv()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ts = TimeSeries(key=STOCK_API_KEY)
data = ts.get_daily(symbol=STOCK)

yesterday = list(data[0].keys())[0]
stockYesterdayInfo = data[0][yesterday]
stockYesterdayPrice = float(stockYesterdayInfo['4. close'])

dayBefore = list(data[0].keys())[1]
stockDayBeforeInfo = data[0][dayBefore]
stockDayBeforePrice = float(stockDayBeforeInfo['4. close'])
percentageDiff = ((stockYesterdayPrice - stockDayBeforePrice) / stockDayBeforePrice) * 100
roundedPercentageDiff = round((int(percentageDiff) * -1))

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}"
response = requests.get(news_url)
articles = response.json()["articles"][:3]

for article in articles:
    print(article["title"])

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
trial_number = os.getenv("TRIAL_NUMBER")
verified_number = os.getenv("VERIFIED_NUMBER")

if percentageDiff <= -1 or percentageDiff >= 1:
    stock_change_symbol = ''

    if percentageDiff <= -1:
        stock_change_symbol = "🔻"
    elif percentageDiff >= 1:
        stock_change_symbol = "🔺"

    messages = []

    for article in articles:
        messages.append(f"{STOCK}: {stock_change_symbol}{roundedPercentageDiff}%\nHeadline: {article['title']}\nBrief: {article['description']}")

    client = Client(account_sid, auth_token)

    for messageBody in messages:
        message = client.messages \
            .create(
            body=messageBody,
            from_=trial_number,
            to=verified_number
        )

        print(message.status)
