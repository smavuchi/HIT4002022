from app.helpers.router import router

router.make_class(
  name="api query routes",
  url_prefix="/query/<string:api_name>/<string:resource_name>",
  classes=["protected routes"]
  )

# querying
# router.make_route(
#   name="perform a POST query on an API endpoint",
#   url="",
#   classes=["api query routes", "creation routes"],
#   description="perform a POST query on an API endpoint"
#   )
router.make_route(
  name="perform a GET query on an API endpoint",
  url="",
  classes=["api query routes", "retrieval routes"],
  description="performs a GET BY ID query on an API endpoint"
  )
# router.make_route(
#   name="perform a GET BY ID query on an API endpoint",
#   url="/<string:item_id>",
#   classes=["api query routes", "retrieval routes"],
#   description="performs a GET BY ID query on an API endpoint"
#   )
# router.make_route(
#   name="perform a PUT or PATCH query on an API endpoint",
#   url="/<string:item_id>",
#   classes=["api query routes", "alteration routes"],
#   description="performs a PUT query on an API endpoint"
#   )
# router.make_route(
#   name="perform a DELETE BY ID query on an API endpoint",
#   url="/<string:item_id>",
#   classes=["api query routes", "deletion routes"],
#   description="performs a DELETE BY ID query on an API endpoint"
#   )
# router.make_route(
#   name="perform a DELETE query on an API endpoint",
#   url="",
#   classes=["api query routes", "deletion routes"],
#   description="performs a DELETE query on an API endpoint"
#   )