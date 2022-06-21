from app.helpers.router import router

router.make_class(
  name="auth routes",
  url_prefix="/auth",
  methods=["POST"],
  middleware=["parameters"]
  )

router.make_route(
  name="email-password auth",
  url="/email",
  classes=["auth routes"],
  description="authenticates using email and password"
  )

router.make_route(
  name="phone-password auth",
  url="/phone",
  classes=["auth routes"],
  description="authenticates using phone number and password"
  )

router.make_route(
  name="username-password auth",
  url="/username",
  classes=["auth routes"],
  description="authenticates using username and password"
  )
