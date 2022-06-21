from app.models.user import User

def find_user_by_api_key(key):
  return User.objects(api_key=key).first()