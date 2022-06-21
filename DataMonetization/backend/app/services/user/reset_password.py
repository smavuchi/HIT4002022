from app.helpers.models import Model
from app.helpers.http.response import report_bad_request_error
from app.helpers.http.response import report_not_found_error
from app.services.user.find_user import find_user
from app.helpers.passwords import hash_password

def reset_password(password="", email="", username="", phone="", code=""):
  user = find_user(email=email, phone=phone, username=username)

  if not user:
    report_not_found_error("no such user exists")

  if user.password_reset_verification_code != code:
    report_bad_request_error("invalid verification code")

  password = hash_password(password)
  Model.modify(user, password=password, password_reset_verification_code=None)