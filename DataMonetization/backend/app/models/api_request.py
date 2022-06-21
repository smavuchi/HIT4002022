from datetime import datetime

from mongoengine.fields import StringField
from mongoengine.fields import DateTimeField
from mongoengine.fields import BooleanField
from mongoengine.fields import IntField
from mongoengine.fields import DictField
from mongoengine.fields import ReferenceField

from mongoengine import Document
from app.helpers.models import dictor

class APIRequest(Document):
  __hidden = ["api_id", "user_id"]
  __embedded_docs_lists = ["features"]

  api_id = StringField(required=True)
  user_id = StringField(required=True)

  # request
  endpoint = StringField(required=True)
  url = StringField(required=True)
  request_headers = DictField()

  # timestamps
  modified_at = DateTimeField(default=datetime.utcnow)
  created_at = DateTimeField(default=datetime.utcnow)
  deleted_at = DateTimeField()

  def to_dict(self, **kwargs):
    return dictor(self, **kwargs)