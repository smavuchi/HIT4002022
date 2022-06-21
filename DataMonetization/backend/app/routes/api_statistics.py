from app.helpers.router import router

router.make_class(
  name="api statistics routes",
  url_prefix="/statistics",
  classes=["specific api routes"]
  )

router.make_route(
  name="get API statistics",
  url="",
  classes=["api statistics routes", "retrieval routes"],
  description="gets statistics of the API"
  )