import flask
from app.helpers.router import router

def get_api_documentation():
  resolved, data = router.resolve()
  urls = set()

  for route in data:
    urls.add(route.url)

  urls = list(urls)
  urls.sort()
  
  routes = []

  for url in urls:
    routes += router.find_by_url(url)

  return flask.render_template("docs.html", routes=routes)