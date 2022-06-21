from app.models.api_subscription import APISubscription
from app.services.api_package.delete_subscription import delete_subscription

def delete_package(package):
  subscriptions = APISubscription.objects(package_id=str(package.id))
  for subscription in subscriptions:
    delete_subscription(subscription)
  package.delete()