import datetime

from app.helpers.time import get_current_time
from app.models.api_subscription import APISubscription
from app.models.api_request import APIRequest

def get_revenue(subscribers):
  revenue = 0
  for subscriber in subscribers:
    revenue += subscriber.paid
  return revenue

def get_statistics(api):
  now = get_current_time()

  subscribers = APISubscription.objects(api_id=str(api.id))
  subscribers_today = subscribers.filter(created_at__gte=now - datetime.timedelta(hours=now.hour))
  subscribers_this_month = subscribers.filter(created_at__gte=now.replace(day=1))
  active_subscribers = subscribers.filter(requests__gte=1, expires_at__gt=get_current_time())

  requests = APIRequest.objects(api_id=str(api.id))
  requests_today = requests.filter(created_at__gte=now - datetime.timedelta(hours=now.hour))
  requests_this_month = requests.filter(created_at__gte=now.replace(day=1))

  return {
    "total_subscribers": subscribers.count(),
    "total_subscribers_today": subscribers_today.count(),
    "total_subscribers_this_month": subscribers_this_month.count(),
    "total_active_subscribers": active_subscribers.count(),
    "total_revenue": get_revenue(subscribers),
    "total_revenue_today": get_revenue(subscribers_today),
    "total_revenue_this_month": get_revenue(subscribers_this_month),
    "total_requests": requests.count(),
    "total_requests_today": requests_today.count(),
    "total_requests_this_month": requests_this_month.count(),
  }