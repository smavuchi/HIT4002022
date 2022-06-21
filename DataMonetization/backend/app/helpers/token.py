import jwt
import flask
import datetime

from app.helpers.http.response import report_expired_token_error
from app.helpers.http.response import report_invalid_token_error

def decode_token(encoded_jwt):
  app = flask.current_app
  try:
    return jwt.decode(encoded_jwt, app.config["SECRET_KEY"], algorithms=["HS256"])["some"]
  except jwt.ExpiredSignatureError:
    report_expired_token_error()
  except:
    report_invalid_token_error()

def encode_token(payload):
  app = flask.current_app

  return jwt.encode({
    "some": payload,
    "exp": datetime.datetime.now(tz=datetime.timezone.utc) + app.config["JWT_ACCESS_TOKEN_EXPIRES"]
    }, app.config["SECRET_KEY"], algorithm="HS256")