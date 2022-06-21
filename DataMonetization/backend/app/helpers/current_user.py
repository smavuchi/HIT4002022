import flask

def get_current_user():
  return flask.g.user