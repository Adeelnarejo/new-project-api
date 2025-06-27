import smtplib, ssl
import os



def send_email(user_email, message):
    host = "smtp.gmail.com"
    port = 465

    username = "user email"
    password = "user password"

    receiver_email = user_email

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)