from services.database import Database


class Task:
        
    def __init__(self) -> None:
        self.db = Database()
        self.task_collection = self.db.get_collection('tasks')
    
    
    #posting a Query into the db  
    def query_Posting(self, data)-> None:
        self.db.insert_one(self.task_collection, data)
        
        
        