import random
from app.models.user import User

from app.helpers.http.response import report_bad_request_error
from app.helpers.http.response import report_forbidden_error
from app.helpers.passwords import hash_password
from app.helpers.models import Model

from app.services.user.verification_email import send_verification_email

def create_user(password, **attributes):
  if User.objects(email=attributes.get("email")).first():
    report_forbidden_error("email already taken")
  
  if attributes.get("username") and User.objects(username=attributes.get("username")).first():
    report_forbidden_error("username already taken")

  password = hash_password(password)
  created, result = Model.create(User, 
    password=password, 
    **attributes)

  if not created:
    report_bad_request_error(result)

  send_verification_email(attributes.get("email"))
  return result