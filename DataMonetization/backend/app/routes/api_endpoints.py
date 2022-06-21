from app.helpers.router import router

router.make_class(
  name="api endpoint routes",
  url_prefix="/endpoints",
  classes=["specific resource routes"]
  )
router.make_class(
  name="specific endpoint routes",
  url_prefix="/<string:action>",
  classes=["api endpoint routes"]
  )


router.make_route(
  name="gets an API endpoint's statistics",
  url="/statistics",
  classes=["retrieval routes", "specific endpoint routes"],
  description="gets statistics for an API endpoint"
  )

router.make_route(
  name="gets an API endpoint's documentation",
  url="/docs",
  classes=["retrieval routes", "specific endpoint routes"],
  description="gets documentation for an API endpoint"
  )

router.make_route(
  name="updates an API endpoint",
  url="/update",
  classes=["alteration routes", "specific endpoint routes"],
  description="updates an endpoint from the API"
  )

router.make_route(
  name="get API endpoints",
  url="",
  classes=["api endpoint routes", "retrieval routes"],
  description="gets endpoints from the API"
  )
