import requests
from app.models.user import User

from app.helpers.http.response import report_not_found_error
from app.helpers.http.response import report_bad_request_error

from app.helpers.credentials import get_credentials

def authenticate(token, returns):
  r = requests.get(f"https://graph.facebook.com/me?access_token={token}")

  if r.status_code != 200:
    report_bad_request_error(f"facebook responded with error: {r.json()['error']['message']}")

  json = r.json()

  #### @TODO: figure out how to get the email from the facebook response json
  user = User.objects(email=json["email"]).first()

  if not user:
    report_not_found_error("no such user exists")

  return get_credentials(user, returns)