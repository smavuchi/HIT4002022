from app.helpers.router import router

router.make_route(
  name="current user statistics",
  url_prefix="/statistics",
  classes=["current user routes", "retrieval routes"]
  )