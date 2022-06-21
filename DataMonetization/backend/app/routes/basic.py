from app.helpers.router import router
router.api_version("v1")

router.make_class(
  name="creation routes",
  methods=["POST"],
  classes=["takes parameters", "protected routes"]
  )
router.make_class(
  name="retrieval routes",
  methods=["GET"],
  classes=["takes parameters"]
  )
router.make_class(
  name="alteration routes",
  methods=["POST"],
  classes=["takes parameters", "protected routes"]
  )
router.make_class(
  name="deletion routes",
  methods=["DELETE"],
  classes=["protected routes"]
  )

# protection
router.make_class(
  name="protected routes",
  middleware=["authorization"],
  requires_user=True
  )

router.make_class(
  name="admin routes",
  classes=["protected routes"],
  roles=["admin"]
  )

# other
router.make_class(
  name="takes parameters",
  middleware=["parameters"]
  )