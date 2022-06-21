import flask
import json

from .helpers import *

class Reponse(object):
  def __init__(self):
    self._status = 200
    self._data = None
    self._message = "success"
    self._headers = {}
    self._extras = {}

  def status(self, new_code):
    self._status = new_code
    return self

  def data(self, new_data):
    self._data = new_data
    return self

  def header(self, name, value):
    self._headers[name] = value
    return self
  
  def message(self, value):
    self._message = value
    return self

  def headers(self, **kwargs):
    for arg in kwargs:
      self.header(arg, kwargs[arg])

    return self

  def make(self):
    return make_response(
      data=self._data,
      status=self._status,
      message=self._message,
      headers=self._headers,
      **self._extras)

  def __call__(self):
    return self.make()

response = Reponse()