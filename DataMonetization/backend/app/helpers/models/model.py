import datetime

class Model(object):
  def create(model, **kwargs):
    try:
      item = model(**kwargs)
      return True, Model.created(item).reload()
    except KeyError as e:
      return False, "missing value: " + repr(e)
    except:
      return False, "invalid details provided."

  def modify(model, **kwargs):
    print("@@@@@@@@@@@@@@@@@", kwargs)
    attrs = {attr: kwargs[attr] for attr in kwargs if kwargs[attr] is not None}

    if not attrs:
      return True, model

    try:
      model.update(**attrs)
      return True, Model.modified(model).reload()
    except KeyError as e:
      return False, "missing value: " + repr(e)
    except:
      return False, "invalid details provided."

  def create_filters(exact_matches, inexact_matches, **kwargs):
    filters = {}

    for field in exact_matches:
      if kwargs[field]:
        filters[field] = kwargs[field]  

    for field in inexact_matches:
      if kwargs[field]:
        filters[field + "__icontains"] = kwargs[field]

    if kwargs["id"]:
      filters["id"] = make_id(kwargs["id"])

    return filters

  def created(model):
    model.created_at = datetime.datetime.utcnow()
    model.save()
    return model

  def modified(model):
    model.modified_at = datetime.datetime.utcnow()
    model.save()
    return model

  def deleted(model):
    model.deleted_at = datetime.datetime.utcnow()
    model.save()
    return model
