from flask import request

def get_client_ipaddress():
  return request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)