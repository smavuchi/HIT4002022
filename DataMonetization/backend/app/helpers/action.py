from app.helpers.http.response import make_response

def action_response(result=None):
  result = result if result else {}

  status = result.get("status", 200)
  data = result.get("data", None)
  message = result.get("message", "success")
  headers = result.get("headers", {})

  return make_response(data=data, status=status, message=message, headers=headers)