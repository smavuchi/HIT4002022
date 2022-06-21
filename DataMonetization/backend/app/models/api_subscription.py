from datetime import datetime

from mongoengine.fields import StringField
from mongoengine.fields import DateTimeField
from mongoengine.fields import BooleanField
from mongoengine.fields import FloatField
from mongoengine.fields import IntField
from mongoengine.fields import ReferenceField

from mongoengine import Document
from app.helpers.models import dictor

class APISubscription(Document):
  api_id = StringField(required=True)
  package_id = StringField(required=True)
  user_id = StringField(required=True)

  requests = IntField(default=0)
  paid = FloatField(default=0)

  # timestamps
  expires_at = DateTimeField()
  modified_at = DateTimeField(default=datetime.utcnow)

  created_at = DateTimeField(default=datetime.utcnow)
  deleted_at = DateTimeField()

  def to_dict(self, **kwargs):
    return dictor(self, **kwargs)