import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGO_URI = "mongodb://localhost:27017"
    MONGO_DB_NAME = "AI_DESKY"
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    PASSWORD_RESET_TOKEN_EXPIRE_MINUTES = 30


    
    
    
    
