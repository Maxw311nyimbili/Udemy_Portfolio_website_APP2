# to enable the user of the form in the app to send an email,
# we use the module smtplib, and we need the receiver's email address as well as
# an email password generated by gmail called an "App password".

import smtplib, ssl

host = "smtp.gmail.com"
port = 465

user_name = "nyimbilimaxwell9@gmail.com"
password = "ivqywoctwwwiwzxe"

receiver = "nyimbilimaxwell9@gmail.com"

# include the backslash and write subject capitalized and put a space after the colon
# then write the intended subject that must be attached when the receiver gets the email

message = """\
Subject: Email From Portfolio App
Hi!
How are you.
"""
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(user_name, password)
    server.sendmail(user_name, receiver, message)