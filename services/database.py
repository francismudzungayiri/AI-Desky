from configs.config import Settings
from pymongo import MongoClient


class DB:
    
    def __init__(self) -> None:
        
        self.client = MongoClient(Settings.MONGO_URI)
        self.db = client(Settings.MONGO_DB_NAME)
        
    #returning the db name
    @property
    def database(self):
        try:
            printing('accessing Datatabase collection')
            return self.db
        except Exception as e:
            print(f'An error occured: {e}')