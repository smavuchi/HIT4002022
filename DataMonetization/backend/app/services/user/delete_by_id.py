from app.models.user import User
from app.services.user.find_by_id import find_user_by_id
from app.services.user.delete_user import delete_user

def delete_user_by_id(user_id):
  user = find_user_by_id(str(user_id))

  if not user:
    report_not_found_error("user not found: ", str(user_id))

  return delete_user(user)