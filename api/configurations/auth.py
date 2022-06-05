import os

from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

# Environment Variables
load_dotenv()

jwt = JWTManager()
jwt_secret_key = os.getenv("JWT_SECRET_KEY")