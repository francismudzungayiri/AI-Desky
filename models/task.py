from services.database import DB


class Task:
    
    
    def __init__(self) -> None:
        db = DB()
        self.query_collection = db.database['Querries']
        
    
    #posting a Query into the db  
    def query_Posting(self, data)-> None:
        self.query_collection.insert_one(data)
        print('QUERY POSTED INTO DB SUCCESSFULLY')
        
        
        