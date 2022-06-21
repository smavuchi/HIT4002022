from bson import ObjectId

from app.models.api_subscription import APISubscription
from app.models.api import API
from app.helpers.time import get_current_time

def get_subscriptions(user_id):  
  apis = []

  for subscription in APISubscription.objects(user_id=user_id, expires_at__gt=get_current_time(), requests__gte=1):
    api = API.objects(id=ObjectId(subscription.api_id)).first()
    apis.append({
      "api": api.to_dict(),
      "subscription": subscription.to_dict()
    })

  return apis