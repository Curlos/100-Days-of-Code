##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
from dotenv import load_dotenv
import smtplib
import os
import datetime as dt
from random import choice
import pandas

load_dotenv()
my_email = "johnsmith42302049234@gmail.com"
quotes = []
now = dt.datetime.now()
df = pandas.read_csv("birthdays.csv")
all_birthday_letters = {}

for row in df.iterrows():
    name = row[1][0]
    email = row[1].email
    year = row[1].year
    month = row[1].month
    day = row[1].day

    if now.day == day and now.month == month:
        new_lines = ''

        with open("letter_templates/letter_1.txt") as f:
            new_lines = f.read().replace("[NAME]", name)
            all_birthday_letters[email] = new_lines

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=os.getenv("PASSWORD"))

    for email, letter in all_birthday_letters.items():
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{letter}")
        print("Email sent!")
    connection.close()
