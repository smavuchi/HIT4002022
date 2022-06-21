class Route(object): 
  def __init__(self, kind):
    self.kind = kind
    self.name=""
    self.methods=[]
    self.middleware=[]
    self.requires_user=False
    self.roles=[]
    self.classes=[]
    self.url_prefix=""
    self.url=""
    self.parameters=None
    self.description=""

    self.status = "unresolved"

  def set_parameters(self, params):
    self.parameters = params

  def to_dict(self):
    parameters = [{
      "name": param.get("name"),
      "type": param.get("type"),
      "required": param.get("required", False),
    } for param in (self.parameters if self.parameters else [])]

    return {
      "name": self.name,
      "methods": self.methods,
      "middleware": self.middleware,
      "roles": self.roles,
      "classes": self.classes,
      "url_prefix": self.url_prefix,
      "url": self.url,
      "parameters": parameters,
      "description": self.description,
    }