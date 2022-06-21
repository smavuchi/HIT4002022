from app.helpers.router import router

router.make_class(
  name="api subscription routes",
  url_prefix="/subscriptions",
  classes=["specific api package routes"]
  )

router.make_route(
  name="make an API subscription",
  url="",
  classes=["api subscription routes", "creation routes"],
  description="makes a subscription on the API"
  )