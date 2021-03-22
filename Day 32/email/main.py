from dotenv import load_dotenv
import smtplib
import os
import datetime as dt
from random import choice

load_dotenv()
my_email = "johnsmith42302049234@gmail.com"
quotes = []
now = dt.datetime.now()

with open("quotes.txt") as f:
    quotes = f.readlines()

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=os.getenv("PASSWORD"))
    connection.sendmail(from_addr=my_email, to_addrs="curlosmart@gmail.com",
                        msg=f"Subject:Monday Motivation\n\n{choice(quotes)}")
    print("Email sent!")
    connection.close()