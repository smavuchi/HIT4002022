from app.models.user import User

from app.helpers.http.response import report_forbidden_error
from app.helpers.http.response import report_not_found_error
from app.helpers.passwords import verify_password
from app.helpers.credentials import get_credentials

def authenticate(phone, password, returns):
  user = User.objects(phone=phone).first()

  if not user:
    report_not_found_error("no such user exists")

  if not verify_password(password, user.password):
    report_forbidden_error("invalid credentials")

  return get_credentials(user, returns)