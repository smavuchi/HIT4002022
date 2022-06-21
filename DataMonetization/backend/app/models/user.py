from datetime import datetime

from mongoengine.fields import ListField
from mongoengine.fields import StringField
from mongoengine.fields import DateTimeField
from mongoengine.fields import BooleanField
from mongoengine.fields import EmbeddedDocumentField

from app.models.notification import Notification

from mongoengine import Document
from app.helpers.models import dictor

class User(Document):
  __hidden = ["verification_code", "notifications", "api_key", "password", "password_reset_verification_code", "modified_at"]
  __embedded_docs_lists = ["notifications"]

  # personal information
  first_name = StringField(required=True)
  last_name = StringField(required=True)
  title = StringField()

  # contact details
  phone = StringField()
  email = StringField(required=True)
  facebook = StringField()
  twitter = StringField()
  instagram = StringField()
  addresses = ListField(StringField())

  # account details
  username = StringField()
  password = StringField(required=True)
  notifications = ListField(Notification)
  role = StringField()
  verified = BooleanField(default=False)
  verification_code = StringField()
  password_reset_verification_code = StringField(default="")

  api_key = StringField()
  api_key_expires_at = DateTimeField()

  # timestamps
  modified_at = DateTimeField(default=datetime.utcnow)
  created_at = DateTimeField(default=datetime.utcnow)
  deleted_at = DateTimeField()

  def to_dict(self, **kwargs):
    return dictor(self, **kwargs)