from configs.config import Settings
from pymongo import MongoClient


class Database:
    
    def __init__(self):
        try:
        
            self.client = MongoClient(Settings.MONGO_URI)
            self.db = self.client[Settings.MONGO_DB_NAME]
            print('Connected to MongoDB')
        except Exception as e:
            print(f'An error occured: {e}')
            raise ConnectionError('Failed to connect to MongoDB')
        
    
    def get_collection(self, collection_name):
        print('Collection accessed successfully')
        return self.db[collection_name]


    def insert_one(self,collection_name, data):
        result =  collection_name.insert_one(data)
        print('Data inserted successfully')
        return result
        
    
    def find_one(self, collection_name, query):
        print('Data found successfully')
        return self.db[collection_name].find_one(query)

    def find_all(self, collection_name, query):
        print('Data found successfully')
        return self.db[collection_name].find(query)
    
    def update_one(self, collection_name, query, data):
        self.db[collection_name].update_one(query, data)
        print('Data updated successfully')
        
        
    #returning the db name
#    @property
#    def database(self):
#        try:
#            printing('accessing Datatabase collection')
#            return self.db
#        except Exception as e:
#            print(f'An error occured: {e}')