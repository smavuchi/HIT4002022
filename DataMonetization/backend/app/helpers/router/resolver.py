class RouteResolver(object):
  def __init__(self, router):
    self.router = router

  def _resolve_route(self, route):
    parent_url_prefix = ""
    for parent in route.classes:
      parent = self.resolve_route_by_name(parent, route.name)

      if len(route.methods) == 0:
        route.methods = parent.methods
      
      for middleware in parent.middleware:
        if middleware not in route.middleware:
          route.middleware.append(middleware)

      for role in parent.roles:
        if role not in route.roles:
          route.roles.append(role)

      if parent.requires_user:
        route.requires_user = True

      if parent.url_prefix:
        parent_url_prefix = parent.url_prefix

    route.url_prefix = parent_url_prefix + route.url_prefix
    route.url = "/api" + self.router._api_version + route.url_prefix + route.url

  def resolve_route(self, route):
    if route.status == "resolved":
      return route

    if route.status == "resolving":
      raise RuntimeError(f"error during route resolution: cyclic dependency on route '{route.name}'")

    route.status = "resolving"
    self._resolve_route(route)
    route.status = "resolved"

    if route.kind == "route":
      self.router._routes.append(route)

    return route

  def resolve_route_by_name(self, name, child=""):
    if name not in self.router.routes:
      text = f"route not found '{name}'. "

      if child:
        text += f"Specified as parent of '{child}'"

      raise RuntimeError(text)
    return self.resolve_route(self.router.routes[name])

  def resolve(self, throw=True): 
    for route in self.router.routes:
      try:
        error = self.resolve_route_by_name(route)
      except Exception as e:
        return False, str(e)
        if throw: 
          raise

    return True, self.router._routes

  def __call__(self):
    return self.resolve()