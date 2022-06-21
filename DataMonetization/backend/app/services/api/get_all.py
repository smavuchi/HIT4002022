from app.models.api import API

def get_all_apis(offset=0, limit=100, owner=None):
  stuff = API.objects

  if owner:
    stuff = stuff.filter(owner_email=owner)

  return stuff.order_by("-created_at").skip(offset).limit(limit)