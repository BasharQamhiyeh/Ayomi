import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://root:example@mongo:27017/app_db")  # Default to local MongoDB
