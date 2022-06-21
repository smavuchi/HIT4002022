from app.models.user import User

def find_user(email=None, phone=None, username=None):
  user = None
  if email:
    user = User.objects(email=email).first()
  elif username:
    user = User.objects(username=username).first()
  elif phone:
    user = User.objects(phone=phone).first()
  return user