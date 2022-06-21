from app.helpers.router import router

router.make_class(
  name="api packages routes",
  url_prefix="/packages",
  classes=["specific api routes"]
  )
router.make_class(
  name="specific api package routes",
  url_prefix="/<string:package_id>",
  classes=["api packages routes"]
  )

router.make_route(
  name="add a new package to the API",
  url="",
  classes=["api packages routes", "creation routes"],
  description="adds a new package to the API"
  )

router.make_route(
  name="delete an API package",
  url="",
  classes=["specific api package routes", "deletion routes"],
  description="deletes package from the API"
  )

router.make_route(
  name="update an API package",
  url="/update",
  classes=["specific api package routes", "alteration routes"],
  description="updates a package on the API"
  )

router.make_route(
  name="get an API package",
  url="",
  classes=["specific api package routes", "retrieval routes"],
  description="gets a package on the API"
  )

router.make_route(
  name="get API packages",
  url="",
  classes=["api packages routes", "retrieval routes"],
  description="gets all package on the API"
  )