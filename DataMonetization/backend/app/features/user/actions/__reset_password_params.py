from app.helpers.email import is_valid_email

parameters = [
  {
    "name": "username",
    "type": "string"
  },
  {
    "name": "email",
    "type": "string",
  },
  {
    "name": "phone",
    "type": "string"
  },
  {
    "name": "code",
    "type": "string",
    "required": True
  },
  {
    "name": "password",
    "type": "string",
    "required": True,
    "convert": False
  },
]