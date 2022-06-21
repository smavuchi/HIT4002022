from email_validator import validate_email, EmailNotValidError

def is_valid_email(text):
  return True
  try:
    valid = validate_email(text.strip())
    return True
  except EmailNotValidError as e:
    return False