class User:
    
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.name = user_data['name']
        self.password = user_data['password']
        
        