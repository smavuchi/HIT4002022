parameters = [
  {
    "name": "name",
    "type": "string",
    "required": True,
  },
  {
    "name": "description",
    "type": "string"
  },
  {
    "name": "url_prefix",
    "type": "string"
  },
  {
    "name": "url_name",
    "type": "string"
  },
  {
    "name": "actions",
    "type": "list",
    "default": ["index", "show", "create", "delete", "clear", "update"]
  },
]