from datetime import datetime

from mongoengine import EmbeddedDocument

from mongoengine.fields import StringField
from mongoengine.fields import BooleanField
from mongoengine.fields import DateTimeField

from app.helpers.models import dictor

class Notification(EmbeddedDocument):
  __hidden = []
  __embedded_docs = []
  __embedded_lists = []

  title = StringField()
  message = StringField(required=True)
  created_at = DateTimeField(default=datetime.utcnow)
  modified_at = DateTimeField(default=datetime.utcnow)
  deleted_at = DateTimeField()

  def to_dict(self, **kwargs):
    return dictor(self, **kwargs)