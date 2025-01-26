# config.py
import os


class Config:
    SECRET_KEY = os.urandom(24)
    MONGO_URI = "mongodb://localhost:27017/social_media_app"


