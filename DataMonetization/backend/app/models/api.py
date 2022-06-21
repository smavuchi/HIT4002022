from datetime import datetime

from mongoengine.fields import StringField
from mongoengine.fields import DateTimeField
from mongoengine.fields import BooleanField
from mongoengine.fields import ListField
from mongoengine.fields import ReferenceField

from mongoengine import Document

from app.models.api_package import APIPackage
from app.models.api_dataset import APIDataset
from app.models.api_resource import APIResource
from app.models.user import User

from app.helpers.models import dictor

class API(Document):
  __hidden = ["packages", "statistics", "resources"]
  __referenced_docs = {
    "owner": ["id", "email", "phone", "username"],
    "statistics": "*"
  }
  __referenced_docs_lists = {
    "resources": ["id", "name"],
    "packages": ["id", "name"],
  }

  # metadata
  owner = ReferenceField(User)
  owner_email = StringField(required=True)
  name = StringField(required=True)
  title = StringField(default="")
  description = StringField(default="")

  # ...
  packages = ListField(ReferenceField(APIPackage))
  resources = ListField(ReferenceField(APIResource))

  # publishing
  published = BooleanField(default=False)
  published_at = DateTimeField()

  # timestamps
  modified_at = DateTimeField(default=datetime.utcnow)
  created_at = DateTimeField(default=datetime.utcnow)
  deleted_at = DateTimeField()

  def to_dict(self, **kwargs):
    return dictor(self, **kwargs)