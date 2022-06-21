from datetime import datetime

from mongoengine.fields import StringField
from mongoengine.fields import DateTimeField
from mongoengine.fields import BooleanField
from mongoengine.fields import ListField
from mongoengine.fields import DictField

from mongoengine import Document
from app.helpers.models import dictor

class APIDataset(Document):
  __hidden = ["filename"]

  resource_id = StringField(default="")

  id_columns = ListField(StringField())

  title = StringField()
  filename = StringField()

  column_types = DictField()

  percentage_missing_values_by_column = DictField()
  kurt_per_column = DictField()
  columns_description = DictField()

  # timestamps
  modified_at = DateTimeField(default=datetime.utcnow)
  created_at = DateTimeField(default=datetime.utcnow)
  deleted_at = DateTimeField()

  def to_dict(self, **kwargs):
    return dictor(self, **kwargs)