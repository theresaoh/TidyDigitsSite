from flask import Blueprint, request, jsonify
import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_handler = Blueprint('email_handler', __name__)


@email_handler.route('/send-email', methods=["POST"])
def test_duplicate_user():
  port = 465  # For SSL
  password = os.environ["EMAIL_PASSWORD"]
  sender_email = os.environ["EMAIL_ADDRESS"]
  receiver_email = request.json["email"]
  first_name = request.json["firstName"]
  last_name = request.json["lastName"]
  submitted_message = request.json["message"]
  email_to_user = MIMEMultipart("alternative")
  email_to_user["Subject"] = "Thank You For Contacting TidyDigits!"
  email_to_user["From"] = sender_email
  email_to_user["To"] = receiver_email
  if first_name != '':
    greeting = f"Hello {first_name}"
  else:
    greeting = "Hello There"

  # Create the plain-text and HTML version of your message
  email_to_user_plain_text = f"""
    {greeting},
    Thank you for contacting TidyDigits. We received your messsage and will be reaching out to you within 5-7 business days. 
    Message you submitted:
    {submitted_message}

    We look forward to doing business with you!
    TidyDigits Team
  """

  email_to_user_html = f"""
    <html>
    <head>
      <style>
      body {{text-align: center; font-family: 'Avenir', Helvetica, Arial, sans-serif; }}
      .container {{padding: 20px; border-radius: 10px;}}
      p {{font-size: 14px;}}
      </style>
    </head>
      <body>
        <div class="container">
          <h1>{greeting},</h1><br>
          <p>Thank you for contacting TidyDigits. We received your messsage and will be reaching out to you within 5-7 business days.<br>
            Message you submitted:<br>
            {submitted_message}<br><br>
            We look forward to doing business with you!<br>
            TidyDigits Team
          </p>
        </div>
      </body>
    </html>
  """

  email_to_admin = f"""\
    Subject: New Submission

    First Name: {first_name}
    Last Name: {last_name}
    Email Address: {receiver_email}
    Message: {submitted_message}
  """

  # Turn these into plain/html MIMEText objects
  part1 = MIMEText(email_to_user_plain_text, "plain")
  part2 = MIMEText(email_to_user_html, "html")

  # Add HTML/plain-text parts to MIMEMultipart message
  # The email client will try to render the last part first
  email_to_user.attach(part1)
  email_to_user.attach(part2)
  
  # Create a secure SSL context
  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, email_to_user.as_string())
      server.sendmail(sender_email, sender_email, email_to_admin)
  return jsonify(success=True)