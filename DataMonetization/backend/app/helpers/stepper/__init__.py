from functools import wraps
from app.helpers.logger import logger

def stepper(message):
  def inner(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
      logger.step(message)
      result = function(*args, **kwargs)
      logger.done(message)
      return result
    return wrapper
  return inner