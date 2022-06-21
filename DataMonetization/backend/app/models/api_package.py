from datetime import datetime

from mongoengine.fields import ReferenceField
from mongoengine.fields import StringField
from mongoengine.fields import DateTimeField
from mongoengine.fields import BooleanField
from mongoengine.fields import IntField, FloatField

from mongoengine import Document
from app.helpers.models import dictor

class APIPackage(Document):
  __hidden = ["api_id"]

  api_id = StringField(default="")

  name = StringField(required=True)
  description = StringField(default="")
  pricing = FloatField(default=0.0)

  requests = IntField(required=True)

  # timestamps
  modified_at = DateTimeField(default=datetime.utcnow)
  created_at = DateTimeField(default=datetime.utcnow)
  deleted_at = DateTimeField()

  def to_dict(self, **kwargs):
    return dictor(self, **kwargs)