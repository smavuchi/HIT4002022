import datetime
import secrets

from app.helpers.token import encode_token
from app.helpers.time import get_current_time

def get_credentials(user, returns="token"):
  data = {}

  if returns == "api-key":
    api_key = secrets.token_urlsafe(20)

    user.update(api_key=api_key, 
      api_key_expires_at=get_current_time() + datetime.timedelta(days=30))
    user.save()

    data["api-key"] = api_key
  else:
    data["token"] = encode_token(user.to_dict(only=[
      "id", "email", "username"
      ]))

  return data