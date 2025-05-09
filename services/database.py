from configs.config import Settings
from pymango import MongoClient


class DB:
    
    client = MongoClient(Settings.MONGO_URI)
    db = client(Settings.MONGO_DB_NAME)