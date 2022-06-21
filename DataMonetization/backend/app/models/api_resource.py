from datetime import datetime

from mongoengine.fields import StringField
from mongoengine.fields import DateTimeField
from mongoengine.fields import BooleanField
from mongoengine.fields import IntField
from mongoengine.fields import DictField
from mongoengine.fields import ListField
from mongoengine.fields import ReferenceField

from mongoengine import Document

from app.helpers.models import dictor

class APIResource(Document):
  __hidden = ["api_id", "endpoints"]
  __embedded_docs_lists = ["endpoints"]

  api_id = StringField(default="")
  name = StringField(required=True)
  description = StringField(default="")
  url_prefix = StringField()
  url_name = StringField()
  actions = ListField(StringField())

  # publishing
  published = BooleanField(default=False)
  published_at = DateTimeField()

  # timestamps
  modified_at = DateTimeField(default=datetime.utcnow)
  created_at = DateTimeField(default=datetime.utcnow)
  deleted_at = DateTimeField()

  def to_dict(self, **kwargs):
    return dictor(self, **kwargs)