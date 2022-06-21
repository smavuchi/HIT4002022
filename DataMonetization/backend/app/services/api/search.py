from app.models.api import API
from mongoengine.queryset.visitor import Q

def search_apis(query, limit, offset, owner=None):
  filters = Q(name__icontains=query) | Q(title__icontains=query) | Q(description__icontains=query)

  if owner:
    filters = filters & Q(owner_email=owner)

  return API.objects.filter(filters).skip(offset).limit(limit)