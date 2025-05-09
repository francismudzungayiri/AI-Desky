import os
from pydantic import BaseModel



class Settings(BaseModel):
    
    MONGO_URI: str ="mongodb://localhost:27017"
    MONGO_DB_NAME: str = "AI DESKY"
    SECRET_KEY: str = f"{os.getenv('SECRET_KEY')}"
    PASSWORD_RESET_TOKEN_EXPIRE_MINUTES: int = 30
    
    
    
    
