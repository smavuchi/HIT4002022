import os
import datetime

def getenv(name, default=None):
  val = os.getenv(name, default)
  if val == '':
    return default
  return val

dir_path = os.path.dirname(os.path.realpath(__file__))
upload_dir = os.path.join(dir_path, "uploads")

class Config(object):
  DEBUG = getenv("FLASK_ENV", "DEVELOPMENT") == "DEBUG"
  ENV = getenv("FLASK_ENV")
  TESTING = getenv("TESTING") == "true"
  PROPAGATE_EXCEPTIONS = getenv("PROPAGATE_EXCEPTIONS", None)
  PRESERVE_CONTEXT_ON_EXCEPTION = getenv("PRESERVE_CONTEXT_ON_EXCEPTION")
  SECRET_KEY = getenv("SECRET_KEY")
  PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=int(getenv("PERMANENT_SESSION_LIFETIME", 31)))
  USE_X_SENDFILE = getenv("USE_X_SENDFILE", "false") == "true"
  SERVER_NAME = getenv("SERVER_NAME")
  APPLICATION_ROOT = getenv("APPLICATION_ROOT", "/")
  SESSION_COOKIE_NAME = getenv("SESSION_COOKIE_NAME", "session")
  SESSION_COOKIE_DOMAIN = getenv("SESSION_COOKIE_DOMAIN")
  SESSION_COOKIE_PATH = getenv("SESSION_COOKIE_PATH")
  SESSION_COOKIE_HTTPONLY = getenv("SESSION_COOKIE_HTTPONLY", "true") == "true"
  SESSION_COOKIE_SECURE = getenv("SESSION_COOKIE_SECURE", "false") == "true"
  SESSION_COOKIE_SAMESITE = getenv("SESSION_COOKIE_SAMESITE")
  SESSION_REFRESH_EACH_REQUEST = getenv("SESSION_REFRESH_EACH_REQUEST", "true") == "true"
  MAX_CONTENT_LENGTH = int(getenv("MAX_CONTENT_LENGTH")) if getenv("MAX_CONTENT_LENGTH", None) is not None else None
  SEND_FILE_MAX_AGE_DEFAULT = getenv("SEND_FILE_MAX_AGE_DEFAULT")
  TRAP_BAD_REQUEST_ERRORS = getenv("TRAP_BAD_REQUEST_ERRORS")
  TRAP_HTTP_EXCEPTIONS = getenv("TRAP_HTTP_EXCEPTIONS", "false") == "true"
  EXPLAIN_TEMPLATE_LOADING = getenv("EXPLAIN_TEMPLATE_LOADING", "false") == "true"
  PREFERRED_URL_SCHEME = getenv("PREFERRED_URL_SCHEME", "http")
  JSON_AS_ASCII = getenv("JSON_AS_ASCII", "true") == "true"
  JSON_SORT_KEYS = getenv("JSON_SORT_KEYS", "true") == "true"
  JSONIFY_PRETTYPRINT_REGULAR = getenv("JSONIFY_PRETTYPRINT_REGULAR", "true") == "true"
  JSONIFY_MIMETYPE = getenv("JSONIFY_MIMETYPE", "application/json")
  TEMPLATES_AUTO_RELOAD = getenv("TEMPLATES_AUTO_RELOAD")
  MAX_COOKIE_SIZE = int(getenv("MAX_COOKIE_SIZE", "4093"))

  HOST=getenv("HOST", "localhost")
  PORT=getenv("PORT", "5000")

  EMAIL=getenv("EMAIL")
  EMAIL_PASSWORD=getenv("EMAIL_PASSWORD")

  JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", "31")))
  JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES", "31")))

  MONGO_CONNECTION_STRING = getenv("MONGO_CONNECTION_STRING")
  UPLOAD_DIR = upload_dir