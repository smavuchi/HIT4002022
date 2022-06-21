import flask

def get_header(name):
  return flask.request.headers.get(name, None)

def get_headers(*names):
  items = {}
  for name in names:
    items[name] = get_header(name)
  return items