import smtplib
import datetime as dt
import random


# Change the receiver email here
EMAIL_TO = ""

# Change your email and password here
EMAIL_FROM = ""
PASSWORD = ""

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as f:
        quotes = f.read().splitlines()

    rand_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_FROM, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_FROM,
            to_addrs=EMAIL_TO,
            msg=f"Subject:Monday Motivation\n\n{rand_quote}".encode('ascii', errors='ignore')
        )


# import smtplib

# # Change the receiver email here
# email_to = "macosta.devnet@yahoo.com"
#
# # Change your email and password here
# email_from = "macosta.devnet@gmail.com"
# password = "iDMlJ00IXgS4qo#8vMPI@x!^"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email_from, password=password)
#     connection.sendmail(
#         from_addr=email_from,
#         to_addrs=email_to,
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# # Change the receiver email here
# email_to = ""
#
# # Change your email and password here
# email_from = ""
# password = ""
#
# with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=email_from, password=password)
#     connection.sendmail(
#         from_addr=email_from,
#         to_addrs=email_to,
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(now)
# print(year)
# print(month)
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1985, month=11, day=2)
# print(date_of_birth)
