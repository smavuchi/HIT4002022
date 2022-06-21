from app.helpers.router import router

router.make_class(
  name="oauth routes",
  url_prefix="/oauth",
  classes=["auth routes"]
  )

router.make_route(
  name="google oauth",
  url="/google",
  classes=["oauth routes"],
  description="authenticates using a google token"
  )

router.make_route(
  name="facebook oauth",
  url="/facebook",
  classes=["oauth routes"],
  description="authenticates using a facebook token"
  )
