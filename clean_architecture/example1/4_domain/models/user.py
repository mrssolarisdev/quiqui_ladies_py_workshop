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

user = User(id=1, first_name="Mariana", last_name="Coelho", user_name="mari_coelho_09", status=UserStatusEnum.ACTIVE)
print(user.fullname)