parameters = [
  {
    "name": "username",
    "type": "string",
    "required": True
  },
  {
    "name": "password",
    "type": "string",
    "convert": False
  },
  {
    "name": "returns",
    "type": "string",
    "required": True,
    "values": ["api-key", "token"]
  },
]