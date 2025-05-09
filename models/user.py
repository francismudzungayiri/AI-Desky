from enum import Enum
from flask_login import UserMixin


# --- Enumerations for Status and Roles ---
class UserStatus(str, Enum):
    PENDING_VERIFICATION = "pending_verification"
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    DELETED = "deleted"


class UserRole(str, Enum):
    USER = "user"
    TECHNICIAN = "technician"
    ADMIN = "admin"
    

class User(UserMixin):
    """
    Wrapper class for Flask-Login.
    It holds the user data fetched from MongoDB.
    """
    def __init__(self, user_data:Dict):
        self.user_data = user_data
        
    
    @property
    def id(self)->str:
        return str(self.user_data.get('_id',""))
    
    @property
    def username(self)->str:
        return str(self.user_data.get("full_name",""))
    
    @property
    def email(self)->str:
        return str(self.user_data.get("email",""))
    
    
    @rproperty
    def roles(self)-> List[UserRole]:
        return [UserRole(role) for role in self.user_data.get("roles",[UserRole.USER.value])]
    
    @property 
    def is_admin(self)->bool:
        return UserRole.ADMIN in self.roles
    
    @property
    def is_active(self) -> bool:
        # Flask-Login uses this to determine if a user can log in.
        # You might want to check for PENDING_VERIFICATION or SUSPENDED status too.
        return self.status == UserStatus.ACTIVE
    
    # You can add other properties from UserInDB as needed
    def get_data(self) -> dict:
        """Returns the raw user data dictionary."""
        return self.user_data
    
    
    @staticmethod
    def get(user_id_str: str) -> Optional['User']:
        """
        Flask-Login's user_loader callback requires this method.
        It fetches a user by their ID (which is MongoDB's _id as a string).
        """
        if not ObjectId.is_valid(user_id_str):
            return None
        user_doc = users_collection.find_one({"_id": ObjectId(user_id_str)})
        if user_doc:
            return User(user_doc)
        return None
        
    
    
    
        
        