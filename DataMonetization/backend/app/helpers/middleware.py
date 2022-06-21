from functools import wraps

registered_middleware = {}

def register_middleware(name, function):
  registered_middleware[name] = function

def middleware(*names, **middleware_kwargs):
  middleware_list = []

  for name in names:
    if name not in registered_middleware:
      raise RuntimeError(f"Middleware not found: {name}")
    middleware_list.append(registered_middleware[name])

  def inner(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
      middleware_results = {}

      for func in middleware_list:
        ret = func(**middleware_kwargs)
        if ret:
          middleware_results = {**middleware_results, **ret}

      if not middleware_results:
        return function(*args, **kwargs)
      return function(*args, **middleware_results, **kwargs)
    return wrapper
  
  return inner