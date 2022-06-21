import datetime

from app.helpers.time import get_current_time

from app.models.api import API
from app.models.api_subscription import APISubscription
from app.models.api_request import APIRequest

from app.services.user.find_by_id import find_user_by_id
from app.services.api.statistics import get_statistics as get_api_statistics

def get_user_business_today(user):
  now = get_current_time()

  total_income = 0 
  total_income_clients = 0 
  
  apis_used = 0
  apis_used_clients = 0
  apis_used_hourly = [int(x) for x in list("0"*24)]

  requests_hourly = [int(x) for x in list("0"*24)]

  total_subscriptions = 0
  subscriptions_clients = 0
  subscriptions_hourly = [int(x) for x in list("0"*24)]

  api_ids = []

  for api in API.objects(owner=user.id):
    api_ids.append(str(api.id))

    stats = get_api_statistics(api)

    total_income += stats["total_revenue_today"]
    total_subscriptions += stats["total_subscribers_today"]
    subscriptions_clients += stats["total_subscribers_today"]
    total_income_clients += stats["total_subscribers_today"]

    requests_today = APIRequest.objects(api_id=str(api.id), created_at__gte=now - datetime.timedelta(hours=now.hour))

    if requests_today.count() > 0:
      apis_used += 1
      apis_used_clients += len(set([x.user_id for x in requests_today]))

  for hour in range(0, now.hour):
    apis = set()
    requests = APIRequest.objects(
      api_id__in=api_ids, 
      created_at__gte=now - datetime.timedelta(hours=now.hour) + datetime.timedelta(hours=hour),
      created_at__lt=now - datetime.timedelta(hours=now.hour) + datetime.timedelta(hours=hour + 1))
    subscriptions = APISubscription.objects(
      api_id__in=api_ids, 
      created_at__gte=now - datetime.timedelta(hours=now.hour) + datetime.timedelta(hours=hour),
      created_at__lt=now - datetime.timedelta(hours=now.hour) + datetime.timedelta(hours=hour + 1))

    for request in requests:
      apis.add(request.api_id)

    apis_used_hourly[hour] += len(apis)
    requests_hourly[hour] += requests.count()
    subscriptions_hourly[hour] += subscriptions.count()

  return {
    "total_income": total_income,
    "total_income_clients": total_income_clients,
    "apis_used": apis_used,
    "apis_used_clients": apis_used_clients,
    "apis_used_hourly": apis_used_hourly,
    "subscriptions": total_subscriptions,
    "subscriptions_clients": subscriptions_clients,
    "requests_hourly": requests_hourly,
    "subscriptions_hourly": subscriptions_hourly
  }