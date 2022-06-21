from app.helpers.http.response import report_bad_request_error
from bson import ObjectId

def id_to_str(_id):
  return str(_id)

def str_to_id(id_str):
  try:
    return ObjectId(id_str)
  except:
    report_bad_request_error("invalid id provided: %s" % str(id_str))