from .resolver import RouteResolver
from .route import Route

class Router(object):
  def __init__(self):
    self._api_version = "/v1"
    self.routes = {}
    self._routes = []
    self.classes = []

  def api_version(self, version): 
    self._api_version = ("/" + version) if version else ""

  def find_by_url(self, url):
    stuff = []
    for item in self.routes:
      if self.routes[item].url == url and self.routes[item].kind == "route":
        stuff.append(self.routes[item])
    return stuff

  def make_route(self,
    name="",
    methods=[],
    middleware=[],
    roles=[],
    requires_user=False,
    classes=[],
    url_prefix="",
    url="",
    kind="route",
    description="",
    parameters=[],
    throw=True
    ): 
    if name in self.routes:
      if throw:
        raise RuntimeError(f"route name '{name}' already taken")
      else:
        return f"route name '{name}' already taken"

    self.routes[name] = Route(kind=kind)
    self.routes[name].name=name
    self.routes[name].methods=list(set(methods))
    self.routes[name].middleware=list(set(middleware))
    self.routes[name].roles=list(set(roles))
    self.routes[name].classes=list(set(classes))
    self.routes[name].url_prefix=url_prefix
    self.routes[name].url=url
    self.routes[name].requires_user=requires_user
    self.routes[name].description=description
    self.routes[name].parameters=parameters

  def make_class(self, **kwargs): 
    self.classes.append(kwargs.get("name"))
    self.make_route(kind="class", **kwargs)

  def resolve(self):
    return RouteResolver(self)()

router = Router()