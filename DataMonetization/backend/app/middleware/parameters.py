import flask
import re

from app.helpers.http.response import report_bad_request_error

### @TODO: refactor this file!!!!

def get_input_data(src):
  input_data = {}

  if src == "form-data":
    return flask.request.form

  if flask.request.method == "GET":
    return flask.request.args
  elif flask.request.method == "POST":
    return flask.request.json
  else:
    return {}

def handle_string_param(param_name, value, requirements):
  value = str(value).strip()

  if requirements.get("convert", True):
    value = value.lower()

  if "regex" in requirements:
    regex = requirements["regex"]
    pattern = re.compile(regex)

    if not pattern.match(value):
      report_bad_request_error("invalid %s (does not match regex: %s)" % (param_name, regex))

  if "regex_s" in requirements:
    regex = requirements["regex_s"]
    pattern = re.compile(regex)

    if not pattern.search(value):
      report_bad_request_error("invalid %s (does not match regex: %s)" % (param_name, regex))

  minlen = requirements.get("minlen", None)
  maxlen = requirements.get("maxlen", None)
  require_special_chars = requirements.get("require_special_chars", False)
  require_digits = requirements.get("require_digits", False)
  require_mixed_case = requirements.get("require_mixed_case", False)

  if minlen is not None and len(value) < minlen:
    report_bad_request_error("%s must be of length > %d" % (param_name, minlen))
  
  if maxlen is not None and len(value) > maxlen:
    report_bad_request_error("%s must be of length < %d" % (param_name, maxlen))

  if require_digits and not re.compile("[0-9]+").search(value):
    report_bad_request_error("%s must contain digits" % param_name)
  
  if require_special_chars and not re.compile(r"[!@#\$%^&\*\(\);\:\.,/\\]+").search(value):
    report_bad_request_error("%s must contain special characters" % param_name)

  if require_mixed_case:
    uppercase_regex = re.compile("[A-Z]+")
    lowercase_regex = re.compile("[a-z]+")

    if not uppercase_regex.search(value):
      report_bad_request_error("%s must also contain uppercase characters" % param_name)
    
    if not lowercase_regex.search(value):
      report_bad_request_error("%s must also contain lowercase characters" % param_name)

  return value

def handle_range_requirements(param_name, value, requirements):
  if ">" in requirements and value <= requirements[">"]:
    report_bad_request_error("{} must be > {}".format(param_name, requirements[">"]))
  elif ">=" in requirements and value < requirements[">"]:
    report_bad_request_error("{} must be >= {}".format(param_name, requirements[">="]))
  elif "<" in requirements and value >= requirements["<"]:
    report_bad_request_error("{} must be < {}".format(param_name, requirements["<"]))
  elif "<=" in requirements and value > requirements["<"]:
    report_bad_request_error("{} must be <= {}".format(param_name, requirements["<="]))

def handle_equality_requirements(param_name, value, requirements):
  if "==" in requirements and value != requirements["=="]:
    report_bad_request_error("{} must be {}".format(param_name, requirements["=="]))
  elif "!=" in requirements and value == requirements["!="]:
    report_bad_request_error("{} must be not be {}".format(param_name, requirements["!="]))

# @TODO: refactor this
def middleware(params={}, **kwargs):
  src = params.get("src", "query")
  defns = params.get("defns", [])

  processed_input_data = {}
  input_data = get_input_data(src)
  missing_parameters = []

  for defn in defns:
    param_name = defn["name"]
    param_type = defn.get("type", "string")
    validator = defn.get("validator", lambda x: True)
    values = defn.get("values", [])

    if param_name not in input_data:
      if defn.get("required", False):
        missing_parameters.append(param_name)
        continue

      value = None

      if "default" in defn:
        value = defn["default"]

      processed_input_data[param_name] = value
      continue

    value = input_data[param_name]

    if param_type == "string":
      value = handle_string_param(param_name, value, defn)

    elif param_type == "list":
      pass
    
    elif param_type == "json":
      try: value = dict(value)
      except: report_bad_request_error("%s must be an integer" % param_name)
      else: pass
    
    elif param_type == "integer":
      try: value = int(value)
      except: report_bad_request_error("%s must be an integer" % param_name)
      else: handle_range_requirements(param_name, value, defn)

    elif param_type == "float":
      try: value = float(value)
      except: report_bad_request_error("%s must be a float" % param_name)
      else: handle_range_requirements(param_name, value, defn)

    elif param_type == "boolean":
      try: 
        if str(value).lower() in ["1", "yes", "true", "aye"]:
          value = True
        elif str(value).lower() in ["0", "no", "false", "nay"]:
          value = False
        else:
          raise RuntimeError("unknown boolean value: %s" % str(value))
      except: 
        report_bad_request_error("%s must be a boolean" % param_name)

    else:
      raise RuntimeError("unknown param type: %s" % param_type)

    handle_equality_requirements(param_name, value, defn)

    if len(values) > 0 and value not in values:
      report_bad_request_error("%s must be one of: %s" % (param_name, repr(values)))

    if not validator(value):
      report_bad_request_error("invalid value supplied for %s" % param_name)

    transform = defn.get("transform", lambda x: x)
    processed_input_data[param_name] = transform(value)

  if len(missing_parameters) > 0:
    report_bad_request_error("missing parameters: %s" % ", ".join(missing_parameters))

  return processed_input_data