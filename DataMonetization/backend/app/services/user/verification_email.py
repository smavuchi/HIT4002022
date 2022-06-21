import random
from app.models.user import User

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_internal_server_error
from app.helpers.models import Model
from app.helpers.email import send_email_from_app

def send_verification_email(email):
  user = User.objects(email=email).first()

  if not user:
    report_not_found_error("user not found")

  verification_code = str(random.randrange(100000, 999999))
  Model.modify(
    user,
    verified=False,
    verification_code=verification_code)

  try:
    send_email_from_app(receiver={
      "email": email
      }, 
      message={
        "subject": "Account verification",
        "content": f"Your account needs to be verified so that we know the email address actually belongs to you. Use the following code to verify:\n{verification_code}"
      })
  except:
    report_internal_server_error("could not send verification email. Please try again later")