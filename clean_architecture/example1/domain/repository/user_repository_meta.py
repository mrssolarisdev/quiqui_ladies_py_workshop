from abc import ABC, abstractmethod

from models.user import User

class UserRepositoryMeta(ABC):
    @abstractmethod
    def add_new_user(self, user: User) -> User:
        raise NotImplementedError
    
    @abstractmethod
    def get_user(self, user_id: int) -> User:
        raise NotImplementedError
    
    @abstractmethod
    def delete_user(self, user_id: int) -> User:
        raise NotImplementedError
    # We are making all the functions raise an error so that in case anyone implements from this interface
    # and don't implement their own version of each function, they'll know they made a mistake.
    
# So, here we're defining an interface. The clean architecture principle says that the comunication in a system should
# flow from the outside to the inside, and not otherwise. So, all the inner layers should comunicate with outer layers
# using interfaces to avoid coupling (which makes our application hard to maintain, understand and test) and breaking 
# the principles, and that is what we're doing. 

# We need to be able to make our service(from the use case layer) talk to the the database layer (in the infra layer),
# in order to persist user data, but we can't do it directly. To make our service talk to the db, we're going to need
# a repository, which is in between this comunication. 

# And once we don't want to be dependent on the db implementation
# we are creating a interface from which each repository (of a specific db implementation having its own way of interacting 
# with the db) will implement. This way, even having different databases with different capabilities we should be able to execute each
# one of the defined capabilities we defined the user repositories should have. This is our way of guaranteeing that it doesn't
# matter what db we're using and if we've swaped one by the other at some point: the application should behave the same and the
# user repository being used should be able to ALWAYS execute the same expected and defined methods, but in its own way, giving the same results.