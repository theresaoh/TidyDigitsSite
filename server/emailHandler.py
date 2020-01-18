from flask import Blueprint, request, jsonify
import smtplib, ssl
import os

email_handler = Blueprint('email_handler', __name__)


@email_handler.route('/send-email', methods=["POST"])
def test_duplicate_user():
  port = 465  # For SSL
  password = os.environ["EMAIL_PASSWORD"]
  sender_email = os.environ["EMAIL_ADDRESS"]
  email = request.json["email"]
  first_name = request.json["firstName"]
  last_name = request.json["lastName"]
  submitted_message = request.json["message"]


  sender_email = "testingpythonemails@gmail.com"
  message = (f'From: {sender_email}\nTo: {email}\nSubject: Hello\n\n{submitted_message}')

  # Create a secure SSL context
  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, email, message)
  return jsonify(success=True)