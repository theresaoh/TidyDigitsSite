from flask import Blueprint
import smtplib, ssl
import os

email_handler = Blueprint('email_handler', __name__)

port = 465  # For SSL
password = os.environ["EMAIL_PASSWORD"]
email = os.environ["EMAIL_ADDRESS"]

sender_email = "no-reply@adomain.com"
message = (f'From: {sender_email}\nTo: {email}\nSubject: Hi There\n\nThis is a message sent with Python! How neat is that?!')

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(email, password)
    server.sendmail(sender_email, email, message)