from app.helpers.router import router

router.make_class(
  name="user routes",
  url_prefix="/users"
  )
router.make_class(
  name="current user routes",
  url_prefix="/myself",
  classes=["user routes", "protected routes"],
  )

router.make_route(
  name="get current user",
  url="",
  classes=["current user routes", "retrieval routes"],
  description="retrieves the current user's information"
  )

router.make_route(
  name="get user subscriptions",
  url="/subscriptions",
  classes=["current user routes", "retrieval routes"],
  description=["retrieve all APIs subscribed to by the user"]
  )


router.make_route(
  name="delete current user",
  url="",
  classes=["current user routes", "protected routes", "deletion routes"],
  description="deletes the current user"
  )

router.make_route(
  name="forgot user password",
  url="/forgot-password",
  classes=["user routes", "creation routes"],
  description="Sends an email to the user with the code to send along the new password during password-reset"
  )

router.make_route(
  name="reset user password",
  url="/reset-password",
  classes=["user routes", "creation routes"],
  description="resets the user password"
  )

router.make_route(
  name="create user",
  url="",
  classes=["user routes", "creation routes"],
  middleware=["parameters"],
  description="creates a user"
  )

router.make_route(
  name="register user",
  url="/register",
  classes=["user routes", "creation routes"],
  middleware=["parameters"],
  description="registers a user"
  )

router.make_class(
  name="verification routes",
  classes=["user routes", "creation routes"],
  middleware=["parameters"]
  )

router.make_route(
  name="verify user",
  url="/verification/verify-code",
  classes=["user routes", "verification routes"],
  description="verifies a user account"
  )

router.make_route(
  name="send verification email",
  url="/verification/send-email",
  classes=["user routes", "verification routes"],
  description="sends a verification email to the given email. Note: there must be an account associated with the given email"
  )