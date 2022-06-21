from app.helpers.router import router

router.make_route(
  name="current user business today",
  url_prefix="/business-today",
  classes=["current user routes", "retrieval routes"],
  )