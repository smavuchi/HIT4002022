from app.models.user import User
from app.helpers.database.mongo import str_to_id

def find_user_by_id(user_id):
  return User.objects(id=str_to_id(user_id)).first()