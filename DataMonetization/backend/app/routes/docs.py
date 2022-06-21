from app.helpers.router import router

router.make_class(
  name="docs routes",
  url_prefix="/docs",
  classes=["retrieval routes"]
  )

router.make_route(
  name="get api documentation",
  url="",
  classes=["docs routes"],
  description="retrieves documentation (use from browser window)"
  )
