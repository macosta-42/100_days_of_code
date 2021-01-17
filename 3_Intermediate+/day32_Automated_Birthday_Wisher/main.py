from datetime import datetime
import pandas
import random
import smtplib

# Change the receiver email here
EMAIL_TO = ""

# Change your email and password here
EMAIL_FROM = ""
PASSWORD = ""

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthdays_dict[today]
    with open(file_path) as letter_file:
        content = letter_file.read()
        new_letter = content.replace("[NAME]", birthday_person["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_FROM, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_FROM,
                to_addrs=EMAIL_TO,
                msg=f"Subject:Happy Birthday\n\n{new_letter}"
            )
