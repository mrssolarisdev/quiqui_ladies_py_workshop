from enum import Enum

class UserStatusEnum(Enum):
    ACTIVE = 1
    INACTIVE = 0
    
    @classmethod
    def _missing_(cls, value):
        raise NotImplementedError(f"{value} is not a valid value in the enum.")