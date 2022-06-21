from app.helpers.router import router

router.make_class(
  name="api routes",
  url_prefix="/client-api",
  classes=["protected routes"]
  )
router.make_class(
  name="specific api routes",
  url_prefix="/<string:api_id>",
  classes=["api routes"]
  )

router.make_route(
  name="create api",
  url="",
  classes=["api routes", "creation routes"],
  description="creates an API"
  )

router.make_route(
  name="create api key",
  url="/key",
  classes=["specific api routes", "creation routes"],
  description="creates an API key for the current user"
  )

router.make_route(
  name="update api",
  url="/update",
  classes=["specific api routes", "alteration routes"],
  description="updates an API"
  )

router.make_route(
  name="delete an api",
  url="",
  classes=["specific api routes", "deletion routes"],
  description="deletes an API"
  )

router.make_route(
  name="get an api",
  url="",
  classes=["specific api routes", "retrieval routes"],
  description="retrieves an API"
  )

router.make_route(
  name="publish an api",
  url="/publish",
  classes=["specific api routes", "creation routes"],
  description="publishes an API"
  )

router.make_route(
  name="get API documentation",
  url="/docs",
  classes=["specific api routes", "retrieval routes"],
  description="get API documentation"
  )

router.make_route(
  name="get apis",
  url="",
  classes=["api routes", "retrieval routes"],
  description="retrieves APIs"
  )

router.make_route(
  name="search apis",
  url="/search",
  classes=["api routes", "retrieval routes"],
  description="searches APIs"
  )

router.make_route(
  name="gets an API subscription",
  url="/subscription",
  classes=["specific api routes", "retrieval routes"],
  description="gets an API subscription"
  )