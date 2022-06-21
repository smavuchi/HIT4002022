def dictify(model, exclude=[], only=[], embedded_docs_lists=[], embedded_docs=[], referenced_docs={}, referenced_docs_lists={}):
  temp = {**model.to_mongo().to_dict()}

  try:
    temp["id"] = str(model.id)
    del temp["_id"]
  except:
    pass

  if len(only) > 0:
    result = {}

    for field in only:
      result[field] = temp.get(field)

    temp = result

  for field in exclude:
    try:
      del temp[field]
    except: 
      pass

  for embedded_list in embedded_docs_lists:
    if embedded_list in temp:
      temp[embedded_list] = [x.to_dict() for x in temp[embedded_list]]

  for embedded_doc in embedded_docs:
    if embedded_doc in temp:
      temp[embedded_doc] = temp[embedded_doc].to_dict()

  for refdoc_list in referenced_docs_lists:
    if refdoc_list not in temp:
      continue

    fields = referenced_docs_lists[refdoc_list]

    if fields == []:
      pass
    elif fields == "*":
      temp[refdoc_list] = [document.to_dict() for document in model.__getattribute__(refdoc_list)]
    else:
      temp[refdoc_list] = [document.to_dict(only=fields) for document in model.__getattribute__(refdoc_list)]

  for referenced_doc in referenced_docs:
    if referenced_doc not in temp:
      continue

    fields = referenced_docs[referenced_doc]
    document = model.__getattribute__(referenced_doc)

    if fields == []:
      del temp[referenced_doc]
    elif fields == "*":
      temp[referenced_doc] = document.to_dict()
    else:
      temp[referenced_doc] = document.to_dict(only=fields)

  return temp

def model_to_dict(model, *args, **kwargs):
  return model.to_dict(*args, **kwargs)

def dictor(self, exclude=[], only=[]):
  classname = str(self.__class__._class_name)

  __hidden = getattr(self.__class__, f"_{classname}__hidden", []) + exclude
  __embedded_docs = getattr(self.__class__, f"_{classname}__embedded_docs", []) 
  __embedded_docs_lists = getattr(self.__class__, f"_{classname}__embedded_docs_lists", []) 
  __referenced_docs = getattr(self.__class__, f"_{classname}__referenced_docs", {}) 
  __referenced_docs_lists = getattr(self.__class__, f"_{classname}__referenced_docs_lists", {}) 

  return dictify(self, 
    exclude=__hidden, 
    only=only,
    embedded_docs=__embedded_docs,
    embedded_docs_lists=__embedded_docs_lists,
    referenced_docs=__referenced_docs,
    referenced_docs_lists=__referenced_docs_lists)