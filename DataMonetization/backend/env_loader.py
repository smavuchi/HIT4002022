from app.helpers.stepper import stepper

@stepper("loading env file")
def load_env():
  from dotenv import load_dotenv
  load_dotenv()

load_env()