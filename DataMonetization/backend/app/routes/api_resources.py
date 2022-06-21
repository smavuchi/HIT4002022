from app.helpers.router import router

router.make_class(
  name="api resources routes",
  url_prefix="/resources",
  classes=["specific api routes"]
  )
router.make_class(
  name="specific resource routes",
  url_prefix="/<string:resource_id>",
  classes=["api resources routes"]
  )

## routes
router.make_route(
  name="create API resource",
  url="",
  classes=["api resources routes", "creation routes"],
  description="gets an API resource"
  )
router.make_route(
  name="get API resources",
  url="",
  classes=["api resources routes", "retrieval routes"],
  description="gets API resources"
  )
router.make_route(
  name="get an API resource",
  url="",
  classes=["specific resource routes", "retrieval routes"],
  description="get an API resource"
  )
router.make_route(
  name="delete an API resource",
  url="",
  classes=["specific resource routes", "deletion routes"],
  description="deletes an API resource"
  )
router.make_route(
  name="update an API resource",
  url="/update",
  classes=["specific resource routes", "alteration routes"],
  description="updates an API resource"
  )
router.make_route(
  name="publish an API resource",
  url="/publish",
  classes=["specific resource routes", "creation routes"],
  description="publishes an API resource. Exposes endpoints for consumption"
  )