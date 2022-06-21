from app.models.user import User
from app.helpers.models import Model
from app.helpers.http.response import report_bad_request_error
from app.helpers.http.response import report_not_found_error
from app.services.user.find_user import find_user

def verify_user(email="", username="", phone="", code=""):
  user = find_user(email=email, phone=phone, username=username)

  if not user:
    report_not_found_error("no such user exists")

  if user.verification_code != code:
    report_bad_request_error("invalid verification code")

  Model.modify(user, verified=True, verification_code=None)