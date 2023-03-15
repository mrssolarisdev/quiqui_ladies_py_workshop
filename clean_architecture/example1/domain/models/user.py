from enums.user_status_enum import UserStatusEnum

class User:
    def __init__(self, id: int, first_name: str, last_name: str, user_name: str, status: UserStatusEnum):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.status = status
        
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def set_user_status(self, status):
        self.status = status
        
# This is an element of the domain layer the lowest of all layers. It includes bussiness logic and data structures of the system.
# It basically encapsulates the core logic of our application. We can have various elements in this layer, like: enums, classes, 
# interfaces, etc. As long as they are responsible for enforcing bussiness specific logic and constraints.