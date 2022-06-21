import smtplib
from flask import current_app

# Import the email modules we'll need
from email.message import EmailMessage

def send_email(sender, receiver, message):
  msg = EmailMessage()
  msg.set_content(message["content"])

  msg['Subject'] = message.get("subject")
  msg['From'] = sender["email"]
  msg['To'] = receiver["email"]

  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login(sender["email"], sender["password"])
  s.send_message(msg)
  s.quit()

def send_email_from_app(receiver, message):
  send_email({
    "email": current_app.config.get("EMAIL"), 
    "password": current_app.config.get("EMAIL_PASSWORD")
  }, receiver, message)