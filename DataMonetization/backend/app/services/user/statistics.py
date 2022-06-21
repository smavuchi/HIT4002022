import datetime

from app.helpers.time import get_current_time
from app.helpers.database.mongo import str_to_id

from app.services.api.statistics import get_statistics as get_api_statistics
from app.models.api import API
from app.models.api_package import APIPackage
from app.models.api_subscription import APISubscription

from app.services.user.find_by_id import find_user_by_id

def get_statistics(user):
  now = get_current_time()

  total_income = 0
  total_income_this_month = 0
  total_income_this_month_pct = 0

  total_payment = 0
  total_payment_this_month = 0
  total_payment_this_month_pct = 0

  total_apis = API.objects(owner=user.id).count()
  total_apis_this_month = API.objects(owner=user.id, created_at__gte=now.replace(day=1)).count()
  total_apis_this_month_pct = 0

  total_subscriptions = 0
  total_subscriptions_this_month = 0
  total_subscriptions_this_month_pct = 0

  recent_subscribers = []
  recent_subscriptions = []

  api_ids = []

  for api in API.objects(owner=user.id):
    api_ids.append(str(api.id))

    stats = get_api_statistics(api)

    total_income += stats["total_revenue"]
    total_income_this_month += stats["total_revenue_this_month"]

    total_subscriptions += stats["total_subscribers"]
    total_subscriptions_this_month += stats["total_subscribers_this_month"]

  for subscription in APISubscription.objects(api_id__in=api_ids).order_by("-created_at").limit(5):
    user = find_user_by_id(subscription.user_id)
    if user:
      recent_subscribers.append(user.to_dict(only=["id", "first_name", "last_name", "email", "username", "phone"]))
      recent_subscriptions.append({
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "api": API.objects(id=str_to_id(subscription.api_id)).first().name,
        "package": APIPackage.objects(id=str_to_id(subscription.package_id)).first().name
        })

  for subscription in APISubscription.objects(user_id=str(user.id)):
    total_payment += subscription.paid

  for subscription in APISubscription.objects(user_id=str(user.id), created_at__gte=now.replace(day=1)):
    total_payment_this_month += subscription.paid

  return {
    "total_income": total_income,
    "total_income_this_month": total_income_this_month,
    "total_income_this_month_pct": round(total_income_this_month/total_income * 100, 2) if total_income > 0 else 0,
    "total_payment": total_payment,
    "total_payment_this_month": total_payment_this_month,
    "total_payment_this_month_pct": round(total_payment_this_month/total_payment * 100, 2) if total_payment > 0 else 0,
    "total_apis": total_apis,
    "total_apis_this_month": total_apis_this_month,
    "total_apis_this_month_pct": round(total_apis_this_month/total_apis * 100, 2) if total_apis > 0 else 0,
    "total_subscriptions": total_subscriptions,
    "total_subscriptions_this_month": total_subscriptions_this_month,
    "total_subscriptions_this_month_pct": round(total_subscriptions_this_month / total_subscriptions * 100, 2) if total_subscriptions > 0 else 0,
    "recent_subscribers": recent_subscribers,
    "recent_subscriptions": recent_subscriptions
  }