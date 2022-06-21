from app.helpers.email import is_valid_email

parameters = [
  # personal details
  {
    "name": "first_name",
    "type": "string",
    "required": True,
  },
  {
    "name": "last_name",
    "type": "string",
    "required": True,
  },
  {
    "name": "title",
    "type": "string",
  },

  # contact details
  {
    "name": "phone",
    "type": "string",
  },
  {
    "name": "username",
    "type": "string"
  },
  {
    "name": "email",
    "type": "string",
    "required": True,
    "validator": is_valid_email
  },
  {
    "name": "facebook",
    "type": "string",
  },
  {
    "name": "twitter",
    "type": "string",
  },
  {
    "name": "instagram",
    "type": "string",
  },
  # account details
  {
    "name": "password",
    "type": "string",
    "required": True,
    "convert": False
  },
  {
    "name": "confirmation_password",
    "type": "string",
    "required": True,
    "convert": False
  }
]