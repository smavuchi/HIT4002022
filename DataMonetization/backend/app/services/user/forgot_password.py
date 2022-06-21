import random
from app.models.user import User

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_internal_server_error
from app.helpers.models import Model
from app.helpers.email import send_email_from_app
from app.services.user.find_user import find_user

def forgot_password(email=None, phone=None, username=None):
  user = find_user(email=email, phone=phone, username=username)
  if not user:
    report_not_found_error("user not found")

  password_reset_verification_code = str(random.randrange(100000, 999999))
  Model.modify(
    user,
    verified=False,
    password_reset_verification_code=password_reset_verification_code)

  try:
    send_email_from_app(receiver={
      "email": email
      }, 
      message={
        "subject": "Password reset",
        "content": f"Use the following code to reset your account password:\n{password_reset_verification_code}"
      })
  except:
    report_internal_server_error("could not send password-reset email. Please try again later")